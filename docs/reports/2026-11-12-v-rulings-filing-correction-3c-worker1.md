# Unit 2026-11-12-v-rulings-filing-correction-3c — worker1 (ADVERSARIAL, narrow)

## Task
Mode ADVERSARIAL (narrow), unit 2026-11-12-v-rulings-filing-correction-3c, worker1, bead Praxis_build-n1y. Read-only on the repo apart from this report; nothing staged, no git ref touched, nothing under vm/ or .claude/ written (REPORTED: a statement about my own actions, not a command output). Scratch files are under /tmp/c3c/w1/.
Scope: (1) the changed lines of docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md ("A") against /tmp/c3c/pre/, graded against the items docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md left open, plus questions (a)-(c); (2) the Correction 3c manager note in docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md ("B"); (3) the new MANIFEST.md rows; (4) the closing scan /tmp/c3c/mgr/close.sh. Line numbers below are for the current files.

## Criteria
- S1 (specs/SPEC_RUBRIC.md): "Every claim in a report has pasted command output, not a description of output."
- S2 (specs/SPEC_RUBRIC.md): "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S13 (excerpt): every report under docs/reports/ carries the S13 sentence once, standalone, as its last non-blank line.
- Email rule (Amear, 2026-11-12, as given in the brief): "MFFU's public support address may appear where it is quoted from an email header or MFFU text. No other email addresses (no personal addresses, no rep addresses, no no-reply addresses). Support reps' names stay de-identified as before."
- Classes per the brief: MAJOR = false claim, email address, rep name in any form, placeholder command, missing or duplicated S13 sentence. MINOR = wording or a weakly backed claim.

## Commands and output
Every block below is a `cat` of a script followed by its run. All output goes through mask.sh (block 1), which replaces the rep's name and any email address; neither occurs in the output.

### 1. Mask filter
```
$ cat /tmp/c3c/w1/mask.sh
#!/bin/bash
# usage: some_command | /tmp/c3c/w1/mask.sh   (masks the rep name and email addresses; refuses to run if the name is empty)
cd /Volumes/Sensidine/Praxis.build || exit 1
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"
[ -n "$N" ] || { echo "mask: N empty, refusing"; exit 1; }
export N
perl -pe 's/\Q$ENV{N}\E/(name withheld)/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
```

### 2. Re-run of A's evidence blocks and self-check, byte compare (questions b and c)
```
$ cat /tmp/c3c/w1/rerun.sh
#!/bin/bash
# worker1 (3c): re-run A's script-run blocks and the self-check; compare with the pasted output byte for byte.
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
O=/tmp/c3c/w1
cmp_block() { # name first_out_line last_out_line command
  sed -n "$2,$3p" "$A" > "$O/$1.pasted"
  bash -c "$4" > "$O/$1.fresh" 2>&1
  if cmp -s "$O/$1.pasted" "$O/$1.fresh"; then echo "$1 identical ($(wc -l < "$O/$1.pasted" | tr -d ' ') lines)"; else echo "$1 DIFFERS:"; diff "$O/$1.pasted" "$O/$1.fresh" | grep -E '^[0-9]' | tr '\n' ' '; echo; fi
}
cmp_block E2 247 283 'MROWS=6 /tmp/c3mgr/scan.sh'
cmp_block E5 355 447 '/tmp/c3mgr/e6.sh'
cmp_block E6 498 559 '/tmp/c3b/mgr/e7.sh'
cmp_block SELF 597 601 "$(sed -n 596p "$A" | sed 's/^\$ //')"
# E3: run each $ line of A:295-309 and rebuild the block
sed -n 295,309p "$A" > "$O/E3.pasted"
sed -n 295,309p "$A" | grep '^\$ ' | sed 's/^\$ //' | while IFS= read -r c; do printf '$ %s\n' "$c"; bash -c "$c" 2>&1; done > "$O/E3.fresh"
if cmp -s "$O/E3.pasted" "$O/E3.fresh"; then echo "E3 identical"; else echo "E3 DIFFERS:"; diff "$O/E3.pasted" "$O/E3.fresh"; fi
$ /tmp/c3c/w1/rerun.sh | /tmp/c3c/w1/mask.sh
E2 identical (37 lines)
E5 DIFFERS:
1c1 24c24 32,33c32,33 36c36,43 56,57c63,64 
E6 DIFFERS:
41c41 47c47 
SELF identical (5 lines)
E3 DIFFERS:
2c2
< 414a415,420
---
> 414a415,426
7,8c7,8
<      420 MANIFEST.md
<      834 total
---
>      426 MANIFEST.md
>      840 total
10,15c10,15
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md 
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md 
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md 
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md 
<  /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md 
---
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md 
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md 
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md 
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md 
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md 
>  /docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md 
```

