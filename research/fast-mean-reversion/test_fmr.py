#!/usr/bin/env python3
"""Tests for candidate 4 (Carver's fast mean reversion). Every simulated order is rechecked against the
locked rule with inputs recomputed here by plain loops, and every qualifying signal between trades is
accounted for. Run: python3 -I -B research/fast-mean-reversion/test_fmr.py"""
import bisect
import datetime as dt
import math
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fmr as F   # noqa: E402

R, O = F.R, F.O
HAVE = os.path.exists(F.DATA)


def mkbar(t, o, h, l, c):
    return F.Bar(t, t.hour * 3600 + t.minute * 60 + t.second, o, h, l, c, 1)


class Pieces(unittest.TestCase):
    def test_session_date(self):
        D = dt.datetime
        self.assertEqual(F.session_date(D(2024, 1, 7, 18, 1)), dt.date(2024, 1, 8))    # Sunday evening -> Monday
        self.assertEqual(F.session_date(D(2024, 1, 8, 17, 0)), dt.date(2024, 1, 8))    # Monday 17:00 stays
        self.assertEqual(F.session_date(D(2024, 1, 11, 18, 1)), dt.date(2024, 1, 12))  # Thursday evening -> Friday
        self.assertIsNone(F.session_date(D(2024, 1, 12, 18, 1)))                       # Friday evening
        self.assertIsNone(F.session_date(D(2024, 1, 13, 12, 11)))                      # Saturday
        self.assertIsNone(F.session_date(D(2024, 1, 7, 12, 0)))                        # Sunday daytime

    def test_ewma(self):
        self.assertEqual(F.ewma([1.0, 4.0], 2), [1.0, 1.0 * (1 / 3.0) + 4.0 * (2 / 3.0)])

    def test_forecast_cap_and_filter(self):
        self.assertEqual(F.forecast(100, 1, 10, 90), 20.0)       # raw 1.0 -> 20 (cap)
        self.assertEqual(F.forecast(100, 1, 10, 95), 10.0)       # raw 0.5 -> 10
        self.assertEqual(F.forecast(100, -1, 10, 95), 0.0)       # buy signal against a down trend -> 0
        self.assertEqual(F.forecast(100, -1, 10, 105), -10.0)
        self.assertEqual(F.forecast(100, 0, 10, 105), 0.0)

    def test_size_counts_stop_slippage_and_commission(self):
        qty, per = F.size(50000, 100.0)
        self.assertAlmostEqual(per, 100.5 * 2 + 1.90)
        self.assertEqual(qty, int(500 / per))
        self.assertEqual(F.size(50000, 300.0)[0], 0)

    def test_stop_distance(self):
        self.assertEqual(F.stop_distance(201.0), 100.5)
        self.assertEqual(F.stop_distance(201.1), 100.75)

    def test_shuffle_trades(self):
        bad = [{"segs": [(-2500.0, -2400.0)]}]
        self.assertEqual(F.shuffle_trades(bad, runs=10)["pct"], 100.0)
        small = [{"segs": [(-50.0, 10.0)]} for _ in range(20)]
        self.assertEqual(F.shuffle_trades(small, runs=10)["pct"], 0.0)
        # the end-of-day mark lifts the floor inside a trade: up 1,500 at a close, then down 2,100 -> crossed
        lift = [{"segs": [(0.0, 1500.0), (-600.0, -500.0)]}]
        self.assertEqual(F.shuffle_trades(lift, runs=1)["pct"], 100.0)


