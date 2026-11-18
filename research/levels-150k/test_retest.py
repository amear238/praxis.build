#!/usr/bin/env python3
"""Tests for retest.py: candidate 2, break and retest (research/levels-150k/PLAN.md, the amendment of 2026-11-18).
Tuesday 2024-01-09: PD high 130, PD low 90, P0 110, ATR 20, so k 0.2 gives d = 4.
Run: python3 -I -B research/levels-150k/test_retest.py"""
import os
import sys
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import retest  # noqa: E402
from test_fade import OPEN, L, market, with_levels  # noqa: E402
from test_levels import ts  # noqa: E402

S = {"name": "t", "kind": "PD", "k": 0.2, "target": 3, "atr_days": 14}
FLAT = (15, 55, 131, 131, 131, 131)


def run(rth, s=S, lv=None, fill="midpoint"):
    mk = market(rth) if lv is None else with_levels(rth, lv)
    return retest.per_contract(mk, s, fill, dates={"2024-01-09"})


def trades(rth, s=S, lv=None):
    return run(rth, s, lv)["trades"]


class Break(unittest.TestCase):
    def test_break_up_then_retest_is_a_long_at_the_level(self):
        t = trades([OPEN, (10, 0, 128, 129, 128, 129), (10, 14, 129, 131, 129, 131), (10, 20, 131, 131, 129.75, 130),
                    FLAT])
        self.assertEqual([(x["side"], x["entry"], x["stop"], x["target"], x["entry_ts"] > 0) for x in t],
                         [(1, 130.0, 126.0, 142.0, True)])

    def test_a_close_needs_a_tick_beyond(self):
        self.assertEqual(trades([OPEN, (10, 14, 129, 131, 129, 130.0), (10, 20, 131, 131, 129.0, 130), FLAT]), [])

    def test_the_break_bar_itself_cannot_fill(self):
        self.assertEqual(trades([OPEN, (10, 0, 130, 131, 129.5, 131), (10, 14, 130, 131, 129.5, 131), FLAT]), [])

    def test_the_break_counts_at_the_bar_close_not_a_minute_close(self):
        # 10:05 closes above 130.25 but the quarter's last minute (10:14) closes below: no break
        self.assertEqual(trades([OPEN, (10, 5, 129, 131, 129, 131), (10, 14, 131, 131, 129.5, 130),
                                 (10, 20, 130, 130, 129.0, 129.5), FLAT]), [])

    def test_quarters_run_from_930(self):
        # 9:44 is the last minute of the 9:30 quarter: its close breaks; 9:45 is the next quarter and can fill
        t = trades([(9, 30, 110, 120, 110, 120), (9, 44, 125, 131, 125, 131), (9, 45, 131, 131, 129.75, 130), FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 9, 45)])

    def test_last_break_bar_starts_at_1445_and_last_entry_before_1500(self):
        ok = trades([OPEN, (14, 44, 129, 131, 129, 131), (14, 50, 131, 131, 129.75, 130), FLAT])
        late = trades([OPEN, (14, 59, 129, 131, 129, 131), (15, 0, 131, 131, 129.0, 130), FLAT])
        self.assertEqual((len(ok), len(late)), (1, 0))

    def test_short_after_a_break_down(self):
        t = trades([OPEN, (10, 14, 92, 92, 89, 89.75), (10, 20, 89.75, 90.25, 89, 90), (15, 55, 85, 85, 85, 85)])
        self.assertEqual([(x["side"], x["entry"], x["stop"], x["target"]) for x in t], [(-1, 90.0, 94.0, 78.0)])

    def test_a_zone_retests_at_its_far_edge_with_the_stop_beyond_its_near_edge(self):
        lv = {"SD": [L("SD", 118.0, "supply", 120.0)]}
        s = dict(S, kind="SD")
        t = trades([OPEN, (10, 14, 119, 121, 119, 120.25), (10, 20, 120.5, 121, 119.75, 120), (15, 55, 121, 121, 121, 121)],
                   s, lv)
        self.assertEqual([(x["side"], x["entry"], x["stop"], x["dist"]) for x in t], [(1, 120.0, 114.0, 6.0)])

    def test_the_armed_list_is_flipped(self):
        got = run([OPEN, FLAT])["armed"]["2024-01-09"]
        self.assertEqual(sorted((a["side"], a["level"], a["stop"]) for a in got), [(-1, 90.0, 94.0), (1, 130.0, 126.0)])


class Exits(unittest.TestCase):
    def test_stop_on_the_entry_minute_and_target_later(self):
        t = trades([OPEN, (10, 14, 129, 131, 129, 131), (10, 20, 131, 131, 125.0, 126)])[0]
        self.assertEqual((t["reason"], t["exit"]), ("stop", 125.5))
        t = trades([OPEN, (10, 14, 129, 131, 129, 131), (10, 20, 131, 143, 129.75, 140), (10, 21, 140, 142.25, 140, 142),
                    FLAT])[0]
        self.assertEqual((t["reason"], t["exit"]), ("target", 142.0))


class Spent(unittest.TestCase):
    def test_a_retest_while_in_a_position_spends_the_level(self):
        # two levels above P0: 120 (ON high) and 130 (PD high). Long from 120's retest; 130 breaks and is retested
        # while long; after the stop, a second retest of 130 makes no trade.
        s = dict(S, kind="ALL", target=None)
        lv = {"PD": [L("PD", 130.0)], "ON": [L("ON", 120.0)]}
        t = trades([OPEN, (10, 14, 119, 121, 119, 121), (10, 20, 121, 121, 119.75, 120), (10, 44, 121, 131, 121, 131),
                    (10, 50, 131, 131, 129.75, 130), (11, 0, 130, 130, 115, 116), (11, 30, 116, 131, 116, 131),
                    (11, 44, 131, 131, 131, 131), (12, 0, 131, 131, 129.0, 130), FLAT], s, lv)
        self.assertEqual([(x["kind"], x["entry"], x["reason"]) for x in t], [("ON", 120.0, "stop")])

    def test_two_retests_in_one_minute_the_nearer_the_open_fills(self):
        s = dict(S, kind="ALL")
        lv = {"PD": [L("PD", 130.0)], "ON": [L("ON", 120.0)]}
        t = trades([OPEN, (10, 14, 119, 131, 119, 131), (10, 20, 131, 131, 119.0, 125), FLAT], s, lv)
        self.assertEqual([(x["kind"], x["entry"]) for x in t], [("PD", 130.0)])


if __name__ == "__main__":
    unittest.main(verbosity=1)
