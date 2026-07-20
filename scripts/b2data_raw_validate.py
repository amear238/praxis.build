#!/usr/bin/env python3
# b2data_raw_validate.py — Praxis_build-3q4 (b2-data-mailbox)
# RAW-LANDING validator for the VM->Mac NQ export mailbox.
#
# SCOPE (design doc §3): validates the RAW per-contract files ONLY — "is the
# export complete + stitch-ready, and is Open Interest present?". It does NOT
# run b2-data spec §4 continuous-series checks (bar-count medians, roll seams,
# gaps) — those operate on the stitched series and belong to the Python stitch
# bead. Keeping them apart prevents false "validated" claims.
#
# Deployment: this file is SOURCE ONLY in the repo. The installer copies it to
# the internal-disk bin (~/Library/Application Support/Praxis/bin) alongside the
# watcher, because macOS TCC blocks launchd from executing scripts on the
# external volume /Volumes/Sensidine. It reads ~/praxis-signals/b2-data/raw/ by
# default; override with --root DIR or env PRAXIS_B2DATA_ROOT (used by the
# self-test to point at a TEMP mailbox root).
#
# Modes:
#   b2data_raw_validate.py [--root DIR]       full battery -> writes
#                                             reports/raw-landing-validation.md,
#                                             prints SUMMARY line, exit 0 iff ready
#   b2data_raw_validate.py --oi-file PATH     single-daily OI check, prints
#                                             OI_PRESENT/OI_BLANK, exit 0 iff present
import csv
import os
import statistics
import sys
from datetime import datetime

# --- The 22-contract expected set (22 x 2 = 44 files) --------------------------
CONTRACTS = [
    "06-21", "09-21", "12-21", "03-22", "06-22", "09-22", "12-22",
    "03-23", "06-23", "09-23", "12-23", "03-24", "06-24", "09-24",
    "12-24", "03-25", "06-25", "09-25", "12-25", "03-26", "06-26", "09-26",
]
EXPECTED = []
for _c in CONTRACTS:
    EXPECTED.append("NQ-%s_1min.csv" % _c)
    EXPECTED.append("NQ-%s_daily.csv" % _c)

MIN_1MIN_ROWS = 20  # coarse floor: below this a 1-min quarterly file is "suspiciously small" (WARN only)
OI_NONZERO_FRACTION = 0.5  # OI is "populated" if non-zero for a MAJORITY of rows


def default_root():
    env = os.environ.get("PRAXIS_B2DATA_ROOT")
    if env:
        return env
    return os.path.join(os.path.expanduser("~"), "praxis-signals", "b2-data")


def read_csv(path):
    """Return (header, data_rows) or (None, None) on unreadable/empty."""
    try:
        with open(path, "r", newline="") as fh:
            rows = [r for r in csv.reader(fh)]
    except Exception:
        return None, None
    if not rows:
        return None, None
    header = rows[0]
    data = [r for r in rows[1:] if any(c.strip() for c in r)]
    return header, data


def find_oi_column(header):
    """Case-insensitive header match on 'open'+'interest'.
    Documented fallback: the LAST column (NT8 daily export = ...,Volume,OpenInterest).
    Returns (index, how)."""
    for i, h in enumerate(header):
        hl = h.strip().lower()
        if "open" in hl and "interest" in hl:
            return i, "header:%s" % h.strip()
    return len(header) - 1, "fallback-last-col"


def to_float(s):
    s = (s or "").strip()
    if s == "":
        return 0.0
    try:
        return float(s)
    except ValueError:
        return 0.0


