# C1 Opening Gap Fade pre-screen — worker 1 (builder) report

Filer's note (praxis-manager): the harness blocked this worker from writing `.md` report files, so it returned the report body inline. The manager filed the body below as returned. Only this note was added; the standing sentence was moved from the top of the body to the end, and one file path that carries a person's name was replaced by a description. The evidence files it cites are in `/tmp/praxis-c1/`.

Unit `2026-11-14-search-c1-gap-fade`, bead `Praxis_build-vn4`. Repo HEAD 244cfc3, branch main.

## Task
Step A: check whether the data's stamps are ET bar-end times, before computing any trade. Step B: write and run `research/search-loop/c1-gap-fade/screen.py`, which implements `RULES.md` (sha256 f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3, not edited). This is a Mac-side Python pre-screen (D-2026-11-14-A). It was written and run but not checked against NT8. No result here is validated or a contender result.

## Mode: BUILD
Nothing was committed, `git add`-ed or staged. The data file was read in place and not copied. The report file itself could not be written, because the harness blocks `.md` reports from subagents. The manager files this text.

## Timestamp evidence (Step A)
Command: `cd /tmp && python3 -I -B /tmp/praxis-c1/tscheck.py | tee /tmp/praxis-c1/tscheck_out.txt`. Script sha256 is 1c0c3e1d…ce18 and output sha256 is ea1f8bb5…6ebd. Output:
```
file /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
lines 1857362 sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
lines with seconds != 00: 0
weekend-dated bars stamped 09:31-16:00, by weekday: {'Sun': 143, 'Sat': 58}

1. Bar counts per stamp, Mon-Thu dates (winter = Jan+Feb, summer = Jul+Aug, all years)
   Mon-Thu dates with any bar: winter 170, summer 188
stamp  winter  summer
16:55     155     180
16:56     155     180
16:57     155     180
16:58     155     180
16:59     155     180
17:00     155     180
17:01       1       0
17:02       0       0
17:03       0       0
17:04       0       0
17:05       0       0
17:06       0       0
17:07       0       1
17:08       0       0
17:09       0       0
17:10       0       0
17:11       0       0
17:12       0       0
17:13       1       0
17:14       0       0
17:15       0       0
17:16       0       0
17:17       0       0
17:18       0       0
17:19       0       0
17:20       1       0
17:21       1       0
17:22       0       0
17:23       0       0
17:24       0       0
17:25       1       0
17:26       0       1
17:27       0       1
17:28       0       0
17:29       0       0
17:30       0       0
17:31       0       0
17:32       0       0
17:33       0       0
17:34       0       0
17:35       0       0
17:36       0       0
17:37       0       0
17:38       0       0
17:39       0       0
17:40       0       0
17:41       0       0
17:42       0       0
17:43       0       0
17:44       0       0
17:45       0       0
17:46       0       0
17:47       0       0
17:48       0       0
17:49       0       0
17:50       0       0
17:51       0       0
17:52       0       0
17:53       0       0
17:54       0       0
17:55       0       0
17:56       0       0
17:57       0       0
17:58       0       0
17:59       0       0
18:00       1       0
18:01     170     187
18:02     170     187
18:03     170     187
18:04     170     187
18:05     170     187

2. Median volume per stamp, Mon-Thu dates (n = bars at that stamp)
stamp  winter_median (n)  summer_median (n)
09:27     389.5 (166)     279.5 (188)
09:28     550.0 (166)     477.0 (188)
09:29     681.5 (166)     601.5 (188)
09:30     915.0 (166)     727.5 (188)
09:31      5329 (165)    4859.5 (188)
09:32      3862 (165)    3636.5 (188)
09:33      3246 (165)    3237.0 (188)
09:34      2795 (165)    2939.0 (188)
09:35      2796 (165)    2754.5 (188)
15:57      1477 (155)    1476.0 (180)
15:58      1639 (155)    1604.5 (180)
15:59      1907 (155)    1868.0 (180)
16:00      7909 (155)    7463.0 (180)
16:01      3139 (155)    3024.0 (180)
16:02      1331 (155)    1146.5 (180)
16:03       842 (155)     758.5 (180)
08:29     186.0 (166)     165.5 (188)
08:30     208.5 (166)     170.0 (188)
08:31     451.0 (166)     431.5 (188)
08:32     392.0 (166)     338.0 (188)
08:33     366.0 (166)     314.5 (188)

3. First 3 lines with weekday names
20210307 180100;16120.5;16167;16120.5;16154.75;17 -> Sunday
20210307 180200;16164.25;16164.25;16144.75;16144.75;7 -> Sunday
20210307 180300;16145.75;16145.75;16129.75;16134.5;5 -> Sunday
```
What this shows (INFERRED from the output):
- The 17:00-18:00 halt shows as bar-end stamps: bars at 17:00, almost none from 17:01 to 18:00 (7 strays), and resumption at 18:01. It is identical in winter and summer, so the stamps are not a fixed UTC offset.
- The volume jump is at 09:31, not 09:30, and the close spike is at 16:00, with 16:01 lower.
- The 08:31 median (451 / 431.5) is about one tenth of 09:31, which rules out Central time.
- The first bar is Sunday 18:01.

