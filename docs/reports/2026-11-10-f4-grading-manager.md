# F4 comparison report: MFFU's written words against the D-2026-11-10-B pattern

**Unit.** `2026-11-10-f4-grading`. **Role.** praxis-manager. **Started.** 2026-11-10T17:02:44Z (`date -u`).
**Baseline.** HEAD `d30ab4d`; the index holds one path (the held-out PNG), pasted in V0.

This report compares. It does not grade F4 and recommends no state for F4. F4 stays FROZEN in `specs/SPEC_RUBRIC.md`. Coverage labels are limited to COVERED-EXPLICITLY, COVERED-BY-INFERENCE, NOT ADDRESSED and CONTRADICTED.

**De-identification.** No support representative's name, no email address, and no mail-thread identifier is written in this report. Where a source line carries one, the name is replaced by `[rep name]`, the trader's name by `[trader]`, and addresses by `[address]`; every such substitution is marked "de-identified". One HEAD path carries a representative's first name in its file name; it is called "the 2026-10-28 reply-filing report" here, and commands resolve it by glob (`2026-10-28-f4-*-reply-filing.md`) so the name is not printed. The PNG and transcript paths are likewise written as `docs/reports/evidence/2026-10-28-mffu-[name]-reply.png` / `...-transcript.md`.

## Task

Set what MFFU actually said in writing, quoted verbatim, against each element of the PRAXIS automation pattern named in D-2026-11-10-B (DECISIONS.md :2054, fallback :2056), and record the outgoing question, each reply's date, channel and author type, the account types each reply speaks to, and any plan document that still claims F4 closed. F4 criterion (specs/SPEC_RUBRIC.md :48–57, pasted in V1): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account."

## Rubric criteria addressed

- F4 is the subject matter only. It is not graded here.
- S1 (pasted output for every claim) and S2 (no element graded above what the words support), as the brief names them. S6 cross-block note below. The rubric lines are pasted in V1.

## Workers dispatched

| Id | Mode | Scope | Outcome | Report |
|---|---|---|---|---|
| worker1 | BUILD | full evidence extraction | Stopped at its 40-turn cap; 22-line skeleton only. Not relied on. | `docs/reports/2026-11-10-f4-grading-worker1.md` |
| worker2 | BUILD | outgoing-inquiry search; F4-closed search; A15 | Returned PASS on its brief. Decisive lines re-run by the manager (V9, V10). | `docs/reports/2026-11-10-f4-grading-worker2.md` |
| worker4 | ADVERSARIAL | rows 2, 4, 13, 14a, 14b, the notes under the table, the inquiry section, after the worker 3 fixes | Returned FAIL: 1 blocking, 3 minor. All four fixed (below). No third pass. | `docs/reports/2026-11-10-f4-grading-worker4.md` |
| worker3 | ADVERSARIAL | S2 labels, quote fidelity, factual claims, personal data, forbidden content, on the draft of this report | Returned FAIL on the draft: 3 blocking, 6 minor. All nine fixed (below). | `docs/reports/2026-11-10-f4-grading-worker3.md` |

## Process log

- 17:02Z baseline captured (V0). Rubric F4 read (V1).
- Worker 1 (BUILD, extraction) stopped at its 40-turn cap with only a 22-line skeleton written. Its file is left as it is; nothing in this report rests on it.
- Worker 2 (BUILD, narrow: outgoing-inquiry search and F4-closed search) dispatched.
- Worker 2 returned; manager re-ran its decisive lines (V9, V10) and wrote the inquiry and F4-closed sections.
- Worker 3 (ADVERSARIAL) attacked the draft; nine findings fixed by the manager (Adversary findings and fixes).
- Worker 4 (ADVERSARIAL) re-attacked the fixed rows and the inquiry section; four findings fixed. Final checks in V11.
- Manager read the HEAD transcript, the 2026-08-07 F4 report §0–§3.5 and addendum, the HEAD blob of the 2026-10-28 reply-filing report, the two authorising DECISION_LOG rows, the D-2026-11-10-B text, the topology spec, and the R6 branch MFFU captures (V2–V8).

## Inquiry as sent (verbatim, de-identified)

**No complete text of any outgoing message to MFFU is on disk at HEAD.** The only verbatim outgoing fragment is the truncated screenshot preview (third table row), which ends mid-sentence. Worker 2 searched for it (outreach, eight-firm, inquiry/enquiry, Earn2Trade, follow-up with MFFU, both authorising timestamps, "NinjaTrader 8 + Rithmic"), and its positive controls hit (worker 2 report Blocks 1, 6). The manager re-ran the decisive lines (V9). What exists:

| Message | What is on disk | Source (HEAD) | Verbatim? |
|---|---|---|---|
| Initial inquiry, "2026-07-26 window", one of eight firms | Purpose only: "the outreach was run to establish whether the PRAXIS automation pattern is permitted per-firm"; "an English inquiry"; earlier, "the MFFU inquiry email are the TRADER'S actions to execute" | ISSUE_REGISTER.md :70; DECISION_LOG.md :46 | No. Neither line says what the email described: no platform, route or architecture is recorded. |
| Follow-up, 2026-08-07 | Description: "A follow-up email naming the actual architecture, and asking the policy's effective date, was **sent 2026-08-07**"; HANDOFF :764 "Follow-up sent 2026-08-07, awaiting reply." | HANDOFF.md :784, :764 | No. The description is the master's ledger text, not the email. Which architecture it named is not recorded. |
| The message shown above reply 2 in the screenshot | Collapsed preview only, truncated in the image: "Hi [rep name] — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f" (de-identified at "[rep name]") | transcript fence line 2 (file :16) | Yes, as far as visible. Ends at "is f". That it is the 2026-08-07 follow-up is an inference from its wording ("thanks for confirming", "Two follow-ups"); nothing on disk dates it. |
| Follow-up ruled 2026-10-28, "naming NinjaTrader 8 + Rithmic" | Ruling only. Whether it was sent: "Does Amear send the follow-up himself" (DECISIONS :539); "Whether Amear sends the follow-up himself is unconfirmed" (voice-session-notes-3 :44) | DECISION_LOG.md :435; DECISIONS.md :539 | No text on disk. Sending not recorded. |

**Consequence for the comparison, stated as a fact about the record:** the outgoing description cannot be set against D-2026-11-10-B element by element, because no outgoing description is on disk. Every visible fragment of an outgoing question predates D-2026-11-10-B (2026-11-10), so no message on disk could have described the NT8-emitter topology it names. The element table therefore compares MFFU's replies (what was answered), not the questions.

## Replies (verbatim, de-identified, date, channel, human or automated)

### Reply 1 (relayed, not on disk as a source)

Quoted in `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` §1 (:28–29, V3), as text Amear pasted in-session. The report itself labels it "UNVERIFIED — relayed, not independently confirmed" and states no agent opened the mail thread (:12–16).

> "Algo trading is now permitted at MFFU moving forward on all plans including
> the evaluation, simulated-funded and live account stages."

- **Date as recorded:** 2026-07-26T21:20:22Z (report §1 table :35; DECISION_LOG :177), "UNVERIFIED — relayed".
- **Channel as recorded:** email; the relayed sender domain is MFFU's Intercom mail domain `myfundedfutures.intercom-mail.com` (address de-identified). Relayed, not header-verified.
- **Human or automated:** recorded as "human support rep" (§1 table :36), "UNVERIFIED — relayed". DECISION_LOG :177 says "by a human rep". Nothing on disk shows how that was established.
- **Restrictions as relayed (§1.1 :44–46):** no high-frequency trading; automated tools may not be built to exploit sim-environment fill favorability; live automation must follow CME guidelines.
- **Points to:** the help-centre article `8444599-fair-play-and-prohibited-trading-practices` (§1 table :37, "URL not fetched").

### Reply 2 (screenshot, transcribed)

Source: HEAD transcript `docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md`, file lines 15–39, the `text` fence (V2). Substantive lines, verbatim (file lines 27–33):

> You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
> • Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
> • Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
> • High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
> • For live accounts, automated trading must comply with CME guidelines.
>
> You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices

- **Date:** not visible. Transcript :64 "The date and time of either message. No timestamp appears in the screenshot." The screenshot file was taken 2026-10-28 (filename, transcript :3); that is the capture date, not the send date.
- **Channel:** email shown in a Gmail view; sender display domain `myfundedfutures.intercom-mail.com` (transcript :18, address de-identified); transcript :65 "It has not been checked as a sending domain." Headers not visible.
- **Human or automated:** not established. The record shows templated-text markers: three openers, and a body name that differs from the sender and signature name (transcript :21–25 and :36; F4 report addendum §E). The addendum labels the boilerplate reading "Inference, not observed" (§E item 2). DECISION_LOG :435 calls the name mismatch a "boilerplate indicator". Whether a person or an automated system composed it is not visible.
- **Whether it answers the outgoing question:** not established. The question it follows is truncated (see "Inquiry as sent").

