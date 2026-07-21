#!/usr/bin/env python3
# b2_stitch.py — Praxis_build-6bw (b2-stitch)
# Continuous NQ 1-min series builder: Vol/OI-crossover roll + Difference
# (Panama / back-adjusted) construction, built OUTSIDE NinjaTrader in Python
# per DECISION D-2026-07-17-A. Roll convention is TRADER-LOCKED
# (DECISIONS.md 2026-07-15): Volume/OI-crossover roll trigger + Difference
# back-adjustment. RATIO construction is explicitly rejected (the Block-2
# breakout strategy reads ABSOLUTE point distances — spec §2.2).
#
# SCOPE: consumes the per-contract raw export
#   ~/praxis-signals/b2-data/raw/  ->  NQ-<MM-YY>_1min.csv + NQ-<MM-YY>_daily.csv
# (44 files = 22 contracts x 2), computes Vol/OI-crossover roll dates from the
# DAILY series (spec §3), applies additive Difference offsets at each seam, and
# emits (a) ONE stitched continuous 1-min CSV and (b) a validation report
# against b2-data spec §4 (bar-count medians, TZ/DST checks, gap analysis,
# roll-seam listing, dedup).
#
# BUILD-AHEAD-OF-DATA: raw/ is empty until the VM coworker's export lands. Run
# on real absent data -> STATUS: VALIDATION-PENDING (exit 3). The bundled
# self-test (scripts/tests/b2-stitch-selftest.py) proves the pipeline end-to-end
# on a synthetic fixture with a known crossover.
#
# OI GATE (critical, D-2026-07-17-A OPEN RISK): if a daily series needed for a
# roll decision is missing Open Interest, the tool REFUSES and emits OI_BLANK
# (exit 2). It NEVER silently falls back to a volume-only crossover — that
# fallback is a documented deviation needing trader sign-off + a DECISIONS
# append that DOES NOT YET EXIST. --allow-volume-only exists only so an
# authorized future run (post sign-off) can proceed, and prints a loud banner.
#
# Dependencies: Python 3 standard library ONLY (csv, datetime, statistics,
# json, os, sys). No pandas/numpy — consistent with scripts/b2data_raw_validate.py
# and avoids a new repo dependency (pandas is not installed on this host).
#
# Exit codes: 0 ok | 1 error/validation-fail | 2 OI_BLANK refusal
#             3 VALIDATION-PENDING (no raw data yet) | 64 usage
import csv
import json
import os
import statistics
import sys
from datetime import datetime, date

# --- The 22-contract expected set + chronological order -----------------------
# NQ quarterly cycle H/M/U/Z (Mar/Jun/Sep/Dec). Same set as the raw validator.
CONTRACTS = [
    "06-21", "09-21", "12-21", "03-22", "06-22", "09-22", "12-22",
    "03-23", "06-23", "09-23", "12-23", "03-24", "06-24", "09-24",
    "12-24", "03-25", "06-25", "09-25", "12-25", "03-26", "06-26", "09-26",
]
_MONTH_ORD = {"03": 1, "06": 2, "09": 3, "12": 4}

OI_NONZERO_FRACTION = 0.5  # OI "present" if non-zero for a MAJORITY of daily rows

# --- Default schema (criterion 3): logical field -> header aliases -------------
# Real coworker export headers are UNKNOWN. Column resolution is
# schema-configurable; override the whole map with --schema PATH (JSON). Matching
# is normalized (case/space/underscore-insensitive) with exact->substring
# precedence, then a documented positional fallback. See resolve_column().
DEFAULT_SCHEMA = {
    "daily": {
        "date":          ["date", "time", "timestamp", "datetime"],
        "open":          ["open", "o"],
        "high":          ["high", "h"],
        "low":           ["low", "l"],
        "close":         ["close", "last", "settle", "c"],
        "volume":        ["volume", "vol", "v"],
        "open_interest": ["open interest", "openinterest", "openint", "oi", "o.i."],
    },
    "minute": {
        "timestamp":     ["timestamp", "datetime", "date time", "time"],
        "date":          ["date"],
        "open":          ["open", "o"],
        "high":          ["high", "h"],
        "low":           ["low", "l"],
        "close":         ["close", "last", "c"],
        "volume":        ["volume", "vol", "v"],
    },
    # Positional layouts for HEADER-LESS files (criterion 2). Index -> logical
    # field. The real NinjaTrader export is semicolon-delimited with NO header:
    #   daily  = YYYYMMDD;open;high;low;close;volume            (6 cols, NO OI)
    #   minute = "YYYYMMDD HHMMSS";open;high;low;close;volume   (combined ts)
    # A 6-col daily therefore has NO open_interest column at all -> oi_present()
    # is False -> the volume-only crossover path (D-2026-07-21-A). A 7-col daily
    # (if a future export adds it) maps its trailing column to open_interest.
    "daily_positional":  ["date", "open", "high", "low", "close", "volume", "open_interest"],
    "minute_positional": ["timestamp", "open", "high", "low", "close", "volume"],
}

