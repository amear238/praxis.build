# 2026-11-11 — vm-agent-hermes correction-1, worker 8 (ADVERSARIAL)

## Task

Unit 2026-11-11-vm-agent-hermes-correction-1, worker 8, mode ADVERSARIAL. Working dir /Volumes/Sensidine/Praxis.build, HEAD 55979ee.

Artifacts under test: `docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md` (696 lines) and `-worker2.md` (1045 lines), as they now stand after worker 7's revision. Worker 6's findings B1-B6 are what that revision was meant to cure. Criteria: S1, S2, S13 (specs/SPEC_RUBRIC.md). The reports were judged against the criteria, not against their fix logs.

What I touched:
- I edited nothing except this report, which I created with `set -o noclobber` after `ls` printed "No such file or directory".
- I staged nothing. I did not touch the git index or /tmp/idx-hermes. No command of mine reads /tmp/idx-hermes.
- My scratch directory is /tmp/hermes-corr1-w8/. I created it fresh: `ls -ld` printed "No such file or directory" first, then `mkdir` printed "created".

The rep-name token was never typed. It was taken at runtime from the PNG filename into `$T`, and every output was masked with `sed "s/$T/<the rep-name token>/g"`. Code blocks use four-backtick fences. In this report the standing limitation sentence is called "the S13 sentence". It appears in full only once, as the last line.

## E1. S1 scan (both reports, read in full)

I read every line of both reports. The two count checks below are the only commands this section needed. Command as run (tool shell, repo root, `W1` and `W2` set to the two report paths):

````
$ echo "w1 MATCH lines in W7-2 chunk1 (532-588):"; sed -n '532,588p' $W1 | command grep -cx 'MATCH'; echo "w1 MISMATCH lines:"; sed -n '532,588p' $W1 | command grep -cx 'MISMATCH'; echo "w1 all MATCH lines 523-637:"; sed -n '523,637p' $W1 | command grep -cx MATCH; echo "w2 MATCH lines 896-984:"; sed -n '896,984p' $W2 | command grep -cx MATCH; command grep -n '18 MATCH\|10 MATCH' $W1 $W2 | cut -c1-140
w1 MATCH lines in W7-2 chunk1 (532-588):
17
w1 MISMATCH lines:
0
w1 all MATCH lines 523-637:
17
w2 MATCH lines 896-984:
10
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:693:  - :497-659 (new): the "Worker 7 evidence" section. W7-1 (:501) quotes 
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:1042:  - :876-1011 (new): the "Worker 7 evidence" section. W7-1 (:880) quote 
````

Worker1 :693 says W7-2 holds "18 MATCH compares". W7-2 holds 17 (5 own-snapshot, 3 manager-snapshot, 2 unedited live reports, 7 protected files/PNG/index). Worker2 :1042 says 10, and there are 10. → C1.

Claims that state a result with no pasted command and raw output in the report:

| file:line | claim | labelled as uncaptured / not evidence? | verdict |
|---|---|---|---|
| w1:693 | "18 MATCH compares" | no | contradicted by the report's own output (17). C1 |
| w1:649, w2:1003 | "None of that later text contains the token. The re-run after the last edit is in the worker 7 return to the manager." | no. It is stated as fact, and its evidence is outside the report | S1 break. True today (E5). C2 |
| w1:499, :527, :681; w2:878, :908, :1030 | "Every reworded line above was replaced one line for one line"; awk ranges "unchanged in number" | no | no diff against the prior revision is pasted. C4 (NOTE) |
| w1:288, :398; w2:70 | worker 5's "leak-check printed 0" | **yes**: "not captured, so the statement is not evidence", and the W7-3 pastes replace it | acceptable |
| w1:16-17, :25, :60, :151, :476-478, :492-493; w2:11, :13, :61, :65, :130-131, :259 | equality with pre-dispatch baselines | **yes**: "baseline from the manager's brief (not observed by this worker)", quoted as text in W7-1, and compared by command in W7-2 (MATCH) | acceptable. See C5 (NOTE) for an in-repo source that is not cited |
| w2:228, :488, :592 | the command worker 4 or the manager actually ran | **yes**: UNVERIFIED | acceptable |
| w1:637 | the 91→92 untracked difference is the worker 6 report | **yes**: "inferred, not checked file by file" | acceptable. My E2 check supports it (C6) |
| w1:105-108 | the `$O` in the snapshot grep is not set in that block (it is set at :184) | n/a | reproducible (worker 6 D2). C7 (NOTE) |

