#!/usr/bin/env python3
"""rule_check.py -- the independent rule check for the trend plan (PLAN.md, "Amendment, 2026-11-18, before any
result"). Written from the plan's text alone, without reading the engines, so a misreading in an engine is not
copied here. Each check re-simulates the rule from the bars and settings, then compares the engine's output trade
by trade and returns a list of breaks (empty = clean). Prices are compared to 1e-6 (or a hundredth of a tick
when the tick is smaller, the yen), money to the cent.

check_weekly(result, series, rolls, specs)              version B, daily bars, back-adjusted prices
check_sameday(result, minutes, daily, specs, settings, fill)   version A, 1-minute bars, actual prices

Readings chosen where the plan is not explicit (the most literal one each time):
 1. The stop rests at the entry FILL minus side x distance (so a stop-out costs distance + one slippage, as the
    size formula's "loss for one contract" says).
 2. A signal exit (B) and the 15:55 flat (A) are market orders: the open plus slippage against, inside the bar.
    The "end" close (B, the data's last bar) and A's "minutes end before 15:55" close are at the bar's close with
    no slippage. That A close is given reason "flat".
 3. B net = the common net minus rolls x contracts x (commission + 2 slippages x dollars a point).
 4. B skipped trades are listed on the decision day (the close where the size was computed).
 5. B: at a market's own last bar, no close decision is made (nothing new, no skip); an open trade closes "end".
 6. B day record: start = the previous day record's end (the first: the starting balance). end and low mark open
    trades with their round-trip commission taken, but not the cost of rolls not yet closed. low uses the
    realised balance after the day's closes and the open trades still open at the close.
 7. A day low = start + sum over the day's trades of (worst x dollars a point x contracts - commission x
    contracts); with the commission, so low never exceeds end.
 8. A "worst" includes the whole range of every minute held, the entry minute and the stop minute included; a
    15:55 flat minute adds only its exit price (the trade is closed at its open).
 8b. A: a day's minutes are those starting at or before 16:00 New York (the plan: nothing held past 16:00). Added
    2026-11-18 by the engine author after the first real-data run: a holiday halt at 13:00 with a reopen at 18:00
    was being flattened at the 18:00 open. Test A5.
 9. A: a market with no entry minute that date gives no trade and no skip; a skip is listed only when an entry
    minute exists. A skip record is {"market", "date", "side", "reason"}. Within a date, trades are realised in
    market (dict) order for each trade's "balance".
10. Floating noise: tick rounding uses quotient +-1e-7, contracts floor(x + 1e-9), "reaches the stop" and "equal
    closes" use a millionth of a tick.

Standard library only. Python 3.14, run with python3 -I -B.
"""
import bisect
import math
from collections import Counter
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

DAY_NS = 86400 * 1_000_000_000
_EPOCH = date(1970, 1, 1).toordinal()
_Q = 1e-7
_NAME = {1: "long", -1: "short"}
_UNDER = "under one contract"


# ------------------------------------------------------------------------------------------------ the rule
def _floor_tick(x, tick):
    return math.floor(x / tick + _Q) * tick


def _ceil_tick(x, tick):
    return math.ceil(x / tick - _Q) * tick


def _slip(spec):
    return spec["slip_ticks"] * spec["tick"]


def _market_fill(o, h, l, order_side, slip):
    """A market order: the open plus slippage against the order (+1 buy, -1 sell), kept inside the bar."""
    return min(max(o + order_side * slip, l), h)


def _stop_fill(o, h, l, stop, side, slip, tick, fill):
    """(fill price, gap) if the bar stops a trade of this side, else None."""
    eps = tick * 1e-6
    if side > 0:
        if o <= stop + eps:
            gap, ref = True, o
        elif l <= stop + eps:
            gap, ref = False, stop
        else:
            return None
        if fill == "kind":
            px = max(ref - slip, l)
        elif fill == "midpoint":
            px = _floor_tick((ref + l) / 2, tick)
        else:
            px = l
    else:
        if o >= stop - eps:
            gap, ref = True, o
        elif h >= stop - eps:
            gap, ref = False, stop
        else:
            return None
        if fill == "kind":
            px = min(ref + slip, h)
        elif fill == "midpoint":
            px = _ceil_tick((ref + h) / 2, tick)
        else:
            px = h
    return px, gap


