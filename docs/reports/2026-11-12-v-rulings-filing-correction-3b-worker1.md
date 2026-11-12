# Unit 2026-11-12-v-rulings-filing-correction-3b, worker1 (ADVERSARIAL)

## Task
Check, against the current files only, whether each of the 9 MINOR findings at docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md lines 284-305 is fixed in:
- docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md (M below)
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md (W2 below)
- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md (W3 below)

Pre-fix copies of these three files were not available. Disposition text claiming a fix was not relied on. Nothing in the repo was edited except this report; nothing was staged.

## Criteria
- S1: "Every claim in a report has pasted command output, not a description of output."
- S2: "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S13: the S13 sentence once, as a standalone final line.

## Commands and output
One runner script reads a command file line by line, prints `$ ` plus the line, runs it from the repo root, and masks any email-shaped string in the output. Three command files were each run once, with output tee'd to a .out file. A note on reading run1: the line right after `$ sed -n '72,73p' /tmp/c3w2/final.out > /tmp/c3b/w1/fo.txt; ` is not a command of mine. It is the first of the two lines of /tmp/c3w2/final.out that this command prints (a pasted `$ head` line and `26`). In the same way, the four lines after `$ sed -n '379p;416,418p'` are lines 379 and 416-418 of the worker6 report, not commands I ran.

The scripts were run as:
```
$ cd /tmp/c3b/w1 && ./run.sh /tmp/c3b/w1/cmds1.txt 2>&1 | tee /tmp/c3b/w1/run1.out
$ cd /tmp/c3b/w1 && ./run.sh /tmp/c3b/w1/cmds2.txt 2>&1 | tee /tmp/c3b/w1/run2.out
$ cd /tmp/c3b/w1 && ./run.sh /tmp/c3b/w1/cmds3.txt 2>&1 | tee /tmp/c3b/w1/run3.out
```
```
$ cat /tmp/c3b/w1/run.sh
#!/bin/bash
# runs each line of the command file given as $1 from the repo root; prints "$ cmd" then its output; any email-shaped string in output is masked
cd /Volumes/Sensidine/Praxis.build || exit 1
date "+%Y-%m-%dT%H:%M:%S %z"
while IFS= read -r c; do
  case "$c" in '#'*) printf '%s\n' "$c"; continue;; '') continue;; esac
  printf '$ %s\n' "$c"
  bash -c "$c" 2>&1 | perl -pe 's/[A-Za-z0-9._%+-]+\@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
done < "$1"
$ cat /tmp/c3b/w1/cmds1.txt
# F1 and F2: worker3 note
grep -n 'about 26\|19:39:57\|00:37:30Z\|not saved on disk' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-110
stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' /tmp/c3pre
grep -n '2026-11-12T00:37:30Z' DECISION_LOG.md | cut -d: -f1
grep '2026-11-12T00:37:30Z' DECISION_LOG.md > /tmp/c3b/w1/dl_line.txt; /tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/dl_line.txt | grep -o 'name_ci=[0-9]* V1_HIT_lines=[0-9]*'
grep -q 'name_ci=0 V1_HIT_lines=0' <(/tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/dl_line.txt) && cut -c1-230 /tmp/c3b/w1/dl_line.txt
grep -n '2026-11-11T19:37:30' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
sed -n '72,73p' /tmp/c3w2/final.out > /tmp/c3b/w1/fo.txt; grep -q 'name_ci=0 V1_HIT_lines=0' <(/tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/fo.txt) && cat /tmp/c3b/w1/fo.txt
head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE '^\$ .*\$\{?(A|PA|B)\b'
sed -n '379p;416,418p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-140
head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b' | wc -l
grep -rlF 'about 26' /tmp/c3mgr /tmp/c3w3 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 2>/dev/null
grep -c 'c3pre' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
# F3: manager S13 coverage line
sed -n '11p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -n 'selfcheck.sh docs' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-12
grep 'selfcheck.sh docs' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -c 'correction-3-worker5'
grep -c 'correction-3-worker5.md: name_ci' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
# F4: MANIFEST step count
sed -n '27p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -ciE 'one step|two steps' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -v '^>'
wc -l MANIFEST.md
$ cat /tmp/c3b/w1/cmds2.txt
# F5: worker3 insertion into the worker1 report
sed -n '16p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
ls /tmp/c3w3/pre
stat -f '%SB birth %Sm mod %N' -t '%Y-%m-%dT%H:%M:%S' /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -v '^>'
diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -c '^<'
grep -n 'c3w3/pre' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-110
# F6: bead email claim
sed -n '36p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
git rev-list HEAD | grep -c '^83891f6'
git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | while read -r f; do git show 83891f6:"$f" | cmp -s - "$f" && echo same || echo "differs $f"; done | sort | uniq -c
git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | while read -r f; do n=$(git show 83891f6:"$f" | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'); [ "$n" != 0 ] && echo "at-83891f6 $f email_lines=$n"; done
# F7: unpasted claims in the manager report
grep -n 'final.out' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-70
grep -c 'FAIL. 1 MAJOR, 6 MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -n 'FAIL. 1 MAJOR, 6 MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
sed -n '23p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -cE '^\$ .*(ls|stat|test).*(lib\.sh|pii\.py)' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
sed -n '24p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -n 'brief limits MANIFEST' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
grep -o 'The brief limits MANIFEST edits to the new rows, so this goes to the master.' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
sed -n '480p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -nE '^\$ wc -l' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-100
grep -n '335' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-100
wc -l docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
grep -n 'no-reply address' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
# F8: /tmp list
sed -n '496p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
ls -d /tmp/c3*
grep -cE '^\$ ls -d' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
# F9: worker2 note
sed -n '19p;29p' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
# current self-checks of the three files
/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
$ cat /tmp/c3b/w1/cmds3.txt
# follow-ups
grep -niE 'one step|two steps' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-90
grep -cE '^\$ .*(cat|ls|stat).*(/tmp/vrf-c2/lib\.sh|/tmp/c2mgr/pii\.py)' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
grep -c '^\$ .*DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
grep -n 'DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-12
grep -cE '^\$ .*(worker4|correction-3-worker2|correction-3-worker5)\.md' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
sed -n '417p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c 'grep -cE'
sed -n '379p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c 'grep -nE'
```

