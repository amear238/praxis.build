# PRAXIS — Strategy Filter Audit (manual residue vs automation)

**Date:** 2026-11-08. **By:** Claude.ai Praxis channel (research agent), at Amear's brief of the same date.
**Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. No decision, spec or ruling is changed. The 2026-11-08 ruling RTH = 09:30–16:00 ET is not reopened.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Grades.** **[V] VERIFIED** = read in the cited source this session. **[I] INFERRED** = the auditor's reasoning. **[U] UNVERIFIED** = nobody has checked. Every class assignment (A/B/C) is the auditor's reading and is therefore [I]. Every "Source" cell is [V] unless marked otherwise.

**Sources read in full.**
- **D1** TRADING COMEBACK PLAN — THREE-PATH ARCHITECTURE (Path 1A)
- **D2** Verified NQ Futures Trading Strategies: Behaviorally-Screened and Algo-Impact-Tested Shortlist
- **D3** PHASE_2_INPUT_COMPILED_Round_1_and_2
- **D4** PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts (the Round 3 prompts)
- **D5** PHASE_2_STRATEGY_DECISION_Handoff_Round3
- **D6** PHASE_2_STRATEGY_DECISION_Compiled_Round_3
- **D7** Phase 2 Closure & Phase 3 Scope Definition
- **D8** Systematic, Higher-Frequency NQ Strategies to Pair with the Noise-Area Breakout

**Also cited (repo, read earlier in this channel, labelled where used):**
- `docs/reports/2026-11-01-three-strategy-results.md:67` (baseline average win and loss)
- `docs/reports/2026-10-31-voice-handoff-backtest-session.md` §0 (LHM research-only)
- `docs/reports/2026-11-07-return-handoff-claude-ai.md` §1 / 11-04 return handoff (LHM retired, PF 0.84)
- `docs/reports/2026-11-04-voice-session-notes-4.md` (higher-win-rate research request)
- `docs/reports/2026-10-28-voice-session-notes.md` (import-file 17:00 and 18:01 rows)
- DECISION_LOG `2026-08-29T18:05:00Z` (F2 frozen on breakers #4 and #5 vs the 16:00 flat)

Breaker #5 is referred to only by number and window (15:00–18:00 ET), per D-2026-08-06-A.

---

## 1. Summary

1. **Two filters did most of the manual-residue damage.** C1 is the 09:00–11:30 active window; C3 is the fixed R:R shape. C2 (macro narrative) mostly shaped rankings and roles, not eliminations. [I]
2. **The R:R shape filter (C3) is not valid for an automated system.**
   - It would fail the project's own anchor. The Noise-Area has a published payoff of 2.25 and no partial-plus-runner structure. The repo baseline's average win ÷ average loss is $1,815.02 ÷ $964.79 ≈ 1.88 (repo `three-strategy-results.md:67`). A ≤1-trade-per-session strategy needs 3:1. [V for the figures, I for the conclusion]
   - It also selects *against* what MFFU's trailing drawdown rewards, which is smoother equity and a higher win rate. That is the class Amear asked to research on 2026-11-04 (notes-4).
3. **Two resolved NQ/ES strategies were parked or demoted mainly by C filters and warrant re-evaluation** (§5):
   - **(1) Pre-Announcement Drift (Hu et al. 2022).** Its "overnight hold" came from a 09:30 entry chosen for the manual window. An evening-entry variant has the same geometry R3 already accepted on MFFU for Overnight Drift. [I]
   - **(2) Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).** It was demoted to "manual fallback" with no non-C reason recorded in any of the eight docs. [V for the absence in D3–D8; I for the cause]
4. **Breakers #2, #3, #4 and the system-wide half of #5 carry manual-era values into the automated book.**
   - Breaker #4 flattens at 11:30. That truncates the published Noise-Area (flat at the cash close, D2), CO-OC's exit window (D8) and the Announcement-Day Premium. [I]
   - The 2-trades-per-day cap conflicts with the R3 portfolio. [I]
   - This sits inside F2 (FROZEN). It is flagged only, not decided.
5. **The overnight-hold parking of FOMC Even-Week is a genuine MFFU rule (A), not manual comfort.** For Pre-Announcement Drift the hold is an artifact of C1 (§4.4).

---

## 2. Filter table

### A — Structural

