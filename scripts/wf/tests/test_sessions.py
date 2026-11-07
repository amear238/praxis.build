"""Tests for scripts/wf/sessions.py (unit 2026-11-07-wf-mac-side-maths, W1)."""
import datetime as dt
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
sys.path.append(WF)
import sessions  # noqa: E402

REAL = "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
SCRIPT = os.path.join(WF, "sessions.py")


def bar(d, t, px=100.0):
    return "%s %s;%s;%s;%s;%s;1\n" % (d, t, px, px + 1, px - 1, px)


class TestBuildWindows(unittest.TestCase):
    def test_n252_k0(self):
        K, w, dropped = sessions.build_windows(252)
        self.assertEqual((K, w, dropped), (0, [], [1, 252]))

    def test_n314_k0(self):
        self.assertEqual(sessions.build_windows(314)[0], 0)

    def test_n315_k1_exact(self):
        K, w, dropped = sessions.build_windows(315)
        self.assertEqual(K, 1)
        self.assertEqual(w, [{"k": 1, "is": [1, 252], "oos": [253, 315]}])
        self.assertIsNone(dropped)

    def test_n377_k1_62_dropped(self):
        K, w, dropped = sessions.build_windows(377)
        self.assertEqual(K, 1)
        self.assertEqual(dropped, [316, 377])
        self.assertEqual(dropped[1] - dropped[0] + 1, 62)

    def test_n378_k2(self):
        K, w, dropped = sessions.build_windows(378)
        self.assertEqual(K, 2)
        self.assertEqual(w[1], {"k": 2, "is": [64, 315], "oos": [316, 378]})
        self.assertIsNone(dropped)

    def test_small_custom(self):
        # IS=4, OOS=2, STEP=2, N=11 -> K=floor((11-4)/2)=3, windows [1-4|5-6],[3-6|7-8],[5-8|9-10], drop 11
        K, w, dropped = sessions.build_windows(11, IS=4, OOS=2, STEP=2)
        self.assertEqual(K, 3)
        self.assertEqual([x["is"] + x["oos"] for x in w], [[1, 4, 5, 6], [3, 6, 7, 8], [5, 8, 9, 10]])
        self.assertEqual(dropped, [11, 11])

    def test_n1352_spec(self):
        K, w, dropped = sessions.build_windows(1352)
        self.assertEqual(K, 17)
        self.assertEqual(dropped, [1324, 1352])
        self.assertEqual(w[-1]["oos"], [1261, 1323])

    def test_too_small_raises(self):
        with self.assertRaises(ValueError):
            sessions.build_windows(251)

    def test_cscv_rows(self):
        self.assertEqual(sessions.cscv_rows(1323), ([12, 1323], 82))
        self.assertEqual(sessions.cscv_rows(32), ([1, 32], 2))