_DT_FORMATS = (
    "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M",
    "%m/%d/%Y %H:%M:%S", "%m/%d/%Y %H:%M", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M",
    # NinjaTrader combined field-0 timestamp: "YYYYMMDD HHMMSS" (space/ T inside
    # the single column). Layout CONFIRMED against the real b2-data export
    # (Praxis_build-8zd), no longer a guess.
    "%Y%m%d %H%M%S", "%Y%m%dT%H%M%S", "%Y%m%d%H%M%S",
)
_DATE_FORMATS = ("%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y", "%d/%m/%Y", "%Y%m%d")


# ---------------------------------------------------------------------------- #
#  Errors                                                                       #
# ---------------------------------------------------------------------------- #
class OIBlankError(Exception):
    """Raised when a daily series required for a roll decision lacks Open Interest."""


class StitchError(Exception):
    """Any other fatal construction error (missing crossover, no data, ...)."""


# ---------------------------------------------------------------------------- #
#  Schema / parsing helpers                                                     #
# ---------------------------------------------------------------------------- #
def _norm(s):
    return (s or "").strip().lower().replace(" ", "").replace("_", "").replace("-", "")


def load_schema(path):
    """Return the schema dict. path=None -> DEFAULT_SCHEMA (deep-copied)."""
    base = json.loads(json.dumps(DEFAULT_SCHEMA))
    if not path:
        return base
    with open(path, "r") as fh:
        override = json.load(fh)
    for section in ("daily", "minute"):
        if section in override:
            base.setdefault(section, {}).update(override[section])
    # positional layouts (header-less files) are wholesale-replaced if provided
    for key in ("daily_positional", "minute_positional"):
        if key in override:
            base[key] = override[key]
    return base


def resolve_column(header, aliases, fallback_index=None, exact_only=False):
    """Resolve one logical field to a column index in `header`.
    Precedence: (1) exact normalized equality; (2) alias substring of header or
    header substring of alias (normalized); (3) documented positional fallback.
    Returns (index, how) or (None, 'unresolved').

    exact_only=True stops after (1) and skips the fallback — used for HEADER-LESS
    files whose header we SYNTHESIZE from canonical names (see _positional_header).
    Substring matching there is both unnecessary and harmful: e.g. the canonical
    'open' column is a substring of the open_interest alias 'openinterest', which
    would otherwise mis-map OPEN price into the OI slot and mask the OI-absent
    state that drives the volume-only path."""
    norm_hdr = [_norm(h) for h in header]
    norm_alias = [_norm(a) for a in aliases]
    # (1) exact
    for i, nh in enumerate(norm_hdr):
        if nh in norm_alias:
            return i, "exact:%s" % header[i].strip()
    if exact_only:
        return None, "unresolved"
    # (2) substring either direction (guard against empty)
    for i, nh in enumerate(norm_hdr):
        if not nh:
            continue
        for na in norm_alias:
            if not na:
                continue
            if na in nh or nh in na:
                return i, "substr:%s" % header[i].strip()
    # (3) positional fallback (documented; caller decides if acceptable)
    if fallback_index is not None and 0 <= fallback_index < len(header):
        return fallback_index, "fallback-col%d" % fallback_index
    return None, "unresolved"


def _parse_dt(s):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in _DT_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    # date-only -> midnight
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def _parse_date(s):
    dt = _parse_dt(s)
    return dt.date() if dt else None


def _to_float(s):
    s = (s or "").strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _sniff_delimiter(sample_line):
    """Pick the delimiter from a sample data line. Real NinjaTrader exports are
    SEMICOLON-delimited; the bundled comma fixtures must still parse. Prefer
    semicolon, then tab, else comma."""
    if ";" in sample_line:
        return ";"
    if "\t" in sample_line:
        return "\t"
    return ","


def _looks_like_header(row):
    """True iff `row` carries a textual header label (a cell that is neither a
    number nor a parseable date/timestamp). Real header-less data rows are all
    numeric / date-like, so this cleanly separates the two export shapes without
    a per-file flag."""
    for c in row:
        s = (c or "").strip()
        if s == "":
            continue
        if _to_float(s) is not None:
            continue
        if _parse_dt(s) is not None:
            continue
        return True  # a non-numeric, non-date token -> this is a header row
    return False


def _read_csv(path):
    """Return (header, data, has_header).

    Delimiter is sniffed per file (semicolon / tab / comma) so real
    semicolon-delimited NinjaTrader exports AND the comma fixtures both parse.
    Header presence is detected from the first data row (criterion 2): a
    header-less file returns header=None and has_header=False — callers then
    apply a positional schema."""
    with open(path, "r", newline="") as fh:
        text = fh.read()
    lines = text.splitlines()
    first = next((ln for ln in lines if ln.strip()), "")
    if not first:
        return None, [], False
    delim = _sniff_delimiter(first)
    rows = [r for r in csv.reader(lines, delimiter=delim) if any(c.strip() for c in r)]
    if not rows:
        return None, [], False
    if _looks_like_header(rows[0]):
        return rows[0], rows[1:], True
    return None, rows, False


