> **UNGRADED RESEARCH INPUT — NOT A RUBRIC ARTIFACT.**
> Produced by a browser-based research agent outside the praxis
> producer/auditor chain. It has NOT been graded against SPEC_RUBRIC.md.
> It does NOT discharge frozen criterion F3 and must not be cited as a
> finding. It is input to a decision that belongs to Amear.

# Backtest Fill-Modelling Fidelity for a Clock-Anchored NQ "Noise Area" Breakout

**Provenance.** Commissioned by praxis-master in session 43 (2026-08-07) after
`Agent(general-purpose)` was denied by `projectSettings` and the praxis agent
types were found to hold no web tools. Executed via browser. Retained verbatim
below, followed by a **master's addendum** recording what was subsequently
verified against this repository — which materially changes how several of these
findings apply.

**Scope.** Informs, does not decide, the A / A+ / B / C choice on data resolution
for a NinjaTrader 8 Strategy Analyzer backtest of the Zarattini–Aziz–Barbon
"Noise Area" breakout (SSRN 4824172) on NQ futures. Every claim is labelled by
source class — vendor documentation / working paper / practitioner consensus /
own inference — and by confidence.

---

## TL;DR (as returned)

- **The spec is internally contradictory.** NT8's "Order Fill Resolution = High"
  is documented (vendor) to require a more-granular secondary series — the most
  granular being 1-tick — and with only 1-minute data present it cannot fill on
  anything finer than the 1-minute bar. "High" does not manufacture intrabar
  precision from 1-minute data.
- **A vendor-documented OHLC fill algorithm *infers* intrabar order-of-events**
  from whether the bar "moved up or down first"; an independent NQ working paper
  finds 18.47% of 1-minute bars are ambiguous for a 10pt/10pt bracket, with a
  best-vs-worst-case span of 3,695 NQ points ($73,900) per 1,000 trades.
- **The paper being replicated used 1-minute OHLC data plus explicit costs, not
  tick data** — so a 1-minute run is faithful to the source on data resolution,
  but the source's per-share ETF cost model does not transfer to NQ.

---

## Area 1 — NT8 mechanics (Order Fill Resolution = High)

**Confidence: HIGH (vendor documentation and official-forum staff answers opened directly).**

- Standard (Fastest) fill resolution uses the *same* OHLC of the series the
  strategy runs on. "High" attaches a **secondary, more-granular bar series**
  used *only* for order-fill pricing; the most granular selectable is 1-tick.
  NT staff, official forum, verbatim: *"Selecting order fill resolution of 'High'
  will allow you to set a secondary bar series to be used as the price data to
  fill your orders… you may have a strategy that you run on 'Daily' bars but then
  want to bring in 'Minute' bars for the historical fill algorithm to be based on."*
- **Critical requirement:** High fetches that granular series from the data
  provider. NT staff: *"using the high order fill resolution set to 1 tick will
  send a request to your data provider for 1-tick data."* With no tick data, the
  finest fill series available is 1-minute.
- **High is single-series only.** Any `AddDataSeries` call causes rejection:
  *"'High' order fill resolution is only available for single-series strategies."*
- **High is mutually exclusive with Tick Replay.** The vendor states Tick Replay
  *"was NOT designed to provide accuracy in backtesting concerning order fills
  and execution."*
- **Fallback behaviour when High is set but tick data is absent — UNVERIFIED.**
  No clean vendor sentence found for that precise configuration. Best-supported
  **own inference**: a single-series strategy set to High will fill against the
  1-minute series; it does not fabricate sub-minute fills. Whether the platform
  warns or silently coarsens is unconfirmed.
- **Intrabar order-of-events — documented assumption, not observation.** The
  official "Historical Order Backfill Logic" page states the algorithm first
  *"Determine[s] whether the current bar's first move was upward or downward,"*
  then takes **three passes** approximating O→H→L→C or O→L→H→C, using temporary
  "next high price"/"next low price" variables *"used to approximate the price
  that would be hit on the next tick."* From OHLC alone it is **inferring** first-move
  direction, not observing it. There is no vendor-supported way, on 1-minute bars,
  to know the true high-before-low sequence.

---

## Area 2 — Measured magnitude of tick-vs-minute divergence

**Confidence: MEDIUM-HIGH for the NQ-specific study (abstract-level); MEDIUM for corroboration.**

**Claeys, "When Backtests Guess: How Trading Platforms Silently Fabricate
Results," SSRN 6240638.** Abstract confirmed verbatim; **full text inaccessible
(SSRN rate-limited) — abstract-level only:**
- **2,064,460 one-minute NQ bars, 2020–2025**; for a 10-point stop / 10-point
  target scalp, **18.47% of all bars are "ambiguous"** (both stop and target fall
  inside the same bar).