class TestSyntheticFile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "data.txt")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, lines):
        with open(self.path, "w") as fh:
            fh.writelines(lines)

    def test_scan_known_sessions(self):
        lines = [
            bar("20210307", "180100"),            # Sunday evening: not RTH, not weekend-RTH
            bar("20210308", "093000"),            # Mon 09:30:00 - outside window (first is 09:31)
            bar("20210308", "093100"),
            bar("20210308", "160000"),
            bar("20210308", "160100"),            # after 16:00 - ignored
            bar("20210309", "170000"),            # Tue: only out-of-RTH bar -> not a session
            bar("20210310", "100000"),            # Wed early close in file, 13:15 -> 12:15
            bar("20210310", "131500"),
            bar("20210311", "100000"),            # Thu last bar 13:00 -> 12:00
            bar("20210311", "130000"),
            bar("20210312", "093500"),            # Fri first bar 09:35, full day
            bar("20210312", "160000"),
            bar("20210313", "120000"),            # Saturday RTH bar -> weekend dropped
            bar("20210314", "100000"),            # Sunday RTH bar -> weekend dropped
            bar("20210305", "120000"),            # before range -> excluded
            bar("20260720", "120000"),            # after range -> excluded
        ]
        self.write(lines)
        r = sessions.scan_file(self.path)
        S = r["sessions"]
        self.assertEqual([s["date"] for s in S], ["2021-03-08", "2021-03-10", "2021-03-11", "2021-03-12"])
        self.assertEqual([s["n"] for s in S], [1, 2, 3, 4])
        self.assertEqual((S[0]["first_bar"], S[0]["last_bar"], S[0]["early_close_in_file"], S[0]["nt8_last_bar"]),
                         ("09:31", "16:00", False, "16:00"))
        self.assertEqual((S[1]["last_bar"], S[1]["early_close_in_file"], S[1]["nt8_last_bar"]), ("13:15", True, "12:15"))
        self.assertEqual(S[2]["nt8_last_bar"], "12:00")
        self.assertEqual(S[3]["nt8_last_bar"], "16:00")
        self.assertEqual(S[1]["nt8_last_bar_grade"], sessions.GRADE_RULE)
        self.assertEqual(S[2]["nt8_last_bar_grade"], sessions.GRADE_RULE)
        self.assertEqual(S[3]["first_bar"], "09:35")
        self.assertEqual(r["weekend_dates_dropped"], 2)
        self.assertEqual(r["weekend_first"], "2021-03-13")

    def test_malformed_line_reports_line_number(self):
        for bad in ["20210308 100000;1;2;3\n", "2021030 100000;1;2;3;4;5\n", "20210308 100000;1;x;3;4;5\n",
                    "20210230 100000;1;2;3;4;5\n", "20210308 250000;1;2;3;4;5\n", "\n"]:
            self.write([bar("20210308", "100000"), bar("20210308", "100100"), bad])
            with self.assertRaises(sessions.DataError) as cm:
                sessions.scan_file(self.path)
            self.assertIn("line 3", str(cm.exception), bad)

    def _year_file(self, n_weekdays, holidays=(), early=None):
        early = early or {}
        d = dt.date(2021, 3, 8)
        lines, count = [], 0
        while count < n_weekdays:
            if d.weekday() < 5:
                count += 1
                if d.isoformat() not in holidays:
                    ds = d.strftime("%Y%m%d")
                    lines.append(bar(ds, "093100"))
                    lines.append(bar(ds, early.get(d.isoformat(), "160000")))
            else:
                lines.append(bar(d.strftime("%Y%m%d"), "120000"))
            d += dt.timedelta(days=1)
        self.write(lines)

    def test_cli_end_to_end(self):
        # 322 weekdays, 2 holes (2021-03-10, 2021-03-17) -> N=320 -> K=1, dropped s316-s320
        self._year_file(322, holidays={"2021-03-10", "2021-03-17"}, early={"2021-03-11": "131500"})
        out = os.path.join(self.tmp.name, "cal.json")
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out, "--print-table"],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        cal = sessions.load_calendar(out)
        self.assertEqual(set(cal), {"schema", "source", "rule", "N", "sessions", "windows", "K", "oos_sessions",
                                    "dropped", "dropped_dates", "cscv_rows", "cscv_S", "cscv_block",
                                    "weekend_dates_dropped"})
        self.assertEqual(cal["N"], 320)
        self.assertEqual(cal["K"], 1)
        self.assertEqual(cal["oos_sessions"], 63)
        self.assertEqual(cal["dropped"], [316, 320])
        w = cal["windows"][0]
        self.assertEqual(w["is"], [1, 252])
        self.assertEqual(w["is_dates"][0], "2021-03-08")
        self.assertEqual(w["is_holes"], 2)
        self.assertEqual(w["oos_holes"], 0)
        self.assertEqual((w["is_early_close"], w["oos_early_close"]), (1, 0))
        self.assertEqual(cal["cscv_rows"], [12, 315])   # 315 // 16 = 19; 16*19 = 304
        self.assertEqual(cal["cscv_block"], 19)
        self.assertGreater(cal["weekend_dates_dropped"], 0)
        d2s = sessions.date_to_session(cal)
        self.assertEqual(d2s["2021-03-08"], 1)
        self.assertEqual(d2s["2021-03-11"], 3)
        self.assertNotIn("2021-03-10", d2s)
        self.assertIn("early_close_in_file sessions: 1", p.stdout)
        self.assertIn("| 3 | 2021-03-11 | 09:31 | 13:15 | 12:15 |", p.stdout)
        # determinism
        with open(out, "rb") as fh:
            first = fh.read()
        p2 = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out, "--print-table"],
                            capture_output=True, text=True)
        with open(out, "rb") as fh:
            self.assertEqual(fh.read(), first)
        self.assertEqual(p2.stdout, p.stdout)

    def test_cli_fails_loudly(self):
        self.write([bar("20210308", "100000"), "garbage\n"])
        out = os.path.join(self.tmp.name, "cal.json")
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out],
                           capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("line 2", p.stderr)
        self.assertFalse(os.path.exists(out))
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path + ".missing", "--out", out],
                           capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)
        # too few sessions -> K=0 -> error
        self._year_file(10)
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out],
                           capture_output=True, text=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("K=0", p.stderr)


