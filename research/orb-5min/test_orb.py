#!/usr/bin/env python3
"""Tests for candidate 2 (5-minute ORB). Every simulated order is checked against the locked rule,
independently of the simulator's loop. Run: python3 -I -B research/orb-5min/test_orb.py"""
import datetime as dt
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import orb as O   # noqa: E402

R, mk = O.R, O.mk
HAVE = os.path.exists(R.DATA)
_M = {}


def market():
    if "m" not in _M:
        _M["m"] = mk.load_market(R.DATA, session_start=R.SESSION_START)
    return _M["m"]


class Bar(object):
    def __init__(self, mod, o, h, l, c):
        self.dt = dt.datetime(2024, 1, 2, mod // 60, mod % 60)
        self.mod, self.o, self.h, self.l, self.c, self.v = mod, o, h, l, c, 1


class Sess(object):
    def __init__(self, bars, date="2024-01-02"):
        self.bars, self.date = bars, date


class Mkt(object):
    def __init__(self, sessions):
        self.sessions = sessions
        self.start, self.end = sessions[0].date, sessions[-1].date


def flat_day(o5, c5, lo5, hi5, path):
    """Opening bars 09:31-09:35 shaped by (open, close, low, high), then `path` bars from 09:36."""
    bars = [Bar(571, o5, hi5, lo5, o5)] + [Bar(m, o5, o5, o5, o5) for m in range(572, 575)] + [Bar(575, o5, o5, o5, c5)]
    bars[-1].h, bars[-1].l = max(o5, c5), min(o5, c5)
    for k, (o, h, l, c) in enumerate(path):
        bars.append(Bar(576 + k, o, h, l, c))
    return bars


class SyntheticRules(unittest.TestCase):
    def test_long_stopped_at_range_low(self):
        bars = flat_day(100, 104, 95, 106, [(104, 105, 94, 95)])
        sim = O.Sim().run(Mkt([Sess(bars)]))
        t = sim.trades[0]
        self.assertEqual((t["side"], t["entry"], t["stop"], t["reason"]), (1, 104.5, 95, "stop"))
        self.assertEqual(t["exit"], 94.5)

    def test_short_on_down_open_and_target(self):
        # short at 99.5 (100 - slip); stop at 106; dist 6.5; target 99.5 - 65 = 34.5
        bars = flat_day(105, 100, 98, 106, [(100, 100, 99, 99), (99, 99, 30, 31)])
        sim = O.Sim().run(Mkt([Sess(bars)]))
        t = sim.trades[0]
        self.assertEqual((t["side"], t["entry"], t["stop"], t["reason"]), (-1, 99.5, 106, "target"))
        self.assertAlmostEqual(t["target"], 34.5)
        self.assertEqual(t["exit"], 35.0)

    def test_doji_no_trade(self):
        bars = flat_day(100, 100, 95, 106, [(100, 101, 99, 100)])
        sim = O.Sim().run(Mkt([Sess(bars)]))
        self.assertEqual((sim.trades, sim.no_signal), ([], 1))

    def test_stop_before_target_on_same_bar(self):
        bars = flat_day(100, 104, 95, 106, [(104, 300, 90, 200)])
        sim = O.Sim().run(Mkt([Sess(bars)]))
        self.assertEqual(sim.trades[0]["reason"], "stop")

    def test_flat_at_1559_filled_at_1600(self):
        path = [(104, 105, 103, 104)] * (959 - 576 + 1) + [(110, 111, 109, 110)]
        bars = flat_day(100, 104, 95, 106, path)
        sim = O.Sim().run(Mkt([Sess(bars)]))
        t = sim.trades[0]
        self.assertEqual((t["reason"], t["exit_dt"][-8:], t["exit"]), ("flat 15:59", "16:00:00", 109.5))

    def test_leverage_cap_binds(self):
        # at a price near 20,000 with a 4.5-point stop, 1% of 50,000 wants 55 MNQ; the 4x cap allows
        # 4 * 50,000 / (20,004.5 * 2) = 4 contracts, so the cap binds
        bars = flat_day(20000, 20004, 19999, 20006, [(20004, 20005, 20004, 20005)] + [(20005, 20005, 20005, 20005)])
        sim = O.Sim().run(Mkt([Sess(bars)]))
        t = sim.trades[0]
        self.assertEqual(t["qty"], int(4 * 50000 / (t["entry"] * 2)))
        self.assertTrue(t["capped"])


@unittest.skipUnless(HAVE, "data file absent")
class OrdersMatchTheRule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = market()
        cls.sim = O.Sim().run(cls.m)

    def test_every_order(self):
        m, sim = self.m, self.sim
        self.assertGreater(len(sim.trades), 1000)
        bal = R.START
        seen_days = set()
        for t in sim.trades:
            n, i0 = m.index[dt.datetime.fromisoformat(t["entry_dt"])]
            s = m.sessions[n - 1]
            self.assertNotIn(s.date, seen_days, "two trades on one day")
            seen_days.add(s.date)
            first5 = s.bars[:5]
            o5, c5 = first5[0].o, first5[-1].c
            hi5, lo5 = max(b.h for b in first5), min(b.l for b in first5)
            side = 1 if c5 > o5 else -1
            self.assertNotEqual(c5, o5)
            self.assertEqual(t["side"], side)
            self.assertEqual(i0, 5, "entry is not the first bar after the opening range")
            self.assertEqual(s.bars[i0].mod, 577 if s.date == "2026-04-02" else 576)
            eb = s.bars[i0]
            self.assertEqual(t["entry"], min(max(eb.o + side * R.SLIP, eb.l), eb.h))
            self.assertEqual(t["stop"], lo5 if side == 1 else hi5)
            dist = (t["entry"] - t["stop"]) * side
            self.assertGreater(dist, 0)
            self.assertAlmostEqual(t["target"], t["entry"] + side * 10 * dist, places=6)
            # size: the most contracts within 1% of the balance before entry and within 4x leverage
            want = min(int(0.01 * bal / (dist * 2) + 1e-9), int(4 * bal / (t["entry"] * 2) + 1e-9))
            self.assertEqual(t["qty"], want)
            self.assertLessEqual(t["planned_loss"], 0.01 * bal + 1e-6)
            # exit: the first bar from entry on that reaches the stop (stop wins ties), else the target,
            # else flat at 15:59 filled on the next bar, else the session's last bar
            exp_reason = exp_exit = exp_dt = None
            for j in range(i0, len(s.bars)):
                b = s.bars[j]
                if (b.l <= t["stop"]) if side == 1 else (b.h >= t["stop"]):
                    exp_reason, exp_exit, exp_dt = "stop", O.stop_fill(b, side, t["stop"]), b.dt
                    break
                if (b.h >= t["target"]) if side == 1 else (b.l <= t["target"]):
                    exp_reason, exp_exit, exp_dt = "target", O.target_fill(b, side, t["target"]), b.dt
                    break
                if j == len(s.bars) - 1:
                    exp_reason, exp_dt = "session close", b.dt
                    exp_exit = min(max(b.c - side * R.SLIP, b.l), b.h)
                    break
                if b.mod >= R.FLAT_MOD:
                    nb = s.bars[j + 1]
                    exp_reason, exp_dt = "flat 15:59", nb.dt
                    exp_exit = min(max(nb.o - side * R.SLIP, nb.l), nb.h)
                    break
            self.assertEqual((t["reason"], t["exit"], t["exit_dt"]), (exp_reason, exp_exit, exp_dt.isoformat(" ")),
                             t["entry_dt"])
            net = (t["exit"] - t["entry"]) * side * t["qty"] * 2 - 1.90 * t["qty"]
            self.assertAlmostEqual(t["net"], round(net, 2), places=2)
            bal += t["net"]
            self.assertAlmostEqual(t["balance"], round(bal, 2), places=1)

    def test_every_untraded_day_is_explained(self):
        traded = {t["entry_dt"][:10] for t in self.sim.trades}
        dojis = skips = 0
        for s in self.m.sessions:
            if s.date in traded:
                continue
            if s.bars[0].o == s.bars[4].c:
                dojis += 1
            else:
                skips += 1
        self.assertEqual((dojis, skips), (self.sim.no_signal, self.sim.skipped))

    def test_reproduces(self):
        again = O.Sim().run(self.m)
        self.assertEqual(R.digest(again), R.digest(self.sim))

    def test_periods_split_cleanly(self):
        seen = O.Sim(period=R.SEEN).run(self.m)
        unseen = O.Sim(period=R.UNSEEN).run(self.m)
        self.assertTrue(all(t["entry_dt"][:10] <= R.SEEN[1] for t in seen.trades))
        self.assertTrue(all(t["entry_dt"][:10] >= R.UNSEEN[0] for t in unseen.trades))

    def test_day_lows_never_above_end(self):
        for d in self.sim.days:
            self.assertLessEqual(d["low"], min(d["start"], d["end"]) + 1e-6)


if __name__ == "__main__":
    unittest.main()
