#!/usr/bin/env python3
"""Tests for rule_check.py, the independent replay of the trend plan's exact rule (PLAN.md, amendment of
2026-11-18). Every expected trade below was worked out by hand from the written rule; the working is in the
comments. Run: python3 -I -B test_rule_check.py (from this folder)."""
import copy
import os
import sys
import unittest
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mdata import Adj, Bar, Roll  # noqa: E402
import rule_check  # noqa: E402

NS = 1_000_000_000
DAY = 86400 * NS
EPOCH = date(1970, 1, 1).toordinal()
BASE = date(2024, 1, 1).toordinal() - EPOCH          # day number of 2024-01-01

S1 = {"pv": 10, "tick": 1.0, "comm": 2.0, "slip_ticks": 1, "max_qty": 90}


def dn(iso):
    return date.fromisoformat(iso).toordinal() - EPOCH


def iso(day):
    return date.fromordinal(EPOCH + day).isoformat()


def A(day, o, h, l, c, iid=1):
    return Adj(Bar(day * DAY, iid, o, h, l, c, 1), o, h, l, c)


def M(utc, o, h, l, c, iid=1):
    """A 1-minute bar starting at the given UTC time 'YYYY-MM-DD HH:MM'."""
    t = datetime.strptime(utc, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
    return Bar(int(t.timestamp()) * NS, iid, o, h, l, c, 1)


def wt(market, side, qty, ed, entry, xd, exit_, stop_initial, dist, planned, reason, gap, rolls, net, bal):
    return {"market": market, "side": side, "qty": qty, "entry_day": BASE + ed, "entry": entry,
            "exit_day": BASE + xd, "exit": exit_, "stop_initial": stop_initial, "dist": dist,
            "planned_cost": planned, "reason": reason, "gap": gap, "rolls": rolls, "net": net, "balance": bal}


def wday(d, start, end, low):
    return {"day": BASE + d, "date": iso(BASE + d), "start": start, "end": end, "low": low}


def bars(rows):
    return [A(BASE + d, o, h, l, c) for d, o, h, l, c in rows]


def weekly_result(settings, fill, trades, days, skipped=(), start=10000.0):
    return {"settings": settings, "fill": fill, "start": start, "trades": list(trades),
            "skipped": list(skipped), "days": list(days)}


def st(lookback, atr, stop, trail, risk):
    return {"lookback": lookback, "atr_days": atr, "stop_mult": stop, "trail_mult": trail, "risk_pct": risk}


# ---------------------------------------------------------------------------------------------- version B
# B1. L=2, ATR over 2 bars, stop 1 ATR, no trail, risk 1 %.
# d2: 104-100 > 0 long; ATR (4+4)/2 = 4, dist 4; loss for one = (4+1)*10+2 = 52; 100/52 -> 1 contract.
# d3: buy at 105+1 = 106, stop 102. d4: low 99 reaches 102 -> stopped (kind 101, midpoint 100.5 -> 100,
# harsh 99). Stopped that day, so no decision at d4's close (its signal is short): the wait of one day.
# d5: 100-107 < 0 short; ATR (8+4)/2 = 6, dist 6; loss for one 72; 1 contract. d6: sell 100-1 = 99, stop 105.
# d7 is the last bar: closes at 96, net (96-99)*-1*10 - 2 = 28.
B1_BARS = bars([(0, 100, 102, 98, 100), (1, 100, 103, 99, 101), (2, 101, 105, 101, 104),
                (3, 105, 108, 104, 107), (4, 107, 107, 99, 102), (5, 102, 103, 99, 100),
                (6, 100, 101, 97, 98), (7, 98, 99, 95, 96)])
B1_SET = st(2, 2, 1, None, 1)


def b1_expected(fill):
    exit1, net1 = {"kind": (101, -52.0), "midpoint": (100, -62.0), "harsh-stops": (99, -72.0)}[fill]
    b1 = 10000 + net1
    trades = [wt("X", "long", 1, 3, 106, 4, exit1, 102, 4, 52.0, "stop", False, 0, net1, b1),
              wt("X", "short", 1, 6, 99, 7, 96, 105, 6, 72.0, "end", False, 0, 28.0, b1 + 28)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000), wday(2, 10000, 10000, 10000),
            # d3 long 1 @106: close 107 -> +10-2; low 104 -> -20-2
            wday(3, 10000, 10008, 9978),
            wday(4, 10008, b1, b1), wday(5, b1, b1, b1),
            # d6 short 1 @99: close 98 -> +10-2; high 101 -> -20-2
            wday(6, b1, b1 + 8, b1 - 22), wday(7, b1 + 8, b1 + 28, b1 + 28)]
    return weekly_result(B1_SET, fill, trades, days)


