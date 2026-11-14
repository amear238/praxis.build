# PRAXIS — FACTS PACK, 2026-08-06

**Purpose.** Five consecutive `praxis-auditor` dispatches died trying to produce a progress
report, because reading this repo's ledgers exhausts a subagent's budget before it can think.
This file is the extracted evidence, gathered by `praxis-master` via targeted shell commands,
so an assessing agent can reason from data instead of mining 160,000 tokens of ledger.

**Provenance.** Every figure below was produced by a command run by `praxis-master` on
2026-08-06 and is reproducible. This file contains **data, not analysis** — deliberately.

---

## 0. The agent-exhaustion problem (measured)

| File | Size | Rows | Bytes/row |
|---|---|---|---|
| `DECISION_LOG.md` | 198,490 B | 163 | 1,218 |
| `HANDOFF.md` | 100,148 B | 626 | — |
| `DISPATCH_LOG.md` | 90,353 B | 219 | 413 |
| `MANIFEST.md` | 81,688 B | 131 | 623 |
| `STATUS.md` | 74,181 B | 197 | — |
| `ISSUE_REGISTER.md` | 57,039 B | 62 | 920 |
| `DECISIONS.md` | 25,638 B | 243 | — |
| `specs/SPEC_RUBRIC.md` | 20,945 B | 346 | — |
| `AUDIT_LOG.md` | 10,251 B | 92 | — |

Total ≈ **659 KB ≈ 160,000 tokens**. `docs/reports/` holds **92 files / 1.6 MB**.

Five agent deaths, same day, same task family:

| Agent | Tool uses | Tokens | Outcome |
|---|---|---|---|
| Progress report (8 sections) | 47 | 107,969 | died mid-investigation |
| Report A (3 questions) | 47 | 85,610 | died after "Now the state files." |
| Report B (2 questions) | 49 | 93,998 | died after "I'll start by reading…" |
| Report C (2 questions) | 36 | **186,424** | died — token budget, not tool budget |
| Sub-report E (1 subsystem) | 41 | 70,759 | died after "I'll start by reading…" |

Successful dispatches the same day, for contrast: C1 audit 22 tool uses; token mint 11;
`cyd` fix audit 25. Managers completed at 50 and 58 tool uses. **The variable is not brief
size — it is how much ledger the brief causes the agent to read.**

---

## 1. Complete commit history — 115 commits

Counts by month: **2026-05: 9 · 2026-07: 105 · 2026-08: 1**

### The last 12 commits, with dates

```
5067d32 2026-08-06 docs(c1): land session-34/35/36 reports + agent-memory local-only declaration
c1dec30 2026-07-26 chore(flush): AUDIT_LOG row Praxis_build-3fe + proposer/approver schema, cold-amendment rule
e785ca4 2026-07-26 chore(flush): AUDIT_LOG rows lnb+nj1, fun + rubric S12/S9/park-rule
63d7523 2026-07-26 docs(session-33): apply rulings R1-R4
712a997 2026-07-26 v2 stack + agent-spawn-guard (accepted per R1)
b8008e4 2026-07-26 feat(agent-stack): install master/manager/auditor v1 — 5 trip tests + depth-2 nesting proven
7d9be8e 2026-07-25 chore(session-30): close — cross-block audit intake; 4uu frozen behind 5 gates
a42038e 2026-07-25 chore(audit): intake master-agent cross-block audit — 6 collision beads filed
52d6bb6 2026-07-25 chore(4uu): HARD phase-gate — backtest frozen until zyd + fx4 resolve
6c91230 2026-07-25 chore(session-29): close — wx7 report shipped, 852 vm-agent leg proven+closed
27766ad 2026-07-25 chore(852): record VM-agent delegation workspace live-executor leg PROVEN
497088b 2026-07-25 docs(wx7): self-contained build-progress report for the scoping agent
```

### Key timeline facts

- **Last commit touching NinjaScript / strategy code:** `719ab11`, 2026-07-16
  ("paper-faithful NQ Noise-Area breakout NinjaScript strategy").
