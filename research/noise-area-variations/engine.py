#!/usr/bin/env python3
"""engine.py -- the backtest engine for one Noise-Area variation, described by a settings dict.

Works on a list of globex.Day (globex.py) and the noise band of bands.py (called as bands.day_bands, so a
test can stand a band in). sm is globex's session minute: 18:01 is sm 1, 09:31 is sm 931, 16:00 is sm 1320.
Stamps mark the END of the minute. Instrument MNQ: 2.00 dollars a point, 1.90 a contract round trip, tick
0.25, slippage 2 ticks (0.5 points) per side on every fill. This module judges nothing: it returns trades.

Settings (validate): exactly the fields name, reason, anchor, lookback, band_mult, cadence, entry_window,
sides, reentry, stop, exit, max_trades_per_day, risk_pct, flat_time; see validate for the allowed values.

Each bar of a trading day, in this order:
  a. Fills. Orders decided on the previous bar fill at this bar's open, 2 ticks against, kept inside the
     bar's range: an exit first, then an entry. A new position's stop rests at entry fill -/+ dist.
  b. Resting stop (from the entry bar on). If the bar's adverse extreme reaches the stop (long: low <= stop;
     short: high >= stop) the stop fills. "kind": at the stop, or at the open when the bar opens already
     beyond it, 2 ticks against, kept inside the bar's range. "harsh-stops": at the bar's low (long) or high
     (short). gap is True, on both models, when the open is already beyond the stop. Nothing else happens on
     that bar.
  c. Flat. On the bar stamped flat_time or later, or on the day's last bar: an open position is closed at
     the next bar's open, 2 ticks against, when the day has a next bar; else at this bar's close, 2 ticks
     against, kept inside the bar's range. Nothing else happens on that bar (no decision, no entry).
  d. Decision bar: a bar that has a band point, stamped :00 or :30 ("half_hour") or any bar ("minute").
     "Long"/"short" below is the position at the start of this step. C is the bar's close.
       Exit (exit "band_or_vwap" only): a long when C <= max(upper, vwap), a short when C >= min(lower, vwap).
       Opposite signal (every exit kind): a long when C < lower and sides allows shorts, a short when
       C > upper and sides allows longs. It closes the position (reason "reverse", or "exit" when the exit
       rule also fires) even when the new entry is then refused.
       Entry: long when C > upper, longs allowed and not long; short when C < lower, shorts allowed and not
       short; and only if the bar's stamp is inside entry_window (first <= T <= second, in trading-day
       order), the day has filled fewer than max_trades_per_day entries, and reentry allows it.
       reentry "fresh": once a position on a side has exited (any reason), no entry on that side until a
       decision bar closes inside the band (lower <= C <= upper). A decided exit's own decision bar counts
       (its close is checked after the exit is decided); a stop bar is no decision bar. Each day starts
       fresh, as in the measuring pass.
       Size, fixed here: dist = the stop kind's distance from C (stop_distance), rounded down to a tick.
       loss_per_contract = (dist + 0.5) * 2.0 + 1.90; qty = floor(balance * risk_pct / 100 /
       loss_per_contract), with balance the realised balance at this decision bar -- on a reverse, before
       the result of the position being closed is known. planned_cost = qty * loss_per_contract. dist under
       10.0 (zero and negative included): skipped, "stop under 10 points"; qty < 1: skipped, "under one
       contract". A skip is listed in `skipped` and does not count toward max_trades_per_day.
       stop "none" (only with allow_no_stop, for the baseline test): qty 1, no stop order; stop_initial,
       dist, planned_cost and r are None.
  e. Trail (exit "trail_r"): at the bar's close the stop moves to best -/+ value * dist (best = the highest
     high of a long, the lowest low of a short, since entry, the entry bar included), placed on the tick
     grid away from the price, and only when that is toward the price. It acts from the next bar. With
     trail_r or hold_to_flat the band-or-VWAP exit is not applied.

Trade: date (trading day), side ("long"|"short"), qty, entry_dt, entry, exit_dt, exit, stop_initial, dist,
planned_cost, reason ("stop"|"exit"|"reverse"|"flat"), gap, net = (exit - entry) * sign * 2.0 * qty -
1.90 * qty (to the cent), r = net / planned_cost, balance (realised, after the trade).
Day: {date, start, end, low}, one per day given; low is the lowest the balance reached that day with an
open position marked at each bar's adverse extreme (commission included), and after every close.
digest: sha256 of json.dumps(trades, sort_keys=True).

Data holes: for every trading purpose a day ends at globex.tradable_end(day), the last bar before the first
gap of more than 60 minutes between consecutive bars (the day's last bar when there is none). That bar is
"the day's last bar" in (c): an open position is closed at its close, 2 ticks against, reason "flat", and a
decision there places no entry. No fill, stop check, decision or day-low mark happens on a later bar. The
band is still built by bands.day_bands from the full, untrimmed days. A fill across a hole would be a fake.

The engine applies no early-close cut and no holiday calendar.

Standard library only. Run with `python3 -I -B`.
"""
import hashlib
import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import bands    # noqa: E402  (called as bands.day_bands, so a test can stand a band in)
import globex   # noqa: E402

