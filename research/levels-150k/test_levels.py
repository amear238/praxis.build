#!/usr/bin/env python3
"""Tests for levels.py: the clock, the traded contract, the roll shift, and the seven kinds of level
(research/levels-150k/PLAN.md, "Candidate 1 ... The exact rule"). Synthetic bars, tiny prices.
Run: python3 -I -B research/levels-150k/test_levels.py"""
import datetime as dt
import os
import sys
import unittest
from zoneinfo import ZoneInfo

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import levels  # noqa: E402
import mdata  # noqa: E402

ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
SPEC = {"traded": "MNQ", "pv": 2.0, "tick": 0.25, "comm": 1.90, "slip_ticks": 2, "max_qty": 90}


def ts(y, m, d, hh, mm):
    return int(dt.datetime(y, m, d, hh, mm, tzinfo=ET).timestamp()) * 10 ** 9


def bar(t, o, h, l, c, v=1, iid=1):
    return mdata.Bar(t, iid, float(o), float(h), float(l), float(c), v)


def daily_before(date, n=20, rng=10.0):
    """n daily bars dated (UTC) on the n calendar days before `date`, each with range `rng`."""
    out = []
    for i in range(n, 0, -1):
        d = date - dt.timedelta(days=i)
        t = int(dt.datetime(d.year, d.month, d.day, tzinfo=UTC).timestamp()) * 10 ** 9
        b = mdata.Bar(t, 1, 100.0, 100.0 + rng, 100.0, 105.0, 1)
        out.append(mdata.Adj(b, b.open, b.high, b.low, b.close))
    return out


def day_of(mk, iso):
    return next(d for d in mk.days if d.date == iso)


MON, TUE, WED = dt.date(2024, 1, 8), dt.date(2024, 1, 9), dt.date(2024, 1, 10)


def two_sessions(shift_iid=False):
    """S(Mon 2024-01-08) and S(Tue 2024-01-09). Monday: overnight high 120 / low 95, day high 130 / low 90.
    Tuesday overnight: 18:00-19:59 Monday evening high 118 / low 101, from 20:00 high 116 / low 99; 09:30 open 110."""
    two = 2 if shift_iid else 1
    return [
        bar(ts(2024, 1, 7, 18, 0), 100, 120, 100, 110),
        bar(ts(2024, 1, 8, 3, 0), 100, 101, 95, 100),
        bar(ts(2024, 1, 8, 9, 30), 105, 106, 104, 105),
        bar(ts(2024, 1, 8, 11, 0), 105, 130, 104, 120),
        bar(ts(2024, 1, 8, 14, 0), 105, 106, 90, 100),
        bar(ts(2024, 1, 8, 16, 30), 100, 101, 99, 100),
        bar(ts(2024, 1, 8, 18, 0), 110, 118, 101, 110),
        bar(ts(2024, 1, 8, 20, 0), 110, 116, 99, 110, iid=two),
        bar(ts(2024, 1, 9, 9, 30), 110, 111, 109, 110, iid=two),
        bar(ts(2024, 1, 9, 10, 0), 110, 111, 109, 110, iid=two),
    ]


