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

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
