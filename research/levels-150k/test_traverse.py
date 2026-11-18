#!/usr/bin/env python3
"""Tests for traverse.py: candidate 3, value area traversal (research/levels-150k/PLAN.md, the candidate 3
amendment of 2026-11-18). Tuesday 2024-01-09: the value area VAL 112, POC 120, VAH 130; P0 110 unless a test
opens elsewhere; ATR 20, so k 0.2 gives d = 4 and a long's stop at 108. NQ: tick 0.25, slippage 2 ticks.
Run: python3 -I -B research/levels-150k/test_traverse.py"""
import os
import sys
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import traverse  # noqa: E402
from test_fade import L, with_levels  # noqa: E402
from test_levels import ts  # noqa: E402

S = {"name": "t", "kind": "VA", "k": 0.2, "min_rr": 0, "atr_days": 14}
VA = {"VP": [L("VP", 130.0, "vah"), L("VP", 120.0, "poc"), L("VP", 112.0, "val")]}
OPEN = (9, 30, 110, 110, 110, 110)
FLAT = (15, 55, 120, 121, 119, 120)
# 9:30 bar closes 110 (outside); 10:00 bar closes 113 and 10:30 bar 114 (both inside): the signal, C = 114
LONG = [OPEN, (10, 29, 113, 113, 113, 113), (10, 59, 114, 114, 114, 114)]
ENTRY = (11, 0, 114, 115, 114, 115)


def run(rth, s=S, lv=VA, fill="midpoint"):
    return traverse.per_contract(with_levels(rth, lv), s, fill, dates={"2024-01-09"})


def trades(rth, s=S, lv=VA, fill="midpoint"):
    return run(rth, s, lv, fill)["trades"]


def m(n):
    return dict(S, min_rr=n)


class SetUp(unittest.TestCase):
    def test_p0_below_val_is_a_long_with_the_stop_d_below_val(self):
        self.assertEqual(run([OPEN, FLAT])["armed"]["2024-01-09"],
                         [{"kind": "VA", "side": 1, "level": 112.0, "far": 130.0, "stop": 108.0}])

    def test_p0_above_vah_is_a_short_with_the_stop_d_above_vah(self):
        self.assertEqual(run([(9, 30, 132, 132, 132, 132), FLAT])["armed"]["2024-01-09"],
                         [{"kind": "VA", "side": -1, "level": 130.0, "far": 112.0, "stop": 134.0}])

    def test_p0_needs_a_tick_outside(self):
        self.assertEqual(run([(9, 30, 112, 112, 112, 112), FLAT])["armed"]["2024-01-09"], [])
        self.assertEqual(run([(9, 30, 130, 130, 130, 130), FLAT])["armed"]["2024-01-09"], [])
        self.assertEqual(len(run([(9, 30, 111.75, 112, 111.75, 112), FLAT])["armed"]["2024-01-09"]), 1)

    def test_p0_inside_has_no_set_up_and_no_trade(self):
        got = run([(9, 30, 120, 120, 120, 120), (10, 29, 121, 121, 121, 121), (10, 59, 122, 122, 122, 122),
                   ENTRY, FLAT])
        self.assertEqual((got["armed"]["2024-01-09"], got["trades"]), ([], []))

    def test_nothing_without_the_value_area(self):
        self.assertEqual(run(LONG + [ENTRY, FLAT], lv={})["trades"], [])

    def test_d_by_k(self):
        # k 0.1: 0.1 x 20 = 2 -> stop 110; k 0.4: 8 -> 104
        self.assertEqual(run([OPEN, FLAT], dict(S, k=0.1))["armed"]["2024-01-09"][0]["stop"], 110.0)
        self.assertEqual(run([OPEN, FLAT], dict(S, k=0.4))["armed"]["2024-01-09"][0]["stop"], 104.0)

    def test_d_rounds_down_to_the_tick(self):
        # ATR 20.9: 0.2 x 20.9 = 4.18 -> 4.00, not the nearer 4.25
        mk = with_levels([OPEN, FLAT], VA)
        day = next(d for d in mk.days if d.date == "2024-01-09")
        day.atr = 20.9
        self.assertEqual(traverse.setup(day, 0.2, 0.25)["stop"], 108.0)