Every other result-bearing line I read has a `$ ` command with raw output under it, or points to one in the other report (w2:132 to worker1 Step 5, and w2:186 to worker1 Step 4b; both targets exist).

## E2. Byte-for-byte re-runs of W7 sections (6 blocks: 4 from worker1, 2 from worker2, plus 2 harness negative controls)

Method:
- For each block, the pasted range was cut out with `sed -n 'A,Bp'` into `<id>.pasted`.
- Every `$ ` line was run through the runner the reports state, `run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 </dev/null; }`. All the lines of one block ran in one subshell, so the assignments carry over.
- The output was masked into `$OUT`, leak-checked, and written to `<id>.mine`.
- The harness was **sourced** in the zsh tool shell, not run as `zsh script`. This keeps the `grep` shell function in scope, so `type grep` reproduces. That was worker 6's one harness difference.
- worker1 chunk 2 gets an unechoed preamble that sets `O` and `W1`, as the report states (":594 … `O` and `W1` set as in chunk 1").

The blocks:

| id | report | lines | content |
|---|---|---|---|
| w1-c1 | worker1 | :532-588 | W7-2 chunk 1: 17 baseline compares |
| w1-c2 | worker1 | :594-621 | W7-2 chunk 2: awk, byte count, birth time, `type grep`, untracked count |
| w1-c3 | worker1 | :627-628 | W7-2 chunk 3: `zsh -c "type grep"` |
| w2-w72 | worker2 | :910-983 | W7-2 whole: 10 compares, the three **negative controls** (cmp rc=1 at chars 156, 15, 2484), the six-byte probes, `$H`, stat, `type grep` x2 |
| w1-w73b | worker1 | :652-656 | W7-3: whole-report token count |
| w2-w73b | worker2 | :1005-1009 | W7-3: whole-report token count |

Harness, verbatim (`/tmp/hermes-corr1-w8/rerun.zsh`):
````
# worker 8 re-run harness. SOURCE it from the zsh tool shell (so the grep shell function is in scope):
#   source /tmp/hermes-corr1-w8/rerun.zsh
cd /Volumes/Sensidine/Praxis.build || return 9
D=/tmp/hermes-corr1-w8
W1=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
W2=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}
run(){ printf '$ %s\n' "$1"; eval "$1" 2>&1 </dev/null; }
# blk ID FILE A B [PRE]: cut pasted range, eval each "$ " line with the stated runner in one subshell,
# mask, store; PRE is an unechoed preamble (state carried over from an earlier chunk).
blk(){ local id=$1 file=$2 a=$3 b=$4 pre=$5
  sed -n "${a},${b}p" $file > $D/$id.pasted
  local -a cmds; cmds=("${(@f)$(command grep '^\$ ' $D/$id.pasted | sed 's/^\$ //')}")
  OUT=$( { eval "$pre"; for c in "${cmds[@]}"; do run "$c"; done; } | sed "s/$T/<the rep-name token>/g" )
  print -r -- "$OUT" > $D/$id.mine
  print -r -- "$OUT" | command grep -ci -- "$T" > $D/$id.leak
}
blk w1-c1 $W1 532 588
blk w1-c2 $W1 594 621 'O=/tmp/hermes-corr1-w1-orig; W1=docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md'
blk w1-c3 $W1 627 628
blk w2-w72 $W2 910 983
blk w1-w73b $W1 652 656
blk w2-w73b $W2 1005 1009
# harness negative controls
sed '3s/.$/X/' $D/w1-c1.pasted > $D/neg-alt.pasted          # 1 byte altered in a pasted copy
run '[ "$(shasum -a 256 < DECISIONS.md | cut -d" " -f1)" = 39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637X ] && echo MATCH || echo MISMATCH' > $D/neg-baseline.mine
for i in w1-c1 w1-c2 w1-c3 w2-w72 w1-w73b w2-w73b; do
  echo "== cmp $i ($(wc -l < $D/$i.pasted | tr -d ' ') pasted lines, $(command grep -c '^\$ ' $D/$i.pasted) commands; leak-check of masked output: $(cat $D/$i.leak))"
  cmp $D/$i.pasted $D/$i.mine; echo "cmp rc=$?"; diff $D/$i.pasted $D/$i.mine
