#!/usr/bin/env python3
# b2-stitch-selftest.py — Praxis_build-6bw (b2-stitch) automated self-test.
#
# Runs the FULL b2_stitch pipeline end-to-end on a bundled, deterministic
# SYNTHETIC fixture (NO real data, NO live services) and asserts the two
# properties that matter for a back-adjusted continuous series:
#   1. the Vol/OI-crossover ROLL DATES are detected exactly, and
#   2. the Difference (Panama) back-adjustment makes the seams continuous
#      (ADDITIVE constant offset per contract — NOT ratio).
# It also asserts the OI GATE: an OI-absent daily makes the tool REFUSE
# (OI_BLANK) instead of silently rolling volume-only.
#
# Verification command (auditor re-runs this):
#     python3 scripts/tests/b2-stitch-selftest.py
# Exit 0 iff ALL cases pass; non-zero (with the failed assertion) otherwise.
#
# Fixture design (3 contracts, 2 known seams so cumulative back-adjust is
# genuinely exercised):
#   C1=03-24, C2=06-24, C3=09-24
#   Seam R1 (C1->C2) = 2024-03-15  (daily close spread 18000 -> 18050 = +50)
#   Seam R2 (C2->C3) = 2024-06-14  (daily close spread 18500 -> 18540 = +40)
#   Panama offsets: off(09-24)=0, off(06-24)=+40, off(03-24)=+40+50=+90
import os
import sys
import shutil
import tempfile
import csv

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))  # scripts/
import b2_stitch as S  # noqa: E402

FAILS = []


def check(cond, msg):
    tag = "PASS" if cond else "FAIL"
    print("  [%s] %s" % (tag, msg))
    if not cond:
        FAILS.append(msg)


def _write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        for r in rows:
            w.writerow(r)


# --- deterministic fixture data ------------------------------------------------
# NOTE headers deliberately non-obvious to exercise schema resolution:
#   daily "OpenInt" (not "Open Interest"); minute single "Timestamp" column.
DAILY_HDR = ["Date", "Open", "High", "Low", "Close", "Volume", "OpenInt"]
MIN_HDR = ["Timestamp", "Open", "High", "Low", "Close", "Volume"]

MAR = ["2024-03-11", "2024-03-12", "2024-03-13", "2024-03-14",
       "2024-03-15", "2024-03-18", "2024-03-19", "2024-03-20"]
JUN = ["2024-06-10", "2024-06-11", "2024-06-12", "2024-06-13",
       "2024-06-14", "2024-06-17", "2024-06-18", "2024-06-19"]

# C1 = 03-24 (front through R1). idx4 (03-15) is the crossover day.
C1_MAR_VOL = [500, 450, 400, 350, 300, 250, 200, 150]
C1_MAR_OI = [800, 780, 760, 740, 700, 650, 600, 550]
C1_MAR_CL = [17960, 17970, 17980, 17990, 18000, 17995, 17990, 17985]  # close@03-15 = 18000
# C2 = 06-24 (back in Mar, front in Jun)
C2_MAR_VOL = [100, 150, 200, 280, 350, 420, 500, 560]                 # crosses C1 at idx4
C2_MAR_OI = [200, 300, 400, 550, 750, 900, 1000, 1100]               # crosses C1 at idx4
C2_MAR_CL = [18010, 18020, 18030, 18040, 18050, 18055, 18060, 18065]  # close@03-15 = 18050
C2_JUN_VOL = [600, 550, 500, 450, 400, 350, 300, 250]
C2_JUN_OI = [900, 880, 860, 840, 800, 750, 700, 650]
C2_JUN_CL = [18460, 18470, 18480, 18490, 18500, 18495, 18490, 18485]  # close@06-14 = 18500
# C3 = 09-24 (back in Jun). idx4 (06-14) is the crossover day.
C3_JUN_VOL = [120, 180, 250, 360, 450, 540, 600, 650]                 # crosses C2 at idx4
C3_JUN_OI = [200, 320, 440, 600, 850, 1000, 1100, 1200]              # crosses C2 at idx4
C3_JUN_CL = [18510, 18520, 18525, 18530, 18540, 18545, 18550, 18555]  # close@06-14 = 18540


