#!/usr/bin/env python3
"""market.py — loaded-bar model of the arm (b) strategy's 1-minute RTH series (unit 2026-11-07-wf-oracles, U3b-2, W1).

Test oracle only (values-spec T6(ii), docs/specs/2026-11-06-walk-forward-values.md:191): it trades nothing
and is not the walk-forward.

What "loaded bars" means here: the bars NT8 feeds `OnBarUpdate` of
`ninjascript/PraxisNoiseAreaBreakoutArmB.cs` (branch origin/arm-b/wf-tunables; read via `git show`, never
checked out) under the RTH template:
  * the session list s1..sN is `scripts/wf/sessions.py`'s (values-spec §5 :83 day rule, SETTLED): Mon-Fri
    dates with >= 1 bar stamped 09:31:00-16:00:00 inside the range; no second calendar is written here;
  * a session's bars are its stamps SESSION_START .. nt8_last_bar inclusive, where SESSION_START is the
    REQUIRED `session_start` argument of load_market, one of two readings (see SESSION_STARTS below; the
    choice between them is escalated, not made here):
      "09:31" -- the values-spec's literal reading (T12(iii) :206 "VWAP from the 09:30 bar"; sessions.py's
                 09:31 day rule; §4 :72 "RTH sessions" for the ATR);
      "08:31" -- OBSERVED fit on the three committed 2026-11-01 NT8 base runs (baseline BandOrVWAP, OppBand,
                 Flat1559: fill rules and T12 (iii)/(iv)/(v) fit every trade only with the 08:31-09:30 bars
                 in the session); UNVERIFIED for arm (b) on the VM.
    The start moves todayOpen, the VWAP anchor (the session's first bar), the session High/Low for the ATR,
    sigma and both bands. Bars past the NT8 cut are DROPPED
    (values-spec §9 oracle input (c) :233). The cut is REPORTED (results report :144-151, OBSERVED there)
    on the results-report rows and the three code-unit days, and INFERRED on every other early-close day
    by sessions.py's NT8_MAP rule (13:15 -> 12:15, 13:00 -> 12:00, 14:03 stays); any other early last bar
    raises sessions.NotSettledBySpec, which propagates;
  * weekend-dated bars are DROPPED. INFERRED (values-spec §9 (b) :232): that NT8's RTH template drops them is
    not observed. If it does not, they enter the history store and the ATR and shift the warm-up;
  * bars stamped outside SESSION_START..16:00:00 are ignored;
  * the session LIST and the s-numbering are sessions.py's at either start (09:31-16:00 day rule). A weekday
    in range with bars only inside SESSION_START..09:30 and none in 09:31-16:00 (possible only at 08:31; on
    the real file: 2021-04-02, 2023-04-07, 2025-01-09, 2026-04-03) is DROPPED, counted and listed in
    Market.pre_open_only_dropped. UNVERIFIED: whether NT8 makes a session of such a day (both choices fit
    the three committed base runs; escalated by the manager). If it does, every later s-number shifts;
  * bars of dates outside [start, end] are not loaded: s1 is the first in-range session, i.e. the oracle
    models an NT8 run whose data starts at `start`.

Standard library only. Run with `python3 -I -B`.
"""
import datetime as _dt
import hashlib
import importlib.util
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WF = os.path.dirname(_HERE)


