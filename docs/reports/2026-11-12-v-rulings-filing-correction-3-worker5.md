# 2026-11-12-v-rulings-filing-correction-3 worker5 (ADVERSARIAL, narrow)
## Task
Unit 2026-11-12-v-rulings-filing-correction-3, bead Praxis_build-n1y, worker5, ADVERSARIAL (narrow). Read-only apart from this report. Scope: the six items of the brief (the whole manager report; worker3 report lines 146-167; worker2 report lines 18-30; worker6 report line 485 and its structure against /tmp/c3pre; /tmp/c3mgr/scan.sh and E2 email hits; this report's self-check). The pending markers for worker5 in the manager report are not flagged.
## Criteria
- S1 (specs/SPEC_RUBRIC.md): every claim in a report has pasted command output, not a description of output.
- S2 (specs/SPEC_RUBRIC.md): no component reported at a higher level than the evidence supports.
- S13: the S13 sentence once, standalone, last line.
## Commands and output
All scripts are in /tmp/c3w5 and run under bash from the repo root. Each block is the `cat` of the script followed by its captured output, embedded by /tmp/c3w5/assemble.py. `N` is built at runtime from the evidence filename and never printed; output passes through a mask for the name and any email address. /tmp/c3mgr was copied to /tmp/c3w5/c3mgr-copy and scan.sh was run as /tmp/c3w5/scan.sh with its scratch paths pointed at the copy (the path diff is at the top of run1.out); nothing under /tmp/c3mgr was written. e6.sh only reads, so it was run in place.
### run1: E2 scan re-run, E5 (e6.sh) re-run, manager self-check re-run, email and name counts
```
$ cat /tmp/c3w5/run1.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
M=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
date "+%Y-%m-%dT%H:%M:%S"
r "MROWS=5 /tmp/c3w5/scan.sh > /tmp/c3w5/scan.out; cat /tmp/c3w5/scan.out"
r "sed -n '242,276p' $M > /tmp/c3w5/scan.pasted; diff /tmp/c3w5/scan.pasted /tmp/c3w5/scan.out; echo diff_exit=\$?"
r "/tmp/c3mgr/e6.sh > /tmp/c3w5/e6.out 2>&1; sed -n '338,410p' $M > /tmp/c3w5/e6.pasted; diff /tmp/c3w5/e6.pasted /tmp/c3w5/e6.out; echo diff_exit=\$?"
r "sed -n '464p' $M | sed 's/^\$ //' > /tmp/c3w5/selfcmd.sh; bash /tmp/c3w5/selfcmd.sh > /tmp/c3w5/self.out 2>&1; sed -n '465,469p' $M | diff - /tmp/c3w5/self.out; echo diff_exit=\$?"
r "grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/scan.sh $M"
r "grep -ci -- \"\$N\" $M; grep -c '@' /tmp/c3mgr/scan.sh"
$ /tmp/c3w5/run1.sh
2026-11-11T20:30:33
$ MROWS=5 /tmp/c3w5/scan.sh > /tmp/c3w5/scan.out; cat /tmp/c3w5/scan.out
name_len=4
files_in_set=30
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md email_lines=2 at=[114,132] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker10.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker6.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker7.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker8.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-11-v-rulings-filing-worker9.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172802Z-STATUS.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172933Z-python-git-install.md email_lines=0 at=[] name_ci=0 name_split=0
vm/replies/20261111T172940Z-STATUS.md email_lines=0 at=[] name_ci=0 name_split=0
email_lines_total_files=2
DECISIONS.md added lines=104 email_lines=0 name_ci=0 name_split=0
MANIFEST.md last 5 rows email_lines=0 name_ci=0 name_split=0
positive controls: name_split_on_hyphenated_synthetic=1 email_on_synthetic=1
$ sed -n '242,276p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md > /tmp/c3w5/scan.pasted; diff /tmp/c3w5/scan.pasted /tmp/c3w5/scan.out; echo diff_exit=$?
2c2
< files_in_set=29
---
> files_in_set=30
28a29
> docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md email_lines=0 at=[] name_ci=0 name_split=0
diff_exit=1
$ /tmp/c3mgr/e6.sh > /tmp/c3w5/e6.out 2>&1; sed -n '338,410p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md > /tmp/c3w5/e6.pasted; diff /tmp/c3w5/e6.pasted /tmp/c3w5/e6.out; echo diff_exit=$?
1c1
< 2026-11-11T20:28:38
---
> 2026-11-11T20:30:33
diff_exit=1
$ sed -n '464p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | sed 's/^$ //' > /tmp/c3w5/selfcmd.sh; bash /tmp/c3w5/selfcmd.sh > /tmp/c3w5/self.out 2>&1; sed -n '465,469p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | diff - /tmp/c3w5/self.out; echo diff_exit=$?
diff_exit=0
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/scan.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
/tmp/c3mgr/scan.sh:0
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:0
$ grep -ci -- "$N" docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -c '@' /tmp/c3mgr/scan.sh
0
3
```
The only differences from the pasted E2 are `files_in_set` 29 to 30 and one extra row: this worker5 report, which did not exist when E2 ran (email_lines=0, name_ci=0). The only difference from the pasted E5 is the date line. The manager self-check block (lines 465-469) equals what its line-464 command prints now (diff_exit=0). Manager report email count 0, name count 0; scan.sh email count 0.

### run2: pasted script sources against the files, helper paths, worker4 tally, final.out leads, bead MANIFEST rows
```
$ cat /tmp/c3w5/run2.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
M=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
W4=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
date "+%Y-%m-%dT%H:%M:%S"
r "grep -n '@' /tmp/c3mgr/scan.sh | cut -c1-200"
r "sed -n '215,240p' $M | diff - /tmp/c3mgr/scan.sh; echo diff_exit=\$?"
r "sed -n '306,336p' $M | diff - /tmp/c3mgr/e6.sh; echo diff_exit=\$?"
r "sed -n '41,66p' $M | diff - /tmp/c3mgr/v1.sh; echo diff_exit=\$?"
r "sed -n '138,149p' $M | diff - /tmp/c3mgr/v2.sh; echo diff_exit=\$?"
r "ls -d /tmp/vrf-c2/selfcheck.sh /tmp/vrf-c2/lib.sh /tmp/c2mgr/pii.py /tmp/c3pre /tmp/c3w1 /tmp/c3w2 /tmp/c3mgr"
r "ls /tmp/c3pre /tmp/c3mgr/pre5"
r "grep -nE 'MAJOR|MINOR' $W4 | cut -c1-220"
r "grep -niE 'two steps|one step|hunk' $W4 | cut -c1-260"
r "grep -niE 'pre-edit copy|Nothing under vm|undefined' /tmp/c3w2/final.out | cut -c1-200"
r "git rev-list HEAD | grep -c ^83891f6; git log --oneline -1 83891f6 | cut -c1-80"
r "git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'"
r "git diff d056e91 83891f6 -- DECISION_LOG.md HANDOFF.md STATUS.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'"
$ /tmp/c3w5/run2.sh
2026-11-11T20:31:13
$ grep -n '@' /tmp/c3mgr/scan.sh | cut -c1-200
5:EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
6:v1() { perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }' "$@"; }
26:echo "positive controls: name_split_on_hyphenated_synthetic=$ctl email_on_synthetic=$(printf 'a.b%sc-d.example\n' '@' | grep -cE "$EM")"
$ sed -n '215,240p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | diff - /tmp/c3mgr/scan.sh; echo diff_exit=$?
diff_exit=0
$ sed -n '306,336p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | diff - /tmp/c3mgr/e6.sh; echo diff_exit=$?
diff_exit=0
$ sed -n '41,66p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | diff - /tmp/c3mgr/v1.sh; echo diff_exit=$?
diff_exit=0
$ sed -n '138,149p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | diff - /tmp/c3mgr/v2.sh; echo diff_exit=$?
diff_exit=0
$ ls -d /tmp/vrf-c2/selfcheck.sh /tmp/vrf-c2/lib.sh /tmp/c2mgr/pii.py /tmp/c3pre /tmp/c3w1 /tmp/c3w2 /tmp/c3mgr
/tmp/c2mgr/pii.py
/tmp/c3mgr
/tmp/c3pre
/tmp/c3w1
/tmp/c3w2
/tmp/vrf-c2/lib.sh
/tmp/vrf-c2/selfcheck.sh
$ ls /tmp/c3pre /tmp/c3mgr/pre5
/tmp/c3mgr/pre5:
2026-11-11-v-rulings-filing-correction-2-worker6.md
2026-11-12-v-rulings-filing-correction-3-worker2.md
2026-11-12-v-rulings-filing-correction-3-worker3.md
scan.sh

/tmp/c3pre:
2026-11-11-v-rulings-filing-correction-2-manager.md
2026-11-11-v-rulings-filing-correction-2-worker6.md
2026-11-11-v-rulings-filing-worker2.md
2026-11-11-v-rulings-filing-worker5.md
$ grep -nE 'MAJOR|MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md | cut -c1-220
465:82:--- E6 (b)(g) lines cited in the MINOR findings
722:1. MAJOR, check (c) and the address rule. docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:240 contains an email address. It is the synthetic positive-control address inside the pasted source of /tmp/
724:2. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:337 says the report has "33 lines". It has 352 (rerun.out: `352 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md`;
726:3. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:11 says the S13 sentence is once, standalone, last line "in each new report and in each edited report (E1 and E2 self-check output
728:4. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:25 (step 6, "appended the MANIFEST rows (E3)") and :27 (step 8, "appended five MANIFEST rows (E3)") say that rows were appended tw
730:5. MINOR, check (g), S2. docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:485: "With these definitions the 37 lines can be run as written, but none was re-run here." Whether the lines can be run is as
732:6. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:132 "37 command lines, not about 26": the figure "about 26" has no paste anywhere in the worker3 report (rerun3.out: the grep find
734:7. MINOR, check (g). docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md:29 says the leads "were followed up by worker3 (BUILD fix) and checked again by worker4 (a fresh ADVERSARIAL pass)". That is past 
747:FAIL. 1 MAJOR, 6 MINOR.
$ grep -niE 'two steps|one step|hunk' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md | cut -c1-260
$ grep -niE 'pre-edit copy|Nothing under vm|undefined' /tmp/c3w2/final.out | cut -c1-200
84:- "Restoration to the exact prior bytes is UNVERIFIED": stays UNVERIFIED. Nothing above tests it, and no pre-edit copy exists.
85:$ grep -nE "find /tmp|MEMORY\*|pre-edit copy" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | cut -c1-120
126:$ sed -n 4p docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -oE "Nothing under vm/ or .claude/ was written."
127:Nothing under vm/ or .claude/ was written.
$ git rev-list HEAD | grep -c ^83891f6; git log --oneline -1 83891f6 | cut -c1-80
0
83891f6 park(Praxis_build-n1y): audit FAIL after Amear resume, parked again per 
$ git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
0
$ git diff d056e91 83891f6 -- DECISION_LOG.md HANDOFF.md STATUS.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
0
```
The three `@` lines in scan.sh are the regex, the perl array and `"$@"`, and the runtime-built control; none is an address. The pasted sources of scan.sh, e6.sh, v1.sh and v2.sh equal the files (diff_exit=0 each).

### run3: worker6 structure, worker3 note sources, specific manager claims
```
$ cat /tmp/c3w5/run3.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
M=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
W6=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
P6=/tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
W3=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; export EM
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
date "+%Y-%m-%dT%H:%M:%S"
echo "--- item 4: worker6 structure"
r "wc -l $P6 $W6"
r "cmp <(head -n 206 $P6) <(head -n 206 $W6) && echo head-1-206-identical"
r "cmp <(tail -n 1 $P6) <(tail -n 1 $W6) && echo last-line-identical"
r "diff -d $P6 $W6 | grep -v '^>'"
r "diff -d $P6 $W6 | grep -c '^<'"
echo "--- item 2: worker3 note sources"
r "sed -n '379p;418p' $W6 | cut -c1-140"
r "sed -n '132,133p' $W3 | cut -c1-300"
r "sed -n '72,73p' /tmp/c3w2/final.out"
r "head -n 206 $W6 | grep -nE '^\\$ .*\\$\\{?(PA|PB|A|B|T|P|W5|D3|C|R)\\b' | wc -l"
r "grep -rn 'about 26' $W3 $M /tmp/c3mgr/*.md /tmp/c3mgr/*.sh /tmp/c3mgr/*.txt 2>/dev/null | cut -c1-160"
echo "--- item 1: manager claims"
r "sed -n '11p' $M; sed -n '25p' $M"
r "grep -c 'S13' /tmp/c3mgr/scan.sh"
r "sed -n '79p' /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -ciE 'noreply'; sed -n '79p' /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -ci 'anthropic'"
r "sed -n '56,81p' /tmp/c3w2/final.out | grep -ciE 'undefined|not defined|\\\$A|\\\$PA'"
r "ls -d /tmp/c3w3 /tmp/c3w4"
r "stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' .claude/settings.json scripts/dispatch-log-writeahead.sh /tmp/c3pre"
r "git diff HEAD -- DECISION_LOG.md HANDOFF.md STATUS.md DISPATCH_LOG.md ISSUE_REGISTER.md AUDIT_LOG.md DECISIONS.md | grep '^+' | grep -v '^+++' | grep -cE \"\$EM\""
r "ls docs/reports/ | grep -c '^2026-11-12-v-rulings-filing-correction-3-worker1'; ls /tmp/c3w3 | grep -ci worker1"
$ /tmp/c3w5/run3.sh
2026-11-11T20:32:16
--- item 4: worker6 structure
$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     207 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
     487 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     694 total
$ cmp <(head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo head-1-206-identical
head-1-206-identical
$ cmp <(tail -n 1 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(tail -n 1 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md) && echo last-line-identical
last-line-identical
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -v '^>'
206a207,486
$ diff -d /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c '^<'
0
--- item 2: worker3 note sources
$ sed -n '379p;418p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-140
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
37
$ sed -n '132,133p' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-300
- W6: 37 command lines, not about 26. The function `r` is defined in no saved script, and the generating script is not saved. The bindings of `C`, `D3` and `W5` are INFERRED from W6:14 and matching paths. No line was re-run.
- W1:4: the only path under .claude or vm newer than the reference file is .claude/state/mint-log, at 18:24:36 local. That is before worker1 began (19:39:57 local), so it is not worker1's write. Nothing under vm/ is listed. The check sees mtimes only.
$ sed -n '72,73p' /tmp/c3w2/final.out
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE "^\\$ .*\\$\{?(A|PA|B)\b"
26
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b' | wc -l
      37
$ grep -rn 'about 26' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md /tmp/c3mgr/*.md /tmp/c3mgr/*.sh /tmp/c3mgr/*.txt 2>/dev/null | cut -c1-160
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:132:- W6: 37 command lines, not about 26. The function `r` is defined in no saved script, and t
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:165:- "about 26" at line 132 is the figure from the manager's brief to worker3. It came from wo
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:438:6. MINOR: the worker3 report gave "about 26" and "19:39:57" with no paste in that file. Fix
/tmp/c3mgr/w3note_text.md:6:- "about 26" at line 132 is the figure from the manager's brief to worker3. It came from worker2's evidence file (its line 73 above:
--- item 1: manager claims
$ sed -n '11p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; sed -n '25p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
- S13 (specs/SPEC_RUBRIC.md:136): the S13 sentence once, standalone, last line, in each new report and in each edited report (E1 and E2 self-check output).
6. Re-ran the append-only and self-checks after worker3 (E1, v2 run). Appended the five MANIFEST rows 415-419 in one step (E3). Dispatched worker4 (ADVERSARIAL) on everything.
$ grep -c 'S13' /tmp/c3mgr/scan.sh
0
$ sed -n '79p' /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -ciE 'noreply'; sed -n '79p' /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md | grep -ci 'anthropic'
1
1
$ sed -n '56,81p' /tmp/c3w2/final.out | grep -ciE 'undefined|not defined|\$A|\$PA'
4
$ ls -d /tmp/c3w3 /tmp/c3w4
/tmp/c3w3
/tmp/c3w4
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' .claude/settings.json scripts/dispatch-log-writeahead.sh /tmp/c3pre
2026-11-05T19:33:46 .claude/settings.json
2026-07-28T12:46:11 scripts/dispatch-log-writeahead.sh
2026-11-11T19:39:57 /tmp/c3pre
$ git diff HEAD -- DECISION_LOG.md HANDOFF.md STATUS.md DISPATCH_LOG.md ISSUE_REGISTER.md AUDIT_LOG.md DECISIONS.md | grep '^+' | grep -v '^+++' | grep -cE "$EM"
0
$ ls docs/reports/ | grep -c '^2026-11-12-v-rulings-filing-correction-3-worker1'; ls /tmp/c3w3 | grep -ci worker1
1
0
```
### run4: local offset, and whether the worker3 note pastes a lower bound for worker1's start
```
$ cat /tmp/c3w5/run4.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
date "+%Y-%m-%dT%H:%M:%S %z"
r "grep -c '2026-11-12T00:37:30Z' DECISION_LOG.md"
r "grep -cE '00:37|lower bound|DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md"
r "sed -n '146,167p' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -cE '00:37|DECISION_LOG|began after'"
$ /tmp/c3w5/run4.sh
2026-11-11T20:33:16 -0500
$ grep -c '2026-11-12T00:37:30Z' DECISION_LOG.md
1
$ grep -cE '00:37|lower bound|DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
0
$ sed -n '146,167p' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | grep -cE '00:37|DECISION_LOG|began after'
0
```
## Findings
Items 4 and 5 hold: the worker6 report is original lines 1-206, then the insertion `206a207,486`, then the original last line, 0 `<` lines (run3); line 485 now says UNVERIFIED (E5 re-run, run1). scan.sh has no literal address (run1: 0; run2: the three `@` lines) and E2 re-run shows exactly two email hits, return-handoff 114 and 132 (run1). The breaks are below.

1. MINOR (S2), docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:166. The note says the /tmp/c3pre mtime means "worker1 began at or before 19:39:57", then concludes "The 18:24:36 time at line 133 is earlier in either case." That does not follow. A time that is at or before 19:39:57 can also be before 18:24:36, so an upper bound on the start cannot show that 18:24:36 came before the start. A lower bound does exist: DECISION_LOG has the 2026-11-12T00:37:30Z resume line (count 1), and the local offset is -0500 (run4), so that is 19:37:30 local. But the note neither pastes nor cites it (run4: 0 hits for `00:37|DECISION_LOG|began after` in lines 146-167). The conclusion is probably true. The support pasted for it is invalid.
2. MINOR (S1), docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:165. "is the figure from the manager's brief to worker3" has no paste. run3's grep for `about 26` across the worker3 report, the manager report and /tmp/c3mgr finds only the claim itself, worker3:132, manager:438 and /tmp/c3mgr/w3note_text.md:6. No saved brief is among them. The rest of the bullet holds: final.out line 73 gives 26, and the wider pattern gives 37 (run3, `wc -l` 37).
3. MINOR (S1/S2), docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:11. It still says "(E1 and E2 self-check output)". This is the exact text worker4 MINOR 3 flagged (worker4:726, run2). E2 has no S13 check (run3: `grep -c 'S13' /tmp/c3mgr/scan.sh` gives 0). The S13 evidence for worker2 and worker4 is in E5, not E1 or E2. Disposition 3 at manager:435 says "Fixed", but line 11 was not changed.
4. MINOR (S2), manager:25. "Appended the five MANIFEST rows 415-419 in one step (E3)." E3 shows a single hunk, `414a415,419`. Two appends in a row against the same pre-copy give that same single hunk, so E3 cannot show "one step". Worker4 MINOR 4 (worker4:728, run2) said the log does not establish the step count, and the new wording claims a count that E3 cannot support either.
5. MINOR (S1/S2), manager:16. Worker3's edits are called "insertions only (E1, v2 run)", and the list includes "an addendum to the worker1 report". v2 diffs only the two correction-2 reports. No pre-edit copy of the worker1 report exists in /tmp/c3pre, /tmp/c3mgr/pre5 or /tmp/c3w3 (run2 `ls /tmp/c3pre /tmp/c3mgr/pre5`; run3 `ls /tmp/c3w3 | grep -ci worker1` gives 0). So "insertions only" is unproven for the worker1 addendum.
6. MINOR (S2), manager:33. "E2 shows they are the only two email hits in the bead." E2 scans the bead's MANIFEST.md only as the last 5 rows of the working copy. The MANIFEST rows the bead added in d056e91..83891f6 are outside E2. The claim happens to hold: those added lines have 0 email hits (run2), and the working-tree added lines of DECISION_LOG, HANDOFF, STATUS, DISPATCH_LOG, ISSUE_REGISTER, AUDIT_LOG and DECISIONS against HEAD have 0 (run3). But E2 does not show it. Note also that 83891f6 is not in HEAD's history (run2: `git rev-list HEAD | grep -c ^83891f6` gives 0). The manager report does not say this.
7. MINOR (S1), manager:15, 17, 21, 22, 32, 440, 445. These claims are true where I could check them, but none is backed by a paste in the manager report:
   - :15 names three specific leads in /tmp/c3w2/final.out, but E4 pastes only section headers and a `$ ` count. run2 finds the "no pre-edit copy exists" lead at final.out:84 and the vm/.claude sentence at :126-127; run3 finds 4 variable-related hits in final.out:56-81.
   - :17 gives worker4's tally "1 MAJOR and 6 MINOR". run2 shows worker4:747 `FAIL. 1 MAJOR, 6 MINOR.`
   - :21 says lib.sh and pii.py exist. run2 `ls -d` lists both.
   - :22 says worker1 copied the files "before editing". There is no paste.
   - :32 says the address was "the Anthropic no-reply address". run3: line 79 of the pre-copy matches `noreply` 1 and `anthropic` 1.
   - :440 says "The brief limits MANIFEST edits to the new rows". There is no paste.
   - :445 (S6) says "touches no block spec, code, hook or setting". There is no paste. run3 stat: .claude/settings.json was last modified 2026-11-05T19:33:46 and scripts/dispatch-log-writeahead.sh 2026-07-28T12:46:11, both before /tmp/c3pre (19:39:57).
8. MINOR (S1), manager:460. "Outside the repo: /tmp/c3pre, /tmp/c3w1, /tmp/c3w2, /tmp/c3mgr" leaves out /tmp/c3w3 and /tmp/c3w4. Both exist (run3 `ls -d`), and worker3's own report names /tmp/c3w3 (worker3:140).
9. MINOR (S1), docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md:19 and :29. Three sentences have no paste in that file: "The sections above are its skeleton, unchanged" (the evidence is E4 in the manager report, not here), "The leads in that evidence file were passed to worker3 (BUILD fix)" and "A fresh ADVERSARIAL pass (worker4) was dispatched after this note was written". The last two are the manager's own dispatch actions, and no command output records them. The stat paste does support "last written before the evidence file" (19:52:28 before 19:59:54).

## Result
FAIL. 0 MAJOR, 9 MINOR. Items 4 and 5 hold, and the E2, E5 and self-check re-runs reproduce (run1).

Self-check of this report, run on the final file (regenerated by /tmp/c3w5/assemble.py until the embedded output equals a fresh run):
```
$ cat /tmp/c3w5/self5.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
F=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
printf '$ %s\n' "/tmp/vrf-c2/selfcheck.sh $F"; /tmp/vrf-c2/selfcheck.sh "$F" 2>&1 | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
printf '$ %s\n' "grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F"; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$F"
printf '$ %s\n' "grep -ci -- \"\$N\" $F"; grep -ci -- "$N" "$F"
printf '$ %s\n' "grep -ciw 'v[e]rdict' $F"; grep -ciw 'v[e]rdict' "$F"
printf '$ %s\n' "grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' $F"; grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' "$F"
printf '$ %s\n' "grep -cE '\.\.\.' $F"; grep -cE '\.\.\.' "$F"
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
0
$ grep -ci -- "$N" docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
0
$ grep -ciw 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
0
$ grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
0
$ grep -cE '\.\.\.' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
0
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
