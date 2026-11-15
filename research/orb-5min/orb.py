#!/usr/bin/env python3
"""Candidate 2: the 5-minute opening range breakout (ORB) on NQ 1-minute bars, long and short.

Why this one: candidate 1 and its four variations all passed the profit bar and failed the survival bar.
The handoff (pasted by Amear 2026-11-15): "Do not fix this by lowering risk per trade alone, because it
cuts profit by the same factor. Search for strategies whose profit is large against their worst losing
runs." Both bars are in dollars and both scale with the risk per trade, so what decides a pass is one
number that does not depend on the risk size: total profit divided by the drop the account takes in the
worst 5% of shuffled orders. Both bars can be met together only if that number is 2 or more. This file
reports it as the "headroom" for every run.

The rule is published and fully mechanical: Zarattini and Aziz, "Can Day Trading Really Be Profitable?"
(SSRN 4416622, 2023), the 5-minute ORB on QQQ. Its stop sits at the far side of the first five minutes,
so the stop is close to the entry and few signals should cost more than the risk budget. An independent
replication (mql5 blog, post 776235) reports the profit before costs reproduces and is near zero after
costs; that is the main risk to this candidate. The paper's own text is not in the repo: the rule below
is the published rule as summarised by the paper's abstract and two write-ups, and the 10R target is
from the paper as recalled, not re-read.

LOCKED SETTINGS (fixed before any run; none is tuned):
  data          NQ continuous 1-minute, 2021-03-08 to 2026-07-17 (the project's only data), bars 09:31-16:00 ET
  opening range the five bars stamped 09:31 to 09:35 (09:30:00-09:35:00). Open = the 09:31 bar's open,
                close = the 09:35 bar's close, high/low = their extremes
  direction     close > open: long. close < open: short. close == open: no trade that day
  entry         market order at the open of the first bar after 09:35 (the 09:36 bar; on 2026-04-02 that
                bar is missing from the data and the 09:37 bar is used), one trade a day at most
  stop          stop-market resting from the fill: long at the opening range low, short at its high
  target        10 x the risk distance from the fill (the paper's 10R); rarely reached, so most trades end
                at the stop or at the close
  close         flat on the 15:59 bar (filled at the 16:00 bar's open); an early-close session closes at
                its last bar
  same bar      if one bar reaches both the stop and the target, the stop is taken (the worse case)
  size          micro contracts (MNQ, $2 a point) = floor(1% of current balance / (risk distance x $2)),
                and never more than 4 x the balance in contract value (the paper's leverage cap);
                fewer than one -> the trade is skipped and counted
  costs         2 ticks (0.5 point) slippage on every fill, the target included; $1.90 commission per
                contract round trip
  account       $50,000 start (stand-in), firm limit $2,000 (stand-in), the end-of-day trailing rule and
                the 10,000-shuffle count exactly as in candidate 1 (research/intraday-momentum-long/run.py)
  periods       seen 2021-03-08 to 2024-12-31 first; unseen 2025-01-01 to 2026-07-17 only after

Standard library only. Run: python3 -I -B research/orb-5min/orb.py
"""
import argparse
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "research", "intraday-momentum-long"))
import run as R          # noqa: E402  candidate 1: trailing rule, shuffle, stats, constants
import variations as V   # noqa: E402  per-year return

mk = R.mk
OR_FIRST, OR_LAST, ENTRY_MOD = 9 * 60 + 31, 9 * 60 + 35, 9 * 60 + 36
TARGET_R = 10.0
LEVERAGE_CAP = 4.0
RISK_PCT = 1.0


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def opening_range(session):
    """-> (open, high, low, close, index of the entry bar, the first after 09:35) or None if the opening bars are incomplete."""
    bars = session.bars
    if len(bars) < 6 or [b.mod for b in bars[:5]] != list(range(OR_FIRST, OR_LAST + 1)) or bars[5].mod < ENTRY_MOD:
        return None
    first5 = bars[:5]
    return (first5[0].o, max(b.h for b in first5), min(b.l for b in first5), first5[-1].c, 5)


def direction(o, c):
    return 1 if c > o else -1 if c < o else 0


def entry_fill(bar, side):
    return _clamp(bar.o + side * R.SLIP, bar.l, bar.h)


def exit_fill(bar, side):
    return _clamp(bar.o - side * R.SLIP, bar.l, bar.h)


def stop_hit(bar, side, stop):
    return bar.l <= stop if side == 1 else bar.h >= stop