def _trail(stop, best, side, t, dist, tick):
    cand = best - side * t * dist
    if side > 0:
        cand = _floor_tick(cand, tick)
        return cand if cand > stop + tick * 1e-6 else stop
    cand = _ceil_tick(cand, tick)
    return cand if cand < stop - tick * 1e-6 else stop


def _size(balance, risk_pct, dist, spec):
    """(contracts, loss for one contract)."""
    loss1 = (dist + _slip(spec)) * spec["pv"] + spec["comm"]
    q = math.floor(balance * risk_pct / 100 / loss1 + 1e-9)
    return min(q, spec["max_qty"]), loss1


def _signal(adj, i, lookback, n_atr, tick):
    if i < 0 or i < lookback or i + 1 < n_atr:
        return 0
    d = adj[i].adj_close - adj[i - lookback].adj_close
    if abs(d) <= tick * 1e-6:
        return 0
    return 1 if d > 0 else -1


def _dist(adj, i, n_atr, mult, tick):
    atr = sum(a.adj_high - a.adj_low for a in adj[i - n_atr + 1:i + 1]) / n_atr
    return max(_floor_tick(mult * atr, tick), tick)


def _iso(day):
    return date.fromordinal(_EPOCH + day).isoformat()


# ------------------------------------------------------------------------------------------------ comparing
def _ptol(spec):
    return min(1e-6, spec["tick"] / 100)


def _px_eq(a, b, tol):
    return a is not None and b is not None and abs(a - b) <= tol


def _money_eq(a, b):
    return a is not None and b is not None and abs(a - b) < 0.006


def _compare_fields(breaks, label, mine, theirs, fields, tol):
    for f, kind in fields:
        if f not in theirs:
            breaks.append(f"{label}: field {f} missing")
            continue
        m, t = mine[f], theirs[f]
        try:
            ok = (_px_eq(m, t, tol) if kind == "px" else _money_eq(m, t) if kind == "money" else m == t)
        except TypeError:
            ok = False
        if not ok:
            breaks.append(f"{label}: {f} is {t!r}, rule says {m!r}")


def _compare_lists(breaks, what, mine, theirs, keyf, labelf, fields, tolf):
    mk = {keyf(t): t for t in mine}
    tk = {}
    for t in theirs:
        try:
            k = keyf(t)
        except (KeyError, TypeError):
            breaks.append(f"{what}: unreadable record {t!r}")
            continue
        if k in tk:
            breaks.append(f"{what} {labelf(k)}: listed twice")
        tk[k] = t
    for k in sorted(set(mk) - set(tk), key=str):
        breaks.append(f"{what} {labelf(k)}: missing (the rule makes this {what}: {mk[k]!r})")
    for k in sorted(set(tk) - set(mk), key=str):
        breaks.append(f"{what} {labelf(k)}: extra (the rule makes no such {what}: {tk[k]!r})")
    for k in sorted(set(mk) & set(tk), key=str):
        _compare_fields(breaks, f"{what} {labelf(k)}", mk[k], tk[k], fields, tolf(k))


def _compare_skips(breaks, mine, theirs, keys):
    def tup(s):
        return tuple(s.get(k) for k in keys)
    m, t = Counter(tup(s) for s in mine), Counter(tup(s) for s in theirs)
    for s in sorted((m - t).elements(), key=str):
        breaks.append(f"skipped {s}: missing (the rule skips this trade)")
    for s in sorted((t - m).elements(), key=str):
        breaks.append(f"skipped {s}: extra (the rule does not skip this)")


# ------------------------------------------------------------------------------------------------ version B
_B_FIELDS = [("side", "eq"), ("qty", "eq"), ("exit_day", "eq"), ("entry", "px"), ("exit", "px"),
             ("stop_initial", "px"), ("dist", "px"), ("planned_cost", "money"), ("reason", "eq"), ("gap", "eq"),
             ("rolls", "eq"), ("net", "money"), ("balance", "money")]
