#!/usr/bin/env python3
"""accel.py -- candidate 4 of research/levels-150k/PLAN.md (the amendment of 2026-11-18): acceleration through a
level. Reuses retest's armed set (candidate 1's, turned to the other side: R and the stop) and its quarter-hour
break, fade's stop fill, fade._close and fade.account, unchanged. Judges nothing.

per_contract(mk, settings, fill, dates=None) -> {"trades", "armed"} at one contract, as retest.per_contract.
  settings: {"kind", "k", "target" (3), ...}. fill: "midpoint" | "kind" | "harsh-stops", for the entry stop and
  the exit stop alike. armed[date] = retest's list (kind, side, level = R, stop).
  15-minute bars from 9:30 as retest's; a level's break bar is the first, starting 9:30 to 14:45, that closes
  one tick or more beyond R in its direction. Its trigger E = the bar's high + one tick (long), its low - one
  tick (short), over all the bar's minutes. The entry rests from the next minute in S(D) after the bar's last
  minute to the last minute stamped before 15:00. On each of those minutes, in order: (1) the open at or beyond
  the stop cancels it; (2) the trigger met (long: high >= E): spent when a position is open on this minute (its
  entry minute to its exit minute), otherwise it may fill; (3) the stop reached (long: low <= stop) cancels it.
  Of the entries that may fill on one minute, the E nearer the open fills (ties: the R nearer the open, the R
  nearer P0, the long, the arming order); the rest are spent.
  Entry fill: the reference is E, or the open when it opens at or beyond E. Midpoint: halfway to the minute's high
  (long), up to the tick; kind: reference + one slippage, at most the high; harsh: the high. Shorts mirror.
  dist = |entry - stop|; target = entry + s x T x dist on the tick grid. Exits as fade's, from the entry minute:
  flat at 15:55, the stop (on the entry minute too), the target from the next minute, the last minute's close.
  Trade fields as retest's (level = R, break_ts) plus trigger = E.

Standard library only. Run tests with python3 -I -B.
"""
import fade
import levels as lv_mod
import retest

Q = 15


def _entry_fill(b, trig, side, slip, tick, fill, eps):
    if side == 1:
        ref = b.open if b.open >= trig - eps else trig
        if fill == "kind":
            return min(ref + slip, b.high)
        if fill == "midpoint":
            return fade._ceil_tick((ref + b.high) / 2.0, tick)
        return b.high
    ref = b.open if b.open <= trig + eps else trig
    if fill == "kind":
        return max(ref - slip, b.low)
    if fill == "midpoint":
        return fade._floor_tick((ref + b.low) / 2.0, tick)
    return b.low


def _beyond(px, level, side, eps):
    """px at or beyond level in the direction side (long: px >= level)."""
    return (px - level) * side >= -eps


