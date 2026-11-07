#!/usr/bin/env python3
"""sessions.py — walk-forward session calendar and window table (unit 2026-11-07-wf-mac-side-maths, W1).

Reads the 1-minute NQ data file (lines `yyyyMMdd HHmmss;O;H;L;C;V`), builds the
session calendar of values-spec §5 :83 (SETTLED day rule), the 252/63/63 windows
of §5 :82/:84, the per-window holes and early-close counts of §5 :85, and the
CSCV row span of §7 :103-104. Writes Interface 1 (praxis-wf-calendar/1).

Standard library only. Run with `python3 -I`.
"""
import argparse
import datetime as _dt
import hashlib
import json
import os
import sys

SCHEMA = "praxis-wf-calendar/1"
RTH_FIRST = "093100"   # values-spec §5 :83 "at least one bar stamped 09:31:00–16:00:00"
RTH_LAST = "160000"
RANGE = ("2021-03-08", "2026-07-17")  # values-spec §5 :83 baseline range
IS_LEN, OOS_LEN, STEP_LEN = 252, 63, 63  # values-spec §5 :82 (RULED)
CSCV_S = 16  # values-spec §7 :104 (SETTLED)
EARLY_NT8 = ("12:00", "12:15", "14:03")  # values-spec §5 :85 "last bar 12:00 / 12:15 / 14:03"

# values-spec §9 oracle input (c) :233 and results report
# docs/reports/2026-11-01-three-strategy-results.md:144-151.
# INFERRED: the mapping file-last-bar -> NT8-last-bar rests only on the eight rows of
# that table (13:15 -> 12:15 session-close exit, 13:00 -> 12:00, 14:03 -> 14:03).
# The full list of early-close days is UNVERIFIED (§9 (c)). 2023-04-05 (14:03) is
# INFERRED there to be a data gap, not an early close (results report :153).
NT8_MAP = {   # file last RTH bar -> NT8 last bar (cut)
    "13:15": "12:15",
    "13:00": "12:00",
    "14:03": "14:03",
}
# The eight dates whose NT8 cut the results report shows (its table at :144-151,
# OBSERVED there): date -> (file last RTH bar, NT8 session-close exit time).
RESULTS_REPORT_ROWS = {
    "2021-11-26": ("13:15", "12:15"),
    "2023-04-05": ("14:03", "14:03"),
    "2024-07-03": ("13:15", "12:15"),
    "2024-11-29": ("13:15", "12:15"),
    "2024-12-24": ("13:15", "12:15"),
    "2025-01-20": ("13:00", "12:00"),
    "2025-06-19": ("13:00", "12:00"),
    "2025-07-03": ("13:15", "12:15"),
}
GRADE_REPORTED = "REPORTED BY docs/reports/2026-11-01-three-strategy-results.md:144-151 (OBSERVED there)"
GRADE_DATA_GAP_NOTE = ("; the results report INFERS 2023-04-05 is a data gap, not an early close "
                       "(docs/reports/2026-11-01-three-strategy-results.md:153)")
GRADE_RULE = "INFERRED: mapped by rule from the file's last bar"
DATA_GAP_DATE = "2023-04-05"
EARLY_CLOSE_FOOTNOTE = ("Note: the early-close counts include 2023-04-05 (file last bar 14:03), which the "
                        "results report INFERS is a data gap, not an early close "
                        "(docs/reports/2026-11-01-three-strategy-results.md:153); values-spec §5 :85 counts "
                        "last bar 12:00 / 12:15 / 14:03.")
# INFERRED: a session whose file last RTH bar is 16:00 ends at 16:00 in NT8 too
# (RTH template 09:30-16:00; not separately observed per session).
GRADE_FULL = "INFERRED: file last bar 16:00, full session"


class DataError(Exception):
    pass


class NotSettledBySpec(DataError):
    """An early-close day whose NT8 cut the spec does not settle; the CLI exits 3."""

    def __init__(self, what):
        super().__init__("NotSettledBySpec: " + what)


def _nt8_grade(date_iso, last_hm):
    """Grade of an early-close session's nt8_last_bar (last_hm is in NT8_MAP)."""
    row = RESULTS_REPORT_ROWS.get(date_iso)
    if row is not None and row == (last_hm, NT8_MAP[last_hm]):
        grade = GRADE_REPORTED
    else:
        grade = GRADE_RULE
    if date_iso == DATA_GAP_DATE:
        grade += GRADE_DATA_GAP_NOTE
    return grade


def has_data_gap_early_close(cal):
    """True iff the calendar counts 2023-04-05 (NT8 last bar 14:03) as an early close."""
    return any(s.get("date") == DATA_GAP_DATE and s.get("nt8_last_bar") == "14:03"
               for s in cal.get("sessions", []))


