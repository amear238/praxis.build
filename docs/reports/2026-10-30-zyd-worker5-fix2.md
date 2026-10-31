# Praxis_build-zyd — worker5 fix pass 2

## Task
Apply manager-confirmed fixes G1–G8 to the D-2026-10-30-A entry of `DECISIONS.md`, `config/backtest-cost-model.json` (`cost_model.fill_resolution_note`), and `MANIFEST.md` rows from line 133 on. Nothing else.

## Mode
BUILD (fix pass 2). Sub-report to the zyd manager report. NOT authoritative.

## Criterion
Rubric F3 written-assumption requirement (`specs/SPEC_RUBRIC.md:45-57`); bead Praxis_build-zyd acceptance (a)(b)(c). This report does not grade F3.

## Process log
- Backed up the three files to scratchpad `w5f/`, then applied all edits with one Python script (`w5f/edit.py`). Each replacement asserts its exact-match count; all assertions passed. DECISIONS edits were applied only to the text from the `## 2026-10-30 — D-2026-10-30-A` heading onward. MANIFEST edits were applied only to line 133 onward.
- G1: inserted the R3 falsifier sentence after "— is INFERRED." in (c); added NEEDS AMEAR 5; added `` → `2026-08-29T00:40:00Z` (R3 control proposed; open)`` after `2026-08-29T00:35:00Z` in the authorisation chain.
- G2: replaced the Unblocks sentence with the stated-limitation wording (`specs/SPEC_RUBRIC.md:55-56`; wording is Amear's, NEEDS AMEAR 4).
- G3: replaced the `**Resolves:**` line with the `**Addresses (for audit; not a grade):**` line. Added nothing about whether F3 is FROZEN or PASSED.
- G4: replaced "the ledger (2026-10-30T21:36:30Z) says…" with the master's-note attribution plus Amear's 00:10 framing and the 00:35 mismatch.
- G5: replaced the END-STAMPED label with "INFERRED by Claude … notes `:25`; Amear's NT8 read … REPORTED, notes `:23`". The rest of the parenthesis (path `:22-27`, "a file untracked in git") is unchanged.
- G6: replaced `:737-775` with `:737-773` (1 occurrence). The source check shows line 774 is the D4 heading (pasted below).
- G7: `fill_resolution_note` clause replaced. The diff against the backup shows this is the only line that changed in the config.
- G8: the run-3 row now carries `, WHO: amear`. Five worker sub-report rows were inserted immediately before the `zyd-f3-artifact.md` row.

## Verification evidence
```
== 1
0                                   # git diff DECISIONS.md MANIFEST.md | grep -c '^-[^-]'
head246 now:            c438920fc1dc03a4b151e620ea8ff33e4fdf7a4926ef60c14704dc653e1a4b20
head246 pre-edit backup: c438920fc1dc03a4b151e620ea8ff33e4fdf7a4926ef60c14704dc653e1a4b20
HEAD:DECISIONS head246: a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a
head243 now vs HEAD:    a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a / a0c8fbeea8dcafd72f7385c2b1c50594a6cf7349c8bd49032531cb4491d5234a
MANIFEST head132 now vs index: ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf / ccb7c2898b679e4abb78e20fceb166b9cd58ee6d32db387e6efe2e3422a06abf
== 2
PARSE_OK
total_cost_per_round_turn_usd = 22.96
total_cost_per_round_turn_ticks = 4.592
slippage_ticks_per_side = 2
fill_resolution = Standard
== 3
R3 Standard-vs-High control => 2      # (c) sentence + NEEDS AMEAR 5
5. The R3 => 1
(R3 control proposed; open) => 1
Addresses (for audit; not a grade) => 1
the wording is Amear => 1
master's note in row => 1
INFERRED by Claude from the import file => 1
:737-773 => 1
**Resolves:** => 0
:737-775 => 0
carry the limitation sentence above => 0
== 4
True f9144cb50aab2885 f9144cb50aab2885
== 5
0                                     # no FROZEN lines in entry
== G6 src (sed -n '772,775p' docs/reports/2026-10-30-3gm-fidelity-check.md)
**ExitOnSessionClose in addition to FlattenAll?** Yes. Both can act on the 16:00 bar; that is scenario S4 (INFERRED).

## D4 — Run 1 (48 trades) vs run 2 (41 trades): NOT resolved
== config diff vs pre-edit backup
old: or on the 16:00 clock for FlatEOD (no Set*/Submit*/limit/stop call — OBSERVED in code)
new: or on any bar with minute-of-day >= 16:00 for FlatEOD, plus the platform session-close exit (IsExitOnSessionCloseStrategy, clock-triggered, INFERRED)
```
Check 6 (`tail -n 16 MANIFEST.md`): the five `zyd-worker{1..5}` rows sit between the voice-session-notes row and the `zyd-f3-artifact.md` row, followed by the config UPDATE row (full output is in the worker's return message).

## Deviations
- Check 1, as briefed, compares `head -n 246 DECISIONS.md` with `git show HEAD:DECISIONS.md | head -n 246`. That comparison cannot match: HEAD's file has only 243 lines. Lines 244-246 are the blank / `---` / blank separator added by an earlier pass. I substituted two checks. First, head-243 now vs HEAD: they match. Second, head-246 now vs my pre-edit backup: they match. Together these show nothing above the entry heading changed.
- None otherwise.

## Files staged
None. Nothing was git-added, per the brief. Files modified in the working tree: `DECISIONS.md`, `MANIFEST.md`, `config/backtest-cost-model.json`, plus this report.

## Result: PASS
