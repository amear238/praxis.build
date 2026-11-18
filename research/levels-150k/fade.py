#!/usr/bin/env python3
"""fade.py -- candidate 1 of research/levels-150k/PLAN.md: fade the first touch of a marked level. Arms the
levels levels.py draws, simulates the resting orders minute by minute, and sizes the trades on one account.
Judges nothing.

arm(day, kind, k, tick) -> [{"kind", "side", "level", "stop", "dist"}] armed at 9:30 (kind "ALL": every kind).
  d = k x ATR rounded down to the tick, at least one tick. Not armed: no ATR; |level - P0| <= d; |level - P0| >
  2 x ATR; a demand zone above P0 or a supply zone below. Each side nearest P0 first (ties: the order of
  levels.KINDS, then the lower price); a level within d of one taken is dropped. Stop: a line d beyond the
  level, a zone d beyond its far edge; dist = |level - stop|.

per_contract(mk, settings, fill, dates=None) -> {"trades": [...], "armed": {date: [...]}} at one contract.
  settings: {"kind", "k", "target" (3 | 5 | None), ...}. fill: "midpoint" | "kind" | "harsh-stops".
  dates: a set of ISO dates to run (None: every trading date).
  Each minute of S(D) from the first at or after 9:30:
  - flat (no position): a minute stamped before 15:00 whose low is at least one tick below an armed long level
    (high one tick above a short's) trades through it. Of the levels traded through, the one nearest the
    minute's open fills (ties as in arm), at the level exactly; the others are spent. The stop is checked on
    the entry minute; the target is not.
  - in a position, in order: (1) a minute stamped at or after 15:55 closes at its open, one slippage against,
    inside the minute (reason "flat"); (2) the stop: long, open <= stop is a gap (reference the open), else
    low <= stop (reference the stop); kind = reference - slip, not below the low; midpoint = halfway between
    the reference and the low, rounded down to the tick; harsh = the low (shorts mirror); (3) the target (not
    on the entry minute): high >= target + one tick, filled at the target. A level traded through while the
    position is open, or on its exit minute, is spent. When S(D)'s minutes end with the position open, it
    closes at the last minute's close, no slippage (reason "flat"), checked after the stop and the target.
  worst = the lowest (adverse extreme - entry) x side over the minutes from the entry minute to the exit
  minute; a flat exit's minute counts only at its fill.

account(per_contract_by_market, specs, risk_pct, start) -> {"start", "trades", "skipped", "days", "digest"}.
  Dates ascending, markets in specs order, trades by entry_ts. Every trade of a date is sized from the realised
  balance at the start of that date: risk = balance x risk_pct / 100; loss a contract = (dist + slip) x pv +
  comm; qty = floor(risk / that), at most max_qty; under one contract: skipped. planned_cost = qty x loss a
  contract; net = (exit - entry) x side x pv x qty - comm x qty; both to the cent. Day {date, start, end, low}
  for each date with a trade: low = start + the sum of (worst x pv - comm) x qty, never above min(start, end).

Standard library only. Run tests with python3 -I -B.
"""
import hashlib
import json
import math

import levels as lv_mod

EPS_T = 1e-6           # in ticks
KIND_ORDER = {k: n for n, k in enumerate(lv_mod.KINDS)}


def _floor_tick(x, tick):
    return math.floor(x / tick + EPS_T) * tick


def _ceil_tick(x, tick):
    return math.ceil(x / tick - EPS_T) * tick


def _rt(x, tick):
    return round(x / tick) * tick


