# 2026-11-11 v-rulings-filing Correction 1 - worker1 (ADVERSARIAL)

## Task
Unit `2026-11-11-v-rulings-filing-correction-1`, ADVERSARIAL mode. I tried to break criteria C1-C5 for the five edited reports docs/reports/2026-11-11-v-rulings-filing-{manager,worker3,worker4,worker5,worker10}.md, comparing each one against its pre-edit copy in /tmp/vrf-c1/. Everything was read-only. The only file I wrote is this report. I made no git index change, no commit, and no memory write.

## Criteria tested
- C1: the support rep's first name appears zero times, case-insensitive, in the 14 scoped files plus `tail -n +2100 DECISIONS.md`. Variants checked: split, URL-encoded, entity-escaped, hex, reversed, base64, and other path separators.
- C2: in each of the five edited files, the only change is the full PNG path replaced by `docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]`. Checked at byte level, with line counts.
- C3: the S13 sentence appears exactly once as a standalone line outside code fences, and it is the last non-blank line.
- C4: the five reports are not staged differently from HEAD (pathspec-restricted check).
- C5: rubric S1 applied to the "Verification evidence (command output)" section of the correction-1 manager report.

## Commands and output (pasted, name masked)

The name is built at runtime only, as `N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')`. Every output below that could contain it was piped through `sed "s/$N/<NAME>/gI"`. In command text, the S13 sentence is shown as `<the S13 sentence>`. In output it is masked as `<S13>` by a sed pass that is part of the command.

### 0. Name variable sanity (length only, never the value)
```
$ echo "matches=$(ls docs/reports/evidence/ | grep -ic '^2026-10-28-mffu-.*-reply\.png$') len=${#N} haslower=..."
matches=1 len=4 haslower=1
```

### 1. C1 plain case-insensitive count per scoped file
```
docs/reports/2026-11-11-v-rulings-filing-manager.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker1.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker2.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker3.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker4.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker5.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker6.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker7.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker8.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker9.md: 0
docs/reports/2026-11-11-v-rulings-filing-worker10.md: 0
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md: 0
vm/replies/20261111T172933Z-python-git-install.md: 0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: 0
tail+2100 DECISIONS.md: 0
DECISIONS.md lines:     2203
```

### 2. C1 variant detectors V1-V6 (same 14 files plus the DECISIONS.md tail written to a mktemp file)
V1 is a perl regex on the lowercase letters of the name, allowing `[^\p{L}\p{N}]{0,3}` between each pair of letters. That catches hyphen, underscore, space, markdown, and zero-width splits. V2 matches each character either literal or as `%XX`. V3 matches each character literal or as `&#NNN;`, `&#xHH;`, `\xHH` or `\u00HH`. V4 is the contiguous hex of the name in lower, upper and original case. V5 is the reversed name. V6 is any `2026?10?28?mffu` fragment with any separator.
```
files=14 + DECISIONS.md tail (     104 lines)
== V1 split: up to 3 non-letter/non-digit chars (any unicode incl. zero-width, space, -, _, markdown) between letters
V1 done
== V2 URL-encoded (each char literal or %XX, mixed)
V2 done
== V3 HTML entity / backslash-x / \u00 escapes
V3 done
== V4 contiguous hex of name
V4 done
== V5 reversed name
V5 done
== V6 any 2026-10-28-mffu- path fragment (generic, any separator)
docs/reports/2026-11-11-v-rulings-filing-manager.md:105:docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
docs/reports/2026-11-11-v-rulings-filing-worker3.md:188: docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
docs/reports/2026-11-11-v-rulings-filing-worker4.md:109:None. I made no index changes, as the brief requires. Written in the working copy only: MANIFEST.md (lines 388-398 appended) and this report. The index already held
docs/reports/2026-11-11-v-rulings-filing-worker5.md:231:docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
docs/reports/2026-11-11-v-rulings-filing-worker10.md:294: docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes
V6 done
```
V1 through V5 printed no HIT line. V6 found only the five placeholder sites. The worker4:109 line was truncated by `cut -c1-220`, and section 4 shows its placeholder.

