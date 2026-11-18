#!/usr/bin/env python3
"""Tests for rule_check.py, the independent replay of candidate 1 of the levels plan (PLAN.md, "Candidate 1: fade
the first touch of a marked level. The exact rule"). Every expected level and trade below was worked out by hand
from the written rule; the working is in the comments. Each rule gets the right engine output, which must pass
clean, and a deliberately wrong one, which must be caught.

Unless a test says otherwise: tick 1, $10 a point, $2 commission, 1 tick slippage, market NQ (round-number step
100). Every daily bar has a range of 10, so ATR = 10. With k = 0.2, d = 2 and the 2 x ATR band is 20: a level
is armed when it lies more than 2 and at most 20 from P0.

Run: python3 -I -B test_rule_check.py (from this folder)."""
import copy
import os
import random
import sys
import unittest
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.append(os.path.normpath(os.path.join(HERE, "..", "trend-150k")))
from mdata import Adj, Bar, Roll  # noqa: E402
import rule_check as rc  # noqa: E402

NY = ZoneInfo("America/New_York")
NS = 1_000_000_000
DAY = 86400 * NS
EPOCH = date(1970, 1, 1).toordinal()


def ts(ny):
    """UTC ns of a New York wall-clock time 'YYYY-MM-DD HH:MM'."""
    return int(datetime.strptime(ny, "%Y-%m-%d %H:%M").replace(tzinfo=NY).timestamp()) * NS


def uts(utc):
    return int(datetime.strptime(utc, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp()) * NS


def m(ny, o, h, l, c, iid=1, v=1):
    return Bar(ts(ny), iid, float(o), float(h), float(l), float(c), v)


def mu(utc, o, h, l, c, iid=1, v=1):
    return Bar(uts(utc), iid, float(o), float(h), float(l), float(c), v)


def dn(iso):
    return date.fromisoformat(iso).toordinal() - EPOCH


def daily(first="2024-01-01", last="2024-12-31", lo=95.0, hi=105.0):
    return [Adj(Bar(d * DAY, 1, (lo + hi) / 2, hi, lo, (lo + hi) / 2, 1), (lo + hi) / 2, hi, lo, (lo + hi) / 2)
            for d in range(dn(first), dn(last) + 1)]


DAILY = daily()
SPEC = {"pv": 10.0, "tick": 1.0, "comm": 2.0, "slip_ticks": 1, "max_qty": 90}


def st(kind, k=0.2, target=None):
    return {"name": f"{kind} k{k} T{target}", "kind": kind, "k": k, "target": target, "atr_days": 14}


def arm(kind, side, level, stop):
    return {"kind": kind, "side": side, "level": float(level), "stop": float(stop)}


def trade(day, kind, side, level, stop, dist, target, entry_at, exit_at, exit_, reason, worst, gap=False,
          market="NQ"):
    return {"market": market, "date": day, "kind": kind, "level": float(level), "side": side,
            "entry_ts": ts(f"{day} {entry_at}"), "entry": float(level), "stop": float(stop), "dist": float(dist),
            "target": None if target is None else float(target), "exit_ts": ts(f"{day} {exit_at}"),
            "exit": float(exit_), "reason": reason, "gap": gap, "points": float((exit_ - level) * side),
            "worst": float(worst)}


def got(trades=(), armed=None):
    return {"trades": [dict(t) for t in trades], "armed": copy.deepcopy(armed or {})}


class Case(unittest.TestCase):
    market, spec, daily_, fill = "NQ", SPEC, DAILY, "midpoint"

    def breaks(self, g, minutes, settings, rolls=(), fill=None, market=None, spec=None, daily_=None):
        return rc.check_market(g, minutes, self.daily_ if daily_ is None else daily_, list(rolls),
                               spec or self.spec, settings, fill or self.fill, market or self.market)

    def clean(self, g, *a, **k):
        self.assertEqual(self.breaks(g, *a, **k), [])

    def caught(self, g, word, *a, **k):
        b = self.breaks(g, *a, **k)
        self.assertTrue(b, "expected a break")
        self.assertTrue(any(word in x for x in b), f"no break mentions {word!r}: {b}")


# A common prior day: S(2024-03-04) has one minute, high 110 and low 90, so on 03-05 (P0 100) PD arms a long at
# 90 (stop 88) and a short at 110 (stop 112). Every entry/exit test below starts from it.
PRIOR = [m("2024-03-04 10:00", 100, 110, 90, 100), m("2024-03-05 09:30", 100, 101, 99, 100)]
PD_ARMED = {"2024-03-05": [arm("PD", 1, 90, 88), arm("PD", -1, 110, 112)]}


def day5(*rows):
    """PRIOR plus 2024-03-05 minutes given as (HH:MM, o, h, l, c)."""
    return PRIOR + [m(f"2024-03-05 {t}", o, h, l, c) for t, o, h, l, c in rows]


# ---------------------------------------------------------------------------------------------- the basic case
# P1. PD, k 0.2, T 3. 10:00 low 89 = 90 - 1 tick: the long fills at 90, stop 88, target 90 + 3 x 2 = 96 (not
# checked on the entry minute). 10:01: low 90 is above the stop; high 97 = 96 + 1 tick: target at 96.
# worst = the lowest low held (89) - 90 = -1. points 6.
P1 = day5(("10:00", 100, 100, 89, 90), ("10:01", 90, 97, 90, 96), ("16:00", 96, 96, 96, 96))
P1_SET = st("PD", 0.2, 3)


def p1():
    return got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -1)], PD_ARMED)


class BasicTests(Case):
    def test_right_output_passes(self):
        self.clean(p1(), P1, P1_SET)

    def test_wrong_exit_price(self):
        g = p1()
        g["trades"][0]["exit"] = 95.0
        self.caught(g, "exit", P1, P1_SET)

    def test_missing_trade(self):
        g = p1()
        g["trades"] = []
        self.caught(g, "missing", P1, P1_SET)

    def test_extra_trade(self):
        g = p1()
        g["trades"].append(trade("2024-03-05", "PD", -1, 110, 112, 2, 104, "10:05", "10:06", 104, "target", -1))
        self.caught(g, "extra", P1, P1_SET)

    def test_each_differing_field_is_its_own_break(self):
        g = p1()
        g["trades"][0]["target"] = None
        g["trades"][0]["worst"] = 0.0
        g["trades"][0]["kind"] = "ON"
        b = self.breaks(g, P1, P1_SET)
        self.assertEqual(len(b), 3, b)
        for word in ("target", "worst", "kind"):
            self.assertTrue(any(f": {word} is" in x for x in b), b)

    def test_wrong_armed_set(self):
        g = p1()
        g["armed"]["2024-03-05"] = g["armed"]["2024-03-05"][:1]
        self.caught(g, "armed level PD short at 110 stop 112 missing", P1, P1_SET)
        g = p1()
        g["armed"]["2024-03-04"] = [arm("PD", 1, 90, 88)]
        self.caught(g, "extra", P1, P1_SET)

    def test_float_noise_is_not_a_break_but_a_millionth_of_a_tick_more_is(self):
        g = p1()
        g["trades"][0]["exit"] = 96.0 + 1e-9
        g["armed"]["2024-03-05"][0]["stop"] = 88.0 - 1e-9
        self.clean(g, P1, P1_SET)
        g["trades"][0]["exit"] = 96.0 + 2e-6
        self.caught(g, "exit", P1, P1_SET)

    def test_unknown_fill_is_refused(self):
        self.assertTrue(self.breaks(p1(), P1, P1_SET, fill="soft"))


