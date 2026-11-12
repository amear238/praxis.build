# Unit 2026-11-12-mffu-prepurchase-filing-resume (Unit 2R) — worker 2, adversarial re-check

## Task

ADVERSARIAL, one re-check round. Artifact `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md` (477 lines), compared against the pre-edit copy `/tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md`. The job: decide whether the three findings in `docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md` "## Findings" are cured, check that no other byte changed beyond the two pointer lines, and run checks 1-7 from the brief. Read-only except this file. Baseline HEAD `ee54344`. Rubric lines in play: S1, S2, S8, S13, F4 (FROZEN).

## Checks run

### Check 1 — diff and sha256

```
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse --short HEAD && wc -l docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md && shasum -a 256 /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md && diff /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; echo "diff exit $?"
ee54344
     477 docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
     475 /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
     952 total
61e980e033014b226f69d9b80570b6405940b1fcf9e9c0684359599dac977840  /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
52a2d7967c4336fb51b5f0ec1e0c962cad5cdbda9345542517e60bbc164d8d66  docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
80c80
< ... Reading "does not cross the daily close" as "not overnight" needs a link between the two. Two texts on disk bear on that link: design :25's gloss, which the design itself grades INFERRED ("(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."), and R1 point 4's clause "the policy distinguishes between holding within a session versus holding through the daily close" (input :23, REPORTED BY). Neither says in terms that such a hold is not overnight. ...
---
> ... Reading "does not cross the daily close" as "not overnight" needs a link between the two. Texts on disk that bear on that link include design :25's gloss, which the design itself grades INFERRED ("(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."), design :110's "is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets" (quoted above), and R1 point 4's clause "the policy distinguishes between holding within a session versus holding through the daily close" (input :23, REPORTED BY). None of them says in terms that such a hold is not overnight. ...
93c93
< ... `Account.Name` is on 7 lines, by `grep -c`). So R2 point 3 alone ...
---
> ... `Account.Name` is on 7 lines, by `grep -c`, with 8 occurrences, by `grep -oF` piped to `wc -l`). So R2 point 3 alone ...
150c150
< (pending worker2)
---
> (manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
158c158
< (pending worker2)
---
> (manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
449a450,451
> $ grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '
> 8
458c460
< - OPEN-1, R6 design :110 (`bf6fcc7`): "no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
---
> - OPEN-1, R6 design :110 (`bf6fcc7`), in full: ""Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
diff exit 1
```

(Lines 80 and 93 are long. In the paste above I cut the parts that are identical in both versions and marked each cut with "..."; the raw diff printed the full lines. Every changed span is shown whole.)

There are six hunks. :80 cures resume-worker1 F1. :93 together with :450-451 cures F3. :460 cures F2. :150 and :158 are the two pointer lines. Nothing changed outside the cures and the pointers. The pointer target `docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md` does not exist yet (`ls` printed "No such file or directory"), which is expected: the resume manager writes it. The pointers stay unresolved until it does.

### Check 2 — are resume-worker1's three findings cured

Sources and the artifact's :79:

```
$ cd /Volumes/Sensidine/Praxis.build && git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '25p;110p'; echo ---INPUT23; sed -n '23p' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
---INPUT23
 I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close.
```

A script checks each :80 quote against its source and byte-compares the Q1 bullet with field 3 of design :110 (script at `/tmp/w2r-scripts/q.py`, run with `python3 -I`):

```
$ python3 -I /tmp/w2r-scripts/q.py
art460 starts: - OPEN-1, R6 design :110 (`bf6fcc7`), in
design25 in_artifact80= True in_source= True
design110 in_artifact80= True in_source= True
input23 in_artifact80= True in_source= True
field3 repr: '"Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use.'
Q1 bullet quote == field3: True len 236 236
field3 sha256 vs quote sha256:
6617635f1013e991d7b3b31446a87e3c6b8b066e75015765d76f4209d7e2c35a
6617635f1013e991d7b3b31446a87e3c6b8b066e75015765d76f4209d7e2c35a
```

- **F1 (MAJOR, :80): cured.** "Two texts on disk bear on that link" became "Texts on disk that bear on that link include". That is non-exhaustive, so the false count is gone and no new count was added. Design :110's clause is now named, and every quote is byte-exact in its source (script above). I tested "None of them says in terms that such a hold is not overnight." against each text. Design :25 never mentions an evening hold. Input :23 says it "cannot confirm". Design :110 is the closest: it says the 18:05→08:25 hold "meets" the FAQ gloss of "Holding overnight will breach", but it never says in terms that the hold is not overnight, and the same line concedes "no MFFU text says it in terms of an evening entry". So the sentence holds literally. NO BREAK, but a narrow pass on design :110.
- **F2 (MINOR, Q1 OPEN-1 bullet): cured.** The quote is now byte-identical to field 3 of design :110: same length (236), same sha256. The "in full" label is true.
- **F3 (MINOR, :93): cured.** The re-run matches the paste at :448-451 (7 lines, 8 occurrences, accounttype 0):

