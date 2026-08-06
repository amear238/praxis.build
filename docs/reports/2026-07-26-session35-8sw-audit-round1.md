# Audit round 1 — session 35 — `Praxis_build-8sw` forensic report

**Auditor:** praxis-auditor (read-only: Read, Grep, Glob, Bash)
**Graded:** 2026-07-26, session 35
**Artifact graded:** `docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md`
**Staged tree:** `f2a3deeb44854015969a7e76c5e1cdacad7766bd` (auditor confirmed independently)
**Dispatched by:** praxis-master. The producing manager did not see this grader and
could not reach it.

## VERDICT: FAIL — S1, S9

No token minted. `audit-approve.sh` not run. Nothing committed.

The auditor's own summary: *"Substantive finding is sound; evidentiary discipline
is not. The (B) verdict survives my independent re-derivation and survives an
adversarial channel the report never considered. But the report's single most
consequential section (§3.3) — and §2.3, §3.2, §4 — contain zero pasted output,
inside a section that opens by claiming 'Pasted command output only.'"*

---

## Staged-set confirmation (auditor, independent)

```
write-tree   f2a3deeb44854015969a7e76c5e1cdacad7766bd   ← matches producer's assertion
HEAD         c1dec30c6516edcf7c79a78fce5c655e007d7ba2   ← unchanged
name-status  A  docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
numstat      611  0  docs/reports/...
```

Exactly one file, add-only, zero deletions.

## Hard limits — HONOURED

Only `.claude/settings.json` differs (`+"agent": "praxis-master"`), mtime
`17:30:37Z`, ~82 minutes *before* the unit's 18:52:19Z dispatch — Amear's
hand-installed key, not this unit's. No edits to hooks, scripts, rubric, or
agent definitions. `parked/Praxis_build-37h` unmoved at `104c58e` (reflog: 2
entries only). `main` reflog `@{0}` = `c1dec30`. Stash empty. No new branch.

---

## The (B) verdict — independently re-derived, and STRENGTHENED

The auditor confirmed all four of the producer's artifacts first-hand, then closed
a channel the producer left open:

> **`--dangerously-skip-permissions` — the report never mentions it, and I closed
> it against them.** `~/.zsh_history:1494` = `: 1785088326:0;claude
> --dangerously-skip-permissions` → `2026-07-26T17:52:06Z`. The denied session's
> first transcript record is `17:52:07.796Z`. **The session that was denied at
> 18:32:35Z was itself launched with that flag.** The flag demonstrably does not
> disarm `gate-commit.sh`.

It also found a fifth artifact the producer missed — and it is the strongest one,
because it is *inside the repo* rather than outside it:

> **`HANDOFF.md:5`, committed inside `104c58e` itself** — "**Amear commits it by
> hand in his own terminal** — `gate-commit.sh` is a Claude Code PreToolUse hook
> and does NOT bind a human shell."

Consequence: the verdict does not rest on `~/.zsh_history`, which the producer
correctly flagged as not tamper-evident. Four mutually independent artifacts
converge.

**Master's own re-verification, run in-session, not accepted from either agent:**
staged set `A` + `611 0`; `HEAD=c1dec30…`; `PARK=104c58e…`; commit body of
`104c58e` is **empty** (`BODY>>><<<END`) where the denied agent attempt carried a
seven-paragraph body and a `Co-Authored-By` trailer; `~/.zsh_history` line at
epoch `1785091551` == commit `%at`/`%ct`, carrying `git add HANDOFF.md`, a command
present in no transcript; `HANDOFF.md:5` read directly out of `104c58e`.

---

## Per-criterion table (auditor)

| Criterion | Verdict | Evidence / gap |
|---|---|---|
| **S1** — pasted command output, not description | **FAIL** | Fence-to-section map: §2.3, §3.1, §3.2, §3.3, §4, §5, §6, §7, S6 and the Result section carry **zero** pasted output. §3.3 — the most consequential claim in the report — is a bullet list with no rc values, no stderr, no transcript; the auditor had to generate that evidence itself. Aggravated by line 211 asserting "Pasted command output only. Nothing in this section is a description of output" immediately above §2.3, which is entirely description. "Files staged" states the DISPATCH_LOG delta as four rows; it was five. |
| **S2** — no component reported above its evidence | **PASS** | §7 caps every copy-driven result at "the script exited 2," never "the tool call was blocked." §6 lists nine UNVERIFIED items. §6.3 self-corrects "the very same park commit." §6.8 downgrades the transcript gap to corroboration. Nothing in §3.3 or §4 is upgraded. |
| **S3** — every gate claimed working deliberately tripped | **PASS** | `gate-commit.sh` tripped live with the block pasted and re-tripped by the auditor. `no-commit-guard.sh` tripped first-hand during the audit itself (`BLOCKED: subagents leave work staged.`). `gate-manager-output.sh:24` and `agent-spawn-guard.sh:41-43` confirmed at source. |
| **S6** — cross-block check | **PASS** | Dedicated section. Correctly states no deviation was approved, checks collateral anyway against S7, the between-sessions rule, the single-session runbook, S12, S10/S11, Blocks 1–5. The S7 tension it flags is real. |
| **S7** — nothing committed with an unchecked box | **PASS** | HEAD unmoved, no token file, no `audit-approve.sh` invocation, one file staged, zero committed. |
| **S8** — no question of Amear's answered for him | **PASS** | Six options, each with Cost + Weakens, explicit arbitrary-order disclaimer, four questions reserved to Amear. Nearest lean: O1's "the rule would be catching up to practice" is an unmatched supporting note — factually true, does not reach an answer given on his behalf. |
| **S9** — positive control, both halves | **FAIL** | Arming-marker half is genuine and was reproduced by the auditor (armed rc=2 / disarmed rc=0 / invented `orchestrator-activee` rc=0, `cmp` identical to disarmed, differs from armed). The **registration field** has its positive half only; the invented-key negative control is absent. Honestly declared UNVERIFIED, but S9 demands both halves — **and the report asserts the hard limit is total without establishing that no equivalent-position control existed outside the forbidden file.** |
| **S12** — ledger writer ships with its counterpart | **PASS (vacuous)** | Staged change is one report file, zero ledger rows; no writer ships. Named gap: the unit's own execution appended **five uncleared `STATE: dispatched` rows** via the SubagentStart write-ahead hook — a live instance of the standing S12 violation running under the report's feet. |

