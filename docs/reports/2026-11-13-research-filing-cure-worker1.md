# Unit 2026-11-13-research-filing-cure, worker 1 (ADVERSARIAL)

## Task

Mode: ADVERSARIAL. Grade the cure ordered by DECISION_LOG 2026-11-13T20:25:43Z: in docs/reports/2026-11-13-research-filing-resume-manager.md (:67, :83) and docs/reports/2026-11-13-research-filing-worker2.md (:584, :594) the private name token in a pasted file name is replaced by [rep], one filer's note per report sits above its final S13 line, MANIFEST.md rows :481 and :483 record the redaction, and /tmp/rf-manifest-blob.md is rebuilt. Checks (a) to (h) as given in the brief, each re-run with my own commands. Working directory /Volumes/Sensidine/Praxis.build, branch main, HEAD 661e073. This report is the only file I created or edited.

Name handling: the name is derived into the shell variable N from the 2026-10-28 F4 reply-filing file name and never printed. Every command runs under `bash -c` so that `grep` is /usr/bin/grep (BSD grep 2.6.0), not the zsh ugrep alias. Old (pre-copy) lines are never printed; for diffs only hunk headers, `grep -c '^<'` and `grep '^>'` are shown.

## Checks

### Setup: N derived, length non-zero, HEAD, authority row carries no name

```
cd /Volumes/Sensidine/Praxis.build && bash -c 'N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}"); echo "len=${#N}"; git rev-parse --short HEAD; tail -1 DECISION_LOG.md | grep -c -i "$N"'
```
```
len=4
661e073
0
```
(exit code 1 comes from grep -c reporting 0 matches. The grep binary in use is confirmed under check (f).)

### (a) Redaction

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
for r in resume-manager worker2; do
 f=docs/reports/2026-11-13-research-filing-$r.md
 echo "== $r"
 echo "-- hunk headers"; diff /tmp/rfc-pre/$r.md $f | grep -E "^[0-9]"
 echo "-- count <"; diff /tmp/rfc-pre/$r.md $f | grep -c "^<"
 echo "-- > lines"; diff /tmp/rfc-pre/$r.md $f | grep "^>"
 echo "-- wc pre/cur"; wc -l < /tmp/rfc-pre/$r.md; wc -l < $f
done'
```
```
== resume-manager
-- hunk headers
67c67
83c83
693a694,695
-- count <
2
-- > lines
>  docs/reports/2026-10-28-f4-[rep]-reply-filing.md    |  75 ++++++++++++++-
> SHA2-256(docs/reports/2026-10-28-f4-[rep]-reply-filing.md)= 222b33c2ee2bfc85a367a0691fb5872a08e02db9cf7d62394aaa14d1f13cbc69
> 
> Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :67 and :83 was replaced by [rep] after the output was captured; no other byte of the output changed.
-- wc pre/cur
     695
     697
== worker2
-- hunk headers
584c584
594c594
612a613,614
-- count <
2
-- > lines
> $ cd /Volumes/Sensidine/Praxis.build && TZ=UTC stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%SZ' .claude/settings.json AUDIT_LOG.md DECISIONS.md DECISION_LOG.md DISPATCH_LOG.md HANDOFF.md ISSUE_REGISTER.md MANIFEST.md STATUS.md docs/reports/2026-10-28-f4-[rep]-reply-filing.md docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md scripts/dispatch-log-writeahead.sh /tmp/rf-diffstat-before.txt; date -u +%Y-%m-%dT%H:%M:%SZ
> 2026-11-13T17:37:18Z docs/reports/2026-10-28-f4-[rep]-reply-filing.md
> Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :584 and :594 was replaced by [rep] after the output was captured; no other byte of the output changed.
> 
-- wc pre/cur
     613
     615
