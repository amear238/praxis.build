# 2026-11-14 — Unit 2026-11-14-dirty-tree-sort — worker 5 report

## Task
Classify the 31 untracked reports dated 2026-11-12 and 2026-11-13 listed in the scratchpad file g5.txt (groups: O3 block1-scope, R6 engine-entry, O4, OPEN-A1, OPEN-A2). Read-only. For each: owner, ledger rows, bead, audit mints, commit status, Result line, name count, class.

## Mode
BUILD (read-only research).

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S7, S8 as restated in the unit preamble; classes CLEAR-FILE / CLEAR-BUT-NEEDS-AUDIT / UNCLEAR.

## Process log
1. Read preamble and g5.txt (31 paths). Read AUDIT_LOG.md :100-:155 with the Read tool.
2. Per-file name count, tracked state, mtime, porcelain status (one loop).
3. Result lines per file; report lists of the unit commits cae83dc, 4ffce95, 9bf653a, 661e073.
4. Ledger greps per slug (DECISION_LOG / DISPATCH_LOG / AUDIT_LOG), bead show.

## Verification evidence

### E1. Name count, tracked state, mtime (local time, zone -0500), status

```
$ date +%z
-0500
$ while read f; do printf '%s | %s | %s | %s\n' "$(grep -ci "$N" "$f")" "$(git ls-files -- "$f" | wc -l | tr -d ' ')" "$(stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' "$f")" "$f"; done < g5.txt | sed "s/$N/[rep]/Ig"
== count | tracked? | mtime | path
0 | 0 | 2026-11-12T12:59:17 | docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
0 | 0 | 2026-11-12T12:55:36 | docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
0 | 0 | 2026-11-12T13:23:11 | docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md
0 | 0 | 2026-11-12T13:19:05 | docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
0 | 0 | 2026-11-12T16:58:18 | docs/reports/2026-11-12-o3-block1-scope-evidence.md
0 | 0 | 2026-11-12T12:57:08 | docs/reports/2026-11-12-o3-block1-scope-manager.md
0 | 0 | 2026-11-12T12:57:08 | docs/reports/2026-11-12-o3-block1-scope-worker1.md
0 | 0 | 2026-11-12T04:43:39 | docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
0 | 0 | 2026-11-12T04:40:08 | docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
0 | 0 | 2026-11-12T04:25:00 | docs/reports/2026-11-12-r6-engine-entry-manager.md
0 | 0 | 2026-11-12T04:14:09 | docs/reports/2026-11-12-r6-engine-entry-worker1.md
0 | 0 | 2026-11-12T04:20:48 | docs/reports/2026-11-12-r6-engine-entry-worker2.md
0 | 0 | 2026-11-13T00:08:37 | docs/reports/2026-11-13-o3-cure3-manager.md
0 | 0 | 2026-11-13T00:07:38 | docs/reports/2026-11-13-o3-cure3-worker1.md
0 | 0 | 2026-11-13T08:23:38 | docs/reports/2026-11-13-o4-cure1-manager.md
0 | 0 | 2026-11-13T08:22:04 | docs/reports/2026-11-13-o4-cure1-worker1.md
0 | 0 | 2026-11-13T00:23:09 | docs/reports/2026-11-13-o4-parity-manager.md
0 | 0 | 2026-11-13T00:38:38 | docs/reports/2026-11-13-o4-parity-worker1.md
0 | 0 | 2026-11-13T00:44:39 | docs/reports/2026-11-13-o4-parity-worker2.md
0 | 0 | 2026-11-13T00:51:53 | docs/reports/2026-11-13-o4-parity-worker3.md
0 | 0 | 2026-11-13T00:58:48 | docs/reports/2026-11-13-o4-parity-worker4.md
0 | 0 | 2026-11-13T01:09:00 | docs/reports/2026-11-13-o4-reduce-manager.md
0 | 0 | 2026-11-13T01:08:16 | docs/reports/2026-11-13-o4-reduce-worker1.md
0 | 0 | 2026-11-13T04:07:52 | docs/reports/2026-11-13-o4-reduce2-manager.md
0 | 0 | 2026-11-13T04:07:08 | docs/reports/2026-11-13-o4-reduce2-worker1.md
0 | 0 | 2026-11-13T08:12:44 | docs/reports/2026-11-13-o4-repoint-manager.md
0 | 0 | 2026-11-13T08:12:00 | docs/reports/2026-11-13-o4-repoint-worker1.md
0 | 0 | 2026-11-13T12:10:52 | docs/reports/2026-11-13-open-a1-cure-worker1.md
0 | 0 | 2026-11-13T08:34:17 | docs/reports/2026-11-13-open-a1-manager.md
0 | 0 | 2026-11-13T08:33:56 | docs/reports/2026-11-13-open-a1-worker1.md
1 | 0 | 2026-11-13T12:30:29 | docs/reports/2026-11-13-open-a2-worker1.md
```
All 31 show `??` in `git status --porcelain` (output captured, every line begins `?? `). Name count matches the manager's measurement: 30 files at 0, open-a2-worker1 at 1 (at line 196, line number only printed).

