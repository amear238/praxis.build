#!/usr/bin/env python3
"""Tests for measure.py. Run: python3 -I -B research/noise-area-variations/test_measure.py

Hand-built days with a hand-built band (bands.day_bands patched) check what counts as a breakout, the
half-hour and any-minute decision bars, the reference price, the four stop distances, the order in which
the stop and the favourable move are checked, tight stops, the parts of the day and the tables. Random days
with the real band check that no event looks ahead. A small synthetic data file checks main: the range
guard, two runs byte-identical, and that a run started mid-range agrees with a run from the beginning.
No test reads the real data file.
"""
import contextlib
import datetime as dt
import io
import json
import os
import random
import shutil
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import globex as g    # noqa: E402
import bands as bd    # noqa: E402
import measure as ms  # noqa: E402

BASE = dt.date(2022, 1, 3)   # a Monday


def stamp_of(date, sm):
    """Trading date + session minute -> the bar's end-of-minute stamp (evening minutes are the day before)."""
    m = sm + 18 * 60
    if m >= 24 * 60:
        return dt.datetime(date.year, date.month, date.day) + dt.timedelta(minutes=m - 24 * 60)
    return dt.datetime(date.year, date.month, date.day) - dt.timedelta(days=1) + dt.timedelta(minutes=m)


