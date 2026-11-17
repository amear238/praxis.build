#!/usr/bin/env python3
"""gates.py -- the five bars for one engine result, and the rule check that replays its trades.

Works on the result of engine.run ({"settings", "fill", "start", "trades", "days", "skipped", "digest"}).
This module judges; it simulates nothing. sm is globex's session minute (18:01 is sm 1, 16:00 is sm 1320).

rule_check(result, days) -> list of breaks (strings), empty when clean. An independent replay: it uses
globex for the days and bands.day_bands for the band, and nothing of engine.py, so a bug in the engine is
not copied into its own check. The rules are recomputed from their written definitions (engine.py's
docstring and the plan's Task 5 and Task 6). Instrument MNQ: 2.00 a point, 1.90 a contract round trip,
tick 0.25, 2 ticks (0.5 points) slippage per side; a market fill is kept inside its bar's range. For each
trade, on the day.bars[: globex.tradable_end(day) + 1] of its trading day:
  * Entry. The entry bar is the bar stamped entry_dt; the decision bar is the tradable bar just before it.
    The decision bar has a band point, is stamped :00 or :30 when the cadence is "half_hour", is stamped
    before flat_time, and is not a bar where a stop filled. The side is allowed by `sides`; the decision
    close is above the upper line (long) or below the lower line (short). The entry bar is stamped before
    flat_time and is not the day's last tradable bar. The decision bar's stamp is
    inside entry_window. The trade is at most the max_trades_per_day-th of its date. The previous trade
    is closed before the entry bar and is not on the same side at the decision bar. reentry "fresh": after
    an exit on the same side the same day, a decision bar closed inside the band (lower <= C <= upper):
    after a stop, one after the stop bar; after a decided exit, the exit's own decision bar or a later
    one, before this trade's decision bar.
  * Stop and size. A stop at entry: stop_initial and dist are set. dist = the stop kind's distance from
    the decision close, rounded down to a tick, and at least 10.0. stop_initial = entry -/+ dist. The
    balance for the size is result["start"] plus the net of every trade whose exit_dt is at or before the
    decision bar's stamp. loss per contract = (dist + 0.5) * 2.0 + 1.90; qty = floor(balance * risk_pct /
    100 / that); planned_cost = qty * that, to the cent.
  * Entry fill: the entry bar's open, 2 ticks against, kept inside the bar's range.
  * The life of the trade, bar by bar from the entry bar: the resting stop (stop_initial, moved by the
    trailing rule when the exit is "trail_r": the highest high / lowest low since entry, entry bar
    included, -/+ value * dist, on the tick grid away from the price, only toward the price, from the next
    bar) fills on the first bar whose adverse extreme reaches it (kind: at the stop, or at the open when the
    bar opens beyond it, 2 ticks against, inside the bar; harsh-stops: the bar's low / high; midpoint:
    halfway between the stop (the open when the bar opens beyond it) and the bar's low / high, to the worse
    tick, no further slippage; gap when the open is beyond the stop); else on the bar stamped flat_time or later, or the day's last tradable bar,
    the position closes at the next bar's open (or at that last bar's close), 2 ticks against; else on a
    decision bar the exit rule ("band_or_vwap" only: long C <= max(upper, vwap), short C >= min(lower,
    vwap)) gives "exit", and the opposite signal (with that side allowed) gives "reverse", both filled at
    the next bar's open, 2 ticks against; such a decided exit has gap true when that open is already
    beyond the stop resting there (the trailed stop included). The trade's reason, exit_dt, exit and gap
    must be the replay's.
    Its exit is no later than the bar stamped 16:00 of its date and inside the day's tradable bars.
  * Money: net = (exit - entry) * sign * 2.0 * qty - 1.90 * qty, to the cent; r = net / planned_cost;
    balance = the realised balance after the trade, trade by trade in list order.
  * On a "kind" result: a trade of any reason with gap false and a loss above planned_cost by more than
    one cent is a break.
And the day dicts the survival bar reads: one per day given, in order; start = the previous day's end (the
first is result["start"]); end = the realised balance after the day's trades; low = the lowest of the
start, the open position marked at each bar's adverse extreme (commission included) on every bar it is
open at the stop check and not stopped, and the balance after every close; all to the cent.

judge(result, all_dates) -> the five bars, separately, and the statistics (see judge). The rule-check
outcome is read from result["rule_breaks"], which run_all.py puts there; when it is absent the bar fails
with breaks -1. Survival uses trailing and shuffled from research/intraday-momentum-long/run.py unchanged.

Standard library only. Run with `python3 -I -B`.
"""
import bisect
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
_IML = os.path.join(os.path.dirname(_HERE), "intraday-momentum-long")
if _IML not in sys.path:
    sys.path.insert(1, _IML)
