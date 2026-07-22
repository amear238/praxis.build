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
from datetime import datetime, date, timezone
from zoneinfo import ZoneInfo

# --- The 22-contract expected set + chronological order -----------------------
# NQ quarterly cycle H/M/U/Z (Mar/Jun/Sep/Dec). Same set as the raw validator.
CONTRACTS = [
    "06-21", "09-21", "12-21", "03-22", "06-22", "09-22", "12-22",
    "03-23", "06-23", "09-23", "12-23", "03-24", "06-24", "09-24",
    "12-24", "03-25", "06-25", "09-25", "12-25", "03-26", "06-26", "09-26",
]
_MONTH_ORD = {"03": 1, "06": 2, "09": 3, "12": 4}

OI_NONZERO_FRACTION = 0.5  # OI "present" if non-zero for a MAJORITY of daily rows

# --- Timezone of the stored series vs the emitted series (Praxis_build-1u6) ----
# The NinjaTrader export stores 1-min timestamps in UTC (CONFIRMED: the Sunday
# reopen is 23:00Z in winter / 22:00Z in summer, BOTH == 18:00 ET, and it tracks
# DST — so UTC is genuine, not a mislabel). The continuous series the Noise-Area
# strategy and the §4.2 maintenance-break gate consume is 09:30-ET-anchored, so
# the OUTPUT carries tz = America/New_York.
#
# LOSSLESS-SEAM RULE (attempt-2 fix; attempt-1 shipped a false PASS here): the
# front/back seam handoff in stitch() is decided on the SOURCE-tz (UTC) calendar
# date — the SAME basis the daily-derived roll_dates use — and the timestamp is
# converted to the target tz ONLY at emission, AFTER routing and dedup. Converting
# BEFORE routing (the attempt-1 trap) shifts every pre-roll evening ETH bar
# (stored 00:00-04:00Z on roll_date, i.e. 19:00-23:00 ET on roll_date-1) back a
# calendar day in ET; stitch() then routes it to the FRONT contract (whose file
# lacks bars that early) while the BACK contract excludes it via date>=roll_date,
# silently dropping ~2,498 real minutes across the roll-eve dates. Routing in the
# source tz keeps the partition BIT-IDENTICAL to the tz-naive baseline
# (1,857,362 bars); the ET conversion is then a pure 1:1 relabel of every
# surviving instant, so no minute is lost or duplicated.
SOURCE_TZ = "UTC"
TARGET_TZ = "America/New_York"

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


def stitch(codes, roll_dates, offsets, minute_by_code,
           source_tz=SOURCE_TZ, target_tz=TARGET_TZ, _naive=False):
    """Concatenate per-contract 1-min bars into ONE continuous series.

    Segment window for C_i is [prev_roll, this_roll): a bar with date < R_i uses
    C_i, a bar with date >= R_i uses C_{i+1} (clean, non-overlapping seams). Each
    segment's O/H/L/C is shifted by offsets[code]; volume passes through. Output
    is sorted by timestamp and de-duplicated on identical instants.

    TIMEZONE (Praxis_build-1u6): stored timestamps are naive `source_tz` (UTC).
    The seam window handoff below is evaluated on the SOURCE-tz calendar date —
    the SAME basis roll_dates use — and each emitted `ts` is converted to
    `target_tz` (America/New_York) AFTER routing and dedup. The partition is thus
    bit-identical to the tz-naive baseline (no minute is routed to a contract
    that lacks it), and the conversion is a pure 1:1 relabel -> ZERO seam loss.

    `_naive=True` routes on the CONVERTED (target-tz) date instead — reproducing
    the attempt-1 bug that dropped ~2,498 evening minutes at the roll seams. It
    exists ONLY so the seam-crossing regression self-test can prove the trap and
    that this code avoids it; NEVER set it in production.

    Returns (rows, dedup_count). Each row: {ts, o, h, l, c, v, src}; `ts` is a
    tz-aware `target_tz` datetime."""
    src = ZoneInfo(source_tz)
    tgt = ZoneInfo(target_tz)
    same_tz = (source_tz == target_tz)

    def convert(dt):
        # naive stored dt (source_tz) -> tz-aware target_tz instant (DST-correct).
        aware = dt.replace(tzinfo=src)
        return aware if same_tz else aware.astimezone(tgt)

    n = len(codes)
    rows = []
    for i, code in enumerate(codes):
        lo = roll_dates[i - 1] if i > 0 else date.min
        hi = roll_dates[i] if i < n - 1 else date.max
        off = offsets[code]
        for b in minute_by_code.get(code, []):
            out_ts = convert(b["ts"])
            # ROUTE on the source-tz date (== roll_dates' basis) so the front/back
            # partition matches the tz-naive baseline exactly. The naive/buggy path
            # routes on the CONVERTED date, which is what dropped the seam minutes.
            route_date = out_ts.date() if _naive else b["ts"].date()
            in_window = (route_date >= lo) and (route_date < hi if hi is not date.max else True)
            if i == 0:
                in_window = (route_date < hi)
            if not in_window:
                continue
            rows.append({
                "ts": out_ts,
                "o": None if b["o"] is None else b["o"] + off,
                "h": None if b["h"] is None else b["h"] + off,
                "l": None if b["l"] is None else b["l"] + off,
                "c": None if b["c"] is None else b["c"] + off,
                "v": b["v"], "src": code,
            })
    rows.sort(key=lambda r: r["ts"])
    # dedup identical INSTANTS (keep first); spec §4.4 zero-duplicate policy. On a
    # DST fall-back the repeated wall-clock hour stays two DISTINCT tz-aware
    # instants (different UTC offsets), so it is never collapsed here — and the NQ
    # session is closed during that Sunday-morning hour anyway, so no such pair
    # actually occurs in this series.
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


