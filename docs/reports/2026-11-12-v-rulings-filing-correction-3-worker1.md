# Unit 2026-11-12-v-rulings-filing-correction-3, worker1 (BUILD)

## Task
Mode BUILD, bead Praxis_build-n1y, repo /Volumes/Sensidine/Praxis.build at HEAD a962475. Two tasks. Nothing was committed or staged. No git ref was touched. Nothing under vm/ or .claude/ was written.
- TASK A. Append a `## Correction 3 (2026-11-12)` section, immediately before the final S13 line, to (M) docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md and (W6) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md. The sections re-run, with literal commands and full output, the flagged lines M:105, M:146, M:153, M:163, M:184, M:204, W6:16 and W6:34.
- TASK B. Two one-line address edits: docs/reports/2026-11-11-v-rulings-filing-worker2.md:169 and docs/reports/2026-11-11-v-rulings-filing-worker5.md:79.

## Criteria
- S1 "Every claim in a report has pasted command output, not a description of output." (specs/SPEC_RUBRIC.md)
- S2 "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S13: the S13 sentence appears once in each file, standalone, as the last line.
- Private data: the support rep's first name appears 0 times. No email address appears in anything written by this unit.

## Commands and output
Every block below is verbatim output. Each `$ ` line is the literal string a bash script passed to `run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }`, run from the repo root. Where a command uses `$N` (the name, built at runtime from the evidence filename and never printed) or `$S13` (the S13 sentence, read from /tmp/vrf-c2/selfcheck.sh), the script defined them as the first block of 3 shows.

### 1. Step 0: pre-edit copies, taken before any edit
Command: `bash -c 'cd /Volumes/Sensidine/Praxis.build && date -u +%Y-%m-%dT%H:%M:%SZ && for f in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md 2026-11-11-v-rulings-filing-worker2.md 2026-11-11-v-rulings-filing-worker5.md; do cp -p docs/reports/$f /tmp/c3pre/$f && cmp docs/reports/$f /tmp/c3pre/$f && echo "identical: $f"; done'`
```
2026-11-12T00:39:57Z
identical: 2026-11-11-v-rulings-filing-correction-2-manager.md
identical: 2026-11-11-v-rulings-filing-correction-2-worker6.md
identical: 2026-11-11-v-rulings-filing-worker2.md
identical: 2026-11-11-v-rulings-filing-worker5.md
```

### 2. Step 1: re-checks on the live files, before any insertion
These outputs were captured to /tmp/c3w1/b*.txt, and were then pasted unchanged into the two Correction 3 sections. Block 3 shows the containment check. They are pasted here as well.