def oi_check(path):
    """Return dict describing the OI column of a daily file."""
    header, data = read_csv(path)
    res = {"present": False, "n": 0, "nonzero": 0, "frac": 0.0,
           "min": 0.0, "median": 0.0, "max": 0.0, "col": "n/a"}
    if header is None or not data:
        res["col"] = "unreadable/empty"
        return res
    idx, how = find_oi_column(header)
    res["col"] = how
    vals = []
    for r in data:
        if idx < len(r):
            vals.append(to_float(r[idx]))
        else:
            vals.append(0.0)
    if not vals:
        return res
    nonzero = sum(1 for v in vals if v != 0.0)
    res["n"] = len(vals)
    res["nonzero"] = nonzero
    res["frac"] = nonzero / len(vals)
    res["min"] = min(vals)
    res["max"] = max(vals)
    try:
        res["median"] = statistics.median(vals)
    except statistics.StatisticsError:
        res["median"] = 0.0
    res["present"] = res["frac"] > OI_NONZERO_FRACTION
    return res


# --- expiry-window coarse coverage --------------------------------------------
def expiry_year_month(code):
    mm, yy = code.split("-")
    return 2000 + int(yy), int(mm)


def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    # last resort: leading YYYY-MM-DD
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d")
    except ValueError:
        return None


def date_coverage(path, code):
    """Coarse (non-blocking) check that the daily's max date year overlaps the
    contract's expected liquid window. Returns (ok, note)."""
    header, data = read_csv(path)
    if header is None or not data:
        return True, "no-dates"
    dates = []
    for r in data:
        if r:
            d = parse_date(r[0])
            if d:
                dates.append(d)
    if not dates:
        return True, "unparseable-dates"
    dmin, dmax = min(dates), max(dates)
    exp_year, _ = expiry_year_month(code)
    ok = (exp_year - 1) <= dmax.year <= (exp_year + 0)
    note = "%s..%s (expiry~%d)" % (dmin.date(), dmax.date(), exp_year)
    return ok, note


