#!/usr/bin/env python3
"""Probability of backtest overfitting by CSCV (values-spec §7 :102-108).

CSCV = combinatorially symmetric cross-validation (Bailey, Borwein, López de
Prado, Zhu, 2017) — values-spec §7 :102. Standard library only.

Reads the calendar JSON (Interface 1) and the 81 arm-b daily-series JSONs
(Interface 2); writes the PBO JSON (Interface 4). Elapsed time goes to stderr
only, so the output is deterministic.
"""
import argparse
import itertools
import json
import math
import os
import statistics
import sys
import time
from operator import itemgetter

_HERE = os.path.dirname(os.path.abspath(__file__))
# select.py shadows the stdlib `select`; load it by path (see select.py docstring).
import importlib.util as _ilu  # noqa: E402

if "praxis_wf_select" in sys.modules:
    sel = sys.modules["praxis_wf_select"]
else:
    _spec = _ilu.spec_from_file_location("praxis_wf_select", os.path.join(_HERE, "select.py"))
    sel = _ilu.module_from_spec(_spec)
    sys.modules["praxis_wf_select"] = sel
    _spec.loader.exec_module(sel)

NotSettledBySpec = sel.NotSettledBySpec
InputError = sel.InputError

SCHEMA_OUT = "praxis-wf-pbo/1"
# values-spec §7 :103 rows s12 … s1323, "1,312 = 16 × 82"; §7 :104 "S = 16 blocks of 82".
SPEC_ROWS = (12, 1323)
SPEC_S = 16
SPEC_BLOCK = 82
assert SPEC_ROWS[1] - SPEC_ROWS[0] + 1 == SPEC_S * SPEC_BLOCK == 1312
# values-spec §7 :108 "arm (b) counts only if **PBO < 0.05**".
THRESHOLD = 0.05


def _undefined_test_sharpe(column, split_no, train):
    return NotSettledBySpec(
        "values-spec §7 :106 ranks the 81 'by test Sharpe' but does not say how to rank a "
        "configuration whose TEST-set Sharpe is undefined (sd = 0 on the test set); "
        "§6 :95 makes such a configuration ineligible for SELECTION only and says 'the "
        "ranking in §7 uses all 81'. Hit at column %s, split #%d (train blocks %s). "
        "Alternatives for the master: (i) score it S = 0 and rank it; (ii) rank it lowest; "
        "(iii) exclude the split from the count." % (column, split_no, list(train)))


def cscv(columns, keys, values, trades, S, block, collect=False):
    """CSCV core. columns[j] name; keys[j] = sel.tie_key(params_j);
    values[j] = S*block daily net P&L; trades[j] = S*block daily trade counts.

    Fast path: exact integer per-block sums (sum X, sum X^2, trades) combined per
    split; test sums = column totals - train sums (exact, ints)."""
    m = len(columns)
    if S < 4 or S % 2:
        raise InputError("S must be even and >= 4")
    rows = S * block
    if not (len(keys) == len(values) == len(trades) == m) or m < 2:
        raise InputError("columns/keys/values/trades length mismatch")
    for j in range(m):
        if len(values[j]) != rows or len(trades[j]) != rows:
            raise InputError("column %s does not have S*block=%d rows" % (columns[j], rows))
    flat = sel.to_scaled_ints([v for col in values for v in col])  # one exact scale
    bt, bq, bc = [], [], []
    for j in range(m):
        x = flat[j * rows:(j + 1) * rows]
        bt.append([sum(x[b * block:(b + 1) * block]) for b in range(S)])
        bq.append([sum(v * v for v in x[b * block:(b + 1) * block]) for b in range(S)])
        bc.append([sum(trades[j][b * block:(b + 1) * block]) for b in range(S)])
    tot_t = [sum(r) for r in bt]
    tot_q = [sum(r) for r in bq]
    half = S // 2
    n_train = half * block
    n_test = (S - half) * block
    splits = le0 = no_elig = 0
    logits = []
    detail = []
    sfs = sel.sharpe_from_sums
    elig = sel.eligible
    for combo in itertools.combinations(range(S), half):  # deterministic order
        splits += 1
        g = itemgetter(*combo)
        tt = [sum(g(r)) for r in bt]
        tq = [sum(g(r)) for r in bq]
        tc = [sum(g(r)) for r in bc]
        # values-spec §7 :105 "Pick on training — SETTLED: n* by §6's rule (Sharpe;
        # minimum trades pro rata, 100 × sessions / 252; tie-break)."
        items = []
        for j in range(m):
            s = sfs(tt[j], tq[j], n_train)
            if elig(s, tc[j], n_train):
                items.append((j, s, keys[j]))
        nstar, _ = sel.choose(items)
        if nstar is None:
            # values-spec §7 :107 "No eligible configuration on a training set —
            # SETTLED: that split counts as λ ≤ 0 (the strict side)."
            no_elig += 1
            le0 += 1
            if collect:
                detail.append((combo, None, None, None))
            continue
        # values-spec §7 :106 "rank the 81 by test Sharpe in ascending order (rank 1 =
        # worst, 81 = best; tied values share their average rank)". All m are ranked
        # (§6 :95 "the ranking in §7 uses all 81"). Tied = exactly equal floats
        # (manager's brief; the spec states no tolerance for rank ties).
        test = []
        for j in range(m):
            s = sfs(tot_t[j] - tt[j], tot_q[j] - tq[j], n_test)
            if s is None:
                raise _undefined_test_sharpe(columns[j], splits, combo)
            test.append(s)
        sn = test[nstar]
        less = sum(1 for s in test if s < sn)
        eq = sum(1 for s in test if s == sn)
        rank = less + (eq + 1) / 2.0  # average of positions less+1 .. less+eq
        # "ω = rank of n* / (81 + 1); λ = ln(ω / (1 − ω))."
        omega = rank / (m + 1)
        lam = math.log(omega / (1.0 - omega))
        logits.append(lam)
        # "**PBO = share of splits with λ ≤ 0.**"
        if lam <= 0:
            le0 += 1
        if collect:
            detail.append((combo, columns[nstar], rank, lam))
    res = {"splits": splits, "le0": le0, "no_eligible_splits": no_elig,
           "pbo": le0 / splits, "logits": logits}
    if collect:
        res["detail"] = detail
    return res


