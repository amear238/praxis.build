SUMMARY b2-stitch label=REAL bars=1857362 days=1712 seams=21 dupes=0 gaps=937 overall=PASS

# Continuous NQ 1-min — Validation Report (b2-data spec §4)

**Dataset:** REAL  ·  **Construction:** volume-crossover roll (16 of 21 seams) + 5 no-overlap BOUNDARY-fallback seam(s) (volume-only, D-2026-07-21-A) + Difference (Panama) back-adjustment
**Output timezone:** America/New_York (ET) — timestamps are ET wall-clock; the 09:30-ET RTH anchor and the 17:00-18:00-ET maintenance break are evaluated in this tz.
**Overall:** PASS

_Run: 2026-07-22T18:42:05Z_

## §4 acceptance checks

| Check | Status | Detail |
|---|---|---|
| §4.1 RTH median == 390 | PASS | measured=390 over 1712 days |
| §4.1 ETH median in [1350,1380] | PASS | measured=1380 over 1712 days |
| §1.1 depth >= ~1008 trading days | PASS | trading days = 1712 |
| §4.2 no regular session inside 17:00-18:00 ET halt | PASS | max contiguous in-halt run = 2 min (FAIL threshold 5); 17:00:00 session-close endpoint excluded |
| §4.2 isolated illiquid halt prints (source artifact) | INFO | 48 isolated 1-min print(s) inside the halt over 43 day(s) (vol 1-10; retained for losslessness, not a tz/seam defect) |
| §4.2 DST boundary hold (both flips/yr) | PASS | 11 DST flip(s) in 2021-03-07..2026-07-20; 17:00-18:00-ET halt session-free across EST+EDT (max in-halt run=2 min) -> DST tracked |
| §4.3 anomalous intra-session gaps | FLAG | 937 anomalous gap(s) |
| §4.4 monotonic non-decreasing ts | PASS | 1857362 rows |
| §4.4 zero duplicate timestamps | PASS | removed 0 duplicate(s) |
| §3 roll count ~4/yr (~20 over 5yr) | INFO | 21 seam(s) in this series |
| §4.2 tz seam-loss == 0 (distinct instants preserved) | PASS | ET instants=1857362, baseline instants=1857362, seam-gap=0, bars=1857362 vs baseline=1857362 |

## Lossless tz-conversion invariants (Praxis_build-1u6)

UTC→America/New_York must relabel every instant 1:1 with no seam loss.

| Invariant | Value | Verdict |
|---|---|---|
| distinct_instants(ET output) | 1857362 | — |
| distinct_instants(UTC baseline) | 1857362 | — |
| ET == baseline (no instant dropped/merged) | True | PASS |
| seam-gap (baseline minutes missing from ET output) | 0 | PASS |
| final bar count | 1857362 | PASS (== baseline 1857362) |
| minutes the NAIVE convert-then-route path would DROP | 2498 | (trap, avoided) |

**09:30-ET RTH-open spot-check:** stored-UTC `2021-03-08 14:30:00 UTC` → emitted-ET `2021-03-08 09:30:00 EST` (src 06-21) — RTH anchor lands exactly on 09:30 ET.

## §3 roll seams

