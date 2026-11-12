# Unit 2026-11-12-mffu-prepurchase-filing — manager report

## Task

File the Claude.ai channel's return handoff `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md` as written, after de-identification checks; grade each numbered statement in MFFU support's two replies against the repo's own text; list two questions for Amear with no recommendation; append MANIFEST rows; run one adversarial worker. Authority: master decision under D-2026-11-08-D D1 within Amear's brief, DECISION_LOG.md:849 (2026-11-12T02:41:00Z). Baseline: `main` at `ee54344`. Nothing is staged or committed by this unit; git refs, the VM, `vm/` and `.claude/` are not touched.

Grade levels used below (S2): OBSERVED means seen in this session with the output pasted here. INFERRED means reasoned from pasted text, not observed. UNVERIFIED means not observed and no source on disk. REPORTED BY means someone's statement, not checked here.

Provenance of the MFFU text (S2). The two replies are REPORTED BY the Claude.ai channel, which says it observed them via the Gmail connector (input :3). No agent in this unit read the Gmail thread. The channel's reading that they are automated assistant replies (input :43) is INFERRED by the channel and is not confirmed here. The channel's other readings at input :44-46 (that OPEN-1 was "answered in writing", that T1 news is answered, and that MFFU "will not approve" a configuration) are likewise INFERRED and are not adopted by this unit; each item is graded below from the reply text itself. Every "MFFU support says" below means "the input file says MFFU support wrote".

## Rubric criteria addressed

- F4 (FROZEN; Owner Amear): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." Graded in G-F4: stays FROZEN / NOT MET.
- S1: every claim below rests on a pasted block in `Verification evidence (command output)` (E0-E9), cited by block id.
- S2: levels as defined above; the MFFU text is REPORTED BY, comparisons are INFERRED.
- S5: no approval is inferred. Amear's chat words "yep" and "go" (input :8-9) are REPORTED BY the channel; the ledger record is DECISION_LOG.md:849 (E9), which itself says "a channel-reported instruction is recorded, not proven given". This unit treats neither reply as an approval of anything.
- S6: cross-block check in its own section (consumer Sim-only guard, D-071, Rule F2-1, R6 design).
- S8: Q1 and Q2 are listed for Amear and not answered; no option is recommended.
- S13: the S13 sentence is the last line of this report, once.

## Workers dispatched (id, mode, outcome)

| id | mode | scope | outcome | report |
|---|---|---|---|---|
| worker1 | ADVERSARIAL | whole report: S1, S2, S8, F4 quote, de-identification, placeholders, S13, forbidden strings, S6, MANIFEST | FAIL: 2 MAJOR, 9 MINOR; all eight pasted evidence blocks re-ran byte for byte (its C1) | `docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md` |
| worker2 | ADVERSARIAL | narrow re-check of the two MAJOR fixes and the moved Questions section | see Adversarial findings | `docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md` |

## Process log

1. Read `specs/SPEC_RUBRIC.md` (461 lines, E9) and the input file in full.
2. Ran the four de-identification checks with runtime positive controls (E1). All four pass; the input is not edited. Its sha256 before and after this unit is in E1 and E8.
3. Line count: the brief says the input is 47 lines; `wc -l` prints 46 (E1) and the file ends in a newline (E9). Recorded here, not corrected; the content is the 46 lines quoted by line number below.
4. Found the repo text for each item by `grep` on the working tree and `git grep` on `HEAD` and on `r6/announcement-research` (`bf6fcc7`), because the R6 design is only on that branch (E2: on `HEAD`, `docs/specs` has the OPEN-1 pointer only in the F2 proposal).
5. Wrote this report, appended MANIFEST rows (E7), then dispatched worker1 (ADVERSARIAL). It returned 2 MAJOR and 9 MINOR. The manager fixed all eleven in this report (no fix worker; doc edits only), added block E9, dropped an unused T1 count from E2/E3, moved the Questions section to the end, and appended a MANIFEST row for worker2.
6. Dispatched worker2 (ADVERSARIAL) on the two MAJOR fixes only; no second round for the MINORs, per the brief.

## Grading of the MFFU statements

Source quotes, copied by script with source line numbers, are block E0. R1 is the 2026-11-11T22:38:25Z reply (input :16-27), R2 the 2026-11-11T22:41:33Z reply (input :32-39). Timing, from the timestamps as written at input :13, :14, :29 and :30 (E9): R1 arrived 58 seconds after the 22:37:27Z mail; R2 arrived 49 seconds after the 22:40:44Z follow-up (arithmetic on REPORTED BY times).

### G1 — R1 point 1 (input :17): automation on funded accounts

Establishes, if accurate (REPORTED BY): automated strategies are permitted on evaluation and funded accounts under Fair Play conditions (own settings, no exploiting simulated fills, no high-frequency trading); the described setup "falls within general automation permission". Does not establish: approval of this configuration ("I cannot issue written approval for your specific configuration"), or that unattended execution is allowed ("or guarantee that unattended execution is allowed without supervision"). It offers a team review. Bearing: G-F4.

### G2 — R1 point 2 (input :19): connection type on funded accounts

Establishes nothing about the account type: "I cannot confirm from available information whether funded accounts use the same "Simulation" connection type as evaluation accounts." It is in tension with R2 point 3 (G8), three minutes later. Bearing: S6 section.

### G3 — R1 point 3 (input :21): inactivity, 7 consecutive calendar days

