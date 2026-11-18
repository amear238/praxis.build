#!/usr/bin/env python3
"""full_run.py -- the full run of the trend plan's locked list on the $150,000 frame (PLAN.md, "How the search runs"
step 3). Judges with the same five bars and code as the Noise-Area $150,000 run.

Locked list: locked/A/<name>.json and locked/B/<name>.json, committed before this runs (refused otherwise).
A file holds the engine settings plus "name" (its stem) and "risk_pct" (of the realised balance, per trade).

Window: 2018-01-01 to the end of the data, all eleven markets at once, start 150,000, the specs of specs.py.
  A: sameday.per_contract per market on every New York date from 2018-01-01, then sameday.account.
  B: weekly.run on every market's daily series sliced by measure.slice_b (first decision the bar before
     2018-01-01's first bar). Also run from 2010 (the series' own start) for information, not judged.
Each version runs on three fills (midpoint judged; kind and harsh beside), each twice, the trade digests
compared. Every result goes through rule_check (the independent replay; absent, the rule bar fails).

Judged by noise-area-variations/gates.judge(limit=4,500) and run_150k.info, unchanged. For them each trade gets
"date" (A: its date; B: its entry's UTC date) and "r" = net / planned_cost. The frequency calendar: every date
from 2018-01-01 on which any market has a bar in the window (A: a minute 09:35-16:00 New York; B: a daily bar).
Extra information: the most contracts open at once (B), trades and net by market, B from 2010.

Writes out/full/<A|B>/<name>/judge.json (results kept out of git: out/full/.gitignore) and out/full/RESULTS.md.
Run: python3 -I -B research/trend-150k/full_run.py
Standard library only.
"""
import copy
import datetime as dt
import json
import multiprocessing
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_NAV = os.path.join(os.path.dirname(_HERE), "noise-area-variations")
for p in (_HERE, _NAV):
    if p not in sys.path:
        sys.path.append(p)
import measure  # noqa: E402
import sameday  # noqa: E402
import specs as specs_mod  # noqa: E402
import weekly  # noqa: E402
import gates  # noqa: E402  research/noise-area-variations/gates.py, unchanged
import run_150k  # noqa: E402  research/noise-area-variations/run_150k.py, unchanged
try:
    import rule_check  # noqa: E402
except ImportError:
    rule_check = None

FIRST = "2018-01-01"
START, LIMIT = 150000.0, 4500.0
FILLS = ("midpoint", "kind", "harsh-stops")
LOCKED = os.path.join(_HERE, "locked")
OUT = os.path.join(_HERE, "out", "full")
DAY_NS = 86400 * 1_000_000_000

_DATA = None


def _iso(day):
    return (dt.date(1970, 1, 1) + dt.timedelta(days=day)).isoformat()


def _uncommitted(paths):
    r = subprocess.run(["git", "status", "--porcelain", "--"] + paths, cwd=_HERE, capture_output=True, text=True)
    return r.stdout.strip()


def locked_list():
    out = []
    for kind in ("A", "B"):
        d = os.path.join(LOCKED, kind)
        for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if f.endswith(".json"):
                with open(os.path.join(d, f)) as fh:
                    s = json.load(fh)
                if s["name"] != f[:-5]:
                    raise ValueError("%s: name %r is not the file stem" % (f, s["name"]))
                out.append((kind, s))
    return out


def _for_judge(res, kind):
    trades = []
    for t in res["trades"]:
        t = dict(t)
        if kind == "B":
            t["date"] = _iso(t["entry_day"])
        t["r"] = t["net"] / t["planned_cost"]
        trades.append(t)
    days = [d for d in res["days"] if d["date"] >= FIRST] if kind == "B" else res["days"]
    return dict(res, trades=trades, days=days)


def _run_a(s, fill):
    by_m = {m: sameday.per_contract(_DATA[m]["minutes"], _DATA[m]["daily"], specs_mod.SPECS[m], s, fill,
                                    days=_DATA[m]["et_days"]) for m in specs_mod.MARKETS}
    return sameday.account(by_m, specs_mod.SPECS, s["risk_pct"], START), by_m


def _run_b(s, fill, first=FIRST):
    lo = (dt.date.fromisoformat(first) - dt.date(1970, 1, 1)).days
    ser = {m: (measure.slice_b(_DATA[m]["daily"], lo, 10 ** 9, s["lookback"], s["atr_days"]) if first
               else _DATA[m]["daily"]) for m in specs_mod.MARKETS}
    rolls = {m: _DATA[m]["rolls"] for m in specs_mod.MARKETS}
    return weekly.run(ser, specs_mod.SPECS, s, fill=fill, start=START, rolls=rolls), ser


