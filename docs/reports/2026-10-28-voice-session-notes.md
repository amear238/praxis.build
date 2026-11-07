# 2026-10-28 — Voice session notes (Amear, by hand)

Written by Claude from a voice/chat session. This is a record for the Claude Code session to pick up.
It is not an audited report. Whatever Amear said is recorded as his ruling. Whatever he saw on screen is recorded as reported by him.

## Amear's rulings
1. **The in-VM automation approach is dropped.** No more Cowork or in-VM Claude Code executor work. Amear builds the rest of the project by hand, and Claude gives him steps one at a time.
2. **The "Trend" box item is dropped.** It will not be investigated.
3. **F3 `[N]` = 2 ticks per side** band-edge slippage. That is $10 per side, which with $2.96 commission comes to about $22.96 per round trip. It was chosen before any backtest output was seen, as his 2026-08-29T00:10:00Z ruling requires. A later stress run at 3 ticks is allowed and does not change the locked number. **Still to do:** record this in DECISION_LOG and DECISIONS.md, commit the F3 artifact, and update `config/backtest-cost-model.json` (slippage 2/side, fill_resolution Standard) with its DECISIONS entry.
4. **The NT8 8.1.8.4 update is skipped for now.** Stay on 8.1.7.2 until the backtest runs clean.
5. **The 2026-10-26 nightly-checks review note is on hold.** It will not be sent.

## Git (typed by Amear)
- `efcf690` pushed. The 11 untracked a20 files were committed by pathspec and pushed. The 9-path carried staged set was confirmed untouched (count = 9).
- The 10-26 review-note draft in `/private/tmp/...scratchpad/` no longer exists ("No such file"). Its content survives in `docs/reports/2026-10-26-nightly-spec-request-review.md`.

## NQCONT chart on Fusion (reported by Amear)
- A 1-minute chart of `NQCONT`, title showing plain `NQCONT` (no expiry), with the default recent-days load: **blank**.
- The same chart with Data Series set to **Custom range 2026-06-01 → 2026-06-30**: **candles render**.
- Reading: the long-running "blank chart" is at least partly a date-range effect. The imported series ends in July 2026, so a default load of recent days requests bars that don't exist. The bar timestamps have not been checked yet. The "unknown instrument NQCONT" Strategy Analyzer defect has not been re-tested yet.

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

## 2026-10-30 18:14 — Correction from Amear's screenshot of the run-3 Summary
- **Run 3 is INVALID. Trading hours were set to `CME FX Futures RTH`, not `CME US Index Futures RTH`.** The strategy depends on an RTH session that opens at 09:30 ET. `PraxisNoiseAreaBreakout.cs:37` says so, and `:147-152` set the session anchor `todayOpen = Open[0]` on `Bars.IsFirstBarOfSession`. With the wrong template, the open anchor, the previous close, the VWAP anchor and the 16:00 flat all land on the wrong bars. The "Praxis Backtest" default template saved earlier carries the same wrong setting.
- Other values read from the screenshot: gross profit $35,911.01 · gross loss −$34,629.40 · commission $3,182.00 · PF 1.04 · max DD −$4,051.57 · 1,075 trades (522 long / 553 short) · **Total slippage 43** (NT8 shows no unit) · Max bars look back 256 · Bars required 20 · Break at EOD ✓ · Exit on session close ✓ · Fill limit on touch ☐.
- **The earlier slippage estimate is withdrawn.** The claim of "≈$21,500 slippage, ≈$26k gross before costs" was wrong. NT8 reports total slippage of 43, far below 2 ticks on every fill, even though every order in the code is a market order (`EnterLong`/`EnterShort`/`ExitLong`/`ExitShort`). Net + commission = $4,463.61 before commission. Whether NT8 is actually applying the 2-tick slippage is an open question for the fidelity check.

## 2026-10-30 ~18:20 — Run 4 (the first valid full-history run; numbers from Amear's screenshot)
- Settings are the same as run 3 except **Trading hours = CME US Index Futures RTH**. Amear is re-saving the "Praxis Backtest" default template with the corrected session.
- 2021-03-08 → 2026-07-17 · **1,211 trades** (584 long / 627 short) · **net $3,136.84** · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 (= 1,211 × 2.96 ✓) · **PF 1.08** · **max DD −$4,108.84** · avg trade $2.59 · longs +$4,541.40 / shorts −$1,404.56 · largest winner $1,792.50 · total slippage 48.44.
- Slippage arithmetic (Claude's, unit unconfirmed): total slippage = trades × 4 / 100 in both runs (1,075 → 43.00; 1,211 → 48.44). This fits 2 ticks on every entry and exit (4 ticks per round trip), shown in an unusual unit. If so, slippage ≈ 1,211 × 4 × $5 ≈ $24,220, and gross before all costs ≈ $30.9k. This supersedes the 18:14 note's suggestion that slippage might not be applied.
- The single largest winner ($1,792.50) is more than half of net profit.
- Verdict held pending the fidelity check. The walk-forward is held. Slippage stays at 2 ticks (locked before results).
---
*Addendum by unit 2026-11-07-rulings-filing-correction-1 (S13 house style; not part of Amear's notes; DECISION_LOG 2026-11-07T13:36:00Z): Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.*