def stop_fill(bar, side, stop):
    """At the stop, or at the open if the bar opened through it, 2 ticks worse."""
    if side == 1:
        return _clamp(min(stop, bar.o) - R.SLIP, bar.l, bar.h)
    return _clamp(max(stop, bar.o) + R.SLIP, bar.l, bar.h)


def target_hit(bar, side, target):
    return bar.h >= target if side == 1 else bar.l <= target


def target_fill(bar, side, target):
    if side == 1:
        return _clamp(max(target, bar.o) - R.SLIP, bar.l, bar.h)
    return _clamp(min(target, bar.o) + R.SLIP, bar.l, bar.h)


class Sim(object):
    def __init__(self, risk_pct=RISK_PCT, start=R.START, period=None):
        self.risk_pct, self.balance, self.start, self.period = risk_pct, start, start, period
        self.trades, self.days = [], []
        self.skipped = self.no_signal = self.capped = 0
        self.pos = None

    def _open(self, bar, side, stop):
        px = entry_fill(bar, side)
        dist = (px - stop) * side
        if dist <= 0:
            self.skipped += 1
            return
        budget = self.risk_pct / 100.0 * self.balance
        by_risk = int(budget / (dist * R.PV) + 1e-9)
        by_lev = int(LEVERAGE_CAP * self.balance / (px * R.PV) + 1e-9)
        qty = min(by_risk, by_lev)
        if qty < 1:
            self.skipped += 1
            return
        if by_lev < by_risk:
            self.capped += 1
        self.pos = {"entry_dt": bar.dt, "side": side, "entry": px, "stop": stop,
                    "target": px + side * TARGET_R * dist, "qty": qty, "planned": qty * dist * R.PV,
                    "budget": budget, "worst": px, "capped": by_lev < by_risk}

    def _close(self, bar, px, reason):
        p = self.pos
        net = (px - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]
        self.balance += net
        worst = min(p["worst"], px) if p["side"] == 1 else max(p["worst"], px)
        self.trades.append({"entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
                            "side": p["side"], "entry": p["entry"], "exit": px, "stop": p["stop"],
                            "target": round(p["target"], 4), "qty": p["qty"], "capped": p["capped"],
                            "planned_loss": round(p["planned"], 2), "budget": round(p["budget"], 2),
                            "reason": reason, "net": round(net, 2), "balance": round(self.balance, 2),
                            "worst_price": worst})
        self.pos = None

    def _adverse(self, bar):
        return bar.l if self.pos["side"] == 1 else bar.h

    def _mark(self, price):
        p = self.pos
        return self.balance + (price - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]

    def run(self, market):
        lo, hi = self.period or (market.start, market.end)
        for s in market.sessions:
            if not (lo <= s.date <= hi):
                continue
            day_start = day_low = self.balance
            orng = opening_range(s)
            side = direction(orng[0], orng[3]) if orng else 0
            if orng and side == 0:
                self.no_signal += 1
            if orng is None:
                raise AssertionError("incomplete opening range on %s" % s.date)
            last = len(s.bars) - 1
            pend_exit = None
            for i, bar in enumerate(s.bars):
                if pend_exit and self.pos:
                    self._close(bar, exit_fill(bar, self.pos["side"]), pend_exit)
                    day_low = min(day_low, self.balance)
                    pend_exit = None
                    continue
                if i == orng[4] and side != 0:
                    self._open(bar, side, orng[2] if side == 1 else orng[1])
                if not self.pos:
                    continue
                p = self.pos
                if stop_hit(bar, p["side"], p["stop"]):
                    fill = stop_fill(bar, p["side"], p["stop"])
                    p["worst"] = fill if p["side"] == 1 and fill < p["worst"] or p["side"] == -1 and fill > p["worst"] else p["worst"]
                    self._close(bar, fill, "stop")
                    day_low = min(day_low, self.balance)
                    continue
                adv = self._adverse(bar)
                p["worst"] = min(p["worst"], adv) if p["side"] == 1 else max(p["worst"], adv)
                day_low = min(day_low, self._mark(adv))
                if target_hit(bar, p["side"], p["target"]):
                    self._close(bar, target_fill(bar, p["side"], p["target"]), "target")
                    day_low = min(day_low, self.balance)
                    continue
                if i == last:
                    self._close(bar, _clamp(bar.c - p["side"] * R.SLIP, bar.l, bar.h), "session close")
                    day_low = min(day_low, self.balance)
                    continue
                if bar.mod >= R.FLAT_MOD:
                    pend_exit = "flat 15:59"
            if self.pos:
                raise AssertionError("position open after %s" % s.date)
            day_low = min(day_low, self.balance)
            self.days.append({"date": s.date, "start": round(day_start, 2), "end": round(self.balance, 2),
                              "low": round(day_low, 2)})
        return self


