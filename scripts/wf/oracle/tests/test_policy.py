"""Synthetic-fixture tests for scripts/wf/oracle/policy.py (T12) — W3, unit 2026-11-07-wf-oracles (U3b-2).

Calendar (reused from test_grade.py): 17 weekdays 2021-03-08 (s1) .. 2021-03-30 (s17); 2021-03-29 is s16.
BASE day (every session unless overridden), volume 10 on every bar:
  09:31 o1000 h1002 l998 c1000; every checkpoint 10:00, 10:30, ..., 15:30; 15:59; 16:00 — all o=h=l=c=1000.
Hand arithmetic used throughout (s16, Lookback 14 or 10, k 1.0, m 1.5):
  * ATR(14) sum at s16 = 14 x TR 4 (max(1002, prev close 1000) - min(998, 1000)) = 56; stop distance
    1.5 x 56 / 14 = 6.0, i.e. the exact test 14 x (fill - close) >= 84 (long).
  * Band at s16: every history close at every checkpoint minute = 1000 = the day's open, so sigma = 0 exactly and
    Upper = max(today open, prev close) = max(1004, 1000) = 1004.0, Lower = min(...) = 1000.0 (s16 opens 1004 in
    every override below; prev close = s15 16:00 = 1000).
  * Fills (market.py defaults): market order = next bar's open +/- 0.5 (adverse) clipped to [l, h]; session close =
    close -/+ 0.5 clipped; FlatEOD = the 16:00 bar's open -/+ 0.5 clipped.
"""
import io
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
if ORACLE not in sys.path:
    sys.path.insert(0, ORACLE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import grade as gr       # noqa: E402
import market as mk      # noqa: E402
import policy as pl      # noqa: E402
import test_grade as tg  # noqa: E402  (W2's calendar, T() and bridge writer; its TestCase is not re-exported)

T = tg.T
DATES = tg.DATES
SC = gr.SESSION_CLOSE
CKPT = ["%02d%02d" % (h, m) for h in range(10, 16) for m in (0, 30)]
BASE = [("0931", 1000, 1002, 998, 1000)] + [(hm, 1000, 1000, 1000, 1000) for hm in CKPT + ["1559", "1600"]]
TAIL = [("1559", 1000, 1000, 1000, 1000), ("1600", 1000, 1000, 1000, 1000)]
OPEN04 = ("0931", 1004, 1006, 1002, 1004)   # s16 open 1004 -> Upper 1004, Lower 1000


def P(policy, L=14, k=1.0, m=1.5):
    return {"Lookback": L, "NoiseMult": k, "StopAtrMult": m, "ExitPolicy": policy}


def write_data(path, overrides, vol=None):
    """overrides: {n: [(hhmm, o, h, l, c[, v])]} (sorted by time here); vol: {n: default volume}."""
    out = []
    for n, day in enumerate(DATES, 1):
        rows = sorted(overrides.get(n, BASE), key=lambda r: r[0])
        for r in rows:
            v = r[5] if len(r) > 5 else (vol or {}).get(n, 10)
            out.append("%s %s00;%r;%r;%r;%r;%d\n" % (day.strftime("%Y%m%d"), r[0], float(r[1]), float(r[2]),
                                                     float(r[3]), float(r[4]), v))
    with open(path, "w") as fh:
        fh.writelines(out)


# ---- TRIO day (s16): the three policies diverge; hand trace per bar ----------------------------------
TRIO_S16 = [OPEN04,
            ("1000", 1004, 1006, 1004, 1006),      # 1006 > Upper 1004 -> EnterLong (all three)
            ("1001", 1006, 1007, 1006, 1006),      # long fill 1006 + 0.5 = 1006.5; level 1000.5
            ("1030", 1006, 1006, 1003, 1003),      # stop 14x3.5=49<84. BandOrVWAP/Flat1559: 1003 <= max(1004, vwap) -> XL;
                                                   # OppBand: 1003 <= Lower 1000? no -> hold. 1003 < 1000? no -> no reversal
            ("1031", 1003, 1003, 1002, 1003),      # XL fill 1003 - 0.5 = 1002.5
            ("1045", 1001, 1001, 1000.5, 1000.5),  # OppBand long: 14 x 6 = 84 >= 84 -> XStop (tie on the stop, exact)
            ("1046", 1000.5, 1001, 1000, 1000.5),  # XStop fill 1000.5 - 0.5 = 1000.0
            ("1100", 1000, 1000, 999, 999),        # all flat: 999 < Lower 1000 -> EnterShort
            ("1101", 999, 1000, 998, 999),         # short fill 999 - 0.5 = 998.5; level 1004.5
            ("1130", 1004, 1004.25, 1004, 1004.25),  # stop 14x5.75=80.5<84. XS under all three (>= min(1000,vwap) /
                                                     # >= Upper 1004); 1004.25 > Upper 1004 -> EnterLong (reversal)
            ("1131", 1004.25, 1005, 1004, 1004.5),   # XS and L both fill 1004.25 + 0.5 = 1004.75; long level 998.75
            ("1140", 999, 999, 998.75, 998.75),      # 14 x 6 = 84 -> XStop (all three)
            ("1141", 998.75, 999, 998, 998.5),       # XStop fill 998.75 - 0.5 = 998.25
            ("1530", 1004, 1006, 1004, 1006),        # EnterLong
            ("1531", 1006, 1007, 1006, 1006),        # fill 1006.5
            ("1559", 1006, 1006, 1006, 1006),        # Flat1559: F (mod 959) -> FlatEOD
            ("1600", 1006, 1007, 1006, 1006)]        # session close 1006-0.5 clipped to l 1006 -> 1006.0;
                                                     # FlatEOD open 1006-0.5 clipped -> 1006.0
R1_XL = ("Long", T(16, "1001"), 1006.5, T(16, "1031"), 1002.5, "XL")
R2_XS = ("Short", T(16, "1101"), 998.5, T(16, "1131"), 1004.75, "XS")
R3_STOP = ("Long", T(16, "1131"), 1004.75, T(16, "1141"), 998.25, "XStop")
R4 = lambda name, px=1006.0: ("Long", T(16, "1531"), 1006.5, T(16, "1600"), px, name)   # noqa: E731
TRADES_A = [R1_XL, R2_XS, R3_STOP, R4(SC)]
TRADES_B = [("Long", T(16, "1001"), 1006.5, T(16, "1046"), 1000.0, "XStop"), R2_XS, R3_STOP, R4(SC)]
TRADES_C = [R1_XL, R2_XS, R3_STOP, R4(gr.FLATEOD)]

# ---- ZV day (s16): zero-volume rule. Typical prices (h+l+c)/3: 09:31 1004, 10:00 3016/3, 10:01 3019/3, 10:30 3016/3.
ZV_S16 = [OPEN04,
          ("1000", 1004, 1006, 1004, 1006),        # EnterLong
          ("1001", 1006, 1007, 1006, 1006),        # fill 1006.5
          ("1030", 1006, 1006, 1005, 1005),        # vol 10: VWAP = (1004 + 3016/3 + 3019/3 + 3016/3)/4 = 1005.25 ->
                                                   # trail max(1004, 1005.25); 1005 <= 1005.25 -> XL here.
                                                   # vol 0: band alone, 1005 <= 1004? no -> hold
          ("1031", 1005, 1005, 1004, 1005),        # XL fill 1004.5
          ("1100", 1004, 1004, 1003.5, 1003.5),    # vol 0: 1003.5 <= 1004 -> XL
          ("1101", 1003.5, 1004, 1003, 1003.5)] + TAIL   # XL fill 1003.0; stop never (14 x 3 = 42 < 84)

# ---- TIE day (s16): OppBand short whose XS decision close equals Upper exactly (sigma 0 -> 1004.0).
TIE_S16 = [OPEN04,
           ("1000", 1000, 1000, 999, 999),         # 999 < Lower 1000 -> EnterShort
           ("1001", 999, 1000, 998, 999),          # fill 998.5; level 1004.5
           ("1030", 1003, 1004, 1003, 1004),       # 1004 >= Upper 1004.0: |1004 - 1004| = 0 <= 1e-9 x 1004 -> tie
           ("1031", 1004, 1005, 1004, 1004.5)] + TAIL   # XS fill 1004.5

# ---- NOPOW day (s16): every trade exits by a non-checkpoint XStop -> no rule can move c*.
NOPOW_S16 = [OPEN04, ("1000", 1004, 1006, 1004, 1006), ("1001", 1006, 1007, 1006, 1006),
             ("1005", 1001, 1001, 1000.5, 1000.5),  # 14 x 6 = 84 -> XStop
             ("1006", 1000.5, 1001, 1000, 1000.5)] + TAIL   # fill 1000.0

# ---- REV day (s16): OppBand stop-and-reverse; open 1002 -> Upper 1002, Lower 1000.
REV_S16 = [("0931", 1002, 1003, 1001, 1002),
           ("1000", 1002, 1002.25, 1002, 1002.25),  # 1002.25 > Upper 1002 -> EnterLong
           ("1001", 1002.25, 1003, 1002, 1002.5),   # fill 1002.75; level 996.75
           ("1030", 1001, 1001, 999, 999),          # stop 14x3.75=52.5<84. OppBand: 999 <= Lower 1000 -> XL, and
                                                    # 999 < Lower 1000 -> EnterShort: reversal on the 10:31 bar
           ("1031", 999, 999.5, 998, 998.5),        # XL and S fill 999 - 0.5 = 998.5; short level 1004.5
           ("1032", 998.5, 999, 998, 998.5),        # (the FAIL variant's S fill: 998.0)
           ("1100", 1001, 1001, 1001, 1001),        # OppBand short: 1001 >= Upper 1002? no
           ("1559", 1000, 1000, 1000, 1000),
           ("1600", 1000, 1001, 1000, 1000)]        # session close (buy) 1000 + 0.5 = 1000.5


class PolicyBase(unittest.TestCase):
    DAYS = {}
    VOL = {}

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="w3-policy-")
        cls.mk, cls.paths = {}, {}
        for key, ov in cls.DAYS.items():
            p = os.path.join(cls.tmp, "w3-data-%s.txt" % key)
            write_data(p, ov, cls.VOL.get(key))
            cls.paths[key] = p
            cls.mk[key] = mk.load_market(p, session_start="09:31")
        cls.k = 0

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def grade(self, key, runs):
        """runs: [(label, trades, params)] -> (ctx, {(test, run): Verdict}, t12 list)."""
        specs = []
        for label, trades, params in runs:
            type(self).k += 1
            p = os.path.join(self.tmp, "w3-trades-%d.json" % self.k)
            tg.write_bridge(p, trades)
            specs.append(dict(params, label=label, path=p, format="bridge"))
        ctx = gr.build_ctx(self.mk[key], specs)
        vs, t12, err = gr.run_graders(ctx)
        self.assertIsNone(err)
        self.assertIsNotNone(t12, "policy.py not loaded by grade.load_policy")
        return ctx, {(v.test, v.run): v for v in t12}, t12


