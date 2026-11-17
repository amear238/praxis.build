#!/usr/bin/env python3
"""orb_engine.py -- the backtest engine for one opening range breakout variation, described by a settings dict.

Works on a list of globex.Day (research/noise-area-variations/globex.py, imported by path). sm is globex's
session minute: 09:31 is sm 931, 15:58 is 1318, 15:59 is 1319, 16:00 is 1320. Stamps mark the END of the
minute, so the bar stamped 09:31 is the 9:30 minute. Instrument MNQ: 2.00 dollars a point, 1.90 a contract
round trip, tick 0.25, slippage 2 ticks (0.5 points) per side on every market fill. This module judges
nothing: it returns trades, in the shape of the Noise-Area engine (research/noise-area-variations/engine.py)
so its bars and extras read them unchanged.

Settings (validate): exactly the fields name, reason, or_minutes, entry, entry_until, sides, stop, exit,
max_or_atr, risk_pct.
  or_minutes   5, 15 or 30 (an int). The opening range is the bars stamped 09:31 to 09:30 + n.
  entry        "direction" or "break".
  entry_until  for "break": an "HH:MM" stamp after the range's last bar and before 15:59 (so 15:58 at the
               latest), the last bar on which a break may be decided, inclusive. For "direction": null.
  sides        "both", "long" or "short".
  stop         ["far_side"], ["or_frac", x] or ["atr_frac", x], x > 0.
  exit         ["hold_to_flat"], ["target_r", x] or ["trail_r", x], x > 0.
  max_or_atr   null, or x > 0.
  risk_pct     0 < risk_pct <= 5, percent of the realised balance.

The tradable bars of a day are day.bars[: globex.tradable_end(day) + 1]: the last bar before the day's
first gap of more than 60 minutes ends the day for every trading purpose (a fill across a hole would be a
fake). The engine applies no early-close cut and no holiday calendar.

opening_range(day, n) -> (o, h, l, c), or None unless every bar stamped 09:31 .. 09:30+n is present and
inside the tradable bars. o = the 09:31 bar's open, h / l = the highest high / lowest low of those bars,
c = the last one's close. A day with no range has no trade; that is not a skip and not a filter.

atr14(days, k) -> the mean of (highest high - lowest low) over the bars stamped 09:31 to 16:00 of the 14
days before days[k] (in the list given) that have a bar stamped 09:31; None when fewer than 14 such days.
Choice: those prior days are read whole, not cut at a data hole (as the Noise-Area band is built from the
full, untrimmed days); a day counts when it has a 09:31 bar anywhere in its bars. Only days before k are
read, so there is no look-ahead.

Each day, in this order (one trade a day at most; the balance is start plus the net of every trade closed
before the decision bar, i.e. the balance at the day's start):
  1. Range. No complete range: nothing that day.
  2. Filter (max_or_atr x set): when atr14 is None or (h - l) > x * atr14, no trade and the date is added
     to `filtered`. Choice: the filter is applied as soon as the range is complete, before the side is
     looked for, so a filtered date is one whose range alone removed it (a doji range or a day with no
     break can still be filtered).
  3. stop "atr_frac" with atr14 None: no trade, not filtered, not skipped.
  4. Decision bar D, its close C.
       "direction": D is the range's last bar; long when c > o, short when c < o; none when c == o or that
       side is not allowed by sides.
       "break": D is the first tradable bar after the range, stamped no later than entry_until, whose
       close is > h (long) or < l (short). A close beyond a side that sides does not allow is ignored and
       the search goes on. No decision is made on a bar stamped after 15:58 (entry_until allows none).
  5. No entry when the bar after D (the next tradable bar) does not exist, is the day's last tradable bar,
     or is stamped 15:59 or later. That is not a skip. The search does not go on past D (no later bar
     could pass this test either).
  6. Size. dist from C: far_side long C - l, short h - C; or_frac x * (h - l); atr_frac x * atr14; rounded
     down to the tick. loss_per_contract = (dist + 0.5) * 2.0 + 1.90. qty = floor(balance * risk_pct / 100
     / loss_per_contract), at most 90; with fixed_qty set, qty = fixed_qty and the balance does not limit
     it (the measuring pass). planned_cost = qty * loss_per_contract, to the cent. dist under 10.0: skipped,
     "stop under 10 points"; qty < 1: skipped, "under one contract". A skip is one entry in `skipped`:
     {date, decision_dt, side, reason} (choice: decision_dt and side are kept beside the date and reason,
     as the Noise-Area engine does).
  7. Entry: at the next bar's open, 2 ticks against (buy +0.5, sell -0.5), kept inside that bar's range.
     The stop rests at entry -/+ dist from that bar on. exit target_r x: a target rests at entry +/- x *
     dist, rounded to the tick away from the entry.
  8. Each bar of the trade, from the entry bar, in this order:
     a. Stop. If the bar's adverse extreme reaches the stop (long: low <= stop; short: high >= stop) the
        stop fills. "kind": at the stop, or at the open when the bar opens already beyond it, 2 ticks
        against, kept inside the bar's range. "harsh-stops": at the bar's low (long) or high (short).
        "midpoint": halfway between the stop price (the open when the bar opens already beyond it) and the
        bar's low (long) or high (short), moved to the worse tick when halfway is off the tick grid, no
        further slippage. gap is True, on every model, when the open is already beyond the stop. Nothing
        else happens on that bar.
     b. Mark. The open position is marked at the bar's adverse extreme for the day's low, and the best
        price (highest high of a long, lowest low of a short, since entry, the entry bar included) is
        updated.
     c. Target. long: high >= target + 0.25; short: low <= target - 0.25: filled at the target price, no
        slippage, gap False, reason "target". A target can fill on the entry bar.
     d. Flat. On the bar stamped 15:59 or later, or on the day's last tradable bar: when the day has a next
        tradable bar the position closes at its open, 2 ticks against, kept inside that bar's range, with
        gap True when that open is already beyond the resting stop; else at this bar's close, 2 ticks
        against, kept inside the bar's range, gap False. reason "flat". Nothing else happens on that bar.
     e. Trail (exit trail_r x). At the bar's close the stop moves to best -/+ x * dist, placed on the tick
        grid away from the price (long: rounded down; short: up), and only when that is toward the price.
        It acts from the next bar.

Trade: date (trading day), side ("long"|"short"), qty, entry_dt, entry, exit_dt, exit, stop_initial, dist,
planned_cost, reason ("stop"|"target"|"flat"), gap, net = (exit - entry) * sign * 2.0 * qty - 1.90 * qty
(to the cent), r = net / planned_cost, balance (realised, after the trade).
Day: {date, start, end, low}, one per day given; low is the lowest the balance reached that day with an
open position marked at each bar's adverse extreme (commission included; step b, so not on a stop bar nor
on the bar where a flat exit fills at the open), and after every close.
digest: sha256 of json.dumps(trades, sort_keys=True).

run(days, settings, fill="midpoint", start=150000.0, fixed_qty=None) -> {"settings", "fill", "start",
"fixed_qty", "trades", "days", "skipped", "filtered", "digest"}. Choice: "fixed_qty" is kept in the result
so the independent check (orb_check.py) can verify the size without being told it.

Run as a script (python3 -I -B research/orb-150k/orb_engine.py) it runs the plan's Task 1 Step 4 settings
on the real data file and prints the count of trades and the skips; it judges nothing.

Standard library only. Run with `python3 -I -B`.
"""
import hashlib
import json
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_NAV = os.path.join(os.path.dirname(_HERE), "noise-area-variations")
if _NAV not in sys.path:
    sys.path.append(_NAV)
