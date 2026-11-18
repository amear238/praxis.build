#!/usr/bin/env python3
"""Tests for fade.py: arming, the limit entry, the stop, the target, the flat, spent levels and the account
(research/levels-150k/PLAN.md, candidate 1's exact rule). Run: python3 -I -B research/levels-150k/test_fade.py"""
import os
import sys
import unittest

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(1, os.path.join(os.path.dirname(_HERE), "trend-150k"))
import fade  # noqa: E402
import levels  # noqa: E402
from test_levels import SPEC, TUE, bar, daily_before, ts  # noqa: E402

S = {"name": "t", "kind": "PD", "k": 0.2, "target": 3, "atr_days": 14}


def fake_day(p0, atr, lv):
    d = levels.Day()
    d.date, d.p0, d.atr, d.levels = "2024-01-09", p0, atr, lv
    return d


def L(kind, price, role="high", far=None):
    return levels.Level(kind, price, role, far)


class Arming(unittest.TestCase):
    def test_sides_and_stops(self):
        d = fake_day(110.0, 20.0, {"PD": [L("PD", 130.0), L("PD", 90.0, "low")]})
        got = sorted((a["side"], a["level"], a["stop"]) for a in fade.arm(d, "PD", 0.2, 0.25))
        self.assertEqual(got, [(-1, 130.0, 134.0), (1, 90.0, 86.0)])

    def test_within_d_or_beyond_two_atr_is_not_armed(self):
        d = fake_day(110.0, 20.0, {"RN": [L("RN", 113.0, "round"), L("RN", 114.25, "round"),
                                          L("RN", 150.25, "round"), L("RN", 150.0, "round")]})
        got = sorted(a["level"] for a in fade.arm(d, "RN", 0.2, 0.25))      # d = 4
        self.assertEqual(got, [114.25, 150.0])

    def test_nearest_first_merge_across_kinds(self):
        d = fake_day(110.0, 20.0, {"PD": [L("PD", 90.0, "low")], "ON": [L("ON", 92.0, "low")],
                                   "PW": [L("PW", 86.0, "low")]})
        got = [(a["kind"], a["level"]) for a in fade.arm(d, "ALL", 0.2, 0.25)]
        self.assertEqual(got, [("ON", 92.0), ("PW", 86.0)])             # 90 is within 4 of 92 -> dropped

    def test_zones_only_on_their_own_side_with_the_stop_beyond_the_far_edge(self):
        d = fake_day(110.0, 20.0, {"SD": [L("SD", 100.0, "demand", 97.0), L("SD", 120.0, "demand", 118.0),
                                          L("SD", 125.0, "supply", 127.5)]})
        got = sorted((a["side"], a["level"], a["stop"], a["dist"]) for a in fade.arm(d, "SD", 0.2, 0.25))
        self.assertEqual(got, [(-1, 125.0, 131.5, 6.5), (1, 100.0, 93.0, 7.0)])

    def test_nothing_without_atr(self):
        self.assertEqual(fade.arm(fake_day(110.0, None, {"PD": [L("PD", 90.0, "low")]}), "PD", 0.2, 0.25), [])

    def test_d_rounds_down_to_the_tick_and_is_at_least_one(self):
        d = fake_day(110.0, 20.1, {"PD": [L("PD", 90.0, "low")]})
        self.assertEqual(fade.arm(d, "PD", 0.2, 0.25)[0]["stop"], 86.0)     # 4.02 -> 4.00
        d = fake_day(110.0, 0.5, {"PD": [L("PD", 109.5, "low")]})
        self.assertEqual(fade.arm(d, "PD", 0.1, 0.25)[0]["stop"], 109.25)   # 0.05 -> one tick


