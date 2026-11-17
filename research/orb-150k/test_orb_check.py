#!/usr/bin/env python3
"""Tests for orb_check.py. Run: python3 -I -B research/orb-150k/test_orb_check.py

The engine's output on hand-built days (the days of test_orb_engine.py, one after another, behind 14 quiet
days so the 14-day average exists) must give no break under any settings and fill. Each tampering of a clean
result must give at least one break, and the break must name what was tampered with.
"""
import copy
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import orb_check as ck          # noqa: E402
import globex as g              # noqa: E402  (on the path through orb_check's import)
import orb_engine as en         # noqa: E402  (the test makes results with it; orb_check does not import it)
import test_orb_engine as te    # noqa: E402  (make_day, weekdays, stamp, the fixture rows)

DATA = en.DATA

QUIET = 14
SHORT = [("09:31", 100, 104, 95, 98), ("09:35", 98, 100, 90, 92), ("09:36", 91.5, 92, 91, 91.5),
         ("10:00", 91, 91, 67, 70), ("10:05", 70, 70, 66.75, 68), ("16:00", 68, 69, 67, 68)]
BREAK = te.RANGE[:4] + [("09:35", 108, 109, 107, 108), ("09:40", 108, 112, 107, 109), ("09:45", 109, 112, 108, 110),
                        ("09:46", 110.5, 111.5, 110, 111), ("10:30", 111, 111, 90, 93), ("10:31", 93, 94, 92, 93),
                        te.CLOSE16]
# (rows, make_day keywords), one day each after the quiet days.
CASES = [
    (te.STD, {}),                                                                       # held to the flat
    (te.STD + [("10:00", 94, 95, 90, 92)], {}),                                         # gap through the stop
    (te.STD + [("10:00", 111.5, 141.5, 111.5, 120), ("10:10", 120, 141.75, 119, 140)], {}),   # 2R target
    (SHORT, {}),                                                                        # short, 2R target
    (te.STD + [("09:40", 111.5, 120, 104, 118), ("09:41", 118, 118, 106, 107), ("09:42", 107, 108, 104, 105)], {}),
    ([("09:31", 100, 104, 95, 102), ("09:35", 102, 111, 99, 100), te.ENTRY, te.CLOSE16], {}),      # doji
    ([("09:31", 100, 104, 100.25, 102), ("09:35", 102, 111, 101, 110), te.ENTRY, te.CLOSE16], {}),  # stop 9.75
    (BREAK, {}),
    (te.STD[:-1] + [("13:00", 111.5, 112, 110, 111)], {"last": "13:00"}),              # half day
    (te.STD + [("10:00", 111.5, 142, 96, 100)], {}),                                    # stop and target, one bar
    (te.STD[:-1] + [("16:00", 90, 91, 88, 89)], {}),                                    # flat fill beyond the stop
    (te.STD, {"drop": ("09:33",)}),                                                     # incomplete range
    (te.STD + [("10:00", 111.5, 112, 100, 111.5)], {}),                                 # last day: a plain trade
]
DATES = te.weekdays(QUIET + len(CASES))
TARGET_DAY = QUIET + 2          # the day whose 10:00 bar touches the 2R target exactly and 10:10 goes through


def fixture_days():
    days = [te.make_day(x, [("10:00", 100, 120, 100, 100)]) for x in DATES[:QUIET]]
    for k, (rows, kw) in enumerate(CASES):
        days.append(te.make_day(DATES[QUIET + k], rows, **kw))
    return days


DAYS = fixture_days()
SETTINGS = [
    {},
    {"exit": ["target_r", 2]},
    {"exit": ["target_r", 1.01]},
    {"exit": ["trail_r", 1]},
    {"exit": ["trail_r", 2]},
    {"entry": "break", "entry_until": "11:00"},
    {"entry": "break", "entry_until": "11:00", "sides": "long", "exit": ["target_r", 2]},
    {"sides": "short"},
    {"stop": ["or_frac", 0.7]},
    {"stop": ["atr_frac", 0.6], "exit": ["trail_r", 1]},
    {"max_or_atr": 1.0},
    {"max_or_atr": 0.75},
    {"or_minutes": 15},
    {"or_minutes": 30, "entry": "break", "entry_until": "15:58"},
    {"risk_pct": 5.0},
]


def result(fill="kind", start=150000.0, fixed_qty=None, days=DAYS, **over):
    return en.run(days, te.settings(**over), fill=fill, start=start, fixed_qty=fixed_qty)


def target_result():
    return result(exit=["target_r", 2])


class Clean(unittest.TestCase):
    def test_clean_result_has_no_breaks(self):
        self.assertEqual([d.date for d in DAYS], sorted(d.date for d in DAYS))
        seen = 0
        for over in SETTINGS:
            for fill in en.FILLS:
                res = result(fill=fill, **over)
                seen += len(res["trades"])
                self.assertEqual(ck.rule_check(res, DAYS), [], (over, fill))
        self.assertGreater(seen, 100)
        for fixed in (None, 1):
            res = result(start=3000.0, fixed_qty=fixed, risk_pct=1.0)       # under one contract unless fixed
            self.assertEqual(ck.rule_check(res, DAYS), [], fixed)
        res = target_result()
        self.assertEqual(sorted({t["reason"] for t in res["trades"]}), ["flat", "stop", "target"])
        self.assertTrue(any(t["gap"] for t in res["trades"]))
        self.assertTrue(res["skipped"])

    def test_engine_unchanged_inputs(self):
        res = target_result()
        before = copy.deepcopy(res)
        ck.rule_check(res, DAYS)
        self.assertEqual(res, before)