class PolicyTests(PolicyBase):
    DAYS = {"TRIO": {16: TRIO_S16}, "ZV0": {16: ZV_S16}, "ZV10": {16: ZV_S16}, "TIE": {16: TIE_S16},
            "NOPOW": {16: NOPOW_S16}, "REV": {16: REV_S16}}
    VOL = {"ZV0": {16: 0}}

    def trio(self, c_trades=TRADES_C, b_trades=TRADES_B):
        return self.grade("TRIO", [("A", TRADES_A, P("BandOrVWAP")), ("B", b_trades, P("OppBand")),
                                   ("C", c_trades, P("Flat1559"))])

    def test_fixture_band_atr_by_hand(self):
        m = self.mk["TRIO"]
        st = gr.Ctx(m, []).band(m.index[T(16, "1030")], 14, 1.0)
        self.assertTrue(st.have_band)
        self.assertEqual((st.sigma, st.upper, st.lower), (0.0, 1004.0, 1000.0))
        self.assertEqual(gr._atr.atr_at(m, 16)[:2], (True, 56.0))

    def test_trio_pass_every_part(self):
        _ctx, V, t12 = self.trio()
        self.assertEqual(V[("T12", "all")].verdict, "PASS", V[("T12", "all")])
        for test in ("T12(ii)", "T12(iii)", "T12(iv)", "T12(v)"):
            for lab in "ABC":
                self.assertEqual(V[(test, lab)].verdict, "PASS", V[(test, lab)])
        self.assertEqual(V[("T12(i)", "all")].verdict, "PASS")
        # (i) first differing rows by hand: A/B row 1 (XL vs XStop), A/C row 4 (session close vs FlatEOD), B/C row 1
        self.assertEqual(V[("T12(i)", "all")].rows, ["A#1", "B#1", "A#4", "C#4", "B#1", "C#1"])
        # (iv): A's XL at 10:30 (1003 not < 1000) -> next entry 11:01 later; XS at 11:30 (1004.25 > 1004) -> reversal
        self.assertEqual(V[("T12(iv)", "A")].rows, [1, 2])
        self.assertEqual(V[("T12(vii) power", "all")].verdict, "PASS")
        self.assertEqual(V[("T12(vii) power", "all")].rows, ["A#1", "B#1"])
        for lab, rows in (("A", [3]), ("B", [1, 3]), ("C", [3])):
            self.assertEqual(V[("T12(vii) stop", lab)].rows, rows)
        self.assertIn("count 0", V[("T12(vi)", "A")].reason)

    # (a) Flat1559 FlatEOD rows at 16:00 -> (ii) PASS; a 16:00 session close -> FAIL; an off-rule price -> not PASS
    def test_a_flat1559_names(self):
        _c, V, _t = self.trio()
        v = V[("T12(ii)", "C")]
        self.assertEqual(v.verdict, "PASS")
        self.assertTrue(any("row 4 open at 15:59 exits FlatEOD s16 2021-03-29 16:00 at 1006.0" in x for x in v.lines),
                        v.lines)   # 16:00 open 1006 - 0.5 = 1005.5 clipped to the bar's low 1006 -> 1006.0
        _c, V, _t = self.trio(c_trades=[R1_XL, R2_XS, R3_STOP, R4(SC)])
        v = V[("T12(ii)", "C")]
        self.assertEqual(v.verdict, "FAIL")
        self.assertEqual(v.rows, [4])
        self.assertTrue(any("on a 16:00 bar" in x for x in v.lines))
        self.assertTrue(any("expected FlatEOD" in x for x in v.lines))
        self.assertEqual(V[("T12", "all")].verdict, "FAIL")
        _c, V, _t = self.trio(c_trades=[R1_XL, R2_XS, R3_STOP, R4(gr.FLATEOD, 1005.5)])   # unclipped: wrong rule
        v = V[("T12(ii)", "C")]
        self.assertEqual(v.verdict, "UNTESTED")    # fill-rule fit fails -> the price is not graded (T8 gating)
        self.assertEqual(v.rows, [4])
        self.assertNotEqual(V[("T12", "all")].verdict, "PASS")

    # (b) OppBand reversal pair -> (iv) PASS; S entry one bar later -> FAIL
    def test_b_oppband_reversal(self):
        xl = ("Long", T(16, "1001"), 1002.75, T(16, "1031"), 998.5, "XL")
        s_ok = ("Short", T(16, "1031"), 998.5, T(16, "1600"), 1000.5, SC)
        _c, V, _t = self.grade("REV", [("R", [xl, s_ok], P("OppBand"))])
        v = V[("T12(iv)", "R")]
        self.assertEqual(v.verdict, "PASS", v)
        self.assertEqual(v.rows, [1])
        self.assertEqual(V[("T12(iii)", "R")].verdict, "PASS")      # c* = 10:30 (999 <= Lower 1000) = d
        s_late = ("Short", T(16, "1032"), 998.0, T(16, "1600"), 1000.5, SC)
        _c, V, _t = self.grade("REV", [("R", [xl, s_late], P("OppBand"))])
        v = V[("T12(iv)", "R")]
        self.assertEqual(v.verdict, "FAIL", v)
        self.assertEqual(v.rows, [1, 2])
        self.assertIn("expect a Short entry filling s16 2021-03-29 10:31", v.lines[0])

    # (c) BandOrVWAP XL at the right c* -> (iii) PASS; one checkpoint late -> FAIL naming the row
    def test_c_bandorvwap_cstar(self):
        _c, V, _t = self.grade("TRIO", [("A", [R1_XL], P("BandOrVWAP"))])
        self.assertEqual(V[("T12(iii)", "A")].verdict, "PASS")
        late = ("Long", T(16, "1001"), 1006.5, T(16, "1101"), 998.5, "XL")   # decided 11:00; c* = 10:30
        _c, V, _t = self.grade("TRIO", [("A", [late], P("BandOrVWAP"))])
        v = V[("T12(iii)", "A")]
        self.assertEqual(v.verdict, "FAIL")
        self.assertEqual(v.rows, [1])
        self.assertIn("row 1 Long XL decided s16 2021-03-29 11:00 but c* = s16 2021-03-29 10:30", v.lines[0])

    # (d) zero volume: band alone
    def test_d_zero_volume_band_alone(self):
        for key, vol_ok in (("ZV0", True), ("ZV10", False)):
            m = self.mk[key]
            st = gr.Ctx(m, []).band(m.index[T(16, "1030")], 14, 1.0)
            if vol_ok:
                self.assertEqual(st.vwap_cum_vol, 0.0)
                self.assertEqual(pl.exit_level("BandOrVWAP", "Long", st), 1004.0)
            else:
                vw = (1004.0 + 3016 / 3 + 3019 / 3 + 3016 / 3) / 4   # 1005.25 (equal volumes)
                self.assertAlmostEqual(st.vwap, vw, places=9)
                self.assertAlmostEqual(pl.exit_level("BandOrVWAP", "Long", st), 1005.25, places=9)
        x1100 = ("Long", T(16, "1001"), 1006.5, T(16, "1101"), 1003.0, "XL")
        x1030 = ("Long", T(16, "1001"), 1006.5, T(16, "1031"), 1004.5, "XL")
        _c, V, _t = self.grade("ZV0", [("Z", [x1100], P("BandOrVWAP", L=10))])
        self.assertEqual(V[("T12(iii)", "Z")].verdict, "PASS")
        _c, V, _t = self.grade("ZV0", [("Z", [x1030], P("BandOrVWAP", L=10))])
        self.assertEqual(V[("T12(iii)", "Z")].verdict, "FAIL")
        self.assertIn("decided s16 2021-03-29 10:30 but c* = none", V[("T12(iii)", "Z")].lines[0])   # 1005 > 1004: no exit by 10:30
        _c, V, _t = self.grade("ZV10", [("Z", [x1030], P("BandOrVWAP", L=10))])
        self.assertEqual(V[("T12(iii)", "Z")].verdict, "PASS")

    # (e) tie listed, not graded, count printed
    def test_e_tie_listed_not_graded(self):
        xs = ("Short", T(16, "1001"), 998.5, T(16, "1031"), 1004.5, "XS")
        _c, V, _t = self.grade("TIE", [("Q", [xs], P("OppBand", L=10))])
        vi = V[("T12(vi)", "Q")]
        self.assertIn("count 2", vi.reason)            # (iii) c* walk at 10:30 and (iv) opposite band at 10:30
        self.assertTrue(any(x.startswith("(iii) row 1") and "tie" in x for x in vi.lines))
        self.assertTrue(any(x.startswith("(iv) row 1") and "tie" in x for x in vi.lines))
        self.assertEqual(V[("T12(iii)", "Q")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(iv)", "Q")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(v)", "Q")].verdict, "PASS")   # 999 vs Lower 1000: not a tie

    # (f) (vii) cross-apply finds a difference (trio test above) / finds none -> UNTESTED
    def test_f_power_none_untested(self):
        stop = ("Long", T(16, "1001"), 1006.5, T(16, "1006"), 1000.0, "XStop")
        _c, V, _t = self.grade("NOPOW", [("A", [stop], P("BandOrVWAP")), ("B", [stop], P("OppBand")),
                                         ("C", [stop], P("Flat1559"))])
        v = V[("T12(vii) power", "all")]
        self.assertEqual(v.verdict, "UNTESTED")
        self.assertIn("no trade whose c* differs", v.reason)
        self.assertEqual(V[("T12(i)", "all")].verdict, "FAIL")      # identical lists
        self.assertEqual(V[("T12", "all")].verdict, "FAIL")

    def test_missing_trio_member_untested(self):
        _c, V, _t = self.grade("TRIO", [("A", TRADES_A, P("BandOrVWAP")), ("C", TRADES_C, P("Flat1559"))])
        self.assertEqual(V[("T12(i)", "all")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(vii) power", "all")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(vii) stop", "T12b")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(ii)", "T12b")].verdict, "UNTESTED")
        self.assertEqual(V[("T12(iii)", "A")].verdict, "PASS")      # (iii)-(vi) still grade
        self.assertEqual(V[("T12", "all")].verdict, "UNTESTED")

    # (j) the sheet from a three-run trio: T12 section, standing sentence at line 3 exactly once
    def test_j_sheet(self):
        specs = []
        for lab, tr, pol in (("A", TRADES_A, "BandOrVWAP"), ("B", TRADES_B, "OppBand"), ("C", TRADES_C, "Flat1559")):
            p = os.path.join(self.tmp, "w3-sheet-%s.json" % lab)
            tg.write_bridge(p, tr)
            specs.append(dict(P(pol), label=lab, path=p, format="bridge"))
        man = os.path.join(self.tmp, "w3-manifest.json")
        with open(man, "w") as fh:
            json.dump(specs, fh)
        out = os.path.join(self.tmp, "w3-sheet.md")
        rc = gr.main(["--runs", man, "--data", self.paths["TRIO"], "--out", out, "--session-start", "09:31"])
        with open(out) as fh:
            text = fh.read()
        lines = text.splitlines()
        self.assertEqual(rc, 0)
        self.assertEqual(lines[2], gr.STANDING_LIMITATION)
        self.assertEqual(gr._norm(text).count("fills are optimistic"), 1)
        self.assertIn("## T12", lines)
        self.assertIn("### T12 — PASS", lines)
        self.assertNotIn(gr.T12_MISSING, text)
        if os.environ.get("W3_SHEET_OUT"):
            with open(os.environ["W3_SHEET_OUT"], "w") as fh:
                fh.write(text)


if __name__ == "__main__":
    unittest.main()
