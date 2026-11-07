#!/usr/bin/env python3
"""atr.py — the arm (b) daily ATR(14) and bar-close stop, as ninjascript/PraxisNoiseAreaBreakoutArmB.cs
(origin/arm-b/wf-tunables) computes them (unit 2026-11-07-wf-oracles, W1). Test oracle only.

INFERRED (values-spec §9 (c) :233): NT8's ATR uses each session's bars up to its last (cut) bar; this
module takes High/Low over the cut bars of market.py and PrevClose = the previous loaded bar's close.
INFERRED: .NET double arithmetic = IEEE binary64, same order => same bits as CPython.

CLI: python3 -I -B scripts/wf/oracle/atr.py --data FILE --session-start {09:31,08:31} --date YYYY-MM-DD
The session's High/Low (hence the ATR) depend on the REQUIRED session start (market.SESSION_STARTS).
"""
import argparse
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import market as _mk  # noqa: E402
import band as _band  # noqa: E402

ATR_PERIOD = _mk.ATR_PERIOD  # .cs :54


def atr_at(market, n):
    """(have_atr, atr_sum, atr) as ComputeAtr (:378-392) leaves them for session n (computed on n's first
    bar, :187, from completed sessions only). Lookback-independent: HistoryCap = Lookback+15 >= 17 > 14 at
    every allowed Lookback (:70), so the last 14 records and `history.Count >= 14` do not depend on it.
    When have_atr is False the .cs fields keep their DataLoaded reset values 0.0 (:160-162, never written
    before the first haveAtr), so (False, 0.0, 0.0) is returned. s1: ComputeAtr never runs (:178-179)."""
    market.session(n)
    if n == 1:
        return False, 0.0, 0.0
    hist = _band.history_for(market, n, 2)            # cap 17 at Lookback 2; >= 14 kept (:70)
    if not (len(hist) >= ATR_PERIOD):                 # :380-382
        return False, 0.0, 0.0
    s = 0.0                                           # :384
    for rec in hist[len(hist) - ATR_PERIOD:]:         # :385 oldest -> newest
        s += max(rec.high, rec.prev_close) - min(rec.low, rec.prev_close)   # :388
    return True, s, s / ATR_PERIOD                    # :390-391


def _side(side):
    if side not in ("Long", "Short"):
        raise ValueError("side must be 'Long' or 'Short': %r" % (side,))
    return side


def _m(m):
    if not (m > 0):
        raise ValueError("StopAtrMult must be > 0 for stop use (0 = no stop, .cs :250, :323): %r" % (m,))
    return m


def stop_level(side, fill, m, atr_sum):
    """.cs :330-332: fill - m*(atrSum/AtrPeriod) (long) / fill + m*(atrSum/AtrPeriod) (short), .cs order."""
    _m(m)
    if _side(side) == "Long":
        return fill - m * (atr_sum / ATR_PERIOD)
    return fill + m * (atr_sum / ATR_PERIOD)


def stop_crossed(side, fill, close, m, atr_sum):
    """.cs :255 `AtrPeriod*(stopFill-Close) >= StopAtrMult*stopAtrSum` (long) / :263 `AtrPeriod*(Close-stopFill)
    >= ...` (short), evaluated EXACTLY in rationals (Fraction of each float). A close equal to the level is a
    crossing. With prices on the 0.25 grid and 4m an integer, the .cs binary64 products are exact, so the
    rational result equals the .cs result; that equality is also checked here and a mismatch raises."""
    _m(m)
    F = Fraction
    if _side(side) == "Long":
        exact = F(ATR_PERIOD) * (F(fill) - F(close)) >= F(m) * F(atr_sum)
        flt = ATR_PERIOD * (fill - close) >= m * atr_sum
    else:
        exact = F(ATR_PERIOD) * (F(close) - F(fill)) >= F(m) * F(atr_sum)
        flt = ATR_PERIOD * (close - fill) >= m * atr_sum
    if exact != flt:
        raise ValueError("binary64 and exact stop comparisons disagree (inputs off the 0.25 grid?): "
                         "%s fill=%r close=%r m=%r atr_sum=%r" % (side, fill, close, m, atr_sum))
    return exact


def main(argv=None):
    ap = argparse.ArgumentParser(description="arm (b) ATR(14) oracle for one session (test oracle; trades nothing)")
    ap.add_argument("--data", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--session-start", required=True, choices=sorted(_mk.SESSION_STARTS),
                    help="REQUIRED, no default: 09:31 = %s; 08:31 = %s" % (_mk.SESSION_STARTS["09:31"],
                                                                         _mk.SESSION_STARTS["08:31"]))
    ap.add_argument("--start", default=_mk.sessions.RANGE[0])
    ap.add_argument("--end", default=_mk.sessions.RANGE[1])
    a = ap.parse_args(argv)
    mk = _mk.load_market(a.data, a.start, a.end, session_start=a.session_start)
    s = mk.by_date.get(a.date)
    if s is None:
        print("no session on %s" % a.date)
        return 2
    have, sm, atr = atr_at(mk, s.n)
    print("oracle values — UNVERIFIED against NT8 until 2a")
    print("source %s sha256 %s" % (mk.source["path"], mk.source["sha256"]))
    print(_mk.session_start_line(mk))
    print("session s%d %s nt8_last_bar %s" % (s.n, s.date, s.nt8_last_bar))
    print("have_atr %r" % have)
    print("atr_sum  %r" % sm)
    print("atr      %r" % atr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