def _daily_rows(dates, vol, oi, cl, blank_oi=False):
    rows = []
    for i, d in enumerate(dates):
        rows.append([d, cl[i], cl[i], cl[i], cl[i], vol[i], "" if blank_oi else oi[i]])
    return rows


# minute bars: (date, HH:MM, close)   OHLC all = close, volume 100
C1_MIN = [
    ("2024-03-13", "09:30", 17980), ("2024-03-13", "09:31", 17981), ("2024-03-13", "09:32", 17982),
    ("2024-03-14", "09:30", 17990), ("2024-03-14", "09:31", 17991), ("2024-03-14", "16:59", 17998),
]
C2_MIN = [
    ("2024-03-15", "09:30", 18049), ("2024-03-15", "09:31", 18050), ("2024-03-15", "09:32", 18051),
    ("2024-03-18", "09:30", 18060),
    ("2024-06-12", "09:30", 18470),
    ("2024-06-13", "09:30", 18490), ("2024-06-13", "16:59", 18498),
]
C3_MIN = [
    ("2024-06-14", "09:30", 18541), ("2024-06-14", "09:31", 18542),
    ("2024-06-17", "09:30", 18550),
]


def _min_rows(bars):
    return [["%s %s:00" % (d, hm), c, c, c, c, 100] for (d, hm, c) in bars]


def build_fixture(root, blank_oi_c2=False):
    raw = os.path.join(root, "raw")
    _write_csv(os.path.join(raw, "NQ-03-24_daily.csv"), DAILY_HDR,
               _daily_rows(MAR, C1_MAR_VOL, C1_MAR_OI, C1_MAR_CL))
    _write_csv(os.path.join(raw, "NQ-06-24_daily.csv"), DAILY_HDR,
               _daily_rows(MAR, C2_MAR_VOL, C2_MAR_OI, C2_MAR_CL, blank_oi=blank_oi_c2)
               + _daily_rows(JUN, C2_JUN_VOL, C2_JUN_OI, C2_JUN_CL, blank_oi=blank_oi_c2))
    _write_csv(os.path.join(raw, "NQ-09-24_daily.csv"), DAILY_HDR,
               _daily_rows(JUN, C3_JUN_VOL, C3_JUN_OI, C3_JUN_CL))
    _write_csv(os.path.join(raw, "NQ-03-24_1min.csv"), MIN_HDR, _min_rows(C1_MIN))
    _write_csv(os.path.join(raw, "NQ-06-24_1min.csv"), MIN_HDR, _min_rows(C2_MIN))
    _write_csv(os.path.join(raw, "NQ-09-24_1min.csv"), MIN_HDR, _min_rows(C3_MIN))


def _last_row(rows, code):
    return [r for r in rows if r["src"] == code][-1]


def _first_row(rows, code):
    return [r for r in rows if r["src"] == code][0]