| # | Roll date | Front→Back | Front close | Back close | Raw gap | Front offset | Roll trigger |
|---|---|---|---|---|---|---|---|
| 1 | 2021-06-11 | 06-21→09-21 | 13994.2 | 13985.8 | -8.50 | +3416.00 | ⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A) |
| 2 | 2021-09-10 | 09-21→12-21 | 15441.5 | 15434 | -7.50 | +3424.50 | ⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A) |
| 3 | 2021-12-10 | 12-21→03-22 | 16329.8 | 16331.5 | +1.75 | +3432.00 | VOLUME-ONLY (deviation) |
| 4 | 2022-03-11 | 03-22→06-22 | 13292 | 13289 | -3.00 | +3430.25 | ⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A) |
| 5 | 2022-06-10 | 06-22→09-22 | 11840 | 11867.8 | +27.75 | +3433.25 | ⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A) |
| 6 | 2022-09-09 | 09-22→12-22 | 12592.5 | 12670.2 | +77.75 | +3405.50 | ⚠ BOUNDARY fallback (volume-only, D-2026-07-21-A) |
| 7 | 2022-12-12 | 12-22→03-23 | 11711.8 | 11829.8 | +118.00 | +3327.75 | VOLUME-ONLY (deviation) |
| 8 | 2023-03-13 | 03-23→06-23 | 11931.8 | 12055 | +123.25 | +3209.75 | VOLUME-ONLY (deviation) |
| 9 | 2023-06-12 | 06-23→09-23 | 14800.5 | 14986.8 | +186.25 | +3086.50 | VOLUME-ONLY (deviation) |
| 10 | 2023-09-11 | 09-23→12-23 | 15475.8 | 15674.2 | +198.50 | +2900.25 | VOLUME-ONLY (deviation) |
| 11 | 2023-12-11 | 12-23→03-24 | 16237 | 16450 | +213.00 | +2701.75 | VOLUME-ONLY (deviation) |
| 12 | 2024-03-11 | 03-24→06-24 | 17971 | 18216.2 | +245.25 | +2488.75 | VOLUME-ONLY (deviation) |
| 13 | 2024-06-17 | 06-24→09-24 | 19921.2 | 20192.8 | +271.50 | +2243.50 | VOLUME-ONLY (deviation) |
| 14 | 2024-09-16 | 09-24→12-24 | 19433 | 19665.2 | +232.25 | +1972.00 | VOLUME-ONLY (deviation) |
| 15 | 2024-12-17 | 12-24→03-25 | 22014.8 | 22314.5 | +299.75 | +1739.75 | VOLUME-ONLY (deviation) |
| 16 | 2025-03-18 | 03-25→06-25 | 19496.8 | 19701.8 | +205.00 | +1440.00 | VOLUME-ONLY (deviation) |
| 17 | 2025-06-16 | 06-25→09-25 | 21941.5 | 22168.2 | +226.75 | +1235.00 | VOLUME-ONLY (deviation) |
| 18 | 2025-09-16 | 09-25→12-25 | 24284 | 24522.2 | +238.25 | +1008.25 | VOLUME-ONLY (deviation) |
| 19 | 2025-12-15 | 12-25→03-26 | 25093.2 | 25342.8 | +249.50 | +770.00 | VOLUME-ONLY (deviation) |
| 20 | 2026-03-16 | 03-26→06-26 | 24675.8 | 24891.2 | +215.50 | +520.50 | VOLUME-ONLY (deviation) |
| 21 | 2026-06-15 | 06-26→09-26 | 30559.2 | 30864.2 | +305.00 | +305.00 | VOLUME-ONLY (deviation) |

## §4.3 anomalous gaps

