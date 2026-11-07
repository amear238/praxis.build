"""Tests for scripts/wf/tradelist.py (synthetic fixtures only). Run with python3 -I."""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tradelist as T  # noqa: E402

# Mon 2021-03-08 .. Fri 2021-03-12, Mon 2021-03-15; weekend 03-13/14 absent.
DATES = ["2021-03-08", "2021-03-09", "2021-03-10", "2021-03-11", "2021-03-12", "2021-03-15"]
ARMB = {"Lookback": 14, "NoiseMult": 1.0, "StopAtrMult": 2.25, "ExitPolicy": "BandOrVWAP", "Contracts": 1}


def trade(entry, exit_, pnl, side="Long", name="Exit on session close"):
    return {"pnl": pnl, "marketPosition": side, "entryTime": entry + ".0000000",
            "exitTime": exit_ + ".0000000", "entryPrice": 13000.25, "exitPrice": 13010.5, "exitName": name}


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(prefix="wf-tl-")
        cal = {"schema": "praxis-wf-calendar/1", "source": {"path": "x", "bytes": 0, "sha256": "0"},
               "rule": {}, "N": len(DATES),
               "sessions": [{"n": i + 1, "date": d, "first_bar": "09:31", "last_bar": "16:00",
                             "early_close_in_file": False, "nt8_last_bar": "16:00",
                             "nt8_last_bar_grade": "test"} for i, d in enumerate(DATES)],
               "windows": [], "K": 0, "oos_sessions": 0, "dropped": [], "dropped_dates": [],
               "cscv_rows": [], "cscv_S": 16, "cscv_block": 82, "weekend_dates_dropped": 0}
        self.cal = self.w("cal.json", cal)
        self.cost = self.w("cost.json", {"cost_model": {"commission_round_turn_usd": 4.68}})
        self.out = os.path.join(self.d, "daily.json")

    def tearDown(self):
        shutil.rmtree(self.d)

    def w(self, name, obj):
        p = os.path.join(self.d, name)
        with open(p, "w", encoding="utf-8") as f:
            if isinstance(obj, str):
                f.write(obj)
            else:
                json.dump(obj, f)
        return p

    def bridge(self, name, trades, net=None, total=None, status="ok", **extra):
        doc = {"id": name, "status": status, "strategy": "PraxisNoiseAreaBreakout",
               "metrics": {"totalTrades": len(trades) if total is None else total, "profitFactor": 1.1,
                           "netProfit": round(sum(t["pnl"] for t in trades), 6) if net is None else net,
                           "maxDrawdown": -10.0},
               "trades": trades}
        doc.update(extra)
        return self.w(name, doc)

    def run_main(self, argv):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            rc = T.main(argv)
        return rc, err.getvalue()

    def ok(self, files, basis="gross", arm=None, flag="--bridge", extra=()):
        arm = ["--arm-a"] if arm is None else ["--params-json", json.dumps(arm)]
        rc, err = self.run_main(["--calendar", self.cal, "--pnl-basis", basis, flag] + list(files) + arm
                                + ["--cost-model", self.cost, "--out", self.out] + list(extra))
        self.assertEqual(rc, 0, err)
        return T.load_daily(self.out)

    def fails(self, files, basis="gross", arm=None, flag="--bridge", extra=()):
        arm = ["--arm-a"] if arm is None else ["--params-json", json.dumps(arm)]
        rc, err = self.run_main(["--calendar", self.cal, "--pnl-basis", basis, flag] + list(files) + arm
                                + ["--cost-model", self.cost, "--out", self.out] + list(extra))
        self.assertEqual(rc, 1, err)
        self.assertFalse(os.path.exists(self.out))
        return err


