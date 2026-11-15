#!/usr/bin/env python3
"""Noise-Area breakout retest with a real stop-market order placed at entry.

Fast Python screen on the Mac, 1-minute bars. NinjaTrader confirms only a finalist.

The strategy rule (same as ninjascript/PraxisNoiseAreaBreakout*.cs, as documented in
scripts/wf/oracle/policy.py), decided on the close of each bar, orders filled on the next bar:
  1. Session flat. On the session's last bar the position is closed at that bar's close.
     Under Flat1559, on a bar stamped 15:59 or later the position is closed at the next bar's open.
     Nothing else happens on such a bar.
  2. Checkpoints are the bars stamped :00 and :30, after 09:30 and before 16:00, when a band exists.
     Long exit:  close <= max(upper band, session VWAP)   (OppBand: close <= lower band)
     Short exit: close >= min(lower band, session VWAP)   (OppBand: close >= upper band)
     Entry: close > upper band and not long -> buy; else close < lower band and not short -> sell.
     "Long"/"short" is the position before this bar's exit, so a long reverses only below the lower band.

Added here (Amear's rules, RULINGS.md): every entry carries a stop-market order from the moment it
fills. The stop distance is set so the price loss at the stop is a set percentage of the CURRENT
account balance, at a fixed number of contracts. A bar on which the stop fires does nothing else.

Two fill models, because 1-minute bars cannot show the path inside a minute:
  kind  : market orders fill at the next bar's open, 2 ticks against; the stop fills at its level
          (or at the bar's open if the bar opens beyond it), 2 ticks against.
  harsh-stops : market orders as in kind; the stop fills at the worst price of the minute in
          which it fires. Market orders here go in at fixed clock times, not into a fast move,
          so this is the realistic pessimistic case.
  harsh : every market order ALSO fills at the worst price of its fill minute. An outer bound
          only: it charges the full one-minute range on every entry and exit.
--slip-sweep reruns the kind model with more slippage per side, to find where the profit ends.

Standard library only. Run: python3 -I -B research/noise-area-stop/retest.py
"""
import argparse
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, "scripts", "wf", "oracle"))
import market as mk   # noqa: E402
import band as bd     # noqa: E402

DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")
TICK = 0.25
SLIP = 0.5            # 2 ticks
LOOKBACK, NOISE_MULT = 14, 1.0
INSTRUMENTS = {"NQ": (20.0, 2.96), "MNQ": (2.0, 1.90)}   # point value, commission per round trip


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def fill_market(bar, buy, model, slip=SLIP):
    """Fill of a market order on `bar`."""
    if model == "harsh":
        return bar.h if buy else bar.l
    return _clamp(bar.o + slip if buy else bar.o - slip, bar.l, bar.h)


def fill_close(bar, buy, slip=SLIP):
    """Exit at the close of the session's last bar (no next bar exists)."""
    return _clamp(bar.c + slip if buy else bar.c - slip, bar.l, bar.h)


def stop_hit(bar, side, stop):
    return bar.l <= stop if side == 1 else bar.h >= stop


def fill_stop(bar, side, stop, model, slip=SLIP):
    """Fill of a stop-market order that fires on `bar`. side: +1 long (sell stop), -1 short (buy stop)."""
    if model in ("harsh", "harsh-stops"):
        return bar.l if side == 1 else bar.h
    if side == 1:
        return _clamp(min(stop, bar.o) - slip, bar.l, bar.h)
    return _clamp(max(stop, bar.o) + slip, bar.l, bar.h)


def floor_tick(x):
    return int(x / TICK + 1e-9) * TICK


