#!/usr/bin/env python3
"""specs.py -- the eleven markets of the trend plan (research/trend-150k/PLAN.md, table "Instruments" and the
2026-11-18 amendment) and one loader for their bars.

SPECS: {data root: {"traded": the contract traded, "pv": dollars a point, "tick", "comm": commission a contract
round trip, "slip_ticks": slippage per market order, "max_qty": the per-trade cap}}. Order = processing order.

load(market, minutes=True) -> {"daily": [mdata.Adj] back-adjusted, "rolls": [mdata.Roll],
"minutes": [mdata.Bar] or None}. Daily bars are UTC-day bars with the weekend stubs merged into Monday, the
front month adjusted with the second month.

Standard library only. Run with python3 -I -B.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import mdata  # noqa: E402

MICRO_CAP, MINI_CAP = 90, 9


def _s(traded, pv, tick, comm, slip, cap):
    return {"traded": traded, "pv": pv, "tick": tick, "comm": comm, "slip_ticks": slip, "max_qty": cap}


SPECS = {
    "NQ": _s("MNQ", 2.0, 0.25, 1.90, 2, MICRO_CAP),
    "ES": _s("MES", 5.0, 0.25, 1.90, 2, MICRO_CAP),
    "RTY": _s("M2K", 5.0, 0.10, 1.90, 2, MICRO_CAP),
    "CL": _s("MCL", 100.0, 0.01, 1.90, 2, MICRO_CAP),
    "GC": _s("MGC", 10.0, 0.10, 1.90, 2, MICRO_CAP),
    "ZN": _s("ZN", 1000.0, 1 / 64, 5.00, 1, MINI_CAP),
    "ZB": _s("ZB", 1000.0, 1 / 32, 5.00, 2, MINI_CAP),
    "6E": _s("M6E", 12500.0, 0.0001, 1.90, 1, MICRO_CAP),
    "6J": _s("MJY", 1250000.0, 0.000001, 1.90, 1, MICRO_CAP),
    "6B": _s("M6B", 6250.0, 0.0001, 1.90, 1, MICRO_CAP),
    "6A": _s("M6A", 10000.0, 0.0001, 1.90, 1, MICRO_CAP),
}
MARKETS = tuple(SPECS)


def load(market, minutes=True, root=mdata.ROOT):
    front = mdata.trading_days(mdata.series(market, "ohlcv-1d", "v.0", root))
    second = mdata.trading_days(mdata.series(market, "ohlcv-1d", "v.1", root))
    daily, rolls = mdata.back_adjust(front, second)
    mins = mdata.series(market, "ohlcv-1m", "v.0", root) if minutes else None
    return {"daily": daily, "rolls": rolls, "minutes": mins}
