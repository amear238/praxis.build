#!/usr/bin/env python3
"""Candidate 3: first half hour into the last half hour (market intraday momentum), NQ 1-minute bars.

Amear's handoff (pasted 2026-11-15): run it as a last cheap test under the same bars, every setting fixed
in code before the run, 2025 to 2026 only after the earlier years; report yearly return, skipped
signals and headroom.

The rule is Gao, Han, Li and Zhou, "Market intraday momentum", Journal of Financial Economics 2018: the
first half-hour return, from the previous day's close to 10:00, predicts the last half hour; trade the
last half hour in its direction. The paper's text is not in the repo (abstract only, see
docs/reports/2026-10-31-7zq-m2-new-strategy.md); the rule is as the paper is widely summarised. The
paper has no stop. Amear's rules need one, so the stop below is this file's addition.

A close cousin already ran on 2026-11-01 in NinjaTrader (Baltussen, Da, Lammers and Martens 2021: the
whole day up to 15:30 as the signal, same last half hour, no stop, one NQ contract): 1,304 trades,
-$76,010, profit factor 0.84 (docs/reports/2026-11-01-three-strategy-results.md). A fail is likely.

LOCKED SETTINGS (fixed before any run; none is tuned):
  data          NQ continuous 1-minute, 2021-03-08 to 2026-07-17, bars 09:31-16:00 ET
  signal        r = close of the 10:00 bar / the previous session's last close - 1.
                r > 0: long. r < 0: short. r == 0: no trade
  trade window  sessions that have a 10:00 bar and a 15:30 bar; others (early closes) no trade
  entry         market order at the open of the first bar after 15:30 (normally 15:31), one trade a day
  stop          stop-market resting from the fill at a distance equal to the average last-half-hour range
                (highest high minus lowest low of the bars stamped 15:31 to 16:00) over the previous 14
                sessions that have both a 15:31 and a 16:00 bar, rounded up to a whole tick. Before 14
                such sessions exist, no trade (counted as warm-up)
  close         flat on the 15:59 bar (filled at the 16:00 bar's open); else the session's last bar
  size          micro contracts (MNQ, $2 a point) = floor(1% of current balance / (stop distance x $2));
                fewer than one -> skipped and counted
  costs         2 ticks (0.5 point) slippage on every fill; $1.90 commission per contract round trip
  account       $50,000 start (stand-in), $2,000 end-of-day trailing limit (stand-in), the same trailing
                rule, 10,000-shuffle count and headroom as candidates 1 and 2
  periods       seen 2021-03-08 to 2024-12-31 first; unseen 2025-01-01 to 2026-07-17 only after

Standard library only. Run: python3 -I -B research/half-hour-momentum/hhm.py
"""
import argparse
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "research", "orb-5min"))
import orb as O   # noqa: E402  fills, shuffled_depth; through it candidate 1's trailing rule and shuffle

R, V, mk = O.R, O.V, O.mk
SIGNAL_MOD, WINDOW_MOD, LAST_FIRST, LAST_END = 10 * 60, 15 * 60 + 30, 15 * 60 + 31, 16 * 60
LOOKBACK = 14
RISK_PCT = 1.0


def last_half_range(session):
    """Range of the bars stamped 15:31-16:00, or None unless both the 15:31 and the 16:00 bar exist."""
    bars = [b for b in session.bars if LAST_FIRST <= b.mod <= LAST_END]
    mods = {b.mod for b in bars}
    if LAST_FIRST not in mods or LAST_END not in mods:
        return None
    return max(b.h for b in bars) - min(b.l for b in bars)


def stop_distance(ranges):
    """Average of the last LOOKBACK ranges, rounded up to a whole tick."""
    avg = sum(ranges[-LOOKBACK:]) / float(LOOKBACK)
    return math.ceil(avg / R.TICK - 1e-9) * R.TICK


def signal(prev_session, session):
    """-> (side, r) from the previous session's last close to the 10:00 bar's close; side 0 = none."""
    ten = [b for b in session.bars if b.mod == SIGNAL_MOD]
    if prev_session is None or not ten or not prev_session.bars:
        return 0, None
    r = ten[0].c / prev_session.bars[-1].c - 1.0
    return (1 if r > 0 else -1 if r < 0 else 0), r


