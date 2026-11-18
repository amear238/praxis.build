#!/usr/bin/env python3
"""Tests for accel.py: candidate 4, acceleration through a level (research/levels-150k/PLAN.md, the amendment of
2026-11-18). Tuesday 2024-01-09: PD high 130, PD low 90, P0 110, ATR 20, so k 0.2 gives d = 4: a long at R 130
(stop 126) after a break up, a short at R 90 (stop 94) after a break down.
Run: python3 -I -B research/levels-150k/test_accel.py"""
import os
import sys
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import accel  # noqa: E402
from test_fade import OPEN, L, market, with_levels  # noqa: E402
from test_levels import ts  # noqa: E402

S = {"name": "t", "kind": "PD", "k": 0.2, "target": 3, "atr_days": 14}
FLAT = (15, 55, 133, 134, 132, 133.5)                # flat at 133 - 0.5 = 132.5; an early close would be 133.5
BREAK = (10, 14, 129, 131, 129, 131)              # the 10:00 quarter closes 131: 130 broken, trigger 131.25
TWO = {"PD": [L("PD", 130.0)], "ON": [L("ON", 120.0)]}
ALL = dict(S, kind="ALL")


def run(rth, s=S, lv=None, fill="midpoint"):
    mk = market(rth) if lv is None else with_levels(rth, lv)
    return accel.per_contract(mk, s, fill, dates={"2024-01-09"})


def trades(rth, s=S, lv=None, fill="midpoint"):
    return run(rth, s, lv, fill)["trades"]


def t9(hh, mm):
    return ts(2024, 1, 9, hh, mm)


class Entry(unittest.TestCase):
    def test_a_break_up_enters_one_tick_above_the_break_bar_high(self):
        t = trades([OPEN, (10, 0, 128, 129, 128, 129), BREAK, (10, 20, 131, 132.5, 130.5, 132),
                    (11, 0, 132, 132, 129, 131), FLAT])
        self.assertEqual([(x["side"], x["kind"], x["level"], x["trigger"], x["entry"], x["stop"], x["dist"],
                           x["target"], x["break_ts"], x["entry_ts"], x["reason"], x["exit"], x["worst"]) for x in t],
                         [(1, "PD", 130.0, 131.25, 132.0, 126.0, 6.0, 150.0, t9(10, 14), t9(10, 20), "flat",
                           132.5, -3.0)])       # midpoint: (131.25 + 132.5) / 2 = 131.875, up to 132.0

    def test_the_break_bar_high_is_over_all_its_minutes_and_a_touch_fills(self):
        t = trades([OPEN, (10, 0, 128, 133, 128, 129), BREAK, (10, 20, 131, 133, 130.5, 132),
                    (10, 30, 132, 133.25, 131, 133), FLAT])
        self.assertEqual([(x["trigger"], x["entry_ts"], x["entry"]) for x in t], [(133.25, t9(10, 30), 133.25)])

    def test_the_trigger_is_the_raw_high_plus_a_tick_never_rounded(self):
        # the check's reading R40: a high off the tick grid gives a trigger off it too
        t = trades([OPEN, (10, 14, 129, 131.125, 129, 131), (10, 20, 131, 131.375, 130.5, 131), FLAT])
        self.assertEqual([(x["trigger"], x["entry"]) for x in t], [(131.375, 131.5)])

    def test_no_break_no_entry(self):
        self.assertEqual(trades([OPEN, (10, 14, 129, 131, 129, 130.0), (10, 20, 130, 135, 129.5, 134), FLAT]), [])

    def test_quarters_from_930_and_the_window_opens_on_the_next_minute(self):
        t = trades([(9, 30, 110, 120, 110, 120), (9, 44, 125, 131, 125, 131), (9, 45, 131, 131.5, 130.5, 131), FLAT])
        self.assertEqual([(x["break_ts"], x["entry_ts"], x["entry"]) for x in t], [(t9(9, 44), t9(9, 45), 131.5)])

    def test_the_three_fills_without_a_gap(self):
        rth = [OPEN, BREAK, (10, 20, 131, 132.5, 130.5, 132), FLAT]
        self.assertEqual([trades(rth, fill=f)[0]["entry"] for f in ("midpoint", "kind", "harsh-stops")],
                         [132.0, 131.75, 132.5])

    def test_the_kind_fill_stays_inside_the_minute(self):
        self.assertEqual(trades([OPEN, BREAK, (10, 20, 131, 131.5, 130.5, 131), FLAT], fill="kind")[0]["entry"], 131.5)

    def test_a_gap_open_beyond_the_trigger_is_the_reference(self):
        rth = [OPEN, BREAK, (10, 20, 132, 134, 131.5, 133.5), FLAT]
        self.assertEqual([trades(rth, fill=f)[0]["entry"] for f in ("midpoint", "kind", "harsh-stops")],
                         [133.0, 132.5, 134.0])

    def test_a_short_after_a_break_down_mirrors(self):
        t = trades([OPEN, (10, 14, 92, 92, 89, 89.75), (10, 20, 89.5, 90, 88, 88.5), (15, 55, 85, 85, 85, 85)])
        self.assertEqual([(x["side"], x["level"], x["trigger"], x["entry"], x["stop"], x["dist"], x["target"])
                          for x in t], [(-1, 90.0, 88.75, 88.25, 94.0, 5.75, 71.0)])

    def test_a_zone_breaks_at_its_far_edge_with_the_stop_beyond_its_near_edge(self):
        lv = {"SD": [L("SD", 118.0, "supply", 120.0)]}
        t = trades([OPEN, (10, 14, 119, 121, 119, 120.25), (10, 20, 120.5, 121.5, 120, 121), FLAT],
                   dict(S, kind="SD"), lv)
        self.assertEqual([(x["kind"], x["side"], x["level"], x["stop"], x["trigger"], x["entry"], x["dist"],
                           x["target"]) for x in t], [("SD", 1, 120.0, 114.0, 121.25, 121.5, 7.5, 144.0)])

    def test_the_entry_lapses_at_1500(self):
        ok = trades([OPEN, (14, 44, 129, 131, 129, 131), (14, 59, 131, 132, 130.5, 131.5), FLAT])
        late = trades([OPEN, (14, 44, 129, 131, 129, 131), (15, 0, 131, 132, 130.5, 131.5), FLAT])
        on_245 = trades([OPEN, (14, 59, 129, 131, 129, 131), (15, 0, 131, 132, 130.5, 131.5), FLAT])
        self.assertEqual((len(ok), len(late), len(on_245)), (1, 0, 0))

    def test_the_armed_list_is_candidate_2s(self):
        got = run([OPEN, FLAT])["armed"]["2024-01-09"]
        self.assertEqual(sorted((a["side"], a["level"], a["stop"]) for a in got),
                         [(-1, 90.0, 94.0), (1, 130.0, 126.0)])


