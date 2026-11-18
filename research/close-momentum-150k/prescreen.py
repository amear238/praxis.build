#!/usr/bin/env python3
"""prescreen.py -- the pre-screen of PLAN.md ("How the search runs", step 1): for each market and signal,
2018-2023 only, no stop, the average of side x (price at C - price at C-30) in ticks before costs, the share of
days right, and the round-trip cost in ticks, for 2018-2020 and 2021-2023 apart. Writes out/PRESCREEN.md and
out/prescreen.json. Exit 2 when the plan's drop rule fires (edge at or below zero everywhere).

Run: python3 -I -B research/close-momentum-150k/prescreen.py [MARKET ...]   one market at a time, no pool.
Standard library only.
"""
import datetime as dt
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_RES = os.path.dirname(_HERE)
for p in (os.path.join(_RES, "levels-150k"), os.path.join(_RES, "trend-150k")):
    if p not in sys.path:
        sys.path.append(p)
import levels  # noqa: E402  (the New York clock, _wall)
import specs as specs_mod  # noqa: E402

# Open O and close C, minutes after midnight New York (PLAN.md, "Data and markets").
HOURS = {"NQ": (570, 960), "ES": (570, 960), "RTY": (570, 960),
         "ZN": (500, 900), "ZB": (500, 900),
         "6E": (500, 900), "6J": (500, 900), "6B": (500, 900), "6A": (500, 900),
         "CL": (540, 870), "GC": (500, 810)}
SIGNALS = ("S1", "S2", "S3")
FIRST, END = dt.date(2018, 1, 1).toordinal(), dt.date(2023, 12, 31).toordinal()
HALVES = (("2018-2020", FIRST, dt.date(2020, 12, 31).toordinal()), ("2021-2023", dt.date(2021, 1, 1).toordinal(), END))


def index_days(minutes, o, c):
    """{date ordinal: {minute of day: bar}} for the bars of the minutes the rule reads, New York weekdays only,
    the trading days (New York weekdays with minute bars in them), and each date's set of contracts."""
    # A margin either side of what the rule reads, so price_at and last_before alone set the windows.
    want = set(range(o + 20, o + 35)) | set(range(c - 40, c - 20)) | set(range(c - 5, c + 10))
    days, trading, iids = {}, set(), {}
    for b in minutes:
        w = levels._wall(b.ts)
        d = w // 86400 + levels.EPOCH_ORD
        if dt.date.fromordinal(d).weekday() >= 5:
            continue
        m = (w % 86400) // 60
        trading.add(d)
        iids.setdefault(d, set()).add(b.iid)
        if m in want:
            days.setdefault(d, {})[m] = b
    return days, sorted(trading), iids


def price_at(day, t):
    """The open of the first bar stamped in [t, t+5), or None (PLAN.md rule 1)."""
    for m in range(t, t + 5):
        b = day.get(m)
        if b is not None:
            return b
    return None


def last_before(day, t):
    """The last bar stamped in [t-5, t) (its close is the price), or None (PLAN.md rule 1)."""
    for m in range(t - 1, t - 6, -1):
        b = day.get(m)
        if b is not None:
            return b
    return None


def trades(minutes, o, c, tick=None):
    """[(date ordinal, {signal: side or 0}, entry price, exit price)] for every day with a trade possible.
    A side needs the signal more than eps = tick x 1e-6 away from Y (no tick: exactly away)."""
    eps = tick * 1e-6 if tick else 0.0
    days, trading, iids_by_day = index_days(minutes, o, c)
    out = []
    for k in range(1, len(trading)):
        d, prev = trading[k], trading[k - 1]
        today, yday = days.get(d, {}), days.get(prev, {})
        yb = price_at(yday, c)
        eb, xb = price_at(today, c - 30), price_at(today, c)
        s1b, s2b = last_before(today, c - 30), last_before(today, o + 30)
        if yb is None or eb is None or xb is None:
            continue
        if iids_by_day[d] != {yb.iid}:
            continue
        y = yb.open

        def side(b):
            if b is None or abs(b.close - y) <= eps:
                return 0
            return 1 if b.close > y else -1
        a, b = side(s1b), side(s2b)
        sides = {"S1": a, "S2": b, "S3": a if a == b else 0}
        out.append((d, sides, eb.open, xb.open))
    return out


