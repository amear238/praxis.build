# PRAXIS — Build-Progress Report for the Project-Scoping Agent

**Date:** 2026-07-25 (build session 28)
**Author:** the build-side agent (Claude Code, working in the PRAXIS git repository)
**Audience:** the Claude.ai agent that scoped and planned this project from the start
**Bead:** Praxis_build-wx7

---

## 0. How to read this document

You planned this project. I did not, and this report does not touch the plan. I am an authority on **what has been built and its current state** — nothing more. Where the build diverged from your plan, I flag it explicitly in a dedicated section (§7) and note that Amear (the trader) approved each divergence, with a citation you can trace. I do not argue for or against any of those choices; ownership of the plan and the strategy stays with you.

You have **no access to this repository, to the issue tracker, or to any file referenced here.** So this document is self-contained: every internal term, file, and short identifier is expanded on first use. Where I cite a commit hash or a decision record, that is verifiable grounding you could confirm if you were given repo access — it is not asking you to take anything on faith.

The tone throughout is factual. "Built" means the artifact exists and (where stated) passed an independent check. "Not proven" means exactly that.

---

## 1. What PRAXIS is (self-contained)

PRAXIS is an automated futures-trading system for a single instrument: **NQ**, the E-mini Nasdaq-100 futures contract. Its purpose is to take a trading signal, validate it, and place a bracketed order (an entry plus an attached stop-loss and profit-target) into a broker-connected trading platform, entirely by deterministic code with no large-language-model in the order-placement path.

### The signal path (the spine of the system)

```
TradingView alert
   → webhook (HTTP POST)
      → n8n workflow (an automation tool; validates + writes the signal to a file)
         → JSON file dropped into a watched folder
            → NinjaTrader 8 (the trading platform; a NinjaScript strategy watches that folder)
               → bracket order (entry + stop + target)
                  → Rithmic (the brokerage order-routing API)
                     → MFFU funded account (the capital the system trades)
```

Definitions of the moving parts, for readers who have not seen the internal shorthand:

- **TradingView** — the charting service that emits the alert that starts the chain.
- **n8n** — a self-hosted, open-source workflow-automation tool running in a Docker container. In PRAXIS it receives the webhook, validates the payload, and writes a signal file.
- **NinjaTrader 8 (NT8)** — the Windows desktop trading platform. Strategies for it are written in **NinjaScript**, which is C# on the .NET 4.8 runtime. The PRAXIS strategy uses a **FileSystemWatcher** (a standard .NET component that fires when a file appears in a folder) to detect new signal files.
- **Rithmic** — the low-latency futures order-routing API/brokerage connection NT8 talks to.
- **MFFU** — the funded-account provider ("My Funded Futures"-style prop account). This is the account with a real trailing-drawdown limit that the system is ultimately meant to trade. No live capital is being traded today; all current work is on simulated ("sim") accounts and historical backtests.

### The execution host, today

NT8 runs inside a **Parallels Windows 11 ARM virtual machine (VM) on an Apple-Silicon Mac Studio.** The Mac cannot run Windows natively (no Boot Camp on Apple Silicon), so the VM is the build-and-simulation host. A dedicated native x64 Windows PC is a documented, required hardening step **before any live trading** — the VM is explicitly a build/sim expedient, not the live host. (This is a planned gate, not a deviation.)

### The block structure (so you can locate progress)

The build is organized into seven blocks, 0 through 6. Each block ends in a **milestone that only Amear can sign off** — the build side never self-certifies a milestone.

- **Block 0 — Infrastructure setup.** Git, issue tracker, Google Sheets dashboard, n8n webhook + Telegram notifications. **Milestone signed off by Amear 2026-07-09.**
- **Block 1 — Foundation / the signal path on sim data.** Build the full delivery pipe end-to-end on simulated data. **Milestone signed off by Amear 2026-07-15.**
- **Block 2 — Backtesting.** *Current block, in progress.* Re-implement and validate the trading strategy against historical NQ data.
- **Block 3 — Circuit breakers** (includes the Strategy Health Monitor, described below). Not started.
- **Block 4 — Paper trading.** Not started.
- **Block 5 — Graduated live deployment.** Gated by a hard comprehension test (see §6). Not started.
- **Block 6 — Satellite strategies.** Not started.

