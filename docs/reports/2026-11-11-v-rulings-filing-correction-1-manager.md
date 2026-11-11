# 2026-11-11 v-rulings-filing Correction 1 - manager report

## Task
Unit `2026-11-11-v-rulings-filing-correction-1`. Authority: master's row DECISION_LOG 2026-11-11T19:32:56Z (decided by master under D-2026-11-08-D D1). This is the correction after audit FAIL 1, check 4, on unit `2026-11-11-v-rulings-filing`. The finding: a support rep's first name appeared 5 times in added lines of the unit's reports, each time as the path of the held-out evidence image under docs/reports/evidence/. Required: zero occurrences. Fix: replace each full path with `docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]` and change nothing else.

The name is built at runtime from the filename and is never printed. Every count below is printed by a script that outputs numbers only. The only places the name could appear in pasted output, the `<` side of each diff, are masked as `<NAME>` by a sed pass in the command, and a count of the name on that masked output is shown as 0.

## Rubric criteria addressed
- S1: "Every claim in a report has pasted command output, not a description of output." Every claim below has its output pasted.
- S7: "Nothing is committed while any audit box is unchecked." No git add and no commit by me or the worker. The index check is pasted below.
- S13: the S13 sentence is the last standalone line of this report. It was checked in the five edited reports and in both new reports.

## Workers dispatched (id, mode, outcome)
| id | mode | outcome | report |
|----|------|---------|--------|
| worker1 (agent ae6bf20091d4176fe) | ADVERSARIAL | PASS. C1-C4 HOLD. C5 not gradable, because this report was still a skeleton when the worker read it. | docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md |

I made the edit myself. It was one python command doing an exact byte-string replacement, which falls under the single-line exception. No BUILD worker was dispatched, so fewer parties ever handled the name.

## Process log
1. I read specs/SPEC_RUBRIC.md S1 (line 124), S6 (line 129), S7 (line 130) and S13 (line 136), then wrote the skeleton of this report.
2. I wrote /tmp/vrf-c1/count.sh. It builds N with the brief's `ls | grep | sed` pipeline and prints only `grep -ci -- "$N"` per file. I ran it before the edit.
3. I printed occurrence counts and the matching lines for the five affected reports, name masked, to confirm that each hit was the exact full path.
4. I copied the five reports to /tmp/vrf-c1/ with `cp -p`. Each copy's sha256 equals its source.
5. I ran the replacement. A python3 -I one-liner reads N from the environment and does `bytes.replace(full_path, neutral_text)` on each file.
6. Checks after the edit: masked diffs, a byte-identity reversal, the counts again, and S13 placement.
7. I dispatched worker1 (ADVERSARIAL). I gave it the artifact and the criteria, and none of my reasoning.
8. I read the worker1 report file in full. Its last line is the S13 sentence, and its own name count is 0 (re-run below).
9. I copied MANIFEST.md to /tmp/vrf-c1/MANIFEST.md.pre, appended two rows, and diffed.
10. Final self-check: name counts over all 14 listed files plus both new reports, S13 placement in both new reports, and the index state.

## Verification evidence (command output)