- **Best-case vs worst-case intrabar-ordering gap: 3,695 NQ points = $73,900 per
  1,000 trades** ($20/pt × 3,695 — internally consistent).
- Five major platforms compared; *"each one uses a different method, none of which
  is provably correct without tick data."*
- **UNVERIFIED:** how the ambiguity fraction scales with bracket width.

**Mesfin, "Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures"
(arXiv 2605.04004)** — full text retrieved, **5-minute MNQ, not 1-minute NQ:**
- Across 14 OHLCV signal families on **72,604 five-minute MNQ RTH bars
  (Dec 2021–Aug 2025)**, gross edge ceiling ~0.07–1.50 points/trade, below a
  ~2.0-point (~$4/micro) friction floor — every single-bar signal family failed
  net of costs.
- Only strategies **holding 12–15 bars (60–75 min)** cleared friction.
- Author on execution: *"Every signal fires at bar close. Every entry executes at
  the open of the next bar… it eliminates the common backtest error of pretending
  you can fill at prices you saw before the bar closed."*
- Treat as **directional corroboration, not a transferable number.**

**Platform-behaviour corroboration (practitioner + vendor):** NT users report
large Standard-vs-High deltas — one reported High yielding ~55% of Standard net
profit on a breakout with a 10-tick stop on a 15-minute chart. NT staff: *"These
differences will add up. The more trades, the larger the difference."*

**No credible source found** for a peer-reviewed tick-vs-minute Sharpe delta for
this exact strategy on NQ.

---

## Area 3 — Realised slippage at breakout moments on NQ

**Confidence: MEDIUM (practitioner consensus; no single authoritative dataset).**

- **Quiet RTH:** consensus **0–1 tick** for 1–2 lot NQ market/stop orders.
  Optimus Futures: *"In highly liquid markets like ES or NQ during active hours,
  expect 0-1 tick of slippage for small orders."*
- **Breakout / momentum-ignition moments:** resting liquidity is *pulled*, stop
  clusters fire market orders into a thinning book, price "skips" ticks. During
  CPI/FOMC/NFP, *"can explode to 5–20 ticks."*
- **Highest-value datapoint — the source authors' own disclosure.** The
  Concretum/Zarattini team (QuantConnect thread) contrast their 30-minute-interval
  momentum, where *"slippage is generally less of a concern,"* with *"pure breakout
  strategies, where assuming execution at the exact breakout level may be overly
  optimistic."* They disclosed real Interactive Brokers slippage of **$0.005/share
  versus the $0.001/share assumed in the paper — 5× the modelled figure** — live-testing
  a similar intraday momentum strategy on SPY.

---

## Area 4 — What the source paper (SSRN 4824172) assumed

**Confidence: HIGH (abstract + Swiss Finance Institute listing + independent summaries).**

- **Instrument/data:** SPY ETF (not futures), **1-minute OHLC** for SPY and VIX,
  **May 2007–April 2024**. The source used **minute resolution, not tick data.**
- **Signal:** noise boundaries = daily open × (1 ± average intraday return to that
  minute over prior 14 days), gap-adjusted. **Trades evaluated only at each clock
  hour/half-hour (HH:00 / HH:30)** — semi-hourly, NOT continuous tick-by-tick.
  Exit on opposite boundary or VWAP trailing stop; flat at 16:00 ET.
- **Costs:** commissions **$0.0035/share** (IBKR Pro Tiered top rate) **plus
  $0.001/share slippage.** Headline net result: **total return 1,985%, annualized
  ~19.6%, Sharpe 1.33.**
- **Execution timing:** semi-hourly evaluation means the paper is **not** a pure
  instantaneous-touch breakout. It never claimed instantaneous band-touch fills.
- **Independent futures replication (Quantitativo, Databento minute data):**
  $0.85/contract commission + $1.40/contract fees + **0.5 tick/trade slippage**;
  for NQ (14-day lookback, target-vol variant) *"Sharpe ratio achieves 1.67 vs.
  0.93 NQ long only; Max drawdown is at 24% vs. 35%… expected return per trade is
  +6 bps, with a win ratio of 38% and a payoff ratio of 2.25."* Same author warns:
  *"slippage assumptions cause a significant impact… I don't think it's realistic
  to assume less than 0.5 tick/trade, which is already optimistic."*

---

## Area 5 — Standard remedies and what counts as defensible

**Confidence: MEDIUM-HIGH (practitioner consensus + one academic WFE convention).**

- **Slippage sensitivity sweep (Option A+):** established and cheap. Convention is
  to re-price the whole trade record at rising cost levels and report a **"cushion"** —
  the multiple of assumed cost the edge absorbs before disappearing; a
  representative codification warns when the cushion is below ~3×. **What it
  proves:** only that *average* per-trade cost up to N ticks leaves expectancy
  positive. It does **not** prove fills happened at modelled prices, does not
  capture *when* slippage clusters, and does not fix intrabar ordering.