def _load_sessions():
    """Import scripts/wf/sessions.py by file path (READ-ONLY reuse). scripts/wf is NOT put on sys.path:
    it holds `select.py`, which would shadow the stdlib `select` module. The module is registered as
    sys.modules['sessions'] so that every importer shares one NotSettledBySpec class."""
    path = os.path.join(_WF, "sessions.py")
    mod = sys.modules.get("sessions")
    if mod is not None and os.path.abspath(getattr(mod, "__file__", "")) == path:
        return mod
    spec = importlib.util.spec_from_file_location("sessions", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["sessions"] = mod
    spec.loader.exec_module(mod)
    return mod


sessions = _load_sessions()
DataError = sessions.DataError
NotSettledBySpec = sessions.NotSettledBySpec

# ---- .cs constants (PraxisNoiseAreaBreakoutArmB.cs:50-54) ----
OPEN_MOD = 9 * 60 + 30      # :50 OpenMod    = 570
CLOSE_MOD = 16 * 60         # :51 CloseMod   = 960
FLATTEN_MOD = CLOSE_MOD - 1  # :52 FlattenMod = 959 (Flat1559 only)
ORACLE_MOD = 10 * 60        # :53 OracleMod  = 600
ATR_PERIOD = 14             # :54 AtrPeriod  = 14

# :40-45 enum PraxisNoiseArmBExitPolicy { BandOrVWAP, OppBand, Flat1559 }. By NAME only (values-spec §9 (d)
# :234: ArmB's numeric order differs from the base enum's, so a number is refused).
POLICIES = ("BandOrVWAP", "OppBand", "Flat1559")

# ---- Fill rules. Defaults OBSERVED in docs/reports/2026-11-01-three-strategy-results.md:133-135 (session
# close fills at the CLOSE of the 16:00-stamped bar, within 0.50) and :255 (FlatEOD = OPEN of the 16:00 bar,
# 2 ticks adverse, clipped to the bar range). The VM refits these from T1/T3; they are defaults, not facts
# about the arm (b) runs.
TICK = 0.25
SLIP_TICKS = 2
SLIP = SLIP_TICKS * TICK  # 0.5


class Bar(object):
    """One loaded 1-minute bar. dt = the file stamp (naive, end-of-bar); mod = H*60+M of the stamp, as the
    .cs `int mod = Time[0].Hour * 60 + Time[0].Minute;` (:181)."""
    __slots__ = ("dt", "mod", "o", "h", "l", "c", "v")

    def __init__(self, dt, mod, o, h, l, c, v):
        self.dt, self.mod, self.o, self.h, self.l, self.c, self.v = dt, mod, o, h, l, c, v

    def __repr__(self):
        return "Bar(%s mod=%d o=%r h=%r l=%r c=%r v=%d)" % (self.dt.isoformat(" "), self.mod, self.o, self.h,
                                                             self.l, self.c, self.v)


class Session(object):
    """n = sessions.py's 1-based number; bars = stamps session_start..nt8_last_bar inclusive, in stamp order."""
    __slots__ = ("n", "date", "bars", "nt8_last_bar", "early", "file_last_bar", "cut_dropped")

    def __init__(self, n, date, nt8_last_bar, early, file_last_bar):
        self.n, self.date, self.nt8_last_bar, self.early, self.file_last_bar = n, date, nt8_last_bar, early, file_last_bar
        self.bars = []
        self.cut_dropped = 0   # bars in session_start-16:00 past the NT8 cut (dropped)

    def __repr__(self):
        return "Session(s%d %s bars=%d nt8_last_bar=%s early=%s)" % (self.n, self.date, len(self.bars),
                                                                      self.nt8_last_bar, self.early)


class DayRecord(object):
    """The .cs DayRecord (:58-67) as it stands when the session is committed: Open (:190-191), High/Low (:192-193,
    :208-209), PrevClose (:194-196), Closes minute->Close (:207, a dictionary: a later bar with the same
    minute overwrites). committed mirrors CommitDay's test (:413) plus the s1 drop (:178-179, :203-204)."""
    __slots__ = ("n", "open", "high", "low", "prev_close", "closes", "committed")


class Market(object):
    def __init__(self):
        self.sessions = []     # Session, index n-1
        self.by_date = {}      # 'YYYY-MM-DD' -> Session
        self.index = {}        # datetime -> (n, i)
        self.source = {}       # {'path', 'bytes', 'sha256'}
        self.start = self.end = None
        self.weekend_dates_dropped = 0       # in range (sessions.scan_file)
        self.weekend_dates_whole_file = 0
        self.weekend_bars_dropped = 0        # weekend-dated bars in session_start-16:00, in range
        self.session_start = None            # "09:31" or "08:31" (SESSION_STARTS)
        self.session_start_label = None      # SESSION_STARTS[session_start]
        self.pre_open_only_dropped = []      # 'YYYY-MM-DD' weekdays with bars only in session_start..09:30 (dropped)
        self.pre_open_only_bars_dropped = 0  # their bars
        self.pre_open_bars = 0               # loaded session bars stamped before 09:31 (0 at "09:31")
        self.cut_bars_dropped = 0            # bars past the NT8 early-close cut
        self._records = None
        self._committed_ns = None

    @property
    def N(self):
        return len(self.sessions)

    def session(self, n):
        if not (1 <= n <= len(self.sessions)):
            raise IndexError("no session s%d (N = %d)" % (n, len(self.sessions)))
        return self.sessions[n - 1]

    # ---- per-session DayRecords, built once ----
    def records(self):
        if self._records is None:
            recs = []
            for s in self.sessions:
                r = DayRecord()
                r.n = s.n
                b0 = s.bars[0]
                r.open = b0.o                       # :190-191 todayOpen = Open[0]; today.Open = todayOpen
                hi, lo = b0.h, b0.l                 # :192-193
                closes = {}
                for b in s.bars:
                    closes[b.mod] = b.c             # :207 today.Closes[mod] = Close[0]
                    hi = max(hi, b.h)               # :208 Math.Max(today.High, High[0])
                    lo = min(lo, b.l)               # :209 Math.Min(today.Low, Low[0])
                r.high, r.low, r.closes = hi, lo, closes
                pb = prev_bar(self, s.n, 0)
                if pb is None:
                    r.prev_close = None             # s1: :178 `if (CurrentBar < 1) return;` -- never reached
                else:
                    pc = pb.c                       # :194 prevClose = Close[1] (previous LOADED bar)
                    if pc <= 0:
                        pc = r.open                 # :195 if (prevClose <= 0) prevClose = todayOpen
                    r.prev_close = pc               # :196
                # :178-179 s1's bar 0 returns before IsFirstBarOfSession; its other bars return at :203-204
                # (haveDay false), so `today` stays null and :413 never adds s1. Every later session is
                # added iff Open > 0 and Closes non-empty (:413).
                r.committed = (s.n >= 2) and r.open > 0 and len(closes) > 0
                recs.append(r)
            self._records = recs
            self._committed_ns = [r.n for r in recs if r.committed]
        return self._records


def _hms(hm):
    """'HH:MM' or 'HH:MM:SS' -> 'HHMMSS'."""
    p = hm.split(":")
    return p[0] + p[1] + (p[2] if len(p) > 2 else "00")


# The two session-start readings. The oracle does NOT pick one: every loader takes it as a required argument
# and every printed table / grade sheet names it with its label.
SESSION_STARTS = {
    "09:31": "the values-spec's literal reading (T12(iii) :206 \"VWAP from the 09:30 bar\"; sessions.py's "
             "09:31 day rule; §4 :72 \"RTH sessions\")",
    "08:31": "OBSERVED fit on the three committed 2026-11-01 NT8 base runs (bars from the one stamped 08:31); "
             "UNVERIFIED for arm (b) on the VM",
}
_READINGS = "; ".join('"%s" = %s' % kv for kv in SESSION_STARTS.items())
_MISSING = object()


def check_session_start(session_start):
    """-> the value, or raise: exactly "09:31" or "08:31" (no other spelling)."""
    if session_start is _MISSING:
        raise TypeError("load_market: session_start is REQUIRED (no default; the choice is escalated): give "
                        "session_start= one of the two readings: %s" % _READINGS)
    if not isinstance(session_start, str) or session_start not in SESSION_STARTS:
        raise ValueError("session_start must be exactly one of %s; got %r. The two readings: %s"
                         % (sorted(SESSION_STARTS), session_start, _READINGS))
    return session_start


def session_start_line(market):
    """One printable line naming the market's session start and its label."""
    return "session start: %s — %s" % (market.session_start, market.session_start_label)


def load_market(path, start=sessions.RANGE[0], end=sessions.RANGE[1], *, session_start=_MISSING):
    """Load the loaded-bar model. session_start is REQUIRED ("09:31" or "08:31"; SESSION_STARTS): bars stamped
    session_start..cut (inclusive) belong to the session. Session list and numbering from sessions.scan_file
    (09:31-16:00 day rule at either start; it validates every line with sessions._parse_line and raises
    NotSettledBySpec on an unmapped early close). A second streaming pass reads OHLCV; its sha256 must equal
    scan_file's (same bytes => every line already validated)."""
    session_start = check_session_start(session_start)
    scan = sessions.scan_file(path, start, end)
    m = Market()
    m.start, m.end = start, end
    m.session_start, m.session_start_label = session_start, SESSION_STARTS[session_start]
    m.source = dict(scan["source"])
    m.weekend_dates_dropped = scan["weekend_dates_dropped"]
    m.weekend_dates_whole_file = scan["weekend_dates_whole_file"]
    cut = {}
    for row in scan["sessions"]:
        s = Session(row["n"], row["date"], row["nt8_last_bar"], row["early_close_in_file"], row["last_bar"])
        m.sessions.append(s)
        m.by_date[s.date] = s
        cut[s.date.replace("-", "")] = (s, _hms(s.nt8_last_bar))
    d0, d1 = start.replace("-", ""), end.replace("-", "")
    first, last = _hms(session_start), sessions.RTH_LAST
    day_first = sessions.RTH_FIRST          # "093100": the day rule's first stamp (session list)
    pre_only = {}                           # 'YYYYMMDD' -> bars, weekdays with pre-open bars and no session
    h = hashlib.sha256()
    wk = {}
    with open(path, "rb") as fh:
        for raw in fh:
            h.update(raw)
            line = raw.decode("ascii")
            if line.endswith("\n"):
                line = line[:-1]
            if line.endswith("\r"):
                line = line[:-1]
            parts = line.split(";")
            stamp = parts[0]
            t = stamp[9:]
            if not (first <= t <= last):
                continue                       # outside session_start..16:00: ignored
            d = stamp[:8]
            if not (d0 <= d <= d1):
                continue
            hit = cut.get(d)
            if hit is None:
                w = wk.get(d)
                if w is None:
                    w = wk[d] = _dt.date(int(d[:4]), int(d[4:6]), int(d[6:8])).weekday() >= 5
                if w:
                    m.weekend_bars_dropped += 1   # INFERRED drop (§9 (b))
                    continue
                if t < day_first:
                    # Pre-open-only weekday (only at "08:31"): DROPPED. UNVERIFIED whether NT8 makes it a
                    # session (both choices fit the three committed base runs); escalated by the manager.
                    pre_only[d] = pre_only.get(d, 0) + 1
                    continue
                raise DataError("bar %s on a weekday with no session (calendar mismatch)" % stamp)
            s, cut_t = hit
            if t > cut_t:
                s.cut_dropped += 1                # past the NT8 cut (§9 (c)): dropped
                m.cut_bars_dropped += 1
                continue
            dt = _dt.datetime(int(d[:4]), int(d[4:6]), int(d[6:8]), int(t[:2]), int(t[2:4]), int(t[4:6]))
            if s.bars and not (dt > s.bars[-1].dt):
                raise DataError("bars out of order or duplicated at %s" % stamp)
            s.bars.append(Bar(dt, int(t[:2]) * 60 + int(t[2:4]), float(parts[1]), float(parts[2]),
                              float(parts[3]), float(parts[4]), int(parts[5])))
            if t < day_first:
                m.pre_open_bars += 1
    if h.hexdigest() != m.source["sha256"]:
        raise DataError("data file changed between passes: %s" % path)
    m.pre_open_only_dropped = ["%s-%s-%s" % (d[:4], d[4:6], d[6:8]) for d in sorted(pre_only)]
    m.pre_open_only_bars_dropped = sum(pre_only.values())
    for s in m.sessions:
        if not s.bars:
            # A session with no bar up to its cut would not exist in NT8 and would shift the numbering.
            raise DataError("session s%d %s has no bar up to its NT8 cut %s" % (s.n, s.date, s.nt8_last_bar))
        for i, b in enumerate(s.bars):
            m.index[b.dt] = (s.n, i)
    return m


def prev_bar(market, n, i):
    """The previous LOADED bar (the .cs Close[1], :194): crosses into the previous session's last (cut) bar,
    skipping dropped weekend bars; None for s1 bar 0."""
    if i > 0:
        return market.sessions[n - 1].bars[i - 1]
    if n > 1:
        return market.sessions[n - 2].bars[-1]
    return None


def is_checkpoint(mod):
    """.cs :272 `(Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod`."""
    minute = mod % 60
    return (minute == 0 or minute == 30) and OPEN_MOD < mod < CLOSE_MOD


def check_policy(policy):
    if not isinstance(policy, str) or policy not in POLICIES:
        raise ValueError("ExitPolicy must be one of %s by name (values-spec §9 (d)); got %r" % (POLICIES, policy))
    return policy


def session_flat_mods(policy):
    """.cs :234 flatMod = (ExitPolicy == Flat1559) ? FlattenMod : CloseMod."""
    return FLATTEN_MOD if check_policy(policy) == "Flat1559" else CLOSE_MOD


def is_session_flat(market, n, i, policy):
    """Step (1) of values-spec §4 precedence: the bar is the session's last loaded bar (16:00, or the
    early-close cut 12:00/12:15/14:03 where NT8's exit on session close flattens; .cs :241-244, that
    IsLastBarOfSession is true there is UNVERIFIED) OR bar.mod >= flatMod (:234-235)."""
    s = market.sessions[n - 1]
    return i == len(s.bars) - 1 or s.bars[i].mod >= session_flat_mods(policy)


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def market_fill(bar, buy):
    """Market order filled on `bar` (the bar after the decision): OPEN, SLIP adverse, clipped to [l, h]."""
    return _clamp(bar.o + SLIP if buy else bar.o - SLIP, bar.l, bar.h)


def session_close_fill(bar, buy):
    """NT8 exit on session close: CLOSE of the session's last bar, SLIP adverse, clipped (results :135)."""
    return _clamp(bar.c + SLIP if buy else bar.c - SLIP, bar.l, bar.h)


def flateod_fill(bar_1600, buy):
    """FlatEOD = market fill on the 16:00-stamped bar (results :255)."""
    return market_fill(bar_1600, buy)


class Trade(object):
    __slots__ = ("entry_dt", "exit_dt", "side", "entry_price", "exit_price", "entry_name", "exit_name", "row")

    def __init__(self, entry_dt, exit_dt, side, entry_price, exit_price, entry_name, exit_name, row):
        if side not in ("Long", "Short"):
            raise ValueError("side must be 'Long' or 'Short': %r" % (side,))
        self.entry_dt, self.exit_dt, self.side = entry_dt, exit_dt, side
        self.entry_price, self.exit_price = entry_price, exit_price
        self.entry_name, self.exit_name, self.row = entry_name, exit_name, row   # row: 1-based in the source

    def __repr__(self):
        return "Trade(row=%r %s %s@%r -> %s@%r %s/%s)" % (self.row, self.side, self.entry_dt, self.entry_price,
                                                         self.exit_dt, self.exit_price, self.entry_name, self.exit_name)


class Run(object):
    """params: {'Lookback', 'NoiseMult', 'StopAtrMult', 'ExitPolicy'}; built by grade.py via tradelist.py."""
    __slots__ = ("params", "trades", "source")

    def __init__(self, params, trades=None, source=None):
        self.params, self.trades, self.source = dict(params), list(trades or []), source