def _max_open(trades):
    ev = []
    for t in trades:
        ev += [(t["entry_day"], 1, t["qty"]), (t["exit_day"], 0, -t["qty"])]
    cur = best = 0
    for _, _, q in sorted(ev):
        cur += q
        best = max(best, cur)
    return best


def _calendar(kind):
    if kind == "A":
        return sorted({d for m in specs_mod.MARKETS for d in _DATA[m]["et_days"]})
    return sorted({_iso(a.bar.ts // DAY_NS) for m in specs_mod.MARKETS for a in _DATA[m]["daily"]
                   if _iso(a.bar.ts // DAY_NS) >= FIRST})


def _one(item):
    kind, s = item
    res, breaks, inputs = {}, [], {}
    for fill in FILLS:
        a, inp = (_run_a if kind == "A" else _run_b)(copy.deepcopy(s), fill)
        b, _ = (_run_a if kind == "A" else _run_b)(copy.deepcopy(s), fill)
        if a["digest"] != b["digest"]:
            breaks.append("%s: second run gives different trades (%s, then %s)" % (fill, a["digest"], b["digest"]))
        res[fill], inputs[fill] = a, inp
    for fill in FILLS:
        if rule_check is None:
            breaks.append("rule_check.py missing")
            break
        if kind == "A":
            mins = {m: _DATA[m]["minutes"] for m in specs_mod.MARKETS}
            daily = {m: _DATA[m]["daily"] for m in specs_mod.MARKETS}
            got = rule_check.check_sameday(res[fill], mins, daily, specs_mod.SPECS, s, fill)
        else:
            rolls = {m: _DATA[m]["rolls"] for m in specs_mod.MARKETS}
            got = rule_check.check_weekly(res[fill], inputs[fill], rolls, specs_mod.SPECS)
        breaks.extend("%s: %s" % (fill, x) for x in got)
    cal = _calendar(kind)
    judged = gates.judge(dict(_for_judge(res["midpoint"], kind), rule_breaks=breaks), cal, limit=LIMIT)
    judged["kind"] = gates.judge(dict(_for_judge(res["kind"], kind), rule_breaks=breaks), cal, limit=LIMIT)
    judged["harsh_stops"] = gates.judge(dict(_for_judge(res["harsh-stops"], kind), rule_breaks=breaks), cal,
                                        limit=LIMIT)
    jr = _for_judge(res["midpoint"], kind)
    judged["info"] = run_150k.info(jr)
    judged["info"]["by_market"] = {m: {"trades": sum(1 for t in jr["trades"] if t["market"] == m),
                                       "net": round(sum(t["net"] for t in jr["trades"] if t["market"] == m), 2)}
                                   for m in specs_mod.MARKETS}
    judged["info"]["skipped"] = len(res["midpoint"]["skipped"])
    if kind == "B":
        judged["info"]["max_contracts_open"] = _max_open(res["midpoint"]["trades"])
        full, _ = _run_b(copy.deepcopy(s), "midpoint", first=None)
        f = _for_judge(dict(full, days=full["days"]), "A")
        judged["info"]["from_2010"] = {"trades": len(f["trades"]), "net": round(sum(t["net"] for t in f["trades"]), 2),
                                      "survival": gates._survival(f, limit=LIMIT)}
    judged["digests"] = {fill: res[fill]["digest"] for fill in FILLS}
    judged["rule_breaks"] = breaks[:200]
    judged["rule_break_count"] = len(breaks)
    judged["settings"] = s
    return kind, s["name"], judged


def _load_all():
    data = {}
    for m in specs_mod.MARKETS:
        d = specs_mod.load(m)
        d["et_days"] = {k: v for k, v in sameday.et_days(d["minutes"], 9 * 60 + 35, 16 * 60).items() if k >= FIRST}
        data[m] = d
    return data


def main():
    global _DATA
    items = locked_list()
    if not items:
        print("refused: no locked list")
        return 2
    dirty = _uncommitted([LOCKED])
    if dirty:
        print("refused: locked list not committed:\n" + dirty)
        return 2
    _DATA = _load_all()
    with multiprocessing.get_context("fork").Pool(min(len(items), os.cpu_count() or 4)) as pool:
        got = pool.map(_one, items)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, ".gitignore"), "w") as f:
        f.write("*/\n")
    for kind, name, j in got:
        d = os.path.join(OUT, kind, name)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "judge.json"), "w") as f:
            json.dump(j, f, indent=1, sort_keys=True)
    with open(os.path.join(OUT, "results.json"), "w") as f:
        json.dump([{"kind": k, "name": n, "judge": {x: j[x] for x in j if x != "rule_breaks"}} for k, n, j in got],
                  f, indent=1, sort_keys=True)
    for kind, name, j in got:
        print(kind, name, {b: j[b]["pass"] for b in ("rule_check", "two_to_one", "frequency", "profit", "survival")},
              "overall", j["overall"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
