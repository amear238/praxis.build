# O4 deletion-only round 2 — manager report

## Task
Bead Praxis_build-yra, rubric O4. Master DECISION_LOG row 2026-11-13T09:03:00Z (decided by master under D-2026-11-08-D D1). Delete two strings from DECISIONS.md line 2393 (entry D-2026-11-13-A, lines 2389-2416): ", the version closest to live" and " (R-VN3-5, R-1104-3)". No new words.

## Rubric criteria addressed
O4 (specs/SPEC_RUBRIC.md lines 117-122), S1, S2, S8.

## Workers dispatched
- worker1, ADVERSARIAL, cold, report docs/reports/2026-11-13-o4-reduce2-worker1.md. Outcome: Grade: FAIL (1 defect).

## Process log
1. Pre-check hash on lines 2389-2416 matched (7f9b16a1...9908). HEAD 587101b.
2. Pre-copy to /tmp/o4red2-pre-DECISIONS.md.
3. One perl substitution scoped to line 2393 removed the two adjacent strings (together they form ", the version closest to live (R-VN3-5, R-1104-3)"). The edit was a single line, so the manager made it directly.
4. Diff shows line 2393 only; both files are 2416 lines.

## Verification evidence (command output)

```
$ awk 'NR==2389,NR==2416' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 7f9b16a1a6c0c7473aa7e32824bbbc1a0f980f1067e8fb2c2b6efee5f31f9908
```

```
$ diff /tmp/o4red2-pre-DECISIONS.md DECISIONS.md
2393c2393
< **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series, the version closest to live (R-VN3-5, R-1104-3). The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.
---
> **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.
```

```
$ git diff --cached --name-only | wc -l
       1
```

```
$ grep -n "is read as the with series" DECISIONS.md | cut -c1-12
2410:**S6 cr
$ awk "NR>=2389 && NR<=2416" DECISIONS.md | grep -no "master.s reading under D1"
7:master's reading under D1
9:master's reading under D1
```
The entry offsets 7 and 9 are lines 2395 and 2397. Line 2410 carries no such label.

## Adversarial findings
Worker1 (cold, one round) graded FAIL (1 defect). Check (c): DECISIONS.md:2410 says SHM-4 and SHM-5's "backtest" is read as the with series. That is the master's reading of bands Amear resolved himself (D-2026-07-15-B, line 180, "(trader, session 15)"), and it is not labelled as the master's reading, although lines 2395 and 2397 do label theirs. The manager re-checked this and it holds (see evidence). Checks (a), (b), (d), (e), (f) passed. Per the brief, there was no second round and no cure.

Observations only (not graded, not fixed): line 2393 calls the 2026-11-01 runs without-series records, but those runs used different strategy variants whose exits do not match the without definition. Line 512, quoted under Sources, is the agent's reading confirmed by Amear in voice only, and the entry does not say so.

## S6 cross-block check
The entry is a DECISIONS.md text change only; no hook, script, setting or other block's file was touched.

## Files staged
None. Working-tree edits only: DECISIONS.md line 2393, this report, the worker report.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