# ---------------------------------------------------------------------------------------------- the clock
class ClockTests(Case):
    def test_session_date_is_new_york_clock_plus_seven_hours(self):
        sd = rc.session_date
        self.assertEqual(sd(ts("2024-03-04 16:59")), "2024-03-04")
        self.assertEqual(sd(ts("2024-03-04 17:00")), "2024-03-05")
        self.assertEqual(sd(ts("2024-03-03 18:00")), "2024-03-04")        # Sunday evening is Monday's session
        self.assertEqual(sd(uts("2024-03-10 21:30")), "2024-03-11")       # 17:30 EDT, the day clocks go forward
        self.assertEqual(sd(uts("2024-03-03 21:30")), "2024-03-03")       # 16:30 EST
        self.assertEqual(sd(uts("2024-11-03 21:30")), "2024-11-03")       # 16:30 EST, the day clocks go back
        self.assertEqual(sd(uts("2024-11-02 21:30")), "2024-11-03")       # 17:30 EDT

    def test_prepared_sessions_agree_with_the_definition_across_both_changes(self):
        mins = []
        for first in ("2024-03-07 00:00", "2024-10-31 00:00"):
            t = uts(first)
            for _ in range(6 * 72):                                       # every 20 minutes for six days
                mins.append(Bar(t, 1, 100.0, 100.0, 100.0, 100.0, 1))
                t += 20 * 60 * NS
        p = rc._Prep(mins, [], [], SPEC, "NQ")
        seen = 0
        for D, (s0, s1) in p.sess.items():
            for i in range(s0, s1):
                self.assertEqual(rc.session_date(mins[i].ts), rc._iso(D))
            seen += s1 - s0
        self.assertEqual(seen, len(mins))
        for D, (s0, s1, i900, i930, i1500, i1555) in p.tinfo.items():
            self.assertEqual(datetime.fromtimestamp(mins[i930].ts // NS, NY).strftime("%H:%M"), "09:40")

    # ON from the previous evening. 16:30 on 03-04 is S(03-04); 18:00 on 03-04 is S(03-05).
    # ON(03-05) = 18:00 (high 112) and 09:00 (low 92): a short at 112 (stop 114) and a long at 92 (stop 90).
    CLK = [m("2024-03-04 10:00", 100, 101, 99, 100), m("2024-03-04 16:30", 100, 115, 100, 100),
           m("2024-03-04 18:00", 100, 112, 100, 100), m("2024-03-05 09:00", 100, 100, 92, 100),
           m("2024-03-05 09:30", 100, 100, 100, 100), m("2024-03-05 16:00", 100, 100, 100, 100)]

    def test_overnight_runs_from_the_previous_evening(self):
        right = {"2024-03-05": [arm("ON", -1, 112, 114), arm("ON", 1, 92, 90)]}
        self.clean(got([], right), self.CLK, st("ON"))
        # no 7-hour shift: ON is only 03-05's own minutes before 9:30 (high 100 = P0, not armed)
        self.caught(got([], {"2024-03-05": [arm("ON", 1, 92, 90)]}), "missing", self.CLK, st("ON"))
        # 16:30 wrongly counted in 03-05's session: ON high 115
        self.caught(got([], {"2024-03-05": [arm("ON", -1, 115, 117), arm("ON", 1, 92, 90)]}), "extra",
                    self.CLK, st("ON"))

    # Spring: 2024-03-10 21:30 UTC is 17:30 EDT, so it is S(03-11) and its high 113 is ON. 13:30 UTC is 9:30 EDT.
    # An engine on a fixed UTC-5 clock reads 21:30 as 16:30 (Sunday's session) and arms only the long.
    DST = [mu("2024-03-08 15:00", 100, 101, 99, 100), mu("2024-03-10 21:30", 100, 113, 100, 100),
           mu("2024-03-10 23:00", 100, 100, 93, 100), mu("2024-03-11 13:30", 100, 100, 100, 100),
           mu("2024-03-11 20:00", 100, 100, 100, 100)]

    def test_daylight_saving_starts(self):
        self.clean(got([], {"2024-03-11": [arm("ON", -1, 113, 115), arm("ON", 1, 93, 91)]}), self.DST, st("ON"))
        self.caught(got([], {"2024-03-11": [arm("ON", 1, 93, 91)]}), "missing", self.DST, st("ON"))

    # Autumn: 2024-11-03 21:30 UTC is 16:30 EST, so it is S(11-03), not ON for 11-04. ON(11-04) = 23:00 UTC
    # (18:00 EST, high 108) and 13:00 UTC (8:00 EST, low 94). An engine still on UTC-4 takes the 114.
    FALL = [mu("2024-11-01 14:00", 100, 101, 99, 100), mu("2024-11-03 21:30", 100, 114, 100, 100),
            mu("2024-11-03 23:00", 100, 108, 100, 100), mu("2024-11-04 13:00", 100, 100, 94, 100),
            mu("2024-11-04 14:30", 100, 100, 100, 100), mu("2024-11-04 21:00", 100, 100, 100, 100)]

    def test_daylight_saving_ends(self):
        self.clean(got([], {"2024-11-04": [arm("ON", -1, 108, 110), arm("ON", 1, 94, 92)]}), self.FALL, st("ON"))
        self.caught(got([], {"2024-11-04": [arm("ON", -1, 114, 116), arm("ON", 1, 94, 92)]}), "extra",
                    self.FALL, st("ON"))


# ---------------------------------------------------------------------------------------------- one contract a day
class ContractTests(Case):
    # R1. 03-04 is contract 1; the roll to contract 2 (gap +5) is stamped 00:00 UTC 03-05 (19:00 EST 03-04).
    # D = 03-05 trades contract 2, P0 105. PD moved by +5: 115 and 95, both 10 from P0.
    ROLLED = [m("2024-03-04 10:00", 100, 110, 90, 100, iid=1), m("2024-03-05 09:30", 105, 105, 105, 105, iid=2),
              m("2024-03-05 16:00", 105, 105, 105, 105, iid=2)]
    ROLL = [Roll(uts("2024-03-05 00:00"), 1, 2, 5.0)]
    MOVED = {"2024-03-05": [arm("PD", -1, 115, 117), arm("PD", 1, 95, 93)]}
    UNMOVED = {"2024-03-05": [arm("PD", -1, 110, 112), arm("PD", 1, 90, 88)]}

    def test_older_contract_moved_by_the_roll_gap(self):
        self.clean(got([], self.MOVED), self.ROLLED, st("PD"), rolls=self.ROLL)
        self.caught(got([], self.UNMOVED), "missing", self.ROLLED, st("PD"), rolls=self.ROLL)

    # R2. The roll falls inside D's overnight: 18:00 (contract 1, before the 19:00 roll) is moved +5 to 113;
    # 20:00 is contract 2 (low 99). ON = 113 / 99; the traded contract is the 9:30 minute's (2).
    def test_overnight_straddling_the_roll(self):
        mins = [m("2024-03-04 10:00", 100, 101, 99, 100, iid=1), m("2024-03-04 18:00", 100, 108, 100, 100, iid=1),
                m("2024-03-04 20:00", 105, 106, 99, 105, iid=2), m("2024-03-05 09:30", 105, 105, 105, 105, iid=2),
                m("2024-03-05 16:00", 105, 105, 105, 105, iid=2)]
        self.clean(got([], {"2024-03-05": [arm("ON", -1, 113, 115), arm("ON", 1, 99, 97)]}), mins, st("ON"),
                   rolls=self.ROLL)
        self.caught(got([], {"2024-03-05": [arm("ON", -1, 108, 110), arm("ON", 1, 99, 97)]}), "extra", mins,
                    st("ON"), rolls=self.ROLL)

    # R3. A minute of contract 3 in S(03-04) has no roll to contract 2: PD needs it, so PD is not drawn on 03-05.
    # ON(03-05) reads only contract-2 minutes (112 / 98) and is drawn as usual.
    UNJOIN = [m("2024-03-04 10:00", 100, 110, 90, 100, iid=1), m("2024-03-04 11:00", 100, 104, 96, 100, iid=3),
              m("2024-03-04 18:00", 105, 112, 105, 105, iid=2), m("2024-03-05 09:00", 105, 105, 98, 105, iid=2),
              m("2024-03-05 09:30", 105, 105, 105, 105, iid=2), m("2024-03-05 16:00", 105, 105, 105, 105, iid=2)]

    def test_a_minute_that_cannot_be_joined_stops_the_level(self):
        self.clean(got(), self.UNJOIN, st("PD"), rolls=self.ROLL)
        self.caught(got([], self.MOVED), "extra", self.UNJOIN, st("PD"), rolls=self.ROLL)
        self.clean(got([], {"2024-03-05": [arm("ON", -1, 112, 114), arm("ON", 1, 98, 96)]}), self.UNJOIN,
                   st("ON"), rolls=self.ROLL)

    def test_a_roll_with_no_known_gap_cannot_be_joined(self):
        none_gap = [Roll(uts("2024-03-05 00:00"), 1, 2, None)]
        self.clean(got(), self.ROLLED, st("PD"), rolls=none_gap)
        self.caught(got([], self.UNMOVED), "extra", self.ROLLED, st("PD"), rolls=none_gap)

    # R5. Two rolls in a row: 1 -> 2 (+2) on 03-06 and 2 -> 3 (+3) on 03-12. On 03-13 (contract 3, P0 105) the
    # prior week's contract-1 minute moves +5 (113 / 101) and its contract-2 minute +3 (112 / 100): PW 113 / 100.
    def test_a_chain_of_rolls_adds_every_gap(self):
        mins = [m("2024-03-04 10:00", 100, 108, 96, 100, iid=1), m("2024-03-06 10:00", 102, 109, 97, 102, iid=2),
                m("2024-03-13 09:30", 105, 105, 105, 105, iid=3), m("2024-03-13 16:00", 105, 105, 105, 105, iid=3)]
        rolls = [Roll(uts("2024-03-06 00:00"), 1, 2, 2.0), Roll(uts("2024-03-12 00:00"), 2, 3, 3.0)]
        self.clean(got([], {"2024-03-13": [arm("PW", -1, 113, 115), arm("PW", 1, 100, 98)]}), mins, st("PW"),
                   rolls=rolls)
        # only the last gap added to both: 111/99 and 112/100 -> PW 112 / 99
        self.caught(got([], {"2024-03-13": [arm("PW", -1, 112, 114), arm("PW", 1, 99, 97)]}), "missing", mins,
                    st("PW"), rolls=rolls)

    # R6. A moved price is rounded to the tick, half up: a +0.5 gap makes 110.5 -> 111 and 90.5 -> 91.
    def test_moved_price_rounded_half_up(self):
        half = [Roll(uts("2024-03-05 00:00"), 1, 2, 0.5)]
        self.clean(got([], {"2024-03-05": [arm("PD", -1, 111, 113), arm("PD", 1, 91, 89)]}), self.ROLLED,
                   st("PD"), rolls=half)
        self.caught(got([], {"2024-03-05": [arm("PD", -1, 110, 112), arm("PD", 1, 90, 88)]}), "missing",
                    self.ROLLED, st("PD"), rolls=half)


# ---------------------------------------------------------------------------------------------- the seven kinds
class KindTests(Case):
    # PD = S(previous trading date) whole. D = Monday 03-04, previous trading date Friday 03-01, whose session
    # runs from 18:00 on 02-29 (high 109) to 16:30 on 03-01 (low 93). Sunday 18:00 belongs to 03-04, not PD.
    def test_pd_is_the_whole_previous_session(self):
        mins = [m("2024-02-29 18:00", 100, 109, 100, 100), m("2024-03-01 10:00", 100, 101, 99, 100),
                m("2024-03-01 16:30", 100, 100, 93, 100), m("2024-03-03 18:00", 100, 115, 85, 100),
                m("2024-03-04 09:30", 100, 100, 100, 100), m("2024-03-04 16:00", 100, 100, 100, 100)]
        self.clean(got([], {"2024-03-04": [arm("PD", -1, 109, 111), arm("PD", 1, 93, 91)]}), mins, st("PD"))
        self.caught(got(), "missing", mins, st("PD"))       # 9:30-16:00 only: 101 / 99, both within d of P0
        self.caught(got([], {"2024-03-04": [arm("PD", -1, 115, 117), arm("PD", 1, 85, 83)]}), "extra", mins,
                    st("PD"))

    # PW for 03-11, 03-12 and 03-13 = the trading dates of the ISO week 03-04 to 03-10: S(03-04) (with the Sunday
    # 18:00 minute, high 111), S(03-05) and S(03-08) (with 16:30, low 92). The 02-29 minute is two weeks back.
    # Sunday 03-10 18:00 is S(03-11), this week. P0 100 on all three dates: short 111 / 113, long 92 / 90.
    # 03-04 to 03-08 see 02-29's week (130 / 70, beyond the band): nothing.
    PW_MIN = [m("2024-02-29 10:00", 100, 130, 70, 100), m("2024-03-03 18:00", 100, 111, 100, 100),
              m("2024-03-04 10:00", 100, 101, 99, 100), m("2024-03-05 10:00", 100, 104, 94, 100),
              m("2024-03-08 10:00", 100, 101, 99, 100), m("2024-03-08 16:30", 100, 100, 92, 100),
              m("2024-03-10 18:00", 100, 125, 75, 100), m("2024-03-11 10:00", 100, 101, 99, 100),
              m("2024-03-12 10:00", 100, 101, 99, 100), m("2024-03-13 09:30", 100, 100, 100, 100),
              m("2024-03-13 16:00", 100, 100, 100, 100)]

    def test_pw_is_the_prior_iso_week_of_sessions(self):
        right = {d: [arm("PW", -1, 111, 113), arm("PW", 1, 92, 90)] for d in ("2024-03-11", "2024-03-12",
                                                                                "2024-03-13")}
        self.clean(got([], right), self.PW_MIN, st("PW"))
        # calendar days in place of sessions: the Sunday 18:00 minute lost, PW high 104
        wrong = copy.deepcopy(right)
        wrong["2024-03-13"] = [arm("PW", -1, 104, 106), arm("PW", 1, 92, 90)]
        self.caught(got([], wrong), "missing", self.PW_MIN, st("PW"))

    # SW. D = 03-11; its 5 trading dates before are 03-04 to 03-08 (one bar each at 10:00), then S(03-11)'s bars
    # ending by 9:00: 18:00 (03-10), 02:00, 08:00. Eight bars:
    #   b0 101/98  b1 102/97  b2 103/90  b3 110/96  b4 104/88  b5 105/94  b6 106/93  b7 102/99   (high/low)
    # b3: 110 > 101, 102, 103 and > 104, 105, 106: a swing high. b4: 88 < 97, 90, 96 and < 94, 93, 99: a swing low.
    # 9:10 on D is a later minute but not a bar. P0 100: short 110 / 112, long 88 / 86.
    SW_BASE = [m("2024-03-04 10:00", 100, 101, 98, 100), m("2024-03-05 10:00", 100, 102, 97, 100),
               m("2024-03-06 10:00", 100, 103, 90, 100), m("2024-03-07 10:00", 100, 110, 96, 100),
               m("2024-03-08 10:00", 100, 104, 88, 100), m("2024-03-10 18:00", 100, 105, 94, 100),
               m("2024-03-11 02:00", 100, 106, 93, 100), m("2024-03-11 08:00", 100, 102, 99, 100)]

    def sw(self, trace_low=95, base=None):
        return sorted((base or self.SW_BASE) + [m("2024-03-11 09:10", 100, 105, trace_low, 100),
                                                m("2024-03-11 09:30", 100, 100, 100, 100),
                                                m("2024-03-11 16:00", 100, 100, 100, 100)], key=lambda b: b.ts)

    SW_BOTH = {"2024-03-11": [arm("SW", -1, 110, 112), arm("SW", 1, 88, 86)]}
    SW_HIGH = {"2024-03-11": [arm("SW", -1, 110, 112)]}

    def test_sw_swing_high_and_low(self):
        self.clean(got([], self.SW_BOTH), self.sw(), st("SW"))
        self.caught(got([], self.SW_HIGH), "missing", self.sw(), st("SW"))

    def test_sw_traded_through_by_a_later_minute_before_930(self):
        self.clean(got([], self.SW_HIGH), self.sw(trace_low=87), st("SW"))          # 87 = 88 - 1 tick
        self.caught(got([], self.SW_BOTH), "extra", self.sw(trace_low=87), st("SW"))
        self.clean(got([], self.SW_BOTH), self.sw(trace_low=88), st("SW"))          # equal is not through
        self.caught(got([], self.SW_HIGH), "missing", self.sw(trace_low=88), st("SW"))

    def test_sw_uses_exactly_five_trading_dates(self):
        # add 03-01 (a sixth date back) and drop b2's low to 85. With five dates b2 is bar 0..2 deep, so it has
        # no 3 bars before it: no swing. An engine reading six dates finds a swing low 85 (85 < 99, 98, 97 and
        # < 96, 88, 94) and arms a long 85 / 83. b4 (88) is not below b2's 85, so it is no swing either.
        base = [m("2024-03-01 10:00", 100, 100, 99, 100)] + [
            m("2024-03-06 10:00", 100, 103, 85, 100) if b.ts == ts("2024-03-06 10:00") else b for b in self.SW_BASE]
        self.clean(got([], self.SW_HIGH), self.sw(base=base), st("SW"))
        self.caught(got([], {"2024-03-11": [arm("SW", -1, 110, 112), arm("SW", 1, 85, 83)]}), "extra",
                    self.sw(base=base), st("SW"))

    def test_sw_bars_end_with_the_bar_ending_900(self):
        # highs b0..b7 = 101 102 103 104 105 112 106 107, lows all 99; 9:05 has high 103. With bars only up to
        # 8:00-9:00, b5 (112) has 2 bars after it: no swing, nothing armed. Taking 9:00-9:30 as a ninth bar makes
        # b5 a swing high (112 > 103, 104, 105 and > 106, 107, 103) armed short 112 / 114.
        highs = (101, 102, 103, 104, 105, 112, 106, 107)
        base = [m(t, 100, h, 99, 100) for t, h in zip(
            ("2024-03-04 10:00", "2024-03-05 10:00", "2024-03-06 10:00", "2024-03-07 10:00", "2024-03-08 10:00",
             "2024-03-10 18:00", "2024-03-11 02:00", "2024-03-11 08:00"), highs)]
        mins = base + [m("2024-03-11 09:05", 100, 103, 99, 100), m("2024-03-11 09:30", 100, 100, 100, 100),
                       m("2024-03-11 16:00", 100, 100, 100, 100)]
        self.clean(got(), mins, st("SW"))
        self.caught(got([], {"2024-03-11": [arm("SW", -1, 112, 114)]}), "extra", mins, st("SW"))

    # RN on RTY (step 25), P0 110: 100 is 10 below (long / 98), 125 is 15 above (short / 127); 75 and 150 are
    # beyond the band.
    def test_rn_round_numbers(self):
        mins = [m("2024-03-04 09:30", 110, 110, 110, 110), m("2024-03-04 16:00", 110, 110, 110, 110)]
        self.clean(got([], {"2024-03-04": [arm("RN", 1, 100, 98), arm("RN", -1, 125, 127)]}), mins, st("RN"),
                   market="RTY")
        self.caught(got([], {"2024-03-04": [arm("RN", 1, 100, 98)]}), "missing", mins, st("RN"), market="RTY")

    # RN on the yen: tick 0.000001, P0 0.009100, daily range 0.0001 (ATR 100 ticks), k 0.2: d = 20 ticks, band
    # 200 ticks. Half-yen levels 1 / (0.5 n) to the nearest tick, in ticks from P0 (9100):
    #   n 215 (107.5) 9302: +202, out      n 220 (110.0) 9091: -9, within d
    #   n 216 (108.0) 9259: +159           n 221 (110.5) 9050: -50
    #   n 217 (108.5) 9217: +117           n 222 (111.0) 9009: -91
    #   n 218 (109.0) 9174: +74            n 223 (111.5) 8969: -131
    #   n 219 (109.5) 9132: +32            n 224 (112.0) 8929: -171      n 225 (112.5) 8889: -211, out
    JY = {"pv": 1250000.0, "tick": 0.000001, "comm": 1.9, "slip_ticks": 1, "max_qty": 90}

    def test_rn_yen_half_yen_levels(self):
        dly = daily(lo=0.00905, hi=0.00915)
        mins = [m("2024-03-04 09:30", 0.0091, 0.0091, 0.0091, 0.0091),
                m("2024-03-04 16:00", 0.0091, 0.0091, 0.0091, 0.0091)]
        shorts = [arm("RN", -1, t * 1e-6, (t + 20) * 1e-6) for t in (9132, 9174, 9217, 9259)]
        longs = [arm("RN", 1, t * 1e-6, (t - 20) * 1e-6) for t in (9050, 9009, 8969, 8929)]
        self.clean(got([], {"2024-03-04": shorts + longs}), mins, st("RN"), market="6J", spec=self.JY,
                   daily_=dly)
        whole_yen = [a for a in shorts + longs if round(a["level"] * 1e6) not in (9132, 9217, 9050, 8969)]
        self.caught(got([], {"2024-03-04": whole_yen}), "missing", mins, st("RN"), market="6J", spec=self.JY,
                    daily_=dly)

    # VP of S(03-04): 100 x10 (one price), 105 x4, 95 x3, 106-110 x5 (1 a price), 90-94 x5 (1 a price). Total 27,
    # 70% = 18.9. POC 100. Growing the value area: 101/99 both 0, a tie, both (and so on to 104/96); 105 (4) beats
    # 95 (3): up, 14; 95 (3) beats 106 (1): down, 17; 106 and 94 tie at 1: both, 19 >= 18.9. VA 94 to 106.
    # P0 97: POC 100 short / 102, VAH 106 short / 108, VAL 94 long / 92.
    VP = [m("2024-03-04 10:00", 100, 100, 100, 100, v=10), m("2024-03-04 10:01", 105, 105, 105, 105, v=4),
          m("2024-03-04 10:02", 95, 95, 95, 95, v=3), m("2024-03-04 10:03", 106, 110, 106, 110, v=5),
          m("2024-03-04 10:04", 94, 94, 90, 90, v=5), m("2024-03-05 09:30", 97, 97, 97, 97),
          m("2024-03-05 16:00", 97, 97, 97, 97)]

    def test_vp_point_of_control_and_value_area(self):
        self.clean(got([], {"2024-03-05": [arm("VP", -1, 100, 102), arm("VP", -1, 106, 108), arm("VP", 1, 94, 92)]}),
                   self.VP, st("VP"))
        # a tie adds only the price above: VA 100 to 110, so short 100 / 102 and short 110 / 112, no long
        self.caught(got([], {"2024-03-05": [arm("VP", -1, 100, 102), arm("VP", -1, 110, 112)]}), "missing",
                    self.VP, st("VP"))

    def test_vp_point_of_control_tie_goes_nearest_the_midpoint_then_lower(self):
        # 100 x10 and 104 x10, with 98 x1 and 108 x1: midpoint 103, so the POC is 104. VA from 104: 105/103,
        # 106/102 and 107/101 are 0-0 ties (both), then 100 (10) beats 108 (1): VA 100 to 107 (20 >= 15.4).
        # P0 112, all longs: 107 / 105, 104 / 102, 100 / 98 (4 apart, none merged).
        mins = [m("2024-03-04 10:00", 100, 100, 100, 100, v=10), m("2024-03-04 10:01", 104, 104, 104, 104, v=10),
                m("2024-03-04 10:02", 98, 98, 98, 98, v=1), m("2024-03-04 10:03", 108, 108, 108, 108, v=1),
                m("2024-03-05 09:30", 112, 112, 112, 112), m("2024-03-05 16:00", 112, 112, 112, 112)]
        self.clean(got([], {"2024-03-05": [arm("VP", 1, 107, 105), arm("VP", 1, 104, 102), arm("VP", 1, 100, 98)]}),
                   mins, st("VP"))
        # the lower of the tied prices as POC: VA 98 to 104, armed 104 and 100 only
        self.caught(got([], {"2024-03-05": [arm("VP", 1, 104, 102), arm("VP", 1, 100, 98)]}), "missing", mins,
                    st("VP"))
        # with 106 x1 in place of 108 the midpoint is 102, both 2 away: the lower, 100. VA 98 to 104; armed 104
        # and 100 (98 is within d of 100 and dropped).
        mins[3] = m("2024-03-04 10:03", 106, 106, 106, 106, v=1)
        self.clean(got([], {"2024-03-05": [arm("VP", 1, 104, 102), arm("VP", 1, 100, 98)]}), mins, st("VP"))
        # POC 104 instead: VA 100 to 106, armed 106 and 100
        self.caught(got([], {"2024-03-05": [arm("VP", 1, 106, 104), arm("VP", 1, 100, 98)]}), "missing", mins,
                    st("VP"))

    def test_vp_volume_is_split_exactly_not_in_floats(self):
        # 100 x10 (one price); 1 and 2 over 101-110 (0.1 + 0.2 = 0.3 a price); 3 over 90-99 (0.3 a price).
        # Total 16, 70% = 11.2. Exactly, 101 and 99 tie at 0.3: both, 10.6; 102 and 98 tie: both, 11.2. VA 98 to
        # 102. In floats 0.1 + 0.2 = 0.30000000000000004 beats 0.3, the area grows upward only and ends 100 to
        # 104. P0 110: exact VAH 102 (long / 100) and VAL 98 (long / 96); the POC 100 is within d of 102.
        mins = [m("2024-03-04 10:00", 100, 100, 100, 100, v=10), m("2024-03-04 10:01", 101, 110, 101, 110, v=1),
                m("2024-03-04 10:02", 101, 110, 101, 110, v=2), m("2024-03-04 10:03", 99, 99, 90, 90, v=3),
                m("2024-03-05 09:30", 110, 110, 110, 110), m("2024-03-05 16:00", 110, 110, 110, 110)]
        self.clean(got([], {"2024-03-05": [arm("VP", 1, 102, 100), arm("VP", 1, 98, 96)]}), mins, st("VP"))
        # the float answer: VAH 104 (long / 102) and POC = VAL 100 (long / 98)
        self.caught(got([], {"2024-03-05": [arm("VP", 1, 104, 102), arm("VP", 1, 100, 98)]}), "missing", mins,
                    st("VP"))

    # SD. D = 03-15; its 10 trading dates before are 03-01 and 03-04 to 03-14 (one bar each at 10:00), then
    # S(03-15)'s bars at 18:00 (03-14) and 03:00. Twelve bars, ranges 6 6 6 6 2 2 14 6 6 6 6 6: sum 72, A60 = 6.
    # Base bars need a range <= 3 (b4, b5), an impulse >= 12 (b6, closing 116 above the base's high 103).
    # b3's range 6 is too wide, so the base is b4-b5: zone 100 to 103, level 103. No later low below 103 (the
    # lowest is 104). P0 110: long 103, stop = bottom 100 - d 2 = 98 (distance 5).
    SD_BARS = [m("2024-03-01 10:00", 98, 101, 95, 98), m("2024-03-04 10:00", 99, 102, 96, 99),
               m("2024-03-05 10:00", 100, 103, 97, 100), m("2024-03-06 10:00", 101, 104, 98, 101),
               m("2024-03-07 10:00", 101, 102, 100, 101), m("2024-03-08 10:00", 102, 103, 101, 103),
               m("2024-03-11 10:00", 103, 117, 103, 116), m("2024-03-12 10:00", 112, 116, 110, 112),
               m("2024-03-13 10:00", 110, 114, 108, 110), m("2024-03-14 10:00", 108, 112, 106, 108),
               m("2024-03-14 18:00", 107, 111, 105, 107), m("2024-03-15 03:00", 106, 110, 104, 106)]

    def sd(self, bars=None, trace_low=105, p0=110, mirror=False):
        rows = (bars or self.SD_BARS) + [m("2024-03-15 09:10", 106, 108, trace_low, 106),
                                         m("2024-03-15 09:30", p0, p0, p0, p0), m("2024-03-15 16:00", p0, p0, p0, p0)]
        if mirror:
            rows = [Bar(b.ts, b.iid, 200 - b.open, 200 - b.low, 200 - b.high, 200 - b.close, b.volume) for b in rows]
        return rows

    def test_sd_demand_zone(self):
        self.clean(got([], {"2024-03-15": [arm("SD", 1, 103, 98)]}), self.sd(), st("SD"))
        # the stop d below the near edge instead of the far edge
        self.caught(got([], {"2024-03-15": [arm("SD", 1, 103, 101)]}), "missing", self.sd(), st("SD"))

    def test_sd_supply_zone_mirrors(self):
        # every price p becomes 200 - p. Base bars 100/98 and 99/97 (high/low); the impulse closes 84, below the
        # base's low 97: zone 97 to 100, level 97 (the bottom), stop = top 100 + d = 102. P0 90: a short.
        self.clean(got([], {"2024-03-15": [arm("SD", -1, 97, 102)]}), self.sd(p0=110, mirror=True), st("SD"))
        self.caught(got([], {"2024-03-15": [arm("SD", -1, 97, 99)]}), "missing", self.sd(p0=110, mirror=True),
                    st("SD"))

    def test_sd_longest_base_is_taken(self):
        # b3 narrowed to 100/98 (range 2): sum 68, A60 = 5.67, base bars <= 2.83: b3, b4, b5 all fit. The base of
        # three gives zone 98 to 103: long 103, stop 98 - 2 = 96. The one-bar base would give stop 99.
        bars = [m("2024-03-06 10:00", 99, 100, 98, 99) if b.ts == ts("2024-03-06 10:00") else b for b in self.SD_BARS]
        self.clean(got([], {"2024-03-15": [arm("SD", 1, 103, 96)]}), self.sd(bars), st("SD"))
        self.caught(got([], {"2024-03-15": [arm("SD", 1, 103, 99)]}), "missing", self.sd(bars), st("SD"))

    def test_sd_zone_traded_into_before_930_is_not_drawn(self):
        self.clean(got(), self.sd(trace_low=102), st("SD"))         # 102 = 103 - 1 tick, at 9:10 on D
        self.caught(got([], {"2024-03-15": [arm("SD", 1, 103, 98)]}), "extra", self.sd(trace_low=102), st("SD"))
        self.clean(got([], {"2024-03-15": [arm("SD", 1, 103, 98)]}), self.sd(trace_low=103), st("SD"))

    def test_sd_zone_only_on_its_own_side(self):
        # P0 99: the demand zone's level 103 is 4 above P0, the resistance side. Not armed.
        self.clean(got(), self.sd(p0=99), st("SD"))
        self.caught(got([], {"2024-03-15": [arm("SD", -1, 103, 105)]}), "extra", self.sd(p0=99), st("SD"))

    def test_sd_needs_ten_trading_dates(self):
        # dropping 03-01 leaves 03-15 with 9 dates before it: no SD at all.
        self.clean(got(), self.sd(self.SD_BARS[1:]), st("SD"))
        self.caught(got([], {"2024-03-15": [arm("SD", 1, 103, 98)]}), "extra", self.sd(self.SD_BARS[1:]), st("SD"))

    # ALL. 03-05: one minute 110 / 92. 03-12: 9:00 high 110 low 95 (v 1), 9:30 at 100 (v 1000, so S(03-12)'s
    # value area is the single price 100). 03-12 18:00: high 103, low 94 (ON for 03-13).
    # 03-12 (P0 100): ON 110/95, PD (S(03-05)) 110/92, PW (week of 03-04) 110/92, VP of S(03-05) (one minute,
    # 92-110, flat profile: POC 101, VA 94-108), RN 100. Shorts by distance: VP 108 taken; the 110s are within
    # 2 of it. Longs: ON 95 taken; VP 94 within d of 95; PD 92 (3 from 95) taken; PW 92 the same price, PD
    # first in the plan's order. -> VP short 108 / 110, ON long 95 / 93, PD long 92 / 90.
    # 03-13 (P0 100): ON 103/94, PD (S(03-12)) 110/95, PW 110/92, VP all 100 (within d). Shorts: ON 103, then
    # PD 110 (7 from 103), PW 110 dropped. Longs: PD 95; ON 94 dropped; PW 92 taken (3 from 95).
    ALL_MIN = [m("2024-03-05 10:00", 100, 110, 92, 100), m("2024-03-12 09:00", 100, 110, 95, 100),
               m("2024-03-12 09:30", 100, 100, 100, 100, v=1000), m("2024-03-12 18:00", 100, 103, 94, 100),
               m("2024-03-13 09:30", 100, 100, 100, 100), m("2024-03-13 16:00", 100, 100, 100, 100)]
    ALL_ARMED = {"2024-03-12": [arm("VP", -1, 108, 110), arm("ON", 1, 95, 93), arm("PD", 1, 92, 90)],
                 "2024-03-13": [arm("ON", -1, 103, 105), arm("PD", -1, 110, 112), arm("PD", 1, 95, 93),
                                arm("PW", 1, 92, 90)]}

    def test_all_merges_across_kinds(self):
        self.clean(got([], self.ALL_ARMED), self.ALL_MIN, st("ALL"))

    def test_all_equal_levels_go_to_the_earlier_kind(self):
        wrong = copy.deepcopy(self.ALL_ARMED)
        wrong["2024-03-13"][1] = arm("PW", -1, 110, 112)
        self.caught(got([], wrong), "PD short at 110 stop 112 missing", self.ALL_MIN, st("ALL"))


# ---------------------------------------------------------------------------------------------- arming
class ArmingTests(Case):
    # 03-05: ON 102 / 80 (from 03-04 18:00); 03-06: ON 103 / 79 (from 03-05 18:00). P0 100 both days.
    # 102 is exactly d above: within d, not armed. 80 is exactly 2 x ATR below: not further, armed (long / 78).
    # 103 is armed (short / 105). 79 is 21 below: further than 2 x ATR, not armed.
    BAND = [m("2024-03-04 10:00", 100, 101, 99, 100), m("2024-03-04 18:00", 100, 102, 80, 100),
            m("2024-03-05 09:30", 100, 100, 100, 100), m("2024-03-05 18:00", 100, 103, 79, 100),
            m("2024-03-06 09:30", 100, 100, 100, 100), m("2024-03-06 16:00", 100, 100, 100, 100)]
    BAND_ARMED = {"2024-03-05": [arm("ON", 1, 80, 78)], "2024-03-06": [arm("ON", -1, 103, 105)]}

    def test_within_d_and_beyond_two_atr_bounds(self):
        self.clean(got([], self.BAND_ARMED), self.BAND, st("ON"))
        wrong = copy.deepcopy(self.BAND_ARMED)
        wrong["2024-03-05"].append(arm("ON", -1, 102, 104))          # "within d" read as strictly within
        self.caught(got([], wrong), "extra", self.BAND, st("ON"))
        wrong = copy.deepcopy(self.BAND_ARMED)
        del wrong["2024-03-05"]                                        # 2 x ATR read as excluded
        self.caught(got([], wrong), "missing", self.BAND, st("ON"))

    def test_merge_measures_against_the_levels_already_taken(self):
        # In ALL (KindTests.ALL_MIN), 03-13's longs are PD 95, ON 94, PW 92: 95 taken, 94 dropped (1 from 95),
        # 92 kept (3 from 95). An engine measuring against the last level considered (94) drops 92 as well.
        wrong = copy.deepcopy(KindTests.ALL_ARMED)
        wrong["2024-03-13"] = wrong["2024-03-13"][:3]
        self.caught(got([], wrong), "PW long at 92 stop 90 missing", KindTests.ALL_MIN, st("ALL"))

    def test_no_atr_no_levels(self):
        # 13 daily bars before 03-05: no ATR, nothing armed, no trade. With 14 the basic case arms and trades.
        self.clean(got(), P1, P1_SET, daily_=daily("2024-02-21", "2024-03-04"))
        self.caught(p1(), "extra", P1, P1_SET, daily_=daily("2024-02-21", "2024-03-04"))
        self.clean(p1(), P1, P1_SET, daily_=daily("2024-02-20", "2024-03-04"))

    def test_atr_excludes_the_daily_bar_dated_d(self):
        # The bar dated 03-05 itself has a range of 100; ATR must come from the 14 bars before it (range 10).
        # With that bar counted, ATR would be 16.4 and d 3: different stops.
        dly = [a if a.bar.ts != dn("2024-03-05") * DAY else
               Adj(Bar(a.bar.ts, 1, 100.0, 150.0, 50.0, 100.0, 1), 100.0, 150.0, 50.0, 100.0) for a in DAILY]
        self.clean(p1(), P1, P1_SET, daily_=dly)
        g = got([], {"2024-03-05": [arm("PD", 1, 90, 87), arm("PD", -1, 110, 113)]})
        self.caught(g, "missing", P1, P1_SET, daily_=dly)


# ---------------------------------------------------------------------------------------------- entries
class EntryTests(Case):
    def test_limit_fills_only_on_a_one_tick_trade_through_at_the_level_exactly(self):
        # 10:00 low 90 only touches the level: no fill. 10:05 opens 89, below the level, low 89: fills at 90, not
        # at the better 89. Stop 88 is not reached. Flat at 15:55: 93 - 1 = 92. worst 89 - 90 = -1.
        mins = day5(("10:00", 95, 95, 90, 91), ("10:05", 89, 89, 89, 89), ("10:06", 89, 92, 89, 92),
                    ("15:55", 93, 94, 92, 93), ("16:00", 93, 93, 93, 93))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:05", "15:55", 92, "flat", -1)], PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0]["entry_ts"] = ts("2024-03-05 10:00")             # filled on the touch
        self.caught(g, "entry_ts", mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0].update(entry=89.0, points=3.0)                   # filled at the open, better than L
        self.caught(g, "entry", mins, st("PD"))

    def test_one_position_at_a_time_and_spent_levels(self):
        # 10:00 long at 90. 11:00 trades through 110 while the long is open: the short is spent. 12:00 stops the
        # long (reference 88, midpoint of 88 and 87 = 87.5, down to 87). 13:00 trades through 110 again: no trade.
        mins = day5(("10:00", 100, 100, 89, 90), ("11:00", 90, 111, 90, 110), ("12:00", 110, 110, 87, 88),
                    ("13:00", 88, 112, 88, 111), ("16:00", 111, 111, 111, 111))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "12:00", 87, "stop", -3)], PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"].append(trade("2024-03-05", "PD", -1, 110, 112, 2, None, "13:00", "16:00", 111, "flat", -2))
        self.caught(g, "extra", mins, st("PD"))

    def test_two_levels_traded_through_in_one_minute(self):
        # 10:00 opens 105, high 111, low 89: both levels traded through. 110 is 5 from the open, 90 is 15: the
        # short fills at 110 and the long is spent. T 3: target 110 - 6 = 104, hit at 10:01 (low 102). 10:02
        # trades through 90 again: spent, no trade. worst: the highest high held, 111: (111 - 110) x -1 = -1.
        mins = day5(("10:00", 105, 111, 89, 100), ("10:01", 103, 104, 102, 102), ("10:02", 100, 100, 88, 89),
                    ("16:00", 89, 89, 89, 89))
        right = got([trade("2024-03-05", "PD", -1, 110, 112, 2, 104, "10:00", "10:01", 104, "target", -1)],
                    PD_ARMED)
        self.clean(right, mins, st("PD", 0.2, 3))
        g = copy.deepcopy(right)
        g["trades"].append(trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:02", "16:00", 89, "flat", -2))
        self.caught(g, "extra", mins, st("PD", 0.2, 3))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -1)], PD_ARMED)
        self.caught(g, "missing", mins, st("PD", 0.2, 3))

    def test_equal_distance_from_the_open_goes_to_the_long(self):
        # 10:00 opens 100, high 111, low 89: 110 and 90 are both 10 from the open and 10 from P0. The long fills
        # (R15). Stop 88 not reached (low 89). 10:01 high 97: target 96.
        mins = day5(("10:00", 100, 111, 89, 95), ("10:01", 95, 97, 94, 96), ("16:00", 96, 96, 96, 96))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -1)], PD_ARMED)
        self.clean(right, mins, st("PD", 0.2, 3))
        g = got([trade("2024-03-05", "PD", -1, 110, 112, 2, 104, "10:00", "10:01", 104, "target", -1)], PD_ARMED)
        self.caught(g, "missing", mins, st("PD", 0.2, 3))

    def test_last_entry_minute_is_1459(self):
        # 14:59 low 89: fills. Flat at 15:55: 92 - 1 = 91. worst -1 (14:59's low 89).
        mins = day5(("14:59", 100, 100, 89, 90), ("15:55", 92, 93, 91, 92), ("16:00", 92, 92, 92, 92))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "14:59", "15:55", 91, "flat", -1)], PD_ARMED)
        self.clean(right, mins, st("PD"))
        self.caught(got([], PD_ARMED), "missing", mins, st("PD"))

    def test_no_entry_at_1500(self):
        mins = day5(("15:00", 100, 100, 89, 90), ("15:55", 92, 93, 91, 92), ("16:00", 92, 92, 92, 92))
        self.clean(got([], PD_ARMED), mins, st("PD"))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "15:00", "15:55", 91, "flat", -1)], PD_ARMED)
        self.caught(g, "extra", mins, st("PD"))

    def test_level_traded_through_on_the_exit_minute_is_spent(self):
        # 10:01 hits the long's target (96) and its high 111 trades through 110 on that exit minute: spent.
        # 10:02 trades through 110 again: no short.
        mins = day5(("10:00", 100, 100, 89, 90), ("10:01", 95, 111, 95, 105), ("10:02", 105, 112, 105, 111),
                    ("16:00", 111, 111, 111, 111))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -1)], PD_ARMED)
        self.clean(right, mins, st("PD", 0.2, 3))
        g = copy.deepcopy(right)
        g["trades"].append(trade("2024-03-05", "PD", -1, 110, 112, 2, 104, "10:02", "16:00", 111, "flat", -2))
        self.caught(g, "extra", mins, st("PD", 0.2, 3))

    def test_trades_out_of_entry_order(self):
        # two trades on one day: the long (10:00 to 10:01, target 96), then the short at 110 (10:05), which is
        # not spent because it was first traded through after the long's exit. Short target 104; 10:06 low 103.
        mins = day5(("10:00", 100, 100, 89, 90), ("10:01", 95, 97, 95, 96), ("10:05", 105, 111, 105, 108),
                    ("10:06", 106, 106, 103, 104), ("16:00", 104, 104, 104, 104))
        t1 = trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -1)
        t2 = trade("2024-03-05", "PD", -1, 110, 112, 2, 104, "10:05", "10:06", 104, "target", -1)
        self.clean(got([t1, t2], PD_ARMED), mins, st("PD", 0.2, 3))
        self.caught(got([t2, t1], PD_ARMED), "entry order", mins, st("PD", 0.2, 3))


