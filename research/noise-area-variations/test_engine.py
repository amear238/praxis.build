#!/usr/bin/env python3
"""Tests for engine.py. Run: python3 -I -B research/noise-area-variations/test_engine.py

Most tests run on small hand-built days with a hand-set band (bands.day_bands is stood in for), so every
expected fill is worked out by hand in the test. The look-ahead and repeat tests use random-walk days with
the real band. One test reads the real data file and checks that the no-stop baseline settings give the
same trades as research/noise-area-stop/retest.py (Flat1559, session start 09:31, no stop, kind fills).

Hand-set band unless a test says otherwise: upper 99, lower 60, VWAP 80, anchor price 79, width 40, so the
half-width stop is 20 points; on 50,000 at 1% that is 42.90 a contract at the stop and 11 contracts.
"""
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
import sys
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import bands as bd        # noqa: E402
import engine as en       # noqa: E402
import globex as g        # noqa: E402
import test_bands as tb   # noqa: E402  (stamp_of, random_days, copy_day, trimmed_to_market)

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
D = dt.date(2024, 3, 6)          # a Wednesday trading day
SM = g.sm_of
STD = bd.BandPoint(99.0, 60.0, 80.0, 79.0, 40.0)

BASE = {"name": "T", "reason": "test", "anchor": "0930", "lookback": 14, "band_mult": 1.0,
        "cadence": "half_hour", "entry_window": ["09:31", "15:30"], "sides": "both", "reentry": "any",
        "stop": {"kind": "half_width"}, "exit": {"kind": "band_or_vwap"}, "max_trades_per_day": 3,
        "risk_pct": 1.0, "flat_time": "15:59"}

# The breakout used by most tests: the 10:00 bar closes at 100 (above 99), the 10:01 bar opens at 101.
UP = {"10:00": (80, 100, 80, 100), "10:01": (101, 102, 100.5, 101.5)}
# The same, with a 16:00 bar that has a range, so the flat exit's 2 ticks are not cut off by the bar's range
# (a fill is always kept inside its bar's range, as in retest.py).
UP_FLAT = dict(UP, **{"16:00": (101.5, 102, 100.5, 101.5)})