import globex   # noqa: E402

PV = 2.0
COMM = 1.90
TICK = 0.25
SLIP = 0.5
MIN_STOP = 10.0
MAX_QTY = 90
START = 150000.0
FILLS = ("kind", "harsh-stops", "midpoint")
DATA = os.environ.get("PRAXIS_DATA", "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt")

FIELDS = ("name", "reason", "or_minutes", "entry", "entry_until", "sides", "stop", "exit", "max_or_atr",
          "risk_pct")
OR_MINUTES = (5, 15, 30)
ENTRIES = ("direction", "break")
SIDES = ("both", "long", "short")
STOPS = {"far_side": False, "or_frac": True, "atr_frac": True}      # kind -> takes a value
EXITS = {"hold_to_flat": False, "target_r": True, "trail_r": True}
SM_0931 = globex.sm_of("09:31")
SM_1559 = globex.sm_of("15:59")
SM_1600 = globex.sm_of("16:00")


# ---------------------------------------------------------------------------------------------- settings
def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _need(ok, field, msg):
    if not ok:
        raise ValueError("%s: %s" % (field, msg))


def _order(field, v, kinds):
    _need(isinstance(v, (list, tuple)) and len(v) >= 1, field, "must be a list like [kind] or [kind, x], got %r" % (v,))
    _need(v[0] in kinds, field, "kind must be one of %s, got %r" % (sorted(kinds), v[0]))
    if kinds[v[0]]:
        _need(len(v) == 2 and _num(v[1]) and v[1] > 0, field, "%s takes one value above 0, got %r" % (v[0], v))
    else:
        _need(len(v) == 1, field, "%s takes no value, got %r" % (v[0], v))


