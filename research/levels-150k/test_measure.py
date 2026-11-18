#!/usr/bin/env python3
"""Tests for measure.py: R per trade, the stable market set, the portfolio figures and the pre-run gate
(research/levels-150k/PLAN.md, "How the search runs" steps 1 to 3). Run: python3 -I -B research/levels-150k/test_measure.py"""
import os
import sys
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import measure  # noqa: E402

SP = {"pv": 2.0, "tick": 0.25, "comm": 1.90, "slip_ticks": 2, "max_qty": 90}


def tr(date, points, dist, worst, side=1):
    return {"date": date, "side": side, "points": points, "dist": dist, "worst": worst}


class RRows(unittest.TestCase):
    def test_r_after_and_before_costs(self):
        (date, side, r, worst_r, gross), = measure.r_rows([tr("2018-01-02", 30.0, 10.0, -4.0)], SP)
        lpc = (10.0 + 0.5) * 2.0 + 1.9
        self.assertAlmostEqual(r, (30.0 * 2.0 - 1.9) / lpc)
        self.assertAlmostEqual(worst_r, (-4.0 * 2.0 - 1.9) / lpc)
        self.assertAlmostEqual(gross, 3.0)


def rows(*pairs):
    """(date, r) -> r_rows-shaped rows with worst = min(r, 0) and gross = r."""
    return [(d, 1, r, min(r, 0.0), r) for d, r in pairs]


class Sets(unittest.TestCase):
    def test_stable_needs_profit_in_both_halves(self):
        by_m = {"A": rows(("2018-03-01", 1.0), ("2022-03-01", 0.5)),
                "B": rows(("2018-03-01", 1.0), ("2022-03-01", -0.5)),
                "C": rows(("2019-03-01", -1.0), ("2023-03-01", 2.0))}
        self.assertEqual(measure.stable_markets(by_m), ["A"])


class Portfolio(unittest.TestCase):
    def test_figures(self):
        cal = ["2018-01-0%d" % d for d in range(1, 10)]
        by_m = {"A": rows(("2018-01-01", -1.0), ("2018-01-02", 3.0), ("2018-01-09", -1.0)),
                "B": rows(("2018-01-02", -1.0))}
        p = measure.portfolio(by_m, ["A", "B"], cal, full_days=18)
        self.assertEqual(p["trades"], 4)
        self.assertEqual(p["avg_winner_r"], 3.0)
        self.assertEqual(p["net_r"], 0.0)
        self.assertEqual(p["max_gap"], 6)                     # 01-03 .. 01-08
        self.assertEqual(p["worst_day_r"], -1.0)              # 01-02: A's low 0 and B's -1 at once; 01-01 and 01-09 -1
        self.assertEqual(p["longest_losing_run"], 2)          # B on 01-02, then A on 01-09

    def test_a_winning_day_still_counts_its_open_loss(self):
        by_m = {"A": [("2018-01-01", 1, 2.0, -0.8, 2.0)]}
        self.assertEqual(measure.portfolio(by_m, ["A"], ["2018-01-01"], 1)["worst_day_r"], -0.8)

    def test_only_the_set_counts(self):
        cal = ["2018-01-01", "2018-01-02"]
        by_m = {"A": rows(("2018-01-01", 2.0)), "B": rows(("2018-01-02", -1.0))}
        self.assertEqual(measure.portfolio(by_m, ["A"], cal, 2)["trades"], 1)


class Gate(unittest.TestCase):
    def test_all_three_needed(self):
        ok = {"avg_winner_r": 2.0, "max_gap": 7, "projected_profit": 9000.0}
        self.assertTrue(measure.gate(ok))
        self.assertFalse(measure.gate(dict(ok, avg_winner_r=1.99)))
        self.assertFalse(measure.gate(dict(ok, max_gap=8)))
        self.assertFalse(measure.gate(dict(ok, projected_profit=8999.0)))
        self.assertFalse(measure.gate(dict(ok, projected_profit=None)))


class Grid(unittest.TestCase):
    def test_seventy_two_settings(self):
        g = measure.grid()
        self.assertEqual(len(g), 72)
        self.assertEqual(len({s["name"] for s in g}), 72)
        self.assertEqual({s["kind"] for s in g}, {"PD", "ON", "PW", "SW", "RN", "VP", "SD", "ALL"})
        self.assertEqual({s["k"] for s in g}, {0.1, 0.2, 0.4})
        self.assertEqual({s["target"] for s in g}, {3, 5, None})

    def test_nine_settings_for_candidate_3(self):
        g = measure.grid("3")
        self.assertEqual([s["name"] for s in g], ["VA-k0.1-m0", "VA-k0.1-m2", "VA-k0.1-m3", "VA-k0.2-m0",
                                                  "VA-k0.2-m2", "VA-k0.2-m3", "VA-k0.4-m0", "VA-k0.4-m2",
                                                  "VA-k0.4-m3"])
        self.assertEqual({(s["kind"], s["atr_days"]) for s in g}, {("VA", 14)})
        self.assertEqual(sorted({(s["k"], s["min_rr"]) for s in g}),
                         [(k, m) for k in (0.1, 0.2, 0.4) for m in (0, 2, 3)])
        self.assertEqual(len(measure.grid("2")), 72)
        self.assertIs(measure.ENGINES["3"].__name__, "traverse")


if __name__ == "__main__":
    unittest.main(verbosity=1)
