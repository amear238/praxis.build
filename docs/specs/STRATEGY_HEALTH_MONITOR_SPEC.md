# STRATEGY HEALTH MONITOR (SHM) — SPECIFICATION v0.1
**Project:** PRAXIS | **Added:** 2026-07-04 | **Ref:** DECISIONS D-2026-07-04-B | **Open Item:** #7

---

## 1. PURPOSE — WHAT THIS IS AND IS NOT

Three defensive layers now exist. They answer different questions. Do not conflate them.

| Layer | Question it answers | Timescale | Action |
|---|---|---|---|
| Nine circuit breakers | "Is the system operating safely right now?" | Per-order / intraday | Block order submission |
| Block 5 kill criteria | "Is live execution failing?" | Days–weeks | Demote a graduation phase |
| **Strategy Health Monitor** | **"Is the edge itself dead or decaying?"** | **Weeks–months** | **Auto-demote strategy to paper** |

The SHM detects edge decay — the impersonal arbitrage of a published anomaly as capital crowds it. It is not a drawdown alarm. Drawdowns are expected and modeled. The SHM fires when live behavior falls **outside the distribution the backtest said was possible**.

---

## 2. CORE PRINCIPLE — PRE-COMMITMENT

All thresholds are written and locked **before** live deployment, derived from Block 2 walk-forward output. No threshold is adjusted while the strategy is in drawdown. Adjustments are permitted only:
1. While the strategy is at or above its rolling performance baseline, AND
2. Via an append-only entry in DECISIONS.md, AND
3. With a mandatory 5-trading-day cooling period between the proposed change and its activation.

**Rationale (behavioral):** the decision "is the edge dead or am I scared" is never made live. The system decides mechanically; the trader reviews afterward, offline, as research.

---

## 3. MONITORED SIGNALS (thresholds = placeholders; values locked at Block 2 milestone)

### SHM-1 — Rolling Profit Factor vs. OOS Distribution
- **Metric:** Profit factor over the trailing N trades (N = TBD at Block 2; candidate: 25, matching the Block 4 minimum sample).
- **Trigger:** Rolling PF falls below the [Xth] percentile of the walk-forward out-of-sample window distribution (candidate: 5th percentile).
- **Interpretation:** Live performance is worse than nearly every OOS window the validation produced. Either regime shift or decay.

### SHM-2 — Drawdown Depth vs. Monte Carlo Envelope
- **Metric:** Current peak-to-trough drawdown (R-multiples, not dollars).
- **Trigger:** Drawdown exceeds the [Xth] percentile of the Monte Carlo drawdown distribution generated from Block 2 results (candidate: 95th percentile).
- **Interpretation:** The system is losing more than the model said was statistically plausible.

### SHM-3 — Drawdown Duration vs. Monte Carlo Envelope
- **Metric:** Trading days since last equity high.
- **Trigger:** Duration exceeds the [Xth] percentile of the Monte Carlo time-underwater distribution (candidate: 95th percentile).
- **Interpretation:** Depth can be normal while duration is not. A shallow drawdown that never ends is decay's most common signature.

### SHM-4 — Live-vs-Backtest Divergence
- **Metric:** Per-trade comparison of live fills against the backtest model on the same signals — slippage, entry timing, MFE/MAE profile, win rate.
- **Trigger:** Divergence beyond [TBD] on a rolling 20-trade basis.
- **Interpretation:** Distinguishes "edge is dying" from "execution is degrading." An execution problem routes to infrastructure review, not strategy retirement.

### SHM-5 — Signal Frequency Drift
- **Metric:** Trades triggered per month vs. backtested frequency.
- **Trigger:** Frequency outside [TBD] band for two consecutive months.
- **Interpretation:** The market condition the strategy feeds on is appearing more or less often than history. Either direction is diagnostic.

---

## 4. FIRING PROTOCOL

1. **Any single trigger fires →** automatic demotion to paper trading before the next session. n8n executes the demotion; no order flows live. Telegram notification sent with the fired signal, the value, and the threshold.
2. **Trader review is scheduled, not immediate.** Minimum 48 hours after demotion before the review session (no underwater decisions, even in review form).
3. **Review is a research session** run against Block 2 tooling: was this regime shift, decay, execution degradation, or statistical noise at the tail?
4. **Re-promotion path:** identical to Block 5 rules — return to Phase A (1 MNQ), no skipping. Re-promotion requires the strategy to re-clear a defined paper sample ([TBD] trades) with SHM signals back inside bounds.
5. **Retirement:** If the review concludes decay (mechanism gone or crowded out), the strategy is retired via DECISIONS.md entry and the satellite pipeline (Block 6) supplies the replacement candidate. Retirement is a normal lifecycle event, not a failure. Published edges are decaying assets by definition.

---

## 5. IMPLEMENTATION NOTES

- **Where it lives:** n8n scheduled workflow (daily post-session) reading the trade log (PostgreSQL audit trail) + Block 2 reference distributions stored as static JSON in the repo (`/shm/reference_distributions.json`, generated once at Block 2 milestone, git-tracked, immutable).
- **No LLM in the loop.** SHM evaluation is deterministic arithmetic, same philosophy as the Python fallback script. Claude Code builds it; nothing intelligent runs it.
- **Build slot:** Block 3 (alongside circuit breakers — same deterministic-safety build session). Reference distributions plug in at Block 2 completion; thresholds locked then via DECISIONS.md entry.
- **Testing gate:** Every SHM trigger must be intentionally fired on synthetic trade-log data and verified to execute demotion + notification before Block 5 Phase A opens. Mirrors the Block 3 breaker milestone.

---

## 6. WHAT THE SHM DOES NOT DO

- It does not evaluate single trades (that is execution review / Praxis debrief territory).
- It does not halt intraday (that is the circuit breakers).
- It does not decide *why* the edge changed (that is the offline review).
- It does not consult the trader before demoting. Demotion is mechanical. Consultation is afterward.

---
*End SHM Spec v0.1 — numeric thresholds pending Block 2 milestone.*
