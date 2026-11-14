# 2026-11-14 dirty-tree-sort — worker 4 report

## Task
Classify 31 untracked items (27 reports dated 2026-10-26..2026-11-11 from g4.txt, plus 4 vm/replies files of 2026-11-10) as CLEAR-FILE / CLEAR-BUT-NEEDS-AUDIT / UNCLEAR. Read-only.

## Mode
BUILD (read-only research). Unit 2026-11-14-dirty-tree-sort, worker 4.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S7, S8 (per preamble). Rep name never printed (bead Praxis_build-c2w); `[rep]` substitutes.

## Process log
1. Read preamble and g4.txt.
2. Name counts, mtimes, tracked status, Result lines (below).
3. Ledger greps per slug (E4), context windows (E5), AUDIT_LOG read-only greps (E6), commits and filed siblings (E7), beads (E8), VM reply timestamps (E9).
4. Classified the items by group and ran the name check on this report.
About 31 tool calls in total.

## Verification evidence

### E1. Name count / mtime / tracked (0 = untracked) — `date +%z` = -0500 (mtimes are local)

```
$ for f in ...; do printf '%s | %s | %s | %s\n' "$(grep -ci "$N" "$f")" "$(stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' "$f")" "$(git ls-files "$f" | wc -l)" "$f"; done | sed "s/$N/[rep]/Ig"
0 | 2026-10-26T07:58:03 | 0 | docs/reports/2026-10-26-nightly-spec-request-review.md
6 | 2026-10-28T17:06:52 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-adversarial-addendum.md
7 | 2026-10-28T17:23:10 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-adversarial-confirm.md
6 | 2026-10-28T17:16:55 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-adversarial-final.md
4 | 2026-10-28T17:11:39 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-adversarial-recheck.md
9 | 2026-10-28T17:00:22 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-adversarial-transcript.md
10 | 2026-10-28T16:57:05 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-worker1.md
19 | 2026-10-28T17:03:31 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-worker3.md
5 | 2026-10-28T17:08:14 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-worker5-fix.md
2 | 2026-10-28T17:13:03 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-worker7-fix.md
6 | 2026-10-28T17:18:14 | 0 | docs/reports/2026-10-28-f4-[rep]-reply-worker9-fix.md
0 | 2026-10-28T17:35:59 | 0 | docs/reports/2026-10-28-review-note-delivery.md
0 | 2026-10-31T13:06:52 | 0 | docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md
0 | 2026-11-01T16:57:37 | 0 | docs/reports/2026-11-01-csv-analyses-fix-manager-record.md
0 | 2026-11-01T09:11:26 | 0 | docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md
0 | 2026-11-08T12:02:18 | 0 | docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
0 | 2026-11-08T12:17:52 | 0 | docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md
0 | 2026-11-08T12:19:55 | 0 | docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md
0 | 2026-11-09T01:15:12 | 0 | docs/reports/2026-11-08-wf-spec-amendment-manager.md
0 | 2026-11-09T14:17:51 | 0 | docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md
0 | 2026-11-09T01:31:01 | 0 | docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md
1 | 2026-11-10T04:26:05 | 0 | docs/reports/2026-11-10-scrub-forward-c1-adversarial.md
0 | 2026-11-11T11:16:54 | 0 | docs/reports/2026-11-11-hermes-replies-grading-manager.md
14 | 2026-11-11T12:03:42 | 0 | docs/reports/2026-11-11-hermes-replies-grading-worker1.md
0 | 2026-11-11T11:26:28 | 0 | docs/reports/2026-11-11-hermes-replies-grading-worker2.md
2 | 2026-11-11T11:40:14 | 0 | docs/reports/2026-11-11-hermes-replies-grading-worker4.md
0 | 2026-11-11T11:58:01 | 0 | docs/reports/2026-11-11-hermes-replies-grading-worker6.md
0 | 2026-11-10T16:46:36 | 0 | vm/replies/20261110T214542Z-STATUS.md
0 | 2026-11-10T16:48:54 | 0 | vm/replies/20261110T214834Z-self-report.md
0 | 2026-11-10T16:50:17 | 0 | vm/replies/20261110T215014Z-STATUS.md
0 | 2026-11-10T16:49:56 | 0 | vm/replies/20261110T224920Z-2b-skill-job.md
```
Manager-measured counts re-checked: all match (ten F4 files 2-19; scrub-forward-c1-adversarial 1; hermes worker1 14; worker4 2; all others 0).

