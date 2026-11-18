#!/usr/bin/env python3
"""rule_check.py -- the independent rule check for momentum into the close (research/close-momentum-150k/PLAN.md,
the sections "Data and markets", "The exact rule" and "Amendment, 2026-11-18, before any engine code", which
spells out rules 4 to 6 and replaces rule 7). Written from the plan's text alone, without seeing the engine or
the pre-screen, so a misreading there is not copied here. The check replays the rule from the raw bars and the
settings, then compares the engine's trades field by field and returns a list of breaks (empty = clean).

replay_market(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None) -> [trade]
    One dict per trade, with exactly the fields of the amendment's "Each trade records" (FIELDS), for every
    trading day d with first <= d <= last (ISO dates, inclusive; None = no bound). minutes = [mdata.Bar] sorted
    by stamp, daily = [mdata.Adj] (specs.load), spec = one entry of specs.SPECS, market = its key, settings =
    {"name", "signal": "S1" | "S2" | "S3", "k", "atr_days"}, fill = "midpoint" | "kind" | "harsh-stops".
replay_days(...), the same arguments -> [(date, trade or None, why)]: the rule's outcome for every trading day in
    the range, with the reason when there is no trade.
check_market(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None) -> [str]
    got = the engine's output for one market, {"trades": [...]}. Missing trades, extra trades (with the rule's
    reason for making none) and every differing field, each naming the date and the field.
check_account(result, per_contract_by_market, specs_by_market, risk_pct, start) -> [str]
    The size (the amendment's "Size", which replaces rule 7) is the levels plan's account, so this is
    research/levels-150k/rule_check.check_account, unchanged, run on these trades (C17).

Readings
--------
Where the plan's words leave a choice, the most literal reading is taken.

 C1. Trading day: a New York calendar date, Monday to Friday, on which at least one minute bar is stamped. A bar
     belongs to the New York date of its stamp (the start of its minute), from the tz database with daylight
     saving. Saturdays and Sundays are never trading days, whatever bars they hold (the Sunday evening open); a
     weekday with no bar at all is not one. Words: "a New York weekday with minute bars in it".
 C2. "The trading day before d" is the latest trading day earlier than d in the minutes given, whatever it holds.
     It need not have a bar in [O, C) or a price at C. When it has no price at C there is no Y and no trade on d;
     the rule does not look further back. So a part-day holiday with no bar in [C, C + 5) costs that day and the
     next. The first trading day in the data has no day before it: no trade. Words: "Y = the price at C on the
     trading day before d".
 C3. The clock. O, C, O + 30 and C - 30 are New York clock times on the day in question (C on the day before, for
     Y), turned into UTC instants with the tz database. "t + 5 minutes" and "t - 5 minutes" are 300 seconds (no
     clock change falls in these hours, so clock and elapsed time agree). "At or after t and before t + 5
     minutes" is [t, t + 5 min) and "at or after t - 5 minutes and before t" is [t - 5 min, t), on the bar's
     stamp. So the last price before O + 30 reads only bars stamped O + 25 to O + 29, and a bar stamped exactly
     C - 30 is the entry bar, never the S1 bar. Words: rule 1.
 C4. Y is the open of the first bar in [C, C + 5 min) on the trading day before d (rule 1's "price at C"), not a
     close and not a settlement.
 C5. The roll rule. "Today's bars" are every minute bar whose New York date is d, midnight to midnight, the
     evening after the close included. If any one of them is of a contract (iid) other than that of Y's bar,
     there is no trade on d; so a roll stamped in d's evening, after its close, also costs d. The `rolls` list
     (of the daily series) is not read: the rule speaks of minute bars. Words: "if that bar and today's bars are
     of different contracts (a roll in between), no trade that day".
 C6. Signals. Above Y: s - Y > eps; below: s - Y < -eps; otherwise equal, no trade (rule 3, and "eps = tick x
     10^-6 in every comparison"). Prices raw. A missing price gives no side. S3 trades only when S1 and S2 give
     the same side; a missing or an equal one means no trade. Words: "S3, both: S1 and S2 agree".
 C7. Every trade records both s1 and s2, whatever its signal; each is None when its window holds no bar. Words:
     "s1 (...) and s2 (...), each None when that bar is missing".
 C8. Entry = min(max(open + side x slip, low), high) of the entry bar; the close exit = min(max(open - side x
     slip, low), high) of the exit bar; slip = slip_ticks x tick. Raw, never rounded. Words: "held inside that
     bar: no higher than its high, no lower than its low".
 C9. A = sum / atr_days of (adj_high - adj_low) over the last atr_days (14) daily bars, in list order, whose
     stamp's UTC date is before d, d being the New York date. A daily bar stamped on d's own UTC date is not
     read. Fewer such bars: no trade. A is not rounded. atr_days is the settings' (14 in all twelve; 14 when
     absent). Words: "the 14 daily bars (back-adjusted, specs.load) whose UTC date is before day d".
C10. dist = max(floor_tick(k x A), tick), floor_tick and ceil_tick as the amendment writes them; stop = entry -
     side x dist, raw, so off the tick grid when the entry is.
C11. The watched minutes are the bars of the minutes list from the entry bar's index up to, not including, the exit
     bar's. The exit bar is never checked. On each, the gap test (the open) comes before the touch test. A short
     mirrors the long with the tolerance mirrored too: a gap when open >= stop - eps, a touch when high >= stop -
     eps; midpoint ceil_tick((reference + high) / 2); kind min(reference + slip, high); harsh the high. A literal
     swap of >= for <= in "open <= stop + eps" would leave "+ eps", which turns the tolerance against the fill;
     "a short mirrors it" is read as the reflection.
C12. The stop is checked on the entry bar itself with that bar's open, high and low. When the entry fill lies at
     least dist past the open (dist <= slip, as at the one-tick floor), the entry bar opens at or beyond the stop:
     a gap stop on the entry bar, its open the reference. Words: "from the entry bar itself".
C13. Rule 5's "a minute that opens beyond the stop fills at its open" is read through the amendment, which spells
     rule 5 out: the open is the gap's reference, and the fill is the midpoint, kind or harsh fill from it. The
     fill setting changes only stop fills; the entry and the close exit are market orders under every fill.
C14. No price at C: no trade at all, even on a day whose stop would have filled before C (rule 4 lists it with
     the no-trade cases, before any order).
C15. worst. A stop exit: the minimum of (adverse - entry) x side over the bars from the entry bar to the stop's
     bar, both whole (adverse = low for a long, high for a short). A close exit: the same over the entry bar to
     the bar before the exit bar, and (exit - entry) x side for the exit bar. The entry bar counts whole though
     the fill came at its open plus slippage. points = (exit - entry) x side.
C16. Comparing. Trades are matched by date (one per market per day). The ten price fields (y, s1, s2, atr, dist,
     entry, stop, exit, points, worst) must lie within 1e-9 of the rule's, and None matches only None. Every
     other field must be equal, gap must be a bool (1 is not True) and side not a bool. A field missing from the
     engine's record is a break; fields the plan does not list are named once per market. The engine's trades
     outside first..last show as extra. The engine's trades must be in date order.
C17. check_account runs the levels check_account (research/levels-150k/rule_check.py, loaded by path) on these
     trades. It compares the fields of a levels trade, so kind, level and target, which these trades do not
     have, are set to one placeholder on both sides before it runs; the five fields it does not know (signal, y,
     s1, s2, atr) are then compared here, account trade against per-contract trade.
C18. The minutes and the daily bars are taken as given; a stamp out of order or repeated raises ValueError rather
     than being resolved.

Standard library only. Python 3.14, run with python3 -I -B.
"""
import bisect
import importlib.util
import math
import os
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

