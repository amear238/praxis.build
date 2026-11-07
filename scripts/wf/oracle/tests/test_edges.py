"""Edge-case tests W2 did not cover (W3, unit 2026-11-07-wf-oracles, U3b-2): early-close days, the Flat1559 15:59
bar under the stop, and an entry filling on a session's first bar. Calendar, BASE day and hand arithmetic as in
test_policy.py's docstring (s16 = 2021-03-29, ATR(14) sum 56 at s16, stop distance 6.0 at m 1.5, sigma 0,
Upper = max(s16 open, 1000), Lower = min(...)). Lookback 10 is used where the run must NOT be a T12 trio member
(trio = (14, 1.0, 1.5)); at s16 the Lookback-10 band also has sigma 0.
"""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import test_policy as tp  # noqa: E402  (fixture writers; its TestCases are not re-exported: module import only)

gr, T, P, SC = tp.gr, tp.T, tp.P, tp.SC

# (g1) s16 file last bar 13:15 -> NT8 cut 12:15 (sessions.py NT8_MAP), bars 12:16..13:15 dropped; F = 12:15.
EC1215_S16 = [tp.OPEN04,
              ("1000", 1004, 1006, 1004, 1006),       # 1006 > Upper 1004 -> EnterLong
              ("1001", 1006, 1007, 1006, 1006),       # fill 1006.5; level 1000.5
              ("1215", 1001, 1001, 1000, 1000.5),     # 14 x 6 = 84: first crossing ON F (stop suppressed, .cs :244/:250);
                                                      # Exit on session close at F's close 1000.5 - 0.5 = 1000.0 (l 1000)
              ("1230", 1000, 1000, 1000, 1000),       # dropped (past the cut)
              ("1315", 1000, 1000, 1000, 1000)]       # dropped; file last bar 13:15
# (g2) s16 file last bar 13:00 -> cut 12:00, which is both the last bar (F) and a checkpoint.
EC1200_S16 = [tp.OPEN04,
              ("1000", 1004, 1004, 1003, 1003),       # 1000 < 1003 < 1004: no entry
              ("1200", 1004, 1006, 1004, 1006),       # checkpoint step runs on F (§4 v2.1): 1006 > 1004 -> EnterLong
              ("1230", 1000, 1000, 1000, 1000),       # dropped
              ("1300", 1000, 1000, 1000, 1000)]       # dropped; file last bar 13:00
# s17 (BASE): the entry fills on s17 09:31 (first bar): open 1000 + 0.5 = 1000.5. At s17 10:00 (Lookback 10) the band
# has prev close 1006 (s16's last LOADED bar) -> Upper >= 1006 >= close 1000 -> BandOrVWAP XL, filled on the next
# loaded bar 10:30 at 1000 - 0.5 clipped to l 1000 -> 1000.0. Stop: s17 ATR sum = 13 x 4 + TR(s16) 6 = 58 ->
# level 1000.5 - 1.5 x 58 / 14 ~ 994.29; with s16's sum 56 -> 994.5; no s17 close (1000) crosses either.

# (h) Flat1559: first stop crossing on the 15:59 bar (F under Flat1559: .cs :234-238 returns before the stop).
F59_S16 = [tp.OPEN04,
           ("1530", 1004, 1006, 1004, 1006),          # EnterLong
           ("1531", 1006, 1007, 1006, 1006),          # fill 1006.5; level 1000.5
           ("1559", 1001, 1001, 1000.5, 1000.5),      # 14 x 6 = 84: crossing on F (15:59)
           ("1600", 1000.5, 1001, 1000, 1000.5)]      # FlatEOD = 16:00 open 1000.5 - 0.5 = 1000.0 (clipped at l 1000)


