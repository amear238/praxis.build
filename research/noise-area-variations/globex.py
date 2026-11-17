#!/usr/bin/env python3
"""globex.py -- the NQ 1-minute file cut into full Globex trading days, 6:01 PM to 4:00 PM Eastern.

Data lines are `YYYYMMDD HHMMSS;open;high;low;close;volume`. Stamps are Eastern time and mark the END of
the minute, so the bar stamped 09:31 is the 9:30 minute.

Day rules:
  * A trading day is named by the date its 9:30 AM open belongs to.
  * A bar stamped 18:01 to 23:59 belongs to the trading day of the NEXT calendar day: Sunday evening
    belongs to Monday, Thursday evening to Friday. A bar stamped 00:00 to 16:00 belongs to its own date.
  * Bars stamped 16:01 to 18:00 (the daily break) are dropped.
  * A trading day is kept only if it is Monday to Friday and has at least one bar. So Friday and
    Saturday evening stamps (which would belong to Saturday and Sunday) and weekend daytime stamps are
    dropped: Friday evening does not exist. The real file holds a few such stray bars.
  * Holidays: there is no holiday calendar. A weekday with any bar is a trading day, even when its only
    bars are the evening before and the early morning. A weekday with no bar at all does not appear.
  * Holes: the file has holes inside trading days, where bars are missing for hours (for example a jump
    from 00:00 to 20:00, or from 19:00 to 05:34). A hole is missing data, not a holiday or a halt that the
    loader recognises. load_days keeps every bar regardless (the band needs them all);
    tradable_end(day) says where a day's tradable bars end: the last bar before the day's first gap of
    more than 60 minutes between consecutive bars. Prices taken across a hole are not real fills.
  * Half days: there is no cut. Every bar up to the last one in the file is kept (the RTH loader in
    scripts/wf/oracle/market.py drops bars past its NinjaTrader cut; this loader does not).
  * `start` and `end` bound the trading-day date, both inclusive: the evening before `start` is loaded
    as part of `start`.
  * Every stamp in the file must be strictly later than the one before it, and its seconds must be 00;
    otherwise ValueError. A malformed line also raises ValueError.

sm ("session minute") is minutes after 18:00 of the trading day's evening: stamp 18:01 is sm 1, 00:00 is
360, 09:31 is 931, 16:00 is 1320.

Standard library only. Run with `python3 -I -B`.
"""
import datetime as _dt

_ONE_DAY = _dt.timedelta(days=1)
BREAK_FIRST, BREAK_LAST = "160100", "180000"   # dropped, inclusive


class Bar(object):
    __slots__ = ("dt", "sm", "o", "h", "l", "c", "v")

    def __init__(self, dt, sm, o, h, l, c, v):
        self.dt, self.sm, self.o, self.h, self.l, self.c, self.v = dt, sm, o, h, l, c, v

    def __repr__(self):
        return "Bar(%s sm=%d o=%r h=%r l=%r c=%r v=%d)" % (self.dt.isoformat(" "), self.sm, self.o, self.h,
                                                            self.l, self.c, self.v)


class Day(object):
    __slots__ = ("date", "bars", "by_sm")

    def __init__(self, date):
        self.date = date
        self.bars = []
        self.by_sm = {}

    def __repr__(self):
        return "Day(%s bars=%d)" % (self.date, len(self.bars))


def _sm(hh, mm):
    m = hh * 60 + mm
    if m >= 18 * 60 + 1:
        return m - 18 * 60
    if m <= 16 * 60:
        return m + 6 * 60
    raise ValueError("%02d:%02d is in the daily break (16:01-18:00) and has no session minute" % (hh, mm))


def sm_of(hhmm):
    """'HH:MM' -> minutes after 18:00 of the trading day's evening. '18:01' -> 1, '16:00' -> 1320.
    A time in the break (16:01 to 18:00) raises ValueError."""
    hh, mm = hhmm.split(":")
    hh, mm = int(hh), int(mm)
    if not (0 <= hh < 24 and 0 <= mm < 60):
        raise ValueError("not a time: %r" % (hhmm,))
    return _sm(hh, mm)


def tradable_end(day, max_gap_minutes=60):
    """-> the index in day.bars of the last bar before the day's first gap of MORE than max_gap_minutes
    minutes between consecutive bars (by Bar.dt); len(day.bars) - 1 when there is no such gap (0 for a
    one-bar day). A gap of exactly max_gap_minutes does not end the day."""
    limit = _dt.timedelta(minutes=max_gap_minutes)
    bars = day.bars
    for i in range(1, len(bars)):
        if bars[i].dt - bars[i - 1].dt > limit:
            return i - 1
    return len(bars) - 1


def load_days(path, start="2021-03-08", end="2026-07-17"):
    """-> list of Day in date order, trading days start..end inclusive (see the module rules)."""
    d0 = _dt.date.fromisoformat(start)
    d1 = _dt.date.fromisoformat(end)
    days = []
    cur = None
    trade_of = {}          # 'YYYYMMDD' + evening flag -> 'YYYY-MM-DD' or None (not loaded)
    prev = None
    with open(path, "r", encoding="ascii", newline="") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip("\r\n")
            parts = line.split(";")
            stamp = parts[0]
            if len(parts) != 6 or len(stamp) != 15 or stamp[8] != " " or not (stamp[:8] + stamp[9:]).isdigit():
                raise ValueError("line %d: malformed: %r" % (lineno, line))
            if prev is not None and stamp <= prev:
                raise ValueError("line %d: stamp %s is not after %s (out of order or duplicate)"
                                 % (lineno, stamp, prev))
            prev = stamp
            t = stamp[9:]
            if t[4:] != "00":
                raise ValueError("line %d: stamp %s has seconds" % (lineno, stamp))
            if BREAK_FIRST <= t <= BREAK_LAST:
                continue
            evening = t > BREAK_LAST
            key = (stamp[:8], evening)
            if key in trade_of:
                tdate = trade_of[key]
            else:
                cal = _dt.date(int(stamp[:4]), int(stamp[4:6]), int(stamp[6:8]))
                td = cal + _ONE_DAY if evening else cal
                tdate = td.isoformat() if (td.weekday() < 5 and d0 <= td <= d1) else None
                trade_of[key] = tdate
            if tdate is None:
                continue
            hh, mm = int(t[:2]), int(t[2:4])
            dt = _dt.datetime(int(stamp[:4]), int(stamp[4:6]), int(stamp[6:8]), hh, mm)
            if cur is None or cur.date != tdate:
                cur = Day(tdate)
                days.append(cur)
            sm = _sm(hh, mm)
            cur.by_sm[sm] = len(cur.bars)
            cur.bars.append(Bar(dt, sm, float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]),
                                int(parts[5])))
    return days