def market(rth, on=((18, 0, 110, 112, 108, 110),)):
    """Monday's session gives PD high 130, low 90 (and nothing else near P0); Tuesday's overnight `on`;
    Tuesday's day minutes `rth` as (hh, mm, o, h, l, c). ATR 20, so k 0.2 -> d 4."""
    mins = [bar(ts(2024, 1, 8, 10, 0), 110, 130, 109, 110), bar(ts(2024, 1, 8, 14, 0), 110, 111, 90, 110)]
    for hh, mm, o, h, l, c in on:
        mins.append(bar(ts(2024, 1, 8, hh, mm), o, h, l, c))
    for hh, mm, o, h, l, c in rth:
        mins.append(bar(ts(2024, 1, 9, hh, mm), o, h, l, c))
    mins.sort(key=lambda b: b.ts)
    return levels.Market(mins, daily_before(TUE, rng=20.0), [], SPEC, "NQ")


def trades(rth, s=S, fill="midpoint"):
    return fade.per_contract(market(rth), s, fill, dates={"2024-01-09"})["trades"]


OPEN = (9, 30, 110, 110, 110, 110)


class Entry(unittest.TestCase):
    def test_a_touch_is_not_a_fill(self):
        self.assertEqual(trades([OPEN, (10, 0, 95, 95, 90, 92)]), [])

    def test_one_tick_through_fills_at_the_level(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (15, 55, 93, 93, 93, 93)])
        self.assertEqual([(x["side"], x["entry"], x["stop"], x["target"], x["kind"]) for x in t],
                         [(1, 90.0, 86.0, 102.0, "PD")])

    def test_no_entry_from_1500(self):
        self.assertEqual(trades([OPEN, (15, 0, 95, 95, 89.0, 92), (15, 55, 93, 93, 93, 93)]), [])
        self.assertEqual(len(trades([OPEN, (14, 59, 95, 95, 89.0, 92), (15, 55, 93, 93, 93, 93)])), 1)

    def test_short_at_resistance(self):
        t = trades([OPEN, (10, 0, 128, 130.25, 128, 129), (15, 55, 125, 125, 125, 125)])
        self.assertEqual([(x["side"], x["entry"], x["stop"], x["target"]) for x in t], [(-1, 130.0, 134.0, 118.0)])


class Exits(unittest.TestCase):
    def test_flat_at_355_at_the_open_less_slippage_inside_the_range(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (15, 55, 93, 93.5, 92.75, 93)])[0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("flat", 92.75, False))     # 93 - 0.5 -> low 92.75

    def test_midpoint_stop(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (11, 0, 90, 90, 84.0, 85)])[0]
        self.assertEqual((t["reason"], t["exit"], t["gap"]), ("stop", 85.0, False))      # (86 + 84) / 2

    def test_kind_and_harsh_stops(self):
        rth = [OPEN, (10, 0, 95, 95, 89.75, 92), (11, 0, 90, 90, 84.0, 85)]
        self.assertEqual(trades(rth, fill="kind")[0]["exit"], 85.5)
        self.assertEqual(trades(rth, fill="harsh-stops")[0]["exit"], 84.0)

    def test_a_gap_through_the_stop_uses_the_open(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (10, 1, 92, 92, 91, 91), (11, 0, 85, 85, 84.0, 85)])[0]
        self.assertEqual((t["exit"], t["gap"]), (84.5, True))

    def test_stop_on_the_entry_minute(self):
        t = trades([OPEN, (10, 0, 95, 95, 85.0, 86)])[0]
        self.assertEqual((t["reason"], t["exit_ts"], t["exit"]), ("stop", ts(2024, 1, 9, 10, 0), 85.5))

    def test_target_needs_a_tick_through_and_not_on_the_entry_minute(self):
        self.assertEqual(trades([OPEN, (10, 0, 103, 103, 89.75, 92), (15, 55, 95, 95, 95, 95)])[0]["reason"], "flat")
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (10, 1, 92, 102, 92, 101), (10, 2, 101, 102.25, 100, 101),
                    (15, 55, 95, 95, 95, 95)])[0]
        self.assertEqual((t["reason"], t["exit"], t["exit_ts"]), ("target", 102.0, ts(2024, 1, 9, 10, 2)))

    def test_stop_before_target_in_one_minute(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (10, 1, 92, 103, 85, 100)])[0]
        self.assertEqual(t["reason"], "stop")

    def test_no_target(self):
        s = dict(S, target=None)
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (10, 1, 92, 200, 92, 150), (15, 55, 150, 150, 149, 150)], s)[0]
        self.assertEqual((t["reason"], t["target"], t["exit"]), ("flat", None, 149.5))

    def test_an_early_close_closes_at_the_last_close(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (12, 59, 93, 93, 91, 92.5)])[0]
        self.assertEqual((t["reason"], t["exit"], t["exit_ts"]), ("flat", 92.5, ts(2024, 1, 9, 12, 59)))

    def test_points_and_worst(self):
        t = trades([OPEN, (10, 0, 95, 95, 89.75, 92), (11, 0, 92, 93, 88, 92), (15, 55, 93, 99, 80, 93)])[0]
        self.assertEqual((t["points"], t["worst"]), (2.5, -2.0))           # exit 92.5; lows 89.75, 88; fill 92.5


