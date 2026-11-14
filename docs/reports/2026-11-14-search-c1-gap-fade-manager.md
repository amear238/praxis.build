# C1 Opening Gap Fade pre-screen — manager report

Unit `2026-11-14-search-c1-gap-fade`, bead `Praxis_build-vn4`. HEAD = origin/main = 244cfc3. Strategy search loop candidate 1. Scope: DECISION_LOG row 2026-11-14T13:04:00Z (master under D-2026-11-08-D D1).

**Result: PASS** (the unit is complete: rules and entry written first, screen written and run, cold re-implementation matches, bar scored, everything staged in the temp index).

**Verdict: PRE-SCREEN FAIL.** Bar items 3 and 4 fail. Item 2 is NOT MET by construction (no NT8 run). Also, no variant passed the in-sample selection, so the candidate FAILS in-sample. V2 is shown "for the record, not selected". This is a Mac-side Python pre-screen, written and run. It is not validated against NT8, and nothing here is a contender result.

## Task
Write C1's rules and the D-2026-11-14-A entry before any test. Have a builder check the data's timestamps, then write and run `screen.py`. Have a cold worker re-implement the in-sample figures from the rules alone. Compare the two, score the candidate against the contender bar (D-2026-11-13-E, handoff :73-:81), and stage everything in `/tmp/praxis-c1/idx`.

## Rubric criteria addressed
S1 (pasted output), S2 (levels: specified / written / run; not validated against NT8), S4 (D-2026-11-14-A written before the screen ran, timestamps below), S6 (cross-block section), S13 (one standalone sentence per report and in the entry).

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| worker 1 | BUILD | Checked the timestamps (not contradicted). Wrote and ran `screen.py` once. Report body returned inline (the harness blocks subagent `.md` writes) and filed by the manager as `-worker1.md`. |
| worker 2 | ADVERSARIAL (cold re-implementation) | Had RULES.md and the data path only. Wrote `/tmp/praxis-c1/reimpl/reimpl.py` and computed in-sample V1-V3. Matches worker 1 on all 1,304 trades, field by field. Body filed by the manager as `-worker2.md`. |

## Timeline (pasted `date -u` and `ls -lT`)
```
Sat Nov 14 13:04:14 UTC 2026        <- before step 1
Sat Nov 14 13:06:00 UTC 2026        <- after RULES.md and the entry file were written; shas below
Sat Nov 14 13:10:23 UTC 2026        <- worker 1 screen.py run start (its pasted date -u)
Sat Nov 14 13:10:30 UTC 2026        <- worker 1 run end
Sat Nov 14 13:15:35 UTC 2026        <- before step 4
Sat Nov 14 13:16:46 UTC 2026        <- worker 2 run start (its pasted date -u)
Sat Nov 14 13:16:50 UTC 2026        <- worker 2 run end
```
File order. Local time is EST, UTC−5: `date` printed `Sat Nov 14 08:20:04 EST 2026` at the same moment `date -u` printed `Sat Nov 14 13:20:04 UTC 2026`.
```
-rw-r--r--@ 1 admin  staff   1365 Nov 14 08:05:58 2026 research/search-loop/c1-gap-fade/D-2026-11-14-A.entry.md
-rw-r--r--@ 1 admin  staff   4075 Nov 14 08:05:48 2026 research/search-loop/c1-gap-fade/RULES.md
-rw-r--r--@ 1 admin  staff  26500 Nov 14 08:10:10 2026 research/search-loop/c1-gap-fade/screen.py
```
So RULES.md was written at 13:05:48Z and the entry at 13:05:58Z. screen.py was saved at 13:10:10Z and first run at 13:10:23Z.

## Rules sha and entry sha
```
f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3  RULES.md
a7c4b74aeaa4610c1cc86af11561bc88ec55f0dba2c8c7ffe1aef09b22e56a82  D-2026-11-14-A.entry.md
```
The fill model was stated in writing before the run, in RULES.md "Entry" and "Exits": 0.5 points (2 ticks) of slippage on every fill, the stop taken first when one bar hits both stop and target, and the time exit at the last RTH bar.

