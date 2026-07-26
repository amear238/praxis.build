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
| S12 | A ledger **writer** ships with its **closing or flushing counterpart in the same change**. Anything that appends rows lands together with the mechanism that carries those rows to a terminal state, or into the repo. A writer without its counterpart yields a ledger that only ever grows, whose backlog is then cleared by hand — and hand-clearing is not a mechanism, it is an unfunded obligation on whoever notices. Two existing violations are named below; neither is repaired. |

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

The cost of not doing this is session 33's **three unobserved assertions**. The
orchestrator stated all three about `scripts/agent-spawn-guard.sh` — the one
component the whole producer/grader guarantee rests on — without having observed
any of them. Each was falsified the moment someone looked. *Source: 2026-07-26
human ruling.*

1. *"The guard is registered globally."* — **false. It is project-scoped.** It is
   registered in exactly one place, `.claude/settings.json`; no user-level,
   local, or managed settings file carries a `hooks` key at all. The guard cannot
   fire in any other repo. `docs/agent-spawn-guard.md` §1, behaviourally
   confirmed at T9.
2. *"The guard fails safe — it denies when unsure."* — **false. It fails OPEN.**
   Every branch it cannot positively identify as a forbidden spawn exits 0:
   absent `agent_type`, empty `agent_type`, absent `subagent_type`, malformed
   JSON, empty stdin, non-`Agent` tool. "Fail safe" in its own header means *does
   not break unrelated work* — the opposite reading of the word from the one
   asserted. `docs/agent-spawn-guard.md` §4.
3. *"T6 and T7 both depend on the guard."* — **false. T6 depends on it solely;
   T7 does not depend on it at all.** T7 was fixed by adding `praxis-worker` to
   `praxis-master`'s allowlist (S10 amendment above); the guard's only obligation
   to T7 is not to interfere. `docs/agent-spawn-guard.md` §6.

Note what these three have in common with the config-key failures: **nothing was
broken.** The guard was correctly written and correctly registered. What was
wrong was every statement made *about* it — its scope, its failure direction, and
what depended on it. A component can be sound while the entire account of it is
false, and only the account reaches the next reader.

The general lesson: **a mechanism named in a comment, a brief, or a report is a
claim, and a claim is graded by experiment, not by inspection.** The live
instance of this is `disallowedTools: Agent`, named in
`scripts/agent-spawn-guard.sh:32-33` as the control covering the
omitted-`subagent_type` bypass and never once tested — recorded in
`docs/agent-spawn-guard.md` (header block and §3.1) with the toggle experiment
that would settle it, and tracked as `Praxis_build-1ys` (P0, open).

**S12 — the two existing violations, 2026-07-26 human ruling. Neither is
repaired; both are named so the criterion is not read as hypothetical.**

**Violation 1 — `scripts/dispatch-log-writeahead.sh`.** Registered on
`SubagentStart`, it appends one `DISPATCH_LOG.md` row per spawn, every row
reading `HOW: awaiting terminal state | STATE: dispatched`. **Nothing ever
resolves that wait.** The only `SubagentStop` registration in
`.claude/settings.json` is `scripts/gate-manager-output.sh`, matcher
`^praxis-manager$` — an output gate, not a log closer. The writer shipped; the
closer was never written.

As of this change, 29 rows stand at `STATE: dispatched`. The 16 rows that *do*
carry a terminal state were closed by a **manual reconciliation sweep at
session-31 close** — they read `HOW: reconciled at session-31 close`, which is
the evidence for S12 rather than a counterexample to it. A ledger whose rows
reach a terminal state only when a human happens to sweep it is a ledger that
records dispatch and nothing else.

**Violation 2 — `AUDIT_LOG.md` mint rows.** `audit-approve.sh` appends the PASS
row *after* the staged diff is hashed, so **a change can never contain its own
audit row** — the row is stranded in the working tree by construction. No flush
counterpart shipped with the writer. `Praxis_build-30h` (CLOSED) adopted option
(a), a dedicated flush-mode commit, and that is the sanctioned path — but it is a
*procedure someone must remember*, not a mechanism. Rows have stranded at every
session close since. `Praxis_build-3fe` carries the current flush.

**What S12 asks of the next writer.** Not that flushing be automatic — that a
writer is not accepted as complete until the change that adds it also states, in
committed text, exactly how its rows terminate and who or what performs that
step. Both violations above pass every other criterion in this table. They fail
only this one, and only because the question was never asked at the time.

## Process rulings — binding on the orchestrator

**Park rule — amended to ABSOLUTE, 2026-07-26 human ruling. Supersedes
orchestrator-mine v3's "park it blocked, move on."**

On the **second** audit FAIL for the same bead, with no exceptions and no
orchestrator judgment applied:

