# 2026-11-14 dirty-tree CNA filing: adversarial worker 1

## Task
Adversarial check of the claims C1-C6 made by unit 2026-11-14-dirty-tree-cna-filing: the 11 appended files, the 22 unedited files, the temp index /tmp/praxis-cna/idx, the staged MANIFEST.md, and the real index.

## Mode
ADVERSARIAL, read-only. HEAD = 9a18fdee64b563c86dd2fda92e344651f913a38f. This file is my only write in the repo. Scratch is under /tmp/praxis-cna-w2/ (s1.sh, s2.sh, s3.sh). I never wrote /tmp/praxis-cna/idx: `git write-tree` ran on a copy (/tmp/praxis-cna-w2/idx-copy), and the sha256 of idx was the same before and after my reads. Every script's output went through a perl filter that would print `<N>` in place of the name token. That marker appears nowhere below.

Method notes. "Last standalone line" means the last non-blank line (`awk 'NF{l=$0} END{print l}'`). The S13 counts in C2 are whole-line counts (`grep -cxF`). The S13 counts in C1 are substring counts (Python `bytes.count`).

## Checks C1-C6

### C1: the 11 appended files. PASS (as stated)
Runner: `bash /tmp/praxis-cna-w2/s1.sh` (section `=== C1`). For each file the script checks four things. One, post starts with the pre bytes. Two, the tail after them is exactly the filer's note line, a newline, the S13 sentence and a newline. Three, the diff has exactly 2 changed lines and both are additions. Four, both shas match the recorded values and the pre copy's last line is not S13.
```
=== C1
2026-07-28-session39-agents-dir-write-path.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-08-06-facts-pack.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-08-06-praxis-assessment.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-08-06-subreport-agent-memory.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-08-07-f3-fill-resolution-research-UNGRADED.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-08-29-session53-parallel-handoff.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-10-26-nightly-spec-request-review.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-10-31-voice-handoff-future-row-walkthrough.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-11-01-csv-analyses-fix-manager-record.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-11-01-three-strategy-results-s2-fix-manager-record.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=0 s13_in_post=1 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
2026-11-09-c7-probe-fresh-manifest-manager.md | OK b"Filer'" pre_ends_nl=True s13_in_pre=1 s13_in_post=2 note_in_pre=0 | diff_lines=2 | pre_sha_match=Y post_sha_match=Y | pre_last_is_S13=no
```
All 11 match the claim as worded. But see the c7-probe row: `s13_in_pre=1 s13_in_post=2`. That is Defect 2.