- **Pessimistic intrabar ordering:** NT8 exposes conservative/liberal fill options.
  Running **both** best- and worst-case ordering **brackets** the true result; the
  width of that bracket directly measures how much the 1-minute data is guessing
  for your trade set. Cheapest high-value diagnostic on existing data.
- **Option C (measured haircut from a tick sample):** recognised *in spirit*
  (implementation-shortfall reconciliation) but **no established, named standard**
  for the buy-a-sample-and-extrapolate procedure. A defensible engineering
  improvisation, not a codified method. **No authoritative haircut magnitude found.**
  Extrapolating one overlap window assumes divergence is stationary across regimes —
  it is not.
- **WFE ≥ 0.50 context.** Per **Robert Pardo, *The Evaluation and Optimization of
  Trading Strategies* (2008)**: *"WFE > 0.5 — Suggests robustness"*, 0.5–0.7 the
  realistic target, *"WFE < 0.3 — Red flag."* **Own inference:** systematically
  optimistic fills inflate *both* IS and OOS legs, so WFE (a ratio) can look healthy
  while both legs are biased upward. **A WFE pass does not certify fill realism.**
  The two concerns are orthogonal.

---

## Area 6 — The honest counter-case

**Confidence: MEDIUM.**

The concern is **real but not automatically decisive.**

- **The paper itself used 1-minute data and semi-hourly entries.** If the
  replication matches that design, minute resolution is the *faithful* choice, and
  buying tick data would test a *different* system than the one published.
- **Errors partially wash out over large samples** — *provided* the strategy is not
  systematically picking the ambiguous side.
- **Conditions under which minute resolution is adequate:** (1) entries at discrete
  clock anchors, not instantaneous touches; (2) bracket wide relative to a 1-minute
  bar's range, so same-bar ambiguity is rare (Claeys' 18.47% was for a *tight*
  10pt/10pt scalp); (3) holding period spans many bars; (4) the edge survives
  realistic slippage sweeps with comfortable cushion.
- **Counter to the counter (own inference):** "reverse-and-re-enter on opposite-band
  cross" is the aggressive behaviour that maximises same-bar ambiguity — *if* it
  fires intrabar. Answerable empirically from the 1-minute run itself.

---

## What this does and does not settle (as returned)

**Settles:** (1) On 1-minute-only data, "High + 1-tick" cannot run as written.
(2) NT8 **infers** intrabar ordering from OHLC; not fixable without finer data.
(3) The source paper used 1-minute data, semi-hourly entries, per-share ETF costs.
(4) Fill/slippage error is largest at breakout entries; the paper's own authors
observed 5× their assumed slippage live.

**Does not settle:** (1) Exact NT8 behaviour with High and no tick data.
(2) A strategy-specific tick-vs-minute delta for this system on NQ.
(3) A credible haircut magnitude for Option C.
(4) Whether the concern is decisive for *this* parameterisation.

---

## Caveats (as returned)

- The Claeys NQ paper is **abstract-level only**; bracket-width scaling unconfirmed.
- Mesfin is **5-minute MNQ**, directional only. Both are **non-peer-reviewed working papers**.
- SSRN 4824172 is a **working paper** (Swiss Finance Institute), authors affiliated
  with commercial trading/education firms; independent reviewers flag results as
  *"a bit too good to be true"*.
- Area 3 slippage figures are **practitioner consensus**; the one hard disclosure
  ($0.005 vs $0.001/share) is **SPY, not NQ futures**.
- NT8 fallback behaviour (Area 1) is **UNVERIFIED**.

### Sources opened

- https://ninjatrader.com/support/helpguides/nt8/historical_order_backfill_logic.htm
- https://ninjatrader.com/support/helpGuides/nt8/backtesting_ninjascript_strate.htm
- https://forum.ninjatrader.com/forum/ninjatrader-8/strategy-development/110064-high-fill-resolution
- https://forum.ninjatrader.com/forum/ninjatrader-8/strategy-development/1056413-historical-fill-processing-in-nt8
- https://forum.ninjatrader.com/forum/ninjatrader-8/strategy-development/107490-using-the-high-order-fill-resolution
- https://forum.ninjatrader.com/forum/ninjatrader-8/strategy-development/1153892-reliability-of-backtesting-in-nt8
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6240638
- https://arxiv.org/pdf/2605.04004
- https://www.cxoadvisory.com/momentum-investing/complex-intraday-time-series-momentum-strategy-applied-to-spy/
- https://www.quantitativo.com/p/intraday-momentum-for-es-and-nq
- https://www.quantconnect.com/forum/discussion/17091/beat-the-market-an-effective-intraday-momentum-strategy-for-s-amp-p500-etf-spy/
- https://quantmacro.substack.com/p/paper-review-an-effective-intraday
- https://quantifiedstrategies.substack.com/p/systematic-intraday-trend-following
- https://learn.optimusfutures.com/price-impact-analysis
- https://www.elitetrader.com/et/threads/what-is-the-slippage-for-nq-stop-market-orders-during-non-spike-trading-hours.385991/
- https://grizzlyparrottrading.com/futures-basics/how-slippage-works.html
- https://futures.aeromir.com/post/111/ninjatrader-backtesting-explained-which-method-should-you-trust
- https://www.mql5.com/en/articles/23299
- https://www.tradingview.com/chart/ES1!/2LJFMp8Z-Walk-Forward-Testing-and-Out-of-Sample-Validation/

