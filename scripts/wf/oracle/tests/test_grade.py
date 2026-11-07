"""Synthetic-fixture tests for scripts/wf/oracle/grade.py (T8-T11 graders, loader, sheet).

Fixture: 17 weekday sessions 2021-03-08 (s1) .. 2021-03-30 (s17); 2021-03-29 is s16 (as values-spec T11 :201).
Quiet session bars (every session unless overridden), all v 10:
  09:31 o 1000 h 1002 l 998 c 1000;  10:00, 10:30, 11:00, 15:30, 15:59, 16:00  o=h=l=c=1000
Hand arithmetic used throughout:
  * TR of every session s2..s15 = max(1002, prev close 1000) - min(998, 1000) = 4, so at s16 the ATR(14) sum is
    14 x 4 = 56 (ATR 4.0). At m = 1.5 the level distance is 1.5 x 56 / 14 = 6.0, i.e. the exact test
    14 x (fill - close) >= 84.
  * Band at s16, Lookback 10: history s6..s15, every close at a checkpoint minute = 1000 = open, so sigma = 0 and
    Upper = Lower = max/min(today open 1000, prev close 1000) = 1000. A checkpoint close > 1000 enters long,
    < 1000 short.
  * Fill rules (market.py defaults): market order = next bar open +/- 0.5 clipped to [l, h]; session close =
    close -/+ 0.5 clipped.
"""
import datetime as dt
import io
import json
import os
import shutil
import sys
import tempfile
import time
import unittest
from contextlib import redirect_stdout, redirect_stderr

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
if ORACLE not in sys.path:
    sys.path.insert(0, ORACLE)
import grade as gr     # noqa: E402
import market as mk    # noqa: E402

COLS = gr.tradelist.EXPECTED_NT8_COLUMNS


def weekdays(first, count):
    d, out = first, []
    while len(out) < count:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


DATES = weekdays(dt.date(2021, 3, 8), 17)
QUIET = [("0931", 1000, 1002, 998, 1000)] + [(t, 1000, 1000, 1000, 1000)
                                             for t in ("1000", "1030", "1100", "1530", "1559", "1600")]

# s16 day A: long XStop decided 10:04 (c = 10:04 by the tie 14 x 6 = 84), short XStop decided 10:33.
DAY_A = [("0931", 1000, 1002, 998, 1000),
         ("1000", 1000, 1003, 1000, 1003),     # checkpoint: 1003 > Upper 1000 -> EnterLong
         ("1001", 1003, 1004, 1002, 1003),     # long fill 1003 + 0.5 = 1003.5; level 997.5
         ("1002", 1003, 1003, 1001, 1001),     # 14 x 2.5 = 35 < 84
         ("1003", 1001, 1001, 999, 999),       # 14 x 4.5 = 63 < 84
         ("1004", 999, 999, 997.5, 997.5),     # 14 x 6 = 84 >= 84: crossing (tie)
         ("1005", 997, 997, 996, 996),         # XStop fill 997 - 0.5 = 996.5
         ("1006", 996, 996, 996, 996),
         ("1030", 996, 996, 990, 990),         # checkpoint: 990 < Lower 1000 -> EnterShort
         ("1031", 990, 990, 989, 989),         # short fill 990 - 0.5 = 989.5; level 995.5
         ("1032", 989, 993, 989, 993),         # 14 x 3.5 = 49 < 84
         ("1033", 993, 995.5, 993, 995.5),     # 14 x 6 = 84: crossing (tie)
         ("1034", 996, 997, 996, 997),         # XStop fill 996 + 0.5 = 996.5
         ("1035", 997, 997, 997, 997),
         ("1100", 1000, 1000, 1000, 1000), ("1530", 1000, 1000, 1000, 1000),
         ("1559", 1000, 1000, 1000, 1000), ("1600", 1000, 1000, 1000, 1000)]

# s16 day D: long entered 15:31, first crossing on the 16:00 bar (F under BandOrVWAP).
DAY_D = [("0931", 1000, 1002, 998, 1000), ("1000", 1000, 1000, 1000, 1000), ("1030", 1000, 1000, 1000, 1000),
         ("1100", 1000, 1000, 1000, 1000),
         ("1530", 1000, 1003, 1000, 1003),     # checkpoint 1003 > 1000 -> EnterLong
         ("1531", 1003, 1004, 1002, 1003),     # fill 1003.5, level 997.5
         ("1559", 1003, 1003, 1000, 1000),     # 14 x 3.5 = 49 < 84
         ("1600", 1000, 1000, 997, 997.5)]     # 84: crossing on F; session close fill 997.5 - 0.5 = 997.0