### MFFU published text (not a reply; supporting context only)

The help-centre article both replies link to was fetched by the R6 unit on branch `r6/announcement-research` (`bf6fcc7`), not on `main`. Capture header: `FETCHED_UTC: Mon Nov  9 09:06:24 UTC 2026`, `HTTP: 200` (V8). Its automation section, verbatim:

> Section 1: Automated Trading Protocols
> High-frequency Trading is not allowed on our plans.
> Traders may make use of automated trading strategies tailored to their own specific settings so long as these automated tools do not aim to exploit the favorable fills offered in the Simulated Environment.
> Traders trading live accounts with automated trading must abide by CME guidelines.

This is a public page addressed to nobody. It is not written confirmation to the trader and is not one of the replies. It is listed because it bears on automation permission and is MFFU's own text.

## Element table

The pattern under comparison is D-2026-11-10-B option 1 (DECISIONS.md :2054) with fallback option 3 (:2056), and the order route of CLAUDE.md :21 / topology spec :41 (V5, V6). "R1" is reply 1 (relayed), "R2" is reply 2 (screenshot), "P" is the published page (R6 branch, context only). Term counts for R2 are in V7.

| # | Pattern element | MFFU words that bear on it (verbatim) | Label | What the label rests on |
|---|---|---|---|---|
| 1 | Automated trading in general (algo trading permitted at all) | R1: "Algo trading is now permitted at MFFU moving forward on all plans"; R2: "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages."; P: "Traders may make use of automated trading strategies" | COVERED-EXPLICITLY | The words name algo/automated trading as permitted. This row is the general activity only, not any component of this pattern. R1 is relayed (UNVERIFIED). |
| 2 | Fully automated order submission, no human click per order (`SubmitBracket` in `PraxisSignalConsumer.cs` places entry plus stop and target), taken apart from the platform (row 3) and the route (row 8) | R2: "for fully automated order execution"; "This enables your custom software to submit orders, manage positions" | COVERED-BY-INFERENCE | The explicit words sit inside the Tradovate API sentences ("custom Tradovate API access", "via the Tradovate API"). Outside those sentences, the step needed is the inference that "Algo trading" in the platform-free bullet ("Algo trading is permitted on all plans", R2 bullet 2; R1) includes order submission by software with no per-order human action. No MFFU line defines "algo trading". The inference says nothing about route or platform; those stay NOT ADDRESSED (rows 3, 8). |
| 3 | NinjaTrader 8 as the platform that places orders | none: R2 has 0 lines for NinjaTrader, NT8, Ninja (V7) | NOT ADDRESSED | Zero hits in the R2 fence; R1 as relayed names no platform (V3); P names no platform. |
| 4 | An automated strategy that submits orders, taken apart from the platform it runs on (the platform is row 3) | R2: "integrate your trading bot or automated strategy via the Tradovate API"; P: "automated trading strategies tailored to their own specific settings" | COVERED-BY-INFERENCE | "automated strategy" is named, but in R2 only "via the Tradovate API". P is general and names no platform. The inference is that "Algo trading" (R2 bullet 2, R1) covers a strategy that submits its own orders. It says nothing about the platform (row 3) or route (row 8), which stay NOT ADDRESSED. P is context only. |
| 5 | Signal computed by a separate NT8 emitter strategy that places no orders and HTTP-POSTs to a local webhook | none | NOT ADDRESSED | No line in R1, R2 or P describes signal emission separated from order placement, webhooks (R2 webhook = 0, V7), or HTTP. |
| 6 | External program (n8n, with Redis breaker gates) decides whether a trade goes ahead and writes a JSON file that NT8 picks up and acts on | R2: "your custom software to submit orders" (Tradovate API sentence) | NOT ADDRESSED | R2 n8n = 0, file = see V7; "custom software" in R2 is the software that submits orders "via the Tradovate API", not software that hands decisions to a trading platform through files. Reading this element in requires taking "Algo trading" to cover every architecture; the words do not describe one. |
| 7 | Trader-built automated risk gates (nine breakers, default closed) | R2: "You are responsible for the performance and reliability of your automated system." | NOT ADDRESSED | The sentence assigns responsibility; it says nothing about gating components. Recorded as a condition, not as coverage. |
| 8 | Rithmic as the connection / order route (NT8 → Rithmic → MFFU) | none: R2 Rithmic = 0 (V7); R2 names the Tradovate API and "Tradovate evaluation and funded accounts" | NOT ADDRESSED | No MFFU line names Rithmic. R2's only named route is Tradovate. R2 does not say a non-Tradovate route is barred, so the label is not CONTRADICTED. Whether the trader's account is Tradovate- or Rithmic-routed is not established on disk (F4 report addendum §C row 2). |
| 9 | TradingView alert as emitter (CLAUDE.md :21 flow; not on the D-2026-11-10-B live path, topology spec 1.5) | none: R2 TradingView = 0 (V7) | NOT ADDRESSED | Listed because CLAUDE.md still names it. |
| 10 | Evaluation account | R1: "the evaluation, simulated-funded and live account stages"; R2: "Algo trading is permitted on all plans, including evaluation"; R2: "your MyFundedFutures Tradovate evaluation and funded accounts" | COVERED-EXPLICITLY | For algo trading in general (row 1), not for rows 2–9. |
| 11 | Sim-funded account | R1: "simulated-funded"; R2: "simulated-funded" | COVERED-EXPLICITLY | Same scope note as row 10. |
| 12 | Live funded account (F4's "on a funded account") | R1: "live account stages"; R2: "live account stages"; R2: "For live accounts, automated trading must comply with CME guidelines." | COVERED-EXPLICITLY | Same scope note as row 10. R2's "Tradovate evaluation and funded accounts" can be read as Tradovate-only (F4 addendum §C row 2); the "all plans ... live account stages" bullet carries no platform word. |
| 13 | The trader's own account, opened before any "now permitted" change | R1: "now permitted", "moving forward", "on all plans"; R2: "on all plans", "your MyFundedFutures Tradovate evaluation and funded accounts" | NOT ADDRESSED | The R1 words bear on timing but give no effective date; "on all plans" names plan types, not account opening dates, and says nothing on accounts opened before a change; the R2 words are second-person and generic and name no account. Neither reply names an account or an effective date (F4 report §3.2; addendum §C rows 3–4). |
| 14a | Fallback option 3, automation part: one strategy computes the signal, gates itself, and calls its own `EnterLong` / `EnterShort` | as rows 1, 2, 4 | COVERED-BY-INFERENCE | Same inference as rows 2 and 4 (that "Algo trading" covers a strategy that submits its own orders). The inference says nothing about platform or route; those are row 14b. |
| 14b | Fallback option 3, platform and route part: that strategy is NinjaScript in NT8, routed NT8 → Rithmic | none: R2 NinjaTrader, NT8, Ninja, Rithmic = 0 (V7) | NOT ADDRESSED | As rows 3 and 8. |

**Read as a whole.** This report does not combine the row labels into one label for the pattern. Rows 3, 5, 6, 7, 8, 9, 13 and 14b are NOT ADDRESSED.

**CONTRADICTED.** No row carries it. No line in R1 or R2 prohibits any element. In P (context only, R6 branch), two lines bear on the pattern and are recorded here without a label, because neither names automation:

> Each individual trader is required to maintain their own individual trading activity. Meaning, entering, exiting and cancelling their own trade executions. Traders are not permitted to copy trade one another by entering, exiting or cancelling trade positions.

(P, "Section 4: Device Sharing & Copy-Trading other Traders", capture :98 heading, :100 text). Read apart from its copy-trading heading, "entering, exiting and cancelling their own trade executions" could be taken to bear on row 2. Section 1 of the same page permits automated trading strategies. Which reading MFFU intends is not stated (Open question 9).

> ● Slippage and Bracket Usage: Exploiting the absence of slippage and utilizing tight brackets to gain from favorable fills are not permitted.

(P, Section 2, capture :87). It bears on row 2, because `SubmitBracket` places bracket orders. It is a condition on how brackets are used, not a ban on brackets.

**Conditions recorded, not assessed.** R1 (relayed) and R2: no HFT; no automated tools that exploit favourable sim fills; CME guidelines on live accounts; R2 adds that the trader is responsible for the system. P adds, among others: no multiple limit orders at one price to manipulate fills; no profiting from gapped or illiquid fills; the tight-bracket line above; "Engaging in trades during tier 1 economic data releases is restricted."; no collaborative trading; "MyFunded Futures prohibits hedging of any kind." This report does not assess PRAXIS against any of them (see Open questions and S6). Line numbers in V8b.

## Account-type scope

| Source | Account types named, verbatim | Platform qualifier in the same sentence |
|---|---|---|
| R1 (relayed) | "evaluation, simulated-funded and live account stages" | none as relayed |
| R2 sentence 1 | "your MyFundedFutures Tradovate evaluation and funded accounts" | "Tradovate" (scope over "funded accounts" ambiguous) |
| R2 bullet 2 | "evaluation, simulated-funded, and live account stages" | none |
| R2 bullet 4 | "For live accounts" | none (condition: CME guidelines) |
| P (R6 branch) | "on our plans"; "Traders trading live accounts with automated trading" | none |

Pasted in V2, V3, V8.

## Plan documents that claim F4 closed

One HEAD document calls F4 closed in its own words. Quoted, not adopted:

> `docs/reports/2026-11-08-strategy-filter-audit.md:68`: "| A15 | Low frequency to reduce prop-firm detection risk | D3 §1 and §6 Scenario B | Was A at the time. **Now void:** MFFU permits automation in writing (F4 closed; repo F4 evidence). |"

Two HEAD documents flag that row as in conflict with the rubric: DECISION_LOG.md :801 ("F4 is called "closed" in the strategy filter audit's row A15 while the rubric holds F4 FROZEN (recorded; the rubric governs)") and `docs/reports/2026-11-10-f1-f2-proposal-manager.md:36`. The rubric at HEAD has `### F4` at :48, inside `## FROZEN` (:17) and above `## PASSED` (:61) (V10).

Other HEAD lines say MFFU confirmed or permits algo trading while stating F4 stays FROZEN: HANDOFF.md :764, :784; DECISION_LOG.md :177, :179; ISSUE_REGISTER.md :68 (worker 2 Block 8; :764, :784 and :177, :179 re-run in V4 and V9). Hits that use "F4" for a different item (a20-adversarial-2 :101 "F4 | RESOLVED"; r8j-phase3-import §F4.x) are not the rubric's F4 (worker 2 Block 8, worker's own figures, not re-run).

