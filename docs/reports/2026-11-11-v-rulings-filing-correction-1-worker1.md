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

## Correction 2 (unit 2026-11-11-v-rulings-filing-correction-2, 2026-11-11)

This section is append-only. No line above it was changed or deleted. The pre-edit copy is /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md, and `diff` of that copy against this file shows one add hunk (pasted in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md). A reference like `:NNN` means a line of this file above this section. The section exists because the audit of unit 2026-11-11-v-rulings-filing-correction-1 failed rubric S1: some count and set claims were not backed by full pasted output.

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

### C2.1 - Corrects :207-218 (section 7, the read of the manager-report skeleton)
Original wording: :209 `name hits: 0`; :210 `      27 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md`; :211 `2026-11-11T14:33:58`; :218 "All nine sections read `(pending)`. Lines 1-14 and 17-26 were elided above, and every one of them is a header, a blank line, or `(pending)`." Only 3 of the 27 output lines were pasted (:213, :214, :216). The C5 finding at :250 rests on the same read.

Re-run:
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
Result of the re-run above. That block was taken in the first correction-2 pass, before (b) was edited in that pass (it shows (b) with 242 lines, the same as the /tmp/c2pre copy), so its figures are first-pass figures, not current ones. At that time the manager report had been rewritten since section 7 was written. It had 242 lines and mtime 2026-11-11T14:40:46, with 8 lines starting `## `, 0 lines equal to `(pending)` and 0 lines containing `PENDING`. It was untracked and not in the index, so git held no earlier copy. Under /tmp and /private/tmp, the only file whose name contained `correction-1-manager` was the /tmp/c2pre copy. That copy has 242 lines and was written at 17:08:51, so it is not the skeleton. At the time of the second fix pass (worker5, block below, run at 2026-11-11T18:07:10 local), (b) has 684 lines and is still untracked and not in the index, and the same `find` returns 2 files: the /tmp/c2fix copy (488 lines, written 17:44:14) and the /tmp/c2pre copy (242 lines, written 17:08:51). Neither has 27 lines, so neither is the skeleton. So there is no copy of the skeleton under /tmp, /private/tmp or in git. That negative covers those three places only. The earlier version of this item stopped there. Its UNVERIFIED (not re-runnable) label covered :210, the two claims at :218, :211 and :250, and it said that :209 could not be re-run on the skeleton (its line references, apart from time-of-day fragments, are :210, :211, :218, :218, :209 and :250; block below). It did not label :213, :214 or :216, which are the three pasted output lines. :212 and :215 are elision markers (five spaces then `...`, block below), not claims. This version replaces that label with the recovered evidence below.

Re-run at the time of the second fix pass (worker5), same definitions:
```
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
       2
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
:40 :46 :33 :58 :08 :51 :210 :33 :58 :211 :218 :218 :209 :250 
$ sed -n "212p;215p" $PA | od -c
0000000                        .   .   .  \n                       .   .
0000020    .  \n                                                        
0000022
$ date "+%Y-%m-%dT%H:%M:%S"
2026-11-11T18:07:10
$ wc -l $B
     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
$ git ls-files -s -- $B | wc -l
       0
$ git ls-tree HEAD -- $B | wc -l
       0
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | M
/private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | wc -l
       2
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | while read f; do wc -l "$f"; stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" "$f"; done | M
     488 /private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:44:14
     242 /private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:08:51
```

