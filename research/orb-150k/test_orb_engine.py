#!/usr/bin/env python3
"""Tests for orb_engine.py. Run: python3 -I -B research/orb-150k/test_orb_engine.py

Every test runs on small hand-built days (make_day), so each expected fill is worked out by hand here.

The day most tests use (STD): a 5-minute range 09:31..09:35 with open 100, high 111, low 95, close 110, so
"direction" goes long; the 09:36 bar opens at 111, so the entry is 111.5 (2 ticks against). The far-side
stop distance is floor(110 - 95) = 15.0, the loss at the stop is (15 + 0.5) * 2 + 1.90 = 32.90 a contract,
and on 150,000 at 0.1% (150 dollars) that is 4 contracts, planned cost 131.60, stop 96.5. Every other bar
is flat at the previous close, and the 16:00 bar has a range so the flat exit's 2 ticks are not cut off.
"""
import copy
import datetime as dt
import hashlib
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
NAV = os.path.join(os.path.dirname(HERE), "noise-area-variations")
sys.path.insert(0, HERE)
if NAV not in sys.path:
    sys.path.append(NAV)
import globex as g          # noqa: E402
import orb_engine as en     # noqa: E402

SM = g.sm_of
D = dt.date(2024, 3, 6)     # a Wednesday

BASE = {"name": "T", "reason": "test", "or_minutes": 5, "entry": "direction", "entry_until": None,
        "sides": "both", "stop": ["far_side"], "exit": ["hold_to_flat"], "max_or_atr": None, "risk_pct": 0.1}

RANGE = [("09:31", 100, 104, 95, 102), ("09:32", 102, 106, 101, 105), ("09:33", 105, 108, 104, 107),
         ("09:34", 107, 109, 106, 108), ("09:35", 108, 111, 107, 110)]
ENTRY = ("09:36", 111, 112, 110.5, 111.5)
CLOSE16 = ("16:00", 111.5, 112, 110, 111.5)
STD = RANGE + [ENTRY, CLOSE16]


