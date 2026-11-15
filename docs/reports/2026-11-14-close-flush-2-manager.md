# 2026-11-14 close-flush-2: manager report

## Task
Unit `2026-11-14-close-flush-2`, scope DECISION_LOG.md :961 `[2026-11-14T09:51:00Z]` (read in full by grepping its stamp). Build temp index /tmp/praxis-cf2/idx from HEAD bdb63b7: five modified blobs (HANDOFF.md, STATUS.md, DECISION_LOG.md, DISPATCH_LOG.md, MANIFEST.md), each built from `git show HEAD:<file>` plus working-tree additions, and the untracked 2026-11-14 reports that pass the S13 and name screens. Append the new MANIFEST rows to the working-tree MANIFEST.md. No commit; real index untouched. Scripts: /tmp/praxis-cf2/build.sh (build), /tmp/praxis-cf2/check.sh and check2.sh (checks). /tmp/praxis-cf/ was read for its scripts and its 19 draft rows only; its index and blobs were not used.

Rubric criteria addressed (specs/SPEC_RUBRIC.md): S1, S2, S6, S7, S12, S13.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| worker1 | ADVERSARIAL (read-only, cold) | Stopped at its 40-turn limit before it wrote its report. `docs/reports/2026-11-14-close-flush-2-worker1.md` does not exist. Its scratch dir /tmp/praxis-cf2-adv/ has independent rebuilds of all five M blobs, its own expected path list, and its own scanner. I compared those against the idx (pasted below): all five shas match and the path list matches. Checks it did not finish: the truth-check of the MANIFEST rows, its own canonical hash, its real-index check, and its report. The brief allows one adversary only, so I did not dispatch a second. |

## Process log
1. Checked HEAD = bdb63b7. Took the real-index fingerprint before any work: `369ec788...6bec2f`, 1 staged path.
2. Read the scope row :961, the rubric table, the prior flush's scripts, and the structure of the prior manager report. Read the heads, section lists and Result lines of the 8 reports that had no draft row.
3. Found that the working-tree MANIFEST.md is not a HEAD prefix. It first differs at line 307 (an older row layout, `git diff --stat`: 42 insertions, 29 deletions). Its lines :499-:517 are byte-identical to the prior flush's 19 draft rows (/tmp/praxis-cf/manifest-rows.txt). All 19 rows end `filed by unit 2026-11-14-close-flush, DECISION_LOG 2026-11-14T02:09:11Z`. That attribution is no longer true, because that flush was abandoned and this unit files them. So I did not byte-copy them: build.sh rewrites that one suffix to `close-flush-2, DECISION_LOG 2026-11-14T09:51:00Z` and changes nothing else. The 19 report files have the same sha256 prefixes as in the prior flush's final.out, so the descriptive text describes the same bytes. Their row claims that DECISION_LOG rows sit "at :930-:932 in the DECISION_LOG committed by this flush" hold for this blob too (pasted below).
4. Wrote 7 new rows (/tmp/praxis-cf2/new-rows.txt). The 8th report without a draft row fails S13, so it gets no row.
5. Ran build.sh once. Snapshot stamp 2026-11-14T09:53:48Z. Then ran check.sh, check2.sh, the negative tests, and the comparison with the adversary's scratch output. Ran check.sh again at 10:00:51Z. Its output was identical apart from the date.
6. Mistake, disclosed: a `->` in one test command's echo text was parsed as a redirect. It created an untracked file `blocks` (10 bytes, `differs -`) at the repo root. I removed it right away (porcelain count after: 0). It was never staged and never in the idx. I re-ran the comparison correctly (pasted below).

## Verification evidence

