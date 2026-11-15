#!/usr/bin/env python3
"""Candidate 4: Carver's fast mean reversion (Strategy 27, "safer fast mean reversion"), NQ, all hours.

Amear's handoff (pasted 2026-11-15): run Carver's fast mean reversion on the held NQ 1-minute data;
overnight holds allowed; no swing trading; longest hold the end of the next trading day (the voice
agent's default, not his ruling); every trade has a stop-market order at entry; risk per trade a set
percentage of the balance, stop slippage counted in it; Carver's rules as published, any missing or
open rule given one value, named, and never tuned; settings fixed before the first run; 2021-2024
first, 2025-2026 after; overnight stops modelled; whole trades shuffled.

WHERE THE RULES COME FROM. Carver, Advanced Futures Trading Strategies (2023), Part Four. The book is
not in the repo and no source read reproduces its text. The rule-level source is a third-party
replication (github.com/dgarciagud/Forex, docs/carver_estrategias.md and src/carver_s27.py), which
states: equilibrium = EWMA span 5 of daily closes, last close t-1; raw = (equilibrium - price) /
daily price volatility; Strategy 26 forecast = 9.3 x raw capped at +-20; Strategy 27 adds the trend
filter EWMAC(16,64) on daily closes (the forecast is set to 0 when the trend's sign differs) and uses a
forecast scalar of about 20; volatility = 0.7 x EWMA span 32 of daily returns + 0.3 x its long-run
average. Carver's own execution is a ladder of limit orders around the equilibrium with a position that
grows and shrinks with the forecast; there is no stop.

WHAT HAD TO BE ADDED OR CHOSEN (one value each, chosen before any run, never tuned):
  A1 one trade at a time, fixed risk. Amear's rules need a single trade with a stop-market and a set
     cost, so Carver's sliding position becomes: enter when |forecast| reaches 10 (Carver scales every
     forecast so that its average size is 10), exit when the forecast is back to 0 or has the other
     sign (price back at the equilibrium, or the trend filter has turned off).
  A2 stop-market at entry, 0.5 x the daily price volatility from the fill, rounded up to a tick. At the
     entry threshold (raw 0.5) this sits where Carver's forecast reaches its cap of 20 (raw 1.0).
  A3 longest hold: flat at the close of the next trading day's session (the voice agent's default).
     A Friday entry is therefore held over the weekend into Monday.
  A4 market orders, filled at the next 1-minute bar's open with 2 ticks of slippage, instead of
     Carver's limit ladder (limit fills cannot be checked honestly on 1-minute bars).
  A5 volatility in points: EWMA span 32 of squared daily close-to-close changes, square-rooted (the
     same as % volatility x price, without the distortion of the back-adjusted price level); the
     long-run average is the average of that series over all history so far (Carver: 10 years; the
     data holds about 5).
  A6 the volatility attenuation that the replication lists is left out: it cannot be confirmed as part
     of Strategy 27, and its percentile needs more history than the data holds.
  A7 forecast scalar 20 (Strategy 27, per the replication).

LOCKED SETTINGS:
  data          NQ continuous 1-minute, all hours, stamped at the minute's end in New York time. A
                trading day runs 18:01 to 17:00; bars after 17:00 Sunday to Thursday belong to the next
                weekday. Bars dated Saturday, Sunday up to 17:00, or Friday after 17:00 are dropped and
                counted. Data 2021-03-07 to 2026-07-17 (the last full session).
  daily close   the close of the 16:00 bar (the last bar at or before 16:00 if there is none)
  equilibrium   EWMA span 5 of daily closes through the previous trading day (adjust=False)
  trend         sign of EWMA span 16 minus EWMA span 64 of daily closes through the previous trading day
  volatility    see A5, through the previous trading day
  forecast      F = clamp(20 x (equilibrium - price) / volatility, -20, 20), set to 0 if its sign differs
                from the trend's; evaluated at every hourly close (bars stamped hh:00) except the
                session's last bar, price = that bar's close
  entry         flat and F >= 10: buy; flat and F <= -10: sell short; filled at the next bar's open
  exit          long and F <= 0, or short and F >= 0: market at the next bar's open; the stop at any bar,
                overnight included (at the stop, or at the open if the bar opened through it, 2 ticks
                worse); flat at the close of the next trading day (A3); a trade still open on the
                data's last bar is closed there ("end of data")
  size          MNQ ($2 a point) = floor(1% of balance / ((stop distance + 2 ticks) x $2 + $1.90));
                fewer than one -> skipped and counted
  costs         2 ticks on every fill, $1.90 commission per contract round trip
  warm-up       no trade in the first 65 trading days (64 daily closes for the trend filter)
  account       $50,000 start, $2,000 end-of-day trailing limit (stand-ins); the end-of-day balance
                includes the open trade marked at the session's last close
  shuffle       10,000 reorderings of whole trades, seed 20261115; each trade keeps its day-by-day low
                and end-of-day marks so the trailing floor moves as it would live
  periods       entries 2021-2024 first; entries 2025-2026 only after

Standard library only. Run: python3 -I -B research/fast-mean-reversion/fmr.py
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "research", "orb-5min"))
import orb as O   # noqa: E402  fills; through it candidate 1's constants, stats, trailing rule

R, V = O.R, O.V
DATA = R.DATA
LAST_DAY = "2026-07-17"
EQ_SPAN, FAST, SLOW, VOL_SPAN = 5, 16, 64, 32
SCALAR, CAP, ENTER = 20.0, 20.0, 10.0
STOP_VOL = 0.5
WARMUP = 65
RISK_PCT = 1.0
DAY_END, CLOSE_HMS = 17 * 3600, 16 * 3600


class Bar(object):
    __slots__ = ("dt", "sec", "o", "h", "l", "c", "v")

    def __init__(self, t, sec, o, h, l, c, v):
        self.dt, self.sec, self.o, self.h, self.l, self.c, self.v = t, sec, o, h, l, c, v


class Day(object):
    def __init__(self, date):
        self.date, self.bars, self.close = date, [], None


def session_date(t):
    """Trading day of a bar stamped t, or None if the bar is dropped."""
    sec = t.hour * 3600 + t.minute * 60 + t.second
    wd = t.weekday()   # Mon 0 .. Sun 6
    if sec > DAY_END:
        if wd in (4, 5):   # Friday or Saturday evening
            return None
        nxt = t.date() + dt.timedelta(days=1)
        return nxt
    if wd >= 5:
        return None
    return t.date()


def load(path=DATA, last_day=LAST_DAY):
    days, dropped = {}, 0
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            stamp, o, h, l, c, v = line.split(";")
            t = dt.datetime(int(stamp[0:4]), int(stamp[4:6]), int(stamp[6:8]),
                            int(stamp[9:11]), int(stamp[11:13]), int(stamp[13:15]))
            d = session_date(t)
            if d is None:
                dropped += 1
                continue
            ds = d.isoformat()
            if ds > last_day:
                continue
            if ds not in days:
                days[ds] = Day(ds)
            days[ds].bars.append(Bar(t, t.hour * 3600 + t.minute * 60 + t.second,
                                     float(o), float(h), float(l), float(c), int(v)))
    out = []
    for ds in sorted(days):
        day = days[ds]
        day.bars.sort(key=lambda b: b.dt)
        upto = [b for b in day.bars if b.dt.date().isoformat() == ds and b.sec <= CLOSE_HMS]
        day.close = upto[-1].c if upto else day.bars[-1].c
        out.append(day)
    return out, dropped


def ewma(xs, span):
    a, out, e = 2.0 / (span + 1.0), [], None
    for x in xs:
        e = x if e is None else a * x + (1.0 - a) * e
        out.append(e)
    return out


def daily_inputs(days):
    """For day k: (equilibrium, trend sign, volatility in points), all from closes through day k-1.
    Day 0 and day 1 have no inputs (None)."""
    closes = [d.close for d in days]
    eq, fast, slow = ewma(closes, EQ_SPAN), ewma(closes, FAST), ewma(closes, SLOW)
    diffs = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    var = ewma([x * x for x in diffs], VOL_SPAN)
    vol_now = [math.sqrt(v) for v in var]          # vol_now[j] is through close j+1
    blended, run = [], 0.0
    for j, v in enumerate(vol_now):
        run += v
        blended.append(0.7 * v + 0.3 * run / (j + 1))
    inputs = [None, None]
    for k in range(2, len(days)):
        j = k - 1   # inputs from closes through day k-1
        tr = fast[j] - slow[j]
        inputs.append((eq[j], 1 if tr > 0 else -1 if tr < 0 else 0, blended[j - 1]))
    return inputs


def forecast(eq, trend, vol, price):
    f = SCALAR * (eq - price) / vol
    f = max(-CAP, min(CAP, f))
    if (f > 0 and trend != 1) or (f < 0 and trend != -1):
        return 0.0
    return f


def stop_distance(vol):
    return math.ceil(STOP_VOL * vol / R.TICK - 1e-9) * R.TICK


def size(balance, dist, risk_pct=RISK_PCT):
    per = (dist + R.SLIP) * R.PV + R.COMM
    return int(risk_pct / 100.0 * balance / per + 1e-9), per


def is_hour_close(bar, last):
    return bar.sec % 3600 == 0 and not last


class Sim(object):
    def __init__(self, risk_pct=RISK_PCT, start=R.START, period=None):
        self.risk_pct, self.balance, self.start, self.period = risk_pct, start, start, period
        self.trades, self.days = [], []
        self.skipped = 0
        self.pos = None

    def _mark(self, price):
        p = self.pos
        return self.balance + (price - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]

    def _open(self, bar, side, vol, k, f):
        px = O.entry_fill(bar, side)
        dist = stop_distance(vol)
        qty, per = size(self.balance, dist, self.risk_pct)
        if qty < 1:
            self.skipped += 1
            return
        self.pos = {"entry_dt": bar.dt, "side": side, "entry": px, "stop": px - side * dist, "dist": dist,
                    "qty": qty, "planned": qty * per, "budget": self.risk_pct / 100.0 * self.balance,
                    "day_k": k, "f": round(f, 4), "b0": self.balance, "segs": [], "seg_low": self.balance}

    def _close(self, bar, px, reason):
        p = self.pos
        net = (px - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]
        self.balance += net
        p["seg_low"] = min(p["seg_low"], self.balance)
        p["segs"].append((round(p["seg_low"] - p["b0"], 2), round(net, 2)))
        self.trades.append({"entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
                            "side": p["side"], "entry": p["entry"], "exit": px, "stop": p["stop"],
                            "dist": p["dist"], "qty": p["qty"], "planned_loss": round(p["planned"], 2),
                            "budget": round(p["budget"], 2), "reason": reason, "net": round(net, 2),
                            "balance": round(self.balance, 2), "f_at_signal": p["f"],
                            "hours": round((bar.dt - p["entry_dt"]).total_seconds() / 3600.0, 2),
                            "segs": p["segs"]})
        self.pos = None

    def run(self, days):
        inputs = daily_inputs(days)
        lo, hi = self.period or (days[0].date, days[-1].date)
        for k, day in enumerate(days):
            entries_ok = k >= WARMUP and lo <= day.date <= hi and inputs[k] is not None
            if not entries_ok and self.pos is None and day.date > hi:
                break
            carried = self.pos is not None
            day_start = day_low = self.balance if self.pos is None else self._mark(day.bars[0].o)
            if self.pos:
                day_start = self.days[-1]["end"] if self.days else self.balance
            pend = None
            last = len(day.bars) - 1
            for i, bar in enumerate(day.bars):
                if pend is not None:
                    kind, side, f = pend
                    pend = None
                    if kind == "exit" and self.pos:
                        self._close(bar, O.exit_fill(bar, self.pos["side"]), "back to equilibrium")
                        day_low = min(day_low, self.balance)
                    elif kind == "entry" and self.pos is None:
                        self._open(bar, side, inputs[k][2], k, f)
                if self.pos:
                    p = self.pos
                    if O.stop_hit(bar, p["side"], p["stop"]):
                        fill = O.stop_fill(bar, p["side"], p["stop"])
                        p["seg_low"] = min(p["seg_low"], self._mark(fill))
                        self._close(bar, fill, "stop")
                        day_low = min(day_low, self.balance)
                    else:
                        m = self._mark(bar.l if p["side"] == 1 else bar.h)
                        p["seg_low"] = min(p["seg_low"], m)
                        day_low = min(day_low, m)
                        if i == last and (k >= p["day_k"] + 1 or k == len(days) - 1):
                            why = "next-day close" if k >= p["day_k"] + 1 else "end of data"
                            self._close(bar, O._clamp(bar.c - p["side"] * R.SLIP, bar.l, bar.h), why)
                            day_low = min(day_low, self.balance)
                if inputs[k] is None or not is_hour_close(bar, i == last):
                    continue
                eq, trend, vol = inputs[k]
                f = forecast(eq, trend, vol, bar.c)
                if self.pos:
                    if f * self.pos["side"] <= 0:
                        pend = ("exit", 0, f)
                elif entries_ok and abs(f) >= ENTER:
                    pend = ("entry", 1 if f > 0 else -1, f)
            end = self.balance
            if self.pos:
                p = self.pos
                end = self._mark(day.bars[-1].c)
                p["segs"].append((round(p["seg_low"] - p["b0"], 2), round(end - p["b0"], 2)))
                p["seg_low"] = end
            day_low = min(day_low, end, self.balance)
            self.days.append({"date": day.date, "start": round(day_start, 2), "end": round(end, 2),
                              "low": round(day_low, 2), "carried": carried})
        if self.pos:
            raise AssertionError("position open at the end of the data")
        return self


def shuffle_trades(trades, runs=R.SHUFFLES, seed=R.SEED, start=R.START, limit=R.LIMIT):
    """Reorder whole trades. Each trade replays its day-by-day (low, end-of-day mark) segments against
    the end-of-day trailing floor. -> crossing count and the drop reached in the worst 5% of orders."""
    blocks = [t["segs"] for t in trades]
    rng = random.Random(seed)
    crossed, depths = 0, []
    for _ in range(runs):
        rng.shuffle(blocks)
        bal = hwm = start
        hit, deep = False, 0.0
        for segs in blocks:
            for low, eod in segs:
                if not hit and bal + low <= hwm - limit:
                    hit = True
                deep = max(deep, hwm - (bal + low))
                hwm = max(hwm, bal + eod)
            bal += segs[-1][1]
        crossed += hit
        depths.append(deep)
    depths.sort()
    return {"runs": runs, "crossed": crossed, "pct": round(100.0 * crossed / runs, 1),
            "worst_5pct_drop": round(depths[int(0.95 * runs) - 1], 2), "trades": len(blocks)}


def summarise(sim, years):
    st = R.stats(sim)
    tr = sim.trades
    st["shorts"] = sum(1 for t in tr if t["side"] == -1)
    st["per_year_pct"] = round(V.per_year(sim.start, sim.balance, years), 1)
    st["by_reason"] = {r: sum(1 for t in tr if t["reason"] == r) for r in sorted({t["reason"] for t in tr})}
    hrs = sorted(t["hours"] for t in tr)
    st["median_hours"] = hrs[len(hrs) // 2] if hrs else None
    st["held_overnight"] = sum(1 for t in tr if t["entry_dt"][:10] != t["exit_dt"][:10] or t["hours"] >= 23)
    st["avg_stop_points"] = round(sum(t["dist"] for t in tr) / len(tr), 2) if tr else None
    return st


def digest(sim):
    keys = ("entry_dt", "exit_dt", "side", "entry", "exit", "stop", "qty", "reason", "net", "balance")
    return hashlib.sha256(json.dumps([[t[k] for k in keys] for t in sim.trades]).encode()).hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=DATA)
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--seen-only", action="store_true")
    a = ap.parse_args(argv)
    days, dropped = load(a.data)
    print("trading days %d (%s to %s), bars dropped %d" % (len(days), days[0].date, days[-1].date, dropped))
    os.makedirs(a.out, exist_ok=True)
    yrs = {"seen": V.years_between(*R.SEEN), "unseen": V.years_between(R.UNSEEN[0], LAST_DAY),
           "full": V.years_between(days[0].date, LAST_DAY)}
    plan = (("seen", R.SEEN),) if a.seen_only else (("seen", R.SEEN), ("unseen", (R.UNSEEN[0], LAST_DAY)), ("full", None))
    results = {}
    for label, period in plan:
        sim = Sim(period=period).run(days)
        st = summarise(sim, yrs[label])
        results[label] = (sim, st)
        print("%-6s trades %4d (shorts %d) | win %4.1f%% | net %9s | %.1f%% a year | PF %s | worst closed drop %s | "
              "largest loss %s | losing run %d | skipped %d | exits %s | median hold %s h | overnight %d | "
              "avg stop %s pts | avg MNQ %.2f | sha %s"
              % (label, st["trades"], st["shorts"], st["win_pct"], R.money(st["net"]), st["per_year_pct"],
                 st["profit_factor"], R.money(st["max_closed_drawdown"]), R.money(st["largest_loss"]),
                 st["longest_losing_run"], st["skipped"], st["by_reason"], st["median_hours"],
                 st["held_overnight"], st["avg_stop_points"], st["avg_contracts"], digest(sim)[:12]))
        print("       by year: %s" % st["by_year"])
        if not a.seen_only:
            with open(os.path.join(a.out, label + ".json"), "w") as fh:
                json.dump({"stats": st, "trades": sim.trades, "days": sim.days}, fh, indent=1)
    if a.seen_only:
        return
    full_sim, full = results["full"]
    tr = R.trailing(full_sim.days)
    sh = shuffle_trades(full_sim.trades)
    headroom = round(full["net"] / sh["worst_5pct_drop"], 2) if sh["worst_5pct_drop"] > 0 else None
    a_pass, b_pass = full["net"] >= 2 * R.LIMIT, sh["pct"] <= 5.0
    print()
    print("PROFIT   total %s against a bar of %s -> %s | %.1f%% a year | skipped %d | unseen years %s"
          % (R.money(full["net"]), R.money(2 * R.LIMIT), "PASS" if a_pass else "FAIL", full["per_year_pct"],
             full["skipped"], R.money(results["unseen"][1]["net"])))
    print("SURVIVAL real order: crossed %s, closest room %s on %s | whole-trade shuffles: crossed in %d of %d (%.1f%%) vs 5%% -> %s"
          % (tr["first_cross"] or "never", R.money(tr["closest_room"]), tr["closest_date"], sh["crossed"],
             sh["runs"], sh["pct"], "PASS" if b_pass else "FAIL"))
    print("HEADROOM profit %s / worst-5%%-of-shuffles drop %s = %s (both bars together need 2 or more)"
          % (R.money(full["net"]), R.money(sh["worst_5pct_drop"]), headroom))
    with open(os.path.join(a.out, "branches.json"), "w") as fh:
        json.dump({"A": {"net": full["net"], "bar": 2 * R.LIMIT, "pass": a_pass, "per_year_pct": full["per_year_pct"],
                         "skipped": full["skipped"], "unseen_net": results["unseen"][1]["net"]},
                   "B": {"trailing": tr, "shuffled": sh, "pass": b_pass},
                   "headroom": headroom, "dropped_bars": dropped}, fh, indent=1)


if __name__ == "__main__":
    main()
