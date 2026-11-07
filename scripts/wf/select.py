#!/usr/bin/env python3
"""Walk-forward per-window selection (arm b) and window slicing (arm a).

Unit 2026-11-07-wf-mac-side-maths, worker W3. Standard library only.
Spec: docs/specs/2026-11-06-walk-forward-values.md (v2.1) = "values-spec".

Reads the calendar JSON (contract Interface 1) and canonical daily-series
JSONs (Interface 2) directly; writes the selection JSON (Interface 3).

IMPORT HAZARD (OBSERVED, python3 3.14.7): this file's name shadows the
stdlib extension module `select` (lib-dynload/select.cpython-314-darwin.so),
which `selectors`/`subprocess` import. Never put scripts/wf on sys.path and
`import select`. Load this file by path instead, e.g. via
`load_module_by_path("praxis_wf_select", <path>)` below (pbo.py and the tests
do exactly that).
"""
import argparse
import glob
import hashlib
import importlib.util
import json
import math
import os
import sys
from collections import Counter

SCHEMA_CAL = "praxis-wf-calendar/1"
SCHEMA_DAILY = "praxis-wf-daily/1"
SCHEMA_OUT = "praxis-wf-selection/1"
ARM_A_COLUMN = "armA"   # contract Interface 2 column naming

# values-spec §3 :49-52 grid. Order inside each tuple is the §6 :97
# lexicographic order: "lexicographic, ascending: lookback, then k, then m
# (1.5, 2.25, 3.0), then policy in the order BandOrVWAP, OppBand, Flat1559".
LOOKBACKS = (10, 14, 18)
NOISE_MULTS = (0.8, 1.0, 1.2)
STOP_MULTS = (1.5, 2.25, 3.0)
POLICIES = ("BandOrVWAP", "OppBand", "Flat1559")
PARAM_KEYS = ("Lookback", "NoiseMult", "StopAtrMult", "ExitPolicy", "Contracts")
# §3 :49-52 anchors: Lookback 14, k 1.0, policy BandOrVWAP; m has none (§6 :97).
ANCHOR_LOOKBACK = 14
ANCHOR_K = 1.0
ANCHOR_POLICY = "BandOrVWAP"

# values-spec §6 :97 "Tie-break — SETTLED: equal S to 1e-9".
# INFERRED: absolute tolerance, measured against the best S.
TIE_TOL = 1e-9
# values-spec §6 :94 "100 trades per 252-session in-sample window";
# §7 :105 "minimum trades pro rata, 100 × sessions / 252".
MIN_TRADES = 100
MIN_TRADES_BASE = 252
# values-spec §6 :93 "S = mean(d) / sd(d) × √252, sd with n − 1, risk-free rate 0".
ANNUALISATION = 252
# values-spec §5 :85 "252 / 63 / 63 sessions".
IS_LEN, OOS_LEN, STEP = 252, 63, 63
# values-spec §7 :104 "S = 16 blocks"; :103 rows = the windows' span trimmed by its
# oldest sessions to a multiple of S.
CSCV_S = 16
# values-spec §7 :112 "A run that returns exactly 5,000 trades — SETTLED: treated as
# truncated"; the bridge list is "capped at 5000" (§7 :111).
TRADE_CAP = 5000


class InputError(Exception):
    """Bad or inconsistent input: the CLI exits 2."""


class NotSettledBySpec(Exception):
    """The spec leaves a maths choice open; the CLI exits 3 (contract rule)."""

    def __init__(self, what):
        super().__init__("NotSettledBySpec: " + what)


def load_module_by_path(name, path):
    """Import a file under a unique module name (see IMPORT HAZARD above)."""
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# --------------------------------------------------------------------------
# Grid and naming (contract "Column naming"; values-spec §3)
# --------------------------------------------------------------------------
def column_name(params):
    """`L{Lookback}_k{NoiseMult:.1f}_m{StopAtrMult:g}_{ExitPolicy}` (contract).

    INFERRED: identical to W2's tradelist.column_name (not imported, by brief);
    the cross-check is run_selection's requirement that every arm-b file's
    `column` equals column_name(its params)."""
    return "L{}_k{:.1f}_m{:g}_{}".format(params["Lookback"], params["NoiseMult"],
                                         params["StopAtrMult"], params["ExitPolicy"])