### E2. Result lines (per file)

```
$ while read f; do echo "## $f"; grep -n '^Result\|^\*\*Result\|^## Result' "$f" | cut -c1-220; done < g5.txt | sed "s/$N/[rep]/Ig"
## docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
620:Result: BLOCKED
## docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
494:Result: FAIL
## docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md
206:Result: FAIL
## docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
350:Result: FAIL
## docs/reports/2026-11-12-o3-block1-scope-evidence.md
1339:## Result
1341:Result: FAIL
## docs/reports/2026-11-12-o3-block1-scope-manager.md
372:Result: PASS
## docs/reports/2026-11-12-o3-block1-scope-worker1.md
335:Result: FAIL
## docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
376:Result: PASS
## docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
409:## Result
411:Result: FAIL
## docs/reports/2026-11-12-r6-engine-entry-manager.md
206:Result of the grade, as recorded in the entry: 1N, 1C, 1F no conflict with #4 or #5; 2A conflicts [...cut by me at 220 chars]
223:Result: PASS
## docs/reports/2026-11-12-r6-engine-entry-worker1.md
370:## Result: FAIL
## docs/reports/2026-11-12-r6-engine-entry-worker2.md
357:## Result: PASS
## docs/reports/2026-11-13-o3-cure3-manager.md
48:Result: PASS
## docs/reports/2026-11-13-o3-cure3-worker1.md
## docs/reports/2026-11-13-o4-cure1-manager.md
57:Result: FAIL
## docs/reports/2026-11-13-o4-cure1-worker1.md
## docs/reports/2026-11-13-o4-parity-manager.md
156:Result: RESULT_LINE
## docs/reports/2026-11-13-o4-parity-worker1.md
## docs/reports/2026-11-13-o4-parity-worker2.md
310:## Result
## docs/reports/2026-11-13-o4-parity-worker3.md
292:## Result
## docs/reports/2026-11-13-o4-parity-worker4.md
290:## Result
## docs/reports/2026-11-13-o4-reduce-manager.md
68:## Result
69:Result: FAIL (adversary worker1 `Grade: FAIL (1 defect)`; the three master-accepted defects are cured by deletion, one check (c) defect remains in Decision 1, outside this unit's edit scope).
## docs/reports/2026-11-13-o4-reduce-worker1.md
317:## Result
## docs/reports/2026-11-13-o4-reduce2-manager.md
58:Result: FAIL
## docs/reports/2026-11-13-o4-reduce2-worker1.md
65:## Result: FAIL (1 defect)
## docs/reports/2026-11-13-o4-repoint-manager.md
64:Result: PASS
## docs/reports/2026-11-13-o4-repoint-worker1.md
245:## Result: PASS
## docs/reports/2026-11-13-open-a1-cure-worker1.md
328:Result: FAIL
## docs/reports/2026-11-13-open-a1-manager.md
76:Result: PASS
## docs/reports/2026-11-13-open-a1-worker1.md
## docs/reports/2026-11-13-open-a2-worker1.md
184:Result: PASS
261:Result: FAIL
```
Files with no matching Result line, follow-up grep (`grep -ni 'result\|grade:\|verdict' | tail -4`, and `sed -n` after `## Result`):
```
## 2026-11-13-o3-cure3-worker1
86:> GRADE: PENDING
133:GRADE: PASS
## 2026-11-13-o4-cure1-worker1
21:89: Result: PASS        <- a quoted line from another file, not this report's own verdict
62:Self-check of this report (run after writing): ... results reported in the return message.
## 2026-11-13-o4-parity-worker1
266:Grade: FAIL (4 defects)
## 2026-11-13-open-a1-worker1
236:## Overall: PASS
## 2026-11-13-o4-parity-worker2 (after :310)  FAIL (4 defects). ... Grade: FAIL (4 defects)
## 2026-11-13-o4-parity-worker3 (after :292)  FAIL (2 defects) ... Grade: FAIL (2 defects)
## 2026-11-13-o4-parity-worker4 (after :290)  FAIL ... Grade: FAIL (3 defects)
## 2026-11-13-o4-reduce-worker1 (after :317)  FAIL
## 2026-11-13-o4-parity-manager :156          Result: RESULT_LINE   (unfilled placeholder)
```
o4-cure1-worker1 has no own verdict line I found (UNVERIFIED what it graded; it says results went to the return message). open-a2-worker1 carries two Result lines, PASS :184 then FAIL :261.

### E3. Unit commits and which reports they carry (commit times are -0500)

