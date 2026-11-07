#!/usr/bin/env python3
"""tradelist.py -- bridge trade-list JSON / NT8 trade-list CSV -> canonical daily series.

Produces Interface 2 (schema "praxis-wf-daily/1") of the unit contract
2026-11-07-wf-mac-side-maths. Standard library only. Run with `python3 -I`.

Spec = docs/specs/2026-11-06-walk-forward-values.md (v2.1), cited "values-spec".
Bridge payload = docs/reports/2026-11-06-cli-nt-bridge-code-read.md (B14/B15,
NT8BridgeServer.cs:2812-2863) -- CODE READ, NEVER RUN. No bridge response has
been observed by this code's author.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys
from datetime import datetime
from decimal import Decimal

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

SCHEMA = "praxis-wf-daily/1"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_COST_MODEL = os.path.join(REPO_ROOT, "config", "backtest-cost-model.json")

# UNVERIFIED: the bridge's success string for `status`. The code read (B14) shows the
# key but no observed value. Only these values are accepted unless --accept-status adds one.
OK_STATUSES = ("ok",)

# Bridge list cap, NT8BridgeServer.cs:2844 (`int cap = nTrades < 5000 ? nTrades : 5000;`),
# REPORTED BY the bridge report B15 (code read). values-spec §7 :112: exactly 5000 = truncated.
BRIDGE_TRADE_CAP = 5000

# values-spec §9 inputs table: property names exactly these; ExitPolicy sent BY NAME
# (values-spec oracle input (d)).
PARAM_KEYS = ("Lookback", "NoiseMult", "StopAtrMult", "ExitPolicy", "Contracts")
GRID_LOOKBACK = (10, 14, 18)              # values-spec §3 :49 (RULED, Q2)
GRID_NOISEMULT = (0.8, 1.0, 1.2)          # values-spec §3 :50 (RULED, Q2)
GRID_STOPATRMULT = (1.5, 2.25, 3.0)       # values-spec §3 :51 (SETTLED, D-2026-11-07-A)
GRID_EXITPOLICY = ("BandOrVWAP", "OppBand", "Flat1559")  # values-spec §3 :52 (RULED, ruling 4)
WF_CONTRACTS = 1                          # values-spec §2 :41 (Contracts = 1); WF runs at 1 NQ

# 81 param dicts in the values-spec §6 lexicographic order: lookback asc, k asc, m asc,
# policy BandOrVWAP, OppBand, Flat1559. Every run sends all five inputs (values-spec §7 :111).
GRID = [
    {"Lookback": lb, "NoiseMult": k, "StopAtrMult": m, "ExitPolicy": pol, "Contracts": WF_CONTRACTS}
    for lb in GRID_LOOKBACK for k in GRID_NOISEMULT for m in GRID_STOPATRMULT for pol in GRID_EXITPOLICY
]

# UNVERIFIED: NT8 Strategy Analyzer "Trades" tab CSV export headers. Nobody on this project
# has observed an export; this is the documented Trades-grid column set as best known.
# Any mismatch fails loudly with a diff -- the constant must be corrected from a real file.
EXPECTED_NT8_COLUMNS = (
    "Trade number", "Instrument", "Account", "Strategy", "Market pos.", "Qty",
    "Entry price", "Exit price", "Entry time", "Exit time", "Entry name", "Exit name",
    "Profit", "Cum. net profit", "Commission", "MAE", "MFE", "ETD", "Bars",
)
# UNVERIFIED: NT8 CSV date/time formats (locale-dependent; en-US assumed first).
NT8_CSV_TIME_FORMATS = ("%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S")


class TradelistError(Exception):
    """Bad input: the run must stop (fail loudly)."""


class NotSettledBySpec(TradelistError):
    """A choice the spec does not settle; this code refuses to make it."""

    def __init__(self, what):
        super().__init__("NotSettledBySpec: " + what)


# ---------------------------------------------------------------------------------------
# naming / grid
# ---------------------------------------------------------------------------------------

def column_name(params):
    """`L{Lookback}_k{NoiseMult:.1f}_m{StopAtrMult:g}_{ExitPolicy}`; None -> "armA"."""
    if params is None:
        return "armA"
    return "L{}_k{:.1f}_m{:g}_{}".format(
        int(params["Lookback"]), float(params["NoiseMult"]), float(params["StopAtrMult"]),
        params["ExitPolicy"])


def validate_params(params):
    """Return the GRID entry equal to `params`; fail loudly otherwise."""
    if not isinstance(params, dict):
        raise TradelistError("params must be a JSON object, got %r" % (params,))
    keys = set(params)
    if keys != set(PARAM_KEYS):
        raise TradelistError("params keys must be exactly %s (values-spec §7 :111, every run sends "
                             "all five); missing %s, extra %s" % (
                                 list(PARAM_KEYS), sorted(set(PARAM_KEYS) - keys),
                                 sorted(keys - set(PARAM_KEYS))))
    c = params["Contracts"]
    if isinstance(c, bool) or not isinstance(c, int):
        raise TradelistError("params.Contracts must be an integer, got %r" % (c,))
    if c != WF_CONTRACTS:
        raise NotSettledBySpec("Contracts=%r; the walk-forward runs at 1 (values-spec §2 :41) and the "
                               "bridge list has no quantity, so P&L scaling for Contracts != 1 is not "
                               "defined here" % (c,))
    if not isinstance(params["ExitPolicy"], str):
        raise TradelistError("params.ExitPolicy must be sent BY NAME (values-spec oracle input (d)), "
                             "got %r" % (params["ExitPolicy"],))
    for k in ("Lookback", "NoiseMult", "StopAtrMult"):
        v = params[k]
        if isinstance(v, bool) or not isinstance(v, (int, float, Decimal)):
            raise TradelistError("params.%s must be a number, got %r" % (k, v))
    for g in GRID:
        if (int(params["Lookback"]) == params["Lookback"] and g["Lookback"] == int(params["Lookback"])
                and g["NoiseMult"] == float(params["NoiseMult"])
                and g["StopAtrMult"] == float(params["StopAtrMult"])
                and g["ExitPolicy"] == params["ExitPolicy"]):
            return dict(g)
    raise TradelistError("params %r are not one of the 81 GRID configurations (values-spec §3 :49-52)"
                         % (params,))


# ---------------------------------------------------------------------------------------
# inputs
# ---------------------------------------------------------------------------------------

def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _reject_constant(name):
    raise TradelistError("non-finite number %s in JSON input" % name)


def load_cost_model(path):
    """cost_model.commission_round_turn_usd as Decimal (values-spec §7 :115, RULED $4.68)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = json.load(f, parse_float=Decimal, parse_constant=_reject_constant)
    except (OSError, ValueError) as e:
        raise TradelistError("cannot read cost model %s: %s" % (path, e))
    try:
        v = doc["cost_model"]["commission_round_turn_usd"]
    except (KeyError, TypeError):
        raise TradelistError("cost model %s has no cost_model.commission_round_turn_usd" % path)
    if isinstance(v, bool) or not isinstance(v, (int, Decimal)) or v < 0:
        raise TradelistError("cost model commission_round_turn_usd must be a number >= 0, got %r" % (v,))
    return Decimal(v)


