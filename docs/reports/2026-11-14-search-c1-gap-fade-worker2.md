# 2026-11-14 search C1 gap fade — worker 2 (cold re-implementation)

Filer's note (praxis-manager): the harness blocked this worker from writing `.md` report files, so it returned the report body inline. The manager filed the body below as returned. Only this note was added, and the HTML escapes in the returned text (`&lt;`, `&gt;`, `&amp;`) were turned back into `<`, `>`, `&`. The worker's files are in `/tmp/praxis-c1/reimpl/`.

## Task
Re-implement unit `2026-11-14-search-c1-gap-fade` (bead `Praxis_build-vn4`) from `/tmp/praxis-c1/reimpl/RULES.md` (sha256 f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3) alone, in-sample only, variants V1/V2/V3. Script: `/tmp/praxis-c1/reimpl/reimpl.py`. Per-trade CSVs: `/tmp/praxis-c1/reimpl/is_trades_V1.csv`, `is_trades_V2.csv`, `is_trades_V3.csv`.

## Mode
ADVERSARIAL, cold re-implementation. I read nothing under `research/`, nothing in `/tmp/praxis-c1/` outside `reimpl/`, and no `docs/reports/2026-11-14-search-c1*` file. I wrote nothing in the repo. Python 3 with `-I -B`, standard library only.

This is a Python pre-screen, not an NT8 run. None of these results are validated.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Interpretations
1. **RTH bars:** stamps 093100 to 160000 inclusive, grouped by the stamp's calendar date. Every stamp in the file has seconds 00 (checked).
2. **Trading day:** any date whose earliest RTH bar is stamped 093100, applied literally. So a Sunday with one stray 09:31 bar counts: 2021-03-28 (in-sample) and 2025-03-16. Dates with RTH-window bars but no 09:31 bar are not trading days (139 such dates, all printed below).
3. **Previous trading day:** the immediately preceding trading day as defined in item 2. PC is the close of its last RTH bar. On early-close days and on the truncated 2023-04-05 (last bar 14:03), that bar is earlier than 16:00. 2021-03-29 takes its PC from the Sunday 2021-03-28 stray bar (16375), not from the Friday close.
4. **4-day skip:** skip when (date − previous trading day) is more than 4 calendar days. The first trading day in the file (2021-03-08) has no previous trading day and is skipped.
5. **Gap band:** gap_pct is computed with exact rationals (`Fraction`), so the inclusive bounds GMIN <= |gap| <= GMAX are compared exactly, with no float edge errors.
6. **Bar order:** bars are scanned from the 09:31 bar (the entry bar) through the last RTH bar of the day. On each bar the stop is tested before the target, so a bar that hits both exits at the stop.
7. **Stop:** hit at exact touch (short high >= stop, long low <= stop). No tick-through is required.
8. **Target:** needs a 1-tick trade-through of PC.
9. **Fills:** "worsened by 0.5" means against the trader. Short entry O−0.5. Short exits (buys) at level+0.5. Long entry O+0.5. Long exits (sells) at level−0.5.
10. **Time exit:** close of the day's last RTH bar, minus 0.5 for a long or plus 0.5 for a short. If 2021-03-28 had traded, that bar would be its own entry bar; it did not trade in any variant.
11. **Trade period:** set by the entry date. Points = (exit − entry) × side, with long = +1 and short = −1.
12. **Costs:**
    - NQ net = points × 20 − 2.96, or points × 20 − 4.68.
    - MNQ net = points × 2 − 1.90.
13. **Profit factor @ $4.68:** sum of per-trade NQ net that is greater than 0, divided by the absolute sum of per-trade NQ net that is less than 0. Each trade's net is after its $4.68.
14. **Max drawdown:** the largest drop from a running peak in cumulative closed-trade P&L, with the peak starting at 0. Only this one measure was computed, at NQ $4.68 and at 1 MNQ.
    - End-of-day equity is not computed. For this one-trade-per-day intraday strategy it would match closed-trade equity at day ends, but that is INFERRED, not computed.
    - The MAE-based intratrade low and the D6 window measures are not computed. The brief scoped them out, and the MAE method lives in the unit report, which I may not read.
