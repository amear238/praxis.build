#!/usr/bin/env python3
"""bands.py -- the Noise-Area noise band, anchored at the 9:30 AM open or at the 6:00 PM open.

Works on a list of globex.Day (globex.py). sm is globex's session minute: 18:01 is sm 1, 09:31 is sm 931,
16:00 is sm 1320. Stamps mark the END of the minute, so the bar stamped 09:31 is the 9:30 minute.

day_bands(days, k, anchor, lookback=14, mult=1.0) -> {sm: BandPoint} for day index k, one entry per bar of
day k at or after the anchor bar, only where the band exists.

Anchor "0930" -- the published rule, as scripts/wf/oracle/band.py codes it at session start "09:31":
  * open = the open of day k's bar stamped 09:31; prev_close = the close of the last bar of the previous
    day (the nearest earlier day that has a 09:31 bar); a prev_close <= 0 is replaced by the open.
  * upper = max(open, prev_close) * (1 + mult * sigma); lower = min(open, prev_close) * (1 - mult * sigma).
  * anchor_price = open; width = open * mult * sigma.
Anchor "1800":
  * open = the open of day k's bar stamped 18:01, with no previous-close adjustment.
  * upper = open * (1 + mult * sigma); lower = open * (1 - mult * sigma); anchor_price = open;
    width = open * mult * sigma.
Both anchors:
  * A day with no anchor bar has no band, and it is neither used nor counted in other days' sigma.
  * Sigma at minute sm: of the most recent lookback + 15 earlier days that have an anchor bar, walk from the
    newest back; each one that has a bar at sm adds abs(close_at_sm / its_own_anchor_open - 1), until
    lookback of them have been added. Sigma is their mean. Fewer than lookback found: no band at sm.
  * VWAP runs from the anchor bar: typical price (h + l + c) / 3 weighted by volume, bars with volume 0
    skipped; while no volume has been seen, the VWAP is the bar's close.
  * No look-ahead: a band point at sm of day k uses earlier days' bars and day k's bars stamped at or before
    sm only.
The arithmetic keeps band.py's order of operations, so the 9:30 values equal band.py's bit for bit on the
same bars.

This module applies no early-close cut and no holiday calendar: it bands whatever days and bars it is given.

Standard library only. Run with `python3 -I -B`.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from globex import sm_of  # noqa: E402

ANCHORS = {"0930": sm_of("09:31"), "1800": sm_of("18:01")}
EXTRA_LOOKBACK = 15   # the walk reaches back at most lookback + 15 days with an anchor bar (band.py history_cap)


class BandPoint(object):
    __slots__ = ("upper", "lower", "vwap", "anchor_price", "width")

    def __init__(self, upper, lower, vwap, anchor_price, width):
        self.upper, self.lower, self.vwap, self.anchor_price, self.width = upper, lower, vwap, anchor_price, width

    def __repr__(self):
        return "BandPoint(upper=%r lower=%r vwap=%r anchor_price=%r width=%r)" % (
            self.upper, self.lower, self.vwap, self.anchor_price, self.width)


def _check(days, k, anchor, lookback, mult):
    if anchor not in ANCHORS:
        raise ValueError("anchor must be one of %s, got %r" % (sorted(ANCHORS), anchor))
    if not isinstance(lookback, int) or isinstance(lookback, bool) or lookback < 1:
        raise ValueError("lookback must be an int >= 1, got %r" % (lookback,))
    float(mult)
    if not isinstance(k, int) or isinstance(k, bool) or not (0 <= k < len(days)):
        raise IndexError("day index %r out of range (%d days)" % (k, len(days)))


def day_bands(days, k, anchor, lookback=14, mult=1.0):
    """-> {sm: BandPoint} for days[k] (see the module rules). {} when the day has no band at all."""
    _check(days, k, anchor, lookback, mult)
    a_sm = ANCHORS[anchor]
    day = days[k]
    i0 = day.by_sm.get(a_sm)
    if i0 is None:
        return {}
    # Earlier days with an anchor bar, newest first, at most lookback + 15: (by_sm, bars, anchor open).
    cap = lookback + EXTRA_LOOKBACK
    # A day whose anchor open is not > 0 is not used (band.py's CommitDay test); prices never are.
    hist = []
    prev = None                                   # the nearest earlier day with an anchor bar
    j = k - 1
    while j >= 0 and len(hist) < cap:
        d = days[j]
        ia = d.by_sm.get(a_sm)
        if ia is not None:
            if prev is None:
                prev = d
            if d.bars[ia].o > 0:
                hist.append((d.by_sm, d.bars, d.bars[ia].o))
        j -= 1
    if len(hist) < lookback:
        return {}
    open_ = day.bars[i0].o
    if not (open_ > 0):
        return {}
    if anchor == "0930":
        pc = prev.bars[-1].c                      # band.py :194-195
        if not (pc > 0):
            pc = open_
        ref_upper = max(open_, pc)
        ref_lower = min(open_, pc)
    else:
        ref_upper = ref_lower = open_
    out = {}
    cum_pv = 0.0
    cum_vol = 0.0
    bars = day.bars
    for i in range(i0, len(bars)):
        b = bars[i]
        vol = float(b.v)
        if vol > 0:
            cum_pv += ((b.h + b.l + b.c) / 3.0) * vol
            cum_vol += vol
        sm = b.sm
        sum_abs = 0.0
        cnt = 0
        for by_sm, hbars, ho in hist:
            jj = by_sm.get(sm)
            if jj is not None:
                sum_abs += abs(hbars[jj].c / ho - 1.0)
                cnt += 1
                if cnt >= lookback:
                    break
        if cnt < lookback:
            continue
        sigma = sum_abs / cnt
        vwap = cum_pv / cum_vol if cum_vol > 0 else b.c
        out[sm] = BandPoint(ref_upper * (1.0 + mult * sigma), ref_lower * (1.0 - mult * sigma), vwap, open_,
                            open_ * mult * sigma)
    return out