def load_calendar_any(path):
    """Use W1's sessions.load_calendar/date_to_session when present; else read Interface 1 directly."""
    try:
        import sessions  # noqa: sibling module (W1)
    except ImportError:
        sessions = None
    if sessions is not None:
        try:
            cal = sessions.load_calendar(path)
            d2s = sessions.date_to_session(cal)
        except (OSError, ValueError, KeyError, TypeError, getattr(sessions, "DataError", ValueError)) as e:
            raise TradelistError("cannot load calendar %s via sessions.py: %s: %s" % (path, type(e).__name__, e))
    else:
        try:
            with open(path, "r", encoding="utf-8") as f:
                cal = json.load(f)
        except (OSError, ValueError) as e:
            raise TradelistError("cannot read calendar %s: %s" % (path, e))
        try:
            d2s = {s["date"]: int(s["n"]) for s in cal["sessions"]}
        except (KeyError, TypeError, ValueError) as e:
            raise TradelistError("calendar %s: bad sessions[] (need n, date): %s" % (path, e))
    if not isinstance(cal, dict) or "N" not in cal or "sessions" not in cal:
        raise TradelistError("calendar %s lacks N / sessions (Interface 1)" % path)
    N = cal["N"]
    ns = sorted(d2s.values())
    if len(cal["sessions"]) != N or len(d2s) != N or ns != list(range(1, N + 1)):
        raise TradelistError("calendar %s inconsistent: N=%r, %d sessions, %d unique dates, n not 1..N"
                             % (path, N, len(cal["sessions"]), len(d2s)))
    return cal, d2s


