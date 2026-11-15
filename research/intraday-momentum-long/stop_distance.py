#!/usr/bin/env python3
"""Stop-distance variations of candidate 1 (long-only intraday momentum).

Amear's ask (2026-11-15): candidate 1 passed the profit bar and failed survival (24.5% against the 5% bar),
about 2% a year, 1,029 of 1,344 signals skipped because the stop was too far. "Propose and test variations
that address the stop distance. Fix every setting before each run, no tuning on results, 2025 to 2026 last."
Bars (his): profit >= 2 x the prop maximum drawdown ($2,000 stand-in -> $4,000); trailing limit crossed in
at most 5% of 10,000 shuffled orders. Also reported: return a year, skipped signals.

WHAT WAS ALREADY KNOWN WHEN THESE WERE CHOSEN (stated, not hidden): variations.py's V1-V4. A tighter stop
(the day's starting level) removes the skips but crosses the limit in 100% of shuffles at 1% risk ($500 a
trade, a quarter of the $2,000 limit); at 0.5% it is 53.8%. Losing runs were 6 to 12 trades. 2025-2026 has
been looked at for candidate 1 and V1-V4, so it is less unseen than it was.

ALL SETTINGS FIXED HERE, IN THIS FILE, AND COMMITTED BEFORE ANY OF D1-D4 WAS RUN. Everything not listed is
candidate 1's locked setting (run.py): 14-session noise band x1.0, :00/:30 decisions filled at the next
bar's open, long only, exit at a decision bar when close <= max(upper band, VWAP), flat 15:59, 2 ticks per
side, $1.90 commission per MNQ round trip, $50,000 start, end-of-day trailing floor $2,000 below the high.

  "cost distance"  the stop distance at which ONE micro contract loses exactly the cost of the trade,
                   slippage and commission included: (budget - $1.90) / $2 - 0.5 point, the stop then
                   rounded to the tick on the entry side (so the loss is never above the budget). The stop
                   is a stop-market order placed at the fill. At $50,000 and 0.25% that is 61.0 points.
  "moved up"       the strategy's own stop is used when at least one MNQ fits the budget under candidate 1's
                   sizing rule; when none fits, the stop is moved up to the cost distance and one MNQ is
                   traded, instead of skipping the signal.

  D1  lower band (candidate 1's stop), moved up instead of skipped, 1% risk     (candidate 1, no skips)
  D2  the cost distance always, one MNQ, 0.25% risk                              (stop set by the cost)
  D3  day's starting level (V1's stop), moved up instead of skipped, 0.25% risk
  D4  day's starting level, skipped if too far (V1's rule), 0.25% risk

Why 0.25% (D2-D4): the longest losing runs seen were 6 to 12; at 0.25% of $50,000 ($125) twelve losers in a
row use $1,500, inside the $2,000 limit. Chosen from the losing-run length, not from any D result.

One size-free figure is added: profit divided by the drop from the high that the shuffles reach 1 time in
20 (95th percentile). Changing the risk percentage scales both roughly together, so this figure shows
whether any risk size could pass both bars: roughly, it needs to be at least 2.

Order of work: --phase seen (2021-2024) for all four, then --phase unseen (2025-2026), then --phase full
(the whole run, which the two bars judge). Standard library only.
Run: python3 -I -B research/intraday-momentum-long/stop_distance.py --phase seen|unseen|full
"""
import argparse
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as R          # noqa: E402
import variations as V   # noqa: E402

mk, bd = R.mk, R.bd
OUT = os.path.join(HERE, "out", "stop_distance")

VARIANTS = {
    "D1": {"stop": "lower_band", "sides": "long", "exit": "trail", "risk": 1.0, "fallback": "move_up",
           "say": "candidate 1's stop, moved up instead of skipped, 1%"},
    "D2": {"stop": "cost", "sides": "long", "exit": "trail", "risk": 0.25, "fallback": "move_up",
           "say": "stop set by the cost, one micro, 0.25%"},
    "D3": {"stop": "reference", "sides": "long", "exit": "trail", "risk": 0.25, "fallback": "move_up",
           "say": "day's starting level, moved up instead of skipped, 0.25%"},
    "D4": {"stop": "reference", "sides": "long", "exit": "trail", "risk": 0.25, "fallback": "skip",
           "say": "day's starting level, skipped if too far, 0.25%"},
}


def cost_distance(budget):
    """Points from the fill at which one MNQ loses `budget` with 2 ticks slippage and commission."""
    return (budget - R.COMM) / R.PV - R.SLIP


def cost_stop(px, budget):
    """Long stop at the cost distance below the fill, rounded up to the tick (toward the entry)."""
    raw = px - cost_distance(budget)
    return math.ceil(raw / R.TICK - 1e-9) * R.TICK


class Sim(V.Sim):
    """variations.Sim with the stop-distance rule. Long only (every D variant is long only)."""

    def _open(self, bar, side, stop):
        assert side == 1
        px = V.entry_fill(bar, side)
        budget = self.v["risk"] / 100.0 * self.balance
        moved = False
        qty = 0
        if self.v["stop"] != "cost":
            dist = px - stop
            qty = int(budget / (dist * R.PV) + 1e-9) if dist > 0 else 0
        if qty < 1:
            if self.v["fallback"] != "move_up" or cost_distance(budget) <= 0:
                self.skipped += 1
                return
            stop, qty, moved = cost_stop(px, budget), 1, self.v["stop"] != "cost"
        self.pos = {"side": side, "entry_dt": bar.dt, "entry": px, "stop": stop, "qty": qty,
                    "budget": budget, "worst": px, "moved": moved}

    def _close(self, bar, px, reason):
        moved = self.pos["moved"]
        V.Sim._close(self, bar, px, reason)
        self.trades[-1]["moved_up"] = moved


