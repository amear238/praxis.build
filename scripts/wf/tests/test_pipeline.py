"""End-to-end test of the five walk-forward scripts run together through their CLIs.

sessions.py (real data file, read-only) -> tradelist.py (82 runs) -> select.py --arm a / --arm b
-> pbo.py -> report.py, on SYNTHETIC bridge JSONs (seeded random.Random). Also: the stdlib
`select` import hazard (scripts/wf/select.py shadows it), the pnl-basis passthrough, a gross-basis
run, and the 5000-trade truncation refusal.

Run: python3 -I -B -m unittest discover -s scripts/wf/tests -p 'test_pipeline.py' -v
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
# Same path setup as the sibling tests: APPEND (not insert at 0) so the stdlib resolves first.
sys.path.append(WF)

import select  # noqa: E402  (must be the stdlib, not scripts/wf/select.py)
import subprocess  # noqa: E402

import json  # noqa: E402
import random  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402
import unittest  # noqa: E402
import zlib  # noqa: E402
from decimal import Decimal  # noqa: E402

DATA = "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
REPO = os.path.dirname(os.path.dirname(WF))
COST_MODEL = os.path.join(REPO, "config", "backtest-cost-model.json")
STANDING = ("Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; "
            "2 ticks/side slippage assumed.")
# values-spec §3 :49-52 grid, §6 :97 order.
LOOKBACKS = (10, 14, 18)
NOISE_MULTS = (0.8, 1.0, 1.2)
STOP_MULTS = (1.5, 2.25, 3.0)
POLICIES = ("BandOrVWAP", "OppBand", "Flat1559")
GRID = [{"Lookback": lb, "NoiseMult": k, "StopAtrMult": m, "ExitPolicy": p, "Contracts": 1}
        for lb in LOOKBACKS for k in NOISE_MULTS for m in STOP_MULTS for p in POLICIES]
SEED = 20261107


def colname(params):
    if params is None:
        return "armA"
    return "L{}_k{:.1f}_m{:g}_{}".format(params["Lookback"], params["NoiseMult"],
                                        params["StopAtrMult"], params["ExitPolicy"])


def gen_bridge(dates, column, per_session=None, n_exact=None):
    """Synthetic bridge JSON (shape: bridge report B14). One trade on ~70% of sessions from s16
    on, or `per_session` trades on every session from s16 until `n_exact` trades exist."""
    rng = random.Random(SEED ^ zlib.crc32(column.encode("utf-8")))
    mu = rng.uniform(-25.0, 45.0)          # per-column drift so selection has something to pick
    trades = []
    for d in dates[15:]:                   # dates[15] = session 16
        k = per_session if per_session else (1 if rng.random() < 0.7 else 0)
        for j in range(k):
            if n_exact is not None and len(trades) >= n_exact:
                break
            eh, em = 10 + j, rng.randrange(0, 50)
            hold = rng.randrange(1, 9)
            side = "Long" if rng.random() < 0.5 else "Short"
            pnl = round(rng.gauss(mu, 300.0), 2)
            px = round(15000 + rng.uniform(-500, 500) * 4) / 4
            trades.append({
                "pnl": pnl, "marketPosition": side,
                "entryTime": "%sT%02d:%02d:00.0000000" % (d, eh, em),
                "exitTime": "%sT%02d:%02d:00.0000000" % (d, eh, em + hold),
                "entryPrice": px, "exitPrice": px + round(pnl / 20.0 * 4) / 4,
                "exitName": rng.choice(["Stop", "Band", "VWAP", "Flat1559"])})
    net = sum((Decimal(repr(t["pnl"])) for t in trades), Decimal(0))
    pf_w = sum(t["pnl"] for t in trades if t["pnl"] > 0)
    pf_l = -sum(t["pnl"] for t in trades if t["pnl"] < 0)
    return {"id": "synthetic-" + column, "status": "ok", "strategy": "PraxisORB",
            "metrics": {"totalTrades": len(trades), "profitFactor": round(pf_w / pf_l, 4) if pf_l else 0.0,
                        "netProfit": float(net), "maxDrawdown": 0.0},
            "trades": trades}


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, sort_keys=True, indent=1)
        f.write("\n")


def cli(script, *args):
    return subprocess.run([sys.executable, "-I", "-B", os.path.join(WF, script)] + list(args),
                          capture_output=True, text=True)


def read_bytes(p):
    with open(p, "rb") as f:
        return f.read()


def run_pipeline(root, cal, dates, outdir):
    """Full run: generate 82 bridge files, 82 tradelist runs, select a/b, pbo, report.
    Returns {name: CompletedProcess}."""
    bdir, ddir, adir = (os.path.join(root, x) for x in ("bridge", "daily_b", "daily_a"))
    for d in (bdir, ddir, adir, outdir):
        os.makedirs(d, exist_ok=True)
    procs = {}
    jobs = [(None, os.path.join(adir, "armA.json"))] + [
        (p, os.path.join(ddir, colname(p) + ".json")) for p in GRID]
    for params, dpath in jobs:
        col = colname(params)
        bpath = os.path.join(bdir, "backtest_%s.json" % col)
        write_json(bpath, gen_bridge(dates, col))
        arm = ["--arm-a"] if params is None else ["--params-json", json.dumps(params, sort_keys=True)]
        procs["tradelist " + col] = cli("tradelist.py", "--calendar", cal, "--pnl-basis", "net",
                                        "--bridge", bpath, *arm, "--out", dpath)
    sel_a, sel_b = os.path.join(outdir, "sel_a.json"), os.path.join(outdir, "sel_b.json")
    pbo, rep = os.path.join(outdir, "pbo.json"), os.path.join(outdir, "report.md")
    procs["select a"] = cli("select.py", "--arm", "a", "--calendar", cal,
                            "--daily", os.path.join(adir, "armA.json"), "--out", sel_a)
    procs["select b"] = cli("select.py", "--arm", "b", "--calendar", cal, "--daily", ddir, "--out", sel_b)
    procs["pbo"] = cli("pbo.py", "--calendar", cal, "--daily", ddir, "--out", pbo)
    procs["report"] = cli("report.py", "--calendar", cal, "--sel-a", sel_a, "--sel-b", sel_b,
                          "--pbo", pbo, "--out", rep)
    return procs


class TestImportHazard(unittest.TestCase):
    def test_stdlib_select_resolves_in_this_process(self):
        f = getattr(select, "__file__", None)   # None would mean a builtin: also the stdlib
        self.assertFalse(f is not None and os.path.realpath(f).startswith(os.path.realpath(WF) + os.sep),
                         "select resolved to %r (scripts/wf/select.py shadows the stdlib)" % f)
        self.assertTrue(hasattr(select, "select"))
        self.assertTrue(callable(subprocess.run))

    def test_fresh_interpreter_append_vs_insert(self):
        # Fresh process: nothing cached. append -> stdlib; insert(0) -> the shadow (positive control).
        code = ("import sys; sys.path.{}; import select; "
                "print(getattr(select, '__file__', '<builtin>'))")
        app = subprocess.run([sys.executable, "-I", "-B", "-c",
                              code.format("append(%r)" % WF) + "; import subprocess, sessions, tradelist"],
                             capture_output=True, text=True)
        self.assertEqual(app.returncode, 0, app.stderr)
        self.assertFalse(os.path.realpath(app.stdout.strip()).startswith(os.path.realpath(WF) + os.sep),
                         app.stdout)
        ins = subprocess.run([sys.executable, "-I", "-B", "-c", code.format("insert(0, %r)" % WF)],
                             capture_output=True, text=True)
        self.assertEqual(os.path.realpath(ins.stdout.strip()), os.path.realpath(os.path.join(WF, "select.py")),
                         "positive control: insert(0) should pick up scripts/wf/select.py")


class TestPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not os.path.isfile(DATA):
            raise unittest.SkipTest("real data file absent: %s" % DATA)
        cls.tmp = tempfile.mkdtemp(prefix="praxis-wf-e2e-")
        cls.cal = os.path.join(cls.tmp, "cal.json")
        p = cli("sessions.py", "--data", DATA, "--out", cls.cal)
        if p.returncode != 0:
            raise RuntimeError("sessions.py failed: %s" % p.stderr)
        with open(cls.cal, encoding="utf-8") as f:
            cls.calendar = json.load(f)
        cls.dates = [s["date"] for s in cls.calendar["sessions"]]
        cls.run1 = os.path.join(cls.tmp, "run1")
        cls.run2 = os.path.join(cls.tmp, "run2")
        cls.procs1 = run_pipeline(cls.tmp, cls.cal, cls.dates, cls.run1)
        cls.procs2 = run_pipeline(cls.tmp, cls.cal, cls.dates, cls.run2)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _load(self, name, run=None):
        with open(os.path.join(run or self.run1, name), encoding="utf-8") as f:
            return json.load(f)

    def test_exit_codes_all_zero(self):
        self.assertEqual(len([k for k in self.procs1 if k.startswith("tradelist ")]), 82)
        for procs in (self.procs1, self.procs2):
            for name, p in procs.items():
                self.assertEqual(p.returncode, 0, "%s: %s" % (name, p.stderr))

    def test_report_standing_sentence_line3_once(self):
        with open(os.path.join(self.run1, "report.md"), encoding="utf-8") as f:
            text = f.read()
        self.assertEqual(text.split("\n")[2], STANDING)
        self.assertEqual(text.count(STANDING), 1)

    def test_gates_2_and_6_open_both_arms(self):
        with open(os.path.join(self.run1, "report.md"), encoding="utf-8") as f:
            lines = f.read().split("\n")
        for n in ("2. ", "6. "):
            hits = [ln for ln in lines if ln.startswith(n) and "— OPEN." in ln]
            self.assertEqual(len(hits), 2, "gate %s OPEN lines: %r" % (n.strip(), hits))

    def test_pbo_range_and_splits(self):
        pbo = self._load("pbo.json")
        self.assertEqual(pbo["splits"], 12870)
        self.assertGreaterEqual(pbo["pbo"], 0.0)
        self.assertLessEqual(pbo["pbo"], 1.0)

    def test_17_windows(self):
        self.assertEqual(self.calendar["K"], 17)
        for name in ("sel_a.json", "sel_b.json"):
            self.assertEqual(len(self._load(name)["windows"]), 17, name)

    def test_second_run_byte_identical(self):
        for name in ("sel_a.json", "sel_b.json", "pbo.json", "report.md"):
            self.assertEqual(read_bytes(os.path.join(self.run1, name)),
                             read_bytes(os.path.join(self.run2, name)), name)

    def test_pnl_basis_passthrough(self):
        sa, sb = self._load("sel_a.json"), self._load("sel_b.json")
        self.assertEqual(sa["pnl_basis_in"], {"armA": "net"})
        self.assertEqual(sorted(sb["pnl_basis_in"]), sorted(colname(p) for p in GRID))
        self.assertEqual(set(sb["pnl_basis_in"].values()), {"net"})
        with open(os.path.join(self.run1, "report.md"), encoding="utf-8") as f:
            text = f.read()
        self.assertNotIn("not present in the selection JSON", text)
        self.assertIn("Input pnl basis: arm (a) net (1 column); arm (b) net (81 columns).", text)

    def test_gross_basis_end_to_end(self):
        with open(COST_MODEL, encoding="utf-8") as f:
            rt = json.load(f)["cost_model"]["commission_round_turn_usd"]
        self.assertEqual(rt, 4.68)
        g = os.path.join(self.tmp, "gross")
        os.makedirs(g, exist_ok=True)
        bridge = gen_bridge(self.dates, "armA")
        bpath, dpath = os.path.join(g, "backtest_gross.json"), os.path.join(g, "armA.json")
        write_json(bpath, bridge)
        p = cli("tradelist.py", "--calendar", self.cal, "--pnl-basis", "gross", "--bridge", bpath,
                "--arm-a", "--out", dpath)
        self.assertEqual(p.returncode, 0, p.stderr)
        sel = os.path.join(g, "sel_a.json")
        p = cli("select.py", "--arm", "a", "--calendar", self.cal, "--daily", dpath, "--out", sel)
        self.assertEqual(p.returncode, 0, p.stderr)
        rep = os.path.join(g, "report.md")
        p = cli("report.py", "--calendar", self.cal, "--sel-a", sel,
                "--sel-b", os.path.join(self.run1, "sel_b.json"),
                "--pbo", os.path.join(self.run1, "pbo.json"), "--out", rep)
        self.assertEqual(p.returncode, 0, p.stderr)
        with open(sel, encoding="utf-8") as f:
            s = json.load(f)
        pnl_by_exit = {t["exitTime"][:19]: t["pnl"] for t in bridge["trades"]}
        checked = 0
        for w in s["windows"]:
            for t in w["oos_trade_list"]:
                pnl = pnl_by_exit[t["exit_time"][:19]]
                self.assertAlmostEqual(t["net_pnl"], pnl - 4.68, places=9)
                self.assertAlmostEqual(t["gross_pnl"], pnl, places=9)
                checked += 1
        self.assertEqual(checked, s["oos_total_trades"])
        self.assertGreater(checked, 500)
        n = len(bridge["trades"])
        self.assertEqual(s["full_span"]["trades"], n)
        exp = sum(Decimal(repr(t["pnl"])) for t in bridge["trades"]) - Decimal("4.68") * n
        self.assertAlmostEqual(s["full_span"]["net"], float(exp), places=6)
        self.assertEqual(s["pnl_basis_in"], {"armA": "gross"})
        with open(rep, encoding="utf-8") as f:
            self.assertIn("Input pnl basis: arm (a) gross (1 column); arm (b) net (81 columns).", f.read())

    def test_5000_trades_select_refuses(self):
        g = os.path.join(self.tmp, "trunc")
        os.makedirs(g, exist_ok=True)
        bridge = gen_bridge(self.dates, "armA", per_session=4, n_exact=5000)
        self.assertEqual(len(bridge["trades"]), 5000)
        bpath, dpath = os.path.join(g, "backtest_5000.json"), os.path.join(g, "armA.json")
        write_json(bpath, bridge)
        p = cli("tradelist.py", "--calendar", self.cal, "--pnl-basis", "net", "--bridge", bpath,
                "--arm-a", "--out", dpath)
        self.assertEqual(p.returncode, 0, p.stderr)
        with open(dpath, encoding="utf-8") as f:
            self.assertIs(json.load(f)["truncated"], True)
        out = os.path.join(g, "sel_a.json")
        p = cli("select.py", "--arm", "a", "--calendar", self.cal, "--daily", dpath, "--out", out)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("truncat", p.stderr.lower())
        self.assertFalse(os.path.exists(out))


if __name__ == "__main__":
    unittest.main()
