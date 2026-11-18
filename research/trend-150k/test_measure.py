#!/usr/bin/env python3
"""Tests for measure.py's pieces (python3 -I -B test_measure.py)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measure  # noqa: E402
from mdata import Adj, Bar  # noqa: E402

DAY_NS = 86400 * 1_000_000_000
SPEC = {"pv": 2.0, "tick": 0.25, "comm": 1.90, "slip_ticks": 2, "max_qty": 90}


def adj(day, c):
    b = Bar(day * DAY_NS, 1, c, c + 1, c - 1, c, 10)
    return Adj(b, c, c + 1, c - 1, c)


class TestR(unittest.TestCase):
    def test_r_of_a_trade_at_one_contract(self):
        # dist 10 points, slip 0.5: loss a contract = 10.5 * 2 + 1.9 = 22.9; a 20-point win nets 40 - 1.9
        t = {"points": 20.0, "worst": -3.0, "dist": 10.0}
        r, worst = measure.r_sameday(t, SPEC)
        self.assertAlmostEqual(r, 38.1 / 22.9)
        self.assertAlmostEqual(worst, -7.9 / 22.9)

    def test_full_stop_loss_is_minus_one_r_less_a_cent_or_so(self):
        t = {"points": -10.5, "worst": -10.5, "dist": 10.0}
        r, _ = measure.r_sameday(t, SPEC)
        self.assertAlmostEqual(r, -1.0)


class TestCounts(unittest.TestCase):
    def test_longest_losing_run(self):
        self.assertEqual(measure.longest_losing_run([1, -1, -1, 0, -1, -1, -1, 2, -1]), 3)
        self.assertEqual(measure.longest_losing_run([]), 0)

    def test_max_gap(self):
        cal = ["d1", "d2", "d3", "d4", "d5", "d6"]
        self.assertEqual(measure.max_gap(cal, {"d1", "d5"}), 3)
        self.assertEqual(measure.max_gap(cal, set()), 6)
        self.assertEqual(measure.max_gap(cal, set(cal)), 0)


class TestDrawdown(unittest.TestCase):
    def test_max_drop_counts_the_intraday_low(self):
        # +2 (high 2), then a day ending -1 with a low of -3: drop = 2 - (2 - 3) = 3
        self.assertAlmostEqual(measure._max_drop([(2, 0), (-1, -3)]), 3)

    def test_dd975_is_deterministic(self):
        rows = [(1, -0.5), (-1, -1), (2, 0), (-1, -1.2)] * 10
        self.assertEqual(measure.dd975_r(rows, runs=200), measure.dd975_r(rows, runs=200))


class TestSlice(unittest.TestCase):
    def test_first_decision_is_the_bar_before_the_window(self):
        # 10 bars on days 0..9; window starts at day 5; lookback 3: the slice starts at index 5 - 1 - 3 = 1, so
        # slice index 3 (the first with 3 earlier bars) is day 4, whose decision fills on day 5
        s = [adj(d, 100 + d) for d in range(10)]
        out = measure.slice_b(s, first_day=5, last_day=8, lookback=3, atr_days=2)
        self.assertEqual(out[0].bar.ts // DAY_NS, 1)
        self.assertEqual(out[3].bar.ts // DAY_NS, 4)
        self.assertEqual(out[-1].bar.ts // DAY_NS, 8)

    def test_atr_needs_more_history_than_the_lookback(self):
        s = [adj(d, 100 + d) for d in range(30)]
        out = measure.slice_b(s, first_day=20, last_day=29, lookback=3, atr_days=14)
        # decision bar day 19 must be slice index >= 13: the slice starts at day 6
        self.assertEqual(out[0].bar.ts // DAY_NS, 6)


if __name__ == "__main__":
    unittest.main()
