# Noise-area paper read, worker 6 (ADVERSARIAL): Addendum 2 (worker 5)

## Task

Unit `2026-11-15-noise-area-paper-read`, worker 6, mode ADVERSARIAL, read-only. Artifact: section `## Addendum 2 (worker 5, corrections to the worker 3 addendum)`, lines 955-1063 of `docs/reports/2026-11-15-noise-area-paper-read-worker1.md`. Criteria: specs/SPEC_RUBRIC.md S1, S2, S8, S13. Nothing was staged or committed. Git commands were read-only, run with `GIT_OPTIONAL_LOCKS=0`, and no `git status` was run. Report written at 2026-11-15 16:59:15 UTC (`date -u`).

## Artifact hash

```
Sun 15 Nov 2026 16:56:31 UTC
2e8327578e7a5eab740ddb3d83cd8342be828fef82bdc0e986ca5fd0778860e4  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
41d635d162551c4add329d2a11cd9571aea391befd00e472ed81c0070bb207ad  /tmp/praxis-npr/dl/w1/paper.pdf
    1063 /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-15-noise-area-paper-read-worker1.md
```
Both hashes match the brief. My own extraction (`pdftotext -layout -f N -l N`, 43 pages) went into `/tmp/praxis-npr/w6-text/`. My pages 02, 09, 10 and 37 have the same hashes as the w1-text copies:
```
ac382048da4b62bf680366757240f714ef6d83a6e66967d6e9740fcb4257ed80  page-02.txt (w6 and w1 equal)
bbb6ce8b2232c61ea75988dbd1d15e634ca7f8c3923763eb8eabc238082bcae0  page-09.txt (w6 and w1 equal)
07320da13071cc031934f7e3adc2ba400aed17cea0478a747880939d4def5e35  page-10.txt (w6 and w1 equal)
de5e5d8dec9f8df65c7fcde433ba9aca86af3f53f0a748e909aff7f503cadd86  page-37.txt (w6 and w1 equal)
```

## Quote verification

Script `/tmp/praxis-npr/scripts-w6/quotes.py`, run as `python3 -I -B` from scripts-w6 against my w6-text pages. It checks four things. (1) Pasted blocks: each line must equal the paper line, with the `cat -n` number checked. (2) Grep-output lines. (3) Inline raw-line quotes, compared after stripping indentation. (4) Assembled phrases, joined across lines with de-hyphenation, which must appear both in the paper span and in the section. Result: **38/38 PASS** (output under Verification evidence).

## Git and grep re-runs

All F1 commands give the same output as the artifact. The only difference is that `wc -l` pads its number with spaces. I also checked further: `git log --all -- Redemtion/` has 0 commits, and the RTF exists on disk (45151 bytes). The label grep limited to lines 1-954 gives the same 4 lines (453, 598, 613, 623). The paths on lines 613 and 623 are tracked.

## Count and omission checks

