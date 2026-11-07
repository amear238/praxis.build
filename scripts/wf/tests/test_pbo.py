"""Tests for scripts/wf/pbo.py (values-spec §7 :102-108), analytic answers.

subprocess first (see test_select.py); modules loaded by path, never via sys.path.
"""
import subprocess  # noqa: F401  (must stay first: caches the stdlib `select`)
import importlib.util
import itertools
import json
import math
import os
import random
import sys
import tempfile
import time
import unittest

WF = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def load(name, fname, here=WF):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, os.path.join(here, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sel = load("praxis_wf_select", "select.py")
pbo = load("praxis_wf_pbo", "pbo.py")
ts = load("praxis_wf_test_select", "test_select.py", os.path.join(WF, "tests"))

S, BLOCK = 16, 82
ROWS = S * BLOCK          # 1312 = 16 x 82 (values-spec §7 :103)
COLS = sel.GRID_COLUMNS
KEYS = [sel.tie_key(p) for p in sel.GRID]
ALT = [1.0 if r % 2 else -1.0 for r in range(ROWS)]   # each 82-row block: mean exactly 0
ONES = [1] * ROWS          # one trade a day: 656 per training set >= 261


def full(values, trades=None, collect=True):
    return pbo.cscv(COLS, KEYS, values, trades or [ONES] * 81, S, BLOCK, collect=collect)


def direct(columns, keys, values, trades, s_blocks, block):
    """Slow reference: per split, concatenate the rows and compute everything afresh;
    average ranks by sorting (a different algorithm from pbo.cscv's less/equal count)."""
    m = len(columns)
    blocks = range(s_blocks)
    rows_of = lambda bs, arr: [arr[b * block + i] for b in bs for i in range(block)]
    detail, le0, ne = [], 0, 0
    for combo in itertools.combinations(blocks, s_blocks // 2):
        test_b = [b for b in blocks if b not in combo]
        n_tr = len(combo) * block
        items = []
        for j in range(m):
            s = sel.sharpe(rows_of(combo, values[j]))
            if sel.eligible(s, sum(rows_of(combo, trades[j])), n_tr):
                items.append((j, s, keys[j]))
        nstar, _ = sel.choose(items)
        if nstar is None:
            le0 += 1
            ne += 1
            detail.append((combo, None, None, None))
            continue
        t = [sel.sharpe(rows_of(test_b, values[j])) for j in range(m)]
        order = sorted(range(m), key=lambda j: t[j])
        ranks = [0.0] * m
        i = 0
        while i < m:
            k = i
            while k + 1 < m and t[order[k + 1]] == t[order[i]]:
                k += 1
            for q in range(i, k + 1):
                ranks[order[q]] = (i + 1 + k + 1) / 2.0
            i = k + 1
        om = ranks[nstar] / (m + 1)
        lam = math.log(om / (1 - om))
        le0 += lam <= 0
        detail.append((combo, columns[nstar], ranks[nstar], lam))
    return {"le0": le0, "no_eligible_splits": ne, "pbo": le0 / len(detail), "detail": detail}


class TestPboAnalytic(unittest.TestCase):
    def test_identical_columns_pbo_one(self):
        # 81 identical columns: on every split all train S are equal -> tie-break -> n* =
        # L14_k1.0_m1.5_BandOrVWAP (distance 0, m 1.5 first); all test S equal -> every rank
        # is the average (1+81)/2 = 41; omega = 41/82 = 0.5; lambda = ln(1) = 0.
        # Under the spec's "PBO = share of splits with λ ≤ 0" (§7 :106) lambda = 0 COUNTS,
        # so PBO = 1.0 exactly.
        rng = random.Random(1)
        v = [round(rng.uniform(-300, 300), 2) for _ in range(ROWS)]
        r = full([v] * 81)
        self.assertEqual((r["splits"], r["le0"], r["no_eligible_splits"], r["pbo"]), (12870, 12870, 0, 1.0))
        self.assertTrue(all(d[1] == "L14_k1.0_m1.5_BandOrVWAP" and d[2] == 41.0 and d[3] == 0.0
                            for d in r["detail"]))

    def test_dominant_column_pbo_zero(self):
        # one column = 5 +- 1 (positive mean on every block); the other 80 = +-1 with block
        # mean exactly 0 -> S = 0 on every set. Dominant is the unique best on every train
        # and every test: rank 81, omega 81/82, lambda = ln(81) > 0 -> PBO 0.0.
        dom = COLS.index("L18_k0.8_m3_Flat1559")  # far from the anchor on purpose
        vals = [[5.0 + a for a in ALT] if j == dom else ALT for j in range(81)]
        r = full(vals)
        self.assertEqual((r["le0"], r["no_eligible_splits"], r["pbo"]), (0, 0, 0.0))
        self.assertTrue(all(d[1] == COLS[dom] and d[2] == 81.0 for d in r["detail"]))
        self.assertAlmostEqual(r["detail"][0][3], math.log(81), delta=1e-12)

    def test_train_best_is_test_worst_pbo_one(self):
        # The brief's literal construction ("best on train and worst on test in every split")
        # is impossible under CSCV: each split's test set is another split's training set.
        # Equivalent analytic construction: column j has block mean +c on 8 blocks and -c on
        # the other 8 (a distinct 8-subset per column), +-a alternating inside each block.
        # Then every column's total is 0, so test mean = -(train mean), and sum of squares
        # is the same on every 8-block set, so test S = -(train S) exactly. The train-best
        # n* is therefore in the LOWEST test group: rank <= 41, lambda <= 0 -> PBO 1.0.
        c, a = 1.0, 3.0
        subsets = random.Random(7).sample(list(itertools.combinations(range(S), 8)), 81)
        vals = []
        for pos in subsets:
            vals.append([(c if (r // BLOCK) in pos else -c) + a * ALT[r] for r in range(ROWS)])
        r = full(vals)
        self.assertEqual((r["le0"], r["no_eligible_splits"], r["pbo"]), (12870, 0, 1.0))
        self.assertTrue(all(d[2] <= 41.0 and d[3] <= 0 for d in r["detail"]))

    def test_all_ineligible_pbo_one(self):
        # one trade every 4th session: 21 per 82-row block, 168 per training set < 261
        # (100 * 656 / 252 = 260.3, §7 :105) -> no eligible n* in any split ->
        # each counts as lambda <= 0 (§7 :107) -> PBO 1.0, no_eligible_splits 12870.
        rng = random.Random(2)
        vals = [[round(rng.uniform(-50, 50), 2) for _ in range(ROWS)] for _ in range(81)]
        sparse = [1 if r % 4 == 0 else 0 for r in range(ROWS)]
        self.assertEqual(sum(sparse[:BLOCK]), 21)
        r = full(vals, [sparse] * 81, collect=False)
        self.assertEqual((r["le0"], r["no_eligible_splits"], r["pbo"], r["logits"]), (12870, 12870, 1.0, []))

    def test_undefined_test_sharpe_not_settled(self):
        rng = random.Random(4)
        vals = [[round(rng.uniform(-50, 50), 2) for _ in range(ROWS)] for _ in range(81)]
        vals[40] = [0.0] * ROWS  # sd = 0 on every test set
        with self.assertRaises(sel.NotSettledBySpec) as cm:
            full(vals, collect=False)
        self.assertIn("NotSettledBySpec", str(cm.exception))
        self.assertIn("TEST-set Sharpe is undefined", str(cm.exception))
        self.assertIs(pbo.NotSettledBySpec, sel.NotSettledBySpec)


class TestFastEqualsDirect(unittest.TestCase):
    def test_seeded_small_cases(self):
        for seed in range(12):
            rng = random.Random(1000 + seed)
            s_blocks, block = (4, 5) if seed % 2 == 0 else (6, 4)
            m = 7
            idx = sorted(rng.sample(range(81), m))
            cols = [COLS[i] for i in idx]
            keys = [KEYS[i] for i in idx]
            rows = s_blocks * block
            vals = [[round(rng.uniform(-100, 100), 2) for _ in range(rows)] for _ in range(m)]
            vals[3] = list(vals[1])                     # exact ties on train and test
            vals[5] = [2.0 * v for v in vals[2]]        # same Sharpe (scale-invariant), exact
            trs = [[rng.choice([0, 1, 1]) for _ in range(rows)] for _ in range(m)]
            fast = pbo.cscv(cols, keys, vals, trs, s_blocks, block, collect=True)
            slow = direct(cols, keys, vals, trs, s_blocks, block)
            self.assertEqual(fast["detail"], slow["detail"], "seed %d" % seed)
            self.assertEqual((fast["le0"], fast["no_eligible_splits"], fast["pbo"]),
                             (slow["le0"], slow["no_eligible_splits"], slow["pbo"]))
            self.assertEqual(fast["splits"], math.comb(s_blocks, s_blocks // 2))


class TestPboCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        t = cls.tmp.name
        cls.cal = ts.make_calendar()
        cls.cal_path = ts.write_json(os.path.join(t, "cal.json"), cls.cal)
        n = cls.cal["N"]
        dom = "L18_k0.8_m3_Flat1559"
        cls.dir = os.path.join(t, "b")
        os.mkdir(cls.dir)
        alt = [1.0 if i % 2 else -1.0 for i in range(n)]
        for col, prm in zip(COLS, sel.GRID):
            v = [5.0 + x for x in alt] if col == dom else list(alt)
            ts.write_json(os.path.join(cls.dir, col + ".json"), ts.make_daily(col, prm, v, [1] * n))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_cli_dominant(self):
        out = os.path.join(self.tmp.name, "pbo.json")
        t0 = time.monotonic()
        r = ts.run_cli("pbo.py", "--calendar", self.cal_path, "--daily", self.dir, "--out", out)
        el = time.monotonic() - t0
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("elapsed", r.stderr)
        self.assertLess(el, 60.0)
        o = ts.read_json(out)
        for k, v in {"schema": "praxis-wf-pbo/1", "S": 16, "block": 82, "rows": [12, 1323],
                     "splits": 12870, "le0": 0, "no_eligible_splits": 0, "pbo": 0.0,
                     "threshold": 0.05, "passes": True}.items():
            self.assertEqual(o[k], v, k)
        self.assertNotIn("elapsed", json.dumps(o))

    def test_cli_bad_cscv_rows(self):
        cal = json.loads(json.dumps(self.cal))
        cal["cscv_rows"] = [1, 1312]
        p = ts.write_json(os.path.join(self.tmp.name, "badcal.json"), cal)
        r = ts.run_cli("pbo.py", "--calendar", p, "--daily", self.dir, "--out", os.path.join(self.tmp.name, "x.json"))
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn("cscv_rows", r.stderr)


    # W6 fix round: defects 1-3 reach pbo.py through sel.load_calendar / sel.load_dailies.
    def _pbo_refused(self, cal=None, mutate=None, needle=""):
        import shutil
        t = tempfile.mkdtemp(dir=self.tmp.name)
        cp = self.cal_path if cal is None else ts.write_json(os.path.join(t, "cal.json"), cal)
        dd = os.path.join(t, "b")
        shutil.copytree(self.dir, dd)
        if mutate is not None:
            fp = os.path.join(dd, COLS[0] + ".json")
            d = ts.read_json(fp)
            mutate(d)
            ts.write_json(fp, d)
        r = ts.run_cli("pbo.py", "--calendar", cp, "--daily", dd, "--out", os.path.join(t, "o.json"))
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn(needle, r.stderr)

    def test_cli_missing_pnl_basis_in(self):
        self._pbo_refused(mutate=lambda d: d.pop("pnl_basis_in"), needle="'pnl_basis_in'")

    def test_cli_n_trades_mismatch(self):
        self._pbo_refused(mutate=lambda d: d.__setitem__("n_trades", d["n_trades"] + 1),
                          needle="n_trades=1353 != len(trades)=1352")

    def test_cli_n_trades_5000(self):
        self._pbo_refused(mutate=lambda d: d.__setitem__("n_trades", 5000), needle="§7 :112")

    def test_cli_short_k(self):
        cal = json.loads(json.dumps(self.cal))
        cal["windows"] = cal["windows"][:16]
        cal["K"] = 16
        self._pbo_refused(cal=cal, needle="K=16 but N=1352 implies K=17")


if __name__ == "__main__":
    unittest.main()