_HERE = os.path.dirname(os.path.abspath(__file__))
_LEVELS_CHECK = os.path.normpath(os.path.join(_HERE, "..", "levels-150k", "rule_check.py"))

NY = ZoneInfo("America/New_York")
NS = 1_000_000_000
MIN_NS = 60 * NS
DAY_NS = 86400 * NS
_EPOCH = date(1970, 1, 1).toordinal()
_SECOND = timedelta(seconds=1)
FILLS = ("midpoint", "kind", "harsh-stops")
SIGNALS = ("S1", "S2", "S3")
FIELDS = ("market", "date", "signal", "side", "y", "s1", "s2", "atr", "dist", "entry_ts", "entry", "stop",
          "exit_ts", "exit", "reason", "gap", "points", "worst")
PRICE_FIELDS = frozenset(("y", "s1", "s2", "atr", "dist", "entry", "stop", "exit", "points", "worst"))
TOL = 1e-9
_NUDGE = 1e-6       # the amendment's 10^-6 inside floor_tick and ceil_tick
_EPS_TICKS = 1e-6   # eps = tick x 10^-6

# The plan's table "Data and markets": (open O, close C), New York clock.
_IDX, _BONDS_FX, _CL, _GC = ((9, 30), (16, 0)), ((8, 20), (15, 0)), ((9, 0), (14, 30)), ((8, 20), (13, 30))
HOURS = {"NQ": _IDX, "ES": _IDX, "RTY": _IDX, "ZN": _BONDS_FX, "ZB": _BONDS_FX, "6E": _BONDS_FX,
         "6J": _BONDS_FX, "6B": _BONDS_FX, "6A": _BONDS_FX, "CL": _CL, "GC": _GC}


