#!/usr/bin/env python3
"""orb_check.py -- the independent rule check for one opening range breakout result.

rule_check(result, days) -> list of breaks (strings), empty when clean. It works on the result of
orb_engine.run ({"settings", "fill", "start", "fixed_qty", "trades", "days", "skipped", "filtered",
"digest"}) and the same list of globex.Day. It imports globex (research/noise-area-variations/globex.py,
by path) and nothing of orb_engine.py: every day is re-derived from the written rule (the plan's Task 1
rule block, docs/superpowers/plans/2026-11-17-orb-150k.md, and orb_engine.py's docstring), so a bug in the
engine is not copied into its own check. sm is globex's session minute (09:31 is 931, 15:59 is 1319).
MNQ: 2.00 a point, 1.90 a contract round trip, tick 0.25, 2 ticks (0.5 points) slippage a side on market
fills, a market fill kept inside its bar's range; stops under 10 points and more than 90 contracts are not
allowed.

For every day given, on its tradable bars day.bars[: globex.tradable_end(day) + 1], the check works out
what the rule does and compares it with the result:
  * Range: every bar stamped 09:31 .. 09:30+n present and tradable; o, h, l, c. None: no trade, no skip,
    no filter that day.
  * atr14: the mean of (highest high - lowest low) of the bars stamped 09:31 to 16:00 of the 14 previous
    days in the list that have a 09:31 bar (whole days, not cut at a hole); None with fewer than 14.
  * Filter (max_or_atr x): atr14 None or (h - l) > x * atr14: the date must be in `filtered`, with no
    trade; and no other date may be there.
  * stop atr_frac with atr14 None: no trade, no skip, no filter.
  * Decision bar: "direction": the range's last bar, side by c vs o (none when equal or not allowed);
    "break": the first bar after the range, stamped no later than entry_until, closing above h (long) or
    below l (short) on an allowed side. So no earlier bar that day qualified. No entry when the bar after
    it is missing, is the last tradable bar or is stamped 15:59 or later.
  * dist from the decision close (far_side, or_frac x * (h - l), atr_frac x * atr14), down to the tick.
    Under 10: the date must be skipped "stop under 10 points". qty = floor(balance * risk_pct / 100 /
    ((dist + 0.5) * 2 + 1.90)) capped at 90 (or the result's fixed_qty), the balance being start plus the
    net of every result trade that closed before the decision bar; under 1: skipped "under one contract".
    A skip's decision_dt and side, when given, must be the decision bar's.
  * Otherwise the date must have exactly one trade: side, entry_dt = the bar after the decision bar,
    entry = its open 2 ticks against inside its range, dist, stop_initial = entry -/+ dist, qty,
    planned_cost (to the cent). Then the life of the trade is replayed bar by bar from the entry bar with
    the rule's values under the result's fill: stop (kind / harsh-stops / midpoint as in the Noise-Area
    engine's step b, gap when the bar opens beyond the stop), else target (resting at entry +/- x * dist,
    rounded away from the entry, filled at its price on one tick through), else flat (on the 15:59 bar or
    later or the last tradable bar: the next tradable bar's open 2 ticks against, gap when that open is
    beyond the stop; or the last bar's close 2 ticks against), else the trail (best -/+ x * dist on the
    tick grid away from the price, only toward it, from the next bar). reason, exit_dt, exit and gap must
    be the replay's, and net = (exit - entry) * sign * 2.0 * qty - 1.90 * qty to the cent (from the rule's
    fills and from the trade's own), r = net / planned_cost, balance = the realised balance in list order.
  * Any date with a trade, skip or filter the rule does not give is a break; so is any lost signal.
  * On a "kind" result, a trade with gap false and a loss above planned_cost by more than a cent.
  * Day lines: one per day given, in order; start = the realised balance before the day; end = after its
    trade; low = the lowest of the start, the open position marked at each bar's adverse extreme
    (commission included) on the bars it is open past the stop check, and the balance after the close.

The real-data runs of the plan's Task 2 Step 4 are in test_orb_check.py (RealData), so this module never
imports the engine.

Standard library only. Run with `python3 -I -B`.
"""
import bisect
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_NAV = os.path.join(os.path.dirname(_HERE), "noise-area-variations")
if _NAV not in sys.path:
    sys.path.append(_NAV)
import globex   # noqa: E402

PV, COMM, TICK, SLIP = 2.0, 1.90, 0.25, 0.5
MIN_STOP, QTY_CAP = 10.0, 90
FILL_MODELS = ("kind", "harsh-stops", "midpoint")
EPS = 1e-9
CENT = 0.01
OPEN_SM = globex.sm_of("09:31")
CLOSE_SM = globex.sm_of("16:00")
FLAT_SM = globex.sm_of("15:59")