```
(The worker2 `>` line at :584 is a file list inside the report as filed; it is shown only because the brief permits `grep '^>'` on diffs, and it carries [rep], not the name.)

Byte proof: apply the same replacement to the pre-copy line in a pipe and cmp with the current line; then whole-file cmp of (pre-copy with the replacement applied on the 4 lines) against (current file with the 2 inserted lines deleted); also the step1 intermediates differ from the pre-copies on exactly the 4 lines.

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
export N
chk(){ r=$1; l=$2; f=docs/reports/2026-11-13-research-filing-$r.md
 printf "%s:%s pre-name-hits(case-insens)=%s exact-case=%s " $r $l "$(sed -n "${l}p" /tmp/rfc-pre/$r.md | grep -o -i -F "$N" | wc -l | tr -d " ")" "$(sed -n "${l}p" /tmp/rfc-pre/$r.md | grep -o -F "$N" | wc -l | tr -d " ")"
 cmp <(sed -n "${l}p" /tmp/rfc-pre/$r.md | perl -pe "s/\Q\$ENV{N}\E/[rep]/gi") <(sed -n "${l}p" $f) && echo "cmp-equal"; }
chk resume-manager 67; chk resume-manager 83; chk worker2 584; chk worker2 594
echo "-- step1 vs pre (edit 1 only)"
for r in resume-manager worker2; do diff /tmp/rfc-pre/$r.md /tmp/rfc-pre/$r.step1.md | grep -E "^[0-9]"; done
echo "-- whole-file: pre with replacement applied on the 4 lines vs current minus note insertion"
cmp <(perl -pe "s/\Q\$ENV{N}\E/[rep]/gi if \$.==67||\$.==83" /tmp/rfc-pre/resume-manager.md) <(sed "694,695d" docs/reports/2026-11-13-research-filing-resume-manager.md) && echo "resume-manager equal"
cmp <(perl -pe "s/\Q\$ENV{N}\E/[rep]/gi if \$.==584||\$.==594" /tmp/rfc-pre/worker2.md) <(sed "613,614d" docs/reports/2026-11-13-research-filing-worker2.md) && echo "worker2 equal"
'
```
```
resume-manager:67 pre-name-hits(case-insens)=1 exact-case=1 cmp-equal
resume-manager:83 pre-name-hits(case-insens)=1 exact-case=1 cmp-equal
worker2:584 pre-name-hits(case-insens)=1 exact-case=1 cmp-equal
worker2:594 pre-name-hits(case-insens)=1 exact-case=1 cmp-equal
-- step1 vs pre (edit 1 only)
67c67
83c83
584c584
594c594
-- whole-file: pre with replacement applied on the 4 lines vs current minus note insertion
resume-manager equal
worker2 equal
```

Each redacted line held exactly one name occurrence, in the case the replacement matched (exact-case=1). The only changes are the 4 one-line `Nc N` hunks plus one 2-line insertion per report. **(a) PASS**

