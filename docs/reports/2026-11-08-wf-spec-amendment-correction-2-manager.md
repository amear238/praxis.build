Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

# Manager report — unit 2026-11-08-wf-spec-amendment-correction-2 (cures U7 audit FAIL 1)

Date 2026-11-08. Manager: praxis-manager. HEAD `6c4c109`, branch `main`. Nothing was staged or committed. Ungraded: the master's auditor grades this.

## Task

Cure the four findings of U7's audit FAIL 1, recorded in DECISION_LOG row `2026-11-08T17:08:00Z` (WHO: praxis-master). The method was fixed by the master's brief. (A) Append "Correction 1" to `docs/reports/2026-11-08-wf-spec-amendment-manager.md` (the U7 report). (B) Make in-place label edits on values spec lines 5, 93 and 135, and on WF spec lines 28 and 107. (C) Append two MANIFEST rows. (D) Run one adversary. Nothing else.

The ledger row, first 400 characters (`grep '2026-11-08T17:08:00Z' DECISION_LOG.md | head -c 400`):

```
- [2026-11-08T17:08:00Z] WHO: praxis-master | WHAT: **AUDIT (U7, `commit-idx-u7`) — FAIL 1 (11 tool uses, ~3 min). Hash `5f7b8d2f…c9c4` and numstat reproduced. PASS on S2, S5, S6, S8, S13, quote fidelity (A1–A5, A7, A8, R1–R3 character-for-character), line stability (349/349, 224/224), pointers, ledger flush, MANIFEST, S6-in-report, de-identification, as-is excluded, standing sentence. FAI
```

## Rubric criteria addressed

Lines from `specs/SPEC_RUBRIC.md` (`grep -nE '\bS(1|2|8|13) *\|'`; S13 cut at 400 characters by the capture):

```
115:| S1 | Every claim in a report has pasted command output, not a description of output. |
116:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
122:| S8 | No question that belongs to Amear is answered on his behalf. |
127:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the sentence on line 1 of this report] Reports with no such figure carry it too, as house style, until the void clause of D-2026-10-30-A fires. Settled under R-1104-2 on 2026-11-06 (D-20
```

(The S13 line above has the quoted sentence replaced with a bracketed pointer. Otherwise this report would carry the sentence twice. The live line also continues past what the brief quoted: "Settled under R-1104-2 …".)