### The Strategy Health Monitor (SHM), so a later reference makes sense

The **SHM** is a planned component (Block 3 build, thresholds locked at the Block 2 milestone) that asks one question the circuit breakers do not: *is the strategy's edge itself dead or decaying?* Its retirement/demotion thresholds are meant to be written **quantitatively and in advance**, derived from Block 2 backtest output, so that a "should I stop trading this?" decision is never made discretionarily mid-drawdown. It matters here only because Block 2's job is to produce the distributions the SHM thresholds are read from.

---

## 2. Overall status in one paragraph

Blocks 0 and 1 are **complete and milestone-signed-off by Amear.** The full signal-delivery pipe works end-to-end on sim data and has been exercised in NT8. The project is now inside **Block 2 (backtesting)**, which is **in progress**: the strategy has been re-implemented in NinjaScript, a continuous historical NQ price series has been constructed and validated, and the remaining gate is a set of steps that must run inside the Windows VM (compile the strategy, import the data, run the backtest, reconcile the output). Two build-tooling side-efforts from the most recent sessions — a reusable VM-delegation workspace and a teaching-agent — are **built but not yet proven/accepted**; both are honestly reported as such below.

---

## 3. Block 1 — the signal path (shipped, milestone-signed-off)

**State: COMPLETE. Amear signed off the Block 1 milestone on 2026-07-15**, on the basis of an independent evidence audit (repository commit `d405125`).

What was actually built and verified on simulated data:

- **n8n receives the webhook and writes the signal file atomically** (writes to a temporary name, then renames — so a half-written file is never picked up), with a retry and an error-notification path. (Block 1 item "B1-b".)
- **A Mac-side relay** moves the signal file into the folder shared into the Windows VM. This started as an event-triggered launchd job but was re-architected into a **persistent 1-second sweep daemon** after measurement showed the event-trigger mechanism imposed a ~10-second minimum-runtime throttle that broke the under-5-second delivery target. Delivery is now ~0.5–1.3 seconds. (Decision record **D-2026-07-12-A**; this is an internal build-mechanics change, not a strategy/plan deviation.)
- **The NinjaScript consumer** (`ninjascript/PraxisSignalConsumer.cs`) runs inside NT8. It is **hard-guarded to sim-only accounts** (a non-configurable account-name-prefix check), de-duplicates signals by an in-file `signal_id` using an append-only journal (so a signal is submitted **at most once**, even across a platform restart), and places one bracket order per new signal. It also has a **pre-submit geometry gate**: it rejects any bracket whose stop/target sit on the wrong side of the market, placing zero orders in that case.
- **Latency, idempotency, and offline-failure behavior were tested** (Block 1 items B1-d, B1-e): under-5-second delivery confirmed, duplicate-signal suppression confirmed, and a silent-loss gap found in the offline drill was closed by an added stuck-backlog detector.
- **The four acceptance tests (T1–T4)** — valid signal produces one bracket; a repeated `signal_id` produces no second order; a malformed signal is rejected; a platform restart does not replay old signals — **all passed**, and the resulting standing bracket order was **confirmed by Amear in the live NT8 GUI** (entry filled, stop and target both working on one OCO order, no errors).

**Known-open items carried into Block 2 with Amear's eyes open** (all minor, none blocking): a bracket-cascade bug on a specific reject path (`btb`), a VM rendering glitch that is monitor-only (`518`), and a couple of low-priority follow-ups. These were disclosed at the milestone sign-off; the milestone was taken deliberately with them open.

**One Block-1 topology choice was an approved deviation from the original plan — see §7, item G.**

---

## 4. Block 2 — backtesting (in progress)

This is the current block. Its job: prove the strategy on historical NQ data and produce the out-of-sample performance distributions that later blocks (SHM thresholds, sizing) depend on.

### 4.1 The strategy under test

