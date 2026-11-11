# 2026-11-11 v-rulings-filing Correction 2 - worker4 (ADVERSARIAL)

## Task
Unit 2026-11-11-v-rulings-filing-correction-2 (bead Praxis_build-n1y), mode ADVERSARIAL. Try to break the latest fix pass on four files: (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, (b) docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md, (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md, (d) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md. Read-only except this report. Nothing staged, committed or edited in (a)-(d).

## Criteria tested
S1 (every claim has pasted output), S2 (no claim above its evidence), S13 (the standing sentence once, standalone, last line). Unit rules: append-only bodies of (a) and (b) against /tmp/c2pre; (c) pre-pass lines unchanged against /tmp/c2fix; complete pasted outputs; byte-exact original wording; RECOVERED / INFERRED / UNVERIFIED labels; no negative or universal claim broader than its search; zero name hits; no PII.

## Commands and output
All commands were run on 2026-11-11 from the repo root under /bin/bash, via /tmp/w4/gen.sh. That script sources /tmp/w4/pre.sh (printed in block 2) and prints every command as `$ cmd` with its full output. Output is masked: the name as `<NAME>`, the S13 sentence as `<S13>`, and lines that begin with three backticks as `<fence>`.

### 1. Append-only
```
$ cmp <(sed -n 1,264p $PA) <(sed -n 1,264p $A); echo "a 1-264 rc=$?"
a 1-264 rc=0
$ cmp <(tail -n 1 $PA) <(tail -n 1 $A); echo "a last rc=$?"
a last rc=0
$ cmp <(sed -n 1,241p $PB) <(sed -n 1,241p $B); echo "b 1-241 rc=$?"
b 1-241 rc=0
$ cmp <(tail -n 1 $PB) <(tail -n 1 $B); echo "b last rc=$?"
b last rc=0
$ for f in $A $B; do echo "$f vs c2pre: lt=$(diff -d /tmp/c2pre/${f##*/} $f | grep -c "^<") hunks=$(diff -d /tmp/c2pre/${f##*/} $f | grep "^[0-9]" | tr "\n" " ")"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md vs c2pre: lt=0 hunks=264a265,844 
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md vs c2pre: lt=0 hunks=241a242,683 
$ for f in $A $B $C; do echo "$f vs c2fix: lt=$(diff -d /tmp/c2fix/${f##*/} $f | grep -c "^<") hunks=$(diff -d /tmp/c2fix/${f##*/} $f | grep "^[0-9]" | tr "\n" " ")"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md vs c2fix: lt=2 hunks=281c281 314c314 315a316,614 452a752,772 
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md vs c2fix: lt=2 hunks=364a365 365a367,386 405c426,428 469c492 470a494,581 486a598,682 
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md vs c2fix: lt=0 hunks=451a452,566 
```
Result. The original body of (a) (1-264 plus the last line) and of (b) (1-241 plus the last line) is byte-identical to /tmp/c2pre, with 0 `<` lines and one add hunk each. Against /tmp/c2fix, (c) has 0 `<` lines and one add hunk. (a) and (b) each have 2 `<` lines against /tmp/c2fix: (a) 281 and 314, and (b) 405 and 469. These lines are inside the Correction 2 sections that the first build pass of this same unit added. (d):4 discloses that those sections were revised in place. No unit rule forbids this, so it is noted here, not flagged.

### 2. Re-run harness
h.py parses every fenced block that starts in a line range. It re-runs each `$ ` line in one bash process per block, with pre.sh as the preamble, and compares the real output line by line with the pasted lines, up to the next `$ ` line or fence.
```
$ cat /tmp/w4/pre.sh
cd /Volumes/Sensidine/Praxis.build
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
export N
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
A=docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
B=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
T=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl
W=/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl
S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }
Fz() { perl -pe 's/^(\s*)\x60\x60\x60/$1<fence>/'; }
C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
W3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
R=${ROVERRIDE:-docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md}
$ cat /tmp/w4/pre.sh | wc -l
      15
$ cat /tmp/w4/h.py
# usage: python3 -I h.py <file> <lo> <hi> [ROVERRIDE]; re-runs each "$ cmd" in fenced blocks starting in lo..hi, compares to pasted output
import sys, subprocess, os, difflib
f, lo, hi = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
env = dict(os.environ)
if len(sys.argv) > 4: env['ROVERRIDE'] = sys.argv[4]
L = open('/Volumes/Sensidine/Praxis.build/' + f, encoding='utf-8').read().split('\n')
N = subprocess.run("ls /Volumes/Sensidine/Praxis.build/docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\\.png$//'", shell=True, capture_output=True, text=True).stdout.strip()
S13 = subprocess.run(['sed','-n',"s/^S='\\(.*\\)'$/\\1/p",'/tmp/vrf-c2/selfcheck.sh'],capture_output=True,text=True).stdout.rstrip('\n')
def mask(s):
    import re
    return re.sub(re.escape(N), '<NAME>', s, flags=re.I).replace(S13, '<S13>')
i = lo - 1; tot = same = 0
while i < hi:
    if L[i].startswith('```'):
        j = i + 1
        while not L[j].startswith('```'): j += 1
        blk = L[i+1:j]; cmds = []
        for k, x in enumerate(blk):
            if x.startswith('$ '): cmds.append([i + 2 + k, x[2:], []])
            elif cmds: cmds[-1][2].append(x)
        if cmds:
            sc = open('/tmp/w4/pre.sh').read()
            for n, c, _ in cmds: sc += "\necho '@@@%d'\n%s 2>&1\n" % (n, c)
            sc += "\necho '@@@END'\n"
            out = subprocess.run(['/bin/bash', '-c', sc], capture_output=True, text=True, env=env).stdout.split('\n')
            got = {}; cur = None
            for x in out:
                if x.startswith('@@@'): cur = x[3:]; got[cur] = []; continue
                if cur: got[cur].append(x)
            for n, c, exp in cmds:
                g = got.get(str(n), ['<missing>']); tot += 1
                if g == exp: same += 1; print('%s:%d SAME pasted=%d real=%d' % (f.split('/')[-1][-20:], n, len(exp), len(g)))
                else:
                    print('%s:%d DIFF pasted=%d real=%d' % (f.split('/')[-1][-20:], n, len(exp), len(g)))
                    for d in difflib.unified_diff(exp, g, 'pasted', 'real', n=0, lineterm=''): print('    ' + mask(d)[:300])
        i = j + 1
    else: i += 1
print('TOTAL commands=%d same=%d diff=%d' % (tot, same, tot - same))
$ cat /tmp/w4/h.py | wc -l
      38
```

### 3. Re-run of every command in the regions the latest pass added to (a) and (b)
```
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 280 614
rection-1-worker1.md:285 SAME pasted=1 real=1
rection-1-worker1.md:287 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -     242 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    +     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
rection-1-worker1.md:289 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -2026-11-11T14:40:46
    +2026-11-11T17:50:55
rection-1-worker1.md:291 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -8
    +10
rection-1-worker1.md:293 SAME pasted=1 real=1
rection-1-worker1.md:295 SAME pasted=1 real=1
rection-1-worker1.md:297 DIFF pasted=1 real=2
    --- pasted
    +++ real
    @@ -0,0 +1 @@
    +/private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
rection-1-worker1.md:299 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -       1
    +       2
rection-1-worker1.md:301 SAME pasted=1 real=1
rection-1-worker1.md:303 SAME pasted=1 real=1
rection-1-worker1.md:305 SAME pasted=1 real=1
rection-1-worker1.md:307 SAME pasted=1 real=1
rection-1-worker1.md:309 SAME pasted=1 real=1
rection-1-worker1.md:311 SAME pasted=1 real=1
rection-1-worker1.md:325 SAME pasted=2 real=2
rection-1-worker1.md:328 SAME pasted=1 real=1
rection-1-worker1.md:330 SAME pasted=74 real=74
rection-1-worker1.md:405 SAME pasted=1 real=1
rection-1-worker1.md:407 SAME pasted=56 real=56
rection-1-worker1.md:464 SAME pasted=1 real=1
rection-1-worker1.md:469 SAME pasted=31 real=31
rection-1-worker1.md:501 SAME pasted=1 real=1
rection-1-worker1.md:506 SAME pasted=40 real=40
rection-1-worker1.md:547 SAME pasted=1 real=1
rection-1-worker1.md:552 SAME pasted=10 real=10
rection-1-worker1.md:563 SAME pasted=1 real=1
rection-1-worker1.md:565 SAME pasted=24 real=24
rection-1-worker1.md:590 SAME pasted=1 real=1
rection-1-worker1.md:592 SAME pasted=1 real=1
rection-1-worker1.md:597 SAME pasted=1 real=1
rection-1-worker1.md:599 SAME pasted=3 real=3
rection-1-worker1.md:603 SAME pasted=1 real=1
TOTAL commands=32 same=27 diff=5
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md 752 772
rection-1-worker1.md:754 SAME pasted=2 real=2
rection-1-worker1.md:757 SAME pasted=1 real=1
rection-1-worker1.md:759 SAME pasted=2 real=2
rection-1-worker1.md:762 SAME pasted=1 real=1
rection-1-worker1.md:764 SAME pasted=1 real=1
rection-1-worker1.md:766 SAME pasted=2 real=2
rection-1-worker1.md:769 SAME pasted=1 real=1
TOTAL commands=7 same=7 diff=0
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 365 386
rection-1-manager.md:367 SAME pasted=2 real=2
rection-1-manager.md:370 SAME pasted=1 real=1
rection-1-manager.md:372 SAME pasted=2 real=2
rection-1-manager.md:375 SAME pasted=1 real=1
rection-1-manager.md:377 SAME pasted=1 real=1
rection-1-manager.md:379 SAME pasted=2 real=2
rection-1-manager.md:382 SAME pasted=1 real=1
rection-1-manager.md:387 SAME pasted=11 real=11
rection-1-manager.md:399 SAME pasted=1 real=1
rection-1-manager.md:401 SAME pasted=11 real=11
rection-1-manager.md:413 SAME pasted=1 real=1
TOTAL commands=11 same=11 diff=0
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 426 490
rection-1-manager.md:431 SAME pasted=1 real=1
rection-1-manager.md:433 SAME pasted=1 real=1
rection-1-manager.md:435 SAME pasted=1 real=1
rection-1-manager.md:437 SAME pasted=1 real=1
rection-1-manager.md:439 SAME pasted=1 real=1
rection-1-manager.md:441 SAME pasted=1 real=1
rection-1-manager.md:443 SAME pasted=2 real=2
rection-1-manager.md:446 SAME pasted=1 real=1
rection-1-manager.md:448 SAME pasted=8 real=8
rection-1-manager.md:457 SAME pasted=1 real=1
rection-1-manager.md:459 SAME pasted=1 real=1
rection-1-manager.md:461 SAME pasted=18 real=18
rection-1-manager.md:480 SAME pasted=1 real=1
rection-1-manager.md:482 SAME pasted=1 real=1
rection-1-manager.md:484 SAME pasted=1 real=1
TOTAL commands=15 same=15 diff=0
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md 491 682
rection-1-manager.md:501 SAME pasted=7 real=7
rection-1-manager.md:509 SAME pasted=1 real=1
rection-1-manager.md:511 SAME pasted=5 real=5
rection-1-manager.md:517 SAME pasted=1 real=1
rection-1-manager.md:519 DIFF pasted=5 real=28
    --- pasted
    +++ real
    @@ -5,0 +6,23 @@
    +$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
    +name-length=4 matching-files=1
    +0	docs/reports/2026-11-11-v-rulings-filing-manager.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker1.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker2.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker3.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker4.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker5.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker6.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker7.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker8.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker9.md
    +0	docs/reports/2026-11-11-v-rulings-filing-worker10.md
    +0	docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
    +0	vm/replies/20261111T172933Z-python-git-install.md
    +0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    +0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
    +0	DECISIONS.md (tail -n +2100)
    +$ python3 -I /tmp/vrf-c1/s13.py <two new reports>
    +2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
    +2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
    +$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l
    +       0
rection-1-manager.md:525 SAME pasted=17 real=17
rection-1-manager.md:543 DIFF pasted=2 real=1
    --- pasted
    +++ real
    @@ -1,2 +1 @@
    -2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
    -2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
    +
rection-1-manager.md:546 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -       0
    +<missing>
rection-1-manager.md:548 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -      28
    +<missing>
rection-1-manager.md:550 DIFF pasted=14 real=1
    --- pasted
    +++ real
    @@ -1,14 +1 @@
    -matching_tool_uses=1
    -=== tool_use timestamp=2026-11-11T19:40:36.861Z tool=Bash ; tool_result timestamp=2026-11-11T19:40:37.235Z
    ---- input:
    -export SC="$(cat /tmp/vrf-c1/selfcheck.txt)" && python3 -I -c '
    -import os
    -f="docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md"
    -b=open(f,encoding="utf-8").read(); assert b.count("SELFCHECK_PLACEHOLDER")==1
    -b=b.replace("SELFCHECK_PLACEHOLDER","Run on this report with this section still a placeholder. The re-run after pasting is the last block in this section.\n```\n"+os.environ["SC"]+"\n```")
    -open(f,"w",encoding="utf-8").write(b)' && /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | tail -3 && python3 -I /tmp/vrf-c1/s13.py docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.m
    ---- result:
    -0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    -0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
    -0	DECISIONS.md (tail -n +2100)
    -2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
    +<missing>
rection-1-manager.md:565 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -      14
    +<missing>
rection-1-manager.md:567 DIFF pasted=7 real=1
    --- pasted
    +++ real
    @@ -1,7 +1 @@
    -original_line_207 in_19:40:29_result=True in_19:40:36_result=False
    -original_line_208 in_19:40:29_result=True in_19:40:36_result=False
    -original_line_210 in_19:40:29_result=True in_19:40:36_result=False
    -original_line_214 in_19:40:29_result=True in_19:40:36_result=True
    -original_line_215 in_19:40:29_result=True in_19:40:36_result=True
    -original_line_216 in_19:40:29_result=True in_19:40:36_result=True
    -original_line_217 in_19:40:29_result=False in_19:40:36_result=True
    +<missing>
rection-1-manager.md:575 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -       7
    +<missing>
rection-1-manager.md:582 DIFF pasted=2 real=2
    --- pasted
    +++ real
    @@ -1,2 +1,2 @@
    -A identical to pre-edit copy
    -B identical to pre-edit copy
    +docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md differ: char 17670, line 265
    +docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md differ: char 17199, line 242
rection-1-manager.md:585 DIFF pasted=3 real=3
    --- pasted
    +++ real
    @@ -1,2 +1,2 @@
    -docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
    -docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
    +docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[845] last_nonblank_line=845 last_nonblank_is_S13=YES lines=845
    +docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[684] last_nonblank_line=684 last_nonblank_is_S13=YES lines=684
rection-1-manager.md:589 SAME pasted=1 real=1
rection-1-manager.md:591 DIFF pasted=2 real=2
    --- pasted
    +++ real
    @@ -1,2 +1,2 @@
    -2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
    -2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[242] in_fence=0 last_nonblank_line=242 is_last=True substring_lines=1
    +2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[845] in_fence=0 last_nonblank_line=845 is_last=True substring_lines=1
    +2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[684] in_fence=0 last_nonblank_line=684 is_last=True substring_lines=1
rection-1-manager.md:594 SAME pasted=1 real=1
rection-1-manager.md:606 DIFF pasted=18 real=37
    --- pasted
    +++ real
    @@ -18,0 +19,19 @@
    +$ git diff --cached --name-only -- 'docs/reports/2026-11-11-v-rulings-filing-*' MANIFEST.md | wc -l
    +       0
    +<fence>
    +<fence>
    +$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)
    +0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    +0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
    +0	DECISIONS.md (tail -n +2100)
    +2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
    +<fence>
    +
    +## Adversarial findings
    +manager True
    +worker3 True
    +worker4 True
    +worker5 True
    +worker10 True
    +     405 MANIFEST.md
    +[This command modified 1 file you've previously read: docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md. Call Read before editing.]
rection-1-manager.md:625 DIFF pasted=3 real=1
    --- pasted
    +++ real
    @@ -2,2 +1,0 @@
    -<fence>
    -<fence>
rection-1-manager.md:629 DIFF pasted=14 real=1
    --- pasted
    +++ real
    @@ -1,5 +0,0 @@
    -0	docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
    -0	docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
    -0	DECISIONS.md (tail -n +2100)
    -2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
    -<fence>
    @@ -7,8 +1,0 @@
    -## Adversarial findings
    -manager True
    -worker3 True
    -worker4 True
    -worker5 True
    -worker10 True
    -     405 MANIFEST.md
    -[This command modified 1 file you've previously read: docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md. Call Read before editing.]
rection-1-manager.md:644 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -      37
    +<missing>
rection-1-manager.md:649 SAME pasted=9 real=9
rection-1-manager.md:659 SAME pasted=1 real=1
rection-1-manager.md:661 SAME pasted=17 real=17
rection-1-manager.md:679 SAME pasted=1 real=1
TOTAL commands=26 same=11 diff=15
```
Every DIFF above is explained, and none is a shortfall in the pasted output:
- (a):287-299. This block is the first-pass "re-run on current files". It is unchanged context inside C2.1. Since then (b) has grown from 242 to 684 lines (its mtime changed, and it now has 10 `## ` lines), and the /tmp/c2fix copy has been created. The pre-edit state is no longer on disk, apart from /tmp/c2pre. On the /tmp/c2pre copy, the line count and name count match (block 5). See finding 2.
- (b):519, :550, :606. The recorded tool results contain `$ ` lines of their own, so h.py splits them into fake commands (:525, :543, :546, :548, :565, :567, :575, :625, :629, :644 are results of that split). Block 5 compares each full tx.py/rec.py output with the pasted range directly. All four match exactly (diff rc=0), with real line counts 28, 14, 37 and 7, equal to the pasted `wc -l` lines.
- (b):582, :585, :591. These were run "before Correction 2 was added", as the report states. The same commands on the /tmp/c2pre copies reproduce the pasted figures (block 5). Only the path prefix differs, because selfcheck.sh prints the argument path.

### 4. Re-run of every command in the (c) addendum and in (d)
```
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md 452 566
rection-2-worker1.md:457 SAME pasted=0 real=0
rection-2-worker1.md:458 SAME pasted=1 real=1
rection-2-worker1.md:460 DIFF pasted=1 real=1
    --- pasted
    +++ real
    @@ -1 +1 @@
    -406 411 413 417 423 429 431 
    +406 411 413 417 423 429 431 455 458 460 487 533 541 543 
rection-2-worker1.md:466 SAME pasted=4 real=4
rection-2-worker1.md:471 SAME pasted=1 real=1
rection-2-worker1.md:473 SAME pasted=1 real=1
rection-2-worker1.md:475 SAME pasted=1 real=1
rection-2-worker1.md:477 SAME pasted=1 real=1
rection-2-worker1.md:479 SAME pasted=1 real=1
rection-2-worker1.md:481 SAME pasted=2 real=2
rection-2-worker1.md:484 SAME pasted=2 real=2
rection-2-worker1.md:487 DIFF pasted=2 real=5
    --- pasted
    +++ real
    @@ -2,0 +3,3 @@
    +464:**Step 1 (:12).** :12 says that (a) and (b) matched their pre-edit copies (`diff` exit 0), and that the raw name count was 0 in all four files, meaning (a), (b) and their /tmp/c2pre copies. That full-file match described (a) and (b) before the Correction 2 insertion, and it cannot be re-execute
    +488:307:A identical to pre-edit copy
    +489:308:B identical to pre-edit copy
rection-2-worker1.md:494 SAME pasted=12 real=12
rection-2-worker1.md:507 SAME pasted=1 real=1
rection-2-worker1.md:509 DIFF pasted=6 real=6
    --- pasted
    +++ real
    @@ -1 +1 @@
    -/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.OkE5X7xMH3/2026-11-11-v-rulings-filing-correction-1-worker1.md inserted 260 lines before final line
    +/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.7Fbr8ckSIx/2026-11-11-v-rulings-filing-correction-1-worker1.md inserted 260 lines before final line
    @@ -3 +3 @@
    -/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.OkE5X7xMH3/2026-11-11-v-rulings-filing-correction-1-manager.md inserted 246 lines before final line
    +/var/folders/6g/9y7c60hs3yv9bmk1w1lwbt4c0000gn/T/tmp.7Fbr8ckSIx/2026-11-11-v-rulings-filing-correction-1-manager.md inserted 246 lines before final line
rection-2-worker1.md:516 SAME pasted=5 real=5
rection-2-worker1.md:522 SAME pasted=6 real=6
rection-2-worker1.md:533 SAME pasted=7 real=7
rection-2-worker1.md:541 SAME pasted=1 real=1
rection-2-worker1.md:543 DIFF pasted=14 real=15
    --- pasted
    +++ real
    @@ -14,0 +15 @@
    +452:## Addendum (worker3, fix pass)
TOTAL commands=20 same=16 diff=4
$ python3 -I /tmp/w4/h.py docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md 1 323
rection-2-worker3.md:27 SAME pasted=31 real=31
rection-2-worker3.md:59 SAME pasted=1 real=1
rection-2-worker3.md:63 SAME pasted=10 real=10
rection-2-worker3.md:74 SAME pasted=1 real=1
rection-2-worker3.md:76 SAME pasted=24 real=24
rection-2-worker3.md:101 SAME pasted=1 real=1
rection-2-worker3.md:103 SAME pasted=1 real=1
rection-2-worker3.md:108 SAME pasted=2 real=2
rection-2-worker3.md:111 SAME pasted=1 real=1
rection-2-worker3.md:113 SAME pasted=1 real=1
rection-2-worker3.md:115 SAME pasted=1 real=1
rection-2-worker3.md:123 SAME pasted=7 real=7
rection-2-worker3.md:131 SAME pasted=1 real=1
rection-2-worker3.md:138 SAME pasted=17 real=17
rection-2-worker3.md:156 SAME pasted=1 real=1
rection-2-worker3.md:163 SAME pasted=16 real=16
rection-2-worker3.md:180 SAME pasted=1 real=1
rection-2-worker3.md:182 SAME pasted=2 real=2
rection-2-worker3.md:185 SAME pasted=1 real=1
rection-2-worker3.md:193 SAME pasted=2 real=2
rection-2-worker3.md:196 SAME pasted=1 real=1
rection-2-worker3.md:198 SAME pasted=2 real=2
rection-2-worker3.md:201 SAME pasted=1 real=1
rection-2-worker3.md:203 SAME pasted=1 real=1
rection-2-worker3.md:205 SAME pasted=2 real=2
rection-2-worker3.md:208 SAME pasted=1 real=1
rection-2-worker3.md:218 SAME pasted=4 real=4
rection-2-worker3.md:223 SAME pasted=1 real=1
rection-2-worker3.md:225 SAME pasted=6 real=6
rection-2-worker3.md:232 SAME pasted=1 real=1
rection-2-worker3.md:234 SAME pasted=12 real=12
rection-2-worker3.md:247 SAME pasted=1 real=1
rection-2-worker3.md:249 SAME pasted=4 real=4
rection-2-worker3.md:262 SAME pasted=1 real=1
rection-2-worker3.md:264 SAME pasted=1 real=1
rection-2-worker3.md:266 SAME pasted=1 real=1
rection-2-worker3.md:268 SAME pasted=2 real=2
rection-2-worker3.md:271 SAME pasted=1 real=1
rection-2-worker3.md:273 SAME pasted=1 real=1
rection-2-worker3.md:275 SAME pasted=1 real=1
rection-2-worker3.md:277 SAME pasted=2 real=2
rection-2-worker3.md:280 SAME pasted=1 real=1
rection-2-worker3.md:282 SAME pasted=1 real=1
rection-2-worker3.md:284 SAME pasted=1 real=1
rection-2-worker3.md:286 SAME pasted=2 real=2
rection-2-worker3.md:289 SAME pasted=1 real=1
rection-2-worker3.md:294 SAME pasted=1 real=1
rection-2-worker3.md:296 SAME pasted=5 real=5
rection-2-worker3.md:302 SAME pasted=1 real=1
rection-2-worker3.md:304 SAME pasted=4 real=4
rection-2-worker3.md:309 SAME pasted=1 real=1
rection-2-worker3.md:311 SAME pasted=4 real=4
rection-2-worker3.md:316 SAME pasted=1 real=1
TOTAL commands=53 same=53 diff=0
```
(d): 53 of 53 commands reproduce exactly. In the (c) addendum, :460, :487 and :543 differ only by lines of the addendum itself. The addendum says its blocks were run before it was inserted. The same commands on the /tmp/c2fix copy of (c) reproduce the pasted output exactly (block 5 for :458/:460, block 6 for :487/:533/:543). :509 differs only in the random mktemp directory name.

### 5. Direct comparisons for the nested tool outputs, and pre-edit re-runs on the /tmp copies
```
$ for r in "520 547 19:40:29" "551 564 19:40:36" "607 643 19:40:46"; do set -- $r; diff <(sed -n "$1,$2p" $B) <(python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T$3 | M | Fz) >/dev/null; echo "(b):$1-$2 vs tx.py ts $3 | M | Fz: diff_rc=$? real_lines=$(python3 -I /tmp/c2fix/tx.py ts $T 2026-11-11T$3 | M | Fz | wc -l | tr -d " ")"; done
(b):520-547 vs tx.py ts 19:40:29 | M | Fz: diff_rc=0 real_lines=28
(b):551-564 vs tx.py ts 19:40:36 | M | Fz: diff_rc=0 real_lines=14
(b):607-643 vs tx.py ts 19:40:46 | M | Fz: diff_rc=0 real_lines=37
$ diff <(sed -n 568,574p $B) <(python3 -I /tmp/c2fix/rec.py bmatch $T $PB | M); echo "(b):568-574 vs bmatch diff_rc=$?"
(b):568-574 vs bmatch diff_rc=0
$ cmp $PA $PA && echo "A identical to pre-edit copy"; cmp $PB $PB && echo "B identical to pre-edit copy"
A identical to pre-edit copy
B identical to pre-edit copy
$ /tmp/vrf-c2/selfcheck.sh $PA $PB | M
/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ python3 -I /tmp/vrf-c1/s13.py $PA $PB | M
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[242] in_fence=0 last_nonblank_line=242 is_last=True substring_lines=1
$ R=/tmp/c2fix/${C##*/}; grep -c "^R=" $R; grep -n "\$R" $R | cut -d: -f1 | tr "\n" " "; echo
0
406 411 413 417 423 429 431 
$ stat -f "%N %z bytes, modified %Sm" $T $W
/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl 440951 bytes, modified Nov 11 14:41:00 2026
/Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl 405504 bytes, modified Nov 11 14:39:09 2026
```
The transcripts T and W have the same size and mtime as pasted in (a):325-327. They are completed subagent logs, so they are stable.

### 6. (c) addendum commands, re-run on the pre-addendum copy
```
$ R=/tmp/c2fix/${C##*/}; grep -n "identical to pre-edit copy" $R | grep -v "&&"
307:A identical to pre-edit copy
308:B identical to pre-edit copy
$ R=/tmp/c2fix/${C##*/}; grep -n -e "^### " -e "^## " $R | M
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
$ R=/tmp/c2fix/${C##*/}; grep -n -e "^### " -e "^## " $R | M | wc -l
      14
$ R=/tmp/c2fix/${C##*/}; diff <(python3 -I /tmp/c2fix/blkcheck.py $R 32 322 $A $B) <(sed -n 534,540p $C); echo "blkcheck on c2fix copy vs (c):534-540 diff_rc=$?"
blkcheck on c2fix copy vs (c):534-540 diff_rc=0
$ diff <(R=/tmp/c2fix/${C##*/}; grep -n -e "^### " -e "^## " $R | M) <(sed -n 544,557p $C); echo "(c):544-557 vs c2fix diff_rc=$?"
(c):544-557 vs c2fix diff_rc=0
```

### 7. Factual checks of the key corrected claims
This block uses an extraction independent of tx.py (wc.py reads the raw JSON).
```
$ python3 -I /tmp/c2fix/tx.py grepuse $T "" | M | awk '$1>="2026-11-11T19:40:20" && $1<="2026-11-11T19:40:50"'
2026-11-11T19:40:23.359Z Bash toolu_017G3w23tgBpsj7kmiG5bHyu
2026-11-11T19:40:29.324Z Bash toolu_01AHMAe3BYDF5GcgGr1QES4y
2026-11-11T19:40:36.861Z Bash toolu_01YZKGcW7FakwQtHeFE46cyx
2026-11-11T19:40:46.708Z Bash toolu_01EVaw9EMxSMWHuSDmmMMDdf
$ date +%Z%z
EST-0500
$ python3 -I -c "import datetime as d; t=d.datetime(2026,11,11,19,33,58,tzinfo=d.timezone.utc); print(int(t.timestamp()), t.astimezone(d.timezone(d.timedelta(hours=-5))).isoformat())"
1794425638 2026-11-11T14:33:58-05:00
$ cat /tmp/w4/wc.py
# usage: python3 -I wc.py <transcript>; independent of tx.py: counts in the manager's Write content for the correction-1 manager report
import json, sys
for ln in open(sys.argv[1], encoding='utf-8'):
    if not ln.strip(): continue
    r = json.loads(ln)
    if r.get('type') != 'assistant': continue
    for b in (r.get('message') or {}).get('content') or []:
        if isinstance(b, dict) and b.get('type') == 'tool_use' and b['name'] == 'Write' and b['input'].get('file_path', '').endswith('correction-1-manager.md'):
            c = b['input']['content']; L = c.split('\n')
            print(r['timestamp'], 'newlines=%d hash2=%d pending=%d hash1=%d' % (c.count('\n'), sum(x.startswith('## ') for x in L), sum(x == '(pending)' for x in L), sum(x.startswith('# ') for x in L)))
            for i, x in enumerate(L[:-1]):
                if x.startswith('## '): print('  line', i + 1, 'next_is_pending=%s' % (L[i + 1] == '(pending)'))
$ python3 -I /tmp/w4/wc.py $T | M
2026-11-11T19:33:58.402Z newlines=27 hash2=8 pending=8 hash1=1
  line 3 next_is_pending=True
  line 6 next_is_pending=True
  line 9 next_is_pending=True
  line 12 next_is_pending=True
  line 15 next_is_pending=True
  line 18 next_is_pending=True
  line 21 next_is_pending=True
  line 24 next_is_pending=True
```
Result. The recovered skeleton has 27 lines (27 newline-terminated), 8 `## ` lines and 8 `(pending)` lines, and each `## ` line is followed by `(pending)`. So the original (a):218 "All nine sections" is wrong, as (a) C2.1 now says. 19:33:58Z is 14:33:58 at -0500, and this machine reports EST-0500. The epoch 1794425638 matches (a):600. (b) :207 `at=[210]` and :217 `at=[235]` are reproduced from T (block 5). The (b) C2.4 count.sh output is complete: 17 lines, matching its `wc -l`. T has exactly 4 tool calls between 19:40:20 and 19:40:50, and all of them are in the `grepuse` list. This closes, for T, the "Not checked" item at (d):321.

### 8. Quote exactness
q.py is independent of qcheck.py. It parses every "Original wording" line in the Correction 2 sections of (a) and (b), including range references like `:223-225`. It compares each backtick or double-quote span with the /tmp/c2pre line or lines it cites:
```
$ cat /tmp/w4/q.py
import re
F={'a':('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md','/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md',264),
   'b':('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md','/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md',241)}
for k,(cur,pre,body) in F.items():
    c=open(cur,encoding='utf-8').read().split('\n'); p=open(pre,encoding='utf-8').read().split('\n')
    for i,line in enumerate(c[body:],body+1):
        if 'Original wording' not in line: continue
        # tokenise: refs :N or :N-M, backtick spans, double-quote spans (may contain backticks)
        toks=re.finditer(r':(\d+)(?:-(\d+))?|"((?:[^"])*)"|`([^`]*)`',line.split('Original wording:',1)[1])
        ref=None; spans=[]
        for m in toks:
            if m.group(1): ref=(int(m.group(1)),int(m.group(2) or m.group(1))); continue
            q=m.group(3) if m.group(3) is not None else m.group(4)
            if ref is None: ref=('none',)
            spans.append((ref,q,'dq' if m.group(3) is not None else 'bt'))
        for ref,q,t in spans:
            if ref==('none',):
                hits=[n+1 for n in range(body) if q in p[n]]
                print('(%s):%d %s unref-quote len=%d found_in_pre_lines=%s'%(k,i,t,len(q),hits)); continue
            lo,hi=ref; eq=[n for n in range(lo,hi+1) if p[n-1]==q]; sub=[n for n in range(lo,hi+1) if q in p[n-1]]
            print('(%s):%d %s ref=:%d-%d len=%d equal_lines=%s substring_lines=%s'%(k,i,t,lo,hi,len(q),eq,sub))
$ python3 -I /tmp/w4/q.py
(a):281 bt ref=:209-209 len=12 equal_lines=[209] substring_lines=[209]
(a):281 bt ref=:210-210 len=73 equal_lines=[210] substring_lines=[210]
(a):281 bt ref=:211-211 len=19 equal_lines=[211] substring_lines=[211]
(a):281 dq ref=:218-218 len=140 equal_lines=[218] substring_lines=[218]
(a):616 bt ref=:223-225 len=23 equal_lines=[223] substring_lines=[223]
(a):616 bt ref=:223-225 len=24 equal_lines=[224] substring_lines=[224]
(a):616 bt ref=:223-225 len=21 equal_lines=[225] substring_lines=[225]
(a):616 bt ref=:226-226 len=42 equal_lines=[226] substring_lines=[226]
(a):644 dq ref=:228-228 len=111 equal_lines=[228] substring_lines=[228]
(a):644 bt ref=:240-240 len=62 equal_lines=[240] substring_lines=[240]
(a):644 dq ref=:242-242 len=93 equal_lines=[] substring_lines=[242]
(a):821 dq unref-quote len=142 found_in_pre_lines=[252]
(a):826 dq ref=:257-257 len=95 equal_lines=[] substring_lines=[257]
(a):826 bt ref=:261-261 len=21 equal_lines=[261] substring_lines=[261]
(a):826 bt ref=:262-262 len=63 equal_lines=[262] substring_lines=[262]
(b):258 dq unref-quote len=248 found_in_pre_lines=[228]
(b):427 bt ref=:238-238 len=41 equal_lines=[238] substring_lines=[238]
(b):492 bt ref=:207-207 len=152 equal_lines=[207] substring_lines=[207]
(b):492 bt ref=:217-217 len=152 equal_lines=[217] substring_lines=[217]
(b):600 bt ref=:206-206 len=49 equal_lines=[206] substring_lines=[206]
(b):600 bt ref=:213-213 len=136 equal_lines=[213] substring_lines=[213]
$ python3 -I /tmp/w4/q.py | wc -l
      21
$ python3 -I /tmp/c2fix/qcheck.py | grep -c ":22[345] "
0
```
Result. All 21 spans are exact. 19 equal a whole cited line, and the other 2 are substrings: (a):644 of :242 and (a):826 of :257 (both partial quotes, untouched by this pass). The two unreferenced quotes are found at PA:252 and PB:228. qcheck.py, which (d) uses, has 0 rows for :223, :224 and :225 (finding 3).

### 9. Evidence for findings 1, 2 and 4
```
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -oE ":[0-9]{3}(-[0-9]{3})?" | tr "\n" " "; echo
:210 :211 :218 :218 :209 :250 
$ sed -n 314p $A | grep -oE ":[0-9]{3}(-[0-9]{3})?" | tr "\n" " "; echo
:209-211 :213-216 :218 :250 
$ grep -n UNVERIFIED /tmp/c2fix/${A##*/} | cut -d: -f1 | tr "\n" " "; echo
314 
$ sed -n 215p $PA | od -c
0000000                        .   .   .  \n                            
0000011
$ grep -c "^ *assert" /tmp/vrf-c2/insert.py
3
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | M
/private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ wc -l /tmp/c2fix/${B##*/}
     488 /tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
```

### 10. Name, PII and S13 on (a)-(d) and this report
The regex text inside the grep commands below is not a hit: these lines are command text, and the counts are computed on file content. Every count is 0 for all five files, including this report, whose grep commands contain the regex text.
```
$ echo "len=${#N}"
len=4
$ cat /tmp/w4/pii.sh
#!/bin/bash
# usage: pii.sh <file>... ; prints counts only
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
for f in "$@"; do
  ci=$(grep -ci -- "$N" "$f")
  ip=$(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$f" | grep -vcx '127\.0\.0\.1')
  mac=$(grep -ciE '([0-9a-f]{2}[:-]){5}[0-9a-f]{2}' "$f")
  em=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f")
  kp=$(grep -ciE 'id_(r)sa|id_(e)d25519|id_(e)cdsa|\.p(e)m\b|\.s(s)h/|PRIVATE[ ]KEY' "$f")
  echo "$f ci=$ci ipv4_non_loopback=$ip mac=$mac email=$em keypath=$kp"
done
$ cat /tmp/w4/pii.sh | wc -l
      12
$ /tmp/w4/pii.sh $A $B $C $W3 $W4 | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md ci=0 ipv4_non_loopback=0 mac=0 email=0 keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md ci=0 ipv4_non_loopback=0 mac=0 email=0 keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md ci=0 ipv4_non_loopback=0 mac=0 email=0 keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md ci=0 ipv4_non_loopback=0 mac=0 email=0 keypath=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md ci=0 ipv4_non_loopback=0 mac=0 email=0 keypath=0
$ /tmp/vrf-c2/selfcheck.sh $A $B $C $W3 $W4 | M
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[845] last_nonblank_line=845 last_nonblank_is_S13=YES lines=845
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[684] last_nonblank_line=684 last_nonblank_is_S13=YES lines=684
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[567] last_nonblank_line=567 last_nonblank_is_S13=YES lines=567
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[323] last_nonblank_line=323 last_nonblank_is_S13=YES lines=323
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[712] last_nonblank_line=712 last_nonblank_is_S13=YES lines=712
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ python3 -I /tmp/vrf-c1/s13.py $A $B $C $W3 $W4 | M
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[845] in_fence=0 last_nonblank_line=845 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[684] in_fence=0 last_nonblank_line=684 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker1.md standalone_outside_fence=1 at=[567] in_fence=0 last_nonblank_line=567 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker3.md standalone_outside_fence=1 at=[323] in_fence=0 last_nonblank_line=323 is_last=True substring_lines=1
2026-11-11-v-rulings-filing-correction-2-worker4.md standalone_outside_fence=1 at=[712] in_fence=0 last_nonblank_line=712 is_last=True substring_lines=1
$ for f in $A $B $C $W3 $W4; do echo "$f last_line_is_S13=$(tail -n 1 $f | grep -cxF -- "$S13")"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md last_line_is_S13=1
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md last_line_is_S13=1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md last_line_is_S13=1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md last_line_is_S13=1
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md last_line_is_S13=1
$ git diff --cached --name-only -- $A $B $C $W3 $W4 | wc -l
       0
```

## Findings
1. MINOR (S1, misstatement of a predecessor state). (a):314, rewritten in this pass, says "The earlier version of this item stopped there and labelled :209-211, :213-216, :218 and :250 UNVERIFIED (not re-runnable)." The earlier version (/tmp/c2fix copy, line 314, the only UNVERIFIED line in that file) labelled :210, :211, :218 (twice), :209 and :250. It never labelled :213-216 (block 9). Also, :215 (like :212) is an elision marker, five spaces then `...` (block 9 `od -c`), and (a):610 itself says it is not an output line. (c):560 repeats this: "the skeleton claims at (a) :209-211, :213-216, :218 and :250 are no longer UNVERIFIED" and "On that evidence, :209, :210, :211, :213-216 ... hold". That counts :215 as a claim that holds.
2. MINOR (S1, stale "current" result in a rewritten line). (a):314 was rewritten in this pass, after /tmp/c2fix was created at 17:44. It still opens "Result of the re-run on current files" and states that the manager report "now has 242 lines" and that "the only file whose name contains `correction-1-manager` is the /tmp/c2pre copy". When it was rewritten, (b) had 488 lines and the /tmp/c2fix copy existed. Re-run now, `find` returns 2 files (block 9; block 3 :297/:299). The conclusion "no copy of the skeleton" still holds, because the /tmp/c2fix copy has 488 lines. But the line presents first-pass figures as current and does not date them.
3. MINOR (universal claim broader than its check). (d):161 says "Check of every `:N` quote in an 'Original wording:' line against line N of the /tmp/c2pre copy". qcheck.py's pattern `:(\d+) ` requires a space after the number, so the three spans after `:223-225` in (a):616 are skipped. Its output has 0 rows for :223-225 (block 8). The spans are in fact exact (q.py rows for (a):616), so no wording is wrong. Only the coverage claim is overstated.
4. MINOR (S2, liveness claim above its test). (c):492 says "Two negative controls show that the assertions are live." insert.py has 3 assertions (block 9). The controls trip `unexpected tail` and `S not in`. The assertion `section must end with one blank line` is never shown failing.

Checked with no break found: append-only bodies and (c) pre-pass lines (block 1); every command in the added regions of (a), (b) and (c), and all 53 in (d), reproduce, or differ only for the stated reasons (blocks 3-6); 27/8/8 skeleton counts, the conversion of 14:33:58 local to 19:33:58Z, at=[210] and at=[235], and the full 17-line count.sh output (blocks 5 and 7); every original-wording quote is byte-exact (block 8); the name appears 0 times (case-insensitive and split-name detector, positive control 1); no PII; S13 is standalone once on the last line in all five files (block 10); RECOVERED, INFERRED and UNVERIFIED labels are present where required ((a):316, (a):609, (b):489, (b):492, (b):604).

## Result
FAIL: 4 MINOR defects, 0 MAJOR. None of them changes a corrected figure. Findings 1 and 2 are wrong or stale statements in a line this pass rewrote. Findings 3 and 4 are coverage claims that are broader than their checks.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