- F2: The artifact's regex gives 5 matches, 3 of them across a line break (p9:6, p10:11, p37:48). A broader regex of my own gives the same 5 and 3. It adds hyphenation (`mar-ket`), `market's close`, `close of the day/session/market`, `end of the trading day/session` and `end-of-day`. **F2 count CONFIRMED.**
- F3 "namic trailing stops already quoted": line 770 is `29: which have been ... dy-`, line 771 is `30: namic trailing stops ...`, and line 802 holds the assembled phrase. **CONFIRMED** (but see defect 3).
- F3 "entry-timing sentence is an omission (0 hits in this file before this addendum)": the artifact's grep pattern does give 0 hits in lines 1-954. **But raw line p2:25, the first line of that same sentence, is already in the file at line 905**: `page-02.txt:25:       500. Unlike the academic literature that typically limits trading to the last 30 min-`. It is part of worker 3's `order|limit|fixed...` grep output in D7(d). Line 907 also carries the body's restatement of the same point (p4:32, "our model does not limit the trading to the last 30-minutes of the trading session"). The artifact's own grep output pastes line 906, the very next line, and does not mention 905. See defect 1.
- Own page greps: `grep -n -i 'as soon as there' page-*.txt` gives exit 1 (no match). The two-pattern grep gives p2:26 and p2:27. Both **CONFIRMED.**

## Effect paragraph check

- (a) "dynamic trailing stops ... unlimited upside potential was already considered": line 802 and the worker 3 Effect (a) at line 949 both carry it. CONFIRMED. "None of F1-F3 adds a fixed maximum loss known at entry": none of the quoted lines (p2:22-31, p9:5-7, p10:11-12, p37:48-49) names a fixed loss. CONFIRMED.
- (b) "The Figure 2 caption's 16:00 close is already in Q3 and the answer": Q3 (lines 263-275) contains the caption, and the Answer has line 434 "The market Close at 16:00 (Q2, Q3)". CONFIRMED. "as soon as there is an indication ... names no check frequency": p2:25-28 contains no interval. CONFIRMED.
- "F1 changes only the provenance label": consistent with F1 as written.

## Privacy, S8, S13

- Section 955-1063: 0 at-sign characters. The email regex gives exit 1 (no match). A grep for the names of the trader (first name and surname), Zarattini, Aziz and Barbon gives exit 1. The section names no person. The capitalised word pairs it contains are all titles, paths or paper text ("Asset Under").
- S8: the only hit for recommend/should/retest/decide is line 107 of the section, the disclaimer. No decision or trading recommendation is made.
- S13: the standing sentence occurs once in the whole file (`grep -c -F` = 1), and the last line matches it exactly (LAST_LINE_MATCH).
- Observation, not a defect: the corrected D6 wording "Only the p. 9 caption describes an exit rule" is scoped to the "three more occurrences" across line breaks. The single-line hits p9:20 ("Positions are unwound either at market Close ...") and p9:31 also describe exit rules. In context the scope holds, but the sentence read alone does not.
- Observation, not a defect: the F2 python step is paraphrased as `(python3 -I, regex ..., print matches containing a newline)` rather than pasted as a command. Its output reproduces exactly with my script.

## Verification evidence

```
Sun 15 Nov 2026 16:57:38 UTC   (quotes.py)
PASS block md994 == p9:5 exact=True rstrip=True catn_num_ok=True
PASS block md995 == p9:6 exact=True rstrip=True catn_num_ok=True
PASS block md996 == p9:7 exact=True rstrip=True catn_num_ok=True
PASS block md998 == p10:11 exact=True rstrip=True catn_num_ok=True
PASS block md999 == p10:12 exact=True rstrip=True catn_num_ok=True
PASS block md1001 == p37:48 exact=True rstrip=True catn_num_ok=True
PASS block md1002 == p37:49 exact=True rstrip=True catn_num_ok=True
PASS block md1024 == p2:22 exact=True rstrip=True catn_num_ok=True
PASS block md1025 == p2:23 exact=True rstrip=True catn_num_ok=True
PASS block md1026 == p2:24 exact=True rstrip=True catn_num_ok=True
PASS block md1027 == p2:25 exact=True rstrip=True catn_num_ok=True
PASS block md1028 == p2:26 exact=True rstrip=True catn_num_ok=True
PASS block md1029 == p2:27 exact=True rstrip=True catn_num_ok=True
PASS block md1030 == p2:28 exact=True rstrip=True catn_num_ok=True
PASS block md1031 == p2:29 exact=True rstrip=True catn_num_ok=True
PASS block md1032 == p2:30 exact=True rstrip=True catn_num_ok=True
PASS block md1033 == p2:31 exact=True rstrip=True catn_num_ok=True
PASS grep md1053 == p2:26
PASS grep md1054 == p2:27
PASS inline md1012 == p2:25 strip
PASS inline md1013 == p2:26 strip
PASS inline md1014 == p2:27 strip
PASS inline md1015 == p2:28 strip
PASS inline md1017 part1 == p2:29 strip
PASS inline md1017 part2 == p2:30 strip
PASS inline md1017 part3 == p2:31 strip
PASS phrase 'Please note that all positions are closed at the market Close (16:00).' in p9:5-7 (md has it: True)
PASS phrase 'closed at the market / Close (16:00)' in p9:6-7 (md has it: True)
PASS phrase 'market / Close' in p9:6-7 (md has it: True)
PASS phrase 'end / of day' in p10:11-12 (md has it: True)
PASS phrase 'until market / close' in p37:48-49 (md has it: True)
PASS phrase 'end of day t − 1' in p10:11-12 (md has it: True)
PASS phrase 'the last 30 minutes of the trading session' in p2:25-26 (md has it: True)
PASS phrase 'as soon as there is an indication' in p2:26-27 (md has it: True)
PASS phrase 'dynamic trailing stops' in p2:29-30 (md has it: True)
PASS phrase 'unlimited upside potential' in p2:30-31 (md has it: True)
PASS phrase '500.' in p2:25-25 (md has it: True)
PASS phrase 'price action.' in p2:28-28 (md has it: True)
TOTAL 38/38 PASS
```
```
Sun 15 Nov 2026 16:57:44 UTC   (count.py)
== worker5: total=5 linesplit=3
SPLIT page-09.txt 6 'market\nClose'
      page-09.txt 20 'market Close'
      page-09.txt 31 'market Close'
SPLIT page-10.txt 11 'end\nof day'
SPLIT page-37.txt 48 'market\nclose'
== broad: total=5 linesplit=3
SPLIT page-09.txt 6 'market\nClose'
      page-09.txt 20 'market Close'
      page-09.txt 31 'market Close'
SPLIT page-10.txt 11 'end\nof day'
SPLIT page-37.txt 48 'market\nclose'
```
```
Sun 15 Nov 2026 16:57:53 UTC   (F1 re-runs, repo root)
$ git rev-parse --short HEAD
d9fc5f0
$ git cat-file -e d9fc5f0:"<RTF>"; echo $?
fatal: path 'Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf' exists on disk, but not in 'd9fc5f0'
128
$ git ls-files -- "<RTF>" | wc -l
       0