15. **No roll handling:** the continuous series is used as-is. Any gaps caused by contract rolls were not checked or handled (UNVERIFIED whether the series is back-adjusted).

## Run output (verbatim)
```
Sat Nov 14 13:16:46 UTC 2026
C1 gap fade re-implementation (worker 2) - IN-SAMPLE ONLY 2021-03-08 to 2024-12-31
Trading days in whole file: 1355 (first 2021-03-08, last 2026-07-20)
In-sample trading days with a valid setup: 969
Dates in whole file with RTH bars but NO 09:31-stamped bar (not trading days): 139 ['2021-03-14', '2021-03-20', '2021-04-03', '2021-04-04', '2021-04-17', '2021-04-18', '2021-05-01', '2021-05-02', '2021-05-08', '2021-06-12', '2021-06-20', '2021-06-26', '2021-07-18', '2021-07-25', '2021-08-01', '2021-08-14', '2021-08-21', '2021-08-28', '2021-09-04', '2021-10-24', '2021-10-31', '2021-11-13', '2021-11-21', '2021-12-12', '2021-12-19', '2022-01-23', '2022-01-30', '2022-02-20', '2022-03-06', '2022-03-13', '2022-03-19', '2022-03-27', '2022-04-03', '2022-04-10', '2022-04-24', '2022-05-01', '2022-05-08', '2022-05-29', '2022-06-04', '2022-06-18', '2022-06-19', '2022-07-16', '2022-07-17', '2022-07-30', '2022-07-31', '2022-08-07', '2022-08-28', '2022-09-03', '2022-09-04', '2022-09-10', '2022-10-09', '2022-10-16', '2022-10-30', '2022-11-06', '2022-11-13', '2022-11-26', '2023-02-05', '2023-03-04', '2023-03-18', '2023-03-19', '2023-04-15', '2023-05-07', '2023-06-03', '2023-06-04', '2023-06-25', '2023-08-27', '2023-09-10', '2023-09-17', '2023-11-05', '2023-11-11', '2023-12-31', '2024-01-13', '2024-01-20', '2024-01-21', '2024-02-03', '2024-02-25', '2024-03-09', '2024-03-10', '2024-05-04', '2024-05-12', '2024-06-02', '2024-06-08', '2024-07-07', '2024-07-21', '2024-07-28', '2024-08-25', '2024-09-28', '2024-10-12', '2024-10-26', '2024-10-27', '2024-11-23', '2024-11-24', '2024-11-30', '2024-12-08', '2024-12-29', '2025-01-11', '2025-02-01', '2025-02-16', '2025-02-23', '2025-03-02', '2025-03-09', '2025-03-15', '2025-03-30', '2025-04-20', '2025-04-27', '2025-05-03', '2025-05-04', '2025-05-11', '2025-05-17', '2025-05-18', '2025-05-25', '2025-06-08', '2025-06-15', '2025-06-22', '2025-07-06', '2025-07-20', '2025-07-27', '2025-08-03', '2025-08-09', '2025-08-10', '2025-08-24', '2025-08-30', '2025-09-07', '2025-09-28', '2025-10-05', '2025-10-19', '2025-10-26', '2025-11-02', '2025-11-09', '2025-11-16', '2025-11-23', '2026-01-04', '2026-01-11', '2026-01-18', '2026-01-25', '2026-02-01', '2026-02-07', '2026-02-08', '2026-04-05']
In-sample setup days whose last RTH bar is not 16:00 (time exit at that bar): 34 ['2021-03-28@093100', '2021-05-31@130000', '2021-07-05@130000', '2021-09-06@130000', '2021-11-25@130000', '2021-11-26@131500', '2022-01-17@130000', '2022-02-21@130000', '2022-05-30@130000', '2022-06-20@130000', '2022-07-04@130000', '2022-09-05@130000', '2022-11-24@130000', '2022-11-25@131500', '2023-01-16@130000', '2023-02-20@130000', '2023-04-05@140300', '2023-05-29@130000', '2023-06-19@130000', '2023-07-03@131500', '2023-07-04@130000', '2023-09-04@130000', '2023-11-23@130000', '2023-11-24@131500', '2024-01-15@130000', '2024-02-19@130000', '2024-05-27@130000', '2024-06-19@130000', '2024-07-03@131500', '2024-07-04@130000', '2024-09-02@130000', '2024-11-28@130000', '2024-11-29@131500', '2024-12-24@131500']
In-sample setup days whose PC bar is not 16:00: 34 ['2021-03-29(prev 2021-03-28@093100)', '2021-06-01(prev 2021-05-31@130000)', '2021-07-06(prev 2021-07-05@130000)', '2021-09-07(prev 2021-09-06@130000)', '2021-11-26(prev 2021-11-25@130000)', '2021-11-29(prev 2021-11-26@131500)', '2022-01-18(prev 2022-01-17@130000)', '2022-02-22(prev 2022-02-21@130000)', '2022-05-31(prev 2022-05-30@130000)', '2022-06-21(prev 2022-06-20@130000)', '2022-07-05(prev 2022-07-04@130000)', '2022-09-06(prev 2022-09-05@130000)', '2022-11-25(prev 2022-11-24@130000)', '2022-11-28(prev 2022-11-25@131500)', '2023-01-17(prev 2023-01-16@130000)', '2023-02-21(prev 2023-02-20@130000)', '2023-04-06(prev 2023-04-05@140300)', '2023-05-30(prev 2023-05-29@130000)', '2023-06-20(prev 2023-06-19@130000)', '2023-07-04(prev 2023-07-03@131500)', '2023-07-05(prev 2023-07-04@130000)', '2023-09-05(prev 2023-09-04@130000)', '2023-11-24(prev 2023-11-23@130000)', '2023-11-27(prev 2023-11-24@131500)', '2024-01-16(prev 2024-01-15@130000)', '2024-02-20(prev 2024-02-19@130000)', '2024-05-28(prev 2024-05-27@130000)', '2024-06-20(prev 2024-06-19@130000)', '2024-07-04(prev 2024-07-03@131500)', '2024-07-05(prev 2024-07-04@130000)', '2024-09-03(prev 2024-09-02@130000)', '2024-11-29(prev 2024-11-28@130000)', '2024-12-02(prev 2024-11-29@131500)', '2024-12-26(prev 2024-12-24@131500)']
Skipped in-sample days: 2
  SKIP 2021-03-08: no previous trading day in data
  SKIP 2021-09-27: previous trading day 2021-09-09 is 18 calendar days back (>4)

=== V1  GMIN 0.10  GMAX 0.50 ===
trades 456 (long 214 / short 242); exits target 216 / stop 221 / time 19
gross points -1085.50
net NQ @ $2.96/rt: -23059.76
net NQ @ $4.68/rt: -23844.08
profit factor @ $4.68 (sum of per-trade net>0 / |sum of per-trade net<0|): 0.8986  (gross win 211370.72 / gross loss 235214.80)
net 1 MNQ (points x $2 - $1.90): -3037.40
max DD closed-trade, NQ @ $4.68: 38125.48
max DD closed-trade, 1 MNQ: 4257.90
winners @ $4.68: 221 of 456

=== V2  GMIN 0.20  GMAX 0.80 ===
trades 488 (long 225 / short 263); exits target 224 / stop 218 / time 46
gross points 347.75
net NQ @ $2.96/rt: 5510.52
net NQ @ $4.68/rt: 4671.16
profit factor @ $4.68 (sum of per-trade net>0 / |sum of per-trade net<0|): 1.0132  (gross win 358262.44 / gross loss 353591.28)
net 1 MNQ (points x $2 - $1.90): -231.70
max DD closed-trade, NQ @ $4.68: 29876.28
max DD closed-trade, 1 MNQ: 3339.90
winners @ $4.68: 242 of 488

=== V3  GMIN 0.05  GMAX 0.30 ===
trades 360 (long 165 / short 195); exits target 170 / stop 181 / time 9
gross points -572.75
net NQ @ $2.96/rt: -12520.60
net NQ @ $4.68/rt: -13139.80
profit factor @ $4.68 (sum of per-trade net>0 / |sum of per-trade net<0|): 0.8876  (gross win 103795.04 / gross loss 116934.84)
net 1 MNQ (points x $2 - $1.90): -1829.50
max DD closed-trade, NQ @ $4.68: 17911.76
max DD closed-trade, 1 MNQ: 2170.40
winners @ $4.68: 172 of 360

Sat Nov 14 13:16:50 UTC 2026
```

