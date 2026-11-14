# 2026-11-14 dirty-tree CNA filing: finisher manager report

## Task

Finish unit `2026-11-14-dirty-tree-cna-filing` from the artifacts the first manager left on disk. Three DECISION_LOG rows govern it, each read in full by grepping its stamp:

- DECISION_LOG.md:956 `[2026-11-14T09:06:00Z]`: unit scope. Rule (i) lifts an earlier exclusion row only where its reason was scope or timing, and "a doubtful case stays out". Rule (ii): a file with a rep-name hit, an email address or a credential-like string stays out, with no redaction. Rule (iii): files are filed with their text unchanged, and "a docs/reports file whose last standalone line is not the S13 sentence gets two lines appended at the end". Rule (iv): one temp index /tmp/praxis-cna/idx built from HEAD 9a18fde, the MANIFEST blob is HEAD MANIFEST.md plus one row per filed file, and the real index is not touched.
- DECISION_LOG.md:957 `[2026-11-14T09:36:00Z]`: the first manager "stopped at its 60-turn limit with no report and no verdict". The master counts that as FAIL for the commit decision but not as a strike. It dispatched one finisher that changes nothing and writes this report from the artifacts, with no new adversary.
- DECISION_LOG.md:958 `[2026-11-14T09:39:00Z]`: amends 09:36 by one change. `docs/reports/2026-11-13-open-a1-cure-worker1.md` already carried the S13 sentence once as a standalone line (:327), so the append made it twice, against S13 "carries, once" ("standalone lines count"). The finisher restores that file to its pre-append bytes, re-adds it to the temp index and recomputes the canonical hash. "The other 11 appends stand (each file had 0 standalone S13 lines before)."

Rubric criteria addressed: S1, S2, S7, S13 (specs/SPEC_RUBRIC.md).

## What the first manager did

Level: it built the work and ran three adversary rounds. It did not report or give a verdict (DECISION_LOG :957). From the artifacts in /tmp/praxis-cna:

- cands.txt: 36 candidates, grouped U4, U9, U10, U13, U18, U19, U21, U22, U25 and U27.
- in32.txt: 32 IN paths. out.txt: 4 OUT paths.
- append12.txt: 12 files given the two-line append, with pre-append copies in pre/ and hashes in pre-sha.txt. unedited20.txt holds the hashes of the 20 files it did not edit.
- rows.txt (32 rows) and MANIFEST.blob: HEAD MANIFEST.md plus those rows.
- idx: the temp index. worker3 graded it at hash adbf31b8...5c30 (worker3 :131), and the master recomputed the same hash (DECISION_LOG :957).
- Earlier states also remain on disk: in.txt (33), append.txt (11), append10.txt, rows-new*.txt, unedited.txt and unedited-sha.txt (22). They are round-1 and round-2 states, superseded. worker3 observation 1 flags unedited-sha.txt as stale.

No manager report existed before this one. This report is written from those artifacts and the fresh checks below, not from the first manager's reasoning.

## IN table (32)

Exclusion-row quotes come from worker2's Check A table (worker2 :12-:37). Each phrase was re-checked this session against its DECISION_LOG line (q.sh output below; all 15 counts are 1). "Appended" means the two-line filer's note plus S13 at the end of the file, as it stands after the restore.

