# Unit 2026-11-12-mffu-prepurchase-filing-resume (Unit 2R), manager report

## Task

Resume Unit 2 (MFFU pre-purchase filing). Its manager died before returning. Authority: DECISION_LOG.md rows 2026-11-12T02:41:00Z (Unit 2 dispatch, Amear's brief) and 2026-11-12T05:08:00Z (this resume, decided by master under D-2026-11-08-D D1); both pasted in V1. Brief:
1. Verify worker2's three findings against the unfinished manager report `docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md`.
2. Fix them by the smallest edit, and replace each "(pending worker2)" line with one pointer line.
3. Run one narrow adversary on the edits, with one re-check if it finds a MAJOR.
4. Write this report, and append MANIFEST rows.

The input file `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md` is not edited (V9). Nothing is staged or committed by this unit (V10). F4 stays FROZEN / NOT MET; nothing in this unit claims otherwise (V8).

## Rubric criteria addressed

- S1 "Every claim in a report has pasted command output, not a description of output." Every fact below cites a V-block.
- S2 "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." This unit changes no component. It edits report text only.
- S8 "No question that belongs to Amear is answered on his behalf." Q1 and Q2 stay open, with no recommendation (V7).
- S13: the standing sentence appears once, as the last line, in the artifact (V6) and in this report.
- F4 (FROZEN): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." NOT MET; unchanged (V8).

## Workers dispatched (id, mode, outcome)

| Worker | Agent id | Mode | Scope | Outcome |
|---|---|---|---|---|
| resume-worker1 | a905240ac77902b01 | ADVERSARIAL | The pre-edit diff, cure of worker2's 3 findings, pointer lines, S13, emails, rep name, Q1/Q2 leaning, F4 | FAIL: 1 MAJOR (:80), 2 MINOR (:458, :93) (V5) |
| resume-worker2 | af4bd4842123536da | ADVERSARIAL (the one re-check round) | Cure of resume-worker1's 3 findings, the diff, consistency, the same structural checks | FAIL: 1 MINOR (:147); all 3 resume-worker1 findings cured (V5) |

Both were read-only except for their own report files. Both reports end with the S13 sentence.

## Process log

1. Read the two authority rows (V1) and the rubric lines S1, S2, S8, S13, F4 (V1).
2. Saved the pre-edit copy to `/tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md` before any edit. Its sha256 matched the artifact's when copied (V2).
3. Worker2 graded a 471-line version of the artifact. The file on disk was 475 lines (V2). Located each finding by content. All three were already cured in the pre-edit file, and the dead manager had written their dispositions at :146-148 (V3). Q1 at pre-edit :460 is byte-identical to a bullet built by script from input :23 (V3). The only remaining work in the artifact was the two "(pending worker2)" lines (V2).
4. Replaced the two "(pending worker2)" lines with the pointer line (edit P below).
5. Dispatched resume-worker1. It found a MAJOR in the dead manager's :80 cure: "Two texts on disk bear on that link" is an exhaustive count, and it is false. The artifact's own :79 quotes design :110, which applies the FAQ gloss to the evening hold. I confirmed this myself (V4). I kept the MAJOR grade and fixed it (edit A). I also wrote the two MINOR fixes (edits B and C/E).
6. Dispatched resume-worker2 as the single re-check round. All three resume-worker1 findings are cured (V5). Its one MINOR was :147, a disposition that my edit A had made stale. I fixed it without a second round, per the brief (edit D).
7. Wrote this report and appended three MANIFEST rows (V11).

Deviations from the brief's literal text, for the master:
- Edit E adds 2 lines to the artifact's E9 evidence block. The brief asked for "7 lines, 8 occurrences" at :93, and S1 needs a paste for "8". Before this edit, the artifact pasted only the `grep -c` line count.
- Edit D changes :147. It is outside the brief's "change no other byte" list, but the brief also says "Write MINOR fixes without a second round". Without the edit, :147 would state a false count about :80. The dead manager's original sentence is kept, and a superseded note is appended.
- The worker2 dispositions at :146 and :148 are unchanged. Both remain true (V3, V5).
- MANIFEST.md's working-tree diff also carries 8 rows from 2026-11-08/09 that are not this unit's. Unit 2's four rows come last, then this unit's three (V11).

## Edits to the artifact, itemised (before = pre-edit copy, after = current file)

Edit P, pointer lines (pre-edit :150 and :158; current :150 and :158):
```text
$ sed -n '150p;158p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
(pending worker2)
(pending worker2)
$ sed -n '150p;158p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)
```

Edit A, G9 (:80, resume-worker1 F1 MAJOR). The count claim is replaced by "include". Design :110's clause is added (it is quoted at :79 and pasted at E2 :269). "Neither" becomes "None of them". The changed spans:
```text
$ sed -n '80p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md | grep -o -E 'Two texts on disk bear on that link: design :25.s gloss|INFERRED\)\."\), and R1 point 4.s clause|Neither says in terms that such a hold is not overnight\.'
Two texts on disk bear on that link: design :25's gloss
INFERRED)."), and R1 point 4's clause
Neither says in terms that such a hold is not overnight.
$ sed -n '80p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -o -E 'Texts on disk that bear on that link include design :25.s gloss|INFERRED\)\."\), design :110.s .{0,140}\(quoted above\), and R1 point 4.s clause|None of them says in terms that such a hold is not overnight\.'
Texts on disk that bear on that link include design :25's gloss
INFERRED)."), design :110's "is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets" (quoted above), and R1 point 4's clause
None of them says in terms that such a hold is not overnight.
```

Edit B, S6 item 1 (:93, resume-worker1 F3; the brief's "7 lines, 8 occurrences"):
```text
$ sed -n '93p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md | grep -o -E '.Account\.Name. is on 7 lines[^)]*\)'
`Account.Name` is on 7 lines, by `grep -c`)
$ sed -n '93p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -o -E '.Account\.Name. is on 7 lines[^)]*\)'
`Account.Name` is on 7 lines, by `grep -c`, with 8 occurrences, by `grep -oF` piped to `wc -l`)
```

Edit E, E9 evidence block (2 lines inserted after pre-edit :449, now :450-451). The command was run in this session; its output is in V3.
```text
$ sed -n '448,450p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
```
$ sed -n '448,452p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
$ grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '
8
```
```

Edit C, Q1 OPEN-1 bullet (pre-edit :458, current :460, resume-worker1 F2). It now quotes design :110's third `|`-separated field in full, copied by script from `git show bf6fcc7`:
```text
$ sed -n '458p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
- OPEN-1, R6 design :110 (`bf6fcc7`): "no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
$ sed -n '460p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
- OPEN-1, R6 design :110 (`bf6fcc7`), in full: ""Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
```

Edit D, worker2 disposition 2 (:147, resume-worker2 F1 MINOR). A superseded note is appended, and the original sentence is unchanged:
```text
$ sed -n '147p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms.
$ sed -n '147p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms. (Superseded at :80 by unit 2026-11-12-mffu-prepurchase-filing-resume: G9 now says the texts that bear on the link include design :25's gloss, design :110's clause and input :23's clause, and that none of them says it in terms.)
```

## Diff of the artifact against its pre-edit copy (full)

```text
$ diff /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; echo "diff_exit=$?"
80c80
< Graded against that wording (INFERRED): the input gives, as MFFU support's text, a statement that speaks of an evening entry in terms ("A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close."). Whether that text is the written MFFU answer design :110 asks for is Q1. What it does not do: it does not use the word "overnight" (E9: 0 hits on input :38-39), and does not say whether such a hold counts as holding overnight, which is how design :28, message 3 item (4) ("evening entry vs overnight", input :29) and the C3.3 draft's question 4 (E9: investigation :1444, "count as holding overnight?") put it. Reading "does not cross the daily close" as "not overnight" needs a link between the two. Two texts on disk bear on that link: design :25's gloss, which the design itself grades INFERRED ("(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."), and R1 point 4's clause "the policy distinguishes between holding within a session versus holding through the daily close" (input :23, REPORTED BY). Neither says in terms that such a hold is not overnight. R1 point 4, three minutes earlier, said the definition could not be confirmed and needed the team; R2 came 49 seconds after the request for a team review, and the channel reads it as an automated reply (INFERRED). Whether R2 point 4 closes OPEN-1 is not decided here; it is Q1.
---
> Graded against that wording (INFERRED): the input gives, as MFFU support's text, a statement that speaks of an evening entry in terms ("A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close."). Whether that text is the written MFFU answer design :110 asks for is Q1. What it does not do: it does not use the word "overnight" (E9: 0 hits on input :38-39), and does not say whether such a hold counts as holding overnight, which is how design :28, message 3 item (4) ("evening entry vs overnight", input :29) and the C3.3 draft's question 4 (E9: investigation :1444, "count as holding overnight?") put it. Reading "does not cross the daily close" as "not overnight" needs a link between the two. Texts on disk that bear on that link include design :25's gloss, which the design itself grades INFERRED ("(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."), design :110's "is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets" (quoted above), and R1 point 4's clause "the policy distinguishes between holding within a session versus holding through the daily close" (input :23, REPORTED BY). None of them says in terms that such a hold is not overnight. R1 point 4, three minutes earlier, said the definition could not be confirmed and needed the team; R2 came 49 seconds after the request for a team review, and the channel reads it as an automated reply (INFERRED). Whether R2 point 4 closes OPEN-1 is not decided here; it is Q1.
93c93
<    What R2 point 3 would mean for the guard if accurate, INFERRED: it describes the connection's account-type property; the guard reads the account name, not that property (E9: `accounttype` occurs 0 times in the consumer; `Account.Name` is on 7 lines, by `grep -c`). So R2 point 3 alone does not show whether the guard would admit or refuse an MFFU account. If an MFFU account under a "Simulation" connection had a name starting with "sim" in any letter case (the comparison is OrdinalIgnoreCase), the guard would admit it with no code change, and the wall would no longer separate NT8's own simulation accounts from an MFFU account; if not, Correction 1's reading at :347 stands. No MFFU account name was observed by anyone in this unit (Amear has no account, input :10), so which case holds is UNVERIFIED. Nothing is decided; any change to the guard or to the order path to a funded account is D2(b), Amear's.
---
>    What R2 point 3 would mean for the guard if accurate, INFERRED: it describes the connection's account-type property; the guard reads the account name, not that property (E9: `accounttype` occurs 0 times in the consumer; `Account.Name` is on 7 lines, by `grep -c`, with 8 occurrences, by `grep -oF` piped to `wc -l`). So R2 point 3 alone does not show whether the guard would admit or refuse an MFFU account. If an MFFU account under a "Simulation" connection had a name starting with "sim" in any letter case (the comparison is OrdinalIgnoreCase), the guard would admit it with no code change, and the wall would no longer separate NT8's own simulation accounts from an MFFU account; if not, Correction 1's reading at :347 stands. No MFFU account name was observed by anyone in this unit (Amear has no account, input :10), so which case holds is UNVERIFIED. Nothing is decided; any change to the guard or to the order path to a funded account is D2(b), Amear's.
147c147
< 2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms.
---
> 2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms. (Superseded at :80 by unit 2026-11-12-mffu-prepurchase-filing-resume: G9 now says the texts that bear on the link include design :25's gloss, design :110's clause and input :23's clause, and that none of them says it in terms.)
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
diff_exit=1
```

## Adversarial findings

resume-worker1 (`docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md`):
1. MAJOR, :80, the false "Two texts" count. Confirmed by me (V4) and fixed by edit A. resume-worker2 found it cured (V5).
2. MINOR, :458, design :110 quoted mid-sentence with no marker, the same pattern as worker2's MAJOR. Fixed by edit C. resume-worker2 found it byte-identical (V5).
3. MINOR, :93, the brief's "8 occurrences" was missing. Fixed by edits B and E. resume-worker2's re-run matches the paste (V5).

resume-worker2 (`docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md`):
1. MINOR, :147, the disposition was stale after edit A. Fixed by edit D. There was no second round, per the brief. My own check of the fix is in V5b.

Negative tests (the gates used in this report do block). Each check is run on a mutated /tmp copy, and each returns the failing value (V12).

## S6 cross-block check

This unit decides nothing and changes no component. Edit B is the only edit inside the artifact's S6 section. It adds the occurrence count to S6 item 1, and the reasoning is unchanged: the guard reads `Account.Name`, which occurs 0 times as `accounttype` and 8 times on 7 lines. Which MFFU account name would be presented is still UNVERIFIED in the artifact. The guard and the order path stay D2(b), Amear's. F4 stays FROZEN / NOT MET (V8).

## Files staged

None by this unit. One file, `docs/reports/evidence/2026-10-28-mffu-[name]-reply.png` (name token masked), was already in the index at session start (gitStatus `A`). This unit did not touch it (V10). Working-tree changes by this unit:
- the artifact, edited as above;
- this report and the two resume-worker reports, all new and untracked;
- three MANIFEST rows appended (V11).

## Result

Result: PASS

The checks behind this: all three of worker2's findings were cured (pre-edit, V3). resume-worker1's MAJOR was cured and re-checked once (V5). The remaining MINORs were fixed (V5, V5b). Pointer lines: 2, and "pending worker2" occurs 0 times. S13 appears once, as the last line. Emails 0, rep-name token 0, Q2 line exact, no F4 MET claim (V6-V8). The three deviations listed in the Process log are for the master to accept or reverse. This grade is the manager's; the auditor's is separate.

## Verification evidence (command output)

V1, the authority rows (first 120 characters each) and the rubric lines:
```text
$ grep -n '2026-11-12T02:41:00Z\|2026-11-12T05:08:00Z' DECISION_LOG.md | cut -c1-120
849:- [2026-11-12T02:41:00Z] WHO: amear | REPORTED BY: the Claude.ai Praxis channel, in `docs/reports/2026-11-11-return-
850:- [2026-11-12T05:08:00Z] WHO: praxis-master | WHAT: **Session start (`claude -p`, pid 17658, cwd this tree) and drif
$ grep -n -E '^\| S1 \||^\| S2 \||^\| S8 \|' specs/SPEC_RUBRIC.md
124:| S1 | Every claim in a report has pasted command output, not a description of output. |
125:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
131:| S8 | No question that belongs to Amear is answered on his behalf. |
$ grep -n -E '^\| S13 \|' specs/SPEC_RUBRIC.md | cut -c1-60
136:| S13 | Every report under docs/reports/ and every DECIS
$ sed -n '48,50p' specs/SPEC_RUBRIC.md
### F4 — MFFU automation compliance
**Criterion.** Written confirmation from MFFU that this specific automation
pattern is permitted on a funded account.
```

V2, pre-edit copy, line counts, the worker2-graded length and the pre-edit pending lines:
```text
$ shasum -a 256 /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
61e980e033014b226f69d9b80570b6405940b1fcf9e9c0684359599dac977840  /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
$ wc -l /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
     475 /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
     477 docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
     952 total
$ grep -n -o -E 'total= +[0-9]+' docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md
83:total=     471
$ grep -n 'pending worker2' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
150:(pending worker2)
158:(pending worker2)
```

V3, worker2's findings were already cured in the pre-edit file. Q1's bullet is byte-compared against input :23, and the E9 paste is re-run:
```text
$ Q=$(sed -n '23p' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | sed 's/^ //'); L=$(sed -n '460p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md); [ "$L" = "- The earlier reply, input :23, in full: \"$Q\"" ] && echo IDENTICAL || echo DIFFERS
IDENTICAL
$ grep -c -F 'from our team".' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md
1
$ sed -n '93p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md | grep -o -E '.Account\.Name. is on 7 lines, by .grep -c.'
`Account.Name` is on 7 lines, by `grep -c`
$ grep -c 'Account.Name' ninjascript/PraxisSignalConsumer.cs
7
$ grep -oF 'Account.Name' ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '
8
$ sed -n '146,148p' /tmp/2026-11-12-mffu-prepurchase-filing-manager.preedit.md | cut -c1-110
1. MAJOR (S8 leaning), Q1's quote of input :23 stopped at "from our team" and dropped the clause tying "overni
2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both te
3. MINOR, "`Account.Name` occurs 7 times" is a line count. Disposition: reworded to "is on 7 lines, by `grep -
```

V4, the resume-worker1 MAJOR confirmed. The artifact's :79 quotes design :110's application of the gloss, and the source lines are shown:
```text
$ sed -n '79p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -o -F 'which an 18:05→08:25 hold meets'
which an 18:05→08:25 hold meets
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '25p;110p'
- (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
$ sed -n '1379p' docs/reports/2026-11-11-mffu-connection-investigation.md | cut -c1-200
| R2 | Holding overnight breaches the account | **OBSERVED** (MFFU page), plan-specific wording | Rapid FAQ: "All positions must be closed before the daily session close. Holding overnight will breach
```

V5, the adversary results (headings and finding lines from their report files):
```text
$ grep -n -E '^## Result' docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md
docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md:281:## Result: FAIL
docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md:209:## Result: FAIL
$ sed -n '/^## Findings/,/^## Result/p' docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md | grep -E '^[0-9]\.' | cut -c1-110
1. MAJOR (S1 / S2 drift; brief "no new claim"; worker2 finding 2 not cured), artifact :80. "Two texts on disk 
2. MINOR (S8 drift; quote truncation with no marker), artifact :458. Q1's OPEN-1 bullet quotes design :110 fro
3. MINOR (brief deviation, not a rubric breach), artifact :93. The brief asked for "7 lines, 8 occurrences". T
$ sed -n '/^## Findings/,/^## Result/p' docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md | grep -E '^([0-9]\.|Checked with no break)' | cut -c1-200
1. MINOR (S1-class accuracy defect; not S2, since no component's level is overstated), artifact :147. Worker2 disposition 2 says, in the present tense, "G9 now names both texts that bear on the link (
Checked with no break: the diff touches only the three cures and the two pointer lines (Check 1). All three resume-worker1 findings are cured, with byte-exact quotes and a re-run that matches the past
```

V5b, my checks of edits A, C and D against their sources (run after the last edit):
```text
$ C=$(git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | sed -n '110p' | awk -F' \\| ' '{print $3}'); L=$(sed -n '460p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md); [ "$L" = "- OPEN-1, R6 design :110 (\`bf6fcc7\`), in full: \"$C\"" ] && echo IDENTICAL || echo DIFFERS
IDENTICAL
$ sed -n '79p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -c -F '"Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets'
1
$ sed -n '80p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -c -E 'Texts on disk that bear on that link include design :25.s gloss.*design :110.s.*R1 point 4.s clause.*None of them says in terms'
1
$ grep -c -F 'Two texts on disk' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
0
$ sed -n '147p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -o -E '\(Superseded at :80.*\)'
(Superseded at :80 by unit 2026-11-12-mffu-prepurchase-filing-resume: G9 now says the texts that bear on the link include design :25's gloss, design :110's clause and input :23's clause, and that none of them says it in terms.)
```

V6, pointer lines and S13 in the artifact:
```text
$ grep -c 'pending worker2' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
0
$ grep -n -F '(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | cut -d: -f1
150
158
$ S=$(grep -o -E 'Fills are optimistic[^|`"]*assumed\.' specs/SPEC_RUBRIC.md | head -1); echo "count=$(grep -cF -- "$S" docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md) last_line_exact=$(tail -n1 docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -cxF -- "$S") total=$(wc -l < docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | tr -d ' ')"
count=1 last_line_exact=1 total=477
```

V7, S8: the Q2 line is exact, there is no recommendation wording in the Questions section, and there are no email addresses or rep-name token (the patterns are built at runtime, each with a positive control):
```text
$ grep -c -x -F "Q2. Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing?" docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
1
$ sed -n '/^## Questions for Amear/,$p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | grep -c -i -E 'recommend|should close|we suggest|advise|propose'
0
$ RX='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'; P=$(printf '%s%s%s' probe.user '@' example.org); printf '%s\n' "$P" | grep -cE "$RX"; grep -cE "$RX" docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
1
0
$ N=$(basename docs/reports/evidence/2026-10-28-mffu-*-reply.png .png | cut -d- -f5); echo "len=${#N}"; printf 'x %s y\n' "$N" | grep -ciw -- "$N"; grep -ciw -- "$N" docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
len=4
1
0
```

V8, F4 in the artifact:
```text
$ grep -n -i -E 'F4[^.]{0,40}(is|now) (met|unfrozen)' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md; echo "grep_exit=$?"
grep_exit=1
$ grep -c -F 'F4 stays FROZEN' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
2
```

V9, the input is unedited (its sha256 now, against the value the artifact recorded at E1 and E8):
```text
$ shasum -a 256 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ grep -n -o -E '^[0-9a-f]{64}  docs/reports/2026-11-11-return-handoff' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
208:9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff
405:9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff
```

V10, git state (HEAD, index, status of the unit's files):
```text
$ git rev-parse --short HEAD
ee54344
$ git diff --cached --name-status | sed -E 's/mffu-[a-z]+-reply/mffu-[name]-reply/'
A	docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
$ git status --porcelain -- MANIFEST.md docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md
 M MANIFEST.md
?? docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
?? docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
?? docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md
?? docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md
?? docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md
```

V11, MANIFEST rows (the last 7 rows, path column only; the count of rows added against HEAD):
```text
$ tail -n 7 MANIFEST.md | cut -d'|' -f2
 /docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker1.md 
 /docs/reports/2026-11-12-mffu-prepurchase-filing-resume-worker2.md 
$ git diff HEAD -- MANIFEST.md | grep -c '^+|'
15
```

V12, negative tests: each check run against a mutated /tmp copy returns the failing value:
```text
$ head -n 476 docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md > /tmp/r2r/neg-nos13.md; S=$(grep -o -E 'Fills are optimistic[^|`"]*assumed\.' specs/SPEC_RUBRIC.md | head -1); echo "count=$(grep -cF -- "$S" /tmp/r2r/neg-nos13.md) last_line_exact=$(tail -n1 /tmp/r2r/neg-nos13.md | grep -cxF -- "$S")"
count=0 last_line_exact=0
$ sed '462s/from our team, as the policy/from our team/' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md > /tmp/r2r/neg-trunc.md; Q=$(sed -n '23p' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | sed 's/^ //'); L=$(sed -n '462p' /tmp/r2r/neg-trunc.md); [ "$L" = "- The earlier reply, input :23, in full: \"$Q\"" ] && echo IDENTICAL || echo DIFFERS
DIFFERS
$ Q=$(sed -n '23p' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | sed 's/^ //'); L=$(sed -n '462p' docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md); [ "$L" = "- The earlier reply, input :23, in full: \"$Q\"" ] && echo IDENTICAL || echo DIFFERS
IDENTICAL
$ printf '(pending worker2)\n' > /tmp/r2r/neg-pending.md; grep -c 'pending worker2' /tmp/r2r/neg-pending.md
1
```

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
