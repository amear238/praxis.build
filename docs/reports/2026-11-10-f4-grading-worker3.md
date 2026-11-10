# 2026-11-10-f4-grading — worker 3 (ADVERSARIAL)

## Task
Attack `docs/reports/2026-11-10-f4-grading-manager.md` (untracked draft, 362 lines, read in full at call 2) on criteria A–E of the brief. Do not improve it.

## Mode
ADVERSARIAL. Read-only on every file except this one. HEAD d30ab4d. Nothing staged, no git index operations.

## Criterion
Brief A (S2 labels), B (quote fidelity against HEAD blobs), C (factual claims), D (personal data in the artifact and worker 1 / worker 2 reports), E (forbidden content).

Naming convention used here: name-1 = the sender/signature name on reply 2; name-2 = the name in reply 2's body ("My name is ..."); name-3 = the reply-1 Respondent in the 2026-08-07 report §1 (:36), also the addressee in the outgoing preview (transcript :16). The transcript path is written `docs/reports/evidence/2026-10-28-mffu-*-reply-transcript.md` because the real file name carries name-1.

## Process log
- Call 1: this file did not exist (`ls: ... No such file or directory`); transcript path resolved by `git ls-tree` (single HEAD blob); artifact untracked (`?? docs/reports/2026-11-10-f4-grading-manager.md`).
- Call 2: read the artifact in full. Call 3: skeleton of this report.
- Calls 4–17: transcript read with line numbers; forbidden-token and personal-data greps; quote-fidelity greps against HEAD blobs; 2026-08-07 report §B/§C/§E read (names masked in output); R6 page capture read in full around Section 1–5; V7 counts re-run; F4-closed and outgoing-text searches; spot checks of line numbers.

## Findings

### 1. BLOCKING (brief E) — a forbidden word is in the artifact, artifact :281
The first forbidden word of brief E appears once, inside V4's pasted cut of DECISION_LOG.md :179 (the phrase "audit FAIL [word] itself"). It enters through quoted source text, but brief E bars the word from the artifact without exception.
```text
word1 lines: 281
token2 count: 0
token3 count: 0
S13 sentence count: 0
```
Fix: cut the V4 :179 line before that phrase (for example `cut -c1-330`, ending after "BANKED, not spent.**"), or replace the word with a marked `[word withheld]` token and say so in the V4 header.