### Blob composition proofs (build.sh output, with ledger part counts, report screen and idx build): /tmp/praxis-cf2/build.out
```
$ git rev-parse --short HEAD
bdb63b7
name-token derived: length=4
real index BEFORE: ls-files fp=369ec7886a898370f0d1a955a6f18d1d84414d9dbe28965e779eb112fe6bec2f staged=1
snapshot stamp: 2026-11-14T09:53:48Z
  HANDOFF.md WT=2249 HEAD=2141
  STATUS.md WT=714 HEAD=685
  DECISION_LOG.md WT=961 HEAD=921
  DISPATCH_LOG.md WT=2917 HEAD=2769
  MANIFEST.md WT=517 HEAD=504
## HANDOFF
WT :82 = ## Resume card — 2026-11-13 run (from 17:00Z, timer pro
line 82 prefix OK
parked 17:00Z card = WT :82-:108 (27 lines); next card WT :109 = ## Resume card — 2026-11-13 run (from 13:01Z, timer pro
$ cmp <(sed -n '109,$p' WT) <(git show HEAD:HANDOFF.md)
HANDOFF WT :109-end == HEAD:HANDOFF.md (cmp exit 0)
## STATUS
WT :24 = ## 2026-11-13 (timer run 17:00Z) — short stat
line 24 prefix OK
parked 17:00Z block = WT :24-:31 (8 lines); next block WT :32 = ## 2026-11-13 (timer run 13:01Z) — short stat
$ cmp <(sed -n '1,2p;32,$p' WT) <(git show HEAD:STATUS.md)
STATUS WT :1-:2 + :32-end == HEAD:STATUS.md (cmp exit 0)
## DECISION_LOG.md cutoff 2026-11-13T19:40:54Z
HEAD:DECISION_LOG.md (921 lines) is a byte prefix of the WT snapshot (cmp exit 0)
excluded rows=12 first=2026-11-13T13:44:24Z last=2026-11-13T17:43:11Z
excluded stamps: 2026-11-13T13:44:24Z 2026-11-13T17:02:02Z 2026-11-13T17:12:19Z 2026-11-13T17:15:15Z 2026-11-13T17:18:24Z 2026-11-13T17:19:15Z 2026-11-13T17:22:34Z 2026-11-13T17:33:15Z 2026-11-13T17:37:20Z 2026-11-13T17:38:10Z 2026-11-13T17:41:08Z 2026-11-13T17:43:11Z
included rows=28 (WT :934-:961) first=2026-11-13T19:40:54Z last=2026-11-14T09:51:00Z
HEAD 921 + excluded 12 + included 28 = 961 ; WT total 961
parts contiguous, nothing else: OK
blob tail == WT snapshot :934-:961 (cmp exit 0); blob lines=949
## DISPATCH_LOG.md cutoff 2026-11-13T19:40:00Z
HEAD:DISPATCH_LOG.md (2769 lines) is a byte prefix of the WT snapshot (cmp exit 0)
excluded rows=22 first=2026-11-13T13:42:23Z last=2026-11-13T17:42:39Z
excluded stamps: 2026-11-13T13:42:23Z 2026-11-13T13:43:52Z 2026-11-13T17:03:10Z 2026-11-13T17:05:41Z 2026-11-13T17:11:05Z 2026-11-13T17:11:48Z 2026-11-13T17:12:46Z 2026-11-13T17:14:33Z 2026-11-13T17:15:41Z 2026-11-13T17:17:52Z 2026-11-13T17:20:06Z 2026-11-13T17:22:27Z 2026-11-13T17:23:08Z 2026-11-13T17:26:12Z 2026-11-13T17:30:37Z 2026-11-13T17:32:42Z 2026-11-13T17:33:39Z 2026-11-13T17:37:00Z 2026-11-13T17:38:36Z 2026-11-13T17:40:52Z 2026-11-13T17:41:28Z 2026-11-13T17:42:39Z
included rows=126 (WT :2792-:2917) first=2026-11-13T19:41:48Z last=2026-11-14T09:50:40Z
HEAD 2769 + excluded 22 + included 126 = 2917 ; WT total 2917
parts contiguous, nothing else: OK
blob tail == WT snapshot :2792-:2917 (cmp exit 0); blob lines=2895
## reports
candidates: 27 (porcelain codes:  27 ?? )
IN s13x=1 name=0 2026-11-14-close-flush-manager.md
IN s13x=1 name=0 2026-11-14-close-flush-worker1.md
IN s13x=1 name=0 2026-11-14-close-flush-worker2.md
IN s13x=1 name=0 2026-11-14-dirty-tree-cna-filing-manager.md
IN s13x=1 name=0 2026-11-14-dirty-tree-cna-filing-trim-manager.md
OUT s13x=2 name=0 2026-11-14-dirty-tree-cna-filing-worker1.md
IN s13x=1 name=0 2026-11-14-dirty-tree-cna-filing-worker2.md
IN s13x=1 name=0 2026-11-14-dirty-tree-cna-filing-worker3.md
IN s13x=1 name=0 2026-11-14-dirty-tree-sort-manager.md
IN s13x=1 name=0 2026-11-14-dirty-tree-sort-worker4.md
IN s13x=1 name=0 2026-11-14-dirty-tree-sort-worker5.md
IN s13x=1 name=0 2026-11-14-dirty-tree-sort-worker6.md
IN s13x=1 name=0 2026-11-14-dirty-tree-sort-worker7.md
IN s13x=1 name=0 2026-11-14-evening-rulings-manager.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker1.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker2.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker3.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker4.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker5.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker6.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker7.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker8.md
IN s13x=1 name=0 2026-11-14-evening-rulings-worker9.md
IN s13x=1 name=0 2026-11-14-hermes-resume-0400.md
IN s13x=1 name=0 2026-11-14-strategy-review-filing-manager.md
IN s13x=1 name=0 2026-11-14-strategy-review-filing-worker1.md
IN s13x=1 name=0 2026-11-14-strategy-review-filing-worker2.md
IN=26 OUT=1
rows19 suffix-corrected: 19 of 19; old suffix left: 0
rows kept=26
row paths == IN file list (cmp exit 0)
blob HANDOFF.md 743cc42715986a4ba7ab8a51e7bf9451aef41e82
blob STATUS.md 96c9c3408942e7a254af38a757a8f22aa07445a0
blob DECISION_LOG.md 62cd08e54e779a8d62a4321d7cf6def32515b089
blob DISPATCH_LOG.md ccbbd1b3d1e15ea09d882ddc7a456dd4b3b90857
blob MANIFEST.md 5f4bc659b1faec38b055fec586c525675669b61a
WT MANIFEST: appended 7 rows; now 524 lines
real index AFTER: ls-files fp=369ec7886a898370f0d1a955a6f18d1d84414d9dbe28965e779eb112fe6bec2f staged=1
```