def date_of(i):
    return BASE + dt.timedelta(days=7 * (i // 5) + i % 5)


def make_day(i, bars):
    """Day number i (a weekday counted from BASE) from [(hhmm or sm, o, h, l, c), ...] in time order."""
    date = date_of(i)
    d = g.Day(date.isoformat())
    for t, o, h, l, c in bars:
        sm = g.sm_of(t) if isinstance(t, str) else t
        d.by_sm[sm] = len(d.bars)
        d.bars.append(g.Bar(stamp_of(date, sm), sm, float(o), float(h), float(l), float(c), 10))
    return d


def flat(t, c):
    """A bar at t that opens, trades and closes at c."""
    return (t, c, c, c, c)


def minutes(first, closes):
    """Consecutive one-minute flat bars starting at stamp `first`, closing at each of closes."""
    sm0 = g.sm_of(first)
    return [flat(sm0 + j, c) for j, c in enumerate(closes)]


def fake_bands(upper=120.0, lower=80.0, anchor_price=100.0, width=20.0, from_sm=None):
    """A stand-in for bands.day_bands: the same band at every bar of the day from from_sm on."""
    def day_bands(days, k, anchor, lookback=14, mult=1.0):
        start = from_sm if from_sm is not None else bd.ANCHORS[anchor]
        return {b.sm: bd.BandPoint(upper, lower, 100.0, anchor_price, width)
                for b in days[k].bars if b.sm >= start}
    return day_bands


def run(days, anchor="0930", cadence="minute", **band):
    with mock.patch.object(bd, "day_bands", fake_bands(**band)):
        return ms.events(days, anchor, cadence)


class Breakouts(unittest.TestCase):
    def test_one_event_per_excursion(self):
        # inside, then 5 closes above in a row, back inside, above again
        day = make_day(0, minutes("10:00", [100, 121, 122, 123, 124, 125, 110, 121, 100]))
        evts = run([day])
        self.assertEqual([(e["time"], e["side"]) for e in evts], [("10:01", "long"), ("10:07", "long")])

    def test_on_the_band_is_inside(self):
        # a close exactly on the upper band is inside: it ends the excursion
        day = make_day(0, minutes("10:00", [121, 120, 121, 80, 79, 100]))
        evts = run([day])
        self.assertEqual([(e["time"], e["side"]) for e in evts],
                         [("10:00", "long"), ("10:02", "long"), ("10:04", "short")])

    def test_straight_through_to_other_side(self):
        day = make_day(0, minutes("10:00", [100, 121, 79, 70, 121, 100]))
        evts = run([day])
        self.assertEqual([(e["time"], e["side"]) for e in evts],
                         [("10:01", "long"), ("10:02", "short"), ("10:04", "long")])

    def test_first_decision_bar_already_outside(self):
        # the band exists from 09:31; the day's first decision bar closes above it: an event
        day = make_day(0, [flat("09:00", 150)] + minutes("09:31", [121, 122, 100]))
        evts = run([day])
        self.assertEqual([e["time"] for e in evts], ["09:31"])

    def test_each_day_starts_fresh(self):
        # day 0 ends outside; day 1's first decision bar is still outside: a new event on day 1
        d0 = make_day(0, minutes("10:00", [100, 121, 122]))
        d1 = make_day(1, minutes("10:00", [123, 124]))
        evts = run([d0, d1])
        self.assertEqual([(e["date"], e["time"]) for e in evts],
                         [(d0.date, "10:01"), (d1.date, "10:00")])

    def test_half_hour_ignores_other_minutes(self):
        closes = [100] * 17 + [121] * 14 + [100] * 3          # 10:00..10:16 inside, 10:17..10:30 above
        day = make_day(0, minutes("10:00", closes))
        self.assertEqual([e["time"] for e in run([day], cadence="half_hour")], ["10:30"])
        self.assertEqual([e["time"] for e in run([day], cadence="minute")], ["10:17"])
        # out at 10:17, back inside by 10:30: no half-hour event at all
        closes = [100] * 17 + [121] * 8 + [100] * 9
        day = make_day(0, minutes("10:00", closes))
        self.assertEqual(run([day], cadence="half_hour"), [])
        # half-hour excursions are judged on half-hour closes only: inside at 10:47 does not end it
        closes = [100] * 30 + [121] * 17 + [100] + [121] * 20  # 10:30 above, 10:47 inside, 11:00 above
        day = make_day(0, minutes("10:00", closes))
        self.assertEqual([e["time"] for e in run([day], cadence="half_hour")], ["10:30"])

    def test_no_next_bar_no_event(self):
        # an early close: the last bar of the day closes outside, there is no entry bar
        day = make_day(0, minutes("12:58", [100, 100, 121]))
        self.assertEqual(run([day]), [])
        # same with a half-hour decision bar that is the day's last bar
        day = make_day(0, minutes("12:30", [100] * 30 + [121]))
        self.assertEqual(run([day], cadence="half_hour"), [])

    def test_last_decision_bar_is_1559(self):
        day = make_day(0, minutes("15:57", [100, 100, 121, 100]))   # 15:59 above, entry 16:00
        evts = run([day])
        self.assertEqual([(e["time"], e["entry_time"]) for e in evts], [("15:59", "16:00")])
        day = make_day(0, minutes("15:57", [100, 100, 100, 121]))   # 16:00 above: not a decision bar
        self.assertEqual(run([day]), [])
        # half-hour: the last decision bar is 15:30; above from 15:31 on is never decided
        day = make_day(0, minutes("15:29", [100, 100] + [121] * 30))
        self.assertEqual(run([day], cadence="half_hour"), [])
        day = make_day(0, minutes("15:29", [100] + [121] * 31))
        self.assertEqual([e["time"] for e in run([day], cadence="half_hour")], ["15:30"])

    def test_only_bars_with_a_band_decide(self):
        # the band starts at 09:31 for the 9:30 anchor: closes before it decide nothing
        day = make_day(0, minutes("09:28", [150, 150, 150, 100, 121, 100]))
        self.assertEqual([e["time"] for e in run([day])], ["09:32"])
        # a band from 18:01 (the 6 PM anchor) decides in the evening too
        day = make_day(0, minutes("18:01", [100, 121, 100]))
        self.assertEqual([(e["time"], e["part"]) for e in run([day], anchor="1800")], [("18:02", "evening")])

    def test_event_fields(self):
        day = make_day(0, [flat("10:00", 100), ("10:01", 118, 122, 117, 121), ("10:02", 123, 124, 122, 123),
                           flat("10:03", 123)])
        (e,) = run([day], anchor="0930", cadence="minute")
        self.assertEqual((e["date"], e["time"], e["sm"], e["part"], e["side"], e["anchor"], e["cadence"]),
                         (day.date, "10:01", g.sm_of("10:01"), "morning", "long", "0930", "minute"))
        self.assertEqual((e["close"], e["upper"], e["lower"], e["anchor_price"], e["width"]),
                         (121.0, 120.0, 80.0, 100.0, 20.0))
        self.assertEqual((e["entry_time"], e["ref"]), ("10:02", 123.0))
        self.assertEqual(sorted(e["stops"]), sorted(ms.STOPS))


class Distances(unittest.TestCase):
    def test_long_distances(self):
        # ref 125 (next open, no slippage); band 80..120, anchor 100, width 20
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 125, 126, 124, 125),
                           flat("10:03", 125)])
        (e,) = run([day])
        self.assertEqual(e["ref"], 125.0)
        dist = {k: e["stops"][k]["dist"] for k in ms.STOPS}
        self.assertEqual(dist, {"half_width": 10.0, "full_width": 20.0, "to_anchor": 25.0,
                                "opposite_band": 45.0})

    def test_short_distances(self):
        # ref 77; for a short: to_anchor = 100 - 77, opposite band = 120 - 77
        day = make_day(0, [flat("10:00", 100), flat("10:01", 79), ("10:02", 77, 78, 76, 77),
                           flat("10:03", 77)])
        (e,) = run([day])
        self.assertEqual((e["side"], e["ref"]), ("short", 77.0))
        dist = {k: e["stops"][k]["dist"] for k in ms.STOPS}
        self.assertEqual(dist, {"half_width": 10.0, "full_width": 20.0, "to_anchor": 23.0,
                                "opposite_band": 43.0})

    def test_distances_use_the_decision_bar_band(self):
        # the band at the entry bar differs from the band at the decision bar: the decision bar's is used
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), flat("10:02", 125), flat("10:03", 125)])
        sm1 = g.sm_of("10:01")

        def day_bands(days, k, anchor, lookback=14, mult=1.0):
            out = {}
            for b in days[k].bars:
                w = 20.0 if b.sm <= sm1 else 60.0
                lo = 80.0 if b.sm <= sm1 else 10.0
                out[b.sm] = bd.BandPoint(120.0, lo, 100.0, 100.0 if b.sm <= sm1 else 50.0, w)
            return out
        with mock.patch.object(bd, "day_bands", day_bands):
            (e,) = ms.events([day], "0930", "minute")
        dist = {k: e["stops"][k]["dist"] for k in ms.STOPS}
        self.assertEqual(dist, {"half_width": 10.0, "full_width": 20.0, "to_anchor": 25.0,
                                "opposite_band": 45.0})


