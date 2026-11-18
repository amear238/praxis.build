#!/usr/bin/env python3
"""check_all.py -- the independent rule check (rule_check.py, written from PLAN.md alone by a separate agent)
run against every trade of every measured setting of candidate 1: 72 settings x 11 markets, trading dates
2018-01-01 to 2023-12-31, midpoint fills, plus the kind and harsh fills on every setting with ALL; then the
account check on two risk sizes for every k and target of ALL. Writes out/check_all.json; exit 1 on any break.

Run: python3 -I -B research/levels-150k/check_all.py. Standard library only.
"""
import json
import multiprocessing
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_TREND = os.path.join(os.path.dirname(_HERE), "trend-150k")
for p in (_HERE, _TREND):
    if p not in sys.path:
        sys.path.append(p)
import fade  # noqa: E402
import retest  # noqa: E402
import levels  # noqa: E402
import measure  # noqa: E402
import rule_check  # noqa: E402
import specs as specs_mod  # noqa: E402

OUT = os.path.join(_HERE, "out")


def _work(market):
    sp = specs_mod.SPECS[market]
    data = specs_mod.load(market)
    mk = levels.Market(data["minutes"], data["daily"], data["rolls"], sp, market)
    window = {d.date for d in mk.days if measure.FIRST <= d.date <= measure.END}
    out, pcs, n = {}, {}, 0
    jobs = [(s, "midpoint") for s in measure.grid()]
    jobs += [(s, f) for s in measure.grid() if s["kind"] == "ALL" for f in ("kind", "harsh-stops")]
    for s, fill in jobs:
        got = fade.per_contract(mk, s, fill, dates=window)
        n += len(got["trades"])
        br = rule_check.check_market(got, data["minutes"], data["daily"], data["rolls"], sp, s, fill, market,
                                     first=measure.FIRST, last=measure.END)
        if br:
            out["%s/%s" % (s["name"], fill)] = br[:50] + (["... %d more" % (len(br) - 50)] if len(br) > 50 else [])
        if s["kind"] == "ALL" and fill == "midpoint":
            pcs[s["name"]] = got["trades"]
    return market, out, n, pcs


def main():
    with multiprocessing.get_context("fork").Pool(len(specs_mod.MARKETS)) as pool:
        res = pool.map(_work, specs_mod.MARKETS)
    breaks = {m: b for m, b, _, _ in res if b}
    trades = sum(n for _, _, n, _ in res)
    acct = {}
    for s in measure.grid():
        if s["kind"] != "ALL":
            continue
        by_m = {m: pcs[s["name"]] for m, _, _, pcs in res}
        for risk in (0.05, 0.5):
            r = fade.account(by_m, specs_mod.SPECS, risk, 150000.0)
            br = rule_check.check_account(r, {m: {"trades": v} for m, v in by_m.items()}, specs_mod.SPECS, risk,
                                          150000.0)
            if br:
                acct["%s/%s" % (s["name"], risk)] = br[:50]
    os.makedirs(OUT, exist_ok=True)
    summary = {"trades_checked": trades, "market_breaks": breaks, "account_breaks": acct,
               "clean": not breaks and not acct}
    with open(os.path.join(OUT, "check_all.json"), "w") as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    print("trades checked", trades, "| market settings with breaks", sum(len(b) for b in breaks.values()),
          "| account checks with breaks", len(acct), "| clean", summary["clean"])
    for m, b in breaks.items():
        for k, v in list(b.items())[:3]:
            print(m, k, v[:3])
    for k, v in list(acct.items())[:3]:
        print(k, v[:3])
    return 0 if summary["clean"] else 1


if __name__ == "__main__":
    sys.exit(main())
