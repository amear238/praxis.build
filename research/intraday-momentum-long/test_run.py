#!/usr/bin/env python3
"""Tests for run.py. Every simulated order is checked against the locked rule, independently of the
simulator's own loop. Run: python3 -I -B research/intraday-momentum-long/test_run.py"""
import datetime as dt
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as R   # noqa: E402

mk, bd = R.mk, R.bd
HAVE = os.path.exists(R.DATA)
_M = {}


def market():
    if "m" not in _M:
        _M["m"] = mk.load_market(R.DATA, session_start=R.SESSION_START)
    return _M["m"]


def prev_bar_of(m, n, i):
    return m.sessions[n - 1].bars[i - 1]


@unittest.skipUnless(HAVE, "data file absent")
class OrdersMatchTheRule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = market()
        cls.sim = R.Sim().run(cls.m)

    def test_every_order(self):
        m, sim = self.m, self.sim
        self.assertGreater(len(sim.trades), 200)
        bal = R.START
        for t in sim.trades:
            n, i0 = m.index[dt.datetime.fromisoformat(t["entry_dt"])]
            n1, i1 = m.index[dt.datetime.fromisoformat(t["exit_dt"])]
            self.assertEqual(n, n1, "held overnight")
            bars = m.sessions[n - 1].bars
            # entry decided on the previous bar: a :00/:30 bar that closed above the upper band
            d = prev_bar_of(m, n, i0)
            self.assertTrue(mk.is_checkpoint(d.mod))
            band = bd.band_at(m, n, d.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
            self.assertTrue(band.have_band and d.c > band.upper)
            # stop = that bar's lower band; entry fill = next open + 2 ticks
            self.assertAlmostEqual(t["stop"], band.lower, places=9)
            self.assertAlmostEqual(t["entry"], R.buy_fill(bars[i0]), places=9)
            # size: whole micro contracts, risk at the stop within 1% of the balance at entry
            self.assertGreaterEqual(t["qty"], 1)
            self.assertAlmostEqual(t["budget"], 0.01 * bal, places=1)
            self.assertLessEqual(t["qty"] * (t["entry"] - t["stop"]) * R.PV, 0.01 * bal + 0.01)
            self.assertGreater((t["qty"] + 1) * (t["entry"] - t["stop"]) * R.PV, 0.01 * bal - 0.01)
            # never held through a bar that reached the stop
            for b in bars[i0:i1]:
                self.assertGreater(b.l, t["stop"], "held past the stop")
            xb = bars[i1]
            self.assertTrue(xb.l <= t["exit"] <= xb.h)
            if t["reason"] == "stop":
                self.assertLessEqual(xb.l, t["stop"])
                self.assertAlmostEqual(t["exit"], R.stop_fill(xb, t["stop"]), places=9)
            elif t["reason"] == "band/VWAP exit":
                e = prev_bar_of(m, n, i1)
                st = bd.band_at(m, n, e.dt.strftime("%H:%M"), R.LOOKBACK, R.NOISE_MULT)
                self.assertTrue(mk.is_checkpoint(e.mod) and e.c <= max(st.upper, st.vwap))
                self.assertAlmostEqual(t["exit"], R.sell_fill(xb), places=9)
            elif t["reason"] == "flat 15:59":
                self.assertEqual(prev_bar_of(m, n, i1).mod, R.FLAT_MOD)
            else:
                self.assertEqual(t["reason"], "session close")
                self.assertEqual(i1, len(bars) - 1)
            # money
            net = (t["exit"] - t["entry"]) * t["qty"] * R.PV - R.COMM * t["qty"]
            self.assertAlmostEqual(t["net"], round(net, 2), places=2)
            bal += net
            self.assertAlmostEqual(t["balance"], bal, places=1)
        self.assertAlmostEqual(bal, sim.balance, places=1)

    def test_only_longs_and_one_at_a_time(self):
        last_exit = None
        for t in self.sim.trades:
            self.assertGreater(t["entry"], t["stop"])
            if last_exit:
                self.assertGreaterEqual(t["entry_dt"], last_exit)
            last_exit = t["exit_dt"]

    def test_same_run_twice(self):
        self.assertEqual(R.digest(self.sim), R.digest(R.Sim().run(self.m)))

    def test_periods_split_cleanly(self):
        seen = R.Sim(period=R.SEEN).run(self.m)
        unseen = R.Sim(period=R.UNSEEN).run(self.m)
        self.assertTrue(all(t["entry_dt"] < "2025-01-01" for t in seen.trades))
        self.assertTrue(all(t["entry_dt"] >= "2025-01-01" for t in unseen.trades))


class TrailingRule(unittest.TestCase):
    def test_floor_trails_end_of_day_high(self):
        days = [{"date": "d1", "start": 50000, "end": 51500, "low": 49900},
                {"date": "d2", "start": 51500, "end": 51000, "low": 49600},
                {"date": "d3", "start": 51000, "end": 50000, "low": 49400}]
        r = R.trailing(days)
        self.assertEqual(r["first_cross"], "d3")       # floor 49,500 after d1; d3 low 49,400
        self.assertEqual(r["closest_room"], -100.0)

    def test_never_crossed(self):
        days = [{"date": "d1", "start": 50000, "end": 50100, "low": 48100}]
        self.assertIsNone(R.trailing(days)["first_cross"])

    def test_shuffle_counts(self):
        always = [{"date": "x", "start": 50000, "end": 47000, "low": 47000}]
        self.assertEqual(R.shuffled(always, runs=50)["crossed"], 50)
        never = [{"date": "x", "start": 50000, "end": 50100, "low": 49900}] * 5
        self.assertEqual(R.shuffled(never, runs=50)["crossed"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