def _down(x):
    return math.floor(x / TICK + EPS) * TICK


def _up(x):
    return math.ceil(x / TICK - EPS) * TICK


def _inside(x, b):
    return min(max(x, b.l), b.h)


def _eq(a, b):
    return isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) <= EPS


def _st(b):
    return b.dt.isoformat(" ")


def _day_range(day):
    """Highest high - lowest low of the bars stamped 09:31..16:00 of the whole day, or None (no 09:31)."""
    hi = lo = None
    has_open = False
    for b in day.bars:
        if OPEN_SM <= b.sm <= CLOSE_SM:
            if b.sm == OPEN_SM:
                has_open = True
            hi = b.h if hi is None else max(hi, b.h)
            lo = b.l if lo is None else min(lo, b.l)
    return (hi - lo) if has_open else None


def _atrs(days):
    ranges = [_day_range(d) for d in days]
    out = []
    for k in range(len(days)):
        prior = [r for r in ranges[:k] if r is not None][-14:]
        out.append(sum(prior) / 14.0 if len(prior) == 14 else None)
    return out


class _Rule(object):
    def __init__(self, s, fill, fixed_qty):
        self.n = s["or_minutes"]
        self.entry = s["entry"]
        self.until = globex.sm_of(s["entry_until"]) if s["entry"] == "break" else None
        self.sides = {1: s["sides"] in ("both", "long"), -1: s["sides"] in ("both", "short")}
        self.stop = tuple(s["stop"])
        self.exit = tuple(s["exit"])
        self.cap = s["max_or_atr"]
        self.risk = s["risk_pct"]
        self.fill = fill
        self.fixed_qty = fixed_qty

    def plan(self, day, atr, balance_at):
        """What the rule does on `day` -> dict(kind=None|"filtered"|"skip"|"trade", ...)."""
        last = globex.tradable_end(day) if day.bars else -1
        bars = day.bars[:last + 1]
        pos = {b.sm: i for i, b in enumerate(bars)}
        idx = [pos.get(OPEN_SM + m) for m in range(self.n)]
        if any(i is None for i in idx):
            return {"kind": None}
        rb = [bars[i] for i in idx]
        o, c = rb[0].o, rb[-1].c
        h, l = max(b.h for b in rb), min(b.l for b in rb)
        out = {"kind": None, "bars": bars, "last": last, "range": (o, h, l, c), "atr": atr}
        if self.cap is not None and (atr is None or h - l > self.cap * atr):
            out["kind"] = "filtered"
            return out
        if self.stop[0] == "atr_frac" and atr is None:
            return out
        j, side = None, 0
        if self.entry == "direction":
            j = idx[-1]
            side = 1 if c > o else (-1 if c < o else 0)
            if side == 0 or not self.sides[side]:
                return out
        else:
            for i in range(idx[-1] + 1, len(bars)):
                b = bars[i]
                if b.sm > self.until:
                    break
                if self.sides[1] and b.c > h:
                    j, side = i, 1
                    break
                if self.sides[-1] and b.c < l:
                    j, side = i, -1
                    break
            if j is None:
                return out
        if j + 1 > last - 1 or bars[j + 1].sm >= FLAT_SM:
            return out
        d = bars[j]
        out.update(decision=j, side=side)
        if self.stop[0] == "far_side":
            raw = (d.c - l) if side == 1 else (h - d.c)
        elif self.stop[0] == "or_frac":
            raw = self.stop[1] * (h - l)
        else:
            raw = self.stop[1] * atr
        dist = _down(raw)
        lpc = (dist + SLIP) * PV + COMM
        out["dist"] = dist
        if dist < MIN_STOP:
            out.update(kind="skip", reason="stop under 10 points")
            return out
        balance = balance_at(_st(d))
        if self.fixed_qty is not None:
            qty = self.fixed_qty
        else:
            qty = min(int(math.floor(balance * self.risk / 100.0 / lpc + EPS)), QTY_CAP)
        if qty < 1:
            out.update(kind="skip", reason="under one contract")
            return out
        e = bars[j + 1]
        entry = _inside(e.o + SLIP * side, e)
        out.update(kind="trade", entry_i=j + 1, entry=entry, stop0=entry - side * dist, qty=qty,
                   planned=round(qty * lpc, 2))
        return out

    def life(self, p):
        """Replay the trade -> (reason, exit index, exit price, gap, the bars it is marked open on)."""
        bars, last, side = p["bars"], p["last"], p["side"]
        entry, dist, stop = p["entry"], p["dist"], p["stop0"]
        target = None
        if self.exit[0] == "target_r":
            raw = entry + side * self.exit[1] * dist
            target = _up(raw) if side == 1 else _down(raw)
        best = entry
        marked = []
        for i in range(p["entry_i"], last + 1):
            b = bars[i]
            reached = b.l <= stop if side == 1 else b.h >= stop
            if reached:
                beyond = b.o < stop if side == 1 else b.o > stop
                ref = b.o if beyond else stop
                worst = b.l if side == 1 else b.h
                if self.fill == "harsh-stops":
                    px = worst
                elif self.fill == "midpoint":
                    px = _down((ref + worst) / 2.0) if side == 1 else _up((ref + worst) / 2.0)
                else:
                    px = _inside(ref - SLIP * side, b)
                return "stop", i, px, beyond, marked
            marked.append(b)
            best = max(best, b.h) if side == 1 else min(best, b.l)
            if target is not None and (b.h >= target + TICK if side == 1 else b.l <= target - TICK):
                return "target", i, target, False, marked
            if b.sm >= FLAT_SM or i == last:
                if i < last:
                    nb = bars[i + 1]
                    beyond = nb.o < stop if side == 1 else nb.o > stop
                    return "flat", i + 1, _inside(nb.o - SLIP * side, nb), beyond, marked
                return "flat", i, _inside(b.c - SLIP * side, b), False, marked
            if self.exit[0] == "trail_r":
                x = self.exit[1] * dist
                cand = _down(best - x) if side == 1 else _up(best + x)
                if (cand > stop) if side == 1 else (cand < stop):
                    stop = cand
        raise AssertionError("the replay ran off the day's bars")