- S1: finding 1 (the U7 report's :16, :20, :64, :69, :70 and the stale diff paste). Re-run outputs or retractions are in Correction 1, U7 report :449 onward.
- S8 / S2: findings 2 and 3, the labels "changeable by Amear" and OPEN.
- S4 (finding 4): Correction 1 quotes the master's answer only.
- S13: line 1 of this report. The U7 report still carries the exact sentence once (pasted below).

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| abaf4a488d863abe1 | ADVERSARIAL | GRADE: REFUTED. 1 MAJOR: this report did not yet exist, cured by writing it (below). 3 MINOR, disclosed. Closing block pasted under Adversarial findings. |

No BUILD worker. The manager made all edits: six exact-once string inserts, one append and one two-row append. The brief fixed every inserted string, so there was nothing to decompose.

## Process log

1. Read the rubric and the ledger row (pasted above). Took baseline captures (pasted below). Copied both specs, MANIFEST.md and the U7 report into `scratchpad/before/` before any edit.
2. (B) Ran `scratchpad/edit.py`, a line-scoped exact-once replace. It aborts unless the anchor occurs once in its line and once in the file (output pasted). Placement of " (OPEN, Q9)":
   - WF :107: the only "tier pick stays Q9" is inside the A4 quote. The label goes after that quote's closing mark (`…equity-base item." (OPEN, Q9)`).
   - Values :135: the phrase occurs three times (pre-edit grep pasted). Two are inside quotes: A4's ruling and `(his words "tier pick stays Q9")`. One is the editor's own unquoted sentence, "Tier pick stays Q9" (capital T). The label went directly after that unquoted occurrence, outside all of his words.
3. (C) Appended MANIFEST rows 302–303 in the 5-cell format of rows 299–301.
4. (A) Re-ran the U7 commands, generating each paste block to a file. Captured the diff of record after (B). Assembled Correction 1 from a template, filling in the quotes from the pre-edit copy of the U7 report. Appended it once.
5. (D) Ran one adversary. Wrote this report.

Memory line in place of an agent-memory write (brief rule): *the values spec :135 has the phrase "tier pick stays Q9" three times, two quoted and one the editor's; a "label after the phrase" brief needs every occurrence classified first.*

## Verification evidence

### Baseline (before any edit)

```
$ wc -l <values> <WF> <U7 report> MANIFEST.md
     349 docs/specs/2026-11-06-walk-forward-values.md
     224 docs/specs/2026-11-05-walk-forward-spec.md
     448 docs/reports/2026-11-08-wf-spec-amendment-manager.md
     301 MANIFEST.md
    1322 total
$ git diff --numstat HEAD -- <values> <WF> MANIFEST.md <U7 report>
3	0	MANIFEST.md
5	5	docs/specs/2026-11-05-walk-forward-spec.md
20	20	docs/specs/2026-11-06-walk-forward-values.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ head -n 448 docs/reports/2026-11-08-wf-spec-amendment-manager.md | openssl dgst -sha256
SHA2-256(stdin)= fee64ca8cf93b3817de72322bae166bd205d42060d928ee390be09005215a600
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 298 MANIFEST.md); echo cmp rc $?
cmp rc 0
$ git ls-files --error-unmatch docs/reports/2026-11-08-wf-spec-amendment-manager.md 2>&1 | tail -1
Did you forget to 'git add'?
```

The U7 report is untracked. So `git diff --numstat HEAD` prints no row for it, before or after. Its stability is shown by the hash and `cmp` instead.

### (B) Anchor strings, pre-edit

```
# run in scratchpad/before (pre-edit copies)
$ grep -n -o "Label (the editor's, from A3's words[^:]*" 2026-11-06-walk-forward-values.md
135:Label (the editor's, from A3's words)
$ grep -n -o '(A5, first half)' 2026-11-06-walk-forward-values.md
5:(A5, first half)
$ grep -n -o 'and nothing is assumed about that definition here\.' 2026-11-06-walk-forward-values.md
93:and nothing is assumed about that definition here.
$ grep -n -o -i 'tier pick stays Q9[^ ]*' 2026-11-06-walk-forward-values.md 2026-11-05-walk-forward-spec.md
2026-11-06-walk-forward-values.md:135:tier pick stays Q9.
2026-11-06-walk-forward-values.md:135:Tier pick stays Q9
2026-11-06-walk-forward-values.md:135:tier pick stays Q9").
2026-11-05-walk-forward-spec.md:107:tier pick stays Q9.
$ grep -n -o "is the editor's reading, not his words[^ ]*" 2026-11-05-walk-forward-spec.md
28:is the editor's reading, not his words;
```

### (B) Edit run

```
$ python3 -I scratchpad/edit.py
2026-11-06-walk-forward-values.md 5 count_in_line 1 count_in_file 1
2026-11-06-walk-forward-values.md 93 count_in_line 1 count_in_file 1
2026-11-06-walk-forward-values.md 135 count_in_line 1 count_in_file 1
2026-11-06-walk-forward-values.md 135 count_in_line 1 count_in_file 1
2026-11-05-walk-forward-spec.md 28 count_in_line 1 count_in_file 1
2026-11-05-walk-forward-spec.md 107 count_in_line 1 count_in_file 1
done
```

### (A) Append proof for the U7 report

```
$ head -n 448 docs/reports/2026-11-08-wf-spec-amendment-manager.md | openssl dgst -sha256   # before append
SHA2-256(stdin)= fee64ca8cf93b3817de72322bae166bd205d42060d928ee390be09005215a600
$ head -n 448 docs/reports/2026-11-08-wf-spec-amendment-manager.md | openssl dgst -sha256   # after append
SHA2-256(stdin)= fee64ca8cf93b3817de72322bae166bd205d42060d928ee390be09005215a600
$ cmp /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dac8a676-3ed6-4fca-96a1-deecc90b3c48/scratchpad/before/2026-11-08-wf-spec-amendment-manager.md <(head -n 448 docs/reports/2026-11-08-wf-spec-amendment-manager.md); echo "rc $?"
rc 0
$ wc -l docs/reports/2026-11-08-wf-spec-amendment-manager.md
     627 docs/reports/2026-11-08-wf-spec-amendment-manager.md
# the two checks below were re-run with variable patterns, so that this report does not carry the sentence or the banned strings itself
$ SENT=$(head -n 1 docs/reports/2026-11-08-wf-spec-amendment-manager.md)   # line 1 of the U7 report is the standing sentence
$ grep -cF "$SENT" docs/reports/2026-11-08-wf-spec-amendment-manager.md
1
$ BANNED=$(printf 'V%sDICT|COMMIT-IN%sX|COMMIT-DIFF-SHA%s' ER DE 256)
$ grep -ciE "$BANNED" <(tail -n +449 docs/reports/2026-11-08-wf-spec-amendment-manager.md)
0
```

The "before append" hash equals the baseline hash above (`fee64ca8…a600`). Lines 1–448 are byte-identical (`cmp` rc 0).

### (C) MANIFEST

```
$ wc -l MANIFEST.md
     303 MANIFEST.md
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 298 MANIFEST.md); echo "cmp HEAD vs head-298 rc $?"
cmp HEAD vs head-298 rc 0
$ cmp <(sed -n '299,301p' before/MANIFEST.md) <(sed -n '299,301p' MANIFEST.md); echo "cmp 299-301 rc $?"
cmp 299-301 rc 0
$ cmp before/MANIFEST.md <(head -n 301 MANIFEST.md); echo "cmp before vs head-301 rc $?"
cmp before vs head-301 rc 0
$ sed -n '302,303p' MANIFEST.md | awk -F'|' '{print NR+301, "NF="NF}'
302 NF=7
303 NF=7
```

### After state: line counts, numstat, staged stat, untouched-line proof, labels

```
$ wc -l <both specs> <U7 report> MANIFEST.md   # after
     349 docs/specs/2026-11-06-walk-forward-values.md
     224 docs/specs/2026-11-05-walk-forward-spec.md
     627 docs/reports/2026-11-08-wf-spec-amendment-manager.md
     303 MANIFEST.md
    1503 total
$ git diff --numstat HEAD -- <values> <WF> MANIFEST.md <U7 report>   # after
5	0	MANIFEST.md
5	5	docs/specs/2026-11-05-walk-forward-spec.md
20	20	docs/specs/2026-11-06-walk-forward-values.md
$ git status --short <U7 report>
?? docs/reports/2026-11-08-wf-spec-amendment-manager.md
$ git diff --cached --stat | tail -1   # after
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ diff <(sed '5d;93d;135d' before/values) <(sed '5d;93d;135d' values); echo rc
rc 0
$ diff <(sed '28d;107d' before/WF) <(sed '28d;107d' WF); echo rc
rc 0
$ diff before/values values | grep -E "^[0-9]"; diff before/WF WF | grep -E "^[0-9]"; diff before/MANIFEST.md MANIFEST.md | grep -E "^[0-9]"
5c5
93c93
135c135
28c28
107c107
301a302,303
$ python3 -I strip.py <scratchpad>   # each edited line minus its inserted text == before line
2026-11-06-walk-forward-values.md 5 after-minus-inserts == before: True len before/after 1292 1310
2026-11-06-walk-forward-values.md 93 after-minus-inserts == before: True len before/after 1628 1694
2026-11-06-walk-forward-values.md 135 after-minus-inserts == before: True len before/after 1749 1781
2026-11-05-walk-forward-spec.md 28 after-minus-inserts == before: True len before/after 568 589
2026-11-05-walk-forward-spec.md 107 after-minus-inserts == before: True len before/after 874 885
$ grep -o for each inserted label (after)
5:(A5, first half; second half OPEN)
93:A5's second half: OPEN (waits on a read of MFFU's current terms).
135:Label (the editor's, from A3's words, changeable by Amear)
135:Tier pick stays Q9 (OPEN, Q9) (his words "tier pick stays Q9")
28:is the editor's reading, not his words, changeable by Amear
107:equity-base item." (OPEN, Q9) The gate in force
$ tier pick status: grep -n -o on values :137 and :306
**The tier pick is OPEN** — his, after paper results.
1. **The tier pick**, after paper results (Q9: "I pick after paper results").
```

### The two "tier pick stays Q9" lines, both ways

WF spec :107 before:

```
- Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules its base: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used." (`:814`). — RULED (D-2026-11-05-A). **Amended by A4** (D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." The gate in force is A4's. The limit type and stage for the Studio Static rows and for rows whose Eval and Sim-Funded types differ are NEEDS AMEAR (ii) of D-2026-11-08-B (cf. this file's NEEDS AMEAR 12).
```

WF spec :107 after:

```
- Original Block 2 gate wording: "Max drawdown ≤ 4% of equity" (Phase 3 spec `:82`). Item 3 rules its base: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used." (`:814`). — RULED (D-2026-11-05-A). **Amended by A4** (D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." (OPEN, Q9) The gate in force is A4's. The limit type and stage for the Studio Static rows and for rows whose Eval and Sim-Funded types differ are NEEDS AMEAR (ii) of D-2026-11-08-B (cf. this file's NEEDS AMEAR 12).
```

Values spec :135 before:

```
- **Max-DD gate base** — RULED (A4, D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." In his words, it amends D-2026-11-05-A item 3 ("This amends D-2026-11-05-A item 3 with a safety buffer for model error.") and closes the notes-4 DD equity-base item ("Closes the notes-4 DD equity-base item."). Tier pick stays Q9 (his words "tier pick stays Q9"). OPEN: which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded limit types differ — NEEDS AMEAR (ii) of D-2026-11-08-B. was: "RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit."). It stands as written. Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that item stays OPEN (ruling 9; list (C))." **Win rate** — RULED (A3, D-2026-11-08-B, DECISIONS.md:1730–1734, joined): "Win rate is not a Block 2 pass gate. Per trade: W / (W + L + 0.5 x B), B = trade exited at its entry price. No-trade sessions excluded. It is the quantity for O4's Block 4 "within +/-15% win rate" check, computed identically on backtest and paper." Label (the editor's, from A3's words): not a Block 2 pass gate; the quantity for O4's Block 4 "within +/-15% win rate" check. Whether W and L are classified by price or by net P&L after commission and slippage: OPEN, NEEDS AMEAR (i) of D-2026-11-08-B.
```

Values spec :135 after:

```
- **Max-DD gate base** — RULED (A4, D-2026-11-08-B, DECISIONS.md:1735–1740, joined): "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit. This amends D-2026-11-05-A item 3 with a safety buffer for model error. Evaluated against every tier row; tier pick stays Q9. Closes the notes-4 DD equity-base item." In his words, it amends D-2026-11-05-A item 3 ("This amends D-2026-11-05-A item 3 with a safety buffer for model error.") and closes the notes-4 DD equity-base item ("Closes the notes-4 DD equity-base item."). Tier pick stays Q9 (OPEN, Q9) (his words "tier pick stays Q9"). OPEN: which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded limit types differ — NEEDS AMEAR (ii) of D-2026-11-08-B. was: "RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit."). It stands as written. Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that item stays OPEN (ruling 9; list (C))." **Win rate** — RULED (A3, D-2026-11-08-B, DECISIONS.md:1730–1734, joined): "Win rate is not a Block 2 pass gate. Per trade: W / (W + L + 0.5 x B), B = trade exited at its entry price. No-trade sessions excluded. It is the quantity for O4's Block 4 "within +/-15% win rate" check, computed identically on backtest and paper." Label (the editor's, from A3's words, changeable by Amear): not a Block 2 pass gate; the quantity for O4's Block 4 "within +/-15% win rate" check. Whether W and L are classified by price or by net P&L after commission and slippage: OPEN, NEEDS AMEAR (i) of D-2026-11-08-B.
```

## Adversarial findings

Worker abaf4a488d863abe1 (ADVERSARIAL). It was given the before copies, the live files, the four findings and the rubric lines, but not this manager's reasoning. Its closing block, verbatim (its trailing spoken-summary block is omitted: that block is barred from generated documents):

````
**Adversarial check of the U7 correction (unit correction-2).** I broke it in one place. The appended section cites a file that does not exist.

1. **MAJOR. A new claim in the cure section is false and its evidence is not pasted (S1).** U7 report :452, Basis line: "the `head -n 448` sha256, taken before and after, is pasted in `docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md`." MANIFEST row 303 lists the same file. It is not on disk:
```
$ ls -la docs/reports/2026-11-08-wf-spec-amendment-correction-*-manager.md
-rw-r--r--@ 1 admin staff 9508 Nov  8 12:02 docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md
ugrep: warning: docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md: No such file or directory
$ head -n 448 <U7 report> | shasum -a 256
fee64ca8cf93b3817de72322bae166bd205d42060d928ee390be09005215a600  -
```
I can't reproduce the "before" hash. My own `cmp` of lines 1–448 does pass (item 3). This is cured only if that manager report is later written with the matching paste.

2. **MINOR. WF :107: the label could be read as applying to a RULED sentence.** The text is `…tier pick stays Q9. Closes the notes-4 DD equity-base item." (OPEN, Q9) The gate in force is A4's.` The label sits after the closing quote, as the brief allows. But the sentence right before it, the DD equity-base closure, is RULED. Values :137 confirms the tier pick itself is OPEN ("**The tier pick is OPEN** — his, after paper results."), so the label is correct for the pick.

3. **NONE. No other line changed (attack B).** The `diff` of before against after shows only values 5c5, 93c93 and 135c135, WF 28c28 and 107c107, and MANIFEST `301a302,303`. Line counts are still 349, 224, 303 and 627. CR count is 0 in every file and each ends in `0a`. These all came back clean: `U7-448-identical`, `MAN301`, `MAN298HEAD`, and `12 files changed, 5726 insertions(+), 2 deletions(-)`.

4. **NONE. The pasted diff matches the live one.** My live `git diff -U0 HEAD` gives 76 lines. Raw sha256 is `deec1a46…d083` and stripped is `fb8251a1…5356`, the same as pasted. The pasted block (report :545–620) compared to my stripped diff with `cmp` gives `PASTED==LIVE_STRIPPED`. The sed's stated effect is correct: the cut fragment really is 80 characters long.

5. **NONE. The :16, :69 and :70 re-runs reproduce exactly.** Results: `1`, ` M DECISION_LOG.md`, `299–301 NF=7 pipes=6`, `2026-11-06T00:33:46Z`, `Nov  5 19:33:46 2026`, `MEMORY.md 2026-11-08T16:59:00Z`. The :64 retraction uses the required words. The :20 withdrawal is present. Each quoted line matches what the report actually says at :16, :20, :64, :69 and :70.

6. **NONE. The S4 quote is verbatim.** Running `grep -cF` for the blockquote text in DECISION_LOG.md gives `1` (row :739).

7. **NONE. The standing sentence appears once.** `grep -c` for the exact sentence in the report gives `1` (line 1). Report :199 holds an older truncated header fragment from lines 1–448, but not the full sentence.

8. **NONE. No label sits inside his words (attack C).** I counted ASCII double quotes before each inserted label: 2, 18, 6, 18, 8 and 6, all even. For values :93 I checked every pair, including the nested ones: the label at index 1081 comes after the last closing quote at 908. Neither spec file has curly quotes near the edits (only WF :161 has any).

9. **MINOR.** Correction :433 quotes the question cut short at "…DECISIONS.md entry" with no ellipsis. The original goes on with ": zero-insertion appends…".

10. **MINOR, outside the allowed edit lines.** Values :12 still says "Nothing else is open (list C)", which contradicts the new "A5's second half: OPEN" at :93.

GRADE: REFUTED — the cure section's Basis line cites a pasted sha256 in a correction-2 manager report that does not exist on disk.
````

Disposition:
- **1 (MAJOR): cured by this file.** This report now exists and pastes the `head -n 448` sha256 before and after: `fee64ca8…a600` both times, matching the adversary's own `shasum`. Writing this report is the cure, and no adversary re-attacked it.
- **2 (MINOR): not changed.** The placement is what the brief prescribes for a phrase inside his quoted words. Values :137 makes the tier pick OPEN (pasted above). The label can still be misread as applying to the A4 sentence it follows.
- **9 (MINOR): not changed.** Correction 1 quotes the first clause of :433 without an ellipsis, the same clause the 17:08:00Z row quotes. Editing my own appended text after the adversary's pass would itself need re-attacking.
- **10 (MINOR): outside this unit's lines.** See the S6 section and Does NOT cover.

## S6 cross-block check

These are cross-file effects of the new labels on the lines this unit may not touch:

```
$ grep -n -o 'Nothing else is open[^.]*' docs/specs/2026-11-06-walk-forward-values.md
12:Nothing else is open (list C)
$ grep -n -o -i "A5's second half[^.]*" docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
docs/specs/2026-11-06-walk-forward-values.md:93:A5's second half: OPEN (waits on a read of MFFU's current terms)
$ grep -c 'second half' docs/specs/2026-11-06-walk-forward-values.md docs/specs/2026-11-05-walk-forward-spec.md
docs/specs/2026-11-05-walk-forward-spec.md:0
docs/specs/2026-11-06-walk-forward-values.md:6
$ grep -n -o 'tier pick[^.;]*' docs/specs/2026-11-05-walk-forward-spec.md
107:tier pick stays Q9
$ grep -n -o -i 'editor.s reading[^;.]*' docs/specs/2026-11-05-walk-forward-spec.md | head
28:editor's reading, not his words, changeable by Amear
```

- Values :12 ("Nothing else is open (list C)") now sits beside :93's "A5's second half: OPEN". This unit may not edit :12, so the tension is left as found.
- U7 report :427 already records that list (C) gives A5's second half no OPEN grade. That is also not edited here.
- The WF spec has no other "tier pick" or "editor's reading" occurrence (grep above). No other WF line needed the same label.
- MANIFEST row 299 already says "A5's second half … stay open". That is consistent with the new :5 and :93 text.

## Files staged

None. This unit staged nothing (`git diff --cached --stat | tail -1` is unchanged, pasted above). These working-tree files were changed and left unstaged:
- `docs/specs/2026-11-06-walk-forward-values.md` (lines 5, 93, 135)
- `docs/specs/2026-11-05-walk-forward-spec.md` (lines 28, 107)
- `MANIFEST.md` (rows 302–303 appended)
- `docs/reports/2026-11-08-wf-spec-amendment-manager.md` (untracked; Correction 1 appended at :449–627)
- this report (new, untracked)

Nothing was written under `.claude/`, `.claude/agent-memory/`, the ledgers, DECISIONS.md, the rubric, vm/ or code.

**Result: PASS** at level WRITTEN. This is the producer's claim, not a grade: the edits and the append are on disk and proven by the outputs above. The adversary's one MAJOR was cured by writing this report, and that cure has not been re-attacked.

## Does NOT cover

- Values :12 "Nothing else is open (list C)" and list (C)'s missing OPEN entry for A5's second half (U7 :427). Both are outside this unit's lines and are left for the master.
- Adversary MINORs 2 and 9, left as is (see Disposition).
- The U7 report's other claims that the audit did not flag, for example :70's "Nothing was staged, committed, stashed or reset". Only :16, :20, :64, :69 and :70's mtime half were re-examined.
- Whether `scratchpad/before/` stays available. It is session-scoped and not in git.
- Any judgement on Amear's open questions (D-2026-11-08-B NEEDS AMEAR (i)–(iv), the tier pick, A5's second half). They are labelled OPEN, not answered.
- Re-auditing, rebuilding the commit index, and committing. Those belong to the master.