**Data file** (read in place, not copied into the repo):
```
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
 1857362
20210307 180100;16120.5;16167;16120.5;16154.75;17
20260720 112700;29005.5;29020.75;29003.5;29016;308
```

**MNQ commission.** D6 does define it. RULES.md quotes D6 :50-52: "MNQ net = points × $2 − $1.90 (cost model v1.2.0)". The NQ ÷ 10 fallback was therefore not used. `config/backtest-cost-model.json` has `"commission_round_turn_usd_mnq": 1.90`.

## Timestamp evidence (worker 1, `/tmp/praxis-c1/tscheck_out.txt`, excerpt; full output in `-worker1.md`)
```
lines with seconds != 00: 0
stamp  winter  summer
17:00     155     180
17:01       1       0
18:00       1       0
18:01     170     187
stamp  winter_median (n)  summer_median (n)
09:30     915.0 (166)     727.5 (188)
09:31      5329 (165)    4859.5 (188)
16:00      7909 (155)    7463.0 (180)
16:01      3139 (155)    3024.0 (180)
08:31     451.0 (166)     431.5 (188)
20210307 180100;16120.5;16167;16120.5;16154.75;17 -> Sunday
```
Every stamp from 17:02 to 17:59 has at most 1 bar. That is 7 strays in total across both seasons, listed in `-worker1.md`. The pattern is the same in winter and summer. The volume jump is at the 09:31 stamp, which fits ET bar-end stamps; the master's reading is not contradicted. The ET reading is INFERRED from the CME break and the open/close volume spikes. No external timezone source was checked.

## In-sample, every variant (2021-03-08 to 2024-12-31; from `/tmp/praxis-c1/screen_run.txt`)
```
V1 GMIN 0.10 GMAX 0.50 | trades 456 (long 214, short 242) | exits target 216 / stop 221 / time 19 | wins 221 losses 235 zero 0 (at NQ $4.68)
    net NQ @2.96 $-23,059.76 PF 0.9018 | net NQ @4.68 $-23,844.08 PF 0.8986 | net MNQ $-3,037.40 PF 0.8727 | sum points -1085.5
    closed-trade max DD: NQ @2.96 $37,590.56 | NQ @4.68 $38,125.48 | MNQ $4,257.90
V2 GMIN 0.20 GMAX 0.80 | trades 488 (long 225, short 263) | exits target 224 / stop 218 / time 46 | wins 242 losses 246 zero 0 (at NQ $4.68)
    net NQ @2.96 $5,510.52 PF 1.0156 | net NQ @4.68 $4,671.16 PF 1.0132 | net MNQ $-231.70 PF 0.9935 | sum points 347.75
    closed-trade max DD: NQ @2.96 $29,453.16 | NQ @4.68 $29,876.28 | MNQ $3,339.90
V3 GMIN 0.05 GMAX 0.30 | trades 360 (long 165, short 195) | exits target 170 / stop 181 / time 9 | wins 172 losses 188 zero 0 (at NQ $4.68)
    net NQ @2.96 $-12,520.60 PF 0.8926 | net NQ @4.68 $-13,139.80 PF 0.8876 | net MNQ $-1,829.50 PF 0.8471 | sum points -572.75
    closed-trade max DD: NQ @2.96 $17,598.72 | NQ @4.68 $17,911.76 | MNQ $2,170.40
```
PF is the sum of positive per-trade nets divided by the absolute sum of negative per-trade nets, at the stated commission. Both workers used this definition independently.

## Selection
```
V1: net @4.68 $-23,844.08, PF @4.68 0.8986 -> does not qualify
V2: net @4.68 $4,671.16, PF @4.68 1.0132 -> does not qualify
V3: net @4.68 $-13,139.80, PF @4.68 0.8876 -> does not qualify
RESULT: V2 -> for the record, not selected (candidate FAILS in-sample)
```
All three variants are logged, including the failures (D-2026-11-13-E guard). The holdout and the full period were run once, for V2 only. The guard is enforced in code, and its negative test is below.

