# 2026-11-12 — O3 Block 1 milestone scope — correction 1 — ADVERSARIAL worker 1 report

## Task
Mode: ADVERSARIAL, read-only except this one new report. Working directory /Volumes/Sensidine/Praxis.build, branch main, HEAD a411e17. Artifacts under test: A = docs/reports/2026-11-12-o3-block1-scope-manager.md, B = docs/reports/2026-11-12-o3-block1-scope-worker1.md (both edited in place by correction 1; pre-correction copies /tmp/o3c1/manager.orig.md and /tmp/o3c1/worker1.orig.md), C = docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md (the correction report and its Items 1 to 18), and the last 2 MANIFEST.md rows. Criteria 1 to 5 of the brief: edit-log fidelity, rubric S1 (specs/SPEC_RUBRIC.md :127) sweep of all lines of A, B and C, the cure checks, the report rules, de-identification. C's four markers (@@WORKERS@@, @@SCANS@@, @@ADV@@, @@RESULT@@) are not counted as defects. File:line references below use the current files.

## Checks run
1. Report path absent before writing (`test -e`), HEAD.
2. Full `diff` of each pre-correction copy against the current file (pasted in full below); a script parses the 18 Items of C's edit log and compares each OLD text with the pre-correction copy at the stated line, each NEW text with the current file, and checks that no OLD line is left in the current file.
3. S1 sweep: every prose line of A, B and C read against the pasted output in the same report; targeted greps for the claim classes found.
4. Re-run of 23 pasted commands from A (including its "Correction 1 evidence" block and "Report scans" block), B (including its "Correction 1 evidence" block) and C, compared with the pasted output.
5. Report rules on A, B, C (S13 count and last line, Result line, evidence section, banned words, placeholder forms, listing commands) and on this report.
6. De-identification on the lines added by correction 1: the `>` lines of both diffs, all of C and the last 2 MANIFEST rows (504 lines in /tmp/o3c1w/added.txt), and on this report.

## Verification evidence (command output)