import bands    # noqa: E402  (called as bands.day_bands, so a test can stand a band in)
import globex   # noqa: E402
import run as _candidate1   # noqa: E402  research/intraday-momentum-long/run.py, unchanged

trailing = _candidate1.trailing
shuffled = _candidate1.shuffled

LATER_FROM = "2024-01-01"
LIMIT = 2000.0
SHUFFLE_RUNS, SHUFFLE_SEED = 10000, 20261115
MAX_GAP_DAYS = 7
SHUFFLE_PCT_MAX = 5.0
MIN_AVG_WINNER_R = 2.0

PV, COMM, TICK, SLIP = 2.0, 1.90, 0.25, 0.5
MIN_STOP = 10.0
CENT = 0.01
EPS = 1e-9
SM_1600 = globex.sm_of("16:00")


# ---------------------------------------------------------------------------------------------- rule check
def _floor_tick(x):
    return math.floor(x / TICK + EPS) * TICK


def _ceil_tick(x):
    return math.ceil(x / TICK - EPS) * TICK


def _inside(x, b):
    return min(max(x, b.l), b.h)


def _beyond(b, stop, sign):
    """True when bar b opens already beyond the resting stop (long: open < stop; short: open > stop)."""
    return stop is not None and (b.o < stop if sign == 1 else b.o > stop)


def _same(a, b):
    return a is not None and b is not None and abs(a - b) <= EPS


def _dist(kind, value, sign, close, p):
    if kind == "half_width":
        x = p.width / 2.0
    elif kind == "full_width":
        x = p.width
    elif kind == "width_frac":
        x = value * p.width
    elif kind == "to_anchor":
        x = close - p.anchor_price if sign == 1 else p.anchor_price - close
    elif kind == "opposite_band":
        x = close - p.lower if sign == 1 else p.upper - close
    else:
        return None                     # stop kind "none" or unknown: no distance
    return _floor_tick(x)


class _DayView(object):
    """A trading day's tradable bars, its band and the bars where a stop filled."""

    def __init__(self, days, k, s, stop_stamps):
        self.day = days[k]
        self.last = globex.tradable_end(self.day)
        self.bars = self.day.bars[:self.last + 1]
        self.idx = {b.dt.isoformat(" "): i for i, b in enumerate(self.bars)}
        self.all_stamps = {b.dt.isoformat(" ") for b in self.day.bars}
        self.bmap = bands.day_bands(days, k, s["anchor"], s["lookback"], s["band_mult"])
        self.stop_stamps = stop_stamps
        self.flat_sm = globex.sm_of(s["flat_time"])
        self.half_hour = s["cadence"] == "half_hour"

    def stamp(self, i):
        return self.bars[i].dt.isoformat(" ")

    def is_decision(self, i):
        """True when bar i is a decision bar: a band point, on the cadence, before the flat, not a stop bar."""
        b = self.bars[i]
        return (b.sm in self.bmap and (not self.half_hour or b.dt.minute in (0, 30)) and b.sm < self.flat_sm
                and i != self.last and self.stamp(i) not in self.stop_stamps)