# ---------------------------------------------------------------------------------------------- exits
class ExitTests(Case):
    def test_flat_at_1555_with_slippage_before_the_stop(self):
        # 15:55 opens 91: flat first, sold at 91 - 1 = 90, though its low 85 is through the stop. worst: lows held
        # 89 and 90, and the flat minute only at its fill 90: -1.
        mins = day5(("10:00", 100, 100, 89, 90), ("15:54", 91, 92, 90, 91), ("15:55", 91, 91, 85, 86),
                    ("16:00", 86, 86, 86, 86))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "15:55", 90, "flat", -1)], PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0].update(exit=86.0, reason="stop", points=-4.0)    # the stop checked first
        self.caught(g, "reason", mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0].update(exit=91.0, points=1.0)                    # no slippage
        self.caught(g, "exit", mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0]["worst"] = -5.0                                  # the flat minute's whole range counted
        self.caught(g, "worst", mins, st("PD"))

    def test_flat_fill_kept_inside_the_minute(self):
        # short at 110 (10:00 high 111, under the stop 112). 15:55 is 108 flat: 108 + 1 = 109 is above its high,
        # so 108. worst: 111 held -> -1; fill 108 -> +2.
        mins = day5(("10:00", 105, 111, 105, 108), ("15:55", 108, 108, 108, 108), ("16:00", 108, 108, 108, 108))
        right = got([trade("2024-03-05", "PD", -1, 110, 112, 2, None, "10:00", "15:55", 108, "flat", -1)],
                    PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = copy.deepcopy(right)
        g["trades"][0].update(exit=109.0, points=1.0)
        self.caught(g, "exit", mins, st("PD"))

    # A long at 90 (stop 88), stopped at 11:00: opens 92, low 85. Reference 88. Kind 88 - 1 = 87; midpoint
    # (88 + 85) / 2 = 86.5, down to 86; harsh 85. worst 85 - 90 = -5.
    LONG_STOP = day5(("10:00", 100, 100, 89, 90), ("11:00", 92, 92, 85, 86), ("16:00", 86, 86, 86, 86))
    # A short at 110 (stop 112), stopped at 11:00: opens 108, high 117. Kind 113; midpoint 114.5, up to 115;
    # harsh 117. worst (117 - 110) x -1 = -7.
    SHORT_STOP = day5(("10:00", 105, 111, 105, 108), ("11:00", 108, 117, 108, 116), ("16:00", 116, 116, 116, 116))

    def test_each_stop_fill(self):
        for fill, lx, sx in (("midpoint", 86, 115), ("kind", 87, 113), ("harsh-stops", 85, 117)):
            with self.subTest(fill=fill):
                right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "11:00", lx, "stop", -5)],
                            PD_ARMED)
                self.clean(right, self.LONG_STOP, st("PD"), fill=fill)
                right = got([trade("2024-03-05", "PD", -1, 110, 112, 2, None, "10:00", "11:00", sx, "stop", -7)],
                            PD_ARMED)
                self.clean(right, self.SHORT_STOP, st("PD"), fill=fill)
        # midpoint rounded to the nearest tick (87 / 114) instead of against the trade
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "11:00", 87, "stop", -5)], PD_ARMED)
        self.caught(g, "exit", self.LONG_STOP, st("PD"), fill="midpoint")
        g = got([trade("2024-03-05", "PD", -1, 110, 112, 2, None, "10:00", "11:00", 114, "stop", -7)], PD_ARMED)
        self.caught(g, "exit", self.SHORT_STOP, st("PD"), fill="midpoint")

    def test_gap_through_the_stop(self):
        # 11:00 opens 86, below the stop 88: a gap, reference 86. Midpoint (86 + 84) / 2 = 85; kind 86 - 1 = 85;
        # harsh 84. worst -6. A short gapping open at 114 over its 112 stop: kind 115 (its high).
        mins = day5(("10:00", 100, 100, 89, 90), ("11:00", 86, 87, 84, 85), ("16:00", 85, 85, 85, 85))
        for fill, x in (("midpoint", 85), ("kind", 85), ("harsh-stops", 84)):
            with self.subTest(fill=fill):
                self.clean(got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "11:00", x, "stop", -6,
                                      gap=True)], PD_ARMED), mins, st("PD"), fill=fill)
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "11:00", 86, "stop", -6)], PD_ARMED)
        b = self.breaks(g, mins, st("PD"))
        self.assertTrue(any(": gap is False" in x for x in b) and any(": exit is 86" in x for x in b), b)
        mins = day5(("10:00", 105, 111, 105, 108), ("11:00", 114, 115, 113, 115), ("16:00", 115, 115, 115, 115))
        self.clean(got([trade("2024-03-05", "PD", -1, 110, 112, 2, None, "10:00", "11:00", 115, "stop", -5,
                              gap=True)], PD_ARMED), mins, st("PD"), fill="kind")

    def test_stop_checked_on_the_entry_minute(self):
        # 10:00 low 87 fills the long at 90 and reaches the stop 88 on the same minute: reference 88, midpoint
        # 87.5 -> 87. worst -3.
        mins = day5(("10:00", 100, 100, 87, 88), ("10:01", 88, 95, 88, 95), ("16:00", 95, 95, 95, 95))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "10:00", 87, "stop", -3)], PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "10:01", 88, "stop", -3)], PD_ARMED)
        self.caught(g, "exit_ts", mins, st("PD"))

    def test_entry_minute_opening_through_the_stop_is_a_gap(self):
        # 10:00 opens 87 (below the stop 88), low 86: the long fills at 90 (never better) and the same minute is a
        # gap stop, reference 87: midpoint 86.5 -> 86. worst 86 - 90 = -4 (R16).
        mins = day5(("10:00", 87, 87, 86, 86), ("16:00", 86, 86, 86, 86))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "10:00", 86, "stop", -4, gap=True)],
                    PD_ARMED)
        self.clean(right, mins, st("PD"))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, None, "10:00", "10:00", 87, "stop", -4)], PD_ARMED)
        self.caught(g, "gap", mins, st("PD"))

    def test_stop_before_target_and_no_target_on_the_entry_minute(self):
        # T 3, target 96. The entry minute's high 100 is above 96 + 1, but no target on the entry minute. 10:01
        # reaches both the stop (low 87) and the target (high 98): the stop, midpoint 87.5 -> 87.
        mins = day5(("10:00", 100, 100, 89, 98), ("10:01", 95, 98, 87, 90), ("16:00", 90, 90, 90, 90))
        right = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 87, "stop", -3)], PD_ARMED)
        self.clean(right, mins, st("PD", 0.2, 3))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:00", 96, "target", -1)], PD_ARMED)
        self.caught(g, "exit_ts", mins, st("PD", 0.2, 3))
        g = got([trade("2024-03-05", "PD", 1, 90, 88, 2, 96, "10:00", "10:01", 96, "target", -3)], PD_ARMED)
        self.caught(g, "reason", mins, st("PD", 0.2, 3))

    # Early close: 2024-07-03 halts at 13:00 and reopens at 18:00, which is the next session. k 0.4, so d = 4:
    # long 90 / 86, short 110 / 114. The long from 10:00 is never stopped (12:59 low 87 > 86) and closes at the
    # last minute's close, 94, reason flat. worst: 10:00's low 89 -> -1; the exit minute only at its fill (+4),
    # not its low 87.
    EARLY = [m("2024-07-02 10:00", 100, 110, 90, 100), m("2024-07-03 09:30", 100, 101, 99, 100),
             m("2024-07-03 10:00", 100, 100, 89, 93), m("2024-07-03 12:59", 93, 95, 87, 94),
             m("2024-07-03 18:00", 94, 99, 80, 98)]
    EARLY_ARMED = {"2024-07-03": [arm("PD", 1, 90, 86), arm("PD", -1, 110, 114)]}

    def test_early_close(self):
        right = got([trade("2024-07-03", "PD", 1, 90, 86, 4, None, "10:00", "12:59", 94, "flat", -1)],
                    self.EARLY_ARMED)
        self.clean(right, self.EARLY, st("PD", 0.4))
        # the 18:00 reopen taken as part of the day: stopped there (midpoint of 86 and 80 = 83)
        g = got([trade("2024-07-03", "PD", 1, 90, 86, 4, None, "10:00", "18:00", 83, "stop", -10)],
                self.EARLY_ARMED)
        self.caught(g, "exit_ts", self.EARLY, st("PD", 0.4))
        g = copy.deepcopy(right)
        g["trades"][0]["worst"] = -3.0                  # the exit minute's low counted
        self.caught(g, "worst", self.EARLY, st("PD", 0.4))

    def test_early_close_on_the_entry_minute_counts_only_its_close(self):
        # the only trading minute after 9:30 is 12:59: it fills the long (low 89) and is the last minute. Closed
        # at its close 93; worst counts only that fill: +3 (favourable).
        mins = [m("2024-07-02 10:00", 100, 110, 90, 100), m("2024-07-03 09:30", 100, 101, 99, 100),
                m("2024-07-03 12:59", 100, 100, 89, 93)]
        right = got([trade("2024-07-03", "PD", 1, 90, 86, 4, None, "12:59", "12:59", 93, "flat", 3)],
                    self.EARLY_ARMED)
        self.clean(right, mins, st("PD", 0.4))
        g = copy.deepcopy(right)
        g["trades"][0]["worst"] = -1.0
        self.caught(g, "worst", mins, st("PD", 0.4))


