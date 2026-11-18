#!/usr/bin/env python3
"""Tests for closemom.py against research/close-momentum-150k/PLAN.md: "The exact rule" and the amendment
"before any engine code". Synthetic bars on the micro Nasdaq's ticks (0.25, slippage 2 ticks = 0.5).
Run: python3 -I -B research/close-momentum-150k/test_closemom.py"""
import datetime as dt
import os
import sys
import unittest
from zoneinfo import ZoneInfo

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import closemom as cm  # noqa: E402
import mdata  # noqa: E402
import prescreen  # noqa: E402

ET = ZoneInfo("America/New_York")
UTC = dt.timezone.utc
NQ = {"traded": "MNQ", "pv": 2.0, "tick": 0.25, "comm": 1.90, "slip_ticks": 2, "max_qty": 90}
ZN = {"traded": "ZN", "pv": 1000.0, "tick": 1 / 64, "comm": 5.00, "slip_ticks": 1, "max_qty": 9}
O, C = 570, 960
MON, TUE, WED = dt.date(2019, 3, 4), dt.date(2019, 3, 5), dt.date(2019, 3, 6)


def ts(d, minute):
    return int(dt.datetime(d.year, d.month, d.day, minute // 60, minute % 60, tzinfo=ET).timestamp()) * 10 ** 9


def bar(d, minute, o, h=None, l=None, c=None, iid=1):
    h = o if h is None else h
    l = o if l is None else l
    c = o if c is None else c
    return mdata.Bar(ts(d, minute), iid, float(o), float(h), float(l), float(c), 1)


def daily_before(d, n=20, rng=40.0):
    """n daily bars dated (UTC) on the n calendar days before d, each with range rng: A = rng."""
    out = []
    for i in range(n, 0, -1):
        x = d - dt.timedelta(days=i)
        t = int(dt.datetime(x.year, x.month, x.day, tzinfo=UTC).timestamp()) * 10 ** 9
        b = mdata.Bar(t, 1, 1000.0, 1000.0 + rng, 1000.0, 1010.0, 1)
        out.append(mdata.Adj(b, b.open, b.high, b.low, b.close))
    return out


def S(signal="S1", k=0.1):
    return {"name": "%s-k%g" % (signal, k), "signal": signal, "k": k, "atr_days": 14}


def yday(d=MON, y=100.0, iid=1, o=O, c=C):
    """A trading day whose close (the open of the bar at C) is y."""
    return [bar(d, o, y, iid=iid), bar(d, c, y, iid=iid)]


def today(d=TUE, s2=101.0, s1=102.0, entry=(102.0, 103.0, 101.5), mid=(), exit_=(106.0, 106.5, 105.0), iid=1,
          o=O, c=C, extra=()):
    """Bars of day d: the open bar, the bar before O+30 closing at s2, the bar before C-30 closing at s1, the
    entry bar at C-30 (open, high, low), the bars `mid` [(minute, open, high, low)], the exit bar at C."""
    out = [bar(d, o, 100.0, iid=iid)]
    if s2 is not None:
        out.append(bar(d, o + 29, 100.0, max(100.0, s2), min(100.0, s2), s2, iid=iid))
    if s1 is not None:
        out.append(bar(d, c - 31, s1, c=s1, iid=iid))
    if entry is not None:
        out.append(bar(d, c - 30, entry[0], entry[1], entry[2], iid=iid))
    for m, a, h, l in mid:
        out.append(bar(d, m, a, h, l, iid=iid))
    if exit_ is not None:
        out.append(bar(d, c, exit_[0], exit_[1], exit_[2], iid=iid))
    out.extend(extra)
    return sorted(out, key=lambda b: b.ts)


def run(minutes, settings=None, fill="midpoint", spec=NQ, market="NQ", daily=None, dates=None):
    return cm.run(minutes, daily if daily is not None else daily_before(TUE), spec, market, settings or S(), fill,
                  dates)["trades"]


class Entry(unittest.TestCase):
    def test_long_closes_at_the_exit_bar_open_less_slippage(self):
        t, = run(yday() + today())
        self.assertEqual((t["market"], t["date"], t["signal"], t["side"]), ("NQ", "2019-03-05", "S1", 1))
        self.assertEqual((t["y"], t["s1"], t["s2"], t["atr"]), (100.0, 102.0, 101.0, 40.0))
        self.assertEqual((t["entry"], t["dist"], t["stop"]), (102.5, 4.0, 98.5))
        self.assertEqual((t["exit"], t["reason"], t["gap"]), (105.5, "close", False))
        self.assertEqual(t["points"], 3.0)
        self.assertEqual((t["entry_ts"], t["exit_ts"]), (ts(TUE, C - 30), ts(TUE, C)))

    def test_entry_held_inside_the_bar(self):
        t, = run(yday() + today(entry=(102.0, 102.25, 101.5)))
        self.assertEqual(t["entry"], 102.25)
        self.assertEqual(t["stop"], 98.25)

    def test_short_mirrors(self):
        t, = run(yday() + today(s2=99.0, s1=98.0, entry=(98.0, 98.5, 97.75), exit_=(95.0, 95.5, 94.0)))
        self.assertEqual(t["side"], -1)
        self.assertEqual((t["entry"], t["stop"]), (97.75, 101.75))   # 98 - 0.5 held at the low 97.75
        self.assertEqual((t["exit"], t["points"]), (95.5, 2.25))

    def test_dist_rounds_down_to_the_tick_with_a_one_tick_floor(self):
        t, = run(yday() + today(), settings=S(k=0.0999))          # 3.996 -> 3.75
        self.assertEqual(t["dist"], 3.75)
        t, = run(yday() + today(), settings=S(k=0.001))           # 0.04 -> one tick
        self.assertEqual(t["dist"], 0.25)
        self.assertEqual(t["stop"], 102.25)

    def test_a_is_the_mean_range_of_the_14_daily_bars_dated_before_the_day(self):
        daily = daily_before(TUE, n=13, rng=40.0)
        self.assertEqual(run(yday() + today(), daily=daily), [])
        x = TUE - dt.timedelta(days=14)
        b = mdata.Bar(int(dt.datetime(x.year, x.month, x.day, tzinfo=UTC).timestamp()) * 10 ** 9, 1, 0.0, 12.0,
                      0.0, 0.0, 1)
        daily = [mdata.Adj(b, 0.0, 12.0, 0.0, 0.0)] + daily
        later = TUE
        b2 = mdata.Bar(int(dt.datetime(later.year, later.month, later.day, tzinfo=UTC).timestamp()) * 10 ** 9, 1,
                       0.0, 999.0, 0.0, 0.0, 1)
        daily = daily + [mdata.Adj(b2, 0.0, 999.0, 0.0, 0.0)]       # dated the day itself: not used
        t, = run(yday() + today(), daily=daily)
        self.assertAlmostEqual(t["atr"], (13 * 40.0 + 12.0) / 14)


class Signals(unittest.TestCase):
    def test_s2_uses_the_first_half_hour(self):
        t, = run(yday() + today(s2=99.0, s1=102.0, entry=(102.0, 102.5, 101.0), exit_=(101.0, 101.5, 100.0)),
                 settings=S("S2"))
        self.assertEqual(t["side"], -1)
        self.assertEqual(t["signal"], "S2")

    def test_s3_trades_only_when_both_agree(self):
        self.assertEqual(run(yday() + today(s2=99.0, s1=102.0), settings=S("S3")), [])
        t, = run(yday() + today(s2=101.0, s1=102.0), settings=S("S3"))
        self.assertEqual(t["side"], 1)

    def test_equal_to_yesterday_is_no_trade(self):
        self.assertEqual(run(yday() + today(s1=100.0)), [])

    def test_a_missing_signal_bar_is_none_and_no_side(self):
        t, = run(yday() + today(s2=None), settings=S("S1"))
        self.assertIsNone(t["s2"])
        self.assertEqual(run(yday() + today(s2=None), settings=S("S2")), [])

    def test_y_is_the_open_of_the_bar_at_c(self):
        y = [bar(MON, O, 100.0), bar(MON, C, 100.0, 104.0, 100.0, 104.0)]
        t, = run(y + today(s1=102.0))
        self.assertEqual((t["y"], t["side"]), (100.0, 1))

    def test_s1_is_the_close_of_its_bar(self):
        b = [bar(TUE, C - 31, 98.0, 102.0, 98.0, 102.0)]
        t, = run(yday() + today(s1=None, extra=b))
        self.assertEqual((t["s1"], t["side"]), (102.0, 1))

    def test_the_price_at_c_minus_30_is_the_first_bar_within_five_minutes(self):
        late = [bar(TUE, C - 26, 102.0, 103.0, 101.5)]
        t, = run(yday() + today(entry=None, extra=late))
        self.assertEqual(t["entry_ts"], ts(TUE, C - 26))
        too_late = [bar(TUE, C - 25, 102.0, 103.0, 101.5)]
        self.assertEqual(run(yday() + today(entry=None, extra=too_late)), [])

    def test_the_last_price_before_looks_back_five_minutes_only(self):
        near = [bar(TUE, C - 35, 102.0)]
        t, = run(yday() + today(s1=None, extra=near))
        self.assertEqual(t["s1"], 102.0)
        old = [bar(TUE, C - 36, 102.0)]
        self.assertEqual(run(yday() + today(s1=None, extra=old)), [])
        s2_edge = [bar(TUE, O + 25, 99.0)]
        t, = run(yday() + today(s2=None, extra=s2_edge), settings=S("S2"))
        self.assertEqual((t["s2"], t["side"]), (99.0, -1))
        s2_late = [bar(TUE, O + 30, 99.0)]
        self.assertEqual(run(yday() + today(s2=None, extra=s2_late), settings=S("S2")), [])

    def test_a_roll_between_yesterday_and_today_is_no_trade(self):
        self.assertEqual(run(yday(iid=1) + today(iid=2)), [])

    def test_no_price_at_c_or_at_c_minus_30_is_no_trade(self):
        self.assertEqual(run(yday() + today(exit_=None)), [])
        self.assertEqual(run(yday() + today(entry=None)), [])

    def test_a_weekday_with_any_bar_is_a_trading_day(self):
        # PLAN.md: "a New York weekday with minute bars in it" (the check's C1, C2). Wednesday has only an evening
        # bar: it is the trading day before Thursday, it has no price at C, so Thursday has no Y and no trade.
        thu = dt.date(2019, 3, 7)
        wed_evening = [bar(WED, 18 * 60, 150.0)]
        self.assertEqual(run(yday(TUE) + wed_evening + today(thu), daily=daily_before(thu)), [])
        t, = run(yday(TUE) + today(thu), daily=daily_before(thu))   # no Wednesday bars: Tuesday is the day before
        self.assertEqual((t["date"], t["y"]), ("2019-03-07", 100.0))

    def test_a_contract_change_in_the_evening_of_the_day_means_no_trade(self):
        # PLAN.md rule 2, "that bar and today's bars" (the check's C5): every bar dated d, the evening included.
        evening = [bar(TUE, 19 * 60, 102.0, iid=2)]
        self.assertEqual(run(yday() + today(extra=evening)), [])
        same = [bar(TUE, 19 * 60, 102.0, iid=1)]
        self.assertEqual(len(run(yday() + today(extra=same))), 1)

    def test_within_eps_of_y_is_equal(self):
        # The amendment: eps = tick x 1e-6 in every comparison (the check's C6).
        self.assertEqual(run(yday() + today(s1=100.0 + 0.25 * 1e-7)), [])
        self.assertEqual(len(run(yday() + today(s1=100.0 + 0.25 * 1e-5))), 1)

    def test_weekend_bars_do_not_make_a_trading_day(self):
        fri, mon = dt.date(2019, 3, 1), dt.date(2019, 3, 4)
        sat = [bar(dt.date(2019, 3, 2), O, 150.0), bar(dt.date(2019, 3, 2), C, 150.0)]
        t, = run(yday(fri) + sat + today(mon), daily=daily_before(mon))
        self.assertEqual(t["y"], 100.0)

    def test_dates_limits_the_days_run(self):
        self.assertEqual(run(yday() + today(), dates={"2019-03-06"}), [])
        self.assertEqual(len(run(yday() + today(), dates={"2019-03-05"})), 1)

    def test_each_market_has_its_own_open_and_close(self):
        o, c = cm.HOURS["ZN"]
        self.assertEqual((o, c), (500, 900))
        bars = yday(o=o, c=c, y=120.0) + today(o=o, c=c, s2=120.5, s1=121.0, entry=(121.0, 121.5, 121.0),
                                               exit_=(122.0, 122.0, 121.5))
        t, = run(bars, spec=ZN, market="ZN", daily=daily_before(TUE, rng=0.64))
        self.assertEqual((t["entry_ts"], t["exit_ts"]), (ts(TUE, c - 30), ts(TUE, c)))
        self.assertAlmostEqual(t["entry"], 121.0 + 1 / 64)
        self.assertAlmostEqual(t["dist"], 4 / 64)                   # 0.064 -> 4 ticks of 1/64
        self.assertEqual(cm.HOURS, prescreen.HOURS)


class Stop(unittest.TestCase):
    MID = [(C - 20, 100.0, 100.5, 97.75)]       # reaches the 98.5 stop; midpoint 98.125 -> 98.0

    def test_midpoint_kind_and_harsh_long(self):
        got = {f: run(yday() + today(mid=self.MID), fill=f)[0] for f in ("midpoint", "kind", "harsh-stops")}
        self.assertEqual({f: t["exit"] for f, t in got.items()}, {"midpoint": 98.0, "kind": 98.0,
                                                                  "harsh-stops": 97.75})
        t = got["midpoint"]
        self.assertEqual((t["reason"], t["gap"], t["exit_ts"]), ("stop", False, ts(TUE, C - 20)))
        self.assertEqual(t["points"], -4.5)

    def test_kind_is_one_slippage_beyond_unless_the_low_is_nearer(self):
        t, = run(yday() + today(mid=[(C - 20, 100.0, 100.5, 97.0)]), fill="kind")
        self.assertEqual(t["exit"], 98.0)
        t, = run(yday() + today(mid=[(C - 20, 100.0, 100.5, 98.25)]), fill="kind")
        self.assertEqual(t["exit"], 98.25)

    def test_a_gap_fills_from_the_open(self):
        t, = run(yday() + today(mid=[(C - 20, 98.0, 98.25, 97.0)]))
        self.assertEqual((t["exit"], t["gap"]), (97.5, True))
        t, = run(yday() + today(mid=[(C - 20, 98.0, 98.25, 97.0)]), fill="kind")
        self.assertEqual(t["exit"], 97.5)

    def test_short_stop_rounds_up(self):
        bars = yday() + today(s2=99.0, s1=98.0, entry=(98.0, 98.5, 97.0), mid=[(C - 10, 101.0, 102.25, 100.5)],
                              exit_=(95.0, 95.5, 94.0))
        t, = run(bars)                                              # entry 97.5, stop 101.5, (101.5+102.25)/2
        self.assertEqual((t["stop"], t["exit"], t["reason"]), (101.5, 102.0, "stop"))
        t, = run(bars, fill="harsh-stops")
        self.assertEqual(t["exit"], 102.25)

    def test_the_entry_bar_itself_is_watched(self):
        t, = run(yday() + today(entry=(102.0, 103.0, 98.0)))
        self.assertEqual((t["reason"], t["exit_ts"]), ("stop", ts(TUE, C - 30)))
        self.assertEqual(t["exit"], 98.25)                          # floor_tick((98.5 + 98) / 2)
        self.assertEqual(t["worst"], 98.0 - 102.5)

    def test_the_exit_bar_is_not_checked_for_the_stop(self):
        t, = run(yday() + today(exit_=(98.0, 98.5, 96.0)))
        self.assertEqual((t["reason"], t["exit"]), ("close", 97.5))

    def test_the_exit_is_held_inside_its_bar(self):
        t, = run(yday() + today(exit_=(106.0, 106.5, 105.75)))
        self.assertEqual(t["exit"], 105.75)

    def test_a_bar_after_the_exit_bar_is_not_watched(self):
        t, = run(yday() + today(extra=[bar(TUE, C + 1, 99.0, 99.0, 90.0)]))
        self.assertEqual(t["reason"], "close")

    def test_the_first_stop_minute_ends_it(self):
        t, = run(yday() + today(mid=[(C - 20, 100.0, 100.5, 97.75), (C - 19, 97.0, 97.0, 90.0)]))
        self.assertEqual((t["exit_ts"], t["exit"]), (ts(TUE, C - 20), 98.0))


class Worst(unittest.TestCase):
    def test_a_stop_minute_counts_whole(self):
        t, = run(yday() + today(mid=[(C - 25, 101.0, 101.0, 100.0), (C - 20, 100.0, 100.5, 97.75)]))
        self.assertEqual(t["worst"], 97.75 - 102.5)

    def test_a_close_counts_the_exit_bar_only_at_its_fill(self):
        t, = run(yday() + today(mid=[(C - 25, 101.0, 101.0, 100.0)], exit_=(101.0, 101.0, 99.0)))
        self.assertEqual(t["exit"], 100.5)
        self.assertEqual(t["worst"], 100.0 - 102.5)                 # the 15:35 low, not the exit bar's 99
        t, = run(yday() + today(mid=[(C - 25, 101.0, 101.0, 101.0)], exit_=(100.25, 100.25, 99.0)))
        self.assertEqual(t["worst"], max(99.0, 100.25 - 0.5) - 102.5)

    def test_short_worst_uses_the_high(self):
        t, = run(yday() + today(s2=99.0, s1=98.0, entry=(98.0, 99.0, 97.0), mid=[(C - 25, 98.0, 100.0, 97.0)],
                                exit_=(95.0, 95.5, 94.0)))
        self.assertEqual(t["worst"], -(100.0 - 97.5))


class AgreesWithThePrescreen(unittest.TestCase):
    def test_same_days_sides_and_entry_bars(self):
        days = [dt.date(2019, 3, 4) + dt.timedelta(days=i) for i in range(10)]
        days = [d for d in days if d.weekday() < 5]
        bars, y = [], 100.0
        for n, d in enumerate(days):
            s = 100.0 + (3 if n % 3 else -3)
            bars += [bar(d, O, 100.0), bar(d, O + 29, 100.0, c=s - 1), bar(d, C - 31, s, c=s),
                     bar(d, C - 30, s, s + 1, s - 1), bar(d, C, s + (1 if n % 2 else -1))]
        bars.sort(key=lambda b: b.ts)
        daily = daily_before(days[0])
        for sig in ("S1", "S2", "S3"):
            mine = [(t["date"], t["side"]) for t in run(bars, settings=S(sig), daily=daily)]
            theirs = [(dt.date.fromordinal(d).isoformat(), s[sig]) for d, s, e, x in prescreen.trades(bars, O, C)
                      if s[sig]]
            self.assertEqual(mine, theirs, sig)
            self.assertTrue(mine)


if __name__ == "__main__":
    unittest.main()