def validate(settings):
    """-> None, or raise ValueError naming the first bad field."""
    s = settings
    _need(isinstance(s, dict), "settings", "must be a dict")
    extra = sorted(set(s) - set(FIELDS))
    _need(not extra, ",".join(extra), "unknown field")
    missing = [f for f in FIELDS if f not in s]
    _need(not missing, ",".join(missing), "missing field")
    _need(isinstance(s["name"], str) and s["name"] != "", "name", "must be a non-empty string")
    _need(isinstance(s["reason"], str), "reason", "must be a string")
    n = s["or_minutes"]
    _need(isinstance(n, int) and not isinstance(n, bool) and n in OR_MINUTES, "or_minutes",
          "must be one of %s, got %r" % (OR_MINUTES, n))
    _need(s["entry"] in ENTRIES, "entry", "must be one of %s, got %r" % (ENTRIES, s["entry"]))
    u = s["entry_until"]
    if s["entry"] == "break":
        _need(isinstance(u, str) and len(u) == 5 and u[2] == ":" and (u[:2] + u[3:]).isdigit(), "entry_until",
              "must be an 'HH:MM' stamp for break, got %r" % (u,))
        try:
            sm = globex.sm_of(u)
        except ValueError:
            sm = None
        _need(sm is not None and SM_0931 + n - 1 < sm < SM_1559, "entry_until",
              "must be after the range and before 15:59, got %r" % (u,))
    else:
        _need(u is None, "entry_until", "must be null for direction, got %r" % (u,))
    _need(s["sides"] in SIDES, "sides", "must be one of %s, got %r" % (SIDES, s["sides"]))
    _order("stop", s["stop"], STOPS)
    _order("exit", s["exit"], EXITS)
    m = s["max_or_atr"]
    _need(m is None or (_num(m) and m > 0), "max_or_atr", "must be null or above 0, got %r" % (m,))
    _need(_num(s["risk_pct"]) and 0 < s["risk_pct"] <= 5, "risk_pct", "must be above 0 and at most 5")


# ---------------------------------------------------------------------------------------------- prices
def floor_tick(x):
    return math.floor(x / TICK + 1e-9) * TICK


def ceil_tick(x):
    return math.ceil(x / TICK - 1e-9) * TICK


def loss_per_contract(dist):
    return (dist + SLIP) * PV + COMM


def _clamp(x, b):
    return b.l if x < b.l else b.h if x > b.h else x


def _market(b, side_of_order):
    """Market fill at bar b's open; side_of_order +1 buys, -1 sells."""
    return _clamp(b.o + SLIP * side_of_order, b)


# ---------------------------------------------------------------------------------------------- range, atr
def _range_index(day, n):
    """-> (index of the range's first bar, index of its last bar), or None (module docstring)."""
    last = globex.tradable_end(day) if day.bars else -1
    idx = []
    for sm in range(SM_0931, SM_0931 + n):
        i = day.by_sm.get(sm)
        if i is None or i > last:
            return None
        idx.append(i)
    return idx[0], idx[-1]


def opening_range(day, n):
    r = _range_index(day, n)
    if r is None:
        return None
    bars = day.bars[r[0]:r[1] + 1]
    return (bars[0].o, max(b.h for b in bars), min(b.l for b in bars), bars[-1].c)


def _rth_range(day):
    """-> highest high - lowest low of the bars stamped 09:31 to 16:00, or None without a 09:31 bar."""
    if SM_0931 not in day.by_sm:
        return None
    bars = [b for b in day.bars if SM_0931 <= b.sm <= SM_1600]
    return max(b.h for b in bars) - min(b.l for b in bars)