class Cancel(unittest.TestCase):
    def test_an_open_at_the_stop_cancels_even_when_the_trigger_trades(self):
        self.assertEqual(trades([OPEN, BREAK, (10, 20, 126, 132, 126, 131), (10, 30, 131, 135, 130.5, 134), FLAT]),
                         [])

    def test_the_stop_reached_before_the_trigger_cancels(self):
        for low in (125.75, 126.0):
            self.assertEqual(trades([OPEN, BREAK, (10, 20, 129, 129, low, 127), (10, 30, 127, 135, 127, 134), FLAT]),
                             [], low)

    def test_trigger_and_stop_in_one_minute_fill_then_stop(self):
        t = trades([OPEN, BREAK, (10, 20, 128, 132, 125, 127), FLAT])
        self.assertEqual([(x["entry"], x["exit"], x["reason"], x["gap"], x["exit_ts"], x["worst"]) for x in t],
                         [(131.75, 125.5, "stop", False, t9(10, 20), -6.75)])


class Exits(unittest.TestCase):
    def test_the_target_is_three_times_the_risk_from_the_fill_and_not_on_the_entry_minute(self):
        t = trades([OPEN, BREAK, (10, 20, 131, 160, 130.5, 150), (10, 21, 150, 150, 148, 149), FLAT], fill="kind")
        self.assertEqual([(x["entry"], x["dist"], x["target"], x["reason"], x["exit"], x["exit_ts"]) for x in t],
                         [(131.75, 5.75, 149.0, "target", 149.0, t9(10, 21))])

    def test_an_early_close(self):
        t = trades([OPEN, BREAK, (10, 20, 131, 132.5, 130.5, 132), (12, 59, 133, 133, 131, 132.5)])
        self.assertEqual([(x["reason"], x["exit"], x["exit_ts"], x["worst"]) for x in t],
                         [("flat", 132.5, t9(12, 59), -1.5)])

    def test_an_entry_on_the_last_minute_counts_only_the_fill(self):
        t = trades([OPEN, BREAK, (10, 20, 131, 132.5, 130.5, 132)])
        self.assertEqual([(x["reason"], x["exit"], x["worst"]) for x in t], [("flat", 132.0, 0.0)])