def arm(day, kind, k, tick):
    if day.atr is None or day.p0 is None:
        return []
    eps = tick * EPS_T
    d = max(_floor_tick(k * day.atr, tick), tick)
    kinds = lv_mod.KINDS if kind == "ALL" else (kind,)
    sides = {1: [], -1: []}
    for kd in kinds:
        for lv in day.levels.get(kd) or []:
            gap = abs(lv.price - day.p0)
            if gap <= d + eps or gap > 2 * day.atr + eps:
                continue
            side = 1 if lv.price < day.p0 else -1
            if (lv.role == "demand" and side != 1) or (lv.role == "supply" and side != -1):
                continue
            sides[side].append(lv)
    out = []
    for side, cands in sides.items():
        cands.sort(key=lambda x: (abs(x.price - day.p0), KIND_ORDER[x.kind], x.price))
        taken = []
        for lv in cands:
            if any(abs(lv.price - t.price) <= d + eps for t in taken):
                continue
            taken.append(lv)
        for lv in taken:
            edge = lv.far if lv.role in ("demand", "supply") else lv.price
            stop = _rt(edge - side * d, tick)
            out.append({"kind": lv.kind, "side": side, "level": lv.price, "stop": stop,
                        "dist": _rt(abs(lv.price - stop), tick)})
    return out


def _through(b, a, tick, eps):
    return b.low <= a["level"] - tick + eps if a["side"] == 1 else b.high >= a["level"] + tick - eps


def _stop_fill(b, stop, side, slip, tick, fill, eps):
    """-> (price, gap) or None when the minute does not reach the stop."""
    if side == 1:
        if b.open <= stop + eps:
            ref, gap = b.open, True
        elif b.low <= stop + eps:
            ref, gap = stop, False
        else:
            return None
        if fill == "kind":
            return max(ref - slip, b.low), gap
        if fill == "midpoint":
            return _floor_tick((ref + b.low) / 2.0, tick), gap
        return b.low, gap
    if b.open >= stop - eps:
        ref, gap = b.open, True
    elif b.high >= stop - eps:
        ref, gap = stop, False
    else:
        return None
    if fill == "kind":
        return min(ref + slip, b.high), gap
    if fill == "midpoint":
        return _ceil_tick((ref + b.high) / 2.0, tick), gap
    return b.high, gap


def _sim_day(mk, day, armed, settings, fill, spec, market):
    m, mod = mk.minutes, mk.mod
    tick = spec["tick"]
    eps = tick * EPS_T
    slip = spec["slip_ticks"] * tick
    tgt_mult = settings["target"]
    live = [dict(a) for a in armed]
    spent = [False] * len(live)
    trades, pos = [], None
    for i in range(day.f, day.end):
        b = m[i]
        t = mod[i]
        if pos is None:
            if t >= lv_mod.LAST_ENTRY_MIN:
                continue
            hit = [n for n, a in enumerate(live) if not spent[n] and _through(b, a, tick, eps)]
            if not hit:
                continue
            hit.sort(key=lambda n: (abs(b.open - live[n]["level"]), KIND_ORDER[live[n]["kind"]], live[n]["level"]))
            for n in hit:
                spent[n] = True
            a = live[hit[0]]
            side, entry, stop = a["side"], a["level"], a["stop"]
            dist = a["dist"]
            target = _rt(entry + side * tgt_mult * dist, tick) if tgt_mult else None
            pos = {"market": market, "date": day.date, "kind": a["kind"], "level": a["level"], "side": side,
                   "entry_ts": b.ts, "entry": entry, "stop": stop, "dist": dist, "target": target}
            worst = ((b.low if side == 1 else b.high) - entry) * side
            sf = _stop_fill(b, stop, side, slip, tick, fill, eps)
            if sf is not None:
                trades.append(_close(pos, b, sf[0], "stop", sf[1], worst))
                pos = None
            continue
        side, entry = pos["side"], pos["entry"]
        adverse = ((b.low if side == 1 else b.high) - entry) * side
        exit_ = None
        if t >= lv_mod.FLAT_MIN:
            px = b.open - side * slip
            px = min(max(px, b.low), b.high)
            exit_ = (px, "flat", False, min(worst, (px - entry) * side))
        else:
            sf = _stop_fill(b, pos["stop"], side, slip, tick, fill, eps)
            if sf is not None:
                exit_ = (sf[0], "stop", sf[1], min(worst, adverse))
            elif pos["target"] is not None and (
                    b.high >= pos["target"] + tick - eps if side == 1 else b.low <= pos["target"] - tick + eps):
                exit_ = (pos["target"], "target", False, min(worst, adverse))
            elif i == day.end - 1:
                exit_ = (b.close, "flat", False, min(worst, (b.close - entry) * side))
        for n, a in enumerate(live):
            if not spent[n] and _through(b, a, tick, eps):
                spent[n] = True
        if exit_ is None:
            worst = min(worst, adverse)
            continue
        trades.append(_close(pos, b, exit_[0], exit_[1], exit_[2], exit_[3]))
        pos = None
        if t >= lv_mod.FLAT_MIN:
            break
    if pos is not None:            # only when the entry minute was S(D)'s last minute
        b = m[day.end - 1]
        trades.append(_close(pos, b, b.close, "flat", False, min(worst, (b.close - pos["entry"]) * pos["side"])))
    return trades