Verdict: not contradicted.

## Implementation notes
- **Arithmetic:** Fractions throughout. gap_pct is an exact Fraction, compared inclusively with Fraction('0.10') and the other bounds. Floats are used only for printing.
- **Session rules:** an RTH bar has a stamp in [093100, 160000]. A trading day is a date with a 093100 bar, and data after 2026-07-17 is dropped at load. The previous trading day is the latest earlier trading day, and the day is skipped if it is more than 4 days back. The first trading day is skipped. PC is the previous trading day's last RTH close. O is the open of the 093100 bar.
- **Bar walk:** from the 093100 bar (entry bar included) to the last RTH bar. If one bar hits both stop and target, the stop is taken. The fills are exactly as in the brief. points = (exit − entry) × side. NQ net = points × 20 − C. MNQ net = points × 2 − 1.90.
- **PF:** sum of positive nets / |sum of negative nets| at the stated commission. Zero-net trades are excluded (there were 0 in every table). If there are no losers, PF is "inf" and qualifies when net > 0. Wins and losses are counted on NQ net at $4.68.
- **Overfitting guard:** `run_period()` asserts that any non-in-sample period runs only for `ALLOWED["selected"]`. That value is set only after selection runs on in-sample stats.
- **Closed-trade DD:** `R._dd_series` from 0, with the peak including 0. Sanity check: 350.0.
- **D6 basis:**
  - `sessions.py` and `report.py` are imported read-only with `-B`.
  - The calendar comes from D6's own file `NQ-continuous-1min.nt8import.txt`, which is present. `cmp` shows it is byte-identical to our file, with the same sha. It gives N 1352, K 17, with 1324-1352 dropped.
  - `window_measures` is reproduced from D6 :697. TIERS, `ceiling()`, `judged()` and `rows_for()` are copied from D6 :589 and :779-830.
  - The Static rows also print D6's "static measure, shown" line, marked not judged.
- **MAE:** a bar-based bound, not an NT8 figure. It runs from the entry bar to the exit bar inclusive (short: max high − entry fill; long: entry fill − min low) and is floored at 0. On a stop-exit bar the adverse price is the stop exit fill. On a target-exit bar the bar's full extreme is counted, which is conservative. Intratrade low = equity before the trade − MAE × $2 − $1.90 (MNQ), or × $20 − $4.68 (NQ).
- **FULL column:** all trades over the full period, measured from 0. EOD rows use max(closed-trade, EOD), and SimF rows add the intratrade-inclusive figure. EOD uses one point per trading day that has a trade; days with no trade leave equity flat, so the DD is the same. JUDGED = PASS only if VS4 passes 17/17 AND FULL < ceiling. The 1 NQ lines use $4.68.
- **Unit check before the run:** `/tmp/praxis-c1/unit_sim.py` (sha256 7f3bc5e5…cfb40) ran on synthetic bars only, with no data file. Output:
```
short target on bar2 | short entry 10019.5 target 093200 exit 10000.5 pts 19 nq468 375.32 mnq 36.1 mae 10.5
short both on bar1 -> stop | short entry 10019.5 stop 093100 exit 10040.5 pts -21 nq468 -424.68 mnq -43.9 mae 21
short no-touch target (low = PC) | short entry 10019.5 time 160000 exit 10008.5 pts 11 nq468 215.32 mnq 20.1 mae 5.5
short stop bar2 | short entry 10019.5 stop 093200 exit 10040.5 pts -21 nq468 -424.68 mnq -43.9 mae 21
long target bar1 | long 9980.5 target 9999.5 19 mae 10.5
long stop bar1 | long 9980.5 stop 9959.5 -21 mae 21
O 10010 gap 0.100000 -> trade
O 10050 gap 0.500000 -> trade
O 10009.75 gap 0.097500 -> no trade
O 10050.25 gap 0.502500 -> no trade
pf 1 inf
```

## Run output (single recorded run, no re-run)
Command: `date -u; cd /Volumes/Sensidine/Praxis.build && python3 -I -B research/search-loop/c1-gap-fade/screen.py | tee /tmp/praxis-c1/screen_run.txt; date -u`. It printed `Sat Nov 14 13:10:23 UTC 2026` before and `Sat Nov 14 13:10:30 UTC 2026` after.

