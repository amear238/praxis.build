#!/usr/bin/env python3
"""measure.py -- the measuring pass: 108 opening range breakout rules on 2021-03-08 to 2023-12-31 at one micro.

Each rule of grid() (3 or_minutes x 2 entries x 3 stops x 6 exits, both sides, entry_until 11:00 for
break, no max_or_atr, risk_pct 1.0 unused) is run by orb_engine.run with fixed_qty=1, fill "midpoint",
start 150,000, on the days dated up to 2023-12-31 only, and checked by orb_check.rule_check (a break stops
the pass). Nothing after 2023 is read for a result; the full file is loaded once only to count its trading
days for the projection. This module judges nothing; it writes out/measure.json and out/MEASURE.md.

Definitions (R per trade = net / planned_cost, i.e. the trade's r):
  calendar      the trading days with a bar stamped 09:31 (anywhere in the day's bars), from the first one
                on which the rule can trade: the 15th such day for a rule using the 14-day average
                (stop atr_frac or a max_or_atr filter), else the first.
  max_gap_days  the longest run of consecutive calendar days with no trade entered (skipped and filtered
                days are no-trade days).
  day rows      for each date with a trade: ((day end - day start) / planned_cost, (day low - day start) /
                planned_cost), in R.
  dd975_r       shuffle the day rows `runs` times (one random.Random(seed), a fresh copy shuffled each run);
                in each order, with balance and high-water mark starting at 0, the drop on a day is the
                high-water mark (the highest end-of-day balance so far) minus (the balance before the day +
                the day's low change); the day's end change is then added and the mark updated. The order's
                figure is its largest drop. Return the 97.5th percentile: the sorted figures at index
                ceil(0.975 * runs) - 1. runs 2,000, seed 20261115.
  safe_dollars_per_r = 4,500 / dd975_r. projected_profit = net_r / measured_days * full_days *
                safe_dollars_per_r, measured_days and full_days being the counts of trading days with a
                09:31 bar on 2021-03-08 to 2023-12-31 and on 2021-03-08 to 2026-07-17. headroom =
                projected_profit / 9,000. With dd975_r at 0 or below, all three are null.
  win_pct       share of trades with net > 0, in percent. avg_winner_r / avg_loser_r: mean R of the trades
                with net > 0 / net < 0 (null when none). longest_losing_run: most trades in a row with net < 0.
  terciles      for each or_minutes, the ratio (h - l) / atr14 over every measured day with a complete range
                and a 14-day average; cut points c1 = sorted[N // 3], c2 = sorted[2N // 3]; low < c1 <= mid <
                c2 <= high. Each trade on a day with a ratio falls in one; trades and net R per tercile.
  stop_loss_above_planned_pct   share of trades (percent) that are stop exits losing more than planned_cost
                by over a cent (gaps through the stop; information only).

Run: python3 -I -B research/orb-150k/measure.py  (forks one worker per CPU; the output does not depend on
it: rows are returned in grid order and every number is computed in one process per rule).

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
import orb_check    # noqa: E402
import orb_engine   # noqa: E402
import globex       # noqa: E402  (on the path through orb_engine)

END = "2023-12-31"
FIRST = "2021-03-08"
FULL_END = "2026-07-17"
YEARS = ("2021", "2022", "2023")
LIMIT = 4500.0
TARGET = 9000.0
RUNS, SEED = 2000, 20261115
OUT = os.path.join(_HERE, "out")

STOPS = (("far_side",), ("or_frac", 0.5), ("atr_frac", 0.10))
EXITS = (("hold_to_flat",), ("target_r", 3), ("target_r", 5), ("target_r", 10), ("trail_r", 1), ("trail_r", 2))


def _label(x):
    return x[0] if len(x) == 1 else "%s%g" % (x[0], x[1])


def grid():
    out = []
    for n in (5, 15, 30):
        for entry in ("direction", "break"):
            for stop in STOPS:
                for ex in EXITS:
                    out.append({"name": "or%d-%s-%s-%s" % (n, entry, _label(stop), _label(ex)),
                                "reason": "measuring pass, one micro, 2021-2023", "or_minutes": n,
                                "entry": entry, "entry_until": "11:00" if entry == "break" else None,
                                "sides": "both", "stop": list(stop), "exit": list(ex), "max_or_atr": None,
                                "risk_pct": 1.0})
    return out


# ---------------------------------------------------------------------------------------------- drawdown
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


def projection(net_r, dd975, measured_days, full_days):
    """-> (safe_dollars_per_r, projected_profit, headroom), or three None when dd975 <= 0."""
    if not dd975 or dd975 <= 0:
        return None, None, None
    safe = LIMIT / dd975
    projected = net_r / measured_days * full_days * safe
    return safe, projected, projected / TARGET


# ---------------------------------------------------------------------------------------------- one rule
def _uses_atr(s):
    return s["stop"][0] == "atr_frac" or s["max_or_atr"] is not None


def _open_days(days):
    return [d for d in days if orb_engine.SM_0931 in d.by_sm]


def _cuts(days, n):
    """-> ({date: ratio}, (c1, c2)) for or_minutes n."""
    ratio = {}
    for k, d in enumerate(days):
        r = orb_engine.opening_range(d, n)
        a = orb_engine.atr14(days, k) if r is not None else None
        if r is not None and a:
            ratio[d.date] = (r[1] - r[2]) / a
    xs = sorted(ratio.values())
    if not xs:
        return ratio, None
    return ratio, (xs[len(xs) // 3], xs[2 * len(xs) // 3])


def _mean(xs):
    return sum(xs) / len(xs) if xs else None


def measure_one(s, days, full_days, cuts=None):
    days = [d for d in days if d.date <= END]
    res = orb_engine.run(days, s, fill="midpoint", start=150000.0, fixed_qty=1)
    breaks = orb_check.rule_check(res, days)
    if breaks:
        raise AssertionError("%s: %d rule breaks, first: %s" % (s["name"], len(breaks), breaks[0]))
    trades = res["trades"]
    rs = [t["r"] for t in trades]
    wins = [t["r"] for t in trades if t["net"] > 0]
    losses = [t["r"] for t in trades if t["net"] < 0]
    run = longest = 0
    for t in trades:
        run = run + 1 if t["net"] < 0 else 0
        longest = max(longest, run)
    cal = [d.date for d in _open_days(days)]
    if _uses_atr(s):
        cal = cal[14:]
    traded = {t["date"] for t in trades}
    gap = best_gap = 0
    for date in cal:
        gap = 0 if date in traded else gap + 1
        best_gap = max(best_gap, gap)
    planned = {t["date"]: t["planned_cost"] for t in trades}
    day_rows = [((d["end"] - d["start"]) / planned[d["date"]], (d["low"] - d["start"]) / planned[d["date"]])
                for d in res["days"] if d["date"] in planned]
    dd = dd975_r(day_rows)
    net_r = sum(rs)
    measured_days = len(_open_days(days))
    safe, projected, headroom = projection(net_r, dd, measured_days, full_days)
    ratio, cut = cuts if cuts is not None else _cuts(days, s["or_minutes"])
    terc = {k: {"trades": 0, "net_r": 0.0} for k in ("low", "mid", "high")}
    if cut is not None:
        for t in trades:
            x = ratio.get(t["date"])
            if x is None:
                continue
            k = "low" if x < cut[0] else ("mid" if x < cut[1] else "high")
            terc[k]["trades"] += 1
            terc[k]["net_r"] += t["r"]
    above = sum(1 for t in trades if t["reason"] == "stop" and -t["net"] - t["planned_cost"] > 0.01 + 1e-9)
    return {
        "name": s["name"], "settings": s, "trades": len(trades),
        "skipped": sum(1 for x in res["skipped"] if x["reason"] == "stop under 10 points"),
        "win_pct": 100.0 * len(wins) / len(trades) if trades else None,
        "avg_winner_r": _mean(wins), "avg_loser_r": _mean(losses), "avg_r": _mean(rs), "net_r": net_r,
        "net_r_by_year": {y: sum(t["r"] for t in trades if t["date"][:4] == y) for y in YEARS},
        "net_r_long": sum(t["r"] for t in trades if t["side"] == "long"),
        "net_r_short": sum(t["r"] for t in trades if t["side"] == "short"),
        "longest_losing_run": longest, "max_gap_days": best_gap, "dd975_r": dd,
        "safe_dollars_per_r": safe, "projected_profit": projected, "headroom": headroom,
        "measured_days": measured_days, "full_days": full_days,
        "net_r_by_or_tercile": terc, "tercile_cuts": list(cut) if cut is not None else None,
        "stop_loss_above_planned_pct": 100.0 * above / len(trades) if trades else None,
        "digest": res["digest"],
    }


# ---------------------------------------------------------------------------------------------- the pass
def load(path):
    """-> (days up to 2023-12-31, count of trading days with a 09:31 bar over the whole range)."""
    days = [d for d in globex.load_days(path, end=END) if d.date <= END]
    full = globex.load_days(path)
    return days, len(_open_days(full))


_W = {}


def _work(i):
    s = _W["grid"][i]
    return measure_one(s, _W["days"], _W["full"], _W["cuts"][s["or_minutes"]])


def measure(days, full_days, workers=None):
    days = [d for d in days if d.date <= END]
    _W.update(grid=grid(), days=days, full=full_days,
              cuts={n: _cuts(days, n) for n in (5, 15, 30)})
    idx = list(range(len(_W["grid"])))
    if workers == 1:
        return [_work(i) for i in idx]
    with multiprocessing.get_context("fork").Pool(workers) as pool:
        return pool.map(_work, idx)


def _f(x, fmt):
    return "" if x is None else fmt % x


def markdown(rows, measured_days, full_days):
    key = lambda r: (r["headroom"] is None, -(r["headroom"] or 0.0), r["name"])  # noqa: E731
    lines = ["%d rules measured on %s to %s at one micro, midpoint fills (%d trading days; the projection "
             "scales to the %d trading days of %s to %s)." % (len(rows), FIRST, END, measured_days, full_days,
                                                               FIRST, FULL_END),
             "",
             "| Rule | Trades | Win % | Average winner (R) | Average loser (R) | Net (R) | Net 2021 (R) | "
             "Net 2022 (R) | Net 2023 (R) | Longest losing run | Longest gap (days) | Drawdown in 97.5% of "
             "shuffles (R) | Safe dollars per R | Projected profit ($) | Headroom | Net R by range size "
             "(low / mid / high) |",
             "|" + "---|" * 16]
    for r in sorted(rows, key=key):
        y = r["net_r_by_year"]
        t = r["net_r_by_or_tercile"]
        lines.append("| %s | %d | %s | %s | %s | %s | %s | %s | %s | %d | %d | %s | %s | %s | %s | %s |" % (
            r["name"], r["trades"], _f(r["win_pct"], "%.1f"), _f(r["avg_winner_r"], "%.2f"),
            _f(r["avg_loser_r"], "%.2f"), _f(r["net_r"], "%.1f"), _f(y["2021"], "%.1f"), _f(y["2022"], "%.1f"),
            _f(y["2023"], "%.1f"), r["longest_losing_run"], r["max_gap_days"], _f(r["dd975_r"], "%.1f"),
            _f(r["safe_dollars_per_r"], "%.0f"), _f(r["projected_profit"], "%.0f"), _f(r["headroom"], "%.2f"),
            "%.1f / %.1f / %.1f" % (t["low"]["net_r"], t["mid"]["net_r"], t["high"]["net_r"])))
    return "\n".join(lines) + "\n"


def main():
    data = os.environ.get("PRAXIS_DATA", orb_engine.DATA)
    days, full_days = load(data)
    rows = measure(days, full_days)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "measure.json"), "w") as fh:
        json.dump(rows, fh, sort_keys=True, indent=1)
        fh.write("\n")
    md = markdown(rows, rows[0]["measured_days"], full_days)
    with open(os.path.join(OUT, "MEASURE.md"), "w") as fh:
        fh.write(md)
    print("%d rules, %d measured days, %d full days" % (len(rows), rows[0]["measured_days"], full_days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