done
echo "== NEG cmp of w1-c1.pasted against a copy with one byte altered (expect rc=1)"
cmp $D/w1-c1.pasted $D/neg-alt.pasted; echo "cmp rc=$?"
echo "== NEG compare against a deliberately wrong DECISIONS.md baseline (expect MISMATCH)"
cat $D/neg-baseline.mine
````

Command as run: ``source /tmp/hermes-corr1-w8/rerun.zsh 2>&1 | tee /tmp/hermes-corr1-w8/cmp.out | sed "s/$(ls /Volumes/Sensidine/Praxis.build/docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$' | sed 's/^2026-10-28-mffu-//; s/-reply\.png$//')/<the rep-name token>/g"``. Raw output:
````
== cmp w1-c1 (57 pasted lines, 21 commands; leak-check of masked output: 0)
/tmp/hermes-corr1-w8/w1-c1.pasted /tmp/hermes-corr1-w8/w1-c1.mine differ: char 315, line 4
cmp rc=1
4c4
< 2026-11-11T15:39:30Z
---
> 2026-11-11T15:46:14Z
== cmp w1-c2 (28 pasted lines, 5 commands; leak-check of masked output: 0)
/tmp/hermes-corr1-w8/w1-c2.pasted /tmp/hermes-corr1-w8/w1-c2.mine differ: char 2338, line 28
cmp rc=1
28c28
< 92
---
> 93
== cmp w1-c3 (2 pasted lines, 1 commands; leak-check of masked output: 0)
cmp rc=0
== cmp w2-w72 (74 pasted lines, 27 commands; leak-check of masked output: 0)
/tmp/hermes-corr1-w8/w2-w72.pasted /tmp/hermes-corr1-w8/w2-w72.mine differ: char 379, line 4
cmp rc=1
4c4
< 2026-11-11T15:41:58Z
---
> 2026-11-11T15:46:14Z
== cmp w1-w73b (5 pasted lines, 2 commands; leak-check of masked output: 0)
/tmp/hermes-corr1-w8/w1-w73b.pasted /tmp/hermes-corr1-w8/w1-w73b.mine differ: char 46, line 2
cmp rc=1
2c2
< 2026-11-11T15:43:04Z
---
> 2026-11-11T15:46:15Z
== cmp w2-w73b (5 pasted lines, 2 commands; leak-check of masked output: 0)
/tmp/hermes-corr1-w8/w2-w73b.pasted /tmp/hermes-corr1-w8/w2-w73b.mine differ: char 46, line 2
cmp rc=1
2c2
< 2026-11-11T15:43:04Z
---
> 2026-11-11T15:46:15Z
== NEG cmp of w1-c1.pasted against a copy with one byte altered (expect rc=1)
/tmp/hermes-corr1-w8/w1-c1.pasted /tmp/hermes-corr1-w8/neg-alt.pasted differ: char 299, line 3
cmp rc=1
== NEG compare against a deliberately wrong DECISIONS.md baseline (expect MISMATCH)
$ [ "$(shasum -a 256 < DECISIONS.md | cut -d" " -f1)" = 39e5ba0c27a1aab9736d6f23ce28efbb663bfcd1bcab5b5f305b2911669bc637X ] && echo MATCH || echo MISMATCH
MISMATCH
````

