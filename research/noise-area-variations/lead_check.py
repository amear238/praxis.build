#!/usr/bin/env python3
"""lead_check.py -- the lead's own recomputation of the five bars from the raw result files.

Reads only out/variations/<name>/{harsh-stops,kind}-{50000,10000}.json and compares what it computes with
out/variations/<name>/judge.json. It does not import gates.py, engine.py or run_all.py. It uses globex and
bands only to build the trading-day calendar (from the first day the variation's band exists), and
`trailing` and `shuffled` from research/intraday-momentum-long/run.py, unchanged.

Recomputed per variation, on the harsh-stops 50,000 result and again on the kind 50,000 result:
  average winner in risks (all years, and 2024-01-01 on), net from 2024 on, the longest stretch of trading
  days with no entry, net profit, the first real crossing of the trailing 2,000 limit, and the share of
  10,000 shuffled orders (seed 20261115) that cross it.
Plain checks on every trade of all four files: the money chain (start + nets = balance), r = net / planned
cost, the stop exactly `dist` from the entry, dist >= 10 points, no exit stamped after 16:00, and on kind
fills no loss above the planned cost by more than a cent unless `gap` is set.

Prints one line per figure and a final count of differences. Exit code 0 when there are none, 1 otherwise.
Standard library only. Run with `python3 -I -B research/noise-area-variations/lead_check.py`.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "research", "intraday-momentum-long"))
import bands    # noqa: E402
import globex   # noqa: E402
from run import shuffled, trailing   # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
OUT = os.path.join(HERE, "out", "variations")
LIMIT = 2000.0
LATER = "2024-01-01"
RUNS, SEED = 10000, 20261115
TOL = 1e-6


def load(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def calendar(days, s):
    for k in range(len(days)):
        if bands.day_bands(days, k, s["anchor"], s["lookback"], s["band_mult"]):
            return [d.date for d in days[k:]]
    return [d.date for d in days]


def longest_gap(dates, traded):
    best = cur = 0
    for d in dates:
        cur = 0 if d in traded else cur + 1
        best = max(best, cur)
    return best


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def bars(res, dates):
    tr = res["trades"]
    win = [t["r"] for t in tr if t["net"] > 0]
    late = [t for t in tr if t["date"] >= LATER]
    late_win = [t["r"] for t in late if t["net"] > 0]
    net = sum(t["net"] for t in tr)
    late_net = sum(t["net"] for t in late)
    gap = longest_gap(dates, set(t["date"] for t in tr))
    first = trailing(res["days"], start=res["start"], limit=LIMIT)["first_cross"]
    sh = shuffled(res["days"], runs=RUNS, seed=SEED, start=res["start"], limit=LIMIT)
    pct = 100.0 * sh["crossed"] / sh["runs"]
    out = {
        "two_to_one": {"avg_winner_r": mean(win), "later_avg_winner_r": mean(late_win), "later_net": late_net,
                       "pass": bool(win) and bool(late_win) and mean(win) >= 2.0 and mean(late_win) >= 2.0
                       and late_net > 0},
        "frequency": {"max_gap_trading_days": gap, "pass": gap <= 7},
        "profit": {"net": net, "pass": net >= 2 * LIMIT},
        "survival": {"first_cross": first, "shuffle_pct": pct,
                     "pass": first is None and sh["crossed"] * 100 <= 5 * sh["runs"]},
    }
    return out


def plain_checks(label, res):
    """-> list of problems found in the raw trades of one result file."""
    bad = []
    bal = res["start"]
    for i, t in enumerate(res["trades"]):
        tag = "%s trade %d (%s)" % (label, i, t["entry_dt"])
        bal = round(bal + t["net"], 2)
        if abs(bal - t["balance"]) > 0.005:
            bad.append("%s: balance %.2f, money chain gives %.2f" % (tag, t["balance"], bal))
            bal = t["balance"]
        if t["stop_initial"] is None or t["dist"] is None or not t["planned_cost"]:
            bad.append("%s: no stop or no planned cost" % tag)
            continue
        sign = 1 if t["side"] == "long" else -1
        if abs((t["entry"] - sign * t["dist"]) - t["stop_initial"]) > 1e-9:
            bad.append("%s: stop %.2f is not %.2f from entry %.2f" % (tag, t["stop_initial"], t["dist"], t["entry"]))
        if t["dist"] < 10.0:
            bad.append("%s: stop distance %.2f under 10 points" % (tag, t["dist"]))
        if abs(t["r"] - t["net"] / t["planned_cost"]) > 1e-9:
            bad.append("%s: r %.6f is not net / planned cost" % (tag, t["r"]))
        want = round((t["exit"] - t["entry"]) * sign * 2.0 * t["qty"] - 1.90 * t["qty"], 2)
        if abs(want - t["net"]) > 0.005:
            bad.append("%s: net %.2f, prices and size give %.2f" % (tag, t["net"], want))
        loss_pc = (t["dist"] + 0.5) * 2.0 + 1.90
        if abs(round(t["qty"] * loss_pc, 2) - t["planned_cost"]) > 0.005 or t["qty"] < 1:
            bad.append("%s: planned cost %.2f is not qty x loss per contract" % (tag, t["planned_cost"]))
        if t["exit_dt"][11:16] > "16:00" and t["exit_dt"][11:16] < "18:01":
            bad.append("%s: exit stamped %s, after 16:00" % (tag, t["exit_dt"]))
        if res["fill"] == "kind" and not t["gap"] and -t["net"] > t["planned_cost"] + 0.01:
            bad.append("%s: kind-fill loss %.2f above planned cost %.2f with no gap" % (tag, -t["net"], t["planned_cost"]))
    return bad


def compare(name, which, mine, theirs, lines):
    diffs = 0
    for bar in ("two_to_one", "frequency", "profit", "survival"):
        for key, val in sorted(mine[bar].items()):
            got = theirs[bar].get(key)
            if isinstance(val, float) and isinstance(got, (int, float)) and not isinstance(got, bool):
                same = abs(val - got) <= TOL
            else:
                same = val == got
            lines.append("%s %-11s %-10s %-22s lead %-22r judge %-22r %s"
                         % (name, which, bar, key, val, got, "same" if same else "DIFFERENT"))
            diffs += 0 if same else 1
    return diffs


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out = argv[0] if argv else OUT
    days = globex.load_days(DATA)
    lines, diffs = [], 0
    names = sorted(n for n in os.listdir(out) if os.path.isdir(os.path.join(out, n)))
    for name in names:
        vdir = os.path.join(out, name)
        judge = load(os.path.join(vdir, "judge.json"))
        res = {}
        for fill in ("harsh-stops", "kind"):
            for start in (50000, 10000):
                r = load(os.path.join(vdir, "%s-%d.json" % (fill, start)))
                if r["fill"] != fill or r["start"] != float(start):
                    lines.append("%s %s-%d: file holds fill %r start %r DIFFERENT" % (name, fill, start, r["fill"], r["start"]))
                    diffs += 1
                res[fill, start] = r
                bad = plain_checks("%s %s-%d" % (name, fill, start), r)
                lines.extend(b + " DIFFERENT" for b in bad)
                diffs += len(bad)
        settings = res["harsh-stops", 50000]["settings"]
        for key, r in res.items():
            if r["settings"] != settings:
                lines.append("%s %s-%d: settings differ between result files DIFFERENT" % (name, key[0], key[1]))
                diffs += 1
        dates = calendar(days, settings)
        diffs += compare(name, "harsh-stops", bars(res["harsh-stops", 50000], dates), judge, lines)
        diffs += compare(name, "kind", bars(res["kind", 50000], dates), judge["kind_50000"], lines)
        mine_overall = all(bars(res["harsh-stops", 50000], dates)[b]["pass"]
                           for b in ("two_to_one", "frequency", "profit", "survival")) and judge["rule_check"]["pass"]
        same = mine_overall == judge["overall"]
        lines.append("%s overall: lead %r judge %r %s" % (name, mine_overall, judge["overall"], "same" if same else "DIFFERENT"))
        diffs += 0 if same else 1
        for fill in ("harsh-stops", "kind"):
            net = round(sum(t["net"] for t in res[fill, 10000]["trades"]), 2)
            got = judge["info_10000"][fill]["net"]
            same = abs(net - got) <= 0.005
            lines.append("%s 10000 %s net: lead %.2f judge %.2f %s" % (name, fill, net, got, "same" if same else "DIFFERENT"))
            diffs += 0 if same else 1
    for ln in lines:
        print(ln)
    print("variations checked: %d. differences: %d" % (len(names), diffs))
    return 0 if diffs == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