### Temp index pastes (name-status, numstat, composition from idx blobs, per-file screen, added-line scans, canonical hash, real index): /tmp/praxis-cf2/check-final.out
```
$ date -u; git rev-parse HEAD
Sat 14 Nov 2026 10:00:51 UTC
bdb63b78175c016b7606153006b97f1adb57971c
real index: fp=369ec7886a898370f0d1a955a6f18d1d84414d9dbe28965e779eb112fe6bec2f staged=1
idx sha256 = 6909ae04450eec3b1808c4bf5a4eede51d35f5c5ab76947373b4da8893368acb
$ GIT_INDEX_FILE=/tmp/praxis-cf2/idx git diff --cached --name-status | cut -c1 | sort | uniq -c
  26 A
   5 M
$ GIT_INDEX_FILE=/tmp/praxis-cf2/idx git diff --cached --name-status
M	DECISION_LOG.md
M	DISPATCH_LOG.md
M	HANDOFF.md
M	MANIFEST.md
M	STATUS.md
A	docs/reports/2026-11-14-close-flush-manager.md
A	docs/reports/2026-11-14-close-flush-worker1.md
A	docs/reports/2026-11-14-close-flush-worker2.md
A	docs/reports/2026-11-14-dirty-tree-cna-filing-manager.md
A	docs/reports/2026-11-14-dirty-tree-cna-filing-trim-manager.md
A	docs/reports/2026-11-14-dirty-tree-cna-filing-worker2.md
A	docs/reports/2026-11-14-dirty-tree-cna-filing-worker3.md
A	docs/reports/2026-11-14-dirty-tree-sort-manager.md
A	docs/reports/2026-11-14-dirty-tree-sort-worker4.md
A	docs/reports/2026-11-14-dirty-tree-sort-worker5.md
A	docs/reports/2026-11-14-dirty-tree-sort-worker6.md
A	docs/reports/2026-11-14-dirty-tree-sort-worker7.md
A	docs/reports/2026-11-14-evening-rulings-manager.md
A	docs/reports/2026-11-14-evening-rulings-worker1.md
A	docs/reports/2026-11-14-evening-rulings-worker2.md
A	docs/reports/2026-11-14-evening-rulings-worker3.md
A	docs/reports/2026-11-14-evening-rulings-worker4.md
A	docs/reports/2026-11-14-evening-rulings-worker5.md
A	docs/reports/2026-11-14-evening-rulings-worker6.md
A	docs/reports/2026-11-14-evening-rulings-worker7.md
A	docs/reports/2026-11-14-evening-rulings-worker8.md
A	docs/reports/2026-11-14-evening-rulings-worker9.md
A	docs/reports/2026-11-14-hermes-resume-0400.md
A	docs/reports/2026-11-14-strategy-review-filing-manager.md
A	docs/reports/2026-11-14-strategy-review-filing-worker1.md
A	docs/reports/2026-11-14-strategy-review-filing-worker2.md
$ GIT_INDEX_FILE=/tmp/praxis-cf2/idx git diff --cached --numstat -- HANDOFF.md STATUS.md DECISION_LOG.md DISPATCH_LOG.md MANIFEST.md
28	0	DECISION_LOG.md
126	0	DISPATCH_LOG.md
81	0	HANDOFF.md
26	0	MANIFEST.md
21	0	STATUS.md
index entries: 594 vs HEAD tree: 568
## blob composition, from the index blobs (git show :<path>)
HANDOFF idx :82-end == HEAD:HANDOFF.md
HANDOFF idx :1-:81 == WT snapshot :1-:81
STATUS idx :1-:2 + :24-end == HEAD:STATUS.md
STATUS idx :3-:23 == WT snapshot :3-:23
DECISION_LOG.md: HEAD (921 lines) is a byte prefix of the idx blob (949 lines); last stamp/row: - [2026-11-14T09:51:00Z]
DISPATCH_LOG.md: HEAD (2769 lines) is a byte prefix of the idx blob (2895 lines); last stamp/row: - [2026-11-14T09:50:40Z]
MANIFEST.md: HEAD (504 lines) is a byte prefix of the idx blob (530 lines); last stamp/row: | /docs/reports/2026-11-
DECISION_LOG idx tail == WT snapshot :934-:961
DISPATCH_LOG idx tail == WT snapshot :2792-:2917
MANIFEST idx tail == rows.txt (26 rows)
DECISION_LOG idx :930-:932 stamps: 2026-11-14T01:25:40Z 2026-11-14T01:27:05Z 2026-11-14T01:28:05Z 
## added files: index blob == working tree, S13 whole-line count, name count
same s13x=1 s13sub=1 name=0 2026-11-14-close-flush-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-close-flush-worker1.md
same s13x=1 s13sub=1 name=0 2026-11-14-close-flush-worker2.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-cna-filing-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-cna-filing-trim-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-cna-filing-worker2.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-cna-filing-worker3.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-sort-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-sort-worker4.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-sort-worker5.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-sort-worker6.md
same s13x=1 s13sub=1 name=0 2026-11-14-dirty-tree-sort-worker7.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker1.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker2.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker3.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker4.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker5.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker6.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker7.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker8.md
same s13x=1 s13sub=1 name=0 2026-11-14-evening-rulings-worker9.md
same s13x=1 s13sub=1 name=0 2026-11-14-hermes-resume-0400.md
same s13x=1 s13sub=1 name=0 2026-11-14-strategy-review-filing-manager.md
same s13x=1 s13sub=1 name=0 2026-11-14-strategy-review-filing-worker1.md
same s13x=1 s13sub=1 name=0 2026-11-14-strategy-review-filing-worker2.md
added files: 26; added list == files.txt: yes
## added-line scans over the whole temp-index diff
added lines: 6379
name-token count (case-insensitive) in added lines: 0
S13 sentence lines in added lines (whole-line, after the +): 30
email-regex hits in added lines: 0
  email hit: DECISION_LOG.md:940
  email hit: DISPATCH_LOG.md:2808
  email hit: DISPATCH_LOG.md:2809
  email hit: DISPATCH_LOG.md:2845
  email hit: DISPATCH_LOG.md:2847
  email hit: DISPATCH_LOG.md:2852
  email hit: DISPATCH_LOG.md:2880
  email hit: docs/reports/2026-11-14-dirty-tree-sort-worker6.md:103
secret-regex hits in added lines: 0
tracked files changed other than the five: 0
DECISIONS.md / .claude/ paths in idx diff: 0
$ (repo root) GIT_INDEX_FILE=/tmp/praxis-cf2/idx git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256
6107b4bcde208af5802b3d0ac5cab2da66cbb8b856e1b17f366f68db75a77c0b  -
real index after: fp=369ec7886a898370f0d1a955a6f18d1d84414d9dbe28965e779eb112fe6bec2f staged=1
WT MANIFEST: 524 lines; last 7 == wt-append.txt: yes; WT 1-517 == snapshot: yes
WT MANIFEST rows per IN path (want 1 each):  26 1 
idx MANIFEST rows per IN path (want 1 each):  26 1 
OUT file row present in idx MANIFEST: 0  in WT MANIFEST: 0
```

