# B2-Q1 — Strategy Identity & Exportability Assessment

**Project:** PRAXIS | **Date:** 2026-07-15 | **Bead:** Praxis_build-9sl (b2-q1)
**Answers:** Block-2 spec-gap **Q1** in `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md` §5
**Status:** Findings + **proposed** Q1 answer — final lock is trader-only (see Trader-Confirmation Gaps)

> **Q1 (the Block-2 hard blocker):** "What exactly is the strategy under test? Is the TradingView strategy exportable as a historical signal series, or must the entry logic be re-implemented in NT8/Python for backtesting?" This determines the entire Block-2 toolchain (NT8 Strategy Analyzer vs external Python engine vs signal-replay harness).

---

## 1. Strategy identity

**The strategy under test is the Zarattini–Aziz–Barbon "Noise-Area" Intraday Momentum Breakout on NQ.**

- Named verbatim as the baseline: *"Zarattini–Aziz–Barbon Noise-Area Intraday Momentum Breakout on NQ (09:30–11:30 ET, Sharpe ~1.67, 38% WR, 2.25 payoff)"* — `Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md` (header, line 6). Reconfirmed as the anchor: *"the Zarattini NQ Noise-Area Breakout"* (line 165) and *"NQ Noise-Area Breakout (baseline)"* in the session map (line 106).
- The Phase 3 Build Spec fixes it as the one strategy for Blocks 1–5: *"The NQ Noise-Area Breakout is the baseline. Everything else layers on top of the same infrastructure."* — `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf`, "The Build" section.
- **Mechanical description** (Phase 3 spec, Block 1): *"at a fixed time, check if price has broken above or below a calculated noise band, place a stop-market entry with a bracket (stop-loss + take-profit)… an `OnBarUpdate()` method that checks the time, computes the band from the day's range, and calls `EnterLongStopMarket()` or `EnterShortStopMarket()` with `SetStopLoss()` and `SetProfitTarget()`."* It is **clock-anchored, fully rules-based, deterministic** — one bracket order per session, decision at 09:30 ET, session close/flatten by 11:30 ET.
- **The four optimizable parameters** (Phase 3 spec, Block 2): *lookback, noise multiplier, stop ATR multiplier, exit policy.* "Session window and clock times held fixed." This is the canonical parameter set the walk-forward optimizes.

**Companion / satellite strategies (NOT under test in Block 2).** The portfolio adds uncorrelated satellites *after* Block 5 proves the baseline (Phase 3 spec, Block 6): **FX Fixings** (6E/6J, London/NY fix), **Overnight Drift** (`OvernightDrift.cs` — clock entry on ES at 02:00 ET, ATR-trailing runner, hard time-stop 09:25 ET; Compiled_Round_3 line 218), and **CL/NG EIA** announcement plays. The spec is explicit — *"One strategy. One instrument. One build path."* — so Block 2 scope is **NQ Noise-Area only**; the satellites each get their own backtest in Block 6.

## 2. Where the entry logic actually lives right now

**Nowhere as executable source in this repo — and specifically NOT as TradingView Pine.**

- **No Pine Script exists in-repo.** A repo-wide grep for `//@version`, `pinescript`, `strategy.entry`, `strategy.exit`, and `*.pine` / `*noise*` / `*breakout*` source files returned **zero** strategy sources. There is no Pine `strategy` object, no bar-replay alert log, no historical signal export anywhere in the tree.
- **The canonical definition of the entry logic is the academic strategy (Zarattini/Aziz/Barbon paper) plus the Phase 3 spec's parameterization** — not any code artifact the trader currently holds.
- **The live signal path does not carry strategy internals.** The n8n webhook (`workflows/EmMbN4sslwIx1ydn*.json`) validates a payload of exactly `{symbol, side, qty, price, signal_id, ts}` with `side ∈ {BUY, SELL}`. That is a bare directional order instruction — it contains no noise-band value, no lookback state, no decision rationale. So even a captured stream of live/sim TradingView alerts would give a *signal series* but not a *backtestable strategy*, and only forward-collected, sparse (one/session), and cost-blind.
- **Architectural note / genuine ambiguity:** The documented signal flow is TradingView → n8n → NT8, which *implies* TradingView (Pine) is the signal generator. But the Phase 3 spec describes the strategy AS a NinjaScript `OnBarUpdate()` the build will write ("Claude writes the code. You read it… That's the bar."). These are in tension: it is unclear whether a TradingView Pine strategy is intended to exist at all, or whether the strategy is computed in NT8 and TradingView is a passthrough/manual-alert convenience. **For backtesting this ambiguity does not change the answer** (Strategy Analyzer needs the logic in NinjaScript either way), but it is a real trader gap (see §5).

