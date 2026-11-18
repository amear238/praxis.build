#!/usr/bin/env python3
"""Tests for sameday.py (the same-day trend engine). Run: python3 -I -B research/trend-150k/test_sameday.py

Spec: 1 dollar a point, tick 1, commission 2, 1 tick slip. Minute bars are given as (HH:MM start, o, h, l, c) in ET.
"""
import datetime as dt
import os
import sys
import unittest
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdata  # noqa: E402
import sameday  # noqa: E402

ET = ZoneInfo("America/New_York")
DAY = 86400 * 1_000_000_000
SPEC = {"pv": 1.0, "tick": 1.0, "comm": 2.0, "slip_ticks": 1, "max_qty": 1000}
S = {"lookback": 2, "atr_days": 2, "stop_mult": 1.0, "trail_mult": None, "entry": "09:35", "flat": "15:55",
     "risk_pct": 1.0}


def daily(closes, rng=10.0, first="2024-03-01"):
    """Daily Adj bars on consecutive UTC dates from `first`, each with range `rng` around its close."""
    d0 = dt.date.fromisoformat(first)
    out = []
    for i, c in enumerate(closes):
        ts = int(dt.datetime.combine(d0 + dt.timedelta(days=i), dt.time(), dt.UTC).timestamp()) * 1_000_000_000
        b = mdata.Bar(ts, 1, c, c + rng / 2, c - rng / 2, c, 1)
        out.append(mdata.Adj(b, c, c + rng / 2, c - rng / 2, c))
    return out


def minutes(date, rows, iid=1):
    out = []
    for hhmm, o, h, l, c in rows:
        t = dt.datetime.combine(dt.date.fromisoformat(date), dt.time.fromisoformat(hhmm), ET)
        out.append(mdata.Bar(int(t.timestamp()) * 1_000_000_000, iid, o, h, l, c, 1))
    return out


# daily closes 100,100,110 on Mar 1-3: on Mar 4 the signal (110 vs 100, two bars back) is long, ATR(2) = 10
D_UP = daily([100, 100, 110])
D_DOWN = daily([110, 110, 100])


def one(mins, d=D_UP, settings=None, fill="kind"):
    st = dict(S, **(settings or {}))
    return sameday.per_contract(mins, d, SPEC, st, fill)


class PerContractTests(unittest.TestCase):
    def test_long_entry_at_entry_time_open_and_flat_exit(self):
        m = minutes("2024-03-04", [("09:34", 99, 100, 98, 99), ("09:35", 100, 101, 99, 100),
                                   ("12:00", 104, 106, 103, 105), ("15:55", 107, 108, 106, 107)])
        tr = one(m)
        self.assertEqual(len(tr), 1)
        t = tr[0]
        self.assertEqual((t["date"], t["side"], t["entry"], t["stop_initial"], t["dist"]),
                         ("2024-03-04", "long", 101.0, 91.0, 10.0))
        self.assertEqual((t["reason"], t["exit"]), ("flat", 106.0))      # 15:55 open 107 - 1 tick
        self.assertEqual(t["worst"], -2.0)        # lowest low while open: 99 on the entry bar, 99 - 101
        self.assertEqual(t["points"], 5.0)

    def test_short_side_from_down_trend(self):
        m = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("15:55", 95, 96, 94, 95)])
        t = one(m, D_DOWN)[0]
        self.assertEqual((t["side"], t["entry"], t["stop_initial"], t["exit"]), ("short", 99.0, 109.0, 96.0))

    def test_stop_models_and_gap(self):
        m = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("10:00", 95, 96, 85, 86), ("15:55", 86, 87, 85, 86)])
        k, mid, h = one(m)[0], one(m, fill="midpoint")[0], one(m, fill="harsh-stops")[0]
        self.assertEqual((k["reason"], k["exit"], k["gap"]), ("stop", 90.0, False))   # stop 91 - 1
        self.assertEqual(mid["exit"], 88.0)                                         # (91 + 85) / 2
        self.assertEqual(h["exit"], 85.0)
        g = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("10:00", 89, 90, 85, 86), ("15:55", 86, 87, 85, 86)])
        kg = one(g)[0]
        self.assertTrue(kg["gap"])
        self.assertEqual(kg["exit"], 88.0)                                           # open 89 - 1

    def test_trailing_stop(self):
        m = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("10:00", 100, 120, 100, 119),
                                   ("10:01", 119, 119, 110, 111), ("15:55", 111, 112, 110, 111)])
        t = one(m, settings={"trail_mult": 0.5})[0]
        # best 120 at the 10:00 close -> stop 120 - 5 = 115; hit on 10:01 -> kind 114
        self.assertEqual((t["reason"], t["exit"]), ("stop", 114.0))

    def test_no_trade_without_entry_bar_or_history(self):
        self.assertEqual(one(minutes("2024-03-04", [("09:34", 1, 1, 1, 1), ("15:55", 1, 1, 1, 1)])), [])
        self.assertEqual(one(minutes("2024-03-02", [("09:35", 1, 1, 1, 1), ("15:55", 1, 1, 1, 1)])), [])

    def test_last_bar_before_flat_closes_at_its_close_when_no_flat_bar(self):
        m = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("13:00", 104, 105, 103, 104)])
        t = one(m)[0]
        self.assertEqual((t["reason"], t["exit"]), ("flat", 104))   # the close, no slippage (PLAN amendment)

    def test_signal_uses_only_days_before_the_trade_date(self):
        # a daily bar dated the trade date itself (close 50) must not flip the signal
        d = daily([100, 100, 110, 50])
        m = minutes("2024-03-04", [("09:35", 100, 101, 99, 100), ("15:55", 101, 102, 100, 101)])
        self.assertEqual(one(m, d)[0]["side"], "long")