### (b) Filer's notes

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
S="Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
for spec in "resume-manager 67 83" "worker2 584 594"; do set -- $spec; r=$1; a=$2; b=$3
 f=docs/reports/2026-11-13-research-filing-$r.md
 exp="Filer'"'"'s note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person'"'"'s name in a file name inside pasted command output at :$a and :$b was replaced by [rep] after the output was captured; no other byte of the output changed."
 echo "== $r"
 echo "note line(s) (grep -n -x -F expected | cut -d: -f1): $(grep -n -x -F "$exp" $f | cut -d: -f1 | tr "\n" " ")"
 echo "S13 line(s) (grep -n -x -F | cut -d: -f1): $(grep -n -x -F "$S" $f | cut -d: -f1 | tr "\n" " ")"
 echo "total lines: $(wc -l < $f)"
 n=$(wc -l < $f)
 for i in $(seq $((n-5)) $n); do l=$(sed -n "${i}p" $f); printf "%s len=%s head=%q\n" $i ${#l} "${l:0:20}"; done
 echo "-- pre-copy tail shape"
 n=$(wc -l < /tmp/rfc-pre/$r.md)
 for i in $(seq $((n-4)) $n); do l=$(sed -n "${i}p" /tmp/rfc-pre/$r.md); printf "%s len=%s\n" $i ${#l}; done
 printf "last byte: "; tail -c 1 $f | xxd -p
done'
```
```
== resume-manager
note line(s) (grep -n -x -F expected | cut -d: -f1): 695 
S13 line(s) (grep -n -x -F | cut -d: -f1): 697 
total lines:      697
692 len=0 head=''
693 len=345 head=Reason:\ step\ 4\ and\ a
694 len=0 head=''
695 len=260 head=Filer\'s\ note\ \(unit\ 2
696 len=0 head=''
697 len=90 head=Fills\ are\ optimistic
-- pre-copy tail shape
691 len=15
692 len=0
693 len=345
694 len=0
695 len=90
last byte: 0a
== worker2
note line(s) (grep -n -x -F expected | cut -d: -f1): 613 
S13 line(s) (grep -n -x -F | cut -d: -f1): 615 
total lines:      615
610 len=0 head=''
611 len=12 head=Result:\ PASS
612 len=0 head=''
613 len=262 head=Filer\'s\ note\ \(unit\ 2
614 len=0 head=''
615 len=90 head=Fills\ are\ optimistic
-- pre-copy tail shape
609 len=78
610 len=0
611 len=12
612 len=0
613 len=90
last byte: 0a
```

The expected note text, built with the report's own :A :B, matches as a whole line exactly once in each report (grep -x -F). resume-manager: note at **:695**, citing :67 and :83. worker2: note at **:613**, citing :584 and :594. Those are the redacted lines; [rep] line numbers are confirmed under (c). Both pre-copies end with blank line, then the S13 line. Both current files keep that style: note, blank line, then the S13 line as the last line. Neither redacted line moved, since both insertions come after it. **(b) PASS**

### (c) S13

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
S="Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
for r in resume-manager worker2; do f=docs/reports/2026-11-13-research-filing-$r.md
 echo "== $r"
 echo "[rep] line numbers: $(grep -n -F "[rep]" $f | cut -d: -f1 | tr "\n" " ")"
 echo "grep -c -x -F S13: $(grep -c -x -F "$S" $f)"
 echo "grep -c -F S13 (substring, any line): $(grep -c -F "$S" $f)"
 awk -v s="$S" "/^[ \t]*(\`\`\`|~~~)/{inf=!inf; next} \$0==s{ if(inf) inside++; else {outside++; last=NR} } END{printf \"fence-aware: outside=%d inside=%d lastOutsideLine=%d NR=%d fenceOpenAtEOF=%d\n\", outside, inside, last, NR, inf}" $f
done'
```
```
== resume-manager
[rep] line numbers: 67 83 695 
grep -c -x -F S13: 1
grep -c -F S13 (substring, any line): 3
fence-aware: outside=1 inside=0 lastOutsideLine=697 NR=697 fenceOpenAtEOF=0
== worker2
[rep] line numbers: 584 594 613 
grep -c -x -F S13: 1
grep -c -F S13 (substring, any line): 17
fence-aware: outside=1 inside=0 lastOutsideLine=615 NR=615 fenceOpenAtEOF=0
```

In each report the S13 sentence appears exactly once as a standalone line. That line is outside any code fence, no fence is left open at EOF, and the line is the last line (lastOutsideLine = NR). The other substring hits are the sentence embedded inside longer lines, such as pasted commands or quotes. They are not standalone lines, and the pre-copies already had them because the only changes are the ones shown in (a). **(c) PASS**

### (d) MANIFEST

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
echo "name hits pre MANIFEST: $(grep -c -i -F "$N" /tmp/rfc-pre/MANIFEST.md) ; cur MANIFEST: $(grep -c -i -F "$N" MANIFEST.md)"
echo "-- hunk headers"; diff /tmp/rfc-pre/MANIFEST.md MANIFEST.md | grep -E "^[0-9]"
echo "-- count <"; diff /tmp/rfc-pre/MANIFEST.md MANIFEST.md | grep -c "^<"
echo "-- > lines"; diff /tmp/rfc-pre/MANIFEST.md MANIFEST.md | grep "^>"
echo "-- wc pre/cur"; wc -l < /tmp/rfc-pre/MANIFEST.md; wc -l < MANIFEST.md
for spec in "481 resume-manager 67 83 695" "483 worker2 584 594 613"; do set -- $spec
 ins="; a private name in pasted output at :$3 and :$4 replaced by [rep] with a filer'"'"'s note at :$5 (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z)"
 old=$(sed -n "${1}p" /tmp/rfc-pre/MANIFEST.md)
 echo "row $1 mentions $2.md: $(printf %s "$old" | grep -c -F "2026-11-13-research-filing-$2.md")  anchor count in old row: $(printf %s "$old" | grep -o -F "; ungraded at time of row" | wc -l | tr -d " ")"
 exp=$(printf %s "$old" | awk -v ins="$ins" "{i=index(\$0,\"; ungraded at time of row\"); print substr(\$0,1,i-1) ins substr(\$0,i)}")
 cmp <(printf "%s\n" "$exp") <(sed -n "${1}p" MANIFEST.md) && echo "row $1: old row + exact insertion before anchor == current row"
done
echo "-- all other lines identical:"
cmp <(sed "481d;483d" /tmp/rfc-pre/MANIFEST.md) <(sed "481d;483d" MANIFEST.md) && echo "MANIFEST minus 481,483 equal"
'
```
```
name hits pre MANIFEST: 2 ; cur MANIFEST: 2
-- hunk headers
481c481
483c483
-- count <
2
-- > lines
> | /docs/reports/2026-11-13-research-filing-resume-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing-resume (DECISION_LOG 2026-11-13T19:58:43Z), standing as the manager report of unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z) after the power outage: the rebuild of the two lost received copies with sha256 compared to worker 1's pre-copy hashes, diffs of the two Downloads copies against their filed twins, S13 line counts, a PII scan, the MANIFEST row changes and blob cmp checks, the tracked-file diff comparison, and the cold adversary's grades; a private name in pasted output at :67 and :83 replaced by [rep] with a filer's note at :695 (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z); ungraded at time of row |
> | /docs/reports/2026-11-13-research-filing-worker2.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 2 report written by praxis-worker for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): checks (a)-(f) on worker 1's edits to the four return-handoff files, the five MANIFEST rows and the blob, including diffs against the received copies, S13 line counts, a PII scan and a diff-stat comparison; a private name in pasted output at :584 and :594 replaced by [rep] with a filer's note at :613 (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z); ungraded at time of row |
-- wc pre/cur
     483
     483
