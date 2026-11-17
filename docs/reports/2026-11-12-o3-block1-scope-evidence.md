# 2026-11-12 — O3 Block-1 scope evidence (unit 2026-11-12-o3-evidence, bead Praxis_build-p3l, rubric O3)

Manager report, with cure rounds 2 and 3 by BUILD praxis-workers. Master's decisions under D-2026-11-08-D D1: DECISION_LOG 2026-11-12T21:04:00Z (first pass), 2026-11-12T21:25:00Z (cure round 2) and 2026-11-12T21:41:00Z (cure round 3). Nothing is staged or committed by this unit.

Claim: the master's 21:04:00Z decision row is in the working-tree DECISION_LOG.md (full line) and is not yet at HEAD (count 0):

```text
$ grep -n -F '2026-11-12T21:04' DECISION_LOG.md
886:- [2026-11-12T21:04:00Z] WHO: praxis-master | WHAT: **Unit 1 dispatched: O3 material reduction (bead `Praxis_build-p3l`, strike 1 of 2).** OBSERVED before dispatch: entry D-2026-11-12-C :2385 (S6 paragraph) ends "Evidence: `docs/reports/2026-11-12-o3-block1-scope-manager.md` (S6 section)." — a report the 18:30:00Z recipe keeps out of the commit, so the committed entry would cite a file not in the repo. **Decided by master under D-2026-11-08-D D1, amending the 18:30:00Z recipe item (b), changeable by Amear:** the entry's one Evidence pointer at :2385 is re-pointed to the new report `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section); no other byte of the entry changes; the old/new text and old/new sha256 of :2371–2387 are itemised in the new report. The six earlier O3 reports stay on disk, unedited, uncommitted (sha256 before and after recorded). MANIFEST commit blob = HEAD MANIFEST (444 lines) + the working-tree DECISIONS.md amendment row (:459) + one new row for the evidence report. One praxis-manager, foreground, 35-call budget, report written early; one adversary worker re-runs every pasted command. | WHY: rubric O3; S1; S7; park rule | WHERE: DECISIONS.md :2385, docs/reports, MANIFEST.md | WHEN: 21:04Z (`date -u` 21:01:14Z plus brief drafting) | HOW: praxis-manager foreground | STATE: open
```

```text
$ git show HEAD:DECISION_LOG.md | grep -c -F '2026-11-12T21:04'
0
```

Claim: the master's 21:25:00Z decision row is in the working-tree DECISION_LOG.md (count 1) and not yet at HEAD (count 0). It holds an ellipsis string from the list in /tmp/o3e-ellipsis.txt (count 1), so it is not pasted whole; the phrases below are matched on that row and show its decided items (a), (b) and (c):

```text
$ grep -c -F '2026-11-12T21:25' DECISION_LOG.md
1
```

```text
$ git show HEAD:DECISION_LOG.md | grep -c -F '2026-11-12T21:25'
0
```

```text
$ grep -F '2026-11-12T21:25' DECISION_LOG.md | grep -c -F -f /tmp/o3e-ellipsis.txt
1
```

```text
$ grep -F '2026-11-12T21:25' DECISION_LOG.md | grep -o -F 'Decided by master under D-2026-11-08-D D1, changeable by Amear:'
Decided by master under D-2026-11-08-D D1, changeable by Amear:
```

```text
$ grep -F '2026-11-12T21:25' DECISION_LOG.md | grep -o -F "but the entry adds ONE sentence naming Block 0's Step 0.8 as a curl test to a remote public-host webhook"
but the entry adds ONE sentence naming Block 0's Step 0.8 as a curl test to a remote public-host webhook
```

```text
$ grep -F '2026-11-12T21:25' DECISION_LOG.md | grep -o -F "(b) the entry's S6 paragraph names Block 0"
(b) the entry's S6 paragraph names Block 0
```

```text
$ grep -F '2026-11-12T21:25' DECISION_LOG.md | grep -o -F '(c) report items 1–3 are cured by DELETING or narrowing the unbacked sentences, not by adding claims'
(c) report items 1–3 are cured by DELETING or narrowing the unbacked sentences, not by adding claims
```

Claim: the master's 21:41:00Z decision row is in the working-tree DECISION_LOG.md (count 1) and not yet at HEAD (count 0). It also holds an ellipsis string from the list in /tmp/o3e-ellipsis.txt (count 1), so it is not pasted whole; the phrases below are matched on that row and show its decided items (1) to (4):

```text
$ grep -c -F '2026-11-12T21:41' DECISION_LOG.md
1
```

```text
$ git show HEAD:DECISION_LOG.md | grep -c -F '2026-11-12T21:41'
0
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -c -F -f /tmp/o3e-ellipsis.txt
1
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F 'Decided by master under D-2026-11-08-D D1, changeable by Amear:'
Decided by master under D-2026-11-08-D D1, changeable by Amear:
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F '(1) REMOVE the 21:25:00Z item (a) sentence from the scope line entirely (the scope line returns to its audited text)'
(1) REMOVE the 21:25:00Z item (a) sentence from the scope line entirely (the scope line returns to its audited text)
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F '(2) rewrite only the S6 paragraph to name Block 0'
(2) rewrite only the S6 paragraph to name Block 0
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F 'and to record ONE conflict, not resolved'
and to record ONE conflict, not resolved
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F '(3) the report drops every claim it cannot paste'
(3) the report drops every claim it cannot paste
```

```text
$ grep -F '2026-11-12T21:41' DECISION_LOG.md | grep -o -F '(4) one adversary on the whole report and entry'
(4) one adversary on the whole report and entry
```

How to read this report: every fenced block whose first line starts with `$ ` was produced by a script that printed the command after `$ ` and then ran it with bash, from the working directory /Volumes/Sensidine/Praxis.build, with stdin from /dev/null, and captured stdout and stderr (in cure round 3, a run helper that re-ran every such block of this file in order and pasted its output). To re-check a block, run the text after `$ ` from that directory. Exit codes appear only where the command itself echoes them. The fenced blocks whose first line does not start with `$ ` (Process log items 2, 6, 7, 8 and 9) are records of edit commands as they were run once, by hand, and were not run by the script.

## Task

Back entry D-2026-11-12-C (working-tree DECISIONS.md lines 2371–2387, uncommitted) with pasted command output, re-point the entry's one S6 evidence pointer from the earlier manager report to this report, and append one MANIFEST.md row for this report. Cure round 2 (21:25:00Z): add one sentence to the entry's scope line naming Block 0's Step 0.8 test, name Block 0 in the entry's S6 paragraph, cure the report items by deleting or narrowing, and rewrite this report's MANIFEST row to name those edits. Cure round 3 (21:41:00Z): the cure-round-2 sentence is removed from line 2376 and the S6 paragraph on line 2385 is rewritten (Edits 4 and 5); this report re-runs or re-points its blocks, rewrites its S6 section and its MANIFEST row, and drops claims it cannot paste. Working-tree DECISIONS.md lines 2279–2370 belong to the parked unit ckh (entry D-2026-11-12-B) and are outside this unit. The six earlier O3 reports are left as they are.

Claim: the parked entry's id and bead sit inside working-tree lines 2279–2370 (line numbers with the matched id only; the parked text is not reproduced):

```text
$ grep -n -o -F 'D-2026-11-12-B' DECISIONS.md
2280:D-2026-11-12-B
2287:D-2026-11-12-B
```

```text
$ grep -n -o -F 'Praxis_build-ckh' DECISIONS.md
2283:Praxis_build-ckh
```

The entry as it now stands, lines 2371–2386 (line 2387 is the standing limitation line; it is checked by count, not pasted, so that the sentence stands alone only once in this report):

```text
$ sed -n '2371,2386p' DECISIONS.md

## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-12T17:31Z), changeable by Amear. Not Amear's ruling. A scope record only.

**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).

**Sources (DECISIONS.md at a411e17).**
- D-2026-07-09-D, heading at :133 ("n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live"); the path and the deferral are in its **Decision:** paragraph at :140.
- The sign-off, heading "## 2026-07-15 — Block 1 milestone — trader sign-off" at :174, body at :175; the body records B1-a as "verified-as-DEFERRED (D-2026-07-09-D)".
- Rubric O3, `specs/SPEC_RUBRIC.md` "## OPEN — gradeable now", "### O3 — Block-1 milestone scope statement".

**Limits.** This entry records scope only. It makes no design choice, adds no test, and does not re-open or re-grade the 2026-07-15 sign-off. It does not change rubric O3's state; that move is a later master step. It does not decide where public ingress goes. Cross-reference only: `docs/specs/2026-11-10-live-signal-topology.md` (D-2026-11-10-B) :112 already says Deviation G's ingress question leaves the anchor's live path; this entry adds nothing to it.

**S6 cross-block.** Touches Block 0 (Step 0.8, commit `2582531`, whose body records "Webhook->validate->file write (/tmp/praxis-signals on n8n host)"; nothing in Block 0 is re-graded), Block 1 (the reach of the 2026-07-15 sign-off), Block 2 (`docs/specs/2026-11-05-phase3-build-specification.md` :180, "When Block 1’s milestone is hit, Block 2 starts. Not before."), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved there) and rubric F1 / the live-signal topology `docs/specs/2026-11-10-live-signal-topology.md` (:112, cross-reference only). One conflict, recorded, not resolved: the Phase 3 spec's Block 1 milestone (:60, "fire a fake signal from TradingView") includes TradingView ingress; the milestone signed off on 2026-07-15 did not; Block 2 started on that sign-off (:180). This entry records the gap; it does not re-grade the sign-off, re-open Block 1 or stop Block 2 (decided by master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:41Z, changeable by Amear). Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).

