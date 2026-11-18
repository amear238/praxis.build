#!/usr/bin/env python3
"""test_rule_check.py -- tests of rule_check.py, the independent rule check of momentum into the close
(PLAN.md, "Data and markets", "The exact rule" and the amendment of 2026-11-18). Small synthetic bars. Every
expected figure is worked by hand from the plan's words (in the comments), and every stamp is built from a fixed
UTC offset, not the tz database, so the check's New York clock is tested against something independent.

NQ figures unless a test says otherwise: tick 0.25, slip 2 ticks = 0.5. Daily ranges 40 -> A = 40, k 0.025 ->
dist = floor_tick(1.0) = 1.0. Run: python3 -I -B test_rule_check.py
"""
import importlib.util
import os
import sys
import unittest
from datetime import date, timedelta

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("cm_rule_check", os.path.join(_HERE, "rule_check.py"))
rc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rc)
_TREND = os.path.normpath(os.path.join(_HERE, "..", "trend-150k"))
if _TREND not in sys.path:
    sys.path.append(_TREND)
import mdata  # noqa: E402
import specs  # noqa: E402

NS = 10 ** 9
EST, EDT = -5, -4
_EPOCH = date(1970, 1, 1).toordinal()
D0, D1, D2, D3 = date(2024, 1, 9), date(2024, 1, 10), date(2024, 1, 11), date(2024, 1, 12)   # Tue..Fri, EST
TE = 0.25 * 1e-7    # a tenth of NQ's eps (tick x 10^-6): inside the tolerance
TO = 0.25 * 1e-5    # ten of NQ's eps: outside it


def utc(d, hh, mm, off=EST):
    """hh:mm at the fixed offset `off` hours on date d, as UTC nanoseconds (no tz database)."""
    return ((d.toordinal() - _EPOCH) * 86400 + hh * 3600 + mm * 60 - off * 3600) * NS


def settings(signal="S1", k=0.025, atr_days=14):
    return {"name": f"{signal}-k{k}", "signal": signal, "k": k, "atr_days": atr_days}


def daily_bars(last_day, ranges, base=1000.0, first_iid=7):
    """One daily bar per calendar day ending last_day, stamped 00:00 UTC, with these adjusted ranges. The raw bar's
    range is a quarter of the adjusted one: real back-adjusted bars have equal ranges, so this only pins that the
    adjusted fields are the ones read (C9)."""
    out, n = [], len(ranges)
    for i, r in enumerate(ranges):
        d = last_day - timedelta(days=n - 1 - i)
        ts = (d.toordinal() - _EPOCH) * 86400 * NS
        raw = mdata.Bar(ts, first_iid, base - 100, base - 100 + r / 4, base - 100, base - 100, 1)
        out.append(mdata.Adj(raw, base, base + r / 2, base - r / 2, base))
    return out


