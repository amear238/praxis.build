# 2026-11-10 f4-grading, correction 1, adversarial worker 1

## Task

Attack Correction 1 of `docs/reports/2026-11-10-f4-grading-manager.md` (:460 to the end) and, in `docs/reports/2026-11-10-f4-grading-correction-1-manager.md`, block C1-V0 and the table "Finding, cure, where". Question: are audit findings 1, 2, 3 and 7 cured; is there a new described-not-pasted block; does the section change a label or grade F4; personal data; banned strings; S13. Read-only except this report. HEAD `d30ab4d`, 2026-11-10.

## Mode

ADVERSARIAL

## Criterion

Rubric S1 (specs/SPEC_RUBRIC.md :124), S2 (:125), S13 (:136).

## Method

I pulled every fenced block out of manager :460–726 and fed each block's `$ ` lines through the manager's own runner `/tmp/f4c1/run.sh`, then diffed the result against what was pasted. Then I ran targeted probes. All commands were run from the repo root. Outputs below are pasted unedited, except that, where the command line shows it, they went through the `sed` path mask and `perl -p /tmp/f4c1/redact.pl`.

~~~text
$ mkdir -p /tmp/w1 && cd /Volumes/Sensidine/Praxis.build && M=docs/reports/2026-11-10-f4-grading-manager.md && sed -n '460,726p' $M | awk 'BEGIN{n=0} /^~~~text$/{n++; f=1; next} /^~~~$/{f=0; next} f{print > ("/tmp/w1/exp" n ".txt"); if (/^\$ /) {sub(/^\$ /,""); print > ("/tmp/w1/cmd" n ".txt")}}' && ls /tmp/w1 && cat /tmp/f4c1/run.sh | head -20 && for n in 1 2 3 4 5 6; do bash /tmp/f4c1/run.sh /tmp/w1/cmd$n.txt > /tmp/w1/got$n.txt 2>&1; echo "== block $n: exp=$(wc -l < /tmp/w1/exp$n.txt) got=$(wc -l < /tmp/w1/got$n.txt)"; diff /tmp/w1/exp$n.txt /tmp/w1/got$n.txt | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl; done
cmd1.txt
cmd2.txt
cmd3.txt
cmd4.txt
cmd5.txt
cmd6.txt
exp1.txt
exp2.txt
exp3.txt
exp4.txt
exp5.txt
exp6.txt
#!/bin/bash
# prints each command line with a "$ " prefix, then runs that exact line (eval) in one bash shell
cd /Volumes/Sensidine/Praxis.build || exit 1
while IFS= read -r line <&3; do
  [ -z "$line" ] && continue
  printf '$ %s\n' "$line"
  eval "$line" 2>&1
done 3< "$1"
== block 1: exp=      27 got=      27
== block 2: exp=      30 got=      30
== block 3: exp=      48 got=      48
== block 4: exp=      66 got=      66
== block 5: exp=      14 got=      14
2c2
<      460
---
>      726
== block 6: exp=      25 got=      26
25a26
> 719:427:$ grep -c -E "F4 (passes|is closed|is satisfied)|satisfies F4" manager report
~~~

Blocks 1 to 6 are C1-V2, C1-V7, C1-V3, C1-V40, C1-T and C1-V11, in that order. Blocks 1 to 4 reproduce byte for byte. Blocks 5 and 6 differ only as Findings 4 and 5 below describe.

## Findings

### 1. BLOCKING. manager :590 (C1-V3 Reading). The cause given for the extra line is false, and the command behind V3's eleven `N:` lines is still not shown (audit finding 2 not fully cured; S1, S2)

The claim: "These include all eleven of V3's; 716 is extra because the re-run uses `-i`." V3's eleven lines (manager :311–321) are 28, 29, 34, 35, 36, 37, 44, 45, 46, 636 and 724. They include 46 and do not include 716. I ran the same `grep -n` without `-i`:

~~~text
$ git show HEAD:$E | grep -n -e 'Algo trading is now permitted' -e 'simulated-funded and live account stages' -e '^| Sender |' -e '^| Timestamp |' -e '^| Respondent |' -e '^| Policy article |' -e 'No high-frequency trading' -e 'exploit sim-environment fill' -e 'live automation must follow CME' | cut -d: -f1 | tr '\n' ' '
28 29 34 35 36 37 44 45 636 724 
~~~