def _fmt_time(t):
    """'HHMMSS' -> 'HH:MM' (or 'HH:MM:SS' if seconds non-zero)."""
    s = t[0:2] + ":" + t[2:4]
    return s if t[4:6] == "00" else s + ":" + t[4:6]


def _parse_line(raw, lineno):
    try:
        line = raw.decode("ascii")
    except UnicodeDecodeError:
        raise DataError("line %d: non-ASCII bytes" % lineno)
    if line.endswith("\n"):
        line = line[:-1]
    if line.endswith("\r"):
        line = line[:-1]
    parts = line.split(";")
    if len(parts) != 6:
        raise DataError("line %d: expected 6 ';'-separated fields, got %d: %r" % (lineno, len(parts), line))
    stamp = parts[0]
    if len(stamp) != 15 or stamp[8] != " " or not (stamp[:8].isdigit() and stamp[9:].isdigit()):
        raise DataError("line %d: bad timestamp %r (want 'yyyyMMdd HHmmss')" % (lineno, stamp))
    d, t = stamp[:8], stamp[9:]
    try:
        date = _dt.date(int(d[:4]), int(d[4:6]), int(d[6:8]))
    except ValueError:
        raise DataError("line %d: invalid date %r" % (lineno, d))
    if not (int(t[:2]) < 24 and int(t[2:4]) < 60 and int(t[4:6]) < 60):
        raise DataError("line %d: invalid time %r" % (lineno, t))
    try:
        for f in parts[1:5]:
            float(f)
        int(parts[5])
    except ValueError:
        raise DataError("line %d: non-numeric OHLC/V field in %r" % (lineno, line))
    return date, t


def scan_file(path, start=RANGE[0], end=RANGE[1]):
    """Stream the data file once. Returns dict with source info, the ordered session
    list (values-spec §5 :83 day rule) and weekend counts. Raises DataError on any
    malformed line (with its 1-based line number)."""
    d0 = _dt.date.fromisoformat(start)
    d1 = _dt.date.fromisoformat(end)
    h = hashlib.sha256()
    nbytes = 0
    rth = {}            # date -> [first HHMMSS, last HHMMSS] of bars in 09:31:00-16:00:00
    weekend_all = set()  # weekend dates with an RTH-stamped bar, whole file
    lineno = 0
    with open(path, "rb") as fh:
        for raw in fh:
            lineno += 1
            h.update(raw)
            nbytes += len(raw)
            date, t = _parse_line(raw, lineno)
            if not (RTH_FIRST <= t <= RTH_LAST):
                continue
            if date.weekday() >= 5:
                weekend_all.add(date)
                continue
            if not (d0 <= date <= d1):
                continue
            cur = rth.get(date)
            if cur is None:
                rth[date] = [t, t]
            else:
                if t < cur[0]:
                    cur[0] = t
                if t > cur[1]:
                    cur[1] = t
    if lineno == 0:
        raise DataError("data file is empty: %s" % path)
    sessions = []
    for i, date in enumerate(sorted(rth), 1):
        first, last = rth[date]
        last_hm = _fmt_time(last)
        early = last < RTH_LAST
        if not early:
            nt8, grade = "16:00", GRADE_FULL
        elif last_hm in NT8_MAP:
            nt8, grade = NT8_MAP[last_hm], _nt8_grade(date.isoformat(), last_hm)
        else:
            # values-spec §9 (c) :233 names NT8 cuts only for file last bar 13:15 / 13:00 /
            # 14:03; any other early last bar would drop out of the §5 :85 counts silently.
            raise NotSettledBySpec("early-close day with no NT8 cut mapping: %s %s"
                                   % (date.isoformat(), last_hm))
        sessions.append({"n": i, "date": date.isoformat(), "first_bar": _fmt_time(first),
                         "last_bar": last_hm, "early_close_in_file": early,
                         "nt8_last_bar": nt8, "nt8_last_bar_grade": grade})
    # values-spec §9 oracle input (b) :232 reports 141 weekend dates OBSERVED by the
    # arm (b) code unit. INFERRED (not observed here): that NT8's RTH session template
    # also drops weekend-dated bars. The count below is restricted to the baseline range.
    weekend_in_range = sorted(x for x in weekend_all if d0 <= x <= d1)
    return {"source": {"path": os.path.abspath(path), "bytes": nbytes, "sha256": h.hexdigest()},
            "lines": lineno, "sessions": sessions,
            "weekend_dates_dropped": len(weekend_in_range),
            "weekend_first": weekend_in_range[0].isoformat() if weekend_in_range else None,
            "weekend_dates_whole_file": len(weekend_all)}