run1 (`cat /tmp/c3b/w1/run1.out`):
```
2026-11-11T20:42:11 -0500
# F1 and F2: worker3 note
$ grep -n 'about 26\|19:39:57\|00:37:30Z\|not saved on disk' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-110
132:- W6: 37 command lines, not about 26. The function `r` is defined in no saved script, and the generating s
133:- W1:4: the only path under .claude or vm newer than the reference file is .claude/state/mint-log, at 18:2
154:$ grep -n '19:39:57' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-60
155:663:2026-11-11T19:39:57 /tmp/c3pre
159:2026-11-11T19:39:57 /tmp/c3pre
165:- "about 26" at line 132 is the figure from the manager's brief to worker3 (REPORTED by the manager; the b
166:- "19:39:57" at line 133 is the mtime of /tmp/c3pre (stat above), the directory worker1 filled with pre-ed
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' /tmp/c3pre
2026-11-11T19:39:57 /tmp/c3pre
$ grep -n '2026-11-12T00:37:30Z' DECISION_LOG.md | cut -d: -f1
842
$ grep '2026-11-12T00:37:30Z' DECISION_LOG.md > /tmp/c3b/w1/dl_line.txt; /tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/dl_line.txt | grep -o 'name_ci=[0-9]* V1_HIT_lines=[0-9]*'
name_ci=0 V1_HIT_lines=0
$ grep -q 'name_ci=0 V1_HIT_lines=0' <(/tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/dl_line.txt) && cut -c1-230 /tmp/c3b/w1/dl_line.txt
- [2026-11-12T00:37:30Z] WHO: amear | REPORTED BY: the Claude.ai Praxis channel | WHAT: **SECOND RESUME OF PARKED BEAD `Praxis_build-n1y` BY A HUMAN, and his go.** Chat 2026-11-11 19:31-19:33 ET (00:31-00:33Z 2026-11-12): the chan
$ grep -n '2026-11-11T19:37:30' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
445:2026-11-11T19:37:30
$ sed -n '72,73p' /tmp/c3w2/final.out > /tmp/c3b/w1/fo.txt; grep -q 'name_ci=0 V1_HIT_lines=0' <(/tmp/vrf-c2/selfcheck.sh /tmp/c3b/w1/fo.txt) && cat /tmp/c3b/w1/fo.txt
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE "^\\$ .*\\$\{?(A|PA|B)\b"
26
$ head -n 206 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE '^\$ .*\$\{?(A|PA|B)\b'
26
$ sed -n '379p;416,418p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-140
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
176:$ sed -n 284,313p $A | grep -n "manager.md" | cut -c1-90
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
37
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b' | wc -l
      37
$ grep -rlF 'about 26' /tmp/c3mgr /tmp/c3w3 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 2>/dev/null
/tmp/c3mgr/w3note_text.md
/tmp/c3mgr/pre5/2026-11-12-v-rulings-filing-correction-3-worker3.md
/tmp/c3mgr/parts/ADV
/tmp/c3w3/t_r.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
$ grep -c 'c3pre' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
45
# F3: manager S13 coverage line
$ sed -n '11p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
- S13 (specs/SPEC_RUBRIC.md:136): the S13 sentence once, standalone, last line, in each new report and in each edited report (E1 and E5 self-check output, and the self-check block at the end of this report).
$ grep -n 'selfcheck.sh docs' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-12
66:r "/tmp/v
124:$ /tmp/v
151:r "/tmp/
185:$ /tmp/v
339:run "/tm
406:$ /tmp/v
500:$ /tmp/v
$ grep 'selfcheck.sh docs' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -c 'correction-3-worker5'
0
$ grep -c 'correction-3-worker5.md: name_ci' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
V1 positive control (hyphen-split synthetic line): HIT_lines=1
# F4: MANIFEST step count
$ sed -n '27p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
6. Re-ran the append-only and self-checks after worker3 (E1, v2 run). Appended the five MANIFEST rows 415-419 (E3 shows them as one block against the pre-append copy). Dispatched worker4 (ADVERSARIAL) on everything.
$ grep -ciE 'one step|two steps' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
1
$ diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -v '^>'
414a415,420
$ wc -l MANIFEST.md
     420 MANIFEST.md
```

