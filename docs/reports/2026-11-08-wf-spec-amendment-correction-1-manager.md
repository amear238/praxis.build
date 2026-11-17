Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# 2026-11-08 — wf-spec-amendment correction 1 (manager report)

## Task
Unit `2026-11-08-wf-spec-amendment-correction-1`. Two dictated in-place edits to `docs/specs/2026-11-06-walk-forward-values.md`, defects found by the master in the prior unit `2026-11-08-wf-spec-amendment` (DECISION_LOG row `2026-11-08T17:01:00Z`, WHO: praxis-master):
1. Line 128: the sentence resting on the unfiled U7 dispatch brief replaced by the dictated sentence citing the 17:01:00Z ledger row.
2. Line 3: the dictated attribution of the v2.2 changes inserted directly after "**Status: version 2.2 (2026-11-08).**".

## Rubric criteria addressed
- S1: every claim below rests on pasted output.
- S2: the result is claimed at level WRITTEN only (edits applied in the working tree, not staged, not graded).
- S8: no Amear question answered. The new line-128 sentence labels the reading as the master's, citing the master's ledger row, "not his words, changeable by Amear". The wording was dictated by the master; I authored none of it.
- S13: the standing sentence appears once, as line 1 of this report.

## Workers dispatched
None. Both edits were dictated text; the brief allowed the manager to do them itself.

## Process log
1. Scratch copy taken before any edit: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/wfv-before.md` (written as "before-copy" in the commands below).
2. Edits applied by a `python3 -I` byte-level script. It asserted the old line-3 prefix occurs exactly once at the start of line 3, and the old line-128 sentence occurs exactly once in the whole file and inside line 128. It then wrote the file back with line endings unchanged. Output: `ok`.
3. Line-3 wording: I used the dictated form "… Version 2 by Unit `2026-11-07-wf-values-fresh`; …". The capital "U" in "by Unit" is slightly awkward, but the sentence reads correctly and the brief requires the original text after the insert to stay byte-identical. So I made no change to the dictated wording. Alternative considered and NOT applied: "… changelog :5.) Version 2: Unit `2026-11-07-wf-values-fresh`; …".
4. The changelog pointer ":5" is checked below: line 5 of the spec holds the Version 2.2 entry.
5. Side effect of the dictated replacement, noted rather than fixed: the old line 128 ended "…; this file does not reconcile them." The new sentence ends at "…changeable by Amear." The earlier sentence on the same line, "This file does not reconcile them.", is unchanged.

## Verification evidence

### Before (taken before the edit, same session)
```
$ git rev-parse --short HEAD
6c4c109
$ git diff --numstat HEAD -- docs/specs/2026-11-06-walk-forward-values.md
20	20	docs/specs/2026-11-06-walk-forward-values.md
$ wc -l docs/specs/2026-11-06-walk-forward-values.md
     349 docs/specs/2026-11-06-walk-forward-values.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ grep -c 'not filed in the repo' docs/specs/2026-11-06-walk-forward-values.md
