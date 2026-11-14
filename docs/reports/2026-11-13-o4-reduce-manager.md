# 2026-11-13 o4-reduce: manager report

## Task
Unit 2026-11-13-o4-reduce, bead `Praxis_build-yra`, rubric O4. Decided by master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T06:06:00Z. Cure the three defects the fourth adversary found in DECISIONS.md entry D-2026-11-13-A (docs/reports/2026-11-13-o4-parity-worker4.md :276-278) by deletion only; add no new claim.

## Rubric criteria addressed
O4 (`specs/SPEC_RUBRIC.md`:117-122): "a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both — and how the Block 4 gate is satisfiable if they differ." The entry's Decision 1 answers the first question (both, graded with) and Decision 2 the second. No acceptance criterion was authored here; the adversary's checks (a) to (f) are the master's.

## Workers dispatched
- worker1, ADVERSARIAL, cold (rubric O4 text, entry line range, checks (a) to (f) only; no manager reasoning). Report `docs/reports/2026-11-13-o4-reduce-worker1.md`. Outcome: `Grade: FAIL (1 defect)` (report :312). Per the brief, no second adversary round was started.

The deletions themselves were made by the manager: a pure doc edit of five exact-string replacements, each asserted to occur exactly once and below the entry heading.

## Process log
1. `cp DECISIONS.md /tmp/o4red-pre-DECISIONS.md`; pre-edit `wc -l` 2416; staged path count 1.
2. Defect (1): deleted the D-2026-11-04-A NEEDS AMEAR 4 / :832 clause in Decision 2; parenthesis now closes after "changeable".
3. Defect (2): deleted the sentence from "Amear's words: R-VN3-5 says" through "this entry plans no run." The trailing D-2026-11-04-A (ii) re-ask clause sat inside that same sentence and carried no quote and no cited line, so the keep test (quote byte-present at its cited line) could not be met; deleted with it.
4. Defect (3): replaced the span from "#4: both series carry" through "(D-2026-10-31-A NEEDS AMEAR 3, DECISIONS.md:351)" with the master's exact sentence. The span ended before "; #5", which first left ".;"; corrected to ". #5" (punctuation only). The #5 and "#1 and #6 to #9" clauses are unchanged.
5. Limits: "#1 or #6 to #9" changed to "#1, #4 or #6 to #9".
6. Sources: the :1490, :944, :351, :212 and :108 cites were inline in the deleted S6 text only and left with it; none was in a Sources bullet. In the "Breakers on" bullet, the fragment `:761 "when the time comes ask agaian."` existed only to back the deleted re-ask clause and was deleted; :512 stays (R-VN3-5 is still cited in Decision 1), as do :1584 and :1588 (R8, cited in Decision 1 and Limits). No whole Sources bullet was deleted. :205 and :191 stay (the full-day flat and the strategy's 16:00 flat are named in the new #4 sentence).

## Verification evidence (command output)
```
$ diff /tmp/o4red-pre-DECISIONS.md DECISIONS.md
2397c2397
< **Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable; open item D-2026-11-04-A NEEDS AMEAR 4, DECISIONS.md:832, "Is R-1104-3's judged version arm (a), arm (b) or both?"), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.
---
> **Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.
2405c2405
< - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; :761 "when the time comes ask agaian."; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
---
> - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
2410c2410
< **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. Amear's words: R-VN3-5 says "once they are built"; the with series simulates specified text before any breaker exists (named difference); D-2026-11-04-A (ii) re-ask binds before a High run, and this entry plans no run. #4: both series carry the strategy's 16:00 flat, so on a full trading day #4 does not split them. Early-close days are a named parity gap, not decided here: amended #4 flattens "or the exchange's early close on an early-close day if earlier" (spec :212); the strategy's explicit flat tests 16:00 only (code :189), its early-close exit is the platform backstop `IsExitOnSessionCloseStrategy              = true;` (code :108), and the record already shows an "early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00)" (DECISIONS.md:1490) and "12:15 early-close exits" accepted as is (DECISIONS.md:944). Whether the backtest's early-close exit matches amended #4's time is not established; early-close sessions are reported apart in Block 2 and Block 4, and whether they enter the gate is left open with early-close handling (D-2026-10-31-A NEEDS AMEAR 3, DECISIONS.md:351); #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
---
> **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
2412c2412
< **Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1 or #6 to #9, and does not mark O4 passed.
---
> **Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1, #4 or #6 to #9, and does not mark O4 passed.
[exit 1]
$ grep -n -F "## 2026-11-13 — D-2026-11-13-A" DECISIONS.md
2389:## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)
$ sed -n '2389,2416p' DECISIONS.md | shasum -a 256
7f9b16a1a6c0c7473aa7e32824bbbc1a0f980f1067e8fb2c2b6efee5f31f9908  -
$ wc -l DECISIONS.md
    2416 DECISIONS.md
$ git diff --cached --name-only | wc -l
       1
$ grep -n '^Grade' docs/reports/2026-11-13-o4-reduce-worker1.md
312:Grade: FAIL (1 defect)
```

Entry line range: 2389-2416 (heading at :2389; :2416 is the entry's S13 line, checked by `sed -n '2416p'`, output omitted here so the sentence appears once).

## Adversarial findings
worker1, one defect, checks (a), (b), (d), (e), (f) passed (31 quotes found at their cited lines; diff confined to lines 2397, 2405, 2410, 2412):
1. DECISIONS.md:2393, Decision 1, check (c): "the version closest to live (R-VN3-5, R-1104-3)" grounds grading on the with series in Amear's rulings, but his cited words do not carry it. R-VN3-5 (:510, :512) says breakers on "once they are built", while the with series is simulated from specified text before any breaker exists; the deleted S6 sentence was the place that named that difference. R-1104-3 is recorded as Amear's "Yeah" to "brief's framing" (:736), not his words.

Manager's check of the evidence: `grep -n -E 'R-1104-3' DECISIONS.md` shows :736 titling R-1104-3 as "Yeah" (brief's framing: High fill resolution + breakers on as the judged version)"; :508 to :512 show R-VN3-5 is the agent's reading confirmed in voice. The defect stands. It sits in Decision 1, which this unit's brief ("Nothing else changes") did not open, and it was partly exposed by the deletion of defect (2)'s sentence. Not cured here: any cure edits Decision 1 and needs a master decision (for example, delete the "(R-VN3-5, R-1104-3)" cite, or mark it as the master's reading under D1, changeable).

## S6 cross-block check
The edit removes claims; it adds none. Block 4 parity for breaker #4 is now named as not decided (S6 and Limits agree). Block 2 grading, Block 3 assumption (iii) and SHM text are unchanged. No other DECISIONS.md entry, spec, report or MANIFEST row is touched.

## Files staged
None by this unit. DECISIONS.md is modified in the working tree, unstaged; the real index still holds exactly 1 path (count below). New untracked files: this report and `docs/reports/2026-11-13-o4-reduce-worker1.md`.

## Result
Result: FAIL (adversary worker1 `Grade: FAIL (1 defect)`; the three master-accepted defects are cured by deletion, one check (c) defect remains in Decision 1, outside this unit's edit scope).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
