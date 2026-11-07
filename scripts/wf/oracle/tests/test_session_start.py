"""Session-start tests (finding B1, unit 2026-11-07-wf-oracles, W6): market.load_market(..., session_start=) is
REQUIRED, "09:31" (the values-spec's literal reading) or "08:31" (OBSERVED fit on the three committed 2026-11-01
base runs; UNVERIFIED for arm (b) on the VM). Expected values in (a) are explicit arithmetic on the fixture
literals below, in the .cs operation order -- never a call into the code under test. The real-file literals in
(d) come from the adversary's independent parse (it imports no oracle code).

Fixture (18 weekdays from Mon 2021-03-08; the 4th, Thu 2021-03-11, is PRE-OPEN-ONLY: bars 08:45 and 09:30 only,
so it is no session; s1..s17 are the other 17 days). Every session n:
  08:30  o=h=l=c 5000 v 99          (before either start: ignored at both)
  08:31  o 990 h 1010 l 985 c 995 v 10
  09:30  o=h=l=c 995 v 5
  09:31  o 1000 h 1002 l 998 c 1000 v 10
  10:00  o 1000 h C_n l 1000 c C_n v 20     C_n = 1004 + 0.25*(n % 3)
  16:00  o=h=l=c 1000 v 10
"""
import datetime as dt
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
for _p in (ORACLE, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import market as mk   # noqa: E402
import band as bd     # noqa: E402
import atr as at      # noqa: E402
import grade as gr    # noqa: E402
import t6ii as t6     # noqa: E402

DATA = os.environ.get("PRAXIS_ORACLE_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")


def _weekdays(first, count):
    d, out = first, []
    while len(out) < count:
        if d.weekday() < 5:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


ALL_DAYS = _weekdays(dt.date(2021, 3, 8), 18)
PRE_ONLY = ALL_DAYS[3]                       # 2021-03-11
DATES = [d for d in ALL_DAYS if d != PRE_ONLY]   # s1..s17
C = {n: 1004 + 0.25 * (n % 3) for n in range(1, 18)}


def _line(day, hhmmss, o, h, l, c, v):
    return "%s %s;%r;%r;%r;%r;%d\n" % (day.strftime("%Y%m%d"), hhmmss, float(o), float(h), float(l), float(c), v)


def build(path):
    out = []
    for day in ALL_DAYS:
        if day == PRE_ONLY:
            out += [_line(day, "084500", 777, 777, 777, 777, 3), _line(day, "093000", 778, 778, 778, 778, 4)]
            continue
        n = DATES.index(day) + 1
        out += [_line(day, "083000", 5000, 5000, 5000, 5000, 99),
                _line(day, "083100", 990, 1010, 985, 995, 10),
                _line(day, "093000", 995, 995, 995, 995, 5),
                _line(day, "093100", 1000, 1002, 998, 1000, 10),
                _line(day, "100000", 1000, C[n], 1000, C[n], 20),
                _line(day, "160000", 1000, 1000, 1000, 1000, 10)]
    with open(path, "w") as fh:
        fh.writelines(out)


# ---- hand values, s17 10:00, Lookback 2, k 1.0 (.cs order: band :350-367 newest -> oldest, VWAP :213-218/:368,
# ATR :384-391 oldest -> newest over the last 14 committed records s3..s16) ----
def _tp(h, l, c):
    return (h + l + c) / 3.0


def hand(start):
    o = 990.0 if start == "08:31" else 1000.0        # todayOpen = first loaded bar's open (every session alike)
    pc = 1000.0                                       # s16 16:00 close
    sum_abs = 0.0
    sum_abs += abs(C[16] / o - 1.0)
    sum_abs += abs(C[15] / o - 1.0)
    sigma = sum_abs / 2
    upper = max(o, pc) * (1.0 + 1.0 * sigma)
    lower = min(o, pc) * (1.0 - 1.0 * sigma)
    pv, vol = 0.0, 0.0
    bars = [(1002.0, 998.0, 1000.0, 10.0), (C[17], 1000.0, C[17], 20.0)]
    if start == "08:31":
        bars = [(1010.0, 985.0, 995.0, 10.0), (995.0, 995.0, 995.0, 5.0)] + bars
    for h, l, c, v in bars:
        pv += _tp(h, l, c) * v
        vol += v
    vwap = pv / vol
    s = 0.0
    for n in range(3, 17):
        hi, lo = (1010.0, 985.0) if start == "08:31" else (max(1002.0, C[n], 1000.0), 998.0)
        s += max(hi, pc) - min(lo, pc)
    return {"sigma": sigma, "upper": upper, "lower": lower, "vwap": vwap, "today_open": o, "atr_sum": s,
            "atr": s / 14}


class SessionStartSynthetic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="w6-ss-")
        cls.path = os.path.join(cls.tmp, "w6-fixture.txt")
        build(cls.path)
        cls.m = {s: mk.load_market(cls.path, session_start=s) for s in ("09:31", "08:31")}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    # (a) hand values at each start, and they differ
    def test_a_hand_values(self):
        got = {}
        for start in ("09:31", "08:31"):
            m, H = self.m[start], hand(start)
            st = bd.band_at(m, 17, "10:00", 2, 1.0)
            have, s, atr = at.atr_at(m, 17)
            self.assertTrue(st.have_band and have, start)
            self.assertEqual(st.today_open, H["today_open"], start)
            self.assertEqual(st.sigma, H["sigma"], start)
            self.assertEqual(st.upper, H["upper"], start)
            self.assertEqual(st.lower, H["lower"], start)
            self.assertEqual(st.vwap, H["vwap"], start)
            self.assertEqual((s, atr), (H["atr_sum"], H["atr"]), start)
            got[start] = (st.today_open, st.sigma, st.upper, st.lower, st.vwap, atr)
        for j, name in enumerate(("open", "sigma", "upper", "lower", "vwap", "atr")):
            self.assertNotEqual(got["09:31"][j], got["08:31"][j], name)
        self.assertEqual(hand("08:31")["atr"], 25.0)

    def test_a_bars_and_labels(self):
        m31, m08 = self.m["09:31"], self.m["08:31"]
        self.assertEqual([b.mod for b in m31.session(5).bars], [571, 600, 960])
        self.assertEqual([b.mod for b in m08.session(5).bars], [511, 570, 571, 600, 960])   # 08:30 never loaded
        self.assertEqual((m31.pre_open_bars, m08.pre_open_bars), (0, 2 * 17))
        self.assertEqual(m08.session_start, "08:31")
        self.assertEqual(m08.session_start_label, mk.SESSION_STARTS["08:31"])
        self.assertIn("OBSERVED fit", mk.session_start_line(m08))
        self.assertIn("UNVERIFIED for arm (b)", mk.session_start_line(m08))
        self.assertIn("literal reading", mk.session_start_line(m31))
        self.assertEqual(sorted(mk.SESSION_STARTS), ["08:31", "09:31"])

    # (b) required, exact
    def test_b_required_and_exact(self):
        with self.assertRaises(TypeError) as cm:
            mk.load_market(self.path)
        for s in ("REQUIRED", '"09:31"', '"08:31"', "literal reading", "OBSERVED fit"):
            self.assertIn(s, str(cm.exception))
        for bad in ("09:30", "8:31", "0831", "08:31:00", " 08:31", None, 831):
            with self.assertRaises(ValueError, msg=repr(bad)) as cm:
                mk.load_market(self.path, session_start=bad)
            self.assertIn("08:31", str(cm.exception))
        with self.assertRaises(TypeError):
            mk.load_market(self.path, mk.sessions.RANGE[0], mk.sessions.RANGE[1], "08:31")   # keyword-only
        for main, argv in ((t6.main, ["--data", self.path, "--grid"]),
                           (bd.main, ["--data", self.path, "--lookback", "2", "--noise-mult", "1.0", "--date",
                                      "2021-03-31", "--time", "10:00"]),
                           (at.main, ["--data", self.path, "--date", "2021-03-31"]),
                           (gr.main, ["--runs", "/nonexistent.json", "--data", self.path])):
            for extra in ([], ["--session-start", "09:30"], ["--session-start", "8:31"]):
                err = io.StringIO()
                with redirect_stderr(err), self.assertRaises(SystemExit) as cm:
                    main(argv + extra)
                self.assertEqual(cm.exception.code, 2, (main.__module__, extra))
                self.assertIn("--session-start", err.getvalue())

    def test_b_cli_prints_start(self):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = bd.main(["--data", self.path, "--session-start", "08:31", "--lookback", "2", "--noise-mult", "1.0",
                          "--date", DATES[16].isoformat(), "--time", "10:00"])
        self.assertEqual(rc, 0)
        self.assertIn(mk.session_start_line(self.m["08:31"]), out.getvalue())
        self.assertIn("sigma          %r" % hand("08:31")["sigma"], out.getvalue())
        out = io.StringIO()
        with redirect_stdout(out):
            rc = at.main(["--data", self.path, "--session-start", "09:31", "--date", DATES[16].isoformat()])
        self.assertEqual(rc, 0)
        self.assertIn("session start: 09:31 — ", out.getvalue())
        self.assertIn("atr      %r" % hand("09:31")["atr"], out.getvalue())

    # (c) pre-open-only weekday: dropped and counted at 08:31, no numbering shift
    def test_c_pre_open_only_dropped(self):
        m31, m08 = self.m["09:31"], self.m["08:31"]
        self.assertEqual(m08.pre_open_only_dropped, ["2021-03-11"])
        self.assertEqual(m08.pre_open_only_bars_dropped, 2)
        self.assertEqual((m31.pre_open_only_dropped, m31.pre_open_only_bars_dropped), ([], 0))
        self.assertNotIn("2021-03-11", m08.by_date)
        self.assertEqual(m08.N, 17)
        self.assertEqual([(s.n, s.date) for s in m08.sessions], [(s.n, s.date) for s in m31.sessions])
        self.assertEqual((m08.by_date["2021-03-10"].n, m08.by_date["2021-03-12"].n), (3, 4))
        pb = mk.prev_bar(m08, 4, 0)                    # s4's previous loaded bar = s3 16:00, not the dropped day
        self.assertEqual((pb.dt, pb.c), (dt.datetime(2021, 3, 10, 16, 0), 1000.0))
        self.assertEqual(m08.session(4).bars[0].dt, dt.datetime(2021, 3, 12, 8, 31))

    # grade sheet: the chosen start is printed; line 3 stays the standing sentence, once
    def test_grade_sheet_names_start(self):
        import test_grade as tg
        p = os.path.join(self.tmp, "w6-gdata.txt")
        tg.write_data(p, {16: tg.DAY_A})
        tb = os.path.join(self.tmp, "w6-trades.json")
        tg.write_bridge(tb, [tg.A_LONG, tg.A_SHORT])
        man = os.path.join(self.tmp, "w6-man.json")
        with open(man, "w") as fh:
            json.dump([dict(tg.P10, label="A", path=tb, format="bridge")], fh)
        for start in ("08:31", "09:31"):
            out = os.path.join(self.tmp, "w6-sheet-%s.md" % start.replace(":", ""))
            rc = gr.main(["--runs", man, "--data", p, "--out", out, "--session-start", start])
            self.assertEqual(rc, 0, start)
            with open(out) as fh:
                text = fh.read()
            lines = text.splitlines()
            self.assertEqual(lines[2], gr.STANDING_LIMITATION)
            self.assertEqual(gr._norm(text).count(gr.STANDING_PHRASE), 1)
            self.assertEqual(sum(1 for x in lines if x.startswith("- session start: %s — %s" % (start, mk.SESSION_STARTS[start]))), 1)


