"""Tests for scripts/wf/report.py — synthetic JSON fixtures in a tempdir.

Run: python3 -I -m unittest discover -s scripts/wf/tests -p 'test_report.py' -v
"""

import datetime
import decimal
import json
import math
import contextlib
import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(HERE))  # scripts/wf (python3 -I implies -P)

import report  # noqa: E402

NQ_RT = 4.68  # config/backtest-cost-model.json cost_model.commission_round_turn_usd


GRID_COLUMNS = ["L{}_k{}_m{}_{}".format(L, k, m, p) for L in (10, 14, 18) for k in ("0.8", "1.0", "1.2")
                for m in ("1.5", "2.25", "3") for p in ("BandOrVWAP", "OppBand", "Flat1559")]


def make_calendar(K=17, is_len=252, oos_len=63, extra=0):
    # values-spec IS 252 / OOS 63 / STEP 63; N = 252 + 63K (+ extra < 63 dropped sessions).
    # W8: K = 17 (the RULED calendar) so the CSCV shape is S 16 x block 82 = 1312 rows.
    n_total = is_len + K * oos_len + extra
    d0 = datetime.date(2021, 3, 8)
    sessions = []
    d = d0
    while len(sessions) < n_total:
        if d.weekday() < 5:
            sessions.append({"n": len(sessions) + 1, "date": d.isoformat(), "first_bar": "09:31",
                             "last_bar": "16:00", "early_close_in_file": False,
                             "nt8_last_bar": "16:00", "nt8_last_bar_grade": "synthetic"})
        d += datetime.timedelta(days=1)
    windows = []
    for k in range(1, K + 1):
        oa = is_len + (k - 1) * oos_len + 1
        ob = oa + oos_len - 1
        ia, ib = oa - is_len, oa - 1
        windows.append({"k": k, "is": [ia, ib], "oos": [oa, ob],
                        "is_dates": [sessions[ia - 1]["date"], sessions[ib - 1]["date"]],
                        "oos_dates": [sessions[oa - 1]["date"], sessions[ob - 1]["date"]],
                        "is_holes": k % 3, "oos_holes": 0, "is_early_close": 1, "oos_early_close": k % 2})
    return {"schema": "praxis-wf-calendar/1", "source": {"path": "synthetic", "bytes": 0, "sha256": "0"},
            "rule": {}, "N": n_total, "sessions": sessions, "windows": windows, "K": K,
            "oos_sessions": K * oos_len, "dropped": None, "dropped_dates": [],
            "cscv_rows": [is_len + K * oos_len - 1311, is_len + K * oos_len], "cscv_S": 16, "cscv_block": 82,
            "weekend_dates_dropped": 0}


