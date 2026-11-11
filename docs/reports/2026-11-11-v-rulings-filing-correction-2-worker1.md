# 2026-11-11 v-rulings-filing Correction 2 - worker1 (BUILD)

## Task
Unit `2026-11-11-v-rulings-filing-correction-2` (bead Praxis_build-n1y), BUILD mode. The audit of unit `2026-11-11-v-rulings-filing-correction-1` failed rubric S1 on two reports. The first is the worker1 report, docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, referred to here as (a): its section 7, section 8 and Findings made count and set claims without full pasted output. The second is the manager report, docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md, referred to here as (b): its :228 repeats those claims. There were also MINOR findings in (b): stale S13 positions at :206-217, and MANIFEST row numbers at :238 that are working-tree positions. This unit does three things:
1. Re-runs every one of those claims and captures the full output.
2. Appends a section "Correction 2" to (a) and (b), changing no existing line.
3. Writes this report.

Criteria: rubric S1 (every claim has pasted command output), S2 (no claim above the evidence), S13 (the S13 sentence is the single standalone last line). Mode BUILD. Files edited: (a), (b), and this report. Nothing was staged or committed. MANIFEST, DECISIONS and the ledgers were not touched.

## Process log
1. Read (a) and (b) in full, with the name masked on output. Confirmed that both match their pre-edit copies in /tmp/c2pre/ (`diff` exit 0) and that the raw name count is 0 in all four files.
2. Wrote helper scripts in /tmp/vrf-c2/ (outside the repo): lib.sh (definitions and the command blocks), repogrep.sh (the repo-wide search, counting on real paths and masking only the output), selfcheck.sh (name count, V1 split detector with a positive control, S13 counts; it prints counts only), and gen_a.sh and gen_b.sh, which run the command blocks and write the correction sections. Every block below was produced by a `run` helper that prints `$ <command>` and then the command's real output. Nothing was typed by hand.
3. The repo-wide search turned up two files under ./Redemtion/. That directory is gitignored and untracked. One of the file titles describes personal matters unrelated to this unit. repogrep.sh masks any path under ./Redemtion/ as `./Redemtion/<gitignored-file>` in its output, as shown in the script. The counts are unaffected. The manager decides whether that mask is acceptable under S1.
4. Generated both sections before editing either file, so every "before" figure was measured on unedited files (`cmp` against /tmp/c2pre/ is in the last block of section 5 below).
5. Inserted each section before the file's last line, the S13 line, with python3 -I. The script asserted that the tail was blank line, S13 line, newline, and that the section contained no S13 sentence. Then checked the insertion with `diff -d` against /tmp/c2pre/ and with `cmp` of the inserted range against the generated section.
6. Wrote this report and ran the self-check on all three files.

## Commands and output
All blocks in sections 1 to 5 were captured before (a) and (b) were edited, by the same run whose output is pasted in their Correction 2 sections. The blocks are byte-identical copies. In sections 1 to 5, every list output is followed by the same command piped to `wc -l`.

Definitions (bash, repo root):
```
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
A=docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
B=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
```

### 1. (a) section 7 claims: the manager-report skeleton (corrects (a) :207-218)
```
$ echo "len=${#N}"
len=4
$ wc -l $B
     242 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
$ stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' $B
2026-11-11T14:40:46
$ grep -c '^## ' $B
8
$ grep -cx '(pending)' $B
0
$ grep -c 'PENDING' $B
0
$ find /tmp /private/tmp -name '*correction-1-manager*' 2>/dev/null | M
/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ find /tmp /private/tmp -name '*correction-1-manager*' 2>/dev/null | wc -l
       1
$ wc -l $PB
     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' $PB
2026-11-11T17:08:51
$ git ls-files -s -- $B | wc -l
       0
$ git ls-tree HEAD -- $B | wc -l
       0
$ grep -ci -- "$N" $B
0
$ grep -ci -- "$N" $PB
0
```
The skeleton is gone. (b) is now 242 lines with mtime 14:40:46, 8 `## ` headers, and 0 `(pending)` lines. It is untracked and unindexed. The only saved copy under /tmp or /private/tmp is /tmp/c2pre, which has 242 lines. The claims at (a) :210 (27 lines), :211 (mtime 14:33:58) and :218 ("All nine sections read `(pending)`", lines 1-14 and 17-26) are relabelled UNVERIFIED (not re-runnable). The name count re-run on the current (b) and on the /tmp/c2pre copy gives 0 and 0.

