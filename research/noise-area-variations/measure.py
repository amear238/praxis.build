#!/usr/bin/env python3
"""measure.py -- the measuring pass: every Noise-Area breakout, and how far price ran after it.

Places no trades and keeps no account. Works on globex.Day lists (globex.py) and the noise band of
bands.py, built with lookback 14 and multiplier 1.0. sm is globex's session minute (18:01 is sm 1, 09:31
is sm 931, 16:00 is sm 1320). Stamps mark the END of the minute.

Tradable bars: for every purpose except the band, a day is day.bars[: globex.tradable_end(day) + 1], its
bars up to the first hole of more than 60 minutes (a data hole; see globex.py). The band is still built
from every bar of every day, and the trading-day calendar keeps every day.

Breakouts (events(days, anchor, cadence)):
  * Decision bars: every tradable bar of the day that has a band point ("minute"), or only the bars stamped :00 and
    :30 that have one ("half_hour"); in both cases only bars stamped at or before 15:59.
  * Side at a decision bar: "long" when its close is above the band's upper line, "short" when below the
    lower line, inside when lower <= close <= upper.
  * An event is a decision bar that is outside on a side different from the previous decision bar of the
    same day (the day starts as if inside). So one excursion is one event; it ends when a decision bar
    closes inside, or when one closes straight through to the other side, which is a new event of that
    side. Each day starts fresh.
  * A decision bar with no next tradable bar in its day makes no event (there is no entry bar).
  * The reference entry price `ref` is the open of the next bar (the entry bar), no slippage.
  * Stop distances, in points, from the band at the decision bar, signed in the direction of risk:
      half_width = width / 2; full_width = width;
      to_anchor = ref - anchor_price (long) or anchor_price - ref (short);
      opposite_band = ref - lower (long) or upper - ref (short).
    A distance below MIN_STOP_POINTS (10.0), zero and negative included, is tight; a tight stop has no
    outcome (its outcome fields are None).
  * Outcome walk for each stop that is not tight: stop = ref - dist (long) or ref + dist (short). From the
    entry bar itself to the day's last tradable bar (at or before 16:00), in order: if the bar's adverse extreme
    reaches the stop (long: low <= stop; short: high >= stop) the event is stopped there and that bar's
    favourable move is not counted; otherwise the best favourable move so far (long: high - ref; short:
    ref - low; never below 0) is updated. mfe_r = best move / dist; reached_N = mfe_r >= N;
    r_at_flat = -1.0 when stopped, else (last bar's close - ref) / dist, signed for the side.
  * No look-ahead: whether an event exists at decision bar T, and every field except the outcome fields
    (stopped, stop_time, mfe_r, r_at_flat, reached_*), depend only on bars at or before T and the next
    bar's open. The band itself is built from earlier days and bars at or before T only (bands.py).

Each event: date (the trading date), time (the decision bar's stamp, HH:MM), sm, part, side, anchor,
cadence, close, upper, lower, anchor_price, width (the band at the decision bar), entry_time, ref, and
stops = {kind: {dist, tight, stopped, stop_time, mfe_r, r_at_flat, reached_2, reached_3, reached_5}}.

Parts of the day: a decision stamp T is in a part when start < T <= end, along the 18:00 to 16:00 day.

Tables (tables(evts, calendars)): one row per anchor, cadence, stop kind, part (the five parts that the
anchor's band covers, then "all") and side ("long", "short", "both"). n counts the events that are not
tight for that stop (the ones the percentages and the average are over); tight_excluded counts the tight
ones. pct_reached_N is the share of the n that reached N times the stop distance, in percent;
avg_r_at_flat is the mean r_at_flat of the n (a stopped event counts -1.0); both are None when n is 0.
max_gap_trading_days is the longest run of consecutive trading days in calendars[anchor] with no event of
that row (tight events do not count as events here); a run at the very start or very end counts.

Calendar (calendar(days, anchor)): the loaded trading days from the first one that has a band for that
anchor to the last one loaded, days without a band included.

main: --start/--end bound the trading dates measured (default 2021-03-08 to 2023-12-31); an --end later
than 2023-12-31 is refused (exit code 2) unless --allow-later is given. To warm the band up, days from up
to WARMUP_DAYS calendar days before --start are loaded too (never before 2021-03-08, unless --start is
itself earlier); they feed the band only, and no event or calendar day comes from them, so a run started
mid-range gives the same events as a run from the beginning. Writes events-<anchor>-<cadence>.json,
tables.json and tables.md to --out. Two runs on the same file give byte-identical output.

Standard library only. Run with `python3 -I -B`.
"""
import argparse
import datetime as _dt
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import bands    # noqa: E402  (called as bands.day_bands, so a test can stand a band in)
import globex   # noqa: E402