| ID | Filter | Source | Justification |
|---|---|---|---|
| A1 | Fully objective, codifiable entry/exit; no visual or discretionary judgment | D1 Path 1A "Discretionary level"; D4 Hard Filter 1; D6 F5 | A coded system can only run what can be coded. |
| A2 | Automation feasibility | D1 Path 1A "Automation potential"; D6 F5 | Same as A1, applied to the platform: NinjaScript, or Pine plus n8n. |
| A3 | Published performance data; ≥200 trades in sample | D1 "Back-test data required"; D4 Hard Filter 4; D6 F1 | Validation needs an evidence base, whoever executes. |
| A4 | Post-2018 / algo-impact survival | D2 §1, §4; D4 Hard Filter 4; D6 F4 | Edge decay is a property of the market, not of the operator. |
| A5 | Source tiering (peer-reviewed or institutional; no course sellers) | D1 credibility note; D4 "Source Requirements" | An epistemic standard, independent of execution mode. |
| A6 | Survives instrument-specific costs; ≥$20 per trade after costs | D4 Hard Filter 5; D8 Strategy A/B/C rows | Costs apply to every fill. |
| A7 | MFFU constraints: automation permitted, EOD trailing drawdown, flat by close, <200 trades/day, 50% consistency rule | D4 Hard Filter 6; D5 "Prop Firm & Infrastructure"; D6 F6 | The account's own rules. Stated in the docs; not checked against MFFU's current terms [U]. |
| A8 | MFFU news-event (T1) restrictions | D6 #4, #5, §5 gap 5 | A firm rule. Which events, and how many minutes of blackout, are [U] in these docs. |
| A9 | Instrument routable on Rithmic/MFFU | D5 instrument note; D6 #7, #10 | Platform reach. |
| A10 | Latency feasibility (no co-location needed) | D8 Key Finding 5 | The infrastructure cannot do microsecond horizons. |
| A11 | Defined active window tied to the edge's mechanism | D4 Hard Filter 7 | A strategy definition requirement. Not the same as C1. |
| A12 | Liquidity flag (<50k contracts/day) | D4 Agent 1 constraints | Fill quality under automation. |
| A13 | Not a duplicate of, or highly correlated with, the baseline | D8 Strategy B row and §3; D6 §3 | Portfolio construction on one account. |
| A14 | No same-instrument position conflict on one account | D8 §3 ("at most one leg has a position"); part of D6 F7 | One account cannot hold two strategies' NQ positions independently. |
| A15 | Low frequency to reduce prop-firm detection risk | D3 §1 and §6 Scenario B | Was A at the time. **Now void:** MFFU permits automation in writing (F4 closed; repo F4 evidence). |

### B — Behavioural, still valid under full automation

| ID | Filter | Source | Failure mode it guards against |
|---|---|---|---|
| B1 | Mechanism clarity: "teach it to someone" | D4 Hard Filter 3; D5 Gap 4; D6 F3 | The operator switches off or overrides a system he can't explain at the first drawdown (D5 conviction quote). It also feeds the Block 5 comprehension gate, where Amear explains entries, exits and breakers unprompted. **Contamination:** in D2 and D5 it was partly scored as "macro story" (C2). §4.3 separates the two. |
| B2 | Breaker #9, round-number block on orders "with no pending signal" | D3 breaker table #9 | Operator-entered orders. It never blocks a coded signal, so it filters no strategy. |
| B3 | Behavioural detectors: no-signal order block, revenge-trade block, post-win sizing alert | D3 "Behavioral Pattern Detection" table | Operator interference. These filter no strategy. |
| B4 | Floor rule; breaker #1 daily loss limit | D1 "Floor Rule"; D3 #1 | Staying in the game. MFFU has no daily loss limit (D5), so this is the project's own floor, not the firm's. |
| B5 | Breaker #2 max trades, and #8 cascade detector, **as caps** | D3 #2, #8 | The operator adding trades, and system runaway. **The value** "2 per day" was set for manual NQ; see C11. |
| B6 | Breaker #5 **as a lockout on human interaction** 15:00–18:00 | D3 #5 | Operator decisions in the stated window. The same breaker **as a disable of the system's own trading** is C9. |
| B7 | Number of live strategies the operator must be able to explain | D1 §9 (specialization); B1 | Comprehension load at Block 5. This is the only valid residue of C7. |

### C — Manual residue