The untracked count moved from 92 to 93. To see why, I listed the untracked files and their birth times. Command as run (masked):
````
$ f=$(ls docs/reports/evidence/ | command grep '^2026-10-28-mffu-.*-reply\.png$'); T=${f#2026-10-28-mffu-}; T=${T%-reply.png}; { git --no-optional-locks status --short | command grep '^??' | command grep -c .; git --no-optional-locks status --short | command grep '^??' | sed 's/^?? //' | while read p; do [ -e "$p" ] && stat -f "%SB %N" -t "%Y-%m-%dT%H:%M:%S" "$p"; done | sort | awk '$1>="2026-11-11T09:00"'; echo ---; command grep -n 'worker 7 return\|None of that later text' docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker{1,2}.md | cut -c1-200; } | sed "s/$T/<the rep-name token>/g"
93
2026-11-11T09:53:19 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
2026-11-11T09:53:19 docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
2026-11-11T09:53:19 docs/reports/2026-11-10-vm-agent-hermes-ssh.md
2026-11-11T10:05:05 docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md
2026-11-11T10:14:00 docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md
2026-11-11T10:27:30 docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker6.md
2026-11-11T10:43:43 docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md
2026-11-11T10:43:51 docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md
2026-11-11T10:44:37 docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker8.md
---
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:649:Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text a
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:1003:Next is the count over the whole of both reports, run in a separate call. It ran after W7-2 was in place and before this W7-3 text
````
(The `stat -t` format carries no zone. The times are local, -0500.)

Verdict on E2: **no content difference.** Every difference is time-dependent and named:
- `date -u` lines: 4 blocks (w1-c1 :535, w2-w72 :913, w1-w73b :653, w2-w73b :1006).
- Untracked count, 92 → 93 (w1 :621). The 93rd file is this report, born 10:44:37 -0500. The worker 6 report (born 10:27:30) falls between worker 5's 91 and worker 7's 92. That supports w1:637's labelled inference.
- Everything else is byte-identical:
  - all 27 compares (17 + 10) still print MATCH;
  - worker2's three negative controls still fail at chars 156, 15 and 2484, with the same `/dev/fd/14` and `/dev/fd/11` names;
  - the six-byte probes print `__TS__`;
  - `type grep` and `zsh -c "type grep"` reproduce;
  - both whole-report token counts are still 0, now **after** worker 7's last edit.
- The two harness negative controls behave as expected: cmp rc=1 on a 1-byte alteration, and MISMATCH on a wrong baseline. So the harness can detect a difference.

## E3. S2 scan

- **w1:476 "This is proven by hash." and w1:17, :492 "No content was added to the index".** The evidence is a two-point equality: the index digest at dispatch (a brief baseline) and at worker 5's and worker 7's runs. The same report says so for this very digest at w1:634: "This is equality at the dispatch and at 15:39Z; it does not show that nothing changed in between." Worker 7 also downgraded the parallel file claims (w1:478 "same as at dispatch, not unchanged"; w2:65, :986). The index claims were left at "proven". A transient `git add` followed by `git restore --staged` between the two instants would leave the same digest, and HEAD and the reflog would not show it. → C3.
- **w2:139 / :992.** "The controls show the substitution is needed. The rc=0 positive compares show it is sufficient." This is correctly scoped. The rc=0 compares carry "only change", and the controls only locate the first difference (re-run byte-identical in E2). No break.
- **w1:16 "That rules out a content change"** for the PNG. It is relative to a brief baseline that is labelled not observed, and the label is next to the claim. No break.
- **w1:637.** The untracked difference is labelled as inferred, and E2 supports it. No break.
- I found no re-run presented as a 2026-11-10 observation. The "today vs yesterday" qualifiers in worker2 (:27, :259, :328, :404-406, :447) remain.

## E4. S13 placement

Command as run (tool shell, repo root, `W1` and `W2` set, the same `run()` runner, the batch masked). `/tmp/hermes-corr1-w8/s13.py` is a fence-aware script. A fence opens on three or more backticks or tildes, and closes on a line of the same character at least as long. It counts substring hits inside and outside fences, and checks the last non-empty line for an exact match:
````
$ S13="$(sed -n 136p specs/SPEC_RUBRIC.md | command grep -o "\"Fills [^\"]*\"" | head -1 | tr -d "\"")"; printf "%s" "$S13" | shasum -a 256; printf "%s" "$S13" | wc -c
816836b085174d186c602ff95da9035d47853b4ca4e4447c6c4d4b711afcce30  -
      90
$ python3 -I /tmp/hermes-corr1-w8/s13.py "$S13" $W1 $W2
2026-11-11-vm-agent-hermes-correction-1-worker1.md | fences opened: 24 | open at EOF: False | hits outside (line, exact): [(696, True)] | hits inside: [] | last non-empty: 696 exact: True | total substring count: 1 | ends with newline: True
2026-11-11-vm-agent-hermes-correction-1-worker2.md | fences opened: 56 | open at EOF: False | hits outside (line, exact): [(1045, True)] | hits inside: [] | last non-empty: 1045 exact: True | total substring count: 1 | ends with newline: True
$ command grep -cF -- "$S13" $W1 $W2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:1
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:1
$ command grep -ci -- "$T" $W1 $W2
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker1.md:0
docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker2.md:0
$ command grep -oi -- "$T" $W1 $W2 | wc -l
       0
