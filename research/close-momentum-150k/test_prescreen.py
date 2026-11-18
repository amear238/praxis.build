#!/usr/bin/env python3
"""Tests for prescreen.py against PLAN.md's exact rule, rules 1 to 4, and the pre-screen's sums. Synthetic bars.
Run: python3 -I -B research/close-momentum-150k/test_prescreen.py"""
import datetime as dt
import os
import sys
import unittest
from zoneinfo import ZoneInfo

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import mdata  # noqa: E402
import prescreen as ps  # noqa: E402

ET = ZoneInfo("America/New_York")
O, C = 570, 960
NQ = {"traded": "MNQ", "pv": 2.0, "tick": 0.25, "comm": 1.90, "slip_ticks": 2, "max_qty": 90}


def ts(d, minute):
    return int(dt.datetime(d.year, d.month, d.day, minute // 60, minute % 60, tzinfo=ET).timestamp()) * 10 ** 9


def bar(d, minute, o, c=None, iid=1):
    c = o if c is None else c
    return mdata.Bar(ts(d, minute), iid, float(o), float(max(o, c)), float(min(o, c)), float(c), 1)


MON, TUE, WED = dt.date(2019, 3, 4), dt.date(2019, 3, 5), dt.date(2019, 3, 6)


def day(d, y_open=None, s2=None, s1=None, entry=None, exit_=None, iid=1, extra=()):
    """One day's bars: the 9:30 bar (a trading day), the 9:59 bar closing at s2, the 15:29 bar closing at s1,
    the 15:30 bar opening at entry, the 16:00 bar opening at exit_ (it is also tomorrow's Y)."""
    out = [bar(d, O, 100, iid=iid)]
    if s2 is not None:
        out.append(bar(d, O + 29, 100, s2, iid=iid))
    if s1 is not None:
        out.append(bar(d, C - 31, 100, s1, iid=iid))
    if entry is not None:
        out.append(bar(d, C - 30, entry, iid=iid))
    if exit_ is not None:
        out.append(bar(d, C, exit_, iid=iid))
    out.extend(extra)
    return sorted(out, key=lambda b: b.ts)


class Rule(unittest.TestCase):
    def test_long_when_up_on_the_day_and_the_trade_is_entry_to_close(self):
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, entry=102, exit_=103), O, C)
        self.assertEqual(len(rows), 1)
        d, sides, e, x = rows[0]
        self.assertEqual(d, TUE.toordinal())
        self.assertEqual(sides, {"S1": 1, "S2": 1, "S3": 1})
        self.assertEqual((e, x), (102.0, 103.0))

    def test_short_when_down_and_s3_off_when_the_two_differ(self):
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=99, entry=99, exit_=98), O, C)
        self.assertEqual(rows[0][1], {"S1": -1, "S2": 1, "S3": 0})

    def test_equal_to_yesterday_is_no_side(self):
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=100, s1=100, entry=100, exit_=101), O, C)
        self.assertEqual(rows[0][1], {"S1": 0, "S2": 0, "S3": 0})

    def test_a_roll_between_yesterday_and_today_means_no_trade(self):
        rows = ps.trades(day(MON, exit_=100, iid=1) + day(TUE, s2=101, s1=102, entry=102, exit_=103, iid=2), O, C)
        self.assertEqual(rows, [])

    def test_a_signal_bar_of_another_contract_means_no_trade(self):
        other = [bar(TUE, C - 31, 100, 102, iid=2)]
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, entry=102, exit_=103, extra=other), O, C)
        self.assertEqual(rows, [])

    def test_no_price_at_the_close_means_no_trade(self):
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, entry=102), O, C)
        self.assertEqual(rows, [])

    def test_no_yesterday_close_means_no_trade(self):
        rows = ps.trades(day(MON) + day(TUE, s2=101, s1=102, entry=102, exit_=103), O, C)
        self.assertEqual(rows, [])

    def test_price_at_takes_the_first_bar_within_five_minutes(self):
        late = [bar(TUE, C - 27, 105)]
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, exit_=103, extra=late), O, C)
        self.assertEqual(rows[0][2], 105.0)
        too_late = [bar(TUE, C - 25, 105)]
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, exit_=103, extra=too_late), O, C)
        self.assertEqual(rows, [])

    def test_last_before_looks_back_five_minutes_only(self):
        old = [bar(TUE, C - 36, 100, 110)]   # 15:24, six minutes before 15:30
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, entry=102, exit_=103, extra=old), O, C)
        self.assertEqual(rows[0][1]["S1"], 0)
        near = [bar(TUE, C - 35, 100, 110)]  # 15:25, five minutes before
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, entry=102, exit_=103, extra=near), O, C)
        self.assertEqual(rows[0][1]["S1"], 1)

    def test_the_trading_day_before_skips_a_weekend(self):
        fri, mon = dt.date(2019, 3, 1), dt.date(2019, 3, 4)
        sat = [bar(dt.date(2019, 3, 2), O, 50)]
        rows = ps.trades(day(fri, exit_=100) + sat + day(mon, s2=99, s1=99, entry=99, exit_=97), O, C)
        self.assertEqual([r[0] for r in rows], [mon.toordinal()])
        self.assertEqual(rows[0][1]["S1"], -1)

    def test_yesterday_is_the_previous_trading_day_not_the_previous_date_with_bars(self):
        # Wednesday has bars only after C, none in [O, C): not a trading day, so Thursday's yesterday is Tuesday.
        thu = dt.date(2019, 3, 7)
        wed_night = [bar(WED, C + 1, 150)]
        rows = ps.trades(day(TUE, exit_=100) + wed_night + day(thu, s2=101, s1=101, entry=101, exit_=102), O, C)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1]["S1"], 1)

    def test_yesterday_is_the_open_of_the_close_bar_not_its_close(self):
        mon = [bar(MON, O, 100), bar(MON, C, 100, 104)]   # opens 100, closes 104
        rows = ps.trades(mon + day(TUE, s2=102, s1=102, entry=102, exit_=103), O, C)
        self.assertEqual(rows[0][1]["S1"], 1)               # 102 against 100, not against 104

    def test_the_exit_is_the_open_of_the_first_bar_at_or_after_c(self):
        before = [bar(TUE, C - 1, 90)]                       # 15:59 is before C: not the exit
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, entry=102, exit_=103, extra=before), O, C)
        self.assertEqual(rows[0][3], 103.0)
        only_late = [bar(TUE, C + 4, 107)]                   # 16:04 is within five minutes of C
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s2=101, s1=102, entry=102, extra=before + only_late), O, C)
        self.assertEqual(rows[0][3], 107.0)

    def test_s2_reads_the_five_minutes_before_o_plus_30(self):
        edge = [bar(TUE, O + 25, 100, 97)]                   # 9:55, five minutes before 10:00
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s1=102, entry=102, exit_=103, extra=edge), O, C)
        self.assertEqual(rows[0][1]["S2"], -1)
        on_time = [bar(TUE, O + 30, 100, 97)]                # 10:00 itself is not before O + 30
        rows = ps.trades(day(MON, exit_=100) + day(TUE, s1=102, entry=102, exit_=103, extra=on_time), O, C)
        self.assertEqual(rows[0][1]["S2"], 0)


