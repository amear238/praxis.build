# 2026-11-11 v-rulings-filing Correction 2 - worker3 (BUILD, fix pass)

## Task
Unit `2026-11-11-v-rulings-filing-correction-2` (bead Praxis_build-n1y), mode BUILD (fix). An adversarial check of the unit's first build pass found six defects. This pass fixes them in three files: (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, (b) docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md, and (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md. This report is the fourth file. The original bodies of (a) (lines 1-264 and the last line) and (b) (lines 1-241 and the last line) stay byte-identical to /tmp/c2pre/. Only their Correction 2 sections were revised in place. In (c), no existing line was changed and one addendum was inserted. Nothing was staged or committed. MANIFEST, DECISIONS, the ledgers and .claude/ were not touched. Before editing, (a), (b) and (c) were copied to /tmp/c2fix/, and every "before" diff below is against those copies. In correction text, the standing limitation sentence is called "the S13 sentence", and output masks it as `<S13>`.

## Commands and output
All commands were run on 2026-11-11 from the repo root under bash. Helper scripts are in /tmp/c2fix/ and /tmp/vrf-c2/, outside the repo. tx.py and rec.py are pasted in full in (a) C2.1. Definitions:
```
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
A=docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
B=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
T=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl
W=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl
S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }
Fz() { perl -pe 's/^(\s*)\x60\x60\x60/$1<fence>/'; }
C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
W3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
```

