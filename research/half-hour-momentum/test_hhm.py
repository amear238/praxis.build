#!/usr/bin/env python3
"""Tests for candidate 3 (first half hour into the last half hour). Every simulated order is rechecked
against the locked rule from the raw bars, without the simulator's loop.
Run: python3 -I -B research/half-hour-momentum/test_hhm.py"""
import datetime as dt
import math
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hhm as H   # noqa: E402

R, O, mk = H.R, H.O, H.mk
HAVE = os.path.exists(R.DATA)


class Bar(object):
    def __init__(self, day, mod, o, h, l, c):
        self.dt = dt.datetime(2024, 1, day, mod // 60, mod % 60)
        self.mod, self.o, self.h, self.l, self.c, self.v = mod, o, h, l, c, 1


class Sess(object):
    def __init__(self, day, bars):
        self.date, self.bars = "2024-01-%02d" % day, bars


class Mkt(object):
    def __init__(self, sessions):
        self.sessions, self.start, self.end = sessions, sessions[0].date, sessions[-1].date


def day(d, open_px, ten_close, late=None, rng=10.0):
    """A full session of flat bars at open_px, a 10:00 close of ten_close, a last half hour of range `rng`,
    and optional (mod -> (o, h, l, c)) overrides from 15:31 on."""
    bars = []
    for mod in range(571, 961):
        px = ten_close if mod >= 600 else open_px
        b = Bar(d, mod, px, px, px, px)
        if mod == 931:
            b.h, b.l = px + rng / 2, px - rng / 2
        if late and mod in late:
            b.o, b.h, b.l, b.c = late[mod]
        bars.append(b)
    return Sess(d, bars)


class SyntheticRules(unittest.TestCase):
    def warm(self):
        return [day(d, 100, 100) for d in range(1, 15)]   # 14 sessions, range 10, no signal (r == 0)

    def test_warmup_and_no_signal(self):
        sim = H.Sim().run(Mkt(self.warm()))
        self.assertEqual((len(sim.trades), sim.no_signal, sim.warmup), (0, 14, 0))
        # first session has no previous close -> no signal

    def test_long_held_to_flat(self):
        s = day(15, 100, 101, late={960: (103, 104, 102, 103)})
        sim = H.Sim().run(Mkt(self.warm() + [s]))
        t = sim.trades[0]
        self.assertEqual((t["side"], t["entry"], t["dist"], t["stop"]), (1, 101.5, 10.0, 91.5))
        self.assertEqual((t["reason"], t["exit"], t["exit_dt"][-8:]), ("flat 15:59", 102.5, "16:00:00"))
        self.assertEqual(t["qty"], int(500 / 20.0))

    def test_short_stopped(self):
        s = day(15, 100, 99, late={940: (99, 112, 99, 111)})
        sim = H.Sim().run(Mkt(self.warm() + [s]))
        t = sim.trades[0]
        self.assertEqual((t["side"], t["entry"], t["stop"], t["reason"], t["exit"]), (-1, 98.5, 108.5, "stop", 109.0))

    def test_stop_rounds_up_to_tick(self):
        self.assertEqual(H.stop_distance([10.1] * 14), 10.25)
        self.assertEqual(H.stop_distance([10.0] * 14), 10.0)

    def test_early_close_no_trade(self):
        s = day(15, 100, 101)
        s.bars = [b for b in s.bars if b.mod <= 13 * 60]
        sim = H.Sim().run(Mkt(self.warm() + [s]))
        self.assertEqual((sim.trades, sim.no_window), ([], 1))


@unittest.skipUnless(HAVE, "data file absent")
class OrdersMatchTheRule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mk.load_market(R.DATA, session_start=R.SESSION_START)
        cls.sim = H.Sim().run(cls.m)

    def test_every_order(self):
        m, sim = self.m, self.sim
        by_date = {t["entry_dt"][:10]: t for t in sim.trades}
        self.assertEqual(len(by_date), len(sim.trades), "two trades on one day")
        self.assertGreater(len(sim.trades), 1000)
        ranges, prev, bal = [], None, R.START
        counts = {"no_window": 0, "no_signal": 0, "warmup": 0, "skipped": 0}
        for s in m.sessions:
            mods = [b.mod for b in s.bars]
            t = by_date.get(s.date)
            ten = [b for b in s.bars if b.mod == 600]
            if 930 not in mods or not any(x > 930 for x in mods):
                counts["no_window"] += 1
                self.assertIsNone(t)
            else:
                r = ten[0].c / prev.bars[-1].c - 1 if (prev and ten) else 0.0
                side = 1 if r > 0 else -1 if r < 0 else 0
                if side == 0:
                    counts["no_signal"] += 1
                    self.assertIsNone(t)
                elif len(ranges) < 14:
                    counts["warmup"] += 1
                    self.assertIsNone(t)
                else:
                    dist = math.ceil(sum(ranges[-14:]) / 14.0 / 0.25 - 1e-9) * 0.25
                    k = next(i for i, b in enumerate(s.bars) if b.mod > 930)
                    eb = s.bars[k]
                    entry = min(max(eb.o + side * 0.5, eb.l), eb.h)
                    qty = int(0.01 * bal / (dist * 2) + 1e-9)
                    if qty < 1:
                        counts["skipped"] += 1
                        self.assertIsNone(t)
                    else:
                        self.assertIsNotNone(t, s.date)
                        stop = entry - side * dist
                        self.assertEqual((t["side"], t["entry"], t["dist"], t["stop"], t["qty"]),
                                         (side, entry, dist, stop, qty), s.date)
                        self.assertEqual(t["entry_dt"], eb.dt.isoformat(" "))
                        self.assertLessEqual(t["planned_loss"], 0.01 * bal + 1e-6)
                        reason = px = when = None
                        for j in range(k, len(s.bars)):
                            b = s.bars[j]
                            if (b.l <= stop) if side == 1 else (b.h >= stop):
                                reason, px, when = "stop", O.stop_fill(b, side, stop), b.dt
                                break
                            if j == len(s.bars) - 1:
                                reason, px, when = "session close", min(max(b.c - side * 0.5, b.l), b.h), b.dt
                                break
                            if b.mod >= 959:
                                nb = s.bars[j + 1]
                                reason, px, when = "flat 15:59", min(max(nb.o - side * 0.5, nb.l), nb.h), nb.dt
                                break
                        self.assertEqual((t["reason"], t["exit"], t["exit_dt"]), (reason, px, when.isoformat(" ")), s.date)
                        net = (px - entry) * side * qty * 2 - 1.90 * qty
                        self.assertAlmostEqual(t["net"], round(net, 2), places=2)
                        bal += t["net"]
                        self.assertAlmostEqual(t["balance"], round(bal, 2), places=1)
            sub = [b for b in s.bars if 931 <= b.mod <= 960]
            if 931 in mods and 960 in mods:
                ranges.append(max(b.h for b in sub) - min(b.l for b in sub))
            prev = s
        self.assertEqual(counts, {"no_window": sim.no_window, "no_signal": sim.no_signal, "warmup": sim.warmup,
                                  "skipped": sim.skipped})

    def test_reproduces(self):
        self.assertEqual(R.digest(H.Sim().run(self.m)), R.digest(self.sim))

    def test_periods_split_cleanly(self):
        seen = H.Sim(period=R.SEEN).run(self.m)
        unseen = H.Sim(period=R.UNSEEN).run(self.m)
        self.assertTrue(all(t["entry_dt"][:10] <= R.SEEN[1] for t in seen.trades))
        self.assertTrue(all(t["entry_dt"][:10] >= R.UNSEEN[0] for t in unseen.trades))

    def test_day_lows_never_above_end(self):
        for d in self.sim.days:
            self.assertLessEqual(d["low"], min(d["start"], d["end"]) + 1e-6)


if __name__ == "__main__":
    unittest.main()
