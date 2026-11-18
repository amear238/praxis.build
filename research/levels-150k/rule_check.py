#!/usr/bin/env python3
"""rule_check.py -- the independent rule check for candidate 1 of the levels plan, "fade the first touch of a
marked level" (research/levels-150k/PLAN.md, the sections "Candidate 1: fade the first touch of a marked level.
The exact rule" and "Data and markets"). Written from the plan's text alone, without seeing the engine, so a
misreading in the engine is not copied here. Each check replays the rule from the raw bars and the settings,
then compares the engine's output field by field and returns a list of breaks (empty = clean).

check_market(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None) -> [str]
    got = the engine's per_contract output for one market: {"trades": [...], "armed": {date: [...]}}.
    first / last (ISO dates, optional) limit the trading dates the rule replays; every minute is still read for
    the levels. The engine's records outside that range are not dropped: they show as extra.
check_account(result, per_contract_by_market, specs_by_market, risk_pct, start) -> [str]
    result = the engine's account output; sizing, net, balances, skips and day records are recomputed from the
    per-contract trades by the plan's "Money" paragraph.
replay_market(...) and replay_account(...) return the rule's own output, in the engine's shapes.
check_market2(...) and replay_market2(...), the same arguments, do candidate 2, "break and retest" (PLAN.md,
    "Amendment, 2026-11-18: candidate 2, break and retest. The exact rule", read at commit c105ac1). Its
    "armed" holds (kind, s, R, stop); each trade has level = R and break_ts, the stamp of the break bar's last
    minute. check_account serves both candidates (the money rules are the same).
check_market3(...) and replay_market3(...), the same arguments, do candidate 3, "value area traversal" (PLAN.md,
    "Amendment, 2026-11-18: candidate 3, value area traversal", read at commit 911bd1c). settings = {"name",
    "kind": "VA", "k", "min_rr", "atr_days"}. Its "armed" holds (kind "VA", s, level = N, far = F, stop); each
    trade has level = N, target = F and setup_ts, the stamp of the second signal bar's last minute.
check_market4(...) and replay_market4(...), the same arguments, do candidate 4, "acceleration through a level"
    (PLAN.md, "Amendment, 2026-11-18: candidate 4, acceleration through a level", read at commit 61db1e6).
    settings = {"name", "kind", "k", "target": 3, "atr_days"}. Its "armed" is candidate 2's (kind, s, R, stop);
    each trade has level = R, break_ts and trigger = E, the price of the stop order to enter.
    check_account serves all four candidates.

Trades are matched by (date, side, level), so a wrong entry minute shows as a differing field. The armed sets
are compared date by date as multisets of (kind, side, level, stop), with far added for candidate 3; a date
with an empty list is the same as a date left out. Prices are equal within a millionth of a tick. Money is
computed exactly (rationals) and the engine's figure must lie within half a cent of the exact value, so either
rounding of an exact half cent passes
and a cent off fails; a net must also be a whole number of cents. The realised balance is carried with the
engine's net wherever that net passes, so one disputed half cent never cascades into every later balance.

Speed: the levels of each (date, kind) are drawn once per market and reused across k and target; arming and the
trades are redone per setting. Call all settings of one market before the next market (the last two markets'
prepared data are kept).

Readings
--------
Where the plan's words leave a choice, the most literal reading is taken. The engine follows these.

 R1. Session date: the calendar date of the New York wall-clock stamp plus 7 hours on the clock, so S(D) is every
     minute stamped from 5:00 PM New York on the day before D to before 5:00 PM on D. New York time comes from
     the tz database, daylight saving included.
 R2. "Stamped at or after 9:30", "before 9:30", 9:00, 3:00 PM and 3:55 PM are New York clock times on D itself.
     The previous evening's minutes of S(D) are "before 9:30" and "before 9:00".
 R3. Only trading dates are armed and traded. A session date that is not a trading date arms nothing. Its
     minutes are read only where the rule says "any later minute" (the SW and SD trade-through checks).
 R4. The traded contract T is the contract of D's first minute stamped at or after 9:30 (the P0 minute). A
     minute of T is used unmoved. A minute of another contract c is moved by walking the rolls stamped after
     the minute and at or before the P0 minute, in time order: each roll whose old contract is the current one
     moves it to the new one and adds its gap, stopping when T is first reached. A gap of None on that walk, or
     never reaching T, means the minute cannot be joined. The trading minutes, from 9:30 on, are traded as they
     are (the plan's data check: the contract never changes inside 9:30 to 4:00).
 R5. A kind needs every minute it reads, so one minute that cannot be joined means that kind draws nothing that
     day. PD and VP read S(previous trading date). ON reads S(D) before 9:30. PW reads the S(D') of the prior
     ISO week. SW and SD read every minute from the start of the earliest S(D') they use to before 9:30 on D.
     RN reads no minute.
 R6. Tick grid: every minute price read to draw a level, moved or not, is rounded to the nearest tick. A price
     within a millionth of a tick of halfway rounds up. Trading uses each minute's own prices, unrounded: P0,
     trade-throughs, stop and flat fills, the early close and "worst". This changes a result only where the
     data's tick is finer than the traded contract's (6E, 6A and 6J data carry half ticks of the micro).
 R7. ATR is the mean of adj_high - adj_low over the atr_days (14) daily bars ending at the latest bar whose UTC
     date is before D. ATR itself is not rounded. d = floor(k x ATR / tick) ticks, at least 1 (a 1e-7 tick
     allowance absorbs float noise).
 R8. Hourly bars: one bar for each UTC hour that holds a minute (the same as New York clock hours, since the
     offset is whole hours). A bar's open is its first minute's open, its close its last minute's close. "The 3
     bars before/after" and "consecutive" count bars in the series, so an hour with no minute leaves no gap.
     S(D)'s bars are its minutes stamped before 9:00 on D. D's minutes from 9:00 to 9:29 are not a bar, but they
     are later minutes for the trade-through checks.
 R9. SW and SD need their full count of trading dates (5 and 10) before D. With fewer in the data, that kind
     draws nothing that day. PW uses whatever trading dates the prior ISO week holds. PD and VP need a previous
     trading date.
R10. SW: a swing needs 3 bars before and 3 after it in the series, all with strictly lower highs (a swing high)
     or strictly higher lows (a swing low). One bar can give both. "Later minute": every minute stamped after the
     swing bar's hour and before 9:30 on D. Traded through means a rounded high at least 1 tick above (or low 1
     tick below).
R11. SD: ranges in ticks, compared exactly with A60 = the mean range of every bar used (the 10 dates plus D's
     bars before 9:00). A base "fits" when every base bar's range, the impulse's range and the close condition
     all hold. Lengths 3, 2, 1 are tried in that order and the first fit is the zone. If that zone has been
     traded into, it is not drawn, and no shorter base is tried.
R12. VP: on the rounded grid. A minute's volume is split equally over its high - low + 1 tick prices, computed
     exactly as rationals, not floats. The session's midpoint is (lowest low + highest high) / 2 of S(previous
     trading date). When one side has no next price inside the session's range, the other side is added. "At
     least 70%" is value-area volume >= 0.7 x session volume, exactly.
R13. RN: the plan's steps. For 6J, 1 / (0.5 n) is rounded to the nearest tick for every whole n. Only levels
     inside the 2 x ATR band can be armed, so only those are drawn.
R14. Arming: the side and band filters come first, then the merge. "Within d of P0" means |L - P0| <= d, so
     equal counts as within, and a level at P0 is never armed. "Further than 2 x ATR" means |L - P0| > 2 ATR.
     A level within a millionth of a tick of a bound is on it. Merge: |L - L'| <= d to one already taken, so
     equal is dropped. Two levels on one side at the same distance from P0 (the same price) are taken in the
     plan's kind order PD, ON, PW, SW, RN, VP, SD, then the earlier drawn (SW: the swing bar's time; SD: the
     impulse bar's time; PD and PW: the high before the low; VP: top, point of control, bottom). The later one
     is dropped.
R15. Entry minutes: those stamped from 9:30 to before 3:00 PM on D. Trade-through for a long: the raw low <= L
     minus 1 tick (short: high >= L plus 1 tick). The fill is at L even when the minute opens beyond L. A
     level's fate is fixed at its first trade-through. If a position is open at that minute (its entry minute
     through its exit minute, both included), the level is spent. If not, it fills, unless another level traded
     through on the same minute is nearer the minute's open; that one fills and the rest are spent. A tie for
     nearer the open goes to the level nearer P0, then to the long.
R16. Stop on the entry minute: if the entry minute itself opened at or beyond the stop, it is a gap stop on that
     minute with the open as reference, even though the fill was at L. "At or below" and "reaches" are <= (>= for
     shorts), within a millionth of a tick. Target: the high >= target + 1 tick (short: low <= target - 1 tick).
     The target is entry + T x the stop distance, on the tick grid.
R17. Flat: the first minute of S(D) stamped at or after 3:55 PM on D, at any time up to 4:59 PM. It fills at open
     minus slippage for a long (plus for a short), kept inside [low, high]. If S(D) has no such minute, the
     trade closes at the close of S(D)'s last minute (reason "flat", gap False, exit_ts that minute).
R18. worst = the minimum over the held minutes of (adverse extreme - entry) x side, entry and exit minutes
     included. For any "flat" exit (the 3:55 flat and an early close), the exit minute counts only at its exit
     price. So an early close on the entry minute counts only the close, and worst can then be favourable.
R19. Money: loss for one = (dist + slip) x pv + comm. Contracts = floor(balance_start x risk% / 100 / loss for
     one), computed exactly, then capped. A trade under one contract is listed in "skipped" and leaves no other
     mark: no money, and no day record if the date has no other trade. It does not change the per-contract
     trades, which are sized nowhere: the market still held that trade for the one-position rule and for spent
     levels. Within a date, trades are in market
     order (the key order of per_contract_by_market), then entry_ts. Day low = min(start + the sum of (worst x pv
     x qty - comm x qty), start, end).
R20. Midpoint stop fill: floor((reference + low) / 2 to the tick) for a long and ceil((reference + high) / 2 to
     the tick) for a short, with a 1e-7 tick allowance for float noise.

Candidate 2, break and retest. R1 to R20 hold unless one below changes them.

R21. The armed set is candidate 1's, after its filters and merge and in its order, each level turned to the
     other side: s = minus candidate 1's side. "armed" lists every one of them, with s, R and the stop, whether
     or not it is ever broken.
R22. 15-minute bars are quarter hours on the New York clock (:00, :15, :30, :45; the UTC quarter hours are the
     same, the offset being whole hours). They hold D's minutes stamped from 9:30 to before 3:00 PM, so they are
     exactly the bars starting 9:30 to 2:45 PM. A quarter with a single minute is a bar. A bar's close is its
     last minute's own close, unrounded (R6: trading prices are raw).
R23. The break: a bar's close >= R + 1 tick for s = +1, or <= R - 1 tick for s = -1, within a millionth of a
     tick. The first such bar breaks the level for the rest of the day, whatever price does afterwards. Only the
     closes decide it: an open position, a spent level and the bar's high and low play no part. break_ts is the
     stamp of the break bar's last minute.
R24. The retest window runs from the next minute in the data after the break bar's last minute, to the last
     minute stamped before 3:00 PM. A break on the bar starting at 2:45 PM therefore leaves no minute to retest
     in, and that level never trades. This follows from the plan's two windows; it is written here so the
     window is never stretched past 3:00 PM.
R25. The retest fill: a long when a raw low <= R - 1 tick, a short when a raw high >= R + 1 tick, filled at R
     even when the minute opens beyond R. A broken level's fate is fixed at its first such minute in its
     window, as in R15. If a position is open then (its entry minute through its exit minute, both included),
     the level is spent. If not, it fills, unless another broken level meets its fill condition on that minute
     and its R is nearer the open.
R26. Ties go first to the R nearer the minute's open, then to the level nearer P0, by |R - P0|. That is the
     retest price, not candidate 1's level, and the two differ for a zone. Then the long. Two broken levels with
     the same R and the same s (a zone's far edge lying on another level) are still tied: the one candidate 1's
     arming took first fills (R14's order).
R27. The exits, worst and the money are candidate 1's (R16 to R20), with entry R and target R + s x T x the stop
     distance. A trade's level is R and its kind is the armed level's kind.

Candidate 3, value area traversal. R1 to R20 hold unless one below changes them. R21 to R27 do not apply.

R28. The set-up. VAH and VAL are the VP kind's top and bottom (R12), drawn on S(previous trading date) joined to
     D's traded contract (R4, R5). The point of control plays no part. P0 is raw (R6). The set-up is a short when
     P0 >= VAH + 1 tick and a long when P0 <= VAL - 1 tick, within a millionth of a tick. A P0 between the
     edges, on one, or only half a tick beyond one (6E, 6A and 6J data) is no set-up. There is no set-up without
     ATR (R7), without a previous trading date, or when one minute of that session cannot be joined (R5). d is
     R7's. N, F and the stop are on the tick grid. A value area of one or two prices still sets up, though no
     close can then be inside it.
R29. 30-minute bars are half hours on the New York clock (:00 and :30; the UTC half hours are the same, the offset
     being whole hours), holding D's minutes from 9:30. Only bars starting 9:30 to 2:00 PM can be in the pair, so
     only minutes before 2:30 PM are read for it. A bar starts at its half hour on the clock, not at its first
     minute: a 2:00 PM bar whose first minute is 2:10 PM can be the second bar. A bar's close is its last
     minute's own close, unrounded (R6). A half hour with no minute leaves no gap in the series.
R30. Inside: VAL + 1 tick <= close <= VAH - 1 tick, within a millionth of a tick. A close on VAL or VAH is not
     inside.
R31. The pair is at the first i in the bar series where bars i and i + 1 both close inside and bar i + 1 starts at
     or before 2:00 PM. Three inside bars in a row give the first two. A lone inside bar does not spoil the day.
     The first bar may be the one starting 9:30. Once the pair is found, no later pair is looked at, whether it
     is the filter, the entry minute or that minute's open that stops the trade. A bar holds every minute of its
     half hour, so a second bar starting at 2:30 PM leaves its next minute at or after 3:00 PM. The 2:00 PM limit
     and the 3:00 PM entry window (R33) therefore never disagree on a trade. The limit is kept as written.
R32. The filter: reward = |F - C| and risk = |C - stop|, with C the second bar's raw close, never the fill. The
     trade is taken when reward >= m x risk, within a millionth of a tick, so the equal case is taken. m = 0
     always takes it.
R33. The entry minute is the minute right after the second bar's last minute in the data, whatever its stamp.
     There is no trade when there is no such minute, or when it is stamped at or after 3:00 PM on D. A gap in
     the data, an early close or the end of the data can make it a minute of the next session, which is after
     3:00 PM on D: no trade. A minute stamped before 3:00 PM on D is always in S(D).
R34. The entry fill: a long at min(open + slip, high), a short at max(open - slip, low), raw prices. There is no
     trade when a long's entry minute opens at or below the stop or at or above F (a short: at or above the
     stop, or at or below F), within a millionth of a tick. The fill after slippage may still lie at or beyond
     F (an open one tick short of F with two ticks of slippage). The trade is then taken, its target stays F,
     and a target exit fills at F for a loss or for nothing.
R35. A trade: kind "VA", level N, target F, entry the fill, stop N - s x d, dist (entry - stop) x s (off the tick
     grid when the fill is), and setup_ts, the stamp of the second bar's last minute.
R36. The exits and worst are R16 to R18 with entry = the fill and target = F. The stop counts from the entry minute.
     That minute never opens at or beyond the stop (R34), so it is never a gap stop. The target counts from the
     next minute (long: high >= F + 1 tick, filled at F). Then flat at 3:55 PM, and the early close at S(D)'s
     last minute. worst counts the entry minute's whole low (a short: its high), though the fill came at its
     open (R18).
R37. "armed" holds one record for each trading date with a set-up, {"kind": "VA", "side", "level": N, "far": F,
     "stop"}, whatever became of the pair. It is compared as a multiset of (kind, side, level, far, stop) on the
     tick grid.
R38. Settings: kind "VA", k, min_rr (m, any number >= 0; the grid uses 0, 2 and 3) and atr_days (14 if absent).
     No target multiple is read. check_account compares setup_ts wherever a trade carries one, as it does
     break_ts.

Candidate 4, acceleration through a level. R1 to R23 hold. R27 holds with entry = the entry stop's fill (R46) and
target = entry + s x 3 x the stop distance (R47). R24 to R26 (candidate 2's retest) are replaced by R40 to R45.
R28 to R38 do not apply.

R39. The armed set, its order, "armed", R and the stop are candidate 2's (R21): a line's R is the level and its
     stop R - s x d; a zone's R is its far edge and its stop d beyond its near edge. The break and break_ts are
     R23's, on R22's bars, whatever any position or entry is doing.
R40. The trigger E: long, the highest raw high over every minute of the break bar, plus one tick; short, the
     lowest raw low, minus one tick. Not the last minute's extreme and not the close. E is raw, never rounded to
     the grid (R6), so on data carrying half ticks of the traded contract (6E, 6A, 6J) it can lie half a tick
     off the grid. A trade's trigger field is E.
R41. The window: from the next minute in the data after the break bar's last minute to the last minute stamped
     before 3:00 PM on D, then the entry lapses. The break bar's own minutes never act on its entry: none can
     meet E, which lies beyond their extreme, and one reaching the stop cancels nothing, the order not yet
     resting. A break on the bar starting 2:45 PM leaves no minute (as R24), and nor does any break whose next
     minute is at or after 3:00 PM.
R42. The three steps, for one entry on one minute, in the amendment's order. Long: step 1, open <= stop; step 2,
     high >= E; step 3, low <= stop. Short: open >= stop, low <= E, high >= stop. Each is within a millionth of
     a tick, so an open exactly at the stop cancels, a high exactly at E triggers, and a low exactly at the stop
     with E unmet cancels. An entry's fate is fixed on the first minute of its window where any step acts. As the
     open lies inside the minute's range, that is the first minute whose high meets E or whose low reaches the
     stop. A minute that meets E and reaches the stop, but opens above the stop, triggers (step 2 comes before
     step 3) and is then stopped on that same minute (R48).
R43. Steps 1 and 3 act whatever else is going on: a resting entry is cancelled by its stop while another position
     is open, too. A cancelled, spent or lapsed entry leaves no record; it shows only in "armed".
R44. A position is open from its entry minute to its exit minute, both included (R15). An entry whose trigger is
     met on such a minute is spent, on the exit minute as well, whatever the exit. A level broken while a
     position is open has its entry resting from the minute after its break bar like any other (R23); it fills
     when its deciding minute (R42) comes after the exit minute.
R45. Ties: only the entries whose step 2 is met on one minute while no position is open are in it. One cancelled
     by step 1 on that minute is not. The key is |E - open|, then |R - open|, then |R - P0|, then the long, then
     candidate 1's arming order (R14). Each distance is absolute and in ticks, compared within a millionth of a
     tick, so an open beyond E counts its distance past E. Entries of one side broken by the same bar share E,
     so R decides. A long and a short can never be met on one minute: each long's stop lies above P0 and each
     short's below (candidate 1 arms a level only more than d from P0), so whichever side breaks later closes
     its break bar beyond the other side's stop, and that cancels or fills the other first. "Then the long" is
     therefore never reached; it is kept as written. Equal E, equal R and one side occur when a zone's far edge
     lies on a line level more than d from the zone's near edge; candidate 1's arming order decides.
R46. The entry fill is the exit stop's fill turned round (R20's arithmetic). Long: the reference is the open when
     the open >= E (within a millionth of a tick), else E. Midpoint (reference + high) / 2 rounded up to the
     tick; kind min(reference + slip, high); harsh the high. Short: the open when it is <= E; (reference + low)
     / 2 rounded down; max(reference - slip, low); the low. Raw prices. An open exactly at E fills the same
     either way.
R47. The trade: entry = the fill; stop = candidate 2's; dist = (entry - stop) x s, unrounded, so it carries the
     fill; target = entry + s x 3 x dist, rounded to the nearest tick as R6 rounds. With a fill on the grid the
     target is already on it, and with half-tick data 4 x entry - 3 x stop is too, so the rounding only removes
     float noise. level = R, kind = the armed level's kind.
R48. The exits and worst are R16 to R18 from the entry minute: the stop checked on the entry minute (never a gap
     there, by step 1), the target from the next minute (high >= target + 1 tick, filled at the target), flat at
     3:55 PM, the early close at S(D)'s last minute. worst counts the entry minute's whole adverse extreme (a
     long: its low, though the fill came at or above E), as R36.
R49. fill sets the entry stop's fill and the exit stop's fill together.
R50. Trades are matched by (date, side, R) as in candidate 2. Two entries with one R and one side share E and
     their window, so at most one of them trades (the other loses the tie or is cancelled first) and the key
     stays unique.
R51. Settings: kind (the seven and ALL), k, target (3; absent is read as 3; anything else is refused) and
     atr_days (14 if absent).
R52. check_account compares trigger, as a price within a millionth of a tick, wherever a trade carries one.

Standard library only. Python 3.14, run with python3 -I -B.
"""
import bisect
import math
import operator
import os
import sys
from array import array
from collections import Counter, namedtuple
from datetime import date, datetime, timedelta
from fractions import Fraction
from itertools import compress, islice
from zoneinfo import ZoneInfo