## Holdout and full, V2 (for the record, not selected), both commissions
```
=== HOLDOUT 2025-01-01..2026-07-17, V2 (for the record, not selected) ===
V2 | trades 160 (long 70, short 90) | exits target 77 / stop 68 / time 15 | wins 82 losses 78 zero 0 (at NQ $4.68)
    net NQ @2.96 $2,341.40 PF 1.0142 | net NQ @4.68 $2,066.20 PF 1.0125 | net MNQ $-22.50 PF 0.9986 | sum points 140.75
    closed-trade max DD: NQ @2.96 $44,912.00 | NQ @4.68 $45,041.00 | MNQ $4,611.50
=== FULL 2021-03-08..2026-07-17, V2 (for the record, not selected) ===
V2 | trades 648 (long 295, short 353) | exits target 301 / stop 286 / time 61 | wins 324 losses 324 zero 0 (at NQ $4.68)
    net NQ @2.96 $7,851.92 PF 1.0151 | net NQ @4.68 $6,737.36 PF 1.0130 | net MNQ $-254.20 PF 0.9951 | sum points 488.5
    closed-trade max DD: NQ @2.96 $44,912.00 | NQ @4.68 $45,041.00 | MNQ $4,611.50
```
I recomputed these myself from `out/trades_V2_full.csv` with `/tmp/praxis-c1/mgr/fullchk.py`, which does not use screen.py's code:
```
full rows 648 | in-sample part equals builder IS V2 list: True
HOLDOUT NQ@2.96 trades 160 net 2341.40 PF 1.0142 closed-trade maxDD 44912.00
HOLDOUT NQ@4.68 trades 160 net 2066.20 PF 1.0125 closed-trade maxDD 45041.00
HOLDOUT MNQ@1.90 trades 160 net -22.50 PF 0.9986 closed-trade maxDD 4611.50
FULL NQ@2.96 trades 648 net 7851.92 PF 1.0151 closed-trade maxDD 44912.00
FULL NQ@4.68 trades 648 net 6737.36 PF 1.0130 closed-trade maxDD 45041.00
FULL MNQ@1.90 trades 648 net -254.20 PF 0.9951 closed-trade maxDD 4611.50
```