# ---------------------------------------------------------------------------------------------- money
SA = {"pv": 10.0, "tick": 1.0, "comm": 2.0, "slip_ticks": 1, "max_qty": 90}
SPECS = {"A": SA, "B": dict(SA, max_qty=2), "C": {"pv": 1.0, "tick": 1.0, "comm": 0.5, "slip_ticks": 1,
                                                   "max_qty": 90}}


def pc(market, day, side, entry, exit_, dist, worst, at="10:00"):
    return {"market": market, "date": day, "kind": "PD", "level": float(entry), "side": side,
            "entry_ts": ts(f"{day} {at}"), "entry": float(entry), "stop": float(entry - side * dist),
            "dist": float(dist), "target": None, "exit_ts": ts(f"{day} 15:55"), "exit": float(exit_),
            "reason": "flat", "gap": False, "points": float((exit_ - entry) * side), "worst": float(worst)}


# Start $10,000, risk 1 %.
# 03-05 (start 10,000, risk 100): A long dist 2: loss for one (2 + 1) x 10 + 2 = 32, 100 / 32 -> 3, planned 96,
#   net 6 x 10 x 3 - 6 = 174, worst open -1 x 30 - 6 = -36. B short dist 2: 3, capped at 2, planned 64,
#   net -3 x 10 x 2 - 4 = -64, worst open -3 x 20 - 4 = -64. End 10,110; low 10,000 - 100 = 9,900.
# 03-06 (start 10,110, risk 101.10): A dist 40: loss for one 412, under one contract: skipped. B dist 3: 42,
#   2.4 -> 2, planned 84, net 1 x 20 - 4 = 16, worst open +1 x 20 - 4 = +16. End 10,126; low would be 10,126,
#   but never above the lower of start and end: 10,110.
# 03-07: only A dist 40: skipped; no day record.
# 03-08 (start 10,126, risk 101.26): A dist 2: 3.16 -> 3, net -1 x 30 - 6 = -36, worst open -2 x 30 - 6 = -66.
#   C dist 49 ($1 a point, $0.50 commission): loss for one 50.5, 101.26 / 50.5 = 2.005 -> 2 (from the day's
#   start; the balance after A, 10,090, would give 1), planned 101, net 10 x 2 - 1 = 19, worst open -4 x 2 - 1
#   = -9. End 10,109; low 10,126 - 75 = 10,051.
PER = {"A": {"trades": [pc("A", "2024-03-05", 1, 90, 96, 2, -1), pc("A", "2024-03-06", 1, 50, 45, 40, -6),
                        pc("A", "2024-03-07", 1, 50, 45, 40, -6), pc("A", "2024-03-08", 1, 90, 89, 2, -2)]},
       "B": {"trades": [pc("B", "2024-03-05", -1, 110, 113, 2, -3), pc("B", "2024-03-06", 1, 100, 101, 3, 1)]},
       "C": {"trades": [pc("C", "2024-03-08", 1, 200, 210, 49, -4, at="11:00")]}}


