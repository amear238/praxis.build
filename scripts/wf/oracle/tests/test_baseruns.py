"""Base-run cross-check (finding B1, unit 2026-11-07-wf-oracles, W6). The three committed NT8 Strategy Analyzer
trade lists of the BASE strategies (2026-11-01; their band / VWAP / checkpoint code matches arm (b)'s) are graded
with the oracle's per-run functions: grade.py fill-rule fit, policy.py T12 (iii)/(iv)/(v), Lookback 14, k 1.0.
They are m = 0 (stop-less) runs: grade.annotate_trade is called with StopAtrMult = NO_STOP (a stand-in for "no
stop": 14*(fill-close) >= 1e9*atrSum never holds; asserted: no crossing on any trade).

Asserted: at session start "08:31" every check PASSes on every trade of all three runs with 0 ties; at "09:31"
T12(v) FAILs on the baseline -- this documents the divergence (it is expected; which reading arm (b) on the VM
follows is escalated, not decided here). The CSVs are read-only inputs (never moved or edited); absent -> skip.
Not gated: the whole oracle suite with this file stays well under 90 s (W6 report: ~15 s for this file).
"""
import csv
import datetime as dt
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
if ORACLE not in sys.path:
    sys.path.insert(0, ORACLE)
import market as mk   # noqa: E402
import grade as gr    # noqa: E402
import policy as pl   # noqa: E402

DATA = os.environ.get("PRAXIS_ORACLE_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
DESK = "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 %s.csv"
RUNS = (("baseline", "BandOrVWAP", DESK % "07-10 AM", 1190),   # BandOrVWAP base strategy
        ("OppBand", "OppBand", DESK % "07-57 AM", 810),         # _OppBand.cs (opposite-band rule)
        ("Flat1559", "Flat1559", DESK % "07-59 AM", 1190))
NO_STOP = 1e9
HAVE = os.path.exists(DATA) and all(os.path.exists(p) for _l, _p, p, _n in RUNS)


def _t(s):
    return dt.datetime.strptime(s, "%Y-%m-%d %I:%M:%S %p")      # e.g. "2021-03-29 10:01:00 AM"


def load_csv(path):
    """Adapter: NT8 grid CSV (24 columns, the last one empty) -> [market.Trade]. Read-only."""
    with open(path, "r", newline="") as fh:
        rows = list(csv.reader(fh))
    head = rows[0]
    if len(head) != 24 or head[-1] != "":
        raise AssertionError("%s: expected 24 columns with a trailing empty one, got %d" % (path, len(head)))
    ix = {name: j for j, name in enumerate(head)}
    out = []
    for j, r in enumerate(rows[1:], 1):
        if len(r) != 24:
            raise AssertionError("%s row %d: %d columns" % (path, j, len(r)))
        out.append(mk.Trade(_t(r[ix["Entry time"]]), _t(r[ix["Exit time"]]), r[ix["Market pos."]],
                            float(r[ix["Entry price"]]), float(r[ix["Exit price"]]), r[ix["Entry name"]],
                            r[ix["Exit name"]], j))
    return out


def grade_base(market, label, policy, trades):
    """-> (n stop crossings, fill-fit Verdict, (iii, iv, v) Verdicts, ties)."""
    params = {"Lookback": 14, "NoiseMult": 1.0, "StopAtrMult": NO_STOP, "ExitPolicy": policy}
    anns = [gr.annotate_trade(market, t, params) for t in trades]
    r = gr.GradedRun(label, mk.Run(params, trades, {"label": label}), anns, "nt8csv", "-", "-")
    ctx = gr.Ctx(market, [r])
    (ff,) = gr.grade_fillfit(ctx)
    ties = []
    vs = tuple(fn(ctx, r, ties) for fn in (pl.grade_iii, pl.grade_iv, pl.grade_v))
    return sum(1 for a in anns if a.c_pos is not None), ff, vs, ties


@unittest.skipUnless(HAVE, "data file or one of the three 2026-11-01 base-run CSVs absent")
class BaseRunCrossCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trades = {label: load_csv(path) for label, _p, path, _n in RUNS}

    def test_0831_every_trade_passes(self):
        m = mk.load_market(DATA, session_start="08:31")
        for label, policy, _path, n in RUNS:
            trades = self.trades[label]
            self.assertEqual(len(trades), n, label)
            nstop, ff, (iii, iv, v), ties = grade_base(m, label, policy, trades)
            self.assertEqual(nstop, 0, label)
            self.assertEqual((ff.verdict, ff.reason), ("PASS", "every entry and exit price equals the default fill "
                                                       "rule (%d trades)" % n), (label, ff.lines[:5]))
            for vd in (iii, iv, v):
                self.assertEqual(vd.verdict, "PASS", (label, vd.test, vd.reason, vd.lines[:5]))
            self.assertEqual(len(iii.rows), n, label)    # every trade graded by (iii)
            self.assertEqual(len(v.rows), n, label)      # every entry graded by (v)
            self.assertEqual(ties, [], label)

    def test_0931_baseline_v_fails(self):
        m = mk.load_market(DATA, session_start="09:31")
        label, policy, _path, n = RUNS[0]
        nstop, ff, (_iii, _iv, v), _ties = grade_base(m, label, policy, self.trades[label])
        self.assertEqual(nstop, 0)
        self.assertEqual(ff.verdict, "PASS")            # fill rules fit at either start
        self.assertEqual(v.verdict, "FAIL")             # documents the divergence (expected)
        sys.stderr.write("\n[baseruns] 09:31 baseline T12(v): %s, %d of %d entries\n" % (v.reason, len(v.rows), n))
        self.assertEqual(len(v.rows), 326)


if __name__ == "__main__":
    unittest.main()
