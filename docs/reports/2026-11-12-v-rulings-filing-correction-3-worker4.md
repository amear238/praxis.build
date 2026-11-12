# 2026-11-12 v-rulings filing correction 3 - worker4 (ADVERSARIAL)

## Task

Adversarial re-check of unit 2026-11-12-v-rulings-filing-correction-3 (bead Praxis_build-n1y), mode ADVERSARIAL, read-only apart from this report. Scope: the inserted Correction 3 sections of the correction-2 manager and worker6 reports, the two one-line address masks in the 2026-11-11 worker2 and worker5 reports, MANIFEST rows 415-419, and the four correction-3 reports (worker1, worker2, worker3, manager). Every output below is embedded mechanically from the file the script wrote (by /tmp/c3w4/assemble.py), not typed. All output is masked for the rep name (`<NAME>`) and for email addresses (`(address withheld)`).

## Criteria

- S1: every claim in a report has pasted command output, not a description of output.
- S2: no component is reported at a higher level than the evidence supports.
- S13: the S13 sentence once, standalone, last line.
- Address rule (Amear, 2026-11-12): MFFU's public support address may appear only where quoted from an email header or MFFU text; no other email addresses; rep names stay de-identified.
- Checks (a) to (h) of the brief.

## Commands and output

### checks.out

Command: `bash /tmp/c3w4/checks.sh > /tmp/c3w4/checks.out 2>&1`

