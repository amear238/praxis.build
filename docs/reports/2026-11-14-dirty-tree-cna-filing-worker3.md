# Dirty-tree CNA filing: worker 3 adversarial check

## Task

Try to break claims 1 to 6 for unit 2026-11-14-dirty-tree-cna-filing: the IN list, the 12 two-line appends, the S13 end state, rows.txt, the temp index /tmp/praxis-cna/idx, and the real index. HEAD 9a18fde (checked with `git rev-parse --short HEAD`, output `9a18fde`).

## Mode

ADVERSARIAL, read-only, cold. The only repo write is this report. The temp index was read only through `GIT_INDEX_FILE=/tmp/praxis-cna/idx` with read-only git commands. My scratch files are under /tmp/praxis-cna-w4/ (check.sh, ns.txt, A.txt, in.s, man.exp, man.stg, d.txt, rowp.txt).

## Process log

1. Read .claude/hooks/gate-commit.sh :678 (the canonical HASH line) and git_idx() at :423-429.
2. Ran /tmp/praxis-cna-w4/check.sh. It covers claims 1, 2, 3, 5, 6 and the structural part of 4.
3. Printed rows 11 and 32 in full. Checked each fact in them against the two files and against DECISION_LOG.md, using grep only on DECISION_LOG.md.

The canonical command at gate-commit.sh :678, as read:
```
HASH=$(git_idx diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256 | awk '{print $1}')
```
In check.sh I ran it as `GIT_INDEX_FILE=/tmp/praxis-cna/idx git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256 | awk '{print $1}'` from the repo root.

## Claim 1: PASS

```
in32 lines:       32 unique:       32
evidence in in32: 0
evidence in idx:        0
evidence in idx diff: 0
evidence sha now:      e8e095cf5df092c4c595f316bdbef7455b5169281a03d070f725d2114f322479
evidence sha recorded: e8e095cf5df092c4c595f316bdbef7455b5169281a03d070f725d2114f322479
```
`git status --porcelain` on the -evidence.md path gives `?? docs/reports/2026-11-12-o3-block1-scope-evidence.md`. It is untracked and not in HEAD (`EV_NOT_IN_HEAD`).

## Claim 2: PASS

For each file, the check computed sha256(pre copy + note line + S13 line, each ending in LF) and compared it with the current file. It also checked that the first N bytes of the current file match the pre copy byte for byte (`headeq`) and that the bytes after them are exactly the two lines (`tail`).
```
append12 count       12 unique       12; all in in32: 12
pre dir files:       12
2026-07-28-session39-agents-dir-write-path.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-08-06-facts-pack.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-08-06-praxis-assessment.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-08-06-subreport-agent-memory.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-08-07-f3-fill-resolution-research-UNGRADED.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-08-29-session53-parallel-handoff.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-10-26-nightly-spec-request-review.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-10-31-voice-handoff-future-row-walkthrough.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-11-01-csv-analyses-fix-manager-record.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-11-01-three-strategy-results-s2-fix-manager-record.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-11-09-c7-probe-fresh-manifest-manager.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=0 preLastNonblank=other
2026-11-13-open-a1-cure-worker1.md preSha=OK cur=pre+2=OK prelastbyte=0a headeq=y tail=OK preS13x=1 preLastNonblank=other
post-sha-2 check:
docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md OK
docs/reports/2026-11-13-open-a1-cure-worker1.md OK
```
In all 12 pre copies, the last non-blank line is not the S13 sentence. So the rule calls for an append in every one of them, and no file got an append it did not need. The two named cases hold:
- c7: `preS13x=0`. The sentence appears only inside :3 (`Standing limitation: Fills are optimistic; ...`). The pre copy has 91 lines and the current file has 93.
- open-a1: `preS13x=1`, with the standalone sentence at :327 and `Result: FAIL` at :328. The pre copy has 328 lines and the current file has 330.

## Claim 3: PASS

```
S13ok lastline=y appended trailNL=0a docs/reports/2026-07-28-session39-agents-dir-write-path.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-08-06-facts-pack.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-08-06-praxis-assessment.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-08-06-subreport-agent-memory.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-08-29-session53-parallel-handoff.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-10-26-nightly-spec-request-review.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-11-01-csv-analyses-fix-manager-record.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md
vm lastline=- shaOK trailNL=0a vm/replies/20261110T214542Z-STATUS.md
vm lastline=- shaOK trailNL=0a vm/replies/20261110T214834Z-self-report.md
vm lastline=- shaOK trailNL=0a vm/replies/20261110T215014Z-STATUS.md
vm lastline=- shaOK trailNL=0a vm/replies/20261110T224920Z-2b-skill-job.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o3-cure3-manager.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o3-cure3-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-parity-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-parity-worker2.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-parity-worker3.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-parity-worker4.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-reduce-manager.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-reduce-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-reduce2-manager.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-reduce2-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-repoint-manager.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-repoint-worker1.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-cure1-manager.md
S13ok lastline=y shaOK trailNL=0a docs/reports/2026-11-13-o4-cure1-worker1.md
S13ok lastline=y appended trailNL=0a docs/reports/2026-11-13-open-a1-cure-worker1.md
```
How to read the columns: `S13ok` means the last non-blank line is exactly the S13 sentence. `lastline=y` means the physical last line is exactly the S13 sentence. `shaOK` means the current sha256 equals the entry in unedited-sha.txt. None of the 4 vm/replies files is in HEAD, so all 4 are added as new files, not modified.