class Spent(unittest.TestCase):
    def test_an_entry_triggered_while_in_a_position_is_spent(self):
        t = trades([OPEN, (10, 14, 119, 121, 119, 121), (10, 20, 121, 122, 120.5, 121.5), (10, 44, 125, 131, 125, 131),
                    (10, 50, 131, 132, 130, 131.5), (11, 0, 132, 139.25, 131, 139), (11, 30, 139, 140, 137, 139.5),
                    FLAT], ALL, TWO)
        self.assertEqual([(x["kind"], x["entry"], x["target"], x["reason"]) for x in t],
                         [("ON", 121.75, 139.0, "target")])

    def test_an_entry_triggered_on_the_exit_minute_is_spent(self):
        t = trades([OPEN, (10, 14, 119, 121, 119, 121), (10, 20, 121, 122, 120.5, 121.5), (10, 44, 125, 131, 125, 131),
                    (10, 45, 131, 131, 130.5, 131), (11, 0, 131, 139.5, 130.5, 139), (11, 30, 139, 140, 138, 139.5),
                    FLAT], ALL, TWO)
        self.assertEqual([(x["kind"], x["reason"]) for x in t], [("ON", "target")])

    def test_a_level_broken_while_in_a_position_can_fill_after_it(self):
        # the long stops out on 10:44, the last minute of the quarter that breaks 90 down
        t = trades([OPEN, BREAK, (10, 20, 131, 131.5, 130.5, 131), (10, 44, 130, 130, 89, 89.5),
                    (10, 50, 89.5, 90, 88.5, 89), (15, 55, 85, 85, 85, 85)])
        self.assertEqual([(x["side"], x["entry"], x["reason"], x["exit"]) for x in t],
                         [(1, 131.5, "stop", 107.5), (-1, 88.5, "flat", 85.0)])


class Ties(unittest.TestCase):
    def test_the_trigger_nearer_the_open_fills_and_the_other_is_spent(self):
        # 120 breaks on a bar reaching 135 (trigger 135.25); 130 breaks at 10:29 (trigger 131.25). 10:30 opens 134:
        # 135.25 is nearer than 131.25, though R 130 is nearer than R 120.
        t = trades([OPEN, (10, 14, 119, 135, 119, 120.5), (10, 29, 130, 131, 129, 130.5),
                    (10, 30, 134, 136, 133.5, 135.5), FLAT], ALL, TWO)
        self.assertEqual([(x["kind"], x["level"], x["trigger"], x["entry"], x["dist"], x["target"]) for x in t],
                         [("ON", 120.0, 135.25, 135.75, 19.75, 195.0)])

    def test_one_bar_breaking_two_levels_the_r_nearer_the_open_fills(self):
        # both triggers are 131.25. PD 130 fills and stops at 10:21 without reaching 131.25 or ON's stop 116;
        # ON was spent at the tie, so 10:30 makes no second trade.
        t = trades([OPEN, BREAK, (10, 20, 131, 132, 130.5, 131.5), (10, 21, 130, 130, 125, 125.5),
                    (10, 30, 126, 132, 126, 131.5), FLAT], ALL, TWO)
        self.assertEqual([(x["kind"], x["level"], x["entry"], x["stop"], x["reason"]) for x in t],
                         [("PD", 130.0, 131.75, 126.0, "stop")])

    def test_then_the_r_nearer_p0(self):
        t = trades([OPEN, BREAK, (10, 20, 125, 132, 125, 131.5), FLAT], dict(ALL, k=0.4), TWO)
        self.assertEqual([(x["kind"], x["level"], x["entry"], x["stop"]) for x in t], [("ON", 120.0, 131.75, 112.0)])


if __name__ == "__main__":
    unittest.main(verbosity=1)
