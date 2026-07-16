# B2 — Noise-Area Breakout Strategy: Implementation Report (bead Praxis_build-4uu)

**Project:** PRAXIS | **Date:** 2026-07-16 | **Bead:** Praxis_build-4uu (b2-signal-repro)
**Artifact:** `ninjascript/PraxisNoiseAreaBreakout.cs` (new NT8 Strategy, C#/.NET 4.8)
**Authoritative source:** `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (Zarattini/Aziz/Barbon, SSRN 4824172 / SFI RP 24-97, 3-Feb-2025).
**Trader locks (DECISION_LOG 2026-07-16, session 16):** 16:00 ET flat; reverse-on-opposite-cross; pure paper replication with FIXED params (Lookback=14, band=1×σ, no ATR stop); ExitMode is the only knob.

> Cannot compile on Mac — the NT8 compiler is on the Win11 VM. Code is written compile-intended; §B below is the VM compile+reconcile gate.

---

## A. Rule-by-rule traceability

| Code block (PraxisNoiseAreaBreakout.cs) | Implements | Spec § / paper page |
|---|---|---|
| `Calculate = Calculate.OnBarClose` (SetDefaults) | No look-ahead — σ reads only closed bars | §1; guard-rail |
| `Lookback` = `private const int 14` (not an Input; not optimizable) | 14-day fixed lookback | §1/§3 p.6 |
| `BandSigmaMult` = `private const double 1.0` (not an Input; not optimizable) | Band half-width = 1×σ, no free multiplier | §1 p.7 / §5 D1 |
| `ExitMode` enum default `BandOrVWAP` | Selectable exit; paper-preferred default | §4 p.13 / §6 param-map |
| `BuildBand()` — `sumAbs += Abs(c/rec.Open − 1)`, `/cnt` | σ = 14-day mean absolute move-from-open at that minute-of-day | §1 steps 1–2, pp.6–7 |
| `BuildBand()` — `Max/Min(todayOpen, prevClose)·(1 ± k·σ)` | Overnight-gap-adjusted Upper/Lower bounds | §1 step 3 p.7 |
| `history` = completed days only; `CommitDay()` on first bar of session | σ never sees the in-progress day (no look-ahead) | §1; guard-rail |
| Per-bar `today.Closes[mod] = Close[0]`; `mod = H*60+M` | Minute-of-day close store keyed to session-elapsed time | §1; §6 note |
| VWAP accum reset on `IsFirstBarOfSession`; typical-price×vol | Session VWAP, RTH-only, anchored 09:30 | §4 p.13 fn.2 |
| `isCheckpoint = (min==0 || min==30) && OpenMod<mod<CloseMod` | Act only at HH:00 / HH:30 stamps | §2 p.9 |
| `price > curUpper → EnterLong`; `price < curLower → EnterShort` | Long above band / short below band | §2 p.9 |
| `Position.MarketPosition != Long/Short` guard on entries → NT8 managed reverse | Reverse & re-enter on opposite-band cross | §2 p.9; trader lock |
| Long stop `Max(curUpper, curVwap)`; Short `Min(curLower, curVwap)`; evaluated only at checkpoint | Trailing stop = band-or-VWAP (whichever tighter), at the stamp | §4 p.9,13 |
| `ExitMode==OppBand` → stop = band only | Base "Stop @ Opp. Band" variant | §4 p.9 / Table 1 |
| `mod >= CloseMod → FlattenAll(); return` | 16:00 ET cash-close flat, no new entry at/after close | §4 p.9,12; trader lock |
| No ATR field; no profit target | Paper has neither | §3 p.50 / §5 D10 |
| `Contracts` input (sizing only, comment) | Fixed sizing; paper's 2% vol-target NOT ported | §3 p.15 (noted as out-of-scope) |

---

## B. VM compile + reconcile checklist (Win11 NT8)

1. **Import/compile.** Copy `PraxisNoiseAreaBreakout.cs` into `Documents\NinjaTrader 8\bin\Custom\Strategies\`. Open NinjaScript Editor → Compile (F5). Fix any errors, re-sync the file back to the repo, re-audit.
2. **Data.** Load the b2-data NQ **1-minute** series (per `2026-07-15 b2-data` acquisition spec). Confirm the chart/Analyzer uses an **RTH 09:30–16:00 ET** session template — the band math assumes it.
3. **Strategy Analyzer run.** Add `PraxisNoiseAreaBreakout` on NQ 1-min, RTH template. Only ExitMode and Contracts are Inputs (leave at BandOrVWAP, 1); Lookback=14 and σ-mult=1.0 are compiled-in consts, not shown/optimizable in the Analyzer. Backtest ≥ 3 months so σ has ≥14 warm-up days.
4. **Band visual check.** Chart the run; the three plots (UpperBound/LowerBound/SessionVWAP) should form a band that **widens through the day** and re-anchors each 09:30 (paper Fig.1 p.8). VWAP should start at the open and be RTH-only.
5. **Signal reconcile.** Pull a sample of known live/sim TradingView Noise-Area alerts (n8n outbox / signal journal). For each, confirm: (a) the strategy's entry fires on the **same HH:00/HH:30 stamp**; (b) direction matches (long above / short below); (c) an opposite-band cross **reverses** rather than just exiting; (d) every day is **flat by 16:00**. Log deltas.
6. **Stamp-vs-fill divergence.** NT8 fills managed market entries at the **next bar's open**, whereas the paper acts *at* the stamp price. Quantify the per-trade slippage vs the stamp Close; if material, consider a stop-market-at-boundary realization (spec §6 p.99 flags this) — but that is a separate decision, not this pass.
7. **Trade-frequency sanity.** Paper reports ~1.3 trades/day (OppBand) → ~1.8 (BandOrVWAP), Table 4 p.16 — **for SPY full-day**. NQ counts will differ (instrument + reversal cadence); use as an order-of-magnitude tripwire, not a pass/fail.

---

## C. Assumptions & things I was unsure of

- **Bar timestamping.** Assumed NT8 1-min bars are **close-stamped** (RTH first bar ≈ 09:31 whose `Open[0]` is the 09:30 open; the 16:00-stamped bar is the session's last). If this install is open-stamped, the minute-of-day mapping and `prevClose = Close[1]` shift by one bar — verify in step 4/5.
- **`prevClose` source.** Taken as `Close[1]` on the first bar of a session (= prior session's last/16:00 bar). Robust once ≥1 session of warm-up exists; the very first session falls back to `todayOpen` (band symmetric that day).
- **Full-sample σ requirement.** `BuildBand()` requires a **complete `Lookback` sample** for the exact minute-of-day, else it skips trading that checkpoint. This is stricter than "average whatever is available" and means early-close/holiday minutes-of-day may not trade until 14 clean samples exist. Conservative and faithful to the fixed-N paper; flag if the trader wants graceful degradation.
- **Reversal via NT8 managed reverse.** `EnterLong` while short auto-closes and flips (EntriesPerDirection=1, AllEntries). I did NOT hand-code Exit+Enter for reversals. The same-side trailing stop (`ExitLong/ExitShort`) is what takes a position to *flat*; the opposite-band cross is what *reverses*. On a bar where a long both stops out and price is below Lower, the pre-fill `Position.MarketPosition` still reads Long so the short reversal fires — intended, but confirm fill behavior in the Analyzer trade list.
- **VWAP definition.** Typical-price ((H+L+C)/3) × volume, cumulative from 09:30. Paper says "VWAP … market-hours only, anchored at the 09:30 open" (fn.2 p.13) without pinning the price proxy; typical-price VWAP is the standard reading. Swap to close-based if the reference feed differs.
- **Sizing / vol-target NOT ported.** Paper's `σ_target=2%`, 4× cap sizing (§3 p.15) is out of scope for a pure signal-replication pass; fixed `Contracts` used. Flagged, not implemented.
- **Session-flat mechanism.** Explicit `mod >= 16:00 → flatten` is primary; `IsExitOnSessionCloseStrategy=true` (30s) is a backstop. On a strict RTH template these coincide; on a template extending past 16:00 the explicit check governs.

---

*End report. Code on disk at `ninjascript/PraxisNoiseAreaBreakout.cs`; not compiled on Mac (no NT8 toolchain).*
