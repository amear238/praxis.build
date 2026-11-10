# 2026-11-10 f4-grading, correction 1, adversarial worker 2

## Task
Attack the Correction 1 sections of worker2 (:148 on), worker3 (:153 on), worker4 (:85 on), manifest-manager (:98 on), and block C1-V0 of the correction-1 manager report, against audit findings 4, 5 and 6, and checks A to E of the brief. Read-only on the artifact.

## Mode
ADVERSARIAL. HEAD d30ab4d. All evidence below was produced by passing one-line command files through the manager's runner `/tmp/f4c1/run.sh` (it prints `$ ` plus the line, then evals that exact line), so every `$ ` line is the literal command and the text under it is its unedited output. Command files and captures: `/tmp/f4c1-w2adv/{E1..E7,N1,N2}.txt` and `out-*.txt`.

## Criterion
specs/SPEC_RUBRIC.md S1 (:124), S2 (:125), S13 (:136).

## Findings

### 1. BLOCKING. Audit finding 5 is not cured: several "Checks that found nothing" items in workers 3 and 4 are neither re-run nor listed as not re-run
- Where: worker4 :72, :73, :74, :75 (CONTRADICTED paragraph, Conditions paragraph, Grading check, Rows 4 and 14b); worker4 "Not re-run" :188 to :190 covers only findings 1 to 4 and the process log. worker3 :143 (A. Rows 1, 5, 6, 7, 9 to 12 and the Account-type table), :144 (A. Sentences that grade F4: "None found"), and the :141 classifications of DECISIONS :285, a20 report :487 and kit gap list :28; worker3 "Not re-run" :285 to :288 covers only findings 1 to 9 and item D. The correction-1 manager table at :109 says "Every probe under "Checks that found nothing" re-run by the manager and labelled as such", which these items contradict. (Worker 4's Conditions item cites P :85 to :90; C1-Y3 prints only :87 and :88 of that range.)
- Evidence (E1):
~~~text
$ grep -n -o -E '^- \*\*[^*]+\*\*' docs/reports/2026-11-10-f4-grading-worker4.md | sed -n '19,28p'
66:- **Ledger quotes in the Inquiry table.**
67:- **Outgoing preview.**
68:- **Opening bold sentence of "Inquiry as sent".**
69:- **Published-page quotes.**
70:- **R2 quotes in rows 2, 4 and 13.**
71:- **"Read as a whole" row list.**
72:- **CONTRADICTED paragraph.**
73:- **Conditions paragraph.**
74:- **Grading check.**
75:- **Rows 4 and 14b.**
$ for s in 'CONTRADICTED paragraph' 'Conditions paragraph' 'Grading check' 'Rows 4 and 14b' ':85' ':89' ':90'; do printf '%-24s %s\n' "$s" "$(sed -n '85,191p' docs/reports/2026-11-10-f4-grading-worker4.md | grep -c -F -e "$s")"; done
CONTRADICTED paragraph   0
Conditions paragraph     0
Grading check            0
Rows 4 and 14b           0
:85                      0
:89                      0
:90                      0
$ sed -n '188,190p' docs/reports/2026-11-10-f4-grading-worker4.md | cut -c1-150
### Not re-run

The evidence under findings 1 to 4 quotes the manager draft as it stood when worker 4 read it, with that draft's line numbers (for example :111, :99, 
$ grep -n -o -E '^- \*\*[^*]+\*\*' docs/reports/2026-11-10-f4-grading-worker3.md | sed -n '9,10p'
143:- **A. Rows 1, 5, 6, 7, 9, 10, 11, 12 and the Account-type scope table.**
144:- **A. Sentences that grade F4.**
$ sed -n 141p docs/reports/2026-11-10-f4-grading-worker3.md | grep -o -E 'DECISIONS :285|a20 report :487|kit gap list :28'
DECISIONS :285
a20 report :487
kit gap list :28
$ for s in 'Rows 1, 5' 'Account-type' 'Sentences that grade' 'grade F4' ':285' ':487' 'kit gap'; do printf '%-24s %s\n' "$s" "$(sed -n '153,289p' docs/reports/2026-11-10-f4-grading-worker3.md | grep -c -F -e "$s")"; done
Rows 1, 5                0
Account-type             0
Sentences that grade     0
grade F4                 0
:285                     0
:487                     0
kit gap                  0
$ sed -n '285,288p' docs/reports/2026-11-10-f4-grading-worker3.md | cut -c1-100
### Not re-run

- The evidence blocks under findings 1 to 9 quote the manager draft as it stood when worker 3 read i
- "D. Personal data, the three reports": the per-file counts for every report of this unit are re-ru
$ sed -n 109p docs/reports/2026-11-10-f4-grading-correction-1-manager.md | grep -o 'Every probe under "Checks that found nothing" re-run by the manager and labelled as such'
Every probe under "Checks that found nothing" re-run by the manager and labelled as such
~~~
- Proposed fix: for each item, either paste a re-run (for example the current manager table rows and the CONTRADICTED and Conditions paragraphs with the cited source lines) or add it by name to the section's "Not re-run" list with the reason; then correct the :109 table cell.

### 2. BLOCKING. Worker 2, C1-W5 claims a span is pasted in C1-W1 that is not there
- Where: worker2 :262 ("The HANDOFF.md :784 span is in C1-W1 above"). C1-W1's command cuts every line at 140 characters (:161), so the HANDOFF :784 line ends at "(human rep, written)". The two spans the original relies on, "naming the actual architecture, and asking the policy's effective date" (Q1 answer :100) and "F4 STAYS FROZEN" (Block 8 :127), are in HEAD HANDOFF :784 but appear nowhere in the Correction 1 section. The claim is true at HEAD; the cross-reference that says it is pasted is false (S1).
- Evidence (E2):
~~~text
$ sed -n 262p docs/reports/2026-11-10-f4-grading-worker2.md | grep -o 'The HANDOFF.md :784 span is in C1-W1 above'
The HANDOFF.md :784 span is in C1-W1 above
$ sed -n 161p docs/reports/2026-11-10-f4-grading-worker2.md | grep -o 'cut -c1-140'
cut -c1-140
$ git show HEAD:HANDOFF.md | sed -n 784p | grep -c -F 'naming the actual architecture, and asking the policy'
1
$ git show HEAD:HANDOFF.md | sed -n 784p | grep -c -F 'F4 STAYS FROZEN'
1
$ sed -n '148,341p' docs/reports/2026-11-10-f4-grading-worker2.md | grep -c -F 'naming the actual architecture'
0
$ sed -n '148,341p' docs/reports/2026-11-10-f4-grading-worker2.md | grep -c -F 'STAYS FROZEN'
0
$ sed -n 100p docs/reports/2026-11-10-f4-grading-worker2.md | grep -o 'HANDOFF.md:784 describes it as "naming the actual architecture'
HANDOFF.md:784 describes it as "naming the actual architecture
$ sed -n 127p docs/reports/2026-11-10-f4-grading-worker2.md | grep -o 'HANDOFF.md:784 | '
HANDOFF.md:784 | 
~~~
- Proposed fix: add `git show HEAD:HANDOFF.md | sed -n 784p | grep -o -e 'naming the actual architecture, and asking the policy.s effective date' -e 'F4 STAYS FROZEN'` with its output to C1-W5, and delete or correct the :262 sentence.

### 3. MINOR. Worker 3, C1-X2 says worker 3 did not record its filter, then re-runs a narrower one and calls the result agreement
- Where: worker3 :217. Worker 3's own :141 records its word list (eight words). The manager's regex uses four of them and gets 6 hits. With worker 3's eight words the same regex gets 12 hits, including reply-filing :348 and STATUS :143, which :217 explains away as not being hits. None of the six extra hits, in the excerpts below, states that F4 is closed in its own words, so worker 3's conclusion survives; the stated reason for the :348 difference is wrong. (In the :232 excerpt the source's angle brackets are turned into square brackets by the `tr` in the command; :232 is a search pattern inside a command in that HEAD report. The :348 excerpt does not show the sentence's first word, so its reading is limited to the excerpt.)
- Evidence (E3):
~~~text
$ sed -n 141p docs/reports/2026-11-10-f4-grading-worker3.md | grep -o 'filtered for [a-z/]*'
filtered for closed/satisfied/cleared/unfrozen/resolved/passed/met/done
$ sed -n 217p docs/reports/2026-11-10-f4-grading-worker3.md | grep -o -e 'Worker 3 did not record its status-word filter' -e 'closed, satisfied, cleared or unfrozen' -e 'is not among this regex.s hits'
Worker 3 did not record its status-word filter
closed, satisfied, cleared or unfrozen
is not among this regex's hits
$ git grep -n -i -P '\bF4\b[^.|;]{0,25}\b(closed|satisfied|cleared|unfrozen)\b' HEAD | wc -l
       6
$ git grep -n -i -P '\bF4\b[^.|;]{0,25}\b(closed|satisfied|cleared|unfrozen|resolved|passed|met|done)\b' HEAD | cut -d: -f1-3 | sed 's/-[a-z]*-reply/-[name]-reply/'
HEAD:DECISION_LOG.md:801
HEAD:STATUS.md:143
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:140
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:533
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:232
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:348
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:367
HEAD:docs/reports/2026-11-04-status-refresh-manager.md:257
HEAD:docs/reports/2026-11-06-status-handoff-refresh-manager.md:148
HEAD:docs/reports/2026-11-06-status-handoff-refresh-manager.md:194
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:68
HEAD:docs/reports/2026-11-10-f1-f2-proposal-manager.md:36
$ RF=$(git ls-tree -r --name-only HEAD docs/reports/ | grep -- '-f4-[a-z]*-reply-filing.md$'); for x in STATUS.md:143 "$RF:232" "$RF:348" docs/reports/2026-11-04-status-refresh-manager.md:257 docs/reports/2026-11-06-status-handoff-refresh-manager.md:148 docs/reports/2026-11-06-status-handoff-refresh-manager.md:194; do f=${x%:*}; n=${x##*:}; printf '%s | ' "$(echo "$x" | sed 's/-[a-z]*-reply/-[name]-reply/')"; git show "HEAD:$f" | sed -n "${n}p" | perl -ne 'print "$1\n" if /(.{0,50}\bF4\b[^.|;]{0,25}\b(?:closed|satisfied|cleared|unfrozen|resolved|passed|met|done)\b.{0,15})/i' | tr '<>' '[]' | perl -p /tmp/f4c1/redact.pl; done
STATUS.md:143 | /SPEC_RUBRIC.md` F1 :17-28, F2 :30-43, F3 :45-57, F4 :59-70 (no `PASSED@` or `WAIVED` 
docs/reports/2026-10-28-f4-[name]-reply-filing.md:232 | der]|effectively|confirms the PRAXIS|satisfies F4|F4 is (met|satisfied|clea
docs/reports/2026-10-28-f4-[name]-reply-filing.md:348 | round found wording that says or implies F4 is met. No round foun
docs/reports/2026-11-04-status-refresh-manager.md:257 | /SPEC_RUBRIC.md` F1 :17-28, F2 :30-43, F3 :45-57, F4 :59-70 (no `PASSED@` or `WAIVED` 
docs/reports/2026-11-06-status-handoff-refresh-manager.md:148 | | F1–F4 not PASSED/WAIVED; F1/F2/
docs/reports/2026-11-06-status-handoff-refresh-manager.md:194 | F1–F4 are FROZEN (CMD: no `PASSED@`/`WAIVED` bey
~~~
- Proposed fix: replace "Worker 3 did not record its status-word filter" with the eight-word list from :141 and re-run with all eight words, pasting the 12 hits and their classification.

### 4. MINOR. Worker 2, C1-W8 reading says each negating line "names F4 once"; three name it twice
- Where: worker2 :340. The pasted command uses `grep -c -w F4`, which counts lines, not occurrences, so the pasted output cannot support "once", and the re-run shows three of the twelve lines carry two occurrences (S2).
- Evidence (E4):
~~~text
$ sed -n 340p docs/reports/2026-11-10-f4-grading-worker2.md | grep -o 'Each of the twelve lines Block 8 calls negating names F4 once'
Each of the twelve lines Block 8 calls negating names F4 once
$ for x in docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:533 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:763 DECISION_LOG.md:165; do f=${x%:*}; n=${x##*:}; printf '%s lines=%s occurrences=%s\n' "$x" "$(git show "HEAD:$f" | sed -n "${n}p" | grep -c -w F4)" "$(git show "HEAD:$f" | sed -n "${n}p" | grep -o -w F4 | wc -l | tr -d ' ')"; done
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:533 lines=1 occurrences=2
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:763 lines=1 occurrences=2
DECISION_LOG.md:165 lines=1 occurrences=2
~~~
- Proposed fix: "Each of the twelve lines contains F4 (grep -c counts lines, so 1 means at least once)".

### 5. MINOR. Multi-pattern greps cannot show that each string is present, yet the readings say each is
- Where: worker3 C1-X4 :243 to :244 with reading :271; worker4 C1-Y2 :116 to :117 with reading :128 ("Each set of strings is found only at the cited lines"); worker4 C1-Y4 :157 to :158; worker3/worker4 ISSUE_REGISTER greps (three strings, output "70"). A `grep -n -e A -e B | cut -d: -f1` prints the same line list whether or not every pattern matched. My per-string re-run shows every string is in fact present at the cited line, so nothing is false; it is the pasted output that does not show it (S1).
- Evidence (E5):
~~~text
$ sed -n 271p docs/reports/2026-11-10-f4-grading-worker3.md | grep -o 'DECISION_LOG.md holds its strings at :46, :177, :435 and :801'
DECISION_LOG.md holds its strings at :46, :177, :435 and :801
$ sed -n 128p docs/reports/2026-11-10-f4-grading-worker4.md | grep -o 'Each set of strings is found only at the cited lines'
Each set of strings is found only at the cited lines
$ for s in "the MFFU inquiry email are the TRADER'S actions to execute" 'by a human rep' 'boilerplate indicator' 'F4 is called "closed" in the strategy filter audit' 'naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.**'; do printf '%s => %s\n' "$(echo "$s" | cut -c1-30)" "$(git show HEAD:DECISION_LOG.md | grep -n -F -e "$s" | cut -d: -f1 | tr '\n' ' ')"; done
the MFFU inquiry email are the => 46 
by a human rep => 177 
boilerplate indicator => 435 
F4 is called "closed" in the s => 801 
naming NinjaTrader 8 + Rithmic => 435 
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); for s in 'for fully automated order execution' 'This enables your custom software to submit orders, manage positions' 'integrate your trading bot or automated strategy via the Tradovate API' 'your MyFundedFutures Tradovate evaluation and funded accounts' 'on all plans'; do printf '%s => %s\n' "$(echo "$s" | cut -c1-30)" "$(git show "HEAD:$T" | grep -n -F -e "$s" | cut -d: -f1 | tr '\n' ' ')"; done
for fully automated order exec => 27 
This enables your custom softw => 28 
integrate your trading bot or  => 28 
your MyFundedFutures Tradovate => 27 
on all plans => 29 
~~~
- Proposed fix: paste a per-string loop like the two above in place of, or next to, each combined grep.

### 6. MINOR. Worker 2 section leaves some original claims neither re-run nor listed as not re-run
- Where: worker2 Block 6 :90 ("remaining hits: unrelated", a claim about rubric manager reports), Block 8 :126 (re-quotes at the f4 evidence report :349 and d11 sweep :1790), :130 (r8j lines 458/1143/1448/1451), :133 (stale cites at rvn4-filing-manager:120 and others). C1-W8 prints only the first six `F4.N` hits of r8j (452 to 495). The Correction 1 section never names these, and only the Block 7 status-word count is marked UNVERIFIED. The r8j lines do carry `F4.N` ids (last command below), so this is a coverage gap, not a false claim.
- Evidence (E6):
~~~text
$ sed -n '90p;126p;130p;133p' docs/reports/2026-11-10-f4-grading-worker2.md | grep -o -e 'remaining hits: unrelated' -e 'also re-quoted at f4 evidence report :349 and d11-sweep-manager :1790' -e '458/1143/1448/1451' -e 'rvn4-filing-manager:120'
remaining hits: unrelated
also re-quoted at f4 evidence report :349 and d11-sweep-manager :1790
458/1143/1448/1451
rvn4-filing-manager:120
$ for s in 1143 1448 1451 ':349' ':1790' 'confirmed by direct inquiry' 'rvn4'; do printf '%-28s %s\n' "$s" "$(sed -n '148,341p' docs/reports/2026-11-10-f4-grading-worker2.md | grep -c -F -e "$s")"; done
1143                         0
1448                         0
1451                         0
:349                         0
:1790                        0
confirmed by direct inquiry  0
rvn4                         0
$ for n in 1143 1448 1451; do printf '%s %s\n' $n "$(git show HEAD:docs/reports/2026-08-06-session42-r8j-phase3-import.md | sed -n ${n}p | grep -c 'F4\.[0-9]')"; done
1143 1
1448 1
1451 1
~~~
- Proposed fix: add a "Not re-run" list to the worker 2 section (as workers 3 and 4 have) naming these, or paste re-runs.

### 7. MINOR. Four smaller unbacked or mis-cited statements (E7)
- 7a. worker4 :67 says the outgoing preview is "byte-equal apart from [rep name]". C1-Y1 (:89 to :104) prints 30 characters of fence line 2 and contains no `cmp` or `diff`; byte equality is not shown.
- 7b. correction-1 manager :3 says "Started 2026-11-10T17:38:16Z (`date -u`, block C1-V0)", but C1-V0's `date -u` at :40 prints 17:44:58. The cited block does not show the cited time.
- 7c. manifest-manager :143 says "A diff against HEAD", but every command in the section is `git diff` (working tree against the index); no `git diff HEAD` or `--cached` is in the section. My re-run shows the HEAD diff is also `13 0` and the index holds no MANIFEST change, so the statement is true now; it is not shown in the section.
- 7d. worker3 :288 sends item D to the correction-1 manager's "Final checks", which is still a placeholder (:127 to :129). Item D stays unbacked until that section is filled; the brief marks that placeholder as intentional, so this is conditional.
~~~text
$ sed -n 67p docs/reports/2026-11-10-f4-grading-worker4.md | grep -o 'byte-equal apart from "\[rep name\]"'
byte-equal apart from "[rep name]"
$ sed -n '89,104p' docs/reports/2026-11-10-f4-grading-worker4.md | grep -c -e 'cmp' -e 'diff'
0
$ sed -n 3p docs/reports/2026-11-10-f4-grading-correction-1-manager.md | grep -o 'Started.\{0,60\}'
Started.** 2026-11-10T17:38:16Z (`date -u`, block C1-V0).
$ sed -n 40p docs/reports/2026-11-10-f4-grading-correction-1-manager.md
Tue Nov 10 17:44:58 UTC 2026
$ sed -n 143p docs/reports/2026-11-10-f4-grading-manifest-manager.md | grep -o 'A diff against HEAD'
A diff against HEAD
$ sed -n '98,152p' docs/reports/2026-11-10-f4-grading-manifest-manager.md | grep -c -e 'diff HEAD' -e 'diff --cached'
0
$ git diff HEAD --numstat -- MANIFEST.md; git diff --cached --numstat -- MANIFEST.md | wc -l
13	0	MANIFEST.md
       0
$ sed -n 288p docs/reports/2026-11-10-f4-grading-worker3.md | grep -o 'section "Final checks"'
section "Final checks"
$ sed -n '127,129p' docs/reports/2026-11-10-f4-grading-correction-1-manager.md
## Final checks

Pending: run after the last edit to every file.
~~~
- Proposed fix: 7a paste a `cmp` of fence line 2 against the manager report's quoted preview after the token swap, or drop "byte-equal"; 7b cite the block that holds 17:38:16Z or change the time; 7c add `git diff HEAD --numstat -- MANIFEST.md` and `git diff --cached --numstat -- MANIFEST.md | wc -l`; 7d fill Final checks before the audit.

## Checks that found nothing

- Check A, finding 4 (line numbers, Block 7 count): reproduced. `grep -n` gives 26, 639, 640, 642, 644, 645 (six off by one, as the correction says); the original Block 3 still carries 25, 638, 639, 641, 643, 644. Block 7: `-w F4` = 496, `-P` = 496, `-i -w` = 634, `-E \b` = 0, A15 = 6. Block 1 and Block 6 counts reproduce.
- Check A, finding 5, the re-runs that do exist: worker 3 X1 phrase counts and worker 4 Y1 hits reproduce; the R6 branch is `bf6fcc7`, 117 lines, sections at 76 82 92 98 104.
- Check A, finding 6: cured. Numstat `13 0`, hunks `@@ -306,0 +307,8 @@` and `@@ -350,0 +359,5 @@`, 0 deleted lines all reproduce; my own run of the scratch demonstration gives `2 0` before and after the in-place edit; both sentences are retracted and the 8 rows' unchanged state is marked UNVERIFIED (manifest-manager :147 to :150).
- C1-V0: the pattern, S13, banned-word and address-local-part files rebuild byte-identical from the C1-V0 commands; both "My name is" lines in the transcript (25, 50) carry a name that is in the pattern file.
- Check C: no element-table label, coverage reading or F4 grade is changed. The only label words in the four sections are worker 4's C1-Y5 print-out of the current table; the one `PASSED@` hit in worker 3's section is HEAD STATUS :104 text inside a re-run output.
- Checks D, E and S13 on the five files: every count 0; last line is the standing sentence and it occurs exactly once; each Correction 1 section is byte-equal to the manager's build file. Original text above each section: no pre-correction copy exists, so "unchanged" is UNVERIFIED by me; the surviving Block 3 numbers above are consistent with it.
~~~text
$ for f in docs/reports/2026-11-10-f4-grading-worker2.md docs/reports/2026-11-10-f4-grading-worker3.md docs/reports/2026-11-10-f4-grading-worker4.md docs/reports/2026-11-10-f4-grading-manifest-manager.md docs/reports/2026-11-10-f4-grading-correction-1-manager.md; do printf '%s last=%s s13x=%s bw=%s pat=%s email=%s lp=%s hex16=%s\n' "${f#docs/reports/2026-11-10-f4-grading-}" "$(tail -n1 "$f" | cmp -s - /tmp/f4c1-s13.txt && echo ok || echo BAD)" "$(grep -c -x -F -f /tmp/f4c1-s13.txt "$f")" "$(grep -c -i -F -f /tmp/f4c1-bw.txt "$f")" "$(grep -c -i -w -F -f /tmp/f4c1-pat.txt "$f")" "$(grep -c -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f")" "$(grep -c -i -w -F -f /tmp/f4c1-lp.txt "$f")" "$(grep -c -E '\b[0-9a-f]{16}\b' "$f")"; done
worker2.md last=ok s13x=1 bw=0 pat=0 email=0 lp=0 hex16=0
worker3.md last=ok s13x=1 bw=0 pat=0 email=0 lp=0 hex16=0
worker4.md last=ok s13x=1 bw=0 pat=0 email=0 lp=0 hex16=0
manifest-manager.md last=ok s13x=1 bw=0 pat=0 email=0 lp=0 hex16=0
correction-1-manager.md last=ok s13x=1 bw=0 pat=0 email=0 lp=0 hex16=0
$ for p in worker2:148:s-worker2 worker3:153:s-worker3 worker4:85:s-worker4 manifest-manager:98:s-mm; do IFS=: read n s b <<< "$p"; F=docs/reports/2026-11-10-f4-grading-$n.md; L=$(wc -l < "$F"); sed -n "${s},$((L-1))p" "$F" | cmp -s - /tmp/f4c1/$b.md && echo "$n section = /tmp/f4c1/$b.md" || echo "$n section differs"; done
worker2 section = /tmp/f4c1/s-worker2.md
worker3 section = /tmp/f4c1/s-worker3.md
worker4 section = /tmp/f4c1/s-worker4.md
manifest-manager section = /tmp/f4c1/s-mm.md
$ for p in worker2.md:148 worker3.md:153 worker4.md:85 manifest-manager.md:98; do F=docs/reports/2026-11-10-f4-grading-${p%:*}; s=${p##*:}; printf '%s labels=%s passed=%s f4state=%s\n' "${p%:*}" "$(sed -n "${s},\$p" $F | grep -c -E 'COVERED|NOT ADDRESSED|CONTRADICTED')" "$(sed -n "${s},\$p" $F | grep -c -E 'PASSED@|WAIVED')" "$(sed -n "${s},\$p" $F | grep -c -i -E 'F4 (is|should be|can be|may be) (closed|satisfied|met|passed|unfrozen|cleared)')"; done
worker2.md labels=0 passed=0 f4state=0
worker3.md labels=0 passed=1 f4state=0
worker4.md labels=9 passed=0 f4state=0
manifest-manager.md labels=0 passed=0 f4state=0
$ sed -n '153,$p' docs/reports/2026-11-10-f4-grading-worker3.md | grep -n -E 'PASSED@|WAIVED' | cut -c1-90
43:104:**Phase: unchanged. Block 2 — Backtesting. F1, F2, F4 FROZEN; F3 FROZEN.** `grep -n
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); { git show "HEAD:$T" | sed -n 15p | awk '{print $2}'; git show "HEAD:$T" | sed -n 16p | awk '{print $2}'; git show "HEAD:$T" | sed -n 25p | grep -o 'My name is [A-Za-z]*' | awk '{print $4}'; git show "HEAD:$T" | sed -n 36p | cut -d- -f1; git show HEAD:DECISION_LOG.md | sed -n 177p | grep -oE '[0-9a-f]{16}' | sort -u; } > /tmp/f4c1-w2adv/pat.txt; cmp /tmp/f4c1-w2adv/pat.txt /tmp/f4c1-pat.txt && echo "pattern file rebuilt per C1-V0: identical"
pattern file rebuilt per C1-V0: identical
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 136p | grep -o '"Fills are optimistic[^"]*"' | tr -d '"' | cmp - /tmp/f4c1-s13.txt && echo "s13 file identical"; printf '%s\n' "ver""dict" "COMMIT-""INDEX" "COMMIT-DIFF-""SHA256" | cmp - /tmp/f4c1-bw.txt && echo "bw file identical"; git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 34p | grep -oE '[A-Za-z0-9._%+-]+@' | tr -d '@' | cmp - /tmp/f4c1-lp.txt && echo "lp file identical"
s13 file identical
bw file identical
lp file identical
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); git show "HEAD:$T" | grep -n -i 'my name is' | cut -d: -f1 | tr '\n' ' '; git show "HEAD:$T" | grep -i -o 'my name is [A-Za-z]*' | awk '{print $4}' | grep -c -i -x -F -f /tmp/f4c1-pat.txt
25 50 2
~~~
~~~text
$ git grep -E '\bF4\b' HEAD | wc -l; git grep -w F4 HEAD | wc -l; git grep -P '\bF4\b' HEAD | wc -l; git grep -w A15 HEAD | wc -l; git grep -i -w F4 HEAD | wc -l
       0
     496
     496
       6
     634
$ git grep -c -i -e 'outreach' -e 'eight-firm' HEAD -- DECISION_LOG.md HANDOFF.md ISSUE_REGISTER.md docs/reports/2026-08-07-f4-mffu-compliance-evidence.md docs/reports/2026-10-30-zyd-f3-artifact.md
HEAD:DECISION_LOG.md:1
HEAD:HANDOFF.md:1
HEAD:ISSUE_REGISTER.md:1
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:3
HEAD:docs/reports/2026-10-30-zyd-f3-artifact.md:1
$ git grep -c -i -E 'inquiry|enquiry' HEAD -- DECISION_LOG.md ISSUE_REGISTER.md docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
HEAD:DECISION_LOG.md:1
HEAD:ISSUE_REGISTER.md:1
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:1
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -e 'Quoted verbatim as relayed' -e 'Algo trading is now permitted at MFFU' -e 'the evaluation, simulated-funded and live' -e '^| Timestamp | 2026-07-26' -e '^| Respondent |' -e 'truncated follow-up' -e '^in full as visible' -e 'Two follow-ups so I can be sure' -e 'The full text of his questions' -e '^not say whether the reply answers' | cut -d: -f1 | tr '\n' ' '; echo
26 28 29 35 36 636 639 640 642 644 645 
$ sed -n '46p;54p;55p;56p;57p;58p' docs/reports/2026-11-10-f4-grading-worker2.md | cut -c1-5 | tr '\n' ' '; echo
25: Q 638:  639:  641:  643:  644:  
$ for s in "Dear MFFU" "Hi MFFU" "Hello MFFU" "I am building" "draft email" "draft of the follow-up" "follow-up draft" "To: support" "Subject: " "email draft"; do printf '%s=%s ' "$s" "$(git grep -l -i -F -e "$s" HEAD | wc -l | tr -d ' ')"; done; echo
Dear MFFU=0 Hi MFFU=0 Hello MFFU=0 I am building=0 draft email=0 draft of the follow-up=0 follow-up draft=0 To: support=0 Subject: =2 email draft=1 
$ git grep -n -i -F -e "Two follow-ups" -e "Does this specific" HEAD | cut -d: -f1-3 | sed 's/-[a-z]*-reply/-[name]-reply/'
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:642
HEAD:docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md:16
$ git rev-parse --short r6/announcement-research; R=r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt; git show "$R" | wc -l; git show "$R" | grep -n 'Section [0-9]' | cut -d: -f1 | tr '\n' ' '; echo
bf6fcc7
     117
76 82 92 98 104 
$ git diff --numstat -- MANIFEST.md; git diff -U0 -- MANIFEST.md | grep '^@@'; git diff -U0 -- MANIFEST.md | grep -c '^-[^-]'
13	0	MANIFEST.md
@@ -306,0 +307,8 @@
@@ -350,0 +359,5 @@
0
$ D=/tmp/f4c1-w2adv/demo; rm -rf $D && mkdir $D && printf 'a\n' > $D/base.md && printf 'a\nrow1\nrow2\n' > $D/m.md && git diff --no-index --numstat $D/base.md $D/m.md; sed -i '' 's/row1/row1-edited-in-place/' $D/m.md && git diff --no-index --numstat $D/base.md $D/m.md; git diff --no-index -U0 $D/base.md $D/m.md | grep -c '^-[^-]'
2	0	/tmp/f4c1-w2adv/demo/{base.md => m.md}
2	0	/tmp/f4c1-w2adv/demo/{base.md => m.md}
0
$ git diff --cached --name-only | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
~~~

## Files staged
None. This report is new and untracked; no git add, reset, stash, checkout or commit was run.

## Result
FAIL. 2 BLOCKING (findings 1, 2), 5 MINOR (findings 3 to 7, with 7 holding four items). Audit finding 6 is cured; audit finding 4 is cured for commands and line numbers but finding 2 and 6 above leave gaps; audit finding 5 is not cured (finding 1).
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