def hhmm_of(sm):
    m = (sm + 18 * 60) % (24 * 60)
    return "%02d:%02d" % (m // 60, m % 60)


def stamp(date, hhmm):
    return tb.stamp_of(date, SM(hhmm)).isoformat(" ")


def build_day(date, marks, first="09:31", last="16:00", base=80.0):
    """One bar a minute from `first` to `last`. marks: {'HH:MM': (o, h, l, c)}; every other minute is a flat
    bar at the previous bar's close (base before the first mark)."""
    d = g.Day(date.isoformat())
    price = float(base)
    for sm in range(SM(first), SM(last) + 1):
        o, h, l, c = marks.get(hhmm_of(sm), (price, price, price, price))
        d.by_sm[sm] = len(d.bars)
        d.bars.append(g.Bar(tb.stamp_of(date, sm), sm, float(o), float(h), float(l), float(c), 10))
        price = float(c)
    return d


def fake_bands(spec):
    """A stand-in for bands.day_bands: spec(date, sm) -> BandPoint or None, on bars at or after the anchor."""
    def day_bands(days, k, anchor, lookback=14, mult=1.0):
        d = days[k]
        out = {}
        for b in d.bars:
            if b.sm >= bd.ANCHORS[anchor]:
                p = spec(d.date, b.sm)
                if p is not None:
                    out[b.sm] = p
        return out
    return day_bands


def settings(**over):
    s = copy.deepcopy(BASE)
    s.update(over)
    return s


def run(days, fill="kind", start=50000.0, spec=None, **over):
    with mock.patch.object(bd, "day_bands", fake_bands(spec or (lambda date, sm: STD))):
        return en.run(days, settings(**over), fill=fill, start=start)


class Validate(unittest.TestCase):
    def test_accepts_and_returns(self):
        s = settings()
        self.assertIs(en.validate(s), s)
        en.validate(settings(stop={"kind": "width_frac", "value": 0.5}, exit={"kind": "trail_r", "value": 2.0},
                             anchor="1800", entry_window=["18:01", "02:00"], cadence="minute"))
        en.validate(settings(stop={"kind": "none"}), allow_no_stop=True)

    def test_validate_rejects(self):
        bad = {
            "unknown field": dict(settings(), colour="red"),
            "stop none without the flag": settings(stop={"kind": "none"}),
            "flat_time 16:00": settings(flat_time="16:00"),
            "risk_pct 3": settings(risk_pct=3),
            "window end after flat_time": settings(flat_time="15:00", entry_window=["09:31", "15:30"]),
            "missing field": {k: v for k, v in settings().items() if k != "sides"},
            "empty name": settings(name=""),
            "reason not a string": settings(reason=None),
            "lookback 4": settings(lookback=4),
            "lookback 61": settings(lookback=61),
            "lookback float": settings(lookback=14.0),
            "band_mult 0.2": settings(band_mult=0.2),
            "band_mult 4.5": settings(band_mult=4.5),
            "anchor": settings(anchor="0931"),
            "cadence": settings(cadence="hourly"),
            "sides": settings(sides="up"),
            "reentry": settings(reentry="never"),
            "stop kind": settings(stop={"kind": "atr"}),
            "width_frac without value": settings(stop={"kind": "width_frac"}),
            "width_frac 3.5": settings(stop={"kind": "width_frac", "value": 3.5}),
            "value on half_width": settings(stop={"kind": "half_width", "value": 1.0}),
            "exit kind": settings(exit={"kind": "target"}),
            "trail_r without value": settings(exit={"kind": "trail_r"}),
            "trail_r 0.4": settings(exit={"kind": "trail_r", "value": 0.4}),
            "max_trades 0": settings(max_trades_per_day=0),
            "max_trades 11": settings(max_trades_per_day=11),
            "risk_pct 0.05": settings(risk_pct=0.05),
            "flat_time in the break": settings(flat_time="17:00"),
            "flat_time format": settings(flat_time="3:59"),
            "window reversed": settings(entry_window=["15:30", "09:31"]),
            "window one stamp": settings(entry_window=["09:31"]),
            "window 18:00": settings(entry_window=["18:00", "02:00"]),
            "window across midnight reversed": settings(entry_window=["02:00", "18:01"]),
        }
        for why, s in bad.items():
            with self.assertRaises(ValueError, msg=why):
                en.validate(s)
        with self.assertRaises(ValueError):    # trail_r needs a stop distance
            en.validate(settings(stop={"kind": "none"}, exit={"kind": "trail_r", "value": 1.0}),
                        allow_no_stop=True)
        with self.assertRaises(ValueError):
            en.run([], settings(), fill="harsh")

    def test_error_names_the_field(self):
        with self.assertRaises(ValueError) as cm:
            en.validate(settings(risk_pct=3))
        self.assertIn("risk_pct", str(cm.exception))


class Fills(unittest.TestCase):
    def test_entry_fill_and_stop_offset(self):
        res = run([build_day(D, UP_FLAT)])
        self.assertEqual(len(res["trades"]), 1)
        t = res["trades"][0]
        self.assertEqual((t["side"], t["date"], t["entry_dt"]), ("long", "2024-03-06", stamp(D, "10:01")))
        self.assertEqual((t["entry"], t["dist"], t["stop_initial"]), (101.5, 20.0, 81.5))
        # Held above the band all day: flat on the 15:59 bar, filled at the 16:00 open, 2 ticks against.
        self.assertEqual((t["exit_dt"], t["exit"], t["reason"], t["gap"]), (stamp(D, "16:00"), 101.0, "flat", False))

    def test_size_and_planned_cost(self):
        self.assertAlmostEqual(en.loss_per_contract(20.0), 42.90, places=9)
        t = run([build_day(D, UP_FLAT)])["trades"][0]
        self.assertEqual((t["qty"], t["planned_cost"]), (11, 471.90))
        self.assertEqual(t["net"], -31.9)                    # (101.0 - 101.5) * 2 * 11 - 1.90 * 11
        self.assertAlmostEqual(t["r"], -31.9 / 471.9, places=12)
        self.assertEqual(t["balance"], 49968.1)

    def test_kind_stop_loss_equals_planned(self):
        day = build_day(D, dict(UP, **{"10:15": (101.5, 101.5, 70, 75)}))
        res = run([day])
        self.assertEqual(len(res["trades"]), 1)              # 75 is inside the band: nothing more
        t = res["trades"][0]
        self.assertEqual((t["reason"], t["exit_dt"], t["exit"], t["gap"]), ("stop", stamp(D, "10:15"), 81.0, False))
        self.assertEqual(t["net"], -t["planned_cost"])
        self.assertEqual(t["net"], -471.9)
        self.assertEqual(t["r"], -1.0)
        self.assertEqual(t["balance"], 49528.1)

    def test_gap_through_stop(self):
        day = build_day(D, dict(UP, **{"10:15": (76.5, 77, 70, 75)}))
        t = run([day])["trades"][0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("stop", 76.0, True))
        self.assertEqual(t["net"], -581.9)                   # (76.0 - 101.5) * 22 - 20.9
        self.assertLess(t["net"], -t["planned_cost"])

    def test_harsh_stop_fills_at_low(self):
        t = run([build_day(D, dict(UP, **{"10:15": (101.5, 101.5, 70, 75)}))], fill="harsh-stops")["trades"][0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("stop", 70.0, False))
        self.assertEqual(t["net"], -713.9)
        t = run([build_day(D, dict(UP, **{"10:15": (76.5, 77, 70, 75)}))], fill="harsh-stops")["trades"][0]
        self.assertEqual((t["exit"], t["gap"]), (70.0, True))
        # The harsh model is the default fill.
        with mock.patch.object(bd, "day_bands", fake_bands(lambda date, sm: STD)):
            res = en.run([build_day(D, dict(UP, **{"10:15": (101.5, 101.5, 70, 75)}))], settings())
        self.assertEqual((res["fill"], res["trades"][0]["exit"]), ("harsh-stops", 70.0))

    def test_short_mirror(self):
        marks = {"10:00": (80, 80, 50, 50), "10:01": (49, 49.5, 48, 48.5), "10:15": (48.5, 75, 48.5, 70)}
        t = run([build_day(D, marks)])["trades"]
        self.assertEqual(len(t), 1)
        t = t[0]
        self.assertEqual((t["side"], t["entry"], t["stop_initial"], t["qty"]), ("short", 48.5, 68.5, 11))
        self.assertEqual((t["reason"], t["exit"], t["net"], t["r"]), ("stop", 69.0, -471.9, -1.0))

    def test_stop_distances(self):
        p = STD
        f = en.stop_distance
        self.assertEqual(f("half_width", None, 1, 100.3, p), 20.0)
        self.assertEqual(f("full_width", None, 1, 100.3, p), 40.0)
        self.assertEqual(f("width_frac", 0.33, 1, 100.3, p), 13.0)       # 13.2 rounded down to a tick
        self.assertEqual(f("to_anchor", None, 1, 100.3, p), 21.25)       # 100.3 - 79
        self.assertEqual(f("opposite_band", None, 1, 100.3, p), 40.25)   # 100.3 - 60
        self.assertEqual(f("to_anchor", None, -1, 55.1, p), 23.75)       # 79 - 55.1
        self.assertEqual(f("opposite_band", None, -1, 55.1, p), 43.75)   # 99 - 55.1
        self.assertEqual(f("to_anchor", None, -1, 85.0, p), -6.0)
        self.assertEqual(f("width_frac", 1.1, 1, 0.0, bd.BandPoint(0, 0, 0, 0, 20.0)), 22.0)


class Rules(unittest.TestCase):
    def test_skips(self):
        later = {"10:31": (101, 102, 100.5, 101.5)}
        day = build_day(D, dict(UP, **later))
        narrow = bd.BandPoint(99.0, 60.0, 80.0, 79.0, 16.0)
        res = run([day], max_trades_per_day=1, spec=lambda date, sm: narrow if sm == SM("10:00") else STD)
        self.assertEqual(res["skipped"], [{"date": "2024-03-06", "decision_dt": stamp(D, "10:00"), "side": "long",
                                           "reason": "stop under 10 points"}])
        self.assertEqual([t["entry_dt"] for t in res["trades"]], [stamp(D, "10:31")])
        # 3,000 at 1% is 30: a 20-point stop (42.90) is under one contract, a 10-point stop (22.90) is one.
        half = bd.BandPoint(99.0, 60.0, 80.0, 79.0, 20.0)
        res = run([day], start=3000.0, max_trades_per_day=1,
                  spec=lambda date, sm: STD if sm == SM("10:00") else half)
        self.assertEqual(res["skipped"], [{"date": "2024-03-06", "decision_dt": stamp(D, "10:00"), "side": "long",
                                           "reason": "under one contract"}])
        self.assertEqual([(t["entry_dt"], t["qty"], t["dist"]) for t in res["trades"]],
                         [(stamp(D, "10:31"), 1, 10.0)])

    def test_half_day_flat_at_last_bar(self):
        day = build_day(D, dict(UP, **{"13:00": (101.5, 102, 100, 100.5)}), last="13:00")
        t = run([day])["trades"]
        self.assertEqual(len(t), 1)
        self.assertEqual((t[0]["exit_dt"], t[0]["exit"], t[0]["reason"]), (stamp(D, "13:00"), 100.0, "flat"))

    def test_window_across_midnight(self):
        kw = dict(anchor="1800", entry_window=["18:01", "02:00"])

        def up_at(hhmm):
            sm = SM(hhmm)
            return {hhmm: (80, 100, 80, 100), hhmm_of(sm + 1): (101, 102, 100.5, 101.5)}

        t = run([build_day(D, up_at("23:30"), first="18:01")], **kw)["trades"]
        self.assertEqual([(x["date"], x["entry_dt"]) for x in t], [("2024-03-06", "2024-03-05 23:31:00")])
        t = run([build_day(D, up_at("01:30"), first="18:01")], **kw)["trades"]
        self.assertEqual([(x["date"], x["entry_dt"]) for x in t], [("2024-03-06", "2024-03-06 01:31:00")])
        # Above the band from 02:01 on: the 02:30 decision bar is outside the window, as is every later one.
        day = build_day(D, up_at("02:01"), first="18:01")
        self.assertEqual(run([day], **kw)["trades"], [])
        t = run([day], **dict(kw, entry_window=["18:01", "03:00"]))["trades"]
        self.assertEqual([x["entry_dt"] for x in t], ["2024-03-06 02:31:00"])

    def test_max_trades_per_day(self):
        up = (101, 102, 100.5, 101.5)
        marks = {"10:00": (80, 100, 80, 100), "10:01": up, "10:30": (101.5, 101.5, 95, 95), "10:31": (95, 96, 94, 95),
                 "11:00": (95, 100, 95, 100), "11:01": up, "11:30": (101.5, 101.5, 95, 95), "11:31": (95, 96, 94, 95),
                 "12:00": (95, 100, 95, 100), "12:01": up}
        day = build_day(D, marks)
        t = run([day], max_trades_per_day=2)["trades"]
        self.assertEqual([x["entry_dt"] for x in t], [stamp(D, "10:01"), stamp(D, "11:01")])
        self.assertEqual([x["reason"] for x in t], ["exit", "exit"])
        self.assertEqual(t[0]["exit"], 94.5)
        t = run([day], max_trades_per_day=3)["trades"]
        self.assertEqual(len(t), 3)
        # The count is per trading day: the same day again the next day trades twice more.
        d2 = build_day(D + dt.timedelta(days=1), marks)
        self.assertEqual(len(run([day, d2], max_trades_per_day=2)["trades"]), 4)

    def test_fresh_reentry(self):
        marks = dict(UP, **{"10:15": (101.5, 102, 81, 100), "10:31": (101, 102, 100.5, 101.5),
                            "11:00": (101.5, 101.5, 95, 95), "11:30": (95, 100, 95, 100),
                            "11:31": (101, 102, 100.5, 101.5)})
        day = build_day(D, marks)
        t_any = run([day], reentry="any")["trades"]
        self.assertEqual([x["entry_dt"] for x in t_any], [stamp(D, "10:01"), stamp(D, "10:31"), stamp(D, "11:31")])
        self.assertEqual(t_any[0]["reason"], "stop")
        # fresh: the 10:30 close is still above the band after the stop; the 11:00 close inside frees it.
        t_fresh = run([day], reentry="fresh")["trades"]
        self.assertEqual([x["entry_dt"] for x in t_fresh], [stamp(D, "10:01"), stamp(D, "11:31")])

    def test_trail_r_only_tightens(self):
        marks = dict(UP, **{"10:05": (101.5, 120, 101.5, 119), "10:06": (119, 119, 104, 105),
                            "10:07": (105, 105, 97, 100)})
        day = build_day(D, marks)
        # value 1: stop 81.5 -> 82 (entry bar high 102) -> 100 (high 120); the 10:06 high of 119 does not
        # loosen it to 99. Fires at 10:07: kind fill at the stop 100, 2 ticks against.
        t = run([day], exit={"kind": "trail_r", "value": 1.0}, max_trades_per_day=1)["trades"]
        self.assertEqual((t[0]["reason"], t[0]["exit_dt"], t[0]["exit"], t[0]["stop_initial"]),
                         ("stop", stamp(D, "10:07"), 99.5, 81.5))
        # value 1.1: 120 - 22 = 98.0 (on the tick grid despite the float product); hit by the 97 low.
        t = run([day], exit={"kind": "trail_r", "value": 1.1}, max_trades_per_day=1)["trades"]
        self.assertEqual((t[0]["exit_dt"], t[0]["exit"]), (stamp(D, "10:07"), 97.5))
        # value 3: 120 - 60 = 60 is below the initial stop, which stays; no band exit; flat at 16:00.
        t = run([day], exit={"kind": "trail_r", "value": 3.0}, max_trades_per_day=1)["trades"]
        self.assertEqual((t[0]["reason"], t[0]["exit_dt"]), ("flat", stamp(D, "16:00")))
        # The trail moves at the entry bar's close (high 102 -> stop 82.0), so a low of exactly 82 on the next
        # bar fires it (82.0 less 2 ticks is cut to the bar's low, 82.0); the initial 81.5 would not have fired.
        m2 = dict(UP, **{"10:02": (101.5, 101.5, 82, 90)})
        t = run([build_day(D, m2)], exit={"kind": "trail_r", "value": 1.0}, max_trades_per_day=1)["trades"]
        self.assertEqual((t[0]["reason"], t[0]["exit_dt"], t[0]["exit"]), ("stop", stamp(D, "10:02"), 82.0))
        t = run([build_day(D, m2)], max_trades_per_day=1)["trades"]
        self.assertEqual(t[0]["reason"], "exit")              # no trail: 90 <= 99 at 10:30, not stopped

    def test_hold_to_flat_ignores_band_exit(self):
        day = build_day(D, dict(UP, **{"10:30": (101.5, 101.5, 95, 95)}))
        self.assertEqual(run([day])["trades"][0]["reason"], "exit")
        t = run([day], exit={"kind": "hold_to_flat"})["trades"]
        self.assertEqual([(x["reason"], x["exit_dt"], x["exit"]) for x in t], [("flat", stamp(D, "16:00"), 95.0)])

    def test_reverse(self):
        wide = {"kind": "width_frac", "value": 2.0}       # 80 points: the drop to 55 does not reach the stop
        day = build_day(D, dict(UP, **{"11:00": (95, 95, 55, 55), "11:01": (55, 56, 54, 55)}))
        t = run([day], stop=wide, exit={"kind": "hold_to_flat"})["trades"]
        self.assertEqual([(x["side"], x["reason"], x["exit_dt"], x["exit"]) for x in t],
                         [("long", "reverse", stamp(D, "11:01"), 54.5), ("short", "flat", stamp(D, "16:00"), 55.0)])
        self.assertEqual((t[0]["qty"], t[1]["entry"], t[1]["stop_initial"]), (3, 54.5, 134.5))
        # The long's size and the short's both come from the realised balance at the decision bar.
        self.assertEqual(t[1]["qty"], 3)
        # band_or_vwap: the same close also meets the exit rule, so the reason is "exit".
        t = run([day], stop=wide)["trades"]
        self.assertEqual([(x["side"], x["reason"]) for x in t], [("long", "exit"), ("short", "flat")])
        # The opposite signal closes the long even when the short is refused (window ended at 10:30).
        t = run([day], stop=wide, exit={"kind": "hold_to_flat"}, entry_window=["09:31", "10:30"])["trades"]
        self.assertEqual([(x["side"], x["reason"]) for x in t], [("long", "reverse")])
        # sides "long": there is no opposite signal, the long is held to the flat.
        t = run([day], stop=wide, exit={"kind": "hold_to_flat"}, sides="long")["trades"]
        self.assertEqual([(x["side"], x["reason"]) for x in t], [("long", "flat")])
        # sides "short": the 10:00 breakout up is not taken, the 11:00 one down is.
        t = run([day], stop=wide, sides="short")["trades"]
        self.assertEqual([(x["side"], x["entry_dt"]) for x in t], [("short", stamp(D, "11:01"))])

    def test_stop_bar_does_nothing_else(self):
        # 10:30 is a decision bar that hits the stop and closes below the lower band: the stop fills, and
        # there is no short entry at 10:31.
        day = build_day(D, dict(UP, **{"10:30": (101, 101, 50, 55)}))
        res = run([day])
        self.assertEqual([(x["side"], x["reason"], x["exit_dt"], x["entry_dt"]) for x in res["trades"]],
                         [("long", "stop", stamp(D, "10:30"), stamp(D, "10:01")),
                          ("short", "flat", stamp(D, "16:00"), stamp(D, "11:01"))])   # 11:00 (still 55) shorts
        self.assertEqual(res["skipped"], [])

    def test_data_hole_ends_the_day(self):
        # No bars from 11:01 to 13:59 (a three-hour hole): the long open since 10:01 is closed at the 11:00
        # bar's close, 2 ticks against; the breakout at 14:00 after the hole makes no trade.
        marks = dict(UP, **{"11:00": (101.5, 102, 101, 101.5), "14:00": (80, 100, 80, 100),
                            "14:01": (101, 102, 100.5, 101.5)})
        day = build_day(D, marks)
        holed = g.Day(day.date)
        for b in day.bars:
            if not (SM("11:01") <= b.sm <= SM("13:59")):
                holed.by_sm[b.sm] = len(holed.bars)
                holed.bars.append(b)
        self.assertEqual(g.tradable_end(holed), holed.by_sm[SM("11:00")])
        res = run([holed])
        self.assertEqual([(x["entry_dt"], x["exit_dt"], x["exit"], x["reason"]) for x in res["trades"]],
                         [(stamp(D, "10:01"), stamp(D, "11:00"), 101.0, "flat")])
        self.assertEqual(res["skipped"], [])
        self.assertEqual(len(res["days"]), 1)
        # Bars 10:31 to 11:29 missing: 10:30 to 11:30 is a 60-minute step, not more, so the day goes on: the
        # long is still open after 11:00 and is stopped by the 14:00 bar's low of 80; the 14:30 close above the
        # band then goes long again, flat at 16:00.
        gap60 = g.Day(day.date)
        for b in day.bars:
            if not (SM("10:31") <= b.sm <= SM("11:29")):
                gap60.by_sm[b.sm] = len(gap60.bars)
                gap60.bars.append(b)
        self.assertEqual(g.tradable_end(gap60), len(gap60.bars) - 1)
        t = run([gap60])["trades"]
        self.assertEqual([(x["entry_dt"], x["exit_dt"], x["reason"]) for x in t],
                         [(stamp(D, "10:01"), stamp(D, "14:00"), "stop"), (stamp(D, "14:31"), stamp(D, "16:00"), "flat")])

    def test_day_low_marks_adverse_extreme(self):
        day1 = build_day(D, dict(UP_FLAT, **{"10:10": (101.5, 101.5, 90, 101.5)}))
        day2 = build_day(D + dt.timedelta(days=1), {})
        res = run([day1, day2])
        self.assertEqual(res["days"], [
            {"date": "2024-03-06", "start": 50000.0, "end": 49968.1, "low": 49726.1},   # 50000 + (90-101.5)*22 - 20.9
            {"date": "2024-03-07", "start": 49968.1, "end": 49968.1, "low": 49968.1}])


def random_settings():
    return [
        settings(cadence="minute", max_trades_per_day=10),
        settings(anchor="1800", entry_window=["18:01", "15:00"], exit={"kind": "trail_r", "value": 1.0},
                 reentry="fresh", stop={"kind": "to_anchor"}),
        settings(anchor="1800", cadence="minute", entry_window=["20:00", "12:00"], stop={"kind": "full_width"},
                 exit={"kind": "hold_to_flat"}, sides="short", max_trades_per_day=5),
        settings(cadence="minute", stop={"kind": "opposite_band"}, reentry="fresh", max_trades_per_day=10),
    ]


class Random(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.days = tb.random_days(22, seed=20211117)

    def test_no_lookahead(self):
        k = 18
        B = self.days[k].bars[self.days[k].by_sm[SM("12:00")]]
        cut = B.dt.isoformat(" ")
        changed = (self.days[:k] + [tb.copy_day(self.days[k], change_after=B.sm, factor=1.37)]
                   + [tb.copy_day(d, factor=1.37) for d in self.days[k + 1:]])
        for s in random_settings():
            for fill in ("kind", "harsh-stops"):
                a = en.run(self.days, s, fill=fill)
                b = en.run(changed, s, fill=fill)
                before = [t for t in a["trades"] if t["exit_dt"] <= cut]
                self.assertGreaterEqual(len(before), 3, s)
                self.assertEqual([t for t in b["trades"] if t["exit_dt"] <= cut], before, (s["stop"], fill))
                self.assertEqual([x for x in b["skipped"] if x["decision_dt"] <= cut],
                                 [x for x in a["skipped"] if x["decision_dt"] <= cut])
                self.assertEqual(b["days"][:k], a["days"][:k])
                self.assertNotEqual(b["trades"], a["trades"])    # the change after B is seen

    def test_same_twice(self):
        for s in random_settings():
            a = en.run(self.days, s)
            b = en.run(self.days, copy.deepcopy(s))
            self.assertTrue(a["trades"])
            self.assertEqual(a["digest"], b["digest"])
            self.assertEqual(a, b)
            want = hashlib.sha256(json.dumps(a["trades"], sort_keys=True).encode()).hexdigest()
            self.assertEqual(a["digest"], want)
            self.assertEqual(len(a["days"]), len(self.days))

    def test_rules_hold_on_random_days(self):
        """Every trade on the random days obeys the size, stop and flat rules."""
        for s in random_settings():
            for fill in ("kind", "harsh-stops"):
                res = en.run(self.days, s, fill=fill)
                bal = 50000.0
                for t in res["trades"]:
                    lpc = en.loss_per_contract(t["dist"])
                    self.assertGreaterEqual(t["dist"], 10.0)
                    self.assertEqual(t["qty"], int(bal * s["risk_pct"] / 100.0 / lpc + 1e-9))
                    self.assertAlmostEqual(t["planned_cost"], t["qty"] * lpc, places=6)
                    sign = 1 if t["side"] == "long" else -1
                    self.assertEqual(t["stop_initial"], t["entry"] - sign * t["dist"])
                    self.assertLessEqual(SM(t["exit_dt"][11:16]), SM("16:00"))
                    self.assertLess(SM(t["entry_dt"][11:16]), SM(s["flat_time"]) + 1)
                    if fill == "kind" and t["reason"] == "stop" and not t["gap"]:
                        self.assertGreaterEqual(t["net"], -t["planned_cost"] - 0.011)
                    bal = round(bal + t["net"], 2)
                    self.assertEqual(t["balance"], bal)
                self.assertEqual(res["days"][-1]["end"], bal)


def _load_retest():
    path = os.path.join(REPO, "research", "noise-area-stop", "retest.py")
    spec = importlib.util.spec_from_file_location("retest_for_engine_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@unittest.skipUnless(os.path.exists(DATA), "data file absent")
class Baseline(unittest.TestCase):
    def test_baseline_matches_retest(self):
        rt = _load_retest()
        market = rt.mk.load_market(DATA, session_start="09:31")
        want = [(t["side"].lower(), t["entry_dt"], t["entry"], t["exit_dt"], t["exit"])
                for t in rt.Sim(policy="Flat1559", risk_pct=None, model="kind").run(market).trades]
        days = tb.trimmed_to_market(g.load_days(DATA), market)
        s = settings(stop={"kind": "none"}, exit={"kind": "band_or_vwap"}, sides="both", reentry="any",
                     max_trades_per_day=10, flat_time="15:59", entry_window=["09:31", "15:30"],
                     anchor="0930", cadence="half_hour", lookback=14, band_mult=1.0)
        res = en.run(days, s, fill="kind", allow_no_stop=True)
        got = [(t["side"], t["entry_dt"], t["entry"], t["exit_dt"], t["exit"]) for t in res["trades"]]
        self.assertGreater(len(want), 1000)
        self.assertEqual(got, want)
        for t in res["trades"]:
            self.assertEqual((t["qty"], t["stop_initial"], t["dist"], t["planned_cost"], t["r"]),
                             (1, None, None, None, None))
        self.assertEqual(len(res["days"]), len(days))


if __name__ == "__main__":
    unittest.main()