### 3. C1 base64 detector V7 and positive controls for the detectors
V7 decodes every `[A-Za-z0-9+/_=-]{8,}` token, both standard and URL-safe, at all 4 character shifts, and searches the decoded bytes for the name. The controls are synthetic lines fed on stdin. Nothing was written to disk.
```
== V7 base64 (standard + url-safe, all 4 char shifts) decode of every token >=8 chars
V7 done
== POSITIVE CONTROLS (synthetic lines fed on stdin; expect HIT for each)
split form len=6
V1 control HIT
V1 zero-width control HIT
V2 control HIT
V7 control HIT (prefix len 0)
V7 control HIT (prefix len 1)
V7 control HIT (prefix len 2)
V7 url-safe control HIT
```
The detectors fire on a planted hyphen/underscore split, a zero-width split, `%XX` encoding, base64 of the full PNG path at all three byte alignments, and URL-safe base64. They found nothing in the scoped files.

### 4. C2 byte-level comparison (reverse and forward substitution, cmp, masked diff)
For each file, the command is `perl -0777 -pe 's/\Q$PH\E/$path/g' edited | cmp - orig` and the reverse. Here `$path` is `docs/reports/evidence/2026-10-28-mffu-$N-reply.png`, built at runtime.
```
=== manager
lines edited=195 orig=195  bytes edited=14291 orig=14273
orig: fullpath occurrences=1  name occurrences(ci)=1  placeholder occurrences=0
edit: fullpath occurrences=0  name occurrences(ci)=0  placeholder occurrences=1
REVERSED edited == orig (cmp exit 0)
FORWARD orig->edited == edited (cmp exit 0)
--- diff (masked):
105c105
< docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png
---
> docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
=== worker3
lines edited=277 orig=277  bytes edited=27056 orig=27038
orig: fullpath occurrences=1  name occurrences(ci)=1  placeholder occurrences=0
edit: fullpath occurrences=0  name occurrences(ci)=0  placeholder occurrences=1
REVERSED edited == orig (cmp exit 0)
FORWARD orig->edited == edited (cmp exit 0)
--- diff (masked):
188c188
<  docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
---
>  docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes   (already 'A' in the baseline)
=== worker4
lines edited=113 orig=113  bytes edited=8603 orig=8585
orig: fullpath occurrences=1  name occurrences(ci)=1  placeholder occurrences=0
edit: fullpath occurrences=0  name occurrences(ci)=0  placeholder occurrences=1
REVERSED edited == orig (cmp exit 0)
FORWARD orig->edited == edited (cmp exit 0)
--- diff (masked):
109c109
< None. I made no index changes, as the brief requires. Written in the working copy only: MANIFEST.md (lines 388-398 appended) and this report. The index already held `docs/reports/evidence/2026-10-28
---
> None. I made no index changes, as the brief requires. Written in the working copy only: MANIFEST.md (lines 388-398 appended) and this report. The index already held `docs/reports/evidence/[2026-10-2
=== worker5
lines edited=241 orig=241  bytes edited=19841 orig=19823
orig: fullpath occurrences=1  name occurrences(ci)=1  placeholder occurrences=0
edit: fullpath occurrences=0  name occurrences(ci)=0  placeholder occurrences=1
REVERSED edited == orig (cmp exit 0)
FORWARD orig->edited == edited (cmp exit 0)
--- diff (masked):
231c231
< docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png
---
> docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
=== worker10
lines edited=353 orig=353  bytes edited=26199 orig=26181
orig: fullpath occurrences=1  name occurrences(ci)=1  placeholder occurrences=0
edit: fullpath occurrences=0  name occurrences(ci)=0  placeholder occurrences=1
REVERSED edited == orig (cmp exit 0)
FORWARD orig->edited == edited (cmp exit 0)
--- diff (masked):
294c294
<  docs/reports/evidence/2026-10-28-mffu-<NAME>-reply.png | Bin 0 -> 254350 bytes
---
>  docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld] | Bin 0 -> 254350 bytes
```
Each file grew by 18 bytes. That matches the string lengths: the full path is 52 bytes (22 + 16 + 4 + 10) and the placeholder is 70 bytes (22 + 48).

Mode bits did not change:
```
-rw-r--r-- -rw-r--r--  manager
-rw-r--r-- -rw-r--r--  worker3
-rw-r--r-- -rw-r--r--  worker4
-rw-r--r-- -rw-r--r--  worker5
-rw-r--r-- -rw-r--r--  worker10
```