_HERE = os.path.dirname(os.path.abspath(__file__))
_TREND = os.path.normpath(os.path.join(_HERE, "..", "trend-150k"))
if _TREND not in sys.path:
    sys.path.append(_TREND)         # appended, so the trend pass's own rule_check.py never shadows this one
import mdata  # noqa: E402  (the data types Bar, Adj and Roll; the plan's data are read with it)

NY = ZoneInfo("America/New_York")
NS = 1_000_000_000
DAY_NS = mdata.DAY_NS
HOUR_NS = 3600 * NS
_EPOCH = date(1970, 1, 1).toordinal()
KINDS = ("PD", "ON", "PW", "SW", "RN", "VP", "SD")
FILLS = ("midpoint", "kind", "harsh-stops")
RN_STEP = {"NQ": 100, "ES": 50, "RTY": 25, "CL": 1.0, "GC": 25, "ZN": 0.5, "ZB": 1,
           "6E": 0.005, "6B": 0.005, "6A": 0.005, "6J": "yen"}
SW_DATES, SD_DATES, SWING_SIDE = 5, 10, 3
_EPS = 1e-6         # a millionth of a tick: prices this close are equal
_Q = 1e-7           # float-noise allowance, in ticks, when rounding down or up to the tick
_INF = float("inf")
_NAME = {1: "long", -1: "short"}
_UNDER = "under one contract"