class Clock(unittest.TestCase):
    def test_session_date_is_the_wall_clock_plus_seven_hours(self):
        self.assertEqual(levels.session_date(ts(2024, 1, 7, 18, 0)), "2024-01-08")
        self.assertEqual(levels.session_date(ts(2024, 1, 8, 16, 59)), "2024-01-08")
        self.assertEqual(levels.session_date(ts(2024, 1, 8, 17, 0)), "2024-01-09")
        self.assertEqual(levels.session_date(ts(2024, 3, 10, 18, 0)), "2024-03-11")   # first evening of summer time
        self.assertEqual(levels.session_date(ts(2024, 11, 3, 18, 0)), "2024-11-04")   # first evening of winter time

    def test_a_trading_date_needs_a_minute_from_930_to_before_355(self):
        mins = [bar(ts(2024, 1, 8, 3, 0), 1, 1, 1, 1), bar(ts(2024, 1, 8, 15, 55), 1, 1, 1, 1),
                bar(ts(2024, 1, 9, 15, 54), 1, 1, 1, 1), bar(ts(2024, 1, 10, 9, 29), 1, 1, 1, 1),
                bar(ts(2024, 1, 11, 9, 30), 1, 1, 1, 1)]
        mk = levels.Market(mins, daily_before(dt.date(2024, 1, 12)), [], SPEC, "NQ")
        self.assertEqual([d.date for d in mk.days], ["2024-01-09", "2024-01-11"])

    def test_p0_iid_and_atr(self):
        mk = levels.Market(two_sessions(True), daily_before(TUE, rng=8.0), [mdata.Roll(ts(2024, 1, 8, 20, 0), 1, 2, 5.0)], SPEC, "NQ")
        d = day_of(mk, "2024-01-09")
        self.assertEqual((d.p0, d.iid, d.atr), (110.0, 2, 8.0))

    def test_no_atr_before_fourteen_daily_bars(self):
        mk = levels.Market(two_sessions(), daily_before(TUE, n=13), [], SPEC, "NQ")
        self.assertIsNone(day_of(mk, "2024-01-09").atr)

    def test_atr_reads_only_daily_bars_dated_before_the_day(self):
        daily = daily_before(TUE, rng=8.0)
        t = int(dt.datetime(2024, 1, 9, tzinfo=UTC).timestamp()) * 10 ** 9
        big = mdata.Bar(t, 1, 100.0, 1000.0, 100.0, 100.0, 1)
        daily.append(mdata.Adj(big, 100.0, 1000.0, 100.0, 100.0))
        mk = levels.Market(two_sessions(), daily, [], SPEC, "NQ")
        self.assertEqual(day_of(mk, "2024-01-09").atr, 8.0)


def prices(day, kind):
    return sorted(lv.price for lv in day.levels.get(kind) or [])


class Grid(unittest.TestCase):
    def test_a_half_tick_rounds_up(self):
        spec = dict(SPEC, tick=0.0001)
        mins = [bar(ts(2024, 1, 8, 10, 0), 1.17, 1.17325, 1.16985, 1.17), bar(ts(2024, 1, 9, 9, 30), 1.17, 1.17, 1.17, 1.17)]
        d = day_of(levels.Market(mins, daily_before(TUE, rng=0.01), [], spec, "6E"), "2024-01-09")
        got = prices(d, "PD")
        self.assertAlmostEqual(got[1], 1.1733, places=9)
        self.assertAlmostEqual(got[0], 1.1699, places=9)

    def test_hourly_bars_go_by_the_utc_hour(self):
        # 1:10 AM summer time and 1:10 AM winter time on 2024-11-03 are two bars
        t1 = int(dt.datetime(2024, 11, 3, 5, 10, tzinfo=UTC).timestamp()) * 10 ** 9
        t2 = int(dt.datetime(2024, 11, 3, 6, 10, tzinfo=UTC).timestamp()) * 10 ** 9
        mk = levels.Market([bar(t1, 1, 1, 1, 1), bar(t2, 1, 1, 1, 1)], [], [], SPEC, "NQ")
        self.assertEqual(len(mk.hbars), 2)