`screen_run.txt` has 131 lines (sha256 b722d67f…af28). Line 1 is the script printing the standing sentence; it is omitted here so the report carries that sentence once (S13). Lines 2-131 are verbatim:
```
C1 Opening Gap Fade PRE-SCREEN (not validated, not checked against NT8). Run at 2026-11-14T13:10:23Z
RULES.md sha256 f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3 MATCH
screen.py sha256 0d7a06d2d27711a7a3c04f3060245fa68c550e2672d2ecd50409830b2e756445
PF definition: sum of positive net trade P&L / |sum of negative net trade P&L| at the stated commission; zero-net trades excluded; 'inf' if no losers.
Wins/losses counted on NQ net at $4.68.
data /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt | lines 1857362 | sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454 MATCH
trading days (date with a 09:31 bar, <= 2026-07-17): 1354, first 2021-03-08 last 2026-07-17
skipped days (no PC): 3
   skip 2021-03-08 - first trading day (no previous)
   skip 2021-09-27 - previous trading day 2021-09-09 is 18 days back
   skip 2026-01-02 - previous trading day 2025-12-12 is 21 days back
weekend-dated trading days (literal rule, kept): [('2021-03-28', 'Sun', 1), ('2025-03-16', 'Sun', 3)]
trading days whose last RTH bar is not 16:00 (time exit at that bar): 49
   [('2021-03-28', '093100'), ('2021-05-31', '130000'), ('2021-07-05', '130000'), ('2021-09-06', '130000'), ('2021-11-25', '130000'), ('2021-11-26', '131500'), ('2022-01-17', '130000'), ('2022-02-21', '130000'), ('2022-05-30', '130000'), ('2022-06-20', '130000'), ('2022-07-04', '130000'), ('2022-09-05', '130000'), ('2022-11-24', '130000'), ('2022-11-25', '131500'), ('2023-01-16', '130000'), ('2023-02-20', '130000'), ('2023-04-05', '140300'), ('2023-05-29', '130000'), ('2023-06-19', '130000'), ('2023-07-03', '131500'), ('2023-07-04', '130000'), ('2023-09-04', '130000'), ('2023-11-23', '130000'), ('2023-11-24', '131500'), ('2024-01-15', '130000'), ('2024-02-19', '130000'), ('2024-05-27', '130000'), ('2024-06-19', '130000'), ('2024-07-03', '131500'), ('2024-07-04', '130000'), ('2024-09-02', '130000'), ('2024-11-28', '130000'), ('2024-11-29', '131500'), ('2024-12-24', '131500'), ('2025-01-20', '130000'), ('2025-02-17', '130000'), ('2025-03-16', '150900'), ('2025-05-26', '130000'), ('2025-06-19', '130000'), ('2025-07-03', '131500'), ('2025-07-04', '130000'), ('2025-09-01', '130000'), ('2025-11-27', '130000'), ('2025-11-28', '131500'), ('2026-01-19', '130000'), ('2026-02-16', '130000'), ('2026-05-25', '130000'), ('2026-06-19', '130000'), ('2026-07-03', '130000')]
sanity _dd_series([+100,-300,+50,-100]) = 350.0 (expect 350)

=== IN-SAMPLE 2021-03-08..2024-12-31, all variants ===
V1 GMIN 0.10 GMAX 0.50 | trades 456 (long 214, short 242) | exits target 216 / stop 221 / time 19 | wins 221 losses 235 zero 0 (at NQ $4.68)
    net NQ @2.96 $-23,059.76 PF 0.9018 | net NQ @4.68 $-23,844.08 PF 0.8986 | net MNQ $-3,037.40 PF 0.8727 | sum points -1085.5
    closed-trade max DD: NQ @2.96 $37,590.56 | NQ @4.68 $38,125.48 | MNQ $4,257.90
    in-sample trades on weekend-dated days: []
V2 GMIN 0.20 GMAX 0.80 | trades 488 (long 225, short 263) | exits target 224 / stop 218 / time 46 | wins 242 losses 246 zero 0 (at NQ $4.68)
    net NQ @2.96 $5,510.52 PF 1.0156 | net NQ @4.68 $4,671.16 PF 1.0132 | net MNQ $-231.70 PF 0.9935 | sum points 347.75
    closed-trade max DD: NQ @2.96 $29,453.16 | NQ @4.68 $29,876.28 | MNQ $3,339.90
    in-sample trades on weekend-dated days: []
V3 GMIN 0.05 GMAX 0.30 | trades 360 (long 165, short 195) | exits target 170 / stop 181 / time 9 | wins 172 losses 188 zero 0 (at NQ $4.68)
    net NQ @2.96 $-12,520.60 PF 0.8926 | net NQ @4.68 $-13,139.80 PF 0.8876 | net MNQ $-1,829.50 PF 0.8471 | sum points -572.75
    closed-trade max DD: NQ @2.96 $17,598.72 | NQ @4.68 $17,911.76 | MNQ $2,170.40
    in-sample trades on weekend-dated days: []

=== SELECTION (in-sample net @4.68 > 0 AND PF @4.68 >= 1.10; highest net @4.68) ===
V1: net @4.68 $-23,844.08, PF @4.68 0.8986 -> does not qualify
V2: net @4.68 $4,671.16, PF @4.68 1.0132 -> does not qualify
V3: net @4.68 $-13,139.80, PF @4.68 0.8876 -> does not qualify
RESULT: V2 -> for the record, not selected (candidate FAILS in-sample)

=== HOLDOUT 2025-01-01..2026-07-17, V2 (for the record, not selected) ===
V2 | trades 160 (long 70, short 90) | exits target 77 / stop 68 / time 15 | wins 82 losses 78 zero 0 (at NQ $4.68)
    net NQ @2.96 $2,341.40 PF 1.0142 | net NQ @4.68 $2,066.20 PF 1.0125 | net MNQ $-22.50 PF 0.9986 | sum points 140.75
    closed-trade max DD: NQ @2.96 $44,912.00 | NQ @4.68 $45,041.00 | MNQ $4,611.50

=== FULL 2021-03-08..2026-07-17, V2 (for the record, not selected) ===
V2 | trades 648 (long 295, short 353) | exits target 301 / stop 286 / time 61 | wins 324 losses 324 zero 0 (at NQ $4.68)
    net NQ @2.96 $7,851.92 PF 1.0151 | net NQ @4.68 $6,737.36 PF 1.0130 | net MNQ $-254.20 PF 0.9951 | sum points 488.5
    closed-trade max DD: NQ @2.96 $44,912.00 | NQ @4.68 $45,041.00 | MNQ $4,611.50

=== D6 four-measure basis, V2, FULL period ===
calendar file (D6's): /Users/admin/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
calendar file sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
N sessions 1352 first 2021-03-08 last 2026-07-17 K 17 dropped [1324, 1352] ['2026-06-08', '2026-07-17']
our full-period trade dates that are not calendar sessions: 0 []
trades after the last OOS session (2026-06-05), outside every window: 10
trades before the first OOS session (2022-03-17), outside every window: 125

--- V2 @ 1 MNQ: per OOS window (dollars) ---
k | OOS dates | trades | net | ct_start | eod_start | ct_carry | eod_carry | WORST4 | mae_start | mae_carry | static_ct | static_mae
1 | 2022-03-17..2022-06-15 | 26 | $143.10 | $812.30 | $812.30 | $812.30 | $812.30 | $812.30 | $870.20 | $870.20 | $29.00 | $109.40
2 | 2022-06-16..2022-09-13 | 35 | $-458.00 | $1,180.10 | $1,180.10 | $1,361.70 | $1,361.70 | $1,361.70 | $1,271.60 | $1,453.20 | $721.50 | $813.00
3 | 2022-09-14..2022-12-09 | 33 | $-27.20 | $646.40 | $646.40 | $1,254.20 | $1,254.20 | $1,254.20 | $671.80 | $1,279.60 | $156.00 | $181.40
4 | 2022-12-12..2023-03-10 | 29 | $-396.60 | $669.60 | $669.60 | $1,522.00 | $1,522.00 | $1,522.00 | $669.60 | $1,577.30 | $396.60 | $451.90
5 | 2023-03-13..2023-06-08 | 27 | $837.70 | $364.70 | $364.70 | $1,522.00 | $1,522.00 | $1,522.00 | $502.10 | $1,653.90 | $0.00 | $131.90
6 | 2023-06-09..2023-09-05 | 34 | $254.40 | $738.30 | $738.30 | $1,012.10 | $1,012.10 | $1,012.10 | $753.40 | $1,027.20 | $327.80 | $342.90
7 | 2023-09-06..2023-12-01 | 34 | $-1,559.10 | $1,658.80 | $1,658.80 | $2,088.70 | $2,088.70 | $2,088.70 | $1,784.20 | $2,214.10 | $1,658.80 | $1,784.20
8 | 2023-12-04..2024-03-01 | 33 | $-436.20 | $1,350.60 | $1,350.60 | $2,826.10 | $2,826.10 | $2,826.10 | $1,432.00 | $2,907.50 | $837.10 | $918.50
9 | 2024-03-04..2024-05-30 | 35 | $399.00 | $914.70 | $914.70 | $3,339.90 | $3,339.90 | $3,339.90 | $950.60 | $3,375.80 | $914.70 | $950.60
10 | 2024-05-31..2024-08-27 | 23 | $129.80 | $1,017.30 | $1,017.30 | $2,819.40 | $2,819.40 | $2,819.40 | $1,090.70 | $2,892.80 | $793.20 | $866.60
11 | 2024-08-28..2024-11-22 | 36 | $543.10 | $1,062.00 | $1,062.00 | $2,064.60 | $2,064.60 | $2,064.60 | $1,092.40 | $2,195.70 | $168.20 | $299.30
12 | 2024-11-25..2025-02-25 | 32 | $-49.80 | $1,380.00 | $1,380.00 | $2,399.70 | $2,399.70 | $2,399.70 | $1,499.40 | $2,519.10 | $1,046.40 | $1,165.80
13 | 2025-02-26..2025-05-27 | 23 | $832.80 | $448.20 | $448.20 | $1,585.00 | $1,585.00 | $1,585.00 | $535.60 | $1,668.40 | $181.90 | $265.30
14 | 2025-05-28..2025-08-22 | 26 | $889.10 | $1,155.90 | $1,155.90 | $1,248.30 | $1,248.30 | $1,248.30 | $1,262.30 | $1,354.70 | $678.00 | $784.40
15 | 2025-08-25..2025-11-20 | 26 | $-842.90 | $1,443.70 | $1,443.70 | $1,443.70 | $1,443.70 | $1,443.70 | $1,443.70 | $1,443.70 | $842.90 | $842.90
16 | 2025-11-21..2026-03-09 | 34 | $-212.60 | $1,461.40 | $1,461.40 | $2,905.10 | $2,905.10 | $2,905.10 | $1,473.10 | $2,916.80 | $1,461.40 | $1,473.10
17 | 2026-03-10..2026-06-05 | 27 | $-2,493.30 | $2,754.00 | $2,754.00 | $4,410.30 | $4,410.30 | $4,410.30 | $2,806.10 | $4,462.40 | $2,754.00 | $2,806.10
MAX over windows: WORST4 $4,410.30 | MAE-incl $4,462.40 | static_ct $2,754.00 | static_mae $2,806.10
FULL period, all trades, 1 MNQ: closed-trade max DD $4,611.50 | end-of-day max DD $4,611.50 | intratrade-inclusive max DD $4,737.90
FULL period, all trades, 1 NQ: closed-trade max DD $45,041.00 | end-of-day max DD $45,041.00 | intratrade-inclusive max DD $46,290.68
MAE note: bar-based bound from the trade's 1-minute bars (entry bar to exit bar inclusive; stop-exit bar uses the stop exit fill), not an NT8 figure.

=== TIER TABLE @ 1 MNQ (D6 method; ceiling = min(3.2% size, 80% limit), strict '<') ===
tier | ceiling | WIN worst window (windows below /17) | VS4 worst window (windows below /17) | FULL | JUDGED
Studio #003 5K [trailing measure = stricter] | $160.00 | $2,754.00 FAIL (0/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Studio #003 5K [static measure, shown, not judged] | $160.00 | static_ct worst $2,754.00 (3/17)
Studio #001 10K [trailing measure = stricter] | $320.00 | $2,754.00 FAIL (0/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Studio #001 10K [static measure, shown, not judged] | $320.00 | static_ct worst $2,754.00 (5/17)
Studio #002 20K [trailing measure = stricter] | $640.00 | $2,754.00 FAIL (2/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Studio #002 20K [static measure, shown, not judged] | $640.00 | static_ct worst $2,754.00 (7/17)
Rapid 25K [Eval EOD] | $800.00 | $2,754.00 FAIL (5/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Rapid 25K [SimF intraday] | $800.00 | $2,806.10 FAIL (5/17) | $4,462.40 FAIL (0/17) | $4,737.90 FAIL | FAIL
Rapid EOD 25K | $800.00 | $2,754.00 FAIL (5/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Builder 25K | $800.00 | $2,754.00 FAIL (5/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Rapid 50K [Eval EOD] | $1,600.00 | $2,754.00 FAIL (15/17) | $4,410.30 FAIL (9/17) | $4,611.50 FAIL | FAIL
Rapid 50K [SimF intraday] | $1,600.00 | $2,806.10 FAIL (15/17) | $4,462.40 FAIL (7/17) | $4,737.90 FAIL | FAIL
Rapid EOD 50K | $1,600.00 | $2,754.00 FAIL (15/17) | $4,410.30 FAIL (9/17) | $4,611.50 FAIL | FAIL
Pro 50K | $1,600.00 | $2,754.00 FAIL (15/17) | $4,410.30 FAIL (9/17) | $4,611.50 FAIL | FAIL
Builder 50K | $1,600.00 | $2,754.00 FAIL (15/17) | $4,410.30 FAIL (9/17) | $4,611.50 FAIL | FAIL
Builder 50K add-on | $1,200.00 | $2,754.00 FAIL (11/17) | $4,410.30 FAIL (2/17) | $4,611.50 FAIL | FAIL
Rapid 100K [Eval EOD] | $2,400.00 | $2,754.00 FAIL (16/17) | $4,410.30 FAIL (12/17) | $4,611.50 FAIL | FAIL
Rapid 100K [SimF intraday] | $2,400.00 | $2,806.10 FAIL (16/17) | $4,462.40 FAIL (11/17) | $4,737.90 FAIL | FAIL
Pro 100K | $2,400.00 | $2,754.00 FAIL (16/17) | $4,410.30 FAIL (12/17) | $4,611.50 FAIL | FAIL
Builder 100K | $2,400.00 | $2,754.00 FAIL (16/17) | $4,410.30 FAIL (12/17) | $4,611.50 FAIL | FAIL
Rapid 150K [Eval EOD] | $3,600.00 | $2,754.00 PASS (17/17) | $4,410.30 FAIL (16/17) | $4,611.50 FAIL | FAIL
Rapid 150K [SimF intraday] | $3,600.00 | $2,806.10 PASS (17/17) | $4,462.40 FAIL (16/17) | $4,737.90 FAIL | FAIL
Pro 150K | $3,600.00 | $2,754.00 PASS (17/17) | $4,410.30 FAIL (16/17) | $4,611.50 FAIL | FAIL
Builder 150K | $3,600.00 | $2,754.00 PASS (17/17) | $4,410.30 FAIL (16/17) | $4,611.50 FAIL | FAIL
1 MNQ JUDGED PASS rows: NONE

=== 1 NQ (@ $4.68) JUDGED, one line per tier row ===
Studio #003 5K [trailing measure = stricter] | ceiling $160.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Studio #001 10K [trailing measure = stricter] | ceiling $320.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Studio #002 20K [trailing measure = stricter] | ceiling $640.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 25K [Eval EOD] | ceiling $800.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 25K [SimF intraday] | ceiling $800.00 | VS4 worst $43,607.28 (0/17) | FULL $46,290.68 | JUDGED FAIL
Rapid EOD 25K | ceiling $800.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Builder 25K | ceiling $800.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 50K [Eval EOD] | ceiling $1,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 50K [SimF intraday] | ceiling $1,600.00 | VS4 worst $43,607.28 (0/17) | FULL $46,290.68 | JUDGED FAIL
Rapid EOD 50K | ceiling $1,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Pro 50K | ceiling $1,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Builder 50K | ceiling $1,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Builder 50K add-on | ceiling $1,200.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 100K [Eval EOD] | ceiling $2,400.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 100K [SimF intraday] | ceiling $2,400.00 | VS4 worst $43,607.28 (0/17) | FULL $46,290.68 | JUDGED FAIL
Pro 100K | ceiling $2,400.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Builder 100K | ceiling $2,400.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 150K [Eval EOD] | ceiling $3,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Rapid 150K [SimF intraday] | ceiling $3,600.00 | VS4 worst $43,607.28 (0/17) | FULL $46,290.68 | JUDGED FAIL
Pro 150K | ceiling $3,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL
Builder 150K | ceiling $3,600.00 | VS4 worst $43,143.56 (0/17) | FULL $45,041.00 | JUDGED FAIL

wrote /Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/summary.json and /Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/trades_V2_full.csv
```