### 2. (a) section 8 helper files and DECISIONS.md (corrects (a) :222-226)
```
$ for f in /tmp/vrf-c1/count.sh /tmp/vrf-c1/diffs.txt /tmp/vrf-c1/s13.py; do echo "$f: $(grep -ciw -- "$N" $f)"; done
/tmp/vrf-c1/count.sh: 0
/tmp/vrf-c1/diffs.txt: 0
/tmp/vrf-c1/s13.py: 0
$ for f in /tmp/vrf-c1/count.sh /tmp/vrf-c1/diffs.txt /tmp/vrf-c1/s13.py; do echo "$f: $(grep -ciw -- "$N" $f)"; done | wc -l
       3
$ for f in /tmp/vrf-c1/count.sh /tmp/vrf-c1/diffs.txt /tmp/vrf-c1/s13.py; do echo "$f: $(grep -ci -- "$N" $f)"; done
/tmp/vrf-c1/count.sh: 0
/tmp/vrf-c1/diffs.txt: 0
/tmp/vrf-c1/s13.py: 0
$ for f in /tmp/vrf-c1/count.sh /tmp/vrf-c1/diffs.txt /tmp/vrf-c1/s13.py; do echo "$f: $(grep -ci -- "$N" $f)"; done | wc -l
       3
$ wc -l DECISIONS.md
    2203 DECISIONS.md
$ head -n 2099 DECISIONS.md | grep -ciw -- "$N"
0
$ head -n 2099 DECISIONS.md | grep -ci -- "$N"
0
$ tail -n +2100 DECISIONS.md | grep -ci -- "$N"
0
```
These match the original figures: 0, 0, 0, and DECISIONS.md lines 1-2099 whole-word 0. DECISIONS.md is 2203 lines.