The worker found that `git grep -E '\bF4\b'` returns 0 lines on this machine while `-w` returns 634 (worker 2 Block 7). That figure is the worker's; the A15 line itself is re-run in V10.

Counter-record, quoted as a fact and not adopted as a grade: DECISION_LOG.md :179, Amear 2026-08-07T18:37:25Z, "TWO RULINGS. (1) MFFU's general permission does NOT satisfy F4 — F4 STAYS FROZEN and a follow-up email naming the specific automation pattern is authorised." (bold markers dropped; V4). DECISION_LOG.md :435, Amear 2026-10-28T20:54:29Z: "F4 evidence: FILE the MFFU "[rep name]" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN." (de-identified at "[rep name]"; bold markers dropped; V4).

## Adversary findings and fixes

Worker 3 attacked the draft and was given the artifact and the criteria, not the manager's reasoning. Its findings (its report holds the command output) and what the manager did:

| # | Severity | Finding | Fix |
|---|---|---|---|
| 1 | BLOCKING | A banned word reached the draft through the pasted cut of DECISION_LOG :179 in V4. | V4 re-run with :179 cut at 345 characters, before the word. V11 shows 0 hits. |
| 2 | BLOCKING | Row 14 (fallback) was COVERED-BY-INFERENCE although its platform and route parts are NOT ADDRESSED; row 4 named NT8 while row 3 (NT8) was NOT ADDRESSED, so two labels rested on one inference. | Row 4 restated without the platform (the platform is row 3). Row 14 split: 14a automation part COVERED-BY-INFERENCE, 14b NT8/Rithmic part NOT ADDRESSED. Added a "Read as a whole" note that row labels are not combined. (A citation of the addendum's own single label was added here and then removed after worker 4, see below; the V8b line for :634 is left as captured.) |
| 3 | BLOCKING | The bold line said no verbatim outgoing text exists, while the table showed a verbatim preview. | Now reads "No complete text"; the truncated preview is named as the only verbatim fragment. |
| 4 | MINOR | "fence lines 15–39 / 27–33" were file line numbers. | Now "file lines". |
| 5 | MINOR | DECISION_LOG :179 quote added a closing bold marker. | Bold markers dropped from the quote, and the drop noted. |
| 6 | MINOR | DECISION_LOG :435 quote dropped the quote marks round the name token. | Restored as "[rep name]". |
| 7 | MINOR | Row 10 quoted a shortened string with "..." inside quote marks (0 source hits). | Replaced by the full source string. |
| 8 | MINOR | Row 13 listed no MFFU words although "now permitted", "moving forward" and "your ... accounts" bear on it. | Row 13 now quotes them; label unchanged (NOT ADDRESSED), reason stated. |
| 9 | MINOR | The published page has further conditions (tight brackets, tier-1 data, Section 4 own-executions line, hedging); "no MFFU line prohibits any element" was not checked against Section 4. | Section 4 and the bracket line quoted under the table, unlabeled, with an open question; the other conditions listed as recorded, not assessed; the CONTRADICTED sentence narrowed to R1 and R2. |

Worker 3 found no personal-data leak in this draft or the worker 1 and worker 2 reports, and its re-run of the V7 term counts matched. It noted its F4-closed search used a fixed word list, so other phrasings could slip past.

**Second adversarial pass (worker 4, scoped to the fixed rows and the inquiry section).** It returned FAIL on 1 blocking and 3 minor findings. Fixed by the manager:

| # | Severity | Finding | Fix |
|---|---|---|---|
| 4.1 | BLOCKING | Rows 2 and 14a stated their inference as reaching orders "by any route" / "by a non-Tradovate route", while the route is NOT ADDRESSED in rows 8 and 14b. | Rows 2, 4 and 14a restated route-free and platform-free: the inference is only that "Algo trading" covers software placing orders without a per-order human action; platform and route are pointed to rows 3, 8, 14b. |
| 4.2 | MINOR | "Read as a whole" quoted the addendum's single label for "this specific automation pattern", near to grading F4 through another document; that label is not one of the four. | Citation removed. |
| 4.3 | MINOR | Row 13 did not deal with "on all plans". | Quoted and addressed; label unchanged. |
| 4.4 | MINOR | "R2 bullet 3" / "bullet 5" miscounted the four marked bullets. | Now bullet 2 / bullet 4. |

Worker 4 found every quoted string in its scope byte-present at its cited line, and its own search did not find a complete outgoing text. No third adversarial pass was run on these last fixes.

## Open questions for the auditor (questions only, no grade of F4)

1. F4 reads "this specific automation pattern". No outgoing message on disk describes any pattern, and every visible fragment predates D-2026-11-10-B. Can a reply be read as answering a pattern that was never put to MFFU in writing?
2. Reply 2 names only the Tradovate API route. Does its platform-free bullet ("Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.") stand alone, or sit under the Tradovate sentence? The F4 report addendum §C left this to Amear (S8); is that ruling on disk anywhere?
3. Rows 2, 4 and 14a are COVERED-BY-INFERENCE through the same step (that "Algo trading" covers software that places orders with no per-order human action), with platform and route left NOT ADDRESSED. Is that one inference, or several, and does F4 allow the automation part and the platform/route part to be read apart?
4. Reply 1 is a relay only (no agent read the source); reply 2 is a screenshot only (no date, no headers, templated-text markers). Which of them, if either, counts as "written confirmation from MFFU" for F4's purpose?
5. Is the trader's MFFU account Tradovate- or Rithmic-routed? Nothing on disk found by this unit says.
6. Was the 2026-10-28 follow-up "naming NinjaTrader 8 + Rithmic" ever sent? DECISIONS.md :539 and voice-session-notes-3 :44 leave it open.
7. The strategy filter audit row A15 calls F4 "closed". Does anything downstream rest on that row?
8. MFFU's conditions (no HFT; no automated tools that exploit favourable sim fills; CME guidelines on live accounts) are recorded, not assessed. The sim-fill condition couples to F3. Should the auditor treat that as part of F4 or as a separate check?
9. The published page's Section 4 says each trader must maintain "their own individual trading activity. Meaning, entering, exiting and cancelling their own trade executions." Its heading is about device sharing and copy-trading. Does it bear on automated order submission, and has MFFU said so anywhere on disk?

## Verification evidence (command output)

All blocks below were piped through a redaction filter (addresses to [address], support names to [rep name], the thread id to [thread-id]; transcript name lines to [trader]). Blocks so marked are therefore de-identified, not byte-exact, at those tokens only.

### V0. Baseline
```text
$ date -u; git rev-parse --short HEAD; git diff --cached --name-only | sed "s/-[a-z]*-reply/-[name]-reply/"
2026-11-10T17:02:44Z
d30ab4d
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
```

### V1. Rubric F4 and rubric section headers (HEAD)
```text
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n 48,57p
### F4 — MFFU automation compliance
**Criterion.** Written confirmation from MFFU that this specific automation
pattern is permitted on a funded account.
**Why frozen.** Flagged as blocking in the Round 1+2 compilation, still open in
the Phase 2 closure document, still open in the Phase 3 output summary, absent
from the session-28 build report. The plan documents also contradict each
other: the Round 3 handoff asserts automation is explicitly permitted; Phase 2
closure states it has not been confirmed by direct inquiry.
**Owner.** Amear. Not a build task — an email.
**Blocks.** Block 4. Block 5.
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n "124,125p;129p"
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
```

### V2 and V7. Reply 2 transcript lines and term counts (HEAD, de-identified)
```text
$ git show HEAD:<transcript> | awk fence > fence.txt; wc -l; sed -n (fence) lines
      25
$ git show HEAD:<transcript> | sed -n "16p;21,33p;36p;64,65p" | (de-identified)
     1	Hi [rep name] — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f
     2	Hello [trader],i hope this mail meets you well.
     3	
     4	Thank you for contacting MyFundedFutures Support! I'll be happy to assist you today.
     5	
     6	Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is [rep name] and I am here to help you with any support you may need today.
     7	
     8	You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
     9	• Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
    10	• Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
    11	• High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
    12	• For live accounts, automated trading must comply with CME guidelines.
    13	
    14	You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
    15	[rep name]-MyFundedFutures Support
    16	- The date and time of either message. No timestamp appears in the screenshot.
    17	- The full headers: From/Reply-To/To/Cc/Bcc, Subject, Message-ID, and the authentication results (SPF/DKIM/DMARC). The domain `myfundedfutures.intercom-mail.com` is only the display text in angle brackets. It has not been checked as a sending domain.
$ git show HEAD:<transcript> | grep -n "No timestamp\|not been checked as a sending domain"
64:- The date and time of either message. No timestamp appears in the screenshot.
65:- The full headers: From/Reply-To/To/Cc/Bcc, Subject, Message-ID, and the authentication results (SPF/DKIM/DMARC). The domain `myfundedfutures.intercom-mail.com` is only the display text in angle brackets. It has not been checked as a sending domain.
$ for p in ...; grep -ci on fence; positive control on topology spec at HEAD
NinjaTrader  fence=0  topology=0
NT8          fence=0  topology=19
Ninja        fence=0  topology=7
Rithmic      fence=0  topology=2
webhook      fence=0  topology=12
n8n          fence=0  topology=27
TradingView  fence=0  topology=5
file         fence=0  topology=23
Tradovate    fence=2  topology=0
API          fence=2  topology=0
strategy     fence=1  topology=17
bot          fence=1  topology=4
automat      fence=5  topology=1
algo         fence=1  topology=0
human        fence=0  topology=1
click        fence=0  topology=0
$ grep -nio "file\|bot\|strategy\|automat[a-z]*\|algo" fence.txt
13:automated
14:Automated
14:bot
14:automated
14:strategy
15:Algo
16:automated
17:automated
19:automated
```

### V3. Reply 1 as relayed in the 2026-08-07 F4 report (HEAD, de-identified)
```text
$ positive controls for the two zero/zero patterns
NinjaTrader CLAUDE.md@HEAD=2
click DECISION_LOG.md@HEAD=17
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n "12,16p;26,27p;31,35p;44,46p;141,145p" (de-identified)
**UNVERIFIED — relayed, not independently confirmed.** Neither the master nor
this manager has read the underlying Gmail thread. Every assertion in sections
1, 2 and 3 below traces to text Amear pasted in-session and to nothing else. No
agent in this chain has opened `[thread-id]`, contacted MFFU, or seen a
message header. The artifact that *is* verified is this file's existence and
Quoted verbatim as relayed. **UNVERIFIED — relayed, not independently confirmed.**

| Field | Value | Status |
|---|---|---|
| Thread ID | `[thread-id]` | UNVERIFIED — relayed |
| Sender | `[address]` | UNVERIFIED — relayed |
| Timestamp | 2026-07-26T21:20:22Z | UNVERIFIED — relayed |
1. **No high-frequency trading.**
2. **Automated tools may not be built to exploit sim-environment fill favorability.**
3. **Live automation must follow CME guidelines.**
- Not claimed: that the PRAXIS pattern specifically was described to MFFU and
  approved as described. The relayed quote is a **general** permission for "algo
  trading," not an assessment of this system's architecture. F4's criterion reads
  "*this specific* automation pattern" — the relayed evidence is broader and
  vaguer than the criterion's wording. Whether the general permission satisfies
$ git diff --quiet HEAD -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md; echo rc
rc=0 (0 = working copy equals HEAD)
     779
28:> "Algo trading is now permitted at MFFU moving forward on all plans including
29:> the evaluation, simulated-funded and live account stages."
34:| Sender | `[address]` | UNVERIFIED — relayed |
35:| Timestamp | 2026-07-26T21:20:22Z | UNVERIFIED — relayed |
36:| Respondent | [rep name], human support rep | UNVERIFIED — relayed |
37:| Policy article | `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices` | UNVERIFIED — relayed; URL not fetched |
44:1. **No high-frequency trading.**
45:2. **Automated tools may not be built to exploit sim-environment fill favorability.**
46:3. **Live automation must follow CME guidelines.**
636:| §3.2 effective date | **DOES NOT ADDRESS** | No date or effective date appears anywhere in the visible text of the reply. As a plain textual fact, [rep name]'s line "Algo trading is permitted on
724:favorability; live automation must follow CME guidelines). No comparison of
```

### V4. Authorising and ruling rows (HEAD DECISION_LOG.md, de-identified, cut)
```text
$ git show HEAD:DECISION_LOG.md | sed -n "177p;435p" | cut -c1-520; git show HEAD:DECISION_LOG.md | sed -n 179p | cut -c1-345
- [2026-08-07T16:13:58Z] **WHO: amear** | PROPOSED BY: — (Amear-originated) | APPROVED BY: Amear, 2026-08-07, in-session | WHAT: **F4 — Amear supplied the unblocking artifact. MFFU confirmed in writing, by a human rep, that algo trading is permitted on all plans including live.** praxis-manager dispatched to land the evidence on disk. **F4 DOES NOT UNFREEZE ON THIS ROW** — it unfreezes when the artifact is committed and the auditor has graded it | WHY: F4's criterion is *"Written confirmation from MFFU that this sp
- [2026-10-28T20:54:29Z] WHO: amear | WHAT: **F4 evidence: FILE the MFFU "[rep name]" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.** Source: Amear's screenshot `~/Desktop/Screenshot 2026-10-28 at 4.53.23<U+202F>PM.png` (254350 bytes, sha256 `15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992`, VERIFIED by the master). Master's reading of the image (to be re-done independently by the worker and auditor): the reply confirms automated trading via the **Tradovate API** on MFFU Tra
- [2026-08-07T18:37:25Z] **WHO: amear** | PROPOSED BY: praxis-master (two questions put) | APPROVED BY: Amear, 2026-08-07, in-session | WHAT: **TWO RULINGS. (1) MFFU's general permission does NOT satisfy F4 — F4 STAYS FROZEN and a follow-up email naming the specific automation pattern is authorised. (2) The F4 evidence unit's second audit shot
$ git show HEAD:DECISION_LOG.md | sed -n 435p | grep -o "The greeting names.\{0,90\}"
The greeting names "[rep name]" but it is signed "[rep name]" (boilerplate indicator). The date, full headers and thr
```

### V5. D-2026-11-10-B (HEAD DECISIONS.md :2054, :2056, cut)
```text
$ git show HEAD:DECISIONS.md | sed -n "2054p;2056p" | cut -c1-430
**The working design: option 1** (:37–41, :74, :78). A new NT8 signal-emitter strategy (working name `PraxisNoiseAreaEmitter`, not built, :39) runs the Noise-Area band logic on bar close, calls no order method, and posts each decision to the existing local n8n webhook `praxis-signal` (:39). The breaker gates run in n8n with Redis, default closed, before Write Signal File (:41, :45). `PraxisSignalConsumer.cs` stays the only com
**Fallback: option 3, only if OPEN-T1 fails.** Option 3 (the NT8 strategy computes the signal and gates itself, in NinjaScript, before its own order calls, :76) is the fallback only if OPEN-T1 finds the VM cannot reach the n8n webhook (:78, :98). It is not adopted by this entry.
```

### V6. Topology spec and CLAUDE.md signal flow (HEAD)
```text
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n "39p;41p;76p"
The live trading signal is emitted by **a new NT8 signal-emitter strategy** (working name `PraxisNoiseAreaEmitter`, not built). It runs the same Noise-Area band logic as `PraxisNoiseAreaBreakout.cs`, on bar close, but it never calls `EnterLong`, `EnterShort`, `ExitLong`, `ExitShort` or any order method. Instead it sends each decision (entry, exit, reverse, session flat) as an HTTP POST to the existing local n8n webhook `praxis-signal`. n8n runs the breaker gates and only then writes the signal file. `PraxisSignalConsumer.cs` stays the **only** component that submits orders.
Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.
| 3 (fallback) | NT8 strategy computes the signal and gates itself | In NinjaScript, before its own `EnterLong` / `EnterShort` | gate code in the strategy; account-state read (available in NT8); trip log; heartbeat source; fallback script | No: there is no n8n gate and no Redis; the Block 1 pipe is unused |
$ git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n "1.5 | TradingView\|1.12 | Order submission" | cut -c1-200
21:| 1.5 | TradingView as the emitter | The anchor strategy is "NOT TradingView-exportable"; "no Pine source anywhere in repo" (DECISION_LOG 2026-07-15T21:10Z). `git ls-files` shows no Pine file. | No
28:| 1.12 | Order submission | `SubmitBracket` in `PraxisSignalConsumer.cs`: `SetStopLoss` / `SetProfitTarget`, then `EnterLong(sig.Qty, …)` / `EnterShort(sig.Qty, …)` (:660, :662). This is the only p
$ git show HEAD:CLAUDE.md | grep -n "Signal flow\|Automated trading infrastructure"
4:- Automated trading infrastructure: TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU
21:Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
```

### V8. MFFU published page, R6 branch capture (not main)
```text
$ git rev-parse --short r6/announcement-research; git show r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt | grep -n "8444599\|FETCHED_UTC: Mon Nov  9 09:06:24\|^HTTP\|Automated Trading Protocols\|High-frequency Trading is not\|Traders may make use of automated\|Traders trading live accounts"
bf6fcc7
3:HTTP: 200
64:URL: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
65:FETCHED_UTC: Mon Nov  9 09:06:24 UTC 2026
66:HTTP: 200
76:Section 1: Automated Trading Protocols
77:High-frequency Trading is not allowed on our plans.
79:Traders may make use of automated trading strategies tailored to their own specific settings so long as these automated tools do not aim to exploit the favorable fills offered in the Simulated Environment.
80:Traders trading live accounts with automated trading must abide by CME guidelines.
```

### V8b. Further lines of the same page capture (R6 branch)
```text
$ git show r6/announcement-research:docs/reports/evidence/2026-11-09-r6-mffu-news.txt | grep -n -F -e 'Each individual trader is required to maintain' -e 'Slippage and Bracket Usage' -e 'Tier 1 Economic Data Trading' -e 'prohibits hedging of any kind' -e 'Section 4: Device Sharing' -e 'Order Placement: Simultaneously' -e 'Gapped or Illiquid' -e 'Collaborative Trading'
85:● Order Placement: Simultaneously placing multiple limit orders at the same price to manipulate order fills is prohibited.
86:● Gapped or Illiquid Market Trading: Profiting from isolated, stale or unrealistic fills in low-liquidity contracts (including back-month contracts) or during low-volume hours is not allowed, regardless of how long the position is held.
87:● Slippage and Bracket Usage: Exploiting the absence of slippage and utilizing tight brackets to gain from favorable fills are not permitted.
88:● Tier 1 Economic Data Trading: Engaging in trades during tier 1 economic data releases is restricted.
90:● Collaborative Trading: Collaborating with others to execute identical or opposite strategies across unconnected accounts is prohibited.
98:​Section 4: Device Sharing & Copy-Trading other Traders
100:Each individual trader is required to maintain their own individual trading activity. Meaning, entering, exiting and cancelling their own trade executions. Traders are not permitted to copy trade one another by entering, exiting or cancelling trade positions.
106:MyFunded Futures prohibits hedging of any kind. Hedging is defined as a trader entering both buy and sell positions on the same underlying asset, at the same time.
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n 634p | cut -c1-100
| F4 "this specific automation pattern" (and §3.5, specific vs general) | **DOES NOT ADDRESS** | The
```

### V9 and V10. Outgoing-inquiry records, F4-closed claim, rubric headers (HEAD; manager re-run of worker 2; trader name replaced)
```text
$ git grep -n -w A15 HEAD -- docs/reports/2026-11-08-strategy-filter-audit.md
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:68:| A15 | Low frequency to reduce prop-firm detection risk | D3 §1 and §6 Scenario B | Was A at the time. **Now void:** MFFU permits automation in writing (F4 closed; repo F4 evidence). |
$ git show HEAD:DECISION_LOG.md | sed -n 801p | LC_ALL=C grep -o 'F4 is called "closed".\{0,140\}'
F4 is called "closed" in the strategy filter audit's row A15 while the rubric holds F4 FROZEN (recorded; the rubric governs). **Decided by master under D1:** ind
$ git show HEAD:docs/reports/2026-11-10-f1-f2-proposal-manager.md | sed -n 36p
Observation not acted on: the strategy filter audit row A15 (audit :68) calls F4 "closed"; the rubric still lists F4 under FROZEN (`specs/SPEC_RUBRIC.md`:61, [E28]). Outside this unit; flagged for the master.
$ git show HEAD:HANDOFF.md | sed -n "764p;784p" | cut -c1-700
**1 MFFU email** — sent; MFFU permits algo trading, but [trader] ruled it too general for F4. Follow-up sent 2026-08-07, awaiting reply. **F4 still FROZEN.** · **2 Stop supervision** — RULED, done. · **3 Compact the ledgers** — OPEN; caused today's auditor null. · **4 `CLAUDE.md:51`** — OPEN; hit live when the write-guard blocked master memory. · **5 Commit path** — OPEN; the binding constraint. · **6 Phase 3 spec** — advanced, spec still not on `main`.
1. **F4 — [trader] ran the outreach. Six of eight firms replied; MFFU confirmed algo trading permitted (human rep, written).** Evidence landed and staged. **[trader] then ruled that the general permission does NOT satisfy F4's *"this **specific** automation pattern"* — so F4 STAYS FROZEN.** A follow-up email naming the actual architecture, and asking the policy's effective date, was **sent 2026-08-07** and is awaiting reply. Auditor returned `Result: FAIL` on **C2** (staged `ISSUE_REGISTER.md:70` asserts all eight firms' results as fact with zero relay qualifiers, control 4 on line 68) and **C3** (a claimed MANIFEST deletion with no output behind it; a stale positive control reading `317` where th
$ git show HEAD:ISSUE_REGISTER.md | sed -n 70p | grep -o "WHY: the outreach.\{0,120\}\|WHEN: outreach.\{0,60\}\|an English inquiry"
WHY: the outreach was run to establish whether the PRAXIS automation pattern is permitted per-firm. Six of eight replied, but only FIVE r
an English inquiry
WHEN: outreach sent 2026-07-26 window; recorded 2026-08-07, session 43 | H
$ git show HEAD:DECISIONS.md | sed -n 539p
9. F4: the 2026-10-28 MFFU reply names the Tradovate API, not NinjaTrader/Rithmic. Does [trader] send the follow-up himself (notes-3 line 44)?
$ git show HEAD:docs/reports/2026-11-01-voice-session-notes-3.md | sed -n 44p
- F4: the 2026-10-28 MFFU reply names the Tradovate API, not NinjaTrader/Rithmic. Whether [trader] sends the follow-up himself is unconfirmed.
$ git show HEAD:DECISION_LOG.md | sed -n 46p | grep -o ".\{0,60\}MFFU inquiry email.\{0,80\}"
tion (NOT build-agent tasks): praxispush provisioning + the MFFU inquiry email are the TRADER'S actions to execute, not the build agent's to decide. | STATE: 
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n "^## \|^### F4"
17:## FROZEN — nothing downstream may proceed until these clear
48:### F4 — MFFU automation compliance
61:## PASSED — closed criteria
96:## OPEN — gradeable now
120:## Standing criteria — graded on every dispatch
253:## Process rulings — binding on the orchestrator
431:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
```


### V11. Final checks on the finished reports

Run after the last edit to every report. The counts for this report were taken just before this block was inserted; the block adds no name, banned word or S13 sentence (re-checked after insertion by the manager). The first four byte-presence lines are from an earlier run, against HEAD blobs that have not changed. The pattern file holds the three support names, the trader surname and the thread id; only counts are shown.

```text
$ for f in manager worker1..worker4: hits per line of the pattern file (3 support names, trader surname, thread id), email regex, banned words bw1..bw3 (the three the brief names), count of the S13 sentence, and whether the last line is the S13 sentence
manager: pat1=0 pat2=0 pat3=0 pat4=0 pat5=0 email=0 bw1=0 bw2=0 bw3=0 S13count=1 lastIsS13=yes
worker1: pat1=0 pat2=0 pat3=0 pat4=0 pat5=0 email=0 bw1=0 bw2=0 bw3=0 S13count=1 lastIsS13=yes
worker2: pat1=0 pat2=0 pat3=0 pat4=0 pat5=0 email=0 bw1=0 bw2=0 bw3=0 S13count=1 lastIsS13=yes
worker3: pat1=0 pat2=0 pat3=0 pat4=0 pat5=0 email=0 bw1=0 bw2=0 bw3=0 S13count=1 lastIsS13=yes
worker4: pat1=0 pat2=0 pat3=0 pat4=0 pat5=0 email=0 bw1=0 bw2=0 bw3=0 S13count=1 lastIsS13=yes
$ grep -c -E "F4 (passes|is closed|is satisfied)|satisfies F4" manager report
0
$ byte-presence of quotes changed after the adversaries (grep -cF on HEAD blobs)
R1 full string, F4 report: 1
DL:179 ruling string: 1
DL:435 tail after name token: 1
A15 row: 1
R2 accounts phrase, transcript: 1
R1 "moving forward": 2
"on all plans" in R1 (F4 report) / R2 (transcript): 1 / 1
$ git diff --cached --name-only (name masked); git status --porcelain for this unit; HEAD
docs/reports/evidence/2026-10-28-mffu-[name]-reply.png
?? docs/reports/2026-11-10-f4-grading-manager.md
?? docs/reports/2026-11-10-f4-grading-worker1.md
?? docs/reports/2026-11-10-f4-grading-worker2.md
?? docs/reports/2026-11-10-f4-grading-worker3.md
?? docs/reports/2026-11-10-f4-grading-worker4.md
d30ab4d
2026-11-10T17:24:06Z
```

## S6 cross-block check

This unit approves no deviation and changes no spec. The conditions MFFU attached touch other blocks: the sim-fill condition couples to F3 (F4 report §4 already records this) and the CME condition to Blocks 4 and 5. They are recorded, not assessed.

## Files staged

None by this unit. Reports left untracked for the master.

Result: PASS

This result is about whether this unit produced the comparison the brief asked for. It is not a result for F4, which this report does not grade and which stays FROZEN.

## Correction 1 (2026-11-10, after audit fail 1)

This section changes evidence form only. No element-table label, no coverage reading and no row text above is changed, and F4 is not graded here; it stays FROZEN. The section re-runs, with the literal command lines shown, the blocks the first audit found described rather than pasted (audit findings 1, 2 and 3), corrects one worker figure this report cites, and narrows the de-identification sentence at :8 (audit finding 7). Line numbers such as ":40" refer to lines 1 to 459 of this file, which are unchanged; this section was inserted after them, before the last line.

**How these blocks were made.** Each block is the output of `bash /tmp/f4c1/run.sh <command file>`. That script starts in the repo root, prints each command line with a `$ ` prefix, then runs exactly that line with `eval` in one bash shell, so a variable set on one line (for example `T`, the transcript path) is still set on the next. The script text, the pattern files and the redaction filter are pasted in block C1-V0 of `docs/reports/2026-11-10-f4-grading-correction-1-manager.md`. No personal name is typed in any command line. The trader's surname (pattern line 1), the three support representatives' names (lines 2 to 4) and the mail-thread id (line 5) are held in `/tmp/f4c1-pat.txt`, which was built from the HEAD transcript and DECISION_LOG.md :177 by commands that print counts only. Where output would carry one of them, the command line shows the pipe through `perl -p /tmp/f4c1/redact.pl`, which writes `[address]` for an email address and `[patN]` for pattern line N. A path that carries a representative's first name is put into a variable by `git ls-tree | grep` and is printed only through `sed 's/-[a-z]*-reply/-[name]-reply/'`, which the command line shows. Apart from those two filters, the output is unedited. All runs: 2026-11-10, HEAD `d30ab4d`, by the manager.

### C1-V2. Re-run of V2 (audit finding 1: the V2 line that describes the fence extraction instead of showing it)

~~~text
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); echo "$T" | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md
$ git show "HEAD:$T" | grep -n '^```'
14:```text
40:```
$ git show "HEAD:$T" | awk '/^```text$/{f=1;next} f&&/^```$/{exit} f' > /tmp/f4c1/fence.txt; wc -l < /tmp/f4c1/fence.txt
      25
