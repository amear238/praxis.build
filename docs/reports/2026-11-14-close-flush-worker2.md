# Unit 2026-11-14-close-flush, worker 2: adversarial check of temp index /tmp/praxis-cf/idx

## Task
Try to refute the claim that temp index /tmp/praxis-cf/idx is exactly correct against the scope ruling (DECISION_LOG 2026-11-14T02:08:10Z and 02:09:11Z): base HEAD 9a18fde, 19 A + 5 M, the HANDOFF/STATUS/DECISION_LOG/DISPATCH_LOG/MANIFEST blob recipes, the 19 A files identical to the working tree, S13 and de-identification on every added file, and truthful MANIFEST rows. Fix nothing.

## Mode
ADVERSARIAL (read-only). Every blob was rebuilt independently under /tmp/praxis-cf/adv/ from `git show HEAD:<file>` and the working tree, then compared by `git hash-object` against `GIT_INDEX_FILE=/tmp/praxis-cf/idx git ls-files -s`. The real index was not touched. This report is the only repo file written.

Elision note: two pasted outputs in check 2 (HANDOFF line 40 and STATUS line 13) printed the closing line. Each copy is replaced with a bracketed marker so the line occurs once. Nothing else in the pasted output was changed.

## Checks

### 1. name-status and numstat of the temp index against HEAD
```
$ git rev-parse --short HEAD
9a18fde
== name-status
M	DECISION_LOG.md
M	DISPATCH_LOG.md
M	HANDOFF.md
M	MANIFEST.md
M	STATUS.md
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
== numstat
20	0	DECISION_LOG.md
106	0	DISPATCH_LOG.md
41	0	HANDOFF.md
19	0	MANIFEST.md
12	0	STATUS.md
330	0	docs/reports/2026-11-14-dirty-tree-sort-manager.md
380	0	docs/reports/2026-11-14-dirty-tree-sort-worker4.md
432	0	docs/reports/2026-11-14-dirty-tree-sort-worker5.md
193	0	docs/reports/2026-11-14-dirty-tree-sort-worker6.md
335	0	docs/reports/2026-11-14-dirty-tree-sort-worker7.md
95	0	docs/reports/2026-11-14-evening-rulings-manager.md
201	0	docs/reports/2026-11-14-evening-rulings-worker1.md
114	0	docs/reports/2026-11-14-evening-rulings-worker2.md
194	0	docs/reports/2026-11-14-evening-rulings-worker3.md
663	0	docs/reports/2026-11-14-evening-rulings-worker4.md
595	0	docs/reports/2026-11-14-evening-rulings-worker5.md
158	0	docs/reports/2026-11-14-evening-rulings-worker6.md
217	0	docs/reports/2026-11-14-evening-rulings-worker7.md
60	0	docs/reports/2026-11-14-evening-rulings-worker8.md
113	0	docs/reports/2026-11-14-evening-rulings-worker9.md
99	0	docs/reports/2026-11-14-hermes-resume-0400.md
196	0	docs/reports/2026-11-14-strategy-review-filing-manager.md
101	0	docs/reports/2026-11-14-strategy-review-filing-worker1.md
149	0	docs/reports/2026-11-14-strategy-review-filing-worker2.md
== count
      24
  19 A
   5 M
```
DECISIONS.md is not in the diff. Index integrity:
```
== index entries / HEAD tree entries
     558
     539
== nonzero stages
       0
== skip-worktree/assume-unchanged/ita flags
 558 H
== A paths == files.txt (set)
equal
== A paths untracked in real index
checked
== idx verify   (temp-index DECISIONS.md blob, then HEAD:DECISIONS.md)
b11ecfd9caa8bfe40a1fc567878f9b33dc2d81b7
b11ecfd9caa8bfe40a1fc567878f9b33dc2d81b7
```
539 + 19 = 558. No conflict stages, no skip-worktree or intent-to-add entries. None of the 19 paths is tracked in the real index.

### 2. Independent rebuilds and hash compare