### 3. Repo-wide body and filename search (corrects (a) :228-242 and :252, and (b) :228)
The script:
```
$ cat /tmp/vrf-c2/repogrep.sh
#!/bin/bash
# usage: repogrep.sh <w|nw> ; excludes .git and any dir named evidence (only ./docs/reports/evidence exists)
# output masks: the name -> <NAME>; any path under ./Redemtion/ (gitignored, untracked, personal) -> ./Redemtion/<gitignored-file>
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
if [ "$1" = w ]; then FL=-rIliw; CF=-ciw; else FL=-rIli; CF=-ci; fi
grep $FL --exclude-dir=.git --exclude-dir=evidence -- "$N" . | LC_ALL=C sort | while IFS= read -r p; do
  printf '%s: %s\n' "$p" "$(grep $CF -- "$N" "$p")"
done | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s{^\./Redemtion/.*(: \d+)$}{./Redemtion/<gitignored-file>$1}'
$ cat /tmp/vrf-c2/repogrep.sh | wc -l
       9
```
Body search (excluding .git and every directory named evidence; ./docs/reports/evidence is the only one):
```
$ git check-ignore -q Redemtion; echo "check-ignore rc=$?"; git ls-files -- Redemtion | wc -l
check-ignore rc=0
       0
$ find . -path ./.git -prune -o -type d -name evidence -print
./docs/reports/evidence
$ /tmp/vrf-c2/repogrep.sh w
./.claude/agent-memory/praxis-auditor/audit_evidence_standards.md: 1
./.claude/agent-memory/praxis-manager/project_heredoc_commit_text_denied.md: 1
./.claude/agent-memory/praxis-manager/project_stop_gate_newest_file_race.md: 1
./DECISION_LOG.md: 6
./HANDOFF.md: 3
./MANIFEST.md: 2
./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md: 17
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-addendum.md: 6
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-confirm.md: 6
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-final.md: 6
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-recheck.md: 4
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-transcript.md: 9
./docs/reports/2026-10-28-f4-<NAME>-reply-filing.md: 22
./docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md: 9
./docs/reports/2026-10-28-f4-<NAME>-reply-worker3.md: 17
./docs/reports/2026-10-28-f4-<NAME>-reply-worker5-fix.md: 5
./docs/reports/2026-10-28-f4-<NAME>-reply-worker7-fix.md: 2
./docs/reports/2026-10-28-f4-<NAME>-reply-worker9-fix.md: 6
./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md: 4
./docs/reports/2026-10-30-zyd-rulings-append.md: 3
./docs/reports/2026-10-31-7zq-m1-variants.md: 3
./docs/reports/2026-10-31-7zq-m3-append.md: 3
./docs/reports/2026-11-01-csv-analyses-manager.md: 3
./docs/reports/2026-11-02-r-vn3-1-filing-manager.md: 16
./docs/reports/2026-11-02-tickprep-intake-manager.md: 3
./docs/reports/2026-11-06-post-commit-refresh-manager.md: 6
./docs/reports/2026-11-06-status-handoff-evening-manager.md: 1
./docs/reports/2026-11-07-wf-mac-side-maths-manager.md: 13
./docs/reports/2026-11-08-voice-strategy-brief.md: 1
./docs/reports/2026-11-09-c7-manager-memory-off-manager.md: 3
./docs/reports/2026-11-10-c2-park-gate-resume-manager.md: 3
./docs/reports/2026-11-10-d9-housekeeping-manager.md: 40
./docs/reports/2026-11-10-f1-f2-proposal-manager.md: 1
./docs/reports/2026-11-10-housekeeping-2a-manager.md: 2
./docs/reports/2026-11-10-housekeeping-2b-adversarial.md: 5
./docs/reports/2026-11-10-housekeeping-2b-manager.md: 4
./docs/reports/2026-11-10-housekeeping-2b-worker1.md: 5
./docs/reports/2026-11-10-scrub-forward-adversarial.md: 1
./docs/reports/2026-11-10-scrub-forward-c1-adversarial.md: 1
./docs/reports/2026-11-10-scrub-forward-manager.md: 2
./docs/reports/2026-11-10-scrub-forward-worker1.md: 3
./docs/reports/2026-11-11-hermes-replies-grading-worker1.md: 14
./docs/reports/2026-11-11-hermes-replies-grading-worker4.md: 2
$ /tmp/vrf-c2/repogrep.sh w | wc -l
      43
$ /tmp/vrf-c2/repogrep.sh w | grep -c '^\./\.claude/agent-memory/'
3
$ /tmp/vrf-c2/repogrep.sh w | grep -c '^\./docs/reports/'
37
$ /tmp/vrf-c2/repogrep.sh w | grep -v -e '^\./\.claude/agent-memory/' -e '^\./docs/reports/'
./DECISION_LOG.md: 6
./HANDOFF.md: 3
./MANIFEST.md: 2
$ /tmp/vrf-c2/repogrep.sh w | grep -v -e '^\./\.claude/agent-memory/' -e '^\./docs/reports/' | wc -l
       3
$ /tmp/vrf-c2/repogrep.sh w | grep -c '^\./docs/reports/2026-10-28-f4-<NAME>-reply'
11
$ /tmp/vrf-c2/repogrep.sh w | awk -F': ' '{s+=$NF} END{print s}'
265
$ /tmp/vrf-c2/repogrep.sh nw | wc -l
      46
$ /tmp/vrf-c2/repogrep.sh nw | grep -c '^\./\.claude/agent-memory/'
3
$ /tmp/vrf-c2/repogrep.sh nw | grep -c '^\./docs/reports/'
38
$ /tmp/vrf-c2/repogrep.sh nw | grep -vc -e '^\./\.claude/agent-memory/' -e '^\./docs/reports/'
5
$ diff <(/tmp/vrf-c2/repogrep.sh w | sed 's/: [0-9]*$//') <(/tmp/vrf-c2/repogrep.sh nw | sed 's/: [0-9]*$//')
6a7,8
> ./Redemtion/<gitignored-file>
> ./Redemtion/<gitignored-file>
25a28
> ./docs/reports/2026-11-04-proof-of-concept-standard.md
$ diff <(/tmp/vrf-c2/repogrep.sh w | sed 's/: [0-9]*$//') <(/tmp/vrf-c2/repogrep.sh nw | sed 's/: [0-9]*$//') | wc -l
       5
$ join -t: <(/tmp/vrf-c2/repogrep.sh w | sort) <(/tmp/vrf-c2/repogrep.sh nw | sort) | awk -F: '$2!=$3'
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-confirm.md: 6: 7
./docs/reports/2026-10-28-f4-<NAME>-reply-filing.md: 22: 23
./docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md: 9: 10
./docs/reports/2026-10-28-f4-<NAME>-reply-worker3.md: 17: 19
$ join -t: <(/tmp/vrf-c2/repogrep.sh w | sort) <(/tmp/vrf-c2/repogrep.sh nw | sort) | awk -F: '$2!=$3' | wc -l
       4
```
Filename search:
```
$ find docs/reports -path docs/reports/evidence -prune -o -type f -iname "*$N*" -print | LC_ALL=C sort | M
docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-addendum.md
docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-confirm.md
docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-final.md
docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-recheck.md
docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-transcript.md
docs/reports/2026-10-28-f4-<NAME>-reply-filing.md
docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md
docs/reports/2026-10-28-f4-<NAME>-reply-worker3.md
docs/reports/2026-10-28-f4-<NAME>-reply-worker5-fix.md
docs/reports/2026-10-28-f4-<NAME>-reply-worker7-fix.md
docs/reports/2026-10-28-f4-<NAME>-reply-worker9-fix.md
$ find docs/reports -path docs/reports/evidence -prune -o -type f -iname "*$N*" -print | wc -l
      11
$ find . \( -path ./.git -o -path ./docs/reports/evidence \) -prune -o -iname "*$N*" -print | LC_ALL=C sort | M
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-addendum.md
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-confirm.md
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-final.md
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-recheck.md
./docs/reports/2026-10-28-f4-<NAME>-reply-adversarial-transcript.md
./docs/reports/2026-10-28-f4-<NAME>-reply-filing.md
./docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md
./docs/reports/2026-10-28-f4-<NAME>-reply-worker3.md
./docs/reports/2026-10-28-f4-<NAME>-reply-worker5-fix.md
./docs/reports/2026-10-28-f4-<NAME>-reply-worker7-fix.md
./docs/reports/2026-10-28-f4-<NAME>-reply-worker9-fix.md
$ find . \( -path ./.git -o -path ./docs/reports/evidence \) -prune -o -iname "*$N*" -print | wc -l
      11
```