### Defect 1 (MAJOR): (a) C2.1, the skeleton claims
C2.1 was rewritten in place. It now runs from (a):280 to (a):613, followed by a blank line at 614. The old negative is kept and scoped to "no copy under /tmp, /private/tmp or in git". The skeleton is RECOVERED from the session transcript (machine-local, not version-controlled) in two places. The first is the manager's Write call at 2026-11-11T19:33:58.402Z in T. The second is worker1's own read at 2026-11-11T19:37:00Z in W, which is the command and output behind (a) section 7, and it was not named in the brief. Both are pasted in full in (a) C2.1. The key outputs, re-run for this report:
```
$ python3 -I /tmp/c2fix/tx.py write $T v-rulings-filing-correction-1-manager.md | M
matching_Write_calls=1
timestamp=2026-11-11T19:33:58.402Z tool=Write file_path=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
name_count_ci=0 newline_terminated_lines=27 ends_with_newline=True
hash_hash_space_lines=8 pending_paren_lines=8 PENDING_containing_lines=1
     1	# 2026-11-11 v-rulings-filing Correction 1 - manager report
     2	
     3	## Task
     4	(pending)
     5	
     6	## Rubric criteria addressed
     7	(pending)
     8	
     9	## Workers dispatched (id, mode, outcome)
    10	(pending)
    11	
    12	## Process log
    13	(pending)
    14	
    15	## Verification evidence (command output)
    16	(pending)
    17	
    18	## Adversarial findings
    19	(pending)
    20	
    21	## S6 cross-block check
    22	(pending)
    23	
    24	## Files staged
    25	(pending)
    26	
    27	Result: PENDING
$ python3 -I /tmp/c2fix/tx.py write $T v-rulings-filing-correction-1-manager.md | M | wc -l
      31
```
```
$ python3 -I /tmp/c2fix/rec.py amatch $T $W $PA | M
read_output_lines=30 write_content_lines=27
read_output_cat_n_part_equals_write_content=True
original_line_209_is_an_exact_line_of_recovered_read_output=True
original_line_210_is_an_exact_line_of_recovered_read_output=True
original_line_211_is_an_exact_line_of_recovered_read_output=True
original_line_213_is_an_exact_line_of_recovered_read_output=True
original_line_214_is_an_exact_line_of_recovered_read_output=True
original_line_216_is_an_exact_line_of_recovered_read_output=True
original_line_212_is_an_exact_line_of_recovered_read_output=False
original_line_215_is_an_exact_line_of_recovered_read_output=False
$ python3 -I /tmp/c2fix/rec.py amatch $T $W $PA | M | wc -l
      10
$ python3 -I /tmp/c2fix/rec.py classify $T $W $PA | M
1 header(#)
2 blank
3 header(##)
4 (pending)
5 blank
6 header(##)
7 (pending)
8 blank
9 header(##)
10 (pending)
11 blank
12 header(##)
13 (pending)
14 blank
17 blank
18 header(##)
19 (pending)
20 blank
21 header(##)
22 (pending)
23 blank
24 header(##)
25 (pending)
26 blank
$ python3 -I /tmp/c2fix/rec.py classify $T $W $PA | M | wc -l
      24
$ python3 -I /tmp/c2fix/rec.py classify $T $W $PA | grep -c OTHER
0
```
Outcome on the recovered evidence: (a) :209, :210, :211 (as recovered `stat` output, consistent with the Write timestamp 19:33:58Z = 14:33:58 EST; the file mtime itself is not re-runnable), :213/:214/:216, the second sentence of :218, and :250 HOLD. The first sentence of :218, "All nine sections read `(pending)`.", is WRONG: there are 8 `## ` lines and 8 `(pending)` lines. The search for other "cannot be re-run" wording in the (a) and (b) Correction 2 sections:
```
$ grep -n -e 'cannot be re-run' -e 're-runnable' -e 're-executed' -e 'UNVERIFIED' $A | awk -F: '$1>=265' | M | S
314:Result of the re-run on current files. The manager report has been rewritten since section 7 was written. It now has 242 lines and mtime 2026-11-11T14:40:46, with 8 lines starting `## `, 0 lines equal to `(pending)` and 0 lines containing `PENDING`. It is untracked and not in the index, so git holds no earlier copy. Under /tmp and /private/tmp, the only file whose name contains `correction-1-manager` is the /tmp/c2pre copy. That copy has 242 lines and was written at 17:08:51, so it is not the skeleton. So there is no copy of the skeleton under /tmp, /private/tmp or in git. That negative covers those three places only. The earlier version of this item stopped there and labelled :209-211, :213-216, :218 and :250 UNVERIFIED (not re-runnable). This version replaces that label with the recovered evidence below.
609:- :211 `2026-11-11T14:33:58` HOLDS as recovered output. It is line 3 of worker1's output, printed by `stat` at 19:37:00Z. It is consistent with the recorded Write timestamp: 2026-11-11T19:33:58.402Z is 2026-11-11T14:33:58 EST, and this machine's zone is EST-0500. The file mtime itself is not re-runnable, because the file has since been rewritten.
$ grep -n -e 'cannot be re-run' -e 're-runnable' -e 're-executed' -e 'UNVERIFIED' $A | awk -F: '$1>=265' | M | S | wc -l
       2
$ grep -n -e 'cannot be re-run' -e 're-runnable' -e 're-executed' -e 'UNVERIFIED' $B | awk -F: '$1>=242' | M | S
492:Original wording: :207 `2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1`; :217 `2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1`. Both outputs describe earlier, shorter states of this file. Those file states cannot be re-executed. The original outputs are **RECOVERED from the session transcript (machine-local, not version-controlled)**, and they match :207 and :217 (blocks below). T is the manager's transcript. tx.py and rec.py are pasted in full in Correction 2 item C2.1 of docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md. These definitions are used in addition to the Method block:
$ grep -n -e 'cannot be re-run' -e 're-runnable' -e 're-executed' -e 'UNVERIFIED' $B | awk -F: '$1>=242' | M | S | wc -l
       1
