# PRAXIS — SPEC RUBRIC

Authority: the scoping agent (Claude.ai) via Amear. The build side does not
edit this file. It proposes changes; Amear applies them.

This file exists because context windows compact and reasoning held only in a
session is reasoning that will be lost. Every criterion below is graded, not
recalled.

State values: `FROZEN` (blocks dependent work) · `OPEN` (gradeable now) ·
`PASSED@<sha>` (graded and closed) · `WAIVED` (Amear overrode; see DECISION_LOG).

---

## FROZEN — nothing downstream may proceed until these clear

### F1 — Signal-path topology vs. circuit-breaker placement
**Criterion.** A written statement, committed, naming what emits the live
trading signal, and showing how each of the nine circuit breakers sits upstream
of order submission on that path.
**Why frozen.** Block 3 specifies the breakers as n8n workflow gates that
terminate before the file-write node. Deviation A moved strategy logic into
NinjaScript. If NT8 computes the signal internally there is no webhook, no n8n
execution, and no gate — every breaker is bypassed and the Block 1 pipe is
unused.
**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
and the auditor confirms it addresses every one of the nine breakers by name.
**Blocks.** Block 3 entirely. Any SHM threshold derivation.

### F2 — Session-flat time vs. breakers #4 and #5
**Criterion.** One governing rule, written down, resolving: breaker #4 closes
positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET;
Deviation B flattens at 16:00 ET. State what happens to an open position at
15:00.
**Why frozen.** The plan itself carried the contradiction — the strategy
shortlist recorded the source strategy as EOD-flat while Phase 2 closure and
the Phase 3 spec locked 09:30–11:30 and built breaker #4 around it. The build
resolved it toward the paper without re-scoping the safety layer. Phase 2's
medication-window justification for the 11:30 cut is now unsupported and was
never revisited.
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
**Blocks.** Block 3. Block 4 paper trading.

### F3 — Backtest fill resolution vs. acquired data granularity
**Criterion.** The fill resolution the Strategy Analyzer will actually run at,
and the slippage assumption applied at the band edge, stated in writing before
the backtest runs.
**Why frozen.** The Block 2 spec requires Order Fill Resolution = High with a
1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
delivered 1-minute bars. High-resolution fill modelling needs a finer intrabar
series. A band-touch strategy backtested on 1-minute bars with no intrabar
resolution produces optimistic fills exactly where the edge lives, and the
optimism is invisible in the output.
**Unblocks when.** The assumption is committed and the backtest report carries
it as a stated limitation.
**Blocks.** `4uu`. Everything downstream of `4uu`.

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

---

## OPEN — gradeable now

### O1 — Walk-forward gate set for the replication arm
Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates
and is undefined without an in-sample optimisation step. Deviation D removed
optimisation from the first pass. **Required:** a written statement of which
gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
replication arm or the later optimisation arm.

### O2 — `praxispush` provisioning
The signal directory was specified as a dedicated low-privilege macOS user, the
rationale being structural blast-radius limitation. The build report places it
at `~/praxis-signals/`, surfacing in Windows as `C:\Mac\Home\praxis-signals\` —
the primary account home mounted into the VM. **Required:** either the user
exists, or a DECISIONS.md entry records the removal and its accepted risk.
A security requirement that stopped being mentioned is not a resolved one.

### O3 — Block-1 milestone scope statement
Block 1 was signed off as the signal path proven end-to-end. Deviation G defers
public ingress to Blocks 4–5, untested. **Required:** one line in DECISIONS.md
recording that the Block 1 milestone covers the internal path only.

### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.

---

## Standing criteria — graded on every dispatch

| # | Criterion |
|---|---|
| S1 | Every claim in a report has pasted command output, not a description of output. |
| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
| S3 | Every gate claimed working has been deliberately tripped at least once, with the block observed. |
| S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
| S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation. |
| S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own. |
| S7 | Nothing is committed while any audit box is unchecked. |
| S8 | No question that belongs to Amear is answered on his behalf. |

**S6 is the one that failed.** Six deviations were each approved in isolation
and four downstream components broke without anyone noticing. Every future
deviation gets graded against S6 explicitly, by name, in the report.