class Sim(object):
    def __init__(self, policy="Flat1559", risk_pct=None, model="kind", instrument="MNQ", qty=1,
                 start_balance=10000.0, lookback=LOOKBACK, noise_mult=NOISE_MULT, slip=SLIP):
        mk.check_policy(policy)
        if model not in ("kind", "harsh-stops", "harsh"):
            raise ValueError(model)
        self.slip = slip
        self.policy, self.risk_pct, self.model, self.qty = policy, risk_pct, model, qty
        self.pv, self.comm = INSTRUMENTS[instrument]
        self.instrument = instrument
        self.balance = start_balance
        self.start_balance = start_balance
        self.lookback, self.noise_mult = lookback, noise_mult
        self.trades = []
        self.skipped = 0
        self.pos = None       # dict while a position is open

    # --- position bookkeeping -------------------------------------------------------------
    def _open(self, bar, side):
        px = fill_market(bar, side == 1, self.model, self.slip)
        stop = planned = None
        if self.risk_pct is not None:
            planned = self.risk_pct / 100.0 * self.balance
            dist = floor_tick(planned / (self.pv * self.qty))
            if dist < TICK:
                self.skipped += 1
                return
            stop = px - dist if side == 1 else px + dist
        self.pos = {"side": side, "entry_dt": bar.dt, "entry": px, "stop": stop, "planned": planned,
                    "balance_at_entry": self.balance}

    def _close(self, bar, px, reason):
        p = self.pos
        pts = (px - p["entry"]) * p["side"]
        net = pts * self.pv * self.qty - self.comm * self.qty
        self.balance += net
        self.trades.append({
            "entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
            "side": "Long" if p["side"] == 1 else "Short", "entry": p["entry"], "exit": px,
            "stop": p["stop"], "planned_cost": p["planned"], "reason": reason, "points": pts,
            "net": round(net, 2), "balance": round(self.balance, 2)})
        self.pos = None

    # --- the run --------------------------------------------------------------------------
    def run(self, market):
        opp = self.policy == "OppBand"
        flat_mod = mk.session_flat_mods(self.policy)
        for s in market.sessions:
            pend_exit = pend_entry = None          # orders decided on the previous bar
            last = len(s.bars) - 1
            for i, bar, st in bd.iter_session_states(market, s.n, self.lookback, self.noise_mult):
                # orders from the previous bar's close fill on this bar
                if pend_exit and self.pos:
                    self._close(bar, fill_market(bar, self.pos["side"] == -1, self.model, self.slip), pend_exit)
                if pend_entry:
                    self._open(bar, pend_entry)
                pend_exit = pend_entry = None
                # the resting stop, live from the entry fill onward
                if self.pos and self.pos["stop"] is not None and stop_hit(bar, self.pos["side"], self.pos["stop"]):
                    self._close(bar, fill_stop(bar, self.pos["side"], self.pos["stop"], self.model, self.slip), "stop")
                    continue
                # 1. session flat
                if i == last:
                    if self.pos:
                        self._close(bar, fill_close(bar, self.pos["side"] == -1, self.slip), "session close")
                    continue
                if bar.mod >= flat_mod:
                    if self.pos:
                        pend_exit = "flat 15:59"
                    continue
                # 2. checkpoint
                if not mk.is_checkpoint(bar.mod) or not st.have_band:
                    continue
                price = bar.c
                side = self.pos["side"] if self.pos else 0
                if side == 1:
                    trail = st.lower if opp else (max(st.upper, st.vwap) if st.vwap_cum_vol > 0 else st.upper)
                    if price <= trail:
                        pend_exit = "band/VWAP exit"
                elif side == -1:
                    trail = st.upper if opp else (min(st.lower, st.vwap) if st.vwap_cum_vol > 0 else st.lower)
                    if price >= trail:
                        pend_exit = "band/VWAP exit"
                if price > st.upper and side != 1:
                    pend_entry = 1
                    if side == -1:
                        pend_exit = pend_exit or "reverse"
                elif price < st.lower and side != -1:
                    pend_entry = -1
                    if side == 1:
                        pend_exit = pend_exit or "reverse"
            if self.pos:   # cannot happen: the last bar closes any position
                raise AssertionError("position open after session %s" % s.date)
        return self