def make_selection(cal, arm, trades_by_window, no_eligible=()):
    """trades_by_window: list (per window) of list of (offset_in_oos, net_pnl)."""
    ws = []
    tot_net = 0.0
    tot_tr = 0
    for cw, trades in zip(cal["windows"], trades_by_window):
        a, b = cw["oos"]
        span = b - a + 1
        daily = [0.0] * span
        tl = []
        for j, (off, net) in enumerate(trades):
            s = a + off
            date = cal["sessions"][s - 1]["date"]
            tl.append({"session": s, "entry_time": "{}T10:00:00".format(date),
                       "exit_time": "{}T10:{:02d}:{:02d}".format(date, 1 + j // 60, j % 60),
                       "side": "Long", "net_pnl": net, "exit_name": "x",
                       # as tradelist.py does: Decimal arithmetic, then float (no float residue)
                       "gross_pnl": float(decimal.Decimal(repr(net)) + decimal.Decimal(repr(NQ_RT)))})
            daily[off] += net
        ne = cw["k"] in no_eligible
        ws.append({"k": cw["k"], "is": cw["is"], "oos": cw["oos"], "eligible": 0 if ne else 81,
                   "pick": None if (ne or arm == "a") else "L14_k1.0_m2.25_BandOrVWAP",
                   "pick_is_sharpe": None, "pick_is_trades": None, "tied": [], "no_eligible": ne,
                   "oos_net": sum(daily), "oos_trades": len(tl), "oos_daily": daily, "oos_trade_list": tl})
        tot_net += sum(daily)
        tot_tr += len(tl)
    sel = {"schema": "praxis-wf-selection/1", "arm": arm,
           "columns": ["armA"] if arm == "a" else list(GRID_COLUMNS), "windows": ws,
           "oos_total_net": tot_net, "oos_total_trades": tot_tr}
    if arm == "a":
        sel["full_span"] = {"net": tot_net + 123.45, "trades": tot_tr + 7}
    return sel


def make_pbo(cal, value=None, splits=12870, le0=None):
    if le0 is None:
        le0 = int(round(value * splits))
    return {"schema": "praxis-wf-pbo/1", "S": cal["cscv_S"], "block": cal["cscv_block"],
            "rows": cal["cscv_rows"], "splits": splits, "le0": le0,
            "no_eligible_splits": 0, "pbo": le0 / splits, "threshold": 0.05, "passes": le0 * 20 < splits,
            "logit_summary": {"min": -1.0, "median": 0.5, "max": 2.0}}


def default_trades(K=17, profitable=11):
    """`profitable` windows with +300,-100 (net +200); the rest -100."""
    return [[(0, 300.0), (1, -100.0)] if k < profitable else [(0, -100.0)] for k in range(K)]


class Fixture:
    def __init__(self, cal=None, sel_a=None, sel_b=None, pbo=None):
        self.dir = tempfile.TemporaryDirectory()
        self.cal = cal or make_calendar()
        self.sel_a = sel_a or make_selection(self.cal, "a", default_trades())
        self.sel_b = sel_b or make_selection(self.cal, "b", default_trades())
        self.pbo = pbo or make_pbo(self.cal, 0.01)

    def paths(self):
        p = {}
        for name in ("cal", "sel_a", "sel_b", "pbo"):
            p[name] = os.path.join(self.dir.name, name + ".json")
            with open(p[name], "w") as fh:
                json.dump(getattr(self, name), fh, sort_keys=True)
        p["out"] = os.path.join(self.dir.name, "report.md")
        return p

    def run(self):
        p = self.paths()
        rc = report.main(["--calendar", p["cal"], "--sel-a", p["sel_a"], "--sel-b", p["sel_b"],
                          "--pbo", p["pbo"], "--out", p["out"]])
        text = None
        if rc == 0 and os.path.exists(p["out"]):
            with open(p["out"], encoding="utf-8") as fh:
                text = fh.read()
        return rc, text

    def close(self):
        self.dir.cleanup()


def render(**kw):
    f = Fixture(**kw)
    try:
        rc, text = f.run()
    finally:
        f.close()
    assert rc == 0, "report refused a valid fixture"
    return text


def arm_section(text, arm):
    start = text.index("## Arm ({}) — the six Phase 3 gates".format(arm))
    end = text.index("### Arm ({}) gate 3 per-tier table".format(arm))
    return text[start:end]


def gate_line(text, arm, n):
    for line in arm_section(text, arm).splitlines():
        if line.startswith("{}. ".format(n)):
            return line
    raise AssertionError("gate {} line not found".format(n))


class TestStandingLimitation(unittest.TestCase):
    def test_once_at_line_3(self):
        text = render()
        lines = text.splitlines()
        self.assertTrue(lines[0].startswith("# "))
        self.assertEqual(lines[2], "Standing limitation: Fills are optimistic; Standard resolution on "
                                   "1-minute bars; 2 ticks/side slippage assumed.")
        self.assertEqual(text.count(report.STANDING_LIMITATION), 1)
        self.assertEqual(text.count("Fills are optimistic"), 1)

    def test_deterministic(self):
        self.assertEqual(render(), render())

    def test_provisional_and_judged_arm(self):
        text = render()
        self.assertIn("PROVISIONAL", text)
        self.assertIn("not by itself the go/no-go judgement", text)
        self.assertIn("Judged arm = (a)", text)
        self.assertIn("does not reconcile", text)


class TestProfitFactor(unittest.TestCase):
    def test_hand_series(self):
        pf, why = report.profit_factor([300.0, -100.0, 100.0, -100.0])
        self.assertEqual(pf, 2.0)
        self.assertIsNone(why)

    def test_no_losses_undefined(self):
        pf, why = report.profit_factor([10.0, 20.0, 0.0])
        self.assertIsNone(pf)
        self.assertEqual(why, "undefined (no losses)")

    def test_rendered_hand_series(self):
        cal = make_calendar()
        tr = [[(0, 300.0), (1, -100.0)], [(0, 100.0), (1, -100.0)]] + [[] for _ in range(15)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("PASS (PF = 2.0000;", gate_line(text, "a", 1))

    def test_rendered_no_losses_not_pass(self):
        cal = make_calendar()
        tr = [[(0, 50.0)] for _ in range(17)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        line = gate_line(text, "a", 1)
        self.assertIn("undefined (no losses)", line)
        self.assertNotIn("PASS", line)


class TestGate4(unittest.TestCase):
    def _line(self, n):
        cal = make_calendar()
        tr = [[(i % 3, 1.0 if i % 2 else -1.0) for i in range(n)]] + [[] for _ in range(16)]
        # keep exit order: sort window-1 trades by session offset
        tr[0].sort(key=lambda x: x[0])
        return gate_line(render(cal=cal, sel_a=make_selection(cal, "a", tr)), "a", 4)

    def test_249_fail(self):
        line = self._line(249)
        self.assertIn("FAIL (249 OOS trades)", line)

    def test_250_pass(self):
        line = self._line(250)
        self.assertIn("PASS (250 OOS trades)", line)


class TestGate5(unittest.TestCase):
    def test_eleven_of_seventeen_pass(self):
        line = gate_line(render(), "b", 5)
        self.assertIn("PASS (11/17 windows profitable", line)

    def test_ten_of_seventeen_fail(self):
        cal = make_calendar()
        text = render(cal=cal, sel_b=make_selection(cal, "b", default_trades(profitable=10)))
        self.assertIn("FAIL (10/17 windows profitable", gate_line(text, "b", 5))

    def test_zero_net_window_not_profitable(self):
        cal = make_calendar()
        tr = default_trades(profitable=10)
        tr[10] = [(0, 100.0), (1, -100.0)]  # exactly 0 net
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("FAIL (10/17 windows profitable", gate_line(text, "a", 5))

    def test_no_eligible_window_not_profitable(self):
        cal = make_calendar()
        tr = default_trades(profitable=11)
        tr[0] = []
        sel = make_selection(cal, "b", tr, no_eligible={1})
        text = render(cal=cal, sel_b=sel)
        self.assertIn("FAIL (10/17 windows profitable", gate_line(text, "b", 5))
        self.assertIn("none (no eligible)", text)


class TestDrawdown(unittest.TestCase):
    def test_carried_worse_than_from_start(self):
        # W1 trades +100, -50 ; W2 trades -30, +10 (one per session).
        # from start: W1 ct 50, W2 ct 30. carried: after W1 eq 50 peak 100; W2 -> 20 (dd 80), 30 (dd 70).
        m = report.four_measure_drawdowns([[100.0, -50.0], [-30.0, 10.0]],
                                          [[100.0, -50.0, 0.0], [-30.0, 10.0, 0.0]])
        self.assertEqual(m[0], {"ct_start": 50.0, "eod_start": 50.0, "ct_carry": 50.0,
                                "eod_carry": 50.0, "worst": 50.0})
        self.assertEqual(m[1], {"ct_start": 30.0, "eod_start": 30.0, "ct_carry": 80.0,
                                "eod_carry": 80.0, "worst": 80.0})

    def test_closed_trade_vs_eod(self):
        # one session: +100 then -150 -> ct dd 150 ; eod -50 vs peak 0 -> 50
        m = report.four_measure_drawdowns([[100.0, -150.0]], [[-50.0]])
        self.assertEqual((m[0]["ct_start"], m[0]["eod_start"], m[0]["worst"]), (150.0, 50.0, 150.0))

    def test_no_trade_window_inherits_depth_in_eod_carry(self):
        # W7 (ADV-C D6): the carried-in depth at window start counts in ct_carry too.
        m = report.four_measure_drawdowns([[-40.0], []], [[-40.0], [0.0, 0.0]])
        self.assertEqual(m[1]["ct_carry"], 40.0)
        self.assertEqual(m[1]["eod_carry"], 40.0)
        self.assertEqual((m[1]["ct_start"], m[1]["eod_start"]), (0.0, 0.0))
        self.assertEqual(m[1]["worst"], 40.0)

    def test_rendered_overall_worst(self):
        cal = make_calendar()
        tr = [[(0, 100.0), (1, -50.0)], [(0, -30.0), (1, 10.0)]] + [[] for _ in range(15)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("Overall worst drawdown (max over windows): 1 NQ $80.00", text)
        self.assertIn("Intrabar equity is not available", text)
        self.assertIn("That this equals an own MNQ run is INFERRED", text)


class TestMNQ(unittest.TestCase):
    def test_hand_example(self):
        self.assertTrue(math.isclose(report.mnq_from_nq_gross(95.32 + 4.68, 1.90), 8.10, abs_tol=1e-9))

    def test_rendered_mnq_drawdown(self):
        # W1: net +95.32 then net -104.68 (gross 100 / -100) -> MNQ +8.10, -11.90 -> dd 11.90
        cal = make_calendar()
        tr = [[(0, 95.32), (1, -104.68)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("1 MNQ $11.90", text)

    def test_costs_from_config(self):
        nq, mnq = report.load_costs(report.default_cost_path())
        self.assertEqual((nq, mnq), (4.68, 1.9))


class TestTierTable(unittest.TestCase):
    def test_every_row_no_tier_chosen(self):
        text = render()
        self.assertEqual(len(report.TIERS), 18)  # 16 plan rows + Builder 50K add-on + Flex
        for arm in ("a", "b"):
            start = text.index("### Arm ({}) gate 3 per-tier table".format(arm))
            block = text[start:text.index("\n\n", text.index("|---", start))]
            rows = [l for l in block.splitlines() if l.startswith("| ") and not l.startswith("| Plan")]
            self.assertEqual(len(rows), 18)
            self.assertEqual(sum(1 for r in rows if r.startswith("| Studio")), 3)
            addon = [r for r in rows if "with add-on" in r.split("|")[1]]
            self.assertEqual(len(addon), 1)
            self.assertIn("| $1,500 |", addon[0])
            flex = [r for r in rows if r.startswith("| Flex")]
            self.assertEqual(len(flex), 1)
            self.assertIn("UNVERIFIED", flex[0])
            for r in rows:
                self.assertNotIn("chosen", r.lower())
                self.assertNotIn("PASS", r)
                self.assertNotIn("FAIL", r)
        self.assertNotIn("tier chosen:", text.lower())

    def test_within_exceeds(self):
        # worst NQ dd 250 -> within $1,000 rows; exceeds Studio 5K ($200)
        cal = make_calendar()
        tr = [[(0, -250.0)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        start = text.index("### Arm (a) gate 3 per-tier table")
        block = text[start:text.index("\n\n", text.index("|---", start))]
        studio5 = [l for l in block.splitlines() if l.startswith("| Studio #003")][0]
        rapid25 = [l for l in block.splitlines() if l.startswith("| Rapid · 25K")][0]
        self.assertIn("| $250.00 | exceeds |", studio5)
        self.assertIn("| $250.00 | within |", rapid25)


class TestOpenGates(unittest.TestCase):
    def test_gates_2_and_6_open(self):
        text = render()
        for arm in ("a", "b"):
            for n in (2, 6):
                line = gate_line(text, arm, n)
                self.assertIn("OPEN", line)
                self.assertNotIn("PASS", line)
                self.assertNotIn("FAIL", line)
            self.assertIn("NOT the gate's definition", gate_line(text, arm, 2))
            self.assertIn("NO SINGLE VERDICT", gate_line(text, arm, 3))

    def test_gates_quoted(self):
        text = render()
        for g in report.GATES:
            self.assertEqual(text.count(g), 2)  # once per arm


class TestPBO(unittest.TestCase):
    # W8: splits must be C(16,8) = 12870, so 0.05 exactly (643.5/12870) cannot occur;
    # 644/12870 = 0.05004 is the smallest failing PBO, 643/12870 = 0.04996 the largest passing.
    def test_644_of_12870_fails(self):
        f = Fixture()
        f.pbo = make_pbo(f.cal, le0=644)
        rc, text = f.run()
        f.close()
        self.assertEqual(rc, 0)
        self.assertIn("PBO < 0.05 — FAIL", text)
        self.assertIn("arm (b) does not count", text)

    def test_643_of_12870_passes(self):
        f = Fixture()
        f.pbo = make_pbo(f.cal, le0=643)
        rc, text = f.run()
        f.close()
        self.assertEqual(rc, 0)
        self.assertIn("PBO < 0.05 — PASS", text)
        self.assertNotIn("does not count", text)


class TestRefusals(unittest.TestCase):
    def _rc(self, mutate):
        f = Fixture()
        mutate(f)
        rc, _ = f.run()
        f.close()
        return rc

    def test_window_count_mismatch(self):
        self.assertEqual(self._rc(lambda f: f.sel_a["windows"].pop()), 2)

    def test_window_bounds_mismatch(self):
        self.assertEqual(self._rc(lambda f: f.sel_b["windows"][3].__setitem__("oos", [1, 3])), 2)

    def test_truncated_flag(self):
        self.assertEqual(self._rc(lambda f: f.sel_b.__setitem__("truncated", True)), 2)

    def test_short_daily(self):
        self.assertEqual(self._rc(lambda f: f.sel_a["windows"][0]["oos_daily"].pop()), 2)

    def test_trade_count_mismatch(self):
        self.assertEqual(self._rc(lambda f: f.sel_a["windows"][0].__setitem__("oos_trades", 9)), 2)

    def test_gross_net_mismatch(self):
        self.assertEqual(self._rc(
            lambda f: f.sel_a["windows"][0]["oos_trade_list"][0].__setitem__("gross_pnl", 1.0)), 2)

    def test_missing_full_span(self):
        self.assertEqual(self._rc(lambda f: f.sel_a.pop("full_span")), 2)

    def test_pbo_passes_disagrees(self):
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("passes", False)), 2)

    def test_truncated_json_file(self):
        f = Fixture()
        p = f.paths()
        with open(p["sel_a"], "r+") as fh:
            body = fh.read()
            fh.seek(0)
            fh.truncate()
            fh.write(body[: len(body) // 2])
        rc = report.main(["--calendar", p["cal"], "--sel-a", p["sel_a"], "--sel-b", p["sel_b"],
                          "--pbo", p["pbo"], "--out", p["out"]])
        f.close()
        self.assertEqual(rc, 2)



class TestW6Footnote(unittest.TestCase):
    """W6 fix round, defect 6: per-window table footnote on the 2023-04-05 14:03 day."""
    FOOT = ("Note: the early-close counts include 2023-04-05 (file last bar 14:03), which the "
            "results report INFERS is a data gap, not an early close")

    def cal_with_gap_day(self):
        cal = make_calendar()
        s = [x for x in cal["sessions"] if x["date"] == "2023-04-05"][0]   # a Wednesday, in range
        s.update({"date": "2023-04-05", "last_bar": "14:03", "early_close_in_file": True,
                  "nt8_last_bar": "14:03"})
        return cal

    def test_footnote_once_per_window_table(self):
        text = render(cal=self.cal_with_gap_day())
        self.assertEqual(text.count(self.FOOT), 2)  # arm (a) and arm (b) per-window tables
        for arm in ("a", "b"):
            sec = text[text.index("## Arm ({}) per-window table".format(arm)):]
            sec = sec[:sec.index("Overall worst drawdown")]
            self.assertEqual(sec.count(self.FOOT), 1, arm)
        lines = text.splitlines()
        self.assertEqual(lines[2], report.STANDING_LIMITATION)
        self.assertEqual(text.count(report.STANDING_LIMITATION), 1)
        self.assertEqual(text.count("Fills are optimistic"), 1)

    def test_no_footnote_without_gap_day(self):
        self.assertNotIn(self.FOOT, render())


# ------------------------------------------------------------------ W7 fix round (ADV-C D1-D6)

STAND_CORE = "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."


def tier_row(text, heading, prefix):
    start = text.index(heading)
    block = text[start:text.index("\n\n", text.index("|---", start))]
    return [l for l in block.splitlines() if l.startswith(prefix)][0]


class TestW7ExactMoney(unittest.TestCase):
    def test_d1_pf_exactly_130_passes(self):
        # ADV-C r1: wins 0.32 x5 + 1205.32; losses -79.68 -304.68 -204.68 -249.68 -89.68 -> PF = 1.3 exactly
        cal = make_calendar()
        seq = [0.32] * 5 + [1205.32, -79.68, -304.68, -204.68, -249.68, -89.68]
        tr = [[(i, x) for i, x in enumerate(seq)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("PASS (PF = 1.3000;", gate_line(text, "a", 1))

    def test_d2_mnq_drawdown_exactly_200_is_within_200(self):
        # ADV-C mnq200: 1 MNQ worst drawdown is exactly $200.00; Studio #003 5K limit used = $200
        seq = [100.32, -119.68, -169.68, -109.68, -259.68, -124.68, -84.68, -9.68, -179.68, -64.68,
               -4.68, -184.68, -84.68, -19.68, -189.68, -179.68]
        cal = make_calendar()
        tr = [[(i, x) for i, x in enumerate(seq)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        row = tier_row(text, "### Arm (a) gate 3 per-tier table", "| Studio #003")
        self.assertIn("| $200.00 | within | :115 |", row)


class TestW7Validation(unittest.TestCase):
    def _rc(self, mutate):
        f = Fixture()
        mutate(f)
        rc, _ = f.run()
        f.close()
        return rc

    def test_d3_pick_is_standing_sentence_refused(self):
        self.assertEqual(self._rc(lambda f: f.sel_b["windows"][0].__setitem__(
            "pick", report.STANDING_LIMITATION)), 2)

    def test_d3_pick_off_grid_refused(self):
        def m(f):
            f.sel_b["windows"][0]["pick"] = "L99_k9.9_m9_Nope"
            f.sel_b["columns"].append("L99_k9.9_m9_Nope")
        self.assertEqual(self._rc(m), 2)

    def test_d3_pick_not_in_columns_refused(self):
        def m(f):
            f.sel_b["columns"].remove("L14_k1.0_m2.25_BandOrVWAP")
        self.assertEqual(self._rc(m), 2)

    def test_d3_null_pick_without_no_eligible_refused(self):
        self.assertEqual(self._rc(lambda f: f.sel_b["windows"][0].__setitem__("pick", None)), 2)

    def test_d3_arm_a_no_eligible_refused(self):
        self.assertEqual(self._rc(lambda f: f.sel_a["windows"][0].__setitem__("no_eligible", True)), 2)

    def test_d3_pnl_basis_injection_refused(self):
        self.assertEqual(self._rc(lambda f: f.sel_a.__setitem__("pnl_basis_in", report.STANDING_LIMITATION)), 2)
        self.assertEqual(self._rc(lambda f: f.sel_b.__setitem__(
            "pnl_basis_in", {"L14_k1.0_m2.25_BandOrVWAP": "Net"})), 2)
        self.assertEqual(self._rc(lambda f: f.sel_b.__setitem__(
            "pnl_basis_in", {report.STANDING_LIMITATION: "net"})), 2)

    def test_d3_arm_a_column_must_be_armA(self):
        self.assertEqual(self._rc(lambda f: f.sel_a.__setitem__("columns", ["armB"])), 2)

    def test_d3_valid_bases_accepted(self):
        def m(f):
            f.sel_a["pnl_basis_in"] = {"armA": "gross"}
            f.sel_b["pnl_basis_in"] = {c: "net" for c in GRID_COLUMNS}
        self.assertEqual(self._rc(m), 0)

    def test_d3_final_guard_refuses_duplicate_sentence(self):
        f = Fixture()
        orig = report.render
        report.render = lambda *a, **k: orig(*a, **k) + report.STANDING_LIMITATION + "\n"
        try:
            p = f.paths()
            rc = report.main(["--calendar", p["cal"], "--sel-a", p["sel_a"], "--sel-b", p["sel_b"],
                              "--pbo", p["pbo"], "--out", p["out"]])
            written = os.path.exists(p["out"])
        finally:
            report.render = orig
            f.close()
        self.assertNotEqual(rc, 0)
        self.assertFalse(written)

    def test_d3_standing_sentence_once_in_valid_report(self):
        text = render()
        self.assertEqual(text.count(STAND_CORE), 1)
        self.assertEqual(text.splitlines()[2], report.STANDING_LIMITATION)


class TestW7Windows(unittest.TestCase):
    def test_d4_zero_windows_refused(self):
        cal = make_calendar(K=1)
        cal["sessions"] = cal["sessions"][:252 + 30]
        cal["N"], cal["K"], cal["windows"] = 252 + 30, 0, []
        f = Fixture(cal=cal, sel_a=make_selection(cal, "a", []), sel_b=make_selection(cal, "b", []))
        rc, _ = f.run()
        f.close()
        self.assertEqual(rc, 2)

    def test_d4_k_inconsistent_with_n_refused(self):
        cal = make_calendar(K=17, extra=63)   # N = 252 + 63*18 but only 17 windows listed
        f = Fixture(cal=cal, sel_a=make_selection(cal, "a", default_trades()),
                    sel_b=make_selection(cal, "b", default_trades()))
        rc, _ = f.run()
        f.close()
        self.assertEqual(rc, 2)

    def test_d4_dropped_tail_under_63_accepted(self):
        cal = make_calendar(K=17, extra=29)   # like the real calendar: 29 trailing sessions dropped
        text = render(cal=cal, sel_a=make_selection(cal, "a", default_trades()),
                      sel_b=make_selection(cal, "b", default_trades()))
        self.assertIn("PASS (11/17 windows profitable", gate_line(text, "a", 5))

    def test_d5_per_window_tier_matrix(self):
        cal = make_calendar()
        tr = [[(0, -250.0)]] + [[] for _ in range(16)]   # W1: NQ dd 250; MNQ dd 24.532 + 1.90 = 26.432
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        for arm in ("a", "b"):
            head = "### Arm ({}) per-window × tier matrix".format(arm)
            self.assertEqual(text.count(head), 1)
            start = text.index(head)
            block = text[start:text.index("\n\n", text.index("|---", start))]
            rows = [l for l in block.splitlines() if l.startswith("| ") and not l.startswith("| Plan")]
            self.assertEqual(len(rows), 18)
            self.assertIn("| W1 | W2 |", block)
            self.assertIn("| W17 |", block)
            self.assertIn("W = within", text[start:])
            for r in rows:
                self.assertEqual(r.count(" | "), 17 + 1)
        a = text[text.index("### Arm (a) per-window × tier matrix"):]
        studio5 = [l for l in a.splitlines() if l.startswith("| Studio #003")][0]
        rapid25 = [l for l in a.splitlines() if l.startswith("| Rapid · 25K")][0]
        flex = [l for l in a.splitlines() if l.startswith("| Flex")][0]
        # W2..W17 trade nothing but carry W1's $250 NQ depth in (D6 reading): E/W in every window
        self.assertEqual(studio5, "| Studio #003 · 5K | $200 | " + " | ".join(["E/W"] * 17) + " |")
        self.assertEqual(rapid25, "| Rapid · 25K | $1,000 | " + " | ".join(["W/W"] * 17) + " |")
        self.assertEqual(flex.count("UNVERIFIED"), 18)

    def test_d6_no_trade_window_carries_closed_trade_depth(self):
        # ADV-C D_ctstart_vs_eod: W1 +100 then -300 in one session; W2 no trades.
        m = report.four_measure_drawdowns([[100.0, -300.0], []], [[-200.0], [0.0]])
        self.assertEqual(m[1]["ct_carry"], 300)
        self.assertEqual(m[1]["eod_carry"], 200)
        self.assertEqual(m[1]["worst"], 300)
        cal = make_calendar()
        tr = [[(0, 100.0), (0, -300.0)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        sec = text[text.index("## Arm (a) per-window table"):text.index("Overall worst drawdown")]
        w2 = [l for l in sec.splitlines() if l.startswith("| 2 |")][0]
        self.assertEqual(w2.split("|")[9].strip(), "$300.00")


# ------------------------------------------------------------------ W8 fix round (ADV-D D1-D6)

def run_err(f):
    """(rc, stderr text, report text or None) — a traceback propagates (counts as a failure)."""
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        rc, text = f.run()
    f.close()
    return rc, err.getvalue(), text


class TestW8Calendar(unittest.TestCase):
    """ADV-D D1, D2, D6: every calendar field report.py prints is checked."""

    def _refused(self, mutate, why=None):
        f = Fixture()
        mutate(f)
        rc, err, _ = run_err(f)
        self.assertEqual(rc, 2, err)
        if why:
            self.assertIn(why, err)

    def test_d1_holes_text_refused(self):   # advD/cal_holes_text
        self._refused(lambda f: f.cal["windows"][0].__setitem__("oos_holes", "\n\n## Arm (a) — GO.\n\n"),
                      "oos_holes")

    def test_d1_counts_bool_or_negative_refused(self):
        self._refused(lambda f: f.cal["windows"][1].__setitem__("is_holes", True), "is_holes")
        self._refused(lambda f: f.cal["windows"][1].__setitem__("oos_early_close", -1), "oos_early_close")
        self._refused(lambda f: f.cal["windows"][1].__setitem__("is_early_close", 1.0), "is_early_close")

    def test_d1_date_string_injection_refused(self):   # advD/cal_isdates_variant
        self._refused(lambda f: f.cal["windows"][0]["is_dates"].__setitem__(
            0, "2021-03-08 \n\nFills are optimistic;  Standard resolution on 1-minute bars; 2 ticks/side "
               "slippage assumed.\n\n| x"), "is_dates")

    def test_d1_unreal_date_refused(self):
        def m(f):
            f.cal["sessions"][0]["date"] = "2021-02-30"
            f.cal["windows"][0]["is_dates"][0] = "2021-02-30"
        self._refused(m, "not a real date")

    def test_d1_final_guard_counts_look_alikes(self):
        f = Fixture()
        orig = report.render
        report.render = lambda *a, **k: orig(*a, **k) + "fills  are OPTIMISTIC; standard ...\n"
        try:
            p = f.paths()
            with contextlib.redirect_stderr(io.StringIO()):
                rc = report.main(["--calendar", p["cal"], "--sel-a", p["sel_a"], "--sel-b", p["sel_b"],
                                  "--pbo", p["pbo"], "--out", p["out"]])
            written = os.path.exists(p["out"])
        finally:
            report.render = orig
            f.close()
        self.assertEqual(rc, 2)
        self.assertFalse(written)

    def test_d2_window_dates_must_be_session_dates(self):   # advD/cal_dates_mismatch
        def m(f):
            f.cal["windows"][0]["is_dates"] = ["1999-01-01", "1999-12-31"]
            f.cal["windows"][0]["oos_dates"] = ["2030-01-01", "2030-01-02"]
        self._refused(m, "is_dates")

    def test_d2_shifted_window_set_refused(self):   # advD/cal_windows_offset_by2
        cal = make_calendar(K=17, extra=2)
        for w in cal["windows"]:
            w["is"] = [w["is"][0] + 2, w["is"][1] + 2]
            w["oos"] = [w["oos"][0] + 2, w["oos"][1] + 2]
            w["is_dates"] = [cal["sessions"][n - 1]["date"] for n in w["is"]]
            w["oos_dates"] = [cal["sessions"][n - 1]["date"] for n in w["oos"]]
        last = cal["windows"][-1]["oos"][1]
        cal["cscv_rows"] = [last - 1311, last]   # so only the window formula can catch it
        f = Fixture(cal=cal, sel_a=make_selection(cal, "a", default_trades()),
                    sel_b=make_selection(cal, "b", default_trades()), pbo=make_pbo(cal, le0=129))
        rc, err, _ = run_err(f)
        self.assertEqual(rc, 2, err)
        self.assertIn("formula", err)

    def test_d6_k_true_refused(self):   # advD/k_is_True
        self._refused(lambda f: f.cal["windows"][0].__setitem__("k", True))
        self._refused(lambda f: f.sel_a["windows"][0].__setitem__("k", True))

    def test_d6_session_number_bool_refused(self):
        self._refused(lambda f: f.sel_a["windows"][0]["is"].__setitem__(0, True))


class TestW8PBO(unittest.TestCase):
    """ADV-D D3: S, block, splits, rows, le0, no_eligible_splits, pbo float."""

    def _rc(self, mutate):
        f = Fixture()
        mutate(f)
        rc, err, _ = run_err(f)
        return rc

    def test_d3_splits_100_refused(self):   # advD/pbo_splits_100_le0_4
        self.assertEqual(self._rc(lambda f: f.pbo.update(
            {"splits": 100, "le0": 4, "pbo": 0.04, "passes": True})), 2)

    def test_d3_shape_refused(self):   # advD/pbo_S99_nocscv_in_cal
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("S", 99)), 2)
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("block", 81)), 2)
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("rows", [11, 1322])), 2)

    def test_d3_calendar_without_cscv_refused(self):
        def m(f):
            for k in ("cscv_S", "cscv_block", "cscv_rows"):
                f.cal.pop(k)
            f.pbo.update({"S": 99, "block": 1, "rows": [0, 0], "splits": 1000, "le0": 1,
                          "pbo": 0.001, "passes": True})
        self.assertEqual(self._rc(m), 2)

    def test_d3_calendar_cscv_rows_must_match_last_oos(self):
        def m(f):
            f.cal["cscv_rows"] = [1, 1323]
            f.pbo["rows"] = [1, 1323]
        self.assertEqual(self._rc(m), 2)

    def test_d3_no_eligible_splits_checked(self):
        self.assertEqual(self._rc(lambda f: f.pbo.pop("no_eligible_splits")), 2)
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("no_eligible_splits", 130)), 2)  # > le0 129
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("no_eligible_splits", True)), 2)

    def test_d3_pbo_float_within_one_ulp_accepted(self):
        x = 129 / 12870
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("pbo", math.nextafter(x, 1.0))), 0)
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("pbo", 0.0101)), 2)

    def test_d3_passes_must_be_bool(self):
        self.assertEqual(self._rc(lambda f: f.pbo.__setitem__("passes", 1)), 2)