```
$ diff /tmp/c3c/w1/E6.pasted /tmp/c3c/w1/E6.fresh | /tmp/c3c/w1/mask.sh
41c41
<      420 MANIFEST.md
---
>      426 MANIFEST.md
47c47
<     3891 total
---
>     3897 total
$ diff /tmp/c3c/w1/E5.pasted /tmp/c3c/w1/E5.fresh | grep -E '^[0-9]'
1c1
24c24
32,33c32,33
36c36,43
56,57c63,64
```

### 3. B: insertion only, and re-run of the note's commands (item 2)
```
$ cat /tmp/c3c/w1/reB.sh
#!/bin/bash
# re-run each $ line of the 3b manager note (lines 32-44) and compare with the pasted block byte for byte
cd /Volumes/Sensidine/Praxis.build || exit 1
B=docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md
sed -n 32,44p "$B" > /tmp/c3c/w1/B.pasted
sed -n 32,44p "$B" | grep '^\$ ' | sed 's/^\$ //' | while IFS= read -r c; do printf '$ %s\n' "$c"; bash -c "$c" 2>&1; done > /tmp/c3c/w1/B.fresh
if cmp -s /tmp/c3c/w1/B.pasted /tmp/c3c/w1/B.fresh; then echo "B-note identical ($(wc -l < /tmp/c3c/w1/B.pasted | tr -d ' ') lines)"; else echo "B-note DIFFERS"; diff /tmp/c3c/w1/B.pasted /tmp/c3c/w1/B.fresh; fi
```
```
$ diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -v '^>'; diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3b-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -c '^<'
28a29,47
0
$ /tmp/c3c/w1/reB.sh | /tmp/c3c/w1/mask.sh
B-note identical (13 lines)
```

