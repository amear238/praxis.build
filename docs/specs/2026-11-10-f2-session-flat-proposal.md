# F2 session-flat proposal: one governing rule for breakers #4, #5 and Deviation B

Status: PROPOSED. F2 stays FROZEN until Amear approves (A6, DECISIONS.md:1744)

Unit: 2026-11-10-f1-f2-proposal (authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z, praxis-master, items (2) and (3)). Bead context: `Praxis_build-ax4`.
Evidence for every repo-based claim is pasted in `docs/reports/2026-11-10-f1-f2-proposal-manager.md`, section "Verification evidence (command output)", under the tag in square brackets.

This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes no rubric state. F2 unblocks when "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match" (`specs/SPEC_RUBRIC.md`:43–44). Under A6, "F2's state changes when Amear approves the proposed values" (DECISIONS.md:1744–1745).

## 1. The three terms in conflict

- Breaker #4, Session time gate: "clock hits 11:30 ET → close positions, disable until next session" (Phase 3 import :100, at HEAD) [E1].
- Breaker #5, Afternoon session window: "clock enters 3:00–6:00 PM ET → disable everything" (Phase 3 import :101) [E1].
- Deviation B: session-flat = 16:00 ET cash close (DECISION_LOG 2026-07-16T19:29Z item (1); `ninjascript/PraxisNoiseAreaBreakout.cs`:188–191) [E3], [E7].

A Deviation B position runs past 11:30 (against #4) and through 15:00 (against #5) [E16].

## 2. The governing rule (PROPOSED)

**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**

That is the one rule. Breakers #4 and #5 are amended to enforce it (section 4); they do not compete with it.

- Strategies may flat earlier than 16:00 by their own rules (for example arm (b)'s Flat1559 exit policy). No system position may have its closing order sent later than the flat time.
- "Session" means the MFFU trading day, 18:00 ET → 16:10 ET (R6 step 1, `bf6fcc7`, MFFU capture trading-day.txt:10, :12; adopted for R6 as A5, R6 design :118) [E15]. The system's own flat time (16:00) sits 10 minutes inside MFFU's 4:10 PM auto-close. MFFU writes "EST"; this file reads it as US Eastern local time (ET), an INFERENCE, not stated by MFFU.
- Early-close days: flat by the exchange's early close, meaning the CME early close for NQ on that date as the exchange publishes it (the time itself is not checked in this unit). MFFU: "auto-liquidation will not occur at the half-time market close" (trading-day.txt:20–22) [E15], so on those days the system has to flatten itself.

## 3. What happens to an open position at 15:00

**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).

## 4. Proposed replacement text for breakers #4 and #5

Proposed text only. The Phase 3 import (`docs/specs/2026-11-05-phase3-build-specification.md`) is not edited by this unit.

> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.

> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.

Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system entry block in the window) and states what changes under this proposal: if adopted, the system window check is removed and only the operator lockout remains. That document notes that #5's operator lockout cannot sit on the signal path, because manual orders never pass n8n (its bypass B3, OPEN-T8).

How the rule maps to R8 (DECISIONS.md:1583–1589): R8 opens "F2 unfreezes." and says "#4 flat at 11:30" and "#5 as a disable of the system's own trading 15:00–18:00" are values "set for manual trading" that are "redone for the automated book", and it says "KEEP: … #5 as a lockout on Amear's own interaction 15:00–18:00" [E17]. The proposed #4 is the redone #4; the proposed #5 is R8's KEPT half; the redone system half of #5 becomes the 16:00–18:00 no-entry period inside #4.

## 5. Inputs carried