class PriorDayOvernightWeek(unittest.TestCase):
    def test_a_flip_flop_joins_by_the_first_roll_after_the_minute(self):
        mins = two_sessions(True)
        rolls = [mdata.Roll(ts(2024, 1, 8, 19, 0), 1, 2, 5.0), mdata.Roll(ts(2024, 1, 8, 19, 30), 2, 1, -5.0),
                 mdata.Roll(ts(2024, 1, 8, 19, 45), 1, 2, 6.0)]
        d = day_of(levels.Market(mins, daily_before(TUE), rolls, SPEC, "NQ"), "2024-01-09")
        self.assertEqual(prices(d, "PD"), [95.0, 135.0])     # + 5, the first roll after Monday's minutes


    def test_pd_is_the_whole_prior_session_and_on_the_overnight_before_930(self):
        mk = levels.Market(two_sessions(), daily_before(TUE), [], SPEC, "NQ")
        d = day_of(mk, "2024-01-09")
        self.assertEqual(prices(d, "PD"), [90.0, 130.0])
        self.assertEqual(prices(d, "ON"), [99.0, 118.0])

    def test_a_minute_from_1700_belongs_to_the_next_session(self):
        mins = two_sessions() + [bar(ts(2024, 1, 8, 17, 0), 110, 125, 100, 110)]
        mins.sort(key=lambda b: b.ts)
        d = day_of(levels.Market(mins, daily_before(TUE), [], SPEC, "NQ"), "2024-01-09")
        self.assertEqual(prices(d, "ON"), [99.0, 125.0])
        self.assertEqual(prices(d, "PD"), [90.0, 130.0])

    def test_older_contract_minutes_move_by_the_roll_gap(self):
        mk = levels.Market(two_sessions(True), daily_before(TUE), [mdata.Roll(ts(2024, 1, 8, 20, 0), 1, 2, 5.0)], SPEC, "NQ")
        d = day_of(mk, "2024-01-09")
        self.assertEqual(prices(d, "PD"), [95.0, 135.0])
        self.assertEqual(prices(d, "ON"), [99.0, 123.0])     # 118 + 5 from contract 1; 99 on contract 2

    def test_a_chain_of_rolls_adds_every_gap(self):
        mins = two_sessions(True)
        mins = [b._replace(iid=7) if b.ts < ts(2024, 1, 8, 12, 0) else b for b in mins]
        rolls = [mdata.Roll(ts(2024, 1, 8, 12, 0), 7, 1, 2.0), mdata.Roll(ts(2024, 1, 8, 20, 0), 1, 2, 5.0)]
        d = day_of(levels.Market(mins, daily_before(TUE), rolls, SPEC, "NQ"), "2024-01-09")
        self.assertEqual(prices(d, "PD"), [95.0, 137.0])     # 130 + 2 + 5 on contract 7, 90 + 5 on contract 1

    def test_a_contract_that_cannot_be_joined_drops_the_level(self):
        mins = two_sessions(True)
        mins[1] = mins[1]._replace(iid=9)
        d = day_of(levels.Market(mins, daily_before(TUE), [mdata.Roll(ts(2024, 1, 8, 20, 0), 1, 2, 5.0)], SPEC, "NQ"), "2024-01-09")
        self.assertEqual(prices(d, "PD"), [])
        self.assertEqual(prices(d, "ON"), [99.0, 123.0])

    def test_pw_is_the_prior_iso_week(self):
        mins = [bar(ts(2024, 1, 3, 10, 0), 50, 60, 40, 50),      # Wed of ISO week 1
                bar(ts(2024, 1, 4, 10, 0), 50, 70, 45, 50),      # Thu of ISO week 1
                bar(ts(2024, 1, 4, 18, 0), 50, 99, 1, 50),       # session Fri 01-05, no day minute: not a trading date
                bar(ts(2024, 1, 8, 10, 0), 50, 80, 30, 50),      # Mon of week 2
                bar(ts(2024, 1, 9, 9, 30), 50, 51, 49, 50)]      # Tue of week 2
        mk = levels.Market(mins, daily_before(TUE), [], SPEC, "NQ")
        self.assertEqual(prices(day_of(mk, "2024-01-09"), "PW"), [40.0, 70.0])
        self.assertEqual(prices(day_of(mk, "2024-01-08"), "PW"), [40.0, 70.0])


def hourly_minutes(day, hours_highs_lows, iid=1):
    """One minute in each listed clock hour of the session ending on `day` (hour 18..23 belong to the evening before)."""
    out = []
    for hh, h, l in hours_highs_lows:
        cal = day - dt.timedelta(days=1) if hh >= 17 else day
        out.append(bar(ts(cal.year, cal.month, cal.day, hh, 10), (h + l) / 2, h, l, (h + l) / 2, iid=iid))
    return out


def quiet_dates(day, n, h=10.0, l=9.0):
    """One minute at 10:00 on each of the n weekdays before `day`: n prior trading dates, one hourly bar each."""
    out, d = [], day
    while len(out) < n:
        d -= dt.timedelta(days=1)
        if d.weekday() < 5:
            out.append(bar(ts(d.year, d.month, d.day, 10, 0), h, h, l, h))
    return out