def _positional_header(schema, section, ncols):
    """Synthesize a canonical header for a header-less file from the section's
    positional layout, sized to the actual column count. Extra columns get
    inert 'colN' names so they resolve to nothing (never to OI/close by
    accident)."""
    layout = schema.get(section + "_positional", [])
    return [layout[i] if i < len(layout) else "col%d" % i for i in range(ncols)]


# ---------------------------------------------------------------------------- #
#  Loaders                                                                       #
# ---------------------------------------------------------------------------- #
def read_daily(path, schema):
    """Return list of dicts {date, close, volume, oi, oi_col_how, oi_resolved}.
    OI resolution falls back to the LAST column (documented) — a blank/zero
    fallback column is still caught by the presence check, so it can never
    silently pass volume-only."""
    header, data, has_header = _read_csv(path)
    if not data:
        raise StitchError("empty/unreadable daily file: %s" % path)
    if not has_header:
        header = _positional_header(schema, "daily", len(data[0]))
    sd = schema["daily"]
    # Header-LESS files use a synthesized canonical header -> resolve by EXACT
    # name only (no substring/fallback). Header-bearing files keep the full
    # exact->substring->fallback resolution for unknown real column names.
    xo = not has_header
    i_date, _ = resolve_column(header, sd["date"], fallback_index=(None if xo else 0), exact_only=xo)
    i_close, _ = resolve_column(header, sd["close"], exact_only=xo)
    i_vol, _ = resolve_column(header, sd["volume"], exact_only=xo)
    # OI: with an UNKNOWN real header we fall back to the last column (a
    # blank/zero fallback is still caught by oi_present). A header-LESS file has
    # a KNOWN positional layout — a 6-col daily has no OI column, so exact_only
    # resolution returns None (OI absent) -> oi_present() False -> volume-only
    # path. No fallback there (it would mask the OI-absent state).
    oi_fallback = (len(header) - 1) if has_header else None
    i_oi, oi_how = resolve_column(header, sd["open_interest"],
                                  fallback_index=oi_fallback, exact_only=xo)
    oi_resolved = (i_oi is not None) and not oi_how.startswith("fallback")
    if i_date is None or i_close is None or i_vol is None:
        raise StitchError("daily %s: could not resolve date/close/volume columns "
                          "(header=%s)" % (os.path.basename(path), header))
    out = []
    for r in data:
        d = _parse_date(r[i_date]) if i_date < len(r) else None
        if d is None:
            continue
        out.append({
            "date": d,
            "close": _to_float(r[i_close]) if i_close < len(r) else None,
            "volume": _to_float(r[i_vol]) if i_vol < len(r) else None,
            "oi": _to_float(r[i_oi]) if (i_oi is not None and i_oi < len(r)) else None,
        })
    out.sort(key=lambda x: x["date"])
    return out, oi_how, oi_resolved


def read_minute(path, schema):
    """Return list of dicts {ts(datetime), o,h,l,c,v} sorted by ts."""
    header, data, has_header = _read_csv(path)
    if not data:
        raise StitchError("empty/unreadable minute file: %s" % path)
    if not has_header:
        header = _positional_header(schema, "minute", len(data[0]))
    sm = schema["minute"]
    xo = not has_header  # header-less -> exact-only canonical resolution
    i_ts, _ = resolve_column(header, sm["timestamp"], exact_only=xo)
    i_date, _ = resolve_column(header, sm["date"], exact_only=xo)
    i_o, _ = resolve_column(header, sm["open"], exact_only=xo)
    i_h, _ = resolve_column(header, sm["high"], exact_only=xo)
    i_l, _ = resolve_column(header, sm["low"], exact_only=xo)
    i_c, _ = resolve_column(header, sm["close"], exact_only=xo)
    i_v, _ = resolve_column(header, sm["volume"], exact_only=xo)
    if i_c is None or (i_ts is None and i_date is None):
        raise StitchError("minute %s: could not resolve timestamp/close columns "
                          "(header=%s)" % (os.path.basename(path), header))
    out = []
    for r in data:
        ts = None
        if i_ts is not None and i_ts < len(r):
            ts = _parse_dt(r[i_ts])
        if ts is None and i_date is not None and i_date < len(r):
            ts = _parse_dt(r[i_date])
        if ts is None:
            continue
        out.append({
            "ts": ts,
            "o": _to_float(r[i_o]) if (i_o is not None and i_o < len(r)) else None,
            "h": _to_float(r[i_h]) if (i_h is not None and i_h < len(r)) else None,
            "l": _to_float(r[i_l]) if (i_l is not None and i_l < len(r)) else None,
            "c": _to_float(r[i_c]) if i_c < len(r) else None,
            "v": _to_float(r[i_v]) if (i_v is not None and i_v < len(r)) else None,
        })
    out.sort(key=lambda x: x["ts"])
    return out