GRID = [{"Lookback": lb, "NoiseMult": k, "StopAtrMult": m, "ExitPolicy": p, "Contracts": 1}
        for lb in LOOKBACKS for k in NOISE_MULTS for m in STOP_MULTS for p in POLICIES]
GRID_COLUMNS = [column_name(p) for p in GRID]
assert len(GRID) == 81 and len(set(GRID_COLUMNS)) == 81  # §3 :60 "3 × 3 × 3 × 3 = 81"


def _grid_index(value, axis, label):
    for i, v in enumerate(axis):
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value == v:
            return i
    raise InputError("%s=%r is not on the values-spec §3 grid %r" % (label, value, axis))


def anchor_distance(params):
    """values-spec §6 :97: "the configuration nearest the anchor, as the sum of
    grid-step distances on lookback (anchor 14) and k (anchor 1.0), plus
    exit-policy distance 0 for BandOrVWAP, else 1. The stop axis adds 0 to the
    distance, because it has no paper anchor (§1)."""
    d_lb = abs(_grid_index(params["Lookback"], LOOKBACKS, "Lookback")
               - LOOKBACKS.index(ANCHOR_LOOKBACK))
    d_k = abs(_grid_index(params["NoiseMult"], NOISE_MULTS, "NoiseMult")
              - NOISE_MULTS.index(ANCHOR_K))
    _grid_index(params["StopAtrMult"], STOP_MULTS, "StopAtrMult")  # validated; adds 0
    if params["ExitPolicy"] not in POLICIES:
        raise InputError("ExitPolicy=%r is not on the values-spec §3 grid" % (params["ExitPolicy"],))
    d_p = 0 if params["ExitPolicy"] == ANCHOR_POLICY else 1
    return d_lb + d_k + d_p


def tie_key(params):
    """Sort key: anchor distance, then §6 :97 lexicographic ascending
    Lookback, k, m, policy (BandOrVWAP, OppBand, Flat1559)."""
    return (anchor_distance(params), params["Lookback"], params["NoiseMult"],
            params["StopAtrMult"], POLICIES.index(params["ExitPolicy"]))