# ------------------------------------------------------------------------------------------------ the clock
def ny_ns(day, hh, mm):
    """UTC nanoseconds of hh:mm New York clock time on the date `day`."""
    off = datetime(day.year, day.month, day.day, hh, mm, tzinfo=NY).utcoffset()
    secs = (day.toordinal() - _EPOCH) * 86400 + hh * 3600 + mm * 60 - off // _SECOND
    return secs * NS


def ny_date(ts):
    """The New York calendar date of the instant ts (UTC nanoseconds)."""
    return datetime.fromtimestamp(ts // NS, NY).date()


# ------------------------------------------------------------------------------------------------ ticks
def floor_tick(x, tick):
    return math.floor(x / tick + _NUDGE) * tick


def ceil_tick(x, tick):
    return math.ceil(x / tick - _NUDGE) * tick


# ------------------------------------------------------------------------------------------------ the data
_PREP = []
_PREP_SIZE = 2


def _sorted_stamps(ts, what):
    for i in range(1, len(ts)):
        if ts[i] <= ts[i - 1]:
            raise ValueError(f"{what}: stamp {ts[i]} at position {i} is not after {ts[i - 1]} (C18)")


def _prep(minutes, daily):
    for m, d, p in _PREP:
        if m is minutes and d is daily:
            return p
    ts = [b.ts for b in minutes]
    _sorted_stamps(ts, "minutes")
    days, i, n = [], 0, len(ts)
    while i < n:                                     # C1: New York dates, weekdays only
        d = ny_date(ts[i])
        j = bisect.bisect_left(ts, ny_ns(d + timedelta(days=1), 0, 0), i)
        if d.weekday() < 5:
            days.append((d, i, j))
        i = j
    dts = [a.bar.ts for a in daily]
    _sorted_stamps(dts, "daily bars")
    p = {"ts": ts, "days": days, "dts": dts, "ranges": [a.adj_high - a.adj_low for a in daily], "iids": {}}
    _PREP.append((minutes, daily, p))
    del _PREP[:-_PREP_SIZE]
    return p


def clear_cache():
    _PREP.clear()


def _price_at(ts, t):
    """Index of the bar giving "the price at t": the first stamped in [t, t + 5 min); None if there is none."""
    k = bisect.bisect_left(ts, t)
    return k if k < len(ts) and ts[k] < t + 5 * MIN_NS else None


def _last_before(ts, t):
    """Index of the bar giving "the last price before t": the last stamped in [t - 5 min, t); None if none."""
    k = bisect.bisect_left(ts, t) - 1
    return k if k >= 0 and ts[k] >= t - 5 * MIN_NS else None


def _day_iids(p, minutes, t):
    """The set of contracts among trading day t's bars (C5)."""
    got = p["iids"].get(t)
    if got is None:
        _d, lo, hi = p["days"][t]
        got = p["iids"][t] = frozenset(minutes[i].iid for i in range(lo, hi))
    return got


def _atr(p, day, n_atr):
    """C9: the mean daily range of the last n_atr daily bars whose UTC date is before `day`; None if too few."""
    m = bisect.bisect_left(p["dts"], (day.toordinal() - _EPOCH) * DAY_NS)
    if m < n_atr:
        return None
    return sum(p["ranges"][m - n_atr:m]) / n_atr


def _side(s, y, eps):
    if s is None:
        return 0
    if s - y > eps:
        return 1
    if s - y < -eps:
        return -1
    return 0


# ------------------------------------------------------------------------------------------------ the rule
def _settings(settings, fill, market):
    if fill not in FILLS:
        raise ValueError(f"fill {fill!r} is not one of {FILLS}")
    if market not in HOURS:
        raise ValueError(f"market {market!r} is not in the plan's table of hours")
    sig = settings.get("signal")
    if sig not in SIGNALS:
        raise ValueError(f"signal {sig!r} is not one of {SIGNALS}")
    n_atr = settings.get("atr_days", 14)
    if not isinstance(n_atr, int) or isinstance(n_atr, bool) or n_atr < 1:
        raise ValueError(f"atr_days {n_atr!r} is not a whole number of days")
    return sig, float(settings["k"]), n_atr


def _stop_fill(b, side, stop, eps, slip, tick, fill):
    """The amendment's stop test on one watched minute: (fill, gap) or None when the stop does not fill."""
    if side > 0:
        if b.open <= stop + eps:
            ref, gap = b.open, True
        elif b.low <= stop + eps:
            ref, gap = stop, False
        else:
            return None
        if fill == "midpoint":
            return floor_tick((ref + b.low) / 2, tick), gap
        if fill == "kind":
            return max(ref - slip, b.low), gap
        return b.low, gap
    if b.open >= stop - eps:
        ref, gap = b.open, True
    elif b.high >= stop - eps:
        ref, gap = stop, False
    else:
        return None
    if fill == "midpoint":
        return ceil_tick((ref + b.high) / 2, tick), gap
    if fill == "kind":
        return min(ref + slip, b.high), gap
    return b.high, gap


def _day(minutes, p, t, market, tick, slip, sig, k, n_atr, fill):
    """The rule on trading day t (index into p["days"]): (trade, None) or (None, why)."""
    ts, days = p["ts"], p["days"]
    d = days[t][0]
    if t == 0:
        return None, "no trading day before it in the data"
    (oh, om), (ch, cm) = HOURS[market]
    eps = tick * _EPS_TICKS
    prev = days[t - 1][0]
    yk = _price_at(ts, ny_ns(prev, ch, cm))
    if yk is None:
        return None, f"no price at C on the trading day before ({prev.isoformat()}): no Y"
    ybar = minutes[yk]
    y = ybar.open
    iids = _day_iids(p, minutes, t)
    if iids != {ybar.iid}:
        return None, f"a roll: Y's bar is contract {ybar.iid}, today's bars are {sorted(iids)}"
    O, C = ny_ns(d, oh, om), ny_ns(d, ch, cm)
    k1, k2 = _last_before(ts, C - 30 * MIN_NS), _last_before(ts, O + 30 * MIN_NS)
    s1 = minutes[k1].close if k1 is not None else None
    s2 = minutes[k2].close if k2 is not None else None
    side1, side2 = _side(s1, y, eps), _side(s2, y, eps)
    if sig == "S1":
        side = side1
    elif sig == "S2":
        side = side2
    else:
        side = side1 if side1 == side2 else 0
    if side == 0:
        return None, f"no side ({sig}: s1 {s1}, s2 {s2}, y {y})"
    ek = _price_at(ts, C - 30 * MIN_NS)
    if ek is None:
        return None, "no price at C - 30"
    xk = _price_at(ts, C)
    if xk is None:
        return None, "no price at C"
    A = _atr(p, d, n_atr)
    if A is None:
        return None, f"fewer than {n_atr} daily bars before the day"
    eb = minutes[ek]
    entry = min(max(eb.open + side * slip, eb.low), eb.high)
    dist = max(floor_tick(k * A, tick), tick)
    stop = entry - side * dist
    exit_px = exit_ts = None
    gap, reason, last_i = False, "close", xk - 1
    for i in range(ek, xk):                          # C11: the entry bar up to, not including, the exit bar
        b = minutes[i]
        hit = _stop_fill(b, side, stop, eps, slip, tick, fill)
        if hit is not None:
            exit_px, gap = hit
            exit_ts, reason, last_i = b.ts, "stop", i
            break
    if side > 0:
        worst = min(minutes[i].low - entry for i in range(ek, last_i + 1))
    else:
        worst = min(entry - minutes[i].high for i in range(ek, last_i + 1))
    if reason == "close":
        xb = minutes[xk]
        exit_px = min(max(xb.open - side * slip, xb.low), xb.high)
        exit_ts = xb.ts
        worst = min(worst, (exit_px - entry) * side)
    return {"market": market, "date": d.isoformat(), "signal": sig, "side": side, "y": y, "s1": s1, "s2": s2,
            "atr": A, "dist": dist, "entry_ts": eb.ts, "entry": entry, "stop": stop, "exit_ts": exit_ts,
            "exit": exit_px, "reason": reason, "gap": gap, "points": (exit_px - entry) * side,
            "worst": worst}, None


def replay_days(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """[(ISO date, trade or None, why)] for every trading day d with first <= d <= last."""
    sig, k, n_atr = _settings(settings, fill, market)
    tick = float(spec["tick"])
    slip = spec["slip_ticks"] * tick
    p = _prep(minutes, daily)
    out = []
    for t, (d, _lo, _hi) in enumerate(p["days"]):
        iso = d.isoformat()
        if (first is not None and iso < first) or (last is not None and iso > last):
            continue
        trade, why = _day(minutes, p, t, market, tick, slip, sig, k, n_atr, fill)
        out.append((iso, trade, why))
    return out


def replay_market(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """The rule's trades for one market and one setting, in date order."""
    return [t for _d, t, _w in replay_days(minutes, daily, rolls, spec, settings, fill, market, first, last)
            if t is not None]


# ------------------------------------------------------------------------------------------------ comparing
def _fmt(x):
    return f"{x:.12g}" if isinstance(x, float) else repr(x)


def _same(field, mine, theirs):
    if field in PRICE_FIELDS:
        if mine is None or theirs is None:
            return mine is None and theirs is None
        if isinstance(theirs, bool) or not isinstance(theirs, (int, float)):
            return False
        return abs(mine - theirs) <= TOL
    if isinstance(mine, bool) or isinstance(theirs, bool):
        return type(mine) is type(theirs) and mine == theirs
    return mine == theirs


def _field_breaks(breaks, label, mine, theirs, fields):
    for f in fields:
        if f not in theirs:
            breaks.append(f"{label}: field {f} missing")
        elif not _same(f, mine[f], theirs[f]):
            breaks.append(f"{label}: {f} is {_fmt(theirs[f])}, rule says {_fmt(mine[f])}")


def check_market(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Breaks between the engine's trades for one market and setting and the rule's replay (C16)."""
    try:
        days = replay_days(minutes, daily, rolls, spec, settings, fill, market, first, last)
    except (ValueError, KeyError, TypeError) as e:
        return [f"{market}: cannot replay: {e}"]
    if not isinstance(got, dict) or not isinstance(got.get("trades"), list):
        return [f"{market}: the engine's output is not a dict with a list of trades"]
    mine = {d: t for d, t, _w in days if t is not None}
    why = {d: w for d, t, w in days if t is None}
    breaks, theirs, unlisted = [], {}, {}
    dates = []
    for t in got["trades"]:
        if not isinstance(t, dict) or not isinstance(t.get("date"), str):
            breaks.append(f"{market}: unreadable trade record {t!r}")
            continue
        dates.append(t["date"])
        if t["date"] in theirs:
            breaks.append(f"{market} {t['date']}: trade listed twice")
            continue
        theirs[t["date"]] = t
        for f in t:
            if f not in FIELDS:
                unlisted[f] = unlisted.get(f, 0) + 1
    if dates != sorted(dates):
        breaks.append(f"{market}: the engine's trades are not in date order")
    for d in sorted(set(mine) - set(theirs)):
        breaks.append(f"{market} {d}: trade missing (the rule makes it: {mine[d]!r})")
    for d in sorted(set(theirs) - set(mine)):
        reason = why.get(d, "not a trading day in first..last")
        breaks.append(f"{market} {d}: extra trade (the rule makes none: {reason}): {theirs[d]!r}")
    for d in sorted(set(mine) & set(theirs)):
        _field_breaks(breaks, f"{market} {d}", mine[d], theirs[d], FIELDS)
    if unlisted:
        breaks.append(f"{market}: trades carry fields the plan does not list: "
                      + ", ".join(f"{f} ({n} trades)" for f, n in sorted(unlisted.items())))
    return breaks


# ------------------------------------------------------------------------------------------------ the account
_LEVELS = []
_PLACEHOLDER = {"kind": "close-momentum", "level": 0.0, "target": None}
_EXTRA_FIELDS = ("signal", "y", "s1", "s2", "atr")


def _levels_check():
    if not _LEVELS:
        spec = importlib.util.spec_from_file_location("levels_rule_check", _LEVELS_CHECK)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _LEVELS.append(mod)
    return _LEVELS[0]


def _shim(t):
    if not isinstance(t, dict):
        return t
    u = dict(t)
    u.update(_PLACEHOLDER)
    return u


def check_account(result, per_contract_by_market, specs_by_market, risk_pct, start):
    """Breaks between the engine's account output and the levels plan's account replayed on these trades (C17)."""
    lv = _levels_check()
    pcs = {m: {"trades": [_shim(t) for t in (v.get("trades", []) if isinstance(v, dict) else [])]}
           for m, v in per_contract_by_market.items()}
    if not isinstance(result, dict):
        return ["account: the engine's output is not a dict"]
    res = dict(result)
    res["trades"] = [_shim(t) for t in result.get("trades", [])]
    breaks = lv.check_account(res, pcs, specs_by_market, risk_pct, start)
    mine = {}
    for m, v in per_contract_by_market.items():
        for t in (v.get("trades", []) if isinstance(v, dict) else []):
            mine[(m, t["date"], t["entry_ts"])] = t
    for t in result.get("trades", []):
        try:
            key = (t["market"], t["date"], t["entry_ts"])
        except (KeyError, TypeError):
            continue                                 # the levels check has named it
        if key in mine:
            _field_breaks(breaks, f"account: trade {key[0]} {key[1]} entered {key[2]}", mine[key], t,
                          _EXTRA_FIELDS)
    return breaks