What it says (REPORTED BY): the rule applies after 7 consecutive calendar days without a trade; contacting support is "advisable", with no exemption guaranteed and no confirmation "that notification alone prevents closure". The 7-day figure matches the MFFU page text already in the repo (E5: investigation :1380, "within 7 consecutive calendar days on your sim funded account"). Against the repo's trade-frequency figures (E5):
- R6 event strategy, design :96 (`bf6fcc7`): "of 173 gaps between consecutive event dates in range, 90 exceed 7 days and the longest is 37"; design :103: "Per year about 8 FOMC + 12 CPI + 12 NFP, union 30-34 dates."
- `PraxisNoiseAreaBreakout`, Run 3 record (transcribed from Amear's screenshot, record :1): "Avg. # of trades per day | 0.81" and "Longest flat period | 20.88 days" (All trades column). That is a backtest figure, not live.
Grade, INFERRED: the R6 design shows 90 gaps of more than 7 days, and the Run 3 record shows at least one (its longest flat period, 20.88 days), so both strategies as designed or backtested go more than 7 calendar days without a trade at least once, and R1 point 3 gives no route that is confirmed to prevent closure. The reply does not change R6 design :96's own position ("A standalone event strategy therefore fails the inactivity rule on Sim Funded accounts"). Nothing is decided here.

### G4 — R1 point 4 (input :23): "overnight"

Establishes: nothing about the definition. "I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team". It adds that "the policy distinguishes between holding within a session versus holding through the daily close". Bearing: G9 and Q1.

### G5 — R1 point 5 (input :25-27): T1 news

The plan's window is on the R6 branch only; `HEAD`'s specs have no news window (E3b: `git grep -c -i news` exit 1). R6 design :22: "(i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage."; :66: exit at the close of the T−5 bar, re-enter at the close of the T+3 bar, "fills at T−4 and T+4, outside T±2". The C3.3 draft ticket states the same window (E3: investigation :1445); that the sent mail carried it is REPORTED BY the channel (input :13, "Five questions as C3.3").
Graded against that text (INFERRED, arithmetic on the pasted lines): MFFU support's window on Rapid and Pro Sim Funded is two minutes before and after the release; [T−2, T+2] lies inside [T−5, T+3], so the reply's statement that the plan's window "covers this requirement" agrees with the plan's own arithmetic. What it does not establish: the reply's rule covers "positions or orders"; design :22 says "Flat" and the pasted lines do not say that no working order exists inside T±2. That is UNVERIFIED. The R6 strategies have no file under `ninjascript/` on the branch (E3: 0 matching names among the branch's `ninjascript/` files), so the window is a design statement, not tested behaviour. Also, R1 says "Builder Sim Funded accounts are unrestricted for T1 news trading"; R6 design :29 treats Builder as blocked because "MFFU's text conflicts (image banner vs Builder guides)". The reply is new text on that conflict; the design's rule (i) applies the window on every account anyway, so nothing in the design is loosened or tightened by this unit. R1 also says the window "does not apply at the evaluation stage", consistent with design :29's "Allowed by the T1 rule in evaluations".

### G6 — R2 point 1 (input :33): the specific configuration

Establishes, if accurate: automation is permitted on Evaluation, Sim Funded and Live under the applicable rules. States in terms that "a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information" and "individual setups are not automatically approved". Bearing: G-F4.

### G7 — R2 point 2 (input :35): unattended execution

Establishes, if accurate (REPORTED BY): that the policy "does not confirm whether unattended execution without supervision is allowed or required", and that "The absence of a supervision rule does not establish permission for a specific unattended configuration." Unattended execution is not confirmed.

### G8 — R2 point 3 (input :37): Simulation account type

What it says (REPORTED BY): "the connection should be configured with the account type set to Simulation in the NinjaTrader connection properties." It agrees with the help article already graded in the repo (E4: investigation :118, :979, "The article tells every reader to set "Simulation" and gives no condition."). It says "your MFFU account" and does not name funded accounts, so it does not answer what R1 point 2 said it could not confirm. Cross-block grading is in the S6 section.

### G9 — R2 point 4 (input :39): evening entry; trading hours

R6 OPEN-1 as the repo words it (E2, design :110 at `bf6fcc7`): "| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |". Design :28 puts the question as "Whether MFFU counts the evening entry as holding overnight".
Graded against that wording (INFERRED): the input gives, as MFFU support's text, a statement that speaks of an evening entry in terms ("A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close."). Whether that text is the written MFFU answer design :110 asks for is Q1. What it does not do: it does not use the word "overnight" (E9: 0 hits on input :38-39), and does not say whether such a hold counts as holding overnight, which is how design :28, message 3 item (4) ("evening entry vs overnight", input :29) and the C3.3 draft's question 4 (E9: investigation :1444, "count as holding overnight?") put it. Reading "does not cross the daily close" as "not overnight" needs a link between the two. Texts on disk that bear on that link include design :25's gloss, which the design itself grades INFERRED ("(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."), design :110's "is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets" (quoted above), and R1 point 4's clause "the policy distinguishes between holding within a session versus holding through the daily close" (input :23, REPORTED BY). None of them says in terms that such a hold is not overnight. R1 point 4, three minutes earlier, said the definition could not be confirmed and needed the team; R2 came 49 seconds after the request for a team review, and the channel reads it as an automated reply (INFERRED). Whether R2 point 4 closes OPEN-1 is not decided here; it is Q1.