def _replay(v, s, fill, t, i0, sign, stop):
    """The trade's life from entry bar i0 -> (reason, exit index, exit price, gap, last bar marked open)."""
    bars = v.bars
    trail = s["exit"].get("value") if s["exit"]["kind"] == "trail_r" else None
    band_exit = s["exit"]["kind"] == "band_or_vwap"
    long_ok = s["sides"] in ("both", "long")
    short_ok = s["sides"] in ("both", "short")
    best = t["entry"]
    i = i0
    while True:
        b = bars[i]
        if stop is not None and (b.l <= stop if sign == 1 else b.h >= stop):
            gap = b.o < stop if sign == 1 else b.o > stop
            if fill == "harsh-stops":
                px = b.l if sign == 1 else b.h
            elif fill == "midpoint":
                ref = min(stop, b.o) if sign == 1 else max(stop, b.o)
                worst = b.l if sign == 1 else b.h
                half = (ref + worst) / 2.0
                px = _floor_tick(half) if sign == 1 else _ceil_tick(half)
            else:
                px = _inside(min(stop, b.o) - SLIP, b) if sign == 1 else _inside(max(stop, b.o) + SLIP, b)
            return "stop", i, px, gap, i - 1
        best = max(best, b.h) if sign == 1 else min(best, b.l)
        if b.sm >= v.flat_sm or i == v.last:
            if i < v.last:
                n = bars[i + 1]
                return "flat", i + 1, _inside(n.o - SLIP * sign, n), _beyond(n, stop, sign), i
            return "flat", i, _inside(b.c - SLIP * sign, b), False, i
        p = v.bmap.get(b.sm)
        why = None
        if p is not None and (not v.half_hour or b.dt.minute in (0, 30)):
            c = b.c
            if sign == 1:
                if band_exit and c <= max(p.upper, p.vwap):
                    why = "exit"
                elif short_ok and c < p.lower:
                    why = "reverse"
            else:
                if band_exit and c >= min(p.lower, p.vwap):
                    why = "exit"
                elif long_ok and c > p.upper:
                    why = "reverse"
        if trail is not None and stop is not None and t["dist"] is not None:
            if sign == 1:
                new = _floor_tick(best - trail * t["dist"])
                if new > stop:
                    stop = new
            else:
                new = _ceil_tick(best + trail * t["dist"])
                if new < stop:
                    stop = new
        if why is not None:                       # filled at the next open; the stop resting there decides gap
            n = bars[i + 1]
            return why, i + 1, _inside(n.o - SLIP * sign, n), _beyond(n, stop, sign), i
        i += 1