### 5. C3 S13 line check (perl fence-aware scan; command used `S='<the S13 sentence>'`)
```
docs/reports/2026-11-11-v-rulings-filing-manager.md: standalone-outside-fence=1 (line 195) standalone-inside-fence=0 lines-containing-substring=2 last-nonblank-line=195 last-nonblank-is-S13=YES fence-open-at-EOF=no
  final bytes: 642e0a
  CR count: 0
docs/reports/2026-11-11-v-rulings-filing-worker3.md: standalone-outside-fence=1 (line 277) standalone-inside-fence=0 lines-containing-substring=1 last-nonblank-line=277 last-nonblank-is-S13=YES fence-open-at-EOF=no
  final bytes: 642e0a
  CR count: 0
docs/reports/2026-11-11-v-rulings-filing-worker4.md: standalone-outside-fence=1 (line 113) standalone-inside-fence=0 lines-containing-substring=1 last-nonblank-line=113 last-nonblank-is-S13=YES fence-open-at-EOF=no
  final bytes: 642e0a
  CR count: 0
docs/reports/2026-11-11-v-rulings-filing-worker5.md: standalone-outside-fence=1 (line 241) standalone-inside-fence=0 lines-containing-substring=1 last-nonblank-line=241 last-nonblank-is-S13=YES fence-open-at-EOF=no
  final bytes: 642e0a
  CR count: 0
docs/reports/2026-11-11-v-rulings-filing-worker10.md: standalone-outside-fence=1 (line 353) standalone-inside-fence=0 lines-containing-substring=2 last-nonblank-line=353 last-nonblank-is-S13=YES fence-open-at-EOF=no
  final bytes: 642e0a
  CR count: 0
```
The second substring hits in manager and worker10 (grep -nF output, S13 masked by sed):
```
manager:124:> <S13>
manager:195:<S13>
worker10:239:RH new last two lines: ["Filer's addendum, 2026-11-11: standing limitation line added as house style (S13).", '<S13>', '']
worker10:353:<S13>
== same lines in /tmp pre-edit copies?
manager orig lines: 124 195 
worker10 orig lines: 239 353 
```

### 6. C4 index check (pathspec-restricted only) and per-file index/HEAD state
```
== C4 index check (pathspec-restricted)
exit=0 (empty output above = nothing staged)
== tracked in HEAD? / index vs HEAD per file
manager HEAD=untracked index=none worktree=2b2a82d6ef0bbd24c3a0630368409c89bd3c7638 tmpcopy=5b111e27754b89cfdb46a40255a84e5957db0a4a
worker3 HEAD=untracked index=none worktree=70a3677a8c68469c66e9d51aca656754f7c9f3f9 tmpcopy=80565357c7be099d1fe09006226c438773addfc6
worker4 HEAD=untracked index=none worktree=bdb38ac6cca0b22b55e3adbcfa661f78bcfe5637 tmpcopy=943d610ff03aaffea1ff940032dce42e6538a20e
worker5 HEAD=untracked index=none worktree=0b05cc3754d61cb73fb15f7b29cbf21bafa1fabd tmpcopy=4015f34f80ba9ca2e46ed872388b6fe49cf23877
worker10 HEAD=untracked index=none worktree=5b6a36c4e23a794f8372ac05428f68cad3e197e6 tmpcopy=71c1f5e6b30ae0184bb712298e9322600086cdb2
== mtimes
2026-11-11T14:27:09 /tmp/vrf-c1/2026-11-11-v-rulings-filing-manager.md
2026-11-11T14:34:05 docs/reports/2026-11-11-v-rulings-filing-manager.md
2026-11-11T13:43:18 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker3.md
2026-11-11T14:34:05 docs/reports/2026-11-11-v-rulings-filing-worker3.md
2026-11-11T13:36:12 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker4.md
2026-11-11T14:34:05 docs/reports/2026-11-11-v-rulings-filing-worker4.md
2026-11-11T13:48:57 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker5.md
2026-11-11T14:34:05 docs/reports/2026-11-11-v-rulings-filing-worker5.md
2026-11-11T14:25:15 /tmp/vrf-c1/2026-11-11-v-rulings-filing-worker10.md
2026-11-11T14:34:05 docs/reports/2026-11-11-v-rulings-filing-worker10.md
```
`git ls-tree HEAD -- <path>` and `git ls-files -s -- <path>` returned nothing for all five files. `git hash-object` only computes hashes and does not write to the object store or index without `-w`.

### 7. C5 correction-1 manager report as read (cat -n, masked)
```
name hits: 0
      27 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T14:33:58
     ...
    15	## Verification evidence (command output)
    16	(pending)
     ...
    27	Result: PENDING
```
All nine sections read `(pending)`. Lines 1-14 and 17-26 were elided above, and every one of them is a header, a blank line, or `(pending)`.