def acct_trade(t, qty, planned, net, bal):
    return dict(t, qty=qty, planned_cost=planned, net=net, balance_start=bal)


def acct():
    A, B, C = PER["A"]["trades"], PER["B"]["trades"], PER["C"]["trades"]
    return {"start": 10000.0,
            "trades": [acct_trade(A[0], 3, 96.0, 174.0, 10000.0), acct_trade(B[0], 2, 64.0, -64.0, 10000.0),
                       acct_trade(B[1], 2, 84.0, 16.0, 10110.0), acct_trade(A[3], 3, 96.0, -36.0, 10126.0),
                       acct_trade(C[0], 2, 101.0, 19.0, 10126.0)],
            "skipped": [{"market": "A", "date": d, "entry_ts": t["entry_ts"], "reason": "under one contract"}
                        for d, t in (("2024-03-06", A[1]), ("2024-03-07", A[2]))],
            "days": [{"date": "2024-03-05", "start": 10000.0, "end": 10110.0, "low": 9900.0},
                     {"date": "2024-03-06", "start": 10110.0, "end": 10126.0, "low": 10110.0},
                     {"date": "2024-03-08", "start": 10126.0, "end": 10109.0, "low": 10051.0}]}


class AccountTests(unittest.TestCase):
    def run_acct(self, r, per=PER, specs=SPECS, risk=1.0):
        return rc.check_account(r, per, specs, risk, 10000.0)

    def caught(self, r, word, **k):
        b = self.run_acct(r, **k)
        self.assertTrue(b, "expected a break")
        self.assertTrue(any(word in x for x in b), f"no break mentions {word!r}: {b}")

    def test_right_account_passes(self):
        self.assertEqual(self.run_acct(acct()), [])
        self.assertEqual(rc.replay_account(PER, SPECS, 1.0, 10000.0)["days"], acct()["days"])

    def test_the_cap(self):
        r = acct()
        r["trades"][1].update(qty=3, planned_cost=96.0, net=-96.0)
        self.caught(r, "qty")

    def test_sized_from_the_balance_at_the_start_of_the_day(self):
        r = acct()
        r["trades"][4].update(qty=1, planned_cost=50.5, net=9.5)
        self.caught(r, "qty")

    def test_under_one_contract_is_skipped_and_listed(self):
        r = acct()
        r["skipped"] = r["skipped"][:1]
        self.caught(r, "skipped")
        r = acct()
        r["skipped"].append({"market": "B", "date": "2024-03-06", "entry_ts": PER["B"]["trades"][1]["entry_ts"],
                             "reason": "under one contract"})
        self.caught(r, "skipped")

    def test_day_low_is_never_above_the_lower_of_start_and_end(self):
        r = acct()
        r["days"][1]["low"] = 10126.0
        self.caught(r, "low")
        r = acct()
        r["days"][0]["low"] = 9964.0                    # one trade's open loss left out
        self.caught(r, "low")

    def test_no_day_record_for_a_date_with_only_skips(self):
        r = acct()
        r["days"].insert(2, {"date": "2024-03-07", "start": 10126.0, "end": 10126.0, "low": 10126.0})
        self.caught(r, "extra")

    def test_net_and_balances_to_the_cent(self):
        r = acct()
        r["trades"][0]["net"] = 174.01
        self.caught(r, "net")
        r = acct()
        r["trades"][3]["balance_start"] = 10090.0
        self.caught(r, "balance_start")
        r = acct()
        r["days"][2]["end"] = 10109.01
        self.caught(r, "end")

    def test_trades_in_date_then_market_order(self):
        r = acct()
        r["trades"][3], r["trades"][4] = r["trades"][4], r["trades"][3]
        self.caught(r, "order")

    def test_a_half_cent_may_round_either_way_but_not_further(self):
        # 6B: $6,250 a point, tick 0.0001 ($0.625). Long 1.2700 -> 1.2701, dist 0.0050, risk 0.5 % of $10,000:
        # loss for one (0.0050 + 0.0001) x 6250 + 1.90 = 33.775, 50 / 33.775 -> 1. planned 33.775 and net
        # 0.625 - 1.90 = -1.275: both exact half cents. worst -0.0010: open loss -6.25 - 1.90 = -8.15.
        spec = {"6B": {"pv": 6250.0, "tick": 0.0001, "comm": 1.9, "slip_ticks": 1, "max_qty": 90}}
        t = pc("6B", "2024-03-05", 1, 1.2700, 1.2701, 0.0050, -0.0010)
        per = {"6B": {"trades": [t]}}
        for net, planned in ((-1.28, 33.78), (-1.27, 33.77)):
            with self.subTest(net=net):
                r = {"start": 10000.0, "trades": [dict(t, qty=1, planned_cost=planned, net=net, balance_start=10000.0)],
                     "skipped": [], "days": [{"date": "2024-03-05", "start": 10000.0, "end": 10000.0 + net,
                                              "low": 9991.85}]}
                self.assertEqual(rc.check_account(r, per, spec, 0.5, 10000.0), [])
        for net in (-1.26, -1.275):
            with self.subTest(net=net):
                r = {"start": 10000.0, "trades": [dict(t, qty=1, planned_cost=33.78, net=net, balance_start=10000.0)],
                     "skipped": [], "days": [{"date": "2024-03-05", "start": 10000.0, "end": 10000.0 + net,
                                              "low": 9991.85}]}
                b = rc.check_account(r, per, spec, 0.5, 10000.0)
                self.assertTrue(any(": net is" in x for x in b), b)