```

```text
$ sed -n '2387p' DECISIONS.md | grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
```

## Rubric criteria addressed

- O3 (Block-1 milestone scope statement): text pasted from HEAD in section E3.

- S1 (every claim has pasted command output).

- S2 (no component reported above its evidence): section S2 statement.

- S6 (cross-block check): section S6 cross-block check.

- S13 (standing limitation sentence, once): carried as the last line of this file; count shown in Verification evidence.

## Workers dispatched

- Worker 1 (agent a552582f0bffee24b): praxis-worker, ADVERSARIAL, full re-run of every command in this report; wrote no report file. Outcome: GRADE: FAIL (9 defects); all nine cured (see Adversary).
- Worker 2: praxis-worker, ADVERSARIAL, re-check of the cured items only; wrote no report file. Outcome: GRADE: FAIL (5 defects); cured in Cure round 2 (see Cure round 2 and Adversary).
- Worker 3: praxis-worker, BUILD, cure round 2: made the two entry edits (lines 2376 and 2385), rewrote the MANIFEST row for this report, and regenerated this report by script; wrote no other report file.
- Worker 4: praxis-worker, ADVERSARIAL, re-run of every pasted command after cure round 2 (Adversary 3).
- Worker 5: praxis-worker, BUILD, cure round 3: edited this report in place and rewrote the MANIFEST row for this report; made no DECISIONS.md edit (per its brief, the manager made the two cure-round-3 entry edits); wrote no other report file.
- Worker 6: praxis-worker, ADVERSARIAL, Adversary 4 (pending).
- Before cure round 2 there was no BUILD worker: per the master's brief, the manager made the one-line pointer edit, the MANIFEST row and the earlier passes of this report himself.

## Process log

1. Before any edit, the manager ran one shell call that wrote the sha256 of the six earlier reports and of lines 2371–2387 to /tmp/o3-pre.txt (via tee) and saved the old line 2385 to /tmp/o3e-old-2385.txt. Their contents are pasted in Entry edit log and Untouched files, each with a re-derivation that does not depend on the capture.

2. One edit to DECISIONS.md (the pointer edit), run once by the manager. It is recorded here and must not be re-run (re-running is a no-op, since the old substring is gone):

```text
perl -i -pe 'if ($. == 2385) { s/\Q`docs\/reports\/2026-11-12-o3-block1-scope-manager.md` (S6 section)\E/`docs\/reports\/2026-11-12-o3-block1-scope-evidence.md` (S6 section)/ }' DECISIONS.md
```

3. One MANIFEST.md row appended with printf to the end of the file. Shown in the MANIFEST section, with a count showing the row starts a line of its own.

4. This report generated by script, then two ADVERSARIAL praxis-workers in turn: the first re-ran every command, the second re-checked the cured items (see Adversary).

Limitation: no whole-file copy of DECISIONS.md was taken before the pointer edit, so the claim that lines 2279–2370 were left byte-identical by that edit rests on the line-conditional perl command above and on the entry hash captured before that edit (Entry edit log); it was not observed by a before/after file compare. The cure-round-2 edits were checked by a whole-file before/after compare (Entry edit log, Whole-file compare: diff and cmp).

5. Cure round 2 (master, 21:25:00Z). The brief named the scope-line paragraph as line 2375. Line 2375 is a blank line (its capture is 1 byte) and the scope-line paragraph is line 2376, so the edit was made at 2376:

```text
$ wc -c < /tmp/o3e-old-2375.txt
       1
```

```text
$ grep -n -o -F '**Scope line (rubric O3).**' /tmp/o3e-pre-cure2-DECISIONS.md
2376:**Scope line (rubric O3).**
```

6. Whole-file copy and line captures, then the edit, run once each by the BUILD worker (record; not re-run):

```text
cd /Volumes/Sensidine/Praxis.build && cp DECISIONS.md /tmp/o3e-pre-cure2-DECISIONS.md && sed -n '2375p' DECISIONS.md > /tmp/o3e-old-2375.txt; sed -n '2385p' DECISIONS.md > /tmp/o3e-old-2385b.txt; wc -c /tmp/o3e-old-2375.txt /tmp/o3e-old-2385b.txt; tail -c 40 /tmp/o3e-old-2375.txt; grep -c -F 'Touches Block 1 (' /tmp/o3e-old-2385b.txt; grep -o -F 'Touches Block 1 (' DECISIONS.md | wc -l; cmp /tmp/o3e-pre-cure2-DECISIONS.md DECISIONS.md; echo exit=$?
cd /Volumes/Sensidine/Praxis.build && sed -n '2376p' DECISIONS.md > /tmp/o3e-old-2376.txt && cmp /tmp/o3e-pre-cure2-DECISIONS.md DECISIONS.md && echo same-before && python3 -I /tmp/o3e-cure2-edit.py; echo exit=$?; wc -l DECISIONS.md; diff /tmp/o3e-pre-cure2-DECISIONS.md DECISIONS.md | grep -E '^[0-9]'; tail -c 1 DECISIONS.md | xxd
```

The edit script, as it is on disk (it edits only file lines 2376 and 2385, and exits without writing if either line's guard fails). Since cure round 3, line 2385 no longer contains 'Touches Block 1 (' (count 0, after the script), so a re-run now stops at the 2385 guard:

```text
$ cat /tmp/o3e-cure2-edit.py
import sys
p = '/Volumes/Sensidine/Praxis.build/DECISIONS.md'
with open(p, 'rb') as f:
    lines = f.read().split(b'\n')
# lines[i] is file line i+1
a = 2376 - 1
b = 2385 - 1
old_a_end = 'and is untested (rubric O3).'.encode()
new_a_add = " Block 0's Step 0.8 (commit `2582531`, 2026-07-08) posted a test payload by curl to a webhook on a remote public host whose n8n wrote to a directory on that host; it ran before the local path existed and was not TradingView ingress into it (D-2026-07-09-D :140, \"as Step 0.8 did against `/tmp`\").".encode()
old_b = 'Touches Block 1 ('.encode()
new_b = 'Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 ('.encode()
if not lines[a].startswith('**Scope line (rubric O3).**'.encode()) or not lines[a].endswith(old_a_end):
    sys.exit('line 2376 guard failed; no change written')
if not lines[b].startswith('**S6 cross-block.**'.encode()) or lines[b].count(old_b) != 1:
    sys.exit('line 2385 guard failed; no change written')
lines[a] = lines[a] + new_a_add
lines[b] = lines[b].replace(old_b, new_b, 1)
with open(p, 'wb') as f:
    f.write(b'\n'.join(lines))
print('edited lines 2376 and 2385')
```

```text
$ sed -n '2385p' DECISIONS.md | grep -c -F 'Touches Block 1 ('
0
```

7. MANIFEST.md: whole-file copy, then the last row rewritten in two line-conditional edits on line 466 (the last line), run once each (record; not re-run):

```text
cd /Volumes/Sensidine/Praxis.build && cp MANIFEST.md /tmp/o3e-pre-cure2-MANIFEST.md && wc -l < MANIFEST.md && tail -n 1 MANIFEST.md > /tmp/o3e-old-manifest-last.txt && perl -i -pe 'if ($. == 466 && eof) { s/\Qthe one-pointer edit to the entry S6 evidence path,\E/the one-pointer edit to the entry S6 evidence path and the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph),/ }' MANIFEST.md; echo exit=$?; wc -l < MANIFEST.md; diff /tmp/o3e-pre-cure2-MANIFEST.md MANIFEST.md | grep -E '^[0-9]'; tail -n 1 MANIFEST.md
cd /Volumes/Sensidine/Praxis.build && perl -i -pe 'if ($. == 466 && eof) { s/\QDECISION_LOG 2026-11-12T21:04:00Z)\E/DECISION_LOG 2026-11-12T21:04:00Z and 2026-11-12T21:25:00Z)/ }' MANIFEST.md; echo exit=$?; wc -l < MANIFEST.md; diff /tmp/o3e-pre-cure2-MANIFEST.md MANIFEST.md | grep -E '^[0-9]'; tail -n 1 MANIFEST.md | grep -c -F '21:04:00Z and 2026-11-12T21:25:00Z)'; head -n 465 MANIFEST.md | cmp - <(head -n 465 /tmp/o3e-pre-cure2-MANIFEST.md); echo exit=$?
```

8. Generator (cure round 2): the command used to regenerate this report from /tmp/o3e-gen2.sh (record; not re-run; its cmp result is not pasted):

```text
cd /Volumes/Sensidine/Praxis.build && for i in 1 2 3; do bash /tmp/o3e-gen2.sh > /tmp/o3e-q$i.md && cp /tmp/o3e-q$i.md docs/reports/2026-11-12-o3-block1-scope-evidence.md; done; cmp /tmp/o3e-q2.md /tmp/o3e-q3.md; echo exit=$?
```

Then one ADVERSARIAL praxis-worker re-runs every pasted command (Adversary 3).

9. Cure round 3 (master, 21:41:00Z). Lines 2376 and 2385 differ from the whole-file copy /tmp/o3e-pre-cure3-DECISIONS.md and no other line does (Entry edit log, Whole-file compare (cure round 3)). The master's item (3) says the report is regenerated from its script; the first generator, /tmp/o3e-gen.sh, holds no 'cure round' text (case-insensitive count 0, below), so it cannot reproduce the cure-round sections, and this report was instead edited in place, then every block whose first line starts with `$ ` was re-run in order by the run helper and its output pasted.

```text
$ grep -c -i -F 'cure round' /tmp/o3e-gen.sh
0
```

The MANIFEST row for this report was rewritten by the record command below, run once (record; not re-run). The script is pasted after it:

```text
cp MANIFEST.md /tmp/o3e-pre-cure3-MANIFEST.md && python3 -I /tmp/o3e-r3-manifest-edit.py; echo exit=$?; wc -l < MANIFEST.md; diff /tmp/o3e-pre-cure3-MANIFEST.md MANIFEST.md | grep -E '^[0-9]'
```

```text
$ cat /tmp/o3e-r3-manifest-edit.py
import sys
p = '/Volumes/Sensidine/Praxis.build/MANIFEST.md'
with open(p, 'rb') as f:
    data = f.read()
assert data.endswith(b'\n')
lines = data[:-1].split(b'\n')
last = lines[-1]
o1 = 'DECISION_LOG 2026-11-12T21:04:00Z and 2026-11-12T21:25:00Z)'.encode()
n1 = 'DECISION_LOG 2026-11-12T21:04:00Z, 2026-11-12T21:25:00Z and 2026-11-12T21:41:00Z)'.encode()
o2 = 'the one-pointer edit to the entry S6 evidence path and the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph),'.encode()
n2 = 'the one-pointer edit to the entry S6 evidence path, the two cure-round-2 entry edits and the two cure-round-3 entry edits (scope line restored to its pre-cure-2 text; S6 paragraph rewritten to name Blocks 0, 1, 2, 4 and 5 and F1 and to record one conflict, not resolved),'.encode()
if not last.startswith(b'| /docs/reports/2026-11-12-o3-block1-scope-evidence.md |') or last.count(o1) != 1 or last.count(o2) != 1:
    sys.exit('last-row guard failed; no change written')
lines[-1] = last.replace(o1, n1, 1).replace(o2, n2, 1)
with open(p, 'wb') as f:
    f.write(b'\n'.join(lines) + b'\n')
print('edited last line of MANIFEST.md')
```

Then one ADVERSARIAL praxis-worker re-runs every pasted command (Adversary 4).

## E1 prefix

Claim: the candidate commit blob (HEAD DECISIONS.md plus lines 2371–2387, without the parked lines 2279–2370) is built, has 2295 lines, starts with HEAD byte-for-byte, contains no D-2026-11-12-B, and equals the working tree with lines 2279–2370 deleted.

```text
$ { git show HEAD:DECISIONS.md; sed -n '2371,2387p' DECISIONS.md; } > /tmp/o3e-decisions-blob.md; echo exit=$?
exit=0
```

```text
$ wc -l < /tmp/o3e-decisions-blob.md
    2295
```

```text
$ git show HEAD:DECISIONS.md > /tmp/o3e-head-decisions.md; wc -l < /tmp/o3e-head-decisions.md
    2278
```

```text
$ head -n 2278 /tmp/o3e-decisions-blob.md | cmp - <(git show HEAD:DECISIONS.md); echo exit=$?
exit=0
```

```text
$ grep -c 'D-2026-11-12-B' /tmp/o3e-decisions-blob.md; echo exit=$?
0
exit=1
```

```text
$ sed '2279,2370d' DECISIONS.md | cmp - /tmp/o3e-decisions-blob.md; echo exit=$?
exit=0
```

```text
$ sed -n '2371p' DECISIONS.md | wc -c
       1
