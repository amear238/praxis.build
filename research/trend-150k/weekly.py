#!/usr/bin/env python3
"""weekly.py -- version B of the trend plan (research/trend-150k/PLAN.md): multi-week trend-following on daily bars,
all markets at once on one balance. Judges nothing; returns trades and day records.

Inputs. series: {market: [mdata.Adj]} daily bars, back-adjusted; the engine trades the ADJUSTED prices (open,
high, low, close), which keeps every price difference inside a contract and joins contracts at the second-month
gap, i.e. the position is rolled at the gap. rolls: {market: [mdata.Roll]}; each roll a position is held through
(entry day < roll day <= exit day) costs one commission and two slips a contract (closing one contract, opening
the next). specs: {market: {pv, tick, comm, slip_ticks, max_qty}}. A bar's day = ts // one day (integer); its date
the ISO date of ts in UTC.

Settings: lookback L (days), atr_days N, stop_mult k, trail_mult t (None: no trail), risk_pct (of the realised
balance, per trade).

Per date (the union of the markets' dates, ascending), two phases.
 Phase 1, each market with a bar that day, in the order given:
  a. Orders decided at the previous close fill at this bar's open, slip against, kept inside the bar's range:
     an exit first (reason "signal"), then an entry. The entry's stop rests at entry -/+ dist (dist from the
     decision bar).
  b. Stop. long: open <= stop is a gap; else low <= stop (both within a millionth of a tick, _reaches). kind: the stop (the open on a gap) minus slip, not below
     the low; midpoint: halfway between the stop (the open on a gap) and the low, to the tick below; harsh-stops:
     the low. Shorts mirror (high, tick above). Checked on the entry bar too. The stopped market makes no
     decision on this bar.
  c. Still open: best = highest high (long) / lowest low (short) since entry, this bar included.
 Phase 2, each market with a bar that day, same order, at the close:
  signal = sign(adj close - adj close L bars back) (0 when equal); none until the bar has L earlier bars and
  N bars of range. ATR = mean(high - low) of the last N bars, this one included. dist = k * ATR, on the tick
  grid rounded down, at least one tick.
  - Open position, signal opposite: exit at the next open and enter the other side there (a reverse).
  - Open position otherwise: with t set, stop = best -/+ t * dist_of_the_trade, on the grid away from the price,
    moved only toward the price.
  - Flat (and not stopped on this bar), signal not 0: enter at the next open.
  Size at the decision: risk = balance * risk_pct / 100, balance = start + net of every trade closed so far
  (this date's phase 1 included). loss a contract = (dist + slip) * pv + comm. qty = floor(risk / that), at most
  max_qty. qty < 1: skipped ("under one contract"), nothing entered.
 At a market's last bar (phase 2), a position still open closes at that close, no slippage, reason "end", and
 no decision is made. signal: within a millionth of a tick of equal is no signal (_sign). A signal exit's gap
 flag is False (the flag marks stop fills through the open).

Trade: market, side, qty, entry_day, entry, exit_day, exit, stop_initial, dist, planned_cost, reason
("stop" | "signal" | "end"), gap, rolls, net = (exit - entry) * sign * pv * qty - comm * qty
- rolls * (comm + 2 * slip * pv) * qty, to the cent.
Day: {day, date, start, end, low}. end = realised balance + every open position marked at the close, its
commission already deducted; low = realised + every open position marked at
its bar's adverse extreme (a market with no bar that day: its last close) (all at once; conservative), not clamped to start or end. start = the previous day's end.

Standard library only. Run tests with python3 -I -B.
"""
import datetime as _dt
import hashlib
import json
import math

DAY_NS = 86400 * 1_000_000_000
EPS = 1e-9


def _floor_tick(x, tick):
    return math.floor(x / tick + EPS) * tick


def _ceil_tick(x, tick):
    return math.ceil(x / tick - EPS) * tick


def _inside(x, lo, hi):
    return min(max(x, lo), hi)


def _reaches(price, stop, tick, side):
    """A long's stop is reached at or below it, a short's at or above, within a millionth of a tick (float noise
    in back-adjusted prices must not turn a touch into a miss)."""
    return price <= stop + tick * 1e-6 if side == "long" else price >= stop - tick * 1e-6


def _sign(c, c_back, tick):
    d = c - c_back
    return 0 if abs(d) <= tick * 1e-6 else (1 if d > 0 else -1)


class _Pos:
    __slots__ = ("side", "qty", "entry_day", "entry", "stop", "stop_initial", "dist", "planned_cost", "best")