STOPS = ("half_width", "full_width", "to_anchor", "opposite_band")
PARTS = (("evening", "18:00", "02:00"), ("overnight", "02:00", "09:30"), ("morning", "09:30", "11:30"),
         ("midday", "11:30", "14:00"), ("afternoon", "14:00", "16:00"))   # start < T <= end
MIN_STOP_POINTS = 10.0
ANCHOR_LIST = ("0930", "1800")
CADENCES = ("half_hour", "minute")
SIDES = ("long", "short", "both")
REACH = (2, 3, 5)
LOOKBACK, MULT = 14, 1.0
LAST_DECISION_SM = globex.sm_of("15:59")
LAST_BAR_SM = globex.sm_of("16:00")
DEFAULT_START, DEFAULT_END = "2021-03-08", "2023-12-31"
FIRST_DATE = "2021-03-08"
WARMUP_DAYS = 120
DEFAULT_DATA = "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
DEFAULT_OUT = os.path.join(_HERE, "out", "measure")


def _part_sm(hhmm):
    return 0 if hhmm == "18:00" else globex.sm_of(hhmm)


_PART_SM = tuple((name, _part_sm(a), _part_sm(b)) for name, a, b in PARTS)


def part_of(t):
    """'HH:MM' stamp or session minute -> the part of the day it falls in (start < T <= end)."""
    sm = globex.sm_of(t) if isinstance(t, str) else t
    for name, a, b in _PART_SM:
        if a < sm <= b:
            return name
    raise ValueError("no part of the day holds %r" % (t,))


def _hhmm(bar):
    return bar.dt.strftime("%H:%M")


def _is_decision(bar, cadence):
    if bar.sm > LAST_DECISION_SM:
        return False
    if cadence == "minute":
        return True
    return bar.dt.minute in (0, 30)


def _distances(side, ref, p):
    if side == "long":
        return {"half_width": p.width / 2.0, "full_width": p.width, "to_anchor": ref - p.anchor_price,
                "opposite_band": ref - p.lower}
    return {"half_width": p.width / 2.0, "full_width": p.width, "to_anchor": p.anchor_price - ref,
            "opposite_band": p.upper - ref}


def _walk(bars, i_entry, side, ref, dist):
    """The outcome of one stop distance, walking from the entry bar to the day's last bar."""
    out = {"dist": dist, "tight": dist < MIN_STOP_POINTS}
    if out["tight"]:
        for k in ("stopped", "stop_time", "mfe_r", "r_at_flat") + tuple("reached_%d" % n for n in REACH):
            out[k] = None
        return out
    long_ = side == "long"
    stop = ref - dist if long_ else ref + dist
    mfe = 0.0
    stopped_at = None
    last = None
    for i in range(i_entry, len(bars)):
        b = bars[i]
        if b.sm > LAST_BAR_SM:
            break
        last = b
        if long_:
            if b.l <= stop:
                stopped_at = b
                break
            mfe = max(mfe, b.h - ref)
        else:
            if b.h >= stop:
                stopped_at = b
                break
            mfe = max(mfe, ref - b.l)
    mfe_r = mfe / dist
    out["stopped"] = stopped_at is not None
    out["stop_time"] = _hhmm(stopped_at) if stopped_at is not None else None
    out["mfe_r"] = mfe_r
    if stopped_at is not None:
        out["r_at_flat"] = -1.0
    else:
        out["r_at_flat"] = ((last.c - ref) if long_ else (ref - last.c)) / dist
    for n in REACH:
        out["reached_%d" % n] = mfe_r >= n
    return out


def _check(anchor, cadence):
    if anchor not in ANCHOR_LIST:
        raise ValueError("anchor must be one of %s, got %r" % (ANCHOR_LIST, anchor))
    if cadence not in CADENCES:
        raise ValueError("cadence must be one of %s, got %r" % (CADENCES, cadence))


def events(days, anchor, cadence, first_date=None):
    """-> list of event dicts in time order (see the module rules). Days dated before first_date feed the
    band only and make no events."""
    _check(anchor, cadence)
    out = []
    for k, day in enumerate(days):
        if first_date is not None and day.date < first_date:
            continue
        bmap = bands.day_bands(days, k, anchor, LOOKBACK, MULT)
        if not bmap:
            continue
        bars = day.bars[: globex.tradable_end(day) + 1]   # the band above used every bar
        state = "inside"
        for i, b in enumerate(bars):
            p = bmap.get(b.sm)
            if p is None or not _is_decision(b, cadence):
                continue
            if b.c > p.upper:
                pos = "long"
            elif b.c < p.lower:
                pos = "short"
            else:
                pos = "inside"
            new = pos != "inside" and pos != state
            state = pos
            if not new or i + 1 >= len(bars):
                continue
            entry = bars[i + 1]
            ref = entry.o
            dists = _distances(pos, ref, p)
            out.append({
                "date": day.date, "time": _hhmm(b), "sm": b.sm, "part": part_of(b.sm), "side": pos,
                "anchor": anchor, "cadence": cadence, "close": b.c, "upper": p.upper, "lower": p.lower,
                "anchor_price": p.anchor_price, "width": p.width, "entry_time": _hhmm(entry), "ref": ref,
                "stops": {kind: _walk(bars, i + 1, pos, ref, dists[kind]) for kind in STOPS},
            })
    return out