def summarise(rows, tick, cost_ticks):
    res = {}
    for sig in SIGNALS:
        for name, lo, hi in (("2018-2023", FIRST, END),) + HALVES:
            g = [s[sig] * (x - e) / tick for d, s, e, x in rows if lo <= d <= hi and s[sig]]
            n = len(g)
            res["%s/%s" % (sig, name)] = {
                "trades": n,
                "edge_ticks": round(sum(g) / n, 4) if n else None,
                "right": round(sum(1 for v in g if v > 0) / n, 4) if n else None,
                "net_ticks": round(sum(g) / n - cost_ticks, 4) if n else None}
    return res


def cost_ticks(sp):
    return 2 * sp["slip_ticks"] + sp["comm"] / (sp["pv"] * sp["tick"])


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    markets = argv or list(specs_mod.MARKETS)
    out_dir = os.path.join(_HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "prescreen.json")
    allres = {}
    if argv and os.path.exists(path):
        with open(path) as f:
            allres = json.load(f)
    for m in markets:
        sp = specs_mod.SPECS[m]
        data = specs_mod.load(m)
        o, c = HOURS[m]
        rows = trades(data["minutes"], o, c, sp["tick"])
        ct = cost_ticks(sp)
        allres[m] = {"cost_ticks": round(ct, 4), "days": len([r for r in rows if FIRST <= r[0] <= END]),
                     "results": summarise(rows, sp["tick"], ct)}
        r = allres[m]["results"]
        print(m, "cost %.2f ticks" % ct, " ".join("%s %s/%s" % (s, r[s + "/2018-2023"]["edge_ticks"],
                                                            r[s + "/2018-2023"]["right"]) for s in SIGNALS), flush=True)
        del data, rows
    with open(path, "w") as f:
        json.dump(allres, f, indent=1, sort_keys=True)
    done = [m for m in specs_mod.MARKETS if m in allres]
    edges = [allres[m]["results"]["%s/%s" % (s, h)]["edge_ticks"] for m in done for s in SIGNALS
             for h, _, _ in HALVES]
    drop = len(done) == len(specs_mod.MARKETS) and all(e is None or e <= 0 for e in edges)
    with open(os.path.join(out_dir, "PRESCREEN.md"), "w") as f:
        f.write(report(allres, done, drop))
    print("drop rule fires" if drop else "drop rule does not fire", "(%d of %d markets)" % (len(done),
                                                                                        len(specs_mod.MARKETS)))
    return 2 if drop else 0


def report(allres, done, drop):
    L = ["# Momentum into the close: the pre-screen", "",
         "2018 to 2023 only, no stop, before costs: the average of side x (price at the close - entry price) in "
         "ticks, the share of days right, and the round-trip cost in ticks (`specs.py`). PLAN.md, \"How the search "
         "runs\", step 1. Written by `prescreen.py`.", "",
         "| Market | Signal | Days | Edge, ticks, 2018-2023 | Right | 2018-2020 | 2021-2023 | Cost, ticks | "
         "After costs |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for m in done:
        a = allres[m]
        for s in SIGNALS:
            r = a["results"]
            w, h1, h2 = r[s + "/2018-2023"], r[s + "/2018-2020"], r[s + "/2021-2023"]
            L.append("| %s | %s | %d | %s | %s | %s | %s | %.2f | %s |" % (
                m, s, w["trades"], _f(w["edge_ticks"]), _p(w["right"]), _f(h1["edge_ticks"]), _f(h2["edge_ticks"]),
                a["cost_ticks"], _f(w["net_ticks"])))
    L += ["", "Drop rule (fixed in PLAN.md before the run): the edge before costs at or below zero on all eleven "
          "markets, all three signals, both halves. **%s.**" % ("Fires: the family is dropped" if drop else
                                                                "Does not fire"), ""]
    return "\n".join(L)


def _f(x):
    return "" if x is None else "%+.2f" % x


def _p(x):
    return "" if x is None else "%.0f%%" % (100 * x)


if __name__ == "__main__":
    sys.exit(main())