def stats(sim):
    tr = sim.trades
    nets = [t["net"] for t in tr]
    wins = [x for x in nets if x > 0]
    losses = [x for x in nets if x < 0]
    eq = peak = sim.start_balance
    max_dd = max_dd_pct = 0.0
    streak = worst_streak = 0
    by_year = {}
    for t in tr:
        eq += t["net"]
        peak = max(peak, eq)
        dd = peak - eq
        if dd > max_dd:
            max_dd = dd
        if peak > 0 and dd / peak > max_dd_pct:
            max_dd_pct = dd / peak
        streak = streak + 1 if t["net"] < 0 else 0
        worst_streak = max(worst_streak, streak)
        y = t["entry_dt"][:4]
        by_year[y] = round(by_year.get(y, 0.0) + t["net"], 2)
    stops = [t for t in tr if t["reason"] == "stop"]
    over = [t for t in tr if t["planned_cost"] is not None and -t["net"] > t["planned_cost"] + 1e-9]
    worst_over = max((-t["net"] / t["planned_cost"] for t in over), default=0.0)
    gp, gl = sum(wins), -sum(losses)
    return {
        "trades": len(tr), "win_pct": round(100.0 * len(wins) / len(tr), 1) if tr else 0.0,
        "net": round(sum(nets), 2), "end_balance": round(sim.balance, 2),
        "profit_factor": round(gp / gl, 3) if gl else None,
        "max_drawdown": round(max_dd, 2), "max_drawdown_pct": round(100 * max_dd_pct, 1),
        "largest_loss": round(min(nets), 2) if nets else 0.0,
        "largest_win": round(max(nets), 2) if nets else 0.0,
        "longest_losing_run": worst_streak, "stop_exits": len(stops),
        "losses_above_planned_cost": len(over), "worst_loss_vs_planned": round(worst_over, 2),
        "skipped_entries": sim.skipped, "by_year": by_year}


def digest(sim):
    return hashlib.sha256(json.dumps(sim.trades, sort_keys=True).encode()).hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=DATA)
    ap.add_argument("--session-start", default="09:31", choices=sorted(mk.SESSION_STARTS))
    ap.add_argument("--policy", default="Flat1559", choices=mk.POLICIES)
    ap.add_argument("--risk", default="none,0.5,1,2", help="comma list of risk %% of balance; 'none' = no stop")
    ap.add_argument("--slip-sweep", default=None, help="comma list of points of slippage per side, e.g. 0.5,1,2,3,4")
    ap.add_argument("--out", default=None, help="directory for trade lists (json)")
    a = ap.parse_args(argv)
    market = mk.load_market(a.data, session_start=a.session_start)
    print("data %s | sessions %d | %s to %s | session start %s | %s | 1 MNQ | start $10,000"
          % (os.path.basename(a.data), len(market.sessions), market.start, market.end, a.session_start, a.policy))
    cols = ("trades", "win_pct", "net", "profit_factor", "max_drawdown", "max_drawdown_pct", "largest_loss",
            "longest_losing_run", "stop_exits", "losses_above_planned_cost", "worst_loss_vs_planned")
    print("%-10s %-11s " % ("stop", "fills") + " ".join("%s" % c for c in cols))
    for r in a.risk.split(","):
        risk = None if r == "none" else float(r)
        for model in ("kind", "harsh-stops", "harsh"):
            if risk is None and model == "harsh-stops":
                continue
            sim = Sim(policy=a.policy, risk_pct=risk, model=model).run(market)
            st = stats(sim)
            print("%-10s %-11s " % ("none" if risk is None else "%g%%" % risk, model)
                  + " | ".join(str(st[c]) for c in cols))
            print("           by year: %s | sha %s" % (st["by_year"], digest(sim)[:12]))
            if a.out:
                os.makedirs(a.out, exist_ok=True)
                name = "%s-%s-%s-%s.json" % (a.policy, a.session_start.replace(":", ""), r, model)
                with open(os.path.join(a.out, name), "w") as fh:
                    json.dump({"stats": st, "trades": sim.trades}, fh, indent=1)
    if a.slip_sweep:
        print("slippage sweep, 1% stop: points per side -> kind fills | harsh-stops fills (net, profit factor, max drawdown %)")
        for x in a.slip_sweep.split(","):
            row = []
            for model in ("kind", "harsh-stops"):
                st = stats(Sim(policy=a.policy, risk_pct=1.0, model=model, slip=float(x)).run(market))
                row.append("%10.2f  %5.3f  %5.1f%%" % (st["net"], st["profit_factor"], st["max_drawdown_pct"]))
            print("  %4s pt -> %s | %s" % (x, row[0], row[1]))


if __name__ == "__main__":
    main()