class Tampered(unittest.TestCase):
    def check(self, res, word):
        got = ck.rule_check(res, DAYS)
        self.assertTrue(got, "no break")
        self.assertTrue(any(word in x for x in got), got)
        return got

    def test_moved_stop(self):
        res = target_result()
        res["trades"][0]["stop_initial"] += 1.0
        self.check(res, "stop_initial")

    def test_wrong_qty(self):
        res = target_result()
        t = res["trades"][-1]
        t["qty"] += 1
        t["planned_cost"] = round(t["qty"] * en.loss_per_contract(t["dist"]), 2)
        t["net"] = round((t["exit"] - t["entry"]) * 2.0 * t["qty"] - 1.90 * t["qty"], 2)
        t["r"] = t["net"] / t["planned_cost"]
        self.check(res, "qty")

    def test_entry_a_bar_late(self):
        res = target_result()
        t = res["trades"][0]
        day = [d for d in DAYS if d.date == t["date"]][0]
        i = [b.dt.isoformat(" ") for b in day.bars].index(t["entry_dt"]) + 1
        b = day.bars[i]
        t["entry_dt"] = b.dt.isoformat(" ")
        t["entry"] = min(max(b.o + 0.5, b.l), b.h)
        t["stop_initial"] = t["entry"] - t["dist"]
        self.check(res, "entry")

    def test_missing_trade_on_signal_day(self):
        res = target_result()
        gone = res["trades"].pop()
        last = res["days"][-1]
        self.assertEqual(last["date"], gone["date"])
        last["end"] = last["low"] = last["start"]
        self.check(res, "no trade")

    def test_wrong_net(self):
        res = target_result()
        res["trades"][1]["net"] += 1.0
        self.check(res, "net")

    def test_day_low_too_high(self):
        res = target_result()
        k = [d["date"] for d in res["days"]].index(res["trades"][0]["date"])
        res["days"][k]["low"] += 10.0
        self.check(res, "low")

    def test_target_fill_without_tick_through(self):
        res = target_result()
        date = DAYS[TARGET_DAY].date
        t = [x for x in res["trades"] if x["date"] == date][0]
        self.assertEqual((t["reason"], t["exit_dt"], t["exit"]), ("target", date + " 10:10:00", 141.5))
        t["exit_dt"] = date + " 10:00:00"           # 10:00's high is the target itself, not a tick through
        self.check(res, "exit")

    def test_more_tamperings(self):
        cases = {
            "side": lambda r: r["trades"][0].update(side="short"),
            "two trades": lambda r: r["trades"].insert(1, dict(r["trades"][0])),
            "reason": lambda r: r["trades"][1].update(reason="flat"),
            "gap": lambda r: r["trades"][1].update(gap=not r["trades"][1]["gap"]),
            "balance": lambda r: r["trades"][2].update(balance=r["trades"][2]["balance"] + 0.05),
            "r": lambda r: r["trades"][2].update(r=0.5),
            "skip": lambda r: r["skipped"].clear(),
            "filtered": lambda r: r["filtered"].append(r["days"][-1]["date"]),
            "day end": lambda r: r["days"][-1].update(end=r["days"][-1]["end"] + 1),
            "dist": lambda r: r["trades"][0].update(dist=r["trades"][0]["dist"] + 0.25),
            "planned": lambda r: r["trades"][0].update(planned_cost=1.0),
            "day missing": lambda r: r["days"].pop(3),
        }
        for why, f in cases.items():
            res = target_result()
            f(res)
            self.assertTrue(ck.rule_check(res, DAYS), why)

    def test_kind_loss_above_planned_without_gap(self):
        res = result(fill="kind")
        t = [x for x in res["trades"] if x["gap"]][0]
        t["gap"] = False
        self.check(res, "planned")


@unittest.skipUnless(os.path.exists(DATA), "data file absent")
class RealData(unittest.TestCase):
    """The plan's Task 2 Step 4: the Task 1 Step 4 run, and each of the six exits with each of the three stops
    at midpoint fills, plus three more settings at kind fills; zero breaks on every one."""

    def test_real_data_runs_have_no_breaks(self):
        days = g.load_days(DATA)
        base = dict(en.STEP4)
        runs = [("task1 step4, harsh-stops, from 50000", base, "harsh-stops", 50000.0)]
        for stop in (["far_side"], ["or_frac", 0.5], ["atr_frac", 0.10]):
            for ex in (["hold_to_flat"], ["target_r", 3], ["target_r", 5], ["target_r", 10], ["trail_r", 1],
                       ["trail_r", 2]):
                runs.append(("%s %s, midpoint" % (stop, ex), dict(base, stop=stop, exit=ex), "midpoint", 150000.0))
        for s in (dict(base, entry="break", entry_until="11:00", or_minutes=15, stop=["or_frac", 0.5],
                       exit=["trail_r", 2]),
                  dict(base, or_minutes=30, sides="long", max_or_atr=0.5, stop=["atr_frac", 0.1]),
                  dict(base, entry="break", entry_until="15:58", sides="short", exit=["target_r", 3])):
            runs.append(("%s or%d %s %s, kind" % (s["entry"], s["or_minutes"], s["sides"], s["exit"]), s, "kind",
                         150000.0))
        total = 0
        for label, s, fill, start in runs:
            res = en.run(days, s, fill=fill, start=start)
            breaks = ck.rule_check(res, days)
            total += len(breaks)
            sys.stderr.write("\n  %-48s trades %5d  skipped %4d  filtered %4d  breaks %d"
                             % (label, len(res["trades"]), len(res["skipped"]), len(res["filtered"]), len(breaks)))
            for b in breaks[:5]:
                sys.stderr.write("\n      " + b)
            self.assertGreater(len(res["trades"]), 300, label)
        sys.stderr.write("\n  runs %d, breaks %d\n" % (len(runs), total))
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