# B2. L=1, ATR 1 bar, stop 2 ATR, trail 1 x dist, risk 2 %.
# d1: 102-100 long; ATR 2, dist 4; loss for one 52; 200/52 -> 3. d2: buy 104, stop 100; trail: best 106 - 4
# = 102. d3: best 109 -> 105. d4: 106-108 < 0 flips short; ATR 4, dist 8; loss for one 92; 200/92 -> 2.
# d5: sell to exit at 105-1 = 104 (net 0*30 - 6 = -6); sell short at 104, stop 112; trail: best low 101 + 8
# = 109. d6: high 110 reaches 109 -> buy at 109+1 = 110: net (110-104)*-1*10*2 - 4 = -124.
B2_BARS = bars([(0, 100, 101, 99, 100), (1, 100, 102, 100, 102), (2, 103, 106, 102, 105),
                (3, 105, 109, 105, 108), (4, 108, 110, 106, 106), (5, 105, 106, 101, 102),
                (6, 102, 110, 100, 108), (7, 108, 109, 107, 108)])
B2_SET = st(1, 1, 2, 1, 2)


def b2_expected():
    trades = [wt("X", "long", 3, 2, 104, 5, 104, 100, 4, 156.0, "signal", False, 0, -6.0, 9994.0),
              wt("X", "short", 2, 5, 104, 6, 110, 112, 8, 184.0, "stop", False, 0, -124.0, 9870.0)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000),
            wday(2, 10000, 10024, 9934),      # close 105: 1*30-6; low 102: -2*30-6
            wday(3, 10024, 10114, 10024),     # close 108: 4*30-6; low 105: 1*30-6
            wday(4, 10114, 10054, 10054),     # close 106 = low: 2*30-6
            wday(5, 10054, 10030, 9950),      # 9994 + short 2 @104: close 102 -> +40-4; high 106 -> -40-4
            wday(6, 10030, 9870, 9870), wday(7, 9870, 9870, 9870)]
    return weekly_result(B2_SET, "kind", trades, days)


# B3. Gap through the stop, and a market fill kept inside the bar.
# d1 long, dist 2, loss for one 32, 3 contracts. d2: buy 104 (= high), stop 102. d3 opens 98 <= 102: gap,
# kind 98-1 = 97 (net -7*30-6 = -216). d4: signal 97-97 = 0, no trade. d5: 99-97 long, risk 97.84 -> 3.
# d6 (last bar): buy 99+1 = 100 is above the high 99 -> 99; stop 97; closes at 99 (end): net -6.
B3_BARS = bars([(0, 100, 101, 99, 100), (1, 100, 102, 100, 102), (2, 103, 104, 103, 103),
                (3, 98, 99, 96, 97), (4, 97, 98, 96, 97), (5, 97, 99, 97, 99), (6, 99, 99, 98, 99)])
B3_SET = st(1, 1, 1, None, 1)


def b3_expected():
    trades = [wt("X", "long", 3, 2, 104, 3, 97, 102, 2, 96.0, "stop", True, 0, -216.0, 9784.0),
              wt("X", "long", 3, 6, 99, 6, 99, 97, 2, 96.0, "end", False, 0, -6.0, 9778.0)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000), wday(2, 10000, 9964, 9964),
            wday(3, 9964, 9784, 9784), wday(4, 9784, 9784, 9784), wday(5, 9784, 9784, 9784),
            wday(6, 9784, 9778, 9778)]
    return weekly_result(B3_SET, "kind", trades, days)