- 2021-03-07 18:59:00-05:00 → 2021-03-07 19:03:00-05:00 (4 min)
- 2021-03-07 19:07:00-05:00 → 2021-03-07 19:10:00-05:00 (3 min)
- 2021-03-07 19:10:00-05:00 → 2021-03-07 19:12:00-05:00 (2 min)
- 2021-03-07 19:15:00-05:00 → 2021-03-07 19:17:00-05:00 (2 min)
- 2021-03-07 19:21:00-05:00 → 2021-03-07 19:23:00-05:00 (2 min)
- 2021-03-07 19:28:00-05:00 → 2021-03-07 19:31:00-05:00 (3 min)
- 2021-03-07 19:33:00-05:00 → 2021-03-07 19:35:00-05:00 (2 min)
- 2021-03-07 19:35:00-05:00 → 2021-03-07 19:37:00-05:00 (2 min)
- 2021-03-07 19:37:00-05:00 → 2021-03-07 19:39:00-05:00 (2 min)
- 2021-03-07 19:40:00-05:00 → 2021-03-07 19:42:00-05:00 (2 min)
- 2021-03-07 19:46:00-05:00 → 2021-03-07 19:48:00-05:00 (2 min)
- 2021-03-07 19:48:00-05:00 → 2021-03-07 19:50:00-05:00 (2 min)
- 2021-03-07 19:55:00-05:00 → 2021-03-07 19:57:00-05:00 (2 min)
- 2021-03-07 19:59:00-05:00 → 2021-03-07 20:01:00-05:00 (2 min)
- 2021-03-07 20:03:00-05:00 → 2021-03-07 20:05:00-05:00 (2 min)
- 2021-03-07 20:06:00-05:00 → 2021-03-07 20:09:00-05:00 (3 min)
- 2021-03-07 20:09:00-05:00 → 2021-03-07 20:11:00-05:00 (2 min)
- 2021-03-07 20:17:00-05:00 → 2021-03-07 20:19:00-05:00 (2 min)
- 2021-03-07 20:27:00-05:00 → 2021-03-07 20:29:00-05:00 (2 min)
- 2021-03-07 20:32:00-05:00 → 2021-03-07 20:34:00-05:00 (2 min)
- 2021-03-07 20:34:00-05:00 → 2021-03-07 20:37:00-05:00 (3 min)
- 2021-03-07 20:37:00-05:00 → 2021-03-07 20:39:00-05:00 (2 min)
- 2021-03-07 20:41:00-05:00 → 2021-03-07 20:43:00-05:00 (2 min)
- 2021-03-07 20:49:00-05:00 → 2021-03-07 20:51:00-05:00 (2 min)
- 2021-03-07 20:51:00-05:00 → 2021-03-07 20:53:00-05:00 (2 min)
- 2021-03-07 20:53:00-05:00 → 2021-03-07 20:55:00-05:00 (2 min)
- 2021-03-07 20:55:00-05:00 → 2021-03-07 20:58:00-05:00 (3 min)
- 2021-03-07 20:58:00-05:00 → 2021-03-07 21:01:00-05:00 (3 min)
- 2021-03-07 21:01:00-05:00 → 2021-03-07 21:03:00-05:00 (2 min)
- 2021-03-07 21:06:00-05:00 → 2021-03-07 21:08:00-05:00 (2 min)
- 2021-03-07 21:09:00-05:00 → 2021-03-07 21:11:00-05:00 (2 min)
- 2021-03-07 21:11:00-05:00 → 2021-03-07 21:13:00-05:00 (2 min)
- 2021-03-07 21:32:00-05:00 → 2021-03-07 21:34:00-05:00 (2 min)
- 2021-03-07 21:38:00-05:00 → 2021-03-07 21:40:00-05:00 (2 min)
- 2021-03-07 21:41:00-05:00 → 2021-03-07 21:45:00-05:00 (4 min)
- 2021-03-07 21:54:00-05:00 → 2021-03-07 21:57:00-05:00 (3 min)
- 2021-03-07 21:58:00-05:00 → 2021-03-07 22:00:00-05:00 (2 min)
- 2021-03-07 22:01:00-05:00 → 2021-03-07 22:03:00-05:00 (2 min)
- 2021-03-07 22:06:00-05:00 → 2021-03-07 22:08:00-05:00 (2 min)
- 2021-03-07 22:08:00-05:00 → 2021-03-07 22:10:00-05:00 (2 min)
- 2021-03-07 22:15:00-05:00 → 2021-03-07 22:17:00-05:00 (2 min)
- 2021-03-07 22:17:00-05:00 → 2021-03-07 22:20:00-05:00 (3 min)
- 2021-03-07 22:20:00-05:00 → 2021-03-07 22:22:00-05:00 (2 min)
- 2021-03-07 22:22:00-05:00 → 2021-03-07 22:24:00-05:00 (2 min)
- 2021-03-07 22:24:00-05:00 → 2021-03-07 22:29:00-05:00 (5 min)
- 2021-03-07 22:29:00-05:00 → 2021-03-07 22:31:00-05:00 (2 min)
- 2021-03-07 22:39:00-05:00 → 2021-03-07 22:42:00-05:00 (3 min)
- 2021-03-07 22:58:00-05:00 → 2021-03-07 23:00:00-05:00 (2 min)
- 2021-03-07 23:00:00-05:00 → 2021-03-07 23:10:00-05:00 (10 min)
- 2021-03-07 23:10:00-05:00 → 2021-03-07 23:13:00-05:00 (3 min)