### Scanner corroboration with perl and positive controls: /tmp/praxis-cf2/check2.out
```
$ grep --version | head -1
grep (BSD grep, GNU compatible) 2.6.0-FreeBSD
$ type grep
grep is /usr/bin/grep
perl: added lines=6379 name-token=0 email-regex hits=0 secret-regex hits=0
## positive controls for the scanners (synthetic lines, not repo content)
control: name=1 email=1 secret=1 (want 1 1 1)
ugrep on the same control: name=1 email=1 secret=1
## S13 whole-line count per added report, perl (index blobs)
  files with s13 count   26 1
```

### Email false-positive shapes (awk pass; letters to a, digits to 9)
```
DECISION_LOG.md:940 tokens-with- aaaaaaaaa@9a99aaa
DISPATCH_LOG.md:2808 tokens-with- aaaaaa@aaaaaaaaa-aa
DISPATCH_LOG.md:2809 tokens-with- aaaaaa@aaaaaaaaa-aa
DISPATCH_LOG.md:2845 tokens-with- aaaaaa@aaaaaaaaa-aa
DISPATCH_LOG.md:2847 tokens-with- aaaaaa@aaaaaaaaa-aa
DISPATCH_LOG.md:2852 tokens-with- aaaaaa@aaaaaaaaa-aa
DISPATCH_LOG.md:2880 tokens-with- aaaaaa@aaaaaaaaa-aa
docs/reports/2026-11-14-dirty-tree-sort-worker6.md:103 tokens-with- aaaaaaaaa@aa9aaa9".
```

