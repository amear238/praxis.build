# 2026-11-12 — fgd doc alignment (bead Praxis_build-fgd, part A) — manager report

## Task

Unit `2026-11-12-fgd-doc-alignment`, decided by master under D-2026-11-08-D D1, changeable by Amear. It carries out D-2026-11-12-A (DECISIONS.md:2205; E5, E14) and Amendment 1 of `docs/specs/2026-11-05-phase3-build-specification.md` for five follow-ups named in `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` :134–142 (E14): F-1, F-2 (topology doc), F-3 (Noise-Area ruleset), F-7, F-9 (F2 proposal). Method fixed by the master: one dated, labelled section appended at the end of each file; body lines unchanged; no new design choice; no DECISIONS.md entry. The breakers remain SPECIFIED ONLY (zero implemented, zero tested, zero tested under failure); nothing in this unit changes that.

## Rubric criteria addressed

S1 (pasted output), S2 (level), S4 (no deviation from plan: this unit writes no design choice; it carries out D-2026-11-12-A, which was written before its spec edit), S6 (cross-block table below), S13 (last line). The F1 bearing is stated with grep output; F1 is not re-graded and the rubric is not edited.

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| worker1 | ADVERSARIAL (artifact and criteria only; not the manager's reasoning) | see "Adversarial findings" |
| worker2 | ADVERSARIAL, narrow re-check of the cures to worker1 findings 1-4 | Verdict: PASS, 0 breaks, 1 observation (worker2 :397, E14; see "Adversarial findings") |

The three notes were written by the manager (pure doc edits, as the master's brief directs: "check your notes"); the 16 old body lines quoted in them were copied by script: `/tmp/fgd/build.sh`:8 defines a function `q` that runs `git show "HEAD:$1" | sed -n "${2}p"`, and build.sh calls it for those 16 lines (E14).

## Process log

1. Read the follow-up list (F2 amendment report :134–142), D-2026-11-12-A (DECISIONS.md:2205–2278, the last entry at HEAD), Amendment 1 (Phase 3 :190–244, heading at :190), the rubric F1/F2 sections, and the three target files in full with line numbers. The cited lines are pasted in E14 (follow-up list, DECISIONS.md, rubric, Phase 3, topology, ruleset, proposal); that pasted set is what is shown, not every line read. One extra line found in F-1's subject: topology :78 ("all nine checks move into the strategy"; E14), added to the topology note and labelled as found by this unit (note line 178, E14).
2. Read the trader's 2026-07-16 lock (DECISION_LOG.md:42 at HEAD, E5) and `ninjascript/PraxisNoiseAreaBreakout.cs` :188–191 (16:00 flat, "trader-locked"; E14) for F-3.
3. Built the notes in /tmp with a script; appended them; proved additions only (E2, E3).
4. Defect found and cured by the manager: in the proposal note, line 95, the en dash after a variable name lost its first byte in the shell (the manager's account of the cause), leaving invalid UTF-8 (":" followed by two stray bytes, then "94"). The `iconv` detection output was not kept, and it is not reproducible after the repair; no INVALID result is pasted here. The pre-repair bytes `3a 80 93 39 34` on line 95 are pasted in worker1's report, section C3a (its python output, offsets 13567 and 13568). Repaired with a byte-level substitution on line 95 only. Only the post-repair results are pasted: valid UTF-8 and the `:93–94` text (E9), body still identical (E3), numstat still 30/0 (E2).
5. MANIFEST rows appended at :446–451 (working-tree positions; row :451 is worker2's, E13) after the 14 uncommitted rows of other units at :307–314 and :440–445 (E6, E14).
6. ADVERSARIAL worker1 dispatched; its report read on disk (Findings, verdict, last line, placeholder scan). Findings 2-4 cured by the manager with /tmp/fgd/cure.py (exact-string replacement in the appended notes only; each replacement string now occurs once, E14); E3 proves additions only and E13 gives the hashes after the cures. 7. ADVERSARIAL worker2 re-checked the cures on the current hashes (its sha1s at worker2 :35–37 equal E13; E14).

## Per-follow-up disposition

| Follow-up | Lines checked (HEAD text in E14) | Disposition |
|---|---|---|
| F-1 | topology :41, :48, :62, :74, :86, plus :78 (found here) | DONE. Note reads the consumer-side checks as #4, #7, #8, #9; #5 has no system check on the path; the #5 row's own conditional ("the n8n/consumer window check is then removed"; topology :62, E14) is in effect because D-2026-11-12-A adopts the proposal text. |
| F-2 | topology :54, :61, :62 | DONE. Amended names "Session flat gate" (#4) and "Session window (operator lockout)" (#5) govern; body names kept as written. One OPEN item raised (OPEN-A1, placement of amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)"; Phase 3 :212, E14), two readings, not chosen. |
| F-3 | ruleset :8, :79, :84, :99, :105 | DONE for the replication strategy, on two prior records: the trader's lock DECISION_LOG.md:42 item (1) "session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)" (E5) and D-2026-11-12-A (no breaker forces 11:30). One OPEN item (OPEN-A2): whether a strategy-level 11:30 stop stays available to a later arm; two readings, not chosen. |
| F-7 | proposal :8 | DONE. Unblock clause re-pointed to `specs/SPEC_RUBRIC.md`:93–94 at `006a08b` (E5; was :30–31 at `e3323a8`, E14; F2 moved to PASSED at `c29d08b`, E9); A6 citation :1744–1745 unchanged (proposal :8 and DECISIONS.md:1744–1745 at HEAD, E14). |
| F-9 | proposal :79 (read with :3) | DONE. OPEN-F2-5 recorded as closed: each step in its own "What would decide it" column has a record (D-2026-11-11-A V2 at :2108; D-2026-11-12-A at :2205; Amendment 1; E11, E14); rubric F2 PASSED@e3323a8 (E5). D-2026-11-12-A's limits carried: approval given on a summary; #4/#5 text is the master's adoption under D1; whether the approval reaches that text, and whether A6 is triggered, not graded. |

## OPEN items (recorded in the notes, not chosen)

- OPEN-A1 (topology note). Where amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (Phase 3 :212, E14) sit on the live path. (a) inside the FLATTEN command the consumer executes; (b) a separate n8n-side account-state check (needs OPEN-T3's feed).
- OPEN-A2 (ruleset note). Whether a strategy-level 11:30 stop remains available to a later Noise-Area arm. (a) No: lock item (1) and Rule F2-1's entries-until-16:00 carry the full-day window to every arm. (b) Yes, as that arm's own design choice: lock item (3) scopes the "FIRST build" to replication (E5), and Rule F2-1 sets only the latest flat (proposal :24, E14).

New follow-ups observed, not fixed (outside the five): other rubric line citations that moved when F1/F2 moved to PASSED — proposal :61 (O4 cited at :108–113; O4 heading is now :114), proposal :69 (F2 "Why frozen" cited at :37–42; now :87 onward), topology :7 (F1 unblock cited at :28–29; now :75–76, E14), topology :112 (cited :30; F1 "Blocks" line now :77). See E10.

## F1 nine-name check

E4 below: each of the nine Phase 3 body names (:97–105, E14) occurs in the topology doc (counts 1, 1, 1, 3, 3, 1, 1, 2, 1), the breaker table :58–66 still lists all nine in order, and the amended names "Session flat gate" and "Session window (operator lockout)" (Phase 3 :212, :224) each occur 3 times, all in the note (note lines 124–168, E14). Bearing, not a grade: amended #5 no longer sits on the signal path at all, so F1's "showing how each of the nine circuit breakers sits upstream of order submission" (rubric :68–69, E14) now reads, for #5, through #4 (system half) and B3/OPEN-T8 (lockout). Whether F1 needs re-grading is the master's call.

## S6 cross-block check

Source of hits: `/tmp/fgd/s6.sh` (git grep at HEAD, excluding the F2 amendment reports that list F-1 to F-9); its full output is pasted under E11; s6.sh cuts each hit line to 230 characters (`cut -c1-230`, E14). Nothing listed here was edited.

Topology note:

| Citing doc and line | What it cites | Grade |
|---|---|---|
| DECISIONS.md:2058 | topology :48, the CLAUDE.md signal-flow quote | unaffected (that part of :48 is not superseded) |
| DECISIONS.md:2155; `docs/reports/2026-11-11-v-rulings-filing-worker7.md`:71 | :41 path ending "→ Rithmic → account" | unaffected (path tail unchanged) |
| `docs/reports/2026-11-11-mffu-connection-investigation.md`:50, :88; `docs/reports/2026-11-11-v-rulings-filing-worker1.md`:137 | :41 path tail | unaffected |
| DECISIONS.md:2247 (D-2026-11-12-A) | other specs cite topology :24, :61, :89, so no body line may shift (E14) | agrees (no body line moved, E3) |
| Phase 3 :244 (Amendment 1) | placement of #4/#5 is in topology section 3, "which this amendment does not edit" (E14) | agrees (section 3 body still unedited; the note reads it under Amendment 1) |
| proposal :40 | "if adopted, the system window check is removed and only the operator lockout remains" (E14) | agrees (the note records the condition as met) |
| rubric F1 :63 (filer's note), :75–76 (unblock clause) | nine breakers by name (E14) | bearing, see F1 check |

Ruleset note:

| Citing doc and line | What it cites | Grade |
|---|---|---|
| DECISION_LOG.md:42 | the lock itself | agrees (it is the note's source) |
| `docs/reports/2026-10-30-3gm-fidelity-check.md`:644 (R27) and `docs/reports/2026-10-30-3gm-worker1-checklist.md`:757 | ruleset :99, for its stop-market entry idea | unaffected (the stop-market part of :99 is not superseded) |
| `docs/reports/2026-11-09-d11-sweep-manager.md`:266, :2076, :2079 (W4-11) | ruleset :105 and :79; closes the backtest flat via R1; says "the live 11:30 flat is breaker #4" (:266, E14) | agrees on the backtest flat; its "live 11:30 flat is breaker #4" sentence conflicts with D-2026-11-12-A (dated report, not edited) |
| `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191 (not a citation; the code) | 16:00 flat, "trader-locked" (E14) | agrees (WRITTEN, backtested; not edited) |

Proposal note:

| Citing doc and line | What it cites | Grade |
|---|---|---|
| DECISIONS.md:2272 (D-2026-11-12-A) | proposal :8 cites :43–44; clause "is at :30–31" (E14) | agrees as of `e3323a8`; as a current pointer it is stale (clause now :93–94); append-only, not edited |
| DECISION_LOG.md:830; HANDOFF.md:90; `docs/reports/2026-11-11-v-rulings-filing-manager.md`:173; `docs/reports/2026-11-11-v-rulings-filing-worker1.md`:311 | that proposal :8's :43–44 is at :30–31 (paraphrase, not a quotation; each line's wording in E14) | conflicts as a current pointer (now :93–94); dated records, not edited |
| DECISIONS.md:2108 (D-2026-11-11-A V2) | "OPEN-F2-5 is not closed by this entry" (E14) | agrees (that entry did not close it; the note closes it after D-2026-11-12-A) |
| `docs/reports/2026-11-11-v-rulings-filing-manager.md`:181; `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md`:361–362; v-rulings worker3/5/6/7/10 rows quoting proposal :79 | OPEN-F2-5 open at their date (E11, E14) | agrees as of their date (historical) |
| rubric F2 filer note :79 | F2 PASSED, residuals in bead fgd (E14) | agrees |

## Verification evidence

Blocks E1–E13 below are the output of the evidence scripts /tmp/fgd/evidence.sh, /tmp/fgd/evidence2.sh and /tmp/fgd/e13.sh (each prints the command, then its full output and exit code). Before correction-1 masked one filename in E1, E1–E13 were byte-identical to those scripts' saved outputs, written at 08:25:05–08:25:06, after the last modification of the three spec files (08:19:44) and MANIFEST.md (08:24:38) (E14). A re-run after every edit of this unit is not shown by pasted output. E14 is correction-1's re-run. E14 was run before correction-1 appended its two MANIFEST.md rows (:452–453); a fresh run now differs from the paste only in the MANIFEST.md mtime line and the MANIFEST.md hunk header (`+440,12` becomes `+440,14`), shown in C8 of `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md`.

```text
## E1 HEAD and index
$ git rev-parse --short HEAD
006a08b
(exit 0)

$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-[rep-name]-reply.png
[correction-1, 2026-11-12: the support rep's first name in this filename is masked as [rep-name]; the actual output carried the name]
(exit 0)

## E2 numstat per file
$ git diff --numstat HEAD -- docs/specs/2026-11-10-live-signal-topology.md
86	0	docs/specs/2026-11-10-live-signal-topology.md
(exit 0)

$ git diff --numstat HEAD -- docs/specs/2026-07-16-b2-noise-area-ruleset.md
59	0	docs/specs/2026-07-16-b2-noise-area-ruleset.md
(exit 0)

$ git diff --numstat HEAD -- docs/specs/2026-11-10-f2-session-flat-proposal.md
30	0	docs/specs/2026-11-10-f2-session-flat-proposal.md
(exit 0)

$ git diff --numstat HEAD -- MANIFEST.md
20	0	MANIFEST.md
(exit 0)

## E3 additions-only proof
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | wc -l
     114
(exit 0)

$ head -n 114 docs/specs/2026-11-10-live-signal-topology.md | cmp - <(git show HEAD:docs/specs/2026-11-10-live-signal-topology.md) && echo BODY-IDENTICAL
BODY-IDENTICAL
(exit 0)

$ git diff HEAD -- docs/specs/2026-11-10-live-signal-topology.md | grep -c '^-[^-]' || true
0
(exit 0)

$ git diff HEAD -- docs/specs/2026-11-10-live-signal-topology.md | grep -n '^@@'
5:@@ -112,3 +112,89 @@ Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, po
(exit 0)

$ git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | wc -l
     111
(exit 0)

$ head -n 111 docs/specs/2026-07-16-b2-noise-area-ruleset.md | cmp - <(git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md) && echo BODY-IDENTICAL
BODY-IDENTICAL
(exit 0)

$ git diff HEAD -- docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -c '^-[^-]' || true
0
(exit 0)

$ git diff HEAD -- docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -n '^@@'
5:@@ -109,3 +109,62 @@ Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`
(exit 0)

$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | wc -l
      81
(exit 0)

$ head -n 81 docs/specs/2026-11-10-f2-session-flat-proposal.md | cmp - <(git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md) && echo BODY-IDENTICAL
BODY-IDENTICAL
(exit 0)

$ git diff HEAD -- docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -c '^-[^-]' || true
0
(exit 0)

$ git diff HEAD -- docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -n '^@@'
5:@@ -79,3 +79,33 @@ How the rule maps to R8 (DECISIONS.md:1583–1589): R8 opens "F2 unfreezes." and
(exit 0)

## E4 F1 nine-name check (Phase 3 :97-105 body names, :212/:224 amended names) in the topology doc
$ grep -c -F 'Daily loss limit' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Max trades per day' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Consecutive loss (“two and done”)' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Session time gate' docs/specs/2026-11-10-live-signal-topology.md
3
(exit 0)

$ grep -c -F 'Afternoon session window' docs/specs/2026-11-10-live-signal-topology.md
3
(exit 0)

$ grep -c -F 'Trailing drawdown proximity' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Max position size' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Stale signal filter' docs/specs/2026-11-10-live-signal-topology.md
2
(exit 0)

$ grep -c -F 'Heartbeat dead-man switch' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'Session flat gate' docs/specs/2026-11-10-live-signal-topology.md
3
(exit 0)

$ grep -c -F 'Session window (operator lockout)' docs/specs/2026-11-10-live-signal-topology.md
3
(exit 0)

$ sed -n 58,66p docs/specs/2026-11-10-live-signal-topology.md | cut -d'|' -f2-3
 1 | Daily loss limit 
 2 | Max trades per day 
 3 | Consecutive loss (“two and done”) 
 4 | Session time gate 
 5 | Afternoon session window 
 6 | Trailing drawdown proximity 
 7 | Max position size 
 8 | Stale signal filter 
 9 | Heartbeat dead-man switch 
(exit 0)

## E5 cited governing lines
$ sed -n 2205p DECISIONS.md
## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
(exit 0)

$ sed -n 212p docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-60
> 4. Session flat gate — clock reaches 16:00:00 ET, or the e
(exit 0)

$ sed -n 224p docs/specs/2026-11-05-phase3-build-specification.md | cut -c1-60
> 5. Session window (operator lockout) — clock is in 3:00–6:
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '46p;81p;82p;93p;94p'
## PASSED — closed criteria
### F2 — Session-flat time vs. breakers #4 and #5
**State:** PASSED@e3323a8.
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
(exit 0)

$ sed -n 1551p DECISIONS.md | grep -o 'RTH = 09:30–16:00 ET'
RTH = 09:30–16:00 ET
(exit 0)

$ git show HEAD:DECISION_LOG.md | sed -n 42p | grep -o -E '(\(1\)|\(3\)) [^;]{0,70}'
(1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)
(3) FIRST build = pure paper replication with FIXED params (lookback=14, b
(exit 0)

## E6 MANIFEST rows added
$ git diff HEAD -- MANIFEST.md | grep -c '^+|'
20
(exit 0)

$ grep -n 'fgd-doc-alignment' MANIFEST.md | cut -d'|' -f1-2
446:| /docs/specs/2026-11-10-live-signal-topology.md 
447:| /docs/specs/2026-07-16-b2-noise-area-ruleset.md 
448:| /docs/specs/2026-11-10-f2-session-flat-proposal.md 
449:| /docs/reports/2026-11-12-fgd-doc-alignment-manager.md 
450:| /docs/reports/2026-11-12-fgd-doc-alignment-worker1.md 
451:| /docs/reports/2026-11-12-fgd-doc-alignment-worker2.md 
(exit 0)

## E7 de-identification of the appended text (patterns in /tmp/fgd/deid.sh; counts only)
$ bash /tmp/fgd/deid.sh
email-pattern: 0
paper-author-surnames: 0
med-terms: 0
(exit 0)

## E8 out-of-scope files untouched by this unit (paths with diffs vs HEAD among the forbidden set, compared to session start)
$ git status --short -- DECISIONS.md specs/SPEC_RUBRIC.md docs/specs/2026-11-05-phase3-build-specification.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md ninjascript DECISION_LOG.md DISPATCH_LOG.md HANDOFF.md STATUS.md ISSUE_REGISTER.md AUDIT_LOG.md .claude
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISIONS.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M ISSUE_REGISTER.md
 M docs/specs/2026-11-05-walk-forward-spec.md
 M docs/specs/2026-11-06-walk-forward-values.md
(exit 0)

## E9 UTF-8 validity after the line-95 repair
$ iconv -f UTF-8 -t UTF-8 docs/specs/2026-11-10-live-signal-topology.md > /dev/null && echo valid-utf8
valid-utf8
(exit 0)

$ iconv -f UTF-8 -t UTF-8 docs/specs/2026-07-16-b2-noise-area-ruleset.md > /dev/null && echo valid-utf8
valid-utf8
(exit 0)

$ iconv -f UTF-8 -t UTF-8 docs/specs/2026-11-10-f2-session-flat-proposal.md > /dev/null && echo valid-utf8
valid-utf8
(exit 0)

$ iconv -f UTF-8 -t UTF-8 MANIFEST.md > /dev/null && echo valid-utf8
valid-utf8
(exit 0)

$ sed -n 95p docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -o 'SPEC_RUBRIC.md`:93–94 at HEAD'
SPEC_RUBRIC.md`:93–94 at HEAD
(exit 0)

$ git log -1 --format='%h %s' c29d08b | cut -c1-60
c29d08b rubric: F2 moved FROZEN to PASSED@e3323a8 (filer not
(exit 0)

## E10 other moved rubric citations (observed, not fixed)
$ grep -n -o -a -E 'SPEC_RUBRIC\.md`:[0-9]+(–[0-9]+)?' docs/specs/2026-11-10-f2-session-flat-proposal.md docs/specs/2026-11-10-live-signal-topology.md
docs/specs/2026-11-10-f2-session-flat-proposal.md:8:SPEC_RUBRIC.md`:43–44
docs/specs/2026-11-10-f2-session-flat-proposal.md:61:SPEC_RUBRIC.md`:108–113
docs/specs/2026-11-10-f2-session-flat-proposal.md:69:SPEC_RUBRIC.md`:37–42
docs/specs/2026-11-10-f2-session-flat-proposal.md:92:SPEC_RUBRIC.md`:43–44
docs/specs/2026-11-10-f2-session-flat-proposal.md:95:SPEC_RUBRIC.md`:93–94
docs/specs/2026-11-10-live-signal-topology.md:7:SPEC_RUBRIC.md`:28–29
docs/specs/2026-11-10-live-signal-topology.md:112:SPEC_RUBRIC.md`:30
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -E '^### (F1|F2|O4)|^\*\*Why frozen\.\*\* The plan|^\*\*Blocks\.\*\* Block 3 entirely'
65:### F1 — Signal-path topology vs. circuit-breaker placement
77:**Blocks.** Block 3 entirely. Any SHM threshold derivation.
81:### F2 — Session-flat time vs. breakers #4 and #5
87:**Why frozen.** The plan itself carried the contradiction — the strategy
114:### O4 — Backtest-vs-live configuration parity
(exit 0)

## E11 S6 grep script output
$ bash /tmp/fgd/s6.sh
### T: topology cited at :41 :48 :54 :61 :62 :74 :86
HEAD:DECISIONS.md:2058:**The deviation this entry records (S4).** CLAUDE.md states the signal flow as "TradingView alert → webhook → n8n workflow → …" (quoted from CLAUDE.md itself, more fully than the topology doc's :48). For the
HEAD:DECISIONS.md:2155:3. MFFU's "we do not offer Rithmic" (return-handoff :120) contradicts D-2026-11-10-B's broker route (DECISIONS.md:2054: "The path in full is the one at :41."; the topology path ends "→ Rithmic → account.", `
HEAD:DECISIONS.md:2247:The Phase 3 spec is a faithful import, so :100 and :101 are not rewritten. The amendment is a labelled section appended at the end of that file ("Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2
HEAD:docs/reports/2026-11-11-mffu-connection-investigation.md:50:- `docs/specs/2026-11-10-live-signal-topology.md:41` — "SubmitBracket → Rithmic → account" [OBSERVED]
HEAD:docs/reports/2026-11-11-mffu-connection-investigation.md:88:- `docs/specs/2026-11-10-live-signal-topology.md:41` — Breaker placement downstream terminal point labeled `SubmitBracket → Rithmic → account` [OBSERVED].
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md:137:TOP41_tail	docs/specs/2026-11-10-live-signal-topology.md:41	→ Rithmic → account.
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker7.md:71:3. MFFU's "we do not offer Rithmic" (return-handoff :120) contradicts D-2026-11-10-B's broker route (DECISIONS.md:2054: "The path in full is the one at :41."; the topolog
(count: 7)
### T: topology 'section 3' or '#5 row' citations
HEAD:docs/specs/2026-11-05-phase3-build-specification.md:244:Breakers #1, #2, #3, #6, #7, #8 and #9 and their values; the Block 3 state management, fallback script and milestone text; Blocks 1, 2, 4 and 5. Where #4 and #5 sit on t
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:40:Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system entry block i
HEAD:docs/specs/2026-11-10-live-signal-topology.md:44:1. Every one of the nine breakers must sit upstream of order submission on the live path. Under this topology, every gate check runs before `SubmitBracket` (table, section 3). 
(count: 3)
### R: ruleset cited at :8 :79 :84 :99 :105 (incl. sed -n and Spec L)
HEAD:docs/reports/2026-10-30-3gm-fidelity-check.md:644:$ sed -n '99,99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
HEAD:docs/reports/2026-10-30-3gm-worker1-checklist.md:757:**Rule:** the paper "acts on the **stamp**". Spec L99 (spec §6, an implementation note, not a paper rule) offers `EnterLongStopMarket/EnterShortStopMarket` as "a reasonable
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md:266:| W4-11 | ""**T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** ... Trader must decide the flat time"" | docs/specs/2026-07-16-b2-noise-area-
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md:2076:# docs/specs/2026-07-16-b2-noise-area-ruleset.md:79  (users W4-11)
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md:2079:# docs/specs/2026-07-16-b2-noise-area-ruleset.md:105  (users W4-11)
(count: 5)
### R: ruleset items D8 / T1 cited
(count: 0)
### P: proposal :8 or :79 cited
HEAD:DECISIONS.md:2108:**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:0
HEAD:DECISIONS.md:2272:This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and records the amendment of #4 and #5. It does not grade the clause and does not change F2's state. The F2 state move is a later, s
HEAD:DECISION_LOG.md:830:- [2026-11-11T19:30:00Z] WHO: praxis-master | WHAT: **Filing unit manager (ab1ae55da6b5b6948) returned `Result: PASS`; report and entries read on disk.** D-2026-11-11-A at DECISIONS.md:2101–2174 and D-2026
HEAD:DECISION_LOG.md:834:- [2026-11-11T21:06:30Z] WHO: praxis-master | WHAT: **Session start (`claude -p`, prompt = ritual plus "Resume from HANDOFF.md. Apply D-2026-11-08-D D1-D5 ... Run units until done").** OBSERVED: `claude --
HEAD:HANDOFF.md:90:3. Still open from earlier: the 16:00Z Hermes-replies grading unit (manager report reads `(pending)`); broker route (MFFU does not offer Rithmic; D-2026-11-10-B contradicted, not re-decided); F2 breaker #4/#5 sp
HEAD:docs/reports/2026-11-11-v-rulings-filing-manager.md:173:  (3) F2 proposal :8 cites the rubric's unblock clause at :43–44; it is at :30–31 now.
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md:130:PROP79	docs/specs/2026-11-10-f2-session-flat-proposal.md:79	Adoption of Rule F2-1.
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md:214:OK  ['proposal:79']  "Adoption of Rule F2-1."
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md:311:`docs/specs/2026-11-10-f2-session-flat-proposal.md`:8 cites the F2 unblock clause as `specs/SPEC_RUBRIC.md`:43–44. In the current rubric it is at :30–31 (grep above). D-
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker10.md:160:--- docs/specs/2026-11-10-f2-session-flat-proposal.md:79
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker3.md:198:DECISIONS.md:2108 (Entry A): "... This answers the A6 hold, OPEN-F2-5 at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 ..."
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker3.md:217:- OPEN-F2-5 (proposal :79) needs three things: Amear's approval, a DECISIONS entry, and the amended #4/#5 text. Only the first exists, and it covers the channel's summar
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker3.md:219:- Fix: replace with "Recorded against the A6 hold (OPEN-F2-5, proposal :79). Whether his approval of the summary meets A6's 'approves the proposed values' is not graded 
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker3.md:256:**13. Out of scope, reported only (not this unit's lines).** One of the four removed IPv4 identifiers is already in the tree at HEAD: DECISIONS.md:1004 and :1016, and DE
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker5.md:14:2. Pulled every cited source line by `sed -n`: proposal :79, return-handoff :46 and :53, DECISIONS.md:1740–1748 (A6), :2076–2097 (D-2026-11-10-C, IPv4 masked on display),
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker5.md:22:- Fix 1: the first mention keeps the full path `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79. The short name "proposal" is defined in that same sentence, so "pro
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker5.md:119:2108	... Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, OPEN-F2-5 at `docs/specs/2026-11-10-f2-session-flat-proposal.
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker6.md:164:proposal :79: | OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker6.md:218:**M2 — MAJOR (S2).** DECISIONS.md:2108 says V2 is "filed as closing the A6 hold, OPEN-F2-5 at proposal:79". OPEN-F2-5's own resolution column (proposal :79, pasted above
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker7.md:14:2. Read the source lines: proposal :79, DECISION_LOG.md :828 and :829, DECISIONS.md :2082, :2085, :2089, :1744–1745, :2054, topology :41, return-handoff :72.
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker7.md:67:**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position o
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker7.md:83:MATCH  docs/specs/2026-11-10-f2-session-flat-proposal.md:79 <- DECISIONS.md:2108  [Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the 
(count: 22)
### P: stale rubric citation SPEC_RUBRIC.md:43-44
HEAD:DECISIONS.md:2272:This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and records the amendment of #4 and #5. It does not grade the clause and does not change F2's state. The F2 state move is a later, s
HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md:311:`docs/specs/2026-11-10-f2-session-flat-proposal.md`:8 cites the F2 unblock clause as `specs/SPEC_RUBRIC.md`:43–44. In the current rubric it is at :30–31 (grep above). D-
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:8:This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes no rubric state. F2 unblocks when "A DECISIONS.md entry names the governing
(count: 3)
(exit 0)

## E12 de-identification, final report included
$ bash /tmp/fgd/deid.sh
email-pattern: 0
paper-author-surnames: 0
med-terms: 0
(exit 0)

## E13 current hashes, MANIFEST :451, worker report checks
$ shasum docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md
5865a1121cd1b55783f217c4f341e20b7cfc03d5  docs/specs/2026-11-10-live-signal-topology.md
b68c098f4aa1d3273ad179474299d662f1e0c243  docs/specs/2026-07-16-b2-noise-area-ruleset.md
24598c3d73d8dd3a3961a7083aa8e42a68012362  docs/specs/2026-11-10-f2-session-flat-proposal.md
(exit 0)

$ sed -n 451p MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-12-fgd-doc-alignment-worker2.md 
(exit 0)

$ git diff --numstat HEAD -- MANIFEST.md
20	0	MANIFEST.md
(exit 0)

$ tail -n 1 docs/reports/2026-11-12-fgd-doc-alignment-worker1.md; tail -n 1 docs/reports/2026-11-12-fgd-doc-alignment-worker2.md
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
(exit 0)

$ grep -n -E '^Verdict:|^\*\*Verdict' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:562:Verdict: PASS
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:326:Verdict: PASS
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:399:Verdict: PASS
(exit 0)

$ grep -c -F '<…>' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md || true
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:0
(exit 0)

$ grep -c -E '^\$ .*\.\.\.' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md || true
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:0
(exit 0)

$ bash /tmp/fgd/deid.sh
email-pattern: 0
paper-author-surnames: 0
med-terms: 0
(exit 0)

## E14 Correction-1 re-run evidence (2026-11-12)
(re-run 2026-11-12 by correction-1, script /tmp/fgdc1/ev-manager.sh; worker1/worker2 lines are read from the pre-correction copies in /tmp/fgdc1/orig)

$ git rev-parse --short HEAD
006a08b
(exit 0)

### E14a worker report lines (pre-correction copies)
$ grep -n -E '^Verdict:' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
562:Verdict: PASS
(exit 0)

$ wc -l < /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
     564
(exit 0)

$ awk '/^```/{f=!f} index($0,"..."){print NR": "(f?"in-fence":"prose")}' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
314: prose
553: prose
555: prose
(exit 0)

$ sed -n 553p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-110
2. **MINOR — topology :136 (aligned reading for :41).** "...('the n8n/consumer window check is then removed');
(exit 0)

$ sed -n 555p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-150
4. **MINOR — proposal :103 (F-9).** The note opens "OPEN-F2-5 is closed." without qualification. The item's decider is "Amear's approval under A6; the
(exit 0)

$ sed -n 86,88p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-120
docs/specs/2026-11-10-live-signal-topology.md body 1-114 BYTE-IDENTICAL; total lines now      200; sha1 5aea715d2ff4
docs/specs/2026-07-16-b2-noise-area-ruleset.md body 1-111 BYTE-IDENTICAL; total lines now      170; sha1 b68c098f4aa1
docs/specs/2026-11-10-f2-session-flat-proposal.md body 1-81 BYTE-IDENTICAL; total lines now      111; sha1 e1d2d72895b3
(exit 0)

$ sed -n 552p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md | grep -o 'I did not make this edit, and I do not know who did.'
I did not make this edit, and I do not know who did.
(exit 0)

$ sed -n 35,37p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md
5865a1121cd1b55783f217c4f341e20b7cfc03d5  docs/specs/2026-11-10-live-signal-topology.md
b68c098f4aa1d3273ad179474299d662f1e0c243  docs/specs/2026-07-16-b2-noise-area-ruleset.md
24598c3d73d8dd3a3961a7083aa8e42a68012362  docs/specs/2026-11-10-f2-session-flat-proposal.md
(exit 0)

$ sed -n 374p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md | cut -c1-80
Observation, not a break: D-2026-11-12-A never names OPEN-F2-5 (C6 grep is empty
(exit 0)

$ sed -n 397p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker2.md | cut -c1-80
Findings count: 0 breaks. 1 observation: D-2026-11-12-A does not itself name OPE
(exit 0)

### E14b F2 amendment report follow-up list (HEAD)
$ git show HEAD:docs/reports/2026-11-12-f2-breaker-amendment-manager.md | grep -n -E '^### Follow-ups|^- F-(1|2|3|7|9):' | cut -c1-75
132:### Follow-ups (named, not fixed)
134:- F-1: topology doc :41, :48, :62, :74, :86 — #5 still placed as a syst
135:- F-2: topology doc :54, :61–62 — breaker names for #4/#5; F1 bearing.
136:- F-3: Noise-Area ruleset :8, :79, :84, :99, :105 — 09:30–11:30 window 
140:- F-7: F2 proposal :8 rubric line citation.
142:- F-9: OPEN-F2-5 (proposal :79) closure, with the F2 state move.
(exit 0)

### E14c DECISIONS.md (HEAD)
$ git show HEAD:DECISIONS.md | wc -l
    2278
(exit 0)

$ git show HEAD:DECISIONS.md | grep -n '^## ' | tail -n 2 | cut -c1-70
2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by A
2205:## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to mat
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 1744,1745p
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 2108p | grep -o 'OPEN-F2-5 is not closed by this entry'
OPEN-F2-5 is not closed by this entry
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 2232p | grep -o "The proposal's replacement text for breakers #4 and #5 is adopted"
The proposal's replacement text for breakers #4 and #5 is adopted
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 2247p | grep -o 'other specs cite (topology doc :24, :61, :89; proposal :67)'
other specs cite (topology doc :24, :61, :89; proposal :67)
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 2272p | grep -o -E 'SPEC_RUBRIC.md.:43–44.{0,27}'
SPEC_RUBRIC.md`:43–44); the clause is at :30–31.
(exit 0)

$ git show HEAD:DECISIONS.md | sed -n 2204,2278p | grep -c 'OPEN-F2-5' || true
0
(exit 0)

### E14d rubric
$ git show e3323a8:specs/SPEC_RUBRIC.md | sed -n 30,31p
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 63p | grep -o 'nine breakers by name'
nine breakers by name
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 68,69p
trading signal, and showing how each of the nine circuit breakers sits upstream
of order submission on that path.
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 75,76p
**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
and the auditor confirms it addresses every one of the nine breakers by name.
(exit 0)

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 79p | grep -o 'Residuals named there and in bead .Praxis_build-fgd.'
Residuals named there and in bead `Praxis_build-fgd`
(exit 0)

### E14e Phase 3 spec (HEAD; no working-tree diff)
$ git diff --quiet HEAD -- docs/specs/2026-11-05-phase3-build-specification.md && echo NO-DIFF
NO-DIFF
(exit 0)

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | wc -l
     244
(exit 0)

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n 97,105p | cut -c1-45
1. Daily loss limit — unrealized + realized P
2. Max trades per day — trade count hits dail
3. Consecutive loss (“two and done”) — 2 cons
4. Session time gate — clock hits 11:30 ET → 
5. Afternoon session window — clock enters 3:
6. Trailing drawdown proximity — account appr
7. Max position size — order quantity exceeds
8. Stale signal filter — signal file older th
9. Heartbeat dead-man switch — if n8n hasn’t 
(exit 0)

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n 190p
## Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)
(exit 0)

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | grep -n -o -F -e 'cancel working entry orders' -e 'confirm flat before 4:10 PM ET (alert if not)' -e 'which this amendment does not edit'
212:cancel working entry orders
212:confirm flat before 4:10 PM ET (alert if not)
244:which this amendment does not edit
(exit 0)

### E14f topology (body lines at HEAD; note lines in the working tree)
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n '' | sed -n '41p;48p;54p;61p;62p;74p;78p;86p;105p' | cut -c1-100
41:Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default 
48:**What changes from the Block 1 architecture.** The emitter is NT8, not TradingView (CLAUDE.md "S
54:Names are exactly as the Phase 3 import lists them (`docs/specs/2026-11-05-phase3-build-specifica
61:| 4 | Session time gate | Two checks: an n8n gate node before Write Signal File (ET clock; entrie
62:| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal
74:| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before 
78:Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, position and clock.
86:| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incomi
105:| OPEN-T8 | How R8's lockout on Amear's own interaction 15:00–18:00 is enforced, since manual or
(exit 0)

$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n -o -F -e 'all nine checks move into the strategy' -e 'the n8n/consumer window check is then removed'
62:the n8n/consumer window check is then removed
78:all nine checks move into the strategy
(exit 0)

$ grep -n -o -F 'Session flat gate' docs/specs/2026-11-10-live-signal-topology.md
124:Session flat gate
152:Session flat gate
160:Session flat gate
(exit 0)

$ grep -n -o -F 'Session window (operator lockout)' docs/specs/2026-11-10-live-signal-topology.md
128:Session window (operator lockout)
152:Session window (operator lockout)
168:Session window (operator lockout)
(exit 0)

$ grep -n -o -F 'found by this unit' docs/specs/2026-11-10-live-signal-topology.md
178:found by this unit
(exit 0)

$ grep -c -F 'replacement text (DECISIONS.md:2232)' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

$ grep -c -F 'where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105), not decided here.' docs/specs/2026-11-10-live-signal-topology.md
1
(exit 0)

### E14g ruleset body lines (HEAD)
$ git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -n '' | sed -n '8p;79p;84p;99p;105p' | cut -c1-100
8:> **Scope note.** The paper studies **SPY** (the ETF), NOT NQ futures, and trades **all day** (eve
79:| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET 
84:**Net:** The RTF prose is a faithful summary of the paper on band/gap/sizing/16:00-flat, but thre
99:Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = ma
105:- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The pap
(exit 0)

### E14h proposal (HEAD body; working-tree note)
$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -n '' | sed -n '3p;8p;24p;40p;79p' | cut -c1-100
3:Status: PROPOSED. F2 stays FROZEN until Amear approves (A6, DECISIONS.md:1744)
8:This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes 
24:- Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit 
40:Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section
79:| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and t
(exit 0)

$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | sed -n 8p | grep -o -F 'DECISIONS.md:1744–1745'
DECISIONS.md:1744–1745
(exit 0)

$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | sed -n 40p | grep -o -F 'if adopted, the system window check is removed and only the operator lockout remains'
if adopted, the system window check is removed and only the operator lockout remains
(exit 0)

$ grep -c -F "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits." docs/specs/2026-11-10-f2-session-flat-proposal.md
1
(exit 0)

### E14i other cited records (HEAD)
$ git show HEAD:DECISION_LOG.md | sed -n 830p | grep -o -E '.{0,25}:43–44.{0,22}'
es the rubric unblock at :43–44 (it is at :30–31); th
(exit 0)

$ git show HEAD:HANDOFF.md | sed -n 90p | grep -o -E '.{0,25}:43–44.{0,30}'
proposal :8 cites rubric :43–44 for the unblock clause (it is
(exit 0)

$ git show HEAD:docs/reports/2026-11-11-v-rulings-filing-manager.md | sed -n 173p | grep -o -E '.{0,25}:43–44.{0,25}'
bric's unblock clause at :43–44; it is at :30–31 now.
(exit 0)

$ git show HEAD:docs/reports/2026-11-11-v-rulings-filing-worker1.md | sed -n 311p | grep -o -E '.{0,25}:43–44.{0,40}'
as `specs/SPEC_RUBRIC.md`:43–44. In the current rubric it is at :30–31 
(exit 0)

$ git show HEAD:docs/reports/2026-11-11-v-rulings-filing-manager.md | sed -n 181p | grep -o 'OPEN-F2-5 is not closed'
OPEN-F2-5 is not closed
(exit 0)

$ git show HEAD:docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | sed -n 361,362p | cut -c1-120
$ sed -n 2108p DECISIONS.md | grep -o 'The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry.
The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry.
(exit 0)

$ git show HEAD:docs/reports/2026-11-09-d11-sweep-manager.md | sed -n 266p | grep -o -F 'the live 11:30 flat is breaker #4'
the live 11:30 flat is breaker #4
(exit 0)

### E14j strategy code (HEAD; no working-tree diff)
$ git diff --quiet HEAD -- ninjascript/PraxisNoiseAreaBreakout.cs && echo NO-DIFF
NO-DIFF
(exit 0)

$ git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | sed -n 188,191p
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
(exit 0)

### E14k build script quoting function and its calls
$ grep -n -E '^q\(\)|^q ' /tmp/fgd/build.sh
8:q() { echo '```text'; git show "HEAD:$1" | sed -n "${2}p"; echo '```'; }
39:q $T 41
47:q $T 48
55:q $T 54
63:q $T 61
71:q $T 62
79:q $T 74
87:q $T 78
95:q $T 86
124:q $R 8
132:q $R 79
140:q $R 84
148:q $R 99
156:q $R 105
178:q $P 8
186:q $P 79
194:q $P 3
(exit 0)

### E14k2 S6 script line cut
$ grep -n -o 'cut -c1-230' /tmp/fgd/s6.sh
4:cut -c1-230
(exit 0)

### E14l saved evidence outputs vs the pre-correction E1-E13 block; mtimes
$ sed -n 90,433p /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md | cmp - <(cat /tmp/fgd/evidence.txt /tmp/fgd/evidence2.txt /tmp/fgd/e13.txt) && echo IDENTICAL
IDENTICAL
(exit 0)

$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md MANIFEST.md /tmp/fgd/evidence.txt /tmp/fgd/evidence2.txt /tmp/fgd/e13.txt
2026-11-12T08:19:44 docs/specs/2026-11-10-live-signal-topology.md
2026-11-12T08:10:48 docs/specs/2026-07-16-b2-noise-area-ruleset.md
2026-11-12T08:19:44 docs/specs/2026-11-10-f2-session-flat-proposal.md
2026-11-12T08:24:38 MANIFEST.md
2026-11-12T08:25:05 /tmp/fgd/evidence.txt
2026-11-12T08:25:06 /tmp/fgd/evidence2.txt
2026-11-12T08:25:06 /tmp/fgd/e13.txt
(exit 0)

### E14m MANIFEST.md (working tree)
$ git diff -U0 HEAD -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -431,0 +440,12 @@
(exit 0)

$ sed -n '307,314p;440,451p' MANIFEST.md | cut -d'|' -f2
 /docs/specs/2026-11-06-walk-forward-values.md 
 /docs/specs/2026-11-05-walk-forward-spec.md 
 /docs/reports/2026-11-08-wf-spec-amendment-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md 
 /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md 
 /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch 
 /docs/reports/2026-11-12-r6-engine-entry-manager.md 
 /docs/reports/2026-11-12-r6-engine-entry-worker1.md 
 /docs/reports/2026-11-12-r6-engine-entry-worker2.md 
 /DECISIONS.md 
 /docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md 
 /docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md 
 /docs/specs/2026-11-10-live-signal-topology.md 
 /docs/specs/2026-07-16-b2-noise-area-ruleset.md 
 /docs/specs/2026-11-10-f2-session-flat-proposal.md 
 /docs/reports/2026-11-12-fgd-doc-alignment-manager.md 
 /docs/reports/2026-11-12-fgd-doc-alignment-worker1.md 
 /docs/reports/2026-11-12-fgd-doc-alignment-worker2.md 
(exit 0)

### E14n paths of the E8 set with no diff against HEAD
$ git diff --quiet HEAD -- specs/SPEC_RUBRIC.md docs/specs/2026-11-05-phase3-build-specification.md ninjascript HANDOFF.md STATUS.md && echo NO-DIFF
NO-DIFF
(exit 0)

```

## Adversarial findings

worker1 (`docs/reports/2026-11-12-fgd-doc-alignment-worker1.md`, ADVERSARIAL, `Verdict: PASS` at its line 562 (E13, E14), graded on sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3` (its lines 86–88, E14)). Its report was read on disk (Findings section, verdict line, last line) and scanned for placeholders. Dispositions:

1. MAJOR, observed and already cured: proposal note line 95 held invalid UTF-8 where `:93–94` should be. This is the defect the manager found and repaired during the review (process log step 4; E9). The repair was the manager's edit (worker1 could not tell who made it: its line 552, E14).
2. MINOR, topology note aligned reading for :41, "D-2026-11-12-A adopts that text". Cured: now reads that D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232) and that proposal :40 states the window check is then removed (E14).
3. MINOR, topology note aligned reading for :78, "its operator lockout cannot sit in the strategy either". Cured: now leaves where the lockout sits, including whether the strategy could carry it, to OPEN-T8 (:105), not decided here (E14).
4. MINOR, proposal note :79 lead sentence unqualified. Cured: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits." (E14)
5. MINOR, process: files changed during the review. Answered by worker2 below, which graded the current hashes.

worker2 (`docs/reports/2026-11-12-fgd-doc-alignment-worker2.md`, ADVERSARIAL narrow re-check of cures 1–4, `Verdict: PASS`, 0 breaks, 1 observation). Its current-file sha1s: topology `5865a1121cd1`, ruleset `b68c098f4aa1`, proposal `24598c3d73d8` (worker2 :35–37, E14); these match the `shasum` output in E13 below. Its observation (worker2 :374, E14): D-2026-11-12-A never names OPEN-F2-5 (DECISIONS.md:2204–2278 at HEAD has 0 hits, E14), so "closed" is the note's own reading of the three records the item's own column names; recorded here as a residual, not changed (the master's brief asks for the F-9 closure).

Residual on the evidence rules, stated honestly: worker1's Findings prose (its lines 553 and 555 in the pre-correction copy, E14) quotes note text with "..." elisions inside quotation marks. Those are quotations in prose, not commands and not cut output; its commands and outputs carry no `...` or `<…>` placeholders (E13 scan; E14: every line with `...` is outside a fence, including one more prose elision at its line 314, outside Findings). The worker report was not edited by the manager.

## Files changed by this unit (working tree only)

- `docs/specs/2026-11-10-live-signal-topology.md` — 86 added, 0 removed; body :1–114 byte-identical to HEAD.
- `docs/specs/2026-07-16-b2-noise-area-ruleset.md` — 59 added, 0 removed; body :1–111 byte-identical.
- `docs/specs/2026-11-10-f2-session-flat-proposal.md` — 30 added, 0 removed; body :1–81 byte-identical.
- `MANIFEST.md` — 6 rows appended at :446–451 (working-tree positions) after the 14 uncommitted rows of other units (diff vs HEAD now 20 added, 0 removed: 14 of other units + 6 this unit; E2, E14).
- `docs/reports/2026-11-12-fgd-doc-alignment-manager.md` (this file), `-worker1.md`, `-worker2.md` — new.

Not edited: DECISIONS.md, specs/SPEC_RUBRIC.md, the Phase 3 spec, the walk-forward spec and values, ninjascript/, ledgers, .claude/ (E8 lists the paths in that set that differ from HEAD; specs/SPEC_RUBRIC.md, the Phase 3 spec, ninjascript/, HANDOFF.md and STATUS.md show no diff, E14. For the paths that do differ, no session-start snapshot was pasted, so that this unit did not edit them is not shown by pasted output.)

## MANIFEST rows added

MANIFEST.md:446 (topology), :447 (ruleset), :448 (proposal), :449 (this report), :450 (worker1), :451 (worker2), working-tree positions. Output in E6, E13 and E14.

## Files staged

None by this unit. The index holds one path, the PNG listed in E1. The master builds the index.

## Result

All five follow-ups are aligned by appended notes, and the bodies are unchanged. Two OPEN items (OPEN-A1, OPEN-A2) are recorded with both readings and not chosen. All nine breaker names are still present. The S6 table is graded, both adversarial checks are on disk, and the one MAJOR found has been cured and re-checked. The breakers remain SPECIFIED ONLY.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
