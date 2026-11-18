#!/usr/bin/env python3
"""check_all.py -- the independent rule check (rule_check.py here, written from PLAN.md alone by a separate
agent) run against every trade of every measured setting of momentum into the close: 12 settings x 11 markets x
the three fills (midpoint, kind, harsh-stops), trading dates 2018-01-01 to 2023-12-31; then the account check
(this folder's rule_check.check_account, which runs the levels check_account on these trades, against
fade.account) on two risk sizes for every setting at midpoint fills. Writes out/check_all.json; exit 1 on any break.

Run: python3 -I -B research/close-momentum-150k/check_all.py   (one worker per market; run it alone)
Standard library only.
"""
import importlib.util
import json
import multiprocessing
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_RES = os.path.dirname(_HERE)
_LEV = os.path.join(_RES, "levels-150k")
for p in (_HERE, _LEV, os.path.join(_RES, "trend-150k")):
    if p not in sys.path:
        sys.path.append(p)
import closemom  # noqa: E402
import fade  # noqa: E402
import specs as specs_mod  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rc = _load("close_rule_check", os.path.join(_HERE, "rule_check.py"))
measure = _load("levels_measure", os.path.join(_LEV, "measure.py"))

FIRST, END = measure.FIRST, measure.END
FILLS = ("midpoint", "kind", "harsh-stops")


def _work(market):
    sp = specs_mod.SPECS[market]
    data = specs_mod.load(market)
    out, mids, n = {}, {}, 0
    for s in measure.grid("5"):
        for fill in FILLS:
            got = {"trades": [t for t in closemom.run(data["minutes"], data["daily"], sp, market, s, fill)["trades"]
                              if FIRST <= t["date"] <= END]}
            n += len(got["trades"])
            br = rc.check_market(got, data["minutes"], data["daily"], data["rolls"], sp, s, fill, market,
                                 first=FIRST, last=END)
            if br:
                out["%s/%s" % (s["name"], fill)] = br[:50] + (["... %d more" % (len(br) - 50)] if len(br) > 50 else [])
            if fill == "midpoint":
                mids[s["name"]] = got["trades"]
    return market, out, n, mids


def main():
    with multiprocessing.get_context("fork").Pool(len(specs_mod.MARKETS)) as pool:
        res = pool.map(_work, specs_mod.MARKETS)
    breaks = {m: b for m, b, _, _ in res if b}
    trades = sum(n for _, _, n, _ in res)
    acct, acct_trades = {}, 0
    for s in measure.grid("5"):
        by_m = {m: mids[s["name"]] for m, _, _, mids in res}
        for risk in (0.05, 0.5):
            r = fade.account(by_m, specs_mod.SPECS, risk, 150000.0)
            acct_trades += len(r["trades"])
            br = rc.check_account(r, {m: {"trades": v} for m, v in by_m.items()}, specs_mod.SPECS, risk, 150000.0)
            if br:
                acct["%s/%s" % (s["name"], risk)] = br[:50]
    os.makedirs(os.path.join(_HERE, "out"), exist_ok=True)
    summary = {"trades_checked": trades, "account_trades_checked": acct_trades, "market_breaks": breaks,
               "account_breaks": acct, "clean": not breaks and not acct}
    with open(os.path.join(_HERE, "out", "check_all.json"), "w") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    print("trades checked", trades, "| account trades", acct_trades, "| market settings with breaks",
          sum(len(b) for b in breaks.values()), "| account checks with breaks", len(acct), "| clean",
          summary["clean"])
    for m, b in breaks.items():
        for k, v in list(b.items())[:3]:
            print(m, k, v[:3])
    for k, v in list(acct.items())[:3]:
        print(k, v[:3])
    return 0 if summary["clean"] else 1


if __name__ == "__main__":
    sys.exit(main())
