Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

> ***Added at import, 2026-11-05; not part of the source document.*** The line above is the project's standing limitation sentence, carried verbatim at the top of this file because the dispatching brief for this unit required it; the ledger rule, ruled by Amear, is that every backtest report carries it (`DECISIONS.md:302`). It differs from the Block 2 configuration this source specifies below (Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries). That difference is open under rubric F3 (`specs/SPEC_RUBRIC.md`); this import does not resolve it.

Here’s the Phase 3 build specification. Adapted for your local server, your proof-of-concept-first approach, and the conviction requirement.

# PHASE 3 — BUILD SPECIFICATION

> ***Added at import; not part of the source document.***
>
> **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ implemented ≠ tested ≠ tested under failure. Basis, checked 2026-11-05: `grep -rniE "breaker|circuit" ninjascript/` returns one hit, a source comment in `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` (line 31) that names breakers #4/#5 only to say that variant does not decide rubric F2 — a comment, not breaker code; `grep -rnilE "breaker" scripts/` returns nothing; there is no `n8n/` directory in the repository; across all tracked `.cs`/`.py`/`.js`/`.ts`/`.json`/`.sh`/`.ps1` files the only file mentioning "breaker" is that same `.cs` file. Scope of that basis: it is a keyword search. `ninjascript/PraxisSignalConsumer.cs` rejects any order whose qty exceeds a `MaxQty` sim sanity cap (default 5; lines 94 and 527–528), which resembles breaker #7's behaviour; it is not the specified n8n breaker and has not been tested as a breaker. Nothing in this document is evidence that any circuit breaker — or any other component described below — exists in working form. The body text is the source author's design language; where it speaks in the present tense (for example, that the system "blocks violations before they reach the order engine"), it is describing intent, not a built system. That wording is preserved verbatim because this is an import; it is not a status claim.
>
> **This document is an import of a pre-existing planning artifact, not new design work.** It is a markdown conversion of a document written earlier and held outside this repository. No design decision recorded below was made by, or originates in, the import. The conversion added no requirement, no threshold, no gate and no rationale.
>
> **De-identification.** Circuit breaker #5 is carried here as a session-window constraint. The source document's title for that breaker is **not** reproduced in this repository, and its underlying rationale is held outside this repository and is not stated here (this document's silence is a de-identification of *this* import only; it makes no claim about any other file in the repository). Breaker #5's *behaviour* is imported unchanged. Authorised by Amear's ruling in DECISION_LOG row `2026-08-06T20:18:56Z` (WHO: amear), present on main (in HEAD as of 2026-11-05). The `DECISIONS.md` entry `D-2026-08-06-A` that recorded the ruling exists only in commit `f258a5d` on the parked branch `parked/Praxis_build-r8j`; it is not in `DECISIONS.md` on main. The replacement wording in breaker #5's line ("Afternoon session window") is the importer's wording from 2026-08-06, not Amear's; his ruling specified a session window. De-identification is scoped to that one reference alone; every other passage is imported faithfully, including the author's second-person address, informal phrasing, opening line (the line beginning "Here’s the Phase 3 build specification", above these notes) and closing question.
>
> **This import does not discharge frozen rubric criteria F1 or F2** (`specs/SPEC_RUBRIC.md`). A document arriving in the repository is not a criterion clearing.
>
> **Source:** `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf` [local-only — not in this repo by design]. Extracted 2026-11-05 with `textutil -convert txt`: 111 lines / 2,350 words of plaintext, sha256 `d149bc8e11b18cd9db075dd4ad19c9ecea53b1f8e3c5460fcf583b83bc888de5`. This is a **markup conversion, not a byte copy**, and four classes of change were made. (a) *Markup characters were converted, not preserved:* the source's 17 U+2022 list bullets became markdown `-` list markers, and the source's 58 tab characters on its 29 list lines (on each, one leading indentation tab and one tab separating the bullet or number from its text) were replaced by markdown list syntax; separately, markdown heading markers were added to lines that are plain text in the source. (b) The source's 16 trailing zero-width characters (U+200B) were dropped. (c) The source's title for circuit breaker #5 was replaced, as stated above under **De-identification**. (d) Beyond (a)–(c), **no other content character was changed** in the body (the first line of this file and these notes are labelled additions, not part of the conversion): measured by normalising both texts for the markup in (a) and diffing, the two agree on all 97 non-empty content lines except the one carrying the breaker-#5 title. (The counts in (a), (b) and (d) were re-measured against the 2026-11-05 extraction.)
>
> **Added at import, 2026-11-05 — Amear's rulings that bear on how the breakers are read.** Quoted from `DECISION_LOG.md`; the quoted text is extracted from the ledger, not retyped.
>
> - Row `[2026-11-05T23:50:09Z] WHO: amear` (typed, verbatim), ruling 1: "Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest."
> - Row `[2026-11-05T23:51:21Z] WHO: amear` — this row is labelled REPORTED BY the voice agent (source: `docs/reports/2026-11-04-voice-session-notes-4.md`): R-VN4-2 breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latter." (voice agent's reading: bar-close market flatten in the backtest, resting stops once live; confirmed by Amear's typed ruling 1 at 23:50:09Z)
> - The reading "bar-close market flatten in the backtest, resting stops once live" is the voice agent's reading of R-VN4-2, not Amear's words. The ledger records it as confirmed by ruling 1 (row `2026-11-05T23:50:09Z`); ruling 1's own words speak to the backtest ("Not a resting stop in the backtest") and do not separately address the live case.
> - This note does not change any breaker's specified behaviour below, implements nothing, tests nothing, and does not resolve F1 or F2.

