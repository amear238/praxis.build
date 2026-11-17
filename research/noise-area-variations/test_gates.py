#!/usr/bin/env python3
"""Tests for gates.py and run_all.py. Run: python3 -I -B research/noise-area-variations/test_gates.py

The bars are tested on hand-built trade lists and day dicts. rule_check is tested on engine results from
small hand-built days with a hand-set band (test_engine's helpers: upper 99, lower 60, VWAP 80, anchor
price 79, width 40), each tampered one way, and on random-walk days with the real band, where it must
find nothing. run_all is tested in a temporary git repository on synthetic days. Nothing here reads the
real data file.
"""
import copy
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bands as bd         # noqa: E402
import engine as en        # noqa: E402
import gates               # noqa: E402
import globex as g         # noqa: E402
import run_all as ra       # noqa: E402
import test_bands as tb    # noqa: E402
import test_engine as te   # noqa: E402

D = te.D                                   # Wednesday 2024-03-06
D2 = D + dt.timedelta(days=1)              # Thursday 2024-03-07
STAMP = te.stamp


def weekdays(first, n):
    out, d = [], dt.date.fromisoformat(first)
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d += dt.timedelta(days=1)
    return out


def trade(date, net, r, reason="flat", planned=100.0):
    return {"date": date, "side": "long", "qty": 1, "entry_dt": date + " 10:01:00", "entry": 100.0,
            "exit_dt": date + " 15:00:00", "exit": 100.0, "stop_initial": 50.0, "dist": 50.0,
            "planned_cost": planned, "reason": reason, "gap": False, "net": net, "r": r, "balance": 0.0}


def result(trades, dates=None, start=50000.0, breaks=(), skipped=()):
    """An engine-shaped result: day dicts from the trades' nets (the day's low is its end or its start)."""
    dates = dates or sorted({t["date"] for t in trades})
    bal, days = start, []
    for d in dates:
        s = bal
        bal = round(bal + sum(t["net"] for t in trades if t["date"] == d), 2)
        days.append({"date": d, "start": s, "end": bal, "low": min(s, bal)})
    out = {"settings": {}, "fill": "harsh-stops", "start": start, "trades": trades, "days": days,
           "skipped": list(skipped), "digest": "x"}
    if breaks is not None:
        out["rule_breaks"] = list(breaks)
    return out


def shuffle(crossed, runs=10000):
    """A stand-in result of shuffled(): its "pct" is rounded to 0.1, as the real one's is."""
    return {"runs": runs, "crossed": crossed, "pct": round(100.0 * crossed / runs, 1)}


def judged(res, dates, crossed=0):
    with mock.patch.object(gates, "shuffled", return_value=shuffle(crossed)):
        return gates.judge(res, dates)


# ---------------------------------------------------------------------------------------------- the bars
class TwoToOne(unittest.TestCase):
    def test_two_to_one_boundary(self):
        dates = weekdays("2024-02-01", 3)
        tr = [trade(dates[0], 150.0, 1.5), trade(dates[1], 250.0, 2.5), trade(dates[2], -100.0, -1.0, "stop")]
        j = judged(result(tr), dates)["two_to_one"]
        self.assertEqual(j, {"pass": True, "avg_winner_r": 2.0, "later_avg_winner_r": 2.0, "later_net": 300.0})
        tr[1] = trade(dates[1], 240.0, 2.4)
        j = judged(result(tr), dates)["two_to_one"]
        self.assertFalse(j["pass"])
        self.assertAlmostEqual(j["avg_winner_r"], 1.95, places=12)
        # A trade with net 0 is not a winner.
        tr = [trade(dates[0], 250.0, 2.5), trade(dates[1], 0.0, 0.0)]
        self.assertEqual(judged(result(tr), dates)["two_to_one"]["avg_winner_r"], 2.5)
        # No winners: 0.0 and a fail.
        j = judged(result([trade(dates[0], -100.0, -1.0, "stop")]), dates)["two_to_one"]
        self.assertEqual((j["pass"], j["avg_winner_r"], j["later_avg_winner_r"]), (False, 0.0, 0.0))

    def test_two_to_one_needs_later_years(self):
        self.assertEqual(gates.LATER_FROM, "2024-01-01")
        early, later = weekdays("2023-12-28", 2), weekdays("2024-01-01", 3)    # 2023-12-28, 2023-12-29
        dates = early + later
        # Full average 2.5, later winners 1.8: fail.
        tr = [trade(early[0], 320.0, 3.2), trade(later[0], 180.0, 1.8)]
        j = judged(result(tr), dates)["two_to_one"]
        self.assertAlmostEqual(j["avg_winner_r"], 2.5, places=12)
        self.assertAlmostEqual(j["later_avg_winner_r"], 1.8, places=12)
        self.assertEqual(j["later_net"], 180.0)
        self.assertFalse(j["pass"])
        # Later winners 2.5 but the later years lose money: fail; exactly 0 also fails.
        tr = [trade(early[0], 320.0, 3.2), trade(later[0], 250.0, 2.5), trade(later[1], -300.0, -3.0, "stop")]
        j = judged(result(tr), dates)["two_to_one"]
        self.assertEqual((j["later_net"], j["pass"]), (-50.0, False))
        tr[2] = trade(later[1], -250.0, -2.5, "stop")
        j = judged(result(tr), dates)["two_to_one"]
        self.assertEqual((j["later_net"], j["pass"]), (0.0, False))
        tr[2] = trade(later[1], -249.99, -2.4999, "stop")
        self.assertTrue(judged(result(tr), dates)["two_to_one"]["pass"])
        # No trade from 2024 on: fail.
        j = judged(result([trade(early[0], 320.0, 3.2)]), dates)["two_to_one"]
        self.assertEqual((j["later_avg_winner_r"], j["later_net"], j["pass"]), (0.0, 0.0, False))


