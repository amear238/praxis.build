# Decisions Log — PRAXIS

## Decision 1 — 2026-05-08
**Context:** Project needed version control and remote backup.
**Decision:** Git repo initialized at /Volumes/Sensidine/Praxis.build/, pushed to GitHub as amear238/praxis.build (public).
**Rationale:** Git is the source of truth for code + state files + history. GitHub provides remote backup and is physically downloadable via git clone.
**Impact:** All project files tracked from this point forward.

---

## Decision 2 — 2026-05-08
**Context:** Phase 3 research defaulted to Chicago VPS and Claude API integration.
**Decision:** Local server is the default. Execution is deterministic code — no LLM, no API at order placement. Milestones replace deadlines.
**Rationale:** Trader has equivalent redundancy (UPS, 5G, n8n watchdog). Latency irrelevant for clock-anchored strategy. Education timeline is unknown — deadlines create pressure that feeds behavioral pattern.
**Impact:** Monthly cost reduced by $42-85/month. Full local visibility feeds conviction requirement.

---
---

## D-2026-07-04-A — Build-First Reorder: Comprehension Gate Moved from Pre-Build to Pre-Live

**Date:** 2026-07-04
**Status:** LOCKED (trader-confirmed)
**Supersedes:** Block 1 education-as-prerequisite sequencing in PHASE 3 BUILD SPECIFICATION

**Decision:**
The education track is no longer a prerequisite to the Block 1 build. Claude Code (with the `praxis-build-manager` skill) builds the full Block 1 signal path immediately and runs it on free sim data. The trader learns against the live artifact, not ahead of it.

**The gate does not disappear. It moves:**

> **COMPREHENSION GATE (pre-live, hard):** Block 5 (Graduated Live Deployment) does not open until Amear can explain, unprompted and without reference material, (1) what determines an entry, (2) what determines an exit, and (3) what trips each circuit breaker. Verified in a recorded debrief session with Praxis. Pass/fail. No partial credit.

**Rationale:**
- Two months elapsed (May 8 → July 4) with near-zero progress under education-as-prerequisite. A structure that does not get executed is a failed structure.
- The comprehension requirement exists because of the documented abandonment pattern ("systems he doesn't understand get abandoned"). Paper money does not require conviction to survive a drawdown. Live capital does. Therefore the gate belongs at the paper→live boundary, not the study→build boundary.
- A running system on sim is a superior learning artifact for the trader's neurology than an abstract video queue.

**Named risk (on the record):**
The moment paper trading shows green, "I'll learn it later" will attempt to become "I don't need to." That is the Success-Triggered Relapse mechanism applied to education. The gate above is the pre-commitment against it. It does not loosen on paper performance.

---

## D-2026-07-04-B — Strategy Health Monitor Added (Open Item #7)

**Date:** 2026-07-04
**Status:** LOCKED (trader-confirmed)
**Spec:** STRATEGY_HEALTH_MONITOR_SPEC.md

**Decision:**
A Strategy Health Monitor (SHM) is added to the architecture as a component distinct from the nine circuit breakers (operational safety) and the Block 5 kill criteria (execution failure). The SHM answers one question neither of them asks: **is the edge itself dead or decaying?**

**Core rule:**
Retirement/demotion criteria are quantitative and written **before** deployment, derived from Block 2 walk-forward output. When the SHM fires, the system auto-demotes the strategy to paper. Trader review happens offline, afterward, as research — never as a live judgment call mid-drawdown.

**Rationale:**
"Is the strategy dead or am I just scared" is a discretionary decision that must not be made underwater. Decided in advance, it is engineering. Decided in the moment, it is indistinguishable from the abandonment pattern.

**Sequencing:** Threshold placeholders defined now (see spec). Numeric values locked at the Block 2 milestone, when the walk-forward out-of-sample distribution and Monte Carlo envelope exist. SHM must be live before Block 5 Phase A.

---

## D-2026-07-08-A — Coworker Visibility via GitHub, Not Google Drive Sync (Supersedes Step 0.7 mechanism)

**Date:** 2026-07-08
**Status:** LOCKED (trader-confirmed: "do it if it's better")
**Supersedes:** Step 0.7 "Coworker folder connection (Drive sync)" — the Drive-for-Desktop sync mechanism only, not the underlying goal.

**Decision:**
The coworker gains visibility into build artifacts through **read access on the GitHub repo (amear238/praxis.build)**, not through a Google Drive folder synced to the repo directory. The Drive-sync half of Step 0.7 is dropped.