def calendar(days, anchor, first_date=None):
    """-> trading dates from the first day (dated first_date or later) with a band for anchor to the last."""
    if anchor not in ANCHOR_LIST:
        raise ValueError("anchor must be one of %s, got %r" % (ANCHOR_LIST, anchor))
    for k, day in enumerate(days):
        if first_date is not None and day.date < first_date:
            continue
        if bands.day_bands(days, k, anchor, LOOKBACK, MULT):
            return [d.date for d in days[k:]]
    return []


def _parts_for(anchor):
    a_sm = bands.ANCHORS[anchor]
    return [name for name, _a, b in _PART_SM if b >= a_sm] + ["all"]


def _longest_gap(cal, dates):
    best = run = 0
    for d in cal:
        if d in dates:
            run = 0
        else:
            run += 1
            best = max(best, run)
    return best


def tables(evts, calendars=None):
    """-> table rows (see the module rules), ordered by anchor, cadence, stop, part, side. calendars maps an
    anchor to its list of trading dates; without one, max_gap_trading_days is None."""
    combos = sorted(set((e["anchor"], e["cadence"]) for e in evts))
    rows = []
    for anchor, cadence in combos:
        mine = [e for e in evts if e["anchor"] == anchor and e["cadence"] == cadence]
        cal = (calendars or {}).get(anchor)
        for stop in STOPS:
            for part in _parts_for(anchor):
                for side in SIDES:
                    group = [e for e in mine if (part == "all" or e["part"] == part)
                             and (side == "both" or e["side"] == side)]
                    used = [e["stops"][stop] for e in group if not e["stops"][stop]["tight"]]
                    n = len(used)
                    row = {"anchor": anchor, "cadence": cadence, "stop": stop, "part": part, "side": side,
                           "n": n, "tight_excluded": len(group) - n}
                    for r in REACH:
                        row["pct_reached_%d" % r] = (100.0 * sum(1 for s in used if s["reached_%d" % r]) / n
                                                     if n else None)
                    row["avg_r_at_flat"] = sum(s["r_at_flat"] for s in used) / n if n else None
                    if cal is None:
                        row["max_gap_trading_days"] = None
                    else:
                        dates = set(e["date"] for e in group if not e["stops"][stop]["tight"])
                        row["max_gap_trading_days"] = _longest_gap(cal, dates)
                    rows.append(row)
    return rows


# ---- plain-English tables -------------------------------------------------------------------------------

_STOP_TITLE = {
    "half_width": "Stop at half the band width",
    "full_width": "Stop at the full band width",
    "to_anchor": "Stop back at the anchor price",
    "opposite_band": "Stop at the opposite edge of the band",
}
_STOP_NOTE = {
    "half_width": "The stop sits half the band's width away from the entry price.",
    "full_width": "The stop sits the band's full width away from the entry price.",
    "to_anchor": "The stop sits at the price the band is built around (the opening price it is anchored to).",
    "opposite_band": "The stop sits at the other edge of the band: below the band for a buy, above it for a sell.",
}
_ANCHOR_NAME = {"0930": "9:30 AM open", "1800": "6:00 PM open"}
_CADENCE_NAME = {"half_hour": "On the half hour", "minute": "Any minute"}
_PART_NAME = {"evening": "Evening, 6 PM to 2 AM", "overnight": "Overnight, 2 AM to 9:30 AM",
              "morning": "Morning, 9:30 to 11:30 AM", "midday": "Midday, 11:30 AM to 2 PM",
              "afternoon": "Afternoon, 2 to 4 PM", "all": "Whole day"}
_SIDE_NAME = {"long": "Buy (closed above)", "short": "Sell (closed below)", "both": "Both"}
_COLUMNS = ("Band built from the", "Breakouts looked for", "Part of the day", "Side", "All breakouts",
            "Measured", "Left out, stop under 10 points", "Reached 2 times the risk",
            "Reached 3 times the risk", "Reached 5 times the risk", "Average result if held to 4 PM, in risks",
            "Longest stretch with no breakout, trading days")


def _pct(x):
    return "-" if x is None else "%.1f%%" % x