row 481 mentions resume-manager.md: 1  anchor count in old row: 1
row 481: old row + exact insertion before anchor == current row
row 483 mentions worker2.md: 1  anchor count in old row: 1
row 483: old row + exact insertion before anchor == current row
-- all other lines identical:
MANIFEST minus 481,483 equal
```

Only :481 and :483 changed. Each changed row is exactly the old row with the brief's insertion text placed before its single "; ungraded at time of row" anchor. The :A :B :C values are 67/83/695 and 584/594/613, matching (a) to (c). Every other line is byte-identical. MANIFEST has 2 name hits at lines 335 and 336, the same before and after; see Observation 2. **(d) PASS**

### (e) Blob

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
echo "MANIFEST name-hit line numbers: $(grep -n -i -F "$N" MANIFEST.md | cut -d: -f1 | tr "\n" " ")"
echo "HEAD MANIFEST name hits: $(git show HEAD:MANIFEST.md | grep -c -i -F "$N")"
echo "HEAD MANIFEST lines: $(git show HEAD:MANIFEST.md | wc -l | tr -d " ")"
echo "blob lines: $(wc -l < /tmp/rf-manifest-blob.md | tr -d " ")"
cmp <(head -n 453 /tmp/rf-manifest-blob.md) <(git show HEAD:MANIFEST.md) && echo "blob first 453 == HEAD:MANIFEST.md"
cmp <(head -n 476 MANIFEST.md) <(git show HEAD:MANIFEST.md) ; echo "(info) wt MANIFEST head vs HEAD cmp rc=$?"
echo "sha256 blob tail7: $(tail -n 7 /tmp/rf-manifest-blob.md | shasum -a 256 | cut -c1-64)"
echo "sha256 MANIFEST tail7: $(tail -n 7 MANIFEST.md | shasum -a 256 | cut -c1-64)"
echo "blob sha256: $(shasum -a 256 /tmp/rf-manifest-blob.md | cut -c1-64)"
echo "blob last byte: $(tail -c1 /tmp/rf-manifest-blob.md | xxd -p)"
echo "-- tail7 starts at MANIFEST line $(( $(wc -l < MANIFEST.md) - 6 )); rows 481 and 483 within tail7: $(tail -n 7 MANIFEST.md | grep -c "research-filing-cure")"
'
```
```
MANIFEST name-hit line numbers: 335 336 
HEAD MANIFEST name hits: 2
HEAD MANIFEST lines: 453
blob lines: 460
blob first 453 == HEAD:MANIFEST.md
/dev/fd/63 /dev/fd/62 differ: char 142364, line 307
(info) wt MANIFEST head vs HEAD cmp rc=1
sha256 blob tail7: 89909cd16815325619e82ccfb5f8ee3e856808e74ff82bc530526cc40d4dfb64
sha256 MANIFEST tail7: 89909cd16815325619e82ccfb5f8ee3e856808e74ff82bc530526cc40d4dfb64
blob sha256: 1569e2e474e77166b93c27fbd50bd54a21434a23f5ca3d15e808461a20d9333b
blob last byte: 0a
-- tail7 starts at MANIFEST line 477; rows 481 and 483 within tail7: 2
```