### Before counts (lines with a match, `grep -ci`)
```
$ /tmp/vrf-c1/count.sh
name-length=4 matching-files=1
1	docs/reports/2026-11-11-v-rulings-filing-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-worker1.md
0	docs/reports/2026-11-11-v-rulings-filing-worker2.md
1	docs/reports/2026-11-11-v-rulings-filing-worker3.md
1	docs/reports/2026-11-11-v-rulings-filing-worker4.md
1	docs/reports/2026-11-11-v-rulings-filing-worker5.md
0	docs/reports/2026-11-11-v-rulings-filing-worker6.md
0	docs/reports/2026-11-11-v-rulings-filing-worker7.md
0	docs/reports/2026-11-11-v-rulings-filing-worker8.md
0	docs/reports/2026-11-11-v-rulings-filing-worker9.md
1	docs/reports/2026-11-11-v-rulings-filing-worker10.md
0	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
0	vm/replies/20261111T172933Z-python-git-install.md
0	DECISIONS.md (tail -n +2100)
```
Occurrence counts (`grep -oi | wc -l`), exact-path counts (`grep -oF "$P"`), and line counts for the five affected reports, before the edit:
```
docs/reports/2026-11-11-v-rulings-filing-manager.md occ=1 exactpath=1 lines=195
docs/reports/2026-11-11-v-rulings-filing-worker3.md occ=1 exactpath=1 lines=277
docs/reports/2026-11-11-v-rulings-filing-worker4.md occ=1 exactpath=1 lines=113
docs/reports/2026-11-11-v-rulings-filing-worker5.md occ=1 exactpath=1 lines=241
docs/reports/2026-11-11-v-rulings-filing-worker10.md occ=1 exactpath=1 lines=353
```

### Backups
```
$ shasum -a 256 /tmp/vrf-c1/*.md <five reports>   (first 16 hex chars)
bc59ca06e3ce82cb /tmp/vrf-c1/2026-11-11-v-rulings-filing-manager.md
8e91bc5132524ae3 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker10.md
39c2710dabf98fb9 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker3.md
d7dc78d0a6be0485 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker4.md
b4f30bf811e2c630 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker5.md
bc59ca06e3ce82cb docs/reports/2026-11-11-v-rulings-filing-manager.md
39c2710dabf98fb9 docs/reports/2026-11-11-v-rulings-filing-worker3.md
d7dc78d0a6be0485 docs/reports/2026-11-11-v-rulings-filing-worker4.md
b4f30bf811e2c630 docs/reports/2026-11-11-v-rulings-filing-worker5.md
8e91bc5132524ae3 docs/reports/2026-11-11-v-rulings-filing-worker10.md
```

### Edit
```
$ export N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') && python3 -I -c '<old=b"docs/reports/evidence/2026-10-28-mffu-"+N+b"-reply.png"; new=b"docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]"; per file: write(b.replace(old,new)); print count>' <five reports>
docs/reports/2026-11-11-v-rulings-filing-manager.md replaced=1
docs/reports/2026-11-11-v-rulings-filing-worker3.md replaced=1
docs/reports/2026-11-11-v-rulings-filing-worker4.md replaced=1
docs/reports/2026-11-11-v-rulings-filing-worker5.md replaced=1
docs/reports/2026-11-11-v-rulings-filing-worker10.md replaced=1
```

### Diffs (`<` side masked; the name count on this masked output was 0)
```
$ for f in ...; do diff /tmp/vrf-c1/$F docs/reports/$F | sed "s/$N/<NAME>/gI"; ...; done | tee /tmp/vrf-c1/diffs.txt | grep -ci -- "$N"
0
$ cat /tmp/vrf-c1/diffs.txt
$ diff /tmp/vrf-c1/2026-11-11-v-rulings-filing-manager.md docs/reports/2026-11-11-v-rulings-filing-manager.md | (name masked as <NAME>)
105c105
< docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png
---
> docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
lines before=195 after=195
$ diff /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker3.md docs/reports/2026-11-11-v-rulings-filing-worker3.md | (name masked as <NAME>)
188c188
<  docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
---
>  docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
lines before=277 after=277
$ diff /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker4.md docs/reports/2026-11-11-v-rulings-filing-worker4.md | (name masked as <NAME>)
109c109
< None. I made no index changes, as the brief requires. Written in the working copy only: MANIFEST.md (lines 388-398 appended) and this report. The index already held `docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png` before I started (`git diff --cached --stat`). That file was not staged by me.
---
> None. I made no index changes, as the brief requires. Written in the working copy only: MANIFEST.md (lines 388-398 appended) and this report. The index already held `docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]` before I started (`git diff --cached --stat`). That file was not staged by me.
lines before=113 after=113
$ diff /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md | (name masked as <NAME>)
231c231
< docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png
---
> docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
lines before=241 after=241
$ diff /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker10.md docs/reports/2026-11-11-v-rulings-filing-worker10.md | (name masked as <NAME>)
294c294
<  docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png | Bin 0 -> 254350 bytes
---
>  docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes
lines before=353 after=353
```