1. Commit the work to a branch `parked/<bead-id>`. It does not reach `main`.
2. Fire `.claude/hooks/notify.sh audit-fail-x2 "<bead-id>"`.
3. **End the session.**

**A human resumes it. The orchestrator does not.** There is no third dispatch,
no "the defect was mechanical," no "the fix is two characters." The rule is
absolute precisely because those judgments are the ones an orchestrator is worst
placed to make about its own work — it has already been wrong twice about the
same change by the time the rule fires.

The deviation this amendment responds to is the `DECISION_LOG.md` **17:55Z row**
(2026-07-26, `Praxis_build-fun`), where the orchestrator fired the notification
and then re-dispatched anyway, reasoning that both failures were mechanical and
that parking would strand a human ruling. The auditor concurred. **Both were
wrong, and the ruling overrides both.** That row stands unedited as the record of
the deviation — it is not retro-justified here, and it is not to be softened.

*Note for whoever installs this:* the global skill file
`~/.claude/skills/orchestrator-mine/SKILL.md` still carries the weaker "park it
blocked, move on" wording. It is outside this repository and affects other
projects, so it is **not** edited from here. This section is the binding text for
PRAXIS work.

**Absolutes are amended between sessions only — 2026-07-26 human ruling.**

A rule declared absolute is **never amended inside the session that hits it.**
The sequence when one fires is fixed: **hit the absolute → park → amend cold, by
a human, in a session that is not blocked on the work the rule stopped.**

The reasoning is not new to this project; it is the Strategy Health Monitor's
pre-commitment principle applied to process instead of to thresholds.
`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md` §2:

> All thresholds are written and locked **before** live deployment […] No
> threshold is adjusted while the strategy is in drawdown. Adjustments are
> permitted only: 1. While the strategy is at or above its rolling performance
> baseline, AND 2. Via an append-only entry in DECISIONS.md, AND 3. With a
> mandatory 5-trading-day cooling period between the proposed change and its
> activation.
>
> **Rationale (behavioral):** the decision "is the edge dead or am I scared" is
> never made live.

An agent amending a rule that has just blocked it is in exactly that position.
The judgment "this rule is too strict" and the judgment "this rule is stopping
me right now" are indistinguishable from inside the blocked session, which is
why the SHM never lets the trader make the analogous call mid-drawdown. The cold
session is the cooling period. The park branch is the demotion to paper.

**This applies retrospectively to the park rule itself, which is named here
rather than exempted.** The absolute park rule was written into this file at
`e785ca4` — *in the same session that hit the audit-fail-x2 condition and
deviated from it.* Under the rule above, that amendment should have waited for a
cold session. It was human-issued and it stands, but it is an instance of the
pattern this rule now forbids, and the next such amendment does not get the same
latitude.

**Flush-commit subject lines — `Praxis_build-t83`, approved as convention
2026-07-26.**

A flush commit's subject line names **every bead id whose `AUDIT_LOG` row it
carries**, plus its own bead. Flush mode's prescribed check is that each staged
row maps to a real prior audited change, tested by grepping the log for the
row's bead id — and at `e785ca4` that grep returned nothing for the
`lnb+nj1` row, because the only commit naming those beads was where they were
*filed*, not where the audited work landed. The auditor mapped it by timestamp
window instead. Sound, but by inference, and inference is the thing flush mode
exists to remove.

**`DECISION_LOG` row schema — `PROPOSED BY:` / `APPROVED BY:`, effective
2026-07-26 forward.**

`WHO:` conflated two different roles and is split. Rulings originating with
**Praxis (the claude.ai scoping agent)** record Praxis as `PROPOSED BY:` and
**Amear** as `APPROVED BY:`. Rows written before this date are **not**
retro-edited — the ledger is append-only, and a schema change is not a licence
to rewrite history. Where proposal and approval fall on different dates, both
are recorded.

**What this fix is, and what it is not — read this before relying on it.** It is
a **legibility** fix. It is **not verification, and it is not authentication.**
Nothing prevents an orchestrator from authoring both fields; an agent-written
`APPROVED BY: Amear` is indistinguishable in the file from a real one. The
auditor said as much when it graded `e785ca4` — it could confirm the ruling was
*recorded*, not that it was *given*, since every artifact asserting it was
orchestrator-authored.

**The threat model is drift, not forgery.** The failure this guards against is
the ordinary one: a proposal restated across a few sessions until nobody can say
whether Amear ever approved it or whether it simply survived long enough to look
settled. Splitting the field makes that question answerable by reading. It does
not make the answer trustworthy — for that, the authorisation chain in S4 and
S5 (the ledger append *is* the authorisation) remains the only control, and it
too is a record rather than a proof.