def atr14(days, k):
    got = []
    for j in range(k - 1, -1, -1):
        r = _rth_range(days[j])
        if r is not None:
            got.append(r)
            if len(got) == 14:
                return sum(got) / 14.0
    return None


def _atr_series(days):
    """atr14 for every k, in one pass."""
    out, window = [], []
    for d in days:
        out.append(sum(window) / 14.0 if len(window) == 14 else None)
        r = _rth_range(d)
        if r is not None:
            window.append(r)
            if len(window) > 14:
                window.pop(0)
    return out


# ---------------------------------------------------------------------------------------------- the run
def run(days, settings, fill="midpoint", start=START, fixed_qty=None):
    """Simulate one variation over `days` (a list of globex.Day in date order; earlier days feed atr14)."""
    validate(settings)
    if fill not in FILLS:
        raise ValueError("fill must be one of %s, got %r" % (FILLS, fill))
    if fixed_qty is not None and not (isinstance(fixed_qty, int) and not isinstance(fixed_qty, bool)
                                      and fixed_qty >= 1):
        raise ValueError("fixed_qty must be null or an integer of at least 1, got %r" % (fixed_qty,))
    sim = _Sim(settings, fill, float(start), fixed_qty)
    atrs = _atr_series(days)
    for k, d in enumerate(days):
        sim.day(d, atrs[k])
    digest = hashlib.sha256(json.dumps(sim.trades, sort_keys=True).encode()).hexdigest()
    return {"settings": settings, "fill": fill, "start": float(start), "fixed_qty": fixed_qty,
            "trades": sim.trades, "days": sim.days, "skipped": sim.skipped, "filtered": sim.filtered,
            "digest": digest}