# B4. Two markets, the size cap, and the order of the morning's stops.
# Both long at d1 from 10000: A 3 contracts; B 100/32 -> 3, capped at 2 (planned 64).
# d2: A buy 104, stop 102, low 99 -> kind 101: net -96 -> 9904; then B buy 54, stop 52, low 52 -> kind
# 52-1 = 51 is below the low -> 52: net -2*20-4 = -44 -> 9860.
B4_SPECS = {"A": S1, "B": dict(S1, max_qty=2)}
B4_SERIES = {"A": bars([(0, 100, 101, 99, 100), (1, 100, 102, 100, 102), (2, 103, 104, 99, 100),
                        (3, 100, 101, 99, 100)]),
             "B": bars([(0, 50, 51, 49, 50), (1, 50, 52, 50, 52), (2, 53, 54, 52, 53), (3, 52, 53, 51, 52)])}


def b4_expected():
    trades = [wt("A", "long", 3, 2, 104, 2, 101, 102, 2, 96.0, "stop", False, 0, -96.0, 9904.0),
              wt("B", "long", 2, 2, 54, 2, 52, 52, 2, 64.0, "stop", False, 0, -44.0, 9860.0)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000), wday(2, 10000, 9860, 9860),
            wday(3, 9860, 9860, 9860)]
    return weekly_result(st(1, 1, 1, None, 1), "kind", trades, days)


# B5. A market with no bar is marked at its last close; the evening decisions run in market order, so B sizes
# from the balance after A's last-bar close; a trade under one contract is skipped and listed.
# A: long 3 @104 from d2, no bar d3, last bar d4 closes at 103: net -36 -> 9964.
# B (commission 10): d4 56-50 long, ATR 8, dist 8, loss for one 9*10+10 = 100; 99.64/100 -> 0: skipped.
B5_SPECS = {"A": S1, "B": dict(S1, comm=10.0)}
B5_SERIES = {"A": bars([(0, 100, 101, 99, 100), (1, 100, 102, 100, 102), (2, 103, 104, 103, 104),
                        (4, 104, 105, 103, 103)]),
             "B": bars([(0, 50, 51, 49, 50), (2, 50, 51, 50, 50), (3, 50, 51, 49, 50), (4, 50, 57, 49, 56),
                        (5, 56, 57, 55, 56)])}


def b5_expected():
    trades = [wt("A", "long", 3, 2, 104, 4, 103, 102, 2, 96.0, "end", False, 0, -36.0, 9964.0)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000),
            wday(2, 10000, 9994, 9964),       # close 104: 0-6; low 103: -30-6
            wday(3, 9994, 9994, 9994),        # A has no bar: marked at its last close 104
            wday(4, 9994, 9964, 9964), wday(5, 9964, 9964, 9964)]
    skipped = [{"market": "B", "day": BASE + 4, "side": "long", "reason": "under one contract"}]
    return weekly_result(st(1, 1, 1, None, 1), "kind", trades, days, skipped)


# B6. Rolls held through: rolls on d3 and d4 count (entry d2 < roll day <= exit d4); d2 and d5 do not.
# Each costs a commission and two slippages a contract: 3 * (2 + 2*1*10) = 66 a roll.
# Net = (105-104)*30 - 6 - 2*66 = -108.
B6_BARS = bars([(0, 100, 101, 99, 100), (1, 100, 102, 100, 102), (2, 103, 104, 103, 104),
                (3, 104, 106, 104, 105), (4, 105, 106, 104, 105)])
B6_ROLLS = [Roll((BASE + d) * DAY, 1, 2, 0.0) for d in (2, 3, 4, 5)]


def b6_expected():
    trades = [wt("X", "long", 3, 2, 104, 4, 105, 102, 2, 96.0, "end", False, 2, -108.0, 9892.0)]
    days = [wday(0, 10000, 10000, 10000), wday(1, 10000, 10000, 10000), wday(2, 10000, 9994, 9964),
            wday(3, 9994, 10024, 9994), wday(4, 10024, 9892, 9892)]
    return weekly_result(st(1, 1, 1, None, 1), "kind", trades, days)