# --------------------------------------------------------------------------
# Statistic (values-spec §6 :92-93)
# --------------------------------------------------------------------------
def to_scaled_ints(values):
    """Exact integer images of finite floats under one common power-of-two scale.

    Every finite float is p/q with q a power of two, so X_i = x_i * max(q) is an
    exact integer. Sums of X and X^2 are then exact (Python ints), which makes
    the block-combined fast path in pbo.py bit-identical to a direct pass."""
    ratios = []
    for v in values:
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise InputError("daily value %r is not a finite number" % (v,))
        ratios.append(float(v).as_integer_ratio())
    den = max((q for _, q in ratios), default=1)
    return [p * (den // q) for p, q in ratios]


def sharpe_from_sums(t, q2, n):
    """Sharpe from exact integer sums t = sum X, q2 = sum X^2 over n sessions.

    mean = t/n; var(n-1) = (n*q2 - t^2) / (n(n-1)); so
    S = mean/sd*sqrt(252) = sign(t) * sqrt(252 (n-1) t^2 / (n D)), D = n*q2 - t^2.
    D == 0 exactly iff every value is equal, i.e. iff sd == 0 (values-spec §6 :95
    "a configuration whose daily P&L has zero standard deviation is ineligible").
    The int/int true division is correctly rounded by CPython, so the float
    result depends only on the exact rational value (scale-invariant)."""
    if n < 2:
        return None
    d = n * q2 - t * t
    if d == 0:
        return None
    if d < 0:  # impossible by Cauchy-Schwarz; guard against misuse
        raise AssertionError("negative variance numerator")
    r = (t * t * ANNUALISATION * (n - 1)) / (n * d)
    return math.copysign(math.sqrt(r), t)


def sharpe(daily):
    """values-spec §6 :93: "S = mean(d) / sd(d) × √252, sd with n − 1,
    risk-free rate 0", over ALL sessions of the set, zero days included
    (§6 :93 "d_i = sum of the net P&L ... of trades exited in session i, 0 if none").
    Returns None if n < 2 or sd == 0 (§6 :95 "ineligible")."""
    x = to_scaled_ints(list(daily))
    return sharpe_from_sums(sum(x), sum(v * v for v in x), len(x))


def eligible(s, trades, n_sessions):
    """values-spec §6 :94 "100 trades per 252-session in-sample window ... A
    configuration below 100 is ineligible"; §7 :105 "minimum trades pro rata,
    100 × sessions / 252"; §6 :95 zero sd -> ineligible (s is None).
    Exact integer comparison: trades * 252 >= 100 * n_sessions."""
    if s is None:
        return False
    return trades * MIN_TRADES_BASE >= MIN_TRADES * n_sessions


def choose(items):
    """items: [(column, S, tie_key)] already ELIGIBLE. Returns (pick, tied).

    values-spec §6 :97: "equal S to 1e-9 → the configuration nearest the anchor
    ... Then lexicographic, ascending". §6 :98: "net profit is not the objective
    and is not a tie-break" — net profit is never an argument here.
    §6 :96: no eligible configuration -> (None, [])."""
    if not items:
        return None, []
    best = max(s for _, s, _ in items)
    tied = [it for it in items if it[1] >= best - TIE_TOL]
    win = min(tied, key=lambda it: it[2])
    return win[0], [c for c, _, _ in tied]


def pick(candidates):
    """candidates: [{"column","params","sharpe","trades","n_sessions"}].
    Returns the picked column or None (values-spec §6 :92-98)."""
    return select_one(candidates)["pick"]


def select_one(candidates):
    items = [(c["column"], c["sharpe"], tie_key(c["params"])) for c in candidates
             if eligible(c["sharpe"], c["trades"], c["n_sessions"])]
    p, tied = choose(items)
    return {"pick": p, "tied": tied, "eligible": len(items)}


# --------------------------------------------------------------------------
# Input loading and validation (fail loudly, never guess)
# --------------------------------------------------------------------------
def _reject_constant(tok):
    raise InputError("non-finite JSON constant %s" % tok)


def load_json(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError as e:
        raise InputError("cannot read %s: %s" % (path, e))
    try:
        obj = json.loads(raw.decode("utf-8"), parse_constant=_reject_constant)
    except (ValueError, UnicodeDecodeError) as e:
        raise InputError("%s is not valid JSON: %s" % (path, e))
    return obj, hashlib.sha256(raw).hexdigest()


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def check_calendar(cal, path="<calendar>"):
    if not isinstance(cal, dict) or cal.get("schema") != SCHEMA_CAL:
        raise InputError("%s: schema is not %s" % (path, SCHEMA_CAL))
    n = cal.get("N")
    sessions = cal.get("sessions")
    if not _is_int(n) or not isinstance(sessions, list) or len(sessions) != n:
        raise InputError("%s: N must equal len(sessions)" % path)
    for i, s in enumerate(sessions, 1):
        if not isinstance(s, dict) or s.get("n") != i:
            raise InputError("%s: sessions must be numbered 1..N in order (at %d)" % (path, i))
    rule = cal.get("rule", {})
    if (rule.get("IS"), rule.get("OOS"), rule.get("STEP")) != (IS_LEN, OOS_LEN, STEP):
        raise InputError("%s: rule IS/OOS/STEP must be 252/63/63 (values-spec §5 :85)" % path)
    wins = cal.get("windows")
    if not isinstance(wins, list) or not wins or cal.get("K") != len(wins):
        raise InputError("%s: K must equal len(windows) > 0" % path)
    # values-spec §5 :84 "Full windows K = floor((N − 252) / 63) ... Sessions after
    # s(252 + 63K) are dropped"; §7 :103-104 CSCV rows. Recomputed from N; any
    # disagreement is refused (a short K would silently drop windows).
    if n < IS_LEN + OOS_LEN:
        raise InputError("%s: N=%d gives no full window (values-spec §5 :84)" % (path, n))
    k_want = (n - IS_LEN) // OOS_LEN
    last = IS_LEN + OOS_LEN * k_want
    block = last // CSCV_S
    want = {"K": k_want, "oos_sessions": OOS_LEN * k_want,
            "dropped": [last + 1, n] if last < n else None,
            "cscv_rows": [last - CSCV_S * block + 1, last], "cscv_S": CSCV_S, "cscv_block": block}
    for key, v in want.items():
        got = cal.get(key)
        if key not in cal or isinstance(got, bool) or got != v:
            raise InputError("%s: %s=%r but N=%d implies %s=%r (values-spec §5 :84, §7 :103-104)"
                             % (path, key, cal.get(key), n, key, v))
    # values-spec §5 :87 "Window k: in-sample s(63(k−1)+1) … s(63(k−1)+252);
    # out-of-sample the next 63."
    for k, w in enumerate(wins, 1):
        a = STEP * (k - 1) + 1
        want_is, want_oos = [a, a + IS_LEN - 1], [a + IS_LEN, a + IS_LEN + OOS_LEN - 1]
        if w.get("k") != k or list(w.get("is", [])) != want_is or list(w.get("oos", [])) != want_oos:
            raise InputError("%s: window %d is not IS %s / OOS %s (values-spec §5 :87)"
                             % (path, k, want_is, want_oos))
        if want_oos[1] > n:
            raise InputError("%s: window %d runs past N=%d" % (path, k, n))
    return cal


def load_calendar(path):
    cal, sha = load_json(path)
    check_calendar(cal, path)
    return cal, sha


def check_daily(d, n_cal, path="<daily>"):
    if not isinstance(d, dict) or d.get("schema") != SCHEMA_DAILY:
        raise InputError("%s: schema is not %s" % (path, SCHEMA_DAILY))
    for key in ("column", "params", "pnl_basis_in", "truncated", "n_trades", "N",
                "daily_net", "daily_trades", "trades"):
        if key not in d:
            raise InputError("%s: missing key %r" % (path, key))
    # values-spec §7 :112 "A run that returns exactly 5,000 trades — SETTLED:
    # treated as truncated, and rerun or split by date." Refuse it here.
    if d["truncated"] is not False:
        raise InputError("%s: truncated=%r — values-spec §7 :112: a truncated run is "
                         "rerun or split by date before use; refusing it" % (path, d["truncated"]))
    if not isinstance(d["trades"], list):
        raise InputError("%s: trades must be a list" % path)
    if not _is_int(d["n_trades"]):
        raise InputError("%s: n_trades=%r is not an int" % (path, d["n_trades"]))
    if TRADE_CAP in (d["n_trades"], len(d["trades"])):
        raise InputError("%s: exactly %d trades (n_trades=%r, len(trades)=%d) but truncated=false — "
                         "values-spec §7 :112: exactly 5,000 trades is treated as truncated; a "
                         "truncated run is rerun or split by date before use; refusing it"
                         % (path, TRADE_CAP, d["n_trades"], len(d["trades"])))
    if d["n_trades"] != len(d["trades"]):
        raise InputError("%s: n_trades=%r != len(trades)=%d; refusing it"
                         % (path, d["n_trades"], len(d["trades"])))
    if d["N"] != n_cal:
        raise InputError("%s: N=%r does not match calendar N=%d" % (path, d["N"], n_cal))
    net, tr = d["daily_net"], d["daily_trades"]
    if not isinstance(net, list) or len(net) != n_cal:
        raise InputError("%s: daily_net must have N=%d entries" % (path, n_cal))
    if not isinstance(tr, list) or len(tr) != n_cal or not all(_is_int(t) and t >= 0 for t in tr):
        raise InputError("%s: daily_trades must be N=%d non-negative ints" % (path, n_cal))
    if sum(tr) != d["n_trades"]:
        raise InputError("%s: n_trades=%r != sum(daily_trades)=%d; refusing it"
                         % (path, d["n_trades"], sum(tr)))
    to_scaled_ints(net)  # finiteness check
    # Consistency: trade list vs daily arrays (contract Interface 2 definitions).
    trades = d["trades"]
    if not isinstance(trades, list):
        raise InputError("%s: trades must be a list" % path)
    per_n = Counter()
    per_net = {}
    for t in trades:
        s = t.get("session") if isinstance(t, dict) else None
        if not _is_int(s) or not 1 <= s <= n_cal:
            raise InputError("%s: trade with session %r outside 1..%d" % (path, s, n_cal))
        per_n[s] += 1
        per_net.setdefault(s, []).append(t.get("net_pnl"))
    for i in range(1, n_cal + 1):
        if per_n.get(i, 0) != tr[i - 1]:
            raise InputError("%s: session %d has %d trades in the list but daily_trades=%d"
                             % (path, i, per_n.get(i, 0), tr[i - 1]))
        if i in per_net:
            vals = per_net[i]
            to_scaled_ints(vals)
            if abs(math.fsum(vals) - net[i - 1]) > 1e-6:
                raise InputError("%s: session %d net_pnl sum %r != daily_net %r"
                                 % (path, i, math.fsum(vals), net[i - 1]))
        elif net[i - 1] != 0:
            raise InputError("%s: session %d has no trade but daily_net=%r" % (path, i, net[i - 1]))
    return d


def expand_daily_paths(items):
    """Files are taken as given; a directory contributes its *.json, sorted."""
    paths = []
    for it in items:
        if os.path.isdir(it):
            found = sorted(glob.glob(os.path.join(it, "*.json")))
            if not found:
                raise InputError("directory %s holds no *.json" % it)
            paths.extend(found)
        elif os.path.isfile(it):
            paths.append(it)
        else:
            raise InputError("no such file or directory: %s" % it)
    real = [os.path.realpath(p) for p in paths]
    if len(set(real)) != len(real):
        raise InputError("the same daily file was given twice")
    return paths


def load_dailies(items, arm, n_cal):
    """Returns (ordered list of daily dicts, {column: sha256})."""
    loaded = []
    for p in expand_daily_paths(items):
        d, sha = load_json(p)
        check_daily(d, n_cal, p)
        loaded.append((p, d, sha))
    cols = [d["column"] for _, d, _ in loaded]
    dup = sorted(c for c, k in Counter(cols).items() if k > 1)
    if dup:
        raise InputError("duplicate column(s): %s" % ", ".join(dup))
    if arm == "a":
        if cols != [ARM_A_COLUMN]:
            raise InputError("arm a needs exactly one daily file with column %r; got %r"
                             % (ARM_A_COLUMN, cols))
    else:
        missing = [c for c in GRID_COLUMNS if c not in cols]
        extra = sorted(c for c in cols if c not in GRID_COLUMNS)
        if missing or extra:
            raise InputError("arm b needs exactly the 81 values-spec §3 grid columns; "
                             "missing %d %s; extra %d %s" % (len(missing), missing[:5], len(extra), extra[:5]))
        for p, d, _ in loaded:
            prm = d["params"]
            if not isinstance(prm, dict) or any(k not in prm for k in PARAM_KEYS):
                raise InputError("%s: params must carry %s" % (p, PARAM_KEYS))
            if column_name(prm) != d["column"] or prm["Contracts"] != 1:
                raise InputError("%s: params %r do not name column %r (Contracts 1)"
                                 % (p, prm, d["column"]))
        order = {c: i for i, c in enumerate(GRID_COLUMNS)}
        loaded.sort(key=lambda x: order[x[1]["column"]])
    return [d for _, d, _ in loaded], {d["column"]: sha for _, d, sha in loaded}


# --------------------------------------------------------------------------
# Per-window selection
# --------------------------------------------------------------------------
def run_selection(cal, dailies, arm):
    out_windows = []
    for w in cal["windows"]:
        a, b = w["is"]
        c, e = w["oos"]
        n_is = b - a + 1
        cands = []
        for d in dailies:
            cands.append({"column": d["column"], "params": d["params"],
                          "sharpe": sharpe(d["daily_net"][a - 1:b]),
                          "trades": sum(d["daily_trades"][a - 1:b]), "n_sessions": n_is})
        if arm == "a":
            # values-spec §2 :43: arm (a) "reported on the same 17 out-of-sample
            # windows as arm (b)". No selection: eligibility is not applied.
            # INFERRED shape: eligible null, tied [], no_eligible false.
            res = {"pick": ARM_A_COLUMN, "tied": [], "eligible": None}
        else:
            res = select_one(cands)
        by_col = {x["column"]: x for x in cands}
        pk = res["pick"]
        if pk is None:
            # values-spec §6 :96 "arm (b) trades nothing in that out-of-sample
            # window, and the window counts as not profitable."
            oos_daily, oos_trades, oos_list = [0.0] * (e - c + 1), 0, []
        else:
            d = next(x for x in dailies if x["column"] == pk)
            oos_daily = [float(v) for v in d["daily_net"][c - 1:e]]
            oos_trades = sum(d["daily_trades"][c - 1:e])
            oos_list = [t for t in d["trades"] if c <= t["session"] <= e]
        out_windows.append({
            "k": w["k"], "is": [a, b], "oos": [c, e],
            "eligible": res["eligible"], "pick": pk,
            "pick_is_sharpe": by_col[pk]["sharpe"] if pk else None,
            "pick_is_trades": by_col[pk]["trades"] if pk else None,
            "tied": res["tied"], "no_eligible": pk is None,
            "oos_net": math.fsum(oos_daily), "oos_trades": oos_trades,
            "oos_daily": oos_daily, "oos_trade_list": oos_list})
    out = {"schema": SCHEMA_OUT, "arm": arm, "columns": [d["column"] for d in dailies],
           "windows": out_windows,
           "oos_total_net": math.fsum(v for w in out_windows for v in w["oos_daily"]),
           "oos_total_trades": sum(w["oos_trades"] for w in out_windows),
           # Passthrough only, no maths: each input series' pnl basis (contract
           # Interface 2 "pnl_basis_in"). UNVERIFIED whether NT8's `pnl` is gross
           # or net (values-spec §7); report.py prints this map.
           "pnl_basis_in": {d["column"]: d["pnl_basis_in"] for d in dailies}}
    if arm == "a":
        d = dailies[0]
        # values-spec §2 :43 "plus the full-span total": all N sessions.
        out["full_span"] = {"net": math.fsum(d["daily_net"]), "trades": sum(d["daily_trades"])}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="select.py",
        description="Walk-forward per-window selection (values-spec §5-§6). Arm a: one "
                    "fixed-rules column sliced on the calendar's windows plus the full-span "
                    "total. Arm b: pick per window among the 81 grid columns by in-sample "
                    "Sharpe with a minimum trade count and the §6 tie-break.")
    ap.add_argument("--arm", required=True, choices=["a", "b"])
    ap.add_argument("--calendar", required=True, help="calendar JSON (praxis-wf-calendar/1)")
    ap.add_argument("--daily", required=True, nargs="+",
                    help="daily-series JSON files and/or directories of them (praxis-wf-daily/1)")
    ap.add_argument("--out", required=True, help="output selection JSON (praxis-wf-selection/1)")
    args = ap.parse_args(argv)
    try:
        cal, cal_sha = load_calendar(args.calendar)
        dailies, shas = load_dailies(args.daily, args.arm, cal["N"])
        out = run_selection(cal, dailies, args.arm)
        out["inputs"] = {"calendar_sha256": cal_sha, "daily_sha256": shas}
    except NotSettledBySpec as e:
        print(str(e), file=sys.stderr)
        return 3
    except InputError as e:
        print("select.py: error: %s" % e, file=sys.stderr)
        return 2
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, sort_keys=True, indent=1, allow_nan=False)
        fh.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