class Outcomes(unittest.TestCase):
    def test_mfe_and_stop_order(self):
        # long, ref 121, full width 20 -> stop 101: bars run to +50, then down to -25 -> stopped
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 121, 171, 119, 160),
                           ("10:03", 160, 161, 96, 98), ("10:04", 98, 300, 98, 290)])
        (e,) = run([day])
        s = e["stops"]["full_width"]
        self.assertEqual(s["dist"], 20.0)
        self.assertFalse(s["tight"])
        self.assertTrue(s["stopped"])
        self.assertEqual(s["stop_time"], "10:03")
        self.assertEqual(s["mfe_r"], 2.5)
        self.assertEqual((s["reached_2"], s["reached_3"], s["reached_5"]), (True, False, False))
        self.assertEqual(s["r_at_flat"], -1.0)

    def test_stop_bar_favourable_move_not_counted(self):
        # long, ref 121, full width 20 -> stop 101. The entry bar itself reaches +100 and touches 101.
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 121, 221, 101, 200),
                           flat("10:03", 200)])
        (e,) = run([day])
        s = e["stops"]["full_width"]
        self.assertTrue(s["stopped"])
        self.assertEqual(s["stop_time"], "10:02")
        self.assertEqual(s["mfe_r"], 0.0)
        self.assertEqual((s["reached_2"], s["reached_3"], s["reached_5"]), (False, False, False))
        self.assertEqual(s["r_at_flat"], -1.0)
        # a later stop bar: the favourable move of the bars before it counts, the stop bar's does not
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 121, 151, 120, 150),
                           ("10:03", 150, 250, 100, 120)])
        s = run([day])[0]["stops"]["full_width"]
        self.assertEqual((s["stopped"], s["mfe_r"]), (True, 1.5))

    def test_held_to_the_flat(self):
        # long, ref 121, half width 10 -> stop 111: never hit; best +60; last bar of the day closes at 146
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 121, 140, 112, 139),
                           ("15:59", 139, 181, 130, 150), ("16:00", 150, 151, 145, 146)])
        (e,) = run([day])
        s = e["stops"]["half_width"]
        self.assertEqual(s["dist"], 10.0)
        self.assertFalse(s["stopped"])
        self.assertIsNone(s["stop_time"])
        self.assertEqual(s["mfe_r"], 6.0)
        self.assertEqual((s["reached_2"], s["reached_3"], s["reached_5"]), (True, True, True))
        self.assertEqual(s["r_at_flat"], 2.5)

    def test_flat_below_entry(self):
        # not stopped but closing below the entry: a negative result above -1
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), ("10:02", 121, 122, 105, 106)])
        s = run([day])[0]["stops"]["full_width"]
        self.assertEqual((s["stopped"], s["mfe_r"], s["r_at_flat"]), (False, 0.05, -0.75))

    def test_short_outcome(self):
        # short, ref 79, full width 20 -> stop 99; runs to 19 (+3R), then flat at 49 (+1.5R)
        day = make_day(0, [flat("10:00", 100), flat("10:01", 79), ("10:02", 79, 98, 19, 30),
                           ("13:00", 30, 49, 25, 49)])
        (e,) = run([day])
        s = e["stops"]["full_width"]
        self.assertEqual(e["side"], "short")
        self.assertEqual((s["stopped"], s["mfe_r"], s["r_at_flat"]), (False, 3.0, 1.5))
        self.assertEqual((s["reached_2"], s["reached_3"], s["reached_5"]), (True, True, False))
        # the same short stopped: the bar's high reaches 99; its low (the favourable side) is not counted
        day = make_day(0, [flat("10:00", 100), flat("10:01", 79), ("10:02", 79, 99, 0, 50)])
        s = run([day])[0]["stops"]["full_width"]
        self.assertEqual((s["stopped"], s["mfe_r"], s["r_at_flat"]), (True, 0.0, -1.0))

    def test_walk_stays_in_the_day(self):
        # the next day crashes; the event's walk ends at its own day's last bar
        d0 = make_day(0, [flat("10:00", 100), flat("10:01", 121), flat("10:02", 121), flat("12:00", 131)])
        d1 = make_day(1, [flat("10:00", 1)])
        s = run([d0, d1])[0]["stops"]["full_width"]
        self.assertEqual((s["stopped"], s["mfe_r"], s["r_at_flat"]), (False, 0.5, 0.5))

    def test_tight(self):
        # width 12: half width 6 is tight; outcome fields are None for it, filled for the others
        day = make_day(0, [flat("10:00", 100), flat("10:01", 113), flat("10:02", 113), flat("10:03", 140)])
        (e,) = run([day], upper=112.0, lower=88.0, width=12.0)
        hw = e["stops"]["half_width"]
        self.assertEqual((hw["dist"], hw["tight"]), (6.0, True))
        for k in ("stopped", "stop_time", "mfe_r", "r_at_flat", "reached_2", "reached_3", "reached_5"):
            self.assertIsNone(hw[k], k)
        fw = e["stops"]["full_width"]
        self.assertEqual((fw["dist"], fw["tight"], fw["stopped"]), (12.0, False, False))
        self.assertAlmostEqual(fw["mfe_r"], 27.0 / 12.0, places=12)

    def test_tight_threshold_and_negative(self):
        self.assertEqual(ms.MIN_STOP_POINTS, 10.0)
        # half width 10.0 exactly is not tight; ref below the anchor on a long makes to_anchor negative
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), flat("10:02", 95), flat("10:03", 95)])
        e = run([day])[0]["stops"]
        self.assertEqual((e["half_width"]["dist"], e["half_width"]["tight"]), (10.0, False))
        self.assertEqual((e["to_anchor"]["dist"], e["to_anchor"]["tight"]), (-5.0, True))
        self.assertIsNone(e["to_anchor"]["mfe_r"])
        # ref exactly on the anchor: distance 0, tight
        day = make_day(0, [flat("10:00", 100), flat("10:01", 121), flat("10:02", 100), flat("10:03", 95)])
        e = run([day])[0]["stops"]
        self.assertEqual((e["to_anchor"]["dist"], e["to_anchor"]["tight"]), (0.0, True))