```
$ cd /Volumes/Sensidine/Praxis.build && grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs; grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '; grep -c -i "accounttype" ninjascript/PraxisSignalConsumer.cs; echo "exit $?"; git status --short ninjascript/PraxisSignalConsumer.cs; echo "status-done"
7
8
0
exit 1
status-done
$ cd /Volumes/Sensidine/Praxis.build && grep -cF "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
```

The artifact's E9 paste (from `sed -n '440,477p'`):

```
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
$ grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '
8
```

The consumer file has no working-tree change, so the re-run measures the same file the paste did.

### Check 3 — is the rest of the artifact consistent with the edits

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; sed -n '147p' $F | grep -o -F -e 'G9 now names both texts that bear on the link' -e 'says neither states it in terms'; sed -n '80p' $F | grep -o -F -e 'Texts on disk that bear on that link include' -e 'None of them says in terms'; sed -n '93p' $F | grep -o -F '`Account.Name` is on 7 lines, by `grep -c`'
G9 now names both texts that bear on the link
says neither states it in terms
Texts on disk that bear on that link include
None of them says in terms
`Account.Name` is on 7 lines, by `grep -c`
```

Full line :147, from `sed -n '138,162p'`:

```
2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms.
```

- :147 (worker2 disposition 2) says, in the present tense, that G9 "now names both texts that bear on the link" and "says neither states it in terms". G9 at :80 now names three texts, as a non-exhaustive "include", and says "None of them". So :147 no longer describes :80. It also repeats the exhaustive "both texts that bear on the link" count that resume-worker1 F1 refuted. This is Finding 1 below.
- :148 (disposition 3, "reworded to "is on 7 lines, by `grep -c`"") is still true: the quoted string is at :93 verbatim (output above), and adding "8 occurrences" does not contradict it. No finding.
- :106 (disposition 4) and its E9 evidence still hold:

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; grep -v '^\$ ' $F | grep -c -F 'Whether that text is the written MFFU answer design :110 asks for is Q1.'; grep -v '^\$ ' $F | grep -c -F 'That is the gap design :110 names'
1
0
```

These match the artifact's pasted 1 and 0 at :124 and :126.

### Check 4 — S13 sentence and pending count

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; S=$(grep -o -E 'Fills are optimistic[^|`"]*assumed\.' specs/SPEC_RUBRIC.md | head -1); echo "S13 length ${#S}"; echo "exact-line count: $(grep -cxF "$S" $F)"; echo "substring count: $(grep -cF "$S" $F)"; echo "on line: $(grep -nF "$S" $F | cut -d: -f1)"; echo "total lines: $(wc -l < $F | tr -d ' ')"; echo "last line is S13: $(tail -n 1 $F | grep -cxF "$S")"; echo "pending: $(grep -cF '(pending worker2)' $F)"; echo "prefix-hit lines: $(grep -n 'Fills are optimistic' $F | cut -d: -f1 | tr '\n' ' ')"; echo "prefix-hit lines in pre-edit copy: $(grep -n 'Fills are optimistic' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md | cut -d: -f1 | tr '\n' ' ')"
S13 length 90
exact-line count: 1
substring count: 1
on line: 477
total lines: 477
last line is S13: 1
pending: 0
prefix-hit lines: 141 242 477 
prefix-hit lines in pre-edit copy: 141 242 475 
```

The full sentence appears once, on line 477 of 477, which is the last line. This re-run does not print the sentence itself, so this report carries it only once. Lines 141 and 242 hold prefix fragments inside pasted commands and outputs; both were in the pre-edit copy (as 141 and 242). "(pending worker2)" occurs 0 times. PASS.

### Check 5 — email addresses and the rep's name

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; RE='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; CTRL=$(printf '%s@%s.%s' probe example com); echo "$CTRL" | grep -cE "$RE"; grep -cE "$RE" $F; echo "exit $?"; grep -cE "$RE" docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
1
0
exit 1
0
```