### 8. Out-of-scope observations (NOT part of C1's file set; counts only, masked)
```
== out-of-scope observation: /tmp/vrf-c1 helper files
/tmp/vrf-c1/count.sh: 0
/tmp/vrf-c1/diffs.txt: 0
/tmp/vrf-c1/s13.py: 0
== DECISIONS.md lines 1-2099 whole-word: 0
```
A repo-wide `grep -rIlwi` found the name in many other files, outside the C1 set. Excerpt of the masked output:
```
./.claude/agent-memory/praxis-manager/project_stop_gate_newest_file_race.md: 1
./.claude/agent-memory/praxis-manager/project_heredoc_commit_text_denied.md: 1
./.claude/agent-memory/praxis-auditor/audit_evidence_standards.md: 1
./docs/reports/2026-11-10-d9-housekeeping-manager.md: 40
./docs/reports/2026-11-02-r-vn3-1-filing-manager.md: 16
./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md: 17
./docs/reports/2026-11-11-hermes-replies-grading-worker1.md: 14
./docs/reports/2026-11-07-wf-mac-side-maths-manager.md: 13
./docs/reports/2026-10-28-f4-<NAME>-reply-filing.md: 
./docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md: 
... (about 45 files in total; the run was cut off by head -40)
```
The blank counts on the `2026-10-28-f4-<NAME>-reply-*.md` rows come from a bug in my loop: I fed masked filenames back into grep, which then printed "No such file or directory". The rows still prove that at least 11 report **filenames** in docs/reports/ contain the name. I did not check whether a 4-letter whole-word match in the agent-memory files is the name itself or a common English word.

## Findings

- **C1 HOLDS.** I found zero case-insensitive hits in all 14 scoped files and in `tail -n +2100 DECISIONS.md` (section 1). The variant detectors also found nothing: split by any 0-3 non-alphanumeric characters including zero-width, URL-encoded, HTML/hex escapes, contiguous hex, reversed, and base64 standard and URL-safe at every alignment. The detectors were proven live by positive controls on planted inputs (sections 2-3). The only `2026-10-28-mffu` fragments left are the five placeholders.
- **C2 HOLDS.** Reversing the substitution on each edited file gives a byte-identical copy of its /tmp/vrf-c1 version (`cmp` exit 0), and the forward substitution matches too. Line counts are equal. Each file had exactly one full-path occurrence before the edit and one placeholder after it. The +18-byte delta matches the length difference, and mode bits are unchanged (section 4). Limitation: all five files are untracked in HEAD, so the /tmp copies are the only baseline. I cannot independently show that they are the true pre-edit state. Their mtimes (13:36-14:27) are all earlier than the edited files' common mtime of 14:34:05, which fits but proves nothing.
- **C3 HOLDS.** In all five files, the S13 sentence is a standalone line exactly once outside fences, never inside a fence, and it is the last non-blank line. No fence is left open at EOF and there are no CRs (section 5). Note: manager:124 (as a `> ` blockquote) and worker10:239 (inside a quoted Python list) also contain the S13 sentence as a substring. Neither is a standalone line, so the criterion as worded holds. Both lines were also in the pre-edit copies, so this edit did not create them. A stricter reading such as "the sentence appears exactly once" would fail for those two files.
- **C4 HOLDS.** The pathspec-restricted `git diff --cached --name-only` printed nothing. `git ls-tree HEAD` and `git ls-files -s` show all five files as untracked and absent from the index (section 6). Caveat: I could not run a positive control on this command. The only staged path I know of is the evidence image, and listing it is forbidden.
- **C5 NOT GRADABLE (skeleton).** When I read the correction-1 manager report (mtime 14:33:58), its "Verification evidence (command output)" section was `(pending)` and the Result was `PENDING`. As the brief instructs, only C1-C4 are graded.

Out of scope, reported and not fixed: the name still appears in at least 11 report filenames (`docs/reports/2026-10-28-f4-<NAME>-reply-*.md`) and in the body of many other reports. Anyone with the repo can recover it, which makes the "filename withheld" placeholder largely cosmetic outside the C1 file set.

## Result: PASS
C1-C4 HOLD and C5 is a skeleton, not graded. I found no break.

Self-check on this report. I ran it on the file as first written, before this block existed, and again after inserting it.
```
$ grep -ci -- "$N" docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md   (plus V1 split detector and S13 line counts)
grep -ci name: 0
V1 on own report done
S13 lines containing: 1  standalone: 1  last nonblank is S13: 1
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