_TIME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,7}))?$")


def parse_nt_time(s):
    """Parse .NET DateTime.ToString("o") for DateTimeKind.Unspecified, e.g.
    "2021-03-29T10:01:00.0000000" (7 fractional digits), into a naive datetime.

    INFERRED (bridge report B15, NT8BridgeServer.cs:2849-2852): times are tz-naive NT chart
    wall clock. A value with an offset or "Z" (Kind Local/Utc) fails loudly rather than
    being converted. A 7th fractional digit that is not 0 (sub-microsecond) also fails.
    """
    if not isinstance(s, str) or not s:
        raise TradelistError("empty or non-string time %r (bridge writes \"\" when Entry/Exit is null)" % (s,))
    m = _TIME_RE.match(s)
    if not m:
        raise TradelistError("time %r is not tz-naive ISO 'YYYY-MM-DDTHH:MM:SS[.fffffff]'" % (s,))
    y, mo, d, hh, mi, ss, frac = m.groups()
    us = 0
    if frac:
        frac7 = frac.ljust(7, "0")
        if frac7[6] != "0":
            raise TradelistError("time %r has sub-microsecond precision" % (s,))
        us = int(frac7[:6])
    try:
        return datetime(int(y), int(mo), int(d), int(hh), int(mi), int(ss), us)
    except ValueError as e:
        raise TradelistError("time %r invalid: %s" % (s, e))


def _side(v, where):
    if v not in ("Long", "Short"):
        raise TradelistError("%s: market position %r is not 'Long' or 'Short'" % (where, v))
    return v