class TestPnlBasis(Base):
    def test_gross_subtracts_4_68_exactly(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:01:00", "2021-03-08T16:00:00", 100.0),
                                   trade("2021-03-09T10:31:00", "2021-03-09T11:00:00", -50.5, "Short")])
        s = self.ok([f], "gross")
        self.assertEqual(s["pnl_basis_in"], "gross")
        self.assertEqual(s["commission_rt_usd"], 4.68)
        self.assertEqual([t["net_pnl"] for t in s["trades"]], [95.32, -55.18])
        self.assertEqual([t["gross_pnl"] for t in s["trades"]], [100.0, -50.5])
        self.assertEqual(s["daily_net"], [95.32, -55.18, 0.0, 0.0, 0.0, 0.0])

    def test_net_adds_back_for_gross(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:01:00", "2021-03-08T16:00:00", 95.32)])
        s = self.ok([f], "net")
        self.assertEqual(s["trades"][0]["net_pnl"], 95.32)
        self.assertEqual(s["trades"][0]["gross_pnl"], 100.0)
        self.assertEqual(s["daily_net"][0], 95.32)

    def test_missing_pnl_basis_is_argparse_error(self):
        f = self.bridge("b.json", [])
        err = io.StringIO()
        with contextlib.redirect_stderr(err), self.assertRaises(SystemExit) as cm:
            T.main(["--calendar", self.cal, "--bridge", f, "--arm-a", "--out", self.out])
        self.assertEqual(cm.exception.code, 2)
        self.assertIn("--pnl-basis", err.getvalue())

    def test_cost_model_without_commission_fails(self):
        f = self.bridge("b.json", [])
        self.cost = self.w("cost2.json", {"cost_model": {}})
        self.assertIn("commission_round_turn_usd", self.fails([f]))


class TestKeying(Base):
    def test_exit_date_keying_two_in_one_session_and_zero_session(self):
        f = self.bridge("b.json", [
            trade("2021-03-08T10:01:00", "2021-03-09T10:30:00", 10.0),   # cross-session
            trade("2021-03-09T11:00:00", "2021-03-09T15:59:00", 20.0),
            trade("2021-03-11T10:00:00", "2021-03-11T16:00:00", -5.0, "Short"),
            trade("2021-03-15T10:00:00", "2021-03-15T12:00:00", 1.0)])
        s = self.ok([f], "net")
        self.assertEqual(s["daily_trades"], [0, 2, 0, 1, 0, 1])
        self.assertEqual(s["daily_net"], [0.0, 30.0, 0.0, -5.0, 0.0, 1.0])
        self.assertEqual(s["cross_session_trades"], 1)
        self.assertEqual([t["session"] for t in s["trades"]], [2, 2, 4, 6])
        self.assertEqual(s["N"], 6)
        self.assertEqual(s["n_trades"], 4)
        self.assertEqual(s["trades"][0]["exit_time"], "2021-03-09T10:30:00")

    def test_weekend_exit_fails_listing_offender(self):
        f = self.bridge("b.json", [trade("2021-03-12T10:00:00", "2021-03-13T10:00:00", 1.0),
                                   trade("2021-03-15T10:00:00", "2021-03-15T11:00:00", 1.0)])
        err = self.fails([f])
        self.assertIn("not a calendar session", err)
        self.assertIn("2021-03-13T10:00:00", err)

    def test_out_of_range_exit_fails(self):
        f = self.bridge("b.json", [trade("2021-03-15T10:00:00", "2021-03-16T10:00:00", 1.0)])
        self.assertIn("2021-03-16", self.fails([f]))

    def test_bad_market_position_fails(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0, "Flat")])
        self.assertIn("'Flat'", self.fails([f]))

    def test_unknown_status_fails_and_override(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0)], status="done")
        self.assertIn("'done'", self.fails([f]))
        self.ok([f], extra=["--accept-status", "done"])


class TestTruncationAndConsistency(Base):
    def many(self, n, **kw):
        ts = [trade("2021-03-10T10:00:00", "2021-03-10T11:00:00", 1.0) for _ in range(n)]
        return self.bridge("m%d.json" % n, ts, **kw)

    def test_exactly_5000_is_truncated(self):
        s = self.ok([self.many(5000, total=5000)])
        self.assertTrue(s["truncated"])
        self.assertEqual(s["n_trades"], 5000)

    def test_4999_not_truncated(self):
        s = self.ok([self.many(4999)])
        self.assertFalse(s["truncated"])
        self.assertEqual(s["daily_trades"][2], 4999)

    def test_total_trades_above_list_is_truncated(self):
        s = self.ok([self.many(10, total=12, net=999.0)])   # consistency check skipped when truncated
        self.assertTrue(s["truncated"])

    def test_total_trades_below_list_fails(self):
        self.assertIn("totalTrades=9", self.fails([self.many(10, total=9)]))

    def test_sum_vs_netprofit_mismatch_fails_with_both_numbers(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 10.0),
                                   trade("2021-03-09T10:00:00", "2021-03-09T11:00:00", 5.0)], net=15.02)
        err = self.fails([f])
        self.assertIn("15.0", err)
        self.assertIn("15.02", err)

    def test_sum_within_one_cent_passes(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 10.0)], net=10.01)
        self.ok([f])


