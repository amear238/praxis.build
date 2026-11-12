# Manager report: 2026-11-12-v-rulings-filing-correction-3c

## Task
Bead Praxis_build-n1y, unit 2026-11-12-v-rulings-filing-correction-3c (DECISION_LOG 2026-11-12T00:37:30Z, 01:39:00Z, 02:01:00Z). Cure, by the smallest edit, the items docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md left open in A = docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; add a labelled manager note to the Correction 3b manager skeleton; regenerate A's self-check; append MANIFEST rows for the 3b and 3c reports; one narrow adversarial check; closing scan. Nothing committed or staged by this unit.

## Rubric criteria addressed
- S1 (specs/SPEC_RUBRIC.md:124): each open item is cured by deleting or narrowing the clause to what A already pastes, or by a REPORTED label on an event (V3 shows every edit).
- S2 (specs/SPEC_RUBRIC.md:125): no edit raises a claim's level; A's E3 now says its MANIFEST output is as it was before the Correction 3c rows (V3, edit 6).
- S7 (specs/SPEC_RUBRIC.md:130): HEAD a962475 and 0 staged paths outside docs/reports/evidence/ (V1).
- S8 (specs/SPEC_RUBRIC.md:131): no question of Amear's is answered here; the address rule is quoted, not re-applied.
- S13 (specs/SPEC_RUBRIC.md:136): the S13 sentence standalone once as the last non-blank line in every report scanned (V7), this one included.

## Workers dispatched
- worker1, ADVERSARIAL (narrow): the lines changed in A, the 3b skeleton note, the MANIFEST rows and the closing scan. Outcome: it stopped at its 40-turn limit (REPORTED by the harness notification); its report on disk is complete, with a Result line and the S13 sentence last (V7): FAIL, 0 MAJOR and 5 MINOR; all eight open items graded CURED. Report docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md.

## Process log
My account of my own actions; dispatches and edits are events and are REPORTED; outputs are in the Verification evidence section.
1. Read the rubric rows and 3b-worker3's report. Copied A, C (docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md), the 3b manager skeleton and MANIFEST.md to /tmp/c3c/pre/.
2. Edited A with /tmp/c3c/mgr/fixA.py (exact-string replacements, each required to match once) and regenerated A's self-check block with /tmp/c3c/mgr/regen.py (V3, V4). C was not edited (V2).
3. Inserted the manager note into the 3b skeleton (V5). Appended six MANIFEST rows (V6).
4. Dispatched worker1 (ADVERSARIAL, narrow) with the artifacts and the criteria. It returned 0 MAJOR and 5 MINOR. I fixed all five by small edits (see Adversarial findings), re-ran V1-V6 (the outputs below are from that re-run) and regenerated A's self-check. No second adversarial round (brief: none for MINORs).
5. Ran the closing scan (V7) and assembled this report.

## Edits to A (each one in V3)
1. Line 15 (3b-worker2 MINOR 7; 3b-worker1 finding 5): the lead "undefined variables in other original commands of the two correction-2 reports" narrowed to what E6's paste of /tmp/c3w2/final.out lines 56, 64 and 65 shows: "placeholder commands in the original bodies that Correction 3 does not re-run, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report".
2. Line 34 (3b-worker2 MINOR 8): "the MFFU public support address itself" narrowed to "the sender address of the MFFU reply itself", which is what E6 shows (same_address=YES against return-handoff line 114, under the heading "## MFFU replies to V1 and V6").
3. Line 36 (3b-worker3 new 3): "the two lines this unit edited also carried one address each" narrowed to "the two files whose address lines this unit edited also carried one email line each", matching E6's per-file counts 2, 1 and 1 (wording after worker1 MINOR 1).
4. Line 312, now 313 (3b-worker3 new 2): the unpasted clause "re-run now, its finding 6 and finding 7 sections show those edits too" deleted.
5. Line 572, now 573 (3b-worker3 new 1): the sentence "These edits have NOT been re-checked by an adversarial worker." deleted.
6. New line 293 in E3: "Correction 3c note (REPORTED): rows were appended to MANIFEST.md after line 420 in Correction 3c, after E2, E3 and E6 were captured; those blocks and the Files staged count show MANIFEST.md as it was then (E2's last six rows were then rows 415-420)." Added because the V6 append changes what E2's last-six-rows scan covers and makes E3's `tail -n 6`, E6's `wc -l` and the Files staged count no longer reproduce (wording after worker1 MINOR 2).
7. Line 585, now 586 (3b-worker3 new 4, worker2 report): "reworded again and lines 30-36 added in Correction 3b" replaced by "REPORTED: edited again in Correction 3b".
8. Line 590, now 591 (3b-worker3 new 4, worker3 report): "(lines 161-172 edited or added in Correction 3b)" replaced by "(REPORTED: edited in Correction 3b)", which drops the range that took in C:163-164.
9. Line 593, now 594: "; in Correction 3c, /tmp/c3c/mgr/regen.py" added to the list of regeneration scripts. Lines 596-597: the self-check output regenerated (606 to 607 lines); V4 shows it equals a fresh run.