Original figures next to re-run figures:

| claim | where | original | re-run |
|---|---|---|---|
| files with a whole-word body match | (a) :240 | "about 45" (truncated by head -40) | 43 |
| of those, under .claude/agent-memory/ | (a) :230-232, (b) :228 | 3 | 3 |
| of those, under docs/reports/ | (a) :228 "many", (a) :252 and (b) :228 "many" | not counted | 37, 26 of them beyond the 11 named files |
| of those, elsewhere | - | not stated | 3: DECISION_LOG.md, HANDOFF.md, MANIFEST.md |
| sum of per-file whole-word line counts | - | not stated | 265 |
| files with a substring match (`-rIli`) | - | not run | 46. Adds 2 files under ./Redemtion/ and docs/reports/2026-11-04-proof-of-concept-standard.md; 4 files have a higher count |
| report filenames containing the name | (a) :242 and :252, (b) :228 | "at least 11" | 11 |
| filenames containing the name, repo-wide (excluding .git and docs/reports/evidence) | - | not run | 11, the same set |

### 4. MANIFEST positions (corrects (b) :238)
```
$ grep -n -F "docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md" MANIFEST.md | cut -d"|" -f1-2 | M
404:| /docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 
$ grep -n -F "docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md" MANIFEST.md | cut -d"|" -f1-2 | M
405:| /docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 
$ wc -l MANIFEST.md
     405 MANIFEST.md
$ git show HEAD:MANIFEST.md | wc -l
     379
$ diff <(git show HEAD:MANIFEST.md) MANIFEST.md | grep -c '^>'
26
$ diff <(git show HEAD:MANIFEST.md) MANIFEST.md | grep -c '^<'
0
$ diff <(git show HEAD:MANIFEST.md) MANIFEST.md | grep -v '^>'
306a307,314
379a388,405
$ diff <(git show HEAD:MANIFEST.md) MANIFEST.md | grep -v '^>' | wc -l
       2
$ sed -n 307,314p MANIFEST.md | cut -d'|' -f2 | nl -v307 -ba | M
   307	 /docs/specs/2026-11-06-walk-forward-values.md 
   308	 /docs/specs/2026-11-05-walk-forward-spec.md 
   309	 /docs/reports/2026-11-08-wf-spec-amendment-manager.md 
   310	 /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
   311	 /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md 
   312	 /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md 
   313	 /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md 
   314	 /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch 
$ sed -n 307,314p MANIFEST.md | cut -d'|' -f2 | nl -v307 -ba | M | wc -l
       8
$ sed -n 307,314p MANIFEST.md | grep -c diq
2
$ sed -n 388,405p MANIFEST.md | cut -d'|' -f2 | nl -v388 -ba | M
   388	 /DECISIONS.md 
   389	 /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md 
   390	 /vm/replies/20261111T172933Z-python-git-install.md 
   391	 /vm/replies/20261111T172802Z-STATUS.md 
   392	 /vm/replies/20261111T172940Z-STATUS.md 
   393	 /docs/reports/2026-11-11-v-rulings-filing-manager.md 
   394	 /docs/reports/2026-11-11-v-rulings-filing-worker1.md 
   395	 /docs/reports/2026-11-11-v-rulings-filing-worker2.md 
   396	 /docs/reports/2026-11-11-v-rulings-filing-worker3.md 
   397	 /docs/reports/2026-11-11-v-rulings-filing-worker4.md 
   398	 /docs/reports/2026-11-11-v-rulings-filing-worker5.md 
   399	 /docs/reports/2026-11-11-v-rulings-filing-worker6.md 
   400	 /docs/reports/2026-11-11-v-rulings-filing-worker7.md 
   401	 /docs/reports/2026-11-11-v-rulings-filing-worker8.md 
   402	 /docs/reports/2026-11-11-v-rulings-filing-worker9.md 
   403	 /docs/reports/2026-11-11-v-rulings-filing-worker10.md 
   404	 /docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 
   405	 /docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 
$ sed -n 388,405p MANIFEST.md | cut -d'|' -f2 | nl -v388 -ba | M | wc -l
      18
$ sed -n 388,405p MANIFEST.md | grep -c diq
0
$ git diff --cached --name-only -- MANIFEST.md | wc -l
       0
```
Working-tree positions: correction-1 manager row 404, worker1 row 405. These match (b) :238 for the working tree. HEAD has 379 lines. The diff from HEAD is 26 added lines in two hunks, 307-314 (8 rows) and 388-405 (18 rows), with 0 removed lines. MANIFEST.md is not staged.

