# Unit 2026-11-12-v-rulings-filing-correction-3b — worker3 (ADVERSARIAL, narrow)

## Task
Mode ADVERSARIAL (narrow), unit 2026-11-12-v-rulings-filing-correction-3b, worker3. Read-only on the repo apart from this report; nothing staged, no git ref touched, nothing under vm/ or .claude/ written (REPORTED: a statement about my own actions, not a command output).
Scope: the changed lines of three reports against their pre-edit copies in /tmp/c3b/pre/ (A = docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md, B = docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md, C = docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md), plus what those lines cite. Items: (1) grade each of the 1 MAJOR + 12 MINOR of 3b-worker2 and the 7 new findings of 3b-worker1; (2) new S1/S2 and forbidden-string defects in the changed lines; (3) byte-for-byte re-runs of the A E6 block, the A:287 one-liner (N unset), the A self-check, the two B diff commands and the changed or added C commands; (4) S13 in each file.

## Criteria
- S1 (specs/SPEC_RUBRIC.md): "Every claim in a report has pasted command output, not a description of output."
- S2 (specs/SPEC_RUBRIC.md): "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S13: the S13 sentence exactly once, standalone, final non-blank line.

## Commands and output
All commands ran under bash. Two scripts; their sources and full outputs follow. Line numbers in the outputs are line numbers of the current files A, B and C. The scripts build the rep-name mask token at runtime from line 4 of /tmp/vrf-c2/selfcheck.sh and never print it; email output is masked.
```
$ cat /tmp/c3b/w3/rerun.sh
#!/bin/bash
# worker3 (3b) re-runs: compare pasted output with fresh output, byte for byte. Masked output only.
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
B=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
C=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
W=/tmp/c3b/w3
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
[ -n "$N" ] && echo "mask token built: YES"

echo "=== R1. A E6: pasted script source (A:471-495) vs /tmp/c3b/mgr/e7.sh"
sed -n '471,495p' $A > $W/e7.src.pasted
cmp $W/e7.src.pasted /tmp/c3b/mgr/e7.sh && echo e7-source-identical
echo "=== R2. A E6: pasted output (A:497-558) vs fresh run"
sed -n '497,558p' $A > $W/e7.out.pasted
/tmp/c3b/mgr/e7.sh > $W/e7.out.fresh 2>&1
wc -l < $W/e7.out.fresh | sed 's/^ */fresh_lines=/'
cmp $W/e7.out.pasted $W/e7.out.fresh && echo e7-output-identical

echo "=== R3. A:287 one-liner, run with N unset, vs A:288-289"
sed -n 287p $A | sed 's/^\$ //' > $W/a287.cmd
env -u N bash -c 'echo "N_in_child=[${N-unset}]"'
env -u N bash $W/a287.cmd > $W/a287.fresh 2>&1
sed -n '288,289p' $A > $W/a287.pasted
cmp $W/a287.pasted $W/a287.fresh && echo a287-output-identical
grep -c '(address withheld)' $W/a287.fresh

echo "=== R4. A self-check: the \$ line at A:595 vs A:596-600"
sed -n 595p $A | sed 's/^\$ //' > $W/asc.cmd
bash $W/asc.cmd > $W/asc.fresh 2>&1
sed -n '596,600p' $A > $W/asc.pasted
cmp $W/asc.pasted $W/asc.fresh && echo a-selfcheck-identical

echo "=== R5. B: the two diff commands at B:32 and B:34 vs B:33 and B:35"
for n in 32 34; do
  sed -n ${n}p $B | sed 's/^\$ //' > $W/b$n.cmd
  bash $W/b$n.cmd > $W/b$n.fresh 2>&1
  sed -n "$((n+1))p" $B > $W/b$n.pasted
  cmp $W/b$n.pasted $W/b$n.fresh && echo "B:$n output identical"
done

echo "=== R6. C: changed or added commands C:161, C:168, C:170 vs their pasted output"
sed -n 161p $C | sed 's/^\$ //' > $W/c161.cmd; bash $W/c161.cmd > $W/c161.fresh 2>&1; sed -n '162,163p' $C > $W/c161.pasted
cmp $W/c161.pasted $W/c161.fresh && echo "C:161 output identical"
sed -n 168p $C | sed 's/^\$ //' > $W/c168.cmd; bash $W/c168.cmd > $W/c168.fresh 2>&1; sed -n 169p $C > $W/c168.pasted
cmp $W/c168.pasted $W/c168.fresh && echo "C:168 output identical"
sed -n 170p $C | sed 's/^\$ //' > $W/c170.cmd; bash $W/c170.cmd > $W/c170.fresh 2>&1; sed -n 171p $C > $W/c170.pasted
cmp $W/c170.pasted $W/c170.fresh && echo "C:170 output identical"
echo "--- worker6:417 run itself (C:165 says 418 is its output); then 416-419 context"
sed -n 417p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | sed 's/^\$ //' > $W/w6417.cmd; bash $W/w6417.cmd
sed -n '416,419p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-60 | mask

echo "=== R7. A:312 claim: re-run of /tmp/c3mgr/e6.sh vs A E5 pasted output (A:354-446); which sections differ"
sed -n '354,446p' $A > $W/e6.out.pasted
/tmp/c3mgr/e6.sh > $W/e6.out.fresh 2>&1
diff $W/e6.out.pasted $W/e6.out.fresh | grep -E '^[0-9]' | tr '\n' ' '; echo
for h in $(diff $W/e6.out.pasted $W/e6.out.fresh | grep -E '^[0-9]' | sed -E 's/^([0-9]+).*/\1/'); do
  awk -v n=$h 'NR<=n && /^--- /{s=$0} NR==n{print "pasted line " n " is under section: " s}' $W/e6.out.pasted
done
$ /tmp/c3b/w3/rerun.sh > /tmp/c3b/w3/rerun.out 2>&1
$ cat /tmp/c3b/w3/rerun.out
mask token built: YES
=== R1. A E6: pasted script source (A:471-495) vs /tmp/c3b/mgr/e7.sh
e7-source-identical
=== R2. A E6: pasted output (A:497-558) vs fresh run
fresh_lines=62
e7-output-identical
=== R3. A:287 one-liner, run with N unset, vs A:288-289
N_in_child=[unset]
a287-output-identical
2
=== R4. A self-check: the $ line at A:595 vs A:596-600
a-selfcheck-identical
=== R5. B: the two diff commands at B:32 and B:34 vs B:33 and B:35
B:32 output identical
B:34 output identical
=== R6. C: changed or added commands C:161, C:168, C:170 vs their pasted output
C:161 output identical
C:168 output identical
C:170 output identical
--- worker6:417 run itself (C:165 says 418 is its output); then 416-419 context
37
176:$ sed -n 284,313p $A | grep -n "manager.md" | cut -c1-90
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-corre
37
$ for v in PA PB A B T P W5 D3 C R; do printf '%s: ' "$v"; h
=== R7. A:312 claim: re-run of /tmp/c3mgr/e6.sh vs A E5 pasted output (A:354-446); which sections differ
1c1 24c24 32,33c32,33 36c36,43 56,57c63,64 
pasted line 1 is under section: 
pasted line 24 is under section: --- finding 6: worker3 report
pasted line 32 is under section: --- finding 7: worker2 report
pasted line 36 is under section: --- finding 7: worker2 report
pasted line 56 is under section: --- S13, name, email, banned strings: every new correction-3 report except this one, and the four edited reports
```

