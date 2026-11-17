#!/usr/bin/env python3
"""Tests for globex.py. Run: python3 -I -B research/noise-area-variations/test_globex.py

Small hand-built files check each day rule. One test reads the real data file and checks that every
regular-hours session of the project's existing loader (scripts/wf/oracle/market.py, start 09:31) has
the same bars, stamp for stamp, in the Globex day of the same date.
"""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import globex as g   # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")


def line(stamp, o=100.0, h=101.0, l=99.0, c=100.5, v=10):
    return "%s;%s;%s;%s;%s;%d\n" % (stamp, o, h, l, c, v)


class SmallFiles(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, stamps):
        path = os.path.join(self.tmp, "bars.txt")
        with open(path, "w") as fh:
            for i, s in enumerate(stamps):
                fh.write(line(s, o=100.0 + i, v=i + 1))
        return path

    def test_sm_of(self):
        self.assertEqual([g.sm_of(x) for x in ("18:01", "00:00", "02:00", "09:31", "16:00")], [1, 360, 480, 931, 1320])

    def test_sm_of_refuses_the_break(self):
        for x in ("16:01", "17:00", "18:00"):
            with self.assertRaises(ValueError):
                g.sm_of(x)

    def test_sunday_evening_belongs_to_monday(self):
        path = self.write(["20210307 180100", "20210308 093100"])
        days = g.load_days(path)
        self.assertEqual([d.date for d in days], ["2021-03-08"])
        self.assertEqual(len(days[0].bars), 2)
        self.assertEqual([b.sm for b in days[0].bars], [1, 931])
        self.assertEqual(days[0].by_sm, {1: 0, 931: 1})

    def test_bar_after_midnight_same_trading_day(self):
        path = self.write(["20210308 230000", "20210309 010000"])
        days = g.load_days(path)
        self.assertEqual([d.date for d in days], ["2021-03-09"])
        self.assertEqual([b.sm for b in days[0].bars], [300, 420])
        self.assertEqual([b.dt.isoformat(" ") for b in days[0].bars], ["2021-03-08 23:00:00", "2021-03-09 01:00:00"])

    def test_break_bars_dropped(self):
        path = self.write(["20210308 160000", "20210308 163000", "20210308 180000", "20210308 180100"])
        days = g.load_days(path)
        self.assertEqual([d.date for d in days], ["2021-03-08", "2021-03-09"])
        self.assertEqual([b.dt.strftime("%H%M%S") for b in days[0].bars], ["160000"])
        self.assertEqual([b.dt.strftime("%H%M%S") for b in days[1].bars], ["180100"])

    def test_duplicate_stamp_raises(self):
        path = self.write(["20210308 093100", "20210308 093100"])
        with self.assertRaises(ValueError):
            g.load_days(path)

    def test_out_of_order_stamp_raises(self):
        path = self.write(["20210308 093200", "20210308 093100"])
        with self.assertRaises(ValueError):
            g.load_days(path)

    def test_bar_values_kept(self):
        path = os.path.join(self.tmp, "bars.txt")
        with open(path, "w") as fh:
            fh.write("20210308 093100;13000.25;13010;12990.5;13005.75;123\n")
        b = g.load_days(path)[0].bars[0]
        self.assertEqual((b.o, b.h, b.l, b.c, b.v), (13000.25, 13010.0, 12990.5, 13005.75, 123))

    def test_friday_and_saturday_evenings_and_weekend_days_dropped(self):
        # 2021-03-12 is a Friday. Its evening, Saturday's and Sunday's daytime stamps and Saturday's
        # evening belong to no trading day; Sunday evening belongs to Monday 2021-03-15.
        path = self.write(["20210312 160000", "20210312 180500", "20210313 100000", "20210313 180500",
                           "20210314 100000", "20210314 180500", "20210315 093100"])
        days = g.load_days(path)
        self.assertEqual([d.date for d in days], ["2021-03-12", "2021-03-15"])
        self.assertEqual([b.dt.isoformat(" ") for b in days[1].bars], ["2021-03-14 18:05:00", "2021-03-15 09:31:00"])

    def test_holiday_with_only_overnight_bars_is_kept(self):
        # A weekday whose only bars are the evening before and the early morning is still a trading day.
        path = self.write(["20210315 180100", "20210316 080000", "20210317 093100"])
        days = g.load_days(path)
        self.assertEqual([d.date for d in days], ["2021-03-16", "2021-03-17"])
        self.assertEqual(len(days[0].bars), 2)

    def test_half_day_keeps_every_bar_to_its_last(self):
        # An early close is not cut: bars stay up to the last one in the file.
        path = self.write(["20211126 093100", "20211126 131400", "20211126 131500"])
        days = g.load_days(path)
        self.assertEqual([b.sm for b in days[0].bars], [931, 1154, 1155])

    def test_tradable_end_gap_of_exactly_60_minutes_does_not_end_the_day(self):
        path = self.write(["20210316 093100", "20210316 103100", "20210316 103200"])
        (day,) = g.load_days(path)
        self.assertEqual(g.tradable_end(day), 2)

    def test_tradable_end_gap_of_61_minutes_ends_the_day(self):
        path = self.write(["20210316 093100", "20210316 103200", "20210316 103300"])
        (day,) = g.load_days(path)
        self.assertEqual(g.tradable_end(day), 0)
        self.assertEqual(len(day.bars), 3)           # load_days keeps every bar; only the helper cuts
        self.assertEqual(g.tradable_end(day, max_gap_minutes=61), 2)

    def test_tradable_end_only_the_first_hole_counts(self):
        # holes 09:32 -> 11:00 and 11:01 -> 13:00; the day's tradable bars end at 09:32
        path = self.write(["20210316 093100", "20210316 093200", "20210316 110000", "20210316 110100",
                           "20210316 130000"])
        (day,) = g.load_days(path)
        self.assertEqual(g.tradable_end(day), 1)

    def test_tradable_end_hole_across_midnight(self):
        # trading day 2021-03-16: evening 19:00 on the 15th, then 05:34 on the 16th
        path = self.write(["20210315 185900", "20210315 190000", "20210316 053400", "20210316 053500"])
        (day,) = g.load_days(path)
        self.assertEqual(g.tradable_end(day), 1)
        # 23:59 -> 00:00 is one minute, not a hole
        path = self.write(["20210315 235900", "20210316 000000", "20210316 000100"])
        (day,) = g.load_days(path)
        self.assertEqual(g.tradable_end(day), 2)

    def test_tradable_end_no_gap(self):
        path = self.write(["20210316 093100", "20210316 093200", "20210316 093300", "20210317 093100"])
        days = g.load_days(path)
        self.assertEqual(g.tradable_end(days[0]), 2)
        self.assertEqual(g.tradable_end(days[1]), 0)    # a one-bar day

    def test_range_is_by_trading_day(self):
        # The evening of the day before `start` belongs to `start`; the evening of `end` belongs to the
        # day after and is not loaded.
        path = self.write(["20210307 180100", "20210308 093100", "20210309 093100", "20210309 180100"])
        days = g.load_days(path, start="2021-03-08", end="2021-03-09")
        self.assertEqual([d.date for d in days], ["2021-03-08", "2021-03-09"])
        self.assertEqual(len(days[0].bars), 2)
        self.assertEqual(len(days[1].bars), 1)