class Signal(unittest.TestCase):
    def test_two_closes_inside_then_a_market_entry_on_the_next_minute(self):
        t = trades(LONG + [ENTRY, FLAT])
        self.assertEqual([(x["kind"], x["level"], x["side"], x["entry"], x["stop"], x["dist"], x["target"],
                           x["setup_ts"], x["entry_ts"]) for x in t],
                         [("VA", 112.0, 1, 114.5, 108.0, 6.5, 130.0, ts(2024, 1, 9, 10, 59), ts(2024, 1, 9, 11, 0))])

    def test_inside_needs_a_tick(self):
        # 10:00 closes at VAL exactly: not inside; the pair is 10:30 and 11:00, entry 11:30
        t = trades([OPEN, (10, 29, 112, 112, 112, 112), (10, 59, 114, 114, 114, 114), (11, 29, 114, 114, 114, 114),
                    (11, 30, 114, 115, 114, 115), FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 11, 30)])

    def test_a_close_a_tick_inside_counts(self):
        t = trades([OPEN, (10, 29, 112.25, 112.25, 112.25, 112.25), (10, 59, 129.75, 129.75, 129.75, 129.75),
                    (11, 0, 129.5, 129.75, 129.5, 129.5), FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 11, 0)])

    def test_a_close_at_the_far_edge_is_not_inside(self):
        t = trades([OPEN, (10, 29, 113, 113, 113, 113), (10, 59, 130, 130, 130, 130), (11, 0, 129, 129.5, 129, 129),
                    FLAT])
        self.assertEqual(t, [])

    def test_the_bar_close_is_its_last_minute(self):
        # 10:05 closes inside but 10:29, the half hour's last minute, closes outside
        t = trades([OPEN, (10, 5, 113, 113, 113, 113), (10, 29, 111, 111, 111, 111), (10, 59, 114, 114, 114, 114),
                    (11, 29, 114, 114, 114, 114), (11, 30, 114, 115, 114, 115), FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 11, 30)])

    def test_the_930_bar_can_be_the_first_of_the_pair(self):
        t = trades([OPEN, (9, 59, 113, 113, 113, 113), (10, 29, 114, 114, 114, 114), (10, 30, 114, 115, 114, 115),
                    FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 10, 30)])

    def test_only_the_first_pair_counts(self):
        # m 3: the first pair (C 114) fails the filter; the next pair (C 113.5) would pass, but does not count
        t = trades(LONG + [(11, 29, 113.5, 113.5, 113.5, 113.5), (11, 30, 113.5, 114, 113.5, 114), FLAT], m(3))
        self.assertEqual(t, [])

    def test_the_second_bar_starts_by_1400(self):
        ok = trades([OPEN, (13, 59, 113, 113, 113, 113), (14, 29, 114, 114, 114, 114), (14, 30, 114, 115, 114, 115),
                     FLAT])
        # a second bar starting 14:30 ends by 14:59, so its next minute is never before 15:00 either
        late = trades([OPEN, (14, 29, 113, 113, 113, 113), (14, 59, 114, 114, 114, 114), (15, 0, 114, 115, 114, 115),
                       FLAT])
        self.assertEqual(([x["entry_ts"] for x in ok], late), ([ts(2024, 1, 9, 14, 30)], []))

    def test_a_missing_half_hour_leaves_no_gap(self):
        t = trades([OPEN, (10, 29, 113, 113, 113, 113), (11, 29, 114, 114, 114, 114), (11, 30, 114, 115, 114, 115),
                    FLAT])
        self.assertEqual([(x["setup_ts"], x["entry_ts"]) for x in t],
                         [(ts(2024, 1, 9, 11, 29), ts(2024, 1, 9, 11, 30))])

    def test_the_entry_is_the_next_minute_in_the_data(self):
        t = trades(LONG + [(11, 5, 114, 115, 114, 115), FLAT])
        self.assertEqual([x["entry_ts"] for x in t], [ts(2024, 1, 9, 11, 5)])

    def test_no_entry_from_1500(self):
        t = trades([OPEN, (13, 59, 113, 113, 113, 113), (14, 29, 114, 114, 114, 114), (15, 0, 114, 115, 114, 115),
                    FLAT])
        self.assertEqual(t, [])

    def test_short_mirror(self):
        t = trades([(9, 30, 132, 132, 132, 132), (10, 29, 129, 129, 129, 129), (10, 59, 128, 128, 128, 128),
                    (11, 0, 128, 128, 127, 127), (15, 55, 120, 121, 119, 120)])
        self.assertEqual([(x["side"], x["level"], x["entry"], x["stop"], x["dist"], x["target"], x["exit"])
                          for x in t], [(-1, 130.0, 127.5, 134.0, 6.5, 112.0, 120.5)])