def entry_index(session):
    """Index of the first bar after 15:30 if the session has a 15:30 bar, else None."""
    if not any(b.mod == WINDOW_MOD for b in session.bars):
        return None
    for i, b in enumerate(session.bars):
        if b.mod > WINDOW_MOD:
            return i
    return None


class Sim(object):
    def __init__(self, risk_pct=RISK_PCT, start=R.START, period=None):
        self.risk_pct, self.balance, self.start, self.period = risk_pct, start, start, period
        self.trades, self.days = [], []
        self.skipped = self.no_signal = self.warmup = self.no_window = 0
        self.pos = None

    def _open(self, bar, side, dist):
        px = O.entry_fill(bar, side)
        stop = px - side * dist
        budget = self.risk_pct / 100.0 * self.balance
        qty = int(budget / (dist * R.PV) + 1e-9)
        if qty < 1:
            self.skipped += 1
            return
        self.pos = {"entry_dt": bar.dt, "side": side, "entry": px, "stop": stop, "dist": dist, "qty": qty,
                    "planned": qty * dist * R.PV, "budget": budget, "worst": px}

    def _close(self, bar, px, reason):
        p = self.pos
        net = (px - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]
        self.balance += net
        self.trades.append({"entry_dt": p["entry_dt"].isoformat(" "), "exit_dt": bar.dt.isoformat(" "),
                            "side": p["side"], "entry": p["entry"], "exit": px, "stop": p["stop"],
                            "dist": p["dist"], "qty": p["qty"], "planned_loss": round(p["planned"], 2),
                            "budget": round(p["budget"], 2), "reason": reason, "net": round(net, 2),
                            "balance": round(self.balance, 2), "worst_price": p["worst"]})
        self.pos = None

    def _mark(self, price):
        p = self.pos
        return self.balance + (price - p["entry"]) * p["side"] * p["qty"] * R.PV - R.COMM * p["qty"]

    def run(self, market):
        lo, hi = self.period or (market.start, market.end)
        ranges, prev = [], None
        for s in market.sessions:
            in_period = lo <= s.date <= hi
            if in_period:
                day_start = day_low = self.balance
                side, _ = signal(prev, s)
                k = entry_index(s)
                if k is None:
                    self.no_window += 1
                elif side == 0:
                    self.no_signal += 1
                elif len(ranges) < LOOKBACK:
                    self.warmup += 1
                else:
                    dist = stop_distance(ranges)
                    last = len(s.bars) - 1
                    pend_exit = None
                    for i in range(k, len(s.bars)):
                        bar = s.bars[i]
                        if pend_exit and self.pos:
                            self._close(bar, O.exit_fill(bar, self.pos["side"]), pend_exit)
                            day_low = min(day_low, self.balance)
                            break
                        if i == k:
                            self._open(bar, side, dist)
                        if not self.pos:
                            break
                        p = self.pos
                        if O.stop_hit(bar, p["side"], p["stop"]):
                            fill = O.stop_fill(bar, p["side"], p["stop"])
                            p["worst"] = min(p["worst"], fill) if p["side"] == 1 else max(p["worst"], fill)
                            self._close(bar, fill, "stop")
                            day_low = min(day_low, self.balance)
                            break
                        adv = bar.l if p["side"] == 1 else bar.h
                        p["worst"] = min(p["worst"], adv) if p["side"] == 1 else max(p["worst"], adv)
                        day_low = min(day_low, self._mark(adv))
                        if i == last:
                            self._close(bar, O._clamp(bar.c - p["side"] * R.SLIP, bar.l, bar.h), "session close")
                            day_low = min(day_low, self.balance)
                            break
                        if bar.mod >= R.FLAT_MOD:
                            pend_exit = "flat 15:59"
                if self.pos:
                    raise AssertionError("position open after %s" % s.date)
                day_low = min(day_low, self.balance)
                self.days.append({"date": s.date, "start": round(day_start, 2), "end": round(self.balance, 2),
                                  "low": round(day_low, 2)})
            # the stop's lookback uses every earlier session, inside the period or not (no result is used)
            rg = last_half_range(s)
            if rg is not None:
                ranges.append(rg)
            prev = s
        return self