class Parts(unittest.TestCase):
    STAMPS = ["18:01", "02:00", "02:01", "09:30", "09:31", "11:30", "14:00", "14:01"]
    WANT = ["evening", "evening", "overnight", "overnight", "morning", "morning", "midday", "afternoon"]

    def test_parts(self):
        self.assertEqual([ms.part_of(t) for t in self.STAMPS], self.WANT)
        self.assertEqual([ms.part_of(t) for t in ("23:59", "00:00", "11:31", "15:59", "16:00")],
                         ["evening", "evening", "midday", "afternoon", "afternoon"])
        self.assertEqual([p[0] for p in ms.PARTS], ["evening", "overnight", "morning", "midday", "afternoon"])

    def test_parts_on_events(self):
        # a bar at each stamp above, closing above and below the 6 PM band in turn: each one is a breakout
        bars = [flat(t, 121 if j % 2 == 0 else 79) for j, t in enumerate(self.STAMPS)] + [flat("14:02", 100)]
        day = make_day(0, bars)
        evts = run([day], anchor="1800", from_sm=1)
        self.assertEqual([(e["time"], e["part"]) for e in evts], list(zip(self.STAMPS, self.WANT)))


def random_days(n, seed, step=10):
    """n weekdays of bars every `step` minutes from 18:01 to 16:00 (plus 09:31), a seeded random walk."""
    rnd = random.Random(seed)
    sms = sorted(set([1, g.sm_of("09:31")] + list(range(step, g.sm_of("16:00") + 1, step))))
    days = []
    px = 15000.0
    for i in range(n):
        bars = []
        for sm in sms:
            o = px
            c = round(o + rnd.gauss(0.0, 9.0), 2)
            h = round(max(o, c) + abs(rnd.gauss(0.0, 4.0)), 2)
            l = round(min(o, c) - abs(rnd.gauss(0.0, 4.0)), 2)
            bars.append((sm, o, h, l, c))
            px = c
        days.append(make_day(i, bars))
        px = round(px + rnd.gauss(0.0, 30.0), 2)
    return days


