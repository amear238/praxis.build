# AMEAR'S ANSWERS A1–A11 TO THE D-2026-11-08-A FLAGS — 2026-11-08 voice session (WHO: amear)

Filed verbatim by praxis-master on 2026-11-08 from the message Amear pasted into the Claude Code session as his second message of the day (received while the U1 correction unit was running; `date -u` not read at receipt — the row in DECISION_LOG carries the estimate). Evidence grade: OBSERVED (the fenced block is the message as received, copied without edits; nothing acted on at the time of filing). The words are REPORTED BY the Claude.ai Praxis channel (its record of his voice session) and pasted by Amear. They answer FLAGS 1–6 of D-2026-11-08-A (DECISIONS.md:1534–1645, working tree) and the three items the master routed to his open list in DECISION_LOG `2026-11-08T14:35:00Z` (R3 vs Q8; whether R2/R3 discharge O1; audit §6 Q3), plus the master's R-1104-2 call on settlement 9, plus one standing rule change (A11).

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

---

The paste, verbatim. The first line and the outer fence are the Claude.ai channel's framing; the rulings are the lines from `PRAXIS — AMEAR'S ANSWERS` to the end of A11. The exact line numbers of the ruling block in this file are recorded in the DECISION_LOG row after an `openssl dgst -sha256` read, not counted by hand.

~~~text
That’s all nine. Here’s the updated handoff to paste to the Code agent:

```
PRAXIS — AMEAR'S ANSWERS TO D-2026-11-08-A FLAGS (voice, 2026-11-08)
WHO: amear. File as D-2026-11-08-B, citing this session.

A1  FLAG 1: R4 applies to gate 2 only. The values-spec §6 in-sample
    selection statistic stays as written.
A2  FLAG 2: Gate 2 "OOS Sharpe >= 1.0" = the §6 formula on
    out-of-sample sessions: daily net P&L after commission and
    slippage, 0 on no-trade sessions, sqrt(252), sd n-1, risk-free 0.
    Fixed base, no compounding; tier pick not needed for this gate.
A3  FLAG 3: Win rate is not a Block 2 pass gate. Per trade:
    W / (W + L + 0.5 x B), B = trade exited at its entry price.
    No-trade sessions excluded. It is the quantity for O4's Block 4
    "within +/-15% win rate" check, computed identically on backtest
    and paper.
A4  FLAG 4: Max-DD gate = backtest max drawdown must stay below 80%
    of the ruled limit, i.e. below the lower of 3.2% of the MFFU
    account size and 80% of MFFU's trailing drawdown limit. This
    amends D-2026-11-05-A item 3 with a safety buffer for model error.
    Evaluated against every tier row; tier pick stays Q9. Closes the
    notes-4 DD equity-base item.
A5  FLAG 5: For arms (a)/(b), "trading day" = session i of §6
    (09:30-16:00 ET per R1). For R6 evening-entry research, "trading
    day" = MFFU's own definition from its current terms.
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
A7  R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not
    applicable). Arm (b) on gates 1-6 plus PBO < 0.05.
A8  O1 is discharged by R2 + R3 + A7. Gate 6 formula (Pardo WFE):
    annualised OOS net profit / annualised IS net profit of the
    selected parameter set, pooled across all windows; pass >= 0.50.
A9  File the 2026-11-08 strategy filter audit as an input to F2.
A10 The master's R-1104-2 call that settlement 9 stands beside R6 is
    accepted.

STANDING RULE CHANGE
A11 Amear no longer edits any repo file by hand, including
    specs/SPEC_RUBRIC.md. Amear decides; agents write. Every rubric
    edit cites a logged Amear approval inline and passes the auditor
    before commit. Replace the rubric's "The build side does not edit
    this file. It proposes changes; Amear applies them." accordingly,
    citing this ruling. Do not hand Amear paste-in steps for repo
    files.
```
~~~

---

## Master's filing notes (not rulings; the master's readings, changeable by Amear)

1. **Sequencing.** D-2026-11-08-B is appended to DECISIONS.md only after D-2026-11-08-A's commit lands (the A entry is in the audited temp index `commit-idx-u1`; appending B first would change that blob). Then: B filed → verified on disk → the units it authorises (rubric edit under A11; values-spec amendments for A2/A4/A5/A7/A8; O1 state change under A8; A9 into the F2 proposal unit U4) are dispatched, one manager at a time.
2. **A11 and the rubric.** A11 replaces `specs/SPEC_RUBRIC.md:3-4` by an agent's hand. The uncommitted July hunk in that file (`git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10 0`, R-A/R-B/R-C at :267+) is return handoff §4 item 4, still Amear's; a rubric edit unit builds its blob from HEAD's rubric plus the :3-4 change only, so the July hunk stays out unless he rules on it. A11 also supersedes the part of bd memory `amear-walkthrough-preference` that named Amear as the only hand for rubric edits and commits; the memory is updated to say so, append-style, by the master.
3. **A8 and O1.** `PASSED@<sha>` is the rubric's "graded and closed" state. Reading: the sha is the commit that lands D-2026-11-08-B; the auditor of the rubric unit confirms the written statement O1 asks for exists at that sha (R2, R3, A7, A8 in B). Changeable by him.
4. **A4** amends D-2026-11-05-A item 3 ("the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit") to 80% of that; the values spec §8 "Max-DD gate base" line (`docs/specs/2026-11-06-walk-forward-values.md:135`) and WF spec §6 lines that carry 4% need an amendment unit citing B. Not done at filing.
5. **A5** second sentence depends on U2's read of MFFU's current terms ("MFFU's own definition") — U2 records that definition; nothing is assumed about it here.
