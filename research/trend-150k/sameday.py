#!/usr/bin/env python3
"""sameday.py -- version A of the trend plan (research/trend-150k/PLAN.md): the recent trend sets the side, one
trade per market per day, entered after the US open and flat before 16:00 ET. Judges nothing.

Two steps, exact because every position is flat by the close (a trade's path does not depend on its size):

per_contract(minute_bars, daily, spec, settings, fill) -> one market's trades at one contract.
  minute_bars: [mdata.Bar] (actual front-month prices; ts = the minute's START, UTC). daily: [mdata.Adj] (the
  back-adjusted daily series; a daily bar's date is its ts's UTC date). Each ET trading date D with minute bars:
  - Signal: j = the last daily bar dated before D. Needs j >= L and j >= N - 1. side = sign(adj close[j] -
    adj close[j - L]); none when equal. ATR = mean(high - low) of daily bars j - N + 1 .. j. dist = stop_mult *
    ATR on the tick grid rounded down, at least one tick.
  - Entry: the first bar of D starting at or after settings["entry"] (ET) and before settings["flat"]; at its
    open, slip against, kept inside the bar. No such bar: no trade. Stop at entry -/+ dist.
  - Each bar from the entry bar, in order: (a) flat: a bar starting at or after settings["flat"] closes the
    trade at its open, slip against, inside the bar, reason "flat", gap when that open is beyond the stop;
    (b) stop: long open <= stop is a gap, else low <= stop; kind = stop (open on a gap) - slip, not below the
    low; midpoint = halfway to the low, tick below; harsh-stops = the low (shorts mirror); reason "stop";
    (c) mark the adverse extreme into `worst`, update best; (d) trail (trail_mult t): stop moves to best -/+
    t * dist on the grid away from price, only toward the price, acting from the next bar.
    Bars run out before flat: close at the last bar's close, slip against, reason "flat".
  Trade: market (filled by the caller), date, side, entry, exit, stop_initial, dist, reason, gap,
  points = (exit - entry) * sign, worst = the lowest (adverse extreme - entry) * sign over bars marked (<= 0).

account(per_contract_by_market, specs, risk_pct, start) -> trades sized on one balance, day records.
  Dates ascending; on each date every market's trade is sized from the realised balance at the day's start
  (all are flat overnight): risk = balance * risk_pct / 100; loss a contract = (dist + slip) * pv + comm;
  qty = floor(risk / that), at most max_qty; qty < 1 skipped ("under one contract").
  net = points * pv * qty - comm * qty, to the cent. Day {date, start, end, low}: low = start + the sum of every
  trade's (worst * pv * qty - comm * qty) (all at once; conservative), never above min(start, end).

Standard library only. Run tests with python3 -I -B.
"""
import bisect
import datetime as dt
import hashlib
import json
import math
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
EPS = 1e-9


def _floor_tick(x, tick):
    return math.floor(x / tick + EPS) * tick


def _ceil_tick(x, tick):
    return math.ceil(x / tick - EPS) * tick


def _inside(x, lo, hi):
    return min(max(x, lo), hi)


