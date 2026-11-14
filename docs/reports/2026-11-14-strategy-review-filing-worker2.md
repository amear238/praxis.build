# Unit 2026-11-14-strategy-review-filing, worker 2 (BUILD): MANIFEST rows 9-15

## Task

Mode: BUILD. Draft one MANIFEST.md row for each of 7 untracked reports (items 9-15 of the unit's list), by reading each file in full, in the style of the 7 rows commit 9ff8a48 added. Authority: DECISION_LOG 2026-11-14T01:27:05Z (praxis-master under D-2026-11-08-D D1). Only writes: /tmp/praxis-sr/rows-w2.txt and this report. No tracked file edited, none of the 7 files edited, git index not touched, nothing staged.

Name handling: the support rep's first name was derived into `N` from the F4 reply-filing file name and never typed; every read of the 7 files went through `sed "s/$N/[rep]/gI"`.

## Files read (wc -l output)

All 7 read in full (files 12, 13 and 15 in chunks; long lines of the prose sections re-read uncut).

```
$ wc -l <the 7 files>
      97 docs/reports/2026-11-13-voice-handoff-strategy-review.md
     113 docs/reports/2026-11-13-hermes-handoff-strategy-search.md
      29 docs/reports/2026-11-13-research-filing-manager.md
     599 docs/reports/2026-11-13-research-filing-resume-worker1.md
     755 docs/reports/2026-11-13-research-filing-resume-worker2.md
     257 docs/reports/2026-11-13-research-filing-cure-manager.md
     422 docs/reports/2026-11-13-research-filing-cure-worker1.md
    2272 total
```

S13 lines, last line, name count and tracked status per file (S = the sentence cut from specs/SPEC_RUBRIC.md :145; x-lines = whole-line matches; substr = substring matches; tracked = `git ls-files` count):

```
S13 len=90
voice-handoff-strategy-review x-lines=97  last-line-is-S13=y substr=1 name=0 tracked=0
hermes-handoff-strategy-search x-lines=113  last-line-is-S13=y substr=1 name=0 tracked=0
research-filing-manager x-lines=29  last-line-is-S13=y substr=1 name=0 tracked=0
research-filing-resume-worker1 x-lines=599  last-line-is-S13=y substr=1 name=0 tracked=0
research-filing-resume-worker2 x-lines=755  last-line-is-S13=y substr=1 name=0 tracked=0
research-filing-cure-manager x-lines=257  last-line-is-S13=y substr=1 name=0 tracked=0
research-filing-cure-worker1 x-lines=422  last-line-is-S13=y substr=3 name=0 tracked=0
109 168 422 
```

(The last output line is the substring-match line numbers in cure-worker1: :109 and :168 are the `S="..."` assignments inside fenced commands; :422 is the standalone last line.)

DECISION_LOG stamps used in the rows, one row each:

```
2026-11-13T21:03:55Z rows=1
2026-11-14T01:23:10Z rows=1
2026-11-14T01:27:05Z rows=1
2026-11-13T19:40:54Z rows=1
2026-11-13T19:58:43Z rows=1
2026-11-13T20:21:12Z rows=1
2026-11-13T20:25:43Z rows=1
2026-11-13T20:34:10Z rows=1
```

Facts checked against the files where the manager's paraphrase differed or needed confirming:

- File 9: line 3 reads "Written by praxis-master for the voice-chat agent."
- File 10: line 3 reads "Written 2026-11-14T01:20Z (2026-11-13 20:20 ET) by the Claude.ai channel for the Hermes agent." The file does not say that Amear pasted it. That comes from the intake row 2026-11-14T01:23:10Z ("Intake: Hermes handoff, pasted into this session by Amear"), and the row cites that stamp. The file's step 2(b) lists five items "Amear's rulings from this evening" for Hermes to append to DECISIONS.md. The row reports these as the channel's list and does not treat them as filed decisions (S8).
- File 11: not every section is "(in progress)". Task and Rubric criteria are written out, Files staged reads "None. Nothing staged by this unit; the master builds the commit.", and the Result line reads "Result: BLOCKED (report in progress)". The file names no author. The row says this.
- File 12: title "Resume worker 1 report (adversary): unit 2026-11-13-research-filing-resume, round 1". Mode ADVERSARIAL. Grades: (a) PASS, (b) PASS, (c) PASS, (d) "FAIL (row 5 only)", (e) PASS, (f) FAIL, (g) PASS, and "Result: FAIL" at :597. The file never calls itself praxis-worker. At :68 it says "INFERRED: this is my own spawn" of the praxis-worker hook row at 20:02:04Z.
- File 13: title "Resume worker 2 report: unit 2026-11-13-research-filing-resume, adversary round 2". The Task says "round 2 (last round)". Mode ADVERSARIAL. Grades: (a)-(e) and (g) PASS, (f) FAIL, and "Result: FAIL" at :753. At (f) it infers that its own spawn is the praxis-worker row at 20:11:40Z.
- File 14: line 3 "Author: praxis-manager". :19 gives worker 1 as "8 checks (a)-(h) PASS ... one round". :253 "Result: PASS". :36 says the cure manager and adversary reports "get no MANIFEST row". The row reports this line as the file's own statement.
- File 15: title "Unit 2026-11-13-research-filing-cure, worker 1 (ADVERSARIAL)". Checks (a)-(h) are each PASS, "Defects" reads "none", and "Result: PASS" is at :420. It names no agent type.
- The DECISION_LOG context for files 12-15 (round counts, which grades went PASS or FAIL in which round) was not re-read in full. Only the stamps were counted. Each row describes its file's contents.

Row format reference: the 7 rows that 9ff8a48 added (names masked; shown only as field counts):

```
$ git show 9ff8a48 -- MANIFEST.md | grep '^+|' | sed 's/^+//' | awk -F'|' '{print NR": NF="NF}'
1: NF=7
2: NF=7
3: NF=7
4: NF=7
5: NF=7
6: NF=7
7: NF=7
$ ... | grep -c -E '; ungraded at time of row \|$'
7
$ git rev-parse --short HEAD
9ff8a48
```

## Rows drafted

```
$ cat /tmp/praxis-sr/rows-w2.txt
| /docs/reports/2026-11-13-voice-handoff-strategy-review.md | Report | 3 | 2026-11-13 | Voice handoff written by praxis-master for the voice-chat agent, for a strategy review with Amear: Amear's request quoted from the session, rules for running the conversation (plain English, every figure labelled by source, the voice agent makes no decisions and leaves four kinds of action to Amear's explicit word, notes go in one new file with his words verbatim), a reading list, and five sections citing the strategy-review index manager report by line: the four 2026-11-01 hand-run backtests at 1 NQ with the D6 drawdown check and D7, the research runs, whether indicator strategies were considered, the VM code agent's 2026-11-12 and 2026-11-13 work as reported second-hand by the channel (with three mismatches it says to mention, not resolve), and where things stand; it ends with what to write down if Amear wants to look at indicators; S13 sentence once, last line (:97); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-hermes-handoff-strategy-search.md | Report | 3 | 2026-11-13 | Handoff written 2026-11-14T01:20Z by the Claude.ai channel for the Hermes agent (pasted into the praxis-master session by Amear, intake row DECISION_LOG 2026-11-14T01:23:10Z): Amear's typed instruction of 2026-11-14T01:16Z quoted verbatim and three of his voice remarks as transcribed by the channel, then four ordered steps for Hermes: stop the open Praxis Master sessions; file the day's work through the auditor in one fresh Claude Code session (the strategy-review unit, five items the channel lists as Amear's rulings of that evening to append to DECISIONS.md, and the rest of the dirty tree sorted into units); pause builds until three strategy contenders exist; run a strategy search loop in Claude Code on the Mac with backtests through the VM bridge; plus a contender bar and an overfitting guard, both marked PROPOSED by the channel, the hard limits, and open items to carry; S13 sentence once, last line (:113); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-manager.md | Report | 3 | 2026-11-13 | Stub manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z); the file names no author: Task (file four Claude.ai channel reports, the allowed edits, five MANIFEST rows and a blob) and rubric criteria S1, S2, S8, S13 are written; Workers dispatched, Process log, Verification evidence, Adversarial findings and S6 cross-block check each read "(in progress)"; Files staged: none; Result: BLOCKED (report in progress); per DECISION_LOG 2026-11-13T19:58:43Z it was left by a power outage and stays unchanged; S13 sentence once, last line (:29); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-resume-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL report of resume worker 1, adversary round 1, for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z, read with 19:40:54Z); the file infers from a DISPATCH_LOG hook row that it is the praxis-worker spawn of 2026-11-13T20:02:04Z: checks (a)-(g) on HEAD 661e073 at 2026-11-13T20:07Z, with one consolidated script's output: (a) rebuild hashes and Downloads diffs PASS, (b) S13 once per filed return-handoff file PASS, (c) PII scan PASS, (d) the seven unit MANIFEST rows FAIL on row 5 only (it names content the resume manager report still showed as pending), (e) blob PASS, (f) only MANIFEST.md changed FAIL (two hook-recorded DISPATCH_LOG rows appended after the baseline), (g) stub manager report unchanged PASS; Result: FAIL; S13 sentence once, last line (:599); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-resume-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL report of resume worker 2, adversary round 2 (last round), for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z, read with 19:40:54Z); the file infers that it is the praxis-worker spawn of 2026-11-13T20:11:40Z: checks (a)-(g) with its own commands, (a)-(e) and (g) PASS, (f) only MANIFEST.md changed FAIL (five hook-recorded DISPATCH_LOG rows after the baseline at 2026-11-13T20:14:33Z), plus a check of the resume manager report against its own rules; three defects named (a quoted VM folder path at manager report :321 that is not byte-exact, the (f) DISPATCH_LOG change, a wrong reason given for one PII false positive) and five observations; evidence sections E1-E9; Result: FAIL; S13 sentence once, last line (:755); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-cure-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-cure (DECISION_LOG 2026-11-13T20:25:43Z), curing audit FAIL 1 check 3 (de-identification) of unit 2026-11-13-research-filing: a private name token replaced by [rep] in 4 lines of two evidence reports (resume-manager :67, :83; worker2 :584, :594), one filer's note per report, MANIFEST rows :481 and :483 amended and the blob made again, with pre-copy sha256, edit diffs, zero-count and S13 proofs, a negative control, the one-round cold adversary's checks (a)-(h) reported all PASS, and three out-of-scope name occurrences escalated to the master, not acted on; its :36 says the cure reports get no MANIFEST row under that unit's brief; Result: PASS, which the report limits to the brief's edits and proofs; S13 sentence once, last line (:257); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-cure-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-research-filing-cure (DECISION_LOG 2026-11-13T20:25:43Z); the file names no agent type: checks (a) redaction, (b) filer's notes, (c) S13, (d) MANIFEST, (e) blob, (f) zero name hits with a negative control and a sweep of the day's reports, (g) unchanged files, (h) index untouched, each PASS with commands and output, the name held only in a shell variable and never printed; defects: none; three observations outside its scope (one untracked report, two HEAD MANIFEST rows and the one staged path's file name carry the name token); name self-count 0; Result: PASS; S13 sentence once standalone, last line (:422), and also inside two shell-variable assignments in pasted commands in code fences (:109, :168); filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z; ungraded at time of row |
```

## Checks

```
$ wc -l /tmp/praxis-sr/rows-w2.txt
       7 /tmp/praxis-sr/rows-w2.txt
$ awk -F'|' '{print NR": NF="NF}' /tmp/praxis-sr/rows-w2.txt
1: NF=7
2: NF=7
3: NF=7
4: NF=7
5: NF=7
6: NF=7
7: NF=7
$ awk -F' \| ' '{print NR": col2="$2" col3="$3" col4="$4}' /tmp/praxis-sr/rows-w2.txt
1: col2=Report col3=3 col4=2026-11-13
2: col2=Report col3=3 col4=2026-11-13
3: col2=Report col3=3 col4=2026-11-13
4: col2=Report col3=3 col4=2026-11-13
5: col2=Report col3=3 col4=2026-11-13
6: col2=Report col3=3 col4=2026-11-13
7: col2=Report col3=3 col4=2026-11-13
$ grep -c -E '; ungraded at time of row \|$' /tmp/praxis-sr/rows-w2.txt
7
$ grep -c -F 'filed as written; no line changed; filed by unit 2026-11-14-strategy-review-filing, DECISION_LOG 2026-11-14T01:27:05Z' /tmp/praxis-sr/rows-w2.txt
7
$ grep -o -i -E 'built|tested|verified|working|viable|retired|decided' /tmp/praxis-sr/rows-w2.txt; echo "level-word exit=$?"
level-word exit=1
$ cut -d'|' -f2 /tmp/praxis-sr/rows-w2.txt
 /docs/reports/2026-11-13-voice-handoff-strategy-review.md 
 /docs/reports/2026-11-13-hermes-handoff-strategy-search.md 
 /docs/reports/2026-11-13-research-filing-manager.md 
 /docs/reports/2026-11-13-research-filing-resume-worker1.md 
 /docs/reports/2026-11-13-research-filing-resume-worker2.md 
 /docs/reports/2026-11-13-research-filing-cure-manager.md 
 /docs/reports/2026-11-13-research-filing-cure-worker1.md 
```

Name counts (N derived from the F4 reply-filing file name, never printed):

```
$ grep -ci "$N" /tmp/praxis-sr/rows-w2.txt
0
$ grep -ci "$N" docs/reports/2026-11-14-strategy-review-filing-worker2.md
0
```

(The report count was taken before this section was added and re-run after the last line was written. See the final check in the return message.)

## Files staged

None. Written: /tmp/praxis-sr/rows-w2.txt and this report (untracked, not staged).

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