$ git show "HEAD:$T" | sed -n '15,39p' | cmp - /tmp/f4c1/fence.txt && echo "fence = file lines 15-39"
fence = file lines 15-39
$ git show "HEAD:$T" | grep -n '' | sed -n '16p;21,33p;36p;64,65p' | perl -p /tmp/f4c1/redact.pl
16:Hi [pat2] — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f
21:Hello amear,i hope this mail meets you well.
22:
23:Thank you for contacting MyFundedFutures Support! I'll be happy to assist you today.
24:
25:Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is [pat3] and I am here to help you with any support you may need today.
26:
27:You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
28:• Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
29:• Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
30:• High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
31:• For live accounts, automated trading must comply with CME guidelines.
32:
33:You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
36:[pat4]-MyFundedFutures Support
64:- The date and time of either message. No timestamp appears in the screenshot.
65:- The full headers: From/Reply-To/To/Cc/Bcc, Subject, Message-ID, and the authentication results (SPF/DKIM/DMARC). The domain `myfundedfutures.intercom-mail.com` is only the display text in angle brackets. It has not been checked as a sending domain.
$ git show "HEAD:$T" | grep -n "No timestamp\|not been checked as a sending domain" | cut -c1-60
64:- The date and time of either message. No timestamp appea
65:- The full headers: From/Reply-To/To/Cc/Bcc, Subject, Mes
~~~