HANDOFF and STATUS (recipes: wt :1-:41 + HEAD; HEAD :1-:2 + wt :3-:14 + HEAD :3-end):
```
HANDOFF.md mine=2351febb3e244a9b5095b9d126a27affaa84f4d7 idx=2351febb3e244a9b5095b9d126a27affaa84f4d7
STATUS.md mine=2cd57b4fa95671848551df2069302ad61b98e641 idx=2cd57b4fa95671848551df2069302ad61b98e641
== HANDOFF wt line 40-43 (first 150 chars)
[closing-line text elided by worker 2 so it occurs once]

## Resume card — 2026-11-13 run (from 17:00Z, timer prompt) — `main` = `origin/main` = `661e073` plus this close flush; topology OPEN-A1 LANDED (`9bf6

== wt HANDOFF structure: does wt tail after parked card equal HEAD?
    2209
    2141
wt tail == HEAD
parked lines = 27
== STATUS wt 1-2 vs HEAD 1-2
same
[closing-line text elided by worker 2 so it occurs once]

## 2026-11-13 (timer run 17:00Z) — short status by praxis-master

S head=     685 wt=     705
wt STATUS tail == HEAD 3-end
parked status lines=8
== does idx HANDOFF contain wt line 42?
0
head has it:
0
```
The working-tree HANDOFF is card (41) + parked card (27) + HEAD; STATUS is HEAD :1-:2 + block (12) + parked block (8) + HEAD :3-end. The parked card and block are not in the blobs.

Ledgers (working tree snapshotted to /tmp/praxis-cf/adv at check time):
```
######## DECISION_LOG.md threshold 2026-11-13T19:40:54Z
head=     921 wt=     953 extra=32
wt prefix == HEAD
extra lines not starting '- [':
0
extra lines w/o stamp pattern:
0
keep=      20 drop=      12
drop stamps:
- [2026-11-13T13:44:24Z]  - [2026-11-13T17:02:02Z]  - [2026-11-13T17:12:19Z]  - [2026-11-13T17:15:15Z]  - [2026-11-13T17:18:24Z]  - [2026-11-13T17:19:15Z]  - [2026-11-13T17:22:34Z]  - [2026-11-13T17:33:15Z]  - [2026-11-13T17:37:20Z]  - [2026-11-13T17:38:10Z]  - [2026-11-13T17:41:08Z]  - [2026-11-13T17:43:11Z]
keep in order?
sorted
extra in order?
sorted
keep first/last:
- [2026-11-13T19:40:54Z]
- [2026-11-14T02:09:11Z]
mine-full=30e92f6fccc562b3f6d8136e7b711929c752a2ad idx=30e92f6fccc562b3f6d8136e7b711929c752a2ad
idxblob lines=     941; idx added=20
idx prefix == HEAD
idx added == first       20 keep rows
keep rows past idx: 0
idx last stamp: - [2026-11-14T02:09:11Z]
idxadd non-row lines: 0
dropped rows present in idx: 0
######## DISPATCH_LOG.md threshold 2026-11-13T19:40:00Z
head=    2769 wt=    2898 extra=129
wt prefix == HEAD
extra lines not starting '- [':
0
extra lines w/o stamp pattern:
0
keep=     107 drop=      22
drop stamps:
- [2026-11-13T13:42:23Z]  - [2026-11-13T13:43:52Z]  - [2026-11-13T17:03:10Z]  - [2026-11-13T17:05:41Z]  - [2026-11-13T17:11:05Z]  - [2026-11-13T17:11:48Z]  - [2026-11-13T17:12:46Z]  - [2026-11-13T17:14:33Z]  - [2026-11-13T17:15:41Z]  - [2026-11-13T17:17:52Z]  - [2026-11-13T17:20:06Z]  - [2026-11-13T17:22:27Z]  - [2026-11-13T17:23:08Z]  - [2026-11-13T17:26:12Z]  - [2026-11-13T17:30:37Z]  - [2026-11-13T17:32:42Z]  - [2026-11-13T17:33:39Z]  - [2026-11-13T17:37:00Z]  - [2026-11-13T17:38:36Z]  - [2026-11-13T17:40:52Z]  - [2026-11-13T17:41:28Z]  - [2026-11-13T17:42:39Z]
keep in order?
sorted
extra in order?
sorted
keep first/last:
- [2026-11-13T19:41:48Z]
- [2026-11-14T02:16:21Z]
mine-full=6711dd768db406b24176aea397b7b58187216bec idx=956d18a13ea113c9fd2351b5535fc64551af3332
idxblob lines=    2875; idx added=106
idx prefix == HEAD
idx added == first      106 keep rows
keep rows past idx: 1
- [2026-11-14T02:16:21Z]
idx last stamp: - [2026-11-14T02:15:17Z]
idxadd non-row lines: 0
dropped rows present in idx: 0
```
The DISPATCH_LOG full-rebuild hash differs only because one working-tree row was appended after the build. The 106 rows in the blob are byte-equal to the first 106 qualifying rows (`cmp`). The extra row and the timing:
```
2898:- [2026-11-14T02:16:21Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 9a18fde corr=a4e9f6e45e06cb84f | WHEN: spawn | HOW: awaiting terminal state | STATE: dispatched
== mtime idx vs ledger wt
2026-11-13T21:15:35-0500 /tmp/praxis-cf/idx
2026-11-13T21:16:21-0500 DISPATCH_LOG.md
2026-11-13T21:09:21-0500 DECISION_LOG.md
== wtsnap check (builder's snapshot)
DECISION_LOG snap lines      953
- [2026-11-14T02:09:11Z]
DISPATCH_LOG snap lines     2897
- [2026-11-14T02:15:17Z]
```
The idx was written at 02:15:35Z and the row is stamped 02:16:21Z, so it is a later append, which the ruling allows. Last stamp in the blob: DECISION_LOG 2026-11-14T02:09:11Z (no working-tree row past it); DISPATCH_LOG 2026-11-14T02:15:17Z (one working-tree row past it, 02:16:21Z). The excluded rows are exactly the parked ranges named in the ruling: DECISION_LOG 13:44:24Z to 17:43:11Z (12 rows), DISPATCH_LOG 13:42:23Z, 13:43:52Z and 17:03:10Z to 17:42:39Z (22 rows). Duplicate and byte checks:
```
DL kept rows already in HEAD: 0
DP kept rows already in HEAD: 0
MANIFEST new rows already in HEAD: 0
MANIFEST HEAD rows naming the 19 paths: 0
CR in added lines: 0
```

MANIFEST (recipe: HEAD + 19 rows, the same 19 rows as the working-tree's last 19 lines):
```
== MANIFEST
head=     475 wt=     517
mine=4f6e27becc1acd6db1d871706be63dc2c271d5df idx=4f6e27becc1acd6db1d871706be63dc2c271d5df
idx prefix == HEAD
idx tail == wt last 19
== wt MANIFEST vs HEAD (line-level, counts)
42
0
306a307,314
431a440,445
445a460,465
447a468
450a472,473
475a499,517
== b1815d2 rows NF
  15 7
== new rows NF
  19 7
```
The 42 working-tree additions are 23 interleaved rows by other units plus the 19 appended at the tail (475a499,517). The row paths equal files.txt in order, apart from the leading `/` that the b1815d2 rows also carry. Columns 3-5 are `Report | 3 | <date>` as in b1815d2. Every row ends with the b1815d2 pattern:
```
$ git show b1815d2 -- MANIFEST.md | grep '^+|' | grep -c 'ungraded at time of row |$'
15
$ grep -c 'ungraded at time of row |$' /tmp/praxis-cf/adv/M.wt19
19
```

### 3. S13 and name counts on the 19 files
Columns: same = working-tree hash equals temp-index blob; exact = `grep -cF`; standalone = `grep -cxF`; outfence = standalone copies outside ``` / ~~~ fences; name = `grep -ci "$N"` on the index blob; lastline = last line is the sentence.
```
Nlen=4
file                                                        same exact standalone outfence  name lastline
2026-11-14-strategy-review-filing-manager.md                   Y     1     1     1     0 1
2026-11-14-strategy-review-filing-worker1.md                   Y     1     1     1     0 1
2026-11-14-strategy-review-filing-worker2.md                   Y     1     1     1     0 1
2026-11-14-dirty-tree-sort-manager.md                          Y     1     1     1     0 1
2026-11-14-dirty-tree-sort-worker4.md                          Y     1     1     1     0 1
2026-11-14-dirty-tree-sort-worker5.md                          Y     1     1     1     0 1
2026-11-14-dirty-tree-sort-worker6.md                          Y     1     1     1     0 1
2026-11-14-dirty-tree-sort-worker7.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-manager.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker1.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker2.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker3.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker4.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker5.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker6.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker7.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker8.md                          Y     1     1     1     0 1
2026-11-14-evening-rulings-worker9.md                          Y     1     1     1     0 1
2026-11-14-hermes-resume-0400.md                               Y     1     1     1     0 1
== name count over added lines of full diff
0
== name count over wt MANIFEST 19 rows / HANDOFF 1-41 / STATUS 3-14
0
0
0
== fence balance per file   (prints only files with an odd fence count)
done
== mode bits
  19 100644
```

### 4. MANIFEST row truthfulness (11 of 19 rows checked)
Rows checked: 1 (strategy-review-filing-manager), 2 (strategy-review-filing-worker1), 4 (dirty-tree-sort-manager), 8 (dirty-tree-sort-worker7), 9 (evening-rulings-manager), 12 (evening-rulings-worker3), 13 (evening-rulings-worker4, the longest file), 14 (evening-rulings-worker5, the second longest), 16 (evening-rulings-worker7), 17 (evening-rulings-worker8), 19 (hermes-resume-0400). For each I checked the Mode line, unit, cited stamps, counts and Result line against the file. Evidence excerpts:

- Row 13, worker4 (663 lines). `:4` "(read :51-:55 only)"; `:603-:604` "Reading notes ... the brief's gloss "filing (step 2)" is taken from the brief, UNVERIFIED"; `:28/:84/:92` bd list open/in_progress/blocked; Counts `:650-:655`: "PAUSES: 7", "CARRIES ON: 5", "NOT BUILD: 9", "UNCLEAR: 36 (16 named rows + 20 harness beads)", "Total: 57"; table class column tally: `5 CARRIES ON / 9 NOT BUILD / 6 PAUSES / 1 PAUSES (in part) / 17 UNCLEAR` (16 + one 20-bead row); `:661` "PASS (classification delivered; 36 UNCLEAR beads are routed up for a ruling, not decided here)." All match.
- Row 14, worker5 (595 lines). `:7` "BUILD (read-only research ...). HEAD 9ff8a48."; nine `### Batch` headings (:14 to :550); `:361` quotes "944:- [2026-11-14T01:28:05Z]"; elision `:563` "Four pasted outputs contained it"; Q4 items 1-5 graded OBSERVED / REPORTED BY / OBSERVED absence / OBSERVED absence / OBSERVED; findings F1-F5 (:583-:587); `:592-:593` "## Result: PASS" and "Both questions were answered from the record with file:line citations. Five mismatches are listed above." All match.
- Row 19, hermes-resume-0400 (99 lines). `:2` "Written 2026-11-14T01:34Z ... by praxis-master, for the Hermes agent"; authority 01:25:40Z verbatim and 01:33:55Z; 04:00 ET one-shot cron, `praxis-build-loop` stays paused; step 1 pid 1986, `pgrep -P 1986`, leave-alone list, git-lock check; step 2 three-unit table and the "landed only if its commit is in `git log` AND a DECISION_LOG row says `COMMITTED <sha>`" test; step 4 reporter, first-run $4.68 Telegram, stop at third contender; gap 1 ends "(UNVERIFIED):", gaps 2-4 as listed; `grep -ci '^## Result\|Result:'` = 0; S13 at :99 = last line. All match.
- Row 1, strategy-review-filing-manager. Workers table `:15-:18` (worker1/worker2 BUILD PASS 8 and 7 rows; worker3/worker4 NOT DISPATCHED, "Concurrent subagent limit reached ... Do not retry."); negative test `:60-:65`; "WT: 498 lines; blob: 475 lines"; 15 A / 1 M; fingerprint unchanged; nine spot-check bullets `:168-:176`; S6 not applicable `:183`; `:194` "Result: BLOCKED: step E not run." All match.
- Row 2, strategy-review-filing-worker1. `:7` "BUILD."; criteria S1/S2 "as quoted in the brief"; "2518 total"; NF=7; `:99` "PASS. 8 rows drafted ... Name counts are 0 and 0." All match.
- Row 4, dirty-tree-sort-manager. 18 T rows, 28 U rows, 1 X row (counted); `:61-:64` CLEAR-FILE 0, CNA 36 + 4 rows, 116 in scope; workers `:79-:85` (W1-W3 cap, W4-W6 PASS, W7 "1 refuted, 5 partly, 11 confirmed"); four hook hazards `:95-:99`; `:221` "126 are zero and 19 are non-zero"; five S6 hazards; six questions `:304-:310`; `:328` "Result: PASS". All match.
- Row 8, dirty-tree-sort-worker7. Verdict column: C10 "REFUTED (name count), rest PARTLY"; PARTLY C3, C5, C8, C14, C16; the rest CONFIRMED; three cross-cutting findings `:34-:37`; two questions `:39-:41`; E1-E17 + shared-mtime + name count sections; process log `:50` two hook blocks; `:334` "Result: PASS". All match.
- Row 9, evening-rulings-manager. Filer's note "Apart from this note and the title line, the content is the manager's. The master edited no figure, pointer or result in it."; workers table as described; three self-corrected citations; five record-level findings; temp index `M DECISIONS.md` only; `:5` "Result: BLOCKED: manager report file ... not written (tool-refused) ...". All match.
- Row 12, evening-rulings-worker3. `:7` "ADVERSARIAL"; criteria S1, S2, S4, S5, S6, S8, S13 + items 1-8; defects 1 BLOCKING + 5 MINOR as summarised; `:31` "25 lines across 9 files"; per-item 1, 2, 4, 6, 7 PASS and 3, 5, 8 FAIL; `:192` "Result: FAIL". All match.
- Row 16, evening-rulings-worker7. Criteria `:10`; per-item table prior 1-6 and a-f all PASS, d "PASS (with MINOR)"; defects 1-7 MINOR, defect 7 precondition; out-of-scope line-2280 note; `:206` "UNVERIFIED: the bead lists and counts"; canonical hash section; `:214-:215` Result PASS line quoted exactly. All match.
- Row 17, evening-rulings-worker8. Defects 1 BLOCKING (HEAD moved), 2-4 MINOR, 5 disclosed `git write-tree` breach ("rewrote the index file ... The entries did not change"); per-item results as described; `:57-:58` "## Result: FAIL" and the quoted line. All match.

No mismatch found in a factual claim. No row calls a file PASS or graded where the file says otherwise: each row's Result phrase was compared with the file's Result line (rows 1 and 9 BLOCKED, rows 12 and 17 FAIL, row 19 no Result line, the rest PASS), and all 19 rows end "ungraded at time of row".
```
== Result lines per file
strategy-review-filing-manager :: 194:Result: BLOCKED: step E not run. ...
strategy-review-filing-worker1 :: 98:## Result
strategy-review-filing-worker2 :: 147:Result: PASS
dirty-tree-sort-manager :: 328:Result: PASS
dirty-tree-sort-worker4 :: 378:Result: PASS
dirty-tree-sort-worker5 :: ... 430:Result: PASS
dirty-tree-sort-worker6 :: 191:Result: PASS (scope completed; 4 files sorted into groups)
dirty-tree-sort-worker7 :: 334:Result: PASS
evening-rulings-manager :: 5:Result: BLOCKED: manager report file ...
evening-rulings-worker1 :: 199:Result: PASS
evening-rulings-worker2 :: 111:## Result
evening-rulings-worker3 :: 192:Result: FAIL
evening-rulings-worker4 :: 660:## Result
evening-rulings-worker5 :: 592:## Result: PASS
evening-rulings-worker6 :: 155:## Result
evening-rulings-worker7 :: 214:## Result: PASS
evening-rulings-worker8 :: 57:## Result: FAIL
evening-rulings-worker9 :: 111:Result: PASS
hermes-resume-0400 ::
```

Line-number drift in the committed DECISION_LOG (see Defect 1):
```
== wt DL 942-944 stamps
- [2026-11-14T01:25:40Z]
- [2026-11-14T01:27:05Z]
- [2026-11-14T01:28:05Z]
== those stamps in idx blob
2026-11-14T01:25:40Z idx-line=930
2026-11-14T01:27:05Z idx-line=931
2026-11-14T01:28:05Z idx-line=932
2026-11-13T19:40:54Z idx-line=922
     941
== rows citing :94x line numbers
9 10 12 14 16 18
```

### 5. Canonical hash
```
$ GIT_INDEX_FILE=/tmp/praxis-cf/idx git -C /Volumes/Sensidine/Praxis.build diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | shasum -a 256
ff253813b7b9986bb284977ff3279ba21d70a91c01d8ebc6e0f04795f00d909a  -
```

### 6. Real index
```
== real index count
       1
```
(Run at the start and again after all checks; both gave 1.)

## Defects
1. MINOR (S1 citation, not against the ruling's recipe). Six MANIFEST rows (9, 10, 12, 14, 16, 18) repeat the files' working-tree line numbers DECISION_LOG :942-:944. In the committed DECISION_LOG blob (941 lines) those rows are at :930-:932, so :942-:944 point past the end of the file (evidence above). Rows 10, 14 and 18 also give the stamps. Rows 9, 12 and 16 give line numbers only, though each says honestly that the file cites by line number. The rows are true about the files. They cannot be followed in the committed ledger without the stamps 01:25:40Z, 01:27:05Z and 01:28:05Z. The 02:08:10Z ruling already carries the same drift for D/E as an ungraded note.
2. MINOR (observation on the master's card, which the recipe requires byte-for-byte). HANDOFF.md :3, in the blob, says "The parked 17:00Z card below (bead `gfx`) is NOT committed by this flush." In the committed HANDOFF no such card follows: HEAD's HANDOFF follows the card. The sentence is true (the card is not committed), but "below" only makes sense in the working copy. STATUS :9 refers to "parked `ckh`, `diq` and `gfx`" by bead, which does not drift.

No BLOCKING defect found. Cases tried and holding: base and path set (24 = 19 A + 5 M, DECISIONS.md absent, index entry count 558 = 539 + 19, no stage/flag anomalies); all five M blobs rebuilt independently and hash-equal (DISPATCH_LOG equal over the 106 qualifying rows that existed at build time); ledger additions are single-line `- [` rows with full-second stamps, in order, with no duplicate of a HEAD row and no parked row; parked HANDOFF card (27 lines) and STATUS block (8 lines) absent; 19 A blobs equal the working tree, mode 100644; S13 standalone outside fences = 1 and last line in every file; name count 0 in every added file, in the diff's added lines, in the 19 rows, the card and the block; row format equals b1815d2 (NF=7, `Report | 3 | date`, same ending); 11 rows checked for truthfulness with no factual mismatch.

## Result: PASS
PASS with 2 MINOR defects and no BLOCKING defect. The claim that /tmp/praxis-cf/idx is exactly correct against the 02:08:10Z/02:09:11Z ruling held under every check above.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