def copy_day(day, after=None, keep_open_at=None, factor=1.0):
    """A copy of day; bars with sm > after (all when None) get every price scaled, except that the open of
    the bar at sm keep_open_at stays as it was."""
    out = g.Day(day.date)
    for b in day.bars:
        f = factor if (after is None or b.sm > after) else 1.0
        o = b.o if b.sm == keep_open_at else b.o * f
        out.by_sm[b.sm] = len(out.bars)
        out.bars.append(g.Bar(b.dt, b.sm, o, b.h * f, b.l * f, b.c * f, b.v))
    return out


KNOWN_NOW = ("date", "time", "sm", "part", "side", "anchor", "cadence", "close", "upper", "lower",
             "anchor_price", "width", "entry_time", "ref")


def known_at_decision(e):
    """The fields of an event that must be known at its decision bar (plus the next bar's open)."""
    return (tuple(e[k] for k in KNOWN_NOW)
            + tuple((k, e["stops"][k]["dist"], e["stops"][k]["tight"]) for k in ms.STOPS))


class NoLookAhead(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.days = random_days(20, seed=20221117)

    def test_no_lookahead(self):
        days = self.days
        checked = 0
        for anchor in ("0930", "1800"):
            for cadence in ("half_hour", "minute"):
                base = ms.events(days, anchor, cadence)
                self.assertTrue(base, "%s %s has events" % (anchor, cadence))
                for k in (15, 18):
                    date = days[k].date
                    todays = [e for e in base if e["date"] == date]
                    self.assertTrue(todays, "%s %s day %d has events" % (anchor, cadence, k))
                    for e in todays[:: max(1, len(todays) // 4)]:
                        T = e["sm"]
                        entry = days[k].bars[days[k].by_sm[T] + 1].sm
                        changed = (days[:k]
                                   + [copy_day(days[k], after=T, keep_open_at=entry, factor=0.93)]
                                   + [copy_day(d, factor=1.11) for d in days[k + 1:]])
                        after = ms.events(changed, anchor, cadence)
                        want = [known_at_decision(x) for x in base
                                if x["date"] < date or (x["date"] == date and x["sm"] <= T)]
                        got = [known_at_decision(x) for x in after
                               if x["date"] < date or (x["date"] == date and x["sm"] <= T)]
                        self.assertEqual(got, want, "%s %s day %d T=%d" % (anchor, cadence, k, T))
                        checked += 1
        self.assertGreater(checked, 8)

    def test_outcomes_do_look_forward(self):
        # sanity for the test above: changing the bars after the entry does change some outcome
        days = self.days
        k = 16
        base = [e for e in ms.events(days, "1800", "minute") if e["date"] == days[k].date]
        e = base[0]
        entry = days[k].bars[days[k].by_sm[e["sm"]] + 1].sm
        changed = days[:k] + [copy_day(days[k], after=entry, factor=0.8)] + days[k + 1:]
        e2 = [x for x in ms.events(changed, "1800", "minute") if x["date"] == days[k].date][0]
        self.assertEqual(known_at_decision(e2), known_at_decision(e))
        self.assertNotEqual(e2["stops"], e["stops"])


def mk_evt(date, part, side, anchor="1800", cadence="minute", **stops):
    """A hand-built event for the tables: stops maps a stop kind to (tight, mfe_r, r_at_flat)."""
    st = {}
    for k in ms.STOPS:
        tight, mfe_r, r = stops.get(k, (False, 0.0, -1.0))
        if tight:
            st[k] = {"dist": 5.0, "tight": True, "stopped": None, "stop_time": None, "mfe_r": None,
                     "r_at_flat": None, "reached_2": None, "reached_3": None, "reached_5": None}
        else:
            st[k] = {"dist": 20.0, "tight": False, "stopped": r == -1.0, "stop_time": None, "mfe_r": mfe_r,
                     "r_at_flat": r, "reached_2": mfe_r >= 2, "reached_3": mfe_r >= 3, "reached_5": mfe_r >= 5}
    return {"date": date, "time": "10:00", "sm": 960, "part": part, "side": side, "anchor": anchor,
            "cadence": cadence, "stops": st}


class Tables(unittest.TestCase):
    CAL = ["2022-01-%02d" % d for d in (3, 4, 5, 6, 7, 10, 11, 12, 13, 14)]

    def evts(self):
        c = self.CAL
        return [
            mk_evt(c[2], "morning", "long", full_width=(False, 2.5, -1.0)),
            mk_evt(c[3], "morning", "long", full_width=(False, 5.0, 3.0)),
            mk_evt(c[5], "morning", "long", full_width=(True, None, None)),   # tight: does not break a gap
            mk_evt(c[7], "morning", "short", full_width=(False, 1.0, 0.5)),
            mk_evt(c[7], "evening", "short", full_width=(False, 3.5, 2.0)),
        ]

    def row(self, rows, **key):
        found = [r for r in rows if all(r[k] == v for k, v in key.items())]
        self.assertEqual(len(found), 1, key)
        return found[0]

    def test_tables_rows(self):
        rows = ms.tables(self.evts(), calendars={"1800": self.CAL})
        r = self.row(rows, anchor="1800", cadence="minute", stop="full_width", part="morning", side="long")
        self.assertEqual((r["n"], r["tight_excluded"]), (2, 1))
        self.assertEqual((r["pct_reached_2"], r["pct_reached_3"], r["pct_reached_5"]), (100.0, 50.0, 50.0))
        self.assertEqual(r["avg_r_at_flat"], 1.0)
        # morning long events on c[2], c[3] (c[5] is tight): runs 2, 6 -> 6
        self.assertEqual(r["max_gap_trading_days"], 6)
        b = self.row(rows, anchor="1800", cadence="minute", stop="full_width", part="morning", side="both")
        self.assertEqual((b["n"], b["tight_excluded"]), (3, 1))
        self.assertAlmostEqual(b["pct_reached_2"], 200.0 / 3, places=9)
        self.assertAlmostEqual(b["avg_r_at_flat"], 2.5 / 3, places=12)
        self.assertEqual(b["max_gap_trading_days"], 3)     # events c[2], c[3], c[7]: runs 2, 3, 2
        a = self.row(rows, anchor="1800", cadence="minute", stop="full_width", part="all", side="both")
        self.assertEqual((a["n"], a["tight_excluded"]), (4, 1))
        self.assertEqual(a["pct_reached_3"], 50.0)
        # half width: nothing is tight; the c[5] event counts and breaks the gap
        h = self.row(rows, anchor="1800", cadence="minute", stop="half_width", part="morning", side="long")
        self.assertEqual((h["n"], h["tight_excluded"], h["max_gap_trading_days"]), (3, 0, 4))

    def test_empty_rows(self):
        rows = ms.tables(self.evts(), calendars={"1800": self.CAL})
        r = self.row(rows, anchor="1800", cadence="minute", stop="to_anchor", part="afternoon", side="short")
        self.assertEqual((r["n"], r["tight_excluded"], r["max_gap_trading_days"]), (0, 0, 10))
        for k in ("pct_reached_2", "pct_reached_3", "pct_reached_5", "avg_r_at_flat"):
            self.assertIsNone(r[k])

    def test_row_set_and_order(self):
        evts = self.evts() + [mk_evt(self.CAL[0], "morning", "long", anchor="0930", cadence="half_hour")]
        rows = ms.tables(evts, calendars={"1800": self.CAL, "0930": self.CAL})
        keys = [(r["anchor"], r["cadence"], r["stop"], r["part"], r["side"]) for r in rows]
        self.assertEqual(len(keys), len(set(keys)))
        parts_0930 = ["morning", "midday", "afternoon", "all"]
        parts_1800 = [p[0] for p in ms.PARTS] + ["all"]
        want = ([("0930", "half_hour", s, p, sd) for s in ms.STOPS for p in parts_0930
                 for sd in ("long", "short", "both")]
                + [("1800", "minute", s, p, sd) for s in ms.STOPS for p in parts_1800
                   for sd in ("long", "short", "both")])
        self.assertEqual(keys, want)
        for r in rows:
            self.assertEqual(sorted(r), sorted(["anchor", "cadence", "stop", "part", "side", "n", "tight_excluded",
                                                "pct_reached_2", "pct_reached_3", "pct_reached_5",
                                                "avg_r_at_flat", "max_gap_trading_days"]))

    def test_calendar(self):
        # the trading days from the first day with a band to the last day loaded
        days = [make_day(i, minutes("09:31", [100, 100])) for i in range(6)]

        def day_bands(dd, k, anchor, lookback=14, mult=1.0):
            return {} if k < 2 or k == 4 else {931: bd.BandPoint(120.0, 80.0, 100.0, 100.0, 20.0)}
        with mock.patch.object(bd, "day_bands", day_bands):
            self.assertEqual(ms.calendar(days, "0930"), [d.date for d in days[2:]])


def write_data(path, days):
    with open(path, "w", encoding="ascii", newline="") as fh:
        for d in days:
            for b in d.bars:
                fh.write("%s;%r;%r;%r;%r;%d\r\n" % (b.dt.strftime("%Y%m%d %H%M%S"), b.o, b.h, b.l, b.c, b.v))


class Main(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="measure-test-")
        cls.data = os.path.join(cls.tmp, "data.txt")
        write_data(cls.data, random_days(24, seed=20231117, step=15))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ms.main(list(args))
        return code, out.getvalue(), err.getvalue()

    def test_range_guard(self):
        out = os.path.join(self.tmp, "guard")
        code, _, err = self.main("--data", self.data, "--end", "2024-01-02", "--out", out)
        self.assertEqual(code, 2)
        self.assertIn("2023-12-31", err)
        self.assertFalse(os.path.exists(out))
        code, _, _ = self.main("--data", self.data, "--start", "2022-02-01", "--end", "2022-01-31", "--out", out)
        self.assertEqual(code, 2)
        self.assertFalse(os.path.exists(out))
        code, _, _ = self.main("--data", self.data, "--end", "2024-01-02", "--allow-later", "--out", out)
        self.assertEqual(code, 0)
        self.assertTrue(os.path.exists(os.path.join(out, "tables.json")))
        self.assertEqual(ms.DEFAULT_START, "2021-03-08")
        self.assertEqual(ms.DEFAULT_END, "2023-12-31")

    def test_same_twice(self):
        outs = []
        for name in ("one", "two"):
            out = os.path.join(self.tmp, name)
            code, _, _ = self.main("--data", self.data, "--out", out)
            self.assertEqual(code, 0)
            outs.append(out)
        names = sorted(os.listdir(outs[0]))
        self.assertEqual(names, sorted(os.listdir(outs[1])))
        self.assertEqual(names, ["events-0930-half_hour.json", "events-0930-minute.json",
                                 "events-1800-half_hour.json", "events-1800-minute.json",
                                 "tables.json", "tables.md"])
        for n in names:
            with open(os.path.join(outs[0], n), "rb") as a, open(os.path.join(outs[1], n), "rb") as b:
                self.assertEqual(a.read(), b.read(), n)

    def test_outputs_match_the_functions(self):
        out = os.path.join(self.tmp, "match")
        self.assertEqual(self.main("--data", self.data, "--out", out)[0], 0)
        days = g.load_days(self.data, "2021-03-08", "2023-12-31")
        all_evts = []
        for anchor in ("0930", "1800"):
            for cadence in ("half_hour", "minute"):
                want = ms.events(days, anchor, cadence)
                self.assertTrue(want, (anchor, cadence))
                with open(os.path.join(out, "events-%s-%s.json" % (anchor, cadence))) as fh:
                    self.assertEqual(json.load(fh), want)
                all_evts += want
        cals = {a: ms.calendar(days, a) for a in ("0930", "1800")}
        with open(os.path.join(out, "tables.json")) as fh:
            self.assertEqual(json.load(fh), ms.tables(all_evts, calendars=cals))
        with open(os.path.join(out, "tables.md")) as fh:
            md = fh.read()
        # plain English for a reader who does not program: no code names
        for word in ("half_width", "full_width", "to_anchor", "opposite_band", "half_hour", "r_at_flat",
                     "pct_", "max_gap", "tight_excluded", "None", "null", "0930", "1800"):
            self.assertNotIn(word, md, word)
        self.assertEqual(md.count("\n## "), len(ms.STOPS))

    def test_start_mid_range_matches_full_run(self):
        # a run that starts mid-range warms its band up on the days before --start: the same events
        full, part = os.path.join(self.tmp, "full"), os.path.join(self.tmp, "part")
        start = date_of(17).isoformat()
        self.assertEqual(self.main("--data", self.data, "--out", full)[0], 0)
        self.assertEqual(self.main("--data", self.data, "--start", start, "--out", part)[0], 0)
        for anchor in ("0930", "1800"):
            for cadence in ("half_hour", "minute"):
                n = "events-%s-%s.json" % (anchor, cadence)
                with open(os.path.join(full, n)) as a, open(os.path.join(part, n)) as b:
                    want = [e for e in json.load(a) if e["date"] >= start]
                    got = json.load(b)
                self.assertTrue(got, n)
                self.assertEqual(got, want, n)
        with open(os.path.join(part, "tables.json")) as fh:
            rows = json.load(fh)
        r = [x for x in rows if x["anchor"] == "1800" and x["cadence"] == "minute" and x["stop"] == "to_anchor"
             and x["part"] == "afternoon" and x["side"] == "both"][0]
        self.assertLessEqual(r["max_gap_trading_days"], 24 - 17)


if __name__ == "__main__":
    unittest.main()