The blob's first 453 lines are byte-equal to HEAD:MANIFEST.md, which is 453 lines. The blob is 460 lines. The last 7 lines of the blob and of MANIFEST.md have the same sha256. Working-tree lines 477 to 483 make up those last 7 lines, and they include both amended rows. Blob sha256 = 1569e2e474e77166b93c27fbd50bd54a21434a23f5ca3d15e808461a20d9333b. The "(info)" line was extra and is not part of the check. It shows that the working-tree MANIFEST differs from HEAD before its tail, at line 307, because of other uncommitted work. That is why the blob is built from HEAD plus the tail, which is the design. **(e) PASS**

### (f) Zero name hits

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
echo "len(N)=${#N}"
for f in docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-research-filing-resume-manager.md docs/reports/2026-11-13-research-filing-worker1.md docs/reports/2026-11-13-research-filing-worker2.md; do
 printf "%s %s\n" "$(grep -c -i "$N" $f)" "$f"; done
printf "%s %s\n" "$(tail -n 7 MANIFEST.md | grep -c -i "$N")" "tail -n 7 MANIFEST.md"
printf "%s %s\n" "$(tail -n 7 /tmp/rf-manifest-blob.md | grep -c -i "$N")" "tail -n 7 /tmp/rf-manifest-blob.md"
echo "-- negative control"
printf "%s %s\n" "$(grep -c -i "$N" /tmp/rfc-pre/resume-manager.md)" "/tmp/rfc-pre/resume-manager.md"
printf "%s %s\n" "$(grep -c -i "$N" /tmp/rfc-pre/worker2.md)" "/tmp/rfc-pre/worker2.md"
echo "pre-copy hit line numbers: rm=$(grep -n -i "$N" /tmp/rfc-pre/resume-manager.md | cut -d: -f1 | tr "\n" " ") w2=$(grep -n -i "$N" /tmp/rfc-pre/worker2.md | cut -d: -f1 | tr "\n" " ")"
echo "-- cure manager report"
ls docs/reports/2026-11-13-research-filing-cure-manager.md >/dev/null 2>&1 && echo exists || echo "does not exist"
printf "%s %s\n" "$(grep -c -i "$N" docs/reports/2026-11-13-research-filing-cure-manager.md 2>&1)" "docs/reports/2026-11-13-research-filing-cure-manager.md"
'
```
```
len(N)=4
0 docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
0 docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
0 docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
0 docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
0 docs/reports/2026-11-13-research-filing-resume-manager.md
0 docs/reports/2026-11-13-research-filing-worker1.md
0 docs/reports/2026-11-13-research-filing-worker2.md
0 tail -n 7 MANIFEST.md
0 tail -n 7 /tmp/rf-manifest-blob.md
-- negative control
2 /tmp/rfc-pre/resume-manager.md
2 /tmp/rfc-pre/worker2.md
pre-copy hit line numbers: rm=67 83  w2=584 594 
-- cure manager report
exists
0 docs/reports/2026-11-13-research-filing-cure-manager.md
```

Extra probes: a binary-safe recount with `-a`, a non-ASCII line count, and a sweep of every docs/reports/2026-11-13-*.md file:

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
type grep; grep --version | head -1
echo "binary-safe recount (grep -a -c -i) of the 7 files + 2 pre-copies:"
for f in docs/reports/2026-11-13-return-handoff-claude-ai-{strategy-research,kimi-research,session-close,vm-queue-results}.md docs/reports/2026-11-13-research-filing-{resume-manager,worker1,worker2}.md /tmp/rfc-pre/resume-manager.md /tmp/rfc-pre/worker2.md; do printf "%s " "$(grep -a -c -i -F "$N" $f)"; done; echo
echo "non-ASCII byte lines in the 7 files: $(cat docs/reports/2026-11-13-return-handoff-claude-ai-{strategy-research,kimi-research,session-close,vm-queue-results}.md docs/reports/2026-11-13-research-filing-{resume-manager,worker1,worker2}.md | LC_ALL=C grep -c "[^ -~	]")"
echo "-- sweep: all docs/reports/2026-11-13-*.md files with nonzero name count (count:file):"
for f in docs/reports/2026-11-13-*.md; do c=$(grep -a -c -i -F "$N" "$f"); [ "$c" != 0 ] && echo "$c:$f"; done; echo "(end sweep)"
'
```
```
grep is /usr/bin/grep
grep (BSD grep, GNU compatible) 2.6.0-FreeBSD
binary-safe recount (grep -a -c -i) of the 7 files + 2 pre-copies:
0 0 0 0 0 0 0 2 2 
non-ASCII byte lines in the 7 files: 99
-- sweep: all docs/reports/2026-11-13-*.md files with nonzero name count (count:file):
1:docs/reports/2026-11-13-open-a2-worker1.md
(end sweep)
```

