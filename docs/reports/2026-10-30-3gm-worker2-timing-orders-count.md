# 3gm worker 2: bar timing, order types, run-1 vs run-2 trade count (D2, D3, D4)

> **Post-adversarial status (2026-10-30, manager-adjudicated).** The adversarial review `docs/reports/2026-10-30-3gm-worker4-adversarial-d2d4.md` (VERDICT: FAIL on F1, F2) corrected two evidence labels and added scenarios and hypotheses. Where the body and the "Post-adversarial corrections" section at the end differ, the corrections section is authoritative.

## Task
Unit `Praxis_build-3gm`, worker 2. Deliverables: D2 (end-stamped bars vs the author's assumption), D3 (order-type inventory and slippage formula), D4 (why run 1 had 48 trades and run 2 had 41). This is read-only analysis of `ninjascript/PraxisNoiseAreaBreakout.cs`. No repo file was modified. This report is the only file written in the repo.

## Mode
BUILD (read-only analysis, one output file). Nothing staged: the brief forbids `git add`.

## Criterion
As stated in the dispatch brief for D2/D3/D4. The brief did not give a `specs/SPEC_RUBRIC.md` line number, and I did not look one up: **NOT CHECKED**.

## Label key
- **OBSERVED**: read by me in this session from a file or command output pasted below.
- **REPORTED BY AMEAR**: from `docs/reports/2026-10-28-voice-session-notes.md`. No Claude saw the screenshots.
- **INFERRED**: my reasoning, or NT8 runtime behaviour that no file on disk records as observed.
- **CANNOT-DETERMINE-STATICALLY**: needs an NT8 readback, which I name.

## Process log
1. Hashed and dumped the strategy file (`shasum`, `wc`, `cat -n`). The hash matches the brief, so I proceeded.
2. Captured the voice notes (lines 22–44), the reference-doc TODO line 156, and DECISION_LOG line 353.
3. Ran the order-call grep, the null-search with a positive control, a docs/ grep for NT8 runtime semantics, and a docs/ grep for point value.
4. Extracted the per-mechanism `sed -n` ranges and the spec lines, enumerated the checkpoints, and did the cost arithmetic with python3 and bc.
5. Wrote this report. The evidence is embedded with `cat` from scratch files in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w2/`.

## Verification evidence: inputs

### Strategy file hash (OBSERVED: matches the brief's 35393823…2752265, 312 lines)
```
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
$ wc -l ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
```

### Amear's VM results (REPORTED BY AMEAR, verbatim)
```
$ sed -n '22,44p' docs/reports/2026-10-28-voice-session-notes.md
## 2026-10-30 — Bar-time check (NT8 read by Amear; file read by Claude)
- NT8 on Fusion, NQCONT 1-minute, 2026-07-17, RTH template. Amear read the 9:31 bar Open as **28605.25** and the 9:32 bar Open as **28644.25**. No 9:30 bar is shown: the 16:00 bar is followed by 9:31.
- Import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` has `20260717 093100;28605.25;…;4963` and `20260717 093200;28644.25;…`. **NT8 matches the file bar for bar. There is no hour shift and no minute shift.**
- Source convention: the file is **end-stamped**. It has 1,302 `17:00:00` rows and 1,354 `18:01:00` rows, but only one `18:00:00` row. The opening-minute volume (4,963) sits on the 09:31 row. That is the same convention NT8 uses. So the `09:30:00` row (Open 28608.75) is the 9:29–9:30 pre-open minute, and the RTH template is right to exclude it.
- **The old expectation that "09:30 Open 28608.75 is the first RTH bar"** (session-52 walkthrough v2 `:219`, 4uu brief) **assumed start-stamped bars and was wrong.** The true first RTH bar is NT8's 9:31, Open 28605.25.
- Bar times: **PASS.**

## 2026-10-30 — Strategy installed, compiled, first backtests (all reported by Amear by voice; Claude saw no screenshots)
- The NinjaScript Editor on Fusion listed **only the sample strategies**. PraxisNoiseAreaBreakout was not installed (fresh install).
- `ninjascript/PraxisNoiseAreaBreakout.cs` was copied from Praxis.build (sha256 `35393823…2752265`, which equals the b2-data copy and commit `719ab11`) to the VM desktop, then into `Documents\NinjaTrader 8\bin\Custom\Strategies\`. **F5 compile: clean.** It showed the progress animation and no errors, and the strategy now appears in the list. The hash was not recomputed inside the VM.
- **Commission template `PRAXIS`** created (Tools > Commissions): minimum 0, per unit $1.48 per side. Assigned to Sim101 via Accounts > Edit Account.
- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · **Slippage 2** · **Order fill resolution Standard**. Saved as template **"Praxis Backtest"** and as default.
- **The "unknown instrument NQCONT" Analyzer defect did not appear.** The strategy ran on NQCONT.

| Run | Range | Trades | Net profit | Commission | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| 1 (settings not verified; may have reset) | 2026-04-01 → 2026-07-17 | 48 | $225.64 | $0 (not included) | — | — |
| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |

- Run 3 cost arithmetic (Claude's estimate): commission ≈ 1,075 × $2.96 = $3,182. Slippage ≈ 1,075 × 2 sides × 2 ticks × $5 = $21,500, **if NT8 applied slippage to every fill**. In NT8 the Analyzer slippage applies to market and stop fills, not limit fills, so check which order types the strategy uses. Gross before costs is therefore ≈ $26k, but that figure is unverified.
- The run 1 → run 2 drop (48 → 41 trades, and higher profit after adding commission) is **unexplained**. Run 1's settings were not read back.
- **Amear's ruling: hand off to Claude Code. Hold the walk-forward** until the code is checked for fidelity to the paper.

```

### Session-template hours were never captured (OBSERVED)
```
$ sed -n '156p' docs/reference/2026-07-24-nt8-windows-reference.md
- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)

$ /usr/bin/grep -niE 'session template|trading hours|RTH|never captured|not captured' docs/reference/2026-07-24-nt8-windows-reference.md | head -40
32:- **Tools menu** (from notes): Instruments · Instrument Lists · Database Management · Hot Keys · **Historical Data** · Commissions · Risk · **Trading Hours** · Import · Export · Remove NinjaScript Assembly… · Global Simulation Mode *(license-gated)* · Client Dashboard · Settings.
150:4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
156:- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)
213:1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*

```

**Template-hours inconsistency (INFERRED).** The dispatch brief described the template as "8:30–16:00 Central = 09:30–16:00 ET". That is internally inconsistent: 08:30 CT is 09:30 ET, but 16:00 CT is 17:00 ET. I do not rely on it. The usable evidence is Amear's report that "the 16:00 bar is followed by 9:31". He also reports that the import file has 1,302 rows stamped `17:00:00` and that NT8 shows the file "bar for bar", with no hour shift. So data exists past 16:00 ET, and the RTH chart still jumps from 16:00 to 09:31. That implies the template's session ends at **16:00 ET (15:00 CT)**, not 16:00 CT (INFERRED). It rests on one date read by Amear (2026-07-17). Every D2 answer below assumes "last RTH bar = 16:00 ET stamp". The printed hours (`Tools > Trading Hours`) remain the open TODO above.

### Prior static reading under test: DECISION_LOG line 353 (OBSERVED text)
```
$ sed -n '353p' DECISION_LOG.md
- [2026-08-29T00:35:00Z] WHO: praxis-master (session 52) | WHAT: **CONSEQUENCE FOR `[N]`: THE STATED BASIS OF AMEAR'S SLIPPAGE FRAMING DOES NOT SURVIVE THE VERIFICATION ABOVE. SURFACED TO HIM, NOT RE-DECIDED — THE NUMBER REMAINS HIS** | WHY: S8, and because the master must not report a component at a level the evidence supports in either direction. Amear's framing at `00:10:00Z` was that `[N]` must price *"realistic slippage on a fill I'm being granted by an optimistic assumption, at exactly the price level where everyone else's stops are"* — i.e. **breakout adverse selection at a stop cluster**, and therefore *"a worse number"* than the committed 1 tick/side. **That framing presupposes a touch-triggered fill at the band. Verified above: there is none.** The order is a market order submitted `OnBarClose` at a semi-hourly stamp and filled at the next bar's open. The UNGRADED research states the same distinction independently at its Area-3 rollup: *"Not breakout adverse selection — the order is not triggered by a touch — but not free"* | WHERE: `DECISION_LOG` `2026-08-29T00:10:00Z` (his framing, transcribed); `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md` Areas 3-4 and addendum §"What survives" | WHEN: 2026-08-29 | HOW: **WHAT THE VERIFICATION MOVES, AND WHAT IT LEAVES ALONE.** It removes the *stated reason* for widening past 1 tick; it does **not** establish that 1 tick is correct, and the master does not assert that. Three facts bear on `[N]` and all three are recorded rather than resolved: (1) the research's quiet-RTH practitioner consensus for 1-2 lot NQ market orders is **0-1 tick**, which is the bucket a stamp-timed market order actually falls in; (2) the independent NQ futures replication used **0.5 tick/trade** and its author called that *"already optimistic"* — so `config/backtest-cost-model.json`'s committed **1 tick/side is more conservative than the replication reporting Sharpe 1.67**; (3) the source paper's own authors disclosed live IBKR slippage at **5x their modelled figure**, which is the strongest cautionary number on record and is **SPY, not NQ**. **HIS BEHAVIOURAL PRE-COMMITMENT IS UNAFFECTED AND STANDS:** the number is fixed **before the equity curve exists**, per his own words and per `docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md` §2. **The master does not propose a value for `[N]` and did not offer him a menu of candidate magnitudes, on the grounds that anchoring is picking it by another route** | STATE: open — `[N]` still outstanding and still Amear's; only its stated justification has changed

```

### On-disk record of NT8 runtime semantics (fill timing, ExitOnSessionClose, slippage)
The reference doc has no hit for managed approach, next bar, ExitOnSessionClose or slippage semantics. It only lists the Analyzer field names at line 151:
```
$ /usr/bin/grep -niE 'managed approach|next bar|ExitOnSessionClose|exit on session close|slippage|fill' docs/reference/2026-07-24-nt8-windows-reference.md
43:  - **Orders** — working/filled/rejected orders (Instrument, Action, Type, Qty, Limit, Stop, State, Filled…). Double-click to modify qty/price inline; right-click to cancel. ([`03-cc-orders.png`](assets/nt8-2026-07-24/03-cc-orders.png))
44:  - **Executions** — individual fills. ([`04-cc-executions.png`](assets/nt8-2026-07-24/04-cc-executions.png))
151:5. **Execution:** Include commission · Order fill resolution · Slippage (ticks) · Bars required to trade · Max bars look back · Entry handling.

```
The docs-wide grep returned **56** lines (count below), then the lines themselves:
```
$ /usr/bin/grep -rniI 'managed approach\|next bar\|ExitOnSessionClose\|exit on session close\|slippage' docs/ | wc -l
      56

```
```
$ cut -c1-260 $W/rt_all.txt   # $W/rt_all.txt = output of: /usr/bin/grep -rniI 'managed approach\|next bar\|ExitOnSessionClose\|exit on session close\|slippage' docs/
docs/design/2026-07-08-block1-signal-delivery.md:13:- **Latency:** NQ futures signals are time-sensitive; every second of delivery delay is slippage risk. Target: webhook receipt → local file on disk in low single-digit seconds.
docs/specs/2026-07-16-b2-noise-area-ruleset.md:53:| Costs assumed | $0.0035/share commission + $0.001/share slippage (IBKR, SPY) | §3 p. 10 |
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:91:| SHM-4 | Divergence bands | Win rate > 15 ppts below backtest, OR mean slippage > 2 ticks/side worse than modeled, over the 20-trade window | Coarse, few, pre-declarable bands beat a fitted statist
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:104:- [ ] CANDIDATE — Walk-forward matrix run to completion; ≥ 12 OOS windows; configuration (windows, roll rule, costs, slippage model) committed to the repo
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:121:| Q5 | Cost model to assume: commissions, slippage ticks/side, and whether MFFU/Rithmic fee schedule is specified | P&L and every SHM distribution are meaningless without pinned costs |
docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129:**Answer:** The strategy under test is the **Zarattini–Aziz–Barbon NQ "Noise-Area" intraday breakout** (clock-anchored, rules-based, one bracket/session). It is **NOT exportable from TradingVie
docs/specs/2026-07-15-b2-data-acquisition-spec.md:53:- **Why volume/OI roll, not calendar:** Rolling on the liquidity crossover keeps the continuous series on the **actually-traded** contract, so fills, slippage (Q5, 1 tick/side), and the High-resolution intra
docs/specs/STRATEGY_HEALTH_MONITOR_SPEC.md:49:- **Metric:** Per-trade comparison of live fills against the backtest model on the same signals — slippage, entry timing, MFE/MAE profile, win rate.
docs/reference/2026-07-24-nt8-windows-reference.md:151:5. **Execution:** Include commission · Order fill resolution · Slippage (ticks) · Bars required to trade · Max bars look back · Entry handling.
docs/reports/2026-07-15-btb-oco-geometry-fix.md:26:The entry is a **market order**, so its fill tracks the live inside market, not the payload price — the same session even showed a fill/reference delta on a *good* signal (fill 29820 vs reference 29821.25). 
docs/reports/2026-07-15-b2-q1-strategy-exportability.md:39:- **The Phase 3 spec already prescribes exactly this.** Block 2 verbatim: *"Validating the NQ Noise-Area strategy against historical data using **NinjaTrader's Strategy Analyzer**."* It pins the full c
docs/reports/2026-07-15-b2-q1-strategy-exportability.md:53:- **Primary engine:** NT8 Strategy Analyzer — rolling walk-forward 252 IS / 63 OOS / 63 step; High fill resolution, 1-tick series, 1-tick entry slippage, $2.96 RT commission; optimize {lookback, nois
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:314:- **Slippage (ticks)**
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:324:**The operator brief never specifies `Order fill resolution`, `Slippage`, or
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:356:they're results rather than a control, F3 requires the slippage assumption
docs/reports/2026-07-10-b1f-ninjascript-consumer.md:43:**Managed approach**: `SetStopLoss(entrySignal, CalculationMode.Price, …)` + `SetProfitTarget(entrySignal, CalculationMode.Price, …)` before `EnterLong/EnterShort(qty, entrySignal)` (entrySignal = `PRX
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:17:resolution and the slippage assumption must be **written down and committed
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:19:slippage number is yours and you have not given it.
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:26:  **Not authorised until the slippage number is committed.**
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:245:than as a control, F3 requires the slippage assumption committed first. That is
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:162:> and the slippage assumption applied at the band edge, stated in writing before
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md:168:> 1-tick resolution series, 1-tick slippage, $2.96 round-trip. Deviation F
docs/reports/2026-08-29-session52-handoff-planning-chat.md:50:> and the slippage assumption applied at the band edge, stated in writing before
docs/reports/2026-08-29-session52-handoff-planning-chat.md:86:- **The slippage number.** Called `[N]` throughout the ledger. **Amear's, and
docs/reports/2026-08-29-session52-handoff-planning-chat.md:97:> We accept Standard resolution on 1-minute bars. Band-edge slippage widened to
docs/reports/2026-08-29-session52-handoff-planning-chat.md:108:single written slippage assumption. Same single VM trip.
docs/reports/2026-08-29-session52-handoff-planning-chat.md:127:`b2_stitch.py` validates the stitched CSV — it does not grade a written slippage
docs/reports/2026-07-16-4uu-noise-area-strategy.md:43:6. **Stamp-vs-fill divergence.** NT8 fills managed market entries at the **next bar's open**, whereas the paper acts *at* the stamp price. Quantify the per-trade slippage vs the stamp Close; if material, co
docs/reports/2026-07-16-4uu-noise-area-strategy.md:56:- **Session-flat mechanism.** Explicit `mod >= 16:00 → flatten` is primary; `IsExitOnSessionCloseStrategy=true` (30s) is a backstop. On a strict RTH template these coincide; on a template extending past 1
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:101:  the open of the next bar… it eliminates the common backtest error of pretending
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:115:## Area 3 — Realised slippage at breakout moments on NQ
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:121:  expect 0-1 tick of slippage for small orders."*
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:127:  momentum, where *"slippage is generally less of a concern,"* with *"pure breakout
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:129:  optimistic."* They disclosed real Interactive Brokers slippage of **$0.005/share
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:146:  $0.001/share slippage.** Headline net result: **total return 1,985%, annualized
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:151:  $0.85/contract commission + $1.40/contract fees + **0.5 tick/trade slippage**;
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:155:  *"slippage assumptions cause a significant impact… I don't think it's realistic
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:164:- **Slippage sensitivity sweep (Option A+):** established and cheap. Convention is
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:170:  capture *when* slippage clusters, and does not fix intrabar ordering.
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:205:  realistic slippage sweeps with comfortable cushion.
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:217:(4) Fill/slippage error is largest at breakout entries; the paper's own authors
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:218:observed 5× their assumed slippage live.
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:234:- Area 3 slippage figures are **practitioner consensus**; the one hard disclosure
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:255:- https://www.elitetrader.com/et/threads/what-is-the-slippage-for-nq-stop-market-orders-during-non-spike-trading-hours.385991/
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:256:- https://grizzlyparrottrading.com/futures-basics/how-slippage-works.html
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:306:- Slippage on market orders submitted `OnBarClose` at a stamp is real; they fill at
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:307:  the next bar's open. Not breakout adverse selection — the order is not triggered
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:309:- The source authors' **5× live-vs-modelled slippage** disclosure stands as the
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:314:- **F3 remains unmet.** Its criterion demands the fill resolution and the slippage
docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:325:irrelevant here rather than argued irrelevant, and F3 reduces to a written slippage
docs/reports/2026-08-29-session53-parallel-handoff.md:83:7. **`[N]`, the band-edge slippage number, is Amear's and is undecided.** Do not
docs/reports/2026-10-28-voice-session-notes.md:9:3. **F3 `[N]` = 2 ticks per side** band-edge slippage. That is $10 per side, which with $2.96 commission comes to about $22.96 per round trip. It was chosen before any backtest output was seen, as his 2026-08-29
docs/reports/2026-10-28-voice-session-notes.md:33:- **Strategy Analyzer settings:** PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim1
docs/reports/2026-10-28-voice-session-notes.md:42:- Run 3 cost arithmetic (Claude's estimate): commission ≈ 1,075 × $2.96 = $3,182. Slippage ≈ 1,075 × 2 sides × 2 ticks × $5 = $21,500, **if NT8 applied slippage to every fill**. In NT8 the Analyzer slip
docs/reports/2026-07-15-b2-data-spec.md:23:- **Volume/OI roll** (not fixed calendar) keeps the series on the actually-traded liquid contract for realistic Q5 fills/slippage.
docs/reports/2026-07-15-b2-data-spec.md:29:**`config/backtest-cost-model.json`** — $2.96 RT commission, 1 tick/side (=$5) slippage, High fill resolution; derived totals 12.96 USD / 2.592 ticks round-turn; NQ metadata (tick 0.25, point $20, tick $5); `applies
```
The only lines that state NT8 fill timing or EOSC behaviour are `docs/reports/2026-07-16-4uu-noise-area-strategy.md:43` and `:56`, and the UNGRADED f3 research at `:101`/`:306`:
```
$ sed -n '43p;56p' docs/reports/2026-07-16-4uu-noise-area-strategy.md
6. **Stamp-vs-fill divergence.** NT8 fills managed market entries at the **next bar's open**, whereas the paper acts *at* the stamp price. Quantify the per-trade slippage vs the stamp Close; if material, consider a stop-market-at-boundary realization (spec §6 p.99 flags this) — but that is a separate decision, not this pass.
- **Session-flat mechanism.** Explicit `mod >= 16:00 → flatten` is primary; `IsExitOnSessionCloseStrategy=true` (30s) is a backstop. On a strict RTH template these coincide; on a template extending past 16:00 the explicit check governs.

$ sed -n '95,104p' docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md
- Across 14 OHLCV signal families on **72,604 five-minute MNQ RTH bars
  (Dec 2021–Aug 2025)**, gross edge ceiling ~0.07–1.50 points/trade, below a
  ~2.0-point (~$4/micro) friction floor — every single-bar signal family failed
  net of costs.
- Only strategies **holding 12–15 bars (60–75 min)** cleared friction.
- Author on execution: *"Every signal fires at bar close. Every entry executes at
  the open of the next bar… it eliminates the common backtest error of pretending
  you can fill at prices you saw before the bar closed."*
- Treat as **directional corroboration, not a transferable number.**


$ sed -n '1,12p' docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md
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

```
**Finding (OBSERVED in the files):** none of these records an **observation** of NT8 behaviour. 4uu `:43`/`:56` are assertions in the build report, written before any NT8 run. f3 `:101` quotes a third-party author describing **his own** backtest convention on MNQ 5-minute bars, not NT8. The file's own banner says "UNGRADED … must not be cited as a finding". So next-bar-open fills, ExitOnSessionClose timing, Day-TIF cancellation and slippage application all stay **INFERRED** throughout this report. Scope caveat: I searched `docs/` and the reference doc only. Files outside `docs/` (e.g. `~/praxis-signals/`) are NOT CHECKED.

**DL353 verdict.** "Market order submitted `OnBarClose` at a semi-hourly stamp" is **OBSERVED in code**: line 105 sets `Calculate.OnBarClose`, line 196 gates on HH:00/HH:30, and lines 227/229 are `EnterLong(Contracts,"L")`/`EnterShort(Contracts,"S")` with no price argument. "Filled at the next bar's open" is **INFERRED**: no on-disk observation supports it. So the DL353 row is half-verified. It holds for checkpoint entries/exits and **fails to address** the 16:00 FlatEOD case, where the "next bar" is the next day's 09:31 (see D2(c)).

---

## D2: end-stamped bars vs the author's assumption

Premise (REPORTED BY AMEAR): NT8 1-minute bars are **end-stamped**. The first RTH bar is stamped 09:31 and covers 09:30–09:31. The 16:00 bar is followed directly by the next day's 09:31.

Spec context: the spec says nothing about the bar-stamp convention of the paper's own data (grep count **0**, pasted below). Its early-close coverage is a single unrelated "Partial" hit at line 77 (count **1**, pasted below), so early close is **spec-silent**.
```
$ /usr/bin/grep -n 'Close1600' ninjascript/PraxisNoiseAreaBreakout.cs
68:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
169:				today.Close1600 = Close[0];

$ /usr/bin/grep -ciE 'early|half-day|half day|holiday|partial' docs/specs/2026-07-16-b2-noise-area-ruleset.md
1

$ /usr/bin/grep -ciE 'early|half-day|half day|holiday|partial' ninjascript/PraxisNoiseAreaBreakout.cs
0

$ /usr/bin/grep -ciE 'end-stamp|start-stamp|bar stamp|timestamp' docs/specs/2026-07-16-b2-noise-area-ruleset.md
0

```
```
$ /usr/bin/grep -niE 'early|half-day|half day|holiday|partial' docs/specs/2026-07-16-b2-noise-area-ruleset.md | cut -c1-300
77:| D6 | Exit stop | opposite band, or `max/min(band, VWAP)` (pp. 9,13) | RTF: "VWAP trailing stop" | ⚠️ Partial — paper's stop is band-**or**-VWAP (whichever tighter), not VWAP alone |

```
Spec lines governing timing (OBSERVED):
```
$ sed -n '36,38p;64p;99p' docs/specs/2026-07-16-b2-noise-area-ruleset.md
- **Entry condition:** at a **semi-hourly checkpoint only** — `HH:00` and `HH:30` — if price is **above** the Upper Boundary → **go long**; if **below** the Lower Boundary → **go short**. Checking only at the half-hour (not tick-by-tick) is deliberate, to avoid acting on transient spikes; the paper shows a breach a few minutes before 10:30 is not acted on until the 10:30 stamp (Fig. 2, p. 9).
- **Direction rule:** long above the band, short below — trend-following the breakout side (p. 8–9).
- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** into a new position that direction (p. 9). Realized average trade frequency is **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).
- **Session flat:** **all positions closed at the market Close = 16:00 ET** (cash close), never held overnight (Fig. 2 caption p. 9; Fig. 4 p. 12). The paper has **no intraday time-stop** — the only time-based exit is 16:00.
Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, market-hours only; **flat at 16:00** (or the trader-chosen 11:30 — see D8). Entry via `EnterLongStopMarket`/`EnterShortStopMarket` at the boundary is a reasonable NT8 realization of "act at the next HH:00/HH:30 stamp if price is outside the band," but note the paper acts on the **stamp**, not on an intrabar stop-touch — a stop-market order can fill mid-bar and diverge slightly; reconcile in b2-signal-repro.

```

### Mechanism walk-through

**M1. Session rollover, `todayOpen`, `prevClose`, `CommitDay`, VWAP reset (lines 140–161):**
```
$ sed -n '140,161p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (CurrentBar < 1)
				return;

			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar

			// ---- Session rollover: on the first bar of a new RTH session, close out the prior
			// day into history (so σ sees it ONLY once complete — no look-ahead), then reset. ----
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;
				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;

				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
				vwapCumVol = 0.0;
				haveDay    = true;
			}

```
- `mod = H*60+M` (143): the minute-of-day of the bar's **end** stamp. The bar stamped 10:00 has `mod` 600 and spans 09:59–10:00. **Holds** for the paper's `Close_{HH:MM}` meaning "price at HH:MM" (INFERRED; the paper's own stamp convention is spec-silent).
- `IsFirstBarOfSession` (147): this is NT8's session flag, not a clock test, so it does not depend on the stamp convention. On this template it is true on the 09:31 bar (INFERRED from standard NT8 semantics plus Amear's "no 9:30 bar is shown"). **Holds.**
- `todayOpen = Open[0]` (152): the Open of the 09:31-stamped bar is the first trade in 09:30:00–09:31. That is the paper's `Open_{t,9:30}`. Amear read it as 28605.25 on 2026-07-17 (REPORTED). **Holds.** The code never used the 09:30-stamped pre-open row that the old expectation pointed at, so the old start-stamp error did not reach the code (OBSERVED: no clock-based open lookup exists).
- `prevClose = Close[1]` (155): on the 09:31 bar, `[1]` is the prior session's last bar, the one stamped 16:00 (REPORTED: 16:00 → 9:31). Its Close is the 16:00:00 price, the paper's `Close_{t-1,16:00}`. **Holds on normal days.** On an early-close day it becomes the early-close price (see (d)). The `(CurrentBar >= 1)` guard is dead code: line 140 already returns when `CurrentBar < 1` (OBSERVED, harmless).
- `CommitDay()` (149; body below): it runs on the 09:31 bar and pushes the completed prior day. There is no look-ahead. **Holds.**
- VWAP: the accumulators reset at lines 158–159, **before** the 09:31 bar's own accumulation at lines 171–176 in the same call. The VWAP therefore covers bars 09:31…current, which is 09:30:00 up to the current stamp. **Holds** for "anchored at 09:30" (spec line 61). It is a typical-price (HLC/3 × volume) approximation on 1-minute bars. That is a formula-granularity question, not a stamping one: spec-silent on granularity, INFERRED acceptable.

**M2. Per-bar bookkeeping and VWAP accumulation (lines 163–176):**
```
$ sed -n '163,176p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (!haveDay)
				return;                         // haven't seen a session open yet in this run

			// ---- Per-bar bookkeeping: record this minute's close + advance session VWAP. ----
			today.Closes[mod] = Close[0];       // minute-of-day -> close (spec §1: Close_{t,HH:MM})
			if (mod == CloseMod)
				today.Close1600 = Close[0];

			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}

```
`today.Closes[mod]` is keyed by end-stamp minute, so σ's `Close_{t-i,HH:MM}` and today's checkpoint `Close[0]` use the **same** stamp convention. They are mutually consistent whatever the paper used (OBSERVED in code). `Close1600` is written at line 169 and never read; only lines 68 and 169 match (OBSERVED, pasted below). It is a dead field and harmless, because `prevClose` comes from `Close[1]`.
```
$ /usr/bin/grep -n Close1600 ninjascript/PraxisNoiseAreaBreakout.cs   (see misc block above for identical output)
68:			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
169:				today.Close1600 = Close[0];
```

**M3. Band/plots (178–186) and band build (238–267):**
```
$ sed -n '178,186p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- Build the band for THIS bar's minute-of-day (for plots every bar; orders only at checkpoints). ----
			BuildBand(mod);
			if (haveBand)
			{
				Values[0][0] = curUpper;
				Values[1][0] = curLower;
			}
			if (vwapCumVol > 0)
				Values[2][0] = curVwap;

```
```
$ sed -n '238,267p' ninjascript/PraxisNoiseAreaBreakout.cs
		private void BuildBand(int mod)
		{
			haveBand = false;
			if (todayOpen <= 0)
				return;

			double sumAbs = 0.0;
			int cnt = 0;
			// Walk newest->oldest completed days; take up to Lookback that recorded this minute-of-day.
			for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
			{
				DayRecord rec = history[d];
				double c;
				if (rec.Open > 0 && rec.Closes.TryGetValue(mod, out c))
				{
					sumAbs += Math.Abs(c / rec.Open - 1.0);     // spec §1 step 1
					cnt++;
				}
			}
			if (cnt < Lookback)                                 // require a full 14-day sample (spec §3 fixed N)
				return;

			curSigma = sumAbs / cnt;                            // spec §1 step 2
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
			haveBand = true;
		}

```

**M4. Flatten, checkpoint gate, order actions (188–198, 200–230):**
```
$ sed -n '188,198p' ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}

			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

```
```
$ sed -n '200,230p' ninjascript/PraxisNoiseAreaBreakout.cs
			double price = Close[0];             // the checkpoint stamp price (spec §2: evaluate at the stamp, not intrabar)
			MarketPosition mp = Position.MarketPosition;

			// (1) TRAILING-STOP / EXIT — evaluated ONLY at the stamp (spec §4 p.9). Reversal (2) below
			//     handles the opposite-band cross; this closes to FLAT on the same-side band/VWAP trail.
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
			}

			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
		}

```
Checkpoint set produced by line 196 under end-stamping (OBSERVED by enumeration):
```
$ python3 -c "<enumerate end-stamp minutes 09:31..16:00 satisfying line 196>"
checkpoint stamps: 10:00 10:30 11:00 11:30 12:00 12:30 13:00 13:30 14:00 14:30 15:00 15:30
count = 12
flatten (mod>=960) bars in an RTH session ending 16:00: ['16:00']
```

**M5. CommitDay / FlattenAll (270–291):**
```
$ sed -n '270,291p' ninjascript/PraxisNoiseAreaBreakout.cs
		#region Session commit / flatten
		// Push the completed in-progress day into the history store (trim to HistoryCap). Called on
		// the first bar of each new session, so the day just ended becomes available to σ — and never
		// before it is complete (the no-look-ahead invariant).
		private void CommitDay()
		{
			if (today != null && today.Open > 0 && today.Closes.Count > 0)
			{
				history.Add(today);
				while (history.Count > HistoryCap)
					history.RemoveAt(0);
			}
			today = null;
		}

		private void FlattenAll(string reason)
		{
			if (Position.MarketPosition == MarketPosition.Long)
				ExitLong("FlatEOD", "");
			else if (Position.MarketPosition == MarketPosition.Short)
				ExitShort("FlatEOD", "");
		}

```

**M6. Session-close settings (97–114):**
```
$ sed -n '97,114p' ninjascript/PraxisNoiseAreaBreakout.cs
		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET.";
				Name         = "PraxisNoiseAreaBreakout";

				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
				Calculate                                 = Calculate.OnBarClose;
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
				BarsRequiredToTrade                       = 20;
				IsInstantiatedOnEachOptimizationIteration = false;


```

### D2 answers

**(a) The bar stamped 10:00.**
- **Does the checkpoint fire?** Yes. `mod` = 600, `Minute` = 0, and 570 < 600 < 960. It also needs `haveBand`, i.e. 14 completed sessions that recorded minute 600 (OBSERVED in code, lines 196–198 and 257).
- **Is `Close[0]` the paper's 10:00 price?** Yes, under end-stamping. It is the last trade in 09:59–10:00, i.e. the 10:00:00 price (INFERRED from Amear's end-stamp report). The paper's own data convention is spec-silent. Internal consistency holds either way (M2).
- **Where does the order fill?** The order is a no-price managed order, a **market** order (INFERRED), submitted when the 10:00 bar closes. Under `Calculate.OnBarClose` and Standard fill resolution it is expected to fill at the **Open of the 10:01-stamped bar**, the first trade at or after 10:00:00, with 2 ticks of adverse slippage added (INFERRED; no on-disk observation, see above).
- **Net timing gap vs the paper:** about one tick-time of drift plus the slippage. It is not a full minute (INFERRED).

**(b) The bar stamped 16:00.**
- **Does it trigger the flatten?** Yes. `mod` = 960 ≥ `CloseMod` 960 → `FlattenAll(...)`, then `return` (OBSERVED, lines 189–193; the enumeration shows `['16:00']` as the only flatten bar).
- **Is an entry at 16:00 blocked?** Yes, twice over. The `return` at line 192 exits first, and `isCheckpoint` requires `mod < CloseMod` (OBSERVED, line 196). 16:00 is not in the checkpoint list.

**(c) KEY: which order actually closes the 16:00 position?** Grade: **CANNOT-DETERMINE-STATICALLY.**

What is OBSERVED in code:
- `FlattenAll` submits `ExitLong("FlatEOD","")`/`ExitShort("FlatEOD","")` (lines 288/290) on the close of the 16:00 bar.
- On this template that bar is the session's **last** bar (REPORTED).
- `IsExitOnSessionCloseStrategy = true`, `ExitOnSessionCloseSeconds = 30`, `TimeInForce = TimeInForce.Day` (lines 108, 109, 111).

The bar after the 16:00 bar is the **next day's 09:31**. If the managed market order fills at the next bar's Open (INFERRED), FlatEOD fills at the **next-day 09:31 open**. The position would then carry the overnight gap, which breaks spec line 64: "never held overnight".

Competing mechanisms (all INFERRED, none observed on disk):
- **S1, EOSC closes at 16:00.** NT8 submits an "Exit on session close" order on the last bar whose time is ≥ session end − 30 s (the 16:00 bar) and fills it at that bar's **Close** (the 16:00:00 price). FlatEOD then either sees `MarketPosition.Flat` and submits nothing (if EOSC is processed before `OnBarUpdate`), or is submitted against a position that is already closing and gets ignored or cancelled. Trades tab: exit name **"Exit on session close"**, exit time **16:00** on the entry date. This would be the most paper-faithful outcome. It would also mean the comment at line 108 ("backstop; explicit 16:00 flat is primary") is inverted in practice.
- **S2, FlatEOD fills next day.** EOSC does not fire, e.g. it was unchecked in the Analyzer or its timing does not match this bar. FlatEOD fills at the next-day 09:31 Open. Trades tab: exit name **"FlatEOD"**, exit time **09:31** on the **next** date, and entry date ≠ exit date.
- **S3, Day-TIF cancellation.** EOSC does not fire and the `TimeInForce.Day` FlatEOD order is cancelled at session end. The position is then carried into the next session and closed later by an XL/XS/reverse/FlatEOD/EOSC. Trades tab: an entry date earlier than the exit date, with the exit name ≠ "FlatEOD at 09:31".
- **S4, both orders work.** EOSC fills at 16:00, and a FlatEOD submitted in the same `OnBarUpdate` also fills next morning against a flat position, opening an unintended position. Trades tab: an extra row opening at 09:31. I consider S4 least likely because managed exit orders normally do not open positions (INFERRED).

The build report's assertion (4uu `:56`, "on a strict RTH template these coincide") is an assumption, not an observation.

**Readback that settles (c), Strategy Analyzer run 2, Trades tab (41 rows):**
1. Tally the **Exit name** column: how many rows read `FlatEOD`, `Exit on session close`, `XL`, `XS`, or anything else (e.g. `Close position`).
2. For every `FlatEOD` or `Exit on session close` row, compare **Exit time** (16:00 vs 09:31) and **Entry time date vs Exit time date**.
3. Count rows where the entry date ≠ the exit date (overnight holds).
4. Cross-check in the Executions tab for any execution named `FlatEOD` stamped 09:31.

**(d) Early-close day (session ends before 16:00 ET).** Spec-silent (grep above). The code has no early-close handling (grep count **0**, below).
```
$ /usr/bin/grep -ciE "early|half-day|half day|holiday|partial" ninjascript/PraxisNoiseAreaBreakout.cs
0
```
If the template encodes an early end E (e.g. about 13:00 ET; the exact CME/NT8 times are UNVERIFIED), the last bar has `mod` < 960 (INFERRED):
- `FlattenAll` **never fires** that day.
- If E is an HH:00/HH:30 stamp, the last bar is **also a checkpoint**. The strategy can then enter or reverse on the session's final bar, and that order's "next bar" is the next session's 09:31.
- Only EOSC (if it fires at E) closes the position that day. With EOSC off, the position is carried overnight.
- The next day's `prevClose` is the E close. That is arguably correct for the cash close of that day, but spec-silent.
- σ: the early day has no closes after E. `BuildBand` (lines 247–256) walks back past it to the next older day that recorded the minute, so the sample stays at 14. That is a benign deviation, and `HistoryCap` = 29 allows it (OBSERVED in code).

If the template does **not** encode the early close, no bar reaches `mod` ≥ 960 or the session end − 30 s that day. Neither flatten mechanism has a bar to act on, and an overnight hold is likely (INFERRED).

**Readback:** Trades rows whose entry falls on a known early-close or holiday-adjacent date in the run-3 range. Read the exit name and exit date/time. Also read `Tools > Trading Hours > CME US Index Futures RTH > Holidays/partial sessions`. The dates themselves are UNVERIFIED and should be taken from the template.

**(e) 15:30 checkpoint.** `mod` = 930 is in the checkpoint list (OBSERVED enumeration). Entries, exits and reversals evaluate at the 15:30 close and are expected to fill at the 15:31 Open (INFERRED). The position is then held until the 16:00 flatten, whose real fill is the open question in (c). EOSC's 30-second window is not reached at 15:30 (INFERRED). **Behaves normally**; it inherits (c) for its exit.

---

## D3: order-type inventory

### Call-site grep (OBSERVED: 8 matching lines; lines 224 and 225 are comments, which leaves 6 call sites)
```
$ /usr/bin/grep -nE 'Enter(Long|Short)|Exit(Long|Short)|Set(StopLoss|ProfitTarget|TrailStop)|Submit' ninjascript/PraxisNoiseAreaBreakout.cs
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");

```

| Line | Call | Context | NT8 order type |
|---|---|---|---|
| 211 | `ExitLong("XL","")` | long, checkpoint, `price <= stop` | managed **market** exit (INFERRED) |
| 219 | `ExitShort("XS","")` | short, checkpoint, `price >= stop` | managed **market** exit (INFERRED) |
| 227 | `EnterLong(Contracts,"L")` | checkpoint, `price > curUpper`, not long | managed **market** entry. When short, a managed **reverse** (INFERRED) |
| 229 | `EnterShort(Contracts,"S")` | checkpoint, `price < curLower`, not short | managed **market** entry. When long, a managed **reverse** (INFERRED) |
| 288 | `ExitLong("FlatEOD","")` | any bar with `mod >= 960`, long | managed **market** exit (INFERRED) |
| 290 | `ExitShort("FlatEOD","")` | any bar with `mod >= 960`, short | managed **market** exit (INFERRED) |
| (none) | NT8 "Exit on session close" | `IsExitOnSessionCloseStrategy=true` (108) | platform-generated **market** exit (INFERRED) |

There are no `Set(StopLoss|ProfitTarget|TrailStop)` calls, no `Submit*` calls, and no `EnterLong/ShortLimit/StopMarket/StopLimit` variants. The regex `Enter(Long|Short)` would also have matched those variant prefixes, and only plain `EnterLong`/`EnterShort` appear (OBSERVED). The "trailing stops" are therefore **clock-sampled conditions that send market orders**, not resting stop orders. That matches spec line 38 ("stops … evaluated only at the semi-hourly stamps"). It also confirms DL353's "not touch-triggered" point (OBSERVED).

**Managed reverse (INFERRED).** `EnterShort` while long is expected to make NT8 send a close-position order for the open long and then the short entry. These are two fills: the old trade's exit and the new trade's entry.

**Same-checkpoint double fire (OBSERVED in code: both calls fire).** Take a long position with `price < curLower`:
1. Line 208: `stop = max(curUpper, curVwap) ≥ curUpper` (BandOrVWAP; OppBand gives `stop = curUpper`).
2. From lines 263–264, `curUpper = refUpper·(1+σ) ≥ refLower·(1−σ) = curLower`, because `refUpper ≥ refLower > 0` and σ ≥ 0.
3. So `price < curLower ≤ curUpper ≤ stop`, which gives `price <= stop`, so **`ExitLong("XL")` fires** (line 211).
4. Line 226 is false. Line 228 tests `Position.MarketPosition`, which is still `Long` because no fill happens inside `OnBarUpdate` under `OnBarClose`. The author's own comment at 224–225 says the same (INFERRED for NT8). So **`EnterShort(1,"S")` also fires** (line 229).

The short→long case mirrors this: `stop = min(curLower, VWAP) ≤ curLower ≤ curUpper < price`, so XS fires **and** EnterLong fires. Therefore **every reversal, in both ExitModes, submits an explicit exit and a reverse entry on the same bar** (OBSERVED in code).

What NT8 then does is **CANNOT-DETERMINE-STATICALLY**. The candidate outcomes are all INFERRED:
- (i) Clean: XL closes the long, the reverse's close portion is dropped, and S opens a short of 1.
- (ii) Double-close: XL **and** the reverse's close both fill, producing a net short of 2 or an extra trade row.
- (iii) The entry is ignored because an exit is pending. The result is flat, not reversed, which **removes reversals** and changes the trade count.

**Readback:**
1. Trades tab: any row with **Qty > 1**; any **two exit rows with the same exit time**; whether each `S`/`L` entry shares its timestamp with an `XL`/`XS` exit.
2. Executions tab at a reversal timestamp: the number of executions and their quantities.
3. Log tab: any "ignored" order warnings.

Partial evidence for run 2 (INFERRED): commission $121.36 = 41 × $2.96 = 82 × $1.48 exactly (arithmetic below). That is 82 contract-sides over 41 trades, so **no run-2 trade carries Qty 2**, assuming NT8 charges commission per contract per fill. It does not exclude outcome (iii). The code sets no `TraceOrders` (OBSERVED in the `cat -n` above), so the Output window will not explain order handling unless the code is changed (not done; see return note).

**EOSC in addition to FlattenAll?** Yes, it can fire on the same 16:00 bar. See D2(c), scenarios S1 and S4 (INFERRED / CANNOT-DETERMINE-STATICALLY).

### Does the 2-tick slippage hit every fill in run 3? Is $21,500 the right formula?
Every strategy-originated order is a market order (OBSERVED: no limit/stop variants). If NT8 applies Analyzer slippage to market fills (INFERRED; voice note line 42 states it, and no on-disk NT8 observation exists), then **yes, every fill is slipped**, including FlatEOD and EOSC exits if those are market orders (INFERRED).

`1,075 × 2 × 2 × $5 = $21,500` holds **only if all of these hold**:
1. **Fills per trade = 2, each for 1 contract.** Contracts = 1 (Analyzer setting, REPORTED). Reversals do not add fills per trade, since the close fill belongs to the old trade and the entry fill to the new one (INFERRED). That fails under double-close outcome (ii).
2. Slippage applies to **both** entry and exit fills, including platform EOSC exits (INFERRED).
3. NT8 does **not truncate** slippage to keep the fill inside the bar's high/low (UNVERIFIED; I believe NT8 may cap it, and that would make $21,500 an upper bound).
4. **NQCONT point value = $20 is honoured** (UNVERIFIED: nqcont investigation `:224`, pasted below). If it is not honoured, slippage would be $1,075 and **every** dollar figure, including the $1,281.61 net, is off by 20×. Tick size is 0.25, so tick value = $5.
5. 1,075 counts round-trip Trades rows, including any position force-closed at the end of data (INFERRED).
6. Run 3 actually used Slippage 2. The brief says "same settings", but run 3's commission was not read back (REPORTED, "—").

Point-value evidence (OBSERVED: grep count **20**):
```
$ cut -c1-200 $W/pv_all.txt   # $W/pv_all.txt = output of: /usr/bin/grep -rniI 'point value' docs/
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:94:| Point value | `20` |
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:103:A wrong tick size or point value silently corrupts every number downstream. It
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:62:| Point value | `20` (so tick value is $5) |
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:70:stop.** A wrong tick size or point value corrupts every number downstream without
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:373:/Users/admin/praxis-signals/b2-data/4uu-VM-brief.md:42:- **Point value:** `$20`  (tick value = $5)
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:377:/Users/admin/praxis-signals/b2-data/outbound/INSTRUCTIONS.md:42:- **Point value:** `$20`  (tick value = $5)
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:380:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:77:  through the Instruments GUI. A hand-written row with a wrong tick size or
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:383:/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:205:| Point value | `$20` (tick value $5) |
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:386:/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:77:  through the Instruments GUI. A hand-written row with a wrong tic
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:389:/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:205:| Point value | `$20` (tick value $5) |
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:160:  contract shows as **$20.00**, not $1.00. If point value is not honoured, abandon
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:57:instrument, correct tick and point value, no expiry, accepts imported flat bars."*
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:63:be made to carry a $20 point value is Q-B below, and it is **UNVERIFIED**.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:218:   that accepts a tick size and a point value.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:219:2. Tick size `0.25`, point value `20`, currency `USD`, trading hours
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:224:**UNVERIFIED:** whether NT8 honours **point value** for P&L on a non-Future type.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:230:B** — a silently wrong point value is worse than a blank chart.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:262:5. **Does NT8 honour tick size and point value for P&L on non-Future instrument
docs/reports/2026-08-29-session53-w2-q2-nqcont-definition.md:78:94:| Point value | `20` |
docs/reports/2026-08-29-session53-w2-q2-nqcont-definition.md:93:`NQCONT` was visible in the Instruments manager. Tick size, point value, currency,
```
```
$ /usr/bin/grep -rniI 'point value' docs/ | wc -l
      20

$ sed -n '218,230p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
   that accepts a tick size and a point value.
2. Tick size `0.25`, point value `20`, currency `USD`, trading hours
   `CME US Index Futures RTH`.
3. Import `NQCONT2.Last.txt` and chart the bare name.

**⚠️ The check that decides whether B is usable at all — do not skip it.**
**UNVERIFIED:** whether NT8 honours **point value** for P&L on a non-Future type.
If it treats the instrument as 1 unit = $1, every P&L number is wrong by a factor
of 20 and *nothing on the surface will say so.*

**Test:** run a backtest, take one trade with a known entry and exit, and confirm a
**1.00-point move on 1 contract shows as $20.00**. If it shows $1.00, **abandon Fix
B** — a silently wrong point value is worse than a blank chart.

```
Arithmetic (OBSERVED output):
```
$ python3 -c "print('run3 slippage 1075*2*2*5 =', 1075*2*2*5); print('run3 commission 1075*2.96 =', round(1075*2.96,2)); print('run3 gross est 1281.61+3182+21500 =', round(1281.61+1075*2.96+1075*2*2*5,2)); print('run2 commission 41*2.96 =', round(41*2.96,2)); print('run2 slippage 41*2*2*5 =', 41*2*2*5); print('run2 gross est 599.08+121.36+820 =', round(599.08+41*2.96+41*20,2)); print('run1 gross if slip 0 =', 225.64, '; if slip 2 =', round(225.64+48*20,2)); print('tick value 0.25*20 =', 0.25*20); print('per-trade slip at 2 ticks/side, 2 sides =', 2*2*0.25*20); print('slippage if point value=1 (not honoured):', 1075*2*2*0.25*1)"
run3 slippage 1075*2*2*5 = 21500
run3 commission 1075*2.96 = 3182.0
run3 gross est 1281.61+3182+21500 = 25963.61
run2 commission 41*2.96 = 121.36
run2 slippage 41*2*2*5 = 820
run2 gross est 599.08+121.36+820 = 1540.44
run1 gross if slip 0 = 225.64 ; if slip 2 = 1185.64
tick value 0.25*20 = 5.0
per-trade slip at 2 ticks/side, 2 sides = 20.0
slippage if point value=1 (not honoured): 1075.0

$ echo '41*2.96' | bc
121.36

```
The pre-cost gross of run 3 (≈ $25,963.61) and the run-2 gross (≈ $1,540.44) are **conditional on items 1–6**, and are therefore INFERRED. **Readback that settles item 4 without a new run:** take one run-2 Trades row and check `Profit = (Exit price − Entry price) × 20 × direction × Qty − $2.96`. Slippage is already baked into the fill prices (INFERRED). Comparing those fill prices with the Open of the next bar after the stamp also measures item 3.

---

## D4: why run 1 had 48 trades and run 2 had 41

### Can slippage or commission change a trade decision? Null-search with positive control
```
$ /usr/bin/grep -nE 'Position\.AveragePrice|SystemPerformance|Account|GetProfitLoss|Execution|OnOrderUpdate|OnExecutionUpdate|Position\.MarketPosition' ninjascript/PraxisNoiseAreaBreakout.cs
201:			MarketPosition mp = Position.MarketPosition;
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
226:			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
228:			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
287:			if (Position.MarketPosition == MarketPosition.Long)
289:			else if (Position.MarketPosition == MarketPosition.Short)

$ /usr/bin/grep -cE 'Position\.AveragePrice|SystemPerformance|Account|GetProfitLoss|Execution|OnOrderUpdate|OnExecutionUpdate' ninjascript/PraxisNoiseAreaBreakout.cs
0

$ /usr/bin/grep -cE 'Position\.MarketPosition' ninjascript/PraxisNoiseAreaBreakout.cs
6

$ /usr/bin/grep -nE 'Unrealized|Realized|Commission|Slippage|Fill|AvgPrice|Bars\.IsLastBarOfSession|IsLastBarOfSession|SessionIterator|ActualSessionEnd' ninjascript/PraxisNoiseAreaBreakout.cs

```
**OBSERVED:**
- The combined grep's only hits are `Position.MarketPosition` (positive control, count **6**).
- The P&L/fill/account tokens return count **0**.
- A wider probe (`Unrealized|Realized|Commission|Slippage|Fill|AvgPrice|IsLastBarOfSession|SessionIterator|ActualSessionEnd`) returns **no lines**.

Every decision input is bar OHLCV, `Time[0]`, internal state, and `Position.MarketPosition`, which depends on **whether** a fill happened, not its price. So **slippage and commission cannot change which orders are submitted**. Market orders fill regardless of price (INFERRED), so they cannot change the trade count either.

**Run 1 vs run 2 (INFERRED):**
- If only costs had differed, the trade set would be identical and the count would be the same. The count differs (48 vs 41).
- Adding costs to an identical trade set can only lower net. Yet run 2 has commission $121.36 (and presumably $820 slippage) and a **higher** net ($599.08 vs $225.64).

Both facts mean **the trade set differed**, not just costs. Run 1's gross is $225.64 if it had no slippage, or $1,185.64 if it had 2 ticks. Run 2's conditional gross is $1,540.44. These figures cannot be decomposed further without run 1's settings.

### Hypotheses ranked by plausible count change (all INFERRED)
1. **Trading-hours template was not "CME US Index Futures RTH" in run 1.** Candidates: `<Use instrument settings>` (with NQCONT's instrument-level hours not RTH), an ETH template, or a 24×7 default. A settings "reset" makes this plausible. Effect: session start moves to the evening open, so `todayOpen`, σ's anchor, `prevClose` and VWAP all change. `mod >= 960` fires on every 16:00–23:59 bar, and EOSC fires at a different time. The trade set changes wholesale. **Largest expected impact.**
2. **Exit on session close or Time in force differed (both Analyzer-editable).** This interacts with D2(c). With EOSC on, 16:00 positions close at 16:00 (S1). With it off, FlatEOD fills next morning (S2) or is Day-cancelled and carried over (S3). Carried positions change the next day's `Position.MarketPosition` at checkpoints, which changes whether `EnterLong/Short` fires, so the count changes.
3. **Date range or data state differed.** Examples: a different start date, which shifts the ~14-session σ warm-up (lines 257–258) inside a 3.5-month window, or a different loaded data state for NQCONT between runs. Amear says "same range", but run 1's fields were not read back.
4. **Order fill resolution High vs Standard.** With High, market orders fill on the intrabar series rather than the next bar's Open. That can change how EOSC, FlatEOD and same-bar exit+reverse pairs resolve (D3), and so can change the count. With only 1-minute imported data, High may have no finer series to use (INFERRED).
5. **ExitMode = OppBand in run 1.** For a long, OppBand `stop = curUpper ≤ max(curUpper, VWAP)` (lines 208–209), so OppBand exits **less** often and should give **fewer** trades. That matches the paper's 1.3 vs 1.8 trades/day (spec line 38). Run 1 had **more** trades, and the property default is BandOrVWAP (line 118), so a reset would not produce this. Low.
6. **Entries per direction / Entry handling.** Entry names are fixed (`L`/`S`), and lines 226/228 block same-direction re-entry, so changing these mostly does nothing. They could alter how the same-bar exit+reverse resolves. Low.
7. **Price based on Bid/Ask instead of Last.** Imported NQCONT is Last-only (REPORTED "Last"), so the result would be no data or different data. The count would collapse rather than land at 48. Low.
8. **Bar type/value not Minute 1.** The `mod` mapping and σ store break, and line 133 prints a warning. Amear would likely have noticed. Low.
9. **Bars required to trade.** Default 20 bars (line 112) is dwarfed by the 14-session band warm-up, so only an extreme value matters. Low.
10. **Break at EOD.** Negligible for Minute bars (INFERRED). Low.
11. **Contracts / Set order quantity.** These change quantity, not count. Near zero.
12. **Slippage / commission.** **Zero effect on count**, per the null-search above.

### NT8 readback that would settle it (not resolved here)
- **Run 1 settings, if the result is still listed in the Analyzer:** Trading hours · Exit on session close (+ seconds) · Time in force · Order fill resolution · Slippage · Include commission · Start/End date · Price based on · Type/Value · Break at EOD · ExitMode · Contracts · Entries per direction · Entry handling · Bars required to trade · Set order quantity. Whether NT8 keeps prior Analyzer results with their settings is UNVERIFIED.
- **If run 1 is gone:** re-run run 2's settings changing one field at a time, in order: Trading hours = `<Use instrument settings>`, Exit on session close = off, Order fill resolution = High. Stop when 48 trades / $225.64 / $0 commission reproduces.
- **Run 2 Trades tab:** the Exit-name tally, Exit-time vs Entry-date checks, and Qty > 1 check from D2(c) and D3.
- **Instrument and template:** `Tools > Instruments > NQCONT` → the Trading hours field, plus the point value check above. `Tools > Trading Hours > CME US Index Futures RTH` → the printed session and holiday hours (closes the TODO at reference line 156).

---

## Other findings (reported, not fixed; out of scope)
- **Wrong comment, line 36:** "NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick)". NQ is $20/point, $5/tick (the docs' point-value hits above). No code reads it (OBSERVED: no point-value token in the code), so it is cosmetic, but it misleads readers.
- **Dead code:** `Close1600` is written but never read (OBSERVED). The `(CurrentBar >= 1)` guard at line 155 is always true (OBSERVED).
- **Naming/fidelity question for D1's owner:** the code's OppBand long stop is `curUpper` (line 209; comment line 45: "same-side band the breakout came through"). Spec line 59 calls the base stop the "**opposite** Noise-Area boundary". This is not graded here.

## Files staged
None. The brief forbids `git add`. One new untracked file was written: `docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md`.

## Result
**PASS** for the analysis deliverable. All three parts are answered with pasted evidence:
- D2(c) is graded **CANNOT-DETERMINE-STATICALLY**, with readbacks named.
- D3's double-close is **CANNOT-DETERMINE-STATICALLY**, with readbacks named.
- D4 is **not resolved**: the hypotheses are ranked and labelled INFERRED.

## Post-adversarial corrections (manager-adjudicated, 2026-10-30)

- **C1 (F1, MAJOR). "Every reversal submits an explicit exit and a reverse entry on the same bar" is INFERRED, not OBSERVED.** What is OBSERVED in code (lines 205–229) is that whenever the reverse-entry condition holds, the exit condition also holds in the same OnBarUpdate. Worker 4 confirmed this by fuzzing a python port: 0 of 305,112 reversal cases lacked the exit condition (worker 4 report). Two premises are INFERRED NT8 runtime behaviour: that `Position.MarketPosition` still reads Long at line 228, and that NT8 then submits both orders. So the conclusion is INFERRED.
- **C2 (F2, MAJOR). The run-2 commission identity does not discriminate the reversal outcomes.** $121.36 = 41 × $2.96 = 82 × $1.48 shows only that commission was charged on 82 contract-sides. A double-close booked as extra Qty-1 rows also gives rows × $2.96. If that happened, the 41-trade count is itself inflated. The identity is evidence neither for nor against outcomes (i)–(iii). Nor is it recorded whether Amear read $121.36 off the screen or the figure was computed as 41 × 2.96 (the notes print it as "$121.36 (= 41 × 2.96)").

```
$ sed -n '36,40p' docs/reports/2026-10-28-voice-session-notes.md
| Run | Range | Trades | Net profit | Commission | Profit factor | Max drawdown |
|---|---|---|---|---|---|---|
| 1 (settings not verified; may have reset) | 2026-04-01 → 2026-07-17 | 48 | $225.64 | $0 (not included) | — | — |
| 2 (all fields read back by Amear) | 2026-04-01 → 2026-07-17 | 41 | $599.08 | $121.36 (= 41 × 2.96) | — | — |
| 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | **1,075** | **$1,281.61** | — | **1.04** | **$4,051.57** |
```

- **C3 (F3). Slippage condition 1, restated.** Every Trades row is Qty 1, with two fills (entry and exit). If double-closes are booked as extra rows, the per-row formula still holds, but the 1,075 may include spurious rows. Tick size 0.25 comes from the same NQCONT instrument definition as the point value, and whether NT8 honours it on a non-Future instrument type is equally UNVERIFIED.
- **C4 (F4). Missing hypothesis and readback field: Instrument.** Run 1 may have run on a different instrument or data series, such as a dated NQ contract with partial data (INFERRED). That would change the count by an unbounded amount. Add "Instrument (exact name shown in the Analyzer's left panel)" to the run-1 readback list.
- **C5 (F5). Missing scenario S5 for D2(c).** The template's printed hours were never captured (reference line 156). If the session ends after 16:00 ET, `mod >= 960` re-fires FlattenAll on the 16:01+ bars, and FlatEOD fills the same day at the 16:01 bar's Open (INFERRED). Amear's "16:00 bar followed by 9:31" contradicts this only for the one date he read (2026-07-17). Also, the "S4 least likely" ranking has no evidence behind it: treat S1–S5 as unranked.
- **C6 (F6). D4 #5.** The paper's 1.3 vs 1.8 trades/day is NOT corroboration for the code's OppBand mode, because the code's OppBand stop is the same-side band, not the paper's opposite band. The conclusion "OppBand gives fewer trades than BandOrVWAP" rests on the code-level argument plus worker 4's path fuzz (0 of 200,000 violations). It is INFERRED for NT8 fills.
- **C7 (F7). Missing evidence, now pasted.** P3 shows the TraceOrders count. P4 is a reproducible checkpoint enumeration that replaces the placeholder command.

```
$ /usr/bin/grep -c TraceOrders ninjascript/PraxisNoiseAreaBreakout.cs
0
```

```
$ python3 -c "print([f'{m//60:02d}:{m%60:02d}' for m in range(571,960) if m%60 in (0,30)])"
['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30']
```

- **C8 (F8). The counts 56 and 20 were captured before the other 2026-10-30 reports existed.** A re-run now also counts those reports, including this one: an observer effect. The original figures are left unedited.

```
$ /usr/bin/grep -rniI 'managed approach\|next bar\|ExitOnSessionClose\|exit on session close\|slippage' docs/ | wc -l
     175
$ /usr/bin/grep -rniI --exclude='2026-10-30-*' 'managed approach\|next bar\|ExitOnSessionClose\|exit on session close\|slippage' docs/ | wc -l
      56
$ /usr/bin/grep -rniI 'point value' docs/ | wc -l
      58
$ /usr/bin/grep -rniI --exclude='2026-10-30-*' 'point value' docs/ | wc -l
      20
```

WORKER STATUS: COMPLETE