The strategy is a **clock-anchored noise-area breakout** on NQ, following the published methodology of Zarattini, Aziz, and Barbon (sourced from their SSRN working paper 4824172; the canonical ruleset is recorded in the repo at `docs/specs/2026-07-16-b2-noise-area-ruleset.md`). In plain terms: it anchors to the session open, builds a "noise band" around price, and trades breakouts out of that band at fixed clock checkpoints.

The strategy has been **re-implemented from scratch in NinjaScript** (`ninjascript/PraxisNoiseAreaBreakout.cs`, first authored at commit `719ab11`) because it was not exportable from TradingView — **this is an approved deviation, §7 item A.** The first-pass build is a **faithful paper replication with fixed parameters** (no optimization on the first pass) — **also an approved deviation, §7 item D.** During the code audit, two parameters that had been quietly made tunable were caught and fixed back to fixed constants, so the replication baseline stays clean.

### 4.2 Historical data acquisition and construction

The backtest needs a single **continuous** multi-year NQ 1-minute price series. Individual NQ futures contracts expire quarterly, so a continuous series has to be stitched from ~22 individual expiry contracts with a defined roll rule and price back-adjustment. Status:

- **Raw data landed:** all 44 raw export files (22 daily + 22 one-minute contracts) were pulled from NT8's default data provider inside the VM and delivered to a shared folder. **No paid data was purchased — this is an approved deviation, §7 item F.**
- **Continuous series built and validated:** a Python stitching tool (`scripts/b2_stitch.py`) computed the roll dates, applied additive ("Difference"/Panama) back-adjustment to remove the artificial price gaps at each roll seam, and emitted the continuous series. It was then converted from UTC to US-Eastern wall-clock time (an early conversion attempt silently dropped ~2,498 evening bars at each roll boundary; the independent auditor **caught that and failed it**, and the fix was re-verified to reproduce the exact original bar count of **1,857,362 bars**, seam-gap zero). The validated series lives on the share at `~/praxis-signals/b2-data/NQ-continuous-1min.csv`.
- **Roll convention** — the trigger and back-adjustment rule went through an approved chain of deviations driven by a hard platform limitation (NT8 cannot export open-interest data). **See §7 item E** for the full chain; the net result is a **volume-only crossover roll trigger with Difference back-adjustment**, with each such stitch run printing a loud "volume-only deviation" banner so the choice is never silent.

### 4.3 What is built vs. what is blocked on the trader/VM

The **entire remaining Block-2 critical path is gated on steps that must run inside the Windows VM**, because compiling a NinjaScript strategy, importing data into NT8, and running its Strategy Analyzer are all GUI/desktop operations on the trader's machine. Concretely, the remaining `4uu` work is:

1. Import the continuous series into NT8 as a custom instrument.
2. Compile `PraxisNoiseAreaBreakout.cs` (the F5 compile).
3. Run it in the NT8 Strategy Analyzer over the historical series.
4. Reconcile the strategy's generated signals against the specification (a self-contained spec-consistency check — there is no external TradingView-alert corpus to reconcile against, because this is a paper re-implementation, not a port of a live system; this reconciliation basis was settled with Amear in an interactive session).

**Status of `4uu` (the signal-reproduction / re-import task):** *not yet completed.* Two earlier import attempts inside the VM did not produce the backtest output:

- The 2026-07-24 attempt **failed on two now-fixed causes**: the import filename was missing a required data-type token, and an NT8 rendering fault silently dropped GUI clicks. Both are resolved (a corrected instruction brief was written, specifying a dedicated custom instrument named `NQCONT`, the correct filename `NQCONT.Last.txt`, an explicit US-Eastern timezone override, and a restart precondition; the rendering fault was independently confirmed cleared).
- A subsequent VM pass was a **layout-reference capture** (screenshots of the NT8 interface), **not** the re-import — so no compile/backtest output exists yet.