### E2. Result lines
```
$ grep -n '^\**Result' <f> | tail -2   (then for blanks: grep -niE '^(#+ *)?(\*\*)?(result|verdict)')
2026-10-26-nightly-spec-request-review.md: (none)
f4-[rep]-reply-adversarial-addendum.md: 147:Result: FAIL
f4-[rep]-reply-adversarial-confirm.md: 165:Result: PASS
f4-[rep]-reply-adversarial-final.md: 146:Result: FAIL
f4-[rep]-reply-adversarial-recheck.md: 130:Result: FAIL
f4-[rep]-reply-adversarial-transcript.md: 128:## Result / 131:VERDICT: DISCREPANCIES FOUND (2)
f4-[rep]-reply-worker1.md: 110:## Result: PASS
f4-[rep]-reply-worker3.md: 296:Result: PASS
f4-[rep]-reply-worker5-fix.md: 100:Result: PASS
f4-[rep]-reply-worker7-fix.md: 78:## Result: PASS
f4-[rep]-reply-worker9-fix.md: 81:## Result: PASS
2026-10-28-review-note-delivery.md: 104:Result: PASS
2026-10-31-voice-handoff-future-row-walkthrough.md: (none)
2026-11-01-csv-analyses-fix-manager-record.md: 33:Result: PASS / 52:Result: PASS (scoped to the mechanical check: one hunk, line 37 only, 695 lines)
2026-11-01-three-strategy-results-s2-fix-manager-record.md: 64:Result: BLOCKED. The six edits are applied, and the diff above verifies them. The verdict is pending the auditor's re-grade on S2, which the manager may not
2026-11-08-wf-spec-amendment-correction-1-manager.md: 104:## Result: PASS at level WRITTEN
2026-11-08-wf-spec-amendment-correction-2-manager.md: 302:**Result: PASS** at level WRITTEN. This is the producer's claim, not a grade: ...
2026-11-08-wf-spec-amendment-correction-3-manager.md: 109:## Result: PASS at level WRITTEN
2026-11-08-wf-spec-amendment-manager.md: 411:Result: PASS at level WRITTEN.
2026-11-09-c7-probe-fresh-manifest-manager.md: 91:Result: PASS
2026-11-09-wf-spec-amendment-resume-manager.md: 587:Result: PASS / 624:Result: PASS
2026-11-10-scrub-forward-c1-adversarial.md: 98:Result: FAIL
2026-11-11-hermes-replies-grading-manager.md: 75:Result: (pending)
2026-11-11-hermes-replies-grading-worker1.md: 1114:Result: PASS
2026-11-11-hermes-replies-grading-worker2.md: 320:Result: FAIL
2026-11-11-hermes-replies-grading-worker4.md: 300:Result: FAIL
2026-11-11-hermes-replies-grading-worker6.md: 287:Result: FAIL
vm/replies/20261110T214542Z-STATUS.md: 1 line "STARTED"
vm/replies/20261110T214834Z-self-report.md: 113 lines, header "RESULT: DONE", REPLY-TO step 1, UTC 20261110T214834Z
vm/replies/20261110T215014Z-STATUS.md: 1 line "FINISHED"
vm/replies/20261110T224920Z-2b-skill-job.md: 39 lines, header "RESULT: DONE", REPLY-TO step 2, UTC 20261110T224920Z
```

### E3. Tracked vm/replies siblings
```
$ git ls-files vm/replies
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
vm/replies/20261111T172802Z-STATUS.md
vm/replies/20261111T172933Z-python-git-install.md
vm/replies/20261111T172940Z-STATUS.md
vm/replies/README.md
```