def rule_check(result, days):
    """-> list of breaks, one line each; empty when the result obeys the written rule (module docstring)."""
    s, fill = result["settings"], result["fill"]
    start = float(result["start"])
    fixed_qty = result.get("fixed_qty")
    trades = result["trades"]
    out = []
    if fill not in FILL_MODELS:
        return ["fill %r is not one of %s" % (fill, FILL_MODELS)]
    rule = _Rule(s, fill, fixed_qty)
    dates = [d.date for d in days]
    known = set(dates)

    # Trades: in date order, one a day, on loaded days; money consistent with their own fills.
    by_date = {}
    bal = start
    chain = []                       # (exit_dt, realised balance after it), from the result's nets
    for n, t in enumerate(trades):
        tag = "%s %s entered %s" % (t.get("date"), t.get("side"), t.get("entry_dt"))
        if t["date"] not in known:
            out.append("%s: not a loaded day" % tag)
        by_date.setdefault(t["date"], []).append(n)
        if n and trades[n - 1]["date"] >= t["date"]:
            out.append("%s: not after the previous trade's date %s (one trade a day, in order)"
                       % (tag, trades[n - 1]["date"]))
        sign = 1 if t["side"] == "long" else -1
        own = round((t["exit"] - t["entry"]) * sign * PV * t["qty"] - COMM * t["qty"], 2)
        if not _eq(own, t["net"]):
            out.append("%s: net %r does not match its own fills, which give %r" % (tag, t["net"], own))
        if not t["planned_cost"] or t["r"] is None or abs(t["r"] - t["net"] / t["planned_cost"]) > 1e-12:
            out.append("%s: r %r is not net / planned_cost" % (tag, t["r"]))
        bal = round(bal + t["net"], 2)
        if not _eq(bal, t["balance"]):
            out.append("%s: balance %r, the realised balance is %r" % (tag, t["balance"], bal))
        chain.append((t["exit_dt"], bal))
        if t["stop_initial"] is None or t["dist"] is None:
            out.append("%s: no stop at entry" % tag)
        if fill == "kind" and not t["gap"] and -t["net"] - t["planned_cost"] > CENT + EPS:
            out.append("%s: loss above the planned cost without a gap: net %r, planned %r"
                       % (tag, t["net"], t["planned_cost"]))

    stamps = [x for x, _ in chain]

    def balance_at(stamp):
        m = bisect.bisect_right(stamps, stamp)     # trades are in date order, so exit stamps are sorted
        return chain[m - 1][1] if m else start

    skipped = {}
    for x in result["skipped"]:
        if x["date"] in skipped:
            out.append("skipped: %s listed twice" % x["date"])
        skipped[x["date"]] = x
    filtered = list(result["filtered"])
    if len(set(filtered)) != len(filtered):
        out.append("filtered: a date listed twice")
    want_filtered = []
    atrs = _atrs(days)

    got_days = result["days"]
    if [d.get("date") for d in got_days] != dates:
        out.append("days: the day lines are not one per day given, in order")
        got_days = None
    bal = start
    for k, day in enumerate(days):
        date = day.date
        p = rule.plan(day, atrs[k], balance_at)
        ns = by_date.get(date, [])
        if len(ns) > 1:
            out.append("%s: %d trades on one day" % (date, len(ns)))
        t = trades[ns[0]] if ns else None
        kind = p["kind"]
        if kind == "filtered":
            want_filtered.append(date)
        sk = skipped.get(date)
        if kind == "skip":
            if sk is None:
                out.append("%s: the rule skips (%s) but the result does not list the skip" % (date, p["reason"]))
            else:
                if sk["reason"] != p["reason"]:
                    out.append("%s: skip reason %r, the rule gives %r" % (date, sk["reason"], p["reason"]))
                if "decision_dt" in sk and sk["decision_dt"] != _st(p["bars"][p["decision"]]):
                    out.append("%s: skip decision_dt %s, the rule's decision bar is %s"
                               % (date, sk["decision_dt"], _st(p["bars"][p["decision"]])))
                if "side" in sk and sk["side"] != ("long" if p["side"] == 1 else "short"):
                    out.append("%s: skip side %s does not match the rule" % (date, sk["side"]))
        elif sk is not None:
            out.append("%s: skipped (%s) where the rule gives no skip" % (date, sk["reason"]))
        if kind == "trade" and t is None:
            out.append("%s: no trade on a day the rule trades (%s at %s)"
                       % (date, "long" if p["side"] == 1 else "short", _st(p["bars"][p["entry_i"]])))
        if kind != "trade" and t is not None:
            out.append("%s %s entered %s: a trade on a day the rule gives none (%s)"
                       % (date, t["side"], t["entry_dt"], kind or "no signal"))
        day_start = low = bal
        if t is not None:
            bal = round(bal + t["net"], 2)
        if kind == "trade" and t is not None:
            marked = _compare(out, rule, p, t, date)
            sign = 1 if t["side"] == "long" else -1
            for b in marked:
                x = b.l if sign == 1 else b.h
                low = min(low, day_start + (x - t["entry"]) * sign * PV * t["qty"] - COMM * t["qty"])
        low = min(low, bal)
        if got_days is not None:
            g = got_days[k]
            want = {"start": round(day_start, 2), "end": round(bal, 2), "low": round(low, 2)}
            for key in ("start", "end", "low"):
                if not _eq(g.get(key), want[key]):
                    out.append("day %s: %s %r, the replay gives %r" % (date, key, g.get(key), want[key]))
    if filtered != want_filtered:
        extra = sorted(set(filtered) - set(want_filtered))
        lost = sorted(set(want_filtered) - set(filtered))
        out.append("filtered does not match the rule: listed but not filtered %s; filtered but not listed %s%s"
                   % (extra[:5], lost[:5], "" if extra or lost else " (order)"))
    return out