class EdgeTests(tp.PolicyBase):
    DAYS = {"EC1215": {16: EC1215_S16}, "EC1200": {16: EC1200_S16}, "F59": {16: F59_S16}}

    def all_verdicts(self, key, runs):
        ctx, V, t12 = self.grade(key, runs)
        vs, _t, _e = gr.run_graders(ctx)
        return ctx, {(v.test, v.run): v for v in vs}

    # (g1) early close 13:15 file -> F = 12:15; a trade open there exits by session close at 12:15 -> T9 PASS
    def test_g_early_close_1215(self):
        m = self.mk["EC1215"]
        s = m.sessions[15]
        self.assertEqual((s.nt8_last_bar, s.early, s.file_last_bar), ("12:15", True, "13:15"))
        self.assertEqual(s.bars[-1].dt, T(16, "1215"))
        self.assertEqual(gr.first_flat_pos(m, 16, "BandOrVWAP"), m.index[T(16, "1215")])
        tr = ("Long", T(16, "1001"), 1006.5, T(16, "1215"), 1000.0, SC)
        for pol in ("BandOrVWAP", "Flat1559"):
            ctx, V = self.all_verdicts("EC1215", [("E", [tr], P(pol, L=10))])
            self.assertEqual(V[("T9", "E")].verdict, "PASS", V[("T9", "E")])
            self.assertEqual(V[("T9", "E")].rows, [1])
            self.assertEqual(V[("T8(i-iv)", "E")].verdict, "PASS", V[("T8(i-iv)", "E")])
            # T12(ii): under Flat1559 a session close is allowed only on an early-close day's last bar: this one
            self.assertEqual(V[("T12(ii)", "E")].verdict, "PASS", V[("T12(ii)", "E")])
            self.assertEqual(V[("T12(iii)", "E")].verdict, "PASS")    # no checkpoint between 10:01 and F (excluded)

    # (g2) 13:00 file: 12:00 is the last bar AND a checkpoint; an entry decided there is not flagged by (v)
    # (i)  that entry fills on s17's first bar: grade.py flags it (W2 reading 6), unambiguous here
    def test_g_early_close_1200_checkpoint_entry_and_first_bar_flag(self):
        m = self.mk["EC1200"]
        s = m.sessions[15]
        self.assertEqual((s.nt8_last_bar, s.early), ("12:00", True))
        F = m.index[T(16, "1200")]
        self.assertTrue(gr.is_flat_pos(m, F, "BandOrVWAP"))
        self.assertTrue(gr._mk.is_checkpoint(gr.bar_at(m, F).mod))
        tr = ("Long", T(17, "0931"), 1000.5, T(17, "1030"), 1000.0, "XL")
        ctx, V = self.all_verdicts("EC1200", [("E", [tr], P("BandOrVWAP", L=10))])
        v = V[("T12(v)", "E")]
        self.assertEqual(v.verdict, "PASS", v)
        self.assertEqual(v.rows, [1])
        self.assertIn("early-close last bar: checkpoint step runs", v.lines[0])
        a = ctx.runs[0].anns[0]
        self.assertEqual(a.entry_pos, (17, 0))
        self.assertEqual(a.entry_dec_pos, F)
        self.assertTrue(any(x.startswith("FLAG: entry fills on the session's first bar") for x in a.notes), a.notes)
        self.assertFalse(a.ambiguous)
        self.assertEqual((a.c_pos, a.alt_c_pos), (None, None))
        self.assertEqual(V[("T12(iii)", "E")].verdict, "PASS")       # c* = s17 10:00 = d
        # a control: the same entry decided on a NON-checkpoint bar would be flagged by (v)
        self.assertFalse(gr._mk.is_checkpoint(gr.bar_at(m, m.index[T(16, "0931")]).mod))

    # (h) Flat1559, first crossing on 15:59: no XStop expected, FlatEOD -> T9 PASS; an XStop decided 15:59 -> FAIL
    def test_h_flat1559_crossing_on_1559(self):
        ok = ("Long", T(16, "1531"), 1006.5, T(16, "1600"), 1000.0, gr.FLATEOD)
        ctx, V = self.all_verdicts("F59", [("H", [ok], P("Flat1559", L=10))])
        a = ctx.runs[0].anns[0]
        self.assertEqual(a.c_pos, ctx.market.index[T(16, "1559")])
        self.assertTrue(a.c_flat)
        self.assertEqual(V[("T9", "H")].verdict, "PASS", V[("T9", "H")])
        self.assertEqual(V[("T8(i-iv)", "H")].verdict, "PASS", V[("T8(i-iv)", "H")])
        self.assertEqual(V[("T12(ii)", "H")].verdict, "PASS", V[("T12(ii)", "H")])
        bad = ("Long", T(16, "1531"), 1006.5, T(16, "1600"), 1000.0, "XStop")   # same price by the market rule
        ctx, V = self.all_verdicts("F59", [("H", [bad], P("Flat1559", L=10))])
        self.assertEqual(V[("T9", "H")].verdict, "FAIL", V[("T9", "H")])
        self.assertEqual(V[("T9", "H")].rows, [1])
        self.assertEqual(V[("T8(i-iv)", "H")].verdict, "FAIL", V[("T8(i-iv)", "H")])
        self.assertEqual(V[("T12(ii)", "H")].verdict, "FAIL")        # open at 15:59 but not FlatEOD


if __name__ == "__main__":
    unittest.main()