@unittest.skipUnless(os.path.exists(DATA), "data file absent")
class RealFile(unittest.TestCase):
    def test_real_file_matches_rth_loader(self):
        sys.path.insert(0, os.path.join(REPO, "scripts", "wf", "oracle"))
        import market as mk   # noqa: E402
        market = mk.load_market(DATA, session_start="09:31")
        days = g.load_days(DATA)
        self.assertEqual([d.date for d in days], sorted(set(d.date for d in days)))
        by_date = {d.date: d for d in days}
        compared = 0
        for s in market.sessions:
            day = by_date.get(s.date)
            self.assertIsNotNone(day, "session %s has no Globex day" % s.date)
            last = s.bars[-1].dt
            mine = [(b.dt, b.o, b.h, b.l, b.c, b.v) for b in day.bars
                    if b.sm >= 931 and b.dt <= last]
            theirs = [(b.dt, b.o, b.h, b.l, b.c, b.v) for b in s.bars]
            self.assertEqual(mine, theirs, "session %s differs" % s.date)
            compared += 1
        self.assertGreater(compared, 1300)
        for d in days:
            self.assertEqual(d.by_sm, {b.sm: i for i, b in enumerate(d.bars)})
            self.assertTrue(all(1 <= b.sm <= 1320 for b in d.bars))


if __name__ == "__main__":
    unittest.main()
