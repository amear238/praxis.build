# 2026-11-11 v-rulings-filing Correction 2 - worker2 (ADVERSARIAL)

## Task
Unit `2026-11-11-v-rulings-filing-correction-2` (bead Praxis_build-n1y), ADVERSARIAL mode. Try to break three artifacts:
- (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, Correction 2 section at lines 265-524. Pre-edit copy: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md.
- (b) docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md, Correction 2 section at lines 242-487. Pre-edit copy: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md.
- (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md (new).

The only file written was this report. Nothing was staged, committed, or written under .claude/. No memory writes.

## Criteria tested
- S1: every claim has pasted command output, not a description of output.
- S2: nothing is reported above what the evidence supports.
- S13: the S13 sentence appears once, as the standalone last line, outside code fences and bullets. It does not appear verbatim in the inserted sections.
- Unit requirements:
  - Corrections are append-only.
  - Every pasted block is complete.
  - Each quoted original wording matches the pre-edit line.
  - Claims that could not be re-run are labelled UNVERIFIED (not re-runnable).
  - Inferred figures are labelled INFERRED.
- The name must not leak, and there is no other PII.

Masking used in all output below: the name becomes `<NAME>` (perl `\Q$ENV{N}\E`, case-insensitive), and the S13 sentence becomes `<S13>`. Neither appears in any command, because both are built at runtime.

## Commands and output
All commands were run on 2026-11-11 from the repo root unless a `cd` is shown. `N` was always derived as specified in the brief. `run` is `printf '$ %s\n' "$1"; eval "$1" 2>&1`.

### 1. Append-only check of (a) and (b)
```
== A
$ shasum -a 256 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
24932bddc8402421df8a3304d9dd5b2875a0eec21f1d8d205735146ac2c12049  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | grep -cE '^<'
0
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | grep -cE '^[0-9]+(,[0-9]+)?[cd]'
0
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | grep -vE '^>'
262a263,451
263a453,484
264a486,524
$ diff -d /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | grep -vE '^>'
264a265,524
L=265
$ head -n 264 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | cmp - <(head -n 264 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md) && echo first-L-1-identical
first-L-1-identical
$ tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | cmp - <(tail -n 1 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md) && echo last-line-identical
last-line-identical
$ tail -c 1 docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | xxd -p
0a
$ wc -l < docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
     525
$ git ls-files -s -- docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md | wc -l
       0
== B
$ shasum -a 256 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
cc00cc5edd2035b26ad6e0c247de1ffbaf9d08dc2c8fe9be1d864feba6d222ed  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | grep -cE '^<'
0
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | grep -cE '^[0-9]+(,[0-9]+)?[cd]'
0
$ diff /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | grep -vE '^>'
240a241,395
241a397,487
$ diff -d /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | grep -vE '^>'
241a242,487
L=242
$ head -n 241 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | cmp - <(head -n 241 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md) && echo first-L-1-identical
first-L-1-identical
$ tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | cmp - <(tail -n 1 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md) && echo last-line-identical
last-line-identical
$ tail -c 1 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | xxd -p
0a
$ wc -l < docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
     488
$ git ls-files -s -- docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md | wc -l
       0
```
Both pre-edit hashes match the brief. Neither diff has a `<` line or a `c`/`d` hunk. The first L-1 lines are byte-identical, and so is the last line.

### 2. Re-run of every `$ command` in the inserted sections and in (c)
The checker extracts every fenced `$ ` line and the output lines pasted under it, then re-runs the command under bash and compares. Substitution modes:
- `sub`: `A=$PA` and `B=$PB`. Used for all fenced blocks in (a) 265-524, all fenced blocks in (b) 242-487, and (c) lines 1-349. These were captured before the edit.
- `cur`: `A` and `B` bound to the live files. Used for (c) 350-452 ("Edits made" and "Self-check"), which describe the post-edit state.
- `R` is (c) in both modes.

Each output line identifies the command by its artifact line number.
```
$ N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') python3 -I - <<'PYEOF' 2>&1 | N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/Fills are optimistic.*?assumed\./<S13>/g'
import subprocess, difflib
A='docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md'
B='docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md'
R='docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md'
PRE=r'''cd /Volumes/Sensidine/Praxis.build
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
R=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
'''
PRE_SUB = PRE + 'A=$PA\nB=$PB\n'
PRE_CUR = PRE + 'A='+A+'\nB='+B+'\n'
def blocks(path, lo, hi):
    L=open(path,encoding='utf-8').read().split('\n'); out=[]; cur=None
    for i in range(lo-1, hi):
        l=L[i]
        if l.startswith('```'):
            if cur is None: cur=[]
            else: out.append(cur); cur=None
        elif cur is not None: cur.append((i+1,l))
    return out
def cmds(blk):
    res=[]; c=None
    for ln,l in blk:
        if l.startswith('$ '):
            if c: res.append(c)
            c=[ln,l[2:],[]]
        elif c: c[2].append(l)
    if c: res.append(c)
    return res
plan=[('(a)',A,265,524,'sub'),('(b)',B,242,487,'sub'),('(c)',R,1,349,'sub'),('(c)',R,350,452,'cur')]
tot=0; bad=0; short=0
for tag,path,lo,hi,mode in plan:
    for blk in blocks(path,lo,hi):
        for ln,cmd,pasted in cmds(blk):
            tot+=1
            p=subprocess.run(['bash','-c',(PRE_SUB if mode=='sub' else PRE_CUR)+cmd],capture_output=True,text=True)
            s=p.stdout+p.stderr
            out=s.rstrip('\n').split('\n') if s else []
            same = out==pasted
            if len(pasted)<len(out): short+=1
            print(f"{tag}:{ln} [{mode}] pasted={len(pasted)} actual={len(out)} {'IDENTICAL' if same else 'DIFFERS'}")
            if not same:
                bad+=1
                print('      cmd: '+cmd)
                for d in difflib.unified_diff(pasted,out,'pasted','actual',lineterm='',n=0): print('      '+d)
print('commands checked:',tot,'differing:',bad,'pasted-shorter-than-actual:',short)
PYEOF
(a):285 [sub] pasted=1 actual=1 IDENTICAL
(a):287 [sub] pasted=1 actual=1 DIFFERS
      cmd: wc -l $B
      --- pasted
      +++ actual
      @@ -1 +1 @@
      -     242 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
      +     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
(a):289 [sub] pasted=1 actual=1 DIFFERS
      cmd: stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' $B
      --- pasted
      +++ actual
      @@ -1 +1 @@
      -2026-11-11T14:40:46
      +2026-11-11T17:08:51
(a):291 [sub] pasted=1 actual=1 IDENTICAL
(a):293 [sub] pasted=1 actual=1 IDENTICAL
(a):295 [sub] pasted=1 actual=1 IDENTICAL
(a):297 [sub] pasted=1 actual=1 IDENTICAL
(a):299 [sub] pasted=1 actual=1 IDENTICAL
(a):301 [sub] pasted=1 actual=1 IDENTICAL
(a):303 [sub] pasted=1 actual=1 IDENTICAL
(a):305 [sub] pasted=1 actual=2 DIFFERS
      cmd: git ls-files -s -- $B | wc -l
      --- pasted
      +++ actual
      @@ -1,0 +2 @@
      +fatal: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md' is outside repository at '/Volumes/Sensidine/Praxis.build'
(a):307 [sub] pasted=1 actual=2 DIFFERS
      cmd: git ls-tree HEAD -- $B | wc -l
      --- pasted
      +++ actual
      @@ -1,0 +2 @@
      +fatal: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md' is outside repository at '/Volumes/Sensidine/Praxis.build'
(a):309 [sub] pasted=1 actual=1 IDENTICAL
(a):311 [sub] pasted=1 actual=1 IDENTICAL
(a):321 [sub] pasted=3 actual=3 IDENTICAL
(a):325 [sub] pasted=1 actual=1 IDENTICAL
(a):327 [sub] pasted=3 actual=3 IDENTICAL
(a):331 [sub] pasted=1 actual=1 IDENTICAL
(a):333 [sub] pasted=1 actual=1 IDENTICAL
(a):335 [sub] pasted=1 actual=1 IDENTICAL
(a):337 [sub] pasted=1 actual=1 IDENTICAL
(a):339 [sub] pasted=1 actual=1 IDENTICAL
(a):349 [sub] pasted=9 actual=9 IDENTICAL
(a):359 [sub] pasted=1 actual=1 IDENTICAL
(a):364 [sub] pasted=2 actual=2 IDENTICAL
(a):367 [sub] pasted=1 actual=1 IDENTICAL
(a):369 [sub] pasted=43 actual=43 IDENTICAL
(a):413 [sub] pasted=1 actual=1 IDENTICAL
(a):415 [sub] pasted=1 actual=1 IDENTICAL
(a):417 [sub] pasted=1 actual=1 IDENTICAL
(a):419 [sub] pasted=3 actual=3 IDENTICAL
(a):423 [sub] pasted=1 actual=1 IDENTICAL
(a):425 [sub] pasted=1 actual=1 IDENTICAL
(a):427 [sub] pasted=1 actual=1 IDENTICAL
(a):429 [sub] pasted=1 actual=1 IDENTICAL
(a):431 [sub] pasted=1 actual=1 IDENTICAL
(a):433 [sub] pasted=1 actual=1 IDENTICAL
(a):435 [sub] pasted=1 actual=1 IDENTICAL
(a):437 [sub] pasted=5 actual=5 IDENTICAL
(a):443 [sub] pasted=1 actual=1 IDENTICAL
(a):445 [sub] pasted=4 actual=4 IDENTICAL
(a):450 [sub] pasted=1 actual=1 IDENTICAL
(a):455 [sub] pasted=11 actual=11 IDENTICAL
(a):467 [sub] pasted=1 actual=1 IDENTICAL
(a):469 [sub] pasted=11 actual=11 IDENTICAL
(a):481 [sub] pasted=1 actual=1 IDENTICAL
(a):508 [sub] pasted=2 actual=2 IDENTICAL
(a):511 [sub] pasted=3 actual=3 DIFFERS
      cmd: /tmp/vrf-c2/selfcheck.sh $A $B | M
      --- pasted
      +++ actual
      @@ -1,2 +1,2 @@
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
(a):515 [sub] pasted=1 actual=1 IDENTICAL
(a):517 [sub] pasted=2 actual=2 IDENTICAL
(a):520 [sub] pasted=1 actual=1 IDENTICAL
(b):262 [sub] pasted=9 actual=9 IDENTICAL
(b):272 [sub] pasted=1 actual=1 IDENTICAL
(b):276 [sub] pasted=2 actual=2 IDENTICAL
(b):279 [sub] pasted=1 actual=1 IDENTICAL
(b):281 [sub] pasted=43 actual=43 IDENTICAL
(b):325 [sub] pasted=1 actual=1 IDENTICAL
(b):327 [sub] pasted=1 actual=1 IDENTICAL
(b):329 [sub] pasted=1 actual=1 IDENTICAL
(b):331 [sub] pasted=3 actual=3 IDENTICAL
(b):335 [sub] pasted=1 actual=1 IDENTICAL
(b):337 [sub] pasted=1 actual=1 IDENTICAL
(b):339 [sub] pasted=1 actual=1 IDENTICAL
(b):341 [sub] pasted=1 actual=1 IDENTICAL
(b):343 [sub] pasted=1 actual=1 IDENTICAL
(b):345 [sub] pasted=1 actual=1 IDENTICAL
(b):347 [sub] pasted=1 actual=1 IDENTICAL
(b):349 [sub] pasted=5 actual=5 IDENTICAL
(b):355 [sub] pasted=1 actual=1 IDENTICAL
(b):357 [sub] pasted=4 actual=4 IDENTICAL
(b):362 [sub] pasted=1 actual=1 IDENTICAL
(b):366 [sub] pasted=11 actual=11 IDENTICAL
(b):378 [sub] pasted=1 actual=1 IDENTICAL
(b):380 [sub] pasted=11 actual=11 IDENTICAL
(b):392 [sub] pasted=1 actual=1 IDENTICAL
(b):408 [sub] pasted=1 actual=1 IDENTICAL
(b):410 [sub] pasted=1 actual=1 IDENTICAL
(b):412 [sub] pasted=1 actual=1 IDENTICAL
(b):414 [sub] pasted=1 actual=1 IDENTICAL
(b):416 [sub] pasted=1 actual=1 IDENTICAL
(b):418 [sub] pasted=1 actual=1 IDENTICAL
(b):420 [sub] pasted=2 actual=2 IDENTICAL
(b):423 [sub] pasted=1 actual=1 IDENTICAL
(b):425 [sub] pasted=8 actual=8 IDENTICAL
(b):434 [sub] pasted=1 actual=1 IDENTICAL
(b):436 [sub] pasted=1 actual=1 IDENTICAL
(b):438 [sub] pasted=18 actual=18 IDENTICAL
(b):457 [sub] pasted=1 actual=1 IDENTICAL
(b):459 [sub] pasted=1 actual=1 IDENTICAL
(b):461 [sub] pasted=1 actual=1 IDENTICAL
(b):471 [sub] pasted=2 actual=2 IDENTICAL
(b):474 [sub] pasted=3 actual=3 DIFFERS
      cmd: /tmp/vrf-c2/selfcheck.sh $A $B | M
      --- pasted
      +++ actual
      @@ -1,2 +1,2 @@
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
(b):478 [sub] pasted=1 actual=1 IDENTICAL
(b):480 [sub] pasted=2 actual=2 IDENTICAL
(b):483 [sub] pasted=1 actual=1 IDENTICAL
(c):34 [sub] pasted=1 actual=1 IDENTICAL
(c):36 [sub] pasted=1 actual=1 DIFFERS
      cmd: wc -l $B
      --- pasted
      +++ actual
      @@ -1 +1 @@
      -     242 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
      +     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
(c):38 [sub] pasted=1 actual=1 DIFFERS
      cmd: stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%S' $B
      --- pasted
      +++ actual
      @@ -1 +1 @@
      -2026-11-11T14:40:46
      +2026-11-11T17:08:51
(c):40 [sub] pasted=1 actual=1 IDENTICAL
(c):42 [sub] pasted=1 actual=1 IDENTICAL
(c):44 [sub] pasted=1 actual=1 IDENTICAL
(c):46 [sub] pasted=1 actual=1 IDENTICAL
(c):48 [sub] pasted=1 actual=1 IDENTICAL
(c):50 [sub] pasted=1 actual=1 IDENTICAL
(c):52 [sub] pasted=1 actual=1 IDENTICAL
(c):54 [sub] pasted=1 actual=2 DIFFERS
      cmd: git ls-files -s -- $B | wc -l
      --- pasted
      +++ actual
      @@ -1,0 +2 @@
      +fatal: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md' is outside repository at '/Volumes/Sensidine/Praxis.build'
(c):56 [sub] pasted=1 actual=2 DIFFERS
      cmd: git ls-tree HEAD -- $B | wc -l
      --- pasted
      +++ actual
      @@ -1,0 +2 @@
      +fatal: /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md' is outside repository at '/Volumes/Sensidine/Praxis.build'
(c):58 [sub] pasted=1 actual=1 IDENTICAL
(c):60 [sub] pasted=1 actual=1 IDENTICAL
(c):67 [sub] pasted=3 actual=3 IDENTICAL
(c):71 [sub] pasted=1 actual=1 IDENTICAL
(c):73 [sub] pasted=3 actual=3 IDENTICAL
(c):77 [sub] pasted=1 actual=1 IDENTICAL
(c):79 [sub] pasted=1 actual=1 IDENTICAL
(c):81 [sub] pasted=1 actual=1 IDENTICAL
(c):83 [sub] pasted=1 actual=1 IDENTICAL
(c):85 [sub] pasted=1 actual=1 IDENTICAL
(c):93 [sub] pasted=9 actual=9 IDENTICAL
(c):103 [sub] pasted=1 actual=1 IDENTICAL
(c):108 [sub] pasted=2 actual=2 IDENTICAL
(c):111 [sub] pasted=1 actual=1 IDENTICAL
(c):113 [sub] pasted=43 actual=43 IDENTICAL
(c):157 [sub] pasted=1 actual=1 IDENTICAL
(c):159 [sub] pasted=1 actual=1 IDENTICAL
(c):161 [sub] pasted=1 actual=1 IDENTICAL
(c):163 [sub] pasted=3 actual=3 IDENTICAL
(c):167 [sub] pasted=1 actual=1 IDENTICAL
(c):169 [sub] pasted=1 actual=1 IDENTICAL
(c):171 [sub] pasted=1 actual=1 IDENTICAL
(c):173 [sub] pasted=1 actual=1 IDENTICAL
(c):175 [sub] pasted=1 actual=1 IDENTICAL
(c):177 [sub] pasted=1 actual=1 IDENTICAL
(c):179 [sub] pasted=1 actual=1 IDENTICAL
(c):181 [sub] pasted=5 actual=5 IDENTICAL
(c):187 [sub] pasted=1 actual=1 IDENTICAL
(c):189 [sub] pasted=4 actual=4 IDENTICAL
(c):194 [sub] pasted=1 actual=1 IDENTICAL
(c):199 [sub] pasted=11 actual=11 IDENTICAL
(c):211 [sub] pasted=1 actual=1 IDENTICAL
(c):213 [sub] pasted=11 actual=11 IDENTICAL
(c):225 [sub] pasted=1 actual=1 IDENTICAL
(c):244 [sub] pasted=1 actual=1 IDENTICAL
(c):246 [sub] pasted=1 actual=1 IDENTICAL
(c):248 [sub] pasted=1 actual=1 IDENTICAL
(c):250 [sub] pasted=1 actual=1 IDENTICAL
(c):252 [sub] pasted=1 actual=1 IDENTICAL
(c):254 [sub] pasted=1 actual=1 IDENTICAL
(c):256 [sub] pasted=2 actual=2 IDENTICAL
(c):259 [sub] pasted=1 actual=1 IDENTICAL
(c):261 [sub] pasted=8 actual=8 IDENTICAL
(c):270 [sub] pasted=1 actual=1 IDENTICAL
(c):272 [sub] pasted=1 actual=1 IDENTICAL
(c):274 [sub] pasted=18 actual=18 IDENTICAL
(c):293 [sub] pasted=1 actual=1 IDENTICAL
(c):295 [sub] pasted=1 actual=1 IDENTICAL
(c):297 [sub] pasted=1 actual=1 IDENTICAL
(c):306 [sub] pasted=2 actual=2 IDENTICAL
(c):309 [sub] pasted=3 actual=3 DIFFERS
      cmd: /tmp/vrf-c2/selfcheck.sh $A $B | M
      --- pasted
      +++ actual
      @@ -1,2 +1,2 @@
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      -docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[265] last_nonblank_line=265 last_nonblank_is_S13=YES lines=265
      +/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[242] last_nonblank_line=242 last_nonblank_is_S13=YES lines=242
(c):313 [sub] pasted=1 actual=1 IDENTICAL
(c):315 [sub] pasted=2 actual=2 IDENTICAL
(c):318 [sub] pasted=1 actual=1 IDENTICAL
(c):325 [sub] pasted=20 actual=20 IDENTICAL
(c):346 [sub] pasted=1 actual=1 IDENTICAL
(c):355 [cur] pasted=1 actual=1 IDENTICAL
(c):357 [cur] pasted=1 actual=1 IDENTICAL
(c):359 [cur] pasted=1 actual=1 IDENTICAL
(c):361 [cur] pasted=1 actual=1 IDENTICAL
(c):363 [cur] pasted=3 actual=3 IDENTICAL
(c):367 [cur] pasted=1 actual=1 IDENTICAL
(c):369 [cur] pasted=1 actual=1 IDENTICAL
(c):371 [cur] pasted=1 actual=1 IDENTICAL
(c):373 [cur] pasted=1 actual=1 IDENTICAL
(c):375 [cur] pasted=1 actual=1 IDENTICAL
(c):377 [cur] pasted=1 actual=1 IDENTICAL
(c):379 [cur] pasted=1 actual=1 IDENTICAL
(c):381 [cur] pasted=1 actual=1 IDENTICAL
(c):383 [cur] pasted=1 actual=1 IDENTICAL
(c):385 [cur] pasted=2 actual=2 IDENTICAL
(c):388 [cur] pasted=1 actual=1 IDENTICAL
(c):390 [cur] pasted=1 actual=1 IDENTICAL
(c):392 [cur] pasted=1 actual=1 IDENTICAL
(c):394 [cur] pasted=1 actual=1 IDENTICAL
(c):396 [cur] pasted=1 actual=1 IDENTICAL
(c):404 [cur] pasted=1 actual=1 IDENTICAL
(c):406 [cur] pasted=4 actual=4 IDENTICAL
(c):411 [cur] pasted=1 actual=1 IDENTICAL
(c):413 [cur] pasted=3 actual=3 IDENTICAL
(c):417 [cur] pasted=1 actual=1 IDENTICAL
(c):419 [cur] pasted=1 actual=1 IDENTICAL
(c):421 [cur] pasted=1 actual=1 IDENTICAL
(c):423 [cur] pasted=1 actual=1 IDENTICAL
(c):425 [cur] pasted=1 actual=1 IDENTICAL
(c):427 [cur] pasted=1 actual=1 IDENTICAL
(c):429 [cur] pasted=1 actual=1 IDENTICAL
(c):431 [cur] pasted=1 actual=1 IDENTICAL
(c):436 [cur] pasted=1 actual=1 IDENTICAL
commands checked: 196 differing: 11 pasted-shorter-than-actual: 4
```
All 11 differences come from my substitution, not from the artifacts:
- `wc -l $B` and the selfcheck rows print the /tmp/c2pre path instead of the repo path. The counts are identical.
- `stat $B` gives the copy's mtime (17:08:51), not the live file's. The live (b) has since been edited, so its 14:40:46 mtime can no longer be re-observed (live mtime below).
- The four "pasted-shorter" cases are the `git ls-files` and `git ls-tree` runs. Git refuses a path outside the repo, so it adds a `fatal:` line. Re-run on the live (b):
```
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" $B
2026-11-11T17:16:43
$ git ls-files -s -- $B | wc -l
       0
$ git ls-tree HEAD -- $B | wc -l
       0
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | wc -l
       1
$ ls /Users/admin/.claude/file-history | wc -l
      34
$ grep -rlF "Result: PENDING" /Users/admin/.claude/file-history 2>/dev/null | wc -l
       0
```
The repogrep and MANIFEST blocks all re-ran IDENTICAL. The repo-wide counts did not change after (a), (b) and (c) were written, which is consistent with their name count being 0.

### 3. Every `| wc -l` figure against the rows listed above it
```
$ python3 -I - <<'PY'
import re
files=[('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md',265,524),('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md',242,487),('docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md',1,452)]
for p,lo,hi in files:
    L=open(p,encoding='utf-8').read().split('\n')
    cmds=[]; cur=None; infence=False
    for i in range(lo-1,hi):
        l=L[i]
        if l.startswith('```'):
            infence=not infence
            if cur: cmds.append(cur); cur=None
            continue
        if not infence: continue
        if l.startswith('$ '):
            if cur: cmds.append(cur)
            cur=[i+1,l[2:],[]]
        elif cur: cur[2].append(l)
    d={c[1]:c for c in cmds}
    for ln,cmd,out in cmds:
        m=re.match(r'(.*) \| wc -l$',cmd)
        if m and m.group(1) in d:
            src=d[m.group(1)]
            print('%s:%d wc=%s listed_rows=%d (from :%d) %s' % (p.split('/')[-1][-30:],ln,out[0].strip(),len(src[2]),src[0],'OK' if int(out[0])==len(src[2]) else 'MISMATCH'))
        elif m:
            print('%s:%d wc=%s no listed source in block (count-only)' % (p.split('/')[-1][-30:],ln,out[0].strip()))
PY
filing-correction-1-worker1.md:299 wc=1 no listed source in block (count-only)
filing-correction-1-worker1.md:305 wc=0 no listed source in block (count-only)
filing-correction-1-worker1.md:307 wc=0 no listed source in block (count-only)
filing-correction-1-worker1.md:325 wc=3 listed_rows=3 (from :321) OK
filing-correction-1-worker1.md:331 wc=3 listed_rows=3 (from :327) OK
filing-correction-1-worker1.md:359 wc=9 listed_rows=9 (from :349) OK
filing-correction-1-worker1.md:364 wc=check-ignore rc=0 no listed source in block (count-only)
filing-correction-1-worker1.md:413 wc=43 listed_rows=43 (from :369) OK
filing-correction-1-worker1.md:423 wc=3 listed_rows=3 (from :419) OK
filing-correction-1-worker1.md:429 wc=46 no listed source in block (count-only)
filing-correction-1-worker1.md:443 wc=5 listed_rows=5 (from :437) OK
filing-correction-1-worker1.md:450 wc=4 listed_rows=4 (from :445) OK
filing-correction-1-worker1.md:467 wc=11 no listed source in block (count-only)
filing-correction-1-worker1.md:481 wc=11 no listed source in block (count-only)
filing-correction-1-worker1.md:515 wc=3 listed_rows=3 (from :511) OK
filing-correction-1-worker1.md:520 wc=2 listed_rows=2 (from :517) OK
filing-correction-1-manager.md:272 wc=9 listed_rows=9 (from :262) OK
filing-correction-1-manager.md:276 wc=check-ignore rc=0 no listed source in block (count-only)
filing-correction-1-manager.md:325 wc=43 listed_rows=43 (from :281) OK
filing-correction-1-manager.md:335 wc=3 listed_rows=3 (from :331) OK
filing-correction-1-manager.md:341 wc=46 no listed source in block (count-only)
filing-correction-1-manager.md:355 wc=5 listed_rows=5 (from :349) OK
filing-correction-1-manager.md:362 wc=4 listed_rows=4 (from :357) OK
filing-correction-1-manager.md:378 wc=11 no listed source in block (count-only)
filing-correction-1-manager.md:392 wc=11 no listed source in block (count-only)
filing-correction-1-manager.md:414 wc=379 no listed source in block (count-only)
filing-correction-1-manager.md:423 wc=2 listed_rows=2 (from :420) OK
filing-correction-1-manager.md:434 wc=8 listed_rows=8 (from :425) OK
filing-correction-1-manager.md:457 wc=18 listed_rows=18 (from :438) OK
filing-correction-1-manager.md:461 wc=0 no listed source in block (count-only)
filing-correction-1-manager.md:478 wc=3 listed_rows=3 (from :474) OK
filing-correction-1-manager.md:483 wc=2 listed_rows=2 (from :480) OK
filing-correction-2-worker1.md:48 wc=1 no listed source in block (count-only)
filing-correction-2-worker1.md:54 wc=0 no listed source in block (count-only)
filing-correction-2-worker1.md:56 wc=0 no listed source in block (count-only)
filing-correction-2-worker1.md:71 wc=3 listed_rows=3 (from :67) OK
filing-correction-2-worker1.md:77 wc=3 listed_rows=3 (from :73) OK
filing-correction-2-worker1.md:103 wc=9 listed_rows=9 (from :93) OK
filing-correction-2-worker1.md:108 wc=check-ignore rc=0 no listed source in block (count-only)
filing-correction-2-worker1.md:157 wc=43 listed_rows=43 (from :113) OK
filing-correction-2-worker1.md:167 wc=3 listed_rows=3 (from :163) OK
filing-correction-2-worker1.md:173 wc=46 no listed source in block (count-only)
filing-correction-2-worker1.md:187 wc=5 listed_rows=5 (from :181) OK
filing-correction-2-worker1.md:194 wc=4 listed_rows=4 (from :189) OK
filing-correction-2-worker1.md:211 wc=11 no listed source in block (count-only)
filing-correction-2-worker1.md:225 wc=11 no listed source in block (count-only)
filing-correction-2-worker1.md:250 wc=379 no listed source in block (count-only)
filing-correction-2-worker1.md:259 wc=2 listed_rows=2 (from :256) OK
filing-correction-2-worker1.md:270 wc=8 listed_rows=8 (from :261) OK
filing-correction-2-worker1.md:293 wc=18 listed_rows=18 (from :274) OK
filing-correction-2-worker1.md:297 wc=0 no listed source in block (count-only)
filing-correction-2-worker1.md:313 wc=3 listed_rows=3 (from :309) OK
filing-correction-2-worker1.md:318 wc=2 listed_rows=2 (from :315) OK
filing-correction-2-worker1.md:346 wc=20 listed_rows=20 (from :325) OK
filing-correction-2-worker1.md:357 wc=1 listed_rows=1 (from :355) OK
filing-correction-2-worker1.md:367 wc=3 listed_rows=3 (from :363) OK
filing-correction-2-worker1.md:379 wc=1 listed_rows=1 (from :377) OK
filing-correction-2-worker1.md:388 wc=2 listed_rows=2 (from :385) OK
filing-correction-2-worker1.md:411 wc=4 listed_rows=4 (from :406) OK
filing-correction-2-worker1.md:417 wc=3 listed_rows=3 (from :413) OK
```
There is no MISMATCH. The count-only rows are as follows:
- `find ... | wc -l` = 11 is paired with the `| LC_ALL=C sort | M` listing directly above it, which has 11 rows.
- `repogrep.sh nw | wc -l` = 46 has no pasted listing of its own. The listing is derivable from what is pasted: the 43 whole-word rows, plus the 3 rows added in the pasted `diff`, gives 46. The `join` pairs all 43 shared paths:
```
$ join -t: <(/tmp/vrf-c2/repogrep.sh w | sort) <(/tmp/vrf-c2/repogrep.sh nw | sort) | wc -l
      43
```

### 4. Are the (c) blocks byte-identical to the (a) and (b) blocks? (claim at (c):20)
```
$ python3 -I - <<'PY'
def blocks(path, lo=1, hi=None):
    L=open(path,encoding='utf-8').read().split('\n'); hi=hi or len(L)
    out=[]; cur=None
    for i in range(lo-1,hi):
        l=L[i]
        if l.startswith('```'):
            if cur is None: cur=[]; s=i+1
            else: out.append((s,'\n'.join(cur))); cur=None
        elif cur is not None: cur.append(l)
    return out
a=blocks('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md',265,524)
b=blocks('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md',242,487)
c=blocks('docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md',1,349)
print('blocks: a=%d b=%d c(1-349)=%d' % (len(a),len(b),len(c)))
for s,x in c:
    print('(c) block at :%d lines=%d in(a)=%s in(b)=%s' % (s, x.count('\n')+1, [t for t,y in a if y==x], [t for t,y in b if y==x]))
PY
blocks: a=7 b=6 c(1-349)=9
(c) block at :23 lines=6 in(a)=[270] in(b)=[247]
(c) block at :33 lines=28 in(a)=[284] in(b)=[]
(c) block at :66 lines=20 in(a)=[320] in(b)=[]
(c) block at :92 lines=12 in(a)=[348] in(b)=[261]
(c) block at :107 lines=88 in(a)=[363] in(b)=[275]
(c) block at :198 lines=28 in(a)=[454] in(b)=[365]
(c) block at :243 lines=55 in(a)=[] in(b)=[407]
(c) block at :305 lines=14 in(a)=[507] in(b)=[470]
(c) block at :324 lines=23 in(a)=[] in(b)=[]
```
Every (c) block in sections 1-5 has an exact twin in (a) or (b). The block at :324 (the script listing, section 6) is unique to (c).

### 5. Quoted original wording against the pre-edit copies
```
$ sed -n 40p $PA
DECISIONS.md lines:     2203
$ sed -n 207p $PA
### 7. C5 correction-1 manager report as read (cat -n, masked)
$ sed -n 209p $PA
name hits: 0
$ sed -n 210p $PA
      27 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
$ sed -n 211p $PA
2026-11-11T14:33:58
$ sed -n 218p $PA
All nine sections read `(pending)`. Lines 1-14 and 17-26 were elided above, and every one of them is a header, a blank line, or `(pending)`.
$ sed -n 222p $PA
== out-of-scope observation: /tmp/vrf-c1 helper files
$ sed -n 223p $PA
/tmp/vrf-c1/count.sh: 0
$ sed -n 224p $PA
/tmp/vrf-c1/diffs.txt: 0
$ sed -n 225p $PA
/tmp/vrf-c1/s13.py: 0
$ sed -n 226p $PA
== DECISIONS.md lines 1-2099 whole-word: 0
$ sed -n 228p $PA
A repo-wide `grep -rIlwi` found the name in many other files, outside the C1 set. Excerpt of the masked output:
$ sed -n 238p $PA
./docs/reports/2026-10-28-f4-<NAME>-reply-filing.md: 
$ sed -n 239p $PA
./docs/reports/2026-10-28-f4-<NAME>-reply-worker1.md: 
$ sed -n 240p $PA
... (about 45 files in total; the run was cut off by head -40)
$ sed -n 242p $PA
The blank counts on the `2026-10-28-f4-<NAME>-reply-*.md` rows come from a bug in my loop: I fed masked filenames back into grep, which then printed "No such file or directory". The rows still prove that at least 11 report **filenames** in docs/reports/ contain the name. I did not check whether a 4-letter whole-word match in the agent-memory files is the name itself or a common English word.
$ sed -n 250p $PA
- **C5 NOT GRADABLE (skeleton).** When I read the correction-1 manager report (mtime 14:33:58), its "Verification evidence (command output)" section was `(pending)` and the Result was `PENDING`. As the brief instructs, only C1-C4 are graded.
$ sed -n 252p $PA
Out of scope, reported and not fixed: the name still appears in at least 11 report filenames (`docs/reports/2026-10-28-f4-<NAME>-reply-*.md`) and in the body of many other reports. Anyone with the repo can recover it, which makes the "filename withheld" placeholder largely cosmetic outside the C1 file set.
$ sed -n 257p $PA
Self-check on this report. I ran it on the file as first written, before this block existed, and again after inserting it.
$ sed -n 261p $PA
V1 on own report done
$ sed -n 262p $PA
S13 lines containing: 1  standalone: 1  last nonblank is S13: 1
$ sed -n 263p $PA | od -c
0000000    `   `   `  \n                                                
0000004
$ sed -n 206p $PB
$ python3 -I /tmp/vrf-c1/s13.py <two new reports>
$ sed -n 207p $PB
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
$ sed -n 208p $PB
2026-11-11-v-rulings-filing-correction-1-worker1.md standalone_outside_fence=1 at=[265] in_fence=0 last_nonblank_line=265 is_last=True substring_lines=1
$ sed -n 213p $PB
$ /tmp/vrf-c1/count.sh <two new reports> | tail -3; python3 -I /tmp/vrf-c1/s13.py <this report>   (re-run after pasting the block above)
$ sed -n 217p $PB
2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
$ sed -n 228p $PB
Out of scope for this unit, for the master to decide. Worker1 section 8 found the name, masked in its output, in at least 11 filenames under docs/reports/ of the form `2026-10-28-f4-<NAME>-reply-*.md`. It also found it in the body of many earlier reports and in three files under .claude/agent-memory/. Worker1 did not confirm whether the agent-memory hits are the name or a common word that happens to match. While those files exist, the "filename withheld" placeholder does not stop anyone with the repo from recovering the name. This unit's hard limits forbid touching those files, so I changed nothing there.
$ sed -n 238p $PB
- MANIFEST.md: rows 404 and 405 appended.
```
Line 263 of $PA is a bare code fence, so it is shown through `od -c` to keep this block intact. The other 28 rows came from one loop, `for n in 40 207 ... 263; do printf "\$ sed -n %sp \$PA\n" $n; sed -n "${n}p" $PA; done` and the same loop for $PB over 206 207 208 213 217 228 238. Its output was piped through the name and S13 mask. The `od -c` row was run separately.

Every quoted wording matches its line, with two whitespace or marker differences (Finding 6):
- (a):281 quotes :210 without its 6 leading spaces.
- (b):405 quotes :238 without the leading `- `.

The (a):281 count "Only 3 of the 27 lines were pasted" matches :213, :214 and :216. The 10-row excerpt at :230-239 is correct, and all 10 paths appear in the re-run 43-row list.

### 6. Is the skeleton really not re-runnable? (claim at (a):314 and (c):63)
The C2.1 search covered only /tmp, /private/tmp and git. The Claude Code session transcripts on this machine are machine-local and unversioned. Searched for the Write tool call that created the manager report:
```
$ cd /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build && find . -name '*.jsonl' -newermt '2026-11-11 12:00' 2>/dev/null | wc -l; find . -name '*.jsonl' -newermt '2026-11-11 12:00' 2>/dev/null | xargs grep -lF 'Result: PENDING' 2>/dev/null | while read -r f; do printf '%s hits=%s corr1mgr_write=%s\n' "$f" "$(grep -cF 'Result: PENDING' "$f")" "$(grep -F 'Result: PENDING' "$f" | grep -cF 'v-rulings-filing-correction-1-manager.md')"; done
      41
./70d84e75-8dec-499b-b88a-215626eebb89.jsonl hits=3 corr1mgr_write=3
./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-a28ce5ae8c803f99e.jsonl hits=3 corr1mgr_write=2
./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl hits=3 corr1mgr_write=3
./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-ae6bf20091d4176fe.jsonl hits=3 corr1mgr_write=3
./70d84e75-8dec-499b-b88a-215626eebb89/subagents/agent-a5b585c2515165043.jsonl hits=1 corr1mgr_write=1
./70d84e75-8dec-499b-b88a-215626eebb89/subagents/agent-a6d61175cced0b0fa.jsonl hits=6 corr1mgr_write=2
./70d84e75-8dec-499b-b88a-215626eebb89/subagents/agent-a27bdd123e733df38.jsonl hits=4 corr1mgr_write=2
$ find . -name '*.jsonl' -newermt '2026-11-11 12:00' -print0 | xargs -0 python3 -I -c '
import sys, json
for p in sys.argv[1:]:
    for ln in open(p, encoding="utf-8", errors="replace"):
        try: o=json.loads(ln)
        except Exception: continue
        m=o.get("message") or {}
        c=m.get("content")
        if not isinstance(c,list): continue
        for it in c:
            if isinstance(it,dict) and it.get("type")=="tool_use":
                inp=it.get("input") or {}
                fp=str(inp.get("file_path",""))
                if fp.endswith("v-rulings-filing-correction-1-manager.md"):
                    txt=inp.get("content") or inp.get("new_string") or ""
                    L=txt.split("\n")
                    print(p.split("/")[-1][:30], o.get("timestamp"), it.get("name"), "chars=%d lines=%d pending_lines=%d hdr2=%d PENDING=%d" % (len(txt), txt.count("\n"), sum(1 for x in L if x.strip()=="(pending)"), sum(1 for x in L if x.startswith("## ")), txt.count("PENDING")))
'
70d84e75-8dec-499b-b88a-215626 2026-11-11T22:08:08.274Z Read chars=0 lines=0 pending_lines=0 hdr2=0 PENDING=0
70d84e75-8dec-499b-b88a-215626 None Read chars=0 lines=0 pending_lines=0 hdr2=0 PENDING=0
agent-abe49d634e60ac82e.jsonl 2026-11-11T19:33:58.402Z Write chars=365 lines=27 pending_lines=8 hdr2=8 PENDING=1
agent-abe49d634e60ac82e.jsonl None Write chars=365 lines=27 pending_lines=8 hdr2=8 PENDING=1
```
(The 70d84e75 rows are this session's own Read calls.) The Write at 2026-11-11T19:33:58.402Z is the skeleton. Its full content, masked:
```
$ N=$(ls /Volumes/Sensidine/Praxis.build/docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') python3 -I -c '
import json, os, re, glob
N=os.environ["N"]
p=glob.glob("./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl")[0]
seen=False
for ln in open(p, encoding="utf-8"):
    o=json.loads(ln)
    c=(o.get("message") or {}).get("content")
    if not isinstance(c,list): continue
    for it in c:
        if isinstance(it,dict) and it.get("type")=="tool_use" and str((it.get("input") or {}).get("file_path","")).endswith("v-rulings-filing-correction-1-manager.md") and not seen:
            seen=True
            inp=it["input"]; txt=inp["content"]
            print("timestamp", o.get("timestamp"), "tool", it["name"], "file_path", inp["file_path"])
            print("name_ci_count", len(re.findall(re.escape(N), txt, re.I)))
            print("ends_with_newline", txt.endswith("\n"))
            for i,l in enumerate(txt.split("\n"),1):
                print("%4d\t%s" % (i, re.sub(re.escape(N), "<NAME>", l, flags=re.I)))
'
timestamp 2026-11-11T19:33:58.402Z tool Write file_path /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
name_ci_count 0
ends_with_newline True
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
  28	
```
(Row 28 is the empty string after the final newline, printed by `split("\n")`.) Here are the (a) section 7 checks, re-run on that recovered content. `SK` prints the Write's `input.content` to stdout. Run from the transcript directory, under bash, with `run` masking the name. In the second run, `SK` also printed the Write's timestamp to stderr:
```
$ SK() { python3 -I -c '
import json
p="./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl"
for ln in open(p, encoding="utf-8"):
    o=json.loads(ln); c=(o.get("message") or {}).get("content")
    if isinstance(c,list):
        for it in c:
            if isinstance(it,dict) and it.get("type")=="tool_use" and str((it.get("input") or {}).get("file_path","")).endswith("v-rulings-filing-correction-1-manager.md"):
                print(it["input"]["content"], end=""); raise SystemExit
'; }
$ SK | wc -l
      27
$ SK | grep -c "^## "
8
$ SK | grep -cx "(pending)"
8
$ SK | grep -c "PENDING"
1
$ SK | grep -ci -- "$N"
0
$ SK | grep -vnxE "|#+ .*|\(pending\)"
grep: empty (sub)expression
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
$ SK | shasum -a 256
e45ec8e6215df41ac1523ee51d14452a872ec1ad04d746e70988380cbf10f9a4  -
$ SK 2>/dev/null | sed -n "1,14p;17,26p" | grep -vcE "^$|^#+ |^\(pending\)$"
0
$ SK 2>/dev/null | sed -n "15,16p;27p"
## Verification evidence (command output)
(pending)
Result: PENDING
$ SK 2>&1 >/dev/null
2026-11-11T19:33:58.402Z
$ date -j -u -f "%Y-%m-%dT%H:%M:%S" "2026-11-11T19:33:58" +%s | xargs -I{} date -r {} "+%Y-%m-%dT%H:%M:%S %Z"
2026-11-11T14:33:58 EST
```
(The grep on the sixth command was a malformed pattern of mine. It is replaced by the `grep -vcE` command after it.)

The results, claim by claim:
- (a):210, 27 lines: holds.
- (a):211, mtime 14:33:58: holds (the Write was at 14:33:58 EST).
- (a):213-216, lines 15, 16 and 27: hold.
- (a):218, lines 1-14 and 17-26 are all header, blank or `(pending)`: holds.
- (a):209, name hits 0: holds.
- (a):218, "All nine sections read `(pending)`": **false**. There are 8 `## ` sections and 8 `(pending)` lines. The other two headers do not read `(pending)`: the `#` title has no section body, and line 27 is `Result: PENDING`.

The original outputs behind (b):207 and (b):217 are also in a transcript, as real Bash tool results:
```
$ find . -name '*.jsonl' -newermt '2026-11-11 12:00' ! -path './70d84e75-8dec-499b-b88a-215626eebb89.jsonl' -print0 | xargs -0 python3 -I -c '
import sys, json
pat=["correction-1-manager.md standalone_outside_fence=1 at=[210]","correction-1-manager.md standalone_outside_fence=1 at=[235]"]
for p in sys.argv[1:]:
    for ln in open(p, encoding="utf-8", errors="replace"):
        try: o=json.loads(ln)
        except Exception: continue
        c=(o.get("message") or {}).get("content")
        if not isinstance(c,list): continue
        for it in c:
            if isinstance(it,dict) and it.get("type")=="tool_result":
                cc=it.get("content"); s=json.dumps(cc) if not isinstance(cc,str) else cc
                for q in pat:
                    if q in s: print(p.split("/")[-1][:32], o.get("timestamp"), "tool_result contains:", q.split(" ")[-1])
'
agent-abe49d634e60ac82e.jsonl 2026-11-11T19:40:29.560Z tool_result contains: at=[210]
agent-abe49d634e60ac82e.jsonl 2026-11-11T19:40:37.235Z tool_result contains: at=[235]
agent-abe49d634e60ac82e.jsonl 2026-11-11T19:40:47.219Z tool_result contains: at=[235]
agent-a28ce5ae8c803f99e.jsonl 2026-11-11T19:42:39.407Z tool_result contains: at=[210]
agent-a28ce5ae8c803f99e.jsonl 2026-11-11T19:42:39.407Z tool_result contains: at=[235]
agent-a5b585c2515165043.jsonl 2026-11-11T22:10:54.025Z tool_result contains: at=[210]
agent-a5b585c2515165043.jsonl 2026-11-11T22:10:54.025Z tool_result contains: at=[235]
agent-a5b585c2515165043.jsonl 2026-11-11T22:12:51.087Z tool_result contains: at=[210]
agent-a6d61175cced0b0fa.jsonl 2026-11-11T22:08:58.179Z tool_result contains: at=[210]
agent-a6d61175cced0b0fa.jsonl 2026-11-11T22:08:58.179Z tool_result contains: at=[235]
agent-a27bdd123e733df38.jsonl 2026-11-11T22:21:33.233Z tool_result contains: at=[210]
agent-a27bdd123e733df38.jsonl 2026-11-11T22:21:33.233Z tool_result contains: at=[235]
agent-a27bdd123e733df38.jsonl 2026-11-11T22:22:44.377Z tool_result contains: at=[210]
agent-a27bdd123e733df38.jsonl 2026-11-11T22:22:44.377Z tool_result contains: at=[235]
agent-a27bdd123e733df38.jsonl 2026-11-11T22:26:13.286Z tool_result contains: at=[210]
$ N=$(ls /Volumes/Sensidine/Praxis.build/docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//') python3 -I -c '
import json, re, os, glob
N=os.environ["N"]
p=glob.glob("./365cca85-6a45-4395-899d-9b204327f164/subagents/agent-abe49d634e60ac82e.jsonl")[0]
uses={}
for ln in open(p, encoding="utf-8"):
    o=json.loads(ln); c=(o.get("message") or {}).get("content")
    if not isinstance(c,list): continue
    for it in c:
        if not isinstance(it,dict): continue
        if it.get("type")=="tool_use": uses[it["id"]]=(it["name"], json.dumps(it.get("input"))[:400])
        if it.get("type")=="tool_result" and o.get("timestamp") in ("2026-11-11T19:40:29.560Z","2026-11-11T19:40:37.235Z"):
            cc=it.get("content"); s=cc if isinstance(cc,str) else "\n".join(x.get("text","") for x in cc if isinstance(x,dict))
            u=uses.get(it.get("tool_use_id"))
            print("== ts", o.get("timestamp"), "tool", u[0] if u else None)
            print("cmd:", re.sub(re.escape(N),"<NAME>",u[1] if u else "",flags=re.I).replace("Fills are optimistic","<S13 start>"))
            for l in s.split("\n"):
                if "correction-1-manager.md standalone" in l or "s13" in l.lower(): print("out:", re.sub(re.escape(N),"<NAME>",l,flags=re.I))
'
== ts 2026-11-11T19:40:29.560Z tool Bash
cmd: {"command": "{ echo '$ /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md'; /tmp/vrf-c1/count.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md; echo '$ python3 -I /tmp/vrf-c1/s13.py <two new reports>'; python3 -I /tm
out: $ python3 -I /tmp/vrf-c1/s13.py <two new reports>
out: 2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[210] in_fence=0 last_nonblank_line=210 is_last=True substring_lines=1
== ts 2026-11-11T19:40:37.235Z tool Bash
cmd: {"command": "export SC=\"$(cat /tmp/vrf-c1/selfcheck.txt)\" && python3 -I -c '\nimport os\nf=\"docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md\"\nb=open(f,encoding=\"utf-8\").read(); assert b.count(\"SELFCHECK_PLACEHOLDER\")==1\nb=b.replace(\"SELFCHECK_PLACEHOLDER\",\"Run on this report with this section still a placeholder. The re-run after pasting is the last block in this secti
out: 2026-11-11-v-rulings-filing-correction-1-manager.md standalone_outside_fence=1 at=[235] in_fence=0 last_nonblank_line=235 is_last=True substring_lines=1
```
(The `cmd:` field is cut to 400 characters by my own print, `[:400]`. This is a display limit of the label, not truncation of the result lines, which are printed in full.)

### 7. Name leak (a), (b), (c), and the /tmp/vrf-c2 helpers
```
$ echo "len=${#N}"
len=4
$ for f in $A $B $R; do echo "$f grep-ci=$(grep -ci -- "$N" $f)"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md grep-ci=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md grep-ci=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md grep-ci=0
$ for f in $A $B $R; do echo "$f split-detector-hit-lines=$(perl -CSD -Mutf8 -ne "$DET" $f)"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md split-detector-hit-lines=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md split-detector-hit-lines=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md split-detector-hit-lines=0
$ printf "x %s y\n" "$(echo "$N" | sed "s/./&. /g")" | perl -CSD -Mutf8 -ne "$DET" | sed "s/^/positive-control(dot-space split) hit-lines=/"
positive-control(dot-space split) hit-lines=1
$ printf "x %s y\n" "$(echo "$N" | perl -CSD -pe "chomp; s/(.)/\$1\x{200B}/g")" | perl -CSD -Mutf8 -ne "$DET" | sed "s/^/positive-control(zero-width split) hit-lines=/"
positive-control(zero-width split) hit-lines=1
$ printf "x %s y\n" "$(echo "$N" | tr a-z A-Z)" | perl -CSD -Mutf8 -ne "$DET" | sed "s/^/positive-control(upper) hit-lines=/"
positive-control(upper) hit-lines=1
$ printf "nothing here\n" | perl -CSD -Mutf8 -ne "$DET" | sed "s/^/negative-control hit-lines=/"
negative-control hit-lines=0
$ for f in $A $B $R; do echo "$f reversed-ci=$(grep -ci -- "$(echo "$N" | rev)" $f)"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md reversed-ci=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md reversed-ci=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md reversed-ci=0
$ for f in $A $B $R; do echo "$f base64=$(grep -c -- "$(printf %s "$N" | base64 | tr -d =)" $f) urlenc-first-char=$(grep -ci -- "%$(printf %s "${N:0:1}" | xxd -p)" $f)"; done
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md base64=0 urlenc-first-char=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md base64=0 urlenc-first-char=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md base64=0 urlenc-first-char=0
$ for s in /tmp/vrf-c2/selfcheck.sh "/tmp/vrf-c2/repogrep.sh w" "/tmp/vrf-c2/repogrep.sh nw"; do echo "$s raw-output-name-count=$($s $A $B $R 2>&1 | grep -ci -- "$N")"; done
/tmp/vrf-c2/selfcheck.sh raw-output-name-count=0
/tmp/vrf-c2/repogrep.sh w raw-output-name-count=0
/tmp/vrf-c2/repogrep.sh nw raw-output-name-count=0
$ for s in edits_cmds.sh selfcheck_cmds.sh script_cmds.sh; do echo "$s raw-output-name-count=$(bash /tmp/vrf-c2/$s 2>&1 | grep -ci -- "$N")"; done
edits_cmds.sh raw-output-name-count=0
selfcheck_cmds.sh raw-output-name-count=0
script_cmds.sh raw-output-name-count=0
$ for s in gen_a.sh gen_b.sh; do echo "$s contains-lines-with-name=$(grep -ci -- "$N" /tmp/vrf-c2/$s)"; done
gen_a.sh contains-lines-with-name=0
gen_b.sh contains-lines-with-name=0
$ for f in /tmp/vrf-c2/*; do echo "$f name-lines=$(grep -ci -- "$N" "$f")"; done
/tmp/vrf-c2/allblocks.txt name-lines=0
/tmp/vrf-c2/blocks.py name-lines=0
/tmp/vrf-c2/common_intro.sh name-lines=0
/tmp/vrf-c2/edits_block.txt name-lines=0
/tmp/vrf-c2/edits_cmds.sh name-lines=0
/tmp/vrf-c2/gen_a.err name-lines=0
/tmp/vrf-c2/gen_a.sh name-lines=0
/tmp/vrf-c2/gen_b.err name-lines=0
/tmp/vrf-c2/gen_b.sh name-lines=0
/tmp/vrf-c2/gen_report.py name-lines=0
/tmp/vrf-c2/insert.py name-lines=0
/tmp/vrf-c2/lib.sh name-lines=0
/tmp/vrf-c2/nw.txt name-lines=0
/tmp/vrf-c2/repogrep.sh name-lines=0
/tmp/vrf-c2/sc_new.txt name-lines=0
/tmp/vrf-c2/script_block.txt name-lines=0
/tmp/vrf-c2/script_cmds.sh name-lines=0
/tmp/vrf-c2/sec_a.md name-lines=0
/tmp/vrf-c2/sec_b.md name-lines=0
/tmp/vrf-c2/selfcheck.sh name-lines=0
/tmp/vrf-c2/selfcheck_block.txt name-lines=0
/tmp/vrf-c2/selfcheck_cmds.sh name-lines=0
/tmp/vrf-c2/w.txt name-lines=0
```
`DET` is `BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n, "\n" }`. Its controls are synthetic stdin lines, never printed.

Is the name an ordinary word? If it were, whole-word hits might not be the name. Dictionary check:
```
$ grep -cix -- "$N" /usr/share/dict/words
0
$ grep -cx -- "$N" /usr/share/dict/words
0
$ grep -ci -- "$N" /usr/share/dict/words
14
$ find . -path ./.git -prune -o -type l -print | wc -l
       0
```
There are no symlinks in the repo, so `grep -r` (which does not follow symlinks) missed nothing.

### 8. Other PII and S13 structure, whole files (a), (b), (c)
```
$ grep -nE "([0-9]{1,3}\.){3}[0-9]{1,3}" $A $B $R; echo "rc=$?"
rc=1
$ grep -nE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" $A $B $R; echo "rc=$?"
rc=1
$ grep -niE "([0-9a-f]{2}[:-]){5}[0-9a-f]{2}" $A $B $R; echo "rc=$?"
rc=1
$ grep -niE "id_rsa|id_ed25519|id_ecdsa|\.pem\b|\.ssh/|\.key\b|BEGIN [A-Z ]*PRIVATE" $A $B $R; echo "rc=$?"
rc=1
$ grep -c . $A $B $R
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:491
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md:456
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md:431
$ python3 -I - "$A" "$B" "$R" <<'PY'
import sys
S="Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage"+" assumed."
rng={"worker1.md":(265,524),"manager.md":(242,487)}
for p in sys.argv[1:]:
    L=open(p,encoding="utf-8").read().split("\n")
    if L and L[-1]=="": L=L[:-1]
    fence=False; sa=[]; inf=[]; sub=[]; bul=[]
    for i,l in enumerate(L,1):
        if l.lstrip().startswith("`"*3): fence=not fence; continue
        if S in l: sub.append(i)
        if l==S: (inf if fence else sa).append(i)
        if S in l and l!=S: bul.append(i)
    lastnb=max(i for i,l in enumerate(L,1) if l.strip())
    k=[k for k in rng if p.endswith("correction-1-"+k)]
    ins="n/a"
    if k:
        lo,hi=rng[k[0]]; ins=sum(1 for i in range(lo,hi+1) if S in L[i-1])
    print(p.split("/")[-1], "lines=%d substring_lines=%s standalone_outside_fence=%s in_fence=%s nonstandalone=%s last_nonblank=%d last_is_S13=%s fence_open_at_eof=%s CR=%d inserted_section_S13_hits=%s" % (len(L), sub, sa, inf, bul, lastnb, L[lastnb-1]==S, fence, sum(l.endswith("\r") for l in L), ins))
PY
2026-11-11-v-rulings-filing-correction-1-worker1.md lines=525 substring_lines=[525] standalone_outside_fence=[525] in_fence=[] nonstandalone=[] last_nonblank=525 last_is_S13=True fence_open_at_eof=False CR=0 inserted_section_S13_hits=0
2026-11-11-v-rulings-filing-correction-1-manager.md lines=488 substring_lines=[488] standalone_outside_fence=[488] in_fence=[] nonstandalone=[] last_nonblank=488 last_is_S13=True fence_open_at_eof=False CR=0 inserted_section_S13_hits=0
2026-11-11-v-rulings-filing-correction-2-worker1.md lines=452 substring_lines=[452] standalone_outside_fence=[452] in_fence=[] nonstandalone=[] last_nonblank=452 last_is_S13=True fence_open_at_eof=False CR=0 inserted_section_S13_hits=n/a
```
There is no IPv4 address (not even 127.0.0.1), no email, no MAC and no key path. The S13 check holds in all three files.

## Findings

1. **MAJOR**: the skeleton is called non-re-runnable, but it is recoverable. This is S2 and the unit's UNVERIFIED rule.
   - Where: (a):314 says "**The skeleton cannot be re-run against.**" and relabels :209-211, :218 and :250 as UNVERIFIED (not re-runnable). (c):63 says "The skeleton is gone." (c):450 repeats the relabel as a PASS ground.
   - The evidence for that negative is a search of /tmp, /private/tmp and git only.
   - The skeleton's full 27-line content is in the session transcript, as the Write tool call at 2026-11-11T19:33:58Z (14:33:58 EST, matching :211). Block 6 shows it.
   - Re-run on that content, :209, :210, :211, :213-216, the elided-lines claim at :218, and :250 all hold.
   - **(a):218 "All nine sections read `(pending)`" is false**: 8 `## ` sections, 8 `(pending)` lines. So the correction labelled a wrong original claim UNVERIFIED instead of correcting it, and it labelled five true claims UNVERIFIED.
   - Caveat: the transcript corpus is machine-local and not under version control. Whether it counts as re-runnable evidence is the manager's call. Even so, "cannot be re-run" is a universal negative that its own evidence does not support. A scoped wording ("no copy under /tmp or in git") would have been accurate.

2. **MINOR**: (b):469 labels the S13 positions 210 and 235 at :207 and :217 "UNVERIFIED (not re-runnable)".
   - Re-execution on those earlier file states is indeed impossible.
   - However, both outputs exist as genuine Bash tool results in transcript agent-abe49d634e60ac82e.jsonl, at 19:40:29Z (at=[210]) and 19:40:37Z (at=[235]) (block 6).
   - Their provenance is therefore verifiable. "UNVERIFIED" understates the evidence, and S2 cuts both ways.

3. **MINOR**: (c)'s Self-check block uses `$R` at (c):406, :411, :413, :417, :423, :429 and :431. `R` is not defined in (c)'s Definitions block at (c):23-30. It is defined only in /tmp/vrf-c2/selfcheck_cmds.sh, so a reader of (c) alone cannot reproduce the block exactly. I bound `R` to (c), and every row re-ran IDENTICAL.

4. **MINOR**: some process-log claims in (c) describe output instead of pasting it (S1).
   - (c):12 has "(`diff` exit 0)" and "the raw name count is 0 in all four files". No diff exit status is pasted, and there is no name count for $PA as such (it is only implied via `cmp` plus selfcheck).
   - (c):16 says insert.py "asserted that the tail was blank line, S13 line, newline, and that the section contained no S13 sentence". No insert.py output is pasted; the script prints "inserted N lines before final line".
   - The outcomes are independently confirmed by blocks 1 and 8 here, so this is form, not substance.

5. **MINOR (disclosed)**: repogrep.sh rewrites any ./Redemtion/ path to `./Redemtion/<gitignored-file>`.
   - Where: (a):358, :439-440; (b):271, :351-352; (c):102, :183-184.
   - Two distinct output rows become indistinguishable. The brief does not mandate this redaction.
   - The line count and the counts are unaffected (block 2: IDENTICAL against the same masked script), and (c):14 flags it for the manager. Not a truncation, but a reader cannot tell the two rows apart.

6. **MINOR (cosmetic)**: two quotes are not byte-exact. (a):281 quotes :210 without its 6 leading spaces. (b):405 quotes :238 without the leading `- `, and the (b) C2.2 item has no "Original wording:" line. Every other quote matches byte-for-byte (block 5).

7. **MINOR (pre-existing, acknowledged in (c):445, not caused by this unit)**: (b) still carries a tail-truncated pasted block, `count.sh <two new reports> | tail -3` at :213. It also uses placeholder commands (`<two new reports>`, `<this report>`) at :206 and :213. Neither Correction 2 section corrects them.

No break was found on:
- append-only for (a) and (b) (block 1);
- completeness of the pasted blocks: 196 commands re-run, and every difference is explained by my substitution (block 2);
- the `wc -l` figures (block 3);
- byte-identity of the (c) blocks (block 4);
- the INFERRED labels on the staged MANIFEST positions ((b):466, (c):302);
- the name count, split detector and helper outputs (block 7);
- other PII and S13 (block 8).

## Result: FAIL
The FAIL rests on Finding 1. The skeleton claims were relabelled "not re-runnable" when they could be re-run. Re-running them shows that one original claim, (a):218 "nine sections", is false and was left uncorrected. Everything else holds.

## Self-check of this report
(Not completed: worker2 stopped at its 40-turn limit before running this self-check. The manager ran the check on this file; the output is in docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md, Verification evidence.)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