```
$ for c in cae83dc 4ffce95 9bf653a 661e073; do git show --stat --format='%h %ci %s' $c | grep -E 'reports|^[0-9a-f]{7}' | cut -c1-160; done
cae83dc 2026-11-13 00:13:58 -0500 decisions: D-2026-11-12-C records that the Block 1 milestone covers ...
4ffce95 2026-11-13 08:28:15 -0500 decisions: D-2026-11-13-A backtest-vs-live breaker parity ...
 docs/reports/2026-11-13-o4-reduce3-manager.md |  91 +++++++++
 docs/reports/2026-11-13-o4-reduce3-worker1.md | 257 ++++++++++++++++++++++++++
9bf653a 2026-11-13 12:18:08 -0500 decisions: D-2026-11-13-B breaker 4 cancel and confirm-flat placement ...
 docs/reports/2026-11-13-open-a1-cure-manager.md | 276 ++++++++++++++++++++++++
661e073 2026-11-13 12:37:11 -0500 decisions: D-2026-11-13-C strategy-level stop before 16:00 ...
 docs/reports/2026-11-13-open-a2-manager.md | 234 +++++++++++++++++++++++++++++
$ git show --stat --format= cae83dc
 DECISIONS.md                                       |  17 +
 MANIFEST.md                                        |   2 +
 .../2026-11-12-o3-block1-scope-evidence-2.md       | 491 +++++++++++++++++++++
 3 files changed, 510 insertions(+)
$ git ls-files docs/reports | grep -E 'o3-|r6-engine|o4-|open-a[12]'
docs/reports/2026-11-12-o3-block1-scope-evidence-2.md
docs/reports/2026-11-13-o4-reduce3-manager.md
docs/reports/2026-11-13-o4-reduce3-worker1.md
docs/reports/2026-11-13-open-a1-cure-manager.md
docs/reports/2026-11-13-open-a2-manager.md
```
In UTC the commits are cae83dc 05:13:58Z, 4ffce95 13:28:15Z, 9bf653a 17:18:08Z, 661e073 17:37:11Z. Each is 14 s or less after an AUDIT_LOG mint (Read tool, AUDIT_LOG.md):
```
147	2026-11-13T05:13:44Z praxis-auditor:ace91b1fb59b1b68a 5ef19c8d0cd0fa894b88e0123e57f59ffb656326bb44c508e980d29c1afcf5ba PASS index=/private/tmp/idx-o3
150	2026-11-13T13:28:02Z praxis-auditor:a8825e4c44e7ddd02 f20576358918d725bff5f08ff7ab9ee0f6749eeeeab97ad9f0ee533676fcfe81 PASS index=/private/tmp/idx-o4b
152	2026-11-13T17:17:52Z praxis-auditor:a054a91f88cc970b0 1f25eaec35646b832825a57f5588ddb3a50a67b55178be5ca095433a91579e59 PASS index=/private/tmp/idx-oa1c
153	2026-11-13T17:37:00Z praxis-auditor:ace433dccdd9ac803 17b33c5b05e10ff97ea2a32d1507bd1701bc067a012a0ca2c893bb61cdb59c96 PASS index=/private/tmp/idx-oa2
```
AUDIT_LOG rows carry no report path, only an index path (rows :100-:154 read in full). So "does a PASS cover this file" is decided by what the index held, which the DECISION_LOG rows state.

---

## Group 1 — O3 block1-scope (9 files), bead Praxis_build-p3l

Paths: docs/reports/2026-11-12-o3-block1-scope-{manager,worker1,correction-1-manager,correction-1-worker1,correction-2-manager,correction-2-worker2,evidence}.md; docs/reports/2026-11-13-o3-cure3-{manager,worker1}.md.

Owner: unit O3 (rubric O3, D-2026-11-12-C), master runs 2026-11-12 17:00Z, 21:01Z, 2026-11-13 01:00Z, 05:01Z. One owner.