# A contiguous run of this many 1-min bars INSIDE the halt can only be a mislaid
# regular session (the tz-misalignment symptom the §4.2 gate exists to catch — a
# whole ~60-min trading hour landing in the break). Genuine CME halt prints are
# isolated (observed max run = 2 across 2021-2026). Anything below this stays a
# documented source-data note; at/above it FAILS as a real session misalignment.
BREAK_SESSION_RUN_MIN = 5


def _in_break(ts):
    # CME equity-index maintenance halt is the OPEN interval (17:00, 18:00) ET.
    # The ETH session runs "18:00 -> 17:00" (spec §4.1), so the bar stamped
    # EXACTLY 17:00:00 is the session-CLOSE endpoint, NOT inside the halt — the
    # raw export confirms continuous trading through the 17:00:00 bar (e.g.
    # 2024-01-19 17:00:00 ET vol 490) then a gap until the 18:00 ET reopen.
    return ts.hour == 17 and not (ts.minute == 0 and ts.second == 0)


def _max_break_run(break_ts):
    """Longest run of CONSECUTIVE (1-min-apart, same-day) bars inside the halt,
    plus the bar/day counts. A tz MISALIGNMENT dumps a whole ~60-min session in
    the break (long run); genuine illiquid halt prints are isolated (run 1-2).
    Returns (max_run, n_bars, n_days)."""
    if not break_ts:
        return 0, 0, 0
    ts = sorted(break_ts)
    best = run = 1
    for i in range(1, len(ts)):
        if (ts[i] - ts[i - 1]).total_seconds() == 60 and ts[i].date() == ts[i - 1].date():
            run += 1
        else:
            run = 1
        if run > best:
            best = run
    return best, len(ts), len({t.date() for t in ts})


def _nth_weekday(year, month, weekday, n):
    """The n-th `weekday` (Mon=0..Sun=6) of month/year (n>=1)."""
    first = date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return date(year, month, 1 + offset + 7 * (n - 1))


def _dst_flips_between(d0, d1):
    """US DST transition dates in [d0, d1]: spring-forward = 2nd Sunday March,
    fall-back = 1st Sunday November (post-2007 rule). Used to prove the ET series
    spans both flips so the maintenance-halt DST-hold is actually gradable."""
    flips = []
    for y in range(d0.year, d1.year + 1):
        for f in (_nth_weekday(y, 3, 6, 2), _nth_weekday(y, 11, 6, 1)):
            if d0 <= f <= d1:
                flips.append(f)
    return flips


def _first_rth_open(rows):
    """First bar that lands exactly on 09:30 (target-tz wall clock) — the
    Noise-Area anchor. Returns the row or None."""
    for r in rows:
        if r["ts"].hour == 9 and r["ts"].minute == 30:
            return r
    return None