def run_battery(root):
    raw = os.path.join(root, "raw")
    reports = os.path.join(root, "reports")
    os.makedirs(reports, exist_ok=True)

    present, missing = [], []
    for name in EXPECTED:
        if os.path.isfile(os.path.join(raw, name)):
            present.append(name)
        else:
            missing.append(name)

    hard_failures = []   # zero-byte / truncated -> block ready
    warnings = []        # coarse / non-blocking
    for name in present:
        path = os.path.join(raw, name)
        try:
            size = os.path.getsize(path)
        except OSError:
            size = 0
        if size == 0:
            hard_failures.append("%s: zero-byte" % name)
            continue
        header, data = read_csv(path)
        if header is None or not data:
            hard_failures.append("%s: truncated (header+>=1 data row required)" % name)
            continue
        # column-count consistency (coarse WARN)
        bad = sum(1 for r in data if len(r) != len(header))
        if bad:
            warnings.append("%s: %d row(s) column-count != header(%d)" % (name, bad, len(header)))
        if name.endswith("_1min.csv"):
            if len(header) < 5:
                warnings.append("%s: 1min header has <5 columns (need ts+OHLCV)" % name)
            if len(data) < MIN_1MIN_ROWS:
                warnings.append("%s: only %d rows (<%d floor) — suspiciously small" % (name, len(data), MIN_1MIN_ROWS))
        else:  # _daily.csv
            hl = [h.strip().lower() for h in header]
            if not any("vol" in h for h in hl):
                warnings.append("%s: daily header missing a Volume column" % name)
            code = name[len("NQ-"):-len("_daily.csv")]
            ok, note = date_coverage(path, code)
            if not ok:
                warnings.append("%s: date coverage %s does not overlap expected window" % (name, note))

    # OI verdict over present dailies
    oi_rows = []
    oi_blank = []
    for code in CONTRACTS:
        name = "NQ-%s_daily.csv" % code
        if name in present:
            r = oi_check(os.path.join(raw, name))
            oi_rows.append((name, r))
            if not r["present"]:
                oi_blank.append(name)
    if not oi_rows:
        oi_verdict = "NA"
    elif oi_blank:
        oi_verdict = "BLANK"
    else:
        oi_verdict = "PRESENT"

    ready = (len(present) == len(EXPECTED)) and (oi_verdict == "PRESENT") and (not hard_failures)

    summary = "SUMMARY present=%d/%d oi=%s ready=%s" % (
        len(present), len(EXPECTED), oi_verdict, "YES" if ready else "NO")
    if oi_verdict == "BLANK":
        summary += " stop=OI_BLANK"

    # blockers list for the human verdict line
    blockers = []
    if len(present) != len(EXPECTED):
        blockers.append("incomplete %d/%d" % (len(present), len(EXPECTED)))
    if oi_verdict == "BLANK":
        blockers.append("OI_BLANK")
    if hard_failures:
        blockers.append("%d file-sanity failure(s)" % len(hard_failures))

    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = []
    lines.append(summary)
    lines.append("")
    lines.append("# Raw-Landing Validation — b2-data")
    lines.append("")
    if ready:
        lines.append("**VERDICT: READY TO STITCH** — complete set, OI present, no sanity failures.")
    else:
        lines.append("**VERDICT: NOT READY** (blockers: %s)" % ", ".join(blockers))
    if oi_verdict == "BLANK":
        lines.append("")
        lines.append("> **STOP — OI_BLANK.** One or more daily files have blank/zero Open Interest. "
                     "The volume-only crossover fallback is a documented deviation that needs trader "
                     "sign-off + a DECISIONS entry (D-2026-07-17-A OPEN RISK) BEFORE any use.")
    lines.append("")
    lines.append("_Run: %s · root: %s_" % (now, root))
    lines.append("")
    # OI section
    lines.append("## Open Interest (per daily)")
    lines.append("")
    lines.append("| Daily file | col | rows | non-zero | frac | min | median | max | verdict |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for name, r in oi_rows:
        lines.append("| %s | %s | %d | %d | %.2f | %g | %g | %g | %s |" % (
            name, r["col"], r["n"], r["nonzero"], r["frac"],
            r["min"], r["median"], r["max"],
            "OI_PRESENT" if r["present"] else "OI_BLANK"))
    if not oi_rows:
        lines.append("| _(no daily files present)_ | | | | | | | | |")
    lines.append("")
    # Completeness
    lines.append("## Completeness (%d/%d)" % (len(present), len(EXPECTED)))
    lines.append("")
    if missing:
        lines.append("**Missing (%d):**" % len(missing))
        for m in missing:
            lines.append("- %s" % m)
    else:
        lines.append("All 44 expected files present.")
    lines.append("")
    # Sanity
    lines.append("## Per-file sanity")
    lines.append("")
    if hard_failures:
        lines.append("**Hard failures (block ready):**")
        for f in hard_failures:
            lines.append("- %s" % f)
    else:
        lines.append("No hard failures (no zero-byte / truncated files).")
    lines.append("")
    if warnings:
        lines.append("**Warnings (coarse / non-blocking):**")
        for w in warnings:
            lines.append("- %s" % w)
    else:
        lines.append("No coarse warnings.")
    lines.append("")

    report_path = os.path.join(reports, "raw-landing-validation.md")
    try:
        with open(report_path, "w") as fh:
            fh.write("\n".join(lines) + "\n")
    except Exception as e:
        sys.stderr.write("WARN could not write report: %s\n" % e)

    print(summary)
    return 0 if ready else 1


def run_oi_file(path):
    r = oi_check(path)
    tag = "OI_PRESENT" if r["present"] else "OI_BLANK"
    print("%s frac=%.2f nonzero=%d/%d min=%g median=%g max=%g col=%s" % (
        tag, r["frac"], r["nonzero"], r["n"], r["min"], r["median"], r["max"], r["col"]))
    return 0 if r["present"] else 2


def main(argv):
    root = None
    oi_file = None
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--root" and i + 1 < len(argv):
            root = argv[i + 1]
            i += 2
        elif a == "--oi-file" and i + 1 < len(argv):
            oi_file = argv[i + 1]
            i += 2
        elif a in ("-h", "--help"):
            print(__doc__ or "usage: b2data_raw_validate.py [--root DIR] | --oi-file PATH")
            return 0
        else:
            sys.stderr.write("unknown arg: %s\n" % a)
            return 64
    if oi_file:
        return run_oi_file(oi_file)
    if root is None:
        root = default_root()
    return run_battery(root)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