def build_windows(N, IS=IS_LEN, OOS=OOS_LEN, STEP=STEP_LEN):
    """values-spec §5 :84. Returns (K, windows, dropped) with windows a list of
    {"k", "is": [a, b], "oos": [c, d]} (1-based session numbers) and dropped =
    [first, last] or None. Partial last window dropped (§5 :82, RULED)."""
    for name, v in (("N", N), ("IS", IS), ("OOS", OOS), ("STEP", STEP)):
        if not isinstance(v, int) or isinstance(v, bool):
            raise ValueError("%s must be int, got %r" % (name, v))
    if IS < 1 or OOS < 1 or STEP < 1:
        raise ValueError("IS, OOS, STEP must be >= 1")
    if N < IS:
        raise ValueError("N=%d < IS=%d: no window possible" % (N, IS))
    K = 0 if N < IS + OOS else (N - IS - OOS) // STEP + 1
    if STEP == OOS:
        assert K == (N - IS) // OOS  # the spec's form, values-spec §5 :84
    windows = []
    for k in range(1, K + 1):
        a = STEP * (k - 1) + 1
        b = a + IS - 1
        windows.append({"k": k, "is": [a, b], "oos": [b + 1, b + OOS]})
    last_used = windows[-1]["oos"][1] if windows else 0
    dropped = [last_used + 1, N] if last_used < N else None
    return K, windows, dropped


def cscv_rows(last_oos, S=CSCV_S):
    """values-spec §7 :103: the windows' span s1..last_oos trimmed by its oldest
    sessions so that the row count is S * floor(last_oos / S)."""
    block = last_oos // S
    if block < 1:
        raise ValueError("span %d too short for S=%d" % (last_oos, S))
    return [last_oos - S * block + 1, last_oos], block


def _holes(d_first, d_last, session_dates):
    """Mon-Fri dates in [d_first, d_last] that are not sessions (values-spec §5 :85)."""
    d = _dt.date.fromisoformat(d_first)
    e = _dt.date.fromisoformat(d_last)
    n = 0
    one = _dt.timedelta(days=1)
    while d <= e:
        if d.weekday() < 5 and d.isoformat() not in session_dates:
            n += 1
        d += one
    return n


def build_calendar(path, start=RANGE[0], end=RANGE[1], IS=IS_LEN, OOS=OOS_LEN, STEP=STEP_LEN, info=None):
    """Interface 1 dict, exactly the contract's keys. If `info` (a dict) is given it is
    filled with diagnostics not in Interface 1 (weekend_first, whole-file weekend count, lines)."""
    scan = scan_file(path, start, end)
    if info is not None:
        info.update({"weekend_first": scan["weekend_first"],
                     "weekend_dates_whole_file": scan["weekend_dates_whole_file"],
                     "lines": scan["lines"]})
    sessions = scan["sessions"]
    N = len(sessions)
    if N < IS + OOS:
        raise DataError("N=%d sessions gives K=0 full windows (need >= %d)" % (N, IS + OOS))
    K, wins, dropped = build_windows(N, IS, OOS, STEP)
    if K < 1:
        raise DataError("N=%d sessions gives K=0 full windows (need >= %d)" % (N, IS + OOS))
    dates = [s["date"] for s in sessions]
    dset = set(dates)
    early = [s["nt8_last_bar"] in EARLY_NT8 for s in sessions]
    for w in wins:
        a, b = w["is"]
        c, d = w["oos"]
        w["is_dates"] = [dates[a - 1], dates[b - 1]]
        w["oos_dates"] = [dates[c - 1], dates[d - 1]]
        w["is_holes"] = _holes(dates[a - 1], dates[b - 1], dset)
        w["oos_holes"] = _holes(dates[c - 1], dates[d - 1], dset)
        w["is_early_close"] = sum(early[a - 1:b])
        w["oos_early_close"] = sum(early[c - 1:d])
    last_oos = wins[-1]["oos"][1]
    rows, block = cscv_rows(last_oos)
    return {
        "schema": SCHEMA,
        "source": scan["source"],
        "rule": {"rth_first": "09:31:00", "rth_last": "16:00:00", "weekdays": "Mon-Fri",
                 "range": [start, end], "IS": IS, "OOS": OOS, "STEP": STEP},
        "N": N,
        "sessions": sessions,
        "windows": wins,
        "K": K,
        "oos_sessions": K * OOS,
        "dropped": dropped,
        "dropped_dates": [dates[dropped[0] - 1], dates[dropped[1] - 1]] if dropped else None,
        "cscv_rows": rows,
        "cscv_S": CSCV_S,
        "cscv_block": block,
        "weekend_dates_dropped": scan["weekend_dates_dropped"],
    }