def summarise(sim, years):
    st = R.stats(sim)
    st["shorts"] = sum(1 for t in sim.trades if t["side"] == -1)
    st["no_signal_days"], st["warmup_days"], st["no_window_days"] = sim.no_signal, sim.warmup, sim.no_window
    st["per_year_pct"] = round(V.per_year(sim.start, sim.balance, years), 1)
    st["avg_stop_points"] = round(sum(t["dist"] for t in sim.trades) / len(sim.trades), 2) if sim.trades else None
    return st


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=R.DATA)
    ap.add_argument("--out", default=os.path.join(HERE, "out"))
    ap.add_argument("--seen-only", action="store_true", help="run 2021-2024 only")
    a = ap.parse_args(argv)
    market = mk.load_market(a.data, session_start=R.SESSION_START)
    os.makedirs(a.out, exist_ok=True)
    yrs = {"seen": V.years_between(*R.SEEN), "unseen": V.years_between(*R.UNSEEN),
           "full": V.years_between(market.start, market.end)}
    plan = (("seen", R.SEEN),) if a.seen_only else (("seen", R.SEEN), ("unseen", R.UNSEEN), ("full", None))
    results = {}
    for label, period in plan:
        sim = Sim(period=period).run(market)
        st = summarise(sim, yrs[label])
        results[label] = (sim, st)
        print("%-6s trades %4d (shorts %d) | win %4.1f%% | net %9s | %.1f%% a year | PF %s | worst closed drop %s | "
              "largest loss %s | losing run %d | stops %d | skipped %d | no-signal %d | warm-up %d | "
              "early-close %d | avg stop %s pts | avg MNQ %.2f | sha %s"
              % (label, st["trades"], st["shorts"], st["win_pct"], R.money(st["net"]), st["per_year_pct"],
                 st["profit_factor"], R.money(st["max_closed_drawdown"]), R.money(st["largest_loss"]),
                 st["longest_losing_run"], st["stop_exits"], st["skipped"], st["no_signal_days"],
                 st["warmup_days"], st["no_window_days"], st["avg_stop_points"], st["avg_contracts"],
                 R.digest(sim)[:12]))
        print("       by year: %s" % st["by_year"])
        if not a.seen_only:
            with open(os.path.join(a.out, label + ".json"), "w") as fh:
                json.dump({"stats": st, "trades": sim.trades, "days": sim.days}, fh, indent=1)
    if a.seen_only:
        return
    full_sim, full = results["full"]
    tr = R.trailing(full_sim.days)
    sh = R.shuffled(full_sim.days)
    depth = O.shuffled_depth(full_sim.days)
    headroom = round(full["net"] / depth, 2) if depth > 0 else None
    a_pass, b_pass = full["net"] >= 2 * R.LIMIT, sh["pct"] <= 5.0
    print()
    print("PROFIT   total %s against a bar of %s -> %s | %.1f%% a year | skipped %d"
          % (R.money(full["net"]), R.money(2 * R.LIMIT), "PASS" if a_pass else "FAIL", full["per_year_pct"],
             full["skipped"]))
    print("SURVIVAL real order: crossed %s, closest room %s on %s | shuffled: crossed in %d of %d (%.1f%%) vs 5%% -> %s"
          % (tr["first_cross"] or "never", R.money(tr["closest_room"]), tr["closest_date"], sh["crossed"],
             sh["runs"], sh["pct"], "PASS" if b_pass else "FAIL"))
    print("HEADROOM profit %s / worst-5%%-of-shuffles drop %s = %s (both bars together need 2 or more)"
          % (R.money(full["net"]), R.money(depth), headroom))
    with open(os.path.join(a.out, "branches.json"), "w") as fh:
        json.dump({"A": {"net": full["net"], "bar": 2 * R.LIMIT, "pass": a_pass,
                         "per_year_pct": full["per_year_pct"], "skipped": full["skipped"]},
                   "B": {"trailing": tr, "shuffled": sh, "pass": b_pass},
                   "headroom": {"worst_5pct_drop": depth, "ratio": headroom}}, fh, indent=1)


if __name__ == "__main__":
    main()
