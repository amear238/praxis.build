# Run 3 — Strategy Analyzer Summary, transcribed from Amear's screenshot

**Recorded:** 2026-10-30T22:17Z by praxis-master. **Grade of every value below: OBSERVED BY THE MASTER in the image Amear pasted into this session.** The master did not see the VM; Amear did. Nothing here validates the trades — it records what the Analyzer displayed.
**Evidence:** `docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp` — 111,376 bytes, sha256 `8787483dcb41fbc0d52c023faeb32ff3606075a8fa518126749b1a4da90eac55` (hashed from the session image before copying; same bytes).
**Window:** NinjaTrader 8 Strategy Analyzer, Display = `Summary ($)`, tab `Analyzer`, label `template` at the lower right of the Settings pane. Windows taskbar clock `6:12 PM 2026-10-30`, `13°C Partly sunny`. A small `Trend` slider box floats over the results pane (dropped per Amear's 2026-10-28 ruling; noted only).
**Related:** `docs/reports/2026-10-28-voice-session-notes.md:29-44` (the voice-side record of runs 1–3); `docs/reports/2026-10-30-3gm-fidelity-check.md` (code fidelity, audit strike one at the time of writing).

## Settings pane (right), top to bottom

| Group | Field | Value |
|---|---|---|
| General | Backtest type | Backtest |
| General | Strategy | PraxisNoiseAreaBreakout |
| 02. Praxis (tunable) | Exit mode (ONLY tunab…) | BandOrVWAP |
| 02. Praxis (tunable) | Contracts | 1 |
| Data Series | Instrument | NQCONT |
| Data Series | Price based on | Last |
| Data Series | Type | Minute |
| Data Series | Value | 1 |
| Time frame | Start date | 2021-03-08 |
| Time frame | End date | 2026-07-17 |
| Time frame | Trading hours | **CME FX Futures RTH** |
| Time frame | Break at EOD | ☑ |
| Setup | Include commission | ☑ |
| Setup | Commission template | PRAXIS |
| Setup | Maximum bars look back | 256 |
| Setup | Bars required to trade | 20 |
| Historical fill processing | Order fill resolution | Standard (Fastest) |
| Historical fill processing | Fill limit orders on touch | ☐ |
| Historical fill processing | Slippage | 2 |
| Order handling | Entries per direction | 1 |
| Order handling | Entry handling | All entries |
| Order handling | Exit on session close | ☑ |
| Order properties | Set order quantity | Strategy |
| Order properties | Time in force | DAY |

## Performance table (left)

| Performance | All trades | Long trades | Short trades |
|---|---|---|---|
| Total net profit | $1,281.61 | $2,721.21 | −$1,439.60 |
| Gross profit | $35,911.01 | $17,606.91 | $18,304.10 |
| Gross loss | −$34,629.40 | −$14,885.70 | −$19,743.70 |
| Commission | $3,182.00 | $1,545.12 | $1,636.88 |
| Profit factor | 1.04 | 1.18 | 0.93 |
| Max. drawdown | −$4,051.57 | −$1,713.82 | −$3,179.91 |
| Sharpe ratio | 0.07 | 0.23 | −0.10 |
| Sortino ratio | 0.11 | 0.40 | −0.14 |
| Ulcer index | 0.06 | 0.02 | 0.08 |
| R squared | 0.38 | 0.82 | 0.49 |
| Total Fees | $0.00 | $0.00 | $0.00 |
| Probability | 26.82% | 3.61% | 76.03% |
| Start date / time | 2021-03-08 12:00 AM | | |
| End date / time | 2026-07-17 12:00 AM | | |
| Total # of trades | 1075 | 522 | 553 |
| Percent profitable | 38.05% | 43.87% | 32.55% |
| # of winning trades | 409 | 229 | 180 |
| # of losing trades | 666 | 293 | 373 |
| # of even trades | 0 | 0 | 0 |
| Total slippage | **43** | 20.88 | 22.12 |
| Avg. trade | $1.19 | $5.21 | −$2.60 |
| Avg. winning trade | $87.80 | $76.89 | $101.69 |
| Avg. losing trade | −$52.00 | −$50.80 | −$52.93 |
| Ratio avg. win / avg. loss | 1.69 | 1.51 | 1.92 |
| Max. consec. winners | 7 | 8 | 5 |
| Max. consec. losers | 17 | 11 | 16 |
| Largest winning trade | $580.25 | $373.00 | $580.25 |
| Largest losing trade | −$319.25 | −$318.00 | −$319.25 |
| Avg. # of trades per day | 0.81 | 0.39 | 0.42 |
| Avg. time in market | 106.49 min | 115.65 min | 97.84 min |
| Avg. bars in trade | 106.48 | 115.64 | 97.83 |
| Profit per month | $20.22 | $42.96 | −$22.88 |
| Max. time to recover | 606.94 days | 427.00 days | 1813.94 days |
| Longest flat period | 20.88 days | 30.94 days | 34.98 days |
| Avg. MAE | $52.13 | $47.73 | $56.27 |
| Avg. MFE | $72.06 | $64.90 | $78.82 |
| Avg. ETD | $70.87 | $59.69 | $81.42 |

## Arithmetic checks (master, this session)

```
$ python3 -c "print(35911.01-34629.40, 1075*2.96, 409/1075, 1075*2*2*5, 1075*2*2*0.25)"
1281.6100000000006 3182.0 0.38046511627906976 21500 1075.0
```

- Net $1,281.61 = gross profit − gross loss exactly → commission is already netted inside the per-trade figures, not deducted afterwards.
- Commission $3,182.00 = 1,075 × $2.96 → every trade carries one round turn at the PRAXIS template rate; consistent with Qty-1 trades and two fills each.
- 409 / 1,075 = 38.05% ✓.
- 0.81 trades/day over 2021-03-08 → 2026-07-17 is consistent with 1,075 trades (≈1,330 trading days). The paper's SPY figure is 1.3–1.8/day — an order-of-magnitude tripwire only (3gm report, checklist §B.7).

## Two discrepancies with the voice-side notes — recorded, NOT diagnosed

**(A) Trading hours = `CME FX Futures RTH`.** The notes (`:33`) report the saved template "Praxis Backtest" as `trading hours CME US Index Futures RTH`. The screenshot shows a different template selected for the run on screen. The code hard-codes a 09:30–16:00 ET session (`ninjascript/PraxisNoiseAreaBreakout.cs` lines 58, 189, 196) and takes `todayOpen`, `prevClose`, the VWAP reset and the 16:00 flatten from NT8's session boundaries, so the template decides what the strategy actually anchored on. **The FX template's session hours are UNVERIFIED in this repo.** Whether this run is the same configuration as run 2, and whether the "unknown instrument" and bar-time checks were done under this template, is NOT KNOWN. This is the 3gm report's D4 hypothesis #1 — template drift between runs — appearing in run 3's own settings. **Falsifier / readback (Amear):** `Tools > Trading Hours`, open `CME FX Futures RTH` and `CME US Index Futures RTH`, read each one's session rows; then read which one the saved "Praxis Backtest" template actually stores.

**(B) Total slippage = 43 (long 20.88, short 22.12).** The 3gm report's D3 upper bound for 2 ticks on every fill of 1,075 trades is 4,300 ticks = 1,075 points = $21,500. 43 matches none of those units, and the long/short split is non-integer, so the cell is not a tick count. What NT8's Summary "Total slippage" measures (and in what unit, under `Summary ($)`) is UNVERIFIED. No inference is drawn about whether slippage was applied. **Readback (Amear):** one run-3 trade from the Trades tab — entry price vs the next bar's Open on the chart — and the NT8 Help entry for the Summary's "Total slippage" row.

## What this record does and does not change

- Run 3's **settings and summary** move from REPORTED (notes) to OBSERVED (this image). The trades, fills, template hours and data coverage from 2021-03-08 remain unobserved.
- The F3 ruling (`[N]` = 2 ticks/side, Standard) is consistent with the Slippage 2 / Standard (Fastest) fields shown.
- Amear's hold on the walk-forward stands. Nothing here lifts or extends it.

## Addendum 2026-10-30T22:40Z — RUN 3 RULED INVALID by Amear; run 4 supersedes it (REPORTED)

Appended by praxis-master after the body above was written. The body stands unedited as the transcription of what the Analyzer displayed.

**Amear's ruling (DECISION_LOG `2026-10-30T22:22:00Z`; `docs/reports/2026-10-28-voice-session-notes.md:45-60`):** discrepancy (A) was real. Run 3 ran on `CME FX Futures RTH`. The strategy anchors on `Bars.IsFirstBarOfSession` for a 09:30 ET session (`ninjascript/PraxisNoiseAreaBreakout.cs:37`, `:147-152`), so the open anchor, prior close, VWAP anchor and 16:00 flat sat on the wrong bars. **Run 3 is recorded as INVALID, not as a result.** The saved "Praxis Backtest" default template carried the same error; Amear corrected the trading hours to `CME US Index Futures RTH`, changed nothing else, re-ran, and re-saved the template.

**Run 4 — first valid full-history run. Grade: REPORTED BY AMEAR from his screenshot; no Claude has seen the image.**
2021-03-08 → 2026-07-17 · NQCONT 1-min · BandOrVWAP · 1 contract · Slippage 2 · Standard · PRAXIS commission · trading hours `CME US Index Futures RTH`.
1,211 trades (584 L / 627 S) · net $3,136.84 · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 · avg trade $2.59 · longs +$4,541.40 / shorts −$1,404.56 · largest winner $1,792.50 · total slippage 48.44.

```
$ python3 -c "print(1075*4/100, 1211*4/100, 1211*2.96, 41447.47-38310.63, 4541.40-1404.56, 1211*4*5, 1792.50/3136.84, 3136.84/1211)"
43.0 48.44 3584.56 3136.840000000004 3136.8399999999997 24220 0.5714349472717767 2.5902890173410404
```

- Commission = 1,211 × $2.96 ✓. Net = gross profit − gross loss ✓ = longs + shorts ✓. Avg trade $2.59 ✓. Largest winner = 57% of net.
- **Discrepancy (B) re-read with two data points:** total slippage = trades × 4 / 100 in both runs (43.00 and 48.44 — exact). Amear's reading: 2 ticks on every entry and every exit (4 ticks per round trip) shown in an unfamiliar unit; if so ≈ $24,220 slippage on run 4 and ≈ $30.9k gross before all costs. **The unit is UNCONFIRMED.** The voice-side "≈$21.5k / ≈$26k" estimate from run 3 and the later "slippage may not be applied" note are both withdrawn by Amear. Confirming the unit, and that slippage lands on every market fill, is a queued follow-up (bead `Praxis_build-3gm` notes) — from sources on disk, else UNVERIFIED with a readback named.
- `[N]` = 2 ticks/side stays locked; it was set before results.

**Open for the follow-up unit:** why the short side loses (−$1,404.56 on 627 trades) while longs win (+$4,541.40 on 584) — a code-level symmetry read of the long and short paths, labelled INFERRED, since no trade list has reached this repo.