```

```text
$ shasum -a 256 /tmp/o3e-decisions-blob.md
4c17cf4d6f95a7e56a9121b3a7ddfc94396976152d5c3c88e29d113daf037f26  /tmp/o3e-decisions-blob.md
```

## E2 quotes

Claim: the entry's sources are cited at a411e17; DECISIONS.md is identical at a411e17 and HEAD.

```text
$ git diff --quiet a411e17 HEAD -- DECISIONS.md; echo exit=$?
exit=0
```

Claim: each double-quoted DECISIONS.md string in the entry occurs verbatim at HEAD, at the line shown (grep -o prints line number and the matched text).

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F 'webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order'
140:webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order
```

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F 'deferred to pre-live (Block 4–5)'
140:deferred to pre-live (Block 4–5)
```

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F 'n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live'
133:n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live
```

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F '## 2026-07-15 — Block 1 milestone — trader sign-off'
174:## 2026-07-15 — Block 1 milestone — trader sign-off
```

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F 'verified-as-DEFERRED (D-2026-07-09-D)'
175:verified-as-DEFERRED (D-2026-07-09-D)
```

Claim: the two double-quoted rubric strings occur verbatim in HEAD specs/SPEC_RUBRIC.md.

```text
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -o -F '## OPEN — gradeable now'
99:## OPEN — gradeable now
```

```text
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -o -F '### O3 — Block-1 milestone scope statement'
109:### O3 — Block-1 milestone scope statement
```

Claim: HEAD lines 133, 140, 174 and 175 are the heading of D-2026-07-09-D, its Decision paragraph, the sign-off heading and the sign-off body (full lines):

```text
$ git show HEAD:DECISIONS.md | sed -n '133p;140p;174p;175p'
## D-2026-07-09-D — n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live
For Block-1 build-first (sim data), **n8n runs locally on the Mac**, not on a remote internet-facing VPS. The signal path is built and proven end-to-end using **test webhook posts** driven locally (as Step 0.8 did against `/tmp`): webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order. The question of how live TradingView (public internet) signals reach the system — **rent a VPS + WireGuard** vs **a tunnel relay (e.g. Cloudflare Tunnel)** — is **deferred to pre-live (Block 4–5)** when live signal ingress is actually exercised.
## 2026-07-15 — Block 1 milestone — trader sign-off
Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15, in-session (AskUserQuestion record) + Google Sheets row (clipboard-delivered). Basis: independent evidence audit docs/reports/2026-07-15-block1-milestone-audit.md (commit d405125) — B1-0/b/c/d/e/f VERIFIED, B1-a verified-as-DEFERRED (D-2026-07-09-D), B1-f T1-T4 all PASS with the standing bracket TRADER-CONFIRMED in the NT8 GUI. Known-open items carried into Block 2 with eyes open: btb P2 (trader chose post-milestone, next-session dispatch), 10i P2, 518/01h/qxd P3, 6h7 P4. Block 2 (Backtesting) entry condition now satisfied.
```

Claim: HEAD :139 is the Decision label line, so :140 is the body of the Decision paragraph:

```text
$ git show HEAD:DECISIONS.md | sed -n '139p'
**Decision:**
```

Claim: the DECISION_LOG time the entry cites (2026-11-12T17:31Z) is present in HEAD DECISION_LOG.md (count of lines):

```text
$ git show HEAD:DECISION_LOG.md | grep -c -F '2026-11-12T17:31'
1
```

The row itself (full line), showing it records the master's D1 decision to append D-2026-11-12-C:

```text
$ git show HEAD:DECISION_LOG.md | grep -n -F '2026-11-12T17:31'
879:- [2026-11-12T17:31:00Z] WHO: praxis-master | WHAT: **Unit 2 dispatched: rubric O3, Block 1 milestone scope statement.** Rubric O3 (re-read this run, `specs/SPEC_RUBRIC.md` "## OPEN — gradeable now"): "Block 1 was signed off as the signal path proven end-to-end. Deviation G defers public ingress to Blocks 4–5, untested. **Required:** one line in DECISIONS.md recording that the Block 1 milestone covers the internal path only." Sources: Deviation G = D-2026-07-09-D (DECISIONS.md :133); the sign-off = "2026-07-15 — Block 1 milestone — trader sign-off" (DECISIONS.md :173–175). **Decided by master under D-2026-11-08-D D1, changeable by Amear:** (1) a new entry D-2026-11-12-C (the id D-2026-11-12-B is taken by the parked `ckh` entry in the working tree) appended at the end of DECISIONS.md, carrying the one required line plus its sources, and stating it records scope and makes no design choice, adds no test, and does not re-open or re-grade the Block 1 sign-off; (2) the committed DECISIONS.md blob = HEAD DECISIONS.md plus the new entry only; the parked `ckh` entry (working tree :2279–2370) stays out; (3) MANIFEST rows for the entry and the unit reports; (4) rubric O3's move to PASSED is NOT in this unit: it follows in the close flush under A11 + D1 after the entry lands, citing the landing sha. | WHY: rubric O3; D1 | WHERE: DECISIONS.md, MANIFEST.md, docs/reports | WHEN: 17:31Z | HOW: praxis-manager foreground | STATE: open
```

Claim: the entry's straight double-quoted strings are exactly these (every match in lines 2371–2387, one per line):

```text
$ sed -n '2371,2387p' DECISIONS.md | grep -o '"[^"]*"'
"webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"
"deferred to pre-live (Block 4–5)"
"n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live"
"## 2026-07-15 — Block 1 milestone — trader sign-off"
"verified-as-DEFERRED (D-2026-07-09-D)"
"## OPEN — gradeable now"
"### O3 — Block-1 milestone scope statement"
"Webhook->validate->file write (/tmp/praxis-signals on n8n host)"
"When Block 1’s milestone is hit, Block 2 starts. Not before."
"fire a fake signal from TradingView"
```

Claim: the three quotes on line 2385 occur verbatim in the HEAD sources the entry cites (full matching lines with line numbers): the body of commit 2582531, and the Phase 3 build spec at :180 and :60:

```text
$ git log -1 --format=%b 2582531 | grep -n -F 'Webhook->validate->file write (/tmp/praxis-signals on n8n host)'
1:Webhook->validate->file write (/tmp/praxis-signals on n8n host)->200->Telegram, plus 400-reject path, verified live twice (implementer + auditor). 3 workflow defects fixed en route. Local-Mac delivery = Block 1.
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | grep -n -F 'When Block 1’s milestone is hit, Block 2 starts. Not before.'
180:Timelines with dates. You named it: the education component means you don’t know how long each block takes. Milestones, not deadlines. When Block 1’s milestone is hit, Block 2 starts. Not before.
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | grep -n -F 'fire a fake signal from TradingView'
60:Milestone: You can fire a fake signal from TradingView, watch it flow through n8n, appear as a file in NinjaTrader’s watched directory, get parsed by your NinjaScript add-on, and receive a Telegram confirmation — all without touching anything manually. That’s the proof of concept. Zero subscriptions. Zero cost beyond your existing infrastructure.
```

Apostrophe byte check: the apostrophe in the pattern below is U+2019 (bytes e28099); the phrase with it occurs once in the HEAD spec and once on line 2385, and the same phrase with an ASCII apostrophe occurs on neither:

```text
$ printf '%s' '’' | xxd -p
e28099
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F 'When Block 1’s milestone'
1
```

```text
$ sed -n '2385p' DECISIONS.md | grep -c -F 'When Block 1’s milestone'
1
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | grep -c -F "When Block 1's milestone"; sed -n '2385p' DECISIONS.md | grep -c -F "When Block 1's milestone"
0
0
```

## E3 rubric O3 text present at HEAD

```text
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F '### O3 — Block-1 milestone scope statement'
109:### O3 — Block-1 milestone scope statement
```

```text
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F '**Required:** one line in DECISIONS.md'
111:public ingress to Blocks 4–5, untested. **Required:** one line in DECISIONS.md
```

```text
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '109,112p'
### O3 — Block-1 milestone scope statement
Block 1 was signed off as the signal path proven end-to-end. Deviation G defers
public ingress to Blocks 4–5, untested. **Required:** one line in DECISIONS.md
recording that the Block 1 milestone covers the internal path only.
```

```text
$ git diff --quiet HEAD -- specs/SPEC_RUBRIC.md; echo exit=$?
exit=0
```

## E4 cross-reference

Claim: HEAD line 112 of the live-signal topology doc says Deviation G's ingress question leaves the anchor's live path (full line):

```text
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '112p'
This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).
```

Claim: the decision id the entry gives the topology doc, D-2026-11-10-B, is the HEAD DECISIONS.md entry that adopts that topology (full heading line), and HEAD DECISIONS.md names the doc path at the line numbers shown. The doc itself does not carry the id (count 0):

```text
$ git show HEAD:DECISIONS.md | sed -n '2047p'
## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
```

```text
$ git show HEAD:DECISIONS.md | grep -n -o -F 'docs/specs/2026-11-10-live-signal-topology.md'
2050:docs/specs/2026-11-10-live-signal-topology.md
2155:docs/specs/2026-11-10-live-signal-topology.md
```

```text
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -c -F 'D-2026-11-10-B'
0
```

## S6 cross-block check

The entry's S6 paragraph (line 2385, full line under Entry edit log, Edit 5) names Block 0, Block 1, Block 2, Blocks 4 and 5, and rubric F1 / the live-signal topology, and records one conflict. One bullet per touched area; each pastes the source of that clause.

- Block 0. Step 0.8 is commit 2582531 (one log line); line 1 of its body holds the phrase the entry quotes; the entry states that nothing in Block 0 is re-graded (phrase on line 2385):

```text
$ git log -1 --format='%h %ad %s' --date=short 2582531
2582531 2026-07-08 Praxis_build-v5h: Step 0.8 Block 0 full-loop verification PASSED
```

```text
$ git log -1 --format=%b 2582531 | sed -n '1p'
Webhook->validate->file write (/tmp/praxis-signals on n8n host)->200->Telegram, plus 400-reject path, verified live twice (implementer + auditor). 3 workflow defects fixed en route. Local-Mac delivery = Block 1.
```

```text
$ sed -n '2385p' DECISIONS.md | grep -o -F 'nothing in Block 0 is re-graded'
nothing in Block 0 is re-graded
```

- Block 1. The 2026-07-15 sign-off, HEAD DECISIONS.md :174 and :175 (full lines):

```text
$ git show HEAD:DECISIONS.md | sed -n '174p;175p'
## 2026-07-15 — Block 1 milestone — trader sign-off
Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15, in-session (AskUserQuestion record) + Google Sheets row (clipboard-delivered). Basis: independent evidence audit docs/reports/2026-07-15-block1-milestone-audit.md (commit d405125) — B1-0/b/c/d/e/f VERIFIED, B1-a verified-as-DEFERRED (D-2026-07-09-D), B1-f T1-T4 all PASS with the standing bracket TRADER-CONFIRMED in the NT8 GUI. Known-open items carried into Block 2 with eyes open: btb P2 (trader chose post-milestone, next-session dispatch), 10i P2, 518/01h/qxd P3, 6h7 P4. Block 2 (Backtesting) entry condition now satisfied.
```

