#!/usr/bin/env python3
"""band.py — the arm (b) noise band, sigma and session VWAP, line by line as
ninjascript/PraxisNoiseAreaBreakoutArmB.cs (origin/arm-b/wf-tunables) computes them (unit 2026-11-07-wf-oracles, W1).

Test oracle only (values-spec T6(ii)). INFERRED: .NET 4.8 x64 (RyuJIT, SSE2) double arithmetic is IEEE
binary64 with round-to-nearest and no FMA contraction, i.e. identical to CPython float arithmetic when the
same operations run in the same order; every expression below keeps the .cs order.

CLI: python3 -I -B scripts/wf/oracle/band.py --data FILE --session-start {09:31,08:31} --lookback L --noise-mult k
     --date YYYY-MM-DD --time HH:MM
The session start is a market.load_market argument (REQUIRED; market.SESSION_STARTS); everything here takes
the loaded Market. At "08:31" the pre-open minutes 08:31-09:30 (mod 511-570) can be addressed only as
'HH:MM' strings: an int < 570 is a bar index (bar_index).
"""
import argparse
import bisect
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import market as _mk  # noqa: E402

MAX_INDEX = _mk.OPEN_MOD  # an int < 571 passed as mod_or_i is a bar index; >= 571 is a minute of day


class BandState(object):
    """State after BuildBand (:342-370) on one bar. have_band = the .cs haveBand. sigma/upper/lower are None
    when have_band is False (the .cs leaves curSigma/curUpper/curLower stale then; nothing reads them,
    :221, :273, :398). vwap is the :368 expression evaluated on this bar even when have_band is False (the
    .cs refreshes curVwap only with a band; its only trading reader is behind haveBand, :273/:286/:297).
    ref_upper/ref_lower are the :364-365 values (None when there is no day / todayOpen <= 0)."""
    __slots__ = ("have_band", "sigma", "upper", "lower", "vwap", "vwap_cum_vol", "vwap_cum_pv", "cnt",
                 "ref_upper", "ref_lower", "today_open", "prev_close", "have_day")

    def __init__(self):
        for f in self.__slots__:
            setattr(self, f, None)
        self.have_band = False
        self.have_day = False
        self.cnt = 0

    def as_dict(self):
        return {f: getattr(self, f) for f in self.__slots__}

    def __repr__(self):
        return "BandState(%s)" % ", ".join("%s=%r" % (f, getattr(self, f)) for f in self.__slots__)


def history_cap(lookback):
    """.cs :70 HistoryCap = Lookback + 15."""
    return lookback + 15


def history_for(market, n, lookback):
    """The .cs `history` (:69) as it stands at session n's first bar, after CommitDay (:186, :411-420):
    the committed DayRecords of s2..s(n-1), oldest..newest, trimmed to the last Lookback+15 (:416-417).
    s1 is never committed (:178-179 `if (CurrentBar < 1) return;` skips s1's first bar, the only one with
    IsFirstBarOfSession, so haveDay stays false and `today` stays null, :203-204, :413)."""
    recs = market.records()
    ns = market._committed_ns
    k = bisect.bisect_left(ns, n)            # committed sessions with number < n
    lo = max(0, k - history_cap(lookback))
    return [recs[j - 1] for j in ns[lo:k]]


def _build_band(st, hist, mod, close0, lookback, noise_mult):
    """.cs BuildBand(mod), :342-370, on state st (today_open, prev_close, vwap_cum_* already set)."""
    st.have_band = False                                             # :344
    if not (st.today_open > 0):                                      # :345-346
        return st
    sum_abs = 0.0                                                    # :348
    cnt = 0                                                          # :349
    d = len(hist) - 1                                                # :350 newest -> oldest, while cnt < Lookback
    while d >= 0 and cnt < lookback:
        rec = hist[d]
        c = rec.closes.get(mod)                                      # :354 TryGetValue(mod, out c)
        if rec.open > 0 and c is not None:                           # :354 skip a day lacking this minute
            sum_abs += abs(c / rec.open - 1.0)                       # :356
            cnt += 1                                                 # :357
        d -= 1
    st.cnt = cnt
    st.ref_upper = max(st.today_open, st.prev_close)                 # :364 (locals; reported regardless)
    st.ref_lower = min(st.today_open, st.prev_close)                 # :365
    st.vwap = st.vwap_cum_pv / st.vwap_cum_vol if st.vwap_cum_vol > 0 else close0   # :368
    if cnt < lookback:                                               # :360-361 no band
        return st
    st.sigma = sum_abs / cnt                                         # :363
    st.upper = st.ref_upper * (1.0 + noise_mult * st.sigma)         # :366
    st.lower = st.ref_lower * (1.0 - noise_mult * st.sigma)         # :367
    st.have_band = True                                              # :369
    return st


def _check_params(lookback, noise_mult):
    if not isinstance(lookback, int) or isinstance(lookback, bool) or lookback < 2:
        raise ValueError("Lookback must be an int >= 2 (.cs [Range(2, 60)], :434): %r" % (lookback,))
    float(noise_mult)