## Post-run checks
The full pasted output is in `/tmp/praxis-c1/post_out.txt`, from `bash /tmp/praxis-c1/post.sh`. Key lines, verbatim:
```
$ git status --short scripts/wf
$ find scripts/wf -name __pycache__ -newer research/search-loop/c1-gap-fade/RULES.md
$ find research -name __pycache__
$ git status --short research/ && git diff --cached --stat | tail -1
?? research/
 1 file changed, 0 insertions(+), 0 deletions(-)
$ wc -c research/search-loop/c1-gap-fade/out/trades_V2_full.csv
   67969 research/search-loop/c1-gap-fade/out/trades_V2_full.csv
```
- The one staged file is the png that was already staged at session start (an evidence png under `docs/reports/evidence/`; path withheld by the filer). It is not from this unit.
- My first try at this listing exited 1. The cause was a zsh no-match on a trailing `docs/reports/2026-11-14-search-c1*` glob; the same read-only commands then ran cleanly via post.sh.
- One correction: a scratch `python3 -c` gap calculation I ran used a made-up O for 2025-03-17. That output is void. 2025-03-17 has no RTH bars, and the real check below uses 2025-03-18's actual open.

## Files written, with sha256
| Path | sha256 |
|---|---|
| research/search-loop/c1-gap-fade/screen.py | 0d7a06d2d27711a7a3c04f3060245fa68c550e2672d2ecd50409830b2e756445 |
| research/search-loop/c1-gap-fade/out/summary.json | 9aa4e68ff9bb8a9350f118e1f96a60b8657c3bdca23177e9b49f2e464a5e99d4 |
| research/search-loop/c1-gap-fade/out/trades_V2_full.csv (67969 B, 648 rows) | 6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045 |
| /tmp/praxis-c1/builder_is_trades_V1.csv (456) | 0dae9abe991cd78ef64ba507b55fd845bd3e9dda1f380151da8cd56d9e60cb00 |
| /tmp/praxis-c1/builder_is_trades_V2.csv (488) | 985d5ec343053bbd8bdfd9b4b083b75168edf9e570b633c93c16fefd1287928e |
| /tmp/praxis-c1/builder_is_trades_V3.csv (360) | 4de91f644bcac811d73b8ad50e0aaecc3651dd2299a44334035bf19ddb580a75 |
| /tmp/praxis-c1/screen_run.txt | b722d67f0447364aa99603b76c6e686cf6d9bee87fa83b431256474b2cb2af28 |

