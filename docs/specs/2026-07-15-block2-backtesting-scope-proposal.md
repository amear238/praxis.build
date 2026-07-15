# BLOCK 2 — BACKTESTING SCOPE PROPOSAL
**Project:** PRAXIS | **Date:** 2026-07-15 | **Bead:** Praxis_build-s1c | **Status:** PROPOSAL — nothing herein is binding

> **Scope wall.** This is a planning document only. Every numeric value below is a **PROPOSAL** until the trader locks it (SHM thresholds lock at the Block-2 milestone per D-2026-07-04-B and SHM spec §2 "Core Principle — Pre-Commitment"). The authoritative **PHASE 3 BUILD SPECIFICATION has not been imported into the repo**; its Block-2 exit-milestone text is MISSING (see §5). This document deliberately does **not** invent binding milestone criteria in its place. No phase advancement or sign-off is implied anywhere below — that authority is trader-only.

---

## 0. What Block 2 must produce (per existing repo commitments)

The SHM spec (§3 "Monitored Signals", §5 "Implementation Notes") already obligates Block 2 to output two concrete artifacts:

1. **Walk-forward out-of-sample (OOS) window distribution** — feeds SHM-1 (rolling PF percentile) and SHM-5 (signal frequency band).
2. **Monte Carlo drawdown envelopes** (depth + duration) — feeds SHM-2 and SHM-3.

Both land as `/shm/reference_distributions.json` — "generated once at Block 2 milestone, git-tracked, immutable" (SHM §5). Everything below is scoped to produce those artifacts credibly, plus a live-vs-backtest baseline for SHM-4.

---

## 1. Walk-Forward OOS Methodology — PROPOSAL

### 1.1 Window structure options

| Option | How it works | Pros | Cons |
|---|---|---|---|
| **Anchored** | IS start fixed; IS grows each step; OOS slides forward | More data per fit; stable parameters | Old regimes never age out; NQ microstructure has changed (tick programs, 0DTE era) |
| **Rolling (recommended PROPOSAL)** | Fixed-length IS window slides with OOS | Adapts to regime; every OOS window comparable — cleaner distribution for SHM-1 | Fewer samples per fit; noisier parameter estimates |

**PROPOSAL:** Rolling, because SHM-1 compares live rolling PF against the *distribution of OOS windows* — that comparison is only apples-to-apples if OOS windows come from same-length IS fits.

### 1.2 Split geometry — PROPOSAL (all numbers PROPOSAL)

| Parameter | PROPOSAL | Rationale (one line each) |
|---|---|---|
| IS : OOS ratio | 3 : 1 (e.g. 9 mo IS / 3 mo OOS) | Common WFA default; enough IS to fit, enough OOS windows to build a distribution |
| Step size | = OOS length (non-overlapping OOS) | Overlapping OOS windows inflate the SHM-1 percentile sample with correlated points |
| Total history | ≥ 4 years NQ (≥ 12 OOS windows) | Fewer than ~12 OOS windows makes a "5th percentile" (SHM-1 candidate) statistically meaningless |
| Re-optimization cadence (live) | Per D-2026-07-04-B protocol only — no scheduled re-opt inside Block 2 | SHM pre-commitment (§2) forbids threshold/parameter drift while underwater; re-opt policy is a trader decision |
| Walk-forward efficiency (WFE) gate | OOS/IS performance ratio ≥ 0.5 flagged as CANDIDATE screen | Standard overfit smoke-test; final gate belongs to PHASE 3 BUILD SPEC (§5, gap Q3) |

### 1.3 Data-source options for NQ futures