Trading hours against Rule F2-1 (E6, DECISIONS.md:2111, inside D-2026-11-11-A, which runs from :2101 to the next heading at :2176, E9): "The closing order for every open system position is submitted no later than 16:00:00 ET (...), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET". R2: "MFFU trading hours run from 6:00 PM to 4:10 PM Eastern Time. Positions must be closed by the 4:10 PM cutoff." Compatibility, INFERRED: F2-1's 16:00 flat precedes the 16:10 cutoff, and F2-1's no-entry interval 16:00-18:00 contains MFFU's closed interval 16:10-18:00, so the two texts do not conflict. Compatibility only: F2 stays FROZEN. Its unblock also needs breaker specs #4 and #5 amended (rubric :30-31), and DECISIONS.md:2108 says "The amended #4/#5 text does not exist" (E6).

### G-F4 — F4

Rubric text (E6, rubric :49-50): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." Grade: NOT MET. F4 stays FROZEN; Owner Amear.
What the replies establish, as REPORTED BY the channel: MFFU support writes that automation is permitted in principle on evaluation, Sim Funded and Live accounts under its rules, and that the described setup "falls within general automation permission" (input :17).
What they do not establish: the thing F4 names. Both replies decline it in terms: "I cannot issue written approval for your specific configuration" (input :17) and "a specific technical configuration (...) cannot be approved in writing from the available information" (input :33). Neither confirms unattended execution (input :17, :35). R1 offers a team review (input :17); the input's message list ends at item 4, the 22:41:33Z reply (E9), so it records no team decision. On top of that, the text is REPORTED BY, and possibly an automated assistant's (INFERRED by the channel).

## S6 cross-block check

1. Consumer Sim-only guard (Block 1/3 code) vs R2 point 3. The guard, read in this session (E4): `RequiredAccountPrefix = "Sim"` (:48) and `Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase)` in `State.DataLoaded` (:96, :100) and at the order boundary (:637, :639) (E9); header :39, "refuses to run unless the attached account name starts with "Sim"". The investigation's Correction 1 (E4, :347): "An MFFU evaluation or funded account is not a "Sim…" account in NT8 terms, so the consumer would refuse to trade it. Going live needs someone to change that guard on purpose. That change is Amear's under D2(b)"; :318, "No change to the consumer's Sim-only guard is proposed or drafted."
   What R2 point 3 would mean for the guard if accurate, INFERRED: it describes the connection's account-type property; the guard reads the account name, not that property (E9: `accounttype` occurs 0 times in the consumer; `Account.Name` is on 7 lines, by `grep -c`, with 8 occurrences, by `grep -oF` piped to `wc -l`). So R2 point 3 alone does not show whether the guard would admit or refuse an MFFU account. If an MFFU account under a "Simulation" connection had a name starting with "sim" in any letter case (the comparison is OrdinalIgnoreCase), the guard would admit it with no code change, and the wall would no longer separate NT8's own simulation accounts from an MFFU account; if not, Correction 1's reading at :347 stands. No MFFU account name was observed by anyone in this unit (Amear has no account, input :10), so which case holds is UNVERIFIED. Nothing is decided; any change to the guard or to the order path to a funded account is D2(b), Amear's.
2. D-071 vs R2 point 3. DECISIONS.md:950 (E4), a line headed "reading (voice agent, notes-4)", so the voice agent's reading, REPORTED BY that agent: "**The MFFU Rithmic connection is approved to be opened when Block 4 starts.** D-071 (Simulated Data Feed only) stands until then." The reply describes how to configure an MFFU connection; it does not change D-071, and no connection is made by this unit.
3. Rule F2-1 (Block 3 session rule) vs R2 point 4: compatible as text (G9); F2 stays FROZEN.
4. R6 design (Block 2 research) vs R1 points 3 and 5 and R2 point 4: G3, G5, G9. Design :96 (inactivity) and :22 (T1 window) are unchanged; OPEN-1 is not closed by this unit.
5. Rubric F4: G-F4, NOT MET.

## Adversarial findings

Worker1 findings, as numbered in its report (:347-367), with the disposition of each:

1. MAJOR (S2, S8), Q2 premise "MFFU support says it will not approve". Disposition: the question's text is the brief's and is kept as given; a wording note under Q2 now states that "will not approve" is the channel's reading (input :46, INFERRED) and quotes MFFU support's own words (input :33) and the team-review offer (input :17). The channel's readings at input :44-46 are also named as not adopted in the provenance paragraph.
2. MAJOR (S1), DECISION_LOG.md:849 quoted with no paste. Disposition: pasted in E9.
3. MINOR (S1), unpasted claims. Disposition: rubric length, input last byte, D-2026-11-11-A bounds, "V3 as clarified by V5", the guard's `State.DataLoaded` and order-boundary lines and the `accounttype` negative search are pasted in E9; "no team decision is on disk" is reworded to what the input's message list shows (E9).
4. MINOR (S8 leaning), G9 and Q1. Disposition: the G9 sentence saying the reply fills the gap design :110 names is replaced by a sentence routing that question to Q1; the "no word overnight" counter-fact is added to G9 and to Q1's facts, with pastes (E9).
5. MINOR (S2 hedging). Disposition: G7 hedged "if accurate (REPORTED BY)"; G9 says "the input gives, as MFFU support's text"; G5 says the C3.3 draft states the window and the sent text is REPORTED BY the channel.
6. MINOR (S2), D-071 line. Disposition: the S6 item now says the line is headed "reading (voice agent, notes-4)" and is REPORTED BY that agent.
7. MINOR (S6), OrdinalIgnoreCase. Disposition: S6 item 1 now states the comparison is case-insensitive.
8. MINOR (S2), "stretches" for Run 3. Disposition: G3 now says the Run 3 record shows at least one.
9. MINOR, input :44-46 not graded. Disposition: provenance paragraph names them as INFERRED and not adopted.
10. MINOR (S1), unused T1 count. Disposition: the command is dropped from E2/E3.
11. MINOR (structure), Questions not last. Disposition: moved after the evidence section, directly before the final line.