### 4. Lines each grade rests on (A changed lines, MANIFEST rows, B note, close.sh coverage)
```
$ cat /tmp/c3c/w1/ev.sh
#!/bin/bash
# worker1 (3c): the lines each grade rests on. Text lines are cut; run through mask.sh.
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
B=docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
echo "--- 1. hunks of A against its pre-edit copy"
r "diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md $A | grep -E '^[0-9]'"
echo "--- 2. A:15 lead wording (MINOR 7, item 5)"
r "sed -n 15p $A | grep -oE 'passed to worker3 as fix items[^:]*: [^,]*, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report'"
r "grep -c 'undefined variables in other original commands' $A"
echo "--- 3. A:34 sender address (MINOR 8) and the header line it is backed by"
r "sed -n 34p $A | grep -oE 'giving the sender address of the MFFU reply itself'"
r "sed -n 34p $A | grep -o 'public' | wc -l | tr -d ' '"
r "sed -n 288p $A | grep -oE '^### Reply to V1 .{24}, from \(address withheld\)'"
echo "--- 4. A:36 per-file wording (new 3) and what this unit edited per Files staged"
r "sed -n 36p $A | grep -oE 'the two files this unit edited also carried one email line each \(E6: email_lines 2, 1 and 1\)'"
r "sed -n '578,592p' $A | grep -E '^- docs/reports/2026-11-11-|^- MANIFEST' | grep -E ' edited' | cut -d: -f1"
echo "--- 5. A:573 (new 1), A:313 (new 2), A:586 and A:591 (new 4)"
r "grep -c 'NOT re-checked' $A"
r "sed -n 573p $A | grep -oE 'the worker2 note \(pointer to E4, REPORTED label on dispatches\)\.\$'"
r "sed -n 313p $A"
r "grep -c 're-run now' $A"
r "sed -n '586p;591p' $A | grep -oE 'REPORTED: edited (again )?in Correction 3b'"
echo "--- 6. A:293 note and the MANIFEST state it describes"
r "sed -n 293p $A"
r "wc -l /tmp/c3c/pre/MANIFEST.md MANIFEST.md"
r "diff -d /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -v '^>'"
r "diff -d /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -c '^<'"
echo "--- 7. E2 scans the last MROWS rows of MANIFEST.md; which rows those are now"
r "sed -n 242p $A"
r "sed -n '246p;282p' $A | sed 's/^/A-line: /'"
r "sed -n 285p $A | grep -oE 'in the new MANIFEST rows'"
r "tail -n 6 MANIFEST.md | cut -d'|' -f2"
echo "--- 8. MANIFEST rows 421-424 against the files they name"
r "sed -n 421p MANIFEST.md | grep -oE 'carries no result of its own'"
r "grep -n '^Result' $B"
r "sed -n '422,424p' MANIFEST.md | grep -oE 'FAIL with [0-9]+ (new )?MINOR, [0-9]+ MAJOR|FAIL with [0-9]+ MAJOR, [0-9]+ MINOR'"
r "grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md | cut -c1-110"
r "grep -m1 -oE 'worker[0-9] \(ADVERSARIAL[^)]*\)|worker[0-9], ADVERSARIAL|worker[0-9] - ADVERSARIAL|worker2 \(ADVERSARIAL\)' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md"
r "sed -n 426p MANIFEST.md | grep -oE 'ADVERSARIAL worker 1 report for unit 2026-11-12-v-rulings-filing-correction-3c'"
echo "--- 9. the 3b manager note: what it says is shown, and what is shown"
r "sed -n 30p $B | grep -oE 'the row and its words are shown below'"
r "sed -n '32,35p' $B | sed 's/^/B-line: /'"
r "grep -c '2026-11-12T02:01:00Z' DECISION_LOG.md"
echo "--- 10. close.sh: is the split-letter check applied to the MANIFEST added lines"
r "grep -n 'manifest_added' /tmp/c3c/mgr/close.sh | cut -c1-90"
r "sed -n '32p;48p' /tmp/c3c/mgr/close.sh"
r "perl -CSD -Mutf8 -n /tmp/c3c/w1/v1.pl /tmp/c3c/mgr/manifest_added.txt"
echo "--- 11. extra backing: A:34 'public' contexts, worker6 lead in final.out, regen.py, close.sh path coverage"
r "sed -n 34p $A | grep -oE '.{0,22}public.{0,22}'"
r "sed -n '72,75p' /tmp/c3w2/final.out | cut -c1-120 | sed 's/^/final.out: /'"
r "ls /tmp/c3c/mgr/regen.py"
r "for p in 3-manager 3-worker3 3-worker1 3-worker2 3-worker4 3-worker5 3b-manager 3b-worker1 3b-worker2 3b-worker3 3c-manager 3c-worker1; do printf '%s ' \"\$(grep -c \"docs/reports/2026-11-12-v-rulings-filing-correction-\$p.md\" /tmp/c3c/mgr/close.sh)\"; done; for p in correction-2-manager correction-2-worker6 worker2 worker5; do printf '%s ' \"\$(grep -c \"docs/reports/2026-11-11-v-rulings-filing-\$p.md\" /tmp/c3c/mgr/close.sh)\"; done; echo"
$ /tmp/c3c/w1/ev.sh | /tmp/c3c/w1/mask.sh
--- 1. hunks of A against its pre-edit copy
$ diff /tmp/c3c/pre/2026-11-12-v-rulings-filing-correction-3-manager.md docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -E '^[0-9]'
15c15
34c34
36c36
292a293
312c313
572c573
585c586
590c591
593c594
596c597
--- 2. A:15 lead wording (MINOR 7, item 5)
$ sed -n 15p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'passed to worker3 as fix items[^:]*: [^,]*, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report'
passed to worker3 as fix items (the passing on is REPORTED): placeholder commands in the original bodies that Correction 3 does not re-run, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report
$ grep -c 'undefined variables in other original commands' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
--- 3. A:34 sender address (MINOR 8) and the header line it is backed by
$ sed -n 34p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'giving the sender address of the MFFU reply itself'
giving the sender address of the MFFU reply itself
$ sed -n 34p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -o 'public' | wc -l | tr -d ' '
2
$ sed -n 288p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE '^### Reply to V1 .{24}, from \(address withheld\)'
### Reply to V1 — 2026-11-10T19:43:42Z, from (address withheld)
--- 4. A:36 per-file wording (new 3) and what this unit edited per Files staged
$ sed -n 36p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'the two files this unit edited also carried one email line each \(E6: email_lines 2, 1 and 1\)'
the two files this unit edited also carried one email line each (E6: email_lines 2, 1 and 1)
$ sed -n '578,592p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -E '^- docs/reports/2026-11-11-|^- MANIFEST' | grep -E ' edited' | cut -d: -f1
- docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
- docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
- docs/reports/2026-11-11-v-rulings-filing-worker2.md
- docs/reports/2026-11-11-v-rulings-filing-worker5.md
- MANIFEST.md
--- 5. A:573 (new 1), A:313 (new 2), A:586 and A:591 (new 4)
$ grep -c 'NOT re-checked' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
$ sed -n 573p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'the worker2 note \(pointer to E4, REPORTED label on dispatches\)\.$'
the worker2 note (pointer to E4, REPORTED label on dispatches).
$ sed -n 313p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
Correction 3b note: the output below was captured in Correction 3, before the Correction 3b edits to the worker2 and worker3 reports. E6 pastes the current diffs.
$ grep -c 're-run now' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
0
$ sed -n '586p;591p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'REPORTED: edited (again )?in Correction 3b'
REPORTED: edited again in Correction 3b
REPORTED: edited in Correction 3b
--- 6. A:293 note and the MANIFEST state it describes
$ sed -n 293p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
Correction 3c note (REPORTED): rows were appended to MANIFEST.md after line 420 in Correction 3c, after E3 and E6 were captured; E3, E6 and the Files staged count show MANIFEST.md as it was then.
$ wc -l /tmp/c3c/pre/MANIFEST.md MANIFEST.md
     420 /tmp/c3c/pre/MANIFEST.md
     426 MANIFEST.md
     846 total
$ diff -d /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -v '^>'
420a421,426
$ diff -d /tmp/c3c/pre/MANIFEST.md MANIFEST.md | grep -c '^<'
0
--- 7. E2 scans the last MROWS rows of MANIFEST.md; which rows those are now
$ sed -n 242p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
tail -n "${MROWS:-4}" MANIFEST.md > /tmp/c3mgr/manifest_tail.txt
$ sed -n '246p;282p' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | sed 's/^/A-line: /'
A-line: $ MROWS=6 /tmp/c3mgr/scan.sh
A-line: MANIFEST.md last 6 rows email_lines=0 name_ci=0 name_split=0
$ sed -n 285p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE 'in the new MANIFEST rows'
in the new MANIFEST rows
$ tail -n 6 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md 
--- 8. MANIFEST rows 421-424 against the files they name
$ sed -n 421p MANIFEST.md | grep -oE 'carries no result of its own'
carries no result of its own
$ grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md
27:Result: BLOCKED (skeleton; not yet filled)
$ sed -n '422,424p' MANIFEST.md | grep -oE 'FAIL with [0-9]+ (new )?MINOR, [0-9]+ MAJOR|FAIL with [0-9]+ MAJOR, [0-9]+ MINOR'
FAIL with 7 MINOR, 0 MAJOR
FAIL with 1 MAJOR, 12 MINOR
FAIL with 4 new MINOR, 0 MAJOR
$ grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md | cut -c1-110
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md:366:Result: FAIL. 0 MAJOR, 7 MINOR. Of worke
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md:285:Result: FAIL - 1 MAJOR, 12 MINOR.
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md:303:Result: FAIL. 0 MAJOR, 4 MINOR new findi
$ grep -m1 -oE 'worker[0-9] \(ADVERSARIAL[^)]*\)|worker[0-9], ADVERSARIAL|worker[0-9] - ADVERSARIAL|worker2 \(ADVERSARIAL\)' docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md:worker1 (ADVERSARIAL)
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md:worker2 (ADVERSARIAL)
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md:worker3 (ADVERSARIAL, narrow)
$ sed -n 426p MANIFEST.md | grep -oE 'ADVERSARIAL worker 1 report for unit 2026-11-12-v-rulings-filing-correction-3c'
ADVERSARIAL worker 1 report for unit 2026-11-12-v-rulings-filing-correction-3c
--- 9. the 3b manager note: what it says is shown, and what is shown
$ sed -n 30p docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | grep -oE 'the row and its words are shown below'
the row and its words are shown below
$ sed -n '32,35p' docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md | sed 's/^/B-line: /'
B-line: $ grep -c '2026-11-12T02:01:00Z' DECISION_LOG.md
B-line: 1
B-line: $ grep '2026-11-12T02:01:00Z' DECISION_LOG.md | grep -o 'STOPPED AT ITS 60-TURN CAP'
B-line: STOPPED AT ITS 60-TURN CAP
$ grep -c '2026-11-12T02:01:00Z' DECISION_LOG.md
1
--- 10. close.sh: is the split-letter check applied to the MANIFEST added lines
$ grep -n 'manifest_added' /tmp/c3c/mgr/close.sh | cut -c1-90
8:git diff HEAD -- MANIFEST.md | grep '^+' | grep -v '^+++' > /tmp/c3c/mgr/manifest_added.
9:echo "MANIFEST.md added lines vs HEAD: $(wc -l < /tmp/c3c/mgr/manifest_added.txt | tr -d
28:  /tmp/c3c/mgr/manifest_added.txt; do
$ sed -n '32p;48p' /tmp/c3c/mgr/close.sh
/tmp/vrf-c2/selfcheck.sh \
  docs/reports/2026-11-11-v-rulings-filing-worker5.md
$ perl -CSD -Mutf8 -n /tmp/c3c/w1/v1.pl /tmp/c3c/mgr/manifest_added.txt
0
--- 11. extra backing: A:34 'public' contexts, worker6 lead in final.out, regen.py, close.sh path coverage
$ sed -n 34p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -oE '.{0,22}public.{0,22}'
:114, 132). This is a public company address. Kept
old the words `MFFU's public support address`; the
$ sed -n '72,75p' /tmp/c3w2/final.out | cut -c1-120 | sed 's/^/final.out: /'
final.out: $ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE "^\\$ .*\\$\{?(A|PA|B)\b"
final.out: 26
final.out: $ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE "(^|[^A-Za-z0-9_])(A|PA|B)="
final.out: 0
$ ls /tmp/c3c/mgr/regen.py
/tmp/c3c/mgr/regen.py
$ for p in 3-manager 3-worker3 3-worker1 3-worker2 3-worker4 3-worker5 3b-manager 3b-worker1 3b-worker2 3b-worker3 3c-manager 3c-worker1; do printf '%s ' "$(grep -c "docs/reports/2026-11-12-v-rulings-filing-correction-$p.md" /tmp/c3c/mgr/close.sh)"; done; for p in correction-2-manager correction-2-worker6 worker2 worker5; do printf '%s ' "$(grep -c "docs/reports/2026-11-11-v-rulings-filing-$p.md" /tmp/c3c/mgr/close.sh)"; done; echo
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
```

### 5. Negative tests of close.sh's checks on planted files (item 4)
```
$ cat /tmp/c3c/w1/plant.sh
#!/bin/bash
# worker1 (3c): negative tests for close.sh. Planted files are built at runtime; nothing planted is printed.
cd /Volumes/Sensidine/Praxis.build || exit 1
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
P=/tmp/c3c/w1/plant; rm -rf "$P"; mkdir -p "$P"
eval "$(grep '^S=' /tmp/vrf-c2/selfcheck.sh)"
AT=$(printf '\x40'); W="verd"; W="${W}ict"; X1="COMMIT-"; X1="${X1}INDEX"; X2="COMMIT-"; X2="${X2}DIFF-SHA256"
printf 'a\nmail me at q.r%sexample.org now\n\n%s\n' "$AT" "$S" > "$P/email.md"
printf 'a\nrep was %s here\n\n%s\n' "$(echo "$N" | tr a-z A-Z)" "$S" > "$P/name.md"
printf 'a\nrep was %s here\n\n%s\n' "$(echo "$N" | sed 's/./&. /g')" "$S" > "$P/split.md"
printf 'a\nthe %s is in\n\n%s\n' "$(echo "$W" | sed 's/^v/V/')" "$S" > "$P/word.md"
printf 'a\n%s and %s\n\n%s\n' "$X1" "$X2" "$S" > "$P/strings.md"
printf 'a\n%s\n\n%s\n' "$S" "$S" > "$P/s13twice.md"
printf 'a\nb\n' > "$P/s13missing.md"
printf 'a\n%s\nb\n' "$S" > "$P/s13notlast.md"
printf 'a\n  %s\n' "$S" > "$P/s13indented.md"
# the per-file line of close.sh, taken from its source and evaluated as is
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
L=$(grep -F 'echo "$f: email=' /tmp/c3c/mgr/close.sh)
echo "close.sh per-file line found: $([ -n "$L" ] && echo YES || echo NO)"
for f in "$P"/*.md; do eval "$L"; done | sed "s#$P/#plant/#"
echo "--- selfcheck.sh on the planted files (close.sh's S13 and split check)"
/tmp/vrf-c2/selfcheck.sh "$P"/*.md | sed "s#$P/#plant/#"
echo "--- is selfcheck.sh (the split-letter check) run on the MANIFEST added lines in close.sh?"
grep -n 'selfcheck.sh' /tmp/c3c/mgr/close.sh | cut -d: -f1 | tr '\n' ' '; echo
grep -c 'manifest_added.txt' /tmp/c3c/mgr/close.sh
awk '/selfcheck.sh \\/{f=1} f&&/manifest_added/{print "selfcheck block names manifest_added: YES"; found=1} f&&!/\\$/{f=0} END{if(!found) print "selfcheck block names manifest_added: NO"}' /tmp/c3c/mgr/close.sh
$ /tmp/c3c/w1/plant.sh | /tmp/c3c/w1/mask.sh
close.sh per-file line found: YES
plant/email.md: email=1 name_ci=0 word_ci=0 s1=0 s2=0
plant/name.md: email=0 name_ci=1 word_ci=0 s1=0 s2=0
plant/s13indented.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
plant/s13missing.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
plant/s13notlast.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
plant/s13twice.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
plant/split.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
plant/strings.md: email=0 name_ci=0 word_ci=0 s1=1 s2=1
plant/word.md: email=0 name_ci=0 word_ci=1 s1=0 s2=0
--- selfcheck.sh on the planted files (close.sh's S13 and split check)
plant/email.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
plant/name.md: name_ci=1 V1_HIT_lines=1 S13_containing=1 S13_standalone=1 at=[4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
plant/s13indented.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=0 at=[] last_nonblank_line=2 last_nonblank_is_S13=NO lines=2
plant/s13missing.md: name_ci=0 V1_HIT_lines=0 S13_containing=0 S13_standalone=0 at=[] last_nonblank_line=2 last_nonblank_is_S13=NO lines=2
plant/s13notlast.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[2] last_nonblank_line=3 last_nonblank_is_S13=NO lines=3
plant/s13twice.md: name_ci=0 V1_HIT_lines=0 S13_containing=2 S13_standalone=2 at=[2 4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
plant/split.md: name_ci=0 V1_HIT_lines=1 S13_containing=1 S13_standalone=1 at=[4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
plant/strings.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
plant/word.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[4] last_nonblank_line=4 last_nonblank_is_S13=YES lines=4
V1 positive control (hyphen-split synthetic line): HIT_lines=1
--- is selfcheck.sh (the split-letter check) run on the MANIFEST added lines in close.sh?
4 31 32 
3
selfcheck block names manifest_added: NO
```

```
$ cat /tmp/c3c/w1/v1.pl
# split-letter detector, same regex as /tmp/vrf-c2/selfcheck.sh; reads N from the environment, prints a count only
BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n, "\n" }
```

### 6. The closing scan itself (item 4), run after this report's last edit
```
$ cat /tmp/c3c/mgr/close.sh
#!/bin/bash
# Correction 3c closing scan. Counts and line numbers only; the rep's name, the word and the two strings are built at runtime and never printed.
cd /Volumes/Sensidine/Praxis.build || exit 1
eval "$(sed -n 4p /tmp/vrf-c2/selfcheck.sh)"; export N
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
W="verd"; W="${W}ict"; X1="COMMIT-"; X1="${X1}INDEX"; X2="COMMIT-"; X2="${X2}DIFF-SHA256"
[ -n "$N" ] && echo "name token built: YES"
git diff HEAD -- MANIFEST.md | grep '^+' | grep -v '^+++' > /tmp/c3c/mgr/manifest_added.txt
echo "MANIFEST.md added lines vs HEAD: $(wc -l < /tmp/c3c/mgr/manifest_added.txt | tr -d ' ')"
echo "--- per file: email lines, rep-name lines, word lines, string-1 lines, string-2 lines"
for f in \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md \
  docs/reports/2026-11-11-v-rulings-filing-worker2.md \
  docs/reports/2026-11-11-v-rulings-filing-worker5.md \
  /tmp/c3c/mgr/manifest_added.txt; do
  echo "$f: email=$(grep -cE "$EM" "$f") name_ci=$(grep -ci -- "$N" "$f") word_ci=$(grep -ci -- "$W" "$f") s1=$(grep -c -- "$X1" "$f") s2=$(grep -c -- "$X2" "$f")"
done
echo "--- S13 and split-name check per report (selfcheck.sh)"
/tmp/vrf-c2/selfcheck.sh \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md \
  docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md \
  docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md \
  docs/reports/2026-11-11-v-rulings-filing-worker2.md \
  docs/reports/2026-11-11-v-rulings-filing-worker5.md
echo "--- positive controls (synthetic lines built at runtime, never printed)"
AT=$(printf '\x40'); printf 'x a.b%sc-d.example y\n' "$AT" | grep -cE "$EM"
printf 'x %s y\n' "$N" | grep -ci -- "$N"
printf 'x %s y\n' "$(echo "$W" | tr a-z A-Z)" | grep -ci -- "$W"
printf 'x %s %s y\n' "$X1" "$X2" | grep -c -- "$X1"
printf 'x %s y\n' "$X2" | grep -c -- "$X2"
$ /tmp/c3c/mgr/close.sh | /tmp/c3c/w1/mask.sh
name token built: YES
MANIFEST.md added lines vs HEAD: 47
--- per file: email lines, rep-name lines, word lines, string-1 lines, string-2 lines
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-worker2.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
docs/reports/2026-11-11-v-rulings-filing-worker5.md: email=0 name_ci=0 word_ci=0 s1=0 s2=0
/tmp/c3c/mgr/manifest_added.txt: email=0 name_ci=0 word_ci=0 s1=0 s2=0
--- S13 and split-name check per report (selfcheck.sh)
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[607] last_nonblank_line=607 last_nonblank_is_S13=YES lines=607
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[174] last_nonblank_line=174 last_nonblank_is_S13=YES lines=174
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[678] last_nonblank_line=678 last_nonblank_is_S13=YES lines=678
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[38] last_nonblank_line=38 last_nonblank_is_S13=YES lines=38
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[749] last_nonblank_line=749 last_nonblank_is_S13=YES lines=749
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
docs/reports/2026-11-12-v-rulings-filing-correction-3b-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[48] last_nonblank_line=48 last_nonblank_is_S13=YES lines=48
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[395] last_nonblank_line=395 last_nonblank_is_S13=YES lines=395
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[306] last_nonblank_line=306 last_nonblank_is_S13=YES lines=306
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[317] last_nonblank_line=317 last_nonblank_is_S13=YES lines=317
docs/reports/2026-11-12-v-rulings-filing-correction-3c-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[29] last_nonblank_line=29 last_nonblank_is_S13=YES lines=29
docs/reports/2026-11-12-v-rulings-filing-correction-3c-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[501] last_nonblank_line=501 last_nonblank_is_S13=YES lines=501
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[590] last_nonblank_line=590 last_nonblank_is_S13=YES lines=590
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[487] last_nonblank_line=487 last_nonblank_is_S13=YES lines=487
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=3 S13_standalone=1 at=[179] last_nonblank_line=179 last_nonblank_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[241] last_nonblank_line=241 last_nonblank_is_S13=YES lines=241
V1 positive control (hyphen-split synthetic line): HIT_lines=1
--- positive controls (synthetic lines built at runtime, never printed)
1
1
1
1
1
```

## Findings

### Grades of the open items (pre-edit line numbers in brackets)
- 3b-worker2 MINOR 7 and 3b-worker1 item 5, A:15 (the leads in worker2's evidence file). CURED. The first lead now reads "placeholder commands in the original bodies that Correction 3 does not re-run, with no definition of P, PA or T in the first 205 lines of the correction-2 manager report". That is the section title at final.out:56 plus the count 0 at final.out:64-65, both pasted in A's E6 (block 4, item 2: old phrase count 0; E6 re-run differs only in the MANIFEST lines, block 2). Not graded: final.out:72-75 also hold a worker6 lead (26 command lines using A, PA or B, 0 definitions; block 4, item 11) that A:15 no longer mentions. A:15 does not say the list is complete, so this leaves it short, not false.
- 3b-worker2 MINOR 8, A:34 (address called public and support). CURED. A:34 now says "the sender address of the MFFU reply itself". A:288 pastes line 114 as "from (address withheld)" and E6 pastes same_address=YES (block 4, item 3). The two remaining "public" hits on A:34 are inside quotes: the old disposition text and the replacement words (block 4, item 11).
- 3b-worker3 new 1, A:573 [572] ("NOT re-checked"). CURED. The sentence is gone: count 0, and the line ends at "the worker2 note (pointer to E4, REPORTED label on dispatches)." (block 4, item 5).
- 3b-worker3 new 2, A:313 [312] (re-run described but not pasted). CURED. "re-run now" count 0; the note now claims only that E5 was captured before the 3b edits. Consistent with the re-run: E5 differs from its paste in the same five hunks 3b-worker3 found (1c1 date, 24c24, 32,33c32,33, 36c36,43, 56,57c63,64), and in no other hunk (block 2).
- 3b-worker3 new 3, A:36 (per-line claim, per-file counts). CURED as raised: the claim is now per file ("one email line each", E6 counts 1 and 1). The new wording has its own defect; see MINOR 1.
- 3b-worker3 new 4, A:586 [585] and A:591 [590] (3b line ranges with no diff). CURED. The ranges are gone; both lines now carry "REPORTED: edited (again) in Correction 3b" (block 4, item 5).

### Questions (a)-(c)
- (a) One changed line is inaccurate (MINOR 1). The A:293 note is labelled REPORTED and matches the files: /tmp/c3c/pre/MANIFEST.md has 420 lines, MANIFEST.md has 426, the change is `420a421,426` with 0 `<` lines (block 4, item 6). A:594 names /tmp/c3c/mgr/regen.py, which exists (block 4, item 11).
- (b) The self-check block A:597-601 equals a fresh run of the `$ ` command at A:596: "SELF identical (5 lines)" (block 2).
- (c) E3 differs from a re-run only in MANIFEST-dependent lines (2c2, 7-8, 10-15), and E6 only at 41 and 47 (MANIFEST.md 420 to 426, and the total) (block 2). Both are covered by the A:293 note, and so is the Files staged count at A:584. E2 re-runs byte-identical, but it no longer checks the same rows; see MINOR 2.

### MAJOR
None. Block 6 shows email=0, name_ci=0 and V1_HIT_lines=0 for every file in scope, including A, B and this report, and for the MANIFEST added lines (email 0, name 0; split-letter count 0 in block 4, item 10). Block 4, item 1 shows the A hunks contain no `$ ` line. B's four new `$ ` lines use no variables and re-run byte-identical (block 3). S13 is standalone once and last in A (607), B (48) and every other report in scope (block 6).

### MINOR
1. A:36 (changed line), S1 wording. "the two files this unit edited also carried one email line each". A's own Files staged marks five paths as edited: four existing reports plus MANIFEST.md (block 4, item 4). The two files meant are filing-worker2 and filing-worker5, the ones whose address lines were changed, and the E6 counts for those two (1 and 1) are true. The noun phrase is wrong; the counted fact is right. I class it MINOR, not MAJOR, because the parenthetical "(E6: email_lines 2, 1 and 1)" fixes which files are meant.
2. A:293 (changed line) and A:285 (E2), S1. The note names E3, E6 and the Files staged count as showing MANIFEST.md "as it was then". It does not name E2. E2 scans `tail -n "${MROWS:-4}" MANIFEST.md` with MROWS=6 (A:242, A:246). A:285 says that is "the new MANIFEST rows". A re-run gives the same bytes ("E2 identical (37 lines)", block 2), but the last 6 rows are now the 3b and 3c rows, not correction-3 rows 415-420 (block 4, item 7). A reader who re-runs E2 gets a matching line that checks different rows, and nothing in A says so. The current rows are clean either way (block 6: manifest_added email=0 name_ci=0).
3. MANIFEST.md:421 (new row), S1 wording. "carries no result of its own" does not match the file's own Result line: B:27 is "Result: BLOCKED (skeleton; not yet filled)" (block 4, item 8). The row should quote that line. Not MAJOR, because the file's own parenthetical says the result was never filled in. Rows 422-424 match their files' Result lines: 0/7, 1/12 and 0/4 (MAJOR/MINOR), all ADVERSARIAL. Row 426 has the right mode and unit (block 4, item 8).
4. B:30 (manager note), S1 wording. "the row and its words are shown below". The block shows a count (1) and the four-word phrase `STOPPED AT ITS 60-TURN CAP`. It does not show the row (block 4, item 9). The REPORTED event is otherwise backed, and the re-run is byte-identical (block 3).
5. /tmp/c3c/mgr/close.sh, scan coverage. It names all 16 report paths in scope twice each (block 4, item 11: sixteen 2s) and scans the MANIFEST added lines against HEAD (47 lines) for email, name, the word and the two strings. The split-letter check (selfcheck.sh, close.sh lines 32-48) is run on the 16 reports only, not on manifest_added.txt (block 4, item 10). The same regex run by me on that file gives 0 (block 4, item 10). This is a coverage gap with no hit. Every other check fires on its planted file (block 5): email 1, name 1, split 1 (V1 only), word 1, strings 1 and 1, S13 duplicated (standalone=2), missing (0), not last (NO) and indented (standalone=0). The five built-in positive controls print 1 each (block 6). Not graded: with an empty name token the name control still prints 1 (`grep -ci -- ""` matches); the only signal is the missing "name token built: YES" line, and every name_ci count would then be nonzero.

## Result
Result: FAIL. 0 MAJOR, 5 MINOR (A:36; A:293/A:285 E2 drift; MANIFEST.md:421; B:30; close.sh split-letter coverage of the MANIFEST added lines). Open items: of the eight graded (3b-worker2 MINOR 7 and 8, 3b-worker1 item 5, 3b-worker3 new 1-4), all are CURED and none is PARTLY CURED or NOT CURED; new 3 is cured as raised, but its new wording is MINOR 1. A's self-check equals a fresh run. E3 and E6 differ only where the A:293 note says they would. B is an insertion only, and its pasted commands re-run byte-identical.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