# (d) real-file regression at 08:31 (literals from the adversary's independent parse; asserted with ==)
REAL = (("2021-06-15", 70, 0.0018909606026999743, 17597.212832025823, 17514.567896083972, 136.32142857142858),
        ("2024-12-26", 967, 0.002936108576064768, 23500.798896154352, 23316.588366921584, 338.35714285714283),
        ("2026-03-18", 1267, 0.0042497760950293085, 25438.90214070721, 25208.163730822263, 450.25))


@unittest.skipUnless(os.path.exists(DATA), "data file absent: %s" % DATA)
class SessionStartRealFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = mk.load_market(DATA, session_start="08:31")

    def test_d_oracle_sessions_0831(self):
        m = self.m
        self.assertEqual(m.N, 1352)
        for date, n, sigma, upper, lower, atr in REAL:
            self.assertEqual(m.by_date[date].n, n)
            st = bd.band_at(m, n, "10:00", 14, 1.0)
            have, _s, a = at.atr_at(m, n)
            self.assertTrue(st.have_band and have, date)
            self.assertEqual(st.sigma, sigma, date)
            self.assertEqual(st.upper, upper, date)
            self.assertEqual(st.lower, lower, date)
            self.assertEqual(a, atr, date)
            self.assertEqual(m.by_date[date].bars[0].dt.strftime("%H:%M"), "08:31", date)

    def test_d_pre_open_only_days(self):
        self.assertEqual(self.m.pre_open_only_dropped, ["2021-04-02", "2023-04-07", "2025-01-09", "2026-04-03"])
        self.assertGreater(self.m.pre_open_bars, 0)
        for date, n in (("2021-03-08", 1), ("2021-03-29", 16), ("2026-07-17", 1352)):
            self.assertEqual(self.m.session(n).date, date)
        t6.check_sessions(self.m)                      # s70 / s967 / s1267 unchanged at 08:31


if __name__ == "__main__":
    unittest.main()