def rule_check(result, days):
    """-> list of breaks, one line each; empty when every trade obeys the written rules (module docstring)."""
    s, fill, start = result["settings"], result["fill"], float(result["start"])
    trades = result["trades"]
    k_of = {d.date: k for k, d in enumerate(days)}
    stop_stamps = {}
    for t in trades:
        if t["reason"] == "stop":
            stop_stamps.setdefault(t["date"], set()).add(t["exit_dt"])
    views = {}
    win = (globex.sm_of(s["entry_window"][0]), globex.sm_of(s["entry_window"][1]))
    long_ok = s["sides"] in ("both", "long")
    short_ok = s["sides"] in ("both", "short")
    stop_kind, stop_value = s["stop"]["kind"], s["stop"].get("value")
    out = []
    open_bars = {}                               # trade index -> the bars on which it is marked open
    per_date = {}
    bal = start
    # The realised balance at a stamp: start plus the net of every trade with exit_dt at or before it.
    by_exit = sorted(trades, key=lambda x: x["exit_dt"])
    exit_stamps, realised, b = [], [], start
    for x in by_exit:
        b = round(b + x["net"], 2)
        exit_stamps.append(x["exit_dt"])
        realised.append(b)

    for n, t in enumerate(trades):
        lines = []
        sign = 1 if t["side"] == "long" else -1

        def br(msg):
            lines.append("%s %s entered %s: %s" % (t["date"], t["side"], t["entry_dt"], msg))

        # Money, trade by trade in list order.
        if t["qty"] is not None and t["entry"] is not None and t["exit"] is not None:
            want = round((t["exit"] - t["entry"]) * sign * PV * t["qty"] - COMM * t["qty"], 2)
            if not _same(want, t["net"]):
                br("net does not match: %r, the fills give %r" % (t["net"], want))
        if t["planned_cost"]:
            if t["r"] is None or abs(t["r"] - t["net"] / t["planned_cost"]) > 1e-12:
                br("r does not match: %r, net / planned_cost is %r" % (t["r"], t["net"] / t["planned_cost"]))
        bal = round(bal + t["net"], 2)
        if not _same(bal, t["balance"]):
            br("balance does not match: %r, the realised balance is %r" % (t["balance"], bal))
        # Stop at entry.
        if t["stop_initial"] is None or t["dist"] is None:
            br("no stop at entry")
        elif not _same(t["stop_initial"], t["entry"] - sign * t["dist"]):
            br("stop_initial is not dist from the entry: %r, entry %r, dist %r"
               % (t["stop_initial"], t["entry"], t["dist"]))
        if t["dist"] is not None and t["dist"] < MIN_STOP:
            br("dist under 10 points: %r" % (t["dist"],))
        # kind: no loss above the planned cost, whatever the reason, except on a gap.
        if (fill == "kind" and not t["gap"] and t["planned_cost"] is not None
                and -t["net"] - t["planned_cost"] > CENT + EPS):
            br("loss above the planned cost (reason %s): net %r, planned %r"
               % (t["reason"], t["net"], t["planned_cost"]))
        # Most trades a day.
        per_date[t["date"]] = per_date.get(t["date"], 0) + 1
        if per_date[t["date"]] > s["max_trades_per_day"]:
            br("over max_trades_per_day: trade %d of the day, most %d" % (per_date[t["date"]],
                                                                          s["max_trades_per_day"]))
        if t["exit_dt"] > t["date"] + " 16:00:00":
            br("exit after the 16:00 bar: %s" % (t["exit_dt"],))
        # One position at a time.
        prev = trades[n - 1] if n > 0 else None
        if prev is not None and prev["exit_dt"] > t["entry_dt"]:
            br("opened while another position was open (exit %s)" % (prev["exit_dt"],))

        # The bars.
        k = k_of.get(t["date"])
        if k is None:
            br("not a loaded day")
            out.extend(lines)
            continue
        if t["date"] not in views:
            views[t["date"]] = _DayView(days, k, s, stop_stamps.get(t["date"], set()))
        v = views[t["date"]]
        i0 = v.idx.get(t["entry_dt"])
        if i0 is None or i0 == 0:
            br("entry not at a tradable bar of its day after a decision bar")
            out.extend(lines)
            continue
        j = i0 - 1
        d, e = v.bars[j], v.bars[i0]
        dstamp = v.stamp(j)
        # Decision bar.
        if d.sm >= v.flat_sm or e.sm >= v.flat_sm:
            br("entry at or after flat_time: decided %s, filled %s, flat_time %s"
               % (dstamp, t["entry_dt"], s["flat_time"]))
        if i0 == v.last:
            br("entry on the day's last tradable bar: %s" % (t["entry_dt"],))
        if dstamp in v.stop_stamps:
            br("decided on a bar where a stop filled: %s" % (dstamp,))
        if v.half_hour and d.dt.minute not in (0, 30):
            br("decision bar not on the half-hour cadence: %s" % (dstamp,))
        p = v.bmap.get(d.sm)
        if not (long_ok if sign == 1 else short_ok):
            br("side not allowed by sides %r" % (s["sides"],))
        if p is None:
            br("no band at the decision bar %s" % (dstamp,))
        elif not (d.c > p.upper if sign == 1 else d.c < p.lower):
            br("entry signal not true at the decision bar %s: close %r, band %r to %r"
               % (dstamp, d.c, p.lower, p.upper))
        if not (win[0] <= d.sm <= win[1]):
            br("entry outside entry_window: decided %s" % (dstamp,))
        if prev is not None and prev["side"] == t["side"] and prev["exit_dt"] > dstamp:
            br("entered while already on that side (previous exit %s)" % (prev["exit_dt"],))
        if s["reentry"] == "fresh":
            _fresh(v, trades, n, t, j, br)
        # Distance and size.
        if p is not None and t["dist"] is not None:
            want = _dist(stop_kind, stop_value, sign, d.c, p)
            if not _same(want, t["dist"]):
                br("dist does not match the stop distance at the decision bar: %r, the rule gives %r"
                   % (t["dist"], want))
            if want is not None and want >= MIN_STOP:
                m = bisect.bisect_right(exit_stamps, dstamp)
                basis = realised[m - 1] if m else start
                lpc = (want + SLIP) * PV + COMM
                qty = int(math.floor(basis * s["risk_pct"] / 100.0 / lpc + EPS))
                if qty != t["qty"]:
                    br("qty does not match the size rule: %r, balance %r gives %r" % (t["qty"], basis, qty))
                if t["planned_cost"] is None or abs(round(qty * lpc, 2) - t["planned_cost"]) > EPS:
                    br("planned_cost does not match the size rule: %r, the rule gives %r"
                       % (t["planned_cost"], round(qty * lpc, 2)))
        # Entry fill.
        if not _same(t["entry"], _inside(e.o + SLIP * sign, e)):
            br("entry fill is not the entry bar's open 2 ticks against: %r, open %r" % (t["entry"], e.o))
        # The life of the trade.
        ix = v.idx.get(t["exit_dt"])
        if ix is None:
            if t["exit_dt"] in v.all_stamps:
                br("open across the end of the day's tradable bars: exit %s, last tradable bar %s"
                   % (t["exit_dt"], v.stamp(v.last)))
            else:
                br("exit not at a tradable bar of its day: %s" % (t["exit_dt"],))
        elif ix < i0:
            br("exit before the entry: %s" % (t["exit_dt"],))
        else:
            reason, wi, px, gap, marked = _replay(v, s, fill, t, i0, sign, t["stop_initial"])
            open_bars[n] = v.bars[i0:marked + 1]
            got = (t["reason"], t["exit_dt"], t["exit"], bool(t["gap"]))
            if reason == "stop" and wi < ix:
                br("bar %s reached the stop before the exit" % (v.stamp(wi),))
            if t["reason"] == "stop" and not (reason == "stop" and wi == ix):
                br("stop exit at a bar that did not reach the stop first: %s" % (t["exit_dt"],))
            if not (got[0] == reason and got[1] == v.stamp(wi) and _same(got[2], px) and got[3] == gap):
                br("exit does not match the rules: got %r, the rules give %r"
                   % (got, (reason, v.stamp(wi), px, gap)))
        out.extend(lines)
    out.extend(_day_lines(result, days, open_bars))
    return out


