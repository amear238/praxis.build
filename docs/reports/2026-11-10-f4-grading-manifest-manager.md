# 2026-11-10 f4-grading-manifest — manager report

## Task
Unit `2026-11-10-f4-grading-manifest`. Append exactly five rows to the end of the working-copy `MANIFEST.md`, one for each new report of unit `2026-11-10-f4-grading` (manager, worker1 through worker4). Use the column shape and block number (3) of the f1-closeout rows. Touch no other line or file except this report. No git index operations. Baseline HEAD `d30ab4d`.

## Rubric criteria addressed
- S1: every claim below rests on pasted command output.
- S2: rows give each report's own Result line as the report states it, and each says "ungraded at time of row". The manager-report row says it does not grade F4 and F4 stays FROZEN, which matches the report head (":5 This report compares. It does not grade F4 ... F4 stays FROZEN") and rubric F4 (specs/SPEC_RUBRIC.md :48, still under FROZEN).
- S8: no F4 state is recommended. F4's owner is Amear.
- S13: this report carries the S13 sentence once, as its last line.
- Project rule "Update MANIFEST.md when creating or modifying files" (CLAUDE.md), applied to the five reports.

## Workers dispatched
None. The master's brief allowed the manager to do this small unit directly. It is a pure doc edit: one heredoc append.

## Process log
- 17:2xZ: confirmed HEAD `d30ab4d`. Before the edit, MANIFEST numstat was `8 0` and the index held one path. Read the MANIFEST tail (f1-closeout rows: `| path | Report | 3 | 2026-11-10 | ... |`).
- Read the head, the Result line and the tail of each of the five reports:
  - manager: comparison only, does not grade F4, F4 stays FROZEN, `Result: PASS` at :456.
  - worker1: `## Result (in progress)`, followed by a manager note: stopped at its 40-turn cap with only a skeleton, Result FAIL (no deliverables).
  - worker2: BUILD read-only extraction, `## Result: PASS`.
  - worker3: ADVERSARIAL, `FAIL — 3 BLOCKING (findings 1–3), 6 MINOR (findings 4–9)`.
  - worker4: ADVERSARIAL, `FAIL: one BLOCKING finding (1) and three MINOR findings (2, 3, 4)`.
- Appended five rows with one `cat >> MANIFEST.md <<'EOF'` heredoc. The file already ended in `\n` (checked with od), so nothing was merged into the last line.
- Ran the four required checks and three extra ones (field count, deleted-line count, `@` count).

## Verification evidence (command output)

`git diff -- MANIFEST.md | tail -n 8`
```
 | /DECISIONS.md | Log | 3 | 2026-11-10 | MODIFIED (unit 2026-11-10-f1-closeout; bead Praxis_build-1hv; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-10T13:36:00Z): entry D-2026-11-10-B (live-signal topology adopted as the working design; rubric F1) appended at lines 2046-2074 (heading :2047); lines 1-2045 unchanged |
 | /specs/SPEC_RUBRIC.md | Spec | 3 | 2026-11-10 | MODIFIED (unit 2026-11-10-f1-closeout; bead Praxis_build-1hv; master under D-2026-11-08-D D1 and A11, DECISION_LOG row 2026-11-10T13:36:00Z): F1 block moved from FROZEN to PASSED after O1, text unchanged, with a State line PASSED@b4c3291 and a filer's note above it; F2, F3, F4 untouched |
 | /docs/reports/2026-11-10-f1-closeout-manager.md | Report | 3 | 2026-11-10 | Manager report for unit 2026-11-10-f1-closeout (bead Praxis_build-1hv): D-2026-11-10-B filing, F1 rubric move, pasted verification evidence, adversarial findings, S6 cross-block check, file hashes |
+| /docs/reports/2026-11-10-f4-grading-manager.md | Report | 3 | 2026-11-10 | Manager report for unit 2026-11-10-f4-grading: compares MFFU's written words, quoted verbatim, against each element of the D-2026-11-10-B automation pattern with coverage labels only; it does not grade F4 and F4 stays FROZEN; report's own Result line PASS, ungraded at time of row |
+| /docs/reports/2026-11-10-f4-grading-worker1.md | Report | 3 | 2026-11-10 | BUILD (read-only extraction) worker 1 report for unit 2026-11-10-f4-grading: stopped at its turn cap with a skeleton only, manager note records Result FAIL (no deliverables) and that nothing in the manager report rests on it; ungraded at time of row |
+| /docs/reports/2026-11-10-f4-grading-worker2.md | Report | 3 | 2026-11-10 | BUILD (read-only extraction) worker 2 report for unit 2026-11-10-f4-grading: whether the outgoing MFFU inquiry text is recorded at HEAD and which HEAD documents say F4 is closed, answered from pasted HEAD output with de-identified blocks; report's own Result line PASS, ungraded at time of row |
+| /docs/reports/2026-11-10-f4-grading-worker3.md | Report | 3 | 2026-11-10 | ADVERSARIAL worker 3 report for unit 2026-11-10-f4-grading: attack on the manager draft for label strength, quote fidelity, factual claims, personal data and forbidden content; report's own Result line FAIL (3 blocking, 6 minor findings), ungraded at time of row |
+| /docs/reports/2026-11-10-f4-grading-worker4.md | Report | 3 | 2026-11-10 | ADVERSARIAL worker 4 report for unit 2026-11-10-f4-grading: scoped attack on the manager draft's element table rows, coverage paragraphs and inquiry section; report's own Result line FAIL (1 blocking, 3 minor findings), ungraded at time of row |
```