| # | Path | Exclusion row and reason (quoted) | Appended |
|---|---|---|---|
| 1 | docs/reports/2026-07-28-session39-agents-dir-write-path.md | none (worker2 :12: ":121 cites it as the report; no exclusion row") | y |
| 2 | docs/reports/2026-08-06-facts-pack.md | none (:165 cites it as evidence) | y |
| 3 | docs/reports/2026-08-06-praxis-assessment.md | none (:165) | y |
| 4 | docs/reports/2026-08-06-subreport-agent-memory.md | none ("no row names it") | y |
| 5 | docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md | none. Its header label "must not be cited as a finding" is "the file's own label, not an exclusion row" (worker2 :16) | y |
| 6 | docs/reports/2026-08-29-session53-parallel-handoff.md | none (:375, :389 "(untracked)") | y |
| 7 | docs/reports/2026-10-26-nightly-spec-request-review.md | none (:433 "What survives") | y |
| 8 | docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md | none (:632) | y |
| 9 | docs/reports/2026-11-01-csv-analyses-fix-manager-record.md | :616 "Excluded: `2026-11-01-csv-analyses-fix-manager-record.md` (gate artefact)". This is scope: a commit-composition list (worker2 note 1, :39) | y |
| 10 | docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md | :622 "excluded from the commit and MANIFEST" (scope) | y |
| 11 | docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md | :776 "stays out of this commit and untracked" (scope) | y |
| 12 | vm/replies/20261110T214542Z-STATUS.md | none (:818-:823). vm/replies files are not edited | n |
| 13 | vm/replies/20261110T214834Z-self-report.md | none | n |
| 14 | vm/replies/20261110T215014Z-STATUS.md | none | n |
| 15 | vm/replies/20261110T224920Z-2b-skill-job.md | none | n |
| 16 | docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md | :883 "stay on disk, uncommitted and unedited, as the record of the failed attempts" (scope; no content clause against this file) | n |
| 17 | docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md | :883 as above | n |
| 18 | docs/reports/2026-11-13-o3-cure3-manager.md | :897 "stay on disk, uncommitted" (scope) | n (2 standalone S13 lines, see Result) |
| 19 | docs/reports/2026-11-13-o3-cure3-worker1.md | :897 as above | n |
| 20 | docs/reports/2026-11-13-o4-parity-worker1.md | :912 "The five earlier O4 reports stay on disk, uncommitted." Its content clause is about `-o4-parity-manager.md`, which is not a candidate (worker2 :33) | n |
| 21 | docs/reports/2026-11-13-o4-parity-worker2.md | :912 as above | n (2 standalone S13 lines, see Result) |
| 22 | docs/reports/2026-11-13-o4-parity-worker3.md | :912 as above | n (2 standalone S13 lines, see Result) |
| 23 | docs/reports/2026-11-13-o4-parity-worker4.md | :912 as above | n |
| 24 | docs/reports/2026-11-13-o4-reduce-manager.md | :912; :913 "Out of the commit, on disk:" (scope) | n |
| 25 | docs/reports/2026-11-13-o4-reduce-worker1.md | :912; :913 | n |
| 26 | docs/reports/2026-11-13-o4-reduce2-manager.md | :912; :913 | n |
| 27 | docs/reports/2026-11-13-o4-reduce2-worker1.md | :912; :913 | n |
| 28 | docs/reports/2026-11-13-o4-repoint-manager.md | :913 "Out of the commit, on disk:" (scope) | n |
| 29 | docs/reports/2026-11-13-o4-repoint-worker1.md | :913 | n |
| 30 | docs/reports/2026-11-13-o4-cure1-manager.md | :915 "out of the commit's scope" | n |
| 31 | docs/reports/2026-11-13-o4-cure1-worker1.md | :915 | n |
| 32 | docs/reports/2026-11-13-open-a1-cure-worker1.md | :923 "whose report stays out of the commit"; :925 "Out of the commit, on disk:" (scope) | n (restored under :958) |

## OUT list (4) for HANDOFF

1. `docs/reports/2026-10-28-review-note-delivery.md`. Rule (ii): it contains email addresses. The fresh check shows 5 regex hits (`review-note-delivery email-regex hits: 5`). It is not redacted, under rule (ii).
2. `docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md`. Content: :883 lists it as "still open in the older reports", with "defect-6 cures at correction-1 manager ... unchecked".
3. `docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md`. Content: :883 "cured by the manager in its own report only, unchecked".
4. `docs/reports/2026-11-12-o3-block1-scope-evidence.md`. Content, or at least doubtful: :889 "Adversary 4 `GRADE: FAIL (7 defects)`", six of them report wording. :889 and :890 freeze it "unedited". It was moved OUT on worker2 defect 1 (worker2 :94).

The fresh check confirms all four are on disk and absent from the temp index. No rows.txt row names any of them (q.sh output: `0`).

