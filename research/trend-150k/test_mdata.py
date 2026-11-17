#!/usr/bin/env python3
"""Tests for mdata.py (the Databento loader and roll back-adjustment). Run: python3 -I -B research/trend-150k/test_mdata.py"""
import os
import struct
import sys
import tempfile
import unittest
from compression import zstd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdata  # noqa: E402

NS = 1_000_000_000
DAY = 86400 * NS


def rec(ts, iid, o, h, l, c, v=1):
    s = 1e9
    return struct.pack("<BBHIQqqqqQ", 14, 0x20, 1, iid, ts, round(o * s), round(h * s), round(l * s), round(c * s), v)


def write_dbn(path, recs, meta=b"\x00" * 40):
    raw = b"DBN\x03" + struct.pack("<I", len(meta)) + meta + b"".join(recs)
    with open(path, "wb") as f:
        f.write(zstd.compress(raw))


class ReadTests(unittest.TestCase):
    def test_reads_records_in_dollars(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "X.v.0.ohlcv-1d.2020-01-01_2020-01-03.dbn.zst")
            write_dbn(p, [rec(1 * DAY, 7, 100.25, 101.5, 99.75, 100.0, 5)])
            bars = mdata.read_dbn(p)
            self.assertEqual(bars, [mdata.Bar(1 * DAY, 7, 100.25, 101.5, 99.75, 100.0, 5)])

    def test_rejects_non_dbn(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "bad.dbn.zst")
            with open(p, "wb") as f:
                f.write(zstd.compress(b"NOPE" + b"\x00" * 60))
            with self.assertRaises(ValueError):
                mdata.read_dbn(p)

    def test_rejects_wrong_record_length(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.dbn.zst")
            write_dbn(p, [rec(1, 1, 1, 1, 1, 1)[:-8]])
            with self.assertRaises(ValueError):
                mdata.read_dbn(p)

    def test_series_merges_chunks_sorted_and_rejects_overlap_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            write_dbn(os.path.join(d, "X.v.0.ohlcv-1d.2020-01-02_2020-01-03.dbn.zst"), [rec(2 * DAY, 1, 2, 2, 2, 2)])
            write_dbn(os.path.join(d, "X.v.0.ohlcv-1d.2020-01-01_2020-01-02.dbn.zst"), [rec(1 * DAY, 1, 1, 1, 1, 1)])
            write_dbn(os.path.join(d, "Y.v.0.ohlcv-1d.2020-01-01_2020-01-02.dbn.zst"), [rec(1 * DAY, 9, 9, 9, 9, 9)])
            s = mdata.series("X", "ohlcv-1d", "v.0", root=d)
            self.assertEqual([b.ts for b in s], [1 * DAY, 2 * DAY])
            # same stamp twice with different values is a data error
            write_dbn(os.path.join(d, "X.v.0.ohlcv-1d.2020-01-02_2020-01-04.dbn.zst"), [rec(2 * DAY, 1, 3, 3, 3, 3)])
            with self.assertRaises(ValueError):
                mdata.series("X", "ohlcv-1d", "v.0", root=d)


def B(day, iid, c, h=None, l=None):
    return mdata.Bar(day * DAY, iid, c, h if h is not None else c, l if l is not None else c, c, 1)


class AdjustTests(unittest.TestCase):
    def test_no_roll_means_no_adjustment(self):
        front = [B(1, 1, 100), B(2, 1, 101), B(3, 1, 102)]
        adj, rolls = mdata.back_adjust(front, [])
        self.assertEqual([a.adj_close for a in adj], [100, 101, 102])
        self.assertEqual(rolls, [])

    def test_roll_adds_the_gap_to_every_earlier_bar(self):
        # day 3 the front moves from contract 1 to contract 2; on day 2 contract 2 closed 10 above contract 1
        front = [B(1, 1, 100), B(2, 1, 101), B(3, 2, 112), B(4, 2, 113)]
        second = [B(1, 2, 110), B(2, 2, 111), B(3, 3, 120), B(4, 3, 121)]
        adj, rolls = mdata.back_adjust(front, second)
        self.assertEqual([a.adj_close for a in adj], [110, 111, 112, 113])
        self.assertEqual([round(a.adj_high, 9) for a in adj], [110, 111, 112, 113])
        self.assertEqual(len(rolls), 1)
        self.assertEqual(rolls[0], mdata.Roll(3 * DAY, 1, 2, 10.0))
        # actual prices are untouched
        self.assertEqual([a.bar.close for a in adj], [100, 101, 112, 113])

    def test_two_rolls_accumulate(self):
        front = [B(1, 1, 100), B(2, 2, 105), B(3, 3, 100)]
        second = [B(1, 2, 104), B(2, 3, 99), B(3, 4, 98)]
        adj, rolls = mdata.back_adjust(front, second)
        # gap1 at day 2 = 104 - 100 = 4 ; gap2 at day 3 = 99 - 105 = -6
        self.assertEqual([a.adj_close for a in adj], [100 + 4 - 6, 105 - 6, 100])
        self.assertEqual([r.gap for r in rolls], [4.0, -6.0])

    def test_roll_without_matching_second_month_is_listed_unadjusted(self):
        front = [B(1, 1, 100), B(2, 5, 130)]
        second = [B(1, 2, 104)]  # contract 2 was second, but the front jumped to contract 5
        adj, rolls = mdata.back_adjust(front, second)
        self.assertEqual([a.adj_close for a in adj], [100, 130])
        self.assertEqual(rolls, [mdata.Roll(2 * DAY, 1, 5, None)])


if __name__ == "__main__":
    unittest.main(verbosity=1)
