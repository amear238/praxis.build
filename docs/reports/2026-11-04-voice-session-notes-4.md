# 2026-11-04 — Voice session notes 4 (Amear, Claude.ai voice; written 2026-11-05)

Written by Claude from the voice session of 2026-11-04 evening (ET), which discussed `docs/reports/2026-11-04-research-compiled-for-voice-v2.md` and its §5 decision list. Record for the next Claude Code session. Not an audited report. Rulings are Amear's, quoted or closely paraphrased; Claude's readings are labelled. Code files each as a `WHO: amear` ledger row and a DECISIONS entry before acting on it.

**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Corrections applied to the v2 summary during the session (both the master's, logged by Code already):** the "a 09:30 start gives 32" sentence in §1 item 8 was dropped (33 missing sessions, 32 if the 2025-01-09 closure counts); the §3 partial-window line reads "none of the vendors with published prices sells a 12-month slice" (Databento, TickData, DataMine unpriced).

## Rulings (R-VN4-1 .. R-VN4-14)

| # | Topic (v2 §5 item) | Amear's words | Ruling as read by Claude |
|---|---|---|---|
| R-VN4-1 | GitHub login, future use (25) | "Only within this directory." | Agents may use his `gh` login only against the Praxis.build repo itself. Never for research reads of other people's repos. Past use (item 24): not ruled on further; no action requested. |
| R-VN4-2 | Breakers as resting stops? (11) | "Until the account is live … resting stops." Asked which: "The latter." | Bar-close checks (market-order flatten) in the backtest; resting stop orders once live. Claude noted the gap: the backtest then does not test live stop fills; paper trading (Block 4) covers it. |
| R-VN4-3 | Walk-forward on minute data (12) | "Yes." | Walk-forward runs on the existing 1-minute data. The spec's High/1-tick requirement is deferred, not deleted. |
| R-VN4-4 | r8j at P0 (27) | "Yes." | **r8j confirmed P0 by Amear.** |
| R-VN4-5 | Data gaps (8) | "As long as the data that I generated came back similar to … what is found online, I'm happy to move on." | 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged. Basis: baseline shape matches the published NQ replication (lower win rate, bigger winners), weaker. |
| R-VN4-6 | Commission $2.96 (9) | "Put together whatever fees would make reasonable sense. Even if it's a range, as long as it's a tight range." Then: "Apply the best figure you can find to the data." | Apply **$5.76 round trip all-in** ($2.88/side) in place of $2.96. Range $5.00–$5.80. Source: Tradeify's published NQ all-in and FundedNext's example (both REPORTED from web search in-call; MFFU's own fee page NOT read). **Code confirms against MFFU's fee page before the cost model changes; D-2026-10-30-A's cost model v1.1.0 is amended by a new DECISIONS entry, not edited.** Amear's expectation: prop sim accounts still deduct exchange/NFA/clearing fees from the sim balance (Claude: Topstep documents this; MFFU unverified). Effect on the baseline ≈ −$3,300 on 1,190 trades (Claude's arithmetic). |
| R-VN4-7 | Proof of concept (1, 2, 14) | "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." "We're just gonna proceed without that [historical tick data]." | **R-1104-3 defined:** PoC = full pipeline (TradingView → n8n → NT8 → Rithmic → MFFU sim) running on sim in live markets = Block 4. **No historical tick-data purchase; proceed without it.** The PROPOSED 12-item checklist from report C is not adopted; items 1–7, 10, 13–20 of v2 §5 are moot or deferred by this ruling. |
| R-VN4-8 | D-071 connection (15) | "Yes." | **The MFFU Rithmic connection is approved to be opened when Block 4 starts.** D-071 (Simulated Data Feed only) stands until then. |
| R-VN4-9 | Gate: forgeable harness files (26a) | "Yeah, I do." | Accepts the risk that anything running as his user can forge the gate's files, for now. Full closure (separate user/machine) deferred. |
| R-VN4-10 | Gate: rubric citation and PASS signal (26b, 26c) | "Use common sense and just give it the label that would make the least amount of mistakes … we need a system that has very specific description … **We're not here to fuck around.**" (Amear asked to be quoted.) | Choose the format with the least room for error. Claude's reading, to be confirmed by the gate's producer: auditor cites **rule ID and exact wording**; PASS signal is **one fixed structured verdict line** (e.g. `Result: PASS`), not a word search. |
| R-VN4-11 | Repo licences (21) | "Yes to all." | Code may borrow or re-implement from the researched repos **within each licence**. MIT: yes. No licence (e.g. skizzunni/money): read-only reference. |
| R-VN4-12 | Borrowed code in the repo | "Can it just be put in there as a branch so there could be a distinction between the pre and post?" | **Borrowed code lands on its own branch**, never straight onto `main`. |
| R-VN4-13 | NT8 add-ons on the trading install (22) | "Yeah, just do the snapshot." | Add-ons may go on the Fusion install **after a VMware snapshot** of the VM; roll back if anything breaks. |
| R-VN4-14 | Mac ↔ VM file sharing | "I want there to be file sharing between the Mac and the VM … I don't need them to be isolated right now as there's no live money being traded." | **Now:** enable VMware Fusion shared folders (Praxis.build visible to the VM) to replace the Drive round trip. **Go-live checklist item (Block 5):** isolate the VM — remove the shared folder, no access to the main directory — before real money. |

## Not ruled on (stay open)
- v2 §5 item 24 (past use of the GitHub login): no remedy requested.
- Item 23 (second Rithmic read-only connection): not reached. Partly covered by R-VN4-8 for Block 4.
- Item 19 (CME Atlassian wiki as a source): not reached.
- Item 5 (equity base for the 4% DD gate) and item 4 (Sharpe definition): not reached; relevant once r8j lands the gates. Noted in-call: baseline max DD ≈ $45k on one contract vs MFFU's $1,500 trailing drawdown.
- Item 6 (gate set / WFE when nothing is optimised): O1 stays open.

## New work requested by Amear
1. **Research brief:** a non-discretionary, codeable strategy with a higher win rate / smoother equity (mean-reversion class) that fits MFFU's $1,500 trailing drawdown better than the Noise-Area's rare-big-winner profile. Same research standard as `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md`. Claude.ai writes the brief on request; not yet written.
2. **No-trade-day check:** stays in the viability scanner, **not** added as a tenth breaker ("Just keep it where it is"). Data noted as free and backtestable: CME holiday calendar / NT8 trading-hours template, Fed FOMC dates, FRED release calendar, VIX from FRED.
3. **Fusion shared folders now; VM isolation on the go-live checklist** (R-VN4-14).

## Facts stated in-call that Code should treat as REPORTED, not OBSERVED
- Published NQ replication comparison (win rate ~38%, avg win/loss ~2.25, Sharpe ~1.67, 2010–2024, vol-sized up to 4× leverage) vs baseline (41%, ~1.9, Sharpe ≈ 1.1 by Claude's rough arithmetic). Source: report C and the 08-07 research as read in-call.
- Prop-firm fee figures ($5.76 Tradeify; $2.88/side FundedNext example; Topstep deducts fees on sim). Web search in-call; not audited.

## Dispatch order suggested (Code decides)
1. File R-VN4-1..14 (ledger + DECISIONS). 2. Commit the uncommitted 11-04 research set and this file under R-1104-1 once the gate passes. 3. r8j (P0). 4. Cost-model amendment after the MFFU fee page is read. 5. Fusion shared folders (hand step for Amear; Code writes the one-step walkthrough). 6. Higher-win-rate strategy brief, when Amear asks for it here.