All repo files are untracked and not staged. MANIFEST.md was not updated, because it is outside the brief's scope.

## Ambiguities and how I resolved them
1. **Weekend stray bars count as "trading days" under the literal rule.** The run kept 2021-03-28 and 2025-03-16, both Sundays with stale one-price bars. No trade falls on either Sunday. Effect on the next day (output in `/tmp/praxis-c1/weekend_out.txt`):
   - **2021-03-29:** PC becomes the Sunday stray close, 16375 instead of Friday's 16:00 close of 16378. The gap is −0.108397% instead of −0.126694%. V1 and V3 trade either way, but with a different PC; under the literal rule it is a stop at −$379.68. V2 does not trade it either way.
   - **2025-03-18:** PC becomes 21107.5 instead of 21145.75. The gap is 0.120810% instead of −0.060296%. V2 does not trade it either way.
   - **Result:** V2's holdout and full figures are the same under both readings. That selection is unaffected is INFERRED (one trade per variant cannot lift a PF of about 0.89 to 1.10); the weekday-only alternative was not run.
   - The D6 calendar is Mon-Fri, so its windows are unaffected.
2. **Early closes:** 49 days end before 16:00. PC and the time exit use the last RTH bar of the day.
3. **Gap skips:** 2021-09-27 (18 days back) and 2026-01-02 (21 days back) are skipped. They look like data gaps (INFERRED).
4. **MAE on a target-exit bar:** the bar's full extreme is counted, which is conservative.
5. **EOD drawdown point set:** only trading days with a trade. This does not change the figure.
6. **Ties and PF = inf:** neither case arose.

