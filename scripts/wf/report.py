#!/usr/bin/env python3
"""Walk-forward results report (values-spec §8) — arm (a) and arm (b), Markdown.

Reads the calendar JSON (contract Interface 1), the two selection JSONs
(Interface 3) and the PBO JSON (Interface 4). It does not import the producers;
it reads their JSON directly and refuses anything truncated or inconsistent
with the calendar.

Spec   = docs/specs/2026-11-06-walk-forward-values.md (v2.1) ("values-spec")
WF spec = docs/specs/2026-11-05-walk-forward-spec.md
Gates  = docs/specs/2026-11-05-phase3-build-specification.md :80-85

Standard library only. Deterministic output (no timestamps, fixed formatting).
"""

import argparse
import datetime
import json
import math
import os
import re
import statistics
import sys
import unicodedata
from decimal import Decimal
from fractions import Fraction

STANDING_LIMITATION = ("Standing limitation: Fills are optimistic; Standard resolution "
                       "on 1-minute bars; 2 ticks/side slippage assumed.")
STANDING_CORE = STANDING_LIMITATION[len("Standing limitation: "):]

# values-spec §5 :85 counts "last bar 12:00 / 12:15 / 14:03"; the results report
# (docs/reports/2026-11-01-three-strategy-results.md:153) INFERS the 14:03 day is a data gap.
EARLY_CLOSE_FOOTNOTE = ("Note: the early-close counts include 2023-04-05 (file last bar 14:03), which the "
                        "results report INFERS is a data gap, not an early close "
                        "(docs/reports/2026-11-01-three-strategy-results.md:153); values-spec §5 :85 counts "
                        "last bar 12:00 / 12:15 / 14:03.")


def has_data_gap_early_close(cal):
    """True iff the calendar counts 2023-04-05 (NT8 last bar 14:03) as an early close."""
    return any(isinstance(s, dict) and s.get("date") == "2023-04-05" and s.get("nt8_last_bar") == "14:03"
               for s in cal.get("sessions", []))


# The six gates, byte for byte from Phase 3 spec :80-85 (under "Pass gates (non-negotiable):" :78).
GATES = [
    "OOS profit factor ≥ 1.30",
    "OOS Sharpe ≥ 1.0",
    "Max drawdown ≤ 4% of equity",
    "≥ 250 aggregate OOS trades",
    "≥ 60% of walk-forward windows profitable",
    "Walk-forward efficiency ≥ 0.50",
]

# Money arithmetic is exact (W7 fix, ADV-C D1/D2): every P&L value read from JSON is
# converted with Fraction(Decimal(repr(x))) and PF, equity, drawdowns and the MNQ
# conversion are computed and compared exactly; rounding happens only for display.
PF_THRESHOLD = Fraction("1.30")   # gate 1
TRADES_THRESHOLD = 250            # gate 4
PROFITABLE_PCT = 60               # gate 5 (integer percent, compared exactly: n*100 >= 60*K)
PBO_THRESHOLD = Fraction(5, 100)  # values-spec §7 :108, §8 :129 — arm (b) counts only if PBO < 0.05

# values-spec §3 :49-52 grid; contract Interface 2 column naming. Arm (a)'s column is "armA".
GRID_COLUMN_RE = re.compile(r"L(10|14|18)_k(0\.8|1\.0|1\.2)_m(1\.5|2\.25|3)_(BandOrVWAP|OppBand|Flat1559)")
# W8 fix (ADV-D D4): arm (b) must carry exactly these 81 columns (values-spec §3 :49-52;
# contract Interface 2 naming `L{Lookback}_k{NoiseMult:.1f}_m{StopAtrMult:g}_{ExitPolicy}`).
GRID_COLUMNS = frozenset("L{}_k{:.1f}_m{:g}_{}".format(L, k, m, p)
                         for L in (10, 14, 18) for k in (0.8, 1.0, 1.2) for m in (1.5, 2.25, 3.0)
                         for p in ("BandOrVWAP", "OppBand", "Flat1559"))
assert len(GRID_COLUMNS) == 81
ARM_A_COLUMN = "armA"
PNL_BASES = ("net", "gross")

# values-spec §4 / WF spec: IS 252, OOS 63, STEP 63 sessions; K = floor((N - 252) / 63).
IS_LEN, OOS_LEN, STEP = 252, 63, 63