class SyntheticSession(unittest.TestCase):
    """70 rising days, a dip that triggers a long, and a gap through the stop in the overnight hours."""

    def build(self):
        days, base = [], dt.date(2024, 1, 1)
        d, k = base, 0
        while len(days) < 72:
            if d.weekday() < 5:
                day = F.Day(d.isoformat())
                px = 1000.0 + 10.0 * k + (5.0 if k % 2 else -5.0)
                for hh in (10, 11, 16, 17):
                    t = dt.datetime(d.year, d.month, d.day, hh, 0)
                    day.bars.append(mkbar(t, px, px + 1, px - 1, px))
                days.append(day)
                k += 1
            d += dt.timedelta(days=1)
        for day in days:
            day.close = [b for b in day.bars if b.sec == 16 * 3600][0].c
        return days

    def test_long_entry_then_overnight_gap_stop(self):
        days = self.build()
        k = 70
        eq, trend, vol = F.daily_inputs(days)[k]
        self.assertEqual(trend, 1)
        dip = eq - 0.75 * vol                      # raw 0.75 -> F = 15
        d0 = days[k]
        d0.bars[0].c = dip                         # 10:00 close: the signal
        d0.bars[0].l = min(d0.bars[0].l, dip)
        for b in d0.bars[1:]:
            b.o = b.h = b.l = b.c = dip            # quiet afterwards, stays below equilibrium
        entry = O.entry_fill(d0.bars[1], 1)
        stop = entry - F.stop_distance(vol)
        nxt = days[k + 1]
        when = dt.datetime.fromisoformat(d0.date) + dt.timedelta(hours=19)
        gap = mkbar(when, stop - 20, stop - 15, stop - 30, stop - 18)   # opens through the stop at 19:00
        nxt.bars = [gap] + nxt.bars
        sim = F.Sim().run(days)
        t = sim.trades[0]
        self.assertEqual((t["side"], t["entry"], t["stop"]), (1, entry, stop))
        self.assertEqual((t["reason"], t["exit"], t["exit_dt"]), ("stop", stop - 20.5, when.isoformat(" ")))

    def test_held_to_next_day_close(self):
        days = self.build()
        k = 70
        eq, trend, vol = F.daily_inputs(days)[k]
        dip = eq - 0.75 * vol
        for b in days[k].bars:
            b.o = b.h = b.l = b.c = dip
        for b in days[k + 1].bars:
            b.o = b.h = b.l = b.c = dip
        sim = F.Sim().run(days)
        t = sim.trades[0]
        self.assertEqual(t["reason"], "next-day close")
        self.assertEqual(t["exit_dt"][:10], days[k + 1].date)


def plain_inputs(closes, k):
    """Inputs for day k from closes[0..k-1], by plain loops (independent of fmr.daily_inputs)."""
    def ew(xs, span):
        a, e = 2.0 / (span + 1), xs[0]
        for x in xs[1:]:
            e = a * x + (1 - a) * e
        return e
    past = closes[:k]
    eq = ew(past, 5)
    tr = ew(past, 16) - ew(past, 64)
    sq = [(past[i] - past[i - 1]) ** 2 for i in range(1, len(past))]
    a, var, vols = 2.0 / 33, None, []
    for x in sq:
        var = x if var is None else a * x + (1 - a) * var
        vols.append(math.sqrt(var))
    vol = 0.7 * vols[-1] + 0.3 * sum(vols) / len(vols)
    return eq, (1 if tr > 0 else -1 if tr < 0 else 0), vol


