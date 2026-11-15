#!/usr/bin/env python3
"""Tests for stop_distance.py: every order of D1-D4 matches its locked rule, the run reproduces, the
shuffle figures match run.shuffled, and D4 equals V1's rule at 0.25% run through variations.py.
Run: python3 -I -B research/intraday-momentum-long/test_stop_distance.py"""
import datetime as dt
import math
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as R             # noqa: E402
import variations as V      # noqa: E402
import stop_distance as S   # noqa: E402

mk, bd = R.mk, R.bd
HAVE = os.path.exists(R.DATA)


class CostStop(unittest.TestCase):
    def test_loss_at_the_stop_never_above_the_budget(self):
        for budget in (50.0, 125.0, 131.37, 500.0, 612.9):
            for px in (14000.25, 20000.5, 30411.75):
                s = S.cost_stop(px, budget)
                self.assertEqual(s / R.TICK, math.floor(s / R.TICK))
                loss = (px - (s - R.SLIP)) * R.PV + R.COMM
                self.assertLessEqual(loss, budget + 1e-9)
                self.assertGreater(loss, budget - R.TICK * R.PV - 1e-9)   # within one tick of the budget


@unittest.skipUnless(HAVE, "data file absent")
class StopDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mk.load_market(R.DATA, session_start=R.SESSION_START)
        cls.sims = {k: S.Sim(v).run(cls.m) for k, v in S.VARIANTS.items()}

    def test_every_order_matches_its_rule(self):
        m = self.m
        for name, sim in self.sims.items():
            v = S.VARIANTS[name]
            bal, last_exit = R.START, ""
            self.assertGreater(len(sim.trades), 50, name)
            for t in sim.trades:
                self.assertEqual(t["side"], "Long", name)
                self.assertGreaterEqual(t["entry_dt"], last_exit, "%s: overlapping trades" % name)
                last_exit = t["exit_dt"]
                n, i0 = m.index[dt.datetime.fromisoformat(t["entry_dt"])]
                n1, i1 = m.index[dt.datetime.fromisoformat(t["exit_dt"])]
                self.assertEqual(n, n1)
                bars = m.sessions[n - 1].bars
                d = bars[i0 - 1]
                st = bd.band_at(m, n, d.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
                self.assertTrue(mk.is_checkpoint(d.mod) and st.have_band)
                self.assertGreater(d.c, st.upper, name)
                self.assertAlmostEqual(t["entry"], V.entry_fill(bars[i0], 1), places=9)
                budget = v["risk"] / 100.0 * bal
                self.assertAlmostEqual(t["budget"], budget, places=1)
                own = None if v["stop"] == "cost" else (st.lower if v["stop"] == "lower_band" else st.ref_upper)
                own_qty = int(budget / ((t["entry"] - own) * R.PV) + 1e-9) if own is not None and t["entry"] > own else 0
                if own is not None and own_qty >= 1:
                    # the strategy's own stop, candidate 1's sizing
                    self.assertFalse(t["moved_up"], name)
                    self.assertAlmostEqual(t["stop"], own, places=9)
                    self.assertEqual(t["qty"], own_qty)
                else:
                    # moved up (or D2): one MNQ at the cost distance
                    self.assertEqual(v["fallback"], "move_up", name)
                    self.assertEqual(t["moved_up"], v["stop"] != "cost", name)
                    self.assertEqual(t["qty"], 1)
                    self.assertAlmostEqual(t["stop"], S.cost_stop(t["entry"], budget), places=9)
                    self.assertLessEqual((t["entry"] - t["stop"] + R.SLIP) * R.PV + R.COMM, budget + 1e-6)
                self.assertLessEqual(t["qty"] * (t["entry"] - t["stop"]) * R.PV, budget + 0.01)
                for b in bars[i0:i1]:
                    self.assertFalse(V.stop_hit(b, 1, t["stop"]), "%s: held past the stop" % name)
                xb = bars[i1]
                self.assertTrue(xb.l <= t["exit"] <= xb.h)
                if t["reason"] == "stop":
                    self.assertTrue(V.stop_hit(xb, 1, t["stop"]))
                    self.assertAlmostEqual(t["exit"], V.stop_fill(xb, 1, t["stop"]), places=9)
                elif t["reason"] == "band/VWAP exit":
                    e = bars[i1 - 1]
                    se = bd.band_at(m, n, e.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
                    self.assertLessEqual(e.c, max(se.upper, se.vwap))
                elif t["reason"] == "flat 15:59":
                    self.assertEqual(bars[i1 - 1].mod, R.FLAT_MOD)
                else:
                    self.assertEqual(i1, len(bars) - 1)
                bal += (t["exit"] - t["entry"]) * t["qty"] * R.PV - R.COMM * t["qty"]
                self.assertAlmostEqual(t["balance"], bal, places=1)
            self.assertAlmostEqual(bal, sim.balance, places=1)

    def test_skips(self):
        for k in ("D1", "D2", "D3"):
            self.assertEqual(self.sims[k].skipped, 0, k)
        self.assertGreater(self.sims["D4"].skipped, 0)
        self.assertFalse(any(t["moved_up"] for t in self.sims["D4"].trades))
        self.assertTrue(any(t["moved_up"] for t in self.sims["D1"].trades))

    def test_d4_equals_v1_rule_at_quarter_percent(self):
        v1 = dict(V.VARIANTS["V1"], risk=0.25)
        other = V.Sim(v1).run(self.m)
        self.assertEqual(V.digest(other.trades), V.digest(self.sims["D4"].trades))
        self.assertEqual(other.skipped, self.sims["D4"].skipped)

    def test_same_run_twice(self):
        for k, v in S.VARIANTS.items():
            again = S.Sim(v).run(self.m)
            self.assertEqual(V.digest(again.trades), V.digest(self.sims[k].trades), k)
            self.assertEqual(again.days, self.sims[k].days, k)

    def test_shuffle_count_matches_run_shuffled(self):
        for k in ("D2", "D4"):
            days = self.sims[k].days
            self.assertEqual(S.shuffle_drops(days)["crossed"], R.shuffled(days)["crossed"], k)


if __name__ == "__main__":
    unittest.main(verbosity=2)
