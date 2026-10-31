# Praxis_build-zyd — rulings append to D-2026-10-30-A

## Task
Append ONE "Rulings 2026-10-30" block (brief text, verbatim) after the `**Unblocks:**` paragraph of D-2026-10-30-A in `DECISIONS.md`. No existing line changed. Staged, not committed. Done by the manager directly per the brief (no workers dispatched).

## Rubric criteria addressed
```
107:| S1 | Every claim in a report has pasted command output, not a description of output. |
111:| S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation. |
```

## Authorisation (S5) — DECISION_LOG row `2026-10-30T23:23:00Z`
```
458:- [2026-10-30T23:23:00Z] **WHO: amear** | PROPOSED BY: praxis-master (three structured questions lifted from D-2026-10-30-A's NEEDS AMEAR 5, 2 and 4) | APPROVED BY: amear, AskUserQuestion this turn | WHAT: **THREE RULINGS ON THE F3 ARTIFACT.** **(R-F3-1, closes NEEDS AMEAR 5 / bead zyd (c)):** *"Commit conditional + R3 control tomorrow."* D-2026-10-30-A is committed tonight as the CONDITIONAL entry it already is. On 2026-10-31 Amear runs the run-4 configuration TWICE — `Order fill resolution` Standard vs High, every other field held — and compares the trade lists. Identical → (c) is OBSERVED and F3 moves to PASSED (his edit of the rubric line); different → the `00:10:00Z` void clause fires and (c) is re-decided cold. This is the R3 control proposed at `2026-08-29T00:40:00Z`, adopted. The "rule (c) stands as INFERRED" option was offered and NOT taken. **(R-F3-2, closes NEEDS AMEAR 2):** *"Yes — the 10-28 notes are the writing."* F3's "stated in writing before the backtest runs" is satisfied by `docs/reports/2026-10-28-voice-session-notes.md` §rulings item 3, a dated written record of `[N]` = 2 preceding every Analyzer run; the ledger rows transcribe it. **(R-F3-3, closes NEEDS AMEAR 4):** limitation sentence APPROVED as proposed — *"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."* Every backtest report carries it. **Still open (not asked this turn):** NEEDS AMEAR 1 (SHM-4 band re-read against a 2-tick base), 3 (slippage unit — now bead `o78`), 6 (scope of the `[N]` lock over session-close/stop-out exits) | WHY: S8 — asked, not decided; memory `amear-conditional-commitment` — the decide-now branch rested on unobserved mechanism, so the conditional-plus-control form was offered first and he took it | WHERE: `DECISIONS.md` entry D-2026-10-30-A (its NEEDS AMEAR 2/4/5 are answered by this row; the entry is amended by APPEND after the running audit returns, not under it); tomorrow's hand-test plan (bead `7zq` checklists) gains the Standard-vs-High pair as step 0 | WHEN: 2026-10-30 | HOW: a small manager append to the entry ("Rulings 2026-10-30" paragraph) once the auditor is out of the files, graded on the delta, then the commit commands | STATE: closed — ruled; amendment pending
```
Note: the brief's text paraphrases the row in two places (row says `00:10:00Z` and `§rulings item 3`; the appended text says `2026-08-29T00:10:00Z` and `§"Amear's rulings" item 3`). Both anchors were checked to exist:
```
347:- [2026-08-29T00:10:00Z] WHO: praxis-master (session 52) | PROPOSED BY: praxis-master 
355:- [2026-08-29T00:40:00Z] WHO: praxis-master (session 52) | WHAT: **A STRONGER F3 CLEAR
6:## Amear's rulings
```

## Process log / Verification evidence
Before (pre-edit numstat, captured this session): `54	0	DECISIONS.md`, `wc -l` = 297. Pre-edit copy saved to scratchpad; checks run right after the append:
```
$ wc -l DECISIONS.md
     304 DECISIONS.md
$ cmp <(head -297 DECISIONS.md) DECISIONS.before && echo PREFIX_IDENTICAL
PREFIX_IDENTICAL
$ diff <(tail -n 6 DECISIONS.md) block.md && echo BLOCK_VERBATIM
BLOCK_VERBATIM
$ git diff --cached --numstat DECISIONS.md
61	0	DECISIONS.md
```
Added rose 54 → 61 (+7 = 1 blank + 6 block lines); deleted stays 0.