```
$ cat /tmp/c3b/w3/claims.sh
#!/bin/bash
# worker3 (3b) scans of changed lines and claim checks. Counts, line numbers and masked text only.
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
B=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
C=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
P=/tmp/c3b/pre
W=/tmp/c3b/w3
AT=$(printf '\x40')
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }

echo "=== Q1. hunk headers of the three diffs (pre-edit copy vs current)"
for f in $A $B $C; do printf '%s: ' "${f##*/}"; diff $P/${f##*/} $f | grep -E '^[0-9]' | tr '\n' ' '; echo; done

echo "=== Q2. new-side changed lines: S1/S2 string scans (counts)"
for f in $A $B $C; do
  diff $P/${f##*/} $f | grep '^> ' | sed 's/^> //' > $W/new.${f##*/}
  printf '%s: new_lines=%s email=%s word=%s s1=%s s2=%s name_ci=%s dollar_lines=%s dots_in_dollar=%s angle_in_dollar=%s\n' "${f##*/}" \
    "$(wc -l < $W/new.${f##*/} | tr -d ' ')" \
    "$(grep -cE "$EM" $W/new.${f##*/})" \
    "$(grep -ci 'v[e]rdict' $W/new.${f##*/})" \
    "$(grep -c 'COMMIT[-]INDEX' $W/new.${f##*/})" \
    "$(grep -c 'COMMIT[-]DIFF[-]SHA256' $W/new.${f##*/})" \
    "$(grep -ci -- "$N" $W/new.${f##*/})" \
    "$(grep -c '^\$ ' $W/new.${f##*/})" \
    "$(grep '^\$ ' $W/new.${f##*/} | grep -cF '...')" \
    "$(grep '^\$ ' $W/new.${f##*/} | grep -cE '<[A-Za-z_ -]+>')"
done
echo "--- positive controls for the scans"
printf 'x a.b%sc-d.example y\n' "$AT" | grep -cE "$EM"
printf '$ cmd ... <file>\n' | grep -cF '...'
printf '$ cmd <file>\n' | grep -cE '<[A-Za-z_ -]+>'
echo "--- the <word> tokens matched in A new $ lines"
grep '^\$ ' $W/new.${A##*/} | grep -oE '<[A-Za-z_ -]+>' | mask

echo "=== Q3. A:36 claim: line numbers of the email lines in the two edited files as committed at 83891f6"
for f in docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md; do
  echo "$f at 83891f6 email_line_numbers=$(git show 83891f6:$f | grep -nE "$EM" | cut -d: -f1 | tr '\n' ' ')"
done
echo "--- is the /tmp/c3pre copy of each file identical to 83891f6?"
for f in docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md; do
  git show 83891f6:$f | cmp -s - /tmp/c3pre/${f##*/} && echo "${f##*/} c3pre==83891f6" || echo "${f##*/} c3pre!=83891f6"
done

echo "=== Q4. A:34 'public support address': does the shared address have local part 'support'? (count only)"
sed -n 114p docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | grep -ciE "(^|[^A-Za-z0-9._%+-])support$AT"
echo "--- does A paste anything that shows the word support next to that address? lines of A with 'support' inside a code block"
awk '/^```/{c=!c; next} c && /[Ss]upport/{print NR}' $A | tr '\n' ' '; echo

