#!/usr/bin/env python3
"""Tests for bands.py. Run: python3 -I -B research/noise-area-variations/test_bands.py

Hand-built days check the 6 PM band's sigma, its 14-day warm-up, a missing anchor bar at either anchor,
the 9:30 band's reference prices, and that no band value looks ahead. One test reads the real data file
and checks that the 9:30 band equals the project's existing band oracle (scripts/wf/oracle/band.py,
session start 09:31) at every minute of 60 dates spread over the file.
"""
import datetime as dt
import os
import random
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import globex as g   # noqa: E402
import bands as bd   # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
BASE = dt.date(2021, 3, 8)
SM_0931 = g.sm_of("09:31")
SM_1600 = g.sm_of("16:00")


def stamp_of(date, sm):
    """Trading date + session minute -> the bar's end-of-minute stamp (evening minutes are the day before)."""
    m = sm + 18 * 60
    if m >= 24 * 60:
        return dt.datetime(date.year, date.month, date.day) + dt.timedelta(minutes=m - 24 * 60)
    return dt.datetime(date.year, date.month, date.day) - dt.timedelta(days=1) + dt.timedelta(minutes=m)


def make_day(i, bars):
    """Day number i (a weekday counted from BASE) from [(sm, o, h, l, c, v), ...] in sm order."""
    date = BASE + dt.timedelta(days=7 * (i // 5) + i % 5)
    d = g.Day(date.isoformat())
    for sm, o, h, l, c, v in bars:
        d.by_sm[sm] = len(d.bars)
        d.bars.append(g.Bar(stamp_of(date, sm), sm, o, h, l, c, v))
    return d


def copy_day(day, change_after=None, factor=1.0):
    """A fresh copy of day; bars with sm > change_after (all bars when None) get every price scaled."""
    out = g.Day(day.date)
    for b in day.bars:
        f = factor if (change_after is None or b.sm > change_after) else 1.0
        out.by_sm[b.sm] = len(out.bars)
        out.bars.append(g.Bar(b.dt, b.sm, b.o * f, b.h * f, b.l * f, b.c * f, b.v + (7 if f != 1.0 else 0)))
    return out


def points(bmap):
    return {sm: (p.upper, p.lower, p.vwap, p.anchor_price, p.width) for sm, p in bmap.items()}


def evening_day(i, open_=100.0, move=0.01, with_1801=True):
    """A 6 PM test day: 18:01 bar opening at open_, a bar at sm 60 closing at open_ * (1 + move)."""
    o = open_ + i
    bars = []
    if with_1801:
        bars.append((1, o, o + 1, o - 1, o, 10))
    else:
        bars.append((2, o * 0.95, o, o * 0.9, o * 0.95, 10))   # first bar is not 18:01, a different open
    bars.append((60, o, o * 1.02, o, o * (1.0 + move), 20))
    return make_day(i, bars)


class SixPm(unittest.TestCase):
    def test_1800_sigma_by_hand(self):
        days = [evening_day(i) for i in range(15)]
        b = bd.day_bands(days, 14, "1800")
        o = days[14].bars[0].o
        self.assertEqual(sorted(b), [1, 60])
        p = b[60]
        self.assertAlmostEqual(p.anchor_price, o, places=12)
        self.assertAlmostEqual(p.upper, o * 1.01, places=9)
        self.assertAlmostEqual(p.lower, o * 0.99, places=9)
        self.assertAlmostEqual(p.width, o * 0.01, places=9)
        # VWAP from the 18:01 bar: typical prices (h + l + c) / 3 weighted by volume.
        b1, b60 = days[14].bars
        tp1, tp60 = (b1.h + b1.l + b1.c) / 3.0, (b60.h + b60.l + b60.c) / 3.0
        self.assertAlmostEqual(b[1].vwap, tp1, places=9)
        self.assertAlmostEqual(p.vwap, (tp1 * 10 + tp60 * 20) / 30.0, places=9)
        # At sm 1 every earlier day moved 0 from its own open: the band is the open itself.
        self.assertEqual((b[1].upper, b[1].lower, b[1].width), (o, o, 0.0))

    def test_1800_mult_scales_sigma(self):
        days = [evening_day(i) for i in range(15)]
        p = bd.day_bands(days, 14, "1800", mult=2.5)[60]
        o = days[14].bars[0].o
        self.assertAlmostEqual(p.upper, o * 1.025, places=9)
        self.assertAlmostEqual(p.lower, o * 0.975, places=9)
        self.assertAlmostEqual(p.width, o * 0.025, places=9)

    def test_1800_needs_14_days(self):
        days = [evening_day(i) for i in range(15)]
        self.assertEqual(bd.day_bands(days, 13, "1800"), {})
        self.assertNotEqual(bd.day_bands(days, 14, "1800"), {})
        for k in range(14):
            self.assertEqual(bd.day_bands(days, k, "1800"), {}, "day %d" % k)

    def test_1800_lookback_window_is_14_most_recent(self):
        # Days 0..4 moved 5%, days 5..18 moved 1%: day 19 averages only the 14 most recent (all 1%).
        days = [evening_day(i, move=0.05 if i < 5 else 0.01) for i in range(20)]
        p = bd.day_bands(days, 19, "1800")[60]
        self.assertAlmostEqual(p.width, days[19].bars[0].o * 0.01, places=9)
        # Day 18 reaches back to day 4 (5%): 13 days at 1% and one at 5%.
        p18 = bd.day_bands(days, 18, "1800")[60]
        self.assertAlmostEqual(p18.width / days[18].bars[0].o, (13 * 0.01 + 0.05) / 14, places=12)

    def test_walk_reaches_back_lookback_plus_15_days(self):
        # lookback 2 -> at most 17 earlier days. sm 100 trades on the first day, the day before the last,
        # and the last day only.
        def build(n):
            days = []
            for i in range(n):
                o = 100.0 + i
                bars = [(1, o, o, o, o, 10)]
                if i in (0, n - 2, n - 1):
                    bars.append((100, o, o, o, o * 1.02, 10))
                days.append(make_day(i, bars))
            return days
        near = build(18)    # day 17 reaches days 0..16: both found
        self.assertIn(100, bd.day_bands(near, 17, "1800", lookback=2))
        far = build(19)     # day 18 reaches days 1..17: day 0 is out of reach, only day 17 found
        self.assertNotIn(100, bd.day_bands(far, 18, "1800", lookback=2))
        self.assertIn(1, bd.day_bands(far, 18, "1800", lookback=2))

    def test_missing_1801_bar_no_band(self):
        # Day 5 has no 18:01 bar; its first bar opens 5% lower, so using it would show in sigma.
        days = [evening_day(i, with_1801=(i != 5)) for i in range(16)]
        days[5].bars[-1].c = days[5].bars[0].o * 1.30   # a 30% move from its first bar, if it were used
        self.assertEqual(bd.day_bands(days, 5, "1800"), {})
        # Not counted: day 14 has only 13 earlier days with an 18:01 bar.
        self.assertEqual(bd.day_bands(days, 14, "1800"), {})
        # Not used: day 15's sigma is the 1% of the 14 days that have one.
        p = bd.day_bands(days, 15, "1800")[60]
        self.assertAlmostEqual(p.width, days[15].bars[0].o * 0.01, places=9)


def morning_day(i, open_=200.0, move=0.01, prev_last=None, with_0931=True, evening=True):
    """A 9:30 test day: an evening bar, a 09:31 bar opening at open_+i, a 10:00 bar closing +move, and a last
    bar at 16:00 closing at prev_last (when given) or at the open."""
    o = open_ + i
    bars = []
    if evening:
        bars.append((1, o - 50, o - 49, o - 51, o - 50, 5))
    if with_0931:
        bars.append((SM_0931, o, o + 1, o - 1, o, 10))
    else:
        bars.append((SM_0931 + 1, o * 0.9, o, o * 0.9, o * 0.9, 10))
    bars.append((g.sm_of("10:00"), o, o * 1.02, o, o * (1.0 + move), 20))
    last = o if prev_last is None else prev_last
    bars.append((SM_1600, last, last, last, last, 30))
    return make_day(i, bars)


class NineThirty(unittest.TestCase):
    def test_0930_reference_prices_by_hand(self):
        days = [morning_day(i) for i in range(15)]
        # Previous close 10 above today's open: upper rests on the previous close, lower on the open.
        days[13] = morning_day(13, prev_last=days[14].bars[1].o + 10.0)
        b = bd.day_bands(days, 14, "0930")
        self.assertEqual(sorted(b), [SM_0931, g.sm_of("10:00"), SM_1600])   # nothing before 09:31
        o = days[14].bars[1].o
        pc = o + 10.0
        p = b[g.sm_of("10:00")]
        self.assertEqual(p.anchor_price, o)
        self.assertAlmostEqual(p.upper, pc * 1.01, places=9)
        self.assertAlmostEqual(p.lower, o * 0.99, places=9)
        self.assertAlmostEqual(p.width, o * 0.01, places=9)
        # VWAP starts at the 09:31 bar; the evening bar is not in it.
        b0931 = days[14].bars[1]
        self.assertAlmostEqual(b[SM_0931].vwap, (b0931.h + b0931.l + b0931.c) / 3.0, places=9)

    def test_0930_previous_close_below_open(self):
        days = [morning_day(i) for i in range(15)]
        days[13] = morning_day(13, prev_last=days[14].bars[1].o - 4.0)
        p = bd.day_bands(days, 14, "0930")[g.sm_of("10:00")]
        o = days[14].bars[1].o
        self.assertAlmostEqual(p.upper, o * 1.01, places=9)
        self.assertAlmostEqual(p.lower, (o - 4.0) * 0.99, places=9)

    def test_0930_needs_14_days(self):
        days = [morning_day(i) for i in range(15)]
        self.assertEqual(bd.day_bands(days, 13, "0930"), {})
        self.assertNotEqual(bd.day_bands(days, 14, "0930"), {})

    def test_missing_0931_bar_no_band(self):
        # Day 5 has no 09:31 bar (its first daytime bar is 09:32, 10% lower): no band, not counted, not
        # used; and day 6's previous close is day 4's last bar, not day 5's.
        days = [morning_day(i, with_0931=(i != 5)) for i in range(16)]
        days[5] = morning_day(5, with_0931=False, move=0.30, prev_last=1.0)
        days[4] = morning_day(4, prev_last=days[6].bars[1].o + 3.0)
        self.assertEqual(bd.day_bands(days, 5, "0930"), {})
        self.assertEqual(bd.day_bands(days, 14, "0930"), {})
        p = bd.day_bands(days, 15, "0930")[g.sm_of("10:00")]
        self.assertAlmostEqual(p.width, days[15].bars[1].o * 0.01, places=9)
        # Day 6 has only 5 earlier days with a 09:31 bar; at lookback 4 it gets a band, and its upper reference
        # is day 4's last close (day 5's last close of 1.0 would make the lower reference 1.0).
        p6 = bd.day_bands(days, 6, "0930", lookback=4)[g.sm_of("10:00")]
        o6 = days[6].bars[1].o
        self.assertAlmostEqual(p6.upper, (o6 + 3.0) * 1.01, places=9)
        self.assertAlmostEqual(p6.lower, o6 * 0.99, places=9)

    def test_first_day_has_no_band(self):
        days = [morning_day(i) for i in range(3)]
        self.assertEqual(bd.day_bands(days, 0, "0930", lookback=1), {})
        self.assertEqual(bd.day_bands(days, 0, "1800", lookback=1), {})

    def test_bad_arguments(self):
        days = [morning_day(i) for i in range(3)]
        with self.assertRaises(ValueError):
            bd.day_bands(days, 2, "0931")
        with self.assertRaises(ValueError):
            bd.day_bands(days, 2, "0930", lookback=0)
        with self.assertRaises(IndexError):
            bd.day_bands(days, 3, "0930")


def random_days(n, seed):
    """n days with a bar at most minutes 18:01..16:00 (a few gaps), prices on a random walk."""
    rnd = random.Random(seed)
    price = 13000.0
    days = []
    for i in range(n):
        bars = []
        for sm in range(1, SM_1600 + 1):
            if rnd.random() < 0.03 and sm not in (1, SM_0931):
                continue
            o = price
            c = o + rnd.uniform(-6.0, 6.0)
            h = max(o, c) + rnd.uniform(0.0, 3.0)
            l = min(o, c) - rnd.uniform(0.0, 3.0)
            bars.append((sm, o, h, l, c, rnd.randint(0, 50)))
            price = c
        days.append(make_day(i, bars))
    return days


class NoLookAhead(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.days = random_days(22, seed=20211117)

    def test_no_lookahead(self):
        days = self.days
        for anchor in ("0930", "1800"):
            for k in (14, 17, 20):
                base = bd.day_bands(days, k, anchor)
                self.assertTrue(base, "%s day %d has a band" % (anchor, k))
                # Every bar of day k+1 onward changed: day k unchanged.
                later = days[:k + 1] + [copy_day(d, factor=1.37) for d in days[k + 1:]]
                self.assertEqual(points(bd.day_bands(later, k, anchor)), points(base), "%s k=%d" % (anchor, k))
                # Day k's bars after sm S changed: every band point at sm <= S unchanged.
                for S in (SM_0931, g.sm_of("11:45"), g.sm_of("02:00"), 1):
                    changed = days[:k] + [copy_day(days[k], change_after=S, factor=0.81)] + days[k + 1:]
                    after = bd.day_bands(changed, k, anchor)
                    want = {sm: v for sm, v in points(base).items() if sm <= S}
                    got = {sm: v for sm, v in points(after).items() if sm <= S}
                    self.assertEqual(got, want, "%s k=%d S=%d" % (anchor, k, S))
                    # and the change is visible after S (the test would catch a band that ignored it)
                    if any(sm > S for sm in base):
                        self.assertNotEqual(points(after), points(base))

    def test_earlier_days_do_matter(self):
        # Sanity for the test above: changing an earlier day does change day k's band.
        k = 17
        for anchor in ("0930", "1800"):
            base = bd.day_bands(self.days, k, anchor)
            changed = list(self.days)
            changed[k - 1] = copy_day(self.days[k - 1], change_after=g.sm_of("12:00"), factor=1.05)
            self.assertNotEqual(points(bd.day_bands(changed, k, anchor)), points(base), anchor)

    def test_repeat_calls_agree(self):
        for anchor in ("0930", "1800"):
            a = points(bd.day_bands(self.days, 18, anchor, lookback=10, mult=0.7))
            b = points(bd.day_bands(self.days, 18, anchor, lookback=10, mult=0.7))
            self.assertEqual(a, b)


def trimmed_to_market(days, market):
    """Like-for-like input for the band.py comparison (a test helper, not part of bands.py): only dates in
    market.py's session list, each Globex day's bars only up to that session's last bar (market's
    early-close cut); evening and overnight bars before 09:31 stay. The first session s1 is left out:
    band.py never commits s1 into the history (an NT8 start-up artifact, band.history_for), so the list
    starts at s2, whose own band is empty on both sides (no earlier day)."""
    by_date = {d.date: d for d in days}
    out = []
    for s in market.sessions[1:]:
        d = by_date[s.date]
        last = s.bars[-1].dt
        t = g.Day(d.date)
        for b in d.bars:
            if b.dt <= last:
                t.by_sm[b.sm] = len(t.bars)
                t.bars.append(b)
        out.append(t)
    return out


@unittest.skipUnless(os.path.exists(DATA), "data file absent")
class RealFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, os.path.join(REPO, "scripts", "wf", "oracle"))
        import market as mk   # noqa: E402
        import band as bo     # noqa: E402
        cls.bo = bo
        cls.market = mk.load_market(DATA, session_start="09:31")
        cls.days = trimmed_to_market(g.load_days(DATA), cls.market)

    def compare(self, lookback, mult, idxs):
        days, market = self.days, self.market
        by_date = {s.date: s for s in market.sessions}
        banded = 0
        for k in idxs:
            day = days[k]
            s = by_date[day.date]
            mine = bd.day_bands(days, k, "0930", lookback, mult)
            want = {}
            for _i, b, st in self.bo.iter_session_states(market, s.n, lookback, mult):
                sm = g.sm_of("%02d:%02d" % (b.mod // 60, b.mod % 60))
                self.assertTrue(SM_0931 <= sm <= SM_1600)
                self.assertEqual(day.bars[day.by_sm[sm]].dt, b.dt)
                if st.have_band:
                    want[sm] = st
                else:
                    self.assertNotIn(sm, mine, "%s %s: band where band.py has none" % (day.date, b.dt))
            self.assertEqual(sorted(mine), sorted(want), day.date)
            for sm, st in want.items():
                p = mine[sm]
                msg = "%s sm %d" % (day.date, sm)
                self.assertAlmostEqual(p.upper, st.upper, delta=1e-9, msg=msg)
                self.assertAlmostEqual(p.lower, st.lower, delta=1e-9, msg=msg)
                self.assertAlmostEqual(p.vwap, st.vwap, delta=1e-9, msg=msg)
                self.assertAlmostEqual(p.anchor_price, st.today_open, delta=1e-9, msg=msg)
                self.assertAlmostEqual(p.width, st.today_open * mult * st.sigma, delta=1e-9, msg=msg)
            banded += bool(want)
        return banded

    def sample(self):
        n = len(self.days)
        idxs = sorted(set([round(j * (n - 1) / 59.0) for j in range(60)]))
        self.assertEqual(len(idxs), 60)
        return idxs

    def test_0930_reproduces_band_py_on_real_file(self):
        idxs = self.sample()
        banded = self.compare(14, 1.0, idxs)
        self.assertGreaterEqual(banded, 58)
        # The warm-up edge: s15 (index 13) has 13 earlier days and no band, s16 (index 14) has 14 and one.
        self.assertEqual(self.compare(14, 1.0, [13]), 0)
        self.assertEqual(self.compare(14, 1.0, [14]), 1)

    def test_0930_reproduces_band_py_other_parameters(self):
        self.assertGreaterEqual(self.compare(10, 1.6, self.sample()[::4]), 14)


if __name__ == "__main__":
    unittest.main()