### Negative tests, adversary-scratch comparison, carried-row and new-row citation checks: /tmp/praxis-cf2/neg.out
```
## negative tests
off-by-one HANDOFF composition (blob :81-end vs HEAD): cmp exit 1, mismatch caught
DECISION_LOG rebuilt WITH the 12 parked rows: 7dd2a6ebda231d7bace24eb57d4be4f61fa71793; idx sha 62cd08e54e779a8d62a4321d7cf6def32515b089; equal=no
S13 screen trip: OUT file 2026-11-14-dirty-tree-cna-filing-worker1.md, whole-line count 2 at lines 188 193 
## adversary scratch (/tmp/praxis-cf2-adv) vs idx
HANDOFF.md adv=743cc42715986a4ba7ab8a51e7bf9451aef41e82 idx=743cc42715986a4ba7ab8a51e7bf9451aef41e82 match=yes
STATUS.md adv=96c9c3408942e7a254af38a757a8f22aa07445a0 idx=96c9c3408942e7a254af38a757a8f22aa07445a0 match=yes
DECISION_LOG.md adv=62cd08e54e779a8d62a4321d7cf6def32515b089 idx=62cd08e54e779a8d62a4321d7cf6def32515b089 match=yes
DISPATCH_LOG.md adv=ccbbd1b3d1e15ea09d882ddc7a456dd4b3b90857 idx=ccbbd1b3d1e15ea09d882ddc7a456dd4b3b90857 match=yes
MANIFEST.md adv=5f4bc659b1faec38b055fec586c525675669b61a idx=5f4bc659b1faec38b055fec586c525675669b61a match=yes
adv expected paths (slash stripped, sorted) == my IN list: yes; count=26; cna-filing-worker1 in adv list: 0
adv added-line extract lines=6379 mine=6379
adv scan.pl on its extract: name=0 email=0 cred=0
## carried 19 rows: report bytes unchanged since prior flush (sha256 prefix, prior final.out vs now)
  19 same
rows19 vs prior drafts: lines differing only in suffix: all 19 (no other byte differs)
## cited line numbers in the 7 new rows
close-flush-manager :167=[Result: PASS] :168 is-last-line=yes s13-at-:168=1
close-flush-worker1 :85=[Result: PASS] :88 is-last-line=yes s13-at-:88=1
close-flush-worker2 :338=[Result: PASS] :341 is-last-line=yes s13-at-:341=1
dirty-tree-cna-filing-manager :341=[Result: BLOCKED] :343 is-last-line=yes s13-at-:343=1
dirty-tree-cna-filing-trim-manager :243=[Result: PASS] :245 is-last-line=yes s13-at-:245=1
dirty-tree-cna-filing-worker2 :110=[Result: FAIL] :112 is-last-line=yes s13-at-:112=1
dirty-tree-cna-filing-worker3 :173=[Result: PASS] :175 is-last-line=yes s13-at-:175=1
phrases: cna-manager heading 'open-a1 restore (DECISION_LOG :958)'=1; trim '## OUT list (7)'=1; cna-w2 'IN 33, OUT 3'=1; cf-w2 :336 'No BLOCKING'=1
scope row: DECISION_LOG :961, contains 'praxis-cf is abandoned': 1
repo-root stray file check: 0
```