class Sums(unittest.TestCase):
    def test_cost_ticks_for_the_micro_nasdaq(self):
        self.assertAlmostEqual(ps.cost_ticks(NQ), 2 * 2 + 1.90 / (2.0 * 0.25))

    def test_edge_right_and_net(self):
        d1, d2, d3 = dt.date(2019, 1, 2).toordinal(), dt.date(2019, 1, 3).toordinal(), dt.date(2022, 1, 3).toordinal()
        rows = [(d1, {"S1": 1, "S2": 0, "S3": 0}, 100.0, 101.0),     # +4 ticks
                (d2, {"S1": -1, "S2": -1, "S3": -1}, 100.0, 100.5),  # -2 ticks
                (d3, {"S1": 1, "S2": 1, "S3": 1}, 100.0, 100.0)]     # 0, not right
        r = ps.summarise(rows, 0.25, 1.0)
        self.assertEqual(r["S1/2018-2023"], {"trades": 3, "edge_ticks": round(2 / 3, 4), "right": round(1 / 3, 4),
                                             "net_ticks": round(2 / 3 - 1.0, 4)})
        self.assertEqual(r["S1/2018-2020"]["trades"], 2)
        self.assertEqual(r["S1/2021-2023"]["edge_ticks"], 0.0)
        self.assertEqual(r["S2/2018-2023"]["trades"], 2)
        self.assertEqual(r["S3/2018-2020"]["edge_ticks"], -2.0)

    def test_outside_2018_to_2023_is_not_counted(self):
        rows = [(dt.date(2024, 1, 2).toordinal(), {"S1": 1, "S2": 1, "S3": 1}, 100.0, 101.0)]
        r = ps.summarise(rows, 0.25, 1.0)
        self.assertEqual(r["S1/2018-2023"]["trades"], 0)
        self.assertIsNone(r["S1/2018-2023"]["edge_ticks"])


if __name__ == "__main__":
    unittest.main()