class TestW6EarlyClose(unittest.TestCase):
    """W6 fix round: defects 4-6 (grades, unmapped early close, footnote)."""

    REPORTED = {"2021-11-26": "131500", "2023-04-05": "140300", "2024-07-03": "131500",
                "2024-11-29": "131500", "2024-12-24": "131500", "2025-01-20": "130000",
                "2025-06-19": "130000", "2025-07-03": "131500"}

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "data.txt")

    def tearDown(self):
        self.tmp.cleanup()

    def write_days(self, days):
        with open(self.path, "w") as fh:
            for d, last in sorted(days.items()):
                ds = d.replace("-", "")
                fh.write(bar(ds, "093100"))
                fh.write(bar(ds, last))

    def test_grades_reported_vs_rule(self):
        days = dict(self.REPORTED)
        days.update({"2022-11-25": "131500", "2023-07-03": "130000", "2022-03-14": "160000"})
        self.write_days(days)
        S = {s["date"]: s for s in sessions.scan_file(self.path)["sessions"]}
        rep = "REPORTED BY docs/reports/2026-11-01-three-strategy-results.md:144-151 (OBSERVED there)"
        rule = "INFERRED: mapped by rule from the file's last bar"
        for d in self.REPORTED:
            self.assertTrue(S[d]["nt8_last_bar_grade"].startswith(rep), d)
        for d in ("2022-11-25", "2023-07-03"):
            self.assertEqual(S[d]["nt8_last_bar_grade"], rule, d)
        g = S["2023-04-05"]["nt8_last_bar_grade"]
        self.assertIn("INFERS", g)
        self.assertIn("data gap, not an early close", g)
        for d in self.REPORTED:
            if d != "2023-04-05":
                self.assertEqual(S[d]["nt8_last_bar_grade"], rep, d)
        self.assertEqual(S["2022-03-14"]["nt8_last_bar_grade"], sessions.GRADE_FULL)

    def test_unmapped_early_close_refused(self):
        for t, hm in (("120000", "12:00"), ("121500", "12:15"), ("150000", "15:00")):
            self.write_days({"2021-03-08": "160000", "2021-03-12": t})
            with self.assertRaises(sessions.NotSettledBySpec) as cm:
                sessions.scan_file(self.path)
            self.assertIn("NotSettledBySpec: early-close day with no NT8 cut mapping: 2021-03-12 " + hm,
                          str(cm.exception))

    def test_unmapped_early_close_cli_exit(self):
        self.write_days({"2021-03-08": "160000", "2021-03-12": "120000"})
        out = os.path.join(self.tmp.name, "cal.json")
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 3, p.stderr)
        self.assertIn("NotSettledBySpec: early-close day with no NT8 cut mapping: 2021-03-12 12:00", p.stderr)
        self.assertFalse(os.path.exists(out))

    def test_print_table_footnote(self):
        foot = ("Note: the early-close counts include 2023-04-05 (file last bar 14:03), which the "
                "results report INFERS is a data gap, not an early close")
        days, d = {}, dt.date(2021, 3, 8)
        while d <= dt.date(2023, 6, 30):
            if d.weekday() < 5:
                days[d.isoformat()] = "160000"
            d += dt.timedelta(days=1)
        days["2023-04-05"] = "140300"
        self.write_days(days)
        out = os.path.join(self.tmp.name, "cal.json")
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out,
                            "--print-table"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(p.stdout.count(foot), 1, p.stdout)
        days["2023-04-05"] = "160000"
        self.write_days(days)
        p = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--data", self.path, "--out", out,
                            "--print-table"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertNotIn(foot, p.stdout)