- Block 2. In the HEAD Phase 3 build spec, line 46 is the Block 1 heading, lines 47–59 hold no heading line (count 0), and lines 60 and 180 are the Block 1 milestone and the Block 2 start condition (full lines). The sign-off body at HEAD DECISIONS.md :175 says the Block 2 entry condition is satisfied:

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '46p'
### Block 1: Foundation (No Subscription Required)
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '47,59p' | grep -c -E '^#|^(=+|-+)$'
0
```

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '60p;180p'
Milestone: You can fire a fake signal from TradingView, watch it flow through n8n, appear as a file in NinjaTrader’s watched directory, get parsed by your NinjaScript add-on, and receive a Telegram confirmation — all without touching anything manually. That’s the proof of concept. Zero subscriptions. Zero cost beyond your existing infrastructure.
Timelines with dates. You named it: the education component means you don’t know how long each block takes. Milestones, not deadlines. When Block 1’s milestone is hit, Block 2 starts. Not before.
```

```text
$ git show HEAD:DECISIONS.md | sed -n '175p' | grep -o -F 'Block 2 (Backtesting) entry condition now satisfied'
Block 2 (Backtesting) entry condition now satisfied
```

- Blocks 4 and 5. HEAD DECISIONS.md :140 and :143 (full lines):

```text
$ git show HEAD:DECISIONS.md | sed -n '140p;143p'
For Block-1 build-first (sim data), **n8n runs locally on the Mac**, not on a remote internet-facing VPS. The signal path is built and proven end-to-end using **test webhook posts** driven locally (as Step 0.8 did against `/tmp`): webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order. The question of how live TradingView (public internet) signals reach the system — **rent a VPS + WireGuard** vs **a tunnel relay (e.g. Cloudflare Tunnel)** — is **deferred to pre-live (Block 4–5)** when live signal ingress is actually exercised.
- **Build-first discipline (D-2026-07-04-A).** Block 1 builds the smallest complete path on sim data. Public TradingView ingress is not exercised by sim; standing up a remote VPS + WireGuard now is premature infrastructure — real monthly cost and a public Linux box to secure/patch for a capability the sim phase doesn't use.
```

- Rubric F1 / the live-signal topology. HEAD topology doc :112 (full line):

```text
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '112p'
This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).
```

- The one conflict, recorded, not resolved. Spec :60 (pasted above) contains 'fire a fake signal from TradingView'. The sign-off body at :175 records B1-a as verified-as-DEFERRED, citing D-2026-07-09-D, whose :140 (pasted above) defers the question of how live TradingView signals reach the system to pre-live (Block 4–5). The sign-off body says the Block 2 entry condition is satisfied, and spec :180 starts Block 2 when Block 1's milestone is hit (both pasted above). The entry records the gap and does not resolve it (phrases on line 2385):

```text
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '60p' | grep -o -F 'fire a fake signal from TradingView'
fire a fake signal from TradingView
```

```text
$ git show HEAD:DECISIONS.md | sed -n '175p' | grep -o -F 'B1-a verified-as-DEFERRED (D-2026-07-09-D)'
B1-a verified-as-DEFERRED (D-2026-07-09-D)
```

```text
$ git show HEAD:DECISIONS.md | sed -n '140p' | grep -o -F 'The question of how live TradingView (public internet) signals reach the system'
The question of how live TradingView (public internet) signals reach the system
```

```text
$ git show HEAD:DECISIONS.md | sed -n '140p' | grep -o -F 'is **deferred to pre-live (Block 4–5)**'
is **deferred to pre-live (Block 4–5)**
```

```text
$ sed -n '2385p' DECISIONS.md | grep -o -F 'One conflict, recorded, not resolved'
One conflict, recorded, not resolved
```

```text
$ sed -n '2385p' DECISIONS.md | grep -o -F 'it does not re-grade the sign-off, re-open Block 1 or stop Block 2'
it does not re-grade the sign-off, re-open Block 1 or stop Block 2
```

## S2 statement

The entry records scope only; it claims no component at any level beyond what its HEAD sources already state. Its Limits paragraph (full line):

```text
$ sed -n '2383p' DECISIONS.md
**Limits.** This entry records scope only. It makes no design choice, adds no test, and does not re-open or re-grade the 2026-07-15 sign-off. It does not change rubric O3's state; that move is a later master step. It does not decide where public ingress goes. Cross-reference only: `docs/specs/2026-11-10-live-signal-topology.md` (D-2026-11-10-B) :112 already says Deviation G's ingress question leaves the anchor's live path; this entry adds nothing to it.
```

Every level word in the entry (specified, implemented, tested, untested, and verified with any suffix) with its line number within the entry:

```text
$ sed -n '2371,2387p' DECISIONS.md > /tmp/o3e-entry.md; grep -n -o -i -E 'untested|tested|implemented|specified|verified[-A-Za-z]*' /tmp/o3e-entry.md
6:untested
10:verified-as-DEFERRED
```

The only level words are 'untested' (public TradingView ingress; the rubric's own word at HEAD :111, pasted in E3) and 'verified-as-DEFERRED' (quoted from the HEAD sign-off body at :175, pasted in E2). Neither raises any component above its source.

## Entry edit log

Five edits to entry D-2026-11-12-C, in order. Edit 1 is the first pass's pointer edit, kept as recorded. Edits 2 and 3 are cure round 2. Edits 4 and 5 are cure round 3. The texts of lines 2376 and 2385 after cure round 2 are in /tmp/o3e-r3-old-2376.txt and /tmp/o3e-r3-old-2385.txt (each equal to that line of /tmp/o3e-pre-cure3-DECISIONS.md, cmp under Edits 4 and 5); the blocks under Edits 2 and 3 and Whole-file compare (cure round 2) read those captures and copies.

### Edit 1: S6 evidence pointer (line 2385, first pass)

Old line 2385, captured to /tmp/o3e-old-2385.txt before the edit (full line):

```text
$ cat /tmp/o3e-old-2385.txt
**S6 cross-block.** Touches Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-manager.md` (S6 section).
```

Line 2385 after edit 1 and before cure round 2, captured to /tmp/o3e-old-2385b.txt (full line):

```text
$ cat /tmp/o3e-old-2385b.txt
**S6 cross-block.** Touches Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

Claim: the two differ only by the substituted path (reverting the path reproduces the captured old line byte-for-byte):

```text
$ sed 's#2026-11-12-o3-block1-scope-evidence.md#2026-11-12-o3-block1-scope-manager.md#' /tmp/o3e-old-2385b.txt | cmp - /tmp/o3e-old-2385.txt; echo exit=$?
exit=0
```

Entry sha256 (lines 2371–2387) captured before edit 1 (last line of the capture file), and re-derived by reverting the path on entry line 15 (file line 2385) of the pre-cure-2 whole-file copy:

```text
$ tail -n 1 /tmp/o3-pre.txt
7d8f6577dfe6e75fdeb42158ff33e1e3ab29da864d839f16c918360132ed0653  -
```

```text
$ sed -n '2371,2387p' /tmp/o3e-pre-cure2-DECISIONS.md | sed '15s#2026-11-12-o3-block1-scope-evidence.md#2026-11-12-o3-block1-scope-manager.md#' | shasum -a 256
7d8f6577dfe6e75fdeb42158ff33e1e3ab29da864d839f16c918360132ed0653  -
```

Entry sha256 after edit 1, which is also the value before cure round 2 (from the whole-file copy):

```text
$ sed -n '2371,2387p' /tmp/o3e-pre-cure2-DECISIONS.md | shasum -a 256
29d3cbb57d95787318e73eff306167aaebf3d000a8a078e7e128a7d812dbae3e  -
```

### Edit 2: scope-line sentence (line 2376, cure round 2)

Old paragraph, captured to /tmp/o3e-old-2376.txt before the edit (full line):

```text
$ cat /tmp/o3e-old-2376.txt
**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).
```

New paragraph after cure round 2 (capture /tmp/o3e-r3-old-2376.txt, full line):

```text
$ cat /tmp/o3e-r3-old-2376.txt
**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3). Block 0's Step 0.8 (commit `2582531`, 2026-07-08) posted a test payload by curl to a webhook on a remote public host whose n8n wrote to a directory on that host; it ran before the local path existed and was not TradingView ingress into it (D-2026-07-09-D :140, "as Step 0.8 did against `/tmp`").
```

Claim: the new line is the old line with one sentence appended (cutting from ' Block 0' plus 's Step 0.8 (commit ' to the end reproduces the old line byte-for-byte), and 'is untested' stays:

```text
$ sed -E 's/ Block 0.s Step 0\.8 \(commit .*$//' /tmp/o3e-r3-old-2376.txt | cmp - /tmp/o3e-old-2376.txt; echo exit=$?
exit=0
```

```text
$ grep -o -F 'and is untested (rubric O3).' /tmp/o3e-r3-old-2376.txt
and is untested (rubric O3).
```

### Edit 3: Block 0 in the S6 paragraph (line 2385, cure round 2)

Old paragraph: /tmp/o3e-old-2385b.txt, pasted in full under Edit 1. New paragraph after cure round 2 (capture /tmp/o3e-r3-old-2385.txt, full line):

```text
$ cat /tmp/o3e-r3-old-2385.txt
**S6 cross-block.** Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

Claim: the only change is the inserted Block 0 clause (reverting it reproduces the old line byte-for-byte), and the Evidence pointer is unchanged:

```text
$ sed 's/Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (/Touches Block 1 (/' /tmp/o3e-r3-old-2385.txt | cmp - /tmp/o3e-old-2385b.txt; echo exit=$?
exit=0
```

```text
$ grep -o -F 'Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).' /tmp/o3e-r3-old-2385.txt
Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

### Whole-file compare (cure round 2)

On the whole-file copies taken before cure round 2 and before cure round 3: the line count of the later copy, the full diff between them (only 2376c2376 and 2385c2385), and a byte compare of every line before the first edited line (1–2375, which includes the parked lines 2279–2370):

```text
$ wc -l < /tmp/o3e-pre-cure3-DECISIONS.md
    2387
```

```text
$ diff /tmp/o3e-pre-cure2-DECISIONS.md /tmp/o3e-pre-cure3-DECISIONS.md
2376c2376
< **Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).
---
> **Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3). Block 0's Step 0.8 (commit `2582531`, 2026-07-08) posted a test payload by curl to a webhook on a remote public host whose n8n wrote to a directory on that host; it ran before the local path existed and was not TradingView ingress into it (D-2026-07-09-D :140, "as Step 0.8 did against `/tmp`").
2385c2385
< **S6 cross-block.** Touches Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
---
> **S6 cross-block.** Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

```text
$ head -n 2375 /tmp/o3e-pre-cure3-DECISIONS.md | cmp - <(head -n 2375 /tmp/o3e-pre-cure2-DECISIONS.md); echo exit=$?
exit=0
```

Entry boundaries in the working tree now: lines 2370 (the parked entry's last line) and 2387 are each the standing limitation sentence (count 2), line 2371 is empty (1 byte), and there is no line 2388 (0 bytes):

```text
$ sed -n '2370p;2387p' DECISIONS.md | grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
2
```

```text
$ sed -n '2371p' DECISIONS.md | wc -c; sed -n '2388p' DECISIONS.md | wc -c
       1
       0
```

Entry sha256 (lines 2371–2387) before and after cure round 2 (the after value from the copy taken before cure round 3):

```text
$ sed -n '2371,2387p' /tmp/o3e-pre-cure2-DECISIONS.md | shasum -a 256; sed -n '2371,2387p' /tmp/o3e-pre-cure3-DECISIONS.md | shasum -a 256
29d3cbb57d95787318e73eff306167aaebf3d000a8a078e7e128a7d812dbae3e  -
7d35623d9f12861463cc5cdd2e34fb931043c7dd859ba07e115764bdd6349871  -
```

```text
$ git diff --numstat HEAD -- DECISIONS.md
109	0	DECISIONS.md
```

### Edit 4: scope line restored (line 2376, cure round 3)

Old line 2376 (the cure-round-2 text), captured to /tmp/o3e-r3-old-2376.txt before cure round 3, full line, then a compare with line 2376 of /tmp/o3e-pre-cure3-DECISIONS.md:

```text
$ cat /tmp/o3e-r3-old-2376.txt
**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3). Block 0's Step 0.8 (commit `2582531`, 2026-07-08) posted a test payload by curl to a webhook on a remote public host whose n8n wrote to a directory on that host; it ran before the local path existed and was not TradingView ingress into it (D-2026-07-09-D :140, "as Step 0.8 did against `/tmp`").
```

```text
$ sed -n '2376p' /tmp/o3e-pre-cure3-DECISIONS.md | cmp - /tmp/o3e-r3-old-2376.txt; echo exit=$?
exit=0
```

New line 2376 (full line):

```text
$ sed -n '2376p' DECISIONS.md
**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).
```

Claim: the new line is byte-identical to the pre-cure-2 capture /tmp/o3e-old-2376.txt, to line 2376 of /tmp/o3e-pre-cure2-DECISIONS.md, and to the old line pasted in this report under Edit 2 (extracted from this file by awk: its byte count, then the compare):

```text
$ sed -n '2376p' DECISIONS.md | cmp - /tmp/o3e-old-2376.txt; echo exit=$?
exit=0
```

```text
$ sed -n '2376p' DECISIONS.md | cmp - <(sed -n '2376p' /tmp/o3e-pre-cure2-DECISIONS.md); echo exit=$?
exit=0
```

```text
$ awk 'p{print; exit} $0=="$ cat /tmp/o3e-old-2376.txt"{p=1}' docs/reports/2026-11-12-o3-block1-scope-evidence.md | wc -c
     447