---

## ⚠️ The finding that outranks 8sw

Not a grading item — a discovery made while the auditor tried to *falsify* §3.3
and failed. Reproduced by the auditor against a byte-identical copy
(`sha256 b3de1137…c330ef`, `cmp` clean) of the live hook:

```
BASELINE plain          rc=2   [Commit denied: no audit PASS token…]
SHAPE brace group       rc=0   []
SHAPE if-then-fi        rc=0   []
SHAPE ! negation        rc=0   []
SHAPE func-then-call    rc=0   []
SHAPE for-loop          rc=0   []
payload=''              rc=0     payload='not json at all'  rc=0
payload='{"tool_input":{'  rc=0  payload='{"foo":"bar"}'    rc=0
```

Root cause visible at `gate-commit.sh:46` — `ANCHOR='(^|[;&|(`])[[:space:]]*'`
admits neither `{` nor the `then`/`do`/`!` keywords, so line 55 `exit 0`s before
line 59 ever reads the arming marker. **The parser fails OPEN, contradicting the
script's own header comments.**

The auditor's falsification attempt made it worse, not better. Its hypothesis was
that `no-commit-guard.sh`, on the same `PreToolUse`/`Bash` matcher, would catch
every admitted shape and render the hole unreachable. Falsified at
`no-commit-guard.sh:16-18`:

```
[ -z "$AGENT" ] && exit 0                                        # ordinary session → untouched
[ "$AGENT" = "praxis-master" ] && [ -z "$AGENT_ID" ] && exit 0   # main-thread master → untouched

ncg, agent_type=praxis-manager, brace group  → rc=2  BLOCKED
ncg, agent_type=praxis-master,  brace group  → rc=0  (no block)
```

**Consequence: the one actor permitted to commit — the main-thread master — is
the one actor for whom both guards fall open on a brace group.** S7's enforcement
is bypassable, today, by the agent it most needs to bind. Scope limit, stated
precisely and not upgraded: these are *script-logic* results from direct
invocation on a byte-identical copy. Whether a live tool call carrying those
shapes completes end-to-end was **not** tested live.

---

## What must change (auditor)

1. §3.3, §4, §3.2, §2.3 carry no pasted output. The rc/stderr/`cmp` results exist
   in `/tmp/praxis-s35-gatelogic/out/` and the worker files; none reached the artifact.
2. Line 211's "Pasted command output only" is false as written.
3. S9's registration control is declared, not discharged; the totality of the
   limit is asserted rather than shown.
4. §1(v) claims the (A)-shaped alternatives were "hunted and came back empty"
   without naming `--dangerously-skip-permissions`, visible two lines above
   evidence the report does quote.
5. "Files staged" DISPATCH_LOG delta is five rows, stated as four.

## Could not verify (auditor)

- Deny-exclusivity at 18:32:35Z — whether a second hook also denied and lost the
  stderr race is not recoverable from the transcript.
- `notify.sh` delivery — POSTs and exits 0 unconditionally, writes no local
  artifact. Whether the `audit-fail-x2` notification reached Amear is
  undeterminable from inside this repo.
- The worker-attributed sweeps in §2.3/§4 (52-case exit vector, token
  replay/expiry) **as executed events** — the logic was reproduced where shapes
  were named, but the full sweeps exist only as prose and as `/tmp` files outside
  the graded diff.

---

## Master's disposition

**Not committed.** Auditor FAIL stands; S7 forbids a commit with any box
unchecked. This is audit FAIL **1** on this unit. Under the ABSOLUTE park rule a
second FAIL on the same bead ends the session with a park — no third dispatch,
no "the defect was mechanical" exemption.

Noted against the master, not the manager: **S9 failed partly because the
master's own brief forbade editing `.claude/settings.json`**, which is the only
place the registration-field negative control can be run. Re-dispatching under
the identical limit would fail S9 again by construction and force a park through
a defective brief rather than through defective work. That is the master's error
to own, and the scope question goes to Amear rather than being resolved here.