# ---------------------------------------------------------------------------- #
#  OI gate                                                                       #
# ---------------------------------------------------------------------------- #
def oi_present(daily_rows):
    """True iff a non-zero OI exists for a MAJORITY of rows (mirrors the raw
    validator's OI_NONZERO_FRACTION convention)."""
    if not daily_rows:
        return False
    n = len(daily_rows)
    nonzero = sum(1 for r in daily_rows if r["oi"] not in (None, 0.0))
    return (nonzero / n) > OI_NONZERO_FRACTION


# ---------------------------------------------------------------------------- #
#  Roll-date engine (criterion 1 / spec §3)                                      #
# ---------------------------------------------------------------------------- #
def compute_roll_date(front_daily, back_daily, confirm=1, allow_volume_only=False):
    """Vol/OI-crossover roll date between an adjacent (front, back) contract pair.

    RULE (spec §3, D-2026-07-15 lock): scanning the COMMON daily dates in
    chronological order, the roll date is the FIRST date on which the back
    month's volume AND open interest BOTH STRICTLY exceed the front month's,
    and that joint condition HOLDS for `confirm` consecutive common dates
    (default 1 = the plain single-day reading of the spec).

    TIE-BREAK / determinism:
      * STRICT greater-than on both legs — an exact tie does NOT trigger the roll.
      * Earliest qualifying common date wins.
      * Only dates present in BOTH dailies are considered (no interpolation).
      * If OI is absent, this raises OIBlankError unless allow_volume_only=True,
        in which case it rolls on the volume-only crossover and the caller must
        emit the documented-deviation banner.

    Returns dict: {roll_date, trigger, front_vol, back_vol, front_oi, back_oi}."""
    have_oi = oi_present(front_daily) and oi_present(back_daily)
    if not have_oi and not allow_volume_only:
        raise OIBlankError("roll pair missing Open Interest — refuse (OI_BLANK)")

    fb = {r["date"]: r for r in back_daily}
    common = [r for r in front_daily if r["date"] in fb]
    common.sort(key=lambda r: r["date"])

    run = 0
    first_qual = None
    for fr in common:
        d = fr["date"]
        br = fb[d]
        vol_ok = (br["volume"] is not None and fr["volume"] is not None
                  and br["volume"] > fr["volume"])
        if have_oi:
            oi_ok = (br["oi"] is not None and fr["oi"] is not None
                     and br["oi"] > fr["oi"])
            cond = vol_ok and oi_ok
        else:
            cond = vol_ok  # volume-only (authorized deviation only)
        if cond:
            if run == 0:
                first_qual = fr
            run += 1
            if run >= confirm:
                trig = "vol+oi crossover" if have_oi else "VOLUME-ONLY (deviation)"
                return {
                    "roll_date": first_qual["date"],
                    "trigger": trig,
                    "front_vol": first_qual["volume"], "back_vol": fb[first_qual["date"]]["volume"],
                    "front_oi": first_qual["oi"], "back_oi": fb[first_qual["date"]]["oi"],
                    "oi_used": have_oi,
                }
        else:
            run = 0
            first_qual = None

    # No strict crossover anywhere in the common overlap. Under the AUTHORIZED
    # volume-only deviation only (D-2026-07-21-A), fall back to the last common
    # date as the roll seam. Rationale (Praxis_build-8zd, real-data finding): the
    # NinjaTrader export trims each contract's DAILY series to ~1-3 days past its
    # own roll, so the earliest (2-day) overlaps end on the day the back month is
    # still a hair UNDER the front — the true crossover lands on the first
    # UN-shared day, for which there is no front row. The last shared date is
    # therefore the effective front/back boundary (front daily data ends there),
    # so we roll on it. This fires ONLY when allow_volume_only is set AND no
    # strict crossover exists; the OI-present path (self-test Case A) and every
    # genuine crossover (17 of 21 real seams, self-test Case D) are unaffected.
    # The Difference/Panama offset math is untouched — the seam gap is still
    # taken at this roll date.
    if allow_volume_only and common:
        last = common[-1]
        return {
            "roll_date": last["date"],
            "trigger": "VOLUME-ONLY boundary (no crossover in trimmed overlap)",
            "front_vol": last["volume"], "back_vol": fb[last["date"]]["volume"],
            "front_oi": last["oi"], "back_oi": fb[last["date"]]["oi"],
            "oi_used": False,
        }
    raise StitchError("no vol/OI crossover found in the common daily window "
                      "(front %s..%s) — cannot roll" %
                      (common[0]["date"] if common else "?",
                       common[-1]["date"] if common else "?"))