def load_bridge_file(path, ok_statuses):
    """Read one bridge backtest_<id>.json. Returns a source dict with parsed trades."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = json.load(f, parse_float=Decimal, parse_constant=_reject_constant)
    except (OSError, ValueError) as e:
        raise TradelistError("cannot read bridge file %s: %s" % (path, e))
    if not isinstance(doc, dict):
        raise TradelistError("%s: top level is not an object" % path)
    for k in ("status", "metrics", "trades"):
        if k not in doc:
            raise TradelistError("%s: missing top-level key %r (B14: {id,status,strategy,metrics,trades})"
                                 % (path, k))
    if doc["status"] not in ok_statuses:
        raise TradelistError("%s: status %r not in accepted %r (success string UNVERIFIED; use "
                             "--accept-status only after observing a real success response)"
                             % (path, doc["status"], list(ok_statuses)))
    metrics = doc["metrics"]
    trades = doc["trades"]
    if not isinstance(metrics, dict) or not isinstance(trades, list):
        raise TradelistError("%s: metrics must be an object and trades a list" % path)
    tt = metrics.get("totalTrades")
    if isinstance(tt, bool) or not isinstance(tt, int):
        raise TradelistError("%s: metrics.totalTrades missing or not an integer: %r" % (path, tt))
    n = len(trades)
    if n > BRIDGE_TRADE_CAP:
        raise TradelistError("%s: %d trades exceeds the bridge cap %d (code read B15) -- not a bridge file?"
                             % (path, n, BRIDGE_TRADE_CAP))
    if tt < n:
        raise TradelistError("%s: metrics.totalTrades=%d < len(trades)=%d" % (path, tt, n))
    # values-spec §7 :112: exactly 5000 returned = truncated; totalTrades > listed also means cut.
    truncated = (n == BRIDGE_TRADE_CAP) or (tt > n)

    parsed = []
    for i, t in enumerate(trades):
        where = "%s trade[%d]" % (path, i)
        if not isinstance(t, dict):
            raise TradelistError("%s: not an object" % where)
        for k in ("pnl", "marketPosition", "entryTime", "exitTime", "exitName"):
            if k not in t:
                raise TradelistError("%s: missing key %r" % (where, k))
        pnl = t["pnl"]
        if isinstance(pnl, bool) or not isinstance(pnl, (int, Decimal)):
            raise TradelistError("%s: pnl %r is not a number" % (where, pnl))
        en, ex = parse_nt_time(t["entryTime"]), parse_nt_time(t["exitTime"])
        if ex < en:
            raise TradelistError("%s: exitTime %s before entryTime %s" % (where, t["exitTime"], t["entryTime"]))
        parsed.append({"entry": en, "exit": ex, "side": _side(t["marketPosition"], where),
                       "pnl": Decimal(pnl), "exit_name": str(t["exitName"])})

    if not truncated:
        # Internal consistency ONLY: the list sums to the bridge's own netProfit (CumProfit) and
        # its count equals totalTrades. This does NOT establish whether pnl is gross or net of the
        # template commission -- that stays UNVERIFIED (values-spec §7 :113).
        # UNVERIFIED: that the bridge's Num() keeps enough digits for 0.01 over ~1300 trades.
        npf = metrics.get("netProfit")
        if isinstance(npf, bool) or not isinstance(npf, (int, Decimal)):
            raise TradelistError("%s: metrics.netProfit missing or not a number: %r" % (path, npf))
        s = sum((p["pnl"] for p in parsed), Decimal(0))
        if abs(s - Decimal(npf)) > Decimal("0.01"):
            raise TradelistError("%s: sum(trades.pnl)=%s != metrics.netProfit=%s (|diff|=%s > 0.01)"
                                 % (path, s, npf, abs(s - Decimal(npf))))
        if n != tt:
            raise TradelistError("%s: len(trades)=%d != metrics.totalTrades=%d" % (path, n, tt))

    return {"path": path, "sha256": _sha256(path), "n_trades": n, "truncated": truncated,
            "metrics": _plain(metrics), "strategy": doc.get("strategy"),
            "file_params": doc.get("params", None), "has_params": "params" in doc, "trades": parsed}


def _plain(o):
    """Decimals -> float for output."""
    if isinstance(o, Decimal):
        return float(o)
    if isinstance(o, dict):
        return {k: _plain(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_plain(v) for v in o]
    return o


_MONEY_RE = re.compile(r"^(-)?\(?(-)?\$?([0-9][0-9,]*(?:\.[0-9]+)?)\)?$")


def _parse_money(s, where):
    # UNVERIFIED: NT8 CSV currency formatting ("$1,234.50", "-$45.00" or "($45.00)" assumed).
    raw = s.strip()
    m = _MONEY_RE.match(raw)
    if not m:
        raise TradelistError("%s: cannot parse money %r (format UNVERIFIED)" % (where, s))
    neg = bool(m.group(1) or m.group(2) or (raw.startswith("(") and raw.endswith(")")))
    v = Decimal(m.group(3).replace(",", ""))
    return -v if neg else v


def _parse_csv_time(s, where):
    for fmt in NT8_CSV_TIME_FORMATS:
        try:
            return datetime.strptime(s.strip(), fmt)
        except ValueError:
            pass
    raise TradelistError("%s: cannot parse time %r with UNVERIFIED formats %r" % (where, s, NT8_CSV_TIME_FORMATS))


def load_nt8_csv(path, contracts):
    """Read an NT8 Strategy Analyzer Trades-tab CSV export. FORMAT UNVERIFIED (never observed)."""
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))  # UNVERIFIED: comma delimiter
    except (OSError, UnicodeDecodeError) as e:
        raise TradelistError("cannot read NT8 CSV %s: %s" % (path, e))
    if not rows:
        raise TradelistError("%s: empty CSV" % path)
    header = tuple(h.strip() for h in rows[0])
    if header != EXPECTED_NT8_COLUMNS:
        exp, got = list(EXPECTED_NT8_COLUMNS), list(header)
        raise TradelistError(
            "%s: NT8 CSV header mismatch (EXPECTED_NT8_COLUMNS is UNVERIFIED)\n  expected: %r\n  found:    %r\n"
            "  missing:  %r\n  extra:    %r" % (path, exp, got, [c for c in exp if c not in got],
                                                [c for c in got if c not in exp]))
    idx = {c: i for i, c in enumerate(header)}
    parsed = []
    for r, row in enumerate(rows[1:], start=2):
        where = "%s line %d" % (path, r)
        if not any(c.strip() for c in row):
            continue
        if len(row) != len(header):
            raise TradelistError("%s: %d fields, header has %d" % (where, len(row), len(header)))
        try:
            qty = int(row[idx["Qty"]].strip())
        except ValueError:
            raise TradelistError("%s: Qty %r is not an integer" % (where, row[idx["Qty"]]))
        if qty != contracts:
            raise NotSettledBySpec("%s: Qty=%d, the walk-forward runs at %d contract(s)" % (where, qty, contracts))
        en = _parse_csv_time(row[idx["Entry time"]], where)
        ex = _parse_csv_time(row[idx["Exit time"]], where)
        if ex < en:
            raise TradelistError("%s: exit before entry" % where)
        # The Commission column is NOT used: --pnl-basis governs "Profit", commission comes from
        # the cost model, as for the bridge (values-spec §7 :114). UNVERIFIED whether Profit is net.
        parsed.append({"entry": en, "exit": ex, "side": _side(row[idx["Market pos."]].strip(), where),
                       "pnl": _parse_money(row[idx["Profit"]], where),
                       "exit_name": row[idx["Exit name"]].strip()})
    return {"path": path, "sha256": _sha256(path), "n_trades": len(parsed), "truncated": False,
            "metrics": None, "strategy": None, "file_params": None, "has_params": False, "trades": parsed}


# ---------------------------------------------------------------------------------------
# series
# ---------------------------------------------------------------------------------------

def check_sources(sources, params):
    """Several files = one configuration split by date (values-spec §7 :112)."""
    paths = [s["path"] for s in sources]
    if len(set(os.path.realpath(p) for p in paths)) != len(paths):
        raise TradelistError("the same input file is given twice: %r" % paths)
    strategies = set(json.dumps(s["strategy"], sort_keys=True) for s in sources)
    if len(strategies) > 1:
        raise TradelistError("input files name different strategies: %s" % sorted(strategies))
    with_p = [s for s in sources if s["has_params"]]
    # INFERRED: the bridge response (B14) carries no params; if a batch driver embeds them,
    # they must agree with each other and with --params-json.
    for s in with_p:
        fp = _plain(s["file_params"])
        if fp != _plain(with_p[0]["file_params"]):
            raise TradelistError("params differ between %s and %s" % (with_p[0]["path"], s["path"]))
        if params is not None and validate_params(fp) != params:
            raise TradelistError("%s params %r differ from --params-json %r" % (s["path"], fp, params))
    ranges = []
    for s in sources:
        if s["trades"]:
            ranges.append((min(t["entry"] for t in s["trades"]), max(t["exit"] for t in s["trades"]), s["path"]))
    ranges.sort()
    for a, b in zip(ranges, ranges[1:]):
        if b[0] <= a[1]:
            raise TradelistError("trade time ranges overlap: %s [%s .. %s] and %s [%s .. %s]"
                                 % (a[2], a[0].isoformat(), a[1].isoformat(),
                                    b[2], b[0].isoformat(), b[1].isoformat()))


def build_series(cal, d2s, sources, pnl_basis, commission, contracts, params):
    if pnl_basis not in ("net", "gross"):
        raise TradelistError("pnl_basis must be 'net' or 'gross', got %r" % (pnl_basis,))
    if contracts != WF_CONTRACTS:
        raise NotSettledBySpec("contracts=%r (walk-forward runs at 1, values-spec §2 :41)" % (contracts,))
    check_sources(sources, params)
    N = cal["N"]
    # INFERRED: the bridge list has no quantity (B15), so every trade is ASSUMED to be
    # `contracts` contracts; commission per trade = round-turn commission x contracts.
    cost = commission * contracts
    allt = [t for s in sources for t in s["trades"]]
    allt.sort(key=lambda t: (t["exit"], t["entry"]))
    bad_exit = [t for t in allt if t["exit"].date().isoformat() not in d2s]
    if bad_exit:
        raise TradelistError("%d trade(s) exit on a date that is not a calendar session (weekend-dated bars, "
                             "out of range or a hole; values-spec oracle input (b)); first 5: %s"
                             % (len(bad_exit), [t["exit"].isoformat() for t in bad_exit[:5]]))
    # Conservative choice of this module (not in the brief): an entry on a non-session date fails too.
    bad_entry = [t for t in allt if t["entry"].date().isoformat() not in d2s]
    if bad_entry:
        raise TradelistError("%d trade(s) enter on a date that is not a calendar session; first 5: %s"
                             % (len(bad_entry), [t["entry"].isoformat() for t in bad_entry[:5]]))
    daily = [Decimal(0)] * N
    counts = [0] * N
    out_trades = []
    cross = 0
    for t in allt:
        n = d2s[t["exit"].date().isoformat()]   # keyed by EXIT session, values-spec §6 :92
        if d2s[t["entry"].date().isoformat()] != n:
            cross += 1
        if pnl_basis == "gross":   # values-spec §7 :114 SETTLED: subtract $4.68 per round turn
            gross, net = t["pnl"], t["pnl"] - cost
        else:                      # gross kept for the 1 MNQ derivation, values-spec :139
            net, gross = t["pnl"], t["pnl"] + cost
        daily[n - 1] += net
        counts[n - 1] += 1
        out_trades.append({"session": n, "entry_time": t["entry"].isoformat(),
                           "exit_time": t["exit"].isoformat(), "side": t["side"],
                           "net_pnl": float(net), "gross_pnl": float(gross), "exit_name": t["exit_name"]})
    return {
        "schema": SCHEMA,
        "column": column_name(params),
        "params": params,
        "pnl_basis_in": pnl_basis,
        "commission_rt_usd": float(commission),
        "contracts": contracts,
        "truncated": any(s["truncated"] for s in sources),
        "n_trades": len(out_trades),
        "N": N,
        "daily_net": [float(x) for x in daily],
        "daily_trades": counts,
        "trades": out_trades,
        "cross_session_trades": cross,
        "sources": [{"path": s["path"], "sha256": s["sha256"], "n_trades": s["n_trades"],
                     "metrics": s["metrics"]} for s in sources],
    }


def load_daily(path):
    """Read and shape-check an Interface 2 file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError) as e:
        raise TradelistError("cannot read daily series %s: %s" % (path, e))
    if not isinstance(d, dict) or d.get("schema") != SCHEMA:
        raise TradelistError("%s: schema is not %s" % (path, SCHEMA))
    for k in ("column", "params", "pnl_basis_in", "commission_rt_usd", "contracts", "truncated",
              "n_trades", "N", "daily_net", "daily_trades", "trades", "cross_session_trades", "sources"):
        if k not in d:
            raise TradelistError("%s: missing key %r" % (path, k))
    N = d["N"]
    if len(d["daily_net"]) != N or len(d["daily_trades"]) != N:
        raise TradelistError("%s: daily_net/daily_trades length != N=%r" % (path, N))
    if sum(d["daily_trades"]) != d["n_trades"] or len(d["trades"]) != d["n_trades"]:
        raise TradelistError("%s: trade counts inconsistent" % path)
    return d