class _Sim(object):
    def __init__(self, s, fill, start, fixed_qty):
        self.s, self.fill, self.balance, self.fixed_qty = s, fill, start, fixed_qty
        self.n = s["or_minutes"]
        self.long_ok = s["sides"] in ("both", "long")
        self.short_ok = s["sides"] in ("both", "short")
        self.until = globex.sm_of(s["entry_until"]) if s["entry"] == "break" else None
        self.stop_kind = s["stop"][0]
        self.stop_x = s["stop"][1] if len(s["stop"]) > 1 else None
        self.exit_kind = s["exit"][0]
        self.exit_x = s["exit"][1] if len(s["exit"]) > 1 else None
        self.trades, self.days, self.skipped, self.filtered = [], [], [], []

    def _decision(self, bars, last, r_last, o, h, l, c):
        """-> (index of D, side) or None."""
        if self.s["entry"] == "direction":
            side = 1 if c > o else -1 if c < o else 0
            if (side == 1 and not self.long_ok) or (side == -1 and not self.short_ok) or side == 0:
                return None
            return r_last, side
        for i in range(r_last + 1, last + 1):
            b = bars[i]
            if b.sm > self.until:
                return None
            if b.c > h and self.long_ok:
                return i, 1
            if b.c < l and self.short_ok:
                return i, -1
        return None

    def _dist(self, side, C, h, l, atr):
        if self.stop_kind == "far_side":
            x = C - l if side == 1 else h - C
        elif self.stop_kind == "or_frac":
            x = self.stop_x * (h - l)
        else:
            x = self.stop_x * atr
        return floor_tick(x)

    def _stop_fill(self, b, side, stop):
        if side == 1:
            gap = b.o < stop
            if self.fill == "harsh-stops":
                px = b.l
            elif self.fill == "midpoint":
                px = floor_tick((min(stop, b.o) + b.l) / 2.0)
            else:
                px = _clamp(min(stop, b.o) - SLIP, b)
        else:
            gap = b.o > stop
            if self.fill == "harsh-stops":
                px = b.h
            elif self.fill == "midpoint":
                px = ceil_tick((max(stop, b.o) + b.h) / 2.0)
            else:
                px = _clamp(max(stop, b.o) + SLIP, b)
        return px, gap

    def day(self, day, atr):
        date = day.date
        day_start = day_low = self.balance
        self._trade(day, atr, date)
        day_low = min(day_low, self._low, self.balance)
        self.days.append({"date": date, "start": round(day_start, 2), "end": round(self.balance, 2),
                          "low": round(day_low, 2)})

    def _trade(self, day, atr, date):
        self._low = self.balance
        r = _range_index(day, self.n)
        if r is None:
            return
        last = globex.tradable_end(day)
        bars = day.bars[:last + 1]
        rb = bars[r[0]:r[1] + 1]
        o, h, l, c = rb[0].o, max(b.h for b in rb), min(b.l for b in rb), rb[-1].c
        mx = self.s["max_or_atr"]
        if mx is not None and (atr is None or (h - l) > mx * atr):
            self.filtered.append(date)
            return
        if self.stop_kind == "atr_frac" and atr is None:
            return
        dec = self._decision(bars, last, r[1], o, h, l, c)
        if dec is None:
            return
        i, side = dec
        if i + 1 >= last or bars[i + 1].sm >= SM_1559:
            return
        D = bars[i]
        dist = self._dist(side, D.c, h, l, atr)
        why = None
        lpc = loss_per_contract(dist)
        if dist < MIN_STOP:
            why = "stop under 10 points"
        elif self.fixed_qty is not None:
            qty = self.fixed_qty
        else:
            qty = min(int(math.floor(self.balance * self.s["risk_pct"] / 100.0 / lpc + 1e-9)), MAX_QTY)
            if qty < 1:
                why = "under one contract"
        if why is not None:
            self.skipped.append({"date": date, "decision_dt": D.dt.isoformat(" "),
                                 "side": "long" if side == 1 else "short", "reason": why})
            return
        planned = round(qty * lpc, 2)
        i0 = i + 1
        E = bars[i0]
        entry = _market(E, side)
        stop = stop_initial = entry - side * dist
        target = None
        if self.exit_kind == "target_r":
            target = (ceil_tick if side == 1 else floor_tick)(entry + side * self.exit_x * dist)
        trail = self.exit_x if self.exit_kind == "trail_r" else None
        best = entry
        low = self.balance
        j = i0
        while True:
            b = bars[j]
            # a. the resting stop
            if (b.l <= stop) if side == 1 else (b.h >= stop):
                px, gap = self._stop_fill(b, side, stop)
                reason, xb = "stop", b
                break
            # b. mark and best
            x = b.l if side == 1 else b.h
            low = min(low, self.balance + (x - entry) * side * PV * qty - COMM * qty)
            best = max(best, b.h) if side == 1 else min(best, b.l)
            # c. target
            if target is not None and ((b.h >= target + TICK) if side == 1 else (b.l <= target - TICK)):
                px, gap, reason, xb = target, False, "target", b
                break
            # d. flat
            if b.sm >= SM_1559 or j == last:
                if j < last:
                    xb = bars[j + 1]
                    px = _market(xb, -side)
                    gap = (xb.o < stop) if side == 1 else (xb.o > stop)
                else:
                    xb = b
                    px = _clamp(b.c - SLIP * side, b)
                    gap = False
                reason = "flat"
                break
            # e. trail, from the next bar
            if trail is not None:
                if side == 1:
                    new = floor_tick(best - trail * dist)
                    if new > stop:
                        stop = new
                else:
                    new = ceil_tick(best + trail * dist)
                    if new < stop:
                        stop = new
            j += 1
        net = round((px - entry) * side * PV * qty - COMM * qty, 2)
        self.balance = round(self.balance + net, 2)
        self._low = min(low, self.balance)
        self.trades.append({
            "date": date, "side": "long" if side == 1 else "short", "qty": qty,
            "entry_dt": E.dt.isoformat(" "), "entry": entry, "exit_dt": xb.dt.isoformat(" "), "exit": px,
            "stop_initial": stop_initial, "dist": dist, "planned_cost": planned, "reason": reason,
            "gap": gap, "net": net, "r": net / planned, "balance": self.balance})


# ---------------------------------------------------------------------------------------------- script
STEP4 = {"name": "step4", "reason": "plan Task 1 Step 4: near candidate 2", "or_minutes": 5,
         "entry": "direction", "entry_until": None, "sides": "both", "stop": ["far_side"],
         "exit": ["target_r", 10], "max_or_atr": None, "risk_pct": 1.0}


def main():
    days = globex.load_days(DATA)
    res = run(days, STEP4, fill="harsh-stops", start=50000.0)
    reasons = {}
    for x in res["skipped"]:
        reasons[x["reason"]] = reasons.get(x["reason"], 0) + 1
    print("days %d, trades %d, skipped %d %s, filtered %d, digest %s"
          % (len(days), len(res["trades"]), len(res["skipped"]), json.dumps(reasons, sort_keys=True),
             len(res["filtered"]), res["digest"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
