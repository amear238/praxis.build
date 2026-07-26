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
| S9 | Any config field a guarantee depends on is positive-controlled: confirm a visible script fires at that field, then confirm an invented key at the same position produces byte-identical silence. A field that parses is not a field that is honoured. |
| S10 | `Agent(<type>)` allowlist narrowing is not a scoping mechanism. Honoured on a main thread, discarded on child spawn, where the subagent inherits the spawning parent's roster. Confirmed by control experiment 2026-07-26. Any separation guarantee must be enforced by a registered hook, never by frontmatter or by an allowlist line. **But the inherited roster is load-bearing for reachability** — see the amendment below; the allowlist is dead as a *restriction*, not as a *grant*. |
| S11 | Nesting is depth-capped. Spawned one level deeper, `praxis-manager` receives no `Agent` tool at all; the manager role is unexecutable there. The topology is fixed at master → manager → worker. Do not design for deeper nesting. |

**S6 is the one that failed.** Six deviations were each approved in isolation
and four downstream components broke without anyone noticing. Every future
deviation gets graded against S6 explicitly, by name, in the report.

**S9 was referenced before it was written.** The 2026-07-26 brief carried
"S9 applies to everything in this brief" as a standing rule, but no S9 existed
in this file — the table stopped at S8. The wording above is transcribed from
that brief's own standing rule 5 and is **pending Amear's ratification**; the
criterion was applied in full this session (see `docs/agent-spawn-guard.md` §5).
Reword or renumber it if the intent was different.

**S10 and S11 are permanent constraints, not open issues.** They are recorded
here rather than in `ISSUE_REGISTER.md` because there is nothing to resolve. The
underlying drop defect and its evidence are in `PATCH_NOTES.md` (PN-001).

**S10 amendment — ruling R2, 2026-07-26.** The first reading of S10 was too
broad. The allowlist is discarded as a **restriction on the child**: a spawned
agent's own `Agent(<type>)` line grants it nothing and forbids it nothing, so no
separation guarantee may rest on it. But the **spawning parent's roster is
inherited, and that inheritance is load-bearing for reachability**: an agent type
that appears in **no ancestor's** allowlist is absent from every inherited roster
and is unspawnable outright (`Agent type '<name>' not found.`). The allowlist is
therefore dead as a *restriction* and live as a *grant*.

Two standing consequences:

1. **Do not remove `praxis-worker` from `praxis-master`'s allowlist.** The line
   `tools: Agent(praxis-manager, praxis-auditor, praxis-worker)` in
   `.claude/agents/praxis-master.md` is what makes `manager → worker` spawnable
   at all — the manager inherits it. This is the T7 repair
   (`PATCH_NOTES.md` PN-001, trip-tests T7). Deleting the entry as "dead
   frontmatter per S10" would silently re-break worker dispatch.
2. Conversely, `praxis-manager.md`'s own `tools: Agent(praxis-worker)` line
   **is** inert, and is deliberately left in place — see PN-001, "Not silently
   fixed."

Read S10 as: *frontmatter cannot take a capability away from a child; it can
still be the only thing that puts one within reach.*

**S9 note — ruling R3, 2026-07-26. Positive control extends to claims about
mechanism, not only to config keys.** S9 as written tests a *field*: make the
script fire at it, then show an invented key at the same position produces
byte-identical silence. That is not enough. A claim of the form *"X is covered
by mechanism Y"* gets the same treatment — toggle Y, hold everything else
constant, and show the behaviour changes. If it does not change, Y was never the
mechanism.

The cost of not doing this is session 33's **three-assumption chain**, where each
link was accepted on the strength of the one before it and none was controlled:

1. *"`praxis-worker` cannot spawn, because its `tools:` line omits `Agent`."* —
   **false.** Killed by S10: the child inherits the parent's roster, so omitting
   a type from the child's own line restricts nothing.
2. *"That is fine, because `disallowedTools: Agent` is the worker's own
   control."* — **untested.** Asserted in `scripts/agent-spawn-guard.sh:32-33`
   and never run. It is the same class of field as the one that just failed in
   (1).
3. *"So the guard's omitted-`subagent_type` bypass is a defence-in-depth gap,
   not a hole."* — **rests entirely on (2).** If (2) is inert on a spawned
   child, the terminal-layer rule has no enforcement at all.

Recorded in `docs/agent-spawn-guard.md` (header block and §3.1) and tracked as
`Praxis_build-1ys` (P0, open). The general lesson is the chain, not the
particular field: **a mechanism named in a comment is a claim, and a claim is
graded by experiment, not by inspection.**
