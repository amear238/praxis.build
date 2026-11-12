# Unit 2026-11-12-v-rulings-filing-correction-3, manager report

## Task
Bead Praxis_build-n1y (resumed by Amear, DECISION_LOG 2026-11-12T00:37:30Z). Cure the two checks a fresh audit failed. Check 2 (S1): unpasted claims and placeholder commands in docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md (lines 105, 146, 153, 163, 184, 204) and docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md (lines 16, 34). Check 4: email addresses in added lines, under the corrected rule from Amear's channel of 2026-11-12 as applied by the master (DECISION_LOG 00:37:30Z). Nothing is committed or staged by this unit. F2 and F4 are out of scope; this report claims nothing about them.

## Rubric criteria addressed
- S1 (specs/SPEC_RUBRIC.md:124): every flagged line now has a literal command and its full output in a Correction 3 section.
- S2 (specs/SPEC_RUBRIC.md:125): facts that did not reproduce are marked WRONG or "no longer holds", not softened.
- S7 (specs/SPEC_RUBRIC.md:130): nothing committed (HEAD is still a962475, E1) and nothing staged by this unit: the one staged path is a pre-existing one under docs/reports/evidence/, and the count of staged paths outside that directory is 0 (E1).
- S8 (specs/SPEC_RUBRIC.md:131): the address rule is Amear's (2026-11-12); its application to each line is the master's (DECISION_LOG 00:37:30Z). This unit decided nothing on his behalf.
- S13 (specs/SPEC_RUBRIC.md:136): the S13 sentence once, standalone, last line, in each new report and in each edited report (E1 and E5 self-check output, E6 for the worker5 report, and the self-check block at the end of this report).