## Adapted Architecture: Your Server, Not a VPS

The research defaulted to a Chicago VPS. You have a local server with UPS backup, 5G failover, and n8n health monitoring already running. The architecture adapts as follows:

What changes: NinjaTrader 8 runs on your local machine instead of QuantVPS. Docker containers (n8n, PostgreSQL, Redis, Uptime Kuma) run locally. No $42/month VPS cost. No CrossTrade add-on needed if you build equivalent auto-recovery in n8n (you already have the watchdog infrastructure).

What doesn’t change: The execution path is identical. TradingView webhook → n8n → file-drop → NinjaScript → Rithmic → MFFU. The circuit breakers, the file-drop integration, the monitoring — all the same logic, different machine.

What you lose: Sub-millisecond latency to CME. What you actually lose in practice for a clock-anchored strategy that places one bracket order per session: nothing measurable. The 15–40ms from your home connection versus 0.5ms from Chicago does not affect a strategy that decides at 09:30 and enters on a stop-market order.

What you gain: Full visibility into the machine. You can physically watch it. You can open NinjaTrader and see what it’s doing. You can read the n8n logs in real time. That visibility feeds conviction. A VPS is a black box you access through Remote Desktop — when something breaks at 2:00 a.m. during an Overnight Drift trade, you’re debugging through an RDP session. On your own machine, you’re right there.

The migration option stays open. If you validate everything locally and decide production needs Chicago proximity or 24/7 uptime you can’t match — migrate later. The NinjaScript strategies, n8n workflows, and Docker containers are portable. Nothing you build locally locks you out of a VPS later.

## The Build — What Gets Built, In What Order

Everything below applies regardless of which satellite strategy you pursue. The NQ Noise-Area Breakout is the baseline. Everything else layers on top of the same infrastructure.

### Block 1: Foundation (No Subscription Required)

What you’re doing: Installing the tools, connecting the pipes, proving the signal path works end-to-end with zero money involved.

Components:

NinjaTrader 8 installation and familiarization. Free download. Connect to NinjaTrader’s sim data feed (free, no Rithmic account needed yet). Learn the interface — not to trade manually, but to understand what the automation will be controlling. You need to know what the Strategy Analyzer does, what the Control Center shows, how a strategy gets enabled/disabled, and what happens when a bracket order fills. This is the conviction education. If you can’t explain what NinjaTrader is doing when your strategy fires, you won’t trust it in live markets.

NinjaScript fundamentals. The NQ Noise-Area strategy is mechanically simple: at a fixed time, check if price has broken above or below a calculated noise band, place a stop-market entry with a bracket (stop-loss + take-profit). In NinjaScript, that’s an OnBarUpdate() method that checks the time, computes the band from the day’s range, and calls EnterLongStopMarket() or EnterShortStopMarket() with SetStopLoss() and SetProfitTarget(). Claude writes the code. You read it, understand what each block does, and can explain it back. That’s the bar.