Before — `sed -n '295,297p'` of the pre-edit file:
```
**Supersedes:** D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY. Q5's $2.96 round-turn commission and "Applies to ALL P&L / SHM distributions" stand. D-2026-07-15-B's text is not edited.

**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.
```
After — `sed -n '295,304p' DECISIONS.md`:
```
**Supersedes:** D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY. Q5's $2.96 round-turn commission and "Applies to ALL P&L / SHM distributions" stand. D-2026-07-15-B's text is not edited.

**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.

**Rulings 2026-10-30 (Amear, DECISION_LOG `2026-10-30T23:23:00Z`; answer NEEDS AMEAR 5, 2 and 4 above — appended, nothing above edited):**
- **NEEDS AMEAR 5 → RULED: "Commit conditional + R3 control tomorrow."** This entry is committed as the CONDITIONAL it is. On 2026-10-31 Amear runs the run-4 configuration twice — `Order fill resolution` Standard vs High, every other field held — and compares the trade lists. Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires and (c) is re-decided cold. This adopts the R3 control proposed at DECISION_LOG `2026-08-29T00:40:00Z`. "Rule (c) stands as INFERRED" was offered and not taken.
- **NEEDS AMEAR 2 → RULED: "Yes — the 10-28 notes are the writing."** F3's "stated in writing before the backtest runs" is satisfied by `docs/reports/2026-10-28-voice-session-notes.md` §"Amear's rulings" item 3, a dated written record of `[N]` = 2 preceding every Analyzer run; the DECISION_LOG rows transcribe it.
- **NEEDS AMEAR 4 → RULED: limitation sentence APPROVED as proposed.** Every backtest report carries: `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
- **Still open:** NEEDS AMEAR 1 (SHM-4 band vs the 2-tick base), 3 (slippage unit — bead Praxis_build-o78), 6 (scope of the `[N]` lock over session-close / stop-out exits).
- **Status after these rulings:** CONDITIONAL, committable; bead zyd (c) closes on the 2026-10-31 control result, not on this entry.
```

`git diff --cached DECISIONS.md | tail -40`:
```
+- **Limitation sentence — PROPOSED wording, not ruled by Amear (his ruled requirement is only "Fills are optimistic and the report states so", 2026-08-29T00:10:00Z):** `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
+
+**Rationale:** Amear's ruling, ledgered. Standard on 1-minute bars was accepted in the `00:10:00Z` conditional; `[N]` = 2 was set by Amear at `21:36:30Z` and reaffirmed at `2026-10-30T22:22:00Z` (WHO: amear). The master does not assert 2 ticks is correct (`21:36:30Z`); this entry does not either.
+
+**Authorisation chain (S5 — the ledger rows are the authorisation):** DECISION_LOG `2026-08-29T00:10:00Z` → `2026-08-29T00:35:00Z` → `2026-08-29T00:40:00Z` (R3 control proposed; open) → `2026-10-30T21:36:00Z` (WHO: amear; intake of the rulings) → `2026-10-30T21:36:30Z` → `2026-10-30T22:22:00Z` (WHO: amear) (`[N]` stays 2) → `2026-10-30T22:28:00Z` (dispatch).
+
+**Config pointer:** this entry IS the DECISIONS.md entry that `config/backtest-cost-model.json`'s `$schema_note` requires for the v1.1.0 number change.
+
+**Scope of change (explicit):**
+- `config/backtest-cost-model.json` → v1.1.0: slippage 1 → 2 ticks/side ($5 → $10/side; 2 → 4 ticks / $10 → $20 RT); `fill_resolution` High → Standard; total $12.96 / 2.592 ticks → $22.96 / 4.592 ticks RT.
+- Added key `amended: 2026-10-30`; `$schema_note`, `decision_ref`, `fill_resolution_note` and `total_cost_breakdown_note` text updated. No key removed.
+- Commission ($2.96 RT), instrument block, `applies_to`, `bead`, `created` unchanged.
+
+**S6 cross-block — consumers and what changes for each:**
+- All P&L distributions (NT8 WFA fills + Python Monte Carlo): now carry $22.96 RT.
+- R-multiple conversion (Q6): the new $22.96 RT cost is deducted before R normalisation.
+- All SHM distributions and threshold derivations (D-2026-07-04-B): derive from the 2-tick base. SHM-4 (`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:48-51`) includes slippage in its metric; its band numbers live in D-2026-07-15-B Q9 — see NEEDS AMEAR (1).
+- Rubric O4 Block-4 gate (`specs/SPEC_RUBRIC.md:94-99`, ±15% win rate / ±25% average trade P&L): compares live to a 2-tick backtest.
+- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
+- Spec text still carrying the superseded Q5 terms (not edited here; superseded on slippage and fill resolution by this entry): `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129` ("High fill res, 1-tick series, 1-tick slippage", attributed there to the Phase 3 Build Spec) and `docs/specs/2026-07-15-b2-data-acquisition-spec.md:53` ("Q5, 1 tick/side" and "the High-resolution intrabar path").
+- F4 (MFFU automation compliance): `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` §4 (`:151`) couples MFFU restriction 2 (no automated tools built to exploit sim-environment fill favorability, `:45`) to F3's optimistic-fill failure mode. Named, not resolved; F4's disposition is Amear's.
+
+**NEEDS AMEAR (questions only):**
+1. Is SHM-4's "slippage >2 ticks/side worse" band (D-2026-07-15-B Q9) re-read against the new 2-tick base?
+2. `[N]` was chosen 2026-10-28 (REPORTED); its first ledger writing is the `2026-10-30T21:36:00Z` (WHO: amear) intake row, restated at `2026-10-30T21:36:30Z`, both after runs 1–3 had run; this entry is written after run 4 (REPORTED). Does that satisfy F3's "stated in writing before the backtest runs"?
+3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?
+4. Approve or replace the proposed limitation sentence.
+5. The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Is it run before F3 is graded, or does (c) stand as INFERRED?
+6. Scope of the `[N]` lock (3gm `:949`, reserved for Amear): row `2026-10-30T21:36:30Z` sets `[N]` as band-edge slippage and states it per round trip ($22.96); the Analyzer's Slippage setting applies to every market fill (INFERRED). Was the lock meant to cover session-close and stop-out exits as well?
+
+**Supersedes:** D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY. Q5's $2.96 round-turn commission and "Applies to ALL P&L / SHM distributions" stand. D-2026-07-15-B's text is not edited.
+
+**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.
+
+**Rulings 2026-10-30 (Amear, DECISION_LOG `2026-10-30T23:23:00Z`; answer NEEDS AMEAR 5, 2 and 4 above — appended, nothing above edited):**
+- **NEEDS AMEAR 5 → RULED: "Commit conditional + R3 control tomorrow."** This entry is committed as the CONDITIONAL it is. On 2026-10-31 Amear runs the run-4 configuration twice — `Order fill resolution` Standard vs High, every other field held — and compares the trade lists. Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires and (c) is re-decided cold. This adopts the R3 control proposed at DECISION_LOG `2026-08-29T00:40:00Z`. "Rule (c) stands as INFERRED" was offered and not taken.
+- **NEEDS AMEAR 2 → RULED: "Yes — the 10-28 notes are the writing."** F3's "stated in writing before the backtest runs" is satisfied by `docs/reports/2026-10-28-voice-session-notes.md` §"Amear's rulings" item 3, a dated written record of `[N]` = 2 preceding every Analyzer run; the DECISION_LOG rows transcribe it.
+- **NEEDS AMEAR 4 → RULED: limitation sentence APPROVED as proposed.** Every backtest report carries: `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
+- **Still open:** NEEDS AMEAR 1 (SHM-4 band vs the 2-tick base), 3 (slippage unit — bead Praxis_build-o78), 6 (scope of the `[N]` lock over session-close / stop-out exits).
+- **Status after these rulings:** CONDITIONAL, committable; bead zyd (c) closes on the 2026-10-31 control result, not on this entry.
```

## Workers dispatched
None — the brief required the manager to do this edit directly.

## Adversarial findings
No adversarial worker (brief: do not spawn). Self-check only: byte-level prefix `cmp` and block `diff` above. The row-vs-brief paraphrase noted above is the one open discrepancy, for the auditor to judge.

## S6 cross-block check
Not exercised — no hook trip in this unit.

## Files staged
```
$ git status --short DECISIONS.md docs/reports/2026-10-30-zyd-rulings-append.md
M  DECISIONS.md
AM docs/reports/2026-10-30-zyd-rulings-append.md
$ git status --short | /usr/bin/grep -v '^??' | wc -l   (full tracked status; untracked set unchanged by this unit)
      33