def _num(x):
    return "-" if x is None else "%.2f" % x


def tables_md(rows, start, end):
    lines = [
        "# Noise-Area breakouts: the measuring pass",
        "",
        "Trading days %s to %s. No trades were placed; this only measures what price did after each "
        "breakout." % (start, end),
        "",
        "A breakout is the first close outside the noise band after a close inside it (or the first close "
        "of the day, if it is already outside). It is not counted again until price closes back inside. "
        "The entry price is the open of the next minute. \"Reached 2 times the risk\" means price moved in "
        "favour by at least twice the stop distance before the stop was hit. The average result is in "
        "multiples of the stop distance, holding to the day's last bar (4 PM, or earlier on a short day); "
        "a stopped breakout counts as minus one. A stop under 10 points is too tight to use, so those "
        "breakouts are left out of the shares and the average, and counted in their own column. "
        "\"Measured\" is the number the shares are taken over.",
        "",
        "\"On the half hour\" looks at closes on the hour and half hour only (the original rule). "
        "\"Any minute\" looks at every one-minute close. The band is built either from the 9:30 AM open "
        "(the original rule) or from the 6:00 PM open; the 9:30 AM band starts at 9:31 AM, so it has no "
        "evening or overnight rows.",
        "",
    ]
    for stop in STOPS:
        lines += ["## " + _STOP_TITLE[stop], "", _STOP_NOTE[stop], "",
                  "| " + " | ".join(_COLUMNS) + " |",
                  "|" + "|".join(["---"] * 4 + ["---:"] * (len(_COLUMNS) - 4)) + "|"]
        for r in rows:
            if r["stop"] != stop:
                continue
            gap = "-" if r["max_gap_trading_days"] is None else str(r["max_gap_trading_days"])
            cells = [_ANCHOR_NAME[r["anchor"]], _CADENCE_NAME[r["cadence"]], _PART_NAME[r["part"]],
                     _SIDE_NAME[r["side"]], str(r["n"] + r["tight_excluded"]), str(r["n"]),
                     str(r["tight_excluded"]), _pct(r["pct_reached_2"]), _pct(r["pct_reached_3"]),
                     _pct(r["pct_reached_5"]), _num(r["avg_r_at_flat"]), gap]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
    return "\n".join(lines)


def _write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def _events_json(evts):
    if not evts:
        return "[]\n"
    return "[\n" + ",\n".join(json.dumps(e, sort_keys=True, allow_nan=False) for e in evts) + "\n]\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="The Noise-Area measuring pass (no trades).")
    ap.add_argument("--start", default=DEFAULT_START)
    ap.add_argument("--end", default=DEFAULT_END)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--data", default=os.environ.get("PRAXIS_DATA", DEFAULT_DATA))
    ap.add_argument("--allow-later", action="store_true",
                    help="allow an --end later than %s (the measuring pass stops there)" % DEFAULT_END)
    a = ap.parse_args(argv)
    try:
        d0 = _dt.date.fromisoformat(a.start)
        d1 = _dt.date.fromisoformat(a.end)
    except ValueError as exc:
        print("measure: bad date: %s" % exc, file=sys.stderr)
        return 2
    if d1 > _dt.date.fromisoformat(DEFAULT_END) and not a.allow_later:
        print("measure: --end %s is later than %s, where the measuring pass stops; refused "
              "(--allow-later overrides)" % (a.end, DEFAULT_END), file=sys.stderr)
        return 2
    if d0 > d1:
        print("measure: --start %s is after --end %s" % (a.start, a.end), file=sys.stderr)
        return 2
    first = _dt.date.fromisoformat(FIRST_DATE)
    warm = min(d0, max(d0 - _dt.timedelta(days=WARMUP_DAYS), first))
    start, end = d0.isoformat(), d1.isoformat()
    days = globex.load_days(a.data, warm.isoformat(), end)
    os.makedirs(a.out, exist_ok=True)
    all_evts = []
    for anchor in ANCHOR_LIST:
        for cadence in CADENCES:
            evts = events(days, anchor, cadence, first_date=start)
            _write(os.path.join(a.out, "events-%s-%s.json" % (anchor, cadence)), _events_json(evts))
            print("%s %s: %d breakouts" % (_ANCHOR_NAME[anchor], _CADENCE_NAME[cadence].lower(), len(evts)))
            all_evts += evts
    cals = {anchor: calendar(days, anchor, first_date=start) for anchor in ANCHOR_LIST}
    rows = tables(all_evts, calendars=cals)
    _write(os.path.join(a.out, "tables.json"), json.dumps(rows, indent=1, sort_keys=True, allow_nan=False) + "\n")
    _write(os.path.join(a.out, "tables.md"), tables_md(rows, start, end))
    print("wrote %s" % a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
