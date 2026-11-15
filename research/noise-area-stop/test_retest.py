#!/usr/bin/env python3
"""Tests for retest.py. Run: python3 -I -B research/noise-area-stop/test_retest.py

1. Without a stop, the simulator must reproduce the three NinjaTrader trade lists of 2026-11-01
   trade for trade (side, entry time and price, exit time and price).
2. With a stop, every order must match the rule: a stop exists from entry, sits at the planned
   distance, fires only when the bar reached it, and no trade is held past a bar that reached it.
3. The same run twice gives the same trade list.
"""
import csv
import datetime as dt
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import retest as rt   # noqa: E402

mk = rt.mk
EVID = os.path.join(rt.REPO, "docs", "reports", "evidence", "2026-11-01-ninjatrader-grid-%s.csv")
NT_RUNS = (("BandOrVWAP", EVID % "0710am"), ("OppBand", EVID % "0757am"), ("Flat1559", EVID % "0759am"))
HAVE = os.path.exists(rt.DATA) and all(os.path.exists(p) for _, p in NT_RUNS)
_MARKETS = {}


def market(start):
    if start not in _MARKETS:
        _MARKETS[start] = mk.load_market(rt.DATA, session_start=start)
    return _MARKETS[start]


def nt_trades(path):
    out = []
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            t = lambda s: dt.datetime.strptime(s, "%Y-%m-%d %I:%M:%S %p").isoformat(" ")
            out.append((r["Market pos."], t(r["Entry time"]), float(r["Entry price"]),
                        t(r["Exit time"]), float(r["Exit price"]),
                        float(r["Profit"].replace("$", "").replace(",", ""))))
    return out


@unittest.skipUnless(HAVE, "data file or NinjaTrader trade lists absent")
class ReproducesNinjaTrader(unittest.TestCase):
    def test_trade_for_trade(self):
        for policy, path in NT_RUNS:
            nt = nt_trades(path)
            sim = rt.Sim(policy=policy, risk_pct=None, model="kind", instrument="NQ").run(market("08:31"))
            mine = [(t["side"], t["entry_dt"], t["entry"], t["exit_dt"], t["exit"], t["net"]) for t in sim.trades]
            self.assertEqual(len(mine), len(nt), "%s: trade count %d vs NinjaTrader %d" % (policy, len(mine), len(nt)))
            bad = [(j + 1, a, b) for j, (a, b) in enumerate(zip(mine, nt))
                   if a[:2] != b[:2] or a[3] != b[3] or abs(a[2] - b[2]) > 1e-9 or abs(a[4] - b[4]) > 1e-9
                   or abs(a[5] - b[5]) > 0.005]
            self.assertEqual(bad[:3], [], "%s: %d trades differ" % (policy, len(bad)))
            self.assertAlmostEqual(sum(t[5] for t in mine), sum(t[5] for t in nt), places=2)


@unittest.skipUnless(os.path.exists(rt.DATA), "data file absent")
class StopOrdersMatchTheRule(unittest.TestCase):
    def check(self, model, risk):
        m = market("09:31")
        sim = rt.Sim(policy="Flat1559", risk_pct=risk, model=model).run(m)
        self.assertGreater(len(sim.trades), 100)
        bal = sim.start_balance
        for t in sim.trades:
            side = 1 if t["side"] == "Long" else -1
            # a stop exists from entry, at the planned distance from the entry fill
            self.assertIsNotNone(t["stop"])
            planned = risk / 100.0 * bal
            self.assertAlmostEqual(t["planned_cost"], planned, places=6)
            dist = (t["entry"] - t["stop"]) * side
            self.assertAlmostEqual(dist, rt.floor_tick(planned / 2.0), places=9)
            self.assertLessEqual(dist * 2.0, planned + 1e-9)
            # walk the bars the trade was open
            n, i0 = m.index[dt.datetime.fromisoformat(t["entry_dt"])]
            n1, i1 = m.index[dt.datetime.fromisoformat(t["exit_dt"])]
            self.assertEqual(n, n1, "trade held overnight: %r" % (t,))
            bars = m.sessions[n - 1].bars
            for b in bars[i0:i1]:
                self.assertFalse(rt.stop_hit(b, side, t["stop"]), "held past a bar that reached the stop: %r" % (t,))
            xb = bars[i1]
            if t["reason"] == "stop":
                self.assertTrue(rt.stop_hit(xb, side, t["stop"]))
                self.assertTrue(xb.l <= t["exit"] <= xb.h)
                if model in ("harsh", "harsh-stops"):
                    self.assertEqual(t["exit"], xb.l if side == 1 else xb.h)
                else:
                    self.assertLessEqual((t["stop"] - t["exit"]) * side, max(rt.SLIP, abs(xb.o - t["stop"]) + rt.SLIP) + 1e-9)
            else:
                self.assertIn(t["reason"], ("band/VWAP exit", "reverse", "flat 15:59", "session close"))
                # an exit that was not the stop: the stop was not reached on the exit bar before the fill
                # can be known only for exits at the bar's open; a later touch in that bar is after the exit.
            self.assertTrue(xb.l <= t["exit"] <= xb.h)
            self.assertTrue(bars[i0].l <= t["entry"] <= bars[i0].h)
            bal = t["balance"]
        self.assertAlmostEqual(bal, sim.balance, places=2)

    def test_kind_1pct(self):
        self.check("kind", 1.0)

    def test_harsh_1pct(self):
        self.check("harsh", 1.0)

    def test_harsh_stops_1pct(self):
        self.check("harsh-stops", 1.0)

    def test_same_run_twice(self):
        m = market("09:31")
        a = rt.digest(rt.Sim(risk_pct=1.0, model="kind").run(m))
        b = rt.digest(rt.Sim(risk_pct=1.0, model="kind").run(m))
        self.assertEqual(a, b)

    def test_harsh_never_better_than_kind_on_stops(self):
        m = market("09:31")
        k = rt.stats(rt.Sim(risk_pct=1.0, model="kind").run(m))
        h = rt.stats(rt.Sim(risk_pct=1.0, model="harsh").run(m))
        self.assertLess(h["net"], k["net"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