# ---------------------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------------------

HELP_EPILOG = """\
Output: Interface 2 (schema praxis-wf-daily/1). daily_net[i-1] = sum of NET P&L of trades
EXITED in session i, 0.0 if none (values-spec §6 :92).

--pnl-basis is REQUIRED with no default: whether the bridge's `pnl` (t.ProfitCurrency) is net of
the template commission is UNVERIFIED (values-spec §7 :113). gross: net = pnl - commission x
contracts (§7 :114). net: gross = pnl + commission x contracts (kept for the 1 MNQ derivation).
Commission = cost_model.commission_round_turn_usd of --cost-model. Contracts must be 1; the bridge
list has no quantity, so every trade is ASSUMED to be 1 contract (INFERRED).

Truncation: a file with exactly 5000 trades, or metrics.totalTrades > len(trades), sets
truncated=true for the whole series (values-spec §7 :112). The file is still written, flagged;
downstream selection and PBO REFUSE a truncated series -- rerun or split by date.
Several --bridge files = one configuration split by date: concatenated; overlapping trade time
ranges or differing params/strategy fail. Non-truncated files must satisfy
|sum(pnl) - metrics.netProfit| <= 0.01 and len(trades) == metrics.totalTrades (internal
consistency only, NOT a gross/net check). Bridge status must be in OK_STATUSES=%r (UNVERIFIED).

--nt8-csv: NT8 Strategy Analyzer trade-list CSV. FORMAT UNVERIFIED -- nobody has observed one.
Expected header (UNVERIFIED): %s. Times parsed with UNVERIFIED formats %r; money as
"$1,234.50"/"-$5.00"/"($5.00)" (UNVERIFIED). Any header mismatch fails with a diff; Qty != 1 fails.

Exit date not a calendar session (weekend-dated bar, out of range, hole) fails, listing the
first 5 offenders. Entry session != exit session is counted in cross_session_trades.
""" % (OK_STATUSES, ", ".join(EXPECTED_NT8_COLUMNS), NT8_CSV_TIME_FORMATS)


