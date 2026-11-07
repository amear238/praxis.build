"""Real-calendar checks on the 1-minute data file (values-spec §5 :86-87, §9 (a)/(e) :231/:235).
Skipped if the file is absent. The market is loaded once (setUpClass)."""
import os
import sys
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
if ORACLE not in sys.path:
    sys.path.insert(0, ORACLE)
import market as mk   # noqa: E402
import band as bd     # noqa: E402
import atr as at      # noqa: E402

DATA = os.environ.get("PRAXIS_ORACLE_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")


@unittest.skipUnless(os.path.exists(DATA), "data file absent: %s" % DATA)
class RealFileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        t0 = time.time()
        cls.m = mk.load_market(DATA, session_start="09:31")
        cls.load_s = time.time() - t0
        sys.stderr.write("\n[realfile] load_market %.2f s\n" % cls.load_s)

    def test_calendar(self):
        m = self.m
        self.assertEqual(m.N, 1352)
        for n, date in ((1, "2021-03-08"), (16, "2021-03-29"), (70, "2021-06-15"), (967, "2024-12-26"),
                        (1267, "2026-03-18"), (1352, "2026-07-17")):
            self.assertEqual(m.session(n).date, date)
        self.assertEqual(m.weekend_dates_dropped, 141)

    def test_early_close_cut(self):
        for date, nt8, last_mod in (("2024-12-24", "12:15", 735), ("2025-01-20", "12:00", 720),
                                    ("2025-06-19", "12:00", 720)):
            s = self.m.by_date[date]
            self.assertEqual(s.nt8_last_bar, nt8)
            self.assertEqual(s.bars[-1].mod, last_mod)
            self.assertGreater(s.cut_dropped, 0)

    def test_band_warmup(self):
        for L, first in ((10, 12), (14, 16), (18, 20)):
            self.assertFalse(bd.band_at(self.m, first - 1, "10:00", L, 1.0).have_band, (L, first))
            self.assertTrue(bd.band_at(self.m, first, "10:00", L, 1.0).have_band, (L, first))

    def test_atr_warmup(self):
        self.assertFalse(at.atr_at(self.m, 15)[0])
        self.assertTrue(at.atr_at(self.m, 16)[0])


if __name__ == "__main__":
    unittest.main()