echo "=== Q5. A:572 vs A:468: re-check statements in the same file"
sed -n 468p $A | cut -c1-90
sed -n 572p $A | grep -oE 'These edits have NOT been re-checked by an adversarial worker\.'
grep -c '3b-worker[12]' $A
ls docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md
grep -n '^## Result' -A1 docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md | cut -c1-140

echo "=== Q6. A Files staged paths (A:579-588, without A itself) vs the paths in E6's wc -l (A:533-543)"
sed -n '579,588p' $A | grep -oE '^- [^:]+' | sed 's/^- //' | sort > $W/staged.paths
sed -n '533,543p' $A | awk '$2!="total"{print $2}' | sort > $W/wc.paths
diff $W/staged.paths $W/wc.paths && echo staged-list-equals-wc-list
wc -l < $W/staged.paths | sed 's/^ */staged_paths=/'

echo "=== Q7. A:312 claim: content of the e6.sh re-run differences (masked, cut)"
diff $W/e6.out.pasted $W/e6.out.fresh | sed -n '1,8p' | cut -c1-90 | mask
diff $W/e6.out.pasted $W/e6.out.fresh | awk '/^56,57c63,64/{p=1} p' | cut -c1-175 | mask

echo "=== Q8. A:15 lead 'undefined variables in ... the two correction-2 reports': which reports do the E6 lines name?"
sed -n '56p;64,65p' /tmp/c3w2/final.out | grep -oE 'correction-2-[a-z0-9]+\.md' | sort | uniq -c
sed -n '57,63p' /tmp/c3w2/final.out | grep -c '\$PA\|\$T\|\$P'