### Absence, HEAD, full diffs, edit-log script
```
$ test -e docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md; echo "test -e exit=$?"
test -e exit=1
$ git rev-parse --short HEAD
a411e17
$ diff /tmp/o3c1/manager.orig.md docs/reports/2026-11-12-o3-block1-scope-manager.md; echo "diff exit=$?"
16c16
< No BUILD worker: the filing is a 17-line doc append written by the manager (brief: builder optional).
---
> No BUILD worker for the filing (worker2 above is BUILD for the worker1 report fix only): the filing is a 17-line doc append written by the manager (brief: builder optional).
21c21
< 3. Appended the entry (17 lines, starting with a blank separator) to DECISIONS.md; appended 3 MANIFEST rows; corrected this unit's DECISIONS.md row type column from "Decision log" to "Log" (house value) by one exact-match sed on that row only.
---
> 3. Appended the entry (17 lines, starting with a blank separator) to DECISIONS.md; appended 3 MANIFEST rows; this unit's DECISIONS.md row type column reads "Log" (house value). Correction 1: the earlier text here said how the type column was changed, with no paste; that is withdrawn. The current rows and the after-count are pasted under "Correction 1 evidence"; the before-count cannot be reproduced after the edit and is not claimed.
24c24
< 6. Worker1 defect 1 (pending sections in this report) cured by completing this report; its three minor observations dispositioned below.
---
> 6. Worker1 defect 1 (pending sections in this report) cured by completing this report; its observations O-a, O-b, O-c and its MANIFEST limit dispositioned below (items 2 to 5). Correction 1: "three minor observations" corrected; worker1 lists five observations (count under "Correction 1 evidence"); O-d and O-e get no item.
175c175
< Run on both unit reports after worker2's fix and before this block was pasted. /tmp/o3-placeholders.txt holds the two placeholder forms the brief bans; /tmp/o3-listing-cmds.txt holds the three banned git command forms; /tmp/o3-worker1-orig.md is worker2's pre-edit copy of the worker1 report. The capitalised tokens not in the system word list are product, tool, path or heading words; the only person name is Amear.
---
> Run on both unit reports after worker2's fix and before this block was pasted. /tmp/o3-placeholders.txt holds the two placeholder forms the brief bans; /tmp/o3-listing-cmds.txt holds the three banned git command forms; /tmp/o3-worker1-orig.md is worker2's pre-edit copy of the worker1 report. The capitalised tokens not in the system word list are product, tool, path or heading words; the only person name is Amear. [Correction 1 label: this run predates correction 1, which changed both reports; worker1 line numbers in the last three commands below (diff and Result line) are as at that run; the re-run is in the correction 1 manager report.]
225a226,309
> ```
> 
> ### Correction 1 evidence
> Added by correction 1 after the original run, run against the working tree before correction 1 appended its MANIFEST rows. Claims covered, by pre-correction line of this report: :21 and :234 (the unit's rows as they are now; after-count of "Decision log" 0 case-sensitive, 1 case-insensitive at MANIFEST.md line 155 of 461, outside the last 3 rows); :24 (worker1 lists five observations); :25 and :235 (worker2's pre-edit copy held the S13 sentence at lines 35, 52, 288); :63 (HEAD line 2278 is the S13 sentence and the blob ends in a newline); :79 (/tmp/s13.txt is one line); :92 (numstat 109 added, 0 removed); :139 (MANIFEST hunks add 8, 6 and 3 rows); :155, :172, :175 (line counts of the /tmp list files, contents not printed; the rep pattern re-derived by script from the PNG filename equals /tmp/o3-rep-name.txt); :157 (/tmp/o3-added.txt is the 17 entry lines plus the last 3 MANIFEST rows); :232 (item (4) of the master's row); :233 (17:31Z in the master's row and the entry's Status line); :13 and :14 (the two agent ids occur in DISPATCH_LOG.md); :246 (nothing staged in this unit's four files; both reports absent from HEAD); :249 (no diff to the rubric).
> ```
> $ grep -c -F 'Decision log' MANIFEST.md
> 0
> $ grep -c -i -F 'Decision log' MANIFEST.md
> 1
> $ tail -n 3 MANIFEST.md
> | /DECISIONS.md | Log | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry). Unit 2026-11-12-o3-block1-scope (rubric O3; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T17:31:00Z): appends entry D-2026-11-12-C, "Block 1 milestone scope — internal path only", recording that the Block 1 milestone signed off on 2026-07-15 covers the internal path only and that public TradingView ingress (Deviation G, D-2026-07-09-D) is deferred and untested. Scope record only: no design choice, no test, no re-grade of the sign-off, rubric O3 state unchanged. |
> | /docs/reports/2026-11-12-o3-block1-scope-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-o3-block1-scope (rubric O3; master under D-2026-11-08-D D1): filing of DECISIONS.md entry D-2026-11-12-C, S4 pre-check, HEAD source quote checks, committed-blob line arithmetic and sha256, parked-entry byte-identity check, S6 cross-block check, de-identification scan. |
> | /docs/reports/2026-11-12-o3-block1-scope-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-o3-block1-scope: independent read-only re-check of entry D-2026-11-12-C quotes against HEAD sources, no-design-choice and S2 level check, parked-entry byte-identity, line-range arithmetic, evidence rules on both unit reports. |
> $ tail -n 3 MANIFEST.md | cut -d'|' -f2-3
>  /DECISIONS.md | Log 
>  /docs/reports/2026-11-12-o3-block1-scope-manager.md | Report 
>  /docs/reports/2026-11-12-o3-block1-scope-worker1.md | Report 
> $ git show HEAD:DECISIONS.md | sed -n 2278p | grep -c -x -F -f /tmp/s13.txt
> 1
> $ git show HEAD:DECISIONS.md | tail -c 1 | xxd
> 00000000: 0a                                       .
> $ wc -l < /tmp/s13.txt
>        1
> $ git diff HEAD --numstat -- DECISIONS.md
> 109	0	DECISIONS.md
> $ git diff HEAD -- MANIFEST.md | grep "^@@"
> @@ -304,6 +304,14 @@
> @@ -429,6 +437,12 @@
> @@ -442,3 +456,6 @@
> $ wc -l < /tmp/o3-rep-name.txt
>        1
> $ wc -l < /tmp/o3-med-words.txt
>       40
> $ wc -l < /tmp/o3-banned-words.txt
>        3
> $ wc -l < /tmp/o3-placeholders.txt
>        2
> $ wc -l < /tmp/o3-listing-cmds.txt
>        3
> $ (sed -n 2371,2387p DECISIONS.md; tail -n 3 MANIFEST.md) | cmp - /tmp/o3-added.txt && echo identical
> identical
> $ grep -n -F -f /tmp/s13.txt /tmp/o3-worker1-orig.md | cut -d: -f1
> 35
> 52
> 288
> $ grep -c -E '^- O-[a-e]\. ' docs/reports/2026-11-12-o3-block1-scope-worker1.md
> 5
> $ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -o -E '\(4\)[^(]{0,160}'
> (4) rubric O3's move to PASSED is NOT in this unit: it follows in the close flush under A11 + D1 after the entry lands, citing the landing sha. | WHY: rubric O3; D
> $ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -o -F 'DECISION_LOG 2026-11-12T17:31Z' | head -n 1
> $ grep -c -F -e a53f0e5696829473b -e aa39938f1424cfea1 DISPATCH_LOG.md
> 4
> $ grep -c -F -e a53f0e5696829473b -e aa39938f1424cfea1 DECISION_LOG.md
> 0
> $ git diff HEAD --numstat -- specs/SPEC_RUBRIC.md | wc -l
>        0
> $ git diff --cached --quiet -- DECISIONS.md MANIFEST.md docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md; echo "cached-diff exit=$?"
> cached-diff exit=0
> $ git cat-file -e HEAD:docs/reports/2026-11-12-o3-block1-scope-manager.md; echo "in-HEAD exit=$?"
> fatal: path 'docs/reports/2026-11-12-o3-block1-scope-manager.md' exists on disk, but not in 'HEAD'
> in-HEAD exit=128
> $ git cat-file -e HEAD:docs/reports/2026-11-12-o3-block1-scope-worker1.md; echo "in-HEAD exit=$?"
> fatal: path 'docs/reports/2026-11-12-o3-block1-scope-worker1.md' exists on disk, but not in 'HEAD'
> in-HEAD exit=128
> $ sed -n 2371,2387p DECISIONS.md | grep -c -F 'proven end-to-end'
> 0
> $ sed -n 95p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -c -F 'Deviation G (D-2026-07-09-D)'
> 1
> $ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 110p | grep -c -F 'proven end-to-end'
> 1
> $ grep -n -i -F 'Decision log' MANIFEST.md | cut -d: -f1
> 155
> $ wc -l < MANIFEST.md
>      461
> $ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -c -F '17:31Z'
> 1
> $ for f in docs/reports/evidence/2026-10-28-mffu-*-reply.png; do basename "$f" | sed -E 's/^2026-10-28-mffu-//; s/-reply[.]png$//'; done > /tmp/o3c1/rep-derived.txt; wc -l < /tmp/o3c1/rep-derived.txt
>        1
> $ cmp -s /tmp/o3c1/rep-derived.txt /tmp/o3-rep-name.txt && echo rep-pattern-same || echo rep-pattern-differs
> rep-pattern-same
> $ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -o -E '.{0,30}17:31Z.{0,12}'
> FEST.md, docs/reports | WHEN: 17:31Z | HOW: prax
> $ sed -n 2374p DECISIONS.md | grep -c -F 'DECISION_LOG 2026-11-12T17:31Z'
> 1
233,234c317,318
< 4. Observation: the entry writes 17:31Z, other files 17:31:00Z. Disposition: no change; 17:31Z is the form the brief gave for the Status line.
< 5. Worker1 limit: the 14 earlier MANIFEST rows were confirmed not removed, not byte-identical against a prior hash. Disposition: this unit's only in-place MANIFEST edit was the one sed on its own row, matched by a string that occurred once (count 1 before, 0 after, pasted above); no other row was edited.
---
> 4. Observation: the entry writes 17:31Z, other files 17:31:00Z. Disposition: no change; the master's row DECISION_LOG 2026-11-12T17:31:00Z itself writes 17:31Z, and the entry's Status line cites it in that form (both under "Correction 1 evidence"). Correction 1: the earlier basis, "the form the brief gave", had no paste and is replaced.
> 5. Worker1 limit: the 14 earlier MANIFEST rows were confirmed not removed, not byte-identical against a prior hash. Disposition: this unit's own DECISIONS.md row type column reads "Log" now, and the string "Decision log" occurs 0 times in MANIFEST.md case-sensitive (1 case-insensitive, at line 155, outside the last 3 rows); both pasted under "Correction 1 evidence". Correction 1: the count before the edit cannot be reproduced after the edit and is not claimed; the earlier "count 1 before" and "no other row was edited" had no paste and are withdrawn. No byte-identity of the 14 earlier rows is claimed.
diff exit=1
$ diff /tmp/o3c1/worker1.orig.md docs/reports/2026-11-12-o3-block1-scope-worker1.md; echo "diff exit=$?"
17c17
< All commands were run inside one `/bin/bash -c` call per block from /Volumes/Sensidine/Praxis.build. Each block shows the literal lines and their full output.
---
> All commands were run inside one `/bin/bash -c` call per block from /Volumes/Sensidine/Praxis.build. Each block shows the literal lines and their full output. [Correction 1 label: the first sentence is a process record of worker1's run, not reproducible now and not claimed as evidence.]
35c35
<      6	[the S13 sentence, filtered]
---
>      6	[the S13 sentence, filtered] [Correction 1 label: this output line was altered after the run by the fix worker; see :271–273.]
52c52
<     23	[the S13 sentence, filtered]
---
>     23	[the S13 sentence, filtered] [Correction 1 label: this output line was altered after the run by the fix worker; see :271–273.]
101c101
< The last pipeline returned nothing (exit 1) because "Deviation G" is at rubric :110 and "untested" at :111; the -A4 output above shows both. Topology :112 also names "Deviation G (D-2026-07-09-D)", which sources the Deviation G = D-2026-07-09-D equation.
---
> The last pipeline printed nothing [Correction 1: "(exit 1)" removed, the exit status was not pasted; see "Correction 1 evidence" for the count 0 and the topology :112 check] because "Deviation G" is at rubric :110 and "untested" at :111; the -A4 output above shows both. Topology :112 also names "Deviation G (D-2026-07-09-D)", which sources the Deviation G = D-2026-07-09-D equation.
202c202
< Run before this block and the S13 line were inserted; the inserted text is commands and counts only.
---
> Run before this block and the S13 line were inserted; the inserted text is commands and counts only. [Correction 1 label: process record of worker1's run, not reproducible now and not claimed as evidence.]
269c269
< Person names: every capitalised token above is a word, product, acronym or path part; the only person name is Amear. The first token list is the one from the scan call of the same session (unit DECISIONS and MANIFEST lines plus the manager report). The five /tmp/w1-* setup lines ran in an earlier call of this session and the files were reused. The manager report's s13=0 is noted only, as briefed; this report's s13=0 is before the S13 line was appended.
---
> Person names: every capitalised token above is a word, product, acronym or path part; the only person name is Amear. The first token list is the one from the scan call of the same session (unit DECISIONS and MANIFEST lines plus the manager report). The five /tmp/w1-* setup lines ran in an earlier call of this session and the files were reused. [Correction 1 label: the second and third sentences are process records of worker1's run, not reproducible now and not claimed as evidence.] The manager report's s13=0 is noted only, as briefed; this report's s13=0 is before the S13 line was appended.
275c275
< Output of the two checks, run after the edit (final run):
---
> Output of the two checks, run after the edit (final run): [Correction 1 label: this run predates correction 1, which edited lines and inserted 21 lines in this file; the S13 sentence is still the last line, now line 322; the re-run is in the correction 1 manager report.]
283a284,304
> ### Correction 1 evidence
> Added by the correction 1 manager after the run; these commands were run by the correction 1 manager, not by worker1, before this block was inserted. They cover :101 (the pipeline count 0; topology :112 names Deviation G (D-2026-07-09-D)), O-e (the entry holds no "proven end-to-end"; HEAD :140 and rubric :110 do) and the fix note (the pre-edit copy held the S13 sentence at lines 35, 52 and 288 of 288).
> ```
> $ sed -n 2371,2387p DECISIONS.md | grep -c -F 'proven end-to-end'
> 0
> $ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 110p | grep -c -F 'proven end-to-end'
> 1
> $ git show HEAD:DECISIONS.md | sed -n 140p | grep -c -F 'proven end-to-end'
> 1
> $ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 112p | grep -c -F 'Deviation G (D-2026-07-09-D)'
> 1
> $ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F 'untested' | grep -c -F 'Deviation G'
> 0
> $ grep -n -F -f /tmp/s13.txt /tmp/o3-worker1-orig.md | cut -d: -f1
> 35
> 52
> 288
> $ wc -l < /tmp/o3-worker1-orig.md
>      288
> ```
> 
288c309
< 1. Manager report is incomplete beyond the two parts declared pending. `docs/reports/2026-11-12-o3-block1-scope-manager.md` :10–11 "## Workers dispatched" holds only "(filled below)", :13–14 "## Process log" holds only "(filled below)", and :163 reads "(report scans below)", so the report's own evidence-rule and de-identification scans (S13 count, banned words, rep pattern, medication list, email, person names on the report text) are absent. The brief declared only "Adversarial findings" (:165–166) and the Result line (:178) pending. Evidence: the `(filled below)` / `(report scans below)` grep lines in the scan block below. The S13 sentence is absent from the manager report (count 0, last line "Result: PENDING"); noted only, as briefed.
---
> 1. Manager report is incomplete beyond the two parts declared pending. `docs/reports/2026-11-12-o3-block1-scope-manager.md` :10–11 "## Workers dispatched" holds only "(filled below)", :13–14 "## Process log" holds only "(filled below)", and :163 reads "(report scans below)", so the report's own evidence-rule and de-identification scans (S13 count, banned words, rep pattern, medication list, email, person names on the report text) are absent. The brief declared only "Adversarial findings" (:165–166) and the Result line (:178) pending. Evidence: the `(filled below)` / `(report scans below)` grep lines in the scan block below. At the time worker1 ran, the S13 sentence was absent from the manager report (s13=0 for the manager report in the scan block above); noted only, as briefed. [Correction 1 label: the earlier words on the manager report's last line had no pasted output and are withdrawn; manager report line numbers in this item are as at worker1's run, when it had 178 lines (scan block above).]
297,298c318,319
< - O-d. The topology phrase "Deviation G's ingress question leaves the anchor's live path" is at topology :112 and also :217 (manager report :101–103); the entry cites :112 only, as briefed. The topology doc does not carry the id D-2026-11-10-B; the link is DECISIONS.md :2047 (adopts the topology for rubric F1), which the entry's parenthetical relies on.
< - O-e. S2 read of the entry: it does not claim anything was tested or proven on its own authority. "proven end-to-end" appears only in the HEAD sources (:140, rubric :110), not in the entry. "untested" is attributed to rubric O3 (:111). The ingress-placement claim (Block 4–5) is quoted from :140. The entry makes no design choice and records no ingress decision.
---
> - O-d. The topology phrase "Deviation G's ingress question leaves the anchor's live path" is at topology :112 and also :217 (manager report :101–103, line numbers as at worker1's run); the entry cites :112 only, as briefed. The topology doc does not carry the id D-2026-11-10-B; the link is DECISIONS.md :2047 (adopts the topology for rubric F1), which the entry's parenthetical relies on.
> - O-e. S2 read of the entry: it does not claim anything was tested or proven on its own authority. "proven end-to-end" appears only in the HEAD sources (:140, rubric :110), not in the entry (counts under "Correction 1 evidence"). "untested" is attributed to rubric O3 (:111). The ingress-placement claim (Block 4–5) is quoted from :140. The entry makes no design choice and records no ingress decision.
diff exit=1
$ cat /tmp/o3c1w/chk.py
import re,sys
C=open(sys.argv[1],encoding='utf-8').read().split('\n')
files={'docs/reports/2026-11-12-o3-block1-scope-manager.md':('/tmp/o3c1/manager.orig.md',),
       'docs/reports/2026-11-12-o3-block1-scope-worker1.md':('/tmp/o3c1/worker1.orig.md',)}
items=[];i=0
while i<len(C):
    m=re.match(r'### Item (\d+): `([^`]+)`, (?:line (\d+)|insert after pre-correction :(\d+) \(new lines (\d+) to (\d+)\))',C[i])
    if m:
        blocks=[];j=i+1
        while len(blocks)<2:
            if C[j]=='~~~~text':
                k=j+1
                while C[k]!='~~~~': k+=1
                blocks.append(C[j+1:k]); j=k
            j+=1
        items.append((int(m.group(1)),m.group(2),m.group(3),m.group(4),m.group(5),m.group(6),blocks[0],blocks[1])); i=j
    else: i+=1
print('items parsed',len(items))
for n,f,line,ins,a,b,old,new in items:
    orig=open(files[f][0],encoding='utf-8').read().split('\n')
    cur=open('/Volumes/Sensidine/Praxis.build/'+f,encoding='utf-8').read().split('\n')
    if line:
        L=int(line)
        o_ok = orig[L-1:L-1+len(old)]==old
        cnt_new=sum(1 for x in cur if x==new[0])
        cnt_old_cur=sum(1 for x in cur if x==old[0])
        print(f'Item {n}: orig line {L} == OLD: {o_ok}; NEW lines in current: {cnt_new}; OLD lines left in current: {cnt_old_cur}; OLD bytes {len(old[0].encode())} NEW bytes {len(new[0].encode())}')
    else:
        I=int(ins);A=int(a);B=int(b)
        print(f'Item {n}: insert after {I}; NEW has {len(new)} lines; stated range {A}-{B} = {B-A+1} lines; cur[{A}..{B}]==NEW: {cur[A-1:B]==new}; orig line {I}: {orig[I-1]!r}; cur line {A-1}: {cur[A-2]!r}')
$ python3 -I /tmp/o3c1w/chk.py docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
items parsed 18
Item 1: orig line 16 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 101 NEW bytes 173
Item 2: orig line 21 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 243 NEW bytes 436
Item 3: orig line 24 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 136 NEW bytes 324
Item 4: orig line 233 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 142 NEW bytes 338
Item 5: orig line 234 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 305 NEW bytes 607
Item 6: insert after 226; NEW has 84 lines; stated range 227-310 = 84 lines; cur[227..310]==NEW: True; orig line 226: '```'; cur line 226: '```'
Item 7: orig line 17 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 158 NEW bytes 287
Item 8: orig line 35 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 35 NEW bytes 135
Item 9: orig line 52 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 35 NEW bytes 135
Item 10: orig line 101 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 254 NEW bytes 384
Item 11: orig line 202 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 100 NEW bytes 205
Item 12: orig line 269 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 456 NEW bytes 597
Item 13: orig line 288 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 752 NEW bytes 1016
Item 14: orig line 297 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 357 NEW bytes 391
Item 15: orig line 298 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 365 NEW bytes 404
Item 16: insert after 283; NEW has 21 lines; stated range 284-304 = 21 lines; cur[284..304]==NEW: True; orig line 283: ''; cur line 283: ''
Item 17: orig line 275 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 57 NEW bytes 271
Item 18: orig line 175 == OLD: True; NEW lines in current: 1; OLD lines left in current: 0; OLD bytes 416 NEW bytes 645
$ sed -n 271p docs/reports/2026-11-12-o3-block1-scope-worker1.md
### Fix note (S13 filter)
$ sed -n 273p docs/reports/2026-11-12-o3-block1-scope-worker1.md | cut -c1-60
Lines 35 and 52 of this file (inside the pasted numbered lis
$ grep -c -F 'last line "Result: PENDING"' docs/reports/2026-11-12-o3-block1-scope-worker1.md
0
$ sed -n 259p docs/reports/2026-11-12-o3-block1-scope-worker1.md
  s13=0 result-lines=1 evidence-section=1
$ grep -n -F 'cannot be reproduced' docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
21
318
$ sed -n 279p docs/reports/2026-11-12-o3-block1-scope-worker1.md
301
$ grep -n -F -e 'tail -n 1' -e 'f /tmp/s13.txt' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | cut -c1-110
102:$ git show HEAD:DECISIONS.md | sed -n 2278p | grep -c -x -F -f /tmp/s13.txt
126:$ grep -n -F -f /tmp/s13.txt /tmp/o3-worker1-orig.md | cut -d: -f1
282:$ grep -n -F -f /tmp/s13.txt /tmp/o3-worker1-orig.md | cut -d: -f1
$ sed -n 175p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'the re-run is in the correction 1 manager report'
the re-run is in the correction 1 manager report
$ sed -n 175p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'the last three commands'
the last three commands
$ sed -n 275p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -F 'now line 322; the re-run is in the correction 1 manager report'
now line 322; the re-run is in the correction 1 manager report
$ sed -n 317p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -F '(as the brief prescribes)'
(as the brief prescribes)
$ sed -n 309p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -F -e 'The brief declared only' -e 'as briefed'
The brief declared only
as briefed
$ sed -n 125p docs/reports/2026-11-12-o3-block1-scope-worker1.md
   1 217:D-2026-11-10-A
$ sed -n 318p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -F 'is at topology :112 and also :217'
is at topology :112 and also :217
$ grep -n -F untouched docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
139
$ sed -n 318p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F -e 'no other row was edited' -e 'No byte-identity of the 14 earlier rows is claimed'
no other row was edited
No byte-identity of the 14 earlier rows is claimed
$ sed -n 184p docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -F 'it does not show they are byte-'
it does not show they are byte-
$ sed -n 17p docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | grep -o -F 'by a script that asserts each OLD text is present exactly once on its line'
by a script that asserts each OLD text is present exactly once on its line
$ sed -n 24p docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | grep -o -F -e 'process record of this run' -e 'worker1 pasted output line 149'
process record of this run
worker1 pasted output line 149
$ sed -n 376p docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | grep -o -F 'the one the original reports pasted (7d8f6577)'
the one the original reports pasted (7d8f6577)
$ sed -n 4p docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | grep -o -E 'nothing comm[i]tted'
nothing committed
$ grep -n -F 7d8f6577 docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md | cut -d: -f1-2
docs/reports/2026-11-12-o3-block1-scope-manager.md:73
docs/reports/2026-11-12-o3-block1-scope-worker1.md:147
docs/reports/2026-11-12-o3-block1-scope-worker1.md:157
$ sed -n 14p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'entry, parked block, line arithmetic and MANIFEST rows held'
entry, parked block, line arithmetic and MANIFEST rows held
$ sed -n 320p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'Worker1 confirmed: all 5 quotes byte for byte'
Worker1 confirmed: all 5 quotes byte for byte
$ sed -n 315p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'label is at HEAD :139'
label is at HEAD :139
$ grep -n -F ':139' docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
229
315
$ sed -n 47p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'The entry cites :174 and :175'
The entry cites :174 and :175
$ sed -n 120p docs/reports/2026-11-12-o3-block1-scope-manager.md | grep -o -F 'is attributed to rubric O3'
is attributed to rubric O3
$ grep -n -F 'B1-a' docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
324
```

### Re-run sample and targeted checks
```
$ grep -c -F 'Decision log' MANIFEST.md
0
$ grep -c -i -F 'Decision log' MANIFEST.md
1
$ tail -n 3 MANIFEST.md | cut -d'|' -f2-3
 /docs/reports/2026-11-12-o3-block1-scope-worker1.md | Report 
 /docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | Report 
 /docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md | Report 
$ git show HEAD:DECISIONS.md | sed -n 2278p | grep -c -x -F -f /tmp/s13.txt
1
$ git diff HEAD -- MANIFEST.md | grep "^@@"
@@ -304,6 +304,14 @@
@@ -429,6 +437,12 @@
@@ -442,3 +456,8 @@
$ wc -l < MANIFEST.md
     463
$ grep -c -E '^- O-[a-e]\. ' docs/reports/2026-11-12-o3-block1-scope-worker1.md
5
$ grep -c -F -e a53f0e5696829473b -e aa39938f1424cfea1 DISPATCH_LOG.md
4
$ grep -c -F a53f0e5696829473b DISPATCH_LOG.md
2
$ grep -c -F aa39938f1424cfea1 DISPATCH_LOG.md
2
$ grep -F '[2026-11-12T17:31:00Z]' DECISION_LOG.md | grep -o -E '.{0,30}17:31Z.{0,12}'
FEST.md, docs/reports | WHEN: 17:31Z | HOW: prax
$ sed -n 2374p DECISIONS.md | grep -c -F 'DECISION_LOG 2026-11-12T17:31Z'
1
$ git show HEAD:DECISIONS.md | sed -n 140p | grep -c -F 'proven end-to-end'
1
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F 'untested' | grep -c -F 'Deviation G'
0
$ wc -l < /tmp/o3-worker1-orig.md
     288
$ grep -c -F 'Correction 1' docs/reports/2026-11-12-o3-block1-scope-manager.md
6
$ grep -c -F 'Correction 1' docs/reports/2026-11-12-o3-block1-scope-worker1.md
10
$ git diff HEAD -- MANIFEST.md | grep -c "^-[^-]"
0
$ sed -n 2371,2387p DECISIONS.md | shasum -a 256
7d8f6577dfe6e75fdeb42158ff33e1e3ab29da864d839f16c918360132ed0653  -
$ shasum -a 256 /tmp/o3c1/manager.orig.md /tmp/o3c1/worker1.orig.md
10432dceffdd4a8d2ad02c68e15297a8e616b856b2be121cf1098f8e1ddcea9a  /tmp/o3c1/manager.orig.md
77e1c53345b1c5eb88a870b073050c3fe8239c64b3f2913915d6ed4bf99ffdeb  /tmp/o3c1/worker1.orig.md
$ tail -n 2 MANIFEST.md | cut -d'|' -f2-5
 /docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | Report | 3 | 2026-11-12 
 /docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md | Report | 3 | 2026-11-12 
$ grep -n -F -f /tmp/s13.txt docs/reports/2026-11-12-o3-block1-scope-worker1.md | cut -d: -f1
322
$ grep -n -E '^Result: ' docs/reports/2026-11-12-o3-block1-scope-worker1.md
321:Result: FAIL
$ cat docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md | grep -o -E '\b[A-Z][a-z]+\b' | sort -u | while read t; do grep -qix "$t" /usr/share/dict/words || printf '%s ' "$t"; done; echo
Adversarial Amear Appended Artifacts Backtesting Blocks Checks Claims Cloudflare Conflicts Defects Dispatched Files Fills Findings Google Limits Lines Observations Parallels Parked Pre Quotes Redis Required Runs Scans Sensidine Sheets Sources Supersedes Timestamp Touches Volumes Workers 
$ sed -n 149p docs/reports/2026-11-12-o3-block1-scope-worker1.md | cmp -s - <(cut -c1-40 /tmp/s13.txt) && echo b149-equals-s13-first-40 || echo b149-differs
b149-equals-s13-first-40
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n -F "Deviation G's ingress question leaves the anchor's live path" | cut -d: -f1
112
217
$ grep -c -F '217' docs/reports/2026-11-12-o3-block1-scope-worker1.md
2
$ grep -n -F -e 'as briefed' -e 'brief prescribes' -e 'brief declared' docs/reports/2026-11-12-o3-block1-scope-worker1.md | cut -d: -f1
269
309
317
318
$ grep -n -F -e 'untouched' -e 'brief' docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
16
47
139
172
175
317
330
$ grep -n -F -e '7d8f6577' -e 'line 149' -e 'asserts each OLD' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md | cut -d: -f1
17
24
365
376
```

### Report rules and de-identification scans on A, B, C and the added lines
```
$ grep -n -F 'Adversarial Amear Appended' docs/reports/2026-11-12-o3-block1-scope-manager.md | cut -d: -f1
218
$ grep -F 'Adversarial Amear Appended' docs/reports/2026-11-12-o3-block1-scope-manager.md | tr ' ' '\n' | grep -c -x -F -e Claims -e Workers
1
$ (diff /tmp/o3c1/manager.orig.md docs/reports/2026-11-12-o3-block1-scope-manager.md; diff /tmp/o3c1/worker1.orig.md docs/reports/2026-11-12-o3-block1-scope-worker1.md) | grep '^>' | sed 's/^> \{0,1\}//' > /tmp/o3c1w/added.txt; cat docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md >> /tmp/o3c1w/added.txt; tail -n 2 MANIFEST.md >> /tmp/o3c1w/added.txt; wc -l < /tmp/o3c1w/added.txt
     504
$ grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/o3c1w/added.txt
0
$ grep -c -i -F -f /tmp/o3-rep-name.txt /tmp/o3c1w/added.txt
0
$ grep -c -i -F -f /tmp/o3-med-words.txt /tmp/o3c1w/added.txt
0
$ grep -c -i -F -f /tmp/o3-banned-words.txt /tmp/o3c1w/added.txt
0
$ grep -o -w Amear /tmp/o3c1w/added.txt | wc -l
       6
$ grep -o -E '\b[A-Z][A-Za-z]+\b' /tmp/o3c1w/added.txt | sort -u | grep -v -i -F -f /tmp/o3-rep-name.txt | grep -v -i -F -f /tmp/o3-med-words.txt | while read t; do grep -qix "$t" /usr/share/dict/words || printf '%s ' "$t"; done; echo
ADV ADVERSARIAL Adversarial Amear Appended Claims Conflicts DECISIONS Dispatched Files Items Lines PASSED PNG Pre SCANS Scans Sensidine TradingView Volumes WORKERS Workers 
$ for f in docs/reports/2026-11-12-o3-block1-scope-manager.md docs/reports/2026-11-12-o3-block1-scope-worker1.md docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md; do printf '%s s13=%s last-is-s13=%s result=%s section=%s banned=%s placeholders=%s listing=%s email=%s rep=%s med=%s\n' "$f" "$(grep -c -x -F -f /tmp/s13.txt $f)" "$(tail -n 1 $f | grep -c -x -F -f /tmp/s13.txt)" "$(grep -c -E '^Result: (PASS|FAIL|BLOCKED)$' $f)" "$(grep -c -x -F '## Verification evidence (command output)' $f)" "$(grep -c -i -F -f /tmp/o3-banned-words.txt $f)" "$(grep -c -F -f /tmp/o3-placeholders.txt $f)" "$(grep -c -F -f /tmp/o3-listing-cmds.txt $f)" "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f)" "$(grep -c -i -F -f /tmp/o3-rep-name.txt $f)" "$(grep -c -i -F -f /tmp/o3-med-words.txt $f)"; done
docs/reports/2026-11-12-o3-block1-scope-manager.md s13=1 last-is-s13=1 result=1 section=1 banned=0 placeholders=0 listing=0 email=0 rep=0 med=0
docs/reports/2026-11-12-o3-block1-scope-worker1.md s13=1 last-is-s13=1 result=1 section=1 banned=0 placeholders=0 listing=0 email=0 rep=0 med=0
docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md s13=0 last-is-s13=0 result=0 section=1 banned=0 placeholders=0 listing=0 email=0 rep=0 med=0
$ grep -c -F '@@' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
8
$ grep -n -E '^@@[A-Z]+@@$' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
11:@@WORKERS@@
370:@@SCANS@@
373:@@ADV@@
381:@@RESULT@@
$ grep -c -E '<[a-z_ -]+>|[.]{3}' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
0
$ grep -c -F 'cmp -s' docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md
1
```

### Own-report scans
Run on /tmp/o3c1w/draft.md, which is this report without this subsection, before this subsection was inserted and before the S13 line was appended; this subsection holds commands and counts only.
```
$ wc -l < /tmp/o3c1w/draft.md
     467
$ grep -c -x -F -f /tmp/s13.txt /tmp/o3c1w/draft.md
0
$ grep -c -E '^Result: (PASS|FAIL|BLOCKED)$' /tmp/o3c1w/draft.md
1
$ grep -c -x -F '## Verification evidence (command output)' /tmp/o3c1w/draft.md
1
$ grep -c -i -F -f /tmp/o3-banned-words.txt /tmp/o3c1w/draft.md
0
$ grep -c -F -f /tmp/o3-placeholders.txt /tmp/o3c1w/draft.md
0
$ grep -c -F -f /tmp/o3-listing-cmds.txt /tmp/o3c1w/draft.md
0
$ grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/o3c1w/draft.md
0
$ grep -c -i -F -f /tmp/o3-rep-name.txt /tmp/o3c1w/draft.md
0
$ grep -c -i -F -f /tmp/o3-med-words.txt /tmp/o3c1w/draft.md
0
$ grep -o -E '\b[A-Z][A-Za-z]+\b' /tmp/o3c1w/draft.md | sort -u | grep -v -i -F -f /tmp/o3-rep-name.txt | grep -v -i -F -f /tmp/o3-med-words.txt | while read t; do grep -qix "$t" /usr/share/dict/words || printf '%s ' "$t"; done; echo
ADV ADVERSARIAL Adversarial Amear Appended Artifacts Backtesting Blocks Checks Claims Cloudflare Conflicts DECISIONS Defects Dispatched Files Fills Findings Google Items Limits Lines Observations PASSED PNG Parallels Parked Pre Quotes Redis Required Runs SCANS Scans Sensidine Sheets Sources Supersedes Timestamp Touches TradingView Volumes WORKERS Workers 
```

## Findings

Criterion 1 (edit-log fidelity) holds: the script parsed 18 Items; every OLD text matches the pre-correction copy at the stated line (True for Items 1 to 5, 7 to 15, 17, 18); every NEW text occurs once in the current file and no OLD line is left (0 for each); the two inserts match the stated ranges (Item 6: 84 lines at 227 to 310; Item 16: 21 lines at 284 to 304). The diff hunks are 6 in A and 10 in B; hunk 233,234c317,318 maps to Items 4 and 5, hunk 297,298c318,319 to Items 14 and 15, every other hunk to one Item; no hunk without an Item, no Item without a hunk.

Criterion 3 holds: A :21 and :318 state the before-count cannot be reproduced and is not claimed; A's "Correction 1 evidence" pastes `grep -c` after-counts (0 and 1) and the full `tail -n 3 MANIFEST.md` output; B :309 no longer holds the words on the manager report's last line (C's paste: count 0 for that string) and reduces the claim to s13=0 from B's own scan block (B :259); B :35 and :52 are the OLD text plus one appended label citing :271–273 (Items 8 and 9, script True), and B :271 to :273 are the "Fix note (S13 filter)" heading and paragraph (B listing above).

Criterion 5 holds: on the 504 added lines, email 0, rep 0, med 0, banned 0; the capitalised tokens not in the system word list are markers (ADV, SCANS, WORKERS), product, path, heading and acronym words; the only person name is Amear (6 occurrences).

Defects:

1. C fails the S13 rule of criterion 4. C scan line: `s13=0 last-is-s13=0`. The S13 sentence is not in C at all; it is not one of the four excused markers. (If the manager means to append it after @@RESULT@@ is filled, nothing in C says so.)

2. B :275 and A :175: the labels make claims with no paste in the same report, and the re-run they point to does not exist. B :275 says "the S13 sentence is still the last line, now line 322; the re-run is in the correction 1 manager report". B has no command that shows 322 (its pasted output at :279 still shows 301), and C has no command that runs `grep -n -F -f /tmp/s13.txt` or `tail -n 1` on B (C's only reference is the @@SCANS@@ marker). The claim is true now (re-run: `322`, and `321:Result: FAIL`), but under S1 it is unbacked in both B and C. A :175 says the same thing ("the re-run is in the correction 1 manager report") about A's report scans, and C has no such re-run either.

3. B :317 (O-c) still says "(as the brief prescribes)", and B :269, :309 and :318 still say "as briefed" / "The brief declared only". None of these has a paste. Correction 1 replaced exactly this kind of claim in A (Item 4: "the form the brief gave", replaced as having "no paste"), but its sweep of B left these four lines alone. Line hits: `269 309 317 318`.

4. B :318 (O-d) says the topology phrase "is at topology :112 and also :217". Nothing in B shows the phrase at :217. B's only paste that mentions 217 is `1 217:D-2026-11-10-A` (an id grep, B :125). Correction 1 edited this line (Item 14) but added only a line-number label, no evidence. The claim is true (re-run: `112` and `217`), but it is unbacked in B.

5. A :139 still says "14 pre-existing uncommitted rows (parked work, untouched)". After correction 1, A :318 says "no other row was edited" is withdrawn and "No byte-identity of the 14 earlier rows is claimed". "untouched" is that same claim, with no paste: B :184 says the check "does not show they are byte-" identical. Correction 1's evidence header covers :139 only for the hunk sizes (8, 6, 3). Hit: `139` in the grep for 'untouched'.

6. C itself has claims with no paste. C :24 says worker1's pasted output line 149 holds the first 40 characters of the S13 sentence. That is true (re-run: `b149-equals-s13-first-40`), but C pastes no command for it. C :17 says the edits were made "by a script that asserts each OLD text is present exactly once on its line", with no paste and no process-record label (C :24 has such a label, C :17 does not). C :376 says the entry hash is "the one the original reports pasted (7d8f6577)", and C pastes nothing from A or B showing it (it is at A :73 and B :147). C :4 says "nothing committed", with no paste.

7. The S1 sweep missed claims in A's unedited lines that have no paste in A. A :14: worker1's "entry, parked block, line arithmetic and MANIFEST rows held". A :320: "Worker1 confirmed: all 5 quotes byte for byte". A :315: "the `**Decision:**` label is at HEAD :139", but A pastes no :139. A :47: "The entry cites :174 and :175". A :120: "The entry's "untested" is attributed to rubric O3". A :324: "B1-a". The only support for these is in B or in the entry text, and neither is pasted in A.

Observations (not defects):

- O-1. Re-run differences that labels cover: `tail -n 3 MANIFEST.md | cut` now lists the two correction 1 rows; the last MANIFEST hunk is now `@@ -442,3 +456,8 @@` (was +456,6); `wc -l < MANIFEST.md` is 463 (was 461). A's evidence header says the block ran before correction 1 appended its MANIFEST rows. B's pasted 301 is now 322, and the worker1 Result line went from 300 to 321; the labels at B :275 and A :175 cover both.
- O-2. One re-run difference no label covers: A :218, the capitalised-token list of A and B. A :175's label covers only "the last three commands", but this is the fourth from last, and its output has changed. The pasted line holds 1 of {Claims, Workers}; the re-run holds both ("Claims" comes from correction 1's "Claims covered").
- O-3. A's evidence for ":13 and :14 (the two agent ids occur in DISPATCH_LOG.md)" is one combined count, 4, which does not show that each id occurs. Separate re-run: 2 and 2. The claim holds.
- O-4. A's "Correction 1 evidence" pastes `grep -o -F 'DECISION_LOG 2026-11-12T17:31Z' | head -n 1` with empty output. It supports nothing, and the next commands carry the :233 claim.
- O-5. Every other sampled re-run matched its paste: 0, 1, 1, 5, 4, "WHEN: 17:31Z", 1, 1, 0, 288, 6, 10, 0, 7d8f6577, both orig sha256, tail -n 2 rows.

Defect count: 7.

Result: FAIL
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