# ============================================================================ #
def case_A_happy():
    print("\nCASE A — full pipeline on good fixture (roll dates + Difference seams)")
    root = tempfile.mkdtemp(prefix="b2stitch-A-")
    try:
        build_fixture(root)
        # Existing fixtures author their bars in the OUTPUT wall-clock already, so
        # force source_tz==target_tz (no shift) — the tz-conversion path is
        # exercised separately by Case E (Praxis_build-1u6).
        res = S.run_pipeline(root, label="SYNTHETIC-FIXTURE", target_tz="UTC")
        assert not res["pending"]

        # (crit 1) roll dates detected exactly
        from datetime import date
        check(res["roll_dates"] == [date(2024, 3, 15), date(2024, 6, 14)],
              "roll dates == [2024-03-15, 2024-06-14]  (got %s)" % res["roll_dates"])
        check(res["roll_diags"][0]["trigger"] == "vol+oi crossover"
              and res["roll_diags"][0]["oi_used"] is True,
              "R1 trigger = vol+oi crossover (OI used, not volume-only)")

        # (crit 2) Panama additive offsets
        off = res["offsets"]
        check(off["09-24"] == 0.0 and off["06-24"] == 40.0 and off["03-24"] == 90.0,
              "offsets == {09-24:0, 06-24:+40, 03-24:+90}  (got %s)" % off)
        check(res["seams"][0]["raw_gap"] == 50.0 and res["seams"][1]["raw_gap"] == 40.0,
              "seam raw daily-close gaps == +50, +40")

        rows = res["rows"]
        by_ts = {r["ts"].strftime("%Y-%m-%d %H:%M"): r for r in rows}

        # additive (NOT ratio): two DIFFERENT-priced C1 bars both shift by exactly +90
        b1 = by_ts["2024-03-13 09:30"]; b2 = by_ts["2024-03-14 16:59"]
        check(b1["c"] == 17980 + 90 and b2["c"] == 17998 + 90,
              "C1 bars shifted by CONSTANT +90 (17980->%g, 17998->%g) — additive, not ratio"
              % (b1["c"], b2["c"]))

        # seam continuity R1: adjusted delta tiny (+1) vs RAW delta (+51 spread removed)
        lastC1 = _last_row(rows, "03-24"); firstC2 = _first_row(rows, "06-24")
        adj_d1 = firstC2["c"] - lastC1["c"]
        raw_d1 = 18049 - 17998
        check(adj_d1 == 1.0 and raw_d1 == 51.0,
              "R1 seam: adjusted delta=+%g pt (continuous); raw delta=+%g pt (spread removed)"
              % (adj_d1, raw_d1))

        # seam continuity R2
        lastC2 = _last_row(rows, "06-24"); firstC3 = _first_row(rows, "09-24")
        adj_d2 = firstC3["c"] - lastC2["c"]
        raw_d2 = 18541 - 18498
        check(adj_d2 == 3.0 and raw_d2 == 43.0,
              "R2 seam: adjusted delta=+%g pt (continuous); raw delta=+%g pt (spread removed)"
              % (adj_d2, raw_d2))

        # monotonic + dedup
        mono = all(rows[i]["ts"] <= rows[i + 1]["ts"] for i in range(len(rows) - 1))
        check(mono and res["dupes"] == 0, "monotonic timestamps, 0 duplicates")

        # artifacts written + report has 2 seams
        check(os.path.isfile(res["out_path"]), "stitched CSV written: %s" % os.path.basename(res["out_path"]))
        with open(res["report_path"]) as fh:
            rep = fh.read()
        check("seams=2" in res["summary"] and "§3 roll seams" in rep,
              "validation report generated with 2 roll seams  (%s)" % res["summary"])
        print("    SUMMARY: %s" % res["summary"])
    finally:
        shutil.rmtree(root, ignore_errors=True)


def case_B_oi_blank():
    print("\nCASE B — OI GATE: back-month daily OI blank -> tool REFUSES (OI_BLANK)")
    root = tempfile.mkdtemp(prefix="b2stitch-B-")
    out = os.path.join(root, "reports", "should-not-exist.csv")
    try:
        build_fixture(root, blank_oi_c2=True)
        refused = False
        try:
            S.run_pipeline(root, out_path=out, label="SYNTHETIC-FIXTURE", target_tz="UTC")
        except S.OIBlankError as e:
            refused = True
            print("    raised OIBlankError: %s" % str(e).split(".")[0])
        check(refused, "run_pipeline RAISED OIBlankError (did not silently proceed)")
        check(not os.path.isfile(out), "NO stitched CSV written on OI_BLANK (no silent volume-only fallback)")

        # and prove the CLI surfaces it as exit code 2
        rc = S.main(["b2_stitch.py", "--root", root, "--label", "SYNTHETIC-FIXTURE"])
        check(rc == 2, "CLI exit code == 2 (OI_BLANK)  (got %d)" % rc)
    finally:
        shutil.rmtree(root, ignore_errors=True)


def case_C_pending():
    print("\nCASE C — build-ahead-of-data: empty raw/ -> VALIDATION-PENDING (exit 3)")
    root = tempfile.mkdtemp(prefix="b2stitch-C-")
    try:
        os.makedirs(os.path.join(root, "raw"), exist_ok=True)
        res = S.run_pipeline(root, label="REAL")
        check(res.get("pending") is True, "run_pipeline returns pending on empty raw/")
        rc = S.main(["b2_stitch.py", "--root", root])
        check(rc == 3, "CLI exit code == 3 (VALIDATION-PENDING)  (got %d)" % rc)
    finally:
        shutil.rmtree(root, ignore_errors=True)