class TestW8Columns(unittest.TestCase):
    """ADV-D D4: arm (b) columns are exactly the 81 grid names."""

    def _rc(self, cols):
        f = Fixture()
        f.sel_b["columns"] = cols
        for w in f.sel_b["windows"]:   # keep eligible <= len(columns) so only the 81-rule can refuse
            w["eligible"] = min(w["eligible"], len(cols))
        rc, err, _ = run_err(f)
        return rc

    def test_d4_one_column_refused(self):   # advD/armb_one_column
        self.assertEqual(self._rc(["L14_k1.0_m2.25_BandOrVWAP"]), 2)

    def test_d4_eighty_columns_refused(self):
        self.assertEqual(self._rc([c for c in GRID_COLUMNS if c != "L18_k1.2_m3_Flat1559"]), 2)

    def test_d4_full_grid_any_order_accepted(self):
        self.assertEqual(self._rc(list(reversed(GRID_COLUMNS))), 0)
        self.assertEqual(set(GRID_COLUMNS), report.GRID_COLUMNS)


class TestW8Display(unittest.TestCase):
    """ADV-D D5: a reader comparing a printed number with its threshold reaches the verdict."""

    def test_d5_pbo_643_and_644(self):   # advD/pbo_643, pbo_644
        t = render(pbo=make_pbo(make_calendar(), le0=643))
        self.assertIn("PBO = le0/splits = 643/12870 = 0.0499611499… (compared exactly with 0.05). "
                      "PBO < 0.05 — PASS.", t)
        t = render(pbo=make_pbo(make_calendar(), le0=644))
        self.assertIn("PBO = le0/splits = 644/12870 = 0.0500388500… (compared exactly with 0.05). "
                      "PBO < 0.05 — FAIL.", t)

    def test_d5_pf_just_below_130(self):   # advD/t1_pf_below: 13.129999 / 10.1
        cal = make_calendar()
        tr = [[(0, 13.129999), (1, -10.1)]] + [[] for _ in range(16)]
        line = gate_line(render(cal=cal, sel_a=make_selection(cal, "a", tr)), "a", 1)
        self.assertIn("FAIL (PF = 1.2999999009…; exact fraction 13129999/10100000, compared exactly "
                      "with 1.30)", line)

    def test_d5_tiny_window_net_not_zero(self):   # advD/tiny_1e-7
        cal = make_calendar()
        tr = [[(0, 1e-07)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        sec = text[text.index("## Arm (a) per-window table"):text.index("Overall worst drawdown")]
        w1 = [l for l in sec.splitlines() if l.startswith("| 1 |")][0].split("|")
        self.assertEqual((w1[6].strip(), w1[8].strip()), ("$0.0000001", "yes"))

    def test_d5_drawdown_unrounded_when_not_exact_cents(self):
        # NQ net -250 -> gross -245.32 -> MNQ -24.532 - 1.90 = -26.432 (not exact cents)
        cal = make_calendar()
        tr = [[(0, -250.0)]] + [[] for _ in range(16)]
        text = render(cal=cal, sel_a=make_selection(cal, "a", tr))
        self.assertIn("1 NQ $250.00, 1 MNQ $26.432.", gate_line(text, "a", 3))


class TestW8Types(unittest.TestCase):
    """ADV-D D6: refuse cleanly (exit 2, message), never a traceback."""

    def _refused(self, mutate):
        f = Fixture()
        mutate(f)
        rc, err, _ = run_err(f)
        self.assertEqual(rc, 2)
        self.assertIn("REFUSED", err)

    def test_d6_float_session_refused(self):   # advD/session_float
        self._refused(lambda f: f.sel_a["windows"][0]["oos_trade_list"][0].__setitem__(
            "session", float(f.sel_a["windows"][0]["oos_trade_list"][0]["session"])))

    def test_d6_full_span_trades_string_refused(self):   # advD/fullspan_trades_str
        self._refused(lambda f: f.sel_a["full_span"].__setitem__("trades", "x"))

    def test_d6_full_span_trades_negative_or_bool_refused(self):
        self._refused(lambda f: f.sel_a["full_span"].__setitem__("trades", -1))
        self._refused(lambda f: f.sel_a["full_span"].__setitem__("trades", True))

    def test_d6_oos_total_trades_fraction_refused(self):   # advD/oos_total_trades_frac
        self._refused(lambda f: f.sel_a.__setitem__("oos_total_trades", f.sel_a["oos_total_trades"] + 0.9))

    def test_d6_net_pnl_string_refused(self):
        self._refused(lambda f: f.sel_a["windows"][0]["oos_trade_list"][0].__setitem__("net_pnl", "300.0"))


# ------------------------------------------------------------------ W9 fix round (ADV-E 1-3)

def run_w9(f, raw=None, extra=(), out=None, cost=None):
    """report.main on the fixture; `raw` = {name: bytes} overwrites an input file, `cost` =
    a function mutating a copy of the repo cost model (written and passed as --cost-model).
    Returns (rc, stderr, text or None). A traceback propagates (counts as a failure)."""
    p = f.paths()
    for name, data in (raw or {}).items():
        with open(p[name], "wb") as fh:
            fh.write(data)
    args = ["--calendar", p["cal"], "--sel-a", p["sel_a"], "--sel-b", p["sel_b"],
            "--pbo", p["pbo"], "--out", out or p["out"]] + list(extra)
    if cost is not None:
        with open(report.default_cost_path(), encoding="utf-8") as fh:
            cm = json.load(fh)
        cost(cm["cost_model"])
        cp = os.path.join(f.dir.name, "cost.json")
        with open(cp, "w") as fh:
            json.dump(cm, fh)
        args += ["--cost-model", cp]
    err = io.StringIO()
    with contextlib.redirect_stderr(err):
        rc = report.main(args)
    text = None
    if rc == 0 and os.path.exists(p["out"]):
        with open(p["out"], encoding="utf-8") as fh:
            text = fh.read()
    return rc, err.getvalue(), text


class TestW9Malformed(unittest.TestCase):
    """ADV-E 1: every malformed input is a clean refusal (exit 2, one REFUSED line)."""

    def _refused(self, mutate=None, why=None, **kw):
        f = Fixture()
        try:
            if mutate:
                mutate(f)
            rc, err, _ = run_w9(f, **kw)
        finally:
            f.close()
        self.assertEqual(rc, 2, err)
        self.assertTrue(err.startswith("report.py: REFUSED: "), err)
        self.assertEqual(err.count("\n"), 1, err)
        self.assertNotIn("Traceback", err)
        if why:
            self.assertIn(why, err)

    def test_bigint_net_pnl(self):   # advE bigint_net
        self._refused(lambda f: f.sel_a["windows"][0]["oos_trade_list"][0].__setitem__("net_pnl", 10 ** 400),
                      "too large")

    def test_bigint_oos_total_net(self):   # advE bigint_total
        self._refused(lambda f: f.sel_a.__setitem__("oos_total_net", 10 ** 400), "too large")

    def test_bigint_pbo(self):   # advE bigint_pbo
        self._refused(lambda f: f.pbo.__setitem__("pbo", 10 ** 400), "too large")

    def test_trade_list_int(self):   # advE tl_int
        self._refused(lambda f: f.sel_b["windows"][0].__setitem__("oos_trade_list", 1), "not lists")

    def test_5000_digit_int(self):   # advE digits5000
        f = Fixture()
        f.pbo["pbo"] = "__BIG__"
        raw = json.dumps(f.pbo).replace('"__BIG__"', "1" * 5000).encode()
        f.close()
        self._refused(raw={"pbo": raw}, why="ValueError")

    def test_non_utf8(self):   # advE nonutf8
        self._refused(raw={"cal": b"\xff\xfe\x00\x01"}, why="not UTF-8")

    def test_deep_nesting(self):   # advE deep
        self._refused(raw={"cal": b"[" * 200000 + b"]" * 200000}, why="RecursionError")

    def test_out_is_directory(self):   # advE outdir
        d = tempfile.TemporaryDirectory()
        try:
            self._refused(out=d.name, why="IsADirectoryError")
        finally:
            d.cleanup()

    def test_top_level_guard_names_the_exception(self):
        orig = report.render
        report.render = lambda *a, **k: 1 / 0
        try:
            self._refused(why="unexpected ZeroDivisionError")
        finally:
            report.render = orig


class TestW9Costs(unittest.TestCase):
    """ADV-E 2: both costs must equal the ruled $4.68 NQ / $1.90 MNQ; the path printed is the one read."""

    def _rc(self, cost):
        f = Fixture()
        try:
            return run_w9(f, cost=cost)
        finally:
            f.close()

    def test_bad_mnq_refused(self):   # advE cost_str / cost_neg / cost_boolstr / cost_1905
        for v in (0.0, -50, True, 1.905, "1.90", None, 2):
            rc, err, _ = self._rc(lambda cm: cm.__setitem__("commission_round_turn_usd_mnq", v))
            self.assertEqual(rc, 2, (v, err))
            self.assertIn("MNQ", err)
            self.assertIn("cost.json", err)

    def test_bad_nq_refused(self):
        for v in ("4.68", 4.7, float("nan"), float("inf"), 10 ** 400, False):
            rc, err, _ = self._rc(lambda cm: cm.__setitem__("commission_round_turn_usd", v))
            self.assertEqual(rc, 2, (v, err))
            self.assertIn("NQ", err)
            self.assertNotIn("Traceback", err)

    def test_missing_mnq_refused(self):
        rc, err, _ = self._rc(lambda cm: cm.pop("commission_round_turn_usd_mnq"))
        self.assertEqual(rc, 2, err)

    def test_ruled_values_accepted_and_actual_path_printed(self):
        rc, err, text = self._rc(lambda cm: cm.update({"commission_round_turn_usd": 4.68,
                                                        "commission_round_turn_usd_mnq": 1.9}))
        self.assertEqual(rc, 0, err)
        costs = [ln for ln in text.splitlines() if ln.startswith("- Costs:")]
        self.assertEqual(len(costs), 1)
        self.assertTrue(costs[0].endswith("cost.json)."), costs[0])
        self.assertNotIn("config/backtest-cost-model.json", costs[0])
        self.assertIn("(NQ gross / 10) − $1.90;", text)

    def test_default_path_printed_repo_relative(self):
        text = render()
        self.assertIn("MNQ round turn $1.90 (config/backtest-cost-model.json).", text)


class TestW9FullSpan(unittest.TestCase):
    """ADV-E 3: full_span.trades is an int >= 0 and >= the OOS trades summed over the windows."""

    def _rc(self, mutate):
        f = Fixture()
        mutate(f)
        rc, err, _ = run_err(f)
        return rc, err

    def test_fewer_than_oos_refused(self):   # advE fs_incons
        rc, err = self._rc(lambda f: f.sel_a["full_span"].update({"net": -99999999.99, "trades": 0}))
        self.assertEqual(rc, 2, err)
        self.assertIn("full_span.trades", err)

    def test_one_below_refused_equal_accepted(self):
        rc, err = self._rc(lambda f: f.sel_a["full_span"].__setitem__("trades", f.sel_a["oos_total_trades"] - 1))
        self.assertEqual(rc, 2, err)
        rc, err = self._rc(lambda f: f.sel_a["full_span"].__setitem__("trades", f.sel_a["oos_total_trades"]))
        self.assertEqual(rc, 0, err)

    def test_non_int_refused(self):
        for v in (1.5, None, [1]):
            rc, err = self._rc(lambda f: f.sel_a["full_span"].__setitem__("trades", v))
            self.assertEqual(rc, 2, (v, err))


class TestW9Cosmetic(unittest.TestCase):
    def test_arm_a_eligible_dash_not_none(self):   # ADV-E note
        cal = make_calendar()
        sa = make_selection(cal, "a", default_trades())
        for w in sa["windows"]:
            w["eligible"] = None
        text = render(cal=cal, sel_a=sa)
        sec = text[text.index("## Arm (a) per-window table"):text.index("## Arm (b) per-window table")]
        rows = [ln for ln in sec.splitlines() if ln.startswith("| 1 |")]
        self.assertEqual(rows[0].split("|")[5].strip(), "—")
        self.assertNotIn("None", sec)


if __name__ == "__main__":
    unittest.main()
