#!/usr/bin/env python3
"""mdata.py -- read the bought Databento bars and back-adjust the daily series across contract rolls.

Files: market-data/databento/<market>.<rank>.<schema>.<start>_<end>.dbn.zst (see research/data/fetch_databento.py).
Format: DBN, zstd-compressed. "DBN" + version byte, a u32 metadata length, the metadata, then 56-byte OHLCV
records: length u8 (14, in 4-byte words), rtype u8, publisher u16, instrument_id u32, ts_event u64
(nanoseconds UTC, the bar's START), open, high, low, close i64 (price * 1e9), volume u64. The metadata
(symbol maps) is not needed: each record carries its contract's instrument_id.

read_dbn(path) -> [Bar]. trading_days(daily) merges the weekend stubs of UTC-day daily bars into Monday. series(market, schema, rank, root) -> the series' chunks merged, sorted by ts; a stamp
present twice must be identical, else ValueError (a data error is never silently resolved).

back_adjust(front, second) -> ([Adj], [Roll]). A roll is a bar whose front contract differs from the previous
bar's. Its gap = the second-month close minus the front close on the previous bar's stamp, taken only when
that second-month bar is the contract the front rolled into; otherwise the roll is listed with gap None and
nothing is added. Every bar before a roll gets that roll's gap added to its open, high, low and close
(additive back-adjustment), so the adjusted series has no fake move at a roll and the latest prices are the
actual ones. Signals read adj_*; fills read bar (the actual contract's prices).

Standard library only (Python 3.14 for compression.zstd). Run tests with python3 -I -B.
"""
import glob
import os
import struct
from collections import namedtuple
from compression import zstd

Bar = namedtuple("Bar", "ts iid open high low close volume")
Adj = namedtuple("Adj", "bar adj_open adj_high adj_low adj_close")
Roll = namedtuple("Roll", "ts old_iid new_iid gap")

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "market-data", "databento")
_REC = struct.Struct("<BBHIQqqqqQ")
_OHLCV_RTYPES = {0x20, 0x21, 0x22, 0x23, 0x24}
_SCALE = 1e9
DAY_NS = 86400 * 1_000_000_000


def read_dbn(path):
    with open(path, "rb") as f:
        raw = zstd.decompress(f.read())
    if raw[:3] != b"DBN":
        raise ValueError(f"not a DBN file: {path}")
    (mlen,) = struct.unpack_from("<I", raw, 4)
    body = memoryview(raw)[8 + mlen:]
    if len(body) % _REC.size:
        raise ValueError(f"{path}: body of {len(body)} bytes is not whole 56-byte records")
    out = []
    for length, rtype, _pub, iid, ts, o, h, l, c, v in _REC.iter_unpack(body):
        if length != 14 or rtype not in _OHLCV_RTYPES:
            raise ValueError(f"{path}: unexpected record (length {length}, rtype {rtype:#x})")
        out.append(Bar(ts, iid, o / _SCALE, h / _SCALE, l / _SCALE, c / _SCALE, v))
    return out


def series(market, schema, rank, root=ROOT):
    files = sorted(glob.glob(os.path.join(root, f"{market}.{rank}.{schema}.*_*.dbn.zst")))
    by_ts = {}
    for p in files:
        for b in read_dbn(p):
            seen = by_ts.get(b.ts)
            if seen is not None and seen != b:
                raise ValueError(f"{market} {rank} {schema}: two different bars at ts {b.ts}")
            by_ts[b.ts] = b
    return [by_ts[t] for t in sorted(by_ts)]


def trading_days(bars):
    """Daily bars are cut by UTC day, so Sunday evening's first hours (and any Saturday stub) arrive as their own
    bar. Each weekend bar is merged into the next bar when that bar is the same contract (open from the weekend
    bar, high / low across both, close and stamp from the weekday bar, volumes added), else dropped."""
    out, carry = [], None
    for b in bars:
        weekday = (b.ts // DAY_NS + 3) % 7          # 1970-01-01 was a Thursday: 0 = Monday
        if weekday >= 5:
            carry = b if carry is None or carry.iid != b.iid else Bar(
                carry.ts, b.iid, carry.open, max(carry.high, b.high), min(carry.low, b.low), b.close,
                carry.volume + b.volume)
            continue
        if carry is not None and carry.iid == b.iid:
            b = Bar(b.ts, b.iid, carry.open, max(carry.high, b.high), min(carry.low, b.low), b.close,
                    carry.volume + b.volume)
        carry = None
        out.append(b)
    return out


def back_adjust(front, second):
    sec_at = {b.ts: b for b in second}
    rolls = []
    for prev, cur in zip(front, front[1:]):
        if cur.iid != prev.iid:
            s = sec_at.get(prev.ts)
            gap = s.close - prev.close if s is not None and s.iid == cur.iid else None
            rolls.append(Roll(cur.ts, prev.iid, cur.iid, gap))
    out, k, add = [], len(rolls), 0.0
    # walk backwards: a bar gets the sum of the gaps of every roll stamped after it
    for b in reversed(front):
        while k and rolls[k - 1].ts > b.ts:
            k -= 1
            add += rolls[k].gap or 0.0
        out.append(Adj(b, b.open + add, b.high + add, b.low + add, b.close + add))
    out.reverse()
    return out, rolls
