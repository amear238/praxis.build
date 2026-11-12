# Unit 2026-11-11-v-rulings-filing-correction-2, worker6 (ADVERSARIAL)

## Task
Mode ADVERSARIAL, narrow scope, bead Praxis_build-n1y. Try to break the second fix pass (worker5). Scope: only the lines that differ between the /tmp/c2w5 copies and the current (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md and (d) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md, plus all of (e) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md. Read-only apart from this report. No index or HEAD changes. Nothing under .claude/ was touched.

## Criteria
- S1: every claim in a report has pasted command output, not a description of output.
- S2: no component is reported at a higher level than the evidence supports.
- S13: the S13 sentence appears once in each file, standalone, as the last line.
- Append-only: (a) lines 1-264 and its last line are byte-identical to /tmp/c2pre; (d) has no `<` lines against /tmp/c2w5.
- Name: the support rep's first name appears 0 times in (a), (c), (d), (e) and this report. PII: no IPv4 other than 127.0.0.1, no MAC, no key path, no email.

## Commands and output
All commands ran under bash from the repo root, after sourcing /tmp/vrf-c2/lib.sh and /tmp/c2fix/defs.sh, with `C`, `D3` and `W5` set to (c), (d) and (e). `r` prints `$ cmd` and then the output passed through `M`. The whole stream was then masked for S13. The name was built only at runtime and was never typed or printed.

Diff sizes and the `<` counts (zsh; `for f in <a c d>; do echo "=== $f"; wc -l /tmp/c2w5/$f $R/$f | grep -v total; echo "lt=$(diff /tmp/c2w5/$f $R/$f | grep -c '^<')"; done; wc -l <e>; selfcheck.sh <this report>`). Output is verbatim:
```
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
     408 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
lt=0
     358 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[205] last_nonblank_line=205 last_nonblank_is_S13=YES lines=205
V1 positive control (hyphen-split synthetic line): HIT_lines=1
```
The self-check line for this report was taken before this edit. The edit adds lines, so `at=`, `last_nonblank_line=` and `lines=` for this report are stale by the number of lines added. The name count stays 0 because the edit adds no name. The only IPv4, MAC or email hit in this report is the 127.0.0.1 in the Criteria section.

Block 1: the commands in the new (a) block ((a):318-343, which (e):20-47 repeats) and the (c) third control, re-run:
```
$ date "+%Y-%m-%dT%H:%M:%S"
2026-11-11T18:12:00
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
       2
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
:40 :46 :33 :58 :08 :51 :210 :33 :58 :211 :218 :218 :209 :250 
$ sed -n "212p;215p" $PA | od -c
0000000                        .   .   .  \n                       .   .
0000020    .  \n                                                        
0000022
$ sed -n "213p;214p;216p" $PA | cut -c1-60
    15	## Verification evidence (command output)
    16	(pending)
    27	Result: PENDING
$ wc -l $B
     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
$ git ls-files -s -- $B | wc -l
       0
$ git ls-tree HEAD -- $B | wc -l
       0
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null
/private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | wc -l
       2
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | while read f; do wc -l "$f"; stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" "$f"; done
     488 /private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:44:14
     242 /private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:08:51
$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" $B
2026-11-11T17:50:55
$ sed -n 314p $A | grep -o "UNVERIFIED" | wc -l
       1
$ grep -c "assert " /tmp/vrf-c2/insert.py
3
$ sed -n 314p /tmp/c2fix/${A##*/} | cut -c1-80
Result. The manager report has been rewritten since section 7 was written. It no
$ sed -n 560p /tmp/c2w5/${C##*/} | cut -c1-80
- Section 1 (:32-64). Its block is still in (a) C2.1. The conclusion drawn from 
$ sed -n 161p /tmp/c2w5/${D3##*/} | cut -c1-80
(a):281 now quotes :210 with its 6 leading spaces. (b) C2.2 has a new heading at
$ cmp <(sed -n 9,16p $W5) <(cat /dev/null) >/dev/null; sed -n 314p /tmp/c2fix/${A##*/} | cmp - <(sed -n 10p $W5); echo "e10 vs c2fix314 rc=$?"
cmp: EOF on /dev/fd/62
e10 vs c2fix314 rc=0
$ D=$(mktemp -d); cp $PA "$D/t.md"; printf "x\n" > "$D/noblank.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/noblank.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"; od -c "$D/noblank.md"; rm -r "$D"
Traceback (most recent call last):
  File "/tmp/vrf-c2/insert.py", line 7, in <module>
    assert seclines[-1] == '' and seclines[-2] == '', 'section must end with one blank line'
AssertionError: section must end with one blank line
rc=1
target unchanged rc=0
0000000    x  \n                                                        
0000002
```
(The first `cmp` in the `e10` line is a leftover no-op and its `EOF` message means nothing. The second `cmp` is the test: the pasted (e):10 is byte-identical to /tmp/c2fix line 314.)

Block 2: qcheck2, the (e) Self-check block, and PII, re-run:
```
$ python3 -I /tmp/c2w5/qcheck2.py > /tmp/w6q.$$ ; sed -n 110,136p $W5 | M | diff - /tmp/w6q.$$; echo "diff vs pasted rows rc=$?"; rm /tmp/w6q.$$
1d0
< $ python3 -I /tmp/c2w5/qcheck2.py | M
diff vs pasted rows rc=1
$ python3 -I /tmp/c2w5/qcheck2.py | wc -l
      26
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c " MATCH "
19
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c MISMATCH
0
$ python3 -I /tmp/c2fix/qcheck.py | grep -c ":22[345] "
0
$ sed -n 65,109p $W5 | tail -n +2 | cmp - /tmp/c2w5/qcheck2.py; echo "pasted src vs file rc=$?"
pasted src vs file rc=0
$ sed -n 9p /tmp/c2fix/qcheck.py | cut -c1-60
        for m in re.finditer(r':(\d+) (`[^`]*(?:`[^`]*)*?`|"
$ grep -n "^Original wording:" $A | cut -d: -f1 | tr "\n" " "; echo
281 646 674 851 856 
$ grep -n "^Original wording:" $B | cut -d: -f1 | tr "\n" " "; echo
258 427 492 600 
$ diff -d $PA $A | grep -v "^>"
264a265,874
$ diff -d $PA $A | grep -c "^<"
0
$ cmp <(head -n 264 $PA) <(head -n 264 $A); echo "first264 rc=$?"
first264 rc=0
$ cmp <(tail -n 1 $PA) <(tail -n 1 $A); echo "lastline rc=$?"
lastline rc=0
$ diff /tmp/c2fix/${C##*/} $C | grep "^[0-9]"
450a451,490
451a492,576
$ diff /tmp/c2fix/${C##*/} $C | grep -c "^<"
0
$ grep -n "^## Addendum (worker3, fix pass)" $C
452:## Addendum (worker3, fix pass)
$ diff /tmp/c2w5/${D3##*/} $D3 | grep "^[0-9]"
322a323,407
$ diff /tmp/c2w5/${D3##*/} $D3 | grep -c "^<"
0
$ diff /tmp/c2w5/${A##*/} $A | grep "^[0-9]"; diff /tmp/c2w5/${C##*/} $C | grep "^[0-9]"
314c314,344
492c492
526a527,533
528a536,538
560c570
$ /tmp/vrf-c2/selfcheck.sh $A $C $D3 $W5 | S
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[875] last_nonblank_line=875 last_nonblank_is_S13=YES lines=875
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[577] last_nonblank_line=577 last_nonblank_is_S13=YES lines=577
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[408] last_nonblank_line=408 last_nonblank_is_S13=YES lines=408
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[358] last_nonblank_line=358 last_nonblank_is_S13=YES lines=358
V1 positive control (hyphen-split synthetic line): HIT_lines=1
$ grep -nE "([0-9]{1,3}\.){3}[0-9]{1,3}" $A $C $D3 $W5 | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c
$ grep -ciE "([0-9a-f]{2}:){5}[0-9a-f]{2}" $A $C $D3 $W5
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
$ grep -ciE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}" $A $C $D3 $W5
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
$ grep -ciE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $A $C $D3 $W5
docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md:0
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:1
$ git diff --cached --name-only -- $A $C $D3 $W5 | wc -l
       0
```
(The diff in the first command shows only the `$` header line that I included in the sed range. All 26 pasted rows are byte-identical to the live output.)

Block 3: where the key-path hit in (e) comes from, and the line bounds of the (a) block:
```
$ grep -noE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5
347:.ssh/
347:.pem
$ grep -nE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5 | cut -c1-70
347:$ grep -ciE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $A $C $D3 $W5
$ sed -n 284,313p $A | grep -n "manager.md" | cut -c1-90
5:     242 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
15:/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
19:     242 /tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
```
(The echo of these headers in my shell dropped the `\b`. The commands that actually ran contained it.)

Search for definitions of `C`, `D3` and `W5` (output trimmed to the matching lines):
```
/tmp/c2w5/diffs.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/diffs.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
/tmp/c2w5/verify.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/verify.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
/tmp/c2w5/verify.sh:5:W5=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
/tmp/c2fix/gen_w3.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
```
grep of (d) for `qcheck.py`: the only hits are (d):163, :180 and :404, which run it, and (d):324, the Erratum prose. No `cat /tmp/c2fix/qcheck.py` appears in (d).

Re-run differences that are explained, not flagged: the `date` reads 18:12:00 instead of 18:07:10 because time has passed. (b) still has 684 lines, and its mtime of 17:50:55 is earlier than worker5's 18:07:10 run, so that figure is current. Everything else in Blocks 1 and 2 matches the pasted output exactly, apart from the stale self-check values in Findings 1 and 2.

## Findings
1. MINOR (S2 and stale self-check), (e):300 and (e):334. (e):300 says pasting the Self-check block "changes only the `lines=` value for the report". That is false. (e):334 pastes `at=[308] last_nonblank_line=308 ... lines=308` for (e). The re-run gives `at=[358] last_nonblank_line=358 ... lines=358` (Block 2). Three values went stale, not one. The S13 placement itself is fine in the re-run: S13 appears once, standalone, as the last line.
2. MINOR (stale self-check), (e):351. It pastes `...-2-worker5.md:0` for the key-path grep. The re-run gives `:1`. The hit is the grep's own pattern text at (e):347 (`.ssh/` and `.pem`, Block 3), so it is a self-match and not a real key path. There is no PII leak, but the pasted count of 0 for (e) no longer holds, and (e):300's caveat does not mention it.
3. MINOR (S1), (d):324, the Erratum. The statement that qcheck.py's "pattern `:(\d+) ` needs a space right after the number" is not backed by any pasted source. (d) runs qcheck.py at :163, :180 and :404 but never pastes it. The only pasted support is the indirect count `grep -c ":22[345] "` = 0. The claim is true: /tmp/c2fix/qcheck.py:9 has `r':(\d+) (` (Block 2). But it is a description, not pasted output.
4. MINOR (S1, reproducibility), (e):4. It says "Definitions are those of /tmp/vrf-c2/lib.sh and /tmp/c2fix/defs.sh". But `$C`, `$D3` and `$W5`, used at (e):11, :13 and :310-352, are defined in neither file. They are defined only in /tmp/c2w5/verify.sh and diffs.sh, which (e) does not name. With the stated definitions, those commands run on empty variables.

Checked and not broken: all new factual figures. (b) has 684 lines. The `find` returns 2 files, with 488 and 242 lines and mtimes 17:44:14 and 17:08:51. The UNVERIFIED count is 2. The ref list matches. Lines :212 and :215 are elision markers (5 spaces then `...`). Lines :213, :214 and :216 are the pasted lines. insert.py has 3 asserts. The third negative control fires with rc=1 and leaves the target unchanged. qcheck2 gives 26 rows, 19 MATCH and 0 MISMATCH, and its pasted source is byte-identical to the file. The (a) line shifts are +30 (616 to 646, 644 to 674, 821 to 851, 826 to 856), which agree with the `Original wording:` line numbers. The (a) block :284-313 shows (b) at 242 lines, as (a):314 says. Append-only holds: (a) first264 rc=0, lastline rc=0, 0 `<` lines; (d) 0 `<` lines. The name count is 0 and the V1 count is 0 in (a), (c), (d) and (e). There is no IPv4, no MAC and no email. Nothing is staged for these four paths.

## Result
FAIL, on four MINOR defects and no MAJOR one. Findings 1 and 2 are stale self-check values in (e). Findings 3 and 4 are S1 gaps in (d):324 and (e):4. The substance of the fixes to (a), (c) and (d) holds.

## Correction 3 (2026-11-12)
Unit 2026-11-12-v-rulings-filing-correction-3, bead Praxis_build-n1y, written by that unit's worker1 (report: docs/reports/2026-11-12-v-rulings-filing-correction-3-worker1.md). This section is append-only. No line above it was changed. Each line named below stands as written above and is superseded by this section. Every check here was run on this report and the other files as they stood before this section was inserted, when this report had 207 lines.

Preamble. The checks ran under bash from the repo root as two scripts, /tmp/c3w1/step1.sh and /tmp/c3w1/step1b.sh. Each `$ ` line below is the literal string the script passed to `run`. The lines after it are that command's output, with stderr included. The lines each script ran before its checks:
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
`N` holds the support rep's first name. It is built at runtime from the evidence filename and is never printed. `S13` holds the S13 sentence, read from /tmp/vrf-c2/selfcheck.sh, and is used only to mask it. (step1c.sh, also listed, ran no check for this section.)

### C3.1 Line 16: the command with placeholders `<a c d>`, `<e>`, `<this report>` and an undefined `$R`
Re-run as a literal command (a = 2026-11-11-v-rulings-filing-correction-1-worker1.md, c = 2026-11-11-v-rulings-filing-correction-2-worker1.md, d = 2026-11-11-v-rulings-filing-correction-2-worker3.md, e = docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md, this report = docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md). Then the line counts and mtimes of the manager's /tmp/c2mgr copies of (d) and (e) against the live files, and the full plain diffs:
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
The same two comparisons with `diff -d`, the /tmp/c2w5 copy of (d) against the /tmp/c2mgr copy, and the manager-note headings:
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
Result, compared with lines 18-31:
- (a): 845 and 875 lines, `lt=1`. Same as lines 18-21.
- (c): 567 and 577 lines, `lt=2`. Same as lines 22-25.
- (d): the /tmp/c2w5 copy is 323 lines and `lt=0`, as at lines 27 and 29. The live file is now 428 lines. Line 28 shows 408.
- (e): now 370 lines. Line 30 shows 358.
- This report: the self-check now gives `at=[207] last_nonblank_line=207 lines=207`. Line 31 shows 205 for all three. The name count is 0, as at line 31.
Why (d) and (e) differ: the /tmp/c2mgr copies are 408 and 358 lines, the same figures as lines 28 and 30. The /tmp/c2mgr copy of (d) is the /tmp/c2w5 copy plus one added block (`322a323,407`, 0 `<` lines). Against the live files, `diff -d` gives one added hunk each, `407a408,427` (20 lines) and `357a358,369` (12 lines), with 0 `<` lines. The added lines are the manager notes: `## Manager note` occurs 0 times in each copy and once in each live file, at (d):408 and (e):358. The plain `diff` splits the (d) insertion into two hunks (`405a406,424` and `406a426`). The live (d) and (e) have mtime 2026-11-11T18:15:13, later than this report's 2026-11-11T18:14:52. Lines 28 and 30 match the /tmp/c2mgr copies, so they held for (d) and (e) as they stood without the notes. That those copies are the exact bytes this report measured is INFERRED from the line counts. Lines 28, 30 and 31 are not current.

### C3.2 Line 34: stale self-check fields, and "The only IPv4, MAC or email hit in this report is the 127.0.0.1 in the Criteria section"
The self-check of this report (207 lines, before this section was inserted), the three literal scans, each also piped to `wc -l`, and pii.py:
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
Result:
- Stale self-check fields: reproduces. `at=`, `last_nonblank_line=` and `lines=` are now 207, and line 31 shows 205. The name count is 0.
- MAC: 0 lines. Email: 0 lines. Both reproduce. pii.py agrees: `ipv4_not_loopback=0 email=0 mac=0`.
- IPv4: does NOT reproduce as stated. The scan matches 2 lines, not 1: line 11 (the Criteria section) and line 34, the claim sentence itself, which also contains 127.0.0.1. The statement "The only IPv4 ... hit in this report is the 127.0.0.1 in the Criteria section" is WRONG by one line. Both hits are the loopback address. No other IPv4 address is in this report.

### C3.3 Summary
Did not reproduce: lines 28, 30 and 31 (not current, because the manager notes in (d) and (e) and the later lines of this report were added after them), and the IPv4 part of line 34 (WRONG, 2 hit lines and not 1). Everything else named above reproduces.

### C3.4 Variables used in other original commands
Added by worker3 of unit 2026-11-12-v-rulings-filing-correction-3 (report: docs/reports/2026-11-12-v-rulings-filing-correction-3-worker3.md). Insertion only. No line above was changed. This subsection covers the `$ ` lines in lines 1-206 that use a shell variable this report does not define. The commands ran under bash through /tmp/c3w3/gen.sh, which is pasted in full as the second command below. Each `$ ` line is one line of /tmp/c3w3/cmds_w6.txt, passed unchanged to `run`. Line 7 of gen.sh masks the whole output stream for the name and the S13 sentence.
```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-12T01:12:25Z
$ cat -n /tmp/c3w3/gen.sh
     1	#!/bin/bash
     2	cd /Volumes/Sensidine/Praxis.build || exit 1
     3	N=$(ls docs/reports/evidence/ | grep -i '^2026-10-28-mffu-.*-reply\.png$' | sed -e 's/^2026-10-28-mffu-//' -e 's/-reply\.png$//')
     4	S13=$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)
     5	export N S13
     6	run() { printf '$ %s\n' "$1"; eval "$1" 2>&1; }
     7	while IFS= read -r c <&3; do run "$c" </dev/null; done 3< "$1" | perl -pe 's/\Q$ENV{N}\E/<NAME>/gi; s/\Q$ENV{S13}\E/<S13>/g'
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
40:$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
42:$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
44:$ sed -n "212p;215p" $PA | od -c
48:$ sed -n "213p;214p;216p" $PA | cut -c1-60
52:$ wc -l $B
54:$ git ls-files -s -- $B | wc -l
56:$ git ls-tree HEAD -- $B | wc -l
68:$ stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" $B
70:$ sed -n 314p $A | grep -o "UNVERIFIED" | wc -l
74:$ sed -n 314p /tmp/c2fix/${A##*/} | cut -c1-80
76:$ sed -n 560p /tmp/c2w5/${C##*/} | cut -c1-80
78:$ sed -n 161p /tmp/c2w5/${D3##*/} | cut -c1-80
80:$ cmp <(sed -n 9,16p $W5) <(cat /dev/null) >/dev/null; sed -n 314p /tmp/c2fix/${A##*/} | cmp - <(sed -n 10p $W5); echo "e10 vs c2fix314 rc=$?"
83:$ D=$(mktemp -d); cp $PA "$D/t.md"; printf "x\n" > "$D/noblank.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/noblank.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"; od -c "$D/noblank.md"; rm -r "$D"
97:$ python3 -I /tmp/c2w5/qcheck2.py > /tmp/w6q.$$ ; sed -n 110,136p $W5 | M | diff - /tmp/w6q.$$; echo "diff vs pasted rows rc=$?"; rm /tmp/w6q.$$
109:$ sed -n 65,109p $W5 | tail -n +2 | cmp - /tmp/c2w5/qcheck2.py; echo "pasted src vs file rc=$?"
113:$ grep -n "^Original wording:" $A | cut -d: -f1 | tr "\n" " "; echo
115:$ grep -n "^Original wording:" $B | cut -d: -f1 | tr "\n" " "; echo
117:$ diff -d $PA $A | grep -v "^>"
119:$ diff -d $PA $A | grep -c "^<"
121:$ cmp <(head -n 264 $PA) <(head -n 264 $A); echo "first264 rc=$?"
123:$ cmp <(tail -n 1 $PA) <(tail -n 1 $A); echo "lastline rc=$?"
125:$ diff /tmp/c2fix/${C##*/} $C | grep "^[0-9]"
128:$ diff /tmp/c2fix/${C##*/} $C | grep -c "^<"
130:$ grep -n "^## Addendum (worker3, fix pass)" $C
132:$ diff /tmp/c2w5/${D3##*/} $D3 | grep "^[0-9]"
134:$ diff /tmp/c2w5/${D3##*/} $D3 | grep -c "^<"
136:$ diff /tmp/c2w5/${A##*/} $A | grep "^[0-9]"; diff /tmp/c2w5/${C##*/} $C | grep "^[0-9]"
142:$ /tmp/vrf-c2/selfcheck.sh $A $C $D3 $W5 | S
148:$ grep -nE "([0-9]{1,3}\.){3}[0-9]{1,3}" $A $C $D3 $W5 | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort | uniq -c
149:$ grep -ciE "([0-9a-f]{2}:){5}[0-9a-f]{2}" $A $C $D3 $W5
154:$ grep -ciE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}" $A $C $D3 $W5
159:$ grep -ciE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $A $C $D3 $W5
164:$ git diff --cached --name-only -- $A $C $D3 $W5 | wc -l
171:$ grep -noE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5
174:$ grep -nE "id_(rsa|ed25519|ecdsa)|\.ssh/|\.pem\b" $W5 | cut -c1-70
176:$ sed -n 284,313p $A | grep -n "manager.md" | cut -c1-90
$ head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -cE '^\$ .*\$\{?(PA|PB|A|B|T|P|W5|D3|C|R)\b'
37
$ for v in PA PB A B T P W5 D3 C R; do printf '%s: ' "$v"; head -n 206 docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md | grep -nE '^\$ .*\$\{?'"$v"'\b' | cut -d: -f1 | tr '\n' ' '; echo; done
PA: 44 48 83 117 119 121 123 
PB: 
A: 40 42 70 74 80 113 117 119 121 123 136 142 148 149 154 159 164 176 
B: 52 54 56 68 115 
T: 
P: 
W5: 80 97 109 142 148 149 154 159 164 171 174 
D3: 78 132 134 142 148 149 154 159 164 
C: 76 125 128 130 136 142 148 149 154 159 164 
R: 
$ sed -n 4p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
Mode ADVERSARIAL, narrow scope, bead Praxis_build-n1y. Try to break the second fix pass (worker5). Scope: only the lines that differ between the /tmp/c2w5 copies and the current (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md, (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md and (d) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md, plus all of (e) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md. Read-only apart from this report. No index or HEAD changes. Nothing under .claude/ was touched.
$ sed -n 14p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
All commands ran under bash from the repo root, after sourcing /tmp/vrf-c2/lib.sh and /tmp/c2fix/defs.sh, with `C`, `D3` and `W5` set to (c), (d) and (e). `r` prints `$ cmd` and then the output passed through `M`. The whole stream was then masked for S13. The name was built only at runtime and was never typed or printed.
$ sed -n 16p docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md
Diff sizes and the `<` counts (zsh; `for f in <a c d>; do echo "=== $f"; wc -l /tmp/c2w5/$f $R/$f | grep -v total; echo "lt=$(diff /tmp/c2w5/$f $R/$f | grep -c '^<')"; done; wc -l <e>; selfcheck.sh <this report>`). Output is verbatim:
$ grep -nE '^(A|B|PA|PB)=' /tmp/vrf-c2/lib.sh
5:A=docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md
6:B=docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
7:PA=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md
8:PB=/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ grep -nE '^M\(\)' /tmp/vrf-c2/lib.sh
4:M() { N="$N" perl -pe 's/\Q$ENV{N}\E/<NAME>/gi'; }
$ grep -nE '^(T|W)=' /tmp/c2fix/defs.sh | cut -d= -f1
2:T
3:W
$ grep -nE '^S\(\)' /tmp/c2fix/defs.sh
4:S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }
$ grep -nE '^(C|D3|W5)=' /tmp/c2w5/verify.sh /tmp/c2w5/diffs.sh
/tmp/c2w5/verify.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/verify.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
/tmp/c2w5/verify.sh:5:W5=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
/tmp/c2w5/diffs.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/diffs.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
$ grep -rnE '(^|[^A-Za-z_0-9])(C|D3|W5|R)=' /tmp/vrf-c1 /tmp/vrf-c2 /tmp/c2fix /tmp/c2w5 /tmp/c2mgr /tmp/c2pre --include='*.sh' --include='*.py' | cut -c1-120; echo "grep rc=${PIPESTATUS[0]}"
/tmp/vrf-c2/selfcheck_cmds.sh:2:R=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2fix/gen_c.sh:3:R=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2fix/gen_c.sh:6:run 'R=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md'
/tmp/c2fix/gen_c.sh:7:run 'grep -c "^R=" $R'
/tmp/c2fix/mk_add.py:4:Worker3 of unit 2026-11-11-v-rulings-filing-correction-2 added this section in the fix pass. No e
/tmp/c2fix/assemble.py:6:defs = '```\n' + ''.join(open('/tmp/vrf-c2/lib.sh').read().splitlines(True)[2:9]) + ''.join(l f
/tmp/c2fix/gen_w3.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/verify.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/verify.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
/tmp/c2w5/verify.sh:5:W5=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
/tmp/c2w5/diffs.sh:3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
/tmp/c2w5/diffs.sh:4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
grep rc=0
$ grep -rnE '(^|[^A-Za-z_0-9])r ?\(\)' /tmp/vrf-c1 /tmp/vrf-c2 /tmp/c2fix /tmp/c2w5 /tmp/c2mgr /tmp/c2pre --include='*.sh' --include='*.py'; echo "grep rc=$?"
grep rc=1
$ grep -rlF 'w6q.' /private/tmp 2>/dev/null | grep -v -e '^/private/tmp/c3w3/' -e '/\.git/' | sort
/private/tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S" /tmp/vrf-c2/lib.sh /tmp/c2fix/defs.sh /tmp/c2w5/verify.sh /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
2026-11-11T17:15:24 /tmp/vrf-c2/lib.sh
2026-11-11T17:49:37 /tmp/c2fix/defs.sh
2026-11-11T18:09:09 /tmp/c2w5/verify.sh
2026-11-11T18:14:52 /tmp/c3pre/2026-11-11-v-rulings-filing-correction-2-worker6.md
```
What the output shows:
- 37 original command lines use such a variable. They use `A`, `PA`, `B`, `C`, `D3` and `W5`. None uses `PB`, `T`, `P` or `R`. `R` appears only in the prose at line 16, which C3.1 covers.
- Line 14 is the only place this report says where its variables come from: lib.sh and defs.sh were sourced, and `C`, `D3` and `W5` were set to (c), (d) and (e). Line 4 gives the (c), (d) and (e) paths.
- `A`, `B`, `PA`: /tmp/vrf-c2/lib.sh:5-7, pasted above. `PB` (lib.sh:8) is not used. The functions `M` (lib.sh:4) and `S` (defs.sh:4), which these lines call as `| M` and `| S`, are also pasted above. defs.sh also defines `T` and `W`. Only their names are shown, because their values are machine-local transcript paths. No line here uses them. The last modification of lib.sh (17:15:24) and defs.sh (17:49:37) is earlier than the /tmp/c3pre copy of this report (18:14:52, a `cp -p` copy that keeps the source's mtime).
- `C`, `D3`, `W5`: nothing in this report defines them except line 14's prose. The saved definitions are /tmp/c2w5/verify.sh:3-5 and /tmp/c2w5/diffs.sh:3-4. /tmp/c2fix/gen_w3.sh:3 also sets `C` to the same path. Their values are the (c), (d) and (e) paths at line 4. That these are the values this report's commands used is INFERRED from line 14 and the matching paths.
- `R`: /tmp/vrf-c2/selfcheck_cmds.sh:2 and /tmp/c2fix/gen_c.sh:3 set it to docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md. No `$ ` line here uses it.
- Not defined anywhere searched: the function `r` that line 14 describes (grep rc=1). No `$ ` line calls `r`, so no command line depends on it. The script that produced this report's command block is not saved either: under /private/tmp, only the /tmp/c3pre copy of this report contains `w6q.`, a string from line 97.
With these definitions the 37 lines may be re-runnable, but that is UNVERIFIED: none was re-run here. Their original output stands as pasted at the time.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
