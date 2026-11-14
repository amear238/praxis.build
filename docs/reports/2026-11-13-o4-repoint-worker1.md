# O4 repoint, worker 1: adversarial check of the DECISIONS.md :2402 repoint and MANIFEST :469-470 rows

## Task

Unit 2026-11-13-o4-repoint (rubric O4 in `specs/SPEC_RUBRIC.md`, bead Praxis_build-yra). Mode: ADVERSARIAL, read-only. Try to falsify four claims about the edit to DECISIONS.md (line 2402 pointer) and MANIFEST.md (two appended rows). The edited files were compared against the pre-copies `/tmp/o4rp-pre-DECISIONS.md` and `/tmp/o4rp-pre-MANIFEST.md`. No file was modified. No staging command was run. This report is the only file written.

Process: diffed both files against their pre-copies; checked line 2402 byte-exactly in Python (substituting the old string with the new in the pre-copy line gives the post line); checked that MANIFEST lines 1-468 are byte-identical to the pre-copy; read both reduce3 reports in full (manager 90 lines, worker1 257 lines); re-ran the zero-hit grep and the glob; checked the cited DECISION_LOG rows; counted MANIFEST columns; grepped DECISIONS.md for the old pointer. Commands under "Checks" ran through a bash runner that prints `$ <command>` and then evals it, so every command shown is the literal one run.

## Checks

### Check 1: diff shape and line counts

```
$ diff /tmp/o4rp-pre-DECISIONS.md DECISIONS.md; echo exit=$?
2402c2402
< - Strategy `ninjascript/PraxisNoiseAreaBreakout.cs`: :32 "Positions/session = REVERSE & re-enter on an opposite-band cross"; :189 "if (mod >= CloseMod)" and :191 `FlattenAll("16:00 session flat");`. No trade cap and no loser-streak stop: zero hits for `MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak` in all three `PraxisNoiseAreaBreakout*.cs` (`docs/reports/2026-11-13-o4-parity-manager.md`). Implemented: reverse and 16:00 flat. Not implemented: #2, #3.
---
> - Strategy `ninjascript/PraxisNoiseAreaBreakout.cs`: :32 "Positions/session = REVERSE & re-enter on an opposite-band cross"; :189 "if (mod >= CloseMod)" and :191 `FlattenAll("16:00 session flat");`. No trade cap and no loser-streak stop: zero hits for `MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak` in all three `PraxisNoiseAreaBreakout*.cs` (`docs/reports/2026-11-13-o4-reduce3-worker1.md` E3). Implemented: reverse and 16:00 flat. Not implemented: #2, #3.
exit=1
$ diff /tmp/o4rp-pre-MANIFEST.md MANIFEST.md; echo exit=$?
468a469,470
> | /docs/reports/2026-11-13-o4-reduce3-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-o4-reduce3 (rubric O4, bead Praxis_build-yra; master under D-2026-11-08-D D1, DECISION_LOG 2026-11-13T09:09:00Z and 13:02:03Z): three deletion-and-label edits to D-2026-11-13-A at DECISIONS.md :2393, :2405, :2410, full diff against a pre-copy, adversary grades quoted. |
> | /docs/reports/2026-11-13-o4-reduce3-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-o4-reduce3: checks (a)-(g) on D-2026-11-13-A, including byte checks of the cited quotes and the zero-hit grep the entry cites at :2402. |
exit=1
$ wc -l /tmp/o4rp-pre-DECISIONS.md DECISIONS.md /tmp/o4rp-pre-MANIFEST.md MANIFEST.md
    2416 /tmp/o4rp-pre-DECISIONS.md
    2416 DECISIONS.md
     468 /tmp/o4rp-pre-MANIFEST.md
     470 MANIFEST.md
    5770 total
$ diff /tmp/o4rp-pre-DECISIONS.md DECISIONS.md | /usr/bin/grep -E "^[0-9]"; diff /tmp/o4rp-pre-MANIFEST.md MANIFEST.md | /usr/bin/grep -E "^[0-9]"
2402c2402
468a469,470
$ python3 -I -c 'a=open("/tmp/o4rp-pre-DECISIONS.md",encoding="utf-8").read().split("\n"); b=open("DECISIONS.md",encoding="utf-8").read().split("\n"); old="(`docs/reports/2026-11-13-o4-parity-manager.md`)"; new="(`docs/reports/2026-11-13-o4-reduce3-worker1.md` E3)"; print("differing lines:",[i+1 for i,(x,y) in enumerate(zip(a,b)) if x!=y]); print("old count in pre 2402:",a[2401].count(old)); print("pre2402.replace(old,new)==post2402:",a[2401].replace(old,new)==b[2401])'
differing lines: [2402]
old count in pre 2402: 1
pre2402.replace(old,new)==post2402: True
$ head -n 468 MANIFEST.md | cmp - /tmp/o4rp-pre-MANIFEST.md; echo cmp_exit=$?
cmp_exit=0
```