| ID | Filter | Source | Justification |
|---|---|---|---|
| C1 | Active window 09:00–11:30 ET; no London/Asian dependence | D1 Path 1A; D2 title and §5 | It existed so a human could execute in a set window. D4 itself says "both constraints are removed" under automation. |
| C2 | Fundamentals / macro-narrative preference for conviction | D1 "Strategy style bias"; D2 "Macro narrative" notes; D5 "Style preference" | Conviction at the moment of clicking. D3 §6 already says it is "irrelevant because the system executes" (Scenarios A/B). |
| C3 | R:R shape: 3:1 on a 50% partial plus runner (low frequency); 1.5:1 (higher frequency); "avg win ÷ avg loss < 1.5 fails regardless of win rate" | D4 Hard Filter 2; D5 Gap 3; D6 F2 | Copied from the discretionary reference style. D1 had called those figures "reference only — not required". §4.1 covers it. |
| C4 | Ledger sensitivity / screen-watching during holds | D2 compatibility notes, strategies #2, #3, #4 | A human watching P&L. The structural answer is no manual order path (B3), not strategy choice. |
| C5 | Cascade resistance as a property of the strategy | D2 #1, #5 notes | A coded strategy takes only its rule-permitted trades. Operator cascade is caught by B5. |
| C6 | Fabricated-setup resistance as a property of the strategy | D2 #1–#4 notes | A coded rule cannot fabricate a setup. What remains is A1. |
| C7 | Single-instrument specialization / cognitive load | D1 executive summary (dual-instrument overload) and §9; D2 "Specialization" notes and CTA row | Monitoring load for a human. Only B7 survives. |
| C8 | NQ preference from existing competence and pattern recognition | D1 "NQ preferred"; D6 §4 point 5 | Manual skill transfer. D6 §4's other reasons (Sharpe, infrastructure, liquidity) are A and keep NQ as anchor on their own. |
| C9 | Session timing tied to the operator's day: "aligns with the medication window" (D6 §4 point 3); breaker #4 flat at 11:30; breaker #5 disabling the **system's** trading 15:00–18:00 | D6 §4; D3 #4, #5 | These time limits were set for the operator, not for any edge. **F2 is FROZEN on exactly this contradiction** (DECISION_LOG 2026-08-29T18:05:00Z), so this is flagged only. |
| C10 | R3 F7 "does not conflict with the 09:30–11:30 baseline" | D6 F7 | The 11:30 boundary is C1/C9 residue. Its concurrency concern is A14. It eliminated nothing alone (§3). |
| C11 | Breaker values tuned for manual NQ: max 2 trades/day; "two and done"; inter-trade interval < 5 minutes | D3 #2, #3, #8 | As caps they are B5. As **numbers** they cap any book above 2 trades/day, and the <5-minute rule would block a same-bar exit-and-reverse, which the Noise-Area does [I]. |

---

## 3. Affected-strategy table (every strategy touched by a C filter)

"Primary?" = was the C filter the main stated reason. "Non-C disqualifier?" = does an A reason disqualify it on its own.