## Verification evidence (command output)
All commands ran under bash from the repo root. The scripts are shown with `cat`, so every command is literal. None of the files diffed below holds an email address or the rep's name (V7), so no output here is masked.
```
$ cat /tmp/c3c/mgr/ev.sh
#!/bin/bash
# Correction 3c manager evidence. Prints each command, then its output. No address, name or banned string is in any file diffed here (closing scan).
cd /Volumes/Sensidine/Praxis.build || exit 1
run() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
echo "--- V1. HEAD and staging (S7)"
run "git rev-parse --short HEAD"
run "git diff --cached --name-only | grep -vc '^docs/reports/evidence/'"
echo "--- V2. correction-3 worker3 report (C) not edited in Correction 3c"
run "cmp /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md && echo C-unchanged"
echo "--- V3. correction-3 manager report (A): every Correction 3c edit, before and after"
run "diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md"
run "wc -l /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md"
echo "--- V4. A self-check block equals a fresh run of its own command; then a trip test of the comparison"
run "cat /tmp/c3c/mgr/eq.sh"
run "/tmp/c3c/mgr/eq.sh"
run "sed 's/lines=607/lines=606/' /tmp/c3c/mgr/sc.fresh | cmp -s - /tmp/c3c/mgr/sc.pasted; echo tampered-copy-cmp-rc=\$?"
echo "--- V5. 3b manager skeleton: insertion only, before its final line"
run "diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -v '^>'"
run "diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -c '^<'"
run "head -n 28 docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | cmp - <(head -n 28 /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo first-28-lines-identical"
run "tail -n 1 docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | cmp - <(tail -n 1 /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo last-line-identical"
run "sed -n 30p docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -oF \"the row's count and four of its words are shown below\""
run "cat /tmp/c3c/mgr/note3b.sh"
run "/tmp/c3c/mgr/note3b.sh | cmp - <(sed -n '32,44p' docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo note-block-equals-fresh-run"
echo "--- V6. MANIFEST.md: append only"
run "diff /tmp/c3c/pre/MANIFEST.md MANIFEST.md"
run "diff /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -c '^<'"
run "wc -l /tmp/c3c/pre/MANIFEST.md MANIFEST.md"
run "head -n 420 MANIFEST.md | cmp - /tmp/c3c/pre/MANIFEST.md && echo first-420-lines-identical"
$ /tmp/c3c/mgr/ev.sh
--- V1. HEAD and staging (S7)
$ git rev-parse --short HEAD
a962475
$ git diff --cached --name-only | grep -vc '^docs/reports/evidence/'
0
--- V2. correction-3 worker3 report (C) not edited in Correction 3c
$ cmp /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md && echo C-unchanged
C-unchanged
--- V3. correction-3 manager report (A): every Correction 3c edit, before and after
$ diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
15c15
< - worker2, ADVERSARIAL: hunt for placeholder commands, unpasted claims, email addresses, rep-name occurrences, S13 and byte-scope faults across every file this unit touches or creates. Outcome: stopped at its 40-turn limit with no findings written (REPORTED by the harness notification, not re-runnable). Its report is a skeleton plus a manager note (E4). Its evidence file /tmp/c3w2/final.out held leads (E6 pastes its lines 56, 64, 65, 84, 126 and 127) that I read and passed to worker3 as fix items (the passing on is REPORTED): undefined variables in other original commands of the two correction-2 reports, an unpasted "no pre-edit copy exists" in the manager report's C3.5, and an unpasted "Nothing under vm/ or .claude/ was written." in the worker1 report. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md.
---
> - worker2, ADVERSARIAL: hunt for placeholder commands, unpasted claims, email addresses, rep-name occurrences, S13 and byte-scope faults across every file this unit touches or creates. Outcome: stopped at its 40-turn limit with no findings written (REPORTED by the harness notification, not re-runnable). Its report is a skeleton plus a manager note (E4). Its evidence file /tmp/c3w2/final.out held leads (E6 pastes its lines 56, 64, 65, 84, 126 and 127) that I read and passed to worker3 as fix items (the passing on is REPORTED): placeholder commands in the original bodies that Correction 3 does not re-run, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report, an unpasted "no pre-edit copy exists" in the manager report's C3.5, and an unpasted "Nothing under vm/ or .claude/ was written." in the worker1 report. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md.
34c34
< - docs/reports/2026-11-11-v-rulings-filing-worker2.md:169. Before: a disposition note giving the MFFU public support address itself (E6: it is the address in the header of the MFFU reply at return-handoff line 114, same_address=YES), inside backticks, followed by "(A:114, 132). This is a public company address. Kept." After: the backticks hold the words `MFFU's public support address`; the rest of the line is unchanged. Size 11554 to 11556 bytes, still 179 lines, every other line byte-identical (E1).
---
> - docs/reports/2026-11-11-v-rulings-filing-worker2.md:169. Before: a disposition note giving the sender address of the MFFU reply itself (E6: it is the address in the header of the MFFU reply at return-handoff line 114, same_address=YES), inside backticks, followed by "(A:114, 132). This is a public company address. Kept." After: the backticks hold the words `MFFU's public support address`; the rest of the line is unchanged. Size 11554 to 11556 bytes, still 179 lines, every other line byte-identical (E1).
36c36
< - docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:114 and :132 were not changed (master's application: email-header quotes of the MFFU support address). E2 shows they are the only two email hits in the working copy of the bead's files, in the DECISIONS.md added lines and in the bead's MANIFEST added lines. Note: 83891f6 (the parked tip) is not an ancestor of HEAD (E5). As committed at 83891f6, the two lines this unit edited also carried one address each (E6: email_lines 2, 1 and 1).
---
> - docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:114 and :132 were not changed (master's application: email-header quotes of the MFFU support address). E2 shows they are the only two email hits in the working copy of the bead's files, in the DECISIONS.md added lines and in the bead's MANIFEST added lines. Note: 83891f6 (the parked tip) is not an ancestor of HEAD (E5). As committed at 83891f6, the two files whose address lines this unit edited also carried one email line each (E6: email_lines 2, 1 and 1).
292a293
> Correction 3c note (REPORTED): rows were appended to MANIFEST.md after line 420 in Correction 3c, after E2, E3 and E6 were captured; those blocks and the Files staged count show MANIFEST.md as it was then (E2's last six rows were then rows 415-420).
312c313
< Correction 3b note: the output below was captured in Correction 3, before the Correction 3b edits to the worker2 and worker3 reports; re-run now, its finding 6 and finding 7 sections show those edits too. E6 pastes the current diffs.
---
> Correction 3b note: the output below was captured in Correction 3, before the Correction 3b edits to the worker2 and worker3 reports. E6 pastes the current diffs.
572c573
< - Worker5 (ADVERSARIAL, narrow): FAIL with 0 MAJOR and 9 MINOR findings (E6; docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md). I addressed all nine by text edits after it returned: this report's lines on S13 coverage, the worker1 insertion, the MANIFEST step, the no-reply address, the MANIFEST scan and the ancestry of 83891f6, the S6 basis and the /tmp list, plus the REPORTED label on the process log (new commands in E2 and E5); the worker3 note (start-time reasoning, REPORTED label on the brief figure); the worker2 note (pointer to E4, REPORTED label on dispatches). These edits have NOT been re-checked by an adversarial worker.
---
> - Worker5 (ADVERSARIAL, narrow): FAIL with 0 MAJOR and 9 MINOR findings (E6; docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md). I addressed all nine by text edits after it returned: this report's lines on S13 coverage, the worker1 insertion, the MANIFEST step, the no-reply address, the MANIFEST scan and the ancestry of 83891f6, the S6 basis and the /tmp list, plus the REPORTED label on the process log (new commands in E2 and E5); the worker3 note (start-time reasoning, REPORTED label on the brief figure); the worker2 note (pointer to E4, REPORTED label on dispatches).
585c586
< - docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: 38 lines; new; skeleton plus manager note at lines 18-37 (two sentences of it reworded by me after worker5; reworded again and lines 30-36 added in Correction 3b).
---
> - docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: 38 lines; new; skeleton plus manager note at lines 18-37 (two sentences of it reworded by me after worker5; REPORTED: edited again in Correction 3b).
590c591
< - docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md also carries a manager note at its lines 146-173 (lines 161-172 edited or added in Correction 3b); docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md line 485 was reworded by me inside the inserted section (E5).
---
> - docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md also carries a manager note at its lines 146-173 (REPORTED: edited in Correction 3b); docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md line 485 was reworded by me inside the inserted section (E5).
593c594
< Self-check of this report, run on the final file. The block below was regenerated (/tmp/c3mgr/assemble.py; in Correction 3b, /tmp/c3b/mgr/fixA.py) until the output it contains equals the output of the same command run on the file that contains it:
---
> Self-check of this report, run on the final file. The block below was regenerated (/tmp/c3mgr/assemble.py; in Correction 3b, /tmp/c3b/mgr/fixA.py; in Correction 3c, /tmp/c3c/mgr/regen.py) until the output it contains equals the output of the same command run on the file that contains it:
596c597
< docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[606] last_nonblank_line=606 last_nonblank_is_S13=YES lines=606
---
> docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[607] last_nonblank_line=607 last_nonblank_is_S13=YES lines=607
$ wc -l /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
     606 /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md
     607 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
    1213 total
--- V4. A self-check block equals a fresh run of its own command; then a trip test of the comparison
$ cat /tmp/c3c/mgr/eq.sh
#!/bin/bash
# Re-runs the self-check command pasted at the end of the correction-3 manager report and compares with the pasted block, byte for byte.
cd /Volumes/Sensidine/Praxis.build || exit 1
F=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
L=$(grep -n '^\$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md;' "$F" | cut -d: -f1)
echo "self-check command line: $L"
sed -n "${L}p" "$F" | sed 's/^\$ //' > /tmp/c3c/mgr/sc.cmd
bash /tmp/c3c/mgr/sc.cmd > /tmp/c3c/mgr/sc.fresh 2>&1
sed -n "$((L+1)),$((L+5))p" "$F" > /tmp/c3c/mgr/sc.pasted
sed -n "$((L+6))p" "$F"
cmp /tmp/c3c/mgr/sc.pasted /tmp/c3c/mgr/sc.fresh && echo pasted-block-equals-fresh-run
cat /tmp/c3c/mgr/sc.fresh
$ /tmp/c3c/mgr/eq.sh
self-check command line: 596
```
pasted-block-equals-fresh-run
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[607] last_nonblank_line=607 last_nonblank_is_S13=YES lines=607
V1 positive control (hyphen-split synthetic line): HIT_lines=1
0
0
0
$ sed 's/lines=607/lines=606/' /tmp/c3c/mgr/sc.fresh | cmp -s - /tmp/c3c/mgr/sc.pasted; echo tampered-copy-cmp-rc=$?
tampered-copy-cmp-rc=1
--- V5. 3b manager skeleton: insertion only, before its final line
$ diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -v '^>'
28a29,47
$ diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -c '^<'
0
$ head -n 28 docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | cmp - <(head -n 28 /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo first-28-lines-identical
first-28-lines-identical
$ tail -n 1 docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | cmp - <(tail -n 1 /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo last-line-identical
last-line-identical
$ sed -n 30p docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -oF "the row's count and four of its words are shown below"
the row's count and four of its words are shown below
$ cat /tmp/c3c/mgr/note3b.sh
#!/bin/bash
# Builds the Correction 3c manager note for the 3b manager skeleton; prints each command then its output.
cd /Volumes/Sensidine/Praxis.build || exit 1
run() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
run "grep -c '2026-11-12T02:01:00Z' DECISION_LOG.md"
run "grep '2026-11-12T02:01:00Z' DECISION_LOG.md | grep -o 'STOPPED AT ITS 60-TURN CAP'"
run "wc -l docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md"
run "grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md | cut -c1-190"
$ /tmp/c3c/mgr/note3b.sh | cmp - <(sed -n '32,44p' docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md) && echo note-block-equals-fresh-run
note-block-equals-fresh-run
--- V6. MANIFEST.md: append only
$ diff /tmp/c3c/pre/MANIFEST.md MANIFEST.md
420a421,426
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-v-rulings-filing-correction-3b (bead Praxis_build-n1y): skeleton left when the manager stopped at its turn limit, plus a Correction 3c manager note listing its three worker reports and their result lines; its own Result line reads BLOCKED (skeleton; not yet filled); ungraded at time of row |
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-v-rulings-filing-correction-3b: re-check of the 9 correction-3 worker 5 findings; FAIL with 7 MINOR, 0 MAJOR; ungraded at time of row |
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 2 report for unit 2026-11-12-v-rulings-filing-correction-3b: re-check of the correction-3 manager report and the two manager notes; FAIL with 1 MAJOR, 12 MINOR; ungraded at time of row |
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 3 report for unit 2026-11-12-v-rulings-filing-correction-3b: narrow re-check of the Correction 3b edits; FAIL with 4 new MINOR, 0 MAJOR; ungraded at time of row |
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-v-rulings-filing-correction-3c (bead Praxis_build-n1y): smallest edits to the correction-3 manager report for the open 3b worker 3 items, manager note in the 3b manager skeleton, MANIFEST rows, closing scan; ungraded at time of row |
> | /docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-v-rulings-filing-correction-3c: narrow re-check of the lines changed in Correction 3c and of the closing scan; ungraded at time of row |
$ diff /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -c '^<'
0
$ wc -l /tmp/c3c/pre/MANIFEST.md MANIFEST.md
     420 /tmp/c3c/pre/MANIFEST.md
     426 MANIFEST.md
     846 total
$ head -n 420 MANIFEST.md | cmp - /tmp/c3c/pre/MANIFEST.md && echo first-420-lines-identical
first-420-lines-identical
```

### V7. Closing scan
The rep's name is built at runtime from line 4 of /tmp/vrf-c2/selfcheck.sh and never printed; the word and the two strings are built at runtime. Expected: email=0, name_ci=0, word_ci=0, s1=0, s2=0 for every path; S13_standalone=1 and last_nonblank_is_S13=YES for every report; each positive control 1.
```
$ cat /tmp/c3c/mgr/close.sh
#!/bin/bash
# Correction 3c closing scan. Counts and line numbers only; the rep's name, the word and the two strings are built at runtime and never printed.
cd /Volumes/Sensidine/Praxis.build || exit 1
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
W="verd"; W="${W}ict"; X1="COMMIT-"; X1="${X1}INDEX"; X2="COMMIT-"; X2="${X2}DIFF-SHA256"
[ -n "$N" ] || { echo "name token EMPTY; scan not valid"; exit 1; }; echo "name token built: YES"
git diff HEAD -- MANIFEST.md | grep '^+' | grep -v '^+++' > /tmp/c3c/mgr/manifest_added.txt
echo "MANIFEST.md added lines vs HEAD: $(wc -l < /tmp/c3c/mgr/manifest_added.txt | tr -d ' ')"
echo "--- per file: email lines, rep-name lines, word lines, string-1 lines, string-2 lines"
for f in \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md \
  docs/reports/2026-11-11-v-rulings-filing-worker2.md \
  docs/reports/2026-11-11-v-rulings-filing-worker5.md \
  /tmp/c3c/mgr/manifest_added.txt; do
  echo "$f: email=$(grep -cE "$EM" "$f") name_ci=$(grep -ci -- "$N" "$f") word_ci=$(grep -ci -- "$W" "$f") s1=$(grep -c -- "$X1" "$f") s2=$(grep -c -- "$X2" "$f")"
done
echo "--- S13 and split-name check per report (selfcheck.sh)"
/tmp/vrf-c2/selfcheck.sh \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md \
  docs/reports/2026-11-11-v-rulings-filing-worker2.md \
  docs/reports/2026-11-11-v-rulings-filing-worker5.md
echo "--- split-name check on the MANIFEST added lines (S13 fields do not apply to this file)"
/tmp/vrf-c2/selfcheck.sh /tmp/c3c/mgr/manifest_added.txt | head -n 1 | grep -oE 'V1_HIT_lines=[0-9]+'
echo "--- positive controls (synthetic lines built at runtime, never printed)"
AT=$(printf '\x40'); printf 'x a.b%sc-d.example y\n' "$AT" | grep -cE "$EM"
printf 'x %s y\n' "$N" | grep -ci -- "$N"
printf 'x %s y\n' "$(echo "$W" | tr a-z A-Z)" | grep -ci -- "$W"
printf 'x %s %s y\n' "$X1" "$X2" | grep -c -- "$X1"
printf 'x %s y\n' "$X2" | grep -c -- "$X2"
$ /tmp/c3c/mgr/close.sh
name token built: YES
MANIFEST.md added lines vs HEAD: 47
--- per file: email lines, rep-name lines, word lines, string-1 lines, string-2 lines
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-worker5.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
/tmp/c3c/mgr/manifest_added.txt: email=0 name_ci=0 word_ci=0 s1=0 s2=0
--- S13 and split-name check per report (selfcheck.sh)
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[607] last_nonblank_line=607 last_nonblank_is_S13=YES lines=607
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[174] last_nonblank_line=174 last_nonblank_is_S13=YES lines=174
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[678] last_nonblank_line=678 last_nonblank_is_S13=YES lines=678
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[38] last_nonblank_line=38 last_nonblank_is_S13=YES lines=38
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[749] last_nonblank_line=749 last_nonblank_is_S13=YES lines=749
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[48] last_nonblank_line=48 last_nonblank_is_S13=YES lines=48
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[395] last_nonblank_line=395 last_nonblank_is_S13=YES lines=395
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[306] last_nonblank_line=306 last_nonblank_is_S13=YES lines=306
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[317] last_nonblank_line=317 last_nonblank_is_S13=YES lines=317
docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[333] last_nonblank_line=333 last_nonblank_is_S13=YES lines=333
docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[501] last_nonblank_line=501 last_nonblank_is_S13=YES lines=501
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[590] last_nonblank_line=590 last_nonblank_is_S13=YES lines=590
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[487] last_nonblank_line=487 last_nonblank_is_S13=YES lines=487
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[241] last_nonblank_line=241 last_nonblank_is_S13=YES lines=241
V1 positive control (hyphen-split synthetic line): HIT_lines=1
--- split-name check on the MANIFEST added lines (S13 fields do not apply to this file)
V1_HIT_lines=0
--- positive controls (synthetic lines built at runtime, never printed)
1
1
1
1
1
```
Result of the scan: every count is 0, every report has S13_standalone=1 and last_nonblank_is_S13=YES, and every positive control prints 1. Pre-existing and not changed: docs/reports/2026-11-11-v-rulings-filing-worker2.md has S13_containing=3 with S13_standalone=1.

## Adversarial findings
worker1 (ADVERSARIAL, narrow; docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md): 0 MAJOR, 5 MINOR. It graded every open item CURED: 3b-worker2 MINOR 7 and 8, 3b-worker1 item 5, 3b-worker3 new 1-4. Its Result line, pasted:
```
$ grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md | cut -c1-200
499:Result: FAIL. 0 MAJOR, 5 MINOR (A:36; A:293/A:285 E2 drift; MANIFEST.md:421; B:30; close.sh split-letter coverage of the MANIFEST added lines). Open items: of the eight graded (3b-worker2 MINOR 7 
```
Dispositions (each fix is in a paste in this report):
1. MINOR, A:36, "the two files this unit edited" (A's Files staged lists five edited paths). Fixed: now "the two files whose address lines this unit edited" (V3, hunk 36c36).
2. MINOR, A:293, the note did not name E2, whose last-six-rows scan now covers other rows. Fixed: the note now names E2, E3 and E6 and adds "(E2's last six rows were then rows 415-420)" (V3, hunk 292a293). At capture time MANIFEST.md had 420 lines (A's E3 `wc -l`).
3. MINOR, MANIFEST.md:421, "carries no result of its own" does not quote the file's Result line. Fixed: the row now says "its own Result line reads BLOCKED (skeleton; not yet filled)" (V6).
4. MINOR, 3b manager note line 30, "the row and its words are shown below". Fixed: now "the row's count and four of its words are shown below" (V5, the `sed -n 30p` line).
5. MINOR, close.sh ran no split-letter check on the MANIFEST added lines. Fixed: close.sh now runs selfcheck.sh's split-letter count on /tmp/c3c/mgr/manifest_added.txt (V7: V1_HIT_lines=0). worker1's side note, that an empty name token would still let the name control print 1, is fixed too: close.sh now exits if the token is empty (V7, source).
- Not graded by worker1, and not changed: A:15 no longer mentions the worker6 lead in /tmp/c3w2/final.out lines 72-75. A:15 now names only what E6 pastes and does not say the list is complete. Adding the worker6 lead back would mean a new paste in A, and the brief asks for the smallest edit.
- Also not changed: A's Result section still says it needs a re-check of the edits made after worker5. That is A's own record of its result; the master decides on it.

## S6 cross-block check
Not applicable. This unit approves no deviation. Every file it changed or created is a report under docs/reports/ or MANIFEST.md (V3, V5, V6, and the scan list in V7); no block spec, code, hook or setting is among them.

## Files staged
None by this unit (V1). Changed or created in the working tree:
- docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: edited, 606 to 607 lines (V3).
- docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md: edited, 19 lines inserted before its final line, 29 to 48 lines (V5, V7).
- MANIFEST.md: 6 rows appended, 420 to 426 lines (V6).
- docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md: new, 501 lines (V7).
- docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: new, this report (line count in the self-check below).
- Outside the repo: /tmp/c3c/pre (pre-edit copies), /tmp/c3c/mgr (my scripts and outputs), /tmp/c3c/w1 (worker1 scratch).

Self-check of this report, regenerated by /tmp/c3c/mgr/assemble.py until the block equals a fresh run of its command on this file:
```
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md
docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[333] last_nonblank_line=333 last_nonblank_is_S13=YES lines=333
V1 positive control (hyphen-split synthetic line): HIT_lines=1
```

Result: PASS (manager grade only; the auditor grades this unit). The adversarial pass found 0 MAJOR; all 5 MINOR are fixed, and the fixes are shown in V3, V5, V6 and V7. Nothing is staged or committed.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