def run(series, specs, settings, fill="midpoint", start=150000.0, rolls=None):
    L, N = settings["lookback"], settings["atr_days"]
    k, t, rp = settings["stop_mult"], settings["trail_mult"], settings["risk_pct"]
    rolls = rolls or {}
    markets = list(series)
    idx = {m: {a.bar.ts // DAY_NS: i for i, a in enumerate(series[m])} for m in markets}
    roll_days = {m: [r.ts // DAY_NS for r in rolls.get(m, [])] for m in markets}
    all_days = sorted(set().union(*[set(idx[m]) for m in markets]))

    realised = start
    pos = {m: None for m in markets}
    pending = {m: None for m in markets}     # (exit: bool, entry: (side, qty, dist, planned_cost) or None)
    trades, skipped, days = [], [], []
    prev_end = start

    def close(m, p, day, px, reason, gap):
        nonlocal realised
        sp = specs[m]
        sign = 1 if p.side == "long" else -1
        n_rolls = sum(1 for rd in roll_days[m] if p.entry_day < rd <= day)
        slip = sp["slip_ticks"] * sp["tick"]
        net = ((px - p.entry) * sign * sp["pv"] * p.qty - sp["comm"] * p.qty
               - n_rolls * (sp["comm"] + 2 * slip * sp["pv"]) * p.qty)
        net = round(net, 2)
        realised = round(realised + net, 2)
        trades.append({"market": m, "side": p.side, "qty": p.qty, "entry_day": p.entry_day, "entry": p.entry,
                       "exit_day": day, "exit": px, "stop_initial": p.stop_initial, "dist": p.dist,
                       "planned_cost": p.planned_cost, "reason": reason, "gap": gap, "rolls": n_rolls,
                       "net": net, "balance": realised})

    for day in all_days:
        stopped = set()
        # phase 1
        for m in markets:
            i = idx[m].get(day)
            if i is None:
                continue
            a, sp = series[m][i], specs[m]
            slip = sp["slip_ticks"] * sp["tick"]
            o, h, l = a.adj_open, a.adj_high, a.adj_low
            if pending[m] is not None:
                do_exit, entry = pending[m]
                pending[m] = None
                p = pos[m]
                if do_exit and p is not None:
                    px = _inside(o - slip if p.side == "long" else o + slip, l, h)
                    close(m, p, day, px, "signal", False)
                    pos[m] = None
                if entry is not None:
                    side, qty, dist, planned = entry
                    p = _Pos()
                    p.side, p.qty, p.dist, p.planned_cost, p.entry_day = side, qty, dist, planned, day
                    p.entry = _inside(o + slip if side == "long" else o - slip, l, h)
                    p.stop = p.stop_initial = p.entry - dist if side == "long" else p.entry + dist
                    p.best = None
                    pos[m] = p
            p = pos[m]
            if p is None:
                continue
            if p.side == "long":
                gap = _reaches(o, p.stop, sp["tick"], "long")
                if gap or _reaches(l, p.stop, sp["tick"], "long"):
                    ref = o if gap else p.stop
                    px = {"kind": max(l, ref - slip), "midpoint": _floor_tick((ref + l) / 2, sp["tick"]),
                          "harsh-stops": l}[fill]
                    close(m, p, day, px, "stop", gap)
                    pos[m] = None
                    stopped.add(m)
                    continue
                p.best = h if p.best is None else max(p.best, h)
            else:
                gap = _reaches(o, p.stop, sp["tick"], "short")
                if gap or _reaches(h, p.stop, sp["tick"], "short"):
                    ref = o if gap else p.stop
                    px = {"kind": min(h, ref + slip), "midpoint": _ceil_tick((ref + h) / 2, sp["tick"]),
                          "harsh-stops": h}[fill]
                    close(m, p, day, px, "stop", gap)
                    pos[m] = None
                    stopped.add(m)
                    continue
                p.best = l if p.best is None else min(p.best, l)
        # phase 2
        for m in markets:
            i = idx[m].get(day)
            if i is None:
                continue
            if i == len(series[m]) - 1:      # the market's last bar: close what is open, decide nothing
                if pos[m] is not None:
                    close(m, pos[m], day, series[m][i].adj_close, "end", False)
                    pos[m] = None
                continue
            if m in stopped or i < L or i < N - 1:
                continue
            s, sp = series[m], specs[m]
            sg = _sign(s[i].adj_close, s[i - L].adj_close, sp["tick"])
            signal = "long" if sg > 0 else "short" if sg < 0 else None
            p = pos[m]
            if p is not None and (signal is None or signal == p.side):
                if t is not None:
                    tr = t * p.dist
                    if p.side == "long":
                        p.stop = max(p.stop, _floor_tick(p.best - tr, sp["tick"]))
                    else:
                        p.stop = min(p.stop, _ceil_tick(p.best + tr, sp["tick"]))
                continue
            if signal is None:
                continue
            atr = sum(x.adj_high - x.adj_low for x in s[i - N + 1:i + 1]) / N
            dist = max(_floor_tick(k * atr, sp["tick"]), sp["tick"])
            slip = sp["slip_ticks"] * sp["tick"]
            lpc = (dist + slip) * sp["pv"] + sp["comm"]
            qty = min(int(math.floor(realised * rp / 100.0 / lpc + EPS)), sp["max_qty"])
            do_exit = p is not None
            if qty < 1:
                skipped.append({"market": m, "day": day, "side": signal, "reason": "under one contract"})
                if do_exit:
                    pending[m] = (True, None)
                continue
            pending[m] = (do_exit, (signal, qty, dist, round(qty * lpc, 2)))
        # day record
        end, low = realised, realised
        for m in markets:
            p = pos[m]
            if p is None:
                continue
            sp = specs[m]
            i = idx[m].get(day)
            no_bar = i is None
            if no_bar:         # no bar for this market today: its last close for both marks
                i = max(j for d, j in idx[m].items() if d < day)
            a = series[m][i]
            sign = 1 if p.side == "long" else -1
            adverse = a.adj_close if no_bar else (a.adj_low if p.side == "long" else a.adj_high)
            end += (a.adj_close - p.entry) * sign * sp["pv"] * p.qty - sp["comm"] * p.qty
            low += (adverse - p.entry) * sign * sp["pv"] * p.qty - sp["comm"] * p.qty
        end, low = round(end, 2), round(low, 2)
        date = _dt.datetime.fromtimestamp(day * 86400, _dt.UTC).date().isoformat()
        days.append({"day": day, "date": date, "start": prev_end, "end": end, "low": low})
        prev_end = end

    if any(p is not None for p in pos.values()):
        raise AssertionError("a position is open after every market's last bar")
    trades.sort(key=lambda x: (x["entry_day"], markets.index(x["market"])))
    digest = hashlib.sha256(json.dumps(trades, sort_keys=True).encode()).hexdigest()
    return {"settings": settings, "fill": fill, "start": start, "trades": trades, "days": days,
            "skipped": skipped, "digest": digest}