class TestSplit(Base):
    def test_date_split_concatenates(self):
        a = self.bridge("a.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0)])
        b = self.bridge("b.json", [trade("2021-03-11T10:00:00", "2021-03-11T11:00:00", 2.0)])
        s = self.ok([b, a], "net", arm=ARMB)   # order of files does not matter
        self.assertEqual(s["column"], "L14_k1.0_m2.25_BandOrVWAP")
        self.assertEqual(s["params"], ARMB)
        self.assertEqual(s["daily_net"], [1.0, 0.0, 0.0, 2.0, 0.0, 0.0])
        self.assertEqual(len(s["sources"]), 2)
        self.assertEqual(s["sources"][0]["n_trades"], 1)
        self.assertEqual(len(s["sources"][0]["sha256"]), 64)

    def test_overlap_fails(self):
        a = self.bridge("a.json", [trade("2021-03-08T10:00:00", "2021-03-10T11:00:00", 1.0)])
        b = self.bridge("b.json", [trade("2021-03-09T10:00:00", "2021-03-09T11:00:00", 2.0)])
        self.assertIn("overlap", self.fails([a, b]))

    def test_differing_embedded_params_fail(self):
        p2 = dict(ARMB, Lookback=18)
        a = self.bridge("a.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0)], params=ARMB)
        b = self.bridge("b.json", [trade("2021-03-11T10:00:00", "2021-03-11T11:00:00", 2.0)], params=p2)
        self.assertIn("params differ", self.fails([a, b], arm=ARMB))

    def test_same_file_twice_fails(self):
        a = self.bridge("a.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0)])
        self.assertIn("twice", self.fails([a, a]))


class TestParams(Base):
    def test_contracts_2_not_settled(self):
        f = self.bridge("b.json", [])
        self.assertIn("NotSettledBySpec", self.fails([f], arm=dict(ARMB, Contracts=2)))

    def test_params_off_grid_fail(self):
        f = self.bridge("b.json", [])
        self.assertIn("not one of the 81", self.fails([f], arm=dict(ARMB, StopAtrMult=2.0)))

    def test_params_missing_key_fail(self):
        f = self.bridge("b.json", [])
        p = dict(ARMB)
        del p["Contracts"]
        self.assertIn("Contracts", self.fails([f], arm=p))

    def test_exit_policy_number_fails(self):
        f = self.bridge("b.json", [])
        self.assertIn("BY NAME", self.fails([f], arm=dict(ARMB, ExitPolicy=0)))


class TestGrid(unittest.TestCase):
    def test_grid(self):
        self.assertEqual(len(T.GRID), 81)
        self.assertEqual(len({T.column_name(g) for g in T.GRID}), 81)
        self.assertEqual(T.GRID[0], {"Lookback": 10, "NoiseMult": 0.8, "StopAtrMult": 1.5,
                                     "ExitPolicy": "BandOrVWAP", "Contracts": 1})
        self.assertEqual(T.GRID[1]["ExitPolicy"], "OppBand")
        self.assertEqual(T.GRID[2]["ExitPolicy"], "Flat1559")
        self.assertEqual(T.GRID[3]["StopAtrMult"], 2.25)
        self.assertEqual(T.GRID[-1], {"Lookback": 18, "NoiseMult": 1.2, "StopAtrMult": 3.0,
                                      "ExitPolicy": "Flat1559", "Contracts": 1})
        self.assertEqual(T.column_name(T.GRID[0]), "L10_k0.8_m1.5_BandOrVWAP")
        self.assertEqual(T.column_name(T.GRID[-1]), "L18_k1.2_m3_Flat1559")
        self.assertEqual(T.column_name(ARMB), "L14_k1.0_m2.25_BandOrVWAP")
        self.assertEqual(T.column_name(None), "armA")


class TestTime(unittest.TestCase):
    def test_seven_digit_fraction(self):
        self.assertEqual(T.parse_nt_time("2021-03-29T10:01:00.0000000"), datetime(2021, 3, 29, 10, 1))
        self.assertEqual(T.parse_nt_time("2021-03-29T10:01:00.1234560"), datetime(2021, 3, 29, 10, 1, 0, 123456))
        self.assertEqual(T.parse_nt_time("2021-03-29T10:01:00"), datetime(2021, 3, 29, 10, 1))

    def test_rejects_offset_empty_and_sub_microsecond(self):
        for bad in ("2021-03-29T10:01:00.0000000-04:00", "2021-03-29T10:01:00Z", "",
                    "2021-03-29T10:01:00.1234567", "2021-02-30T10:01:00"):
            with self.assertRaises(T.TradelistError, msg=bad):
                T.parse_nt_time(bad)


class TestNt8Csv(Base):
    def csv(self, name, header, rows):
        lines = [",".join(header)] + [",".join(r) for r in rows]
        return self.w(name, "\n".join(lines) + "\n")

    def row(self, qty="1", profit="$100.00", pos="Long"):
        return ["1", "NQ 06-21", "Sim101", "PraxisNoiseAreaBreakout", pos, qty, "13000.25", "13005.25",
                "3/9/2021 10:01:00 AM", "3/9/2021 4:00:00 PM", "Entry", "Exit on session close",
                '"' + profit + '"', '"$100.00"', '"$4.68"', '"$10.00"', '"$20.00"', '"$5.00"', "359"]

    def test_expected_header_parses(self):
        f = self.csv("t.csv", T.EXPECTED_NT8_COLUMNS, [self.row(), self.row(profit="($5.00)", pos="Short")])
        s = self.ok([f], "gross", flag="--nt8-csv")
        self.assertEqual([t["net_pnl"] for t in s["trades"]], [95.32, -9.68])
        self.assertEqual(s["trades"][0]["exit_time"], "2021-03-09T16:00:00")
        self.assertEqual(s["daily_trades"], [0, 2, 0, 0, 0, 0])
        self.assertIsNone(s["sources"][0]["metrics"])
        self.assertFalse(s["truncated"])

    def test_wrong_header_fails_with_diff(self):
        h = list(T.EXPECTED_NT8_COLUMNS)
        h[12] = "Net profit"
        f = self.csv("t.csv", h, [self.row()])
        err = self.fails([f], flag="--nt8-csv")
        self.assertIn("header mismatch", err)
        self.assertIn("'Profit'", err)
        self.assertIn("'Net profit'", err)

    def test_qty_2_refused(self):
        f = self.csv("t.csv", T.EXPECTED_NT8_COLUMNS, [self.row(qty="2")])
        self.assertIn("NotSettledBySpec", self.fails([f], flag="--nt8-csv"))


class TestOutput(Base):
    def test_deterministic_and_schema(self):
        f = self.bridge("b.json", [trade("2021-03-08T10:00:00", "2021-03-08T11:00:00", 1.0)])
        self.ok([f])
        with open(self.out, "rb") as fh:
            first = fh.read()
        s = self.ok([f])
        with open(self.out, "rb") as fh:
            self.assertEqual(fh.read(), first)
        self.assertEqual(s["schema"], "praxis-wf-daily/1")
        self.assertIsNone(s["params"])
        self.assertEqual(s["column"], "armA")
        self.assertEqual(s["contracts"], 1)
        self.assertEqual(set(s["trades"][0]), {"session", "entry_time", "exit_time", "side", "net_pnl",
                                               "gross_pnl", "exit_name"})
        self.assertEqual(set(s["sources"][0]), {"path", "sha256", "n_trades", "metrics"})


if __name__ == "__main__":
    unittest.main()