| Source | Granularity | Cost/effort | Trade-offs |
|---|---|---|---|
| **NT8 historical (default provider)** | Minute reliable; tick spotty pre-recent | Included | Already in stack; continuous-contract splicing settings must be pinned and recorded; depth of tick history varies by provider |
| **Rithmic history (via NT8 connection)** | Tick, but shallow lookback | Included w/ MFFU conn | Best fidelity match to live fills (same feed as execution) but typically months not years — good for SHM-4 baseline, insufficient for 4-yr WFA |
| **Kinetick (NT8 native partner)** | EOD free; minute/tick paid | $ | Cleanest NT8 integration for deep minute history |
| **Third-party archive (e.g. CQG/CSI/Portara-class NQ tick sets)** | Deep tick | $$–$$$ | Only route to multi-year tick-accurate fills; import/rollover handling becomes our problem |

**PROPOSAL:** Hybrid — deep minute-level history (NT8 default provider or Kinetick) for the walk-forward matrix, plus Rithmic-fed recent tick data to (a) validate fill assumptions and (b) seed the SHM-4 live-vs-backtest divergence baseline. Contract-roll convention (back-adjusted continuous, roll rule pinned in the config) recorded in DECISIONS.md before the first run.

**Open dependency:** the strategy under test. B1-f consumes external TradingView signals; backtesting them requires either (a) exporting the TradingView strategy's historical signal series, or (b) re-implementing the entry logic in NT8. This is spec-gap Q1 (§5) — it changes the entire Block-2 toolchain and must be answered first.

---

## 2. Monte Carlo Scope — PROPOSAL

### 2.1 What gets resampled

| Method | What it preserves / destroys | Verdict (PROPOSAL) |
|---|---|---|
| **Trade-order shuffle (permutation, no replacement)** | Keeps the exact trade P&L set; destroys sequence | INCLUDE — canonical envelope for SHM-2/SHM-3 (sequence risk is what drawdown envelopes measure) |
| **Trade bootstrap (resample with replacement)** | Allows repeated/omitted trades; wider tails | INCLUDE — stress variant; use for risk-of-ruin |
| **Returns/bar bootstrap** | Resamples underlying returns, not trades | EXCLUDE for Block 2 — divorces results from the actual signal process; adds model risk without feeding any SHM signal |

**PROPOSAL:** Run both trade-level methods on the pooled walk-forward **OOS** trade list only (never IS trades — envelopes must describe what validation, not fitting, said was possible).

### 2.2 Run counts and extracted metrics (all numbers PROPOSAL)

| Item | PROPOSAL | Feeds which decision |
|---|---|---|
| Iterations | 10,000 per method | Stable 95th/99th percentile tails; cheap at trade-list scale |
| Max drawdown depth distribution (R-multiples) | Record full distribution + 95th/99th pct | SHM-2 threshold lock; also position-sizing sanity vs MFFU account drawdown rules |
| Time-underwater distribution (trading days) | Full distribution + 95th/99th pct | SHM-3 threshold lock |
| Risk-of-ruin | P(equity path breaches MFFU trailing-drawdown limit) at proposed size | Go/no-go input on contract sizing for Block 4/5 — trader decision, not auto-gate |
| CAR/MDD (return-to-drawdown ratio) distribution | Median + 5th pct | "Is this edge worth the pain" review input at the Block-2 milestone discussion |
| Units | R-multiples throughout (SHM §3, SHM-2: "R-multiples, not dollars") | Keeps envelopes valid across sizing changes |

---

## 3. SHM Threshold PROPOSALS

Mapped to SHM spec v0.1 §3 signal-by-signal. **Every value is a PROPOSAL; per SHM §2 and §3, values lock only via trader decision at the Block-2 milestone (DECISIONS.md entry).** The spec's own "candidate" placeholders are noted where they exist.