File-drop integration prototype. This is the critical plumbing test. Build a minimal NinjaScript add-on that watches a directory (e.g., C:\Signals\Incoming\). n8n writes a JSON file to that directory. NinjaScript detects the file, reads it, logs what it found, and moves the file to C:\Signals\Processed\. No orders placed — just proving the pipe works. Then reverse it: NinjaScript writes a confirmation file to C:\Signals\Acks\, n8n detects it and logs it. Run this 100+ times. Measure how long it takes from file write to detection. The research estimated this is negligible for 30-minute decision windows, but you need to see it yourself.

n8n workflow skeleton. You already run n8n. Build the trading orchestration workflow as a skeleton: webhook receiver node → pre-trade validation node (placeholder logic) → file writer node → ack poller node → Telegram notification node. No circuit breakers yet — just the signal path. Fire test webhooks from TradingView (or manually from n8n) and confirm the full chain completes.

Milestone: You can fire a fake signal from TradingView, watch it flow through n8n, appear as a file in NinjaTrader’s watched directory, get parsed by your NinjaScript add-on, and receive a Telegram confirmation — all without touching anything manually. That’s the proof of concept. Zero subscriptions. Zero cost beyond your existing infrastructure.

### Block 2: Backtesting (Requires Rithmic Data Connection)

What you’re doing: Validating the NQ Noise-Area strategy against historical data using NinjaTrader’s Strategy Analyzer. This is where the MFFU connection becomes necessary — not for live trading, but for historical data access through Rithmic.

Decision point (pinned from your request): Historical data sourcing.

Option A — Collect forward from Rithmic. Once you connect NinjaTrader to Rithmic (via MFFU eval or sim account), NinjaTrader begins storing tick and bar data locally. This is free. The limitation: you only have data from the day you connect forward. For a strategy that needs 5+ years of walk-forward validation (252-day in-sample, 63-day out-of-sample, rolled forward), collecting forward means waiting years before you have enough data. This doesn’t work as your primary backtest source.

However — collecting forward starting now has a different purpose. It builds your untouched out-of-sample dataset. While you backtest on purchased historical data, the data you’re collecting live becomes the final validation set that was never touched during optimization. That’s methodologically valuable. Start collection as early as possible.

Option B — Purchase historical data. FirstRate Data, $75–225 one-time depending on instruments and depth. Gets you 5–10 years of 1-minute NQ bars immediately. NinjaTrader can import this directly into its historical data store and run Strategy Analyzer against it.

Option C — Both. Buy historical for backtesting. Collect forward for out-of-sample validation. This is the methodologically strongest path and costs only the one-time FirstRate purchase.

The backtest itself: NinjaTrader Strategy Analyzer with the configuration already specified in the research. Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract. Rolling walk-forward optimization: 252-day in-sample / 63-day out-of-sample / 63-day step. Four parameters optimized (lookback, noise multiplier, stop ATR multiplier, exit policy). Session window and clock times held fixed.

Pass gates (non-negotiable):

- OOS profit factor ≥ 1.30
- OOS Sharpe ≥ 1.0
- Max drawdown ≤ 4% of equity
- ≥ 250 aggregate OOS trades
- ≥ 60% of walk-forward windows profitable
- Walk-forward efficiency ≥ 0.50

If it doesn’t pass, the strategy doesn’t deploy. No partial passes. No “close enough.”

Milestone: Walk-forward validation report complete. GO / HOLD / REJECT decision made on NQ Noise-Area with your own data, on your own machine, verified by your own eyes.

### Block 3: Circuit Breakers and Safety Architecture

What you’re doing: Building the nine circuit breakers into the n8n workflow so that the system blocks violations before they reach the order engine.

The breakers (from Round 2 Agent 3):

1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
2. Max trades per day — trade count hits daily max → disable order submission
3. Consecutive loss (“two and done”) — 2 consecutive losers in one session → identical to max trades
4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
7. Max position size — order quantity exceeds plan → reject
8. Stale signal filter — signal file older than X seconds → reject (prevents acting on delayed signals after a system hiccup)
9. Heartbeat dead-man switch — if n8n hasn’t confirmed system health in 5 minutes → disable new orders