## D6-basis drawdown at 1 MNQ, per tier (V2, full period; screen.py output)
Method, quoted in RULES.md: D6 :19-23 and :54. The calendar comes from D6's own data file. Worker 1 found it byte-identical to ours (same sha, 307c5e8a…6b16e454). N = 1,352 and K = 17. 125 trades fall before the first OOS window and 10 after the last; the FULL column covers them.
```
MAX over windows: WORST4 $4,410.30 | MAE-incl $4,462.40 | static_ct $2,754.00 | static_mae $2,806.10
FULL period, all trades, 1 MNQ: closed-trade max DD $4,611.50 | end-of-day max DD $4,611.50 | intratrade-inclusive max DD $4,737.90
tier | ceiling | WIN worst window (windows below /17) | VS4 worst window (windows below /17) | FULL | JUDGED
Studio #003 5K [trailing measure = stricter] | $160.00 | $2,754.00 FAIL (0/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Studio #001 10K [trailing measure = stricter] | $320.00 | $2,754.00 FAIL (0/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
Studio #002 20K [trailing measure = stricter] | $640.00 | $2,754.00 FAIL (2/17) | $4,410.30 FAIL (0/17) | $4,611.50 FAIL | FAIL
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
```
- **Judging rule (the manager's decision under D1).** JUDGED = PASS only if VS4 passes all 17 windows AND the full-period figure is below the ceiling. VS4 is D6's committed measure (D6 Decision 5). FULL is what RULES.md adds: closed-trade peak to trough over all trades. Only the within-window WIN measure passes, and only at the four 150K rows. If item 3 were judged on WIN alone it would pass at 150K. The committed measure, VS4, fails every row.
- **Static rows.** The D6 "static measure, shown" lines are in `-worker1.md`; they are not judged, as in D6.
- **Intratrade measure.** The MAE behind it is a bound built from the trade's own 1-minute bars. It is not NT8's MAE column, which does not exist for this candidate.
- **Re-implementation scope.** The D6 window, EOD and MAE measures were computed by worker 1 only. Worker 2 did not re-implement them; it re-implemented closed-trade drawdown, which matched. My `fullchk.py` reproduces the full-period closed-trade $4,611.50 independently.

## Re-implementation comparison (in-sample, `/tmp/praxis-c1/mgr/cmp.py`)
Worker 2's own figures (from its run.txt) for V1 / V2 / V3:
- Trades: 456 / 488 / 360.
- Net at $4.68: -23844.08 / 4671.16 / -13139.80.
- Closed-trade max DD at NQ $4.68: 38125.48 / 29876.28 / 17911.76.
- Closed-trade max DD at 1 MNQ: 4257.90 / 3339.90 / 2170.40.

These equal worker 1's figures exactly. Per-trade diff on date, side, PC, O, entry_fill, exit_kind, exit_stamp, exit_fill, points and nq_net_468, compared as exact Fractions:
```
variant | builder trades | reimpl trades | rows differing | sum|net diff| @4.68 | builder net @4.68 | reimpl net @4.68 | sum net diff
V1 | 456 | 456 | 0 | 0.00 | -23844.08 | -23844.08 | 0.00
V2 | 488 | 488 | 0 | 0.00 | 4671.16 | 4671.16 | 0.00
V3 | 360 | 360 | 0 | 0.00 | -13139.80 | -13139.80 | 0.00
```
Trade counts match exactly, and the summed net difference is $0.00, inside the $0.01-per-trade tolerance. No fix cycle was needed.

## Bar scoring (contender bar, D-2026-11-13-E, handoff :73-:81), on the $4.68 numbers
| Item | Holds? | Evidence |
|---|---|---|
| 1. Fully mechanical rules | HOLDS | RULES.md: no step needs judgment. Two implementations working from the text alone gave identical trade lists. |
| 2. Full five-year backtest at $4.68 | NOT MET (by construction) | Pre-screen only; no NT8 run (D-2026-11-14-A). |
| 3. Drawdown gate at 1 MNQ, at least one tier | FAILS | JUDGED PASS rows: NONE. The best tier is 150K, ceiling $3,600: VS4 worst window is $4,410.30 and FULL is $4,611.50. |
| 4. Money over full period, PF >= 1.10, money in holdout | FAILS | Full NQ @4.68 is +$6,737.36, but PF is 1.0130 < 1.10. Holdout NQ @4.68 is +$2,066.20 (PF 1.0125). At 1 MNQ, both full (-$254.20) and holdout (-$22.50) lose money. |
| 5. At least 200 trades over five years | HOLDS | 648 trades (V2, full). |
| 6. Different way of making money | N/A | No contenders exist yet, so there is nothing to compare against. |
| 7. Independent auditor | NOT MINE | This is for the master's auditor; I did not grade it. |

**Verdict: PRE-SCREEN FAIL** (failing items: 3 and 4). The candidate also fails the in-sample selection, and item 2 is unmet by construction. It does not earn an NT8 run on this evidence.

## Verification evidence (manager re-runs, pasted)
**Re-run of screen.py.** I ran `python3 -I -B research/search-loop/c1-gap-fade/screen.py > /tmp/praxis-c1/mgr_rerun.txt` and diffed it against worker 1's recorded run, excluding the header line:
```
exit=0
RERUN_IDENTICAL_EXCEPT_HEADER
2c2
< C1 Opening Gap Fade PRE-SCREEN (not validated, not checked against NT8). Run at 2026-11-14T13:10:23Z
---
> C1 Opening Gap Fade PRE-SCREEN (not validated, not checked against NT8). Run at 2026-11-14T13:16:01Z
```
The output is deterministic. It was the same frozen V2 computation, not a new trial and not a new variant. Side effect: screen.py rewrites `out/summary.json` on every run, so the staged summary.json is from my re-run. Its `run_timestamp_utc` is `2026-11-14T13:16:01Z`, and its sha changed from 9aa4e68f…5e99d4 (worker 1's table) to 71cd0733…c9a9a8. `trades_V2_full.csv` is unchanged (6d07b245…352045).

**Negative test, overfitting guard** (`/tmp/praxis-c1/mgr/neg.py`, which imports screen.py and calls `run_period`):
```
selected=None run V1 on holdout -> BLOCKED: overfitting guard: V1 not allowed on holdout
selected=None run V2 on full -> BLOCKED: overfitting guard: V2 not allowed on full
selected=V2 run V1 on holdout -> BLOCKED: overfitting guard: V1 not allowed on holdout
selected=V2 run V3 on full -> BLOCKED: overfitting guard: V3 not allowed on full
selected=V2 run V2 on holdout -> RAN (no block)
selected=None run V1 on in-sample -> RAN (no block)
```
The guard is an `assert`, so `python3 -O` would strip it. It holds only under the documented `-I -B` run line.

**Spot check of three holdout trades against raw bars** (`/tmp/praxis-c1/mgr/spot.sh`):
```
20241231 160000;22655.5;22675.75;22655.25;22660.75;8405       <- PC 22660.75 for 2025-01-02 (Jan 1 has no 09:31 bar)
20250102 093600;22707.25;22715.5;22663.5;22665.5;4027         <- low 22663.5 > 22660.5: no target yet
20250102 093700;22665.5;22682.5;22652.5;22658.25;3889         <- low <= 22660.5: target; CSV exit 093700 at 22661.25
20250103 094000;22806;22857.5;22800.75;22853.5;4552           <- high 22857.5 < stop 22858
20250103 094100;22851.75;22862;22837.5;22851.25;2958          <- first high >= 22858: stop; CSV exit 094100 at 22858.5
20250120 130000;23128;23129.25;23120.25;23123;127             <- last RTH bar (early close); CSV time exit 23123.5
minlow 23060 maxhigh 23218.75                                  <- 2025-01-20: no target (needs <= 23040.75), no stop (23286.5); CSV mae 55.5 = 23218.75 - 23163.25
```

**Repo hygiene** (worker 1's post.sh): `git status --short scripts/wf` printed nothing, and `find scripts/wf -name __pycache__ -newer RULES.md` printed nothing.

## Adversarial findings
1. **Weekend stray bars become trading days under the literal rule.** RULES.md defines a trading day as "a date with a 09:31-stamped bar". Two Sundays carry one-price stray 09:31 bars (2021-03-28 and 2025-03-16), so they count. As a result, 2021-03-29's PC is 16375, the Sunday stray close, instead of Friday's 16378. That changes one V1 trade and one V3 trade, both in-sample (a stop, −$379.68 each). It does not change V2 or the selection: the highest-PF variant is at 1.0132, against 1.10. Both workers applied the literal rule independently. I did not change the rule.
2. **Truncated data on 2023-04-05** (last bar 14:03). 2023-04-06's PC comes from the 14:03 close, and all three variants trade that day. This is the literal rule, applied the same way by both workers. It is a data artifact, carried as a limitation.
3. **Two skipped days with data gaps:** 2021-09-27 (previous trading day 18 days back) and 2026-01-02 (21 days back). Both are skipped by the 4-day rule.
4. **Citation correction.** The master's DECISION_LOG row 2026-11-14T13:04:00Z cites "vm-queue results :52" for the `satemplate` OK. That file has 44 lines (`wc -l` → 44), and the text is at :42 ("set by hand or via the bridge's `satemplate` command (needs Amear's OK)"). D-2026-11-14-A cites :42.
5. **The D-2026-11-14-A entry is written but not committed.** Its file's mtime (13:05:58Z) is before the first screen run (13:10:23Z). The DECISION_LOG row asks for it to be committed before the run, and I cannot commit (hook-blocked). The master decides whether the file-timestamp evidence meets S4's "written before the work".

## S6 cross-block check
- **Block 2 (walk-forward).** No walk-forward file was edited. `scripts/wf/sessions.py` and `report.py` were imported read-only, with `-B`, and `git status --short scripts/wf` is empty. The pre-screen's D6-basis numbers are not Block 2 gate results, and no Block 2 gate is claimed.
- **Block 3 (breakers).** No breaker was touched. There is no daily-loss-cap simulation.
- **Blocks 4-5 (paper / live).** Nothing was touched: no NinjaScript, n8n, monitor or VM action.
- **F3 / F4.** F3 stays FROZEN and is not claimed cleared. This candidate is not bead `4uu`. The F4 tier sizes are D6's TIERS (the WF spec's 2026-11-05 capture); MFFU's pages were not re-read (no network).
- **Bead `ckh`.** Not touched. Its parked D-2026-11-12-B text in the working-tree DECISIONS.md was not read as authority and was not staged. The staged DECISIONS.md blob is `HEAD:DECISIONS.md` plus the entry only.

## Fill model and limitations
- **Bars.** Price is seen only as 1-minute bars (open, high, low, close). There is no intrabar order: within one bar, the code cannot tell whether the stop or the target traded first.
- **Stop-first rule.** When one bar touches both the stop and the target, the stop is taken. That is pessimistic for that bar, but it is a rule, not an observation.
- **Slippage.** 0.5 points (2 ticks) against the trader on every fill: entry, target, stop and time exit. Target and stop fills assume the order fills at its level plus slippage, even when a bar gaps through the level.
- **Entry price.** Entry is at the 09:31 bar's open, so the 09:30 open is assumed tradeable at that price plus slippage.
- **Continuous-contract roll effects.** The data is a continuous series. Whether it is back-adjusted is UNVERIFIED. A roll between the prior close and the open can create or remove an artificial gap, and that would directly change which days this strategy trades.
- **Data artifacts.** Weekend stray bars and the truncated 2023-04-05 are listed under Adversarial findings above.
- **MAE.** The intratrade bound comes from the trade's own bars. It is not NT8's MAE.
- **MNQ figures** are derived from NQ points at $2 a point with $1.90 commission (the D6 method). They are not an MNQ-data run.
- **Level.** NOT validated against NT8. These are Mac-side Python pre-screen figures: written and run, and reproduced by a second independent Python implementation (in-sample only). Agreement between two Python implementations of the same text does not check them against NT8's fill engine.

## Files staged (temp index `/tmp/praxis-c1/idx` only)
Built with `GIT_INDEX_FILE=/tmp/praxis-c1/idx git read-tree HEAD`. The DECISIONS.md blob is `git show HEAD:DECISIONS.md` + one blank line + the entry file (2,525 → 2,537 lines; 0 matches for `D-2026-11-12-B` in the diff). The MANIFEST.md blob is `git show HEAD:MANIFEST.md` + 8 rows, one per new file. The trade CSV is 67,969 bytes, under 2 MB, so it is staged.
`GIT_INDEX_FILE=/tmp/praxis-c1/idx git diff --cached --numstat HEAD`, taken before this section was written; this file's own row is therefore smaller than its final count:
```
12	0	DECISIONS.md
8	0	MANIFEST.md
246	0	docs/reports/2026-11-14-search-c1-gap-fade-manager.md
342	0	docs/reports/2026-11-14-search-c1-gap-fade-worker1.md
127	0	docs/reports/2026-11-14-search-c1-gap-fade-worker2.md
11	0	research/search-loop/c1-gap-fade/D-2026-11-14-A.entry.md
52	0	research/search-loop/c1-gap-fade/RULES.md
1051	0	research/search-loop/c1-gap-fade/out/summary.json
649	0	research/search-loop/c1-gap-fade/out/trades_V2_full.csv
587	0	research/search-loop/c1-gap-fade/screen.py
```
Real index, `git diff --cached --stat | tail -1` (unchanged: the 1 path staged at session start):
```
 1 file changed, 0 insertions(+), 0 deletions(-)
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Cure 1 (S1), appended 2026-11-14 by the manager

### (b) supports manager.md :219 ("instead of Friday's 16378")

```
$ /usr/bin/grep -n -E '^20210326 160000' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
19230:20210326 160000;16357.5;16391;16357.5;16378;6771
$ awk -F'[ ;]' '$1=="20210328" && $2>="093100" && $2<="160000" {print NR": "$0}' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
19276: 20210328 093100;16375;16375;16375;16375;1
$ /usr/bin/grep -c '^20210328 ' "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
360
```

### (d) supports manager.md :229 (F4 tier sizes are D6's TIERS, the WF spec's 2026-11-05 capture)

```
$ /usr/bin/grep -n -e 'tier sizes and limits are' -e 'tier rows: WF spec' -e 'The tier rows are' docs/reports/2026-11-09-d6-drawdown-check-manager.md
112:The tier rows are `git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` :115-130 (sizes and limits as coded in `TIERS` in Appendix B; Flex :131 is UNVERIFIED and has no figures, so it is not computed). Excerpt:
240:- **F4 / MFFU terms.** The tier sizes and limits are the WF spec's 2026-11-05 capture. MFFU's current pages were not re-read (no network). They are UNVERIFIED as of today.
588:# ---------- tier rows: WF spec HEAD :115-130; A4 = below min(3.2% size, 80% limit) ----------
```

### (e) supports manager.md :54 (cost-model MNQ commission)

```
$ /usr/bin/grep -n commission_round_turn_usd_mnq config/backtest-cost-model.json
22:    "commission_round_turn_usd_mnq": 1.90,
$ git show HEAD:config/backtest-cost-model.json | /usr/bin/grep -n commission_round_turn_usd_mnq
22:    "commission_round_turn_usd_mnq": 1.90,
```

### Restaging evidence

Pre-edit copies and their blob ids, captured before any edit:

```
$ cat /tmp/praxis-c1/cure1/pre_idx.txt
$ date -u; GIT_INDEX_FILE=/tmp/praxis-c1/idx git ls-files -s docs/reports/2026-11-14-search-c1-gap-fade-manager.md docs/reports/2026-11-14-search-c1-gap-fade-worker1.md; git hash-object /tmp/praxis-c1/cure1/pre/*.md; wc -l /tmp/praxis-c1/cure1/pre/*.md
Sat Nov 14 13:29:43 UTC 2026
100644 86299a866af895455553d3a6c275634d8f913a48 0	docs/reports/2026-11-14-search-c1-gap-fade-manager.md
100644 75bb1ea73bcb29d7140ff6241f823604f0f52859 0	docs/reports/2026-11-14-search-c1-gap-fade-worker1.md
86299a866af895455553d3a6c275634d8f913a48
75bb1ea73bcb29d7140ff6241f823604f0f52859
     263 /tmp/praxis-c1/cure1/pre/2026-11-14-search-c1-gap-fade-manager.md
     342 /tmp/praxis-c1/cure1/pre/2026-11-14-search-c1-gap-fade-worker1.md
     605 total
```

Pre-cure lines unchanged (no output from `cmp` means identical):

```
$ head -n 342 docs/reports/2026-11-14-search-c1-gap-fade-worker1.md | cmp - /tmp/praxis-c1/cure1/pre/2026-11-14-search-c1-gap-fade-worker1.md; echo cmp_exit=$?
cmp_exit=0
$ head -n 263 docs/reports/2026-11-14-search-c1-gap-fade-manager.md | cmp - /tmp/praxis-c1/cure1/pre/2026-11-14-search-c1-gap-fade-manager.md; echo cmp_exit=$?
cmp_exit=0
```

Standing limitation sentence counts (exact-line, then substring):

```
$ /usr/bin/grep -c -x 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' docs/reports/2026-11-14-search-c1-gap-fade-worker1.md docs/reports/2026-11-14-search-c1-gap-fade-manager.md
docs/reports/2026-11-14-search-c1-gap-fade-worker1.md:1
docs/reports/2026-11-14-search-c1-gap-fade-manager.md:1
$ /usr/bin/grep -c 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' docs/reports/2026-11-14-search-c1-gap-fade-worker1.md docs/reports/2026-11-14-search-c1-gap-fade-manager.md
docs/reports/2026-11-14-search-c1-gap-fade-worker1.md:1
docs/reports/2026-11-14-search-c1-gap-fade-manager.md:3
```

MANIFEST rows in the staged blob. No row states a line count, size or sha for either report, so MANIFEST.md was left untouched:

```
$ GIT_INDEX_FILE=/tmp/praxis-c1/idx git show :MANIFEST.md | tail -8
| /research/search-loop/c1-gap-fade/RULES.md | Spec | 3 | 2026-11-14 | Strategy search loop candidate 1 (C1 Opening Gap Fade) rules, written before any test (13:05:48Z; sha256 f892a265…74ba3): 09:31-bar open fade toward the prior RTH close, stop = gap distance, 2 ticks/side slippage, stop-first, time exit at last RTH bar; variants V1-V3, periods, fixed selection rule; MNQ cost and four-measure drawdown basis quoted from the D6 report. Pre-screen rules only (D-2026-11-14-A); no NinjaScript |
| /research/search-loop/c1-gap-fade/D-2026-11-14-A.entry.md | Log | 3 | 2026-11-14 | Source text of DECISIONS.md entry D-2026-11-14-A (search loop Mac-side pre-screen; master under D-2026-11-08-D D1), written 13:05:58Z before the screen ran; appended verbatim to the staged DECISIONS.md blob |
| /research/search-loop/c1-gap-fade/screen.py | Script | 3 | 2026-11-14 | C1 Opening Gap Fade Mac-side Python PRE-SCREEN (stdlib, exact Fractions; run `python3 -I -B`): in-sample V1-V3, selection, holdout and full for the selected or for-the-record variant only (assert guard), D6 four-measure drawdown tier table at 1 MNQ via read-only import of scripts/wf; WRITTEN + RUN, in-sample reproduced by a cold re-implementation; NOT validated against NT8 |
| /research/search-loop/c1-gap-fade/out/summary.json | Data | 3 | 2026-11-14 | screen.py output: per-variant in-sample tables, selection (none qualifies; V2 for the record), V2 holdout and full tables at $2.96/$4.68/MNQ, D6-basis per-window and tier tables, input shas (written by the manager's verification re-run 13:16:01Z, output identical to the recorded 13:10:23Z run except the timestamp) |
| /research/search-loop/c1-gap-fade/out/trades_V2_full.csv | Data | 3 | 2026-11-14 | screen.py trade list, V2 (for the record, not selected), full period 2021-03-08 to 2026-07-17: 648 trades with PC, O, gap_pct, fills, exit kind/stamp, points, NQ net at $2.96/$4.68, MNQ net, bar-based MAE |
| /docs/reports/2026-11-14-search-c1-gap-fade-manager.md | Report | 3 | 2026-11-14 | Manager report for unit 2026-11-14-search-c1-gap-fade (bead Praxis_build-vn4; criteria S1, S2, S4, S6, S13): timeline, rules and entry shas, timestamp evidence, in-sample tables V1-V3, selection (none qualifies), V2 holdout/full, D6-basis 1 MNQ tier table (no row passes), re-implementation comparison (1,304 trades identical), bar scoring; verdict PRE-SCREEN FAIL (items 3, 4; item 2 not met by construction) |
| /docs/reports/2026-11-14-search-c1-gap-fade-worker1.md | Report | 3 | 2026-11-14 | BUILD worker 1 report for unit 2026-11-14-search-c1-gap-fade (filed by the manager from the inline return): timestamp-convention check (ET bar-end not contradicted), screen.py implementation notes, full run output, file shas, ambiguities (weekend stray bars, early closes, gap skips) |
| /docs/reports/2026-11-14-search-c1-gap-fade-worker2.md | Report | 3 | 2026-11-14 | ADVERSARIAL worker 2 report for unit 2026-11-14-search-c1-gap-fade (cold re-implementation from RULES.md only; filed by the manager from the inline return): interpretations, in-sample V1-V3 run output, data-artifact check, shas |
```

Temp index after restaging the two reports, and the real index:

```
$ GIT_INDEX_FILE=/tmp/praxis-c1/idx git diff --cached --numstat HEAD
12	0	DECISIONS.md
8	0	MANIFEST.md
364	0	docs/reports/2026-11-14-search-c1-gap-fade-manager.md
465	0	docs/reports/2026-11-14-search-c1-gap-fade-worker1.md
127	0	docs/reports/2026-11-14-search-c1-gap-fade-worker2.md
11	0	research/search-loop/c1-gap-fade/D-2026-11-14-A.entry.md
52	0	research/search-loop/c1-gap-fade/RULES.md
1051	0	research/search-loop/c1-gap-fade/out/summary.json
649	0	research/search-loop/c1-gap-fade/out/trades_V2_full.csv
587	0	research/search-loop/c1-gap-fade/screen.py
$ git diff --cached --stat | tail -1
 1 file changed, 0 insertions(+), 0 deletions(-)
```