---

# MASTER'S ADDENDUM — repository verification, 2026-08-07

**This addendum is also UNGRADED.** It records facts the master verified against
this repository in session 43, because they change how the research above applies.
It has not been through the auditor.

## The hinge question the research named — answered from the repo

The research identified the decisive variable: *does this implementation fire at
the paper's semi-hourly stamp, or at a continuous tick touch?* Verified:

**`docs/specs/2026-07-16-b2-noise-area-ruleset.md:36`** — *"**Entry condition:** at
a **semi-hourly checkpoint only** — `HH:00` and `HH:30` … Checking only at the
half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes."*
Line 59: stops *"Evaluated only at semi-hourly stamps."*

**`ninjascript/PraxisNoiseAreaBreakout.cs`** (tracked, 312 lines):
- `:105` — `Calculate = Calculate.OnBarClose;`
- `:196` — `bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && …`
- `:200` — `double price = Close[0];  // the checkpoint stamp price (spec §2: evaluate at the stamp, not intrabar)`
- `:227`/`:229` — `EnterLong(Contracts, "L")` / `EnterShort(Contracts, "S")` —
  **plain market orders, not `EnterLongStopMarket`**
- `:132-134` — warns if the series is not 1-minute

## What this changes

1. **The intrabar-ordering problem is structurally absent.** Claeys' 18.47%
   ambiguous-bar figure concerns a resting stop-and-target bracket inside a bar.
   This strategy has **no resting intrabar bracket** — entries *and* exits are
   evaluated only at 30-minute stamps. **That figure does not transfer.**
2. **Order Fill Resolution = High is irrelevant here**, for a stronger reason than
   Area 1 gives: there are no intrabar fills to resolve at all. The spec's
   "High + 1-tick" line is cosmetic for this strategy.
3. **1-minute data is faithful to the paper on both axes** — resolution *and*
   entry cadence.
4. **The one trap the spec anticipated was avoided.** `…ruleset.md:99` warned that
   a `StopMarket` realisation *"can fill mid-bar and diverge slightly; reconcile in
   b2-signal-repro."* The implementation did not use stop-market orders.
5. **Options B and C would purchase tick data to resolve an intrabar risk this
   strategy does not carry.**

## What survives

- Slippage on market orders submitted `OnBarClose` at a stamp is real; they fill at
  the next bar's open. Not breakout adverse selection — the order is not triggered
  by a touch — but not free.
- The source authors' **5× live-vs-modelled slippage** disclosure stands as the
  strongest cautionary number.
- The independent NQ replication used **0.5 tick/trade** and called that *"already
  optimistic."* This project's spec assumes **1 tick** — more conservative than the
  replication that reported Sharpe 1.67.
- **F3 remains unmet.** Its criterion demands the fill resolution and the slippage
  assumption *"stated in writing before the backtest runs."* That statement does not
  yet exist.

## Master's recommendation (not a ruling)

**A+ with no data purchase**, plus one control experiment: run the backtest twice,
identical in all respects, **Standard vs High** fill resolution. Under checkpoint-only
evaluation the results should be identical. Per rubric ruling **R3**, that is the
correct form of proof — toggle the mechanism, hold everything else constant, and
show whether behaviour changes. If it does not, fill resolution is *proven*
irrelevant here rather than argued irrelevant, and F3 reduces to a written slippage
assumption.

**Two gates on that experiment, both Amear's:** it touches FROZEN criterion F3
(which blocks `4uu`), and it requires the Parallels Win11 VM running NT8 — outside
any subagent's reach.

## Correction recorded

The master initially characterised this strategy to Amear as one whose *"edge is
defined at the instant of a band touch,"* making 1-minute bars close to
disqualifying. **That was wrong.** It was constructed from a general description of
a band-cross entry without reading the spec or the implementation, both of which
say the opposite. Recorded here rather than silently corrected, per this project's
standing practice.
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