$ git status --short | /usr/bin/grep -v '^??'
 M .claude/settings.json
 M AUDIT_LOG.md
M  DECISIONS.md
MM DECISION_LOG.md
 M DISPATCH_LOG.md
MM ISSUE_REGISTER.md
M  MANIFEST.md
M  config/backtest-cost-model.json
A  docs/reports/2026-08-06-session42-r8j-phase3-import.md
A  docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction.md
AM docs/reports/2026-10-28-f4-davi-reply-filing.md
A  docs/reports/2026-10-28-nightly-checks-plan-review-note.md
AM docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
A  docs/reports/2026-10-30-zyd-f3-artifact.md
AM docs/reports/2026-10-30-zyd-rulings-append.md
A  docs/reports/2026-10-30-zyd-worker1-build.md
A  docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md
A  docs/reports/2026-10-30-zyd-worker2-adversarial.md
A  docs/reports/2026-10-30-zyd-worker3-fix.md
A  docs/reports/2026-10-30-zyd-worker4-readversarial.md
A  docs/reports/2026-10-30-zyd-worker5-fix2.md
A  docs/reports/2026-10-30-zyd-worker6-final-adversarial.md
A  docs/reports/2026-10-30-zyd-worker7-fix3.md
A  docs/reports/2026-10-30-zyd-worker8-final2-adversarial.md
A  docs/reports/2026-10-30-zyd-worker9-fix4.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
M  docs/specs/2026-08-08-ledger-compaction-spec.md
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
```
Observer effect: the report shows `AM` above because the status was captured while this section was being appended; the report was re-staged afterwards and is `A ` (checked by the final `git status --short` at return). Other tracked lines match the session-start snapshot; this unit added only the report and the DECISIONS.md delta.

Result: PASS (self-verified; final grade is the auditor's)
