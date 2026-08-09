# Ledger compaction — spec · PROJECT-KIT v0.1 retrofit #1

Status: PROPOSED. Author: praxis-master (session 45). Ratifier: Amear, at the review gate. Source: `ISSUE_REGISTER.md:61`,
under the session-42 maintenance-only ruling. Body ≤60 lines. CONFORMANCE is excluded from the count and is the only place
a conflict may be resolved. Agents propose tags; only Amear ratifies; no agent flips one.

## 1. Context and baseline

743,224 bytes / ~186k tokens across 9 tracked state files — `DECISION_LOG.md` 225 KB, `HANDOFF.md` 122 KB,
`DISPATCH_LOG.md` 113 KB / 275 rows, `MANIFEST.md` 83 KB, `STATUS.md` 77 KB, `ISSUE_REGISTER.md` 66 KB / 35 rows — plus
101 files in `docs/reports/`. The 2026-08-06 figure was 659 KB; it grew 13% while being documented. Terminal rows
archivable today: 50 / 86 / 10. **181 of `DISPATCH_LOG.md`'s 275 rows read `STATE: dispatched`** and are S12 violation 1:
nothing will ever close them.

## 2. Design

### 2.1 STATE.md — the sole spawn-read
Repo root. Contents per template §3 and nothing else: SPEC pointer · F1–F4 one-liners (name, state, unblocking artifact) ·
open bead IDs with one-line summaries · next 3 dispatches · quota and session window. Forbidden: full ledger rows, 5W1H
fields, narrative, resume cards. Every brief cites STATE.md and nothing else from the state layer. With no §3 home of its
own — template gap (b) — compact.sh also regenerates the line `S12: <N> rows abandoned at dispatched` on every run.

### 2.2 compact.sh — deterministic, zero agent tokens
`scripts/compact.sh`, POSIX shell or stdlib Python, run at session close by a human. It registers no hook.
- **Archive** rows whose `STATE:` is CLOSED, RESOLVED or SUPERSEDED out of the three ledgers into `archive/<same-name>`,
  appended in file order and never rewritten.
- **Retain** OPEN, BLOCKED, DEFERRED and IN-PROGRESS as open items. DEFERRED is open; it does not vanish. **DISPATCHED**
  is handled per §2.3.
- **Unknown state is a hard error.** Fail safe toward retention: never archive a row the script cannot classify.
- **Exit nonzero, loudly,** when STATE.md breaches the ceiling. No soft-warning path — failing loud is the enforcement.

### 2.3 DISPATCHED — the boundary is since the last compaction
A `dispatched` row older than the marker is archived as terminal by abandonment: the issuing agent is dead per
kill-after-subtask, so nothing returns to close the row. A row newer than the marker stays open and reaches STATE.md —
in-flight rows are never swept. compact.sh writes the marker at the end of every successful run and reads it at the start
of the next. **First run, no marker present: retain ALL dispatched rows** per D-4's fail-safe toward retention, emit the
counter, and write the marker.

### 2.4 Report archive and dispatch template
All 101 files in `docs/reports/` move to `docs/reports/archive/` except any named in an open bead (18 filenames resolve
from `bd list`; the in-directory subset is computed at run time, not hardcoded). A filename-only index is added to
`MANIFEST.md`. The 26 untracked reports are `git add`-ed in the archive commit — they exist on this disk only.
Separately: leaf agents — workers and auditors — receive pasted context only. They do not read `DECISION_LOG.md`,
`DISPATCH_LOG.md`, `ISSUE_REGISTER.md`, `HANDOFF.md`, `STATUS.md` or `docs/reports/`. Surgical lookups by bead ID are the
master's, pasted into the brief. A convention, not a hook.

## 3. Constraints and acceptance

| # | Constraint | Tag |
|---|---|---|
| K1 | STATE.md ceiling 14,000, byte-only enforcement | [PROPOSED] |
| K2 | Marker path `.claude/state/last-compaction` | [PROPOSED] |
| K3 | Boundary is the last compaction, not session start | [BINDING — DECISION_LOG 2026-08-08T01:20:00Z] |
| K4 | First run with no marker retains every dispatched row | [PROPOSED] |
| K5 | Unknown state is a hard error, biased to retention | [PROPOSED] |
| K6 | Environment subtraction stays DEFERRED (D-7) | [PROPOSED] |

Acceptance: STATE.md within K1 · compact.sh exits nonzero when it is not · Step 3's positive control — one auditor
answering a known-answer question under the new brief format in under 30,000 tokens — is the empirical check on K1.

## CONFORMANCE

Excluded from the body line count. Nothing below is resolved silently.

**C-1 — DEVIATION. Ceiling enforcement changes from tokens to bytes.** Old mechanism: 4,000 tokens. New mechanism:
14,000, byte-only, [PROPOSED]. Rationale in full: tokenizers are model-versioned dependencies and the portfolio spans
providers; a byte count is model-agnostic and deterministic forever; the 4k-token intent lives in the choice of 14,000,
not in the enforcement. Residual carried in the same row: the conversion assumes ~3.5 bytes per token, ID-dense content
tokenizes worse than prose, and Step 3's 30,000-token positive control is the empirical check on the number. Amear
ratifies number and mechanism together, as one item. No silent supersession.

**C-2 — DEVIATION from A2-as-written.** A2 said "current session start"; the spec says the last compaction. Residual,
verbatim: a skipped session merges two windows; rows abandoned in it archive one run late. Supersession trail: Hermes A2
→ session-45 conflict row (no mechanical source exists, and creating one is prohibited) → Amear-approved
compact.sh-marker resolution at `DECISION_LOG` 2026-08-08T01:20:00Z. Legality: the guards inspect the master's command
string only, so writes performed inside a script the master invokes fall outside the hook surface — which is why this
satisfies no-new-hooks while the master's own direct writes stay denied.

**C-3 — EXCEPTION.** Environment subtraction is template default for greenfield but stays DEFERRED for Praxis under D-7
and the moratorium. Conformance exception recorded; P2 bead unchanged.

**C-4 — UNDERDETERMINED.** The brief mandates "three sections" but does not name them. The three above are the author's
partition, not template content. Correct at the gate if the template names different ones.

**C-5 — TEMPLATE GAP (a).** Template §4 carries no rule for the DISPATCHED state. Supplied here by operative A2;
recorded for v0.2, not fixed here.

**C-6 — TEMPLATE GAP (b).** Template §3's STATE.md contents list has no home for the regenerated `S12` counter. Placed in
§2.1 by the author; recorded for v0.2.

**C-7 — TEMPLATE GAP (c), NEW, measured this session.** Suite v3's mode rule flattens with `tr '\n' ' '`, which preserves
a continuation line's indentation. A phrase wrapping into an indented line therefore flattens to *multiple* spaces and a
literal grep still misses it. Measured: the retired literal `abandoned at dispatched` returns 0 both line-wise and
flattened. S45-2 states that flattening alone re-nulls that check — it does not. The mode rule needs whitespace squeezed
(`tr -s ' '`) to hold. C2 and C4 escape this only because their phrases were deliberately kept unwrapped, which is a
property of this author's formatting rather than of the suite.

**C-8 — PROCESS.** This spec was authored by praxis-master, the producing role for this unit. It must be graded by
praxis-auditor, and the master must not self-grade. Recorded because the master normally dispatches rather than authors:
writing to `specs/` is permitted by `master-write-guard.sh:15`, and dispatching a manager to write it would have spent
the tokens the spec exists to save.
