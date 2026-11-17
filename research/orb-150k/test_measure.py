#!/usr/bin/env python3
"""Tests for measure.py. Run: python3 -I -B research/orb-150k/test_measure.py

Hand-built days from test_orb_engine.py; the shuffled drawdown is checked on four hand-made day rows whose
shuffle order is worked out here with the same random.Random(seed).shuffle the module uses.
"""
import datetime as dt
import os
import random
import sys
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import measure as ms            # noqa: E402
import orb_engine as en         # noqa: E402
import globex as g              # noqa: E402  (on the path through orb_engine's import)
import test_orb_engine as te    # noqa: E402

LOSS = (-1.0, -1.0)             # (end - start, low - start) in R
WIN = (5.0, -0.5)
ROWS = [LOSS, LOSS, LOSS, WIN]


def order_of(seed):
    x = list(ROWS)
    random.Random(seed).shuffle(x)
    return x


class Grid(unittest.TestCase):
    def test_grid_has_108_unique_valid_settings(self):
        grid = ms.grid()
        self.assertEqual(len(grid), 108)
        self.assertEqual(len({s["name"] for s in grid}), 108)
        keys = {(s["or_minutes"], s["entry"], tuple(s["stop"]), tuple(s["exit"])) for s in grid}
        self.assertEqual(len(keys), 108)
        for s in grid:
            en.validate(s)
            self.assertEqual((s["sides"], s["max_or_atr"], s["risk_pct"]), ("both", None, 1.0))
            self.assertEqual(s["entry_until"], "11:00" if s["entry"] == "break" else None)
        self.assertEqual({s["or_minutes"] for s in grid}, {5, 15, 30})
        self.assertEqual({tuple(s["stop"]) for s in grid}, {("far_side",), ("or_frac", 0.5), ("atr_frac", 0.10)})
        self.assertEqual({tuple(s["exit"]) for s in grid},
                         {("hold_to_flat",), ("target_r", 3), ("target_r", 5), ("target_r", 10), ("trail_r", 1),
                          ("trail_r", 2)})
        self.assertIn("or5-direction-far_side-target_r10", {s["name"] for s in grid})


class Drawdown(unittest.TestCase):
    def test_dd975_known_sequence(self):
        # Win first: hwm 0, the win day dips to -0.5 (drop 0.5), ends at 5; then three losing days end at 4, 3,
        # 2, each dipping to its end: drops 1, 2, 3. Largest 3.0.
        # Win last: drops 1, 2, 3, then the win day dips to -3.5 below a high of 0: 3.5.
        seeds = {}
        for seed in range(1000):
            o = order_of(seed)
            if o[0] == WIN and "first" not in seeds:
                seeds["first"] = seed
            if o[-1] == WIN and "last" not in seeds:
                seeds["last"] = seed
        self.assertEqual(ms.dd975_r(ROWS, runs=1, seed=seeds["first"]), 3.0)
        self.assertEqual(ms.dd975_r(ROWS, runs=1, seed=seeds["last"]), 3.5)
        # Win second: drop 1 (first loss), then the win day dips to -1.5 (drop 1.5), ends 4; hwm 4; then
        # 3 and 2: drops 1 and 2. Largest 2.0.
        second = next(s for s in range(1000) if order_of(s)[1] == WIN)
        self.assertEqual(ms.dd975_r(ROWS, runs=1, seed=second), 2.0)
        # The 97.5th percentile is index ceil(0.975 * runs) - 1 of the sorted maxima: with 40 runs, the 39th.
        rng = random.Random(7)
        maxima = []
        for _ in range(40):
            x = list(ROWS)
            rng.shuffle(x)
            maxima.append(ms._max_drop(x))
        self.assertEqual(ms.dd975_r(ROWS, runs=40, seed=7), sorted(maxima)[38])
        self.assertEqual(ms.dd975_r(ROWS), ms.dd975_r(ROWS))


class Money(unittest.TestCase):
    def test_safe_dollars_and_projection(self):
        safe, projected, headroom = ms.projection(net_r=60.0, dd975=15.0, measured_days=700, full_days=1350)
        self.assertEqual(safe, 300.0)                                  # 4500 / 15
        self.assertAlmostEqual(projected, 60.0 / 700 * 1350 * 300.0, places=9)   # 34,714.29
        self.assertAlmostEqual(headroom, projected / 9000.0, places=12)
        self.assertEqual(ms.projection(net_r=-5.0, dd975=0.0, measured_days=700, full_days=1350), (None, None, None))


def fixture():
    """14 quiet days, then three trade days in December 2023 and one in January 2024."""
    dates = te.weekdays(14, dt.date(2023, 11, 20))
    days = [te.make_day(x, [("10:00", 100, 120, 100, 100)]) for x in dates]
    tail = [dt.date(2023, 12, 27), dt.date(2023, 12, 28), dt.date(2023, 12, 29), dt.date(2024, 1, 2)]
    rows = [te.STD + [("10:00", 111.5, 141.5, 111.5, 120), ("10:10", 120, 141.75, 119, 140)],   # 2R target
            te.STD + [("10:00", 100, 101, 90, 92)],                                            # stop
            te.STD,                                                                            # flat
            te.STD + [("10:00", 111.5, 142, 111.5, 140)]]                                      # 2024: target
    return days + [te.make_day(x, r) for x, r in zip(tail, rows)]


class Measure(unittest.TestCase):
    def test_uses_no_day_after_2023(self):
        days = fixture()
        s = dict(te.settings(exit=["target_r", 2]), name="t")
        row = ms.measure_one(s, days, full_days=100)
        self.assertEqual(row["trades"], 3)
        self.assertEqual(set(row["net_r_by_year"]), {"2021", "2022", "2023"})
        self.assertEqual(row["measured_days"], 17)
        # One micro, midpoint fills: target +30 points = 58.10 on 32.90; stop at 93.25 = -38.40; flat -2.90.
        self.assertAlmostEqual(row["net_r"], (58.1 - 38.4 - 2.9) / 32.9, places=12)
        self.assertEqual((row["win_pct"], row["longest_losing_run"]), (100.0 / 3, 2))
        self.assertAlmostEqual(row["avg_winner_r"], 58.1 / 32.9, places=12)
        # The calendar starts on the first day (far side): 14 quiet days with no trade, then trades.
        self.assertEqual(row["max_gap_days"], 14)
        # The atr rules start on the 15th day: no gap before the first trade.
        row = ms.measure_one(dict(s, stop=["atr_frac", 0.6]), days, full_days=100)
        self.assertEqual((row["trades"], row["max_gap_days"]), (3, 0))
        # The loader is asked for nothing after 2023.
        with mock.patch.object(g, "load_days", return_value=days) as ld:
            got, full = ms.load("x")
        self.assertEqual(ld.call_args_list[0], mock.call("x", end="2023-12-31"))
        self.assertTrue(all(d.date <= "2023-12-31" for d in got))
        self.assertEqual(full, 18)


if __name__ == "__main__":
    unittest.main()