def logit_summary(logits):
    if not logits:
        return {"min": None, "median": None, "max": None, "n": 0}
    return {"min": min(logits), "median": statistics.median(logits),
            "max": max(logits), "n": len(logits)}


def run_pbo(cal, dailies):
    rows = list(cal.get("cscv_rows", []))
    if rows != list(SPEC_ROWS) or cal.get("cscv_S") != SPEC_S or cal.get("cscv_block") != SPEC_BLOCK:
        raise InputError("calendar cscv_rows/cscv_S/cscv_block = %r/%r/%r, values-spec §7 "
                         ":103-104 wants [12, 1323]/16/82"
                         % (cal.get("cscv_rows"), cal.get("cscv_S"), cal.get("cscv_block")))
    if rows[1] > cal["N"]:
        raise InputError("cscv rows run past N")
    a, b = rows
    columns = [d["column"] for d in dailies]
    keys = [sel.tie_key(d["params"]) for d in dailies]
    values = [d["daily_net"][a - 1:b] for d in dailies]
    trades = [d["daily_trades"][a - 1:b] for d in dailies]
    res = cscv(columns, keys, values, trades, SPEC_S, SPEC_BLOCK)
    return {"schema": SCHEMA_OUT, "S": SPEC_S, "block": SPEC_BLOCK, "rows": rows,
            "splits": res["splits"], "le0": res["le0"],
            "no_eligible_splits": res["no_eligible_splits"], "pbo": res["pbo"],
            "threshold": THRESHOLD, "passes": res["pbo"] < THRESHOLD,
            "logit_summary": logit_summary(res["logits"])}


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="pbo.py",
        description="CSCV probability of backtest overfitting over the 81 arm-b columns "
                    "(values-spec §7): rows s12..s1323, S=16 blocks of 82, all C(16,8)=12,870 "
                    "splits, n* by the §6 rule on training, PBO = share of splits with "
                    "lambda <= 0; passes iff PBO < 0.05.")
    ap.add_argument("--calendar", required=True, help="calendar JSON (praxis-wf-calendar/1)")
    ap.add_argument("--daily", required=True, nargs="+",
                    help="the 81 daily-series JSON files and/or directories of them")
    ap.add_argument("--out", required=True, help="output PBO JSON (praxis-wf-pbo/1)")
    args = ap.parse_args(argv)
    t0 = time.monotonic()
    try:
        cal, cal_sha = sel.load_calendar(args.calendar)
        dailies, shas = sel.load_dailies(args.daily, "b", cal["N"])
        out = run_pbo(cal, dailies)
        out["inputs"] = {"calendar_sha256": cal_sha, "daily_sha256": shas}
    except NotSettledBySpec as e:
        print(str(e), file=sys.stderr)
        return 3
    except InputError as e:
        print("pbo.py: error: %s" % e, file=sys.stderr)
        return 2
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, sort_keys=True, indent=1, allow_nan=False)
        fh.write("\n")
    print("pbo.py: elapsed %.2f s (splits=%d)" % (time.monotonic() - t0, out["splits"]),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