def case_D_volonly_override():
    print("\nCASE D — authorized override: --allow-volume-only rolls on volume alone (banner)")
    root = tempfile.mkdtemp(prefix="b2stitch-D-")
    try:
        build_fixture(root, blank_oi_c2=True)
        # with the override the pipeline proceeds (roll on volume-only crossover)
        res = S.run_pipeline(root, label="SYNTHETIC-FIXTURE", allow_volume_only=True,
                             verbose=False, target_tz="UTC")
        from datetime import date
        check(not res["pending"] and res["roll_dates"] == [date(2024, 3, 15), date(2024, 6, 14)],
              "override proceeds; volume-only crossover still finds correct seams")
        check(res["roll_diags"][0]["oi_used"] is False,
              "diag records oi_used=False (deviation is recorded, not hidden)")
    finally:
        shutil.rmtree(root, ignore_errors=True)


def case_E_tz_seam_lossless():
    print("\nCASE E — UTC->ET conversion ACROSS a roll seam: ZERO seam loss (Praxis_build-1u6)")
    # The attempt-1 trap: pre-roll EVENING ETH bars are stored as early-UTC on the
    # roll date but fall on roll_date-1 in ET. Converting BEFORE the seam handoff
    # routes them to the FRONT contract (which lacks them) while the BACK contract
    # excludes them via date>=roll_date -> the bars are silently DROPPED. The fix
    # routes on the SOURCE-tz date and converts only the emitted ts, so nothing is
    # lost. This fixture puts such evening bars in the BACK contract (06-24) and
    # asserts: (a) the fix keeps them (correct ET timestamps), and (b) the naive
    # convert-then-route path DROPS exactly them — so the test fails against the
    # bug and passes against the fix.
    from datetime import date, timezone
    root = tempfile.mkdtemp(prefix="b2stitch-E-")
    raw = os.path.join(root, "raw")
    try:
        # --- daily: 2 contracts, OI present, vol+OI crossover at 2024-03-15 ----
        _write_csv(os.path.join(raw, "NQ-03-24_daily.csv"), DAILY_HDR,
                   _daily_rows(MAR, C1_MAR_VOL, C1_MAR_OI, C1_MAR_CL))
        _write_csv(os.path.join(raw, "NQ-06-24_daily.csv"), DAILY_HDR,
                   _daily_rows(MAR, C2_MAR_VOL, C2_MAR_OI, C2_MAR_CL))
        # --- minute: front (03-24) bars strictly before the roll date ----------
        c1_min = [
            ["2024-03-13 13:30:00", 17980, 17980, 17980, 17980, 100],
            ["2024-03-14 13:30:00", 17990, 17990, 17990, 17990, 100],
            ["2024-03-14 20:59:00", 17998, 17998, 17998, 17998, 100],
        ]
        # back (06-24) minute file. The three EVENING seam bars are stored at
        # 01:00/02:00/03:00Z on the roll date 2024-03-15 == 21:00/22:00/23:00 ET on
        # 2024-03-14 (EDT, DST already in effect since 2024-03-10). Plus a 13:30Z
        # bar == 09:30 ET (the RTH-open anchor) and a next-session bar.
        c2_min = [
            ["2024-03-15 01:00:00", 18050, 18050, 18050, 18050, 100],  # -> ET 03-14 21:00
            ["2024-03-15 02:00:00", 18051, 18051, 18051, 18051, 100],  # -> ET 03-14 22:00
            ["2024-03-15 03:00:00", 18052, 18052, 18052, 18052, 100],  # -> ET 03-14 23:00
            ["2024-03-15 13:30:00", 18060, 18060, 18060, 18060, 100],  # -> ET 03-15 09:30 (RTH open)
            ["2024-03-15 13:31:00", 18061, 18061, 18061, 18061, 100],  # -> ET 03-15 09:31
            ["2024-03-18 13:30:00", 18075, 18075, 18075, 18075, 100],  # -> ET 03-18 09:30
        ]
        _write_csv(os.path.join(raw, "NQ-03-24_1min.csv"), MIN_HDR, c1_min)
        _write_csv(os.path.join(raw, "NQ-06-24_1min.csv"), MIN_HDR, c2_min)

        # build the pipeline pieces directly so we can drive BOTH routing paths
        schema = S.load_schema(None)
        d1, _, _ = S.read_daily(os.path.join(raw, "NQ-03-24_daily.csv"), schema)
        d2, _, _ = S.read_daily(os.path.join(raw, "NQ-06-24_daily.csv"), schema)
        m1 = S.read_minute(os.path.join(raw, "NQ-03-24_1min.csv"), schema)
        m2 = S.read_minute(os.path.join(raw, "NQ-06-24_1min.csv"), schema)
        codes = ["03-24", "06-24"]
        rd = S.compute_roll_date(d1, d2)
        check(rd["roll_date"] == date(2024, 3, 15) and rd["oi_used"] is True,
              "roll date == 2024-03-15 on vol+OI crossover (got %s)" % rd["roll_date"])
        roll_dates = [rd["roll_date"]]
        offsets, _seams = S.build_offsets(codes, roll_dates, {"03-24": d1, "06-24": d2})
        minute_by_code = {"03-24": m1, "06-24": m2}

        # (fix) route on the SOURCE-tz date, emit ET
        fix_rows, _ = S.stitch(codes, roll_dates, offsets, minute_by_code,
                               source_tz="UTC", target_tz="America/New_York")
        # (bug) convert-then-route — the attempt-1 approach
        naive_rows, _ = S.stitch(codes, roll_dates, offsets, minute_by_code,
                                 source_tz="UTC", target_tz="America/New_York", _naive=True)

        total_in = len(m1) + len(m2)  # every real minute lives in exactly one window
        check(len(fix_rows) == total_in,
              "fix keeps ALL %d real minutes (got %d) — zero seam loss" % (total_in, len(fix_rows)))

        et = {r["ts"].strftime("%Y-%m-%d %H:%M"): r for r in fix_rows}
        # the three evening seam bars survived, sourced from the BACK contract, ET-dated
        evenings = ["2024-03-14 21:00", "2024-03-14 22:00", "2024-03-14 23:00"]
        got_ev = all(k in et and et[k]["src"] == "06-24" for k in evenings)
        check(got_ev, "3 pre-roll evening bars present & sourced from BACK 06-24 (ET %s)" % evenings)

        # RTH-open spot-check: stored 13:30Z -> emitted 09:30 ET
        check("2024-03-15 09:30" in et and et["2024-03-15 09:30"]["src"] == "06-24",
              "RTH-open: stored 2024-03-15 13:30Z -> emitted 2024-03-15 09:30 ET")

        # distinct instants preserved (no dup / no merge)
        inst = {r["ts"].astimezone(timezone.utc) for r in fix_rows}
        check(len(inst) == len(fix_rows) == total_in,
              "distinct instants == bar count == %d (no dup/merge)" % total_in)

        # THE REGRESSION: the naive path drops EXACTLY the 3 evening bars
        naive_et = {r["ts"].strftime("%Y-%m-%d %H:%M") for r in naive_rows}
        dropped = [k for k in evenings if k not in naive_et]
        check(len(naive_rows) == total_in - 3 and dropped == evenings,
              "naive convert-then-route DROPS exactly the 3 evening seam bars "
              "(bug reproduced: %d vs %d)" % (len(naive_rows), total_in))

        # and end-to-end through run_pipeline (default UTC->ET): invariants clean
        res = S.run_pipeline(root, label="SYNTHETIC-FIXTURE", verbose=False)
        inv = res["invariants"]
        check(inv["instants_equal"] and inv["seam_gap"] == 0
              and inv["bar_count"] == inv["base_bar_count"],
              "run_pipeline invariants: instants_equal=%s seam_gap=%d bars=%d==baseline=%d"
              % (inv["instants_equal"], inv["seam_gap"], inv["bar_count"], inv["base_bar_count"]))
        check(inv["naive_dropped"] == 3,
              "run_pipeline reports naive-would-drop == 3 (trap quantified)")
    finally:
        shutil.rmtree(root, ignore_errors=True)


def main():
    print("=== b2-stitch self-test (Praxis_build-6bw) ===")
    case_A_happy()
    case_B_oi_blank()
    case_C_pending()
    case_D_volonly_override()
    case_E_tz_seam_lossless()
    print("\n%s" % ("=" * 60))
    if FAILS:
        print("RESULT: FAIL — %d assertion(s) failed:" % len(FAILS))
        for f in FAILS:
            print("  - %s" % f)
        return 1
    print("RESULT: PASS — all cases green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
