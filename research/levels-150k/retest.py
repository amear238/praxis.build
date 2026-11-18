#!/usr/bin/env python3
"""retest.py -- candidate 2 of research/levels-150k/PLAN.md (the amendment of 2026-11-18): break and retest.
Reuses levels.py's levels, fade.arm's armed set, fade's stop fill and fade.account, unchanged. Judges nothing.

flip(armed) -> candidate 2's armed set: each of candidate 1's armed levels on the other side s. A line: R = the
  level, stop = R - s x d. A zone: R = its far edge, stop = its near edge - s x d. dist unchanged.

per_contract(mk, settings, fill, dates=None) -> {"trades", "armed"} at one contract, as fade.per_contract.
  Each minute of S(D) from the first at or after 9:30, in order:
  - flat: a minute stamped before 15:00 meets a broken, unspent level's fill condition (long: low <= R - one
    tick; short: high >= R + one tick). Of those, the R nearest the minute's open fills (ties: the one nearer
    P0, then the long), at R exactly; the others are spent. Stop checked on the entry minute, target not.
  - in a position: fade's exits (flat at 15:55, stop, target from the next minute, the last minute's close);
    a broken level whose fill condition is met on any minute of the position, its exit minute included, is
    spent.
  - then, when the minute is the last of its quarter hour (quarters from 9:30) and the quarter starts at or
    before 14:45: every unbroken level whose R the minute's close is one tick or more beyond (long: close >=
    R + one tick) is broken, its limit resting from the next minute.
  Trade fields as fade's, with level = R and break_ts = the stamp of the break bar's last minute.

Standard library only. Run tests with python3 -I -B.
"""
import fade
import levels as lv_mod

LAST_BREAK_Q = (14 * 60 + 45 - lv_mod.OPEN_MIN) // 15          # the quarter starting at 14:45


def flip(armed):
    out = []
    for a in armed:
        s = -a["side"]
        if a.get("zone"):
            r, stop = a["far"], fade._rt(a["level"] - s * a["d"], a["tick"])
        else:
            r, stop = a["level"], fade._rt(a["level"] - s * a["d"], a["tick"])
        out.append({"kind": a["kind"], "side": s, "level": r, "stop": stop, "dist": a["dist"]})
    return out


def _arm2(day, kind, k, tick):
    """fade.arm's set, with what flip needs (the far edge and d)."""
    a1 = fade.arm(day, kind, k, tick)
    d = max(fade._floor_tick(k * day.atr, tick), tick) if day.atr is not None else None
    far = {}
    kinds = lv_mod.KINDS if kind == "ALL" else (kind,)
    for kd in kinds:
        for lv in day.levels.get(kd) or []:
            if lv.role in ("demand", "supply"):
                far[(lv.kind, lv.price)] = lv.far
    for a in a1:
        f = far.get((a["kind"], a["level"]))
        a.update(zone=f is not None, far=f, d=d, tick=tick)
    return flip(a1)


def _fills(b, a, tick, eps):
    return b.low <= a["level"] - tick + eps if a["side"] == 1 else b.high >= a["level"] + tick - eps


def _sim_day(mk, day, armed, settings, fill, spec, market):
    m, mod = mk.minutes, mk.mod
    tick = spec["tick"]
    eps = tick * fade.EPS_T
    slip = spec["slip_ticks"] * tick
    tgt_mult = settings["target"]
    live = [dict(a, broken=None) for a in armed]
    spent = [False] * len(live)
    trades, pos, worst = [], None, 0.0
    for i in range(day.f, day.end):
        b = m[i]
        t = mod[i]
        active = [n for n, a in enumerate(live) if a["broken"] is not None and not spent[n]]
        if pos is None:
            if t < lv_mod.LAST_ENTRY_MIN:
                hit = [n for n in active if _fills(b, live[n], tick, eps)]
                if hit:
                    hit.sort(key=lambda n: (abs(b.open - live[n]["level"]), abs(live[n]["level"] - day.p0),
                                            -live[n]["side"]))
                    for n in hit:
                        spent[n] = True
                    a = live[hit[0]]
                    side, entry, dist = a["side"], a["level"], a["dist"]
                    pos = {"market": market, "date": day.date, "kind": a["kind"], "level": entry, "side": side,
                           "entry_ts": b.ts, "entry": entry, "stop": a["stop"], "dist": dist,
                           "target": fade._rt(entry + side * tgt_mult * dist, tick) if tgt_mult else None,
                           "break_ts": a["broken"]}
                    worst = ((b.low if side == 1 else b.high) - entry) * side
                    sf = fade._stop_fill(b, a["stop"], side, slip, tick, fill, eps)
                    if sf is not None:
                        trades.append(fade._close(pos, b, sf[0], "stop", sf[1], worst))
                        pos = None
        else:
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
            for n in active:
                if _fills(b, live[n], tick, eps):
                    spent[n] = True
            if exit_ is None:
                worst = min(worst, adverse)
            else:
                trades.append(fade._close(pos, b, exit_[0], exit_[1], exit_[2], exit_[3]))
                pos = None
                if t >= lv_mod.FLAT_MIN:
                    break
        # the end of a quarter hour: record breaks
        q = (t - lv_mod.OPEN_MIN) // 15
        last_of_q = i + 1 >= day.end or (mod[i + 1] - lv_mod.OPEN_MIN) // 15 != q or mk.cal[i + 1] != mk.cal[i]
        if last_of_q and 0 <= q <= LAST_BREAK_Q:
            for a in live:
                if a["broken"] is None and (b.close >= a["level"] + tick - eps if a["side"] == 1
                                            else b.close <= a["level"] - tick + eps):
                    a["broken"] = b.ts
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
        a = _arm2(day, settings["kind"], settings["k"], spec["tick"])
        armed[day.date] = [{x: v for x, v in y.items() if x != "dist"} for y in a]
        if a:
            trades.extend(_sim_day(mk, day, a, settings, fill, spec, mk.market))
    return {"trades": trades, "armed": armed}
