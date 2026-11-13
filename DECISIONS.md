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

## 2026-07-15 — Block 1 milestone — trader sign-off
Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15, in-session (AskUserQuestion record) + Google Sheets row (clipboard-delivered). Basis: independent evidence audit docs/reports/2026-07-15-block1-milestone-audit.md (commit d405125) — B1-0/b/c/d/e/f VERIFIED, B1-a verified-as-DEFERRED (D-2026-07-09-D), B1-f T1-T4 all PASS with the standing bracket TRADER-CONFIRMED in the NT8 GUI. Known-open items carried into Block 2 with eyes open: btb P2 (trader chose post-milestone, next-session dispatch), 10i P2, 518/01h/qxd P3, 6h7 P4. Block 2 (Backtesting) entry condition now satisfied.

## 2026-07-15 — D-2026-07-15-A: OnTermination-journaling DECLINED (trader-ratified)
The B1-f consumer deliberately does NOT write journal entries during NT8 strategy termination (OnTermination). Runbook §6.2 recommendation RATIFIED by Amear 2026-07-15. WHY: a journal write during WPF/strategy teardown risks corrupt or partial lines in the at-most-once dedup journal; the restart catch-up scan already re-derives state safely from journal + processed/ dirs (proven by T4 no-replay, 2026-07-15 9:43 restart evidence, commit 5a05a67). Revisit only if a future incident shows signal loss attributable to termination-window drops.

## 2026-07-15 — D-2026-07-15-B: Block-2 spec gaps Q2–Q9 RESOLVED (trader, session 15)
Q1 was closed session 14 (re-implement in NT8, D 21:10Z). The remaining Block-2 scope gaps (docs/specs/2026-07-15-block2-backtesting-scope-proposal.md §5/§6) are now trader-locked via in-session AskUserQuestion (bead Praxis_build-cd4):
- **Q2 exit-milestone:** Adopt §4's 7-item CANDIDATE checklist as the WORKING Block-2 exit definition. Reconcile against the PHASE 3 BUILD SPEC verbatim text if/when that spec is imported; final trader sign-off still human-gated.
- **Q3 WFA gate:** WFE (OOS/IS ratio) ≥ 0.5 is a HARD pass/fail gate for the walk-forward result.
- **Q4 data:** NT8 default-provider MINUTE history — no paid-data budget this block. Depth target ≥4 yrs NQ / ≥12 OOS windows (subject to what the default provider supplies; shortfall to be logged, not silently accepted).
- **Q5 cost model:** $2.96 round-turn commission + 1 tick/side slippage + High fill resolution. Applies to ALL P&L / SHM distributions.
- **Q6 sizing (RoR basis):** MFFU account + trailing-drawdown. P&L held in R-multiples throughout. SUB-INPUT PENDING: exact MFFU account size + trailing-DD limit numbers needed before b2-refdist RoR can compute — captured as a trader-input gap on that bead, not a blocker to b2-data/b2-wfa.
- **Q7 optimize:** OPTIMIZE {lookback, noise multiplier, stop-ATR multiplier, exit policy} inside rolling WFA (252 IS / 63 OOS / 63 step). OOS windows guard against curve-fit. (Larger scope than validation-only, chosen deliberately.)
- **Q8 platform:** BOTH — NT8 Strategy Analyzer (VM) runs WFA + fills; Python (Mac) runs Monte Carlo over the exported OOS trade list. Artifacts archived from both layers.
- **Q9 SHM band form:** FIXED pre-declared bands. SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window. SHM-5: monthly trade count within [0.5×, 2.0×] of backtest mean; breach = 2 consecutive months. (Coarse + transparent chosen over fitted statistical test.)

**Unblocks:** b2-data (Praxis_build-hlw) and b2-wfa (Praxis_build-zi1) now have their data source, cost model, gate, and optimize scope. b2-refdist carries the Q6 numeric sub-input gap.

---

## 2026-07-15 — b2-data (Praxis_build-hlw): cost-model artifact path + roll-convention RECOMMENDATION

**Cost-model config artifact (pointer, not a new decision):** The Q5 cost model already locked in D-2026-07-15-B is now ENCODED in a machine-readable artifact consumed by BOTH the NT8 Strategy Analyzer backtest and the Python Monte Carlo layer: **`config/backtest-cost-model.json`** ($2.96 RT commission, 1 tick/side slippage, High fill resolution, plus NQ tick size 0.25 / point value $20 / tick value $5 metadata). This restates D-2026-07-15-B Q5; it does not change it.

**Roll convention — TRADER-LOCKED 2026-07-15 (session 15):** For the NT8 continuous NQ contract, the roll construction is **volume/OI-crossover roll trigger + Difference (back-adjusted / Panama) adjustment** — Amear locked the b2-data spec recommendation (spec `docs/specs/2026-07-15-b2-data-acquisition-spec.md` §2) via in-session AskUserQuestion. Rationale: a breakout strategy measures signals as absolute point distances, so (a) Difference back-adjustment removes the artificial price gap at each roll seam that would otherwise fabricate breakout signals/fake stop-outs, while preserving true point size; (b) Ratio adjustment is rejected because it distorts absolute point distances (the optimized inputs); (c) volume/OI roll keeps the series on the actually-traded, liquid contract for realistic fills. The VM NT8 pull MUST use exactly this construction. Concrete pull range: NQ 1-min, 2021-07-15 → 2026-07-14 (~5 yr / ~16 OOS windows, clears the ≥4-yr / ≥12-window floor with warmup headroom).

---

## 2026-07-17 — D-2026-07-17-A: hlw continuous NQ series built OUTSIDE NT8 in Python (locked roll convention UNCHANGED)

**Date:** 2026-07-17
**Status:** LOCKED (trader-chosen via AskUserQuestion, session 17)

**Context:** The VM coworker reports the locked roll convention — Vol/OI-crossover trigger + Difference back-adjustment (D-2026-07-15, b2-data §2) — is **not natively constructible** in the current NT8 install (NT8's built-in continuous contract offers Difference back-adjustment but a calendar/expiry roll trigger, not Vol/OI-crossover). Given four paths (NT8 native calendar approximation / NinjaTrader Continuum feed / build outside NT8 in Python / hold), the trader chose **build outside NT8 in Python**.

**Decision:** Construct the continuous NQ 1-min series **outside NT8, in Python (Mac-side, per Q8)**, from individual expiry contracts — exactly reproducing the locked convention (Vol/OI-crossover roll + Difference back-adjustment) — then import the stitched series back into NT8 as a custom instrument for the Strategy-Analyzer WFA. **The 2026-07-15 roll convention itself is UNCHANGED**; this is an implementation-path decision, not a convention change. Trader chose fidelity over the faster NT8-native calendar approximation.

**Method / division of labor:**
- **VM / NT8 (coworker):** export per-contract **1-min OHLCV** + **daily bars (carry volume & open interest)** for each NQ quarterly (H/M/U/Z) whose liquid window overlaps 2021-07-15 → 2026-07-14 (≈06-21 through 09-26, ~20–22 contracts), to `\\Mac\praxis-signals\b2-data\raw\`.
- **Mac / Python (Claude):** compute Vol/OI-crossover roll dates from the daily series, apply Difference back-adjustment across seams, emit the stitched continuous 1-min series + a validation report against b2-data spec §4; re-import to NT8 as a custom instrument.

**OPEN RISK (flagged, not yet decided):** if the free default provider does **not** supply open interest, the roll trigger falls back to **volume-only crossover** — a documented deviation (logged, not silently accepted, per Q4), surfaced to the trader BEFORE any fallback is used.

**Supersedes:** the "VM NT8 native continuous pull" execution assumption in `docs/specs/2026-07-15-b2-data-acquisition-spec.md` §5. That spec's §2 convention and §4 validation criteria stand unchanged.

---

## 2026-07-21 — D-2026-07-21-A: OI_BLANK resolved — volume-only crossover roll trigger AUTHORIZED (resolves D-2026-07-17-A OPEN RISK)

**Date:** 2026-07-21
**Status:** LOCKED (trader-chosen via AskUserQuestion, session 20 — Amear)
**Resolves:** the D-2026-07-17-A OPEN RISK (volume-only fallback), which is hereby CLOSED.
**Bead:** Praxis_build-6hu (P1).

**Context:** NinjaTrader 8 cannot export Open Interest. Confirmed a HARD platform limitation — OI is structurally absent from NT8's futures historical-export schema at every interval/data-type, NOT a config miss (coworker report 2026-07-20). Every landed daily file is 6-col `date;open;high;low;close;volume` with no OI column; the b2data-watch daemon's OI gate fired OI_BLANK on all of them (`~/praxis-signals/b2-data/reports/landing-log.txt`). Therefore "re-export the daily series WITH OI" is IMPOSSIBLE via this toolchain, and the Vol/OI-crossover roll trigger locked in D-2026-07-15 / reproduced in D-2026-07-17-A cannot be computed from NT8 data. Real choice presented to the trader: (A) volume-only crossover fallback, or (B) source daily OI from another provider (heavier, delays Block-2).

**Decision:** The continuous NQ series roll trigger is changed to a **volume-only daily crossover** (roll to the back contract when the back month's daily volume strictly exceeds the front month's, per the tool's confirm-day logic). **The Difference (Panama / back-adjusted) adjustment is UNCHANGED** — it still removes the price gap at each seam so absolute point distances (what the Noise-Area breakout strategy measures) are preserved. This is the ONLY change: OI is dropped from the roll-trigger test; nothing else about the convention moves. Path (B) — sourcing OI elsewhere — was declined in favor of unblocking Block-2 now.

**Rationale / accepted trade-off:** Roll seams may land ~1–2 days from where a true volume+OI crossover would place them, so for ~1–2 days per quarter the series may sit on a marginally-less-liquid contract around the roll. Impact on the strategy is bounded because (a) Difference back-adjustment preserves true point size regardless of the exact seam date, and (b) the seam shift is small relative to the contract's liquid window. Trader accepted this over the delay of sourcing OI from a second provider.

**Scope of change (explicit):**
- The 2026-07-15 roll convention is amended ONLY in its trigger term: `volume/OI-crossover` → `volume-only crossover`. Difference back-adjustment, the pull range (NQ 1-min 2021-07-15 → 2026-07-14), and b2-data spec §4 validation criteria all stand unchanged.
- D-2026-07-17-A's build-outside-NT8-in-Python implementation path is unchanged and now proceeds without the OI dependency.

**Enablement / guardrail (already built):** `scripts/b2_stitch.py` (bead 6bw, c2f674d) was pre-built to REFUSE OI-blank data (exit 2) unless invoked with `--allow-volume-only`, whose file-header contract states the flag may be used ONLY once a DECISIONS append authorizing volume-only exists. **This entry IS that authorization.** The stitch may now be run in volume-only mode; the tool still prints a loud VOLUME-ONLY DEVIATION banner on each such run (deviation logged, not silent — satisfies D-2026-07-15-B Q4). No code change was required.

**Note on prior verbal approval:** the coworker's report that the trader verbally approved volume-only in the VM was NOT sufficient to authorize the change — a roll-convention deviation requires an in-ledger, append-only DECISIONS entry. This entry supplies it; the earlier verbal is now formalized here, not relied upon.

**Unblocks:** Praxis_build-6bw real-data validate+run (in volume-only mode, once raw/ is fully populated) → NT8 re-import → 4uu reconcile → zi1 (WFA) → ajj (MC) → xdr (refdist).

---

## 2026-10-30 — D-2026-10-30-A: F3 backtest fill resolution (CONDITIONAL, void clause live) + band-edge slippage [N] = 2 ticks/side (locked by Amear); amends D-2026-07-15-B Q5 slippage/fill terms

**Date:** 2026-10-30
**Status:** CONDITIONAL — in the form ruled by Amear at DECISION_LOG 2026-08-29T00:10:00Z, void clause live (see below); the commit is Amear's; [N] = 2 ticks/side LOCKED by Amear at 2026-10-30T21:36:30Z, reaffirmed at 2026-10-30T22:22:00Z (WHO: amear).
**Addresses (for audit; not a grade):** rubric F3's written-assumption requirement (`specs/SPEC_RUBRIC.md:45-57`) and bead Praxis_build-zyd acceptance (a)(b)(c). Whether it satisfies F3 — including "before the backtest runs" — is Amear's (NEEDS AMEAR 2).
**Bead:** Praxis_build-zyd (P1).

**Context:** D-2026-07-15-B Q5 locked "1 tick/side slippage + High fill resolution". DECISION_LOG `2026-08-29T00:10:00Z` ruled a conditional form with `[N]` unfilled and a void clause. `2026-08-29T00:35:00Z` recorded that the strategy's order is a market order submitted OnBarClose at a semi-hourly stamp and filled at the next bar's open (INFERRED per 3gm D2(a) `:710`), so the touch-triggered / stop-cluster adverse-selection premise does not apply. `2026-10-30T21:36:30Z` set `[N]` = 2 ticks per side; `2026-10-30T22:22:00Z` (WHO: amear) kept `[N]` at 2 after run 4.

**Decision:**
- **(a) Bar / data resolution:** 1-minute bars of `NQCONT`, the Python-stitched continuous series (volume-only crossover roll + Difference back-adjustment, D-2026-07-17-A / D-2026-07-21-A), END-STAMPED (INFERRED by Claude from the import file's row counts, notes `:25`; Amear's NT8 read of the 9:31/9:32 Opens REPORTED, notes `:23`; bar-time check PASS 2026-10-30, `docs/reports/2026-10-28-voice-session-notes.md:22-27`, a file untracked in git). Import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` (OBSERVED): first row `20210307 180100`, last row `20260720 112700`, 1,857,362 lines. Run-4 range 2021-03-08 → 2026-07-17 (REPORTED). No tick or second series.
- **(b) Intrabar fill assumption:** Strategy Analyzer `Order fill resolution` = **Standard**, set explicitly (explicitness REPORTED BY AMEAR, `2026-10-30T21:36:30Z`; the value OBSERVED on the run-3 screenshot as "Standard (Fastest)", `2026-10-30T22:17:00Z`; REPORTED for run 4). No secondary / 1-tick series. Slippage **2 ticks per side** ($10/side; 4 ticks / $20 round turn) on top of the unchanged $2.96 RT commission = **$22.96 / 4.592 ticks per round turn**. Dollar figures assume NQCONT honours the $20 point value / $5 tick, which 3gm `:949` records as UNVERIFIED. Fill is assumed at the next bar's open after the signal bar — INFERRED, not observed. Whether NT8 applies the 2 ticks on every market fill is UNCONFIRMED (`2026-10-30T22:22:00Z` (WHO: amear)).
- **(c) Why the fill-resolution choice does not decide the checkpoint order logic of this strategy, and where it may still bias the backtest:** the bead's premise ("enters on band-touch … INTRABAR events") does not match the code. `ninjascript/PraxisNoiseAreaBreakout.cs` (sha256 35393823…2752265, commit 719ab11) has six order call sites — `:211` ExitLong("XL",""), `:219` ExitShort("XS",""), `:227` EnterLong(Contracts,"L"), `:229` EnterShort(Contracts,"S"), `:288` ExitLong("FlatEOD",""), `:290` ExitShort("FlatEOD","") — each a managed Enter*/Exit* call with no price argument — plus (`:108`) IsExitOnSessionCloseStrategy = true — platform session-close exit, clock-triggered (INFERRED); no Set*/Submit*/limit/stop call exists; entry and checkpoint-exit decisions (`:211`, `:219`, `:227`, `:229`) are evaluated only at HH:00/HH:30 checkpoint bars (`:196-198`); the FlatEOD exits (`:288`, `:290`) run on any bar with mod >= CloseMod (`:189`), a clock condition, not a price touch. Calculate.OnBarClose is set at `:105` and the decision price is Close[0] at `:200` (code OBSERVED; OnBarClose runtime semantics INFERRED per 3gm Audit-1 §5 `:1164-1173`). Sources: 3gm D3 `:737-773`, Audit-1 §5 `:1164-1173`, §7 `:1185-1207`, D2 `:688-735`. No Set*/Submit*/limit/stop call exists (OBSERVED); assuming the Enter*/Exit* calls are market orders (INFERRED), there is no resting or touch-triggered order, so Standard's intrabar High-vs-Low ordering assumption would not decide, at a checkpoint with a given position state, whether an entry or exit order is sent. That NT8 realises these calls as market orders — and therefore that the Analyzer never needs the intrabar path — is INFERRED. A falsifier for this argument was proposed and is open, not run: the R3 Standard-vs-High control (DECISION_LOG 2026-08-29T00:40:00Z; a High run would also bear on the void clause). Its disposition is Amear's. Contrary hypothesis on record, not resolved: 3gm D4 hypothesis 5 (`:784`, INFERRED) holds that Order fill resolution High vs Standard could change how same-bar exit+reverse pairs and the 16:00 orders resolve. So the fill-resolution choice may still bias how NT8 fills those two cases. Because order decisions read position state (`Position.MarketPosition` at `:201`, `:226`, `:228`, `:287`, `:289`, OBSERVED, 3gm Audit-1 §1 `:1032-1083`), a different resolution of those fills would change later position state and, through it, which later entries fire (3gm `:781`, `:784`, INFERRED — fill resolution is listed among the candidate causes of the run-1 vs run-2 trade-count difference). (c) therefore holds only for the checkpoint decision given a position state, not for the trade set as a whole. This entry does not establish the bead's (c) in full; the R3 control (NEEDS AMEAR 5) is what would settle it. This is NOT a claim that the backtest is unbiased overall. Residual risks that remain. Only the first is a slippage item; the master's note in row 2026-10-30T21:36:30Z (INFERRED from source, pending 3gm) says 2 ticks prices stamp-to-next-open slippage; Amear's own framing (2026-08-29T00:10:00Z) was stop-cluster adverse selection, and 2026-08-29T00:35:00Z surfaced the mismatch without his re-ruling; no row says it prices the others:
  - stamp-to-next-open slippage (not touch adverse selection; `2026-08-29T00:35:00Z`);
  - the 16:00 FlatEOD fill path, whose "next bar" may be the next day's 09:31 (CANNOT-DETERMINE-STATICALLY, INFERRED; 3gm D2(c)) — fill resolution may bear on this (3gm `:784`, INFERRED);
  - same-bar exit+reverse resolution (CANNOT-DETERMINE-STATICALLY, INFERRED) — fill resolution may bear on this (3gm `:784`, INFERRED); early-close days (CANNOT-DETERMINE-STATICALLY, INFERRED).
- **Pre-commitment:** `[N]` was chosen 2026-10-28, before any backtest output existed (REPORTED; first Analyzer run 2026-10-30; rows `2026-08-29T00:10:00Z`, `2026-10-30T21:36:30Z`). A later 3-tick stress run is ALLOWED and does not change the locked number.
- **Void clause (VERBATIM, DECISION_LOG `2026-08-29T00:10:00Z`):** *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold."* **Status:** NOT triggered and NOT retired (`2026-10-30T21:36:30Z`, REPORTED BY AMEAR: Standard was set explicitly in Analyzer template "Praxis Backtest", so the High-with-no-tick-data fallback was never exercised; no run has set High). The clause's trigger is "the VM measurement"; the ledger records only that no run has set High (REPORTED BY AMEAR, 2026-10-30T21:36:30Z). Whether a High run is the trigger is Amear's.
- **Limitation sentence — PROPOSED wording, not ruled by Amear (his ruled requirement is only "Fills are optimistic and the report states so", 2026-08-29T00:10:00Z):** `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`

**Rationale:** Amear's ruling, ledgered. Standard on 1-minute bars was accepted in the `00:10:00Z` conditional; `[N]` = 2 was set by Amear at `21:36:30Z` and reaffirmed at `2026-10-30T22:22:00Z` (WHO: amear). The master does not assert 2 ticks is correct (`21:36:30Z`); this entry does not either.

**Authorisation chain (S5 — the ledger rows are the authorisation):** DECISION_LOG `2026-08-29T00:10:00Z` → `2026-08-29T00:35:00Z` → `2026-08-29T00:40:00Z` (R3 control proposed; open) → `2026-10-30T21:36:00Z` (WHO: amear; intake of the rulings) → `2026-10-30T21:36:30Z` → `2026-10-30T22:22:00Z` (WHO: amear) (`[N]` stays 2) → `2026-10-30T22:28:00Z` (dispatch).

**Config pointer:** this entry IS the DECISIONS.md entry that `config/backtest-cost-model.json`'s `$schema_note` requires for the v1.1.0 number change.

**Scope of change (explicit):**
- `config/backtest-cost-model.json` → v1.1.0: slippage 1 → 2 ticks/side ($5 → $10/side; 2 → 4 ticks / $10 → $20 RT); `fill_resolution` High → Standard; total $12.96 / 2.592 ticks → $22.96 / 4.592 ticks RT.
- Added key `amended: 2026-10-30`; `$schema_note`, `decision_ref`, `fill_resolution_note` and `total_cost_breakdown_note` text updated. No key removed.
- Commission ($2.96 RT), instrument block, `applies_to`, `bead`, `created` unchanged.

**S6 cross-block — consumers and what changes for each:**
- All P&L distributions (NT8 WFA fills + Python Monte Carlo): now carry $22.96 RT.
- R-multiple conversion (Q6): the new $22.96 RT cost is deducted before R normalisation.
- All SHM distributions and threshold derivations (D-2026-07-04-B): derive from the 2-tick base. SHM-4 (`docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:48-51`) includes slippage in its metric; its band numbers live in D-2026-07-15-B Q9 — see NEEDS AMEAR (1).
- Rubric O4 Block-4 gate (`specs/SPEC_RUBRIC.md:94-99`, ±15% win rate / ±25% average trade P&L): compares live to a 2-tick backtest.
- Analyzer template "Praxis Backtest": already at Slippage 2 / Standard (REPORTED); no change.
- Spec text still carrying the superseded Q5 terms (not edited here; superseded on slippage and fill resolution by this entry): `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129` ("High fill res, 1-tick series, 1-tick slippage", attributed there to the Phase 3 Build Spec) and `docs/specs/2026-07-15-b2-data-acquisition-spec.md:53` ("Q5, 1 tick/side" and "the High-resolution intrabar path").
- F4 (MFFU automation compliance): `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` §4 (`:151`) couples MFFU restriction 2 (no automated tools built to exploit sim-environment fill favorability, `:45`) to F3's optimistic-fill failure mode. Named, not resolved; F4's disposition is Amear's.

**NEEDS AMEAR (questions only):**
1. Is SHM-4's "slippage >2 ticks/side worse" band (D-2026-07-15-B Q9) re-read against the new 2-tick base?
2. `[N]` was chosen 2026-10-28 (REPORTED); its first ledger writing is the `2026-10-30T21:36:00Z` (WHO: amear) intake row, restated at `2026-10-30T21:36:30Z`, both after runs 1–3 had run; this entry is written after run 4 (REPORTED). Does that satisfy F3's "stated in writing before the backtest runs"?
3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 2 on every market fill, and what is the unit of the Summary's "Total slippage" cell?
4. Approve or replace the proposed limitation sentence.
5. The R3 Standard-vs-High control proposed at 2026-08-29T00:40:00Z is open. Is it run before F3 is graded, or does (c) stand as INFERRED?
6. Scope of the `[N]` lock (3gm `:949`, reserved for Amear): row `2026-10-30T21:36:30Z` sets `[N]` as band-edge slippage and states it per round trip ($22.96); the Analyzer's Slippage setting applies to every market fill (INFERRED). Was the lock meant to cover session-close and stop-out exits as well?

**Supersedes:** D-2026-07-15-B Q5's "1 tick/side slippage" and "High fill resolution" terms ONLY. Q5's $2.96 round-turn commission and "Applies to ALL P&L / SHM distributions" stand. D-2026-07-15-B's text is not edited.

**Unblocks:** audit of this artifact under Praxis_build-zyd; closure is not decided here (NEEDS AMEAR 5 bears on it). F3's unblock condition also requires the backtest report to carry the assumption as a stated limitation (`specs/SPEC_RUBRIC.md:55-56`); the wording is Amear's (NEEDS AMEAR 4); this entry does not do that.

**Rulings 2026-10-30 (Amear, DECISION_LOG `2026-10-30T23:23:00Z`; answer NEEDS AMEAR 5, 2 and 4 above — appended, nothing above edited):**
- **NEEDS AMEAR 5 → RULED: "Commit conditional + R3 control tomorrow."** This entry is committed as the CONDITIONAL it is. On 2026-10-31 Amear runs the run-4 configuration twice — `Order fill resolution` Standard vs High, every other field held — and compares the trade lists. Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires and (c) is re-decided cold. This adopts the R3 control proposed at DECISION_LOG `2026-08-29T00:40:00Z`. "Rule (c) stands as INFERRED" was offered and not taken.
- **NEEDS AMEAR 2 → RULED: "Yes — the 10-28 notes are the writing."** F3's "stated in writing before the backtest runs" is satisfied by `docs/reports/2026-10-28-voice-session-notes.md` §"Amear's rulings" item 3, a dated written record of `[N]` = 2 preceding every Analyzer run; the DECISION_LOG rows transcribe it.
- **NEEDS AMEAR 4 → RULED: limitation sentence APPROVED as proposed.** Every backtest report carries: `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
- **Still open:** NEEDS AMEAR 1 (SHM-4 band vs the 2-tick base), 3 (slippage unit — bead Praxis_build-o78), 6 (scope of the `[N]` lock over session-close / stop-out exits).
- **Status after these rulings:** CONDITIONAL, committable; bead zyd (c) closes on the 2026-10-31 control result, not on this entry.

---

## 2026-10-31 — D-2026-10-31-A: 7zq scope extension — two Noise-Area backtest variants (OppBand, Flat1559) + one new researched NQ intraday strategy; vol-target variant deliberately NOT built

**Date:** 2026-10-31
**Status:** AUTHORISED by Amear — R-7zq-1, DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear): *"Yes — append it now, then commit."* Appended 2026-10-31 by M3. The third file, PraxisLastHalfHourMomentum, is research-only backtest material (R-7zq-4, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear): *"Research-only backtest material"*). Originally PROPOSED — authorised by DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): *"RULING REVERSED BY AMEAR: 'Run them now and I'll commit in the morning.' Supersedes the 00:41:00Z row's item (1) only: `Praxis_build-7zq` (three backtest .cs files) IS dispatched tonight; commits 2 and 3 remain his, in the morning, unchanged."* Third file, same row: *"Build the top-ranked one (Recommended)"*. Amear may swap after reading the shortlist; he kept #1 as built (R-7zq-3, `2026-10-31T11:45:29Z` (WHO: amear)).
**Addresses (for audit; not a grade):** standing criterion S4 (`specs/SPEC_RUBRIC.md:110`: a DECISIONS.md entry with a traceable authorisation chain for every deviation) for the 7zq scope extension; bead acceptance "a DECISIONS.md entry recording the scope extension … and the two variants".
**Bead:** Praxis_build-7zq (P1).

**Context:** Amear's directive, DECISION_LOG `2026-10-30T22:58:00Z` (WHO: amear): *"put together three separate backtest .cs files using deep research for me to test tomorrow"*. Scope ruled by AskUserQuestion: **"Mix: 2 variants + 1 new"**. Two variants of `PraxisNoiseAreaBreakout` + one NEW NQ intraday strategy chosen from a researched shortlist. The master picked the two variants ("stated so he can swap it"): the OppBand correction (3gm R14) and the 16:00 flat realised inside the session. The vol-target sizing variant was NOT picked, because it would pre-empt Amear's open 3gm Q1. The same row records: no file replaces `PraxisNoiseAreaBreakout.cs`; files are compile-intended only (no NT8 on the Mac); nothing in the unit runs a backtest or touches the walk-forward hold. DECISION_LOG `2026-10-31T00:41:00Z` (WHO: amear) ruled *"Start it not and I'll do them in the morning"* (7zq not dispatched). `2026-10-31T00:46:43Z` reversed that for 7zq only. The new strategy sits outside the Block-2 replication arm, whose gate set is rubric O1 (`specs/SPEC_RUBRIC.md:74-79`).

**Decision:**
- **Variant 1 — `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`, class / strategy name `PraxisNoiseAreaBreakout_OppBand`.**
  - *Why:* 3gm R14, DEVIATION (unauthorised). The base's `OppBand` mode trails at the SAME-side band (`:209`, `:217`; comment `:45`), where the spec says the opposite band (spec L38/L49/L59; paper Table 1 "Stop @ Opp. Band"). This gives Amear test material for his open 3gm Q2. The variant does **not** decide Q2.
  - *Change:* `:209` `: curUpper` → `: (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper)` (long stop = Lower band in OppBand mode) and `:217` `: curLower` → `: (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower)` (short stop = Upper band in OppBand mode). The preceding `double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)` lines (`:208`, `:216`) are byte-identical to the base. So BandOrVWAP mode is unchanged from the base, including its `vwapCumVol == 0` fallback (same-side band). Default `ExitMode = OppBand` in this file (base `:118` defaults to BandOrVWAP).
  - *Non-logic edits (strings and comments):* the `Description` string (base `:101`, a VARIANT sentence appended); `Name` (`:102`); a new variant header block before the base header; the enum-block comments (`:44-46`, re-worded, with the dependency note); the (1) comment (`:204`); the long and short stop comments (`:207`, `:215`); the reversal comment (`:225`, INFERRED / CANNOT-DETERMINE-STATICALLY label appended); the `:118` default's trailing comment; and the `Display` Description of `ExitMode` (`:299`).
  - *Consequence (INFERRED):* the long exit (`Close <= Lower`) coincides with the reversal trigger (`Close < Lower`, `:228`), so OppBand becomes "reverse, or hold to 16:00". A flat-only exit happens only at exact equality. How NT8 resolves the same-bar exit + reverse is CANNOT-DETERMINE-STATICALLY (3gm table rows R12/R21; the reversal readback is 3gm readback R2 (NEEDS AMEAR, `docs/reports/2026-10-30-3gm-fidelity-check.md:850`)). In OppBand mode this co-occurs on every reversal.
- **Variant 2 — `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`, class / strategy name `PraxisNoiseAreaBreakout_Flat1559`.**
  - *Why:* 3gm D2(c), CANNOT-DETERMINE-STATICALLY, scenarios S1–S5. The base's FlatEOD market exit is submitted on the close of the 16:00-stamped bar, which is INFERRED to be the session's last bar (pending 3gm readback R4, template hours; 3gm `:692` "Template hours were never captured"), so its "next bar" may be the next day's 09:31 (INFERRED).
  - *Change:* base `:189` `mod >= CloseMod` → `mod >= FlattenMod`, with a new `private const int FlattenMod = CloseMod - 1; // 959`. The flatten decision fires on the 15:59-stamped bar, so the managed market exit fills at the 16:00 bar's open the same day (INFERRED). `CloseMod` (`:58`) and the checkpoint guard `mod < CloseMod` (`:196`) are unchanged, so the last checkpoint stays 15:30. Default ExitMode unchanged (BandOrVWAP).
  - *Non-logic edits (strings and comments):* the `Description` string (base `:101`, a VARIANT sentence appended); `Name` (`:102`); a new variant header block before the base header; the enum-block comments (`:44-46`, with the dependency note); the trailing comment on the new `FlattenMod` const; the `:108` `IsExitOnSessionCloseStrategy` comment; and the added comment lines above the flatten test (`:188` region).
  - *Consequence:* the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00, INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET.
  - *Limits:* on early-close sessions ending before 15:59 ET the decision logic that day is identical to the base (backstop only; 3gm `:733`/`:842`), but the position/state carried into that day can differ because earlier days flattened differently (INFERRED). For a session-template-aware API (SessionIterator / ActualSessionEnd): no NT8 documentation of SessionIterator behaviour for this use was found; NT-shipped source on disk uses it (e.g. `@StrategyGenerator.cs:1800-1826` in the rescued NT8 folders, per `docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md`), but its behaviour here is UNVERIFIED. So 15:59 is hard-coded.
  - **This variant does not change the governing flat time.** It changes only when the exit order is submitted inside a backtest. Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00, INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET.
- **Both variants:**
  - They drop the `PraxisNoiseExitMode` enum declaration (base `:44-51`) and reuse the base's type, because a second declaration in the same namespace would be CS0101 (INFERRED). So **each variant requires `PraxisNoiseAreaBreakout.cs` to stay installed** in the same NT8 folder.
  - Apart from the class name, the code changes and the string/comment edits listed per variant above (and the enum-declaration removal), everything else is byte-for-byte the base at `719ab11`. The base file is not modified.
- **Third file — one new researched NQ intraday strategy, built in milestone M2:** **`PraxisLastHalfHourMomentum`** (`ninjascript/PraxisLastHalfHourMomentum.cs`, class and strategy name `PraxisLastHalfHourMomentum`), the last-half-hour market intraday momentum timing strategy `η(r_ROD)` of Baltussen, G., Da, Z., Lammers, S. & Martens, M. (2021), "Hedging demand and market intraday momentum", *Journal of Financial Economics* 142, 377–403, DOI 10.1016/j.jfineco.2021.04.029. *Rule:* at the close of the first 1-minute bar in [15:30, 15:59) of a weekday session (normally the 15:30-stamped bar), r = Close(that bar) / Close(most recent 16:00-stamped bar of a prior session) − 1; if r > 0 go long (`LHMomLong`), otherwise, including r = 0, go short (`LHMomShort`); market orders; flatten on the 15:59-stamped bar (`LHFlat1559`, which fills at the 16:00 bar's Open, ≈15:59 price); at most one trade per session; no signal on a Saturday/Sunday bar; sessions with no bar in that window (early close) are not traded; the only input is `Contracts`; compile-intended, not compiled. *Why #1:* it ranked first on the shortlist (`docs/reports/2026-10-31-7zq-m2-shortlist.md`) with a score of **15**, over **#2 TORB** (Tsai et al. 2019, *IEEE Access* 7) at **12** and **#3 5-minute ORB** (Zarattini & Aziz 2023, SSRN 4416622) at **10**. It is the only candidate whose full rule set was read in the primary source, it has zero free parameters, it has NQ-specific published evidence (1996-04-12 → 2020-05-01), and it is the most distinct from Noise-Area (one fixed 15:30 decision; no band, no checkpoint ladder, no VWAP exit). Caveats: the published results are gross of costs (p. 386) and for an equity-futures portfolio, not NQ alone. **Amear may swap to #2 or #3 after reading the shortlist.** The research manager ranks a shortlist of three; #1 is built; Amear may swap in the morning (ruled 2026-10-31: kept — R-7zq-3, see Rulings below), and the other two survive as written specs (`2026-10-31T00:46:43Z`).
- **Deliberately NOT built:** the vol-target sizing variant (paper variant (c)). Building it would pre-empt Amear's open 3gm Q1 (sizing (b) vs (c); `docs/reports/2026-10-30-3gm-fidelity-check.md:857`).
- **Not done by this unit:** no backtest is run and no backtest report is written. Every expected behaviour in the hand-test checklist (`docs/reports/2026-10-31-7zq-handtest-checklist.md`) is INFERRED. Compiling on the VM (F5) is Amear's step.

**Authorisation chain (S5 — the ledger rows are the authorisation):** DECISION_LOG `2026-10-30T22:58:00Z` (WHO: amear; directive + scope "Mix: 2 variants + 1 new") → `2026-10-31T00:41:00Z` (WHO: amear; not dispatched tonight) → `2026-10-31T00:46:43Z` (WHO: amear; reversed: dispatch now; third file = top-ranked) → `2026-10-31T00:49:35Z` (praxis-master; M1 dispatched). The 3gm findings these variants address were audited PASS at `2026-10-30T22:40:00Z` and committed at `4d7ca80`.

**S6 cross-block — touches Block 2 only:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. No live-signal code. The three files are Strategy Analyzer backtest strategies, not `PraxisSignalConsumer.cs` and not on the n8n → file-drop path.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. The governing flat time stays 16:00 ET, and the 15:00 disposition is not addressed. Flat1559 moves only the submission bar of the backtest exit order (15:59 close → 16:00 open fill); it does not name a governing rule. Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00, INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET. DECISION_LOG `2026-10-31T00:49:35Z` asks the auditor to grade this claim.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. No backtest is run or reported. F3 stays FROZEN until a backtest report carries the limitation sentence (`2026-10-31T10:10:15Z`). The hand-test checklist carries that sentence verbatim in its Step 0, but it is not that report.
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. Nothing MFFU-facing; no live or funded account; Sim-only Analyzer use.
- **O1** (`specs/SPEC_RUBRIC.md:74-79`): the new M2 strategy sits outside the replication arm, so O1's gate-set question is not answered or changed. The two variants are test material, not a replacement replication target.
- **O4** (`specs/SPEC_RUBRIC.md:94-99`): the variants run without breakers, like the base. No statement on breaker parity is made.
- **Walk-forward hold:** unchanged (Amear's ruling; `2026-10-30T22:58:00Z` "nothing in this unit … touches the walk-forward hold").

**NEEDS AMEAR (questions only):**
1. **3gm Q2:** should OppBand mean the paper's opposite band in the replication (change base `:209/:217`, keep and rename, or drop)? The OppBand variant does not decide it.
2. **3gm Q1:** sizing (b) vs (c). It is still open; this entry builds no vol-target variant.
3. **Early-close handling:** once the template's early-close rows (3gm R4) and the early-close trades (R6) are read, should a session-aware flat be built, and where?
4. **3gm C3:** if Flat1559 shows same-day 16:00 fills, does the 15:59 decision become how the replication realises the 16:00 flat, or stay a test variant? (It changes "act at the stamp" semantics, 3gm `:866`.)
5. **S4 timing:** row `2026-10-30T22:58:00Z` required this entry "written and staged BEFORE any `.cs` line". Under `2026-10-31T00:46:43Z` the entry was drafted into this file in the same milestone as the .cs files, with the append due before any 7zq commit. Does that arrangement meet his constraint?
6. **Third file:** the M2 pick is #1 of the shortlist by his ruling. The swap stays his after he reads the shortlist.
7. **Flat1559 fill price:** is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of the 16:00 flat, or does he want another mechanism (e.g. a finer secondary series)? Unanswered; no option is recommended. (Checklist B.5a reads it back.)

**Rulings (Amear, 2026-10-31):**
- **R-7zq-1 — S4 ordering (answers NEEDS AMEAR 5 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — append it now, then commit."* The draft-alongside-the-.cs ordering, with the `2026-10-31T00:46:43Z` row as authorisation, satisfies his `2026-10-30T22:58:00Z` "before any .cs" rule; this entry is appended before any 7zq commit.
- **R-7zq-2 — Flat1559 fill (answers NEEDS AMEAR 7 above), DECISION_LOG `2026-10-31T11:04:20Z` (WHO: amear):** *"Yes — test it as built."* The 15:59-bar submission / 16:00-bar-open fill (~15:59 price, flat by 16:00) is accepted as the backtest realisation; the Trades-tab readback decides whether the base's own flat was landing next-day.
- **R-7zq-3 — third file (answers NEEDS AMEAR 6 above), DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Keep #1 (as built)"* — `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021) stands; TORB and ORB remain written specs in the shortlist.
- **R-7zq-4 — breaker #5, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Research-only backtest material"* — tested today; breaker #5 and F2 untouched; any move toward live is a separate decision.
- **R-7zq-5 — 15:59 exit of the third file, DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear):** *"Yes — same ruling"* — R-7zq-2 extends to `PraxisLastHalfHourMomentum`.
- **Still open (NEEDS AMEAR):** 3gm Q1 sizing (b) vs (c) (item 2 above); 3gm Q2, what OppBand means for the base (item 1 above); early-close handling (item 3 above); adoption of the 15:59 decision into the base as the replication's realisation of the 16:00 flat (3gm C3, item 4 above; R-7zq-2 rules the backtest fill of the variant, not this); Step 0, the values for High's extra fields and what counts as "identical" (`docs/reports/2026-10-31-7zq-m1-variants.md:148`; `docs/reports/2026-10-31-7zq-handtest-checklist.md:293`); and, for the third file (M2 addendum §(e), left open by DECISION_LOG `2026-10-31T11:45:29Z` (WHO: amear)): r = 0 → short; the previous-close rule; the missing-15:30 fallback; the 15:30 reference price; the η(r_ONFH, r_ROD) variant; the roll convention. Addendum §(e) item 9 (the first session of the series has no prior close; the design skips it) is not in that row's list and has not been ruled either.
- **Note:** DECISION_LOG line numbers quoted above were taken at draft time and have shifted; row stamps are the stable key. (This entry cites DECISION_LOG by row stamp; its `:NNN` citations point into other files and are left as drafted.)

---

## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)

**Date:** 2026-11-02
**Status:** RULED by Amear — R-VN3-1. Ledger authorisation (S5): DECISION_LOG row `2026-11-02T21:23:45Z` (WHO: amear). Appended 2026-11-02 by praxis-manager, unit `2026-11-02-r-vn3-1-filing`.
**Bead:** Praxis_build-afe (P2). `Praxis_build-7zq`, under which the strategy was built (D-2026-10-31-A, R-7zq-3), is not closed by this entry; whether it closes is Amear's call.

**Ruling (Amear's words, `docs/reports/2026-11-01-voice-session-notes-3.md`):**
- Voice, ~13:17Z (notes-3 line 10): *"So first things first, the strategies that performed the worst. Uh, which was the uh, last half hour. We're gonna scrap that."*
- Chat, ~13:20Z (notes-3 line 11): *"the scrapping of the last half hour ... is going to be added to the repo."*

**Confirmation (ledger paraphrase, not a quote):** notes-3 line 12 recorded the retire-not-delete reading as not yet confirmed. DECISION_LOG `2026-11-02T21:23:45Z` (WHO: amear) records it as confirmed by Amear in his "21:2xZ filing brief": retire, don't delete — the `.cs` file, its trade list and the 11-01 reports stay as the record; the strategy leaves the active candidate set.

**Context:** the 2026-11-01 hand-test run of `PraxisLastHalfHourMomentum`: 1,304 trades, net −$76,009.84, PF 0.84, max DD −$99,806.96 (`docs/reports/2026-11-01-three-strategy-results.md:405`, figures read from Amear's Desktop CSV).

**Decision:**
- `PraxisLastHalfHourMomentum` (Baltussen, Da, Lammers & Martens 2021; third file of D-2026-10-31-A) is **removed from the active candidate set**. What that excludes beyond the removal is not ruled here (see NEEDS AMEAR 3).
- **Retire, not delete.** Nothing is deleted, moved or edited. The record stays:
  - `ninjascript/PraxisLastHalfHourMomentum.cs` (unchanged);
  - the 11-01 reports — every file matching `docs/reports/2026-11-01-*`; those carrying the LHM results are `docs/reports/2026-11-01-three-strategy-results.md`, `docs/reports/2026-11-01-three-strategy-results-manager.md`, `docs/reports/2026-11-01-csv-analyses.md`, `docs/reports/2026-11-01-csv-analyses-manager.md` and `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md`;
  - also kept (filer's addition — the ruling does not name them; nothing is deleted under it either way): the 7zq M2 reports, the nine files matching `docs/reports/2026-10-31-7zq-m2-*`;
  - the trade list `~/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` — **outside the repo**; not copied. Whether it is archived is open (handoff §5 item 8).
- Filer's reading, not a ruling: notes-3 line 10 names only "the last half hour", so the two Noise-Area variants (OppBand, Flat1559) and the baseline are outside this entry.

**S6 cross-block — no block's spec changes:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. FROZEN.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. FROZEN.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. The void clause of D-2026-10-30-A stands.
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. FROZEN.
- No code, template or config changed.

**NEEDS AMEAR (questions only):**
1. Does `Praxis_build-7zq` close now that its third file is retired?
2. Is the Desktop trade list archived into the repo, and where (handoff §5 item 8)?
3. Is `PraxisLastHalfHourMomentum` also out of the R-VN3-2 High fill-resolution preparation, or does it stay in that comparison as a record run?

---

## 2026-11-02 — D-2026-11-02-B: R-VN3-2 — praxis-tickprep source intake into tools/tickprep/ (source only; not run; .exe absent)

**Date:** 2026-11-02
**Status:** RECORDS AN INTAKE. This entry is NOT a ruling by Amear and authorises nothing. The intake was asked for in Amear's filing brief, recorded by the master at DECISION_LOG `2026-11-02T21:23:45Z` (WHO: praxis-master, "FILING BRIEF (four items)", item 3) and dispatched at DECISION_LOG `2026-11-02T21:38:24Z` (WHO: praxis-master); R-VN3-2 itself is DECISION_LOG `2026-11-02T21:23:45Z` (WHO: amear). None of these rows authorises a purchase, an NT8 import, a run, or adding the `.exe` files. Appended 2026-11-02 by praxis-manager, unit `2026-11-02-tickprep-intake`.
**Ruling it serves:** R-VN3-2 (`docs/reports/2026-11-01-voice-session-notes-3.md` line 16): *"It does not authorize a purchase, an import or a run."*

**Evidence grades used below:** OBSERVED (seen by this unit on this Mac, 2026-11-02) / INFERRED (reasoned, not checked) / REPORTED BY AMEAR / REPORTED BY the VM agent (the agent that wrote the tool on the Windows VM) / UNVERIFIED (not checked by anyone on record).

**a. Provenance chain:**
1. Windows VM, where an agent wrote the tool — REPORTED BY the VM agent (README line 5: *"Belongs in the Praxis.build repo; copied here 2026-11-02 because the repo wasn't reachable from the VM."*) and REPORTED BY AMEAR.
2. Google Drive folder id `1YaM4I3BKt_nNKWdUnOkj4kJzCeBEwLe_`, uploaded by an agent on Amear's side — REPORTED BY AMEAR. Not opened by this unit.
3. Downloaded to `~/Downloads/drive-download-20261102T213740Z-1-001/` — by Amear, REPORTED BY AMEAR (DECISION_LOG `2026-11-02T21:38:24Z`: *"it int he downloads"*). OBSERVED: the folder exists and holds exactly four files, `MakeSynth.cs` (3,732 bytes), `README.md` (2,219), `TickPrep.cs` (18,785), `nt-implied-offsets.csv` (645).
4. Copied by this unit (`cp -p`) to `tools/tickprep/` — OBSERVED: `cmp` of each download file against its repo copy printed nothing, exit 0, for all four.

**b. Hashes (sha256, OBSERVED, hashed in the repo 2026-11-02; each equals the download-side hash):**
- `tools/tickprep/MakeSynth.cs` — `398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507`
- `tools/tickprep/README.md` — `81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5`
- `tools/tickprep/TickPrep.cs` — `104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545`
- `tools/tickprep/nt-implied-offsets.csv` — `69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9`
- `tools/tickprep/SHA256SUMS` (generated in the repo by this unit from the four lines above, relative names; `shasum -a 256 -c SHA256SUMS` passes) — `5aca84487edd132089914674e6713699aa8184646d854a84b15d5fc9b7542b5f`
- Zip `~/Downloads/drive-download-20261102T213740Z-1-001.zip` — `78e386891faa7f32ddec3c2f330f24978ed394fed95a99fb6acffa6166fa09f2` (OBSERVED, re-hashed by this unit). The zip was not extracted to disk. Its member list (`unzip -l`: the same four names and sizes) and the sha256 of each member read to stdout (`unzip -p <zip> <member> | shasum -a 256`) equal the folder's four hashes above (OBSERVED, re-run by the manager 2026-11-02).

**c. VM-side originals — UNVERIFIED.** No VM-side hash of any of the four files is on record. The master's dispatch brief states they were never hashed on the VM; DECISION_LOG `2026-11-02T21:36:22Z` says the VM-side sha256 of the `.exe`s and of the original CSV *"are not obtainable here"*. Neither statement is verified by this unit. That the Mac copies equal the VM files cannot be shown from this side. The hashes of `TickPrep.exe` and `MakeSynth.exe` are unknown.

**d. Line endings of `nt-implied-offsets.csv`:**
- REPORTED BY AMEAR: the `.cs` sizes equal the VM copies; `nt-implied-offsets.csv` is *"24 bytes smaller than the Desktop copy because of line endings; the contents are the same"*.
- OBSERVED (repo copy): `file` prints `CSV text` (no CRLF terminators reported); `wc -l` prints 24; `wc -c` prints 645; the file contains 0 CR bytes (`tr -cd '\r' | wc -c` → 0).
- INFERRED (arithmetic only, the Desktop copy was not checked): 24 lines × 1 CR byte = 24 bytes, CONSISTENT with a CRLF→LF conversion somewhere between the VM Desktop and this Mac.
- Consequence: by Amear's own report the repo csv is NOT byte-identical to the VM Desktop copy. Its hash in (b) identifies the LF copy only.

**e. `.exe` status:** `TickPrep.exe` and `MakeSynth.exe` are ABSENT — OBSERVED (not in the download folder, not in the repo). Not uploaded — REPORTED BY AMEAR: retyping ~39,000 encoded characters by hand was judged unsafe. README line 8 and line 9 list both `.exe` files as part of the tool. README line 32 (verbatim, `sed -n 32p`):
`` `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /optimize+ /out:TickPrep.exe TickPrep.cs` ``
That is the only rebuild command in the README; it builds `TickPrep.exe` only. No command for `MakeSynth.exe` is given (OBSERVED from the README, 32 lines). Nothing was compiled by this unit.

**f. What the tool is for** — the author's description, REPORTED BY the VM agent; the summary of what the code does is INFERRED from a source read. NOT tested, not compiled, not run.
- README line 3: *"This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C)."*
- README line 4: *"It doesn't touch NinjaTrader. It reads the tick files and the 1-min file and writes only to the output paths you give it."*
- `TickPrep.cs` lines 1–2: *"TickPrep: match per-contract NQ tick files to a back-adjusted 1-minute file, then / write one adjusted tick file that reproduces those minute bars exactly."*
- `TickPrep.cs` lines 5, 9, 13 name three commands: `measure <minuteFile> <contracts.csv> <outDir> [--tz-in Eastern|UTC]`, `build   <minuteFile> <contracts.csv> <outDir> <outTickFile> [--tz-in ...]`, `verify  <minuteFile> <tickFile>`. Lines 6–8: measure *"finds each contract's additive / offset, and assigns every minute of <minuteFile> to the contract + offset that / reproduces it."* Lines 10–12: build is *"Strict: ticks in minutes that are / missing from <minuteFile> are NOT written (holes/gaps stay as they are)."* Line 14: verify *"Rebuilds 1-min bars from <tickFile> and compares them with <minuteFile>."*
- `TickPrep.cs` line 20: *"Read-only on inputs; writes only into <outDir> and <outTickFile>."*
- `MakeSynth.cs` line 1: *"Test helper: make fake per-contract tick files from a back-adjusted minute file."*

**g. NT-touch / write-path grading (greps run on the repo copies, OBSERVED):**
- `/usr/bin/grep -n -i "ninjatrader\|sqlite\|Documents\|AppData\|Registry\|Process\.\|Environment\.\|WebClient\|Http\|Socket\|Delete(\|Move(" TickPrep.cs MakeSynth.cs` → exactly two hits, `TickPrep.cs:17` and `TickPrep.cs:18`, both comments naming the NinjaTrader text format (*"Minute file: NinjaTrader minute format, ..."*, *"Tick files:  NinjaTrader tick format: ..."*).
- `/usr/bin/grep -n "File\.\(Create\|Write\|Open\|AppendAll\|Copy\)\|new StreamWriter\|new FileStream\|Directory\.\|Path\.Combine" TickPrep.cs MakeSynth.cs` → TickPrep: `:177` `Directory.CreateDirectory(outDir)`; `:276`, `:277`, `:280` `File.WriteAllText(Path.Combine(outDir, ...))` for report.txt, segments.csv, offsets.csv; `:281` `File.Create(Path.Combine(outDir, "assign.bin"))`; `:297` `File.OpenRead(... "assign.bin")` (a read); `:316` `new StreamWriter(outTickFile, false, ...)`. MakeSynth: `:35` `string path = Path.Combine(a[1], c.Item1 + ".Last.txt");` and `:36` `using (var w = new StreamWriter(path, false, new UTF8Encoding(false)))`; `:59` `File.WriteAllText(Path.Combine(a[1], "contracts.csv"), ...)`. Writes go only under `outDir` / `outTickFile` (TickPrep) and `a[1]` (MakeSynth).
- `TickPrep.cs:309`: *"if (File.Exists(outTickFile)) throw new IOException("output exists, refusing to overwrite: " + outTickFile);"* — the overwrite refusal covers `outTickFile` only. OBSERVED in source: the measure outputs in `outDir` (`:276`–`:281`) and MakeSynth's outputs (`:36`, `:59`) have no such guard.
- Grade of the README line-4 claim (*"It doesn't touch NinjaTrader ... writes only to the output paths you give it"*): consistent with the source read — INFERRED, not tested. The greps match listed patterns only; they do not prove that no other I/O API is used.
- README line 10: the offsets came from *"NinjaTrader's NQ rollover table (copy of `NinjaTrader.sqlite`, read 2026-10-31)"* — REPORTED BY the VM agent. A read of a copy, not an import. Not verifiable from here.

**h. R-VN3-2 limits — status:**
- README line 3: *"This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C)."*
- README line 13: *"## Use (after Amear approves and buys the data)"*
- README line 23: *"Any import into NinjaTrader is a separate step, and it needs Amear's OK."*
- README lines 25–29: *"## Self-test result (2026-11-02)"* / *"- Test data: fake H21/M21/U21 contracts, 2021-03-07 to 2021-06-21. The window spans the DST change and the cut-short 2021-06-10 roll."* / *"- Offsets recovered exactly: 3400 / 3390.25 / 3380.5."* / *"- All 99,705 rebuilt bars matched the file, with none missing or extra."* / *"- UTC-stamped input gave the same result as Eastern."*
- `TickPrep.cs` header (lines 1–20) does not mention Portara, buying data or importing into NT8 (OBSERVED).
- Status (OBSERVED from the four files): nothing in the folder records a purchase — README line 13 presupposes one *"after Amear approves and buys the data"*. Nothing records an NT8 import — README line 23 says that is a separate step needing Amear's OK. Nothing records a run on purchased Portara tick data. The one run the folder records is the VM-side self-test (next bullet), and its 1-min input file is not identified.
- The self-test (README lines 25–29) is a VM-side run — REPORTED BY the VM agent; not reproduced here. Per README line 26 the *contracts* (the per-contract tick files) were fake. Per README line 9 and `MakeSynth.cs` line 26 (`foreach (var line in File.ReadLines(a[0]))`, the minute file given on the command line) they were generated from "the 1-min file". Whether that minute file was real market data is UNVERIFIED (README line 11 ties the offsets to NinjaTrader's back-adjusted `NQ ##-##`). The offsets it reports (3400 / 3390.25 / 3380.5) match the constants hard-coded in `MakeSynth.cs` lines 21–23 (`3400.00m`, `3390.25m`, `3380.50m`; OBSERVED in source). That shows consistency, not that the run happened. The README does not say which 1-min file the self-test used (OBSERVED).
- R-VN3-2's text (notes-3 line 16): *"It does not authorize a purchase, an import or a run."* Whether the VM self-test counts as a "run" under that line is NOT for this entry to decide (NEEDS AMEAR 3).

**S6 cross-block — no block's spec changes:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. FROZEN.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. FROZEN.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. The void clause of D-2026-10-30-A stands.
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. FROZEN.
- No code, template or config changed; `tools/tickprep/` is new source, not built, not wired to anything.

**NEEDS AMEAR (questions only):**
1. `.exe` ruling: source only with the rebuild steps, or the binaries too? If binaries: how do they reach this repo (the hand-retyping route was judged unsafe), and who hashes them on the VM so the repo copy can be checked against the original?
2. Is the Portara data purchase that README line 13 presupposes authorised? (R-VN3-2 does not authorise a purchase.)
3. The VM-side self-test (README lines 25–29) ran the tool on synthetic tick files built from an unidentified 1-min file. Does it count as a "run" under R-VN3-2, and is its result accepted as reported or to be re-run under approval?
4. Should the VM-side originals (the four files and both `.exe`) be hashed on the VM to close the UNVERIFIED link in the provenance chain?
5. `nt-implied-offsets.csv`: is the LF repo copy the canonical one, given Amear reports that the Desktop/VM copy differs by line endings?
6. `--offsets` FORCES offsets. `TickPrep.cs` lines 45–55 parse it before the command switch (line 45: *"int fo = a.IndexOf("--offsets");   // optional CSV contract,offset_points to force offsets"*; line 52: *"forced[p[0].Trim()] = (long)(decimal.Parse(p[1], Inv) * 4m);"*). In measure, line 212: *"if (forced.ContainsKey(contracts[k].Key)) { chosen = forced[contracts[k].Key]; why = "FORCED by --offsets"; }"* — for every contract whose `contracts.csv` name equals a CSV `contract` value exactly (both sides `Trim()`med, lines 52 and 169; the `forced` dictionary at line 34 uses the default, case-sensitive comparer), the measured longest-run offset is replaced by the CSV value. A contract with no exact match keeps its measured offset; that is not an error, and its report.txt line shows `[longest run]` instead of `[FORCED by --offsets]` (INFERRED from the source read). That value is then used to assign minutes (line 236), written to `offsets.csv` (lines 278–280) and `assign.bin` (lines 281–286), which build reads (lines 297–305). README line 15 passes `[--offsets nt-implied-offsets.csv]` to `measure`; README line 17 says *"Check that the offsets match `nt-implied-offsets.csv`"*. With `--offsets`, the offsets written for listed contracts equal the CSV by construction (INFERRED from the source read); report.txt prints the exact-minute count and longest run for the chosen offset, i.e. the forced one when forcing applies; the measured winner then appears only as the "next best" entry, and only when more than one offset was measured — with one, "next best" prints `none` and the measured winner does not appear (lines 214–218). `--offsets` is not in the header's command list (lines 5, 9). Should `measure` be run with or without forced offsets when the time comes?
7. README line 3 says *"`NQCONTROW 09-25` (High fill resolution, option C)"*. Which option list is "option C" from? A case-insensitive search (`/usr/bin/grep -rn -i "option C" docs/reports/*.md`) finds three candidate meanings, none confirmed as the README's: `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:175` *"Option C (measured haircut from a tick sample)"* (a fill-resolution option, in an UNGRADED report); `docs/reports/2026-07-15-b2-q1-strategy-exportability.md:42` *"Phase 3 spec Block 2 Option C"* (a data-sourcing option); and the Kinetick connection option C in `docs/reports/2026-10-20-a20-kinetick-research.md` (line 127, *"C. Connect at startup"*). The VM agent's R-VN3-2 plan file is absent from this Mac (DECISION_LOG `2026-11-02T21:38:24Z`). The label is unresolved here.
8. Which 1-min file is the input to `measure` / `build` / `verify`? README line 11 is conditional (*"If the 1-min file is NinjaTrader's back-adjusted `NQ ##-##`, the offsets the tool measures should equal these."*). And which 1-min file did the VM self-test use?
9. `verify` exits 0 when no price differs and no extra bars exist. Minute-file bars with no ticks are printed (`TickPrep.cs` line 355) but do not change the exit code (line 357: `return priceDiff == 0 && extra == 0 ? 0 : 3;`) — INFERRED from the source read; not compiled or run. How many unmatched or missing minutes are acceptable before the output is used?
10. Is `tools/tickprep/` the path Amear wants? The brief asked for a proposed path; this unit proposed it and copied the files there.

---

## 2026-11-02 — D-2026-11-02-C: R-VN3-3 to R-VN3-6 — data used as is; Flat1559 exit accepted; backtest with breakers on once built (O4, agent's reading confirmed in voice only); judge the version closest to live (O1)

**Date:** 2026-11-02
**Status:** RULED by Amear — R-VN3-3..6, ledger authorisation DECISION_LOG `2026-11-02T21:54:14Z` (WHO: amear). Appended 2026-11-02 by praxis-manager, unit `2026-11-02-r-vn3-3-6-filing`. R-VN3-1 is filed in D-2026-11-02-A. R-VN3-2 is entered at DECISION_LOG `2026-11-02T21:23:45Z` (WHO: amear); D-2026-11-02-B records the tickprep intake that serves it and is not itself a ruling. Neither is refiled here.
**Beads:** Praxis_build-y07 (R-VN3-3), Praxis_build-99k (R-VN3-4), Praxis_build-1r7 (R-VN3-5), Praxis_build-48p (R-VN3-6), all P2. `Praxis_build-r8j` (Phase 3 spec import) raised P1 → P0 by this unit under R-VN3-5 and R-VN3-6. Amear's brief, as the master recorded it at DECISION_LOG `2026-11-02T22:12:53Z` (WHO: praxis-master), says only *"R-VN3-5 and R-VN3-6 raise the priority of r8j"*; it names no level. The level P0 is the master's choice in that dispatch row (*"the `r8j` priority raise P1 → P0 that R-VN3-5/6 call for"*), not Amear's (see NEEDS AMEAR 13).
**Source:** `docs/reports/2026-11-01-voice-session-notes-3.md` (47 lines, written by the chat/voice agent; untracked in git at the time of this entry). Each quoted string below is labelled with its author where it appears: Amear's words (as notes-3 records them), the voice agent's words, the rubric, or a ledger row. Anything from notes-3 not marked as Amear's words is the voice agent's record or the agent's reading.

**Times (notes-3 line 18, the voice agent's words, verbatim):** *"voice session 2026-11-02, between 21:21Z and 21:52Z. Exact times were not captured."*

**R-VN3-3 — data holes and gaps (handoff §5.2).**
- Amear's words (notes-3 line 21): *"I would just proceed as it is."*
- Voice agent's record (notes-3 line 20): proceed with the data as it is; the two 17-day holes and the three wider gaps are carried as a stated limitation, and nothing is re-sourced for them.
- The holes and gaps named, as recorded in `docs/reports/2026-11-01-three-strategy-results.md` (OBSERVED there by `grep -n`): holes 2021-09-09 → 2021-09-27 and 2025-12-14 → 2026-01-01 (lines 55, 413); gaps 2024-07-19 09:58–10:07 (line 59), 2024-08-02 11:55–12:02 (line 60), 2026-07-17 10:59–12:06 (line 61); *"**Three known gaps are wider than recorded**"* (line 414, verbatim). The known-gap day 2023-04-05 (line 62) is not one of the three and is not named by the ruling.
- **Settles:** the 1-minute data (date range 2021-03-08 → 2026-07-17, results report line 88) is used as it is; no re-sourcing or re-import of the holes or gaps; future backtest reports on this data carry them as a stated limitation.
- **Leaves open:** see NEEDS AMEAR 7 and 8.

**R-VN3-4 — Flat1559 exit (handoff §5.3).**
- Amear's first answer (notes-3 line 24): *"No."*
- Voice agent's record (notes-3 line 24): after it was explained that the trade closes at the 15:59 price and that the 4:00 PM label comes from NT8 stamping each bar with its end time, he answered (line 25): *"Uh, yeah."*
- Voice agent's record (notes-3 line 23): the fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is unchanged.
- **Settles:** handoff §5 item 3 (filer's mapping: that item asks whether a fill at the 15:59:00 price meets his "flat at 15:59" intent) — accepted; `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` is unchanged.
- **Leaves open:** F2 (session-flat time vs breakers #4 and #5) is not touched by this ruling and stays FROZEN; the early-close stamp question (handoff §5 item 1) is separate and not ruled.

**R-VN3-5 — O4, backtest vs breakers.**
- Amear's words (notes-3 line 28): *"If they're not live, then they're not live."* … *"Yeah, once uh, once it goes through."* Between the two quotes the voice agent recorded, in brackets, what Amear was told: *"[told breakers will be live, built in Block 3, required before paper and live]"* — the agent's words, not Amear's.
- Agent's reading, confirmed by Amear in voice only (notes-3 line 29): the backtest runs **with the breakers on, once they are built**. That raises the priority of `r8j`, the Phase 3 spec import, because the breaker definitions live there.
- **O4 criterion** (`specs/SPEC_RUBRIC.md:94-99`, verbatim): *"Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end the session after two consecutive losers. Block 4's gate compares live to backtest within ±15% win rate and ±25% average trade P&L. **Required:** a written statement of whether the Block 2 backtest runs with breakers applied, without them, or both — and how the Block 4 gate is satisfiable if they differ."*
- **Settles (against O4):** in the agent's reading, confirmed by Amear in voice only and entered at the ledger row above: the backtest runs **with the breakers on, once they are built** (notes-3 line 29). Filer's mapping, not part of the ruling: O4 asks this of the Block 2 backtest. The ruling says nothing about any other run (see Leaves open).
- **Leaves open (against O4):** whether a without-breakers run is also kept (the "or both" option); how the Block 4 gate is satisfiable if the backtest and live configurations differ — the ruling does not address it; the breakers are not defined in the repo (`Praxis_build-r8j`, description: the nine breakers are *"TBD — needs PHASE 3 BUILD SPECIFICATION import"*) and are not built. This entry does not mark O4 cleared; that is the auditor's grade.

**R-VN3-6 — O1, which version is judged (go/no-go).**
- Amear's words (notes-3 line 32): *"one that is closest to live execution."*
- Agent's reading, given to Amear in voice and not contradicted (notes-3 line 33): judge whichever version will actually trade live, tested as close to real conditions as possible, meaning High fill resolution and breakers on.
- Voice agent's record (notes-3 line 34, verbatim, bold markers as in the file): `` **Still open under O1:** the ruling does not say which of the six pass gates apply, or whether walk-forward efficiency ≥ 0.50 applies to an untuned version. That needs the Phase 3 spec (`r8j`). ``
- **O1 criterion** (`specs/SPEC_RUBRIC.md:74-79`, verbatim): *"Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates and is undefined without an in-sample optimisation step. Deviation D removed optimisation from the first pass. **Required:** a written statement of which gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the replication arm or the later optimisation arm."*
- **Settles (against O1), in Amear's words only:** the go/no-go judges the version *"closest to live execution"*. That this means High fill resolution and breakers on is the agent's reading, which Amear did not contradict. Not contradicting a reading is not ruling on it, so this entry records it as the agent's reading and not as Amear's ruling (see NEEDS AMEAR 14).
- **Leaves open (against O1):** which gate set applies; whether WFE ≥ 0.50 applies to an untuned version; whether GO/HOLD/REJECT sits on the replication arm or the later optimisation arm. O1's **Required** statement is not supplied by this ruling. This entry does not mark O1 cleared.

**S6 cross-block — no block's spec changes:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. FROZEN.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. FROZEN. R-VN3-4 concerns the Flat1559 strategy variant only.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. The void clause of D-2026-10-30-A stands. R-VN3-6's "High fill resolution" reading does not authorise a purchase, an import or a run (R-VN3-2, notes-3 line 16).
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. FROZEN.
- No code, template or config changed.

**NEEDS AMEAR (questions only):**
1. O1: which of the six Block 2 pass gates apply to the version judged under R-VN3-6?
2. O1: does walk-forward efficiency ≥ 0.50 apply to an untuned (no-optimisation) version, and does GO/HOLD/REJECT sit on the replication arm or the later optimisation arm?
3. O4: is a without-breakers backtest also kept alongside the with-breakers one, and how is the Block 4 ±15% / ±25% gate to be satisfied if the backtest and live configurations differ?
4. Until the breakers are built, are backtest results without breakers (such as the 2026-11-01 runs) used for anything, or held as records only?
5. With F1 FROZEN (Block 3 specifies the breakers as n8n workflow gates), how are the breakers to be applied inside a Strategy Analyzer backtest?
6. Not ruled (notes-3 line 40): how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7 (VM hash-check of the three strategy files) and 8 (archiving the Desktop CSVs and screenshots)?
7. R-VN3-3: does "proceed as it is" also cover the effect of each 17-day hole on the 14-day lookback the Noise-Area bands use for the sessions right after it (handoff §4 item 2, not analysed)?
8. R-VN3-3: does it also apply to the tick data for the High fill-resolution preparation (R-VN3-2), or only to the 1-minute data?
9. F4: the 2026-10-28 MFFU reply names the Tradovate API, not NinjaTrader/Rithmic. Does Amear send the follow-up himself (notes-3 line 44)?
10. Not ruled (notes-3 line 45): how does Amear answer csv-analyses §7 questions 1–6 (`docs/reports/2026-11-01-csv-analyses.md:292-297`)?
11. Does `Praxis_build-7zq` close?
12. Is `PraxisLastHalfHourMomentum` in or out of the High fill-resolution comparison?
13. `Praxis_build-r8j` was raised to P0, the level the master chose. Amear's brief asks for a raise without naming a level. Is P0 the level he wants?
14. R-VN3-6: does "closest to live execution" mean High fill resolution and breakers on, as the agent read it to him?

---

## 2026-11-03 — D-2026-11-03-A: R-VN3-2 — VM agent's High fill-resolution plan and VM notes filed to docs/reports/ unchanged; VM-side hash chain as reported; R-VN3-2 limits check; open questions listed, not answered

**Date:** 2026-11-03
**Status:** RECORDS A FILING. This entry is NOT a ruling by Amear and authorises nothing. Amear's brief item 2 (2026-11-02) asked for it: copy the VM agent's plan into `docs/reports/`, add MANIFEST rows, check the plan against R-VN3-2's limits, list its open questions, and not answer them. Ledger row for this unit (S4/S5): DECISION_LOG `2026-11-03T18:32:27Z` (WHO: praxis-master, "UNIT `2026-11-03-vm-plan-filing` DISPATCHED (brief item 2 of pasted 012a, 2026-11-02)"). R-VN3-2 itself is DECISION_LOG `2026-11-02T21:23:45Z` (WHO: amear). None of these rows authorises a purchase, an NT8 import or a run. Appended 2026-11-03 by praxis-manager, unit `2026-11-03-vm-plan-filing`.
**Ruling it serves:** R-VN3-2 (`docs/reports/2026-11-01-voice-session-notes-3.md` line 16): *"It does not authorize a purchase, an import or a run."* The limits, as the master's brief for this unit quotes Amear's brief: no purchases, no NT8 imports, no runs without Amear's approval.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades used below:** OBSERVED (seen by this unit on this Mac, 2026-11-03) / INFERRED (reasoned, not checked) / REPORTED BY AMEAR / REPORTED BY the VM agent (the Claude Code agent on the Windows VM that wrote the plan and notes) / REPORTED (vendor or forum, as cited by the VM agent) / UNVERIFIED. The VM agent's own grade words (its "OBSERVED", "VERIFIED", "REPORTED BY AMEAR") mean seen on the VM, or said to it. On this Mac, everything the VM agent says it saw or heard is REPORTED BY the VM agent.

**Files filed (copied with `cp`, names unchanged, contents NOT edited — findings are recorded here, not fixed in the files):**
- `docs/reports/2026-11-02-vm-high-res-plan.md` — 11,834 B, sha256 `99e23a0512546d328e48d1f0f6fcc920f53a80905968f19c97d75f0944dcdf40`, 138 lines.
- `docs/reports/2026-11-02-vm-notes.md` — 4,829 B, sha256 `304f5795a353bedfe38c741f0f78f09487ab5b0d1fd19afed2ecfece0e29aee3`, 65 lines.
- `docs/reports/SHA256SUMS-vm-handoff.txt` — 186 B, sha256 `00ce26cd39a21a3b0d72b6e66ff9f97dc0a6ca2a39a8f953f1cffa2fb583e787`; two lines, the VM-side sums of the two files above.
Plan line numbers below are `cat -n` line numbers of the filed copy. Notes line numbers likewise.

### a. Provenance chain and the VM-side hash block

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

1. **Windows VM.** The VM agent wrote the plan and the notes there and hashed the tickprep originals in `C:\Users\amear\Desktop\praxis-tickprep\` with `Get-FileHash -Algorithm SHA256`, "run 2026-11-02" (notes lines 12–14). REPORTED BY the VM agent.
2. **Google Drive.** Uploaded to Amear's Drive, "same Drive folder as `praxis-tickprep`" (notes line 7). REPORTED BY the VM agent. Notes line 43 quotes Amear asking for the upload (*"upload it to my google drive and give mew the ling"*, quoted as the notes give it) — REPORTED BY the VM agent, quoting Amear. Whether this is the same Drive folder id `1YaM4I3BKt_nNKWdUnOkj4kJzCeBEwLe_` that D-2026-11-02-B names: UNVERIFIED (not checked).
3. **Mac synced folder** `~/Library/CloudStorage/GoogleDrive-bani.amear@gmail.com/My Drive/praxis-tickprep/` — OBSERVED: it holds seven files: the plan (11,834 B), the notes (4,829 B), `SHA256SUMS-vm-handoff.txt` (186 B), and `MakeSynth.cs` (3,732), `README.md` (2,219), `TickPrep.cs` (18,785), `nt-implied-offsets.csv` (645). No `.exe` file is in it (OBSERVED). The plan and the notes hash to the two values in `SHA256SUMS-vm-handoff.txt` (OBSERVED). The four tickprep files hash equal to `tools/tickprep/SHA256SUMS` (OBSERVED).
4. **`docs/reports/`** — copied by this unit with `cp`. OBSERVED: source and destination sha256 equal for all three files; `cmp` exit 0 for all three; `cd docs/reports && shasum -a 256 -c SHA256SUMS-vm-handoff.txt` prints `OK` for both files, exit 0.
- What this shows and what it does not: the Mac OBSERVED that the copies equal the hashes the VM agent wrote into `SHA256SUMS-vm-handoff.txt`. That those hashes were computed on the VM is REPORTED BY the VM agent. `SHA256SUMS-vm-handoff.txt` itself carries no VM-side hash; under handoff §0 (line 11) it stays UNVERIFIED as a VM original.

**VM-side hash block (notes lines 17–22, verbatim; REPORTED BY the VM agent — the Mac cannot run `Get-FileHash` on the VM):**
```
398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507     3732 B  MakeSynth.cs
3d81495ffe060ffffd71ca4f5993e9f8c312df8d76a1d34818d6c9062a7763a0     7168 B  MakeSynth.exe
199a66a73cdf6c1af032a2807d4d3b9e0bceff8a655f80408d3d6e2f7df491a3      669 B  nt-implied-offsets.csv
81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5     2219 B  README.md
104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545    18785 B  TickPrep.cs
72f237468758f8c053a93a9d8ed4ad3805a5b8353afa0eb640d6a1ef9f2cce88    22016 B  TickPrep.exe
```
- **Compiler banner** (notes line 28, REPORTED BY the VM agent): `Microsoft (R) Visual C# Compiler version 4.8.9221.0` (`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe`).
- **`.cs` and `.md` files.** The three reported hashes for `MakeSynth.cs`, `README.md` and `TickPrep.cs` equal the Mac copies in `tools/tickprep/SHA256SUMS` (string equality OBSERVED). The VM agent's grade "Transfer: VERIFIED" (notes line 25) is its own word. On this Mac the link is: reported VM hash = observed Mac hash.
- **`nt-implied-offsets.csv`.** Reported VM file: 669 B, 24 CRLF lines (notes line 26). OBSERVED on this Mac: converting the Mac copy (645 B, LF) to CRLF line endings (`awk '{printf "%s\r\n", $0}'`, piped to stdout, no file written) gives 669 bytes and sha256 `199a66a73cdf6c1af032a2807d4d3b9e0bceff8a655f80408d3d6e2f7df491a3`, which equals the reported VM hash. The Mac copy plus CRLF reproduces the reported VM bytes. That the VM file has that hash is REPORTED BY the VM agent.
- **`.exe` files.** The hashes are REPORTED BY the VM agent: `TickPrep.exe` 22,016 B `72f23746…ce88`, `MakeSynth.exe` 7,168 B `3d81495f…63a0`. The binaries have **not** been transferred (OBSERVED: absent from the synced Drive folder and from `tools/tickprep/`). Nothing here has been compiled.

**What this changes in D-2026-11-02-B's grades (B-4 and every other NEEDS AMEAR item stay open):**
- B §c ("VM-side originals — UNVERIFIED"; "The hashes of `TickPrep.exe` and `MakeSynth.exe` are unknown"): the VM-side hashes now exist on record as REPORTED BY the VM agent. For the three `.cs`/`.md` files the reported hashes equal the Mac copies (OBSERVED equality). For the CSV, the reported hash equals the Mac copy converted to CRLF (OBSERVED computation). The `.exe` hashes are known as reported values only. No byte of a VM file was observed from the Mac.
- B §d (CRLF arithmetic, "INFERRED ... the Desktop copy was not checked"): the VM agent now reports 669 B with 24 CR bytes, and the Mac's CRLF conversion reproduces the reported hash (OBSERVED). B §d's INFERRED reading is consistent with this. The VM Desktop copy has still not been seen from the Mac.
- B §a.2 (folder id `1YaM4I3BKt_nNKWdUnOkj4kJzCeBEwLe_`, "Not opened by this unit"): not closed. A Drive folder named `praxis-tickprep` is now OBSERVED through the Mac's sync, and its four tickprep files equal `tools/tickprep/SHA256SUMS`. Whether it is the folder with that id stays UNVERIFIED (step 2 above).
- D-2026-11-02-B's NEEDS AMEAR items, as this entry finds them (it closes none itself): B-1 (`.exe`) — DECISION_LOG `2026-11-03T18:45:00Z` (WHO: amear) records *"**"commit to repo"** = BINARIES TOO (closes D-2026-11-02-B NEEDS AMEAR 1)"*; B-2 (purchase) — DECISION_LOG `2026-11-03T18:40:00Z` (WHO: amear) records *"**"no, not paying that. i dont know what 8 questions."** = NO Portara purchase at $695"*. That row answers a $695 question; it does not name B-2, which asks about the purchase with no price. Linking the row to B-2 is the filer's cross-reference. B-2 stays open apart from the $695 purchase (both rows are the authorisation, S5; see the note at the head of e). Still open: B-2 (apart from the $695 purchase), B-3 (self-test as a "run"), B-4 (whether the VM originals should be hashed — the hashing is REPORTED BY the VM agent as done, at handoff §3.2's request; whether that disposes of B-4 is Amear's), B-5 (which CSV copy is canonical), B-6 (`--offsets`), B-7 ("option C" — see (e) item 31), B-8, B-9, B-10.

### b. R-VN3-2 limits check of the plan

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Does the plan itself buy, import or run anything?** No such act is recorded. Plan line 3: *"**Plan only.** Nothing was bought, imported, run or changed in NinjaTrader to write it."* Notes line 3: *"Nothing was bought, imported, run, compiled, edited or deleted for this. The only actions were reads, hashes, and writing these two files."* Both are REPORTED BY the VM agent; nothing on the Mac can check what happened on the VM. Reads of NT8 data the VM agent reports making: `db\tick` file count (plan line 25, notes line 34), the `db\minute` folder names (notes line 35: *"Only the folder names were read, not the contents or date ranges."*), the 0-S snapshot in `strategyanalyzerlogs` (plan line 17). These are reads, as reported, not imports or runs.

**Steps the plan proposes that would need Amear's approval, and whether the plan labels each as his decision:**

| Step | Plan line(s) | Labelled as Amear's decision? |
|---|---|---|
| Purchase of Portara ticks, $695 | 53, 130 | Yes. Line 53: *"**Question for Amear (purchase):** buy Portara ENQ trades-only ticks ... for **$695**?"*; line 130 (Q1). |
| P0: TickPrep measure/build/verify on a March 2021 sample, "no import" | 96 | **No separate question.** Line 57's §3 heading gates the build chain *"after purchase and Amear's OK"*; P0 uses a sample asked for free (line 127), so whether line 57 covers it is not stated. Line 133 (Q4) presupposes P0 (*"once the sample passes"*). Relates to B-3. |
| P1: one-month import (March 2021), plus *"one High run on the month to time it, measure memory, and see whether slippage is applied"* | 97, 133, 86 | **Partly.** Line 133 (Q4): *"Approve P1 (one-month import) once the sample passes?"* — names the import; the Standard run (*"0-S on that month unchanged"*) and the High run inside P1 (line 97) are not named in the question. Line 86: *"Import dialog (when approved)"*. |
| Safeguard: copy `db\minute\NQCONTROW 09-25` and hash it before any import | 82 | Not labelled separately; placed inside the import step (line 81 *"Safeguards in the plan"*). |
| Full-range tick import (all 23 contracts), which R0 presupposes | 98 (*"after full import"*) | **No question.** Line 133 (Q4) covers the one-month import only. |
| R0: 0-S full range after full import | 85, 98 | **No question.** |
| R1: 0-H (High, Tick 1, slippage 2) | 99 | **No question of its own.** The nearest is line 138 (Q9): *"Should the High measurement runs wait for `r8j` (breakers), or go ahead as measurement-only?"* |
| R2: High with slippage 1 | 100, 134 | Yes, line 134 (Q5). |
| R3–R4: OppBand, Flat1559 at High | 101 | **No question.** |
| `--offsets` forcing | 65, 132 | Yes. Line 65: *"Rerunning with `--offsets` to force NT's values is a choice for him, not a default."*; line 132 (Q3). |
| Central-time code change | 73 | Yes in text: *"Central would need a code change, a question for Amear first"*. Not in the §6 list. |
| TickPrep `measure` → `build` → `verify` on purchased real data | 57, 63–67 | Yes. Line 57: *"Build chain (after purchase and Amear's OK; not run on real data)"*. |
| Memory fallbacks: year-by-year runs, or a 1-second fill series | 105, 136 | Yes. Line 105: *"a 1-second fill series (a departure from the spec). Both are Amear's call."*; line 136 (Q7). |
| Reading NT's per-contract NQ minute folders | notes 35, notes 61 | Yes (notes). Notes line 35: *"That's a question for Amear, not done."* Not in the plan. |
| Analyzer dropdown look (whether Tick 1 can be picked), "with no run" | 29 | **Not labelled.** Line 29: *"Checking that Tick 1 can be picked is a 2-minute look at the dropdown, with no run."* Whether it needs approval is Amear's. |

**Things the plan presents as settled that the ledger records as open or as Amear's (recorded, not decided):**
1. Line 32: *"R-VN3-5/6: the judged version is High resolution **with the circuit breakers on**."* The plan grades this line *"REPORTED (Mac handoff)"* and calls every High run in it *"a **measurement run** ... not the go/no-go run"*. The handoff (§2 line 36) told the VM agent: *"Treat that reading as the working target, not as his ruling."* The sentence as written states the reading as settled; High fill resolution under R-VN3-6 is the voice agent's reading, not Amear's ruling (D-2026-11-02-C, NEEDS AMEAR 14).
2. Line 103: *"Last-Half-Hour Momentum is **not included** (R-VN3-1)."* Whether it is in or out of the High comparison is open (D-2026-11-02-A NEEDS AMEAR 3; D-2026-11-02-C NEEDS AMEAR 12). The handoff told the VM agent not to include it unless Amear says so (handoff §2 line 31), so the plan follows the handoff's default. Its citation of R-VN3-1 as the reason goes further than the ledger does.
3. Lines 66 and 71 apply R-VN3-3 to the tick build (*"Strict: minutes missing from the 1-min file get no ticks (R-VN3-3)"*; the holes *"stay empty (R-VN3-3)"*). Whether R-VN3-3 covers the tick data is open (D-2026-11-02-C NEEDS AMEAR 8). The handoff's line 33 told the VM agent to keep `TickPrep build` strict.
4. Line 28 and line 99 call a slippage drop under High *"the F3 void-clause trigger"* / *"stop: F3 void clause, back to Amear."* This is the VM agent's reading of the void clause (see d).
5. Line 45: *"Flat is cheaper."* (the $695 flat price against $750 by the year) and line 48 *"**Ask for US Eastern**"* are recommendations inside a purchase that is posed as a question (line 53). Recorded, not adopted.
6. Line 64 step 1(b) sets an acceptance for unmatched minutes (*"every one listed and explained"*). The threshold is open (D-2026-11-02-B NEEDS AMEAR 9).
7. Line 85 (R0 must reproduce *"1,190 trades and $197,327.60 exactly"*) and line 98 (*"total slippage 1190"*): these are pass bars the plan sets. The figures themselves are on record on the Mac: 1190 trades and net $197327.60 (`docs/reports/2026-11-01-three-strategy-results.md` lines 67 and 73, CSV OBSERVED there and REPORTED BY AMEAR from his C4 Summary), and "Total slippage" shown 1190, equal to the trade count, NOT DERIVABLE from the CSV (same file, line 227). Whether these are the R0 and R1 pass bars is Amear's.

### c. Evidence-grade issues (recorded, not fixed — the filed files are unedited)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

1. **"REPORTED BY AMEAR" in the VM files.** Plan line 38 (*"REPORTED BY AMEAR (button answers in this VM session)"*), plan line 22 (*"REPORTED BY AMEAR (C4 screenshot readback)"*) and notes §3 (line 37 heading *"Amear's words in this VM session: REPORTED BY AMEAR"*, quotes at lines 40–43). On this Mac all of these are REPORTED BY the VM agent: this unit has only the VM agent's account; notes line 45 places the exact text *"in the VM session transcript"*, which this unit has not seen. Notes line 45 is marked *"Paraphrased"* under the same heading; a paraphrase is the VM agent's words.
2. **Plan line 71**: *"REPORTED BY AMEAR ("I would just proceed as it is")"*. That quote reached the VM through the Mac handoff (handoff line 33). On the Mac its source is notes-3 line 21 (the voice agent's record of Amear's words). For the VM agent, the plan's own grade for this would be "REPORTED (Mac handoff)".
3. **The VM agent's "OBSERVED" and "VERIFIED".** Plan line 7 defines OBSERVED as *"run or read on this VM"*. Notes lines 25–26 use "VERIFIED", which is not one of the handoff's grades (handoff line 13: OBSERVED / INFERRED / REPORTED BY AMEAR / UNVERIFIED). On the Mac all of these are REPORTED BY the VM agent unless re-checked here. Re-checked here, OBSERVED: `nt-implied-offsets.csv` has 23 data rows (24 lines with the header), `NQ 06-21,3342.75,2021-03-11` (line 3) and `NQ 09-26,0,2026-06-12` (line 24), matching plan lines 43 and 64. The three Noise-Area strategy files in `ninjascript/` contain 0 occurrences of `AddDataSeries` (`/usr/bin/grep -c`), consistent with plan line 26's single-series claim for the repo copies. Whether the VM-installed copies are the same files is open (handoff §3.3; (e) item 26).
4. **NT8 behaviour resting on forum posts or docs** stays REPORTED/UNVERIFIED, as the plan itself grades it: slippage under High (line 28, *"REPORTED (forum); UNVERIFIED on 8.1.8.4"*); Tick-1 availability on a 1-min primary (line 29, *"REPORTED (forum); UNVERIFIED"*); server tick retention and "Unknown instrument" (line 27, *"REPORTED (NT forum / help guide); the server limit is UNVERIFIED here"*); High not usable with `AddDataSeries` or Tick Replay (line 26, *"/ docs"*). The import writing only to `db\tick` (line 80) is graded *"Import behaviour: INFERRED"* by the plan. On the Mac it is INFERRED by the VM agent, not tested. Handoff line 13: a claim about NT8 behaviour is graded by running it.
5. **Portara facts are REPORTED (vendor).** Product, price ($695 flat; $125/yr, $500 minimum, $750 to reach March 2021), the 56.8 GB size, timestamps (plan lines 42, 45, 46, 48) are graded REPORTED (Portara pages, read 2026-11-02, by the VM agent). The ~10–25 GB window estimate is INFERRED from *"an assumed 200k–500k trades/day (no published figure)"* (line 46). The licence (line 49) and delivery (line 50) are UNVERIFIED. Notes line 48 corrects an earlier VM figure of ~$625 to $695.
6. **Spec-line claim vs `specs/SPEC_RUBRIC.md` F3.** F3's "Why frozen" text (rubric lines 49–50, verbatim): *"The Block 2 spec requires Order Fill Resolution = High with a 1-tick resolution series, 1-tick slippage, $2.96 round-trip."* Plan table lines 17–21, column *"High value (spec F3 line)"*: High; Tick; 1; slippage *"**1** per the spec line"*; commission *"$2.96 round trip ... unchanged"*. The four values match the rubric text. Two notes, not findings against the plan: (i) the line the plan quotes is F3's "Why frozen" description of the Block 2 spec, not F3's **Criterion** (rubric lines 46–48: *"The fill resolution the Strategy Analyzer will actually run at, and the slippage assumption applied at the band edge, stated in writing before the backtest runs."*); (ii) the rubric says "1-tick slippage" with no "/side"; the plan's column is "ticks/side" (line 20). The rubric's F3 text in the working tree equals `HEAD` (OBSERVED, `diff` of lines 45–57 empty).
7. **Handoff §3.1 six-section check.** The plan's six headings are §1 line 11 *"What High resolution needs"*, §2 line 36 *"Data"*, §3 line 57 *"Build chain"*, §4 line 77 *"The instrument and how a tick import would sit"*, §5 line 90 *"The 0-H control"*, §6 line 110 *"Risks and open questions for Amear"*. They follow handoff items 1–6 in order. Against the item contents: item 2's licence and delivery are present as "Ask" (lines 49–50); item 3's 2021-06-10 roll, DST and time zone are present (lines 70, 72, 73); item 4 is "plan only, no import" (line 77); item 5 is "design only" (line 90); item 6 is numbered. Handoff line 43 asks for *"every number graded"*: the §5 table (lines 94–101), including the R0 bars, has no grade column, and line 106 states no runtime basis.
8. **File span conflict.** Handoff item 2 (line 45) and handoff §4 (line 61) give the 1-min file as 2021-03-08 → 2026-07-17. Plan line 44 and notes line 51 give the file as 2021-03-07 → 2026-07-20 and the test window as 2021-03-08 → 2026-07-17 (REPORTED BY the VM agent; the plan grades it OBSERVED). OBSERVED on the Mac copy `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt` (the bar file `docs/reports/2026-11-01-three-strategy-results.md` line 38 names): first line `20210307 180100;16120.5;16167;16120.5;16154.75;17`, last line `20260720 112700;29005.5;29020.75;29003.5;29016;308`. The Mac copy's span agrees with plan line 44, not with handoff lines 45 and 61. Whether the Mac copy is byte-identical to the VM's file is UNVERIFIED (no hash comparison on record).
9. **VM host name.** Notes line 32 (REPORTED BY the VM agent): *"Host: **VMware** ... An earlier VM note called it Parallels; that was wrong."* `DECISIONS.md` D-2026-07-09-B (line 96) titles the execution host *"Parallels Windows 11 ARM VM"*. This entry does not amend D-2026-07-09-B. Recorded only.
10. **Self-test.** Plan line 59 restates the self-test as *"OBSERVED on the VM 2026-11-02; on the Mac it is REPORTED."* That matches D-2026-11-02-B §h's grade. Not reproduced here.

### d. F3 interaction — the plan's "void-clause trigger" against D-2026-10-30-A as written

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **The plan** (line 28, verbatim): *"**Slippage under High: risk.** An NT staff forum post says slippage applies only under Standard. If that's true, a High run silently drops 2 ticks/side. That is the **F3 void-clause trigger**: if it is seen, F3 goes back to Amear. REPORTED (forum); UNVERIFIED on 8.1.8.4."* Line 99 (R1 stop check): *"Total slippage must still read 1190. If not, stop: F3 void clause, back to Amear."* Line 113 (risk 1): *"Slippage may be ignored under High, which would trigger F3."*
- **D-2026-10-30-A's void clause** (`DECISIONS.md` line 264, VERBATIM there from DECISION_LOG `2026-08-29T00:10:00Z`): *"We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold."* Same line: *"The clause's trigger is "the VM measurement"; the ledger records only that no run has set High (REPORTED BY AMEAR, 2026-10-30T21:36:30Z). Whether a High run is the trigger is Amear's."*
- **D-2026-10-30-A NEEDS AMEAR 5, as ruled** (`DECISIONS.md` line 300): *"Identical → (c) is OBSERVED and F3 moves to PASSED by Amear's edit of `specs/SPEC_RUBRIC.md`; different → the `2026-08-29T00:10:00Z` void clause fires and (c) is re-decided cold."* The comparison there is of trade lists, Standard vs High, *"every other field held"*.
- **Recorded, not decided:** the clause's text names NT8 *erroring* or *demanding a secondary series* "rather than falling back silently". A silent slippage drop under High is not named in the clause's text. The plan's line 28 links the two; that link is the VM agent's reading. Line 300's ruling names a second outcome (the trade lists differ). The plan's R1 stop check (line 99) tests the total-slippage figure. Its R1-vs-R0 report (line 103, *"trade count, number of trades whose entry or exit price changed, net, PF, max DD, and per-exit-type differences (XS / XL / session close)"*) compares the two runs' trades. The plan does not tie line 103 to the void clause or to line 300. The plan's R1 changes Order fill resolution to High and the fill-resolution type from Minute to Tick (lines 17–18, 99) and holds slippage at 2 (line 99, *"**Slippage stays 2.**"*). Whether that set of changes is the control ruled at line 300 is open: D-2026-10-31-A (line 363) lists as still open *"Step 0, the values for High's extra fields and what counts as "identical""*. Whether a slippage drop under High voids D-2026-10-30-A, and which check decides it, are Amear's (line 264). The plan's line 28 says *"F3 goes back to Amear"*; it does not decide the outcome either.
- F3 is not advanced by this entry. No High run exists. The void clause stands, NOT triggered and NOT retired.

### e. Consolidated NEEDS AMEAR list (questions only — listed, not answered, not recommended, not ranked)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Numbering follows the order of the sources (plan §6, then notes §6, then notes §5, then items found elsewhere in the two files). It is not a priority order. "Same as" means the item is already open in an earlier entry and is listed here once with the cross-reference; "relates to" means it overlaps without being the same question. B-n, C-n and A-n are the NEEDS AMEAR items of D-2026-11-02-B, -C and -A.

**Ledger rows written while this unit ran.** DECISION_LOG now carries three rows WHO: amear, stamped `2026-11-03T18:40:00Z`, `2026-11-03T18:45:00Z` and `2026-11-03T18:50:00Z` (each with an approximate `WHEN: ~` time). Under S5 those ledger rows are the authorisation; they govern wherever they rule on an item below, whether or not a DECISIONS entry has filed them yet. The 18:40Z and 18:45Z rows each say *"to be filed in DECISIONS after the running unit returns"*; this entry does not file them or interpret them. It marks, at items 14, 21, 22, 23, 24 and 25 (and at B-1 and B-2 in section a), which row speaks to the item, quoting the row; where a row records its outcome as unresolved or deferred, that is quoted too. The 18:50Z row also records rulings outside this list (on the STATUS.md refresh and on old uncommitted changes; and, on whether to look for a cheaper or free tick source, a bare *"yes"* that the row records under *"master reading: LOOK"*, with the scope *"set by master"*). The list otherwise records the plan's and the notes' questions as written.

*Plan §6, Risks (lines 112–117) — the plan lists these under "Risks and open questions for Amear"; recorded as written:*
1. Line 113: *"Slippage may be ignored under High, which would trigger F3. REPORTED (forum)."* Relates to D-2026-10-30-A line 264 (whether a High run is the trigger is Amear's) and to (d).
2. Line 114: *"The measured offsets might not equal NT's (the 1-min file's source isn't proven)."* Relates to B-6 and B-8, and to items 15 and 16.
3. Line 115: *"Importing ticks could change how NT builds the 1-min primary. R0 catches this."* New.
4. Line 116: *"A full-range High run could run out of memory."* Relates to item 20.
5. Line 117: *"The Portara licence is unknown."* Same as item 11.

*Plan §6, Questions to send Portara (lines 119–127; line 119: "Amear sends them"):*
6. Line 120: *"What roll dates and back-adjustment method does the continuous ENQ file use?"*
7. Line 121: *"Do individual contract files cover the whole contract life or only the front-month window?"*
8. Line 122: *"Are Eastern stamps DST-aware and at trade time?"*
9. Line 123: *"What is the delivered size for ENQ 2014 → now, zipped and unzipped?"*
10. Line 124: *"Are ticks filtered or cleaned?"*
11. Line 125: *"Does the licence allow personal backtesting?"*
12. Line 126: *"How is the data delivered, and how long does it take?"*
13. Line 127: *"Can we have a free March 2021 sample?"* Relates to item 34 (P0).
(Whether these eight are sent is notes §6 item 1, item 23 below.)

*Plan §6, Open questions for Amear (lines 129–138):*
14. Line 130: *"Buy Portara ENQ ticks for $695 (after the answers above)?"* Relates to B-2 (B-2 names no price); restated by notes line 60 (item 23). Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (1), *"= NO Portara purchase at $695."*
15. Line 131: *"Where did the 1-min file come from? If it's NinjaTrader's `NQ ##-##` back-adjusted series, the offsets in `nt-implied-offsets.csv` are the expected answer."* Relates to B-8 (first half) and to item 24.
16. Line 132: *"If any measured offset differs from NT's, stop there, or force NT's values with `--offsets`?"* Same as B-6.
17. Line 133: *"Approve P1 (one-month import) once the sample passes?"* New. P1 (line 97) also contains a 0-S run on that month and one High run on the month; this question's text names neither.
18. Line 134: *"R2: add the 1-tick-slippage spec run after the 0-H control?"* New. R2 changes slippage from R1 (line 100, *"R1 plus slippage = 1"*). Relates to D-2026-10-30-A line 300 and to D-2026-10-31-A line 363 (High's extra fields; what counts as "identical"); see item 36.
19. Line 135: *"Is "Baseline-H" a separate run from 0-H, or the same?"* New. The term "Baseline-H" occurs in no other `docs/reports/*.md` file (OBSERVED, `/usr/bin/grep -rln`).
20. Line 136: *"Memory fallback: year-by-year runs or a 1-second fill series?"* New. Line 105 calls the 1-second series *"a departure from the spec"*.
21. Line 137: *"Should the `.exe` files go into the repo, or source only with the rebuild command?"* Same as B-1; restated by notes line 62 (item 25). Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (3) *"**"keep them for reference"** — master reading UNRESOLVED"*, then `2026-11-03T18:45:00Z` (3) *"**"commit to repo"** = BINARIES TOO"*.
22. Line 138: *"Should the High measurement runs wait for `r8j` (breakers), or go ahead as measurement-only?"* Relates to C-4 and C-5 and to R-VN3-5 (D-2026-11-02-C). Relates to items 17, 36 and 37. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (4) *"**"yes"** — master reading UNRESOLVED"*, then `2026-11-03T18:45:00Z` (4) *"**"when the time comes ask agaian."** = DEFERRED"*.

*Notes §6 (lines 58–63; line 59: "The ones that block the next step"):*
23. Line 60: *"Send Portara the eight questions (plan §6), then decide whether to buy for $695."* Same as item 14 for the purchase; relates to B-2. Sending the questions is new. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (1), Amear's words *"no, not paying that. i dont know what 8 questions."*
24. Line 61: *"Should the per-contract NQ minute folders already on the VM be read (read-only) to confirm the 1-min file's source before buying?"* New. Relates to items 15 and B-8. Notes line 35: the folders seen are *"NQ 03-20 through NQ 12-26"*; *"Only the folder names were read"*. Ledger: DECISION_LOG `2026-11-03T18:40:00Z` (2) *"**"yes"** = read-only readback APPROVED for the VM agent."*
25. Line 62: *"`.exe` files: into the repo or not? If yes, they go up as the files themselves via Drive, with the hashes above."* Same as B-1 / item 21. Ledger: see item 21.
26. Line 63: *"§3.3 items (strategy-file hash check, template early-close readback): do them or not?"* Same as C-6 (11-01 handoff §5 items 7 and 1). The 11-02 handoff §3.3 (lines 56–58) puts them under "Only if Amear rules it".

*Notes §5, still owed from the screen (lines 53–56) — listed as owed, not as rulings:*
27. Line 54: *"Strategy Analyzer Log tab "ignored" messages"*.
28. Line 55: *"C6: save settings as default"* — step C6 of `docs/reports/2026-11-01-voice-handoff-commission-fix.md` (line 105).
29. Line 56: *"C7: NQCONTROW instrument readback."* — step C7 of the same file (line 113). Plan line 79 depends on it: the rollover 2021-03-01 / Do not merge state is *"REPORTED (Mac handoff)"* and *"UNVERIFIED"* until C7.

*Found elsewhere in the plan or notes, not in plan §6 (filer's extraction; listed, not answered):*
30. Plan line 73: tick files delivered in Central time *"would need a code change, a question for Amear first"*. New.
31. "Option C" label. Plan line 36 (*"Data (option C: Portara per-contract ticks)"*) and notes line 41 (*"Adjust per-contract myself" (option C, TickPrep)*) give the VM-side use of the label. REPORTED BY the VM agent. Relates to B-7. This entry does not mark B-7 closed.
32. Plan line 64 step 1(b): unmatched minutes *"every one listed and explained"*. Same as B-9.
33. CSV canonical copy: the VM copy is reported CRLF 669 B (notes line 26); the repo copy is LF 645 B. Same as B-5.
34. Plan line 96, P0 (TickPrep on the March 2021 sample): no approval question is posed for it. Relates to B-3 (whether the VM self-test counts as a "run" under R-VN3-2) and to item 13.
35. Plan lines 85 and 98, R0 (0-S full range after the import): no approval question is posed for it, nor for the full-range tick import it presupposes (line 98, *"after full import"*). Line 133 (Q4) covers the one-month import only.
36. Plan line 99, R1 (0-H): no approval question is posed for it apart from item 22. Relates to the Standard-vs-High control ruled at D-2026-10-30-A line 300 (NEEDS AMEAR 5: *"Commit conditional + R3 control tomorrow."*) and to D-2026-10-31-A line 363 (High's extra fields and what counts as "identical", still open). The plan does not say whether R1 is that control.
37. Plan line 101, R3–R4 (OppBand and Flat1559 at High): no approval question is posed for them.
38. Plan line 29, the Analyzer dropdown look ("with no run"): whether it needs approval is not posed.
39. Plan line 103, LHM *"not included (R-VN3-1)"*. Same as A-3 / C-12.
40. Plan lines 66 and 71, R-VN3-3 applied to the tick build. Same as C-8.
41. Plan line 32, the judged version as High + breakers on. Same as C-14.
42. Plan lines 85 and 98: whether "1,190 trades", "$197,327.60" and "total slippage 1190" are the R0/R1 pass bars (see b, item 7). New.
43. D-2026-11-02-B items not listed above: B-10 (`tools/tickprep/` path), not raised by the plan or notes; B-4 (whether the VM originals should be hashed), whose hashing the notes report done (section a). Both still open. B-3 is at item 34.
44. Plan line 82, the safeguard *"Copy `db\minute\NQCONTROW 09-25` and record SHA-256 for every file before any import"*: not posed as a question of its own; placed inside the import step (section b).
45. Plan lines 45 and 48: the price route (*"Flat is cheaper"*: $695 flat against $750 by the year) and the time zone to ask Portara for (*"**Ask for US Eastern**"*) are recommendations inside the purchase question (section b, item 5). Listed, not adopted.

### f. What this unit did and did not do on the Mac

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- Nothing was bought, imported, run, compiled or deleted on the Mac in this unit. No NT8 action. No tickprep command. Nothing was executed from the Drive folder.
- Acts: `cp` of the three files into `docs/reports/`; reads and hashes (`ls`, `cat`, `sed`, `shasum`, `cmp`, `wc`, `file`, `/usr/bin/grep`, `find`); one `awk` CRLF conversion of `tools/tickprep/nt-implied-offsets.csv` to stdout piped to `shasum` and `wc` (no file written); appends to `DECISIONS.md` (this entry) and `MANIFEST.md` (four rows); the manager report `docs/reports/2026-11-03-vm-plan-filing-manager.md`.
- Nothing staged by this unit. The filed copies are unedited.

**S6 cross-block — no block's spec changes:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. FROZEN.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. FROZEN.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. The void clause of D-2026-10-30-A stands. The plan is a plan; no High run exists.
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. FROZEN.
- No code, template or config changed.

---

## 2026-11-04 — D-2026-11-04-A: R-1104-1..3 — commit permission; housekeeping is Code's; R-1104-3 "Yeah" (brief's framing: High fill resolution + breakers on as the judged version); tick-data purchase condition (proof of concept)

**Date:** 2026-11-04
**Status:** RULED by Amear — R-1104-1..3, graded REPORTED BY AMEAR. They were relayed in his typed brief "BRIEF FROM AMEAR — 2026-11-04 (Claude.ai voice call)". The quotes are his; the framing is the brief's. Ledger authorisation (S5): DECISION_LOG `2026-11-04T17:27:42Z` (WHO: amear). Unit row: DECISION_LOG `2026-11-04T17:41:34Z` (WHO: praxis-master). Appended 2026-11-04 by praxis-manager, unit `2026-11-04-handoff-r1104-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades:** REPORTED BY AMEAR = his words in italics, as the 17:27:42Z row records them, except where another DECISION_LOG row is cited beside the quote (those are his words typed in session, verbatim in that row). Brief's framing = the other text of the 17:27:42Z row; it is not Amear's words. OBSERVED = seen by this unit on this Mac, 2026-11-04.

**R-1104-1 — commit permission (the word "standing" is the brief's framing).**
- Amear's words: *"I'm giving the agent permission to commit."*
- Brief's framing: the master may stage, commit and push its own audited units without asking. Exceptions unchanged: the old 12-path staged set, root file `F`, and other old uncommitted changes stay untouched and out of every commit (Amear, DECISION_LOG `2026-11-03T18:50:00Z` item (3), *"as is"*). Audit and park rules still apply.

**R-1104-2 — housekeeping is Code's.**
- Amear's words: *"state MD and all that kind of stuff can be handled by the code agent ... I don't know why this stuff keeps on coming up to me."*
- Brief's framing: STATUS.md, HANDOFF.md, MANIFEST rows, ledger flushes and commit composition are done by Code without escalation. Escalate only real decisions: strategy, money, live risk, F1–F4.

**R-1104-3 — judged go/no-go version; tick-data purchase condition.** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- Amear's words: *"Yeah"*. Brief's framing: *"Yeah"* = High fill resolution with circuit breakers on as the judged go/no-go version, confirming R-VN3-6. The row does not record the question he answered.
- Closes D-2026-11-02-C NEEDS AMEAR 14 (DECISIONS.md:544). That closure label is in the ledger row's framing. Amear's own word is "Yeah".
- Condition, Amear's words: *"if the high fill resolution costs $700 for the data, I'm not going to pay that right now until there's proof of concept."*
- Brief's framing: no tick-data purchase until Standard-resolution results show proof of concept. This entry does not define "proof of concept" (this entry's NEEDS AMEAR 1).
- Does not clear O1. The gate set is still open (D-2026-11-02-C NEEDS AMEAR 1–2, DECISIONS.md:531-532).

**Interactions — recorded, not decided.** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- (i) F3 (`specs/SPEC_RUBRIC.md:45-57`) and D-2026-10-30-A's void clause (DECISIONS.md:264): F3 stays FROZEN. The void clause stands, not triggered and not retired. Filer's reading, not a ruling: R-1104-3 authorises no purchase, import or run.
- (ii) R-VN3-5 (DECISIONS.md:508-513): the breakers are not built and not defined in the repo; they wait for `Praxis_build-r8j`. Amear, DECISION_LOG `2026-11-03T18:45:00Z` item (4): *"when the time comes ask agaian."* = DEFERRED. The master must re-ask before any High run is planned.
- (iii) 2026-11-03 rulings: no Portara purchase at $695 (DECISION_LOG `2026-11-03T18:40:00Z` item (1)). Cheaper or free tick-source search is research only (`2026-11-03T18:50:00Z` item (1); that scope was set by the master). Amear said "$700"; the declined Portara price was $695. Whether the two refer to the same offer is not decided here.

**S6 cross-block — no block's spec changes:**
- **F1** (`specs/SPEC_RUBRIC.md:17-28`), **F2** (`:30-43`), **F4** (`:59-70`): untouched. FROZEN.
- **F3** (`specs/SPEC_RUBRIC.md:45-57`): untouched. FROZEN. The void clause of D-2026-10-30-A stands.
- No code, template or config changed. Nothing here claims any F advanced.

**NEEDS AMEAR (questions only, not answered):** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
1. What counts as "proof of concept"? (His words name no test; the brief's framing ties it to Standard-resolution results.)
2. `Praxis_build-r8j` is at P0, the master's choice (D-2026-11-02-C, DECISIONS.md:489; NEEDS AMEAR 13). Is P0 the level he wants?

## 2026-11-04 — D-2026-11-04-B: R-1104-1 — commit gate accepts a praxis-auditor PASS (SubagentStop minter, provenance-checked) and a `GIT_INDEX_FILE=<abs path>` temp-index commit

**Date:** 2026-11-04 (written 2026-11-04T20:31Z, BEFORE any hook edit, per S4)
**Status:** DESIGN — specified, not yet implemented or tested at the time of writing. Filed by praxis-manager, unit `2026-11-04-gate-r1104-1`.
**Authorisation chain (S4/S5):**
- Amear, R-1104-1: *"I'm giving the agent permission to commit."* (D-2026-11-04-A; DECISION_LOG `2026-11-04T17:27:42Z`).
- Amear, DECISION_LOG `2026-11-04T20:25:10Z` (WHO: amear, AskUserQuestion button): *"Yes, change the gate"* = change the commit gate so Code can commit its own audited work after praxis-auditor passes it.
- Dispatch: DECISION_LOG `2026-11-04T20:25:33Z` (WHO: praxis-master) — this unit.
- Constraint carried: the old 12-path staged set in the real index stays "as is" (DECISION_LOG `2026-11-03T18:50:00Z` item (3)); hence temp-index commits.

**Problem (from the brief, re-read by the filer):** `.claude/hooks/gate-commit.sh:152-179` honours only a token minted by `audit-approve.sh`, which only `orchestrator-auditor` runs; that agent is not spawnable from the praxis-master roster, so no master commit can pass. The gate also hashes the REAL index only (line 152), so a temp-index commit would be checked against the wrong diff.

**Design.**
1. **Auditor output contract** (`.claude/agents/praxis-auditor.md`): when asked to authorise a commit, the auditor computes the hash itself and ends its final message with three bare lines: `VERDICT: PASS`, `COMMIT-INDEX: REAL` or `COMMIT-INDEX: <absolute index path>`, `COMMIT-DIFF-SHA256: <64 hex>` (sha256 of the cached diff under that index).
2. **Minter** `.claude/hooks/auditor-mint.sh`, registered on `SubagentStop` with matcher `^praxis-auditor$`. It re-checks `agent_type == praxis-auditor` itself, parses `last_assistant_message` (exactly one VERDICT line and it is PASS; exactly one of each COMMIT- line), recomputes the hash of the named index vs HEAD and mints only on an exact match of a non-empty diff. Token `.claude/state/audit-pass-<hash>` carries `tree=`, `index=`, `minter=praxis-auditor`, `agent_id=`, `agent_transcript=`, `parent_transcript=`; AUDIT_LOG row `<ts> praxis-auditor:<agent_id> <hash> PASS index=<..>`. Always exits 0 (never blocks a stop).
3. **Provenance check** (shared lib `.claude/hooks/audit-provenance.sh`, used at mint AND at commit): the agent transcript must be `$HOME/.claude/projects/<slug>/<session>/subagents/agent-<agent_id>.jsonl`; its sibling `.meta.json` must say `agentType` praxis-auditor, `spawnDepth` 1; its `toolUseId` must appear in the parent session transcript `<slug>/<session>.jsonl` as an `Agent` tool_use with `subagent_type` praxis-auditor; the agent transcript must contain the `COMMIT-DIFF-SHA256: <hash>` line. So a mint needs a harness-written auditor transcript spawned from the main thread (depth 1), not by a producer (depth 2).
4. **Gate** `.claude/hooks/gate-commit.sh`: accepts `GIT_INDEX_FILE=<absolute unquoted path>` followed directly by the commit invocation as the whole command (any other appearance of `INDEX_FILE`, or the variable set in the hook's own env, denies fail-closed); hashes and write-trees THAT index; the token's `index=` must equal the commit's index (legacy tokens = REAL). praxis-auditor tokens are re-verified (provenance, and parent transcript == the committing payload's `transcript_path`). A main-thread `praxis-master` caller is accepted ONLY with a provenance-verified praxis-auditor token — a legacy `audit-approve.sh` token is refused for it, so running audit-approve.sh by hand does not let the master commit. Legacy route unchanged for every other caller (orchestrator-auditor route preserved). Pathspec, `-a`/`--all`/`--amend`, one-commit-per-call, single-session and tree binding unchanged. Token stays single-use (deleted at allow).
5. **Tripwire** `scripts/mint-guard.sh` (PreToolUse `Bash|Write|Edit|NotebookEdit`): any `praxis-*` caller is denied a Bash command naming `audit-approve`, `auditor-mint`, `audit-provenance` or `audit-pass-`, a Bash write form on `AUDIT_LOG`, or a Write/Edit to `AUDIT_LOG.md` or `.claude/state/audit-pass-*`. A tripwire, not a wall: string obfuscation evades it.

**What this does NOT prevent (stated up front):** every actor runs as the same uid with Bash. A producer or the master that fabricates a meta file, a subagent transcript AND a matching tool_use line in the live session transcript can still forge a mint; this design turns that into a multi-file forgery of harness-owned files instead of one `audit-approve.sh` call. Hooks also run from the working tree, so a producer that edits the minter or gate changes enforcement live, before any audit.

**Out of scope, interactions noted only:** `Praxis_build-hwk` (quoted-subcommand evasion still evades the gate), `-nvn`, `-22q`.

**D-2026-11-04-B addendum — deviations from the design above (appended 2026-11-04T21:34:49Z, AFTER the fix work; S4 timing NOT met for these items, stated rather than hidden).** Same authorisation chain as above (R-1104-1; DECISION_LOG `2026-11-04T20:25:10Z`, `20:25:33Z`). Each item closes a break that an adversarial worker in this unit demonstrated against scratch copies (report `docs/reports/2026-11-04-gate-r1104-1-manager.md`):
- Canonical hash command everywhere (lib, gate, `audit-approve.sh`, auditor def) is `git diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative`. A plain cached diff could be hidden by diff.external, textconv, binary attributes, ignoreSubmodules or diff.relative. `audit-approve.sh` changed accordingly; the legacy route still works.
- Minter: the three lines must be the last three lines; exactly one line anywhere containing VERDICT / COMMIT-INDEX / COMMIT-DIFF-SHA256; refuse if the words FAIL*, UNVERIFIABLE or BLOCKED appear anywhere. The transcript-text check is skipped at mint time (flush order unverified) and enforced at commit time. Refuse if the git toplevel is not ROOT.
- Gate, stack master only: the whole command must be `[GIT_INDEX_FILE=<abs path> ]git commit` followed only by `-m <msg>` pairs. Unquoted characters are allowlisted. The payload `cwd` and the git toplevel must equal ROOT. The effective git hooks dir must match HEAD (it lives at `.beads/hooks` in this repo). At commit time, the parent transcript must hold the harness's Agent tool_result stub (column-0 `agentId: <aid>`) for the meta toolUseId, plus the hash line in that result or in the `<agent-message from="<aid>">` hand-back (a `user` record or a `queued_command` attachment).
- New `scripts/commit-tree-verify.sh` (PostToolUse Bash). It compares the new HEAD tree with the tree the gate allowed. This is detection only: it cannot undo a commit.
- mint-guard now also covers `orchestrator-active`, `last-allowed`, `mint-log`, `.beads/hooks/` and `shell-snapshots`, with paths normalised.

## 2026-11-05 — D-2026-11-05-A: Walk-forward design rulings (Amear, voice 2026-11-05)

**Date:** 2026-11-05
**Status:** RULED by Amear — items 1–5, graded REPORTED BY the voice agent. The text is the voice agent's record of his rulings, pasted by Amear with "file as WHO: amear". Ledger authorisation (S5): DECISION_LOG `2026-11-05T23:40:21Z` (WHO: amear). Appended 2026-11-05 by praxis-manager, unit `2026-11-05-addendum-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades:** REPORTED BY the voice agent = the five quoted items below, copied character for character from the `23:40:21Z` row. They are the voice agent's record, not a transcript of Amear's speech. Master's reading = the row's text marked "flagged not decided"; it is not Amear's words. The pointers below are the filer's, to existing repo text; they rule nothing.

**The five items, verbatim from the row (REPORTED BY the voice agent, pasted by Amear with "file as WHO: amear"):**
- *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
- *"2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."*
- *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
- *"4. Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."*
- *"5. Account tier: no decision until backtest + paper results exist."*

**Interactions — stated, not resolved.** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- (i) O1 (`specs/SPEC_RUBRIC.md:74-79`) and D-2026-11-02-C NEEDS AMEAR 1–2 (DECISIONS.md:531-532): the gate set, and whether walk-forward efficiency ≥ 0.50 applies. Per the master's reading, items (1a)/(1b) speak to these: "(a) has no optimisation step, (b) does". The row does not say which gates apply to which arm. O1 stays OPEN.
- (ii) Report C (`docs/reports/2026-11-04-proof-of-concept-standard.md:248`) NEEDS AMEAR 2, the equity base for "max DD ≤ 4% of equity". The master's reading says item 3 answers it, and summary v2 item 5, in part, and that "the MFFU account size itself is still not on the ledger". Report C:248 mentions "the MFFU $1,500 EOD trailing DD"; this entry does not adopt that figure as the limit.
- (iii) Report C §3 (`:144`): tick data becomes a prerequisite once a resting stop or target exists (`:170`). Report C grades this INFERRED: `:170` sits under the heading at `:165`, "Answer (INFERRED from the code, the vendor document and the reproduction; untested in NinjaTrader because no High run exists)", and summary item 5 (`:17`) reads "INFERRED; untested in NinjaTrader". Item 1(b) adds a stop; the master's reading calls it a resting order. Per the master's reading, this interaction "is put back to Amear, not resolved" (see also C NEEDS AMEAR 11, `:257`).
- (iv) Bead `Praxis_build-r8j` is P0, the master's choice, not confirmed by Amear (D-2026-11-04-A NEEDS AMEAR 2). `bd show` on 2026-11-05 reads "P0 · OPEN". Per the master's reading, walk-forward still waits on it, and on the data-quality items that C NEEDS AMEAR 7 (`:253`) leaves to Amear: 33 missing sessions and the 12:15 template.
- (v) Per the master's reading, item 1(b) authorises a stop in the strategy on its own branch in principle, but no build is dispatched. This entry dispatches no build and creates no branch. The master's reading also states: "Nothing here authorises a purchase, an import or a run."

**S6 cross-block — no block's spec changes:**
- **F1** (`specs/SPEC_RUBRIC.md:17`), **F2** (`:30`), **F3** (`:45`), **F4** (`:59`): untouched. No code, template or config changed. Nothing here claims any F advanced.

**NEEDS AMEAR (questions only, not answered):**
1. Which MFFU account size and which tier limits are to be used for items 3 and 4, given that item 5 defers the account-tier decision until backtest and paper results exist?
2. Does arm (b) run on minute data, given its stop (report C NEEDS AMEAR 11)?
3. What is the candidate set for the exit-policy parameter in item 1(b)?
4. Is R-1104-3's judged version arm (a), arm (b) or both?

## 2026-11-05 — D-2026-11-04-B addendum 2 (R-VN4-10, R-VN4-9)

**D-2026-11-04-B addendum 2 — R-VN4-10 (minter PASS signal) and R-VN4-9 (same-uid residual) (appended 2026-11-05T23:55Z, BEFORE the minter edit, per S4; correction unit `2026-11-04-gate-r1104-1` correction 1).**
**Authorisation chain (S4/S5):**
- Amear, R-VN4-10, DECISION_LOG `2026-11-05T23:51:21Z` (WHO: amear; REPORTED BY the voice agent, from `docs/reports/2026-11-04-voice-session-notes-4.md`): *"Use common sense and just give it the label that would make the least amount of mistakes … we need a system that has very specific description … We're not here to fuck around."* The voice agent's reading: cite rule ID and exact wording; the PASS signal is one fixed structured verdict line, not a word search.
- **The change below is the master's reading, flagged as a reading and not Amear's words** (same row): *"drop the minter's FAIL-word filter and rely on the exact `VERDICT: PASS` + COMMIT-INDEX + COMMIT-DIFF-SHA256 lines; quoting a criterion's text must not block a mint"*.
- Dispatch: DECISION_LOG `2026-11-05T23:51:21Z` (WHO: praxis-master) item (2).
- Amear, R-VN4-9, same row: *"Yeah, I do."* (accepts the same-uid residual for now).

**Change (minter `.claude/hooks/auditor-mint.sh` only):** rule (c) is removed. That rule refused when FAIL as a word start, UNVERIFIABLE or BLOCKED appeared anywhere in the message. Every other check is kept unchanged:
- (a) exactly one line anywhere (any case) contains VERDICT, one contains COMMIT-INDEX, and one contains COMMIT-DIFF-SHA256;
- (b) the last three lines are exactly `VERDICT: PASS` / `COMMIT-INDEX: <REAL|/abs/path>` / `COMMIT-DIFF-SHA256: <64 hex>`;
- the NUL refusal, the toplevel check, the hash recompute on a non-empty diff, and provenance.

Gate, provenance library, tripwire and verifier are not changed.

**Consequences, stated before the work:**
1. A PASS message that quotes a criterion containing "fail"/"failure" (e.g. S2's text) now mints.
2. **Attacks A6a/A6b (W10, 2026-11-04) are re-opened by design.** A FAIL written in prose without the word VERDICT ("FAIL R2", "Result: FAIL"), followed by the contract block, mints again. Under R-VN4-10 the structured verdict line is the PASS signal. An auditor that writes FAIL in prose and then emits `VERDICT: PASS` is an auditor-honesty fault, the same class as the already-residual W14 F1. The minter does not judge it.
3. A7 (`VERDICT: FAIL` plus a quoted PASS block) stays closed by rule (a). `VERDICT: FAIL` as the verdict line stays refused by rule (b).
4. Rule (a) still refuses a message where the word VERDICT appears on any second line, including a quotation. The auditor contract note says so.
5. Regression rows are added to the scratch matrix (PASS with "failure" in its body mints; last three lines not the contract → none; `VERDICT: FAIL` → none), and the A6a/A6b rows flip to the expected `minted`.

**R-VN4-9:** the same-uid forgery residual (report `docs/reports/2026-11-04-gate-r1104-1-manager.md` §Residual risks, first item) is accepted by Amear for now. No code change. The residual stays documented, as accepted rather than closed.

## 2026-11-06 — D-2026-11-04-B addendum 3 (look-alike verdict lines, W18 B1/B3)

**D-2026-11-04-B addendum 3: look-alike VERDICT lines (appended 2026-11-06T00:18Z, BEFORE the minter edit, per S4; correction unit `2026-11-04-gate-r1104-1`, correction 1b).**
**Authorisation chain (S4/S5):**
- Amear, R-VN4-10, DECISION_LOG `2026-11-05T23:51:21Z` (WHO: amear; REPORTED BY the voice agent): *"we need a system that has very specific description"*.
- Finding: W18 B1, OBSERVED (`docs/reports/2026-11-04-gate-r1104-1-manager.md` §Correction 1). A `VERDICT: FAIL` line spelled with a look-alike, zero-width or fullwidth letter, followed by the real three-line block, mints (`[M15-cyrillic-E-FAIL] … MINTED`). This falsifies addendum 2, consequence 3 ("A7 … stays closed by rule (a)") for any non-ASCII spelling. **This entry corrects that sentence.** Addendum 2 is not edited.
- Dispatch: the master's correction-1b brief to praxis-manager, 2026-11-06. Items (1) to (3) below are that brief's, which is the master's reading and not Amear's words.

**Change (minter `.claude/hooks/auditor-mint.sh` only):**
1. **Final three lines must be pure printable ASCII.** Take the raw `last_assistant_message`, split it on LF, and drop trailing lines that are empty or contain only spaces. Each of the last three lines must then consist only of bytes 0x20–0x7E. Any byte ≥ 0x80, and any control character (including CR, TAB, VT and FF), is refused. Also, `LC_ALL=C` is exported at the top of the script. The existing trailing-whitespace strip therefore no longer depends on locale (closes W18 B3: NBSP minted under UTF-8 and was refused under C).
2. **One verdict line in total, and it is the PASS line.** Each line of the message is folded as follows: delete Unicode format characters (U+200B–U+200F, U+2060–U+2064 and U+FEFF, as the brief lists, plus every other general-category Cf character and U+00AD); apply NFKC; delete combining marks (category Mn/Me). In the folded line, any non-ASCII **letter** (category L*) counts as a stand-in for any letter of VERDICT, and `1`, `l` and `|` count as stand-ins for `I`. A line is a **verdict line** if the folded text contains V-E-R-D-I-C-T (case-insensitive, those stand-ins allowed) **anywhere** in the line. The minter refuses unless exactly one line is a verdict line and that line is the raw third-from-last line `VERDICT: PASS`.
3. Everything else is kept unchanged, including rule (a) (the ASCII count) and rule (b) (the exact last three lines).

**Definition chosen, and a conflict flagged to the master.** The brief documents the verdict line as `^\s*VERDICT\s*:` after folding, which is an anchored pattern. It also states rule (2) as "/verdict/i" (unanchored), and it keeps rule (a) (unanchored). The anchored form alone would let `**VERDICT: FAIL**` through after folding (attack A7-bold). The minter therefore uses the **unanchored** form, which fails closed. Consequence: a PASS message that quotes prose containing "verdict" is still refused (false deny 2 is retained; rule (a) already refused it). **Master: confirm or overrule.**

**Consequences, stated before the work:**
1. Fullwidth, zero-width-split and Cyrillic/Greek look-alike `VERDICT: FAIL` lines, followed by the real block, are refused.
2. A `<SPOKEN>` block after the contract is still refused, by design: the three lines must be last. Auditors are briefed to omit the SPOKEN block in authorising audits; a SPOKEN block placed before the contract still mints.
3. New false-deny class: a line that contains seven consecutive non-ASCII letters (e.g. a Cyrillic or CJK word). Auditor reports are English, so this is accepted.
4. Residual, not closed: an ASCII spelling with separators (`V E R D I C T`, `V.E.R.D.I.C.T`) or other ASCII look-alikes beyond I→1/l/|. Same auditor-honesty class as W14 F1 and A6.
5. The gate, the provenance library, the tripwire and the verifier are not changed.

## 2026-11-05 — D-2026-11-05-C: Phase 3 spec import (r8j) and walk-forward spec

**Date:** 2026-11-05
**Status:** FILED by praxis-manager, unit `2026-11-05-r8j-phase3-import-and-wf-spec` (bead `Praxis_build-r8j`, P0). Not audited when this entry was written; the master-spawned auditor grades it. Neither file below has been ruled on as a whole by Amear.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Authorisation chain (S4/S5):**
- Amear, DECISION_LOG `2026-11-05T23:50:09Z` (WHO: amear, typed), item b: *"b. r8j (P0): import the Phase 3 spec into the repo; derive the walk-forward spec from the 2026-11-05 addendum (both arms, 252/63/63, DD gate = lower of 4% of MFFU account or MFFU trailing limit, per-window DD at 1 MNQ and 1 NQ vs every MFFU tier). Audit, commit."*
- Amear, R-VN4-4 (r8j at P0): *"Yes."* (DECISION_LOG `2026-11-05T23:51:21Z`, WHO: amear; REPORTED BY the voice agent).
- Dispatch: DECISION_LOG `2026-11-05T23:55:05Z` (WHO: praxis-master).

**Files (new; untracked and unstaged at time of entry):**
1. `docs/specs/2026-11-05-phase3-build-specification.md`: 188 lines / 3,360 words, sha256 `cd02d34ae635626e674f4316bdfd9ac14d96f819aaf28d39b7d651607be69b83`. This is an import of the gitignored source `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf`, read on 2026-11-05 as `textutil` plaintext: 111 lines / 2,350 words, sha256 `d149bc8e11b18cd9db075dd4ad19c9ecea53b1f8e3c5460fcf583b83bc888de5`. Its body is identical to the parked conversion: `diff` against `git show f258a5d:docs/specs/2026-08-06-phase3-build-specification.md` exits 0. Normalised per-item diffs against the source exit 0 for all nine breakers, the Block-2 pass gates and the Block-4 gate text. Breaker #5 was compared only from its em dash on. The nine breakers are SPECIFIED ONLY, with zero implemented. That basis and its scope are stated in the file's STATUS note.
2. `docs/specs/2026-11-05-walk-forward-spec.md`: 224 lines / 5,544 words, sha256 `b4341724134b0af1c2b268c7c38952f7f75cc801d84c72c61aad5ec0020d8645`. Status: DERIVED. It covers:
   - arms (a) and (b), the 252/63/63 windows (day-count convention INFERRED) and the existing 1-minute data as is;
   - the DD-gate base, as a per-tier table from MFFU's own pages fetched 2026-11-05 (REPORTED BY MFFU's pages, no tier chosen);
   - the per-window 1 MNQ / 1 NQ drawdown reporting and the six Block-2 gates, verbatim.
   Its section `## NEEDS AMEAR` holds questions 1–29.
3. `docs/reports/2026-11-05-r8j-phase3-import-and-wf-spec-manager.md`: the unit's manager report and evidence.

**Parked history:**
- `r8j` was parked on 2026-08-07 at audit FAIL ×2 (`parked/Praxis_build-r8j`, `f258a5d`). The blocking finding was an arithmetic error in a byte-offset locator table in that unit's report; the auditor confirmed the spec conversion byte-correct.
- This unit used new paths only and contains no byte-offset table. It left these untouched: the parked branch, `docs/reports/2026-08-06-session42-r8j-phase3-import.md` and the `docs/reports/2026-08-07-session44-r8j-*` files.
- The de-identification rule for breaker #5 is kept. Its ruling, DECISION_LOG `2026-08-06T20:18:56Z` (WHO: amear), is on main. The entry that recorded it, `D-2026-08-06-A`, exists only at `f258a5d`, not in this file on main.

**Rulings the files cite (no new ruling made here):**
- Ruling 1 (`2026-11-05T23:50:09Z`, typed): *"Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest."*
- From `2026-11-05T23:51:21Z` (REPORTED BY the voice agent): R-VN4-2, R-VN4-3, R-VN4-5 and R-VN4-7.
- D-2026-11-05-A items 1–5.
- D-2026-11-02-C: R-VN3-3 (data as is) and R-VN3-6. R-VN3-5 (breakers on once built) is graded there as the agent's reading, confirmed by Amear in voice only.
- D-2026-10-30-A, Status CONDITIONAL.

**Deviations from the plan:** none made by this unit. The import's header notes are labelled additions. The import changes no design text, and the walk-forward spec adopts no unruled choice.

**S6 cross-block:**
- F1, F2, F3 and F4 are neither discharged nor changed. No code, hook or config was edited by this unit: `git diff --quiet HEAD -- ninjascript/` exits 0.
- O1 and O4 stay OPEN.
- The walk-forward spec touches Block 2 (gates, windows, configuration), Block 3 (how breakers are modelled in a backtest, quoted from ruling 1 only) and Block 4 (the O4 parity gate, left open). It touches the account tier only as a table, under item 5.

**NEEDS AMEAR:** see `docs/specs/2026-11-05-walk-forward-spec.md`, section `## NEEDS AMEAR`, items 1–29 (questions only; none answered here).

**Open for the master (not decided here):** whether `D-2026-08-06-A` is carried from `f258a5d` to `DECISIONS.md` on main.

## 2026-11-05 — D-2026-11-05-B: R-VN4-1..14 — voice session 2026-11-04 (filed 2026-11-06)

**Date:** 2026-11-06 (UTC; rulings spoken 2026-11-04 evening ET)
**Status:** RULED by Amear — R-VN4-1..14, graded REPORTED BY the voice agent. The notes (`docs/reports/2026-11-04-voice-session-notes-4.md:3`) say *"Rulings are Amear's, quoted or closely paraphrased; Claude's readings are labelled."* Ledger authorisation (S5): DECISION_LOG `2026-11-05T23:51:21Z` (WHO: amear). Appended by praxis-manager, unit `2026-11-06-rvn4-filing`, under R-1104-2 (housekeeping).
**Filing delay, stated plainly:** this entry was queued at `2026-11-05T23:51:21Z` (WHO: praxis-master, item 3: "DECISIONS entry D-2026-11-05-B queued after the gate correction") and was not dispatched until `2026-11-06T01:07:39Z`. The omission was the master's; the status-refresh producer caught it (DECISION_LOG `2026-11-06T01:07:39Z`, item 2: "Master's omission").
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades:** *Amear's words* = the quoted text of each item below, copied character for character from the `23:51:21Z` row (extracted by script, not retyped). They are the voice agent's record, not a transcript of his speech. *Reading* = column 4 ("Ruling as read by Claude") of the notes-4 table, copied as written; it is the voice agent's reading, not Amear's words. *Master's reading, flagged* = text the master added in the row; it is not Amear's words. Where the row and notes-4 differ (joiners, emphasis, one added parenthetical), the row is the filed source; the differences are listed after the items.

**The 14 rulings (Amear's words verbatim from the `23:51:21Z` row):**
- **R-VN4-1** — GitHub login, future use: "Only within this directory."
  - reading (voice agent, notes-4): Agents may use his `gh` login only against the Praxis.build repo itself. Never for research reads of other people's repos. Past use (item 24): not ruled on further; no action requested.
- **R-VN4-2** — breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter."
  - reading (voice agent, notes-4): Bar-close checks (market-order flatten) in the backtest; resting stop orders once live. Claude noted the gap: the backtest then does not test live stop fills; paper trading (Block 4) covers it.
  - master's reading, flagged (row text, labelled there as the voice agent's reading): *"voice agent's reading: bar-close market flatten in the backtest, resting stops once live; confirmed by Amear's typed ruling 1 at 23:50:09Z"*. The clause "confirmed by Amear's typed ruling 1 at 23:50:09Z" is the master's link; the voice agent's notes predate that ruling.
- **R-VN4-3** — walk-forward on minute data: "Yes."
  - reading (voice agent, notes-4): Walk-forward runs on the existing 1-minute data. The spec's High/1-tick requirement is deferred, not deleted.
- **R-VN4-4** — r8j at P0: "Yes."
  - reading (voice agent, notes-4): **r8j confirmed P0 by Amear.**
- **R-VN4-5** — data gaps: "As long as the data that I generated came back similar to … what is found online, I'm happy to move on."
  - reading (voice agent, notes-4): 33 missing sessions and the 12:15 early-close exits are accepted as is. No fix before results are judged. Basis: baseline shape matches the published NQ replication (lower win rate, bigger winners), weaker.
- **R-VN4-6** — commission: "Put together whatever fees would make reasonable sense. Even if it's a range, as long as it's a tight range." / "Apply the best figure you can find to the data."
  - reading (voice agent, notes-4): Apply **$5.76 round trip all-in** ($2.88/side) in place of $2.96. Range $5.00–$5.80. Source: Tradeify's published NQ all-in and FundedNext's example (both REPORTED from web search in-call; MFFU's own fee page NOT read). **Code confirms against MFFU's fee page before the cost model changes; D-2026-10-30-A's cost model v1.1.0 is amended by a new DECISIONS entry, not edited.** Amear's expectation: prop sim accounts still deduct exchange/NFA/clearing fees from the sim balance (Claude: Topstep documents this; MFFU unverified). Effect on the baseline ≈ −$3,300 on 1,190 trades (Claude's arithmetic).
- **R-VN4-7** — proof of concept: "Proof of concept is having the full trading pipeline existing and having it run in real live markets on a sim account." / "We're just gonna proceed without that [historical tick data]."
  - reading (voice agent, notes-4): **R-1104-3 defined:** PoC = full pipeline (TradingView → n8n → NT8 → Rithmic → MFFU sim) running on sim in live markets = Block 4. **No historical tick-data purchase; proceed without it.** The PROPOSED 12-item checklist from report C is not adopted; items 1–7, 10, 13–20 of v2 §5 are moot or deferred by this ruling.
- **R-VN4-8** — D-071: "Yes."
  - reading (voice agent, notes-4): **The MFFU Rithmic connection is approved to be opened when Block 4 starts.** D-071 (Simulated Data Feed only) stands until then.
- **R-VN4-9** — forgeable harness files: "Yeah, I do."
  - reading (voice agent, notes-4): Accepts the risk that anything running as his user can forge the gate's files, for now. Full closure (separate user/machine) deferred.
- **R-VN4-10** — rubric citation and PASS signal: "Use common sense and just give it the label that would make the least amount of mistakes … we need a system that has very specific description … We're not here to fuck around."
  - reading (voice agent, notes-4): Choose the format with the least room for error. Claude's reading, to be confirmed by the gate's producer: auditor cites **rule ID and exact wording**; PASS signal is **one fixed structured verdict line** (e.g. `Result: PASS`), not a word search.
  - master's reading, flagged (row text): *"drop the minter's FAIL-word filter and rely on the exact `VERDICT: PASS` + COMMIT-INDEX + COMMIT-DIFF-SHA256 lines; quoting a criterion's text must not block a mint"*. Not confirmed by Amear (NEEDS AMEAR 1).
- **R-VN4-11** — repo licences: "Yes to all."
  - reading (voice agent, notes-4): Code may borrow or re-implement from the researched repos **within each licence**. MIT: yes. No licence (e.g. skizzunni/money): read-only reference.
- **R-VN4-12** — borrowed code: "Can it just be put in there as a branch so there could be a distinction between the pre and post?"
  - reading (voice agent, notes-4): **Borrowed code lands on its own branch**, never straight onto `main`.
- **R-VN4-13** — NT8 add-ons: "Yeah, just do the snapshot."
  - reading (voice agent, notes-4): Add-ons may go on the Fusion install **after a VMware snapshot** of the VM; roll back if anything breaks.
- **R-VN4-14** — Mac↔VM sharing: "I want there to be file sharing between the Mac and the VM … I don't need them to be isolated right now as there's no live money being traded."
  - reading (voice agent, notes-4): **Now:** enable VMware Fusion shared folders (Praxis.build visible to the VM) to replace the Drive round trip. **Go-live checklist item (Block 5):** isolate the VM — remove the shared folder, no access to the main directory — before real money.

**Row vs notes-4, Amear's-words column:** identical for R-VN4-1, R-VN4-2, R-VN4-3, R-VN4-4, R-VN4-5, R-VN4-8, R-VN4-9, R-VN4-11, R-VN4-12, R-VN4-13, R-VN4-14; different for R-VN4-6, R-VN4-7, R-VN4-10. The differences are joiners and emphasis only (row ` / ` where notes-4 has `Then: ` or a space; notes-4 bolds the last sentence of R-VN4-10 and adds "(Amear asked to be quoted.)"). The text inside the quote marks is identical in both once notes-4's `**` bold markers are removed (script check).

**Interactions — stated, not resolved.** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- (i) R-VN4-2 and Amear's typed ruling 1 (DECISION_LOG `2026-11-05T23:50:09Z`, WHO: amear): *"Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4-7 stands."* It names R-VN4-2 and covers the backtest (bar-close check, market exit next bar). Per the reading, resting stops once live rest on R-VN4-2 alone; ruling 1 does not address live trading.
- (ii) R-VN4-3 and R-VN4-5 with D-2026-11-05-A (DECISIONS.md:803) and D-2026-11-05-C (DECISIONS.md:881): walk-forward on the existing minute data; the data is used as is (33 missing sessions, 12:15 early-close exits). This entry changes neither.
- (iii) R-VN4-6 with the fee report (`docs/reports/2026-11-05-mffu-fee-check.md:7-10`): MFFU's own page gives NQ $4.68 round trip (MNQ $1.90), not $5.76; $5.76 on that page is YM. The cost model stays $2.96 (D-2026-10-30-A unchanged) pending Amear (DECISION_LOG `2026-11-05T23:59:40Z`, `2026-11-06T00:06:48Z`; fee report NEEDS AMEAR at `:131`).
- (iv) R-VN4-7 with R-1104-3 (D-2026-11-04-A, DECISIONS.md:752): per the reading, proof of concept is Block 4 on sim; no tick-data purchase. Report C's PROPOSED checklist is not adopted. Ruling 1 (above) also says "R-VN4-7 stands."
- (v) R-VN4-8 with D-071: per the reading, the MFFU Rithmic connection is approved only when Block 4 starts; D-071 stands until then. DECISIONS.md has no D-071 entry heading (`grep -c '^#.*D-071'` = 0); its in-repo pointer is DECISION_LOG `2026-10-20T15:55:42Z` (line 424).
- (vi) R-VN4-9 and R-VN4-10 with D-2026-11-04-B addendum 2 (DECISIONS.md:834) and addendum 3 (DECISIONS.md:859): both were applied in the gate correction unit, which is now PARKED at FAIL 2 (DECISION_LOG `2026-11-06T00:54:04Z`). This entry neither re-opens nor ratifies that unit.
- (vii) R-VN4-11 and R-VN4-12 with the comparable-builds report (`docs/reports/2026-11-04-comparable-builds.md`): per the readings, borrowing is within each licence (e.g. eman007/cli-nt-bridge MIT, `:65`; skizzunni/money, `:47`, no LICENSE file, `:64`, read-only) and borrowed code goes on its own branch, never straight onto `main`. Amear's R-VN4-12 words are a question; the branch rule is the reading. No code is borrowed and no branch is made by this entry.
- (viii) R-VN4-13: add-ons only after a VMware snapshot of the VM. No snapshot is taken and no add-on is installed by this entry.
- (ix) R-VN4-14 with the Fusion walkthrough (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md:5`, `:8`): VMware says Shared Folder is unsupported for Windows 11 ARM guests on Apple Silicon. Question 0 in that walkthrough is open.

**Not ruled (stay open, from notes-4 `## Not ruled on`):** past use of the GitHub login (item 24; no remedy requested); second Rithmic read-only connection (item 23); CME Atlassian wiki as a source (item 19); equity base for the 4% DD gate (item 5) and Sharpe definition (item 4); O1 gate set / WFE with no optimisation (item 6).

**S6 cross-block — no block's spec changes:**
- **F1** (`specs/SPEC_RUBRIC.md:17`), **F2** (`:30`), **F3** (`:45`), **F4** (`:59`): untouched by this filing. No code, template, hook or config changed. Nothing here claims any F advanced.

**NEEDS AMEAR (pointers and questions only, not answered):**
1. R-VN4-10: is the master's reading (drop the FAIL-word filter; rely on the exact `VERDICT: PASS` + COMMIT-INDEX + COMMIT-DIFF-SHA256 lines) what you meant, or should it be corrected?
2. R-VN4-6: which fee figure applies — see `docs/reports/2026-11-05-mffu-fee-check.md:131` (NEEDS AMEAR 1–3 there).
3. R-VN4-14: Question 0 in `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md:8`.
4. The five "Not ruled" items above.

**D-2026-11-05-B note 1 (2026-11-06, after audit):** (iv) "Report C's PROPOSED checklist is not adopted" is the voice agent's reading of R-VN4-7, not Amear's words. (v) "approved only when Block 4 starts" — the word "only" is the filer's; the reading in notes-4 is "approved to be opened when Block 4 starts". The standing-limitation sentence in the Interactions heading is carried by convention and decides nothing.

## 2026-11-06 — D-2026-11-06-A: Amear's voice notes of 2026-11-06 (NT8 version; in-VM automation lift conditions; SMB file sharing; open items)

**Date:** 2026-11-06
**Status:** RECORDED — Amear's notes, WHO: amear, pasted into the Code session with "file as WHO: amear". Source row and ledger authorisation (S5): DECISION_LOG `2026-11-06T15:15:30Z` (**WHO: amear**), committed in `cca7c6e` (`git show cca7c6e:DECISION_LOG.md`, line 463). Dispatch: DECISION_LOG `2026-11-06T15:28:29Z` (WHO: praxis-master; working tree, not yet in a commit). Appended by praxis-manager, unit `2026-11-06-voice-notes-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades:** *Amear's words* = the four items below, copied byte for byte from the quoted text of the committed `15:15:30Z` row (extracted by script, not retyped). The row says the paste carries no clock. Every fact in them about NT8, the VM and the share is REPORTED BY amear; Code has not observed the NT8 version, the VM or the share. The 2a figures are set against a committed CSV readback below. *Master's reading* = the row's text after the quote, which the row labels "flagged as a reading (not his words)"; where cited below it is marked "master's reading (DECISION_LOG 15:15:30Z), not Amear's words". The pointers are the filer's, to existing repo text; they rule nothing.

**The four items, verbatim from the committed row (WHO: amear).** One item per line; in the row the items are joined by a single space. A text block is used so the UNC path's backslashes show as written.

```text
1. NinjaTrader: Amear updated NT8 before the committed runs; he says the committed numbers already come from the new version. Code: read and record the exact version on the VM's next touch.
2. In-VM automation (Oct 28 ruling): lifted COMPLETELY once two tests pass; until then it stands. a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. b. The VM agent loads a written skill and follows it correctly on a simple job. First confirm the VM's Cowork agent can load skills. Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy.
3. File sharing: Fusion shared folders unavailable (no Sharing pane, as flagged). SMB route done by hand: Mac File Sharing on; Praxis.build shared; admin Read & Write; staff Read Only; Everyone No Access. VM: \\192.168.1.204\Praxis.build mapped as Z:, reconnect at sign-in, credentials remembered. Amear confirmed the folders show. Replaces the Google Drive round trip. Go-live checklist: unmap Z: and turn the share off before real money.
4. Still open from the 11-06 handoff, not discussed today: MFFU fees ($4.68 NQ / $1.90 MNQ; the $5.76 given in voice was YM, Claude's error); commit-gate park and the provenance denial; walk-forward arm (b) settings; which arm is judged.
```

**Structured record — pointers and effects only; nothing here rules:**
- **Item 1 — NT8 version.** REPORTED BY amear: NT8 was updated before the committed runs, and the committed numbers come from the new version. Prior repo record: the 2026-10-28 ruling (4), "stay on 8.1.7.2 until the backtest runs clean" (DECISION_LOG `2026-10-30T21:36:00Z`, WHO: amear); then `docs/reports/2026-10-31-voice-session-notes-2.md:161`, "The NT8 version reads 8.1.8.4." and "C4 ran on 8.1.8.4." (REPORTED); and `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md:23`, "NT8 is 8.1.8.4, which he updated himself." No Code observation of the version exists. **Action owed (his words):** "read and record the exact version on the VM's next touch". Master's reading (DECISION_LOG 15:15:30Z), not Amear's words: "Item 1 is a VM-touch task that Code cannot perform (no VM access)". **State: pending** (master's reading: "it is logged as pending for whoever next touches the VM"; NEEDS AMEAR 7).
- **Item 2 — in-VM automation.** The "Oct 28 ruling" is ruling (1) of `docs/reports/2026-10-28-voice-session-notes.md:7` (untracked file), "The in-VM automation approach is dropped. No more Cowork or in-VM Claude Code executor work.", taken onto the ledger at DECISION_LOG `2026-10-30T21:36:00Z` (WHO: amear). (filer's identification) DECISIONS.md has no entry for it. In his words it is "lifted COMPLETELY once two tests pass; until then it stands." How far "COMPLETELY" reaches beyond that ruling is not stated (NEEDS AMEAR 6). The two tests:
  - **2a** — cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. Those are his REPORTED figures. The committed baseline record is `docs/reports/2026-11-01-three-strategy-results.md:73` (committed in `8ca9861`): `| All | 1190 | $197327.60 | …`, instrument `NQCONTROW SEP25` (`:86`); `:67` grades the CSV values OBSERVED and the `amear=` values REPORTED BY AMEAR. The repo's record of the bridge (its code is not in the repo): `docs/reports/2026-11-04-comparable-builds.md:65`, eman007/cli-nt-bridge, MIT, "implemented; untested on 8.1.7.2".
  - **2b** — the VM agent loads a written skill and follows it correctly on a simple job, after first confirming that the VM's Cowork agent can load skills.
  - **Order he set:** read the bridge's code read-only → write an install walkthrough → VMware snapshot first → then install. Filer's pointer: R-VN4-13 is Amear's "Yeah, just do the snapshot." (DECISIONS.md:960); the voice agent's reading of it (`:961`, not his words) lets add-ons go on "after a VMware snapshot", and the bridge is recorded as a "third-party AddOn" (`docs/reports/2026-11-04-comparable-builds.md:216`). Whether R-VN4-13 covers the bridge is not ruled here.
  - **Direction he set:** the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy. The open question it bears on is the step-c harness question at DECISION_LOG `2026-11-06T00:54:04Z`: "arm (a) can only run in NT8 on the VM (barred overnight: "no NT8 runs or imports on the VM") or via a Mac-side Python harness, and choosing a harness over the spec's NT8 Strategy Analyzer run is a validation-method decision for Amear". Master's reading (DECISION_LOG 15:15:30Z), not Amear's words: "item 2 answers the step-c harness question from 00:54:04Z — NT8 on the VM through cli-nt-bridge, not a Mac Python harness — but the in-VM automation ban STANDS until tests 2a and 2b pass, so step c still cannot run". Step c is not run by this entry. Passing 2a and 2b is the condition his words set for the 2026-10-28 ruling; whether the `23:50:09Z` limit also has to be lifted before step c is NEEDS AMEAR 6.
  - **State:** the repo holds no specification of test 2a or 2b and no record of either being run. Nothing is downloaded, installed or run by this entry.
- **Item 3 — file sharing.** REPORTED BY amear, done by his hand: Mac File Sharing on; `Praxis.build` shared; `admin` Read & Write; `staff` Read Only; Everyone No Access; the VM maps `\\192.168.1.204\Praxis.build` as `Z:`, reconnect at sign-in, credentials remembered; he confirmed the folders show. Code has not opened, probed or tested the share or the path.
  - **Walkthrough** `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`: Question 0 (`:8`) ends "Try these steps / D-072 SMB / keep Google Drive `praxis-tickprep`? Your call; nothing chosen." Questions 1–3 are at `:9-11` and the Steps at `:13-21`. REPORTED BY amear: "Fusion shared folders unavailable (no Sharing pane, as flagged)". Master's reading (DECISION_LOG 15:15:30Z), not Amear's words: "Item 3 closes Fusion Question 0 (SMB chosen and done by his hand; the walkthrough's Questions 1–3 are moot)". Whether Questions 0–3 are closed is put to him (NEEDS AMEAR 10). The walkthrough is not edited by this entry.
  - **Google Drive round trip:** his words, "Replaces the Google Drive round trip." Master's reading (DECISION_LOG 15:15:30Z), not Amear's words: it "supersedes the Google Drive `praxis-tickprep` round trip". Where the round trip is recorded: the R-VN4-14 reading, "to replace the Drive round trip" (DECISIONS.md:963; notes-4 `docs/reports/2026-11-04-voice-session-notes-4.md:26`); the VM handoffs that use the Drive `praxis-tickprep` folder, `docs/reports/2026-11-04-vm-handoff-readback-ticksource-exe.md:28` and `:53`, and `docs/reports/2026-11-02-vm-handoff-high-res-prep.md:18`. None of those files is edited.
  - **D-072:** a migration-ledger decision, not in this repo (walkthrough `:8`: "REPORTED; migration ledger, not this repo; user not created"). In this repo it is quoted at `docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md:59`: "D-072 item 7: a new low-privilege Mac user, `praxispush`, that can see only `~/praxis-signals`." The two records differ (both REPORTED): D-072 names the low-privilege user `praxispush` and `~/praxis-signals` only; item 3 shares `Praxis.build`, with `admin` Read & Write and `staff` Read Only. That the share is the repo root `/Volumes/Sensidine/Praxis.build` is the filer's inference from the name; item 3 does not give a path on the Mac.
  - **Go-live checklist (his words):** unmap `Z:` and turn the share off before real money. Recorded here only. The walkthrough's go-live line (`:26-27`, R-VN4-14) covers the Fusion shared folder and is not amended (NEEDS AMEAR 1).
- **Item 4 — still open (his list, "from the 11-06 handoff, not discussed today").** Each with where it is tracked; none is ruled here:
  - "MFFU fees ($4.68 NQ / $1.90 MNQ; the $5.76 given in voice was YM, Claude's error)" — the attribution of the error is his words. Tracked: `docs/reports/2026-11-05-mffu-fee-check.md:131-134` (NEEDS AMEAR 1–3); D-2026-11-05-B (iii), DECISIONS.md:970. The cost model is unchanged by this entry.
  - "commit-gate park and the provenance denial" — bead `Praxis_build-uqb` (`bd show`: "P0 · OPEN"); the park, DECISION_LOG `2026-11-06T00:54:04Z`; the provenance denials, `2026-11-06T00:50:30Z` and `2026-11-06T15:20:30Z` (two rows; his list says "the provenance denial"). The `15:20:30Z` row is in the DECISION_LOG working tree, not yet in a commit; the other two are in `cca7c6e`.
  - "walk-forward arm (b) settings" — `docs/specs/2026-11-05-walk-forward-spec.md` `## NEEDS AMEAR` (`:194`): items 1–6 (`:196-201`), 14 (`:209`), 27 (`:222`), 28 (`:223`).
  - "which arm is judged" — the same section, item 10 (`:205`); related items 9 (`:204`) and 25 (`:220`).

**Cross-references:**
- D-2026-11-05-A (DECISIONS.md:803) — walk-forward design, both arms.
- D-2026-11-05-B (DECISIONS.md:924) — R-VN4-13, "Yeah, just do the snapshot." (`:960`; the add-ons-after-snapshot ordering is the voice agent's reading, `:961`); R-VN4-14, file sharing (`:962`); the go-live isolation item is the voice agent's reading (`:963`).
- D-2026-11-05-C (DECISIONS.md:881) — Phase 3 spec import and the walk-forward spec.
- 2026-10-28 in-VM automation ruling — DECISION_LOG `2026-10-30T21:36:00Z` (WHO: amear), ruling (1); `docs/reports/2026-10-28-voice-session-notes.md:7`.
- D-071 (no new NT8 connection) — no DECISIONS.md heading; in-repo pointer DECISION_LOG `2026-10-20T15:55:42Z` (D-2026-11-05-B (v), DECISIONS.md:972).
- DECISION_LOG `2026-11-05T23:50:09Z` (WHO: amear) hard limits: "nothing bought, no new NT8 connection (D-071), no NT8 runs or imports on the VM, F1/F2/F4 untouched, no edits to main from borrowed code, …".
- **No limit is lifted by this entry.** The 2026-10-28 ruling, D-071 and the `23:50:09Z` hard limits all stand. Only Amear's words lift them. His words in item 2 set the conditions for lifting the 2026-10-28 ruling (2a and 2b both pass); they do not name D-071 or the `23:50:09Z` limits (NEEDS AMEAR 6).
- Master's reading (DECISION_LOG 15:15:30Z), not Amear's words: "the install itself is his hand step or the VM agent's, not Code's (D-071, "no NT8 runs or imports on the VM" from 2026-11-05T23:50:09Z stand until he lifts them)".

**S6 cross-block — no block's spec changes:**
- **F1** (`specs/SPEC_RUBRIC.md:17`), **F2** (`:30`), **F3** (`:45`), **F4** (`:59`): untouched by this filing. This filing changes no code, template, hook or config. Nothing here claims any F advanced.

**NEEDS AMEAR (questions only, not answered):**
1. Should the Fusion walkthrough's go-live section (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md:26-27`) be amended with your line "unmap Z: and turn the share off before real money"?
2. After the install walkthrough is written, who performs the install? (The master's reading names you by hand or the VM agent, not Code.)
3. What is "the VM's Cowork agent", where does it run, and where is its skills directory? (The filer cannot write test 2b's steps without it.)
4. For test 2a: is `docs/reports/2026-11-01-three-strategy-results.md:73` (1190 trades, $197327.60 net, `NQCONTROW SEP25`) the reference run, and does "reproduces" mean an exact match on trades and net, or a tolerance?
5. Should the rule that reports carry the standing limitation sentence (the sentence on this entry's **Standing limitation** line; today a master's standing instruction) be written into `specs/SPEC_RUBRIC.md`? REPORTED BY the flush auditor (DECISION_LOG `2026-11-06T15:19:51Z`, working tree, not yet in a commit): it "could not find the house rule written in CLAUDE.md/SPEC_RUBRIC/agents/runbooks — it lives in the master's standing instructions and in DECISION_LOG rows only". The dispatch row (`2026-11-06T15:28:29Z`) calls this "a spec change and therefore Amear's".
6. Does test 2a (as the filer reads it, an NT8 run on the VM driven through the bridge) need your separate lift of the `23:50:09Z` limit "no NT8 runs or imports on the VM", and of D-071 if the bridge needs a connection, or does item 2 cover them?
7. Item 1 says "Code: read and record the exact version on the VM's next touch." Per the master's reading (DECISION_LOG 15:15:30Z), Code has no VM access. Who reads the version on the VM (you or the VM agent) for Code to record?
8. Who judges that 2a and 2b have passed, and is the lift recorded by your own ledger row?
9. `CLAUDE.md:30` says not to "Run multiple Claude sessions against this working tree — one session per repo". Item 3 gives `admin` Read & Write and `staff` Read Only on the `Praxis.build` share, mapped on the VM as `Z:`; it does not say which account the VM signs in with. If a VM agent session can write in `Z:`, does that count as a second session against this working tree?
10. Does item 3 close the Fusion walkthrough's Question 0 (`:8`) and make its Questions 1–3 (`:9-11`) moot, as the master reads it? Question 0's SMB option was D-072's form (`praxispush`, `~/praxis-signals`); item 3 shares `Praxis.build`, with `admin` Read & Write.

## 2026-11-06 — D-2026-11-06-B: Amear's evening rulings 1–5 and loop a–e (voice, 2026-11-06)

**Date:** 2026-11-06
**Status:** RECORDED — Amear's rulings, WHO: amear. Source row and ledger authorisation (S5): DECISION_LOG `2026-11-06T20:08:28Z` (**WHO: amear**; in the DECISION_LOG working tree, not yet in a commit). The row says the paste carries no clock; the master read `date -u` at 20:08:28Z. Dispatch: DECISION_LOG `2026-11-06T20:12:00Z` (WHO: praxis-master). Appended by praxis-manager, unit `2026-11-06-rulings-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** *Amear's words* = the text block below, copied byte for byte by script from the quoted text of the `20:08:28Z` row (the part between `Text: "` and `" Master's readings`). *Master's readings* = the row's text after the quote, which the row flags "as readings"; they are quoted further down AS the master's readings, not as Amear's words. *Master's decision under delegation* = a settlement the master made under R-1104-2 (DECISIONS.md:748) after ruling 5 handed him the item; it is labelled as such and is not Amear's word. The pointers are the filer's.

**The paste, verbatim (WHO: amear).** One line, as in the row.

```text
Rulings 1. Bridge install (NEEDS AMEAR 2): the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot. 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself. 3. Commit gate: (a) RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit; (b) APPROVE the hook change so the gate accepts the auditor's async hand-back. First commit through it is the test; on failure, revert and I keep typing commits. 4. Walk-forward arm (b) and spec NEEDS AMEAR, under "We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05. Report the exact values chosen back to me. 5. Handoff NEEDS AMEAR 1, 3–10, 15–17, 19: housekeeping or already answered — settle under R-1104-2. Defaults: test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match; my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched; VM agent reads and reports the NT8 version; Code + auditor judge 2a/2b and log the lift under my ruling; VM agent on Z: while Code runs = second session, coordinate. Loop, in order a. Gate: fresh audit of uqb; hook change; first self-commit as the test. b. Commit fees amendment + these rulings. c. Finish the cli-nt-bridge code read; write the VM install walkthrough + test 2a/2b spec + the first skill(s) as one VM handoff file on Z:. Tell me its exact path so I can point the VM session at it. d. Arm (a) and (b) build per the spec, Mac side, ready to run through the bridge once 2a passes. e. STATUS/HANDOFF as you go; return handoff for the Claude.ai chat at the end — committed, built, blocked, and only decisions that are mine. Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit. If a step needs a ruling, log it, skip it, continue.
```

**Master's readings, verbatim from the same row, up to (not including) its closing "Standing limitation on every figure above" sentence (WHO: praxis-master; flagged there "as readings"; not Amear's words):**

```text
Master's readings, flagged as readings: (i) "Handoff NEEDS AMEAR 1, 3–10, 15–17, 19" refers to the numbering in `docs/reports/2026-11-06-voice-handoff-evening.md` §4 (1–10 = D-2026-11-06-A's ten; 11–19 carried) — so items 2 (who installs: ruled in 1), 11–12 (gate: ruled in 3), 13 (fees: ruled in 2), 14 (WF spec: ruled in 4), 18 (notes-4 not-ruled: still open) are handled or left as stated; (ii) ruling 3(a) ratifies the addendum's timing by his word — the filing unit writes that ratification as a WHO: amear addendum to D-2026-11-04-B, which is the named unblocking artifact for uqb; (iii) ruling 3(b) approves a code change to the gate hook — the first code change authorised since "Don't change the code without asking me"; its scope is exactly "accept the auditor's async hand-back", nothing else; (iv) ruling 4 sets defaults and asks for the exact values back — the master proposes values in the spec unit's report, he confirms; (v) "arm (a) and (b) build … Mac side, ready to run through the bridge once 2a passes" — the Mac-side build is strategy code on its own branch ("borrowed code on its own branch" applies to bridge-derived code; PRAXIS strategy changes — the tunables becoming inputs — are a code change he has now asked for in step d); (vi) the bridge-read index (`commit-idx-bridge`, PASS 20:08Z) is held as the candidate for the first self-commit test in step a; if the test fails he types it.
```

**Structured record, ruling by ruling.** "Does NOT lift" applies to every ruling: his words "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." No ruling below is read past its words.

- **Ruling 1 — bridge install.** *Rules:* "the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot." *Unlocks:* answers D-2026-11-06-A NEEDS AMEAR 2 ("who performs the install"). The order he set in D-2026-11-06-A item 2 still applies: code read → install walkthrough → VMware snapshot → install. *Does NOT lift:* the hard limits above; D-071; it does not say Code installs anything, and nothing is downloaded or installed by this entry.
- **Ruling 2 — fees.** *Rules:* "apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model." and "Covered by my earlier "apply the best figure" ruling; settle this class yourself." (the earlier ruling is R-VN4-6, DECISIONS.md:945). *Unlocks:* the cost-model amendment, D-2026-11-06-C below. "This class" is applied here only to the MFFU NQ/MNQ round-trip figures; how far it reaches beyond that is not stated in his words and is not extended here. *Does NOT lift:* F3 and D-2026-10-30-A (slippage 2 ticks/side, fill resolution Standard) are untouched.
- **Ruling 3 — commit gate.** *Rules:* (a) "RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit;" (b) "APPROVE the hook change so the gate accepts the auditor's async hand-back. First commit through it is the test; on failure, revert and I keep typing commits." *Unlocks:* (a) D-2026-11-04-B addendum 4 below, the named unblocking artifact for bead `Praxis_build-uqb`; (b) the hook change, in its own unit (`2026-11-06-gate-async-handback`), whose DECISIONS addendum is the master's later step and is not written here. *Does NOT lift:* (a) is a fresh audit, not a PASS; (b) is scoped by the master's reading (iii) to "accept the auditor's async hand-back", nothing else.
- **Ruling 4 — walk-forward arm (b) and spec NEEDS AMEAR.** *Rules:* the defaults, verbatim: ""We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05. Report the exact values chosen back to me." *Unlocks:* the walk-forward spec unit may propose exact values within these defaults. **No value is chosen here.** The exact values (the grid points, the risk-adjusted metric, the minimum trade count, and any other number the spec needs) are to be proposed by the spec unit and reported back to Amear, per his last sentence (master's reading (iv)). *Does NOT lift:* the hard limits; nothing is run.
- **Ruling 5 — handoff NEEDS AMEAR 1, 3–10, 15–17, 19.** *Rules:* "housekeeping or already answered — settle under R-1104-2." with his defaults (quoted per item in the table). *Unlocks:* the settlements table below. *Does NOT lift:* the hard limits; items 2, 11–14 and 18 are not in his list (see after the table).
- **Loop a–e.** Recorded verbatim in the paste above, in his order a → e, with "If a step needs a ruling, log it, skip it, continue." This entry is loop step b's "these rulings" content; it does not perform steps a, c, d or e.

**Ruling 5 settlements (R-1104-2).** Numbering = `docs/reports/2026-11-06-voice-handoff-evening.md` §4 (master's reading (i)). Column 3 is the master's decision under his delegation, not Amear's word. Source of column 3: the master's dispatch brief to this unit. The ledger row `2026-11-06T20:12:00Z` names the content of items 1, 5, 15 and 16 only, so for items 3, 4, 6–10, 17 and 19 this table is the first written record of the master's settlement; the master's own DECISION_LOG row is owed (this unit does not edit ledgers).

| Item (§4) | Amear's default (his words) | Settlement — master's decision under R-1104-2 | Applied at / pending |
|---|---|---|---|
| 1 — Fusion go-live line | none given | Append his line "unmap Z: and turn the share off before real money" (D-2026-11-06-A item 3) to the walkthrough's end; nothing above it edited. | `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` :33–37 |
| 3 — "the VM's Cowork agent" | none given | The master adopts a working definition: the Claude agent running inside the Windows VM (a definition, not an observation; the VM agent's first reply confirms or corrects it). Its skills directory is reported by the VM agent itself in its first reply. | pending: VM agent (first reply) |
| 4 — test 2a reference | "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match" | Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`; reference record `docs/reports/2026-11-01-three-strategy-results.md:73` (`:86` instrument). | pending: test 2a spec (loop step c) |
| 5 — limitation sentence into the rubric | none given | Written into `specs/SPEC_RUBRIC.md` as standing criterion S13. | `specs/SPEC_RUBRIC.md`:119 |
| 6 — lift scope | "my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched" | His lift covers the bridge install and its import; D-071 untouched. His words also say "what tests 2a/2b need"; whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6) stays in his words and is neither narrowed nor extended here. | pending: VM handoff (loop step c) |
| 7 — who reads the NT8 version | "VM agent reads and reports the NT8 version" | The VM agent reads and reports it; Code records it. | pending: VM agent |
| 8 — who judges 2a/2b | "Code + auditor judge 2a/2b and log the lift under my ruling" | Code + praxis-auditor judge 2a/2b and log the lift under his ruling (filer's identifications: "auditor" = praxis-auditor; the lift is D-2026-11-06-A item 2, "lifted COMPLETELY once two tests pass"; ruling 5 sets who judges). | pending: Code + auditor, after 2a/2b run |
| 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | It is a second session. Coordinate: Code does not run agents while the VM session writes; handover goes through the VM handoff file. | pending: VM handoff file (loop step c) |
| 10 — Fusion Questions 0–3 | none given | Closed by D-2026-11-06-A item 3 (SMB done by his hand) and this ruling. | walkthrough :33–37 |
| 15 — parked branch `parked/Praxis_build-r8j` (f258a5d) leak | none given | Findings only (below); the deletion decision stays with the master. | pending: master |
| 16 — carry D-2026-08-06-A onto main | none given | Carried, text unchanged except as noted in its preface. | `DECISIONS.md`:1131 |
| 17 — master's R-VN4-10 reading | none given | The master's reading stands as applied: the minter has no FAIL-word filter; the exact three-line verdict contract is the signal (D-2026-11-04-B addendum 2, DECISIONS.md:836–858, item 2 at :852). | DECISIONS.md:834–858 (as applied in the gate correction unit, which is parked as `Praxis_build-uqb`) |
| 19 — 10-28 voice notes file | none given | `docs/reports/2026-10-28-voice-session-notes.md` (untracked) is proposed by the master for commit with this unit's batch; a MANIFEST row is added; the file is not edited. Which of his two statements governs may itself be Amear's question (S8); under his loop rule "If a step needs a ruling, log it, skip it, continue" the file stays untracked until that is settled; this unit stages nothing. **Conflict flagged for the master:** the handoff labels this file "(old as-is set)" (§4 item 19), and his hard limit says "old as-is set out of every commit". This entry does not resolve which governs. | MANIFEST.md:244; commit: pending: master |

**Item 15 findings (OBSERVED this unit; commands and output in `docs/reports/2026-11-06-rulings-filing-manager.md`):** `git branch -r --contains f258a5d` printed nothing (rc=0), and `git ls-remote --heads origin 'parked/*'` lists `parked/Praxis_build-a9d` and `parked/Praxis_build-o78` only. So no branch on `origin` holds `f258a5d` today. Whether it was pushed and later deleted cannot be seen from these two commands. Supersession: the r8j manager report says the whole-file diff has "four header hunks" and that "From the `## Adapted Architecture` heading on (parked :17, new :28) the body is byte-identical (exit 0)" (`docs/reports/2026-11-05-r8j-phase3-import-and-wf-spec-manager.md:367`). So the parked spec's body is superseded by the committed `docs/specs/2026-11-05-phase3-build-specification.md`. Its header is not, and the header holds the leak (parked line 11, same report line). Nothing was deleted or rewritten.

**Not in ruling 5's list:** item 2 (who installs) is ruled by ruling 1; items 11–12 (gate park; hook change) by ruling 3; item 13 (fees) by ruling 2; item 14 (walk-forward spec NEEDS AMEAR) by ruling 4, with the values to be proposed back to him; **item 18 (notes-4 "not ruled" items) is still open** and is not settled here.

**S6 cross-block (interactions only; nothing decided here):**
- Test 2a vs the fee amendment. The 2a reference figures were produced with commission $2.96 per trade (`docs/reports/2026-11-01-csv-analyses.md:51`, `commission/trade={'2.96': 1190}`). An exact-match reproduction (item 4) therefore needs the commission used then, not the amended $4.68. At $4.68 the fee check's arithmetic gives $195,280.80 (`docs/reports/2026-11-05-mffu-fee-check.md:9`). Which commission the 2a run uses is for the master to set in the 2a spec.
- F1–F4 (`specs/SPEC_RUBRIC.md` F-sections) are untouched. S13 is a standing criterion, not an F-criterion.

## 2026-11-06 — D-2026-11-04-B addendum 4: ratification (WHO: amear) of addendum 1's timing

**Date:** 2026-11-06
**Status:** RATIFIED by Amear — DECISION_LOG `2026-11-06T20:08:28Z` (**WHO: amear**). Appended by praxis-manager, unit `2026-11-06-rulings-filing` (dispatch DECISION_LOG `2026-11-06T20:12:00Z`).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **His words, ruling 3(a), verbatim:** "(a) RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit;"
- **What is ratified.** The timing of D-2026-11-04-B addendum 1 (DECISIONS.md:796). That addendum describes itself as "appended 2026-11-04T21:34:49Z, AFTER the fix work; S4 timing NOT met for these items, stated rather than hidden". Amear's words at DECISION_LOG `2026-11-06T20:08:28Z` ratify that timing.
- **What it unblocks.** This entry is the named unblocking artifact for bead `Praxis_build-uqb`, parked at DECISION_LOG `2026-11-06T00:54:04Z` on S4 (master's reading (ii), same row).
- **What it does NOT do.** The unpark is a fresh audit, not an automatic PASS. Addendum 1's text is not edited. Nothing else about the gate is ruled here: the hook change under ruling 3(b) has its own unit, and its addendum is the master's later step.

## 2026-11-06 — D-2026-11-06-C: cost model amendment — MFFU published round turn NQ $4.68 / MNQ $1.90 (ruling 2)

**Date:** 2026-11-06 (appended in this unit before the JSON edit — the filer's attestation of command order, not a measurement)
**Status:** RULED by Amear — ruling 2, DECISION_LOG `2026-11-06T20:08:28Z` (**WHO: amear**). Appended by praxis-manager, unit `2026-11-06-rulings-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **His words:** "2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself."
- **Source of the figures:** `docs/reports/2026-11-05-mffu-fee-check.md:7` (MFFU's "Total Cost Round Trip": NQ $4.68, MNQ $1.90; MFFU does not split it into commission, exchange, clearing, NFA or platform fees), `:8` and `:104` ($5.76 is MFFU's YM figure, not NQ), `:98` (NQ $4.68 = $2.34 per side). The fee check grades the figures SPECIFIED by MFFU's page; no sim fill statement was OBSERVED (`:89`).
- **Change to `config/backtest-cost-model.json`:** `version` 1.1.0 → 1.2.0; `amended` 2026-10-30 → 2026-11-06; `decision_ref` += "; amended by D-2026-11-06-C (commission)"; `commission_round_turn_usd` 2.96 → 4.68; `commission_note` per-side 1.48 → 2.34; `total_cost_per_round_turn_usd` 22.96 → 24.68 (4.68 + 20.00); `total_cost_per_round_turn_ticks` 4.592 → 4.936 (24.68 / 5.00); `total_cost_breakdown_note` restated; new sibling `commission_round_turn_usd_mnq` 1.90 with a note. The instrument block stays NQ; MNQ is recorded for the per-tier DD table of the walk-forward spec.
- **Unchanged:** `slippage_*`, `fill_resolution`, `fill_resolution_note` and every note about them. F3 and D-2026-10-30-A are untouched; the limitation sentence is unchanged.
- **Not amended here, for the master** (the `2.96` grep, run this unit with /usr/bin/grep and a FILENAME filter excluding `docs/reports/`, `DECISIONS.md`, `DECISION_LOG.md` and the gitignored `Redemtion/`; the brief's `grep -v DECISIONS.md` form also drops lines that merely mention DECISIONS.md, so it under-reports; 16 lines, no `.py` or `.cs` file matched; `config/backtest-cost-model.json` no longer matches after the edit): `specs/SPEC_RUBRIC.md:50`; `STATUS.md:22`; `STATUS.md:129`; `STATUS.md:286`; `STATUS.md:385`; `STATUS.md:401`; `docs/specs/2026-11-05-phase3-build-specification.md:76`; `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129`; `docs/specs/2026-11-05-walk-forward-spec.md:45`; `docs/specs/2026-11-05-walk-forward-spec.md:191`; `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:25`; `MANIFEST.md:96`; `MANIFEST.md:153`; `MANIFEST.md:230`; `HANDOFF.md:147`; `HANDOFF.md:1181`. `specs/SPEC_RUBRIC.md:50` is F3 text — frozen, not edited. No code is changed: the rule "Don't change the code without asking me" (quoted in the master's reading (iii), DECISION_LOG `2026-11-06T20:08:28Z`; its own WHO: amear source row was not located by this unit). Also not edited: the JSON's `$schema_note`, which still says "v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A" (not in the brief's field list; for the master).
- **Arithmetic (no backtest):** +$1.72 per round turn against $2.96; over the 1,190 baseline trades, −$2,046.80, net $197,327.60 → $195,280.80 (`docs/reports/2026-11-05-mffu-fee-check.md:9`, `:96`). The baseline itself ran at $2.96 (see D-2026-11-06-B S6).

## 2026-08-06 — D-2026-08-06-A: Phase 3 build specification imported DE-IDENTIFIED (medication reference only)

(carried from `parked/Praxis_build-r8j` @ f258a5d on 2026-11-06 under ruling 5 / item 16; text unchanged except as noted) Noted: this preface line is the only addition; 0 redactions.

**Date:** 2026-08-06
**Status:** LOCKED (trader-ruled — Amear, 2026-08-06). Prospective: this entry authorises an import that has NOT yet been performed at the time of writing, per rubric S4 ("written before the work, not after").
**Authorship disclosure (rubric S4) — this entry was written in two stages:** The body was written **before** the import, per S4; both occurrences of "at the time of writing" in this entry refer to that pre-import moment and are not claims about the entry's final state. The entry was then **amended pre-commit on 2026-08-06**, after the post-import audit, to add the KNOWN PRE-EXISTING EXCEPTION and the escalation clause below — both of which necessarily post-date the import — and to correct the `HANDOFF.md` citation to its committed line number. This entry has **never been committed in any earlier form**, so no committed text is revised by the amendment; it is disclosed here rather than left implicit behind the prospective framing.
**AMENDMENT 2026-08-07 (pre-commit; disclosed, not silent) — the ordering claim above is an ATTESTATION, NOT A MEASUREMENT.** An independent audit found that the assertion "the body was written **before** the import" (and the "NOT yet been performed at the time of writing" framing in **Status** above) carries no pasted evidence and cannot be supported from the filesystem: `birth == mod` on `DECISIONS.md`, on the spec and on the report, so all three inodes date from a late whole-file rewrite and order only those rewrites, not the authoring. **The ordering is therefore NOT reconstructible and is not offered as evidence.** Under rubric S4 an ordering attested by the party being graded is exactly what is insufficient, so **S4 is not claimed discharged by this entry**; what remains is that the entry is written in prospective form and discloses its own two-stage authorship. The original wording above is left intact rather than reworded, per the `wx7` / `2026-08-04T18:44Z` preservation ruling — the record must show what was claimed as well as what corrected it. Evidence and full reasoning: `docs/reports/2026-08-06-session42-r8j-phase3-import.md`, section "Audit correction — 2026-08-07", §F6. This entry has still never been committed in any form, so no committed text is revised by this amendment either.
**Bead:** Praxis_build-r8j.
**Authorisation of record:** DECISION_LOG row `2026-08-06T20:18:56Z`. Proposed by praxis-master as an **escalation only** — the hazard was surfaced with no option recommended. Approved by Amear, 2026-08-06, in-session. Per rubric S5 ("No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation"), **the DECISION_LOG append at `2026-08-06T20:18:56Z` IS the authorisation**; the in-session exchange is recorded here only as that row's origin and carries no authorising force on its own.

**Context:** The Phase 3 build specification is to be imported from `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf` [local-only — not in this repo by design]. That source document titles circuit breaker #5 with a medication brand name. This repository is public. Publishing a clinical detail to a public repo is a one-way door: it is resettable in the repo, but not in forks, clones or caches. The 2026-07-24 ruling on the teaching-agent package established the governing pattern — commit behaviours only; clinical detail stays in Drive. The tracked ledgers already use the de-identified form "medication-window": see `specs/SPEC_RUBRIC.md:38-40`, which reads "Phase 2's medication-window justification for the 11:30 cut is now unsupported and was never revisited."

**Decision:** The Phase 3 spec is imported **de-identified**. Amear's ruling, verbatim: **"de-identify it — session window, no drug names"**. Circuit breaker #5 is titled and described as a **session window**. No medication brand name enters the tracked repository — in this import or any later one.

**Scope of change (explicit) — the rule is GENERAL, not a one-off edit:**
- No drug name **shall enter** any tracked artifact — spec, report, ledger row, commit message, or MANIFEST description. This is a **forward-binding obligation** on this import and every later one, matching the governing ruling's own verb ("enters", DECISION_LOG row `2026-08-06T20:18:56Z`). It is **not** an assertion that the repository is currently free of such a name. See the known pre-existing exception immediately below.
- De-identification is scoped to **the medication reference ALONE**. Every other part of the source is imported **faithfully**. The master is **not** licensed to paraphrase, tidy, condense or improve any other passage.

**KNOWN PRE-EXISTING EXCEPTION — the repository is NOT currently clean (rubric S2):** The medication brand name is **already present, verbatim, in two tracked files that were committed before this entry**: `DECISION_LOG.md` line 47 and `HANDOFF.md` line 45 (in `HEAD`, the index and `origin/main`; line 237 in the current uncommitted worktree). It was introduced on 2026-07-25 by commits `a42038e` (DECISION_LOG.md) and `7d9be8e` (HANDOFF.md) — verified absent in each commit's parent — and it is present in `HEAD` and in `origin/main` as of 2026-08-06. The term itself is deliberately **not reproduced here**; only its locations are cited. This condition was **surfaced by this unit, not created by it, and it is NOT resolved by this entry.** No scrub, rewrite, or history edit has been performed.

**Escalated, not answered (rubric S8 — "No question that belongs to Amear is answered on his behalf"):** Whether the de-identification ruling applies **retroactively** — and, if it does, whether remediation is confined to the working copies of those two files or requires rewriting commits `a42038e`/`7d9be8e` and force-updating `origin/main` — is **Amear's question**. It is recorded here and escalated. This entry states no preference, recommends no option, and establishes no default; silence here must not be read as a decision either way. Until Amear rules, the two locations above stand as-is.

**Behaviour preservation (the part F2 depends on):** Breaker #5's *behaviour* is preserved exactly — **the gate disables everything from 15:00 to 18:00 ET**, unchanged. Only its *rationale* changes form: it is carried as a session-window constraint stated without clinical basis.

**What this decision does NOT do:**
1. It does **not** unfreeze rubric criteria F1 or F2. The import supplies the naming half of F1 and the breaker-#4/#5 text that F2 must reconcile; **neither criterion is discharged by a document arriving**.
2. It does **not** authorise un-ignoring `Redemtion/` (`.gitignore:7`). That directory stays out of the repository.
3. It does **not** license paraphrase of any other part of the source (restated here because it is the clause most likely to be eroded in practice).

**Maturity of the circuit breakers (rubric S2 — no component reported above its evidence):** The nine circuit breakers described in the Phase 3 source, breaker #5 included, are **SPECIFIED ONLY** as of 2026-08-06: **zero implemented, zero tested, zero tested under failure**. Nothing in this entry, and nothing in the import it authorises, may be read as evidence that any breaker exists in working form. A specification arriving is not an implementation.

**Target of the import:** `docs/specs/2026-08-06-phase3-build-specification.md` — **this file does not exist at the time of writing**; it is created by step 2 of bead Praxis_build-r8j, under the constraints above.

## 2026-11-06 — D-2026-11-04-B addendum 5: third hand-back shape (task-notification) — WRITTEN AFTER THE WORK; S4 timing NOT met; ratification requested (WHO: amear)

**Timing, stated plainly.** This addendum is written at 2026-11-06T22:25:14Z (`date -u`, OBSERVED by the filer). That is AFTER the work. The code landed at `933ef70`, commit time `2026-11-06T17:01:47-05:00` = 22:01:47Z (OBSERVED, `git show -s --format=%cI 933ef70`). `69ec506` and `234e4bc` were then committed through it (REPORTED BY DECISION_LOG `2026-11-06T22:09:15Z`, `22:11:54Z`). **S4 ("written before the work, not after") is NOT met for this addendum.** The authorisation that DID come before the work: DECISION_LOG `2026-11-06T20:08:28Z` (**WHO: amear**, ruling 3(b)) → dispatch row DECISION_LOG `2026-11-06T20:12:00Z` → unit `2026-11-06-gate-async-handback`. The master's account of the fault is DECISION_LOG `2026-11-06T22:25:00Z`: "I repeated the exact fault class the unit was parked for." D-2026-11-06-B (ruling 3(b) paragraph, DECISIONS.md:1076) had said this addendum "is the master's later step and is not written here".

**RATIFICATION REQUESTED (WHO: amear).** Ratify this addendum's timing as he ratified addendum 1's (ruling 3(a), addendum 4), or do not. That is his call. Nothing here ratifies it. Until he rules, `Praxis_build-uqb` stays open at FAIL 1 of its fresh cycle (REPORTED BY DECISION_LOG `2026-11-06T22:25:00Z`).

**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **His words, ruling 3(b), verbatim** (DECISION_LOG `2026-11-06T20:08:28Z`): "(b) APPROVE the hook change so the gate accepts the auditor's async hand-back. First commit through it is the test; on failure, revert and I keep typing commits."
- **Design, as built** (read from `.claude/hooks/gate-commit.sh` at HEAD `234e4bc`; the file is unchanged since `933ef70`, OBSERVED with `git diff --quiet 933ef70 HEAD -- .claude/hooks/gate-commit.sh`, rc=0). `handback_check` now accepts a third shape, inside the block `# W-TN 2026-11-06 (ruling 3b) BEGIN` … `END` (lines 477–539):
  - The record must be `type=="user"` with `.origin.kind=="task-notification"` and not `isMeta` (lines 506–508).
  - Text is taken only from `.message.content` when it is a string, or from its `type:"text"` blocks (lines 509–512). `tool_result` blocks are never read. Attachment records and assistant records never match the `type=="user"` select.
  - The text must begin with the `<task-notification>` line (line 513). Only the first block counts: the scan opens on the first line and stops at the first `</task-notification>` (lines 514–517).
  - The first `<task-id>` must equal the token's agent id (lines 518–520). The first `<status>` must be `completed` (lines 521–523). The first `<summary>` must equal `<summary>Agent "<desc>" finished</summary>` exactly (lines 505, 524–525). A second `<task-id>`, `<status>` or `<summary>` line ends the scan.
  - `<desc>` is read from the assistant `tool_use` record whose id is the `toolUseId`. The gate takes that `toolUseId` from the agent's `meta.json` (lines 429–431), not from the token; only the agent id comes from the token. The bound stub check below is what ties the two. It must be one non-empty string, the same in every such record, with no newline, CR, `<`, `>`, `"` or `&`. If not, the check returns 1 (lines 491–504).
  - The hash line is accepted only inside that block's `<result>` span, and only after id, status and summary have matched (lines 526–535).
  - The bound stub `tool_result` is still checked first: it is extracted at lines 433–441 and classified at lines 442–446, with the cases handled at lines 447–452. SYNC returns 0 there; NOBIND returns 1; only BOUND reaches the older `agent-message` shapes (lines 453–476) and then this block. Those older shapes are unchanged.
  - Function identity outside the block, OBSERVED now: `handback_check` at HEAD with lines 477–539 removed, and `handback_check` at `933ef70^`, both hash to sha256 `4f1ef67112dcf0d3e4a181f590238f9c42d9732d12e49243dbf84156752589a8`. Also REPORTED BY report `docs/reports/2026-11-06-gate-async-handback-manager.md`:188–189 and :554, and DECISION_LOG `2026-11-06T21:05:00Z`.
  - Design narrative: report :28–62 and :166–442.
- **Tests and evidence pointers.** `scripts/tests/test-gate-handback.sh` (284 lines) runs 32 cases: 5 positives (P0 SYNC, P1/P1b real captures, P2/P2b the older shapes) and 27 negatives. Report :325–360 shows `SUMMARY pass=32 fail=0 total=32`. The forgery cases include: the frame as a `tool_result` content string (N3); as a text block beside a `tool_result`, origin removed (N3b); inside an assistant record (N4); a wrong id (N1); a wrong hash (N2); two blocks in one record (N5, N5b); NOBIND (N6b); an injected or non-plain description (N12–N12e, N15, N17–N17c); and two `tool_use` records with one id and different descriptions (N16) (test file comments, lines 135–271). Mutation control: with the block removed, `pass=30 fail=2`, and only P1/P1b fail, the two real captures (report :362–400). The auditor re-ran these as 32/32 and 30/2 (REPORTED BY DECISION_LOG `2026-11-06T22:25:00Z`). **MINOR:** the fixtures live in that session's scratchpad (report :60). A later session must re-capture them, or the test FAILs. End-to-end: the gate ALLOWED at 22:06:32Z. The allowed tree was `18462b58…` (REPORTED BY DECISION_LOG `2026-11-06T22:07:11Z`), and that equals `69ec506^{tree}` = `18462b5810a302f9b53a4e96a1e7074bc13f739f` (OBSERVED, `git rev-parse`). Commits `69ec506` and `234e4bc` then landed (DECISION_LOG `22:09:15Z`, `22:11:54Z`).
- **Operational consequences** (each graded on its own line):
  - A task-notification that arrives mid-turn is recorded as an `attachment`/`queued_command`, not as a `type=="user"` record. This block does not read attachments, so that hand-back is DENIED (fails closed). The report counted 34 of 118 real notifications in this form (REPORTED BY report :53, :515). The denial in a live run is UNVERIFIED (below). The master's procedure in response is to end its turn after dispatching an auditor (master's practice, REPORTED BY DECISION_LOG `2026-11-06T22:07:11Z`: "end the turn so the notification arrives idle").
  - The auditor's Agent description must be plain (no newline/CR/`<`/`>`/`"`/`&`), or the check returns 1 (code, lines 498, 503).
  - The master bash-guard's regex `(^|[^>])>{1,2}[[:space:]]*[^&]` (`scripts/master-bash-guard.sh`:12) matched the `>` in the `<noreply@anthropic.com>` trailer and denied the first commit attempt. The trailer was then written in parentheses on the gate route (REPORTED BY DECISION_LOG `2026-11-06T22:07:11Z`, the master's own observation). **The guard-vs-trailer question belongs to Amear.** That row names two options: "either the guard exempts `git commit` messages or the attribution line keeps the parenthesised form on this route". The first would be a new hook change, outside ruling 3(b). The parenthesised form is the current practice only; it is not chosen here. Nothing is decided here.
- **Still UNVERIFIED.** The PostToolUse verifier's message on a tree mismatch. The mid-turn denial in a live run (the fail-closed reading rests on the code and the recorded shapes, not on a live denial).
- **What this addendum does NOT do.** It ratifies nothing. It does not extend ruling 3(b) beyond "accept the auditor's async hand-back". It does not edit D-2026-11-06-B or addenda 1–4.

## 2026-11-07 — D-2026-11-04-B addendum 6: ratification (WHO: amear) of addendum 5's timing

**Date:** 2026-11-07
**Status:** RATIFIED by Amear — DECISION_LOG `2026-11-07T12:55:00Z` (**WHO: amear**; working tree, not yet in a commit). Appended by praxis-manager, unit `2026-11-07-rulings-filing` (dispatch DECISION_LOG `2026-11-07T13:00:54Z`, WHO: praxis-master). First written 2026-11-07T13:08:18Z (`date -u`, OBSERVED by the filer); revised by the same unit before its return, after two adversarial passes (wording, labels and pointers only; his words and the paste unchanged).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

- **His words, ruling 1, verbatim** (`docs/reports/2026-11-07-amear-rulings-morning.md`:11): "1. Addendum 5 timing: RATIFIED. Unpark/close uqb on a fresh audit."
- **What is ratified.** The timing of D-2026-11-04-B addendum 5 (DECISIONS.md:1165), as that addendum describes itself (OBSERVED, :1167): written 2026-11-06T22:25:14Z, AFTER the work, which landed at `933ef70`; "S4 ("written before the work, not after") is NOT met for this addendum." Its :1169 requested ratification ("Ratify this addendum's timing as he ratified addendum 1's (ruling 3(a), addendum 4), or do not. That is his call."). Amear's words at DECISION_LOG `2026-11-07T12:55:00Z` ratify that timing.
- **What it unblocks.** This entry is the named unblocking artifact for bead `Praxis_build-uqb`'s S4 FAIL 1 of its fresh cycle (REPORTED BY DECISION_LOG `2026-11-06T22:25:00Z`), and for the addendum-5 audit, "AUDIT FAIL on S4 ONLY", where "only Amear's ratification cures it" (REPORTED BY DECISION_LOG `2026-11-06T22:34:00Z`).
- **What it does NOT do.** "Unpark/close uqb on a fresh audit" is a fresh audit, not an automatic PASS; this entry closes nothing. Addendum 5's text is not edited. Nothing else about the gate is ruled here: the guard-vs-trailer question (addendum 5, DECISIONS.md:1188) is ruling 3, recorded in D-2026-11-07-A below, and no hook, guard or script is changed.

## 2026-11-07 — D-2026-11-07-A: Amear's ten morning rulings (typed, 2026-11-07) — filed WHO: amear

**Date:** 2026-11-07
**Status:** RECORDED — Amear's rulings, WHO: amear. Source row and ledger authorisation (S5): DECISION_LOG `2026-11-07T12:55:00Z` (**WHO: amear**; working tree, not yet in a commit). Dispatch: DECISION_LOG `2026-11-07T13:00:54Z` (WHO: praxis-master). Appended by praxis-manager, unit `2026-11-07-rulings-filing`. First written 2026-11-07T13:08:18Z (`date -u`, OBSERVED by the filer); revised by the same unit before its return, after two adversarial passes (wording, labels and pointers only; his words and the paste unchanged). The master reports that after `/clear` Amear re-typed the rulings and that the re-typed message was "OBSERVED byte-equal to the filed `docs/reports/2026-11-07-amear-rulings-morning.md:9-31`" (REPORTED BY DECISION_LOG `2026-11-07T13:00:54Z`; the filer did not see that message).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** *Amear's words* = the fenced block below, copied byte for byte by script from `docs/reports/2026-11-07-amear-rulings-morning.md` lines 9–31 (the rulings file, filed verbatim by praxis-master at 12:55Z). *Master's decision under delegation* = a settlement the master made under R-1104-2 (DECISIONS.md:748) after Amear handed him the item; it is labelled as such and is not Amear's word. The rulings file's "Master's filing notes (not rulings)" (its lines 35–44) are the master's readings, not rulings, and are not quoted here as his. Line pointers and the identifications marked INFERRED are the filer's.

**The paste, verbatim (WHO: amear).** Rulings file lines 9–31, inserted by script (`sed -n 9,31p`), not retyped.

```text
RULINGS — 2026-11-07 morning (WHO: amear). Answers to the 11-07 return handoff §4.

1. Addendum 5 timing: RATIFIED. Unpark/close uqb on a fresh audit.
2. Item 19: commit docs/reports/2026-10-28-voice-session-notes.md as a one-file exception to the as-is rule — it is the source of a ruling. Fix MANIFEST.md:244 to match.
3. Guard vs trailer: no guard change. Keep the attribution line in the form the guard accepts. Don't loosen a guard to fit a format.
4. Walk-forward values (Q1–Q10):
   Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid.
   Q3 Off is NOT a stop value — I ruled "add the stop, tune all four". Three finite stop-ATR multipliers; you propose them, inside 1.5–3.0 ATR.
   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
   Q6 ATR(14) = 14 completed RTH sessions (daily ATR).
   Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's trade lists. That keeps one copy of the strategy (NT8); only the selection maths runs on the Mac.
   Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05.
   Q9 no tier chosen. Report the per-tier table; I pick after paper results.
   Q10 and every remaining PROPOSED value in the file: settle under R-1104-2, strictest reasonable choice. Add the missing ExitPolicy/Contracts test that parked 867, re-audit, commit.
5. 2a run: YES, covered by my lift. A test that needs a run includes the run.
6. Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then.
7. Bridge items: (4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise. (5) NT8 Guard out. (7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP. (11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\. (12) you propose how each arm runs through the bridge after 2a passes.
8. Snapshot is my hand step: confirmed.
9. Notes-4 unruled items stay open; none block anything.
10. Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share.

Then loop: finish 867, build arm (a) and (b) Mac-side, and tell me when the VM session can start. Return handoff here at the end, only decisions that are genuinely mine.
```

**Copy check.** sha256 of rulings file lines 9–31 (`sed -n 9,31p docs/reports/2026-11-07-amear-rulings-morning.md | shasum -a 256`) = `b6b954347cc2e35a3b2f2ad63d1e49c084a5ceeb236a913384ec3668635656d7`; sha256 of this block's body = `b6b954347cc2e35a3b2f2ad63d1e49c084a5ceeb236a913384ec3668635656d7` (equal; computed by the splice script from the assembled text, and re-checked after insertion from this file by line numbers, OBSERVED).

**Structured record, ruling by ruling.** The quotes below are his words from the block above. No ruling is read past its words.

- **Ruling 1 — addendum 5 timing.** *Rules:* "Addendum 5 timing: RATIFIED. Unpark/close uqb on a fresh audit." *Unlocks:* D-2026-11-04-B addendum 6 above, the named unblocking artifact for `Praxis_build-uqb`; a fresh audit of `uqb`. *Does NOT lift:* the fresh audit is not a PASS; `uqb` is not closed by this entry.
- **Ruling 2 — item 19, the 10-28 voice notes file.** *Rules:* "Item 19: commit docs/reports/2026-10-28-voice-session-notes.md as a one-file exception to the as-is rule — it is the source of a ruling. Fix MANIFEST.md:244 to match." *Unlocks:* a one-file exception to the hard limit "old as-is set out of every commit" (his words, D-2026-11-06-B paste, DECISIONS.md:1063) for `docs/reports/2026-10-28-voice-session-notes.md` ONLY. The file is carried unedited (sha256 `7999c03410ffd0e83253100ea76714b80f0f211a1e363470965231edaeb6cb48`, OBSERVED by the filer at 2026-11-07T13:08Z). This resolves the conflict D-2026-11-06-B flagged at item 19 (DECISIONS.md:1097). "Fix MANIFEST.md:244 to match" is applied as an UPDATE ROW appended to MANIFEST.md that supersedes row 244's "proposed for commit … (master's settlement…)" wording; row 244 itself is not edited: MANIFEST.md:9 declares the file an "Append-only file creation registry", and the UPDATE ROW form follows MANIFEST.md:246. The practice is not uniform (commit `69ec506` edited one MANIFEST row in place, OBSERVED: `git show 69ec506 -- MANIFEST.md` has 1 removed row). The UPDATE ROW form is the master's choice in the dispatch row, not Amear's word; whether it satisfies "Fix MANIFEST.md:244 to match" is his to say if he reads it otherwise. *Does NOT lift:* the rest of the old as-is set stays out of every commit; this entry commits nothing (the gated commit is the master's later step).
- **Ruling 3 — guard vs trailer.** *Rules:* "Guard vs trailer: no guard change. Keep the attribution line in the form the guard accepts. Don't loosen a guard to fit a format." *Unlocks:* closes the guard-vs-trailer question that addendum 5 left to him (DECISIONS.md:1188), between the two options DECISION_LOG `2026-11-06T22:07:11Z` named ("either the guard exempts `git commit` messages or the attribution line keeps the parenthesised form on this route"). The answer is the second, with NO code change: on the master's route the attribution line keeps the form the guard accepts, which today is the parenthesised form (REPORTED BY DECISION_LOG `2026-11-06T22:07:11Z`). *Does NOT lift:* no hook, guard or script is edited; `scripts/master-bash-guard.sh` is not loosened.
- **Ruling 4 — walk-forward values (Q1–Q10).** *Rules,* his answers, each verbatim:
  - Q2: "Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid."
  - Q3: "Q3 Off is NOT a stop value — I ruled "add the stop, tune all four". Three finite stop-ATR multipliers; you propose them, inside 1.5–3.0 ATR." Proposing the values is delegated to the master ("you propose them"). The filer reads the authority to settle them as resting on Q10's delegation (below) (INFERRED: Q10 covers "every remaining PROPOSED value", and whether Q3's stops count as "remaining" is a reading; the dispatch row cites both Q3 and Q10).
  - Q4: "Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs."
  - Q5: "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs."
  - Q6: "Q6 ATR(14) = 14 completed RTH sessions (daily ATR)."
  - Q7: "Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's trade lists. That keeps one copy of the strategy (NT8); only the selection maths runs on the Mac."
  - Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05."
  - Q9: "Q9 no tier chosen. Report the per-tier table; I pick after paper results."
  - Q10: "Q10 and every remaining PROPOSED value in the file: settle under R-1104-2, strictest reasonable choice." Delegated to the master. "The file" is read by the filer as the parked spec `docs/specs/2026-11-06-walk-forward-values.md`, whose values are marked PROPOSED (INFERRED).
  - Q1 got no answer of its own. The filer reads it as falling under Q10's "every remaining PROPOSED value in the file" (INFERRED).
  - Q10's last sentence: "Add the missing ExitPolicy/Contracts test that parked 867, re-audit, commit." It unlocks the next unit, which resumes `Praxis_build-867` (parked at DECISION_LOG `2026-11-07T00:00:00Z`). It is not done here.

  *Unlocks:* the Q3 settlement below, and the values unit D-2026-11-07-B.
  *Does NOT lift:* nothing is run; no code is written; the spec `docs/specs/2026-11-06-walk-forward-values.md` is not edited.

  **Master's decision under delegation (R-1104-2), not Amear's word.** Source: DECISION_LOG `2026-11-07T13:00:54Z` (WHO: praxis-master), on his Q3 words and Q10's "strictest reasonable choice". Q3 stop-ATR multipliers = **{1.5, 2.25, 3.0} × ATR(14)**: "the two bounds he named and their midpoint, nothing chosen outside his range". `StopAtrMult = 0` stays a permitted INPUT value for acceptance tests T1–T3, which reproduce the three committed stop-less runs. It is NOT a grid value. The grid stays 3×3×3×3 = 81, all stop-on. The row says the choice is "reported back to him in U5 and changeable by him". Every OTHER value settlement (Q1, Q10's remaining PROPOSED values, and the spec revision) belongs to **D-2026-11-07-B (to be written)** by the next unit. It is not written here. When D-2026-11-07-B is written, it supersedes the parked draft D-2026-11-06-D (the last block of this file). That draft is not edited here.
- **Ruling 5 — 2a run.** *Rules:* "2a run: YES, covered by my lift. A test that needs a run includes the run." *Unlocks:* answers the run half of D-2026-11-06-A NEEDS AMEAR 6 (DECISIONS.md:1046): his lift covers the test 2a NT8 run on the VM. The D-071 half of that question is not answered by ruling 5's words. *Does NOT lift:* his words do not mention D-071; D-2026-11-06-B settlement 6 (DECISIONS.md:1089), whose default in his 11-06 words reads "D-071 untouched", stands. No run happens here.
- **Ruling 6 — Strategy Analyzer tab. Addendum-level statement to D-2026-11-06-A item 2 (DECISIONS.md:1003).** *Rules:* "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then." *Unlocks:* a PARTIAL PASS state for the in-VM automation lift of D-2026-11-06-A item 2 ("lifted COMPLETELY once two tests pass; until then it stands. a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW."). A 2a run from a hand-set Strategy Analyzer tab counts as "bridge reproduces the baseline", NOT as "driven from the terminal". The full lift needs a run whose settings come from the bridge/config. When 2a passes on a hand-set tab, the lift is logged as a partial pass until such a run; no partial pass is logged now, because 2a has not run. This answers VM handoff §8 row 10 (`vm/2026-11-06-vm-handoff.md`:282). *Does NOT lift:* the full lift. His words do not say that a partial pass lifts any part of the Oct 28 restriction, so item 2's "until then it stands" is neither narrowed nor extended here. Row 10's sub-question "Who sets the tab by hand" is not answered in so many words. "not my hands" may mean his hands set it (INFERRED), but that is not settled here. D-2026-11-06-A's text is not edited.
- **Ruling 7 — bridge items** → VM handoff §8 rows (`vm/2026-11-06-vm-handoff.md`:273–284). His words, per item:
  - (4) → row 4: "(4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise."
  - (5) → row 5: "(5) NT8 Guard out."
  - (7) → row 7: "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." This is a hard STOP condition in his words ("or STOP"). His words do not say whether the STOP ends test 2a or the whole VM session; the rulings file's filing notes call it "a hard STOP condition for the VM session", which is the master's reading, not his word.
  - (11) → row 11: "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\." This answers the `pip` half only. Row 11's route question ("How the source reaches the VM") is not answered by his words and stays his.
  - (12) → row 12: "(12) you propose how each arm runs through the bridge after 2a passes." The master proposes, after 2a passes.

  *Unlocks:* these are APPLIED to `vm/2026-11-06-vm-handoff.md` by a later unit (the VM handoff amendment), not here. *Does NOT lift:* the VM handoff is not edited by this entry; nothing is installed or downloaded.
- **Ruling 8 — snapshot.** *Rules:* "Snapshot is my hand step: confirmed." *Unlocks:* confirms VM handoff §8 row 9 (`vm/2026-11-06-vm-handoff.md`:281). The master's reading there, that the snapshot is his hand step, is now his word. *Does NOT lift:* the order (snapshot before the install, ruling 1 of D-2026-11-06-B) is unchanged; no snapshot is taken here.
- **Ruling 9 — notes-4.** *Rules:* "Notes-4 unruled items stay open; none block anything." *Unlocks:* nothing. The notes-4 items stay open (D-2026-11-06-B item 18, DECISIONS.md:1101), and per his words they block nothing. *Does NOT lift:* none of them is ruled here.
- **Ruling 10 — go-live checklist.** *Rules:* "Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share." *Unlocks:* (i) "remove the unauthenticated bridge request folders (or add auth) before real money" is appended in his words to the go-live material of `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` by this unit, as one line at the end of that file (:38). Placement, the master's and not Amear's word (he named no location): the dispatch row `13:00:54Z` says "Fusion walkthrough `## Go-live (R-VN4-14)` section: append ruling 10's first item in his words … as a dated addendum line below the existing checklist", and the dispatch brief gives that section as lines ~26–37. :38 is the end of that range, below the go-live checklist line at :35; physically it sits under the `## Addendum 2026-11-06` heading that holds :35, while the `## Go-live (R-VN4-14)` heading itself spans :26–27. A strictly literal reading of the row's heading would put the line after :27; the master may move it (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`:38, OBSERVED by the unit's manager after the append; nothing above it edited). (ii) "unmap Z: and turn off the SMB share" is already in the walkthrough at :35, in his 11-06 wording ("unmap Z: and turn the share off before real money", OBSERVED). It is not duplicated; that is the master's choice in the dispatch row, not Amear's word. *Does NOT lift:* nothing is removed, unmapped or turned off now. VM handoff §8 row 3 ("Is an unauthenticated file-drop folder acceptable") is not answered by these words and stays his.
- **Then loop.** Recorded verbatim in the paste above ("Then loop: finish 867, build arm (a) and (b) Mac-side, and tell me when the VM session can start. Return handoff here at the end, only decisions that are genuinely mine."). This entry performs none of its steps.

**VM handoff §8 rows not answered by these rulings** (OBSERVED against `vm/2026-11-06-vm-handoff.md`:273–284): row 1 (the AddOn import file set), row 2 (the in-NT8 compile step's hand), row 3 (unauthenticated file-drop folder; see ruling 10), row 8 (which account the tests use). They stay his. Row 6 (NT8 build) is a pending value, not a question to him. Row 11 is answered for `pip` only (ruling 7).

**What this entry does NOT do.** No code. No run. No VM edit. No purchase. No new data connection. F1–F4 untouched. The D-2026-11-06-D draft is untouched and stays the last block of this file. No value other than Q3 is settled here. No ledger is edited.

**S4 timing.** This entry and addendum 6 are written at 2026-11-07T13:08:18Z, BEFORE the work they authorise: the `uqb` fresh audit, the values unit D-2026-11-07-B, the 867 test, the arm builds and the VM handoff amendment are later units. Addendum 6 is a ratification, not new work. Stated, not hidden: the ruling-10 walkthrough line and the ruling-2 MANIFEST UPDATE ROW are written by this same unit, and the walkthrough line was appended at 13:08:15Z (that file's mtime, `stat`, unchanged since), BEFORE this entry was first spliced into this file. This file's own mtime is not cited: every save of this entry moves it. Their content was set by Amear's `12:55:00Z` row and the dispatch row `2026-11-07T13:00:54Z`, both of which precede all three; the walkthrough line's exact placement is the master's (ruling 10 below). The Q3 settlement's source row (`13:00:54Z`) predates this entry; nothing has been built on it yet (REPORTED BY that row, "U1 dispatching").

**S6 cross-block (interactions only; nothing decided here).**
- F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59) are not modified by this entry. F2 (:30) asks for one governing rule resolving three terms (breaker #4 closes positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET; Deviation B flattens at 16:00 ET) and for what happens to an open position at 15:00. Ruling 4 Q5 ("flatten on the 15:59 bar") defines one exit policy of the walk-forward grid and bears on all three terms: a Flat1559 position runs past 11:30 (breaker #4), through 15:00 (breaker #5) and flattens before 16:00 (Deviation B). F2 is NOT resolved here; that interaction is for D-2026-11-07-B and its audit.
- O1 (`specs/SPEC_RUBRIC.md`:74) requires "a written statement of which gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the replication arm or the later optimisation arm." Ruling 4 Q8 ("both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05") bears on that statement. O1 is NOT resolved here; whether Q8 discharges it is for the unit that writes D-2026-11-07-B and for its audit.
- O4 (`specs/SPEC_RUBRIC.md`:94) is untouched.
- D-2026-11-06-A item 2's "Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy." (DECISIONS.md:1003) and ruling 4 Q7 point the same way (INFERRED: Q7 adds that window selection and PBO run on the Mac from NT8's trade lists).

**Correction 1 (before commit, after audit FAIL 1 on S1/S13/check f; appended by unit 2026-11-07-rulings-filing-correction-1, DECISION_LOG 2026-11-07T13:36:00Z).** Retracted, as written in the S4 timing paragraph above (:1282): "the walkthrough line was appended at 13:08:15Z (that file's mtime, `stat`, unchanged since), BEFORE this entry was first spliced into this file." No output was pasted for it, and "unchanged since" is false. OBSERVED by this unit before any edit: `TZ=UTC stat -f '%Sm' -t '%Y-%m-%dT%H:%M:%SZ' docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` → `2026-11-07T13:25:12Z`. The 13:08:15Z first-append time, and so whether that first append preceded this entry's first write at 13:08:18Z (:1282), is UNVERIFIED: the mtime has moved since. The walkthrough :38 line's current text dates from the W4 fix round of the filing unit (REPORTED BY `docs/reports/2026-11-07-rulings-filing-manager.md`:27 and :230), i.e. after this entry's first write. S4, restated: the line is written by the same unit as this entry (as :1282 says); its CONTENT was set by the `12:55:00Z` (WHO: amear) and `13:00:54Z` rows, both before any edit; its text was last edited after this entry's first write. Also corrected (:1262, :1280): "the last block of this file" means the last block of the WORKING-TREE file; the blob the master's gated commit is to carry ends at the line before the D-2026-11-06-D heading and does not contain the draft (INFERRED: the `13:36:00Z` row assigns the rebuild of `commit-idx-u1` to the master; that blob is not built by this unit). Also corrected (:1244): "The file is carried unedited" now holds for its body (lines 1–56) only; "unedited" is the master's dispatch word (`13:00:54Z`), not Amear's (REPORTED BY the `13:36:00Z` row). Master's decision under R-1104-2 (DECISION_LOG `2026-11-07T13:36:00Z`, WHO: praxis-master; not Amear's word; changeable by him): a `---` separator and one marked S13 addendum line are appended to the end of that file and of `docs/reports/2026-11-07-amear-rulings-morning.md`; their bodies stay byte-identical (sha256 `7999c034…cb48`, lines 1–56; `975f9c48…1c78`, lines 1–44). Void clause, from that row: if Amear wants the notes file byte-identical as a whole, the line comes off and S13 is waived for that file by his word.

## 2026-11-07 — D-2026-11-07-B: walk-forward values — RULED (D-2026-11-07-A) and SETTLED (R-1104-2); arm (b) code design and acceptance tests T1–T13

**Date:** 2026-11-07
**Status:** RULED / SETTLED by source. RULED = Amear's words, quoted from D-2026-11-07-A (and the older rulings named below). SETTLED = a settlement under R-1104-2 (DECISIONS.md:748), delegated by Q10: the stop values and the `StopAtrMult = 0` input rule are the master's own decision in D-2026-11-07-A (:1262); every other settlement is made by this unit on the master's dispatch (DECISION_LOG `2026-11-07T14:06:00Z`); each is changeable by him. Not Amear's word. This entry supersedes the never-committed draft D-2026-11-06-D, parked FAIL 2 at DECISION_LOG `2026-11-07T00:00:00Z`. That draft's text is preserved verbatim in `docs/reports/2026-11-07-wf-values-fresh-manager.md` Appendix B (sha256 `9a83e55d1e56942f80273d9b52721ea6852cf7e5b58cac67d12b876395693683`). Governing spec: `docs/specs/2026-11-06-walk-forward-values.md` version 2. Appended by praxis-manager, unit `2026-11-07-wf-values-fresh`. Dispatch: DECISION_LOG `2026-11-07T14:06:00Z` (WHO: praxis-master). First written 2026-11-07T14:40:44Z (`date -u`).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Authorisation.**
- D-2026-11-07-A ruling 4, his words, copied by script from DECISIONS.md lines 1220–1228 (the fenced block, `sed -n 1220,1228p`), not retyped:

```text
   Q2 yes, lookback {10,14,18} x multiplier {0.8,1.0,1.2} is the small grid.
   Q3 Off is NOT a stop value — I ruled "add the stop, tune all four". Three finite stop-ATR multipliers; you propose them, inside 1.5–3.0 ATR.
   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
   Q6 ATR(14) = 14 completed RTH sessions (daily ATR).
   Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's trade lists. That keeps one copy of the strategy (NT8); only the selection maths runs on the Mac.
   Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05.
   Q9 no tier chosen. Report the per-tier table; I pick after paper results.
   Q10 and every remaining PROPOSED value in the file: settle under R-1104-2, strictest reasonable choice. Add the missing ExitPolicy/Contracts test that parked 867, re-audit, commit.
```

  Q1 got no answer of its own. D-2026-11-07-A's filer reads it as falling under Q10 (DECISIONS.md:1256, INFERRED).
- Reach of Q10 — INFERRED (the master's reading, DECISION_LOG `2026-11-07T14:06:00Z`). The dispatch settles "for every value that was PROPOSED and for Q10's open items — EXCEPT the items ruling 9 keeps open". Version 1's NEEDS AMEAR question 10 was `**The WF spec's 29 items, mapped.**` (version 1 :146, in the unit report's Appendix A). So Q10 is read as also handing over the WF spec's 29 items, except ruling 9's items and the tier pick (Q9). Not Amear's word.
- D-2026-11-06-B ruling 4 (DECISION_LOG `2026-11-06T20:08:28Z`, WHO: amear; paste at DECISIONS.md:1063), as spec §0 quotes it: "4. Walk-forward arm (b) and spec NEEDS AMEAR, under "We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05. Report the exact values chosen back to me."
- Ruling 1 of 2026-11-05 on the bar-close stop (DECISION_LOG `2026-11-05T23:50:09Z`, WHO: amear), as spec §0 quotes it: "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b)."
- D-2026-11-05-A items 1–5 (DECISIONS.md:812–816; the voice agent's record, filed as WHO: amear), copied by script:
  - *"1. Walk-forward runs BOTH ways: (a) paper's fixed rules, nothing optimised; (b) four parameters tuned per window — lookback, noise multiplier, stop-ATR multiplier, exit policy. A stop is added to the strategy for (b) on its own branch; baseline file unchanged."*
  - *"2. Windows per spec: 252-day in-sample / 63-day out-of-sample / 63-day step."*
  - *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
  - *"4. Every window also reports worst drawdown at 1 MNQ and 1 NQ against each MFFU tier's limit."*
  - *"5. Account tier: no decision until backtest + paper results exist."*
- D-2026-11-06-A item 2 (DECISIONS.md:1003): "Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy."
- D-2026-11-07-A, the master's Q3 settlement (DECISIONS.md:1262; DECISION_LOG `2026-11-07T13:00:54Z`, WHO: praxis-master). Not Amear's word.

**Values.** Every value in spec §2–§9. "(B) n" is the row of the spec's list (B). Each SETTLED value is changeable by him.

| Value | Setting | Grade | Spec |
|---|---|---|---|
| Arm (a) code | `ninjascript/PraxisNoiseAreaBreakout.cs` unchanged: Lookback 14, k 1.0, BandOrVWAP, Contracts 1 | The four values OBSERVED (code, spec §2); nothing optimised and the file unchanged: RULED (D-2026-11-05-A item 1, "nothing optimised", "baseline file unchanged") | §2 |
| Arm (a) stop | None | INFERRED (spec §2: item 1 adds the stop "for (b)") | §2 |
| Judged arm | (a) | RULED as his statement (ruling 4 of 2026-11-06, "judged arm = (a) fixed rules"); as an O1 item OPEN (ruling 9) | §2, §8 |
| Arm (a) windows | Full-span run, reported on the 17 OOS windows plus the full-span total | SETTLED; alternative: also window 1's first 252 sessions ((B) 1) | §2 |
| Status of this walk-forward | Provisional result, labelled so; not by itself the go/no-go judgement | SETTLED; alternative: treat it as the judged version ((B) 35) | §2 |
| Breakers | Run without breakers, labelled provisional; repeated with breakers once built; both kept. A reporting convention only | SETTLED for walk-forward use only; the Block 4 question is not decided here (breaker build; O4); alternative: wait for the breakers ((B) 36) | §2 |
| Lookback grid | {10, 14, 18} | RULED (Q2) | §3 |
| Noise multiplier grid | {0.8, 1.0, 1.2} | RULED (Q2) | §3 |
| Stop axis constraint | Off is not a stop value; three finite multipliers inside 1.5–3.0 ATR | RULED (Q3) | §3 |
| Stop-ATR multipliers | {1.5, 2.25, 3.0} × ATR(14) | SETTLED (the master, D-2026-11-07-A :1262); alternative: {1.5, 2.0, 2.5} or {2.0, 2.5, 3.0} ((B) 2) | §3 |
| `StopAtrMult = 0` | Input value for T1–T3 only; not a grid value; at 0 no level and no stop exit | SETTLED (the master, :1262); alternative: no zero input, a separate test build ((B) 3) | §3, §4 |
| Exit policies | BandOrVWAP / OppBand / Flat1559 | RULED (ruling 4 of 2026-11-06) | §3 |
| OppBand definition | The paper's opposite band, as in `_OppBand.cs` | RULED (Q4) | §3 |
| Flat1559 definition | BandOrVWAP exits, flatten on the 15:59 bar, as in `_Flat1559.cs` | RULED (Q5) | §3 |
| Grid size | 3 × 3 × 3 × 3 = 81, all stop-on | INFERRED (arithmetic from the RULED counts) | §3 |
| Stop rule | Evaluated on bar close, market exit next bar, no resting stop | RULED (ruling 1 of 2026-11-05) | §4 |
| ATR period | 14, fixed, not tuned | RULED (ruling 4 of 2026-11-06, "ATR 14") | §3, §9 |
| ATR period held as a constant | `AtrPeriod = 14` a constant, not an input | SETTLED (a code-design choice, not his word); alternative: an input fixed at 14 in every run ((B) 42) | §9 |
| ATR series | 14 completed RTH sessions (daily ATR) | RULED (Q6) | §4 |
| ATR computation | Simple mean of the last 14 completed RTH sessions' true ranges, from the 1-minute bars, in the strategy | SETTLED; alternative: a second, daily series with NT8's `ATR(14)` ((B) 4) | §4 |
| Stop level | Entry fill ∓ m × ATR(14), ATR at the entry bar, fixed | SETTLED; alternative: from the signal bar's close, or trailing ((B) 5) | §4 |
| Stop evaluation | Close of every 1-minute bar in a position | SETTLED; alternative: checkpoints only ((B) 6) | §4 |
| ATR warm-up | No entry until ATR(14) exists (15 completed sessions) | SETTLED; alternative: entries with no stop until ATR exists ((B) 7) | §4 |
| Stop bar | No entry on a stop exit's bar | SETTLED; alternative: allow a reversal ((B) 8) | §4 |
| Precedence | Session flat, then stop, then checkpoint exits and entries | SETTLED; alternative: stop before the session flat ((B) 9) | §4 |
| Windows | 252 / 63 / 63 sessions | RULED (D-2026-11-05-A item 2) | §5 |
| Partial last window | Dropped | RULED (ruling 4 of 2026-11-06) | §5 |
| Day-count convention | Mon–Fri file dates with a 09:31–16:00 bar; weekend-dated bars excluded | SETTLED; alternative: an exchange calendar ((B) 10) | §5 |
| Window warm-up | Prior bars feed band and ATR | SETTLED; alternative: each window's own first sessions ((B) 11) | §5 |
| IS → OOS | Pick on window k's IS, apply unchanged to its OOS; join the 17 OOS segments | SETTLED; alternative: anchored in-sample ((B) 12) | §5 |
| Data | Used as is; each window reports its hole dates and early-close sessions | SETTLED; alternative: no per-window count ((B) 37) | §5 |
| Objective class | Risk-adjusted return with a minimum trade count, never net profit | RULED (ruling 4 of 2026-11-06) | §6 |
| In-sample statistic | Annualised Sharpe of daily net P&L; selection only, not the gate's definition | SETTLED; alternative: per-trade Sharpe, Sortino or MAR ((B) 13) | §6 |
| Minimum trades | 100 per 252-session in-sample window | SETTLED; alternative: 150 ((B) 14) | §6 |
| Undefined statistic | Zero-sd configuration ineligible | SETTLED; alternative: score 0 ((B) 15) | §6 |
| No eligible configuration | Arm (b) flat in that OOS window; not profitable | SETTLED; alternative: carry the previous pick ((B) 16) | §6 |
| Tie-break | Anchor distance, then ascending lookback, k, m, policy | SETTLED; alternative: stop distance from 2.25, descending m ((B) 17) | §6 |
| PBO method | CSCV | SETTLED; alternative: block bootstrap ((B) 18) | §7 |
| CSCV rows | s12 … s1323 (1,312 = 16 × 82) | SETTLED; alternative: trim the newest 11 ((B) 19) | §7 |
| CSCV partitions | S = 16 blocks of 82; 12,870 splits | SETTLED; alternative: S = 8 ((B) 20) | §7 |
| Pick on a training set | §6's rule, minimum trades pro rata | SETTLED; alternative: no minimum ((B) 21) | §7 |
| Ranking | Ascending test Sharpe, average ranks; PBO = share λ ≤ 0 | SETTLED; alternative: ties by the §6 order ((B) 22) | §7 |
| No eligible configuration (CSCV) | Split counts as λ ≤ 0 | SETTLED; alternative: drop the split ((B) 23) | §7 |
| PBO threshold | Arm (b) counts only if PBO < 0.05 | RULED (ruling 4 of 2026-11-06; Q8) | §7, §8 |
| Where it runs | NT8 full-span runs per configuration through the bridge; selection and PBO on the Mac | RULED (Q7; D-2026-11-06-A item 2) | §7 |
| Inputs per run | All five inputs in every run's `params` | SETTLED; alternative: changed values only, template read back ((B) 24) | §7 |
| Truncated trade list | Exactly 5,000 trades → rerun or split by date | SETTLED; alternative: stop the batch ((B) 25) | §7 |
| Gross P&L | If gross, subtract $4.68 per round turn on the Mac | SETTLED; alternative: template commission 0, subtract always ((B) 26) | §7 |
| Walk-forward commission | $4.68 NQ round turn | RULED (ruling 2 of 2026-11-06) | §7 |
| Acceptance-run commission | $2.96 | SETTLED; alternative: $4.68 against recomputed figures ((B) 27) | §7 |
| Slippage and fill resolution | 2 ticks/side, Standard resolution | REPORTED BY D-2026-10-30-A (DECISIONS.md:247, :250); unchanged | §7 |
| Gates | All six Phase 3 gates for both arms; PBO < 0.05 also for arm (b) | RULED as his statement (Q8); as an O1 item OPEN (ruling 9) | §8 |
| Gate Sharpe definition and equity base (notes-4 source, DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)") | Not decided | OPEN (ruling 9) | §6, §8 |
| WFE for arm (a); WFE formula for arm (b) | Not decided | OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74) | §8 |
| GO / HOLD / REJECT on arm (b) | Not decided | OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74) | §8 |
| Arm (b) reporting | Always run and reported next to arm (a), with its PBO | SETTLED; alternative: only after arm (a) passes ((B) 28) | §8 |
| Max-DD gate base | Lower of 4% of the MFFU account size and MFFU's trailing limit | RULED (D-2026-11-05-A item 3); it stands as written; whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here (OPEN, ruling 9) | §8 |
| Per-tier reporting | Every window, 1 MNQ and 1 NQ, against every row of the WF spec §6 table | RULED (D-2026-11-05-A items 4–5) | §8 |
| Per-tier reporting rule | Static rows and the Builder 50K add-on row included; a contradiction shows both figures, the lower used | SETTLED; alternative: trailing-limit rows only, one figure per row ((B) 38) | §8 |
| $1,500 figure | Not a gate figure; only the Builder 50K add-on row; no breaker limit set | SETTLED for walk-forward use only; the breaker #6 figure is not decided here (breaker build; O4); alternative: adopt $1,500 ((B) 39) | §8 |
| Tier | None chosen; the pick is his after paper results | RULED (Q9); the pick OPEN | §8 |
| MNQ cost | $1.90 round turn | RULED (ruling 2 of 2026-11-06) | §8 |
| Worst drawdown per window | Closed-trade and end-of-day equity, each from the window start and carried across windows; the worst of the four judged | SETTLED; alternative: closed-trade only ((B) 40) | §8 |
| 1 MNQ method and contract size | From the 1 NQ trade list: (NQ gross ÷ 10) − $1.90 per round turn (INFERRED equivalence); 1 NQ and 1 MNQ both reported | SETTLED; alternative: an own MNQ run ((B) 41) | §8 |
| Branch | `arm-b/wf-tunables`, from main | SETTLED; alternative: `wf/arm-b` ((B) 29) | §9 |
| File and class | `ninjascript/PraxisNoiseAreaBreakoutArmB.cs`, class `PraxisNoiseAreaBreakoutArmB` | SETTLED; alternative: `PraxisNoiseAreaBreakout_ArmB.cs` ((B) 30) | §9 |
| Enum | `PraxisNoiseArmBExitPolicy { BandOrVWAP, OppBand, Flat1559 }` | SETTLED; alternative: base enum plus a `bool` ((B) 31) | §9 |
| Inputs | Lookback 14, NoiseMult 1.0, StopAtrMult 0.0, ExitPolicy BandOrVWAP, Contracts 1, with the §9 types and ranges | SETTLED; alternative: no `[Range]` limits ((B) 32) | §9 |
| Readback | Five input values printed once at `State.DataLoaded` | SETTLED; alternative: a file beside the trade export ((B) 33) | §9 |
| Base file | Byte-identical on main and on the branch | RULED (D-2026-11-05-A item 1, "baseline file unchanged") | §9 |
| Variant files | `_OppBand.cs` and `_Flat1559.cs` byte-identical on main and on the branch | SETTLED; alternative: retire them on the branch ((B) 34) | §9 |
| Acceptance tests | T1–T13 as below | SETTLED; alternative: one Mac-side end-to-end re-simulation in place of the per-rule oracles (spec §9) | §9 |

**Arm (b) code design.** No code is written here.
- Branch `arm-b/wf-tunables`, cut from main.
- New file `ninjascript/PraxisNoiseAreaBreakoutArmB.cs`, class `PraxisNoiseAreaBreakoutArmB`: the base logic plus the stop (spec §4) and the three policies (spec §3).
- New enum `PraxisNoiseArmBExitPolicy { BandOrVWAP, OppBand, Flat1559 }`, declared in the new file.
- `[NinjaScriptProperty]` inputs: `Lookback` 14, `NoiseMult` 1.0, `StopAtrMult` 0.0, `ExitPolicy` BandOrVWAP, `Contracts` 1.
- `AtrPeriod = 14` is a constant, not an input: SETTLED ((B) 42; alternative: an input fixed at 14 in every run). The value 14, not tuned, is RULED (ruling 4 of 2026-11-06, "ATR 14").
- Readback: at `State.DataLoaded` the strategy prints its five input values once.
- `ninjascript/PraxisNoiseAreaBreakout.cs`, `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs` and `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` stay byte-identical on main and on the branch.

**Acceptance tests T1–T13.** Full text: spec §9 (lines 159–225 of the spec). One line each:
- T1 (spec :180): run T1 (14, 1.0, 0, BandOrVWAP). Pass: the base file's trade list row for row and its totals, 1,190 / $197,327.60.
- T2 (spec :182): run T2 (14, 1.0, 0, OppBand). Pass: the `_OppBand.cs` run row for row, 810 / $210,182.40.
- T3 (spec :184): run T3 (14, 1.0, 0, Flat1559). Pass: the `_Flat1559.cs` run row for row, 1,190 / $193,017.60.
- T4 (spec :186): run T4 (14, 1.0, 1.5, BandOrVWAP). Pass: at least one `XStop`, each filling on the bar after the crossing close; no stop order. No `XStop` = not passed.
- T5 (spec :188): runs T4, T5a–T5e in order. Pass: (i) every run prints the five inputs sent; (ii) T5a, T5b, T5d differ from T4 and T5e equals T4; (iii) T5c differs from T4 when its condition holds, else UNTESTED.
- T6 (spec :190): (i) static reading of the code unit's diff, on the Mac; (ii) band oracle over every stop-on acceptance run. Pass: every listed use reads the property; printed σ and bands (at the 10:00 checkpoint of three named sessions only) and fill, ATR and level (at every entry) match the script to 1e-9; no stop order.
- T7 (spec :192): before every batch. Pass: the tab's commission template, backtest type, fill resolution and slippage read back as set ($2.96 acceptance, $4.68 walk-forward).
- T8 (spec :194): every stop-on acceptance run and the 81. Pass: checks (i)–(iv) against the stop oracle, after calibration, with power checks (a) and (b).
- T9 (spec :196): every T8 run. Pass: no `XStop` decided on a session-flat bar; open trades exit by the session flat. Passed only if a first crossing falls on a session-flat bar, else UNTESTED.
- T10 (spec :198): every T8 run. Pass: no entry fills on an `XStop` exit's fill bar. Passed only if its condition holds, else UNTESTED.
- T11 (spec :200): every stop-on acceptance run and the 81. Pass: (i) no entry before s16, counted as passed in a run only if the first checkpoint where the band exists and the rule holds falls before s16 (possible at Lookback 10 or 14 only), else UNTESTED for that run; (ii) the first entry is at the first checkpoint where band and ATR(14) exist and the rule holds.
- T12 (spec :202–:210): runs T12a, T12b, T12c (m = 1.5, the three policies); (iii)–(vi) also run over every other stop-on acceptance run and the 81. Pass: (i)–(vii): pairwise distinct trade lists, each policy's exit names, the policy-rule oracle, reversals, entry soundness, ties, power. Without an `XStop` in a run, (vii)'s "the stop runs with this policy" is UNTESTED for that run and reported, and (i)–(vi) still grade.
- T13 (spec :212): runs T13a–T13c (`Contracts = 2`) against T4, T12b, T12c. Pass: the same rows, quantity 2 on every row including `XStop`, and exactly 2 × the twin's net. Without an `XStop` in T13a–c the `XStop` part of (ii) is UNTESTED. (iii) assumes the $2.96 template charges per contract (UNVERIFIED); if a row shows $2.96, (iii) is graded on gross only and the per-order charge is reported to the master.

Per-input coverage table, copied by script from spec lines 216–222:

| Input | Dead input caught by | Partly wired (stop-Off path only) caught by | Wrong rule caught by | NOT caught |
|---|---|---|---|---|
| Lookback | T5(ii) (T5a = T4); T6(i); T6(ii) on T5a, T6c, T6d [the build prints the σ it trades on]; T12(iii)/(v) on those runs [an exit or entry moves]. Not T5(i): it prints the property | T5(ii) (T5a and T4 are both stop-on, so T5a = T4); T6(i); T6(ii) on T5a, T6c, T6d [the build prints the σ it trades on]. T1–T3 cannot (they run m = 0 at 14). Other partial wirings: `cnt < 14` left at `:257` while the loop reads the property, caught by T6(i), by T6(ii) at T6d (Lookback 10 never forms a band, so the prints are missing) and by T11(ii) at Lookback 18 [the wrong band admits an entry in s16–s18] | T6(ii) (σ and bands at the three named 10:00 checkpoints only; at entries it prints fill, ATR and level, not σ or bands) [the fault reaches a named checkpoint]; T12(iii)/(v) on every stop-on run [the wrong band moves an exit or entry]; T1–T3 if the fault also holds at 14 on the m = 0 path | `HistoryCap` (`:79`) left at 29: no behaviour change at Lookback ≤ 29, so every grid value; T6(i) only. A band fault confined to sessions not named for T6(ii) (e.g. prevClose taken from `Close1600` (base `:168–169`) in place of `Close[1]` (`:155`), 0 after early-close days, so the `:156` fallback drops the gap adjustment): caught only by T12(iii)/(v) if an exit or entry moves, and by T1–T3 if on the shared m = 0 path. A fault that moves no printed value, exit or entry in any run checked. A fault that only drops entries after a run's first |
| NoiseMult | T5(ii) (T5b = T4); T6(i); T6(ii) on T5b, T6c, T6d [as above]; T12(iii)/(v) [as above] | T5(ii) (T5b, T4 both stop-on); T6(i); T6(ii) on T5b, T6c, T6d [as above]. T1–T3 cannot. k on one bound only (`:263` property, `:264` constant): T6(i) line by line; T6(ii) LowerBound at k ≠ 1 | T6(ii) (the three named 10:00 checkpoints only, as above) [the fault reaches a named checkpoint]; T12(iii)/(v) [an exit or entry moves] | As Lookback (no printed value, exit or entry moves; a band fault confined to sessions not named for T6(ii); dropped later entries). k used inside the stop is a StopAtrMult fault (next row) |
| StopAtrMult | T5(iii) [T4 holds an `XStop` whose close does not reach the 2.25 level]; T6(ii) (the level ≠ fill ∓ m × ATR) [the build prints the level it uses]; T8 (i)–(iv) [the fixed distance moves a predicted stop exit]; T6(i). An m that also switches the stop off: T4 (no `XStop`) and T8 power (a), but these cannot tell it from a correct stop that does not trip at these m | Not applicable as worded: m = 0 is the stop-Off path itself, checked by T1–T3. Stop applied only under some ExitPolicy values: T8 (iii)/(iv) on that policy's runs (T12a–c, T6c, T6d and the 27 of each policy in the 81) [the oracle predicts a crossing there]. m used only in some paths (e.g. longs only, or the stop check only at one m value): T8 only — power (a) (one long and one short `XStop` at each m) [stops occur], and (iii)/(iv) [the correct stop would trip there]. Not T6(ii) (it prints the level, not the check) and not T5(iii) (it fails only when m changes nothing) | T8's four named wrong stops (power-checked (b)): one-minute ATR, band half-width, k in place of m, checkpoint-only. T6(ii) (wrong printed level). T9, T10 [each UNTESTED unless its condition holds]. T11 (gate) [(i)'s condition] | **Any stop fault at an m where no run has an `XStop`.** Whether any `XStop` occurs at 1.5, 2.25 or 3.0 is UNVERIFIED (see T4); at 3.0 it may never occur. §3 then permits no input that tests the stop, and it is reported to the master. Also: a wrong rule outside T8's four that moves no exit in the runs checked, and T9/T10 when UNTESTED. A stop applied only under some ExitPolicy values, at some m or on one side, where no run of that policy, m or side gives the oracle a crossing: then UNTESTED (T12(vii) reports UNTESTED, not a fail). T6(i)'s exemption for "the stop's own level, check and `XStop` exit" lets a stop branch gated on m's magnitude through, so T6(i) does not catch it |
| ExitPolicy | T5(ii) (T5d = T4, whatever the fixed policy); T12(i) unconditionally; T12(ii) (Flat1559's `FlatEOD` vs the 16:00 `Exit on session close`); T12(iii) on the runs whose policy differs from the fixed one [(vii)]. Not T5(i), not T6(ii) (no printed value depends on it) | T12(i) unconditionally (one path under the stop gives T12a = T12b = T12c); T12(ii); T5(ii) (T4 and T5d both run the one fixed path, so T5d = T4, whatever that path is); T6(i) (no `ExitPolicy` read inside a `StopAtrMult` branch). Honoured for exits but not for the 15:59 flatten under the stop: T12(ii). OppBand without its reversal under the stop: T12(iv) [an OppBand checkpoint exit occurs] | OppBand at the same-side band (`PraxisNoiseAreaBreakout.cs:209`, `:217`): T12(iii) on T12b, T6d and the 27 OppBand configurations [at any `XL`/`XS` where the two bands give different c*]; max/min swapped in BandOrVWAP: T12(iii) [an exit moves]; Flat1559 flatten on a later minute (e.g. 16:00): T12(ii) on T12c (trades open at the 15:59 close then exit by a 16:00 `Exit on session close`); on an earlier minute no T12(ii) clause fails, because no trade is open at a 15:59 close; at m = 0 T3 (row for row against `_Flat1559.cs`) catches either, where the fault is also on the m = 0 path | Names never separate BandOrVWAP from OppBand; only T12(iii) does. A policy fault that moves no exit or entry in any run checked; one seen only at ties (T12(vi)); dropped entries after a run's first. A Flat1559 flatten on a minute before 15:59 on the stop-on path only |
| Contracts | T13(ii), every row, unconditionally [a run with a trade]; T6(i) | T13(ii), unconditionally; T6(i). `XStop` with a fixed quantity 1: T13(i)–(iii) [an `XStop` in T13a–c], otherwise T6(i) only. Fixed-1 `FlatEOD`: T13c (ii). Fixed-1 reversal entry: T13(ii) [a reversal row] | A wrong multiple (e.g. 2 × Contracts or Contracts²: 4 ≠ 2): T13(ii) | Faults at other Lookback, k or m (T13 runs (14, 1.0, 1.5) only); at values other than 1 and 2; on an exit kind absent from T13's runs; wired on the stop-on path but not at m = 0 (harmless to the grid). Per-contract commission is read, not tested (T13(iii)) |

"Does NOT catch" lines of T6, T7, T12 and T13, copied by script from spec lines 191, 193, 211, 213 (fenced so the lines keep their bytes):

```text
    - **Does NOT catch:** (i) is a reading, not a run, so it misses a use that names the right property inside a wrong formula, and code the reviewer does not recognise as a use. (i)'s exemption for "the stop's own level, check and `XStop` exit" also lets a stop branch gated on m's magnitude through (e.g. the stop check only when `StopAtrMult < 2.0`); only T8 catches that (power (a); (iii)/(iv) where the correct stop would trip). (ii) misses a build that prints one value and trades on another (T8, T12); σ and band faults anywhere but the three named 10:00 checkpoints, because at entries (ii) prints the fill, ATR and level, not σ or the bands (e.g. prevClose taken from `Close1600`, 0 after early-close days, in sessions not named: caught only by T12(iii)/(v) if an exit or entry moves, and by T1–T3 if on the shared m = 0 path); ATR and level faults off the entry bars (T12's oracle covers exit checkpoints); and anything about `ExitPolicy` or `Contracts`, because no printed value depends on either. That is the hole that parked version 1. T12 and T13 close it, not T6.
    - **Does NOT catch:** anything in the strategy; a tab setting outside the four read back (15 baseline settings have no bridge field, bridge report `:29`) unless the 2a skill reads it; a change between the readback and a later run in the same batch; whether the template charges commission per contract (T13 reads it).
    - **Does NOT catch:** a missing entry after a run's first (no test checks that every checkpoint where the rule holds while flat has an entry); a policy fault that moves no exit or entry in any run checked; a fault seen only at the ties (vi) excludes; a stop disabled under one policy, when that policy's runs give the oracle no crossing (T8's (iii)/(iv) then predict nothing to miss, and (vii) reports UNTESTED, not a fail); fill-price faults on `XL`/`XS`/`FlatEOD` beyond T8's calibrated rules; a Flat1559 flatten on a minute before 15:59 on the stop-on path only ((ii) checks trades open at a 15:59 close, and there are none; T3 catches it only on the m = 0 path).
    - **Does NOT catch:** a `Contracts` fault seen only at other Lookback, k or m values (T13 runs (14, 1.0, 1.5) only); a fault at Contracts values other than 1 and 2 (e.g. a cap at 2); a quantity fault on an exit kind that occurs in none of T13's runs; `Contracts` wired on the stop-on path but not at m = 0 (no T1–T3 run is at 2; harmless to the grid, which has no m = 0 run).
```

Reference figures at the committed $2.96 commission (`docs/reports/2026-11-01-three-strategy-results.md:402-404`, OBSERVED by `sed -n`): base 1,190 trades / $197,327.60; OppBand 810 / $210,182.40; Flat1559 1,190 / $193,017.60.

Before test 2a passes, the code unit can reach WRITTEN only. T6(i) runs on the Mac. Everything else runs on the VM after 2a. No code is changed by this entry; the code unit is dispatched only after this entry is committed.

**S6 cross-block.**
- F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59) are untouched.
- F2 × Flat1559 is an interaction. A Flat1559 position runs past 11:30 (breaker #4), through 15:00 (breaker #5) and flattens before 16:00 (Deviation B). It is NOT resolved here.
- F3: the fill and slippage terms are used as D-2026-10-30-A sets them: Standard resolution, 2 ticks/side.
- O1 (`specs/SPEC_RUBRIC.md`:74): Q8 and "judged arm = (a)" are recorded as his statements. Whether they discharge O1 is left to the master and the auditor.
- O4 (`specs/SPEC_RUBRIC.md`:94) is untouched.
- The cost model is read, not changed. Walk-forward runs use $4.68 (`config/backtest-cost-model.json`:19, `"commission_round_turn_usd": 4.68`). Acceptance runs use $2.96, the committed reference runs' figure. $2.96 is not in the current cost model (`grep -n 2.96` finds no line, OBSERVED).

**S4 timing.** This entry is written before the code unit it authorises.

**NEEDS AMEAR.** Only these:
1. The tier pick, after paper results (Q9).
2. Ruling 9's open items ("Notes-4 unruled items stay open; none block anything."): a second Rithmic read-only connection; the CME wiki as a source; the equity base and the Sharpe definition, scoped in the notes-4 source (DECISIONS.md:978) as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" and read by the WF spec for the "OOS Sharpe ≥ 1.0" gate (D-2026-11-05-A item 3's DD-base ruling stands as written; whether it closes the notes-4 DD-gate item is NOT decided here); the O1 gate set (label REPORTED BY the return handoff :74), including WFE for arm (a) and the WFE formula for arm (b), and whether GO / HOLD / REJECT may rest on arm (b).

## 2026-11-07 — D-2026-11-06-A addendum: rulings 5-8 and 10 applied to the VM handoff

Unit `2026-11-07-vm-handoff-amendment` (praxis-manager), on the master's dispatch DECISION_LOG `2026-11-07T15:19:00Z` (WHO: praxis-master). Source rulings: D-2026-11-07-A, Amear's words at DECISIONS.md:1229–1234 (DECISION_LOG `2026-11-07T12:55:00Z`, WHO: amear). Nothing is installed, run or bought. D-2026-11-06-A's text is not edited.

- **Applied** (section line ranges OBSERVED by `grep -n '^## '` on the amended `vm/2026-11-06-vm-handoff.md`, 2026-11-07): rulings 5, 6, 7(4)(5)(7)(11)(12), 8 and 10 → §1 (:23–42) limits 4, 6 and 8; §2 (:43–57); §5 (:89–159) step 3.4's go-live note (step 3.4 at :131–139) and step 3.5 (:140–156); §6 (:160–250) gate, 4.2, 4.3 and 4.6; §7 (:251–288); §8 (:289–313) rows 3, 4, 5, 7, 9, 10, 11, 12 and the `Settled since 2026-11-06:` bullet; new §9 (:314–351).
- **Partial pass, his words** (ruling 6, DECISIONS.md:1230): "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then." No partial pass is logged now: 2a has not run.
- **pip.** His words (ruling 7(11), :1231): "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\." The bridge declares version floors, not pins: "floors only, no lock file" (`docs/reports/2026-11-06-cli-nt-bridge-code-read.md`:143). What "pinned" means on this bridge is the master's reading, per DECISION_LOG `2026-11-07T15:19:00Z` (WHO: praxis-master): "what "pinned" means on this bridge is the master's reading (INFERRED, labelled)". The rest is this unit's reading on the master's dispatch, INFERRED, not his word, changeable by him: Code's CODE-cli-setup reply may name only `jsonschema`, `numpy`, `pyarrow` and `tzdata` (each `name==version`) and the clone's own `-e .`, no extras; the commands use `pip install --no-deps` (and `--no-deps --no-build-isolation` for `-e .`), so `pip` fails rather than fetching anything unnamed. The step-3.5 STOP before `pip` stays as the confirmation point.
- **Hash STOP.** His words (ruling 7(7), :1231): "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." Scope reading, INFERRED, the master's, not his word, changeable by him: the rulings file's filing note calls it "a hard STOP condition for the VM session" (`docs/reports/2026-11-07-amear-rulings-morning.md`:42; DECISIONS.md:1268). On a mismatch the VM agent pastes the outputs, writes the STOP reply and `FINISHED`, and does nothing further in the VM session, not only in NT8, until a new Code reply. His words do not say whether the STOP ends test 2a or the session.
- **§9.** The master's proposal under ruling 7(12) ("(12) you propose how each arm runs through the bridge after 2a passes."). It awaits his word after 2a passes and is not in force.
- **Ruling 10.** Both go-live items are in `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (OBSERVED by `sed -n`): :35 in his 11-06 wording, "unmap Z: and turn the share off before real money"; :38, "remove the unauthenticated bridge request folders (or add auth) before real money". Nothing was edited there (`git diff --numstat HEAD` on that file prints nothing, OBSERVED).
- **Still his:** §8 rows 1, 2, 3 and 8; row 11's route half; who sets the Strategy Analyzer tab by hand; the account; whether the base packages' own dependencies and the build backend (`setuptools>=61`) count as "the bridge's pinned requirements". §8 row 6 is a pending value from the VM agent's step 1 (DECISIONS.md:1278).

**S4.** The authorising rows precede the work: D-2026-11-07-A (:1272, "these are APPLIED to `vm/2026-11-06-vm-handoff.md` by a later unit") and the DECISION_LOG `2026-11-07T15:19:00Z` dispatch. This addendum records the work.

**S6.** F1–F4 (`specs/SPEC_RUBRIC.md`) untouched. D-071 untouched: ruling 5 does not mention it (DECISIONS.md:1263).

## 2026-11-07 — D-2026-11-07-B addendum 1: early-close checkpoint and session numbering (master's decisions under delegation)

Unit `2026-11-07-arm-b-spec-addendum` (praxis-manager), on the master's dispatch DECISION_LOG `2026-11-07T16:45:00Z` (WHO: praxis-master). The two spec readings were raised by the arm (b) code unit, `docs/reports/2026-11-07-arm-b-code-manager.md` "Still the master's" items 1–2 (:652–:653) and "Does NOT cover" items 5, 13, 14 and 15 (:613, :624–:626). The quotes below are copied from that row by script, byte for byte.

**Both are the master's decisions under delegation (R-1104-2, DECISIONS.md:748), not Amear's word, changeable by him.** The row's own label, quoted: "TWO SPEC READINGS RAISED TO ME — both decided here as **master's decisions under delegation (R-1104-2), not Amear's word, changeable by him**:"

- **Decision (1), early-close checkpoint.** Master's decision under R-1104-2; not Amear's word; changeable by him. Quoted: "(1) EARLY-CLOSE CHECKPOINT: on an early-close last bar that is also a checkpoint (12:00 on 2025-01-20 and 2025-06-19), ArmB KEEPS the base's behaviour (checkpoint exits/entries still run; only the stop decision is suppressed on a session-last bar). Reason: strictest reasonable = zero divergence from the committed, observed base on the m = 0 path (T1–T3 exactness is the test that parked 867's predecessor); skipping step (3) only when m > 0 would put order calls inside a `StopAtrMult` branch, which T6(i) forbids; spec §4's precedence sentence is therefore CORRECTED to say step (1) pre-empts step (2) only, and the checkpoint step on an early-close last bar follows the base. Alternative (changeable): skip step (3) on that bar for all m, re-baselining T1–T3."
  - Alternative (named in the row): "Alternative (changeable): skip step (3) on that bar for all m, re-baselining T1–T3."
- **Decision (2), session numbering.** Master's decision under R-1104-2; not Amear's word; changeable by him. Quoted: "(2) SESSION NUMBERING: the spec's band-first-exists sessions are one early (s12/s16/s20 for Lookback 10/14/18, not s11/s15/s19) because s1 is never committed; §5 :85 and T11 :200 CORRECTED; T11(i) is testable only at Lookback 10 in s12–s15; the T6(ii)/T11 oracle must model the s1 drop; the ATR "from s16" claim stands."
  - Alternative: the row names none for (2). Reading, INFERRED, mine, not the master's word: (2) corrects an arithmetic consequence of the committed base (R19, `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md:89`), so there is no choice to name an alternative for. The warm-up rule itself keeps its version 2 alternative (spec §5).
- **Oracle inputs carried into the spec** (the same row, quoted): "Also carried into the spec as oracle inputs (no code change): weekend-dated bars in the data file (141 dates; RTH template drop INFERRED), early-close cut where NT8 cuts (12:00/12:15/14:03 vs the file's 13:15/13:00), enum numeric order {BandOrVWAP 0, OppBand 1, Flat1559 2} vs the base's — bridge must send by name."

**Spec lines changed** (`docs/specs/2026-11-06-walk-forward-values.md`, version 2 → version 2.1, in place; line numbers in the v2.1 file): :1 title and :3 status (version 2.1); :5 changelog line (new); :77 §4 Precedence (decision (1) appended as a "Version 2.1 correction"); :86 §5 Warm-up (s19 → s20 at Lookback 18, with the s1-drop reason and grades); :195 T8 (step (3) "skipped on a bar where (1) or (2) fired" → skipped where (2) fired; on F, (1) suppresses (2) only); :201 T11 (band from s12 / s16 / s20; T11(i) testable only at Lookback 10, in s12–s15; "or from Lookback 14 at k = 0.8" withdrawn); :228–:235 new subsection "Oracle inputs from the code unit (2026-11-07)", items (a)–(e). No other line changed (full `git diff` pasted in `docs/reports/2026-11-07-arm-b-spec-addendum-manager.md`). **Residuals not edited** (outside this dispatch's line scope; for the master): spec :270, the list (B) summary row 11, still reads "s19 (lookback 18)"; spec :219, the coverage table, still reads "[the wrong band admits an entry in s16–s18]", which under decision (2) would be s16–s19.

**Grades.** Decision (1) is SETTLED (master). Decision (2): s16 = 2021-03-29 and N = 1352 are OBSERVED by the code unit's data-file trace (code report :523–:539, E6); the s12 / s20 arithmetic is INFERRED. Nothing here is compiled, run or tested. The code file's behaviour under (1) (code report :652) is WRITTEN level only (code report :14).

**S4.** Written before the arm (b) code commit. The file `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` exists untracked (`git status --porcelain`: `?? ninjascript/PraxisNoiseAreaBreakoutArmB.cs`); the branch `arm-b/wf-tunables` does not exist yet (`git branch --list 'arm-b*' | wc -l` → `0`). Stated, not hidden: the code was written before this entry and already keeps the base's behaviour that decision (1) chooses (code report :652). This entry precedes the commit, not the writing.

**S6.** F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59) untouched. F2 × Flat1559 is still open (DECISIONS.md:1452); neither decision resolves it.

**S13.** No backtest or P&L figure is stated in this entry, so the standing sentence is not required here.

**NEEDS AMEAR.** None new. Both decisions are his to change; neither is asked of him here.

**Correction 1 to this addendum (DECISION_LOG 2026-11-07T16:50:00Z, after audit FAIL 1 on S4(ii)).** Written by correction unit `2026-11-07-arm-b-main-set-correction-2` on DECISION_LOG `[2026-11-07T17:00:00Z] WHO: praxis-master`. Two sentences of the "Spec lines changed" paragraph above (DECISIONS.md:1492) were true when written and stopped being true when Correction 1 edited the spec. Quoted verbatim from :1492:

> No other line changed (full `git diff` pasted in `docs/reports/2026-11-07-arm-b-spec-addendum-manager.md`).
>
> **Residuals not edited** (outside this dispatch's line scope; for the master): spec :270, the list (B) summary row 11, still reads "s19 (lookback 18)"; spec :219, the coverage table, still reads "[the wrong band admits an entry in s16–s18]", which under decision (2) would be s16–s19.

Both sentences are RETRACTED. Correction 1 made three in-place line edits to `docs/specs/2026-11-06-walk-forward-values.md`, on the authority of DECISION_LOG `[2026-11-07T16:50:00Z] WHO: praxis-master`; until this paragraph no DECISIONS.md line recorded them:

- :197 T9: a "Version 2.1 note" added at the end of the line. On an early-close last bar that is also a checkpoint, the checkpoint step still runs as in the base; whether NT8 fills an entry decided there, and in which session, is UNVERIFIED. It implements decision (1). Correction 2 (DECISION_LOG 2026-11-07T17:00:00Z) appended the label below to the note itself.
- :219 coverage table, Lookback row: `s16–s18` → `s16–s19`. It implements decision (2).
- :270 list (B) summary row 11: `s19 (lookback 18)` → `s20 (lookback 18)`. It implements decision (2).

Label: all three are the master's decisions under delegation (R-1104-2, DECISIONS.md:748), not Amear's word, changeable by him. They carry decisions (1) and (2) above into lines this addendum had left out, and add no new choice. The other spec line numbers given at :1492 stand, because the three edits are in place (spec `git diff --numstat HEAD` was `16 6` at the 16:50:00Z row and is `19 9` after Correction 1). The copy of the coverage table in D-2026-11-07-B above (DECISIONS.md:1429–1435, "copied by script from spec lines 216–222") still reads `s16–s18`. That copy is committed history and is not edited; the spec is the corrected text. This paragraph does not address the S4 timing finding of the same audit (the S4 paragraph above, :1496). That finding is open — Amear's.

## 2026-11-07 — D-2026-11-07-B addendum 2: ratification (WHO: amear) of addendum 1's timing

**Status:** RATIFIED by Amear — DECISION_LOG `2026-11-07T17:08:00Z` (**WHO: amear**; working tree, not yet in a commit). Appended by praxis-manager, unit `2026-11-07-arm-b-ratification-filing` (dispatch DECISION_LOG `2026-11-07T17:09:00Z`, WHO: praxis-master). Both quotes below are copied from the 17:08:00Z row by script, byte for byte.

- **The finding.** The auditor's S4(i) finding: addendum 1 (DECISIONS.md:1479–1516) was written after `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` was written, before any commit, and the file keeps the committed base's early-close checkpoint behaviour where spec v2 said the step is skipped.
- **The question put to him** (AskUserQuestion, the row's question text): "Arm (b) code audit FAIL 1 on S4 timing. The written strategy file keeps the committed base's behaviour on an early-close last bar (12:00 on 2025-01-20 and 2025-06-19): the checkpoint exits/entries still run there and only the stop is suppressed. Spec v2 said that checkpoint step is skipped on such a bar. I decided (under R-1104-2) to keep the base's behaviour and filed D-2026-11-07-B addendum 1 — but the file was written before that entry (both are uncommitted). The auditor: an after-the-fact entry needs your ratification, as with uqb addendum 6. Which do you rule?"
- **His answer, verbatim as returned by the tool:** "Ratify the timing"
- **Reading — the master's, not his words.** Addendum 1 stands as written; its timing is ratified by him; the base's early-close behaviour is kept; T1–T3 stay identical to the committed runs.
- **What he did NOT rule.** He was asked one question only. The R-1104-2-scope question raised by the spec-addendum unit stays open for the return handoff.
- **Precedent.** D-2026-11-04-B addendum 6 (DECISIONS.md:1192), the uqb ratification of addendum 5's timing.
- **Chain.** DECISION_LOG `2026-11-07T17:08:00Z` (WHO: amear) → this addendum → the commits.

**S6.** F1–F4 (`specs/SPEC_RUBRIC.md`) untouched. Nothing was compiled, run or tested.

**S13.** No backtest or P&L figure is stated in this entry, so the standing sentence is not required here.

## 2026-11-08 — D-2026-11-08-A: Amear's nine rulings R1–R9 (voice session, Claude.ai channel, 2026-11-08) — rulings WHO: amear; filed by praxis-manager

**Date:** 2026-11-08
**Status:** RECORDED — Amear's rulings, WHO: amear. The words are REPORTED BY the Claude.ai channel (its record of his voice session) and were pasted by Amear; the paste in `docs/reports/2026-11-08-amear-rulings-voice.md` is OBSERVED as received (REPORTED BY that file's line 3, written by praxis-master). S5 ledger authorisation: DECISION_LOG `2026-11-08T14:02:11Z` (**WHO: amear**; DECISION_LOG.md:718, working tree). Plan/dispatch: DECISION_LOG `2026-11-08T14:22:00Z` (WHO: praxis-master, :719). Correction 1: DECISION_LOG `2026-11-08T14:30:00Z` (WHO: praxis-master, :720) — the paste range is 12–79, not the 13–83 stated in :718, :719, DISPATCH_LOG `2026-11-08T14:24:00Z` (DISPATCH_LOG.md:2024) and the rulings file's line 9. Appended by praxis-manager, unit `2026-11-08-rulings-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** Three kinds, never mixed. (a) *Amear's words* = the fenced block below and nothing else, copied by script from the rulings file lines 12–79. (b) *Master's readings* = the rulings file's "Master's filing notes" 1–5 (`docs/reports/2026-11-08-amear-rulings-voice.md:86-90`), each labelled "master's reading (filing note N), changeable by Amear"; they are not rulings. A master's decision under R-1104-2 (DECISIONS.md:748) is labelled as such. The mapping of R1–R4 to return-handoff §4 items comes from his words ("answers §4 item 1", "§4 item 3" in the block); the mapping of R5–R9 to the strategy filter audit's §6 questions 1–4 is the master's (rulings file :3, "§6 of … (questions 1–4)"; DECISION_LOG :718) — his words say only "plus the strategy filter audit dated 2026-11-08"; each *Answers:* line for R5–R9 below is that master's mapping. (c) *The filer's readings* are labelled "INFERRED, the filer's, not his word". Line pointers are the filer's, each re-read with `sed -n` this session (OBSERVED) unless marked otherwise. S13: the standing sentence above is carried once in this entry; the pasted block carries no copy of it (`sed -n '12,79p' <rulings file> | grep -c` on its first three words = `0`, OBSERVED).

**The paste, verbatim (WHO: amear).** Rulings file lines 12–79, inserted by script, not retyped.

```text
PRAXIS — RULINGS FROM AMEAR, VOICE SESSION 2026-11-08 (Claude.ai channel)
WHO: amear. File each as a DECISIONS.md entry citing this session.
These answer return handoff 2026-11-07-return-handoff-claude-ai-2.md §4
items 1 and 3, plus the strategy filter audit dated 2026-11-08.

RULINGS
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)
    anchor at the 09:30 ET cash open. VM step 0 reads the live
    "CME US Index Futures RTH" template hours (T7 readback). If the
    live template starts 08:30 ET, the 2026-11-01 baselines are
    suspect and are re-run at 09:30 ET before either arm counts.
R2  GO requires arm (a) to pass. Arm (b) can only add confidence or
    block a GO; it can never carry a GO on its own (§4 item 3).
R3  Gate 6 (WFE) applies to arm (b) only (§4 item 3).
R4  Scoring, hybrid (§4 item 3, gate 2):
    - Win rate: no-trade days excluded; a break-even trade counts as
      half a loss.
    - Sharpe: daily returns, every trading day counted (no-trade
      days = 0), equity base = the account size actually traded.
    Check against the values-spec §6/§8 wording; flag any conflict
    back to Amear, do not resolve it.
R5  The fixed R:R shape filter (3:1 partial plus runner; 1.5:1) is
    retired for all automated-strategy research, including the
    higher-win-rate brief. A strategy qualifies if it is fully
    rule-based, net positive after costs, and survives every MFFU
    condition, including the EOD trailing drawdown and the
    consistency rule.
R6  Research and backtest, on the existing 1-minute data only,
    nothing bought (R-1104-3 stands):
    - Pre-Announcement Drift (Hu, Pan, Wang & Zhu 2022), evening-
      entry variant, exit before the release.
    - Macroeconomic Announcement-Day Premium (Savor–Wilson; Ai 2024).
    Runs in parallel with the walk-forward, not queued behind it.
    Before any build, read MFFU's current T1 news rule and confirm
    whether an evening entry counts as the same trading day.
R7  Parallel work runs in a separate git worktree on its own branch,
    never in the same working directory (v6y). NT8 runs on the VM
    take turns.
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
R9  FOMC-Cycle Even-Week stays parked while trading on MFFU
    (multi-day hold breaks flat-by-close). Revisit only if own
    capital is ever used.

HOUSEKEEPING (Code's job, not Amear's)
- The index holds 12 stale staged files from July–October (2026-08
  reports, the F4 evidence PNG, the ledger-compaction spec). Unstage
  or land them deliberately; never commit without a pathspec.
- Stray untracked file "F" (2026-07-28, contents "# DISPATCH LOG"):
  investigate, then remove or log.
- Audit-ledger flush still owed: surgical, nine 2026-11-07 lines,
  the three July/August as-is lines stay out.
- MFFU flat time is 16:10 in one doc and 16:59 in another: read
  MFFU's current terms and record which is right.
- HANDOFF.md line 7 says the bd remember save failed, but
  master-gate-route-2026-11-07 is in the beads store. Correct it
  append-only.
- Stale bead title on Praxis_build-867.

STILL OPEN FOR AMEAR (next session)
§4 items 2 and 4–12 of the 2026-11-07 return handoff, starting with
item 4 (the July SPEC_RUBRIC hunk, R-A/R-B/R-C). Bring a plain-
language summary of what those lines do.
```

**Copy check.** `sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256` = `73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263` (OBSERVED; equals the value in the rulings file's Correction 1, :94). The block body's hash after insertion: `73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263` (computed by the splice script from the assembled text; the post-insertion re-check is pasted in the unit report).

**Per-ruling pointers.** His words are in the block above; they are not restated here. No ruling is read past its words.

- **R1 — RTH session.** *Answers:* return handoff `docs/reports/2026-11-07-return-handoff-claude-ai-2.md` §4 item 1 (B1 session start, :61-65). *Bears on:* values spec `docs/specs/2026-11-06-walk-forward-values.md` T12(iii) "the session's typical-price VWAP from the 09:30 bar" (:206) and §4's ATR line "the last 14 completed RTH sessions" (:72) (both pointers REPORTED BY the return handoff :65; re-read here, OBSERVED); VM handoff step 0 (see R1 in the block above). Master's reading (filing note 2, :87), changeable by Amear: `docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208-219` at commit `29c3e13` prints a RESCUED copy of `CME US Index Futures RTH.xml` as Monday–Friday `830`–`1600`, TimeZone `Eastern Standard Time` (REPORTED BY that worker). The live VM template is UNVERIFIED. Conditional, per bd memory `amear-conditional-commitment`: nothing here asserts what the live template holds. Master's reading (filing note 2, :87), changeable by Amear: "If the T7 readback shows 08:30, R1's re-run clause fires for the three 2026-11-01 runs." His own condition is "If the live template starts 08:30 ET" (block above); the rescued copy carries its own TimeZone field, so whether a readback is "08:30 ET" depends on that field too (INFERRED, the filer's, not his word). The readback has not been observed; it is the observation that decides (INFERRED, the filer's, not his word). *Does NOT settle:* the template's actual hours; no spec wording is changed; the VM handoff step-0 line is a later unit (U3).
- **R2, R3 — which arm carries GO; gate 6.** *Answer:* return handoff §4 item 3 (:67) (his words: "(§4 item 3)" for each); R2 ↔ the part "whether GO / HOLD / REJECT may rest on arm (b)" and R3 ↔ "whether gate 6 applies to arm (a)" is the filer's assignment (INFERRED, the filer's, not his word). *Bear on:* values spec §8 :128 ("Judged arm = (a)" vs Q8 "both arms are judged against all six Phase 3 gates"), :132 (ii) and (iii), :133 ("The WFE formula for arm (b) … OPEN"); O1 (`specs/SPEC_RUBRIC.md:74-79`). Side by side, not reconciled here (INFERRED, the filer's, not his word): R3 "Gate 6 (WFE) applies to arm (b) only" and Q8 at values spec :121 "both arms are judged against all six Phase 3 gates"; raised to the master in the unit report. *Do NOT settle:* whether R2/R3 discharge O1 — the values spec :134 leaves "Whether Q8 discharges O1" to "the master and the auditor"; that the same holds for R2/R3 is INFERRED, the filer's, not his word, and Amear may rule on it; the WFE formula itself (:133) — R3's words do not give it; the values spec is not edited.
- **R4 — scoring, hybrid.** *Answers:* §4 item 3's "the gate 2 Sharpe definition and its equity base" (his words: "(§4 item 3, gate 2)"; the sub-part is the filer's assignment (INFERRED, the filer's, not his word)). R4 instructs "flag any conflict back to Amear, do not resolve it". Master's reading (filing note 3, :88), changeable by Amear, names the same checks. The checks are NEEDS AMEAR FLAGS 1–5 below. *Does NOT settle:* any of FLAGS 1–5; the values spec is not edited.
- **R5 — R:R shape filter.** *Answers:* strategy filter audit `docs/reports/2026-11-08-strategy-filter-audit.md` §6 Q1 (:211). *Bears on:* filter C3 (audit :88; §4.1 at :127). R5's words name "The fixed R:R shape filter (3:1 partial plus runner; 1.5:1)"; that this is the audit's C3 is INFERRED, the filer's, not his word — C3's cell at :88 also carries "avg win ÷ avg loss < 1.5 fails regardless of win rate", a clause R5's words do not name, so whether that clause is retired with it is not settled here. *Bears on:* the higher-win-rate brief requested in `docs/reports/2026-11-04-voice-session-notes-4.md:36` ("New work requested by Amear" item 1, heading :35) and audit :144. The audit is "recommendation only … **PROPOSED**" (:4), by the Claude.ai channel research agent (:3). *Does NOT settle:* the audit's other C filters and its §5 ranking are not adopted by this entry — R5's words rule on the fixed R:R shape filter only (INFERRED, the filer's, not his word).
- **R6 — two announcement studies.** *Answers:* audit §6 Q2 (:212); candidates at §5 (:175). *Pre-conditions, his words:* see R6 in the block above (MFFU's current T1 news rule; whether an evening entry counts as the same trading day). Neither is done here; both are U2 in the `14:22:00Z` plan, and U5 starts only after U2's MFFU T1 read. R-1104-3 stands: D-2026-11-04-A (DECISIONS.md:736), R-1104-3 (:752), the "No historical tick-data purchase" reading (:948). Nothing is bought. "Runs in parallel" — see R7. *Does NOT settle:* no study is started.
- **R7 — parallel work.** Names (v6y), identified (INFERRED, the filer's, not his word) as bead `Praxis_build-v6y` (CLOSED, "Gate/concurrency gap: audit token does not bind the staged tree; parallel sessions can inject files into a repo tip write"; OBSERVED `bd show`). Master's reading (filing note 4, :89), changeable by Amear: R7 does not change the serial-dispatch rules — "one praxis-manager at a time (bug `Praxis_build-9lj`)" and settlement 9. Bead `Praxis_build-9lj` is itself a bug about report grading (OPEN, "gate-manager-output.sh grades the newest docs/reports/*.md, so concurrent managers get each other's reports graded"); settlement 9 of D-2026-11-06-B ruling 5 (DECISIONS.md:1092; a master's decision under R-1104-2, not his word: "Code does not run agents while the VM session writes; handover goes through the VM handoff file"), operationalised as STARTED/FINISHED markers (`vm/replies/README.md:7`, `vm/2026-11-06-vm-handoff.md:37`). Note 4 also reads parallel = separate worktree and branch. R6's "Runs in parallel with the walk-forward, not queued behind it" and settlement 9's "Code does not run agents while the VM session writes" sit side by side on their face; how they combine is not settled here (INFERRED, the filer's, not his word). It is not listed under NEEDS AMEAR, because this unit's brief limits that list to the R4 flags and the R8/F2 question; it is raised to the master in the unit report, and the master operates on note 4 (master's reading (filing note 4), changeable by Amear). *Does NOT settle:* no worktree or branch is created here.
- **R8 — F2 and the breakers.** *Answers:* audit §6 Q3 (:213). Master's reading (filing note 1, :86), changeable by Amear: only Amear edits `specs/SPEC_RUBRIC.md` (:3-4, "The build side does not edit this file. It proposes changes; Amear applies them."). F2's unblock condition (:41-42) is "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match." The master's note says that artifact does "not exist yet". The master treats R8 as unblocking a PROPOSAL unit on breakers #2, #3, #4, #5-system and #8, values returned PROPOSED, and NOT as unblocking Block 3 or Block 4 work (F2 "Blocks." :43). Master's reading (filing note 1), changeable by Amear: the F2 state line in the rubric changes by Amear's hand, and he may override the master's reading. *Does NOT settle:* this entry does not edit the rubric. The block carries R8's words on #4 and #5; whether those words name F2's governing rule or its 15:00 disposition is not decided here — FLAG 6. Audit §6 Q3 also asks "Do you want this audit filed as an input to F2?"; R8's words do not answer that yes/no, and R8 adds #8, which Q3 does not name (INFERRED, the filer's, not his word).
- **R9 — FOMC-Cycle Even-Week.** *Answers:* audit §6 Q4 (:214). *Bears on* (INFERRED, the filer's, not his word): §4.4 "Overnight-hold parking" (:165). *Does NOT settle:* nothing beyond his words.

**HOUSEKEEPING (rulings file lines 61–74; Code's, per his words).** Six items, listed in the block above: the 12 stale staged files; the stray untracked `F`; the surgical audit-ledger flush; the MFFU flat time (16:10 vs 16:59) against MFFU's current terms; HANDOFF.md line 7, append-only; the stale title on `Praxis_build-867`. None is acted on in this unit; they are U2 in the `14:22:00Z` plan.

**STILL OPEN (rulings file lines 76–79; Amear's).** Return handoff §4 items 2 and 4–12, item 4 first (the July rubric hunk, R-A/R-B/R-C). None is answered here.

**What this entry does NOT do.** No code. No run. No VM edit. No purchase. No spec or rubric edit. No ledger edit. No housekeeping item done. No FLAG resolved.

**S4 timing.** This entry is written before any unit that depends on R1–R9 is dispatched. The dependents are U2–U5 in the DECISION_LOG `2026-11-08T14:22:00Z` plan: U2 housekeeping, including the read of MFFU's current terms; U3 VM handoff amendment 2 (the step-0 template-hours line and R1's re-run clause); U4 the F2 breaker-values PROPOSAL; U5 R6 research on branch `research/announcement-drift` in its own worktree, after U2's MFFU T1 read. Master's reading (filing note 5, :90), changeable by Amear, per bd memory `master-s4-entry-before-code`: the master verifies this entry on disk before dispatching them.

**S6 cross-block (interactions only; nothing decided here).** F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59; `grep -n '^### F'`, OBSERVED) are not modified by this unit; `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0` (the pre-existing July hunk, OBSERVED). Interactions: R8↔F2 (FLAG 6); R2/R3↔O1 (:74); R4↔O4 (:94; FLAG 3); R1↔values spec :72 and :206.

**NEEDS AMEAR.** Each flag sets two texts side by side. Not resolved here; no reading is picked.

- **FLAG 1 — R4 vs the §6 selection statistic.** Values spec §6 :92: "**as the in-sample selection objective only**: annualised Sharpe of daily net P&L … d_i = sum of the net P&L … of trades exited in session i, 0 if none. S = mean(d) / sd(d) × √252, sd with n − 1, risk-free rate 0 … dollar P&L at 1 NQ needs no equity base." R4 (block above): "equity base = the account size actually traded". Whether R4 applies to the gate only, or also changes §6's selection statistic — his (the question is raised by master's reading (filing note 3, :88), changeable by Amear). Not resolved here.
- **FLAG 2 — R4 vs the gate-2 open item.** Values spec :93: "This statistic does NOT define the gate "OOS Sharpe ≥ 1.0". The gate's Sharpe definition and its equity base stay OPEN under ruling 9"; §8 :132 (i) the same. R4 supplies daily returns, no-trade days = 0, equity base = the account size actually traded. Open within it (INFERRED, the filer's, not his word): "the account size actually traded" names no figure — "The tier pick is OPEN" (:137, Q9); whether the base is the MFFU account size, the 1 NQ / 1 MNQ figure (:139), or something else; and whether √252, n − 1, rf 0 and the net-of-costs basis ("after commission and slippage") from :92 carry over — R4's words name none of them. His. Not resolved here.
- **FLAG 3 — R4's win-rate rule vs the gate list.** R4 heads itself "(§4 item 3, gate 2)" and includes a win-rate rule. The six gates (:121-127) carry no win-rate gate; gate 2 is "OOS Sharpe ≥ 1.0" (:123). A win-rate figure appears in O4's Block 4 gate, "within ±15% win rate" (`specs/SPEC_RUBRIC.md:96-97`). Where R4's win-rate rule applies — his. Also open (INFERRED, the filer's, not his word): whether R4's win rate is counted per trade or per day ("no-trade days excluded" names days; "a break-even trade" names trades), and whether it is the same quantity as O4's "±15% win rate". Not resolved here.
- **FLAG 4 — the 4% DD equity base.** Values spec :93 and :132 cite DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)". :135: "Max-DD gate base — RULED (D-2026-11-05-A item 3, DECISIONS.md:814 …)", with the notes-4 item kept OPEN. R4's words name Sharpe and win rate, not the drawdown gate (INFERRED, the filer's, not his word). Whether the 4% DD equity-base item stays open — his. Not resolved here.
- **FLAG 5 — "trading day" vs "session".** R4: "every trading day counted (no-trade days = 0)". Values spec :92 counts per session i ("For the in-sample sessions i = 1…n") ("trades exited in session i"). R6 asks to "confirm whether an evening entry counts as the same trading day". Whether R4's "trading day" is the session i of :92 — his (INFERRED, the filer's, not his word). Not resolved here.
- **FLAG 6 — R8 and F2's state.** Does R8 change F2's state in `specs/SPEC_RUBRIC.md` — do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition — and is master's reading (filing note 1), changeable by Amear, right? The rubric is his to edit (:3-4). Not resolved here.

## 2026-11-08 — D-2026-11-08-A Correction 1: FLAG 6 side-by-side, filing form labelled, three minor labels (after audit FAIL 1 and the Correction-1 adversary)

**Date:** 2026-11-08
**Status:** CORRECTION to D-2026-11-08-A. Lines :1534–1645 are NOT edited; a wrong line stays beside its correction. Authorisation (S5): DECISION_LOG `2026-11-08T14:57:00Z` (WHO: praxis-master, DECISION_LOG.md:725, working tree). Source of findings: the Correction-1 adversary block, `docs/reports/2026-11-08-rulings-filing-manager.md:965–1049` (`VERDICT: REFUTED`, :970). Appended by praxis-manager, unit `2026-11-08-rulings-filing-correction-2`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** Every quotation below was produced by script (`sed -n` / `grep -o`) from the file and line cited; none is retyped. Where a quote spans two or more source lines, the lines are joined by script with one space, and the leading label and indent are dropped; the quote's pointer gives the line range. Amear's words carry WHO: amear and a pointer. Other sentences carry one of three labels: "master's reading, changeable by Amear"; "master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear"; "INFERRED, the filer's, not his word". Line pointers were re-read this unit (OBSERVED).

**Cure for finding 1 (FLAG 6, side by side).** Amear's words, R8 (WHO: amear; DECISIONS.md:1583–1589):

```text
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
```

Master's reading (filing note 1, rulings file :86), changeable by Amear: "Until it does, the master treats F2 as still blocking Block 3 and Block 4 work, and treats the proposal unit as unblocked."

The master's row DECISION_LOG `2026-11-08T14:57:00Z` (:725) says his A6 "now answers it"; A6 opens "FLAG 6:" (OBSERVED). FLAG 6 also asks "do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition" (:1645); A6's words do not name that part, and this entry does not read A6 as settling it or as leaving it open. A6 (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, DECISION_LOG.md:723 — a hand stamp, "about 19 minutes ahead; the order of events in this ledger is correct" per DECISION_LOG `2026-11-08T14:47:00Z`, :724; answers file `docs/reports/2026-11-08-amear-answers-flags.md`:38–39):

```text
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
```

Master's reading, changeable by Amear: the F2 breaker-values PROPOSAL unit (U4 in the DECISION_LOG `2026-11-08T14:22:00Z` plan) is authorised. Master's reading, changeable by Amear: F2's state in `specs/SPEC_RUBRIC.md` changes only on his approval of the proposed values. FLAG 6's sentence "The rubric is his to edit (:3-4)." (DECISIONS.md:1645) is superseded by his A11 (master's reading, changeable by Amear). A11's first two sentences (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :50–51, joined): "Amear no longer edits any repo file by hand, including specs/SPEC_RUBRIC.md. Amear decides; agents write." Master's reading, changeable by Amear: the rubric is now edited by agents. A11's third sentence (**WHO: amear**; answers file :51–53, joined): "Every rubric edit cites a logged Amear approval inline and passes the auditor before commit." A11's replacement of the rubric's :3-4 sentence is NOT done here. Nothing is resolved beyond his words.

**Cure for finding 2 (filing form).** Amear's words (WHO: amear; DECISIONS.md:1546, inside the fenced block): "WHO: amear. File each as a DECISIONS.md entry citing this session." Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear: the nine rulings are filed as ONE entry, D-2026-11-08-A, with a labelled section per ruling (eight bullets at DECISIONS.md:1619–1626; R2 and R3 share one, :1620). The decision is on the ledger at DECISION_LOG `2026-11-08T14:57:00Z` (WHO: praxis-master, DECISION_LOG.md:725): "Master's decision under R-1104-2, changeable by him: one entry per ruling-set with a labelled per-ruling section each". It follows the master's plan, DECISION_LOG `2026-11-08T14:22:00Z` (DECISION_LOG.md:719): "U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9". The alternative the master named and did not take (:725, "alternative = nine separate entries"): nine separate entries, one per ruling. Precedent (OBSERVED, DECISIONS.md:1052): `## 2026-11-06 — D-2026-11-06-B: Amear's evening rulings 1–5 and loop a–e (voice, 2026-11-06)`. INFERRED, the filer's, not his word: his own answers heading "File as D-2026-11-08-B" (answers file :16, WHO: amear) covers eleven answers, A1–A11, in one entry. Whether one entry satisfies "File each" is his question; it is under NEEDS AMEAR, unanswered.

**Cure for finding 3 (filing note 3's lean).** Filing note 3 (rulings file :88) also says: "R4 fills the gate definition." That sentence is the master's reading at the time of filing (filing note 3), changeable by Amear; D-2026-11-08-A did not carry it. That his A1 and A2 now rule on that subject is INFERRED, the filer's, not his word (their openings are "FLAG 1:" and "FLAG 2:"; the master's row :725 says "his A1/A2 now rule on it"). A1 and A2 (**WHO: amear**; DECISION_LOG `2026-11-08T15:05:00Z`, :723; answers file :18–23):

```text
A1  FLAG 1: R4 applies to gate 2 only. The values-spec §6 in-sample
    selection statistic stays as written.
A2  FLAG 2: Gate 2 "OOS Sharpe >= 1.0" = the §6 formula on
    out-of-sample sessions: daily net P&L after commission and
    slippage, 0 on no-trade sessions, sqrt(252), sd n-1, risk-free 0.
    Fixed base, no compounding; tier pick not needed for this gate.
```

No reading of the filer's is added.

**Cure for finding 4 (the brief's limit).** DECISIONS.md:1624 says "this unit's brief limits that list to the R4 flags and the R8/F2 question". REPORTED BY master (DECISION_LOG `2026-11-08T14:57:00Z`, :725): that limit rests on the master's dispatch MESSAGE to U1, "REPORTED BY master, not on disk". The same row quotes the brief: "NEEDS AMEAR: the R4 flags; the R8/F2 rubric-edit question; nothing else invented". Grade: REPORTED BY master, UNVERIFIED on disk.

**Cure for finding 7 (unlabelled sentence in R8).** DECISIONS.md:1625 carries, without a label: "The master treats R8 as unblocking a PROPOSAL unit on breakers #2, #3, #4, #5-system and #8, values returned PROPOSED, and NOT as unblocking Block 3 or Block 4 work (F2 "Blocks." :43)." Label attached here: master's reading (filing note 1), changeable by Amear.

**Findings 5, 6, 8, 9 — carried as wording, not cured** (DECISION_LOG :725: "(5)(6)(8)(9) — wording/labels, carried as noted, not individually cured"). Nothing is added for any of them.
- Finding 5: "some identifications carry no label." Carried as wording.
- Finding 6: "FLAG 4 (:1643) quotes only one side." Carried as wording.
- Finding 8: "the evidence-grades line (:1540) says Amear's words are "the fenced block below and nothing else"." Carried as wording.
- Finding 9: "R5 is listed as "Answers" audit Q1 (:1622)." Carried as wording.

**S4.** This entry is written before D-2026-11-08-B is filed (`grep -c '^## .*D-2026-11-08-B' DECISIONS.md` = `0`, OBSERVED) and before U4 is dispatched (no 2026-11-08 U4 row in DISPATCH_LOG, OBSERVED). The decision to correct by append is DECISION_LOG `2026-11-08T14:57:00Z` (WHO: praxis-master), logged before this unit ran.
**S5.** No approval is inferred. A1, A2, A6 and A11 are cited from the ledger row `2026-11-08T15:05:00Z` (**WHO: amear**, DECISION_LOG.md:723).
**S6.** F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59; `grep -n '^### F'`, OBSERVED) untouched. `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md` (the pre-existing July hunk, OBSERVED).
**S13.** The standing sentence is carried once, in the header. No backtest or P&L figure is stated in this entry.

**NEEDS AMEAR.** (i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546). Nothing else.

## 2026-11-08 — D-2026-11-08-B: Amear's answers A1–A11 to the D-2026-11-08-A FLAGS, plus the routed items and the standing rule change A11 (voice session, Claude.ai channel, 2026-11-08) — filed WHO: amear

**Date:** 2026-11-08
**Status:** RECORDED — Amear's answers, WHO: amear. The words are REPORTED BY the Claude.ai channel (its record of his voice session) and were pasted by Amear; the paste in `docs/reports/2026-11-08-amear-answers-flags.md` is OBSERVED as received (answers file :3, written by praxis-master). S5 ledger authorisation: DECISION_LOG `2026-11-08T15:05:00Z` (**WHO: amear**; DECISION_LOG.md:723). Its stamp is a hand estimate about 19 minutes ahead of the clock; the order of events is right, per DECISION_LOG `2026-11-08T14:47:00Z` (WHO: praxis-master, :724), which also records the ruling block range 15–56 and its sha. Dispatch of this unit: DECISION_LOG `2026-11-08T15:20:30Z` (WHO: praxis-master, :731). Filing form: his own heading line in the block, "WHO: amear. File as D-2026-11-08-B, citing this session." (answers file :16). INFERRED, the filer's, not his word: that heading covers all eleven answers, A1–A11, in this one entry. Contrast D-2026-11-08-A Correction 1, "Cure for finding 2" (DECISIONS.md:1678), where one entry was a master's decision under R-1104-2. Appended by praxis-manager, unit `2026-11-08-answers-filing`.
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** Never mixed. (a) *Amear's words* = the fenced block below and nothing else, copied by script from answers file lines 15–56. (b) The answers file's filing notes 1–5 (:64–68) are labelled "master's reading, changeable by Amear"; a master's call is labelled "master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear". (c) The filer's readings are labelled "INFERRED, the filer's, not his word". Line pointers are the filer's, each re-read with `sed -n` / `grep -n` this session (OBSERVED). Answer line ranges in the answers file: A1 :18–19, A2 :20–23, A3 :24–28, A4 :29–34, A5 :35–37, A6 :38–39, A7 :40–41, A8 :42–44, A9 :45, A10 :46–47, A11 :50–56 (heading "STANDING RULE CHANGE" at :49). A1–A6 open with "FLAG 1:" … "FLAG 6:" (his words). That A7–A10 answer the routed items (2a), (2c), (3) and (2b) of DECISION_LOG `2026-11-08T14:35:00Z` (:721) is the master's mapping (answers file :3), master's reading, changeable by Amear.

**The answers, verbatim (WHO: amear).** Answers file lines 15–56, inserted by script, not retyped.

```text
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

**Copy check.** `sed -n '15,56p' docs/reports/2026-11-08-amear-answers-flags.md | openssl dgst -sha256` = `7aebc0158f6d4b1907a7eeaab0d84e5835789fee91512e6d489d5acf857e9fdd` (OBSERVED; equals the value in DECISION_LOG `14:47:00Z`); the fenced body's hash after insertion is pasted in the unit report `docs/reports/2026-11-08-answers-filing-manager.md`.

**Per-answer pointers.** His words are in the block above; they are not restated here. No answer is read past its words.

- **A1.** *Answers:* FLAG 1 (DECISIONS.md:1640). *Amends / supersedes:* nothing; bears on values spec `docs/specs/2026-11-06-walk-forward-values.md`:92 (§6 "Statistic — SETTLED, as the in-sample selection objective only"), which his words keep. *Left for a later unit:* nothing is amended in the values spec here.
- **A2.** *Answers:* FLAG 2 (:1641). *Bears on:* values spec :93 ("This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".") and :132 (i). Whether A2 also closes the notes-4 "Sharpe definition (item 4)" (DECISIONS.md:978) is not decided here: NEEDS AMEAR (iv). *Left for a later unit:* the values-spec amendment.
- **A3.** *Answers:* FLAG 3 (:1642). *Bears on:* O4 (`specs/SPEC_RUBRIC.md:94-99`; the Block 4 "within ±15% win rate", :96-97, joined) and R4's win-rate line (DECISIONS.md:1560–1561, "a break-even trade counts as half a loss", joined). O4's "**Required:**" statement (whether the Block 2 backtest runs with breakers applied, without them, or both; :97-99) is not addressed by A3, and O4 is not discharged here (INFERRED, the filer's, not his word). *Left for a later unit:* any O4 write-up; NEEDS AMEAR (i) below.
- **A4.** *Answers:* FLAG 4 (:1643). *Amends:* D-2026-11-05-A item 3 (DECISIONS.md:814, "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit") — his words "This amends D-2026-11-05-A item 3". *Closes:* the notes-4 DD equity-base item (DECISIONS.md:978, "equity base for the 4% DD gate (item 5)") — his words. *Left for a later unit citing B:* values spec :135 ("Max-DD gate base — RULED …"); the WF spec `docs/specs/2026-11-05-walk-forward-spec.md` lines that carry "4%" (`grep -n '4%'`, OBSERVED: :31 and :39 in §1, which quote the ruling and the brief; :107 and the per-tier table header :113 in §6; :156 in §8, the verbatim gate). Which of these the amendment unit changes is the master's: filing note 4 (:67) names "WF spec §6 lines that carry 4%" (master's reading, changeable by Amear). Tier pick stays Q9 (values spec :137). Not edited here. See NEEDS AMEAR (ii).
- **A5.** *Answers:* FLAG 5 (:1644). *Bears on:* first half, values spec §6 session i (:92) and R1. Second half ("MFFU's own definition from its current terms") depends on a later read of MFFU's current terms — master's reading (filing note 5, answers file :68), changeable by Amear: "U2 records that definition". Nothing is assumed about MFFU's definition here (bd memory `amear-conditional-commitment`: no claim about an unobserved mechanism). *Left for a later unit:* the values-spec amendment; U2's MFFU read.
- **A6.** *Answers:* FLAG 6 (:1645). Master's reading, changeable by Amear (Correction 1, DECISIONS.md:1676): the breaker PROPOSAL unit (U4) is authorised, and F2's state in `specs/SPEC_RUBRIC.md` (:30-43) changes only on his approval of the proposed values. *FLAG 6 RESIDUAL:* D-2026-11-08-A Correction 1 (DECISIONS.md:1669) records that FLAG 6 also asks whether R8's words on #4 and #5 name F2's governing rule and 15:00 disposition, and that "A6's words do not name that part, and this entry does not read A6 as settling it or as leaving it open". Master's reading, changeable by Amear (DECISION_LOG `2026-11-08T15:13:00Z`, :728): that content is the F2 PROPOSAL unit's output, returned PROPOSED. Not resolved here.
- **A7.** *Answers:* the routed item (2a) of DECISION_LOG `2026-11-08T14:35:00Z` (:721): R3 "Gate 6 (WFE) applies to arm (b) only" vs Q8 "both arms are judged against all six Phase 3 gates" ("R3 vs Q8" is the answers file's wording, :3). *Amends:* Q8 in D-2026-11-07-A (DECISIONS.md:1226; restated :1253, :1286) — his words "R3 amends Q8". *Bears on:* values spec :121 (Gates — RULED (Q8 …)) and :128 (Judged arm = (a)); and :132 (ii) (whether WFE applies to arm (a)). *Left for a later unit:* the values-spec amendment.
- **A8.** *Answers:* routed item (2c) "whether R2/R3 discharge O1" (:721), and gives the gate-6 (WFE) formula left OPEN at values spec :133. O1 (`specs/SPEC_RUBRIC.md:74-79`) is discharged — his words. *Left for a later unit:* the rubric's O1 state (state values at rubric :10-11) is not changed here; master's reading (filing notes 1 and 3, :64, :66), changeable by Amear: it changes in a later unit (note 1's "O1 state change under A8", listed apart from the "rubric edit under A11"), and any rubric edit follows A11's rule. Also later: the values-spec amendment for :132–:134. Master's reading (filing note 3, :66), changeable by Amear: "`PASSED@<sha>` is the rubric's "graded and closed" state … the sha is the commit that lands D-2026-11-08-B". See NEEDS AMEAR (iii).
- **A9.** *Answers:* routed item (3), audit §6 Q3's yes/no (`docs/reports/2026-11-08-strategy-filter-audit.md:213`, "Do you want this audit filed as an input to F2?"). *Effect:* the audit is an input to F2 (his words). It stays "recommendation only … PROPOSED" (audit :4); that nothing in it is adopted by A9 is INFERRED, the filer's, not his word. *Left for a later unit:* master's reading (filing note 1, :64), changeable by Amear: the F2 PROPOSAL unit U4 takes it as input.
- **A10.** *Answers:* the master's settlement-9 call (2b) in DECISION_LOG `14:35:00Z` (:721), on settlement 9 of D-2026-11-06-B (DECISIONS.md:1092). The call itself is a master's decision under R-1104-2 (DECISIONS.md:748), now accepted by Amear (A10, WHO: amear). *Left for a later unit:* nothing.
- **A11 — STANDING RULE CHANGE.** *Changes:* who edits the rubric and any repo file. *Supersedes:* the rubric's :3-4 sentence ("The build side does not edit this file. It proposes changes; Amear applies them.", joined); that it is replaced is his word ("Replace the rubric's … accordingly", answers file :53–54, joined). That A11 also supersedes D-2026-11-08-A's FLAG 6 sentence "The rubric is his to edit (:3-4)." (DECISIONS.md:1645) is master's reading, changeable by Amear (Correction 1, :1676). *Left for a later unit:* the replacement of `specs/SPEC_RUBRIC.md:3-4`; the rubric is not edited here. Master's reading (filing note 2, :65), changeable by Amear: the rubric unit "builds its blob from HEAD's rubric plus the :3-4 change only", so the July hunk (`10 0`) stays out.

**Master's filing notes 1–5 (answers file :64–68).**
- Master's reading (filing note 1, :64), changeable by Amear: B is appended "only after D-2026-11-08-A's commit lands"; then "B filed → verified on disk → the units it authorises … are dispatched, one manager at a time". The precondition is met: HEAD `19ae6c8` (DECISION_LOG `15:20:30Z`, :731).
- Master's reading (filing note 2, :65), changeable by Amear: "A11 replaces `specs/SPEC_RUBRIC.md:3-4` by an agent's hand"; the July hunk stays out "unless he rules on it"; A11 also supersedes part of bd memory `amear-walkthrough-preference`.
- Master's reading (filing note 3, :66), changeable by Amear: "the sha is the commit that lands D-2026-11-08-B; the auditor of the rubric unit confirms the written statement O1 asks for exists at that sha".
- Master's reading (filing note 4, :67), changeable by Amear: the values spec "Max-DD gate base" line (:135) and the WF spec §6 lines that carry 4% "need an amendment unit citing B. Not done at filing."
- Master's reading (filing note 5, :68), changeable by Amear: A5's second sentence "depends on U2's read of MFFU's current terms"; "nothing is assumed about it here".

**FLAG 6 residual.** See the A6 bullet: per Correction 1 (DECISIONS.md:1669), "A6's words do not name that part" (FLAG 6's "#4 and #5" part). Not resolved here; master's reading, changeable by Amear (DECISION_LOG `15:13:00Z`, :728): it is the F2 PROPOSAL unit's output, returned PROPOSED.

**What this entry does NOT do.** No spec, rubric, values-spec, WF-spec, ledger or VM edit. No O1 or F2 state change. No MFFU read. No code, no run, no purchase.

**S4 timing.** This entry is written before any unit that acts on it is dispatched. Master's reading (filing note 1, :64), changeable by Amear: the units B authorises are "rubric edit under A11; values-spec amendments for A2/A4/A5/A7/A8; O1 state change under A8; A9 into the F2 proposal unit U4" (the identification of F2's input with U4 is that note's, not his word). DECISION_LOG `15:20:30Z` (:731, WHO: praxis-master): "the units B authorises (A11 rubric edit; values/WF-spec amendments for A2/A4/A5/A7/A8; O1 state change under A8) are dispatched only after B is OBSERVED on disk". U2 (housekeeping, including the read of MFFU's current terms) and U4 are in the U1 plan, DECISION_LOG `2026-11-08T14:22:00Z` (:719), which gates them on U1's entry ("U2–U5 are dispatched only after U1's entry is OBSERVED on disk"); filing note 1 also lists "A9 into the F2 proposal unit U4" among B's units. Which gate holds U4 is the master's; this entry picks neither. One act on A11 precedes this entry: DECISION_LOG `14:47:00Z` (:724, WHO: praxis-master) records `bd remember --key amear-walkthrough-preference` "UPDATED for A11". That act rests on row `15:05:00Z` (WHO: amear), not on this entry; whether it needed a DECISIONS.md entry first is the master's to answer (disclosed here, not cured). That A5's second half waits on U2's read is master's reading (filing note 5, :68), changeable by Amear.

**S5.** No approval is inferred. His words are cited from the answers file :15–56, which is filed under the ledger row `15:05:00Z` (WHO: amear, DECISION_LOG.md:723); that row is the authorisation.

**S6 cross-block (interactions only; nothing decided here).** F1–F4 (`specs/SPEC_RUBRIC.md`:17, :30, :45, :59) are not modified; `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md` (the pre-existing July hunk; OBSERVED by the manager). Interactions: A6/A9 ↔ F2; A8 ↔ O1; A3 ↔ O4; A4/A5 ↔ F4 only via MFFU's terms (INFERRED, the filer's, not his word).

**S13.** The standing sentence is carried once, in the header. No backtest or P&L figure is stated.

**NEEDS AMEAR.** Each item sets two texts side by side. No reading is picked.
- (i) **A3 break-even vs net basis.** A3 (:25): "B = trade exited at its entry price" defines break-even by price. A2 (:21-22, joined): "daily net P&L after commission and slippage", and values spec §6 (:92): "net P&L (after commission and slippage)". A3's words do not say whether W and L are classified by price or by net P&L after commission and slippage. A trade exited at its entry price has a net P&L below zero once commission is charged (INFERRED, the filer's, not his word). His.
- (ii) **A4 limit type and stage.** A4 (:31, :33): "80% of MFFU's trailing drawdown limit" and "Evaluated against every tier row". WF spec :141: "Studio limits are Static, not trailing. Item 3 says "trailing drawdown limit". → NEEDS AMEAR 12."; WF spec NEEDS AMEAR 12 (:207): which stage (Evaluation or Sim-Funded) and which type, and "Do Studio's **Static** limits count?"; values spec :136: "Which tier, plan stage or limit type counts stays OPEN (Q9)". Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his.
- (iii) **A8 annualisation method.** A8 (:43): "annualised OOS net profit / annualised IS net profit" names no annualisation method: neither the length unit nor whether the annualisation is linear or compounded. Side by side: values spec :83: "Day-count convention … SETTLED: a "day" is a Monday–Friday date in the data file … Changeable by him." (a deriver's settled convention, not his word); A2 (:22–23): "sqrt(252)" and "Fixed base, no compounding; tier pick not needed for this gate.", which by their words are gate 2's. His.
- (iv) **A2 and the notes-4 Sharpe item.** A4 (:33–34): "Closes the notes-4 DD equity-base item." A2 (:20–23) gives the gate-2 formula and carries no such words. Notes-4 scope, DECISIONS.md:978: "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"; values spec :93: "The gate's Sharpe definition and its equity base stay OPEN under ruling 9". Precedent, DECISIONS.md:1643: "Whether the 4% DD equity-base item stays open — his." Whether the notes-4 Sharpe-definition item (item 4) is closed by A2 is his.

Nothing else.

## 2026-11-08 — D-2026-11-08-C: Amear's answers C1–C10 to the 2026-11-08 park card (Claude.ai channel, 2026-11-08). Filed WHO: amear.

**Date:** 2026-11-08
**Status:** RECORDED — Amear's answers, WHO: amear. S5 ledger authorisation: DECISION_LOG `2026-11-08T19:12:30Z` (**WHO: amear**; DECISION_LOG.md:743, working tree). The words are REPORTED BY the Claude.ai channel and were pasted by Amear; the paste in `docs/reports/2026-11-08-amear-answers-park-card.md` is OBSERVED as received (answers file :3, written by praxis-master). Filing form: his WHO line in the block, under his heading at :12, "WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-C." (answers file :13). His approval line: "Sending this message is my approval of C1-C10 as written." (:14). C10 was first typed alone, DECISION_LOG `2026-11-08T19:04:00Z` (**WHO: amear**; :742). The park this card follows: DECISION_LOG `2026-11-08T17:25:00Z` (WHO: praxis-master; :741). Dispatch of U8: DISPATCH_LOG `2026-11-08T19:13:00Z` (WHO: praxis-master; DISPATCH_LOG.md:2037). Drafted by praxis-manager, unit `2026-11-08-park-card-filing` (U8), which did not return (DECISION_LOG `2026-11-08T22:27:00Z`, :745). Checked line by line and finished by praxis-manager, unit `2026-11-09-c-d-filing`; corrections are in place and listed in that unit's report `docs/reports/2026-11-09-c-d-filing-manager.md`. That unit did not return (DISPATCH_LOG `2026-11-09T05:04:00Z`, DISPATCH_LOG.md:2124, working tree); its report has no graded Result and is kept as written. Unit `2026-11-09-c-d-filing-resume` re-ran its checks and replaced the HANDOFF.md line pointers in this entry with park-card item pointers (report `docs/reports/2026-11-09-c-d-filing-resume-manager.md`).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** Never mixed. (a) *Amear's words* = the fenced block below and nothing else, copied by script from answers file lines 12–43. (b) The answers file's filing notes 1–5 (:50–54; section heading :48) are each labelled "Master's reading (filing note <n>, :<line>), changeable by Amear" below; a decision taken under D-2026-11-08-D D1 is labelled "decided by master under D-2026-11-08-D D1", changeable by Amear (one, under Open readings below); the label "Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear" appears only inside the C4 bullet's quote of D-2026-11-08-A's Correction 1. (c) The filer's readings are labelled "INFERRED, the filer's, not his word", or "Manager's reading, not a ruling" / "Manager's note, not a ruling" (both in S4 timing). Line pointers are the filer's. Unit `2026-11-09-c-d-filing` had U8's draft pointers checked by an adversary worker (W1; an excerpt of its output is pasted in that unit's report; its second adversary's result was lost when the unit did not return). Unit `2026-11-09-c-d-filing-resume` had the finished entry re-checked by a fresh adversary (output pasted in `docs/reports/2026-11-09-c-d-filing-resume-manager.md`, section "Continuation — manager dispatch 2"). Answer line ranges in the answers file: C1 :16–18, C2 :19–22, C3 :23–27, C4 :28, C5 :29–33, C6 :34–35, C7 :36–37, C8 :38, C9 :39–40, C10 :41–43. Where his words name what they answer ("U7 (Praxis_build-diq)", "Praxis_build-8sw", "Step 0, items 2-6", "for D-2026-11-08-A", "D-2026-11-08-B (i)", "Praxis_build-gjj", "Step 0, item 1"), the pointer follows his words; every mapping to a numbered "For Amear" item of the HANDOFF.md 2026-11-08 park card (HANDOFF.md, the card headed "Resume card — 2026-11-08 — `main` = `origin/main` = `6c4c109`; U7 (walk-forward spec amendment) PARKED at audit FAIL 2 (`Praxis_build-diq`), park commit blocked by `Praxis_build-8sw`; session ended by the park rule", its list headed "**For Amear (none asked — the park ends the session):**"; called "the park card" below, and "park card, item <n>" means item <n> of that list. Pointers into HANDOFF.md are by heading and item number, not line number, because HANDOFF.md is uncommitted and a new card is put at its top each session; the working-tree line numbers cited earlier (U8: 10–16; unit `2026-11-09-c-d-filing`: 63–69) are not to be used) is INFERRED, the filer's, not his word. Side by side, not picked: answers file :3 says the paste answers the card's "For Amear" list "(items 1–6)"; the park card's "For Amear" list has seven items, and the filer maps C8 to park card, item 7.

**The answers, verbatim (WHO: amear).** Answers file lines 12–43, inserted by script, not retyped.

```text
PRAXIS — AMEAR'S ANSWERS TO THE 2026-11-08 PARK CARD (Claude.ai channel)
WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-C.
Sending this message is my approval of C1-C10 as written.

C1  U7 (Praxis_build-diq) resumes in this new session. One correction:
    replace the stale pasted diff with the diff of the blob being
    committed. One audit. No park branch is landed for diq.
C2  Park rule amendment (made between sessions, per the absolutes
    rule): a park commit to parked/ branches is exempt from the
    audit-token gate, because it never touches main. Closes
    Praxis_build-8sw.
C3  Step 0, items 2-6: (2) anonymous HTTPS clone, step 3.1;
    (3) only the two AddOn files of step 3.2; (4) unauthenticated
    request folders acceptable for sim tests only, closed before real
    money (go-live list); (5) Sim101; (6) Amear presses Compile in the
    NinjaScript Editor by hand.
C4  One entry satisfies "File each" for D-2026-11-08-A.
C5  D-2026-11-08-B (i) win/loss judged by price, consistent with
    B = exit at entry price; (ii) Studio Static rows use the stricter
    limit type and stage, both shown; (iii) A8 annualisation = mean net
    P&L per session x 252, for IS and OOS alike; (iv) A2 closes the
    notes-4 Sharpe item.
C6  "Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of
    the OPEN section.
C7  Praxis_build-gjj: disable memory in the praxis-manager agent
    definition. Code makes the edit; auditor checks it.
C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
C9  Step 0, item 1: snapshot taken, named pre-cli-nt-bridge-2026-11-06.
    The Claude session on the VM is closed.
C10 Code writes the filed step-0 answers into vm/2026-11-06-vm-handoff.md
    §2 so the VM session reads them from the file. Amear does not repeat
    them to the VM session.
```

**Copy check.** `sed -n '12,43p' docs/reports/2026-11-08-amear-answers-park-card.md | openssl dgst -sha256` = `7fd6c65e2e694b3dd88b3e99a880288f204c111be70a114cfb1244fa0ffc60fa` (OBSERVED; equals the value in DECISION_LOG `19:12:30Z`, :743); the fenced body's hash after insertion (DECISIONS.md block lines, `openssl dgst -sha256`) is pasted in `docs/reports/2026-11-09-c-d-filing-manager.md`; U8's report holds no such paste (its "## Result" section, :29–30, reads "(in progress)").

**Per-answer pointers.** His words are in the block above; they are not restated here. Each bullet opens with that answer's line range in the answers file. No answer is read past its words. Unit names are as in the order of DECISION_LOG `19:12:30Z` (:743), quoted under S4 timing.

- **C1** (answers file :16–18). *Answers:* card item 1, second half (park card, item 1, "whether/how U7 resumes"), and the park row's open question (DECISION_LOG `17:25:00Z`, :741, "whether and how U7 resumes") — INFERRED, the filer's, not his word; the bead is his ("U7 (Praxis_build-diq)", :16). *Authorises:* U7 (`Praxis_build-diq`, P1 OPEN, `bd show`, OBSERVED) resumes with one correction and one audit (his words). *Sets aside, for diq only:* park step 1 (`specs/SPEC_RUBRIC.md`:252, "Commit the work to a branch `parked/<bead-id>`."), by his words "No park branch is landed for diq" (:18). The park row records step 1 as "NOT DONE, CANNOT BE DONE by the master" (:741). Master's reading (filing note 2, :51), changeable by Amear: "replace" is carried out "by APPENDING the diff of the blob being committed as the diff of record, and marking the earlier paste SUPERSEDED"; "The stale paste is not deleted." *Left for a later unit:* the U7 resumption ("U7 resumes under C1", :743). Nothing of U7 is edited here.
- **C2** (:19–22). *Answers:* card item 1, first half (park card, item 1, "How the park branch is landed under 8sw") — INFERRED, the filer's, not his word; the bead is his ("Closes Praxis_build-8sw", :21–22, joined). `Praxis_build-8sw`: "PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path", P1 OPEN (`bd show`, OBSERVED). *Amends:* the absolute park rule (`specs/SPEC_RUBRIC.md`:246–260): a park commit to `parked/` branches is exempt from the audit-token gate (his words). His words place the amendment under the absolutes rule ("made between sessions, per the absolutes rule", :19–20, joined); that rule is rubric :285–289 in the working tree, :275–279 at HEAD ("A rule declared absolute is **never amended inside the session that hits it.**", working tree :287, HEAD :277). Master's reading (filing note 1, :50), changeable by Amear: the amendment was made "in the Claude.ai channel, which is not the session the rule blocked". Master's reading (filing note 4, :53), changeable by Amear: the exemption is "a rubric text change AND a change to the commit-gate hook", and `Praxis_build-8sw` "closes when both are in and trip-tested". *Conditional (bd memory `amear-conditional-commitment`; INFERRED, the filer's, not his word; a pointer, not a ruling):* "because it never touches main" (:21) rests on a mechanism not observed in this unit — that a commit admitted under the exemption lands only on a `parked/` branch and cannot reach `main`. The gate-hook unit is where it is observed (S3 trip test, S9 positive control). *Left for a later unit:* the rubric unit (C2 text; every rubric edit follows A11, rubric :3–6) and the gate-hook unit (code; trip-tested under S3 and S9 before commit). 8sw is not closed here.
- **C3** (:23–27). *Answers:* card item 2 (park card, item 2, "your six answers") and VM handoff §2 items 2–6 — the item numbers are his ("Step 0, items 2-6", :23). Line correspondence, INFERRED, the filer's, not his word: C3 (2) ↔ `vm/2026-11-06-vm-handoff.md`:51 (bridge source; step 3.1 is :95); (3) ↔ :52 (the two AddOn files; step 3.2 is :107); (4) ↔ :53 (unauthenticated request folders); (5) ↔ :54 (sim account); (6) ↔ :55 (the in-NT8 compile). *Authorises:* under C10, these are written into §2 (§2 is :43–56). C3 (4)'s "closed before real money (go-live list)" (:25–26, joined) bears on the go-live list — see filing note 5 below. *Left for a later unit:* the VM-handoff unit. `vm/` is not edited here.
- **C4** (:28). *Answers:* D-2026-11-08-A's NEEDS AMEAR, Correction 1 (DECISIONS.md:1708): "(i) Whether one entry satisfies "File each as a DECISIONS.md entry" (DECISIONS.md:1546)."; card item 3 (park card, item 3). His words in A's block (DECISIONS.md:1546): "WHO: amear. File each as a DECISIONS.md entry citing this session." *Effect:* that NEEDS AMEAR is answered by his words (:28). Contrast: Correction 1, "Cure for finding 2" (DECISIONS.md:1678), where one entry was a "Master's decision under R-1104-2 (DECISIONS.md:748), changeable by Amear"; C4 is now his word on the same filing form. *Left for a later unit:* nothing. D-2026-11-08-A and its Correction 1 are not edited.
- **C5** (:29–33). *Answers:* D-2026-11-08-B NEEDS AMEAR (i)–(iv) (DECISIONS.md:1801–1804), one by one; card item 4 (park card, item 4). C5 (i) (:29–30) ↔ B (i) "A3 break-even vs net basis" (:1801). C5 (ii) (:30–31) ↔ B (ii) "A4 limit type and stage" (:1802) — see Open readings (i) below. C5 (iii) (:31–32) ↔ B (iii) "A8 annualisation method" (:1803). C5 (iv) (:32–33) ↔ B (iv) "A2 and the notes-4 Sharpe item" (:1804; notes-4 scope at DECISIONS.md:978). *Left for a later unit:* the values-spec unit ("values-spec unit (C5)", :743) changes the values-spec and WF-spec text that still carries these items as NEEDS AMEAR or OPEN (for example WF spec NEEDS AMEAR 12, `git show HEAD:docs/specs/2026-11-05-walk-forward-spec.md` :207, OBSERVED). U7's uncommitted edits to both files are in the working tree (DECISION_LOG :741); the order puts the U7 resumption before the values-spec unit. Neither spec is edited here.
- **C6** (:34–35). *Answers:* card item 5 (park card, item 5). *Effect:* O1's state "PASSED@a2f1067" (`specs/SPEC_RUBRIC.md`:77) is confirmed by his words ("is correct", :34). That this turns the rubric's own label at :81–82 ("Marking O1 PASSED, and the sha as the commit that lands D-2026-11-08-B, are the master's reading (filing note 3), changeable by Amear.", joined) into his word is INFERRED, the filer's, not his word. *Left for a later unit:* the rubric unit moves O1 (rubric :76–88; O2 starts :89) out of the OPEN section (:74). OBSERVED (`grep -n '^## '`): the rubric has no section for PASSED items — its sections are FROZEN :17, OPEN :74, Standing criteria :111, Process rulings :244; state values :12–13. Where O1 goes is the master's in the rubric unit, auditor-checked; it is not picked here.
- **C7** (:36–37). *Answers:* card item 6 (park card, item 6); the bead is his ("Praxis_build-gjj", :36). `Praxis_build-gjj`: "praxis-manager writes to its agent-memory dir despite explicit per-brief prohibition (3x on 2026-11-08)", P2 OPEN (`bd show`, OBSERVED). *Authorises:* the agent-definition unit; his words "Code makes the edit; auditor checks it" (:37). *Conditional (bd memory `amear-conditional-commitment`; INFERRED, the filer's, not his word; a pointer, not a ruling):* "disable memory in the praxis-manager agent definition" (:36–37, joined) rests on a mechanism not observed in this unit — that the agent definition carries a setting that turns memory off, and that turning it off stops the writes gjj records. The agent-definition unit and its auditor are where it is observed. *Left for a later unit:* the agent-definition unit. gjj is not closed here.
- **C8** (:38). *Answers:* card item 7 (park card, item 7), the 11-07 return handoff §4 item 4 — INFERRED, the filer's, not his word. *Effect:* the July R-A/R-B/R-C hunk of `specs/SPEC_RUBRIC.md` (working tree :275–284; `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md`; one hunk; `git diff -U0 HEAD -- specs/SPEC_RUBRIC.md` hunk header `@@ -274,0 +275,10 @@`; OBSERVED) lands as written (his words, :38). That this is the ruling B's filing note 2 waited for ("unless he rules on it", DECISIONS.md:1783) is INFERRED, the filer's, not his word. *Left for a later unit:* the rubric unit. Card item 7 says "a plain-language summary is owed with it" (park card, item 7); whether the rubric unit carries one is the master's. The card's "§4 items 2 and 4–12" (park card, item 7), item 4 apart, are not answered by C1–C10 (INFERRED, the filer's, not his word).
- **C9** (:39–40). *Answers:* card item 2 (park card, item 2, "the snapshot name" and "confirm the VM Claude session is closed") and VM handoff §2 item 1 (`vm/2026-11-06-vm-handoff.md`:50, "the snapshot is taken, and its name;"); the item number is his ("Step 0, item 1", :39). The name he gives equals the name the handoff proposed at :47 (`pre-cli-nt-bridge-2026-11-06`, OBSERVED). *Left for a later unit:* the VM-handoff unit writes it into §2 under C10.
- **C10** (:41–43). *Answers:* no card item; it is DECISION_LOG `19:04:00Z` (:742, WHO: amear), first typed alone. The premise was recorded as not met there: "its premise "the filed step-0 answers" is not met" (:742, master's reading). Row :743: "**C10's premise is now met** by C3 + C9." *Authorises:* the VM-handoff unit writes C3 and C9 into `vm/2026-11-06-vm-handoff.md` §2 so the VM session reads them from the file; Amear does not repeat them (his words). Lines of §2 that his words bear on, INFERRED, the filer's, not his word: :49 ("Then tell the VM session, in your own words, six things.") and :56 ("Step 3 does not start until items 1–6 are answered in your words."). How §2 is reworded is the VM-handoff unit's, auditor-checked. *Left for a later unit:* the VM-handoff unit, with "R1's template read" (:743).

**Filing notes (master's/manager's readings, not rulings).** The master's filing notes 1–5 (answers file :50–54) are below. The readings marked "INFERRED, the filer's" in the bullets above are the manager's.
- Master's reading (filing note 1, :50), changeable by Amear: "The park was hit in this same Claude Code conversation"; "C1 calls this "this new session""; "The resumption is recorded as his explicit decision (WHO: amear); the master does not argue it."
- Master's reading (filing note 2, :51), changeable by Amear: "C1's "replace the stale pasted diff" is carried out by APPENDING the diff of the blob being committed as the diff of record"; "The stale paste is not deleted. Changeable by him: if he means the bytes are to be removed, he says so."
- Master's reading (filing note 3, :52), changeable by Amear: "(a) D-2026-11-08-C is filed and OBSERVED on disk before any unit it authorises is dispatched." The order it gives matches the order of DECISION_LOG `19:12:30Z` (:743), quoted under S4 timing (INFERRED, the filer's, not his word).
- Master's reading (filing note 4, :53), changeable by Amear: "The exemption is a rubric text change AND a change to the commit-gate hook. `Praxis_build-8sw` closes when both are in and trip-tested."
- Master's reading (filing note 5, :54), changeable by Amear: "**C3 (4)** adds an item to the go-live list"; "The VM-handoff unit carries the line there by append." OBSERVED beside it: the list at `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`:38 already carries "Go-live checklist addendum 2026-11-07, his words (ruling 10):" with "remove the unauthenticated bridge request folders (or add auth) before real money". Whether C3 (4) needs a new line beside :38 is the master's; this entry picks nothing.

**What this entry does NOT do.** No rubric, spec, values-spec, WF-spec, VM-handoff, go-live-list, ledger, agent-definition, hook or bead edit. No bead closed (8sw, gjj and diq stay OPEN). No O1 section move. No park branch. No code, no run.

**S4 timing.** This entry is written before any unit it authorises is dispatched (`git show HEAD:DECISIONS.md | grep -c 'D-2026-11-08-[CD]:'` = `0`, OBSERVED by unit `2026-11-09-c-d-filing`; bd memory `master-s4-entry-before-code`). The order, copied by script from DECISION_LOG `19:12:30Z` (:743, **WHO: amear** row, master's text inside it): "U8 files D-2026-11-08-C, which is verified on disk → U7 resumes under C1 (one correction, one audit; MANIFEST blob = HEAD + U7's rows :299–304 only) → D-2026-11-08-C committed → rubric unit (C2 text, C6, C8) → values-spec unit (C5) → VM-handoff unit (C3, C9, C10, R1's template read, C3(4) go-live line) → agent-definition unit (C7) → gate-hook unit (C2) → U2 housekeeping, U4 F2 proposal, U5 R6 research." One manager at a time; no unit in that order is dispatched before this entry is OBSERVED on disk. Manager's reading, not a ruling: D-2026-11-08-D (D12, voice-2 file :71–75, whose sequence comes "after D6") later re-sets this order. That entry follows this one. Manager's note, not a ruling: ":299–304" in the quote is where U7's MANIFEST rows sit in the working tree. If this entry is committed first with MANIFEST.md as HEAD :1–298 plus this filing's rows, as the master's plan records (DECISION_LOG `2026-11-09T01:05:00Z`, :746, working tree: "Commit blob for MANIFEST = HEAD :1–298 + this unit's rows (U7 :299–304 stay out)."), this filing's rows take :299–305 and U7's rows take later row numbers when U7 lands.

**S5.** No approval is inferred. His words are cited from the answers file :12–43, filed under the ledger row `2026-11-08T19:12:30Z` (**WHO: amear**, DECISION_LOG.md:743); that row is the authorisation. His approval line is inside the block (:14).

**S6 cross-block (interactions only; nothing decided here).** F1–F4 (`specs/SPEC_RUBRIC.md`:19, :32, :47, :61; `grep -n '^### F'`, OBSERVED) are not modified; `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0	specs/SPEC_RUBRIC.md` (the July hunk; OBSERVED by the manager and re-read by the filer). F2 is still under FROZEN (:17); C1–C10 do not change F2; A6 governs its state (B's block, DECISIONS.md:1744–1745; B's A6 bullet, :1774). Interactions, INFERRED, the filer's, not his word: C2 ↔ the commit gate and S7/S9 (rubric :121, :123); C6 ↔ O1 (:76–88); C5 ↔ the values-spec gates and WF spec NEEDS AMEAR 12; C3 (4) ↔ the go-live list (walkthrough :35, :38) — F4 (:61) is not touched.

**S13.** The standing sentence is carried once, in the header. No backtest or P&L figure is stated in this entry. C5 (iii) states a formula, not a figure. The block carries no copy of the sentence (`sed -n '12,43p' <answers file> | grep -c 'Fills are'` = `0`, OBSERVED).

**Open readings (not decided here).** Each item sets texts side by side. No reading is picked. U8 drafted this as "NEEDS AMEAR". Decided by master under D-2026-11-08-D D1 (taken by praxis-manager in unit `2026-11-09-c-d-filing`, its report's Decisions taken 1), changeable by Amear: on that unit's reading neither item is a D2 item of D-2026-11-08-D (voice-2 file :22–26), so under D1 (:17–21) neither waits for Amear; for (ii), the acting unit re-checks D2 (d) first (below). The unit that acts on each one decides it, unless for (ii) it finds a D2 (d) question and stops (below), and logs it "decided by master under D-2026-11-08-D D1": the values-spec unit for (i) and the rubric unit for (ii). Amear may reverse either decision (D1, :20–21).
- (i) **C5 (ii) and rows whose Eval and Sim-Funded types differ.** B (ii) (DECISIONS.md:1802): "Which limit type and stage A4 means for the Studio Static rows, and for rows whose Eval and Sim-Funded types differ, is his." C5 (ii) (answers file :30–31, joined): "(ii) Studio Static rows use the stricter limit type and stage, both shown;". WF spec at HEAD, rows :118, :121, :125, :128 (Rapid 25K, 50K, 100K, 150K): "(Eval EOD; Sim-Funded intraday trailing)"; :139: "Rapid: Eval is EOD and Sim-Funded is intraday trailing. These are two stages, not a contradiction."; NEEDS AMEAR 12 (:207): "which **stage** (Evaluation or Sim-Funded) and which **type** (EOD or intraday trailing) counts? Do Studio's **Static** limits count?". C5 (ii)'s words name the Studio Static rows; whether they also reach the Rapid rows is for the values-spec unit to decide under D1, changeable by Amear.
- (ii) **C2 and S7.** S7 (`specs/SPEC_RUBRIC.md`:121): "Nothing is committed while any audit box is unchecked." Park step 1 (:252): "Commit the work to a branch `parked/<bead-id>`. It does not reach `main`." C2 (:20–21, joined): "a park commit to parked/ branches is exempt from the audit-token gate, because it never touches main." The park row cites S7 as its reason (DECISION_LOG :741, master's text): "S7 — nothing committed with a failed audit box." S7's words carry no branch scope; C2's words exempt the park commit from the gate and do not name S7. Whether S7 is amended with C2, or read as covering `main` only, is for the rubric unit to decide under D1, changeable by Amear; if that unit finds the question touches agent permissions (D2 (d), voice-2 file :25–26), it stops for Amear's word instead.

Nothing else.

## 2026-11-08 — D-2026-11-08-D: Amear's rulings D1–D12, voice session 2 (Claude.ai channel, 2026-11-08). Filed WHO: amear.

**Date:** 2026-11-08
**Status:** RECORDED — Amear's rulings, WHO: amear. S5 ledger authorisation: DECISION_LOG `2026-11-08T19:57:00Z` (**WHO: amear**; DECISION_LOG.md:744, working tree). The words are REPORTED BY the Claude.ai channel and were pasted by Amear. The paste in `docs/reports/2026-11-08-amear-rulings-voice-2.md` is OBSERVED as received (voice-2 file :3, written by praxis-master). Filing form, his WHO line in the block, under his heading at :12: "WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-D." (:13). His approval line: "Sending this message is my approval of D1-D12 as written." (:14). Per the voice-2 file :3 (master's text), the rulings answer §4 of `docs/reports/2026-11-08-voice-strategy-brief.md` (§4 is :42–55 there) and set standing rules. Appended by praxis-manager, unit `2026-11-09-c-d-filing`. That unit did not return (DISPATCH_LOG `2026-11-09T05:04:00Z`, DISPATCH_LOG.md:2124, working tree). Unit `2026-11-09-c-d-filing-resume` re-ran its checks (report `docs/reports/2026-11-09-c-d-filing-resume-manager.md`).
**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Evidence grades.** These are kept apart. (a) *Amear's words*: the fenced block below and nothing else, copied by script from voice-2 file lines 12–75 (fences :11 / :76). (b) The master's filing notes 1–5 (voice-2 file :82–98; heading :80) are "the master's readings, changeable by Amear" (:80). They are not rulings. (c) Readings by this unit are marked "manager's reading, not a ruling". Line pointers are into the voice-2 file unless another file is named.

**The rulings, verbatim (WHO: amear).** Voice-2 file lines 12–75, inserted by script, not retyped.

```text
PRAXIS — AMEAR'S RULINGS, VOICE SESSION 2 (2026-11-08, Claude.ai channel)
WHO: amear. Agents write every repo file (A11). File as D-2026-11-08-D.
Sending this message is my approval of D1-D12 as written.

STANDING RULE CHANGE — AUTONOMY
D1  Default-decide. When a unit or the master reaches a question that
    would otherwise go to Amear, it takes the recommended option, logs
    it as "decided by master under D-2026-11-08-D D1", and continues.
    Amear may reverse any such decision later; the reversal is filed
    like any ruling. No unit waits on Amear except for D2 items.
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
D3  The Telegram commit-approval step in the Hermes setup is removed.
    Commits land on an audit PASS. Telegram informs; it does not ask.
D4  Loop: a Hermes timer starts a fresh Code session every four hours.
    Each run reads HANDOFF.md, executes the next unit(s), and ends with
    one Telegram message in plain English: what was done, what was
    decided under D1, what is blocked under D2. No code names (F1, O1,
    bead IDs) without a plain-language gloss. Rough weekly review with
    Amear in the Claude.ai channel; nothing waits on it.
D5  A message to Amear that asks a question with a recommendation
    attached, on a non-D2 item, is a defect under D1. Log it, bead it,
    take the recommendation.

WORK ORDER
D6  FIRST: drawdown viability check, Mac-only, read-only, no VM, no
    purchase. On the three committed 2026-11-01 trade lists, compute
    per-walk-forward-window worst drawdown at 1 MNQ (MFFU MNQ
    commission per cost model v1.2.0), with and without a simulated
    daily-loss cap (breaker #1 at its spec value). Compare to the A4
    ceiling per tier row (80% of the lower of 4% of account and the
    trailing limit). If scripts/wf can regenerate the trade list from
    the 09:30 ET session start (R1), run that too and label it
    UNVERIFIED against NT8. Report: pass/fail per tier at 1 MNQ and
    1 NQ.
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.
D8  Brief §4 decisions: (3) start the VM session as soon as the VM
    handoff carries the step-0 answers (C3, C9, C10). (4) draft the F1
    live-signal topology doc alongside the F2 breaker PROPOSAL. (5) land
    the two staged MFFU evidence reports (2026-08-07, 2026-10-28) and
    grade them against F4's criterion. (6) the five P0 guard beads are
    accepted as known risk while only docs/specs move; fixed before any
    Block 3 code that can place orders. (7) the VM stays a hands-only
    executor; Mac is the only master. (8) "final step of this build" =
    Block 4 paper pass on MFFU sim (the standing proof-of-concept
    ruling). Block 5 live is a separate sign-off under D2(b).
D9  The 12 old staged paths are landed properly (audited) rather than
    unstaged. Root file "F" is traced, then removed and logged.
D10 Messages to Amear are plain English. Account figures are shown in
    dollars at the contract size, not in points or percent alone.
D11 Once per run, the master checks for any waiting question older
    than one run that is not a D2 item, and closes it under D1.
D12 Sequence after D6: U7 resume (C1), rubric unit (C2, C6, C8, and
    D1-D5 as a new "Autonomy" section), values spec (C5), VM handoff
    (C3, C9, C10), manager memory off (C7), park-commit gate exemption
    (C2, trip-tested), housekeeping (D9), F1 topology + F2 PROPOSAL,
    F4 grading, R6 research on its own worktree.
```

**Copy check.** `sed -n '12,75p' docs/reports/2026-11-08-amear-rulings-voice-2.md | openssl dgst -sha256` = `fd2654699e105849cbfa2f0954a89c97aabe896195af1ac02b11866519115ab1` (OBSERVED; equals the value in DECISION_LOG `19:57:00Z`, :744). The hash of the fenced body as inserted here is pasted in `docs/reports/2026-11-09-c-d-filing-manager.md`.

**Per-ruling pointers.** Each bullet gives the ruling's line range in the voice-2 file and quotes his words. A paraphrase is marked *(paraphrase)* and adds nothing that is not in the cited lines. A quote that runs across a line break in the block is joined with one space. The block above is the record; these bullets do not replace it.

*Section "STANDING RULE CHANGE — AUTONOMY" (:16).*
- **D1** (:17–21). "Default-decide." A question "that would otherwise go to Amear" is met this way: the unit or master "takes the recommended option, logs it as "decided by master under D-2026-11-08-D D1", and continues." "Amear may reverse any such decision later; the reversal is filed like any ruling. No unit waits on Amear except for D2 items."
- **D2** (:22–26). "Only four things stop and wait for Amear's word": "(a) spending money"; "(b) switching live trading on, or any order path to a funded account"; "(c) changing circuit-breaker values while real money is at stake"; "(d) installing keys, credentials or agent permissions." "Everything else is D1."
- **D3** (:27–28). "The Telegram commit-approval step in the Hermes setup is removed. Commits land on an audit PASS. Telegram informs; it does not ask."
- **D4** (:29–34). *(paraphrase)* "Loop": every four hours a Hermes timer starts a fresh Code session. Each run reads HANDOFF.md, executes "the next unit(s)", and ends with "one Telegram message in plain English" saying what was done, what was decided under D1, and what is blocked under D2. "No code names (F1, O1, bead IDs) without a plain-language gloss." A rough weekly review with Amear happens in the Claude.ai channel, and "nothing waits on it".
- **D5** (:35–37). "A message to Amear that asks a question with a recommendation attached, on a non-D2 item, is a defect under D1. Log it, bead it, take the recommendation."

*Section "WORK ORDER" (:39).*
- **D6** (:40–49). *(paraphrase)* "FIRST": a drawdown viability check, "Mac-only, read-only, no VM, no purchase". It runs on "the three committed 2026-11-01 trade lists". It computes the worst drawdown in each walk-forward window at 1 MNQ ("MFFU MNQ commission per cost model v1.2.0"), "with and without a simulated daily-loss cap (breaker #1 at its spec value)". It compares that to "the A4 ceiling per tier row (80% of the lower of 4% of account and the trailing limit)". If scripts/wf can regenerate the trade list "from the 09:30 ET session start (R1)", that is run too and labelled "UNVERIFIED against NT8". Report: "pass/fail per tier at 1 MNQ and 1 NQ."
- **D7** (:50–54). *(paraphrase)* If D6 fails at every tier at 1 MNQ, breaker values are not designed to fit the drawdown ceiling ("that is curve-fitting"). It is reported, and "R6's research (higher-win-rate, steadier-equity strategies)" is pulled forward to P0. "The Noise-Area baseline continues through the VM tests for the record, but a GO on MFFU is not expected from it."
- **D8** (:55–64). "Brief §4 decisions:" — "(3) start the VM session as soon as the VM handoff carries the step-0 answers (C3, C9, C10)." "(4) draft the F1 live-signal topology doc alongside the F2 breaker PROPOSAL." "(5) land the two staged MFFU evidence reports (2026-08-07, 2026-10-28) and grade them against F4's criterion." "(6) the five P0 guard beads are accepted as known risk while only docs/specs move; fixed before any Block 3 code that can place orders." "(7) the VM stays a hands-only executor; Mac is the only master." "(8) "final step of this build" = Block 4 paper pass on MFFU sim (the standing proof-of-concept ruling). Block 5 live is a separate sign-off under D2(b)."
- **D9** (:65–66). "The 12 old staged paths are landed properly (audited) rather than unstaged. Root file "F" is traced, then removed and logged."
- **D10** (:67–68). "Messages to Amear are plain English. Account figures are shown in dollars at the contract size, not in points or percent alone."
- **D11** (:69–70). "Once per run, the master checks for any waiting question older than one run that is not a D2 item, and closes it under D1."
- **D12** (:71–75). "Sequence after D6: U7 resume (C1), rubric unit (C2, C6, C8, and D1-D5 as a new "Autonomy" section), values spec (C5), VM handoff (C3, C9, C10), manager memory off (C7), park-commit gate exemption (C2, trip-tested), housekeeping (D9), F1 topology + F2 PROPOSAL, F4 grading, R6 research on its own worktree."

**Filing notes (master's/manager's readings, not rulings).**
- *Manager's reading, not a ruling — S8 scope.* D1–D5 change the scope of rubric S8 (`specs/SPEC_RUBRIC.md`:122, "No question that belongs to Amear is answered on his behalf."). D1 (:21) and D2 (:22, :26) narrow what belongs to Amear to the four D2 items. The rubric text itself is not amended by this entry. D12 (:71–72) gives that to a later unit: "rubric unit (C2, C6, C8, and D1-D5 as a new "Autonomy" section)". The master's filing note 1 (:82) reads it the same way.
- *Manager's reading, not a ruling — §4 numbering.* D8's "(3)"–"(8)" match the items 3–8 of the strategy brief §4 (`docs/reports/2026-11-08-voice-strategy-brief.md`:50–55). Reading them as answers to those items, and reading D6/D7 as the answers to §4 items 1–2 (:44–49 there), is the manager's inference.
- Master's reading (filing note 1, :82), changeable by Amear: D1 "narrows what belongs to Amear"; "Until it lands, auditors are told that D-2026-11-08-D governs S8's scope."
- Master's reading (filing note 2, :83), changeable by Amear: setting up the Hermes timer and Telegram "may install keys, a bot token, or agent permissions", and "Each such step is a D2(d) item and stops for Amear's word when it is reached."
- Master's decision, not Amear's (filing note 3, :84): it is labelled "Decided by master under D-2026-11-08-D D1" and "Changeable by Amear". The decision is that each timer run checks for a live session on the tree and exits without work if it finds one (CLAUDE.md single-session rule).
- Master's reading (filing note 4, :85–92), changeable by Amear: the order in force is (a) U8, (b) U9 files D, (c) "One audit of both entries, then a commit", (d) the D6 drawdown check, (e) the D12 sequence; "D7 is applied to D6's result as written." *Manager's note:* U8 did not return (DECISION_LOG `2026-11-08T22:27:00Z`, :745). Unit `2026-11-09-c-d-filing` filed both C and D and did not return (DISPATCH_LOG `2026-11-09T05:04:00Z`, :2124, working tree); unit `2026-11-09-c-d-filing-resume` re-ran its checks.
- Master's reading (filing note 5, :93–98), changeable by Amear: D6's inputs are named in the D6 brief "read when the unit runs, not assumed now". This entry reads none of them.

**What this entry does NOT do.** It makes no rubric edit; the S8 scope change waits for the D12 rubric unit. It makes no spec, values-spec, WF-spec, VM-handoff, ledger, agent-definition, hook, Hermes or Telegram edit. It does not move the index: D9's landing of the 12 staged paths is the housekeeping unit's. No bead is opened or closed. No D6 run, no code, no purchase.

**S4 timing.** This entry is written before any unit that acts on D is dispatched. OBSERVED by unit `2026-11-09-c-d-filing` (its report, V5): DISPATCH_LOG.md after the U8 dispatch row (:2037) held hook spawn/close rows, the U8 no-return row and that unit's own spawns, and no D6 or D12 unit dispatch. Re-observed by unit `2026-11-09-c-d-filing-resume`: the rows after :2037 now also hold the master's rows for the c-d-filing no-return and the resume dispatches (working tree :2124–2127), and still no D6 or D12 unit dispatch. `git show HEAD:DECISIONS.md | grep -c 'D-2026-11-08-[CD]:'` = `0` (OBSERVED; V2 of `docs/reports/2026-11-09-c-d-filing-manager.md`). The re-observation is pasted in `docs/reports/2026-11-09-c-d-filing-resume-manager.md`.

**S5.** No approval is inferred. His words are cited from the voice-2 file :12–75, filed under the ledger row `2026-11-08T19:57:00Z` (**WHO: amear**, DECISION_LOG.md:744). That row is the authorisation. His approval line is inside the block (:14).

**S6 cross-block (interactions only; nothing decided here).** Manager's readings, not rulings. D1–D5 ↔ S8 (rubric :122) and the D12 rubric unit. D3 ↔ the commit gate and S7 (commits "land on an audit PASS"). D2(b) and D8 (8) ↔ Block 5 sign-off. D2(c) ↔ the circuit breakers (F1/F2; Block 3). D6/D7 ↔ the A4 ceiling (D-2026-11-08-B) and breaker #1. D8 (5) ↔ F4. D8 (6) ↔ the five P0 guard beads. D9 ↔ the 12 staged paths. F1–F4 are not modified by this entry.

**S13.** The standing sentence is carried once, in the header. No backtest or P&L figure is stated in this entry. D6 asks for drawdown figures and states none. "80%" and "4%" are the terms of A4's ceiling, not results. The block carries no copy of the sentence (`grep -c 'Fills are'` on the block = `0`, pasted in `docs/reports/2026-11-09-c-d-filing-manager.md`, V4).

Nothing else.

## 2026-11-10 — Pointer note for D-2026-11-08-C and D-2026-11-08-D (bead Praxis_build-75n)

Filer's note, not a ruling. It edits nothing above; the two entries stand as filed. Both were filed in `ec73ba8` and cite `specs/SPEC_RUBRIC.md` as it stood at `6c4c109` (345 lines), plus, in D-2026-11-08-C only, the then-uncommitted ten-line July R-A/R-B/R-C hunk at working-tree :275–284. The rubric units `cec36b8` and `23556aa` moved those lines. Old cite → the same text in the rubric at `18d94a5` (447 lines; text matched line for line against `git show 6c4c109:specs/SPEC_RUBRIC.md`, evidence in `docs/reports/2026-11-10-housekeeping-2a-manager.md`):

- D-2026-11-08-C, DECISIONS.md:1857 — park step 1 `:252` → `:258`.
- :1858 — absolute park rule `:246–260` → `:252–266`; absolutes ruling "working tree :285–289, :275–279 at HEAD" → `:345–349`; "working tree :287, HEAD :277" → `:347`; A11 header "rubric :3–6" → `:3–6` (unchanged).
- :1862 — O1 state `:77` → `:79`; O1 label `:81–82` → `:83–84`; O1 `:76–88` → `:78–90`; "O2 starts :89" → `:95`; OPEN section `:74` → `:93` (`:74` is now "## PASSED — closed criteria"); Standing criteria `:111` → `:117`; Process rulings `:244` → `:250`; FROZEN `:17` and state values `:12–13` unchanged.
- :1864 — July hunk "working tree :275–284" → `:335–344`, by position: the ten lines directly above the absolutes heading, which was working-tree :285 and is now `:345`. The hunk header `@@ -274,0 +275,10 @@` there is a recorded observation, not a pointer.
- :1881 — F1–F4 `:19, :32, :47, :61` and FROZEN `:17` unchanged; S7/S9 "rubric :121, :123" → `:127`, `:129`; O1 `:76–88` → `:78–90`.
- :1887 — S7 `:121` → `:127`; park step 1 `:252` → `:258`.
- D-2026-11-08-D, DECISIONS.md:1989 — S8 `:122` → `:128`.
- :2003 — S8 "rubric :122" → `:128`.

The same unit inserts eleven lines into the rubric (a ten-line filer's paragraph on the C2 live trip plus one blank line) after the blank line at `:332`. When that lands, every target above at `:333` or below moves down by 11 (`:335–344` → `:346–355`, `:345–349` → `:356–360`, `:347` → `:358`); the rest do not move.

MANIFEST.md row 308 (HEAD `18d94a5`) says the rubric unit left `specs/SPEC_RUBRIC.md` at "now 413" lines. That does not match the committed file: `git show cec36b8:specs/SPEC_RUBRIC.md | wc -l` prints 416. (413 was the count before that unit's Correction 1 added three lines, per `docs/reports/2026-11-09-rubric-unit-manager.md`; the row was not updated.) The row is not edited here.

## 2026-11-10 — D-2026-11-10-A: praxispush low-privilege user DEFERRED, accepted risk recorded (bead Praxis_build-zd4; rubric O2)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** DECISION_LOG.md:795 (row 2026-11-10T09:43:00Z, praxis-master, item (2) G30); D11 sweep row G30 (`docs/reports/2026-11-09-d11-sweep-manager.md`:81); D-2026-11-08-D D1 and D2 (DECISIONS.md:1973–1974).

**What was specified.** D-2026-07-09-C (DECISIONS.md:114–129): the signal drop directory is owned by "a **dedicated low-privilege macOS user `praxispush`**" at `/Users/praxispush/praxis-signals`, the one path used by the B1-a forced-command/rrsync chroot, the B1-a sshd scoping and the B1-c Parallels VM share (:121). Its first rationale is "Structural least privilege" (:124). Context, D-2026-07-09-D (DECISIONS.md:151): the choice "was motivated partly by remote-push-key compromise (now moot with local n8n) and partly by clean VM-share-scope (still valid)", and whether local n8n writes as `praxispush` or the trader user "is revisited at B1-c execution." D-2026-07-09-C's status is "LOCKED (trader-chosen 2026-07-09)" (DECISIONS.md:117); this entry does not change it; it records that it is not yet implemented and when it must be.

**Where B1-c and B1-a stand.** That revisit point has passed (this entry's reading of the bead states below). B1-c (bead `Praxis_build-dnt`) is CLOSED: on 2026-11-10 `bd show Praxis_build-dnt` printed "[● P1 · CLOSED]". The bead does not mention `praxispush`, close reason included: `bd show Praxis_build-dnt | grep -c -i praxispush` printed 0. B1-a (bead `Praxis_build-dgt`) is DEFERRED: on 2026-11-10 `bd show Praxis_build-dgt` printed "[● P1 · DEFERRED]" and "Deferred: 2027-01-01".

**What exists now (OBSERVED 2026-11-10).** There is no `praxispush` user: `id praxispush` printed `id: praxispush: no such user` (exit 1). The drop dir is in the primary account's home, owned by admin: `ls -ld /Users/admin/praxis-signals/` printed `drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/`. This entry did not observe how, or whether, the current VM reaches the drop dir.

**How the VM reaches it, per the records.** The records differ; this entry does not pick one. Parallels era: the rubric (`specs/SPEC_RUBRIC.md`:98–99) gives the Windows path `C:\Mac\Home\praxis-signals\` and calls it "the primary account home mounted into the VM" (:99). The VM workspace design (`docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md`:46–48) gives the same Windows path `C:\Mac\Home\praxis-signals\` and records its prefix check on 2026-07-25 in the Parallels VM; it does not use the rubric's wording. The B1-c close reason (`bd show Praxis_build-dnt`) says instead: "AC2 Parallels share scoped to /Users/admin/praxis-signals only + whole-home 'admin' home share unchecked". Fusion era: D-2026-11-06-A item 3 (DECISIONS.md:1004, REPORTED) says "Fusion shared folders unavailable"; `Praxis.build` is shared over SMB with "admin Read & Write" and is "mapped as Z:" in the VM. DECISIONS.md:1019 notes that D-072 (a migration-ledger decision, not in this repo, quoted there as naming `praxispush` and `~/praxis-signals`) and item 3 differ. The go-live checklist says to "unmap Z: and turn the share off before real money" (DECISIONS.md:1004) and to "unmap Z: and turn off the SMB share" (Ruling 10, DECISIONS.md:1275).

**Decision.** The `praxispush` user is DEFERRED, not dropped. Trigger: the user is provisioned AND the drop dir is moved under it, to the canonical path `/Users/praxispush/praxis-signals` (D-2026-07-09-C, DECISIONS.md:121). This is the first branch of bead `Praxis_build-zd4`'s acceptance: "provision praxispush + relocate the drop dir under it before the B1-a forced-command step". Both must be done before whichever comes first of (1) any Block 3 code that can place orders, using the wording D8(6) gives for the five P0 guard beads: "fixed before any Block 3 code that can place orders" (DECISIONS.md:1982); and (2) the B1-a forced-command step, as the same acceptance names it: "before the B1-a forced-command step". Amear may reverse or replace this decision under D1 (DECISIONS.md:1973): "Amear may reverse any such decision later; the reversal is filed like any ruling."

**Accepted risk, plainly.** Until the trigger, the dedicated-user boundary of D-2026-07-09-C does not exist. Anything that can write as the primary account (admin), which owns the drop dir (OBSERVED above), can drop a signal file there; so can anything with write access through a share that exposes that directory to the VM, if one exists (this entry did not observe one). Blast radius: D-2026-07-09-C's rationale (DECISIONS.md:124) is that with the dedicated user "A compromised n8n push key reaches a directory that contains nothing but signals — no documents, no repo, no credentials"; that push-key motive is "now moot with local n8n" (DECISIONS.md:151), and reading the same limit as applying to any writer of the drop dir is this entry's inference, not the source's words; without the dedicated user, a writer acting as the primary account is not held to that directory (this entry's inference from :124, not tested); the B1-0 spike "accidentally shared the entire Mac home into the VM" (DECISIONS.md:125), and the rubric names the rationale "structural blast-radius limitation" (O2, `specs/SPEC_RUBRIC.md`:97); that is the risk this deferral accepts. Breakers: the rubric says "Block 3 specifies the breakers as n8n workflow gates that terminate before the file-write node" (`specs/SPEC_RUBRIC.md`:23–24), so a file written straight into the drop dir would not pass those gates (inference from that text, not tested). The rulings cited here put any order path to a funded account behind Amear's word: D2(b) keeps "switching live trading on, or any order path to a funded account" behind Amear's word (DECISIONS.md:1974); F1 (signal-path topology vs. circuit-breaker placement) and F4 (MFFU automation compliance) are FROZEN (DECISIONS.md:765; both sit under the rubric's FROZEN heading, `specs/SPEC_RUBRIC.md`:17, :19, :61); and D8(8) makes the "final step of this build" a "Block 4 paper pass on MFFU sim", with "Block 5 live is a separate sign-off under D2(b)" (DECISIONS.md:1982). This entry did not observe the order path, any account connection or any running process. So, on the record, the exposure is limited to sim; that limit is record-level, not tested.

**What this entry does not do.** It provisions no user, changes no permissions and installs nothing; provisioning is D2(d)-adjacent ("installing keys, credentials or agent permissions", DECISIONS.md:1974; sweep row G30, :81) and stays with Amear. It does not edit the rubric: O2 (`specs/SPEC_RUBRIC.md`:95–101) stays OPEN, and this entry does not grade it. Bead `Praxis_build-zd4` stays open; the master updates it after the commit.

S13: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** DECISION_LOG.md row 2026-11-10T13:36:00Z (praxis-master, unit `2026-11-10-f1-closeout`, decided under D-2026-11-08-D D1, DECISIONS.md:1907; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear). The design is the one in `docs/specs/2026-11-10-live-signal-topology.md`, committed at `b4c3291`; its audit is recorded in DECISION_LOG row 2026-11-10T13:34:00Z. Every statement below is taken from that document and cites its lines; where this entry says more than the document, it says so.

**Where things stand today.** Nothing emits a live trading signal, and none of the nine circuit breakers exists in code or workflow (topology doc :31; row 1.6 at :22, row 1.13 at :29). Every breaker's level is SPECIFIED only (:54).

**The working design: option 1** (:37–41, :74, :78). A new NT8 signal-emitter strategy (working name `PraxisNoiseAreaEmitter`, not built, :39) runs the Noise-Area band logic on bar close, calls no order method, and posts each decision to the existing local n8n webhook `praxis-signal` (:39). The breaker gates run in n8n with Redis, default closed, before Write Signal File (:41, :45). `PraxisSignalConsumer.cs` stays the only component that submits orders (:39), and carries consumer-side checks for breakers #4, #5, #7, #8 and #9 before `SubmitBracket` (:41): new checks for #4, #5, #8 and #9 (:48; per breaker, :61–62, :65–66), and for #7 its existing `qty > MaxQty` reject, set to plan size (:64, :74). #5's check is as the Phase 3 text stands; under the F2 proposal (PROPOSED, not adopted) it is removed (:62). The path in full is the one at :41.

**Fallback: option 3, only if OPEN-T1 fails.** Option 3 (the NT8 strategy computes the signal and gates itself, in NinjaScript, before its own order calls, :76) is the fallback only if OPEN-T1 finds the VM cannot reach the n8n webhook (:78, :98). It is not adopted by this entry.

**The deviation this entry records (S4).** CLAUDE.md states the signal flow as "TradingView alert → webhook → n8n workflow → …" (quoted from CLAUDE.md itself, more fully than the topology doc's :48). For the anchor strategy the emitter is NT8, not TradingView (topology doc :48; the anchor strategy is not TradingView-exportable, row 1.5 at :21). The Phase 3 breaker placement (n8n gates before the file-write node, Redis, default closed) is kept (:45, :74). The topology document was committed (`b4c3291`, from git, not from the doc) before this entry, and the audit row 2026-11-10T13:34:00Z names the missing entry as an S4 gap; nothing on the design has been built (:39, :74), so this entry is filed after the design document and before any build work.

**What it leaves with Amear, by name.**
- The B1 HMAC signing key (n8n signs gate-passed files; the consumer refuses unsigned ones): waits for Amear, D2(d) (:86).
- Provisioning the `praxispush` user that would narrow who can write the drop dir (B1 (c)): stays with Amear, D2(d), so B1 stays open as an accepted risk until then (:86).
- The B5 webhook authentication credential: waits for Amear, D2(d) (:90).
- Any order path to a funded account: waits for Amear, D2(b) (:87, :106).
- Breaker values once real money is at stake: wait for Amear, D2(c) (:101; also :58, :63).
- A paid data feed: the document raises it only under option 2 (a Mac-side program with a live NQ feed; "a data subscription may cost money, D2(a), waits for Amear", :75). Option 2 is not adopted.

**F2 stays FROZEN.** Breakers #4 and #5 depend on F2 (:61–62). The F2 proposal `docs/specs/2026-11-10-f2-session-flat-proposal.md` is PROPOSED, not adopted (:62); under A6, "F2's state changes when Amear approves the proposed values" (DECISIONS.md:1744).

**What this entry does not do.** It builds nothing. It edits no code, no n8n workflow and no spec, including the topology document and the Phase 3 breaker text. It does not adopt the F2 proposal or Rule F2-1, and does not set any breaker value. It does not resolve any OPEN item (topology doc :94–106).

**S6 cross-block (from topology doc §7, :112).** Block 1 (emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (emitter-vs-backtest parity under O4); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (paper pass on MFFU sim, D8(8)); Block 5 (live, D2(b)); Deviation A; Deviation C (bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2, F4, O2, O4; the SHM thresholds F1 blocks.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)

**Status:** Decided by master under D-2026-11-08-D D1; changeable by Amear.
**Authority:** Amear's proposal, DECISION_LOG.md:813 (row 2026-11-10T20:42:00Z, WHO: amear; at filing that row sits in the working copy, after the 810 lines of DECISION_LOG.md at HEAD `55979ee`). His words, copied by script from that line:

```text
The Mac's Hermes agent can now drive the Windows VM over SSH (host praxis-vm, key-only, firewall limited to the Mac's two addresses). I propose Hermes runs the VM handoff (vm/2026-11-06-vm-handoff.md) in place of the Claude agent inside the VM. Hermes has no screen, so anything read from NT8's windows (Trading Hours, Help -> About, Strategy Analyzer, Commissions) stays with me. Z: isn't mapped over SSH, so Hermes reads the Mac copies of Z: files and says so in each reply. If you accept, write a CODE- reply in vm/replies naming Hermes over SSH as the VM agent; Hermes won't start without it. Separately, n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network.
```

→ master's decision, DECISION_LOG.md:814 (row 2026-11-10T20:43:00Z, praxis-master, decided under D-2026-11-08-D D1, DECISIONS.md:1907). Settlement 3 ("the Claude agent running inside the Windows VM", DECISIONS.md:1086) was the master's working definition under R-1104-2, not Amear's word, so changing it is a D1 matter. The master reads his message as Amear's word on the D2(d) item ("installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447; DECISIONS.md:1912–1916) for this grant only: Hermes acts as the VM agent over SSH, under the handoff's limits. Settlement 7 (DECISIONS.md:1090, "VM agent reads and reports the NT8 version") changes for Hermes by Amear's own 20:42Z words: the Help → About read is his; the reply's T2(b) file version is extra information only. The SSH key, the firewall rule and the tunnel were set up outside the build loop and are UNVERIFIED by Code; the master installed nothing (master's filing note in DECISION_LOG.md:813, after Amear's quoted words; it reads "set up outside this session").

**What it decides.** The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`) under its skill `praxis-vm-over-ssh`. The terms are in the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md`, made part of the handoff for Hermes by its Amendment 3 (handoff §0, :23). By pointer only: T1 who the VM agent is, every §1 limit unchanged; T2 screen reads are Amear's, and in step 1 items 0 and 6 are not on their own a STOP; T3 Z: reads and writes use the Mac folder, the swap stated in each reply; T4 a same-user check before step 1 item 1; T5 the one-session rule binds Hermes's four-hour Code timer (D4, DECISIONS.md:1919), and T5(a) no Code session Hermes started may still be running when it writes STARTED; T6 one read-only GET of n8n's `/healthz` from the VM, for OPEN-T1; T7 approvals stay manual. The reply's sub-points settle the clashes between the handoff and the skill (step 1 order, the skills-directory copies and their use only under the skill's gates, intended differences against the skill's stop-on-disagreement rule, reading Amendment 3 at the start of every run, the item 1 answer, item 8's overlap with T4, Z: paths inside the two VM skills, one fresh shell per command with folder and venv paths in full, which clock gives `<ts>`, who sets the step 4.3 tab, step 3.3 not being a screen read, a later go-2a reply's precedence on step 4.3, Code sessions still running before STARTED), each marked as the master's reading under D1, changeable by Amear.

**How sure.** REPORTED BY Amear (DECISION_LOG.md:813): Hermes can drive the VM over SSH; key-only login; firewall limited to the Mac's two addresses; Z: not mapped over SSH; the reverse tunnel to n8n; n8n closed to the network. OBSERVED by the master at 20:43Z (DECISION_LOG.md:814): the skill file exists; `vm/replies/` held only README.md. Not observed: SSH reachability, the tunnel, n8n from the VM side. UNVERIFIED: whether `/healthz` exists on this n8n; the T4 command form; the folder the SSH shell starts in (T3(b)). Nothing in the terms has been tried.

**What this entry does not do.** It installs, changes or grants no key, credential or permission beyond reading Amear's grant above (D2(d)); spends nothing (D2(a)); opens no live or funded order path (D2(b)); sets no breaker value (D2(c)). Sim101 stays the only account. It does not settle OPEN-T1, and does not put the tunnel into the live design. It fills in none of Amear's screen reads. It changes no step gate and no hard limit in handoff §1. It edits nothing in the handoff but the one §0 bullet, strikes nothing, and does not edit the walkthrough, the topology document, the rubric or Hermes's skill. Placing the CODE- reply in `vm/replies/` opens Hermes's gate 1; this entry does not place it.

**S6 cross-block.**
- **Block 2 (tests 2a and 2b, in the handoff).** Step 1's self-report is test 2b part 1 (handoff §3, :91); step 2's skill load is test 2b part 2 (§4, :125); step 4.3's hand reads are Amear's (:241). Moving the screen reads to Amear does not change what counts: a hand-set tab counts as "bridge reproduces the baseline", not "driven from the terminal" (DECISIONS.md:1230, ruling 6), as before. T3 moves step 4.2's Z: hash check to the Mac copy; it still compares the Mac working tree, as the Z: check did (Z: = repo root is INFERRED, handoff §0 :8). T4 guards the Documents paths that step 2, 3.2, 3.4 and 4.2 use.
- **Block 3 (live-signal topology, D-2026-11-10-B, DECISIONS.md:2047).** OPEN-T1 (topology doc :98) asks whether an NT8 strategy in the VM can reach the Mac's n8n webhook. T6's GET is a first read-only look: it comes from a PowerShell session over SSH, not an NT8 strategy, and it is not the webhook path, so it does not settle OPEN-T1 by itself; option 3 stays the fallback (:78). If the live path used the reverse tunnel, it would depend on an SSH session staying up; with the tunnel down, n8n is unreachable from the VM, which is the B4 row's case (:89) as seen from the emitter (this entry's inference). If the tunnel works as REPORTED BY Amear, it is also a route by which something on the VM can POST to the webhook, the B5 row (:90); webhook authentication stays with Amear (D2(d)). Both are Block 3 questions, not decided here.
- **Go-live list (`docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`:26–27, :35, :38, :39).** PROPOSAL only, not added to that list, and that file is not edited: before real money, name three go-live items alongside "isolate the VM" (:27) and "unmap Z: and turn the share off" (:35): (1) the SSH key that lets the Mac reach the VM, removed or kept by Amear's word; (2) the VM firewall rule that admits the Mac, reviewed; (3) the reverse tunnel, closed or adopted by a Block 3 design. Adding them is a later unit; the wording is Amear's to accept.
- **Handoff §1 limit 10 and the skill's gates.** The skill's summary of limit 10 is narrower than the handoff's (it leaves out the two SKILL.md copies into the skills directory). The CODE- reply's T1(c) allows exactly those two copies and widens nothing else in the write set; the copies persist in Hermes's skills directory (T1(c)). The skill's gate 1 opens on the reply's existence, and its gate 2 and the handoff's limit 11 are joined by T5 and T5(a).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–V7 (Claude.ai channel voice sessions, 2026-11-10) and MFFU's replies. Filed WHO: amear, REPORTED BY the Claude.ai channel.

**Status:** WHO: amear, REPORTED BY the Claude.ai channel. The four decisions in the master's D1 block below are the master's under D-2026-11-08-D D1, changeable by Amear; they are not Amear's rulings.
**Authority:** DECISION_LOG.md:828 (row 2026-11-11T18:19:40Z, WHO: amear) and DECISION_LOG.md:829 (row 2026-11-11T18:20:00Z, praxis-master, the four D1 decisions); at filing both rows sit in the working copy, after the 826 lines of DECISION_LOG.md at HEAD `d056e91`. Amear's go reached the master through the Claude.ai channel (chat 2026-11-11 17:27Z); his words, copied by script from DECISION_LOG.md:828: "U do them". S5: the ledger append at DECISION_LOG.md:828 is the authorisation record; a channel-reported ruling is recorded, not proven given. The source of every ruling below, except the combined V3/V5 reading (DECISION_LOG.md:828), is `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md` (called the return-handoff file below; untracked at filing), written by the Claude.ai channel; its line numbers are cited as `return-handoff :N`. V4's words are from chat, not a voice session (return-handoff :58: "Amear (chat, 14:38 ET)"). Every quotation in this entry is copied by script, byte-identical to the cited line.

**V1 and V6 — both outgoing MFFU emails: SENT.** V1 (return-handoff :9–11): Amear: "Write it now and then send it." Sent 2026-11-10T19:29:01Z from Amear's Gmail as a reply in the existing MFFU support thread (Gmail message id `1a1c6ef68efc93d2`, thread `19f9edc188595b0c`, return-handoff :11); body at return-handoff :13–42, not re-pasted here. V6 (return-handoff :81–83): Amear: "Go ahead." Sent 2026-11-10T22:49:22Z, same thread (`19f9edc188595b0c`), Gmail message id `1a1c7a6d7d0d0dec` (return-handoff :83); body at return-handoff :84–103, not re-pasted here; it asks R6's OPEN-1. Grade: REPORTED BY the Claude.ai channel. The channel says it OBSERVED both sends via the Gmail connector (return-handoff :11, :83); nobody in this repo did.

**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." Amear: "Uh, yeah, you have my approval." (return-handoff :47). It is filed as closing the A6 hold, that is, Amear's approval, the first of the three parts OPEN-F2-5 names at `docs/specs/2026-11-10-f2-session-flat-proposal.md`:79 (its resolution cell, copied by script: "Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec."), on the words put to him at return-handoff :46. The amended #4/#5 text does not exist, and OPEN-F2-5 is not closed by this entry. Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here. That file is called the proposal below. Rule F2-1 as the proposal writes it, copied by script from proposal :20:

```text
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
```

The 15:00 disposition, copied by script from proposal :30 (its first two sentences; the rest of :30 by pointer): "On a full trading day, at 15:00 ET an open system position stays open." "Nothing closes it at 15:00."

Elements of the proposal's text that are not in the summary at return-handoff :46, listed without grading whether his approval reaches them: (a) the summary says "flat by 16:00 ET"; proposal :20 says "The closing order for every open system position is submitted no later than 16:00:00 ET"; (b) "(or no later than the exchange's early close on an early-close day)" (proposal :20); (c) "the position must be confirmed flat before MFFU's 4:10 PM ET auto-close" (proposal :20); (d) the summary's no-entry period is 16:00–18:00 ET; proposal :20 says "The system opens no new position from that flat time until 18:00 ET"; (e) from proposal :30: "New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9." and "Between 15:00 and 18:00 ET Amear's own manual interaction is locked out"; (f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38). DECISION_LOG.md:828 records V2 in the summary's terms.

The 16:00–18:00 lockout: Amear asked why it exists. The channel's answer, in the channel's words at return-handoff :47 (the channel's, not Amear's): "it only stops the system firing while the account is shut".

MFFU's 4:10 PM auto-close, from the committed capture `bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt`, lines 10 and 12, copied by script: "Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST." and "At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days." Holiday days, line 20: "During holiday trading hours, auto-liquidation will not occur at the half-time market close, and the trader is responsible for closing the positions." MFFU writes "EST"; reading it as ET is an INFERENCE (proposal :25: "this file reads it as US Eastern local time (ET), an INFERENCE, not stated by MFFU"). The channel's own report of these pages (return-handoff :48) is not the source used here.

**F2 stays FROZEN.** The rubric's unblock clause, copied by script from `specs/SPEC_RUBRIC.md`:30–31:

```text
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
```

DECISION_LOG.md:828 records "its unblock also needs breaker specs #4 and #5 amended" (copied by script from DECISION_LOG.md:828). This entry does not read that "also" as meaning any part of the unblock clause is met. This entry amends neither (that is a later unit) and grades no part of the unblock clause. A6 ties F2's state change to Amear's approval ("F2's state changes when Amear approves the proposed values", DECISIONS.md:1744–1745, line break and the next line's leading indent joined as one space). The #4/#5 text was not put to him (element (f) above); whether A6 is triggered is not graded here. This entry changes no rubric state.

**V3 as clarified by V5 — overnight holding.** V3 (return-handoff :50–53): Amear: "Yes, however, if uh, I go with a, another prop firm that uh, potentially allows for overnight uh, holds, would we be able to duplicate the dur uh, the uh, the infrastructure or change that?" Then: "Having to fuck around." (return-handoff :52). V5 (return-handoff :76–79): Amear: "I don't care about evening entries. It's more about compli uh, the MFFU's compliance." (return-handoff :78). The combined ruling as Amear's 2026-11-11 brief states it (relayed, chat 17:27Z), copied by script from DECISION_LOG.md:828: "MFFU compliance governs; nothing across the 16:10-18:00 ET close; evening entries stand on MFFU's written answer" (as relayed in DECISION_LOG.md:828, which calls it "the combined reading"; the brief itself is not on disk). The channel's reading at return-handoff :79 is INFERRED, not his words; the channel says it was "put back to him and not objected to". The ambiguity the channel flagged at return-handoff :55 ("do not file V3 as closing OPEN-1 until Amear answers") is answered by V5, as the combined reading relayed in DECISION_LOG.md:828 states it (REPORTED BY the Claude.ai channel). V3 does not close OPEN-1. R6 stays open pending MFFU's written answer to OPEN-1 (R6 design §7, `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:110: "A written MFFU answer is needed before any funded use.").

**V4.** Pointer only: filed as D-2026-11-10-C (DECISIONS.md:2076).

**V7 — work order for 2026-11-11.** Amear: "commit everything that we just discussed and the plan for tomorrow is to get put together a plan to run within the VM to backtest all these strategies inside of NinjaTrader." (return-handoff :106). Amear: "I don't remember if I installed the tool to access the NinjaTrader through a bash command." (return-handoff :107: "Asked that this check be on tomorrow's (2026-11-11) list."). REPORTED BY the channel from Hermes's replies (return-handoff :108): "So cli-nt-bridge is not installed". This entry claims nothing about it beyond that.

**MFFU's three replies** (return-handoff :112–136; the channel says it OBSERVED them via the Gmail connector at 2026-11-11T17:00Z; graded here REPORTED BY the Claude.ai channel; the rep's name is `[rep]` in that file).
- 2026-11-10T19:43:42Z, reply to V1 (message `1a1c6fce04330f0d`, return-handoff :114). Items 1, 2 and 4, copied by script from return-handoff :120, :121, :123: "1. Kindly be informed that we do not offer Rithmic at MFFu"; "2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices"; "4. You can trade using your strategy at the evaluation phase". The channel's reading (INFERRED, return-handoff :130): "Funded-account permission for the pattern is not stated; item 4 names the evaluation only."
- 2026-11-10T23:08:17Z, reply to V6 (message `1a1c7b82f130416b`, return-handoff :132): an identity-verification request, not an answer; "OPEN-1 (evening entry vs overnight) is NOT answered." (return-handoff :133).
- 2026-11-11T15:20:34Z (message `1a1cb3255cf62d16`, return-handoff :135): ticket closed: "we see you've been inactive for some time, so this ticket is being closed." (return-handoff :136).

**F4 stays FROZEN / NOT MET.** (graded NOT MET by the auditor at `55979ee`; not re-graded here). The rubric's F4 criterion, copied by script from `specs/SPEC_RUBRIC.md`:49–50:

```text
**Criterion.** Written confirmation from MFFU that this specific automation
pattern is permitted on a funded account.
```

A replacement ticket exists at `docs/reports/2026-11-11-mffu-connection-investigation.md`:1422 (heading "C3.3 — Replacement ticket"); its :1424 reads "Amear sends this himself from his logged-in MFFU dashboard."

**Decided by master under D-2026-11-08-D D1, changeable by Amear.**
Source: DECISION_LOG.md:829.
1. The per-firm settings profile, the channel's proposal at return-handoff :53 ("firm rules (flat time, overnight holding, other firm limits) live in a per-firm settings profile, MFFU as the first profile, not hard-coded."), which the channel left for Amear as O2 at return-handoff :72 ("O2 — R6 per-firm profile (V3): confirm."), is adopted as the design direction for firm rules, MFFU as the first profile. Nothing is built. The profile's contents are not decided here.
2. The V7 strategy list at return-handoff :110, copied by script: "the Noise-Area baseline (test 2a: 1,190 trades / $197,327.60 on NQCONTROW SEP25) and its walk-forward; the three 2026-11-01 strategies; the R6 announcement variants (no NinjaScript exists for them; the R6 design proposed a Mac-side Python first pass, which this work order changes to NT8 — the master's call under D1, changeable by Amear)." This list is the working scope of the NT8 backtest plan. R6's first pass moves from Mac-side Python to NT8. The list and its P&L figure are the channel's (REPORTED BY the Claude.ai channel); this entry did not re-check them.
3. MFFU's "we do not offer Rithmic" (return-handoff :120) contradicts D-2026-11-10-B's broker route (DECISIONS.md:2054: "The path in full is the one at :41."; the topology path ends "→ Rithmic → account.", `docs/specs/2026-11-10-live-signal-topology.md`:41). D-2026-11-10-B is not edited. The route is recorded as contradicted and is NOT re-decided here; that is the next unit (DECISION_LOG.md:829: "next unit").
4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel recommends an "SSH reverse tunnel from the Mac for sim testing (no new exposure of n8n)" (return-handoff :71); that tunnel uses SSH keys, which is a D2(d) item ("(d) installing keys, credentials or agent permissions", `specs/SPEC_RUBRIC.md`:446–447, line break and the next line's leading indent joined as one space), so it waits for Amear.

Context for decision 4 (not part of it): D-2026-11-10-C records Amear's 20:42Z words about a reverse tunnel as REPORTED BY Amear and the tunnel as UNVERIFIED (DECISIONS.md:2085, :2089); decision 4 does not change that. Amear's 20:42Z clause, copied by script from DECISIONS.md:2082: "n8n reachability is settled: an SSH reverse tunnel lets the VM reach the Mac's n8n at http://127.0.0.1:5678, and n8n stays closed to the network". DECISION_LOG.md:829 keeps O1 open; the difference between his "is settled" and "stays open" is recorded here, not resolved.

Context from the channel's proposal (return-handoff :53), not part of the decision: "Any overnight-holding profile needs its own backtest, because current results assume flat every day."

**Open for Amear.**
- The SSH keys any VM-to-n8n reverse tunnel would use: D2(d).
- The identity-verification details MFFU asked for: "the verification details are his to give" (return-handoff :136; request at :133).
- Sending the replacement ticket (investigation C3.3, :1422) is his.
- A header-bearing export of the outgoing V1 message is his to file if the auditor wants headers (return-handoff :43).
- Confirming or changing the per-firm profile direction (O2, return-handoff :72) is his; decision 1 is changeable by him.
- Both his 20:42Z "is settled" (DECISIONS.md:2082) and decision 4's "stays open" (DECISION_LOG.md:829) are on record; which stands is his.

**What this entry does not do.** It builds nothing. It edits no spec, no rubric, no VM handoff, and not D-2026-11-10-B, the F2 proposal or the topology document. It does not unblock F2 or F4; it grades neither and does not re-grade F4. It sets no breaker value and amends no breaker text. It decides no D2 item, no broker route, no per-firm profile contents and no VM-to-n8n path. It does not file the four 2026-11-10 Hermes replies (DECISION_LOG.md:829).

**S6 cross-block.** Block 2 (the NT8 backtest plan's working scope is the V7 list, decision 2; R6's first pass in NT8; any overnight-holding profile needs its own backtest, return-handoff :53). Block 3 (broker route recorded as contradicted, decision 3; VM-to-n8n path open, decision 4; breakers #4 and #5 not amended by this entry). Rubric F2 (Rule F2-1 approved; F2 FROZEN). Rubric F4 (FROZEN / NOT MET). R6 OPEN-1 (open; V6 asked it; MFFU's 23:08:17Z reply did not answer it).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 9 lifted by Amear for one install; Python 3.12.10 and git 2.56.0 (ARM64) installed in the VM. Record only. Filed WHO: amear, REPORTED BY the Claude.ai channel.

**Status:** Record only. WHO: amear, REPORTED BY the Claude.ai channel.
**Authority:** DECISION_LOG.md:828 (row 2026-11-11T18:19:40Z, WHO: amear; its ALSO part, on the limit 9 lift) and DECISION_LOG.md:829 (row 2026-11-11T18:20:00Z, praxis-master). Source: `vm/replies/20261111T172933Z-python-git-install.md` (called the install reply below; untracked at filing); its line numbers are cited as `install reply :N`. S5: the ledger append at DECISION_LOG.md:828 is the authorisation record; a channel-reported ruling is recorded, not proven given. Every quotation is copied by script, byte-identical to the cited line.

**The limit.** VM handoff §1 limit 9, copied by script from `vm/2026-11-06-vm-handoff.md`:37: "**Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it."

**Amear's words (install reply :7–8) and the channel's note (:9).** Voice, 2026-11-11 ~16:5xZ, on whether to snapshot first: "Okay, you know what? Let's forget about the snapshot. Let's have it execute those things first." Then: "Hermes is going to give me a uh, a physical button to accept or deny, so don't worry about that." (install reply :7). Chat, 2026-11-11 17:27Z, on the two open items (file the 2026-11-10 note; install Python and git in the VM): "U do them" (install reply :8). Install reply :9: "No new snapshot was taken (Amear's choice)."

**Who did it.** Install reply :2 names the writer as "Claude (Claude.ai Praxis channel, Cowork session)", "driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript". By that line the install was driven by the Claude.ai channel, not by Hermes; D-2026-11-10-C (DECISIONS.md:2076) names Hermes as the VM agent. The install reply does not say whether the accept-or-deny button Amear mentions at :7 was used.

**What was installed, and where (install reply :18–19).** Python: `Python 3.12.10` at `C:\Program Files\Python312-arm64\python.exe` (`py -0p`: `-V:3.12-arm64 *`), installer exit `PYTHON_EXIT=0`. Git: `git version 2.56.0.windows.4` at `C:\Program Files\Git\cmd\git.exe`, installer exit `GIT_EXIT=0`. NinjaTrader still pid 9600, start time unchanged; `PROCESSOR_ARCHITECTURE=ARM64`. Install reply :28 adds "the VM is Windows on ARM64 and winget installed the ARM64 builds". Install reply :17 (the pre-install check: the account the shell ran as, winget's version, the administrator-role result and the NinjaTrader process) is not copied here.

**What was kept (install reply :24–25).** "NinjaTrader not started, stopped or touched (same pid and start time before and after). No connection change (D-071). No orders. No pip run, no clone, no bridge files. No Windows restart. Nothing else installed. Only new files under `vm/replies/`."

**Scope.** The install reply's header (install reply :1) says limit 9 was "lifted by Amear for this install". Amear's quoted words at install reply :7–8 set no scope of their own. This entry reads the lift as covering this one install only and does not widen it; limit 9 binds every later step as written.

**Timing (S4).** The install reply is stamped `UTC: 20261111T172933Z` (install reply :3), that is 2026-11-11T17:29:33Z, before DECISION_LOG.md:828 (2026-11-11T18:19:40Z) and before this entry. This entry records the install after the fact. So for this install the order S4 and S5 ask for (a DECISIONS.md entry and a ledger append before the work) did not hold: the work is stamped 17:29:33Z, the ledger append 18:19:40Z, this entry later. D-2026-11-10-C reads Amear's D2(d) word as "for this grant only: Hermes acts as the VM agent over SSH" (DECISIONS.md:2085, copied by script). This entry records that the Claude.ai channel drove the VM over SSH (install reply :2); it grants nothing.

**Open risk.** Copied by script from install reply :28: "Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) have win_arm64 wheels at versions meeting the bridge's floors is not checked." "If step 3.5 fails on a build-from-source, the fallback is an x64 Python (runs under emulation) — that is Amear's call, not taken here." So the bridge's pip step (handoff step 3.5, "3.5 Python CLI.", `vm/2026-11-06-vm-handoff.md`:188) on ARM64 wheels (`pyarrow`, `numpy`) is UNVERIFIED, and the x64-Python fallback is Amear's call.

**How sure.** Every install fact above is REPORTED BY the Claude.ai channel in the install reply. Nobody in this repo re-ran the commands or looked at the VM.

**Open for Amear.** Whether the Claude.ai channel may drive the VM over SSH again is an agent-permission item, D2(d), his. The x64-Python fallback (install reply :28) is his call.

**What this entry does not do.** No pip, no clone, no venv, no bridge files. It does not edit the VM handoff. It changes no step gate in handoff step 3.5 (`vm/2026-11-06-vm-handoff.md`:188 onward), including its STOP conditions on a failed install (:200, "Consequence") and on any unnamed download (:201, "Detection, after the fact"). It installs nothing and grants no key, credential or permission.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1, changeable by Amear. Not Amear's ruling. A spec amendment only: nothing is built.
**Authority:** DECISION_LOG.md:854 (row 2026-11-12T05:29:00Z, WHO: praxis-master, unit `2026-11-12-f2-breaker-amendment`, Unit F2B); at filing that row sits in the working copy, after the 851 lines of DECISION_LOG.md at HEAD `9905804`. Rule F2-1's approval: D-2026-11-11-A, V2 (DECISIONS.md:2108–2116). D1: `specs/SPEC_RUBRIC.md`:437–442. Every quotation in this entry is copied by script, byte-identical to the cited line or to the stated part of it. The row's item (1), copied by script from DECISION_LOG.md:854:

```text
(1) the proposal's #4/#5 replacement text is adopted as the amended breaker spec, matching Rule F2-1; this is not D2(c) — no account exists and no real money is at stake (D-2026-11-11-A: Amear has no MFFU account; consumer Sim-only guard);
```

Its item (2), copied by script from the same line:

```text
(2) the Phase 3 spec is a faithful import, so its body lines :100–101 are NOT rewritten; the amendment is an appended, labelled amendment section plus at most one pointer line, and a new DECISIONS.md entry D-2026-11-12-A written BEFORE the spec edit (S4) records the adoption and names the governing rule and the 15:00 disposition;
```

**The governing rule: Rule F2-1.** Copied by script from `docs/specs/2026-11-10-f2-session-flat-proposal.md`:20 (called the proposal below):

```text
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
```

**The 15:00 disposition.** Copied by script from proposal :30 (the whole line; its first two sentences are the ones D-2026-11-11-A quotes at DECISIONS.md:2114):

```text
**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
```

**The amended breaker text.** The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec. Copied by script from proposal :36 and :38:

```text
> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.

> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
```

They supersede the Phase 3 import's lines :100 and :101 (`docs/specs/2026-11-05-phase3-build-specification.md`), copied by script:

```text
4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
```

The Phase 3 spec is a faithful import, so :100 and :101 are not rewritten. The amendment is a labelled section appended at the end of that file ("Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)") No pointer line is added inside the body: a line there would shift the body's line numbers after :106, which other specs cite (topology doc :24, :61, :89; proposal :67). This entry is written to disk before that spec edit (S4).

**Why this is the master's decision, changeable by Amear.** Amear's approval (D-2026-11-11-A, V2) was given on the words put to him, "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." (as copied at DECISIONS.md:2108). That entry records, copied by script from DECISIONS.md:2108: "The amended #4/#5 text does not exist" and "Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here." Its element (f), copied by script from DECISIONS.md:2116: "(f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38)." So his approval reached Rule F2-1 as summarised, and whether it reaches element (f) is ungraded. This entry does not read his approval as reaching (f). The adoption of the #4/#5 text is the master's, under D1, and Amear may change it. The master's reading (not graded by anyone else): the adopted text keeps the three parts of the summary — #4 flattens by 16:00 ET and refuses new system entries until 18:00 ET; #5 no longer disables the system's own trading, so a position open at 15:00 may stay open until 16:00.

**Not D2(c).** D2, copied by script from `specs/SPEC_RUBRIC.md`:443–447:

```text
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
```

Moving #4 from 11:30 to 16:00 and removing #5's system disable change breaker values, but no real money is at stake: no account exists. Source, copied by script from `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md`:10 (committed at `9905804`; REPORTED BY the Claude.ai channel): "Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard." The order path is also walled to Sim accounts, copied by script from `ninjascript/PraxisSignalConsumer.cs`:39: "// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"". DECISION_LOG.md:854 cites D-2026-11-11-A for "Amear has no MFFU account"; that statement is not in D-2026-11-11-A; its source is the return handoff's :10, cited above. Once real money is at stake, any further change to these values waits for Amear (D2(c)).

**Level.** The nine breakers, #4 and #5 included, remain SPECIFIED ONLY: zero implemented, zero tested, zero tested under failure (Phase 3 import status note, :11). This entry changes text, not level.

**Rubric F2.** The unblock clause, copied by script from `specs/SPEC_RUBRIC.md`:30–31:

```text
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
```

This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and records the amendment of #4 and #5. It does not grade the clause and does not change F2's state. The F2 state move is a later, separate unit after this unit is audited and committed; DECISION_LOG.md:854 item (4), copied by script: "(4) the rubric F2 state move is a later, separate unit after this one is audited and committed (F1 precedent `b4c3291` → `d30ab4d`)." A6 ties F2's state change to Amear's approval (DECISIONS.md:1744–1745); whether A6 is triggered is not graded here. Citation note, not an edit: the proposal :8 cites the unblock clause as (`specs/SPEC_RUBRIC.md`:43–44); the clause is at :30–31.

**What this entry does not do.** It builds nothing: no code, no n8n workflow, no NinjaScript, no Redis or PostgreSQL. It edits no rubric line and no spec other than the Phase 3 spec's appended Amendment 1; the F2 proposal, the topology document, the walk-forward spec and values, and the Noise-Area ruleset are not edited. It sets no value for #1, #2, #3, #6, #7, #8 or #9. It decides no D2 item. It does not decide OPEN-F2-1 to OPEN-F2-4 (proposal :75–78) or how #5's operator lockout is enforced (topology doc OPEN-T8, :105). D-2026-11-10-B's statement that the F2 proposal is "PROPOSED, not adopted" (DECISIONS.md:2068) is superseded for the #4/#5 text by this entry; that entry is not edited.

**S6 cross-block.** Graded line by line in `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` (S6 section); nothing is edited by it. Conflicts and the other follow-ups are named there as F-1 to F-9 (its subsection "Follow-ups (named, not fixed)"); that subsection is the full list, and this entry does not restate it. Bearings: rubric O4 (breakers-on vs breakers-off backtest; #4 and #5 now share the 16:00-flat clock of the current backtests, #2 and #3 still differ; O4's question is not answered here); OPEN-F2-1 (backtest flat on the 15:59 or the 16:00 bar); the Phase 3 fallback script's "session time" threshold (:109; the line states no value) is read by this entry as 16:00 under the amended #4; Block 4 and Block 5 (live path, D2(b)).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-12 — D-2026-11-12-C: Block 1 milestone scope — internal path only (rubric O3; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-12T17:31Z), changeable by Amear. Not Amear's ruling. A scope record only.

**Scope line (rubric O3).** The Block 1 milestone signed off on 2026-07-15 covers the internal path only: the locally driven path that D-2026-07-09-D names, test webhook posts through "webhook → local n8n → JSON file drop into the signals dir → Parallels VM share → NT8 FileSystemWatcher → sim bracket order"; public TradingView ingress (Deviation G, D-2026-07-09-D) was "deferred to pre-live (Block 4–5)" and is untested (rubric O3).

**Sources (DECISIONS.md at a411e17).**
- D-2026-07-09-D, heading at :133 ("n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live"); the path and the deferral are in its **Decision:** paragraph at :140.
- The sign-off, heading "## 2026-07-15 — Block 1 milestone — trader sign-off" at :174, body at :175; the body records B1-a as "verified-as-DEFERRED (D-2026-07-09-D)".
- Rubric O3, `specs/SPEC_RUBRIC.md` "## OPEN — gradeable now", "### O3 — Block-1 milestone scope statement".

**Limits.** This entry records scope only. It makes no design choice, adds no test, and does not re-open or re-grade the 2026-07-15 sign-off. It does not change rubric O3's state; that move is a later master step. It does not decide where public ingress goes. Cross-reference only: `docs/specs/2026-11-10-live-signal-topology.md` (D-2026-11-10-B) :112 already says Deviation G's ingress question leaves the anchor's live path; this entry adds nothing to it.

**S6 cross-block.** Touches Block 0 (Step 0.8, commit `2582531`, whose body records "Webhook->validate->file write (/tmp/praxis-signals on n8n host)"; nothing in Block 0 is re-graded), Block 1 (the reach of the 2026-07-15 sign-off), Block 2 (`docs/specs/2026-11-05-phase3-build-specification.md` :180, "When Block 1’s milestone is hit, Block 2 starts. Not before."), Block 4 and Block 5 (where D-2026-07-09-D places the deferred ingress question; nothing is moved there) and rubric F1 / the live-signal topology `docs/specs/2026-11-10-live-signal-topology.md` (:112, cross-reference only). One conflict, recorded, not resolved: the Phase 3 spec's Block 1 milestone (:60, "fire a fake signal from TradingView") includes TradingView ingress; the milestone signed off on 2026-07-15 did not; the sign-off records "Block 2 (Backtesting) entry condition now satisfied" (:175). This entry records the gap; it does not re-grade the sign-off, re-open Block 1 or stop Block 2 (decided by master under D-2026-11-08-D D1, DECISION_LOG 2026-11-12T21:41Z, changeable by Amear). Evidence: `docs/reports/2026-11-12-o3-block1-scope-evidence-2.md` (S6 section).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-13 — D-2026-11-13-A: Backtest-vs-live breaker parity (rubric O4; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T05:45:00Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-yra`). Parts marked CONDITIONAL rest on a mechanism nobody has observed and carry a void clause.

**Decision 1: the Block 2 backtest runs both, and is graded with breakers.** Every Block 2 run yields two series from one trade list. The *without* series is the raw list as the strategy emits it (reverse-and-re-enter, 16:00 flat, no trade cap, no loser stop). The *with* series is that list after breakers #2 and #3 are applied to it after the run, Mac-side, by the rule below. Every Block 2 pass-gate value (arm (a) gates 1-5; arm (b) gates 1-6 and PBO) is computed on the with series. The without series is a record of what the breakers cost or saved; it is never graded.

**Decision 1 rule (CONDITIONAL).** Per session, trades are taken in entry order; a trade is one entry, and a reversal is the close of one trade plus the entry of the next. A reversal is processed close leg first: the closed trade's result is counted, then the entry leg meets the gate. #2: once the session's entry count reaches the approved #2 maximum, every later entry is dropped. #3: once the session's run of consecutive losing closed trades reaches the approved #3 count, every later entry is dropped. Neither value is approved for the automated book (R8, A6); spec :98 gives #2 no number and :99 gives #3 as 2. A loser is L as A3 and C5 (i) define it (by price). That a B trade is not a loser and breaks the run is the master's reading under D1, changeable; R4's "a break-even trade counts as" half a loss (DECISIONS.md:1560-1561) scores win rate, not the #3 run (named difference). A dropped entry leg's close leg still executes at the same bar and fill as in the raw list, so the trade it closes keeps its recorded exit. Removed trades leave the with series, stay in the without series, and are listed in a removed-trades table (count and net P&L per session) in the Block 2 report. Assumptions: (i) #2 and #3 gate new entries only and never block a closing order; (ii) in the backtest engine, a reversal's close leg fills at the price a stand-alone exit at that bar would; (iii) Block 3 builds live #2 and #3 to this same rule. Void if any one is observed false (for example, a built gate drops a whole reversal signal and leaves the position open, or a reversal's close fill differs from a stand-alone exit's fill at the same bar): the with series is then produced by re-simulating with the gate inside the bar loop, not by deleting trades, and an amending entry replaces this rule and Decision 2's paper-side counting.

**Decision 2: how the Block 4 gate is satisfiable (CONDITIONAL on assumptions (i) and (iii) above; same void clause).** The gate compares Block 4 paper trades against the with series only: the with series of the arm whose parameters trade in Block 4 (arm (a), which R2 says GO requires; that an adopted arm (b) set would replace it is the master's reading under D1, changeable), over its full test span, at the cost model in force. Win rate is A3's quantity, computed identically on the with series and on all Block 4 paper trades; it passes if the two differ by at most 15 percentage points. Average trade P&L is the mean net P&L per trade per contract after commission and slippage; it passes if |paper mean − with mean| ≤ 0.25 × with mean, a positive with mean being presupposed (R5: net positive after costs). Trades the breakers removed enter neither term; on paper, entries #2 or #3 block make no trade and are logged, not counted. The gate is never re-run on the without series to rescue a failure. Reading "±15%" as percentage points and "±25%" as relative to the with mean is the master's, under D1, changeable.

**Sources (quoted byte-exact; DECISIONS.md lines are the working tree).**
- Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :98 "trade count hits daily max → disable order submission"; :99 "2 consecutive losers in one session → identical to max trades"; :124 "within ±15% win rate and ±25% average trade P&L"; Amendment 1 :205 "The system opens no new position from that flat time until 18:00 ET, when the next session begins."; :224 "The system's own trading is not disabled by this breaker"; :239 "New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9."; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure".
- Deviation C: no DECISIONS.md entry is titled Deviation C (DECISIONS.md:511 quotes the rubric; :2072 names it in an S6 list). Its authority is DECISION_LOG.md:42: "positions/session = reverse & re-enter on opposite-band cross (NOT one-position/session)".
- Strategy `ninjascript/PraxisNoiseAreaBreakout.cs`: :32 "Positions/session = REVERSE & re-enter on an opposite-band cross"; :189 "if (mod >= CloseMod)" and :191 `FlattenAll("16:00 session flat");`. No trade cap and no loser-streak stop: zero hits for `MaxTrades|TradeCount|tradesToday|consecutive|loser|LossStreak` in all three `PraxisNoiseAreaBreakout*.cs` (`docs/reports/2026-11-13-o4-reduce3-worker1.md` E3). Implemented: reverse and 16:00 flat. Not implemented: #2, #3.
- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :59 "Deviation C reverse-and-re-enter counts as an entry"; :58 "must never be blocked by a closed gate".
- Block 2 gates (DECISIONS.md): :1556 "GO requires arm (a) to pass."; :1746 "R3 amends Q8: arm (a) is judged on gates 1-5 (WFE not"; :1748 "O1 is discharged by R2 + R3 + A7."; A3 :1731 "W / (W + L + 0.5 x B), B = trade exited at its entry price." and :1733 `"within +/-15% win rate" check, computed identically on backtest` (pointer :1771); C5 :1836 "win/loss judged by price".
- Breakers on (DECISIONS.md): :512 "the backtest runs **with the breakers on, once they are built**" (the agent's reading, confirmed by Amear in voice only, :512); R8 :1584 "#2 max 2 trades/day, #3 two-and-done" and :1588 "New values come back to Amear as".
- SHM-4, DECISIONS.md:189: "SHM-4: win-rate >15 ppts below backtest OR slippage >2 ticks/side worse, over a 20-trade window."
- R6 (read-only): DECISIONS.md:2350 (parked D-2026-11-12-B) "without breakers as design :116 (O4) states"; `bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`:116 "First pass runs without breakers (no approved values; D6 E4) and says so; a breakers-on run waits for F2."
- After-the-run precedent: `docs/reports/2026-11-09-d6-drawdown-check-manager.md`:55 "every later trade that session is skipped" (breaker #1 sensitivity). Bead `Praxis_build-yra` (`bd show`): "the live-vs-backtest gate is structurally unmeetable."

**S6 cross-block.** Block 2: R2, R3, A7, A8 unchanged; gate values move to the with series; the values-spec §6 selection statistic is not changed, and whether arm (b) selects on the with series is left to the values-spec unit (named gap: selecting on one series and grading on the other). Block 3 breakers: assumption (iii) is a parity requirement on the later build, not an edit; it conflicts with topology :59 as written, which drops "the entry signal" whole, so a reversal sent as one SELL or BUY would leave the position open; neither #2 nor #3 has an approved value, and R8 says both are redone. Block 4 gate: spec :124 and the 25-trade minimum unchanged; Decision 2 fixes only the series and the arithmetic. R6 parked research: its first pass is a without series by its own design and is no Block 4 reference; nothing in R6 changes. SHM: SHM-4 and SHM-5's "backtest" is read as the with series (the master's reading under D1, changeable), bands unchanged; SHM-4 is one-sided over 20 trades, the Block 4 gate is two-sided over the paper period, and neither replaces the other. #4 parity (the full-day flat's timing against the strategy's 16:00 bar-close flat, and early-close days) is not decided here. #5 (the session window) is an operator lockout with no effect on system trades; #1 and #6 to #9 are applied in neither series.

**Limits.** No code, no strategy file, no breaker value and no spec body is changed. The nine breakers stay SPECIFIED ONLY: zero implemented, zero tested; a with series is a simulation of specified text, not evidence that a breaker works. No with series exists yet, and none can be produced until #2 and #3 have approved values (R8: PROPOSED; D2 (c) once real money is at stake); this entry sets none. If an approved #2 or #3 value later changes, the with series is re-derived and every gate value on it is recomputed. It does not lift F3 or F4 and depends on neither: the fill resolution of any run is whatever F3 settles. It does not decide parity for #1, #4 or #6 to #9, and does not mark O4 passed.

**S4 timing.** Written 2026-11-13, before the work it governs: no with series, no breaker code and no Block 4 paper trade exists. Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T05:45:00Z (WHO: praxis-master).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## 2026-11-13 — D-2026-11-13-B: Breaker #4 cancel and confirm-flat placement (topology OPEN-A1; master under D-2026-11-08-D D1)

**Status:** Decided by master under D-2026-11-08-D D1 (DECISION_LOG 2026-11-13T13:29:04Z), changeable by Amear. Not Amear's ruling. A written statement only (bead `Praxis_build-fgd`, topology item OPEN-A1). The part marked CONDITIONAL rests on a mechanism nobody has observed and carries a void clause.

**Decision.** Option (a) of topology :198: amended #4's "cancel working entry orders" and "confirm flat before 4:10 PM ET (alert if not)" (spec :212) are both part of the FLATTEN command the consumer executes at the flat time; the consumer cancels its own working entries and reports flat or not flat. The master's reason: option (b) depends on OPEN-T3 (topology :100), which is unresolved. CONDITIONAL: this rests on the unobserved mechanism that the consumer can see and cancel its own working entry orders and read its own position; FLATTEN as an instruction type is unbuilt (OPEN-T2, topology :99). Void clause: if either is observed false, the placement is re-decided toward (b) after OPEN-T3. Named gap: where the "alert" goes is not decided here. Not a D2 item (no money, no live path switched on, no breaker value, no credential). OPEN-A2 is not decided here.

**Sources (quoted byte-exact).**
- Topology `docs/specs/2026-11-10-live-signal-topology.md`: :198 "(a) Both are part of the FLATTEN command the consumer executes at the flat time (the consumer cancels its own working entries and reports flat or not flat)." and "(b) The confirmation is a separate n8n-side check on account state, which needs the account-state feed of OPEN-T3."; :99 "EXIT / FLATTEN types, unbuilt"; :100 "Where account state (P&L, equity, fills, open position) comes from, and how fresh it must be."; :61 "Its "close positions" action: the emitter's own time exit posted as a FLATTEN signal, plus the FLATTEN command from n8n at the gate time."; :58 "Its "cancel all, flatten" action: n8n writes a FLATTEN command file that the consumer executes"; :106 "D8(8): the final step of this build is a Block 4 paper pass on MFFU sim; Block 5 live is a separate sign-off."
- Phase 3 spec `docs/specs/2026-11-05-phase3-build-specification.md`: :212 "cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not)"; :196 "SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure."

**S6 cross-block.** Block 3 breakers and topology: the two #4 actions at spec :212 are placed inside FLATTEN, the same command topology :61 names for #4's "close positions" action; no topology row and no spec text is edited. OPEN-T2 (topology :99) stays open; under (a) the FLATTEN type it names is where both actions would live. OPEN-T3 (topology :100) stays open; option (b) waits on it under the void clause. Block 4 paper (topology :106): no Block 4 text is changed. Named gap: breaker #1's "cancel all, flatten" action (topology :58) is specified as a FLATTEN command file the consumer executes; whether #1's flatten carries the cancel and confirm-flat steps placed here for #4 is not decided here. Nothing else is edited.

**Limits.** No code, no spec body and no breaker value is changed. The nine breakers stay SPECIFIED ONLY (spec :196): zero implemented, zero tested. This entry does not touch F3 or F4.

**S4 timing.** Written 2026-11-13, before the work it governs: FLATTEN is unbuilt (topology :99) and no breaker is implemented (spec :196). Chain: D-2026-11-08-D D1 → DECISION_LOG 2026-11-13T13:29:04Z (WHO: praxis-master).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