Follow-up (s2.sh):
```
/tmp/praxis-cna/pre/2026-11-09-c7-probe-fresh-manifest-manager.md lines=      91
3:Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md lines=      93
3:Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
93:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

### C2: the 22 unedited files. PASS on the facts. The open-a1 decision is graded under two readings below and left unresolved.
```
=== C2
20261110T214542Z-STATUS.md sha_match=Y s13count=0 last=(not reports)
20261110T214834Z-self-report.md sha_match=Y s13count=0 last=(not reports)
20261110T215014Z-STATUS.md sha_match=Y s13count=0 last=(not reports)
20261110T224920Z-2b-skill-job.md sha_match=Y s13count=0 last=(not reports)
2026-11-12-o3-block1-scope-correction-1-worker1.md sha_match=Y s13count=1 last=S13
2026-11-12-o3-block1-scope-correction-2-worker2.md sha_match=Y s13count=1 last=S13
2026-11-12-o3-block1-scope-evidence.md sha_match=Y s13count=1 last=S13
2026-11-13-o3-cure3-manager.md sha_match=Y s13count=2 last=S13
2026-11-13-o3-cure3-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-parity-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-parity-worker2.md sha_match=Y s13count=2 last=S13
2026-11-13-o4-parity-worker3.md sha_match=Y s13count=2 last=S13
2026-11-13-o4-parity-worker4.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-reduce-manager.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-reduce-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-reduce2-manager.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-reduce2-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-repoint-manager.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-repoint-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-cure1-manager.md sha_match=Y s13count=1 last=S13
2026-11-13-o4-cure1-worker1.md sha_match=Y s13count=1 last=S13
2026-11-13-open-a1-cure-worker1.md sha_match=Y s13count=1 last=NOT_S13: Result: FAIL
```
All 22 shas match. All 4 vm/replies files are unedited and contain no S13. 17 of the 18 docs/reports files end on S13. The only exception is open-a1-cure-worker1, as the claim says. Its tail (`cat -vet`; the file has 328 lines, S13 at :327 and `Result: FAIL` at :328):
```
I did not investigate this further. It is outside this unit's diff, which is taken against the pre-copies.$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.$
Result: FAIL$
```
Rubric text (specs/SPEC_RUBRIC.md:145, cut at 400 chars):
```
145:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." ...
```
Two readings for docs/reports/2026-11-13-open-a1-cure-worker1.md:
- Reading A (unit rule: "a docs/reports file whose last standalone line is not the S13 sentence gets two lines appended"). The last standalone line is `Result: FAIL`, so the rule calls for an append. Under this reading, skipping the file is a FAIL.
- Reading B (rubric S13: carries the sentence "once"). The file already carries the sentence once, as a standalone line at :327. An append would make it two. Under this reading, skipping the file is a PASS.
- Grade: the facts in the claim are all correct (PASS). The decision is PASS under B and FAIL under A. I do not resolve it. Note that the unit applied Reading A to c7-probe and Reading B to open-a1 (Defect 2).

Observation, not a defect of this unit: three unedited reports in this filing already carry S13 as a whole line twice:
- 2026-11-13-o3-cure3-manager.md at :25 and :50
- 2026-11-13-o4-parity-worker2.md at :264 and :314
- 2026-11-13-o4-parity-worker3.md at :251 and :296

Under the "once" wording of S13 these are pre-existing doubles. The unit makes no claim about them.

### C3: temp index. PASS, except one sub-claim that is false as worded (Defect 1)
Hook line (`grep -n 'shasum -a 256'` on the hook):
```
678:HASH=$(git_idx diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256 | awk '{print $1}')
```
`git_idx` (hook :423-427) is `(cd "$ROOT" && GIT_INDEX_FILE="$IDX" git "$@")`, so it adds no extra git flags. That makes the command used in s2.sh equivalent.
```
canonical=716f826d8eadc2c72a4de8bc2bf16ca7d4091efa71305f31c8080c2eecba75a0 expect=716f826d8eadc2c72a4de8bc2bf16ca7d4091efa71305f31c8080c2eecba75a0 match=Y
name-status lines=      34 status-letters:   33 A    1 M 
name-status diff vs expected (empty = equal):
--- blobs vs working tree
BLOB_DIFF M MANIFEST.md staged=100644 313f56cf05e0b0b9c46fd141e18707d607bbe661 wt=ba7a7dc1cb49ae7fa2535b3639ada0001248048c raw=ba7a7dc1cb49ae7fa2535b3639ada0001248048c
blob mismatches=1
removed lines=34 (incl ---); removed excl headers=0
added lines=    7466
name-token hits (ci) in added: 0  in whole diff incl headers: 0
email hits in added: 0
name-token hits in staged paths: 0
write-tree(copy)=ef27c00cc5156340efa514be6641494672329128 expect=ef27c00cc5156340efa514be6641494672329128 match=Y
idx unchanged by my reads: Y
idx entries=     572 HEAD entries=     539
```
Results against the claim:
- Canonical hash: matches.
- Name-status: exactly the 33 A paths plus `M MANIFEST.md`.
- Staged blobs: all 33 A blobs equal `git hash-object` of the working-tree file, both with filters and with `--no-filters`. All are mode 100644.
- Removed lines: 0. The 34 `-` lines are the 34 `--- ` file headers, one per file.
- Name-token and email hits in added lines: 0.
- write-tree: matches.
- Entry count: 572 = 539 + 33.

The exception: the claim says "Every staged blob equals its working-tree file". That is false for MANIFEST.md (staged 313f56c, working tree ba7a7dc). The staged version is HEAD plus rows.txt (C4), and the working tree has other uncommitted MANIFEST edits.

### C4: staged MANIFEST.md. PASS
Runner: `bash /tmp/praxis-cna-w2/s3.sh` (the hook blocked the first heredoc version, so I wrote the script with the Write tool).
```
HEAD MANIFEST last byte:  \n   rows.txt last byte:  \n
cmp staged vs HEAD+rows: IDENTICAL
--- field counts (awk -F'|' NF) last 20 HEAD rows:
  20 7
--- field counts rows.txt:
  33 7