| SHM signal (spec §3 name) | Parameter | PROPOSAL | One-line rationale |
|---|---|---|---|
| SHM-1 Rolling Profit Factor vs. OOS Distribution | Trailing window N | 25 trades | Matches spec's candidate and the Block-4 minimum sample it cites |
| SHM-1 | Trigger percentile | 5th pct of OOS-window PF distribution | Spec's candidate; ~1-in-20 false-fire rate per evaluation is tolerable given demote-to-paper (not retire) consequence |
| SHM-2 Drawdown Depth vs. Monte Carlo Envelope | Trigger percentile | 95th pct of MC max-DD depth (R) | Spec's candidate; symmetric with SHM-3 so a single "outside the modeled envelope" story covers both |
| SHM-3 Drawdown Duration vs. Monte Carlo Envelope | Trigger percentile | 95th pct of MC time-underwater | Spec's candidate; duration is "decay's most common signature" (§3) so it must not be looser than depth |
| SHM-4 Live-vs-Backtest Divergence | Rolling window | 20 trades (per spec) | Spec fixes the window; only the bands are open |
| SHM-4 | Divergence bands | Win rate > 15 ppts below backtest, OR mean slippage > 2 ticks/side worse than modeled, over the 20-trade window | Coarse, few, pre-declarable bands beat a fitted statistic nobody trusts; both are directly measurable from the B1 journal + fill log |
| SHM-5 Signal Frequency Drift | Frequency band | Monthly signal count within [0.5x, 2.0x] of backtest monthly mean, breach = 2 consecutive months (per spec) | Wide asymmetric-tolerant band; NQ signal regimes are lumpy and SHM-5 should catch structural silence/flood, not seasonality |
| SHM-4 re-promotion sample (spec §4 "[TBD] trades") | Paper re-clear sample | 25 trades with all SHM signals in-bounds | Reuses the SHM-1 window so "back inside bounds" is measured on the same yardstick that fired |

Not proposed here (trader/spec territory): any change to the firing protocol (§4), adjustment protocol (§2), or where SHM runs (§5 — n8n, deterministic, no LLM).

---

## 4. CANDIDATE Block-2 Exit Criteria — NON-BINDING

**CANDIDATE ONLY.** The real exit-milestone definition must come "verbatim from PHASE 3 BUILD SPECIFICATION" (skill outline §B) — that spec is not in the repo. This checklist is a strawman for the trader to react to; it certifies nothing and cannot be used to advance the phase.

- [ ] CANDIDATE — Strategy signal history reproduced in the backtest engine and reconciled against a sample of live/sim TradingView alerts (gap Q1 resolved first)
- [ ] CANDIDATE — Walk-forward matrix run to completion; ≥ 12 OOS windows; configuration (windows, roll rule, costs, slippage model) committed to the repo
- [ ] CANDIDATE — Monte Carlo (shuffle + bootstrap, 10k each — PROPOSAL) run on pooled OOS trades; depth/duration/RoR/CAR-MDD distributions reported
- [ ] CANDIDATE — `/shm/reference_distributions.json` generated, git-tracked, and schema-checked against what the Block-3 SHM build will read
- [ ] CANDIDATE — SHM thresholds (§3 above) reviewed, adjusted, and LOCKED by the trader via DECISIONS.md entry (D-2026-07-04-B sequencing)
- [ ] CANDIDATE — Written go/no-go review: does the OOS + MC evidence justify proceeding at proposed sizing? (trader decision, recorded)
- [ ] CANDIDATE — Independent evidence audit of all of the above (orchestrator-auditor, non-certifying), then **trader sign-off — the only act that closes Block 2**

---

## 5. Spec-Gap List — questions only the PHASE 3 BUILD SPEC or the trader can answer

