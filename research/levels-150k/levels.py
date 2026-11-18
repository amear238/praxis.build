#!/usr/bin/env python3
"""levels.py -- the clock, the traded contract, the roll shift and the seven kinds of level of candidate 1
(research/levels-150k/PLAN.md, "Candidate 1: fade the first touch of a marked level. The exact rule").
Draws; trades nothing (fade.py trades).

Market(minutes, daily, rolls, spec, market) prepares one market:
  minutes: [mdata.Bar], the actual front-month 1-minute bars, sorted, ts = the minute's START (UTC ns).
  daily: [mdata.Adj], back-adjusted daily bars (a bar's date = its UTC date). rolls: [mdata.Roll].
  .days: one Day per trading date, in order. Day: date (ISO), ordinal, iid (the traded contract), p0, atr
  (None before 14 daily bars), f (index of the first minute at or after 9:30), end (one past the session's
  last minute), levels {kind: [Level]} for PD, ON, PW, SW, RN, VP, SD (a kind absent or empty: not drawn).
  Level(kind, price, role, far): role "high"/"low" (PD, ON, PW), "swing_high"/"swing_low", "round",
  "vah"/"poc"/"val", or "demand"/"supply" (zones, whose price is the near edge and far the far edge).

Clock (New York wall clock, from zoneinfo). Session date = the calendar date of the wall-clock stamp plus 7
hours. Trading date = a session date with a minute stamped 9:30 to before 15:55.

Shift. For day D the traded contract Y is the contract of D's first minute at or after 9:30. Walking the daily
rolls stamped at or before that minute from the newest back, starting at Y: a roll into the current contract
adds its gap and moves to its old contract; the first time a contract is reached, its shift is the gaps added
so far. A roll with gap None ends the walk. A minute of a contract with no shift is unjoinable; a level that
needs it is not drawn that day. Shifted prices are rounded to the tick.

Hourly bars: each holds the minutes stamped in one wall-clock hour (a repeated hour at the change to winter
time is one bar). A bar holding two contracts is a data error (ValueError); the bought data changes contract
only on the hour.

Standard library only. Run tests with python3 -I -B.
"""
import bisect
import datetime as dt
from collections import namedtuple
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
NS = 1_000_000_000
EPOCH_ORD = dt.date(1970, 1, 1).toordinal()
OPEN_MIN, LAST_ENTRY_MIN, FLAT_MIN = 9 * 60 + 30, 15 * 60, 15 * 60 + 55
SW_DATES, SW_N = 5, 3
SD_DATES, SD_BASE_MAX, SD_SMALL, SD_BIG = 10, 3, 0.5, 2.0
VA_SHARE = 0.70
KINDS = ("PD", "ON", "PW", "SW", "RN", "VP", "SD")
ROUND_STEP = {"NQ": 100.0, "ES": 50.0, "RTY": 25.0, "CL": 1.0, "GC": 25.0, "ZN": 0.5, "ZB": 1.0,
              "6E": 0.005, "6B": 0.005, "6A": 0.005}
YEN_STEP = 0.5
ATR_DAYS = 14

Level = namedtuple("Level", "kind price role far")


def _offset_cache():
    cache = {}

    def off(sec):
        h = sec // 3600
        o = cache.get(h)
        if o is None:
            o = int(dt.datetime.fromtimestamp(h * 3600, ET).utcoffset().total_seconds())
            cache[h] = o
        return o
    return off


_OFF = _offset_cache()


def _wall(ts):
    sec = ts // NS
    return sec + _OFF(sec)


