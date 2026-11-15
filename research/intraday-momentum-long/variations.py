#!/usr/bin/env python3
"""Variations of candidate 1 (long-only intraday momentum), each a separate candidate.

Handoff pasted by Amear 2026-11-15: "Propose and test variations of candidate 1, each fixed before the
run, and report the results side by side in plain English." Pass bars, set by Amear:
  profit   : total backtest profit >= 2 x the firm's maximum drawdown ($2,000 stand-in -> $4,000)
  survival : the trailing limit crossed in at most 5% of 10,000 shuffled orders
Judged separately. Also reported: return as a percentage a year, and skipped signals.

The weakness found in candidate 1 is the stop distance: the lower band is far below the entry, so most
signals cost more than 1% at one micro contract and are skipped. The variations, ALL FIXED HERE BEFORE
ANY OF THEM WAS RUN (everything not listed is candidate 1's locked setting, see run.py):

  C1  candidate 1 itself, rerun through this code (must reproduce run.py exactly; a test checks it)
  V1  tighter stop: the stop sits at the day's reference level, the higher of today's open and the
      prior close (the top of the "noise area" the breakout left). Long only, 1%.
  V2  V1's stop, long AND short. Short entry: a :00/:30 bar closes below the lower band while flat;
      its stop sits at the lower reference level (the lower of today's open and the prior close);
      short exit at a decision bar: close >= min(lower band, VWAP). One position at a time; no reversal.
  V3  V1's stop, no band/VWAP exit: the trade is held to the 15:59 flat unless the stop fires.
  V4  V1 at half the risk: 0.5% of the balance per trade.

Honest limit: 2025-2026 was already looked at once, for candidate 1. These variations were chosen
knowing that result (the stop distance), so the unseen years are less unseen than they were.

Standard library only. Run: python3 -I -B research/intraday-momentum-long/variations.py
"""
import hashlib
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run as R   # noqa: E402

mk, bd = R.mk, R.bd

VARIANTS = {
    "C1": {"stop": "lower_band", "sides": "long", "exit": "trail", "risk": 1.0,
           "say": "candidate 1 (stop at the lower band)"},
    "V1": {"stop": "reference", "sides": "long", "exit": "trail", "risk": 1.0,
           "say": "tighter stop at the day's starting level"},
    "V2": {"stop": "reference", "sides": "both", "exit": "trail", "risk": 1.0,
           "say": "tighter stop, long and short"},
    "V3": {"stop": "reference", "sides": "long", "exit": "close", "risk": 1.0,
           "say": "tighter stop, held to the close"},
    "V4": {"stop": "reference", "sides": "long", "exit": "trail", "risk": 0.5,
           "say": "tighter stop, half the risk (0.5%)"},
}
DATA_YEARS = None   # set from the data in main()


def _clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def entry_fill(bar, side):
    return _clamp(bar.o + R.SLIP, bar.l, bar.h) if side == 1 else _clamp(bar.o - R.SLIP, bar.l, bar.h)


def exit_fill(bar, side):
    return entry_fill(bar, -side)


def stop_fill(bar, side, stop):
    if side == 1:
        return _clamp(min(stop, bar.o) - R.SLIP, bar.l, bar.h)
    return _clamp(max(stop, bar.o) + R.SLIP, bar.l, bar.h)


def stop_hit(bar, side, stop):
    return bar.l <= stop if side == 1 else bar.h >= stop


def stop_for(st, side, mode):
    if mode == "lower_band":
        return st.lower if side == 1 else st.upper
    return st.ref_upper if side == 1 else st.ref_lower


class Sim(object):
    def __init__(self, v, start=R.START, period=None):
        self.v, self.balance, self.start, self.period = dict(v), start, start, period
        self.trades, self.days, self.skipped = [], [], 0
        self.pos = None

    def _open(self, bar, side, stop):
        px = entry_fill(bar, side)
        dist = (px - stop) * side
        budget = self.v["risk"] / 100.0 * self.balance
        if dist <= 0:
            self.skipped += 1
            return
        qty = int(budget / (dist * R.PV) + 1e-9)
        if qty < 1:
            self.skipped += 1
            return
        self.pos = {"side": side, "entry_dt": bar.dt, "entry": px, "stop": stop, "qty": qty,
                    "budget": budget, "worst": px}

    def _close(self, bar, px, reason):
        p = self.pos
        net = (px - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]
        self.balance += net
        self.trades.append({"side": "Long" if p["side"] == 1 else "Short",
                            "entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
                            "entry": p["entry"], "exit": px, "stop": p["stop"], "qty": p["qty"],
                            "budget": round(p["budget"], 2), "reason": reason, "net": round(net, 2),
                            "balance": round(self.balance, 2)})
        self.pos = None

    def _mark(self, price):
        p = self.pos
        return self.balance + (price - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]

    def run(self, market):
        lo, hi = self.period or (market.start, market.end)
        both, trail = self.v["sides"] == "both", self.v["exit"] == "trail"
        for s in market.sessions:
            if not (lo <= s.date <= hi):
                continue
            day_start = day_low = self.balance
            pend_exit = pend_entry = None
            last = len(s.bars) - 1
            for i, bar, st in bd.iter_session_states(market, s.n, R.LOOKBACK, R.NOISE_MULT):
                if pend_exit and self.pos:
                    self._close(bar, exit_fill(bar, self.pos["side"]), pend_exit)
                if pend_entry is not None:
                    self._open(bar, *pend_entry)
                pend_exit = pend_entry = None
                if self.pos:
                    side = self.pos["side"]
                    if stop_hit(bar, side, self.pos["stop"]):
                        self._close(bar, stop_fill(bar, side, self.pos["stop"]), "stop")
                        day_low = min(day_low, self.balance)
                        continue
                    day_low = min(day_low, self._mark(bar.l if side == 1 else bar.h))
                if i == last:
                    if self.pos:
                        self._close(bar, _clamp(bar.c - R.SLIP * self.pos["side"], bar.l, bar.h), "session close")
                    day_low = min(day_low, self.balance)
                    continue
                if bar.mod >= R.FLAT_MOD:
                    if self.pos:
                        pend_exit = "flat 15:59"
                    continue
                if not mk.is_checkpoint(bar.mod) or not st.have_band:
                    continue
                if self.pos:
                    if trail:
                        if self.pos["side"] == 1:
                            lvl = max(st.upper, st.vwap) if st.vwap_cum_vol > 0 else st.upper
                            if bar.c <= lvl:
                                pend_exit = "band/VWAP exit"
                        else:
                            lvl = min(st.lower, st.vwap) if st.vwap_cum_vol > 0 else st.lower
                            if bar.c >= lvl:
                                pend_exit = "band/VWAP exit"
                elif bar.c > st.upper:
                    pend_entry = (1, stop_for(st, 1, self.v["stop"]))
                elif both and bar.c < st.lower:
                    pend_entry = (-1, stop_for(st, -1, self.v["stop"]))
            if self.pos:
                raise AssertionError("position open after %s" % s.date)
            day_low = min(day_low, self.balance)
            self.days.append({"date": s.date, "start": round(day_start, 2), "end": round(self.balance, 2),
                              "low": round(day_low, 2)})
        return self


