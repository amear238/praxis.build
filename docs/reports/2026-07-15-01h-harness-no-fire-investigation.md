# 01h — VM T1–T4 Harness No-Fire Investigation (2026-07-15)

**Bead:** Praxis_build-01h (P3 bug) · **Scope:** Mac-side evidence only (no VM access) · **Investigation-only**
**Bug:** Harness "armed" 2026-07-12 in the Win11 Parallels VM to run B1-f T1–T4 unattended when the go-signal
(`praxis-processed-signals.log`) appeared in `~/praxis-signals`. Journal appeared 2026-07-14 15:23 ET; no tests
fired by 15:53; share report stayed the stale 14:41 pre-start "blocked" version.
**Context since filed:** B1-f T1–T4 all subsequently PASSED via Mac-side runs + trader GUI confirmation; Block 1
trader-signed-off 2026-07-15. The harness's mission is complete regardless of this bug.

---

## 1. Evidence inventory (all times ET unless marked Z)

### Share (`~/praxis-signals/`, mtimes from `ls -laT`)

| Artifact | mtime | Relevance |
|---|---|---|
| `b1f-t1-t4-report-2026-07-12.md` | 07-12 12:10:16 | Session-9 VM blocked report (DirectWrite storm). Byte-identical to repo copy `docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md` (verified by `diff`). |
| `BRIEF-2026-07-14-status-check.md` | 07-14 11:01:39 | Mac→VM brief: "confirm your armed harness state: is the phase0 watcher alive (`%TEMP%\praxis-phase0-watch.log` fresh?) … write findings to `STATUS-2026-07-14-reply.md`". **Reply file was never written.** |
| `BRIEF-2026-07-14-coworker-take-over.md` | 07-14 11:19:35 | Mac→VM brief: take GUI control, start consumer, "Task B — run T1–T4 (your harness from 2026-07-12 is armed; reuse it)", T4 restart self-performed. Assumed GUI-control authorization. |
| `b1f-t1-t4-report-2026-07-14.md` | 07-14 14:41:43 | **Last VM coworker write to the share, ever.** Self-identifies "Cowork VM agent (read-only GUI tier — no click/type access to NinjaTrader)". Status BLOCKED; documents DEMO1628771-renamed-to-"sim101" account trap + MNQ-vs-NQ chart mismatch; evidence window ends ~11:22 ET; explicitly states the read-only tier "is a platform-level access restriction that cannot be overridden by the operator". |
| `praxis-processed-signals.log` | created 07-14 15:23 (per ct5 evidence; current mtime 07-15 14:49) | The go-signal. First journal row 2026-07-14T21:05:06Z (17:05 ET), an ACCEPT from the **Mac-side** run. |
| `BRIEF-2026-07-14-reject-reason-request.md` | 07-14 16:05:53 | Mac→VM brief asking for verbatim reject reasons; requested reply `b1f-reject-reasons-2026-07-14.md`. **Never written.** |
| `PraxisSignalConsumer.cs` | 07-14 10:41:10 | Share copy, sha256 `e4581f4a…` (B1-f-era build). Now STALE vs repo `ninjascript/PraxisSignalConsumer.cs` sha256 `8ce01991…` (post-btb 2026-07-15 fix). |
| `processed/`, `rejected/` contents | 07-14 15:57 → 07-15 | All drops trace to Mac-side ct5/qxd runs (per docs/reports/2026-07-14-b1f-t1-t3-mac-run.md). **Zero VM-originated test drops at any time.** |
| `NEEDS-TRADER-T4-RESTART.txt` | **absent** | The harness's T4 handshake file was never created — the harness never reached even T1. |
| Watcher script / harness log | **absent from share** | No watcher script or harness log exists Mac-side. The only named harness state is `%TEMP%\praxis-phase0-watch.log` **inside the VM** (HANDOFF.md session-9 card), unverifiable from the Mac and never confirmed alive by anyone after 07-12. |

### Repo

- `docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md` — the arming session: T1–T4 NOT RUN, NT8 in a
  DirectWrite exception storm; journal "never created — strategy never reached State.Realtime".
- `HANDOFF.md` session-9 card — coworker "re-armed the automated harness: journal-file go-signal → T1–T3
  unattended → NEEDS-TRADER-T4-RESTART.txt handshake → final report"; "VM harness logs:
  `%TEMP%\praxis-phase0-watch.log` in the VM."
- `HANDOFF.md` session-10 card — "journal appearance was the armed harness go-signal → T1–T3 should have run
  unattended", and already notes the fallback used: raise coworker NT8 permission "from read-only to full control".
- `docs/reports/2026-07-14-b1f-t1-t3-mac-run.md` — the Mac-side runs that actually executed T1–T4.

### Timeline (2026-07-14)

| ET | Event | Source |
|---|---|---|
| 10:25–11:17 | Three NT8 restarts in the VM; 4× `PRAXIS-B1f REFUSED` (DEMO1628771 account) | VM 14:41 report (UTC table, VM local ≈ ET-4 not applicable — report mixes UTC/ET; restarts per its own table) |
| 11:01 | Status-check brief posted, asks "is the phase0 watcher alive?" | share mtime |
| 11:19 | Take-over brief posted ("your harness … is armed; reuse it") | share mtime |
| 14:41 | VM coworker writes blocked report — **read-only GUI tier**, evidence ends ~11:22 ET. Last VM write ever. | share mtime + report body |
| 15:23 | Journal created (consumer STARTED on Sim101) — **go-signal live** | ct5 evidence; reject-reason brief ("dirs + journal created 15:23 ET") |
| 15:53 | No tests fired; share report still the 14:41 version — bug filed | 01h bug text |
| 15:56–16:03 | Mac orchestrator drops test signals itself (rejected — geometry/symbol, later fixed) | `rejected/` mtimes |
| 16:05 | Reject-reason brief posted to VM — never answered | share mtime; reply file absent |
| 17:05 | First journal ACCEPT — Mac-side T1 | journal row 21:05:06Z |