### E4. Ledger rows per slug (DECISION_LOG = DL, DISPATCH_LOG = DPL), trimmed to 200 chars, name-substituted
```
$ for s in <slugs>; do for L in DECISION_LOG.md DISPATCH_LOG.md; do echo "== $s $L count=$(grep -c -- "$s" $L)"; grep -n -- "$s" $L | cut -c1-200 | tail -3; done; done | sed "s/$N/[rep]/Ig"
== nightly-spec-request-review DECISION_LOG.md count=1
433:- [2026-10-28T20:49:38Z] WHO: praxis-master | WHAT: **CORRECTION BY APPEND to row 432: the review note was LOST before audit; the master's earlier "nothing's really lost" was overstated.** Observe
== nightly-spec-request-review DISPATCH_LOG.md count=0
== f4-[rep]-reply DECISION_LOG.md count=2
438:- [2026-10-28T21:33:00Z (approximate)] WHO: praxis-master | WHAT: **AUDIT PASS: F4 "[rep]" reply filing.** The grade is appended at `docs/reports/2026-10-28-f4-[rep]-reply-filing.md:393-465`, ending
806:- [2026-11-10T17:01:00Z] WHO: praxis-master | WHAT: **SESSION START, timer run (`claude -p`, pid 69572, cwd this tree), `date -u` 17:00:42Z.** ...
== f4-[rep]-reply DISPATCH_LOG.md count=0
== review-note-delivery DECISION_LOG.md count=1
441:- [2026-10-30T21:36:00Z] **WHO: amear** | PROPOSED BY: amear (voice/chat session 2026-10-28 → 10-30, hand-run) | ...
== review-note-delivery DISPATCH_LOG.md count=0
== voice-handoff-future-row DECISION_LOG.md count=1
632:- [2026-10-31T17:05:39Z] WHO: praxis-master | WHAT: **VOICE HANDOFF WRITTEN at Amear's request ("give me the handoff to take this back to the voice chat"): `docs/reports/2026-10-31-voice-handoff-f
== voice-handoff-future-row DISPATCH_LOG.md count=0
== csv-analyses-fix DECISION_LOG.md count=1
616:- [2026-11-01T21:58:19Z] WHO: praxis-master | WHAT: **FINAL RE-AUDIT PASS — unit `2026-11-01-csv-analyses`.** ...
== csv-analyses-fix DISPATCH_LOG.md count=1
1377:- [2026-11-01T21:58:19Z] WHO: praxis-master | WHAT: **UNIT `2026-11-01-csv-analyses` — AUDIT PASS; commit handed to Amear.** ...
== three-strategy-results-s2-fix DECISION_LOG.md count=1
622:- [2026-11-01T14:12:50Z] WHO: praxis-master | WHAT: **RE-AUDIT PASS — unit `2026-11-01-three-strategy-results`.** ...
== three-strategy-results-s2-fix DISPATCH_LOG.md count=1
1347:- [2026-11-01T14:12:50Z] WHO: praxis-master | WHAT: **UNIT `2026-11-01-three-strategy-results` — AUDIT PASS; commit handed to Amear.** ...
== wf-spec-amendment-correction DECISION_LOG.md count=3
737:- [2026-11-08T17:01:00Z] WHO: praxis-master | WHAT: **U7 `2026-11-08-wf-spec-amendment` RETURNED (60 tool uses — at the cap — ~47 min, ~190k tokens; `Result: PASS at level WRITTEN`; three adversar
738:- [2026-11-08T17:03:30Z] WHO: praxis-master | WHAT: **U7 CORRECTION 1 RETURNED (10 tool uses, ~2 min; `Result: PASS at level WRITTEN`; ...
739:- [2026-11-08T17:08:00Z] WHO: praxis-master | WHAT: **AUDIT (U7, `commit-idx-u7`) — FAIL 1 (11 tool uses, ~3 min). ...
== wf-spec-amendment-correction DISPATCH_LOG.md count=3
2033:- [2026-11-08T17:02:00Z] WHO: praxis-master | WHAT: U7 returned PASS-at-WRITTEN (60 tool uses, at the cap). ...
2034:- [2026-11-08T17:09:00Z] WHO: praxis-master | WHAT: U7 correction 1 returned PASS-at-WRITTEN (two line edits). U7 index audited FAIL 1 ...
2035:- [2026-11-08T17:19:00Z] WHO: praxis-master | WHAT: U7 correction 2 returned PASS-at-WRITTEN (35 tool uses, ~10 min; ...
== wf-spec-amendment-manager DISPATCH_LOG.md count=1
2032:- [2026-11-08T16:13:00Z] WHO: praxis-master | WHAT: U7 `2026-11-08-wf-spec-amendment` dispatched — praxis-manager amends `docs/specs/2026-11-06-walk-forward-values.md` (v2.1 → v2.2, ...
== wf-spec-amendment-resume DECISION_LOG.md count=0
== wf-spec-amendment-resume DISPATCH_LOG.md count=1
2155:- [2026-11-09T06:19:00Z] WHO: praxis-master | WHAT: U7 resume `2026-11-09-wf-spec-amendment-resume` (bead Praxis_build-diq, Amear C1: ...
== c7-probe-fresh-manifest DECISION_LOG.md count=1
776:- [2026-11-09T19:18:30Z] WHO: praxis-master | WHAT: **MANIFEST row in; temp index for audit.** ...
== c7-probe-fresh-manifest DISPATCH_LOG.md count=1
2270:- [2026-11-09T19:17:30Z] WHO: praxis-master | WHAT: dispatch praxis-manager, unit `2026-11-09-c7-probe-fresh-manifest` (append ONE MANIFEST row for the fresh probe report; no other edit) ...
== scrub-forward-c1 DECISION_LOG.md count=1
793:- [2026-11-10T09:36:00Z] WHO: praxis-master | WHAT: **SCRUB-FORWARD Correction 1 returned (corr aa7c0f4d7096fd734, 48 tool uses, ~18 min), `Correction 1 Result: PASS`; ...
== scrub-forward-c1 DISPATCH_LOG.md count=0
== hermes-replies-grading DECISION_LOG.md count=0
== hermes-replies-grading DISPATCH_LOG.md count=0
```
Park rows for diq (from `grep -n Praxis_build-diq DECISION_LOG.md`):
```
741:- [2026-11-08T17:25:00Z] WHO: praxis-master | WHAT: **RE-AUDIT (U7, `commit-idx-u7`, 8 paths, hash `ab154c4c…431f` reproduced) — FAIL 2. ABSOLUTE PARK RULE FIRED ...
751:- [2026-11-09T06:37:00Z] WHO: praxis-master | WHAT: **U7 (`Praxis_build-diq`) PARKED AGAIN: the single audit allowed by Amear's C1 returned FAIL** (auditor corr addfa3d5d9833f612, index `idx-u7`, ...
```

### E5. Key context windows (python -I extraction of the matched row, name-substituted)
```
== row 433 (2026-10-28T20:49:38Z): ... No AUDIT_LOG or DECISION_LOG row after 432 grades or delivers it. **What survives:** `docs/reports/2026-10-26-nightly-spec-request-review.md` (untracked, 20509 bytes), with re-verified evidence for all five problems as of 10-26 07:33–07:58 EDT, the supersession finding, and the D1–D10 defect labels. **What does not:** the note text (11954 bytes), ...
== row 440 (2026-10-28T21:36:30Z): **DISPATCH: deliver the audited review note to the exchange folder.** A byte-identical copy of `docs/reports/2026-10-28-nightly-checks-plan-review-note.md` goes to `hermes-ops-exchange/from-code/2026-10-28-praxis-nightly-checks-plan-review.md` ... STATE: dispatched — delivery
== row 441 (2026-10-30T21:36:00Z): ... the note was already DELIVERED on 2026-10-28 — `hermes-ops-exchange/from-code/2026-10-28-praxis-nightly-checks-plan-review.md` exists ... and `docs/reports/2026-10-28-review-note-delivery.md:104` grades that delivery `Result: PASS`. Whether the Hermes side has read it is NOT KNOWN. **NEEDS AMEAR: withdraw the copy from `from-code/`, or leave it.** Not acted on (S8)
== row 438 (2026-10-28T21:33:00Z): **AUDIT PASS: F4 "[rep]" reply filing.** The grade is appended at `docs/reports/2026-10-28-f4-[rep]-reply-filing.md:393-465` ... Minors: ... (3) some manager-report statements are unpasted (the worker-isolation claim at `:48`, summaries at `:347-349`, V1/V6 commands not shown) ...
== row 632 (2026-10-31T17:05:39Z): **VOICE HANDOFF WRITTEN at Amear's request (...): `docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md`.** Written by the master directly (reports are inside its write permission; ...)
== row 616 (2026-11-01T21:58:19Z): ... Commit composition: pathspec — the two unit reports, the voice-handoff-3 file ..., MANIFEST.md, DECISION_LOG.md, DISPATCH_LOG.md. Excluded: `2026-11-01-csv-analyses-fix-manager-record.md` (gate artefact), root `F`, the old staged set. ...
== row 622 (2026-11-01T14:12:50Z): ... **Process defect, master's:** the correction brief banned any new report file, which collides with the manager stop gate ...; the manager wrote `docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md` to pass it and said so. File kept on disk (append-only), excluded from the commit and MANIFEST. Future correction briefs must allow a manager record. ...
== row 776 (2026-11-09T19:18:30Z): ... **Decided by master under D1:** the MANIFEST unit's own report `docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md` stays out of this commit and untracked (it has no MANIFEST row; it goes to housekeeping D9). DISPATCH_LOG stays out (bead `trn`). ...
== row 777 (2026-11-09T19:20:30Z): **C7 PROBE LANDED: `02d53c6` on `main` (3 files / 80+), PUSHED, `0 0`.** Audit PASS on `/tmp/idx-c7fresh` (auditor corr ae807da947c4ebafc, ...)
== row 794 (2026-11-10T09:41:00Z): **SCRUB-FORWARD LANDED: `16c7bfe` on `main` (8 files / 970+ / 3−), PUSHED, `0 0`.** Audit PASS on `/tmp/idx-scrub` (...). MINOR, accepted: (1) report :430 points to the c1-adversarial worker report, which stays out and untracked; ...
== row 823 (2026-11-11T16:00:00Z): ... **(2) Unit 2 = grade and file the four Hermes VM replies** (`vm/replies/20261110T214542Z-STATUS.md` STARTED, `20261110T214834Z-self-report.md`, `20261110T215014Z-STATUS.md` FINISHED, `20261110T224920Z-2b-skill-job.md`; all untracked), decided by master under D1, HANDOFF top card step 3: one praxis-manager writes a grading report against handoff steps 1–2 and CODE- reply terms T1–T7, plus MANIFEST rows; then praxis-auditor. Master noticed (OBSERVED `ls -la`, not yet analysed): the 2b reply's UTC field 22:49:20Z is one hour aft[er ...]
== row 824 (2026-11-11T17:25:07Z): **Session-start drift: the 14:47Z timer run ended mid-unit with no close.** ... Unit 2 (Hermes replies grading) manager corr=a12c74b796f026559 (15:58:58Z) and worker corr=ac2903ecacd0faf9a (16:58:37Z) have no close row; manager report on disk reads `Result: (pending)` (:75); HANDOFF top card not updated by that run. ...
== row 825 (2026-11-11T17:32:05Z): ... The 16:00Z Hermes-replies grading unit stays open, not in this brief. ...
== row 834 (2026-11-11T21:06:30Z): ... Unit 2 = resume the 16:00Z Hermes-replies grading unit as a fresh manager with a NEW report path (the old manager report reads `(pending)` and is not overwritten). ...
```
DISPATCH_LOG spawn rows for the grading unit (no close row for either corr):
```
$ grep -n -- a12c74b796f026559 DISPATCH_LOG.md DECISION_LOG.md | cut -c1-260   (and ac2903ecacd0faf9a)
DISPATCH_LOG.md:2474:- [2026-11-11T15:58:58Z] WHO: praxis-manager | WHAT: subagent spawned | ... WHERE: session 85a803f corr=a12c74b796f026559 | ... STATE: dispatched
DISPATCH_LOG.md:2487:- [2026-11-11T16:58:37Z] WHO: praxis-worker | WHAT: subagent spawned | ... WHERE: session 85a803f corr=ac2903ecacd0faf9a | ... STATE: dispatched
DECISION_LOG.md:824: (the drift row above) — for both corrs
```
No later resume report exists:
```
$ ls docs/reports | grep -iE 'repl(y|ies)-grad|vm-repl|hermes-repl'
2026-11-11-hermes-replies-grading-manager.md
2026-11-11-hermes-replies-grading-worker1.md
2026-11-11-hermes-replies-grading-worker2.md
2026-11-11-hermes-replies-grading-worker4.md
2026-11-11-hermes-replies-grading-worker6.md
```
Later DECISION_LOG rows (835 onward) mentioning `vm/replies` only report the newest STATUS (rows 850, 861, 867, 892: "newest `vm/replies/` STATUS `20261111T172940Z`"); none closes or resumes the grading unit (python scan for `Hermes.replies|replies grading|hermes-replies|vm/replies|a12c74b796f026559` over rows 835+ returned only those four rows).

### E6. AUDIT_LOG (read-only greps)
```
$ grep -n -E 'nightly-spec-request-review|reply-worker|reply-adversarial|review-note-delivery|voice-handoff-future-row|csv-analyses-fix|three-strategy-results-s2-fix|wf-spec-amendment|c7-probe-fresh-manifest|scrub-forward-c1|hermes-replies-grading|20261110T21|20261110T22' AUDIT_LOG.md | cut -c1-220
(no output)
$ grep -n -E 'csv-analyses|three-strategy|c7-probe|scrub-forward|hermes-replies|nightly-checks|nightly-spec|review-note|voice-handoff|wf-spec|reply-filing|vm/replies' AUDIT_LOG.md | cut -c1-200 | tail -20
(no output)
$ wc -l AUDIT_LOG.md
     154 AUDIT_LOG.md
```
AUDIT_LOG rows are keyed by index path, not by report path. In-window rows (stamp, verdict, index), trimmed:
```
$ grep -n -E '^2026-1(0-2[6-9]|0-3|1-0|1-1[01])' AUDIT_LOG.md | cut -d' ' -f1,4,5 | cut -c1-140
93..104: 2026-11-06T00:49:17Z .. 2026-11-07T00:39:48Z PASS index=<scratchpad 8eda06af...>
105..113: 2026-11-07T14:00:25Z .. 2026-11-07T22:13:40Z PASS index=<scratchpad d2d7d756...>
114:2026-11-08T15:19:40Z PASS index=<scratchpad dac8a676...>
115:2026-11-08T15:51:07Z PASS index=<scratchpad dac8a676...>
116:2026-11-08T16:10:34Z PASS index=<scratchpad dac8a676...>
117:2026-11-09T05:53:02Z PASS index=<scratchpad 43b18d1e...>
118:2026-11-09T06:11:54Z PASS index=<scratchpad 43b18d1e...>
119:2026-11-09T10:02:24Z PASS index=/private/tmp/idx-r6-step1b
120:2026-11-09T13:51:44Z PASS index=/private/tmp/idx-d11b
121:2026-11-09T14:24:34Z PASS index=/private/tmp/idx-rubric2
122:2026-11-09T18:35:39Z PASS index=/private/tmp/idx-vmh2
123:2026-11-09T18:49:19Z PASS index=/private/tmp/idx-c7
124:2026-11-09T19:19:58Z PASS index=/private/tmp/idx-c7fresh
125:2026-11-10T06:09:28Z PASS index=/private/tmp/idx-c2
126:2026-11-10T07:17:22Z PASS index=/private/tmp/idx-d9
127:2026-11-10T07:34:15Z PASS index=/private/tmp/idx-hk2a
128:2026-11-10T09:38:54Z PASS index=/private/tmp/idx-scrub
129:2026-11-10T10:23:28Z PASS index=/private/tmp/idx-hk2b
130:2026-11-10T13:32:36Z PASS index=/private/tmp/idx-f1f2
131:2026-11-10T13:46:23Z PASS index=/private/tmp/idx-f1c
132:2026-11-10T18:27:31Z PASS index=/private/tmp/idx-f4c1
133:2026-11-11T15:57:13Z PASS index=/private/tmp/idx-hermes2
134:2026-11-11T18:17:50Z PASS index=/private/tmp/idx-mffu1
135:2026-11-11T21:06:21Z PASS index=/private/tmp/idx-flush1
```
(The lines 93-118 rows are paraphrased into ranges: the index paths were cut at 140 chars in the output and all sit in session scratchpads.) There are no AUDIT_LOG rows before line 93 inside this window, so the 2026-10-26..2026-11-05 units have no minted token at all. idx-c7fresh (:124), idx-scrub (:128), idx-hermes2 (:133) map, by DL rows 777, 794 and 822, to commits 02d53c6, 16c7bfe and 85a803f. None of those commits holds any file in my scope (E7). I did not read the index files (preamble forbids GIT_INDEX_FILE use).

### E7. Commit status: filed siblings and commits
```
$ for s in <unit prefixes>; do echo "-- $s"; git ls-files docs/reports | grep -- "$s"; done | sed "s/$N/[rep]/Ig"
-- 2026-10-26-nightly
-- 2026-10-28-f4
docs/reports/2026-10-28-f4-[rep]-reply-filing.md
-- 2026-10-28-review
-- 2026-10-31-voice
docs/reports/2026-10-31-voice-handoff-backtest-session.md
docs/reports/2026-10-31-voice-session-notes-2.md
docs/reports/2026-10-31-voice-session-notes.md
-- 2026-11-01-csv-analyses
docs/reports/2026-11-01-csv-analyses-manager.md
docs/reports/2026-11-01-csv-analyses.md
-- 2026-11-01-three-strategy
docs/reports/2026-11-01-three-strategy-results-manager.md
docs/reports/2026-11-01-three-strategy-results.md
-- 2026-11-08-wf-spec
-- 2026-11-09-c7-probe
docs/reports/2026-11-09-c7-probe-control-manager.md
docs/reports/2026-11-09-c7-probe-fresh-manager.md
docs/reports/2026-11-09-c7-probe-test-manager.md
-- 2026-11-09-wf-spec
-- 2026-11-10-scrub-forward
docs/reports/2026-11-10-scrub-forward-adversarial.md
docs/reports/2026-11-10-scrub-forward-manager.md
docs/reports/2026-11-10-scrub-forward-worker1.md
-- 2026-11-11-hermes
(none)
$ git show --name-only --format= <c> | grep docs/reports
== 02d53c6 : docs/reports/2026-11-09-c7-probe-fresh-manager.md
== 16c7bfe : 2026-11-07-rulings-filing-manager.md, 2026-11-09-d11-sweep-manager.md, 2026-11-10-scrub-forward-adversarial.md, 2026-11-10-scrub-forward-manager.md, 2026-11-10-scrub-forward-worker1.md
== f747889 : 2026-11-01-csv-analyses-manager.md, 2026-11-01-csv-analyses.md, 2026-11-01-voice-handoff-results-and-next-build.md
== 8ca9861 : 2026-10-31-voice-session-notes-2.md, 2026-11-01-three-strategy-results-manager.md, 2026-11-01-three-strategy-results.md, 2026-11-01-voice-handoff-commission-fix.md
$ git show --stat 18d94a5 | sed "s/$N/[rep]/Ig"   (2026-11-10 02:17:43 -0500, "D9 housekeeping")
 ... docs/reports/2026-10-28-f4-[rep]-reply-filing.md | 394 ++++
 .../2026-10-28-nightly-checks-plan-review-note.md  |  186 ++
 ...026-10-28-nightly-checks-plan-review-rebuild.md | 1335 ++++++++++++++
 docs/reports/2026-11-10-d9-housekeeping-manager.md | 1058 +++++++++++
 (14 files, 6824+ / 2-; none of the 10 F4 worker/adversarial files, no review-note-delivery, no 2026-10-26 review)
$ git log --format='%h %s' -- docs/reports/2026-10-31-voice-handoff-backtest-session.md
a91a636 docs: voice-session handoff brief and notes, 2026-10-31 (MANIFEST rows landed with the a9d merge)
$ git log --format='%h %ad %s' -- vm/replies
ee54344 2026-11-11T21:24 docs: file Amear rulings V1-V7 as D-2026-11-11-A ...
85a803f 2026-11-11T10:57 docs: Hermes over SSH as the VM agent (D-2026-11-10-C; ...)
e9f668c 2026-11-06T18:01 vm: VM handoff for tests 2b/2a and the cli-nt-bridge install ...
```
D9 scope, from the D9 manager report :7: `"D9  The 12 old staged paths are landed properly (audited) rather than unstaged. ..."`. D9 covered staged paths only. The c7-probe-fresh-manifest report was routed "to housekeeping D9" (DL :776), but it is untracked, so it was not among the staged paths D9 landed.

### E8. Beads
```
$ bd list --all | grep -iE 'hermes|repl|c2w|diq' | cut -c1-160
○ Praxis_build-diq ● P1 PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired
○ Praxis_build-c2w ● P2 De-identification sweep: MFFU rep first name in committed MANIFEST rows and untracked reports
○ Praxis_build-rpy ● P3 mffu reply PNG held out of D9 (third-party full-name address); still staged in real index
(+ 10i, qtk, aac, unrelated)
$ bd show Praxis_build-c2w | head   (OPEN, P2, created 2026-11-13)
  ... Task: decide under D1 how to treat the committed rows (amendment row vs leave) and rename
  or redact the uncommitted files before they are committed.
```
No bead was found for the hermes-replies-grading unit (the grep above for `hermes|repl` returned none for it).

### E9. VM reply timestamps vs mtimes (date +%z = -0500)
```
214542Z-STATUS       mtime 16:46:36 local = 21:46:36Z   name 21:45:42Z
214834Z-self-report  mtime 16:48:54 local = 21:48:54Z   name/UTC 21:48:34Z
224920Z-2b-skill-job mtime 16:49:56 local = 21:49:56Z   name/UTC 22:49:20Z  <-- name is 59 min AFTER the mtime
215014Z-STATUS       mtime 16:50:17 local = 21:50:17Z   name 21:50:14Z (FINISHED written after the 2b file)
```
This matches the master's observation in DL row 823 ("the 2b reply's UTC field 22:49:20Z is one hour aft[er]..."), which that row marked "not yet analysed". I did not analyse the cause. The grading manager report puts the 2b file in its table, but its Result is pending.

## Classification by group

### G1. 2026-10-26 nightly spec-request review (1 file)
- `docs/reports/2026-10-26-nightly-spec-request-review.md`. Owner: the 2026-10-26 review-note draft unit (master dispatch under Amear's DL :432 approval, 2026-10-26T11:33:00Z). Ledger: DL :433 (2026-10-28T20:49:38Z), which calls it "What survives" (untracked) of a note LOST before audit. Superseded by the 10-28 rebuild, which was audited (DL :439, RE-AUDIT PASS) and committed in 18d94a5. Audit: none (E6 empty; DL :433 says "No AUDIT_LOG or DECISION_LOG row after 432 grades or delivers it"). No Result line (E2). Name count 0. No bead found.
- **Class: CLEAR-BUT-NEEDS-AUDIT.** One owner, a plainly evidential report, not parked, no audit.
- Question for Amear (S8): should a superseded, never-graded draft-unit report be filed as history, or left untracked?

### G2. 2026-10-28 F4 reply filing: 10 worker/adversarial reports
- `docs/reports/2026-10-28-f4-[rep]-reply-{adversarial-addendum, adversarial-confirm, adversarial-final, adversarial-recheck, adversarial-transcript, worker1, worker3, worker5-fix, worker7-fix, worker9-fix}.md`. Owner: unit 2026-10-28 F4 reply filing (Amear DL :435, 2026-10-28T20:54:29Z, verified by `sed -n 435p`; audit PASS DL :438, 2026-10-28T21:33:00Z, which grades the filing report only, at `:393-465`). Filed sibling: the filing report only, landed by 18d94a5 (D9). None of these 10 is in 18d94a5 (E7). AUDIT_LOG: none (E6, plus no AUDIT_LOG row before :93 in the window). Results: addendum FAIL, final FAIL, recheck FAIL, transcript "DISCREPANCIES FOUND (2)", confirm PASS, worker1/3/5/7/9 PASS (E2). Name counts 2-19 each (E1). Bead c2w (OPEN) covers name-bearing untracked reports.
- **Class: UNCLEAR (all 10).** Every one holds the rep name (bead c2w), and three carry adversarial FAILs.

### G3. 2026-10-28 review-note delivery (1 file)
- `docs/reports/2026-10-28-review-note-delivery.md`. Owner: the delivery dispatch DL :440 (2026-10-28T21:36:30Z, praxis-manager → praxis-worker copy). Its self-grade is `104:Result: PASS`, cited by DL :441. Siblings filed: the review note and rebuild report (18d94a5); this file was not. AUDIT_LOG: none (E6). mtime 17:35:59 local = 22:35:59Z. Name count 0.
- **Class: CLEAR-BUT-NEEDS-AUDIT.** One owner, an evidence report, a self-graded PASS but no auditor grade found.
- Open Amear question, already in DL :441: "withdraw the copy from `from-code/`, or leave it". No later amear row on it was found (the grep for `review-note-delivery` hits only :441).

### G4. 2026-10-31 voice handoff (1 file)
- `docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md`. Owner: praxis-master, written directly at Amear's request (DL :632, 2026-10-31T17:05:39Z). Siblings from the same day are filed (a91a636); this one is not. No Result line. AUDIT_LOG: none. Name count 0.
- **Class: CLEAR-BUT-NEEDS-AUDIT.** One owner (master), a handoff document, never graded.

### G5. 2026-11-01 correction manager records (2 files)
- `docs/reports/2026-11-01-csv-analyses-fix-manager-record.md`. Owner: unit 2026-11-01-csv-analyses (correction manager). DL :616 / DPL :1377 (2026-11-01T21:58:19Z) record that the unit passed audit and was committed in f747889, and **explicitly excluded** this file: "Excluded: `2026-11-01-csv-analyses-fix-manager-record.md` (gate artefact)". Result: PASS at :33 and :52 (self). Name count 0.
- `docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md`. Owner: unit 2026-11-01-three-strategy-results. DL :622 / DPL :1347 (2026-11-01T14:12:50Z) record the re-audit PASS and commit 8ca9861, and that the file was "kept on disk (append-only), excluded from the commit and MANIFEST". Its own Result is `BLOCKED ... pending the auditor's re-grade` (:64). The re-grade (DL :622) was a PASS for the unit's report. Name count 0.
- **Class: CLEAR-BUT-NEEDS-AUDIT (both).** One owner each, not parked. The unit audit PASS covered the unit deliverables, not these records. The master decided to exclude them (DL :616, :622). Whether to file them now reverses that decision, so the master or Amear should rule on it.

### G6. 2026-11-08 / 11-09 wf-spec-amendment (5 files, bead diq)
- `docs/reports/2026-11-08-wf-spec-amendment-manager.md`, `-correction-1-manager.md`, `-correction-2-manager.md`, `-correction-3-manager.md`, `docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md`. Owner: U7 2026-11-08-wf-spec-amendment and its 11-09 resume (DPL :2032-2035, :2155; DL :737-739). DL :741 (2026-11-08T17:25:00Z): FAIL 2, absolute park rule fired. DL :751 (2026-11-09T06:37:00Z): "PARKED AGAIN: the single audit allowed by Amear's C1 returned FAIL". Bead diq is OPEN and PARKED (E8). Self-Results: PASS at level WRITTEN (manager and corrections 1-3) and PASS (resume) (E2). Nothing filed (E7). Name count 0.
- **Class: UNCLEAR (all 5).** The unit is parked after two audit FAILs, and per the beads only a human resumes it.

### G7. 2026-11-09 c7-probe-fresh-manifest (1 file)
- `docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md`. Owner: unit 2026-11-09-c7-probe-fresh-manifest (DPL :2270, 2026-11-09T19:17:30Z). DL :776: "stays out of this commit and untracked (it has no MANIFEST row; it goes to housekeeping D9)". The audit PASS on idx-c7fresh (AUDIT_LOG :124, 19:19:58Z) covered commit 02d53c6. That commit holds only `2026-11-09-c7-probe-fresh-manager.md` among reports (E7), not this file. D9 landed staged paths only, and this file is untracked, so it was never picked up. Result: `91:Result: PASS` (self). mtime 14:17:51 local = 19:17:51Z. Name count 0.
- **Class: CLEAR-BUT-NEEDS-AUDIT.** The PASS was for the MANIFEST-row commit, not for filing this report.

### G8. 2026-11-10 scrub-forward c1 adversarial (1 file)
- `docs/reports/2026-11-10-scrub-forward-c1-adversarial.md`. Owner: scrub-forward Correction 1 (DL :793, 2026-11-10T09:36:00Z). The unit landed as 16c7bfe with audit PASS on idx-scrub (AUDIT_LOG :128). DL :794 MINOR (1): "report :430 points to the c1-adversarial worker report, which stays out and untracked". Result: `98:Result: FAIL`. Name count **1**.
- **Class: UNCLEAR.** It holds the rep name once (c2w), and its own Result is FAIL.

### G9. 2026-11-11 hermes-replies-grading (5 files)
- `docs/reports/2026-11-11-hermes-replies-grading-manager.md` (Result `(pending)` :75, name 0), `-worker1.md` (PASS :1114, name **14**), `-worker2.md` (FAIL :320, name 0), `-worker4.md` (FAIL :300, name **2**), `-worker6.md` (FAIL :287, name 0). Owner: Unit 2, opened by the master under D1 at DL :823 (2026-11-11T16:00:00Z). The manager (corr a12c74b796f026559, DPL :2474) and a worker (corr ac2903ecacd0faf9a, DPL :2487) have no close row. DL :824 (17:25:07Z): "the 14:47Z timer run ended mid-unit with no close". DL :825: "stays open". DL :834 (21:06:30Z) planned a fresh resume "with a NEW report path". No resume report exists (E5 ls), and no later row closes it. No siblings filed, no bead found, no AUDIT_LOG entry (E6).
- **Why they were left out:** the unit never finished. It was not graded or closed, so nothing went to a commit. This is not an exclusion by decision.
- **Class: UNCLEAR (all 5).** The unit is open and unclosed, the manager verdict is pending, three workers FAIL, and worker1 and worker4 hold the rep name (c2w).

### G10. vm/replies, four Hermes files of 2026-11-10
- `vm/replies/20261110T214542Z-STATUS.md` (STARTED), `20261110T214834Z-self-report.md` (RESULT: DONE, step 1), `20261110T215014Z-STATUS.md` (FINISHED), `20261110T224920Z-2b-skill-job.md` (RESULT: DONE, step 2). Owner/author: Hermes Agent (header WRITTEN-BY, E2). DL :818 (2026-11-10T21:47:00Z) records STARTED being written, and that the master committed nothing that session. Siblings filed: the outgoing `20261110T211738Z-CODE-vm-agent-hermes.md` (85a803f) and the 2026-11-11 replies (ee54344). Name count 0 each.
- **Why not filed:** they were the subject of the G9 grading unit (DL :823: "Unit 2 = grade and file the four Hermes VM replies ... all untracked"). That unit never closed, so the filing step never ran.
- **Class: CLEAR-BUT-NEEDS-AUDIT (all 4).** The single author is Hermes, the files are raw evidence, no audit exists, and nothing is parked. Caveat on `20261110T224920Z-2b-skill-job.md`: its name/UTC stamp is 59 minutes after its file mtime (E9; also DL :823 "not yet analysed"). Filing it as is would carry a stamp that is unexplained. I left the class unchanged because the preamble's UNCLEAR criteria do not cover this, but the manager may weigh it.

### Summary table
| Class | Count | Items |
|---|---|---|
| CLEAR-FILE | 0 | none. No item has an audit PASS covering its exact content. |
| CLEAR-BUT-NEEDS-AUDIT | 10 | G1 (1), G3 (1), G4 (1), G5 (2), G7 (1), G10 (4) |
| UNCLEAR | 21 | G2 (10, name), G6 (5, diq parked), G8 (1, name + FAIL), G9 (5, open unit; 2 name) |
Total 31.

### Questions for Amear (S8, not decided here)
1. G1: should a superseded, never-graded 10-26 draft report be filed, or left untracked?
2. G3: the open DL :441 item, "withdraw the copy from `from-code/`, or leave it".
3. G5: reverse the master's 2026-11-01 exclusions of the two manager records, or keep them out?
4. G9/G10: resume the Hermes-replies grading unit (planned at DL :834, never run), and decide what to do about the 2b reply's stamp anomaly.

### Second findings (reported, not fixed)
- The committed `docs/reports/2026-10-28-f4-[rep]-reply-filing.md` landed as 394 lines in 18d94a5, while DL :438 places its audit grade at `:393-465`. The working copy is ` M` in git status. This file is out of my scope. I did not check whether the committed copy holds the grade.
- mint-guard blocked three read-only Bash commands of mine on AUDIT_LOG.md: one using `cd ...;` and `sed -n` with `$N`, one using `echo` and `grep -c`, and one using `awk '{print ...}'`. Plain `grep | cut` and `wc`/`tail` passed. The Grep tool is not available in this session, despite the brief.

## Files staged
None (read-only unit). Only this report was written.

## Name check of this report
```
$ grep -ci "$N" docs/reports/2026-11-14-dirty-tree-sort-worker4.md
0
```
(The check ran before this section was added. The section itself contains no name.)

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