# W8 fix (ADV-D D3): CSCV shape, values-spec §7 :103 (S = 16; rows = the last S*block sessions
# ending at the last OOS session). For the RULED calendar (K = 17, last OOS s1323) block = 82,
# rows = [12, 1323]. The brief pins block = 82, so any calendar whose last OOS session is not
# in 1312..1327 is refused here (INFERRED consequence: report.py serves K = 17 only).
CSCV_S, CSCV_BLOCK = 16, 82
CSCV_ROWS = CSCV_S * CSCV_BLOCK            # 1312
CSCV_SPLITS = math.comb(CSCV_S, CSCV_S // 2)   # C(16, 8) = 12870
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")   # ASCII digits only (\d matches other scripts)

# Per-tier table, embedded as data from WF spec §6, table rows at :115-131
# (header :113; values-spec §8 :136 cites the section as :105-141).
# Every row is kept (values-spec §8 :136): the Studio Static rows, the Builder 50K
# add-on as its own $1,500 row, and Flex as UNVERIFIED. No tier is chosen (Q9, §8 :137).
# Fields: (label, account size, 4% of size, MFFU limit text, lower-of-the-two used as limit, wf-spec line)
TIERS = [
    ("Studio #003 · 5K", 5000, 200, "$250 (Static, not trailing)", 200, 115),
    ("Studio #001 · 10K", 10000, 400, "$500 (Static)", 400, 116),
    ("Studio #002 · 20K", 20000, 800, "$1,000 (Static)", 800, 117),
    ("Rapid · 25K", 25000, 1000, "$1,000 (Eval EOD; Sim-Funded intraday trailing)", 1000, 118),
    ("Rapid EOD · 25K", 25000, 1000, "$1,000 (EOD trailing)", 1000, 119),
    ("Builder · 25K", 25000, 1000, "$1,000 (EOD trailing)", 1000, 120),
    ("Rapid · 50K", 50000, 2000, "$2,000 (Eval EOD; Sim-Funded intraday trailing)", 2000, 121),
    ("Rapid EOD · 50K", 50000, 2000, "$2,000 (EOD trailing)", 2000, 122),
    ("Pro · 50K", 50000, 2000, "$2,000 (EOD trailing)", 2000, 123),
    ("Builder · 50K", 50000, 2000, "$2,000 (EOD trailing)", 2000, 124),
    ("Builder · 50K with add-on", 50000, 2000, "$1,500 with add-on (EOD trailing)", 1500, 124),
    ("Rapid · 100K", 100000, 4000, "$3,000 (Eval EOD; Sim-Funded intraday trailing)", 3000, 125),
    ("Pro · 100K", 100000, 4000, "$3,000 (EOD trailing)", 3000, 126),
    ("Builder · 100K", 100000, 4000, "$3,000 (EOD trailing)", 3000, 127),
    ("Rapid · 150K", 150000, 6000, "$4,500 (Eval EOD; Sim-Funded intraday trailing)", 4500, 128),
    ("Pro · 150K", 150000, 6000, "$4,500 (EOD trailing)", 4500, 129),
    ("Builder · 150K", 150000, 6000, "$4,500 (EOD trailing)", 4500, 130),
    ("Flex", None, None, "UNVERIFIED", None, 131),
]

COST_MODEL_REL = os.path.join("config", "backtest-cost-model.json")

# W9 fix (ADV-E 2): the two round-turn costs are RULED (ruling 2 of 2026-11-06): "NQ $4.68"
# (values-spec §7 :115) and "MNQ $1.90" (values-spec §8 :138). A cost model that carries any
# other value is refused, so every printed figure rests on the ruled costs.
RULED_NQ_RT = Fraction("4.68")
RULED_MNQ_RT = Fraction("1.90")


class ReportInputError(Exception):
    """Input refused (truncated, malformed, or not matching the calendar)."""


# ----------------------------------------------------------------- helpers

def _fail(msg):
    raise ReportInputError(msg)


def _close(a, b, tol=1e-6):
    return math.isclose(a, b, rel_tol=0.0, abs_tol=tol * max(1.0, abs(a), abs(b)))


def exact(x):
    """Exact value of a JSON number: Fraction(Decimal(repr(x))) for a float, Fraction(x)
    for an int / Fraction. Refuses bools, strings, NaN and infinities."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        _fail("not a number: {!r}".format(x))
    if isinstance(x, int):
        # W9 fix (ADV-E 1): an integer too large for a float would overflow every later
        # float() / math.isfinite(); it is not a P&L, count or ratio — refuse it here.
        try:
            float(x)
        except OverflowError:
            _fail("integer too large for a float: {} digits".format(len(str(abs(x)))))
        return Fraction(x)
    if not math.isfinite(x):
        _fail("not a finite number: {!r}".format(x))
    return Fraction(Decimal(repr(x)))


def fixed(x, places):
    """Display only: exact value rounded half-even to `places` decimals, with thousands commas."""
    units = round(exact(x) * 10 ** places)   # round() on a Fraction is exact, half-even
    sign = "-" if units < 0 else ""
    whole, frac = divmod(abs(units), 10 ** places)
    if places == 0:
        return "{}{:,}".format(sign, whole)
    return "{}{:,}.{:0{}d}".format(sign, whole, frac, places)


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def _need_int(v, where, lo=None, hi=None):
    """W8 fix (ADV-D D6): an int that is not a bool, optionally within [lo, hi]; else refuse."""
    if not _is_int(v) or (lo is not None and v < lo) or (hi is not None and v > hi):
        rng = "" if lo is None and hi is None else " in [{}, {}]".format(
            "-inf" if lo is None else lo, "inf" if hi is None else hi)
        _fail("{}: {!r} is not an integer{}".format(where, v, rng))
    return v


def _need_num(v, where):
    """A finite JSON number (int or float, not bool, not a string)."""
    try:
        return exact(v)
    except ReportInputError as e:
        _fail("{}: {}".format(where, e))


def _need_date(v, where):
    """W8 fix (ADV-D D1): YYYY-MM-DD, ASCII digits, and a real calendar date."""
    if not isinstance(v, str) or not DATE_RE.fullmatch(v):
        _fail("{}: {!r} is not a YYYY-MM-DD date".format(where, v))
    try:
        datetime.date(int(v[0:4]), int(v[5:7]), int(v[8:10]))
    except ValueError:
        _fail("{}: {!r} is not a real date".format(where, v))
    return v


def _terminating_places(fr):
    """Decimal places of fr's exact expansion, or None if it does not terminate."""
    d = fr.denominator
    a = b = 0
    while d % 2 == 0:
        d //= 2
        a += 1
    while d % 5 == 0:
        d //= 5
        b += 1
    return max(a, b) if d == 1 else None


def exact_decimal(x, min_places=2, max_places=None):
    """W8 fix (ADV-D D5): display that never contradicts an exact comparison.
    The exact decimal expansion with at least `min_places` places. If it does not terminate
    (or needs more than `max_places`), it is cut DOWN (floor) at max_places (10 if None)
    and marked "…": for any threshold t with at most that many places, floor(v) >= t iff
    v >= t, so the printed digits are always on the same side of t as the exact value."""
    fr = exact(x)
    p = _terminating_places(fr)
    if p is not None and (max_places is None or p <= max_places):
        return fixed(fr, max(p, min_places))
    cut = 10 if max_places is None else max_places
    units = math.floor(fr * 10 ** cut)
    return fixed(Fraction(units, 10 ** cut), cut) + "…"


def money(x):
    if x is None:
        return "—"
    # W8 fix (ADV-D D5): exact cents when the value is exact at cents, otherwise the exact,
    # unrounded decimal (never "$0.00" for a non-zero value). An exact zero prints "0.00".
    return exact_decimal(x, 2)


def load_json(path, what):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except OSError as e:
        _fail("{}: cannot read {}: {}".format(what, path, e))
    except UnicodeDecodeError as e:   # W9 fix (ADV-E 1); checked before ValueError (a subclass)
        _fail("{}: {} is not UTF-8 text: {}".format(what, path, e))
    except json.JSONDecodeError as e:
        _fail("{}: {} is not valid JSON (truncated?): {}".format(what, path, e))
    except ValueError as e:   # W9 fix (ADV-E 1): e.g. an integer of more than 4300 digits
        _fail("{}: {} cannot be decoded: ValueError: {}".format(what, path, e))
    except RecursionError as e:   # W9 fix (ADV-E 1): nesting too deep to decode
        _fail("{}: {} is nested too deeply to decode: RecursionError: {}".format(what, path, e))


def load_costs(path):
    """W9 fix (ADV-E 2): both round-turn costs must be real numbers (int/float, not bool,
    not a string), finite, and EQUAL to the ruled values (RULED_NQ_RT, RULED_MNQ_RT)."""
    d = load_json(path, "cost model")
    cm = d.get("cost_model") if isinstance(d, dict) else None
    if not isinstance(cm, dict):
        _fail("cost model {}: no cost_model object".format(path))
    out = []
    for key, ruled, label in (("commission_round_turn_usd", RULED_NQ_RT, "NQ"),
                              ("commission_round_turn_usd_mnq", RULED_MNQ_RT, "MNQ")):
        if key not in cm:
            _fail("cost model {}: missing commission field {!r}".format(path, key))
        v = cm[key]
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            _fail("cost model {}: {} {!r} = {!r} is not a real number".format(path, label, key, v))
        try:
            ev = exact(v)
        except ReportInputError as e:
            _fail("cost model {}: {} {!r}: {}".format(path, label, key, e))
        if ev != ruled:
            _fail("cost model {}: {} {!r} = {!r} != the ruled ${} (ruling 2 of 2026-11-06; "
                  "values-spec §7 :115, §8 :138)".format(path, label, key, v, fixed(ruled, 2)))
        out.append(float(v))
    return out[0], out[1]


# ----------------------------------------------------------------- validation

def validate_calendar(cal):
    if not isinstance(cal, dict) or cal.get("schema") != "praxis-wf-calendar/1":
        _fail("calendar: schema is not praxis-wf-calendar/1")
    for key in ("N", "sessions", "windows", "K"):
        if key not in cal:
            _fail("calendar: missing key {!r} (truncated?)".format(key))
    _need_int(cal["N"], "calendar: N", 0)
    _need_int(cal["K"], "calendar: K", 0)
    if not isinstance(cal["sessions"], list) or not isinstance(cal["windows"], list):
        _fail("calendar: sessions / windows are not lists")
    if len(cal["sessions"]) != cal["N"]:
        _fail("calendar: N={} but {} sessions listed (truncated?)".format(cal["N"], len(cal["sessions"])))
    if len(cal["windows"]) != cal["K"]:
        _fail("calendar: K={} but {} windows listed (truncated?)".format(cal["K"], len(cal["windows"])))
    # W8 fix (ADV-D D1/D2): every session's n and date are checked; they are the source of
    # every date the report prints.
    prev_date = None
    for i, s in enumerate(cal["sessions"], 1):
        if not isinstance(s, dict) or "n" not in s or "date" not in s:
            _fail("calendar session #{}: not an object with n and date".format(i))
        if not _is_int(s["n"]) or s["n"] != i:
            _fail("calendar session #{}: n={!r} (must be the integer {})".format(i, s["n"], i))
        d = _need_date(s["date"], "calendar session {} date".format(i))
        if prev_date is not None and d <= prev_date:
            _fail("calendar session {}: date {} is not after session {}'s {}".format(i, d, i - 1, prev_date))
        prev_date = d
    for i, w in enumerate(cal["windows"], 1):
        if not isinstance(w, dict):
            _fail("calendar window #{}: not an object".format(i))
        for key in ("k", "is", "oos", "is_dates", "oos_dates", "is_holes", "oos_holes",
                    "is_early_close", "oos_early_close"):
            if key not in w:
                _fail("calendar window {}: missing key {!r}".format(i, key))
        if not _is_int(w["k"]) or w["k"] != i:
            _fail("calendar: window #{} has k={!r}".format(i, w["k"]))
        for key in ("is", "oos", "is_dates", "oos_dates"):
            if not isinstance(w[key], list) or len(w[key]) != 2:
                _fail("calendar window {}: {} is not a 2-element list".format(i, key))
        for key in ("is", "oos"):
            for v in w[key]:
                _need_int(v, "calendar window {} {} session number".format(i, key), 1, cal["N"])
        # W8 fix (ADV-D D2): the window set IS the formula (values-spec §5 :82; sessions.py builds
        # from s1): window k IS = s(63(k-1)+1)..s(63(k-1)+252), OOS = the next 63 sessions.
        ia = STEP * (i - 1) + 1
        want_is = [ia, ia + IS_LEN - 1]
        want_oos = [ia + IS_LEN, ia + IS_LEN + OOS_LEN - 1]
        if w["is"] != want_is or w["oos"] != want_oos:
            _fail("calendar window {}: is {} / oos {} != formula is {} / oos {}".format(
                i, w["is"], w["oos"], want_is, want_oos))
        # Dates printed for the window must be the calendar's own session dates.
        for key, nums in (("is_dates", want_is), ("oos_dates", want_oos)):
            for j in (0, 1):
                _need_date(w[key][j], "calendar window {} {}[{}]".format(i, key, j))
            want = [cal["sessions"][nums[0] - 1]["date"], cal["sessions"][nums[1] - 1]["date"]]
            if w[key] != want:
                _fail("calendar window {}: {} {} != sessions {}..{} dates {}".format(
                    i, key, w[key], nums[0], nums[1], want))
        for key in ("is_holes", "oos_holes", "is_early_close", "oos_early_close"):
            _need_int(w[key], "calendar window {} {}".format(i, key), 0)
    # W7 fix (ADV-C D4): recompute K from N; no gate may pass on zero windows.
    n = cal["N"]
    k_expected = (n - IS_LEN) // OOS_LEN if n >= IS_LEN else 0
    if k_expected < 1:
        _fail("calendar: N={} gives K = floor((N-252)/63) = {} < 1 — no walk-forward window".format(
            n, k_expected))
    if cal["K"] != k_expected or len(cal["windows"]) != k_expected:
        _fail("calendar: K={} / {} windows listed, but floor((N-252)/63) = {} for N={}".format(
            cal["K"], len(cal["windows"]), k_expected, n))


def validate_selection(sel, cal, arm, commission_nq):
    what = "selection arm ({})".format(arm)
    if not isinstance(sel, dict) or sel.get("schema") != "praxis-wf-selection/1":
        _fail("{}: schema is not praxis-wf-selection/1".format(what))
    if sel.get("arm") != arm:
        _fail("{}: file says arm={!r}".format(what, sel.get("arm")))
    if sel.get("truncated") is True:
        _fail("{}: input marked truncated (values-spec §7 :112) — refused".format(what))
    for key in ("windows", "oos_total_net", "oos_total_trades"):
        if key not in sel:
            _fail("{}: missing key {!r} (truncated?)".format(what, key))
    if arm == "a":
        fs = sel.get("full_span")
        if not isinstance(fs, dict) or "net" not in fs or "trades" not in fs:
            _fail("{}: full_span {{net, trades}} missing (values-spec §2 :43)".format(what))
        _need_num(fs["net"], "{} full_span.net".format(what))
        _need_int(fs["trades"], "{} full_span.trades".format(what), 0)
    _need_num(sel["oos_total_net"], "{} oos_total_net".format(what))
    _need_int(sel["oos_total_trades"], "{} oos_total_trades".format(what), 0)
    if not isinstance(sel["windows"], list) or not all(isinstance(w, dict) for w in sel["windows"]):
        _fail("{}: windows is not a list of objects".format(what))
    validate_strings(sel, arm, what)
    ws = sel["windows"]
    if len(ws) != len(cal["windows"]):
        _fail("{}: {} windows but calendar has K={}".format(what, len(ws), len(cal["windows"])))
    tot_net, tot_tr = 0.0, 0
    for w, cw in zip(ws, cal["windows"]):
        k = cw["k"]
        if w.get("truncated") is True:
            _fail("{} window {}: marked truncated — refused".format(what, k))
        for key in ("k", "is", "oos", "eligible", "pick", "no_eligible", "oos_net",
                    "oos_trades", "oos_daily", "oos_trade_list"):
            if key not in w:
                _fail("{} window {}: missing key {!r}".format(what, k, key))
        if not _is_int(w["k"]) or not isinstance(w["is"], list) or not isinstance(w["oos"], list) \
                or not all(_is_int(v) for v in list(w["is"]) + list(w["oos"])):
            _fail("{} window {}: k / is / oos session numbers must be integers (not bool)".format(what, k))
        _need_int(w["oos_trades"], "{} window {} oos_trades".format(what, k), 0)
        _need_num(w["oos_net"], "{} window {} oos_net".format(what, k))
        if not isinstance(w["oos_daily"], list) or not isinstance(w["oos_trade_list"], list):
            _fail("{} window {}: oos_daily / oos_trade_list are not lists".format(what, k))
        for x in w["oos_daily"]:
            _need_num(x, "{} window {} oos_daily value".format(what, k))
        if w["k"] != k or list(w["is"]) != list(cw["is"]) or list(w["oos"]) != list(cw["oos"]):
            _fail("{} window {}: k/is/oos {}/{}/{} do not match calendar {}/{}/{}".format(
                what, k, w["k"], w["is"], w["oos"], k, cw["is"], cw["oos"]))
        a, b = cw["oos"]
        span = b - a + 1
        if len(w["oos_daily"]) != span:
            _fail("{} window {}: oos_daily has {} values, OOS span is {} sessions (truncated?)".format(
                what, k, len(w["oos_daily"]), span))
        tl = w["oos_trade_list"]
        if len(tl) != w["oos_trades"]:
            _fail("{} window {}: oos_trades={} but trade list has {} (truncated?)".format(
                what, k, w["oos_trades"], len(tl)))
        daily_from_trades = [0.0] * span
        prev = None
        for t in tl:
            if not isinstance(t, dict):
                _fail("{} window {}: trade is not an object".format(what, k))
            for key in ("session", "exit_time", "net_pnl", "gross_pnl"):
                if key not in t:
                    _fail("{} window {}: trade missing {!r}".format(what, k, key))
            s = _need_int(t["session"], "{} window {} trade session".format(what, k))
            if not isinstance(t["exit_time"], str):
                _fail("{} window {}: trade exit_time {!r} is not a string".format(what, k, t["exit_time"]))
            _need_num(t["net_pnl"], "{} window {} trade net_pnl".format(what, k))
            _need_num(t["gross_pnl"], "{} window {} trade gross_pnl".format(what, k))
            if not (a <= s <= b):
                _fail("{} window {}: trade exit session {} outside OOS {}".format(what, k, s, cw["oos"]))
            order_key = (s, str(t["exit_time"]))
            if prev is not None and order_key < prev:
                _fail("{} window {}: trades not in exit order at {}".format(what, k, t["exit_time"]))
            prev = order_key
            # values-spec §8 :139: NQ gross = NQ net + that run's NQ commission.
            if not _close(float(t["gross_pnl"]) - float(t["net_pnl"]), commission_nq, 1e-6):
                _fail("{} window {}: trade at {} has gross-net = {} != NQ commission {}".format(
                    what, k, t["exit_time"], float(t["gross_pnl"]) - float(t["net_pnl"]), commission_nq))
            daily_from_trades[s - a] += float(t["net_pnl"])
        for i, (x, y) in enumerate(zip(w["oos_daily"], daily_from_trades)):
            if not _close(float(x), y):
                _fail("{} window {}: oos_daily[{}]={} but trades exited that session sum to {}".format(
                    what, k, i, x, y))
        if not _close(float(w["oos_net"]), sum(float(x) for x in w["oos_daily"])):
            _fail("{} window {}: oos_net {} != sum(oos_daily)".format(what, k, w["oos_net"]))
        if arm == "b" and w["no_eligible"] and (w["pick"] is not None or tl):
            _fail("{} window {}: no_eligible but a pick or trades are present".format(what, k))
        validate_window_fields(w, sel, arm, what, k)
        tot_net += float(w["oos_net"])
        tot_tr += int(w["oos_trades"])
    if not _close(float(sel["oos_total_net"]), tot_net) or int(sel["oos_total_trades"]) != tot_tr:
        _fail("{}: oos_total_net/trades {}/{} != window sums {}/{}".format(
            what, sel["oos_total_net"], sel["oos_total_trades"], tot_net, tot_tr))
    # W9 fix (ADV-E 3): the full-span run covers every OOS session, so it cannot have fewer
    # trades than the OOS windows together (INFERRED from values-spec §2 :43).
    if arm == "a" and sel["full_span"]["trades"] < tot_tr:
        _fail("{}: full_span.trades {} < {} OOS trades summed over the windows (values-spec §2 :43)".format(
            what, sel["full_span"]["trades"], tot_tr))


def _check_basis(v, where):
    if not isinstance(v, str) or v not in PNL_BASES:
        _fail("{}: pnl basis {!r} is not one of {}".format(where, v, PNL_BASES))


def validate_strings(sel, arm, what):
    """W7 fix (ADV-C D3): every string the report prints from a selection is checked
    against its closed set, so no input can inject text (values-spec :7, S13)."""
    cols = sel.get("columns")
    if not isinstance(cols, list) or not all(isinstance(c, str) for c in cols):
        _fail("{}: columns missing, not a list, or not all strings".format(what))
    if arm == "a":
        if cols != [ARM_A_COLUMN]:
            _fail("{}: columns {!r} != [{!r}]".format(what, cols, ARM_A_COLUMN))
    else:
        if not cols or len(set(cols)) != len(cols):
            _fail("{}: columns empty or duplicated".format(what))
        for c in cols:
            if not GRID_COLUMN_RE.fullmatch(c) or c not in GRID_COLUMNS:
                _fail("{}: column {!r} is not one of the 81 grid columns".format(what, c))
        # W8 fix (ADV-D D4): exactly the 81 grid columns, no more, no fewer.
        if set(cols) != GRID_COLUMNS or len(cols) != len(GRID_COLUMNS):
            _fail("{}: columns are {} grid names, not exactly the 81 of values-spec §3 :49-52 "
                  "(missing {})".format(what, len(cols), len(GRID_COLUMNS - set(cols))))
    allowed = set(cols)
    m = sel.get("pnl_basis_in")
    if isinstance(m, dict):
        for col, b in m.items():
            if col not in allowed:
                _fail("{}: pnl_basis_in key {!r} is not one of its columns".format(what, col))
            _check_basis(b, "{} pnl_basis_in[{!r}]".format(what, col))
    elif "pnl_basis_in" in sel:
        _check_basis(m, "{} pnl_basis_in".format(what))
    if "pnl_basis" in sel:
        _check_basis(sel["pnl_basis"], "{} pnl_basis".format(what))
    # W9 fix (ADV-E 1): only iterate a trade list that is a list (the type check runs later).
    for w in sel.get("windows", []):
        tl = w.get("oos_trade_list") if isinstance(w, dict) else None
        for t in tl if isinstance(tl, list) else []:
            if isinstance(t, dict) and "pnl_basis_in" in t:
                _check_basis(t["pnl_basis_in"], "{} trade pnl_basis_in".format(what))


def validate_window_fields(w, sel, arm, what, k):
    """W7 fix (ADV-C D3): pick / no_eligible / eligible must be mutually consistent."""
    ne, pick, el = w["no_eligible"], w["pick"], w["eligible"]
    if not isinstance(ne, bool):
        _fail("{} window {}: no_eligible {!r} is not a bool".format(what, k, ne))
    if arm == "a":
        if pick not in (None, ARM_A_COLUMN):
            _fail("{} window {}: arm (a) pick {!r} is not null or {!r}".format(what, k, pick, ARM_A_COLUMN))
        if ne:
            _fail("{} window {}: arm (a) (fixed rules) cannot be no_eligible".format(what, k))
        if el is not None and (isinstance(el, bool) or not isinstance(el, int)):
            _fail("{} window {}: eligible {!r} is not null or an integer".format(what, k, el))
        return
    if pick is not None and (not isinstance(pick, str) or not GRID_COLUMN_RE.fullmatch(pick)
                             or pick not in sel["columns"]):
        _fail("{} window {}: pick {!r} is not null or one of the selection's grid columns".format(
            what, k, pick))
    if ne != (pick is None):
        _fail("{} window {}: no_eligible={} but pick={!r} (no_eligible must be true iff pick is null)".format(
            what, k, ne, pick))
    if isinstance(el, bool) or not isinstance(el, int) or not (0 <= el <= len(sel["columns"])):
        _fail("{} window {}: eligible {!r} is not an integer in 0..{}".format(what, k, el, len(sel["columns"])))
    if (el == 0) != ne:
        _fail("{} window {}: eligible={} but no_eligible={}".format(what, k, el, ne))


def validate_pbo(pbo, cal):
    if not isinstance(pbo, dict) or pbo.get("schema") != "praxis-wf-pbo/1":
        _fail("pbo: schema is not praxis-wf-pbo/1")
    for key in ("pbo", "threshold", "passes", "S", "block", "rows", "splits", "le0", "no_eligible_splits"):
        if key not in pbo:
            _fail("pbo: missing key {!r} (truncated?)".format(key))
    # W8 fix (ADV-D D3): the CSCV shape is fixed (values-spec §7 :103): S = 16, block = 82,
    # splits = C(16, 8) = 12870, rows = the calendar's cscv_rows = [last_oos - 1311, last_oos].
    if not _is_int(pbo["S"]) or pbo["S"] != CSCV_S:
        _fail("pbo: S={!r} != {}".format(pbo["S"], CSCV_S))
    if not _is_int(pbo["block"]) or pbo["block"] != CSCV_BLOCK:
        _fail("pbo: block={!r} != {}".format(pbo["block"], CSCV_BLOCK))
    if not _is_int(pbo["splits"]) or pbo["splits"] != CSCV_SPLITS:
        _fail("pbo: splits={!r} != C({}, {}) = {}".format(pbo["splits"], CSCV_S, CSCV_S // 2, CSCV_SPLITS))
    last_oos = cal["windows"][-1]["oos"][1]
    want_rows = [last_oos - CSCV_ROWS + 1, last_oos]
    for ck, want in (("cscv_S", CSCV_S), ("cscv_block", CSCV_BLOCK), ("cscv_rows", want_rows)):
        if ck not in cal:
            _fail("pbo: calendar has no {} to check the PBO shape against".format(ck))
        cv = cal[ck]
        if (isinstance(want, list) and (not isinstance(cv, list) or not all(_is_int(v) for v in cv))) \
                or (not isinstance(want, list) and not _is_int(cv)) or cv != want:
            _fail("pbo: calendar {}={!r} != {!r} (last OOS session {}; {} = {} x {})".format(
                ck, cv, want, last_oos, CSCV_ROWS, CSCV_S, CSCV_BLOCK))
    rows = pbo["rows"]
    if not isinstance(rows, list) or not all(_is_int(v) for v in rows) or rows != want_rows:
        _fail("pbo: rows={!r} != calendar cscv_rows {}".format(rows, want_rows))
    splits = pbo["splits"]
    le0 = _need_int(pbo["le0"], "pbo: le0", 0, splits)
    _need_int(pbo["no_eligible_splits"], "pbo: no_eligible_splits", 0, le0)
    p = pbo["pbo"]
    # W9 fix (ADV-E 1): exact() first — a huge integer would overflow math.isfinite().
    if not isinstance(p, (int, float)) or isinstance(p, bool) or not (0 <= _need_num(p, "pbo: value") <= 1):
        _fail("pbo: value {!r} is not a number in [0, 1]".format(p))
    # The verdict uses le0/splits exactly; the float must lie within one ulp of it.
    want_p = Fraction(le0, splits)
    if abs(Fraction(p) - want_p) > Fraction(math.ulp(float(want_p))):
        _fail("pbo: pbo={!r} is not le0/splits = {}/{} (to within one ulp)".format(p, le0, splits))
    if not isinstance(pbo["passes"], bool):
        _fail("pbo: passes={!r} is not a bool".format(pbo["passes"]))
    if exact(pbo["threshold"]) != PBO_THRESHOLD:
        _fail("pbo: threshold {} != values-spec §7 :108 threshold 0.05".format(pbo["threshold"]))
    # PBO is a ratio of integers: the verdict is le0/splits < 0.05, compared exactly.
    if bool(pbo["passes"]) != pbo_passes(pbo):
        _fail("pbo: file says passes={} but le0/splits = {}/{} vs < 0.05 gives {}".format(
            pbo["passes"], le0, splits, pbo_passes(pbo)))


def pbo_passes(pbo):
    return Fraction(pbo["le0"], pbo["splits"]) < PBO_THRESHOLD


# ----------------------------------------------------------------- maths

def profit_factor(pnls):
    """Gross profit / |gross loss| over the joined OOS trade list.

    INFERRED: NT8-style definition (sum of positive net P&L / |sum of negative net P&L|)
    is taken as the meaning of gate 1 "OOS profit factor" (Phase 3 spec :80).
    Returns (value|None, reason). No losing trade -> undefined, never a pass.
    """
    pnls = [exact(p) for p in pnls]
    gp = sum((p for p in pnls if p > 0), Fraction(0))
    gl = sum((p for p in pnls if p < 0), Fraction(0))
    if not pnls:
        return None, "undefined (no trades)"
    if gl == 0:
        return None, "undefined (no losses)"
    return gp / abs(gl), None


def sharpe_daily(daily):
    """values-spec §6 :92 statistic: mean/sd(n-1)*sqrt(252), rf 0. None if undefined.
    Printed for information only — NOT gate 2's definition (values-spec §6 :93)."""
    if len(daily) < 2:
        return None
    sd = statistics.stdev(daily)
    if sd == 0:
        return None
    return statistics.fmean(daily) / sd * math.sqrt(252)


def mnq_from_nq_gross(nq_gross, mnq_commission):
    """values-spec §8 :139: MNQ net = (NQ gross / 10) - $1.90.
    INFERRED (values-spec §8 :139): that this equals an own MNQ run."""
    return exact(nq_gross) / 10 - exact(mnq_commission)


def _dd_series(points, eq0=Fraction(0), peak0=Fraction(0)):
    """Max drawdown over a sequence of P&L increments, starting at equity eq0 with
    running peak peak0. The starting point counts toward the peak and is itself an
    observation (depth peak0 - eq0). Returns (max_dd, end_equity, end_peak), exact.
    Drawdown is a positive dollar figure."""
    # INFERRED reading of values-spec §8 :139 "carried across windows": the equity level at
    # the window's start (the carried-in state) is an observation of that window. For the
    # from-window-start measures eq0 = peak0 = 0, so this adds nothing there.
    eq, peak = exact(eq0), exact(peak0)
    dd = peak - eq
    for p in points:
        eq += p
        if eq > peak:
            peak = eq
        if peak - eq > dd:
            dd = peak - eq
    return dd, eq, peak


def four_measure_drawdowns(per_window_trades, per_window_daily):
    """values-spec §8 :139 (SETTLED): worst of four per window.

    per_window_trades: list (per window) of trade P&L in exit order.
    per_window_daily:  list (per window) of daily P&L, one value per OOS session.
    Measures, each a positive dollar drawdown:
      ct_start  closed-trade equity, reset to 0 at window start (peak includes the 0)
      eod_start end-of-day equity, reset to 0 at window start
      ct_carry  closed-trade equity on the joined OOS curve from window 1 (running peak carried)
      eod_carry end-of-day equity on the joined OOS curve from window 1 (running peak carried)
    INFERRED (values-spec §8 :139 "carried across windows"): "carried" = equity and its
    running peak continue across windows on the joined OOS curve that starts at 0 before
    window 1; a window's carried drawdown is the worst depth below that peak at the
    window's start (the carried-in state) and at the window's own points (its trades, or
    its session ends). A window with no trades therefore shows the depth it inherits in
    both ct_carry and eod_carry. All arithmetic is exact (Fractions).
    """
    out = []
    ct_eq = ct_pk = Fraction(0)
    eod_eq = eod_pk = Fraction(0)
    for trades, daily in zip(per_window_trades, per_window_daily):
        trades = [exact(p) for p in trades]
        daily = [exact(x) for x in daily]
        ct_start = _dd_series(trades)[0]
        eod_start = _dd_series(daily)[0]
        ct_carry, ct_eq, ct_pk = _dd_series(trades, ct_eq, ct_pk)
        eod_carry, eod_eq, eod_pk = _dd_series(daily, eod_eq, eod_pk)
        m = {"ct_start": ct_start, "eod_start": eod_start,
             "ct_carry": ct_carry, "eod_carry": eod_carry}
        m["worst"] = max(m.values())
        out.append(m)
    return out


def analyse_arm(sel, mnq_commission):
    ws = sel["windows"]
    # Exact: NQ daily is the exact sum of the exact trade nets per exit session (validated
    # above to equal oos_daily within 1e-6), so equity carries no float residue.
    nq_trades, nq_daily, mnq_trades, mnq_daily = [], [], [], []
    for w in ws:
        a = w["oos"][0]
        span = w["oos"][1] - a + 1
        nt = [exact(t["net_pnl"]) for t in w["oos_trade_list"]]
        tr = [mnq_from_nq_gross(t["gross_pnl"], mnq_commission) for t in w["oos_trade_list"]]
        dn = [Fraction(0)] * span
        d = [Fraction(0)] * span
        for t, pn, p in zip(w["oos_trade_list"], nt, tr):
            dn[t["session"] - a] += pn
            d[t["session"] - a] += p   # MNQ daily = sum of MNQ trade P&L per exit session
        nq_trades.append(nt)
        nq_daily.append(dn)
        mnq_trades.append(tr)
        mnq_daily.append(d)
    dd_nq = four_measure_drawdowns(nq_trades, nq_daily)
    dd_mnq = four_measure_drawdowns(mnq_trades, mnq_daily)
    joined = [p for tr in nq_trades for p in tr]
    joined_daily = [float(x) for d in nq_daily for x in d]   # information-only Sharpe (float)
    pf, pf_reason = profit_factor(joined)
    # INFERRED: a window is profitable iff OOS net > 0; exactly 0 is not profitable.
    # The net is the exact sum of the window's trade nets.
    # values-spec §6 :96: a no-eligible window (arm b trades nothing) counts not profitable.
    profitable = [(sum(tr, Fraction(0)) > 0) and not w.get("no_eligible", False)
                  for w, tr in zip(ws, nq_trades)]
    return {
        "dd_nq": dd_nq, "dd_mnq": dd_mnq,
        "worst_nq": max((m["worst"] for m in dd_nq), default=Fraction(0)),
        "worst_mnq": max((m["worst"] for m in dd_mnq), default=Fraction(0)),
        "pf": pf, "pf_reason": pf_reason,
        "sharpe6": sharpe_daily(joined_daily),
        "trades": sel["oos_total_trades"],   # validated int >= 0 (W8, ADV-D D6)
        # W8 fix (ADV-D D5): print the exact sums the verdicts use, not the file's floats.
        "net": sum(joined, Fraction(0)),
        "win_net": [sum(tr, Fraction(0)) for tr in nq_trades],
        "profitable": profitable,
        "n_profitable": sum(profitable),
        "K": len(ws),
    }


def pnl_basis_of(sel):
    """Print-only: the input pnl basis if the selection JSON carries it.
    UNVERIFIED: whether NT8's `pnl` is gross or net (contract Interface 2; values-spec §7)."""
    m = sel.get("pnl_basis_in")
    if isinstance(m, dict) and m:
        # select.py writes {column: basis}; print each distinct basis with its columns count
        # (one column for arm (a), 81 for arm (b)); a mixed map lists the minority columns.
        by_basis = {}
        for col in sorted(m):
            by_basis.setdefault(str(m[col]), []).append(col)
        if len(by_basis) == 1:
            (b, cols), = by_basis.items()
            return "{} ({} column{})".format(b, len(cols), "" if len(cols) == 1 else "s")
        return "MIXED: " + "; ".join("{} ({} column{}: {})".format(
            b, len(cols), "" if len(cols) == 1 else "s", ", ".join(cols))
            for b, cols in sorted(by_basis.items()))
    for key in ("pnl_basis_in", "pnl_basis"):
        if key in sel:
            return str(sel[key])
    seen = sorted({str(t[k]) for w in sel["windows"] for t in w["oos_trade_list"]
                   for k in ("pnl_basis_in",) if k in t})
    if seen:
        return ", ".join(seen)
    return "not present in the selection JSON"


# ----------------------------------------------------------------- rendering

def render(cal, sel_a, sel_b, pbo, commission_nq, commission_mnq, cost_label=COST_MODEL_REL):
    A = analyse_arm(sel_a, commission_mnq)
    B = analyse_arm(sel_b, commission_mnq)
    L = []
    L.append("# PRAXIS walk-forward report — arm (a) and arm (b)")
    L.append("")
    L.append(STANDING_LIMITATION)
    L.append("")
    L.append("## Status of this result")
    L.append("")
    L.append("PROVISIONAL. This Standard-resolution, breaker-less walk-forward gives a provisional "
             "result; it is not by itself the go/no-go judgement (values-spec §2 :42).")
    L.append("")
    L.append("- Judged arm = (a) (ruling 4 of 2026-11-06: \"judged arm = (a) fixed rules\").")
    L.append("- Q8: \"both arms are judged against all six Phase 3 gates\". Both arms are printed "
             "below; this report does not reconcile the two statements (values-spec §8 :128).")
    L.append("- Calendar: N = {} sessions, K = {} windows, OOS sessions = {}.".format(
        cal["N"], cal["K"], sum(w["oos"][1] - w["oos"][0] + 1 for w in cal["windows"])))
    # W9 fix (ADV-E 2): name the cost model file actually read.
    L.append("- Costs: NQ round turn ${}, MNQ round turn ${} ({}).".format(
        money(commission_nq), money(commission_mnq), cost_label))
    L.append("")

    for arm, sel, R in (("a", sel_a, A), ("b", sel_b, B)):
        L.extend(render_gates(arm, sel, R, pbo))
    L.extend(render_drawdown_notes(commission_mnq))
    for arm, sel, R in (("a", sel_a, A), ("b", sel_b, B)):
        L.extend(render_windows(arm, sel, R, cal))
    L.append("## Arm (a) full-span total (values-spec §2 :43)")
    L.append("")
    L.append("- Net (1 NQ): ${}; trades: {}".format(money(sel_a["full_span"]["net"]),
                                                  sel_a["full_span"]["trades"]))
    L.append("")
    L.extend(render_open(sel_a, sel_b))
    return "\n".join(L) + "\n"


def render_gates(arm, sel, R, pbo):
    L = ["## Arm ({}) — the six Phase 3 gates".format(arm), ""]
    L.append("Gates quoted from docs/specs/2026-11-05-phase3-build-specification.md:80-85.")
    L.append("")
    # Gate 1
    if R["pf"] is None:
        g1 = "{} — not a pass".format(R["pf_reason"])
    else:
        # W8 fix (ADV-D D5): the printed PF is exact, or cut down (floor) at 10 places, so it
        # is always on the same side of 1.30 as the exact value the verdict uses.
        g1 = "{} (PF = {}; exact fraction {}/{}, compared exactly with 1.30)".format(
            "PASS" if R["pf"] >= PF_THRESHOLD else "FAIL", exact_decimal(R["pf"], 4, 10),
            R["pf"].numerator, R["pf"].denominator)
    L.append("1. {} — {}. Computed over the joined OOS trade list as sum of positive net P&L / "
             "|sum of negative net P&L| (NT8-style; INFERRED as the gate's meaning).".format(GATES[0], g1))
    # Gate 2
    s6 = "undefined" if R["sharpe6"] is None else "{:.4f}".format(R["sharpe6"])
    L.append("2. {} — OPEN. The gate's Sharpe definition and equity base are OPEN under ruling 9 "
             "(values-spec §6 :93). For information: §6 daily Sharpe of the joined OOS series "
             "= {} (§6 selection statistic — NOT the gate's definition).".format(GATES[1], s6))
    # Gate 3
    L.append("3. {} — NO SINGLE VERDICT. Base = \"the lower of 4% of the MFFU account size and "
             "MFFU's trailing drawdown limit\" (D-2026-11-05-A item 3); no tier is chosen (Q9). "
             "Worst drawdown over all windows: 1 NQ ${}, 1 MNQ ${}. Per-tier table below. The "
             "equity-base item stays OPEN (values-spec §8 :135).".format(
                 GATES[2], money(R["worst_nq"]), money(R["worst_mnq"])))
    # Gate 4
    L.append("4. {} — {} ({} OOS trades).".format(
        GATES[3], "PASS" if R["trades"] >= TRADES_THRESHOLD else "FAIL", R["trades"]))
    # Gate 5
    ok5 = R["n_profitable"] * 100 >= PROFITABLE_PCT * R["K"]
    L.append("5. {} — {} ({}/{} windows profitable; profitable iff OOS net > 0, 0 is not "
             "profitable (INFERRED); a no-eligible window counts not profitable (values-spec §6 :96)).".format(
                 GATES[4], "PASS" if ok5 else "FAIL", R["n_profitable"], R["K"]))
    # Gate 6
    L.append("6. {} — OPEN. The WFE formula for arm (b) and whether the gate applies to arm (a) "
             "are OPEN (ruling 9; values-spec §8 :132-133). Nothing computed.".format(GATES[5]))
    L.append("")
    if arm == "b":
        ok = pbo_passes(pbo)
        # W8 fix (ADV-D D5): print le0/splits and its exact (or floor-cut) decimal, never a
        # rounding that lands on the other side of 0.05.
        L.append("PBO = le0/splits = {}/{} = {} (compared exactly with 0.05). PBO < 0.05 — {}.".format(
            pbo["le0"], pbo["splits"], exact_decimal(Fraction(pbo["le0"], pbo["splits"]), 4, 10),
            "PASS" if ok else "FAIL"))
        if not ok:
            L.append("")
            L.append("**arm (b) does not count** (PBO ≥ 0.05; values-spec §8 :129).")
        L.append("")
    L.append("### Arm ({}) gate 3 per-tier table (WF spec §6 :113-131; no tier chosen)".format(arm))
    L.append("")
    L.append("| Plan · size | Account size | 4% of size | MFFU limit | Limit used (lower) | "
             "Worst DD 1 NQ | 1 NQ | Worst DD 1 MNQ | 1 MNQ | WF spec line |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for label, size, four, lim_txt, lower, line in TIERS:
        if lower is None:
            L.append("| {} | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | ${} | UNVERIFIED | "
                     "${} | UNVERIFIED | :{} |".format(label, money(R["worst_nq"]), money(R["worst_mnq"]), line))
            continue
        L.append("| {} | ${:,} | ${:,} | {} | ${:,} | ${} | {} | ${} | {} | :{} |".format(
            label, size, four, lim_txt, lower,
            money(R["worst_nq"]), "within" if R["worst_nq"] <= lower else "exceeds",
            money(R["worst_mnq"]), "within" if R["worst_mnq"] <= lower else "exceeds", line))
    L.append("")
    return L


def render_drawdown_notes(commission_mnq):
    return [
        "## Drawdown basis (values-spec §8 :139, SETTLED)",
        "",
        "- Per window, the worst of four: closed-trade equity and end-of-day equity, each (i) from the "
        "window's start (equity reset to 0) and (ii) carried across windows on the joined OOS curve "
        "from window 1. The \"carried\" reading is INFERRED.",
        "- Intrabar equity is not available (not in the trade lists); drawdown below is on closed "
        "trades and session ends only.",
        # W9 fix (ADV-E 2): the formula prints the MNQ cost actually used (refused unless $1.90).
        "- 1 MNQ per trade = (NQ gross / 10) − ${}; MNQ daily = sum of MNQ trade P&L per exit "
        "session. That this equals an own MNQ run is INFERRED.".format(money(commission_mnq)),
        "",
    ]


def render_windows(arm, sel, R, cal):
    L = ["## Arm ({}) per-window table".format(arm), ""]
    L.append("| k | IS dates | OOS dates | pick | eligible | OOS net (NQ) | OOS trades | profitable? | "
             "worst DD NQ | worst DD MNQ | IS holes | OOS holes | IS early-close | OOS early-close |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, (w, cw) in enumerate(zip(sel["windows"], cal["windows"])):
        if arm == "b":
            pick = w["pick"] if w["pick"] is not None else "none (no eligible)"
        else:
            pick = "— (fixed rules)"
        el = "—" if w["eligible"] is None else w["eligible"]   # W9 (ADV-E note): never "None"
        L.append("| {} | {} → {} | {} → {} | {} | {} | ${} | {} | {} | ${} | ${} | {} | {} | {} | {} |".format(
            cw["k"], cw["is_dates"][0], cw["is_dates"][1], cw["oos_dates"][0], cw["oos_dates"][1],
            pick, el, money(R["win_net"][i]), w["oos_trades"],
            "yes" if R["profitable"][i] else "no",
            money(R["dd_nq"][i]["worst"]), money(R["dd_mnq"][i]["worst"]),
            cw["is_holes"], cw["oos_holes"], cw["is_early_close"], cw["oos_early_close"]))
    if has_data_gap_early_close(cal):
        L.append("")
        L.append(EARLY_CLOSE_FOOTNOTE)
    L.append("")
    L.append("Overall worst drawdown (max over windows): 1 NQ ${}; 1 MNQ ${}. OOS total: ${} net, {} trades.".format(
        money(R["worst_nq"]), money(R["worst_mnq"]), money(R["net"]), R["trades"]))
    L.append("")
    L.extend(render_window_tier_matrix(arm, R))
    return L


def render_window_tier_matrix(arm, R):
    """values-spec §8 :136: per-window worst drawdown at 1 MNQ and 1 NQ against every
    row of the WF spec §6 tier table. Exact comparison against each row's limit."""
    K = len(R["dd_nq"])
    L = ["### Arm ({}) per-window × tier matrix (values-spec §8 :136; WF spec §6 :113-131; "
         "no tier chosen)".format(arm), ""]
    L.append("Legend: each cell is NQ/MNQ for that window's worst drawdown (1 NQ / 1 MNQ) against "
             "the row's limit used (the lower of 4% of size and the MFFU limit); W = within "
             "(≤ limit), E = exceeds (> limit). Flex = UNVERIFIED.")
    L.append("")
    L.append("| Plan · size | Limit used (lower) | " + " | ".join("W{}".format(k) for k in range(1, K + 1)) + " |")
    L.append("|---|---|" + "---|" * K)
    for label, size, four, lim_txt, lower, line in TIERS:
        if lower is None:
            L.append("| {} | UNVERIFIED | ".format(label) + " | ".join(["UNVERIFIED"] * K) + " |")
            continue
        cells = ["{}/{}".format("W" if R["dd_nq"][i]["worst"] <= lower else "E",
                                "W" if R["dd_mnq"][i]["worst"] <= lower else "E") for i in range(K)]
        L.append("| {} | ${:,} | ".format(label, lower) + " | ".join(cells) + " |")
    L.append("")
    return L


def render_open(sel_a, sel_b):
    return [
        "## Open — Amear's / not decided here",
        "",
        "- Tier pick (Q9: no tier chosen; he picks after paper results).",
        "- Gate 2: the Sharpe definition and the equity base (ruling 9; values-spec §6 :93).",
        "- Gate 6: walk-forward efficiency — formula for arm (b), applicability to arm (a) "
        "(ruling 9; values-spec §8 :132-133).",
        "- Whether GO / HOLD / REJECT may rest on arm (b) (ruling 9; values-spec §8 :132 (iii)).",
        "- Whether NT8's `pnl` is gross or net — UNVERIFIED. Input pnl basis: arm (a) {}; arm (b) {}.".format(
            pnl_basis_of(sel_a), pnl_basis_of(sel_b)),
        "- NT8 trade export format — UNVERIFIED.",
    ]


# ----------------------------------------------------------------- CLI

def build(cal_path, sel_a_path, sel_b_path, pbo_path, cost_path):
    commission_nq, commission_mnq = load_costs(cost_path)
    cal = load_json(cal_path, "calendar")
    validate_calendar(cal)
    sel_a = load_json(sel_a_path, "selection arm (a)")
    sel_b = load_json(sel_b_path, "selection arm (b)")
    validate_selection(sel_a, cal, "a", commission_nq)
    validate_selection(sel_b, cal, "b", commission_nq)
    pbo = load_json(pbo_path, "pbo")
    validate_pbo(pbo, cal)
    text = render(cal, sel_a, sel_b, pbo, commission_nq, commission_mnq, cost_label(cost_path))
    # Final guard (W7 fix, ADV-C D3; values-spec :7, S13): the standing sentence occurs
    # exactly once, at line 3. Anything else is refused before the file is written.
    # W8 fix (ADV-D D1): count look-alikes too — NFKC, format characters removed, whitespace
    # collapsed, case folded. "fills are optimistic" must occur exactly once, in line 3.
    n = _norm(text).count(STANDING_PHRASE)
    lines = text.splitlines()
    if n != 1 or len(lines) < 3 or lines[2] != STANDING_LIMITATION or _norm(lines[2]).count(STANDING_PHRASE) != 1:
        _fail("rendered report has the standing sentence {} time(s) / not at line 3 — not written".format(n))
    return text


STANDING_PHRASE = "fills are optimistic"


def _norm(text):
    t = unicodedata.normalize("NFKC", text)
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Cf")
    return re.sub(r"\s+", " ", t).casefold()


def _repo_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def default_cost_path():
    return os.path.join(_repo_root(), COST_MODEL_REL)


def cost_label(path):
    """W9 fix (ADV-E 2): the cost model path actually read — repo-relative when inside the
    repo (so the default prints config/backtest-cost-model.json on any checkout), else absolute."""
    ap = os.path.abspath(path)
    try:
        rel = os.path.relpath(ap, _repo_root())
    except ValueError:
        return ap
    if rel == os.pardir or rel.startswith(os.pardir + os.sep):
        return ap
    return rel.replace(os.sep, "/")


def _one_line(msg):
    return re.sub(r"[\r\n]+", " ", str(msg))


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Walk-forward §8 report (values-spec v2.1) for arm (a) and arm (b). "
                    "Reads calendar / selection / PBO JSON; writes deterministic Markdown. "
                    "Refuses truncated inputs and windows that do not match the calendar.")
    ap.add_argument("--calendar", required=True, help="calendar JSON (contract Interface 1)")
    ap.add_argument("--sel-a", required=True, help="arm (a) selection JSON (Interface 3)")
    ap.add_argument("--sel-b", required=True, help="arm (b) selection JSON (Interface 3)")
    ap.add_argument("--pbo", required=True, help="PBO JSON (Interface 4)")
    ap.add_argument("--out", required=True, help="output Markdown path")
    ap.add_argument("--cost-model", default=None,
                    help="cost model JSON (default: <repo>/config/backtest-cost-model.json; read only)")
    args = ap.parse_args(argv)
    try:
        text = build(args.calendar, args.sel_a, args.sel_b, args.pbo,
                     args.cost_model or default_cost_path())
        try:
            with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
        except OSError as e:   # W9 fix (ADV-E 1): e.g. --out is a directory
            _fail("cannot write --out {}: {}: {}".format(args.out, type(e).__name__, e))
    except ReportInputError as e:
        print("report.py: REFUSED: {}".format(_one_line(e)), file=sys.stderr)
        return 2
    except Exception as e:   # W9 fix (ADV-E 1): top-level guard — never a traceback, never silent
        print("report.py: REFUSED: unexpected {} while loading, validating or writing: {}".format(
            type(e).__name__, _one_line(e)), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