- **Last commit advancing the trading system in any form:** 2026-07-25.
- **Every commit from 2026-07-26 onward (6 of them) is agent-supervision machinery** —
  agent stack v1/v2, rulings, two `AUDIT_LOG` flushes, and one documentation commit.
- **Gap between `c1dec30` (2026-07-26) and `5067d32` (2026-08-06): 11 days, spanning
  sessions 37, 38, 39, 40 and most of 41 — all of which closed with zero commits.**

---

## 2. Report inventory — 92 files

By month: **2026-05: 4 · 2026-07: 81 · 2026-08: 7**

Tracked in git: **66**. On disk: **92**. → **26 reports exist only in the working tree.**

Reports dated 2026-07-26 or later (the agent-stack era), by subject — all 35 concern
guards, hooks, agent memory, park rules, audit gates or commit composition:

```
2026-07-26  agent-stack-v2-install / v2-triptests / session34-manifest-amendment /
            session34-p0-flush-audit / session35-8sw-audit-round1 /
            session35-8sw-gate-park-conflict / session36-adversarial-actor-hunt /
            session36-agent-key-audit / session36-agent-key-lab /
            session36-agent-key-s9-control / session36-manifest-and-memory /
            session36-null-attack / session36-worker-trigger-probe
2026-07-27  session36-park-rule-escalation / session37-restage-audit /
            session37-restage-split / session38-guard-evasion-test
2026-07-28  session39-agents-dir-write-path / session39-closer-negative-tests /
            session39-dispatch-log-closer{,-adversarial,-build} /
            session39-live-vs-piped-attack / session40-agent-memory-disposition /
            session40-cbf-audit / session40-ignore-and-citation-adversarial /
            session40-memory-correction-adversarial
2026-07-30  session41-cyd-audit / session41-cyd-four-hook-claim /
            session41-cyd-worker1-hook-experiment / session41-cyd-worker2-adversarial
2026-08-03  session41-cyd-fix{,-adversarial,-audit,-worker1}
2026-08-04  session41-c1-citation-markers / session41-c1-false-quote /
            session41-c1-marker-worker1
```

**Zero reports dated after 2026-07-25 concern the trading system.**

---

## 3. Issue tracker (beads) — 36 open, 0 in progress

### All three P0s are supervision bugs, none trading

```
P0  Praxis_build-s8g  Unguarded write path to .claude/agents/ — master-write-guard
                      exempts ALL subagents at line 8; no hook registers on that dir
P0  Praxis_build-hwk  Commit guards evadable: quoting the subcommand defeats the
                      producer/grader separation
P0  Praxis_build-1ys  agent-spawn-guard: worker terminal-layer rule bypassable by
                      omitting subagent_type
```

### P1 — trading system

```
r8j  Import the Phase 3 Build Specification: the nine NUMBERED circuit breakers + their
     placement in the order path, the Block-4 acceptance gate, the BINDING Block-2
     pass-gate set.  [flagged elsewhere as ROOT CAUSE; blocks 2nh/ax4/yra/qtk]
2nh  Live-signal-emission topology + breaker placement in the order path
ax4  Dev-B 16:00 ET session-flat collides with breaker #4 (11:30) + breaker #5 (15:00-18:00)
yra  Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 reconciliation
zyd  Pin the intrabar fill/bar-resolution assumption BEFORE running the 4uu backtest
fx4  MFFU automation-compliance: written confirmation that automation is permitted
zd4  praxispush low-priv user silently dropped — re-provision or log the removal
```

### P1 — supervision

```
y9c  PARKED: restage/C1 commit composition — audit FAIL 2, park rule fired
8sw  Park rule vs commit gate: absolute park rule has no sanctioned commit path
43n  S12: dispatch-log-writeahead.sh has no SubagentStop closer
cbf  Correct false praxis-worker agent-memory in place, then gitignore
cyd  'four Bash hooks' rests on an UNGRADED out-of-repo plugin hook
kgp  gate-commit.sh: quoted-region strip fails on multi-line commands
sk8  S9 registration-field positive control undischarged
```

### P2 — the Block-2 completion chain, all still open