$ ls -la "<RTF>"
-rw-r--r--<at> 1 admin  staff  45151 May  8  2026 Redemtion/Int   (ls xattr marker masked as <at> to keep the report at-sign free)
$ git check-ignore -v -- "<RTF>"; echo exit=$?
.gitignore:7:Redemtion/	Redemtion/Intitialization-April 2026/Verified Trading-Strategy Shortlist for NQ : Index Futures.rtf
exit=0
$ sed -n 7p .gitignore
Redemtion/
$ git ls-files -- Redemtion/ | wc -l
       0
$ git log --oneline --all -- Redemtion/ | wc -l
       0
$ head -954 F | grep -n label pattern
453:Line numbers are from the working tree. `git status --short` showed the spec, the 4uu report and the scope proposal 
598:$ git status --short -- "<RTF>"   (empty = clean at HEAD)
613:$ git status --short -- docs/specs/2026-07-16-b2-noise-area-ruleset.md   (empty = clean)
623:$ git status --short -- docs/reports/2026-11-14-r3-recheck-manager.md   (empty = clean)
$ git ls-files -- <613 path> <623 path>
docs/reports/2026-11-14-r3-recheck-manager.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
$ sed -n 453p F
Line numbers are from the working tree. `git status --short` showed the spec, the 4uu report and the scope proposal clean at HEAD `d9fc5f0`. `DECISIONS.md` is modified in the working tree (` M`), and `docs/reports/2026-11-15-voice-notes-open-questions.md` is untracked (`??`).
```
```
Sun 15 Nov 2026 16:58:05 / 16:58:12 UTC   (F3 omission, lines 1-954 only)
as soon as there => 0
indication of abnormal => 0
trend-following positions => 0
academic literature => 1
last 30 min => 1
utes of the trading session => 1
page-02.txt:2[5-8] => 1
905:page-02.txt:25:       500. Unlike the academic literature that typically limits trading to the last 30 min-
907:page-04.txt:32:studies, our model does not limit the trading to the last 30-minutes of the trading session;
--- lines 768-773 (cat -n 1-6)
     3	29:       which have been discussed in our previous papers, we introduce the use of dy-
     4	30:       namic trailing stops to mitigate downside risks while allowing for unlimited upside
     5	31:       potential. From 2007 to early 2024, the resulting intraday momentum portfolio
```
(The "utes of the trading session" hit in lines 1-954 is line 907, p4:32, not the abstract.)
```
Sun 15 Nov 2026 16:58:40 UTC   (own page greps, w6-text)
$ /usr/bin/grep -n -i 'as soon as there' page-*.txt
exit=1
$ /usr/bin/grep -n -E 'as soon$|^ *as there is an indication' page-02.txt
26:       utes of the trading session, our model initiates trend-following positions as soon
27:       as there is an indication of abnormal demand/supply imbalance in the intraday
--- p9:20
Positions are unwound either at market Close or if there is a crossover to the opposite
```
```
Sun 15 Nov 2026 16:58:50 UTC
$ git ls-files -- <453 files: b2 ruleset spec, 4uu report, scope proposal>
docs/reports/2026-07-16-4uu-noise-area-strategy.md
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md
docs/specs/2026-07-16-b2-noise-area-ruleset.md
--- at-sign count in section 955-1063
0
--- known-name grep in section
exit=1
--- S13 count whole file
1
--- S8 terms in section
107:This addendum makes no trading recommendation, proposes no retest and decides nothing. Those belong to the trader.
Sun 15 Nov 2026 16:59:11 UTC
--- email regex in section
exit=1
--- last line exact
LAST_LINE_MATCH
--- Answer line
434:  - The market Close at 16:00 (Q2, Q3).
```

## Files staged

None. The only file written is this report. Scratch files are under `/tmp/praxis-npr/w6-text/` and `/tmp/praxis-npr/scripts-w6/`.

## Result: FAIL

1. **S2, F3 (line 1011).** "The entry-timing sentence is an omission (0 hits in this file before this addendum)" overstates. The 0 holds only for the artifact's grep pattern. Raw line p2:25, the first of the sentence's four lines, was already in lines 1-954 at line 905 (worker 3 D7(d) grep output), and line 907 carries the p. 4 body restatement. What holds is narrower: the full sentence was never quoted or discussed. The artifact's pasted grep shows line 906 and does not disclose 905.
2. **S1, F1 (line 961).** "Line 453 names docs/ files ... so those labels are not affected" has no pasted evidence. The reason given ("names docs/ files") is not a reason, because a docs/ path could be ignored too, and line 453 also names root `DECISIONS.md`. The `git ls-files` shown covers only the 613 and 623 paths. My check shows the three line-453 files are tracked, so the conclusion holds, but the artifact does not show it.
3. **S1, F3 (line 1017), minor.** "raw p2:29-30 at lines 770-771 ... see the grep below": the pasted grep shows line 771 only. Nothing in the section shows line 770. My `sed -n 768,773p` confirms line 770 is p2:29, so the claim is true but has no pasted evidence.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