State management: Redis for real-time state checks (is the gate open or closed?), PostgreSQL for durable audit trail (every breaker trip logged with timestamp and context). Both run in Docker on your server. n8n queries Redis at the start of every workflow execution — if any gate is closed, the workflow terminates before reaching the file-write node. Default state is gate closed. The system must actively confirm safety before every order.

The deterministic fallback script. A standalone Python script that runs independently of n8n. It polls the broker API directly, checks hardcoded thresholds (daily loss, max trades, session time), and can issue flatten commands or send alerts. No LLM. No inference. Pure conditional logic. This is your safety net if n8n itself crashes.

Milestone: Every circuit breaker has been triggered intentionally at least once on sim data and verified to block order submission correctly. The fallback script has been tested independently of n8n.

### Block 4: Paper Trading (Requires MFFU Sim or Eval)

What you’re doing: Running the full system — signal generation, n8n orchestration, circuit breakers, NinjaScript execution, monitoring — on MFFU’s simulated account with live market data. No real capital.

Minimum duration: 6 weeks or 25 triggered trades, whichever comes later. Must span at least one FOMC day, one NFP day, and one NQ contract rollover.

What you’re measuring:

- Signal timing: median ≤ 2 seconds from TradingView alert to NinjaTrader file detection
- Order latency: median ≤ 250ms from NinjaTrader order submission to Rithmic fill
- Bracket placement: ≥ 99% placed within 1 second of fill
- Strategy performance vs. backtest: within ±15% win rate and ±25% average trade P&L
- System uptime: ≥ 90% of sessions fully hands-off (no manual intervention)
- Each circuit breaker triggered and verified at least once in live-data conditions

What you’re NOT measuring: P&L. The number doesn’t matter. Execution quality matters. A paper-trading period that produces losses but perfect execution is a pass. A paper-trading period that produces profits through manual overrides is a fail.

Milestone: Paper trading report complete. All execution and system reliability gates pass. The system has proven it can run without you touching it.

### Block 5: Graduated Live Deployment

What you’re doing: Moving from sim to real capital, at minimum size, with quantitative promotion gates.

|Phase     |Sizing                            |Duration                     |Promote When                                    |
|----------|----------------------------------|-----------------------------|------------------------------------------------|
|A — Micro |1 MNQ ($2/point)                  |2 weeks + 10 triggered trades|Live metrics within 1 standard error of paper   |
|B — Single|1 NQ ($20/point)                  |4 weeks + 20 triggered trades|Stats within 0.5σ of backtest median, no DD > 2%|
|C — Full  |Risk-model sizing (0.5% per trade)|Indefinite                   |—                                               |

Kill criteria — return to paper if ANY fires:

- Rolling 20-trade drawdown exceeds 1.5× backtest max OOS drawdown
- Account drawdown exceeds 60% of MFFU trailing DD room
- Rolling 20-trade profit factor < 0.5× backtest profit factor
- More than 3 manual interventions in 5 trading days
- Median latency triples vs. paper baseline

Demotion goes back to Phase A. No skipping on re-promotion.

### Block 6: Satellite Strategy Layering (Only After Block 5 Is Stable)

This is where FX Fixings, Overnight Drift, or CL EIA get added. Same sequence for each: backtest → NinjaScript build → n8n workflow → circuit breaker extension → paper trade → graduated live. Each satellite uses the same file-drop integration, same monitoring, same breaker architecture. The infrastructure you built in Blocks 1–3 is reusable — you’re adding strategies to a proven pipeline, not rebuilding.

FX Fixings requires the historical spread backtest on CME 6E/6J — this is where you may need FirstRate Data for currency futures specifically.

Overnight Drift requires 2019–2025 ES data and the 2:00 a.m. execution means your server must be running and connected at that hour. Your n8n health checks and 5G failover cover this, but verify it works reliably during overnight hours before deploying.

## Cost Summary

Proof of concept (Block 1): $0 additional. Your server, free NinjaTrader, free sim data, existing n8n.

Backtesting (Block 2): $75–225 one-time (FirstRate Data) + MFFU eval fee ($50–100) for Rithmic connection. Monthly: $12 CME data through Rithmic.