To find a rep-name candidate I grepped the input and the prior worker reports. The input writes the rep as `[rep]` (input :14, :30). The only rep name on disk is the 4-character token in the evidence PNG's filename, which I built at runtime and do not print:

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; TOK=$(ls docs/reports/evidence | grep mffu | head -1 | sed 's/.*mffu-//; s/-reply.*//'); echo "token length ${#TOK}"; echo "artifact hits: $(grep -ci -- "$TOK" $F)"; echo "control: $(printf 'z%sz\n' "$TOK" | grep -ci -- "$TOK")"; echo "input hits: $(grep -ci -- "$TOK" docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md)"; echo "[rep] in artifact: $(grep -oF '[rep]' $F | wc -l | tr -d ' ')"; grep -o -E '\b[A-Z][a-z]{2,}\b' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | sort -u | tr '\n' ' '
token length 4
artifact hits: 0
control: 1
input hits: 0
[rep] in artifact: 6
All Amear Authority Automated Automation Both Builder Channel Claude Eastern Email Evaluation Fair Fills Five For Funded Gmail High Holding However Inactivity Live Messages Not Our Overnight Play Positions Praxis Pre Pro Rapid Running Sim Simulation Standard Standing Thank The This Tier Time Verbatim When Whether Written Your
```

The only personal name among the input's capitalized words is the trader's own. PASS.

### Check 6 — S8 in the Questions section

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; Q2="Q2. Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing?"; echo "Q2 exact-line hits: $(grep -cxF -- "$Q2" $F)"; grep -n -E '^Q[0-9]+\.' $F | cut -c1-14; echo "lean words in Q section:"; sed -n '452,476p' $F | grep -n -i -E 'recommend|suggest|should (close|be|change|stay)|prefer|propos|lean|advis|we think|likely|clearly|plainly|therefore|so it|closes OPEN|does close|does not close OPEN' ; echo "lean exit $?"; echo "F4 MET/unfrozen:"; grep -n -i -E 'F4[^.]{0,80}\b(is MET|now MET|MET\b|unfrozen|thaw|satisfied|cleared)' $F | cut -c1-200; grep -n -i -E 'unfroz|thaw' $F; echo "f4 exit $?"
Q2 exact-line hits: 1
456:Q1. Does M
467:Q2. Should
lean words in Q section:
12:- DECISIONS.md:2131 ("V3 as clarified by V5", E9): "evening entries stand on MFFU's written answer"; "V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1".
lean exit 0
```

(This was one command run. Its F4 half printed the output shown under Check 7.)

The only lean-word hit is a verbatim DECISIONS.md quote that was already there before this unit. Q2's line is exact. I read the Q1 fact list in full (`sed -n '440,477p'`, quoted in Check 2). The design :110 bullet now includes "which an 18:05→08:25 hold meets", which points toward closing. It also includes "A written MFFU answer is needed before any funded use". Facts on the other side are still present: input :23 in full ("I cannot confirm"), the absence of the word "overnight", DECISIONS:2131, and the automated-reply provenance. A verbatim full-field quote has no editorial selection, and the cure removed a selection that had dropped one side. The list has no recommendation and no answer, and it does not lean. PASS.

### Check 7 — F4 not claimed MET or unfrozen

```
$ cd /Volumes/Sensidine/Praxis.build && F=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; echo "F4 MET/unfrozen:"; grep -n -i -E 'F4[^.]{0,80}\b(is MET|now MET|MET\b|unfrozen|thaw|satisfied|cleared)' $F | cut -c1-200; grep -n -i -E 'unfroz|thaw' $F; echo "f4 exit $?"
F4 MET/unfrozen:
13:- F4 (FROZEN; Owner Amear): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." Graded in G-F4: stays FROZEN / NOT MET.
97:5. Rubric F4: G-F4, NOT MET.
338:$ sed -n 2172p DECISIONS.md | grep -o 'Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).'
339:Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).
389:> | /docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-mffu-prepurchase-filing: de-identification checks, grading of each MF
f4 exit 1
```

Every hit says FROZEN / NOT MET. "unfroz" and "thaw" have 0 hits. PASS.

## Findings

1. MINOR (S1-class accuracy defect; not S2, since no component's level is overstated), artifact :147. Worker2 disposition 2 says, in the present tense, "G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms." After this unit's :80 cure, G9 names three texts, as a non-exhaustive "include" (adding design :110's clause), and says "None of them". So :147 now misdescribes the artifact's own G9. It also keeps, in the report, the exhaustive "both texts that bear on the link" count that resume-worker1 F1 graded MAJOR and that :80 just removed. The :80 cure created this inconsistency. I grade it MINOR, not MAJOR, for three reasons: it is a disposition recording an earlier round; the governing text at :80 is correct and visible; and nothing downstream relies on :147. A reader holding resume-worker1's standard could argue MAJOR, because it is the same false count. Note on the fix: the unit's edit rule ("change no other byte") excludes :147, so curing it, for example by appending "(superseded at :80 by unit 2026-11-12-mffu-prepurchase-filing-resume: three texts, non-exhaustive)", needs the master's leave. Otherwise the resume-manager report should record it.

Checked with no break: the diff touches only the three cures and the two pointer lines (Check 1). All three resume-worker1 findings are cured, with byte-exact quotes and a re-run that matches the paste (Check 2). "None of them says in terms" holds for each named text, narrowly for design :110 (Check 2). :148 and :106 still hold (Check 3). The S13 sentence appears once, as the last line, and "(pending worker2)" appears 0 times (Check 4). Emails: 0 hits, control 1. Rep-name token: 0 hits, control 1 (Check 5). Q2 is exact and Q1/Q2 carry no recommendation or leaning (Check 6). F4 is never claimed MET or unfrozen (Check 7). Open dependency, not a finding: the pointer target file does not exist yet.

## Result: FAIL

The fail rests on Finding 1 alone, which is MINOR. If the manager accepts it as recorded-not-cured under the no-other-byte rule, every other check passes.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