run2 (`cat /tmp/c3b/w1/run2.out`):
```
2026-11-11T20:42:36 -0500
# F5: worker3 insertion into the worker1 report
$ sed -n '16p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
- worker3, BUILD (fix): added C3.8 and C3.9 to the correction-2 manager report, C3.4 to the worker6 report, and an addendum to the worker1 report. Outcome: done; insertions only (E1 v2 run for the two correction-2 reports; E5 for the worker1 report against worker3's pre-edit copy). Report docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md.
$ ls /tmp/c3w3/pre
2026-11-11-v-rulings-filing-correction-2-manager.md
2026-11-11-v-rulings-filing-correction-2-worker6.md
2026-11-12-v-rulings-filing-correction-3-worker1.md
$ stat -f '%SB birth %Sm mod %N' -t '%Y-%m-%dT%H:%M:%S' /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
2026-11-11T20:04:00 birth 2026-11-11T20:04:00 mod /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md
2026-11-11T19:40:29 birth 2026-11-11T20:15:05 mod docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
2026-11-11T20:16:21 birth 2026-11-11T20:36:24 mod docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
2026-11-11T20:29:42 birth 2026-11-11T20:34:11 mod docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
$ diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -v '^>'
640a641,677
$ diff -d /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | grep -c '^<'
0
$ grep -n 'c3w3/pre' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-110
14:- Insertion only: each diff against /tmp/c3w3/pre/ has 0 `<` lines.
18:Process. Before any edit, the three target files were copied with plain `cp` (no `-p`) to /tmp/c3w3/pre/. E
35:$ wc -l /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md /tmp/c3w3/pre/2026-11-11-v-ruling
36:     464 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md
37:     366 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
38:     641 /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md
40:$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md
41:2026-11-11T20:04:00 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md
42:2026-11-11T20:04:00 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
43:2026-11-11T20:04:00 /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md
51:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-
54:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-
56:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-
58:$ cmp <(head -n 463 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md) <(head -n 463 docs/r
63:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-
65:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-
67:$ diff /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-
69:$ cmp <(head -n 365 /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md) <(head -n 365 docs/r
74:$ diff /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-
76:$ diff /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-
78:$ diff /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md docs/reports/2026-11-12-v-rulings-
80:$ cmp <(head -n 640 /tmp/c3w3/pre/2026-11-12-v-rulings-filing-correction-3-worker1.md) <(head -n 640 docs/r
# F6: bead email claim
$ sed -n '36p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:114 and :132 were not changed (master's application: email-header quotes of the MFFU support address). E2 shows they are the only two email hits in the bead's files, in the DECISIONS.md added lines and in the bead's MANIFEST added lines. Note: 83891f6 (the parked tip) is not an ancestor of HEAD (E5).
$ git rev-list HEAD | grep -c '^83891f6'
0
$ git diff d056e91 83891f6 -- MANIFEST.md | grep '^+' | grep -v '^+++' | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
0
$ git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | while read -r f; do git show 83891f6:"$f" | cmp -s - "$f" && echo same || echo "differs $f"; done | sort | uniq -c
   1 differs docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
   1 differs docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
   1 differs docs/reports/2026-11-11-v-rulings-filing-worker2.md
   1 differs docs/reports/2026-11-11-v-rulings-filing-worker5.md
  20 same
$ git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | while read -r f; do n=$(git show 83891f6:"$f" | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'); [ "$n" != 0 ] && echo "at-83891f6 $f email_lines=$n"; done
at-83891f6 docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md email_lines=2
at-83891f6 docs/reports/2026-11-11-v-rulings-filing-worker2.md email_lines=1
at-83891f6 docs/reports/2026-11-11-v-rulings-filing-worker5.md email_lines=1
# F7: unpasted claims in the manager report
$ grep -n 'final.out' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-70
15:- worker2, ADVERSARIAL: hunt for placeholder commands, unpasted cla
454:$ grep -n '^--- E' /tmp/c3w2/final.out
462:$ grep -c '^\$ ' /tmp/c3w2/final.out
$ grep -c 'FAIL. 1 MAJOR, 6 MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
$ grep -n 'FAIL. 1 MAJOR, 6 MINOR' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
747:FAIL. 1 MAJOR, 6 MINOR.
$ sed -n '23p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
2. Checked that the original helper scripts still exist (/tmp/vrf-c2/selfcheck.sh, /tmp/vrf-c2/lib.sh, /tmp/c2mgr/pii.py); worker1 pastes them in the inserted sections.
$ grep -cE '^\$ .*(ls|stat|test).*(lib\.sh|pii\.py)' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
$ sed -n '24p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
3. Dispatched worker1 (BUILD). It copied the four target files to /tmp/c3pre/ before editing, ran the re-checks on the live files before insertion, then inserted the sections and made the two address edits.
$ grep -n 'brief limits MANIFEST' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
475:- Out of scope, reported and not fixed: worker4 reported
$ grep -o 'The brief limits MANIFEST edits to the new rows, so this goes to the master.' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
The brief limits MANIFEST edits to the new rows, so this goes to the master.
$ sed -n '480p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
Not applicable. This unit approves no deviation. Every file it touches is a report under docs/reports/ or MANIFEST.md (the Files staged list below, built by `wc -l` on each path); no block spec, code, hook or setting is among them. It is append-only text corrections in two reports, two masked addresses, new reports and MANIFEST rows.
$ grep -nE '^\$ wc -l' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-100
76:$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-
86:$ wc -l /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-
103:$ wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-fil
117:$ wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-fil
163:$ wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11
298:$ wc -l /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md
$ grep -n '335' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-100
337:run "sed -n '335,336p' MANIFEST.md | grep -c 'docs/reports/evidence/'"
393:335
403:$ sed -n '335,336p' MANIFEST.md | grep -c 'docs/reports/evidence/'
475:- Out of scope, reported and not fixed: worker4 reported the rep's name in MANIFEST.md at lines 
493:- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: 335 lines; new.
$ wc -l docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
     335 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
$ grep -n 'no-reply address' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-60
35:- docs/reports/2026-11-11-v-rulings-filing-worker5.md:79.
477:- Worker5 (ADVERSARIAL, narrow): FAIL with 0 MAJOR and 9
# F8: /tmp list
$ sed -n '496p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
- Outside the repo: /tmp/c3pre (pre-edit copies), /tmp/c3w1, /tmp/c3w2, /tmp/c3w3, /tmp/c3w4, /tmp/c3w5 (worker scripts), /tmp/c3mgr (my scripts and outputs).
$ ls -d /tmp/c3*
/tmp/c3b
/tmp/c3mgr
/tmp/c3pre
/tmp/c3w1
/tmp/c3w2
/tmp/c3w3
/tmp/c3w4
/tmp/c3w5
$ grep -cE '^\$ ls -d' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
# F9: worker2 note
$ sed -n '19p;29p' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
Written by the unit manager, not by worker2. Worker2 stopped at its 40-turn limit before it wrote its findings (REPORTED: this comes from the harness notification to the manager, which is not a command output and cannot be re-run). The sections above are its skeleton, unchanged (the diff against the pre-note copy is in the manager report, E4: one insertion, 0 deleted lines). This report carries no adversarial result and the unit does not rely on it. Its working files are in /tmp/c3w2/; the sizes and times, taken just before this note was added:
The report above was last written before the evidence file. REPORTED by the manager (dispatches are events, not command outputs): the leads in that evidence file were passed to worker3 (BUILD fix), and a fresh ADVERSARIAL pass (worker4) was dispatched after this note was written; its result is in docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md, not here.
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
17a18,30
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -c '^<'
0
# current self-checks of the three files
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[511] last_nonblank_line=511 last_nonblank_is_S13=YES lines=511
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[31] last_nonblank_line=31 last_nonblank_is_S13=YES lines=31
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[168] last_nonblank_line=168 last_nonblank_is_S13=YES lines=168
V1 positive control (hyphen-split synthetic line): HIT_lines=1
```