### Byte identity (reversing the substitution reproduces the backup exactly)
```
$ byte-identity check (edited file with neutral text reversed == backup)
2026-11-11-v-rulings-filing-manager.md reversed_equals_backup=True neutral_count=1 bytes_before=14273 bytes_after=14291
2026-11-11-v-rulings-filing-worker3.md reversed_equals_backup=True neutral_count=1 bytes_before=27038 bytes_after=27056
2026-11-11-v-rulings-filing-worker4.md reversed_equals_backup=True neutral_count=1 bytes_before=8585 bytes_after=8603
2026-11-11-v-rulings-filing-worker5.md reversed_equals_backup=True neutral_count=1 bytes_before=19823 bytes_after=19841
2026-11-11-v-rulings-filing-worker10.md reversed_equals_backup=True neutral_count=1 bytes_before=26181 bytes_after=26199
```

### After counts
```
$ /tmp/vrf-c1/count.sh   (after)
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
0	DECISIONS.md (tail -n +2100)
```

### S13 in the five edited reports
```
$ python3 -I /tmp/vrf-c1/s13.py <five edited reports>
2026-11-11-v-rulings-filing-manager.md standalone_outside_fence=1 at=[195] in_fence=0 last_nonblank_line=195 is_last=True substring_lines=2
2026-11-11-v-rulings-filing-worker3.md standalone_outside_fence=1 at=[277] in_fence=0 last_nonblank_line=277 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-worker4.md standalone_outside_fence=1 at=[113] in_fence=0 last_nonblank_line=113 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-worker5.md standalone_outside_fence=1 at=[241] in_fence=0 last_nonblank_line=241 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-worker10.md standalone_outside_fence=1 at=[353] in_fence=0 last_nonblank_line=353 is_last=True substring_lines=2
```
`substring_lines=2` in manager and worker10 means the S13 sentence also appears inside a longer, non-standalone line: manager:124 is a `> ` blockquote, and worker10:239 is a quoted Python list. Worker1 section 5 shows both lines at the same line numbers in the pre-edit /tmp copies. The byte-identity check above shows this edit did not touch them, so they are out of scope for this unit.