# s16 day G: long stopped at the 10:30 checkpoint, where 990 < Lower 1000 would EnterShort.
DAY_G = [("0931", 1000, 1002, 998, 1000), ("1000", 1000, 1003, 1000, 1003), ("1001", 1003, 1004, 1002, 1003),
         ("1002", 1003, 1003, 1001, 1001),
         ("1030", 1001, 1001, 990, 990),       # 14 x 13.5 = 189 >= 84: c = d = 10:30
         ("1031", 990, 990, 989, 989),         # XStop fill 989.5
         ("1100", 1000, 1000, 1000, 1000), ("1530", 1000, 1000, 1000, 1000),
         ("1559", 1000, 1000, 1000, 1000), ("1600", 1000, 1000, 1000, 1000)]

# T11 fixture: s13 10:00 closes 1001 (> Upper 1000 at Lookback 10: history s3..s12 all 1000, sigma 0);
# s13 also gets a 10:01 bar. s16 10:30 closes 1005 -> the first checkpoint with band + ATR + rule.
S13_T11 = [("0931", 1000, 1002, 998, 1000), ("1000", 1000, 1001, 1000, 1001), ("1001", 1001, 1001, 1000, 1000),
           ("1030", 1000, 1000, 1000, 1000), ("1100", 1000, 1000, 1000, 1000), ("1530", 1000, 1000, 1000, 1000),
           ("1559", 1000, 1000, 1000, 1000), ("1600", 1000, 1000, 1000, 1000)]
S16_T11 = [("0931", 1000, 1002, 998, 1000), ("1000", 1000, 1000, 1000, 1000),   # 1000 inside 999.9..1000.1
           ("1030", 1000, 1005, 1000, 1005), ("1031", 1005, 1006, 1004, 1005),   # fill 1005.5
           ("1100", 1000, 1000, 1000, 1000), ("1530", 1000, 1000, 1000, 1000),
           ("1559", 1000, 1000, 1000, 1000), ("1600", 1000, 1000, 1000, 1000)]


def write_data(path, overrides):
    out = []
    for n, day in enumerate(DATES, 1):
        for hhmm, o, h, l, c in overrides.get(n, QUIET):
            out.append("%s %s00;%r;%r;%r;%r;10\n" % (day.strftime("%Y%m%d"), hhmm, float(o), float(h),
                                                     float(l), float(c)))
    with open(path, "w") as fh:
        fh.writelines(out)


def T(n, hhmm):
    d = DATES[n - 1]
    return dt.datetime(d.year, d.month, d.day, int(hhmm[:2]), int(hhmm[2:]))


def write_bridge(path, trades):
    """trades: [(side, entry_dt, entry_price, exit_dt, exit_price, exit_name)]."""
    tl = []
    for side, en, ep, ex, xp, name in trades:
        pnl = (xp - ep if side == "Long" else ep - xp) * 20.0
        tl.append({"pnl": pnl, "marketPosition": side, "entryTime": en.strftime("%Y-%m-%dT%H:%M:%S.0000000"),
                   "exitTime": ex.strftime("%Y-%m-%dT%H:%M:%S.0000000"), "entryPrice": ep, "exitPrice": xp,
                   "exitName": name})
    doc = {"id": "t", "status": "ok", "strategy": "PraxisNoiseAreaBreakoutArmB",
           "metrics": {"totalTrades": len(tl), "netProfit": sum(t["pnl"] for t in tl)}, "trades": tl}
    with open(path, "w") as fh:
        json.dump(doc, fh)