### Data-artifact check (verbatim)
```
weekend 0931 2021-03-28 Sun 20210328 093100;16375;16375;16375;16375;1
weekend 0931 2025-03-16 Sun 20250316 093100;21107.5;21107.5;21107.5;21107.5;1
20210328 093100;16375;16375;16375;16375;1
1083
20230405 140100;16144;16145.25;16141.25;16142.25;915
20230405 140200;16142.5;16145;16142.25;16144.75;529
20230405 140300;16144.5;16147.75;16144.5;16147.25;338
V1 2021-03-29,long,16375.0,16357.25,-0.108397,16357.75,stop,093300,16339.0,-18.75,-379.68
V1 2023-04-05,long,16309.75,16260.25,-0.303499,16260.75,stop,094900,16210.25,-50.5,-1014.68
V1 2023-04-06,long,16147.25,16099.0,-0.298812,16099.5,stop,093600,16050.25,-49.25,-989.68
V2 2023-04-05,long,16309.75,16260.25,-0.303499,16260.75,stop,094900,16210.25,-50.5,-1014.68
V2 2023-04-06,long,16147.25,16099.0,-0.298812,16099.5,stop,093600,16050.25,-49.25,-989.68
V3 2021-03-29,long,16375.0,16357.25,-0.108397,16357.75,stop,093300,16339.0,-18.75,-379.68
V3 2023-04-06,long,16147.25,16099.0,-0.298812,16099.5,stop,093600,16050.25,-49.25,-989.68
```
Two days depend on the literal reading and should be compared with the other implementation:
- **2021-03-29:** PC comes from the Sunday stray bar. This changes the V1 and V3 trades that day.
- **2023-04-06:** PC comes from the 14:03 bar, because the 2023-04-05 data is truncated. All three variants trade that day.