PV = 2.0
COMM = 1.90
TICK = 0.25
SLIP = 0.5
START = 50000.0
MIN_STOP_POINTS = 10.0
FILLS = ("kind", "harsh-stops")

FIELDS = ("name", "reason", "anchor", "lookback", "band_mult", "cadence", "entry_window", "sides", "reentry",
          "stop", "exit", "max_trades_per_day", "risk_pct", "flat_time")
ANCHORS = ("0930", "1800")
CADENCES = ("half_hour", "minute")
SIDES = ("both", "long", "short")
REENTRY = ("any", "fresh")
STOP_KINDS = ("half_width", "full_width", "to_anchor", "opposite_band", "width_frac")
EXIT_KINDS = ("band_or_vwap", "hold_to_flat", "trail_r")
LAST_DECISION_SM = globex.sm_of("15:59")


# ---------------------------------------------------------------------------------------------- settings
def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _need(ok, field, msg):
    if not ok:
        raise ValueError("%s: %s" % (field, msg))


def _stamp_sm(field, v):
    """'HH:MM' inside the trading day (18:01 to 15:59) -> sm."""
    _need(isinstance(v, str) and len(v) == 5 and v[2] == ":" and (v[:2] + v[3:]).isdigit(), field,
          "must be an 'HH:MM' stamp, got %r" % (v,))
    try:
        sm = globex.sm_of(v)
    except ValueError:
        sm = None
    _need(sm is not None and 1 <= sm <= LAST_DECISION_SM, field,
          "must be inside the trading day, 18:01 to 15:59, got %r" % (v,))
    return sm


def _order(field, v, kinds, valued):
    """stop / exit: {"kind": k} or, for the kinds in `valued` {k: (lo, hi)}, {"kind": k, "value": x}."""
    _need(isinstance(v, dict), field, "must be a dict, got %r" % (v,))
    _need(v.get("kind") in kinds, field + ".kind", "must be one of %s, got %r" % (kinds, v.get("kind")))
    k = v["kind"]
    if k in valued:
        lo, hi = valued[k]
        _need(set(v) == {"kind", "value"}, field, "%s takes exactly kind and value, got %s" % (k, sorted(v)))
        _need(_num(v["value"]) and lo <= v["value"] <= hi, field + ".value",
              "%s needs a value from %g to %g, got %r" % (k, lo, hi, v["value"]))
    else:
        _need(set(v) == {"kind"}, field, "%s takes only kind, got %s" % (k, sorted(v)))