def write_csv(path, trades):
    import csv
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for j, (side, en, ep, ex, xp, name) in enumerate(trades, 1):
            pnl = (xp - ep if side == "Long" else ep - xp) * 20.0
            row = {"Trade number": str(j), "Instrument": "NQ 09-25", "Account": "Backtest",
                   "Strategy": "PraxisNoiseAreaBreakoutArmB", "Market pos.": side, "Qty": "1",
                   "Entry price": repr(ep), "Exit price": repr(xp),
                   "Entry time": en.strftime("%m/%d/%Y %I:%M:%S %p"), "Exit time": ex.strftime("%m/%d/%Y %I:%M:%S %p"),
                   "Entry name": "L" if side == "Long" else "S", "Exit name": name,
                   "Profit": ("-$%.2f" % -pnl) if pnl < 0 else ("$%.2f" % pnl), "Cum. net profit": "$0.00",
                   "Commission": "$0.00", "MAE": "$0.00", "MFE": "$0.00", "ETD": "$0.00", "Bars": "1"}
            w.writerow([row[c] for c in COLS])


A_LONG = ("Long", T(16, "1001"), 1003.5, T(16, "1005"), 996.5, "XStop")
A_SHORT = ("Short", T(16, "1031"), 989.5, T(16, "1034"), 996.5, "XStop")
P10 = {"Lookback": 10, "NoiseMult": 1.0, "StopAtrMult": 1.5, "ExitPolicy": "BandOrVWAP"}


class GradeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="w2-grade-")
        cls.data = {}
        for key, ov in (("A", {16: DAY_A}), ("D", {16: DAY_D}), ("G", {16: DAY_G}), ("H", {13: S13_T11, 16: S16_T11})):
            p = os.path.join(cls.tmp, "w2-data-%s.txt" % key)
            write_data(p, ov)
            cls.data[key] = (p, mk.load_market(p, session_start="09:31"))
        cls.k = 0

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def run_grade(self, key, runs):
        """runs: [(trades, params, fmt)] -> (ctx, {(test, run): Verdict})."""
        specs = []
        for j, (trades, params, fmt) in enumerate(runs):
            GradeTests.k += 1
            p = os.path.join(self.tmp, "w2-trades-%d.%s" % (self.k, "json" if fmt == "bridge" else "csv"))
            (write_bridge if fmt == "bridge" else write_csv)(p, trades)
            specs.append(dict(params, label="R%d" % (j + 1), path=p, format=fmt))
        ctx = gr.build_ctx(self.data[key][1], specs)
        vs, _t12, _e = gr.run_graders(ctx)
        return ctx, {(v.test, v.run): v for v in vs}, vs

    # ---- session start: these fixtures have no bar stamped before 09:31 -> identical at either start ----
    def test_fixtures_identical_at_either_start(self):
        for key, (p, m31) in sorted(self.data.items()):
            m08 = mk.load_market(p, session_start="08:31")
            self.assertEqual((m08.pre_open_bars, m08.pre_open_only_dropped), (0, []), key)
            bars = lambda m: [(s.n, s.date, [(b.dt, b.o, b.h, b.l, b.c, b.v) for b in s.bars]) for s in m.sessions]  # noqa: E731
            self.assertEqual(bars(m08), bars(m31), key)
        ctx31 = gr.build_ctx(self.data["A"][1], [dict(P10, label="R", path=self._bridge([A_LONG, A_SHORT]), format="bridge")])
        ctx08 = gr.build_ctx(mk.load_market(self.data["A"][0], session_start="08:31"),
                             [dict(P10, label="R", path=self._bridge([A_LONG, A_SHORT]), format="bridge")])
        vv = lambda ctx: [(v.test, v.run, v.verdict, v.reason, v.rows, v.lines) for v in gr.run_graders(ctx)[0]]  # noqa: E731
        self.assertEqual(vv(ctx08), vv(ctx31))

    def _bridge(self, trades):
        GradeTests.k += 1
        p = os.path.join(self.tmp, "w2-trades-%d.json" % self.k)
        write_bridge(p, trades)
        return p

    # ---- calendar / arithmetic preconditions (hand values) ----
    def test_fixture_atr_and_band(self):
        m = self.data["A"][1]
        self.assertEqual(m.N, 17)
        self.assertEqual(m.sessions[15].date, "2021-03-29")
        self.assertEqual(gr._atr.atr_at(m, 16), (True, 56.0, 4.0))
        self.assertFalse(gr._atr.atr_at(m, 15)[0])
        st = gr._band.band_at(m, 16, "10:00", 10, 1.0)
        self.assertTrue(st.have_band)
        self.assertEqual((st.upper, st.lower), (1000.0, 1000.0))

    # ---- T8 ----
    def test_t8_correct_xstops_pass_both_formats(self):
        for fmt in ("bridge", "nt8csv"):
            ctx, V, _ = self.run_grade("A", [([A_LONG, A_SHORT], P10, fmt)])
            a0, a1 = ctx.runs[0].anns
            self.assertEqual(a0.c_pos, ctx.market.index[T(16, "1004")])
            self.assertEqual(a0.d_pos, a0.c_pos)
            self.assertEqual(a1.c_pos, ctx.market.index[T(16, "1033")])
            self.assertEqual(V[("FILLFIT", "R1")].verdict, "PASS", fmt)
            self.assertEqual(V[("T8(i-iv)", "R1")].verdict, "PASS", V[("T8(i-iv)", "R1")].lines)
            self.assertEqual(V[("T8 power (b)", "all")].verdict, "PASS", V[("T8 power (b)", "all")].lines)
            self.assertEqual(V[("T8 m=1.5", "all")].verdict, "PASS")
            self.assertEqual(V[("T8 m=2.25", "all")].verdict, "UNTESTED")   # no run at that m
            if fmt == "nt8csv":
                self.assertEqual(ctx.runs[0].run.trades[0].entry_name, "L")

    def test_t8_wrong_stop_predictions_by_hand(self):
        ctx, _V, _ = self.run_grade("A", [([A_LONG, A_SHORT], P10, "bridge")])
        r, a = ctx.runs[0], ctx.runs[0].anns[0]
        wp = gr._wrong_predictions(ctx, r, a)
        idx = ctx.market.index
        # (1) 14 one-minute TRs ending at s16 10:00: 10:00 -> 3, 09:31 -> 4, s15 bars 0 x4 and 09:31 4,
        #     s14 bars 0 x5 and 09:31 4: sum 15; distance 1.5 x 15/14 = 1.607; 1003.5 - 1001 = 2.5 >= it at 10:02.
        self.assertEqual(wp["atr14min"], idx[T(16, "1002")])
        # (2) sigma 0 -> half-width 0 -> level = fill 1003.5; 10:01 close 1003 crosses.
        self.assertEqual(wp["band_halfwidth"], idx[T(16, "1001")])
        # (3) k = 1.0: distance 4; 1003.5 - 999 = 4.5 at 10:03.
        self.assertEqual(wp["k_for_m"], idx[T(16, "1003")])
        # (4) no checkpoint between 10:01 and 10:04.
        self.assertIsNone(wp["checkpoint_only"])

    def test_t8_late_xstop_fails_naming_row(self):
        late = ("Long", T(16, "1001"), 1003.5, T(16, "1006"), 996.0, "XStop")   # 10:06 fill: 996-0.5 clipped to 996
        _ctx, V, _ = self.run_grade("A", [([late, A_SHORT], P10, "bridge")])
        v = V[("T8(i-iv)", "R1")]
        self.assertEqual(V[("FILLFIT", "R1")].verdict, "PASS")
        self.assertEqual(v.verdict, "FAIL")
        self.assertEqual(v.rows, [1])
        self.assertTrue(any("(iii) row 1" in x for x in v.lines), v.lines)
        self.assertTrue(any("(i) row 1" in x for x in v.lines), v.lines)
        self.assertEqual(V[("T8 m=1.5", "all")].verdict, "FAIL")

    def test_t8_bad_exit_price_not_pass(self):
        bad = ("Long", T(16, "1001"), 1003.5, T(16, "1005"), 997.0, "XStop")    # rule says 996.5
        _ctx, V, _ = self.run_grade("A", [([bad, A_SHORT], P10, "bridge")])
        self.assertEqual(V[("FILLFIT", "R1")].verdict, "UNTESTED")
        self.assertEqual(V[("FILLFIT", "R1")].rows, [1])
        self.assertIn("fill rules do not fit", V[("T8(i-iv)", "R1")].reason)
        self.assertNotEqual(V[("T8 m=1.5", "all")].verdict, "PASS")

    def test_t8_power_a_one_side_only(self):
        _ctx, V, _ = self.run_grade("A", [([A_LONG], P10, "bridge")])
        self.assertEqual(V[("T8(i-iv)", "R1")].verdict, "PASS")
        self.assertEqual(V[("T8 m=1.5", "all")].verdict, "UNTESTED")
        self.assertIn("power check (a)", V[("T8 m=1.5", "all")].reason)

    # ---- T9 ----
    def test_t9_crossing_on_F_session_close_pass(self):
        tr = ("Long", T(16, "1531"), 1003.5, T(16, "1600"), 997.0, gr.SESSION_CLOSE)
        ctx, V, _ = self.run_grade("D", [([tr], P10, "bridge")])
        a = ctx.runs[0].anns[0]
        self.assertEqual(a.c_pos, ctx.market.index[T(16, "1600")])
        self.assertTrue(a.c_flat)
        self.assertEqual(V[("FILLFIT", "R1")].verdict, "PASS")
        self.assertEqual(V[("T9", "R1")].verdict, "PASS")
        self.assertEqual(V[("T9", "R1")].rows, [1])
        self.assertEqual(V[("T8(i-iv)", "R1")].verdict, "PASS")   # c = d on F, exited by the session flat; 0 = 0

    def test_t9_xstop_decided_on_F_fails(self):
        tr = ("Long", T(16, "1531"), 1003.5, T(17, "0931"), 999.5, "XStop")    # d = prev bar = s16 16:00 = F
        _ctx, V, _ = self.run_grade("D", [([tr], P10, "bridge")])
        self.assertEqual(V[("T9", "R1")].verdict, "FAIL")
        self.assertEqual(V[("T9", "R1")].rows, [1])
        self.assertEqual(V[("T8(i-iv)", "R1")].verdict, "FAIL")

    # ---- T10 ----
    def test_t10_entry_on_xstop_fill_bar_fails(self):
        rev = ("Short", T(16, "1005"), 996.5, T(16, "1600"), 1000.0, gr.SESSION_CLOSE)
        _ctx, V, _ = self.run_grade("A", [([A_LONG, rev], P10, "bridge")])
        self.assertEqual(V[("T10", "R1")].verdict, "FAIL")
        self.assertEqual(V[("T10", "R1")].rows, [1, 2])

    def test_t10_stop_at_entering_checkpoint_pass(self):
        tr = ("Long", T(16, "1001"), 1003.5, T(16, "1031"), 989.5, "XStop")
        _ctx, V, _ = self.run_grade("G", [([tr], P10, "bridge")])
        self.assertEqual(V[("T8(i-iv)", "R1")].verdict, "PASS")
        self.assertEqual(V[("T10", "R1")].verdict, "PASS")
        self.assertEqual(V[("T10", "R1")].rows, [1])

    # ---- T11 ----
    def test_t11_entry_in_s13_fails(self):
        tr = ("Long", T(13, "1001"), 1001.0, T(13, "1600"), 1000.0, gr.SESSION_CLOSE)  # 1001+0.5 clipped to h 1001
        _ctx, V, _ = self.run_grade("H", [([tr], P10, "bridge")])
        self.assertEqual(V[("T11(i)", "R1")].verdict, "FAIL")
        self.assertEqual(V[("T11(i)", "R1")].rows, [1])
        self.assertEqual(V[("T11(ii)", "R1")].verdict, "FAIL")

    def test_t11_first_entry_at_oracle_checkpoint_pass(self):
        tr = ("Long", T(16, "1031"), 1005.5, T(16, "1600"), 1000.0, gr.SESSION_CLOSE)  # 999.5 clipped to l 1000
        ctx, V, _ = self.run_grade("H", [([tr], P10, "bridge")])
        self.assertEqual(V[("T11(i)", "R1")].verdict, "PASS", V[("T11(i)", "R1")].lines)
        self.assertIn("s13 2021-03-24 10:00", V[("T11(i)", "R1")].reason)
        self.assertEqual(V[("T11(ii)", "R1")].verdict, "PASS", V[("T11(ii)", "R1")].lines)
        # Lookback 14: no band before s16 -> (i) UNTESTED
        _ctx, V, _ = self.run_grade("H", [([tr], dict(P10, Lookback=14), "bridge")])
        self.assertEqual(V[("T11(i)", "R1")].verdict, "UNTESTED")

    # ---- parameters ----
    def test_refusals(self):
        for ep in ("0", "1", "2", 0, 2, None, "Flat"):
            with self.assertRaises(gr.GradeInputError) as cm:
                gr.check_params(dict(P10, ExitPolicy=ep))
            self.assertIn("§9(d)", str(cm.exception))
        for m in (0, 0.0, "0", 1.0, 2.0):
            with self.assertRaises(gr.GradeInputError) as cm:
                gr.check_params(dict(P10, StopAtrMult=m))
            self.assertIn("stop-on", str(cm.exception))
        with self.assertRaises(gr.GradeInputError):
            gr.check_params(dict(P10, Lookback=12))
        with self.assertRaises(gr.GradeInputError):
            gr.check_params(dict(P10, NoiseMult=0.9))
        self.assertEqual(gr.check_params({"Lookback": "10", "NoiseMult": "1.0", "StopAtrMult": "2.25",
                                          "ExitPolicy": "Flat1559"})["StopAtrMult"], 2.25)

    def test_cli_numeric_policy_exit2(self):
        err = io.StringIO()
        with redirect_stderr(err):
            rc = gr.main(["--trades", "/nonexistent", "--format", "bridge", "--lookback", "10", "--noise-mult", "1.0",
                          "--stop-atr-mult", "1.5", "--exit-policy", "1", "--data", self.data["A"][0],
                          "--session-start", "09:31"])
        self.assertEqual(rc, 2)
        self.assertIn("§9(d)", err.getvalue())

    def test_off_bar_time_fails_loudly(self):
        tr = ("Long", T(16, "1007"), 1000.0, T(16, "1600"), 1000.0, gr.SESSION_CLOSE)   # no 10:07 bar
        with self.assertRaises(gr.GradeInputError) as cm:
            self.run_grade("A", [([tr], P10, "bridge")])
        self.assertIn("row 1", str(cm.exception))

    # ---- sheet via the CLI ----
    def test_sheet_line3_once_and_exit_codes(self):
        man = os.path.join(self.tmp, "w2-manifest.json")
        tb = os.path.join(self.tmp, "w2-sheet-a.json")
        tc = os.path.join(self.tmp, "w2-sheet-a.csv")
        write_bridge(tb, [A_LONG, A_SHORT])
        write_csv(tc, [A_LONG, A_SHORT])
        with open(man, "w") as fh:
            json.dump([dict(P10, label="A-bridge", path=tb, format="bridge"),
                       dict(P10, label="A-csv", path=tc, format="nt8csv")], fh)
        out = os.path.join(self.tmp, "w2-sheet.md")
        rc = gr.main(["--runs", man, "--data", self.data["A"][0], "--out", out, "--session-start", "09:31"])
        with open(out) as fh:
            text = fh.read()
        lines = text.splitlines()
        self.assertEqual(rc, 0)
        self.assertEqual(lines[0], "# Oracle grade sheet — A-bridge, A-csv")
        self.assertEqual(lines[1], "")
        self.assertEqual(lines[2], gr.STANDING_LIMITATION)
        self.assertEqual(gr._norm(text).count("fills are optimistic"), 1)
        self.assertIn("UNVERIFIED against NT8", lines[3])
        if os.path.isfile(os.path.join(ORACLE, "policy.py")):   # W3: policy.py present -> a T12 section
            self.assertNotIn(gr.T12_MISSING, text)
            self.assertIn("## T12", text.splitlines())
        else:
            self.assertIn(gr.T12_MISSING, text)
        self.assertIn(self.data["A"][1].source["sha256"], text)
        late = os.path.join(self.tmp, "w2-sheet-late.json")
        write_bridge(late, [("Long", T(16, "1001"), 1003.5, T(16, "1006"), 996.0, "XStop")])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = gr.main(["--trades", late, "--format", "bridge", "--lookback", "10", "--noise-mult", "1.0",
                          "--stop-atr-mult", "1.5", "--exit-policy", "BandOrVWAP", "--data", self.data["A"][0],
                          "--session-start", "09:31"])
        self.assertEqual(rc, 1)
        self.assertIn("### T8(i-iv) [run1] — FAIL", buf.getvalue())

    def test_render_refuses_second_standing_phrase(self):
        ctx, _V, vs = self.run_grade("A", [([A_LONG], P10, "bridge")])
        vs = vs + [gr.Verdict("T9", "PASS", "Fills  are\u200b OPTIMISTIC here", run="R1")]
        with self.assertRaises(gr.GradeInputError):
            gr.render(ctx, vs, None, None)


if __name__ == "__main__":
    unittest.main()