`tail -n 5 MANIFEST.md`
```
| /docs/reports/2026-11-10-f4-grading-manager.md | Report | 3 | 2026-11-10 | Manager report for unit 2026-11-10-f4-grading: compares MFFU's written words, quoted verbatim, against each element of the D-2026-11-10-B automation pattern with coverage labels only; it does not grade F4 and F4 stays FROZEN; report's own Result line PASS, ungraded at time of row |
| /docs/reports/2026-11-10-f4-grading-worker1.md | Report | 3 | 2026-11-10 | BUILD (read-only extraction) worker 1 report for unit 2026-11-10-f4-grading: stopped at its turn cap with a skeleton only, manager note records Result FAIL (no deliverables) and that nothing in the manager report rests on it; ungraded at time of row |
| /docs/reports/2026-11-10-f4-grading-worker2.md | Report | 3 | 2026-11-10 | BUILD (read-only extraction) worker 2 report for unit 2026-11-10-f4-grading: whether the outgoing MFFU inquiry text is recorded at HEAD and which HEAD documents say F4 is closed, answered from pasted HEAD output with de-identified blocks; report's own Result line PASS, ungraded at time of row |
| /docs/reports/2026-11-10-f4-grading-worker3.md | Report | 3 | 2026-11-10 | ADVERSARIAL worker 3 report for unit 2026-11-10-f4-grading: attack on the manager draft for label strength, quote fidelity, factual claims, personal data and forbidden content; report's own Result line FAIL (3 blocking, 6 minor findings), ungraded at time of row |
| /docs/reports/2026-11-10-f4-grading-worker4.md | Report | 3 | 2026-11-10 | ADVERSARIAL worker 4 report for unit 2026-11-10-f4-grading: scoped attack on the manager draft's element table rows, coverage paragraphs and inquiry section; report's own Result line FAIL (1 blocking, 3 minor findings), ungraded at time of row |
```

`git diff --numstat -- MANIFEST.md` (before the edit it was `8	0	MANIFEST.md`)
```
13	0	MANIFEST.md
```

`git diff --cached --name-only`. In the line below, one path segment is de-identified: the real segment is a support representative's first name, replaced here by `[name]`.
```
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
```
This name-free control shows the index holds exactly one path and that the path matches the expected PNG pattern:
```
$ git diff --cached --name-only | wc -l
       1
$ git diff --cached --name-only | grep -cx 'docs/reports/evidence/2026-10-28-mffu-[a-z]*-reply.png'
1
```

Extra checks:
```
$ git diff -U0 -- MANIFEST.md | grep -c '^-[^-]'        # deleted lines
0
$ tail -n 5 MANIFEST.md | grep -c '@'                    # address characters in new rows
0
$ tail -n 6 MANIFEST.md | awk -F'|' '{print NF}'         # field count: f1-closeout row, then the 5 new rows
7
7
7
7
7
7
```

## Adversarial findings
No separate adversary was used; the master's brief limited this to the manager's own check. My own check:
- Scope: numstat shows 13 added and 0 deleted, and the deleted-line count is 0. The 8 pre-existing uncommitted rows, including the parked unit's rows, are unchanged. The 5 new rows are the last 5 lines of the file.
- Shape: each new row has the same 7 pipe-delimited fields as the f1-closeout row, with type `Report`, block `3` and date `2026-11-10`.
- Personal data: the rows contain no `@` and no person's name. The rows name only the firm (MFFU) and role labels. In this report, the one name that would otherwise show up (inside the staged PNG path) is de-identified as marked above.
- Fidelity: each row's Result wording was checked against the report's own Result line, quoted in the Process log. The worker1 row reflects the manager note and not the worker's "(in progress)" placeholder; the row states both facts.
- Negative test: the scope gate for this unit is the numstat/deleted-line check. If any existing line had been altered, numstat would show a non-zero second column and the `^-` count would be non-zero. Both are 0. A full trip, editing an existing line to watch the count move, was not run, because doing so would modify a line the brief forbids touching.

## S6 cross-block check
No deviation is approved or proposed in this unit. MANIFEST is an index file, and the rows change no block spec. F4 stays FROZEN; F2 and F3 are untouched. Nothing here crosses into another block.

## Files staged
None by this unit. The index still holds only the PNG path above (de-identified). Modified in the working tree: `MANIFEST.md` (5 rows appended). New untracked file: this report.

Result: PASS