## The open-a1 restore (DECISION_LOG :958)

The restore copied `/tmp/praxis-cna/pre/2026-11-13-open-a1-cure-worker1.md` over the working file, then ran `GIT_INDEX_FILE=/tmp/praxis-cna/idx git update-index --add` on the path. Output of /tmp/praxis-cna-fin/fix.sh:

```
HEAD 9a18fde
--- before restore: 28e0ccced63017efbf109399cf5019a705ae14a3068282e0fdbc60bc1b003432  docs/reports/2026-11-13-open-a1-cure-worker1.md
--- after restore:  b6aff5053806ad3104daea2783f545463097ad9fb79cbed5c4346930b63c88db  docs/reports/2026-11-13-open-a1-cure-worker1.md
--- pre-sha entry:  b6aff5053806ad3104daea2783f545463097ad9fb79cbed5c4346930b63c88db  docs/reports/2026-11-13-open-a1-cure-worker1.md
RESTORE_SHA_MATCH
     328 docs/reports/2026-11-13-open-a1-cure-worker1.md
[line 327 = the S13 sentence; elided here so that this report carries it standalone only once]
Result: FAIL
update-index --add ok
rows matching old clause: 1 [32]
32c32
< | /docs/reports/2026-11-13-open-a1-cure-worker1.md | Report | 3 | 2026-11-13 |
---
> | /docs/reports/2026-11-13-open-a1-cure-worker1.md | Report | 3 | 2026-11-13 |
(diff exit shown above; row lines truncated to 80 cols)
      32 /tmp/praxis-cna/rows-fin.txt
new MANIFEST blob e33ec4097c04f9cb9c10183663abe58d5b87060d
MANIFEST re-added
rows.txt now = rows-fin.txt (original kept as rows-pre0939.txt)
      11 /tmp/praxis-cna/append11.txt
```

Disclosure: line 327 of the paste above has been edited. The real output printed the S13 sentence there. It is replaced with a bracketed note so that this report carries the sentence as a standalone line exactly once.

MANIFEST row 32 mentioned the append. Its old clause was "S13 sentence standalone at :327, before the Result line, and an S13 filer's note and sentence appended at :329-:330;". The new clause is "S13 sentence once standalone at :327, before the Result line; filed as written, no line changed (an append made at filing was reverted under DECISION_LOG 2026-11-14T09:39:00Z);". The working-tree MANIFEST.md had no row for this path (`grep -c 'open-a1-cure-worker1' MANIFEST.md` printed `0`), so it was not edited.

## Adversary rounds 1-3