**RECOVERED from the session transcript (machine-local, not version-controlled).** The skeleton's content and worker1's read of it are both in the session's subagent transcripts under ~/.claude/projects/. T is the manager's transcript and W is worker1's. These definitions are used in addition to the Method block:
```
T=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl
W=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl
S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }
Fz() { perl -pe 's/^(\s*)\x60\x60\x60/$1<fence>/'; }
```
The two transcript files and their git status come first, then the two extraction scripts. tx.py reads one JSON record per line. It skips records of type `api-request-blob`, which carry no timestamp, and it masks the name and the S13 sentence in everything it prints. rec.py prints only line numbers, booleans and line classes.
```
$ stat -f "%N %z bytes, modified %Sm" $T $W
/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl 440951 bytes, modified Nov 11 14:41:00 2026
/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl 405504 bytes, modified Nov 11 14:39:09 2026
$ git -C "$(dirname $T)" rev-parse --is-inside-work-tree
fatal: not a git repository (or any of the parent directories): .git
$ cat /tmp/c2fix/tx.py | M | S
# usage: python3 -I tx.py <mode> <transcript> [args]; prints masked output only
import json, sys, os
N = os.environ['N'].lower()
S13 = '<S13>'
def mask(s):
    out = []; i = 0; low = s.lower()
    while True:
        j = low.find(N, i)
        if j < 0: out.append(s[i:]); break
        out.append(s[i:j]); out.append('<NAME>'); i = j + len(N)
    return ''.join(out).replace(S13, '<S13>')
mode, path = sys.argv[1], sys.argv[2]
recs = []
with open(path, encoding='utf-8') as fh:
    for ln in fh:
        ln = ln.strip()
        if ln: recs.append(json.loads(ln))
uses = {}; results = {}
for r in recs:
    if r.get('type') not in ('assistant', 'user'): continue  # skip api-request-blob replays (no timestamp)
    m = r.get('message') or {}
    c = m.get('content')
    if not isinstance(c, list): continue
    for b in c:
        if not isinstance(b, dict): continue
        if b.get('type') == 'tool_use': uses[b['id']] = (r.get('timestamp'), b)
        if b.get('type') == 'tool_result':
            t = b.get('content')
            if isinstance(t, list): t = ''.join(x.get('text', '') for x in t if isinstance(x, dict))
            results[b['tool_use_id']] = (r.get('timestamp'), t)
if mode == 'write':
    suf = sys.argv[3]
    hits = [(ts, b) for ts, b in uses.values() if b['name'] == 'Write' and str(b['input'].get('file_path', '')).endswith(suf)]
    print('matching_Write_calls=%d' % len(hits))
    for ts, b in hits:
        c = b['input']['content']; L = c.split('\n')
        nl = c.count('\n')
        print('timestamp=%s tool=%s file_path=%s' % (ts, b['name'], mask(b['input']['file_path'])))
        print('name_count_ci=%d newline_terminated_lines=%d ends_with_newline=%s' % (c.lower().count(N), nl, c.endswith('\n')))
        body = c[:-1].split('\n') if c.endswith('\n') else L
        print('hash_hash_space_lines=%d pending_paren_lines=%d PENDING_containing_lines=%d' % (
            sum(1 for x in body if x.startswith('## ')), sum(1 for x in body if x == '(pending)'), sum(1 for x in body if 'PENDING' in x)))
        for i, x in enumerate(body, 1):
            print('%6d\t%s' % (i, mask(x)))
elif mode == 'bash':
    needle = sys.argv[3]
    hits = sorted((ts, i, b) for i, (ts, b) in uses.items() if b['name'] == 'Bash' and needle in b['input'].get('command', ''))
    print('matching_Bash_calls=%d' % len(hits))
    for ts, i, b in hits:
        rts, t = results.get(i, (None, '<no result>'))
        print('=== tool_use timestamp=%s ; tool_result timestamp=%s' % (ts, rts))
        print('--- command:'); print(mask(b['input']['command']))
        print('--- result:'); print(mask(t if isinstance(t, str) else json.dumps(t)))
if mode == 'ts':
    pre = sys.argv[3]
    hits = sorted((ts, i, b) for i, (ts, b) in uses.items() if str(ts).startswith(pre))
    print('matching_tool_uses=%d' % len(hits))
    for ts, i, b in hits:
        rts, t = results.get(i, (None, '<no result>'))
        print('=== tool_use timestamp=%s tool=%s ; tool_result timestamp=%s' % (ts, b['name'], rts))
        print('--- input:'); print(mask(b['input'].get('command', json.dumps(b['input']))))
        print('--- result:'); print(mask(t if isinstance(t, str) else json.dumps(t)))
if mode == 'grepuse':
    needle = sys.argv[3]
    for ts, i, b in sorted(((ts, i, b) for i, (ts, b) in uses.items()), key=lambda x: str(x[0])):
        if needle in json.dumps(b['input']): print(ts, b['name'], i)
if mode == 'result':
    pre = sys.argv[3]
    hits = sorted((ts, i, b) for i, (ts, b) in uses.items() if str(ts).startswith(pre))
    print('matching_tool_uses=%d' % len(hits))
    for ts, i, b in hits:
        rts, t = results.get(i, (None, '<no result>'))
        print('=== tool_use timestamp=%s tool=%s input_command_chars=%d ; tool_result timestamp=%s' % (ts, b['name'], len(b['input'].get('command', '')), rts))
        print('--- result:'); print(mask(t if isinstance(t, str) else json.dumps(t)))
$ cat /tmp/c2fix/tx.py | M | S | wc -l
      74
$ cat /tmp/c2fix/rec.py | M | S
# usage: python3 -I rec.py <mode> ... ; N in env; prints line numbers, booleans and classes only
import json, sys, os
N = os.environ['N'].lower()
def load(path):
    uses, results = {}, {}
    for ln in open(path, encoding='utf-8'):
        if not ln.strip(): continue
        r = json.loads(ln)
        if r.get('type') not in ('assistant', 'user'): continue
        c = (r.get('message') or {}).get('content')
        if not isinstance(c, list): continue
        for b in c:
            if not isinstance(b, dict): continue
            if b.get('type') == 'tool_use': uses[b['id']] = (r['timestamp'], b)
            if b.get('type') == 'tool_result':
                t = b.get('content')
                if isinstance(t, list): t = ''.join(x.get('text', '') for x in t if isinstance(x, dict))
                results[b['tool_use_id']] = t
    return uses, results
def result_at(path, pre):
    u, r = load(path)
    ids = [i for i, (ts, b) in u.items() if ts.startswith(pre)]
    assert len(ids) == 1, ids
    return r[ids[0]]
def write_content(path, suf):
    u, _ = load(path)
    w = [b['input']['content'] for ts, b in u.values() if b['name'] == 'Write' and b['input'].get('file_path', '').endswith(suf)]
    assert len(w) == 1
    return w[0]
mode = sys.argv[1]
if mode in ('amatch', 'classify'):
    T, W, P = sys.argv[2:5]
    wc = write_content(T, 'v-rulings-filing-correction-1-manager.md')
    body = wc[:-1].split('\n') if wc.endswith('\n') else wc.split('\n')
    rd = result_at(W, '2026-11-11T19:37:00').split('\n')
    pre = open(P, encoding='utf-8').read().split('\n')
    if mode == 'amatch':
        catn = rd[3:3 + len(body)]
        print('read_output_lines=%d write_content_lines=%d' % (len(rd), len(body)))
        print('read_output_cat_n_part_equals_write_content=%s' % ([x.split('\t', 1)[1] if '\t' in x else None for x in catn] == body and [int(x.split('\t', 1)[0]) for x in catn] == list(range(1, len(body) + 1))))
        for n in (209, 210, 211, 213, 214, 216):
            print('original_line_%d_is_an_exact_line_of_recovered_read_output=%s' % (n, pre[n - 1] in rd))
        for n in (212, 215):
            print('original_line_%d_is_an_exact_line_of_recovered_read_output=%s' % (n, pre[n - 1] in rd))
    else:
        for i in list(range(1, 15)) + list(range(17, 27)):
            x = body[i - 1]
            k = 'header(#)' if x.startswith('# ') else 'header(##)' if x.startswith('## ') else 'blank' if x == '' else '(pending)' if x == '(pending)' else 'OTHER'
            print('%d %s' % (i, k))
if mode == 'bmatch':
    T, P = sys.argv[2:4]
    pre = open(P, encoding='utf-8').read().split('\n')
    r1 = result_at(T, '2026-11-11T19:40:29').split('\n')
    r2 = result_at(T, '2026-11-11T19:40:36').split('\n')
    for n in (207, 208, 210, 214, 215, 216, 217):
        print('original_line_%d in_19:40:29_result=%s in_19:40:36_result=%s' % (n, pre[n - 1] in r1, pre[n - 1] in r2))
$ cat /tmp/c2fix/rec.py | M | S | wc -l
      56
```
The manager's Write call that created the skeleton (in T). The counts are computed on the content string. `newline_terminated_lines` is the number of newline characters, and the content ends with one:
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
Worker1's Bash call that produced section 7 (in W), with its full command and full output:
```
$ python3 -I /tmp/c2fix/tx.py ts $W 2026-11-11T19:37:00 | M
matching_tool_uses=1
=== tool_use timestamp=2026-11-11T19:37:00.275Z tool=Bash ; tool_result timestamp=2026-11-11T19:37:00.424Z
--- input:
/bin/bash <<'EOF'
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
f=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
echo "name hits: $(grep -ci -- "$N" $f)"; wc -l $f; stat -f "%Sm" -t '%Y-%m-%dT%H:%M:%S' $f
cat -n $f | sed "s/$N/<NAME>/gI"
EOF
--- result:
name hits: 0
      27 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T14:33:58
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
$ python3 -I /tmp/c2fix/tx.py ts $W 2026-11-11T19:37:00 | M | wc -l
      40
```
Comparisons. `amatch` checks the cat -n part of worker1's output (its lines 4-30) against the Write content. It also tests each original line :209-:216 as an exact line of that output. `classify` labels each of lines 1-14 and 17-26 of the recovered content:
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
Timestamps. This machine's zone, and the conversion of the two recorded UTC timestamps to local time:
```
$ date +%Z%z
EST-0500
$ E=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-11T19:33:58 +%s); echo "epoch=$E"; date -r $E '+%Y-%m-%dT%H:%M:%S %Z'; TZ=America/New_York date -r $E '+%Y-%m-%dT%H:%M:%S %Z'
epoch=1794425638
2026-11-11T14:33:58 EST
2026-11-11T14:33:58 EST
$ E=$(date -j -u -f '%Y-%m-%dT%H:%M:%S' 2026-11-11T19:37:00 +%s); TZ=America/New_York date -r $E '+%Y-%m-%dT%H:%M:%S %Z'
2026-11-11T14:37:00 EST
```
Claim by claim, on the recovered evidence:
- :209 `name hits: 0` HOLDS. It is an exact line of worker1's recovered output (`original_line_209_...=True`), and the Write content's case-insensitive name count is 0 (`name_count_ci=0`). Run on the current file and on the /tmp/c2pre copy, the count is also 0 and 0 (re-run block above).
- :210, 27 lines, HOLDS. It is an exact line of the recovered output. The Write content has 27 newline-terminated lines (`newline_terminated_lines=27`, `ends_with_newline=True`).
- :211 `2026-11-11T14:33:58` HOLDS as recovered output. It is line 3 of worker1's output, printed by `stat` at 19:37:00Z. It is consistent with the recorded Write timestamp: 2026-11-11T19:33:58.402Z is 2026-11-11T14:33:58 EST, and this machine's zone is EST-0500. The file mtime itself is not re-runnable, because the file has since been rewritten.
- :213, :214 and :216 (cat -n lines 15, 16 and 27) HOLD. Each is an exact line of the recovered output, and the recovered content has the same text at its lines 15, 16 and 27. :212 and :215 are elision markers, not output lines, so the `False` for them is expected.
- The first sentence of :218, "All nine sections read `(pending)`.", is **WRONG**. The recovered content has 8 lines starting `## ` and 8 lines equal to `(pending)`, and each `## ` line is followed by a `(pending)` line. The only other header is the line-1 title (`# `), which has no `(pending)` under it. Line 27 reads `Result: PENDING`, not `(pending)`. The correct figure is 8 sections.
- The second sentence of :218 (each of lines 1-14 and 17-26 is a header, a blank line or `(pending)`) HOLDS. The classification lists 24 lines and 0 of them are OTHER. Line 1 is the `# ` title, and the rest are `## ` headers, blank lines and `(pending)` lines.
- :250 (C5 not gradable) HOLDS. Its facts are the mtime 14:33:58, the "Verification evidence (command output)" section reading `(pending)`, and the Result reading `PENDING`. They are line 3 and cat -n lines 15, 16 and 27 of the recovered output. `read_output_cat_n_part_equals_write_content=True` shows that the file worker1 read at 19:37:00Z (14:37:00 EST) had the content the manager wrote at 19:33:58Z.