**Rationale:**
- Git is already the source of truth and is pushed to GitHub every session. Drive-syncing the same files creates a second, drift-prone copy with no history and two tools writing the same paths.
- GitHub read access is less setup than installing/maintaining Drive-for-Desktop, and is always current.
- The Google **Sheets** Build Tracker is retained — it is a genuine progress dashboard (part of the Git→STATUS→Sheets→ClickUp→n8n→Telegram monitoring chain) and is not redundant with git.

**Follow-up (trader action):** provide the coworker's GitHub username (or confirm they already have access) so the read invite can be sent. The empty PRAXIS Drive folder created during 0.7 prep can stay as a scratch area or be deleted — no longer load-bearing.

---

## D-2026-07-09-A — Block 1 Tunnel Technology = Plain WireGuard (over Tailscale)

**Date:** 2026-07-09
**Status:** LOCKED (trader-chosen 2026-07-09)
**Applies to:** Block 1 bead B1-a; resolves Q2 of docs/design/2026-07-08-block1-signal-delivery.md.

**Decision:**
The private encrypted link between the Mac and the n8n host (the transport under Option 1, SCP push) is built with **plain WireGuard**, not Tailscale.

**Rationale:**
- Both options create an identical encrypted peer-to-peer link Mac ⟷ n8n host; the delivery mechanism is unchanged either way.
- WireGuard has **no third-party coordination plane**. Tailscale's control/coordination plane is a third-party cloud service; using it would put a cloud dependency in the signal-execution stack, in tension with the 2026-05-08 rule ("no cloud API in the execution stack"). Plain WireGuard cleanly satisfies that rule.
- Cost is ~20 min more manual key/peer configuration vs Tailscale's automatic coordination. Accepted.

---

## D-2026-07-09-B — NT8 Execution Host = Parallels Windows 11 ARM VM (Now) / Native x64 Windows PC (Before Block 5 Live)

**Date:** 2026-07-09
**Status:** LOCKED (trader-chosen 2026-07-09)
**Aligns with:** D-2026-07-04-A (build-first). Resolves Q3 of docs/design/2026-07-08-block1-signal-delivery.md.

**Decision:**
NinjaTrader 8 (not yet installed anywhere) runs in a **Parallels Windows 11 ARM VM on the Mac Studio** for build-first Block 1 sim work. Validated signals are delivered into a **folder shared into that VM** (the NT8 FileSystemWatcher runs inside Windows, not on native macOS).

**Constraints and gates:**
- The Mac Studio is Apple Silicon; a native Windows partition (Boot Camp) is **not available** on Apple Silicon, so a VM is the only in-place option now.
- NT8 is an x86 .NET application running under emulation inside the ARM VM — this is **UNPROVEN**. Its viability MUST be validated by bead **B1-0** before any downstream Block 1 delivery work proceeds.
- A **dedicated native x64 Windows PC** is a REQUIRED pre-Block-5 hardening step (revisit gate) — the VM is a build/sim expedient, not the live-execution host.

**Impact:** The SCP push target in the Block 1 design becomes the VM shared-folder path; beads B1-b and B1-c reference that shared-folder target rather than a native macOS directory.

---

## D-2026-07-09-C — Signals Drop Dir = Dedicated Low-Privilege User (`praxispush`), Not Trader Home

**Date:** 2026-07-09
**Status:** LOCKED (trader-chosen 2026-07-09)
**Applies to:** B1-a (Praxis_build-dgt) forced-command chroot target; B1-c (Praxis_build-dnt) Parallels VM share scope. Supersedes the resume-card `~/praxis-signals/` (trader-home) placeholder.

**Decision:**
The signal drop directory is owned by a **dedicated low-privilege macOS user `praxispush`** at the canonical path **`/Users/praxispush/praxis-signals`**. This single path is used identically by (1) the B1-a authorized_keys forced-command/rrsync chroot for the n8n push peer, (2) the B1-a sshd scoping, and (3) the B1-c Parallels VM share. It is NOT the trader's home directory.