```

```text
$ awk 'p{print; exit} $0=="$ cat /tmp/o3e-old-2376.txt"{p=1}' docs/reports/2026-11-12-o3-block1-scope-evidence.md | cmp - <(sed -n '2376p' DECISIONS.md); echo exit=$?
exit=0
```

The cure-round-2 sentence's quote from :140 is no longer in the entry (count 0):

```text
$ sed -n '2371,2387p' DECISIONS.md | grep -c -F 'as Step 0.8 did against'
0
```

### Edit 5: S6 paragraph rewritten (line 2385, cure round 3)

Old line 2385 (the cure-round-2 text), captured to /tmp/o3e-r3-old-2385.txt before cure round 3, full line, then a compare with line 2385 of /tmp/o3e-pre-cure3-DECISIONS.md:

```text
$ cat /tmp/o3e-r3-old-2385.txt
**S6 cross-block.** Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (states the reach of the sign-off; its basis and evidence are unchanged), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved or decided there) and rubric F1 / the live-signal topology (:112, cross-reference only). Conflicts with none: it restates the split D-2026-07-09-D already makes between the local path and the deferred ingress, and the sign-off itself cites D-2026-07-09-D for B1-a. Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

```text
$ sed -n '2385p' /tmp/o3e-pre-cure3-DECISIONS.md | cmp - /tmp/o3e-r3-old-2385.txt; echo exit=$?
exit=0
```

New line 2385 (full line), then a compare with the master's text in /tmp/o3e-r3-new-2385.txt, and the Evidence pointer, unchanged:

```text
$ sed -n '2385p' DECISIONS.md
**S6 cross-block.** Touches Block 0 (Step 0.8, commit `2582531`, whose body records "Webhook->validate->file write (/tmp/praxis-signals on n8n host)"; nothing in Block 0 is re-graded), Block 1 (the reach of the 2026-07-15 sign-off), Block 2 (`docs/specs/2026-11-05-phase3-build-specification.md` :180, "When Block 1’s milestone is hit, Block 2 starts. Not before."), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved there) and rubric F1 / the live-signal topology `docs/specs/2026-11-10-live-signal-topology.md` (:112, cross-reference only). One conflict, recorded, not resolved: the Phase 3 spec's Block 1 milestone (:60, "fire a fake signal from TradingView") includes TradingView ingress; the milestone signed off on 2026-07-15 did not; Block 2 started on that sign-off (:180). This entry records the gap; it does not re-grade the sign-off, re-open Block 1 or stop Block 2 (decided by master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:41Z, changeable by Amear). Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

```text
$ sed -n '2385p' DECISIONS.md | cmp - /tmp/o3e-r3-new-2385.txt; echo exit=$?
exit=0
```

```text
$ sed -n '2385p' DECISIONS.md | grep -o -F 'Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).'
Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).
```

### Whole-file compare (cure round 3)

The changed-line headers of the diff against /tmp/o3e-pre-cure3-DECISIONS.md (only 2376c2376 and 2385c2385), the line count, line 2372 (the entry heading) and line 2387 (the standing limitation sentence, by count), so the entry still spans lines 2371–2387:

```text
$ diff /tmp/o3e-pre-cure3-DECISIONS.md DECISIONS.md | grep -E '^[0-9]'
2376c2376
2385c2385
```

```text
$ wc -l DECISIONS.md
    2387 DECISIONS.md
```

```text
$ sed -n '2372p' DECISIONS.md
## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)
```

```text
$ sed -n '2387p' DECISIONS.md | grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
```

Entry sha256 (lines 2371–2387) before cure round 3 (from the copy) and now:

```text
$ sed -n '2371,2387p' /tmp/o3e-pre-cure3-DECISIONS.md | shasum -a 256; sed -n '2371,2387p' DECISIONS.md | shasum -a 256
7d35623d9f12861463cc5cdd2e34fb931043c7dd859ba07e115764bdd6349871  -
382e091b669a5b97ef907ccfe9114985f7d693f5bb1feb046560b485d2e6b5ea  -
```

## MANIFEST row

The DECISIONS.md amendment row (working-tree line 459, full line):

```text
$ sed -n '459p' MANIFEST.md
| /DECISIONS.md | Log | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry). Unit 2026-11-12-o3-block1-scope (rubric O3; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:31:00Z): appends entry D-2026-11-12-C, "Block 1 milestone scope — internal path only", recording that the Block 1 milestone signed off on 2026-07-15 covers the internal path only and that public TradingView ingress (Deviation G, D-2026-07-09-D) is deferred and untested. Scope record only: no design choice, no test, no re-grade of the sign-off, rubric O3 state unchanged. |
```

The row for this report as it was before cure round 2 (captured to /tmp/o3e-old-manifest-last.txt, full line):

```text
$ cat /tmp/o3e-old-manifest-last.txt
| /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path, before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
```

The row after cure round 2 (last line of the copy taken before cure round 3, full):

```text
$ tail -n 1 /tmp/o3e-pre-cure3-MANIFEST.md
| /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z and 2026-11-12T21:25:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path and the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph), before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
```

Claim: cure round 2 changed only the last line of MANIFEST.md (diff between the copies taken before cure round 2 and before cure round 3, and a byte compare of lines 1–465), the line count is unchanged, and the row starts a line of its own (count on the working tree):

```text
$ diff /tmp/o3e-pre-cure2-MANIFEST.md /tmp/o3e-pre-cure3-MANIFEST.md
466c466
< | /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path, before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
---
> | /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z and 2026-11-12T21:25:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path and the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph), before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
```

```text
$ head -n 465 /tmp/o3e-pre-cure3-MANIFEST.md | cmp - <(head -n 465 /tmp/o3e-pre-cure2-MANIFEST.md); echo exit=$?
exit=0
```

```text
$ wc -l < /tmp/o3e-pre-cure3-MANIFEST.md; wc -l < /tmp/o3e-pre-cure2-MANIFEST.md
     466
     466
```

```text
$ grep -c '^| /docs/reports/2026-11-12-o3-block1-scope-evidence.md |' MANIFEST.md
1
```

Cure round 3 rewrote the same row once more (Process log item 9; the old text is the row after cure round 2, above). The row now (last line, full), the diff against the copy taken before cure round 3, a byte compare of lines 1–465, and the line counts:

```text
$ tail -n 1 MANIFEST.md
| /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z, 2026-11-12T21:25:00Z and 2026-11-12T21:41:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path, the two cure-round-2 entry edits and the two cure-round-3 entry edits (scope line restored to its pre-cure-2 text; S6 paragraph rewritten to name Blocks 0, 1, 2, 4 and 5 and F1 and to record one conflict, not resolved), before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
```

```text
$ diff /tmp/o3e-pre-cure3-MANIFEST.md MANIFEST.md
466c466
< | /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z and 2026-11-12T21:25:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path and the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph), before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
---
> | /docs/reports/2026-11-12-o3-block1-scope-evidence.md | Report | 3 | 2026-11-12 | Evidence report for unit 2026-11-12-o3-evidence (rubric O3, bead Praxis_build-p3l; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:04:00Z, 2026-11-12T21:25:00Z and 2026-11-12T21:41:00Z): pasted command output for entry D-2026-11-12-C (candidate DECISIONS.md commit blob prefix check, quote greps at HEAD, rubric O3 text at HEAD, topology cross-reference, S6 cross-block check), the one-pointer edit to the entry S6 evidence path, the two cure-round-2 entry edits and the two cure-round-3 entry edits (scope line restored to its pre-cure-2 text; S6 paragraph rewritten to name Blocks 0, 1, 2, 4 and 5 and F1 and to record one conflict, not resolved), before and after hashes of the six earlier O3 reports (unedited, uncommitted), de-identification counts, adversary grade line. |
```

```text
$ head -n 465 MANIFEST.md | cmp - <(head -n 465 /tmp/o3e-pre-cure3-MANIFEST.md); echo exit=$?
exit=0
```

```text
$ wc -l < MANIFEST.md; wc -l < /tmp/o3e-pre-cure3-MANIFEST.md
     466
     466
```

Claim: the candidate MANIFEST commit blob (HEAD plus those two rows) has 446 lines and starts with HEAD byte-for-byte:

```text
$ { git show HEAD:MANIFEST.md; sed -n '459p' MANIFEST.md; tail -n 1 MANIFEST.md; } | wc -l
     446
```

```text
$ { git show HEAD:MANIFEST.md; sed -n '459p' MANIFEST.md; tail -n 1 MANIFEST.md; } > /tmp/o3e-manifest-blob.md; wc -l < /tmp/o3e-manifest-blob.md
     446
```

```text
$ git show HEAD:MANIFEST.md > /tmp/o3e-head-manifest.md; wc -l < /tmp/o3e-head-manifest.md
     444