### C2.2 - Corrects :222-226 (section 8, helper files and DECISIONS.md)
Original wording: :223-225 `/tmp/vrf-c1/count.sh: 0`, `/tmp/vrf-c1/diffs.txt: 0`, `/tmp/vrf-c1/s13.py: 0`; :226 `== DECISIONS.md lines 1-2099 whole-word: 0`. The commands behind these figures were not pasted.

Re-run:
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
Result. The figures are unchanged. Each helper file scores 0 both whole-word (`-ciw`) and as a substring (`-ci`). DECISIONS.md lines 1-2099 score 0 whole-word and as a substring, and the tail from line 2100 scores 0. DECISIONS.md is 2203 lines, the same figure as :40. The original values stand, and their commands and output are now pasted.

### C2.3 - Corrects :228-242 (section 8, repo-wide search)
Original wording: :228 "A repo-wide `grep -rIlwi` found the name in many other files, outside the C1 set. Excerpt of the masked output:"; :229-241 a 10-row excerpt; :240 `... (about 45 files in total; the run was cut off by head -40)`; :242 "The rows still prove that at least 11 report **filenames** in docs/reports/ contain the name." The rows at :238-239 had blank counts because of the bug described at :242.

The search script is below. It counts on the real path and masks only the output. Its second perl substitution masks any path under ./Redemtion/. That directory is gitignored and untracked (first command of the next block). Its file titles are personal and unrelated to this unit, so they are kept out of this report. The script's counts are not affected.
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
Repo-wide body search, whole-word and then substring. Both runs exclude .git and every directory named evidence, and ./docs/reports/evidence is the only directory with that name:
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
Result, original next to re-run:

| claim | original | re-run |
|---|---|---|
| files with a whole-word body match (`grep -rIliw`, excluding .git and evidence) | "about 45" (:240, cut at 40 rows by head) | 43 |
| of those, under .claude/agent-memory/ | 3 rows shown (:230-232) | 3 |
| of those, under docs/reports/ | not stated | 37 |
| of those, elsewhere | not stated | 3 (DECISION_LOG.md, HANDOFF.md, MANIFEST.md) |
| sum of per-file whole-word line counts | not stated | 265 |
| files with a substring match (`grep -rIli`, same exclusions) | not run | 46. It adds 3 files over the whole-word list (two under ./Redemtion/, plus docs/reports/2026-11-04-proof-of-concept-standard.md), and 4 files have a higher count |
| report filenames under docs/reports/ that contain the name (`find -iname`) | "at least 11" (:242) | 11 |
| filenames repo-wide that contain the name (excluding .git and docs/reports/evidence) | not run | 11, the same 11 files |
| counts for the two rows at :238-239 | blank (bug) | `-reply-filing.md` 22 and `-reply-worker1.md` 9 (whole-word) |

The script fixes the blank-count bug from :242: grep now runs on the real path, and the mask is applied afterwards.

### C2.4 - Corrects :252 (Findings, out-of-scope note)
Original wording: "the name still appears in at least 11 report filenames (`docs/reports/2026-10-28-f4-<NAME>-reply-*.md`) and in the body of many other reports."