class TouchTests(unittest.TestCase):
    def test_uses_the_same_touch_and_sign_as_weekly(self):
        self.assertTrue(sameday._reaches(1.3033, 13033 * 0.0001, 0.0001, "short"))
        self.assertEqual(sameday._sign(0.1 + 0.2, 0.3, 0.0001), 0)

    def test_net_uses_the_unrounded_points(self):
        # 0.3 - 0.1 is 0.19999999999999998: net at 50 contracts, pv 12.5 must be 124.99999.. -> 125.00, the same
        # money as (exit - entry) computed directly
        x = {"points": round(0.3 - 0.1, 10), "exit": 0.3, "entry": 0.1, "side": "long"}
        self.assertEqual(sameday._net(x, 12.5, 0.0, 50), round((0.3 - 0.1) * 12.5 * 50, 2))


class AccountTests(unittest.TestCase):
    def pc(self, date, points, worst, dist=10.0):
        return {"market": "X", "date": date, "side": "long", "entry": 100.0, "exit": 100.0 + points,
                "stop_initial": 100.0 - dist, "dist": dist, "reason": "flat", "gap": False,
                "points": points, "worst": worst}

    def test_sizing_from_balance_at_day_start_and_day_records(self):
        pcs = {"X": [self.pc("2024-03-04", 5.0, -3.0), self.pc("2024-03-05", -11.0, -11.0)]}
        r = sameday.account(pcs, {"X": SPEC}, 1.0, start=10000.0)
        t0, t1 = r["trades"]
        # loss a contract = (10 + 1) + 2 = 13 -> 7 contracts on 10,000
        self.assertEqual((t0["qty"], t0["net"]), (7, 5.0 * 7 - 14.0))
        self.assertEqual(r["days"][0], {"date": "2024-03-04", "start": 10000.0, "end": 10021.0,
                                        "low": 10000.0 - 3 * 7 - 14})
        self.assertEqual(t1["qty"], 7)                       # floor(100.21 / 13)
        self.assertEqual(r["days"][1]["start"], 10021.0)

    def test_skip_under_one_contract(self):
        r = sameday.account({"X": [self.pc("2024-03-04", 5.0, -3.0)]}, {"X": SPEC}, 1.0, start=500.0)
        self.assertEqual(r["trades"], [])
        self.assertEqual(r["skipped"][0]["reason"], "under one contract")


if __name__ == "__main__":
    unittest.main(verbosity=1)