Script text (`cat /tmp/c3w4/checks.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
S="Fills are optimistic; ""Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
B1="COMMIT-""INDEX"; B2="COMMIT-""DIFF-SHA256"; BW="ver""dict"
export N S
R=docs/reports
F="$R/2026-11-11-v-rulings-filing-correction-2-manager.md $R/2026-11-11-v-rulings-filing-correction-2-worker6.md $R/2026-11-11-v-rulings-filing-worker2.md $R/2026-11-11-v-rulings-filing-worker5.md $R/2026-11-12-v-rulings-filing-correction-3-worker1.md $R/2026-11-12-v-rulings-filing-correction-3-worker2.md $R/2026-11-12-v-rulings-filing-correction-3-worker3.md $R/2026-11-12-v-rulings-filing-correction-3-manager.md MANIFEST.md"
mask() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
echo "== C1 per-file counts"
for f in $F; do
  c=$(grep -ci -- "$N" "$f")
  v1=$(perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }' "$f")
  em=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f")
  ob=$(grep -ciE '[A-Za-z0-9]+ *[\[\(]? *at *[\]\)]? *[A-Za-z0-9-]+ *[\[\(]? *dot *[\]\)]? *(com|net|org|io)\b' "$f")
  bw=$(grep -ci -- "$BW" "$f"); b1=$(grep -c -- "$B1" "$f"); b2=$(grep -c -- "$B2" "$f")
  sub=$(grep -cF -- "$S" "$f"); sa=$(grep -cxF -- "$S" "$f"); sal=$(grep -nxF -- "$S" "$f" | cut -d: -f1 | tr '\n' ' ')
  lastl=$(awk 'NF{l=$0} END{print l}' "$f"); [ "$lastl" = "$S" ] && il=YES || il=NO
  echo "$f: name_ci=$c V1=$v1 email_lines=$em obf_lines=$ob banned_word=$bw B1=$b1 B2=$b2 S13_containing=$sub S13_standalone=$sa at=[${sal% }] last_is_S13=$il lines=$(wc -l < "$f" | tr -d ' ')"
done
ctl=$(printf '%s\n' "x $(echo "$N" | sed 's/./&-/g; s/-$//') y" | perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }')
echo "V1 positive control: HIT_lines=$ctl"
echo "== C2 email-bearing lines (masked)"
for f in $F; do grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f" | sed "s|^|$f:|" | mask | cut -c1-300; done
echo "== C2b distinct addresses, domain part only"
for f in $F; do grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f" | sed 's/.*@/@/' | sort | uniq -c | sed "s|^|$f:|"; done
echo "== C2c obfuscated forms (masked)"
for f in $F; do grep -niE '[A-Za-z0-9]+ *[\[\(]? *at *[\]\)]? *[A-Za-z0-9-]+ *[\[\(]? *dot *[\]\)]? *(com|net|org|io)\b' "$f" | sed "s|^|$f:|" | mask | cut -c1-300; done
echo "== F1 diffs vs /tmp/c3pre"
for b in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md 2026-11-11-v-rulings-filing-worker2.md 2026-11-11-v-rulings-filing-worker5.md; do
  echo "-- $b: pre_lines=$(wc -l < /tmp/c3pre/$b | tr -d ' ') now_lines=$(wc -l < $R/$b | tr -d ' ')"
  diff /tmp/c3pre/$b $R/$b | grep -E '^[0-9]' 
done
echo "-- worker2/worker5 changed lines (masked)"
for b in 2026-11-11-v-rulings-filing-worker2.md 2026-11-11-v-rulings-filing-worker5.md; do diff /tmp/c3pre/$b $R/$b | mask | cut -c1-400; done
echo "-- worker2/worker5: diff after removing addresses from both sides"
for b in 2026-11-11-v-rulings-filing-worker2.md 2026-11-11-v-rulings-filing-worker5.md; do
  diff <(perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/ADDR/g; s/\(address withheld\)/ADDR/g' /tmp/c3pre/$b) <(perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/ADDR/g; s/\(address withheld\)/ADDR/g' $R/$b); echo "$b normalized_diff_rc=$?"
done
echo "-- manager/worker6: pre minus last line == now head, pre last line == now last line"
for b in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md; do
  p=/tmp/c3pre/$b; n=$R/$b; pl=$(wc -l < $p | tr -d ' ')
  cmp <(head -n $((pl-1)) $p) <(head -n $((pl-1)) $n) && echo "$b head_$((pl-1))_identical"
  cmp <(tail -n 1 $p) <(tail -n 1 $n) && echo "$b last_line_identical"
  echo "$b pre_trailing_newline=$(tail -c1 $p | xxd -p) now_trailing_newline=$(tail -c1 $n | xxd -p)"
done
echo "== F2 diffs vs /tmp/c3w3/pre"
for b in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md 2026-11-12-v-rulings-filing-correction-3-worker1.md; do
  echo "-- $b: w3pre_lines=$(wc -l < /tmp/c3w3/pre/$b | tr -d ' ') now=$(wc -l < $R/$b | tr -d ' ')"; diff /tmp/c3w3/pre/$b $R/$b | grep -E '^[0-9]'
done
echo "== F3 c3pre -> c3w3/pre (worker1 stage)"
for b in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md; do echo "-- $b"; diff /tmp/c3pre/$b /tmp/c3w3/pre/$b | grep -E '^[0-9]'; done
echo "== F4 worker2 c3 vs w2.pre"
diff /tmp/c3mgr/w2.pre.md $R/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -E '^[0-9]'
echo "== F5 MANIFEST vs pre"
echo "pre_lines=$(wc -l < /tmp/c3mgr/MANIFEST.pre.md | tr -d ' ') now=$(wc -l < MANIFEST.md | tr -d ' ')"
diff /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -E '^[0-9]'
pl=$(wc -l < /tmp/c3mgr/MANIFEST.pre.md | tr -d ' '); cmp <(head -n $pl /tmp/c3mgr/MANIFEST.pre.md) <(head -n $pl MANIFEST.md) && echo "MANIFEST head_${pl}_identical"
echo "== H1 MANIFEST rows 410-419 field count and path existence"
for i in $(seq 410 419); do l=$(sed -n ${i}p MANIFEST.md); nf=$(echo "$l" | awk -F'|' '{print NF}'); p=$(echo "$l" | awk -F'|' '{gsub(/ /,"",$2); print $2}'); [ -e ".$p" ] && ex=EXISTS || ex=MISSING; t=$(echo "$l" | awk -F'|' '{print $3"|"$4"|"$5}'); echo "row $i fields=$nf path_$ex type_tier_date=[$t]"; done
```

Output:
```
== C1 per-file counts
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[590] last_is_S13=YES lines=590
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[487] last_is_S13=YES lines=487
docs/reports/2026-11-11-v-rulings-filing-worker2.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=3 S13_standalone=1 at=[179] last_is_S13=YES lines=179
docs/reports/2026-11-11-v-rulings-filing-worker5.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[241] last_is_S13=YES lines=241
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[678] last_is_S13=YES lines=678
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[31] last_is_S13=YES lines=31
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md: name_ci=0 V1=0 email_lines=0 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[146] last_is_S13=YES lines=146
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: name_ci=0 V1=0 email_lines=1 obf_lines=0 banned_word=0 B1=0 B2=0 S13_containing=1 S13_standalone=1 at=[352] last_is_S13=YES lines=352
MANIFEST.md: name_ci=2 V1=2 email_lines=0 obf_lines=0 banned_word=9 B1=2 B2=2 S13_containing=0 S13_standalone=0 at=[] last_is_S13=NO lines=419
V1 positive control: HIT_lines=1
== C2 email-bearing lines (masked)
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:240:echo "positive controls: name_split_on_hyphenated_synthetic=$ctl email_on_synthetic=$(printf '(address withheld)\n' | grep -cE "$EM")"
== C2b distinct addresses, domain part only
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:   1 @c-d.example
== C2c obfuscated forms (masked)
== F1 diffs vs /tmp/c3pre
-- 2026-11-11-v-rulings-filing-correction-2-manager.md: pre_lines=206 now_lines=590
204a205,444
205a446,589
-- 2026-11-11-v-rulings-filing-correction-2-worker6.md: pre_lines=207 now_lines=487
205a206,361
206a363,486
-- 2026-11-11-v-rulings-filing-worker2.md: pre_lines=179 now_lines=179
169c169
-- 2026-11-11-v-rulings-filing-worker5.md: pre_lines=241 now_lines=241
79c79
-- worker2/worker5 changed lines (masked)
169c169
< 3. `(address withheld)` (A:114, 132). This is a public company address. Kept.
---
> 3. `MFFU's public support address` (A:114, 132). This is a public company address. Kept.
79c79
< Co-Authored-By: Claude Opus 5.5 ((address withheld))
---
> Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
-- worker2/worker5: diff after removing addresses from both sides
169c169
< 3. `ADDR` (A:114, 132). This is a public company address. Kept.
---
> 3. `MFFU's public support address` (A:114, 132). This is a public company address. Kept.
2026-11-11-v-rulings-filing-worker2.md normalized_diff_rc=1
79c79
< Co-Authored-By: Claude Opus 5.5 (ADDR)
---
> Co-Authored-By: Claude Opus 5.5 (noreply address withheld)
2026-11-11-v-rulings-filing-worker5.md normalized_diff_rc=1
-- manager/worker6: pre minus last line == now head, pre last line == now last line
2026-11-11-v-rulings-filing-correction-2-manager.md head_205_identical
2026-11-11-v-rulings-filing-correction-2-manager.md last_line_identical
2026-11-11-v-rulings-filing-correction-2-manager.md pre_trailing_newline=0a now_trailing_newline=0a
2026-11-11-v-rulings-filing-correction-2-worker6.md head_206_identical
2026-11-11-v-rulings-filing-correction-2-worker6.md last_line_identical
2026-11-11-v-rulings-filing-correction-2-worker6.md pre_trailing_newline=0a now_trailing_newline=0a
== F2 diffs vs /tmp/c3w3/pre
-- 2026-11-11-v-rulings-filing-correction-2-manager.md: w3pre_lines=464 now=590
462a463,564
463a566,589
-- 2026-11-11-v-rulings-filing-correction-2-worker6.md: w3pre_lines=366 now=487
365a366,486
-- 2026-11-12-v-rulings-filing-correction-3-worker1.md: w3pre_lines=641 now=678
640a641,677
== F3 c3pre -> c3w3/pre (worker1 stage)
-- 2026-11-11-v-rulings-filing-correction-2-manager.md
204a205,368
205a370,463
-- 2026-11-11-v-rulings-filing-correction-2-worker6.md
206a207,365
== F4 worker2 c3 vs w2.pre
17a18,30
== F5 MANIFEST vs pre
pre_lines=414 now=419
414a415,419
MANIFEST head_414_identical
== H1 MANIFEST rows 410-419 field count and path existence
row 410 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-11 ]
row 411 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-11 ]
row 412 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-11 ]
row 413 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-11 ]
row 414 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-11 ]
row 415 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-12 ]
row 416 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-12 ]
row 417 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-12 ]
row 418 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-12 ]
row 419 fields=7 path_EXISTS type_tier_date=[ Report | 3 | 2026-11-12 ]
```

### scanA.out

Command: `bash /tmp/c3w4/scanA.sh > /tmp/c3w4/scanA.out 2>&1`

Script text (`cat /tmp/c3w4/scanA.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
export N
R=docs/reports
mask() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
BW="ver""dict"
echo "== MANIFEST name/banned lines (line numbers only)"
grep -ni -- "$N" MANIFEST.md | cut -d: -f1 | tr '\n' ' '; echo
grep -ni -- "$BW" MANIFEST.md | cut -d: -f1 | tr '\n' ' '; echo
grep -n -- "COMMIT-""INDEX\|COMMIT-""DIFF-SHA256" MANIFEST.md | cut -d: -f1 | tr '\n' ' '; echo
echo "== pre line 205/206 of c2 manager, 206/207 of worker6 (lengths)"
for b in 2026-11-11-v-rulings-filing-correction-2-manager.md 2026-11-11-v-rulings-filing-correction-2-worker6.md; do awk -v f=$b '{print f": pre line "NR" len="length($0)}' /tmp/c3pre/$b | tail -n 2; done
echo "== A: dollar-prompt lines with ... or <placeholder> (file ranges)"
scan() { f=$1; a=$2; b=$3; awk -v a=$a -v b=$b -v f=$f 'NR>=a && NR<=b && /^\s*\$ / && (/\.\.\./ || /<[A-Za-z_][^>]*>/) {print f":"NR": "$0}' $f | mask | cut -c1-260; }
scan $R/2026-11-11-v-rulings-filing-correction-2-manager.md 206 589
scan $R/2026-11-11-v-rulings-filing-correction-2-worker6.md 207 486
for f in $R/2026-11-12-v-rulings-filing-correction-3-worker1.md $R/2026-11-12-v-rulings-filing-correction-3-worker2.md $R/2026-11-12-v-rulings-filing-correction-3-worker3.md $R/2026-11-12-v-rulings-filing-correction-3-manager.md; do scan $f 1 99999; done
echo "== A2: variables used on dollar-prompt lines and whether a literal definition exists in the same file"
chk() { f=$1; a=$2; b=$3
  awk -v a=$a -v b=$b 'NR>=a && NR<=b && /^\s*\$ /' $f | grep -oE '\$\{?[A-Za-z_][A-Za-z0-9_]*' | sed 's/[${]//g' | sort -u | while read v; do
    case $v in HOME|PWD|PATH|ENV|_|i|f|l|n|b|x|y|c|p|s|t|k|v|line|file) ;; esac
    d=$(grep -cE "(^|[^A-Za-z0-9_])$v=|for $v in|read( -r)? ([A-Za-z_ ]* )?$v\b|local $v|export $v=|\b$v\(\)|function $v\b|\(\\\$$v\)" $f)
    [ "$d" = 0 ] && echo "$f: var $v NO_DEF"
  done
  awk -v a=$a -v b=$b 'NR>=a && NR<=b && /^\s*\$ /{print $2}' $f | sort | uniq -c | sort -rn | head -15 | sed "s|^|$f first-word: |"
}
chk $R/2026-11-11-v-rulings-filing-correction-2-manager.md 206 589
chk $R/2026-11-11-v-rulings-filing-correction-2-worker6.md 207 486
for f in $R/2026-11-12-v-rulings-filing-correction-3-worker1.md $R/2026-11-12-v-rulings-filing-correction-3-worker2.md $R/2026-11-12-v-rulings-filing-correction-3-worker3.md $R/2026-11-12-v-rulings-filing-correction-3-manager.md; do chk $f 1 99999; done
echo "== A3: dollar-prompt line counts per file"
for f in $R/2026-11-11-v-rulings-filing-correction-2-manager.md $R/2026-11-11-v-rulings-filing-correction-2-worker6.md $R/2026-11-12-v-rulings-filing-correction-3-*.md; do echo "$f $(grep -cE '^\s*\$ ' $f)"; done
```

Output:
```
== MANIFEST name/banned lines (line numbers only)
335 336 
99 102 118 120 130 131 206 209 374 
206 209 
== pre line 205/206 of c2 manager, 206/207 of worker6 (lengths)
2026-11-11-v-rulings-filing-correction-2-manager.md: pre line 205 len=0
2026-11-11-v-rulings-filing-correction-2-manager.md: pre line 206 len=90
2026-11-11-v-rulings-filing-correction-2-worker6.md: pre line 206 len=0
2026-11-11-v-rulings-filing-correction-2-worker6.md: pre line 207 len=90
== A: dollar-prompt lines with ... or <placeholder> (file ranges)
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:269: $ cat /tmp/vrf-c2/selfcheck.sh | S13="$S13" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:290: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:300: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:302: $ diff <(sed -n 137,145p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/re
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:376: $ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <worker2, worker5, worker6 reports>
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md:453: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:236: $ for f in 2026-11-11-v-rulings-filing-correction-1-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker3.md; do echo "=== $f"; wc -
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:264: $ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:289: $ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:341: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:344: $ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:349: $ grep -nE '\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:352: $ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | perl -pe 's/[A-Za-z
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:65: $ cat /tmp/vrf-c2/selfcheck.sh | S13="$S13" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:86: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:96: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md docs/reports/2026-11-11-v-rulings-
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:98: $ diff <(sed -n 137,145p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(/tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md docs/rep
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:166: $ grep -cE "[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem" <worker2, worker5, worker6 reports>
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:231: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:241: $ for f in 2026-11-11-v-rulings-filing-correction-1-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker1.md 2026-11-11-v-rulings-filing-correction-2-worker3.md; do echo "=== $f"; wc -
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:269: $ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker3.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:294: $ diff /tmp/c2mgr/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | S13="$S13
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:336: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:339: $ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:344: $ grep -nE '\b([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:347: $ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi' | perl -pe 's/[A-Za-z
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:542: $ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:547: $ diff /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:579: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker5.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:590: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | N="$N" perl -pe 's/\Q$ENV{N}\E/
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md:629: $ /tmp/vrf-c2/selfcheck.sh docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:279: $ sed -n '114p;132p' docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address w
== A2: variables used on dollar-prompt lines and whether a literal definition exists in the same file
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: var ENV NO_DEF
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: var PIPESTATUS NO_DEF
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md: var T NO_DEF
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:   19 grep
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:   11 date
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:   10 sed
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    8 find
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    5 /tmp/vrf-c2/selfcheck.sh
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    4 diff
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    3 stat
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    3 python3
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    3 head
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    3 cat
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    2 wc
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    2 readlink
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    2 ls
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    2 for
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md first-word:    2 P=docs/reports/2026-11-11-v-rulings-filing-;
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: var ENV NO_DEF
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: var PIPESTATUS NO_DEF
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:   16 grep
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    7 diff
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    6 sed
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    5 date
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    2 wc
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    2 stat
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    2 head
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    2 for
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    1 python3
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    1 cat
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md first-word:    1 /tmp/vrf-c2/selfcheck.sh
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md: var ENV NO_DEF
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:   26 grep
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:   21 diff
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:   21 date
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:   15 sed
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    8 cmp
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    8 /tmp/vrf-c2/selfcheck.sh
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    7 wc
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    6 python3
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    5 stat
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    5 cat
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    4 find
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    3 git
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    3 for
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    2 ls
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md first-word:    1 shasum
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md first-word:    1 wc
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md first-word:    1 stat
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    9 diff
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    4 wc
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    3 sed
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    3 grep
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    3 cmp
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    2 stat
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    2 git
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    1 date
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    1 cat
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    1 W=$(printf
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md first-word:    1 /tmp/vrf-c2/selfcheck.sh
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: var ENV NO_DEF
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:   14 diff
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:   10 git
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    7 grep
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    6 wc
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    4 cmp
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    3 tail
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    3 cat
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    3 /tmp/vrf-c2/selfcheck.sh
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    1 sed
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    1 MROWS=5
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    1 /tmp/c3mgr/v2.sh
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md first-word:    1 /tmp/c3mgr/v1.sh
== A3: dollar-prompt line counts per file
docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md 108
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md 92
docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md 54
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md 138
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md 2
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 30
docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md 0
```

### rerun.out

Command: `bash /tmp/c3w4/rerun.sh > /tmp/c3w4/rerun.out 2>&1`

Script text (`cat /tmp/c3w4/rerun.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
export -f mask
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
date -u "+%Y-%m-%dT%H:%M:%SZ"
echo "#### E2 commands of the correction-3 manager report"
r "git cat-file -t 83891f6; git cat-file -t d056e91; git log --oneline -1 83891f6 | cut -c1-60"
r "git diff --name-only d056e91 83891f6 | wc -l"
r "git diff --name-only d056e91 83891f6 | grep -c '^docs/reports/evidence/'"
r "git diff --name-only d056e91 83891f6 | grep -cxE 'MANIFEST\.md|DECISIONS\.md'"
r "git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | wc -l"
r "cmp <(sed -n 215,240p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | mask) <(cat /tmp/c3mgr/scan.sh | mask) && echo scan.sh-matches-pasted-source"
r "cp /tmp/c3mgr/scanset.txt /tmp/c3w4/scanset.before.txt; MROWS=5 /tmp/c3mgr/scan.sh > /tmp/c3w4/scan.now.txt 2>&1; cp /tmp/c3w4/scanset.before.txt /tmp/c3mgr/scanset.txt; diff <(sed -n 242,275p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md) /tmp/c3w4/scan.now.txt; echo diff-rc=\$?"
r "sed -n '114p;132p' docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l"
r "git diff --stat HEAD -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l; git log --oneline -1 -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | cut -c1-8"
echo "#### synthetic address in the manager report (masked; length and TLD only)"
r "grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -d: -f1"
r "grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | awk '{n=split(\$0,a,\".\"); print \"len=\" length(\$0) \" tld=\" a[n]}'"
r "grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/scan.sh"
echo "#### E1 / E3 / E4"
r "git rev-parse --short HEAD"
r "git diff --cached --name-only | wc -l; git diff --cached --name-only | grep -vc '^docs/reports/evidence/'"
r "diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -v '^>'; diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -c '^<'"
r "tail -n 5 MANIFEST.md | cut -d'|' -f2"
r "grep -n '^--- E' /tmp/c3w2/final.out; grep -c '^\\\$ ' /tmp/c3w2/final.out"
r "diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'"
r "wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md"
r "wc -l docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md"
r "grep -n 'this report\.\$' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-120"
r "grep -ncE 'S13' /tmp/c3mgr/scan.sh"
echo "#### sample from the correction-2 manager Correction 3 section"
r "shasum -a 256 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md"
r "wc -l /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md"
r "grep -rnE \"(^|[^A-Za-z_])P=\" /tmp/vrf-c2 /tmp/c2fix /tmp/c2w5 /tmp/c2mgr /tmp/c2pre --include=\"*.sh\" --include=\"*.py\"; echo \"grep rc=\$?\""
r "sed -n 4p /tmp/vrf-c2/lib.sh"
r "cmp <(sed -n 319,330p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(cat /tmp/c2mgr/pii.py) && echo pii.py-matches-pasted"
r "sed -n 3,7p /tmp/c3w1/step1.sh | wc -l; sed -n 2,5p /tmp/c3w1/step1b.sh | wc -l; sed -n 2,3p /tmp/c3w1/step1c.sh | wc -l"
r "cmp <(sed -n 211,226p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(echo '\$ date -u +%Y-%m-%dT%H:%M:%SZ'; echo 2026-11-12T00:44:34Z; echo '\$ sed -n 3,7p /tmp/c3w1/step1.sh'; sed -n 3,7p /tmp/c3w1/step1.sh; echo '\$ sed -n 2,5p /tmp/c3w1/step1b.sh'; sed -n 2,5p /tmp/c3w1/step1b.sh; echo '\$ sed -n 2,3p /tmp/c3w1/step1c.sh'; sed -n 2,3p /tmp/c3w1/step1c.sh) && echo preamble-matches"
r "/tmp/vrf-c2/selfcheck.sh /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | sed 's#/tmp/c3pre/##'"
r "grep -cE '[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md"
r "grep -cE '[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem' /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md"
```

Output:
```
2026-11-12T01:22:31Z
#### E2 commands of the correction-3 manager report
$ git cat-file -t 83891f6; git cat-file -t d056e91; git log --oneline -1 83891f6 | cut -c1-60
commit
commit
83891f6 park(Praxis_build-n1y): audit FAIL after Amear resum
$ git diff --name-only d056e91 83891f6 | wc -l
      26
$ git diff --name-only d056e91 83891f6 | grep -c '^docs/reports/evidence/'
0
$ git diff --name-only d056e91 83891f6 | grep -cxE 'MANIFEST\.md|DECISIONS\.md'
2
$ git diff --name-only d056e91 83891f6 | grep -vxE 'MANIFEST\.md|DECISIONS\.md' | wc -l
      24
$ cmp <(sed -n 215,240p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | mask) <(cat /tmp/c3mgr/scan.sh | mask) && echo scan.sh-matches-pasted-source
scan.sh-matches-pasted-source
$ cp /tmp/c3mgr/scanset.txt /tmp/c3w4/scanset.before.txt; MROWS=5 /tmp/c3mgr/scan.sh > /tmp/c3w4/scan.now.txt 2>&1; cp /tmp/c3w4/scanset.before.txt /tmp/c3mgr/scanset.txt; diff <(sed -n 242,275p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md) /tmp/c3w4/scan.now.txt; echo diff-rc=$?
2c2
< files_in_set=28
---
> files_in_set=29
24c24
< docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=0 at=[] name_ci=0 name_split=0
---
> docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=1 at=[240] name_ci=0 name_split=0
27a28
> docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md email_lines=0 at=[] name_ci=0 name_split=0
31c32
< email_lines_total_files=2
---
> email_lines_total_files=3
diff-rc=1
$ sed -n '114p;132p' docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l
       2
$ git diff --stat HEAD -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l; git log --oneline -1 -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | cut -c1-8
       0
#### synthetic address in the manager report (masked; length and TLD only)
$ grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -d: -f1
240
$ grep -oE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | awk '{n=split($0,a,"."); print "len=" length($0) " tld=" a[n]}'
len=15 tld=example
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' /tmp/c3mgr/scan.sh
1
#### E1 / E3 / E4
$ git rev-parse --short HEAD
a962475
$ git diff --cached --name-only | wc -l; git diff --cached --name-only | grep -vc '^docs/reports/evidence/'
       1
0
$ diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -v '^>'; diff -d /tmp/c3mgr/MANIFEST.pre.md MANIFEST.md | grep -c '^<'
414a415,419
0
$ tail -n 5 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md 
 /docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md 
$ grep -n '^--- E' /tmp/c3w2/final.out; grep -c '^\$ ' /tmp/c3w2/final.out
3:--- E1 (f) byte checks against /tmp/c3pre
22:--- E2 (c) email regex and obfuscated forms, all six artifact files
37:--- E3 (d)(e) name, split-letter detector and S13, all six artifact files
51:--- E4 (a) command lines inside the two inserted sections
56:--- E5 (a) placeholder commands in the original bodies that Correction 3 does not re-run
82:--- E6 (b)(g) lines cited in the MINOR findings
150:--- E7 independent re-runs of the Correction 3 checks (pre-insertion copies where the section measured the pre-insertion file)
68
$ diff -d /tmp/c3mgr/w2.pre.md docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | grep -v '^>'
17a18,30
$ wc -lc /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md docs/reports/2026-11-11-v-rulings-filing-worker2.md /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md docs/reports/2026-11-11-v-rulings-filing-worker5.md
     179   11554 /tmp/c3pre/2026-11-11-v-rulings-filing-worker2.md
     179   11556 docs/reports/2026-11-11-v-rulings-filing-worker2.md
     241   19841 /tmp/c3pre/2026-11-11-v-rulings-filing-worker5.md
     241   19844 docs/reports/2026-11-11-v-rulings-filing-worker5.md
     840   62795 total
$ wc -l docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
     352 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md
$ grep -n 'this report\.$' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-120
337:- docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md: 33 lines; new; this report.
$ grep -ncE 'S13' /tmp/c3mgr/scan.sh
0
#### sample from the correction-2 manager Correction 3 section
$ shasum -a 256 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
24932bddc8402421df8a3304d9dd5b2875a0eec21f1d8d205735146ac2c12049  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
cc00cc5edd2035b26ad6e0c247de1ffbaf9d08dc2c8fe9be1d864feba6d222ed  /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ wc -l /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
     265 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
     507 total
$ grep -rnE "(^|[^A-Za-z_])P=" /tmp/vrf-c2 /tmp/c2fix /tmp/c2w5 /tmp/c2mgr /tmp/c2pre --include="*.sh" --include="*.py"; echo "grep rc=$?"
grep rc=1
$ sed -n 4p /tmp/vrf-c2/lib.sh
M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
$ cmp <(sed -n 319,330p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(cat /tmp/c2mgr/pii.py) && echo pii.py-matches-pasted
/dev/fd/63 /dev/fd/62 differ: char 1, line 1
$ sed -n 3,7p /tmp/c3w1/step1.sh | wc -l; sed -n 2,5p /tmp/c3w1/step1b.sh | wc -l; sed -n 2,3p /tmp/c3w1/step1c.sh | wc -l
       5
       4
       2
$ cmp <(sed -n 211,226p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(echo '$ date -u +%Y-%m-%dT%H:%M:%SZ'; echo 2026-11-12T00:44:34Z; echo '$ sed -n 3,7p /tmp/c3w1/step1.sh'; sed -n 3,7p /tmp/c3w1/step1.sh; echo '$ sed -n 2,5p /tmp/c3w1/step1b.sh'; sed -n 2,5p /tmp/c3w1/step1b.sh; echo '$ sed -n 2,3p /tmp/c3w1/step1c.sh'; sed -n 2,3p /tmp/c3w1/step1c.sh) && echo preamble-matches
preamble-matches
$ /tmp/vrf-c2/selfcheck.sh /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | sed 's#/tmp/c3pre/##'
2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[207] last_nonblank_line=207 last_nonblank_is_S13=YES lines=207
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -cE '[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem' docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker2.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:0
$ grep -cE '[A-Za-z0-9_~]/\.ssh/|\.ssh/[A-Za-z0-9_]|[A-Za-z0-9_-]+\.pem' /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
0
```

### rerun2.out

Command: `bash /tmp/c3w4/rerun2.sh > /tmp/c3w4/rerun2.out 2>&1`

Script text (`cat /tmp/c3w4/rerun2.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
mask() { perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'; }
export -f mask
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1 | mask; }
r "cmp <(sed -n 313,323p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(cat /tmp/c2mgr/pii.py) && echo pii.py-matches-pasted"
r "git ls-files docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l"
r "git diff 83891f6 -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l"
r "git diff HEAD -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l"
r "git diff --name-only HEAD 83891f6 | wc -l"
```

Output:
```
$ cmp <(sed -n 313,323p docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md) <(cat /tmp/c2mgr/pii.py) && echo pii.py-matches-pasted
pii.py-matches-pasted
$ git ls-files docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l
       0
$ git diff 83891f6 -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l
     144
$ git diff HEAD -- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | wc -l
       0
$ git diff --name-only HEAD 83891f6 | wc -l
      30
```

### rerun3.out

Command: `bash /tmp/c3w4/rerun3.sh > /tmp/c3w4/rerun3.out 2>&1`

Script text (`cat /tmp/c3w4/rerun3.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
W1=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md
W3=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
r "grep -c '19:39:57' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md"
r "grep -nE 'about 26|[^0-9:]26[^0-9]' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-120"
r "grep -nE 'keypath=56|keypath=15' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-160"
r "grep -nE '^(334|345|346|361|320):' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-80"
r "grep -nE 'worker4' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | cut -c1-120"
r "stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md /tmp/c3mgr/w2.pre.md"
r "grep -c 'S13' /tmp/c3mgr/scan.sh; grep -nE 'selfcheck|S13_' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -c 'correction-3-worker2'"
r "sed -n 25p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-120; sed -n 27p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-140"
r "awk -F'|' 'NR>=410 && NR<=419 {print NR, length(\$0), (\$6 ~ /ungraded at time of row \$/ ? \"ends-ungraded\" : \"other-ending\")}' MANIFEST.md"
r "sed -n 191p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-700"
r "sed -n 4p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-900 | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'"
r "sed -n 15p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-700"
```

Output:
```
$ grep -c '19:39:57' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md
1
$ grep -nE 'about 26|[^0-9:]26[^0-9]' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md | cut -c1-120
132:- W6: 37 command lines, not about 26. The function `r` is defined in no saved script, and the generating script is n
$ grep -nE 'keypath=56|keypath=15' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-160
126:docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
131:> docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
235:docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=15 mac_or_key_lines=163,168,169,170,171,172,174
354:- M:162. It gives `keypath=0` for M. The re-run gives `keypath=15` at lines 163, 168-172 and 174, all inside E7, and every hit is a bare pattern token. Mark
595:docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md ipv4_not_loopback=0 email=0 mac=0 keypath=56 mac_or_key_lines=163,168,169,170,171,172,174,3
633:docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md ipv4_not_loopback=0 email=0 mac=0 keypath=56 mac_or_key_lines=107,133,135,144,145,146,147,1
$ grep -nE '^(334|345|346|361|320):' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-80
$ grep -nE 'worker4' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md | cut -c1-120
29:The report above was last written before the evidence file. The leads in that evidence file were followed up by worke
$ stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%S' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md /tmp/c3mgr/w2.pre.md
2026-11-11T20:17:24 docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md
2026-11-11T20:17:17 /tmp/c3mgr/w2.pre.md
$ grep -c 'S13' /tmp/c3mgr/scan.sh; grep -nE 'selfcheck|S13_' docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | grep -c 'correction-3-worker2'
0
0
$ sed -n 25p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-120; sed -n 27p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c1-140
6. Ran the full email and rep-name scan over the bead's files (E2) and appended the MANIFEST rows (E3).
8. Re-ran the append-only and self-checks after worker3 (E1, v2 run), appended five MANIFEST rows (E3), and dispatched worker4 (ADVERSARIAL)
$ awk -F'|' 'NR>=410 && NR<=419 {print NR, length($0), ($6 ~ /ungraded at time of row $/ ? "ends-ungraded" : "other-ending")}' MANIFEST.md
410 441 ends-ungraded
411 437 ends-ungraded
412 263 ends-ungraded
413 313 ends-ungraded
414 410 ends-ungraded
415 350 ends-ungraded
416 301 ends-ungraded
417 301 ends-ungraded
418 303 ends-ungraded
419 257 ends-ungraded
$ sed -n 191p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-700
/reports/evidence/ (count below) and is not a path this unit touched; it was already shown as added in the index in the session-start status snapshot, which this unit did not produce and cannot re-run (REPORTED, not re-runnable). Outside docs/reports/evidence/ the staged count is 0.
$ sed -n 4p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-900 | perl -pe 's/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/(address withheld)/g'
6-11-11-v-rulings-filing-correction-2-worker6.md (lines 16, 34). Check 4: email addresses in added lines, under the corrected rule from Amear's channel of 2026-11-12 as applied by the master (DECISION_LOG 00:37:30Z). Nothing is committed or staged by this unit. F2 and F4 are out of scope; this report claims nothing about them.
$ sed -n 15p docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md | cut -c300-700
ble). Its report is a skeleton plus a manager note (E4). Its evidence file /tmp/c3w2/final.out held leads that I read and passed to worker3 as fix items: undefined variables in other original commands of the two correction-2 reports, an unpasted "no pre-edit copy exists" in the manager report's C3.5, and an unpasted "Nothing under vm/ or .claude/ was written." in the worker1 report. Report docs/rep
```

### rerun4.out

Command: `bash /tmp/c3w4/rerun4.sh > /tmp/c3w4/rerun4.out 2>&1`

Script text (`cat /tmp/c3w4/rerun4.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
r "grep -n '127\.0\.0\.1' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-110 | tail -n 8"
r "grep -nE '(^|[^0-9])41([^0-9]|\$)' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-140"
r "grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -d: -f1 | tr '\n' ' '; echo; grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | sort | uniq -c"
r "awk 'NR>=206 && NR<=463' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -oE 'id_rsa|id_ed25519|\.pem\b|\.ssh/' | wc -l"
```

Output:
```
$ grep -n '127\.0\.0\.1' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-110 | tail -n 8
490:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:11:127.0.0.1
491:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:34:127.0.0.1
492:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:334:127.0.0.1
493:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:345:127.0.0.1
494:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:346:127.0.0.1
495:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:361:127.0.0.1
496:docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:361:127.0.0.1
610:The M key-path count rose from 15 to 56. The 41 new tokens are all inside the Correction 3 section (block 
$ grep -nE '(^|[^0-9])41([^0-9]|$)' docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md | cut -c1-140
422:      41
471:(This is lines 1-41 of /tmp/c3w1/v_taskA.txt. Its last command, lines 42-44, searched the two sections for the three words this unit mus
610:The M key-path count rose from 15 to 56. The 41 new tokens are all inside the Correction 3 section (block 3: 41 tokens in M:206-463), fr
$ grep -nE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | cut -d: -f1 | tr '\n' ' '; echo; grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-worker6.md | sort | uniq -c
11 34 334 345 346 361 
   7 127.0.0.1
$ awk 'NR>=206 && NR<=463' /tmp/c3w3/pre/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -oE 'id_rsa|id_ed25519|\.pem\b|\.ssh/' | wc -l
      41
```

### extra.out

Command: `bash /tmp/c3w4/extra.sh > /tmp/c3w4/extra.out 2>&1`

Script text (`cat /tmp/c3w4/extra.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
r() { printf '$ %s\n' "$1"; bash -c "$1" 2>&1; }
r "for p in /tmp/vrf-c2/insert.py /tmp/c2w5/qcheck2.py /tmp/vrf-c2/lib.sh /tmp/c2fix/defs.sh /tmp/c2w5/verify.sh; do test -f \$p && echo \"exists \$p\" || echo \"missing \$p\"; done"
r "head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -E '^\\\$ ' | grep -oE '\\\$\\{?[A-Za-z_][A-Za-z0-9_]*' | tr -d '\${' | sort -u | tr '\n' ' '; echo"
r "head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -E '^\\\$ ' | grep -oE '\\\$\\{?[A-Za-z_][A-Za-z0-9_]*' | tr -d '\${' | sort -u | tr '\n' ' '; echo"
r "sed -n 83p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -o 'D=\$(mktemp -d)'"
```

Output:
```
$ for p in /tmp/vrf-c2/insert.py /tmp/c2w5/qcheck2.py /tmp/vrf-c2/lib.sh /tmp/c2fix/defs.sh /tmp/c2w5/verify.sh; do test -f $p && echo "exists $p" || echo "missing $p"; done
exists /tmp/vrf-c2/insert.py
exists /tmp/c2w5/qcheck2.py
exists /tmp/vrf-c2/lib.sh
exists /tmp/c2fix/defs.sh
exists /tmp/c2w5/verify.sh
$ head -n 205 docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md | grep -E '^\$ ' | grep -oE '\$\{?[A-Za-z_][A-Za-z0-9_]*' | tr -d '${' | sort -u | tr '\n' ' '; echo
N P PA T W5 f 
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -E '^\$ ' | grep -oE '\$\{?[A-Za-z_][A-Za-z0-9_]*' | tr -d '${' | sort -u | tr '\n' ' '; echo
A B C D D3 PA PIPESTATUS W5 f 
$ sed -n 83p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -o 'D=$(mktemp -d)'
D=$(mktemp -d)
```

### selfcheck.out

Command: `bash /tmp/c3w4/selfcheck.sh > /tmp/c3w4/selfcheck.out 2>&1`

Script text (`cat /tmp/c3w4/selfcheck.sh` content where applicable) and output follow.

Script:
```
#!/bin/bash
cd /Volumes/Sensidine/Praxis.build || exit 1
f=docs/reports/2026-11-12-v-rulings-filing-correction-3-worker4.md
N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//'); export N
S="Fills are optimistic; ""Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."
echo "name_ci=$(grep -ci -- "$N" $f) V1=$(perl -CSD -Mutf8 -ne 'BEGIN{ my @c=split //, lc $ENV{N}; $re=join q{[^\p{L}\p{N}]{0,3}}, map {quotemeta} @c; $re=qr/$re/i; $n=0 } $n++ if /$re/; END{ print $n }' $f)"
echo "email_lines=$(grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f) banned_word=$(grep -ci "ver""dict" $f) B1=$(grep -c "COMMIT-""INDEX" $f) B2=$(grep -c "COMMIT-""DIFF-SHA256" $f)"
echo "S13_containing=$(grep -cF -- "$S" $f) S13_standalone=$(grep -cxF -- "$S" $f) last_nonblank_is_S13=$([ "$(awk 'NF{l=$0} END{print l}' $f)" = "$S" ] && echo YES || echo NO) lines=$(wc -l < $f | tr -d ' ')"
```

Output:
```
name_ci=0 V1=0
email_lines=0 banned_word=0 B1=0 B2=0
S13_containing=1 S13_standalone=1 last_nonblank_is_S13=YES lines=749
```

## Findings

Re-run sample (check (b)): more than 10 commands from the files were run again in rerun.out, rerun2.out, rerun3.out and rerun4.out above. That includes every command in the correction-3 manager report's E2 scan (the four `git diff --name-only d056e91 83891f6` counts, `cat /tmp/c3mgr/scan.sh` compared by `cmp`, `MROWS=5 /tmp/c3mgr/scan.sh`, and the `sed -n '114p;132p'` line). Results that match the pastes: 26, 0, 2 and 24; scan.sh-matches-pasted-source; HEAD a962475; staged count 1, and 0 outside docs/reports/evidence/; MANIFEST `414a415,419` with 0 `<` lines; the five tail paths; the seven `--- E` headers and count 68 in /tmp/c3w2/final.out; the worker2 note diff `17a18,30`; the byte counts 11554/11556 and 19841/19844; both /tmp/c2pre sha256 values; 265 and 242 lines; `grep rc=1` for `P=`; lib.sh:4; pii.py-matches-pasted; preamble-matches; the pre-insertion worker6 self-check `at=[207]`; the key-path grep giving 0, 0 and 0; the worker1 figures 41 and the 127.0.0.1-only IPv4 lines. The one result that does not match is the E2 scan output (Finding 1).

Side effect disclosed: running `/tmp/c3mgr/scan.sh` rewrote /tmp/c3mgr/scanset.txt, /tmp/c3mgr/dec_added.txt and /tmp/c3mgr/manifest_tail.txt. scanset.txt was restored from a copy taken just before the run (rerun.out, the `cp` command). The other two were regenerated from the same sources, and the DECISIONS.md and MANIFEST count lines of the new output equal the pasted ones (the diff in rerun.out lists no difference on those lines).

1. MAJOR, check (c) and the address rule. docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:240 contains an email address. It is the synthetic positive-control address inside the pasted source of /tmp/c3mgr/scan.sh: 15 characters, top-level domain `example` (rerun.out: `240`, `len=15 tld=example`; the script file itself has 1 match). The rule allows no email address other than MFFU's support address quoted from a header or MFFU text, and this unit exists to cure exactly that check. Two present-tense claims in the same report are contradicted by this: :33 "E2 shows they are the only two email hits in the bead" and :277 "exactly two email hits". A re-run of the E2 scan now gives `docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md email_lines=1 at=[240]` and `email_lines_total_files=3` (rerun.out diff). The report's own self-check prints `1` for the email count at :345, and nothing in the report explains it. checks.out C1 shows `email_lines=1` for this file and 0 for every other file in scope.

2. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:337 says the report has "33 lines". It has 352 (rerun.out: `352 docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md`; the grep for that line prints `337:... 33 lines; new; this report.`). This is not one of the pending fields: the worker4 row at :336 is the pending one.

3. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:11 says the S13 sentence is once, standalone, last line "in each new report and in each edited report (E1 and E2 self-check output)". No self-check in the report covers docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md: E1 v1 and v2 do not name it, and scan.sh contains no S13 check (rerun3.out: `grep -c 'S13' /tmp/c3mgr/scan.sh` gives 0, and the grep for a selfcheck line naming correction-3-worker2 gives 0). The claim is true now (checks.out: worker2 `S13_standalone=1 at=[31] last_is_S13=YES`), but the manager report does not paste it.

4. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-manager.md:25 (step 6, "appended the MANIFEST rows (E3)") and :27 (step 8, "appended five MANIFEST rows (E3)") say that rows were appended twice. E3 and my re-run show one block of five rows in total (`414a415,419`, checks.out F5 and rerun.out). Either step 6 appended some of those five and step 8's "five" is wrong, or step 6 appended none. The log does not say how many rows step 6 added. No paste supports both statements.

5. MINOR, check (g), S2. docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md:485: "With these definitions the 37 lines can be run as written, but none was re-run here." Whether the lines can be run is asserted but not tested. The same paragraph marks the bindings of `C`, `D3` and `W5` as INFERRED (:482). The sibling section in the manager report labels the matching case "UNVERIFIED as re-runnable" (manager :562-564, quoted by worker3 at worker3:128-129). The claim should carry the same label. The helper scripts exist (extra.out: `exists /tmp/vrf-c2/insert.py`, `exists /tmp/c2w5/qcheck2.py`), but that does not show the 37 lines run.

6. MINOR, check (b). docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md:132 "37 command lines, not about 26": the figure "about 26" has no paste anywhere in the worker3 report (rerun3.out: the grep finds only line 132). Also :133 "before worker1 began (19:39:57 local)": the only occurrence of 19:39:57 in the worker3 report is that prose line (rerun3.out count 1). The paste is in a different file, the worker1 addendum (worker1 :663, :674). Line 127 does point to "the inserted sections", but the brief requires the support to be in the same file.

7. MINOR, check (g). docs/reports/2026-11-12-v-rulings-filing-correction-3-worker2.md:29 says the leads "were followed up by worker3 (BUILD fix) and checked again by worker4 (a fresh ADVERSARIAL pass)". That is past tense for a check that had not run yet. The report's mtime is 2026-11-11T20:17:24 local (rerun3.out). The manager's v2 run, after which step 8 dispatched worker4, is 20:17:07 (manager :151). This worker4 pass started at 2026-11-12T01:22:31Z, which is 20:22:31 local at -0500 (rerun.out first line).

Checks with no finding (each with its output above):
- (a) Placeholder commands. Every `$ ` line hit in scanA.out is one of three things: a `<NAME>`/`<S13>` replacement text, the quoted original M:163 printed as the output of `sed -n 163p` (manager :375-376, worker1 :165-166), or grep output of original lines (manager :478-483). scanA.out A2 lists only `ENV` (perl) and `PIPESTATUS` (bash) as having no definition, apart from `T` in the manager report, which C3.8 covers as the original being superseded. The full variable list for the original bodies (manager 1-205: N, P, PA, T, W5, f; worker6 1-206: A, B, C, D, D3, PA, PIPESTATUS, W5, f) is covered by C3.1, C3.8 and worker6 C3.4. `D` is defined inline at worker6:83 (`D=$(mktemp -d)`), and `f` by the `for` loops (extra.out has the variable lists and the line 83 match).
- (d) Rep name: `name_ci=0 V1=0` in every in-scope report, and the positive control fires (`HIT_lines=1`), in checks.out C1.
- (e) S13 sentence: `S13_standalone=1`, `last_is_S13=YES` in every in-scope report. The banned word and the two banned strings count 0 in every in-scope report (checks.out C1).
- (f) Byte scope: manager and worker6 `head_205_identical`/`head_206_identical` plus `last_line_identical`, so the content is pre lines 1-205 (1-206), then the insertion, then the original final line. The 2026-11-11 worker2 and worker5 reports differ only at :169 and :79, and only in the address span (normalized diff). The worker1 report shows `640a641,677` against /tmp/c3w3/pre. The correction-3 worker2 report shows `17a18,30` against w2.pre.md. MANIFEST shows `MANIFEST head_414_identical` and `414a415,419` (checks.out F1-F5).
- (h) MANIFEST rows 415-419: 7 fields, `Report | 3 | 2026-11-12`, path exists, ending `ungraded at time of row`, the same as rows 410-414 (checks.out H1, rerun3.out).

Out of scope, reported and not fixed: MANIFEST.md lines 335 and 336 match the rep's name (scanA.out, first line of the name/banned section). They are pre-existing: lines 1-414 are byte-identical to /tmp/c3mgr/MANIFEST.pre.md. The 2026-11-11 worker2 report has `S13_containing=3` (checks.out C1), as worker1 :584 already discloses. MANIFEST also has pre-existing lines with the banned word and banned strings at lines 99-374 (scanA.out), all at or below row 414.

## Result

FAIL. 1 MAJOR, 6 MINOR.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
