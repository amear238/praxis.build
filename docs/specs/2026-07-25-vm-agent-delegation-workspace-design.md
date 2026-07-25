# VM-Agent Delegation Workspace — Design

**Bead:** Praxis_build-852 (P2)
**Date:** 2026-07-25 (session 28)
**Status:** DESIGN — approved section-by-section via brainstorming (this doc pending Amear's written review before build)
**Author:** Mac Claude Code (orchestrator), brainstormed with Amear

---

## 1. Purpose

Give the Windows-side executor a **single, reusable, task-agnostic delegation workspace**
instead of per-task ad-hoc briefs. The orchestrator (Mac Claude Code) POSTS a delegated
task; the Windows executor PICKS IT UP and executes it; output is graded by the read-only
orchestrator-auditor before anything closes.

This generalizes the existing `~/praxis-signals/b2-data/{outbound/INSTRUCTIONS.md, inbound/}`
mailbox — which is 4uu/Block-2-specific — into a channel that works for **any** VM-hands
task (compile, import, hash-verify, Strategy-Analyzer runs, NT8-reference captures, future
work). It becomes the permanent home for 4uu-style handoffs going forward.

**Verbatim requirement (Amear, session 27):** *"create a directory specifically for the
windows vm agent for all the delegated task for windows vm in claude code. set it up so
there is an ASSIGNMENT AREA for the agent to execute what you delegate."*

---

## 2. Decisions locked (brainstorming Q&A, 2026-07-25)

| # | Decision | Choice |
|---|----------|--------|
| D1 | Concurrency | **Queue that degenerates to a single item.** Numbered assignments; executor claims the lowest-numbered `QUEUED`. Works identically for one task or many. |
| D2 | Lifecycle representation | **Self-contained folder + STATUS field, edited in place.** Nothing moves (robust over the Parallels share; matches the no-session-memory executor). |
| D3 | praxis-tutor seam | **Tutor does NOT write into the workspace.** Only the orchestrator posts assignments. Single write-authority. |
| D4 | Watcher (launchd) | **Deferred** to a follow-up bead. Orchestrator `ls`-checks on boot. |
| D5 | 4uu migration | **Leave 4uu in `b2-data`** (mid-flight, already re-handed). Prove `vm-agent` with a throwaway sample; route NEW tasks here. `b2-data` retires naturally when 4uu closes. |
| D6 | Self-containment (Amear) | The orchestrator must give the Windows executor a **self-contained brief OR all access to the Windows-relevant project info** — so reference material is **staged onto the share** in `reference/`, because the executor cannot open the Mac git repo. |
| D7 | Executor model (Amear) | **Hybrid.** Anything on the Windows end goes to **Claude Code *or* Cowork on the Windows side**, whichever fits. `AGENT-BRIEF.md` is written generically for "the Windows executor agent." |
| D8 | Grading | **Orchestrator-auditor grades every `DONE`** assignment against its embedded acceptance criteria before close. No self-certification. Same discipline as 4uu. |

---

## 3. Location & verified path

- **Mac:** `~/praxis-signals/vm-agent/` (on the Parallels share, outside the git repo).
- **Windows:** `C:\Mac\Home\praxis-signals\vm-agent\`
- **Prefix verified** 2026-07-25: `Test-Path C:\Mac\Home\praxis-signals\b2-data` → `True`
  in the Parallels Windows 11 ARM VM. So `C:\Mac\Home\praxis-signals\` is the correct
  Windows prefix and is baked into `AGENT-BRIEF.md` and every `ASSIGNMENT.md`.
- Being outside the git repo, a Claude Code session running here does **not** violate the
  one-session-per-repo rule (that rule guards the `/Volumes/Sensidine/Praxis.build` working
  tree).

---

## 4. Directory structure

```
vm-agent/
├── AGENT-BRIEF.md            ← Windows executor reads FIRST, every session (standing rules)
├── README.md                 ← orchestrator-facing: how to post / grade / archive
├── TEMPLATE-ASSIGNMENT.md    ← copy-paste skeleton for a new assignment
├── reference/                ← the executor's standing Windows knowledge base (staged)
│   ├── nt8-windows-reference.md      (copy of docs/reference/2026-07-24-nt8-windows-reference.md)
│   └── cowork-agent-delegation.md    (copy of docs/runbooks/2026-07-23-cowork-agent-delegation-brief.md)
├── assignments/
│   └── NNNN-slug/            ← one self-contained folder per task, numbered
│       ├── ASSIGNMENT.md     ← the brief (self-contained; restates the hard limits)
│       ├── STATUS.txt        ← state machine, edited in place
│       └── output/           ← executor drops results here
└── archive/                  ← orchestrator moves closed assignments here after grading
```

---

## 5. Lifecycle & claim protocol

**Claim protocol** (identical for single-task and queue):
1. Executor reads `AGENT-BRIEF.md`.
2. Lists `assignments/`, picks the **lowest-numbered folder whose `STATUS.txt` first line
   is `QUEUED`**.
3. Sets it `CLAIMED` (with a session marker + timestamp), then works it one at a time.
4. Updates `STATUS.txt` as it progresses; writes results into that folder's `output/`.

**Who moves what:** the Windows executor **never moves folders** (flaky over the share) —
it only edits `STATUS.txt` and writes into `output/`. The Mac orchestrator (full
filesystem) is the only mover: it archives to `archive/` after a PASS.

**STATUS.txt format:** first line = a single state token; remaining lines = free-text notes,
timestamp, executor identity (Cowork vs Claude Code), blocker reason if any.

**State machine:**
```
QUEUED → CLAIMED → IN_PROGRESS → DONE        (happy path; DONE = ready to grade)
                        ↓
                     BLOCKED                  (executor hit a live/funded/ambiguous step
                                               or a stop-and-flag condition; reason required)
```
- `QUEUED` — orchestrator posted it, not yet claimed.
- `CLAIMED` — executor has read it and is starting.
- `IN_PROGRESS` — actively working.
- `DONE` — finished; `output/` populated; awaiting orchestrator-auditor grading.
- `BLOCKED` — stopped; needs orchestrator/human. Reason mandatory in the file.

---

## 6. Governing documents

### 6.1 `AGENT-BRIEF.md` (root — read first, every session; the executor has no memory)
1. **What this workspace is** + the real Windows root `C:\Mac\Home\praxis-signals\vm-agent\`.
2. **Claim protocol** (§5): lowest-numbered `QUEUED`, one at a time.
3. **The four hard limits — restated inline, verbatim in spirit from the Cowork runbook,
   un-weakened** (per Amear: self-contained, don't rely on a link the agent may not follow):
   - **Sim/backtest only.** Any live / funded / auto-trade step → set `STATUS=BLOCKED`, stop,
     flag. "Go live" is Amear's alone.
   - **Recompute hashes/checksums yourself — never accept a pasted "already verified" value.**
     Especially before any compile/deploy of order-routing code.
   - **Real Windows paths only** (`C:\...`, `C:\Mac\Home\...`, `%USERPROFILE%\Documents\
     NinjaTrader 8\...`). A sandbox path (`/mnt`, `/home`) will not reach NT8.
   - **No web-fetch workarounds.** Blocked/unfetchable domain = hard stop, not a puzzle to
     route around.
4. **STATUS vocabulary** (§5) + the **output contract**: drop results in `output/`, set `DONE`
   when ready to grade, `BLOCKED` with a reason if stuck.
5. **Executor note (hybrid):** written generically for "the Windows executor agent." Some
   steps are GUI-only (NT8 Import dialog, F5 compile, Strategy Analyzer) — a terminal
   executor (Claude Code) cannot click NT8's WPF GUI and must hand those steps to Cowork
   (computer-use) or Amear; a per-assignment note flags which steps are GUI.
6. **Canonical sources:** `reference/nt8-windows-reference.md`, `reference/cowork-agent-
   delegation.md` (staged copies), plus bd memory `cowork-agent-delegation`.

### 6.2 `README.md` (orchestrator-facing)
- **Post:** `cp -r TEMPLATE-ASSIGNMENT.md` scaffold into `assignments/NNNN-slug/`, fill
  `ASSIGNMENT.md`, create empty `output/`, set `STATUS=QUEUED`, hand the real Windows path
  to the Windows executor.
- **Posting rule (D6, enforceable):** every `ASSIGNMENT.md` must be self-contained and may
  cite only (i) docs staged in `vm-agent/reference/`, or (ii) files inside its own
  assignment folder — **never a Mac-repo path the executor cannot open.**
- **Grade:** when `STATUS=DONE`, dispatch the read-only **orchestrator-auditor** against the
  acceptance criteria embedded in that `ASSIGNMENT.md` + its `output/`. On PASS → archive +
  `bd close`. On FAIL → write defects back into the folder, set `STATUS=QUEUED` (or a fix
  note), re-dispatch.
- **Archive:** on PASS, move the folder to `archive/`.
- **Keep `reference/` current:** when a staged doc changes materially in the repo, re-copy it.

### 6.3 `TEMPLATE-ASSIGNMENT.md`
Copy-paste skeleton with the standard header: assignment ID + title, date posted, the real
Windows path to this folder, sim-vs-live classification, GUI-step flags, the numbered task
steps, the explicit **output contract** (what files to drop in `output/`, what `STATUS`
values to set), and the **acceptance criteria** the auditor will grade against.

---

## 7. Executor model (hybrid)

| Capability | Cowork mode | Claude Code in the Windows VM |
|---|---|---|
| Reach `…\vm-agent\` | connected folder | **native filesystem** |
| Recompute a hash itself | must be told | **native + trivial** |
| Terminal / git / staging | sandbox Linux (separate FS) | **real PowerShell + git on Windows FS** |
| Session memory | none | file/git-backed |
| **Drive NT8's WPF GUI** | **yes (computer-use)** | **no (terminal only)** |

**Split:** Claude Code (Windows) handles the file / hash / data / git half of an assignment
natively; NT8-GUI steps go to Cowork's computer-use or Amear. `AGENT-BRIEF.md` reads
correctly for either; each assignment flags its GUI-only steps.

**Claude Code in the VM — install (Windows 11 ARM, verified via official docs 2026-07-25):**
`irm https://claude.ai/install.ps1 | iex` (native ARM64 supported, no WSL needed). Launch in
the workspace: `cd C:\Mac\Home\praxis-signals\vm-agent` then `claude`. Standing kickoff line
= "read `AGENT-BRIEF.md`, work the lowest-numbered `QUEUED` assignment per its `ASSIGNMENT.md`,
recompute hashes, sim-only → `BLOCKED` on anything live, results to `output/`, set `DONE`."

---

## 8. Relationship to existing structures (non-weakening)

- **`b2-data` mailbox / 4uu:** untouched. 4uu stays there until it closes (D5). No re-pathing
  of an in-flight task.
- **Hard limits:** this workspace is purely a delegation *channel*. It weakens **no** limit
  from CLAUDE.md, the praxis-build-manager skill, or the Cowork runbook. The audit gate
  (orchestrator-auditor grades every `DONE`), the sim-only limit, the recompute-hash rule,
  and the milestone-human-gate all remain in force.
- **bd memory `cowork-agent-delegation`** remains the canonical delegation reference;
  `reference/cowork-agent-delegation.md` is a staged copy for the executor's benefit.

---

## 9. Acceptance criteria (bead 852)

1. `vm-agent/` created on the share with `AGENT-BRIEF.md`, `README.md`,
   `TEMPLATE-ASSIGNMENT.md`, `reference/` (both docs staged), `assignments/`, `archive/`.
2. A documented assignment-area contract (this doc + `README.md`).
3. A sample assignment **round-trips**: posted `QUEUED` → readable by the executor at its
   real Windows path → executor writes `output/` and sets `DONE`.
4. `MANIFEST.md` + `STATUS.md` updated.
5. No existing hard limit weakened.

**Honest split of what ships this session vs. the live leg:** the orchestrator builds the
workspace, stages `reference/`, and posts `0000-sample-roundtrip/` as `QUEUED`, and verifies
the entire **Mac side** (folder on the share → surfaces in Windows; prefix already proven).
The **executor leg** (Cowork or Claude-Code-in-VM actually claiming it, recomputing the hash,
dropping `output/`, setting `DONE`) is proven when Amear next runs a Windows session — it is
NOT faked to PASS. Bead 852 closes on that live round-trip.

### 9.1 Sample assignment `0000-sample-roundtrip/`
A trivial, sim-only proof that touches no NT8 GUI:
> Read `AGENT-BRIEF.md`. Confirm you see this folder at its real Windows path. **Compute**
> the SHA256 of `ASSIGNMENT.md` yourself (proves recompute-not-paste). Write
> `output/roundtrip-ack.txt` containing: the Windows path you see + the hash you computed +
> a one-line "brief understood" acknowledgement. Set `STATUS.txt` to `DONE`.

Exercises every moving part: reads the brief → sees the real path → recomputes a hash →
writes `output/` → sets `DONE`.

---

## 10. Out of scope / follow-ups

- **Watcher (launchd):** deferred → follow-up bead (clone of `b2data-watch` to notify on
  `output/` drops). D4.
- **praxis-tutor writing here:** explicitly out (D3).
- **Migrating 4uu:** out this session (D5); may become the first *real* `vm-agent` assignment
  after it closes in `b2-data`.
- **Auto-close on auditor PASS:** the orchestrator archives + `bd close` manually; no
  automation this session.

---

*End design. Next: Amear reviews this doc → on approval, build `vm-agent/` per §4 + post the
§9.1 sample → hand the kickoff line to the Windows executor for the live round-trip.*