def digest(trades, keys=("entry_dt", "exit_dt", "entry", "exit", "stop", "qty", "reason", "net", "balance")):
    return hashlib.sha256(json.dumps([[t[k] for k in keys] for t in trades]).encode()).hexdigest()


def years_between(a, b):
    import datetime as dt
    return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days / 365.25


def per_year(start, end, years):
    if end <= 0:
        return -100.0
    return 100.0 * (math.pow(end / start, 1.0 / years) - 1.0)


def money(x):
    return ("-$" if x < 0 else "$") + "{:,.0f}".format(abs(x))


def main():
    market = mk.load_market(R.DATA, session_start=R.SESSION_START)
    out = os.path.join(HERE, "out", "variations")
    os.makedirs(out, exist_ok=True)
    yrs = {"full": years_between(market.start, market.end), "seen": years_between(*R.SEEN),
           "unseen": years_between(*R.UNSEEN)}
    rows = []
    for name, v in VARIANTS.items():
        row = {"name": name, "say": v["say"]}
        # seen years first, unseen after, then the full run that the two branches judge
        for label, period in (("seen", R.SEEN), ("unseen", R.UNSEEN), ("full", None)):
            sim = Sim(v, period=period).run(market)
            st = R.stats(sim)
            row[label] = {"trades": st["trades"], "skipped": sim.skipped, "net": st["net"],
                          "pf": st["profit_factor"], "per_year": round(per_year(R.START, sim.balance, yrs[label]), 1),
                          "worst_closed_drop": st["max_closed_drawdown"], "largest_loss": st["largest_loss"],
                          "losing_run": st["longest_losing_run"], "by_year": st["by_year"],
                          "shorts": sum(1 for t in sim.trades if t["side"] == "Short")}
            if label == "full":
                row["A_pass"] = st["net"] >= 2 * R.LIMIT
                row["trailing"] = R.trailing(sim.days)
                row["shuffle"] = R.shuffled(sim.days)
                row["B_pass"] = row["shuffle"]["pct"] <= 5.0
                row["sha"] = digest(sim.trades)[:12]
                with open(os.path.join(out, name + ".json"), "w") as fh:
                    json.dump({"variant": v, "row": row, "trades": sim.trades, "days": sim.days}, fh, indent=1)
        rows.append(row)
        f, s_, u = row["full"], row["seen"], row["unseen"]
        print("%s  %s" % (name, v["say"]))
        print("    PROFIT   %s vs $4,000 -> %s | %.1f%% a year | trades %d (shorts %d), skipped %d | PF %s | worst closed drop %s | largest loss %s | losing run %d"
              % (money(f["net"]), "PASS" if row["A_pass"] else "FAIL", f["per_year"], f["trades"], f["shorts"],
                 f["skipped"], f["pf"], money(f["worst_closed_drop"]), money(f["largest_loss"]), f["losing_run"]))
        print("    SURVIVAL crossed in %.1f%% of %d shuffles vs 5%% -> %s | real order: %s, closest room %s (%s)"
              % (row["shuffle"]["pct"], row["shuffle"]["runs"], "PASS" if row["B_pass"] else "FAIL",
                 row["trailing"]["first_cross"] or "never crossed", money(row["trailing"]["closest_room"]),
                 row["trailing"]["closest_date"]))
        print("    seen 2021-2024: %d trades, %s, %.1f%% a year | unseen 2025-2026: %d trades, %s, %.1f%% a year | by year %s | sha %s"
              % (s_["trades"], money(s_["net"]), s_["per_year"], u["trades"], money(u["net"]), u["per_year"],
                 f["by_year"], row["sha"]))
    with open(os.path.join(out, "summary.json"), "w") as fh:
        json.dump(rows, fh, indent=1)


if __name__ == "__main__":
    main()