class Frequency(unittest.TestCase):
    def test_frequency_boundary(self):
        dates = weekdays("2024-03-01", 20)
        tr = [trade(d, 10.0, 0.1) for i, d in enumerate(dates) if not 1 <= i <= 7]
        f = judged(result(tr, dates), dates)["frequency"]
        self.assertEqual(f, {"pass": True, "max_gap_trading_days": 7, "gap_from": dates[1], "gap_to": dates[7]})
        tr = [trade(d, 10.0, 0.1) for i, d in enumerate(dates) if not 1 <= i <= 8]
        f = judged(result(tr, dates), dates)["frequency"]
        self.assertEqual(f, {"pass": False, "max_gap_trading_days": 8, "gap_from": dates[1], "gap_to": dates[8]})
        # Two trades on one day count as one day; the longest gap is the one reported.
        tr = [trade(dates[0], 10.0, 0.1), trade(dates[0], 10.0, 0.1), trade(dates[3], 10.0, 0.1)] + \
             [trade(d, 10.0, 0.1) for d in dates[13:]]
        f = judged(result(tr, dates), dates)["frequency"]
        self.assertEqual((f["max_gap_trading_days"], f["gap_from"], f["gap_to"]), (9, dates[4], dates[12]))
        # Every day has an entry: no gap.
        f = judged(result([trade(d, 10.0, 0.1) for d in dates], dates), dates)["frequency"]
        self.assertEqual(f, {"pass": True, "max_gap_trading_days": 0, "gap_from": None, "gap_to": None})

    def test_frequency_counts_start_and_end(self):
        dates = weekdays("2024-03-01", 20)
        skips = [{"date": d, "decision_dt": d + " 10:00:00", "side": "long", "reason": "under one contract"}
                 for d in dates[:8]]
        tr = [trade(d, 10.0, 0.1) for d in dates[8:]]
        f = judged(result(tr, dates, skipped=skips), dates)["frequency"]     # a skip is not an entry
        self.assertEqual(f, {"pass": False, "max_gap_trading_days": 8, "gap_from": dates[0], "gap_to": dates[7]})
        tr = [trade(d, 10.0, 0.1) for d in dates[:12]]
        f = judged(result(tr, dates), dates)["frequency"]
        self.assertEqual(f, {"pass": False, "max_gap_trading_days": 8, "gap_from": dates[12], "gap_to": dates[19]})
        tr = [trade(d, 10.0, 0.1) for d in dates[7:13]]
        self.assertEqual(judged(result(tr, dates), dates)["frequency"]["max_gap_trading_days"], 7)
        f = judged(result([], dates), dates)["frequency"]
        self.assertEqual(f, {"pass": False, "max_gap_trading_days": 20, "gap_from": dates[0], "gap_to": dates[19]})


class Profit(unittest.TestCase):
    def test_profit_boundary(self):
        dates = weekdays("2024-03-01", 3)
        tr = [trade(d, 1333.33, 13.3333) for d in dates]
        self.assertEqual(judged(result(tr), dates)["profit"], {"pass": False, "net": 3999.99})
        tr[2] = trade(dates[2], 1333.34, 13.3334)
        self.assertEqual(judged(result(tr), dates)["profit"], {"pass": True, "net": 4000.0})


class Survival(unittest.TestCase):
    def test_survival_real_cross_fails(self):
        dates = weekdays("2024-03-01", 3)
        res = result([trade(d, 10.0, 0.1) for d in dates])
        res["days"][1]["low"] = res["days"][1]["start"] - 2000.0      # 50,010 high: the floor is 48,010
        s = judged(res, dates, crossed=0)["survival"]
        self.assertEqual(s, {"pass": False, "first_cross": dates[1], "shuffle_pct": 0.0})
        res["days"][1]["low"] = res["days"][1]["start"] - 1999.99
        self.assertEqual(judged(res, dates, crossed=0)["survival"], {"pass": True, "first_cross": None,
                                                                     "shuffle_pct": 0.0})

    def test_survival_boundary(self):
        dates = weekdays("2024-03-01", 3)
        res = result([trade(d, 10.0, 0.1) for d in dates], start=10000.0)
        with mock.patch.object(gates, "shuffled", return_value=shuffle(500)) as sh:
            s = gates.judge(res, dates)["survival"]
        self.assertEqual(s, {"pass": True, "first_cross": None, "shuffle_pct": 5.0})
        sh.assert_called_once_with(res["days"], runs=10000, seed=20261115, start=10000.0, limit=2000.0)
        # 501 and 502 crossings: "pct" rounds 5.02 to 5.0, the bar does not.
        self.assertEqual(judged(res, dates, crossed=501)["survival"], {"pass": False, "first_cross": None,
                                                                       "shuffle_pct": 5.01})
        s = judged(res, dates, crossed=502)["survival"]
        self.assertEqual((s["pass"], s["shuffle_pct"]), (False, 100.0 * 502 / 10000))
        # The bar reads "crossed" and "runs", not the rounded "pct".
        with mock.patch.object(gates, "shuffled", return_value={"runs": 200, "crossed": 10, "pct": 99.0}):
            self.assertTrue(gates.judge(res, dates)["survival"]["pass"])
        with mock.patch.object(gates, "shuffled", return_value={"runs": 200, "crossed": 11, "pct": 0.0}):
            self.assertFalse(gates.judge(res, dates)["survival"]["pass"])

    def test_uses_the_candidate_1_functions(self):
        path = os.path.join(os.path.dirname(HERE), "intraday-momentum-long", "run.py")
        self.assertEqual(os.path.realpath(gates.shuffled.__code__.co_filename), os.path.realpath(path))
        self.assertEqual(os.path.realpath(gates.trailing.__code__.co_filename), os.path.realpath(path))
        # The real shuffle: every day loses 700, so every order crosses on the third day.
        dates = weekdays("2024-03-01", 5)
        res = result([trade(d, -700.0, -7.0, "stop") for d in dates])
        s = gates.judge(res, dates)["survival"]
        self.assertEqual(s, {"pass": False, "first_cross": dates[2], "shuffle_pct": 100.0})