As of this report, the folder that would hold the VM's output still contains only those two capture artifacts. The corrected brief is staged and ready to be handed to the VM agent again. **Once real compile + backtest output lands, an independent read-only auditor grades it; on a pass, `4uu` closes and the downstream chain unblocks:** walk-forward analysis (`zi1`) → Monte-Carlo envelope (`ajj`) → SHM reference distributions (`xdr`). None of those three has started; they are all blocked behind `4uu`.

**Block-2 scope was fixed with Amear** across a batch of decisions (the walk-forward pass/fail gate, the cost model, the data-depth target, the sizing basis, the optimization scope, and the SHM band form), recorded as decision **D-2026-07-15-B** and in the scope proposal `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md`. I report these as fixed inputs to the build; their appropriateness is your domain, not mine.

---

## 5. Two build-tooling efforts from the latest sessions (built, not yet accepted)

These are not part of the trading strategy; they are infrastructure for how the build delegates work and how the trader learns the system.

### 5.1 The VM-agent delegation workspace (`852`) — BUILT Mac-side, live executor leg NOT yet proven

**This is the item to read most carefully, because its honesty boundary is precise.**

*Context:* much of Block 2's remaining work has to happen inside the Windows VM, and until now each VM task was handed off with an ad-hoc, one-off brief. Amear asked for a single reusable **delegation workspace**: a dedicated directory where the Mac-side orchestrator posts a task and a Windows-side agent picks it up and executes it.

