# O4 reduce-2, worker 1: adversarial check of D-2026-11-13-A (DECISIONS.md:2389-2416)

**Task:** cold adversarial check, six checks (a)-(f). **Mode:** ADVERSARIAL, one round, read-only. **Criterion:** rubric O4, `specs/SPEC_RUBRIC.md:117-122`.
**Process log:** read the entry; diffed against `/tmp/o4red2-pre-DECISIONS.md`; ran a literal byte check on every line-cited quote; read R2-R8 (:1556-1590), R-VN3-5 (:508-513), D-2026-11-08-D D1/D2 (:1907-1916), the Q9 owner (:180) and the 2026-11-01 run readback.

## Verification evidence (command output)

```
$ diff /tmp/o4red2-pre-DECISIONS.md /Volumes/Sensidine/Praxis.build/DECISIONS.md | /usr/bin/grep -E '^[0-9]'
2393c2393
```
(Full diff seen: the only change removes ", the version closest to live (R-VN3-5, R-1104-3)" from line 2393. Both files are 2416 lines.)

Quote check: a bash loop reading 29 `file|line|string` records from a heredoc (each spec, DECISION_LOG, strategy, topology, DECISIONS.md and d6-report quote at its cited line), `sed -n "${l}p" "$f" | /usr/bin/grep -qF -- "$s"`, printing misses and a total:
```
present=29 missing=0
```
```
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '116p' | /usr/bin/grep -cF 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'; sed -n '1560,1561p' DECISIONS.md | tr -s ' \n' ' ' | /usr/bin/grep -cF 'a break-even trade counts as half a loss'; bd show Praxis_build-yra 2>&1 | /usr/bin/grep -cF 'the live-vs-backtest gate is structurally unmeetable.'; /usr/bin/grep -cE 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs | tr '\n' ' '; echo; /usr/bin/grep -c '^## .*Deviation C' DECISIONS.md
1
1
1
ninjascript/PraxisNoiseAreaBreakout.cs:0 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0 
0
```
```
$ sed -n '180p' DECISIONS.md | cut -c1-90; sed -n '2389,2415p' DECISIONS.md | /usr/bin/grep -oE "master's reading|SHM-4 and SHM-5's \"backtest\" is read as the with series|CONDITIONAL|Void if any one is observed false|this entry sets none|No code, no strategy file, no breaker value and no spec body is changed|runs both, and is graded with breakers|The gate compares Block 4 paper trades against the with series only" | sort | uniq -c
## 2026-07-15 — D-2026-07-15-B: Block-2 spec gaps Q2–Q9 RESOLVED (trader, session 15)
   3 CONDITIONAL
   1 No code, no strategy file, no breaker value and no spec body is changed
   1 SHM-4 and SHM-5's "backtest" is read as the with series
   1 The gate compares Block 4 paper trades against the with series only
   1 Void if any one is observed false
   2 master's reading
   1 runs both, and is graded with breakers
   1 this entry sets none
```

## (a) Quotes byte-present: PASS
All 29 line-cited quotes are present at their lines, along with the bf6fcc7:116 quote, R4 :1560-1561 joined and the bead text. The zero-hit claim holds for all three files. No `## ` heading contains Deviation C, which matches the :2401 claim.

## (b) Both O4 questions answered: PASS
:2393 says "runs both, and is graded with breakers". :2397 answers the gate question: compare against the with series only, never re-run on the without series. It fixes the arithmetic for both bands.

## (c) No over-attribution; master's readings labelled: FAIL (1 defect)
Nothing is attributed to Amear beyond his recorded words. R2, R4, R5 and R8 are paraphrased consistently with :1556-1590. Defect 1, line 2410: "SHM-4 and SHM-5's "backtest" is read as the with series" re-reads the word "backtest" in SHM-4 and SHM-5, which are trader-resolved bands (D-2026-07-15-B, :180, "(trader, session 15)"). This reading is not labelled as the master's. The entry labels its other three readings one by one ("master's reading under D1, changeable" at :2395 and :2397, "is the master's, under D1" at :2397), so leaving this one unlabelled suggests it is something other than the master's reading. The Status line's blanket label does not fix that, given the per-item practice.

## (d) Unobserved mechanisms CONDITIONAL with void clause or named gap: PASS
Assumptions (i)-(iii) at :2395 carry CONDITIONAL and the clause "Void if any one is observed false". Decision 2 is CONDITIONAL with "same void clause". The topology :59 conflict and the arm (b) selection split are named at :2410. "No with series exists yet" is stated at :2412.

## (e) No D2 item decided: PASS
No spend, no live or funded order path, no key, credential or permission. "this entry sets none" (:2412) and "no breaker value ... is changed". The #2/#3 rule defines processing order only, not values.

## (f) Diff changes line 2393 only: PASS
`2393c2393` is the only hunk.

## Observations (not defects)
- ":2393 The 2026-11-01 runs are without-series records only" is not checked against what those runs were. The readback (`docs/reports/2026-11-01-three-strategy-results.md` :79, :185) shows they ran OppBand and Flat1559 variants, plus a third LH-momentum strategy (:355-356, entries 15:31, exits LHFlat1559). Run 1 exits are "Exit on session close 792, XL 10, XS 8" (:132). None is named "16:00 session flat", so they do not match the without series defined at :2393 (the raw list of the strategy with reverse and 16:00 flat).
- With 2393's citation removed, Decision 1's "graded with breakers" choice cites no ruling. :512 is quoted in Sources, but :512 itself is "Agent's reading, confirmed by Amear in voice only". The entry does not carry that qualifier.
- `PraxisNoiseAreaBreakout_OppBand.cs` :250 marks same-bar exit+reverse as "CANNOT-DETERMINE-STATICALLY". This supports keeping assumption (ii) CONDITIONAL.

## Files staged
None. Read-only; this report is the only file created.

## Result: FAIL (1 defect)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