class WeeklyCleanTests(unittest.TestCase):
    def test_b1_kind(self):
        self.assertEqual(rule_check.check_weekly(b1_expected("kind"), {"X": B1_BARS}, {}, {"X": S1}), [])

    def test_b1_midpoint(self):
        self.assertEqual(rule_check.check_weekly(b1_expected("midpoint"), {"X": B1_BARS}, {}, {"X": S1}), [])

    def test_b1_harsh(self):
        self.assertEqual(rule_check.check_weekly(b1_expected("harsh-stops"), {"X": B1_BARS}, {}, {"X": S1}), [])

    def test_b2_trail_and_flip(self):
        self.assertEqual(rule_check.check_weekly(b2_expected(), {"X": B2_BARS}, {}, {"X": S1}), [])

    def test_b3_gap_and_fill_inside_bar(self):
        self.assertEqual(rule_check.check_weekly(b3_expected(), {"X": B3_BARS}, {}, {"X": S1}), [])

    def test_b4_two_markets_cap_and_stop_order(self):
        self.assertEqual(rule_check.check_weekly(b4_expected(), B4_SERIES, {}, B4_SPECS), [])

    def test_b5_missing_bar_mark_and_evening_order_skip(self):
        self.assertEqual(rule_check.check_weekly(b5_expected(), B5_SERIES, {}, B5_SPECS), [])

    def test_b6_rolls(self):
        self.assertEqual(rule_check.check_weekly(b6_expected(), {"X": B6_BARS}, {"X": B6_ROLLS}, {"X": S1}), [])


class WeeklyBreakTests(unittest.TestCase):
    def run_b2(self, r):
        return rule_check.check_weekly(r, {"X": B2_BARS}, {}, {"X": S1})

    def assertBreak(self, breaks, word):
        self.assertTrue(breaks, "expected a break")
        self.assertTrue(any(word in b for b in breaks), f"no break mentions {word!r}: {breaks}")

    def test_wrong_side(self):
        r = b2_expected()
        r["trades"][0]["side"] = "short"
        self.assertBreak(self.run_b2(r), "side")

    def test_wrong_qty(self):
        r = b2_expected()
        r["trades"][1]["qty"] = 3
        self.assertBreak(self.run_b2(r), "qty")

    def test_wrong_exit_price(self):
        r = b2_expected()
        r["trades"][1]["exit"] = 109
        self.assertBreak(self.run_b2(r), "exit")

    def test_wrong_net(self):
        r = b2_expected()
        r["trades"][0]["net"] = -5.99
        self.assertBreak(self.run_b2(r), "net")

    def test_missing_trade(self):
        r = b2_expected()
        del r["trades"][1]
        self.assertBreak(self.run_b2(r), "missing")

    def test_extra_trade(self):
        r = b2_expected()
        r["trades"].append(wt("X", "long", 1, 7, 108, 7, 108, 106, 2, 32.0, "end", False, 0, -2.0, 9868.0))
        self.assertBreak(self.run_b2(r), "extra")

    def test_wrong_reason_and_gap(self):
        r = b2_expected()
        r["trades"][1]["gap"] = True
        self.assertBreak(self.run_b2(r), "gap")

    def test_wrong_day_record(self):
        r = b2_expected()
        r["days"][5]["low"] = 9951.0
        self.assertBreak(self.run_b2(r), "low")

    def test_missing_and_extra_skip(self):
        r = b5_expected()
        r["skipped"] = []
        self.assertBreak(rule_check.check_weekly(r, B5_SERIES, {}, B5_SPECS), "skip")
        r = b5_expected()
        r["skipped"].append({"market": "A", "day": BASE + 1, "side": "long", "reason": "under one contract"})
        self.assertBreak(rule_check.check_weekly(r, B5_SERIES, {}, B5_SPECS), "skip")

    def test_wrong_rolls(self):
        r = b6_expected()
        r["trades"][0]["rolls"] = 3
        self.assertBreak(rule_check.check_weekly(r, {"X": B6_BARS}, {"X": B6_ROLLS}, {"X": S1}), "rolls")

    def test_trades_out_of_order(self):
        r = b4_expected()
        r["trades"].reverse()
        self.assertBreak(rule_check.check_weekly(r, B4_SERIES, {}, B4_SPECS), "order")

    def test_net_off_by_a_cent_is_a_break_but_float_noise_is_not(self):
        r = b2_expected()
        r["trades"][0]["net"] = -6.0 + 1e-9
        r["trades"][0]["entry"] = 104 + 1e-9
        self.assertEqual(self.run_b2(r), [])
        r["trades"][0]["net"] = -6.01
        self.assertBreak(self.run_b2(r), "net")