Pasted check that each fix is in the report (lines starting `$ ` are excluded so the commands do not count themselves):

```text
$ R=docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md
$ grep -v '^\$ ' $R | grep -c -F 'Wording note: Q2'"'"'s text is the brief'"'"'s, kept as given.'
1
$ grep -v '^\$ ' $R | grep -c -F 'a channel-reported instruction is recorded, not proven given'
2
$ grep -v '^\$ ' $R | grep -c -F 'Whether that text is the written MFFU answer design :110 asks for is Q1.'
1
$ grep -v '^\$ ' $R | grep -c -F 'That is the gap design :110 names'
0
$ grep -v '^\$ ' $R | grep -c -F 'Establishes, if accurate (REPORTED BY):'
2
$ grep -v '^\$ ' $R | grep -c -F 'the comparison is OrdinalIgnoreCase'
1
$ grep -v '^\$ ' $R | grep -c -F 'at least one (its longest flat period, 20.88 days)'
1
$ grep -v '^\$ ' $R | grep -c -F 'are not adopted by this unit'
1
$ grep -v '^\$ ' $R | grep -c -F 'T1|tier ?1'
0
$ grep -n -E '^## ' $R | tail -2
160:## Verification evidence (command output)
452:## Questions for Amear (his, not D2 items)
$ tail -n 1 $R | cut -c1-20
Fills are optimistic
```

Worker2 (re-check of findings 1, 2 and 11, report `docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md`): A, B and C held (Q2 keeps the brief's text and the wording note's quotes match input :33 and :17; the E9 paste of DECISION_LOG.md:849 re-ran exactly; the S13 sentence is once, on the last line, after the Questions section). It raised 1 MAJOR and 2 MINOR, with dispositions:

