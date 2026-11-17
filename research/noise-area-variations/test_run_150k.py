#!/usr/bin/env python3
"""Tests for run_150k.py. Run: python3 -I -B research/noise-area-variations/test_run_150k.py

Hand-built day dicts for the limit with MFFU's lock and for the evaluation count; the runner itself on the
hand days of test_gates.py in a throwaway git repository.
"""
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bands as bd          # noqa: E402
import engine as en         # noqa: E402
import gates                # noqa: E402
import run_150k as r        # noqa: E402
import test_engine as te    # noqa: E402
import test_gates as tg     # noqa: E402

S = 150000.0


def days_of(rows):
    """rows of (change, lowest mark under the start) -> day dicts from 150,000."""
    out, bal = [], S
    for n, (pnl, low) in enumerate(rows):
        out.append({"date": "2024-03-%02d" % (n + 1), "start": bal, "end": bal + pnl, "low": bal + low})
        bal += pnl
    return out


class Lock(unittest.TestCase):
    def test_level_trails_then_locks(self):
        self.assertEqual(r._floor(150000.0, S, 4500.0, 100.0), 145500.0)
        self.assertEqual(r._floor(152000.0, S, 4500.0, 100.0), 147500.0)
        self.assertEqual(r._floor(154600.0, S, 4500.0, 100.0), 150100.0)
        self.assertEqual(r._floor(170000.0, S, 4500.0, 100.0), 150100.0)

    def test_trailing_lock(self):
        # Day 1 +2,000 (level 147,500). Day 2 dips 4,499.99 under its start: 147,500.01, not crossed.
        d = days_of([(2000.0, 0.0), (0.0, -4499.99), (0.0, 0.0)])
        self.assertIsNone(r.trailing_lock(d))
        d = days_of([(2000.0, 0.0), (0.0, -4500.0), (0.0, 0.0)])
        self.assertEqual(r.trailing_lock(d), "2024-03-02")
        # Up 10,000: the level is locked at 150,100, so a 9,000 dip does not cross; without the lock it does.
        d = days_of([(10000.0, 0.0), (0.0, -9000.0)])
        self.assertIsNone(r.trailing_lock(d))
        self.assertEqual(gates.trailing(d, start=S, limit=4500.0)["first_cross"], "2024-03-02")
        d = days_of([(10000.0, 0.0), (0.0, -9900.0)])
        self.assertEqual(r.trailing_lock(d), "2024-03-02")
        # The level moves at the day's end only: a day that dips before it gains is measured from the old level.
        d = days_of([(3000.0, -4499.0)])
        self.assertIsNone(r.trailing_lock(d))

    def test_shuffled_lock(self):
        # One loser of 4,500 and nothing else: every order crosses.
        self.assertEqual(r.shuffled_lock(days_of([(-4500.0, -4500.0), (10.0, 0.0)]), runs=50), (50, 50))
        # Small days: no order crosses. Days that did nothing are left out.
        d = days_of([(100.0, -50.0), (-80.0, -90.0), (0.0, 0.0), (60.0, 0.0)])
        self.assertEqual(len(r._blocks(d)), 3)
        self.assertEqual(r.shuffled_lock(d, runs=50), (0, 50))
        # +10,000 then a 9,000 dip: crossed only in the orders where the dip comes first (about half).
        c, n = r.shuffled_lock(days_of([(10000.0, 0.0), (0.0, -9000.0)]), runs=2000, seed=1)
        self.assertTrue(800 < c < 1200, c)
        # Same seed, same count.
        self.assertEqual(r.shuffled_lock(days_of([(10000.0, 0.0), (0.0, -9000.0)]), runs=2000, seed=1), (c, n))