class Swings(unittest.TestCase):
    def build(self, extra=(), prior=5):
        hl = [(18, 10, 9), (19, 11, 9), (20, 12, 9), (21, 20, 9), (22, 13, 9), (23, 12, 9), (0, 11, 9),
              (1, 10, 9), (2, 10, 3), (3, 10, 9), (4, 10, 9), (5, 10, 9), (6, 10, 9), (7, 10, 9), (8, 10, 9)]
        mins = hourly_minutes(TUE, hl) + list(extra) + [bar(ts(2024, 1, 9, 9, 30), 10, 10, 10, 10)]
        mins += quiet_dates(TUE, prior)
        mins.sort(key=lambda b: b.ts)
        return day_of(levels.Market(mins, daily_before(TUE), [], SPEC, "NQ"), "2024-01-09")

    def test_swings_need_five_prior_trading_dates(self):
        self.assertEqual(self.build(prior=4).levels.get("SW"), None)

    def test_a_swing_needs_three_lower_bars_each_side(self):
        d = self.build()
        self.assertEqual([lv.price for lv in d.levels["SW"] if lv.price > 15], [20.0])

    def test_a_swing_low(self):
        self.assertEqual([lv.price for lv in self.build().levels["SW"] if lv.price < 5], [3.0])

    def test_an_equal_neighbour_is_not_a_swing(self):
        hl = [(18, 10, 9), (19, 11, 9), (20, 12, 9), (21, 20, 9), (22, 20, 9), (23, 12, 9), (0, 11, 9),
              (1, 10, 9), (2, 10, 9), (3, 10, 9), (4, 10, 9)]
        mins = hourly_minutes(TUE, hl) + [bar(ts(2024, 1, 9, 9, 30), 10, 10, 10, 10)] + quiet_dates(TUE, 5)
        mins.sort(key=lambda b: b.ts)
        d = day_of(levels.Market(mins, daily_before(TUE), [], SPEC, "NQ"), "2024-01-09")
        self.assertEqual([lv.price for lv in d.levels["SW"] if lv.price > 15], [])

    def test_a_later_minute_one_tick_through_breaks_it(self):
        through = bar(ts(2024, 1, 9, 9, 15), 15, 20.25, 15, 15)
        at = bar(ts(2024, 1, 9, 9, 15), 15, 20.0, 15, 15)
        self.assertEqual([lv.price for lv in self.build([through]).levels["SW"] if lv.price > 15], [])
        self.assertEqual([lv.price for lv in self.build([at]).levels["SW"] if lv.price > 15], [20.0])

    def test_the_bar_from_900_is_not_used(self):
        # the 6:00 bar (20) has the 7:00 and 8:00 bars after it; only the 9:00 bar would make the third
        hl = [(18, 10, 9), (19, 10, 9), (20, 10, 9), (21, 10, 9), (22, 10, 9), (23, 10, 9), (0, 10, 9),
              (1, 10, 9), (2, 10, 9), (3, 10, 9), (4, 10, 9), (5, 10, 9), (6, 20, 9), (7, 12, 9), (8, 12, 9),
              (9, 11, 9)]
        mins = hourly_minutes(TUE, hl) + quiet_dates(TUE, 5)
        mins.append(bar(ts(2024, 1, 9, 9, 30), 10, 10, 10, 10))
        mins.sort(key=lambda b: b.ts)
        d = day_of(levels.Market(mins, daily_before(TUE), [], SPEC, "NQ"), "2024-01-09")
        self.assertEqual(d.levels["SW"], [])


class RoundNumbers(unittest.TestCase):
    def test_multiples_of_the_step_near_p0(self):
        mins = [bar(ts(2024, 1, 9, 9, 30), 1050, 1050, 1050, 1050)]
        d = day_of(levels.Market(mins, daily_before(TUE, rng=100.0), [], SPEC, "NQ"), "2024-01-09")
        got = prices(d, "RN")
        for p in (900.0, 1000.0, 1100.0, 1200.0):
            self.assertIn(p, got)
        self.assertNotIn(1050.0, got)

    def test_yen_levels_are_half_yens_in_dollar_yen(self):
        spec = dict(SPEC, tick=0.000001, traded="MJY")
        mins = [bar(ts(2024, 1, 9, 9, 30), 0.0067, 0.0067, 0.0067, 0.0067)]
        d = day_of(levels.Market(mins, daily_before(TUE, rng=0.00005), [], spec, "6J"), "2024-01-09")
        got = prices(d, "RN")
        self.assertIn(round(1 / 149.5 / 0.000001) * 0.000001, got)
        self.assertIn(round(1 / 149.0 / 0.000001) * 0.000001, got)