1. MAJOR (S8 leaning), Q1's quote of input :23 stopped at "from our team" and dropped the clause tying "overnight" to the daily close. Disposition: Q1 now quotes input :23 in full.
2. MINOR, G9 said the "not overnight" reading needs only design :25's gloss. Disposition: G9 now names both texts that bear on the link (design :25, INFERRED; input :23's clause, REPORTED BY) and says neither states it in terms. (Superseded at :80 by unit 2026-11-12-mffu-prepurchase-filing-resume: G9 now says the texts that bear on the link include design :25's gloss, design :110's clause and input :23's clause, and that none of them says it in terms.)
3. MINOR, "`Account.Name` occurs 7 times" is a line count. Disposition: reworded to "is on 7 lines, by `grep -c`".

(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)

## Files staged

None. The brief forbids staging. Working-tree changes by this unit: the input file is filed unedited (untracked; sha256 in E1 and E8); this report and the two worker reports are new and untracked; MANIFEST.md has four rows appended at the end (E7).

## Result

(manager did not return; completed by unit 2026-11-12-mffu-prepurchase-filing-resume — see docs/reports/2026-11-12-mffu-prepurchase-filing-resume-manager.md)

## Verification evidence (command output)

E0 — the replies and context lines, copied by script with line numbers:

```text
$ awk 'NR==3 || (NR>=8 && NR<=10) || NR==13 || NR==14 || (NR>=16 && NR<=27) || NR==29 || NR==30 || (NR>=32 && NR<=39) || NR==43 {print NR": "$0}' docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
3: Written by the Claude.ai Praxis channel at 2026-11-12T00:35Z for praxis-master to file. Not a DECISIONS.md entry; edits no ledger. Email text below was OBSERVED by the channel via the Gmail connector (Gmail thread `1a1ccc24a09baa1f`); on disk it is REPORTED BY the channel. MFFU's support rep display name is replaced by `[rep]`; no email addresses are written here (MFFU's public support address is named only as "MFFU support").
8: - Amear, chat 2026-11-11 17:37 ET, on sending the redrafted ticket (report `docs/reports/2026-11-11-mffu-connection-investigation.md` C3.3) as a new email with a "no account yet" first line: "yep".
9: - Amear, chat 17:40 ET, on replying to ask for a team review: "go".
10: - Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard.
13: 1. 2026-11-11T22:37:27Z, Amear → MFFU support, subject "Pre-purchase question: automated NinjaTrader strategy on evaluation and funded accounts". The C3.3 text, with these changes by the channel: first line "I don't have an account yet. I'm asking before I buy an evaluation."; the "Thank you for confirming…" paragraph dropped; risk checks named (daily loss limit, max trades per session, session time limits); "No copy trading, no third-party signals." added; "so I have a record before I buy" added to the closing. Five questions as C3.3.
14: 2. 2026-11-11T22:38:25Z, MFFU support ([rep]) → Amear. Verbatim:
16: 1. Automated setup on funded accounts
17:  Automated strategies are permitted on evaluation and funded accounts, subject to Fair Play rules: strategies must be tailored to your own settings, must not exploit favorable simulated fills, and high-frequency trading is prohibited. Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you've provided.
18:  2. NinjaTrader connection type on funded accounts
19:  I cannot confirm from available information whether funded accounts use the same "Simulation" connection type as evaluation accounts. This technical detail requires verification with our team.
20:  3. Inactivity notification for low-frequency strategies
21:  The 14-day recommended completion window for KYC is separate from the inactivity policy. Our inactivity rule applies after 7 consecutive calendar days without a trade. If your strategy may go longer than 7 days without a signal, contacting support to explain the situation is advisable, though I cannot guarantee an exemption or confirm that notification alone prevents closure.
22:  4. Overnight positions
23:  I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close.
24:  5. T1 news restrictions
25:  On Rapid Sim Funded and Pro Sim Funded, no positions or orders may remain open within the two-minute window before and after Tier 1 releases. Your strategy's 5-minute pre-release to 3-minute post-release flat window covers this requirement. The restriction does not prohibit trading at other times that day.
26:  Builder Sim Funded accounts are unrestricted for T1 news trading, subject to Fair Play rules.
27:  All evaluations, including Rapid and Pro evaluations, permit T1 news trading with Fair Play restrictions—the two-minute window does not apply at the evaluation stage.
29: 3. 2026-11-11T22:40:44Z, Amear → MFFU support (same thread): asks the team for a written decision on (1) the exact setup on Rapid, Pro and Builder Sim Funded; (2) unattended execution; (3) "Simulation" account type on funded accounts; (4) evening entry vs overnight.
30: 4. 2026-11-11T22:41:33Z, MFFU support ([rep]) → Amear. Verbatim:
32: 1. Automated strategy setup (Rapid, Pro and Builder Sim Funded)
33:  Automated strategies are permitted on MFFU accounts, including Evaluation, Sim Funded and Live, provided they follow the applicable rules. High‑frequency trading is prohibited, and strategies must not attempt to exploit favorable simulated fills. However, a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information. Automation is allowed in principle, but individual setups are not automatically approved.
34:  2. Running the strategy unattended during the session
35:  Automation is permitted, but the policy does not confirm whether unattended execution without supervision is allowed or required. The absence of a supervision rule does not establish permission for a specific unattended configuration.
36:  3. NinjaTrader connection account type
37:  When connecting NinjaTrader to your MFFU account, the connection should be configured with the account type set to Simulation in the NinjaTrader connection properties.
38:  4. Holding a position from 6:00 PM to before 9:30 AM the next day
39:  MFFU trading hours run from 6:00 PM to 4:10 PM Eastern Time. Positions must be closed by the 4:10 PM cutoff. A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close.
43: - Both replies came within about a minute of the outgoing mail; they read as automated assistant replies (INFERRED, not confirmed).
```

E1 — de-identification checks (a)-(c) on the input, with runtime controls (the token is never printed):

```text
$ F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ git rev-parse --short HEAD
ee54344
$ wc -l -c docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
      46    6510 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ git ls-files --error-unmatch docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md 2>&1 | head -1
error: pathspec 'docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md' did not match any file(s) known to git
$ shasum -a 256 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
# (a) email-address lines, then a control built at runtime
$ grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' $F
0
$ printf '%s@%s.%s\n' a b com | grep -cE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
1
# (b) rep first name, token built at runtime, never printed
$ TOK=$(ls docs/reports/evidence | grep mffu | head -1 | sed 's/.*mffu-//; s/-reply.*//'); echo "token length ${#TOK}"
token length 4
$ ls docs/reports/evidence | grep mffu | grep -ci -- "$TOK"
2
$ printf "x%sx\n" "$TOK" | grep -ci -- "$TOK"
1
$ grep -ci -- "$TOK" $F
0
# (c) IPv4 other than 127.0.0.1, MAC, key paths, each with a runtime control
$ grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' $F | grep -vc '^127\.0\.0\.1$'
0
$ printf '%s.%s.%s.%s\n' 10 0 0 7 | grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' | grep -vc '^127\.0\.0\.1$'
1
$ grep -ciE '\b([0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b' $F
0
$ printf '%s:%s:%s:%s:%s:%s\n' aa bb cc dd ee ff | grep -ciE '\b([0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b'
1
$ grep -ciE '(\.ssh/|id_rsa|id_ed25519|\.pem\b|authorized_keys|known_hosts)' $F
0
$ printf '%s\n' '~/.ssh/x' | grep -ciE '(\.ssh/|id_rsa|id_ed25519|\.pem\b|authorized_keys|known_hosts)'
1
```

E1d — check (d), the S13 sentence, compared by script against the rubric's text (the sentence is not printed here):

```text
$ F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ S=$(grep -o '"Fills are optimistic[^"]*"' specs/SPEC_RUBRIC.md | head -1 | tr -d '"'); echo "sentence length ${#S}"
sentence length 90
$ grep -cF -- "$S" $F
1
$ grep -nF -- "$S" $F | cut -d: -f1
5
$ sed -n 5p $F | cut -c1-21
Standing limitation: 
$ sed -n 5p $F | cut -c22- | cmp -s - <(printf "%s\n" "$S") && echo "line 5 after the label is byte-identical to the rubric sentence"
line 5 after the label is byte-identical to the rubric sentence
```

E2/E3 — R6 OPEN-1 and the T1 window (incl. the branch's `ninjascript/` file names, count only):

```text
$ D=docs/specs/2026-11-09-r6-announcement-research-design.md
# E2 R6 OPEN-1
$ git rev-parse --short r6/announcement-research
bf6fcc7
$ git grep -c "OPEN-1" HEAD -- docs/specs; echo "exit $?"
HEAD:docs/specs/2026-11-10-f2-session-flat-proposal.md:1
exit 0
$ git grep -c "OPEN-1" r6/announcement-research -- docs/specs
r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md:5
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==25 || NR==28 || NR==110 {print NR": "$0}'
25: - (iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED).
28: - **Strategy 1, Pre-Announcement Drift, evening entry, exit before the release:** ALLOWED by the T1 rule on every account (exit at T−5). Inside one MFFU session (18:00 → 16:10). Whether MFFU counts the evening entry as holding overnight is UNVERIFIED: MFFU's pages do not say, and a Rapid page says "Holding overnight will breach the account." (plans-site.txt:24). A written MFFU answer is needed before any funded use (OPEN-1).
110: | OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==15' | grep -o 'Trades may be placed[^"]*"\|All positions must be closed before the daily session close. Holding overnight will breach the account.'
Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST"
All positions must be closed before the daily session close. Holding overnight will breach the account.
$ sed -n 2131p DECISIONS.md | grep -o 'MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU.s written answer\|V3 does not close OPEN-1. R6 stays open pending MFFU.s written answer to OPEN-1'
MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer
V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1
# E3 T1 news window
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==22 || NR==66 {print NR": "$0}'
22: - (i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage.
66: - For every T1 release at time T on day E (CPI/NFP 08:30, FOMC statement or FOMC Minutes 14:00): exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2).
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==29' | grep -o 'All positions must be flattened at least two minutes prior to the scheduled T1 News event.\|On Builder Sim Funded, MFFU.s text conflicts (image banner vs Builder guides) → treated as blocked under (i) \[D1\]'
All positions must be flattened at least two minutes prior to the scheduled T1 News event.
On Builder Sim Funded, MFFU's text conflicts (image banner vs Builder guides) → treated as blocked under (i) [D1]
$ awk 'NR==1445 {print NR": "$0}' docs/reports/2026-11-11-mffu-connection-investigation.md
1445: 5. My strategy is flat from 5 minutes before each Tier 1 release until 3 minutes after it. On Rapid and Pro Sim Funded, does "trading on T1 news events is prohibited" mean anything more than that window, for example no trading at all that day? And are Builder Sim Funded accounts restricted or unrestricted?
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==29' | grep -o 'Allowed by the T1 rule in evaluations, Studio and Live per MFFU.s text'
Allowed by the T1 rule in evaluations, Studio and Live per MFFU's text
$ git ls-tree -r --name-only r6/announcement-research -- ninjascript | grep -c -i -E 'announce|drift|premium|r6'; echo "exit $?"
0
exit 1
$ git ls-tree -r --name-only r6/announcement-research -- ninjascript | wc -l
       5
```

E3b/E4/E5/E6 — main-branch news search, consumer guard, D-071, inactivity and trade frequency, Rule F2-1, rubric F2 and F4:

```text
$ D=docs/specs/2026-11-09-r6-announcement-research-design.md
$ I=docs/reports/2026-11-11-mffu-connection-investigation.md
# E3b main branch: no news window in the specs
$ git grep -c -i "news" HEAD -- docs/specs specs; echo "exit $?"
exit 1
$ git grep -n 'OPEN-1' HEAD -- docs/specs | grep -o 'Whether MFFU counts an evening entry as "holding overnight" is R6.s OPEN-1'
Whether MFFU counts an evening entry as "holding overnight" is R6's OPEN-1
# E4 consumer Sim-only guard and D-071
$ grep -n -E "RequiredAccountPrefix|HARD SCOPE WALL" ninjascript/PraxisSignalConsumer.cs
39:// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
48:		private const string RequiredAccountPrefix = "Sim";
100:					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
106:						+ RequiredAccountPrefix + "'). No signals will be processed. SIM ONLY.", LogLevel.Error);
639:				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
$ grep -n -o 'An MFFU evaluation or funded account is not a "Sim…" account in NT8 terms, so the consumer would refuse to trade it. Going live needs someone to change that guard on purpose. That change is Amear.s under D2(b)' $I
347:An MFFU evaluation or funded account is not a "Sim…" account in NT8 terms, so the consumer would refuse to trade it. Going live needs someone to change that guard on purpose. That change is Amear's under D2(b)
$ awk 'NR==318 {print NR": "$0}' $I
318: - No change to the consumer's Sim-only guard is proposed or drafted. That change is Amear's under D2(b) (C1.1).
$ grep -n -o 'Set Account Type to `"Simulation"` \[OBSERVED\]' $I
118:Set Account Type to `"Simulation"` [OBSERVED]
$ grep -n -o 'The article tells every reader to set "Simulation" and gives no condition.' $I
979:The article tells every reader to set "Simulation" and gives no condition.
$ awk 'NR==950 {print NR": "$0}' DECISIONS.md
950:   - reading (voice agent, notes-4): **The MFFU Rithmic connection is approved to be opened when Block 4 starts.** D-071 (Simulated Data Feed only) stands until then.
# E5 inactivity and trade frequency
$ git show r6/announcement-research:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==96 || NR==103 {print NR": "$0}'
96: - Inactivity (7 calendar days): of 173 gaps between consecutive event dates in range, 90 exceed 7 days and the longest is 37 (E8). A standalone event strategy therefore fails the inactivity rule on Sim Funded accounts. It is judged as failing standalone and is then evaluated only as an overlay on an account that trades on other days; no invented "keep-alive" trades [D1].
103: - Trade counts (E8): events on data sessions in range — FOMC 42, CPI 63, NFP 61. Inside the OOS span 2022-03-17 → 2026-06-05: FOMC 33, CPI 50, NFP 49; union 131 distinct dates (ALFRED doubling inflates CPI/NFP by a few). Per OOS window: FOMC 1-2, CPI 2-4, NFP 2-4. Per year about 8 FOMC + 12 CPI + 12 NFP, union 30-34 dates.
$ grep -n -o 'If you do not place a trade within 7 consecutive calendar days on your sim funded account, the account will be closed due to inactivity.' $I
1380:If you do not place a trade within 7 consecutive calendar days on your sim funded account, the account will be closed due to inactivity.
$ awk 'NR==69 || NR==89 {print NR": "$0}' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
69: | Avg. # of trades per day | 0.81 | 0.39 | 0.42 |
89: - 0.81 trades/day over 2021-03-08 → 2026-07-17 is consistent with 1,075 trades (≈1,330 trading days). The paper's SPY figure is 1.3–1.8/day — an order-of-magnitude tripwire only (3gm report, checklist §B.7).
# E6 Rule F2-1, rubric F2
$ awk 'NR==2111 {print NR": "$0}' DECISIONS.md
2111: **Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
$ awk 'NR==2101 {print NR": "$0}' DECISIONS.md
2101: ## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.
$ awk 'NR>=30 && NR<=31 {print NR": "$0}' specs/SPEC_RUBRIC.md
30: **Unblocks when.** A DECISIONS.md entry names the governing rule and the
31: 15:00 disposition, and breaker specs #4 and #5 are amended to match.
$ sed -n 2172p DECISIONS.md | grep -o 'Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).'
Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET).
# E6 rubric F4 and rubric edit rule
$ awk 'NR>=48 && NR<=57 {print NR": "$0}' specs/SPEC_RUBRIC.md
48: ### F4 — MFFU automation compliance
49: **Criterion.** Written confirmation from MFFU that this specific automation
50: pattern is permitted on a funded account.
51: **Why frozen.** Flagged as blocking in the Round 1+2 compilation, still open in
52: the Phase 2 closure document, still open in the Phase 3 output summary, absent
53: from the session-28 build report. The plan documents also contradict each
54: other: the Round 3 handoff asserts automation is explicitly permitted; Phase 2
55: closure states it has not been confirmed by direct inquiry.
56: **Owner.** Amear. Not a build task — an email.
57: **Blocks.** Block 4. Block 5.
$ awk 'NR>=3 && NR<=6 {print NR": "$0}' specs/SPEC_RUBRIC.md
3: Authority: the scoping agent (Claude.ai) via Amear. Amear decides; agents write.
4: Amear does not edit this file by hand. Every edit cites a logged Amear approval
5: inline and passes the auditor before commit (D-2026-11-08-B A11; DECISION_LOG
6: 2026-11-08T15:05:00Z, WHO: amear).
```

```text
# E6 (continued) breaker #4/#5 text; E5 (continued) Run 3 gap search
$ sed -n 2108p DECISIONS.md | grep -o 'The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry.'
The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry.
$ grep -c -i -E 'gap|days without|longest' docs/reports/2026-10-30-run3-backtest-screenshot-record.md; echo "exit $?"
1
exit 0
$ awk 'NR==1 {print NR": "$0}' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
1: # Run 3 — Strategy Analyzer Summary, transcribed from Amear's screenshot
```

E5b — Run 3 record (strategy, trade count, trades per day, longest flat period):

```text
$ R=docs/reports/2026-10-30-run3-backtest-screenshot-record.md
$ awk 'NR==13 || NR==16 || NR==39 || NR==55 || NR==69 || NR==74 {print NR": "$0}' $R
13: | General | Strategy | PraxisNoiseAreaBreakout |
16: | Data Series | Instrument | NQCONT |
39: | Performance | All trades | Long trades | Short trades |
55: | Total # of trades | 1075 | 522 | 553 |
69: | Avg. # of trades per day | 0.81 | 0.39 | 0.42 |
74: | Longest flat period | 20.88 days | 30.94 days | 34.98 days |
```

E7 — MANIFEST.md append (before/after diff):

```text
$ diff /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md; echo "exit $?"
426a427,430
> | /docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | Report | 3 | 2026-11-12 | Return handoff from the Claude.ai Praxis channel: Amear's authority for the MFFU pre-purchase email (no MFFU account), the outgoing messages summarised, MFFU support's two replies of 2026-11-11 verbatim (rep name replaced by [rep]), the channel's INFERRED reading; filed unedited by unit 2026-11-12-mffu-prepurchase-filing after de-identification checks (0 email lines, 0 rep-name hits, 0 IPv4/MAC/key paths, S13 sentence once at :5); ungraded at time of row |
> | /docs/reports/2026-11-12-mffu-prepurchase-filing-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-mffu-prepurchase-filing: de-identification checks, grading of each MFFU reply statement against R6 OPEN-1, the R6 T1 window, the consumer Sim-only guard (S6), the inactivity rule, Rule F2-1 and F4 (F4 stays FROZEN / NOT MET); Questions for Amear Q1 (OPEN-1) and Q2 (F4 bar), no recommendation; ungraded at time of row |
> | /docs/reports/2026-11-12-mffu-prepurchase-filing-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-mffu-prepurchase-filing: check of the manager report for S1, S2, S8, email addresses, the rep's name, placeholder commands and S13 placement; ungraded at time of row |
> | /docs/reports/2026-11-12-mffu-prepurchase-filing-worker2.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 2 report for unit 2026-11-12-mffu-prepurchase-filing: narrow re-check of the two MAJOR fixes (Q2 wording note, DECISION_LOG.md:849 paste) and the moved Questions section; ungraded at time of row |
exit 1
$ wc -l /tmp/mffu-prepurchase-MANIFEST.before MANIFEST.md
     426 /tmp/mffu-prepurchase-MANIFEST.before
     430 MANIFEST.md
     856 total
$ head -n 426 MANIFEST.md | cmp - /tmp/mffu-prepurchase-MANIFEST.before && echo "first 426 lines byte-identical"
first 426 lines byte-identical
```

E8 — input unchanged at end of unit:

```text
$ shasum -a 256 docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
9eedfe85c125fc5be2eb5686b5b9df41dd42e5d9463c2309891561b5b2493598  docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
```

E9 — authority row, rubric length, input last byte and message list, the word "overnight" in reply 2 point 4, D-2026-11-11-A bounds, the guard's checks:

```text
$ F=docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md
$ I=docs/reports/2026-11-11-mffu-connection-investigation.md
# E9 authority row, rubric length, input last byte, message list
$ sed -n 849p DECISION_LOG.md | grep -o -E '^- \[2026-11-12T02:41:00Z\] WHO: amear|a channel-reported instruction is recorded, not proven given'
- [2026-11-12T02:41:00Z] WHO: amear
a channel-reported instruction is recorded, not proven given
$ wc -l specs/SPEC_RUBRIC.md
     461 specs/SPEC_RUBRIC.md
$ tail -c 1 $F | od -c | head -1
0000000   \n                                                            
$ grep -n -E '^[0-9]+\. 2026-11-11T' $F | cut -c1-60
13:1. 2026-11-11T22:37:27Z, Amear → MFFU support, subject 
14:2. 2026-11-11T22:38:25Z, MFFU support ([rep]) → Amear. 
29:3. 2026-11-11T22:40:44Z, Amear → MFFU support (same thr
30:4. 2026-11-11T22:41:33Z, MFFU support ([rep]) → Amear. 
# E9 the word overnight in reply 2 point 4, and the question as sent in the C3.3 draft
$ awk 'NR>=38 && NR<=39' $F | grep -c -i overnight
0
$ awk 'NR>=38 && NR<=39' $F | grep -c -i 'daily close'
1
$ awk 'NR==1444 {print NR": "$0}' $I
1444: 4. Does a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day count as holding overnight? It is never held past your 4:10 PM ET close.
# E9 Rule F2-1 sits inside D-2026-11-11-A; V3 with V5
$ awk 'NR>=2101 && /^## /{print NR": "substr($0,1,60)}' DECISIONS.md | head -2
2101: ## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (C
2176: ## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lif
$ sed -n 2131p DECISIONS.md | grep -o 'V3 as clarified by V5 — overnight holding.'
V3 as clarified by V5 — overnight holding.
# E9 the guard: where it is checked, and what it reads
$ awk 'NR==96 || NR==100 || NR==637 || NR==639 {print NR": "$0}' ninjascript/PraxisSignalConsumer.cs
96: 			else if (State == State.DataLoaded)
100: 					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
637: 			// Defense in depth: re-assert the sim wall at the order boundary.
639: 				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
$ grep -c -i "accounttype" ninjascript/PraxisSignalConsumer.cs; echo "exit $?"
0
exit 1
$ grep -c "Account.Name" ninjascript/PraxisSignalConsumer.cs
7
$ grep -oF "Account.Name" ninjascript/PraxisSignalConsumer.cs | wc -l | tr -d ' '
8
```

## Questions for Amear (his, not D2 items)

Q1. Does MFFU support's reply of 2026-11-11T22:41:33Z, point 4, close R6 OPEN-1?

Facts that bear on it (E0, E2):
- The reply, input :39: "A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close."
- OPEN-1, R6 design :110 (`bf6fcc7`), in full: ""Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use."
- The design's gloss, :25: "(iv) "Overnight" in the FAQs = across the daily session close (the FAQ's own gloss, INFERRED)."
- The earlier reply, input :23, in full: "I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close."
- DECISIONS.md:2131 ("V3 as clarified by V5", E9): "evening entries stand on MFFU's written answer"; "V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1".
- The reply does not use the word "overnight" (E9: 0 hits on input :38-39); the C3.3 draft's question 4 asked whether such a position would "count as holding overnight" (E9: investigation :1444).
- Provenance: REPORTED BY the channel; the channel reads both replies as automated assistant replies (input :43, INFERRED).

Q2. Should F4's bar change, given that MFFU support says it will not approve a specific configuration in writing?

Facts that bear on it (E0, E6):
- Wording note: Q2's text is the brief's, kept as given. The words "will not approve" are the channel's reading (input :46, INFERRED). MFFU support's own text is "cannot be approved in writing from the available information" (input :33), and the earlier reply offers a team review (input :17).
- F4, rubric :49-50: "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." Owner, rubric :56: "Amear. Not a build task — an email."
- Input :33: "a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information."
- Input :17: "Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you've provided."
- Input :35: "the policy does not confirm whether unattended execution without supervision is allowed or required."
- The rubric file says Amear does not edit it by hand and every edit cites a logged Amear approval (rubric :3-6, E6).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