def shuffle_drops(days, runs=R.SHUFFLES, seed=R.SEED, start=R.START, limit=R.LIMIT):
    """Same shuffles as run.shuffled (same blocks, seed, order). Per run: crossed or not, and the deepest
    drop below the end-of-day high over the whole run (marked at each day's low)."""
    blocks = [(d["end"] - d["start"], d["low"] - d["start"]) for d in days
              if d["end"] != d["start"] or d["low"] != d["start"]]
    rng = random.Random(seed)
    crossed, drops = 0, []
    for _ in range(runs):
        rng.shuffle(blocks)
        bal = hwm = start
        deepest, hit = 0.0, False
        for pnl, low in blocks:
            deepest = max(deepest, hwm - (bal + low))
            if not hit and bal + low <= hwm - limit:
                hit = True
            bal += pnl
            hwm = max(hwm, bal)
        crossed += hit
        drops.append(deepest)
    drops.sort()
    return {"runs": runs, "crossed": crossed, "pct": round(100.0 * crossed / runs, 1),
            "drop_1_in_20": round(drops[int(0.95 * runs)], 2), "drop_median": round(drops[runs // 2], 2)}


def summarise(sim, years):
    st = R.stats(sim)
    return {"trades": st["trades"], "skipped": sim.skipped, "moved_up": sum(1 for t in sim.trades if t["moved_up"]),
            "signals": st["trades"] + sim.skipped, "net": st["net"], "pf": st["profit_factor"],
            "win_pct": st["win_pct"], "per_year": round(V.per_year(R.START, sim.balance, years), 1),
            "worst_closed_drop": st["max_closed_drawdown"], "largest_loss": st["largest_loss"],
            "losing_run": st["longest_losing_run"], "stops": st["stop_exits"], "by_year": st["by_year"],
            "sha": V.digest(sim.trades)[:12]}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=("seen", "unseen", "full"), required=True)
    a = ap.parse_args(argv)
    os.makedirs(OUT, exist_ok=True)
    need = {"seen": None, "unseen": "seen", "full": "unseen"}[a.phase]
    if need and not os.path.exists(os.path.join(OUT, need + ".json")):
        sys.exit("run --phase %s first" % need)
    market = mk.load_market(R.DATA, session_start=R.SESSION_START)
    period = {"seen": R.SEEN, "unseen": R.UNSEEN, "full": None}[a.phase]
    years = V.years_between(*(period or (market.start, market.end)))
    rows = {}
    for name, v in VARIANTS.items():
        sim = Sim(v, period=period).run(market)
        row = summarise(sim, years)
        row["say"] = v["say"]
        if a.phase == "full":
            row["A_pass"] = row["net"] >= 2 * R.LIMIT
            row["trailing"] = R.trailing(sim.days)
            row["shuffle"] = shuffle_drops(sim.days)
            row["B_pass"] = row["shuffle"]["pct"] <= 5.0
            d = row["shuffle"]["drop_1_in_20"]
            row["profit_per_bad_stretch"] = round(row["net"] / d, 2) if d > 0 else None
            with open(os.path.join(OUT, name + ".json"), "w") as fh:
                json.dump({"variant": v, "row": row, "trades": sim.trades, "days": sim.days}, fh, indent=1)
        rows[name] = row
        print("%s  %s" % (name, v["say"]))
        print("    %s: %d trades of %d signals | skipped %d | stop moved up %d | net %s | %.1f%% a year | PF %s | "
              "win %.1f%% | worst closed drop %s | largest loss %s | losing run %d | sha %s"
              % (a.phase, row["trades"], row["signals"], row["skipped"], row["moved_up"], V.money(row["net"]),
                 row["per_year"], row["pf"], row["win_pct"], V.money(row["worst_closed_drop"]),
                 V.money(row["largest_loss"]), row["losing_run"], row["sha"]))
        print("    by year %s" % row["by_year"])
        if a.phase == "full":
            sh = row["shuffle"]
            print("    PROFIT   %s vs $4,000 -> %s" % (V.money(row["net"]), "PASS" if row["A_pass"] else "FAIL"))
            print("    SURVIVAL crossed in %.1f%% of %d shuffles vs 5%% -> %s | real order: %s, closest room %s (%s)"
                  % (sh["pct"], sh["runs"], "PASS" if row["B_pass"] else "FAIL",
                     row["trailing"]["first_cross"] or "never crossed", V.money(row["trailing"]["closest_room"]),
                     row["trailing"]["closest_date"]))
            print("    bad stretch 1 in 20 shuffles: %s below the high | profit / bad stretch = %s"
                  % (V.money(sh["drop_1_in_20"]), row["profit_per_bad_stretch"]))
    with open(os.path.join(OUT, a.phase + ".json"), "w") as fh:
        json.dump(rows, fh, indent=1)


if __name__ == "__main__":
    main()