--- first/last char of each row:
  33 ||
--- HEAD last-20 first/last char:
  20 ||
--- HEAD last-20 field-2 first 3 chars:
  20  /d
--- rows.txt field-2 first 3 chars:
  29  /d
   4  /v
--- rows 16,17 vs working-tree MANIFEST.md
row 16 path=2026-11-12-o3-block1-scope-correction-1-worker1.md wt_lines_with_path=1 exact_line_in_wt=1
row 17 path=2026-11-12-o3-block1-scope-correction-2-worker2.md wt_lines_with_path=1 exact_line_in_wt=1
--- all 33 rows: exactline/pathlines in working-tree MANIFEST.md
1:0/0 2:0/0 3:0/0 4:0/0 5:0/0 6:0/0 7:0/0 8:0/0 9:0/0 10:0/0 11:0/0 12:0/0 13:0/0 14:0/0 15:0/0 16:1/1 17:1/1 18:0/0 19:0/0 20:0/0 21:0/0 22:0/0 23:0/0 24:0/0 25:0/0 26:0/0 27:0/0 28:0/0 29:0/0 30:0/0 31:0/0 32:0/0 33:0/0 
--- rows.txt paths already in HEAD MANIFEST:        0
--- duplicate rows in rows.txt: 0
--- CR bytes in rows.txt: 0  tabs: 0
```
Path order: field 2 of each row, stripped of spaces and backticks, equals in.txt line for line except for a leading `/`. The s3.sh `diff` output shows every line as `/docs/...` or `/vm/...` against `docs/...` or `vm/...`, with nothing else different. The leading `/` is the house style: all 20 of the last HEAD rows start field 2 with ` /d`. So the paths match in order.

Observation: the working-tree MANIFEST.md contains rows 16 and 17 and none of the other 31. If someone later stages the working-tree MANIFEST.md as it stands, the 31 rows this unit adds would be removed. This is not a defect of the claim.

### C5: real index unchanged. PASS
```
real ls-files-s sha=336b5c3f279a7b79f070f5985c14408dff2d67d3caefa034b5713af9a572b763 match=Y
real cached name-only count=       1
```

### C6: anything else. FAIL (Defect 2)
s1.sh `=== C6` printed no MISSING, TRACKED_AT_HEAD, IN_REAL_INDEX or OTHER_DIR line for any of the 33 paths:
```
=== C6
vm/replies count: 4  reports count: 29
append non-reports: 0
--- appended vm/replies? 0
```
Other checks from s1.sh, both clean:
```
--- duplicates in in.txt:        0
--- append.txt subset of in.txt? missing:        0
```
So there are no path typos, no IN file tracked at HEAD or present in the real index, no duplicate paths, and no docs/reports file that needed an append but was left out (C2 shows that every non-appended report except open-a1 ends on S13). One problem was found: Defect 2.

## Defects
1. The C3 sub-claim "Every staged blob equals its working-tree file" is false as worded for MANIFEST.md. The staged blob is 313f56cf05e0b0b9c46fd141e18707d607bbe661 and the working-tree blob is ba7a7dc1cb49ae7fa2535b3639ada0001248048c. The difference is by design: the staged file is HEAD plus rows.txt, which C4 confirms. The claim should be limited to the 33 A paths. Severity: wording only.
2. docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md:3 and :93. Before the append, the file already carried the S13 sentence once, at :3 (`Standing limitation: Fills are optimistic; ...`). The unit appended the filer's note at :92 and S13 at :93, so the file now carries the sentence twice. That conflicts with rubric S13 "carries, once" (specs/SPEC_RUBRIC.md:145). For open-a1-cure-worker1.md the unit gave "already carries it once" as its reason not to append. For c7-probe it did the opposite. The same rule was applied two ways and the report does not say so. C1 does not catch it, because the claim only says the last standalone line of the pre copy was not S13, which is true (:3 is not standalone and not last). Severity: substantive. It is the same two-readings question as open-a1 and should go up with it.

## Name-token count of this report
Measured twice: first at the end of s3.sh on the skeleton, then on the final file, before this section was edited in. The edit only added this text and the command output below, neither of which contains the token.
```
--- report self-check
name-token count in my report: 0
```
Final file (`/usr/bin/grep -ic -e "$N"`, plus the email pattern and the last line):
```
name-token count: 0
email hits: 0
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