def _close_on_or_before(daily_rows, d):
    """Daily close on date d, else the nearest prior daily close (<= d)."""
    best = None
    for r in daily_rows:
        if r["date"] <= d and r["close"] is not None:
            if best is None or r["date"] > best["date"]:
                best = r
    return best["close"] if best else None


# ---------------------------------------------------------------------------- #
#  Difference (Panama) back-adjustment (criterion 2 / spec §2)                    #
# ---------------------------------------------------------------------------- #
def build_offsets(codes, roll_dates, daily_by_code):
    """Cumulative ADDITIVE Difference offsets (Panama), one per contract.

    codes are chronological C1..Cn; roll_dates[i] is the C_i -> C_{i+1} seam.
    The NEWEST contract Cn is the anchor (offset 0, unadjusted). Walking
    BACKWARD, each earlier contract is lifted by the raw contract spread at its
    roll seam so the seam has NO artificial jump:

        gap_i   = close_{C_{i+1}}(R_i) - close_{C_i}(R_i)      (daily close ref)
        off(Cn) = 0
        off(C_i)= off(C_{i+1}) + gap_i

    ADDITIVE (points), NOT ratio — preserves absolute point distances (spec §2.2).
    Returns (offsets dict {code: float}, seams list of per-seam diagnostics)."""
    n = len(codes)
    offsets = {codes[-1]: 0.0}
    seams = []
    # iterate seams from newest to oldest so offsets accumulate backward
    for i in range(n - 2, -1, -1):
        fcode, bcode = codes[i], codes[i + 1]
        rd = roll_dates[i]
        fclose = _close_on_or_before(daily_by_code[fcode], rd)
        bclose = _close_on_or_before(daily_by_code[bcode], rd)
        if fclose is None or bclose is None:
            raise StitchError("seam %s->%s @ %s: missing daily close for offset"
                              % (fcode, bcode, rd))
        gap = bclose - fclose
        offsets[fcode] = offsets[bcode] + gap
        seams.append({
            "roll_date": rd, "front": fcode, "back": bcode,
            "front_close": fclose, "back_close": bclose,
            "raw_gap": gap, "offset_front": offsets[fcode], "offset_back": offsets[bcode],
        })
    seams.sort(key=lambda s: s["roll_date"])
    return offsets, seams


def stitch(codes, roll_dates, offsets, minute_by_code):
    """Concatenate per-contract 1-min bars into ONE continuous series.

    Segment window for C_i is [prev_roll, this_roll): a bar with date < R_i uses
    C_i, a bar with date >= R_i uses C_{i+1} (clean, non-overlapping seams). Each
    segment's O/H/L/C is shifted by offsets[code]; volume passes through. Output
    is sorted by timestamp and de-duplicated on identical timestamps.

    Returns (rows, dedup_count). Each row: {ts, o, h, l, c, v, src}."""
    n = len(codes)
    rows = []
    for i, code in enumerate(codes):
        lo = roll_dates[i - 1] if i > 0 else date.min
        hi = roll_dates[i] if i < n - 1 else date.max
        off = offsets[code]
        for b in minute_by_code.get(code, []):
            bd = b["ts"].date()
            in_window = (bd >= lo) and (bd < hi if hi is not date.max else True)
            if i == 0:
                in_window = (bd < hi)
            if not in_window:
                continue
            rows.append({
                "ts": b["ts"],
                "o": None if b["o"] is None else b["o"] + off,
                "h": None if b["h"] is None else b["h"] + off,
                "l": None if b["l"] is None else b["l"] + off,
                "c": None if b["c"] is None else b["c"] + off,
                "v": b["v"], "src": code,
            })
    rows.sort(key=lambda r: r["ts"])
    # dedup identical timestamps (keep first); spec §4.4 zero-duplicate policy
    deduped = []
    seen = set()
    dupes = 0
    for r in rows:
        if r["ts"] in seen:
            dupes += 1
            continue
        seen.add(r["ts"])
        deduped.append(r)
    return deduped, dupes


# ---------------------------------------------------------------------------- #
#  Validation report (criterion 5 / spec §4)                                     #
# ---------------------------------------------------------------------------- #
def _in_rth(ts):
    m = ts.hour * 60 + ts.minute
    return (9 * 60 + 30) <= m < (16 * 60)  # 09:30 <= t < 16:00


def _in_break(ts):
    return ts.hour == 17  # 17:00-17:59 ET daily maintenance break