# ---------------------------------------------------------------------------------------------- candidate 2
# Break and retest (the amendment of 2026-11-18). Candidate 1's armed set is traded the other way: on 03-05 the
# PD high 110 (above P0) becomes a long, R 110, stop 108, after a 15-minute close >= 111; the PD low 90 becomes
# a short, R 90, stop 92, after a close <= 89. The retest: a long fills at R on a minute whose low <= R - 1 tick,
# from the minute after the break bar's last minute to the last minute before 3:00 PM.
ARMED2 = {"2024-03-05": [arm("PD", 1, 110, 108), arm("PD", -1, 90, 92)]}


def trade2(day, kind, side, R, stop, dist, target, entry_at, exit_at, exit_, reason, worst, break_at, gap=False):
    return dict(trade(day, kind, side, R, stop, dist, target, entry_at, exit_at, exit_, reason, worst, gap),
                break_ts=ts(f"{day} {break_at}"))


class Case2(Case):
    def breaks(self, g, minutes, settings, rolls=(), fill=None, market=None, spec=None, daily_=None):
        return rc.check_market2(g, minutes, self.daily_ if daily_ is None else daily_, list(rolls),
                                spec or self.spec, settings, fill or self.fill, market or self.market)


class Candidate2Tests(Case2):
    # Q1. The 9:30 bar (9:30 and 9:44) closes 110 = R: not a tick beyond, though its high is 112. The 9:45 bar
    # (9:50 and 9:59) closes 111: the break, break_ts 9:59. Its own minutes 9:50 and 9:59 dip to 109, but the
    # retest counts only from 10:00: 10:00's low 110 is not through; 10:05's low 109 fills the long at 110, stop
    # 108 untouched. T 3: target 116, hit at 10:10 (high 117). worst 109 - 110 = -1.
    Q1 = day5(("09:44", 109, 112, 109, 110), ("09:50", 110, 112, 109, 111), ("09:59", 111, 112, 109, 111),
              ("10:00", 111, 112, 110, 112), ("10:05", 111, 111, 109, 110), ("10:10", 110, 117, 110, 116),
              ("16:00", 116, 116, 116, 116))
    Q1_TRADE = trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "10:05", "10:10", 116, "target", -1, "09:59")

    def test_break_is_a_quarter_close_a_tick_beyond_and_retest_follows_the_break_bar(self):
        self.clean(got([self.Q1_TRADE], ARMED2), self.Q1, st("PD", 0.2, 3))
        # the break taken on the 9:30 bar (its high, or a close at R): retest from 9:45, filled at 9:50
        g = got([dict(self.Q1_TRADE, entry_ts=ts("2024-03-05 09:50"), break_ts=ts("2024-03-05 09:44"))], ARMED2)
        self.caught(g, "entry_ts", self.Q1, st("PD", 0.2, 3))
        # the retest counted inside the break bar: filled at 9:50 although the break came at 9:59
        g = got([dict(self.Q1_TRADE, entry_ts=ts("2024-03-05 09:50"))], ARMED2)
        self.caught(g, "entry_ts", self.Q1, st("PD", 0.2, 3))
        # break_ts as the break bar's start, not its last minute
        g = got([dict(self.Q1_TRADE, break_ts=ts("2024-03-05 09:45"))], ARMED2)
        self.caught(g, "break_ts", self.Q1, st("PD", 0.2, 3))

    def test_armed_set_is_candidate_1s_traded_the_other_way(self):
        self.clean(got([self.Q1_TRADE], ARMED2), self.Q1, st("PD", 0.2, 3))
        self.caught(got([self.Q1_TRADE], PD_ARMED), "missing", self.Q1, st("PD", 0.2, 3))

    def test_quarter_hours_run_on_the_clock_from_930(self):
        # The first minute after 9:30 is 9:33 (P0 100). The 9:30 to 9:45 bar holds 9:33 and 9:44 and closes 111:
        # the break, break_ts 9:44. 9:46 retests (low 109): long 110, stop 108; 10:00 hits the target 116.
        # Bars rolling from the first minute (9:33 to 9:48) would close 110 at 9:46: no break there, no trade.
        mins = [PRIOR[0], m("2024-03-05 09:33", 100, 101, 99, 100), m("2024-03-05 09:44", 105, 111, 105, 111),
                m("2024-03-05 09:46", 111, 111, 109, 110), m("2024-03-05 10:00", 110, 117, 110, 116),
                m("2024-03-05 16:00", 116, 116, 116, 116)]
        right = got([trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "09:46", "10:00", 116, "target", -1, "09:44")],
                    ARMED2)
        self.clean(right, mins, st("PD", 0.2, 3))
        self.caught(got([], ARMED2), "missing", mins, st("PD", 0.2, 3))

    def test_last_retestable_break_is_the_bar_starting_1430(self):
        # The 2:30 bar's last minute 14:44 closes 111: broken. 14:50 retests (low 109): long 110, flat at 15:55
        # at 112 - 1 = 111. worst: 14:50's low 109 -> -1; the flat minute only at its fill.
        mins = day5(("14:44", 105, 111, 105, 111), ("14:50", 111, 111, 109, 110), ("15:55", 112, 113, 111, 112),
                    ("16:00", 112, 112, 112, 112))
        right = got([trade2("2024-03-05", "PD", 1, 110, 108, 2, None, "14:50", "15:55", 111, "flat", -1, "14:44")],
                    ARMED2)
        self.clean(right, mins, st("PD"))
        self.caught(got([], ARMED2), "missing", mins, st("PD"))

    def test_a_break_on_the_bar_starting_1445_has_no_minute_left_to_retest(self):
        # The 2:45 bar runs to 15:00, so its last minute (14:59, close 111) is the last entry minute: nothing is
        # left after it. 15:00's low 109 would retest, but 15:00 is past the last entry (R24).
        mins = day5(("14:59", 105, 111, 105, 111), ("15:00", 111, 111, 109, 110), ("15:55", 112, 113, 111, 112),
                    ("16:00", 112, 112, 112, 112))
        self.clean(got([], ARMED2), mins, st("PD"))
        g = got([trade2("2024-03-05", "PD", 1, 110, 108, 2, None, "15:00", "15:55", 111, "flat", -1, "14:59")],
                ARMED2)
        self.caught(g, "extra", mins, st("PD"))

    def test_no_retest_entry_at_1500(self):
        # Broken at 14:44; 14:50 stays above 109; the first retest minute is 15:00: too late, no trade.
        mins = day5(("14:44", 105, 111, 105, 111), ("14:50", 111, 112, 110, 111), ("15:00", 111, 111, 109, 110),
                    ("15:55", 112, 113, 111, 112), ("16:00", 112, 112, 112, 112))
        self.clean(got([], ARMED2), mins, st("PD"))
        g = got([trade2("2024-03-05", "PD", 1, 110, 108, 2, None, "15:00", "15:55", 111, "flat", -1, "14:44")],
                ARMED2)
        self.caught(g, "extra", mins, st("PD"))

    # Zones. The demand zone 100 to 103 of KindTests.SD_BARS (P0 110) is armed in candidate 1 as a long at its
    # near edge 103. In candidate 2 it is a short: R = the far edge 100, stop = the near edge 103 + d = 105,
    # distance 5. The 9:30 bar dips to 98 (at 9:35 and on its last minute 9:44) but closes 101: no break.
    # The 9:45 bar closes 99 (<= 100 - 1) at 9:59: broken. Its 9:50 high 101 is inside the break bar; 10:05's
    # high 101 retests: short at 100. T 3: target 100 - 15 = 85, hit at 10:10 (low 84); its high 100 is under
    # the stop. worst (101 - 100) x -1 = -1.
    def sd2(self):
        return sorted(KindTests.sd(self) + [
            m("2024-03-15 09:35", 103, 103, 98, 101), m("2024-03-15 09:44", 101, 102, 98, 101),
            m("2024-03-15 09:50", 101, 101, 98, 99), m("2024-03-15 09:59", 99, 100, 98, 99),
            m("2024-03-15 10:05", 99, 101, 98, 100), m("2024-03-15 10:10", 100, 100, 84, 85)], key=lambda b: b.ts)

    SD_BARS = KindTests.SD_BARS

    def test_zone_retests_at_the_far_edge_with_the_stop_beyond_the_near_edge(self):
        right_trade = trade2("2024-03-15", "SD", -1, 100, 105, 5, 85, "10:05", "10:10", 85, "target", -1, "09:59")
        right = got([right_trade], {"2024-03-15": [arm("SD", -1, 100, 105)]})
        self.clean(right, self.sd2(), st("SD", 0.2, 3))
        # R at the near edge 103: the retest needs a high of 104, never reached
        self.caught(got([], {"2024-03-15": [arm("SD", -1, 103, 105)]}), "missing", self.sd2(), st("SD", 0.2, 3))
        # the stop d beyond the far edge (102): distance 2, target 94
        g = got([dict(right_trade, stop=102.0, dist=2.0, target=94.0, exit=94.0, points=6.0)],
                {"2024-03-15": [arm("SD", -1, 100, 102)]})
        self.caught(g, ": stop is 102", self.sd2(), st("SD", 0.2, 3))
        # the break read off the 9:30 bar's low (98): broken at 9:44, retested and filled at 9:50
        g = got([dict(right_trade, entry_ts=ts("2024-03-15 09:50"), break_ts=ts("2024-03-15 09:44"))],
                {"2024-03-15": [arm("SD", -1, 100, 105)]})
        self.caught(g, "entry_ts", self.sd2(), st("SD", 0.2, 3))

    def test_supply_zone_above_p0_retests_at_its_top(self):
        # The mirrored zone 97 to 100 lies above P0 90: broken up, R = its top 100, stop = its bottom 97 - 2 = 95.
        mins = KindTests.sd(self, mirror=True)
        self.clean(got([], {"2024-03-15": [arm("SD", 1, 100, 95)]}), mins, st("SD"))
        self.caught(got([], {"2024-03-15": [arm("SD", 1, 97, 95)]}), "missing", mins, st("SD"))

    # ALL on 03-05: S(03-04) is one minute 110 / 90 (volume 1) and one at 100 (volume 1000), so its volume levels
    # all sit at 100, within d of P0. ON (03-05 9:00) is 104 / 99. Candidate 1 arms shorts ON 104 and PD 110 and
    # a long PD 90 (ON 99 is within d; RN 100 too). Candidate 2: longs ON R 104 stop 102 and PD R 110 stop 108,
    # a short PD R 90 stop 92.
    BASE2 = [m("2024-03-04 10:00", 100, 110, 90, 100, v=1), m("2024-03-04 10:01", 100, 100, 100, 100, v=1000),
             m("2024-03-05 09:00", 100, 104, 99, 100), m("2024-03-05 09:30", 100, 101, 99, 100)]
    ALL2 = {"2024-03-05": [arm("ON", 1, 104, 102), arm("PD", 1, 110, 108), arm("PD", -1, 90, 92)]}

    def all2(self, *rows):
        return self.BASE2 + [m(f"2024-03-05 {t}", o, h, l, c) for t, o, h, l, c in rows]

    def test_broken_level_retested_while_a_position_is_open_is_spent(self):
        # 9:44 closes 105: ON broken. 9:50 (low 103) fills the ON long at 104. The 10:00 bar closes 111 at 10:14:
        # PD 110 broken while the long is open. 10:20 (low 109) meets PD's retest while the long is open: spent.
        # 11:00 stops the long (reference 102, midpoint 101.5 -> 101). 11:50 meets PD's retest again: no trade.
        # worst: lows held 103, 108, 109, 101 -> -3.
        mins = self.all2(("09:44", 101, 105, 101, 105), ("09:50", 105, 105, 103, 104), ("10:14", 108, 111, 108, 111),
                         ("10:20", 111, 111, 109, 110), ("11:00", 110, 110, 101, 102),
                         ("11:44", 105, 111, 105, 111), ("11:50", 111, 111, 109, 110), ("16:00", 110, 110, 110, 110))
        on = trade2("2024-03-05", "ON", 1, 104, 102, 2, None, "09:50", "11:00", 101, "stop", -3, "09:44")
        self.clean(got([on], self.ALL2), mins, st("ALL"))
        g = got([on, trade2("2024-03-05", "PD", 1, 110, 108, 2, None, "11:50", "16:00", 110, "flat", -1, "10:14")],
                self.ALL2)
        self.caught(g, "extra", mins, st("ALL"))

    def test_broken_level_retested_on_a_trades_exit_minute_is_spent(self):
        # T 5. The ON long (9:50) has target 104 + 10 = 114. PD 110 breaks at 10:14 (close 111, high 111: under
        # ON's target). 10:20 (high 115, low 109) is ON's exit at its target 114, and the first minute of PD's
        # retest: on the exit minute, so PD is spent. 10:30 meets PD's retest again: no trade.
        # worst: lows held 103, 108, 109 -> -1.
        mins = self.all2(("09:44", 101, 105, 101, 105), ("09:50", 105, 105, 103, 104), ("10:14", 108, 111, 108, 111),
                         ("10:20", 113, 115, 109, 110), ("10:30", 110, 110, 109, 110), ("16:00", 110, 110, 110, 110))
        on = trade2("2024-03-05", "ON", 1, 104, 102, 2, 114, "09:50", "10:20", 114, "target", -1, "09:44")
        self.clean(got([on], self.ALL2), mins, st("ALL", 0.2, 5))
        pd = trade2("2024-03-05", "PD", 1, 110, 108, 2, 120, "10:20", "16:00", 110, "flat", -1, "10:14")
        self.caught(got([on, pd], self.ALL2), "extra", mins, st("ALL", 0.2, 5))

    def test_a_break_counts_while_a_position_is_open(self):
        # T 3. The ON long (9:50, target 110) exits at 10:14 (high 111), the same minute that closes the 10:00
        # bar at 111 and breaks PD 110 while the long was open. 10:20 retests PD (low 109) after the exit: long
        # 110, target 116, hit at 10:30.
        mins = self.all2(("09:44", 101, 105, 101, 105), ("09:50", 105, 105, 103, 104), ("10:14", 108, 111, 108, 111),
                         ("10:20", 111, 111, 109, 110), ("10:30", 110, 117, 110, 116), ("16:00", 116, 116, 116, 116))
        right = got([trade2("2024-03-05", "ON", 1, 104, 102, 2, 110, "09:50", "10:14", 110, "target", -1, "09:44"),
                     trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "10:20", "10:30", 116, "target", -1, "10:14")],
                    self.ALL2)
        self.clean(right, mins, st("ALL", 0.2, 3))
        g = copy.deepcopy(right)
        del g["trades"][1]                              # the break ignored because a position was open
        self.caught(g, "missing", mins, st("ALL", 0.2, 3))

    def test_two_retests_in_one_minute_nearer_the_open_fills(self):
        # 9:44 closes 111: ON 104 and PD 110 both broken. 9:50 opens 105 with low 103: both retests met. ON's R
        # is 1 from the open, PD's 5: the ON long fills (stop 102 untouched) and PD is spent. T 3: ON's target
        # 110 at 10:00. 10:10 (low 108) meets PD's retest again: spent, no trade.
        mins = self.all2(("09:44", 101, 112, 101, 111), ("09:50", 105, 106, 103, 104), ("10:00", 104, 111, 104, 110),
                         ("10:10", 110, 110, 108, 109), ("16:00", 109, 109, 109, 109))
        on = trade2("2024-03-05", "ON", 1, 104, 102, 2, 110, "09:50", "10:00", 110, "target", -1, "09:44")
        self.clean(got([on], self.ALL2), mins, st("ALL", 0.2, 3))
        pd = trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "10:10", "16:00", 109, "flat", -2, "09:44")
        self.caught(got([on, pd], self.ALL2), "extra", mins, st("ALL", 0.2, 3))

    def test_two_retests_the_later_listed_level_can_be_nearer_the_open(self):
        # 9:50 opens 109: PD's R 110 is 1 away, ON's 104 is 5. The PD long fills and the same minute stops it
        # (low 103 <= 108; reference 108, midpoint 105.5 -> 105). ON is spent. 10:30 meets ON's retest: no trade.
        mins = self.all2(("09:44", 101, 112, 101, 111), ("09:50", 109, 109, 103, 104), ("10:30", 104, 104, 102, 103),
                         ("16:00", 103, 103, 103, 103))
        pd = trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "09:50", "09:50", 105, "stop", -7, "09:44")
        self.clean(got([pd], self.ALL2), mins, st("ALL", 0.2, 3))
        on = trade2("2024-03-05", "ON", 1, 104, 102, 2, 110, "09:50", "09:50", 102, "stop", -1, "09:44")
        self.caught(got([on], self.ALL2), "missing", mins, st("ALL", 0.2, 3))

    def test_two_retests_equally_near_the_open_go_to_the_r_nearer_p0(self):
        # 9:50 opens 107: both R are 3 away. ON's R 104 is 4 from P0, PD's 110 is 10: ON fills (R26).
        mins = self.all2(("09:44", 101, 112, 101, 111), ("09:50", 107, 107, 103, 104), ("10:00", 104, 111, 104, 110),
                         ("16:00", 110, 110, 110, 110))
        on = trade2("2024-03-05", "ON", 1, 104, 102, 2, 110, "09:50", "10:00", 110, "target", -1, "09:44")
        self.clean(got([on], self.ALL2), mins, st("ALL", 0.2, 3))
        pd = trade2("2024-03-05", "PD", 1, 110, 108, 2, 116, "09:50", "09:50", 105, "stop", -7, "09:44")
        self.caught(got([pd], self.ALL2), "missing", mins, st("ALL", 0.2, 3))

    def test_account_carries_break_ts_through(self):
        per = {"NQ": {"trades": [self.Q1_TRADE]}}
        r = rc.replay_account(per, {"NQ": SPEC}, 1.0, 10000.0)
        self.assertEqual(rc.check_account(r, per, {"NQ": SPEC}, 1.0, 10000.0), [])
        r["trades"][0]["break_ts"] += 60 * NS
        b = rc.check_account(r, per, {"NQ": SPEC}, 1.0, 10000.0)
        self.assertTrue(any("break_ts" in x for x in b), b)


