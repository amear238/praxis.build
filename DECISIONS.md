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