## 3. Exportability paths — evidence-based assessment

### (a) Export the TradingView strategy's historical signal series — NOT VIABLE
- **Precondition fails:** there is no Pine `strategy`/`indicator` source in the repo, and no evidence the trader has authored one. The Compiled_Round_3 automation filter even lists the strategy as *"Fully codifiable in NinjaScript or Pine+n8n"* (line 23) — i.e. Pine is a hypothetical implementation target, not an existing asset.
- **Even if Pine source existed:** TradingView's exportable history is limited — bar-based (not tick-fill) signals, "List of Trades" export capped by plan-tier bar limits, no true tick fill-resolution, and no control over the continuous-contract roll. This cannot satisfy the Phase 3 backtest config below.
- **Live-alert capture** yields at most a sparse forward signal series (one signal/session, no historical depth, no fill/cost model) — useful later for SHM-4 reconciliation, useless as the backtest engine.

### (b) Re-implement entry logic in NT8 (Strategy Analyzer) — VIABLE & SPEC-MANDATED
- **The Phase 3 spec already prescribes exactly this.** Block 2 verbatim: *"Validating the NQ Noise-Area strategy against historical data using **NinjaTrader's Strategy Analyzer**."* It pins the full config: *"Order Fill Resolution = High, 1-tick resolution series, 1-tick slippage on entries, $2.96 round-trip commission per NQ contract. Rolling walk-forward optimization: 252-day in-sample / 63-day out-of-sample / 63-day step. Four parameters optimized (lookback, noise multiplier, stop ATR multiplier, exit policy)."*
- **The strategy is trivially re-implementable:** the spec itself gives the NinjaScript skeleton (`OnBarUpdate()` time-check → compute band → `EnterLongStopMarket`/`EnterShortStopMarket` + `SetStopLoss`/`SetProfitTarget`). It is a handful of deterministic rules, not a discretionary or ML setup.
- **NinjaScript is required regardless**, because the *live executor* is already a NinjaScript strategy/add-on (B1-f consumer, STATUS.md). Re-implementing for backtest reuses the same platform the live order path runs on — the tightest possible backtest-to-live fidelity, and it directly feeds the SHM-4 live-vs-backtest baseline.
- **Data path is already scoped** (Phase 3 spec Block 2 Option C): FirstRate Data 1-min history for the walk-forward + forward-collected Rithmic tick for untouched OOS.

### (c) Re-implement in Python / signal-replay harness — VIABLE but NOT PREFERRED for Block 2
- Technically easy (deterministic rules), and a Python engine gives more flexible Monte Carlo / walk-forward tooling.
- **But** it duplicates the strategy logic in a second language (drift risk vs the live NinjaScript executor), needs its own NQ data ingest + roll handling + a hand-built fill model, and diverges from the spec's Strategy-Analyzer mandate and its six pass-gate definitions. Best reserved as an *optional cross-check* for the Monte Carlo layer (§2 of the scope proposal), consuming the Strategy Analyzer's exported OOS trade list — not as the primary engine.

## 4. RECOMMENDED Q1 answer + resulting toolchain

**RECOMMENDED ANSWER (path b): The strategy is NOT exported from TradingView. It is re-implemented as a NinjaScript strategy and backtested in NinjaTrader 8 Strategy Analyzer.** There is no Pine source to export, the live TradingView payload carries no strategy internals, and the Phase 3 Build Spec already mandates Strategy Analyzer with a fully-pinned walk-forward config and six pass gates. The strategy's rules are simple and deterministic (clock-anchored noise-band breakout), so re-implementation is low-risk, and it reuses the exact NinjaScript platform the live order path runs on.