```
In (a), :314 is the scoped negative and :609 is the mtime statement. C2.5 does not repeat the wording. In (b), the only hit is :492, the relabelled C2.3 ("Those file states cannot be re-executed").

### Defect 2: (b) C2.3, S13 positions 210 and 235
C2.3 now runs from (b):491 to (b):597. It pastes the `grepuse` list, the 19:40:23 result (210 lines), and the full 19:40:29 and 19:40:36 tool calls from T. The line match is below. :207 is in the 19:40:29 result and :217 is in the 19:40:36 result, so the label now reads RECOVERED and matching:
```
$ python3 -I /tmp/c2fix/rec.py bmatch $T $PB | M
original_line_207 in_19:40:29_result=True in_19:40:36_result=False
original_line_208 in_19:40:29_result=True in_19:40:36_result=False
original_line_210 in_19:40:29_result=True in_19:40:36_result=False
original_line_214 in_19:40:29_result=True in_19:40:36_result=True
original_line_215 in_19:40:29_result=True in_19:40:36_result=True
original_line_216 in_19:40:29_result=True in_19:40:36_result=True
original_line_217 in_19:40:29_result=False in_19:40:36_result=True
$ python3 -I /tmp/c2fix/rec.py bmatch $T $PB | M | wc -l
       7
```

### Defect 3: (b) C2.4, placeholder commands and the tail-truncated output
New item, (b):599-682. It quotes :206 and :213 exactly and states that `| tail -3` keeps only 3 of 17 lines. It recovers the real commands from the 19:40:29 and 19:40:46 calls (the 19:40:46 call is pasted in full, with lines that begin with three backticks shown as `<fence>`). The full output of the tail-cut run itself was never printed, so it cannot be recovered. A full count.sh run is pasted. The same run on the final files:
```
$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | M
name-length=4 matching-files=1
0	docs/reports/2026-11-11-v-rulings-filing-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-worker1.md
0	docs/reports/2026-11-11-v-rulings-filing-worker2.md
0	docs/reports/2026-11-11-v-rulings-filing-worker3.md
0	docs/reports/2026-11-11-v-rulings-filing-worker4.md
0	docs/reports/2026-11-11-v-rulings-filing-worker5.md
0	docs/reports/2026-11-11-v-rulings-filing-worker6.md
0	docs/reports/2026-11-11-v-rulings-filing-worker7.md
0	docs/reports/2026-11-11-v-rulings-filing-worker8.md
0	docs/reports/2026-11-11-v-rulings-filing-worker9.md
0	docs/reports/2026-11-11-v-rulings-filing-worker10.md
0	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
0	vm/replies/20261111T172933Z-python-git-install.md
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
0	DECISIONS.md (tail -n +2100)
$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | M | wc -l
      17
```

### Defect 4: byte-exact quotes
(a):281 now quotes :210 with its 6 leading spaces. (b) C2.2 has a new heading at (b):426 and an "Original wording:" line at (b):427 that quotes :238 with its leading `- `. Check of every `:N` quote in an "Original wording:" line against line N of the /tmp/c2pre copy, plus the two unnumbered quotes and the S definition quoted in (c):
```
$ python3 -I /tmp/c2fix/qcheck.py
(a):281 quotes :209  equal_to_pre_line=True  substring_of_pre_line=True
(a):281 quotes :210  equal_to_pre_line=True  substring_of_pre_line=True
(a):281 quotes :211  equal_to_pre_line=True  substring_of_pre_line=True
(a):281 quotes :218  equal_to_pre_line=True  substring_of_pre_line=True
(a):616 quotes :226  equal_to_pre_line=True  substring_of_pre_line=True
(a):644 quotes :228  equal_to_pre_line=True  substring_of_pre_line=True
(a):644 quotes :240  equal_to_pre_line=True  substring_of_pre_line=True
(a):644 quotes :242  equal_to_pre_line=False  substring_of_pre_line=True
(a):826 quotes :257  equal_to_pre_line=False  substring_of_pre_line=True
(a):826 quotes :261  equal_to_pre_line=True  substring_of_pre_line=True
(a):826 quotes :262  equal_to_pre_line=True  substring_of_pre_line=True
(b):427 quotes :238  equal_to_pre_line=True  substring_of_pre_line=True
(b):492 quotes :207  equal_to_pre_line=True  substring_of_pre_line=True
(b):492 quotes :217  equal_to_pre_line=True  substring_of_pre_line=True
(b):600 quotes :206  equal_to_pre_line=True  substring_of_pre_line=True
(b):600 quotes :213  equal_to_pre_line=True  substring_of_pre_line=True
$ python3 -I /tmp/c2fix/qcheck.py | wc -l
      16
