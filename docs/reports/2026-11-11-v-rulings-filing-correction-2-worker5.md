# 2026-11-11 v-rulings-filing correction 2 - worker5 (second fix pass)

## Task
Mode BUILD (fix), unit 2026-11-11-v-rulings-filing-correction-2, bead Praxis_build-n1y. Fix the four MINOR defects in docs/reports/2026-11-11-v-rulings-filing-correction-2-worker4.md (Findings 1-4) in (a) docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md (Correction 2 region only), (c) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md (Addendum region only) and (d) docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md (append an Erratum before the final line only). Copies of (a), (c) and (d) were taken to /tmp/c2w5/ before any edit. Definitions are those of /tmp/vrf-c2/lib.sh and /tmp/c2fix/defs.sh (`M` masks the name as `<NAME>`, `S` masks the S13 sentence as `<S13>`; $A is (a), $PA is its /tmp/c2pre copy, $B is (b), the manager report). Nothing was staged; the index check is in the Self-check block.

## Commands and output
Pre-edit wording of the three lines the findings point at, and the assertion count of insert.py (all masked):
```
$ sed -n 314p /tmp/c2fix/${A##*/} | M
Result. The manager report has been rewritten since section 7 was written. It now has 242 lines (the original said 27). Its mtime is 2026-11-11T14:40:46 (the original said 14:33:58). It has 8 lines starting `## `, 0 lines equal to `(pending)`, and 0 lines containing `PENDING`. The file is untracked and not in the index, so git holds no earlier copy. Under /tmp and /private/tmp, the only file whose name contains `correction-1-manager` is the /tmp/c2pre copy. That copy has 242 lines and was written at 17:08:51, so it is not the skeleton. **The skeleton cannot be re-run against.** These claims are therefore relabelled **UNVERIFIED (not re-runnable)**: the 27-line count at :210, the 14:33:58 mtime at :211, "All nine sections read `(pending)`" at :218, and the statement about lines 1-14 and 17-26 at :218. The "name hits: 0" at :209 cannot be re-run on the skeleton either. Run on the current file and on the /tmp/c2pre copy, it gives 0 and 0. The C5 finding at :250 rests on the same partly pasted read, so it carries the same UNVERIFIED (not re-runnable) label for the skeleton's contents.
$ sed -n 560p /tmp/c2w5/${C##*/} | M
- Section 1 (:32-64). Its block is still in (a) C2.1. The conclusion drawn from it is superseded by the revised (a) C2.1: the skeleton claims at (a) :209-211, :213-216, :218 and :250 are no longer UNVERIFIED (not re-runnable). They are now backed by evidence RECOVERED from the session transcript (machine-local, not version-controlled). On that evidence, :209, :210, :211, :213-216, the second sentence of :218, and :250 hold. The first sentence of :218 ("All nine sections") is WRONG: there are 8 sections and 8 `(pending)` lines.
$ sed -n 161p /tmp/c2w5/${D3##*/} | M
(a):281 now quotes :210 with its 6 leading spaces. (b) C2.2 has a new heading at (b):426 and an "Original wording:" line at (b):427 that quotes :238 with its leading `- `. Check of every `:N` quote in an "Original wording:" line against line N of the /tmp/c2pre copy, plus the two unnumbered quotes and the S definition quoted in (c):
$ grep -c "assert " /tmp/vrf-c2/insert.py
3
```

Defect 1 and 2 evidence, pasted into (a) as the new block after (a):314 (run at 18:07:10 local):
```
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
       2
$ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
:40 :46 :33 :58 :08 :51 :210 :33 :58 :211 :218 :218 :209 :250 
$ sed -n "212p;215p" $PA | od -c
0000000                        .   .   .  \n                       .   .
0000020    .  \n                                                        
0000022
$ date "+%Y-%m-%dT%H:%M:%S"
2026-11-11T18:07:10
$ wc -l $B
     684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
$ git ls-files -s -- $B | wc -l
       0
$ git ls-tree HEAD -- $B | wc -l
       0
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | M
/private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
/private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | wc -l
       2
$ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | while read f; do wc -l "$f"; stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" "$f"; done | M
     488 /private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:44:14
     242 /private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
2026-11-11T17:08:51
```

Defect 4 evidence: third negative control, pasted into the (c) Addendum block:
```
$ D=$(mktemp -d); cp $PA "$D/t.md"; printf "x\n" > "$D/noblank.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/noblank.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"
Traceback (most recent call last):
  File "/tmp/vrf-c2/insert.py", line 7, in <module>
    assert seclines[-1] == '' and seclines[-2] == '', 'section must end with one blank line'
AssertionError: section must end with one blank line
rc=1
target unchanged rc=0
$ od -c "$D/noblank.md"
0000000    x  \n                                                        
0000002
```

Defect 3 evidence: range-aware quote check /tmp/c2w5/qcheck2.py, pasted into the (d) Erratum:
```
$ cat /tmp/c2w5/qcheck2.py
# usage: python3 -I /tmp/c2w5/qcheck2.py
# For every "Original wording:" line after the original body of (a) and (b), parse each line
# reference :N or :N-M and the quoted spans (`...` or "...") that directly follow it, separated by ", ".
# Single :N -> span compared with line N of the /tmp/c2pre copy.
# Range :N-M with exactly M-N+1 spans -> spans paired in order with lines N..M.
# Range with any other span count -> each span is MATCH if it equals or is a substring of some line in N..M.
# References followed by no span are listed as no_span. Quoted text with no reference is listed as unnumbered.
import re
F = {'a': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md', 264),
     'b': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md', 241)}
REF = re.compile(r':(\d+)(?:-(\d+))?(?= )')
def span(t, i):
    q = t[i]
    j = t.index(q, i + 1)
    return t[i + 1:j], j + 1
for k, (cur, pre, body) in F.items():
    c = open(cur, encoding='utf-8').read().split('\n'); p = open(pre, encoding='utf-8').read().split('\n')
    for ln, line in enumerate(c[body:], body + 1):
        if not line.startswith('Original wording:'): continue
        t = line[len('Original wording:'):]; i = 0
        while i < len(t):
            m = REF.match(t, i) if (i == 0 or t[i - 1] == ' ') else None
            if m:
                n1 = int(m.group(1)); n2 = int(m.group(2)) if m.group(2) else n1
                i = m.end() + 1; spans = []
                while i < len(t) and t[i] in '`"':
                    s, i = span(t, i); spans.append(s)
                    if t.startswith(', ', i) and i + 2 < len(t) and t[i + 2] in '`"': i += 2
                    else: break
                ref = ':%d' % n1 if n1 == n2 else ':%d-%d' % (n1, n2)
                if not spans:
                    print('(%s):%d %s no_span' % (k, ln, ref)); continue
                rng = list(range(n1, n2 + 1))
                for x, s in enumerate(spans):
                    if len(spans) == len(rng):
                        L = rng[x]; ok = (s == p[L - 1] or s in p[L - 1]); eq = s == p[L - 1]
                        print('(%s):%d %s span%d -> pre:%d %s equal=%s' % (k, ln, ref, x + 1, L, 'MATCH' if ok else 'MISMATCH', eq))
                    else:
                        hits = [L for L in rng if s in p[L - 1]]
                        print('(%s):%d %s span%d -> pre:%s %s' % (k, ln, ref, x + 1, ','.join(map(str, hits)) or '-', 'MATCH' if hits else 'MISMATCH'))
            elif t[i] in '`"':
                s, i = span(t, i); print('(%s):%d unnumbered span len=%d (not checked here)' % (k, ln, len(s)))
            else:
                i += 1
$ python3 -I /tmp/c2w5/qcheck2.py | M
(a):281 :209 span1 -> pre:209 MATCH equal=True
(a):281 :210 span1 -> pre:210 MATCH equal=True
(a):281 :211 span1 -> pre:211 MATCH equal=True
(a):281 :218 span1 -> pre:218 MATCH equal=True
(a):281 :250 no_span
(a):646 :223-225 span1 -> pre:223 MATCH equal=True
(a):646 :223-225 span2 -> pre:224 MATCH equal=True
(a):646 :223-225 span3 -> pre:225 MATCH equal=True
(a):646 :226 span1 -> pre:226 MATCH equal=True
(a):674 :228 span1 -> pre:228 MATCH equal=True
(a):674 :229-241 no_span
(a):674 :240 span1 -> pre:240 MATCH equal=True
(a):674 :242 span1 -> pre:242 MATCH equal=False
(a):674 :238-239 no_span
(a):851 unnumbered span len=142 (not checked here)
(a):856 :257 span1 -> pre:257 MATCH equal=False
(a):856 :261 span1 -> pre:261 MATCH equal=True
(a):856 :262 span1 -> pre:262 MATCH equal=True
(b):258 unnumbered span len=248 (not checked here)
(b):427 :238 span1 -> pre:238 MATCH equal=True
(b):492 :207 span1 -> pre:207 MATCH equal=True
(b):492 :217 span1 -> pre:217 MATCH equal=True
(b):492 :207 no_span
(b):492 :217 no_span
(b):600 :206 span1 -> pre:206 MATCH equal=True
(b):600 :213 span1 -> pre:213 MATCH equal=True
$ python3 -I /tmp/c2w5/qcheck2.py | wc -l
      26
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c " MATCH "
19
$ python3 -I /tmp/c2w5/qcheck2.py | grep -c MISMATCH
0
$ python3 -I /tmp/c2fix/qcheck.py | grep -c ":22[345] "
0
```

## Edits made (file, lines)
- (a) Defects 1 and 2: line 314 rewritten in place (Correction 2 region). It now says the block at :284-313 is first-pass and was taken before (b) was edited, gives the second-fix-pass figures ((b) 684 lines; `find` returns 2 files, 488 and 242 lines, neither 27, so the no-skeleton conclusion stands for /tmp, /private/tmp and git), states that the earlier version labelled :210, :211, the two :218 claims and :250 UNVERIFIED (not re-runnable) and called :209 not re-runnable, and that :213, :214, :216 are the pasted lines and :212, :215 are elision markers. Lines 315-344 inserted: blank, a label line and the fenced evidence block. Lines 1-264 and the final line are unchanged (cmp below).
- (c) Defects 1 and 4, Addendum region only: line 492 wording changed to "Three negative controls show that all three assertions are live" plus a sentence on the third control. 10 lines inserted inside the existing fenced block after line 528, the end of the second control, so they are now 529-538 (the third control and its output; diff shows them as 526a527,533 and 528a536,538 because two of the new lines repeat existing ones). Line 570 (was 560) rewritten: the relabelled claims are :210, :211, :218 and :250 (and :209); :213, :214, :216 are the pasted lines; :212 and :215 are elision markers.
- (d) Defect 3: lines 323-407 appended before the final line as "## Erratum (worker5)": the coverage gap of qcheck.py, the script /tmp/c2w5/qcheck2.py and its full output (26 rows, 19 MATCH, 0 MISMATCH; range spans of :223-225 match lines 223, 224 and 225). No existing line changed.

Full masked diffs of each edited file against its /tmp/c2w5 copy (taken before this pass):
```
$ diff /tmp/c2w5/${f##*/} $f | M | S   # f=2026-11-11-v-rulings-filing-correction-1-worker1.md
314c314,344
< Result of the re-run on current files. The manager report has been rewritten since section 7 was written. It now has 242 lines and mtime 2026-11-11T14:40:46, with 8 lines starting `## `, 0 lines equal to `(pending)` and 0 lines containing `PENDING`. It is untracked and not in the index, so git holds no earlier copy. Under /tmp and /private/tmp, the only file whose name contains `correction-1-manager` is the /tmp/c2pre copy. That copy has 242 lines and was written at 17:08:51, so it is not the skeleton. So there is no copy of the skeleton under /tmp, /private/tmp or in git. That negative covers those three places only. The earlier version of this item stopped there and labelled :209-211, :213-216, :218 and :250 UNVERIFIED (not re-runnable). This version replaces that label with the recovered evidence below.
---
> Result of the re-run above. That block was taken in the first correction-2 pass, before (b) was edited in that pass (it shows (b) with 242 lines, the same as the /tmp/c2pre copy), so its figures are first-pass figures, not current ones. At that time the manager report had been rewritten since section 7 was written. It had 242 lines and mtime 2026-11-11T14:40:46, with 8 lines starting `## `, 0 lines equal to `(pending)` and 0 lines containing `PENDING`. It was untracked and not in the index, so git held no earlier copy. Under /tmp and /private/tmp, the only file whose name contained `correction-1-manager` was the /tmp/c2pre copy. That copy has 242 lines and was written at 17:08:51, so it is not the skeleton. At the time of the second fix pass (worker5, block below, run at 2026-11-11T18:07:10 local), (b) has 684 lines and is still untracked and not in the index, and the same `find` returns 2 files: the /tmp/c2fix copy (488 lines, written 17:44:14) and the /tmp/c2pre copy (242 lines, written 17:08:51). Neither has 27 lines, so neither is the skeleton. So there is no copy of the skeleton under /tmp, /private/tmp or in git. That negative covers those three places only. The earlier version of this item stopped there. Its UNVERIFIED (not re-runnable) label covered :210, the two claims at :218, :211 and :250, and it said that :209 could not be re-run on the skeleton (its line references, apart from time-of-day fragments, are :210, :211, :218, :218, :209 and :250; block below). It did not label :213, :214 or :216, which are the three pasted output lines. :212 and :215 are elision markers (five spaces then `...`, block below), not claims. This version replaces that label with the recovered evidence below.
> 
> Re-run at the time of the second fix pass (worker5), same definitions:
> ```
> $ sed -n 314p /tmp/c2fix/${A##*/} | grep -o "UNVERIFIED" | wc -l
>        2
> $ sed -n 314p /tmp/c2fix/${A##*/} | grep -o ":[0-9][0-9]*" | tr "\n" " "; echo
> :40 :46 :33 :58 :08 :51 :210 :33 :58 :211 :218 :218 :209 :250 
> $ sed -n "212p;215p" $PA | od -c
> 0000000                        .   .   .  \n                       .   .
> 0000020    .  \n                                                        
> 0000022
> $ date "+%Y-%m-%dT%H:%M:%S"
> 2026-11-11T18:07:10
> $ wc -l $B
>      684 docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md
> $ git ls-files -s -- $B | wc -l
>        0
> $ git ls-tree HEAD -- $B | wc -l
>        0
> $ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | M
> /private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
> /private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
> $ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | wc -l
>        2
> $ find /tmp /private/tmp -name "*correction-1-manager*" 2>/dev/null | while read f; do wc -l "$f"; stat -f "%Sm" -t "%Y-%m-%dT%H:%M:%S" "$f"; done | M
>      488 /private/tmp/c2fix/2026-11-11-v-rulings-filing-correction-1-manager.md
> 2026-11-11T17:44:14
>      242 /private/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md
> 2026-11-11T17:08:51
> ```
$ diff /tmp/c2w5/${f##*/} $f | M | S   # f=2026-11-11-v-rulings-filing-correction-2-worker1.md
492c492
< **Step 5 (:16), the insert script and its assertions.** The script that did the insertion is /tmp/vrf-c2/insert.py (the S13 sentence is masked as `<S13>` by `S`, defined in /tmp/c2fix/defs.sh as `S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }`). The original run on (a) and (b) cannot be repeated on the files themselves, because they have been edited since. It was re-run on copies of the /tmp/c2pre files in a mktemp directory, with the generated sections /tmp/vrf-c2/sec_a.md and sec_b.md. Both runs pass every assertion (rc=0). The results are byte-identical to (a) and (b) as this report's step 5 left them, which are the copies in /tmp/c2fix/ taken at the start of the fix pass. Two negative controls show that the assertions are live. A target whose tail is not blank line, S13 line fails with `unexpected tail`. A section that contains the S13 sentence fails the `S not in` assertion and leaves the target unchanged:
---
> **Step 5 (:16), the insert script and its assertions.** The script that did the insertion is /tmp/vrf-c2/insert.py (the S13 sentence is masked as `<S13>` by `S`, defined in /tmp/c2fix/defs.sh as `S() { S13="$(sed -n "s/^S='\(.*\)'\$/\1/p" /tmp/vrf-c2/selfcheck.sh)" perl -pe 's/\Q$ENV{S13}\E/<S13>/g'; }`). The original run on (a) and (b) cannot be repeated on the files themselves, because they have been edited since. It was re-run on copies of the /tmp/c2pre files in a mktemp directory, with the generated sections /tmp/vrf-c2/sec_a.md and sec_b.md. Both runs pass every assertion (rc=0). The results are byte-identical to (a) and (b) as this report's step 5 left them, which are the copies in /tmp/c2fix/ taken at the start of the fix pass. Three negative controls show that all three assertions are live. A target whose tail is not blank line, S13 line fails with `unexpected tail`. A section that contains the S13 sentence fails the `S not in` assertion and leaves the target unchanged. A section that does not end with one blank line (a one-line file, `x` and a newline) fails `section must end with one blank line` and leaves the target unchanged; that third control was added by worker5 in the second fix pass, in a new mktemp directory:
526a527,533
> rc=1
> target unchanged rc=0
> $ D=$(mktemp -d); cp $PA "$D/t.md"; printf "x\n" > "$D/noblank.md"; python3 -I /tmp/vrf-c2/insert.py "$D/t.md" "$D/noblank.md" 2>&1 | S; echo "rc=${PIPESTATUS[0]}"; cmp "$D/t.md" $PA; echo "target unchanged rc=$?"
> Traceback (most recent call last):
>   File "/tmp/vrf-c2/insert.py", line 7, in <module>
>     assert seclines[-1] == '' and seclines[-2] == '', 'section must end with one blank line'
> AssertionError: section must end with one blank line
528a536,538
> $ od -c "$D/noblank.md"
> 0000000    x  \n                                                        
> 0000002
560c570
< - Section 1 (:32-64). Its block is still in (a) C2.1. The conclusion drawn from it is superseded by the revised (a) C2.1: the skeleton claims at (a) :209-211, :213-216, :218 and :250 are no longer UNVERIFIED (not re-runnable). They are now backed by evidence RECOVERED from the session transcript (machine-local, not version-controlled). On that evidence, :209, :210, :211, :213-216, the second sentence of :218, and :250 hold. The first sentence of :218 ("All nine sections") is WRONG: there are 8 sections and 8 `(pending)` lines.
---
> - Section 1 (:32-64). Its block is still in (a) C2.1. The conclusion drawn from it is superseded by the revised (a) C2.1: the skeleton claims at (a) :210, :211, :218 and :250 are no longer UNVERIFIED (not re-runnable), and :209 is no longer only "not re-runnable on the skeleton". (a) :213, :214 and :216 are the three pasted output lines; :212 and :215 are elision markers (five spaces then `...`), not claims. The relabelled claims are now backed by evidence RECOVERED from the session transcript (machine-local, not version-controlled). On that evidence, :209, :210, :211, the pasted lines :213, :214 and :216, the second sentence of :218, and :250 hold. The first sentence of :218 ("All nine sections") is WRONG: there are 8 sections and 8 `(pending)` lines.
$ diff /tmp/c2w5/${f##*/} $f | M | S   # f=2026-11-11-v-rulings-filing-correction-2-worker3.md
322a323,407
> ## Erratum (worker5)
> Added by worker5 in the second fix pass of unit 2026-11-11-v-rulings-filing-correction-2. No line above was changed. Defect 4 above says it checks "every `:N` quote" in an "Original wording:" line. That overstates the coverage of /tmp/c2fix/qcheck.py. Its pattern `:(\d+) ` needs a space right after the number, so a range reference such as `:223-225` is skipped, and the three quotes after `:223-225` in (a):616 were not checked by it (its output has 0 rows for :223, :224 or :225; last command below). /tmp/c2w5/qcheck2.py, below, also parses `:N-M` references. It pairs the spans in order with lines N to M when the counts agree, lists a reference with no quoted span as no_span, and lists quoted text with no line reference as unnumbered; the two unnumbered quotes, (a):851 (cited above as (a):821) and (b):258, are the ones checked by the `python3 -I -c` command in Defect 4 above. Result: 26 rows, 19 spans MATCH and 0 MISMATCH. The three (a):616 range spans equal lines 223, 224 and 225 of the /tmp/c2pre copy. The two `equal=False` rows are the same partial quotes as above ((a):644 :242 and (a):826 :257). The rows give (a) line numbers after worker5's edit, which inserted 30 lines after (a):314, so (a):616, :644, :821 and :826 cited above appear in the rows as (a):646, :674, :851 and :856. (b) line numbers are unchanged by worker5.
> ```
> $ cat /tmp/c2w5/qcheck2.py
> # usage: python3 -I /tmp/c2w5/qcheck2.py
> # For every "Original wording:" line after the original body of (a) and (b), parse each line
> # reference :N or :N-M and the quoted spans (`...` or "...") that directly follow it, separated by ", ".
> # Single :N -> span compared with line N of the /tmp/c2pre copy.
> # Range :N-M with exactly M-N+1 spans -> spans paired in order with lines N..M.
> # Range with any other span count -> each span is MATCH if it equals or is a substring of some line in N..M.
> # References followed by no span are listed as no_span. Quoted text with no reference is listed as unnumbered.
> import re
> F = {'a': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-worker1.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-worker1.md', 264),
>      'b': ('docs/reports/2026-11-11-v-rulings-filing-correction-1-manager.md', '/tmp/c2pre/2026-11-11-v-rulings-filing-correction-1-manager.md', 241)}
> REF = re.compile(r':(\d+)(?:-(\d+))?(?= )')
> def span(t, i):
>     q = t[i]
>     j = t.index(q, i + 1)
>     return t[i + 1:j], j + 1
> for k, (cur, pre, body) in F.items():
>     c = open(cur, encoding='utf-8').read().split('\n'); p = open(pre, encoding='utf-8').read().split('\n')
>     for ln, line in enumerate(c[body:], body + 1):
>         if not line.startswith('Original wording:'): continue
>         t = line[len('Original wording:'):]; i = 0
>         while i < len(t):
>             m = REF.match(t, i) if (i == 0 or t[i - 1] == ' ') else None
>             if m:
>                 n1 = int(m.group(1)); n2 = int(m.group(2)) if m.group(2) else n1
>                 i = m.end() + 1; spans = []
>                 while i < len(t) and t[i] in '`"':
>                     s, i = span(t, i); spans.append(s)
>                     if t.startswith(', ', i) and i + 2 < len(t) and t[i + 2] in '`"': i += 2
>                     else: break
>                 ref = ':%d' % n1 if n1 == n2 else ':%d-%d' % (n1, n2)
>                 if not spans:
>                     print('(%s):%d %s no_span' % (k, ln, ref)); continue
>                 rng = list(range(n1, n2 + 1))
>                 for x, s in enumerate(spans):
>                     if len(spans) == len(rng):
>                         L = rng[x]; ok = (s == p[L - 1] or s in p[L - 1]); eq = s == p[L - 1]
>                         print('(%s):%d %s span%d -> pre:%d %s equal=%s' % (k, ln, ref, x + 1, L, 'MATCH' if ok else 'MISMATCH', eq))
>                     else:
>                         hits = [L for L in rng if s in p[L - 1]]
>                         print('(%s):%d %s span%d -> pre:%s %s' % (k, ln, ref, x + 1, ','.join(map(str, hits)) or '-', 'MATCH' if hits else 'MISMATCH'))
>             elif t[i] in '`"':
>                 s, i = span(t, i); print('(%s):%d unnumbered span len=%d (not checked here)' % (k, ln, len(s)))
>             else:
>                 i += 1
> $ python3 -I /tmp/c2w5/qcheck2.py | M
> (a):281 :209 span1 -> pre:209 MATCH equal=True
> (a):281 :210 span1 -> pre:210 MATCH equal=True
> (a):281 :211 span1 -> pre:211 MATCH equal=True
> (a):281 :218 span1 -> pre:218 MATCH equal=True
> (a):281 :250 no_span
> (a):646 :223-225 span1 -> pre:223 MATCH equal=True
> (a):646 :223-225 span2 -> pre:224 MATCH equal=True
> (a):646 :223-225 span3 -> pre:225 MATCH equal=True
> (a):646 :226 span1 -> pre:226 MATCH equal=True
> (a):674 :228 span1 -> pre:228 MATCH equal=True
> (a):674 :229-241 no_span
> (a):674 :240 span1 -> pre:240 MATCH equal=True
> (a):674 :242 span1 -> pre:242 MATCH equal=False
> (a):674 :238-239 no_span
> (a):851 unnumbered span len=142 (not checked here)
> (a):856 :257 span1 -> pre:257 MATCH equal=False
> (a):856 :261 span1 -> pre:261 MATCH equal=True
> (a):856 :262 span1 -> pre:262 MATCH equal=True
> (b):258 unnumbered span len=248 (not checked here)
> (b):427 :238 span1 -> pre:238 MATCH equal=True
> (b):492 :207 span1 -> pre:207 MATCH equal=True
> (b):492 :217 span1 -> pre:217 MATCH equal=True
> (b):492 :207 no_span
> (b):492 :217 no_span
> (b):600 :206 span1 -> pre:206 MATCH equal=True
> (b):600 :213 span1 -> pre:213 MATCH equal=True
> $ python3 -I /tmp/c2w5/qcheck2.py | wc -l
>       26
> $ python3 -I /tmp/c2w5/qcheck2.py | grep -c " MATCH "
> 19
> $ python3 -I /tmp/c2w5/qcheck2.py | grep -c MISMATCH
> 0
> $ python3 -I /tmp/c2fix/qcheck.py | grep -c ":22[345] "
> 0
> ```
> 
```

## Self-check
Run on the report before this block was pasted; pasting it changes only the `lines=` value for the report (the block contains no name and the S13 sentence is masked).
```
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
$ tail -n 1 /tmp/c2w5/${D3##*/} | S; tail -n 1 $D3 | S
<S13>
<S13>
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
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md: name_ci=0 V1_HIT_lines=0 S13_containing=1 S13_standalone=1 at=[308] last_nonblank_line=308 last_nonblank_is_S13=YES lines=308
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
docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md:0
$ git diff --cached --name-only -- $A $C $D3 $W5
```

## Result
PASS: all four MINOR defects fixed as above. (a) still differs from /tmp/c2pre by one `a` hunk only, with 0 `<` lines. (c) has 0 `<` lines against /tmp/c2fix; its added lines are 451-490 and 492-576, the blank line before the Addendum heading (452) and the Addendum itself. (d) has 0 `<` lines against its /tmp/c2w5 copy. Not done: no MANIFEST row for this report (MANIFEST is outside this brief). Observation, not fixed: (b) has 684 lines now, against 488 in the /tmp/c2fix copy, so another worker is editing (b) in parallel; this pass did not touch it.

## Manager note (correction-2 manager, after the worker 6 check)
Worker 6 (docs/reports/2026-11-11-v-rulings-filing-correction-2-worker6.md, Findings 1, 2 and 4) found that the Self-check values above are stale and that `$C`, `$D3` and `$W5` are not defined in the files named at :4. The definitions come from /tmp/c2w5/verify.sh:
```
$ grep -nE "^(C|D3|W5)=" /tmp/c2w5/verify.sh
3:C=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker1.md
4:D3=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker3.md
5:W5=docs/reports/2026-11-11-v-rulings-filing-correction-2-worker5.md
$ grep -nE "^(C|D3|W5)=" /tmp/c2w5/verify.sh | wc -l
       3
```
The `lines=`, `at=` and `last_nonblank_line=` values for this report in the Self-check block above were taken before that block and this note were added, so they are stale. The key-path count of 0 for this report is also stale: the grep now matches its own pattern text, pasted in this report. The current values for this report come from a re-run after this note was inserted, and they are in docs/reports/2026-11-11-v-rulings-filing-correction-2-manager.md, Verification evidence.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