def load_calendar(path):
    with open(path, "r", encoding="utf-8") as fh:
        cal = json.load(fh)
    if cal.get("schema") != SCHEMA:
        raise DataError("%s: schema %r, want %r" % (path, cal.get("schema"), SCHEMA))
    if len(cal["sessions"]) != cal["N"]:
        raise DataError("%s: N=%d but %d sessions" % (path, cal["N"], len(cal["sessions"])))
    for i, s in enumerate(cal["sessions"], 1):
        if s["n"] != i:
            raise DataError("%s: session index %d has n=%r" % (path, i, s["n"]))
    return cal


def date_to_session(cal):
    return {s["date"]: s["n"] for s in cal["sessions"]}


def format_table(cal, info=None):
    info = info or {}
    S = cal["sessions"]
    out = []
    p = out.append
    p("source: %s  bytes=%d  sha256=%s" % (cal["source"]["path"], cal["source"]["bytes"], cal["source"]["sha256"]))
    p("N = %d" % cal["N"])
    for n in (1, 16, cal["N"]):
        if n <= cal["N"]:
            p("s%d = %s" % (n, S[n - 1]["date"]))
    p("K = %d   OOS sessions = %d" % (cal["K"], cal["oos_sessions"]))
    if cal["dropped"]:
        d = cal["dropped"]
        p("dropped = s%d-s%d (%d sessions) = %s -> %s" % (d[0], d[1], d[1] - d[0] + 1, cal["dropped_dates"][0], cal["dropped_dates"][1]))
    else:
        p("dropped = none")
    r = cal["cscv_rows"]
    p("cscv rows = s%d-s%d (%d = %d x %d)" % (r[0], r[1], r[1] - r[0] + 1, cal["cscv_S"], cal["cscv_block"]))
    p("weekend dates with a 09:31-16:00 bar, in range (dropped) = %d; first = %s; whole file = %s"
      % (cal["weekend_dates_dropped"], info.get("weekend_first", "n/a"), info.get("weekend_dates_whole_file", "n/a")))
    p("")
    p("| k | IS sessions | IS dates | OOS sessions | OOS dates | IS holes | OOS holes | IS early | OOS early |")
    p("|---|---|---|---|---|---|---|---|---|")
    for w in cal["windows"]:
        p("| %d | s%d-s%d | %s -> %s | s%d-s%d | %s -> %s | %d | %d | %d | %d |" % (
            w["k"], w["is"][0], w["is"][1], w["is_dates"][0], w["is_dates"][1],
            w["oos"][0], w["oos"][1], w["oos_dates"][0], w["oos_dates"][1],
            w["is_holes"], w["oos_holes"], w["is_early_close"], w["oos_early_close"]))
    if has_data_gap_early_close(cal):
        p(EARLY_CLOSE_FOOTNOTE)
    p("")
    ec = [s for s in S if s["early_close_in_file"]]
    p("early_close_in_file sessions: %d" % len(ec))
    p("| n | date | first bar | file last bar | nt8_last_bar | grade |")
    p("|---|---|---|---|---|---|")
    for s in ec:
        p("| %d | %s | %s | %s | %s | %s |" % (s["n"], s["date"], s["first_bar"], s["last_bar"],
                                             s["nt8_last_bar"] if s["nt8_last_bar"] else "null", s["nt8_last_bar_grade"]))
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Build the walk-forward session calendar (values-spec §5) and write "
                    "Interface 1 (praxis-wf-calendar/1) JSON.")
    ap.add_argument("--data", required=True, help="1-minute data file (yyyyMMdd HHmmss;O;H;L;C;V), read-only")
    ap.add_argument("--out", required=True, help="output calendar JSON path")
    ap.add_argument("--print-table", action="store_true", help="print N, key sessions, K, windows and early-close list")
    a = ap.parse_args(argv)
    if not os.path.isfile(a.data):
        print("sessions.py: ERROR: data file not found: %s" % a.data, file=sys.stderr)
        return 2
    try:
        info = {}
        cal = build_calendar(a.data, info=info)
    except NotSettledBySpec as e:
        print("sessions.py: ERROR: %s" % e, file=sys.stderr)
        return 3
    except DataError as e:
        print("sessions.py: ERROR: %s" % e, file=sys.stderr)
        return 1
    tmp = a.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(cal, fh, sort_keys=True, indent=1)
        fh.write("\n")
    os.replace(tmp, a.out)
    if a.print_table:
        sys.stdout.write(format_table(cal, info))
    return 0


if __name__ == "__main__":
    sys.exit(main())