$ python3 -I -c 'import sys; a=open(sys.argv[1]).read().split("\n"); pa=open(sys.argv[2]).read().split("\n"); b=open(sys.argv[3]).read().split("\n"); pb=open(sys.argv[4]).read().split("\n"); qa=a[820].split("Original wording: \"")[1].rsplit("\"",1)[0]; qb=b[257].split("Original wording: \"")[1].rsplit("\"",1)[0]; print("(a):821 quote substring of PA:252 =", qa in pa[251]); print("(b):258 quote substring of PB:228 =", qb in pb[227])' $A $PA $B $PB
(a):821 quote substring of PA:252 = True
(b):258 quote substring of PB:228 = True
$ grep -cF "$(sed -n 4p /tmp/c2fix/defs.sh)" $C
1
```
The 2 `False` rows are partial quotes from the first build pass that this pass did not touch ((a):644 quotes part of :242, and (a):826 quotes part of :257). Both are substrings of their lines.

### Defect 5: the two ./Redemtion/ rows
I chose the alternative. A block numbering the two files `<gitignored-file-1>` and `<gitignored-file-2>`, with their per-file counts and `sort -u | wc -l` = 2, was added after the body-search block in (a) C2.3 ((a):752-772) and in (b) C2.1 ((b):365-385). The paths stay withheld. The block as pasted in both files:
```
$ grep -rIli --exclude-dir=.git --exclude-dir=evidence -- "$N" ./Redemtion | LC_ALL=C sort | awk '{print "./Redemtion/<gitignored-file-" NR ">"}' | M
./Redemtion/<gitignored-file-1>
./Redemtion/<gitignored-file-2>
$ grep -rIli --exclude-dir=.git --exclude-dir=evidence -- "$N" ./Redemtion | LC_ALL=C sort | awk '{print "./Redemtion/<gitignored-file-" NR ">"}' | M | wc -l
       2
$ grep -rIli --exclude-dir=.git --exclude-dir=evidence -- "$N" ./Redemtion | LC_ALL=C sort | while IFS= read -r p; do printf "ci=%s ciw=%s\n" "$(grep -ci -- "$N" "$p")" "$(grep -ciw -- "$N" "$p")"; done | awk '{print "./Redemtion/<gitignored-file-" NR ">: " $0}' | M
./Redemtion/<gitignored-file-1>: ci=1 ciw=0
./Redemtion/<gitignored-file-2>: ci=1 ciw=0
$ grep -rIli --exclude-dir=.git --exclude-dir=evidence -- "$N" ./Redemtion | LC_ALL=C sort | while IFS= read -r p; do printf "ci=%s ciw=%s\n" "$(grep -ci -- "$N" "$p")" "$(grep -ciw -- "$N" "$p")"; done | awk '{print "./Redemtion/<gitignored-file-" NR ">: " $0}' | M | wc -l
       2
$ grep -rIli --exclude-dir=.git --exclude-dir=evidence -- "$N" ./Redemtion | LC_ALL=C sort -u | wc -l
       2
$ /tmp/vrf-c2/repogrep.sh nw | grep '^\./Redemtion/'
./Redemtion/<gitignored-file>: 1
./Redemtion/<gitignored-file>: 1
$ /tmp/vrf-c2/repogrep.sh nw | grep '^\./Redemtion/' | wc -l
       2
