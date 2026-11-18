#!/usr/bin/env python3
"""measure.py -- the measuring pass of the trend plan (research/trend-150k/PLAN.md, "How the search runs" step 1):
both versions, every market, 2018-01-01 to 2023-12-31 only, midpoint fills, size-free (every figure in R, the
money a trade risks). Judges nothing; writes out/measure.json and out/MEASURE.md.

Grids (the plan's values): lookback L in (20, 60, 120, 250); stop multiple k in (0.5, 1, 2) for A and (2, 3, 4)
for B; trail t in (0.5, 1, 2) times the stop distance; atr_days 14. A also has entry in ("09:35", "10:00"),
flat 15:55. 72 settings for A, 36 for B.

R per trade.
  A: loss for one contract lpc = (dist + slip) * pv + comm; r = (points * pv - comm) / lpc; worst_r =
     (worst * pv - comm) / lpc. Computed at one contract, so no rounding of size enters.
  B: weekly.run on the one market at a fixed $1,000,000 risk a trade (start 1e12, risk_pct 1e-4, cap lifted),
     so whole-contract rounding is negligible; r = net / planned_cost. Each market's day records give its day
     rows in R ((end - start) / 1e6, (low - start) / 1e6), summed across markets by date.
  The portfolio's day rows: for each date, the sum over markets of (end change, low change) in R, every market
  at the same risk, all lows at once (conservative).

Windows. A: the minutes on New York dates 2018-01-01 to 2023-12-31; signals read the daily file from 2010.
  B: each market's daily series sliced by slice_b so its first possible decision is the bar before
  2018-01-01's first bar and its last bar is the last on or before 2023-12-31 (a position open then closes at
  that close, reason "end").

Portfolio figures: trades, win %, average winner / loser in R, net R, net R by year, longest losing run (trades
in entry order), max_gap (most calendar days in a row with no new entry; the calendar is every date on which
any market has a bar in the window), worst day in R, dd975_r (orb-150k's method: 2,000 shuffles of the day rows,
seed 20261115, the 97.5th percentile of the largest drop from the high-water mark), safe_dollars_per_r =
4,500 / dd975_r, projected_profit = net_r / measured_days * full_days * safe_dollars_per_r with full_days the
calendar's length from 2018-01-01 to the data's end, headroom = projected_profit / 9,000.

Run: python3 -I -B research/trend-150k/measure.py (one worker per market).

Standard library only.
"""
import json
import math
import multiprocessing
import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import sameday  # noqa: E402
import specs as specs_mod  # noqa: E402
import weekly  # noqa: E402

DAY_NS = 86400 * 1_000_000_000
FIRST, END = "2018-01-01", "2023-12-31"
YEARS = ("2018", "2019", "2020", "2021", "2022", "2023")
LIMIT, TARGET = 4500.0, 9000.0
RUNS, SEED = 2000, 20261115
ATR_DAYS = 14
B_START, B_RISK_PCT, B_UNIT = 1e12, 1e-4, 1e6
OUT = os.path.join(_HERE, "out")


def grid_a():
    return [{"name": "A-L%d-k%g-t%g-%s" % (L, k, t, e.replace(":", "")), "lookback": L, "atr_days": ATR_DAYS,
             "stop_mult": k, "trail_mult": t, "entry": e, "flat": "15:55"}
            for L in (20, 60, 120, 250) for k in (0.5, 1, 2) for t in (0.5, 1, 2) for e in ("09:35", "10:00")]


def grid_b():
    return [{"name": "B-L%d-k%g-t%g" % (L, k, t), "lookback": L, "atr_days": ATR_DAYS, "stop_mult": k,
             "trail_mult": t, "risk_pct": B_RISK_PCT}
            for L in (20, 60, 120, 250) for k in (2, 3, 4) for t in (0.5, 1, 2)]


# ---------------------------------------------------------------------------------------------- pieces
def r_sameday(t, sp):
    lpc = (t["dist"] + sp["slip_ticks"] * sp["tick"]) * sp["pv"] + sp["comm"]
    return (t["points"] * sp["pv"] - sp["comm"]) / lpc, (t["worst"] * sp["pv"] - sp["comm"]) / lpc


def longest_losing_run(rs):
    run = best = 0
    for r in rs:
        run = run + 1 if r < 0 else 0
        best = max(best, run)
    return best


def max_gap(calendar, traded):
    gap = best = 0
    for d in calendar:
        gap = 0 if d in traded else gap + 1
        best = max(best, gap)
    return best


def _max_drop(rows):
    bal = hwm = worst = 0.0
    for end, low in rows:
        worst = max(worst, hwm - (bal + low))
        bal += end
        hwm = max(hwm, bal)
    return worst