_DAY_FIELDS = [("start", "money"), ("end", "money"), ("low", "money")]


def _replay_weekly(settings, fill, start, series, rolls, specs):
    L, n_atr, mult = settings["lookback"], settings["atr_days"], settings["stop_mult"]
    t_mult, risk = settings["trail_mult"], settings["risk_pct"]
    markets = list(series)
    at = {m: {a.bar.ts // DAY_NS: k for k, a in enumerate(series[m])} for m in markets}
    last = {m: series[m][-1].bar.ts // DAY_NS for m in markets if series[m]}
    roll_days = {m: [r.ts // DAY_NS for r in rolls.get(m, [])] for m in markets}
    balance = start
    pos = dict.fromkeys(markets)
    pending = dict.fromkeys(markets)
    last_close = dict.fromkeys(markets)
    trades, skipped, days = [], [], []

    def close(m, p, d, px, reason, gap):
        nonlocal balance
        spec = specs[m]
        n = sum(1 for r in roll_days[m] if p["entry_day"] < r <= d)
        raw = ((px - p["entry"]) * p["side"] * spec["pv"] * p["qty"] - spec["comm"] * p["qty"]
               - n * p["qty"] * (spec["comm"] + 2 * _slip(spec) * spec["pv"]))
        balance = round(balance + round(raw, 2), 2)
        trades.append({"market": m, "side": _NAME[p["side"]], "qty": p["qty"], "entry_day": p["entry_day"],
                       "entry": p["entry"], "exit_day": d, "exit": px, "stop_initial": p["stop_initial"],
                       "dist": p["dist"], "planned_cost": p["planned_cost"], "reason": reason, "gap": gap,
                       "rolls": n, "net": round(raw, 2), "balance": balance})
        pos[m] = None

    def order(m, k, d, side):
        """The entry decided at this close, or None (skipped and listed)."""
        spec = specs[m]
        dist = _dist(series[m], k, n_atr, mult, spec["tick"])
        qty, loss1 = _size(balance, risk, dist, spec)
        if qty < 1:
            skipped.append({"market": m, "day": d, "side": _NAME[side], "reason": _UNDER})
            return None
        return {"side": side, "qty": qty, "dist": dist, "planned_cost": round(qty * loss1, 2)}

    prev_end = start
    for d in sorted(set().union(*at.values())):
        stopped = set()
        for m in markets:                                   # the opens and the stops, in market order
            k = at[m].get(d)
            if k is None:
                continue
            a, spec = series[m][k], specs[m]
            slip, tick = _slip(spec), spec["tick"]
            pend, pending[m] = pending[m], None
            if pend:
                if pend["exit"] and pos[m]:
                    p = pos[m]
                    close(m, p, d, _market_fill(a.adj_open, a.adj_high, a.adj_low, -p["side"], slip), "signal", False)
                e = pend["enter"]
                if e:
                    entry = _market_fill(a.adj_open, a.adj_high, a.adj_low, e["side"], slip)
                    stop = entry - e["side"] * e["dist"]
                    pos[m] = dict(e, entry=entry, entry_day=d, stop=stop, stop_initial=stop, best=None)
            p = pos[m]
            if p:
                hit = _stop_fill(a.adj_open, a.adj_high, a.adj_low, p["stop"], p["side"], slip, tick, fill)
                if hit:
                    close(m, p, d, hit[0], "stop", hit[1])
                    stopped.add(m)
                else:
                    ext = a.adj_high if p["side"] > 0 else a.adj_low
                    p["best"] = ext if p["best"] is None else (max if p["side"] > 0 else min)(p["best"], ext)
        for m in markets:                                   # the close decisions, in market order
            k = at[m].get(d)
            if k is None:
                continue
            a, spec = series[m][k], specs[m]
            last_close[m] = a.adj_close
            if d == last[m]:
                if pos[m]:
                    close(m, pos[m], d, a.adj_close, "end", False)
                continue
            if m in stopped:
                continue
            sig = _signal(series[m], k, L, n_atr, spec["tick"])
            p = pos[m]
            if p:
                if sig and sig != p["side"]:
                    pending[m] = {"exit": True, "enter": order(m, k, d, sig)}
                elif t_mult is not None:
                    p["stop"] = _trail(p["stop"], p["best"], p["side"], t_mult, p["dist"], spec["tick"])
            elif sig:
                e = order(m, k, d, sig)
                if e:
                    pending[m] = {"exit": False, "enter": e}
        end = low = balance
        for m in markets:
            p = pos[m]
            if not p:
                continue
            spec = specs[m]
            k = at[m].get(d)
            adverse = last_close[m] if k is None else (
                series[m][k].adj_low if p["side"] > 0 else series[m][k].adj_high)
            for px, which in ((last_close[m], "end"), (adverse, "low")):
                v = (px - p["entry"]) * p["side"] * spec["pv"] * p["qty"] - spec["comm"] * p["qty"]
                if which == "end":
                    end += v
                else:
                    low += v
        days.append({"day": d, "date": _iso(d), "start": prev_end, "end": end, "low": low})
        prev_end = end
    trades.sort(key=lambda t: (t["entry_day"], markets.index(t["market"])))
    return trades, skipped, days


def check_weekly(result, series, rolls, specs):
    breaks = []
    fill = result.get("fill")
    if fill not in ("kind", "midpoint", "harsh-stops"):
        return [f"fill {fill!r} is not kind, midpoint or harsh-stops"]
    markets = list(series)
    trades, skipped, days = _replay_weekly(result["settings"], fill, result["start"], series, rolls, specs)
    theirs = result.get("trades", [])
    try:
        keys = [(t["entry_day"], markets.index(t["market"])) for t in theirs]
        if keys != sorted(keys):
            breaks.append("trades are not in (entry day, market) order")
    except (KeyError, ValueError):
        breaks.append("trades: a record has no entry_day or an unknown market")
    _compare_lists(breaks, "trade", trades, theirs, lambda t: (t["market"], t["entry_day"]),
                   lambda k: f"{k[0]} entered {_iso(k[1])}", _B_FIELDS, lambda k: _ptol(specs[k[0]]))
    _compare_skips(breaks, skipped, result.get("skipped", []), ("market", "day", "side", "reason"))
    _compare_lists(breaks, "day record", days, result.get("days", []), lambda r: r["day"],
                   lambda k: _iso(k), [("date", "eq")] + _DAY_FIELDS, lambda k: 1e-6)
    return breaks


# ------------------------------------------------------------------------------------------------ version A
_A_FIELDS = [("side", "eq"), ("entry", "px"), ("exit", "px"), ("stop_initial", "px"), ("dist", "px"),
             ("reason", "eq"), ("gap", "eq"), ("points", "px"), ("worst", "px"), ("qty", "eq"),
             ("planned_cost", "money"), ("net", "money"), ("balance", "money")]


def _ny_minutes(bars, tz):
    """{New York day number: [(minute of the day, bar)]}, in time order."""
    out, offs = {}, {}
    for b in sorted(bars, key=lambda b: b.ts):
        sec = b.ts // 1_000_000_000
        hour = sec // 3600
        off = offs.get(hour)
        if off is None:     # New York's offset only changes on the hour
            off = offs[hour] = int(datetime.fromtimestamp(hour * 3600, timezone.utc).astimezone(tz)
                                   .utcoffset().total_seconds())
        local = sec + off
        out.setdefault(local // 86400, []).append(((local % 86400) // 60, b))
    return out


def _hm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def _sim_day(mins, j, side, dist, spec, t_mult, flat_min, fill):
    slip, tick = _slip(spec), spec["tick"]
    b0 = mins[j][1]
    entry = _market_fill(b0.open, b0.high, b0.low, side, slip)
    stop = stop_initial = entry - side * dist
    best, worst, gap, reason, exit_ = None, 0.0, False, None, None
    for mod, b in mins[j:]:
        if mod >= flat_min:
            exit_, reason = _market_fill(b.open, b.high, b.low, -side, slip), "flat"
            break
        worst = min(worst, ((b.low if side > 0 else b.high) - entry) * side)
        hit = _stop_fill(b.open, b.high, b.low, stop, side, slip, tick, fill)
        if hit:
            (exit_, gap), reason = hit, "stop"
            break
        ext = b.high if side > 0 else b.low
        best = ext if best is None else (max if side > 0 else min)(best, ext)
        if t_mult is not None:
            stop = _trail(stop, best, side, t_mult, dist, tick)
    else:
        exit_, reason = mins[-1][1].close, "flat"
    worst = min(worst, (exit_ - entry) * side)
    return entry, exit_, stop_initial, reason, gap, worst


def _replay_sameday(risk, start, minutes, daily, specs, settings, fill):
    tz = ZoneInfo("America/New_York")
    L, n_atr, mult, t_mult = settings["lookback"], settings["atr_days"], settings["stop_mult"], settings["trail_mult"]
    entry_min, flat_min = _hm(settings["entry"]), _hm(settings["flat"])
    markets = list(minutes)
    # nothing is held past 16:00 (PLAN, version A): a day's minutes are those starting at or before 16:00, so an
    # evening reopen after a holiday halt is not part of the trading day
    by_day = {m: {D: [x for x in v if x[0] <= 16 * 60] for D, v in _ny_minutes(minutes[m], tz).items()}
              for m in markets}
    dstamps = {m: [a.bar.ts // DAY_NS for a in daily.get(m, [])] for m in markets}
    balance = start
    trades, skipped, days = [], [], []
    for D in sorted(set().union(*by_day.values())):
        bal0, today = balance, []
        for m in markets:
            mins = by_day[m].get(D)
            if not mins:
                continue
            spec, adj = specs[m], daily.get(m, [])
            i = bisect.bisect_left(dstamps[m], D) - 1      # the last daily bar dated before the trading day
            side = _signal(adj, i, L, n_atr, spec["tick"])
            if not side:
                continue
            j = next((j for j, (mod, _) in enumerate(mins) if entry_min <= mod < flat_min), None)
            if j is None:
                continue
            dist = _dist(adj, i, n_atr, mult, spec["tick"])
            qty, loss1 = _size(bal0, risk, dist, spec)
            if qty < 1:
                skipped.append({"market": m, "date": _iso(D), "side": _NAME[side], "reason": _UNDER})
                continue
            entry, exit_, stop_initial, reason, gap, worst = _sim_day(mins, j, side, dist, spec, t_mult,
                                                                      flat_min, fill)
            net = round((exit_ - entry) * side * spec["pv"] * qty - spec["comm"] * qty, 2)
            today.append({"market": m, "date": _iso(D), "side": _NAME[side], "entry": entry, "exit": exit_,
                          "stop_initial": stop_initial, "dist": dist, "reason": reason, "gap": gap,
                          "points": (exit_ - entry) * side, "worst": worst, "qty": qty,
                          "planned_cost": round(qty * loss1, 2), "net": net,
                          "_open_low": worst * spec["pv"] * qty - spec["comm"] * qty})
        if not today:
            continue
        for t in today:
            balance = round(balance + t["net"], 2)
            t["balance"] = balance
        days.append({"date": _iso(D), "start": bal0, "end": balance,
                     "low": bal0 + sum(t.pop("_open_low") for t in today)})
        trades.extend(today)
    return trades, skipped, days


def check_sameday(result, minutes, daily, specs, settings, fill):
    if fill not in ("kind", "midpoint", "harsh-stops"):
        return [f"fill {fill!r} is not kind, midpoint or harsh-stops"]
    breaks = []
    trades, skipped, days = _replay_sameday(result["risk_pct"], result["start"], minutes, daily, specs,
                                            settings, fill)
    _compare_lists(breaks, "trade", trades, result.get("trades", []), lambda t: (t["market"], t["date"]),
                   lambda k: f"{k[0]} on {k[1]}", _A_FIELDS, lambda k: _ptol(specs[k[0]]))
    _compare_skips(breaks, skipped, result.get("skipped", []), ("market", "date", "side", "reason"))
    _compare_lists(breaks, "day record", days, result.get("days", []), lambda r: r["date"],
                   lambda k: k, _DAY_FIELDS, lambda k: 1e-6)
    return breaks