---

## 2. Root cause

**Finding: nothing was watching when the go-signal appeared.** The "armed harness" was, at the moment it
mattered, a standing instruction in briefs addressed to a coworker-agent capability that no longer existed:

1. **The arming agent session (07-12) was long gone.** The harness was agent-attention-plus-watcher state
   inside a Cowork VM session from 2026-07-12. Its only persistent trace (`%TEMP%\praxis-phase0-watch.log`)
   lives in volatile VM temp storage; at least three NT8 restarts (and an intervening 2-day gap) preceded the
   go-signal, and no one ever re-verified the watcher after 07-12.
2. **The 07-14 coworker session that could have re-armed it could not, and then ended.** It ran at
   platform-enforced **read-only GUI tier** (its own report, verbatim: "could not click, type, or interact"),
   never answered the direct question "is the phase0 watcher alive?", wrote its blocked report at 14:41 ET, and
   made no share write afterward. The journal appeared 42 minutes later, into a share nobody was watching.
3. **Corroboration:** three consecutive briefs (11:01, 11:19, 16:05) produced exactly one response (14:41),
   and both explicitly-requested reply files (`STATUS-2026-07-14-reply.md`, `b1f-reject-reasons-2026-07-14.md`)
   are absent; `NEEDS-TRADER-T4-RESTART.txt` (the first artifact the harness would emit after T1–T3) was never
   created; zero VM-originated signal drops exist in `processed/` or `rejected/`.

**Confidence: HIGH** that no live watcher/agent existed at 15:23 ET on 07-14 (the non-response pattern is
three-for-three and the harness left no artifact whatsoever). **MODERATE** on the precise sub-mechanism
(agent session ended vs watcher script killed by NT8/VM restart vs watcher never re-armed after the 07-12
storm cleanup vs all of these) — distinguishing them requires `%TEMP%\praxis-phase0-watch.log` inside the VM,
which is out of scope for a Mac-side investigation and now of purely historical value. Additionally, even a
live watcher would likely have been unable to complete the tests: the take-over brief's assumption of GUI
control was wrong (read-only tier), so T4 (NT8 restart) and GUI evidence steps were structurally blocked.

---

## 3. Recommendation: **RETIRE** the VM harness

**Rationale:**

- **Mission complete.** B1-f T1–T4 all PASSED via Mac-side drops + trader GUI confirmation; Block 1 milestone
  trader-signed-off 2026-07-15 (audit d405125). There is nothing left for this harness to do.
- **The replacement pattern is proven.** Mac-side signal drops + trader GUI confirm + on-demand VM coworker
  briefs for read-only trace quoting executed the entire matrix. Any Block-2 / btb sim re-test can reuse it.
- **The architecture is structurally unsound.** It depended on (a) a coworker agent session persisting across
  days, (b) `%TEMP%` state surviving VM/NT8 restarts, and (c) a GUI permission tier that platform policy set to
  read-only. None of these are within our control; "fixing" it means rebuilding it as a persistent VM-side
  service, which no Block-2 need justifies (Block 2 is backtesting — Mac/NT8-strategy-analyzer work, not
  cross-VM GUI automation).
- **Leaving it "armed" is a live hazard, not a neutral state.** The go-signal file now permanently exists; the
  take-over brief still sits on the share instructing any future VM agent to "reuse" the harness and drop T1–T3
  signals unattended. A resurrected watcher or a literal-minded future coworker would place unsolicited sim
  bracket orders. Retirement must therefore be explicit, not passive.

### Retirement checklist — share artifacts to archive/remove (LIST ONLY — nothing deleted by this investigation)

Move to `~/praxis-signals/archive/` (or delete after confirming repo capture):

1. `BRIEF-2026-07-14-coworker-take-over.md` — **highest priority**: contains the standing "harness is armed;
   reuse it" instruction and GUI-control authorization; must not remain visible to future VM agents.
2. `BRIEF-2026-07-14-status-check.md` — obsolete tasking.
3. `BRIEF-2026-07-14-reject-reason-request.md` — obsolete tasking (question answered by Mac-side ct5 work).
4. `b1f-t1-t4-report-2026-07-12.md` — already in repo verbatim (`docs/reports/2026-07-12-b1f-t1-t4-vm-run-blocked.md`, diff-verified identical); safe to remove.
5. `b1f-t1-t4-report-2026-07-14.md` — **capture into repo first** (not yet in `docs/reports/`; its
   DEMO-renamed-to-sim101 and read-only-tier findings are quoted above but the full report deserves archival),
   then remove from share.
6. `PraxisSignalConsumer.cs` (share copy) — stale build (sha `e4581f4a…`) vs repo post-btb source
   (sha `8ce01991…`); repo is source of truth; remove to prevent a future stale re-install.

VM-side (next trader or coworker VM session — cannot be done from the Mac):

7. Kill any surviving phase0 watcher process; delete `%TEMP%\praxis-phase0-watch.log` and any watcher script.
8. Delete any VM-local `NEEDS-TRADER-T4-RESTART.txt` if one exists (none on the share).

Keep as-is: `praxis-processed-signals.log`, `.heartbeat`, `incoming/`, `processed/`, `rejected/`, `logs/`,
`signal-template.json`, `archive/` — all are live production or evidence.

---

*Investigation by Mac-side subagent, 2026-07-15. No share files modified or deleted. No VM access used.*