def _day_lines(result, days, open_bars):
    """The day dicts: one per day given, in order; start = the previous end; end = the realised balance after
    the day's trades; low = the lowest of the start, the open position marked at each bar's adverse extreme
    (commission included) and the balance after every close, to the cent."""
    out = []
    got = result["days"]
    if [d["date"] for d in got] != [d.date for d in days]:
        return ["days: the day list is not one entry per loaded day, in order"]
    by_date = {}
    for n, t in enumerate(result["trades"]):
        by_date.setdefault(t["date"], []).append(n)
    bal = float(result["start"])
    for d in got:
        start, low = bal, bal
        for n in by_date.get(d["date"], []):
            t = result["trades"][n]
            sign = 1 if t["side"] == "long" else -1
            for b in open_bars.get(n, []):
                x = b.l if sign == 1 else b.h
                low = min(low, bal + (x - t["entry"]) * sign * PV * t["qty"] - COMM * t["qty"])
            bal = round(bal + t["net"], 2)
            low = min(low, bal)
        want = {"start": round(start, 2), "end": round(bal, 2), "low": round(low, 2)}
        for key in ("start", "end", "low"):
            if not _same(d[key], want[key]):
                out.append("day %s: %s %r, the replay gives %r" % (d["date"], key, d[key], want[key]))
    return out


def _fresh(v, trades, n, t, j, br):
    """reentry "fresh": a same-side exit earlier the same day must be followed by a close inside the band."""
    prev = None
    for m in range(n - 1, -1, -1):
        q = trades[m]
        if q["date"] != t["date"]:
            break
        if q["side"] == t["side"]:
            prev = q
            break
    if prev is None:
        return
    e = v.idx.get(prev["exit_dt"])
    if e is None:
        return                                    # reported on that trade
    first = e + 1 if prev["reason"] == "stop" else e - 1
    for i in range(max(first, 0), j):
        if v.is_decision(i):
            p = v.bmap[v.bars[i].sm]
            if p.lower <= v.bars[i].c <= p.upper:
                return
    br("reentry fresh: no decision bar closed inside the band after the %s exit at %s"
       % (prev["reason"], prev["exit_dt"]))


# ---------------------------------------------------------------------------------------------- the bars
def _mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def _net(trades):
    return round(sum(t["net"] for t in trades), 2)


def _two_to_one(trades):
    win = [t["r"] for t in trades if t["net"] > 0]
    later = [t for t in trades if t["date"] >= LATER_FROM]
    later_win = [t["r"] for t in later if t["net"] > 0]
    avg, later_avg, later_net = _mean(win), _mean(later_win), _net(later)
    return {"pass": avg >= MIN_AVG_WINNER_R and later_avg >= MIN_AVG_WINNER_R and later_net > 0,
            "avg_winner_r": avg, "later_avg_winner_r": later_avg, "later_net": later_net}


def _frequency(trades, all_dates):
    entered = {t["date"] for t in trades}
    best, best_from, best_to = 0, None, None
    run, run_from = 0, None
    for d in all_dates:
        if d in entered:
            run = 0
            continue
        if run == 0:
            run_from = d
        run += 1
        if run > best:
            best, best_from, best_to = run, run_from, d
    return {"pass": best <= MAX_GAP_DAYS, "max_gap_trading_days": best, "gap_from": best_from, "gap_to": best_to}