def shuffled_depth(days, runs=R.SHUFFLES, seed=R.SEED, start=R.START):
    """Same reorderings as candidate 1's shuffle (same seed, same day blocks), but run to the end and
    record each order's deepest fall below the end-of-day high. -> the depth reached in 95% of orders,
    i.e. the drop the account takes in the worst 5% of shuffles."""
    blocks = [(d["end"] - d["start"], d["low"] - d["start"]) for d in days if d["end"] != d["start"] or d["low"] != d["start"]]
    rng = random.Random(seed)
    depths = []
    for _ in range(runs):
        rng.shuffle(blocks)
        bal = hwm = start
        deep = 0.0
        for pnl, low in blocks:
            deep = max(deep, hwm - (bal + low))
            bal += pnl
            hwm = max(hwm, bal)
        depths.append(deep)
    depths.sort()
    return round(depths[int(0.95 * runs) - 1], 2)


def summarise(sim, years):
    st = R.stats(sim)
    st["shorts"] = sum(1 for t in sim.trades if t["side"] == -1)
    st["targets"] = sum(1 for t in sim.trades if t["reason"] == "target")
    st["no_signal_days"] = sim.no_signal
    st["capped"] = sim.capped
    st["per_year_pct"] = round(V.per_year(sim.start, sim.balance, years), 1)
    return st


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=R.DATA)
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    a = ap.parse_args(argv)
    market = mk.load_market(a.data, session_start=R.SESSION_START)
    os.makedirs(a.out, exist_ok=True)
    yrs = {"seen": V.years_between(*R.SEEN), "unseen": V.years_between(*R.UNSEEN),
           "full": V.years_between(market.start, market.end)}
    results = {}
    for label, period in (("seen", R.SEEN), ("unseen", R.UNSEEN), ("full", None)):
        sim = Sim(period=period).run(market)
        st = summarise(sim, yrs[label])
        results[label] = (sim, st)
        print("%-6s trades %4d (shorts %d) | win %4.1f%% | net %9s | %.1f%% a year | PF %s | worst closed drop %s | "
              "largest loss %s | losing run %d | stops %d | targets %d | skipped %d | no-signal days %d | "
              "capped %d | avg MNQ %.2f | sha %s"
              % (label, st["trades"], st["shorts"], st["win_pct"], R.money(st["net"]), st["per_year_pct"],
                 st["profit_factor"], R.money(st["max_closed_drawdown"]), R.money(st["largest_loss"]),
                 st["longest_losing_run"], st["stop_exits"], st["targets"], st["skipped"], st["no_signal_days"],
                 st["capped"], st["avg_contracts"], R.digest(sim)[:12]))
        print("       by year: %s" % st["by_year"])
        with open(os.path.join(a.out, label + ".json"), "w") as fh:
            json.dump({"stats": st, "trades": sim.trades, "days": sim.days}, fh, indent=1)
    full_sim, full = results["full"]
    tr = R.trailing(full_sim.days)
    sh = R.shuffled(full_sim.days)
    depth = shuffled_depth(full_sim.days)
    headroom = round(full["net"] / depth, 2) if depth > 0 else None
    a_pass, b_pass = full["net"] >= 2 * R.LIMIT, sh["pct"] <= 5.0
    print()
    print("PROFIT   total %s against a bar of %s -> %s | %.1f%% a year | skipped %d"
          % (R.money(full["net"]), R.money(2 * R.LIMIT), "PASS" if a_pass else "FAIL", full["per_year_pct"],
             full["skipped"]))
    print("SURVIVAL real order: crossed %s, closest room %s on %s | shuffled: crossed in %d of %d (%.1f%%) vs 5%% -> %s"
          % (tr["first_cross"] or "never", R.money(tr["closest_room"]), tr["closest_date"], sh["crossed"],
             sh["runs"], sh["pct"], "PASS" if b_pass else "FAIL"))
    print("HEADROOM profit %s / worst-5%%-of-shuffles drop %s = %s (both bars together need 2 or more)"
          % (R.money(full["net"]), R.money(depth), headroom))
    with open(os.path.join(a.out, "branches.json"), "w") as fh:
        json.dump({"A": {"net": full["net"], "bar": 2 * R.LIMIT, "pass": a_pass,
                         "per_year_pct": full["per_year_pct"], "skipped": full["skipped"]},
                   "B": {"trailing": tr, "shuffled": sh, "pass": b_pass},
                   "headroom": {"worst_5pct_drop": depth, "ratio": headroom}}, fh, indent=1)


if __name__ == "__main__":
    main()