| # | Open question | Why it blocks |
|---|---|---|
| Q1 | **What exactly is the strategy under test?** Is the TradingView strategy exportable as a historical signal series, or must entry logic be re-implemented in NT8/Python for backtesting? | Determines the entire Block-2 toolchain (NT8 Strategy Analyzer vs external engine vs signal-replay harness) |
| Q2 | The verbatim Block-2 exit-milestone text (skill outline §B requires it from PHASE 3 BUILD SPEC) | Without it, §4 stays CANDIDATE and no completion claim is possible |
| Q3 | Minimum acceptable walk-forward results (WFE floor, min PF, min trade count) — are there spec-mandated gates? | Decides whether Block 2 can "fail" and what failure routes to |
| Q4 | Required history depth and mandated data source/granularity (minute vs tick), and the budget for paid data | Constrains §1.3 choice before any run |
| Q5 | Cost model to assume: commissions, slippage ticks/side, and whether MFFU/Rithmic fee schedule is specified | P&L and every SHM distribution are meaningless without pinned costs |
| Q6 | Contract sizing basis for risk-of-ruin (1 NQ? MNQ? MFFU account size + trailing-drawdown parameters) | RoR (§2.2) is undefined without account rules |
| Q7 | Does Block 2 include parameter optimization at all, or validation-only of fixed TradingView parameters? | Changes IS windows from "fit" to "measure" and shrinks scope materially |
| Q8 | Where do backtest runs execute (VM NT8, Mac-side Python, both) and what artifacts must be archived? | Platform annotations are mandatory per skill §B; affects bead decomposition below |
| Q9 | SHM-4/SHM-5 band *form* preference (ppts/ticks bands as proposed vs statistical test) | Trader must be willing to be auto-demoted by the chosen form — behavioral fit matters (SHM §2 rationale) |

### Q1 — RESOLVED (proposed, pending trader confirmation)

**Answer:** The strategy under test is the **Zarattini–Aziz–Barbon NQ "Noise-Area" intraday breakout** (clock-anchored, rules-based, one bracket/session). It is **NOT exportable from TradingView** — no Pine source exists in-repo and the live webhook payload `{symbol, side, qty, price, signal_id, ts}` carries no strategy internals. It must be **re-implemented as a NinjaScript strategy and backtested in NT8 Strategy Analyzer**, which the Phase 3 Build Spec already mandates (High fill res, 1-tick series, 1-tick slippage, $2.96 RT commission; rolling WFA 252/63/63; optimize {lookback, noise mult, stop-ATR mult, exit policy}). Toolchain = **NT8 Strategy Analyzer** (primary) + FirstRate 1-min NQ history + forward Rithmic tick for OOS; Python only as a downstream Monte Carlo layer over the exported OOS trade list. This collapses execution-sketch bead **b2-signal-repro** to a NinjaScript port + live-alert reconciliation — no external-export or signal-replay harness is needed.

**Still PENDING trader confirmation:** whether any TradingView Pine source exists / TradingView's role (generator vs passthrough); the canonical ruleset + parameter ranges + concrete exit-policy form; and Q7 (optimize vs validate-only). Full evidence and per-path assessment: `docs/reports/2026-07-15-b2-q1-strategy-exportability.md`.

---

## 6. Execution Sketch — likely bead decomposition (dependency order)

Illustrative only; beads get filed when the trader accepts scope.

1. **b2-spec-import** — Obtain/import PHASE 3 BUILD SPEC Block-2 text; resolve Q1–Q9 with trader; record decisions. *Blocks everything.*
2. **b2-data** — Acquire + validate NQ history (source per Q4), pin roll convention + cost model (Q5) via DECISIONS.md.
3. **b2-signal-repro** — Reproduce strategy signals in the chosen engine (per Q1); reconcile a sample against known live/sim alerts.
4. **b2-wfa** — Build + run the walk-forward matrix (§1); emit OOS window stats. *Depends: 2, 3.*
5. **b2-mc** — Monte Carlo engine on pooled OOS trades (§2); emit envelope distributions. *Depends: 4.*
6. **b2-refdist** — Generate `/shm/reference_distributions.json` + schema doc for the Block-3 SHM consumer. *Depends: 4, 5.*
7. **b2-threshold-lock** — Trader threshold-lock session: review §3 PROPOSALS against real distributions; DECISIONS.md entry. *Trader-gated.*
8. **b2-milestone-audit** — Independent evidence audit (non-certifying) → trader sign-off decision. *Trader-gated; closes Block 2 only if the trader says so.*

---
*End Block-2 scope proposal — all values PROPOSAL; milestone authority: trader only.*
