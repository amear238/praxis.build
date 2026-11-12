# 2026-11-12 — fgd doc alignment, correction 1 (bead Praxis_build-fgd) — manager report

## Task

Unit `2026-11-12-fgd-doc-alignment-correction-1`, decided by the master under D-2026-11-08-D D1. The fresh audit of unit `2026-11-12-fgd-doc-alignment` returned FAIL on check 7 (S1) and check 8 (de-identification). This unit cures each finding by in-place edits to the three uncommitted reports `docs/reports/2026-11-12-fgd-doc-alignment-manager.md`, `-worker1.md` and `-worker2.md`, masks the support rep's first name in the manager report's pasted index listing, sweeps all three reports end to end with the same tests, and itemises every edit below. The three spec amendment notes passed and were not touched (their sha1s in C12 equal the E13 values in the manager report). No spec, DECISIONS.md, rubric, ledger, code or `.claude/` file was edited by the manager; worker-memory files written by workers under `.claude/agent-memory/` (gitignored) are listed in C12 and C13a and disclosed under "Adversarial findings".

## Rubric criteria addressed

- S1 (`specs/SPEC_RUBRIC.md`:127): "Every claim in a report has pasted command output, not a description of output." Every cure either pastes a labelled re-run or reduces the claim to what is pasted.
- S2: no level is raised; the corrected reports keep the breakers SPECIFIED ONLY.
- S13 (`specs/SPEC_RUBRIC.md`:139): every report ends with the standing sentence (C10). The three original reports hold the sentence 3, 2 and 2 times, both in the pristine copies and now (C10, first and second commands); the extra occurrences are pasted `tail -n 1` output inside their evidence fences, not added by this unit.
- Public-repo de-identification (master's brief): rep name, email, trader surname, paper-author surnames, medication brands; counts only (C2, C3).

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| build-manager | BUILD | cure and sweep `-manager.md` only | the Agent tool's return for it read "this agent stopped at its 40-turn limit before finishing" (a tool return, not command output; not reproducible); its edit log (44 rows) and E14 block were on disk; the E14 block equals a fresh run of its script except for the two MANIFEST lines this manager changed (C8) |
| build-worker1 | BUILD | cure and sweep `-worker1.md` only, no line-count change at or above :562 | returned; 18 edits; line positions kept (C9) |
| build-worker2 | BUILD | sweep `-worker2.md` only, no line-count change at or above :399 | returned; 10 edits; line positions kept (C9) |
| adv-1 | ADVERSARIAL | re-check every cure, sample 10+ untouched claims, re-scan, S1 check of this report; report `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md` | see Adversarial findings |

## Process log

1. Copied the three reports to `/tmp/fgdc1/orig/` before any edit; every "orig line" below refers to those copies (C2 and C9 read them).
2. Derived the rep-name pattern by script from the one path in the real index into `/tmp/fgdc1/rep.txt` (never printed); its count against the index path is 1 (C1). The negative test: the scan finds it once, at the pre-correction manager copy's line 96 (C2), and 0 times after the mask (C3).
3. Dispatched three BUILD workers in parallel, one file each, with the rules file `/tmp/fgdc1/common-rules.md` (tests a–f). Each wrote an edit log under `/tmp/fgdc1/` and an evidence script; the logs are pasted verbatim in "Edits itemised".
4. Read the diffs of all three files against the pristine copies (hunk headers in C9) and re-ran all three evidence scripts against their pasted blocks (C8).
5. The manager made three edits itself (pure doc edits, itemised as M1–M3 below): a pointer from the manager report's step 4 to worker1's pasted pre-repair bytes (C7), and a one-sentence staleness note on the manager's E14 and worker1's re-run block after the MANIFEST append (C7, C8).
6. Appended MANIFEST.md rows at :452 and :453 (C13).
7. Dispatched adv-1; cures and residuals under Adversarial findings.

## Edits itemised

"orig line" is the line in `/tmp/fgdc1/orig/`; "new line" is the line in the edited file. In each log the old text is the pristine line, kept verbatim here as the append-only record; the rep's name is masked as `[rep-name]` in edit 32 of the manager log. The three logs were written by the BUILD workers and are pasted unchanged.

### Manager-made edits

| # | file | orig line | new line | old text | new text | reason |
|---|---|---|---|---|---|---|
| M1 | `-manager.md` | 25 | 25 | the line as left by build-manager (log row for orig 25; its new text) | the same line with one sentence inserted after "no INVALID result is pasted here.": "The pre-repair bytes `3a 80 93 39 34` on line 95 are pasted in worker1's report, section C3a (its python output, offsets 13567 and 13568)." | test e: the invalid state is shown by worker1's pasted output (C7) |
| M2 | `-manager.md` | 87 | 87 | the line as left by build-manager (log row 31, new text) | the same line plus: "E14 was run before correction-1 appended its two MANIFEST.md rows (:452–453); a fresh run now differs from the paste only in the MANIFEST.md mtime line and the MANIFEST.md hunk header (`+440,12` becomes `+440,14`), shown in C8 of `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md`." | S1: E14 vs fresh run (C8) |
| M3 | `-worker1.md` | (inserted block) | 566 | the block intro line as left by build-worker1 | the same line plus: "This block was run before correction-1 appended its two MANIFEST.md rows (:452–453); a fresh run now differs only in the timestamp line and the MANIFEST.md hunk header (`+440,12` becomes `+440,14`), shown in C8 of `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md`." | S1: block vs fresh run (C8) |
| M4 | `-worker2.md` | 13 | 13 | the line as left by build-worker2 (its log row 2, new text), containing "the index holds 1 entry, a pre-existing PNG under `docs/reports/evidence/`," | the same line with that phrase replaced by "the index holds 1 entry, one PNG under `docs/reports/evidence/` (counts in the re-run block)," | adv-1 finding 6: "pre-existing" not shown by counts (C15) |

### Edit log, -manager.md (/tmp/fgdc1/edits-manager.md, verbatim)

#### Edit log — docs/reports/2026-11-12-fgd-doc-alignment-manager.md (unit 2026-11-12-fgd-doc-alignment-correction-1, bead Praxis_build-fgd)

Source: pristine copy /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md (474 lines). Edited file: 818 lines. Edits applied by /tmp/fgdc1/apply-manager.py (exact-string replacements, each asserted to match once on its line). Evidence block E14: script /tmp/fgdc1/ev-manager.sh, output /tmp/fgdc1/ev-manager.out, pasted verbatim. The support rep's first name is masked as [rep-name] in this log (old text of line 96). Pipes inside table cells are escaped as \|.

| # | orig line | new line | old text | new text | reason |
|---|---|---|---|---|---|
| 1 | 5 | 5 | Unit `2026-11-12-fgd-doc-alignment`, decided by master under D-2026-11-08-D D1, changeable by Amear. It carries out D-2026-11-12-A (DECISIONS.md:2205) and Amendment 1 of `docs/specs/2026-11-05-phase3-build-specification.md` for five follow-ups named in `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` :134–142: F-1, F-2 (topology doc), F-3 (Noise-Area ruleset), F-7, F-9 (F2 proposal). Method fixed by the master: one dated, labelled section appended at the end of each file; body lines unchanged; no new design choice; no DECISIONS.md entry. The breakers remain SPECIFIED ONLY (zero implemented, zero tested, zero tested under failure); nothing in this unit changes that. | Unit `2026-11-12-fgd-doc-alignment`, decided by master under D-2026-11-08-D D1, changeable by Amear. It carries out D-2026-11-12-A (DECISIONS.md:2205; E5, E14) and Amendment 1 of `docs/specs/2026-11-05-phase3-build-specification.md` for five follow-ups named in `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` :134–142 (E14): F-1, F-2 (topology doc), F-3 (Noise-Area ruleset), F-7, F-9 (F2 proposal). Method fixed by the master: one dated, labelled section appended at the end of each file; body lines unchanged; no new design choice; no DECISIONS.md entry. The breakers remain SPECIFIED ONLY (zero implemented, zero tested, zero tested under failure); nothing in this unit changes that. | test d/f: cites :2205, :134–142 pointed at pasted lines (E5, E14); manager list :5 |
| 2 | 16 | 16 | \| worker2 \| ADVERSARIAL, narrow re-check of the cures to worker1 findings 1-4 \| Verdict: PASS, 0 breaks, 1 observation (see "Adversarial findings") \| | \| worker2 \| ADVERSARIAL, narrow re-check of the cures to worker1 findings 1-4 \| Verdict: PASS, 0 breaks, 1 observation (worker2 :397, E14; see "Adversarial findings") \| | test c: worker2 '0 breaks, 1 observation' pointed at worker2 :397 (E14) |
| 3 | 18 | 18 | The three notes were written by the manager (pure doc edits, as the master's brief directs: "check your notes"); every old line quoted in them was copied by script (`/tmp/fgd/build.sh`, `git show HEAD:<file> \| sed -n Np`). | The three notes were written by the manager (pure doc edits, as the master's brief directs: "check your notes"); the 16 old body lines quoted in them were copied by script: `/tmp/fgd/build.sh`:8 defines a function `q` that runs `git show "HEAD:$1" \| sed -n "${2}p"`, and build.sh calls it for those 16 lines (E14). | test a: placeholder command `git show HEAD:<file> | sed -n Np` replaced by the literal function from build.sh:8; 'every old line' reduced to the 16 q() calls pasted (E14) |
| 4 | 22 | 22 | 1. Read the follow-up list (F2 amendment report :120–150), D-2026-11-12-A (DECISIONS.md:2205 onward), Amendment 1 (Phase 3 :189–244), the rubric F1/F2 sections, and the three target files in full with line numbers. Every cited line was checked against HEAD; all cited numbers were correct. One extra line found in F-1's subject: topology :78 ("all nine checks move into the strategy"), added to the topology note and labelled as found by this unit. | 1. Read the follow-up list (F2 amendment report :134–142), D-2026-11-12-A (DECISIONS.md:2205–2278, the last entry at HEAD), Amendment 1 (Phase 3 :190–244, heading at :190), the rubric F1/F2 sections, and the three target files in full with line numbers. The cited lines are pasted in E14 (follow-up list, DECISIONS.md, rubric, Phase 3, topology, ruleset, proposal); that pasted set is what is shown, not every line read. One extra line found in F-1's subject: topology :78 ("all nine checks move into the strategy"; E14), added to the topology note and labelled as found by this unit (note line 178, E14). | tests c/d/f: 'Every cited line was checked...all correct' reduced to the pasted set; :120–150 -> :134–142; 'DECISIONS.md:2205 onward' -> :2205–2278; Phase 3 :189–244 -> :190–244 (heading :190; :189 blank); topology :78 quote pasted (E14) |
| 5 | 23 | 23 | 2. Read the trader's 2026-07-16 lock (DECISION_LOG.md:42) and `PraxisNoiseAreaBreakout.cs` (16:00 flat, "trader-locked") for F-3. | 2. Read the trader's 2026-07-16 lock (DECISION_LOG.md:42 at HEAD, E5) and `ninjascript/PraxisNoiseAreaBreakout.cs` :188–191 (16:00 flat, "trader-locked"; E14) for F-3. | test f / auditor item 5: .cs :188–191 '16:00 flat, trader-locked' pasted (E14); DECISION_LOG.md:42 pointed at E5 (HEAD) |
| 6 | 25 | 25 | 4. Defect found and cured by the manager: in the proposal note, line 95, the shell ate the first byte of an en dash after a variable name, leaving invalid UTF-8 (":" followed by two stray bytes, then "94"). Found by `iconv` (proposal: INVALID-utf8), repaired with a byte-level substitution on line 95 only, re-checked: valid UTF-8, body still identical, numstat still 30/0 (E9). | 4. Defect found and cured by the manager: in the proposal note, line 95, the en dash after a variable name lost its first byte in the shell (the manager's account of the cause), leaving invalid UTF-8 (":" followed by two stray bytes, then "94"). The `iconv` detection output was not kept, and it is not reproducible after the repair; no INVALID result is pasted here. Repaired with a byte-level substitution on line 95 only. Only the post-repair results are pasted: valid UTF-8 and the `:93–94` text (E9), body still identical (E3), numstat still 30/0 (E2). | test e / auditor item 3: iconv INVALID detection not kept and not reproducible after repair; only post-repair E9 pasted; numstat pointer corrected E9 -> E2; shell-cause marked as the manager's account |
| 7 | 26 | 26 | 5. MANIFEST rows appended at :446–451 (row :451 for worker2 added after its dispatch) after the 14 pre-existing uncommitted rows (E6). | 5. MANIFEST rows appended at :446–451 (working-tree positions; row :451 is worker2's, E13) after the 14 uncommitted rows of other units at :307–314 and :440–445 (E6, E14). | tests d/e: MANIFEST positions marked working-tree; 'added after its dispatch' event dropped; '14 pre-existing' -> '14 uncommitted rows of other units' with hunks and paths pasted (E14); auditor item 7 |
| 8 | 27 | 27 | 6. ADVERSARIAL worker1 dispatched; its report read on disk (Findings, verdict, last line, placeholder scan). Findings 2-4 cured by the manager with /tmp/fgd/cure.py (exact-string replacement in the appended notes only); E3 and E13 re-prove additions only. 7. ADVERSARIAL worker2 re-checked the cures on the current hashes. | 6. ADVERSARIAL worker1 dispatched; its report read on disk (Findings, verdict, last line, placeholder scan). Findings 2-4 cured by the manager with /tmp/fgd/cure.py (exact-string replacement in the appended notes only; each replacement string now occurs once, E14); E3 proves additions only and E13 gives the hashes after the cures. 7. ADVERSARIAL worker2 re-checked the cures on the current hashes (its sha1s at worker2 :35–37 equal E13; E14). | tests c/e: cure strings pasted (each occurs once, E14); 'E13 re-proves additions only' corrected (E3 proves it; E13 gives hashes); worker2 hashes pointed at worker2 :35–37 |
| 9 | 31 | 31 | \| Follow-up \| Lines checked \| Disposition \| | \| Follow-up \| Lines checked (HEAD text in E14) \| Disposition \| | test c: 'Lines checked' column pointed at the pasted HEAD text (E14) |
| 10 | 33 | 33 | \| F-1 \| topology :41, :48, :62, :74, :86, plus :78 (found here) \| DONE. Note reads the consumer-side checks as #4, #7, #8, #9; #5 has no system check on the path; the #5 row's own conditional ("the n8n/consumer window check is then removed") is in effect because D-2026-11-12-A adopts the proposal text. \| | \| F-1 \| topology :41, :48, :62, :74, :86, plus :78 (found here) \| DONE. Note reads the consumer-side checks as #4, #7, #8, #9; #5 has no system check on the path; the #5 row's own conditional ("the n8n/consumer window check is then removed"; topology :62, E14) is in effect because D-2026-11-12-A adopts the proposal text. \| | test f: quoted '#5 row' phrase located at topology :62 and pasted (E14) |
| 11 | 34 | 34 | \| F-2 \| topology :54, :61, :62 \| DONE. Amended names "Session flat gate" (#4) and "Session window (operator lockout)" (#5) govern; body names kept as written. One OPEN item raised (OPEN-A1, placement of amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)"), two readings, not chosen. \| | \| F-2 \| topology :54, :61, :62 \| DONE. Amended names "Session flat gate" (#4) and "Session window (operator lockout)" (#5) govern; body names kept as written. One OPEN item raised (OPEN-A1, placement of amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)"; Phase 3 :212, E14), two readings, not chosen. \| | test f: amended #4 quotes located at Phase 3 :212 and pasted (E14) |
| 12 | 35 | 35 | \| F-3 \| ruleset :8, :79, :84, :99, :105 \| DONE for the replication strategy, on two prior records: the trader's lock DECISION_LOG.md:42 item (1) "session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)" and D-2026-11-12-A (no breaker forces 11:30). One OPEN item (OPEN-A2): whether a strategy-level 11:30 stop stays available to a later arm; two readings, not chosen. \| | \| F-3 \| ruleset :8, :79, :84, :99, :105 \| DONE for the replication strategy, on two prior records: the trader's lock DECISION_LOG.md:42 item (1) "session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)" (E5) and D-2026-11-12-A (no breaker forces 11:30). One OPEN item (OPEN-A2): whether a strategy-level 11:30 stop stays available to a later arm; two readings, not chosen. \| | test f: DECISION_LOG.md:42 item (1) quote pointed at E5 |
| 13 | 36 | 36 | \| F-7 \| proposal :8 \| DONE. Unblock clause re-pointed to `specs/SPEC_RUBRIC.md`:93–94 at `006a08b` (was :30–31 at `e3323a8`; F2 moved to PASSED at `c29d08b`); A6 citation :1744–1745 verified unchanged. \| | \| F-7 \| proposal :8 \| DONE. Unblock clause re-pointed to `specs/SPEC_RUBRIC.md`:93–94 at `006a08b` (E5; was :30–31 at `e3323a8`, E14; F2 moved to PASSED at `c29d08b`, E9); A6 citation :1744–1745 unchanged (proposal :8 and DECISIONS.md:1744–1745 at HEAD, E14). \| | tests c/d/f: rubric :30–31 at e3323a8 pasted (E14); 'A6 citation :1744–1745 verified unchanged' -> 'unchanged' with proposal :8 and DECISIONS.md:1744–1745 pasted (E14) |
| 14 | 37 | 37 | \| F-9 \| proposal :79 (read with :3) \| DONE. OPEN-F2-5 recorded as closed: each step in its own "What would decide it" column has a record (D-2026-11-11-A V2 at :2108; D-2026-11-12-A at :2205; Amendment 1); rubric F2 PASSED@e3323a8. D-2026-11-12-A's limits carried: approval given on a summary; #4/#5 text is the master's adoption under D1; whether the approval reaches that text, and whether A6 is triggered, not graded. \| | \| F-9 \| proposal :79 (read with :3) \| DONE. OPEN-F2-5 recorded as closed: each step in its own "What would decide it" column has a record (D-2026-11-11-A V2 at :2108; D-2026-11-12-A at :2205; Amendment 1; E11, E14); rubric F2 PASSED@e3323a8 (E5). D-2026-11-12-A's limits carried: approval given on a summary; #4/#5 text is the master's adoption under D1; whether the approval reaches that text, and whether A6 is triggered, not graded. \| | test d: :2108, :2205, Amendment 1 and F2 state pointed at E11, E14, E5 |
| 15 | 41 | 41 | - OPEN-A1 (topology note). Where amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" sit on the live path. (a) inside the FLATTEN command the consumer executes; (b) a separate n8n-side account-state check (needs OPEN-T3's feed). | - OPEN-A1 (topology note). Where amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (Phase 3 :212, E14) sit on the live path. (a) inside the FLATTEN command the consumer executes; (b) a separate n8n-side account-state check (needs OPEN-T3's feed). | test f: amended #4 quotes pointed at Phase 3 :212 (E14) |
| 16 | 42 | 42 | - OPEN-A2 (ruleset note). Whether a strategy-level 11:30 stop remains available to a later Noise-Area arm. (a) No: lock item (1) and Rule F2-1's entries-until-16:00 carry the full-day window to every arm. (b) Yes, as that arm's own design choice: lock item (3) scopes the "FIRST build" to replication, and Rule F2-1 sets only the latest flat (proposal :24). | - OPEN-A2 (ruleset note). Whether a strategy-level 11:30 stop remains available to a later Noise-Area arm. (a) No: lock item (1) and Rule F2-1's entries-until-16:00 carry the full-day window to every arm. (b) Yes, as that arm's own design choice: lock item (3) scopes the "FIRST build" to replication (E5), and Rule F2-1 sets only the latest flat (proposal :24, E14). | tests d/f: lock item (3) -> E5; proposal :24 pasted (E14) |
| 17 | 44 | 44 | New follow-ups observed, not fixed (outside the five): other rubric line citations that moved when F1/F2 moved to PASSED — proposal :61 (O4 cited at :108–113; O4 heading is now :114), proposal :69 (F2 "Why frozen" cited at :37–42; now :87 onward), topology :7 (F1 unblock cited at :28–29; now :75–76), topology :112 (cited :30; F1 "Blocks" line now :77). See E10. | New follow-ups observed, not fixed (outside the five): other rubric line citations that moved when F1/F2 moved to PASSED — proposal :61 (O4 cited at :108–113; O4 heading is now :114), proposal :69 (F2 "Why frozen" cited at :37–42; now :87 onward), topology :7 (F1 unblock cited at :28–29; now :75–76, E14), topology :112 (cited :30; F1 "Blocks" line now :77). See E10. | test d: rubric F1 unblock :75–76 pasted (E14) |
| 18 | 48 | 48 | E4 below: each of the nine Phase 3 body names (:97–105) occurs in the topology doc (counts 1, 1, 1, 3, 3, 1, 1, 2, 1), the breaker table :58–66 still lists all nine in order, and the amended names "Session flat gate" and "Session window (operator lockout)" (Phase 3 :212, :224) each occur 3 times, all in the note. Bearing, not a grade: amended #5 no longer sits on the signal path at all, so F1's "showing how each of the nine circuit breakers sits upstream of order submission" now reads, for #5, through #4 (system half) and B3/OPEN-T8 (lockout). Whether F1 needs re-grading is the master's call. | E4 below: each of the nine Phase 3 body names (:97–105, E14) occurs in the topology doc (counts 1, 1, 1, 3, 3, 1, 1, 2, 1), the breaker table :58–66 still lists all nine in order, and the amended names "Session flat gate" and "Session window (operator lockout)" (Phase 3 :212, :224) each occur 3 times, all in the note (note lines 124–168, E14). Bearing, not a grade: amended #5 no longer sits on the signal path at all, so F1's "showing how each of the nine circuit breakers sits upstream of order submission" (rubric :68–69, E14) now reads, for #5, through #4 (system half) and B3/OPEN-T8 (lockout). Whether F1 needs re-grading is the master's call. | tests d/f: Phase 3 :97–105 pasted; 'all in the note' backed by note line numbers 124–168; F1 criterion quote at rubric :68–69 pasted (E14) |
| 19 | 52 | 52 | Source of hits: `/tmp/fgd/s6.sh` (git grep at HEAD, excluding the F2 amendment reports that list F-1 to F-9); its full output is pasted under E11. Nothing listed here was edited. | Source of hits: `/tmp/fgd/s6.sh` (git grep at HEAD, excluding the F2 amendment reports that list F-1 to F-9); its full output is pasted under E11; s6.sh cuts each hit line to 230 characters (`cut -c1-230`, E14). Nothing listed here was edited. | sweep (test b): E11's lines are cut to 230 chars inside s6.sh, not in the shown command; cut disclosed and pasted (E14) |
| 20 | 61 | 61 | \| DECISIONS.md:2247 (D-2026-11-12-A) \| other specs cite topology :24, :61, :89, so no body line may shift \| agrees (no body line moved, E3) \| | \| DECISIONS.md:2247 (D-2026-11-12-A) \| other specs cite topology :24, :61, :89, so no body line may shift (E14) \| agrees (no body line moved, E3) \| | test f: DECISIONS.md:2247 phrase pasted (E14) |
| 21 | 62 | 62 | \| Phase 3 :244 (Amendment 1) \| placement of #4/#5 is in topology section 3, "which this amendment does not edit" \| agrees (section 3 body still unedited; the note reads it under Amendment 1) \| | \| Phase 3 :244 (Amendment 1) \| placement of #4/#5 is in topology section 3, "which this amendment does not edit" (E14) \| agrees (section 3 body still unedited; the note reads it under Amendment 1) \| | test f: Phase 3 :244 phrase pasted (E14) |
| 22 | 63 | 63 | \| proposal :40 \| "if adopted, the system window check is removed and only the operator lockout remains" \| agrees (the note records the condition as met) \| | \| proposal :40 \| "if adopted, the system window check is removed and only the operator lockout remains" (E14) \| agrees (the note records the condition as met) \| | test f: proposal :40 quote pasted (E14) |
| 23 | 64 | 64 | \| rubric F1 :63, :75–76 \| nine breakers by name \| bearing, see F1 check \| | \| rubric F1 :63 (filer's note), :75–76 (unblock clause) \| nine breakers by name (E14) \| bearing, see F1 check \| | test d: rubric :63 checked (F1 filer's note, contains 'nine breakers by name'; F1 heading is :65) and :75–76 pasted (E14); labels added |
| 24 | 72 | 72 | \| `docs/reports/2026-11-09-d11-sweep-manager.md`:266, :2076, :2079 (W4-11) \| ruleset :105 and :79; closes the backtest flat via R1; says "the live 11:30 flat is breaker #4" \| agrees on the backtest flat; its "live 11:30 flat is breaker #4" sentence conflicts with D-2026-11-12-A (dated report, not edited) \| | \| `docs/reports/2026-11-09-d11-sweep-manager.md`:266, :2076, :2079 (W4-11) \| ruleset :105 and :79; closes the backtest flat via R1; says "the live 11:30 flat is breaker #4" (:266, E14) \| agrees on the backtest flat; its "live 11:30 flat is breaker #4" sentence conflicts with D-2026-11-12-A (dated report, not edited) \| | test f: d11 :266 quote pasted (E14) |
| 25 | 73 | 73 | \| `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191 (not a citation; the code) \| 16:00 flat, "trader-locked" \| agrees (WRITTEN, backtested; not edited) \| | \| `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191 (not a citation; the code) \| 16:00 flat, "trader-locked" (E14) \| agrees (WRITTEN, backtested; not edited) \| | test f / auditor item 5: .cs :188–191 pasted (E14) |
| 26 | 79 | 79 | \| DECISIONS.md:2272 (D-2026-11-12-A) \| proposal :8 cites :43–44; clause "is at :30–31" \| agrees as of `e3323a8`; as a current pointer it is stale (clause now :93–94); append-only, not edited \| | \| DECISIONS.md:2272 (D-2026-11-12-A) \| proposal :8 cites :43–44; clause "is at :30–31" (E14) \| agrees as of `e3323a8`; as a current pointer it is stale (clause now :93–94); append-only, not edited \| | test f: DECISIONS.md:2272 'is at :30–31' pasted (E14) |
| 27 | 80 | 80 | \| DECISION_LOG.md:830; HANDOFF.md:90; `docs/reports/2026-11-11-v-rulings-filing-manager.md`:173; `docs/reports/2026-11-11-v-rulings-filing-worker1.md`:311 \| ":43–44 should be :30–31" \| conflicts as a current pointer (now :93–94); dated records, not edited \| | \| DECISION_LOG.md:830; HANDOFF.md:90; `docs/reports/2026-11-11-v-rulings-filing-manager.md`:173; `docs/reports/2026-11-11-v-rulings-filing-worker1.md`:311 \| that proposal :8's :43–44 is at :30–31 (paraphrase, not a quotation; each line's wording in E14) \| conflicts as a current pointer (now :93–94); dated records, not edited \| | test f: ':43–44 should be :30–31' is not literal text in any of the four lines; changed to a marked paraphrase, each line's wording pasted (E14) |
| 28 | 81 | 81 | \| DECISIONS.md:2108 (D-2026-11-11-A V2) \| "OPEN-F2-5 is not closed by this entry" \| agrees (that entry did not close it; the note closes it after D-2026-11-12-A) \| | \| DECISIONS.md:2108 (D-2026-11-11-A V2) \| "OPEN-F2-5 is not closed by this entry" (E14) \| agrees (that entry did not close it; the note closes it after D-2026-11-12-A) \| | test f: DECISIONS.md:2108 quote pasted (E14) |
| 29 | 82 | 82 | \| `docs/reports/2026-11-11-v-rulings-filing-manager.md`:181; `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md`:361–362; v-rulings worker3/5/6/7/10 rows quoting proposal :79 \| OPEN-F2-5 open at their date \| agrees as of their date (historical) \| | \| `docs/reports/2026-11-11-v-rulings-filing-manager.md`:181; `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md`:361–362; v-rulings worker3/5/6/7/10 rows quoting proposal :79 \| OPEN-F2-5 open at their date (E11, E14) \| agrees as of their date (historical) \| | test d: v-rulings manager :181 and mffu-prepurchase :361–362 pasted (E14) |
| 30 | 83 | 83 | \| rubric F2 filer note :79 \| F2 PASSED, residuals in bead fgd \| agrees \| | \| rubric F2 filer note :79 \| F2 PASSED, residuals in bead fgd (E14) \| agrees \| | test d/f: rubric :79 filer note 'bead Praxis_build-fgd' pasted (E14) |
| 31 | 87 | 87 | Every block below is the literal output of the evidence scripts /tmp/fgd/evidence.sh, /tmp/fgd/evidence2.sh and /tmp/fgd/e13.sh (each prints the command, then its full output and exit code), all re-run after every edit of this unit. | Blocks E1–E13 below are the output of the evidence scripts /tmp/fgd/evidence.sh, /tmp/fgd/evidence2.sh and /tmp/fgd/e13.sh (each prints the command, then its full output and exit code). Before correction-1 masked one filename in E1, E1–E13 were byte-identical to those scripts' saved outputs, written at 08:25:05–08:25:06, after the last modification of the three spec files (08:19:44) and MANIFEST.md (08:24:38) (E14). A re-run after every edit of this unit is not shown by pasted output. E14 is correction-1's re-run. | test e: 're-run after every edit' event claim removed; replaced by pasted cmp (pre-correction E1–E13 byte-identical to saved outputs) and mtimes (E14) |
| 32 | 96 | 96–97 | `docs/reports/evidence/2026-10-28-mffu-[rep-name]-reply.png` | `docs/reports/evidence/2026-10-28-mffu-[rep-name]-reply.png` + inserted line 97: `[correction-1, 2026-11-12: the support rep's first name in this filename is masked as [rep-name]; the actual output carried the name]` | auditor item 6 (MAJOR, de-identification): rep's first name in pasted filename masked by script (python3 -I, pattern read from /tmp/fgdc1/rep.txt); one correction line inserted after it |
| 33 | after 433 (between orig 433 blank and 434 closing fence) | 435–777 | (none) | +343 lines: evidence block E14 (342 lines of /tmp/fgdc1/ev-manager.sh output, new :435–776, plus one blank :777) | instruction: one labelled re-run block inside the fence after E13; script /tmp/fgdc1/ev-manager.sh, output /tmp/fgdc1/ev-manager.out |
| 34 | 438 | 782 | worker1 (`docs/reports/2026-11-12-fgd-doc-alignment-worker1.md`, ADVERSARIAL, `Verdict: PASS` at its line 573, graded on sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3`). Its report was read on disk (Findings section, verdict line, last line) and scanned for placeholders. Dispositions: | worker1 (`docs/reports/2026-11-12-fgd-doc-alignment-worker1.md`, ADVERSARIAL, `Verdict: PASS` at its line 562 (E13, E14), graded on sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3` (its lines 86–88, E14)). Its report was read on disk (Findings section, verdict line, last line) and scanned for placeholders. Dispositions: | auditor items 1 and sweep: worker1 verdict line 573 -> 562 (grep -n on orig copy, E14); sha1 prefixes pointed at worker1 :86–88 (E14) |
| 35 | 440 | 784 | 1. MAJOR, observed and already cured: proposal note line 95 held invalid UTF-8 where `:93–94` should be. This is the defect the manager found and repaired during the review (process log step 4; E9). The repair was the manager's edit (worker1 could not tell who made it). | 1. MAJOR, observed and already cured: proposal note line 95 held invalid UTF-8 where `:93–94` should be. This is the defect the manager found and repaired during the review (process log step 4; E9). The repair was the manager's edit (worker1 could not tell who made it: its line 552, E14). | test f: 'could not tell who made it' pointed at worker1 :552 (E14) |
| 36 | 441 | 785 | 2. MINOR, topology note aligned reading for :41, "D-2026-11-12-A adopts that text". Cured: now reads that D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232) and that proposal :40 states the window check is then removed. | 2. MINOR, topology note aligned reading for :41, "D-2026-11-12-A adopts that text". Cured: now reads that D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232) and that proposal :40 states the window check is then removed (E14). | test d/f: DECISIONS.md:2232 and proposal :40 pasted (E14) |
| 37 | 442 | 786 | 3. MINOR, topology note aligned reading for :78, "its operator lockout cannot sit in the strategy either". Cured: now leaves where the lockout sits, including whether the strategy could carry it, to OPEN-T8 (:105), not decided here. | 3. MINOR, topology note aligned reading for :78, "its operator lockout cannot sit in the strategy either". Cured: now leaves where the lockout sits, including whether the strategy could carry it, to OPEN-T8 (:105), not decided here (E14). | test d: OPEN-T8 at topology :105 pasted (E14) |
| 38 | 443 | 787 | 4. MINOR, proposal note :79 lead sentence unqualified. Cured: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits." | 4. MINOR, proposal note :79 lead sentence unqualified. Cured: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits." (E14) | test f: cure quote pasted (count 1, E14) |
| 39 | 446 | 790 | worker2 (`docs/reports/2026-11-12-fgd-doc-alignment-worker2.md`, ADVERSARIAL narrow re-check of cures 1–4, `Verdict: PASS`, 0 breaks, 1 observation). Its current-file sha1s: topology `5865a1121cd1`, ruleset `b68c098f4aa1`, proposal `24598c3d73d8`; these match the `shasum` output in E13 below. Its observation: D-2026-11-12-A never names OPEN-F2-5, so "closed" is the note's own reading of the three records the item's own column names; recorded here as a residual, not changed (the master's brief asks for the F-9 closure). | worker2 (`docs/reports/2026-11-12-fgd-doc-alignment-worker2.md`, ADVERSARIAL narrow re-check of cures 1–4, `Verdict: PASS`, 0 breaks, 1 observation). Its current-file sha1s: topology `5865a1121cd1`, ruleset `b68c098f4aa1`, proposal `24598c3d73d8` (worker2 :35–37, E14); these match the `shasum` output in E13 below. Its observation (worker2 :374, E14): D-2026-11-12-A never names OPEN-F2-5 (DECISIONS.md:2204–2278 at HEAD has 0 hits, E14), so "closed" is the note's own reading of the three records the item's own column names; recorded here as a residual, not changed (the master's brief asks for the F-9 closure). | test d/f: worker2 sha1s at worker2 :35–37; observation at worker2 :374; D-2026-11-12-A 0 OPEN-F2-5 hits pasted (E14) |
| 40 | 448 | 792 | Residual on the evidence rules, stated honestly: worker1's Findings prose (its lines 564 and 566) quotes note text with "..." elisions inside quotation marks. Those are quotations in prose, not commands and not cut output; its commands and outputs carry no `...` or `<…>` placeholders (E13 scan). The worker report was not edited by the manager. | Residual on the evidence rules, stated honestly: worker1's Findings prose (its lines 553 and 555 in the pre-correction copy, E14) quotes note text with "..." elisions inside quotation marks. Those are quotations in prose, not commands and not cut output; its commands and outputs carry no `...` or `<…>` placeholders (E13 scan; E14: every line with `...` is outside a fence, including one more prose elision at its line 314, outside Findings). The worker report was not edited by the manager. | auditor item 2: worker1 elision lines 564/566 -> 553/555 (orig copy, E14); E13 scan scope corrected with the fence check (E14), which also shows a third prose elision at :314 |
| 41 | 455 | 799 | - `MANIFEST.md` — 6 rows appended at :446–451 after the 14 pre-existing uncommitted rows (diff vs HEAD now 20 added, 0 removed: 14 pre-existing + 6 this unit). | - `MANIFEST.md` — 6 rows appended at :446–451 (working-tree positions) after the 14 uncommitted rows of other units (diff vs HEAD now 20 added, 0 removed: 14 of other units + 6 this unit; E2, E14). | tests d/e: working-tree positions; '14 pre-existing' -> '14 of other units' (E2, E14) |
| 42 | 458 | 802 | Not edited: DECISIONS.md, specs/SPEC_RUBRIC.md, the Phase 3 spec, the walk-forward spec and values, ninjascript/, ledgers, .claude/ (E8: the modified paths in that set are exactly the ones in the session-start git status snapshot). | Not edited: DECISIONS.md, specs/SPEC_RUBRIC.md, the Phase 3 spec, the walk-forward spec and values, ninjascript/, ledgers, .claude/ (E8 lists the paths in that set that differ from HEAD; specs/SPEC_RUBRIC.md, the Phase 3 spec, ninjascript/, HANDOFF.md and STATUS.md show no diff, E14. For the paths that do differ, no session-start snapshot was pasted, so that this unit did not edit them is not shown by pasted output.) | tests c/e: 'exactly the ones in the session-start git status snapshot' had no paste; reduced to what E8 and E14 show |
| 43 | 462 | 806 | MANIFEST.md:446 (topology), :447 (ruleset), :448 (proposal), :449 (this report), :450 (worker1), :451 (worker2). Output in E6 and E13. | MANIFEST.md:446 (topology), :447 (ruleset), :448 (proposal), :449 (this report), :450 (worker1), :451 (worker2), working-tree positions. Output in E6, E13 and E14. | auditor item 7: working-tree positions; E14 added |
| 44 | 466 | 810 | None by this unit. The index holds only the pre-existing PNG (E1). The master builds the index. | None by this unit. The index holds one path, the PNG listed in E1. The master builds the index. | test e: 'pre-existing PNG' reduced to what E1 shows |

#### Hunk check

Plain `diff orig new` aligns the E14 insert against orig :434–:449 and so prints shifted hunks (434c435,436 … 449a589,793). With the two inserted spans removed (new :97 and :435–:777), every remaining hunk is a one-for-one line change at exactly the orig lines in rows 1–32 and 34–44:

```text
$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md <(sed -e '97d' -e '435,777d' docs/reports/2026-11-12-fgd-doc-alignment-manager.md) | grep -E '^[0-9]' | tr '\n' ' '
5c5 16c16 18c18 22,23c22,23 25,27c25,27 31c31 33,37c33,37 41,42c41,42 44c44 48c48 52c52 61,64c61,64 72,73c72,73 79,83c79,83 87c87 96c96 438c438 440,443c440,443 446c446 448c448 455c455 458c458 462c462 466c466 
```

### Edit log, -worker1.md (/tmp/fgdc1/edits-worker1.md, verbatim)

#### Edit log — docs/reports/2026-11-12-fgd-doc-alignment-worker1.md (unit 2026-11-12-fgd-doc-alignment-correction-1)

Pristine: /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md (564 lines). Edited: 748 lines. Lines 1-563 keep their numbers; every edit there is one line replaced by one line.

| # | orig line | new line | old text (verbatim, full line) | new text (verbatim, full line or block summary) | reason |
|---|---|---|---|---|---|
| 1 | 5 | 5 | Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A). Mode: ADVERSARIAL. HEAD `006a08b`, branch main. Artifact: three appended sections headed "## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)" in `docs/specs/2026-11-10-live-signal-topology.md` (body 1–114), `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (body 1–111) and `docs/specs/2026-11-10-f2-session-flat-proposal.md` (body 1–81), plus the MANIFEST.md fgd rows. Governing sources: D-2026-11-12-A (DECISIONS.md:2205 to the line before :2280), Amendment 1 of the Phase 3 spec, Rule F2-1 (proposal :20) and the 15:00 disposition (proposal :30), rubric F1/F2 (:63–97), DECISION_LOG.md:42. Six attacks, from the brief. Nothing was staged, committed or edited apart from this report. | Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A). Mode: ADVERSARIAL. HEAD `006a08b`, branch main. Artifact: three appended sections headed "## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)" in `docs/specs/2026-11-10-live-signal-topology.md` (body 1–114), `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (body 1–111) and `docs/specs/2026-11-10-f2-session-flat-proposal.md` (body 1–81), plus the MANIFEST.md fgd rows. Governing sources: D-2026-11-12-A (DECISIONS.md:2205 to the line before :2280 in the working tree; at HEAD it runs from :2205 to the file's last line, :2278, E-4), Amendment 1 of the Phase 3 spec, Rule F2-1 (proposal :20) and the 15:00 disposition (proposal :30) (E-3), rubric F1/F2 (:63–97 at HEAD, E-3), DECISION_LOG.md:42 (same at HEAD and in the working tree, E-4). Six attacks, from the brief. Nothing was staged, committed or edited apart from this report. Line numbers in DECISIONS.md, DECISION_LOG.md and MANIFEST.md are working-tree lines as read during the review; "E-n" means a block in "Correction-1 re-run evidence (2026-11-12)" at the end of this report. | test d (state working tree vs HEAD for DECISIONS.md/DECISION_LOG.md/MANIFEST.md; HEAD end :2278) and test d/f (proposal :20, :30 and rubric :63-97 now pasted in E-3); defines E-n references |
| 2 | 7 | 7 | **The artifact changed while I was reviewing it.** At my first read the proposal file held invalid UTF-8 at line 95 (C3a). When I checked again, its mtime was 2026-11-12T08:12:44, and the topology and ruleset files had mtime 08:10:48 (C3b). I re-ran every check on the current files at 08:15:12 (C1c, C2a). The grades below are for the files with these hashes: topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3` (C1c). | **The artifact changed while I was reviewing it.** At my first read the proposal file held invalid UTF-8 at line 95 (C3a). When I checked again, its mtime was 2026-11-12T08:12:44, and the topology and ruleset files had mtime 08:10:48 (C3b). I re-ran the checks shown in C1c on the current files at 08:15:12 (C1c; C2a reads its output). The grades below are for the files with these hashes: topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3` (C1c). | test e: 'I re-ran every check' had no paste for every check; reduced to the C1c checks actually pasted |
| 3 | 51 | 51 | MANIFEST has two insertion hunks: 8 lines at 307–314 from another unit, and 11 at 440–450. Rows 446–450 are this unit's (C6). The whole-file cmp fails on MANIFEST because of the insertion at 307 (C1b). That is expected and is not a finding against this unit. | At review time (working tree), MANIFEST had two insertion hunks: 8 lines at 307–314 from another unit (wf-spec-amendment rows dated 2026-11-08 and 2026-11-09, E-5), and 11 at 440–450. Rows 446–450 are this unit's (C4, C6). Since the review, row 451 was added and the second hunk is now 12 lines (E-5). The whole-file cmp fails on MANIFEST because of the insertion at 307 (C1b). That is expected and is not a finding against this unit. | test d (MANIFEST is working tree; hunk 2 is now 12 lines) and test c ('from another unit' now pasted in E-5); C6 citation widened to C4, which holds rows 440-450 |
| 4 | 119 | 119 | `/tmp/fgdchk/quotes.py` takes each fenced text block in each note and string-compares it with `git show HEAD:<file>` at the line named by the preceding `### :N` heading. For the proposal's `:3` block it uses the line named by "Read with :3". Output is in C1c: 16 of 16 blocks byte-identical=True. | `/tmp/fgdchk/quotes.py` takes each fenced text block in each note and string-compares it with that file's HEAD blob (`git show HEAD:` plus the file's path) at the line named by the preceding `### :N` heading. For the proposal's `:3` block it uses the line named by "Read with :3". Output is in C1c: 16 of 16 blocks byte-identical=True. The script text is pasted in E-6. | test a: `git show HEAD:<file>` placeholder removed; script description now backed by the script text in E-6 (test c) |
| 5 | 121 | 121 | The two "False" lines are a bug in my script, not in the note. The script adds a `> ` prefix, but the Phase 3 lines already start with `> `. C2b is the correct byte comparison. | The two "False" lines are a bug in my script, not in the note. The script adds a `> ` prefix (`q=='> '+p3[cite-1]`, E-6), but the Phase 3 lines already start with `> ` (C2c). C2b is the correct byte comparison. | test c: the script's '> ' prefix claim now points at the pasted script line (E-6) |
| 6 | 188 | 188 | - every DECISION_LOG.md:42 fragment the ruleset note quotes, including WHO. | - every DECISION_LOG.md:42 fragment the ruleset note quotes, including WHO (the quoting line, ruleset :121, is pasted in E-8). | test f: the ruleset note's quoting line (:121) pasted in E-8 |
| 7 | 190 | 190 | ### C2e — DECISIONS.md citations (:2108, :1551, :1744–1745) | ### C2e — DECISIONS.md citations (:2108, :1551, :1744–1745); the first paste below lacks the blank line :2260 that its `sed -n '2260,2279p'` prints first (E-4) | test b: C2e's first paste shows 19 of the 20 lines `sed -n '2260,2279p'` prints (blank :2260 missing); stated in place, E-4 shows :2260 blank |
| 8 | 314 | 314 | The note covers every topology body line that places #5 as a system check: :41, :48, :62, :74, :78 (which the unit found itself) and :86. :88 already keeps #5's lockout off the path, and :112 names only "rubric F2 (... #4/#5)". Neither needs a reading. | The note covers every topology body line that places #5 as a system check: :41, :48, :62, :74, :78 and :86 (E-7 pastes the matching fragment of each). :88 already keeps #5's lockout off the path, and :112 names only "rubric F2 (... #4/#5)". Neither needs a reading. | test e/c: '(which the unit found itself)' unsupported, removed; #5 fragments of each listed body line pasted in E-7 |
| 9 | 348 | 348 | Topology :105 is OPEN-T8, as the note cites. In the ruleset, only :31 is outside the note's set, and :31 is the lookback window, which has nothing to do with the session. The five F-3 lines are exactly :8, :79, :84, :99 and :105, and the note covers all five. | Topology :105 is OPEN-T8, as the note cites. In the ruleset, only :31 is outside the note's set, and :31 is the lookback window, which has nothing to do with the session. The other five lines the grep finds are :8, :79, :84, :99 and :105, and the note covers all five (C1c). This report does not paste follow-up F-3's own text, so it does not grade F-3's list against them. | test c/f: 'The five F-3 lines are exactly' claimed F-3's list without pasting it; reduced to what the grep shows |
| 10 | 374 | 374 | At that read, the F-7 citation was `` `specs/SPEC_RUBRIC.md`: `` followed by bytes `80 93` and then `94`. The digits "93" and the en-dash lead byte `e2` were missing, so the line number F-7 exists to fix was unreadable, and the file was not valid UTF-8. My first quote-script run then crashed on this file: `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 13567: invalid start byte`. | At that read, the F-7 citation was `` `specs/SPEC_RUBRIC.md`: `` followed by bytes `80 93` and then `94` (the python output above). The digits "93" and the en-dash lead byte `e2` were missing, so the line number F-7 exists to fix was unreadable, and the file was not valid UTF-8. The command's last segment, the `grep`/`od -c`/`sed -n 1,12p` pipe, has no output in the paste above; that output was not kept. Its re-run (E-1) shows the repaired file only, not the pre-repair bytes, and its 12-row `od` window ends inside line 92, before line 95. A first quote-script run on this file is not evidenced here: its error output was not kept, and it is not reproducible after the repair. | auditor findings 1 and 2: the UnicodeDecodeError was never pasted and is not reproducible after the repair (reworded, `...`-free); the C3a grep/od/sed segment's output was not in the paste, now re-run as E-1, labelled post-repair |
| 11 | 454 | 454 | The pattern script is `/tmp/fgdchk/deid.py`. Its terms are not reproduced here. It scans only the appended lines of each file: topology from line 115, ruleset from 112, proposal from 82. | The pattern script is `/tmp/fgdchk/deid.py`. Its terms are not reproduced here. It scans only the appended lines of each file: topology from line 115, ruleset from 112, proposal from 82 (offsets 114, 111, 81 and the slice `[n:]`, E-6). | test c: description of deid.py's scan range now backed by E-6 (offsets and slice) |
| 12 | 494 | 494 | The only person name is Amear. "Sharpe" is the ratio, inside the quoted body line :105, and is not a paper author. "Users" is the `/Users/admin` path, inside the quoted body line :86. Attack 6: PASS. | The only person name is Amear. "Sharpe" is the ratio, inside the quoted body line :105 (E-7), and is not a paper author. "Users" is the `/Users/admin` path, inside the quoted body line :86. Attack 6: PASS. | test f: ruleset :105 'Sharpe' fragment pasted in E-7 |
| 13 | 544 | 544 | 2. Quoted old lines: **PASS**, 16/16 byte-identical, plus Phase 3 :212/:224 (C1c, C2b). Other citations checked and correct: DECISIONS.md:2205, :2108, :1551, :1744–1745 (C2e, C2f); Phase 3 :212, :224 (C2c); SPEC_RUBRIC.md :93–94, :81, :30–31@e3323a8 (C2d); DECISION_LOG.md:42 (C2d); proposal :24, :30 (C2g, C2f); topology :105 (C2h). The F-7 citation was broken at first read (Finding 1) and is now correct. | 2. Quoted old lines: **PASS**, 16/16 byte-identical, plus Phase 3 :212/:224 (C1c, C2b). Other citations checked and correct: DECISIONS.md:2205, :2108, :1551, :1744–1745 (C2e, C2f); Phase 3 :212, :224 (C2c); SPEC_RUBRIC.md :93–94, :81, :30–31@e3323a8 (C2d); DECISION_LOG.md:42 (C2d); proposal :24, :20, :30 (C2g, E-3); topology :105 (C2h). The F-7 citation was broken at first read (Finding 1) and is now correct. | test d/f: proposal :30 was cited to C2f, which shows DECISIONS.md quoting it, not the proposal line; E-3 cmp's proposal :20 and :30 against the C2f-pasted DECISIONS.md lines |
| 14 | 553 | 553 | 2. **MINOR — topology :136 (aligned reading for :41).** "...('the n8n/consumer window check is then removed'); D-2026-11-12-A adopts that text." Read naturally, "that text" is the topology :62 row text. D-2026-11-12-A adopts something else, "The proposal's replacement text for breakers #4 and #5" (DECISIONS.md:2232). The same entry also says the topology document is not edited (:2274). Removing the check follows from the adopted #5 text, through proposal :40. Fix: "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232); proposal :40 states that, if adopted, the system window check is removed." | 2. **MINOR — topology :136 in the graded version, sha1 `5aea715d2ff4` (aligned reading for :41; source line in E-2).** "...('the n8n/consumer window check is then removed'); D-2026-11-12-A adopts that text." Read naturally, "that text" is the topology :62 row text (E-7). D-2026-11-12-A adopts something else, "The proposal's replacement text for breakers #4 and #5" (DECISIONS.md:2232). The same entry also says the topology document is not edited (:2274). Removing the check follows from the adopted #5 text, through proposal :40. Fix: "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232); proposal :40 states that, if adopted, the system window check is removed." | test d: appended-note line :136 states its version (sha1 5aea715d2ff4); test f: source line pasted in E-2, body :62 fragment in E-7 |
| 15 | 554 | 554 | 3. **MINOR — topology :184 (aligned reading for :78).** "its operator lockout cannot sit in the strategy either (B3, OPEN-T8)." B3 (:88) says "Nothing on this path can gate a human order", and "this path" is option 1's. OPEN-T8 (:105) leaves the enforcement open ("Block 3 design under D1"), and D-2026-11-12-A does not decide it (:2274). Ruling out a strategy-resident lockout narrows OPEN-T8 without a source. Fix: "#5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105)." | 3. **MINOR — topology :184 in the graded version, sha1 `5aea715d2ff4` (aligned reading for :78; source line in E-2).** "its operator lockout cannot sit in the strategy either (B3, OPEN-T8)." B3 (:88) says "Nothing on this path can gate a human order", and "this path" is option 1's (E-9). OPEN-T8 (:105) leaves the enforcement open ("Block 3 design under D1"), and D-2026-11-12-A does not decide it (:2274). Ruling out a strategy-resident lockout narrows OPEN-T8 without a source. Fix: "#5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105)." | test d: appended-note line :184 states its version (sha1 5aea715d2ff4); test f: source line pasted in E-2; 'this path is option 1's' backed by E-9 |
| 16 | 555 | 555 | 4. **MINOR — proposal :103 (F-9).** The note opens "OPEN-F2-5 is closed." without qualification. The item's decider is "Amear's approval under A6; then ... the amended #4/#5 text". D-2026-11-12-A records that "whether A6 is triggered is not graded here" (DECISIONS.md:2272). It also records that whether his approval reaches element (f), the #4/#5 text, is ungraded (:2249). The note carries both limits in the same paragraph, so this is not a false claim, but the lead sentence states the result at a higher level than its own caveats. Fix: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits:" | 4. **MINOR — proposal :103 in the graded version, sha1 `e1d2d72895b3` (F-9; source line in E-2).** The note opens "OPEN-F2-5 is closed." without qualification. The item's decider is "Amear's approval under A6; then ... the amended #4/#5 text". D-2026-11-12-A records that "whether A6 is triggered is not graded here" (DECISIONS.md:2272). It also records that whether his approval reaches element (f), the #4/#5 text, is ungraded (:2249). The note carries both limits in the same paragraph, so this is not a false claim, but the lead sentence states the result at a higher level than its own caveats. Fix: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits:" | test d: appended-note line :103 states its version (sha1 e1d2d72895b3); test f: source line pasted in E-2 |
| 17 | 556 | 556 | 5. **MINOR (process) — the artifact changed during adversarial review.** Topology and ruleset mtime 2026-11-12T08:10:48; proposal 08:12:44 (C3b). My first reads came before at least the proposal edit (C3a and C3b differ). I re-ran every check at 08:15:12 (C1c). The grade binds only to sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3`. Fix: the manager should confirm the staged blobs match these hashes, or send any later edit for a fresh check. | 5. **MINOR (process) — the artifact changed during adversarial review.** Topology and ruleset mtime 2026-11-12T08:10:48; proposal 08:12:44 (C3b). My first reads came before at least the proposal edit (C3a and C3b differ). I re-ran the C1c checks at 08:15:12 (C1c). The grade binds only to sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3`. Fix: the manager should confirm the staged blobs match these hashes, or send any later edit for a fresh check. At correction-1 the topology and proposal are `5865a1121cd1` and `24598c3d73d8` and the ruleset is unchanged (E-2), so this grade does not cover the current topology and proposal. | test e: 'I re-ran every check' reduced to the C1c checks; S2: notes the current topology/proposal hashes differ from the graded ones (E-2) |
| 18 | (between 563 and 564) | 564-747 | (none: insertion) | +184 lines: evidence block 'Correction-1 re-run evidence (2026-11-12)', E-1 to E-9, output of /tmp/fgdc1/ev-worker1.sh pasted verbatim inside a 4-backtick fence (heading at 564, intro at 566, fence 568-746, blank 747) | auditor finding 2 (C3a re-run, E-1) and tests c, d, f sweep evidence; S13 line stays last (orig 564 -> new 748) |

#### diff check

`diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md` hunks: 5c5, 7c7, 51c51, 119c119, 121c121, 188c188, 190c190, 314c314, 348c348, 374c374, 454c454, 494c494, 544c544, 553,556c553,556 (rows 1-17), and 562a563,644 plus 563a646,747. The last two are one insertion (row 18): diff pairs the original blank line 563 with the blank new line 645 inside the block, so it reports the 184 inserted lines as two hunks. New lines 1-563 equal the edited lines 1-563; the S13 line is the last line (748). Evidence script: /tmp/fgdc1/ev-worker1.sh; its output: /tmp/fgdc1/ev-worker1.out (run 2026-11-12T08:44:16). Log generator: /tmp/fgdc1/mklog-worker1.py.

### Edit log, -worker2.md (/tmp/fgdc1/edits-worker2.md, verbatim)

#### Edit log — docs/reports/2026-11-12-fgd-doc-alignment-worker2.md (correction-1, bead Praxis_build-fgd)

| # | orig line (in /tmp/fgdc1/orig copy) | new line (in edited file) | old text (verbatim, full line) | new text (verbatim, full line or block summary) | reason (test a–f, or auditor finding) |
|---|---|---|---|---|---|
| 1 | 5 | 5 | Unit `2026-11-12-fgd-doc-alignment`, mode ADVERSARIAL, narrow re-check of three wording cures applied after `docs/reports/2026-11-12-fgd-doc-alignment-worker1.md` (section "## Findings", line 550). Working directory `/Volumes/Sensidine/Praxis.build`, branch `main`, HEAD `006a08b`. Files under check: | Unit `2026-11-12-fgd-doc-alignment`, mode ADVERSARIAL, narrow re-check of three wording cures applied after `docs/reports/2026-11-12-fgd-doc-alignment-worker1.md` (section "## Findings", line 550 as filed and at re-run; Correction-1 re-run evidence). Working directory `/Volumes/Sensidine/Praxis.build`, branch `main`, HEAD `006a08b`. Files under check: | d (pin version of worker1 line 550; it may shift under its own correction) — pointer to E-1 |
| 2 | 13 | 13 | Nothing was staged, committed or edited apart from this report. | This worker staged and committed nothing, and wrote no file apart from this report (the last part is a self-report). At re-run HEAD is still `006a08b` and the index holds 1 entry, a pre-existing PNG under `docs/reports/evidence/`, and 0 entries under `docs/specs`, this report or DECISIONS.md (Correction-1 re-run evidence). | c/e (unevidenced "nothing staged" claim; the index holds a pre-existing PNG) — re-run pasted in E-1, remainder labelled self-report |
| 3 | 19 | 19 | The body-identity loop in this call failed because zsh does not word-split `$x`; that part of the output is not evidence and is replaced by C2. The numstat, shasum, removed-line and UTF-8 parts are valid. | The body-identity loop in this call failed because zsh does not word-split `$x` (re-run 2026-11-12 by correction-1: with `x="a 1"`, `set -- $x` gives 1 argument in zsh and 2 in bash; Correction-1 re-run evidence); that part of the output is not evidence and is replaced by C2. The numstat, shasum, removed-line and UTF-8 parts are valid. | e (cause "zsh does not word-split" asserted without paste) — re-run pasted in E-1 |
| 4 | 193 | 193 | ### C4 — DECISIONS.md around :2232, proposal :30 :40 :79, the whole proposal note (:82–111), rubric HEAD :93–94 | ### C4 — DECISIONS.md around :2232 (all DECISIONS.md line numbers in C4–C6 and in Findings are working tree; its lines 1–2278 are identical to HEAD, Correction-1 re-run evidence), proposal :30 :40 :79, the whole proposal note (:82–111), rubric HEAD :93–94 | d (DECISIONS.md modified in working tree; state the version checked) — E-1 shows lines 1–2278 identical HEAD vs working tree |
| 5 | 364 | 364 | **(a) Finding 2 (topology :136, aligned reading for :41): CURED.** The sentence now reads "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed." DECISIONS.md:2232 (C5) reads "The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec." Proposal :40 (C4) reads "if adopted, the system window check is removed and only the operator lockout remains." The object of adoption is now stated exactly, and the old wording "D-2026-11-12-A adopts that text" has 0 matches (C7). Attack tried: proposal :40's "if adopted" refers to "this proposal", but D-2026-11-12-A adopts only the #4/#5 replacement text, and OPEN-F2-1 to OPEN-F2-4 stay open. That does not break the sentence. The removal of the system window check follows from the adopted #5 text itself, "The system's own trading is not disabled by this breaker" (topology note, copied from Phase 3 :224). That is the part of the proposal that was adopted. No break. | **(a) Finding 2 (topology :136, aligned reading for :41): CURED.** The sentence now reads "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232), and proposal :40 states that, if adopted, the system window check is removed." DECISIONS.md:2232 (C5) reads "The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec." Proposal :40 (C4) reads "if adopted, the system window check is removed and only the operator lockout remains." The object of adoption is now stated exactly, and the old wording "D-2026-11-12-A adopts that text" has 0 matches (C7). Attack tried: proposal :40's "if adopted" refers to "this proposal", but D-2026-11-12-A adopts only the #4/#5 replacement text, and OPEN-F2-1 to OPEN-F2-4 (proposal :75–78, Correction-1 re-run evidence) stay open. That does not break the sentence. The removal of the system window check follows from the adopted #5 text itself, "The system's own trading is not disabled by this breaker" (topology note, copied from Phase 3 :224; that :224 holds those words is in Correction-1 re-run evidence). That is the part of the proposal that was adopted. No break. | f (quote attributed to Phase 3 :224 not pasted) and c (OPEN-F2-1–4 stay open, proposal :75–78 not pasted) — E-1 |
| 6 | 374 | 374 | Observation, not a break: D-2026-11-12-A never names OPEN-F2-5 (C6 grep is empty). So "closed" is the note's own reading of the three records, not a statement copied from the decision. The lead sentence frames it as closure "on the records below", and each of the three records exists. Finding 4 graded that as not a false claim, and the brief asks only whether the lead is qualified. It is. | Observation, not a break: D-2026-11-12-A never names OPEN-F2-5 (C6 grep is empty). So "closed" is the note's own reading of the three records, not a statement copied from the decision. The lead sentence frames it as closure "on the records below", and each of the three records exists. Finding 4 graded that as not a false claim; the check here is whether the lead is qualified. It is. | c (claim about the brief with no paste) — reduced |
| 7 | 390 | 390 | - a text-level "enforced by #4" that copies amended #5's own wording (Phase 3 :224, "is enforced by breaker #4"); | - a text-level "enforced by #4" that copies amended #5's own wording (Phase 3 :224, "is enforced by breaker #4"; Correction-1 re-run evidence); | f (quote attributed to Phase 3 :224 not pasted) — E-1 |
| 8 | 391 | 391 | - an old HEAD line copied into a fence (B1 "not tested", ruleset D8 "untested"). | - an old HEAD line copied into a fence (B1 "not tested", topology HEAD :86; ruleset D8 "untested", ruleset HEAD :79; each HEAD line occurs twice in its working file, body and note fence: Correction-1 re-run evidence). | c/f ("old HEAD line" claim without paste) — E-1 shows HEAD topology :86 and ruleset :79, each occurring twice in the working file |
| 9 | 395 | 395 | Scope limit: the pre-cure working-tree blobs were never staged and cannot be recovered, so I could not diff old against new note text line by line. For (f) I checked the current text of the three cured sentences, confirmed the pre-cure wording is gone (0 matches, C7), and scanned all added lines. | Scope limit: I held no copy of the pre-cure working-tree note text, so I could not diff old against new note text line by line. For (f) I checked the current text of the three cured sentences, confirmed the pre-cure wording is gone (0 matches, C7), and scanned all added lines. | e ("never staged and cannot be recovered" asserted without paste) — reduced to what the worker held |
| 10 | (insert after orig 399, before orig 400 blank and orig 401 S13) | 400–470 | (none — inserted) | +71 lines: evidence block E-1, "## Correction-1 re-run evidence (2026-11-12)" heading at 401, fenced script output at 405–470 (lines 406–469 are byte-identical to the output of /tmp/fgdc1/ev-worker2.sh); new 471 blank = orig 400, new 472 S13 = orig 401 | S1 cure for edits 1–5, 7–8; placed after :399 per the line-count constraint |

#### Sweep notes (claims checked, left unchanged)

- Spec sha1 at re-run equal C1 values (topology 5865a1121cd1, ruleset b68c098f4aa1, proposal 24598c3d73d8), so every spec-note line number in C3, C4, C7 and Findings (:105, :136, :184, :95, :103, :81, :46, :93–94, :30–31 at e3323a8) refers to these blobs and was checked against the pasted output.
- DECISIONS.md relative-to-absolute mapping on line 262 (1=2205, 3=2207, 45=2249, 59=2263, 68=2272) checked; D-2026-11-12-B starts at relative 76 = 2280, so the C6 range 2205–2279 covers D-2026-11-12-A.
- Tests a/b: no placeholders or ellipsis-cut output in shown commands; ellipses on lines 371–372 are quotation elisions of the :103 line pasted in full at C7 line 356.
- Verdict lines :326 and :399 unchanged; S13 is the last line (472).

#### diff hunks vs pristine (every hunk is in the table)

```text
5c5
13c13
19c19
193c193
364c364
374c374
390,391c390,391
395c395
399a400,403
400a405,471
```

#### deid.sh (counts only)

```text
docs/reports/2026-11-12-fgd-doc-alignment-manager.md | rep-name=1 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | absent
docs/specs/2026-11-10-live-signal-topology.md (added lines: 86) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-07-16-b2-noise-area-ruleset.md (added lines: 59) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-11-10-f2-session-flat-proposal.md (added lines: 30) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
```

Notes on the pasted logs (adv-1 findings 2 and 5): the manager log's "Hunk check" paragraph shortens the plain-diff hunk list with an ellipsis; the full list is pasted in C9b. The worker2 log's closing scan output, which shows a rep-name count of 1 for `-manager.md`, was run before the mask was applied; the current count, 0, is in C3.

## Verification evidence

Output of `/tmp/fgdc1/ev-corr1.sh` (prints each command, its full output, its exit code), pasted verbatim from `/tmp/fgdc1/ev-corr1.out`. Lines are cut only where the shown command cuts them. C4's last command exits 1 because grep -c found 0; C8's first two commands exit 1 because the diffs differ in the lines stated under M2 and M3. C3, C10 and C12 read the current files, so they change whenever a report in the set changes; this paste is the run made when this file was last built. C10's exit status is that of the loop's last test. C11's two manager hits are literal search patterns, not placeholders (C11, second command).

````text
## C0 rubric lines cited
$ grep -n -E '^\| S(1|2|13) \|' specs/SPEC_RUBRIC.md | cut -c1-80
127:| S1 | Every claim in a report has pasted command output, not a description 
128:| S2 | No component is reported at a higher level than the evidence supports
139:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that s
(exit 0)

## C1 HEAD and real index (counts only; the one path carries the rep name)
$ git rev-parse --short HEAD
006a08b
(exit 0)

$ git diff --cached --name-only | wc -l
       1
(exit 0)

$ git diff --cached --name-only | grep -c '\.png$'
1
(exit 0)

$ git diff --cached --name-only | grep -c -i -f /tmp/fgdc1/rep.txt
1
(exit 0)

## C2 negative test: the scan trips on the pre-correction copies
$ grep -c -i -f /tmp/fgdc1/rep.txt /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md:1
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md:0
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md:0
(exit 0)

$ grep -n -i -f /tmp/fgdc1/rep.txt /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md | cut -d: -f1
96
(exit 0)

## C3 de-identification scan, current files (patterns in /tmp/fgdc1/*.txt; counts only)
$ bash /tmp/fgdc1/deid.sh
docs/reports/2026-11-12-fgd-doc-alignment-manager.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-11-10-live-signal-topology.md (added lines: 86) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-07-16-b2-noise-area-ruleset.md (added lines: 59) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-11-10-f2-session-flat-proposal.md (added lines: 30) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
(exit 0)

$ for f in /tmp/fgdc1/edits-manager.md /tmp/fgdc1/edits-worker1.md /tmp/fgdc1/edits-worker2.md; do echo "$f rep-name=$(grep -c -i -f /tmp/fgdc1/rep.txt $f)"; done
/tmp/fgdc1/edits-manager.md rep-name=0
/tmp/fgdc1/edits-worker1.md rep-name=0
/tmp/fgdc1/edits-worker2.md rep-name=0
(exit 0)

## C4 auditor finding 1 and 2: worker1 verdict line, length, elision lines
$ grep -n '^Verdict' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md:562:Verdict: PASS
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:562:Verdict: PASS
(exit 0)

$ wc -l < /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
     564
(exit 0)

$ awk 'NR>=545 && NR<=563 && index($0,"..."){print NR}' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
553
555
(exit 0)

$ grep -n -o 'at its line 5[0-9][0-9]' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
782:at its line 562
(exit 0)

$ grep -n -o 'its lines 5[0-9][0-9] and 5[0-9][0-9]' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
792:its lines 553 and 555
(exit 0)

$ grep -c -F 'at its line 573' docs/reports/2026-11-12-fgd-doc-alignment-manager.md; grep -c -F 'its lines 564 and 566' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
0
0
(exit 1)

## C5 auditor findings 3-5: iconv, every-cite, UnicodeDecodeError, .cs lines
$ grep -c -F 'INVALID-utf8' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-manager.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md:1
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:0
(exit 0)

$ grep -n -o 'not reproducible after the repair' docs/reports/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:25:not reproducible after the repair
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:374:not reproducible after the repair
(exit 0)

$ grep -c -F 'Every cited line was checked against HEAD' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-manager.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md:1
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:0
(exit 0)

$ grep -n -F 'UnicodeDecodeError ...' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-90
(exit 0)

$ grep -n -F 'PraxisNoiseAreaBreakout.cs' docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -c1-110
23:2. Read the trader's 2026-07-16 lock (DECISION_LOG.md:42 at HEAD, E5) and `ninjascript/PraxisNoiseAreaBreak
73:| `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191 (not a citation; the code) | 16:00 flat, "trader-locked"
692:$ git diff --quiet HEAD -- ninjascript/PraxisNoiseAreaBreakout.cs && echo NO-DIFF
696:$ git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | sed -n 188,191p
(exit 0)

$ sed -n 188,191p ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-150
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
(exit 0)

## C6 auditor MINOR: worker1 od -c segment now has re-run output (E-1)
$ grep -n -F 'od -c' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-80
367:' $f; grep -n 'SPEC_RUBRIC.md`:' $f | cut -c1-60 | od -c | sed -n 1,12p
374:At that read, the F-7 citation was `` `specs/SPEC_RUBRIC.md`: `` followed by
397:$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-f2-session-f
586:' $f; grep -n 'SPEC_RUBRIC.md`:' $f | cut -c1-60 | od -c | sed -n 1,12p
(exit 0)

## C7 manager :25 edit by the correction manager (old line rebuilt by removing the added sentence)
$ sed -n 25p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | sed 's/ The pre-repair bytes .*(its python output, offsets 13567 and 13568)\.//' | cut -c1-200
4. Defect found and cured by the manager: in the proposal note, line 95, the en dash after a variable name lost its first byte in the shell (the manager's account of the cause), leaving invalid UTF-8 
(exit 0)

$ sed -n 25p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -o 'The pre-repair bytes .*'
The pre-repair bytes `3a 80 93 39 34` on line 95 are pasted in worker1's report, section C3a (its python output, offsets 13567 and 13568). Repaired with a byte-level substitution on line 95 only. Only the post-repair results are pasted: valid UTF-8 and the `:93–94` text (E9), body still identical (E3), numstat still 30/0 (E2).
(exit 0)

$ grep -n -F 'invalid byte offsets: [13567, 13568]' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
369:invalid byte offsets: [13567, 13568]
(exit 0)

$ grep -n -o 'E14 was run before correction-1 appended its two MANIFEST.md rows' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
87:E14 was run before correction-1 appended its two MANIFEST.md rows
(exit 0)

$ grep -n -o 'This block was run before correction-1 appended its two MANIFEST.md rows' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
566:This block was run before correction-1 appended its two MANIFEST.md rows
(exit 0)

## C8 pasted evidence blocks equal a fresh run of their scripts
$ bash /tmp/fgdc1/ev-manager.sh > /tmp/fgdc1/re-m.out; n=$(wc -l < /tmp/fgdc1/re-m.out); s=$(grep -n -x -F '## E14 Correction-1 re-run evidence (2026-11-12)' docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -d: -f1); echo "lines=$n start=:$s"; tail -n +$s docs/reports/2026-11-12-fgd-doc-alignment-manager.md | head -n $n | diff - /tmp/fgdc1/re-m.out && echo MATCH
lines=     343 start=:435
304c304
< 2026-11-12T08:24:38 MANIFEST.md
---
> 2026-11-12T08:49:24 MANIFEST.md
313c313
< @@ -431,0 +440,12 @@
---
> @@ -431,0 +440,14 @@
(exit 1)

$ bash /tmp/fgdc1/ev-worker1.sh > /tmp/fgdc1/re-w1.out; n=$(wc -l < /tmp/fgdc1/re-w1.out); s=$(grep -n '^re-run 2026-11-12 by correction-1, 2026-11-12T' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | cut -d: -f1); echo "lines=$n start=:$s"; diff <(tail -n +$((s+1)) docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | head -n $((n-2))) <(sed -n "2,$((n-1))p" /tmp/fgdc1/re-w1.out) && echo 'MATCH (lines 2 to n-1; line 1 is the run timestamp, line n is the trailing blank line)'
lines=     178 start=:569
80c80
< @@ -431,0 +440,12 @@
---
> @@ -431,0 +440,14 @@
(exit 1)

$ bash /tmp/fgdc1/ev-worker2.sh > /tmp/fgdc1/re-w2.out; n=$(wc -l < /tmp/fgdc1/re-w2.out); s=$(grep -n -x -F "$(head -n 1 /tmp/fgdc1/re-w2.out)" docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | head -n 1 | cut -d: -f1); echo "lines=$n start=:$s"; tail -n +$s docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | head -n $n | diff - /tmp/fgdc1/re-w2.out && echo MATCH
lines=      64 start=:406
MATCH
(exit 0)

## C9 line-number preservation in the worker reports (hunk headers vs pristine copies)
$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | grep -E '^[0-9]' | tr '\n' ' '; echo
5c5 7c7 51c51 119c119 121c121 188c188 190c190 314c314 348c348 374c374 454c454 494c494 544c544 553,556c553,556 562a563,644 563a646,747 
(exit 0)

$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | grep -E '^[0-9]' | tr '\n' ' '; echo
5c5 13c13 19c19 193c193 364c364 374c374 390,391c390,391 395c395 399a400,403 400a405,471 
(exit 0)

$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md <(sed -e '97d' -e '435,777d' docs/reports/2026-11-12-fgd-doc-alignment-manager.md) | grep -E '^[0-9]' | tr '\n' ' '; echo
5c5 16c16 18c18 22,23c22,23 25,27c25,27 31c31 33,37c33,37 41,42c41,42 44c44 48c48 52c52 61,64c61,64 72,73c72,73 79,83c79,83 87c87 96c96 438c438 440,443c440,443 446c446 448c448 455c455 458c458 462c462 466c466 
(exit 0)

## C9b plain diff hunk list, manager (full)
$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -E '^[0-9]' | tr '\n' ' '; echo
5c5 16c16 18c18 22,23c22,23 25,27c25,27 31c31 33,37c33,37 41,42c41,42 44c44 48c48 52c52 61,64c61,64 72,73c72,73 79,83c79,83 87c87 96c96,97 434c435,436 436c438,440 438c442,445 440,446c447,449 448c451,587 449a589,793 455c799 458c802 462c806 466c810 
(exit 0)

## C10 S13: last line and count, every report of this bead's fgd-doc-alignment set
$ for f in docs/reports/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md; do [ -f $f ] && echo "$f count=$(grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' $f) last=$(tail -n 1 $f | cut -c1-30)"; done
docs/reports/2026-11-12-fgd-doc-alignment-manager.md count=3 last=Fills are optimistic; Standard
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md count=2 last=Fills are optimistic; Standard
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md count=2 last=Fills are optimistic; Standard
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md count=1 last=Fills are optimistic; Standard
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md count=1 last=Fills are optimistic; Standard
(exit 0)

$ grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md:3
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md:2
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md:2
(exit 0)

## C11 placeholder scan of shown commands in the three corrected reports
$ grep -c -E '^\$ .*(<…>|<[a-z]+>|\.\.\.)' docs/reports/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:2
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:0
(exit 0)

$ grep -n -E '^\$ .*(<…>|<[a-z]+>|\.\.\.)' docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -c1-120
419:$ grep -c -F '<…>' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-wo
451:$ awk '/^```/{f=!f} index($0,"..."){print NR": "(f?"in-fence":"prose")}' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignmen
(exit 0)

## C12 scope: files under these paths modified since the pristine copies were taken
$ find docs specs DECISIONS.md MANIFEST.md .claude ninjascript -type f -newer /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md | sort
.claude/agent-memory/praxis-worker/MEMORY.md
.claude/agent-memory/praxis-worker/project_zsh-echo-mangles-shown-commands.md
.claude/agent-memory/praxis-worker/project_zsh-grep-is-ugrep.md
MANIFEST.md
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md
docs/reports/2026-11-12-fgd-doc-alignment-manager.md
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md
(exit 0)

$ shasum docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md
5865a1121cd1b55783f217c4f341e20b7cfc03d5  docs/specs/2026-11-10-live-signal-topology.md
b68c098f4aa1d3273ad179474299d662f1e0c243  docs/specs/2026-07-16-b2-noise-area-ruleset.md
24598c3d73d8dd3a3961a7083aa8e42a68012362  docs/specs/2026-11-10-f2-session-flat-proposal.md
(exit 0)

## C13a worker memory write under .claude/ (gitignored)
$ git status --short --ignored -- .claude/agent-memory
!! .claude/agent-memory/
(exit 0)

$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md | cut -d: -f1,3
.gitignore:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
(exit 0)

## C14 S6: files outside this report set that cite the three corrected reports (working tree)
$ grep -rl -F 'fgd-doc-alignment-' --include='*.md' . 2>/dev/null | grep -v -E '^\./docs/reports/2026-11-12-fgd-doc-alignment-' | sort
./MANIFEST.md
(exit 0)

$ grep -rn -E 'fgd-doc-alignment-(manager|worker1|worker2)[.]md.?:[0-9]' --include='*.md' . 2>/dev/null | grep -v -E '^[.]/docs/reports/2026-11-12-fgd-doc-alignment-' | cut -c1-160
(exit 0)

## C15 adv-1 cures
$ sed -n 13p docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | grep -o 'one PNG under .docs/reports/evidence/. (counts in the re-run block)'; grep -c -F 'pre-existing PNG' docs/reports/2026-11-12-fgd-doc-alignment-worker2.md
one PNG under `docs/reports/evidence/` (counts in the re-run block)
0
(exit 1)

## C16 adv-1 report checks, and the pre-cure copy of this report it cites
$ grep -n '^Verdict' docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md; tail -n 1 docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | cut -c1-30; grep -n -E '^\$ .*(<…>|<[a-z]+>)' docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | cut -c1-140; grep -n -E '^[0-9]+\. (MAJOR|MINOR)' docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | cut -c1-40
324:Verdict: FAIL
Fills are optimistic; Standard
248:$ grep -n -E "^\\$ .*(<…>|<[a-z]+>|\.\.\.)" docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -c1-60
291:1. MINOR. File and lines: `-correcti
292:2. MINOR. File and line: `-correctio
293:3. MINOR. File and line: `-correctio
294:4. MINOR. File and lines: `-correcti
295:5. MINOR. File and lines: `-correcti
296:6. MINOR. File and line: `-worker2.m
297:7. MINOR. File and line: `-correctio
(exit 0)

$ sed -n 100p /tmp/fgdc1/c1-precure.md | grep -c -F '434c435,436 … 449a589,793'; sed -n 18p /tmp/fgdc1/c1-precure.md | grep -c -F 'stopped at its 40-turn limit with no return text'; grep -c 'ADV_PLACEHOLDER' /tmp/fgdc1/c1-precure.md
1
1
1
(exit 0)

## C13 MANIFEST
$ git diff --numstat HEAD -- MANIFEST.md
22	0	MANIFEST.md
(exit 0)

$ grep -n 'fgd-doc-alignment-correction-1' MANIFEST.md | cut -c1-90
452:| /docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | Report | 3 | 20
453:| /docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | Report | 3 | 20
(exit 0)

$ wc -l < MANIFEST.md
     453
(exit 0)

````

## Adversarial findings

adv-1 (`docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md`, ADVERSARIAL) returned `Verdict: FAIL` on seven MINOR findings and no MAJOR (C16 lists its verdict line and its seven numbered findings). Its report states that the eight audit cures hold and that the 13 untouched claims it sampled hold; those are its findings, with its evidence in its report. Its line numbers for this report refer to the pre-cure build, kept at `/tmp/fgdc1/c1-precure.md` (C16, third command: the quoted text is at :100 and :18 there). Dispositions:

1. Fresh run of C3, C10, C12 differs once adv-1's report exists; C10's exit 1 unexplained. Cured: this report was rebuilt after adv-1 returned, and the evidence intro now says these blocks read current files and why C10's exit status is what it is.
2. Manager edit log's "Hunk check" paragraph shortens the hunk list with an ellipsis. Cured: note after the logs, full list pasted in C9b (the log itself stays verbatim).
3. "stopped at its 40-turn limit with no return text" had no paste. Cured: Workers table now quotes the Agent tool's return and says it is a tool return, not command output, and not reproducible.
4. C11 count of 2 unexplained. Cured: C11 second command lists the two lines (:419, :451); both are literal search patterns.
5. Worker2 log's closing scan shows rep-name=1 for `-manager.md` with no label. Cured: note after the logs (pre-mask run; current 0 in C3).
6. worker2 :13 "a pre-existing PNG" not shown by counts. Cured by edit M4 (C15: new phrase present, "pre-existing PNG" count 0 in that file).
7. Task line pointed to a section not yet written and said "one" memory write. Cured: the Task now points to C12 and C13a and this section, with no count.

Disclosed residuals:
- Worker-memory files were written by workers under `.claude/agent-memory/praxis-worker/` against the brief's "do not edit .claude/"; the directory is gitignored (C13a), so nothing enters the repo. C12 lists the files. Not reverted (their prior content was not kept).
- The cures to adv-1's seven findings are shown by this report's pasted C9b, C11, C15 and C16 output only; no second adversarial worker re-checked them.
- The optional MINOR (MANIFEST positions in the to-be-recorded blob, :432–437) is cured only by the "(working-tree positions)" qualifier in the manager report; the blob positions were not computed in this unit.
- adv-1's own report: C16, first command, lists one shown-command line in it that matches `<…>` or `<word>` (its :248); that is a literal search pattern, not a placeholder.

## S6 cross-block check

C14 lists the files outside the three reports and this unit's own reports that name the fgd-doc-alignment reports, and any that cite a line of them. The corrected reports moved lines only in `-manager.md` (one line inserted at :97 and the 343-line E14 block at :435–777, C9); in `-worker1.md` and `-worker2.md`, every line at or above the Verdict lines (:562; :326 and :399) keeps its number (C9 hunk headers: all one-for-one above those lines). Only MANIFEST.md names these reports outside the set (C14, first command), and no file outside the set cites a line of the three corrected reports (C14, second command, no output). Grade: MANIFEST.md rows :449–451 for the three reports describe them as "ungraded at time of row"; unaffected by in-place cures. The line shifts inside `-manager.md` are cited only by this report and the edit logs, which give the new numbers. The audit finding list given to this unit cites pre-correction manager lines (:22–:25, :73, :96, :438, :448); they map to new :22–:25, :73, :96, :782, :792 (edit log rows; C4).

## Files staged

None. The real index holds one path, the PNG (C1: one name, one `.png`). Files changed by this unit in the working tree: the three reports, this report, `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md` (adv-1), MANIFEST.md (+2 rows at :452–453; numstat 22/0 vs HEAD, of which 20 pre-existing, C13). C12 lists every file under docs, specs, DECISIONS.md, MANIFEST.md, .claude and ninjascript modified after the pristine copies were taken.

## Result

Every audit finding has an in-place cure with pasted evidence (C4 to C7, edit logs), the rep name is masked and the counts-only scan reads 0 across the five reports and the three specs' added lines (C3), every edit is itemised (edit logs, M1 to M4, C9 and C9b hunk lists), and adv-1's seven MINOR findings are cured with the residuals above.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