Reading. The fence opens at file :14 and closes at :40, holds 25 lines, and equals file lines 15 to 39 byte for byte (`cmp` is silent and the `echo` ran). File :16 is fence line 2. The text lines match the V2 block above. The two other V2 lines that name the transcript only by a placeholder (:232 and :250) are the fifth and sixth commands here, with the path held in `$T`. One difference: V2 printed transcript line 21 with `[trader]`; at HEAD that line carries the trader's first name in lower case, shown here unmasked.

### C1-V7. Re-run of V7 (audit finding 1: the V7 line that describes the term-count loop and its positive control)

~~~text
$ for p in NinjaTrader NT8 Ninja Rithmic webhook n8n TradingView file Tradovate API strategy bot automat algo human click; do printf '%-12s fence=%s topology=%s\n' "$p" "$(grep -ci -- "$p" /tmp/f4c1/fence.txt)" "$(git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -ci -- "$p")"; done
NinjaTrader  fence=0 topology=0
NT8          fence=0 topology=19
Ninja        fence=0 topology=7
Rithmic      fence=0 topology=2
webhook      fence=0 topology=12
n8n          fence=0 topology=27
TradingView  fence=0 topology=5
file         fence=0 topology=23
Tradovate    fence=2 topology=0
API          fence=2 topology=0
strategy     fence=1 topology=17
bot          fence=1 topology=4
automat      fence=5 topology=1
algo         fence=1 topology=0
human        fence=0 topology=1
click        fence=0 topology=0
$ grep -nio 'file\|bot\|strategy\|automat[a-z]*\|algo' /tmp/f4c1/fence.txt
13:automated
14:Automated
14:bot
14:automated
14:strategy
15:Algo
16:automated
17:automated
19:automated
$ git show HEAD:CLAUDE.md | grep -ci NinjaTrader; git show HEAD:DECISION_LOG.md | grep -ci click
2
17
~~~