$ printf "%s\n" "token length: chars ${#T}, bytes $(printf %s "$T" | wc -c | tr -d " ")"
token length: chars 4, bytes 4
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-11T15:47:39Z
leak-check of masked output: 0
````
(The last line is the harness's own `echo` of the leak-check on `$OUT`, not a `run` line.)

The rubric-derived sentence is 90 bytes. Its digest 816836b0…ce30 equals the value worker 6 D4 and worker 4 C5 report. Fence counts went from worker 6's 18 and 52 to 24 and 56. The difference is exactly the W7 fences: 6 in worker1 (W7-1, three W7-2 chunks, two W7-3) and 4 in worker2.

Verdict: **HOLDS** for both reports.
- The S13 sentence occurs exactly once in each: worker1 :696, worker2 :1045.
- It is an exact whole line, outside every fence, and the last non-empty line.
- No fence is open at EOF.

## E5. Rep-name token count

The output is in the E4 block: `command grep -ci -- "$T"` gives 0 for both reports, and `grep -oi … | wc -l` gives 0 occurrences. The token is 4 characters and 4 bytes, and exactly one PNG matches the pattern. The same masked run's leak-check printed 0. The earlier run over every file in /tmp/hermes-corr1-w8/ printed 0 for each of the 23 files. That run is not pasted here, because its batch also held a command whose text contains the S13 sentence; it is **not used as evidence**.

Verdict: **HOLDS.** The count is 0 in both reports. This report's own count is in the appended block at the end of the Findings.

## Findings

- **C1 MINOR (S1/S2), worker1 :693.** The fix log says W7-2 holds "18 MATCH compares". The report's own W7-2 output holds 17 (E1 count; E2 re-run: 21 commands, of which 17 are compares). A stated count contradicts the pasted evidence. Worker2's "10" is correct.
- **C2 MINOR (S1), worker1 :649 and worker2 :1003.** "None of that later text contains the token. The re-run after the last edit is in the worker 7 return to the manager." This states a result whose evidence is outside the report, and it is not labelled as uncaptured or not evidence. That is the same class as worker 5's leak-check (B1), which worker 7 itself relabelled. The property is true now: E2 (w1-w73b and w2-w73b, re-run after the last edit) and E4 give 0 and 0.
- **C3 MINOR (S2), worker1 :17, :476, :492.** "No content was added to the index … This is proven by hash" rests on a two-point digest equality. Worker1 :634 says this same equality "does not show that nothing changed in between". The B5 two-point correction was applied to the file claims (w1:478, w2:65) but not to the index claims, so worker1 contradicts itself.
- **C4 NOTE (S1), worker1 :499, :527, :681 and worker2 :878, :908, :1030.** These claim that every reworded line was replaced one line for one line, so that earlier citations and the awk ranges hold. No diff against the pre-worker-7 revision is pasted. Both files were rewritten whole (birth times 10:43:43 and 10:43:51 -0500, E2). The circumstantial evidence is consistent:
  - worker 6's cited lines (w1:288, :398, :479; w2:61, :65, :70, :139, :140, :447) still hold the reworded counterparts;
  - the fence counts rose by exactly the W7 blocks (E4);
  - the awk outputs in W7-2 re-run byte-identically (E2).
- **C5 NOTE (S1 traceability).** The W7-1 baselines are labelled "not observed by this worker", which is honest. But all twelve values appear as pasted command output in the in-repo manager report `docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md` (:50-68), and neither report cites that. Command as run, and its raw output:
  ````
  $ for h in 07720470a993 9cd0c5c6342f 16791c5a1606 c43da4d78a28 6ec6224f4121 2b729b8e4469 39e5ba0c27a1 ff4ba4ac512d 71cf456c349b c06e4b26120a 15af54100ba4 5ac1ef7d17ce; do printf '%s manager-report:%s worker4-report:%s\n' $h "$(command grep -c $h docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md)" "$(command grep -c $h docs/reports/2026-11-11-vm-agent-hermes-correction-1-worker4.md)"; done
  07720470a993 manager-report:2 worker4-report:1
  9cd0c5c6342f manager-report:2 worker4-report:1
  16791c5a1606 manager-report:2 worker4-report:1
  c43da4d78a28 manager-report:2 worker4-report:2
  6ec6224f4121 manager-report:2 worker4-report:2
  2b729b8e4469 manager-report:1 worker4-report:1
  39e5ba0c27a1 manager-report:1 worker4-report:1
  ff4ba4ac512d manager-report:1 worker4-report:1
  71cf456c349b manager-report:1 worker4-report:1
  c06e4b26120a manager-report:1 worker4-report:1
  15af54100ba4 manager-report:1 worker4-report:1
  5ac1ef7d17ce manager-report:1 worker4-report:1
  $ M=docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md; command grep -n '5ac1ef7d17ce\|07720470a993\|71cf456c349b' $M | cut -c1-170; stat -f '%SB | %Sm %N' -t '%Y-%m-%dT%H:%M:%S%z' $M
  50:07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  /tmp/hermes-corr1-mgr-orig/2026-11-10-vm-agent-hermes-ssh.md
  55:07720470a99318d226327708d4592f0a5570c4c08871ac28cbbf5bc602bb9e12  docs/reports/2026-11-10-vm-agent-hermes-ssh.md
  64:71cf456c349ba85b039818b33dc1135218b77ccd78ce37352b5b246ae1cb02a4  HANDOFF.md
  68:5ac1ef7d17ce98a5e256863a10288b12541a502959ffffe3ba79eb282e638ac6  -
  2026-11-11T10:05:05-0500 | 2026-11-11T10:36:11-0500 docs/reports/2026-11-11-vm-agent-hermes-correction-1-manager.md
  ````
  Out of scope, and reported only: the manager report was born at 10:05:05 -0500. That is after worker 1's edits at 09:53:19. Yet its :55 holds the **pre-edit** hash of the live ssh.md. So that block was captured before the file it sits in was created. I did not investigate further.
- **C6 NOTE (E2 reproducibility).** The only E2 differences are 4 `date` lines and the untracked count (92 → 93, which is this report). The worker1 :637 inference about 91 → 92 is supported by the birth times.
- **C7 NOTE (S1 readability), worker1 :108.** The snapshot grep uses `$O`, but `$O` is not assigned in that block or in Step 2. It is assigned at :184. The block reproduces (worker 6 D2), so this is readability only.

Self-check of this report (E4/E5 applied to it). It was run after every section above was written and before this block was inserted. This block adds 15 lines and contains no new fence opening at column 0 outside the one shown. Whether this inserted text holds the token is **not shown** here (the same limit as C2); the re-run after this insertion is in my return to the manager, and it is not evidence in this report:
````
$ S13="$(sed -n 136p specs/SPEC_RUBRIC.md | command grep -o "\"Fills [^\"]*\"" | head -1 | tr -d "\"")"; python3 -I /tmp/hermes-corr1-w8/s13.py "$S13" $R8
2026-11-11-vm-agent-hermes-correction-1-worker8.md | fences opened: 6 | open at EOF: False | hits outside (line, exact): [(281, True)] | hits inside: [] | last non-empty: 281 exact: True | total substring count: 1 | ends with newline: True
$ command grep -ci -- "$T" $R8
0
$ command grep -c "1043" $R8; command grep -c "correction-1-worker2.md:1003:Next" $R8
0
1
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-11T15:49:41Z
leak-check of masked output: 0
````

Worker 6's B1-B6, re-judged as the reports now stand:
- B1 is cured for worker 5's statement (relabelled, with W7-3 pasted). The same defect recurs in W7-3's own closing sentence (C2).
- B2, B3, B4 and B6 are cured. The compares, the re-hash, the proper controls and the environment notes are pasted, and they re-run byte-identically (E2).
- B5 is cured except for the index claim (C3).

## Result

**FAIL at MINOR severity. No BLOCKER.**
- S1 is broken at MINOR in C1 and C2. S2 is broken at MINOR in C3 (and C1). C4-C7 are NOTEs.
- E2: 6 W7 blocks re-run (4 from worker1, 2 from worker2). This includes worker2's three negative controls and two harness negative controls. Only time-dependent lines differ.
- E4 (S13) and E5 (token count 0) HOLD for both reports.
- Nothing I ran contradicts any verdict, count or MATCH that either report pastes as command output.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