def with_levels(rth, lv):
    mk = market(rth)
    next(d for d in mk.days if d.date == "2024-01-09").levels = lv
    return mk


ON96 = {"PD": [L("PD", 90.0, "low")], "ON": [L("ON", 96.0, "low")]}


class Spent(unittest.TestCase):
    def test_one_position_at_a_time_and_a_level_crossed_meanwhile_is_spent(self):
        # long at 90 from PD low; ON low at 96 is armed too in ALL: it is crossed first, so fills first
        s = dict(S, kind="ALL")
        mk = with_levels([OPEN, (10, 0, 100, 100, 95.75, 97), (10, 1, 97, 97, 89.75, 90), (10, 2, 90, 99, 90, 98),
                          (15, 55, 98, 98, 98, 98)], ON96)
        t = fade.per_contract(mk, s, "midpoint", dates={"2024-01-09"})["trades"]
        self.assertEqual([(x["kind"], x["entry"], x["reason"]) for x in t], [("ON", 96.0, "stop")])

    def test_a_level_crossed_during_a_trade_does_not_fill_later(self):
        s = dict(S, kind="ALL", target=5)                     # long 96, stop 92, target 116
        mk = with_levels([OPEN, (10, 0, 100, 100, 95.75, 97), (10, 1, 100, 115.25, 100, 115),
                          (10, 2, 115, 116.25, 114, 116), (10, 3, 116, 116, 114.5, 115), (15, 55, 115, 115, 115, 115)],
                         {"ON": [L("ON", 96.0, "low")], "PW": [L("PW", 115.0, "high")]})
        t = fade.per_contract(mk, s, "midpoint", dates={"2024-01-09"})["trades"]
        self.assertEqual([(x["kind"], x["entry"], x["reason"]) for x in t], [("ON", 96.0, "target")])

    def test_two_levels_in_one_minute_the_nearer_the_open_fills(self):
        s = dict(S, kind="ALL")
        mk = with_levels([OPEN, (10, 0, 100, 100, 89.0, 95), (15, 55, 98, 98, 98, 98)], ON96)
        t = fade.per_contract(mk, s, "midpoint", dates={"2024-01-09"})["trades"]
        self.assertEqual([(x["kind"], x["entry"]) for x in t], [("ON", 96.0)])

    def test_after_a_stop_the_next_level_can_fill(self):
        s = dict(S, kind="ALL")
        mk = with_levels([OPEN, (10, 0, 101, 101, 99.75, 100), (10, 1, 100, 100, 95.5, 96), (10, 2, 96, 96, 89.75, 90),
                          (15, 55, 92, 92, 92, 92)], {"PD": [L("PD", 90.0, "low")], "ON": [L("ON", 100.0, "low")]})
        t = fade.per_contract(mk, s, "midpoint", dates={"2024-01-09"})["trades"]
        self.assertEqual([(x["kind"], x["entry"], x["reason"]) for x in t], [("ON", 100.0, "stop"), ("PD", 90.0, "flat")])

    def test_armed_list(self):
        got = fade.per_contract(market([OPEN, (15, 55, 110, 110, 110, 110)]), S, "midpoint")["armed"]
        self.assertEqual(sorted((a["side"], a["level"]) for a in got["2024-01-09"]), [(-1, 130.0), (1, 90.0)])