def hhmm_of(sm):
    m = (sm + 18 * 60) % (24 * 60)
    return "%02d:%02d" % (m // 60, m % 60)


def stamp_of(date, sm):
    """Trading date + session minute -> the bar's end-of-minute stamp (evening minutes are the day before)."""
    m = sm + 18 * 60
    if m >= 24 * 60:
        return dt.datetime(date.year, date.month, date.day) + dt.timedelta(minutes=m - 24 * 60)
    return dt.datetime(date.year, date.month, date.day) - dt.timedelta(days=1) + dt.timedelta(minutes=m)


def stamp(date, hhmm):
    return stamp_of(date, SM(hhmm)).isoformat(" ")


def make_day(date, rows, first="09:31", last="16:00", base=100.0, drop=()):
    """One bar a minute from `first` to `last`, except the stamps in `drop`. rows: [(HH:MM, o, h, l, c)];
    every other minute is a flat bar at the previous bar's close (`base` before the first row)."""
    marks = {r[0]: r[1:] for r in rows}
    d = g.Day(date.isoformat())
    price = float(base)
    for sm in range(SM(first), SM(last) + 1):
        hm = hhmm_of(sm)
        o, h, l, c = marks.get(hm, (price, price, price, price))
        price = float(c)
        if hm in drop:
            continue
        d.by_sm[sm] = len(d.bars)
        d.bars.append(g.Bar(stamp_of(date, sm), sm, float(o), float(h), float(l), float(c), 10))
    return d


def weekdays(n, first=dt.date(2024, 1, 1)):
    out, x = [], first
    while len(out) < n:
        if x.weekday() < 5:
            out.append(x)
        x += dt.timedelta(days=1)
    return out


def settings(**over):
    s = copy.deepcopy(BASE)
    s.update(over)
    return s


def run(days, fill="kind", start=150000.0, fixed_qty=None, **over):
    return en.run(days, settings(**over), fill=fill, start=start, fixed_qty=fixed_qty)


def one(res):
    assert len(res["trades"]) == 1, res["trades"]
    return res["trades"][0]


def quiet_days(n, rng=20.0, first=dt.date(2024, 1, 1)):
    """n weekdays, each with a doji opening range (no trade) and a regular-hours range of `rng` points."""
    return [make_day(x, [("10:00", 100, 100 + rng, 100, 100)]) for x in weekdays(n, first)]


class Validate(unittest.TestCase):
    def test_validate_rejects_unknown_key_and_bad_values(self):
        en.validate(settings())
        en.validate(settings(entry="break", entry_until="11:00", sides="long", stop=["or_frac", 0.5],
                             exit=["target_r", 3], max_or_atr=1.5, risk_pct=5))
        en.validate(settings(or_minutes=30, entry="break", entry_until="15:58", stop=["atr_frac", 0.1],
                             exit=["trail_r", 2.0], risk_pct=0.01))
        bad = {
            "unknown key": dict(settings(), colour="red"),
            "missing key": {k: v for k, v in settings().items() if k != "sides"},
            "empty name": settings(name=""),
            "reason not a string": settings(reason=None),
            "or_minutes 10": settings(or_minutes=10),
            "or_minutes bool": settings(or_minutes=True),
            "or_minutes float": settings(or_minutes=5.0),
            "entry": settings(entry="fade"),
            "entry_until on direction": settings(entry_until="11:00"),
            "entry_until missing on break": settings(entry="break"),
            "entry_until inside the range": settings(entry="break", or_minutes=15, entry_until="09:45"),
            "entry_until 15:59": settings(entry="break", entry_until="15:59"),
            "entry_until format": settings(entry="break", entry_until="1100"),
            "entry_until in the break": settings(entry="break", entry_until="17:00"),
            "entry_until evening": settings(entry="break", entry_until="20:00"),
            "sides": settings(sides="up"),
            "stop kind": settings(stop=["atr"]),
            "stop not a list": settings(stop="far_side"),
            "far_side with value": settings(stop=["far_side", 1.0]),
            "or_frac without value": settings(stop=["or_frac"]),
            "or_frac 0": settings(stop=["or_frac", 0]),
            "atr_frac negative": settings(stop=["atr_frac", -0.1]),
            "atr_frac string": settings(stop=["atr_frac", "0.1"]),
            "exit kind": settings(exit=["target"]),
            "hold with value": settings(exit=["hold_to_flat", 1]),
            "target_r 0": settings(exit=["target_r", 0]),
            "trail_r without value": settings(exit=["trail_r"]),
            "max_or_atr 0": settings(max_or_atr=0),
            "max_or_atr string": settings(max_or_atr="1"),
            "risk_pct 0": settings(risk_pct=0),
            "risk_pct 5.01": settings(risk_pct=5.01),
            "risk_pct bool": settings(risk_pct=True),
        }
        for why, s in bad.items():
            with self.assertRaises(ValueError, msg=why):
                en.validate(s)
        with self.assertRaises(ValueError):
            en.run([], settings(), fill="harsh")
        with self.assertRaises(ValueError):
            en.run([], settings(), fixed_qty=0)


class Range(unittest.TestCase):
    def day(self, **kw):
        rows = [("09:31", 100, 101, 99, 100.5), ("09:33", 100.5, 103, 98, 102), ("09:35", 102, 102, 101, 101.75),
                ("09:40", 101.75, 106, 101, 104), ("09:45", 104, 104, 100, 103), ("09:50", 103, 103, 90, 95),
                ("10:00", 95, 97, 94, 96.25)]
        return make_day(D, rows, **kw)

    def test_opening_range_5_15_30(self):
        d = self.day()
        self.assertEqual(en.opening_range(d, 5), (100.0, 103.0, 98.0, 101.75))
        self.assertEqual(en.opening_range(d, 15), (100.0, 106.0, 98.0, 103.0))
        self.assertEqual(en.opening_range(d, 30), (100.0, 106.0, 90.0, 96.25))

    def test_opening_range_missing_bar_is_none(self):
        d = self.day(drop=("09:33",))
        for n in (5, 15, 30):
            self.assertIsNone(en.opening_range(d, n))
        d = self.day(drop=("09:50",))
        self.assertIsNotNone(en.opening_range(d, 5))
        self.assertIsNotNone(en.opening_range(d, 15))
        self.assertIsNone(en.opening_range(d, 30))
        # A day starting at 09:32 (no 09:31 bar) has no range.
        self.assertIsNone(en.opening_range(self.day(first="09:32"), 5))
        # Range bars after a data hole are not tradable: 08:00, then nothing until 09:31 (91 minutes).
        d = self.day(first="07:00", drop=tuple(hhmm_of(sm) for sm in range(SM("08:01"), SM("09:31"))))
        self.assertEqual(g.tradable_end(d), d.by_sm[SM("08:00")])
        self.assertIsNone(en.opening_range(d, 5))
        # The run takes no trade on a day whose range is incomplete, and it is no skip and no filter.
        res = run([make_day(D, STD, drop=("09:33",))])
        self.assertEqual((res["trades"], res["skipped"], res["filtered"]), ([], [], []))

    def test_atr14_needs_14_prior_days(self):
        ds = weekdays(16)
        days = [make_day(x, [("10:00", 100, 110 + k, 100, 100)]) for k, x in enumerate(ds)]
        # Overnight bars do not count: day 3 has a huge evening bar.
        days[3] = make_day(ds[3], [("20:00", 100, 500, 50, 100), ("10:00", 100, 113, 100, 100)], first="18:01")
        self.assertIsNone(en.atr14(days, 13))
        self.assertEqual(en.atr14(days, 14), sum(10 + k for k in range(14)) / 14.0)     # 16.5
        self.assertEqual(en.atr14(days, 15), sum(10 + k for k in range(1, 15)) / 14.0)  # 17.5
        # A prior day without a 09:31 bar is not one of the 14.
        days[5] = make_day(ds[5], [("10:00", 100, 115, 100, 100)], first="09:32")
        self.assertIsNone(en.atr14(days, 14))
        self.assertEqual(en.atr14(days, 15), (sum(10 + k for k in range(15)) - 15) / 14.0)


class Entry(unittest.TestCase):
    def test_direction_long_entry_fill_stop_and_size(self):
        t = one(run([make_day(D, STD)]))
        self.assertEqual((t["date"], t["side"], t["entry_dt"], t["entry"]), ("2024-03-06", "long", stamp(D, "09:36"), 111.5))
        self.assertEqual((t["dist"], t["stop_initial"], t["qty"], t["planned_cost"]), (15.0, 96.5, 4, 131.6))
        self.assertAlmostEqual(en.loss_per_contract(15.0), 32.90, places=9)
        # Held to the 15:59 bar, filled at the 16:00 open 111.5, 2 ticks against: 111.0.
        self.assertEqual((t["exit_dt"], t["exit"], t["reason"], t["gap"]), (stamp(D, "16:00"), 111.0, "flat", False))
        self.assertEqual(t["net"], -11.6)                     # (111.0 - 111.5) * 2 * 4 - 1.90 * 4
        self.assertEqual(t["balance"], 149988.4)

    def test_short_mirror(self):
        rows = [("09:31", 100, 104, 95, 98), ("09:35", 98, 100, 90, 92), ("09:36", 91.5, 92, 91, 91.5),
                ("16:00", 91.5, 92, 91, 91.5)]
        t = one(run([make_day(D, rows)]))
        # far side short: h - C = 104 - 92 = 12; entry 91.5 - 0.5 = 91.0; stop 103.0.
        self.assertEqual((t["side"], t["entry"], t["dist"], t["stop_initial"]), ("short", 91.0, 12.0, 103.0))
        self.assertEqual(t["qty"], 5)                         # 150 / 26.90 = 5.58
        self.assertEqual((t["exit"], t["reason"]), (92.0, "flat"))
        self.assertEqual(run([make_day(D, rows)], sides="long")["trades"], [])

    def test_doji_range_no_trade(self):
        rows = [("09:31", 100, 104, 95, 102), ("09:35", 102, 111, 99, 100)]
        res = run([make_day(D, rows + [ENTRY, CLOSE16])])
        self.assertEqual((res["trades"], res["skipped"], res["filtered"]), ([], [], []))
        self.assertEqual(len(res["days"]), 1)

    def test_break_waits_for_close_beyond(self):
        rows = RANGE[:4] + [("09:35", 108, 109, 107, 108), ("09:40", 108, 112, 107, 109),
                            ("09:45", 109, 112, 108, 110), ("09:46", 110.5, 111.5, 110, 111), CLOSE16]
        # h = 109: 09:40 goes through it but closes at 109 (not above); 09:45 closes at 110 above it.
        t = one(run([make_day(D, rows)], entry="break", entry_until="11:00"))
        self.assertEqual((t["side"], t["entry_dt"], t["entry"], t["dist"]), ("long", stamp(D, "09:46"), 111.0, 15.0))

    def test_break_respects_entry_until(self):
        def rows(hm):
            nxt = hhmm_of(SM(hm) + 1)
            return RANGE[:4] + [("09:35", 108, 109, 107, 108), (hm, 108, 111, 107, 110), (nxt, 110, 111, 110, 110.5),
                                CLOSE16]
        self.assertEqual(run([make_day(D, rows("11:01"))], entry="break", entry_until="11:00")["trades"], [])
        t = one(run([make_day(D, rows("11:00"))], entry="break", entry_until="11:00"))
        self.assertEqual(t["entry_dt"], stamp(D, "11:01"))
        t = one(run([make_day(D, rows("11:01"))], entry="break", entry_until="11:01"))
        self.assertEqual(t["entry_dt"], stamp(D, "11:02"))

    def test_break_ignores_disallowed_side_and_keeps_looking(self):
        rows = RANGE[:4] + [("09:35", 108, 109, 107, 108), ("09:40", 108, 108, 90, 94), ("09:41", 94, 95, 93, 94),
                            ("09:50", 94, 111, 94, 110), ("09:51", 110, 111, 110, 110.5), CLOSE16]
        t = one(run([make_day(D, rows)], entry="break", entry_until="11:00", sides="long"))
        self.assertEqual((t["side"], t["entry_dt"]), ("long", stamp(D, "09:51")))
        t = one(run([make_day(D, rows)], entry="break", entry_until="11:00"))
        self.assertEqual((t["side"], t["entry_dt"]), ("short", stamp(D, "09:41")))

    def test_no_entry_into_1559_or_the_last_tradable_bar(self):
        rows = RANGE[:4] + [("09:35", 108, 109, 107, 108), ("15:58", 108, 111, 107, 110), CLOSE16]
        res = run([make_day(D, rows)], entry="break", entry_until="15:58")
        self.assertEqual((res["trades"], res["skipped"]), ([], []))      # it would fill on the 15:59 bar
        rows = RANGE[:4] + [("09:35", 108, 109, 107, 108), ("12:58", 108, 111, 107, 110)]
        res = run([make_day(D, rows, last="12:59")], entry="break", entry_until="15:00")
        self.assertEqual((res["trades"], res["skipped"]), ([], []))      # 12:59 is the last tradable bar


class Size(unittest.TestCase):
    def test_stop_under_10_points_skipped(self):
        rows = [("09:31", 100, 104, 100.25, 102), ("09:35", 102, 111, 101, 110)]      # 110 - 100.25 = 9.75
        res = run([make_day(D, rows + [ENTRY, CLOSE16])])
        self.assertEqual(res["trades"], [])
        self.assertEqual([(x["date"], x["reason"]) for x in res["skipped"]], [("2024-03-06", "stop under 10 points")])

    def test_under_one_contract_skipped(self):
        res = run([make_day(D, STD)], start=3000.0, risk_pct=1.0)                     # 30 < 32.90
        self.assertEqual(res["trades"], [])
        self.assertEqual([(x["date"], x["reason"]) for x in res["skipped"]], [("2024-03-06", "under one contract")])
        t = one(run([make_day(D, STD)], start=3290.0, risk_pct=1.0))
        self.assertEqual(t["qty"], 1)

    def test_qty_capped_at_90(self):
        t = one(run([make_day(D, STD)], risk_pct=5.0))      # 7,500 / 32.90 = 227
        self.assertEqual((t["qty"], t["planned_cost"]), (90, 2961.0))

    def test_fixed_qty_ignores_balance(self):
        t = one(run([make_day(D, STD)], start=1000.0, risk_pct=1.0, fixed_qty=1))
        self.assertEqual((t["qty"], t["planned_cost"]), (1, 32.9))
        t = one(run([make_day(D, STD)], start=150000.0, risk_pct=5.0, fixed_qty=1))
        self.assertEqual(t["qty"], 1)
        res = run([make_day(D, [("09:31", 100, 104, 100.25, 102), ("09:35", 102, 111, 101, 110), ENTRY])],
                  fixed_qty=1)
        self.assertEqual([x["reason"] for x in res["skipped"]], ["stop under 10 points"])

    def test_or_frac_and_atr_frac_distances(self):
        t = one(run([make_day(D, STD)], stop=["or_frac", 0.7]))     # 0.7 * 16 = 11.2 -> 11.0
        self.assertEqual((t["dist"], t["stop_initial"]), (11.0, 100.5))
        days = quiet_days(14, rng=30.0) + [make_day(dt.date(2024, 1, 19), STD)]
        t = one(run(days, stop=["atr_frac", 0.45]))                 # 0.45 * 30 = 13.5
        self.assertEqual((t["date"], t["dist"]), ("2024-01-19", 13.5))
        # atr_frac on a day with no 14-day average: no trade, no skip, no filter.
        res = run([make_day(D, STD)], stop=["atr_frac", 0.45])
        self.assertEqual((res["trades"], res["skipped"], res["filtered"]), ([], [], []))


class Life(unittest.TestCase):
    GAP = ("10:00", 94, 95, 90, 92)      # opens below the 96.5 stop

    def test_gap_through_stop_midpoint_and_kind_and_harsh(self):
        day = make_day(D, STD + [self.GAP])
        want = {"kind": 93.5, "harsh-stops": 90.0, "midpoint": 92.0}   # 94 - 0.5; the low; (94 + 90) / 2
        for fill, px in want.items():
            t = one(run([day], fill=fill))
            self.assertEqual((t["reason"], t["exit_dt"], t["exit"], t["gap"]), ("stop", stamp(D, "10:00"), px, True), fill)
            self.assertEqual(t["net"], round((px - 111.5) * 8 - 7.6, 2))
            self.assertLess(t["net"], -t["planned_cost"])
        # Without a gap: kind at the stop 2 ticks against, the loss is the planned cost exactly.
        day = make_day(D, STD + [("10:00", 100, 101, 90, 92)])
        got = {f: one(run([day], fill=f))["exit"] for f in ("kind", "harsh-stops", "midpoint")}
        self.assertEqual(got, {"kind": 96.0, "harsh-stops": 90.0, "midpoint": 93.25})   # (96.5 + 90) / 2 = 93.25
        t = one(run([day], fill="kind"))
        self.assertEqual((t["net"], t["r"], t["gap"]), (-131.6, -1.0, False))
        # Midpoint off the grid goes to the worse tick: (96.5 + 90.25) / 2 = 93.375 -> 93.25.
        self.assertEqual(one(run([make_day(D, STD + [("10:00", 100, 101, 90.25, 92)])], fill="midpoint"))["exit"], 93.25)

    def test_target_needs_one_tick_through(self):
        # target_r 2: 111.5 + 2 * 15 = 141.5. 10:00 touches 141.5 exactly: no fill. 10:10 trades 141.75: filled at 141.5.
        rows = STD + [("10:00", 111.5, 141.5, 111.5, 120), ("10:10", 120, 141.75, 119, 140)]
        t = one(run([make_day(D, rows)], exit=["target_r", 2]))
        self.assertEqual((t["reason"], t["exit_dt"], t["exit"], t["gap"]), ("target", stamp(D, "10:10"), 141.5, False))
        self.assertEqual(t["net"], 232.4)
        self.assertAlmostEqual(t["r"], 232.4 / 131.6, places=12)
        # Rounded to the tick away from the entry: 1.01 * 15 = 15.15 -> 126.65 -> 126.75; it needs 127.0.
        rows = STD + [("10:00", 111.5, 126.75, 111.5, 120), ("10:10", 120, 127.0, 119, 125)]
        t = one(run([make_day(D, rows)], exit=["target_r", 1.01]))
        self.assertEqual((t["exit_dt"], t["exit"]), (stamp(D, "10:10"), 126.75))
        # Short: 91.0 - 2 * 12 = 67.0; needs 66.75.
        rows = [("09:31", 100, 104, 95, 98), ("09:35", 98, 100, 90, 92), ("09:36", 91.5, 92, 91, 91.5),
                ("10:00", 91, 91, 67, 70), ("10:05", 70, 70, 66.75, 68), ("16:00", 68, 69, 67, 68)]
        t = one(run([make_day(D, rows)], exit=["target_r", 2]))
        self.assertEqual((t["side"], t["exit_dt"], t["exit"], t["reason"]), ("short", stamp(D, "10:05"), 67.0, "target"))

    def test_stop_wins_same_bar_as_target(self):
        t = one(run([make_day(D, STD + [("10:00", 111.5, 142, 96, 100)])], exit=["target_r", 2]))
        self.assertEqual((t["reason"], t["exit"], t["net"]), ("stop", 96.0, -131.6))

    def test_target_can_fill_on_entry_bar(self):
        rows = RANGE + [("09:36", 111, 142, 110.5, 141), CLOSE16]
        t = one(run([make_day(D, rows)], exit=["target_r", 2]))
        self.assertEqual((t["reason"], t["entry_dt"], t["exit_dt"], t["exit"]),
                         ("target", stamp(D, "09:36"), stamp(D, "09:36"), 141.5))

    def test_trail_moves_only_toward_price_from_next_bar(self):
        # trail_r 1, dist 15. Entry bar high 112 -> stop 97 from 09:37. 09:40 makes 120 and dips to 104: the
        # stop is still 97 on that bar; at its close it moves to 105. 09:41 holds 106. 09:42 reaches 104: stopped
        # at 105, kind 104.5.
        rows = STD + [("09:40", 111.5, 120, 104, 118), ("09:41", 118, 118, 106, 107), ("09:42", 107, 108, 104, 105)]
        t = one(run([make_day(D, rows)], exit=["trail_r", 1]))
        self.assertEqual((t["reason"], t["exit_dt"], t["exit"], t["stop_initial"]), ("stop", stamp(D, "09:42"), 104.5, 96.5))
        self.assertEqual(t["net"], -63.6)
        # The stop rests at 97 (not 96.5) after the entry bar: a bar reaching 96.25 fills at 97 - 0.5.
        t = one(run([make_day(D, STD + [("10:00", 111.5, 111.5, 96.25, 100)])], exit=["trail_r", 1]))
        self.assertEqual((t["reason"], t["exit"]), ("stop", 96.5))
        # trail_r 2: 112 - 30 = 82, below the 96.5 stop: the stop does not move down.
        t = one(run([make_day(D, STD + [("10:00", 111.5, 111.5, 96, 100)])], exit=["trail_r", 2]))
        self.assertEqual((t["reason"], t["exit"]), ("stop", 96.0))
        # Short: entry 91.0, dist 12, entry bar low 91 -> stop 103; 10:00 low 80 -> stop 92; 10:01 high 92 stops.
        rows = [("09:31", 100, 104, 95, 98), ("09:35", 98, 100, 90, 92), ("09:36", 91.5, 92, 91, 91.5),
                ("10:00", 91, 91, 80, 85), ("10:01", 85, 92, 85, 90), ("16:00", 90, 91, 89, 90)]
        t = one(run([make_day(D, rows)], exit=["trail_r", 1]))
        self.assertEqual((t["side"], t["exit_dt"], t["exit"]), ("short", stamp(D, "10:01"), 92.0))   # min(92+0.5, high 92)

    def test_flat_at_1559_fills_1600_open(self):
        t = one(run([make_day(D, STD[:-1] + [("16:00", 113, 114, 112, 113.5)])]))
        self.assertEqual((t["exit_dt"], t["exit"], t["reason"], t["gap"]), (stamp(D, "16:00"), 112.5, "flat", False))
        # The 16:00 bar opens below the stop: the flat fill is at that open, 2 ticks against, gap true.
        t = one(run([make_day(D, STD[:-1] + [("16:00", 90, 91, 88, 89)])]))
        self.assertEqual((t["exit"], t["reason"], t["gap"]), (89.5, "flat", True))
        # A stop on the 15:59 bar comes before the flat.
        t = one(run([make_day(D, STD + [("15:59", 111.5, 111.5, 96, 97)])]))
        self.assertEqual((t["reason"], t["exit_dt"]), ("stop", stamp(D, "15:59")))

    def test_half_day_closes_at_last_bar(self):
        t = one(run([make_day(D, STD[:-1] + [("13:00", 111.5, 112, 110, 111)], last="13:00")]))
        self.assertEqual((t["exit_dt"], t["exit"], t["reason"]), (stamp(D, "13:00"), 110.5, "flat"))
        # A hole after 12:00 (nothing until 14:00): the day's trading ends at 12:00, closed at its close.
        drop = tuple(hhmm_of(sm) for sm in range(SM("12:01"), SM("14:00")))
        day = make_day(D, STD[:-1] + [("12:00", 111.5, 112, 110, 111.25), ("15:00", 50, 50, 50, 50)], drop=drop)
        t = one(run([day]))
        self.assertEqual((t["exit_dt"], t["exit"], t["reason"]), (stamp(D, "12:00"), 110.75, "flat"))
        self.assertEqual(len(run([day])["days"]), 1)


class Filter(unittest.TestCase):
    def test_max_or_atr_filters_wide_range(self):
        days = quiet_days(14, rng=20.0) + [make_day(dt.date(2024, 1, 19), STD)]    # range height 16, atr14 20
        res = run(days, max_or_atr=1.0)
        self.assertEqual([t["date"] for t in res["trades"]], ["2024-01-19"])
        # The first 14 days have complete ranges but no 14-day average: filtered.
        self.assertEqual(res["filtered"], [x.isoformat() for x in weekdays(14)])
        res = run(days, max_or_atr=0.75)                                              # 16 > 15
        self.assertEqual(res["trades"], [])
        self.assertEqual(res["filtered"][-1], "2024-01-19")
        self.assertEqual(len(res["filtered"]), 15)
        self.assertEqual(run(days, max_or_atr=0.8)["filtered"][-1], "2024-01-18")    # 16 is not above 16


class Money(unittest.TestCase):
    def test_day_low_marks_adverse_extreme(self):
        res = run([make_day(D, STD + [("10:00", 111.5, 112, 100, 111.5)])])
        t = one(res)
        self.assertEqual(t["exit"], 111.0)
        # 150000 + (100 - 111.5) * 2 * 4 - 7.60 = 149900.40 at the 10:00 low.
        self.assertEqual(res["days"], [{"date": "2024-03-06", "start": 150000.0, "end": 149988.4, "low": 149900.4}])
        # A stop: the low is the balance after the stop (the stop bar is not marked at its extreme).
        res = run([make_day(D, STD + [("10:00", 100, 101, 90, 92)])], fill="midpoint")
        self.assertEqual(res["days"][0]["low"], round(150000 + (93.25 - 111.5) * 8 - 7.6, 2))
        # A winning day: the low is the entry bar's low marked, (110.5 - 111.5) * 8 - 7.6 = -15.6.
        res = run([make_day(D, RANGE + [("09:36", 111, 142, 110.5, 141), CLOSE16])], exit=["target_r", 2])
        self.assertEqual(res["days"][0], {"date": "2024-03-06", "start": 150000.0, "end": 150232.4, "low": 149984.4})

    def test_net_r_balance_to_the_cent(self):
        d1, d2, d3 = weekdays(3, dt.date(2024, 3, 4))
        days = [make_day(d1, STD[:-1] + [("16:00", 113.75, 114, 113, 113.5)]),       # exit 113.25
                make_day(d2, RANGE + [ENTRY]),                                     # the 16:00 bar is flat at 111.5
                make_day(d3, STD + [("10:00", 100, 101, 90, 92)])]                  # stop, kind 96.0
        res = run(days, risk_pct=0.37)
        t1, t2, t3 = res["trades"]
        self.assertEqual((t1["qty"], t1["net"], t1["balance"]), (16, 25.6, 150025.6))   # 1.75 * 2 * 16 - 30.40
        self.assertAlmostEqual(t1["r"], 25.6 / round(16 * 32.9, 2), places=12)
        # Day 2: balance 150,025.60 -> 555.09 at risk -> 16; held, the 16:00 bar is flat at 111.5: exit 111.5.
        self.assertEqual((t2["qty"], t2["exit"], t2["net"], t2["balance"]), (16, 111.5, -30.4, 149995.2))
        self.assertEqual((t3["qty"], t3["net"], t3["balance"]), (16, -526.4, 149468.8))
        self.assertEqual(t3["r"], -1.0)
        self.assertEqual([(x["start"], x["end"]) for x in res["days"]],
                         [(150000.0, 150025.6), (150025.6, 149995.2), (149995.2, 149468.8)])

    def test_digest_repeats(self):
        days = quiet_days(14) + [make_day(dt.date(2024, 1, 19), STD + [("10:00", 100, 101, 90, 92)]),
                                 make_day(dt.date(2024, 1, 22), STD)]
        a = run(days, stop=["atr_frac", 0.6], fill="midpoint")
        b = run(days, stop=["atr_frac", 0.6], fill="midpoint")
        self.assertEqual(len(a["trades"]), 2)
        self.assertEqual(a["digest"], b["digest"])
        self.assertEqual(a["digest"], hashlib.sha256(json.dumps(a["trades"], sort_keys=True).encode()).hexdigest())
        self.assertNotEqual(a["digest"], run(days, stop=["atr_frac", 0.6], fill="kind")["digest"])
        self.assertEqual(set(a), {"settings", "fill", "start", "fixed_qty", "trades", "days", "skipped",
                                  "filtered", "digest"})


if __name__ == "__main__":
    unittest.main()