M:105 (/tmp/c3w1/b1_m105.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:44Z
$ wc -l /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
     265 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
     875 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    2066 total
$ shasum -a 256 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
24932bddc8402421df8a3304d9dd5b2875a0eec21f1d8d205735146ac2c12049  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
cc00cc5edd2035b26ad6e0c247de1ffbaf9d08dc2c8fe9be1d864feba6d222ed  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ cmp <(head -n 264 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md) <(head -n 264 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md) && echo a-body-identical; cmp <(head -n 241 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md) <(head -n 241 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md) && echo b-body-identical
a-body-identical
b-body-identical
$ grep -rnE "(^|[^A-Za-z_])P=" /tmp/vrf-c2 /tmp/c2fix /tmp/c2w5 /tmp/c2mgr /tmp/c2pre --include="*.sh" --include="*.py"; echo "grep rc=$?"
grep rc=1
$ P=docs/reports/2026-11-11-v-rulings-filing-; echo "${P}correction-1-worker1.md"; echo "/tmp/c2pre/${P#docs/reports/}correction-1-worker1.md"
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
```
M:146, the definition of `M` (/tmp/c3w1/b11_m146_M.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:44:34Z
$ sed -n 4p /tmp/vrf-c2/lib.sh
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
$ sed -n 136p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
$ /tmp/vrf-c2/selfcheck.sh ${P}correction-1-worker1.md ${P}correction-1-manager.md ${P}correction-2-worker{1,2,3,4,5,6}.md | M
```
M:146 (/tmp/c3w1/b2_m146.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:44Z
$ cat /tmp/vrf-c2/selfcheck.sh | S13="$S13" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'
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
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[875] last_nonblank_line=875 last_nonblank_is_S13=YES lines=875
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[684] last_nonblank_line=684 last_nonblank_is_S13=YES lines=684
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[577] last_nonblank_line=577 last_nonblank_is_S13=YES lines=577
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[987] last_nonblank_line=987 last_nonblank_is_S13=YES lines=987
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[428] last_nonblank_line=428 last_nonblank_is_S13=YES lines=428
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[712] last_nonblank_line=712 last_nonblank_is_S13=YES lines=712
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[370] last_nonblank_line=370 last_nonblank_is_S13=YES lines=370
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[207] last_nonblank_line=207 last_nonblank_is_S13=YES lines=207
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | wc -l
       9
$ diff <(sed -n 137,145p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'); echo "diff rc=$?"
diff rc=0
```
M:153 and M:162 (/tmp/c3w1/b3_m153.txt and /tmp/c3w1/b10_m153_extra.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ cat /tmp/c2mgr/pii.py
import re, sys
pats = {'ipv4_not_loopback': r'\b(?:\d{1,3}\.){3}\d{1,3}\b', 'email': r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', 'mac': r'\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b', 'keypath': r'id_rsa|id_ed25519|\.pem\b|\.ssh/'}
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    out = []
    for k, p in pats.items():
        m = re.findall(p, t)
        if k == 'ipv4_not_loopback': m = [x for x in m if x != '127.0.0.1']
        out.append('%s=%d' % (k, len(m)))
    hits = [(i, l) for i, l in enumerate(t.split('\n'), 1) if re.search(pats['mac'] + '|' + pats['keypath'], l)]
    print(f, ' '.join(out), 'mac_or_key_lines=' + ','.join(str(i) for i, _ in hits))
$ python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md ipv4_not_loopback=0 email=0 mac=0 keypath=4 mac_or_key_lines=909
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md ipv4_not_loopback=0 email=0 mac=0 keypath=2 mac_or_key_lines=347
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md ipv4_not_loopback=0 email=0 mac=0 keypath=12 mac_or_key_lines=159,171,172,173,174,175,198
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
$ diff <(sed -n 154,162p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md); echo "diff rc=$?"
9c9
< docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=0 mac_or_key_lines=
---
> docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
diff rc=1
$ grep -nE "id_rsa|id_ed25519|\.pem\b|\.ssh/" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | cut -d: -f1 | tr "\n" " "; echo
163 168 169 170 171 172 174 
$ grep -oE "id_rsa|id_ed25519|\.pem\b|\.ssh/" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | wc -l
      15
$ grep -n "^### E7\|^### E8" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
151:### E7. Other personal data
176:### E8. Self-check of this report
```
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:43:33Z
$ grep -noE "id_rsa|id_ed25519|\.pem\b|\.ssh/" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
163:.ssh/
163:.ssh/
163:.pem
168:.ssh/
168:.pem
169:.ssh/
170:.pem
171:.ssh/
171:.pem
172:.ssh/
172:.pem
174:.ssh/
174:.pem
174:id_rsa
174:id_ed25519
```
M:163 (/tmp/c3w1/b4_m163.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ sed -n 163p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
$ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <worker2, worker5, worker6 reports>
$ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:0
```
M:184 (/tmp/c3w1/b5_m184.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" .claude/agent-memory/praxis-worker/MEMORY.md
2026-11-11T17:19:58
$ ls -la .claude/agent-memory/praxis-worker/
total 80
drwxr-xr-x@ 8 admin  staff    256 Nov 11 17:19 .
drwxr-xr-x@ 6 admin  staff    192 Jul 26 10:18 ..
-rw-r--r--@ 1 admin  staff   2970 Nov 11 17:19 MEMORY.md
-rw-r--r--@ 1 admin  staff   1806 Jul 26 19:16 feedback_scoped-hedge-vs-universal-negative.md
-rw-r--r--@ 1 admin  staff   5804 Jul 26 19:17 project_agent-type-source.md
-rw-r--r--@ 1 admin  staff  12558 Jul 30 12:46 project_commit-guards-block-scratch-repos.md
-rw-r--r--@ 1 admin  staff   1240 Nov 10 00:29 project_gate-harness-fake-process.md
-rw-r--r--@ 1 admin  staff   1862 Jul 26 18:04 project_s9-positive-control-harness.md
$ grep -oE '\]\([^)]+\)' .claude/agent-memory/praxis-worker/MEMORY.md
](project_s9-positive-control-harness.md)
](project_agent-type-source.md)
](feedback_scoped-hedge-vs-universal-negative.md)
](project_commit-guards-block-scratch-repos.md)
](project_commit-guards-block-scratch-repos.md)
](project_commit-guards-block-scratch-repos.md)
](project_commit-guards-block-scratch-repos.md)
](project_gate-harness-fake-process.md)
$ grep -oE '\]\([^)]+\)' .claude/agent-memory/praxis-worker/MEMORY.md | sed -e "s/^](//" -e "s/)\$//" | sort -u
feedback_scoped-hedge-vs-universal-negative.md
project_agent-type-source.md
project_commit-guards-block-scratch-repos.md
project_gate-harness-fake-process.md
project_s9-positive-control-harness.md
$ for t in project_s9-positive-control-harness.md project_agent-type-source.md feedback_scoped-hedge-vs-universal-negative.md project_commit-guards-block-scratch-repos.md project_gate-harness-fake-process.md; do if test -f ".claude/agent-memory/praxis-worker/$t"; then echo "ok $t"; else echo "missing $t"; fi; done
ok project_s9-positive-control-harness.md
ok project_agent-type-source.md
ok feedback_scoped-hedge-vs-universal-negative.md
ok project_commit-guards-block-scratch-repos.md
ok project_gate-harness-fake-process.md
$ ls .claude/agent-memory/praxis-worker/ | grep -v "^MEMORY\.md\$" | wc -l
       5