def validation_report(rows, seams, dupes, label="REAL", invariants=None,
                      tz_name=None):
    """Build the spec §4 validation markdown + a machine SUMMARY line.
    On a SYNTHETIC fixture the bar-count medians / depth are informational
    (the fixture is tiny by design); on REAL data the acceptance gate is graded,
    and any not-yet-satisfiable item is marked VALIDATION-PENDING.

    `invariants` (Praxis_build-1u6) carries the lossless-seam proof numbers
    (distinct-instant equality, seam-gap, bar count) rendered below; `tz_name`
    is the output timezone documented in the header."""
    lines, checks = [], []

    def add_check(name, status, detail):
        checks.append((name, status, detail))

    # --- §4.1 bar-count medians per session -----------------------------------
    per_day_rth, per_day_all, break_ts = {}, {}, []
    for r in rows:
        d = r["ts"].date()
        per_day_all[d] = per_day_all.get(d, 0) + 1
        if _in_rth(r["ts"]):
            per_day_rth[d] = per_day_rth.get(d, 0) + 1
        if _in_break(r["ts"]):
            break_ts.append(r["ts"])
    break_bars = len(break_ts)
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
    # The gate exists to catch a tz MISALIGNMENT — the baseline (UTC) dumped a
    # full ~60-min trading hour into the assumed 17:00-18:00-ET break (79,704
    # bars). A CORRECT UTC->ET conversion leaves the halt free of any *session*:
    # the only residents are (a) the 17:00:00 session-CLOSE endpoint (excluded by
    # _in_break) and (b) rare ISOLATED illiquid CME halt prints (vol 1-10) that
    # exist in the raw export and cannot be dropped without breaking the
    # losslessness invariant. So the graded property is "no contiguous SESSION
    # block in the halt"; the isolated prints are reported separately as INFO.
    max_run, _, brk_days = _max_break_run(break_ts)
    if label == "REAL":
        break_ok = "PASS" if max_run < BREAK_SESSION_RUN_MIN else "FAIL"
    else:
        break_ok = "PASS" if break_bars == 0 else "FAIL"
    add_check("§4.2 no regular session inside 17:00-18:00 ET halt", break_ok,
              "max contiguous in-halt run = %d min (FAIL threshold %d); "
              "17:00:00 session-close endpoint excluded" % (max_run, BREAK_SESSION_RUN_MIN))
    if label == "REAL":
        add_check("§4.2 isolated illiquid halt prints (source artifact)", "INFO",
                  "%d isolated 1-min print(s) inside the halt over %d day(s) "
                  "(vol 1-10; retained for losslessness, not a tz/seam defect)"
                  % (break_bars, brk_days))
    # DST hold: with a real multi-year ET series spanning both flips/yr, a correct
    # zoneinfo conversion keeps the halt fixed at 17:00-18:00 ET in BOTH EST and
    # EDT weeks. That is exactly what "no session in the halt across the whole
    # span" proves — so grade it on the span covering >=1 full DST cycle.
    if label == "REAL" and per_day_all:
        d0, d1 = min(per_day_all), max(per_day_all)
        flips = _dst_flips_between(d0, d1)
        dst_ok = "PASS" if (len(flips) >= 2 and max_run < BREAK_SESSION_RUN_MIN) else "PENDING"
        add_check("§4.2 DST boundary hold (both flips/yr)", dst_ok,
                  "%d DST flip(s) in %s..%s; 17:00-18:00-ET halt session-free across "
                  "EST+EDT (max in-halt run=%d min) -> DST tracked" % (len(flips), d0, d1, max_run))
    else:
        add_check("§4.2 DST boundary hold (both flips/yr)", "INFO",
                  "requires multi-year real series; not gradable on fixture")

    # --- §4.3 gap analysis ----------------------------------------------------
    gaps = []
    for i in range(1, len(rows)):
        prev, cur = rows[i - 1], rows[i]
        if prev["ts"].date() != cur["ts"].date():
            continue  # cross-day boundary (weekend/holiday) is benign
        delta = (cur["ts"] - prev["ts"]).total_seconds() / 60.0
        if delta > 1.0:
            # the 17:00-18:00 ET maintenance halt is benign (spec §4.3): the gap
            # runs from the 17:00:00 session-close endpoint (hour 16 or 17) to the
            # 18:00 ET reopen. Flag everything else.
            benign = (prev["ts"].hour in (16, 17) or cur["ts"].hour == 18
                      or _in_break(prev["ts"]) or _in_break(cur["ts"]))
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

    # --- lossless-seam INVARIANTS (Praxis_build-1u6) --------------------------
    # These GATE overall on REAL data: the tz conversion must not drop or merge a
    # single real minute vs the source-tz baseline partition.
    if invariants:
        inv_ok = (invariants["instants_equal"]
                  and invariants["seam_gap"] == 0
                  and invariants["bar_count"] == invariants["base_bar_count"])
        add_check("§4.2 tz seam-loss == 0 (distinct instants preserved)",
                  "PASS" if inv_ok else "FAIL",
                  "ET instants=%d, baseline instants=%d, seam-gap=%d, bars=%d vs baseline=%d"
                  % (invariants["distinct_instants_out"],
                     invariants["distinct_instants_base"],
                     invariants["seam_gap"],
                     invariants["bar_count"], invariants["base_bar_count"]))

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
    if tz_name:
        lines.append("**Output timezone:** %s (ET) — timestamps are ET wall-clock; "
                     "the 09:30-ET RTH anchor and the 17:00-18:00-ET maintenance "
                     "break are evaluated in this tz." % tz_name)
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

    # --- lossless-seam invariants + RTH spot-check (Praxis_build-1u6) ----------
    if invariants:
        lines.append("## Lossless tz-conversion invariants (Praxis_build-1u6)")
        lines.append("")
        lines.append("UTC→%s must relabel every instant 1:1 with no seam loss." % (tz_name or "ET"))
        lines.append("")
        lines.append("| Invariant | Value | Verdict |")
        lines.append("|---|---|---|")
        lines.append("| distinct_instants(ET output) | %d | — |" % invariants["distinct_instants_out"])
        lines.append("| distinct_instants(UTC baseline) | %d | — |" % invariants["distinct_instants_base"])
        lines.append("| ET == baseline (no instant dropped/merged) | %s | %s |"
                     % (invariants["instants_equal"],
                        "PASS" if invariants["instants_equal"] else "FAIL"))
        lines.append("| seam-gap (baseline minutes missing from ET output) | %d | %s |"
                     % (invariants["seam_gap"], "PASS" if invariants["seam_gap"] == 0 else "FAIL"))
        lines.append("| final bar count | %d | %s |"
                     % (invariants["bar_count"],
                        "PASS (== baseline %d)" % invariants["base_bar_count"]
                        if invariants["bar_count"] == invariants["base_bar_count"]
                        else "FAIL (baseline %d)" % invariants["base_bar_count"]))
        if "naive_dropped" in invariants:
            lines.append("| minutes the NAIVE convert-then-route path would DROP | %d | (trap, avoided) |"
                         % invariants["naive_dropped"])
        lines.append("")
        so = invariants.get("spot_0930")
        if so:
            lines.append("**09:30-ET RTH-open spot-check:** stored-UTC `%s` → emitted-ET "
                         "`%s` (src %s) — RTH anchor lands exactly on 09:30 ET."
                         % (so["utc"], so["et"], so["src"]))
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
                 label="REAL", allow_volume_only=False, confirm=1, verbose=True,
                 source_tz=SOURCE_TZ, target_tz=TARGET_TZ):
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
    rows, dupes = stitch(codes, roll_dates, offsets, minute_by_code,
                         source_tz=source_tz, target_tz=target_tz)

    # --- LOSSLESS-SEAM INVARIANTS (Praxis_build-1u6) --------------------------
    # Prove UTC->ET dropped/merged NO real minute vs the source-tz baseline
    # partition. Re-stitch with target==source (the committed tz-naive partition,
    # 1,857,362 bars) and compare distinct instants. Also re-stitch with the NAIVE
    # convert-then-route path to quantify the attempt-1 trap that this fix avoids.
    # Files are already in memory, so these extra passes are cheap.
    base_rows, _ = stitch(codes, roll_dates, offsets, minute_by_code,
                          source_tz=source_tz, target_tz=source_tz)
    naive_rows, _ = stitch(codes, roll_dates, offsets, minute_by_code,
                           source_tz=source_tz, target_tz=target_tz, _naive=True)

    def _utc_instants(rr):
        return {r["ts"].astimezone(timezone.utc) for r in rr}

    inst_out = _utc_instants(rows)
    inst_base = _utc_instants(base_rows)
    inst_naive = _utc_instants(naive_rows)
    spot = _first_rth_open(rows)
    invariants = {
        "distinct_instants_out": len(inst_out),
        "distinct_instants_base": len(inst_base),
        "instants_equal": inst_out == inst_base,
        "seam_gap": len(inst_base - inst_out),
        "bar_count": len(rows),
        "base_bar_count": len(base_rows),
        "naive_dropped": len(inst_base - inst_naive),
    }
    if spot is not None:
        src_utc = spot["ts"].astimezone(timezone.utc)
        invariants["spot_0930"] = {
            "utc": src_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "et": spot["ts"].strftime("%Y-%m-%d %H:%M:%S %Z"),
            "src": spot["src"],
        }
    if verbose:
        sys.stderr.write(
            "INVARIANTS (1u6): bars=%d baseline=%d equal=%s seam-gap=%d "
            "naive-would-drop=%d\n"
            % (invariants["bar_count"], invariants["base_bar_count"],
               invariants["instants_equal"], invariants["seam_gap"],
               invariants["naive_dropped"]))

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
    report_md, summary, overall = validation_report(
        rows, seams, dupes, label=label, invariants=invariants, tz_name=target_tz)

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
        "invariants": invariants, "source_tz": source_tz, "target_tz": target_tz,
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