```

### Defect 6: (c) addendum
The addendum is inserted at (c):452-566 (566 is a blank line), just before the S13 line. It defines R, backs (c):12 and (c):16 with pasted output, shows the insert script, and reproduces it on copies of the /tmp/c2pre files in a mktemp directory, with two negative controls. It also lists the superseded blocks. All 7 fenced blocks in (c) sections 1-5 still appear verbatim in (a) or (b) (block check in the addendum), so (c):20 holds for those blocks. The conclusions of (c) section 1, its section 5 label, its first out-of-scope bullet, its Self-check figures and its Result line are marked superseded.

## Edits made with line ranges
Hunks against the copies taken before this pass (`c` means changed in place, `a` means added), with the resulting section map:
```
$ diff -d /tmp/c2fix/${A##*/} $A | grep -v "^[<>-]"
281c281
314c314
315a316,614
452a752,772
$ diff -d /tmp/c2fix/${A##*/} $A | grep -v "^[<>-]" | wc -l
       4
$ diff -d /tmp/c2fix/${B##*/} $B | grep -v "^[<>-]"
364a365
365a367,386
405c426,428
469c492
470a494,581
486a598,682
$ diff -d /tmp/c2fix/${B##*/} $B | grep -v "^[<>-]" | wc -l
       6
$ grep -n -e '^## Correction 2' -e '^### C2' -e '^## Addendum' $A $B $C
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:265:## Correction 2 (unit 2026-11-11-v-rulings-filing-correction-2, 2026-11-11)
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:280:### C2.1 - Corrects :207-218 (section 7, the read of the manager-report skeleton)
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:615:### C2.2 - Corrects :222-226 (section 8, helper files and DECISIONS.md)
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:643:### C2.3 - Corrects :228-242 (section 8, repo-wide search)
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:820:### C2.4 - Corrects :252 (Findings, out-of-scope note)
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:825:### C2.5 - Corrects :257-263 (self-check)
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:242:## Correction 2 (unit 2026-11-11-v-rulings-filing-correction-2, 2026-11-11)
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:257:### C2.1 - Corrects :228 (out-of-scope note that cites worker1 section 8)
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:426:### C2.2 - Corrects :238 (Files staged, the MANIFEST row positions)
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:491:### C2.3 - Corrects :206-217 (stale S13 positions in the final self-check)
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:599:### C2.4 - Corrects :206 and :213 (placeholder commands, and a tail-truncated output)
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md:452:## Addendum (worker3, fix pass)
$ grep -n -e '^## Correction 2' -e '^### C2' -e '^## Addendum' $A $B $C | wc -l
      12
$ wc -l $A $B $C
     845 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
     567 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
    2096 total
```
- (a): 281 is the :210 quote fix (defect 4). 314, plus the added 316-614, is the C2.1 rewrite (defect 1), so C2.1 is now 280-613 (614 is a blank line). 752-772 is the Redemtion block in C2.3 (defect 5). The Correction 2 section is (a):265-844, where 844 is the blank line before the S13 line at 845.
- (b): 365-385 is the Redemtion block in C2.1 (defect 5; `diff -d` shows it as two hunks around the existing fence pair). 426-428 is the C2.2 heading, the Original wording line and a blank line (defect 4). 492, plus 494-581, is the C2.3 relabel and the recovered blocks (defect 2), so C2.3 is now 491-597. 598-682 is the new C2.4 (defect 3). The Correction 2 section is (b):242-683, where 683 is the blank line before the S13 line at 684.
- (c): 452-566 is the addendum (defect 6). Its first line is the `## Addendum (worker3, fix pass)` heading at 452, and the S13 line is at 567.

## Self-check
Structure. `diff -d` against the /tmp/c2pre copies shows a single `a` hunk for each of (a) and (b), with 0 `<` lines, and the original body ranges and last lines compare equal. For (c), against /tmp/c2fix, `diff -d` shows one add hunk. Plain `diff` shows two add hunks, because it lines up the trailing blank line differently. Either way there are 0 `<` lines:
```
$ diff -d $PA $A | grep -v "^[<>]"
264a265,844
$ diff -d $PA $A | grep -v "^[<>]" | wc -l
       1
$ diff -d $PA $A | grep -c "^<"
0
$ cmp <(head -n 264 $A) <(head -n 264 $PA); echo "first 264 rc=$?"; cmp <(tail -n 1 $A) <(tail -n 1 $PA); echo "last line rc=$?"
first 264 rc=0
last line rc=0
$ diff -d $PB $B | grep -v "^[<>]"
241a242,683
$ diff -d $PB $B | grep -v "^[<>]" | wc -l
       1
$ diff -d $PB $B | grep -c "^<"
0
$ cmp <(head -n 241 $B) <(head -n 241 $PB); echo "first 241 rc=$?"; cmp <(tail -n 1 $B) <(tail -n 1 $PB); echo "last line rc=$?"
first 241 rc=0
last line rc=0
$ diff -d /tmp/c2fix/${C##*/} $C | grep -v "^>"
451a452,566
$ diff -d /tmp/c2fix/${C##*/} $C | grep -v "^>" | wc -l
       1
$ diff -d /tmp/c2fix/${C##*/} $C | grep -c "^<"
0
$ diff /tmp/c2fix/${C##*/} $C | grep -v "^>"
450a451,462
451a464,566
$ diff /tmp/c2fix/${C##*/} $C | grep -v "^>" | wc -l
       2
```
Name, V1, S13 and identifier checks on all four files, final state. This block was produced by re-running it on this report until the output stopped changing. The last re-run matched the pasted text exactly:
```
$ echo "len=${#N}"
len=4
$ /tmp/vrf-c2/selfcheck.sh $A $B $C $W3 | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[845] last_nonblank_line=845 last_nonblank_is_S13=YES lines=845
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[684] last_nonblank_line=684 last_nonblank_is_S13=YES lines=684
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[567] last_nonblank_line=567 last_nonblank_is_S13=YES lines=567
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[323] last_nonblank_line=323 last_nonblank_is_S13=YES lines=323
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ /tmp/vrf-c2/selfcheck.sh $A $B $C $W3 | M | wc -l
       5
$ python3 -I /tmp/vrf-c1/s13.py $A $B $C $W3 | M
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[845] in_fence=0 last_nonblank_line=845 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[684] in_fence=0 last_nonblank_line=684 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker1.md standalone_outside_fence=1 at=[567] in_fence=0 last_nonblank_line=567 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker3.md standalone_outside_fence=1 at=[323] in_fence=0 last_nonblank_line=323 is_last=True substring_lines=1
$ python3 -I /tmp/vrf-c1/s13.py $A $B $C $W3 | M | wc -l
       4
$ for f in $A $B $C $W3; do printf '%s ipv4_lines=%s non_loopback_ipv4=%s email=%s mac_or_keypath=%s\n' "$f" "$(grep -cE '([0-9]{1,3}\.){3}[0-9]{1,3}' $f)" "$(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' $f | grep -vcx '127\.0\.0\.1')" "$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f)" "$(grep -ciE '([0-9a-f]{2}:){5}[0-9a-f]{2}|id_[r]sa|id_[e]d25519|\.p[e]m\b|\.s[s]h/' $f)"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md ipv4_lines=0 non_loopback_ipv4=0 email=0 mac_or_keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md ipv4_lines=0 non_loopback_ipv4=0 email=0 mac_or_keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md ipv4_lines=0 non_loopback_ipv4=0 email=0 mac_or_keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md ipv4_lines=0 non_loopback_ipv4=0 email=0 mac_or_keypath=0
$ git diff --cached --name-only -- $A $B $C $W3 | wc -l
       0
```

## Result: PASS
All six defects are fixed as above. Two things are left for the manager. First, this report has no MANIFEST row, because the brief forbids touching MANIFEST. Second, the recovered evidence depends on the session transcripts under ~/.claude/projects/ and on the helper scripts in /tmp/c2fix/. All of these are machine-local and outside version control, so a checker on another machine cannot re-run those blocks. Not checked: whether any tool call that does not name the file changed the manager report between 19:40:23 and 19:40:46. The `grepuse` list covers only calls whose input contains `correction-1-manager`.

## Erratum (worker5)
Added by worker5 in the second fix pass of unit 2026-11-11-v-rulings-filing-correction-2. No line above was changed. Defect 4 above says it checks "every `:N` quote" in an "Original wording:" line. That overstates the coverage of /tmp/c2fix/qcheck.py. Its pattern `:(\d+) ` needs a space right after the number, so a range reference such as `:223-225` is skipped, and the three quotes after `:223-225` in (a):616 were not checked by it (its output has 0 rows for :223, :224 or :225; last command below). /tmp/c2w5/qcheck2.py, below, also parses `:N-M` references. It pairs the spans in order with lines N to M when the counts agree, lists a reference with no quoted span as no_span, and lists quoted text with no line reference as unnumbered; the two unnumbered quotes, (a):851 (cited above as (a):821) and (b):258, are the ones checked by the `python3 -I -c` command in Defect 4 above. Result: 26 rows, 19 spans MATCH and 0 MISMATCH. The three (a):616 range spans equal lines 223, 224 and 225 of the /tmp/c2pre copy. The two `equal=False` rows are the same partial quotes as above ((a):644 :242 and (a):826 :257). The rows give (a) line numbers after worker5's edit, which inserted 30 lines after (a):314, so (a):616, :644, :821 and :826 cited above appear in the rows as (a):646, :674, :851 and :856. (b) line numbers are unchanged by worker5.
```
$ cat /tmp/c2w5/qcheck2.py
# usage: python3 -I /tmp/c2w5/qcheck2.py
# For every "Original wording:" line after the original body of (a) and (b), parse each line
# reference :N or :N-M and the quoted spans (`...` or "...") that directly follow it, separated by ", ".
# Single :N -> span compared with line N of the /tmp/c2pre copy.
# Range :N-M with exactly M-N+1 spans -> spans paired in order with lines N..M.
# Range with any other span count -> each span is MATCH if it equals or is a substring of some line in N..M.
# References followed by no span are listed as no_span. Quoted text with no reference is listed as unnumbered.
import re
F = {'a': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md', 264),
     'b': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md', 241)}
REF = re.compile(r':(\d+)(?:-(\d+))?(?= )')
def span(t, i):
    q = t[i]
    j = t.index(q, i + 1)
    return t[i + 1:j], j + 1
for k, (cur, pre, body) in F.items():
    c = open(cur, encoding='utf-8').read().split('\n'); p = open(pre, encoding='utf-8').read().split('\n')
    for ln, line in enumerate(c[body:], body + 1):
        if not line.startswith('Original wording:'): continue
        t = line[len('Original wording:'):]; i = 0
        while i < len(t):
            m = REF.match(t, i) if (i == 0 or t[i - 1] == ' ') else None
            if m:
                n1 = int(m.group(1)); n2 = int(m.group(2)) if m.group(2) else n1
                i = m.end() + 1; spans = []
                while i < len(t) and t[i] in '`"':
                    s, i = span(t, i); spans.append(s)
                    if t.startswith(', ', i) and i + 2 < len(t) and t[i + 2] in '`"': i += 2
                    else: break
                ref = ':%d' % n1 if n1 == n2 else ':%d-%d' % (n1, n2)
                if not spans:
                    print('(%s):%d %s no_span' % (k, ln, ref)); continue
                rng = list(range(n1, n2 + 1))
                for x, s in enumerate(spans):
                    if len(spans) == len(rng):
                        L = rng[x]; ok = (s == p[L - 1] or s in p[L - 1]); eq = s == p[L - 1]
                        print('(%s):%d %s span%d -> pre:%d %s equal=%s' % (k, ln, ref, x + 1, L, 'MATCH' if ok else 'MISMATCH', eq))
                    else:
                        hits = [L for L in rng if s in p[L - 1]]
                        print('(%s):%d %s span%d -> pre:%s %s' % (k, ln, ref, x + 1, ','.join(map(str, hits)) or '-', 'MATCH' if hits else 'MISMATCH'))
            elif t[i] in '`"':
                s, i = span(t, i); print('(%s):%d unnumbered span len=%d (not checked here)' % (k, ln, len(s)))
            else:
                i += 1
$ python3 -I /tmp/c2w5/qcheck2.py | M
(a):281 :209 span1 -> pre:209 MATCH equal=True
(a):281 :210 span1 -> pre:210 MATCH equal=True
(a):281 :211 span1 -> pre:211 MATCH equal=True
(a):281 :218 span1 -> pre:218 MATCH equal=True
(a):281 :250 no_span
(a):646 :223-225 span1 -> pre:223 MATCH equal=True
(a):646 :223-225 span2 -> pre:224 MATCH equal=True
(a):646 :223-225 span3 -> pre:225 MATCH equal=True
(a):646 :226 span1 -> pre:226 MATCH equal=True
(a):674 :228 span1 -> pre:228 MATCH equal=True
(a):674 :229-241 no_span
(a):674 :240 span1 -> pre:240 MATCH equal=True
(a):674 :242 span1 -> pre:242 MATCH equal=False
(a):674 :238-239 no_span
(a):851 unnumbered span len=142 (not checked here)
(a):856 :257 span1 -> pre:257 MATCH equal=False
(a):856 :261 span1 -> pre:261 MATCH equal=True
(a):856 :262 span1 -> pre:262 MATCH equal=True
(b):258 unnumbered span len=248 (not checked here)
(b):427 :238 span1 -> pre:238 MATCH equal=True
(b):492 :207 span1 -> pre:207 MATCH equal=True
(b):492 :217 span1 -> pre:217 MATCH equal=True
(b):492 :207 no_span
(b):492 :217 no_span
(b):600 :206 span1 -> pre:206 MATCH equal=True
(b):600 :213 span1 -> pre:213 MATCH equal=True
$ python3 -I /tmp/c2w5/qcheck2.py | wc -l
      26
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c " MATCH "
19
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c MISMATCH
0
$ python3 -I /tmp/c2fix/qcheck.py | grep -c ":22[345] "
0
```

## Manager note (correction-2 manager, after the worker 6 check)
Worker 6 (docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md, Finding 3) found that the Erratum above describes the qcheck.py pattern without pasting the script. The script, in full:
```
$ cat -n /tmp/c2fix/qcheck.py
     1	# usage: python3 -I qcheck.py ; compares each quoted span in a Correction 2 "Original wording:" line with line N of the /tmp/c2pre copy
     2	import re
     3	F = {'a': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md', 264),
     4	     'b': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md', 241)}
     5	for k, (cur, pre, body) in F.items():
     6	    c = open(cur, encoding='utf-8').read().split('\n'); p = open(pre, encoding='utf-8').read().split('\n')
     7	    for i, line in enumerate(c[body:], body + 1):
     8	        if not line.startswith('Original wording:'): continue
     9	        for m in re.finditer(r':(\d+) (`[^`]*(?:`[^`]*)*?`|"[^"]*(?:`[^`]*`[^"]*)*")(?=[;.]|$| Only| The)', line):
    10	            n, q = int(m.group(1)), m.group(2)[1:-1]
    11	            print('(%s):%d quotes :%d  equal_to_pre_line=%s  substring_of_pre_line=%s' % (k, i, n, q == p[n - 1], q in p[n - 1]))
$ cat /tmp/c2fix/qcheck.py | wc -l
      11
```
Line 9 holds the pattern `:(\d+) (`. It requires a space right after the line number, so a range reference such as `:223-225` is not matched.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