### CSV spot check (verbatim)
```
date,side,PC,O,gap_pct,entry_fill,exit_kind,exit_stamp,exit_fill,points,nq_net_468
2021-03-16,short,16484.25,16575.75,0.555075,16575.25,stop,102300,16667.75,-92.5,-1854.68
2021-03-17,long,16554.75,16423.0,-0.795844,16423.5,target,141200,16554.25,130.75,2610.32
2021-03-22,short,16254.25,16344.25,0.553701,16343.75,stop,095600,16434.75,-91.0,-1824.68
/tmp/praxis-c1/reimpl/is_trades_V3.csv:361
/tmp/praxis-c1/reimpl/is_trades_V2.csv:489
/tmp/praxis-c1/reimpl/is_trades_V1.csv:457
```

## sha256 list (verbatim)
```
f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3  /tmp/praxis-c1/reimpl/RULES.md
239d3bd48ab8f37e24c2d012e9c26be5157b4581ae5a338ac7202febc70fb70f  /tmp/praxis-c1/reimpl/is_trades_V1.csv
008c68c4661db50529fe7da360270511dcf391838675af11400c5b78a5107a54  /tmp/praxis-c1/reimpl/is_trades_V2.csv
c78204d20d488eaa19076dca60c21153814b9209dd081062bec5f3dda592c2ac  /tmp/praxis-c1/reimpl/is_trades_V3.csv
a6c9c0bd0e7b16baac6d7b26e281ff8ad150a373e1fa31fb3c1a41ac28acb405  /tmp/praxis-c1/reimpl/reimpl.py
c93160d7979b792789b689829881002e1aeb2be4a92c311b1250cf7db05df019  /tmp/praxis-c1/reimpl/run.txt
```

Result: COMPLETED (in-sample re-implementation numbers produced; nothing validated).