```
zi1  b2-wfa: build + run walk-forward matrix, emit OOS window stats
ajj  b2-mc: Monte Carlo engine on pooled OOS trades
xdr  b2-refdist: generate shm/reference_distributions.json for the Block-3 SHM consumer
qtk  Dev-D no-optimization-first-pass vs WFE>=0.50 gate-set partition
```

Also P2 supervision: `86t`, `c2t`, `nj1`, `lnb`, `37h`, `67b`.

---

## 4. ISSUE_REGISTER — 20 open rows, 9 closed

The most recent open rows, by subject:

```
2026-07-26  Parallel PreToolUse denies mask each other (behavioural constraint)
2026-07-26  tools: Agent(<type>) allowlist NOT ENFORCED on 2.1.220
2026-07-26  agent-frontmatter hooks: SILENTLY IGNORED
2026-07-26  Misfired park commit 599885e on main (later reset)
2026-07-26  Silent-disarm trip-wire: settings 'agent' key resolves to nothing if the
            agent definition is missing; BOTH master guards then stop arming
2026-07-27  Read-only constraint violated by a spawned worker
2026-07-27  Suspected commit-gate bypass (later CONFIRMED as hwk)
2026-07-27  The master cannot write its own persistent memory
2026-07-28  Unguarded write path to .claude/agents/
2026-07-28  The hole was proven and simultaneously exploited by our own agents,
            unreported — two unauthorised /private/tmp/ hooks registered
2026-08-03  The auditor cannot write its own verdict to disk
2026-08-04  Two staged reports quote a sentence their target file does not contain
2026-08-05  gate-commit.sh reports the wrong cause when a token expires
2026-08-05  A denied commit burns the audit token
2026-08-06  The ledgers have outgrown the agents that must read them
```

**Every ISSUE_REGISTER row opened since 2026-07-26 concerns the agent-supervision
machinery. None concerns the trading system.**

---

## 5. The four FROZEN criteria (`specs/SPEC_RUBRIC.md`, verbatim intent)

- **F1 — Signal-path topology vs circuit-breaker placement.** Needs a committed
  `docs/specs/*-live-signal-topology.md` naming what emits the live signal and showing all
  nine breakers upstream of order submission, plus auditor confirmation.
  **Blocks Block 3 entirely, and any SHM threshold derivation.**
- **F2 — Session-flat time vs breakers #4 and #5.** Needs a `DECISIONS.md` entry naming the
  governing rule and the 15:00 disposition, and breaker specs #4/#5 amended to match.
  **Blocks Block 3 and Block 4 paper trading.**
- **F3 — Backtest fill resolution vs data granularity.** Needs the fill-resolution
  assumption committed and carried as a stated limitation in the backtest report.
  **Blocks `4uu` and everything downstream of it.**
- **F4 — MFFU automation compliance.** Needs written confirmation from MFFU that this
  automation pattern is permitted on a funded account. **Owner: Amear. Not a build task —
  an email. Blocks Block 4 and Block 5.**

---

## 6. Phase state

- Block 0 — complete, trader-signed-off 2026-07-09.
- Block 1 — complete, **trader-signed-off 2026-07-15** on evidence audit `d405125`.
- Block 2 (Backtesting) — **active since 2026-07-15, not complete.** `4uu` (the NT8 import +
  compile + Strategy-Analyzer reconcile) is frozen behind five gates and is trader/VM-gated.
  The downstream chain `zi1 → ajj → xdr` has not started.
- Blocks 3, 4, 5, 6 — **not started.** Blocked by F1/F2/F4 and by `r8j`.
- **The nine circuit breakers: specified only. Zero implemented, zero tested** (recorded at
  the 2026-07-25 cross-block audit; `r8j` exists because the Phase 3 spec defining them was
  never imported into this repo).

---

## 7. Verified anchors

```
HEAD                     5067d32 (2026-08-06), == origin/main, 0 ahead
Working tree             39 modified/untracked paths
Reports on disk          92   (66 tracked, 26 untracked)
Open beads               36   (3 P0, 14 P1, 12 P2, 7 P3)
ISSUE_REGISTER           20 open / 9 closed
Claude Code              2.1.220, single binary at /Users/admin/.local/bin/claude
Hook registrations       13, all in-repo
```
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
