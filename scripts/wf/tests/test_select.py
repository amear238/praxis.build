"""Tests for scripts/wf/select.py (values-spec §6 :92-98, §5, §2 :43, §7 :112).

`subprocess` is imported FIRST, before anything else can touch sys.path, so the
stdlib `select` is cached in sys.modules; select.py itself is loaded by path
under the name praxis_wf_select (select.py shadows the stdlib `select`).
"""
import subprocess  # noqa: F401  (must stay first: caches the stdlib `select`)
import importlib.util
import json
import math
import os
import random
import statistics
import sys
import tempfile
import unittest
from fractions import Fraction

WF = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SELECT_PY = os.path.join(WF, "select.py")


def load(name, fname):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, os.path.join(WF, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sel = load("praxis_wf_select", "select.py")


# ---------------------------------------------------------------- synthetic I/O
def make_calendar(n=1352):
    """Interface-1-shaped calendar; windows by values-spec §5 :87."""
    k_full = (n - 252) // 63
    wins = []
    for k in range(1, k_full + 1):
        a = 63 * (k - 1) + 1
        wins.append({"k": k, "is": [a, a + 251], "oos": [a + 252, a + 314],
                     "is_dates": ["x", "y"], "oos_dates": ["x", "y"], "is_holes": 0,
                     "oos_holes": 0, "is_early_close": 0, "oos_early_close": 0})
    last = 252 + 63 * k_full
    return {"schema": "praxis-wf-calendar/1", "source": {"path": "synthetic", "bytes": 0, "sha256": "0"},
            "rule": {"rth_first": "09:31:00", "rth_last": "16:00:00", "weekdays": "Mon-Fri",
                     "range": ["2021-03-08", "2026-07-17"], "IS": 252, "OOS": 63, "STEP": 63},
            "N": n, "sessions": [{"n": i, "date": "d%d" % i, "first_bar": "09:31", "last_bar": "16:00",
                                  "early_close_in_file": False, "nt8_last_bar": "16:00",
                                  "nt8_last_bar_grade": "synthetic"} for i in range(1, n + 1)],
            "windows": wins, "K": k_full, "oos_sessions": 63 * k_full,
            "dropped": [last + 1, n], "dropped_dates": [], "cscv_rows": [12, 1323],
            "cscv_S": 16, "cscv_block": 82, "weekend_dates_dropped": 0}


def make_daily(column, params, net, ntr, truncated=False):
    """Interface-2-shaped daily file; each trading session gets ntr[i] trades
    whose net_pnl sums to net[i] (first trade carries it, the rest 0)."""
    trades = []
    for i, (v, c) in enumerate(zip(net, ntr), 1):
        if c == 0 and v != 0:
            raise ValueError("synthetic: P&L on a no-trade day")
        for t in range(c):
            pv = v if t == 0 else 0.0
            trades.append({"session": i, "entry_time": "e%d" % i, "exit_time": "x%d" % i,
                           "side": "Long", "net_pnl": pv, "gross_pnl": pv + 4.68, "exit_name": "s"})
    return {"schema": "praxis-wf-daily/1", "column": column, "params": params,
            "pnl_basis_in": "net", "commission_rt_usd": 4.68, "contracts": 1,
            "truncated": truncated, "n_trades": len(trades), "N": len(net),
            "daily_net": [float(v) for v in net], "daily_trades": list(ntr), "trades": trades,
            "cross_session_trades": 0, "sources": []}


def read_json(path):
    with open(path) as fh:
        return json.load(fh)


def write_json(path, obj):
    with open(path, "w") as fh:
        json.dump(obj, fh)
    return path


def run_cli(script, *args):
    return subprocess.run([sys.executable, "-I", "-B", os.path.join(WF, script)] + list(args),
                          capture_output=True, text=True)


def cand(col, s, trades=500, n=252):
    params = sel.GRID[sel.GRID_COLUMNS.index(col)]
    return {"column": col, "params": params, "sharpe": s, "trades": trades, "n_sessions": n}


# ------------------------------------------------------------------- statistic
class TestSharpe(unittest.TestCase):
    def test_hand_computed(self):
        # d = [1,2,3,4]: mean 2.5; sd(n-1) = sqrt(((1.5^2+0.5^2)*2)/3) = sqrt(5/3) = 1.2909944...
        # S = 2.5 / 1.2909944 * sqrt(252) = 2.5 * sqrt(3/5) * 15.8745079 = sqrt(6.25*0.6*252) = sqrt(945)
        #   = 30.740852297878796
        s = sel.sharpe([1, 2, 3, 4])
        self.assertAlmostEqual(s, math.sqrt(945), delta=1e-12)
        self.assertAlmostEqual(s, 2.5 / math.sqrt(5 / 3) * math.sqrt(252), delta=1e-12)
        self.assertAlmostEqual(s, 30.740852297878796, delta=1e-12)
        self.assertAlmostEqual(sel.sharpe([-1, -2, -3, -4]), -math.sqrt(945), delta=1e-12)

    def test_zero_days_included(self):
        # d = [0,0,5,0] (§6 :93 "0 if none"): mean 1.25; deviations -1.25 x3, 3.75;
        # var = (3*1.5625 + 14.0625)/3 = 18.75/3 = 6.25, sd 2.5; S = 0.5*sqrt(252) = 7.937253933193772
        self.assertAlmostEqual(sel.sharpe([0, 0, 5, 0]), 0.5 * math.sqrt(252), delta=1e-12)

    def test_undefined(self):
        self.assertIsNone(sel.sharpe([0.0] * 252))   # §6 :95 zero sd -> ineligible
        self.assertIsNone(sel.sharpe([3.7] * 9))
        self.assertIsNone(sel.sharpe([5.0]))         # n < 2
        self.assertIsNone(sel.sharpe([]))
        self.assertEqual(sel.sharpe([1.0, -1.0] * 5), 0.0)

    def test_matches_statistics_module(self):
        rng = random.Random(11)
        for _ in range(200):
            d = [round(rng.uniform(-900, 900), 2) * (rng.random() < 0.6) for _ in range(rng.randint(2, 300))]
            if len(set(d)) < 2:
                continue
            ref = statistics.mean(d) / statistics.stdev(d) * math.sqrt(252)
            self.assertAlmostEqual(sel.sharpe(d), ref, delta=1e-9 * max(1.0, abs(ref)))

    def test_int_division_correctly_rounded(self):
        # sharpe_from_sums relies on CPython int/int true division being correctly rounded.
        rng = random.Random(5)
        for _ in range(2000):
            a, b = rng.getrandbits(rng.randint(1, 200)) + 1, rng.getrandbits(rng.randint(1, 200)) + 1
            self.assertEqual(a / b, float(Fraction(a, b)))

    def test_non_finite_rejected(self):
        with self.assertRaises(sel.InputError):
            sel.sharpe([1.0, float("nan")])


class TestEligibility(unittest.TestCase):
    def test_252(self):  # §6 :94 "100 trades per 252-session in-sample window"
        self.assertTrue(sel.eligible(1.0, 100, 252))
        self.assertFalse(sel.eligible(1.0, 99, 252))

    def test_pro_rata_656(self):  # §7 :105 "100 × sessions / 252" = 260.317... on 656
        self.assertFalse(sel.eligible(1.0, 260, 656))
        self.assertTrue(sel.eligible(1.0, 261, 656))

    def test_undefined_sharpe_ineligible(self):
        self.assertFalse(sel.eligible(None, 10 ** 6, 252))


class TestGridAndTieBreak(unittest.TestCase):
    def test_grid(self):
        self.assertEqual(len(sel.GRID_COLUMNS), 81)
        self.assertEqual(sel.GRID_COLUMNS[0], "L10_k0.8_m1.5_BandOrVWAP")
        self.assertEqual(sel.GRID_COLUMNS[1], "L10_k0.8_m1.5_OppBand")
        self.assertEqual(sel.GRID_COLUMNS[5], "L10_k0.8_m2.25_Flat1559")
        self.assertEqual(sel.GRID_COLUMNS[-1], "L18_k1.2_m3_Flat1559")

    def test_anchor_distance(self):
        g = lambda c: sel.GRID[sel.GRID_COLUMNS.index(c)]
        self.assertEqual(sel.anchor_distance(g("L14_k1.0_m1.5_BandOrVWAP")), 0)
        self.assertEqual(sel.anchor_distance(g("L14_k1.0_m3_BandOrVWAP")), 0)  # stop adds 0
        self.assertEqual(sel.anchor_distance(g("L10_k1.2_m3_Flat1559")), 3)
        self.assertEqual(sel.anchor_distance(g("L18_k0.8_m2.25_OppBand")), 3)
        with self.assertRaises(sel.InputError):
            sel.anchor_distance({"Lookback": 12, "NoiseMult": 1.0, "StopAtrMult": 1.5,
                                 "ExitPolicy": "BandOrVWAP", "Contracts": 1})

    def test_tie_within_1e10_anchor_wins(self):
        a = cand("L10_k0.8_m1.5_BandOrVWAP", 1.0)          # distance 2, best S
        b = cand("L14_k1.0_m3_OppBand", 1.0 - 1e-10)        # distance 1, tied to 1e-9
        self.assertEqual(sel.pick([a, b]), "L14_k1.0_m3_OppBand")
        self.assertEqual(sel.select_one([a, b])["tied"], [a["column"], b["column"]])

    def test_outside_tolerance_best_wins(self):
        a = cand("L10_k0.8_m1.5_BandOrVWAP", 1.0)
        b = cand("L14_k1.0_m1.5_BandOrVWAP", 1.0 - 2e-9)
        self.assertEqual(sel.pick([a, b]), "L10_k0.8_m1.5_BandOrVWAP")

    def test_equal_distance_lexicographic(self):
        # stop axis: m 1.5 before 3
        self.assertEqual(sel.pick([cand("L14_k1.0_m3_BandOrVWAP", 2.0),
                                   cand("L14_k1.0_m1.5_BandOrVWAP", 2.0)]), "L14_k1.0_m1.5_BandOrVWAP")
        # all distance 1: lookback 10 first
        self.assertEqual(sel.pick([cand("L14_k1.0_m1.5_OppBand", 2.0), cand("L14_k0.8_m1.5_BandOrVWAP", 2.0),
                                   cand("L10_k1.0_m2.25_BandOrVWAP", 2.0)]), "L10_k1.0_m2.25_BandOrVWAP")
        # policy order: OppBand before Flat1559
        self.assertEqual(sel.pick([cand("L14_k1.2_m1.5_Flat1559", 2.0),
                                   cand("L14_k1.2_m1.5_OppBand", 2.0)]), "L14_k1.2_m1.5_OppBand")

    def test_ineligible_ignored_and_none(self):
        hi = cand("L14_k1.0_m1.5_BandOrVWAP", 9.0, trades=99)
        lo = cand("L18_k1.2_m3_Flat1559", 0.1)
        self.assertEqual(sel.pick([hi, lo]), "L18_k1.2_m3_Flat1559")
        self.assertIsNone(sel.pick([hi, cand("L10_k0.8_m1.5_OppBand", None)]))
        self.assertEqual(sel.select_one([hi])["eligible"], 0)


# ------------------------------------------------------------------------ CLI
START = 400  # arm-b synthetic columns trade one per session from s400 on


class TestCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        t = cls.tmp.name
        cls.cal = make_calendar()
        cls.cal_path = write_json(os.path.join(t, "cal.json"), cls.cal)
        n = cls.cal["N"]
        rng = random.Random(3)
        # arm a: random P&L on ~half the days
        tr = [1 if rng.random() < 0.5 else 0 for _ in range(n)]
        net = [round(rng.uniform(-400, 500), 2) if c else 0.0 for c in tr]
        cls.arma = make_daily("armA", None, net, tr)
        cls.arma_path = write_json(os.path.join(t, "armA.json"), cls.arma)
        # arm b: WIN = mean 10 +- 1 (highest Sharpe, last in tie order, distance 3);
        # BIG = mean 100 +- 90 (highest NET, lower Sharpe); others +-a alternating, mean ~0.
        cls.bdir = os.path.join(t, "b")
        os.mkdir(cls.bdir)
        cls.win, cls.big = "L18_k1.2_m3_Flat1559", "L10_k0.8_m1.5_BandOrVWAP"
        cls.bpaths = {}
        for j, (col, prm) in enumerate(zip(sel.GRID_COLUMNS, sel.GRID)):
            alt = [(1 if i % 2 else -1) for i in range(n)]
            if col == cls.win:
                vals = [10.0 + a for a in alt]
            elif col == cls.big:
                vals = [100.0 + 90.0 * a for a in alt]
            else:
                vals = [(1.0 + j / 100.0) * a for a in alt]
            net = [vals[i] if i + 1 >= START else 0.0 for i in range(n)]
            trs = [1 if i + 1 >= START else 0 for i in range(n)]
            cls.bpaths[col] = write_json(os.path.join(cls.bdir, col + ".json"), make_daily(col, prm, net, trs))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def out(self, name):
        return os.path.join(self.tmp.name, name)

    def test_arm_a(self):
        r = run_cli("select.py", "--arm", "a", "--calendar", self.cal_path, "--daily", self.arma_path,
                    "--out", self.out("a.json"))
        self.assertEqual(r.returncode, 0, r.stderr)
        o = read_json(self.out("a.json"))
        self.assertEqual((o["schema"], o["arm"], o["columns"]), ("praxis-wf-selection/1", "a", ["armA"]))
        self.assertEqual(len(o["windows"]), 17)
        tot = 0
        for w, cw in zip(o["windows"], self.cal["windows"]):
            c, e = cw["oos"]
            self.assertEqual(w["oos_daily"], self.arma["daily_net"][c - 1:e])
            self.assertEqual(len(w["oos_daily"]), 63)
            self.assertEqual(w["oos_trades"], sum(self.arma["daily_trades"][c - 1:e]))
            self.assertEqual(len(w["oos_trade_list"]), w["oos_trades"])
            self.assertTrue(all(c <= t["session"] <= e for t in w["oos_trade_list"]))
            self.assertAlmostEqual(w["oos_net"], math.fsum(w["oos_daily"]), delta=1e-9)
            self.assertEqual((w["pick"], w["eligible"], w["no_eligible"]), ("armA", None, False))
            tot += w["oos_trades"]
        self.assertEqual(o["oos_total_trades"], tot)
        self.assertEqual(o["full_span"]["trades"], sum(self.arma["daily_trades"]))
        self.assertAlmostEqual(o["full_span"]["net"], math.fsum(self.arma["daily_net"]), delta=1e-9)

    def test_arm_b_picks_and_no_eligible(self):
        r = run_cli("select.py", "--arm", "b", "--calendar", self.cal_path, "--daily", self.bdir,
                    "--out", self.out("b.json"))
        self.assertEqual(r.returncode, 0, r.stderr)
        o = read_json(self.out("b.json"))
        self.assertEqual(o["columns"], sel.GRID_COLUMNS)
        for w in o["windows"]:
            a, b = w["is"]
            n_trading = max(0, b - max(a, START) + 1)
            if n_trading < 100:  # windows 1-4: IS ends <= 441, < 100 trades from s400
                self.assertLessEqual(w["k"], 4)
                self.assertTrue(w["no_eligible"])
                self.assertIsNone(w["pick"])
                self.assertEqual((w["eligible"], w["oos_net"], w["oos_trades"], w["oos_trade_list"]),
                                 (0, 0.0, 0, []))
                self.assertEqual(w["oos_daily"], [0.0] * 63)
            else:
                self.assertGreaterEqual(w["k"], 5)
                self.assertEqual((w["pick"], w["tied"], w["eligible"]), (self.win, [self.win], 81))
                self.assertEqual(w["oos_trades"], 63)
        # window 4's OOS (s442-s504) has P&L in every column, yet arm b trades nothing there
        self.assertEqual(o["windows"][3]["oos"], [442, 504])
        # net profit is never the objective (§6 :98): BIG has 10x WIN's net, never picked
        self.assertNotIn(self.big, [w["pick"] for w in o["windows"]])

    def _fail(self, paths, needle, arm="b"):
        r = run_cli("select.py", "--arm", arm, "--calendar", self.cal_path, "--daily", *paths,
                    "--out", self.out("f.json"))
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn(needle, r.stderr)
        return r

    def test_missing_column(self):
        self._fail([p for c, p in self.bpaths.items() if c != self.win], "missing 1")

    def test_extra_column(self):
        prm = {"Lookback": 14, "NoiseMult": 1.0, "StopAtrMult": 2.0, "ExitPolicy": "BandOrVWAP", "Contracts": 1}
        x = write_json(self.out("extra.json"), make_daily("L14_k1.0_m2_BandOrVWAP", prm, [0.0] * 1352, [0] * 1352))
        self._fail(list(self.bpaths.values()) + [x], "extra 1")

    def test_duplicate_column(self):
        d = read_json(self.bpaths[self.win])
        x = write_json(self.out("dup.json"), d)
        self._fail(list(self.bpaths.values()) + [x], "duplicate column")

    def test_truncated_refused(self):
        d = read_json(self.arma_path)
        d["truncated"] = True
        self._fail([write_json(self.out("trunc.json"), d)], "§7 :112", arm="a")

    def test_n_mismatch_refused(self):
        d = make_daily("armA", None, [0.0] * 1351, [0] * 1351)
        self._fail([write_json(self.out("n.json"), d)], "does not match calendar N", arm="a")

    def test_inconsistent_trade_list_refused(self):
        d = read_json(self.arma_path)
        d["daily_trades"][0] += 1
        self._fail([write_json(self.out("bad.json"), d)], "daily_trades", arm="a")



class TestW6Refusals(unittest.TestCase):
    """W6 fix round: defects 1-3 (values-spec §5 :84, §7 :112)."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.cal = make_calendar()
        cls.cal_path = write_json(os.path.join(cls.tmp.name, "cal.json"), cls.cal)
        n = cls.cal["N"]
        cls.arma = make_daily("armA", None, [0.0] * n, [0] * n)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def out(self, name):
        return os.path.join(self.tmp.name, name)

    def run_a(self, daily, cal=None):
        cp = self.cal_path if cal is None else write_json(self.out("cal_x.json"), cal)
        dp = write_json(self.out("armA_x.json"), daily)
        return run_cli("select.py", "--arm", "a", "--calendar", cp, "--daily", dp,
                       "--out", self.out("sel_x.json")), dp

    def refused(self, daily, needles, cal=None):
        r, dp = self.run_a(daily, cal)
        self.assertEqual(r.returncode, 2, r.stderr)
        for nd in needles:
            self.assertIn(nd, r.stderr)
        return dp

    def test_control_accepted(self):
        r, _ = self.run_a(self.arma)
        self.assertEqual(r.returncode, 0, r.stderr)

    # defect 1
    def test_missing_pnl_basis_in_refused(self):
        d = json.loads(json.dumps(self.arma))
        del d["pnl_basis_in"]
        r, dp = self.run_a(d)
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn(dp, r.stderr)
        self.assertIn("'pnl_basis_in'", r.stderr)
        self.assertNotIn("Traceback", r.stderr)

    # defect 2
    def test_exactly_5000_untruncated_refused(self):
        n = self.cal["N"]
        ntr = [4] * 1250 + [0] * (n - 1250)
        d = make_daily("armA", None, [0.0] * n, ntr)
        self.assertEqual((d["n_trades"], len(d["trades"]), d["truncated"]), (5000, 5000, False))
        self.refused(d, ["§7 :112", "5000"])

    def test_4999_untruncated_accepted(self):
        n = self.cal["N"]
        ntr = [4] * 1249 + [3] + [0] * (n - 1250)
        r, _ = self.run_a(make_daily("armA", None, [0.0] * n, ntr))
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_n_trades_5000_claimed_refused(self):
        d = json.loads(json.dumps(self.arma))
        d["n_trades"] = 5000
        self.refused(d, ["§7 :112"])

    def test_n_trades_ne_len_trades_refused(self):
        n = self.cal["N"]
        d = make_daily("armA", None, [0.0] * n, [1] * 10 + [0] * (n - 10))
        d["n_trades"] = 11
        self.refused(d, ["n_trades=11 != len(trades)=10"])

    def test_n_trades_missing_refused(self):
        d = json.loads(json.dumps(self.arma))
        del d["n_trades"]
        self.refused(d, ["'n_trades'"])

    def test_n_trades_ne_sum_daily_trades_refused(self):
        n = self.cal["N"]
        d = make_daily("armA", None, [0.0] * n, [1] * 10 + [0] * (n - 10))
        d["daily_trades"][20] = 1
        self.refused(d, ["n_trades=10 != sum(daily_trades)=11"])

    # defect 3
    def test_short_k_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["windows"] = cal["windows"][:16]
        cal["K"] = 16
        cal["oos_sessions"] = 16 * 63
        self.refused(self.arma, ["K=16 but N=1352 implies K=17"], cal=cal)

    def test_oos_sessions_mismatch_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["oos_sessions"] = 1070
        self.refused(self.arma, ["oos_sessions=1070"], cal=cal)

    def test_dropped_mismatch_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["dropped"] = [1325, 1352]
        self.refused(self.arma, ["dropped=[1325, 1352]", "[1324, 1352]"], cal=cal)

    def test_cscv_rows_mismatch_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["cscv_rows"] = [1, 1312]
        self.refused(self.arma, ["cscv_rows=[1, 1312]", "[12, 1323]"], cal=cal)

    def test_cscv_block_mismatch_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["cscv_block"] = 81
        self.refused(self.arma, ["cscv_block=81"], cal=cal)

    def test_window_range_mismatch_refused(self):
        cal = json.loads(json.dumps(self.cal))
        cal["windows"][4]["oos"] = [505, 568]
        self.refused(self.arma, ["window 5"], cal=cal)


if __name__ == "__main__":
    unittest.main()