@unittest.skipUnless(os.path.isfile(REAL), "real data file absent: %s — real-calendar test SKIPPED" % REAL)
class TestRealCalendar(unittest.TestCase):
    """Spec figures: values-spec §5 :85-86, §7 :103, §9 (b) :232. Expected values are the
    spec's; do not edit them to match the file — a failure here is a discrepancy to report."""

    @classmethod
    def setUpClass(cls):
        cls.cal = sessions.build_calendar(REAL)

    def test_spec_figures(self):
        c = self.cal
        S = c["sessions"]
        self.assertEqual(c["N"], 1352)
        self.assertEqual(S[0]["date"], "2021-03-08")
        self.assertEqual(S[15]["date"], "2021-03-29")
        self.assertEqual(S[1351]["date"], "2026-07-17")
        self.assertEqual(c["K"], 17)
        self.assertEqual(c["oos_sessions"], 1071)
        self.assertEqual(c["dropped"], [1324, 1352])
        self.assertEqual(c["dropped_dates"], ["2026-06-08", "2026-07-17"])
        w1, w17 = c["windows"][0], c["windows"][16]
        self.assertEqual(w1["is_dates"], ["2021-03-08", "2022-03-16"])
        self.assertEqual(w1["oos_dates"], ["2022-03-17", "2022-06-15"])
        self.assertEqual(w17["is_dates"], ["2025-02-26", "2026-03-09"])
        self.assertEqual(w17["oos_dates"], ["2026-03-10", "2026-06-05"])
        self.assertEqual(c["cscv_rows"], [12, 1323])
        self.assertEqual(c["cscv_rows"][1] - c["cscv_rows"][0] + 1, 1312)
        self.assertEqual(1312, 16 * 82)
        self.assertEqual((c["cscv_S"], c["cscv_block"]), (16, 82))
        self.assertEqual(c["weekend_dates_dropped"], 141)   # §9 (b) :232, 141 dates

    def test_oracle_sessions_9e(self):
        # values-spec §9 (e) :235: 2021-06-15 (s70), 2024-12-26 (s967), 2026-03-18 (s1267)
        d2s = sessions.date_to_session(self.cal)
        self.assertEqual((d2s["2021-06-15"], d2s["2024-12-26"], d2s["2026-03-18"]), (70, 967, 1267))

    def test_early_close_examples_9c(self):
        # values-spec §9 (c) :233 and results report :144-151
        d = {s["date"]: s for s in self.cal["sessions"]}
        for date, last, nt8 in [("2024-12-24", "13:15", "12:15"), ("2025-01-20", "13:00", "12:00"),
                                ("2025-06-19", "13:00", "12:00"), ("2021-11-26", "13:15", "12:15"),
                                ("2024-07-03", "13:15", "12:15"), ("2024-11-29", "13:15", "12:15"),
                                ("2025-07-03", "13:15", "12:15"), ("2023-04-05", "14:03", "14:03")]:
            self.assertEqual((d[date]["last_bar"], d[date]["nt8_last_bar"]), (last, nt8), date)

    def test_grades_w6(self):
        early = [s for s in self.cal["sessions"] if s["early_close_in_file"]]
        rep = "REPORTED BY docs/reports/2026-11-01-three-strategy-results.md:144-151 (OBSERVED there)"
        got = sorted(s["date"] for s in early if s["nt8_last_bar_grade"].startswith(rep))
        self.assertEqual(got, ["2021-11-26", "2023-04-05", "2024-07-03", "2024-11-29", "2024-12-24",
                               "2025-01-20", "2025-06-19", "2025-07-03"])
        rule = [s for s in early if s["nt8_last_bar_grade"] == "INFERRED: mapped by rule from the file's last bar"]
        self.assertEqual(len(rule), 39)
        self.assertEqual(len(early), 47)

    def test_windows_contiguous(self):
        for i, w in enumerate(self.cal["windows"], 1):
            self.assertEqual(w["is"], [63 * (i - 1) + 1, 63 * (i - 1) + 252])
            self.assertEqual(w["oos"], [63 * (i - 1) + 253, 63 * (i - 1) + 315])


if __name__ == "__main__":
    unittest.main()
