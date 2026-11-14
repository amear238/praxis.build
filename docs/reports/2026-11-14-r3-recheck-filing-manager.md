# 2026-11-14 r3-recheck filing — manager report (unit `2026-11-14-r3-recheck-filing`)

## Task
File three audited, untracked reports unchanged, with MANIFEST rows, in temp index `/tmp/praxis-r3f/idx` read from HEAD a9d6b25. Audit: DECISION_LOG 2026-11-14T15:44:00Z, item (2), unit (b) VERDICT PASS.

## Rubric criteria addressed
S1 (output pasted below), S2 (levels stated as observed), S13 (sentence below, once).

## Workers dispatched
None. No adversary was dispatched (the brief allowed 0 or 1). All checks are the manager's own commands.

## Process log
1. The before shas were taken at 15:50:28Z. File mtimes, from `stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S%z'`: `2026-11-14T10:32:10-0500 ...-manager.md`, `2026-11-14T10:26:45-0500 ...-worker1.md`, `2026-11-14T10:28:03-0500 ...-worker2.md`. All three are before the 15:44:00Z audit row. No sha was recorded at audit time, so "unchanged since audit" rests on these mtimes, not on a sha.
2. MANIFEST blob = `git show a9d6b25:MANIFEST.md` + 4 rows (3 reports + this one), via `git hash-object -w` and `git update-index --add --cacheinfo`. The worker 1 row says "read with the manager report; three grading errors corrected there (manager :43, :50, :112-:118)". The working-tree MANIFEST was left alone. `git diff --stat a9d6b25 -- MANIFEST.md` gives `1 file changed, 42 insertions(+), 48 deletions(-)` from parked units, so it is not HEAD plus nothing.

## Verification evidence
Before (`shasum -a 256`), then after (`diff before.txt after.txt && echo ...`), then staged blobs (`git cat-file blob :<f> | shasum -a 256 | cut -c1-16`):
```
afa0572fef25315bdcf6a2ddfae4491711b89f0af4449719127fde18ae9a7d34  docs/reports/2026-11-14-r3-recheck-manager.md
f2eba7392812645cb8a6f33c32fbeba3a087d5db5a87606f5d6b09c25f6bb70c  docs/reports/2026-11-14-r3-recheck-worker1.md
937918bde67d6277e9949575565d99e050412f439dd7c8247eeb6ac60a141bbd  docs/reports/2026-11-14-r3-recheck-worker2.md
working files: before = after
afa0572fef25315b staged docs/reports/2026-11-14-r3-recheck-manager.md
f2eba7392812645c staged docs/reports/2026-11-14-r3-recheck-worker1.md
937918bde67d6277 staged docs/reports/2026-11-14-r3-recheck-worker2.md
```
`git diff --cached --name-status a9d6b25` and `--numstat a9d6b25` (temp index):
```
M	MANIFEST.md
A	docs/reports/2026-11-14-r3-recheck-filing-manager.md
A	docs/reports/2026-11-14-r3-recheck-manager.md
A	docs/reports/2026-11-14-r3-recheck-worker1.md
A	docs/reports/2026-11-14-r3-recheck-worker2.md
4	0	MANIFEST.md
59	0	docs/reports/2026-11-14-r3-recheck-filing-manager.md
140	0	docs/reports/2026-11-14-r3-recheck-manager.md
775	0	docs/reports/2026-11-14-r3-recheck-worker1.md
497	0	docs/reports/2026-11-14-r3-recheck-worker2.md
```
S13 (`grep -cxF "$S" <f>`, S taken by `grep -o` from SPEC_RUBRIC; filing-manager, manager, worker1, worker2), email matches on added diff lines (`grep '^+' | grep -v '^+++' | grep -E -o ... | wc -l`), real index (`env -u GIT_INDEX_FILE git diff --cached --name-status`):
```
1 1 1 1
0
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```
Negative tests: the same grep on a copy of the manager report with the S13 line removed gives `0`. A copy of worker1 with one byte appended hashes to `36a284e0ff258376` (it was `f2eba739...`). The email regex on a test string with an address gives `1`.

## Adversarial findings
None, because no adversary was dispatched. This is a filing-only unit, so the checks above are tested by the manager only (S2).

## S6 cross-block check
No DECISIONS.md or code was touched. The only diff is the 4 added MANIFEST rows and the 4 added files (numstat above).

## Files staged
Temp index only: MANIFEST.md and the four reports listed above. Nothing was staged in the real index.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Result: PASS