| Strategy (source) | Status given | C filter(s) | Primary? | Non-C disqualifier? |
|---|---|---|---|---|
| Overnight Drift (D2 §5) | ELIMINATED on the active window; **re-evaluated in R3 and passed as #2** (D6) | C1 | **Yes** [V] | No on MFFU (D6 #2 "MFFU YES"). Open: post-2020 evidence (A4). **Already corrected.** |
| Pre-Announcement Drift NFP/ISM/GDP (D2 #3; D4 table) | PARKED: "overnight hold + thin annual sample" | C1 (the 09:30 entry, chosen "comfortably inside the 9:00–11:30 window", D2 #3) produced the overnight hold; C4 secondary | **Root cause yes** [I]. The stated reason is A7. | The hold violates A7 only in the 09:30-entry form. An evening entry with exit before the release is untested against A7/A8 [I/U]. Thin sample (A3) is a power problem, not a disqualifier. |
| Macroeconomic Announcement-Day Premium (D2 #4; D4, D5 tables) | "RETAINED as manual fallback only" | C2 (narrative framing); C4; C9 would truncate an open-to-close hold at 11:30 | **Yes, by elimination:** no non-C reason is recorded in D3–D8 [V absence; I cause] | Possible A8: it holds through FOMC (14:00) and ISM (10:00) releases [U]. A14: same NQ day as the baseline unless run on ES. |
| FOMC-Cycle Even-Week (D2 #2; D4 table) | PARKED: "overnight hold incompatible with prop firm" | C4 secondary; C1 shaped the 09:30 entry, but the hold is multi-day by design | No | **Yes on MFFU:** a multi-day hold against flat-by-close (A7) [V rule as stated]. Viable only on a venue that permits multi-day holds (D2 #2). |
| Last-Half-Hour Momentum (D8 Strategy A; D4 "PASSED") | Built 10-31 as research-only "because it trades inside breaker #5's window" (repo, 10-31 handoff §0); retired by R-VN3-1 after net PF 0.84 (repo) | C9 (breaker #5) | At classification, yes [V] | **Yes:** net-of-cost performance (repo). Untested variant: the thresholded θ version D8 recommended was not what was built [I]. |
| CO-OC Reversal (D8 Strategy C) | CONDITIONAL PASS, NQ post-2018 gap | C9: breaker #4 at 11:30 cuts its 12:00–15:00 exit window [I] | No | The evidence gap is A4, not disqualifying. |
| Noise-Area baseline (D2 #1) | SELECTED | C2 (scored "weaker" on narrative); C3 would fail it (payoff 2.25 / 1.88, no partial); C9 breaker #4 cuts the published close-flat | No (selected) | None. **It shows C3 and C9 are inconsistent with the anchor.** [I] |
| Carry + Momentum composite (D6 #9) | "FAILS R:R hard filter" | C3 | **Yes** [V] | **Yes on MFFU:** month-end holds against flat-by-close (A7) [I]; naive carry near zero since 2010 (A4) [V as stated]. |
| FOMC-Day Short-USD Basket (D6 #6) | CONDITIONAL: "R:R unvalidated at 3:1 (low-freq 8/yr)" | C3; C9 (13:00–17:00 overlaps breaker #5) | One of several | A3 (8 trades a year, low power); A9 (spot FX venue). Low priority. |
| ORB on Stocks in Play (D2 #5) | Deprioritized: not the preferred class, fails cascade resistance, weak narrative | C2, C5, C8 | One of several | **Yes:** an equity universe not routable via MFFU futures (A9) [I]; the NQ version lacks evidence (A4) [V]. |
| Cross-asset CTA (D2 §5) | ELIMINATED/demoted: "for a single-NQ trader, not the right fit" | C7 | One of several | **Yes:** portfolio-level capital across many instruments; 2023–25 drawdown (A4/A7) [V as stated]. |
| R3 FDAX/FESX last 30 minutes (D6 #7) | BLOCKED on infrastructure; noted "overlaps NQ tail" | C10 | No | **Yes:** Eurex not routed by MFFU (A9) [V]. |
| R3 Crack-spread mean reversion (D6 exclusions) | "too complex for prop accounts" | C7 possibly | Unclear | Multi-leg margin and execution on a prop account (A7/A9) [I]. Not pursued. |
| The other 13 resolved NQ/ES entries (D4 table: ORB standalone, Pre-FOMC drift, PEAD, VRP/short-VIX, End-of-Day Reversal, OFI, 0DTE gamma, VWAP/Bollinger reversion, gap fade, ML/GBM, TC-FHM; Noise-Area SELECTED and LHHM covered above) | ELIMINATED, EXCLUDED or DEFERRED | none | — | Each carries an A reason as stated (A4, A10, A13, A7 tail risk, or a cross-sectional instrument) [V]. |

**Coverage note.** Rounds 1–2 searched NQ/ES only inside 09:00–15:00 ET (D4 "Purpose"). R3 Agent 3 reopened NQ/ES outside the NY session (D4 Agent 3 mandate) but was told not to re-investigate the resolved list. So any NQ/ES strategy resolved in Rounds 1–2 under C1/C2 framing was never retested by R3. The two in §5 are the ones where that matters. [V for the scope; I for the consequence]

---

## 4. Step 4 findings

### 4.1 The fixed R:R shape (3:1 partial plus runner; 1.5:1)

**Finding: not a valid filter for an automated system.** Replace it with expectancy, net Sharpe and drawdown survival under MFFU's rules. [I]

- **Expectancy, not shape, decides whether a strategy pays.** Expectancy = win rate × average win − loss rate × average loss, net of costs. A 38% / 2.25 strategy and a 60% / 1.0 strategy can have similar expectancy. The filter's own clause, "fails regardless of win rate" (D4 Hard Filter 2), discards that equivalence. [V for the text; I for the arithmetic]
- **MFFU's binding constraint is path, not shape.**
  - The account is a $1,500 EOD trailing drawdown plus a 50% consistency rule (D5, D4). Both punish long losing streaks and lumpy P&L.
  - A low-win-rate, high-payoff profile (what C3 selects) produces exactly those streaks.
  - The repo baseline already shows it. In-call figures: max drawdown about $45k on one NQ, against $1,500 (notes-4 "Not ruled on").
  - So C3 pushes selection the wrong way for this account. [I]
- **It contradicts the anchor.** The Noise-Area has no 3:1 partial or runner, and a payoff of 2.25 published / 1.88 in the repo. It survives only because the resolved list exempted it (D4). [V figures; I conclusion]
- **It was never actually applied with data.** D6 §5 gap 4 and D7 §1 state that every strategy is "formally R:R unvalidated". Its one hard elimination was Carry + Momentum, which has an independent A disqualifier on MFFU. [V]
- **Origin.** D5 Gap 3 quotes Amear's requirement. D1 had framed the same 1:3 / 1:10 figures as "reference only — not required". The hardening happened between D1 and D4. [V]
- **What should govern instead (PROPOSED):**
  - net expectancy per trade above the A6 floor;
  - net Sharpe and out-of-sample walk-forward gates, as already in the Phase 3 spec;
  - simulated survival of MFFU's trailing drawdown per account tier, plus a consistency-rule simulation, as D8 §5 already specifies for LHHM and CO-OC.
- **Live consequence.** The higher-win-rate research Amear asked for on 2026-11-04 (notes-4, "New work" item 1) would be gutted by C3. Mean-reversion strategies typically run average win ÷ average loss below 1.5 [I]. That brief should not inherit C3.

### 4.2 The "resolved" NQ/ES exclusion list

**Finding: three entries were resolved only, or mainly, under manual constraints. One is already corrected; two are open.** [I]

- **Overnight Drift.** C1 only. Corrected: R3 passed it as #2 (D6). [V]
- **Pre-Announcement Drift.** Its parking reason ("overnight hold") is A on its face. The hold exists because D2 placed the entry at 09:30 on the day before the release, explicitly to sit "comfortably inside the 9:00–11:30 AM ET window" (D2 #3 notes), and D2's own §1 says the return is "concentrated in the overnight session before the announcement". Under automation the entry can move to the evening session and exit before the release. That is the same entry and exit geometry R3 judged "MFFU YES" for Overnight Drift (D6 #2: 02:00 entry, exit by 09:25). [V for the text; I for the variant's compliance]
- **Announcement-Day Premium.** Labelled "manual fallback" (D4, D5). D8 Key Finding 9 confirms the aggregate premium is "intact in 2018–2024" but keeps it as fallback without a reason. D3 §6 ties narrative strategies to the manual scenario. No A reason for not running it automated is recorded in D3–D8. [V absence; I cause]
- **The remaining entries** carry A reasons as stated (§3 last row). [V]

### 4.3 Mechanism clarity ("teach it to someone")

**Finding: B, still valid, but its scope should be narrowed.** [I]

- **Why B.** Under full automation the failure mode is operator interference: disabling or overriding a system he cannot explain during a drawdown (D5 conviction requirement, D7 §3 "conviction of pushing away intrusive thoughts"). It also serves the Block 5 comprehension gate. Both survive automation.
- **What is C inside it.** In D2 and D5, "clarity" was partly scored as "macro story". D2 #1 calls the Noise-Area's dealer-hedging rationale "less viscerally satisfying than a CPI-narrative trade". That part is C2.
- **The B version** asks only: can Amear state the rule, and who pays the edge and why, unprompted? Microstructural mechanisms (dealer hedging, inventory risk) pass that test as well as macro ones.
- **R3's F3 wording** ("structural/economic driver, not pattern recognition", D6) is an evidence-quality test and belongs with A4.
- **It eliminated nothing on its own** in D6 or D8. [V]

### 4.4 Overnight-hold parking

**Finding: A for FOMC Even-Week; a C artifact for Pre-Announcement Drift.** [I]

- **FOMC Even-Week.** The published strategy holds across multiple days (D2 #2). That conflicts with MFFU's "flat by close" (A7, as stated in D4 Hard Filter 6). The rule is real for this account. The strategy is venue-blocked, not operator-blocked: D2 itself says it is "materially stronger on the trader's own capital". Re-evaluation would need a second venue, which is a money decision. C4 (ledger watching) was a secondary note only. [V for the text; I for the class]
- **Pre-Announcement Drift.** See §4.2. The multi-session hold was created by the 09:30 entry, not by the edge. [I]
- **Discrepancy to check (for Code, not a decision):** MFFU's flat time appears as 16:10 (D6 session map, "MFFU Auto-Flat") and as 16:59 (D8 Strategy A row). One is wrong or out of date. [V both; which is current is U]

---

## 5. Step 5: ranked re-evaluation list (PROPOSED)

1. **Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022, JFE), evening-entry variant.**
   - **Strongest reason:** its only structural disqualifier, the overnight hold, was manufactured by the manual-window entry. Moving the entry to the evening session gives the entry and exit geometry R3 already accepted on MFFU for Overnight Drift. [I]
   - **Checks before any build:**
     - MFFU's current news rule: which releases count as T1, how many minutes of blackout, and whether an exit must clear it [U].
     - Whether the evening entry counts as the same trading day under MFFU's flat rule [U].
     - Post-2019 persistence: the papers' samples run to 2019 (Hu et al.) and 2018 (Fisher–Martineau–Sheng), per D2 [V]. Later years are [U].
   - **Data:** the existing 1-minute file appears to carry the evening session (10-28 notes: 1,302 rows at 17:00:00 and 1,354 at 18:01:00), so a first backtest may need no purchase [I]. It would need its own session template; the RTH ruling for the baseline is untouched.
2. **Macroeconomic Announcement-Day Premium (Savor–Wilson 2013/2014; Ai 2024).**
   - **Strongest reason:** fully systematic (D2 #4: 10/10), intraday-flat, post-2018 evidence intact through 2022 (D2 #4, Ai 2024 [V as stated]), and demoted with no non-C reason on record. [I]
   - **Checks:**
     - MFFU news rule for holding through FOMC 14:00 / ISM 10:00 [U].
     - Breakers #4/#5 truncation (C9, F2 FROZEN).
     - A14 same-day NQ conflict with the baseline: run on ES or set a priority rule [I].

**Not recommended for re-evaluation, with the non-C reason:**
- **Overnight Drift:** already re-evaluated and passed (D6).
- **FOMC Even-Week:** MFFU flat-by-close (A7); a second-venue question.
- **Carry + Momentum:** month-end holds (A7), naive carry decayed (A4).
- **Last-Half-Hour Momentum:** retired on net performance (repo).
- **ORB Stocks in Play:** equity universe (A9).
- **CTA:** portfolio capital (A7/A4).
- **FOMC-Day USD basket:** 8 trades a year (A3) and spot-FX venue (A9).

**Process recommendation (PROPOSED):** before the higher-win-rate research brief runs:
- drop C3;
- replace it with net expectancy, out-of-sample gates and MFFU drawdown-and-consistency simulation per tier;
- strip C1, C2, C4, C5, C7 and C8 from its filters.

Keep A1–A14, B1 (narrowed per §4.3) and B7.

---

## 6. Open questions for Amear (only his)

1. **R:R filter:** retire the 3:1 / 1.5:1 shape filter for all future strategy research, including the higher-win-rate brief, and judge by net expectancy, out-of-sample gates and MFFU drawdown survival instead?
2. **Re-evaluation:** test the two §5 candidates on the existing minute data, research and backtest only, nothing bought?
3. **Breakers #2, #3, #4 and the system-wide part of #5:** their values were set for a human trader and truncate several strategies, including the baseline's published close-flat. This is F2's frozen question. Do you want this audit filed as an input to F2? Filing it decides nothing.
4. **Overnight-hold strategies (FOMC Even-Week):** these only work on a venue that allows multi-day holds. Park permanently, or revisit if a second venue or own capital is ever on the table?

**For Code, not Amear:** resolve the MFFU flat-time discrepancy (16:10 vs 16:59) and read MFFU's current T1 news-rule text. Both are reads, not decisions.