def iter_session_states(market, n, lookback, noise_mult):
    """Yield (i, bar, BandState) for every loaded bar of session n, in bar order, one pass (VWAP accumulates
    as :213-218, then BuildBand :220)."""
    _check_params(lookback, noise_mult)
    s = market.session(n)
    if n == 1:
        # s1: the .cs never sets haveDay (:178-179, :203-204): no band, no VWAP, nothing.
        for i, b in enumerate(s.bars):
            yield i, b, BandState()
        return
    hist = history_for(market, n, lookback)
    today_open = s.bars[0].o                                         # :190
    pc = _mk.prev_bar(market, n, 0).c                                # :194 Close[1], previous LOADED bar
    if pc <= 0:                                                      # :195
        pc = today_open
    cum_pv = 0.0                                                     # :198
    cum_vol = 0.0                                                    # :199
    for i, b in enumerate(s.bars):
        vol = float(b.v)                                             # :213 double vol = Volume[0]
        if vol > 0:                                                  # :214
            cum_pv += ((b.h + b.l + b.c) / 3.0) * vol                # :216
            cum_vol += vol                                           # :217
        st = BandState()
        st.have_day = True
        st.today_open, st.prev_close = today_open, pc
        st.vwap_cum_pv, st.vwap_cum_vol = cum_pv, cum_vol
        yield i, b, _build_band(st, hist, b.mod, b.c, lookback, noise_mult)


def _parse_hm(text):
    hh, mm = text.split(":")[:2]
    return int(hh) * 60 + int(mm)


def bar_index(market, n, mod_or_i):
    """Resolve mod_or_i to a bar index of session n: a str 'HH:MM' is a minute; an int < 571 is a bar index;
    an int 571..960 is a minute of day. A minute with no bar, or with more than one bar, raises."""
    s = market.session(n)
    if isinstance(mod_or_i, str):
        mod = _parse_hm(mod_or_i)
    elif isinstance(mod_or_i, int) and not isinstance(mod_or_i, bool):
        if mod_or_i < MAX_INDEX:
            if len(s.bars) >= MAX_INDEX:
                raise ValueError("s%d has >= %d bars: an int index is ambiguous" % (n, MAX_INDEX))
            if not (0 <= mod_or_i < len(s.bars)):
                raise IndexError("s%d has no bar index %d" % (n, mod_or_i))
            return mod_or_i
        mod = mod_or_i
    else:
        raise TypeError("mod_or_i must be an int or 'HH:MM': %r" % (mod_or_i,))
    hits = [i for i, b in enumerate(s.bars) if b.mod == mod]
    if not hits:
        raise KeyError("s%d %s has no loaded bar at minute %02d:%02d" % (n, s.date, mod // 60, mod % 60))
    if len(hits) > 1:
        raise ValueError("s%d %s has %d bars at minute %d" % (n, s.date, len(hits), mod))
    return hits[0]


def band_at(market, n, mod_or_i, lookback, noise_mult):
    """BandState after BuildBand on session n's bar (by minute or index; see bar_index)."""
    target = bar_index(market, n, mod_or_i)
    for i, _b, st in iter_session_states(market, n, lookback, noise_mult):
        if i == target:
            return st
    raise AssertionError("unreachable")


def main(argv=None):
    ap = argparse.ArgumentParser(description="arm (b) band oracle at one bar (test oracle; trades nothing)")
    ap.add_argument("--data", required=True)
    ap.add_argument("--lookback", type=int, required=True)
    ap.add_argument("--noise-mult", type=float, required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--time", required=True, help="HH:MM (bar stamp)")
    ap.add_argument("--session-start", required=True, choices=sorted(_mk.SESSION_STARTS),
                    help="REQUIRED, no default: 09:31 = %s; 08:31 = %s" % (_mk.SESSION_STARTS["09:31"],
                                                                         _mk.SESSION_STARTS["08:31"]))
    ap.add_argument("--start", default=_mk.sessions.RANGE[0])
    ap.add_argument("--end", default=_mk.sessions.RANGE[1])
    a = ap.parse_args(argv)
    m = _mk.load_market(a.data, a.start, a.end, session_start=a.session_start)
    s = m.by_date.get(a.date)
    if s is None:
        print("no session on %s" % a.date)
        return 2
    st = band_at(m, s.n, a.time, a.lookback, a.noise_mult)
    print("oracle values — UNVERIFIED against NT8 until 2a")
    print("source %s sha256 %s" % (m.source["path"], m.source["sha256"]))
    print(_mk.session_start_line(m))
    print("session s%d %s nt8_last_bar %s  Lookback=%d NoiseMult=%r  bar %s" % (s.n, s.date, s.nt8_last_bar,
                                                                               a.lookback, a.noise_mult, a.time))
    for k, v in st.as_dict().items():
        print("%-14s %r" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