(`E=docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`, set at the start of the same shell line.) Without `-i` the result is 10 lines: line 46 drops out along with 716, because the pattern `live automation` is lower case and :46 reads "Live automation". So V3's eleven lines come from neither the `-i` form nor the non-`-i` form of this command. The pasted re-run is a 12-line superset that does contain all eleven, so the content of those lines is backed. But the sentence "The `grep -n` command is the command for the `N:` lines that V3 shows without one" is not true as written, and the stated reason for the difference is refuted.

Proposed fix: delete the "because the re-run uses `-i`" clause. Say that the command that produced V3's eleven lines is not recovered, and that the re-run's 12 lines are a superset (716 and 46 both depend on `-i`). Or find, run and paste a command that gives exactly the eleven.

### 2. MINOR. manager :684 (C1-T Reading) and correction-1 manager :111 (table row 7). The first-name list leaves out :412

C1-T reads "Everywhere else, at lines 47, 55, 154, 188, 220, 290, 327, 328 and 329, this report uses the trader's first name". That reads as a complete list, but it came from a case-sensitive `grep -w Amear`. A case-insensitive search finds one more line:

~~~text
$ sed -n '1,459p' $M | grep -n -i -w amear | cut -d: -f1 | tr '\n' ' '; echo; sed -n '1,459p' $M | grep -n -i -w amear | grep -v -w Amear | perl -p /tmp/f4c1/redact.pl | cut -c1-200
47 55 154 188 220 290 327 328 329 412 
412:431:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
~~~

The narrowed claim stays harmless, since the first name is not withheld, but the list is incomplete. Fix: re-run with `-i` and add :412 (lower case) in both places.

### 3. MINOR (open, conditional). Finding 1 for V11 :421 and :437 rests on a placeholder

The original V11 has four described lines: :421 (per-file loop), :427, :429 and :437 (index check). C1-V11 re-runs :427 and :429. The cure for :421 and :437 is "in the correction-1 manager report, section 'Final checks'", and that section is still "Pending". Under the brief this is not a defect. But until that section is filled, audit finding 1 cannot be marked cured for :421 and :437.

### 4. MINOR. manager :718–722 (C1-V11, last command). The pasted output no longer holds after insertion

A re-run of `grep -n -E 'F4 (passes|is closed|is satisfied)|satisfie[s] F4' docs/reports/2026-11-10-f4-grading-manager.md | cut -c1-90` now also returns `719:427:$ grep -c -E ...` (see the block 6 diff in Method: the extra line is `> 719:427:$ grep -c -E "F4 (passes|is closed|is satisfied)|satisfies F4" manager report`). The Reading at :722, "finds one line of this file, :427", was true before the insertion and is false now. :719 is only a quote of :427, so no sentence of the report matches, but the pasted output is now stale. The same applies to C1-T's `wc -l` (pasted 460, now 726; the Reading says so openly). Fix: state that both outputs are pre-insertion captures, or add that a post-insertion run also hits :719, which is the quote of :427.

### 5. MINOR. manager :250 (original V2). A second `<transcript>` placeholder command is not re-run as such

`$ git show HEAD:<transcript> | grep -n "No timestamp\|not been checked as a sending domain"` (:250) has the same placeholder as the :230 line the audit named. C1-V2 shows transcript :64 and :65 through `sed -n '...;64,65p'` but does not re-run this `grep -n`. The content is covered; the command form is not. Fix: add the literal `git show "HEAD:$T" | grep -n ...` line to C1-V2.

### 6. MINOR. Claims in the correction with no pasted output in the correction

- C1-T :684 says the HEAD sources carry the first name "as the last two commands show" for "voice-session-notes-3 :44". The last two commands cover HANDOFF.md :764/:784 and DECISIONS.md :539 only. My check agrees with the claim (`git show HEAD:docs/reports/2026-11-01-voice-session-notes-3.md | sed -n 44p | grep -c -i -w amear` gives `1`), but the artifact does not show it.
- C1-W :688 gives 0 / 496 / 496 / 634 with no block in this file. It points to worker 2's C1-W7, which exists (`grep -n 'C1-W7\|C1-W8' docs/reports/2026-11-10-f4-grading-worker2.md` gives `281:### C1-W7. Block 7 (F4 and A15 counts): one count disagrees` and `304:### C1-W8. ...`). My re-run agrees: `echo "E=$(git grep -E '\bF4\b' HEAD | wc -l) w=$(git grep -w F4 HEAD | wc -l) iw=$(git grep -i -w F4 HEAD | wc -l) P=$(git grep -P '\bF4\b' HEAD | wc -l)"` gives `E=       0 w=     496 iw=     634 P=     496`. The sentence "No label rests on either figure" has no output behind it.
- C1-V40 :663 says "The working-tree search ... finds 'Two follow-ups' only in reports that quote the same preview". Only a file list is pasted. One of those files, `docs/reports/2026-11-10-f4-grading-worker4.md`, has "Two follow-ups" only as a search term, not as a quote of the preview:

~~~text
$ comm -23 <(grep -rIl -F "Two follow-ups" --exclude-dir=.git . | sort) <(grep -rIl -F "Two follow-ups so I can be sure" --exclude-dir=.git . | sort) | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/2026-10-28-f4-[name]-reply-worker5-fix.md
docs/reports/2026-11-10-f4-grading-worker4.md
~~~

For worker 4, `grep -h -o '.\{0,60\}Two follow-ups.\{0,60\}' docs/reports/2026-11-10-f4-grading-worker4.md | head -3 | perl -p /tmp/f4c1/redact.pl` printed search-term lines: "I tried to break it with `git grep` at HEAD for "Two follow-ups" and "Does this specific"", then a `$ git grep -n -i -F -e "Two follow-ups" ...` command, then "Agrees. "Two follow-ups" and "Does this specific" hit only the 2026-08-07 report". The worker5-fix file does quote the preview, wrapped at "so I". The :40 sentence itself is scoped to HEAD, so this affects only the side sentence.

Fix for all three: paste the supporting command, or drop or narrow the sentence.

### 7. MINOR. correction-1 manager :3 and :26. The start time and index state cite C1-V0, which does not show them

:3 reads "Started. 2026-11-10T17:38:16Z (`date -u`, block C1-V0)", but the `date -u` output in C1-V0 (:40) is `Tue Nov 10 17:44:58 UTC 2026`. No pasted output shows 17:38:16Z (`grep -n '17:38' docs/reports/2026-11-10-f4-grading-correction-1-manager.md` gives only :3 and :26). :26 says "index holding one path (C1-V0, Final checks)", and C1-V0 has no index command. Fix: cite the 17:44:58 output, or paste the 17:38 run and an index listing.

## Checks that found nothing

Audit findings 1 (V2, V7, V3 lines), 2 (rc, 779) and 3 (:40 search): every pasted command in C1-V2, C1-V7, C1-V3 and C1-V40 reproduces byte for byte (blocks 1 to 4 in Method). The `$?` cure for the rc line holds. The V7 counts equal the original table (:254–269). The positive controls for "platform" and "NT8", which the C1-V3 control leaves out, also hit: `echo "platform=$(git show HEAD:$E | grep -c -i platform) NT8=$(git show HEAD:$E | grep -c -i NT8)"` gives `platform=4 NT8=9`. The 2026-08-07 :642 preview ends "is f" (`git show HEAD:$E | sed -n 642p | grep -c 'is f$'` gives `1`). The :582 hit is "email draft" (`... sed -n 582p | grep -c -i -F 'Subject:'` gives `0`; `... grep -c -i -F 'email draft'` gives `1`). The DECISION_LOG strings in C1-V11 sit at :435 and :179 (`git show HEAD:DECISION_LOG.md | grep -n -F '" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.' | cut -d: -f1` gives `435`; the TWO RULINGS string gives `179`). So the original's "DL:435 tail" line is covered.

C1-V0 rebuilt independently into /tmp/w1:

~~~text
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); { git show "HEAD:$T" | sed -n 15p | awk '{print $2}'; git show "HEAD:$T" | sed -n 16p | awk '{print $2}'; git show "HEAD:$T" | sed -n 25p | grep -o 'My name is [A-Za-z]*' | awk '{print $4}'; git show "HEAD:$T" | sed -n 36p | cut -d- -f1; git show HEAD:DECISION_LOG.md | sed -n 177p | grep -oE '[0-9a-f]{16}' | sort -u; } > /tmp/w1/pat.txt; cmp /tmp/w1/pat.txt /tmp/f4c1-pat.txt && echo "pat file reproduces"; awk '{print NR, length($0)}' /tmp/w1/pat.txt; git show "HEAD:$T" | sed -n '1p;18p' | grep -c -i -w -F -f <(sed -n 4p /tmp/f4c1-pat.txt); git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 36p | grep -c -i -w -F -f <(sed -n 2p /tmp/f4c1-pat.txt); git show HEAD:specs/SPEC_RUBRIC.md | sed -n 136p | grep -o '"Fills are optimistic[^"]*"' | tr -d '"' | cmp - /tmp/f4c1-s13.txt && echo "s13 file reproduces"; printf '%s\n' "ver""dict" "COMMIT-""INDEX" "COMMIT-DIFF-""SHA256" | cmp - /tmp/f4c1-bw.txt && echo "bw file reproduces"; git grep -c -i -w -F -f /tmp/f4c1-lp.txt HEAD -- DECISION_LOG.md HANDOFF.md | wc -l
pat file reproduces
1 10
2 5
3 7
4 4
5 16
2
1
s13 file reproduces
bw file reproduces
       1