def _close(pos, b, px, reason, gap, worst):
    t = dict(pos)
    t.update(exit_ts=b.ts, exit=px, reason=reason, gap=gap, points=(px - t["entry"]) * t["side"], worst=worst)
    return t


def per_contract(mk, settings, fill, dates=None):
    spec = mk.spec
    trades, armed = [], {}
    for day in mk.days:
        if dates is not None and day.date not in dates:
            continue
        a = arm(day, settings["kind"], settings["k"], spec["tick"])
        armed[day.date] = a
        if a:
            trades.extend(_sim_day(mk, day, a, settings, fill, spec, mk.market))
    return {"trades": trades, "armed": armed}


def _cents(x):
    return round(x + 0.0, 2)


def account(per_contract_by_market, specs, risk_pct, start=150000.0):
    order = {m: n for n, m in enumerate(specs)}
    rows = sorted((t for ts in per_contract_by_market.values() for t in ts),
                  key=lambda t: (t["date"], order[t["market"]], t["entry_ts"]))
    bal = start
    out, skipped, days = [], [], []
    k = 0
    while k < len(rows):
        date = rows[k]["date"]
        day_start, day_net, day_worst, sized = bal, 0.0, 0.0, 0
        while k < len(rows) and rows[k]["date"] == date:
            t = rows[k]
            k += 1
            sp = specs[t["market"]]
            slip = sp["slip_ticks"] * sp["tick"]
            lpc = (t["dist"] + slip) * sp["pv"] + sp["comm"]
            qty = min(int(math.floor(day_start * risk_pct / 100.0 / lpc + 1e-9)), sp["max_qty"])
            if qty < 1:
                skipped.append({"market": t["market"], "date": date, "entry_ts": t["entry_ts"],
                                "reason": "under one contract"})
                continue
            net = _cents((t["exit"] - t["entry"]) * t["side"] * sp["pv"] * qty - sp["comm"] * qty)
            r = dict(t, qty=qty, planned_cost=_cents(lpc * qty), net=net, balance_start=_cents(day_start))
            out.append(r)
            sized += 1
            day_net += net
            day_worst += (t["worst"] * sp["pv"] - sp["comm"]) * qty
        if not sized:
            continue
        end = _cents(day_start + day_net)
        low = _cents(min(day_start + day_worst, day_start, end))
        days.append({"date": date, "start": _cents(day_start), "end": end, "low": low})
        bal = end
    blob = json.dumps([[t["market"], t["date"], t["entry_ts"], t["side"], round(t["entry"], 9), round(t["exit"], 9),
                        t["reason"], t["qty"], t["net"]] for t in out], separators=(",", ":"))
    return {"start": start, "trades": out, "skipped": skipped, "days": days,
            "digest": hashlib.sha256(blob.encode()).hexdigest()[:16]}