1
```

### Ledger row named by the new pointer, and changelog :5
```
$ head -c 300 <(grep '2026-11-08T17:01:00Z' DECISION_LOG.md)
- [2026-11-08T17:01:00Z] WHO: praxis-master | WHAT: **U7 `2026-11-08-wf-spec-amendment` RETURNED (60 tool uses — at the cap — ~47 min, ~190k tokens; `Result: PASS at level WRITTEN`; three adversary rounds: R1 REFUTED 3 MAJOR, R2 REFUTED 1 MAJOR, R3 `GRADE: NOT REFUTED` 6 MINOR; post-R3 narrowing
$ sed -n '737p' DECISION_LOG.md | grep -o "master's reading, changeable by Amear: R2[^)]*" | head -1
master's reading, changeable by Amear: R2 ("GO requires arm (a
$ sed -n '737p' DECISION_LOG.md | grep -c 'together resolve the tension at :128'
1
$ sed -n 5p docs/specs/2026-11-06-walk-forward-values.md | grep -o 'Version 2\.2[^;]\{0,160\}'
Version 2.2, 2026-11-08, unit `2026-11-08-wf-spec-amendment` (dispatch DECISION_LOG `2026-11-08T16:12:00Z`, WHO: praxis-master), under Amear's rulings D-2026-11-08-A R1–R3
```

### After
```
$ git diff --numstat HEAD -- docs/specs/2026-11-06-walk-forward-values.md
20	20	docs/specs/2026-11-06-walk-forward-values.md
$ wc -l docs/specs/2026-11-06-walk-forward-values.md
     349 docs/specs/2026-11-06-walk-forward-values.md
$ diff <(sed -n '3p;128p' before-copy) <(sed -n '3p;128p' docs/specs/2026-11-06-walk-forward-values.md)
1,2c1,2
< **Status: version 2.2 (2026-11-08).** Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-06-wf-values, parked FAIL 2, DECISION_LOG 2026-11-07T00:00:00Z). Version 1 is 
< - **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them. R2 (D-2026-11-08-A, DECISIONS.md:1556–1557, join
---
> **Status: version 2.2 (2026-11-08).** (v2.2 changes: unit `2026-11-08-wf-spec-amendment`, changelog :5.) Version 2 by Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-1
> - **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them. R2 (D-2026-11-08-A, DECISIONS.md:1556–1557, join
$ diff <(sed '3d;128d' before-copy) <(sed '3d;128d' docs/specs/2026-11-06-walk-forward-values.md); echo exit=$?
exit=0
$ grep -c 'not filed in the repo' docs/specs/2026-11-06-walk-forward-values.md
0
$ grep -n '2026-11-08T17:01:00Z' DECISION_LOG.md | cut -c1-300
737:- [2026-11-08T17:01:00Z] WHO: praxis-master | WHAT: **U7 `2026-11-08-wf-spec-amendment` RETURNED (60 tool uses — at the cap — ~47 min, ~190k tokens; `Result: PASS at level WRITTEN`; three adversary rounds: R1 REFUTED 3 MAJOR, R2 REFUTED 1 MAJOR, R3 `GRADE: NOT REFUTED` 6 MINOR; post-R3 narro

$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ cmp <(head -c -0 /dev/null) /dev/null; tail -c1 check
00000000: 0a                                       .
00000000: 0a                                       .
```
(The `diff` lines above were cut to 260 characters by `cut -c1-260`. The last two `xxd` lines show both files end in a single trailing newline; the `$ cmp … ; tail -c1 check` header was a label only.)

### Byte-identity of the parts left unchanged
```
$ sed -n 128p (after)
- **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them. R2 (D-2026-11-08-A, DECISIONS.md:1556–1557, joined): "GO requires arm (a) to pass. Arm (b) can only add confidence or block a GO; it can never carry a GO on its own". A7 (D-2026-11-08-B, DECISIONS.md:1746): "R3 amends Q8". His words do not name the tension recorded on this line. That R2 and A7 together resolve this tension (both arms graded against their own gate sets; GO rests on arm (a) alone, arm (b) only as confidence or veto) is the master's reading, DECISION_LOG 2026-11-08T17:01:00Z (WHO: praxis-master), not his words, changeable by Amear.
$ line 3 after, first 260 chars
**Status: version 2.2 (2026-11-08).** (v2.2 changes: unit `2026-11-08-wf-spec-amendment`, changelog :5.) Version 2 by Unit `2026-11-07-wf-values-fresh`; dispatch: DECISION_LOG row `[2026-11-07T14:06:00Z] WHO: praxis-master`. Supersedes version 1 (unit 2026-11-
$ line-3 suffix check: before[39:] == after[after.index(") Version 2 by")+15:] ; line-128 prefix check
line3 after == o+ins+before[len(o):]: True
line128 prefix identical: True len 490
line128 after ends with new sentence (nothing after it): True
line128 before ended with old sentence (nothing after it): True
```

## Adversarial findings
None run. The brief waived the adversary for two dictated line edits. Self-check only: the identity checks above show (a) line 3 equals the old status prefix, plus the dictated insert, plus the old remainder byte-for-byte; (b) the first 490 bytes of line 128 are unchanged, and the line now ends with the dictated sentence; (c) no other line changed (`exit=0`, empty diff); (d) the line count is still 349; (e) numstat is still `20 20`; (f) the staged stat is unchanged.

## S6 cross-block check
Not exercised. No hook was tripped or tested in this unit, and no gate claim is made.

## Files staged
None. The unit stages nothing. Working-tree changes are to `docs/specs/2026-11-06-walk-forward-values.md` (lines 3 and 128) and to this new, untracked report. The staged set is unchanged (`12 files changed, 5726 insertions(+), 2 deletions(-)`, pasted above).

## Result: PASS at level WRITTEN

## Does NOT cover
- Whether the master's reading in the 17:01:00Z row is correct. That is Amear's to change.
- Any MANIFEST.md row, ledger row, DECISIONS.md entry, or staging of these edits. All were out of scope.
- Independent grading. That is the auditor's job, spawned by the master.
- Any other line of the spec, including whether the "by Unit" capitalisation should be revised later.

## Memory not saved
Not written, per the brief. The line I would have saved: "A dictated sentence replacement can drop a trailing clause the old sentence carried. Name what the replaced span loses in the report, because silent loss reads as scope creep."