~~~

Check C (labels, coverage, grade): the element table labels at :100–128 are COVERED-EXPLICITLY, COVERED-BY-INFERENCE and NOT ADDRESSED. Scanning the correction for label tokens found only two hits:

~~~text
$ sed -n '460,726p' $M | grep -n -o -w -E 'COVERED|NOT COVERED|PARTIAL|SILENT|NAMED|INFERRED|ADDRESSED|NOT ADDRESSED|DOES NOT ADDRESS|CONTRADICTED' | sort | uniq -c
   1 116:DOES NOT ADDRESS
   1 257:DOES NOT ADDRESS
~~~

Both hits (file :575 and :716) are lines quoted from the 2026-08-07 report's own §3.2 row, not labels of this report. No row is relabelled, and F4 is not graded ("F4 is not graded here; it stays FROZEN", :462).

Check B, placeholder scan of the correction:

~~~text
$ sed -n '460,726p' $M | grep '^\$ ' | grep -c -e '\.\.\.' -e '…' -e '<[a-zA-Z]'
0
$ sed -n '460,726p' $M | grep -c -e '\.\.\.' -e '…'
0
~~~

Checks D and E and S13 on the two artifact files:

~~~text
$ for f in $M $C; do printf '%s pat=%s email=%s bw=%s s13=%s last-is-s13=%s\n' "$f" "$(grep -c -i -w -F -f /tmp/f4c1-pat.txt $f)" "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $f)" "$(grep -c -i -F -f /tmp/f4c1-bw.txt $f)" "$(grep -c -x -F -f /tmp/f4c1-s13.txt $f)" "$(tail -1 $f | cmp -s - /tmp/f4c1-s13.txt && echo yes || echo no)"; done; grep -c -i -F -f /tmp/f4c1-lp.txt $M $C; grep -c -E '\b[0-9a-f]{16}\b' $M $C; echo "--- S13 substring anywhere (not only whole-line)"; grep -c -F "$(cat /tmp/f4c1-s13.txt)" $M $C
docs/reports/2026-11-10-f4-grading-manager.md pat=0 email=0 bw=0 s13=1 last-is-s13=yes
docs/reports/2026-11-10-f4-grading-correction-1-manager.md pat=0 email=0 bw=0 s13=1 last-is-s13=yes
docs/reports/2026-11-10-f4-grading-correction-1-manager.md:0
docs/reports/2026-11-10-f4-grading-manager.md:0
docs/reports/2026-11-10-f4-grading-correction-1-manager.md:0
docs/reports/2026-11-10-f4-grading-manager.md:0
--- S13 substring anywhere (not only whole-line)
docs/reports/2026-11-10-f4-grading-correction-1-manager.md:1
docs/reports/2026-11-10-f4-grading-manager.md:1
~~~

(`M` and `C` are the manager and correction-1 manager report paths.)

Correction-1 manager table line ranges: the manager headings fall at 466, 500, 537, 592, 665, 686 and 690 (`grep -n '^###\|^## ' $M`), and the table's ranges :466–499, :500–536, :537–591, :592–664, :665–685, :686–689 and :690–725 match them.

Not verifiable: "lines 1 to 459 are unchanged". The file is untracked, and I found no baseline hash for it (`grep -l -i 'sha256\|shasum' docs/reports/2026-11-10-f4-grading*.md` printed nothing). The lines the audit cited (:8, :40, :152, :199, :234, :393, :394, :400, :402) read as the audit and the correction describe them.

## Files staged

None.

## Result

FAIL: one BLOCKING finding (1) and six MINOR findings (2 to 7).
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