def _compare(out, rule, p, t, date):
    """Compare one trade with the rule's -> the bars the rule's trade is marked open on."""
    bars, side = p["bars"], p["side"]
    tag = "%s %s entered %s" % (date, t["side"], t["entry_dt"])

    def br(msg):
        out.append("%s: %s" % (tag, msg))

    want_side = "long" if side == 1 else "short"
    if t["side"] != want_side:
        br("side %s, the rule gives %s (decision bar %s)" % (t["side"], want_side, _st(bars[p["decision"]])))
    e = bars[p["entry_i"]]
    if t["entry_dt"] != _st(e):
        br("entry not at the bar after the rule's decision bar %s: the rule enters at %s"
           % (_st(bars[p["decision"]]), _st(e)))
    if not _eq(t["entry"], p["entry"]):
        br("entry fill %r, the rule gives %r (open %r, 2 ticks against)" % (t["entry"], p["entry"], e.o))
    if not _eq(t["dist"], p["dist"]):
        br("dist %r, the rule gives %r" % (t["dist"], p["dist"]))
    if not _eq(t["stop_initial"], p["stop0"]):
        br("stop_initial %r, the rule gives %r" % (t["stop_initial"], p["stop0"]))
    if t["qty"] != p["qty"]:
        br("qty %r, the rule gives %r" % (t["qty"], p["qty"]))
    if not _eq(t["planned_cost"], p["planned"]):
        br("planned_cost %r, the rule gives %r" % (t["planned_cost"], p["planned"]))
    reason, xi, px, gap, marked = rule.life(p)
    got = (t["reason"], t["exit_dt"], t["exit"], bool(t["gap"]))
    want = (reason, _st(bars[xi]), px, gap)
    if not (got[0] == want[0] and got[1] == want[1] and _eq(got[2], want[2]) and got[3] == want[3]):
        br("exit (reason, exit_dt, exit, gap) %r, the rule gives %r" % (got, want))
    net = round((px - p["entry"]) * side * PV * p["qty"] - COMM * p["qty"], 2)
    if not _eq(t["net"], net):
        br("net %r, the rule's fills give %r" % (t["net"], net))
    return marked
