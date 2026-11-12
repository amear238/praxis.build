# 2026-11-12 — r6-engine-entry correction 1 — worker 1 (ADVERSARIAL) report

## Task

Instruction (manager brief, not a fact claim): in ADVERSARIAL mode, test `docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md` (the "correction report") against rubric row S1 and the brief rules. (1) Re-run every `$ ` command in its C0-C4 blocks under bash with the same eval runner and compare byte for byte. (2) Flag prose claims that lack pasted output. (3) Run the banned-string, email and S13 checks. Edit nothing except this report. No index or HEAD changes.

Criterion: S1, "Every claim in a report has pasted command output, not a description of output." (row quoted from the correction report's C0, which my re-run reproduces in E2).

Method (plan, carried out as shown in E1-E2): `extract.sh` cuts each C block body out of the correction report into `b0`-`b4` and the `$ ` command lines into `c0`-`c4`. C3 line 178 is left out because it is output that only starts with `$ `. `rerun.sh` feeds each command list through the correction report's own runner, writes `o0`-`o4`, and `cmp`s each one against its block. It also `cmp`s the manager's capture files in `/tmp/corr1` against the blocks.

Known placeholders (listed, not counted as findings; E1 grep): `C5-PENDING` :208, `ADV-PENDING` :212, `WK-PENDING` :218, `RESULT-PENDING` :241. C5 is unfilled, and no `/tmp/corr1/evidence5.txt` exists yet.

## Checks

Every block is a byte-for-byte comparison of my re-run output against the pasted block (E1 `rerun.sh`: `C0`-`C4 rerun MATCH`). A whole-block MATCH means every command in the block matched, including its `[exit N]` line. My full outputs are pasted in E2.

| block | command (as written in the correction report) | result |
|---|---|---|
| C0 | `sed -n '127p;132p' specs/SPEC_RUBRIC.md` | MATCH |
| C1 | `pwd` | MATCH |
| C1 | `git rev-parse --short HEAD` | MATCH |
| C1 | `sed -n '24p'` original report | MATCH |
| C1 | `git show HEAD:` values spec `\| sed -n '125,126p'` | MATCH |
| C1 | `sed -n '125,126p'` values spec | MATCH |
| C1 | HEAD pipe `\| shasum -a 256` | MATCH |
| C1 | working-copy pipe `\| shasum -a 256` | MATCH |
| C1 | `cmp` of the HEAD and working-copy pipes, `&& echo IDENTICAL` | MATCH |
| C1 | `git diff --numstat HEAD` values spec | MATCH |
| C1 | `sed -n '179p'` original report | MATCH |
| C1 | anchored S13 `grep -c` | MATCH |
| C1 | fragment `grep -o \| wc -l` | MATCH |
| C1 | anchored S13 `grep -n \| cut` | MATCH |
| C1 | `wc -l <` original report | MATCH |
| C1 | banned word `grep -ci` | MATCH |
| C1 | banned string 1 `grep -c` | MATCH |
| C1 | banned string 2 `grep -c` | MATCH |
| C1 | email `grep -cE` | MATCH |
| C1 | `sed -n '72p'` original report | MATCH |
| C1 | `git show HEAD:DECISIONS.md \| grep -c` | MATCH |
| C1 | `wc -l DECISIONS.md` | MATCH |
| C1 | `grep -n 'D-2026-11-12-B:' \| cut -c1-80` | MATCH |
| C1 | `git diff --numstat HEAD` DECISIONS.md | MATCH |
| C2 | fragment `grep -n \| cut -d: -f1` | MATCH |
| C2 | full S13 `grep -o \| wc -l` | MATCH |
| C2 | `sed -n '165,173p' \| grep -n \| cut` | MATCH |
| C3 | `sed -n '160p'` original report | MATCH |
| C4 | `git diff --numstat HEAD` MANIFEST.md | MATCH |
| C4 | `tail -n 2 MANIFEST.md \| cut -c1-80` | MATCH |
| C4 | `shasum -a 256` three original reports | MATCH |
| C4 | `git diff --cached --numstat` five paths | MATCH |

Also checked (E1): the manager's capture files `/tmp/corr1/evidence0.txt`-`evidence4.txt` are each `cmp`-equal to their blocks. This backs process-log step 3. No `$ ` line contains a `<...>` or `...` placeholder (E1 grep, exit 1).

## Findings

1. MAJOR. Correction report :38 says "The original command's output cannot be recovered". That is a factual claim with no pasted output, and it is false. The machine-local session transcript (not under version control) still holds both the original E3 command and its output, at subagent transcript `agent-a6e3dbb26888e10a0.jsonl` lines 61-62, 2026-11-12T09:07:10Z (E1 `tr1.py` and `tr2.py`). The cure could have pasted the actual original output, and it did not. Recovered output: `0`, `      92 /tmp/r6entry/entry.md`, `1`, `0`, `    2370 DECISIONS.md`, `2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first`, `2287:$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'`, `92	0	DECISIONS.md`.

2. MAJOR. The :72 (E3) re-run does not run the original check; it runs a narrowed one. The original command's segment was `grep -n 'D-2026-11-12-B' DECISIONS.md | cut -c1-80`, with no colon (E1 `tr2.py`). It printed two lines, 2280 and 2287 (E1 `tr1.py`), and it still prints two lines now (E1 re-run of the original pattern). The correction runs `grep -n 'D-2026-11-12-B:'`, with a colon. That prints one line, and :41 calls it "the same text E3 recorded". So the match with E3 holds only because the pattern was narrowed. The narrowing also hides that E3's own description at :72 left out the 2287 line, and the correction neither reports nor cures that omission.

3. MINOR. The cure re-runs only four of the seven printed segments of the E3 command. The segments that printed `      92 /tmp/r6entry/entry.md`, `1` (S13 count in the entry) and `0` (banned-string and at-sign scan of the entry) are not re-run (E1 `tr1.py`/`tr2.py`). Two of them can still be re-run now: `wc -l /tmp/r6entry/entry.md` prints `92` and the S13 count prints `1` (E1). The scan cannot be re-shown without its spelled pattern, but the correction does not say this. Yet :38 says the checks are "what follows", and E3's arithmetic (2278 + 92 = 2370) depends on the 92-line entry count.

4. MINOR. :38 states "S1 allows the checks to be shown now" as fact, without labelling it an assessment. The S1 row the correction pastes in C0 says nothing about re-runs. A grep of `specs/SPEC_RUBRIC.md` for `re-run|rerun|recover` finds nothing (E1, exit 1).

5. MINOR. The prose number "two MANIFEST.md rows" (:223, :235) does not match its cited evidence. It cites C4, which prints `14	0	MANIFEST.md`. The correction pastes no baseline from before the unit, so nothing in it shows that this unit appended only two of those 14 lines. My E1 listing of the added lines shows 12 rows from earlier units (2026-11-08 to 2026-11-12) plus the two correction-1 rows. The claim may well be true, but the correction report does not back it.

Observations (not counted as findings):
- :46 ("worker 1 re-ran all of them"), :223 (C5 hashes) and :231 ("C4 and C5 hashes of the original reports match") depend on sections that are still pending. :231 has no backing until C5 is filled.
- :20 says "`cmp` ... prints `IDENTICAL`". `cmp` prints nothing; the chained `echo` prints it. The substance is correct.
- C2's third command shows `[exit 0]`, but that is `cut`'s status: the `grep` found no match. The prose never refers to this command.
- :21 "differs from HEAD elsewhere in the file" is borne out: `git diff -U0` shows no hunk starting at line 125 or 126 (E1, count `0`).
- :28's "it is the last line" holds. The original report ends in a newline, `awk` counts 225 records, and its last line is exactly the S13 sentence (E1 `od`, `awk`, `tail-exact: 1`).

## Verification evidence (command output)

Runner for E1-E3, from the repo root (literal): `bash -c 'while IFS= read -r c; do printf "\$ %s\n" "$c"; eval "$c"; printf "[exit %s]\n\n" "$?"; done' < CMDFILE`. CMDFILE was `/tmp/w1corr/cmds.txt` (E1), `/tmp/w1corr/cmds2.txt` (E2) and `/tmp/w1corr/cmds3.txt` (E3). Each block below is the captured output file, pasted verbatim. In E1, the `tr2.py` output masks the banned spellings as `[BANNED-WORD]`, `[BANNED-1]` and `[BANNED-2]`. Everything else is unaltered.

### E1. Extraction, re-run comparison, string checks, transcript recovery, original-pattern re-runs

```
$ cat /tmp/w1corr/extract.sh
cd /Volumes/Sensidine/Praxis.build
R=docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
sed -n '51,55p' $R > /tmp/w1corr/b0.txt
sed -n '61,154p' $R > /tmp/w1corr/b1.txt
sed -n '160,171p' $R > /tmp/w1corr/b2.txt
sed -n '177,180p' $R > /tmp/w1corr/b3.txt
sed -n '186,203p' $R > /tmp/w1corr/b4.txt
for i in 0 1 2 4; do grep '^\$ ' /tmp/w1corr/b$i.txt | sed 's/^\$ //' > /tmp/w1corr/c$i.txt; done
sed -n '1p' /tmp/w1corr/b3.txt | sed 's/^\$ //' > /tmp/w1corr/c3.txt
wc -l /tmp/w1corr/c0.txt /tmp/w1corr/c1.txt /tmp/w1corr/c2.txt /tmp/w1corr/c3.txt /tmp/w1corr/c4.txt
[exit 0]

$ bash /tmp/w1corr/extract.sh
       1 /tmp/w1corr/c0.txt
      23 /tmp/w1corr/c1.txt
       3 /tmp/w1corr/c2.txt
       1 /tmp/w1corr/c3.txt
       4 /tmp/w1corr/c4.txt
      32 total
[exit 0]

$ cat /tmp/w1corr/rerun.sh
cd /Volumes/Sensidine/Praxis.build
for i in 0 1 2 3 4; do
  bash -c 'while IFS= read -r c; do printf "\$ %s\n" "$c"; eval "$c"; printf "[exit %s]\n\n" "$?"; done' < /tmp/w1corr/c$i.txt > /tmp/w1corr/o$i.txt 2>&1
  if cmp -s /tmp/w1corr/o$i.txt /tmp/w1corr/b$i.txt; then echo "C$i rerun MATCH"; else echo "C$i rerun MISMATCH"; diff /tmp/w1corr/b$i.txt /tmp/w1corr/o$i.txt; fi
done
for p in "0 evidence0" "1 evidence" "2 evidence2" "3 evidence3" "4 evidence4"; do
  set -- $p
  if cmp -s /tmp/corr1/$2.txt /tmp/w1corr/b$1.txt; then echo "C$1 capture-file==block"; else echo "C$1 capture-file!=block"; fi
done
[exit 0]

$ bash /tmp/w1corr/rerun.sh
C0 rerun MATCH
C1 rerun MATCH
C2 rerun MATCH
C3 rerun MATCH
C4 rerun MATCH
C0 capture-file==block
C1 capture-file==block
C2 capture-file==block
C3 capture-file==block
C4 capture-file==block
[exit 0]

$ echo "banned-word: $(grep -ci 'ver''dict' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md) banned-1: $(grep -c 'COMMIT''-INDEX' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md) banned-2: $(grep -c 'COMMIT-DIFF''-SHA256' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md)"
banned-word: 0 banned-1: 0 banned-2: 0
[exit 0]

$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
0
[exit 1]

$ grep -o 'Fills are optimistic; Standard'' resolution on 1-minute bars; 2 ticks/side slippage assumed\.' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md | wc -l
       0
[exit 0]

$ grep -nE 'C5-PENDING|ADV-PENDING|WK-PENDING|RESULT-PENDING' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
208:C5-PENDING
212:ADV-PENDING
218:| worker1 | ADVERSARIAL | WK-PENDING |
241:Result: RESULT-PENDING
[exit 0]

$ grep -nE '^\$ .*(<[a-z]|\.\.\.)' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
[exit 1]

$ tail -c 1 docs/reports/2026-11-12-r6-engine-entry-manager.md | od -c | head -1
0000000   \n                                                            
[exit 0]

$ awk 'END{print NR}' docs/reports/2026-11-12-r6-engine-entry-manager.md
225
[exit 0]

$ A='Fills are optimistic; Standard'; B=' resolution on 1-minute bars; 2 ticks/side slippage assumed.'; echo "tail-exact: $(tail -1 docs/reports/2026-11-12-r6-engine-entry-manager.md | grep -cxF "$A$B")"
tail-exact: 1
[exit 0]

$ git diff -U0 HEAD docs/specs/2026-11-06-walk-forward-values.md | grep -c '^@@ -12[56]'
0
[exit 1]

$ git diff -U0 HEAD MANIFEST.md | grep '^+' | grep -v '^+++' | cut -c1-90
+| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-08 | AMENDMENT ROW (
+| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 2026-11-08 | AMENDMENT ROW (ap
+| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | Report | 2 | 2026-11-08 | Manag
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md | Report | 2 | 2026-
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md | Report | 2 | 2026-
+| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md | Report | 2 | 2026-
+| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Report | 2 | 2026-11-09 
+| /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch | Evidence | 2 | 2026-11-09 |
+| /docs/reports/2026-11-12-r6-engine-entry-manager.md | Report | 3 | 2026-11-12 | Manager
+| /docs/reports/2026-11-12-r6-engine-entry-worker1.md | Report | 3 | 2026-11-12 | ADVERSA
+| /docs/reports/2026-11-12-r6-engine-entry-worker2.md | Report | 3 | 2026-11-12 | ADVERSA
+| /DECISIONS.md | Log | 3 | 2026-11-12 | MODIFIED (unit 2026-11-12-r6-engine-entry; maste
+| /docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md | Report | 3 | 2026-11
+| /docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md | Report | 3 | 2026-11
[exit 0]

$ /usr/bin/python3 -I /tmp/w1corr/tr1.py
SESSION/subagents/agent-a2b7820955025deaa.jsonl 13 2026-11-12T09:26:08.617Z
"| /DECISIONS.md | Log | 3 | 2026-11-12 | MODIFIED (unit 2026-11-12-f2-breaker-amendment, Unit F2B; master under D-2026-11-08-D D1, DECISION_LOG row 2026-11-12T05:29:00Z): entry D-2026-11-12-A (breakers #4 and #5 amended to match Rule F2-1; names Rule F2-1 and the 15:00 disposition by script from the F2 proposal :20, :30; adopts the proposal's #4/#5 text :36, :38 as the master's decision, changeable by Amear; not D2(c); breakers SPECIFIED ONLY; no rubric state change) appended at lines 2204-2278 (heading :2205), written before the spec amendment (S4); lines 1-2203 unchanged; ungraded at time of row |\n---\n## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine au\n    2370 DECISIONS.md\n---\n| /docs/reports/2026-11-12-r6-engine-entry-worker2.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 2 report for unit 2\n00000000: 0a                                       .\n92\t0\tDECISIONS.md\n11\t0\tMANIFEST.md"
----
SESSION/subagents/agent-a6e3dbb26888e10a0.jsonl 62 2026-11-12T09:07:10.913Z
"0\n      92 /tmp/r6entry/entry.md\n1\n0\n    2370 DECISIONS.md\n2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first\n2287:$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'\n92\t0\tDECISIONS.md"
----
[exit 0]

$ /usr/bin/python3 -I /tmp/w1corr/tr2.py
line 61 2026-11-12T09:07:10.508Z
git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'; bash /tmp/r6entry/build.sh > /tmp/r6entry/entry.md && wc -l /tmp/r6entry/entry.md && grep -c 'Fills are optimistic' /tmp/r6entry/entry.md && grep -ci '[BANNED-WORD]\|[BANNED-1]\|[BANNED-2]\|@' /tmp/r6entry/entry.md; cat /tmp/r6entry/entry.md >> DECISIONS.md && wc -l DECISIONS.md && grep -n 'D-2026-11-12-B' DECISIONS.md | cut -c1-80 && git diff --numstat HEAD -- DECISIONS.md
[exit 0]

$ grep -n 'D-2026-11-12-B' DECISIONS.md | cut -c1-80
2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first
2287:$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'
[exit 0]

$ wc -l /tmp/r6entry/entry.md
      92 /tmp/r6entry/entry.md
[exit 0]

$ grep -c 'Fills are optimistic' /tmp/r6entry/entry.md
1
[exit 0]

$ sed -n '38p' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
These are re-runs at correction time (HEAD `c29d08b`, C1), not the original command's output. The original command's output cannot be recovered; S1 allows the checks to be shown now, which is what follows (C1):
[exit 0]

$ grep -n 're-run\|rerun\|recover' specs/SPEC_RUBRIC.md
[exit 1]

$ sed -n '223p;235p' docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md
2. Ran the C1, C2 and C3 checks; appended the two MANIFEST.md rows (C4: `14	0	MANIFEST.md`, last two rows printed); recorded hashes of the original report and its two worker reports (C4), and again at unit end (C5) to show they did not change during this unit.
None. Instruction followed: no `git add`, no index or HEAD change. The C4 cached numstat over MANIFEST.md, DECISIONS.md, the original report and both correction reports prints nothing. Files written by this unit (unstaged): this report, the worker 1 report, and the two MANIFEST.md rows (C4).
[exit 0]

```

### E2. Full re-run outputs of C0-C4 (files o0-o4 written by rerun.sh; each cmp-equal to its block per E1)

```
$ cat /tmp/w1corr/o0.txt
$ sed -n '127p;132p' specs/SPEC_RUBRIC.md
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
[exit 0]

[exit 0]

$ cat /tmp/w1corr/o1.txt
$ pwd
/Volumes/Sensidine/Praxis.build
[exit 0]

$ git rev-parse --short HEAD
c29d08b
[exit 0]

$ sed -n '24p' docs/reports/2026-11-12-r6-engine-entry-manager.md
1. Read the rubric rows, the R6 design at `bf6fcc7` (all 123 lines), D-2026-11-12-A (:2205-2278), Amendment 1 of the Phase 3 spec (:190, :212, :224), DECISION_LOG :765 and :861, DECISIONS :1572-1579 and :1940-1944, values spec :125-126 (identical at HEAD and in the working copy), the cost model's version field.
[exit 0]

$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '125,126p'
  4. ≥ 250 aggregate OOS trades
  5. ≥ 60% of walk-forward windows profitable
[exit 0]

$ sed -n '125,126p' docs/specs/2026-11-06-walk-forward-values.md
  4. ≥ 250 aggregate OOS trades
  5. ≥ 60% of walk-forward windows profitable
[exit 0]

$ git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '125,126p' | shasum -a 256
12120c9a6ccb3edad1f5c53e65ca0f20ceceb1ddfe8e172f7840879db7fdaa66  -
[exit 0]

$ sed -n '125,126p' docs/specs/2026-11-06-walk-forward-values.md | shasum -a 256
12120c9a6ccb3edad1f5c53e65ca0f20ceceb1ddfe8e172f7840879db7fdaa66  -
[exit 0]

$ cmp <(git show HEAD:docs/specs/2026-11-06-walk-forward-values.md | sed -n '125,126p') <(sed -n '125,126p' docs/specs/2026-11-06-walk-forward-values.md) && echo IDENTICAL
IDENTICAL
[exit 0]

$ git diff --numstat HEAD -- docs/specs/2026-11-06-walk-forward-values.md
21	21	docs/specs/2026-11-06-walk-forward-values.md
[exit 0]

$ sed -n '179p' docs/reports/2026-11-12-r6-engine-entry-manager.md
Run before this E10 block was inserted; the block adds no full S13 sentence, no banned word and no email (re-checked after insertion, below the block's insertion by the same counts on this file).
[exit 0]

$ grep -c '^Fills are optimistic; Standard.*assumed\.$' docs/reports/2026-11-12-r6-engine-entry-manager.md
1
[exit 0]

$ grep -o 'Fills are optimistic; Standard' docs/reports/2026-11-12-r6-engine-entry-manager.md | wc -l
       2
[exit 0]

$ grep -n '^Fills are optimistic; Standard.*assumed\.$' docs/reports/2026-11-12-r6-engine-entry-manager.md | cut -d: -f1
225
[exit 0]

$ wc -l < docs/reports/2026-11-12-r6-engine-entry-manager.md
     225
[exit 0]

$ grep -ci 'ver''dict' docs/reports/2026-11-12-r6-engine-entry-manager.md
0
[exit 1]

$ grep -c 'COMMIT''-INDEX' docs/reports/2026-11-12-r6-engine-entry-manager.md
0
[exit 1]

$ grep -c 'COMMIT-DIFF''-SHA256' docs/reports/2026-11-12-r6-engine-entry-manager.md
0
[exit 1]

$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-r6-engine-entry-manager.md
0
[exit 1]

$ sed -n '72p' docs/reports/2026-11-12-r6-engine-entry-manager.md
E3. S4 order. E1 shows, before the entry was written, 0 hits for `D-2026-11-12-B` at HEAD and in the working copy, and 2278 lines in DECISIONS.md. The entry was then built by `/tmp/r6entry/build.sh` and appended in one command whose first segment repeated the HEAD check (it printed `0`), whose last segments printed `2370 DECISIONS.md`, `2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first` and `92	0	DECISIONS.md`. That command's full text also carried a banned-string scan whose pattern spells the words this report may not contain, so it is not pasted; its results are re-run without those spellings in E10 (S1 gap, recorded). 2278 + 92 = 2370.
[exit 0]

$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'
0
[exit 1]

$ wc -l DECISIONS.md
    2370 DECISIONS.md
[exit 0]

$ grep -n 'D-2026-11-12-B:' DECISIONS.md | cut -c1-80
2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first
[exit 0]

$ git diff --numstat HEAD -- DECISIONS.md
92	0	DECISIONS.md
[exit 0]

[exit 0]

$ cat /tmp/w1corr/o2.txt
$ grep -n 'Fills are optimistic; Standard' docs/reports/2026-11-12-r6-engine-entry-manager.md | cut -d: -f1
160
225
[exit 0]

$ grep -o 'Fills are optimistic; Standard'' resolution on 1-minute bars; 2 ticks/side slippage assumed\.' docs/reports/2026-11-12-r6-engine-entry-manager.md | wc -l
       1
[exit 0]

$ sed -n '165,173p' docs/reports/2026-11-12-r6-engine-entry-manager.md | grep -n 'Fills are optimistic; Standard' | cut -c1-120
[exit 0]

[exit 0]

$ cat /tmp/w1corr/o3.txt
$ sed -n '160p' docs/reports/2026-11-12-r6-engine-entry-manager.md
$ cd /Volumes/Sensidine/Praxis.build && A='Fills are optimistic; Standard resolution'; B=' on 1-minute bars; 2 ticks/side slippage assumed.'; S="$A$B"; for f in docs/reports/2026-11-12-r6-engine-entry-manager.md docs/reports/2026-11-12-r6-engine-entry-worker1.md docs/reports/2026-11-12-r6-engine-entry-worker2.md; do echo "$f full=$(grep -cF "$S" "$f") last=$(tail -1 "$f" | grep -cxF "$S") banned=$(grep -ciE 'verd''ict|COMMIT-IN''DEX|COMMIT-DIFF-SHA''256' "$f") email=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}' "$f")"; done; echo "entry full=$(sed -n '2279,2370p' DECISIONS.md | grep -cF "$S") last=$(sed -n 2370p DECISIONS.md | grep -cxF "$S") banned=$(sed -n '2279,2370p' DECISIONS.md | grep -ciE 'verd''ict|COMMIT-IN''DEX|COMMIT-DIFF-SHA''256') at=$(sed -n '2279,2370p' DECISIONS.md | grep -c '@')"; diff /tmp/r6entry/DECISIONS.pre-cure2.md DECISIONS.md | grep '^[0-9]'; sed -n 861p DECISION_LOG.md | grep -F -c 'NOT MET'; git -C /Users/admin/Praxis.build-r6 show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n 68p | grep -F -c 'Skip the whole post-release leg on any early-close day'; git diff --numstat HEAD -- DECISIONS.md MANIFEST.md; git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'; grep -c 'D-2026-11-12-B' DECISIONS.md; wc -l < DECISIONS.md 2>&1 | tee /tmp/r6entry/e10.txt
[exit 0]

[exit 0]

$ cat /tmp/w1corr/o4.txt
$ git diff --numstat HEAD -- MANIFEST.md
14	0	MANIFEST.md
[exit 0]

$ tail -n 2 MANIFEST.md | cut -c1-80
| /docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md | Report | 3 
| /docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md | Report | 3 
[exit 0]

$ shasum -a 256 docs/reports/2026-11-12-r6-engine-entry-manager.md docs/reports/2026-11-12-r6-engine-entry-worker1.md docs/reports/2026-11-12-r6-engine-entry-worker2.md
2dbd7fcc0f22c90cc567b6e76c3d491cff9418b04898925100b87fcce70c8343  docs/reports/2026-11-12-r6-engine-entry-manager.md
195282fe82dba53577428d4b3f21728ff9f35b6bb625f951a9eda545b4e13ecb  docs/reports/2026-11-12-r6-engine-entry-worker1.md
5c72f7fcf1f064f067543f476629e572e1a64998b95979bde601b794c8bff18b  docs/reports/2026-11-12-r6-engine-entry-worker2.md
[exit 0]

$ git diff --cached --numstat -- MANIFEST.md DECISIONS.md docs/reports/2026-11-12-r6-engine-entry-manager.md docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
[exit 0]

[exit 0]

```

### E3. Self-check of this report

```
$ echo "banned-word: $(grep -ci 'ver''dict' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md) banned-1: $(grep -c 'COMMIT''-INDEX' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md) banned-2: $(grep -c 'COMMIT-DIFF''-SHA256' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md)"
banned-word: 0 banned-1: 0 banned-2: 0
[exit 0]

$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
0
[exit 1]

$ grep -o 'Fills are optimistic; Standard'' resolution on 1-minute bars; 2 ticks/side slippage assumed\.' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md | wc -l
       1
[exit 0]

$ A='Fills are optimistic; Standard'; B=' resolution on 1-minute bars; 2 ticks/side slippage assumed.'; echo "standalone: $(grep -cxF "$A$B" docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md) last: $(tail -1 docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md | grep -cxF "$A$B")"
standalone: 1 last: 1
[exit 0]

$ grep -cx 'Result: FAIL' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
1
[exit 0]

$ grep -cx '## Verification evidence (command output)' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
1
[exit 0]

$ grep -cE '^Result: (PASS|FAIL|BLOCKED)$' docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md
1
[exit 0]

```

## Result

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
