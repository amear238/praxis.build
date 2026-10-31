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