class _NoJoin(Exception):
    """A minute the kind needs cannot be joined to the traded contract (R4, R5)."""


# An armed level, prices in ticks. L = the level (candidate 1) or R (candidates 2 and 4); near = |L - P0|;
# brk = the index of the break bar's last minute (candidates 2 and 4); order = its place in candidate 1's arming.
_Lv = namedtuple("_Lv", "kind side L stop dist near brk order", defaults=(None, 0))
QUARTER_NS = 900 * NS
HALF_NS = 1800 * NS


# ------------------------------------------------------------------------------------------------ the clock
def _iso(day):
    return date.fromordinal(_EPOCH + day).isoformat()


def _dayno(iso):
    return date.fromisoformat(iso).toordinal() - _EPOCH


def _ny_ns(day, hh, mm):
    """UTC nanoseconds of hh:mm New York time on the day numbered `day`."""
    d = date.fromordinal(_EPOCH + day)
    return int(datetime(d.year, d.month, d.day, hh, mm, tzinfo=NY).timestamp()) * NS


def session_date(ts):
    """The plan's session date (ISO) of a minute stamped ts (UTC ns): the calendar date of its New York wall-clock
    stamp plus 7 hours."""
    wall = datetime.fromtimestamp(ts // NS, NY).replace(tzinfo=None)
    return (wall + timedelta(hours=7)).date().isoformat()


# ------------------------------------------------------------------------------------------------ one market, prepared
class _Prep:
    """The minutes of one market cut into session dates, with each (date, kind)'s levels cached."""

    def __init__(self, minutes, daily, rolls, spec, market):
        self.src = (minutes, daily, rolls)
        self.market = market
        self.tick = float(spec["tick"])
        n = self.n = len(minutes)
        ts = self.ts = array("q", (b.ts for b in minutes))
        if n > 1 and not all(map(operator.lt, ts, islice(ts, 1, None))):
            raise ValueError("minutes are not in strictly increasing time order")
        self.o = array("d", (b.open for b in minutes))
        self.h = array("d", (b.high for b in minutes))
        self.l = array("d", (b.low for b in minutes))
        self.c = array("d", (b.close for b in minutes))
        self.v = array("q", (b.volume for b in minutes))
        iid = [b.iid for b in minutes]
        self.rolls = sorted(rolls, key=lambda r: r.ts)
        self.roll_ts = [r.ts for r in self.rolls]
        # runs: stretches of one contract with no roll stamp inside, so one shift serves the whole run
        cuts = set(compress(range(1, n), map(operator.ne, iid, islice(iid, 1, None))))
        for t in self.roll_ts:
            p = bisect.bisect_left(ts, t)
            if 0 < p < n:
                cuts.add(p)
        self.run_start = ([0] + sorted(cuts)) if n else []
        self.run_end = self.run_start[1:] + [n]
        self.run_iid = [iid[s] for s in self.run_start]
        self.run_k = [bisect.bisect_right(self.roll_ts, ts[s]) for s in self.run_start]
        # session dates (R1) and trading dates
        self.sess, self.tinfo, self.trading = {}, {}, []
        if n:
            d0 = datetime.fromtimestamp(ts[0] // NS, NY).date().toordinal() - _EPOCH
            d1 = datetime.fromtimestamp(ts[-1] // NS, NY).date().toordinal() - _EPOCH + 1
            nxt = _ny_ns(d0 - 1, 17, 0)
            for D in range(d0, d1 + 1):
                cur, nxt = nxt, _ny_ns(D, 17, 0)
                s0 = bisect.bisect_left(ts, cur)
                s1 = bisect.bisect_left(ts, nxt, s0)
                if s1 == s0:
                    continue
                self.sess[D] = (s0, s1)
                i930 = bisect.bisect_left(ts, _ny_ns(D, 9, 30), s0, s1)
                i1555 = bisect.bisect_left(ts, _ny_ns(D, 15, 55), i930, s1)
                if i1555 > i930:                    # a minute stamped from 9:30 to before 3:55 PM
                    i900 = bisect.bisect_left(ts, _ny_ns(D, 9, 0), s0, i930)
                    i1500 = bisect.bisect_left(ts, _ny_ns(D, 15, 0), i930, i1555)
                    self.tinfo[D] = (s0, s1, i900, i930, i1500, i1555)
                    self.trading.append(D)
        self.sess_days = sorted(self.sess)
        self.tindex = {D: k for k, D in enumerate(self.trading)}
        self.dday = [a.bar.ts // DAY_NS for a in daily]
        self.drng = [a.adj_high - a.adj_low for a in daily]
        self._shift, self._groups, self._levels, self._chains, self._ctx = {}, {}, {}, {}, {}
        self._clock = {}

    # -------------------------------------------------------------------------------------- prices on the grid
    def _rt(self, p):
        """Nearest tick, in ticks; within a millionth of a tick of halfway rounds up (R6)."""
        return math.floor(p / self.tick + 0.5 + _EPS)

    def ctx(self, D):
        """(traded contract, number of rolls stamped at or before the P0 minute)."""
        c = self._ctx.get(D)
        if c is None:
            i930 = self.tinfo[D][3]
            r = bisect.bisect_right(self.run_start, i930) - 1
            c = self._ctx[D] = (self.run_iid[r], bisect.bisect_right(self.roll_ts, self.ts[i930]))
        return c

    def shift(self, r, T, kmax):
        """The price shift that joins run r to contract T (R4), or None."""
        c = self.run_iid[r]
        if c == T:
            return 0.0
        k0 = self.run_k[r]
        key = (c, k0, T, kmax)
        if key in self._shift:
            return self._shift[key]
        cur, add, res = c, 0.0, None
        for roll in self.rolls[k0:kmax]:
            if roll.old_iid != cur:
                continue
            if roll.gap is None:
                break
            add += roll.gap
            cur = roll.new_iid
            if cur == T:
                res = add
                break
        self._shift[key] = res
        return res

    def _runs(self, a, b):
        r = bisect.bisect_right(self.run_start, a) - 1
        while r < len(self.run_start) and self.run_start[r] < b:
            yield r, max(a, self.run_start[r]), min(b, self.run_end[r])
            r += 1

    def ext(self, a, b, T, kmax):
        """(highest high, lowest low) in ticks of minutes [a, b) joined to T; None when empty."""
        if a >= b:
            return None
        hi, lo = -_INF, _INF
        for r, ra, rb in self._runs(a, b):
            s = self.shift(r, T, kmax)
            if s is None:
                raise _NoJoin
            hi = max(hi, self._rt(max(self.h[ra:rb]) + s))
            lo = min(lo, self._rt(min(self.l[ra:rb]) + s))
        return hi, lo

    def groups(self, a, b):
        """Minutes [a, b) cut by UTC hour and by run: [(hour, run, open, high, low, close)], raw prices."""
        key = (a, b)
        g = self._groups.get(key)
        if g is None:
            g, ts, i = [], self.ts, a
            while i < b:
                hr = ts[i] // HOUR_NS
                e = bisect.bisect_left(ts, (hr + 1) * HOUR_NS, i, b)
                for r, ra, rb in self._runs(i, e):
                    g.append((hr, r, self.o[ra], max(self.h[ra:rb]), min(self.l[ra:rb]), self.c[rb - 1]))
                i = e
            self._groups[key] = g
        return g

    def hourly(self, D, ndates, T, kmax):
        """The hourly bars for SW or SD (R8), with suffix extremes of every later minute up to 9:30 on D.
        -> (bars [[o, h, l, c, hour]], last item of each bar, suffix highs, suffix lows) or None (R9)."""
        ti = self.tindex[D]
        if ti < ndates:
            return None
        used = set(self.trading[ti - ndates:ti])
        s0, _s1, i900, i930 = self.tinfo[D][:4]
        bars, last, items = [], [], []
        rt = self._rt

        def add(gs, is_bar):
            for hr, r, go, gh, gl, gc in gs:
                s = self.shift(r, T, kmax)
                if s is None:
                    raise _NoJoin
                ht, lt = rt(gh + s), rt(gl + s)
                items.append((ht, lt))
                if not is_bar:
                    continue
                if bars and bars[-1][4] == hr:
                    b = bars[-1]
                    b[1], b[2], b[3] = max(b[1], ht), min(b[2], lt), rt(gc + s)
                    last[-1] = len(items) - 1
                else:
                    bars.append([rt(go + s), ht, lt, rt(gc + s), hr])
                    last.append(len(items) - 1)

        lo_i = bisect.bisect_left(self.sess_days, self.trading[ti - ndates])
        hi_i = bisect.bisect_left(self.sess_days, D)
        for sd in self.sess_days[lo_i:hi_i]:
            add(self.groups(*self.sess[sd]), sd in used)
        add(self.groups(s0, i900), True)
        add(self.groups(i900, i930), False)
        m = len(items)
        suf_h, suf_l = [-_INF] * (m + 1), [_INF] * (m + 1)
        for p in range(m - 1, -1, -1):
            suf_h[p] = max(suf_h[p + 1], items[p][0])
            suf_l[p] = min(suf_l[p + 1], items[p][1])
        return bars, last, suf_h, suf_l

    # -------------------------------------------------------------------------------------- reference values
    def prev_trading(self, D):
        ti = self.tindex[D]
        return self.trading[ti - 1] if ti else None

    def atr(self, D, n_atr):
        j = bisect.bisect_left(self.dday, D) - 1        # the latest daily bar dated (UTC) before D
        if j < n_atr - 1:
            return None
        return sum(self.drng[j - n_atr + 1:j + 1]) / n_atr

    def p0(self, D):
        return self.o[self.tinfo[D][3]]

    # -------------------------------------------------------------------------------------- the seven kinds
    def levels(self, D, kind, n_atr):
        """[(L in ticks, zone or None, order)]; zone = (+1, bottom) demand or (-1, top) supply."""
        key = (D, kind, n_atr) if kind == "RN" else (D, kind)
        lv = self._levels.get(key)
        if lv is not None:
            return lv
        T, kmax = self.ctx(D)
        try:
            lv = getattr(self, "_lv_" + kind.lower())(D, T, kmax, n_atr)
        except _NoJoin:
            lv = []
        self._levels[key] = lv
        return lv

    def _hilo(self, e):
        return [] if e is None else [(e[0], None, 0), (e[1], None, 1)]

    def _lv_pd(self, D, T, kmax, n_atr):
        P = self.prev_trading(D)
        return [] if P is None else self._hilo(self.ext(*self.sess[P], T, kmax))

    def _lv_on(self, D, T, kmax, n_atr):
        s0, _s1, _i900, i930 = self.tinfo[D][:4]
        return self._hilo(self.ext(s0, i930, T, kmax))

    def _lv_pw(self, D, T, kmax, n_atr):
        mon = D - date.fromordinal(_EPOCH + D).weekday() - 7      # Monday of the ISO week before D's
        a = bisect.bisect_left(self.trading, mon)
        b = bisect.bisect_left(self.trading, mon + 7)
        hi, lo = -_INF, _INF
        for P in self.trading[a:b]:
            e = self.ext(*self.sess[P], T, kmax)
            hi, lo = max(hi, e[0]), min(lo, e[1])
        return [] if a == b else [(hi, None, 0), (lo, None, 1)]

    def _lv_sw(self, D, T, kmax, n_atr):
        hb = self.hourly(D, SW_DATES, T, kmax)
        if hb is None:
            return []
        bars, last, suf_h, suf_l = hb
        out, w = [], SWING_SIDE
        for i in range(w, len(bars) - w):
            hi, lo = bars[i][1], bars[i][2]
            around = bars[i - w:i] + bars[i + 1:i + 1 + w]
            if all(hi > b[1] for b in around) and suf_h[last[i] + 1] <= hi:
                out.append((hi, None, 2 * i))
            if all(lo < b[2] for b in around) and suf_l[last[i] + 1] >= lo:
                out.append((lo, None, 2 * i + 1))
        return out

    def _lv_sd(self, D, T, kmax, n_atr):
        hb = self.hourly(D, SD_DATES, T, kmax)
        if hb is None:
            return []
        bars, last, suf_h, suf_l = hb
        N = len(bars)
        S = sum(b[1] - b[2] for b in bars)          # A60 = S / N
        out = []
        for j in range(1, N):
            if N * (bars[j][1] - bars[j][2]) < 2 * S:           # the impulse: range >= 2 x A60
                continue
            cj = bars[j][3]
            for blen in (3, 2, 1):
                if j - blen < 0:
                    continue
                base = bars[j - blen:j]
                if any(2 * N * (b[1] - b[2]) > S for b in base):    # each base bar: range <= 0.5 x A60
                    continue
                top, bot = max(b[1] for b in base), min(b[2] for b in base)
                if cj > top:
                    if suf_l[last[j] + 1] >= top:
                        out.append((top, (1, bot), j))
                elif cj < bot:
                    if suf_h[last[j] + 1] <= bot:
                        out.append((bot, (-1, top), j))
                else:
                    continue
                break
        return out

    def _lv_vp(self, D, T, kmax, n_atr):
        P = self.prev_trading(D)
        if P is None:
            return []
        a, b = self.sess[P]
        rows = []
        for r, ra, rb in self._runs(a, b):
            s = self.shift(r, T, kmax)
            if s is None:
                raise _NoJoin
            for i in range(ra, rb):
                rows.append((self._rt(self.l[i] + s), self._rt(self.h[i] + s), self.v[i]))
        lo0, hi0 = min(x[0] for x in rows), max(x[1] for x in rows)
        if any(hi < lo for lo, hi, _ in rows):
            raise ValueError(f"{self.market} {_iso(P)}: a minute's high is below its low")
        unit = math.lcm(*{hi - lo + 1 for lo, hi, _ in rows})     # volumes in units of 1/unit: exact (R12)
        diff = [0] * (hi0 - lo0 + 2)
        total = 0
        for lo, hi, v in rows:
            w = v * (unit // (hi - lo + 1))
            diff[lo - lo0] += w
            diff[hi - lo0 + 1] -= w
            total += v * unit
        vol, acc = [], 0
        for x in diff[:-1]:
            acc += x
            vol.append(acc)
        best = max(vol)
        mid2 = lo0 + hi0                                # twice the session's midpoint, in ticks
        poc = min((abs(2 * (lo0 + i) - mid2), i) for i, x in enumerate(vol) if x == best)[1]
        lo_i = hi_i = poc
        acc, top = vol[poc], len(vol) - 1
        while acc * 100 < total * 70:
            up, dn = hi_i < top, lo_i > 0
            if up and dn:
                va, vb = vol[hi_i + 1], vol[lo_i - 1]
                if va >= vb:
                    hi_i += 1
                    acc += va
                if vb >= va:
                    lo_i -= 1
                    acc += vb
            elif up:
                hi_i += 1
                acc += vol[hi_i]
            elif dn:
                lo_i -= 1
                acc += vol[lo_i]
            else:
                break
        return [(lo0 + hi_i, None, 0), (lo0 + poc, None, 1), (lo0 + lo_i, None, 2)]

    def _lv_rn(self, D, T, kmax, n_atr):
        atr = self.atr(D, n_atr)
        if atr is None:
            return []
        tick, p0 = self.tick, self.p0(D)
        lo_p, hi_p = p0 - 2 * atr - tick, p0 + 2 * atr + tick
        step = RN_STEP.get(self.market)
        if step is None:
            raise ValueError(f"no round-number step for market {self.market!r}")
        if step == "yen":
            if hi_p <= 0:
                return []
            lo_p = max(lo_p, tick)
            return [(self._rt(1 / (0.5 * n)), None, n)
                    for n in range(max(1, math.floor(2 / hi_p)), math.ceil(2 / lo_p) + 1)]
        return [(round(n * step / tick), None, n)
                for n in range(math.ceil(lo_p / step), math.floor(hi_p / step) + 1)]

    # -------------------------------------------------------------------------------------- the trading minutes
    def clock_bars(self, D, width):
        """D's bars on the clock, `width` ns wide, from 9:30: the index of each bar's last minute, in time order.
        They hold exactly D's minutes stamped from 9:30 to before 3:00 PM (R22, R29)."""
        q = self._clock.get((D, width))
        if q is None:
            i930, i1500 = self.tinfo[D][3], self.tinfo[D][4]
            q, i = [], i930
            while i < i1500:
                e = bisect.bisect_left(self.ts, (self.ts[i] // width + 1) * width, i, i1500)
                q.append(e - 1)
                i = e
            self._clock[(D, width)] = q
        return q

    def quarters(self, D):
        """Candidate 2's 15-minute bars of D, the ones starting 9:30 to 2:45 PM (R22)."""
        return self.clock_bars(D, QUARTER_NS)

    def chains(self, D):
        """Next strictly lower low and next strictly higher high of each minute from the P0 minute on."""
        ch = self._chains.get(D)
        if ch is None:
            _s0, s1, _i900, i930 = self.tinfo[D][:4]
            nl, nh = [s1] * (s1 - i930), [s1] * (s1 - i930)
            for arr, nxt, better in ((self.l, nl, operator.lt), (self.h, nh, operator.gt)):
                st = []
                for i in range(i930, s1):
                    x = arr[i]
                    while st and better(x, arr[st[-1]]):
                        nxt[st.pop() - i930] = i
                    st.append(i)
            ch = self._chains[D] = (nl, nh)
        return ch


def _first(arr, nxt, base, m, x, stop_at, le):
    """The first index in [m, stop_at) with arr <= x (le) or arr >= x (not le); stop_at if none."""
    if le:
        while m < stop_at:
            if arr[m] <= x:
                return m
            m = nxt[m - base]
    else:
        while m < stop_at:
            if arr[m] >= x:
                return m
            m = nxt[m - base]
    return stop_at


_CACHE = []
_CACHE_SIZE = 2


def _prep(minutes, daily, rolls, spec, market):
    for p in _CACHE:
        if (p.src[0] is minutes and p.src[1] is daily and p.src[2] is rolls and p.market == market
                and p.tick == float(spec["tick"]) and p.n == len(minutes)):
            return p
    p = _Prep(minutes, daily, rolls, spec, market)
    _CACHE.insert(0, p)
    del _CACHE[_CACHE_SIZE:]
    return p


def clear_cache():
    del _CACHE[:]


# ------------------------------------------------------------------------------------------------ arming and trading
def _d_ticks(atr, k, tick):
    """The stop distance d in ticks: k x ATR rounded down to the tick, at least one tick (R7)."""
    return max(math.floor(k * atr / tick + _Q), 1)


def _arm(prep, D, kinds, k, n_atr):
    atr = prep.atr(D, n_atr)
    if atr is None:
        return []
    tick = prep.tick
    d = _d_ticks(atr, k, tick)
    p0, band = prep.p0(D) / tick, 2 * atr / tick
    sides = {1: [], -1: []}
    for kind in kinds:
        ko = KINDS.index(kind)
        for L, zone, seq in prep.levels(D, kind, n_atr):
            gap = L - p0
            near = abs(gap)
            if near <= d + _EPS or near > band + _EPS:
                continue
            side = 1 if gap < 0 else -1
            if zone is not None and zone[0] != side:
                continue
            sides[side].append((near, ko, seq, L, zone, kind))
    armed = []
    for side in (1, -1):
        taken = None
        for near, _ko, _seq, L, zone, kind in sorted(sides[side], key=lambda x: x[:3]):
            if taken is not None and abs(L - taken) <= d:
                continue
            taken = L
            stop = (L if zone is None else zone[1]) - side * d
            armed.append(_Lv(kind, side, L, stop, (L - stop) * side, near, None, len(armed)))
    return armed


def _arm2(prep, D, kinds, k, n_atr):
    """Candidate 2's armed set: candidate 1's, each traded the other way (R21)."""
    a1 = _arm(prep, D, kinds, k, n_atr)
    if not a1:
        return []
    d = _d_ticks(prep.atr(D, n_atr), k, prep.tick)
    p0 = prep.p0(D) / prep.tick
    out = []
    for a in a1:
        s = -a.side
        R = a.stop + a.side * d             # candidate 1's stop is d beyond the far edge: R is the far edge
        stop = a.L - s * d                  # d beyond the near edge, which is the level itself for a line
        out.append(_Lv(a.kind, s, R, stop, abs(R - stop), abs(R - p0), None, a.order))
    return out


def _stop_fill(o, h, l, stop, side, slip, tick, fill):
    eps = tick * _EPS
    if side > 0:
        gap = o <= stop + eps
        ref = o if gap else stop
        if fill == "kind":
            return max(ref - slip, l), gap
        if fill == "midpoint":
            return math.floor((ref + l) / 2 / tick + _Q) * tick, gap
        return l, gap
    gap = o >= stop - eps
    ref = o if gap else stop
    if fill == "kind":
        return min(ref + slip, h), gap
    if fill == "midpoint":
        return math.ceil((ref + h) / 2 / tick - _Q) * tick, gap
    return h, gap


def _fill_minute(prep, D, a, start):
    """The first minute from `start` to before 3:00 PM whose price trades a tick through a.L against the side
    (a long: low <= L - 1 tick), or None."""
    tick, eps = prep.tick, prep.tick * _EPS
    i930, i1500 = prep.tinfo[D][3], prep.tinfo[D][4]
    nl, nh = prep.chains(D)
    if a.side > 0:
        f = _first(prep.l, nl, i930, start, (a.L - 1) * tick + eps, i1500, True)
    else:
        f = _first(prep.h, nh, i930, start, (a.L + 1) * tick - eps, i1500, False)
    return f if f < i1500 else None


def _touches1(prep, D, armed):
    """Candidate 1: each armed level's first trade-through from 9:30."""
    out = []
    for a in armed:
        f = _fill_minute(prep, D, a, prep.tinfo[D][3])
        if f is not None:
            out.append((f, a))
    return out


def _break(prep, D, a):
    """Candidates 2 and 4: the index of the last minute of a's break bar, the first 15-minute bar closing a tick
    beyond R in the direction s (R22, R23), or None."""
    tick, eps, C = prep.tick, prep.tick * _EPS, prep.c
    if a.side > 0:
        x = (a.L + 1) * tick - eps
        return next((j for j in prep.quarters(D) if C[j] >= x), None)
    x = (a.L - 1) * tick + eps
    return next((j for j in prep.quarters(D) if C[j] <= x), None)


def _touches2(prep, D, armed):
    """Candidate 2: each armed level's break bar (R22, R23), then its first retest minute after it (R24, R25)."""
    out = []
    for a in armed:
        brk = _break(prep, D, a)
        if brk is None:
            continue
        f = _fill_minute(prep, D, a, brk + 1)
        if f is not None:
            out.append((f, a._replace(brk=brk)))
    return out


def _exit(prep, D, f, side, entry, stop, target, fill, slip):
    """Candidate 1's exits for a position entered at `entry` on minute f (prices in points; target None = no
    target): flat at 3:55 PM, the stop from f, the target from f + 1, the early close (R16 to R18).
    -> (exit minute, exit price, reason, gap, worst)."""
    tick, eps = prep.tick, prep.tick * _EPS
    _s0, s1, _i900, i930, _i1500, i1555 = prep.tinfo[D]
    O, H, L, C = prep.o, prep.h, prep.l, prep.c
    nl, nh = prep.chains(D)
    flat = i1555 if i1555 < s1 else None
    lim = s1 if flat is None else flat
    if side > 0:
        s = _first(L, nl, i930, f, stop + eps, lim, True)
        g = lim if target is None else _first(H, nh, i930, f + 1, target + tick - eps, lim, False)
    else:
        s = _first(H, nh, i930, f, stop - eps, lim, False)
        g = lim if target is None else _first(L, nl, i930, f + 1, target - tick + eps, lim, True)
    gap = False
    if s < lim and s <= g:
        x, reason = s, "stop"
        px, gap = _stop_fill(O[x], H[x], L[x], stop, side, slip, tick, fill)
    elif g < lim:
        x, reason, px = g, "target", target
    elif flat is not None:
        x, reason = flat, "flat"
        px = min(max(O[x] - side * slip, L[x]), H[x])
    else:
        x, reason, px = s1 - 1, "flat", C[s1 - 1]
    held_to = x if reason == "flat" else x + 1      # a flat exit's minute counts only at its fill
    worst = (px - entry) * side if reason == "flat" else _INF
    if held_to > f:
        ext = min(L[f:held_to]) if side > 0 else max(H[f:held_to])
        worst = min(worst, (ext - entry) * side)
    return x, px, reason, gap, worst


def _trade_day(prep, D, touches, t_mult, fill, slip, market):
    """The day's trades from [(fill-condition minute, armed level)]: one position at a time, spent levels, the
    nearer-the-open rule, then the exits."""
    tick = prep.tick
    O, TS = prep.o, prep.ts
    touches = sorted(touches, key=lambda x: x[0])
    out, busy, q = [], -1, 0
    while q < len(touches):
        f = touches[q][0]
        group = []
        while q < len(touches) and touches[q][0] == f:
            group.append(touches[q][1])
            q += 1
        if f <= busy:                       # traded through while a position is open, or on its exit minute
            continue
        op = O[f] / tick
        a = min(group, key=lambda g: (round(abs(g.L - op), 6), round(g.near, 6), -g.side, g.order))
        side, entry, stop = a.side, a.L * tick, a.stop * tick
        target = None if t_mult is None else (a.L + side * t_mult * a.dist) * tick
        x, px, reason, gap, worst = _exit(prep, D, f, side, entry, stop, target, fill, slip)
        t = {"market": market, "date": _iso(D), "kind": a.kind, "level": entry, "side": side,
             "entry_ts": TS[f], "entry": entry, "stop": stop, "dist": a.dist * tick, "target": target,
             "exit_ts": TS[x], "exit": px, "reason": reason, "gap": gap,
             "points": (px - entry) * side, "worst": worst}
        if a.brk is not None:
            t["break_ts"] = TS[a.brk]
        out.append(t)
        busy = x
    return out


def _settings(settings):
    kind = settings["kind"]
    if kind != "ALL" and kind not in KINDS:
        raise ValueError(f"unknown kind {kind!r}")
    t = settings.get("target")
    if t is not None and t <= 0:
        raise ValueError(f"target {t!r} is not a positive multiple")
    return (KINDS if kind == "ALL" else (kind,)), float(settings["k"]), t, int(settings.get("atr_days", 14))


def _window(first, last):
    return (-_INF if first is None else _dayno(first)), (_INF if last is None else _dayno(last))


def _replay(arm, touches, minutes, daily, rolls, spec, settings, fill, market, first, last, day=_trade_day):
    if fill not in FILLS:
        raise ValueError(f"fill {fill!r} is not one of {FILLS}")
    kinds, k, t_mult, n_atr = _settings(settings)
    prep = _prep(minutes, daily, rolls, spec, market)
    tick, slip = prep.tick, spec["slip_ticks"] * float(spec["tick"])
    lo, hi = _window(first, last)
    trades, armed_out = [], {}
    for D in prep.trading:
        if not lo <= D <= hi:
            continue
        armed = arm(prep, D, kinds, k, n_atr)
        if not armed:
            continue
        armed_out[_iso(D)] = [{"kind": a.kind, "side": a.side, "level": a.L * tick, "stop": a.stop * tick}
                              for a in armed]
        trades.extend(day(prep, D, touches(prep, D, armed), t_mult, fill, slip, market))
    return {"trades": trades, "armed": armed_out}


def replay_market(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 1, the rule's own per_contract output for one market: {"trades": [...], "armed": {...}}."""
    return _replay(_arm, _touches1, minutes, daily, rolls, spec, settings, fill, market, first, last)


def replay_market2(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 2 (break and retest), the same shape: "armed" holds (kind, s, R, stop) and each trade has
    level = R and break_ts."""
    return _replay(_arm2, _touches2, minutes, daily, rolls, spec, settings, fill, market, first, last)


# ------------------------------------------------------------------------------------------------ candidate 3
def _settings3(settings):
    """(k, m, atr_days) of a candidate 3 setting (R38)."""
    if settings.get("kind") != "VA":
        raise ValueError(f"candidate 3 takes kind 'VA', not {settings.get('kind')!r}")
    m = float(settings["min_rr"])
    if not m >= 0:
        raise ValueError(f"min_rr {settings['min_rr']!r} is not a number >= 0")
    return float(settings["k"]), m, int(settings.get("atr_days", 14))


def _setup3(prep, D, k, n_atr):
    """D's set-up (R28): (s, N, F, stop) in ticks, or None."""
    atr = prep.atr(D, n_atr)
    if atr is None:
        return None
    vp = {seq: L for L, _zone, seq in prep.levels(D, "VP", n_atr)}
    if not vp:
        return None
    vah, val = vp[0], vp[2]
    p0 = prep.p0(D) / prep.tick
    if p0 >= vah + 1 - _EPS:
        s, N, F = -1, vah, val
    elif p0 <= val - 1 + _EPS:
        s, N, F = 1, val, vah
    else:
        return None
    return s, N, F, N - s * _d_ticks(atr, k, prep.tick)


def _signal3(prep, D, val, vah):
    """The index of the second bar's last minute of D's first inside pair (R29 to R31), or None."""
    tick, eps = prep.tick, prep.tick * _EPS
    lo_in, hi_in = (val + 1) * tick - eps, (vah - 1) * tick + eps
    C, TS = prep.c, prep.ts
    t1400 = _ny_ns(D, 14, 0)
    bars = prep.clock_bars(D, HALF_NS)
    for a, b in zip(bars, bars[1:]):
        if TS[b] // HALF_NS * HALF_NS > t1400:          # the second bar starts after 2:00 PM
            return None
        if lo_in <= C[a] <= hi_in and lo_in <= C[b] <= hi_in:
            return b
    return None


def _trade3(prep, D, setup, m, fill, slip, market):
    """D's trade from its set-up (R29 to R36), or None."""
    s, N, F, stop = setup
    tick, eps = prep.tick, prep.tick * _EPS
    O, H, L, C, TS = prep.o, prep.h, prep.l, prep.c, prep.ts
    sig = _signal3(prep, D, min(N, F), max(N, F))
    if sig is None:
        return None
    c = C[sig] / tick
    if abs(F - c) < m * abs(c - stop) - _EPS:          # the filter, on the signal close (R32)
        return None
    f = sig + 1                                         # the next minute in the data (R33)
    if f >= prep.tinfo[D][4]:
        return None
    o, stop_px, far = O[f], stop * tick, F * tick
    if s > 0:
        if o <= stop_px + eps or o >= far - eps:
            return None
        entry = min(o + slip, H[f])
    else:
        if o >= stop_px - eps or o <= far + eps:
            return None
        entry = max(o - slip, L[f])
    x, px, reason, gap, worst = _exit(prep, D, f, s, entry, stop_px, far, fill, slip)
    return {"market": market, "date": _iso(D), "kind": "VA", "level": N * tick, "side": s,
            "entry_ts": TS[f], "entry": entry, "stop": stop_px, "dist": (entry - stop_px) * s, "target": far,
            "setup_ts": TS[sig], "exit_ts": TS[x], "exit": px, "reason": reason, "gap": gap,
            "points": (px - entry) * s, "worst": worst}


def replay_market3(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 3 (value area traversal), the rule's own per_contract output for one market: "armed" holds one
    (kind "VA", s, N, F, stop) a date with a set-up, and each trade has level = N, target = F and setup_ts."""
    if fill not in FILLS:
        raise ValueError(f"fill {fill!r} is not one of {FILLS}")
    k, m, n_atr = _settings3(settings)
    prep = _prep(minutes, daily, rolls, spec, market)
    tick, slip = prep.tick, spec["slip_ticks"] * float(spec["tick"])
    lo, hi = _window(first, last)
    trades, armed_out = [], {}
    for D in prep.trading:
        if not lo <= D <= hi:
            continue
        setup = _setup3(prep, D, k, n_atr)
        if setup is None:
            continue
        s, N, F, stop = setup
        armed_out[_iso(D)] = [{"kind": "VA", "side": s, "level": N * tick, "far": F * tick, "stop": stop * tick}]
        t = _trade3(prep, D, setup, m, fill, slip, market)
        if t is not None:
            trades.append(t)
    return {"trades": trades, "armed": armed_out}


# ------------------------------------------------------------------------------------------------ candidate 4
def _settings4(settings):
    """Candidate 4's target is fixed at 3 (R51): absent or 3 is read as 3, anything else is refused."""
    t = settings.get("target", 3)
    if isinstance(t, bool) or t != 3:
        raise ValueError(f"candidate 4's target is 3 times the risk, not {t!r}")
    return dict(settings, target=3)


def _touches4(prep, D, armed):
    """Candidate 4: each armed entry's break bar (R22, R23), its trigger E (R40) and the minute its trigger is
    met first in its window, before any cancel (R41 to R43). -> [(minute, armed entry with brk, E in points)]."""
    tick, eps = prep.tick, prep.tick * _EPS
    i930, i1500 = prep.tinfo[D][3], prep.tinfo[D][4]
    O, H, L = prep.o, prep.h, prep.l
    nl, nh = prep.chains(D)
    q = prep.quarters(D)
    out = []
    for a in armed:
        brk = _break(prep, D, a)
        if brk is None:
            continue
        p = bisect.bisect_left(q, brk)
        b0 = q[p - 1] + 1 if p else i930                    # the break bar's first minute
        stop, w = a.stop * tick, brk + 1                    # the window opens on the next minute in the data
        if a.side > 0:
            E = max(H[b0:brk + 1]) + tick
            hit = _first(H, nh, i930, w, E - eps, i1500, False)         # step 2: high >= E
            cut = _first(L, nl, i930, w, stop + eps, i1500, True)       # steps 1 and 3: low <= stop
            beyond = hit < i1500 and O[hit] <= stop + eps
        else:
            E = min(L[b0:brk + 1]) - tick
            hit = _first(L, nl, i930, w, E + eps, i1500, True)
            cut = _first(H, nh, i930, w, stop - eps, i1500, False)
            beyond = hit < i1500 and O[hit] >= stop - eps
        if hit >= i1500 or cut < hit or beyond:            # lapsed, cancelled by step 3, cancelled by step 1
            continue
        out.append((hit, a._replace(brk=brk), E))
    return out


def _tie4(op, g):
    """The tie key of g = (armed entry, E) on a minute opening at op, in ticks (R45)."""
    a, E = g
    return (round(abs(E - op), 6), round(abs(a.L - op), 6), round(a.near, 6), -a.side, a.order)


def _trade_day4(prep, D, touches, t_mult, fill, slip, market):
    """Candidate 4's trades from [(trigger minute, armed entry, E)]: one position at a time, spent entries and the
    tie, the entry stop's fill, then candidate 1's exits (R44 to R48)."""
    tick = prep.tick
    O, H, L, TS = prep.o, prep.h, prep.l, prep.ts
    touches = sorted(touches, key=lambda x: x[0])
    out, busy, q = [], -1, 0
    while q < len(touches):
        f = touches[q][0]
        group = []
        while q < len(touches) and touches[q][0] == f:
            group.append(touches[q][1:])
            q += 1
        if f <= busy:                       # triggered while a position is open, or on its exit minute: spent
            continue
        op = O[f] / tick
        a, E = min(group, key=lambda g: _tie4(op, (g[0], g[1] / tick)))
        side, stop = a.side, a.stop * tick
        entry = _stop_fill(O[f], H[f], L[f], E, -side, slip, tick, fill)[0]     # a stop order, turned (R46)
        dist = (entry - stop) * side
        target = prep._rt(entry + side * t_mult * dist) * tick
        x, px, reason, gap, worst = _exit(prep, D, f, side, entry, stop, target, fill, slip)
        out.append({"market": market, "date": _iso(D), "kind": a.kind, "level": a.L * tick, "side": side,
                    "entry_ts": TS[f], "entry": entry, "stop": stop, "dist": dist, "target": target,
                    "break_ts": TS[a.brk], "trigger": E, "exit_ts": TS[x], "exit": px, "reason": reason,
                    "gap": gap, "points": (px - entry) * side, "worst": worst})
        busy = x
    return out


def replay_market4(minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 4 (acceleration through a level), the rule's own per_contract output for one market: "armed" is
    candidate 2's (kind, s, R, stop) and each trade has level = R, break_ts and trigger = E."""
    return _replay(_arm2, _touches4, minutes, daily, rolls, spec, _settings4(settings), fill, market, first, last,
                   _trade_day4)


# ------------------------------------------------------------------------------------------------ comparing
def _fmt(x):
    return f"{x:.10g}" if isinstance(x, float) else repr(x)


def _px_eq(a, b, tol):
    try:
        return abs(a - b) <= tol
    except TypeError:
        return False


def _field_breaks(breaks, label, mine, theirs, fields, tol):
    for f, how in fields:
        if f not in theirs:
            breaks.append(f"{label}: field {f} missing")
            continue
        m, t = mine[f], theirs[f]
        if how == "px":
            ok = _px_eq(m, t, tol)
        elif how == "pxn":
            ok = (m is None and t is None) or (m is not None and t is not None and _px_eq(m, t, tol))
        else:
            ok = m == t and type(m) is type(t) if isinstance(m, bool) else m == t
        if not ok:
            breaks.append(f"{label}: {f} is {_fmt(t)}, rule says {_fmt(m)}")


_T_FIELDS = (("market", "eq"), ("date", "eq"), ("kind", "eq"), ("level", "px"), ("side", "eq"),
             ("entry_ts", "eq"), ("entry", "px"), ("stop", "px"), ("dist", "px"), ("target", "pxn"),
             ("exit_ts", "eq"), ("exit", "px"), ("reason", "eq"), ("gap", "eq"), ("points", "px"),
             ("worst", "px"))


def _tick_key(x, tick, tol):
    """The tick index of a price, or the price itself when it is not on the grid."""
    k = round(x / tick)
    return k if abs(k * tick - x) <= tol else ("off the tick grid", x)


def _trade_label(market, date_, side, level):
    return f"{market} {date_}: trade {_NAME.get(side, side)} at {_fmt(level)}"


def _compare_trades(breaks, market, mine, theirs, tick, tol, fields, keyf):
    try:
        ets = [t["entry_ts"] for t in theirs]
        if ets != sorted(ets):
            breaks.append(f"{market}: trades are not in entry order")
    except (KeyError, TypeError):
        pass
    mk = {keyf(t): t for t in mine}
    tk = {}
    for t in theirs:
        try:
            k = keyf(t)
        except (KeyError, TypeError, ZeroDivisionError):
            breaks.append(f"{market}: unreadable trade record {t!r}")
            continue
        if k in tk:
            breaks.append(f"{market}: trade {k} listed twice")
        tk[k] = t
    for k in sorted(set(mk) - set(tk), key=str):
        t = mk[k]
        breaks.append(f"{_trade_label(market, t['date'], t['side'], t['level'])}: missing "
                      f"(the rule makes this trade: {t!r})")
    for k in sorted(set(tk) - set(mk), key=str):
        t = tk[k]
        breaks.append(f"{_trade_label(market, t.get('date'), t.get('side'), t.get('level'))}: extra "
                      f"(the rule makes no such trade: {t!r})")
    for k in sorted(set(mk) & set(tk), key=str):
        t = mk[k]
        _field_breaks(breaks, _trade_label(market, t["date"], t["side"], t["level"]), t, tk[k], fields, tol)


_ARM_WORD = {"level": "at", "far": "far", "stop": "stop"}


def _compare_armed(breaks, market, mine, theirs, tick, tol, pfields=("level", "stop")):
    if not isinstance(theirs, dict):
        breaks.append(f"{market}: armed is not a dict of dates")
        return
    for d in sorted(set(mine) | set(theirs)):
        m = Counter((a["kind"], a["side"]) + tuple(round(a[f] / tick) for f in pfields) for a in mine.get(d, []))
        t = Counter()
        for a in theirs.get(d, []) or []:
            try:
                t[(a["kind"], a["side"]) + tuple(_tick_key(a[f], tick, tol) for f in pfields)] += 1
            except (KeyError, TypeError):
                breaks.append(f"{market} {d}: unreadable armed record {a!r}")

        def say(x):
            px = " ".join(f"{_ARM_WORD[f]} {_fmt(v * tick if isinstance(v, int) else v[1])}"
                          for f, v in zip(pfields, x[2:]))
            return f"{x[0]} {_NAME.get(x[1], x[1])} {px}"
        for x in sorted((m - t).elements(), key=str):
            breaks.append(f"{market} {d}: armed level {say(x)} missing (the rule arms it)")
        for x in sorted((t - m).elements(), key=str):
            breaks.append(f"{market} {d}: armed level {say(x)} extra (the rule does not arm it)")


def check_market(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 1: breaks between the engine's per_contract output for one market and the rule's replay."""
    if fill not in FILLS:
        return [f"fill {fill!r} is not one of {FILLS}"]
    mine = replay_market(minutes, daily, rolls, spec, settings, fill, market, first, last)
    return _check(got, mine, spec, market, _T_FIELDS)


_T2_FIELDS = _T_FIELDS + (("break_ts", "eq"),)


def check_market2(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 2 (break and retest): breaks between the engine's per_contract output and the rule's replay."""
    if fill not in FILLS:
        return [f"fill {fill!r} is not one of {FILLS}"]
    mine = replay_market2(minutes, daily, rolls, spec, settings, fill, market, first, last)
    return _check(got, mine, spec, market, _T2_FIELDS)


_T3_FIELDS = _T_FIELDS + (("setup_ts", "eq"),)


def check_market3(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 3 (value area traversal): breaks between the engine's per_contract output and the rule's
    replay."""
    if fill not in FILLS:
        return [f"fill {fill!r} is not one of {FILLS}"]
    mine = replay_market3(minutes, daily, rolls, spec, settings, fill, market, first, last)
    return _check(got, mine, spec, market, _T3_FIELDS, ("level", "far", "stop"))


_T4_FIELDS = _T_FIELDS + (("break_ts", "eq"), ("trigger", "px"))


def check_market4(got, minutes, daily, rolls, spec, settings, fill, market, first=None, last=None):
    """Candidate 4 (acceleration through a level): breaks between the engine's per_contract output and the rule's
    replay."""
    if fill not in FILLS:
        return [f"fill {fill!r} is not one of {FILLS}"]
    mine = replay_market4(minutes, daily, rolls, spec, settings, fill, market, first, last)
    return _check(got, mine, spec, market, _T4_FIELDS)


def _check(got, mine, spec, market, fields, armed_fields=("level", "stop")):
    tick = float(spec["tick"])
    tol = tick * _EPS
    breaks = []
    if not isinstance(got, dict):
        return [f"{market}: the engine's output is not a dict"]
    _compare_armed(breaks, market, mine["armed"], got.get("armed", {}), tick, tol, armed_fields)
    _compare_trades(breaks, market, mine["trades"], got.get("trades", []), tick, tol, fields,
                    lambda t: (t["date"], t["side"], _tick_key(t["level"], tick, tol)))
    return breaks


# ------------------------------------------------------------------------------------------------ the account
def _fr(x):
    """A spec figure (dollars a point, commission, risk %) as the exact decimal it is written as."""
    return Fraction(repr(float(x)))


def _fq(x):
    """A price or price difference, exact at the data's 1e-9 resolution."""
    return Fraction(round(x * 1e9), 10 ** 9)


def _cents(x):
    """The exact Fraction, to the cent, as a float (half away from zero; the check accepts either side)."""
    c = x * 100
    n = math.floor(c + Fraction(1, 2)) if c >= 0 else -math.floor(-c + Fraction(1, 2))
    return n / 100


def _within_half_cent(t, exact):
    try:
        return abs(Fraction(t) - exact) <= Fraction(1, 200) + Fraction(1, 10 ** 9)
    except (TypeError, ValueError, OverflowError):
        return False


def _whole_cents(t):
    try:
        return abs(t * 100 - round(t * 100)) <= 1e-6
    except TypeError:
        return False


def _account(per_contract_by_market, specs_by_market, risk_pct, start, theirs_net=None):
    """The rule's account. theirs_net(key) -> the engine's net for that trade or None; a net within half a cent
    of the exact value is carried into the balance in place of the rule's own rounding."""
    markets = list(per_contract_by_market)
    order = {m: i for i, m in enumerate(markets)}
    rows = []
    for m in markets:
        for t in per_contract_by_market[m].get("trades", []):
            rows.append((t["date"], order[m], t["entry_ts"], m, t))
    rows.sort(key=lambda r: r[:3])
    risk = _fr(risk_pct)
    balance = Fraction(round(float(start) * 100), 100)
    trades, skipped, days, exact = [], [], [], {}
    i = 0
    while i < len(rows):
        d = rows[i][0]
        bal0, total, low_sum, any_trade = balance, Fraction(0), Fraction(0), False
        while i < len(rows) and rows[i][0] == d:
            _d, _o, ets, m, t = rows[i]
            i += 1
            spec = specs_by_market[m]
            pv, comm = _fr(spec["pv"]), _fr(spec["comm"])
            loss1 = (_fq(t["dist"]) + _fq(spec["slip_ticks"] * float(spec["tick"]))) * pv + comm
            qty = min(math.floor(bal0 * risk / 100 / loss1), int(spec["max_qty"]))
            if qty < 1:
                skipped.append({"market": m, "date": d, "entry_ts": ets, "reason": _UNDER})
                continue
            any_trade = True
            planned = qty * loss1
            net = _fq((t["exit"] - t["entry"]) * t["side"]) * pv * qty - comm * qty
            key = (m, d, ets)
            exact[key] = {"planned_cost": planned, "net": net}
            carried = Fraction(round(_cents(net) * 100), 100)
            if theirs_net is not None:
                tn = theirs_net(key)
                if tn is not None and _whole_cents(tn) and _within_half_cent(tn, net):
                    carried = Fraction(round(tn * 100), 100)
            total += carried
            low_sum += _fq(t["worst"]) * pv * qty - comm * qty
            rec = dict(t)
            rec.update(market=m, qty=qty, planned_cost=_cents(planned), net=float(carried),
                       balance_start=float(bal0))
            trades.append(rec)
        if any_trade:
            end = bal0 + total
            low = min(bal0 + low_sum, bal0, end)
            exact[("day", d)] = low
            days.append({"date": d, "start": float(bal0), "end": float(end), "low": _cents(low)})
            balance = end
    return {"start": float(start), "trades": trades, "skipped": skipped, "days": days}, exact


def replay_account(per_contract_by_market, specs_by_market, risk_pct, start):
    """The rule's account output from the per-contract trades (plan, "Money")."""
    return _account(per_contract_by_market, specs_by_market, risk_pct, start)[0]


_A_PRICE_FIELDS = tuple(f for f in _T_FIELDS if f[0] != "market")


def check_account(result, per_contract_by_market, specs_by_market, risk_pct, start):
    """Breaks between the engine's account output and the rule's money, recomputed from the per-contract trades."""
    breaks = []
    if not isinstance(result, dict):
        return ["account: the engine's output is not a dict"]
    theirs = result.get("trades", [])
    by_key = {}
    for t in theirs:
        try:
            by_key.setdefault((t["market"], t["date"], t["entry_ts"]), t)
        except (KeyError, TypeError):
            pass

    def theirs_net(key):
        t = by_key.get(key)
        return t.get("net") if isinstance(t, dict) and isinstance(t.get("net"), (int, float)) else None
    mine, exact = _account(per_contract_by_market, specs_by_market, risk_pct, start, theirs_net)
    if not _px_eq(result.get("start"), float(start), 0.005):
        breaks.append(f"account: start is {_fmt(result.get('start'))}, rule says {_fmt(float(start))}")
    markets = list(per_contract_by_market)
    try:
        keys = [(t["date"], markets.index(t["market"]), t["entry_ts"]) for t in theirs]
        if keys != sorted(keys):
            breaks.append("account: trades are not in (date, market, entry_ts) order")
    except (KeyError, TypeError, ValueError):
        breaks.append("account: a trade has no date, entry_ts or a known market")
    mk = {(t["market"], t["date"], t["entry_ts"]): t for t in mine["trades"]}
    for k in sorted(set(mk) - set(by_key), key=str):
        breaks.append(f"account: trade {k[0]} {k[1]} entered {k[2]}: missing (the rule sizes it at "
                      f"{mk[k]['qty']} contracts)")
    for k in sorted(set(by_key) - set(mk), key=str):
        breaks.append(f"account: trade {k[0]} {k[1]} entered {k[2]}: extra (the rule makes no such trade)")
    for k in sorted(set(mk) & set(by_key), key=str):
        m, t = mk[k], by_key[k]
        label = f"account: trade {k[0]} {k[1]} entered {k[2]}"
        tol = float(specs_by_market[k[0]]["tick"]) * _EPS
        extra = tuple((f, "eq") for f in ("break_ts", "setup_ts") if f in m)     # candidates 2, 3 and 4
        extra += (("trigger", "px"),) if "trigger" in m else ()                 # candidate 4 (R52)
        _field_breaks(breaks, label, m, t, _A_PRICE_FIELDS + extra + (("qty", "eq"),), tol)
        for f in ("planned_cost", "net"):
            if f not in t:
                breaks.append(f"{label}: field {f} missing")
            elif not _within_half_cent(t[f], exact[k][f]) or (f == "net" and not _whole_cents(t[f])):
                breaks.append(f"{label}: {f} is {_fmt(t[f])}, rule says {_fmt(m[f])}")
        if "balance_start" not in t:
            breaks.append(f"{label}: field balance_start missing")
        elif not _px_eq(t["balance_start"], m["balance_start"], 0.005):
            breaks.append(f"{label}: balance_start is {_fmt(t['balance_start'])}, rule says "
                          f"{_fmt(m['balance_start'])}")

    def sk(s):
        return (s.get("market"), s.get("date"), s.get("entry_ts"), s.get("reason"))
    ms = Counter(sk(s) for s in mine["skipped"])
    ts_ = Counter(sk(s) for s in result.get("skipped", []) if isinstance(s, dict))
    for s in sorted((ms - ts_).elements(), key=str):
        breaks.append(f"account: skipped {s}: missing (the rule skips this trade)")
    for s in sorted((ts_ - ms).elements(), key=str):
        breaks.append(f"account: skipped {s}: extra (the rule does not skip this)")
    md = {r["date"]: r for r in mine["days"]}
    td = {}
    for r in result.get("days", []):
        try:
            if r["date"] in td:
                breaks.append(f"account: day record {r['date']} listed twice")
            td[r["date"]] = r
        except (KeyError, TypeError):
            breaks.append(f"account: unreadable day record {r!r}")
    if [r.get("date") for r in result.get("days", []) if isinstance(r, dict)] != sorted(td):
        breaks.append("account: day records are not in ascending date order")
    for d in sorted(set(md) - set(td)):
        breaks.append(f"account: day record {d}: missing")
    for d in sorted(set(td) - set(md)):
        breaks.append(f"account: day record {d}: extra (no trade that date)")
    for d in sorted(set(md) & set(td)):
        m, t = md[d], td[d]
        for f in ("start", "end"):
            if not _px_eq(t.get(f), m[f], 0.005):
                breaks.append(f"account: day record {d}: {f} is {_fmt(t.get(f))}, rule says {_fmt(m[f])}")
        if not _within_half_cent(t.get("low"), exact[("day", d)]):
            breaks.append(f"account: day record {d}: low is {_fmt(t.get('low'))}, rule says {_fmt(m['low'])}")
    return breaks