### 2. BLOCKING (brief A, S2) — row 14 is labelled more strongly than its own required parts, and rows 3/4/8/14 contradict each other, artifact :94, :95, :99, :105
Row 14 (fallback option 3, the whole pattern: NT8 strategy, NinjaScript gates, `EnterLong`/`EnterShort`, Rithmic route) is COVERED-BY-INFERENCE. The rationale says "Its platform and route parts are rows 3 and 8, NOT ADDRESSED". A composite whose required parts are NOT ADDRESSED cannot carry a stronger label than those parts without going above what the words support. Row 4 has the same problem: "A NinjaScript strategy inside NT8" is COVERED-BY-INFERENCE while row 3, "NinjaTrader 8 as the platform", is NOT ADDRESSED. The inference stated for rows 4 and 14 is that "algo trading" / "automated trading strategies" "reaches a strategy hosted in NT8 on a Rithmic route". If that inference is accepted, rows 3 and 8 are also COVERED-BY-INFERENCE (labelled too weak). If it is not accepted, rows 4 and 14 are NOT ADDRESSED (labelled too strong). The table holds both positions at once. The prior record agrees with the weaker reading: the 2026-08-07 report addendum §C labels F4 "this specific automation pattern" **DOES NOT ADDRESS** (HEAD :634), because "PRAXIS routes orders through NinjaTrader 8 and Rithmic, and the reply names neither".
Evidence (the artifact's own rows, from the Read at call 2; R2 platform counts re-run):
```text
94  | 3 | NinjaTrader 8 as the platform that places orders | none: ... | NOT ADDRESSED | ...
95  | 4 | A NinjaScript strategy inside NT8 that submits orders ... | COVERED-BY-INFERENCE | ... The inference is that a strategy hosted in NT8 counts as an "automated trading strateg[y]" ...
99  | 8 | Rithmic as the connection / order route ... | NOT ADDRESSED | ...
105 | 14 | Fallback option 3 ... | COVERED-BY-INFERENCE | Same inference as rows 2 and 4 (that "algo trading" / "automated trading strategies" reaches a strategy hosted in NT8 on a Rithmic route). Its platform and route parts are rows 3 and 8, NOT ADDRESSED. |
25
NinjaTrader=0 NT8=0 Ninja=0 Rithmic=0 webhook=0 n8n=0 TradingView=0 file=0 Tradovate=2 API=2 strategy=1 bot=1 automat=5 algo=1 human=0 click=0 bracket=0 http=1
```
Fix: split row 14 into its parts, or label the composite at the weakest part (NOT ADDRESSED), with the single inference written as an Open question. Make row 4 "strategy, platform-free" only (P / R2 bullet 3 cover "automated trading strategies" as a general activity, which row 1 already does), or say plainly that rows 3, 4, 8 and 14 rest on one inference and give them all the same label. Cite addendum §C :634 as the earlier DOES NOT ADDRESS mapping.

### 3. BLOCKING (brief C) — the bold headline claim is false by the artifact's own table, artifact :32 against :38
:32 says in bold "No verbatim text of any outgoing message to MFFU is on disk at HEAD." Row 3 of the table below it (:38) gives the outgoing preview and marks it "Verbatim? Yes, as far as visible". That preview is on disk at HEAD in two blobs:
```text
thanks for confirming        HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md HEAD:docs/reports/evidence/2026-10-28-mffu-*-reply-transcript.md
Two follow-ups               HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md HEAD:docs/reports/evidence/2026-10-28-mffu-*-reply-transcript.md
642:   (2026-08-07 report line carrying "Two follow-ups so I can be sure")
```
(Transcript path name-masked by me. The underlying grep was `git grep -l -i -F`.)
Fix: "No **complete** text of any outgoing message to MFFU is on disk at HEAD; the only verbatim fragment is the truncated preview at transcript :16 (also 2026-08-07 report :642)."

### 4. MINOR (brief B) — "fence lines" are file line numbers, artifact :60
"fence lines 15–39 (V2) ... (fence lines 27–33)". The fence opens at file :14 and closes at :40, so 15–39 and 27–33 are file lines. In fence numbering they are 1–25 and 13–19. :38 uses the right convention ("fence line 2 (file :16)"), so the report mixes both.
```text
14:```text
40:```
```
Fix: "file lines 15–39 ... (file lines 27–33; fence lines 13–19)".

### 5. MINOR (brief B) — the quote of DECISION_LOG :179 adds a bold marker that is not in the source, artifact :133
The artifact quotes "...naming the specific automation pattern is authorised.**". In HEAD the bold does not close there; it runs on into ruling (2).
```text
179:-        (grep -nF of the quote without the trailing ** hits line 179)
             (the same quote with the trailing ** returns no line)
is authorised. (2) The F4                 <- HEAD DECISION_LOG.md :179
is authorised.**" (                       <- artifact :133
```
Fix: end the quote at "authorised." and close it with "…", or quote through "(2) ... BANKED, not spent.**".

### 6. MINOR (brief B) — the quote of DECISION_LOG :435 drops two quote characters along with the name, artifact :133
HEAD reads `FILE the MFFU "<name-1>" reply`. The artifact reads `FILE the MFFU [rep name] reply`. Only the name itself may be swapped for a token; the surrounding `"` are source bytes. V4 (:282) keeps them, so the two copies in the artifact differ.
```text
F4 evidence: FILE the MFFU "<name-1>" reply      <- HEAD (name masked by sed)
FILE the MFFU [rep name] reply AN                 <- artifact :133
```
Fix: `FILE the MFFU "[rep name]" reply`.

### 7. MINOR (brief B) — elided text shown in quote marks as though verbatim, artifact :101 (and :103)
Row 10 quotes R1 as "the evaluation ... account stages". That string is not in the source (count 0). :103 does the same with "all plans ... live account stages".
```text
101:|      (artifact line holding the elided quote)
0          (count of that string in HEAD 2026-08-07 report)
```
Fix: quote the full R1 phrase ("on all plans including the evaluation, simulated-funded and live account stages."), or mark the cut as "[…]" and add a note that it is an elision.

### 8. MINOR (brief A) — row 13's "MFFU words that bear on it" column says "none" when MFFU words do bear on it, artifact :104
The element is "The trader's own account, opened before any 'now permitted' change". R1's "Algo trading is now permitted at MFFU moving forward on all plans" is the very "now" the element quotes, and R2's "your MyFundedFutures Tradovate evaluation and funded accounts" is the second-person phrase that the addendum §C row 4 maps against this point. The NOT ADDRESSED label can stand, since neither phrase names an account or a date. The "none" in the words column cannot.
```text
| 13 | The trader's own account, opened before any "now permitted" change | none | NOT ADDRESSED | Neither reply names an account or an effective date (F4 report §3.2; addendum §C rows 3–4). |
```
Fix: list both phrases in the words column and keep NOT ADDRESSED, giving the reason ("'now ... moving forward' gives no date; 'your ... accounts' identifies no account").

### 9. MINOR (brief A / completeness) — MFFU's published page carries conditions that bear on rows 2 and 12 but are left out of the record, artifact :77–84, :107
The artifact quotes only Section 1 of the R6 capture and then says (:107) that the stated conditions are "no HFT; no automated tools that exploit favourable sim fills; CME guidelines on live accounts; trader responsible". The same page (same capture, branch `r6/announcement-research` at `bf6fcc7`) also says:
```text
● Slippage and Bracket Usage: Exploiting the absence of slippage and utilizing tight brackets to gain from favorable fills are not permitted.
● Tier 1 Economic Data Trading: Engaging in trades during tier 1 economic data releases is restricted.
Each individual trader is required to maintain their own individual trading activity. Meaning, entering, exiting and cancelling their own trade executions. Traders are not permitted to copy trade one another by entering, exiting or cancelling trade positions.
MyFunded Futures prohibits hedging of any kind. ...
```
Row 2's element is `SubmitBracket` (entry plus stop and target). The bracket line bears on it directly. The Section 4 sentence, read literally ("entering, exiting and cancelling their own trade executions"), is the nearest any MFFU line comes to saying something against "no human click per order". In context it sits under the copy-trading heading, so I do not argue CONTRADICTED, but the CONTRADICTED paragraph should say that this line was considered and why it was rejected. As written, "No MFFU line found prohibits any element" was never tested against it.
Fix: add these lines to the P quote (marked as Sections 2, 4 and 5) and to the conditions list at :107. In row 2, add the bracket line as a condition. In the CONTRADICTED paragraph, add the Section 4 sentence and the reason it is not CONTRADICTED.

## Checks that found nothing

- **D. Personal data, the three reports.** Every count is 0. (Grep run case-insensitively per name; the names stay out of this report.)
```text
docs/reports/2026-11-10-f4-grading-manager.md name-1=       0 name-2=       0 name-3=       0 email=       0
docs/reports/2026-11-10-f4-grading-worker1.md name-1=       0 name-2=       0 name-3=       0 email=       0
docs/reports/2026-11-10-f4-grading-worker2.md name-1=       0 name-2=       0 name-3=       0 email=       0
hex count found: 1
docs/reports/2026-11-10-f4-grading-manager.md tid-hits=0
docs/reports/2026-11-10-f4-grading-worker1.md tid-hits=0
docs/reports/2026-11-10-f4-grading-worker2.md tid-hits=0
docs/reports/2026-11-10-f4-grading-manager.md sender-localpart-hits=0
docs/reports/2026-11-10-f4-grading-worker1.md sender-localpart-hits=0
docs/reports/2026-11-10-f4-grading-worker2.md sender-localpart-hits=0
```
(Email regex `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}`. The thread id is the one 16-hex token on DECISION_LOG :177. The local part is the reply-1 sender local part from the 2026-08-07 report :34.)
- **E. Other forbidden tokens and the S13 sentence.** Token 2 and token 3 count 0. The S13 sentence counts 0 in the artifact (output under finding 1).
- **B. Quote fidelity, all other quotes checked.** Every one is byte-present at the cited line:
```text
2026-08-07 report: R1 line 1 => 28 ; R1 line 2 => 29 ; "human support rep" => 36 349 ; "Inference, not observed" => 748 (inside §E item 2)
transcript: "You are responsible ..." => 33
ISSUE_REGISTER.md: "the outreach was run ..." => 70 ; "an English inquiry" => 70 ; "outreach sent 2026-07-26 window" => 70
DECISION_LOG.md: "the MFFU inquiry email are the TRADER'S actions to execute" => 46 ; "2026-07-26T21:20:22Z" => 177 ; "by a human rep" => 177 ; "boilerplate indicator" => 435 ; A15 conflict sentence => 801 ; "... naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.**" => 435
HANDOFF.md: follow-up description => 784 ; "Follow-up sent 2026-08-07, awaiting reply." => 764
DECISIONS.md: "Does Amear send the follow-up himself" => 539 ; :2054 starts "**The working design: option 1**" ; :2056 starts "**Fallback: option 3, only if OPEN-T1 fails.**"
voice-session-notes-3: "Whether Amear sends the follow-up himself is unconfirmed" => 44
specs/SPEC_RUBRIC.md: criterion => 49 ; "17:## FROZEN" "48:### F4" "61:## PASSED"
strategy-filter-audit A15 row => 68
topology spec :41 starts "Path: NT8 emitter (computes signal) → HT"
R6 branch bf6fcc7: lines 64, 65, 66, 76, 77, 79, 80 as cited in V8 (re-read in full at call 10)
Transcript R2 lines 27–33 match the artifact :62–68 (read with cat -n at call 4)
```
- **C. Reply-1 channel and author claims.** Confirmed: the 2026-08-07 report :34 sender domain is `myfundedfutures.intercom-mail.com` (local part masked), :35 timestamp 2026-07-26T21:20:22Z, :36 Respondent "<name-3>, human support rep", all marked "UNVERIFIED — relayed". DECISION_LOG :177 carries the same timestamp and "by a human rep". ISSUE_REGISTER :68: "MFFU confirmed IN WRITING, via a human support rep, ...".
- **C. Reply-2 date, channel and author claims.** Confirmed against transcript :3, :18, :21–25, :36, :64, :65, and against addendum §E items 1–2 (:727–750). The artifact does not claim a human author for R2.
- **C. V7 term counts.** Re-run on the ```text fence (25 lines): every count matches V7 (output in finding 2). Note that `http` = 1 (the URL). Row 5's "No line ... describes ... HTTP" still holds, since a link is not a description.
- **C. "Only one HEAD document calls F4 closed in its own words."** No break. `git grep -i -w F4` filtered for closed/satisfied/cleared/unfrozen/resolved/passed/met/done (negations removed) leaves only strategy-filter-audit :68 as an affirmative claim. The other hits are negations (2026-08-07 report :140, :533; 2026-10-28 reply-filing report :348, :367), FROZEN status lines (STATUS :104, :143), S6 coupling text (DECISIONS :285), conflict flags (DECISION_LOG :801, f1-f2-proposal :36) or other uses of "F" numbering (a20 report :487, kit gap list :28). "explicitly permitted" appears only at SPEC_RUBRIC :54, the rubric's own description of the Round 3 handoff. Limit: my regex would not catch phrasings outside that word list.
- **C. No complete outgoing text.** No break beyond finding 3. Probes "Dear MFFU", "Hi MFFU", "Hello MFFU", "I am building", "draft email", "draft of the follow-up", "follow-up draft", "To: support" return no files. "Subject: " hits only an unrelated .msi `file` output and a status report. "email draft" hits only the 2026-08-07 report :582, which states no drafting was done.
- **A. Rows 1, 5, 6, 7, 9, 10, 11, 12 and the Account-type scope table.** The labels are consistent with the quoted words. Rows 10–12 are scoped to row 1 in the text. The scope table quotes match R1 :29 and transcript :27, :29, :31 and R6 :77/:80. No CONTRADICTED is owed by R1 or R2. R2's Tradovate route does not bar other routes.
- **A. Sentences that grade F4.** None found. :6, :16 and :139 say the opposite. The A15 and DECISION_LOG :179/:435 lines are marked "Quoted, not adopted".
- **Index state.** `git diff --cached --name-only` shows the one PNG path only (name-masked), matching artifact :4.

## Files staged
None.

## Result
FAIL — 3 BLOCKING (findings 1–3), 6 MINOR (findings 4–9).

## Correction 1 (2026-11-10, after audit fail 1)

This section was written by the manager, not by worker 3. The first audit found that this report states probe results ("return no files", and the other items under "Checks that found nothing") with no output. The blocks below are the **manager's** re-runs at HEAD `d30ab4d` on 2026-11-10. Worker 3 did not run them in this form, and where a worker command is not recorded, the manager's command can differ from it. Each block shows the literal command lines and their unedited output, apart from two filters that the command lines show. `perl -p /tmp/f4c1/redact.pl` writes `[address]` for an email address and `[patN]` for line N of `/tmp/f4c1-pat.txt` (line 1 is the trader's surname, lines 2 to 4 are the support representatives' names, line 5 is the thread id). `sed 's/-[a-z]*-reply/-[name]-reply/'` masks a representative's first name in a path. The method is in block C1-V0 of `docs/reports/2026-11-10-f4-grading-correction-1-manager.md`. This section changes no finding and no severity.

### C1-X1. "C. No complete outgoing text" probes

~~~text
$ for s in "Dear MFFU" "Hi MFFU" "Hello MFFU" "I am building" "draft email" "draft of the follow-up" "follow-up draft" "To: support" "Subject: " "email draft"; do printf '%-24s files=%s\n' "$s" "$(git grep -l -i -F -e "$s" HEAD | wc -l | tr -d ' ')"; done
Dear MFFU                files=0
Hi MFFU                  files=0
Hello MFFU               files=0
I am building            files=0
draft email              files=0
draft of the follow-up   files=0
follow-up draft          files=0
To: support              files=0
Subject:                 files=2
email draft              files=1
$ git grep -l -i -F -e "Subject: " HEAD
HEAD:docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
HEAD:docs/reports/2026-11-06-status-handoff-evening-manager.md
$ git grep -n -i -F -e "email draft" HEAD | cut -d: -f1-3
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:582
~~~

Agrees. The eight phrases worker 3 lists return no file. "Subject: " (with the space) hits two files: the o78 unit's `.msi` `file` output and the 2026-11-06 status-handoff report. "email draft" hits only the 2026-08-07 report :582. The positive controls for this method, and the "Two follow-ups" and "Does this specific" hits, are in the manager report's Correction 1, C1-V40.

### C1-X2. "C. Only one HEAD document calls F4 closed", and "explicitly permitted"

~~~text
$ git grep -n -i -P '\bF4\b[^.|;]{0,25}\b(closed|satisfied|cleared|unfrozen)\b' HEAD | cut -c1-130 | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl
HEAD:DECISION_LOG.md:801:- [2026-11-10T13:29:00Z] WHO: praxis-master | WHAT: **F1/F2 manager returned (corr a6a339af7485905dd, 61 
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:140:- Not claimed: that F4 is discharged, satisfied, or unfrozen.
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:533:correctly and honestly graded*. It does **not** mean F4 is satisfi
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:367:- F4 is not discharged, satisfied or unfrozen. `specs/SPEC_RUBRIC.md` is 
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:68:| A15 | Low frequency to reduce prop-firm detection risk | D3 §1 and §6 S
HEAD:docs/reports/2026-11-10-f1-f2-proposal-manager.md:36:Observation not acted on: the strategy filter audit row A15 (audit :68) 
$ git grep -n -i -F 'explicitly permitted' HEAD | cut -c1-120
HEAD:specs/SPEC_RUBRIC.md:54:other: the Round 3 handoff asserts automation is explicitly permitted; Phase 2
$ git show HEAD:STATUS.md | grep -n -w F4 | cut -c1-100
7:**Phase:** unchanged — Block 2 (Backtesting); F1/F2/F4 FROZEN; F3 FROZEN conditional. No row today
54:**Phase:** unchanged — Block 2 (Backtesting); F1/F2/F4 FROZEN; F3 FROZEN conditional. No ruling t
104:**Phase: unchanged. Block 2 — Backtesting. F1, F2, F4 FROZEN; F3 FROZEN.** `grep -n -E "PASSED@|
143:**Phase: Block 2 — Backtesting. F1, F2, F4 FROZEN. F3 FROZEN in the rubric: the conditional deci
204:**Phase: Block 2 — Backtesting. F1, F2, F4 FROZEN. F3: the assumption is committed, the backtest
218:**Phase: Block 2 — Backtesting. F1, F2, F4 FROZEN and untouched. F3 one commit away from unfreez
230:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
238:**Filed:** `Praxis_build-a20`, the NT8 time-zone and Kinetick reads on Fusion, due before the 20
242:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
256:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
266:**Carried unchanged.** F4 awaits the MFFU reply. `r8j`'s spec is still not on `main`. K7 remains
270:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
282:**Carried unchanged.** F4 awaits the MFFU reply. `r8j`'s spec is still not on `main`, so F1/F2 s
286:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
292:**Amear banked the repair shot and gated Step 2 on it** — `Praxis_build-f5f` stays at FAIL 1 of 
302:**Phase unchanged: Block 2 — Backtesting. F1–F4 all still FROZEN and untouched.** No trading cod
318:**Phase unchanged: Block 2 — Backtesting.** F1–F4 all still FROZEN and untouched.
334:**Phase unchanged: Block 2 — Backtesting.** No build work. `4uu` still frozen; all four FROZEN r
356:**Phase unchanged: Block 2 — Backtesting.** No build work. `4uu` still frozen; all four FROZEN r
368:**Phase unchanged: Block 2 — Backtesting.** No build work. `4uu` still frozen behind its gates; 
$ RF=$(git ls-tree -r --name-only HEAD docs/reports/ | grep -- '-f4-[a-z]*-reply-filing.md$'); git show "HEAD:$RF" | sed -n '348p;367p' | grep -c -w F4
2
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
$ git grep -n -i -o -P '\bF4\b[^.|;]{0,25}\b(closed|satisfied|cleared|unfrozen|resolved|passed|met|done)\b' HEAD -- STATUS.md 'docs/reports/2026-10-28-f4-*-reply-filing.md' docs/reports/2026-11-04-status-refresh-manager.md docs/reports/2026-11-06-status-handoff-refresh-manager.md | sed 's/-[a-z]*-reply/-[name]-reply/'
HEAD:STATUS.md:143:F4 :59-70 (no `PASSED
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:232:F4 is (met
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:348:F4 is met
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:367:F4 is not discharged, satisfied
HEAD:docs/reports/2026-11-04-status-refresh-manager.md:257:F4 :59-70 (no `PASSED
HEAD:docs/reports/2026-11-06-status-handoff-refresh-manager.md:148:F4 not PASSED
HEAD:docs/reports/2026-11-06-status-handoff-refresh-manager.md:194:F4 are FROZEN (CMD: no `PASSED
$ git grep -n -o -P '.{0,20}\bF4 is \(?met.{0,25}' HEAD -- 'docs/reports/2026-10-28-f4-*-reply-filing.md' | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:232:PRAXIS|satisfies F4|F4 is (met|satisfied|cleared)`
HEAD:docs/reports/2026-10-28-f4-[name]-reply-filing.md:348:hat says or implies F4 is met. No round found PRAXIS a
$ git show HEAD:DECISIONS.md | sed -n 285p | grep -c -w F4; git show HEAD:docs/reports/2026-10-20-a20-adversarial-2.md | sed -n 487p | grep -c -w F4; git show HEAD:docs/reports/2026-08-08-project-kit-v0.2-gap-list.md | sed -n 28p | grep -c -w F4
1
0
1
~~~

Reading. Worker 3's :141 names eight status words (closed, satisfied, cleared, unfrozen, resolved, passed, met, done) but not the exact filter it ran. The first command uses four of the words (F4 within 25 characters of closed, satisfied, cleared or unfrozen). Its six hits are: one affirmative claim (strategy-filter-audit :68), two conflict flags (DECISION_LOG.md :801, f1-f2-proposal :36) and three negations (2026-08-07 report :140 and :533, reply-filing report :367). This agrees with worker 3. The reply-filing report's :348, which worker 3 also lists, is not among this regex's hits. The fourth command shows that :348 and :367 both name F4, and the seventh prints the :348 span. "explicitly permitted" appears only at SPEC_RUBRIC.md :54, which agrees. STATUS.md carries F4 FROZEN status lines at :104 and :143 among others, which agrees. The fifth command uses all eight words and gives 12 hits, the six above plus six more: STATUS.md :143, the reply-filing report :232 and :348, status-refresh :257, and status-handoff-refresh :148 and :194. The sixth and seventh commands print the matched spans. In STATUS.md :143 and status-refresh :257 the span is a line reference with "no `PASSED`"; status-handoff-refresh has "F4 not PASSED" and "F4 are FROZEN". At reply-filing :232 the span is part of a search pattern ("satisfies F4|F4 is (met|satisfied|cleared)"), and :348 reads "says or implies F4 is met. No round found". None of the six claims closure of F4, so worker 3's conclusion holds with all eight words too. The last command checks three more of worker 3's :141 entries. DECISIONS.md :285 has F4 (1) and the kit gap list :28 has F4 (1), but a20-adversarial-2 :487 has no F4 as a word (0). That disagrees with worker 3, which lists a20 :487 among the "other uses of F numbering".

### C1-X3. "C. Reply-1 channel and author" and "C. Reply-2 date, channel and author"

~~~text
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); git show "HEAD:$T" | grep -n '' | sed -n '3p;18p' | cut -c1-120 | perl -p /tmp/f4c1/redact.pl
3:- Source file: `/Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23<U+202F>PM.png` (the character before `PM` is U+2
18:[pat4] from MyFundedFutures <[rep-address]@myfundedfutures.intercom-mail.com>
$ git show HEAD:DECISION_LOG.md | sed -n 177p | grep -o -e '2026-07-26T21:20:22Z' -e 'by a human rep' | sort | uniq -c
   1 2026-07-26T21:20:22Z
   1 by a human rep
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F -e 'human support rep' -e 'Inference, not observed' | cut -c1-80 | perl -p /tmp/f4c1/redact.pl
36:| Respondent | [pat2], human support rep | UNVERIFIED — relayed |
349:68:- [2026-08-07T16:13:58Z] WHO: Amear | WHAT: F4 evidence landed — MFFU con
748:   **Inference, not observed:** the two greetings plus the "[pat3]" vs "Dav
$ git show "HEAD:$T" | grep -n -F 'You are responsible for the performance' | cut -c1-60
33:You are responsible for the performance and reliability o
~~~

Agrees. Transcript :3 is the capture source line and :18 is the sender display line, with the domain `myfundedfutures.intercom-mail.com` and the local part already masked in the source. DECISION_LOG.md :177 has the timestamp and "by a human rep" once each. The 2026-08-07 report has "human support rep" at :36 and :349, and "Inference, not observed" at :748, inside §E (heading :727, C1-X4 below). Transcript :21 to :25, :36, :64 and :65 are printed in the manager report's Correction 1, C1-V2, and the report's :34 to :36 in C1-V3.

### C1-X4. "B. Quote fidelity, all other quotes checked"

~~~text
$ git show HEAD:ISSUE_REGISTER.md | grep -n -F -e 'the outreach was run to establish whether the PRAXIS automation pattern is permitted per-firm' -e 'an English inquiry' -e 'outreach sent 2026-07-26 window' | cut -d: -f1 | tr '\n' ' '; echo
70 
$ git show HEAD:DECISION_LOG.md | grep -n -F -e "the MFFU inquiry email are the TRADER'S actions to execute" -e 'by a human rep' -e 'boilerplate indicator' -e 'F4 is called "closed" in the strategy filter audit' -e 'naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.**' | cut -d: -f1 | tr '\n' ' '; echo
46 177 435 801 
$ git show HEAD:DECISION_LOG.md | grep -c -F '2026-07-26T21:20:22Z'
1
$ git show HEAD:HANDOFF.md | grep -n -F -e 'A follow-up email naming the actual architecture, and asking the policy' -e 'Follow-up sent 2026-08-07, awaiting reply.' | cut -d: -f1 | tr '\n' ' '; echo
764 784 
$ git show HEAD:DECISIONS.md | grep -n -F 'Does Amear send the follow-up himself' | cut -d: -f1; git show HEAD:DECISIONS.md | sed -n '2054p;2056p' | cut -c1-48
539
**The working design: option 1** (:37–41, :74, :
**Fallback: option 3, only if OPEN-T1 fails.** O
$ git show HEAD:docs/reports/2026-11-01-voice-session-notes-3.md | grep -n -F 'Whether Amear sends the follow-up himself is unconfirmed' | cut -d: -f1
44
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -F 'Written confirmation from MFFU that this specific automation' | cut -d: -f1
49
$ git show HEAD:docs/reports/2026-11-08-strategy-filter-audit.md | grep -n -F '| A15 | Low frequency to reduce prop-firm detection risk |' | cut -d: -f1
68
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n 41p | cut -c1-40
Path: NT8 emitter (computes signal) → HT
$ git show HEAD:DECISION_LOG.md | sed -n 179p | grep -c -F 'naming the specific automation pattern is authorised. (2)'; git show HEAD:DECISION_LOG.md | sed -n 179p | grep -c -F 'naming the specific automation pattern is authorised.**'
1
0
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F 'Inference, not observed' | cut -d: -f1; git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F '### E' | cut -c1-60
748
727:### E. Anomalies
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); diff <(git show "HEAD:$T" | sed -n 27,33p) <(sed -n 70,76p docs/reports/2026-11-10-f4-grading-manager.md | sed 's/^> \{0,1\}//') && echo "transcript 27-33 = manager report 70-76 (quote prefix removed)"
transcript 27-33 = manager report 70-76 (quote prefix removed)
~~~

Agrees on every line number worker 3 gives. ISSUE_REGISTER.md :70 holds all three strings. DECISION_LOG.md holds its strings at :46, :177, :435 and :801. HANDOFF.md :764 and :784, DECISIONS.md :539, notes-3 :44, SPEC_RUBRIC.md :49 and strategy-filter-audit :68 hold theirs. The DECISIONS.md :2054 and :2056 openings and the topology spec :41 opening agree. The DECISION_LOG.md :179 quote is present without the trailing bold marker (1) and absent with it (0), as finding 5 says. Transcript lines 27 to 33 equal the manager report's current lines 70 to 76 once the `> ` quote prefix is removed. The R6 lines are re-run with literal commands in the manager report's V8.

### C1-X5. "C. V7 term counts" and "Index state"

~~~text
$ grep -ci bracket /tmp/f4c1/fence.txt; grep -ci http /tmp/f4c1/fence.txt
0
1
$ git diff --cached --name-only | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
~~~

Agrees: `bracket` 0 and `http` 1 in the 25-line fence. The other V7 counts are re-run in the manager report's Correction 1, C1-V7, and every one agrees. The index holds only the PNG path, with the name masked.

### C1-X6. "A. Rows 1, 5, 6, 7, 9, 10, 11, 12 and the Account-type scope table" and "A. Sentences that grade F4"

~~~text
$ sed -n '98,115p' docs/reports/2026-11-10-f4-grading-manager.md | grep -E '^\| (1|4|5|6|7|9|10|11|12|14a) \|' | awk -F'|' '{print $2 "|" $5}'
 1 | COVERED-EXPLICITLY 
 4 | COVERED-BY-INFERENCE 
 5 | NOT ADDRESSED 
 6 | NOT ADDRESSED 
 7 | NOT ADDRESSED 
 9 | NOT ADDRESSED 
 10 | COVERED-EXPLICITLY 
 11 | COVERED-EXPLICITLY 
 12 | COVERED-EXPLICITLY 
 14a | COVERED-BY-INFERENCE 
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); for s in 'your MyFundedFutures Tradovate evaluation and funded accounts' 'evaluation, simulated-funded, and live account stages' 'For live accounts'; do printf '%s\n' "$(git show "HEAD:$T" | grep -n -F -- "$s" | cut -d: -f1 | tr '\n' ' ')"; done; git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F 'evaluation, simulated-funded and live account stages' | cut -d: -f1; git show r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt | grep -n -F -e 'on our plans' -e 'Traders trading live accounts with automated trading' | cut -d: -f1 | tr '\n' ' '; echo
27 
29 
31 
29
77 80 
$ grep -n -i -E "does not grade F4|not graded here|Quoted, not adopted" docs/reports/2026-11-10-f4-grading-manager.md | cut -c1-70 | head -5
6:This report compares. It does not grade F4 and recommends no state f
16:- F4 is the subject matter only. It is not graded here.
144:One HEAD document calls F4 closed in its own words. Quoted, not ad
462:This section changes evidence form only. No element-table label, n
$ grep -n -i -E 'F4 (passes|is closed|is satisfied|is met|should be|can be closed)|satisfie[s] F4|recommend(s|ed)? (that )?F4' docs/reports/2026-11-10-f4-grading-manager.md | cut -d: -f1
427
~~~

Reading. The labels of rows 1, 4, 5, 6, 7, 9, 10, 11, 12 and 14a in the current table are as listed. The scope-table quotes are present: R2 at transcript :27, :29 and :31, R1 at the 2026-08-07 report :29, and the published page at :77 and :80. The lines that say the report does not grade F4 are :6 and :16. :144 marks the A15 quote "Quoted, not adopted", and :462 is the opening of the manager report's own Correction 1. Worker 3 cited :139, a line number of the draft it read. The grading-phrase search prints line numbers only. Its only hit is V11's own command line (:427), which contains the searched words. No sentence of the report matches.

### Not re-run

- The evidence blocks under findings 1 to 9 quote the manager draft as it stood when worker 3 read it (362 lines). That draft no longer exists in that form, so those blocks cannot be re-run. Their HEAD-side parts are re-run: finding 3 in the manager report's Correction 1, C1-V40 (the two blobs); finding 4 in C1-V2 (fence :14 and :40); and finding 5 in C1-X4 above (counts 1 and 0).
- "No CONTRADICTED is owed by R1 or R2" and "R2's Tradovate route does not bar other routes" (worker 3, under A) are readings of quoted lines, not probes. The lines they rest on are printed in the manager report's Correction 1, C1-V2.
- "D. Personal data, the three reports": the per-file counts for every report of this unit are re-run after the last edit in the correction-1 manager report, section "Final checks".

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