# ---------------------------------------------------------------------------------------------- a random market
class RandomMarketTests(unittest.TestCase):
    """Twenty days of random-walk minutes, every kind: the replay must run end to end, agree with itself, find
    trades and levels of every kind, and catch any single changed field."""

    @classmethod
    def setUpClass(cls):
        rnd = random.Random(20261118)
        mins, p, iid = [], 10000.0, 1
        t = uts("2024-03-03 23:00")                    # Sunday 18:00 EST
        end = uts("2024-04-01 00:00")
        rolls, sd = [], {}
        while t < end:
            wall = datetime.fromtimestamp(t // NS, NY)
            if wall.weekday() == 5 or (wall.weekday() == 4 and wall.hour >= 17) or \
                    (wall.weekday() == 6 and wall.hour < 18) or wall.hour == 17:
                t += 60 * NS
                continue
            if t == uts("2024-03-14 00:00"):           # a roll to contract 2, 8 PM EDT, gap +12.5
                rolls.append(Roll(t, 1, 2, 12.5))
                iid, p = 2, p + 12.5
            hour = t // (3600 * NS)                     # quiet, normal and fast hours, so zones form
            if hour not in sd:
                sd[hour] = rnd.choice((0.3, 0.3, 2.0, 2.0, 2.0, 7.0))
            o = p
            c = round((o + rnd.gauss(0, sd[hour])) * 4) / 4
            h = max(o, c) + rnd.choice((0, 0.25, 0.5, 1.0))
            lo = min(o, c) - rnd.choice((0, 0.25, 0.5, 1.0))
            mins.append(Bar(t, iid, o, h, lo, c, rnd.randint(1, 50)))
            p = c
            t += 60 * NS
        cls.mins, cls.rolls = mins, rolls
        cls.daily = daily("2024-01-01", "2024-04-30", lo=9900.0, hi=10060.0)        # ATR 160
        cls.spec = {"pv": 2.0, "tick": 0.25, "comm": 1.9, "slip_ticks": 2, "max_qty": 90}

    def replay(self, settings, fill="midpoint"):
        return rc.replay_market(self.mins, self.daily, self.rolls, self.spec, settings, fill, "NQ")

    def test_every_kind_runs_agrees_with_itself_and_trades(self):
        kinds_seen = set()
        for kind in rc.KINDS + ("ALL",):
            for k, target in ((0.1, 3), (0.4, None)):
                for fill in rc.FILLS:
                    s = st(kind, k, target)
                    g = self.replay(s, fill)
                    self.assertEqual(rc.check_market(g, self.mins, self.daily, self.rolls, self.spec, s, fill, "NQ"),
                                     [], (kind, k, target, fill))
                    if g["trades"]:
                        kinds_seen.add(kind)
                    for t in g["trades"]:
                        a = {(x["kind"], x["side"], x["level"]) for x in g["armed"][t["date"]]}
                        self.assertIn((t["kind"], t["side"], t["level"]), a)
                        self.assertLessEqual(t["worst"], max(t["points"], 0) + 1e-9)
                        if t["reason"] == "target":
                            self.assertAlmostEqual(t["points"], target * t["dist"])
        self.assertEqual(kinds_seen, set(rc.KINDS) | {"ALL"})

    def test_any_changed_field_is_caught(self):
        s = st("ALL", 0.1, 3)
        g = self.replay(s)
        self.assertGreater(len(g["trades"]), 10)
        rnd = random.Random(7)
        for _ in range(40):
            h = copy.deepcopy(g)
            t = rnd.choice(h["trades"])
            f = rnd.choice(("entry", "stop", "dist", "exit", "points", "worst", "entry_ts", "exit_ts", "reason",
                            "gap", "kind", "target"))
            if f in ("entry_ts", "exit_ts"):
                t[f] += 60 * NS
            elif f == "reason":
                t[f] = "stop" if t[f] != "stop" else "flat"
            elif f == "gap":
                t[f] = not t[f]
            elif f == "kind":
                t[f] = "ON" if t[f] != "ON" else "PD"
            elif f == "target":
                t[f] = None if t[f] is not None else 1.0
            else:
                t[f] += 0.25
            b = rc.check_market(h, self.mins, self.daily, self.rolls, self.spec, s, "midpoint", "NQ")
            self.assertTrue(any(f"{f} is" in x for x in b), (f, b))

    def test_candidate_2_runs_agrees_with_itself_and_trades(self):
        by_ts = {b.ts: b for b in self.mins}
        seen = set()
        for kind in rc.KINDS + ("ALL",):
            for k, target in ((0.1, 3), (0.4, None)):
                for fill in rc.FILLS:
                    s = st(kind, k, target)
                    g = rc.replay_market2(self.mins, self.daily, self.rolls, self.spec, s, fill, "NQ")
                    self.assertEqual(rc.check_market2(g, self.mins, self.daily, self.rolls, self.spec, s, fill,
                                                      "NQ"), [], (kind, k, target, fill))
                    if g["trades"]:
                        seen.add(kind)
                    for t in g["trades"]:
                        a = {(x["kind"], x["side"], x["level"], x["stop"]) for x in g["armed"][t["date"]]}
                        self.assertIn((t["kind"], t["side"], t["level"], t["stop"]), a)
                        self.assertLess(t["break_ts"], t["entry_ts"])
                        close = by_ts[t["break_ts"]].close
                        self.assertGreaterEqual((close - t["level"]) * t["side"], 0.25 - 1e-9)
                        wall = datetime.fromtimestamp(t["entry_ts"] // NS, NY)
                        self.assertLess((wall.hour, wall.minute), (15, 0))
                        if t["reason"] == "target":
                            self.assertAlmostEqual(t["points"], target * t["dist"])
        self.assertEqual(seen, set(rc.KINDS) | {"ALL"})

    def test_candidate_2_any_changed_field_is_caught(self):
        s = st("ALL", 0.1, 3)
        g = rc.replay_market2(self.mins, self.daily, self.rolls, self.spec, s, "midpoint", "NQ")
        self.assertGreater(len(g["trades"]), 10)
        rnd = random.Random(8)
        for _ in range(40):
            h = copy.deepcopy(g)
            t = rnd.choice(h["trades"])
            f = rnd.choice(("entry", "stop", "dist", "exit", "worst", "entry_ts", "exit_ts", "break_ts", "kind"))
            if f.endswith("_ts"):
                t[f] += 60 * NS
            elif f == "kind":
                t[f] = "ON" if t[f] != "ON" else "PD"
            else:
                t[f] += 0.25
            b = rc.check_market2(h, self.mins, self.daily, self.rolls, self.spec, s, "midpoint", "NQ")
            self.assertTrue(any(f"{f} is" in x for x in b), (f, b))

    def test_reproduces_on_a_second_run_and_from_a_cold_cache(self):
        s = st("ALL", 0.2, 5)
        a = self.replay(s)
        rc.clear_cache()
        self.assertEqual(self.replay(s), a)


if __name__ == "__main__":
    unittest.main()