run3 (`cat /tmp/c3b/w1/run3.out`):
```
2026-11-11T20:43:33 -0500
# follow-ups
$ grep -niE 'one step|two steps' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-90
471:4. MINOR: the process log said the MANIFEST rows were appended in two steps. Fixed: th
$ grep -cE '^\$ .*(cat|ls|stat).*(/tmp/vrf-c2/lib\.sh|/tmp/c2mgr/pii\.py)' docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:2
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:1
$ grep -c '^\$ .*DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
1
$ grep -n 'DECISION_LOG' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-12
4:Bead Praxi
10:- S8 (spe
350:run "gre
442:$ grep -
$ grep -cE '^\$ .*(worker4|correction-3-worker2|correction-3-worker5)\.md' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
7
$ sed -n '417p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c 'grep -cE'
1
$ sed -n '379p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -c 'grep -nE'
1
```

## Findings

### Grade of each worker5 finding
1. W3:166 (start-time reasoning). PARTIALLY FIXED. Current text: "worker1 began at or before 19:39:57. So this mtime alone does not show that 18:24:36 is before worker1 began. What does: worker1 was dispatched in this unit, which the master opened under the DECISION_LOG entry of 2026-11-12T00:37:30Z, that is 2026-11-11T19:37:30 local (pasted in the manager report, E5); 18:24:36 is before that." The invalid inference is gone, and the lower bound is now used. The bound itself is real: DECISION_LOG.md:842 is the "SECOND RESUME OF PARKED BEAD `Praxis_build-n1y`" entry (run1), and M:445 holds `2026-11-11T19:37:30` (run1). But the backing the note points to (M E5) is only `grep -c` of the timestamp string (count 1) and a time conversion. It does not show what the entry says, which is the premise. See new finding 1.
2. W3:165 ("about 26" provenance). FIXED, with a new defect in the backing paste. The line now says "REPORTED by the manager; the brief is not saved on disk". The 26 re-runs: 26 on the /tmp/c3pre copy (run1), and final.out lines 72-73 are a `$ head` line and `26` (run1). However, the paste the same line cites for 37 ("the worker6 report's lines 379 and 418, last command above") is a stitched pair. Line 379 is a `grep -nE` command and line 418 (`37`) is the output of the `grep -cE` command at line 417 (run1 shows lines 379 and 416-418; run3 shows 417 holds `grep -cE` (1) and 379 holds `grep -nE` (1)). See new finding 2. The 37 itself holds (run1: `wc -l` 37).
3. M:11 (S13 coverage). PARTIALLY FIXED. Current text: "in each new report and in each edited report (E1 and E5 self-check output, and the self-check block at the end of this report)." E2 is no longer cited. But the correction-3 worker5 report is a new report of this unit, and no self-check paste in M covers it: 0 of the 7 `selfcheck.sh docs` lines in M name it, and 0 `correction-3-worker5.md: name_ci` output lines exist in M (run1). The file itself passes now (run1: `S13_standalone=1`, `last_nonblank_is_S13=YES`, lines=335). See new finding 3.
4. M:27 (MANIFEST "one step"). FIXED. Current text: "Appended the five MANIFEST rows 415-419 (E3 shows them as one block against the pre-append copy)." No step count is claimed. The only "one step|two steps" hit in M is the worker4 disposition at M:471 (run3). E3's single hunk re-runs as `414a415,420` and MANIFEST.md has 420 lines (run1).
5. M:16 (worker3 "insertions only"). FIXED. Current text: "insertions only (E1 v2 run for the two correction-2 reports; E5 for the worker1 report against worker3's pre-edit copy)". The pre-edit copy exists at /tmp/c3w3/pre/ (worker5's `ls /tmp/c3w3 | grep -ci worker1` did not look inside the `pre` subdirectory). It was born at 20:04:00, before the worker1 report's last change at 20:15:05. W3:18 and :38 document it as worker3's pre-edit copy (641 lines). The diff re-runs as `640a641,677` with 0 `<` lines (run2).
6. M:36 (bead email hits). FIXED as raised: E2 now scans the bead's MANIFEST added lines (27 lines, 0 email, re-run 0 in run2), and the line notes that 83891f6 is not an ancestor of HEAD (run2: `git rev-list HEAD | grep -c '^83891f6'` gives 0). A scope problem remains in the same sentence. See new finding 4.
7. M:15, 17, 21, 22, 32, 440, 445 (now M:15, 17, 23, 24, 35, 475, 480). PARTIALLY FIXED: 3 of 7 sub-items are fixed or backed by cross-reference, and 4 are not.
   - :35 (was :32) the no-reply address: FIXED. It now says "a no-reply address" and cites E5. E5 pastes `grep -c` of the local part and domain on the pre-copy line 79 (1).
   - :23 (was :21) lib.sh and pii.py: backed by cross-reference ("worker1 pastes them in the inserted sections"). The correction-2 manager report has 2 such `$ ` lines and the worker1 report has 1 (run3). M itself pastes none (run2: 0). Accepted.
   - :24 (was :22) "copied the four target files to /tmp/c3pre/ before editing": unchanged (run2). It is indirectly supported by E1's diffs, which show the /tmp/c3pre copies are the live files minus the inserted lines. Accepted as weak support.
   - :15 the three named leads in /tmp/c3w2/final.out: NOT FIXED. M mentions final.out only at :15 and at the two E4 commands (:454 section headers, :462 a `$ ` count) (run2).
   - :17 worker4's tally "1 MAJOR and 6 MINOR": NOT FIXED. M has 0 pastes of it; it is at worker4:747 (run2).
   - :475 (was :440) "The brief limits MANIFEST edits to the new rows": NOT FIXED. The sentence is still there, with no paste and no REPORTED label (run2).
   - :480 (was :445) S6 basis: NOT FIXED, and new wording added. See new finding 6.
8. M:496 (was :460) /tmp list. PARTIALLY FIXED. Current text: "/tmp/c3pre (pre-edit copies), /tmp/c3w1, /tmp/c3w2, /tmp/c3w3, /tmp/c3w4, /tmp/c3w5 (worker scripts), /tmp/c3mgr". This now matches `ls -d /tmp/c3*` except /tmp/c3b, which is this 3b unit's own directory (run2). But M has 0 `$ ls -d` lines (run2), so the list still has no paste. Worker5 graded this under S1. See new finding 7.
9. W2:19 and :29. FIXED. :19 now points to M E4 ("one insertion, 0 deleted lines"), and E4's diff re-runs as `17a18,30` with 0 `<` lines (run2). :29 now carries "REPORTED by the manager (dispatches are events, not command outputs)" (run2).

Tally: FIXED 4 (items 4, 5, 6, 9). FIXED with a new defect 1 (item 2). PARTIALLY FIXED 4 (items 1, 3, 7, 8). NOT FIXED 0 in full.

### New numbered findings
1. MINOR (S1), W3:166. The lower bound rests on "the master opened [this unit] under the DECISION_LOG entry of 2026-11-12T00:37:30Z", but the backing the note cites, M E5 (M:442-445), shows only that the timestamp string occurs once and converts to 19:37:30 local. No paste in W3 or M shows the entry's content. The claim is true: run1 prints DECISION_LOG.md:842, a resume of bead n1y with Amear's go at 19:31-19:33 ET. It just is not backed where the note says.
2. MINOR (S1), W3:161-163 cited at W3:165. The note pastes `$ sed -n '379p;418p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-140`, which prints a `grep -nE` command and then `37`. Read as pasted, that is a command and its output. It is not. The `grep -nE` at worker6:379 prints numbered lines; run1 shows its first output line, `176:$ sed -n 284,313p $A`. The `37` at worker6:418 is the output of a different command, the `grep -cE` at worker6:417 (run1, run3). The figure is right (run1: 37), but the paste does not show what W3:165 says it shows.
3. MINOR (S1), M:11. "the S13 sentence once, standalone, last line, in each new report (E1 and E5 self-check output, and the self-check block at the end of this report)" (abridged). The new correction-3 worker5 report is in no self-check paste in M (run1: 0 and 0). This is the same class of gap worker4 MINOR 3 raised for worker2. The file does pass when checked now (run1).
4. MINOR (S2), M:36. "E2 shows they are the only two email hits in the bead's files". E2 scans the working-copy files, and this unit edited two of them. In the bead's own commit 83891f6, three files carry email lines: return-handoff 2, docs/reports/2026-11-11-v-rulings-filing-worker2.md 1, and docs/reports/2026-11-11-v-rulings-filing-worker5.md 1 (run2). Four of the 24 paths differ between 83891f6 and the working copy (run2). So the "only two" claim holds for the uncommitted working copy, not for the bead as committed. The sentence does not say this. The two edits are disclosed at M:34-35, but the bead-level claim is stated more strongly than E2 supports.
5. MINOR (S1), M:15, M:17, M:475. Three worker5 sub-items are not fixed. They still have no paste and no REPORTED label (run2): the three named leads in final.out (:15), worker4's tally (:17; true per worker4:747, run2), and "The brief limits MANIFEST edits to the new rows" (:475).
6. MINOR (S1/S2), M:480. The S6 basis now reads "(the Files staged list below, built by `wc -l` on each path)". No `wc -l` paste in M covers the list. The six `$ wc -l` lines in M (run2) cover the /tmp/c3pre pairs, four reports and MANIFEST. They do not cover the correction-3 worker2, worker4 or worker5 reports or M itself. M:493's "335 lines" for worker5 has no paste in M (run2), although it is true (run2: `wc -l` 335). Also, a list the manager wrote cannot show that no hook or setting was touched. This new wording adds an unpasted claim and does not fix the original one.
7. MINOR (S1), M:496. The /tmp list is now complete (run2), but no command output in M backs it (0 `$ ls -d` lines, run2).

## Result
Result: FAIL. 0 MAJOR, 7 MINOR. Of worker5's 9 findings, 4 are fixed, 1 is fixed with a new defect in its backing paste, and 4 are partially fixed. None of the defects changes a conclusion of the unit. Every claim checked is true in substance; the gaps are in the pasted backing (S1) and in one scope statement (S2).

## Self-check
Run on the final file. The block is rebuilt by /tmp/c3b/w1/assemble.sh until it equals a fresh run of /tmp/c3b/w1/self.sh on the file that contains it.
```
$ cat /tmp/c3b/w1/self.sh
#!/bin/bash
# self-check of the 3b worker1 report; counts only
cd /Volumes/Sensidine/Praxis.build || exit 1
F=docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
printf '$ %s\n' "/tmp/vrf-c2/selfcheck.sh $F"; /tmp/vrf-c2/selfcheck.sh "$F" 2>&1
printf '$ %s\n' "grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F"; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$F"
printf '$ %s\n' "grep -ciw 'v[e]rdict' $F"; grep -ciw 'v[e]rdict' "$F"
printf '$ %s\n' "grep -cE 'COMMIT[-](INDEX|DIFF[-]SHA256)' $F"; grep -cE 'COMMIT[-](INDEX|DIFF[-]SHA256)' "$F"
printf '$ %s\n' "grep -cE '\.\.\.' $F"; grep -cE '\.\.\.' "$F"
$ /tmp/c3b/w1/self.sh
$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[395] last_nonblank_line=395 last_nonblank_is_S13=YES lines=395
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
0
$ grep -ciw 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
0
$ grep -cE 'COMMIT[-](INDEX|DIFF[-]SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
0
$ grep -cE '\.\.\.' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
0
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
