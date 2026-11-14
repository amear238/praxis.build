# 2026-11-13 o4-cure1 manager report
## Task: Cure audit FAIL 1 on O4 (bead Praxis_build-yra), authorised by DECISION_LOG 2026-11-13T13:17:27Z (praxis-master, under D-2026-11-08-D D1). Deletion and labels only: MANIFEST.md :469-470 and the reduce3 manager report. DECISIONS.md not touched.

## Rubric criteria addressed: O4 (record hygiene of the D-2026-11-13-A evidence trail); S1 (pasted output backs every claim; the unbacked stray-write sentence is deleted).

## Workers dispatched: worker1 (a48c109ce3a68d26c), ADVERSARIAL, read-only: Overall FAIL (check 5). Report docs/reports/2026-11-13-o4-cure1-worker1.md.

## Process log: Pre-copies made, five Edit-tool edits (i)-(v) as briefed, diffs taken, one cold adversary, counts re-run by me. Adversary FAILed, so no cure round, per the hard limit.

## Verification evidence (command output)
```
$ wc -l MANIFEST.md /tmp/o4c1-pre-MANIFEST.md docs/reports/2026-11-13-o4-reduce3-manager.md /tmp/o4c1-pre-manager.md
     470 MANIFEST.md
     470 /tmp/o4c1-pre-MANIFEST.md
      90 docs/reports/2026-11-13-o4-reduce3-manager.md
      90 /tmp/o4c1-pre-manager.md
$ git diff --cached --name-only | wc -l      (start)
       1
$ diff /tmp/o4c1-pre-MANIFEST.md MANIFEST.md
469,470c469,470
< | /docs/reports/2026-11-13-o4-reduce3-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-o4-reduce3 (rubric O4, bead Praxis_build-yra; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T09:09:00Z and 13:02:03Z): three deletion-and-label edits to D-2026-11-13-A at DECISIONS.md :2393, :2405, :2410, full diff against a pre-copy, adversary grades quoted. |
< | /docs/reports/2026-11-13-o4-reduce3-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-o4-reduce3: checks (a)-(g) on D-2026-11-13-A, including byte checks of the cited quotes and the zero-hit grep the entry cites at :2402. |
---
> | /docs/reports/2026-11-13-o4-reduce3-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-o4-reduce3 (rubric O4, bead Praxis_build-yra; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T09:09:00Z and 13:02:03Z): three deletion-and-label edits to D-2026-11-13-A at working-tree DECISIONS.md :2393, :2405, :2410 (the entry's Decision 1, Sources and S6 cross-block paragraphs), full diff against a pre-copy, adversary grades quoted. |
> | /docs/reports/2026-11-13-o4-reduce3-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-o4-reduce3: checks (a)-(g) on D-2026-11-13-A, including byte checks of the cited quotes and the zero-hit grep the entry cites in its Sources (strategy bullet; working-tree DECISIONS.md :2402). |
$ diff /tmp/o4c1-pre-manager.md docs/reports/2026-11-13-o4-reduce3-manager.md | sed -E 's#docs/reports/evidence[/][^ ]*#[evidence path withheld]#'
13c13
< [evidence path withheld]
---
> [one path withheld: a staged evidence file whose name carries a person's name]
78d77
< Stray-write check: files newer than the pre-copy are DECISIONS.md, the two reports, and DISPATCH_LOG.md. DISPATCH_LOG.md's last rows are "hook-recorded at SubagentStart" / "SubagentStop" (13:03:18Z, 13:06:21Z), so the hook wrote them, not the worker. The index count is still 1 at the end.
87a87,88
> Correction (2026-11-13, cure of audit FAIL 1, DECISION_LOG 2026-11-13T13:17:27Z): line 13's pasted path is withheld because the file name carries a person's name; the stray-write sentence formerly at line 78 had no pasted output and is deleted. Nothing else in this report changed.
> 
$ for f in $R $W MANIFEST.md /tmp/o4c1-pre-MANIFEST.md $M; do echo "$f evidence=$(grep -c 'evidence[/]' $f) email=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}' $f)"; done   (R = reduce3 manager report, W = worker1 report, M = this report)
docs/reports/2026-11-13-o4-reduce3-manager.md evidence=0 email=0
docs/reports/2026-11-13-o4-cure1-worker1.md evidence=0 email=0
MANIFEST.md evidence=8 email=0
/tmp/o4c1-pre-MANIFEST.md evidence=8 email=0
docs/reports/2026-11-13-o4-cure1-manager.md evidence=0 email=0
$ grep -n 'evidence[/]' MANIFEST.md | cut -d: -f1
140 314 336 345 346 347 348 351
$ git diff --cached --name-only | wc -l      (end)
       1
```

## Adversarial findings (worker1 report, quoted)
Grades: :5 "## (1) Diffs exactly as expected: PASS"; :25 "## (2) Each of the three findings cured: PASS"; :34 "## (3) Correction line true: PASS"; :37 "## (4) Labels and paragraph names: PASS"; :48 "## (5) Zero evidence paths and emails in all three files: FAIL"; :66 "Overall: FAIL".
:64 process note: the worker wrote a scratch copy of DECISIONS.md under /tmp against the brief, then deleted it.
Check 5 fails on MANIFEST.md: 8 rows carry the evidence-directory path (all there before the cure, and the pre-copy count is also 8). Row :336 holds the same person-named file name that was withheld at report :13. These rows are outside the authorised lines 469-470, so I did not touch them, and I am not softening the criterion.

## S6 cross-block check: Labels and deletions only. No value, gate, breaker or spec body changed. Blocks 2 to 4 are not affected.

## Files staged: None by this unit. Index count is 1 at start and end. Modified: MANIFEST.md :469-470 and the reduce3 manager report. New: this report and the worker1 report. Neither new report has a MANIFEST row, because lines outside 469-470 are off limits; the master has to add those rows.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