def _sim_day(mk, day, armed, settings, fill, spec, market):
    m, mod = mk.minutes, mk.mod
    tick = spec["tick"]
    eps = tick * fade.EPS_T
    slip = spec["slip_ticks"] * tick
    tgt_mult = settings["target"]
    live = [dict(a, broken=None, trig=None, start=None) for a in armed]
    gone = [False] * len(live)
    trades, pos, worst = [], None, 0.0
    q_prev, q_hi, q_lo = None, None, None
    for i in range(day.f, day.end):
        b = m[i]
        t = mod[i]
        q = (t - lv_mod.OPEN_MIN) // Q
        if q != q_prev:
            q_prev, q_hi, q_lo = q, b.high, b.low
        else:
            q_hi, q_lo = max(q_hi, b.high), min(q_lo, b.low)
        held = pos is not None                       # a position is open on this minute, its exit minute included
        if held:
            side, entry = pos["side"], pos["entry"]
            adverse = ((b.low if side == 1 else b.high) - entry) * side
            exit_ = None
            if t >= lv_mod.FLAT_MIN:
                px = min(max(b.open - side * slip, b.low), b.high)
                exit_ = (px, "flat", False, min(worst, (px - entry) * side))
            else:
                sf = fade._stop_fill(b, pos["stop"], side, slip, tick, fill, eps)
                if sf is not None:
                    exit_ = (sf[0], "stop", sf[1], min(worst, adverse))
                elif pos["target"] is not None and (
                        b.high >= pos["target"] + tick - eps if side == 1 else b.low <= pos["target"] - tick + eps):
                    exit_ = (pos["target"], "target", False, min(worst, adverse))
                elif i == day.end - 1:
                    exit_ = (b.close, "flat", False, min(worst, (b.close - entry) * side))
            if exit_ is None:
                worst = min(worst, adverse)
            else:
                trades.append(fade._close(pos, b, exit_[0], exit_[1], exit_[2], exit_[3]))
                pos = None
                if t >= lv_mod.FLAT_MIN:
                    break
        if t < lv_mod.LAST_ENTRY_MIN:
            may = []
            for n, a in enumerate(live):
                if gone[n] or a["start"] is None or i < a["start"]:
                    continue
                s, stop, e = a["side"], a["stop"], a["trig"]
                if _beyond(stop, b.open, s, eps):                         # (1) opens at or beyond the stop
                    gone[n] = True
                elif _beyond(b.high if s == 1 else b.low, e, s, eps):     # (2) the trigger
                    if held:
                        gone[n] = True
                    else:
                        may.append(n)
                elif _beyond(stop, b.low if s == 1 else b.high, s, eps):  # (3) the stop reached
                    gone[n] = True
            if may:
                may.sort(key=lambda n: (abs(b.open - live[n]["trig"]), abs(b.open - live[n]["level"]),
                                        abs(live[n]["level"] - day.p0), -live[n]["side"], n))
                for n in may:
                    gone[n] = True
                a = live[may[0]]
                side, stop = a["side"], a["stop"]
                entry = _entry_fill(b, a["trig"], side, slip, tick, fill, eps)
                dist = abs(entry - stop)
                pos = {"market": market, "date": day.date, "kind": a["kind"], "level": a["level"], "side": side,
                       "entry_ts": b.ts, "entry": entry, "stop": stop, "dist": dist,
                       "target": fade._rt(entry + side * tgt_mult * dist, tick) if tgt_mult else None,
                       "break_ts": a["broken"], "trigger": a["trig"]}
                worst = ((b.low if side == 1 else b.high) - entry) * side
                sf = fade._stop_fill(b, stop, side, slip, tick, fill, eps)
                if sf is not None:
                    trades.append(fade._close(pos, b, sf[0], "stop", sf[1], worst))
                    pos = None
        # the end of a quarter hour: record breaks and set their triggers
        last_of_q = i + 1 >= day.end or (mod[i + 1] - lv_mod.OPEN_MIN) // Q != q or mk.cal[i + 1] != mk.cal[i]
        if last_of_q and 0 <= q <= retest.LAST_BREAK_Q:
            for a in live:
                if a["broken"] is None and _beyond(b.close, a["level"] + a["side"] * tick, a["side"], eps):
                    a["broken"] = b.ts
                    a["trig"] = fade._rt(q_hi + tick if a["side"] == 1 else q_lo - tick, tick)
                    a["start"] = i + 1
    if pos is not None:            # the entry minute was S(D)'s last minute: it counts only at its fill
        b = m[day.end - 1]
        trades.append(fade._close(pos, b, b.close, "flat", False, (b.close - pos["entry"]) * pos["side"]))
    return trades


def per_contract(mk, settings, fill, dates=None):
    spec = mk.spec
    trades, armed = [], {}
    for day in mk.days:
        if dates is not None and day.date not in dates:
            continue
        a = retest._arm2(day, settings["kind"], settings["k"], spec["tick"])
        armed[day.date] = [{x: v for x, v in y.items() if x != "dist"} for y in a]
        if a:
            trades.extend(_sim_day(mk, day, a, settings, fill, spec, mk.market))
    return {"trades": trades, "armed": armed}