@unittest.skipUnless(HAVE, "data file absent")
class OrdersMatchTheRule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.days, cls.dropped = F.load()
        cls.sim = F.Sim().run(cls.days)
        closes = [d.close for d in cls.days]
        cls.inp = [None, None] + [plain_inputs(closes, k) for k in range(2, len(cls.days))]
        cls.where = {}
        for k, d in enumerate(cls.days):
            for i, b in enumerate(d.bars):
                cls.where[b.dt] = (k, i)

    def f_at(self, k, bar):
        eq, trend, vol = self.inp[k]
        raw = 20.0 * (eq - bar.c) / vol
        raw = max(-20.0, min(20.0, raw))
        if (raw > 0 and trend != 1) or (raw < 0 and trend != -1):
            return 0.0
        return raw

    def bars_from(self, k, i):
        while k < len(self.days):
            bars = self.days[k].bars
            while i < len(bars):
                yield k, i, bars[i]
                i += 1
            k, i = k + 1, 0

    def test_inputs_match(self):
        got = F.daily_inputs(self.days)
        for k in range(2, len(self.days)):
            for a, b in zip(got[k], self.inp[k]):
                self.assertAlmostEqual(a, b, places=6)

    def test_every_order_and_every_signal(self):
        days, sim = self.days, self.sim
        self.assertGreater(len(sim.trades), 100)
        bal, skipped = R.START, 0
        # state machine over signals, walking from the warm-up to the end
        k, i = F.WARMUP, 0
        for t in sim.trades:
            ek, ei = self.where[dt.datetime.fromisoformat(t["entry_dt"])]
            # the signal bar is the bar just before the entry bar, in the same trading day
            self.assertGreater(ei, 0)
            sig = days[ek].bars[ei - 1]
            self.assertEqual(sig.sec % 3600, 0)
            f = self.f_at(ek, sig)
            self.assertGreaterEqual(abs(f), 10.0)
            self.assertEqual(t["side"], 1 if f > 0 else -1)
            # no earlier qualifying signal since the last exit, except signals whose trade was skipped
            for kk, ii, b in self.bars_from(k, i):
                if (kk, ii) == (ek, ei - 1):
                    break
                last = ii == len(days[kk].bars) - 1
                if b.sec % 3600 == 0 and not last and abs(self.f_at(kk, b)) >= 10.0:
                    dist = F.stop_distance(self.inp[kk][2])
                    qty = int(0.01 * bal / ((dist + 0.5) * 2 + 1.90) + 1e-9)
                    self.assertLess(qty, 1, "missed signal at %s" % b.dt)
                    skipped += 1
            side = t["side"]
            eb = days[ek].bars[ei]
            entry = min(max(eb.o + side * 0.5, eb.l), eb.h)
            dist = math.ceil(0.5 * self.inp[ek][2] / 0.25 - 1e-9) * 0.25
            qty = int(0.01 * bal / ((dist + 0.5) * 2 + 1.90) + 1e-9)
            self.assertEqual((t["entry"], t["dist"], t["stop"], t["qty"]), (entry, dist, entry - side * dist, qty),
                             t["entry_dt"])
            self.assertLessEqual(t["planned_loss"], 0.01 * bal + 1e-6)
            # the exit: the first of stop, forecast back to zero (filled next bar), close of the next day
            stop = t["stop"]
            exp = None
            pend = False
            for kk, ii, b in self.bars_from(ek, ei):
                last = ii == len(days[kk].bars) - 1
                if pend:
                    exp = ("back to equilibrium", min(max(b.o - side * 0.5, b.l), b.h), b.dt, kk, ii)
                    break
                if (b.l <= stop) if side == 1 else (b.h >= stop):
                    exp = ("stop", O.stop_fill(b, side, stop), b.dt, kk, ii)
                    break
                if last and (kk >= ek + 1 or kk == len(days) - 1):
                    exp = ("next-day close" if kk >= ek + 1 else "end of data",
                           min(max(b.c - side * 0.5, b.l), b.h), b.dt, kk, ii)
                    break
                if b.sec % 3600 == 0 and not last and self.f_at(kk, b) * side <= 0:
                    pend = True
            self.assertEqual((t["reason"], t["exit"], t["exit_dt"]), (exp[0], exp[1], exp[2].isoformat(" ")),
                             t["entry_dt"])
            self.assertLessEqual(exp[3], ek + 1, "held past the next trading day")
            net = (t["exit"] - entry) * side * qty * 2 - 1.90 * qty
            self.assertAlmostEqual(t["net"], round(net, 2), places=2)
            bal += t["net"]
            self.assertAlmostEqual(t["balance"], round(bal, 2), places=1)
            self.assertAlmostEqual(t["segs"][-1][1], t["net"], places=2)
            # the walk resumes at the exit bar: a new signal may form on the same bar
            k, i = exp[3], exp[4]
        self.assertEqual(skipped, sim.skipped)

    def test_reproduces(self):
        self.assertEqual(F.digest(F.Sim().run(self.days)), F.digest(self.sim))

    def test_periods_split_cleanly(self):
        seen = F.Sim(period=R.SEEN).run(self.days)
        unseen = F.Sim(period=(R.UNSEEN[0], F.LAST_DAY)).run(self.days)
        self.assertTrue(all(t["entry_dt"][:10] <= R.SEEN[1] for t in seen.trades))
        self.assertTrue(all(t["entry_dt"][:10] >= "2024-12-31" for t in unseen.trades))

    def test_day_records(self):
        # a trade carried in from the day before can gap up at the evening open, so its day low may sit
        # above the previous close; a day that starts flat cannot
        for d in self.sim.days:
            self.assertLessEqual(d["low"], d["end"] + 1e-6)
            if not d["carried"]:
                self.assertLessEqual(d["low"], d["start"] + 1e-6)

    def test_no_weekend_days(self):
        for d in self.days:
            self.assertLess(dt.date.fromisoformat(d.date).weekday(), 5)


if __name__ == "__main__":
    unittest.main()
