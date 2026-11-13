# O4 reduce-3, manager: deletion and labels on D-2026-11-13-A (bead Praxis_build-yra)

**Task:** three edits to DECISIONS.md lines 2393, 2405, 2410 (one deletion, two labels), then one cold adversary. Authorised by DECISION_LOG rows 2026-11-13T09:09:00Z and 2026-11-13T13:02:03Z (praxis-master, under D-2026-11-08-D D1).
**Rubric criteria addressed:** O4, specs/SPEC_RUBRIC.md:117-122.
**Workers dispatched:** worker 1, ADVERSARIAL, read-only, report docs/reports/2026-11-13-o4-reduce3-worker1.md; outcome under "Adversarial findings".
**Process log:** read rubric O4 and the reduce-2 adversary report; made the pre-copy; ran the three guard checks (all 1); made edits (i), (ii), (iii) with the Edit tool; diffed; dispatched the adversary with only the entry location, pre-copy path, rubric text and prior report path.

## Verification evidence (command output)

```
$ cd /Volumes/Sensidine/Praxis.build && git diff --cached --name-only | wc -l && git diff --cached --name-only && sed -n 110,125p specs/SPEC_RUBRIC.md && cp DECISIONS.md /tmp/o4red3-pre-DECISIONS.md && wc -l DECISIONS.md /tmp/o4red3-pre-DECISIONS.md
       1
[one path withheld: a staged evidence file whose name carries a person's name]
The signal directory was specified as a dedicated low-privilege macOS user, the
rationale being structural blast-radius limitation. The build report places it
at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —
the primary account home mounted into the VM. **Required:** either the user
exists, or a DECISIONS.md entry records the removal and its accepted risk.
A security requirement that stopped being mentioned is not a resolved one.

### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.

---
    2416 DECISIONS.md
    2416 /tmp/o4red3-pre-DECISIONS.md
    4832 total
```
Guard checks, re-run against the pre-edit copy (byte-identical to the pre-edit file: same 2416 lines, and the diff below has only the three intended hunks); line 512 is outside the edit:
```
$ cd /Volumes/Sensidine/Praxis.build && awk 'NR==2410' /tmp/o4red3-pre-DECISIONS.md | grep -o "is read as the with series" | wc -l; awk 'NR==512' DECISIONS.md | grep -cF "the agent's reading, confirmed by Amear in voice only"; awk 'NR==2405' /tmp/o4red3-pre-DECISIONS.md | grep -o 'the backtest runs \*\*with the breakers on, once they are built\*\*"' | wc -l; awk 'NR==2393' /tmp/o4red3-pre-DECISIONS.md | grep -cF ' The 2026-11-01 runs are without-series records only.'; awk 'NR==2393' DECISIONS.md | grep -c 'it is never graded\.$'
       1
1
       1
1
1
```
Line 512 guard is 1, so edit (iii) was made. Line 2393 still ends "it is never graded."

```
$ cd /Volumes/Sensidine/Praxis.build && diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; echo "exit=$?"; wc -l DECISIONS.md; diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md | grep -E '^[0-9]'; git diff --cached --name-only | wc -l
2393c2393
< **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded. The 2026-11-01 runs are without-series records only.
---
> **Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded.
2405c2405
< - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**"; R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
---
> - Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**" (the agent's reading, confirmed by Amear in voice only, :512); R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
2410c2410
< **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series, bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
---
> **S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series (the master's reading under D1, changeable), bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.
exit=1
    2416 DECISIONS.md
2393c2393
2405c2405
2410c2410
       1
```

## Adversarial findings

Worker 1 (cold, ADVERSARIAL, read-only), docs/reports/2026-11-13-o4-reduce3-worker1.md, overall `## Result: PASS` (:255). Grades quoted:
- :228 "## (a) Quotes byte-present: PASS" (28/29 at E2 :79; the miss is the worker's own ASCII "+/-" probe of the bare pointer :1771, and E3 :97 shows the "±" form present)
- :231 "## (b) Both O4 questions answered: PASS"
- :234 "## (c) No over-attribution; master's readings labelled: PASS" (:235: the :2410 reading "now carries \"(the master's reading under D1, changeable)\"")
- :238 "## (d) Unobserved mechanisms CONDITIONAL with void clause or named gap: PASS"
- :241 "## (e) No D2 item decided: PASS"
- :244 "## (f) Diff changes lines 2393, 2405, 2410 only: PASS"
- :247 "## (g) Prior observations graded against the edited entry: PASS": Obs 1 "resolved" (:248), Obs 2 "resolved" (:249), Obs 3 "not a defect" (:250)
Ungraded notes it recorded: :236, R8's #5 wording against amended spec :224 (belongs to D-2026-11-12-A, not this entry); :249, ":512's ruling is \"once they are built\"" against a post-run simulation, declared at :2412.
Negative test: check (c) is the gate that tripped last round (docs/reports/2026-11-13-o4-reduce2-worker1.md:45, "FAIL (1 defect)") on the line 2410 now edited. So the gate has blocked once before; this round it passes.

## S6 cross-block check

Wording only: no value, gate, breaker or spec body changes. The 2393 deletion removes an unchecked claim about the 2026-11-01 runs; Blocks 2 to 4 are unaffected.

## Files staged

None by this unit. Real index left at 1 path (start and end counts above). Files modified: DECISIONS.md (lines 2393, 2405, 2410), this report, and the worker report.

Correction (2026-11-13, cure of audit FAIL 1, DECISION_LOG 2026-11-13T13:17:27Z): line 13's pasted path is withheld because the file name carries a person's name; the stray-write sentence formerly at line 78 had no pasted output and is deleted. Nothing else in this report changed.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