class Overall(unittest.TestCase):
    def passing(self):
        dates = weekdays("2023-12-01", 30)
        tr = []
        for i, d in enumerate(dates):
            tr.append(trade(d, 500.0, 2.5) if i % 2 == 0 else trade(d, -100.0, -1.0, "stop"))
        return result(tr, dates), dates

    def test_overall_needs_all(self):
        res, dates = self.passing()
        j = judged(res, dates)
        bars = ("rule_check", "two_to_one", "frequency", "profit", "survival")
        self.assertEqual([j[k]["pass"] for k in bars], [True] * 5)
        self.assertTrue(j["overall"])
        self.assertEqual(j["rule_check"], {"pass": True, "breaks": 0})

        def fails(res, crossed=0):
            j = judged(res, dates, crossed)
            return [k for k in bars if not j[k]["pass"]], j["overall"]

        r = copy.deepcopy(res)
        r["rule_breaks"] = ["one", "two"]
        self.assertEqual(fails(r), (["rule_check"], False))
        self.assertEqual(judged(r, dates)["rule_check"], {"pass": False, "breaks": 2})
        r = copy.deepcopy(res)
        del r["rule_breaks"]                               # never checked: a fail
        self.assertEqual(judged(r, dates)["rule_check"], {"pass": False, "breaks": -1})
        self.assertEqual(fails(r), (["rule_check"], False))
        r = copy.deepcopy(res)
        for t in r["trades"]:
            if t["net"] > 0:
                t["r"] = 1.9
        self.assertEqual(fails(r), (["two_to_one"], False))
        r = copy.deepcopy(res)
        r["trades"] = [t for t in r["trades"] if not dates[3] <= t["date"] <= dates[10]]
        r["days"] = result(r["trades"], dates)["days"]
        self.assertEqual(fails(r), (["frequency"], False))
        r = copy.deepcopy(res)
        for t in r["trades"]:
            if t["net"] < 0:
                t["net"] = -350.0
        r["days"] = result(r["trades"], dates)["days"]       # net 7,500 - 5,250; from 2024: 2,000 - 1,750
        self.assertEqual(fails(r), (["profit"], False))
        self.assertEqual(fails(res, crossed=501), (["survival"], False))


class Stats(unittest.TestCase):
    def test_stats(self):
        dates = ["2023-01-03", "2023-01-04", "2023-01-05", "2024-01-02", "2024-01-03"]
        tr = [trade(dates[0], 300.0, 3.0), trade(dates[1], -180.0, -1.8, "exit"),
              trade(dates[2], -150.0, -1.5, "stop"), trade(dates[3], 250.0, 2.5),
              trade(dates[4], -100.01, -1.0001, "stop")]
        tr[2]["gap"] = True
        res = result(tr, dates, skipped=[{"date": dates[0]}, {"date": dates[3]}])
        res["days"] = [{"date": dates[0], "start": 50000.0, "end": 50300.0, "low": 50000.0},
                       {"date": dates[1], "start": 50300.0, "end": 50200.0, "low": 50200.0},
                       {"date": dates[2], "start": 50200.0, "end": 50050.0, "low": 50000.0},
                       {"date": dates[3], "start": 50050.0, "end": 50300.0, "low": 49900.0},
                       {"date": dates[4], "start": 50300.0, "end": 50199.99, "low": 50199.99}]
        st = judged(res, dates)["stats"]
        self.assertEqual(st, {
            "trades": 5, "win_pct": 40.0, "avg_winner_dollars": 275.0, "avg_loser_dollars": -143.34,
            "avg_loser_r": -1.433, "longest_losing_run": 2, "worst_drop_dollars": 400.0, "skipped": 2,
            "stops_over_planned": 2, "worst_stop_vs_planned": 1.8,       # any reason; 100.01 is not over
            "by_year": {"2023": {"trades": 3, "net": -30.0, "win_pct": 33.3, "avg_winner_r": 3.0},
                        "2024": {"trades": 2, "net": 149.99, "win_pct": 50.0, "avg_winner_r": 2.5}}})
        st = judged(result([], dates), dates)["stats"]
        self.assertEqual((st["trades"], st["win_pct"], st["avg_winner_dollars"], st["worst_stop_vs_planned"],
                          st["longest_losing_run"], st["by_year"]), (0, 0.0, 0.0, None, 0, {}))


# ---------------------------------------------------------------------------------------------- rule check
STD_BANDS = te.fake_bands(lambda date, sm: te.STD)
LATER = {"10:15": (101.5, 101.5, 70, 75), "10:30": (75, 100, 75, 100), "10:31": (101, 102, 100.5, 101.5)}


def check(res, days, spec=None):
    with mock.patch.object(bd, "day_bands", te.fake_bands(spec) if spec else STD_BANDS):
        return gates.rule_check(res, days)


def hand_days():
    """Day 1: one long held to the flat. Day 2: a long stopped at 10:15, then a long at 10:31 held to the flat."""
    return [te.build_day(D, te.UP_FLAT), te.build_day(D2, dict(te.UP_FLAT, **LATER))]


def holed(day, first, last):
    out = g.Day(day.date)
    for b in day.bars:
        if not (g.sm_of(first) <= b.sm <= g.sm_of(last)):
            out.by_sm[b.sm] = len(out.bars)
            out.bars.append(b)
    return out