def dd975_r(day_rows, runs=RUNS, seed=SEED):
    rng = random.Random(seed)
    figs = []
    for _ in range(runs):
        x = list(day_rows)
        rng.shuffle(x)
        figs.append(_max_drop(x))
    figs.sort()
    return figs[int(math.ceil(0.975 * runs)) - 1]


def slice_b(series, first_day, last_day, lookback, atr_days):
    i0 = next(i for i, a in enumerate(series) if a.bar.ts // DAY_NS >= first_day)
    i1 = max(i for i, a in enumerate(series) if a.bar.ts // DAY_NS <= last_day)
    s = max(0, i0 - 1 - max(lookback, atr_days - 1))
    return series[s:i1 + 1]


def _day(iso):
    import datetime as dt
    return (dt.date.fromisoformat(iso) - dt.date(1970, 1, 1)).days


def _iso(day):
    import datetime as dt
    return (dt.date(1970, 1, 1) + dt.timedelta(days=day)).isoformat()


# ---------------------------------------------------------------------------------------------- workers
def _work_a(market):
    sp = specs_mod.SPECS[market]
    data = specs_mod.load(market)
    days_all = sameday.et_days(data["minutes"], 9 * 60 + 35, 16 * 60)
    full_dates = sorted(days_all)
    days = {d: v for d, v in days_all.items() if FIRST <= d <= END}
    out = {}
    for s in grid_a():
        trs = sameday.per_contract(data["minutes"], data["daily"], sp, s, "midpoint", days=days)
        out[s["name"]] = [(t["date"], t["side"], *r_sameday(t, sp)) for t in trs]
    return market, out, sorted(days), full_dates


def _work_b(market):
    data = specs_mod.load(market, minutes=False)
    sp = dict(specs_mod.SPECS[market], max_qty=10 ** 12)
    lo, hi = _day(FIRST), _day(END)
    out = {}
    for s in grid_b():
        ser = slice_b(data["daily"], lo, hi, s["lookback"], s["atr_days"])
        res = weekly.run({market: ser}, {market: sp}, s, fill="midpoint", start=B_START,
                         rolls={market: data["rolls"]})
        trs = [(_iso(t["entry_day"]), t["side"], t["net"] / t["planned_cost"], t["reason"], t["gap"])
               for t in res["trades"] if t["entry_day"] >= lo]
        rows = {d["date"]: ((d["end"] - d["start"]) / B_UNIT, (d["low"] - d["start"]) / B_UNIT)
                for d in res["days"] if d["day"] >= lo}
        out[s["name"]] = (trs, rows)
    cal = sorted({_iso(a.bar.ts // DAY_NS) for a in data["daily"] if lo <= a.bar.ts // DAY_NS <= hi})
    full = sorted({_iso(a.bar.ts // DAY_NS) for a in data["daily"] if a.bar.ts // DAY_NS >= lo})
    return market, out, cal, full


# ---------------------------------------------------------------------------------------------- summary
def _mean(xs):
    return sum(xs) / len(xs) if xs else None


def _stats(trades):
    """trades: [(date, side, r, ...)] in entry order."""
    rs = [t[2] for t in trades]
    wins, losses = [r for r in rs if r > 0], [r for r in rs if r < 0]
    return {"trades": len(rs), "win_pct": 100.0 * len(wins) / len(rs) if rs else None,
            "avg_winner_r": _mean(wins), "avg_loser_r": _mean(losses), "net_r": sum(rs),
            "net_r_by_year": {y: sum(t[2] for t in trades if t[0][:4] == y) for y in YEARS},
            "longest_losing_run": longest_losing_run(rs)}


def _portfolio(by_market, day_rows, calendar, full_days):
    order = list(specs_mod.MARKETS)
    trades = sorted(((t, order.index(m)) for m, trs in by_market.items() for t in trs),
                    key=lambda x: (x[0][0], x[1]))
    trades = [t for t, _ in trades]
    st = _stats(trades)
    rows = [day_rows[d] for d in sorted(day_rows) if day_rows[d] != (0.0, 0.0)]
    dd = dd975_r(rows) if rows else None
    safe = LIMIT / dd if dd and dd > 0 else None
    proj = st["net_r"] / len(calendar) * full_days * safe if safe else None
    st.update(max_gap=max_gap(calendar, {t[0] for t in trades}), worst_day_r=min((r[1] for r in rows), default=None),
              dd975_r=dd, safe_dollars_per_r=safe, projected_profit=proj,
              headroom=proj / TARGET if proj is not None else None,
              measured_days=len(calendar), full_days=full_days)
    return st


def summarise_a(results):
    calendar = sorted(set().union(*[set(c) for _, _, c, _ in results]))
    full_days = len(set().union(*[{d for d in f if d >= FIRST} for _, _, _, f in results]))
    rows_out = []
    for s in grid_a():
        by_m = {m: out[s["name"]] for m, out, _, _ in results}
        day_rows = {}
        for trs in by_m.values():
            for date, _side, r, worst in trs:
                e, lo = day_rows.get(date, (0.0, 0.0))
                day_rows[date] = (e + r, lo + worst)
        day_rows = {d: (e, min(lo, 0.0, e)) for d, (e, lo) in day_rows.items()}
        rows_out.append({"name": s["name"], "settings": s,
                         "portfolio": _portfolio(by_m, day_rows, calendar, full_days),
                         "markets": {m: _stats(trs) for m, trs in by_m.items()}})
    return rows_out


def summarise_b(results):
    calendar = sorted(set().union(*[set(c) for _, _, c, _ in results]))
    full_days = len(set().union(*[set(f) for _, _, _, f in results]))
    rows_out = []
    for s in grid_b():
        by_m = {m: out[s["name"]][0] for m, out, _, _ in results}
        day_rows = {}
        for m, out, _, _ in results:
            for date, (e, lo) in out[s["name"]][1].items():
                e0, lo0 = day_rows.get(date, (0.0, 0.0))
                day_rows[date] = (e0 + e, lo0 + lo)
        port = _portfolio(by_m, day_rows, calendar, full_days)
        all_t = [t for trs in by_m.values() for t in trs]
        port["gap_stop_pct"] = 100.0 * sum(1 for t in all_t if t[3] == "stop" and t[4]) / len(all_t) if all_t else None
        rows_out.append({"name": s["name"], "settings": s, "portfolio": port,
                         "markets": {m: _stats(trs) for m, trs in by_m.items()}})
    return rows_out


def _f(x, nd=2):
    return "-" if x is None else ("%.*f" % (nd, x))


def _md(title, rows, top=15):
    rows = sorted(rows, key=lambda r: -(r["portfolio"]["projected_profit"] or -1e18))
    lines = ["## " + title, "",
             "| Version | Trades | Win % | Avg winner R | Avg loser R | Net R | Longest losing run | Max days no trade "
             "| Worst day R | dd 97.5% R | Safe $ per R | Projected $ | vs $9,000 | R by year 2018..2023 |",
             "|---|" + "---:|" * 13 + "---|"]
    for r in rows[:top]:
        p = r["portfolio"]
        lines.append("| %s | %d | %s | %s | %s | %s | %d | %d | %s | %s | %s | %s | %s | %s |" % (
            r["name"], p["trades"], _f(p["win_pct"], 1), _f(p["avg_winner_r"]), _f(p["avg_loser_r"]),
            _f(p["net_r"], 1), p["longest_losing_run"], p["max_gap"], _f(p["worst_day_r"]), _f(p["dd975_r"], 1),
            _f(p["safe_dollars_per_r"], 0), _f(p["projected_profit"], 0), _f(p["headroom"]),
            " / ".join(_f(p["net_r_by_year"][y], 0) for y in YEARS)))
    lines.append("")
    best = rows[0]
    lines += ["Per market, %s:" % best["name"], "",
              "| Market | Trades | Win % | Avg winner R | Net R | Longest losing run | R by year |", "|---|" + "---:|" * 5 + "---|"]
    for m, st in best["markets"].items():
        lines.append("| %s | %d | %s | %s | %s | %d | %s |" % (
            m, st["trades"], _f(st["win_pct"], 1), _f(st["avg_winner_r"]), _f(st["net_r"], 1),
            st["longest_losing_run"], " / ".join(_f(st["net_r_by_year"][y], 0) for y in YEARS)))
    return lines + [""]


def main():
    os.makedirs(OUT, exist_ok=True)
    with multiprocessing.get_context("fork").Pool(len(specs_mod.MARKETS)) as pool:
        ra = pool.map(_work_a, specs_mod.MARKETS)
        rb = pool.map(_work_b, specs_mod.MARKETS)
    a, b = summarise_a(ra), summarise_b(rb)
    with open(os.path.join(OUT, "measure.json"), "w") as f:
        json.dump({"A": a, "B": b}, f, indent=1, sort_keys=True)
    md = ["# Trend measuring pass, 2018-01-01 to 2023-12-31", "",
          "Midpoint fills, every figure in R (the money one trade risks). Every market at the same risk; the "
          "portfolio's day lows summed all at once. Sorted by projected profit at the size that keeps the $4,500 "
          "limit crossed in no more than 1 shuffle in 40. Judges nothing; the locked list is written from this.", ""]
    md += _md("A. Same-day (top 15 of %d)" % len(a), a) + _md("B. Multi-week (top 15 of %d)" % len(b), b)
    with open(os.path.join(OUT, "MEASURE.md"), "w") as f:
        f.write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