**Resulting Block-2 toolchain:**
- **Primary engine:** NT8 Strategy Analyzer — rolling walk-forward 252 IS / 63 OOS / 63 step; High fill resolution, 1-tick series, 1-tick entry slippage, $2.96 RT commission; optimize {lookback, noise mult, stop-ATR mult, exit policy}, hold session/clock fixed.
- **Data:** FirstRate Data 1-min NQ (deep history) for the WFA matrix + forward-collected Rithmic tick for untouched OOS / SHM-4 baseline (Phase 3 Block 2 Option C).
- **Monte Carlo (scope proposal §2):** run on the Strategy Analyzer's exported pooled-OOS trade list — Python is fine *here* as a downstream analytics layer, not as the entry-signal engine.
- **Live signal capture:** retain forward TradingView/sim alerts only for SHM-4 live-vs-backtest reconciliation, not for the backtest itself.
- **Consequence for the scope proposal:** the §1.3 "open dependency" and execution-sketch bead **b2-signal-repro** collapse to "port the NinjaScript logic into a Strategy-Analyzer-runnable strategy and reconcile a sample of its bars against known live alerts" — no external-export or signal-replay-harness toolchain is needed.

**Confidence:** High that path (b) is correct; the spec is unambiguous and no competing artifact exists. Residual uncertainty is entirely in the trader-only facts below.

## 5. Trader-confirmation gaps (what still blocks a final lock)

- **Does a TradingView Pine strategy exist at all, and does the trader own its source?** (None found in-repo. If one exists off-repo, it still isn't the backtest engine, but it would need to be reconciled against the NinjaScript re-implementation.)
- **Is TradingView the intended signal *generator* or just a passthrough/manual-alert layer?** Resolves the §2 architecture tension (TradingView→n8n→NT8 vs strategy-computed-in-NT8).
- **Is the strategy the Zarattini/Aziz/Barbon paper's exact ruleset, or a trader-modified variant?** Which paper edition / band definition is canonical, and what are the parameter search ranges for {lookback, noise mult, stop-ATR mult, exit policy}?
- **Exit-policy definition:** it is listed as an optimizable *parameter* but its concrete form (fixed target vs trailing vs 11:30 time-stop, or a choice among these) must be pinned before implementation.
- **Q7 dependency — optimization vs validation-only:** does Block 2 optimize the four parameters (IS = fit) or validate fixed trader-chosen parameters (IS = measure)? Changes whether "re-implement" also means "re-optimize."
- **TradingView plan tier** — only relevant if the trader wants any TradingView-side cross-check; irrelevant to the recommended NT8 path.

## 6. Sources read

- `docs/specs/2026-07-15-block2-backtesting-scope-proposal.md` (§1.1, §1.3, §5 Q1, §6)
- `Redemtion/Intitialization-April 2026/Phase 3 build specification.rtf` — **primary**: Block 1 (strategy mechanics/NinjaScript), Block 2 (Strategy Analyzer config, WFA, pass gates), Block 6 (satellites)
- `Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md` — strategy identity (Zarattini–Aziz–Barbon), ranking matrix, session map, satellite `.cs` names
- `Redemtion/Intitialization-April 2026/PRAXIS_PHASE_3_OUTPUT_SUMMARY.md` — Block 2 recap, six pass gates, data-sourcing Option C
- `Redemtion/Intitialization-April 2026/Phase 2 Closure & Phase 3 Scope Definition.rtf` — Phase 2→3 handoff context
- `workflows/EmMbN4sslwIx1ydn.before-b1-b.json` — live signal payload schema `{symbol, side, qty, price, signal_id, ts}`
- Repo-wide grep (ninjascript/docs/workflows): confirmed **no Pine Script / no strategy source** present
- STATUS.md — B1-f NinjaScript consumer is the live executor (backtest-to-live platform continuity)