def validation_report(rows, seams, dupes, label="REAL"):
    """Build the spec §4 validation markdown + a machine SUMMARY line.
    On a SYNTHETIC fixture the bar-count medians / depth are informational
    (the fixture is tiny by design); on REAL data the acceptance gate is graded,
    and any not-yet-satisfiable item is marked VALIDATION-PENDING."""
    lines, checks = [], []

    def add_check(name, status, detail):
        checks.append((name, status, detail))

    # --- §4.1 bar-count medians per session -----------------------------------
    per_day_rth, per_day_all, break_bars = {}, {}, 0
    for r in rows:
        d = r["ts"].date()
        per_day_all[d] = per_day_all.get(d, 0) + 1
        if _in_rth(r["ts"]):
            per_day_rth[d] = per_day_rth.get(d, 0) + 1
        if _in_break(r["ts"]):
            break_bars += 1
    rth_med = statistics.median(per_day_rth.values()) if per_day_rth else 0
    eth_med = statistics.median(per_day_all.values()) if per_day_all else 0
    n_days = len(per_day_all)
    if label == "REAL":
        rth_ok = "PASS" if abs(rth_med - 390) <= 3 else ("PENDING" if not rows else "FAIL")
        eth_ok = "PASS" if 1350 <= eth_med <= 1380 else ("PENDING" if not rows else "FAIL")
    else:
        rth_ok = eth_ok = "INFO"
    add_check("§4.1 RTH median == 390", rth_ok, "measured=%g over %d days" % (rth_med, n_days))
    add_check("§4.1 ETH median in [1350,1380]", eth_ok, "measured=%g over %d days" % (eth_med, n_days))
    add_check("§1.1 depth >= ~1008 trading days", "PASS" if n_days >= 1008 else ("INFO" if label != "REAL" else "PENDING"),
              "trading days = %d" % n_days)

    # --- §4.2 TZ / DST + maintenance break ------------------------------------
    add_check("§4.2 17:00-18:00 maintenance break empty", "PASS" if break_bars == 0 else "FAIL",
              "bars inside 17:00-17:59 = %d" % break_bars)
    add_check("§4.2 DST boundary hold (both flips/yr)",
              "INFO" if label != "REAL" else "PENDING",
              "requires multi-year real series; not gradable on fixture")

    # --- §4.3 gap analysis ----------------------------------------------------
    gaps = []
    for i in range(1, len(rows)):
        prev, cur = rows[i - 1], rows[i]
        if prev["ts"].date() != cur["ts"].date():
            continue  # cross-day boundary (weekend/holiday) is benign
        delta = (cur["ts"] - prev["ts"]).total_seconds() / 60.0
        if delta > 1.0:
            # 17:00-18:00 break is benign; flag the rest
            benign = prev["ts"].hour == 16 or _in_break(prev["ts"]) or _in_break(cur["ts"])
            if not benign:
                gaps.append((prev["ts"], cur["ts"], delta))
    add_check("§4.3 anomalous intra-session gaps", "PASS" if not gaps else "FLAG",
              "%d anomalous gap(s)" % len(gaps))

    # --- §4.4 dedup / monotonic ----------------------------------------------
    mono = all(rows[i]["ts"] <= rows[i + 1]["ts"] for i in range(len(rows) - 1))
    add_check("§4.4 monotonic non-decreasing ts", "PASS" if mono else "FAIL",
              "%d rows" % len(rows))
    add_check("§4.4 zero duplicate timestamps", "PASS" if dupes == 0 else "PASS(deduped)",
              "removed %d duplicate(s)" % dupes)

    # --- §3 roll-seam listing -------------------------------------------------
    add_check("§3 roll count ~4/yr (~20 over 5yr)", "INFO",
              "%d seam(s) in this series" % len(seams))

    # overall
    grade = [s for _, s, _ in checks]
    if label != "REAL":
        overall = "SYNTHETIC-FIXTURE (informational — real-data gate is VALIDATION-PENDING)"
    elif "FAIL" in grade:
        overall = "FAIL"
    elif "PENDING" in grade:
        overall = "VALIDATION-PENDING"
    else:
        overall = "PASS"

    fpass = sum(1 for g in grade if g == "PASS")
    summary = ("SUMMARY b2-stitch label=%s bars=%d days=%d seams=%d dupes=%d "
               "gaps=%d overall=%s") % (label, len(rows), n_days, len(seams),
                                        dupes, len(gaps), overall.split()[0])

    # markdown
    lines.append(summary)
    lines.append("")
    lines.append("# Continuous NQ 1-min — Validation Report (b2-data spec §4)")
    lines.append("")
    n_boundary = sum(1 for s in seams if "boundary" in s.get("trigger", ""))
    n_cross = len(seams) - n_boundary
    if n_boundary:
        constr = ("volume-crossover roll (%d of %d seams) + %d no-overlap "
                  "BOUNDARY-fallback seam(s) (volume-only, D-2026-07-21-A) + "
                  "Difference (Panama) back-adjustment" % (n_cross, len(seams), n_boundary))
    else:
        constr = ("Vol/OI-crossover roll + Difference (Panama) back-adjustment "
                  "(D-2026-07-15 lock, D-2026-07-17-A path)")
    lines.append("**Dataset:** %s  ·  **Construction:** %s" % (label, constr))
    lines.append("**Overall:** %s" % overall)
    if label == "REAL" and not rows:
        lines.append("")
        lines.append("> **STATUS: VALIDATION-PENDING** — no stitched bars (raw/ not yet "
                     "landed). Re-run after the VM export lands and the raw-landing "
                     "battery (b2data_raw_validate.py) reports READY.")
    lines.append("")
    lines.append("_Run: %sZ_" % datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"))
    lines.append("")
    lines.append("## §4 acceptance checks")
    lines.append("")
    lines.append("| Check | Status | Detail |")
    lines.append("|---|---|---|")
    for name, status, detail in checks:
        lines.append("| %s | %s | %s |" % (name, status, detail))
    lines.append("")
    lines.append("## §3 roll seams")
    lines.append("")
    if seams:
        lines.append("| # | Roll date | Front→Back | Front close | Back close | Raw gap | Front offset | Roll trigger |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for k, s in enumerate(seams, 1):
            trig = s.get("trigger", "?")
            marker = "⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A)" if "boundary" in trig else trig
            lines.append("| %d | %s | %s→%s | %g | %g | %+.2f | %+.2f | %s |" % (
                k, s["roll_date"], s["front"], s["back"],
                s["front_close"], s["back_close"], s["raw_gap"], s["offset_front"], marker))
    else:
        lines.append("_(no seams — single contract or no data)_")
    lines.append("")
    if gaps:
        lines.append("## §4.3 anomalous gaps")
        lines.append("")
        for a, b, dm in gaps[:50]:
            lines.append("- %s → %s (%.0f min)" % (a, b, dm))
        lines.append("")
    return "\n".join(lines) + "\n", summary, overall


# ---------------------------------------------------------------------------- #
#  Pipeline                                                                      #
# ---------------------------------------------------------------------------- #
def discover_contracts(raw_dir):
    """Return chronological list of contract codes that have BOTH files present."""
    found = []
    for code in sorted(CONTRACTS, key=lambda c: (int(c.split("-")[1]), _MONTH_ORD[c.split("-")[0]])):
        d = os.path.join(raw_dir, "NQ-%s_daily.csv" % code)
        m = os.path.join(raw_dir, "NQ-%s_1min.csv" % code)
        if os.path.isfile(d) and os.path.isfile(m):
            found.append(code)
    return found


def run_pipeline(root, schema_path=None, out_path=None, report_path=None,
                 label="REAL", allow_volume_only=False, confirm=1, verbose=True):
    """Full build. Returns dict with rows/seams/offsets/roll_dates/report/summary.
    Raises OIBlankError (-> exit 2) / StitchError (-> exit 1)."""
    schema = load_schema(schema_path)
    raw_dir = os.path.join(root, "raw")
    reports_dir = os.path.join(root, "reports")
    codes = discover_contracts(raw_dir)

    if not codes:
        return {"pending": True}  # VALIDATION-PENDING (no data yet)

    # load daily + minute per contract
    daily_by_code, minute_by_code = {}, {}
    oi_status = {}
    for code in codes:
        drows, oi_how, oi_res = read_daily(os.path.join(raw_dir, "NQ-%s_daily.csv" % code), schema)
        daily_by_code[code] = drows
        minute_by_code[code] = read_minute(os.path.join(raw_dir, "NQ-%s_1min.csv" % code), schema)
        oi_status[code] = {"present": oi_present(drows), "how": oi_how, "resolved": oi_res}

    # --- OI GATE (criterion 4 / D-2026-07-17-A) -------------------------------
    blank = [c for c in codes if not oi_status[c]["present"]]
    if blank and not allow_volume_only:
        raise OIBlankError(
            "OI_BLANK — daily Open Interest missing/zero for: %s. REFUSING to "
            "stitch. The volume-only crossover fallback is a documented deviation "
            "(D-2026-07-17-A OPEN RISK) that needs trader sign-off + a DECISIONS "
            "append BEFORE use. Re-run with --allow-volume-only ONLY after that "
            "sign-off exists." % ", ".join(blank))
    if blank and allow_volume_only and verbose:
        sys.stderr.write(
            "\n!!! VOLUME-ONLY DEVIATION ENABLED — OI blank for %s. This is a "
            "documented deviation (D-2026-07-17-A). Ensure trader sign-off + a "
            "DECISIONS append exist. !!!\n\n" % ", ".join(blank))

    # --- roll dates (criterion 1) ---------------------------------------------
    roll_dates, roll_diags = [], []
    for i in range(len(codes) - 1):
        rd = compute_roll_date(daily_by_code[codes[i]], daily_by_code[codes[i + 1]],
                               confirm=confirm, allow_volume_only=allow_volume_only)
        roll_dates.append(rd["roll_date"])
        roll_diags.append(rd)

    # --- offsets + stitch (criterion 2) ---------------------------------------
    offsets, seams = build_offsets(codes, roll_dates, daily_by_code)
    rows, dupes = stitch(codes, roll_dates, offsets, minute_by_code)

    # annotate each seam with the roll TRIGGER from roll_diags so the persisted
    # report can distinguish true volume-crossover seams from the documented
    # no-overlap boundary fallback (D-2026-07-21-A). Keyed by (front, back).
    trig_by_pair = {(codes[i], codes[i + 1]): roll_diags[i]["trigger"]
                    for i in range(len(codes) - 1)}
    for s in seams:
        s["trigger"] = trig_by_pair.get((s["front"], s["back"]), "?")
    boundary = [s for s in seams if "boundary" in s.get("trigger", "")]
    if boundary and verbose:
        sys.stderr.write(
            "NOTE: %d of %d roll seam(s) used the no-overlap VOLUME-ONLY BOUNDARY "
            "fallback (D-2026-07-21-A), NOT a volume crossover: %s\n"
            % (len(boundary), len(seams),
               ", ".join("%s(%s->%s)" % (s["roll_date"], s["front"], s["back"])
                         for s in boundary)))

    # --- validation report (criterion 5) --------------------------------------
    report_md, summary, overall = validation_report(rows, seams, dupes, label=label)

    # --- write artifacts ------------------------------------------------------
    if out_path is None:
        out_path = os.path.join(reports_dir, "NQ-continuous-1min.csv")
    if report_path is None:
        report_path = os.path.join(reports_dir, "stitch-validation.md")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    os.makedirs(os.path.dirname(report_path) or ".", exist_ok=True)
    with open(out_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Timestamp", "Open", "High", "Low", "Close", "Volume", "SrcContract"])
        for r in rows:
            w.writerow([r["ts"].strftime("%Y-%m-%d %H:%M:%S"),
                        _fmt(r["o"]), _fmt(r["h"]), _fmt(r["l"]), _fmt(r["c"]),
                        _fmt(r["v"]), r["src"]])
    with open(report_path, "w") as fh:
        fh.write(report_md)

    return {
        "pending": False, "codes": codes, "roll_dates": roll_dates,
        "roll_diags": roll_diags, "offsets": offsets, "seams": seams,
        "rows": rows, "dupes": dupes, "summary": summary, "overall": overall,
        "out_path": out_path, "report_path": report_path, "oi_status": oi_status,
    }


def _fmt(x):
    if x is None:
        return ""
    if float(x).is_integer():
        return "%d" % int(x)
    return ("%.4f" % x).rstrip("0").rstrip(".")


# ---------------------------------------------------------------------------- #
#  CLI                                                                           #
# ---------------------------------------------------------------------------- #
def default_root():
    env = os.environ.get("PRAXIS_B2DATA_ROOT")
    if env:
        return env
    return os.path.join(os.path.expanduser("~"), "praxis-signals", "b2-data")


USAGE = """usage: b2_stitch.py [--root DIR] [--schema PATH] [--out CSV] [--report MD]
                    [--label REAL|SYNTHETIC-FIXTURE] [--confirm N]
                    [--allow-volume-only]

Builds the continuous NQ 1-min series (Vol/OI-crossover roll + Difference
back-adjustment) from <root>/raw/ and writes a stitched CSV + a spec-§4
validation report to <root>/reports/. raw/ empty -> VALIDATION-PENDING (exit 3).
Missing OI -> OI_BLANK refusal (exit 2). See file header for the full contract.
"""


def main(argv):
    root = None
    schema = out = report = None
    label = "REAL"
    confirm = 1
    allow_vo = False
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--root" and i + 1 < len(argv):
            root = argv[i + 1]; i += 2
        elif a == "--schema" and i + 1 < len(argv):
            schema = argv[i + 1]; i += 2
        elif a == "--out" and i + 1 < len(argv):
            out = argv[i + 1]; i += 2
        elif a == "--report" and i + 1 < len(argv):
            report = argv[i + 1]; i += 2
        elif a == "--label" and i + 1 < len(argv):
            label = argv[i + 1]; i += 2
        elif a == "--confirm" and i + 1 < len(argv):
            confirm = int(argv[i + 1]); i += 2
        elif a == "--allow-volume-only":
            allow_vo = True; i += 1
        elif a in ("-h", "--help"):
            print(USAGE); return 0
        else:
            sys.stderr.write("unknown arg: %s\n" % a); return 64
    if root is None:
        root = default_root()

    try:
        res = run_pipeline(root, schema_path=schema, out_path=out, report_path=report,
                           label=label, allow_volume_only=allow_vo, confirm=confirm)
    except OIBlankError as e:
        print("OI_BLANK %s" % e)
        return 2
    except StitchError as e:
        print("STITCH_ERROR %s" % e)
        return 1

    if res.get("pending"):
        print("STATUS: VALIDATION-PENDING — no raw contract files under %s/raw "
              "(build-ahead-of-data; D-2026-07-17-A). Nothing to stitch."
              % root)
        return 3

    print(res["summary"])
    print("wrote: %s" % res["out_path"])
    print("wrote: %s" % res["report_path"])
    return 0 if res["overall"] not in ("FAIL",) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
