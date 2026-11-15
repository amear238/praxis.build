#!/usr/bin/env python3
"""Candidate 1: long-only intraday momentum (the noise-band breakout, long side only) on NQ 1-minute bars.

Amear's instruction (pasted 2026-11-15): long-only intraday momentum, stop-market order at entry at the
lower band, fixed-percent risk, 2 ticks of slippage per side, settings locked before the run, 2025 to
2026 kept unseen as the final check. Judge in two separate branches:
  A, profit:   total backtest profit >= 2 x the firm's maximum drawdown. Stand-in: $2,000 -> $4,000.
  B, survival: the account day by day under a trailing loss rule ($2,000 stand-in), and a shuffled-order
               simulation of how often the limit would be crossed. No pass number: figures only.

LOCKED SETTINGS (fixed before any run; none is tuned):
  data          NQ continuous 1-minute, 2021-03-08 to 2026-07-17 (the project's only data)
  session       bars 09:31 to 16:00 ET (regular hours)
  band          noise band from the last 14 sessions' move from the open at the same minute, multiplier 1.0
                (the published rule, as in the NinjaTrader version)
  decisions     on the :00 and :30 bars only, filled at the next bar's open
  entry         long when the bar closes above the upper band and no position is open
  stop          stop-market at the lower band of the entry decision bar, resting from the fill
  exit          at a decision bar, close <= max(upper band, session VWAP); flat on the 15:59 bar (filled
                at the 16:00 bar); anything still open closes at the session's last bar
  size          micro contracts (MNQ, $2 a point) = floor(1% of current balance / (stop distance x $2));
                fewer than one -> the trade is skipped and counted
  costs         2 ticks (0.5 point) slippage per side on every fill; $1.90 commission per contract round trip
  account       $50,000 start (stand-in), firm limit $2,000 (stand-in)
  trailing rule end-of-day trailing: the floor is the highest end-of-day balance so far minus $2,000;
                it never locks. The limit is crossed if the account, marked at each bar's low while a trade
                is open, falls to or below the floor at any time.
  periods       seen 2021-03-08 to 2024-12-31; unseen 2025-01-01 to 2026-07-17 (run only after the seen run)
  shuffle       10,000 reorderings of the trading days (each day's result and its worst point kept whole),
                fixed seed 20261115

Standard library only. Run: python3 -I -B research/intraday-momentum-long/run.py
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import random
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, "scripts", "wf", "oracle"))
import market as mk   # noqa: E402
import band as bd     # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
SESSION_START = "09:31"
LOOKBACK, NOISE_MULT = 14, 1.0
TICK, SLIP = 0.25, 0.5
PV, COMM = 2.0, 1.90
START, LIMIT = 50000.0, 2000.0
RISK_PCT = 1.0
SEEN = ("2021-03-08", "2024-12-31")
UNSEEN = ("2025-01-01", "2026-07-17")
SHUFFLES, SEED = 10000, 20261115
FLAT_MOD = 15 * 60 + 59


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def buy_fill(bar):
    return _clamp(bar.o + SLIP, bar.l, bar.h)


def sell_fill(bar):
    return _clamp(bar.o - SLIP, bar.l, bar.h)


def stop_fill(bar, stop):
    """Sell stop fired on `bar`: at the stop, or at the open if the bar opened below it, 2 ticks worse."""
    return _clamp(min(stop, bar.o) - SLIP, bar.l, bar.h)


class Sim(object):
    def __init__(self, risk_pct=RISK_PCT, start=START, period=None):
        self.risk_pct, self.balance, self.start = risk_pct, start, start
        self.period = period
        self.trades, self.days, self.skipped = [], [], 0
        self.pos = None

    def _open(self, bar, stop):
        px = buy_fill(bar)
        dist = px - stop
        if dist <= 0:
            self.skipped += 1
            return
        qty = int(self.risk_pct / 100.0 * self.balance / (dist * PV) + 1e-9)
        if qty < 1:
            self.skipped += 1
            return
        self.pos = {"entry_dt": bar.dt, "entry": px, "stop": stop, "qty": qty,
                    "planned": qty * dist * PV, "budget": self.risk_pct / 100.0 * self.balance, "low": px}

    def _close(self, bar, px, reason):
        p = self.pos
        net = (px - p["entry"]) * p["qty"] * PV - COMM * p["qty"]
        self.balance += net
        self.trades.append({"entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
                            "entry": p["entry"], "exit": px, "stop": p["stop"], "qty": p["qty"],
                            "planned_loss": round(p["planned"], 2), "budget": round(p["budget"], 2),
                            "reason": reason, "net": round(net, 2), "balance": round(self.balance, 2),
                            "worst_price": min(p["low"], px)})
        self.pos = None

    def _mark(self, price):
        p = self.pos
        return self.balance + (price - p["entry"]) * p["qty"] * PV - COMM * p["qty"]

    def run(self, market):
        lo, hi = self.period or (market.start, market.end)
        for s in market.sessions:
            if not (lo <= s.date <= hi):
                continue
            day_start, day_low = self.balance, self.balance
            pend_exit = pend_entry = None
            last = len(s.bars) - 1
            for i, bar, st in bd.iter_session_states(market, s.n, LOOKBACK, NOISE_MULT):
                if pend_exit and self.pos:
                    self._close(bar, sell_fill(bar), pend_exit)
                if pend_entry is not None:
                    self._open(bar, pend_entry)
                pend_exit = pend_entry = None
                if self.pos:
                    if bar.l <= self.pos["stop"]:
                        fill = stop_fill(bar, self.pos["stop"])
                        self.pos["low"] = min(self.pos["low"], fill)
                        self._close(bar, fill, "stop")
                        day_low = min(day_low, self.balance)
                        continue
                    self.pos["low"] = min(self.pos["low"], bar.l)
                    day_low = min(day_low, self._mark(bar.l))
                if i == last:
                    if self.pos:
                        self._close(bar, _clamp(bar.c - SLIP, bar.l, bar.h), "session close")
                    day_low = min(day_low, self.balance)
                    continue
                if bar.mod >= FLAT_MOD:
                    if self.pos:
                        pend_exit = "flat 15:59"
                    continue
                if not mk.is_checkpoint(bar.mod) or not st.have_band:
                    continue
                if self.pos:
                    trail = max(st.upper, st.vwap) if st.vwap_cum_vol > 0 else st.upper
                    if bar.c <= trail:
                        pend_exit = "band/VWAP exit"
                elif bar.c > st.upper:
                    pend_entry = st.lower
            if self.pos:
                raise AssertionError("position open after %s" % s.date)
            day_low = min(day_low, self.balance)
            self.days.append({"date": s.date, "start": round(day_start, 2), "end": round(self.balance, 2),
                              "low": round(day_low, 2)})
        return self


def trailing(days, start=START, limit=LIMIT):
    """End-of-day trailing floor. -> dict with the first crossing (or None) and the closest approach."""
    hwm, floor = start, start - limit
    first, closest = None, None
    for d in days:
        room = d["low"] - floor
        if closest is None or room < closest[0]:
            closest = (room, d["date"])
        if first is None and d["low"] <= floor:
            first = d["date"]
        hwm = max(hwm, d["end"])
        floor = hwm - limit
    return {"first_cross": first, "closest_room": round(closest[0], 2), "closest_date": closest[1]}


def shuffled(days, runs=SHUFFLES, seed=SEED, start=START, limit=LIMIT):
    """Reorder whole trading days; count the orders in which the trailing floor is crossed."""
    blocks = [(d["end"] - d["start"], d["low"] - d["start"]) for d in days if d["end"] != d["start"] or d["low"] != d["start"]]
    rng = random.Random(seed)
    crossed, when = 0, []
    for _ in range(runs):
        rng.shuffle(blocks)
        bal, hwm = start, start
        for k, (pnl, low) in enumerate(blocks):
            if bal + low <= hwm - limit:
                crossed += 1
                when.append(k + 1)
                break
            bal += pnl
            hwm = max(hwm, bal)
    when.sort()
    return {"runs": runs, "crossed": crossed, "pct": round(100.0 * crossed / runs, 1),
            "median_trading_days_to_cross": when[len(when) // 2] if when else None, "trade_days": len(blocks)}


def stats(sim):
    tr = sim.trades
    nets = [t["net"] for t in tr]
    wins, losses = [x for x in nets if x > 0], [x for x in nets if x < 0]
    eq = peak = sim.start
    max_dd = 0.0
    streak = worst = 0
    by_year = {}
    for t in tr:
        eq += t["net"]
        peak = max(peak, eq)
        max_dd = max(max_dd, peak - eq)
        streak = streak + 1 if t["net"] < 0 else 0
        worst = max(worst, streak)
        by_year[t["entry_dt"][:4]] = round(by_year.get(t["entry_dt"][:4], 0.0) + t["net"], 2)
    gl = -sum(losses)
    return {"trades": len(tr), "win_pct": round(100.0 * len(wins) / len(tr), 1) if tr else 0.0,
            "net": round(sum(nets), 2), "profit_factor": round(sum(wins) / gl, 3) if gl else None,
            "max_closed_drawdown": round(max_dd, 2), "largest_loss": min(nets) if nets else 0.0,
            "largest_win": max(nets) if nets else 0.0, "longest_losing_run": worst,
            "stop_exits": sum(1 for t in tr if t["reason"] == "stop"), "skipped": sim.skipped,
            "avg_contracts": round(sum(t["qty"] for t in tr) / len(tr), 2) if tr else 0.0,
            "by_year": by_year}


def digest(sim):
    return hashlib.sha256(json.dumps(sim.trades, sort_keys=True).encode()).hexdigest()


def money(x):
    return ("-$" if x < 0 else "$") + "{:,.0f}".format(abs(x))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=DATA)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))
    a = ap.parse_args(argv)
    market = mk.load_market(a.data, session_start=SESSION_START)
    os.makedirs(a.out, exist_ok=True)
    results = {}
    # the seen years first; the unseen years only after; then the whole run for the two branches
    for label, period in (("seen 2021-2024", SEEN), ("unseen 2025-2026", UNSEEN), ("full 2021-2026", None)):
        sim = Sim(period=period).run(market)
        st = stats(sim)
        results[label] = (sim, st)
        print("%-17s trades %4d | win %4.1f%% | net %9s | profit factor %s | worst closed drop %s | "
              "largest loss %s | losing run %d | stops %d | skipped %d | avg MNQ %.2f | sha %s"
              % (label, st["trades"], st["win_pct"], money(st["net"]), st["profit_factor"],
                 money(st["max_closed_drawdown"]), money(st["largest_loss"]), st["longest_losing_run"],
                 st["stop_exits"], st["skipped"], st["avg_contracts"], digest(sim)[:12]))
        print("                  by year: %s" % st["by_year"])
        with open(os.path.join(a.out, label.split()[0] + ".json"), "w") as fh:
            json.dump({"stats": st, "trades": sim.trades, "days": sim.days}, fh, indent=1)
    full_sim, full = results["full 2021-2026"]
    print()
    print("BRANCH A, profit: total %s against a bar of %s (2 x %s) -> %s"
          % (money(full["net"]), money(2 * LIMIT), money(LIMIT), "PASS" if full["net"] >= 2 * LIMIT else "FAIL"))
    tr = trailing(full_sim.days)
    sh = shuffled(full_sim.days)
    print("BRANCH B, survival: limit crossed in the real order: %s | closest room to the floor %s on %s"
          % (tr["first_cross"] or "never", money(tr["closest_room"]), tr["closest_date"]))
    print("                    shuffled order: crossed in %d of %d runs (%.1f%%), median %s trading days in"
          % (sh["crossed"], sh["runs"], sh["pct"], sh["median_trading_days_to_cross"]))
    with open(os.path.join(a.out, "branches.json"), "w") as fh:
        json.dump({"A": {"net": full["net"], "bar": 2 * LIMIT, "pass": full["net"] >= 2 * LIMIT},
                   "B": {"trailing": tr, "shuffled": sh}}, fh, indent=1)


if __name__ == "__main__":
    main()