class Scene:
    """Minute bars for one market, put bar by bar (a later put at the same stamp replaces the earlier)."""

    def __init__(self, market="NQ", iid=7):
        self.market, self.spec, self.iid = market, specs.SPECS[market], iid
        self.bars = {}
        self.daily = daily_bars(D0, [40.0] * 20)

    def put(self, d, hh, mm, o, h=None, l=None, c=None, iid=None, off=EST):
        c = o if c is None else c
        h = max(o, c) if h is None else h
        l = min(o, c) if l is None else l
        ts = utc(d, hh, mm, off)
        self.bars[ts] = mdata.Bar(ts, self.iid if iid is None else iid, o, h, l, c, 1)
        return ts

    def span(self, d, start, end, o, h, l, c, off=EST, iid=None):
        """A bar every minute from start up to, not including, end ((hh, mm) pairs)."""
        for t in range(start[0] * 60 + start[1], end[0] * 60 + end[1]):
            self.put(d, t // 60, t % 60, o, h, l, c, iid=iid, off=off)

    def drop(self, d, start, end, off=EST):
        lo, hi = utc(d, *start, off), utc(d, *end, off)
        for ts in [t for t in self.bars if lo <= t < hi]:
            del self.bars[ts]

    def minutes(self):
        return [self.bars[t] for t in sorted(self.bars)]

    def run(self, signal="S1", k=0.025, fill="midpoint", first=None, last=None, atr_days=14):
        return rc.replay_market(self.minutes(), self.daily, [], self.spec, settings(signal, k, atr_days), fill,
                                self.market, first, last)

    def one(self, *a, **kw):
        tr = self.run(*a, **kw)
        assert len(tr) == 1, tr
        return tr[0]

    def days(self, signal="S1", k=0.025, fill="midpoint"):
        return rc.replay_days(self.minutes(), self.daily, [], self.spec, settings(signal, k), fill, self.market)


def y_bar(s, d, o=1000.0, off=EST, iid=None):
    """The bar at C = 16:00 on the day before: Y = its open (its close is 0.25 higher)."""
    s.put(d, 16, 0, o, o + 0.5, o - 0.5, o + 0.25, off=off, iid=iid)


def long_day(s, d, off=EST):
    """The standard long day: s2 = 1002.0 (09:59 close), s1 = 1004.5 (15:29 close), entry bar 15:30 opens 1005.0
    -> entry 1005.5 (inside its high 1006), stop 1004.5; watched lows 1005.0; exit bar 16:00 opens 1007.0 ->
    exit 1006.5. worst = the entry bar's low 1004.75 - 1005.5 = -0.75."""
    s.put(d, 9, 55, 1001.0, 1002.0, 1000.75, 1001.5, off=off)
    s.put(d, 9, 59, 1001.5, 1002.5, 1001.25, 1002.0, off=off)
    s.put(d, 15, 29, 1004.0, 1005.0, 1003.75, 1004.5, off=off)
    s.put(d, 15, 30, 1005.0, 1006.0, 1004.75, 1005.5, off=off)
    s.span(d, (15, 31), (16, 0), 1005.5, 1006.0, 1005.0, 1005.5, off=off)
    s.put(d, 16, 0, 1007.0, 1007.5, 1006.0, 1007.0, off=off)


def short_day(s, d, off=EST):
    """The standard short day: s2 = 998.0, s1 = 995.5, entry bar opens 995.0 -> entry 994.5 (inside its low 994.0),
    stop 995.5; watched highs 995.0; exit bar opens 993.0 -> exit 993.5. worst = 994.5 - the entry bar's high
    995.25 = -0.75."""
    s.put(d, 9, 59, 999.0, 999.25, 997.75, 998.0, off=off)
    s.put(d, 15, 29, 996.0, 996.25, 995.0, 995.5, off=off)
    s.put(d, 15, 30, 995.0, 995.25, 994.0, 994.5, off=off)
    s.span(d, (15, 31), (16, 0), 994.5, 995.0, 994.0, 994.5, off=off)
    s.put(d, 16, 0, 993.0, 994.0, 992.5, 993.0, off=off)


def long_scene():
    s = Scene()
    y_bar(s, D0)
    long_day(s, D1)
    return s


def short_scene():
    s = Scene()
    y_bar(s, D0)
    short_day(s, D1)
    return s


LONG = {"market": "NQ", "date": "2024-01-10", "signal": "S1", "side": 1, "y": 1000.0, "s1": 1004.5, "s2": 1002.0,
        "atr": 40.0, "dist": 1.0, "entry_ts": utc(D1, 15, 30), "entry": 1005.5, "stop": 1004.5,
        "exit_ts": utc(D1, 16, 0), "exit": 1006.5, "reason": "close", "gap": False, "points": 1.0, "worst": -0.75}
SHORT = {"market": "NQ", "date": "2024-01-10", "signal": "S1", "side": -1, "y": 1000.0, "s1": 995.5, "s2": 998.0,
         "atr": 40.0, "dist": 1.0, "entry_ts": utc(D1, 15, 30), "entry": 994.5, "stop": 995.5,
         "exit_ts": utc(D1, 16, 0), "exit": 993.5, "reason": "close", "gap": False, "points": 1.0, "worst": -0.75}


def with_(base, **kw):
    t = dict(base)
    t.update(kw)
    return t


# ------------------------------------------------------------------------------------------------ the record
class TestRecord(unittest.TestCase):
    def test_long_record_exactly(self):
        t = long_scene().one()
        self.assertEqual(t, LONG)
        self.assertEqual(list(t), list(rc.FIELDS))

    def test_short_record_exactly(self):
        self.assertEqual(short_scene().one(), SHORT)

    def test_field_list_is_the_amendments(self):
        self.assertEqual(rc.FIELDS, ("market", "date", "signal", "side", "y", "s1", "s2", "atr", "dist",
                                     "entry_ts", "entry", "stop", "exit_ts", "exit", "reason", "gap", "points",
                                     "worst"))

    def test_types(self):
        t = long_scene().one()
        self.assertIs(type(t["side"]), int)
        self.assertIs(type(t["gap"]), bool)
        self.assertIs(type(t["entry_ts"]), int)
        self.assertIs(type(t["exit_ts"]), int)

    def test_signal_field_is_the_settings(self):
        s = long_scene()
        self.assertEqual(s.one(signal="S2")["signal"], "S2")
        self.assertEqual(s.one(signal="S3")["signal"], "S3")

    def test_fill_does_not_touch_entry_or_close_exit(self):
        s = long_scene()
        for fill in rc.FILLS:
            self.assertEqual(s.one(fill=fill), LONG)

    def test_unknown_fill_or_signal_or_market_refused(self):
        s = long_scene()
        with self.assertRaises(ValueError):
            s.run(fill="mid")
        with self.assertRaises(ValueError):
            s.run(signal="S4")
        with self.assertRaises(ValueError):
            rc.replay_market(s.minutes(), s.daily, [], s.spec, settings(), "midpoint", "YM")

    def test_unsorted_minutes_refused(self):
        m = long_scene().minutes()
        m[3], m[4] = m[4], m[3]
        with self.assertRaises(ValueError):
            rc.replay_market(m, Scene().daily, [], specs.SPECS["NQ"], settings(), "midpoint", "NQ")

    def test_same_minutes_other_daily_bars(self):
        s = long_scene()
        m = s.minutes()
        sp = settings()
        a = rc.replay_market(m, daily_bars(D0, [40.0] * 20), [], s.spec, sp, "midpoint", "NQ")
        b = rc.replay_market(m, daily_bars(D0, [47.0] * 20), [], s.spec, sp, "midpoint", "NQ")
        self.assertEqual((a[0]["atr"], b[0]["atr"]), (40.0, 47.0))

    def test_no_minutes_no_trades(self):
        self.assertEqual(rc.replay_market([], Scene().daily, [], specs.SPECS["NQ"], settings(), "midpoint", "NQ"),
                         [])


# ------------------------------------------------------------------------------------------------ rule 1
class TestReferencePrices(unittest.TestCase):
    def test_price_at_is_first_bar_open_within_five_minutes(self):
        s = long_scene()
        s.drop(D1, (15, 30), (15, 34))                     # the entry bar is now 15:34, the last of [15:30, 15:35)
        s.put(D1, 15, 34, 1005.0, 1006.0, 1004.75, 1005.5)
        t = s.one()
        self.assertEqual(t["entry_ts"], utc(D1, 15, 34))
        self.assertEqual(t["entry"], 1005.5)

    def test_price_at_window_ends_before_t_plus_5(self):
        s = long_scene()
        s.drop(D1, (15, 30), (15, 35))                     # first bar after C - 30 is 15:35: no price at C - 30
        self.assertEqual(s.run(), [])

    def test_price_at_uses_open(self):
        s = long_scene()
        s.put(D1, 15, 30, 1005.0, 1006.0, 1004.75, 1004.75)     # close 1004.75, open 1005.0
        self.assertEqual(s.one()["entry"], 1005.5)

    def test_exit_price_at_c_window(self):
        s = long_scene()
        s.drop(D1, (16, 0), (16, 1))
        s.put(D1, 16, 4, 1007.0, 1007.5, 1006.0, 1007.0)
        t = s.one()
        self.assertEqual((t["exit_ts"], t["exit"]), (utc(D1, 16, 4), 1006.5))
        s.drop(D1, (16, 4), (16, 5))
        s.put(D1, 16, 5, 1007.0, 1007.5, 1006.0, 1007.0)   # 16:05 is outside [C, C + 5): no price at C
        self.assertEqual(s.run(), [])

    def test_last_price_before_is_last_close_in_window(self):
        s = long_scene()
        s.put(D1, 15, 26, 990.0, 990.0, 990.0, 990.0)      # an earlier bar of the window, below Y
        s.put(D1, 15, 29, 999.0, 1005.0, 999.0, 1004.5)    # the last: opens below Y, closes above
        t = s.one()
        self.assertEqual((t["side"], t["s1"]), (1, 1004.5))

    def test_last_price_before_window_starts_at_t_minus_5(self):
        s = long_scene()
        s.drop(D1, (15, 29), (15, 30))
        s.put(D1, 15, 25, 1004.0, 1004.25, 1004.0, 1004.25)    # C - 35: inside
        self.assertEqual(s.one()["s1"], 1004.25)
        s.drop(D1, (15, 25), (15, 26))
        s.put(D1, 15, 24, 1004.0, 1004.25, 1004.0, 1004.25)    # C - 36: outside, so no s1
        self.assertEqual(s.run(), [])

    def test_bar_at_c_minus_30_is_not_the_s1_bar(self):
        s = long_scene()
        s.drop(D1, (15, 25), (15, 30))                     # only the entry bar is left near C - 30
        self.assertEqual(s.run(), [])
        self.assertIsNone(s.one(signal="S2")["s1"])

    def test_s2_window(self):
        s = long_scene()
        s.drop(D1, (9, 55), (10, 0))
        s.put(D1, 10, 0, 1002.0, 1002.0, 1002.0, 1002.0)   # O + 30 itself: not before it
        s.put(D1, 9, 54, 1003.0, 1003.0, 1003.0, 1003.0)   # O + 24: too early
        self.assertEqual(s.run(signal="S2"), [])
        self.assertIsNone(s.one(signal="S1")["s2"])
        s.put(D1, 9, 55, 1001.0, 1001.5, 1001.0, 1001.25)  # O + 25: inside
        self.assertEqual(s.one(signal="S2")["s2"], 1001.25)


# ------------------------------------------------------------------------------------------------ rule 2
class TestYesterday(unittest.TestCase):
    def test_y_is_the_open_at_c(self):
        self.assertEqual(long_scene().one()["y"], 1000.0)   # the 16:00 bar opens 1000.0, closes 1000.25

    def test_y_window(self):
        s = long_scene()
        s.drop(D0, (16, 0), (16, 1))
        s.put(D0, 16, 4, 1000.0, 1000.5, 999.5, 1000.25)
        self.assertEqual(s.one()["y"], 1000.0)
        s.drop(D0, (16, 4), (16, 5))
        s.put(D0, 16, 5, 1000.0)                          # outside [C, C + 5)
        s.put(D0, 15, 59, 1000.0)                         # a last price before C is not the price at C
        self.assertEqual(s.run(), [])

    def test_weekend_reads_friday_and_weekend_is_never_traded(self):
        fri, sat, sun, mon = date(2024, 1, 5), date(2024, 1, 6), date(2024, 1, 7), date(2024, 1, 8)
        s = Scene()
        s.daily = daily_bars(fri, [40.0] * 20)
        y_bar(s, fri, 1000.0)
        s.put(sat, 12, 0, 1010.0)
        long_day(s, sun)                                  # a full day's bars on Sunday, its 16:00 bar opening 1007
        s.span(sun, (18, 0), (18, 5), 1006.0, 1006.0, 1006.0, 1006.0)
        long_day(s, mon)
        t = s.one()
        self.assertEqual((t["date"], t["y"], t["side"]), ("2024-01-08", 1000.0, 1))
        self.assertEqual([d for d, _t, _w in s.days()], ["2024-01-05", "2024-01-08"])

    def test_weekday_without_bars_is_not_a_trading_day(self):
        s = Scene()
        y_bar(s, D0)                                      # Tuesday; Wednesday D1 has no bar at all
        long_day(s, D2)
        t = s.one()
        self.assertEqual((t["date"], t["y"]), ("2024-01-11", 1000.0))

    def test_day_before_with_no_bars_in_o_to_c(self):
        s = Scene()
        y_bar(s, D0)
        s.span(D1, (18, 0), (18, 10), 1003.0, 1003.0, 1003.0, 1003.0)   # Wednesday: evening bars only
        long_day(s, D2)
        self.assertEqual(s.run(), [])                     # Thursday's day before is Wednesday: no price at C
        self.assertEqual([d for d, _t, _w in s.days()], ["2024-01-09", "2024-01-10", "2024-01-11"])

    def test_first_trading_day_has_no_day_before(self):
        s = Scene()
        long_day(s, D1)
        self.assertEqual(s.run(), [])

    def test_y_bar_must_exist_even_if_day_before_traded_late(self):
        s = Scene()
        s.put(D0, 15, 0, 1000.0)                          # Tuesday's last bar is before C
        long_day(s, D1)
        self.assertEqual(s.run(), [])


class TestRoll(unittest.TestCase):
    def test_same_contract_trades(self):
        self.assertEqual(long_scene().one(), LONG)

    def test_roll_between_y_and_today(self):
        s = Scene(iid=8)
        y_bar(s, D0, iid=7)
        long_day(s, D1)
        self.assertEqual(s.run(), [])

    def test_roll_in_todays_evening(self):
        s = long_scene()
        s.put(D1, 19, 30, 1007.0, iid=8)                  # 00:30 UTC on Thursday, but New York's Wednesday
        self.assertEqual(s.run(), [])

    def test_late_bar_of_today_on_new_york_clock(self):
        s = long_scene()
        s.put(D1, 23, 59, 1007.0, iid=8)                  # 04:59 UTC Thursday: still Wednesday in New York
        self.assertEqual(s.run(), [])
        s = long_scene()
        s.put(D2, 0, 0, 1007.0, iid=8)                    # Thursday's first minute: not today's
        self.assertEqual(s.one(), LONG)

    def test_early_bar_of_today_other_contract(self):
        s = long_scene()
        s.put(D1, 3, 0, 1001.0, iid=8)
        self.assertEqual(s.run(), [])

    def test_only_y_bar_of_the_day_before_counts(self):
        s = long_scene()
        s.span(D0, (9, 30), (9, 35), 990.0, 990.0, 990.0, 990.0, iid=6)    # earlier bars, an older contract
        s.put(D0, 18, 0, 1000.0, iid=6)
        self.assertEqual(s.one(), LONG)


# ------------------------------------------------------------------------------------------------ rule 3
def set_s1(s, x):
    s.put(D1, 15, 29, x, x, x, x)


def set_s2(s, x):
    s.drop(D1, (9, 55), (10, 0))
    if x is not None:
        s.put(D1, 9, 59, x, x, x, x)


class TestSignals(unittest.TestCase):
    def test_s1_long_and_short(self):
        self.assertEqual(long_scene().one()["side"], 1)
        self.assertEqual(short_scene().one()["side"], -1)

    def test_s1_equal_is_no_trade(self):
        s = long_scene()
        set_s1(s, 1000.0)
        self.assertEqual(s.run(), [])

    def test_s1_within_eps_is_equal(self):
        s = long_scene()
        set_s1(s, 1000.0 + TE)
        self.assertEqual(s.run(), [])
        set_s1(s, 1000.0 - TE)
        self.assertEqual(s.run(), [])

    def test_s1_beyond_eps_trades(self):
        s = long_scene()
        set_s1(s, 1000.0 + TO)
        self.assertEqual(s.one()["side"], 1)
        set_s1(s, 1000.0 - TO)
        self.assertEqual(s.one()["side"], -1)

    def test_s2_reads_its_own_price(self):
        s = long_scene()
        set_s1(s, 995.0)                                  # S1 would be short
        t = s.one(signal="S2")
        self.assertEqual((t["side"], t["s1"], t["s2"]), (1, 995.0, 1002.0))
        set_s2(s, 998.0)
        set_s1(s, 1004.5)
        self.assertEqual(s.one(signal="S2")["side"], -1)

    def test_s2_equal_and_within_eps_no_trade(self):
        s = long_scene()
        set_s2(s, 1000.0)
        self.assertEqual(s.run(signal="S2"), [])
        set_s2(s, 1000.0 - TE)
        self.assertEqual(s.run(signal="S2"), [])

    def test_missing_s2_is_none_and_no_s2_trade(self):
        s = long_scene()
        set_s2(s, None)
        self.assertEqual(s.run(signal="S2"), [])
        self.assertEqual(s.one(signal="S1"), with_(LONG, s2=None))

    def test_s3_agree(self):
        s = long_scene()
        self.assertEqual(s.one(signal="S3"), with_(LONG, signal="S3"))
        set_s1(s, 999.0)
        set_s2(s, 998.0)
        self.assertEqual(s.one(signal="S3")["side"], -1)

    def test_s3_differ_equal_or_missing(self):
        for s1, s2 in ((1004.5, 998.0), (995.0, 1002.0), (1004.5, 1000.0), (1000.0, 1002.0), (1004.5, None),
                       (1004.5, 1000.0 + TE)):
            s = long_scene()
            set_s1(s, s1)
            set_s2(s, s2)
            self.assertEqual(s.run(signal="S3"), [], (s1, s2))


# ------------------------------------------------------------------------------------------------ rules 4 and 5
class TestNoTrade(unittest.TestCase):
    def test_no_price_at_c_minus_30(self):
        s = long_scene()
        s.drop(D1, (15, 30), (15, 35))
        self.assertEqual(s.run(), [])
        self.assertEqual(s.run(signal="S2"), [])

    def test_no_price_at_c_even_when_stopped_before(self):
        s = long_scene()
        s.put(D1, 15, 40, 1005.0, 1005.5, 1003.25, 1004.0)    # would stop out
        s.drop(D1, (16, 0), (16, 5))
        self.assertEqual(s.run(), [])

    def test_fewer_than_14_daily_bars(self):
        s = long_scene()
        s.daily = daily_bars(D0, [40.0] * 13)
        self.assertEqual(s.run(), [])
        s.daily = daily_bars(D0, [40.0] * 14)
        self.assertEqual(s.one(), LONG)

    def test_daily_bar_on_the_day_itself_not_read(self):
        s = long_scene()
        s.daily = daily_bars(D1, [40.0] * 13 + [400.0])      # the 14th is stamped on D1's UTC date
        self.assertEqual(s.run(), [])
        s.daily = daily_bars(D1, [40.0] * 20 + [400.0])
        self.assertEqual(s.one()["atr"], 40.0)

    def test_atr_is_the_last_14(self):
        s = long_scene()
        s.daily = daily_bars(D0, [400.0] * 6 + [float(r) for r in range(34, 48)])   # 34..47: mean 40.5
        t = s.one()
        self.assertEqual((t["atr"], t["dist"]), (40.5, 1.0))

    def test_atr_days_from_settings(self):
        s = long_scene()
        s.daily = daily_bars(D0, [40.0] * 17 + [48.0] * 3)
        self.assertEqual(s.one(atr_days=3)["atr"], 48.0)
        self.assertEqual(s.one(atr_days=14)["atr"], 40.0 + 3 * 8.0 / 14)


class TestEntryAndStopDistance(unittest.TestCase):
    def test_entry_clamped_to_high(self):
        s = long_scene()
        s.put(D1, 15, 30, 1005.0, 1005.25, 1004.75, 1005.0)   # open + slip = 1005.5 > high
        t = s.one()
        self.assertEqual((t["entry"], t["stop"], t["points"], t["worst"]), (1005.25, 1004.25, 1.25, -0.5))

    def test_entry_clamped_to_low(self):
        s = short_scene()
        s.put(D1, 15, 30, 995.0, 995.25, 994.75, 995.0)       # open - slip = 994.5 < low
        t = s.one()
        self.assertEqual((t["entry"], t["stop"], t["points"], t["worst"]), (994.75, 995.75, 1.25, -0.5))

    def test_dist_rounded_down_to_tick(self):
        s = long_scene()
        s.daily = daily_bars(D0, [47.0] * 20)                 # k A = 1.175 = 4.7 ticks -> 4 ticks
        t = s.one()
        self.assertEqual((t["atr"], t["dist"], t["stop"]), (47.0, 1.0, 1004.5))

    def test_dist_larger_k(self):
        t = long_scene().one(k=0.2)                           # 8.0 points = 32 ticks
        self.assertEqual((t["dist"], t["stop"]), (8.0, 997.5))

    def test_dist_one_tick_floor(self):
        t = long_scene().one(k=0.001)                         # k A = 0.04 -> 0 ticks -> one tick
        self.assertEqual((t["dist"], t["stop"]), (0.25, 1005.25))

    def test_floor_tick_allowance_rty(self):
        # RTY, tick 0.1: k A = 0.05 x 86 = 4.3 in floats is 42.99999999999999 ticks; floor_tick's 10^-6 makes it 43
        s = rty_long()
        s.daily = daily_bars(D0, [86.0] * 20, base=1500.0)
        t = s.one(k=0.05)
        self.assertAlmostEqual(t["dist"], 4.3, delta=1e-9)

    def test_tick_helpers(self):
        self.assertEqual(rc.floor_tick(1.175, 0.25), 1.0)
        self.assertEqual(rc.ceil_tick(1.175, 0.25), 1.25)
        self.assertEqual(rc.floor_tick(1.25 - 1e-9, 0.25), 1.25)
        self.assertEqual(rc.ceil_tick(1.25 + 1e-9, 0.25), 1.25)


# ------------------------------------------------------------------------------------------------ the stop
def stop_bar(s, o, h, l, c=None, at=(15, 40)):
    s.put(D1, at[0], at[1], o, h, l, o if c is None else c)


class TestStopLong(unittest.TestCase):
    def check(self, s, fills, exit_ts, gap, worst):
        for fill, ex in fills.items():
            t = s.one(fill=fill)
            self.assertEqual((t["reason"], t["exit_ts"], t["exit"], t["gap"], t["points"], t["worst"]),
                             ("stop", exit_ts, ex, gap, ex - 1005.5, worst), fill)

    def test_touch_three_fills(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1003.25)     # touch: reference = stop 1004.5
        # midpoint floor_tick((1004.5 + 1003.25) / 2 = 1003.875) = 1003.75; kind max(1004.0, 1003.25); harsh low
        self.check(s, {"midpoint": 1003.75, "kind": 1004.0, "harsh-stops": 1003.25}, utc(D1, 15, 40), False,
                   1003.25 - 1005.5)

    def test_kind_held_at_low(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1004.25)     # kind max(1004.0, 1004.25) = 1004.25
        self.check(s, {"midpoint": 1004.25, "kind": 1004.25, "harsh-stops": 1004.25}, utc(D1, 15, 40), False,
                   -1.25)

    def test_gap_three_fills(self):
        s = long_scene()
        stop_bar(s, 1003.5, 1003.75, 1002.25)    # opens below the stop: reference = open 1003.5
        # midpoint floor_tick(1002.875) = 1002.75; kind max(1003.0, 1002.25) = 1003.0; harsh 1002.25
        self.check(s, {"midpoint": 1002.75, "kind": 1003.0, "harsh-stops": 1002.25}, utc(D1, 15, 40), True,
                   1002.25 - 1005.5)

    def test_open_exactly_at_stop_is_a_gap(self):
        s = long_scene()
        stop_bar(s, 1004.5, 1004.75, 1003.25)
        self.check(s, {"midpoint": 1003.75, "kind": 1004.0, "harsh-stops": 1003.25}, utc(D1, 15, 40), True,
                   1003.25 - 1005.5)

    def test_open_within_eps_of_stop_is_a_gap(self):
        s = long_scene()
        stop_bar(s, 1004.5 + TE, 1004.75, 1003.25)
        self.assertTrue(s.one()["gap"])
        stop_bar(s, 1004.5 + TO, 1004.75, 1003.25)
        self.assertFalse(s.one()["gap"])

    def test_low_exactly_at_stop_fills(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1004.5)
        self.check(s, {"midpoint": 1004.5, "kind": 1004.5, "harsh-stops": 1004.5}, utc(D1, 15, 40), False, -1.0)

    def test_low_within_eps_fills_beyond_does_not(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1004.5 + TE)
        self.assertEqual(s.one()["reason"], "stop")
        stop_bar(s, 1005.0, 1005.5, 1004.5 + TO)
        self.assertEqual(s.one(), with_(LONG, worst=(1004.5 + TO) - 1005.5))   # the near miss's low

    def test_first_fill_ends_the_trade(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1004.25)                  # midpoint floor_tick(1004.375) = 1004.25
        stop_bar(s, 1004.0, 1004.0, 1000.0, at=(15, 41))
        t = s.one()
        self.assertEqual((t["exit_ts"], t["exit"], t["worst"]), (utc(D1, 15, 40), 1004.25, -1.25))

    def test_last_watched_minute(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1003.25, at=(15, 59))
        self.assertEqual(s.one()["exit_ts"], utc(D1, 15, 59))

    def test_stop_on_the_entry_bar(self):
        s = long_scene()
        s.put(D1, 15, 30, 1005.0, 1006.0, 1004.0, 1005.5)     # entry 1005.5, stop 1004.5, low 1004.0
        t = s.one()
        # midpoint floor_tick((1004.5 + 1004.0) / 2) = 1004.25
        self.assertEqual((t["reason"], t["exit_ts"], t["exit"], t["gap"], t["worst"]),
                         ("stop", utc(D1, 15, 30), 1004.25, False, -1.5))

    def test_gap_on_the_entry_bar(self):
        s = long_scene()
        s.put(D1, 15, 30, 1005.0, 1006.0, 1003.75, 1005.5)
        # k 0.001: dist one tick, entry 1005.5, stop 1005.25: the entry bar opened at 1005.0, beyond the stop
        for fill, ex in (("midpoint", 1004.25), ("kind", 1004.5), ("harsh-stops", 1003.75)):
            t = s.one(k=0.001, fill=fill)
            self.assertEqual((t["reason"], t["exit_ts"], t["exit"], t["gap"], t["dist"], t["worst"]),
                             ("stop", utc(D1, 15, 30), ex, True, 0.25, -1.75), fill)

    def test_exit_bar_not_checked(self):
        s = long_scene()
        s.put(D1, 16, 0, 1006.0, 1006.5, 1003.0, 1004.0)      # its low is below the stop 1004.5
        s.put(D1, 16, 1, 1000.0, 1000.0, 999.0, 999.0)        # after the exit bar: never read
        t = s.one()
        self.assertEqual((t["reason"], t["exit"], t["points"], t["worst"]), ("close", 1005.5, 0.0, -0.75))

    def test_midpoint_floor_allowance_rty(self):
        # RTY gap: reference = open 1500.2, low 1500.0: (1500.2 + 1500.0) / 2 / 0.1 = 15000.999999999998 in
        # floats; floor_tick's 10^-6 gives 15001 ticks = 1500.1, not 1500.0
        s = rty_long()
        s.put(D1, 15, 40, 1500.2, 1500.5, 1500.0, 1500.2)
        t = s.one()
        self.assertEqual((t["reason"], t["gap"]), ("stop", True))
        self.assertAlmostEqual(t["exit"], 1500.1, delta=1e-9)


class TestStopShort(unittest.TestCase):
    def check(self, s, fills, exit_ts, gap, worst):
        for fill, ex in fills.items():
            t = s.one(fill=fill)
            self.assertEqual((t["reason"], t["exit_ts"], t["exit"], t["gap"], t["points"], t["worst"]),
                             ("stop", exit_ts, ex, gap, 994.5 - ex, worst), fill)

    def test_touch_three_fills(self):
        s = short_scene()
        stop_bar(s, 995.0, 996.75, 994.75)       # touch: reference = stop 995.5
        # midpoint ceil_tick((995.5 + 996.75) / 2 = 996.125) = 996.25; kind min(996.0, 996.75); harsh the high
        self.check(s, {"midpoint": 996.25, "kind": 996.0, "harsh-stops": 996.75}, utc(D1, 15, 40), False,
                   994.5 - 996.75)

    def test_kind_held_at_high(self):
        s = short_scene()
        stop_bar(s, 995.0, 995.75, 994.75)       # kind min(996.0, 995.75) = 995.75
        self.check(s, {"midpoint": 995.75, "kind": 995.75, "harsh-stops": 995.75}, utc(D1, 15, 40), False,
                   -1.25)

    def test_gap_three_fills(self):
        s = short_scene()
        stop_bar(s, 996.0, 997.25, 995.75)       # opens above the stop: reference = open 996.0
        # midpoint ceil_tick(996.625) = 996.75; kind min(996.5, 997.25) = 996.5; harsh 997.25
        self.check(s, {"midpoint": 996.75, "kind": 996.5, "harsh-stops": 997.25}, utc(D1, 15, 40), True,
                   994.5 - 997.25)

    def test_open_exactly_at_stop_is_a_gap(self):
        s = short_scene()
        stop_bar(s, 995.5, 996.75, 995.25)
        self.check(s, {"midpoint": 996.25, "kind": 996.0, "harsh-stops": 996.75}, utc(D1, 15, 40), True,
                   994.5 - 996.75)

    def test_mirrored_eps(self):
        s = short_scene()
        stop_bar(s, 995.0, 995.5 - TE, 994.75)    # a high a tenth of eps short of the stop still fills (C11)
        t = s.one()
        self.assertEqual((t["reason"], t["gap"]), ("stop", False))
        stop_bar(s, 995.5 - TE, 995.75, 995.0)    # an open a tenth of eps short of the stop is a gap
        self.assertTrue(s.one()["gap"])
        stop_bar(s, 995.0, 995.5 - TO, 994.75)    # ten eps short: no fill
        self.assertEqual(s.one(), with_(SHORT, worst=994.5 - (995.5 - TO)))   # the near miss's high

    def test_stop_on_the_entry_bar(self):
        s = short_scene()
        s.put(D1, 15, 30, 995.0, 996.0, 994.0, 994.5)         # entry 994.5, stop 995.5, high 996.0
        t = s.one()
        # midpoint ceil_tick((995.5 + 996.0) / 2 = 995.75) = 995.75
        self.assertEqual((t["reason"], t["exit_ts"], t["exit"], t["gap"], t["worst"]),
                         ("stop", utc(D1, 15, 30), 995.75, False, -1.5))

    def test_exit_bar_not_checked(self):
        s = short_scene()
        s.put(D1, 16, 0, 994.0, 997.0, 993.5, 996.0)          # its high is above the stop 995.5
        t = s.one()
        self.assertEqual((t["reason"], t["exit"], t["points"], t["worst"]), ("close", 994.5, 0.0, -0.75))

    def test_midpoint_ceil_allowance_rty(self):
        # RTY gap: reference = open 1500.2, high 1500.4: (1500.2 + 1500.4) / 2 / 0.1 = 15003.000000000002 in
        # floats; ceil_tick's 10^-6 gives 15003 ticks = 1500.3, not 1500.4
        s = rty_short()
        s.put(D1, 15, 40, 1500.2, 1500.4, 1500.0, 1500.2)
        t = s.one()
        self.assertEqual((t["reason"], t["gap"]), ("stop", True))
        self.assertAlmostEqual(t["exit"], 1500.3, delta=1e-9)


def rty_long():
    """RTY (tick 0.1, slip 0.2), Y 1500.0, s1 1505.0, entry bar opens 1505.0 -> entry 1505.2, dist 1.0 (A 40),
    stop 1504.2; watched lows 1505.0; exit bar opens 1507.0."""
    s = Scene("RTY")
    s.daily = daily_bars(D0, [40.0] * 20, base=1500.0)
    s.put(D0, 16, 0, 1500.0, 1500.5, 1499.5, 1500.0)
    s.put(D1, 15, 29, 1505.0, 1505.0, 1505.0, 1505.0)
    s.put(D1, 15, 30, 1505.0, 1506.0, 1504.9, 1505.5)
    s.span(D1, (15, 31), (16, 0), 1505.5, 1506.0, 1505.0, 1505.5)
    s.put(D1, 16, 0, 1507.0, 1507.5, 1506.0, 1507.0)
    return s


def rty_short():
    """RTY short: Y 1500.0, s1 1495.0, entry bar opens 1495.0 -> entry 1494.8, stop 1495.8; watched highs 1495.0."""
    s = Scene("RTY")
    s.daily = daily_bars(D0, [40.0] * 20, base=1500.0)
    s.put(D0, 16, 0, 1500.0, 1500.5, 1499.5, 1500.0)
    s.put(D1, 15, 29, 1495.0, 1495.0, 1495.0, 1495.0)
    s.put(D1, 15, 30, 1495.0, 1495.1, 1494.0, 1494.5)
    s.span(D1, (15, 31), (16, 0), 1494.5, 1495.0, 1494.0, 1494.5)
    s.put(D1, 16, 0, 1493.0, 1494.0, 1492.5, 1493.0)
    return s


# ------------------------------------------------------------------------------------------------ rule 6, worst
class TestExitAndWorst(unittest.TestCase):
    def test_exit_clamped_to_low(self):
        s = long_scene()
        s.put(D1, 16, 0, 1007.0, 1007.5, 1006.75, 1007.0)     # open - slip = 1006.5 < low
        t = s.one()
        self.assertEqual((t["exit"], t["points"]), (1006.75, 1.25))

    def test_exit_clamped_to_high(self):
        s = short_scene()
        s.put(D1, 16, 0, 993.0, 993.25, 992.5, 993.0)         # open + slip = 993.5 > high
        t = s.one()
        self.assertEqual((t["exit"], t["points"]), (993.25, 1.25))

    def test_worst_counts_the_entry_bar_whole(self):
        self.assertEqual(long_scene().one()["worst"], -0.75)  # the entry bar's low, not the watched -0.5
        self.assertEqual(short_scene().one()["worst"], -0.75)

    def test_worst_close_exit_counts_the_exit_fill(self):
        s = long_scene()
        s.put(D1, 15, 30, 1005.0, 1006.0, 1005.0, 1005.5)     # entry bar low 1005.0: -0.5
        s.put(D1, 16, 0, 1005.25, 1005.5, 1004.75, 1005.0)    # exit = max(1004.75, 1004.75): -0.75
        t = s.one()
        self.assertEqual((t["exit"], t["points"], t["worst"]), (1004.75, -0.75, -0.75))

    def test_worst_stop_exit_counts_the_stop_minute_whole(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1003.25)
        t = s.one()
        self.assertEqual((t["exit"], t["worst"]), (1003.75, -2.25))   # the fill is -1.75; the low -2.25

    def test_worst_short_uses_highs(self):
        s = short_scene()
        s.put(D1, 15, 45, 994.5, 995.25, 993.0, 994.5)        # a high of 995.25 later: -0.75; its low plays no part
        s.put(D1, 15, 30, 995.0, 995.0, 994.0, 994.5)         # entry bar high 995.0: -0.5
        self.assertEqual(s.one()["worst"], -0.75)


# ------------------------------------------------------------------------------------------------ the markets
TABLE = {"NQ": ((9, 30), (16, 0)), "ES": ((9, 30), (16, 0)), "RTY": ((9, 30), (16, 0)),
         "ZN": ((8, 20), (15, 0)), "ZB": ((8, 20), (15, 0)), "6E": ((8, 20), (15, 0)), "6J": ((8, 20), (15, 0)),
         "6B": ((8, 20), (15, 0)), "6A": ((8, 20), (15, 0)), "CL": ((9, 0), (14, 30)), "GC": ((8, 20), (13, 30))}


def hm(t, dm):
    m = t[0] * 60 + t[1] + dm
    return m // 60, m % 60


def market_scene(market, d=D1, prev=D0, off=EST, prev_off=EST):
    """A long on the market's own hours, prices in its ticks: Y 1000, s2 1003 (O + 29), s1 1004 (C - 31), entry bar
    opens 1005 at C - 30, exit bar opens 1008 at C. k 0.2 of A = 40 ticks -> dist 8 ticks."""
    s = Scene(market)
    tick = s.spec["tick"]

    def px(n):
        return n * tick
    (O, C) = TABLE[market]
    s.daily = daily_bars(prev, [40 * tick] * 20, base=px(1000))
    s.put(prev, C[0], C[1], px(1000), px(1001), px(999), px(1000), off=prev_off)
    s.put(d, *hm(O, 29), px(1003), px(1003), px(1003), px(1003), off=off)
    s.put(d, *hm(C, -31), px(1004), px(1004), px(1004), px(1004), off=off)
    s.put(d, *hm(C, -30), px(1005), px(1010), px(1004), px(1005), off=off)
    s.span(d, hm(C, -29), C, px(1005), px(1006), px(1004), px(1005), off=off)
    s.put(d, C[0], C[1], px(1008), px(1009), px(1005), px(1008), off=off)
    return s, px


class TestMarkets(unittest.TestCase):
    def test_table_of_hours(self):
        self.assertEqual(rc.HOURS, TABLE)

    def test_every_market_on_its_own_hours(self):
        for market, (O, C) in TABLE.items():
            s, px = market_scene(market)
            slip = s.spec["slip_ticks"] * s.spec["tick"]
            for signal in ("S1", "S2", "S3"):
                t = s.one(signal=signal, k=0.2)
                self.assertEqual((t["market"], t["side"], t["entry_ts"], t["exit_ts"], t["reason"]),
                                 (market, 1, utc(D1, *hm(C, -30)), utc(D1, *C), "close"), (market, signal))
                for f, want in (("y", px(1000)), ("s1", px(1004)), ("s2", px(1003)), ("dist", px(8)),
                                ("entry", px(1005) + slip), ("exit", px(1008) - slip)):
                    self.assertAlmostEqual(t[f], want, delta=1e-12, msg=(market, f))

    def test_summer_time(self):
        jul9, jul10 = date(2024, 7, 9), date(2024, 7, 10)
        s, _px = market_scene("NQ", d=jul10, prev=jul9, off=EDT, prev_off=EDT)
        t = s.one(k=0.2)
        self.assertEqual((t["date"], t["entry_ts"]), ("2024-07-10", utc(jul10, 15, 30, EDT)))
        s, _px = market_scene("CL", d=jul10, prev=jul9, off=EDT, prev_off=EDT)
        self.assertEqual(s.one(k=0.2)["exit_ts"], utc(jul10, 14, 30, EDT))

    def test_clock_change_between_days(self):
        fri, mon = date(2024, 3, 8), date(2024, 3, 11)       # Friday on EST, Monday on EDT
        s, px = market_scene("ES", d=mon, prev=fri, off=EDT, prev_off=EST)
        t = s.one(k=0.2)
        self.assertEqual((t["date"], t["y"], t["entry_ts"]), ("2024-03-11", px(1000), utc(mon, 15, 30, EDT)))

    def test_clock_helpers(self):
        self.assertEqual(rc.ny_ns(D1, 9, 30), utc(D1, 9, 30, EST))
        self.assertEqual(rc.ny_ns(date(2024, 7, 10), 16, 0), utc(date(2024, 7, 10), 16, 0, EDT))
        self.assertEqual(rc.ny_date(utc(D1, 23, 59, EST)), D1)
        self.assertEqual(rc.ny_date(utc(D2, 0, 0, EST)), D2)


# ------------------------------------------------------------------------------------------------ first..last
def three_days():
    s = Scene()
    y_bar(s, D0)
    for d in (D1, D2, D3):
        long_day(s, d)
    return s


class TestRange(unittest.TestCase):
    def test_inclusive(self):
        s = three_days()
        self.assertEqual([t["date"] for t in s.run()], ["2024-01-10", "2024-01-11", "2024-01-12"])
        self.assertEqual([t["date"] for t in s.run(first="2024-01-11", last="2024-01-11")], ["2024-01-11"])
        self.assertEqual([t["date"] for t in s.run(first="2024-01-10", last="2024-01-11")],
                         ["2024-01-10", "2024-01-11"])
        self.assertEqual([t["date"] for t in s.run(first="2024-01-11")], ["2024-01-11", "2024-01-12"])

    def test_day_before_first_is_still_read(self):
        s = three_days()
        t = s.one(first="2024-01-11", last="2024-01-11")
        self.assertEqual(t["y"], 1007.0)                     # Wednesday's 16:00 bar opens 1007.0


# ------------------------------------------------------------------------------------------------ check_market
def check(s, got, signal="S1", fill="midpoint", first=None, last=None):
    return rc.check_market(got, s.minutes(), s.daily, [], s.spec, settings(signal), fill, s.market, first, last)


CHANGED = {"market": "ES", "signal": "S2", "side": -1, "entry_ts": LONG["entry_ts"] + 60 * NS,
           "exit_ts": LONG["exit_ts"] + 60 * NS, "reason": "stop", "gap": True}


class TestCheckMarket(unittest.TestCase):
    def test_clean(self):
        s = long_scene()
        self.assertEqual(check(s, {"trades": [dict(LONG)]}), [])
        self.assertEqual(check(s, {"trades": s.run()}), [])

    def test_every_field_compared(self):
        s = long_scene()
        for f in rc.FIELDS:
            if f == "date":
                continue
            bad = CHANGED[f] if f in CHANGED else LONG[f] + 2e-9
            b = check(s, {"trades": [with_(LONG, **{f: bad})]})
            self.assertEqual(len(b), 1, (f, b))
            self.assertIn("2024-01-10", b[0])
            self.assertIn(f"{f} is", b[0])

    def test_float_tolerance(self):
        s = long_scene()
        for f in rc.PRICE_FIELDS:
            self.assertEqual(check(s, {"trades": [with_(LONG, **{f: LONG[f] + 5e-10})]}), [], f)
            self.assertEqual(len(check(s, {"trades": [with_(LONG, **{f: LONG[f] - 2e-9})]})), 1, f)

    def test_none_matches_only_none(self):
        s = long_scene()
        set_s2(s, None)
        good = with_(LONG, s2=None)
        self.assertEqual(check(s, {"trades": [good]}), [])
        self.assertEqual(len(check(s, {"trades": [with_(good, s2=0.0)]})), 1)
        self.assertEqual(len(check(long_scene(), {"trades": [with_(LONG, s2=None)]})), 1)

    def test_bool_and_int_kept_apart(self):
        s = long_scene()
        self.assertEqual(len(check(s, {"trades": [with_(LONG, gap=0)]})), 1)
        self.assertEqual(len(check(s, {"trades": [with_(LONG, side=True)]})), 1)
        self.assertEqual(len(check(s, {"trades": [with_(LONG, y=True)]})), 1)
        self.assertEqual(len(check(s, {"trades": [with_(LONG, y="1000.0")]})), 1)

    def test_missing_trade(self):
        b = check(long_scene(), {"trades": []})
        self.assertEqual(len(b), 1)
        self.assertIn("2024-01-10", b[0])
        self.assertIn("missing", b[0])

    def test_extra_trade_with_the_rules_reason(self):
        s = long_scene()
        set_s1(s, 1000.0)
        b = check(s, {"trades": [dict(LONG)]})
        self.assertEqual(len(b), 1)
        self.assertIn("2024-01-10", b[0])
        self.assertIn("extra", b[0])
        self.assertIn("no side", b[0])

    def test_extra_trade_outside_range(self):
        s = three_days()
        got = {"trades": s.run()}
        b = check(s, got, first="2024-01-11", last="2024-01-11")
        self.assertEqual(len(b), 2)
        self.assertTrue(all("extra" in x for x in b))

    def test_wrong_date_is_missing_and_extra(self):
        b = check(long_scene(), {"trades": [with_(LONG, date="2024-01-11")]})
        self.assertEqual(len(b), 2)

    def test_listed_twice(self):
        b = check(long_scene(), {"trades": [dict(LONG), dict(LONG)]})
        self.assertEqual(len(b), 1)
        self.assertIn("twice", b[0])

    def test_field_missing(self):
        t = dict(LONG)
        del t["worst"]
        b = check(long_scene(), {"trades": [t]})
        self.assertEqual(b, ["NQ 2024-01-10: field worst missing"])

    def test_unlisted_fields_named_once(self):
        s = three_days()
        got = {"trades": [with_(t, qty=1) for t in s.run()]}
        b = check(s, got)
        self.assertEqual(len(b), 1)
        self.assertIn("qty (3 trades)", b[0])

    def test_date_order(self):
        s = three_days()
        b = check(s, {"trades": list(reversed(s.run()))})
        self.assertEqual(b, ["NQ: the engine's trades are not in date order"])

    def test_bad_inputs(self):
        s = long_scene()
        self.assertEqual(len(check(s, [dict(LONG)])), 1)
        self.assertEqual(len(check(s, {"trades": ["x"]})), 2)          # unreadable, and the rule's trade missing
        self.assertEqual(len(check(s, {"trades": [dict(LONG)]}, fill="mid")), 1)

    def test_fill_is_replayed(self):
        s = long_scene()
        stop_bar(s, 1005.0, 1005.5, 1003.25)
        got = {"trades": s.run(fill="kind")}
        self.assertEqual(check(s, got, fill="kind"), [])
        b = check(s, got, fill="midpoint")
        self.assertEqual(len(b), 2)                                     # exit and points
        self.assertTrue(any("exit is" in x for x in b) and any("points is" in x for x in b))


# ------------------------------------------------------------------------------------------------ check_account
def pc_trade(market, d, side, entry, exit_, dist, points, worst, entry_ts, exit_ts, reason="close"):
    return {"market": market, "date": d.isoformat(), "signal": "S1", "side": side, "y": 1.0, "s1": 2.0, "s2": None,
            "atr": 10.0, "dist": dist, "entry_ts": entry_ts, "entry": entry, "stop": entry - side * dist,
            "exit_ts": exit_ts, "exit": exit_, "reason": reason, "gap": False, "points": points, "worst": worst}


NQ1 = pc_trade("NQ", D1, 1, 1005.5, 1006.5, 1.0, 1.0, -0.75, utc(D1, 15, 30), utc(D1, 16, 0))
ZN1 = pc_trade("ZN", D1, 1, 110.0, 110.03125, 0.015625, 0.03125, -0.015625, utc(D1, 14, 30), utc(D1, 15, 0))
ZB1 = pc_trade("ZB", D1, 1, 120.0, 120.5, 1.0, 0.5, -0.25, utc(D1, 14, 30), utc(D1, 15, 0))
NQ2 = pc_trade("NQ", D2, -1, 994.5, 996.25, 1.0, -1.75, -2.25, utc(D2, 15, 30), utc(D2, 15, 40), "stop")
PER_CONTRACT = {"NQ": {"trades": [NQ1, NQ2]}, "ZN": {"trades": [ZN1]}, "ZB": {"trades": [ZB1]}}
SPECS3 = {m: specs.SPECS[m] for m in PER_CONTRACT}


def account_result():
    """By hand, start 150,000 at 0.25%: risk 375.
    2024-01-10. NQ: loss a contract (1.0 + 0.5) x 2 + 1.90 = 4.90 -> 76 contracts (372.40); net 1.0 x 2 x 76 -
    1.90 x 76 = 7.60. ZN: (1/64 + 1/64) x 1000 + 5 = 36.25 -> 10, capped at 9 (326.25); net 0.03125 x 1000 x 9 - 45 =
    236.25. ZB: (1 + 2/32) x 1000 + 5 = 1067.50 > 375: skipped. End 150,243.85; low 150,000 - (0.75 x 2 x 76 +
    144.40) - (15.625 x 9 + 45) = 149,555.975.
    2024-01-11. risk 375.609625 -> NQ 76 contracts; net -1.75 x 2 x 76 - 144.40 = -410.40. End 149,833.45; low
    150,243.85 - (2.25 x 2 x 76 + 144.40) = 149,757.45."""
    def rec(t, qty, planned, net, bal):
        return with_(t, qty=qty, planned_cost=planned, net=net, balance_start=bal)
    return {"start": 150000.0,
            "trades": [rec(NQ1, 76, 372.4, 7.6, 150000.0), rec(ZN1, 9, 326.25, 236.25, 150000.0),
                       rec(NQ2, 76, 372.4, -410.4, 150243.85)],
            "skipped": [{"market": "ZB", "date": "2024-01-10", "entry_ts": utc(D1, 14, 30),
                         "reason": "under one contract"}],
            "days": [{"date": "2024-01-10", "start": 150000.0, "end": 150243.85, "low": 149555.98},
                     {"date": "2024-01-11", "start": 150243.85, "end": 149833.45, "low": 149757.45}]}


class TestCheckAccount(unittest.TestCase):
    def acc(self, result, risk=0.25):
        return rc.check_account(result, PER_CONTRACT, SPECS3, risk, 150000.0)

    def test_clean(self):
        self.assertEqual(self.acc(account_result()), [])

    def test_other_size_breaks(self):
        b = self.acc(account_result(), risk=0.5)                 # 750: NQ 153 -> capped at 90
        self.assertTrue(any("qty is 76, rule says 90" in x for x in b), b)

    def test_wrong_qty_net_skip_day(self):
        r = account_result()
        r["trades"][0]["qty"] = 75
        self.assertTrue(self.acc(r))
        r = account_result()
        r["trades"][1]["net"] = 236.26
        self.assertTrue(self.acc(r))
        r = account_result()
        r["skipped"] = []
        self.assertTrue(self.acc(r))
        r = account_result()
        r["days"][1]["low"] = 149757.46
        self.assertTrue(self.acc(r))

    def test_extra_fields_compared(self):
        for f, bad in (("signal", "S2"), ("y", 1.5), ("s1", 2.5), ("s2", 0.0), ("atr", 10.5)):
            r = account_result()
            r["trades"][2][f] = bad
            b = self.acc(r)
            self.assertEqual(len(b), 1, (f, b))
            self.assertIn(f"{f} is", b[0])

    def test_core_fields_compared(self):
        r = account_result()
        r["trades"][0]["worst"] = -0.5
        self.assertEqual(len(self.acc(r)), 1)


if __name__ == "__main__":
    unittest.main()