def with_bar(day, hhmm, ohlc):
    out = tb.copy_day(day)
    i = out.by_sm[g.sm_of(hhmm)]
    b = out.bars[i]
    out.bars[i] = g.Bar(b.dt, b.sm, *[float(x) for x in ohlc], b.v)
    return out


class RuleCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.days = hand_days()
        cls.kind = te.run(cls.days, fill="kind")
        cls.harsh = te.run(cls.days, fill="harsh-stops")

    def test_hand_results(self):
        t = self.kind["trades"]
        self.assertEqual([(x["date"], x["reason"], x["entry_dt"], x["exit"]) for x in t],
                         [("2024-03-06", "flat", STAMP(D, "10:01"), 101.0), ("2024-03-07", "stop", STAMP(D2, "10:01"), 81.0),
                          ("2024-03-07", "flat", STAMP(D2, "10:31"), 101.0)])
        self.assertEqual(check(self.kind, self.days), [])
        self.assertEqual(check(self.harsh, self.days), [])
        self.assertEqual(self.harsh["trades"][1]["exit"], 70.0)

    def caught(self, res, phrase, days=None, spec=None, n=None):
        breaks = check(res, days or self.days, spec)
        hits = [b for b in breaks if phrase in b]
        self.assertTrue(hits, "%r not in %r" % (phrase, breaks))
        if n is not None:
            self.assertEqual(len(hits), n, breaks)
        return breaks

    def tampered(self, i, base=None, **change):
        res = copy.deepcopy(base or self.kind)
        res["trades"][i].update(change)
        return res

    def with_settings(self, base=None, **change):
        res = copy.deepcopy(base or self.kind)
        res["settings"].update(change)
        return res

    def test_rule_check_catches(self):
        t0 = self.kind["trades"][0]
        # The breaks the plan lists.
        self.caught(self.tampered(0, stop_initial=None), "no stop at entry")
        self.caught(self.tampered(0, dist=None, stop_initial=None), "no stop at entry")
        self.caught(self.tampered(0, stop_initial=t0["stop_initial"] - 1.0), "stop_initial is not dist from the entry")
        # A bar between entry and exit whose low reached the stop (81.5) without a stop exit.
        day1 = with_bar(self.days[0], "12:00", (101.5, 101.5, 81.5, 101.5))
        b = self.caught(self.kind, "reached the stop before the exit", days=[day1, self.days[1]], n=1)
        self.assertIn(STAMP(D, "12:00"), " ".join(b))
        self.caught(self.tampered(1, exit_dt=STAMP(D2, "10:16")), "reached the stop before the exit")
        self.caught(self.tampered(1, exit_dt=STAMP(D2, "10:14")), "did not reach the stop")
        # kind: a loss above the planned cost by more than a cent, without a gap, whatever the reason.
        t1 = self.kind["trades"][1]
        self.caught(self.tampered(1, net=t1["net"] - 0.02), "loss above the planned cost")
        breaks = check(self.tampered(1, net=t1["net"] - 0.01), self.days)
        self.assertFalse([x for x in breaks if "loss above the planned cost" in x], breaks)
        breaks = check(self.tampered(1, net=t1["net"] - 0.02, gap=True), self.days)
        self.assertFalse([x for x in breaks if "loss above the planned cost" in x], breaks)
        self.assertFalse([x for x in check(self.harsh, self.days) if "loss above the planned cost" in x])
        self.caught(self.tampered(0, net=-t0["planned_cost"] - 0.02), "loss above the planned cost (reason flat)")
        # Size: qty and planned cost for the balance before the trade.
        self.caught(self.tampered(0, qty=12), "qty does not match the size rule")
        self.caught(self.tampered(0, planned_cost=t0["planned_cost"] + 0.5), "planned_cost does not match the size rule")
        r = copy.deepcopy(self.kind)
        r["start"] = 47000.0
        self.caught(r, "qty does not match the size rule")
        # Entry window, flat time, most trades a day.
        self.caught(self.with_settings(entry_window=["10:30", "15:30"]), "entry outside entry_window", n=2)
        self.caught(self.with_settings(entry_window=["09:31", "10:00"], flat_time="10:00"),
                    "entry at or after flat_time", n=3)
        self.caught(self.with_settings(max_trades_per_day=1), "over max_trades_per_day", n=1)
        # An exit after the bar stamped 16:00.
        self.caught(self.tampered(0, exit_dt="2024-03-06 16:05:00"), "exit after the 16:00 bar")

    def test_rule_check_catches_more(self):
        t0 = self.kind["trades"][0]
        # The entry signal: the decision close must be beyond the band on the trade's side, on a decision bar,
        # on a side `sides` allows.
        day1 = with_bar(self.days[0], "10:00", (80, 95, 80, 95))
        self.caught(self.kind, "entry signal not true at the decision bar", days=[day1, self.days[1]], n=1)
        self.caught(self.with_settings(sides="short"), "side not allowed by sides", n=3)
        self.caught(self.kind, "no band at the decision bar",
                    spec=lambda date, sm: None if sm == g.sm_of("10:00") else te.STD)
        minute = te.run([te.build_day(D, {"10:07": (80, 100, 80, 100), "10:08": (101, 102, 100.5, 101.5)})],
                        cadence="minute")
        self.assertEqual(check(minute, [te.build_day(D, {"10:07": (80, 100, 80, 100), "10:08": (101, 102, 100.5, 101.5)})]), [])
        minute["settings"]["cadence"] = "half_hour"
        self.caught(minute, "decision bar not on the half-hour cadence",
                    days=[te.build_day(D, {"10:07": (80, 100, 80, 100), "10:08": (101, 102, 100.5, 101.5)})])
        # dist: the stop kind's distance at the decision bar, rounded down to a tick; never under 10.
        self.caught(self.tampered(0, dist=20.25, stop_initial=t0["entry"] - 20.25),
                    "dist does not match the stop distance at the decision bar")
        self.caught(self.with_settings(stop={"kind": "full_width"}),
                    "dist does not match the stop distance at the decision bar")
        self.caught(self.tampered(0, dist=9.75, stop_initial=t0["entry"] - 9.75), "dist under 10 points")
        # Entry fill.
        self.caught(self.tampered(0, entry=101.75, stop_initial=81.75), "entry fill is not the entry bar's open")
        # A trade open across the end of the day's tradable bars (a hole from 14:01 to 15:30).
        day1 = holed(self.days[0], "14:01", "15:30")
        self.caught(self.kind, "open across the end of the day's tradable bars", days=[day1, self.days[1]], n=1)
        # Exit price, reason, net, r and balance.
        self.caught(self.tampered(0, exit=101.25), "exit does not match the rules")
        self.caught(self.tampered(0, reason="exit"), "exit does not match the rules")
        self.caught(self.tampered(1, exit=81.5), "exit does not match the rules")
        self.caught(self.tampered(1, gap=True), "exit does not match the rules")
        self.caught(self.tampered(0, net=t0["net"] + 1.0), "net does not match")
        self.caught(self.tampered(0, r=t0["r"] + 0.001), "r does not match")
        self.caught(self.tampered(0, balance=t0["balance"] + 1.0), "balance does not match")
        # The day dicts the survival bar reads.
        for key in ("start", "end", "low"):
            r = copy.deepcopy(self.kind)
            r["days"][1][key] -= 0.01
            self.caught(r, "day 2024-03-07: %s" % key, n=1)
        r = copy.deepcopy(self.kind)
        r["days"] = r["days"][:1]
        self.caught(r, "not one entry per loaded day")
        # Day 1's low: the long of 11 from 101.5 marked at a 90 low (test_engine's hand value, 49,726.10).
        day1 = with_bar(self.days[0], "10:10", (101.5, 101.5, 90, 101.5))
        res = te.run([day1, self.days[1]])
        self.assertEqual(res["days"][0]["low"], 49726.1)
        self.assertEqual(check(res, [day1, self.days[1]]), [])
        self.caught(res, "day 2024-03-06: low", days=self.days, n=1)
        # Positions: one at a time, no entry on the side already held.
        self.caught(self.tampered(1, exit_dt=STAMP(D2, "10:45")), "entered while already on that side")
        # The trade's day must be a loaded day with that entry bar.
        self.caught(self.tampered(0, date="2024-03-08"), "not a loaded day")
        self.caught(self.tampered(0, entry_dt="2024-03-06 09:00:00"), "entry not at a tradable bar")

    def test_trail_is_replayed(self):
        marks = dict(te.UP, **{"10:05": (101.5, 120, 101.5, 119), "10:06": (119, 119, 104, 105),
                               "10:07": (105, 105, 97, 100)})
        days = [te.build_day(D, marks)]
        res = te.run(days, exit={"kind": "trail_r", "value": 1.0}, max_trades_per_day=1)
        self.assertEqual((res["trades"][0]["reason"], res["trades"][0]["exit"]), ("stop", 99.5))
        self.assertEqual(check(res, days), [])
        # Without the trail the 81.5 stop is never reached: the stop exit at 10:07 breaks the rule.
        res["settings"]["exit"] = {"kind": "hold_to_flat"}
        self.caught(res, "did not reach the stop", days=days)

    def test_gap_on_decided_exits(self):
        # The 10:30 close of 95 decides the exit; the 10:31 bar opens at 80, already below the 81.5 stop.
        days = [te.build_day(D, dict(te.UP, **{"10:30": (101.5, 101.5, 95, 95), "10:31": (80, 81, 79, 80)}))]
        res = te.run(days, max_trades_per_day=1)
        t = res["trades"][0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("exit", 79.5, True))
        self.assertLess(t["net"], -t["planned_cost"] - 0.01)
        self.assertEqual(check(res, days), [])
        bad = self.tampered(0, base=res, gap=False)
        self.caught(bad, "exit does not match the rules", days=days)
        self.caught(bad, "loss above the planned cost (reason exit)", days=days)
        # A trailed stop: 120 - 20 = 100 from 10:05; the flat fill at the 16:00 open of 99 is past it (not past
        # the initial 81.5).
        marks = dict(te.UP, **{"10:05": (101.5, 120, 101.5, 119), "16:00": (99, 99.5, 98, 99)})
        days = [te.build_day(D, marks)]
        res = te.run(days, exit={"kind": "trail_r", "value": 1.0}, max_trades_per_day=1)
        t = res["trades"][0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("flat", 98.5, True))
        self.assertEqual(check(res, days), [])
        self.caught(self.tampered(0, base=res, gap=False), "exit does not match the rules", days=days)
        res["settings"]["exit"] = {"kind": "hold_to_flat"}          # no trail: the open is not past 81.5
        self.caught(res, "exit does not match the rules", days=days)

    def test_entry_bar_before_flat_and_not_last(self):
        # The entry bar (10:01) stamped at flat_time: a break, though the decision bar (10:00) is before it.
        self.caught(self.with_settings(entry_window=["09:31", "10:00"], flat_time="10:01"),
                    "entry at or after flat_time", n=3)
        # The entry bar is the day's last tradable bar (a hole from 10:02 to 15:59 ends day 1 at 10:01).
        day1 = holed(self.days[0], "10:02", "15:59")
        self.assertEqual(g.tradable_end(day1), day1.by_sm[g.sm_of("10:01")])
        self.caught(self.kind, "entry on the day's last tradable bar", days=[day1, self.days[1]], n=1)
        # The engine itself places neither.
        self.assertEqual(te.run([day1], max_trades_per_day=1)["trades"], [])
        r = te.run(self.days, entry_window=["09:31", "10:00"], flat_time="10:01")
        self.assertEqual(r["trades"], [])

    def test_stop_bar_is_no_decision_bar(self):
        days = [te.build_day(D, dict(te.UP, **{"10:30": (101, 101, 50, 55)}))]
        res = te.run(days)
        self.assertEqual([x["reason"] for x in res["trades"]], ["stop", "flat"])
        self.assertEqual(check(res, days), [])
        bad = copy.deepcopy(res)
        bad["trades"][1]["entry_dt"] = STAMP(D, "10:31")
        self.caught(bad, "decided on a bar where a stop filled", days=days)

    def test_fresh_reentry(self):
        # Day 2's second long comes after a stop at 10:15 with no decision bar closing inside the band.
        self.caught(self.with_settings(reentry="fresh"), "reentry fresh", n=1)
        # The engine's own fresh case is clean.
        marks = dict(te.UP, **{"10:15": (101.5, 102, 81, 100), "10:31": (101, 102, 100.5, 101.5),
                               "11:00": (101.5, 101.5, 95, 95), "11:30": (95, 100, 95, 100),
                               "11:31": (101, 102, 100.5, 101.5)})
        days = [te.build_day(D, marks)]
        res = te.run(days, reentry="fresh")
        self.assertEqual(len(res["trades"]), 2)
        self.assertEqual(check(res, days), [])
        res_any = te.run(days, reentry="any")
        self.assertEqual(len(res_any["trades"]), 3)
        res_any["settings"]["reentry"] = "fresh"
        self.caught(res_any, "reentry fresh", days=days, n=1)
        # The written rule: a decided exit's own decision bar counts. The 10:30 close of 95 decides the exit
        # and is inside the band, so the 11:01 long is allowed under fresh.
        marks = dict(te.UP, **{"10:30": (101.5, 101.5, 95, 95), "11:00": (95, 100, 95, 100),
                               "11:01": (101, 102, 100.5, 101.5)})
        days = [te.build_day(D, marks)]
        res_any = te.run(days, reentry="any")
        self.assertEqual([x["entry_dt"] for x in res_any["trades"]], [STAMP(D, "10:01"), STAMP(D, "11:01")])
        res_any["settings"]["reentry"] = "fresh"
        self.assertEqual(check(res_any, days), [])

    def test_clean_on_hand_cases(self):
        # A gap through the stop, on both fills; a reverse; a short stop.
        cases = [([te.build_day(D, dict(te.UP, **{"10:15": (76.5, 77, 70, 75)}))], {}),
                 ([te.build_day(D, dict(te.UP, **{"11:00": (95, 95, 55, 55), "11:01": (55, 56, 54, 55)}))],
                  dict(stop={"kind": "width_frac", "value": 2.0}, exit={"kind": "hold_to_flat"})),
                 ([te.build_day(D, {"10:00": (80, 80, 50, 50), "10:01": (49, 49.5, 48, 48.5),
                                    "10:15": (48.5, 75, 48.5, 70)})], {})]
        seen = []
        for days, over in cases:
            for fill in ("kind", "harsh-stops"):
                res = te.run(days, fill=fill, **over)
                seen.extend((t["side"], t["reason"], t["gap"]) for t in res["trades"])
                self.assertEqual(check(res, days), [], (over, fill))
        self.assertIn(("long", "stop", True), seen)
        self.assertIn(("long", "reverse", False), seen)
        self.assertIn(("short", "stop", False), seen)

    def test_clean_on_random_days(self):
        days = tb.random_days(22, seed=20211117)
        extra = [te.settings(exit={"kind": "trail_r", "value": 1.5}, cadence="minute", max_trades_per_day=10,
                               stop={"kind": "width_frac", "value": 0.3}),
                 te.settings(anchor="1800", entry_window=["18:01", "15:30"], cadence="minute", sides="long",
                             reentry="fresh", stop={"kind": "half_width"}, max_trades_per_day=10, risk_pct=0.5),
                 te.settings(anchor="1800", entry_window=["18:01", "15:30"], cadence="minute",
                             exit={"kind": "hold_to_flat"}, stop={"kind": "width_frac", "value": 3.0},
                             max_trades_per_day=10, band_mult=0.25),
                 te.settings(anchor="1800", entry_window=["18:01", "15:30"], exit={"kind": "trail_r", "value": 3.0},
                             stop={"kind": "full_width"}, max_trades_per_day=10, band_mult=0.25)]
        reasons = set()
        for s in te.random_settings() + extra:
            for fill in ("kind", "harsh-stops"):
                res = en.run(days, s, fill=fill)
                reasons.update((t["reason"], t["side"]) for t in res["trades"])
                self.assertEqual(gates.rule_check(res, days), [], (s, fill))
        self.assertEqual(reasons, {(r, side) for r in ("stop", "exit", "reverse", "flat") for side in ("long", "short")})
        # Holes: day 18 loses its bars 11:01 to 13:59; the engine ends that day at 11:00.
        days = days[:18] + [holed(days[18], "11:01", "13:59")] + days[19:]
        for s in te.random_settings():
            res = en.run(days, s, fill="harsh-stops")
            self.assertEqual(gates.rule_check(res, days), [], s)