echo "=== Q9. whole-file checks on A, B, C"
/tmp/vrf-c2/selfcheck.sh $A $B $C
for f in $A $B $C; do echo "${f##*/}: email=$(grep -cE "$EM" $f) word=$(grep -ci 'v[e]rdict' $f) s1=$(grep -c 'COMMIT[-]INDEX' $f) s2=$(grep -c 'COMMIT[-]DIFF[-]SHA256' $f)"; done
$ cd /tmp/c3b/w3; ./claims.sh > claims.out 2>&1
$ cat /tmp/c3b/w3/claims.out
=== Q1. hunk headers of the three diffs (pre-edit copy vs current)
2026-11-12-v-rulings-filing-correction-3-manager.md: 11c11 15c15 17,18c17,18 23,24c23,24 34c34 36c36 39c39 287c287 311a312 465a467,560 467c562 475c570 477c572 480c575 490,491c585,586 495,496c590,591 498c593 501c596 
2026-11-12-v-rulings-filing-correction-3-worker2.md: 19c19 29c29,36 
2026-11-12-v-rulings-filing-correction-3-worker3.md: 161,162c161,162 165,166c165,172 
=== Q2. new-side changed lines: S1/S2 string scans (counts)
2026-11-12-v-rulings-filing-correction-3-manager.md: new_lines=115 email=0 word=0 s1=0 s2=0 name_ci=0 dollar_lines=17 dots_in_dollar=0 angle_in_dollar=1
2026-11-12-v-rulings-filing-correction-3-worker2.md: new_lines=9 email=0 word=0 s1=0 s2=0 name_ci=0 dollar_lines=2 dots_in_dollar=0 angle_in_dollar=0
2026-11-12-v-rulings-filing-correction-3-worker3.md: new_lines=10 email=0 word=0 s1=0 s2=0 name_ci=0 dollar_lines=4 dots_in_dollar=0 angle_in_dollar=0
--- positive controls for the scans
1
1
1
--- the <word> tokens matched in A new $ lines
<NAME>
=== Q3. A:36 claim: line numbers of the email lines in the two edited files as committed at 83891f6
docs/reports/2026-11-11-v-rulings-filing-worker2.md at 83891f6 email_line_numbers=169 
docs/reports/2026-11-11-v-rulings-filing-worker5.md at 83891f6 email_line_numbers=79 
--- is the /tmp/c3pre copy of each file identical to 83891f6?
2026-11-11-v-rulings-filing-worker2.md c3pre==83891f6
2026-11-11-v-rulings-filing-worker5.md c3pre==83891f6
=== Q4. A:34 'public support address': does the shared address have local part 'support'? (count only)
1
--- does A paste anything that shows the word support next to that address? lines of A with 'support' inside a code block
100 
=== Q5. A:572 vs A:468: re-check statements in the same file
Added in Correction 3b for lines the re-check found unpasted. Counts, line numbers and mas
These edits have NOT been re-checked by an adversarial worker.
0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md:365:## Result
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md-366-Result: FAIL. 0 MAJOR, 7 MINOR. Of worker5's 9 findings, 4 are fixed, 
--
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md:284:## Result
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md-285-Result: FAIL - 1 MAJOR, 12 MINOR.
=== Q6. A Files staged paths (A:579-588, without A itself) vs the paths in E6's wc -l (A:533-543)
staged-list-equals-wc-list
staged_paths=10
=== Q7. A:312 claim: content of the e6.sh re-run differences (masked, cut)
1c1
< 2026-11-11T20:36:24
---
> 2026-11-11T20:56:41
24c24
< 145a146,167
---
> 145a146,173
56,57c63,64
< docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[31] last_nonblank_line=31 last_nonblank_is_S
< docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[168] last_nonblank_line=168 last_nonblank_is
---
> docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[38] last_nonblank_line=38 last_nonblank_is_S
> docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[174] last_nonblank_line=174 last_nonblank_is
=== Q8. A:15 lead 'undefined variables in ... the two correction-2 reports': which reports do the E6 lines name?
   1 correction-2-manager.md