Findings: DECISIONS.md has one hunk, `2402c2402`. The old string occurs once in the pre line, and replacing it with the new string reproduces the post line byte-for-byte, so nothing else on the line changed. MANIFEST.md has one hunk, `468a469,470`. Lines 1-468 are byte-identical to the pre-copy (`cmp` exit 0), so this is a pure 2-line append at the end of the file. DECISIONS.md is 2416 lines before and after. MANIFEST.md goes from 468 to 470.

Attempted break: a first substitution test in bash 3.2 printed "DIFFERENT". I traced this to bash 3.2 quote handling in `${a/"$old"/"$new"}` when the replacement contains backticks; it is not a file difference. The Python check above is byte-exact and settles it. No break.

### Check 2: :2402 pointer names a section that pastes the zero-hit output

```
$ cat -n docs/reports/2026-11-13-o4-reduce3-worker1.md | sed -n 94,106p
    94	### E3: remaining quote, bead, zero-hit and heading checks (check a)
    95	```
    96	$ cd /Volumes/Sensidine/Praxis.build && sed -n '1771p' DECISIONS.md | /usr/bin/grep -cF 'within ±15% win rate'; sed -n '512p' DECISIONS.md | /usr/bin/grep -cF "the agent's reading, confirmed by Amear in voice only"; git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '116p' | /usr/bin/grep -cF 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'; sed -n '1560,1561p' DECISIONS.md | tr -s ' \n' ' ' | /usr/bin/grep -cF 'a break-even trade counts as half a loss'; bd show Praxis_build-yra 2>&1 | /usr/bin/grep -cF 'the live-vs-backtest gate is structurally unmeetable.'; /usr/bin/grep -cE 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs | tr '\n' ' '; echo; /usr/bin/grep -c '^## .*Deviation C' DECISIONS.md; /usr/bin/grep -c '2026-11-13T05:45:00Z' DECISION_LOG.md; ls docs/reports/2026-11-13-o4-parity-manager.md
    97	1
    98	1
    99	1
   100	1
   101	1
   102	ninjascript/PraxisNoiseAreaBreakout.cs:0 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0 
   103	0
   104	1
   105	docs/reports/2026-11-13-o4-parity-manager.md
   106	```
$ ls ninjascript/PraxisNoiseAreaBreakout*.cs
ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
$ /usr/bin/grep -cE 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs; echo exit=$?
ninjascript/PraxisNoiseAreaBreakout.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
exit=1
$ sed -n 2402p DECISIONS.md | /usr/bin/grep -oE "zero hits for .{0,140}"
zero hits for `MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak` in all three `PraxisNoiseAreaBreakout*.cs` (`docs/reports/2026-11-13-o4-redu
```

Ambiguity probe (is "E3" a unique section label in that report?):

```
$ /usr/bin/grep -nE "^#+ .*E3|E3" docs/reports/2026-11-13-o4-reduce3-worker1.md | cut -c1-120
81:The one miss is my own probe record, not an entry quote: the entry cites :1771 only as "(pointer :1771)" with no quot
94:### E3: remaining quote, bead, zero-hit and heading checks (check a)
229:E2 gives 28 of 29 records present. The one miss is a probe record I wrote for :1771 with an ASCII "+/-" string. The 
235:Last round's defect was the unlabelled :2410 SHM reading. It now carries "(the master's reading under D1, changeable
```

Findings: E3 (worker1 :94-106) is the only heading named E3. Every other "E3" hit is a back-reference to it. Its command (:96) uses the same pattern and glob, and its output (:102) pastes `:0` for all three files. Today's re-run gives `:0` for the same three files (grep exit 1 = no match anywhere), and `ls` shows exactly three files match the glob. These are the three the report names. The pattern string in :2402 is the same one the report greps for. No break.

### Check 3: MANIFEST :469-470 rows against the reports

Both reports read in full:

```
$ wc -l docs/reports/2026-11-13-o4-reduce3-manager.md docs/reports/2026-11-13-o4-reduce3-worker1.md
      90 docs/reports/2026-11-13-o4-reduce3-manager.md
     257 docs/reports/2026-11-13-o4-reduce3-worker1.md
     347 total