def _survival(result, limit=LIMIT):
    tr = trailing(result["days"], start=result["start"], limit=limit)
    sh = shuffled(result["days"], runs=SHUFFLE_RUNS, seed=SHUFFLE_SEED, start=result["start"], limit=limit)
    # Exact: at most 5% of the runs cross. shuffled()'s own "pct" is rounded to 0.1 and is not used.
    return {"pass": tr["first_cross"] is None and sh["crossed"] * 100 <= SHUFFLE_PCT_MAX * sh["runs"],
            "first_cross": tr["first_cross"], "shuffle_pct": 100.0 * sh["crossed"] / sh["runs"]}


def _stats(result):
    trades = result["trades"]
    wins = [t for t in trades if t["net"] > 0]
    losses = [t for t in trades if t["net"] < 0]
    longest = cur = 0
    for t in trades:
        cur = cur + 1 if t["net"] < 0 else 0
        longest = max(longest, cur)
    high, drop = result["start"], 0.0
    for d in result["days"]:
        drop = max(drop, high - d["low"])
        high = max(high, d["end"])
    over = [t for t in trades if t["planned_cost"] and -t["net"] - t["planned_cost"] > CENT + EPS]
    by_year = {}
    for y in sorted({t["date"][:4] for t in trades}):
        ty = [t for t in trades if t["date"][:4] == y]
        wy = [t["r"] for t in ty if t["net"] > 0]
        by_year[y] = {"trades": len(ty), "net": _net(ty), "win_pct": round(100.0 * len(wy) / len(ty), 1),
                      "avg_winner_r": round(_mean(wy), 3)}
    return {
        "trades": len(trades),
        "win_pct": round(100.0 * len(wins) / len(trades), 1) if trades else 0.0,
        "avg_winner_dollars": round(_mean([t["net"] for t in wins]), 2),
        "avg_loser_dollars": round(_mean([t["net"] for t in losses]), 2),
        "avg_loser_r": round(_mean([t["r"] for t in losses]), 3),
        "longest_losing_run": longest,
        "worst_drop_dollars": round(drop, 2),
        "skipped": len(result["skipped"]),
        "stops_over_planned": len(over),
        "worst_stop_vs_planned": round(max(-t["net"] / t["planned_cost"] for t in over), 4) if over else None,
        "by_year": by_year,
    }


def judge(result, all_dates, limit=LIMIT):
    """-> {"rule_check", "two_to_one", "frequency", "profit", "survival", "overall", "stats"}.

    rule_check: from result["rule_breaks"] (absent: a fail, breaks -1).
    two_to_one: winners are trades with net > 0; pass when their mean r >= 2.0, the mean r of the winners
                dated LATER_FROM or later >= 2.0, and the net of the trades dated LATER_FROM or later > 0.
    frequency:  the longest run of consecutive dates of all_dates with no trade entered (a trade's date);
                pass when <= 7. gap_from / gap_to are the run's first and last date (None when no gap).
                judge uses the all_dates it is given. The calendar the rule means starts at the first
                trading day on which the variation's band exists and runs to the last day loaded (runs at
                its start and end count); run_all.band_dates builds it.
    limit:      the trailing limit in dollars; 2,000 unless given (4,500 for the 150,000 frame).
    profit:     pass when the net of all trades (to the cent) >= 2 * limit.
    survival:   trailing and shuffled (10,000 runs, seed 20261115) on result["days"] from result["start"]
                with the limit; pass when the real order never crosses and crossed * 100 <= 5 *
                runs (at most 500 of 10,000). shuffle_pct = 100 * crossed / runs, unrounded.
    stats:      dollars to the cent, percentages to 0.1, R to 0.001 (worst_stop_vs_planned to 0.0001).
                stops_over_planned counts every trade, whatever its reason, whose loss is above its
                planned_cost by more than one cent; worst_stop_vs_planned is the largest loss / planned_cost
                among them (None when there is none).
    """
    rb = result.get("rule_breaks")
    out = {"rule_check": {"pass": False, "breaks": -1} if rb is None else {"pass": not rb, "breaks": len(rb)}}
    trades = result["trades"]
    out["two_to_one"] = _two_to_one(trades)
    out["frequency"] = _frequency(trades, all_dates)
    net = _net(trades)
    out["profit"] = {"pass": net >= 2 * limit, "net": net}
    out["survival"] = _survival(result, limit)
    out["overall"] = all(out[k]["pass"] for k in ("rule_check", "two_to_one", "frequency", "profit", "survival"))
    out["stats"] = _stats(result)
    return out
