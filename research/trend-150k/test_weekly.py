#!/usr/bin/env python3
"""Tests for weekly.py (the multi-week trend engine). Run: python3 -I -B research/trend-150k/test_weekly.py

Synthetic daily bars with hand-worked fills. Spec used: 1 dollar a point, tick 1, commission 2, 1 tick slip.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdata  # noqa: E402
import weekly  # noqa: E402

DAY = 86400 * 1_000_000_000
SPEC = {"pv": 1.0, "tick": 1.0, "comm": 2.0, "slip_ticks": 1, "max_qty": 1000}


def bars(rows, iid=1):
    """rows: (open, high, low, close) per day from day 0 -> [Adj] with no roll adjustment."""
    out = []
    for i, (o, h, l, c) in enumerate(rows):
        b = mdata.Bar(i * DAY, iid, o, h, l, c, 1)
        out.append(mdata.Adj(b, o, h, l, c))
    return out


def flat_then(rows_after, n_flat=3, level=100.0, rng=10.0):
    """n_flat quiet days around `level` (range `rng`), then the given rows."""
    quiet = [(level, level + rng / 2, level - rng / 2, level)] * n_flat
    return bars(quiet + rows_after)


S = {"lookback": 2, "atr_days": 2, "stop_mult": 1.0, "trail_mult": None, "risk_pct": 1.0}


def run(rows, settings=None, fill="kind", start=10000.0, rolls=None, spec=SPEC):
    st = dict(S, **(settings or {}))
    return weekly.run({"X": rows}, {"X": spec}, st, fill=fill, start=start, rolls={"X": rolls or []})


class SignalTests(unittest.TestCase):
    def test_no_trade_before_lookback_and_atr_exist(self):
        r = run(bars([(100, 105, 95, 100)] * 2))
        self.assertEqual(r["trades"], [])

    def test_long_entry_next_open_with_stop_and_size(self):
        # days 0-2 quiet at 100 (range 10). day 3 closes 110 > close 2 days back (100): long.
        # ATR(2) at day 3 = mean(range day 2, day 3) = (10 + 10) / 2 = 10 -> dist 10.
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (118, 119, 117, 118)])
        r = run(rows)
        t = r["trades"][0]
        self.assertEqual(t["side"], "long")
        self.assertEqual(t["entry_day"], 4)
        self.assertEqual(t["entry"], 112.0)            # open 111 + 1 tick
        self.assertEqual(t["stop_initial"], 102.0)     # entry - dist 10
        # loss per contract = (10 + 1) * 1 + 2 = 13; risk 1% of 10,000 = 100 -> 7 contracts
        self.assertEqual(t["qty"], 7)
        self.assertEqual(t["planned_cost"], 91.0)

    def test_short_signal_mirrors(self):
        rows = flat_then([(100, 100, 85, 90), (89, 91, 80, 82), (82, 83, 81, 82)])
        r = run(rows)
        t = r["trades"][0]
        self.assertEqual(t["side"], "short")
        self.assertEqual(t["entry"], 88.0)             # open 89 - 1 tick
        # ATR(2) at day 3 = (10 + 15) / 2 = 12.5 -> dist on the tick grid, rounded down = 12
        self.assertEqual(t["stop_initial"], 100.0)


class StopTests(unittest.TestCase):
    def test_stop_fill_models(self):
        # long from 112, stop 102. day 5 low 95 reaches it; opens 108 (above the stop).
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (108, 109, 95, 96)])
        k = run(rows, fill="kind")["trades"][0]
        m = run(rows, fill="midpoint")["trades"][0]
        h = run(rows, fill="harsh-stops")["trades"][0]
        self.assertEqual((k["reason"], k["exit_day"], k["exit"], k["gap"]), ("stop", 5, 101.0, False))
        self.assertEqual(m["exit"], 98.0)               # halfway 102..95 = 98.5, worse tick for a sell = 98
        self.assertEqual(h["exit"], 95.0)
        self.assertEqual(k["net"], (101.0 - 112.0) * 7 - 2.0 * 7)

    def test_gap_through_stop_fills_from_the_open(self):
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (99, 100, 90, 92)])
        k = run(rows, fill="kind")["trades"][0]
        m = run(rows, fill="midpoint")["trades"][0]
        self.assertTrue(k["gap"])
        self.assertEqual(k["exit"], 98.0)               # open 99 - 1 tick
        self.assertEqual(m["exit"], 94.0)               # halfway 99..90 = 94.5 -> 94

    def test_stop_on_entry_bar(self):
        rows = flat_then([(100, 115, 105, 110), (111, 112, 100, 101)])
        t = run(rows)["trades"][0]
        self.assertEqual((t["entry_day"], t["exit_day"], t["reason"]), (4, 4, "stop"))

    def test_waits_a_day_after_a_stop_then_reenters_if_signal_holds(self):
        rows = flat_then([(100, 115, 105, 110), (111, 112, 100, 101),   # day 4 stopped
                          (101, 130, 101, 125),                          # day 5: no decision on day 4, signal on day 5
                          (126, 128, 124, 127)])                         # day 6: re-entry at the open
        tr = run(rows)["trades"]
        self.assertEqual(len(tr), 2)
        self.assertEqual(tr[1]["entry_day"], 6)


class TrailAndReverseTests(unittest.TestCase):
    def test_trail_moves_only_toward_price(self):
        rows = flat_then([(100, 115, 105, 110), (111, 130, 110, 128),    # entry day 4, best 130
                          (128, 129, 120, 121),                          # stop trailed to 130 - 5 = 125 at day-4 close -> hit
                          ])
        t = run(rows, {"trail_mult": 0.5})["trades"][0]
        self.assertEqual(t["reason"], "stop")
        self.assertEqual(t["exit_day"], 5)
        self.assertEqual(t["exit"], 124.0)              # kind: 125 - 1 tick

    def test_opposite_signal_reverses_at_next_open(self):
        rows = flat_then([(100, 115, 105, 110), (111, 116, 106, 112),    # long from day 4
                          (112, 113, 103, 104),                          # day 5 close 104 < close day 3 (110): short
                          (104, 106, 100, 101)])                         # day 6 open: exit long, enter short
        st = {"stop_mult": 2.0}
        tr = run(rows, st)["trades"]
        self.assertEqual([t["side"] for t in tr], ["long", "short"])
        self.assertEqual((tr[0]["reason"], tr[0]["exit_day"], tr[0]["exit"]), ("signal", 6, 103.0))
        self.assertEqual((tr[1]["entry_day"], tr[1]["entry"]), (6, 103.0))


class MoneyTests(unittest.TestCase):
    def test_roll_cost_charged_per_roll_held_through(self):
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (118, 125, 117, 124), (110, 111, 90, 92)])
        base = run(rows)["trades"][0]
        rolled = run(rows, rolls=[mdata.Roll(5 * DAY, 1, 2, 0.0)])["trades"][0]
        # one roll: commission 2 + 2 ticks of slippage (2 x 1) = 4 dollars a contract
        self.assertAlmostEqual(base["net"] - rolled["net"], 4.0 * base["qty"])
        self.assertEqual(rolled["rolls"], 1)

    def test_under_one_contract_is_skipped(self):
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118)])
        r = run(rows, start=500.0)                      # 1% = 5 dollars < 13 a contract
        self.assertEqual(r["trades"], [])
        self.assertEqual(r["skipped"][0]["reason"], "under one contract")

    def test_days_track_equity_and_low(self):
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (118, 119, 117, 118)])
        r = run(rows)
        d = {x["day"]: x for x in r["days"]}
        # day 4: long 7 from 112, close 118: +42 open, minus commission 14 counted at once -> 10,028
        self.assertEqual(d[4]["end"], 10000.0 + (118 - 112) * 7 - 14)
        # low marks the day's low 109: (109 - 112) * 7 - 14 = -35
        self.assertEqual(d[4]["low"], 10000.0 - 35.0)
        self.assertEqual(d[5]["start"], d[4]["end"])

    def test_reproducible_digest(self):
        rows = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (108, 109, 95, 96)])
        self.assertEqual(run(rows)["digest"], run(rows)["digest"])


class PortfolioTests(unittest.TestCase):
    def test_two_markets_share_one_balance(self):
        up = flat_then([(100, 115, 105, 110), (111, 120, 109, 118), (108, 109, 95, 96)])
        r = weekly.run({"A": up, "B": up}, {"A": SPEC, "B": SPEC}, S, fill="kind", start=10000.0,
                       rolls={"A": [], "B": []})
        self.assertEqual([t["market"] for t in r["trades"]], ["A", "B"])
        self.assertEqual(r["days"][-1]["end"], 10000.0 + 2 * r["trades"][0]["net"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
