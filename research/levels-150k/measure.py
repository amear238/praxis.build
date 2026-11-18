#!/usr/bin/env python3
"""measure.py -- the measuring pass of candidate 1 (research/levels-150k/PLAN.md, "How the search runs" steps 1
to 3): every market, trading dates 2018-01-01 to 2023-12-31 only, midpoint fills, every figure in R at one
contract. Judges nothing but the pre-run gate; writes out/measure.json and out/MEASURE.md.

Grid: kind in (PD, ON, PW, SW, RN, VP, SD, ALL) x k in (0.1, 0.2, 0.4) x target T in (3, 5, None): 72 settings.

R per trade (one contract): loss a contract lpc = (dist + slip) x pv + comm; r = (points x pv - comm) / lpc;
worst_r = (worst x pv - comm) / lpc; gross = points / dist (before costs).

Market sets per setting: all eleven, and "stable": the markets whose net R is above 0 at that setting in
2018-2020 and in 2021-2023 (none: no stable set).

Portfolio figures for a set (every market at the same risk): trades, win %, average winner / loser in R, net R,
gross R, net R by year, longest losing run (trades in (date, market order) order), max_gap (most consecutive
calendar dates with no new trade; the calendar is every trading date of any of the eleven markets in the
window), worst day (day rows: end = the sum of r, low = min(the sum of worst_r, 0, end)), dd975_r (2,000 day
shuffles, seed 20261115, the 97.5th percentile of the largest drop; research/trend-150k/measure.py's code),
safe_dollars_per_r = 4,500 / dd975_r, projected_profit = net_r / measured_days x full_days x safe, with
full_days the calendar's length from 2018-01-01 to the data's end, headroom = projected / 9,000.

Gate (plan step 3): average winner >= 2R, max_gap <= 7 and projected_profit >= 9,000.

Run: python3 -I -B research/levels-150k/measure.py [1|2] (candidate; one worker per market). Candidate 1 writes
out/, candidate 2 out/c2/. Standard library only.
"""
import importlib.util
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
import levels  # noqa: E402
import specs as specs_mod  # noqa: E402

_spec = importlib.util.spec_from_file_location("trend_measure", os.path.join(_TREND, "measure.py"))
tm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tm)

FIRST, END = "2018-01-01", "2023-12-31"
YEARS = ("2018", "2019", "2020", "2021", "2022", "2023")
LIMIT, TARGET = 4500.0, 9000.0
KINDS = levels.KINDS + ("ALL",)
ENGINES = {"1": fade}
TITLES = {"1": "Candidate 1 (fade the first touch of a marked level)", "2": "Candidate 2 (break and retest)"}
CAND = "1"


def out_dir(cand):
    return os.path.join(_HERE, "out") if cand == "1" else os.path.join(_HERE, "out", "c" + cand)


def grid():
    return [{"name": "%s-k%g-T%s" % (kd, k, "none" if t is None else t), "kind": kd, "k": k, "target": t,
             "atr_days": 14} for kd in KINDS for k in (0.1, 0.2, 0.4) for t in (3, 5, None)]


def r_rows(trades, sp):
    out = []
    slip = sp["slip_ticks"] * sp["tick"]
    for t in trades:
        lpc = (t["dist"] + slip) * sp["pv"] + sp["comm"]
        out.append((t["date"], t["side"], (t["points"] * sp["pv"] - sp["comm"]) / lpc,
                    (t["worst"] * sp["pv"] - sp["comm"]) / lpc, t["points"] / t["dist"]))
    return out


def stable_markets(by_m):
    out = []
    for m, rs in by_m.items():
        a = sum(r[2] for r in rs if r[0][:4] in ("2018", "2019", "2020"))
        b = sum(r[2] for r in rs if r[0][:4] in ("2021", "2022", "2023"))
        if a > 0 and b > 0:
            out.append(m)
    return out


def _mean(xs):
    return sum(xs) / len(xs) if xs else None


def portfolio(by_m, markets, calendar, full_days):
    order = {m: n for n, m in enumerate(markets)}
    trades = sorted(((r, order[m]) for m in markets for r in by_m.get(m, [])), key=lambda x: (x[0][0], x[1]))
    trades = [t for t, _ in trades]
    rs = [t[2] for t in trades]
    wins, losses = [r for r in rs if r > 0], [r for r in rs if r < 0]
    day = {}
    for t in trades:
        e, lo = day.get(t[0], (0.0, 0.0))
        day[t[0]] = (e + t[2], lo + t[3])
    rows = [(e, min(lo, 0.0, e)) for d, (e, lo) in sorted(day.items())]
    dd = tm.dd975_r(rows) if rows else None
    safe = LIMIT / dd if dd and dd > 0 else None
    net = sum(rs)
    proj = net / len(calendar) * full_days * safe if safe else None
    return {"markets": list(markets), "trades": len(rs), "win_pct": 100.0 * len(wins) / len(rs) if rs else None,
            "avg_winner_r": _mean(wins), "avg_loser_r": _mean(losses), "net_r": net,
            "gross_r": sum(t[4] for t in trades),
            "net_r_by_year": {y: sum(t[2] for t in trades if t[0][:4] == y) for y in YEARS},
            "longest_losing_run": tm.longest_losing_run(rs),
            "max_gap": tm.max_gap(calendar, {t[0] for t in trades}),
            "worst_day_r": min((r[1] for r in rows), default=None), "dd975_r": dd, "safe_dollars_per_r": safe,
            "projected_profit": proj, "headroom": proj / TARGET if proj is not None else None,
            "measured_days": len(calendar), "full_days": full_days}