Re-run: the C2.3 blocks above. Filenames: 11 under docs/reports/, all of the form `2026-10-28-f4-<NAME>-reply-*.md`. The repo-wide run finds the same 11. Body: 37 files under docs/reports/ have a whole-word match. The count of the `2026-10-28-f4-<NAME>-reply` rows in that list is 11, so 26 of the 37 report files are beyond the 11 named files. Outside docs/reports/, there are 3 files under .claude/agent-memory/ and 3 more (DECISION_LOG.md, HANDOFF.md, MANIFEST.md). So "at least 11" becomes 11, and "many other reports" becomes 26 more report files (whole-word), 37 report files in total.

### C2.5 - Corrects :257-263 (self-check)
Original wording: :257 "I ran it on the file as first written, before this block existed, and again after inserting it."; :261 `V1 on own report done`; :262 `S13 lines containing: 1  standalone: 1  last nonblank is S13: 1`. That self-check is older than this correction, and its V1 line printed no count. Fresh run on this file and on the manager report, taken before Correction 2 was added to either one:
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
Result. Both files score 0 on the name count and 0 V1 hit lines, and the V1 positive control hit 1 line. The S13 sentence was on 1 line, standalone once, at the last non-blank line (this file 265, manager report 242). This section moves the S13 line down. The re-run on this file after the insertion is in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md (section Self-check).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
