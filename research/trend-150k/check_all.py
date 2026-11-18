#!/usr/bin/env python3
"""check_all.py -- the independent rule check (rule_check.py) over every setting of the measuring pass.

Each of the 108 settings (measure.grid_a, measure.grid_b) is run on the measuring window, midpoint fills, at the
measuring pass's own sizing (A: sameday.account at start 1e12, risk 1e-4 %, cap lifted, so every trade is
sized; B: weekly.run on all eleven markets at once, the same start, risk and cap), and handed to rule_check.
Prints one line per setting and writes out/check_all.json ({name: [first 20 breaks]}, with a break count).
Exit 0 only when every setting has no break.

Run: python3 -I -B research/trend-150k/check_all.py
Standard library only.
"""
import json
import multiprocessing
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import measure  # noqa: E402
import rule_check  # noqa: E402
import sameday  # noqa: E402
import specs as specs_mod  # noqa: E402
import weekly  # noqa: E402

START, RISK = 1e12, 1e-4
_D = None
_SPECS = {m: dict(s, max_qty=10 ** 12) for m, s in specs_mod.SPECS.items()}


def _load():
    lo, hi = measure._day(measure.FIRST), measure._day(measure.END) + 1
    out = {}
    for m in specs_mod.MARKETS:
        d = specs_mod.load(m)
        days = {k: v for k, v in sameday.et_days(d["minutes"], 9 * 60 + 35, 16 * 60).items()
                if measure.FIRST <= k <= measure.END}
        # New York midnight is 05:00 UTC on both ends of the window (January and December are winter time)
        five = 5 * 3600 * 10 ** 9
        mins = [b for b in d["minutes"] if lo * measure.DAY_NS + five <= b.ts < hi * measure.DAY_NS + five]
        out[m] = dict(d, et_days=days, minutes=mins)
    return out


def _one(item):
    kind, s = item
    M = specs_mod.MARKETS
    if kind == "A":
        by = {m: sameday.per_contract(_D[m]["minutes"], _D[m]["daily"], _SPECS[m], s, "midpoint",
                                      days=_D[m]["et_days"]) for m in M}
        res = sameday.account(by, _SPECS, RISK, START)
        # the checker gets the raw minutes of the window and picks the trading minutes itself
        br = rule_check.check_sameday(res, {m: _D[m]["minutes"] for m in M}, {m: _D[m]["daily"] for m in M}, _SPECS, s, "midpoint")
    else:
        lo, hi = measure._day(measure.FIRST), measure._day(measure.END)
        ser = {m: measure.slice_b(_D[m]["daily"], lo, hi, s["lookback"], s["atr_days"]) for m in M}
        rolls = {m: _D[m]["rolls"] for m in M}
        st = dict(s, risk_pct=RISK)
        res = weekly.run(ser, _SPECS, st, fill="midpoint", start=START, rolls=rolls)
        br = rule_check.check_weekly(res, ser, rolls, _SPECS)
    return s["name"], len(res["trades"]), br


def main():
    global _D
    _D = _load()
    items = [("A", s) for s in measure.grid_a()] + [("B", s) for s in measure.grid_b()]
    with multiprocessing.get_context("fork").Pool(6) as pool:
        got = pool.map(_one, items)
    bad = 0
    out = {}
    for name, n, br in got:
        print("%-22s %6d trades %6d breaks" % (name, n, len(br)))
        out[name] = {"trades": n, "breaks": len(br), "first": br[:20]}
        bad += bool(br)
    os.makedirs(measure.OUT, exist_ok=True)
    with open(os.path.join(measure.OUT, "check_all.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True)
    print("settings with a break: %d of %d" % (bad, len(got)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