*What was built:* the workspace exists on the Parallels share at `~/praxis-signals/vm-agent/` (which surfaces inside Windows at `C:\Mac\Home\praxis-signals\vm-agent\`). It contains a standing agent brief encoding the hard limits (sim-only, recompute-hashes-never-trust-pasted, real Windows paths, stop-and-flag on anything live), a README describing the post/grade/archive protocol for the orchestrator, an assignment template, staged Windows reference material, and a **sample assignment** (`0000-sample-roundtrip`) posted in a `QUEUED` state. The assignment lifecycle uses an in-place status field (`QUEUED → CLAIMED → IN_PROGRESS → DONE`/`BLOCKED`) rather than moving files between folders, chosen so the workspace survives being reshared and works for an executor with no session memory. The approved design is at `docs/specs/2026-07-25-vm-agent-delegation-workspace-design.md` (committed `0229da7`).

*What is explicitly NOT proven:* **no round-trip through the workspace has actually run.** The Mac-side structure is fully built and its Mac-side acceptance is met, but the **live executor leg is unproven** — an agent inside the VM has not yet claimed the sample assignment, recomputed the hash, written the output, and set it to `DONE`, and the auditor has not yet graded that output. That live round-trip is scheduled for the next Windows session and **will not be faked to a pass.** The tracking item `852` is deliberately **left open** for exactly this reason. **Do not read this as a working executor pipeline — read it as a built workspace whose live leg is pending.**

### 5.2 The teaching-agent (`bev`) — BUILT, awaiting Amear's dry-run

A repository sub-agent (`praxis-tutor`, defined in `.claude/agents/praxis-tutor.md`) was built to teach Amear individual PRAXIS/NT8 tasks in his documented learning style. It is deliberately constrained: it is a behaviors-only artifact (the repository is public, so no personal/clinical material is in it), and it is structurally blocked from committing code, closing tracker items, or certifying anything. **It is built but not yet accepted** — acceptance is a live dry-run teaching session that Amear signs off; the build side cannot self-certify it. Its relevance to your plan: it is the delivery mechanism for the **Block-5 comprehension gate** (see §6).

---

## 6. One planned gate you should be aware of (not a deviation — a plan element being honored)

The plan includes a **hard comprehension gate before any live trading**: Block 5 does not open until Amear can explain, unprompted and without notes, (1) what determines an entry, (2) what determines an exit, and (3) what trips each circuit breaker — verified in a recorded debrief, pass/fail, no partial credit (decision **D-2026-07-04-A**). I mention it because the teaching-agent (§5.2) exists to serve it, and because the build is being sequenced to respect it. This is your plan being carried out, not changed.

---

## 7. Deviations from the original plan that Amear approved (explicit)

This section is the point of the report. Each item names the deviation, states what the original plan called for, states what was done instead, and cites the decision record where Amear approved it. I am reporting these as facts of the build; I am **not** arguing that any of them was the right call — that judgment is yours.

Notation: **DECISIONS.md** is the project's append-only architectural-decision record; **DECISION_LOG.md** is the append-only log of dated orchestrator/trader judgments (each row is timestamped and names WHO decided). "AskUserQuestion" denotes an in-session structured prompt Amear answered directly.

### A. Strategy is re-implemented in NinjaScript instead of exported from TradingView
- **Original plan assumption:** the strategy would come from TradingView (implying an exportable strategy definition to port).
- **What was done:** the strategy was found **not** to be TradingView-exportable (no Pine source anywhere; the live TradingView payload carries only side/timestamp/id, no strategy internals). The entry logic was therefore **re-implemented from scratch in NinjaScript** and will be backtested in the NT8 Strategy Analyzer (the scope proposal's "path b").
- **Amear approved:** yes — confirmed via AskUserQuestion on an audited exportability report. **Citation:** DECISION_LOG.md row **2026-07-15T21:10Z** ("Block-2 Q1 CONFIRMED … NOT TradingView-exportable … RE-IMPLEMENTED in NinjaScript"); report `docs/reports/2026-07-15-b2-q1-strategy-exportability.md`; commit `8e739e4`.

### B. Session-flat at 16:00 ET (cash-market close) instead of the 11:30 PRAXIS window
- **Original plan assumption:** an earlier PRAXIS framing used an 11:30 session-flat window.
- **What was done:** the strategy flattens at **16:00 ET (equities cash close)**, matching the source paper's methodology (whose entire performance record is measured full-day-to-16:00).
- **Amear approved:** yes — AskUserQuestion on the audited ruleset spec. **Citation:** DECISION_LOG.md row **2026-07-16T19:29Z**, item (1); spec `docs/specs/2026-07-16-b2-noise-area-ruleset.md`.

### C. Reverse-and-re-enter within a session instead of one position per session
- **Original plan assumption:** one position per session.
- **What was done:** the strategy **reverses and re-enters** on an opposite-band cross, per the source paper.
- **Amear approved:** yes — same AskUserQuestion batch. **Citation:** DECISION_LOG.md row **2026-07-16T19:29Z**, item (2).

### D. First build is a fixed-parameter paper replication — no optimization grid on the first pass
- **Original plan assumption:** decision D-2026-07-15-B (Q7) had framed the first pass as optimizing a set of parameters {lookback, noise multiplier, stop-ATR multiplier, exit policy} inside a walk-forward matrix.
- **What was done:** the **first build is a pure paper replication with fixed parameters** (lookback 14, band 1σ, no noise multiplier, no ATR stop, opposite-band/VWAP exit) — **no optimization on the first pass.** Walk-forward optimization is deferred to a later, separate arm on top of the replication baseline. This **explicitly supersedes** the Q7 optimize-set framing (the noise-multiplier and stop-ATR parameters have no analog in the paper).
- **Amear approved:** yes — same AskUserQuestion batch, and the decision text records that it supersedes the earlier Q7 framing. **Citation:** DECISION_LOG.md row **2026-07-16T19:29Z**, item (3).

### E. Roll-convention chain: locked convention → built outside NT8 in Python → volume-only trigger
This is a **three-step chain of approved deviations**, each forced by a discovered constraint. I give all three because the net rule differs from where the plan started.
- **E1 — roll convention locked.** For the continuous NQ series, Amear locked **volume/open-interest-crossover roll trigger + Difference (back-adjusted/Panama) construction** (Difference preserves absolute point distances, which the breakout strategy measures; Ratio adjustment was rejected for distorting them). **Citation:** DECISIONS.md "2026-07-15 — b2-data … roll convention"; DECISION_LOG.md row **2026-07-15T22:30Z**; spec `docs/specs/2026-07-15-b2-data-acquisition-spec.md` §2.
- **E2 — build the series outside NT8, in Python.** The VM's NT8 install could **not natively construct** that roll convention (it offers Difference back-adjustment but only a calendar/expiry roll trigger, not a volume/OI crossover). Given four options, Amear chose to **build the continuous series outside NT8 in Python** from individual expiry contracts, exactly reproducing the locked convention, then re-import to NT8. The convention itself was unchanged; only the build path moved. **Citation:** decision **D-2026-07-17-A** (DECISIONS.md); confirmed via AskUserQuestion.
- **E3 — volume-only trigger (drop OI).** It was then confirmed that **NT8 cannot export open-interest data at all** (a hard platform limitation, not a config miss), so the OI half of the crossover trigger was uncomputable. Amear authorized a **volume-only crossover roll trigger**, with **Difference back-adjustment unchanged** — the only change is dropping OI from the trigger test. The accepted trade-off (roll seams may land ~1–2 days from where a true volume+OI crossover would place them) is on the record, and every stitch run prints a loud volume-only-deviation banner. **Citation:** decision **D-2026-07-21-A** (DECISIONS.md); DECISION_LOG note that verbal VM approval was **not** treated as sufficient — the in-ledger append is the actual authorization.

### F. Data source = NT8 default provider's minute history, no paid-data budget
- **Original plan assumption:** the scope proposal contemplated data-source trade-offs (including paid providers such as FirstRate).
- **What was done:** the backtest uses **NT8's default-provider minute history with no paid-data budget** for this block, with a data-depth target of ≥4 years / ≥12 out-of-sample windows and any shortfall to be logged rather than silently accepted.
- **Amear approved:** yes — AskUserQuestion (Block-2 Q4). **Citation:** DECISIONS.md **D-2026-07-15-B**, Q4; DECISION_LOG.md row **2026-07-15T22:05Z**.

### G. Block-1 topology: n8n runs locally on the Mac; public ingress and the WireGuard tunnel deferred to pre-live
- **Original plan assumption:** the Block-1 signal-delivery design assumed a remote internet-facing n8n host pushing signals down an encrypted WireGuard tunnel to the Mac.
- **What was done:** for build-first sim work, **n8n runs locally on the Mac**, the signal path is exercised with local test webhook posts, and the whole question of how live public-internet TradingView signals reach the system (rent a VPS + WireGuard vs. a tunnel relay) is **deferred to pre-live (Block 4–5)**. The WireGuard-over-Tailscale reasoning is preserved for when ingress returns; it is deferred, not deleted.
- **Amear approved:** yes — chose local-n8n / defer-ingress via AskUserQuestion when it surfaced that he owns no VPS and sim work exercises no public ingress. **Citation:** decision **D-2026-07-09-D** (DECISIONS.md); DECISION_LOG.md row **2026-07-09T00:00Z** (n8n-local).

---

## 8. Where the build stands relative to your plan — a factual summary

- **Blocks 0 and 1: done, Amear-signed-off.** The signal path is real and works on sim data.
- **Block 2: in progress.** Strategy re-implemented; continuous historical series built and validated (1,857,362 bars); the remaining gate (`4uu`: import + compile + backtest + reconcile inside the VM) has **not yet produced output** after two VM attempts, and everything downstream of it (walk-forward, Monte-Carlo, SHM reference distributions) is blocked behind it.
- **Two infrastructure efforts (`852` delegation workspace, `bev` teaching-agent): built, not yet accepted** — the delegation workspace's live executor leg is explicitly **unproven** and its tracking item is deliberately left open; the teaching-agent awaits a trader dry-run.
- **Blocks 3–6: not started.** The Block-5 pre-live comprehension gate remains a planned, hard, human-verified checkpoint.

Everything above is a statement about the build. The plan and the strategy remain yours; nothing here should be read as the build side proposing a change to either.

---

*End of report. Grounding sources: STATUS.md (session-28 state), DECISIONS.md, DECISION_LOG.md, MANIFEST.md, the issue tracker (beads wx7 / 852 / 4uu / bev / hlw / zi1 / ajj / xdr and the Block-1 items), and the repository commit log through commit `de23587`.*