Ledger rows (DECISION_LOG.md, `grep -n -- o3-block1-scope` / `o3-cure3`, then `sed -n Np | cut`; DISPATCH_LOG grep printed nothing for either slug):
```
881: - [2026-11-12T17:44:00Z] WHO: praxis-master | WHAT: **Unit 2 (O3) AUDIT FAIL 1 (bead `Praxis_build-p3l`, filed this row; strike 1 of 2 under the absolute park rule).** praxis-a
882: - [2026-11-12T18:02:00Z] WHO: praxis-master | WHAT: **O3 Correction 1 manager (af21806f92873fbb4, 22 tool uses) returned `Result: BLOCKED`.** Per its return
883: - [2026-11-12T18:30:00Z] WHO: praxis-master | WHAT: **O3 Correction 2 manager (a01f4cc19809e80a5, 15 tool uses) returned `Result: FAIL`** (per its return, not yet OBSERVED
887: - [2026-11-12T21:25:00Z] WHO: praxis-master | WHAT: **Unit 1 manager (aae45e60025cda6e5, 14 tool uses) returned `Result: FAIL` from its own adversary; report read on disk** (`docs/repo
890: - [2026-11-12T22:07:39Z] WHO: praxis-master | WHAT: **Round-4 manager (a436690f3869ac08a, 14 tool uses) returned `Result: FAIL`; O3 STOPS for this run per the 22:00:00Z row ite
897: - [2026-11-13T05:20:00Z] WHO: praxis-master | WHAT: **Cure-3 manager (a31053066130caa60, 15 tool uses) returned `Result: PASS`; report read on disk** (`docs/reports/2026-11-13-o3-cure3-
898: - [2026-11-13T05:33:00Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate | WHAT: **Rubric O3 entry LANDED: `cae83dc` (3 files / 510+ / 0−), PUSHED
```
Why left out — the recipe, decided by the master (awk substr from the quoted anchors):
```
883: commit only the entry (DECISIONS.md blob = HEAD + working-tree :2371–2387, ...) plus ONE fresh short evidence report written from scratch ...; the six earlier O3 reports are named by path in that report and in the commit body and stay on disk, uncommitted and unedited, as the record of the failed attempts; then ONE fresh reduced audit; ...
886: changeable by Amear:** the entry's one Evidence pointer at :2385 is re-pointed to the new report `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section); ... The six earlier O3 reports stay on disk, unedited, uncommitted (sha256 before and after recorded). ...
897: **Temp index `/tmp/idx-o3`** = HEAD `0804c3e` + DECISIONS.md (HEAD + working-tree :2371–2387) + MANIFEST.md (HEAD + :459 + last row; 446 lines) + `-evidence-2.md`; 3 files, 510+ / 0−; `git diff --cached | openssl dgst -sha256` = `5ef19c8d0cd0fa894b88e0123e57f59ffb656326bb44c508e980d29c1afcf5ba`. The cure-3 manager and worker reports and the seven earlier O3 reports stay on disk, uncommitted. Next: ONE fresh reduced praxis-auditor ...
```
Commit body of cae83dc:
```
$ git show -s --format=%B cae83dc | grep -n -E 'o3-|report'
3:Evidence report cured in three dated rounds (append-only); the cure-3 change is line 251 only, itemised in its Cure 3 section. Seven earlier O3 reports and the cure-3 manager and worker reports stay on disk, uncommitted. ...
```
The filed evidence-2 report names the seven earlier ones by path, not the cure-3 pair:
```
$ for s in ...; do printf '%s %s\n' "$(git show HEAD:docs/reports/2026-11-12-o3-block1-scope-evidence-2.md | grep -c -- "$s")" "$s"; done
4 o3-block1-scope-manager
4 o3-block1-scope-worker1
4 correction-1-manager
4 correction-1-worker1
4 correction-2-manager
4 correction-2-worker2
4 o3-block1-scope-evidence.md
0 o3-cure3
```
Audit: mint :147 (05:13:44Z, hash 5ef19c8d...5ba, idx-o3) equals the 897 index hash; that index held 3 files (897, and cae83dc stat). The PASS covers DECISIONS.md, MANIFEST.md and evidence-2 only, not any file in this group. Audit FAIL 1 at :881 was on the earlier attempt, whose reports these are. No audit for filing any of the 9 was found (DECISION_LOG grep above; AUDIT_LOG rows carry no paths).

Why left out: deliberate master decision under D1 (rows 883, 886, 897; commit body line 3) — the seven earlier reports are "the record of the failed attempts", kept on disk, uncommitted; the cure-3 pair stays out by the same row 897. Not an oversight.

Class, per file:
| path | Result | name | class |
|---|---|---|---|
| 2026-11-12-o3-block1-scope-manager.md | PASS :372 (then audit FAIL 1, row 881) | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-worker1.md | FAIL :335 | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-correction-1-manager.md | BLOCKED :620 | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-correction-1-worker1.md | FAIL :494 | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-correction-2-manager.md | FAIL :206 | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-correction-2-worker2.md | FAIL :350 | 0 | UNCLEAR |
| 2026-11-12-o3-block1-scope-evidence.md | FAIL :1341 | 0 | UNCLEAR |
| 2026-11-13-o3-cure3-manager.md | PASS :48 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| 2026-11-13-o3-cure3-worker1.md | GRADE: PASS :133 (no `Result:` line) | 0 | CLEAR-BUT-NEEDS-AUDIT |

Evidence for UNCLEAR on the seven: manager and worker1 were in the index that FAILed audit 1 (row 880 "+ the 2 reports", row 881 FAIL 1), which is UNCLEAR by the class rule. The other five are FAILed or BLOCKED adversary rounds that were never audited (row 883 "No audit spent"); I mark them UNCLEAR on a judgement call explained in the Summary note, not on the literal rule. Rows 883/886 decided all seven stay uncommitted. Whether to file them now, as history, belongs to Amear (Q1). Evidence for CLEAR-BUT-NEEDS-AUDIT on the cure-3 pair: one owner, PASS round (row 897), not parked (p3l ended at strike 1, row 898), no audit for filing them. Row 897 also says they "stay on disk, uncommitted"; that is a master decision, so filing them needs that decision lifted (Q1).

## Group 2 — R6 engine-entry (5 files), bead Praxis_build-ckh (PARKED)

Paths: docs/reports/2026-11-12-r6-engine-entry-{manager,worker1,worker2,correction-1-manager,correction-1-worker1}.md.

Owner: R6 step 2 unit (D-2026-11-12-B), master run 2026-11-12 09:01Z-09:55Z. One owner.

Ledger rows (DECISION_LOG; DISPATCH_LOG grep printed nothing):
```
862: - [2026-11-12T09:25:24Z] WHO: praxis-master | WHAT: **Unit 1 manager (a6e3dbb26888e10a0, 25 tool uses) returned `Result: PASS`; report read on disk** (`docs/reports/2026-11-12-r6-engine-e
863: - [2026-11-12T09:36:00Z] WHO: praxis-master | WHAT: **Unit 1 AUDIT FAIL 1 (bead `Praxis_build-ckh`; strike 1 of 2 under the absolute park rule).** One praxis-worker (a2b7820955025d
864: - [2026-11-12T09:44:01Z] WHO: praxis-master | WHAT: **Correction 1 manager (a446abc09dd1c759d, 17 tool uses) returned `Result: PASS`; reports read on disk** (`docs/reports/2026-11-12-r6-e
865: - [2026-11-12T09:53:00Z] WHO: praxis-master | WHAT: **Unit 1 AUDIT FAIL 2 on bead `Praxis_build-ckh`: ABSOLUTE PARK RULE FIRES.** praxis-auditor a596df35dd9df27cc (21 tool uses) on `/tmp/idx-u1c`
866: - [2026-11-12T09:54:30Z] WHO: praxis-master | WHO COMMITTED: praxis-master (park commit, C2 exemption, no audit token) | WHAT: **PARKED: `parked/Praxis_build-ckh` @ `9bf0516` (9 files / 1871+ / 0−), PUSHED
```
HANDOFF.md :214 (2026-11-12 09:01Z card): "... no ckh files: DECISIONS.md, the five r6-engine-entry reports and the last 6 MANIFEST rows stay out until `ckh` lands)." HANDOFF.md :13 (top card): "1. Human: resume or rule on `ckh` (cure in the 2026-11-12 09:01Z card below, unchanged)."

Bead:
```
$ bd show Praxis_build-ckh | head -25
○ Praxis_build-ckh · R6 research P0 under D7: ... [● P0 · OPEN]
NOTES
  2026-11-12 PARKED (absolute park rule, audit-fail-x2): step 2 S4 entry D-
  2026-11-12-B on parked/Praxis_build-ckh @ 9bf0516 (pushed). FAIL 1 S1
  ... FAIL 2 S1 in original adversary report worker1 :156 placeholder arg, output cut with ... at :133-
  :314, :154 unpasted claim. A human resumes; ...
```
Already committed on the park branch, byte-identical:
```
$ git show --stat --format='%h %s' 9bf0516
 ...6-11-12-r6-engine-entry-correction-1-manager.md | 378 +++
 ...6-11-12-r6-engine-entry-correction-1-worker1.md | 413 +++
 docs/reports/2026-11-12-r6-engine-entry-manager.md | 225 +++
 docs/reports/2026-11-12-r6-engine-entry-worker1.md | 372 +++
 docs/reports/2026-11-12-r6-engine-entry-worker2.md | 361 +++
 (plus DECISIONS.md, DECISION_LOG.md, DISPATCH_LOG.md, MANIFEST.md; 9 files changed, 1871 insertions(+))
$ for s in ...; do git show 9bf0516:$f | cmp -s - $f; echo "cmp=$? $f"; done
cmp=0 docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
cmp=0 docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
cmp=0 docs/reports/2026-11-12-r6-engine-entry-manager.md
cmp=0 docs/reports/2026-11-12-r6-engine-entry-worker1.md
cmp=0 docs/reports/2026-11-12-r6-engine-entry-worker2.md
$ git branch -a --contains 9bf0516
  parked/Praxis_build-ckh
  remotes/origin/parked/Praxis_build-ckh
```
Audit: two FAILs (rows 863, 865); park commit carries "no audit token" (row 866). No PASS. Why left out of main: parked unit, HANDOFF :214 keeps them out until ckh lands.

Class: all 5 UNCLEAR (parked unit, audit FAILed twice). Name count 0 for all 5. Result lines: manager PASS :223, worker1 FAIL :370, worker2 PASS :357, correction-1-manager PASS :376, correction-1-worker1 FAIL :411. Note: the working-tree copies are already preserved on origin (parked branch), so removing them from main's working tree loses no bytes; that choice, and ckh itself, are Amear's (Q2).

## Group 3 — O4 (13 files), bead Praxis_build-yra (CLOSED)

Paths: docs/reports/2026-11-13-o4-parity-{manager,worker1,worker2,worker3,worker4}.md; -o4-reduce-{manager,worker1}.md; -o4-reduce2-{manager,worker1}.md; -o4-repoint-{manager,worker1}.md; -o4-cure1-{manager,worker1}.md.

Owner: unit O4 (rubric O4, D-2026-11-13-A), master runs 2026-11-13 05:01Z, 09:01Z, 13:01Z. One owner. DISPATCH_LOG grep for every O4 slug printed nothing.

Ledger rows (DECISION_LOG, `grep -n -- <slug>`, cut at 200):
```
900:- [2026-11-13T06:06:00Z] ... **O4 manager (a4df3337448faa3b1, 63 tool uses) STOPPED AT ITS 60-TURN CAP; no Result (R-A: no-verdict return, not an audit, no strike).** OBSERV
901:- [2026-11-13T06:10:00Z] ... **O4 reduction manager (a05349890bd02b350, 12 tool uses) returned `Result: FAIL`; O4 STOPS for this run per the 06:06:00Z row.** OBSERVED (`date
905:- [2026-11-13T09:09:00Z] ... **O4 reduce-2 manager (a306eb0e2eb7e51c2, 10 tool uses) returned `Result: FAIL`; O4 STOPS for this run per the 09:03:00Z row.** OBSERVED (`date
912:- [2026-11-13T13:07:54Z] ... **O4 round-3 manager (a6932a80d84bae1f3, 25 tool uses) returned `Result: PASS`; cold adversary PASS on checks (a)–(g).** Master re-ran: `diff /t
913:- [2026-11-13T13:13:15Z] ... **Unit 2 manager (abd71709ca493a7bf, 12 tool uses) returned `Result: PASS`; cold adversary a355707eaab5c72cb PASS on checks 1–4.** Master re-ran
914:- [2026-11-13T13:17:27Z] ... **Audit FAIL 1 on `/tmp/idx-o4` (praxis-auditor aa9a5db3bab040c8b, 12 tool uses): strike 1 of 2 on bead `Praxis_build-yra`.** Checks 1–5 PASS (s
915:- [2026-11-13T13:24:23Z] ... **Cure manager (ae323e1c231c44f3f, 18 tool uses) returned `Result: FAIL` (`-cure1-manager.md` :57); adversary checks (1)–(4) PASS, (5) FAIL.** M
916:- [2026-11-13T13:28:34Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate | WHAT: **O4 entry LANDED: `4ffce95` (4 files / 380+ / 0−), PUSHED (`52ad416..4ffce95`).** Fresh audit p
```
Why left out (awk `index` excerpts):
```
901: ... + the reduce manager and worker reports; the five earlier O4 reports stay on disk, uncommitted.
912: ... entry :2402 cites `docs/reports/2026-11-13-o4-parity-manager.md` for the zero-hit claim, and that report ends `Result: RESULT_LINE` (:156), an unfinished report (its manager hit the turn cap); it cannot go in the commit, and a citation to an uncommitted file would dangle. ... The five earlier O4 reports stay on disk, uncommitted.
913: Temp index `/tmp/idx-o4` = HEAD `52ad416` + DECISIONS.md blob ... + MANIFEST.md blob ... + the two round-3 reports: 4 files / 379+ / 0−; ... Out of the commit, on disk: MANIFEST :468 (parity-manager row), the five earlier O4 reports, `-repoint-manager.md` and `-repoint-worker1.md`, the parked `ckh` entry.
915: ... + the two round-3 reports (manager report now 91 lines): 4 files / 380+ / 0−; diff sha256 `f2057635…fe81`. The cure reports stay on disk, uncommitted. A FAIL is strike 2 and parks `yra`.
916: ... Master re-ran the diff hash `f2057635…fe81`, equal; gate admitted the commit; `HEAD^{tree}` `2520a8d9…` = `/tmp/idx-o4b` write-tree; ... Strike on `yra` ended at 1.
```
Gap (S2): "the five earlier O4 reports" is first used at 06:10Z (row 901), when the only earlier O4 reports were the five parity files. Rows 912/913 repeat "five" after the reduce and reduce2 pairs (4 more files) existed. I found no row that names the reduce or reduce2 reports as staying out; they are out because the enumerated indexes (913, 915) do not list them. Whether "five" in 912/913 was meant to include them is UNVERIFIED.

Bead:
```
$ bd show Praxis_build-yra | head -4
✓ Praxis_build-yra · Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 live-vs-backtest reconciliation   [● P1 · CLOSED]
Close reason: Rubric O4 answered by D-2026-11-13-A, committed at 4ffce95 after audit PASS (DECISION_LOG 2026-11-13T13:28:34Z); ...
```
Audit: mint :150 (13:28:02Z, hash f20576358918...fcfe81, idx-o4b) matches the 915 index hash `f2057635…fe81`; that index held DECISIONS.md, MANIFEST.md, o4-reduce3-manager, o4-reduce3-worker1 only. Audit FAIL 1 (row 914) was on idx-o4, which held the same two round-3 reports, not any file in this group. No audit PASS or FAIL covers any of these 13 files; no filing audit found.

| path | Result | name | class |
|---|---|---|---|
| o4-parity-manager.md | `Result: RESULT_LINE` :156 (unfilled; manager hit turn cap, row 900, 912) | 0 | UNCLEAR |
| o4-parity-worker1.md | `Grade: FAIL (4 defects)` :266 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-parity-worker2.md | FAIL (4 defects) after :310 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-parity-worker3.md | FAIL (2 defects) after :292 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-parity-worker4.md | FAIL / Grade: FAIL (3 defects) after :290 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-reduce-manager.md | FAIL :69 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-reduce-worker1.md | FAIL after :317 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-reduce2-manager.md | FAIL :58 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-reduce2-worker1.md | FAIL (1 defect) :65 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-repoint-manager.md | PASS :64 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-repoint-worker1.md | PASS :245 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-cure1-manager.md | FAIL :57 | 0 | CLEAR-BUT-NEEDS-AUDIT |
| o4-cure1-worker1.md | no own verdict line found (row 915: adversary (1)-(4) PASS, (5) FAIL) | 0 | CLEAR-BUT-NEEDS-AUDIT |

Evidence for UNCLEAR on parity-manager: row 912 "an unfinished report ... it cannot go in the commit"; its Result line is a placeholder. The other 12: one owner, unit not parked (bead closed), the FAILs are adversary grades on non-audited rounds, not audit FAILs; content is report evidence; no filing audit. Rows 912/913/915 kept them out by master decision for that commit only.

## Group 4 — OPEN-A1 (3 files), bead Praxis_build-fgd (OPEN)

Paths: docs/reports/2026-11-13-open-a1-manager.md; docs/reports/2026-11-13-open-a1-worker1.md; docs/reports/2026-11-13-open-a1-cure-worker1.md.

Owner: OPEN-A1 item of bead fgd (D-2026-11-13-B), master runs 2026-11-13 13:01Z and 17:00Z. One owner. DISPATCH_LOG `grep -c` = 0 for each slug.

Ledger rows:
```
918:- [2026-11-13T13:34:45Z] ... **OPEN-A1 filing manager (af35976deec88ed14, 20 tool uses) returned `Result: PASS` (`-open-a1-manager.md` :76); cold adversary one rou
   ... Temp index `/tmp/idx-oa1` = HEAD `4ffce95` + DECISIONS.md blob ... + the two open-a1 reports: 4 files / 348+ / 0−; diff sha256 `7f3a6b58…6c6d`
919:- [2026-11-13T13:37:42Z] ... **Audit FAIL 1 on `/tmp/idx-oa1` (praxis-auditor aea1f1238aaba8957, 10 tool uses): strike 1 of 2 on the OPEN-A1 item of bead `Praxis_b
   ... dence report from scratch (literal commands, full output, no sed-altered diffs) and commit it in place of the two open-a1 reports, which stay on disk uncommitted; MANIFEST rows re-pointed to the fresh report.
924:- [2026-11-13T17:12:19Z] ... **OPEN-A1 cure manager (aaaa3abe31d9e4d3c, 18 tool uses) returned `Result: BLOCKED` (`-cure-manager.md` :258); cold adversary FAIL on (f) and (g) only, (a)–(e) and (h) PASS (`-cure-worker1.md` :312, :328).**
925:- [2026-11-13T17:15:15Z] ... **Fix manager (abc26e07ccbf03f32, 11 tool uses) returned `Result: PASS` (`-cure-manager.md` :276).** ... Temp index `/tmp/idx-oa1c` ... 3 files / 296+ / 0−; diff sha256 `1f25eaec…9e59`; ... Out of the commit, on disk: MANIFEST :472–:473 (old open-a1 report rows), the two old open-a1 reports, `-cure-worker1.md`.
926:- [2026-11-13T17:18:24Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate | WHAT: **OPEN-A1 entry LANDED: `9bf653a` (3 files / 296+ / 0−), PUSHED (`b64ff1a..9bf653a`).*
```
Bead: `○ Praxis_build-fgd · F2 amendment S6 follow-ups F-1..F-9: ...` (open, not parked).

Audit: mint :152 (17:17:52Z, hash 1f25eaec...9e59, idx-oa1c) matches row 925; that index held DECISIONS.md, MANIFEST.md, open-a1-cure-manager only. Audit FAIL 1 (row 919) graded idx-oa1, which held open-a1-manager and open-a1-worker1 (row 918: "+ the two open-a1 reports").

| path | Result | name | class |
|---|---|---|---|
| open-a1-manager.md | PASS :76 (then audit FAIL 1, row 919) | 0 | UNCLEAR |
| open-a1-worker1.md | `## Overall: PASS` :236 (in the FAILed audit index) | 0 | UNCLEAR |
| open-a1-cure-worker1.md | FAIL :328 | 0 | CLEAR-BUT-NEEDS-AUDIT |

Evidence: manager/worker1 were in the index that FAILed audit (918, 919) and 919 decided they "stay on disk uncommitted", replaced by the fresh report. cure-worker1 was never in an audited index (925 lists it as out of the commit); one owner, adversary FAIL only, fgd not parked.

## Group 5 — OPEN-A2 (1 file), bead Praxis_build-fgd, plus c2w

Path: docs/reports/2026-11-13-open-a2-worker1.md. Owner: OPEN-A2 item of fgd (D-2026-11-13-C), master run 2026-11-13 17:00Z. DISPATCH_LOG `grep -c` = 0.

Ledger rows:
```
929:- [2026-11-13T17:33:15Z] ... **OPEN-A2 report manager (ac5536369775e0d91, 20 tool uses) returned `Result: PASS` (`-open-a2-manager.md` :234); its cold adversary returned FAIL on (b), (c), (g), PASS on (a), (d), (e), (f), (h), (i); the manager cured by deletion only.**
   ... + the report: 3 files / 259+ / 0−; diff sha256 `17b33c5b…9c96`; write-tree `4adad40a…87e7`; `evidenc[e]/` count on the diff 0.
930:- [2026-11-13T17:37:20Z] WHO: praxis-master | WHO COMMITTED: praxis-master through the gate | WHAT: **OPEN-A2 entry LANDED: `661e073` (3 files / 259+ / 0−), PUSHED (`9bf653a..661e073`).*
```
Audit: mint :153 (17:37:00Z, hash 17b33c5b...9c96, idx-oa2) matches row 929; that index held DECISIONS.md, MANIFEST.md, open-a2-manager only. No row I found names open-a2-worker1 as staying out; it is out by enumeration of idx-oa2.

Bead c2w:
```
$ bd show Praxis_build-c2w | head -2; bd show Praxis_build-c2w | grep -n -i 'open-a2'
○ Praxis_build-c2w · De-identification sweep: MFFU rep first name in committed MANIFEST rows and untracked reports   [● P2 · OPEN]
10:  docs/reports/2026-11-13-open-a2-worker1.md (once), and in the file name of
```
Result lines: PASS :184 and FAIL :261 (two rounds in one file). Name count 1 (E1, line 196).

Class: UNCLEAR — content holds the rep name (bead c2w); also its own last verdict is FAIL.

---

## Summary table

| group | files | CLEAR-FILE | CLEAR-BUT-NEEDS-AUDIT | UNCLEAR |
|---|---|---|---|---|
| O3 (p3l) | 9 | 0 | 2 (cure3 pair) + see note | 2 (manager, worker1) + see note |
| R6 (ckh, parked) | 5 | 0 | 0 | 5 |
| O4 (yra) | 13 | 0 | 12 | 1 (parity-manager) |
| OPEN-A1 (fgd) | 3 | 0 | 1 (cure-worker1) | 2 |
| OPEN-A2 (fgd, c2w) | 1 | 0 | 0 | 1 |

Note on O3: the per-file table above marks all seven earlier O3 reports UNCLEAR. By the class wording only manager and worker1 were in an audit that FAILed (row 880: idx-o3 held "the 2 reports"; row 881 FAIL 1). The five later ones (correction-1 pair, correction-2 pair, evidence.md) were never in an audited index (row 883: "No audit spent"), so under the literal class rule they would be CLEAR-BUT-NEEDS-AUDIT, the same as the O4 adversary-FAIL rounds. I keep them UNCLEAR because rows 883/886 and the cae83dc body make them a deliberate "record of the failed attempts", and correction-1 edited the audited manager report in place after FAIL 1 (row 882; manager mtime 12:57:08 -0500 = 17:57:08Z, after the 17:44:00Z FAIL). The manager may re-grade these five to CLEAR-BUT-NEEDS-AUDIT for consistency with O4; I mark the choice, not decide it.

No file in scope is CLEAR-FILE: no AUDIT_LOG PASS index held any of the 31 (E3 and the per-group index rows). Every PASS in the four unit commits graded only the committed files.

## Questions for Amear (S8; not decided here)
- Q1. Should the FAILed or superseded round reports (O3 seven, O4 twelve, OPEN-A1 three) be filed as history, or stay on disk as rows 883/886/897/912/913/915/919/925 left them? Filing any needs a fresh audit.
- Q2. ckh: resume or rule (HANDOFF :13). The five R6 reports are already byte-identical on `parked/Praxis_build-ckh` @ 9bf0516 on origin.
- Q3. open-a2-worker1 waits on the c2w sweep (name present once).

## Out of scope, noted
- Row 897 is stamped 05:20:00Z but cae83dc is 05:13:58Z and the PASS mint is 05:13:44Z; the row stamp is later than the commit it plans. Not graded.

## Name check on this report
```
$ printf '%s %s\n' "$(grep -ci "$N" $R)" $R; grep -c -E '<email pattern>' $R; git status --porcelain -- $R
0 docs/reports/2026-11-14-dirty-tree-sort-worker5.md
0
?? docs/reports/2026-11-14-dirty-tree-sort-worker5.md
```
(Run before this block was added; the block itself holds no name.)

## Files staged
None. This unit is read-only; the only file written is this report (untracked).

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