Result: PASS (build run once; outputs written; report body returned inline because the file write was blocked).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Cure 1 (S1), appended 2026-11-14 by the manager

### (a) supports worker1.md :330-:331 (alternative-reading figures)

```
$ cat /tmp/praxis-c1/weekend_out.txt
$ awk -F'[ ;]' '($1=="20210328"||$1=="20250316") && $2>="093100" && $2<="160000"' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
20210328 093100;16375;16375;16375;16375;1
20250316 093100;21107.5;21107.5;21107.5;21107.5;1
20250316 144100;21107.5;21107.5;21107.5;21107.5;1
20250316 150900;21107.5;21107.5;21107.5;21107.5;2
$ /usr/bin/grep -E '^(20210326|20250314) 160000' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
20210326 160000;16357.5;16391;16357.5;16378;6771
20250314 160000;21171.25;21172.75;21143.75;21145.75;14632
$ awk -F'[ ;]' '$1=="20250317" && $2>="093100" && $2<="160000"' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" | wc -l
       0
$ /usr/bin/grep -E '^(20210329|20250318) 093100' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
20210329 093100;16357.25;16365.25;16349.25;16365.25;2665
20250318 093100;21133;21135.25;21092.75;21095.25;3907
$ /usr/bin/grep -E '^(2021-03-29|2025-03-18),' /Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/trades_V2_full.csv /tmp/praxis-c1/builder_is_trades_V1.csv /tmp/praxis-c1/builder_is_trades_V2.csv /tmp/praxis-c1/builder_is_trades_V3.csv
/tmp/praxis-c1/builder_is_trades_V1.csv:2021-03-29,long,16375,16357.25,-0.108397,16357.75,stop,093300,16339,-18.75,-377.96,-379.68,-39.4,18.75
/tmp/praxis-c1/builder_is_trades_V3.csv:2021-03-29,long,16375,16357.25,-0.108397,16357.75,stop,093300,16339,-18.75,-377.96,-379.68,-39.4,18.75
$ python3 -I -B -c 'from fractions import Fraction as F
for lab,O,pc in (("2021-03-29 literal PC (Sun 03-28 stray 09:31 close)","16357.25","16375"),("2021-03-29 alt PC (Fri 03-26 16:00 close)","16357.25","16378"),("2025-03-18 literal PC (Sun 03-16 stray 15:09 close)","21133","21107.5"),("2025-03-18 alt PC (Fri 03-14 16:00 close)","21133","21145.75")):
    print(lab, "gap_pct %.6f" % float((F(O)-F(pc))/F(pc)*100))'
2021-03-29 literal PC (Sun 03-28 stray 09:31 close) gap_pct -0.108397
2021-03-29 alt PC (Fri 03-26 16:00 close) gap_pct -0.126694
2025-03-18 literal PC (Sun 03-16 stray 15:09 close) gap_pct 0.120810
2025-03-18 alt PC (Fri 03-14 16:00 close) gap_pct -0.060296
$ bash /tmp/praxis-c1/weekend.sh > /tmp/praxis-c1/cure1/weekend_rerun.txt; cmp /tmp/praxis-c1/cure1/weekend_rerun.txt /tmp/praxis-c1/weekend_out.txt; echo cmp_exit=$?
cmp_exit=0
```