def validate(settings, allow_no_stop=False):
    """-> settings itself, or raise ValueError naming the first bad field."""
    s = settings
    _need(isinstance(s, dict), "settings", "must be a dict")
    extra = sorted(set(s) - set(FIELDS))
    _need(not extra, ",".join(extra), "unknown field")
    missing = [f for f in FIELDS if f not in s]
    _need(not missing, ",".join(missing), "missing field")
    _need(isinstance(s["name"], str) and s["name"] != "", "name", "must be a non-empty string")
    _need(isinstance(s["reason"], str), "reason", "must be a string")
    _need(s["anchor"] in ANCHORS, "anchor", "must be one of %s, got %r" % (ANCHORS, s["anchor"]))
    lb = s["lookback"]
    _need(isinstance(lb, int) and not isinstance(lb, bool) and 5 <= lb <= 60, "lookback",
          "must be an integer from 5 to 60, got %r" % (lb,))
    _need(_num(s["band_mult"]) and 0.25 <= s["band_mult"] <= 4.0, "band_mult", "must be from 0.25 to 4.0")
    _need(s["cadence"] in CADENCES, "cadence", "must be one of %s, got %r" % (CADENCES, s["cadence"]))
    _need(s["sides"] in SIDES, "sides", "must be one of %s, got %r" % (SIDES, s["sides"]))
    _need(s["reentry"] in REENTRY, "reentry", "must be one of %s, got %r" % (REENTRY, s["reentry"]))
    kinds = STOP_KINDS + (("none",) if allow_no_stop else ())
    _order("stop", s["stop"], kinds, {"width_frac": (0.1, 3.0)})
    _order("exit", s["exit"], EXIT_KINDS, {"trail_r": (0.5, 5.0)})
    _need(not (s["stop"]["kind"] == "none" and s["exit"]["kind"] == "trail_r"), "exit",
          "trail_r needs a stop distance; stop none has none")
    mt = s["max_trades_per_day"]
    _need(isinstance(mt, int) and not isinstance(mt, bool) and 1 <= mt <= 10, "max_trades_per_day",
          "must be an integer from 1 to 10, got %r" % (mt,))
    _need(_num(s["risk_pct"]) and 0.1 <= s["risk_pct"] <= 2.0, "risk_pct", "must be from 0.1 to 2.0")
    flat_sm = _stamp_sm("flat_time", s["flat_time"])
    w = s["entry_window"]
    _need(isinstance(w, (list, tuple)) and len(w) == 2, "entry_window", "must be two 'HH:MM' stamps")
    a, b = _stamp_sm("entry_window", w[0]), _stamp_sm("entry_window", w[1])
    _need(a < b, "entry_window", "the first stamp must be earlier than the second in trading-day order")
    _need(b <= flat_sm, "entry_window", "must end no later than flat_time")
    return s


# ---------------------------------------------------------------------------------------------- prices
def floor_tick(x):
    return math.floor(x / TICK + 1e-9) * TICK


def ceil_tick(x):
    return math.ceil(x / TICK - 1e-9) * TICK


def loss_per_contract(dist):
    return (dist + SLIP) * PV + COMM


def stop_distance(kind, value, side, close, p):
    """The stop kind's distance in points from the decision bar's close, rounded down to a tick; side +1/-1."""
    if kind == "half_width":
        x = p.width / 2.0
    elif kind == "full_width":
        x = p.width
    elif kind == "width_frac":
        x = value * p.width
    elif kind == "to_anchor":
        x = close - p.anchor_price if side == 1 else p.anchor_price - close
    elif kind == "opposite_band":
        x = close - p.lower if side == 1 else p.upper - close
    else:
        raise ValueError("stop kind %r" % (kind,))
    return floor_tick(x)


def _clamp(x, b):
    return b.l if x < b.l else b.h if x > b.h else x


def _market(b, side_of_order):
    """Market fill at bar b's open; side_of_order +1 buys, -1 sells."""
    return _clamp(b.o + SLIP * side_of_order, b)