$ cat -n docs/reports/2026-11-13-o4-reduce3-manager.md | sed -n "1,6p;44,46p;58,64p;66,75p;84,88p"
     1	# O4 reduce-3, manager: deletion and labels on D-2026-11-13-A (bead Praxis_build-yra)
     2	
     3	**Task:** three edits to DECISIONS.md lines 2393, 2405, 2410 (one deletion, two labels), then one cold adversary. Authorised by DECISION_LOG rows 2026-11-13T09:09:00Z and 2026-11-13T13:02:03Z (praxis-master, under D-2026-11-08-D D1).
     4	**Rubric criteria addressed:** O4, specs/SPEC_RUBRIC.md:117-122.
     5	**Workers dispatched:** worker 1, ADVERSARIAL, read-only, report docs/reports/2026-11-13-o4-reduce3-worker1.md; outcome under "Adversarial findings".
     6	**Process log:** read rubric O4 and the reduce-2 adversary report; made the pre-copy; ran the three guard checks (all 1); made edits (i), (ii), (iii) with the Edit tool; diffed; dispatched the adversary with only the entry location, pre-copy path, rubric text and prior report path.
    44	```
    45	$ cd /Volumes/Sensidine/Praxis.build && diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; echo "exit=$?"; wc -l DECISIONS.md; diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md | grep -E '^[0-9]'; git diff --cached --name-only | wc -l
    46	2393c2393
    58	exit=1
    59	    2416 DECISIONS.md
    60	2393c2393
    61	2405c2405
    62	2410c2410
    63	       1
    64	```
    66	## Adversarial findings
    67	
    68	Worker 1 (cold, ADVERSARIAL, read-only), docs/reports/2026-11-13-o4-reduce3-worker1.md, overall `## Result: PASS` (:255). Grades quoted:
    69	- :228 "## (a) Quotes byte-present: PASS" (28/29 at E2 :79; the miss is the worker's own ASCII "+/-" probe of the bare pointer :1771, and E3 :97 shows the "±" form present)
    70	- :231 "## (b) Both O4 questions answered: PASS"
    71	- :234 "## (c) No over-attribution; master's readings labelled: PASS" (:235: the :2410 reading "now carries \"(the master's reading under D1, changeable)\"")
    72	- :238 "## (d) Unobserved mechanisms CONDITIONAL with void clause or named gap: PASS"
    73	- :241 "## (e) No D2 item decided: PASS"
    74	- :244 "## (f) Diff changes lines 2393, 2405, 2410 only: PASS"
    75	- :247 "## (g) Prior observations graded against the edited entry: PASS": Obs 1 "resolved" (:248), Obs 2 "resolved" (:249), Obs 3 "not a defect" (:250)
    84	## Files staged
    85	
    86	None by this unit. Real index left at 1 path (start and end counts above). Files modified: DECISIONS.md (lines 2393, 2405, 2410), this report, and the worker report.
    87	
    88	Result: PASS
$ cat -n docs/reports/2026-11-13-o4-reduce3-worker1.md | sed -n "1,3p;9,11p;24,31p;33,35p;78,81p;94,96p;102p;228,229p;244,245p;252,255p"
     1	# O4 reduce-3, worker 1: adversarial check of D-2026-11-13-A (DECISIONS.md:2389-2416)
     2	
     3	**Task:** cold adversarial check of the edited entry, seven checks (a)-(g). Checks (a)-(e) are run as `docs/reports/2026-11-13-o4-reduce2-worker1.md` defines them. Check (f) is redefined for this round: the diff changes lines 2393, 2405 and 2410 only. Check (g) grades that report's three "Observations (not defects)". **Mode:** ADVERSARIAL, one round, read-only. **Criterion:** rubric O4, `specs/SPEC_RUBRIC.md:117-122`.
     9	### E1: full diff and line counts (check f)
    10	```
    11	$ cd /Volumes/Sensidine/Praxis.build && diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; echo "diff exit=$?"; wc -l /tmp/o4red3-pre-DECISIONS.md DECISIONS.md; diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md | /usr/bin/grep -E '^[0-9]'
    24	diff exit=1
    25	    2416 /tmp/o4red3-pre-DECISIONS.md
    26	    2416 DECISIONS.md
    27	    4832 total
    28	2393c2393
    29	2405c2405
    30	2410c2410
    31	```
    33	### E2: quote byte check, 29 records (check a)
    34	```
    35	$ cd /Volumes/Sensidine/Praxis.build && bash <<'EOF'
    78	MISS DECISIONS.md:1771 [within +/-15% win rate]
    79	present=28 missing=1
    80	```
    81	The one miss is my own probe record, not an entry quote: the entry cites :1771 only as "(pointer :1771)" with no quoted string, and I guessed ASCII "+/-". Line 1771 carries the Unicode form (E3, first output line `1`):
    94	### E3: remaining quote, bead, zero-hit and heading checks (check a)
    95	```
    96	$ cd /Volumes/Sensidine/Praxis.build && sed -n '1771p' DECISIONS.md | /usr/bin/grep -cF 'within ±15% win rate'; sed -n '512p' DECISIONS.md | /usr/bin/grep -cF "the agent's reading, confirmed by Amear in voice only"; git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '116p' | /usr/bin/grep -cF 'First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2.'; sed -n '1560,1561p' DECISIONS.md | tr -s ' \n' ' ' | /usr/bin/grep -cF 'a break-even trade counts as half a loss'; bd show Praxis_build-yra 2>&1 | /usr/bin/grep -cF 'the live-vs-backtest gate is structurally unmeetable.'; /usr/bin/grep -cE 'MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak' ninjascript/PraxisNoiseAreaBreakout*.cs | tr '\n' ' '; echo; /usr/bin/grep -c '^## .*Deviation C' DECISIONS.md; /usr/bin/grep -c '2026-11-13T05:45:00Z' DECISION_LOG.md; ls docs/reports/2026-11-13-o4-parity-manager.md
   102	ninjascript/PraxisNoiseAreaBreakout.cs:0 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0 
   228	## (a) Quotes byte-present: PASS
   229	E2 gives 28 of 29 records present. The one miss is a probe record I wrote for :1771 with an ASCII "+/-" string. The entry quotes nothing at :1771; it gives a bare "(pointer :1771)". E3 shows :1771 does carry "within ±15% win rate". Every quoted string in the entry is present at its cited line. E3 also confirms the bf6fcc7:116 quote, the R4 :1560-1561 joined quote, the bead text and the DECISION_LOG 05:45:00Z row. Zero hits holds in all three strategy files, and the cited parity-manager report exists. No `## ` heading contains Deviation C, which matches :2401. The new :2405 parenthetical matches :512's own text (E3 line 2 = `1`, E7).
   244	## (f) Diff changes lines 2393, 2405, 2410 only: PASS
   245	E1 gives exactly three hunks, `2393c2393`, `2405c2405` and `2410c2410`, and both files are 2416 lines. Hunk 2393 removes one sentence. Hunk 2405 adds one parenthetical. Hunk 2410 adds one parenthetical.
   252	## Files staged
   253	None. Read-only round; this report is the only file written. No git add, no commit, no bd writes. DECISIONS.md was not modified.
   254	
   255	## Result: PASS
```

Cited DECISION_LOG rows and their content:

```
$ /usr/bin/grep -nE '^- \[2026-11-13T(09:09:00Z|13:02:03Z)\] WHO: praxis-master' DECISION_LOG.md | cut -c1-90
905:- [2026-11-13T09:09:00Z] WHO: praxis-master | WHAT: **O4 reduce-2 manager (a306eb0e2eb
911:- [2026-11-13T13:02:03Z] WHO: praxis-master | WHAT: **Session start (timer prompt) and
$ sed -n 905p DECISION_LOG.md | /usr/bin/grep -oE 'Decided by master under D-2026-11-08-D D1, for the next run|\(i\) deletes the sentence|\(ii\) in :2410 changes|\(iii\) in :2405 adds'
Decided by master under D-2026-11-08-D D1, for the next run
(i) deletes the sentence
(ii) in :2410 changes
(iii) in :2405 adds
$ sed -n 911p DECISION_LOG.md | /usr/bin/grep -oE 'Decided by master under D-2026-11-08-D D1|Unit 1 = O4 round 3 exactly as the 09:09:00Z row items \(i\)–\(iii\)|plus \(g\) grading'
Decided by master under D-2026-11-08-D D1
Unit 1 = O4 round 3 exactly as the 09:09:00Z row items (i)–(iii)
plus (g) grading
```

Column format and over-claim probes:

```
$ awk -F"|" "NR>=468 && NR<=470 {print NR\": NF=\" NF \" col2=[\"\$3\"] col3=[\"\$4\"] col4=[\"\$5\"]\"}" MANIFEST.md
468: NF=7 col2=[ Report ] col3=[ 3 ] col4=[ 2026-11-13 ]
469: NF=7 col2=[ Report ] col3=[ 3 ] col4=[ 2026-11-13 ]
470: NF=7 col2=[ Report ] col3=[ 3 ] col4=[ 2026-11-13 ]
$ sed -n 468,470p MANIFEST.md | cut -c1-60
| /docs/reports/2026-11-13-o4-parity-manager.md | Report | 3
| /docs/reports/2026-11-13-o4-reduce3-manager.md | Report | 
| /docs/reports/2026-11-13-o4-reduce3-worker1.md | Report | 
$ sed -n 469,470p MANIFEST.md | /usr/bin/grep -oiE 'audit[a-z]*|graded|PASS'; echo exit=$?
exit=1
$ /usr/bin/grep -nE 'audit' docs/reports/2026-11-13-o4-reduce3-manager.md docs/reports/2026-11-13-o4-reduce3-worker1.md
docs/reports/2026-11-13-o4-reduce3-worker1.md:201:    Commits land on an audit PASS. Telegram informs; it does not ask.
$ /usr/bin/grep -noE '.{0,40}o4-reduce3.{0,40}' DECISION_LOG.md
912:r.md`)" with "(`docs/reports/2026-11-13-o4-reduce3-worker1.md` E3)", nothing else in DECIS
```

Element-by-element, row :469 (manager report):
- "Manager report": manager :1 "O4 reduce-3, manager". Supported.
- "unit 2026-11-13-o4-reduce3": the report says "O4 reduce-3" (:1) and its filename is `2026-11-13-o4-reduce3-manager.md`. DECISION_LOG :911 calls it "O4 round 3". Neither report spells out the string `2026-11-13-o4-reduce3`; the unit id comes from the filename, the same convention row :468 uses ("unit 2026-11-13-o4-parity"). Supported by convention. Observation, not a defect.
- "rubric O4": manager :4. Supported.
- "bead Praxis_build-yra": manager :1. Supported.
- "master under D-2026-11-08-D D1": manager :3 "(praxis-master, under D-2026-11-08-D D1)", and both DECISION_LOG rows carry "Decided by master under D-2026-11-08-D D1". Supported.
- "DECISION_LOG 2026-11-13T09:09:00Z and 13:02:03Z": manager :3 cites both. Both rows exist (DECISION_LOG :905, :911) as praxis-master rows, and they set the (i)-(iii) edit plan and choose this unit. Supported.
- "three deletion-and-label edits to D-2026-11-13-A at DECISIONS.md :2393, :2405, :2410": manager :3 "three edits to DECISIONS.md lines 2393, 2405, 2410 (one deletion, two labels)", and the hunks at :60-62. Title :1 names D-2026-11-13-A. Supported.
- "full diff against a pre-copy": manager :45 runs `diff /tmp/o4red3-pre-DECISIONS.md DECISIONS.md`, with full hunk output :46-57 and exit :58. Supported.
- "adversary grades quoted": manager :68-75 quote all seven grade lines. Supported.
- Over-claim probe: the row has no "audit", "graded" or "PASS" (grep exit 1). Neither report records an audit (the only "audit" hit is quoted D3 text at worker1 :201). The row does not imply an audit or a grade of the manager report.

Element-by-element, row :470 (worker report):
- "ADVERSARIAL worker 1 report": worker1 :1 "worker 1" and :3 "**Mode:** ADVERSARIAL". Supported.
- "for unit 2026-11-13-o4-reduce3": same filename convention as above. Manager :5 names this file as its worker 1 report. Supported.
- "checks (a)-(g) on D-2026-11-13-A": worker1 :1 "adversarial check of D-2026-11-13-A" and :3 "seven checks (a)-(g)". Grade headings :228-247. Supported.
- "byte checks of the cited quotes": worker1 E2 :33-79 ("quote byte check, 29 records") and check (a) :228 "Quotes byte-present". Supported. The row does not claim 29/29. The 28/29 result and its explanation are in the report (:78-81, :229).
- "the zero-hit grep the entry cites at :2402": worker1 E3 :96 and :102. :2402 is the line that carries the zero-hit claim (Check 2). Supported.
- Over-claim probe: the row states no result and implies no audit (grep exit 1).

Column format: rows :469 and :470 have the same 7-field pipe structure as :468 (NF=7). The fields are a leading-slash `/docs/reports/...` path, `Report`, `3`, `2026-11-13`, and a description ending ` |`. Neither description contains a stray `|`, or NF would exceed 7.

No break.

### Check 4: no o4-parity-manager in DECISIONS.md :2389-2416

```
$ sed -n '2389,2416p' DECISIONS.md | grep -n o4-parity-manager; echo exit=$?
exit=1
$ grep -n o4-parity-manager DECISIONS.md; echo exit=$?
exit=1
```

Findings: no hit in the range (grep exit 1, no output), and no hit anywhere in DECISIONS.md. No break.

## Grades

Check 1: PASS
Check 2: PASS
Check 3: PASS
Check 4: PASS

Observation (not graded as a defect): the unit id `2026-11-13-o4-reduce3` in both rows comes from the report filenames; neither report spells it out. This is the same convention as row :468.

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