def gate(p):
    return (p.get("avg_winner_r") is not None and p["avg_winner_r"] >= 2.0 and p["max_gap"] <= 7
            and p.get("projected_profit") is not None and p["projected_profit"] >= TARGET)


# ---------------------------------------------------------------------------------------------- workers
def _work(market):
    sp = specs_mod.SPECS[market]
    data = specs_mod.load(market)
    mk = levels.Market(data["minutes"], data["daily"], data["rolls"], sp, market)
    window = {d.date for d in mk.days if FIRST <= d.date <= END}
    full = sorted(d.date for d in mk.days if d.date >= FIRST)
    eng = ENGINES[CAND]
    out = {s["name"]: r_rows(eng.per_contract(mk, s, "midpoint", dates=window)["trades"], sp) for s in grid()}
    return market, out, sorted(window), full


def summarise(results):
    calendar = sorted(set().union(*[set(w) for _, _, w, _ in results]))
    full_days = len(set().union(*[set(f) for _, _, _, f in results]))
    all_m = [m for m in specs_mod.MARKETS if any(r[0] == m for r in results)]
    out = []
    for s in grid():
        by_m = {m: o[s["name"]] for m, o, _, _ in results}
        row = {"name": s["name"], "settings": s, "all": portfolio(by_m, all_m, calendar, full_days),
               "by_market": {m: portfolio(by_m, [m], calendar, full_days) for m in all_m}}
        st = [m for m in all_m if m in stable_markets(by_m)]
        row["stable"] = portfolio(by_m, st, calendar, full_days) if st else None
        row["gate"] = {"all": gate(row["all"]), "stable": bool(row["stable"]) and gate(row["stable"])}
        out.append(row)
    return out


def _f(x, nd=2):
    return "-" if x is None else ("%.*f" % (nd, x))


def _line(name, p):
    return "| %s | %s | %d | %s | %s | %s | %s | %s | %d | %d | %s | %s | %s | %s | %s |" % (
        name, ",".join(p["markets"]) if len(p["markets"]) < 11 else "all 11", p["trades"], _f(p["win_pct"], 1),
        _f(p["avg_winner_r"]), _f(p["net_r"], 1), _f(p["gross_r"], 1),
        _f(p["net_r"] / p["trades"] if p["trades"] else None, 3), p["longest_losing_run"], p["max_gap"],
        _f(p["dd975_r"], 1), _f(p["safe_dollars_per_r"], 0), _f(p["projected_profit"], 0), _f(p["headroom"]),
        " / ".join(_f(p["net_r_by_year"][y], 0) for y in YEARS))


HEAD = ["| Setting | Markets | Trades | Win % | Avg winner R | Net R | Gross R | Net R a trade | Longest losing run "
        "| Max days no trade | dd 97.5% R | Safe $ per R | Projected $ | vs $9,000 | Net R by year 2018..2023 |",
        "|---|---|" + "---:|" * 12 + "---|"]


def markdown(rows):
    passed = [(r["name"], k) for r in rows for k in ("all", "stable") if r["gate"][k]]
    md = ["# %s: measuring pass, 2018-01-01 to 2023-12-31" % TITLES[CAND], "",
          "PLAN.md. Midpoint fills, every figure in R (the money one trade "
          "risks), every market at the same risk, the portfolio's day lows summed at once. Sorted by projected "
          "profit at the size that keeps the $4,500 limit crossed in no more than 1 shuffle in 40.", "",
          "**Gate** (average winner at least 2R, never more than 7 trading days without a trade, projected profit at "
          "least $9,000): %s." % ("passed by " + ", ".join("%s (%s)" % p for p in passed) if passed
                                   else "**no setting passes, on either market set**"), ""]
    allrows = sorted(rows, key=lambda r: -(r["all"]["net_r"]))
    md += ["## All eleven markets (all 72 settings, by net R)", ""] + HEAD
    md += [_line(r["name"], r["all"]) for r in allrows] + [""]
    st = sorted([r for r in rows if r["stable"]], key=lambda r: -(r["stable"]["projected_profit"] or -1e18))
    md += ["## Stable markets (net R above 0 in 2018-2020 and in 2021-2023), %d settings have a set" % len(st), ""]
    md += HEAD + [_line(r["name"], r["stable"]) for r in st] + [""]
    best = allrows[0]
    md += ["## By market, %s" % best["name"], ""] + HEAD
    md += [_line(m, p) for m, p in best["by_market"].items()] + [""]
    md += ["## Net R a trade by kind and market, k 0.2, T 3", "",
           "| Kind | " + " | ".join(specs_mod.MARKETS) + " |", "|---|" + "---:|" * len(specs_mod.MARKETS)]
    for kd in KINDS:
        r = next(x for x in rows if x["name"] == "%s-k0.2-T3" % kd)
        md.append("| %s | %s |" % (kd, " | ".join(
            _f(r["by_market"][m]["net_r"] / r["by_market"][m]["trades"] if r["by_market"][m]["trades"] else None, 3)
            for m in specs_mod.MARKETS)))
    return md + [""]


def main(argv=None):
    global CAND
    argv = sys.argv[1:] if argv is None else argv
    CAND = argv[0] if argv else "1"
    OUT = out_dir(CAND)
    os.makedirs(OUT, exist_ok=True)
    with multiprocessing.get_context("fork").Pool(len(specs_mod.MARKETS)) as pool:
        results = pool.map(_work, specs_mod.MARKETS)
    rows = summarise(results)
    with open(os.path.join(OUT, "measure.json"), "w") as f:
        json.dump(rows, f, indent=1, sort_keys=True)
    md = markdown(rows)
    with open(os.path.join(OUT, "MEASURE.md"), "w") as f:
        f.write("\n".join(md))
    print("\n".join(md[:8]))


if __name__ == "__main__":
    main()