## Workers dispatched
- worker1, BUILD: Correction 3 sections in the two correction-2 reports, and the two one-line address edits. Outcome: done. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md.
- worker2, ADVERSARIAL: hunt for placeholder commands, unpasted claims, email addresses, rep-name occurrences, S13 and byte-scope faults across every file this unit touches or creates. Outcome: stopped at its 40-turn limit with no findings written (REPORTED by the harness notification, not re-runnable). Its report is a skeleton plus a manager note (E4). Its evidence file /tmp/c3w2/final.out held leads (E6 pastes its lines 56, 64, 65, 84, 126 and 127) that I read and passed to worker3 as fix items (the passing on is REPORTED): placeholder commands in the original bodies that Correction 3 does not re-run, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report, an unpasted "no pre-edit copy exists" in the manager report's C3.5, and an unpasted "Nothing under vm/ or .claude/ was written." in the worker1 report. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md.
- worker3, BUILD (fix): added C3.8 and C3.9 to the correction-2 manager report, C3.4 to the worker6 report, and an addendum to the worker1 report. Outcome: done; insertions only (E1 v2 run for the two correction-2 reports; E5 for the worker1 report against worker3's pre-edit copy). Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md.
- worker4, ADVERSARIAL: fresh full pass over every file this unit touches or creates, including this report. Outcome: FAIL, 1 MAJOR and 6 MINOR (E6: its line 747), all on files written in this unit; all seven answered by edits (see Adversarial findings), and worker5 then found defects in some of those edits. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md.
- worker5, ADVERSARIAL (narrow): every change made after worker4. Outcome: FAIL, 0 MAJOR and 9 MINOR (E6: its line 305); see Adversarial findings. Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md.

## Process log
This log is my account of my own actions. The dispatches and hand-backs are events, not command outputs, so they are REPORTED; where a step produced output, the E-section is cited.
1. Read the rubric rows (S1, S2, S7, S8, S13 at specs/SPEC_RUBRIC.md:124-136) and the flagged lines.
2. Checked that the original helper scripts still exist (/tmp/vrf-c2/selfcheck.sh, /tmp/vrf-c2/lib.sh, /tmp/c2mgr/pii.py); E6 lists them with `ls -d`; worker1 pastes them in the inserted sections.
3. Dispatched worker1 (BUILD). It inserted the sections and made the two address edits (E1); the order of its own steps is in its report and is not re-shown here.
4. Re-ran the append-only, scope and self-check verification myself (E1, v1 run).
5. Dispatched worker2 (ADVERSARIAL) with the artifacts and the criteria only. It stopped at its turn limit; I added a manager note to its report (E4) and dispatched worker3 (BUILD fix) on the leads in its evidence file.
6. Re-ran the append-only and self-checks after worker3 (E1, v2 run). Appended the five MANIFEST rows 415-419 (E3 shows them as one block against the pre-append copy). Dispatched worker4 (ADVERSARIAL) on everything.
7. Worker4 returned FAIL (1 MAJOR, 6 MINOR). I fixed all seven myself as text edits in my own scripts, my own notes and this report, plus one sentence worker3 had inserted into the worker6 report (E5). Then re-ran the scan (E2) and regenerated this report.
8. Dispatched worker5 (ADVERSARIAL, narrow) on every change made after worker4. It returned FAIL with 9 MINOR findings.
9. Fixed all nine as text edits (see Adversarial findings), appended a sixth MANIFEST row for the worker5 report (E3), re-ran E2 and E5 and regenerated this report. My turn budget ran out before a further adversarial re-check of those nine fixes.

## Disclosed alterations (check 4)
These two edits change bytes in existing reports. Both are shown in E1 with the address masked as `(address withheld)` on the `<` side.
- docs/reports/2026-11-11-v-rulings-filing-worker2.md:169. Before: a disposition note giving the sender address of the MFFU reply itself (E6: it is the address in the header of the MFFU reply at return-handoff line 114, same_address=YES), inside backticks, followed by "(A:114, 132). This is a public company address. Kept." After: the backticks hold the words `MFFU's public support address`; the rest of the line is unchanged. Size 11554 to 11556 bytes, still 179 lines, every other line byte-identical (E1).
- docs/reports/2026-11-11-v-rulings-filing-worker5.md:79. Before: a pasted commit trailer, `Co-Authored-By: Claude Opus 5.5` followed by a no-reply address in parentheses (E5: local part and domain checked without printing the address). After: `Co-Authored-By: Claude Opus 5.5 (noreply address withheld)`. Size 19841 to 19844 bytes, still 241 lines, every other line byte-identical (E1).
- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:114 and :132 were not changed (master's application: email-header quotes of the MFFU support address). E2 shows they are the only two email hits in the working copy of the bead's files, in the DECISIONS.md added lines and in the bead's MANIFEST added lines. Note: 83891f6 (the parked tip) is not an ancestor of HEAD (E5). As committed at 83891f6, the two files whose address lines this unit edited also carried one email line each (E6: email_lines 2, 1 and 1).

## Verification evidence (command output)
All commands ran under bash from the repo root. The script files are listed with `cat` so every command is literal. Output of a script that defines `mask`, or a `run()` with the same perl substitution, passes through it; it replaces the rep's name with `<NAME>` and any email address with `(address withheld)`. Other blocks are not masked; the self-check at the end of this report shows 0 name hits and 0 email lines in the whole file. `N` is built at runtime from the evidence filename and never printed.

### E1. Append-only, edit scope, self-checks (my re-run of worker1's claims)
```
$ cat /tmp/c3mgr/v1.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
export -f mask
date "+%Y-%m-%dT%H:%M:%S"
for f in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md; do
  r "diff -d /tmp/c3pre/$f docs/reports/$f | grep -v '^>'"
  r "diff -d /tmp/c3pre/$f docs/reports/$f | grep -c '^<'"
  r "wc -l /tmp/c3pre/$f docs/reports/$f"
  r "tail -n 1 /tmp/c3pre/$f | cmp - <(tail -n 1 docs/reports/$f) && echo last-line-identical"
done
r "cmp <(head -n 205 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md) <(head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) && echo M-body-1-205-identical"
r "cmp <(head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo W6-body-1-206-identical"
for p in "2026-11-11-v-rulings-filing-worker2.md 169" "2026-11-11-v-rulings-filing-worker5.md 79"; do set -- $p
  r "diff /tmp/c3pre/$1 docs/reports/$1"
  r "cmp <(sed ${2}d /tmp/c3pre/$1) <(sed ${2}d docs/reports/$1) && echo other-lines-identical"
  r "wc -lc /tmp/c3pre/$1 docs/reports/$1"
  r "grep -cE '$EM' /tmp/c3pre/$1 docs/reports/$1"
done
r "/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md"
r "grep -nE '\.\.\.|<[a-z][a-z ,0-9-]*>' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | awk -F: '\$1>205' | cut -c1-160"
r "grep -nE '\.\.\.|<[a-z][a-z ,0-9-]*>' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | awk -F: '\$1>206' | cut -c1-160"
r "git diff --cached --name-only | wc -l"
$ /tmp/c3mgr/v1.sh
2026-11-11T19:50:55
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -v '^>'
205a206,463
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c '^<'
0
$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md
     464 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     670 total
$ tail -n 1 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md | cmp - <(tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) && echo last-line-identical
last-line-identical
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'
206a207,365
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c '^<'
0
$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     207 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
     366 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     573 total
$ tail -n 1 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | cmp - <(tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo last-line-identical
last-line-identical
$ cmp <(head -n 205 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md) <(head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) && echo M-body-1-205-identical
M-body-1-205-identical
$ cmp <(head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo W6-body-1-206-identical
W6-body-1-206-identical
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md
169c169
< 3. `(address withheld)` (A:114, 132). This is a public company address. Kept.
---
> 3. `MFFU's public support address` (A:114, 132). This is a public company address. Kept.
$ cmp <(sed 169d /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md) <(sed 169d docs/reports/2026-11-11-v-rulings-filing-worker2.md) && echo other-lines-identical
other-lines-identical
$ wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md
     179   11554 /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md
     179   11556 docs/reports/2026-11-11-v-rulings-filing-worker2.md
     358   23110 total
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md
/tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md:1
docs/reports/2026-11-11-v-rulings-filing-worker2.md:0
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
79c79
< Co-Authored-By: Claude Opus 5.5 ((address withheld))
---
> Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
$ cmp <(sed 79d /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md) <(sed 79d docs/reports/2026-11-11-v-rulings-filing-worker5.md) && echo other-lines-identical
other-lines-identical
$ wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
     241   19841 /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md
     241   19844 docs/reports/2026-11-11-v-rulings-filing-worker5.md
     482   39685 total
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
/tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md:1
docs/reports/2026-11-11-v-rulings-filing-worker5.md:0
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[464] last_nonblank_line=464 last_nonblank_is_S13=YES lines=464
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[366] last_nonblank_line=366 last_nonblank_is_S13=YES lines=366
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[241] last_nonblank_line=241 last_nonblank_is_S13=YES lines=241
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[641] last_nonblank_line=641 last_nonblank_is_S13=YES lines=641
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -nE '\.\.\.|<[a-z][a-z ,0-9-]*>' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | awk -F: '$1>205' | cut -c1-160
271:# usage: selfcheck.sh <file>... ; prints counts only, never the name or the S13 sentence
376:$ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <worker2, worker5, worker6 reports>
382:Result: the counts reproduce (0, 0 and 0). The format does not. Lines 164-166 show `<filename>: 0`, with the bare filename and a space. `grep -c` with sever
$ grep -nE '\.\.\.|<[a-z][a-z ,0-9-]*>' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | awk -F: '$1>206' | cut -c1-160
231:### C3.1 Line 16: the command with placeholders `<a c d>`, `<e>`, `<this report>` and an undefined `$R`
361:- IPv4: does NOT reproduce as stated. The scan matches 2 lines, not 1: line 11 (the Criteria section) and line 34, the claim sentence itself, which also con
$ git diff --cached --name-only | wc -l
       1
$ cat /tmp/c3mgr/v2.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
date "+%Y-%m-%dT%H:%M:%S"
r "diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -v '^>'"
r "diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c '^<'"
r "diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'"
r "diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c '^<'"
r "wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md"
r "grep -n '^## Correction 3\|^### C3\.' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md"
r "/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md"
r "git diff --cached --name-only | grep -vc '^docs/reports/evidence/'"
$ /tmp/c3mgr/v2.sh
2026-11-11T20:17:07
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -v '^>'
205a206,589
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c '^<'
0
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'
206a207,486
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c '^<'
0
$ wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
     590 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     487 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     678 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
     146 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
    1901 total
$ grep -n '^## Correction 3\|^### C3\.' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:206:## Correction 3 (2026-11-12)
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:230:### C3.1 Line 105 (E5): the `cmp` line with elided paths and an undefined `$P`
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:255:### C3.2 Line 146 (E6): the `selfcheck.sh` count line with elided arguments
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:307:### C3.3 Line 153 (E7): `pii.py` with a described file list, and line 162
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:370:### C3.4 Line 163 (E7): `grep -cE` with a described file list
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:384:### C3.5 Line 184 (Adversarial findings): the agent-memory claims
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:446:### C3.6 Line 204: self-check output joined on one line
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:461:### C3.7 Summary
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:464:### C3.8 Variables used in other original commands
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:566:### C3.9 Search of /tmp for a pre-edit copy of the memory file
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:207:## Correction 3 (2026-11-12)
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:231:### C3.1 Line 16: the command with placeholders `<a c d>`, `<e>`, `<this report>` and an undefined `$R`
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:334:### C3.2 Line 34: stale self-check fields, and "The only IPv4, MAC or email hit in this report is the 127.0.0.1 in the Criteria section"
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:363:### C3.3 Summary
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:366:### C3.4 Variables used in other original commands
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[590] last_nonblank_line=590 last_nonblank_is_S13=YES lines=590
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[487] last_nonblank_line=487 last_nonblank_is_S13=YES lines=487
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[678] last_nonblank_line=678 last_nonblank_is_S13=YES lines=678
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[146] last_nonblank_line=146 last_nonblank_is_S13=YES lines=146
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ git diff --cached --name-only | grep -vc '^docs/reports/evidence/'
0
```
The v1 run (19:50:55) came before worker3's insertions, so its line counts for the two correction-2 reports (464, 366) and the worker1 report (641) are historical; the v2 run (20:17:07) is the current state after worker3 (590, 487, 678). The last command of v1 counts 1 staged path. It is under docs/reports/evidence/ (count below) and is not a path this unit touched; it was already shown as added in the index in the session-start status snapshot, which this unit did not produce and cannot re-run (REPORTED, not re-runnable). Outside docs/reports/evidence/ the staged count is 0.
```
$ git diff --cached --name-only | wc -l
       1
$ git diff --cached --name-only | grep -c '^docs/reports/evidence/'
1
$ git diff --cached --name-only | grep -vc '^docs/reports/evidence/'
0
$ git rev-parse --short HEAD
a962475
```

### E2. Full email scan and rep-name scan (steps 5 and 6)
The scan set is the paths `git diff --name-only d056e91 83891f6` lists other than MANIFEST.md and DECISIONS.md (24 paths, not the 25 the brief named; the count commands are below), plus every correction-3 report, plus the four files edited here, de-duplicated. DECISIONS.md is scanned as its added lines against d056e91. Line numbers only; no address or name is printed.
```
$ git diff --name-only d056e91 83891f6 | wc -l
      26
$ git diff --name-only d056e91 83891f6 | grep -c '^docs/reports/evidence/'
0
$ git diff --name-only d056e91 83891f6 | grep -cxE 'MANIFEST\.md|DECISIONS\.md'
2
$ git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | wc -l
      24
$ cat /tmp/c3mgr/scan.sh
#!/bin/bash
# step 5 (email) and step 6 (name) scan; prints counts and line numbers only, never an address or the name
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
v1() { perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }' "$@"; }
echo "name_len=${#N}"
{ git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md'
  ls docs/reports/2026-11-12-v-rulings-filing-correction-3-*.md
  printf '%s\n' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
} | sort -u > /tmp/c3mgr/scanset.txt
echo "files_in_set=$(wc -l < /tmp/c3mgr/scanset.txt | tr -d ' ')"
tot=0
while read -r f; do
  e=$(grep -cE "$EM" "$f"); el=$(grep -nE "$EM" "$f" | cut -d: -f1 | tr '\n' ',' | sed 's/,$//')
  c=$(grep -ci -- "$N" "$f"); s=$(v1 "$f")
  echo "$f email_lines=$e at=[$el] name_ci=$c name_split=$s"
  tot=$((tot+e))
done < /tmp/c3mgr/scanset.txt
echo "email_lines_total_files=$tot"
git diff d056e91 -- DECISIONS.md | grep '^+' | grep -v '^+++' > /tmp/c3mgr/dec_added.txt
echo "DECISIONS.md added lines=$(wc -l < /tmp/c3mgr/dec_added.txt | tr -d ' ') email_lines=$(grep -cE "$EM" /tmp/c3mgr/dec_added.txt) name_ci=$(grep -ci -- "$N" /tmp/c3mgr/dec_added.txt) name_split=$(v1 /tmp/c3mgr/dec_added.txt)"
git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' > /tmp/c3mgr/man_bead_added.txt
echo "MANIFEST.md bead added lines (d056e91..83891f6)=$(wc -l < /tmp/c3mgr/man_bead_added.txt | tr -d ' ') email_lines=$(grep -cE "$EM" /tmp/c3mgr/man_bead_added.txt) name_ci=$(grep -ci -- "$N" /tmp/c3mgr/man_bead_added.txt) name_split=$(v1 /tmp/c3mgr/man_bead_added.txt)"
tail -n "${MROWS:-4}" MANIFEST.md > /tmp/c3mgr/manifest_tail.txt
echo "MANIFEST.md last ${MROWS:-4} rows email_lines=$(grep -cE "$EM" /tmp/c3mgr/manifest_tail.txt) name_ci=$(grep -ci -- "$N" /tmp/c3mgr/manifest_tail.txt) name_split=$(v1 /tmp/c3mgr/manifest_tail.txt)"
ctl=$(printf 'x %s y\n' "$(echo "$N" | sed 's/./&-/g; s/-$//')" | v1)
echo "positive controls: name_split_on_hyphenated_synthetic=$ctl email_on_synthetic=$(printf 'a.b%sc-d.example\n' '@' | grep -cE "$EM")"
$ MROWS=6 /tmp/c3mgr/scan.sh
name_len=4
files_in_set=30
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md email_lines=2 at=[114,132] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker10.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker6.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker7.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker8.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker9.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172802Z-STATUS.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172933Z-python-git-install.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172940Z-STATUS.md email_lines=0 at=[] name_ci=0 name_split=0
email_lines_total_files=2
DECISIONS.md added lines=104 email_lines=0 name_ci=0 name_split=0
MANIFEST.md bead added lines (d056e91..83891f6)=27 email_lines=0 name_ci=0 name_split=0
MANIFEST.md last 6 rows email_lines=0 name_ci=0 name_split=0
positive controls: name_split_on_hyphenated_synthetic=1 email_on_synthetic=1
```
Result: exactly two email hits, docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md lines 114 and 132, the expected ones. Rep-name count 0 and split-letter count 0 in every file of the set, in the DECISIONS.md added lines and in the new MANIFEST rows. Both positive controls fire (1 and 1). The two hit lines, address masked:
```
$ N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N; sed -n '114p;132p' docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
### Reply to V1 — 2026-11-10T19:43:42Z, from (address withheld) (message `1a1c6fce04330f0d`), verbatim:
### Reply to V6 — 2026-11-10T23:08:17Z, from (address withheld) (message `1a1c7b82f130416b`)
```

### E3. MANIFEST rows
Correction 3c note (REPORTED): rows were appended to MANIFEST.md after line 420 in Correction 3c, after E2, E3 and E6 were captured; those blocks and the Files staged count show MANIFEST.md as it was then (E2's last six rows were then rows 415-420).
```
$ diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -v '^>'
414a415,420
$ diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -c '^<'
0
$ wc -l /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md
     414 /tmp/c3mgr/MANIFEST.pre.md
     420 MANIFEST.md
     834 total
$ tail -n 6 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md 
```

### E5. Fixes for worker4's findings, and the final checks of the other reports
Correction 3b note: the output below was captured in Correction 3, before the Correction 3b edits to the worker2 and worker3 reports. E6 pastes the current diffs.
```
$ cat /tmp/c3mgr/e6.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
run() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
date "+%Y-%m-%dT%H:%M:%S"
echo "--- finding 1: scan script source"
run "diff /tmp/c3mgr/pre5/scan.sh /tmp/c3mgr/scan.sh | sed -E 's/a\.b@c-d\.example/(synthetic address withheld)/'"
run "grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/pre5/scan.sh /tmp/c3mgr/scan.sh"
echo "--- finding 5: worker6 report"
run "diff /tmp/c3mgr/pre5/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md"
run "diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'"
echo "--- finding 6: worker3 report"
run "diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -v '^>'"
run "diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -c '^<'"
echo "--- finding 7: worker2 report"
run "diff /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md"
run "diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'"
echo "--- out of scope: rep name in MANIFEST.md (line numbers and counts only)"
run 'grep -ni -- "$N" MANIFEST.md | cut -d: -f1'
run 'git show d056e91:MANIFEST.md | grep -ci -- "$N"'
run 'git show HEAD:MANIFEST.md | grep -ci -- "$N"'
run 'git diff d056e91 83891f6 -- MANIFEST.md | grep "^+" | grep -ci -- "$N"'
run 'git diff HEAD -- MANIFEST.md | grep "^+" | grep -ci -- "$N"'
run "sed -n '335,336p' MANIFEST.md | grep -c 'docs/reports/evidence/'"
echo "--- S13, name, email, banned strings: every new correction-3 report except this one, and the four edited reports"
run "/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md"
run "grep -ciwE 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md"
run "grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md"
run "/tmp/vrf-c2/selfcheck.sh /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md"
run "git diff --cached --name-only | grep -vc '^docs/reports/evidence/'"
run "git rev-parse --short HEAD"
echo "--- worker5 findings"
run "diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -v '^>'"
run "diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -c '^<'"
run "sed -n 79p /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -c \"noreply\$(printf '\\x40')anthropic\\.\""
run "git merge-base --is-ancestor 83891f6 HEAD; echo is-ancestor-rc=\$?"
run "grep -c '2026-11-12T00:37:30Z' DECISION_LOG.md"
run "date -r \$(date -j -u -f '%Y-%m-%dT%H:%M:%SZ' 2026-11-12T00:37:30Z +%s) '+%Y-%m-%dT%H:%M:%S'"
$ /tmp/c3mgr/e6.sh
2026-11-11T20:36:24
--- finding 1: scan script source
$ diff /tmp/c3mgr/pre5/scan.sh /tmp/c3mgr/scan.sh | sed -E 's/a\.b@c-d\.example/(synthetic address withheld)/'
22a23,24
> git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' > /tmp/c3mgr/man_bead_added.txt
> echo "MANIFEST.md bead added lines (d056e91..83891f6)=$(wc -l < /tmp/c3mgr/man_bead_added.txt | tr -d ' ') email_lines=$(grep -cE "$EM" /tmp/c3mgr/man_bead_added.txt) name_ci=$(grep -ci -- "$N" /tmp/c3mgr/man_bead_added.txt) name_split=$(v1 /tmp/c3mgr/man_bead_added.txt)"
26c28
< echo "positive controls: name_split_on_hyphenated_synthetic=$ctl email_on_synthetic=$(printf '(synthetic address withheld)\n' | grep -cE "$EM")"
---
> echo "positive controls: name_split_on_hyphenated_synthetic=$ctl email_on_synthetic=$(printf 'a.b%sc-d.example\n' '@' | grep -cE "$EM")"
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/pre5/scan.sh /tmp/c3mgr/scan.sh
/tmp/c3mgr/pre5/scan.sh:1
/tmp/c3mgr/scan.sh:0
--- finding 5: worker6 report
$ diff /tmp/c3mgr/pre5/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
485c485
< With these definitions the 37 lines can be run as written, but none was re-run here. Their original output stands as pasted at the time.
---
> With these definitions the 37 lines may be re-runnable, but that is UNVERIFIED: none was re-run here. Their original output stands as pasted at the time.
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'
206a207,486
--- finding 6: worker3 report
$ diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -v '^>'
145a146,167
$ diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -c '^<'
0
--- finding 7: worker2 report
$ diff /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
19c19
< Written by the unit manager, not by worker2. Worker2 stopped at its 40-turn limit before it wrote its findings (REPORTED: this comes from the harness notification to the manager, which is not a command output and cannot be re-run). The sections above are its skeleton, unchanged. This report carries no adversarial result and the unit does not rely on it. Its working files are in /tmp/c3w2/; the sizes and times, taken just before this note was added:
---
> Written by the unit manager, not by worker2. Worker2 stopped at its 40-turn limit before it wrote its findings (REPORTED: this comes from the harness notification to the manager, which is not a command output and cannot be re-run). The sections above are its skeleton, unchanged (the diff against the pre-note copy is in the manager report, E4: one insertion, 0 deleted lines). This report carries no adversarial result and the unit does not rely on it. Its working files are in /tmp/c3w2/; the sizes and times, taken just before this note was added:
29c29
< The report above was last written before the evidence file. The leads in that evidence file were followed up by worker3 (BUILD fix) and checked again by worker4 (a fresh ADVERSARIAL pass); see docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md.
---
> The report above was last written before the evidence file. REPORTED by the manager (dispatches are events, not command outputs): the leads in that evidence file were passed to worker3 (BUILD fix), and a fresh ADVERSARIAL pass (worker4) was dispatched after this note was written; its result is in docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md, not here.
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
0
--- out of scope: rep name in MANIFEST.md (line numbers and counts only)
$ grep -ni -- "$N" MANIFEST.md | cut -d: -f1
335
336
$ git show d056e91:MANIFEST.md | grep -ci -- "$N"
2
$ git show HEAD:MANIFEST.md | grep -ci -- "$N"
2
$ git diff d056e91 83891f6 -- MANIFEST.md | grep "^+" | grep -ci -- "$N"
0
$ git diff HEAD -- MANIFEST.md | grep "^+" | grep -ci -- "$N"
0
$ sed -n '335,336p' MANIFEST.md | grep -c 'docs/reports/evidence/'
1
--- S13, name, email, banned strings: every new correction-3 report except this one, and the four edited reports
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[678] last_nonblank_line=678 last_nonblank_is_S13=YES lines=678
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[31] last_nonblank_line=31 last_nonblank_is_S13=YES lines=31
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[168] last_nonblank_line=168 last_nonblank_is_S13=YES lines=168
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[749] last_nonblank_line=749 last_nonblank_is_S13=YES lines=749
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[590] last_nonblank_line=590 last_nonblank_is_S13=YES lines=590
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[487] last_nonblank_line=487 last_nonblank_is_S13=YES lines=487
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[241] last_nonblank_line=241 last_nonblank_is_S13=YES lines=241
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -ciwE 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md:0
$ grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md:0
$ /tmp/vrf-c2/selfcheck.sh /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md
/tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ git diff --cached --name-only | grep -vc '^docs/reports/evidence/'
0
$ git rev-parse --short HEAD
a962475
--- worker5 findings
$ diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -v '^>'
640a641,677
$ diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -c '^<'
0
$ sed -n 79p /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -c "noreply$(printf '\x40')anthropic\."
1
$ git merge-base --is-ancestor 83891f6 HEAD; echo is-ancestor-rc=$?
is-ancestor-rc=1
$ grep -c '2026-11-12T00:37:30Z' DECISION_LOG.md
1
$ date -r $(date -j -u -f '%Y-%m-%dT%H:%M:%SZ' 2026-11-12T00:37:30Z +%s) '+%Y-%m-%dT%H:%M:%S'
2026-11-11T19:37:30
```

### E4. Worker2 report: manager note, and the leads in its evidence file
```
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
17a18,30
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
0
$ grep -n '^--- E' /tmp/c3w2/final.out
3:--- E1 (f) byte checks against /tmp/c3pre
22:--- E2 (c) email regex and obfuscated forms, all six artifact files
37:--- E3 (d)(e) name, split-letter detector and S13, all six artifact files
51:--- E4 (a) command lines inside the two inserted sections
56:--- E5 (a) placeholder commands in the original bodies that Correction 3 does not re-run
82:--- E6 (b)(g) lines cited in the MINOR findings
150:--- E7 independent re-runs of the Correction 3 checks (pre-insertion copies where the section measured the pre-insertion file)
$ grep -c '^\$ ' /tmp/c3w2/final.out
68
```

### E6. Correction 3b backing pastes
Added in Correction 3b for lines the re-check found unpasted. Counts, line numbers and masked text only.
```
$ cat /tmp/c3b/mgr/e7.sh
#!/bin/bash
# Correction 3b backing pastes for the Correction 3 manager report; counts, line numbers and masked text only
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
run() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
echo "--- worker4 and worker5 result lines (Workers dispatched, Adversarial findings)"
run "grep -n '^FAIL\. [0-9] MAJOR, [0-9] MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md"
echo "--- leads in worker2's evidence file (Workers dispatched, worker2)"
run "sed -n '56p;64,65p;84p;126,127p' /tmp/c3w2/final.out | cut -c1-160"
echo "--- helper scripts and /tmp directories (Process log step 2, Files staged)"
run "ls -d /tmp/vrf-c2/selfcheck.sh /tmp/vrf-c2/lib.sh /tmp/c2mgr/pii.py /tmp/c3pre /tmp/c3w1 /tmp/c3w2 /tmp/c3w3 /tmp/c3w4 /tmp/c3w5 /tmp/c3mgr"
echo "--- the address masked at filing-worker2:169 is the one in the MFFU reply header (Disclosed alterations)"
run "sed -n 112p docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | grep -o '^## MFFU replies to V1 and V6'"
run "a=\$(sed -n 169p /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md | grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | sort -u); b=\$(sed -n 114p docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | sort -u); if [ -n \"\$a\" ] && [ \"\$a\" = \"\$b\" ]; then echo same_address=YES; else echo same_address=NO; fi"
echo "--- email lines in the three files as committed at 83891f6 (Disclosed alterations, scope of E2)"
run "for f in docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md; do echo \"\$f at 83891f6 email_lines=\$(git show 83891f6:\$f | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')\"; done"
echo "--- line counts of every path in Files staged"
run "wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md MANIFEST.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md"
echo "--- S13 and name counts for the worker5 report, and for the worker2 and worker3 reports after the Correction 3b edits"
run "/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md"
echo "--- worker2 and worker3 reports against their pre-note copies, after the Correction 3b edits"
run "diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'"
run "diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'"
run "diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -v '^>'"
run "diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -c '^<'"
$ /tmp/c3b/mgr/e7.sh
--- worker4 and worker5 result lines (Workers dispatched, Adversarial findings)
$ grep -n '^FAIL\. [0-9] MAJOR, [0-9] MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md:747:FAIL. 1 MAJOR, 6 MINOR.
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md:305:FAIL. 0 MAJOR, 9 MINOR. Items 4 and 5 hold, and the E2, E5 and self-check re-runs reproduce (run1).
--- leads in worker2's evidence file (Workers dispatched, worker2)
$ sed -n '56p;64,65p;84p;126,127p' /tmp/c3w2/final.out | cut -c1-160
--- E5 (a) placeholder commands in the original bodies that Correction 3 does not re-run
$ head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -cE "(^|[^A-Za-z0-9_])(P|PA|T)="
0
- "Restoration to the exact prior bytes is UNVERIFIED": stays UNVERIFIED. Nothing above tests it, and no pre-edit copy exists.
$ sed -n 4p docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -oE "Nothing under vm/ or .claude/ was written."
Nothing under vm/ or .claude/ was written.
--- helper scripts and /tmp directories (Process log step 2, Files staged)
$ ls -d /tmp/vrf-c2/selfcheck.sh /tmp/vrf-c2/lib.sh /tmp/c2mgr/pii.py /tmp/c3pre /tmp/c3w1 /tmp/c3w2 /tmp/c3w3 /tmp/c3w4 /tmp/c3w5 /tmp/c3mgr
/tmp/c2mgr/pii.py
/tmp/c3mgr
/tmp/c3pre
/tmp/c3w1
/tmp/c3w2
/tmp/c3w3
/tmp/c3w4
/tmp/c3w5
/tmp/vrf-c2/lib.sh
/tmp/vrf-c2/selfcheck.sh
--- the address masked at filing-worker2:169 is the one in the MFFU reply header (Disclosed alterations)
$ sed -n 112p docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | grep -o '^## MFFU replies to V1 and V6'
## MFFU replies to V1 and V6
$ a=$(sed -n 169p /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md | grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | sort -u); b=$(sed -n 114p docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' | sort -u); if [ -n "$a" ] && [ "$a" = "$b" ]; then echo same_address=YES; else echo same_address=NO; fi
same_address=YES
--- email lines in the three files as committed at 83891f6 (Disclosed alterations, scope of E2)
$ for f in docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md; do echo "$f at 83891f6 email_lines=$(git show 83891f6:$f | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')"; done
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md at 83891f6 email_lines=2
docs/reports/2026-11-11-v-rulings-filing-worker2.md at 83891f6 email_lines=1
docs/reports/2026-11-11-v-rulings-filing-worker5.md at 83891f6 email_lines=1
--- line counts of every path in Files staged
$ wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md MANIFEST.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
     590 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     487 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     179 docs/reports/2026-11-11-v-rulings-filing-worker2.md
     241 docs/reports/2026-11-11-v-rulings-filing-worker5.md
     420 MANIFEST.md
     678 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
      38 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
     174 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
     749 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
     335 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
    3891 total
--- S13 and name counts for the worker5 report, and for the worker2 and worker3 reports after the Correction 3b edits
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[38] last_nonblank_line=38 last_nonblank_is_S13=YES lines=38
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[174] last_nonblank_line=174 last_nonblank_is_S13=YES lines=174
V1 positive control (hyphen-split synthetic line): HIT_lines=1
--- worker2 and worker3 reports against their pre-note copies, after the Correction 3b edits
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
17a18,37
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
0
$ diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -v '^>'
145a146,173
$ diff -d /tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -c '^<'
0
```

## Adversarial findings
Worker4 (ADVERSARIAL, docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md) returned FAIL with 1 MAJOR and 6 MINOR findings (E6). Each disposition below points to pasted output.
1. MAJOR: this report pasted the source of /tmp/c3mgr/scan.sh, whose email positive control held a literal synthetic address, so this report had one email hit and the "exactly two hits" claim was false. Fixed: the control now builds the address at runtime, so the source holds none (E5, finding 1: the diff, and email count 1 then 0). E2 was re-run after the fix and shows exactly two hits, return-handoff lines 114 and 132; the self-check at the end of this report shows 0 email lines here.
2. MINOR: the "Files staged" list gave this report's line count from a run made before the report was assembled. Fixed: this report's own row no longer gives a count; the self-check block at the end of this report gives `lines=`.
3. MINOR: the S13 claim for "each new report" had no paste for the correction-3 worker2 report. Fixed: E5 runs selfcheck.sh on worker1, worker2, worker3 and worker4 of this unit and on the four edited reports (S13_standalone=1 and last_nonblank_is_S13=YES for all eight); this report is covered by the self-check at the end.
4. MINOR: the process log said the MANIFEST rows were appended in two steps. Fixed: the process log was rewritten; E3 shows the rows as one block against the pre-append copy (the sixth row, 420, was added after worker5).
5. MINOR: the worker6 report's inserted C3.4 said the 37 lines "can be run as written" without running them. Fixed by me: that sentence now says it is UNVERIFIED (E5, finding 5: one-line diff at 485). It sits inside the Correction 3 section, so the file is still an insertion only against /tmp/c3pre (`206a207,486`, E5).
6. MINOR: the worker3 report gave "about 26" and "19:39:57" with no paste in that file. Fixed: a manager note before its final line pastes both sources and labels the start time INFERRED (E5, finding 6: insertion `145a146,167`, 0 `<` lines).
7. MINOR: the manager note in the worker2 report said worker4 had "checked again" before worker4 ran. Fixed: the sentence now says worker4 was dispatched after the note was written (E5, finding 7: one-line diff at 29; against the pre-note copy still 0 `<` lines).
- Out of scope, reported and not fixed: worker4 reported the rep's name in MANIFEST.md at lines 335 and 336. E5 shows they were already there at d056e91 and are committed at HEAD (count 2 in both), the bead added none (0 in the d056e91..83891f6 added lines) and this unit added none (0 in the added lines against HEAD); one of the two lines names a path under docs/reports/evidence/. The brief limits MANIFEST edits to the new rows (REPORTED: the Correction 3 brief is not pasted in this report), so this goes to the master.
- Also pre-existing and not changed: the 2026-11-11 worker2 report has S13_containing=3 with S13_standalone=1, before and after the line-169 edit (E5, the /tmp/c3pre copy; E1).
- Worker5 (ADVERSARIAL, narrow): FAIL with 0 MAJOR and 9 MINOR findings (E6; docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md). I addressed all nine by text edits after it returned: this report's lines on S13 coverage, the worker1 insertion, the MANIFEST step, the no-reply address, the MANIFEST scan and the ancestry of 83891f6, the S6 basis and the /tmp list, plus the REPORTED label on the process log (new commands in E2 and E5); the worker3 note (start-time reasoning, REPORTED label on the brief figure); the worker2 note (pointer to E4, REPORTED label on dispatches).

## S6 cross-block check
Not applicable. This unit approves no deviation. Every file in the Files staged list below is a report under docs/reports/ or MANIFEST.md (E6 pastes `wc -l` on each of them except this report, whose count is in the self-check at the end); no block spec, code, hook or setting is among them. It is append-only text corrections in two reports, two masked addresses, new reports and MANIFEST rows.

## Files staged
None by this unit (S7; E1). Written or edited in the working copy only:
- docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: 590 lines; edited: lines 206-589 inserted (Correction 3, worker1 then worker3); original lines 1-205 and the final line unchanged.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: 487 lines; edited: lines 207-486 inserted (Correction 3, worker1 then worker3); original lines 1-206 and the final line unchanged.
- docs/reports/2026-11-11-v-rulings-filing-worker2.md: 179 lines; edited: line 169, address replaced by words (disclosed above).
- docs/reports/2026-11-11-v-rulings-filing-worker5.md: 241 lines; edited: line 79, address masked (disclosed above).
- MANIFEST.md: 420 lines; edited: rows 415-420 appended.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: 678 lines; new.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: 38 lines; new; skeleton plus manager note at lines 18-37 (two sentences of it reworded by me after worker5; REPORTED: edited again in Correction 3b).
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: 174 lines; new.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: 749 lines; new.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: 335 lines; new.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: new; this report (line count in the self-check below).
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md also carries a manager note at its lines 146-173 (REPORTED: edited in Correction 3b); docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md line 485 was reworded by me inside the inserted section (E5).
- Outside the repo: /tmp/c3pre (pre-edit copies), /tmp/c3w1, /tmp/c3w2, /tmp/c3w3, /tmp/c3w4, /tmp/c3w5 (worker scripts), /tmp/c3mgr (my scripts and outputs); E6 lists them with `ls -d`.

Self-check of this report, run on the final file. The block below was regenerated (/tmp/c3mgr/assemble.py; in Correction 3b, /tmp/c3b/mgr/fixA.py; in Correction 3c, /tmp/c3c/mgr/regen.py) until the output it contains equals the output of the same command run on the file that contains it:
```
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -ciw 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[607] last_nonblank_line=607 last_nonblank_is_S13=YES lines=607
V1 positive control (hyphen-split synthetic line): HIT_lines=1
0
0
0
```

Result: BLOCKED
What it needs: one narrow ADVERSARIAL re-check of the edits made after worker5 returned (this report's dispositions and E2/E5 additions, the manager notes in the correction-3 worker2 and worker3 reports). Every other step is done and its output is pasted above; nothing is staged by this unit.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