Paper trading onward (Blocks 3–5): Monthly ~$12 (CME data) + MFFU account fees ($50–200/month depending on tier). No VPS. No API costs for execution. Claude for coaching/debrief is through this interface, not a paid API integration.

Full production monthly (local server): ~$62–212/month. That’s CME data ($12) + MFFU ($50–200). Compare to the research’s VPS-based estimate of $81–340. You’re saving $42–85/month by running locally.

## What You Should Start Now

While you’re still in the education phase:

1. Install NinjaTrader 8. Connect to the free sim. Click around. Understand what the Strategy Analyzer is, what a strategy looks like when it’s enabled, what the Control Center shows during execution.
2. Start the file-drop prototype. This is the single most important plumbing test. If this works reliably, the entire execution architecture holds. If it doesn’t, you find out before spending anything.
3. (Pinned) If you decide to pursue backtesting soon, consider connecting to Rithmic early — even through a free NinjaTrader sim/demo Rithmic connection if available — and letting it collect tick data in the background. Every day of data you collect now is a day you don’t need to buy later for out-of-sample validation. This doesn’t replace purchasing historical data for the primary backtest, but it builds the untouched forward dataset that makes your validation methodologically stronger.

## What This Document Does Not Include (And Why)

Timelines with dates. You named it: the education component means you don’t know how long each block takes. Milestones, not deadlines. When Block 1’s milestone is hit, Block 2 starts. Not before.

Satellite strategy specifications. FX Fixings, Overnight Drift, and CL EIA each need their own NinjaScript spec and backtest configuration. Those get scoped after Block 5 proves the baseline is stable. Building three strategies in parallel before one is validated is the kind of scattered execution that feeds the pattern.

The Praxis coaching integration. The EQS scoring, debrief automation, and behavioral pattern detection described in the research are Phase 4 features. They layer onto a working system. They don’t block the build.

One strategy. One instrument. One build path. Prove it works. Then expand.

What questions do you have before we close this session’s scope?

## Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)

> ***Added 2026-11-12; not part of the source document.*** This section amends the imported breaker list. It is not part of the import and is not the source author's text; the import notes at the top of this file describe the imported body only.

**Authority.** `DECISIONS.md` entry D-2026-11-12-A (DECISIONS.md:2205), decided by master under D-2026-11-08-D D1, changeable by Amear; DECISION_LOG row 2026-11-12T05:29:00Z (WHO: praxis-master). Rule F2-1 was approved by Amear in the words of a summary (D-2026-11-11-A, V2, DECISIONS.md:2108); the #4/#5 text below is the master's adoption of the F2 proposal's replacement text (`docs/specs/2026-11-10-f2-session-flat-proposal.md`:36, :38), not Amear's words.

**Level.** Unchanged: the nine breakers, #4 and #5 included, are SPECIFIED ONLY — zero implemented, zero tested, zero tested under failure. This amendment changes specified text, nothing else.

**How the text was carried.** Each quoted line below is copied by script, byte-identical to the cited line, including the `> ` marker at the start of the proposal's lines :36 and :38. No adaptation was made. The imported body is not rewritten: lines :100 and :101 above stay as imported, no line of the body is changed and no pointer line is added, so the body's line numbers stay as other documents cite them.

### Governing rule (Rule F2-1)

Copied by script from `docs/specs/2026-11-10-f2-session-flat-proposal.md`:20:

```text
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
```

### Breaker #4 — amended

Amended text, copied by script from the proposal :36:

> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.

Supersedes the imported line :100, quoted verbatim:

```text
4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
```

### Breaker #5 — amended

Amended text, copied by script from the proposal :38:

> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.

Supersedes the imported line :101, quoted verbatim:

```text
5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
```

De-identification (import note, top of this file) is unchanged: the amended name "Session window (operator lockout)" is the F2 proposal's wording; the source document's title for breaker #5 is not reproduced.

### What happens to an open position at 15:00

Copied by script from the proposal :30:

```text
**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
```

### Not changed by this amendment

Breakers #1, #2, #3, #6, #7, #8 and #9 and their values; the Block 3 state management, fallback script and milestone text; Blocks 1, 2, 4 and 5. Where #4 and #5 sit on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3, which this amendment does not edit.