def pc(market_name, date, entry_ts, side, entry, exit_, dist, worst):
    return {"market": market_name, "date": date, "kind": "PD", "level": entry, "side": side, "entry_ts": entry_ts,
            "entry": entry, "stop": entry - side * dist, "dist": dist, "target": None, "exit_ts": entry_ts + 60,
            "exit": exit_, "reason": "flat", "gap": False, "points": (exit_ - entry) * side, "worst": worst}


class Account(unittest.TestCase):
    SPECS = {"NQ": dict(SPEC), "ES": dict(SPEC, pv=5.0)}

    def test_size_net_and_day_records(self):
        by_m = {"NQ": [pc("NQ", "2024-01-09", 1, 1, 100.0, 110.0, 10.0, -4.0)],
                "ES": [pc("ES", "2024-01-09", 2, -1, 50.0, 52.0, 2.0, -3.0)]}
        r = fade.account(by_m, self.SPECS, 0.1, 150000.0)
        nq, es = r["trades"]
        # risk 150; NQ loss a contract (10 + 0.5) * 2 + 1.9 = 22.9 -> 6; ES (2 + 0.5) * 5 + 1.9 = 14.4 -> 10
        self.assertEqual((nq["qty"], es["qty"]), (6, 10))
        self.assertEqual((nq["net"], es["net"]), (round(10 * 2 * 6 - 1.9 * 6, 2), round(-2 * 5 * 10 - 1.9 * 10, 2)))
        self.assertEqual(nq["planned_cost"], round(22.9 * 6, 2))
        day = r["days"][0]
        low = 150000.0 + (-4 * 2 * 6 - 1.9 * 6) + (-3 * 5 * 10 - 1.9 * 10)
        self.assertEqual((day["start"], day["end"], day["low"]),
                         (150000.0, round(150000.0 + nq["net"] + es["net"], 2), round(low, 2)))

    def test_cap_and_under_one_contract(self):
        by_m = {"NQ": [pc("NQ", "2024-01-09", 1, 1, 100.0, 101.0, 0.25, -0.25)],
                "ES": [pc("ES", "2024-01-09", 2, 1, 50.0, 51.0, 400.0, -1.0)]}
        r = fade.account(by_m, self.SPECS, 1.0, 150000.0)
        self.assertEqual([t["qty"] for t in r["trades"]], [90])
        self.assertEqual([(s["market"], s["reason"]) for s in r["skipped"]], [("ES", "under one contract")])

    def test_the_day_start_balance_sizes_every_trade_of_the_day(self):
        by_m = {"NQ": [pc("NQ", "2024-01-09", 1, 1, 100.0, 110.0, 10.0, 0.0),
                       pc("NQ", "2024-01-09", 5, 1, 100.0, 110.0, 10.0, 0.0),
                       pc("NQ", "2024-01-10", 1, 1, 100.0, 110.0, 10.0, 0.0)]}
        r = fade.account(by_m, self.SPECS, 0.1, 150000.0)
        self.assertEqual([t["balance_start"] for t in r["trades"]],
                         [150000.0, 150000.0, round(150000.0 + 2 * r["trades"][0]["net"], 2)])

    def test_digest_is_stable(self):
        by_m = {"NQ": [pc("NQ", "2024-01-09", 1, 1, 100.0, 110.0, 10.0, -4.0)]}
        self.assertEqual(fade.account(by_m, self.SPECS, 0.1)["digest"], fade.account(by_m, self.SPECS, 0.1)["digest"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