### (c) supports worker1.md :143 (TIERS, `ceiling()`, `judged()`, `rows_for()` copied from D6)

```
$ sed -n '588,603p;779,792p' docs/reports/2026-11-09-d6-drawdown-check-manager.md
# ---------- tier rows: WF spec HEAD :115-130; A4 = below min(3.2% size, 80% limit) ----------
TIERS = [("Studio #003 5K", 5000, 250, "Static"), ("Studio #001 10K", 10000, 500, "Static"),
         ("Studio #002 20K", 20000, 1000, "Static"),
         ("Rapid 25K", 25000, 1000, "Eval EOD / SimF intraday"), ("Rapid EOD 25K", 25000, 1000, "EOD"),
         ("Builder 25K", 25000, 1000, "EOD"),
         ("Rapid 50K", 50000, 2000, "Eval EOD / SimF intraday"), ("Rapid EOD 50K", 50000, 2000, "EOD"),
         ("Pro 50K", 50000, 2000, "EOD"), ("Builder 50K", 50000, 2000, "EOD"),
         ("Builder 50K add-on", 50000, 1500, "EOD"),
         ("Rapid 100K", 100000, 3000, "Eval EOD / SimF intraday"), ("Pro 100K", 100000, 3000, "EOD"),
         ("Builder 100K", 100000, 3000, "EOD"),
         ("Rapid 150K", 150000, 4500, "Eval EOD / SimF intraday"), ("Pro 150K", 150000, 4500, "EOD"),
         ("Builder 150K", 150000, 4500, "EOD")]


def ceiling(size, limit):
    return min(Fraction(32, 1000) * size, Fraction(8, 10) * limit)
def judged(r, kind, meas):
    if meas == "WIN":
        v = max(r["ct_start"], r["eod_start"])
        return max(v, r["mae_start"]) if kind == "SimF" else v
    v = r["worst"]
    return max(v, r["mae_worst"]) if kind == "SimF" else v


def rows_for(typ):
    if "SimF" in typ:
        return [(" [Eval EOD]", "EOD"), (" [SimF intraday]", "SimF")]
    if typ == "Static":
        return [(" [trailing measure = stricter]", "EOD")]
    return [("", "EOD")]
$ sed -n '51,82p' research/search-loop/c1-gap-fade/screen.py
# D6 TIERS (D6 report Appendix B :589), ceiling() and rows_for() verbatim in logic.
TIERS = [("Studio #003 5K", 5000, 250, "Static"), ("Studio #001 10K", 10000, 500, "Static"),
         ("Studio #002 20K", 20000, 1000, "Static"),
         ("Rapid 25K", 25000, 1000, "Eval EOD / SimF intraday"), ("Rapid EOD 25K", 25000, 1000, "EOD"),
         ("Builder 25K", 25000, 1000, "EOD"),
         ("Rapid 50K", 50000, 2000, "Eval EOD / SimF intraday"), ("Rapid EOD 50K", 50000, 2000, "EOD"),
         ("Pro 50K", 50000, 2000, "EOD"), ("Builder 50K", 50000, 2000, "EOD"),
         ("Builder 50K add-on", 50000, 1500, "EOD"),
         ("Rapid 100K", 100000, 3000, "Eval EOD / SimF intraday"), ("Pro 100K", 100000, 3000, "EOD"),
         ("Builder 100K", 100000, 3000, "EOD"),
         ("Rapid 150K", 150000, 4500, "Eval EOD / SimF intraday"), ("Pro 150K", 150000, 4500, "EOD"),
         ("Builder 150K", 150000, 4500, "EOD")]


def ceiling(size, limit):
    return min(F(32, 1000) * size, F(8, 10) * limit)


def rows_for(typ):
    if "SimF" in typ:
        return [(" [Eval EOD]", "EOD"), (" [SimF intraday]", "SimF")]
    if typ == "Static":
        return [(" [trailing measure = stricter]", "EOD")]
    return [("", "EOD")]


def judged(r, kind, meas):
    if meas == "WIN":
        v = max(r["ct_start"], r["eod_start"])
        return max(v, r["mae_start"]) if kind == "SimF" else v
    v = r["worst"]
    return max(v, r["mae_worst"]) if kind == "SimF" else v
```