Reading. Every count equals the V7 table above. NinjaTrader and click are zero in both columns, so the last command is their positive control with the same `grep -ci`: 2 lines in CLAUDE.md and 17 in DECISION_LOG.md at HEAD. A zero above is therefore a real absence, not a pattern that cannot match. (The positive-control line V3 shows as "$ positive controls for the two zero/zero patterns" is this last command.)

### C1-V3. Re-run of V3 (audit findings 1 and 2)

~~~text
$ git diff --quiet HEAD -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md; echo "rc=$?"
rc=0
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | wc -l
     779
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n '' | sed -n '12,16p;25,29p;31,37p;44,46p' | perl -p /tmp/f4c1/redact.pl
12:**UNVERIFIED — relayed, not independently confirmed.** Neither the master nor
13:this manager has read the underlying Gmail thread. Every assertion in sections
14:1, 2 and 3 below traces to text Amear pasted in-session and to nothing else. No
15:agent in this chain has opened `[pat5]`, contacted MFFU, or seen a
16:message header. The artifact that *is* verified is this file's existence and
25:
26:Quoted verbatim as relayed. **UNVERIFIED — relayed, not independently confirmed.**
27:
28:> "Algo trading is now permitted at MFFU moving forward on all plans including
29:> the evaluation, simulated-funded and live account stages."
31:| Field | Value | Status |
32:|---|---|---|
33:| Thread ID | `[pat5]` | UNVERIFIED — relayed |
34:| Sender | `[address]` | UNVERIFIED — relayed |
35:| Timestamp | 2026-07-26T21:20:22Z | UNVERIFIED — relayed |
36:| Respondent | [pat2], human support rep | UNVERIFIED — relayed |
37:| Policy article | `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices` | UNVERIFIED — relayed; URL not fetched |
44:1. **No high-frequency trading.**
45:2. **Automated tools may not be built to exploit sim-environment fill favorability.**
46:3. **Live automation must follow CME guidelines.**
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -e 'Algo trading is now permitted' -e 'simulated-funded and live account stages' -e '^| Sender |' -e '^| Timestamp |' -e '^| Respondent |' -e '^| Policy article |' -e 'No high-frequency trading' -e 'exploit sim-environment fill' -e 'live automation must follow CME' -i | cut -c1-160 | perl -p /tmp/f4c1/redact.pl
28:> "Algo trading is now permitted at MFFU moving forward on all plans including
29:> the evaluation, simulated-funded and live account stages."
34:| Sender | `[address]` | UNVERIFIED — relayed |
35:| Timestamp | 2026-07-26T21:20:22Z | UNVERIFIED — relayed |
36:| Respondent | [pat2], human support rep | UNVERIFIED — relayed |
37:| Policy article | `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices` | UNVERIFIED — relayed; URL not fetched 
44:1. **No high-frequency trading.**
45:2. **Automated tools may not be built to exploit sim-environment fill favorability.**
46:3. **Live automation must follow CME guidelines.**
636:| §3.2 effective date | **DOES NOT ADDRESS** | No date or effective date appears anywhere in the visible text of the reply. As a plain textual fact, [pat4]'s 
716:So the reply states four conditions: no high-frequency trading; automated tools
724:favorability; live automation must follow CME guidelines). No comparison of
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n '' | sed -n '141,145p'
141:- Not claimed: that the PRAXIS pattern specifically was described to MFFU and
142:  approved as described. The relayed quote is a **general** permission for "algo
143:  trading," not an assessment of this system's architecture. F4's criterion reads
144:  "*this specific* automation pattern" — the relayed evidence is broader and
145:  vaguer than the criterion's wording. Whether the general permission satisfies
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -n '28,29p' | grep -ci -e NinjaTrader -e NT8 -e Rithmic -e Tradovate -e platform
0
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -ci -e NinjaTrader -e Rithmic -e Tradovate
29
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -e 'Algo trading is now permitted' -e 'simulated-funded and live account stages' -e '^| Sender |' -e '^| Timestamp |' -e '^| Respondent |' -e '^| Policy article |' -e 'No high-frequency trading' -e 'exploit sim-environment fill' -e 'Live automation must follow CME' -e 'live automation must follow CME guidelines). No comparison' | cut -d: -f1 | tr '\n' ' '; echo
28 29 34 35 36 37 44 45 46 636 724 
~~~

