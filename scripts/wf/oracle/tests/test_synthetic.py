"""Synthetic-fixture tests for scripts/wf/oracle (market / band / atr). Every expected value is a literal or
explicit arithmetic from the fixture literals below -- never a call into the code under test.

Fixture (22 weekday sessions, 2021-03-08 Mon .. 2021-04-06 Tue; s_n has open 1024.0):
  09:31  o 1024 h 1026 l 1023 c 1025 v 10
  10:00  o=c=1024+d_n, h=c+1, l=c-1, v 20     d_n = (-1)**n * 0.25*n   (absent on s21)
  10:30  o=c=1024.5, h=1024+R_n, l=1024-R_n, v 30   R_n = 7 + n % 3
  16:00  o=h=l=c=E_n = 1024 + 0.5*(n % 5) - 1.0, v 40   (E_6 = 1034.0, a gap above s7's range)
  s10 2021-03-19 early close: no 16:00; 12:15 o=h=l=c=1044 v 40; 12:30 h 2000 l 500 (dropped); 13:15 c 1100
      (file last bar 13:15 -> NT8 cut 12:15, dropped bars 12:30 and 13:15)
  s13: the 10:00 bar has v 0.   s14: every bar v 0.
  Non-RTH noise: s2 has a 09:30 bar (o=h=l=c=1.0), s3 a 16:01 bar (c=9999); Sat 2021-03-13 10:00 bar 5000.
"""
import datetime as dt
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
if ORACLE not in sys.path:
    sys.path.insert(0, ORACLE)
import market as mk   # noqa: E402
import band as bd     # noqa: E402
import atr as at      # noqa: E402

START, END = "2021-03-08", "2026-07-17"


def weekdays(first, count):
    d, out = first, []
    while len(out) < count:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


DATES = weekdays(dt.date(2021, 3, 8), 22)
D = {n: (-1) ** n * 0.25 * n for n in range(1, 23)}
R = {n: 7 + n % 3 for n in range(1, 23)}
E = {n: 1024 + 0.5 * (n % 5) - 1.0 for n in range(1, 23)}
E[6] = 1034.0
E[10] = 1044.0   # s10's last LOADED close is the 12:15 bar


def line(day, hhmmss, o, h, l, c, v):
    return "%s %s;%r;%r;%r;%r;%d\n" % (day.strftime("%Y%m%d"), hhmmss, o, h, l, c, v)


def build_fixture(path, extra=None):
    out = []
    for n, day in enumerate(DATES, 1):
        z = 0 if n == 14 else 1
        if n == 2:
            out.append(line(day, "093000", 1.0, 1.0, 1.0, 1.0, 5))
        out.append(line(day, "093100", 1024.0, 1026.0, 1023.0, 1025.0, 10 * z))
        if n != 21:
            c = 1024 + D[n]
            out.append(line(day, "100000", c, c + 1, c - 1, c, 0 if n == 13 else 20 * z))
        out.append(line(day, "103000", 1024.5, 1024.0 + R[n], 1024.0 - R[n], 1024.5, 30 * z))
        if n == 10:
            out.append(line(day, "121500", 1044.0, 1044.0, 1044.0, 1044.0, 40))
            out.append(line(day, "123000", 1044.0, 2000.0, 500.0, 1044.0, 1000))
            out.append(line(day, "131500", 1100.0, 1100.0, 1100.0, 1100.0, 50))
        else:
            out.append(line(day, "160000", E[n], E[n], E[n], E[n], 40 * z))
        if n == 3:
            out.append(line(day, "160100", 9999.0, 9999.0, 9999.0, 9999.0, 7))
        if n == 5:   # Friday 2021-03-12 -> Saturday 2021-03-13 weekend bar inside 09:31-16:00
            out.append(line(dt.date(2021, 3, 13), "100000", 5000.0, 5000.0, 5000.0, 5000.0, 999))
    if extra:
        out.extend(extra)
    with open(path, "w") as fh:
        fh.writelines(out)


class SyntheticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="w1-oracle-")
        cls.path = os.path.join(cls.tmp, "fixture.txt")
        build_fixture(cls.path)
        cls.m = mk.load_market(cls.path, START, END, session_start="09:31")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    # ---- calendar / loading ----
    def test_calendar_and_weekend_drop(self):
        m = self.m
        self.assertEqual(m.N, 22)
        self.assertEqual(m.sessions[0].date, "2021-03-08")
        self.assertEqual(m.by_date["2021-03-12"].n, 5)
        self.assertEqual(m.by_date["2021-03-15"].n, 6)          # Saturday did not become s6
        self.assertNotIn("2021-03-13", m.by_date)
        self.assertEqual(m.weekend_bars_dropped, 1)
        self.assertEqual(m.weekend_dates_dropped, 1)
        pb = mk.prev_bar(m, 6, 0)                                # Monday's previous loaded bar = Friday 16:00
        self.assertEqual((pb.dt, pb.c), (dt.datetime(2021, 3, 12, 16, 0), E[5]))
        self.assertIsNone(mk.prev_bar(m, 1, 0))

    def test_non_rth_bars_ignored(self):
        s2, s3 = self.m.session(2), self.m.session(3)
        self.assertEqual(s2.bars[0].mod, 9 * 60 + 31)
        self.assertEqual(s2.bars[0].o, 1024.0)
        self.assertEqual(s3.bars[-1].mod, 960)
        self.assertEqual(bd.band_at(self.m, 4, 0, 10, 1.0).prev_close, E[3])   # not 9999.0
        # This fixture HAS a pre-09:31 bar (s2 09:30): at "08:31" it is loaded as s2's first bar, so the two
        # starts differ here (the fixtures of test_grade / test_policy have none; see test_grade).
        m0831 = mk.load_market(self.path, START, END, session_start="08:31")
        self.assertEqual((m0831.session(2).bars[0].mod, m0831.session(2).bars[0].o), (9 * 60 + 30, 1.0))
        self.assertEqual(m0831.pre_open_bars, 1)
        self.assertEqual([len(s.bars) for s in m0831.sessions if s.n != 2],
                         [len(s.bars) for s in self.m.sessions if s.n != 2])

    def test_early_close_cut(self):
        s10 = self.m.session(10)
        self.assertEqual(s10.date, "2021-03-19")
        self.assertTrue(s10.early)
        self.assertEqual(s10.nt8_last_bar, "12:15")
        self.assertEqual([b.mod for b in s10.bars], [571, 600, 630, 735])
        self.assertEqual(s10.cut_dropped, 2)
        rec = self.m.records()[9]
        self.assertEqual((rec.high, rec.low), (1044.0, 1024.0 - 8))   # not 2000 / 500
        self.assertEqual(self.m.records()[10].prev_close, 1044.0)      # s11's PrevClose = 12:15 close
        self.assertEqual(bd.band_at(self.m, 11, 0, 10, 1.0).prev_close, 1044.0)
        self.assertTrue(mk.is_session_flat(self.m, 10, 3, "BandOrVWAP"))  # 12:15 is the session's last bar
        self.assertFalse(mk.is_session_flat(self.m, 10, 2, "Flat1559"))

    def test_unmapped_early_close_raises(self):
        p = os.path.join(self.tmp, "bad.txt")
        build_fixture(p, extra=[line(dt.date(2021, 4, 7), "093100", 1024.0, 1025.0, 1023.0, 1024.0, 1),
                                line(dt.date(2021, 4, 7), "133000", 1024.0, 1025.0, 1023.0, 1024.0, 1)])
        with self.assertRaises(mk.NotSettledBySpec):
            mk.load_market(p, START, END, session_start="09:31")

    # ---- band warm-up: s1 drop ----
    def _sig(self, ns, L):
        s = 0.0
        for n in ns:                         # newest -> oldest, as the .cs loop
            s += abs((1024 + D[n]) / 1024.0 - 1.0)
        return s / L

    def test_band_first_session_per_lookback(self):
        m = self.m
        for L, first in ((10, 12), (14, 16), (18, 20)):
            self.assertFalse(bd.band_at(m, first - 1, "10:00", L, 1.0).have_band, (L, first))
            self.assertEqual(bd.band_at(m, first - 1, "10:00", L, 1.0).cnt, first - 3)
            st = bd.band_at(m, first, "10:00", L, 1.0)
            self.assertTrue(st.have_band, (L, first))
            self.assertEqual(st.cnt, L)
        self.assertFalse(bd.band_at(m, 1, "10:00", 2, 1.0).have_band)   # s1: no day at all

    def test_sigma_bands_vwap_s12(self):
        st = bd.band_at(self.m, 12, "10:00", 10, 0.8)
        # history s2..s11: sum |d_n|/1024 = 0.25*(2+...+11)/1024 = 16.25/1024, exact in binary
        self.assertEqual(st.sigma, 16.25 / 1024 / 10)
        self.assertEqual(st.sigma, self._sig(range(11, 1, -1), 10))
        self.assertEqual(st.today_open, 1024.0)
        self.assertEqual(st.prev_close, 1023.5)             # E_11
        self.assertEqual(st.upper, 1024.0 * (1.0 + 0.8 * (16.25 / 1024 / 10)))
        self.assertEqual(st.lower, 1023.5 * (1.0 - 0.8 * (16.25 / 1024 / 10)))
        # VWAP: 09:31 tp = (1026+1023+1025)/3, v 10; 10:00 bar c = 1024 + 3.0 = 1027, h 1028, l 1026, v 20
        pv = ((1026.0 + 1023.0 + 1025.0) / 3.0) * 10.0
        pv += ((1028.0 + 1026.0 + 1027.0) / 3.0) * 20.0
        self.assertEqual(st.vwap_cum_vol, 30.0)
        self.assertEqual(st.vwap, pv / 30.0)

    def test_sigma_s16_s20(self):
        st = bd.band_at(self.m, 16, "10:00", 14, 1.2)
        self.assertEqual(st.sigma, 0.25 * 119 / 1024 / 14)     # s2..s15: 2+..+15 = 119
        st = bd.band_at(self.m, 20, "10:00", 18, 1.0)
        self.assertEqual(st.sigma, 0.25 * 189 / 1024 / 18)     # s2..s19: 2+..+19 = 189
        self.assertEqual(st.upper, max(1024.0, E[19]) * (1.0 + 1.0 * (0.25 * 189 / 1024 / 18)))

    def test_history_day_missing_minute_is_skipped(self):
        st = bd.band_at(self.m, 22, "10:00", 10, 1.0)
        # history newest s21 lacks 10:00 -> skipped; the loop takes s20..s11: 11+..+20 = 155
        self.assertEqual(st.cnt, 10)
        self.assertEqual(st.sigma, 0.25 * 155 / 1024 / 10)
        self.assertEqual(st.sigma, self._sig(range(20, 10, -1), 10))
        # 10:30 every day has |1024.5/1024 - 1| = 0.5/1024 -> sigma exactly 0.5/1024
        self.assertEqual(bd.band_at(self.m, 22, "10:30", 10, 1.0).sigma, 0.5 / 1024)
        with self.assertRaises(KeyError):
            bd.band_at(self.m, 21, "10:00", 10, 1.0)          # s21 has no 10:00 bar

    def test_history_cap(self):
        h = bd.history_for(self.m, 22, 2)                    # cap 2+15 = 17 of s2..s21 (20) -> s5..s21
        self.assertEqual([r.n for r in h], list(range(5, 22)))
        self.assertEqual([r.n for r in bd.history_for(self.m, 12, 10)], list(range(2, 12)))

    def test_zero_volume(self):
        st = bd.band_at(self.m, 13, "10:00", 10, 1.0)        # 10:00 v 0: VWAP = first bar's tp only
        self.assertEqual(st.vwap_cum_vol, 10.0)
        self.assertEqual(st.vwap, (((1026.0 + 1023.0 + 1025.0) / 3.0) * 10.0) / 10.0)
        st = bd.band_at(self.m, 14, "10:00", 10, 1.0)        # all v 0: VWAP falls back to Close
        self.assertEqual(st.vwap_cum_vol, 0.0)
        self.assertEqual(st.vwap, 1024 + 3.5)
        self.assertTrue(st.have_band)

    def test_iter_matches_band_at(self):
        got = [(i, b.mod, s.have_band) for i, b, s in bd.iter_session_states(self.m, 12, 10, 1.0)]
        # 16:00: s10 (early close, cut 12:15) has no 16:00 close, so s2..s11 yield only 9 -> no band (.cs :354, :360)
        self.assertEqual(got, [(0, 571, True), (1, 600, True), (2, 630, True), (3, 960, False)])
        self.assertEqual(bd.band_at(self.m, 12, "16:00", 10, 1.0).cnt, 9)
        self.assertTrue(bd.band_at(self.m, 13, "16:00", 10, 1.0).have_band)   # s2..s12 minus s10 = 10

    # ---- ATR ----
    def test_atr_first_at_s16(self):
        self.assertEqual(at.atr_at(self.m, 15), (False, 0.0, 0.0))
        self.assertEqual(at.atr_at(self.m, 1), (False, 0.0, 0.0))
        # TR s2..s15 by hand (H, L, PrevClose):
        # s2 1033/1015/1023.5=18  s3 1031/1017/1024=14  s4 1032/1016/1024.5=16  s5 1033/1015/1025=18
        # s6 1034/1017/1023=17    s7 1032/1016/1034=18  s8 1033/1015/1024=18    s9 1031/1017/1024.5=14
        # s10 1044/1016/1025=28   s11 1033/1015/1044=29 s12 1031/1017/1023.5=14 s13 1032/1016/1024=16
        # s14 1033/1015/1024.5=18 s15 1031/1017/1025=14 -> sum 252
        self.assertEqual(at.atr_at(self.m, 16), (True, 252.0, 18.0))

    def test_stop_level_and_cross(self):
        self.assertEqual(at.stop_level("Long", 1000.0, 1.5, 252.0), 973.0)     # 1000 - 1.5*18
        self.assertEqual(at.stop_level("Short", 1000.0, 2.25, 252.0), 1040.5)  # 1000 + 2.25*18
        self.assertTrue(at.stop_crossed("Long", 1000.0, 973.0, 1.5, 252.0))    # tie is a crossing
        self.assertFalse(at.stop_crossed("Long", 1000.0, 973.25, 1.5, 252.0))  # one tick short
        self.assertTrue(at.stop_crossed("Short", 1000.0, 1040.5, 2.25, 252.0))
        self.assertFalse(at.stop_crossed("Short", 1000.0, 1040.25, 2.25, 252.0))
        self.assertTrue(at.stop_crossed("Long", 1000.0, 960.0, 1.5, 252.0))
        for bad in (0, 0.0, -1.5):
            with self.assertRaises(ValueError):
                at.stop_level("Long", 1000.0, bad, 252.0)
            with self.assertRaises(ValueError):
                at.stop_crossed("Long", 1000.0, 973.0, bad, 252.0)
        with self.assertRaises(ValueError):
            at.stop_crossed("LONG", 1000.0, 973.0, 1.5, 252.0)

    # ---- small rules ----
    def test_checkpoint_policy_fills(self):
        self.assertTrue(mk.is_checkpoint(600))
        self.assertTrue(mk.is_checkpoint(930))
        for mod in (570, 960, 601, 615):
            self.assertFalse(mk.is_checkpoint(mod))
        self.assertEqual(mk.session_flat_mods("Flat1559"), 959)
        self.assertEqual(mk.session_flat_mods("BandOrVWAP"), 960)
        self.assertEqual(mk.session_flat_mods("OppBand"), 960)
        for bad in (0, 1, 2, "oppband", None):
            with self.assertRaises(ValueError):
                mk.session_flat_mods(bad)
        b = mk.Bar(dt.datetime(2021, 3, 8, 16, 0), 960, 100.0, 100.25, 99.0, 99.5, 1)
        self.assertEqual(mk.market_fill(b, True), 100.25)    # 100.5 clipped to h
        self.assertEqual(mk.market_fill(b, False), 99.5)
        self.assertEqual(mk.session_close_fill(b, True), 100.0)
        self.assertEqual(mk.session_close_fill(b, False), 99.0)
        self.assertEqual(mk.flateod_fill(b, False), 99.5)


if __name__ == "__main__":
    unittest.main()