# ---------------------------------------------------------------------------------------------- run_all
GIT = ["git", "-c", "user.name=test", "-c", "user.email=", "-c", "commit.gpgsign=false", "-c",
       "core.hooksPath=/dev/null"]


def git(repo, *args):
    subprocess.run(GIT + list(args), cwd=repo, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


class RunAll(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.repo = os.path.join(self.tmp, "repo")
        self.vdir = os.path.join(self.repo, "variations")
        self.out = os.path.join(self.tmp, "out")
        os.makedirs(self.vdir)
        git(self.repo, "init", "-q")
        with open(os.path.join(self.repo, "README"), "w") as fh:
            fh.write("x\n")
        git(self.repo, "add", "README")
        git(self.repo, "commit", "-q", "-m", "init")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, name, s):
        with open(os.path.join(self.vdir, name), "w") as fh:
            json.dump(s, fh)

    def commit(self):
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "settings")

    def call(self, days):
        with mock.patch.object(bd, "day_bands", STD_BANDS), mock.patch("sys.stdout"):
            return ra.run_all(self.vdir, self.out, days=days)

    def test_run_all_refuses_uncommitted(self):
        days = hand_days()
        self.assertEqual(self.call(days), 2)                          # no settings file
        self.write("a.json", te.settings(name="a"))
        self.assertEqual(self.call(days), 2)                          # untracked
        self.assertFalse(os.path.exists(self.out))
        self.commit()
        self.write("a.json", te.settings(name="a", risk_pct=0.5))
        self.assertEqual(self.call(days), 2)                          # modified
        git(self.repo, "checkout", "--", "variations/a.json")
        self.write("b.json", te.settings(name="b"))
        self.assertEqual(self.call(days), 2)                          # a second, uncommitted file
        os.remove(os.path.join(self.vdir, "b.json"))
        with open(os.path.join(self.repo, ".gitignore"), "w") as fh:
            fh.write("variations/c.json\n")
        git(self.repo, "add", ".gitignore")
        git(self.repo, "commit", "-q", "-m", "ignore")
        self.write("c.json", te.settings(name="c"))
        self.assertEqual(self.call(days), 2)                          # ignored is not committed either
        os.remove(os.path.join(self.vdir, "c.json"))
        self.assertFalse(os.path.exists(self.out))
        # An invalid settings file, committed: nothing is run.
        self.write("bad.json", te.settings(name="bad", risk_pct=3))
        self.commit()
        self.assertEqual(self.call(days), 2)
        self.assertFalse(os.path.exists(self.out))
        # Not a git repository: refused.
        plain = os.path.join(self.tmp, "plain")
        os.makedirs(plain)
        shutil.copy(os.path.join(self.vdir, "a.json"), plain)
        with mock.patch.object(bd, "day_bands", STD_BANDS), mock.patch("sys.stdout"):
            self.assertEqual(ra.run_all(plain, self.out, days=days), 2)
        self.assertFalse(os.path.exists(self.out))

    def test_run_all_refuses_settings_unlike_the_commit(self):
        days = hand_days()
        self.write("a.json", te.settings(name="a"))
        self.commit()
        path = os.path.join(self.vdir, "a.json")

        def porcelain():
            return subprocess.run(["git", "status", "--porcelain", "--ignored", "--untracked-files=all"],
                                  cwd=self.vdir, stdout=subprocess.PIPE, universal_newlines=True).stdout
        for flag in ("--skip-worktree", "--assume-unchanged"):
            git(self.repo, "update-index", flag, "variations/a.json")
            self.write("a.json", te.settings(name="a", risk_pct=0.5))
            self.assertEqual(porcelain(), "", flag)                # git status does not see the change
            self.assertEqual(self.call(days), 2, flag)
            self.assertFalse(os.path.exists(self.out))
            git(self.repo, "update-index", flag.replace("--", "--no-"), "variations/a.json")
            git(self.repo, "checkout", "--", "variations/a.json")
        # A committed symlink to a file outside the repository.
        outside = os.path.join(self.tmp, "outside.json")
        with open(outside, "w") as fh:
            json.dump(te.settings(name="a"), fh)
        os.remove(path)
        os.symlink(outside, path)
        self.commit()
        self.assertEqual(porcelain(), "")
        self.assertEqual(self.call(days), 2)
        self.assertFalse(os.path.exists(self.out))
        # A name field unlike the file stem.
        os.remove(path)
        self.write("a.json", te.settings(name="b"))
        self.commit()
        self.assertEqual(self.call(days), 2)
        self.assertFalse(os.path.exists(self.out))
        # GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE in the environment are not used.
        self.write("a.json", te.settings(name="a"))
        self.commit()
        bogus = os.path.join(self.tmp, "nowhere")
        with mock.patch.dict(os.environ, {"GIT_DIR": bogus, "GIT_WORK_TREE": bogus, "GIT_INDEX_FILE": bogus}):
            self.assertEqual(self.call(days), 0)

    def test_run_all_clears_old_output(self):
        days = hand_days()
        self.write("a.json", te.settings(name="a"))
        self.commit()
        os.makedirs(os.path.join(self.out, "a"))
        with open(os.path.join(self.out, "a", "stale.json"), "w") as fh:
            fh.write("{}\n")
        self.assertEqual(self.call(days), 0)
        self.assertNotIn("stale.json", os.listdir(os.path.join(self.out, "a")))

    def test_frequency_calendar_starts_with_the_band(self):
        dates = weekdays("2024-03-04", 20)
        days = [te.build_day(dt.date.fromisoformat(d), te.UP_FLAT) for d in dates]
        first = dates[14]                          # a 14-day band: none on the first 14 days
        spec = te.fake_bands(lambda date, sm: te.STD if date >= first else None)
        self.write("a.json", te.settings(name="a", lookback=14))
        self.commit()
        with mock.patch.object(bd, "day_bands", spec), mock.patch("sys.stdout"):
            self.assertEqual(ra.run_all(self.vdir, self.out, days=days), 0)
        with open(os.path.join(self.out, "a", "judge.json")) as fh:
            j = json.load(fh)
        self.assertEqual(j["frequency"], {"pass": True, "max_gap_trading_days": 0, "gap_from": None, "gap_to": None})
        self.assertEqual(j["stats"]["trades"], 6)
        with open(os.path.join(self.out, "a", "harsh-stops-50000.json")) as fh:
            res = json.load(fh)
        self.assertEqual(sorted({t["date"] for t in res["trades"]}), dates[14:])
        # Counted from the first loaded day, the warm-up would be a 14-day gap.
        self.assertEqual(judged(res, dates)["frequency"]["max_gap_trading_days"], 14)
        # A gap at the end of the calendar still counts: no trade on the last 8 days.
        days = [te.build_day(dt.date.fromisoformat(d), te.UP_FLAT if i < 12 else {}) for i, d in enumerate(dates)]
        spec = te.fake_bands(lambda date, sm: te.STD if date >= dates[4] else None)
        with mock.patch.object(bd, "day_bands", spec), mock.patch("sys.stdout"):
            self.assertEqual(ra.run_all(self.vdir, self.out, days=days), 0)
        with open(os.path.join(self.out, "a", "judge.json")) as fh:
            j = json.load(fh)
        self.assertEqual(j["frequency"], {"pass": False, "max_gap_trading_days": 8, "gap_from": dates[12],
                                          "gap_to": dates[19]})

    def test_run_all_writes_results(self):
        days = hand_days()
        self.write("a.json", te.settings(name="a"))
        self.write("b.json", te.settings(name="b", exit={"kind": "hold_to_flat"}, sides="long"))
        with open(os.path.join(self.vdir, "notes.txt"), "w") as fh:
            fh.write("not a settings file\n")
        self.commit()
        self.assertEqual(self.call(days), 0)
        self.assertEqual(sorted(os.listdir(self.out)), ["a", "b"])
        names = ["harsh-stops-10000.json", "harsh-stops-50000.json", "judge.json", "kind-10000.json",
                 "kind-50000.json"]
        self.assertEqual(sorted(os.listdir(os.path.join(self.out, "a"))), names)
        first = {}
        for v in ("a", "b"):
            for n in names:
                with open(os.path.join(self.out, v, n), "rb") as fh:
                    first[v, n] = fh.read()
                self.assertTrue(first[v, n].endswith(b"\n"))
        with mock.patch.object(bd, "day_bands", STD_BANDS):
            want = en.run(days, te.settings(name="a"), fill="kind", start=10000.0)
        self.assertEqual(json.loads(first["a", "kind-10000.json"]), json.loads(json.dumps(want)))
        j = json.loads(first["a", "judge.json"])
        with mock.patch.object(bd, "day_bands", STD_BANDS):
            harsh = en.run(days, te.settings(name="a"), fill="harsh-stops", start=50000.0)
            kind = en.run(days, te.settings(name="a"), fill="kind", start=50000.0)
            k10 = en.run(days, te.settings(name="a"), fill="kind", start=10000.0)
            h10 = en.run(days, te.settings(name="a"), fill="harsh-stops", start=10000.0)
        dates = [d.date for d in days]
        harsh["rule_breaks"] = kind["rule_breaks"] = []
        for k, v in gates.judge(harsh, dates).items():
            self.assertEqual(j[k], json.loads(json.dumps(v)), k)
        self.assertEqual(j["kind_50000"], json.loads(json.dumps(gates.judge(kind, dates))))
        self.assertEqual(j["rule_breaks"], [])
        self.assertEqual(j["info_10000"], {
            "harsh-stops": {"net": round(sum(t["net"] for t in h10["trades"]), 2), "trades": len(h10["trades"]),
                            "skipped": len(h10["skipped"])},
            "kind": {"net": round(sum(t["net"] for t in k10["trades"]), 2), "trades": len(k10["trades"]),
                     "skipped": len(k10["skipped"])}})
        self.assertEqual(j["rule_check"], {"pass": True, "breaks": 0})
        # A second run writes the same bytes.
        self.assertEqual(self.call(days), 0)
        for (v, n), data in first.items():
            with open(os.path.join(self.out, v, n), "rb") as fh:
                self.assertEqual(fh.read(), data, (v, n))

    def test_run_all_reports_breaks(self):
        days = hand_days()
        self.write("a.json", te.settings(name="a"))
        self.commit()
        real_run = en.run
        calls = []

        def flaky(*a, **k):                       # the second kind 50,000 run gives different trades
            res = real_run(*a, **k)
            calls.append((k.get("fill"), k.get("start")))
            if calls.count(("kind", 50000.0)) == 2 and calls[-1] == ("kind", 50000.0):
                res = dict(res, digest="different")
            return res

        real_check = gates.rule_check

        def checked(res, d):
            out = real_check(res, d)
            return out + ["planted"] if res["fill"] == "kind" else out

        with mock.patch.object(en, "run", flaky), mock.patch.object(gates, "rule_check", checked):
            self.assertEqual(self.call(days), 0)
        with open(os.path.join(self.out, "a", "judge.json")) as fh:
            j = json.load(fh)
        self.assertEqual(len(j["rule_breaks"]), 2, j["rule_breaks"])
        self.assertTrue(any("kind 50000" in b and "second run" in b for b in j["rule_breaks"]))
        self.assertTrue(any(b.startswith("kind 50000: planted") for b in j["rule_breaks"]))
        self.assertEqual(j["rule_check"], {"pass": False, "breaks": 2})
        self.assertFalse(j["overall"])


if __name__ == "__main__":
    unittest.main()