## Correction 1 (2026-11-10, after audit fail 1)

Written by the manager of unit 2026-11-10-f4-grading, correction 1. The first audit's finding 6 (S2): this report says that the 8 pre-existing uncommitted MANIFEST rows "are unchanged". It also says that "if any existing line had been altered, numstat would show a non-zero second column and the `^-` count would be non-zero." That second sentence is false for rows that are themselves uncommitted additions, and no snapshot of those rows was taken before the unit. Both sentences are retracted below. Commands were run by the manager on 2026-11-10 at HEAD `d30ab4d`. The runner prints each command line with a `$ ` prefix and then runs that exact line (block C1-V0 of `docs/reports/2026-11-10-f4-grading-correction-1-manager.md`).

### C1-M1. What numstat and the hunks show now

~~~text
$ git diff --numstat -- MANIFEST.md
13	0	MANIFEST.md
$ git diff -U0 -- MANIFEST.md | grep -c '^-[^-]'; git diff -U0 -- MANIFEST.md | grep -c '^+[^+]'
0
13
$ git diff -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -350,0 +359,5 @@
$ git diff -U0 -- MANIFEST.md | grep '^+[^+]' | cut -d'|' -f2 | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl
 /docs/specs/2026-11-06-walk-forward-values.md 
 /docs/specs/2026-11-05-walk-forward-spec.md 
 /docs/reports/2026-11-08-wf-spec-amendment-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md 
 /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md 
 /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md 
 /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch 
 /docs/reports/2026-11-10-f4-grading-manager.md 
 /docs/reports/2026-11-10-f4-grading-worker1.md 
 /docs/reports/2026-11-10-f4-grading-worker2.md 
 /docs/reports/2026-11-10-f4-grading-worker3.md 
 /docs/reports/2026-11-10-f4-grading-worker4.md 
$ git log -1 --format='%h %cI' -- MANIFEST.md
d30ab4d 2026-11-10T08:46:32-05:00
$ git diff HEAD --numstat -- MANIFEST.md; git diff --cached --numstat -- MANIFEST.md | wc -l
13	0	MANIFEST.md
       0
~~~

The last command compares the working copy with HEAD directly (`git diff HEAD`) and gives the same `13 0`. The index holds no MANIFEST change (0 lines), so the plain `git diff` above is also a diff against HEAD.

### C1-M2. Why the numstat test cannot see an in-place edit of an uncommitted row

This is the same diff computation, run on two scratch files under `/tmp`. `base.md` stands for the committed file and `m.md` for the working copy with two uncommitted rows added. Then one of the added rows is edited in place.

~~~text
$ rm -rf /tmp/f4c1/demo && mkdir /tmp/f4c1/demo && printf 'a\n' > /tmp/f4c1/demo/base.md && printf 'a\nrow1\nrow2\n' > /tmp/f4c1/demo/m.md && git diff --no-index --numstat /tmp/f4c1/demo/base.md /tmp/f4c1/demo/m.md
2	0	/tmp/f4c1/demo/{base.md => m.md}
$ sed -i '' 's/row1/row1-edited-in-place/' /tmp/f4c1/demo/m.md && git diff --no-index --numstat /tmp/f4c1/demo/base.md /tmp/f4c1/demo/m.md; git diff --no-index -U0 /tmp/f4c1/demo/base.md /tmp/f4c1/demo/m.md | grep -c '^-[^-]'
2	0	/tmp/f4c1/demo/{base.md => m.md}
0
~~~

Reading. Two added rows give `2 0`. After one of them is edited in place, the result is still `2 0` with 0 deleted lines. A diff against HEAD shows an uncommitted row only as an added line, whatever was done to it before.

### Retraction (replaces two sentences under "Adversarial findings")

- Retracted: "The 8 pre-existing uncommitted rows, including the parked unit's rows, are unchanged."
- Retracted: "If any existing line had been altered, numstat would show a non-zero second column and the `^-` count would be non-zero."
- What the evidence shows. `git diff --numstat -- MANIFEST.md` gives `13 0`. There are two added hunks, `@@ -306,0 +307,8 @@` (the 8 rows that were already uncommitted, all for the walk-forward unit) and `@@ -350,0 +359,5 @@` (this unit's 5 rows), and 0 deleted lines. So no line committed at HEAD was deleted or edited: an edit to a committed line would show as a deleted line. The 8 uncommitted rows are additions against HEAD, and C1-M2 shows that an edit to such a row leaves both counts as they are. No copy of those 8 rows was taken before this unit. **That the 8 pre-existing uncommitted rows are unchanged by this unit is UNVERIFIED.**
- Also UNVERIFIED: the figure "before the edit it was `8 0`" (Process log and the note above the numstat block). No output for it is pasted, and it cannot be re-run now.
- The negative-test paragraph holds only for lines committed at HEAD. It is not a scope gate for the 8 uncommitted rows. This correction does not change the 5 appended rows and does not change this report's Result line. The Result line's support for the 8 rows is now the UNVERIFIED statement above.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