(The 99 non-ASCII lines are not name hits. The -a recount is binary-safe and still gives 0.)

Follow-up on the sweep hit, with the name masked:

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
f=docs/reports/2026-11-13-open-a2-worker1.md
echo "tracked in HEAD: $(git ls-tree -r --name-only HEAD -- $f | wc -l | tr -d " ")"
echo "HEAD blob name hits: $(git show HEAD:$f 2>/dev/null | grep -c -i -F "$N")"
echo "working-tree differs from HEAD: $(git diff --name-only -- $f | wc -l | tr -d " ")"
echo "hit line number: $(grep -n -i -F "$N" $f | cut -d: -f1)"
echo "introduced by: $(git log --format=%h -1 -- $f)"
echo "hit line, name masked:"; grep -i -F "$N" $f | perl -pe "s/\Q$N\E/[NAME]/gi" | cut -c1-300
'
```
```
tracked in HEAD: 0
HEAD blob name hits: 0
working-tree differs from HEAD: 0
hit line number: 196
introduced by: 
hit line, name masked:
$ grep -nE 'Zarattini|[NAME]' docs/reports/2026-11-13-open-a2-manager.md; echo "exit=$?"
```
(A first try of this command used `-a` together with a word that the gate-commit.sh PreToolUse hook matches, so the hook blocked it before it ran. The command above is the re-run without `-a`.)

All 7 required files, both tails and the cure manager report return 0. The negative control returns 2 on each pre-copy, and the hits are exactly the 4 redacted lines, so the probe works. **(f) PASS**. The sweep hit is outside the 7 files and outside this unit's scope; see Observation 1.

### (g) Unchanged files

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
chk(){ a=$(shasum -a 256 "$1" | cut -c1-64); [ "$a" = "$2" ] && r=MATCH || r=MISMATCH; echo "$a $r $1"; }
chk docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md 6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306
chk docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md 1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3
chk docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md 4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2
chk docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a
chk docs/reports/2026-11-13-research-filing-worker1.md ba25d8e935a9e192eed38911fdcf8f9ed92a4cb664a380eef8ee37b6628a8707
'
```
```
6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306 MATCH docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3 MATCH docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2 MATCH docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a MATCH docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
ba25d8e935a9e192eed38911fdcf8f9ed92a4cb664a380eef8ee37b6628a8707 MATCH docs/reports/2026-11-13-research-filing-worker1.md
```

All 5 match. **(g) PASS**

### (h) Index untouched

```
cd /Volumes/Sensidine/Praxis.build && bash -c '
N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}")
git diff --cached --name-only | wc -l
echo "name hits in the staged path list: $(git diff --cached --name-only | grep -c -i "$N")"
'
```
```
       1
name hits in the staged path list: 1
```

The index holds 1 path, as expected. That one pre-existing staged path has the name token in its file name; see Observation 3. **(h) PASS**

## Defects

none

Observations (outside this unit's edit scope; reported, not fixed, and none of them fails a check):
1. The untracked file docs/reports/2026-11-13-open-a2-worker1.md has the name once, at :196, inside a pasted `grep -nE` pattern. It is not one of the 7 files and not in HEAD. If it is ever filed, it needs the same cure.
2. MANIFEST.md :335 and :336 have the name. They already did in HEAD:MANIFEST.md (2 hits), so the blob's first 453 lines carry it too. Those rows were filed before this unit, and the brief's blob rule (byte-exact HEAD prefix) keeps them unchanged.
3. The main index has one staged path, an evidence PNG from 2026-10-28, and its file name contains the name token. It was staged before this unit, which did not touch it. Any later commit built from that index would carry the name in a path.

## Self-check: name count in this report

```
cd /Volumes/Sensidine/Praxis.build && bash -c 'N=$(basename docs/reports/2026-10-28-f4-*-reply-filing.md | awk -F- "{print \$5}"); grep -c -i "$N" docs/reports/2026-11-13-research-filing-cure-worker1.md'
```
```
0
```
(Exit code 1 means grep matched nothing. I re-ran the count after adding this output, and it was still 0.)

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
