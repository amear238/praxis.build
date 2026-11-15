#!/usr/bin/env python3
"""Tests for variations.py: candidate 1 is reproduced exactly, and every order of every variation
matches its locked rule. Run: python3 -I -B research/intraday-momentum-long/test_variations.py"""
import datetime as dt
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as R          # noqa: E402
import variations as V   # noqa: E402

mk, bd = R.mk, R.bd
HAVE = os.path.exists(R.DATA)


@unittest.skipUnless(HAVE, "data file absent")
class Variations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mk.load_market(R.DATA, session_start=R.SESSION_START)
        cls.sims = {k: V.Sim(v).run(cls.m) for k, v in V.VARIANTS.items()}

    def test_c1_reproduces_candidate_1(self):
        old = R.Sim().run(self.m)
        new = self.sims["C1"]
        self.assertEqual(len(old.trades), len(new.trades))
        self.assertEqual(V.digest(old.trades), V.digest(new.trades))
        self.assertEqual(old.days, new.days)
        self.assertEqual(old.skipped, new.skipped)

    def test_every_order_matches_its_rule(self):
        m = self.m
        for name, sim in self.sims.items():
            v = V.VARIANTS[name]
            bal = R.START
            last_exit = ""
            self.assertGreater(len(sim.trades), 100, name)
            for t in sim.trades:
                side = 1 if t["side"] == "Long" else -1
                if v["sides"] == "long":
                    self.assertEqual(side, 1, name)
                self.assertGreaterEqual(t["entry_dt"], last_exit, "%s: overlapping trades" % name)
                last_exit = t["exit_dt"]
                n, i0 = m.index[dt.datetime.fromisoformat(t["entry_dt"])]
                n1, i1 = m.index[dt.datetime.fromisoformat(t["exit_dt"])]
                self.assertEqual(n, n1)
                bars = m.sessions[n - 1].bars
                d = bars[i0 - 1]
                st = bd.band_at(m, n, d.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
                self.assertTrue(mk.is_checkpoint(d.mod) and st.have_band)
                self.assertTrue(d.c > st.upper if side == 1 else d.c < st.lower, name)
                want_stop = (st.lower if side == 1 else st.upper) if v["stop"] == "lower_band" else \
                            (st.ref_upper if side == 1 else st.ref_lower)
                self.assertAlmostEqual(t["stop"], want_stop, places=9)
                self.assertAlmostEqual(t["entry"], V.entry_fill(bars[i0], side), places=9)
                risk = t["qty"] * (t["entry"] - t["stop"]) * side * R.PV
                budget = v["risk"] / 100.0 * bal
                self.assertAlmostEqual(t["budget"], budget, places=1)
                self.assertLessEqual(risk, budget + 0.01)
                self.assertGreater(risk / t["qty"] * (t["qty"] + 1), budget - 0.01)
                for b in bars[i0:i1]:
                    self.assertFalse(V.stop_hit(b, side, t["stop"]), "%s: held past the stop" % name)
                xb = bars[i1]
                self.assertTrue(xb.l <= t["exit"] <= xb.h)
                if t["reason"] == "stop":
                    self.assertTrue(V.stop_hit(xb, side, t["stop"]))
                    self.assertAlmostEqual(t["exit"], V.stop_fill(xb, side, t["stop"]), places=9)
                elif t["reason"] == "band/VWAP exit":
                    self.assertEqual(v["exit"], "trail", name)
                    e = bars[i1 - 1]
                    se = bd.band_at(m, n, e.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
                    lvl = max(se.upper, se.vwap) if side == 1 else min(se.lower, se.vwap)
                    self.assertTrue(e.c <= lvl if side == 1 else e.c >= lvl)
                elif t["reason"] == "flat 15:59":
                    self.assertEqual(bars[i1 - 1].mod, R.FLAT_MOD)
                else:
                    self.assertEqual(i1, len(bars) - 1)
                net = (t["exit"] - t["entry"]) * side * t["qty"] * R.PV - R.COMM * t["qty"]
                bal += net
                self.assertAlmostEqual(t["balance"], bal, places=1)
            self.assertAlmostEqual(bal, sim.balance, places=1)

    def test_v2_has_shorts_and_v3_never_trails(self):
        self.assertTrue(any(t["side"] == "Short" for t in self.sims["V2"].trades))
        self.assertFalse(any(t["reason"] == "band/VWAP exit" for t in self.sims["V3"].trades))

    def test_same_run_twice(self):
        for k in ("V1", "V2"):
            self.assertEqual(V.digest(self.sims[k].trades), V.digest(V.Sim(V.VARIANTS[k]).run(self.m).trades))


if __name__ == "__main__":
    unittest.main(verbosity=2)
