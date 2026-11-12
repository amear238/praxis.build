# fgd doc-alignment correction-1 — adversarial worker 1 (bead Praxis_build-fgd)

## Task
Unit `2026-11-12-fgd-doc-alignment-correction-1`, adversarial pass. Artifacts: the three corrected reports `docs/reports/2026-11-12-fgd-doc-alignment-{manager,worker1,worker2}.md`, their pristine copies in `/tmp/fgdc1/orig/`, and the correction manager report `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md` (its ADV_PLACEHOLDER and RESULT_PLACEHOLDER sections ignored). HEAD `006a08b`. My scratch dir is `/tmp/fgdc1w/`. The only file I edited is this report. Nothing staged; no git refs touched.

## Mode
ADVERSARIAL.

## Criterion
`specs/SPEC_RUBRIC.md` S1 (pasted output, not a description of it), S2 (no level above the evidence), S13 (footer as last line), public-repo de-identification, and the brief's evidence tests: literal commands, no `...` cuts, no "see output" without a paste, correct line numbers, no event claimed without pasted output.

## Process log
1. Diffed each pristine copy against its current file. Hunk headers match C9 of the correction manager report.
2. Re-checked all 8 cures with my own commands (K1–K9 below). All 8 are cured.
3. Sampled 13 claims that the audit did not cite (T1–T13): 4 in manager, 4 in worker1, 5 in worker2. Seven are line-number claims (T1, T3, T5, T6, T9, T12, T13) and four are quotations (T2, T4, T10, T11). All 13 hold. T3's grep for `:99` came back empty because the two 3gm lines cite ruleset line 99 in other notations, `sed -n '99,99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md` and "Spec L99". Manager E11 :347–348 shows this (pasted under X1).
4. Parsed every edit-log row: old text compared to the pristine line, new text compared to the current line. Every mismatch is accounted for: rows 6 and 31 by M1/M2, row 32 by the mask, and the insert rows. The pasted logs equal `/tmp/fgdc1/edits-*.md`.
5. Re-ran `/tmp/fgdc1/ev-corr1.sh` and diffed the result against the pasted block. Then ran `deid.sh`, including on this report.

## Verification evidence

### K — the cures (`bash /tmp/fgdc1w/cures.sh`)
````
## K1 cure 1: manager pass-line pointer
$ grep -n '^Verdict' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md; wc -l < /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md:562:Verdict: PASS
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:562:Verdict: PASS
     564
(exit 0)
$ grep -n -o -E 'at its line [0-9]+' docs/reports/2026-11-12-fgd-doc-alignment-manager.md; grep -c -F 'line 573' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
782:at its line 562
792:at its line 314
0
(exit 1)
## K2 cure 2: elision-line pointer
$ awk '/^```/{f=!f} index($0,"..."){print NR" fence="f}' /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-worker1.md
314 fence=0
553 fence=0
555 fence=0
(exit 0)
$ grep -n -o -E 'its lines [0-9]+ and [0-9]+[^,]*' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
792:its lines 553 and 555 in the pre-correction copy
(exit 0)
## K3 cure 3: iconv INVALID claim
$ grep -c -F 'INVALID-utf8' docs/reports/2026-11-12-fgd-doc-alignment-manager.md; sed -n 25p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -o -E 'The .iconv. detection output was not kept[^;]*; no INVALID result is pasted here\.'
0
The `iconv` detection output was not kept, and it is not reproducible after the repair; no INVALID result is pasted here.
(exit 0)
$ awk 'NR>=350 && NR<=372 && /3a 80 93 39 34/{print NR}' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
370
371
(exit 0)
## K4 cure 4: every-cited-line claim
$ grep -c -F 'all cited numbers were correct' docs/reports/2026-11-12-fgd-doc-alignment-manager.md; sed -n 22p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -o 'that pasted set is what is shown, not every line read'
0
that pasted set is what is shown, not every line read
(exit 0)
## K5 cure 5: .cs 188-191 (HEAD, and working tree diff)
$ git diff --quiet HEAD -- ninjascript/PraxisNoiseAreaBreakout.cs && echo NO-DIFF; git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | sed -n 188,191p | grep -n -o -E '16:00[^(]*|trader-locked'
NO-DIFF
1:16:00 ET cash-close flat 
1:trader-locked
4:16:00 session flat");
(exit 0)
$ grep -n -c -F 'git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | sed -n 188,191p' docs/reports/2026-11-12-fgd-doc-alignment-manager.md
1
(exit 0)
## K6 cure 6: worker1 UnicodeDecodeError
$ grep -n -o -E 'UnicodeDecodeError[^.]{0,40}' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | cut -c1-80
361:UnicodeDecodeError as e:
382:UnicodeDecodeError as e: print(f,"INVALID utf-8 at",e
580:UnicodeDecodeError as e:
(exit 0)
## K7 cure 7: worker1 C3a od segment
$ grep -n -F '| od -c | sed -n 1,12p' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | cut -d: -f1 | tr '\n' ' '; echo; awk 'NR>=586 && NR<=600 && /^0000[0-7]+ /{c++} END{print "od rows after the re-run command:", c}' docs/reports/2026-11-12-fgd-doc-alignment-worker1.md
367 586 
od rows after the re-run command: 12
(exit 0)
## K8 cure 8: de-identification of manager :96
$ for f in /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-manager.md; do echo "$f rep-name=$(grep -c -i -f /tmp/fgdc1/rep.txt $f)"; done
/tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md rep-name=1
docs/reports/2026-11-12-fgd-doc-alignment-manager.md rep-name=0
(exit 0)
$ sed -n 96p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -c -F 'mffu-[rep-name]-reply.png'; sed -n 97p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -o '^\[correction-1, 2026-11-12: the support rep.s first name in this filename is masked as \[rep-name\]; the actual output carried the name\]$' | wc -l
1
       1
(exit 0)
## K9 S13 occurrences and fence state
$ for f in docs/reports/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md; do awk -v F=$f '/^```/{f=!f} $0=="Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."{print F":"NR" fence="f}' $f; done
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:409 fence=1
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:410 fence=1
docs/reports/2026-11-12-fgd-doc-alignment-manager.md:818 fence=0
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:211 fence=1
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md:748 fence=0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:328 fence=0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md:472 fence=1
(exit 0)
$ for f in docs/reports/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-worker1.md docs/reports/2026-11-12-fgd-doc-alignment-worker2.md; do echo "$f lines=$(wc -l < $f)"; done
docs/reports/2026-11-12-fgd-doc-alignment-manager.md lines=     818
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md lines=     748
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md lines=     472
(exit 0)
````

### T — sampled untouched claims (`bash /tmp/fgdc1w/sample.sh`)
````
## T1 manager :58 DECISIONS.md:2058 cites topology :48
$ git show HEAD:DECISIONS.md | sed -n 2058p | grep -o -E '.{0,60}:48.{0,40}'
d from CLAUDE.md itself, more fully than the topology doc's :48). For the anchor strategy the emitter i
s NT8, not TradingView (topology doc :48; the anchor strategy is not TradingView
(exit 0)
## T2 manager :59 DECISIONS.md:2155 and worker7:71 cite topology :41 path ending in Rithmic
$ git show HEAD:DECISIONS.md | sed -n 2155p | grep -o -E '.{0,50}:41.{0,50}'
ECISIONS.md:2054: "The path in full is the one at :41."; the topology path ends "→ Rithmic → account.",
 `docs/specs/2026-11-10-live-signal-topology.md`:41). D-2026-11-10-B is not edited. The route is reco
(exit 0)
$ git show HEAD:docs/reports/2026-11-11-v-rulings-filing-worker7.md | sed -n 71p | grep -o -E '.{0,40}:41.{0,60}'
d:2054: "The path in full is the one at :41."; the topology path ends "→ Rithmic → account.", `docs/spe
cs/2026-11-10-live-signal-topology.md`:41). D-2026-11-10-B is not edited. The route is recorded as co
(exit 0)
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 41p | grep -o -F '→ Rithmic → account'
→ Rithmic → account
(exit 0)
## T3 manager :71 3gm reports cite ruleset :99
$ git show HEAD:docs/reports/2026-10-30-3gm-fidelity-check.md | sed -n 644p | grep -o -E '.{0,40}:99.{0,40}'
(exit 1)
$ git show HEAD:docs/reports/2026-10-30-3gm-worker1-checklist.md | sed -n 757p | grep -o -E '.{0,40}:99.{0,40}'
(exit 1)
## T4 manager :60 mffu-connection-investigation :50 :88 cite topology :41
$ git show HEAD:docs/reports/2026-11-11-mffu-connection-investigation.md | sed -n '50p;88p' | grep -o -E '.{0,40}:41.{0,30}'
specs/2026-11-10-live-signal-topology.md:41` — "SubmitBracket → Rithmic →
specs/2026-11-10-live-signal-topology.md:41` — Breaker placement downstre
(exit 0)
## T5 worker1 :186 rubric headings :46 :81 :99 (HEAD)
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -E '^#{2,3} ' | awk -F: '$1>=40 && $1<=100' | cut -c1-70
46:## PASSED — closed criteria
50:### O1 — Walk-forward gate set for the replication arm
65:### F1 — Signal-path topology vs. circuit-breaker placement
81:### F2 — Session-flat time vs. breakers #4 and #5
99:## OPEN — gradeable now
(exit 0)
## T6 worker1 :539 S13 footer once in topology and proposal at body :114 and :81
$ grep -n -x -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-11-10-f2-session-flat-proposal.md
docs/specs/2026-11-10-live-signal-topology.md:114:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
docs/specs/2026-11-10-f2-session-flat-proposal.md:81:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
(exit 0)
## T7 worker1 :419 line 95 reads :93–94; MANIFEST row for proposal says 93–94
$ sed -n 95p docs/specs/2026-11-10-f2-session-flat-proposal.md | grep -o -F ':93–94'
:93–94
(exit 0)
$ grep -n -F 'f2-session-flat-proposal.md' MANIFEST.md | grep -o -E '^[0-9]+:|93.94' | tr '\n' ' '; echo
354: 448: 93–94 
(exit 0)
## T8 worker1 :450 'Consecutive loss' lone body hit; amended names 3 and 3 whole-file
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -c -F 'Consecutive loss'
1
(exit 0)
$ grep -c -F 'Session flat gate' docs/specs/2026-11-10-live-signal-topology.md; grep -c -F 'Session window (operator lockout)' docs/specs/2026-11-10-live-signal-topology.md
3
3
(exit 0)
## T9 worker2 :248 proposal :75–78 are OPEN-F2-1 to OPEN-F2-4
$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | sed -n 75,78p | grep -o -E 'OPEN-F2-[0-9]'
OPEN-F2-1
OPEN-F2-2
OPEN-F2-3
OPEN-F2-4
(exit 0)
## T10 worker2 :266 DECISIONS.md:2232 'Copied by script from proposal :36 and :38'; proposal :36 :38 are #4/#5 text
$ sed -n 2232p DECISIONS.md | grep -o 'Copied by script from proposal :36 and :38'
Copied by script from proposal :36 and :38
(exit 0)
$ git show HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md | sed -n '36p;38p' | cut -c1-40
> 4. Session flat gate — clock reaches 1
> 5. Session window (operator lockout) —
(exit 0)
## T11 worker2 :139 topology :54 quote 'Names are exactly as the Phase 3 import lists them'
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 54p | grep -o -F 'Names are exactly as the Phase 3 import lists them'
Names are exactly as the Phase 3 import lists them
(exit 0)
## T12 worker2 :89 topology note is :115–200
$ wc -l < docs/specs/2026-11-10-live-signal-topology.md; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | wc -l; sed -n 115,116p docs/specs/2026-11-10-live-signal-topology.md | cut -c1-60
     200
     114

## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)
(exit 0)
## T13 worker2 :232 rubric HEAD :81 heading text
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 81p
### F2 — Session-flat time vs. breakers #4 and #5
(exit 0)
````

### X1 — T3 supplement, worker2 index-count command, residuals heading
````
$ sed -n 13p docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | grep -o 'git diff --cached --name-only | grep -c [^;]*'; sed -n 408p docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | grep -o 'grep -c .*'
(exit 1)
$ grep -n -i -E '^#+ .*residual' docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | wc -l
       0
(exit 0)
$ sed -n 347,348p docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -c1-110
HEAD:docs/reports/2026-10-30-3gm-fidelity-check.md:644:$ sed -n '99,99p' docs/specs/2026-07-16-b2-noise-area-r
HEAD:docs/reports/2026-10-30-3gm-worker1-checklist.md:757:**Rule:** the paper "acts on the **stamp**". Spec L9
(exit 0)
$ grep -n -o -E 'grep -c [^;]{0,80}' docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | awk -F: '$1>=406 && $1<=416'
413:grep -c '^docs/reports/evidence/.*\.png$'
(exit 0)
````

### R — edit logs, evidence block vs fresh run, S1 checks on the correction manager report (`bash /tmp/fgdc1w/rows-summary.sh`, one mis-echoed block dropped and re-run literally in R2)
````
$ python3 -I /tmp/fgdc1w/rows.py | grep -v -E "old==orig:True new:[0-9]+ new==cur:True$"
manager rows 44
  row 6 orig:25 old==orig:True new:25 new==cur:False
  row 31 orig:87 old==orig:True new:87 new==cur:False
  row 32 non-numeric orig/new: 96 | 96–97
  row 33 non-numeric orig/new: after 433 (between orig 433 blank and 43 | 435–777
worker1 rows 18
  row 18 non-numeric orig/new: (between 563 and 564) | 564-747
worker2 rows 10
  row 10 non-numeric orig/new: (insert after orig 399, before orig 400  | 400–470
(exit 0)
$ python3 -I /tmp/fgdc1w/m.py | head -n 5
M1: cur25 == row6new with sentence inserted after "no INVALID result is pasted here.": True
M2: cur87 startswith row31new: True | appended tail starts:  E14 was run before correction-1 appended its two 
manager edits file lines 59 pasted segment equal (demoted headings ignored): True
worker1 edits file lines 28 pasted segment equal (demoted headings ignored): True
worker2 edits file lines 49 pasted segment equal (demoted headings ignored): True
(exit 0)
$ diff <(sed -n 195,432p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md) /tmp/fgdc1/ev-corr1.out && echo SAME-AS-SAVED
SAME-AS-SAVED
(exit 0)
$ bash /tmp/fgdc1/ev-corr1.sh > /tmp/fgdc1w/ev-corr1.fresh 2>&1; diff <(sed -n 195,432p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md) /tmp/fgdc1w/ev-corr1.fresh
35c35
< docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | absent
---
> docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
182c182,183
< (exit 1)
---
> docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md count=1 last=Fills are optimistic; Standard
> (exit 0)
196a198
> docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md
(exit 1)
$ diff /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md docs/reports/2026-11-12-fgd-doc-alignment-manager.md | grep -E "^[0-9]" | sed -n "/^434/,/^449/p" | tr "\n" " "; echo
434c435,436 436c438,440 438c442,445 440,446c447,449 448c451,587 449a589,793 
(exit 0)
$ grep -n -E "^\\$ .*(<…>|<[a-z]+>|\.\.\.)" docs/reports/2026-11-12-fgd-doc-alignment-manager.md | cut -c1-60
419:$ grep -c -F '<…>' docs/reports/2026-11-12-fgd-doc-align
451:$ awk '/^```/{f=!f} index($0,"..."){print NR": "(f?"in-f
(exit 0)
$ sed -n 13p docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | grep -o "a pre-existing PNG[^,]*"; grep -n -o -E "pre-existing PNG|the PNG listed in E1" docs/reports/2026-11-12-fgd-doc-alignment-manager.md
a pre-existing PNG under `docs/reports/evidence/`
810:the PNG listed in E1
(exit 0)
$ sed -n 18p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | grep -o "stopped at its 40-turn limit with no return text"; sed -n 5p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | grep -o "one worker-memory write.*"; sed -n 437p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md
stopped at its 40-turn limit with no return text
one worker-memory write under `.claude/agent-memory/` (gitignored) is disclosed under Adversarial findings and residuals.
ADV_PLACEHOLDER
(exit 0)
````

### R2
````
$ grep -n -o -E "rep-name=[0-9]+" docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | grep -v ":rep-name=0$"; sed -n 177,180p docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | cut -c1-80
180:rep-name=1
## deid.sh (counts only)

```text
docs/reports/2026-11-12-fgd-doc-alignment-manager.md | rep-name=1 email=0 trader
(exit 0)
$ find .claude/agent-memory -type f -newer /tmp/fgdc1/orig/2026-11-12-fgd-doc-alignment-manager.md | sort
.claude/agent-memory/praxis-worker/MEMORY.md
.claude/agent-memory/praxis-worker/project_zsh-grep-is-ugrep.md
(exit 0)
````

### X2: K9 fence states for worker2 (awk's toggle is thrown off by nested 4-backtick fences)
````
$ grep -n -E '^```' docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | awk -F: '($1>=290 && $1<=340) || $1>=400' | tr '\n' ' '; echo
292:``` 298:```bash 300:``` 304:```text 329:``` 337:```bash 339:``` 405:```text 470:``` 
(exit 0)
````

Reading X2: worker2 :328 sits inside the ```text fence at :304–:329, and :472 is the last line, after the fence closes at :470. So K9's fence=0 at :328 and fence=1 at :472 come from the toggle, not from the file. Every extra S13 occurrence is inside a fence, and every report ends with the footer. That supports correction-1 manager :11.

## Findings

All 8 cures hold (K1–K9). The 13 sampled claims hold (T1–T13, X1). The edit logs cover every diff hunk, and each log row's old and new text equals the pristine and current line, except where M1/M2, the mask or an insert row accounts for it (R). The pasted ev-corr1 block equals its saved output `/tmp/fgdc1/ev-corr1.out` (R). Seven MINOR breaks remain, all S1 evidence-test failures. Six are in the correction manager report and one in a cure it applied to worker2.

1. MINOR. File and lines: `-correction-1-manager.md`:192, with the blocks at :229, :375–376 and :393. Failing test: the evidence block must equal a fresh run, apart from differences the report states. A fresh `ev-corr1.sh` differs in three places: C3's adv-1 line ("absent" becomes counted), C10 (one more line, and exit 1 becomes 0) and C12 (one more file) (R, block 4). :192 explains only C4 and C8, and C10's pasted `(exit 1)` has no explanation. Cure: append to :192 "C3's last line, C10's list and exit code, and C12's list change once adv-1's report exists; C10 exits 1 here because `[ -f ]` fails on the absent adv-1 report", or re-run after adv-1 returns and re-paste.
2. MINOR. File and line: `-correction-1-manager.md`:100. Failing test: no output may be cut with an ellipsis. "(434c435,436 … 449a589,793)" elides diff output, and the plain-diff hunk list is not pasted anywhere in the report (R, block 5 gives it in full). Cure: replace the parenthesis with `434c435,436 436c438,440 438c442,445 440,446c447,449 448c451,587 449a589,793`, and add the command that prints it to `ev-corr1.sh`, with its output pasted.
3. MINOR. File and line: `-correction-1-manager.md`:18. Failing test: no event may be claimed without pasted output, and an event that cannot be reproduced must be stated as such. "stopped at its 40-turn limit with no return text" has no paste and no such statement (R, last block). Cure: append "(the manager's observation of the dispatch; no output kept; not reproducible)".
4. MINOR. File and lines: `-correction-1-manager.md`:379–383 (C11). Failing test: no claim may rest on unexplained output. C11 pastes `manager.md:2` with no reading, and nothing in the report says why 2 hits are not placeholders. The hits are manager :419 and :451, which are search patterns inside shown commands (R, block 6). Cure: add one line under the evidence block naming :419 and :451 as literal search patterns, not placeholders, and paste the `grep -n` output.
5. MINOR. File and lines: `-correction-1-manager.md`:177–188 (the verbatim build-worker2 log). Failing tests: S2, and stale evidence that is not labelled. Line :180 pastes `manager.md | rep-name=1` and :184 shows adv-1 "absent". Both were run before the mask, and nothing next to them says so (R2). A reader can take them as current, while C3 shows 0. Cure: add one line after the log, outside the verbatim text: "build-worker2 ran this deid table before the manager-file mask; current counts are in C3 (rep-name=0)."
6. MINOR. File and line: `-worker2.md`:13, introduced by the correction (worker2 log row 2, and `-correction-1-manager.md`:145). Failing test: no claim without pasted output. "a pre-existing PNG under `docs/reports/evidence/`" goes beyond the paste, because E-1 shows only the counts 1, 0 and 1 (X1: `grep -c '^docs/reports/evidence/.*\.png$'`). The same correction removed the identical wording "pre-existing PNG" from manager :810 under test e (row 44; R shows :810 now reads "the PNG listed in E1"). Cure: replace it with "one PNG under `docs/reports/evidence/` (E-1 counts)", and update log row 2 and its reason cell to match.
7. MINOR. File and line: `-correction-1-manager.md`:5. Failing test: no pointer to a section that lacks the paste. The line says "one worker-memory write … is disclosed under Adversarial findings and residuals". No heading containing "residual" exists (X1: 0), and Adversarial findings is ADV_PLACEHOLDER (R, last block). C12 and R2 show two files written (MEMORY.md and `project_zsh-grep-is-ugrep.md`). Cure: change it to "a worker-memory write of two files under `.claude/agent-memory/` (gitignored; C12, C13a)". If the disclosure is meant to sit in Adversarial findings, write it there when that placeholder is filled.

Not a break: manager :97, the mask disclosure line, sits inside the E1 output fence (fence opens at :89). It is labelled `[correction-1, …]`, so it does not pass as output.

Self-check of this report: every shown command is literal and every output is pasted in full. Where a command cuts its own output (`cut`, `head`), the cut is in the shown command. Two shown commands match the placeholder regex: K2's awk and R block 6's grep. Both are literal search patterns, not placeholders. Line numbers cited in Findings come from the pasted blocks K, T, X and R. The rep's name is not printed anywhere: the scan below counts it, and the two places where a filename could carry it were masked by `sed` before display or shown as counts only.

## De-identification scan (`bash /tmp/fgdc1/deid.sh`, run after this report was written; counts only)
````
$ bash /tmp/fgdc1/deid.sh
docs/reports/2026-11-12-fgd-doc-alignment-manager.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/reports/2026-11-12-fgd-doc-alignment-correction-1-worker1.md | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-11-10-live-signal-topology.md (added lines: 86) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-07-16-b2-noise-area-ruleset.md (added lines: 59) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
docs/specs/2026-11-10-f2-session-flat-proposal.md (added lines: 30) | rep-name=0 email=0 trader-surname=0 paper-surnames=0 med-brands=0
````

All counts are 0. The scan ran on this report after Findings were written. The text appended after it (this note, Files staged, Result, the verdict and the footer) adds no name, email or brand term. A scan run after that point is not pasted here, because pasting it would change the file it scans.

## Files staged
None. In the repo I edited only this report. Outside it, I made one gitignored worker-memory write after the scans: a new memory file under `.claude/agent-memory/praxis-worker/` plus one appended line in its `MEMORY.md`. This write is not covered by the pasted evidence, so it is self-reported. A fresh `ev-corr1.sh` C12 will now list the new file too. Scratch files are in `/tmp/fgdc1w/`. Running `ev-corr1.sh` rewrote `/tmp/fgdc1/re-*.out` and `/tmp/fgdc1/added.txt`, its own scratch outputs.

## Result
FAIL. 8 of 8 audit cures hold, and 13 of 13 sampled claims hold. 7 MINOR findings remain (S1 evidence tests); 0 are MAJOR.

Verdict: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
