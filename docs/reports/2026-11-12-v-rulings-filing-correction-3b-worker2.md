# 2026-11-12 v-rulings filing correction 3b - worker2 (ADVERSARIAL)

## Task
Unit 2026-11-12-v-rulings-filing-correction-3b, worker2, ADVERSARIAL. Read-only on the repo apart from this report. Artifacts: (A) docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md, all 511 lines; (B) docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md lines 18-30; (C) docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md lines 146-167; for checks 6 and 7, all three whole files. Nothing was staged or committed by me; my scripts and outputs are in /tmp/c3b/w2/.

## Criteria
- S1 (specs/SPEC_RUBRIC.md): "Every claim in a report has pasted command output, not a description of output."
- S2 (specs/SPEC_RUBRIC.md): "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- S13: every report carries the S13 sentence once, as a standalone final line.
- Grading per the brief: MAJOR is a rule breach (email address, rep name, forbidden string, missing or duplicated S13 line, non-literal command presented as run). MINOR is an unsupported or over-graded claim.

## Commands and output
All scripts ran under bash. Each is shown with `cat`, followed by the command that ran it and its full output. The rep's name is built at runtime as `N` and never printed. Any output text from other files goes through `mask`.

### mech.sh
```
$ cat /tmp/c3b/w2/mech.sh
#!/bin/bash
# mechanical checks 2,3,4,6,7 plus spot re-runs; prints counts, line numbers and masked text only
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
B=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
C=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
OB='[A-Za-z0-9._-]+ *(\[at\]|\(at\)|\{at\}| at ) *[A-Za-z0-9-]+ *(\.|\[dot\]|\(dot\)| dot ) *[A-Za-z]{2,}'
F1=$(printf '%s-%s' COMMIT INDEX); F2=$(printf '%s-%s-%s' COMMIT DIFF SHA256)
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
date "+%Y-%m-%dT%H:%M:%S"
echo "--- check 3: email regex and obfuscated forms (counts and line numbers only)"
for f in $A $B $C; do
  echo "$f email_lines=$(grep -cE "$EM" $f) at=[$(grep -nE "$EM" $f | cut -d: -f1 | tr '\n' ' ')] obfusc_lines=$(grep -ciE "$OB" $f) at=[$(grep -niE "$OB" $f | cut -d: -f1 | tr '\n' ' ')]"
done
echo "positive controls: email=$(printf 'a.b%sc-d.example\n' '@' | grep -cE "$EM") obfusc=$(printf 'a.b %s c-d %s example\n' '[at]' 'dot' | grep -ciE "$OB")"
echo "--- checks 4 and 6: selfcheck"
/tmp/vrf-c2/selfcheck.sh $A $B $C
echo "--- check 7: forbidden strings, whole files"
for f in $A $B $C; do
  echo "$f word_ci=$(grep -ci 'v[e]rdict' $f) word_ci_w=$(grep -ciw 'v[e]rdict' $f) F1_fixed=$(grep -cF -- "$F1" $f) F2_fixed=$(grep -cF -- "$F2" $f)"
done
echo "positive controls: F1=$(printf 'x %s y\n' "$F1" | grep -cF -- "$F1") F2=$(printf 'x %s y\n' "$F2" | grep -cF -- "$F2") word=$(printf 'x V%sRDICT y\n' E | grep -ci 'v[e]rdict')"
echo "line 500 of A: F1_fixed=$(sed -n 500p $A | grep -cF -- "$F1") F2_fixed=$(sed -n 500p $A | grep -cF -- "$F2") word_ci=$(sed -n 500p $A | grep -ci 'v[e]rdict') COMMIT_hyphen_paren=$(sed -n 500p $A | grep -c 'COMMIT-(INDEX|DIFF-SHA256)')"
echo "--- check 2: dollar-prompt lines inside code blocks, with ellipsis, angle placeholder, or a shell variable"
for f in $A $B $C; do
  awk -v F="$f" '/^```/{inb=!inb; next} inb && /^\$ /{ e=index($0,"...")>0; p=($0 ~ /<[A-Za-z][^>]*>/); v=($0 ~ /\$[A-Za-z_{(]/ && substr($0,3) ~ /\$[A-Za-z_{]/); if(e||p||v) printf "%s:%d ellipsis=%d angle=%d var=%d\n", F, NR, e, p, v }' $f
done
echo "--- check 2: does the block holding A:287 define N"
awk 'NR>=286 && NR<=290' $A | grep -c '^\$ N=\|^N='
echo "--- pasted script sources vs current files in /tmp/c3mgr"
for s in "v1.sh 44 69" "v2.sh 141 152" "scan.sh 218 245" "e6.sh 314 351"; do set -- $s
  if diff -q <(cat /tmp/c3mgr/$1) <(sed -n "$2,$3p" $A) >/dev/null; then echo "$1 A:$2-$3 identical"; else echo "$1 A:$2-$3 DIFFERS difflines=$(diff <(cat /tmp/c3mgr/$1) <(sed -n "$2,$3p" $A) | wc -l | tr -d ' ')"; fi
done
echo "--- A:39 says output passes through mask: mask/perl mentions per script"
for s in v1.sh v2.sh scan.sh e6.sh; do echo "$s mask_or_perl_subst_lines=$(grep -c 'mask\|perl -pe' /tmp/c3mgr/$s)"; done
echo "--- A:11 and A:470 S13 coverage: selfcheck commands in A naming the worker5 report"
grep -n '^\$ /tmp/vrf-c2/selfcheck.sh\|r "/tmp/vrf-c2/selfcheck.sh\|run "/tmp/vrf-c2/selfcheck.sh' $A | cut -d: -f1 | tr '\n' ' '; echo
echo "selfcheck lines naming correction-3-worker5: $(grep 'selfcheck.sh' $A | grep -c 'correction-3-worker5')"
echo "lines of A containing 335 lines: $(grep -n '335 lines' $A | cut -d: -f1 | tr '\n' ' ')"
echo "lines of A with a pasted wc -l naming correction-3-worker5: $(grep -n 'wc -l.*correction-3-worker5' $A | wc -l | tr -d ' ')"
echo "--- current line counts of the Files staged list (A:484-494)"
wc -l docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md MANIFEST.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md $B $C docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md $A
echo "--- A:17-18 worker counts: Result lines of worker4 and worker5 (masked)"
grep -n '^Result' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md | cut -c1-200 | mask
echo "--- A:23 helper scripts and A:496 tmp dirs"
ls -d /tmp/vrf-c2/selfcheck.sh /tmp/vrf-c2/lib.sh /tmp/c2mgr/pii.py /tmp/c3pre /tmp/c3w1 /tmp/c3w2 /tmp/c3w3 /tmp/c3w4 /tmp/c3w5 /tmp/c3mgr /tmp/c3mgr/assemble.py 2>&1
echo "--- A:23 lib.sh / pii.py named anywhere in a pasted command in A: $(grep -n '^\$ .*\(lib\.sh\|pii\.py\)' $A | wc -l | tr -d ' ')"
echo "--- C:161-163: worker6 lines 379 and 418 (masked, cut)"
sed -n '379p;418p' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -c1-140 | mask | sed "s/^/quoted| /"
echo "--- C:165-166 and B:19 cross-file pointers: same-file pastes of 19:37:30 in C, of E4 diff in B"
echo "C 19:37:30 lines=$(grep -c '19:37:30' $C) C date-r commands=$(grep -c '^\$ date' $C) B 17a18,30 lines=$(grep -c '17a18,30' $B)"
echo "--- E-section headings in A, in file order"
grep -n '^### E' $A
$ /tmp/c3b/w2/mech.sh 2>&1 | tee /tmp/c3b/w2/mech.out
2026-11-11T20:44:17
--- check 3: email regex and obfuscated forms (counts and line numbers only)
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=0 at=[] obfusc_lines=0 at=[]
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md email_lines=0 at=[] obfusc_lines=0 at=[]
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md email_lines=0 at=[] obfusc_lines=0 at=[]
positive controls: email=1 obfusc=1
--- checks 4 and 6: selfcheck
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[511] last_nonblank_line=511 last_nonblank_is_S13=YES lines=511
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[31] last_nonblank_line=31 last_nonblank_is_S13=YES lines=31
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[168] last_nonblank_line=168 last_nonblank_is_S13=YES lines=168
V1 positive control (hyphen-split synthetic line): HIT_lines=1
--- check 7: forbidden strings, whole files
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md word_ci=0 word_ci_w=0 F1_fixed=0 F2_fixed=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md word_ci=0 word_ci_w=0 F1_fixed=0 F2_fixed=0
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md word_ci=0 word_ci_w=0 F1_fixed=0 F2_fixed=0
positive controls: F1=1 F2=1 word=1
line 500 of A: F1_fixed=0 F2_fixed=0 word_ci=0 COMMIT_hyphen_paren=1
--- check 2: dollar-prompt lines inside code blocks, with ellipsis, angle placeholder, or a shell variable
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:287 ellipsis=0 angle=1 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:392 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:395 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:397 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:399 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:401 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:96 ellipsis=0 angle=0 var=1
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:101 ellipsis=0 angle=0 var=1
--- check 2: does the block holding A:287 define N
0
--- pasted script sources vs current files in /tmp/c3mgr
v1.sh A:44-69 identical
v2.sh A:141-152 identical
scan.sh A:218-245 identical
e6.sh A:314-351 identical
--- A:39 says output passes through mask: mask/perl mentions per script
v1.sh mask_or_perl_subst_lines=3
v2.sh mask_or_perl_subst_lines=0
scan.sh mask_or_perl_subst_lines=0
e6.sh mask_or_perl_subst_lines=1
--- A:11 and A:470 S13 coverage: selfcheck commands in A naming the worker5 report
66 124 151 185 339 342 406 426 500 
selfcheck lines naming correction-3-worker5: 0
lines of A containing 335 lines: 493 
lines of A with a pasted wc -l naming correction-3-worker5: 0
--- current line counts of the Files staged list (A:484-494)
     590 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md
     487 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
     179 docs/reports/2026-11-11-v-rulings-filing-worker2.md
     241 docs/reports/2026-11-11-v-rulings-filing-worker5.md
     420 MANIFEST.md
     678 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
      31 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
     168 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
     749 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
     335 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
     511 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
    4389 total
--- A:17-18 worker counts: Result lines of worker4 and worker5 (masked)
--- A:23 helper scripts and A:496 tmp dirs
/tmp/c2mgr/pii.py
/tmp/c3mgr
/tmp/c3mgr/assemble.py
/tmp/c3pre
/tmp/c3w1
/tmp/c3w2
/tmp/c3w3
/tmp/c3w4
/tmp/c3w5
/tmp/vrf-c2/lib.sh
/tmp/vrf-c2/selfcheck.sh
--- A:23 lib.sh / pii.py named anywhere in a pasted command in A: 0
--- C:161-163: worker6 lines 379 and 418 (masked, cut)
quoted| $ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
quoted| 37
--- C:165-166 and B:19 cross-file pointers: same-file pastes of 19:37:30 in C, of E4 diff in B
C 19:37:30 lines=1 C date-r commands=1 B 17a18,30 lines=0
--- E-section headings in A, in file order
41:### E1. Append-only, edit scope, self-checks (my re-run of worker1's claims)
206:### E2. Full email scan and rep-name scan (steps 5 and 6)
292:### E3. MANIFEST rows
311:### E5. Fixes for worker4's findings, and the final checks of the other reports
448:### E4. Worker2 report: manager note, and the leads in its evidence file
```

### follow.sh
```
$ cat /tmp/c3b/w2/follow.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
C=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
W6=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
echo "--- worker4 and worker5 result lines"
grep -nE 'Result: ' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md | cut -c1-200 | mask
echo "--- C dollar-date lines and C:96, C:101"
grep -n '^\$ date' $C | cut -c1-160 | mask
sed -n '96p;101p' $C | cut -c1-200 | mask | sed "s/^/quoted| /"
echo "--- worker6 lines 376-381 and 414-419"
sed -n '376,381p;414,419p' $W6 | cut -c1-160 | mask | sed "s/^/quoted| /"
echo "--- re-run of the worker6:379 command"
head -n 206 $W6 | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b' | wc -l
$ /tmp/c3b/w2/follow.sh 2>&1 | tee /tmp/c3b/w2/follow.out
--- worker4 and worker5 result lines
--- C dollar-date lines and C:96, C:101
25:$ date -u +%Y-%m-%dT%H:%M:%SZ
quoted| $ grep -ci -- "$N" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md docs/reports/2026-11-12-v-rulings-filing-correction
quoted| $ W=$(printf "v%sdict|COMMIT-%s|COMMIT-%s" er INDEX DIFF-SHA256); grep -ciE "$W" docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-
--- worker6 lines 376-381 and 414-419
quoted|      5	export N S13
quoted|      6	run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
quoted|      7	while IFS= read -r c <&3; do run "$c" </dev/null; done 3< "$1" | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/\Q$ENV{S13}\E/<S13>/g'
quoted| $ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
quoted| 40:$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
quoted| 42:$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
quoted| 171:$ grep -noE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5
quoted| 174:$ grep -nE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5 | cut -c1-70
quoted| 176:$ sed -n 284,313p $A | grep -n "manager.md" | cut -c1-90
quoted| $ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
quoted| 37
quoted| $ for v in PA PB A B T P W5 D3 C R; do printf '%s: ' "$v"; head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?'
--- re-run of the worker6:379 command
      37
```

### follow2.sh
```
$ cat /tmp/c3b/w2/follow2.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
for f in docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md; do
  echo "--- $f lines containing FAIL or PASS with MAJOR/MINOR"
  grep -nE '(FAIL|PASS).*(MAJOR|MINOR)|^## Result' "$f" | cut -c1-160 | mask
done
echo "--- A lines quoting a worker4 or worker5 Result line inside a code block"
awk '/^```/{inb=!inb; next} inb && /(MAJOR|MINOR)/{print NR}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | tr '\n' ' '; echo
$ /tmp/c3b/w2/follow2.sh 2>&1 | tee /tmp/c3b/w2/follow2.out
--- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md lines containing FAIL or PASS with MAJOR/MINOR
745:## Result
747:FAIL. 1 MAJOR, 6 MINOR.
--- docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md lines containing FAIL or PASS with MAJOR/MINOR
157:747:FAIL. 1 MAJOR, 6 MINOR.
295:   - :17 gives worker4's tally "1 MAJOR and 6 MINOR". run2 shows worker4:747 `FAIL. 1 MAJOR, 6 MINOR.`
304:## Result
305:FAIL. 0 MAJOR, 9 MINOR. Items 4 and 5 hold, and the E2, E5 and self-check re-runs reproduce (run1).
--- A lines quoting a worker4 or worker5 Result line inside a code block
460 
```

### verify.sh
```
$ cat /tmp/c3b/w2/verify.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
A=docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
echo "--- A:498-505: re-run the A:500 command and compare with A:501-505"
diff <(bash -c "$(sed -n 500p $A | sed 's/^\$ //')" 2>&1) <(sed -n '501,505p' $A) && echo A500-output-matches-pasted
echo "--- A:17 and A:469-471: which worker4 findings have a section in e6.sh"
grep -n '^echo "--- finding' /tmp/c3mgr/e6.sh
echo "--- A:287 as pasted, in a shell where N is not set, on a synthetic line"
unset N; printf 'abc\n' | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
echo "--- A:15 leads: code-block lines in A containing the quoted lead texts"
awk '/^```/{inb=!inb; next} inb' $A | grep -c 'no pre-edit copy exists\|Nothing under vm/ or .claude/ was written'
$ /tmp/c3b/w2/verify.sh 2>&1 | tee /tmp/c3b/w2/verify.out
--- A:498-505: re-run the A:500 command and compare with A:501-505
A500-output-matches-pasted
--- A:17 and A:469-471: which worker4 findings have a section in e6.sh
6:echo "--- finding 1: scan script source"
9:echo "--- finding 5: worker6 report"
12:echo "--- finding 6: worker3 report"
15:echo "--- finding 7: worker2 report"
--- A:287 as pasted, in a shell where N is not set, on a synthetic line
<NAME>a<NAME>b<NAME>c<NAME>
<NAME>--- A:15 leads: code-block lines in A containing the quoted lead texts
0
```


## Findings

### Checks with no finding
- Check 3, email: 0 email-regex lines and 0 obfuscated-form lines in A, B and C; both positive controls fire (mech.out, "check 3").
- Check 4, rep name: name_ci=0 and V1_HIT_lines=0 in all three; V1 positive control HIT_lines=1 (mech.out, "checks 4 and 6").
- Check 6, S13: S13_containing=1, S13_standalone=1, last_nonblank_is_S13=YES in all three (A at 511, B at 31, C at 168) (mech.out).
- Check 7, forbidden strings: 0 for the word (case-insensitive, with and without -w) and 0 for each of the two strings (fixed-string grep with the strings built at runtime) in all three whole files; all three positive controls are 1 (mech.out, "check 7").
- A:500. Neither forbidden string is on the line as a literal (F1_fixed=0, F2_fixed=0, word_ci=0). It holds the alternation pattern instead (COMMIT_hyphen_paren=1). The line contains no forbidden literal, so it can be quoted as it stands: `$ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -ciw 'v[e]rdict' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md; grep -cE 'COMMIT-(INDEX|DIFF-SHA256)' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md` (line 500 in full). Its self-check block is current: re-running the A:500 command gives exactly A:501-505 (verify.out, "A500-output-matches-pasted").
- The four script sources pasted in A (v1.sh, v2.sh, scan.sh, e6.sh) are byte-identical to the files now in /tmp/c3mgr (mech.out, "identical" x4).

### MAJOR
1. A:287 (check 2: a shell variable not defined in its block). The pasted command is `$ sed -n '114p;132p' docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'`. `N` is not set anywhere in the block A:286-290 (mech.out: "does the block holding A:287 define N" gives 0). A:39 says `N` is built at runtime, but that applies to the scripts, not to this standalone command. If you run it as written in a shell where `N` is unset, the first substitution has an empty pattern and puts `<NAME>` between every character (verify.out, synthetic line: `<NAME>a<NAME>b<NAME>c<NAME>`). INFERRED, not run on the real file because the run would print the address: the email substitution would then fail to match, and the output would not be what is pasted at A:288-289. This is a non-literal command presented as run.

### MINOR
1. A:39, "Output passes through `mask`, which replaces the rep's name with `<NAME>` and any email address with `(address withheld)`." This is stated for all of the verification evidence, but v2.sh and scan.sh contain no mask (mech.out: mask_or_perl_subst_lines=0 for both). The E1 second block (A:195-204), E3 and E4 are bare commands with no mask either. Their counts show nothing leaked; the guarantee is still claimed for output that never went through the mask (S2).
2. A:11, "the S13 sentence once, standalone, last line, in each new report", and A:470, which lists the coverage as worker1-worker4 plus the four edited reports. The worker5 report is a new report of this unit (A:493), but no selfcheck command in A names it (mech.out: "selfcheck lines naming correction-3-worker5: 0"). The claim has no paste for that file (S1). Its present state is in my self-check section below.
3. A:480, "the Files staged list below, built by `wc -l` on each path", and A:493, "335 lines". No `wc -l` of that list is pasted in A. "335 lines" appears only at A:493, and no pasted `wc -l` names the worker5 report (mech.out). The figure is right now (mech.out wc: 335) but has no paste (S1).
4. A:17, "FAIL, 1 MAJOR and 6 MINOR", A:18, "FAIL, 0 MAJOR and 9 MINOR", and the same tallies at A:467 and A:477. A pastes neither report's result line; the only code-block line in A containing MAJOR or MINOR is A:460, a heading from final.out (follow2.out). The tallies match worker4:747 and worker5:305 (follow2.out) but are not pasted in A (S1).
5. A:17, "all seven fixed". worker5 then failed the post-worker4 changes with 9 MINOR (A:18). A:477 lists what it hit, which includes the fixes for worker4 findings 3, 4, 6 and 7 ("this report's lines on S13 coverage", "the MANIFEST step", "the worker3 note", "the worker2 note"). The re-fixes "have NOT been re-checked by an adversarial worker" (A:477). Also, e6.sh has diff sections only for findings 1, 5, 6 and 7 (verify.out). The unqualified "all seven fixed" in the dispatch list is graded above that evidence (S2).
6. A:23, "Checked that the original helper scripts still exist (/tmp/vrf-c2/selfcheck.sh, /tmp/vrf-c2/lib.sh, /tmp/c2mgr/pii.py)", and A:496, the list of /tmp/c3w1 to /tmp/c3w5. No pasted command in A names lib.sh or pii.py (mech.out: 0), and no listing of the /tmp directories is pasted. All of them exist now (mech.out `ls -d`), but A has no paste for them (S1).
7. A:15, "Its evidence file /tmp/c3w2/final.out held leads", naming among them "an unpasted 'no pre-edit copy exists'" and "an unpasted 'Nothing under vm/ or .claude/ was written.'". E4 (A:449-464) pastes only final.out's section headings and a count of its `$ ` lines. No code-block line in A contains either quoted lead (verify.out: 0) (S1).
8. A:34, "Before: a disposition note giving the MFFU public support address itself". A pastes the line masked (A:98) and an email count of 1 (A:108). Nothing in A shows that the masked address is MFFU's support address. Compare A:35, where the no-reply address is checked for local part and domain (A:438). This identification is unsupported (S1).
9. A:24, "It copied the four target files to /tmp/c3pre/ before editing, ran the re-checks on the live files before insertion". The order of worker1's steps has no paste in A. The REPORTED label at A:21 covers "dispatches and hand-backs", not a worker's internal order of steps (S1).
10. B:19, "(the diff against the pre-note copy is in the manager report, E4: one insertion, 0 deleted lines)" and "the sizes and times, taken just before this note was added". B pastes neither: 0 lines of B contain the diff result (mech.out: "B 17a18,30 lines=0"). The diff is at A:450-453, in another file, and the "just before" timing has no paste anywhere. Under the same-file rule both are unsupported in B (S1).
11. C:161-163 with C:165. The pasted `sed -n '379p;418p'` joins two lines. Worker6:379 is a `grep -nE` command, which prints matching lines, not a count. Worker6:418, the bare `37`, is the output of worker6:417, a different `grep -cE` command (follow.out shows lines 376-381 and 414-419). C:165 cites "the worker6 report's lines 379 and 418, last command above" for the 37, so the paste presents 37 as the output of a command that cannot produce it. The figure itself is right (follow.out re-run: 37) (S1).
12. C:166, "that is 2026-11-11T19:37:30 local (pasted in the manager report, E5)" and "the directory worker1 filled with pre-edit copies as its first step". C does not paste the conversion. C's only `$ date` line is C:25, a `date -u` call (follow.out), and "19:37:30" occurs once in C (mech.out: "C 19:37:30 lines=1"), in this prose line. "As its first step" has no paste in C (S1).

### Observations, not graded (outside scope or cosmetic)
- In A, E4 (A:448) comes after E5 (A:311) (mech.out, E-section headings).
- C:96 is a `$ ` command that uses `$N`, outside the C lines in scope (mech.out check 2; follow.out shows the line). I did not judge whether its block defines `N`.

## Result
Result: FAIL - 1 MAJOR, 12 MINOR.

## Self-check of this report
Run on the final file and re-run after pasting (the selfcheck line for the worker5 report is the present-state evidence for MINOR 2):
```
$ cat /tmp/c3b/w2/self.sh
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
R=docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md
EM='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
OB='[A-Za-z0-9._-]+ *(\[at\]|\(at\)|\{at\}| at ) *[A-Za-z0-9-]+ *(\.|\[dot\]|\(dot\)| dot ) *[A-Za-z]{2,}'
F1=$(printf '%s-%s' COMMIT INDEX); F2=$(printf '%s-%s-%s' COMMIT DIFF SHA256)
/tmp/vrf-c2/selfcheck.sh $R docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md
echo "$R email_lines=$(grep -cE "$EM" $R) obfusc_lines=$(grep -ciE "$OB" $R) word_ci=$(grep -ci 'v[e]rdict' $R) F1_fixed=$(grep -cF -- "$F1" $R) F2_fixed=$(grep -cF -- "$F2" $R)"
$ /tmp/c3b/w2/self.sh 2>&1 | tee /tmp/c3b/w2/self.out
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[306] last_nonblank_line=306 last_nonblank_is_S13=YES lines=306
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[335] last_nonblank_line=335 last_nonblank_is_S13=YES lines=335
V1 positive control (hyphen-split synthetic line): HIT_lines=1
docs/reports/2026-11-12-v-rulings-filing-correction-3b-worker2.md email_lines=0 obfusc_lines=0 word_ci=0 F1_fixed=0 F2_fixed=0
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