# ---------------------------------------------------------------------------------------------- version A
A_SET = {"lookback": 1, "atr_days": 1, "stop_mult": 1, "trail_mult": None, "entry": "09:35", "flat": "15:55"}


def at(market, d, side, entry, exit_, stop_initial, dist, reason, gap, points, worst, qty, planned, net, bal):
    return {"market": market, "date": d, "side": side, "entry": entry, "exit": exit_,
            "stop_initial": stop_initial, "dist": dist, "reason": reason, "gap": gap, "points": points,
            "worst": worst, "qty": qty, "planned_cost": planned, "net": net, "balance": bal}


def aday(d, start, end, low):
    return {"date": d, "start": start, "end": end, "low": low}


def DA(iso_, o, h, l, c):
    return A(dn(iso_), o, h, l, c)


# A1. Winter (New York = UTC-5). Risk 2 %.
# 2024-03-05 reads the daily bar of 03-04 (not 03-05's own): 103-100 long; ATR 4, dist 4; loss for one 52;
# 200/52 -> 3. 09:30 is before the entry time. 09:35: buy 101+1 = 102, stop 98. 10:00 low 95 -> stopped
# (kind 97, midpoint 96.5 -> 96). Kind: points -5, worst -7 (the 10:00 low), net -5*30-6 = -156.
# 2024-03-06 reads 03-05: 96-103 short; ATR 9, dist 9; loss for one 102; 196.88/102 -> 1. 09:34 is before the
# entry; 09:40 sells 90-1 = 89, stop 98; 15:54 high 93; 15:55 flat: buy 92+1 = 93 capped at the high 92.
# points -3, worst -4, net -32.
A1_DAILY = {"X": [DA("2024-03-01", 100, 102, 98, 100), DA("2024-03-04", 100, 104, 100, 103),
                  DA("2024-03-05", 103, 104, 95, 96)]}
A1_MIN = {"X": [M("2024-03-05 14:30", 100, 100, 100, 100), M("2024-03-05 14:35", 101, 103, 100, 102),
                M("2024-03-05 14:36", 102, 104, 99, 103), M("2024-03-05 15:00", 103, 105, 95, 98),
                M("2024-03-05 15:01", 98, 99, 97, 98),
                M("2024-03-06 14:34", 90, 91, 89, 90), M("2024-03-06 14:40", 90, 92, 88, 91),
                M("2024-03-06 20:54", 91, 93, 90, 92), M("2024-03-06 20:55", 92, 92, 91, 91),
                M("2024-03-06 20:56", 91, 99, 91, 99)]}


def a1_expected(fill):
    if fill == "kind":
        t1 = at("X", "2024-03-05", "long", 102, 97, 98, 4, "stop", False, -5, -7, 3, 156.0, -156.0, 9844.0)
        t2 = at("X", "2024-03-06", "short", 89, 92, 98, 9, "flat", False, -3, -4, 1, 102.0, -32.0, 9812.0)
        days = [aday("2024-03-05", 10000, 9844, 10000 - 7 * 30 - 6), aday("2024-03-06", 9844, 9812, 9844 - 42)]
    else:   # midpoint: exit 96, points -6, net -186; then 196.28/102 -> 1
        t1 = at("X", "2024-03-05", "long", 102, 96, 98, 4, "stop", False, -6, -7, 3, 156.0, -186.0, 9814.0)
        t2 = at("X", "2024-03-06", "short", 89, 92, 98, 9, "flat", False, -3, -4, 1, 102.0, -32.0, 9782.0)
        days = [aday("2024-03-05", 10000, 9814, 10000 - 7 * 30 - 6), aday("2024-03-06", 9814, 9782, 9814 - 42)]
    return {"risk_pct": 2, "start": 10000.0, "trades": [t1, t2], "skipped": [], "days": days}