```

```text
$ head -n 444 /tmp/o3e-manifest-blob.md | cmp - /tmp/o3e-head-manifest.md; echo exit=$?
exit=0
```

```text
$ shasum -a 256 /tmp/o3e-manifest-blob.md
8262f7d660f25d96c74b5d8e643ae128202fc51562084da5fd7fcb3be1653e0f  /tmp/o3e-manifest-blob.md
```

## Untouched files

The six earlier O3 reports stay on disk, unedited, unstaged and uncommitted:

- docs/reports/2026-11-12-o3-block1-scope-manager.md

- docs/reports/2026-11-12-o3-block1-scope-worker1.md

- docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md

- docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md

- docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md

- docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md

Before (first six lines of the capture file written before the pointer edit):

```text
$ head -n 6 /tmp/o3-pre.txt
56d46a4fc48687d33e08069bdeee2f0985aee240e22d75b7806d8e226b364554  docs/reports/2026-11-12-o3-block1-scope-manager.md
2d6c6fe63a300b4d36da5edb57cd5c65fcc2b323a0fcb31fbb21242bdaa542d5  docs/reports/2026-11-12-o3-block1-scope-worker1.md
6fef755764f0ddb7c7ae72024072ff3fe67efbe002ba4b2d4a38af1b4902b587  docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
06d0d6675fb0dd9f910d2477af5c141e14d086cdfc7f98147624e423b541845b  docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md
8a1016facb06dc26fd207f1222896654cdf65eb2c91a90cf8b35a675a81a9850  docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md
a478e7064c5ed111e7b79515dc8017c8040e79e798d44234445043ec55254dae  docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md
```

After (re-hashed now, compared with the capture):

```text
$ shasum -a 256 docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md > /tmp/o3e-post.txt; head -n 6 /tmp/o3-pre.txt | cmp - /tmp/o3e-post.txt; echo exit=$?
exit=0
```

Claim: the re-hashed values equal the values pasted above under Before (the pasted lines are extracted from this file by awk: line count, then the compare with the re-hash):

```text
$ awk 'p&&/^```/{exit} p{print} $0=="$ head -n 6 /tmp/o3-pre.txt"{p=1}' docs/reports/2026-11-12-o3-block1-scope-evidence.md | wc -l
       6
```

```text
$ awk 'p&&/^```/{exit} p{print} $0=="$ head -n 6 /tmp/o3-pre.txt"{p=1}' docs/reports/2026-11-12-o3-block1-scope-evidence.md | cmp - /tmp/o3e-post.txt; echo exit=$?
exit=0
```

Claim: none of the six is tracked by git (so none is committed) and none is staged (counts):

```text
$ git ls-files -- docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md | wc -l
       0
```

```text
$ git diff --cached --numstat -- docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md | wc -l
       0
```

Parked lines 2279–2370 (unit ckh): byte-identical to the pre-cure-2 whole-file copy, and the parked entry id is not at HEAD (count 0); E1 shows the working tree minus those lines equals HEAD plus the entry:

```text
$ sed -n '2279,2370p' DECISIONS.md | cmp - <(sed -n '2279,2370p' /tmp/o3e-pre-cure2-DECISIONS.md); echo exit=$?
exit=0
```

```text
$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'
0
```

## De-identification

Scanned: the entry (lines 2371–2387, in /tmp/o3e-entry.md, re-extracted fresh below), this report, and the two MANIFEST rows (line 459 and the last line). Only counts are printed. The support rep's first name is derived by script from the one staged path and is never printed; the byte count (printed without a newline) shows it is non-empty. The medication pattern list is in /tmp/o3e-med.txt and is not printed; its line count shows it is non-empty. The public host name is derived by script from HEAD HANDOFF.md :2011 and is never printed; its byte count shows it is non-empty. This report is one of the scanned files, so it must contain none of these strings.

```text
$ sed -n '2371,2387p' DECISIONS.md > /tmp/o3e-entry.md; wc -l < /tmp/o3e-entry.md
      17
```

```text
$ { sed -n '459p' MANIFEST.md; tail -n 1 MANIFEST.md; } > /tmp/o3e-manifest-rows.md; wc -l < /tmp/o3e-manifest-rows.md
       2
```

```text
$ REP=$(git diff --cached --name-only | sed -E 's#^.*/##; s/^[0-9]{4}-[0-9]{2}-[0-9]{2}-mffu-//; s/-reply\.png$//'); printf '%s' "$REP" | wc -c
       4
```

```text
$ wc -l < /tmp/o3e-med.txt
      88
```

```text
$ H=$(git show HEAD:HANDOFF.md | sed -n '2011p' | grep -o -E 'https://[^/ `]+' | head -n 1 | sed 's#https://##'); printf '%s' "$H" | wc -c
      19
```

Claim: there is exactly one staged path (count only):

```text
$ git diff --cached --name-only | wc -l
       1
```

Support rep first name (case-insensitive, fixed string):

```text
$ REP=$(git diff --cached --name-only | sed -E 's#^.*/##; s/^[0-9]{4}-[0-9]{2}-[0-9]{2}-mffu-//; s/-reply\.png$//'); for f in /tmp/o3e-entry.md docs/reports/2026-11-12-o3-block1-scope-evidence.md /tmp/o3e-manifest-rows.md; do printf '%s ' "$f"; grep -c -i -F "$REP" "$f"; done
/tmp/o3e-entry.md 0
docs/reports/2026-11-12-o3-block1-scope-evidence.md 0
/tmp/o3e-manifest-rows.md 0
```

Email-address pattern:

```text
$ for f in /tmp/o3e-entry.md docs/reports/2026-11-12-o3-block1-scope-evidence.md /tmp/o3e-manifest-rows.md; do printf '%s ' "$f"; grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f"; done
/tmp/o3e-entry.md 0
docs/reports/2026-11-12-o3-block1-scope-evidence.md 0
/tmp/o3e-manifest-rows.md 0
```

Phone-number pattern:

```text
$ for f in /tmp/o3e-entry.md docs/reports/2026-11-12-o3-block1-scope-evidence.md /tmp/o3e-manifest-rows.md; do printf '%s ' "$f"; grep -c -E '(\+?1[-. ]?)?\(?[0-9]{3}\)?[-. ][0-9]{3}[-. ][0-9]{4}' "$f"; done
/tmp/o3e-entry.md 0
docs/reports/2026-11-12-o3-block1-scope-evidence.md 0
/tmp/o3e-manifest-rows.md 0
```

Medication names (whole words, case-insensitive, list from file):

```text
$ for f in /tmp/o3e-entry.md docs/reports/2026-11-12-o3-block1-scope-evidence.md /tmp/o3e-manifest-rows.md; do printf '%s ' "$f"; grep -c -i -w -f /tmp/o3e-med.txt "$f"; done
/tmp/o3e-entry.md 0
docs/reports/2026-11-12-o3-block1-scope-evidence.md 0
/tmp/o3e-manifest-rows.md 0
```

Public host name (case-insensitive, fixed string):

```text
$ H=$(git show HEAD:HANDOFF.md | sed -n '2011p' | grep -o -E 'https://[^/ `]+' | head -n 1 | sed 's#https://##'); for f in /tmp/o3e-entry.md docs/reports/2026-11-12-o3-block1-scope-evidence.md /tmp/o3e-manifest-rows.md; do printf '%s ' "$f"; grep -c -i -F "$H" "$f"; done
/tmp/o3e-entry.md 0
docs/reports/2026-11-12-o3-block1-scope-evidence.md 0
/tmp/o3e-manifest-rows.md 0
```

## Verification evidence (command output)

Key outputs re-run together. Entry sha256 (lines 2371–2387), DECISIONS.md line count, candidate DECISIONS blob line count and sha256, numstat of the two edited tracked files, candidate MANIFEST blob line count:

```text
$ sed -n '2371,2387p' DECISIONS.md | shasum -a 256; wc -l < DECISIONS.md; wc -l < /tmp/o3e-decisions-blob.md; shasum -a 256 /tmp/o3e-decisions-blob.md; git diff --numstat HEAD -- DECISIONS.md MANIFEST.md; wc -l < /tmp/o3e-manifest-blob.md
382e091b669a5b97ef907ccfe9114985f7d693f5bb1feb046560b485d2e6b5ea  -
    2387
    2295
4c17cf4d6f95a7e56a9121b3a7ddfc94396976152d5c3c88e29d113daf037f26  /tmp/o3e-decisions-blob.md
109	0	DECISIONS.md
22	0	MANIFEST.md
     446
```

Report format checks on this file: standalone S13 lines (expect 1), whether the last line is the S13 sentence (expect 1), words that must not appear (list in /tmp/o3e-banned.txt, three lines, case-insensitive), ellipsis strings (list in /tmp/o3e-ellipsis.txt), angle-bracket placeholders, and an even count of fence lines:

```text
$ grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' docs/reports/2026-11-12-o3-block1-scope-evidence.md
1
```

```text
$ tail -n 1 docs/reports/2026-11-12-o3-block1-scope-evidence.md | grep -c -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
1
```

```text
$ wc -l < /tmp/o3e-banned.txt; grep -c -i -f /tmp/o3e-banned.txt docs/reports/2026-11-12-o3-block1-scope-evidence.md
       3
0
```

```text
$ wc -l < /tmp/o3e-ellipsis.txt; grep -c -F -f /tmp/o3e-ellipsis.txt docs/reports/2026-11-12-o3-block1-scope-evidence.md
       2