Reading. `rc=0`: the working copy of the 2026-08-07 F4 report equals HEAD. The HEAD blob has 779 lines. The `grep -n` command is the command for the `N:` lines that V3 shows without one. It gives 28, 29, 34, 35, 36, 37, 44, 45, 46, 636, 716 and 724. These include all eleven of V3's, plus 716. The `-i` is needed for line 46, which has "Live" with a capital L, and it also brings in 716. Without `-i`, both 46 and 716 drop out. The last command is case-sensitive, with one pattern per case, and prints exactly V3's eleven line numbers: 28, 29, 34, 35, 36, 37, 44, 45, 46, 636 and 724. The sed range line numbers match the V3 text (line 26 is "Quoted verbatim as relayed", line 27 is blank). The sixth and seventh commands back row 3's "R1 as relayed names no platform": R1, at lines 28 and 29, has 0 lines naming NinjaTrader, NT8, Rithmic, Tradovate or a platform, while the same blob has 29 lines that name NinjaTrader, Rithmic or Tradovate (positive control).

### C1-V40. Search behind the :40 sentence (audit finding 3)

~~~text
$ for s in "Two follow-ups" "Does this specific" "Dear MFFU" "Hi MFFU" "Hello MFFU" "To: support" "I am building" "Subject:" "draft email" "email draft" "follow-up draft" "draft of the follow-up"; do printf '%-24s files=%s lines=%s\n' "$s" "$(git grep -l -i -F -e "$s" HEAD | wc -l | tr -d ' ')" "$(git grep -n -i -F -e "$s" HEAD | wc -l | tr -d ' ')"; done
Two follow-ups           files=2 lines=2
Does this specific       files=2 lines=2
Dear MFFU                files=0 lines=0
Hi MFFU                  files=0 lines=0
Hello MFFU               files=0 lines=0
To: support              files=0 lines=0
I am building            files=0 lines=0
Subject:                 files=4 lines=4
draft email              files=0 lines=0
email draft              files=1 lines=1
follow-up draft          files=0 lines=0
draft of the follow-up   files=0 lines=0
$ git grep -n -i -F -e "Two follow-ups" -e "Does this specific" HEAD | cut -c1-150 | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:642:> Hi [pat2] — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'
HEAD:docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md:16:Hi [pat2] — thanks for confirming, that's helpful. Two follow-ups so I can be su
$ git grep -n -i -F -e "Subject:" -e "email draft" HEAD | cut -c1-150 | sed 's/-[a-z]*-reply/-[name]-reply/' | perl -p /tmp/f4c1/redact.pl
HEAD:docs/reports/2026-07-26-session34-p0-flush-audit.md:6:**Proposed subject:** chore(flush): AUDIT_LOG row Praxis_build-o3d + session-34 ledger appe
HEAD:docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md:480:ALL tool_use records whose tool_input.command contains the park subject:
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:582:contact MFFU. On the manager's attestation, this filing unit's manager and workers did
HEAD:docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:643:/Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi: Compo
HEAD:docs/reports/2026-11-06-status-handoff-evening-manager.md:18:- R-1104-2 (housekeeping is Code's): D-2026-11-04-A, filed at `87d506f` (commit subj
$ git grep -l -i -F myfundedfutures HEAD | sed 's/-[a-z]*-reply/-[name]-reply/'
HEAD:DECISION_LOG.md
HEAD:ISSUE_REGISTER.md
HEAD:docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md
HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
HEAD:docs/reports/2026-11-05-mffu-fee-check.md
HEAD:docs/reports/2026-11-10-d9-housekeeping-manager.md
HEAD:docs/reports/2026-11-10-f1-f2-proposal-manager.md
HEAD:docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md
HEAD:docs/specs/2026-11-05-walk-forward-spec.md
$ git grep -l -i -F myfundedfutures HEAD | grep -v -c -e '-reply' -e 'f4-mffu-compliance-evidence'
7
$ git grep -c -i -F myfundedfutures HEAD | grep -v -e '-reply' -e 'f4-mffu-compliance-evidence'
HEAD:DECISION_LOG.md:1
HEAD:ISSUE_REGISTER.md:1
HEAD:docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:1
HEAD:docs/reports/2026-11-05-mffu-fee-check.md:22
HEAD:docs/reports/2026-11-10-d9-housekeeping-manager.md:8
HEAD:docs/reports/2026-11-10-f1-f2-proposal-manager.md:1
HEAD:docs/specs/2026-11-05-walk-forward-spec.md:17
$ git grep -l -i -F -e "thanks for confirming" HEAD | wc -l; git grep -l -i -F -e "Algo trading is now permitted" HEAD | wc -l; git grep -l -i -F -e "Hello amear" HEAD | wc -l
       2
       1
       2
$ grep -rlI -i -F "Two follow-ups" --exclude-dir=.git . | sed 's/-[a-z]*-reply/-[name]-reply/' | sort
./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
./docs/reports/2026-10-28-f4-[name]-reply-adversarial-transcript.md
./docs/reports/2026-10-28-f4-[name]-reply-worker3.md
./docs/reports/2026-10-28-f4-[name]-reply-worker5-fix.md
./docs/reports/2026-11-10-f4-grading-correction-1-worker1.md
./docs/reports/2026-11-10-f4-grading-correction-1-worker2.md
./docs/reports/2026-11-10-f4-grading-manager.md
./docs/reports/2026-11-10-f4-grading-worker2.md
./docs/reports/2026-11-10-f4-grading-worker3.md
./docs/reports/2026-11-10-f4-grading-worker4.md
./docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md
$ git grep -l -i -F myfundedfutures HEAD | grep -v -e '-reply' -e 'f4-mffu-compliance-evidence' | sed 's/^HEAD://' | while read -r f; do printf '%s outgoing-phrase-lines=%s\n' "$f" "$(git show "HEAD:$f" | grep -c -i -F -e 'Two follow-ups' -e 'Dear MFFU' -e 'Hi MFFU' -e 'Hello MFFU' -e 'To: support' -e 'I am building' -e 'Does this specific')"; done
DECISION_LOG.md outgoing-phrase-lines=0
ISSUE_REGISTER.md outgoing-phrase-lines=0
docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md outgoing-phrase-lines=0
docs/reports/2026-11-05-mffu-fee-check.md outgoing-phrase-lines=0
docs/reports/2026-11-10-d9-housekeeping-manager.md outgoing-phrase-lines=0
docs/reports/2026-11-10-f1-f2-proposal-manager.md outgoing-phrase-lines=0
docs/specs/2026-11-05-walk-forward-spec.md outgoing-phrase-lines=0
$ git show HEAD:docs/reports/2026-11-10-d9-housekeeping-manager.md | grep -c -i -w -F -f /tmp/f4c1-pat.txt
48
~~~

Reading. Of the twelve outgoing-message phrases, eight hit no file at HEAD: "Dear MFFU", "Hi MFFU", "Hello MFFU", "To: support", "I am building", "draft email", "follow-up draft" and "draft of the follow-up". "Two follow-ups" and "Does this specific" hit two HEAD lines only: the 2026-08-07 report :642 and the transcript :16. Both are the same truncated preview, which ends "is f" (see worker 4's report, Correction 1, C1-Y1). "Subject:" hits 4 lines and "email draft" 1 line. None of them is a message to MFFU. The :582 line is the 2026-08-07 report saying its unit did not contact MFFU. Nine HEAD files contain "myfundedfutures". The seven outside the reply transcript and the 2026-08-07 report contain no line of the outgoing-phrase set. Positive controls: the same `git grep -l -i -F` method finds "thanks for confirming" in 2 files, "Algo trading is now permitted" in 1 and "Hello amear" in 2. The working-tree search, untracked files included, finds "Two follow-ups" in nine files: the two HEAD blobs above, three untracked reports of the 2026-10-28 filing unit and four reports of this unit. It shows where the phrase occurs, not what else those files hold. The :40 sentence is about HEAD only. So the :40 sentence rests on this block: under these probes, no complete outgoing text to MFFU is on disk at HEAD. The probes are a fixed list of phrases and cannot rule out other wording. The last command counts 48 lines in a HEAD report of another unit that match the pattern file. That report is outside this unit and has not been edited; it is reported to the master in the correction-1 manager report.

### C1-T. The :8 de-identification sentence, narrowed (audit finding 7)

~~~text
$ grep -n '^## Correction 1 (2026-11-10, after audit fail 1)$' docs/reports/2026-11-10-f4-grading-manager.md | cut -d: -f1
460
$ sed -n '1,459p' docs/reports/2026-11-10-f4-grading-manager.md | grep -n -F '[trader]' | cut -d: -f1 | tr '\n' ' '; echo
8 199 234 393 394 400 402 
$ sed -n '1,459p' docs/reports/2026-11-10-f4-grading-manager.md | grep -n -i -w Amear | cut -d: -f1 | tr '\n' ' '; echo
47 55 154 188 220 290 327 328 329 412 
$ git show HEAD:specs/SPEC_RUBRIC.md | grep -n -w Amear | head -3 | cut -c1-80
3:Authority: the scoping agent (Claude.ai) via Amear. Amear decides; agents writ
4:Amear does not edit this file by hand. Every edit cites a logged Amear approva
13:`PASSED@<sha>` (graded and closed) · `WAIVED` (Amear overrode; see DECISION_L
$ git show HEAD:HANDOFF.md | sed -n '764p;784p' | grep -o -w 'Amear' | wc -l
       4
$ git show HEAD:DECISIONS.md | sed -n 539p | grep -o 'Does [A-Za-z]* send'
Does Amear send
$ sed -n '1,459p' docs/reports/2026-11-10-f4-grading-manager.md | grep -n -w amear | cut -d: -f1 | tr '\n' ' '; echo
327 328 329 412 
$ git show HEAD:docs/reports/2026-11-01-voice-session-notes-3.md | sed -n 44p | grep -o 'Whether [A-Za-z]* sends'
Whether Amear sends
~~~

Narrowed reading of :8, replacing its words "the trader's name by `[trader]`". The first command shows this section's heading at line 460, so lines 1 to 459 are the text that was there before this correction. In lines 1 to 459 of this file, `[trader]` stands for the trader's first name only where it was applied. Those places are line 234 (V2, transcript :21) and lines 393, 394, 400 and 402 (V9: HANDOFF.md :764 and :784, DECISIONS.md :539, voice-session-notes-3 :44; the HEAD sources carry the first name there, as the fifth, sixth and eighth commands show). Line 8 is the sentence itself, and line 199 is the note that describes the substitution. Everywhere else, at lines 47, 55, 154, 188, 220, 290, 327, 328, 329 and 412, this report uses the trader's first name, as the rubric itself does ("Amear", rubric :3, :4 and :13 above). At lines 327 to 329 and 412 it is in lower case ("WHO: amear", quoted from the sources; the seventh command). The search is case-insensitive (`-i -w`). The first name is not withheld. What this report withholds everywhere is the trader's surname, the support representatives' names, the mail-thread id and every email address. The per-file counts are in the correction-1 manager report, section "Final checks".

### C1-W. A worker figure cited at :152, corrected

:152 says `git grep -E '\bF4\b'` returns 0 lines and `-w` returns 634. Re-run by the manager (the same commands are in worker 2's report, Correction 1, C1-W7):

~~~text
$ git grep -E '\bF4\b' HEAD | wc -l; git grep -w F4 HEAD | wc -l; git grep -P '\bF4\b' HEAD | wc -l; git grep -i -w F4 HEAD | wc -l
       0
     496
     496
     634
$ sed -n '98,115p' docs/reports/2026-11-10-f4-grading-manager.md | grep -c -e 634 -e 'Block 8'
0
~~~

Reading. `-E '\bF4\b'` returns 0 (agrees), `git grep -w F4 HEAD` returns 496 and `git grep -P '\bF4\b' HEAD` returns 496. 634 is the count for `git grep -i -w F4 HEAD`. The figure 634 at :152 is therefore the case-insensitive count, not the `-w` count. The worker 2 Block 8 references at :150 are re-run in worker 2's Correction 1, C1-W8. No label rests on either figure: the element table, lines 98 to 115, contains neither "634" nor "Block 8" (second command).

### C1-V11. Re-run of V11 (audit finding 1: the three V11 lines that describe the per-file loop, the byte-presence checks and the index check)

Byte-presence and grading-phrase lines:

~~~text
$ T=$(git ls-tree -r --name-only HEAD docs/reports/evidence/ | grep -- '-reply-transcript.md$'); echo "$T" | sed 's/-[a-z]*-reply/-[name]-reply/'
docs/reports/evidence/2026-10-28-mffu-[name]-reply-transcript.md
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -c -F '> "Algo trading is now permitted at MFFU moving forward on all plans including'
1
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -c -F '> the evaluation, simulated-funded and live account stages."'
1
$ git show HEAD:DECISION_LOG.md | grep -c -F "TWO RULINGS. (1) MFFU's general permission does NOT satisfy F4 — F4 STAYS FROZEN and a follow-up email naming the specific automation pattern is authorised."
1
$ git show HEAD:DECISION_LOG.md | grep -c -F '" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.'
1
$ git show HEAD:docs/reports/2026-11-08-strategy-filter-audit.md | grep -c -F '| A15 | Low frequency to reduce prop-firm detection risk | D3 §1 and §6 Scenario B | Was A at the time. **Now void:** MFFU permits automation in writing (F4 closed; repo F4 evidence). |'
1
$ git show "HEAD:$T" | grep -c -F 'your MyFundedFutures Tradovate evaluation and funded accounts'
1
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -c -F 'moving forward'
2
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -c -F 'moving forward on all plans'; git show "HEAD:$T" | grep -c -F 'on all plans'
2
1
$ git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -n -F 'moving forward on all plans' | cut -c1-70; git show HEAD:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -c -F 'on all plans including'
28:> "Algo trading is now permitted at MFFU moving forward on all plan
636:| §3.2 effective date | **DOES NOT ADDRESS** | No date or effectiv
1
$ grep -n -E 'F4 (passes|is closed|is satisfied)|satisfie[s] F4' docs/reports/2026-11-10-f4-grading-manager.md | cut -d: -f1
427
~~~

Reading. Each quoted string changed after the adversaries is byte-present in its HEAD blob (count 1). R1's "moving forward" is on 2 lines (the quote at :28 and the 2026-08-07 report's own :636). V11's line `"on all plans" in R1 (F4 report) / R2 (transcript): 1 / 1` does not record its exact string. With "on all plans including", R1 gives 1, which agrees; with "moving forward on all plans" it gives 2 (:28 and :636); R2 gives 1, which agrees. The grading-phrase search prints line numbers only, so this block adds no matching line. It finds :427, which is V11's own command line and contains the searched words. No sentence of this report matches.

The per-file personal-data, banned-word and S13 checks, and the index state, were run after the last edit to every file of this unit, the correction-1 reports included. They are pasted, with their literal commands, in the correction-1 manager report, section "Final checks". They are not repeated here, because pasting them into this file would be an edit made after the run.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