## Claim 4: PASS

```
rows:       32
ROW_ORDER_SAME
evidence named in rows: 0
```
`ROW_ORDER_SAME` means the path column of rows.txt, with the leading `/` removed, matches in32.txt line for line (checked with `diff`).

Row 11 (c7-probe-fresh-manifest-manager), fact by fact:
- `Result: PASS (:91)`: the file has `91:Result: PASS`. PASS.
- S13 inside :3 (not standalone): :3 is `Standing limitation: Fills are optimistic; ...`, and the pre copy has 0 standalone S13 lines. PASS.
- Note and sentence at :92-:93: 93 lines now, 91 before, and the tail bytes are exactly the two lines. PASS.
- "pre- and post-edit line counts and numstat": file :19 and :21 give 323 to 324 lines and numstat `8 0` to `9 0`. PASS.
- "no workers": file :84 says "No adversarial worker was dispatched". PASS.
- "appends one MANIFEST row for the c7-probe-fresh manager report": file :9 says "Append exactly one row ... for /docs/reports/2026-11-09-c7-probe-fresh-manager.md". PASS.
- DECISION_LOG 2026-11-09T19:18:30Z: `wt=1 head=1`. The entry says the report "`docs/reports/2026-11-09-c7-probe-fresh-manifest-manager.md` stays out of this commit and untracked". PASS.
- DECISION_LOG 2026-11-14T09:06:00Z: `wt=1 head=0`. The entry exists in the working tree and is the unit (d) scope entry for `2026-11-14-dirty-tree-cna-filing`. PASS.
- Phase column `2`: not checkable against the file. Not graded.

Row 32 (open-a1-cure-worker1), fact by fact:
- `Result: FAIL (:328)`: the file has `328:Result: FAIL`. PASS.
- S13 standalone at :327, before the Result line: the file has `327:Fills are optimistic; ...`. PASS.
- Note and sentence at :329-:330: 330 lines now, 328 before. PASS.
- Cold, read-only, five-edit cure of D-2026-11-13-B, the MANIFEST row and the manager report: file :5 says "Mode: ADVERSARIAL (cold, read-only). The claim under test: the cure of entry D-2026-11-13-B (DECISIONS.md), the one appended MANIFEST.md row, and the manager report ... (five edits)". PASS.
- Topology OPEN-A1, bead Praxis_build-fgd: present in the file at :31 and :55, inside the quoted manager row. PASS.
- DECISION_LOG 2026-11-13T17:15:15Z: `wt=1 head=0`. The entry says "Out of the commit, on disk: MANIFEST :472–:473 (old open-a1 report rows), the two old open-a1 reports, `-cure-worker1.md`". PASS. One weakness: the entry names the file only by the suffix `-cure-worker1.md`. The context (the OPEN-A1 cure commit) makes the reference unambiguous.
- DECISION_LOG 2026-11-14T09:06:00Z: `wt=1`. PASS.

## Claim 5: PASS

```
hash adbf31b8602a509470677f1c726e48841d00449344d9684c3623e4b723615c30
  32 A
   1 M
A vs in32 diff:
SAME
M	MANIFEST.md
MANIFEST_CMP_OK
HEAD MANIFEST ends NL: 0a
blob mismatches: 0
removed lines: 0 ; '^-' excl ---: 0
name len 4; added-line name hits (i): 0
added-line email hits: 0
```
Notes on this output:
- `MANIFEST_CMP_OK` is `cmp` of (`git show HEAD:MANIFEST.md`; `cat rows.txt`) against `GIT_INDEX_FILE=/tmp/praxis-cna/idx git show :MANIFEST.md`.
- Blob check: for each in32 path, `git rev-parse :<path>` in the temp index equals `git hash-object <path>`.
- The name-token count was case-insensitive (`grep -ci`), which is stricter than required.
- Name-status was taken with `--no-renames`.

## Claim 6: PASS

```
real ls-files: 336b5c3f279a7b79f070f5985c14408dff2d67d3caefa034b5713af9a572b763
real cached count:        1
```

## Defects

No claim fails. Two observations:

1. Artifact hygiene, not a claim failure: /tmp/praxis-cna/unedited-sha.txt has 22 entries. They are the 20 non-appended in32 paths, plus the -evidence.md path, plus `docs/reports/2026-11-13-open-a1-cure-worker1.md` with sha `b6aff505...88db`. That sha is its pre-append hash and equals its pre-sha.txt entry, but the file is in append12.txt and its current hash is `28e0ccce...3432`. Anyone who checks unedited-sha.txt as "every listed file is unchanged" will get a false mismatch on that path. Claim 3 as worded only tests paths not in append12, so it is unaffected.
2. Process breach by this worker, not in this report: one of my diagnostic commands echoed a label made from `${N}` inside a literal string. That printed the private name token once in my tool output (not in this file). Both counts on that line were 0. Disclosed so the manager can judge it.

## Name-token count of this report

Command: `/usr/bin/grep -ci -- "$N" docs/reports/2026-11-14-dirty-tree-cna-filing-worker3.md`, with N loaded as briefed. Output, run after this report was written:
```
count: 0
```

## Result

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