class VolumeProfile(unittest.TestCase):
    def test_poc_and_value_area(self):
        # S(Mon): volume per tick (price: volume) built from three minutes on a 1-point tick grid
        spec = dict(SPEC, tick=1.0)
        mins = [bar(ts(2024, 1, 8, 10, 0), 10, 12, 10, 11, v=30),     # 10, 11, 12: 10 each
                bar(ts(2024, 1, 8, 11, 0), 11, 11, 11, 11, v=50),     # 11: 50
                bar(ts(2024, 1, 8, 12, 0), 13, 16, 13, 14, v=8),      # 13..16: 2 each
                bar(ts(2024, 1, 9, 9, 30), 20, 20, 20, 20)]
        d = day_of(levels.Market(mins, daily_before(TUE), [], spec, "NQ"), "2024-01-09")
        # total 88; POC 11 (60); add 10 vs 12 -> tie (10, 10): both -> 80 >= 61.6 stop. VA 10..12
        self.assertEqual(prices(d, "VP"), [10.0, 11.0, 12.0])

    def test_volume_is_split_exactly(self):
        # 120..124 get 1/10 + 1/5, 100..109 get 3/10: an exact tie. Nearest the midpoint 114.5: 109 and 120, then
        # the lower, 109. In floats 0.1 + 0.2 > 0.3 and 120 would win.
        spec = dict(SPEC, tick=1.0)
        mins = [bar(ts(2024, 1, 8, 10, 0), 120, 129, 120, 120, v=1),  # 120..129, 1/10 each
                bar(ts(2024, 1, 8, 11, 0), 120, 124, 120, 120, v=1),  # 120..124, 1/5 each
                bar(ts(2024, 1, 8, 12, 0), 100, 109, 100, 100, v=3),  # 100..109, 3/10 each
                bar(ts(2024, 1, 9, 9, 30), 130, 130, 130, 130)]
        d = day_of(levels.Market(mins, daily_before(TUE), [], spec, "NQ"), "2024-01-09")
        self.assertEqual([lv.price for lv in d.levels["VP"] if lv.role == "poc"], [109.0])

    def test_poc_tie_goes_nearest_the_midpoint_then_lower(self):
        spec = dict(SPEC, tick=1.0)
        mins = [bar(ts(2024, 1, 8, 10, 0), 10, 10, 10, 10, v=5),
                bar(ts(2024, 1, 8, 11, 0), 14, 14, 14, 14, v=5),
                bar(ts(2024, 1, 8, 12, 0), 18, 18, 18, 18, v=5),
                bar(ts(2024, 1, 9, 9, 30), 20, 20, 20, 20)]
        d = day_of(levels.Market(mins, daily_before(TUE), [], spec, "NQ"), "2024-01-09")
        self.assertIn(14.0, prices(d, "VP"))                  # midpoint (10 + 18) / 2 = 14
        self.assertEqual([lv.price for lv in d.levels["VP"] if lv.role == "poc"], [14.0])


class Zones(unittest.TestCase):
    def build(self, after=(), prior=10):
        # ten bars of range 2 then base (range 0.5, 0.5) and an impulse of range 10 closing above the base
        hl = [(18, 12, 10), (19, 12, 10), (20, 12, 10), (21, 12, 10), (22, 12, 10), (23, 12, 10), (0, 12, 10),
              (1, 11.5, 11), (2, 11.25, 10.75), (3, 21, 11), (4, 22, 20), (5, 22, 20), (6, 22, 20), (7, 22, 20),
              (8, 22, 20)]
        mins = hourly_minutes(TUE, hl)
        mins[9] = mins[9]._replace(close=21.0)                # the impulse closes at 21, above 11.5
        mins += list(after) + [bar(ts(2024, 1, 9, 9, 30), 21, 21, 21, 21)] + quiet_dates(TUE, prior, 10.0, 10.0)
        mins.sort(key=lambda b: b.ts)
        return day_of(levels.Market(mins, daily_before(TUE), [], SPEC, "NQ"), "2024-01-09")

    def test_zones_need_ten_prior_trading_dates(self):
        self.assertEqual(self.build(prior=9).levels.get("SD"), None)

    def test_a_demand_zone_from_the_longest_base(self):
        z = [lv for lv in self.build().levels["SD"] if lv.role == "demand"]
        self.assertEqual([(lv.price, lv.far) for lv in z], [(11.5, 10.75)])

    def test_a_visit_after_the_impulse_removes_it(self):
        visit = bar(ts(2024, 1, 9, 9, 10), 15, 15, 11.25, 15)
        self.assertEqual([lv for lv in self.build([visit]).levels["SD"] if lv.role == "demand"], [])

    def test_a_touch_without_a_tick_through_keeps_it(self):
        touch = bar(ts(2024, 1, 9, 9, 10), 15, 15, 11.5, 15)
        self.assertEqual(len([lv for lv in self.build([touch]).levels["SD"] if lv.role == "demand"]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=1)