# A2. Summer (New York = UTC-4), entry 10:00, MNQ-like ticks, trail 1 x dist, midpoint fills, risk 0.5 %.
# 07-03 reads 07-02: 100.5-100 long; ATR 1.7 -> dist 1.5 (rounded down to the 0.25 tick); loss for one
# (1.5+0.5)*2+1.9 = 5.9; 50/5.9 -> 8. 13:59Z = 09:59 is before 10:00. 10:00: buy 200+0.5 = 200.5, stop 199;
# trail best 200.75-1.5 = 199.25. 10:01: best 202 -> 200.5. 10:02: low 200 reaches 200.5; midpoint of 200.5
# and 200 = 200.25. points -0.25, worst -0.75 (10:00 low 199.75), net -0.25*2*8 - 1.9*8 = -19.2.
MNQ = {"pv": 2, "tick": 0.25, "comm": 1.9, "slip_ticks": 2, "max_qty": 90}
A2_DAILY = {"X": [DA("2024-07-01", 100, 101, 99, 100), DA("2024-07-02", 100, 101.3, 99.6, 100.5)]}
A2_MIN = {"X": [M("2024-07-03 13:59", 200, 201, 199, 200), M("2024-07-03 14:00", 200, 200.75, 199.75, 200.5),
                M("2024-07-03 14:01", 200.5, 202, 200.25, 201.75), M("2024-07-03 14:02", 201.75, 202, 200, 200.25),
                M("2024-07-03 14:03", 200.25, 200.5, 199, 199.5)]}
A2_SET = dict(A_SET, entry="10:00", trail_mult=1)


def a2_expected():
    t = at("X", "2024-07-03", "long", 200.5, 200.25, 199.0, 1.5, "stop", False, -0.25, -0.75, 8, 47.2, -19.2, 9980.8)
    return {"risk_pct": 0.5, "start": 10000.0, "trades": [t], "skipped": [],
            "days": [aday("2024-07-03", 10000, 9980.8, 10000 - 0.75 * 16 - 15.2)]}


# A3. Two markets on one date sized from the date's opening balance; a gap stop; minutes ending before 15:55;
# a trade under one contract. Risk 1 %, kind fills. B's commission is 10.
# 03-05 A: long, dist 2, 3 contracts; buy 104, stop 102, low 102 -> 102-1 = 101 is below the low -> 102;
# points -2, worst -2, net -66. B: 48-50 short, ATR 8, dist 8, loss for one 9*10+10 = 100; 100/100 -> 1
# (from 10000, not A's 9934). Sell 50-1 = 49, stop 57; next minute opens 58: gap, buy 58+1 = 59 (= high);
# points -10, worst -10, net -110.
# 03-06 A: long again (still the 03-04 bar), 98.24/32 -> 3; buy 101, stop 99; the minutes end at 09:36:
# close at its close 102 (flat), points 1, worst -1, net 24. B: 98.24/100 -> 0: skipped.
A3_SPECS = {"A": S1, "B": dict(S1, comm=10.0)}
A3_DAILY = {"A": [DA("2024-03-01", 100, 101, 99, 100), DA("2024-03-04", 100, 102, 100, 102)],
            "B": [DA("2024-03-01", 50, 51, 49, 50), DA("2024-03-04", 50, 54, 46, 48)]}
A3_MIN = {"A": [M("2024-03-05 14:35", 103, 104, 102, 103), M("2024-03-06 14:35", 100, 101, 100, 101),
                M("2024-03-06 14:36", 101, 102, 100, 102)],
          "B": [M("2024-03-05 14:35", 50, 50, 49, 49), M("2024-03-05 14:36", 58, 59, 57, 58),
                M("2024-03-06 14:35", 48, 49, 47, 48)]}