- Round 1, worker1: `191:Result: FAIL`. Defect 1 was wording: "Every staged blob equals its working-tree file" is false for MANIFEST.md, which differs by design. Cure: the blob check now covers the 32 A paths only, and MANIFEST is checked as HEAD plus rows (worker3 Claim 5; check 3 below). Defect 2: c7-probe-fresh-manifest-manager carried S13 inside :3 and had it appended again. The first manager reverted that append (worker2 :57: "sha256 is now `7719abd0...` , the same as /tmp/praxis-cna/pre/"). Worker1 also left the open-a1 reading unresolved (worker1 :78).
- Round 2, worker2: `110:Result: FAIL`.
  - Defect 1: -evidence.md was IN on content grounds. Cure: moved OUT (out.txt #4; not in in32).
  - Defect 2: c7-probe did not get the rule (iii) append. Cure: re-appended. c7 is in append11, and its standalone S13 count is 1 (the copy at :3 is inside a line).
  - Defect 3: open-a1 did not get the rule (iii) append. Cure: appended. That gave the file two standalone S13 lines, which the master reversed at :958 (restore above).
  - Defect 4: the R18 description of -evidence.md. Moot, because -evidence.md is OUT and has no row (q.sh: `0`).
- Round 3, worker3: `173:Result: PASS`, grading hash adbf31b8602a509470677f1c726e48841d00449344d9684c3623e4b723615c30 (:131). That hash is now superseded. After the restore the canonical hash is 460f12a67550437051a62d9e8d49481c95058ce211492272b79d41e126a37d62, which no adversary has graded.

Worker3 observation 2 (worker3 :160), disclosed: one of worker3's diagnostic commands echoed a label built from the name variable, so the private name token was printed once in worker3's own tool output. It is not in any file: worker3's report self-count is `count: 0`, and the fresh sum over the 32 staged files below is 0.

## Verification evidence (fresh checks, S1)

Command scripts: /tmp/praxis-cna-fin/chk.sh, chk2.sh and q.sh. The output below is pasted verbatim.

One tool artifact: in chk.sh the `prefix=` column reads `N` for all 11 files. That came from BSD `cmp -n`, which returned 1 (`cmp_n_rc=1` in chk2). chk2 re-tests the prefix with `head -c <presize> | cmp - pre` and gets `headc_prefix=Y` for all 11, with `delta=2` lines and pre_sha_ok=Y. The cause of the BSD `cmp -n` behaviour was not investigated.

chk.sh:

```
== HEAD 9a18fde
== 1. name-status (temp index)
  32 A
   1 M
M	MANIFEST.md
A	docs/reports/2026-07-28-session39-agents-dir-write-path.md
A	docs/reports/2026-08-06-facts-pack.md
A	docs/reports/2026-08-06-praxis-assessment.md
A	docs/reports/2026-08-06-subreport-agent-memory.md
A	docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md
A	docs/reports/2026-08-29-session53-parallel-handoff.md
A	docs/reports/2026-10-26-nightly-spec-request-review.md
A	docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md
A	docs/reports/2026-11-01-csv-analyses-fix-manager-record.md
A	docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md
A	docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md
A	docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
A	docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
A	docs/reports/2026-11-13-o3-cure3-manager.md
A	docs/reports/2026-11-13-o3-cure3-worker1.md
A	docs/reports/2026-11-13-o4-cure1-manager.md
A	docs/reports/2026-11-13-o4-cure1-worker1.md
A	docs/reports/2026-11-13-o4-parity-worker1.md
A	docs/reports/2026-11-13-o4-parity-worker2.md
A	docs/reports/2026-11-13-o4-parity-worker3.md
A	docs/reports/2026-11-13-o4-parity-worker4.md
A	docs/reports/2026-11-13-o4-reduce-manager.md
A	docs/reports/2026-11-13-o4-reduce-worker1.md
A	docs/reports/2026-11-13-o4-reduce2-manager.md
A	docs/reports/2026-11-13-o4-reduce2-worker1.md
A	docs/reports/2026-11-13-o4-repoint-manager.md
A	docs/reports/2026-11-13-o4-repoint-worker1.md
A	docs/reports/2026-11-13-open-a1-cure-worker1.md
A	vm/replies/20261110T214542Z-STATUS.md
A	vm/replies/20261110T214834Z-self-report.md
A	vm/replies/20261110T215014Z-STATUS.md
A	vm/replies/20261110T224920Z-2b-skill-job.md
== A-set vs in32.txt
SAME
== MANIFEST numstat
32	0	MANIFEST.md
== canonical hash (gate-commit.sh :678 command, GIT_INDEX_FILE set, repo root)
460f12a67550437051a62d9e8d49481c95058ce211492272b79d41e126a37d62  -
== 2. staged blob = working-tree hash-object (32 A paths)
mismatches: 0 of       32
== 3. MANIFEST blob = HEAD MANIFEST + rows
HEAD lines      475; staged lines      507; tail lines 32
HEAD_PREFIX_CMP_OK
TAIL_EQ_ROWS_OK
staged MANIFEST blob: e33ec4097c04f9cb9c10183663abe58d5b87060d
open-a1 rows in staged blob mentioning 'appended at :329': 0
open-a1 rows in staged blob: 1
== 4a. 11 appended files: current = pre + exactly two lines
2026-07-28-session39-agents-dir-write-path.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-08-06-facts-pack.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-08-06-praxis-assessment.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-08-06-subreport-agent-memory.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-08-07-f3-fill-resolution-research-UNGRADED.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-08-29-session53-parallel-handoff.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-10-26-nightly-spec-request-review.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-10-31-voice-handoff-future-row-walkthrough.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-11-01-csv-analyses-fix-manager-record.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-11-01-three-strategy-results-s2-fix-manager-record.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
2026-11-09-c7-probe-fresh-manifest-manager.md prefix=N pre_sha_ok=Y extra_lines=2 line1='Filer's note (2026-11-14, unit 2026-11-1' line2=S13
distinct filer's-note lines across 11: 1
== 4b. 21 other staged paths unchanged
unedited20 match: 20 of       20
open-a1 current b6aff5053806ad3104daea2783f545463097ad9fb79cbed5c4346930b63c88db vs pre-sha b6aff5053806ad3104daea2783f545463097ad9fb79cbed5c4346930b63c88db: MATCH
coverage: append11 + unedited20 + open-a1 = 32 distinct; equal to in32: Y
== 5. standalone S13 count (grep -cxF) per staged docs/reports file
1 docs/reports/2026-07-28-session39-agents-dir-write-path.md
1 docs/reports/2026-08-06-facts-pack.md
1 docs/reports/2026-08-06-praxis-assessment.md
1 docs/reports/2026-08-06-subreport-agent-memory.md
1 docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md
1 docs/reports/2026-08-29-session53-parallel-handoff.md
1 docs/reports/2026-10-26-nightly-spec-request-review.md
1 docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md
1 docs/reports/2026-11-01-csv-analyses-fix-manager-record.md
1 docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md
1 docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md
1 docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
1 docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
2 docs/reports/2026-11-13-o3-cure3-manager.md
1 docs/reports/2026-11-13-o3-cure3-worker1.md
1 docs/reports/2026-11-13-o4-parity-worker1.md
2 docs/reports/2026-11-13-o4-parity-worker2.md
2 docs/reports/2026-11-13-o4-parity-worker3.md
1 docs/reports/2026-11-13-o4-parity-worker4.md
1 docs/reports/2026-11-13-o4-reduce-manager.md
1 docs/reports/2026-11-13-o4-reduce-worker1.md
1 docs/reports/2026-11-13-o4-reduce2-manager.md
1 docs/reports/2026-11-13-o4-reduce2-worker1.md
1 docs/reports/2026-11-13-o4-repoint-manager.md
1 docs/reports/2026-11-13-o4-repoint-worker1.md
1 docs/reports/2026-11-13-o4-cure1-manager.md
1 docs/reports/2026-11-13-o4-cure1-worker1.md
1 docs/reports/2026-11-13-open-a1-cure-worker1.md
vm/replies S13 counts: 0 0 0 0 
== 6. name token / email
token source files found: 1; token length 4
added lines in staged diff: 6120
token hits (case-insens.) in added lines: 0
email hits in added lines: 0
token hits summed over 32 staged files: 0
token hits in staged MANIFEST blob: 2
== 7. real index
336b5c3f279a7b79f070f5985c14408dff2d67d3caefa034b5713af9a572b763  -
real cached count: 1
== OUT files: on disk, absent from temp index
disk=Y idx=N docs/reports/2026-10-28-review-note-delivery.md
disk=Y idx=N docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
disk=Y idx=N docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md
disk=Y idx=N docs/reports/2026-11-12-o3-block1-scope-evidence.md
```

chk2.sh:

```
== 4a recheck: byte-prefix via head -c (cmp -n result above re-tested)
2026-07-28-session39-agents-dir-write-path.md headc_prefix=Y cmp_n_rc=1 pre_lines=430 cur_lines=432 delta=2 pre_standalone_S13=0
2026-08-06-facts-pack.md headc_prefix=Y cmp_n_rc=1 pre_lines=235 cur_lines=237 delta=2 pre_standalone_S13=0
2026-08-06-praxis-assessment.md headc_prefix=Y cmp_n_rc=1 pre_lines=154 cur_lines=156 delta=2 pre_standalone_S13=0
2026-08-06-subreport-agent-memory.md headc_prefix=Y cmp_n_rc=1 pre_lines=363 cur_lines=365 delta=2 pre_standalone_S13=0
2026-08-07-f3-fill-resolution-research-UNGRADED.md headc_prefix=Y cmp_n_rc=1 pre_lines=339 cur_lines=341 delta=2 pre_standalone_S13=0
2026-08-29-session53-parallel-handoff.md headc_prefix=Y cmp_n_rc=1 pre_lines=278 cur_lines=280 delta=2 pre_standalone_S13=0
2026-10-26-nightly-spec-request-review.md headc_prefix=Y cmp_n_rc=1 pre_lines=297 cur_lines=299 delta=2 pre_standalone_S13=0
2026-10-31-voice-handoff-future-row-walkthrough.md headc_prefix=Y cmp_n_rc=1 pre_lines=123 cur_lines=125 delta=2 pre_standalone_S13=0
2026-11-01-csv-analyses-fix-manager-record.md headc_prefix=Y cmp_n_rc=1 pre_lines=52 cur_lines=54 delta=2 pre_standalone_S13=0
2026-11-01-three-strategy-results-s2-fix-manager-record.md headc_prefix=Y cmp_n_rc=1 pre_lines=64 cur_lines=66 delta=2 pre_standalone_S13=0
2026-11-09-c7-probe-fresh-manifest-manager.md headc_prefix=Y cmp_n_rc=1 pre_lines=91 cur_lines=93 delta=2 pre_standalone_S13=0
cmp variant: cmp: unrecognized option `--version'
filer's note text (identical in all 11):
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
== S13 double-standalone files: line numbers of standalone S13, last line, sha vs unedited20
docs/reports/2026-11-13-o3-cure3-manager.md: S13 at lines 25 50 of 50; in append11: 0; sha listed in unedited20: 1
docs/reports/2026-11-13-o4-parity-worker2.md: S13 at lines 264 314 of 314; in append11: 0; sha listed in unedited20: 1
docs/reports/2026-11-13-o4-parity-worker3.md: S13 at lines 251 296 of 296; in append11: 0; sha listed in unedited20: 1
== name token in MANIFEST: HEAD part vs 32 added rows
HEAD:MANIFEST.md hits: 2
rows.txt (32 added rows) hits: 0
HEAD MANIFEST hit lines contain the F4 reply-filing path: 1
token hits in my draft report (if present): absent
== worker report Result lines
docs/reports/2026-11-14-dirty-tree-cna-filing-worker1.md: 191:Result: FAIL 
docs/reports/2026-11-14-dirty-tree-cna-filing-worker2.md: 110:Result: FAIL 
docs/reports/2026-11-14-dirty-tree-cna-filing-worker3.md: 173:Result: PASS 
131:hash adb
== exclusion-row quotes for OUT files (DECISION_LOG line numbers)
review-note-delivery: 441 957 
correction-1-manager: 738 739 810 821 826 864 881 
correction-2-manager: 728 731 732 838 
scope-evidence: 886 887 889 890 
review-note-delivery email-regex hits: 5
== rows.txt exclusion mentions per row (row#: 'kept out'/'stay' phrases)
1:  2:  3:  4:  5:  6:  7:  8:  9:  10: EXCL-CITED 11: EXCL-CITED 12:  13:  14:  15:  16:  17:  18:  19:  20:  21:  22:  23:  24:  25:  26:  27:  28: EXCL-CITED 29:  30:  31:  32: EXCL-CITED 
```

q.sh (exclusion quotes re-checked on their DECISION_LOG lines):

```
count  DECISION_LOG-line  quoted phrase (1 = phrase present on that line)
1  :616  csv-analyses-fix-manager-record.md` (gate artefact)
1  :622  excluded from the commit and MANIFEST
1  :776  stays out of this commit and untracked
1  :883  stay on disk, uncommitted and unedited, as the record of the failed attempts
1  :883  defect-6 cures at correction-1 manager
1  :883  cured by the manager in its own report only, unchecked
1  :889  Adversary 4 `GRADE: FAIL (7 defects)`
1  :889  the old evidence report stays on disk, unedited from now, uncommitted
1  :890  stay on disk, unedited, uncommitted
1  :897  stay on disk, uncommitted
1  :912  The five earlier O4 reports stay on disk, uncommitted.
1  :913  Out of the commit, on disk:
1  :915  out of the commit's scope
1  :923  whose report stays out of the commit
1  :925  Out of the commit, on disk:
rows.txt rows naming -evidence.md, review-note-delivery, correction-1-manager, correction-2-manager: 0
```

## S6 cross-block check

This unit's only deviation is the :958 restore. It touches two things: the one report file, and its MANIFEST row in the temp-index blob. No spec, strategy, hook or ledger block is in this unit's scope, and none was edited. The real index fingerprint and the HEAD sha (pasted above) show nothing else moved.

Lines :329 and :330 of open-a1-cure-worker1 existed only after the append. I searched tracked files (`git grep`) and the staged MANIFEST blob for references to them and found none: `refs to open-a1 :329/:330 in tracked files + staged blob: 0 / 0`. The self-check above was taken before this section was added. Recomputed after it was added: `token 0; email 0; standalone S13 1; last=S13 Y`.

## Files staged

- Temp index /tmp/praxis-cna/idx: 32 A paths (the IN table) and 1 M (MANIFEST.md, blob e33ec4097c04f9cb9c10183663abe58d5b87060d, 32 rows added, 0 removed). Canonical hash: 460f12a67550437051a62d9e8d49481c95058ce211492272b79d41e126a37d62. The index is left in place for the master.
- Real index: untouched. The fingerprint is 336b5c3f...b763, with 1 staged path.
- Working tree, edited by this finisher: `docs/reports/2026-11-13-open-a1-cure-worker1.md`, restored to its pre bytes. This report was also written, and is neither staged nor tracked.
- New artifacts in /tmp/praxis-cna: rows-fin.txt (rows.txt now equals it), rows-pre0939.txt (the old rows.txt), MANIFEST-fin.blob and append11.txt. Scripts and outputs are in /tmp/praxis-cna-fin.

## Decisions taken by me, for the master

1. MANIFEST row 32 wording: the replacement clause quoted above. The rest of the row is byte-identical.
2. rows.txt was overwritten with the corrected rows so the artifact matches the staged blob, and the old copy was kept as rows-pre0939.txt. MANIFEST.blob (the old blob file) was left unchanged. The staged blob is MANIFEST-fin.blob.
3. Result is BLOCKED, not PASS, for two reasons:
   - (a) The brief's check "standalone S13 line count = 1 in every staged docs/reports file" fails on 3 of 28 files. Each was filed unedited (sha matches unedited20) and already ended on the S13 sentence, so rule (iii) gave no append. Each also carries a second standalone copy earlier in its own text:
     - o3-cure3-manager, S13 at :25 and :50
     - o4-parity-worker2, :264 and :314
     - o4-parity-worker3, :251 and :296

     :958 holds that standalone lines count against "carries, once". Under that reading, the same breach found in open-a1 is present in these three files. The defect is in their authored text, not something this unit added. Worker2 :95 had noted it ("R19, R22 and R23 file reports that carry two standalone S13 lines, unchanged"). Curing it needs an edit to authored text, which rule (iii) forbids, or moving the files OUT. Both are outside this finisher's limits. The master needs to choose: (i) a written ruling that pre-existing duplicates in text filed unchanged are acceptable; (ii) move the three files OUT and drop their rows; or (iii) authorise a cure edit.
   - (b) The hash changed to 460f12a6...7d62. Under S7, the new hash needs praxis-auditor grading before any commit.
4. The 2 name-token hits in the staged MANIFEST blob are both in the HEAD part, which is already committed. One hit line is the F4 reply-filing path row. The 32 added rows have 0 hits, and the added lines of the diff have 0. I leave it to the master whether HEAD content is in scope for rule (ii). This unit did not add those hits.

## Name-token and email self-check of this report

```
name-token count (case-insensitive) in this report before this section: 0
email-regex hits: 0
standalone S13 lines before the closing line: 0
```

Result: BLOCKED

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