## S13/name/email/secret checks (summary of the pastes above)
- S13: the screen ran on all 27 candidates. 26 have exactly one standalone whole-line copy (`grep -cxF` count 1; an independent perl count over the idx blobs gives "26 1"). One is OUT: `docs/reports/2026-11-14-dirty-tree-cna-filing-worker1.md`, with whole-line count 2 at :188 and :193. It is not in the idx and has no MANIFEST row in either the blob or the working tree. I did not edit it. The other 30 whole-line copies counted in the added lines are the 26 report lines plus 4 inside ledger rows. S13 covers reports and DECISIONS.md, not ledger rows.
- Name token (length 4, derived from the F4 reply-filing file name, never printed): 0 in each of the 26 added files, 0 in the 6379 added lines of the idx diff (grep and perl agree), 1 in the positive control.
- Email regex: 0 hits in the added lines (grep 0, perl 0, adversary scan.pl 0, positive control fires). check.sh's awk pass listed 8 "email hit" locations. These are false positives, because `awk -v` drops the backslash in `\.`. The masked token shapes show none of the 8 has a dotted domain (`aaaaaa@aaaaaaaaa-aa`, `aaaaaaaaa@9a99aaa`, `aaaaaaaaa@aa9aaa9".`). Locations, file and line only: DECISION_LOG.md:940; DISPATCH_LOG.md:2808, :2809, :2845, :2847, :2852, :2880; docs/reports/2026-11-14-dirty-tree-sort-worker6.md:103.
- Secrets: 0 hits in the added lines (grep 0, perl 0, adversary scan.pl 0, positive control fires).