**Rationale:**
- **Structural least privilege.** A compromised n8n push key reaches a directory that contains nothing but signals — no documents, no repo, no credentials. The trader-home option only stays safe while everything else is configured correctly; the dedicated user is safe even when something is misconfigured. Same logic as the circuit breakers: remove the failure surface, don't rely on correct behavior.
- **Retires the B1-0 finding structurally.** The B1-0 spike accidentally shared the entire Mac home into the VM (`\\psf\Home` / `Z:\`). A dedicated user makes that class of over-exposure impossible to repeat — the share, the SSH chroot, and the forced-command all point at the same signals-only dir.
- **Trivial B1-c share scope.** Share exactly one directory; no judgment call about what else in a home dir is safe to expose.
- **One canonical path across B1-a and B1-c.** No reconciliation drift between beads.

**Impact:** B1-a's `SIGNALS_DIR` = `/Users/praxispush/praxis-signals`; the runbook's dedicated-user assumption is adopted (not the resume-card home-dir placeholder). B1-c creates this user + dir and scopes the Parallels share to it, adding launchd reconciliation. Operator creates the `praxispush` account before the B1-a forced-command step.

---

## D-2026-07-09-D — n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live

**Date:** 2026-07-09
**Status:** LOCKED (trader-chosen 2026-07-09)
**Supersedes the timing/premise of:** D-2026-07-09-A (WireGuard tunnel) and the remote-VPS-n8n assumption in docs/design/2026-07-08-block1-signal-delivery.md (Option 1 = SCP push). Does NOT delete D-2026-07-09-A's WireGuard-over-Tailscale reasoning — it defers the whole remote-host premise those decisions rested on.

**Decision:**
For Block-1 build-first (sim data), **n8n runs locally on the Mac**, not on a remote internet-facing VPS. The signal path is built and proven end-to-end using **test webhook posts** driven locally (as Step 0.8 did against `/tmp`): webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order. The question of how live TradingView (public internet) signals reach the system — **rent a VPS + WireGuard** vs **a tunnel relay (e.g. Cloudflare Tunnel)** — is **deferred to pre-live (Block 4–5)** when live signal ingress is actually exercised.

**Rationale:**
- **Build-first discipline (D-2026-07-04-A).** Block 1 builds the smallest complete path on sim data. Public TradingView ingress is not exercised by sim; standing up a remote VPS + WireGuard now is premature infrastructure — real monthly cost and a public Linux box to secure/patch for a capability the sim phase doesn't use.
- **Removes a failure/attack surface during build.** No internet-facing host, no inbound exposure, nothing to harden yet.
- **Preserves optionality.** Deferring means neither public-ingress design (VPS or tunnel) is locked in prematurely; the choice is made against real requirements at pre-live.
- Trader does not currently own a VPS and is new to operating one; forcing that now adds ongoing ops burden with no build-first payoff.

**Impact:**
- **B1-a (Praxis_build-dgt)** — WireGuard tunnel + scoped SSH is **deferred** (not needed while n8n is local; there is no remote peer to push from). Re-scope pending the pre-live ingress decision.
- **B1-b (Praxis_build-p7s)** — changes from an "n8n SCP-push node over the tunnel" to a **local file-write node** into the signals dir. Re-scoped.
- **B1-c (Praxis_build-dnt)** — still required: the Mac signals dir + Parallels VM-share scope + launchd. Note: D-2026-07-09-C's dedicated-`praxispush`-user choice was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid); whether local n8n writes as `praxispush` vs the trader user is revisited at B1-c execution.
- The Block-1 signal-delivery design doc's remote-push premise is superseded for the sim phase.

---

## D-2026-07-12-A — Signals Relay Moves from launchd WatchPaths to a Persistent KeepAlive Sweep Daemon

**Date:** 2026-07-12
**Status:** DECIDED (orchestrator, evidence-driven; attended session — bead Praxis_build-8xf)

**Decision:**
The outbox→incoming signals relay is re-architected from a launchd **WatchPaths-triggered** job to a **persistent KeepAlive daemon** running a 1s-sleep sweep loop (bead 8xf option b). The existing sweep script logic and stale-heartbeat semantics are reused unchanged; only the launch mechanism changes.

**Rationale (measured, docs/reports/2026-07-12-8xf-latency-investigation.md):**
- launchd enforces a **10s minimum runtime** between WatchPaths respawns (`launchctl print` confirmed; no ThrottleInterval key). Under bursts (6 signals @1.8s) 3/6 deliveries exceeded the <5s target (max 9.15s); even isolated signals hit 7.36s when the throttle window is kept hot.
- Option (a) StartInterval short-poll still collides with the same respawn throttle; option (c) accept-and-document is not viable — throttled delivery is bimodal up to ~10.6s.
- A persistent daemon never respawns per event, so the throttle never applies; relay leg bounded at ~1.3s. If the daemon dies, KeepAlive restarts it (worst case one 10s throttle penalty on crash-loop — acceptable).

**Impact:**
- Deployed plist + installer (internal-disk copy pattern per TCC rule) updated under bead 8xf.
- Separate finding: the n8n Write-node false-failure retry (file lands at +0.15s but n8n retries 2×2s and triple-writes) is **not** blocking after this fix (dedup absorbs it) — filed as its own bug bead; TV-facing HTTP 200 remains delayed ~4s until fixed.
- B1-d's "consistent ~4.3s e2e" is reclassified as a blocking-curl measurement artifact; true unthrottled delivery is ~0.5–1.3s.