```
$ diff <(sed -n '589,599p' docs/reports/2026-11-09-d6-drawdown-check-manager.md) <(sed -n '52,62p' research/search-loop/c1-gap-fade/screen.py); echo TIERS_diff_exit=$?
TIERS_diff_exit=0
$ diff <(sed -n '602,603p' docs/reports/2026-11-09-d6-drawdown-check-manager.md) <(sed -n '65,66p' research/search-loop/c1-gap-fade/screen.py); echo ceiling_diff_exit=$?
2c2
<     return min(Fraction(32, 1000) * size, Fraction(8, 10) * limit)
---
>     return min(F(32, 1000) * size, F(8, 10) * limit)
ceiling_diff_exit=1
$ diff <(sed -n '779,784p' docs/reports/2026-11-09-d6-drawdown-check-manager.md) <(sed -n '77,82p' research/search-loop/c1-gap-fade/screen.py); echo judged_diff_exit=$?
judged_diff_exit=0
$ diff <(sed -n '787,792p' docs/reports/2026-11-09-d6-drawdown-check-manager.md) <(sed -n '69,74p' research/search-loop/c1-gap-fade/screen.py); echo rows_for_diff_exit=$?
rows_for_diff_exit=0
```

not byte-identical; the pasted diff shows the differences

### (f) supports worker1.md :312 (first listing try exited 1)

Claim at worker1.md :312 withdrawn: the output was not kept.
