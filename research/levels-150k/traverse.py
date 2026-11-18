#!/usr/bin/env python3
"""traverse.py -- candidate 3 of research/levels-150k/PLAN.md (the amendment of 2026-11-18): value area traversal,
the "80% rule". Reuses levels.py's VP levels (the prior session's value area), fade's stop fill, fade._close and
fade.account, unchanged. Judges nothing.

setup(day, k, tick) -> {"kind": "VA", "side", "level": N, "far": F, "stop"} or None.
  None without ATR, P0 or both VP edges. P0 >= VAH + one tick: a short, N = VAH, F = VAL. P0 <= VAL - one tick:
  a long, N = VAL, F = VAH. Otherwise None. d = k x ATR rounded down to the tick, at least one tick; stop =
  N - s x d.

per_contract(mk, settings, fill, dates=None) -> {"trades", "armed"} at one contract, as fade.per_contract.
  settings: {"kind": "VA", "k", "min_rr" (0 | 2 | 3), ...}. armed[date] = [setup] or [].
  30-minute bars: D's minutes from 9:30 to before 15:00 by half hour from 9:30; a bar's close is its last
  minute's close; a half hour with no minute has no bar. Inside: VAL + one tick <= close <= VAH - one tick.
  The signal is the first pair of consecutive bars both closing inside whose second bar starts at or before
  14:00; C = its close, setup_ts = the stamp of its last minute. Only that pair counts.
  Filter: |F - C| >= min_rr x |C - stop| (within a millionth of a tick).
  Entry: the next minute after the second bar's last minute, if it is in S(D) and stamped before 15:00. No trade
  if it opens at or beyond the stop or the far edge. Long fill = min(open + slip, high); short = max(open - slip,
  low). dist = |entry - stop|, unrounded. target = F.
  Exits, from the entry minute: flat at 15:55 (open less one slip, inside the minute), the stop (on the entry
  minute too; fade's three fills), the target from the next minute (high >= F + one tick, filled at F), and the
  last minute's close when S(D) ends first. worst as fade's.

Standard library only. Run tests with python3 -I -B.
"""
import fade
import levels as lv_mod

HALF = 30
LAST_SIGNAL_H = (14 * 60 - lv_mod.OPEN_MIN) // HALF          # the half hour starting at 14:00


def setup(day, k, tick):
    if day.atr is None or day.p0 is None:
        return None
    vp = day.levels.get("VP") or []
    vah = next((x.price for x in vp if x.role == "vah"), None)
    val = next((x.price for x in vp if x.role == "val"), None)
    if vah is None or val is None:
        return None
    eps = tick * fade.EPS_T
    if day.p0 >= vah + tick - eps:
        s, n, f = -1, vah, val
    elif day.p0 <= val - tick + eps:
        s, n, f = 1, val, vah
    else:
        return None
    d = max(fade._floor_tick(k * day.atr, tick), tick)
    return {"kind": "VA", "side": s, "level": n, "far": f, "stop": fade._rt(n - s * d, tick)}


def _signal(mk, day, su, tick, eps):
    """-> (index of the second bar's last minute, its close) or None."""
    m, mod = mk.minutes, mk.mod
    lo, hi = min(su["level"], su["far"]), max(su["level"], su["far"])
    bars = []                                   # [half-hour number, index of its last minute]
    for i in range(day.f, day.end):
        t = mod[i]
        if t >= lv_mod.LAST_ENTRY_MIN:
            break
        h = (t - lv_mod.OPEN_MIN) // HALF
        if bars and bars[-1][0] == h:
            bars[-1][1] = i
        else:
            bars.append([h, i])
    prev_in = False
    for h, i in bars:
        c = m[i].close
        inside = lo + tick - eps <= c <= hi - tick + eps
        if inside and prev_in and h <= LAST_SIGNAL_H:
            return i, c
        if h >= LAST_SIGNAL_H:
            return None
        prev_in = inside
    return None


def _sim_day(mk, day, su, settings, fill, spec, market):
    m, mod = mk.minutes, mk.mod
    tick = spec["tick"]
    eps = tick * fade.EPS_T
    slip = spec["slip_ticks"] * tick
    sig = _signal(mk, day, su, tick, eps)
    if sig is None:
        return []
    last, c = sig
    side, stop, far = su["side"], su["stop"], su["far"]
    if abs(far - c) < settings["min_rr"] * abs(c - stop) - eps:
        return []
    i = last + 1
    if i >= day.end or mod[i] >= lv_mod.LAST_ENTRY_MIN:
        return []
    b = m[i]
    if (b.open - stop) * side <= eps or (far - b.open) * side <= eps:
        return []
    entry = min(b.open + slip, b.high) if side == 1 else max(b.open - slip, b.low)
    pos = {"market": market, "date": day.date, "kind": "VA", "level": su["level"], "side": side,
           "entry_ts": b.ts, "entry": entry, "stop": stop, "dist": abs(entry - stop), "target": far,
           "setup_ts": m[last].ts}
    worst = ((b.low if side == 1 else b.high) - entry) * side
    sf = fade._stop_fill(b, stop, side, slip, tick, fill, eps)
    if sf is not None:
        return [fade._close(pos, b, sf[0], "stop", sf[1], worst)]
    for j in range(i + 1, day.end):
        b = m[j]
        adverse = ((b.low if side == 1 else b.high) - entry) * side
        if mod[j] >= lv_mod.FLAT_MIN:
            px = min(max(b.open - side * slip, b.low), b.high)
            return [fade._close(pos, b, px, "flat", False, min(worst, (px - entry) * side))]
        sf = fade._stop_fill(b, stop, side, slip, tick, fill, eps)
        if sf is not None:
            return [fade._close(pos, b, sf[0], "stop", sf[1], min(worst, adverse))]
        if (b.high >= far + tick - eps) if side == 1 else (b.low <= far - tick + eps):
            return [fade._close(pos, b, far, "target", False, min(worst, adverse))]
        if j == day.end - 1:
            return [fade._close(pos, b, b.close, "flat", False, min(worst, (b.close - entry) * side))]
        worst = min(worst, adverse)
    b = m[day.end - 1]                 # the entry minute was S(D)'s last minute: it counts only at its fill
    return [fade._close(pos, b, b.close, "flat", False, (b.close - entry) * side)]


def per_contract(mk, settings, fill, dates=None):
    spec = mk.spec
    trades, armed = [], {}
    for day in mk.days:
        if dates is not None and day.date not in dates:
            continue
        su = setup(day, settings["k"], spec["tick"])
        armed[day.date] = [su] if su else []
        if su:
            trades.extend(_sim_day(mk, day, su, settings, fill, spec, mk.market))
    return {"trades": trades, "armed": armed}