$ comm -3 <(ls .claude/agent-memory/praxis-worker/ | grep -v "^MEMORY\.md\$" | sort) <(grep -oE '\]\([^)]+\)' .claude/agent-memory/praxis-worker/MEMORY.md | sed -e "s/^](//" -e "s/)\$//" | sort -u); echo "comm rc=$?"
comm rc=0
$ git check-ignore -v .claude/agent-memory/praxis-worker/MEMORY.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-worker/MEMORY.md
$ sed -n 26p .gitignore
.claude/agent-memory/
$ find .claude -newer /tmp/c2pre/worker2.as-returned.md | wc -l
       1
$ find .claude -newer /tmp/c2pre/worker2.as-returned.md -exec stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" {} \;
2026-11-11T18:24:36 .claude/state/mint-log
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/c2pre/worker2.as-returned.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
2026-11-11T17:43:33 /tmp/c2pre/worker2.as-returned.md
2026-11-11T18:17:51 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
```
M:204 (/tmp/c3w1/b6_m204.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     206 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[206] last_nonblank_line=206 last_nonblank_is_S13=YES lines=206
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
```
W6:16 (/tmp/c3w1/b7_w6_16.txt and /tmp/c3w1/b9_w6_16_extra.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ for f in 2026-11-11-v-rulings-filing-correction-1-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker3.md; do echo "=== $f"; wc -l /tmp/c2w5/$f docs/reports/$f | grep -v total; echo "lt=$(diff /tmp/c2w5/$f docs/reports/$f | grep -c "^<")"; done; wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md; /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
=== 2026-11-11-v-rulings-filing-correction-1-worker1.md
     845 /tmp/c2w5/2026-11-11-v-rulings-filing-correction-1-worker1.md
     875 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
lt=1
=== 2026-11-11-v-rulings-filing-correction-2-worker1.md
     567 /tmp/c2w5/2026-11-11-v-rulings-filing-correction-2-worker1.md
     577 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
lt=2
=== 2026-11-11-v-rulings-filing-correction-2-worker3.md
     323 /tmp/c2w5/2026-11-11-v-rulings-filing-correction-2-worker3.md
     428 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
lt=0
     370 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[207] last_nonblank_line=207 last_nonblank_is_S13=YES lines=207
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ wc -l /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
     408 /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md
     358 /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md
     428 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
     370 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
    1564 total
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
2026-11-11T18:15:13 /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md
2026-11-11T18:15:13 /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md
2026-11-11T18:15:13 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
2026-11-11T18:15:13 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
2026-11-11T18:14:52 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
$ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'
405a406,424
> ```
> 
> ## Manager note (correction-2 manager, after the worker 6 check)
> Worker 6 (docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md, Finding 3) found that the Erratum above describes the qcheck.py pattern without pasting the script. The script, in full:
> ```
> $ cat -n /tmp/c2fix/qcheck.py
>      1	# usage: python3 -I qcheck.py ; compares each quoted span in a Correction 2 "Original wording:" line with line N of the /tmp/c2pre copy
>      2	import re
>      3	F = {'a': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md', 264),
>      4	     'b': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md', 241)}
>      5	for k, (cur, pre, body) in F.items():
>      6	    c = open(cur, encoding='utf-8').read().split('\n'); p = open(pre, encoding='utf-8').read().split('\n')
>      7	    for i, line in enumerate(c[body:], body + 1):
>      8	        if not line.startswith('Original wording:'): continue
>      9	        for m in re.finditer(r':(\d+) (`[^`]*(?:`[^`]*)*?`|"[^"]*(?:`[^`]*`[^"]*)*")(?=[;.]|$| Only| The)', line):
>     10	            n, q = int(m.group(1)), m.group(2)[1:-1]
>     11	            print('(%s):%d quotes :%d  equal_to_pre_line=%s  substring_of_pre_line=%s' % (k, i, n, q == p[n - 1], q in p[n - 1]))
> $ cat /tmp/c2fix/qcheck.py | wc -l
>       11
406a426
> Line 9 holds the pattern `:(\d+) (`. It requires a space right after the line number, so a range reference such as `:223-225` is not matched.
$ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md | grep -c "^<"
0
$ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'
356a357,368
> 
> ## Manager note (correction-2 manager, after the worker 6 check)
> Worker 6 (docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md, Findings 1, 2 and 4) found that the Self-check values above are stale and that `$C`, `$D3` and `$W5` are not defined in the files named at :4. The definitions come from /tmp/c2w5/verify.sh:
> ```
> $ grep -nE "^(C|D3|W5)=" /tmp/c2w5/verify.sh
> 3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
> 4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
> 5:W5=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
> $ grep -nE "^(C|D3|W5)=" /tmp/c2w5/verify.sh | wc -l
>        3
> ```
> The `lines=`, `at=` and `last_nonblank_line=` values for this report in the Self-check block above were taken before that block and this note were added, so they are stale. The key-path count of 0 for this report is also stale: the grep now matches its own pattern text, pasted in this report. The current values for this report come from a re-run after this note was inserted, and they are in docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md, Verification evidence.
$ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md | grep -c "^<"
0
```
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:43:33Z
$ diff -d /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md | grep -v "^>"
407a408,427
$ diff -d /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md | grep -v "^>"
357a358,369
$ diff /tmp/c2w5/2026-11-11-v-rulings-filing-correction-2-worker3.md /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md | grep "^[0-9]"; diff /tmp/c2w5/2026-11-11-v-rulings-filing-correction-2-worker3.md /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md | grep -c "^<"
322a323,407
0
$ grep -c "^## Manager note" /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
/tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md:0
/tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:1
$ grep -n "^## Manager note" docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:408:## Manager note (correction-2 manager, after the worker 6 check)
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:358:## Manager note (correction-2 manager, after the worker 6 check)
```
W6:34 (/tmp/c3w1/b8_w6_34.txt):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:42:45Z
$ wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     207 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[207] last_nonblank_line=207 last_nonblank_is_S13=YES lines=207
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
11:- Name: the support rep's first name appears 0 times in (a), (c), (d), (e) and this report. PII: no IPv4 other than 127.0.0.1, no MAC, no key path, no email.
34:The self-check line for this report was taken before this edit. The edit adds lines, so `at=`, `last_nonblank_line=` and `lines=` for this report are stale by the number of lines added. The name count stays 0 because the edit adds no name. The only IPv4, MAC or email hit in this report is the 127.0.0.1 in the Criteria section.
$ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | wc -l
       2
$ grep -nE '\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
$ grep -nE '\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | wc -l
       0
$ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
$ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | wc -l
       0
$ python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md ipv4_not_loopback=0 email=0 mac=0 keypath=12 mac_or_key_lines=159,171,172,173,174,175,198
```
Facts that did NOT reproduce (the output is in the blocks above):
- M:162. It gives `keypath=0` for M. The re-run gives `keypath=15` at lines 163, 168-172 and 174, all inside E7, and every hit is a bare pattern token. Marked WRONG.
- M:164-166. The counts 0, 0 and 0 reproduce. The `<filename>: 0` format is not what `grep -c` prints with several paths (`<path>:<count>`). Marked WRONG as a paste.
- M:184, the statement ".claude/ unchanged since worker2 returned". The count is now 1 (.claude/state/mint-log, 2026-11-11T18:24:36, later than M's mtime 18:17:51). It no longer holds. The current output is consistent with 0 at the time E5 ran, but it cannot prove that.
- W6:28, :30 and :31. They are not current. (d) is now 428 lines (was 408), (e) is 370 (was 358), and W6's self-check gives 207 (was 205). The /tmp/c2mgr copies are 408 and 358 lines, and `diff -d` gives `407a408,427` and `357a358,369` (the manager notes, 0 `<` lines).
- W6:34, the IPv4 part. The scan matches 2 lines (:11 and :34, both 127.0.0.1), not 1. Marked WRONG.
Everything else reproduces: M:105 (both cmp identical, and `$P` INFERRED as `docs/reports/2026-11-11-v-rulings-filing-`, not defined in any saved script), M:146 (9 lines, diff rc=0 against M:137-145), M:153 lines 154-161, M:184's mtime, links, 5 files, no orphan and .gitignore:26 (restoration stays UNVERIFIED), M:204 (unjoined values equal), W6:16 rows (a) and (c), W6:34's stale-field statement and its MAC and email counts of 0.

### 3. Step 2: insertion, and the containment check
Command: `bash -c 'cd /Volumes/Sensidine/Praxis.build && date -u +%Y-%m-%dT%H:%M:%SZ && python3 -I /tmp/c3w1/insert.py docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md /tmp/c3w1/secM.md.tmpl && python3 -I /tmp/c3w1/insert.py docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md /tmp/c3w1/secW6.md.tmpl && wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md'`
```
2026-11-12T00:45:37Z
inserted 258 lines before final line of docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
inserted 159 lines before final line of docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     464 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     366 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     830 total
```
(This output was not tee'd to a file when it ran. It is transcribed here from the tool output of that run, unchanged, as /tmp/c3w1/insert_run.txt.)
The script that ran first in step1.sh, step1b.sh and step1c.sh (this block is also each section's preamble):
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:44:34Z
$ sed -n 3,7p /tmp/c3w1/step1.sh
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
S13=$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)
export N S13
run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
$ sed -n 2,5p /tmp/c3w1/step1b.sh
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
export N
run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
$ sed -n 2,3p /tmp/c3w1/step1c.sh
cd /Volumes/Sensidine/Praxis.build || exit 1
run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
```
Containment check (each Step 1 output file appears verbatim, fenced, in the section it belongs to) and the key-path tokens the M section adds:
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:47:35Z
$ cat /tmp/c3w1/contain.py
# usage: python3 -I contain.py ; prints whether each captured output file appears verbatim, fenced, in M or W6
R = '/Volumes/Sensidine/Praxis.build/docs/reports/'
M = open(R + '2026-11-11-v-rulings-filing-correction-2-manager.md', encoding='utf-8').read()
W = open(R + '2026-11-11-v-rulings-filing-correction-2-worker6.md', encoding='utf-8').read()
for b, where in [('b0_preamble', 'MW'), ('b1_m105', 'M'), ('b11_m146_M', 'M'), ('b2_m146', 'M'), ('b3_m153', 'M'), ('b10_m153_extra', 'M'), ('b4_m163', 'M'), ('b5_m184', 'M'), ('b6_m204', 'M'), ('b7_w6_16', 'W'), ('b9_w6_16_extra', 'W'), ('b8_w6_34', 'W')]:
    s = '```\n' + open('/tmp/c3w1/%s.txt' % b, encoding='utf-8').read() + '```\n'
    print(b, 'in_M=%s' % (s in M), 'in_W6=%s' % (s in W), 'expected=%s' % where)
$ python3 -I /tmp/c3w1/contain.py
b0_preamble in_M=True in_W6=True expected=MW
b1_m105 in_M=True in_W6=False expected=M
b11_m146_M in_M=True in_W6=False expected=M
b2_m146 in_M=True in_W6=False expected=M
b3_m153 in_M=True in_W6=False expected=M
b10_m153_extra in_M=True in_W6=False expected=M
b4_m163 in_M=True in_W6=False expected=M
b5_m184 in_M=True in_W6=False expected=M
b6_m204 in_M=True in_W6=False expected=M
b7_w6_16 in_M=False in_W6=True expected=W
b9_w6_16_extra in_M=False in_W6=True expected=W
b8_w6_34 in_M=False in_W6=True expected=W
$ sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -oE "id_rsa|id_ed25519|\.pem\b|\.ssh/" | sort | uniq -c
  13 .pem
  16 .ssh/
   6 id_ed25519
   6 id_rsa
$ sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -oE "id_rsa|id_ed25519|\.pem\b|\.ssh/" | wc -l
      41
$ sed -n 207,365p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE "id_rsa|id_ed25519|\.pem\b|\.ssh/"
0
```

### 4. Step 3: append-only proof for M and W6
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:46:37Z
$ cmp /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md; echo "cmp rc=$?"
/tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md differ: char 19105, line 206
cmp rc=1
$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md
     464 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     207 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
     366 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
    1243 total
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -v "^>"
204a205,368
205a370,463
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c "^<"
0
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c "^>"
258
$ cmp <(head -n 205 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md) <(head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) && echo M-first205-identical
M-first205-identical
$ cmp <(tail -n 1 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md) <(tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) && echo M-lastline-identical
M-lastline-identical
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v "^>"
206a207,365
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c "^<"
0
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c "^>"
159
$ cmp <(head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo W6-first206-identical
W6-first206-identical
$ cmp <(tail -n 1 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo W6-lastline-identical
W6-lastline-identical
$ grep -n "^## Correction 3 (2026-11-12)\$" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:206:## Correction 3 (2026-11-12)
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:207:## Correction 3 (2026-11-12)
$ diff <(sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep "^\$ " | grep -v "^\$ date") <(cat /tmp/c3w1/b0_preamble.txt /tmp/c3w1/b1_m105.txt /tmp/c3w1/b11_m146_M.txt /tmp/c3w1/b2_m146.txt /tmp/c3w1/b3_m153.txt /tmp/c3w1/b10_m153_extra.txt /tmp/c3w1/b4_m163.txt /tmp/c3w1/b5_m184.txt /tmp/c3w1/b6_m204.txt | grep "^\$ " | grep -v "^\$ date"); echo "M commands vs captured rc=$?"
M commands vs captured rc=0
$ grep -cE "\.\.\.|<[a-z][a-z ,0-9-]*>" <(sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep "^\$ ")
1
$ grep -cE "\.\.\.|<[a-z][a-z ,0-9-]*>" <(sed -n 207,365p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep "^\$ ")
0
```
(This is lines 1-41 of /tmp/c3w1/v_taskA.txt. Its last command, lines 42-44, searched the two sections for the three words this unit must not write, and its pattern spelled them out. It is omitted here so that this report does not contain them. The same check, with the pattern built at runtime, is in block 7 and covers both sections and this report.)
The plain `diff` splits the M insertion into two hunks (`204a205,368` and `205a370,463`) because the original blank line 205 lines up with an inserted blank line (369). `diff -d` gives one hunk:
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:47:02Z
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -v "^>"
205a206,463
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -c "^>"
258
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v "^>"
206a207,365
$ sed -n 205p /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md | od -c; sed -n 369p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | od -c
0000000   \n                                                            
0000001
0000000   \n                                                            
0000001
$ grep -nE "\.\.\.|<[a-z][a-z ,0-9-]*>" <(sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) | grep -E "^[0-9]+:\$ " | cut -c1-60
$ grep -onE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:320:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:11:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:34:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:334:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:345:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:346:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:361:127.0.0.1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:361:127.0.0.1
```
Result: M has one hunk, `205a206,463` (258 `>` lines, 0 `<`). Lines 1-205 are identical, and the last line is identical to the original last line. W6 has one hunk, `206a207,365` (159 `>` lines, 0 `<`). Lines 1-206 are identical, and the last line is identical. The one `$ `-prefixed line in the M section that matches `...` or a `<word>` placeholder is section line 171 (file line 376). It is output, not a command: the output of `sed -n 163p` (file line 375) quoting the original line 163:
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:47:08Z
$ sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -n "^\$ " | grep -E "\.\.\.|<[a-z][a-z ,0-9-]*>" | cut -c1-80
171:$ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <wo
$ grep -n "^\$ sed -n 163p" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
375:$ sed -n 163p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
```

### 5. TASK B: the two address edits
Edit command: `bash -c 'cd /Volumes/Sensidine/Praxis.build && date -u +%Y-%m-%dT%H:%M:%SZ && python3 -I /tmp/c3w1/addr.py'`. The script asserts exactly one email-regex match on the line, the expected delimiters on both sides of it, and the expected line prefix. It then replaces only that span and never prints the address. Its source:
```
$ cat /tmp/c3w1/addr.py
import re, sys
# usage: python3 -I addr.py ; replaces the one email address on each target line; never prints it
EM = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
jobs = [('docs/reports/2026-11-11-v-rulings-filing-worker2.md', 169, '`', '`', "MFFU's public support address", '3. `'),
        ('docs/reports/2026-11-11-v-rulings-filing-worker5.md', 79, '(', ')', 'noreply address withheld', 'Co-Authored-By: Claude Opus 5.5 (')]
for path, ln, lq, rq, repl, prefix in jobs:
    data = open(path, 'rb').read()
    lines = data.split(b'\n')
    line = lines[ln - 1].decode('utf-8')
    ms = list(EM.finditer(line))
    assert len(ms) == 1, '%s:%d expected 1 match, got %d' % (path, ln, len(ms))
    m = ms[0]
    assert line[m.start() - 1] == lq and line[m.end()] == rq, 'delimiters'
    assert line.startswith(prefix), 'prefix'
    total = sum(len(EM.findall(l.decode('utf-8'))) for l in lines)
    new = line[:m.start()] + repl + line[m.end():]
    lines[ln - 1] = new.encode('utf-8')
    open(path, 'wb').write(b'\n'.join(lines))
    print('%s:%d replaced span %d-%d (len %d) ; file email matches before=%d' % (path, ln, m.start(), m.end(), m.end() - m.start(), total))
```
Its output:
```
2026-11-12T00:46:03Z
docs/reports/2026-11-11-v-rulings-filing-worker2.md:169 replaced span 4-31 (len 27) ; file email matches before=1
docs/reports/2026-11-11-v-rulings-filing-worker5.md:79 replaced span 33-54 (len 21) ; file email matches before=1
```
Proof. The `<` side is masked with `(address withheld)`, so the address itself is not shown:
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:46:37Z
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g' | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
169c169
< 3. `(address withheld)` (A:114, 132). This is a public company address. Kept.
---
> 3. `MFFU's public support address` (A:114, 132). This is a public company address. Kept.
$ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g' | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
79c79
< Co-Authored-By: Claude Opus 5.5 ((address withheld))
---
> Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
$ cmp <(sed 169d /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md) <(sed 169d docs/reports/2026-11-11-v-rulings-filing-worker2.md) && echo worker2-other-lines-identical
worker2-other-lines-identical
$ cmp <(sed 79d /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md) <(sed 79d docs/reports/2026-11-11-v-rulings-filing-worker5.md) && echo worker5-other-lines-identical
worker5-other-lines-identical
$ wc -c /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
   11554 /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md
   11556 docs/reports/2026-11-11-v-rulings-filing-worker2.md
   19841 /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md
   19844 docs/reports/2026-11-11-v-rulings-filing-worker5.md
   62795 total
$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
     179 /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md
     179 docs/reports/2026-11-11-v-rulings-filing-worker2.md
     241 /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md
     241 docs/reports/2026-11-11-v-rulings-filing-worker5.md
     840 total
$ for f in /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md; do echo "$f email_lines=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f) email_matches=$(grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f | wc -l | tr -d " ")"; done
/tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md email_lines=1 email_matches=1
docs/reports/2026-11-11-v-rulings-filing-worker2.md email_lines=0 email_matches=0
/tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md email_lines=1 email_matches=1
docs/reports/2026-11-11-v-rulings-filing-worker5.md email_lines=0 email_matches=0
$ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | cut -d: -f1,2
/tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md:169
/tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md:79
$ sed -n 169p docs/reports/2026-11-11-v-rulings-filing-worker2.md; sed -n 79p docs/reports/2026-11-11-v-rulings-filing-worker5.md
3. `MFFU's public support address` (A:114, 132). This is a public company address. Kept.
Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[241] last_nonblank_line=241 last_nonblank_is_S13=YES lines=241
V1 positive control (hyphen-split synthetic line): HIT_lines=1
```
Result: the two `sed -n` lines above show the new text of worker2 :169 and worker5 :79. Every other line is byte-identical (the `sed Nd` cmp prints identical). The line counts are unchanged, at 179 and 241. The byte counts went from 11554 to 11556 and from 19841 to 19844. The email-regex count went from 1 to 0 in each file. The worker2 report's `S13_containing=3` is a pre-existing condition and was not touched by this edit (all lines other than :169 are identical). It is reported here and was not fixed.

### 6. Final checks on M and W6 after insertion, and the index check
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:46:38Z
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[464] last_nonblank_line=464 last_nonblank_is_S13=YES lines=464
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[366] last_nonblank_line=366 last_nonblank_is_S13=YES lines=366
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=56 mac_or_key_lines=163,168,169,170,171,172,174,314,340,342,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,368,376,377
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md ipv4_not_loopback=0 email=0 mac=0 keypath=12 mac_or_key_lines=159,171,172,173,174,175,198
$ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -d: -f1,2
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:320
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:11
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:34
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:334
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:345
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:346
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:361
$ git diff --cached --name-only -- docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | wc -l
       0
$ git rev-parse HEAD
a962475b631f1a21b307fd3c51fe42de1f9a68cd
```
The M key-path count rose from 15 to 56. The 41 new tokens are all inside the Correction 3 section (block 3: 41 tokens in M:206-463), from the pasted pii.py source and grep patterns. The W6 section adds 0 key-path lines (block 3). The new IPv4 lines in W6 (:334, :345, :346, :361) and M:320 are all 127.0.0.1, as the last command of the second block in block 4 shows.
`ipv4_not_loopback=0` and `email=0` in both files. Nothing is staged for the five paths (0), and HEAD is still a962475.

## Files changed
- docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: 206 to 464 lines. Lines 206-463 inserted (Correction 3). The S13 sentence moved from :206 to :464.
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: 207 to 366 lines. Lines 207-365 inserted (Correction 3). The S13 sentence moved from :207 to :366.
- docs/reports/2026-11-11-v-rulings-filing-worker2.md: 179 lines before and after. Line 169 address span replaced.
- docs/reports/2026-11-11-v-rulings-filing-worker5.md: 241 lines before and after. Line 79 address span replaced.
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: this report, new.
- Outside the repo: /tmp/c3pre (pre-edit copies) and /tmp/c3w1 (scripts and captured outputs).
Nothing is staged (block 6). MANIFEST.md was not edited, because the brief limits this unit to the four files plus this report. A MANIFEST row for this report is left to the manager.

## Result
PASS on the build: both sections are inserted append-only, both address edits are byte-exact, and the name, S13 and PII checks are clean (blocks 4-7). Five facts in the flagged lines did NOT reproduce. They are listed at the end of block 2 and marked in the sections.

### 7. Self-check of this report
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T00:49:34Z
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[629] last_nonblank_line=629 last_nonblank_is_S13=YES lines=629
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ python3 -I /tmp/c2mgr/pii.py docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=56 mac_or_key_lines=107,133,135,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,166,167,416,417,418,419,420,421,423,503
$ W=$(printf "v%sdict|COMMIT-%s|COMMIT-%s" er INDEX DIFF-SHA256); grep -ciE "$W" <(sed -n 206,463p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(sed -n 207,365p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
/dev/fd/63:0
/dev/fd/62:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:0
```
This output was taken when this block still held a one-line `(pending)` placeholder. Pasting the output and this note added lines. So `at=`, `last_nonblank_line=` and `lines=` here are lower than the final file's values, by the number of lines added. The name, S13, PII and word counts do not depend on that, and this block adds no name, S13, address, key-path token or banned word. The key-path lines listed (107-167, 416-423 and 503) are all in blocks 2, 3 and 4. They are the re-pasted pii.py source, grep patterns, and the quoted M:163 pattern line. None is a key path.

## Addendum (worker3, 2026-11-12)
Added by worker3 of this unit (report: docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md). Insertion only. No line above was changed. Line 4 says "Nothing under vm/ or .claude/ was written." and pastes nothing for it. The check below ran under bash through /tmp/c3w3/gen.sh, which is pasted in full as the third command. Each `$ ` line is one line of /tmp/c3w3/cmds_w1.txt, passed unchanged to `run`. Line 7 of gen.sh masks the whole output stream for the name and the S13 sentence.
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T01:12:46Z
$ date +%z
-0500
$ cat -n /tmp/c3w3/gen.sh
     1	#!/bin/bash
     2	cd /Volumes/Sensidine/Praxis.build || exit 1
     3	N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
     4	S13=$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)
     5	export N S13
     6	run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
     7	while IFS= read -r c <&3; do run "$c" </dev/null; done 3< "$1" | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/\Q$ENV{S13}\E/<S13>/g'
$ find .claude vm -newer /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md -exec stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" {} \;
2026-11-11T18:24:36 .claude/state/mint-log
$ find .claude vm -newer /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md | wc -l
       1
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md
2026-11-11T18:17:51 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/c3pre docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
2026-11-11T19:39:57 /tmp/c3pre
2026-11-11T19:50:13 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
$ sed -n 18p docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -o 'cp -p [^;]*'
cp -p docs/reports/$f /tmp/c3pre/$f && cmp docs/reports/$f /tmp/c3pre/$f && echo "identical: $f"
$ sed -n 20p docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
2026-11-12T00:39:57Z
$ grep -n '^2026-11-12T' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | tail -n 1
628:2026-11-12T00:49:34Z
```
What it shows:
- The `find` lists one path, .claude/state/mint-log, with mtime 2026-11-11T18:24:36. It lists nothing under vm/.
- The reference file's mtime is 2026-11-11T18:17:51. Line 18 shows it was copied with `cp -p`, which keeps the source's mtime, so 18:17:51 is not the time of the copy. /tmp/c3pre itself has mtime 2026-11-11T19:39:57. Line 20 gives worker1's start as 2026-11-12T00:39:57Z. The local offset is -0500, so that is 2026-11-11T19:39:57 local.
- mint-log's mtime (18:24:36 local) is before worker1 began (19:39:57 local), so the mint-log change is not worker1's write. Nothing else under .claude or vm has an mtime after 18:17:51.
- This test sees modification times only. It does not show a write whose mtime was set back afterwards.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