def a3_expected():
    trades = [at("A", "2024-03-05", "long", 104, 102, 102, 2, "stop", False, -2, -2, 3, 96.0, -66.0, 9934.0),
              at("B", "2024-03-05", "short", 49, 59, 57, 8, "stop", True, -10, -10, 1, 100.0, -110.0, 9824.0),
              at("A", "2024-03-06", "long", 101, 102, 99, 2, "flat", False, 1, -1, 3, 96.0, 24.0, 9848.0)]
    days = [aday("2024-03-05", 10000, 9824, 10000 - 66 - 110), aday("2024-03-06", 9824, 9848, 9824 - 36)]
    skipped = [{"market": "B", "date": "2024-03-06", "side": "short", "reason": "under one contract"}]
    return {"risk_pct": 1, "start": 10000.0, "trades": trades, "skipped": skipped, "days": days}


# A4. The 15:55 flat is a market order with slippage, and is checked before the stop.
# 03-05 reads 03-04: long, dist 2, 3 contracts. 09:35 buys 100+1 = 101, stop 99. 15:55 opens 103: sell
# 103-1 = 102 (its low of 98 is below the stop, but the flat comes first and that minute is not held).
# points 1, worst -1 (the entry minute's low 100), net 30-6 = 24.
A4_MIN = {"A": [M("2024-03-05 14:35", 100, 101, 100, 101), M("2024-03-05 20:55", 103, 104, 98, 103)]}


def a4_expected():
    t = at("A", "2024-03-05", "long", 101, 102, 99, 2, "flat", False, 1, -1, 3, 96.0, 24.0, 10024.0)
    return {"risk_pct": 1, "start": 10000.0, "trades": [t], "skipped": [],
            "days": [aday("2024-03-05", 10000, 10024, 10000 - 30 - 6)]}


# A5. A holiday: trading halts at 13:00 New York and reopens at 18:00 the same date. Nothing is held past 16:00
# (PLAN, version A), so the 18:00 minutes are not part of the trading day: the minutes end at 12:59 and the
# trade closes at its close 103, no slippage, reason flat. Long, dist 2, 3 contracts, buy 101, stop 99.
# points 2, worst -1 (the entry minute's low 100), net 60-6 = 54. The 18:00 minute's low of 96 is never seen.
A5_MIN = {"A": [M("2024-03-05 14:35", 100, 101, 100, 101), M("2024-03-05 17:59", 103, 104, 102, 103),
                M("2024-03-05 23:00", 110, 111, 96, 110)]}


def a5_expected():
    t = at("A", "2024-03-05", "long", 101, 103, 99, 2, "flat", False, 2, -1, 3, 96.0, 54.0, 10054.0)
    return {"risk_pct": 1, "start": 10000.0, "trades": [t], "skipped": [],
            "days": [aday("2024-03-05", 10000, 10054, 10000 - 30 - 6)]}


class SamedayCleanTests(unittest.TestCase):
    def test_a5_holiday_halt_closes_at_the_last_minute_before_16(self):
        self.assertEqual(rule_check.check_sameday(a5_expected(), A5_MIN, {"A": A3_DAILY["A"]}, {"A": S1}, A_SET,
                                                  "kind"), [])

    def test_a4_flat_with_slippage_before_the_stop(self):
        self.assertEqual(rule_check.check_sameday(a4_expected(), A4_MIN, {"A": A3_DAILY["A"]}, {"A": S1}, A_SET,
                                                  "kind"), [])

    def test_a1_kind(self):
        self.assertEqual(rule_check.check_sameday(a1_expected("kind"), A1_MIN, A1_DAILY, {"X": S1}, A_SET, "kind"), [])

    def test_a1_midpoint(self):
        self.assertEqual(rule_check.check_sameday(a1_expected("midpoint"), A1_MIN, A1_DAILY, {"X": S1}, A_SET,
                                                  "midpoint"), [])

    def test_a2_summer_time_trail_and_ticks(self):
        self.assertEqual(rule_check.check_sameday(a2_expected(), A2_MIN, A2_DAILY, {"X": MNQ}, A2_SET, "midpoint"), [])

    def test_a3_two_markets(self):
        self.assertEqual(rule_check.check_sameday(a3_expected(), A3_MIN, A3_DAILY, A3_SPECS, A_SET, "kind"), [])