def _hhmm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def et_days(bars, lo_min, hi_min):
    """{ET date iso: [(minute of day, bar)]} for bars starting in [lo_min, hi_min] ET, in order."""
    out = {}
    cache_hour, off = None, None
    for b in bars:
        hour = b.ts // 3_600_000_000_000
        if hour != cache_hour:
            cache_hour = hour
            off = dt.datetime.fromtimestamp(hour * 3600, dt.UTC).astimezone(ET).utcoffset().total_seconds()
        local = b.ts / 1e9 + off
        mod = int(local // 60) % 1440
        if lo_min <= mod <= hi_min:
            d = dt.date.fromordinal(dt.date(1970, 1, 1).toordinal() + int(local // 86400)).isoformat()
            out.setdefault(d, []).append((mod, b))
    return out


def per_contract(minute_bars, daily, spec, settings, fill, days=None):
    L, N = settings["lookback"], settings["atr_days"]
    k, t = settings["stop_mult"], settings["trail_mult"]
    e_min, f_min = _hhmm(settings["entry"]), _hhmm(settings["flat"])
    tick, slip = spec["tick"], spec["slip_ticks"] * spec["tick"]
    if days is None:
        days = et_days(minute_bars, e_min, 16 * 60)
    ddates = [dt.datetime.fromtimestamp(a.bar.ts / 1e9, dt.UTC).date().isoformat() for a in daily]
    out = []
    for date in sorted(days):
        j = bisect.bisect_left(ddates, date) - 1
        if j < L or j < N - 1:
            continue
        c, cb = daily[j].adj_close, daily[j - L].adj_close
        if c == cb:
            continue
        side, sign = ("long", 1) if c > cb else ("short", -1)
        atr = sum(a.adj_high - a.adj_low for a in daily[j - N + 1:j + 1]) / N
        dist = max(_floor_tick(k * atr, tick), tick)
        rows = [(mod, b) for mod, b in days[date] if mod >= e_min]
        if not rows or rows[0][0] >= f_min:
            continue
        b0 = rows[0][1]
        entry = _inside(b0.open + slip * sign, b0.low, b0.high)
        stop = entry - dist * sign
        trade = {"date": date, "side": side, "entry": entry, "stop_initial": stop, "dist": dist}
        best, worst, done = None, 0.0, None
        for mod, b in rows:
            if mod >= f_min:
                px = _inside(b.open - slip * sign, b.low, b.high)
                done = (px, "flat", (b.open - stop) * sign <= 0)
                break
            if sign == 1:
                gap = b.open <= stop
                if gap or b.low <= stop:
                    ref = b.open if gap else stop
                    px = {"kind": max(b.low, ref - slip), "midpoint": _floor_tick((ref + b.low) / 2, tick),
                          "harsh-stops": b.low}[fill]
                    done = (px, "stop", gap)
                    break
                worst = min(worst, b.low - entry)
                best = b.high if best is None else max(best, b.high)
                if t is not None:
                    stop = max(stop, _floor_tick(best - t * dist, tick))
            else:
                gap = b.open >= stop
                if gap or b.high >= stop:
                    ref = b.open if gap else stop
                    px = {"kind": min(b.high, ref + slip), "midpoint": _ceil_tick((ref + b.high) / 2, tick),
                          "harsh-stops": b.high}[fill]
                    done = (px, "stop", gap)
                    break
                worst = min(worst, entry - b.high)
                best = b.low if best is None else min(best, b.low)
                if t is not None:
                    stop = min(stop, _ceil_tick(best + t * dist, tick))
        if done is None:
            lb = rows[-1][1]
            done = (_inside(lb.close - slip * sign, lb.low, lb.high), "flat", False)
        px, reason, gap = done
        trade.update(exit=px, reason=reason, gap=gap, points=round((px - entry) * sign, 10),
                     worst=round(min(worst, (px - entry) * sign), 10))
        out.append(trade)
    return out


def account(per_contract_by_market, specs, risk_pct, start=150000.0):
    by_date = {}
    for m, trs in per_contract_by_market.items():
        for x in trs:
            by_date.setdefault(x["date"], []).append(dict(x, market=m))
    markets = list(per_contract_by_market)
    balance, trades, skipped, days = start, [], [], []
    for date in sorted(by_date):
        day_start, low_sum, todays = balance, 0.0, []
        for x in sorted(by_date[date], key=lambda y: markets.index(y["market"])):
            sp = specs[x["market"]]
            lpc = (x["dist"] + sp["slip_ticks"] * sp["tick"]) * sp["pv"] + sp["comm"]
            qty = min(int(math.floor(day_start * risk_pct / 100.0 / lpc + EPS)), sp["max_qty"])
            if qty < 1:
                skipped.append({"market": x["market"], "date": date, "side": x["side"], "reason": "under one contract"})
                continue
            net = round(x["points"] * sp["pv"] * qty - sp["comm"] * qty, 2)
            low_sum += x["worst"] * sp["pv"] * qty - sp["comm"] * qty
            todays.append(dict(x, qty=qty, planned_cost=round(qty * lpc, 2), net=net))
        for x in todays:
            balance = round(balance + x["net"], 2)
            x["balance"] = balance
            trades.append(x)
        if todays:
            days.append({"date": date, "start": day_start, "end": balance,
                         "low": round(min(day_start + low_sum, day_start, balance), 2)})
    digest = hashlib.sha256(json.dumps(trades, sort_keys=True).encode()).hexdigest()
    return {"risk_pct": risk_pct, "start": start, "trades": trades, "days": days, "skipped": skipped,
            "digest": digest}