5
=== Q9. whole-file checks on A, B, C
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[606] last_nonblank_line=606 last_nonblank_is_S13=YES lines=606
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[38] last_nonblank_line=38 last_nonblank_is_S13=YES lines=38
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[174] last_nonblank_line=174 last_nonblank_is_S13=YES lines=174
V1 positive control (hyphen-split synthetic line): HIT_lines=1
2026-11-12-v-rulings-filing-correction-3-manager.md: email=0 word=0 s1=0 s2=0
2026-11-12-v-rulings-filing-correction-3-worker2.md: email=0 word=0 s1=0 s2=0
2026-11-12-v-rulings-filing-correction-3-worker3.md: email=0 word=0 s1=0 s2=0
```

## Findings

### Re-runs (item 3)
- A E6 (A:469-559): the pasted script source A:471-495 is byte-identical to /tmp/c3b/mgr/e7.sh (R1: `e7-source-identical`), and a fresh run is byte-identical to the pasted output A:497-558 (R2: `e7-output-identical`, 62 lines).
- A:287 one-liner, run in a child shell where N is unset (R3: `N_in_child=[unset]`): byte-identical to A:288-289 (R3: `a287-output-identical`; 2 masked addresses).
- A self-check (the `$ ` line A:595): byte-identical to A:596-600 (R4: `a-selfcheck-identical`).
- B:32 and B:34: both identical to B:33 and B:35 (R5).
- C:161, C:168, C:170 (the changed or added commands): all three identical to their pasted output (R6). The command at worker6:417 gives 37 when run, and worker6:418 is that 37 (R6), as C:165 now says.

### Grade of each 3b-worker2 item
- MAJOR 1 (A:287, N undefined). FIXED. A:287 now starts `$ N=$(` and exports N in the same command; with N unset the output still matches the paste (R3).
- MINOR 1 (A:39, mask claim). FIXED. Current text: "Output of a script that defines `mask`, or a `run()` with the same perl substitution, passes through it ... Other blocks are not masked; the self-check at the end of this report shows 0 name hits and 0 email lines in the whole file." The self-check re-runs with name_ci=0, V1_HIT_lines=0 and email count 0 (R4; Q9).
- MINOR 2 (A:11, worker5 S13). FIXED. A:11 now cites "E6 for the worker5 report"; E6 holds the worker5 selfcheck line with `last_nonblank_is_S13=YES lines=335`, and E6 re-runs identically (R2).
- MINOR 3 (A:480/493, `wc -l` basis). FIXED. A:575: "E6 pastes `wc -l` on each of them except this report". The ten Files staged paths A:579-588 are exactly the ten paths in E6's `wc -l` (Q6: `staged-list-equals-wc-list`, `staged_paths=10`).
- MINOR 4 (tallies). FIXED. A:17 "(E6: its line 747)", A:18 "(E6: its line 305)"; E6's grep shows worker4.md:747 and worker5.md:305 and re-runs (R2).
- MINOR 5 ("all seven fixed"). FIXED. A:17 now reads "all seven answered by edits (see Adversarial findings), and worker5 then found defects in some of those edits."
- MINOR 6 (helper scripts and /tmp dirs). FIXED. A:23 and A:591 cite E6's `ls -d`, which lists all three helpers and all eight directories (R2).
- MINOR 7 (A:15, the three final.out leads). PARTIALLY FIXED. A:15 now says "(E6 pastes its lines 56, 64, 65, 84, 126 and 127)". Lines 84 and 126-127 show the two quoted leads literally. The first lead is "undefined variables in other original commands of the two correction-2 reports", but lines 56 and 64-65 name only one of the two reports, the correction-2 manager report (Q8: `1 correction-2-manager.md`). Line 65 is a 0 count of definitions, so it shows nothing is defined, not that anything is used. The use lines (final.out 57-63: 5 lines with `$PA`, `$T` or `$P`, Q8) are not in E6.
- MINOR 8 (A:34, the address is MFFU's support address). PARTIALLY FIXED. A:34 now says "(E6: it is the address in the header of the MFFU reply at return-handoff line 114, same_address=YES)", and E6 shows that plus the section heading "## MFFU replies to V1 and V6" (R2). That shows it is the sender address of the MFFU reply. Nothing in A shows "support" or "public". The claim is true: the local part is `support` (Q4: count 1). But the only code-block line in A that says "support" is A:100 (Q4), the replacement words themselves, and that is not evidence.
- MINOR 9 (A:24, order of worker1's steps). FIXED. The claim is gone: "the order of its own steps is in its report and is not re-shown here."
- MINOR 10 (B:19, diff in another file, "just before" timing). FIXED. B:19 now says the diff "is pasted at the end of this note", and B:32-35 hold it (re-run identical, R5). The timing is now labelled "REPORTED by the manager".
- MINOR 11 (C:161, stitched pair). FIXED. C:161 is now `sed -n '417p;418p'`, so the paste shows a `grep -cE` command and its output 37 (R6).
- MINOR 12 (C:166, conversion not in C, "first step"). FIXED. C:168-171 paste the DECISION_LOG line and the `date` conversion (both re-run identically, R6), and "as its first step" is gone.

### Grade of each 3b-worker1 new finding
1. C:166, entry content not shown. FIXED. C:169 shows DECISION_LOG.md:842 "SECOND RESUME OF PARKED BEAD `Praxis_build-n1y`" (R6 identical), and the dispatch order is labelled REPORTED.
2. C:161-163, stitched pair. FIXED (see MINOR 11 above).
3. A:11, worker5 report not covered. FIXED (see MINOR 2 above).
4. A:36, "only two email hits in the bead's files". FIXED as raised. It now reads "in the working copy of the bead's files", and the 83891f6 counts are in E6. The sentence that was added has its own gap; see new finding 3.
5. A:15, A:17, A:570 (unpasted leads, tally, brief). PARTIALLY FIXED. The tally is pasted (R2). A:570 now carries "(REPORTED: the Correction 3 brief is not pasted in this report)". The leads are as in MINOR 7 above: one of the three is backed only in part (Q8).
6. A:575, S6 basis. FIXED. The `wc -l` covers the whole list (Q6), and the sentence now speaks of "Every file in the Files staged list", not of every file touched.
7. A:591, /tmp list. FIXED. E6's `ls -d` lists all of them (R2).

### New findings in the changed lines (item 2)
No MAJOR. In the new-side lines of the three diffs: 0 email lines, 0 for the word, 0 for each of the two strings, 0 rep-name hits, 0 `...` in `$ ` lines (Q2, positive controls 1, 1, 1). The single `<...>` token is `<NAME>`, the perl replacement string at A:287 and in e7.sh, not a placeholder argument (Q2). Every shell variable in the new `$ ` lines is defined in its own command or in its pasted script: N at A:287, and N, `$1`, `f`, `a`, `b` in e7.sh (R1). In the whole files, S13 is standalone once and last in A (606), B (38) and C (174), with name_ci=0 and V1_HIT_lines=0 (Q9).

1. MINOR (S2/S1), A:572. This line was edited in Correction 3b ("(E6; ..." added; Q1 hunk `477c572`) but still says "These edits have NOT been re-checked by an adversarial worker." (Q5). That is no longer true. A:468, in the same file, says E6 was "Added in Correction 3b for lines the re-check found unpasted". Both re-checks exist with FAIL results: 3b-worker1 "Result: FAIL. 0 MAJOR, 7 MINOR" and 3b-worker2 "Result: FAIL - 1 MAJOR, 12 MINOR" (Q5). A names neither (Q5: `3b-worker[12]` count 0). The edited line contradicts the file it sits in.
2. MINOR (S1), A:312. "re-run now, its finding 6 and finding 7 sections show those edits too." No re-run is pasted in A. When re-run, /tmp/c3mgr/e6.sh differs from the pasted E5 output in four places, not two: the date line (1c1), finding 6 (24c24), finding 7 (32,33c32,33 and 36c36,43), and also the S13 section (56,57c63,64). In that section the worker2 and worker3 selfcheck lines go from at=[31] and at=[168] to at=[38] and at=[174] (R7, Q7). The note describes output that is not pasted, and its description leaves out a section that changes.
3. MINOR (S1), A:36. "As committed at 83891f6, the two lines this unit edited also carried one address each (E6: email_lines 2, 1 and 1)." E6 pastes counts per file, not per line. Those counts do not show that the one email line in each file is the edited line. The claim is true: the email line numbers at 83891f6 are 169 and 79 (Q3), and the /tmp/c3pre copies are identical to 83891f6 (Q3). Neither fact is pasted in A.
4. MINOR (S1), A:585 and A:590. "reworded again and lines 30-36 added in Correction 3b" (B) and "lines 161-172 edited or added in Correction 3b" (C). A pastes no diff against the Correction 3b pre-edit state. E6's diffs are against the older pre-note copies (`17a18,37`, `145a146,173`), which cannot separate the 3b changes. The real 3b hunks are B `19c19 29c29,36` and C `161,162c161,162 165,166c165,172` (Q1). B's range is right. C's range "161-172" also covers C:163-164, which the 3b edit did not change.

### Observations, not graded (outside the changed lines)
- A's E5 output block (A:354-446) is now stale against a re-run in the four places listed in new finding 2. A:312 discloses that, but only in part.
- A's Result section ("Result: BLOCKED", "What it needs: one narrow ADVERSARIAL re-check of the edits made after worker5 returned") is unchanged. It does not mention the Correction 3b re-checks.

## Result
Result: FAIL. 0 MAJOR, 4 MINOR new findings (A:572, A:312, A:36, A:585/A:590). Prior items: of 3b-worker2's 13 items, 11 FIXED and 2 PARTIALLY FIXED (MINOR 7, MINOR 8). Of 3b-worker1's 7 new findings, 6 FIXED and 1 PARTIALLY FIXED (5). None NOT FIXED. Every re-run in item 3 is byte-identical to its paste, and S13 holds in A, B and C.

## Self-check
Run on this file after the last edit; the block holds the output of the command above it, re-run until it equals itself.
```
$ R=docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md; cd /Volumes/Sensidine/Praxis.build; /tmp/vrf-c2/selfcheck.sh $R; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $R; grep -ci 'v[e]rdict' $R; grep -c 'COMMIT[-]INDEX' $R; grep -c 'COMMIT[-]DIFF[-]SHA256' $R
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[317] last_nonblank_line=317 last_nonblank_is_S13=YES lines=317
V1 positive control (hyphen-split synthetic line): HIT_lines=1
0
0
0
0
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