| Input | Question | Answer here |
|---|---|---|
| G11 (`docs/reports/2026-11-09-d11-sweep-manager.md`:63; FLAG 6 at DECISIONS.md:1645) | Do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition? | **No.** R8 (DECISIONS.md:1583–1589) names which values are redone (#4 flat at 11:30; #5 as a system disable) and which half of #5 is kept (the lockout on Amear's interaction). It does not name a governing rule among {11:30, 16:00, the window}, and it says nothing about a position open at 15:00. This file supplies both, PROPOSED [E17]. |
| G21 item 1 (same report :72; DECISIONS.md:536, :694) | Early-close stamps (F2). | Rule F2-1 covers early-close days (flat by the exchange's early close). **OPEN on the stamp itself:** the 2026-11-01 results (strategy `PraxisNoiseAreaBreakout_OppBand`) show "Exit on session close" at 12:15 on four dates whose bar data run to 13:15, plus two exits at 12:00 and one at 14:03 on 2023-04-05 (`docs/reports/2026-11-01-three-strategy-results.md`:133, :144–148) [E18]. The RTH template prints its hours in Central time (DECISION_LOG 2026-08-29T18:05:00Z) [E18]; that 12:15 is 13:15 ET read in Central time is this unit's INFERENCE, not observed. Deciding it needs a VM read-back of the template's early-close rows and time zone. No template change is proposed. |
| H02 (same report :99; `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:111) | Does #4's "next session" start at 18:00? | **Proposed: yes.** The next session opens at 18:00 ET, MFFU's session open (trading-day.txt:10) and R6's A5 day definition (R6 design :118) [E15]. Written into the proposed #4 text. |
| A9 (DECISIONS.md:1751, :1777) | The 2026-11-08 strategy filter audit is an input to F2. | Taken as input. Its finding C9 (audit :94) is that #4's 11:30 flat and #5's system disable were set for the operator, not for any edge; its finding 4 (audit :40–41) notes #4 "truncates the published Noise-Area (flat at the cash close…)", tagged [I] (inference) by the audit. Rule F2-1 follows that direction. The audit is "recommendation only … PROPOSED" (audit :4) and nothing in it is adopted by citing it here [E19]. |
| MFFU flat time | MFFU auto-closes at 4:10 PM ET (R6 step 1, `bf6fcc7`). | Rule F2-1's 16:00 is 10 minutes inside it. MFFU also warns about orders after 4:10 PM (trading-day.txt:15) [E15]. |
| Breaker #1 value | No numeric value exists anywhere (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`:39, :65) [E20]. | Rule F2-1 does not depend on it. Section 3's reliance on #1 between 15:00 and 16:00 is empty until a value exists. The value is for a later PROPOSED unit (R8 KEEP). Setting it while real money is at stake **waits for Amear (D2(c))**; today none is. |

## 6. What the rule touches (S6), by name

| Block / spec | Touch |
|---|---|
| Block 2 backtest session window | R1 "RTH = 09:30–16:00 ET" (DECISIONS.md:1551) agrees with Rule F2-1 [E21]. `PraxisNoiseAreaBreakout.cs` has an explicit 16:00 flatten (:188–191, WRITTEN) with `IsExitOnSessionCloseStrategy` as backstop (:108). In the 2026-11-01 OppBand run the backstop made all 792 exits and no `FlatEOD` exit appears (results :132) [E18]; if the template's Central-time hours apply (OPEN-F2-3), the exits stamped 16:00 may not be 16:00 ET. So "the backtest flattens at 16:00 ET" is UNVERIFIED. The 1-minute bar-close modelling (decision on a bar close, market exit next bar; Amear's ruling 1, DECISION_LOG 2026-11-05T23:50:09Z) means a backtest flat may fill after 16:00:00; whether the backtest must decide on the 15:59 bar to meet "closed by 16:00:00" is OPEN-F2-1. |
| Walk-forward arm (b) exit policy Flat1559 | Allowed: an earlier flat than 16:00. (`git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` is the authority; parked under `Praxis_build-diq`; not edited.) |
| Block 4 parity gate (rubric O4, `specs/SPEC_RUBRIC.md`:108–113) | Rule F2-1 removes the 11:30 cut and the 15:00 system disable, so a breakers-on backtest and the live run use the same session clock as the current 16:00-flat backtests. O4's question (breakers on, off, or both) is not answered here. |
| Deviation B | Becomes the governing rule (no change to its 16:00). |
| Deviation C, breakers #2 and #3 | Allowing entries 11:30–16:00 gives the Noise-Area more decision points per session (it acts at HH:00 / HH:30; header and `Description`, :101), so a "max 2 trades/day" cap and "two and done" bind more often. R8 says both are redone; values are not proposed here. Bead `Praxis_build-yra`. |
| R6 evening-entry strategy (Pre-Announcement Drift) | Entries at 18:05 fall after the 18:00 next-session start, so they are allowed. Variants that hold to 16:05 (2S/2A, R6 design :111) break Rule F2-1's 16:00 flat and would have to exit by 16:00 (OPEN-F2-2). Whether MFFU counts an evening entry as "holding overnight" is R6's OPEN-1, MFFU's to answer (F4 channel). |
| Last-Half-Hour Momentum (`PraxisLastHalfHourMomentum.cs`) | Its 15:30 entry and 15:59-bar flat (`Description`, :141) would be inside the rule. It is retired (filter audit :110); nothing is reopened. |
| Breaker #8, #9 and the F1 topology | The 16:00 flat needs a FLATTEN path to the order engine, which does not exist (topology doc, breaker #1 and #4 rows). |
| Block 3 deterministic fallback script (Phase 3 :109) | Its "session time" threshold becomes 16:00, not 11:30. |
| D6 drawdown check (`docs/reports/2026-11-09-d6-drawdown-check-manager.md`) | Its 09:30 re-run and drawdown figures are unchanged by the rule. |
| Rubric F2 "Why frozen" (`specs/SPEC_RUBRIC.md`:37–42) | The operator-schedule justification for the 11:30 cut named there is retired by Rule F2-1, not repaired. |

## 7. OPEN

| ID | Open item | What would decide it |
|---|---|---|
| OPEN-F2-1 | Backtest flat on the 15:59 bar (fills by 16:00) or the 16:00 bar (fill may land after 16:00:00). | The master under D1 with the O4 parity statement (not a D2 item); changeable by Amear. |
| OPEN-F2-2 | R6 variants that hold to 16:05. | The R6 unit under D1 (exit by 16:00 under Rule F2-1, or propose an exception inside MFFU's 16:10); changeable by Amear. |
| OPEN-F2-3 | Early-close stamps 12:15 vs 13:15 (G21 item 1). | VM read-back of the trading-hours template. |
| OPEN-F2-4 | Whether R8's #8 numbering is the Phase 3 import's (topology doc OPEN-T6). | A master's reading under D1, changeable by Amear (his words, so his reading wins). |
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)

> ***Added 2026-11-12; not part of the text above.*** Body lines 1–81 above are unchanged. Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A), decided by master under D-2026-11-08-D D1, changeable by Amear. This note carries out D-2026-11-12-A (DECISIONS.md:2205) and Amendment 1 at the end of `docs/specs/2026-11-05-phase3-build-specification.md` (amended #4 at its line :212, amended #5 at :224). It makes no new design choice and writes no DECISIONS.md entry; where an aligned reading would need a choice that D-2026-11-12-A and Rule F2-1 do not make, the item is listed as OPEN below with both readings. Each old line below is copied by script from this file at HEAD, byte-identical.

**Level.** Unchanged: the nine breakers, #4 and #5 included, remain SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This note changes how lines are read; it builds nothing.

### :8 — rubric line citation (follow-up F-7)

```text
This file is a proposal only. It writes no DECISIONS.md entry, edits no breaker spec, and changes no rubric state. F2 unblocks when "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match" (`specs/SPEC_RUBRIC.md`:43–44). Under A6, "F2's state changes when Amear approves the proposed values" (DECISIONS.md:1744–1745).
```

Aligned reading: the F2 unblock clause quoted here is at `specs/SPEC_RUBRIC.md`:93–94 at HEAD `006a08b`, inside the section "### F2 — Session-flat time vs. breakers #4 and #5" (:81), which now sits under "## PASSED — closed criteria". It was at :30–31 at `e3323a8` (D-2026-11-12-A); the rubric change at `c29d08b` moved F2 into PASSED. The quoted words are unchanged. The second citation on this line, DECISIONS.md:1744–1745 (A6), is unchanged. The line's "changes no rubric state" is true of this file; rubric F2's state was moved at `c29d08b`, not by this file.

### :79 — OPEN-F2-5 (follow-up F-9)

```text
| OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
```

Aligned reading: OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits. Each step its "What would decide it" column names now has a record: Amear's approval of Rule F2-1 (D-2026-11-11-A, V2, DECISIONS.md:2108); a DECISIONS.md entry (D-2026-11-12-A, DECISIONS.md:2205); the amended #4/#5 text in the breaker spec (Amendment 1 of the Phase 3 spec). Rubric F2 is PASSED@e3323a8. Limits carried from D-2026-11-12-A, not changed here: Amear's approval was given on the words of a summary; the #4/#5 text is the master's adoption under D1, not Amear's words, changeable by Amear; whether his approval reaches that text, and whether A6 is triggered, are not graded.

Read with :3, which states this file's status when it was filed:

```text
Status: PROPOSED. F2 stays FROZEN until Amear approves (A6, DECISIONS.md:1744)
```

That status is historical: Rule F2-1 is adopted (D-2026-11-12-A) and rubric F2 is PASSED@e3323a8. The rest of this file is unchanged; OPEN-F2-1 to OPEN-F2-4 (:75–78) stay open.
