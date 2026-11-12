# 2026-11-12 v-rulings filing correction 3, worker2 (ADVERSARIAL)

## Task
Unit 2026-11-12-v-rulings-filing-correction-3, bead Praxis_build-n1y, worker2. ADVERSARIAL. Read-only apart from this report.

## Criteria
(a) to (g) of the brief. In progress.

## Commands and output
In progress.

## Findings
In progress.

## Result
In progress.

## Manager note (2026-11-12)
Written by the unit manager, not by worker2. Worker2 stopped at its 40-turn limit before it wrote its findings (REPORTED: this comes from the harness notification to the manager, which is not a command output and cannot be re-run). The sections above are its skeleton, unchanged (the diff against the pre-note copy is pasted at the end of this note). This report carries no adversarial result and the unit does not rely on it. Its working files are in /tmp/c3w2/; their sizes and times as pasted when this note was written in Correction 3 (that this paste ran before the note was added is REPORTED by the manager):
```
$ wc -l /tmp/c3w2/final.out /tmp/c3w2/final.sh
     214 /tmp/c3w2/final.out
      67 /tmp/c3w2/final.sh
     281 total
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md /tmp/c3w2/final.out
2026-11-11T19:52:28 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
2026-11-11T19:59:54 /tmp/c3w2/final.out
```
On that paste, the report was last written before the evidence file. REPORTED by the manager (dispatches are events, not command outputs): the leads in that evidence file were passed to worker3 (BUILD fix), and a fresh ADVERSARIAL pass (worker4) was dispatched after this note was written; its result is in docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md, not here.
Correction 3b: the diff of this file against the pre-note copy /tmp/c3mgr/w2.pre.md, run after the Correction 3b edits:
```
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
17a18,37
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
0
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
