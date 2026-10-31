# 7zq M2 hand-test checklist — PraxisLastHalfHourMomentum (new strategy)

**Unit:** Praxis_build-7zq M2 (worker 3) · 2026-10-31 · for Amear, Fusion VM, NT8 8.1.7.2. **Nothing here was compiled or run;**
every "expected" line is INFERRED, and your screen wins. Grades: OBSERVED · INFERRED · REPORTED BY AMEAR · UNVERIFIED · SPEC-SILENT.
**Rule (Baltussen, Da, Lammers & Martens 2021, JFE 142, 377–403, `η(r_ROD)`):** at the close of the 15:30 bar,
r = Close(15:30) / Close(most recent 16:00-stamped bar of a prior session) − 1. If r > 0, go long (`LHMomLong`); otherwise (r = 0 too), go short (`LHMomShort`).
Flatten on the 15:59 bar (`LHFlat1559`). One trade per weekday session with a bar in [15:30, 15:59); none on Sat/Sun bars. No such bar (early close) means no trade.

## 1 — Install and compile
1. Copy `PraxisLastHalfHourMomentum.cs` into `Documents\NinjaTrader 8\bin\Custom\Strategies\`.
2. `New > NinjaScript Editor`, press **F5**. Clean (no error rows, strategy in the list): ☐
3. **If the compile fails, STOP.** Write down the exact error text: code (e.g. CS0103), file, line, column. **Do not fix it on the VM.**
   NT8 compiles every file together (`docs/reference/2026-07-24-nt8-windows-reference.md:130`), so move this file out and F5 again
   to get the others compiling. Error text: ______________________________________________

## 2 — Strategy Analyzer settings (run 4's)
**FIRST: confirm the template. Trading hours = `CME US Index Futures RTH`** (run 3 was INVALID on `CME FX Futures RTH`,
`docs/reports/2026-10-28-voice-session-notes.md:47`). Look at the field itself. Don't trust the saved template.
REPORTED BY AMEAR (voice notes, untracked): `:52` "Settings are the same as run 3 except **Trading hours = CME US Index Futures
RTH**". Run 3 = "full history, same settings" (`:40`) = the `:33` settings + `:32` commission template; `:48` Exit on session close ✓.
**Time in force DAY is NOT in the notes.** It is from DECISION_LOG `2026-10-30T22:17:00Z` (run-3 screenshot: "Time in force DAY").

| Field | Value | Source | ☐ |
|---|---|---|---|
| Strategy | **PraxisLastHalfHourMomentum** | this unit | ☐ |
| Instrument · Price based on · Type/Value | NQCONT · Last · Minute 1 | `:33` | ☐ |
| Start → End | 2021-03-08 → 2026-07-17 | `:40`, `:53` | ☐ |
| Trading hours | CME US Index Futures RTH | `:52` | ☐ |
| Contracts | 1 (the only input) | `:33` | ☐ |
| Include commission | ✓, template PRAXIS ($1.48/side) | `:32`, `:33` | ☐ |
| Slippage · Order fill resolution | 2 · Standard | `:33` | ☐ |
| Exit on session close · Time in force | ✓ · DAY | `:48` · 22:17:00Z row | ☐ |

## 3 — EXPECTED (every line INFERRED)
- **Trades ≤ 1,304, fewer if the template drops sessions; more would be a defect (phantom weekend trades).** From the import file
  (OBSERVED, manager's `m2-sessions.py`): 1,352 weekday sessions in range, 1,305 with a 15:30 bar; minus the first (no prior 16:00 close).
- **Entries at ~15:31** (fill = Open of the 15:31 bar). **Every exit named `LHFlat1559`, at the 16:00 bar** (fill = that bar's Open, ≈15:59). **Hold ≈ 29 min.**
- **Long/short mix** = sign of the prior-close→15:30 return. It probably leans long, but it can't be predicted. **Expect neither side near 0%.**
- **Zero `LHStaleFlat` and zero `Exit on session close` exits.** If either name appears at all, it is a defect. Report it.
- **Costs (cost model `config/backtest-cost-model.json`: $2.96/round turn, tick $5):** commission ≈ trades × $2.96
  ≤ 1,304 × 2.96 = **$3,859.84**. Slippage ≈ trades × 4 ticks × $5 ≤ 1,304 × $20 = **$26,080**.
  NT's "Total slippage" figure ≈ trades × 4 / 100 ≤ **52.16** (the pattern from runs 3/4, `:54`; unit unconfirmed).
- **Net: no prediction.** The paper is gross of costs ("we do not consider transaction costs", p. 386). Its results are for an
  equity-futures portfolio, not NQ alone. Its NQ sample ends 2020-05-01, so **2021-03 → 2026-07 is entirely out-of-sample.**

## 4 — WHAT TO READ BACK
| Readback | Value |
|---|---|
| Total trades · Long / Short | ____ · ____ / ____ |
| Net profit · Gross profit · Gross loss | ____ · ____ · ____ |
| Commission · Profit factor · Max drawdown · Total slippage | ____ · ____ · ____ · ____ |
| Trades tab: exit names counted (LHFlat1559 / LHStaleFlat / Exit on session close / other) | ____ |
| Exit times: any not at the 16:00 bar? (count + first date) | ____ |
| Entry times: any not 15:31? (count + first date) | ____ |
| One trade: date · entry fill vs **Open of 15:31 bar** (Data Box) · exit fill vs **Open of 16:00 bar** (INFERRED: buy ≈ 2 ticks above, sell ≈ 2 below) | ____ |
| Any day with an entry but no 15:30 bar (e.g. an early-close date)? | ____ |
| Chart/Data Box, a regular day (e.g. 2026-07-16): last bar stamp (expect 16:00; if 17:00, report it — DECISION_LOG:365) · first bar stamp (expect 09:31) | ____ · ____ |
| **Defect check:** any entry on a Saturday/Sunday, or any r using a 13:00 holiday-session price (e.g. 2024-01-16, day after MLK: prior close should be 2024-01-12 16:00)? Report count + first date | ____ |

**Limitations:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
This is not a backtest report; F3 stays FROZEN until one carries that sentence. Open questions: `docs/reports/2026-10-31-7zq-m2-decisions-addendum.md` § NEEDS AMEAR.