class Filter(unittest.TestCase):
    # C 114: reward 130 - 114 = 16, risk 114 - 108 = 6, 2.67 to 1
    def test_m0_and_m2_take_it_m3_does_not(self):
        self.assertEqual([len(trades(LONG + [ENTRY, FLAT], m(n))) for n in (0, 2, 3)], [1, 1, 0])

    def test_the_equal_case_is_taken(self):
        # C 113.5: reward 16.5, risk 5.5, exactly 3 to 1; C 113.75: reward 16.25, risk 5.75, under 3
        eq = [OPEN, (10, 29, 113, 113, 113, 113), (10, 59, 113.5, 113.5, 113.5, 113.5), ENTRY, FLAT]
        under = [OPEN, (10, 29, 113, 113, 113, 113), (10, 59, 113.75, 113.75, 113.75, 113.75), ENTRY, FLAT]
        self.assertEqual((len(trades(eq, m(3))), len(trades(under, m(3)))), (1, 0))

    def test_the_filter_uses_the_signal_close_not_the_fill(self):
        # C 113.5 is exactly 3 to 1; the fill at 116.5 would not be, and the trade is still taken
        t = trades([OPEN, (10, 29, 113, 113, 113, 113), (10, 59, 113.5, 113.5, 113.5, 113.5),
                    (11, 0, 116, 117, 116, 117), FLAT], m(3))
        self.assertEqual([(x["entry"], x["dist"]) for x in t], [(116.5, 8.5)])


class Entry(unittest.TestCase):
    def test_the_slippage_stays_inside_the_minute(self):
        t = trades(LONG + [(11, 0, 114, 114.25, 114, 114.25), FLAT])
        self.assertEqual([x["entry"] for x in t], [114.25])
        t = trades([(9, 30, 132, 132, 132, 132), (10, 29, 129, 129, 129, 129), (10, 59, 128, 128, 128, 128),
                    (11, 0, 128, 128, 127.75, 128), FLAT])
        self.assertEqual([x["entry"] for x in t], [127.75])

    def test_no_trade_when_the_entry_minute_opens_at_the_stop_or_the_far_edge(self):
        self.assertEqual(trades(LONG + [(11, 0, 108, 109, 107, 109), FLAT]), [])
        self.assertEqual(trades(LONG + [(11, 0, 130, 131, 129, 130), FLAT]), [])
        self.assertEqual(len(trades(LONG + [(11, 0, 108.25, 109, 108.25, 109), FLAT])), 1)


class Exits(unittest.TestCase):
    def test_stop_on_the_entry_minute(self):
        t = trades(LONG + [(11, 0, 114, 115, 107, 108)])[0]
        self.assertEqual((t["reason"], t["exit"], t["gap"], t["exit_ts"]), ("stop", 107.5, False, t["entry_ts"]))

    def test_kind_and_harsh_stops(self):
        rth = LONG + [ENTRY, (11, 1, 110, 110, 106, 107)]
        self.assertEqual([trades(rth, fill=f)[0]["exit"] for f in ("kind", "midpoint", "harsh-stops")],
                         [107.5, 107.0, 106.0])

    def test_target_not_on_the_entry_minute_then_a_tick_through(self):
        t = trades(LONG + [(11, 0, 114, 131, 114, 130), (11, 1, 130, 130, 129, 130), (11, 2, 130, 130.25, 129, 130),
                           FLAT])[0]
        self.assertEqual((t["reason"], t["exit"], t["exit_ts"]), ("target", 130.0, ts(2024, 1, 9, 11, 2)))

    def test_flat_at_355(self):
        t = trades(LONG + [ENTRY, FLAT])[0]
        self.assertEqual((t["reason"], t["exit"], t["points"]), ("flat", 119.5, 5.0))

    def test_worst_and_one_trade_a_day(self):
        got = trades(LONG + [ENTRY, (12, 0, 115, 116, 110, 111), (12, 29, 113, 113, 113, 113),
                             (12, 59, 114, 114, 114, 114), (13, 0, 114, 115, 114, 115), FLAT])
        self.assertEqual([(x["worst"], x["reason"]) for x in got], [(-4.5, "flat")])

    def test_early_close(self):
        # S(D) ends at 12:00; the last minute counts only at its close, so worst is the entry minute's -0.5
        t = trades(LONG + [ENTRY, (12, 0, 118, 119, 117, 118.5)])[0]
        self.assertEqual((t["reason"], t["exit"], t["worst"]), ("flat", 118.5, -0.5))


if __name__ == "__main__":
    unittest.main(verbosity=1)