### Index state
```
$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md
exit=0 (empty output = none staged)
$ git diff --cached --name-only | wc -l
       1
```
The one staged path is the evidence image. It was already staged at the start of the session (per the master's brief), and its name is not printed here.

### MANIFEST append
```
$ diff /tmp/vrf-c1/MANIFEST.md.pre MANIFEST.md
403a404,405
> | /docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | Report | 3 | 2026-11-11 | Manager report for unit 2026-11-11-v-rulings-filing-correction-1 (after audit FAIL 1, check 4): the evidence-image path in five unit reports replaced with neutral text, before/after name counts, byte-identity and S13 checks; ungraded at time of row |
> | /docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | Report | 3 | 2026-11-11 | ADVERSARIAL worker 1 report for unit 2026-11-11-v-rulings-filing-correction-1: attack on the path replacement in five unit reports (name count with variant detectors, byte identity, S13 placement, index state); ungraded at time of row |
$ wc -l
     403 /tmp/vrf-c1/MANIFEST.md.pre
     405 MANIFEST.md
```

### Final self-check (new reports included)
Run on this report with this section still a placeholder. The re-run after pasting is the last block in this section.
```
$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
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
$ python3 -I /tmp/vrf-c1/s13.py <two new reports>
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l
       0
```
```
$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
0	DECISIONS.md (tail -n +2100)
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
```

## Adversarial findings
Worker1 (ADVERSARIAL) report: docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md. Its results, with its pasted evidence in its sections 1-7:
- C1 HOLDS. The name count is 0 in all 14 files and in the DECISIONS.md tail. Its variant detectors (split, URL-encoded, entity/hex escapes, hex, reversed, base64 at all alignments) found nothing, and each detector fired on a planted positive control.
- C2 HOLDS. `cmp` exit 0 both ways (reverse and forward substitution). Line counts are equal, the +18 bytes per file matches the length difference, and mode bits are unchanged. Limitation it noted: the five files are untracked in HEAD, so the /tmp copies are the only baseline.
- C3 HOLDS. The S13 sentence appears once as a standalone line, as the last non-blank line, with no fence left open and no CRs. It noted the same two pre-existing substring lines as above.
- C4 HOLDS. The pathspec-restricted cached diff is empty, and `git ls-files -s` / `git ls-tree HEAD` show the five files untracked and unstaged.
- C5 was not graded, because this report was still a skeleton when it read it. The section above now holds the evidence.

Out of scope for this unit, for the master to decide. Worker1 section 8 found the name, masked in its output, in at least 11 filenames under docs/reports/ of the form `2026-10-28-f4-<NAME>-reply-*.md`. It also found it in the body of many earlier reports and in three files under .claude/agent-memory/. Worker1 did not confirm whether the agent-memory hits are the name or a common word that happens to match. While those files exist, the "filename withheld" placeholder does not stop anyone with the repo from recovering the name. This unit's hard limits forbid touching those files, so I changed nothing there.

## S6 cross-block check
Not applicable. This unit approves no deviation. It is a text redaction inside five unit reports plus a MANIFEST append, and it touches no block spec, code, hook or setting.

## Files staged
None. No git add, no commit (S7). Written in the working copy only:
- docs/reports/2026-11-11-v-rulings-filing-{manager,worker3,worker4,worker5,worker10}.md: path replacement only, one line each (manager:105, worker3:188, worker4:109, worker5:231, worker10:294).
- docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md (this report, new).
- docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md (worker1, new).
- MANIFEST.md: rows 404 and 405 appended.

Result: PASS

## Correction 2 (unit 2026-11-11-v-rulings-filing-correction-2, 2026-11-11)

This section is append-only. No line above it was changed or deleted. The pre-edit copy is /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md, and `diff` of that copy against this file shows one add hunk (pasted in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md). A reference like `:NNN` means a line of this file above this section. The section exists because the audit of unit 2026-11-11-v-rulings-filing-correction-1 failed rubric S1: some count and set claims were not backed by full pasted output.

Method. All commands were run on 2026-11-11 from the repo root under bash, with these definitions (from /tmp/vrf-c2/lib.sh):
```
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
A=docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
B=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
```
Every output is pasted in full, with no lines removed. When an output is a list, the next command in the block is the same command piped to `wc -l`, so a checker can compare the count. `<NAME>` in output comes from the `M` mask or from the script's own perl mask. Commands show `$N` literally. The S13 sentence does not appear verbatim in this section.

### C2.1 - Corrects :228 (out-of-scope note that cites worker1 section 8)
Original wording: "Worker1 section 8 found the name, masked in its output, in at least 11 filenames under docs/reports/ of the form `2026-10-28-f4-<NAME>-reply-*.md`. It also found it in the body of many earlier reports and in three files under .claude/agent-memory/."

Worker1 section 8 pasted 10 rows plus a described tail. Its own Correction 2 relabels that. Re-run here, so this report stands alone. The search script counts on the real path and masks only the output. Its second perl substitution masks any path under ./Redemtion/. That directory is gitignored and untracked (first command of the second block). Its file titles are personal and unrelated to this unit, so they are kept out of this report.
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
The two ./Redemtion/ rows in the substring `diff` above print as the same masked string. They are two distinct files. Their paths stay withheld. Below, each is numbered in sorted order instead and given its own counts:
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
Result. There are 2 distinct files (`sort -u | wc -l` gives 2). Each has 1 substring match line and 0 whole-word match lines. These are the same counts repogrep.sh prints for its two ./Redemtion/ rows.
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
Result, original next to re-run:

| claim at :228 | original | re-run |
|---|---|---|
| filenames under docs/reports/ of the form `2026-10-28-f4-<NAME>-reply-*.md` | "at least 11" | 11 (`find docs/reports`). The repo-wide `find` gives the same 11 |
| "the body of many earlier reports" | not counted | 37 files under docs/reports/ have a whole-word match, 26 of them beyond the 11 named files. 38 have a substring match |
| "three files under .claude/agent-memory/" | 3 | 3 (whole-word and substring both) |
| files elsewhere | not stated | 3 whole-word (DECISION_LOG.md, HANDOFF.md, MANIFEST.md). 5 substring (those 3 plus two under ./Redemtion/) |
| total files with a body match | not stated | 43 whole-word, 46 substring |

### C2.2 - Corrects :238 (Files staged, the MANIFEST row positions)
Original wording: :238 `- MANIFEST.md: rows 404 and 405 appended.`

Re-run:
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
Result. In the working tree, the two correction-1 rows sit at lines 404 and 405, so :238 is right about working-tree positions as of this run. The working tree is HEAD (379 lines) plus 26 added lines in two hunks, with 0 removed lines. The first hunk is 8 rows at 307-314 (`306a307,314`). The second is 18 rows at 388-405 (`379a388,405`). MANIFEST.md is not staged (0).

**The staged positions will differ.** The master stages MANIFEST as HEAD plus this bead's rows only. Per the brief for this unit, 8 older rows of bead diq stay out. Rows 307-314 are the only other hunk. 2 of those 8 rows contain the text `diq`, and none of the 18 rows at 388-405 do. So it is INFERRED, not observed, that 307-314 are the diq rows. Suppose the staged file is HEAD's 379 lines plus the 18 rows of the second hunk, in their current order. Then the correction-1 manager row would be at 379 + 17 = 396 and the worker1 row at 379 + 18 = 397. **INFERRED** (depends on the master's staging), not observed.

### C2.3 - Corrects :206-217 (stale S13 positions in the final self-check)
Original wording: :207 `2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1`; :217 `2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1`. Both outputs describe earlier, shorter states of this file. Those file states cannot be re-executed. The original outputs are **RECOVERED from the session transcript (machine-local, not version-controlled)**, and they match :207 and :217 (blocks below). T is the manager's transcript. tx.py and rec.py are pasted in full in Correction 2 item C2.1 of docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md. These definitions are used in addition to the Method block:
```
T=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl
W=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl
S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }
Fz() { perl -pe 's/^(\s*)\x60\x60\x60/$1<fence>/'; }
```
`grepuse` lists every tool call in T whose input names this file. `result` prints the output of the 19:40:23 call that wrote the full body of this file. That call's command embeds the whole report text, so only its length is printed. Then come the 19:40:29 and 19:40:36 calls, each with its full command and output, and the line match:
```
$ python3 -I /tmp/c2fix/tx.py grepuse $T correction-1-manager | M
2026-11-11T19:33:58.402Z Write toolu_012x3LDPpiUyBj9Y4ro9BFRB
2026-11-11T19:34:56.576Z Agent toolu_01J8mdETdYdYyUfS6JLwwhLm
2026-11-11T19:39:30.736Z Bash toolu_018d8fQK1CeTH4zjesfRnwfp
2026-11-11T19:40:23.359Z Bash toolu_017G3w23tgBpsj7kmiG5bHyu
2026-11-11T19:40:29.324Z Bash toolu_01AHMAe3BYDF5GcgGr1QES4y
2026-11-11T19:40:36.861Z Bash toolu_01YZKGcW7FakwQtHeFE46cyx
2026-11-11T19:40:46.708Z Bash toolu_01EVaw9EMxSMWHuSDmmMMDdf
$ python3 -I /tmp/c2fix/tx.py grepuse $T correction-1-manager | M | wc -l
       7
$ python3 -I /tmp/c2fix/tx.py result $T 2026-11-11T19:40:23 | M
matching_tool_uses=1
=== tool_use timestamp=2026-11-11T19:40:23.359Z tool=Bash input_command_chars=13334 ; tool_result timestamp=2026-11-11T19:40:23.642Z
--- result:
     210 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
[This command modified 1 file you've previously read: docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md. Call Read before editing.]
$ python3 -I /tmp/c2fix/tx.py result $T 2026-11-11T19:40:23 | M | wc -l
       5
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:29 | M
matching_tool_uses=1
=== tool_use timestamp=2026-11-11T19:40:29.324Z tool=Bash ; tool_result timestamp=2026-11-11T19:40:29.560Z
--- input:
{ echo '$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md'; /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md; echo '$ python3 -I /tmp/vrf-c1/s13.py <two new reports>'; python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-{manager,worker1}.md; echo "\$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l"; git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l; } > /tmp/vrf-c1/selfcheck.txt 2>&1; cat /tmp/vrf-c1/selfcheck.txt
--- result:
$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
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
$ python3 -I /tmp/vrf-c1/s13.py <two new reports>
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l
       0
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:29 | M | wc -l
      28
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:36 | M
matching_tool_uses=1
=== tool_use timestamp=2026-11-11T19:40:36.861Z tool=Bash ; tool_result timestamp=2026-11-11T19:40:37.235Z
--- input:
export SC="$(cat /tmp/vrf-c1/selfcheck.txt)" && python3 -I -c '
import os
f="docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md"
b=open(f,encoding="utf-8").read(); assert b.count("SELFCHECK_PLACEHOLDER")==1
b=b.replace("SELFCHECK_PLACEHOLDER","Run on this report with this section still a placeholder. The re-run after pasting is the last block in this section.\n```\n"+os.environ["SC"]+"\n```")
open(f,"w",encoding="utf-8").write(b)' && /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | tail -3 && python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
--- result:
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
0	DECISIONS.md (tail -n +2100)
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:36 | M | wc -l
      14
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
Result of the recovery. The 19:40:23 call left this file at 210 lines. The 19:40:29 call ran `s13.py` on both new reports. Its output contains :207 exactly (`at=[210]`), and :208 as well. The 19:40:36 call inserted the first self-check block, then ran `count.sh ... | tail -3` and `s13.py` on this file. Its output contains :217 exactly (`at=[235]`). In the `grepuse` list, no tool call naming this file falls between 19:40:23 and 19:40:29, or between 19:40:29 and 19:40:36. So positions 210 and 235 hold for the file states at 19:40:29 and 19:40:36, on RECOVERED evidence.

Re-run, taken before Correction 2 was added to this file:
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
Result. Before this section was added, the S13 line of this file was at 242, the last line of a 242-line file, not at the 210 or 235 that were cited. The worker1 report's position of 265 (cited at :208) still held. This section moves the S13 line again. The position after the insertion is in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md (section Self-check).

### C2.4 - Corrects :206 and :213 (placeholder commands, and a tail-truncated output)
Original wording: :206 `$ python3 -I /tmp/vrf-c1/s13.py <two new reports>`; :213 `$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)`.

Both lines show placeholders (`<two new reports>`, `<this report>`) instead of the arguments that were run. The output at :214-216 is truncated. `| tail -3` keeps only the last 3 lines of count.sh's output, which is 17 lines for two arguments (fresh run below).

Recovered (session transcript, machine-local, not version-controlled). :206 is a line that the 19:40:29 call printed with `echo`. The command that call actually ran is `python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-{manager,worker1}.md` (C2.3 block above). The same call ran `count.sh` on the same two files without `tail`, and that block shows its full output: 17 lines, all counts 0. :213 was printed with `echo` by the 19:40:46 call below. That call stored the output in RR and inserted it into this file. The commands it actually ran were `/tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | tail -3` and `python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md`. The `tail -3` ran at the source, so the full output of that particular run was never printed and cannot be recovered. Its tool_result shows the block as pasted into this file (printed by `sed`), not RR on its own. Output lines that begin with three backticks are shown as `<fence>` by `Fz`, so they do not close this block:
```
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:46 | M | Fz
matching_tool_uses=1
=== tool_use timestamp=2026-11-11T19:40:46.708Z tool=Bash ; tool_result timestamp=2026-11-11T19:40:47.219Z
--- input:
export RR="$(echo '$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)'; /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | tail -3; python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md)" && python3 -I -c '
import os
f="docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md"
b=open(f,encoding="utf-8").read(); anchor="\n\n## Adversarial findings"; assert b.count(anchor)==1
b=b.replace(anchor,"\n```\n"+os.environ["RR"]+"\n```"+anchor)
open(f,"w",encoding="utf-8").write(b)' && N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') && F=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md && echo "final: name-count=$(grep -ci -- "$N" $F) worker1=$(grep -ci -- "$N" docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md) lines=$(wc -l <$F | tr -d ' ')" && python3 -I /tmp/vrf-c1/s13.py $F && grep -n '^Result:' $F && grep -c '^## Verification evidence (command output)$' $F && sed -n '/^### Final self-check/,/^## Adversarial/p' $F | tail -12 && export N && python3 -I -c '
import os
n=os.environ["N"].encode(); old=b"docs/reports/evidence/2026-10-28-mffu-"+n+b"-reply.png"; new=b"docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]"
for s in ["manager","worker3","worker4","worker5","worker10"]:
    f="2026-11-11-v-rulings-filing-%s.md"%s; print(s, open("docs/reports/"+f,"rb").read().replace(new,old)==open("/tmp/vrf-c1/"+f,"rb").read())'; wc -l MANIFEST.md