def session_date(ts):
    return dt.date.fromordinal((_wall(ts) + 7 * 3600) // 86400 + EPOCH_ORD).isoformat()


def rnd(x, tick):
    return round(x / tick) * tick


class Day(object):
    __slots__ = ("date", "ordinal", "iid", "p0", "atr", "f", "end", "levels", "shift")

    def __repr__(self):
        return "Day(%s iid=%s p0=%s atr=%s)" % (self.date, self.iid, self.p0, self.atr)


class Market(object):
    def __init__(self, minutes, daily, rolls, spec, market):
        self.minutes, self.spec, self.market = minutes, spec, market
        self.tick = spec["tick"]
        self.eps = self.tick * 1e-6
        n = len(minutes)
        cal, mod, sess = [0] * n, [0] * n, [0] * n
        for i, b in enumerate(minutes):
            w = _wall(b.ts)
            cal[i] = w // 86400 + EPOCH_ORD
            mod[i] = (w % 86400) // 60
            sess[i] = (w + 7 * 3600) // 86400 + EPOCH_ORD
        self.cal, self.mod, self.sess = cal, mod, sess
        # sessions: ordinal -> [i0, i1)
        self.sessions = {}
        for i, s in enumerate(sess):
            if s in self.sessions:
                self.sessions[s][1] = i + 1
            else:
                self.sessions[s] = [i, i + 1]
        self._hourly()
        self.daily_ord = [a.bar.ts // NS // 86400 + EPOCH_ORD for a in daily]
        self.daily = daily
        self.rolls = sorted(rolls, key=lambda r: r.ts)
        self.roll_ts = [r.ts for r in self.rolls]
        trading = []
        for s, (i0, i1) in self.sessions.items():
            f = next((i for i in range(i0, i1) if cal[i] == s and OPEN_MIN <= mod[i]), None)
            if f is not None and mod[f] < FLAT_MIN:
                trading.append((s, f, i1))
        self.trading = [t[0] for t in trading]
        self._tindex = {s: k for k, s in enumerate(self.trading)}
        self.days = [self._day(k, s, f, i1) for k, (s, f, i1) in enumerate(trading)]

    # ------------------------------------------------------------------------------------------ hourly bars
    def _hourly(self):
        m = self.minutes
        bars = []          # [key, i0, i1, iid, high, low, close, sess]
        for i, b in enumerate(m):
            key = (self.cal[i], self.mod[i] // 60)
            if bars and bars[-1][0] == key:
                hb = bars[-1]
                if hb[3] != b.iid:
                    raise ValueError("%s: hourly bar %s holds two contracts" % (self.market, key))
                hb[2] = i + 1
                hb[4] = max(hb[4], b.high)
                hb[5] = min(hb[5], b.low)
                hb[6] = b.close
            else:
                bars.append([key, i, i + 1, b.iid, b.high, b.low, b.close, self.sess[i]])
        self.hbars = bars
        self.hbar_i0 = [hb[1] for hb in bars]
        self.hb_by_sess = {}
        for j, hb in enumerate(bars):
            s = hb[7]
            if s in self.hb_by_sess:
                self.hb_by_sess[s][1] = j + 1
            else:
                self.hb_by_sess[s] = [j, j + 1]

    # ------------------------------------------------------------------------------------------ shift
    def _shift_map(self, iid, at_ts):
        out, cur, acc = {iid: 0.0}, iid, 0.0
        k = bisect.bisect_right(self.roll_ts, at_ts)
        for r in reversed(self.rolls[:k]):
            if r.new_iid != cur:
                continue
            if r.gap is None:
                break
            acc += r.gap
            cur = r.old_iid
            if cur not in out:
                out[cur] = acc
        return out

    def _hl(self, i0, i1, shift):
        """Shifted (high, low) of minutes [i0, i1); None when empty or a minute is unjoinable."""
        hi = lo = None
        m = self.minutes
        for i in range(i0, i1):
            s = shift.get(m[i].iid)
            if s is None:
                return None
            h, l = m[i].high + s, m[i].low + s
            hi = h if hi is None or h > hi else hi
            lo = l if lo is None or l < lo else lo
        if hi is None:
            return None
        return rnd(hi, self.tick), rnd(lo, self.tick)

    # ------------------------------------------------------------------------------------------ one day
    def _day(self, k, s, f, end):
        d = Day()
        m = self.minutes
        d.date, d.ordinal, d.f, d.end = dt.date.fromordinal(s).isoformat(), s, f, end
        d.iid, d.p0 = m[f].iid, m[f].open
        j = bisect.bisect_left(self.daily_ord, s)
        d.atr = (sum(a.adj_high - a.adj_low for a in self.daily[j - ATR_DAYS:j]) / ATR_DAYS
                 if j >= ATR_DAYS else None)
        shift = self._shift_map(d.iid, m[f].ts)
        d.shift = shift
        lv = {}
        prev = self.trading[k - 1] if k >= 1 else None
        i0 = self.sessions[s][0]
        if prev is not None:
            p0, p1 = self.sessions[prev]
            hl = self._hl(p0, p1, shift)
            if hl:
                lv["PD"] = [Level("PD", hl[0], "high", None), Level("PD", hl[1], "low", None)]
            vp = self._vp(p0, p1, shift)
            if vp:
                lv["VP"] = vp
        hl = self._hl(i0, f, shift)
        if hl:
            lv["ON"] = [Level("ON", hl[0], "high", None), Level("ON", hl[1], "low", None)]
        pw = self._pw(s, shift)
        if pw:
            lv["PW"] = pw
        if d.atr is not None:
            lv["RN"] = self._rn(d.p0, d.atr)
        lv["SW"] = self._sw(k, s, f, shift)
        lv["SD"] = self._sd(k, s, f, shift)
        d.levels = {kk: v for kk, v in lv.items() if v is not None}
        return d

    def _pw(self, s, shift):
        y, w, _ = dt.date.fromordinal(s - 7).isocalendar()
        dates = [t for t in self.trading if t < s and dt.date.fromordinal(t).isocalendar()[:2] == (y, w)]
        if not dates:
            return None
        hi = lo = None
        for t in dates:
            hl = self._hl(*self.sessions[t], shift)
            if hl is None:
                return None
            hi = hl[0] if hi is None else max(hi, hl[0])
            lo = hl[1] if lo is None else min(lo, hl[1])
        return [Level("PW", hi, "high", None), Level("PW", lo, "low", None)]

    def _rn(self, p0, atr):
        tick, lo, hi = self.tick, p0 - 2 * atr, p0 + 2 * atr
        out = []
        if self.market == "6J":
            if lo <= 0:
                return out
            n0, n1 = int(1.0 / (YEN_STEP * hi)) - 1, int(1.0 / (YEN_STEP * lo)) + 2
            for n in range(max(n0, 1), n1 + 1):
                p = rnd(1.0 / (YEN_STEP * n), tick)
                if lo - tick <= p <= hi + tick:
                    out.append(Level("RN", p, "round", None))
            return sorted(out, key=lambda x: x.price)
        step = ROUND_STEP[self.market]
        n0, n1 = int(lo // step) - 1, int(hi // step) + 2
        for n in range(n0, n1 + 1):
            p = rnd(n * step, tick)
            if lo - step <= p <= hi + step:
                out.append(Level("RN", p, "round", None))
        return out

    def _vp(self, i0, i1, shift):
        tick, m = self.tick, self.minutes
        rows = []
        for i in range(i0, i1):
            s = shift.get(m[i].iid)
            if s is None:
                return None
            rows.append((round((m[i].low + s) / tick), round((m[i].high + s) / tick), m[i].volume))
        if not rows:
            return None
        base = min(r[0] for r in rows)
        top = max(r[1] for r in rows)
        diff = [0.0] * (top - base + 2)
        for lo, hi, v in rows:
            share = v / (hi - lo + 1)
            diff[lo - base] += share
            diff[hi - base + 1] -= share
        vol, run = [], 0.0
        for x in diff[:-1]:
            run += x
            vol.append(run)
        total = sum(v for _, _, v in rows)
        if total <= 0:
            return None
        mid = (base + top) / 2.0
        best = max(vol)
        cands = [k for k, v in enumerate(vol) if v == best]
        poc = min(cands, key=lambda k: (abs(k + base - mid), k))
        a = b = poc
        area = vol[poc]
        while area < VA_SHARE * total - 1e-9 * total:
            up = vol[b + 1] if b + 1 < len(vol) else None
            dn = vol[a - 1] if a - 1 >= 0 else None
            if up is None and dn is None:
                break
            if dn is None or (up is not None and up > dn):
                b += 1
                area += up
            elif up is None or dn > up:
                a -= 1
                area += dn
            else:
                b += 1
                a -= 1
                area += up + dn
        return [Level("VP", rnd((b + base) * tick, tick), "vah", None),
                Level("VP", rnd((poc + base) * tick, tick), "poc", None),
                Level("VP", rnd((a + base) * tick, tick), "val", None)]

    # ------------------------------------------------------------------------------------------ hourly kinds
    def _window(self, k, s, f, n_dates, shift):
        """-> (pattern bars [(g, high, low, close)], late) or None when a bar is unjoinable. Pattern bars: the
        hourly bars of the n_dates trading dates before s and of S(s) up to the bar ending 9:00. late(g) ->
        (max high, min low) of every minute after global bar g and before 9:30 on s (shifted); (None, None)
        when one of them is unjoinable."""
        i0 = self.sessions[s][0]
        i9 = next(i for i in range(i0, f + 1) if self.cal[i] == s and self.mod[i] >= 9 * 60)
        g9 = bisect.bisect_right(self.hbar_i0, i9) - 1          # the bar holding the first minute from 9:00
        g_idx = []
        for t in self.trading[max(0, k - n_dates):k]:
            if t in self.hb_by_sess:
                g_idx.extend(range(*self.hb_by_sess[t]))
        own = self.hb_by_sess.get(s)
        if own:
            g_idx.extend(range(own[0], min(own[1], g9)))
        if not g_idx:
            return None
        tick = self.tick
        pat = []
        for g in g_idx:
            hb = self.hbars[g]
            sh = shift.get(hb[3])
            if sh is None:
                return None
            pat.append((g, rnd(hb[4] + sh, tick), rnd(hb[5] + sh, tick), rnd(hb[6] + sh, tick)))
        hl_tail = self._hl(i9, f, shift) if i9 < f else None
        if i9 < f and hl_tail is None:
            return None
        g_first = g_idx[0]
        n = g9 - g_first                                         # global bars g_first .. g9 - 1
        suf_h, suf_l, bad = [0.0] * (n + 1), [0.0] * (n + 1), [False] * (n + 1)
        suf_h[n] = hl_tail[0] if hl_tail else float("-inf")
        suf_l[n] = hl_tail[1] if hl_tail else float("inf")
        for x in range(n - 1, -1, -1):
            hb = self.hbars[g_first + x]
            sh = shift.get(hb[3])
            if sh is None:
                bad[x], suf_h[x], suf_l[x] = True, suf_h[x + 1], suf_l[x + 1]
            else:
                bad[x] = bad[x + 1]
                suf_h[x] = max(suf_h[x + 1], rnd(hb[4] + sh, tick))
                suf_l[x] = min(suf_l[x + 1], rnd(hb[5] + sh, tick))

        def late(g):
            x = g - g_first + 1
            return (None, None) if bad[x] else (suf_h[x], suf_l[x])
        return pat, late

    def _sw(self, k, s, f, shift):
        w = self._window(k, s, f, SW_DATES, shift)
        if w is None:
            return None
        pat, late = w
        tick, eps, out = self.tick, self.eps, []
        for j in range(SW_N, len(pat) - SW_N):
            g, h, l, _ = pat[j]
            around = pat[j - SW_N:j] + pat[j + 1:j + 1 + SW_N]
            mh, ml = late(g)
            if all(h > x[1] + eps for x in around) and mh is not None and mh < h + tick - eps:
                out.append(Level("SW", h, "swing_high", None))
            if all(l < x[2] - eps for x in around) and ml is not None and ml > l - tick + eps:
                out.append(Level("SW", l, "swing_low", None))
        return out

    def _sd(self, k, s, f, shift):
        w = self._window(k, s, f, SD_DATES, shift)
        if w is None:
            return None
        pat, late = w
        tick, eps, out = self.tick, self.eps, []
        a60 = sum(x[1] - x[2] for x in pat) / len(pat)
        for i in range(1, len(pat)):
            g, h, l, c = pat[i]
            if h - l < SD_BIG * a60 - eps:
                continue
            for b in range(SD_BASE_MAX, 0, -1):
                if i - b < 0:
                    continue
                base = pat[i - b:i]
                if any(x[1] - x[2] > SD_SMALL * a60 + eps for x in base):
                    continue
                top, bot = max(x[1] for x in base), min(x[2] for x in base)
                if c > top + eps:
                    mh, ml = late(g)
                    if ml is not None and ml > top - tick + eps:
                        out.append(Level("SD", top, "demand", bot))
                    break
                if c < bot - eps:
                    mh, ml = late(g)
                    if mh is not None and mh < bot + tick - eps:
                        out.append(Level("SD", bot, "supply", top))
                    break
        return out