def build_parser():
    p = argparse.ArgumentParser(
        prog="tradelist.py",
        description="Bridge trade-list JSON / NT8 trade-list CSV -> canonical daily net P&L series "
                    "per calendar session (walk-forward Mac side).",
        epilog=HELP_EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--calendar", required=True, help="calendar JSON from sessions.py (Interface 1)")
    p.add_argument("--pnl-basis", required=True, choices=("net", "gross"),
                   help="REQUIRED, no default: what the input P&L is (UNVERIFIED which NT8 gives)")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--bridge", nargs="+", metavar="FILE", help="bridge backtest_<id>.json file(s)")
    src.add_argument("--nt8-csv", nargs="+", metavar="FILE", help="NT8 trade-list CSV file(s) (UNVERIFIED format)")
    arm = p.add_mutually_exclusive_group(required=True)
    arm.add_argument("--params-json", metavar="JSON",
                     help="arm (b) params, all five keys: " + ", ".join(PARAM_KEYS))
    arm.add_argument("--arm-a", action="store_true", help="arm (a): fixed rules, column armA, params null")
    p.add_argument("--cost-model", default=DEFAULT_COST_MODEL, help="cost model JSON (default: repo config)")
    p.add_argument("--accept-status", action="append", default=[], metavar="S",
                   help="add an accepted bridge status value (the success string is UNVERIFIED)")
    p.add_argument("--out", required=True, help="output daily series JSON")
    return p


def run(args):
    if args.arm_a:
        params, contracts = None, WF_CONTRACTS   # values-spec §2 :41 Contracts = 1
    else:
        try:
            raw = json.loads(args.params_json, parse_constant=_reject_constant)
        except ValueError as e:
            raise TradelistError("--params-json is not valid JSON: %s" % e)
        params = validate_params(raw)
        contracts = params["Contracts"]
    commission = load_cost_model(args.cost_model)
    cal, d2s = load_calendar_any(args.calendar)
    if args.bridge:
        ok = tuple(OK_STATUSES) + tuple(args.accept_status)
        sources = [load_bridge_file(f, ok) for f in args.bridge]
    else:
        sources = [load_nt8_csv(f, contracts) for f in args.nt8_csv]
    series = build_series(cal, d2s, sources, args.pnl_basis, commission, contracts, params)
    try:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(series, f, sort_keys=True, indent=1)
            f.write("\n")
    except OSError as e:
        raise TradelistError("cannot write %s: %s" % (args.out, e))
    return series


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        s = run(args)
    except TradelistError as e:
        sys.stderr.write("tradelist.py: error: %s\n" % e)
        return 1
    sys.stderr.write("tradelist.py: wrote %s: column %s, %d trades, truncated=%s, cross_session=%d\n"
                     % (args.out, s["column"], s["n_trades"], s["truncated"], s["cross_session_trades"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