--- result:
final: name-count=0 worker1=0 lines=242
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[242] in_fence=0 last_nonblank_line=242 is_last=True substring_lines=1
240:Result: PASS
1
$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l
       0
<fence>
<fence>
$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
0	DECISIONS.md (tail -n +2100)
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
<fence>

## Adversarial findings
manager True
worker3 True
worker4 True
worker5 True
worker10 True
     405 MANIFEST.md
[This command modified 1 file you've previously read: docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md. Call Read before editing.]
$ python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T19:40:46 | M | Fz | wc -l
      37
```
The script, then a fresh full run with the real arguments. This run was taken before this item was inserted. The run on the final file is in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:
```
$ cat /tmp/vrf-c1/count.sh | M
#!/bin/bash
# Prints counts only. Never prints the name.
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
echo "name-length=${#N} matching-files=$(ls docs/reports/evidence/ | grep -ci '^2026-10-28-mffu-.*-reply\.png$')"
for f in docs/reports/2026-11-11-v-rulings-filing-manager.md docs/reports/2026-11-11-v-rulings-filing-worker{1,2,3,4,5,6,7,8,9,10}.md docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md vm/replies/20261111T172933Z-python-git-install.md "$@"; do
  printf '%s\t%s\n' "$(grep -ci -- "$N" "$f")" "$f"
done
printf '%s\t%s\n' "$(tail -n +2100 DECISIONS.md | grep -ci -- "$N")" "DECISIONS.md (tail -n +2100)"
$ cat /tmp/vrf-c1/count.sh | M | wc -l
       9
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
Result. :206 and :213 are now backed by their recovered real commands. The fresh `count.sh` run prints 17 lines, and every count in it is 0, including both correction-1 reports and the DECISIONS.md tail. The 3 rows at :214-216 are identical to its last 3 lines.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