0
```

```text
$ grep -c -E '<[A-Za-z_-]+>' docs/reports/2026-11-12-o3-block1-scope-evidence.md
0
```

```text
$ grep -c '^```' docs/reports/2026-11-12-o3-block1-scope-evidence.md
340
```

```text
$ grep -c -x -E 'Result:[ ].*' docs/reports/2026-11-12-o3-block1-scope-evidence.md
1
```

## Cure round 2

Adversary 2's five defects (section Adversary), each with the text removed or the gap (Old) and what replaced it (New). Cures 1 to 3 delete or narrow report text only; cures 4 and 5 are the master's entry edits at 21:25:00Z.

1. Pointer-edit limitation (Process log). Old: "on the entry at the same line range hashing to the master's pre-edit value before the edit (Pointer edit log)". New: "on the entry hash captured before that edit (Entry edit log)", plus the added sentence "The cure-round-2 edits were checked by a whole-file before/after compare (Entry edit log, Whole-file compare: diff and cmp)." That compare is pasted under Entry edit log.
2. S6 search sentence. Old: "Within that scope, the only line pairing public or TradingView ingress with a test word is the rubric's own 'untested' line." New: "Both patterns match only the literal string 'tested' near an ingress word on one line; each returns the one line shown." No claim about lines the patterns do not match.
3. Block 0 parts of S6. Old touched-list clause: "Block 0 (through D-2026-07-09-D, which supersedes Block 0's remote-host premise)". New: "Block 0 (its Step 0.8 curl test, which the entry's scope line now names)". Old Block 0 bullet: "Block 0: no conflict. D-2026-07-09-D (HEAD :137, below) supersedes the remote-VPS n8n premise that Block 0 built on, and the topology doc row 1.9 (HEAD :25, below) records that the workflow was once published at a public address in Step 0.5 and grades public ingress UNVERIFIED today. A Block 0 publication of the webhook to a since-superseded remote host is not live TradingView ingress into the local path; the entry says public TradingView ingress is untested, which row 1.9's UNVERIFIED grade does not contradict. The entry makes no claim about Block 0." The two blocks pasted under it (HEAD DECISIONS.md :137 and topology doc :25) are removed. New: the Block 0 bullet in S6, with the 2582531 log line, the HANDOFF.md :2011 count and phrases, the :140 count, the f716d2d log line and host-shape counts pasted under it, and a stated limit on what shows the host is public.
4. Block 0's Step 0.8 not weighed against "is untested". Old: the scope line (line 2376; the brief called it 2375) ended at "and is untested (rubric O3)." New: one sentence appended on line 2376; "is untested" stays. Full old and new lines under Entry edit log, Edit 2.
5. The entry's S6 paragraph did not name Block 0. Old: "Touches Block 1 (". New: "Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (". The Evidence pointer is unchanged. Full old and new lines under Entry edit log, Edits 1 and 3.

## Cure round 3

Under the master's decision at DECISION_LOG 2026-11-12T21:41:00Z (phrases pasted at the top of this report). Each item gives the text removed or the gap (Old) and what replaced it (New).

1. Entry scope line (line 2376). Old: the cure-round-2 sentence that began "Block 0's Step 0.8 (commit `2582531`, 2026-07-08) posted a test payload by curl" and ended with the :140 quote. New: the line is restored byte-for-byte to its pre-cure-2 text. Full old and new lines and the compares under Entry edit log, Edit 4.
2. Entry S6 paragraph (line 2385). Old: the cure-round-2 paragraph, which said "Conflicts with none". New: the master's paragraph naming Block 0, Block 1, Block 2, Blocks 4 and 5 and F1 / the topology, and recording one conflict, not resolved. Full old and new lines under Edit 5.
3. Commands re-pointed, so that historical cure-round-2 records read the captures taken before cure round 3 and their pasted output reproduces (Old command, then New command):
   - Edit 2, new paragraph. Old: `sed -n '2376p' DECISIONS.md`. New: `cat /tmp/o3e-r3-old-2376.txt`.
   - Edit 2, cut check. Old: `sed -n '2376p' DECISIONS.md | sed -E 's/ Block 0.s Step 0\.8 \(commit .*$//' | cmp - /tmp/o3e-old-2376.txt; echo exit=$?`. New: `sed -E 's/ Block 0.s Step 0\.8 \(commit .*$//' /tmp/o3e-r3-old-2376.txt | cmp - /tmp/o3e-old-2376.txt; echo exit=$?`.
   - Edit 2, 'is untested' check. Old: `sed -n '2376p' DECISIONS.md | grep -o -F 'and is untested (rubric O3).'`. New: `grep -o -F 'and is untested (rubric O3).' /tmp/o3e-r3-old-2376.txt`.
   - Edit 3, new paragraph. Old: `sed -n '2385p' DECISIONS.md`. New: `cat /tmp/o3e-r3-old-2385.txt`.
   - Edit 3, revert check. Old: `sed -n '2385p' DECISIONS.md | sed 's/Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (/Touches Block 1 (/' | cmp - /tmp/o3e-old-2385b.txt; echo exit=$?`. New: `sed 's/Touches Block 0 (its Step 0.8 public-host curl test, which the scope line names; nothing in Block 0 is re-graded), Block 1 (/Touches Block 1 (/' /tmp/o3e-r3-old-2385.txt | cmp - /tmp/o3e-old-2385b.txt; echo exit=$?`.
   - Edit 3, Evidence pointer. Old: ``sed -n '2385p' DECISIONS.md | grep -o -F 'Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).'``. New: ``grep -o -F 'Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence.md` (S6 section).' /tmp/o3e-r3-old-2385.txt``.
   - Whole-file compare (cure round 2), line count. Old: `wc -l < DECISIONS.md`. New: `wc -l < /tmp/o3e-pre-cure3-DECISIONS.md`.
   - Whole-file compare (cure round 2), diff. Old: `diff /tmp/o3e-pre-cure2-DECISIONS.md DECISIONS.md`. New: `diff /tmp/o3e-pre-cure2-DECISIONS.md /tmp/o3e-pre-cure3-DECISIONS.md`.
   - Whole-file compare (cure round 2), lines 1–2375. Old: `head -n 2375 DECISIONS.md | cmp - <(head -n 2375 /tmp/o3e-pre-cure2-DECISIONS.md); echo exit=$?`. New: `head -n 2375 /tmp/o3e-pre-cure3-DECISIONS.md | cmp - <(head -n 2375 /tmp/o3e-pre-cure2-DECISIONS.md); echo exit=$?`.
   - Whole-file compare (cure round 2), entry sha256. Old: `sed -n '2371,2387p' /tmp/o3e-pre-cure2-DECISIONS.md | shasum -a 256; sed -n '2371,2387p' DECISIONS.md | shasum -a 256`. New: `sed -n '2371,2387p' /tmp/o3e-pre-cure2-DECISIONS.md | shasum -a 256; sed -n '2371,2387p' /tmp/o3e-pre-cure3-DECISIONS.md | shasum -a 256`.
   - MANIFEST row after cure round 2. Old: `tail -n 1 MANIFEST.md`. New: `tail -n 1 /tmp/o3e-pre-cure3-MANIFEST.md`.
   - MANIFEST cure-round-2 diff. Old: `diff /tmp/o3e-pre-cure2-MANIFEST.md MANIFEST.md`. New: `diff /tmp/o3e-pre-cure2-MANIFEST.md /tmp/o3e-pre-cure3-MANIFEST.md`.
   - MANIFEST cure-round-2 lines 1–465. Old: `head -n 465 MANIFEST.md | cmp - <(head -n 465 /tmp/o3e-pre-cure2-MANIFEST.md); echo exit=$?`. New: `head -n 465 /tmp/o3e-pre-cure3-MANIFEST.md | cmp - <(head -n 465 /tmp/o3e-pre-cure2-MANIFEST.md); echo exit=$?`.
   - MANIFEST cure-round-2 line counts. Old: `wc -l < MANIFEST.md; wc -l < /tmp/o3e-pre-cure2-MANIFEST.md`. New: `wc -l < /tmp/o3e-pre-cure3-MANIFEST.md; wc -l < /tmp/o3e-pre-cure2-MANIFEST.md`.
4. Current-state blocks re-run with fresh output, command unchanged: the entry as it now stands (`sed -n '2371,2386p' DECISIONS.md`); E1, `shasum -a 256 /tmp/o3e-decisions-blob.md`; MANIFEST row, `shasum -a 256 /tmp/o3e-manifest-blob.md`; the key-output block under Verification evidence; and the format check that counts fence lines (`` grep -c '^```' `` on this report). Their earlier outputs are not kept here; the entry's sha256 before cure round 3 is under Whole-file compare (cure round 3).
5. Process log item 6. Old: "a re-run now stops at the 2376 guard, since that line no longer ends with 'and is untested (rubric O3).'" (false since Edit 4 restored that ending). New: line 2385 no longer contains 'Touches Block 1 (' (count 0, pasted), so a re-run stops at the 2385 guard.
6. E2. Old: the item for the quote 'as Step 0.8 did against `/tmp`' (no longer in the entry, count 0 under Edit 4); the paragraph "Checks for the cure-round-2 sentence on line 2376." with its :140 count; "Commit 2582531, the sentence's commit and date" with its log line; "The commits that changed the count of D-2026-07-09-D's heading string" with the f716d2d log line; and "HEAD HANDOFF.md :2011 is not reproduced" with its URL count and four phrase blocks. They backed only the removed sentence. New: all removed; the 2582531 log line is now pasted under S6, Block 0. Added: the list of every double-quoted string in the entry, full-line greps for the three line-2385 quotes in their HEAD sources (commit 2582531 body; Phase 3 spec :180 and :60), and the U+2019 byte check.
7. S6 cross-block check, rewritten to follow line 2385. Old, deleted: the opening paragraph that began "The entry is a scope record about Deviation G, not a new deviation."; the bullet "Block 1: no conflict."; the bullet "Blocks 4 and 5: no conflict."; the Block 0 bullet that began "Block 0. Commit 2582531 is dated 2026-07-08", with its blocks (the 2582531 log line, the HANDOFF.md :2011 URL count and four phrases, the :140 count, the f716d2d log line, the host-shape counts, and the two cure-round-2 phrase greps on lines 2376 and 2385); the bullet "Topology (rubric F1): no conflict."; and the paragraph that began "Search scope and limit:" with its two 'tested' search blocks, which backed only the deleted "no conflict" bullets. New: one bullet each for Block 0, Block 1, Block 2, Blocks 4 and 5, and F1 / the topology, and one for the conflict, each with only the pasted source lines and phrases for its clause.
8. Opening paragraph. Old: "Master's decisions under D-2026-11-08-D D1: DECISION_LOG 2026-11-12T21:04:00Z (first pass) and 2026-11-12T21:25:00Z (cure round 2)." New: adds "2026-11-12T21:41:00Z (cure round 3)", backed by the row's count 1, HEAD count 0, ellipsis count 1 and six phrases from the row.
9. Process log item 8. Old: "Its format and de-identification checks read the report file itself, so it was run in passes, each output copied over the report, until two passes in a row were byte-identical (record; the generator cannot run itself):". New: "the command used to regenerate this report from /tmp/o3e-gen2.sh (record; not re-run; its cmp result is not pasted):". Added item 9: the cure-round-3 record of the MANIFEST edit, with its script pasted by cat, and the count showing /tmp/o3e-gen.sh holds no 'cure round' text, so this report was edited in place rather than regenerated from it.
10. How to read. Old: "then ran it, from the working directory /Volumes/Sensidine/Praxis.build, and captured stdout and stderr." and "(Process log items 2, 6, 7 and 8)". New: "then ran it with bash", "with stdin from /dev/null", the run-helper clause, and "(Process log items 2, 6, 7, 8 and 9)".
11. MANIFEST last row. Old: the row after cure round 2 (pasted in full under MANIFEST row), which named "the two cure-round-2 entry edits (scope-line sentence on Block 0 Step 0.8, Block 0 named in the S6 paragraph)", a sentence the entry no longer has. New: the row names 2026-11-12T21:41:00Z and the two cure-round-3 entry edits; full line, diff and line counts under MANIFEST row.
12. Other sections. Task: one sentence on cure round 3 added (gap before). Workers dispatched: Workers 5 and 6 added. Entry edit log: intro now counts five edits and names the captures. Untouched files: added an awk extraction of the pasted Before values, compared with the re-hash. De-identification: added the sentence that this report, being scanned, must contain none of the strings. Files staged: the cure-round-3 lines added. Result: the old paragraph on Adversary 3's defects replaced by "Pending Adversary 4.". Adversary: an Adversary 4 heading added, with "Pending.".

## Adversary

### Adversary 1 (full re-run)

It re-ran all 65 command blocks and found every one matched byte for byte. It found no S13 duplicate, none of the barred words, no ellipsis or placeholder, no cut line and no de-identification hit. Its final grade line, verbatim:

GRADE: FAIL (9 defects)

Defects and cures, itemised. "Old" is text removed from this report or a gap; "New" is what replaced it.

1. Unbacked DECISION_LOG 21:04Z citation in the opening paragraph. Old: the sentence citing DECISION_LOG 2026-11-12T21:04:00Z had no pasted output. New: the working-tree row is pasted in full, plus a HEAD count of 0.
2. Unbacked parked-unit placement in Task. Old: the claim that lines 2279–2370 belong to the parked unit had no output. New: grep -n -o blocks give the line numbers of D-2026-11-12-B (2280, 2287) and Praxis_build-ckh (2283).
3. The ":140 is its Decision paragraph" point was unsupported. Old: only :133, :140, :174 and :175 were pasted. New: HEAD :139 (the Decision label line) is pasted as well.
4. The 17:31Z row was backed by a count only. Old: grep -c output 1. New: the HEAD row is pasted in full after the count.
5. S6 search claim too broad. Old: "Claim: at HEAD, no spec, design doc or decision pairs public ingress with being tested; every match of 'public ingress' followed within 80 characters by 'tested' is shown here:". New: the stated scope is now HEAD specs/, docs/specs/, docs/design/ and DECISIONS.md, single lines only. A second, wider pattern was added (public or TradingView, either word order, docs/design included).
6. S6 left out Block 0. Old: no Block 0 bullet. New: a Block 0 bullet, with HEAD DECISIONS.md :137 and topology doc :25 (row 1.9) pasted in full. Block 0 is added to the touched list.
7. The how-to-read paragraph was false for the perl record block. Old: "every fenced block was produced by a script that printed the command". New: "every fenced block whose first line starts with" the prompt, plus a sentence naming the one block without a prompt as a record, not a run.
8. S2 wording contradicted the level words found. Old: "The entry records scope only; no component level is claimed." New: "The entry records scope only; it claims no component at any level beyond what its HEAD sources already state." The follow-up sentence now cites where each level word is pasted.
9. Four further unbacked claims:
   - (a) Old: "(the file ended in a newline before the append)". New: removed, and a count shows the appended row starts its own line.
   - (b) Old: the limitation relied on "the unchanged line count and unchanged placement of the entry (2371–2387 before and after)". New: it relies on the perl command and on the pre-edit hash at the same line range. It still states that no before/after file compare was made.
   - (c) Old: "They are the record of the failed attempts:". New: removed.
   - (d) Old: "the one staged path" had no count. New: a staged-path count block (wc -l only).

### Adversary 2 (re-check of the nine cured items)

It re-ran all 76 command blocks and found every one matched byte for byte. All nine Old strings are gone from the body. The format and de-identification checks pass. It found that cures 1, 2, 3, 4, 7, 8, 9(a), 9(c) and 9(d) hold, but that the cures for items 5, 6 and 9(b) bring in claims the pasted output does not back. Its final grade line, verbatim:

GRADE: FAIL (5 defects)

Its defects were not cured in that round. They are cured in section Cure round 2, under the master's decision at DECISION_LOG 2026-11-12T21:25:00Z (phrases pasted at the top of this report).

1. Pointer-edit limitation (cure 9b). The report says the entry hashed to "the master's pre-edit value", but no master value is pasted. Only the manager's own capture and a re-derivation are shown. The master's value is in working-tree DECISION_LOG rows 880, 883 and 885, in shortened form, and none of those rows is pasted.
2. S6 search sentence (cure 5) is false within its stated scope. HEAD DECISIONS.md :143 says public TradingView ingress "is not exercised", and topology doc :25 (pasted) grades public ingress UNVERIFIED. Neither matches the literal word "tested", so "the only line pairing ingress with a test word" overclaims, and the patterns cover less than the sentence says.
3. Block 0 bullet (cure 6) has unbacked parts. The pasted :137 places the superseded remote-VPS premise in a Block 1 design doc, not in Block 0. Nothing pasted shows that Step 0.5 belongs to Block 0 or that the public address was a remote host.
4. Block 0 bullet (cure 6) is incomplete as an S6 check. Commit 2582531's subject records Block 0's Step 0.8 full-loop verification as PASSED. HEAD HANDOFF.md :2011 shows the Step 0.8 plan posting a sample payload to a URL on the same public host as the Step 0.5 address. So Block 0 appears to have passed a full-loop test through a public-address webhook, and the bullet never decides whether that conflicts with the entry's "public TradingView ingress is untested" wording. (Side note from the adversary: row 1.9 cites HANDOFF.md:1539, which is blank at HEAD; the record is at :2001.)
5. The entry's own S6 paragraph (DECISIONS.md :2385) lists Block 1, Blocks 4 and 5 and F1, but not Block 0. It now points to this report's S6 section, which says the entry also touches Block 0. The entry's bytes are frozen apart from the pointer, so this is for the master.

Open points it raised for the master (the master decided them at 21:25:00Z; see Cure round 2):
- (a) Whether Block 0's Step 0.8 public-address full loop means the entry's wording "is untested" needs narrowing, for example to live TradingView ingress into the local path. That would change the entry's bytes.
- (b) Whether the entry's S6 paragraph must name Block 0.

### Adversary 3

An ADVERSARIAL praxis-worker re-ran every pasted command and checked the entry. Its final grade line, verbatim:

GRADE: FAIL (6 defects)

It reported that all 124 pasted command blocks re-ran with no byte mismatch, and that the four edit-record blocks were checked by their effect. DECISIONS.md differs from the pre-edit copy only on lines 2376 and 2385, both equal to the authorised text. MANIFEST.md differs only on its last row. The six earlier reports match their captured hashes. The format, de-identification and edit-scope checks pass. Its defects, as it reported them (none cured in this round):

1. S6, Block 2 not listed. HEAD docs/specs/2026-11-05-phase3-build-specification.md :180 makes Block 1's milestone the start condition for Block 2, and the sign-off body says that condition is now satisfied. The entry narrows what the milestone covers, but neither the S6 section nor the entry's S6 paragraph lists or tests Block 2.
2. S6, Block 1 not tested against its own spec. Build spec :60 states the Block 1 milestone as firing a fake signal from TradingView and watching it flow through n8n. On its face that clashes with "internal path only" and "untested". The Block 1 bullet tests only against the sign-off body, and the two S6 searches need the word "tested", so they cannot find this line. The entry's "Conflicts with none" is not backed.
3. S1, "public" in the entry's new sentence. It rests only on host-shape counts (https, dotted name, not an IP address, not localhost), and the report's Block 0 bullet states that limit. A private DNS name passes all three.
4. S1, "posted a test payload by curl", "whose n8n wrote to a directory on that host" and "was not TradingView ingress" rest on HEAD HANDOFF.md :2011. That line is a forward plan, not a record of the run, and the report does not say so. Its "remote-host dir" phrase does not show the directory was on the same host as the webhook. The run records (the body of commit 2582531 and docs/reports/2026-07-08-step-0.8-full-loop.md) are not pasted.
5. S1, "before the local path existed". The pasted output shows only that D-2026-07-09-D is dated a day after Step 0.8, which is a decision date. The cited :140 quote sits in "test webhook posts driven locally", so it backs neither "remote" nor "before".
6. S1, Process log item 8. "until two passes in a row were byte-identical" has no pasted output; the record block pastes no cmp result.

No further cure round was run. Defects 1 to 5 are on the entry's bytes or on the sentence the master set for it, and the brief allows entry edits (a) and (b) only. A report-only cure could reach item 6 alone, so a re-check of the cured items could not end at PASS on the open defects. Open for the master, not decided here:
- (c) Whether the entry must name and test Block 2 and test Block 1 against build spec :60, and so whether "Conflicts with none" stands.
- (d) Whether the new scope-line sentence must be narrowed to what pasted output backs, or the Step 0.8 run records pasted (commit 2582531 body, the 2026-07-08 Step 0.8 report), including whether "public" and "before the local path existed" stay.

### Adversary 4

An ADVERSARIAL praxis-worker re-ran every pasted command and checked the entry, the MANIFEST rows and the de-identification. It wrote no file. Its final grade line, verbatim:

GRADE: FAIL (7 defects)

It reported 165 command blocks re-run with 0 mismatches, the entry diff against the pre-round-3 copy limited to lines 2376 and 2385 (both equal to the authorised text, every quote byte-exact against HEAD), the MANIFEST diff limited to the last row, de-identification counts of 0, and the six earlier reports' hashes unchanged. Its defects, as it reported them (none cured in this round, because defect 6 is on the entry's bytes and the brief allows no entry cure):

1. [REPORT] The Process log reason for editing in place checks /tmp/o3e-gen.sh, but the report names the cure-round-2 generator /tmp/o3e-gen2.sh, which does hold cure-round text (count 16 by its run). The stated reason is false.
2. [REPORT] The claims that a run helper re-ran every block in order and pasted its output have no recorded helper command or pasted run.
3. [REPORT] The Workers line saying the manager made the two cure-round-3 entry edits has no record block for that edit, nor for the copies taken before it; the opening line's "cure rounds 2 and 3 by BUILD praxis-workers" does not fit it.
4. [REPORT] Cure round 3 does not give old and new for every prose change (lead-in lines under Edit 2, Edit 3, Whole-file compare, MANIFEST row, and the opening line).
5. [REPORT] A second "Result" string sits inside Cure round 3 (two matches for the string with its colon); the format self-check uses a whole-line match and misses it.
6. [ENTRY] Line 2385, "Block 2 started on that sign-off (:180)". Spec :180 is a start rule, not a record that Block 2 started; the spec entered the repo on 2026-11-06, after the sign-off; the sign-off's "entry condition now satisfied" does not show a start either. A HEAD STATUS.md phase line would, but it is not pasted.
7. [REPORT] The S6 conflict bullet rests "did not" on "B1-a verified-as-DEFERRED" without pasting what B1-a is; the HEAD milestone audit report defines it as the WireGuard tunnel, deferred by decision, and holds no TradingView match. The entry's wording holds against HEAD; the report's backing does not.

Open for the master, not decided here: (e) whether line 2385's "Block 2 started on that sign-off (:180)" is narrowed (for example to the sign-off's own words, "Block 2 (Backtesting) entry condition now satisfied") or backed by a pasted HEAD STATUS.md phase line. Defects 1 to 5 and 7 are report-wording cures for a later round.

## Files staged

None by this unit; no git add was run. Changed by this unit, all unstaged: DECISIONS.md (line 2385 in the pointer edit; lines 2376 and 2385 in cure round 2; lines 2376 and 2385 again in cure round 3), MANIFEST.md (one appended row, that row rewritten in cure round 2 and again in cure round 3), and this report (new, untracked). Counts of staged entries for those three paths, and whether this report is tracked:

```text
$ git diff --cached --numstat -- DECISIONS.md MANIFEST.md docs/reports/2026-11-12-o3-block1-scope-evidence.md | wc -l
       0
```

```text
$ git ls-files -- docs/reports/2026-11-12-o3-block1-scope-evidence.md | wc -l
       0
```

## Result

Result: FAIL

The last adversary (Adversary 4) graded FAIL (7 defects). Defect 6 is on the entry's bytes (open point (e) for the master); the other six are report-wording cures for a later round.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