class SamedayBreakTests(unittest.TestCase):
    def run_a3(self, r):
        return rule_check.check_sameday(r, A3_MIN, A3_DAILY, A3_SPECS, A_SET, "kind")

    def assertBreak(self, breaks, word):
        self.assertTrue(breaks, "expected a break")
        self.assertTrue(any(word in b for b in breaks), f"no break mentions {word!r}: {breaks}")

    def test_wrong_side(self):
        r = a3_expected()
        r["trades"][1]["side"] = "long"
        self.assertBreak(self.run_a3(r), "side")

    def test_wrong_qty(self):
        r = a3_expected()
        r["trades"][0]["qty"] = 2
        self.assertBreak(self.run_a3(r), "qty")

    def test_wrong_exit(self):
        r = a3_expected()
        r["trades"][1]["exit"] = 58
        self.assertBreak(self.run_a3(r), "exit")

    def test_wrong_net(self):
        r = a3_expected()
        r["trades"][2]["net"] = 24.5
        self.assertBreak(self.run_a3(r), "net")

    def test_missing_trade(self):
        r = a3_expected()
        del r["trades"][1]
        self.assertBreak(self.run_a3(r), "missing")

    def test_extra_trade(self):
        r = a3_expected()
        r["trades"].append(at("B", "2024-03-06", "short", 47, 48, 55, 8, "flat", False, -1, -2, 1, 100.0,
                              -20.0, 9828.0))
        self.assertBreak(self.run_a3(r), "extra")

    def test_wrong_worst_and_day_low(self):
        r = a3_expected()
        r["trades"][2]["worst"] = 0
        self.assertBreak(self.run_a3(r), "worst")
        r = a3_expected()
        r["days"][1]["low"] = 9824.0
        self.assertBreak(self.run_a3(r), "low")

    def test_missing_skip(self):
        r = a3_expected()
        r["skipped"] = []
        self.assertBreak(self.run_a3(r), "skip")

    def test_wrong_entry_price(self):
        r = copy.deepcopy(a2_expected())
        r["trades"][0]["entry"] = 200.5 + 0.25
        self.assertBreak(rule_check.check_sameday(r, A2_MIN, A2_DAILY, {"X": MNQ}, A2_SET, "midpoint"), "entry")


class HelperTests(unittest.TestCase):
    def test_stop_fills_short_mirror(self):
        # short, stop 105, bar high 108 low 100 open 102: reference 105. Kind 105+1 = 106; midpoint of 105 and
        # 108 = 106.5 rounded up to 107; harsh 108. Opening at 106 is a gap: reference 106.
        f = rule_check._stop_fill
        self.assertEqual(f(102, 108, 100, 105, -1, 1.0, 1.0, "kind"), (106, False))
        self.assertEqual(f(102, 108, 100, 105, -1, 1.0, 1.0, "midpoint"), (107, False))
        self.assertEqual(f(102, 108, 100, 105, -1, 1.0, 1.0, "harsh-stops"), (108, False))
        self.assertEqual(f(106, 108, 100, 105, -1, 1.0, 1.0, "kind"), (107, True))
        self.assertIsNone(f(102, 104, 100, 105, -1, 1.0, 1.0, "kind"))
        # long, stop 103, low 100: midpoint 101.5 rounds DOWN to 101 (not to the nearer 102)
        self.assertEqual(f(104, 105, 100, 103, 1, 1.0, 1.0, "midpoint"), (101, False))
        # short, stop 103, high 106: midpoint 104.5 rounds UP to 105
        self.assertEqual(f(102, 106, 101, 103, -1, 1.0, 1.0, "midpoint"), (105, False))

    def test_size_rounds_down_and_caps(self):
        self.assertEqual(rule_check._size(10000, 1, 2, S1)[0], 3)          # 100 / 32
        self.assertEqual(rule_check._size(10000, 50, 2, S1)[0], 90)        # 5000 / 32 = 156, cap 90
        self.assertEqual(rule_check._size(3000, 1, 2, S1)[0], 0)           # 30 / 32

    def test_stop_distance_at_least_one_tick(self):
        adj = bars([(0, 100, 100.2, 100, 100.1)])
        self.assertEqual(rule_check._dist(adj, 0, 1, 1, 1.0), 1.0)


if __name__ == "__main__":
    unittest.main()