class Evaluation(unittest.TestCase):
    def test_counts(self):
        # Start day 1: +5,000, +4,000 -> 159,000 on day 2: passed in 2 days.
        # Start day 2: +4,000, then -4,500 at the low on day 3 (level 149,500; 154,000 - 4,500 = 149,500): failed.
        # Start day 3: -4,500 at the low: failed. Start day 4: +100 and the days run out: unfinished.
        d = days_of([(5000.0, 0.0), (4000.0, 0.0), (-1000.0, -4500.0), (100.0, 0.0)])
        self.assertEqual(r.evaluation(d), {"starts": 4, "passed": 1, "failed": 2, "unfinished": 1,
                                           "median_days_to_pass": 2})
        # One cent short of the target does not pass.
        d = days_of([(8999.99, 0.0)])
        self.assertEqual(r.evaluation(d)["passed"], 0)
        d = days_of([(9000.0, 0.0)])
        self.assertEqual(r.evaluation(d), {"starts": 1, "passed": 1, "failed": 0, "unfinished": 0,
                                           "median_days_to_pass": 1})
        # A day that reaches the level and then ends over the target has failed.
        d = days_of([(9000.0, -4500.0)])
        self.assertEqual((r.evaluation(d)["passed"], r.evaluation(d)["failed"]), (0, 1))
        self.assertEqual(r.evaluation([])["median_days_to_pass"], None)

    def test_info(self):
        d = days_of([(-2500.0, -2500.0), (100.0, -2499.99), (300.0, -2600.0)])
        res = {"days": d, "start": S, "trades": [{"qty": 3}, {"qty": 91}]}
        i = r.info(res)
        self.assertEqual((i["max_qty"], i["days_down_2500"]), (91, 2))
        self.assertEqual(i["lock"]["first_cross"], "2024-03-02")     # 147,500 - 2,499.99 is under 145,500
        self.assertEqual(i["evaluation"]["starts"], 3)
        self.assertEqual(r.info({"days": [], "start": S, "trades": []})["max_qty"], 0)


class Runner(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.repo = os.path.join(self.tmp, "repo")
        self.vdir = os.path.join(self.repo, "variations")
        self.out = os.path.join(self.tmp, "out")
        os.makedirs(self.vdir)
        tg.git(self.repo, "init", "-q")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, name, s):
        with open(os.path.join(self.vdir, name), "w") as fh:
            json.dump(s, fh)

    def call(self, days):
        with mock.patch.object(bd, "day_bands", tg.STD_BANDS), mock.patch("sys.stdout"):
            return r.run_150k(self.vdir, self.out, days=days, workers=1)

    def test_refuses_uncommitted_and_invalid(self):
        days = tg.hand_days()
        self.assertEqual(self.call(days), 2)
        self.write("a.json", te.settings(name="a"))
        self.assertEqual(self.call(days), 2)
        tg.git(self.repo, "add", "-A")
        tg.git(self.repo, "commit", "-q", "-m", "settings")
        self.write("a.json", te.settings(name="a", risk_pct=0.5))
        self.assertEqual(self.call(days), 2)
        self.write("a.json", te.settings(name="b"))
        tg.git(self.repo, "add", "-A")
        tg.git(self.repo, "commit", "-q", "-m", "wrong name")
        self.assertEqual(self.call(days), 2)
        self.assertFalse(os.path.exists(self.out))

    def test_writes_three_fills_and_the_judge(self):
        days = tg.hand_days()
        self.write("a.json", te.settings(name="a"))
        tg.git(self.repo, "add", "-A")
        tg.git(self.repo, "commit", "-q", "-m", "settings")
        self.assertEqual(self.call(days), 0)
        vdir = os.path.join(self.out, "a")
        self.assertEqual(sorted(os.listdir(vdir)), ["harsh-stops.json", "judge.json", "kind.json", "midpoint.json"])
        with open(os.path.join(vdir, "judge.json")) as fh:
            j = json.load(fh)
        with open(os.path.join(vdir, "midpoint.json")) as fh:
            mid = json.load(fh)
        self.assertEqual((mid["fill"], mid["start"]), ("midpoint", 150000.0))
        with mock.patch.object(bd, "day_bands", tg.STD_BANDS):
            want = en.run(days, te.settings(name="a"), fill="midpoint", start=150000.0)
            dates = [d.date for d in days]
            judged = gates.judge(dict(want, rule_breaks=[]), dates, limit=4500.0)
        self.assertEqual(mid["trades"], want["trades"])
        self.assertEqual(j["rule_breaks"], [])
        for k, v in judged.items():
            self.assertEqual(j[k], v, k)
        self.assertEqual(j["digests"]["midpoint"], want["digest"])
        self.assertEqual(sorted(j["digests"]), ["harsh-stops", "kind", "midpoint"])
        self.assertEqual(j["info"], r.info(want))
        self.assertEqual(j["kind"]["profit"]["pass"], j["kind"]["profit"]["net"] >= 9000.0)
        self.assertIn("harsh_stops", j)
        # A second run writes the same bytes.
        with open(os.path.join(vdir, "judge.json"), "rb") as fh:
            first = fh.read()
        self.assertEqual(self.call(days), 0)
        with open(os.path.join(vdir, "judge.json"), "rb") as fh:
            self.assertEqual(fh.read(), first)


if __name__ == "__main__":
    unittest.main()
