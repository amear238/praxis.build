#!/usr/bin/env python3
"""closemom.py -- momentum into the close (research/close-momentum-150k/PLAN.md, "The exact rule" and the
amendment "before any engine code"). Simulates one market at one contract. Judges nothing.

run(minutes, daily, spec, market, settings, fill, dates=None) -> {"trades": [...]}
per_contract(mk, settings, fill, dates=None): the same on a levels.Market (its minutes, daily, spec, market).
  settings: {"name", "signal": "S1" | "S2" | "S3", "k", "atr_days": 14}. fill: "midpoint" | "kind" |
  "harsh-stops". dates: a set of ISO dates to keep (None: every trading day).

Each trading day d (a New York weekday with minute bars in it), against the trading day before it:
  price at t = the open of the first bar stamped in [t, t + 5); last price before t = the close of the last bar
  stamped in [t - 5, t). Y = the price at C the day before. S1 = the last price before C - 30, S2 = the last
  price before O + 30, each against Y (more than eps away); S3 = S1 when the two agree. No trade: no Y, no price
  at C - 30 or at C, Y's bar and the bars dated d (the evening included) not all of one contract, no side, or
  fewer than 14 daily bars dated before d.
  entry = the open of the bar at C - 30 + side x slip, held inside that bar. dist = max(floor_tick(k x A), tick),
  A = the mean high - low of the 14 daily bars dated (UTC) before d. stop = entry - side x dist.
  The stop watches the entry bar and every bar after it before the exit bar, with fade._stop_fill (the levels
  plan's gap, midpoint, kind and harsh fills). Not stopped: close at the exit bar's open - side x slip, held
  inside that bar. worst: a stop minute counts whole, the exit bar only at its fill.

Standard library only. Run tests with python3 -I -B.
"""
import bisect
import datetime as dt
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_RES = os.path.dirname(_HERE)
for p in (os.path.join(_RES, "levels-150k"), os.path.join(_RES, "trend-150k")):
    if p not in sys.path:
        sys.path.append(p)
import fade  # noqa: E402  (_stop_fill, _floor_tick: the levels plan's stop fills)
import levels  # noqa: E402  (the New York clock)

HOURS = {"NQ": (570, 960), "ES": (570, 960), "RTY": (570, 960),
         "ZN": (500, 900), "ZB": (500, 900),
         "6E": (500, 900), "6J": (500, 900), "6B": (500, 900), "6A": (500, 900),
         "CL": (540, 870), "GC": (500, 810)}
ATR_DAYS = 14


class _Index(object):
    """Per New York date: the slice of minutes stamped on it, and each minute's minute of day."""

    def __init__(self, minutes):
        n = len(minutes)
        self.mod = [0] * n
        self.start, self.end, self.iids = {}, {}, {}
        for i, b in enumerate(minutes):
            w = levels._wall(b.ts)
            d = w // 86400 + levels.EPOCH_ORD
            self.mod[i] = (w % 86400) // 60
            if d not in self.start:
                self.start[d] = i
                self.iids[d] = set()
            self.end[d] = i + 1
            self.iids[d].add(b.iid)

    def trading_days(self):
        return [d for d in sorted(self.start) if dt.date.fromordinal(d).weekday() < 5]

    def price_at(self, d, t):
        """Index of the first bar stamped in [t, t + 5) on date d, or None."""
        if d not in self.start:
            return None
        s, e = self.start[d], self.end[d]
        j = bisect.bisect_left(self.mod, t, s, e)
        return j if j < e and self.mod[j] < t + 5 else None

    def last_before(self, d, t):
        """Index of the last bar stamped in [t - 5, t) on date d, or None."""
        if d not in self.start:
            return None
        s, e = self.start[d], self.end[d]
        j = bisect.bisect_left(self.mod, t, s, e) - 1
        return j if j >= s and self.mod[j] >= t - 5 else None


def _atr_fn(daily):
    ords = [a.bar.ts // levels.NS // 86400 + levels.EPOCH_ORD for a in daily]

    def atr(d):
        j = bisect.bisect_left(ords, d)
        if j < ATR_DAYS:
            return None
        return sum(a.adj_high - a.adj_low for a in daily[j - ATR_DAYS:j]) / ATR_DAYS
    return atr


def _side(px, y, eps):
    if px is None or abs(px - y) <= eps:
        return 0
    return 1 if px > y else -1


def run(minutes, daily, spec, market, settings, fill, dates=None):
    o, c = HOURS[market]
    tick, slip = spec["tick"], spec["slip_ticks"] * spec["tick"]
    eps = tick * fade.EPS_T
    ix = _Index(minutes)
    atr = _atr_fn(daily)
    days = ix.trading_days()
    trades = []
    for k in range(1, len(days)):
        d, prev = days[k], days[k - 1]
        iso = dt.date.fromordinal(d).isoformat()
        if dates is not None and iso not in dates:
            continue
        yi, ei, xi = ix.price_at(prev, c), ix.price_at(d, c - 30), ix.price_at(d, c)
        if yi is None or ei is None or xi is None:
            continue
        s1i, s2i = ix.last_before(d, c - 30), ix.last_before(d, o + 30)
        if ix.iids[d] != {minutes[yi].iid}:
            continue
        y = minutes[yi].open
        s1 = minutes[s1i].close if s1i is not None else None
        s2 = minutes[s2i].close if s2i is not None else None
        a, b = _side(s1, y, eps), _side(s2, y, eps)
        side = {"S1": a, "S2": b, "S3": a if a == b else 0}[settings["signal"]]
        if side == 0:
            continue
        A = atr(d)
        if A is None:
            continue
        eb = minutes[ei]
        entry = min(max(eb.open + side * slip, eb.low), eb.high)
        dist = max(fade._floor_tick(settings["k"] * A, tick), tick)
        stop = entry - side * dist
        pos = {"market": market, "date": iso, "signal": settings["signal"], "side": side, "y": y, "s1": s1,
               "s2": s2, "atr": A, "dist": dist, "entry_ts": eb.ts, "entry": entry, "stop": stop}
        worst = None
        done = None
        for i in range(ei, xi):
            bb = minutes[i]
            adverse = ((bb.low if side == 1 else bb.high) - entry) * side
            worst = adverse if worst is None else min(worst, adverse)
            sf = fade._stop_fill(bb, stop, side, slip, tick, fill, eps)
            if sf is not None:
                done = (bb.ts, sf[0], "stop", sf[1], worst)
                break
        if done is None:
            xb = minutes[xi]
            px = min(max(xb.open - side * slip, xb.low), xb.high)
            at_fill = (px - entry) * side
            done = (xb.ts, px, "close", False, at_fill if worst is None else min(worst, at_fill))
        t = dict(pos)
        t.update(exit_ts=done[0], exit=done[1], reason=done[2], gap=done[3], points=(done[1] - entry) * side,
                 worst=done[4])
        trades.append(t)
    return {"trades": trades}


def per_contract(mk, settings, fill, dates=None):
    return run(mk.minutes, mk.daily, mk.spec, mk.market, settings, fill, dates)