## Adversary result
INCOMPLETE. worker1 stopped at its turn limit with no report. Its partial hand-back was one line ("Now MANIFEST. The working tree is not a HEAD prefix; investigate."). From its scratch artifacts, compared against the idx (pasted above):
- All five independently rebuilt blobs (HANDOFF, STATUS, DECISION_LOG, DISPATCH_LOG, MANIFEST) match the idx shas.
- Its expected added-path list (26) equals the idx A list and my IN list. It also excluded the cna-filing worker1 report on its own.
- Its added-line extraction has 6379 lines, the same as mine, and its scanner gives name=0 email=0 cred=0.
Not done by any independent party: the truth-check of the 26 MANIFEST row descriptions against their files, and an independent canonical hash. I checked the cited Result and S13 line numbers and four content phrases of the 7 new rows mechanically (pasted above), but I wrote those rows, and the 19 carried rows were truth-checked only by the prior flush's adversary (11 of 19, on the same file bytes). That is self-evidence for the 7 rows, so I do not claim the rows are adversarially verified (S2).

## Files staged
Real index: unchanged. Fingerprint `369ec7886a898370f0d1a955a6f18d1d84414d9dbe28965e779eb112fe6bec2f` and 1 staged path, before and after.
Temp index /tmp/praxis-cf2/idx (sha256 `6909ae04...68acb`, left for the master): 31 paths, 26 A + 5 M, listed in the name-status paste. Canonical hash `6107b4bcde208af5802b3d0ac5cab2da66cbb8b856e1b17f366f68db75a77c0b`.
Working tree: MANIFEST.md has 7 rows appended at :518-:524 (the close-flush and dirty-tree-cna-filing reports other than the excluded worker1). No other tracked file was edited by this unit. This report is outside the idx, as expected.

## Decisions taken for the master
1. 26 A, not 27. `docs/reports/2026-11-14-dirty-tree-cna-filing-worker1.md` is OUT under the brief's rule (S13 whole-line count 2). Add it to the HANDOFF OUT list.
2. The 19 carried MANIFEST rows go into the blob with their filer suffix corrected (unit close-flush-2, DECISION_LOG 09:51:00Z). They are not byte-copies, because the old suffix named the abandoned unit.
3. The working-tree MANIFEST.md is still divergent. It is not a HEAD prefix (it first differs at :307), and its :499-:517 rows keep the old `close-flush, 02:09:11Z` suffix, because only appends were allowed. After a commit of this idx, the working-tree MANIFEST.md will still differ from HEAD. Reconciling it (for example, restoring it from the new HEAD) is the master's call.
4. Rows written after the 09:53:48Z snapshot (for example DISPATCH_LOG 09:55:35Z, and any rows this unit's spawns or the master add) stay for the next flush, as the scope row says.
5. Result is BLOCKED, not PASS. Stress-test step 4 (an independent adversary on the artifact) did not finish, and the brief caps adversaries at one. Options for the master: let praxis-auditor's grade cover the row truth-check and the hash, or authorise one more read-only adversary limited to check B (row truth) and check E (canonical hash).

## S6 cross-block check
This unit makes no deviation from the plan. It files ledger rows and reports only; no code, config, hook, spec or DECISIONS.md change is in the idx (the paste above shows 0 DECISIONS.md or .claude/ paths, and 0 tracked files changed other than the five). The exclusion of one report and the suffix correction on 19 MANIFEST rows touch only the MANIFEST registry and the HANDOFF OUT list, both docs-only. No other block's spec is touched. S12: this idx is the flushing counterpart for this session's ledger rows up to the snapshot; rows after the snapshot are carried by the next flush.

Result: BLOCKED
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