# ---------------------------------------------------------------------------------------------- the run
class _Pos(object):
    __slots__ = ("side", "qty", "entry_dt", "entry", "stop", "stop_initial", "dist", "planned", "best")


def run(days, settings, fill="harsh-stops", start=START, allow_no_stop=False):
    """Simulate one variation over `days` (a list of globex.Day in date order; earlier days feed the band).
    -> {"settings", "fill", "start", "trades", "days", "skipped", "digest"}."""
    s = validate(settings, allow_no_stop)
    if fill not in FILLS:
        raise ValueError("fill must be one of %s, got %r" % (FILLS, fill))
    sim = _Sim(s, fill, float(start))
    for k in range(len(days)):
        sim.day(days[k], bands.day_bands(days, k, s["anchor"], s["lookback"], s["band_mult"]))
    digest = hashlib.sha256(json.dumps(sim.trades, sort_keys=True).encode()).hexdigest()
    return {"settings": s, "fill": fill, "start": float(start), "trades": sim.trades, "days": sim.days,
            "skipped": sim.skipped, "digest": digest}


class _Sim(object):
    def __init__(self, s, fill, start):
        self.s, self.fill, self.balance = s, fill, start
        self.flat_sm = globex.sm_of(s["flat_time"])
        self.win = (globex.sm_of(s["entry_window"][0]), globex.sm_of(s["entry_window"][1]))
        self.long_ok = s["sides"] in ("both", "long")
        self.short_ok = s["sides"] in ("both", "short")
        self.stop_kind = s["stop"]["kind"]
        self.stop_value = s["stop"].get("value")
        self.exit_kind = s["exit"]["kind"]
        self.trail = s["exit"].get("value") if self.exit_kind == "trail_r" else None
        self.trades, self.days, self.skipped = [], [], []
        self.pos = None

    def _close(self, date, b, px, reason, gap=False):
        p = self.pos
        net = round((px - p.entry) * p.side * PV * p.qty - COMM * p.qty, 2)
        self.balance = round(self.balance + net, 2)
        self.trades.append({
            "date": date, "side": "long" if p.side == 1 else "short", "qty": p.qty,
            "entry_dt": p.entry_dt, "entry": p.entry, "exit_dt": b.dt.isoformat(" "), "exit": px,
            "stop_initial": p.stop_initial, "dist": p.dist, "planned_cost": p.planned, "reason": reason,
            "gap": gap, "net": net, "r": None if p.planned is None else net / p.planned,
            "balance": self.balance})
        self.pos = None
        return p.side

    def _open(self, b, order):
        side, dist, qty, planned = order
        p = _Pos()
        p.side, p.qty, p.dist, p.planned = side, qty, dist, planned
        p.entry_dt = b.dt.isoformat(" ")
        p.entry = _market(b, side)
        p.stop = p.stop_initial = None if dist is None else p.entry - side * dist
        p.best = p.entry
        self.pos = p

    def _stop_fill(self, b):
        p = self.pos
        if p.side == 1:
            gap = b.o < p.stop
            px = b.l if self.fill == "harsh-stops" else _clamp(min(p.stop, b.o) - SLIP, b)
        else:
            gap = b.o > p.stop
            px = b.h if self.fill == "harsh-stops" else _clamp(max(p.stop, b.o) + SLIP, b)
        return px, gap

    def _mark(self, b):
        p = self.pos
        x = b.l if p.side == 1 else b.h
        return self.balance + (x - p.entry) * p.side * PV * p.qty - COMM * p.qty

    def _size(self, date, b, side, p):
        """-> (side, dist, qty, planned) for an entry decided on bar b, or None when the signal is skipped."""
        if self.stop_kind == "none":
            return (side, None, 1, None)
        dist = stop_distance(self.stop_kind, self.stop_value, side, b.c, p)
        why = None
        if dist < MIN_STOP_POINTS:
            why = "stop under 10 points"
        else:
            lpc = loss_per_contract(dist)
            qty = int(math.floor(self.balance * self.s["risk_pct"] / 100.0 / lpc + 1e-9))
            if qty < 1:
                why = "under one contract"
        if why is not None:
            self.skipped.append({"date": date, "decision_dt": b.dt.isoformat(" "),
                                 "side": "long" if side == 1 else "short", "reason": why})
            return None
        return (side, dist, qty, round(qty * lpc, 2))

    def day(self, day, bmap):
        s, date = self.s, day.date
        half_hour = s["cadence"] == "half_hour"
        fresh = s["reentry"] == "fresh"
        blocked = {1: False, -1: False}
        entries = 0
        pend_exit = pend_entry = None
        day_start = day_low = self.balance
        last = globex.tradable_end(day)      # data hole: no bar after it is traded (rule in the docstring)
        bars = day.bars[:last + 1]
        for i, b in enumerate(bars):
            # a. fills: exit first, then entry
            if pend_exit is not None:
                blocked[self._close(date, b, _market(b, -self.pos.side), pend_exit)] = True
                day_low = min(day_low, self.balance)
            if pend_entry is not None:
                self._open(b, pend_entry)
                entries += 1
            pend_exit = pend_entry = None
            pos = self.pos
            # b. the resting stop
            if pos is not None:
                if pos.stop is not None and (b.l <= pos.stop if pos.side == 1 else b.h >= pos.stop):
                    px, gap = self._stop_fill(b)
                    blocked[self._close(date, b, px, "stop", gap)] = True
                    day_low = min(day_low, self.balance)
                    continue
                day_low = min(day_low, self._mark(b))
                pos.best = max(pos.best, b.h) if pos.side == 1 else min(pos.best, b.l)
            # c. flat
            if b.sm >= self.flat_sm or i == last:
                if pos is not None:
                    if i < last:
                        pend_exit = "flat"
                    else:
                        blocked[self._close(date, b, _clamp(b.c - SLIP * pos.side, b), "flat")] = True
                        day_low = min(day_low, self.balance)
                continue
            # d. decision bar
            p = bmap.get(b.sm)
            if p is not None and (not half_hour or b.dt.minute in (0, 30)):
                c = b.c
                side = pos.side if pos is not None else 0
                if side == 1:
                    if self.exit_kind == "band_or_vwap" and c <= max(p.upper, p.vwap):
                        pend_exit = "exit"
                    elif self.short_ok and c < p.lower:
                        pend_exit = "reverse"
                elif side == -1:
                    if self.exit_kind == "band_or_vwap" and c >= min(p.lower, p.vwap):
                        pend_exit = "exit"
                    elif self.long_ok and c > p.upper:
                        pend_exit = "reverse"
                if pend_exit is not None:
                    blocked[side] = True
                if p.lower <= c <= p.upper:
                    blocked[1] = blocked[-1] = False
                want = 0
                if c > p.upper and side != 1 and self.long_ok:
                    want = 1
                elif c < p.lower and side != -1 and self.short_ok:
                    want = -1
                if (want and self.win[0] <= b.sm <= self.win[1] and entries < s["max_trades_per_day"]
                        and not (fresh and blocked[want])):
                    pend_entry = self._size(date, b, want, p)
            # e. the trailing stop, from the next bar
            if pos is not None and self.trail is not None and self.pos is pos:
                if pos.side == 1:
                    new = floor_tick(pos.best - self.trail * pos.dist)
                    if new > pos.stop:
                        pos.stop = new
                else:
                    new = ceil_tick(pos.best + self.trail * pos.dist)
                    if new < pos.stop:
                        pos.stop = new
        if self.pos is not None:
            raise AssertionError("position open after %s" % date)
        self.days.append({"date": date, "start": round(day_start, 2), "end": round(self.balance, 2),
                          "low": round(min(day_low, self.balance), 2)})