The 8 rows at 307-314 form the only other hunk. 2 of the 8 contain the text `diq`. Treating them as the 8 bead-diq rows that the brief says stay out of staging is INFERRED. If the master stages HEAD plus the 18 rows at 388-405 in their current order, the staged positions would be 379 + 17 = 396 (manager row) and 379 + 18 = 397 (worker1 row). INFERRED (depends on the master's staging), not observed.

### 5. Self-check of (a) and (b) before the edit, and S13 positions (corrects (a) :257-263 and (b) :206-217)
```
$ cmp $A $PA && echo "A identical to pre-edit copy"; cmp $B $PB && echo "B identical to pre-edit copy"
A identical to pre-edit copy
B identical to pre-edit copy
$ /tmp/vrf-c2/selfcheck.sh $A $B | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ /tmp/vrf-c2/selfcheck.sh $A $B | M | wc -l
       3
$ python3 -I /tmp/vrf-c1/s13.py $A $B | M
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[242] in_fence=0 last_nonblank_line=242 is_last=True substring_lines=1
$ python3 -I /tmp/vrf-c1/s13.py $A $B | M | wc -l
       2
```
Before the edit, (b) had its S13 line at 242, not at the 210 (:207) or 235 (:217) it cites. (a) had it at 265.

### 6. The self-check script (S13 sentence masked as `<S13>` in this output)
```
$ cat /tmp/vrf-c2/selfcheck.sh | sed 's/Fills are optimistic.*assumed\./<S13>/'
#!/bin/bash
# usage: selfcheck.sh <file>... ; prints counts only, never the name or the S13 sentence
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
S='<S13>'
export N S
for f in "$@"; do
  c=$(grep -ci -- "$N" "$f")
  v1=$(perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }' "$f")
  sub=$(grep -cF -- "$S" "$f")
  sa=$(grep -cxF -- "$S" "$f")
  sal=$(grep -nxF -- "$S" "$f" | cut -d: -f1 | tr '\n' ' ')
  lastn=$(grep -n . "$f" | tail -n 1 | cut -d: -f1)
  lastl=$(awk 'NF{l=$0} END{print l}' "$f")
  if [ "$lastl" = "$S" ]; then il=YES; else il=NO; fi
  echo "$f: name_ci=$c V1_HIT_lines=$v1 S13_containing=$sub S13_standalone=$sa at=[${sal% }] last_nonblank_line=$lastn last_nonblank_is_S13=$il lines=$(wc -l < "$f" | tr -d ' ')"
done
# positive control: synthetic stdin line, name letters joined by hyphens; never printed
ctl=$(printf '%s\n' "x $(echo "$N" | sed 's/./&-/g; s/-$//') y" | perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }')
echo "V1 positive control (hyphen-split synthetic line): HIT_lines=$ctl"
$ cat /tmp/vrf-c2/selfcheck.sh | sed 's/Fills are optimistic.*assumed\./<S13>/' | wc -l
      20
```

## Edits made
- (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: inserted lines 265-524 (260 lines, the Correction 2 section, ending in one blank line). The S13 line moved from 265 to 525.
- (b) docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: inserted lines 242-487 (246 lines, the Correction 2 section, ending in one blank line). The S13 line moved from 242 to 488.

```
$ diff -d $PA $A | grep -v '^>'
264a265,524
$ diff -d $PA $A | grep -v '^>' | wc -l
       1
$ diff -d $PA $A | grep -c '^<'
0
$ diff -d $PA $A | grep -c '^>'
260
$ diff $PA $A | grep -v '^>'
262a263,451
263a453,484
264a486,524
$ diff $PA $A | grep -v '^>' | wc -l
       3
$ diff $PA $A | grep -c '^<'
0
$ sed -n 265,524p $A | cmp - /tmp/vrf-c2/sec_a.md && echo "A 265-524 == generated section"
A 265-524 == generated section
$ head -n 264 $A | cmp - <(head -n 264 $PA) && echo "A 1-264 == pre-edit 1-264"
A 1-264 == pre-edit 1-264
$ tail -n 1 $A | cmp - <(tail -n 1 $PA) && echo "A last line == pre-edit last line"
A last line == pre-edit last line
$ diff -d $PB $B | grep -v '^>'
241a242,487
$ diff -d $PB $B | grep -v '^>' | wc -l
       1
$ diff -d $PB $B | grep -c '^<'
0
$ diff -d $PB $B | grep -c '^>'
246
$ diff $PB $B | grep -v '^>'
240a241,395
241a397,487
$ diff $PB $B | grep -v '^>' | wc -l
       2
$ diff $PB $B | grep -c '^<'
0
$ sed -n 242,487p $B | cmp - /tmp/vrf-c2/sec_b.md && echo "B 242-487 == generated section"
B 242-487 == generated section
$ head -n 241 $B | cmp - <(head -n 241 $PB) && echo "B 1-241 == pre-edit 1-241"
B 1-241 == pre-edit 1-241
$ tail -n 1 $B | cmp - <(tail -n 1 $PB) && echo "B last line == pre-edit last line"
B last line == pre-edit last line
```
Plain `diff` (the default algorithm) splits the same insertion into three add hunks for (a) (`262a263,451`, `263a453,484`, `264a486,524`) and two for (b) (`240a241,395`, `241a397,487`). It does this because it lines up the old trailing code fence and blank lines with identical lines inside the new section. Every one of those hunks is an `a`, and the `^<` count is 0 in both. `diff -d` (minimal) gives the single hunk shown above, and `cmp` confirms that the inserted range is exactly the generated section, so lines before and after it are unchanged.

## Self-check
Run on the final state of all three files. For this report, the block was first produced on a draft with a placeholder of the same line count, then pasted in, then re-run. The re-run output was identical: see the `cmp` block after it.
```
$ echo "len=${#N}"
len=4
$ /tmp/vrf-c2/selfcheck.sh $A $B $R | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[525] last_nonblank_line=525 last_nonblank_is_S13=YES lines=525
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[488] last_nonblank_line=488 last_nonblank_is_S13=YES lines=488
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[452] last_nonblank_line=452 last_nonblank_is_S13=YES lines=452
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ /tmp/vrf-c2/selfcheck.sh $A $B $R | M | wc -l
       4
$ python3 -I /tmp/vrf-c1/s13.py $A $B $R | M
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[525] in_fence=0 last_nonblank_line=525 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[488] in_fence=0 last_nonblank_line=488 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker1.md standalone_outside_fence=1 at=[452] in_fence=0 last_nonblank_line=452 is_last=True substring_lines=1
$ python3 -I /tmp/vrf-c1/s13.py $A $B $R | M | wc -l
       3
$ sed -n 265,524p $A | grep -nE '([0-9]{1,3}\.){3}[0-9]{1,3}'; echo "rc=$?"
rc=1
$ sed -n 242,487p $B | grep -nE '([0-9]{1,3}\.){3}[0-9]{1,3}'; echo "rc=$?"
rc=1
$ grep -nE '([0-9]{1,3}\.){3}[0-9]{1,3}' $R; echo "rc=$?"
rc=1
$ sed -n 265,524p $A | grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; echo "rc=$?"
rc=1
$ sed -n 242,487p $B | grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; echo "rc=$?"
rc=1
$ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $R; echo "rc=$?"
rc=1
$ cat <(sed -n 265,524p $A) <(sed -n 242,487p $B) $R | grep -ciE '([0-9a-f]{2}:){5}[0-9a-f]{2}|id_[r]sa|id_[e]d25519|\.p[e]m\b|\.s[s]h/'
0
```
Re-run against the pasted block above. /tmp/vrf-c2/selfcheck_block.txt is the exact text pasted above, and the generator inserts it verbatim:
```
$ bash /tmp/vrf-c2/selfcheck_cmds.sh | cmp - /tmp/vrf-c2/selfcheck_block.txt && echo identical
identical
```
No IPv4 address, email address, MAC address or key path appears in the inserted lines of (a) and (b) or in this report: every scan above printed no match, so there was no loopback-address or version-number hit to explain.

## Files staged
None. The brief forbids git add. Written in the working tree only: the two insertions above and this report (untracked, new). Helper scripts are in /tmp/vrf-c2/, outside the repo.

## Out-of-scope observations (reported, not fixed)
- (b) :213 has `count.sh <two new reports> | tail -3`, a tail-truncated output, in its second self-check block. The brief did not list it, and it is not corrected here.
- The whole-word search also matches in DECISION_LOG.md (6 lines), HANDOFF.md (3) and MANIFEST.md (2), outside docs/reports/. These counts come from block 3. Whether each match is the name itself was not checked.
- Two gitignored files under ./Redemtion/ match as a substring only, not whole-word. Their paths are masked here (see process log step 3).

## Result: PASS
Every count and set claim listed in the brief was re-run with full output. In (a) and (b), each was corrected append-only in a Correction 2 section, original figure next to re-run figure. The skeleton claims are relabelled UNVERIFIED (not re-runnable), and the staged MANIFEST positions are labelled INFERRED. Both files show only added lines against their pre-edit copies, and the S13 sentence is the single standalone last line in all three files.

## Addendum (worker3, fix pass)
Worker3 of unit 2026-11-11-v-rulings-filing-correction-2 added this section in the fix pass. No existing line of this report was changed (the `diff` against the copy taken before the fix pass is in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md). This section does three things. It defines `R`. It backs process-log steps 1 and 5 with pasted output. It lists which blocks above the revised Correction 2 items in (a) and (b) supersede. The definitions are those at :23-30, plus R. The blocks below were run before this section was inserted, so the `grep` for `^R=` counts lines above this section only.

**R.** The Self-check at :401-439 uses `$R` (at :406-431), and the Definitions block at :23-30 does not define it. The definition is:
```
$ R=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
$ grep -c "^R=" $R
0
$ grep -n '\$R' $R | cut -d: -f1 | tr '\n' ' '; echo
406 411 413 417 423 429 431 
```

**Step 1 (:12).** :12 says that (a) and (b) matched their pre-edit copies (`diff` exit 0), and that the raw name count was 0 in all four files, meaning (a), (b) and their /tmp/c2pre copies. That full-file match described (a) and (b) before the Correction 2 insertion, and it cannot be re-executed now, because both files have been edited since. The block at :307-308 (section 5) holds the `cmp` lines `A identical to pre-edit copy` and `B identical to pre-edit copy`, captured on the unedited files. The re-runnable parts are below. The name count is 0 in all four files. The original body (the first 264 lines and the last line of (a), the first 241 lines and the last line of (b)) is byte-identical to the /tmp/c2pre copies. The full-file `cmp` now differs at the first inserted line (rc=1), as expected:
```
$ for f in $A $B $PA $PB; do echo "$f: $(grep -ci -- "$N" $f)"; done | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: 0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: 0
/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md: 0
/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: 0
$ for f in $A $B $PA $PB; do echo "$f: $(grep -ci -- "$N" $f)"; done | M | wc -l
       4
$ cmp <(head -n 264 $A) <(head -n 264 $PA); echo "cmp first 264 lines (a) vs PA rc=$?"
cmp first 264 lines (a) vs PA rc=0
$ cmp <(tail -n 1 $A) <(tail -n 1 $PA); echo "cmp last line (a) vs PA rc=$?"
cmp last line (a) vs PA rc=0
$ cmp <(head -n 241 $B) <(head -n 241 $PB); echo "cmp first 241 lines (b) vs PB rc=$?"
cmp first 241 lines (b) vs PB rc=0
$ cmp <(tail -n 1 $B) <(tail -n 1 $PB); echo "cmp last line (b) vs PB rc=$?"
cmp last line (b) vs PB rc=0
$ cmp $A $PA; echo "full-file cmp (a) vs PA rc=$?"
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md differ: char 17670, line 265
full-file cmp (a) vs PA rc=1
$ cmp $B $PB; echo "full-file cmp (b) vs PB rc=$?"
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md differ: char 17199, line 242
full-file cmp (b) vs PB rc=1
$ grep -n 'identical to pre-edit copy' $R | grep -v '&&'
307:A identical to pre-edit copy
308:B identical to pre-edit copy
```

**Step 5 (:16), the insert script and its assertions.** The script that did the insertion is /tmp/vrf-c2/insert.py (the S13 sentence is masked as `<S13>` by `S`, defined in /tmp/c2fix/defs.sh as `S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }`). The original run on (a) and (b) cannot be repeated on the files themselves, because they have been edited since. It was re-run on copies of the /tmp/c2pre files in a mktemp directory, with the generated sections /tmp/vrf-c2/sec_a.md and sec_b.md. Both runs pass every assertion (rc=0). The results are byte-identical to (a) and (b) as this report's step 5 left them, which are the copies in /tmp/c2fix/ taken at the start of the fix pass. Three negative controls show that all three assertions are live. A target whose tail is not blank line, S13 line fails with `unexpected tail`. A section that contains the S13 sentence fails the `S not in` assertion and leaves the target unchanged. A section that does not end with one blank line (a one-line file, `x` and a newline) fails `section must end with one blank line` and leaves the target unchanged; that third control was added by worker5 in the second fix pass, in a new mktemp directory:
```
$ cat /tmp/vrf-c2/insert.py | S
import sys
S='<S13>'
target, sec = sys.argv[1], sys.argv[2]
lines = open(target, encoding='utf-8').read().split('\n')
assert lines[-1] == '' and lines[-2] == S and lines[-3] == '', 'unexpected tail'
seclines = open(sec, encoding='utf-8').read().split('\n')
assert seclines[-1] == '' and seclines[-2] == '', 'section must end with one blank line'
seclines = seclines[:-1]  # drop terminal split artefact; keeps the trailing blank line
assert S not in '\n'.join(seclines)
new = lines[:-2] + seclines + lines[-2:]
open(target, 'w', encoding='utf-8').write('\n'.join(new))
print(target, 'inserted', len(seclines), 'lines before final line')
$ cat /tmp/vrf-c2/insert.py | S | wc -l
      12
$ D=$(mktemp -d); cp $PA $PB "$D"/; python3 -I /tmp/vrf-c2/insert.py "$D/${PA##*/}" /tmp/vrf-c2/sec_a.md; echo "rc=$?"; python3 -I /tmp/vrf-c2/insert.py "$D/${PB##*/}" /tmp/vrf-c2/sec_b.md; echo "rc=$?"; cmp "$D/${PA##*/}" /tmp/c2fix/${PA##*/}; echo "cmp vs (a) as left by worker1 rc=$?"; cmp "$D/${PB##*/}" /tmp/c2fix/${PB##*/}; echo "cmp vs (b) as left by worker1 rc=$?"
/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.OkE5X7xMH3/2026-11-11-v-rulings-filing-correction-1-worker1.md inserted 260 lines before final line
rc=0
/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.OkE5X7xMH3/2026-11-11-v-rulings-filing-correction-1-manager.md inserted 246 lines before final line
rc=0
cmp vs (a) as left by worker1 rc=0
cmp vs (b) as left by worker1 rc=0
$ cp /tmp/vrf-c2/sec_a.md "$D/notail.md"; python3 -I /tmp/vrf-c2/insert.py "$D/notail.md" /tmp/vrf-c2/sec_a.md 2>&1 | S; echo "rc=${PIPESTATUS[0]}"
Traceback (most recent call last):
  File "/tmp/vrf-c2/insert.py", line 5, in <module>
    assert lines[-1] == '' and lines[-2] == S and lines[-3] == '', 'unexpected tail'
AssertionError: unexpected tail
rc=1
$ { cat $PA; echo; } > "$D/s13sec.md"; cp $PA "$D/t.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/s13sec.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"
Traceback (most recent call last):
  File "/tmp/vrf-c2/insert.py", line 9, in <module>
    assert S not in '\n'.join(seclines)
AssertionError
rc=1
target unchanged rc=0
$ D=$(mktemp -d); cp $PA "$D/t.md"; printf "x\n" > "$D/noblank.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/noblank.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"
Traceback (most recent call last):
  File "/tmp/vrf-c2/insert.py", line 7, in <module>
    assert seclines[-1] == '' and seclines[-2] == '', 'section must end with one blank line'
AssertionError: section must end with one blank line
rc=1
target unchanged rc=0
$ od -c "$D/noblank.md"
0000000    x  \n                                                        
0000002
```

**Superseded blocks.** Each fenced block in sections 1 to 5 above still appears verbatim in (a) or (b), so the claim at :20 still holds for the blocks this report pastes. But (a) and (b) now hold extra blocks and revised conclusions that are not in this report. Block check and section map:
```
$ python3 -I /tmp/c2fix/blkcheck.py $R 32 322 $A $B
block (c):33-62 lines=30 verbatim_in_a=True verbatim_in_b=False
block (c):66-87 lines=22 verbatim_in_a=True verbatim_in_b=False
block (c):92-105 lines=14 verbatim_in_a=True verbatim_in_b=True
block (c):107-196 lines=90 verbatim_in_a=True verbatim_in_b=True
block (c):198-227 lines=30 verbatim_in_a=True verbatim_in_b=True
block (c):243-299 lines=57 verbatim_in_a=False verbatim_in_b=True
block (c):305-320 lines=16 verbatim_in_a=True verbatim_in_b=True
$ python3 -I /tmp/c2fix/blkcheck.py $R 32 322 $A $B | wc -l
       7
$ grep -n -e '^### ' -e '^## ' $R | M
3:## Task
11:## Process log
19:## Commands and output
32:### 1. (a) section 7 claims: the manager-report skeleton (corrects (a) :207-218)
65:### 2. (a) section 8 helper files and DECISIONS.md (corrects (a) :222-226)
90:### 3. Repo-wide body and filename search (corrects (a) :228-242 and :252, and (b) :228)
242:### 4. MANIFEST positions (corrects (b) :238)
304:### 5. Self-check of (a) and (b) before the edit, and S13 positions (corrects (a) :257-263 and (b) :206-217)
323:### 6. The self-check script (S13 sentence masked as `<S13>` in this output)
350:## Edits made
401:## Self-check
441:## Files staged
444:## Out-of-scope observations (reported, not fixed)
449:## Result: PASS
```

- Section 1 (:32-64). Its block is still in (a) C2.1. The conclusion drawn from it is superseded by the revised (a) C2.1: the skeleton claims at (a) :210, :211, :218 and :250 are no longer UNVERIFIED (not re-runnable), and :209 is no longer only "not re-runnable on the skeleton". (a) :213, :214 and :216 are the three pasted output lines; :212 and :215 are elision markers (five spaces then `...`), not claims. The relabelled claims are now backed by evidence RECOVERED from the session transcript (machine-local, not version-controlled). On that evidence, :209, :210, :211, the pasted lines :213, :214 and :216, the second sentence of :218, and :250 hold. The first sentence of :218 ("All nine sections") is WRONG: there are 8 sections and 8 `(pending)` lines.
- Section 3 (:90-241). Its two ./Redemtion/ rows are masked to the same string. They are supplemented, not replaced, by a new block in (a) C2.3 and (b) C2.1, which numbers them `<gitignored-file-1>` and `<gitignored-file-2>` and shows 2 distinct files. Process-log step 3 (:14) and the third out-of-scope bullet (:447) are supplemented the same way.
- Section 5 (:304-322). Its block is still in (a) C2.5 and (b) C2.3. The label for the S13 positions 210 and 235 at (b) :207 and :217 is superseded by the revised (b) C2.3. The original outputs are RECOVERED from the session transcript, and they match.
- The first out-of-scope bullet (:445, (b) :213 tail-truncated) is now corrected by the new (b) C2.4.
- The Self-check at :401-439 gives (a) 525 lines, S13 at 525, and (b) 488 lines, S13 at 488. That was the state before the fix pass, and it is superseded by the self-check in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md.
- The Result at :449-450 says the skeleton claims were relabelled UNVERIFIED (not re-runnable). That is superseded, as stated for section 1 above.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
