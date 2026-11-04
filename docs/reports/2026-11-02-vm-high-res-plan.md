# High fill-resolution plan (VM side) — 2026-11-02

Written by Claude Code on the VM (VMware, Windows 11 ARM64, NinjaTrader 8.1.8.4) under Amear's ruling R-VN3-2. **Plan only.** Nothing was bought, imported, run or changed in NinjaTrader to write it.

**Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Grades: **OBSERVED** = run or read on this VM and the result seen · **INFERRED** = reasoned, not run · **REPORTED BY AMEAR** = his words · **REPORTED (source)** = a vendor page, forum post or the Mac handoff · **UNVERIFIED** = not yet checked.

---

## 1. What High resolution needs

### 1.1 Analyzer fields: locked Standard vs proposed High

| Field | Locked 0-S value | High value (spec F3 line) | Grade |
|---|---|---|---|
| Order fill resolution | Standard (Fastest) | **High** | OBSERVED (0-S snapshot in `strategyanalyzerlogs`) |
| Fill-resolution type | Minute | **Tick** | OBSERVED (0-S) / spec |
| Fill-resolution value | 1 | **1** | OBSERVED (0-S) / spec |
| Slippage (ticks/side) | 2 | **1** per the spec line; **2** for the 0-H control (§5) | OBSERVED (0-S) / spec |
| Commission | PRAXIS, $2.96 round trip | unchanged | OBSERVED (all 1,190 trades show $2.96) |
| Everything else (instrument, Last, Minute 1, 2021-03-08 → 2026-07-17, CME US Index Futures RTH, Break at EOD, max bars 256, bars required 20, fill limit on touch off, 1 entry/direction, exit on session close, DAY, BandOrVWAP, 1 contract) | as in C4 | unchanged | REPORTED BY AMEAR (C4 screenshot readback) |

### 1.2 What NinjaTrader needs underneath
- **Tick data for the instrument.** NT8 can't build a Tick series from imported 1-minute data. `db\tick` on this VM has 0 files today. OBSERVED.
- **Single-series strategies.** High can't be used with `AddDataSeries` or Tick Replay. The Praxis strategies (Baseline, OppBand, Flat1559) are single-series with no `AddDataSeries`. OBSERVED (source read 2026-11-01) / docs.
- **No backfill.** NT's servers keep about 1 year of ticks, and a custom name like `NQCONTROW` returns "Unknown instrument". The ticks must be imported. REPORTED (NT forum / help guide); the server limit is UNVERIFIED here.
- **Slippage under High: risk.** An NT staff forum post says slippage applies only under Standard. If that's true, a High run silently drops 2 ticks/side. That is the **F3 void-clause trigger**: if it is seen, F3 goes back to Amear. REPORTED (forum); UNVERIFIED on 8.1.8.4.
- **Allowed fill types on a 1-min primary.** The help guide doesn't list them. Staff reported a "bleedover" error with Tick 2 on a 1-min primary. Checking that Tick 1 can be picked is a 2-minute look at the dropdown, with no run. REPORTED (forum); UNVERIFIED.

### 1.3 The judged run is not this plan's run
R-VN3-5/6: the judged version is High resolution **with the circuit breakers on**. Breaker definitions wait for bead `r8j`. Every High run described here is a **measurement run** (fill-optimism gap and data checks), not the go/no-go run. No breaker logic and no pass gates are proposed. REPORTED (Mac handoff).

---

## 2. Data (option C: Portara per-contract ticks)

REPORTED BY AMEAR (button answers in this VM session): "Portara NT-format", then "Adjust per-contract myself".

| Item | Value | Grade |
|---|---|---|
| Product | Portara/CQG, NinjaTrader-format, trades-only ticks, **individual contract files** | REPORTED (portaracqg.com, read 2026-11-02) |
| Contracts needed | **23**: NQ 03-21 through NQ 09-26 (every quarterly contract active between 2021-03-07 and 2026-07-20, the span of the 1-min file) | OBSERVED (`nt-implied-offsets.csv`, file span) |
| Date range | 2021-03-07 → 2026-07-20 (file). The test window is 2021-03-08 → 2026-07-17. | OBSERVED |
| **Price** | **$695 flat, 2014 → present.** Per year is $125 with a $500 minimum, counted back from today, so reaching March 2021 costs 6 × $125 = **$750**. Flat is cheaper. | REPORTED (Portara pricing pages) |
| Expected size | Portara lists E-mini Nasdaq at 56.8 GB for full history (zipped or not isn't stated). For this window: **~10–25 GB** of text, from an assumed 200k–500k trades/day (no published figure). | REPORTED / INFERRED |
| Disk | C: has **98.3 GB free**. | OBSERVED (2026-11-02) |
| Time stamps | 7-digit fractional seconds; local or exchange time on request. **Ask for US Eastern** to match the 1-min file and the VM. TickPrep also takes `--tz-in UTC`. | REPORTED (Portara) / OBSERVED (TickPrep self-test, UTC = Eastern result) |
| Licence | Not published. **Ask** whether personal backtesting use is allowed. | UNVERIFIED |
| Delivery | Method and lead time not published. **Ask.** | UNVERIFIED |
| Free sample | Ask for March 2021 (it has the 2021-03-14 DST change and the March roll). | INFERRED |

**Question for Amear (purchase):** buy Portara ENQ trades-only ticks, individual NinjaTrader-format contract files, US Eastern, 2014 → present, for **$695**? Send the questions in §6 first.

---

## 3. Build chain (after purchase and Amear's OK; not run on real data)

Tool: `praxis-tickprep` (`TickPrep.cs`, SHA-256 `104dc9d9…6545`, identical on the VM and the Mac). Self-test on synthetic data passed (offsets 3400 / 3390.25 / 3380.5 recovered; 99,705/99,705 bars matched; UTC = Eastern). OBSERVED on the VM 2026-11-02; on the Mac it is REPORTED.

| Step | Command | Acceptance |
|---|---|---|
| 0 | Write `contracts.csv` (23 lines, names as in `nt-implied-offsets.csv`). | All 23 paths exist. |
| 1 | `TickPrep measure "<1-min>" contracts.csv <out> [--tz-in UTC]` | (a) Each contract's measured offset **equals** `nt-implied-offsets.csv` (e.g. NQ 06-21 = 3342.75, NQ 09-26 = 0). (b) `report.txt` unmatched minutes inside the covered span: every one listed and explained. (c) Segment order follows the roll dates. |
| 1b | If (a) fails for any contract | **Stop.** Report to Amear. Rerunning with `--offsets` to force NT's values is a choice for him, not a default. |
| 2 | `TickPrep build "<1-min>" contracts.csv <out> "<out>\NQCONTROW 09-25.Last.txt"` | No "out of time order" error (contract runs don't interleave). The tick count is reported. Strict: minutes missing from the 1-min file get no ticks (R-VN3-3). |
| 3 | `TickPrep verify "<1-min>" "<tick file>"` | Exit code 0: zero OHLC differences, zero bars only in ticks. Volume differences are reported but not a failure. |

**Edge cases**
- **2021-06-10 cut-short roll (241 bars).** Only minutes present in the 1-min file are written, so the day stays cut short in the tick file. That's the same behaviour as the self-test, which covered this roll. INFERRED / OBSERVED (synthetic).
- **The two 17-day holes** sit on the NQ 12-21 roll (2021-09-09) and the NQ 03-26 roll (2025-12-15). They stay empty (R-VN3-3). OBSERVED (file) / REPORTED BY AMEAR ("I would just proceed as it is").
- **DST.** US clock changes happen at 02:00 on Sunday while CME Globex is closed (it reopens Sunday 18:00 ET), so Eastern stamps have no repeated or skipped trading hour. With `--tz-in UTC`, conversion is per hour through Windows' Eastern zone. INFERRED / OBSERVED (synthetic span crossed 2021-03-14).
- **Tick time zone.** Ask Portara for US Eastern. If they deliver UTC or Central, pass `--tz-in UTC` (UTC only; Central would need a code change, a question for Amear first). INFERRED.

---

## 4. The instrument and how a tick import would sit (plan only, no import)

- Target: **`NQCONTROW 09-25`**, the Future row ($20/pt, tick 0.25, rollover 2021-03-01, Do not merge). These values are REPORTED (Mac handoff). The VM's last read of the database showed one rollover (09-25 on 2025-12-01) **before** Amear's fix, which hasn't been re-read since (C7 is still owed). UNVERIFIED.
- NT stores ticks in `db\tick\<instrument>\` and minutes in `db\minute\<instrument>\`. A Last tick import writes only to `db\tick`, so the existing minute data isn't touched. Layout: OBSERVED (`db\minute\NQCONTROW 09-25` exists; `db\tick` is empty). Import behaviour: INFERRED.
- **Safeguards in the plan:**
  1. Copy `db\minute\NQCONTROW 09-25` and record SHA-256 for every file before any import.
  2. Pilot with one month first (§5, P1).
  3. After import, re-hash the minute files. They must be **identical**, otherwise stop.
  4. Rerun 0-S (R0). It must reproduce 1,190 trades and $197,327.60 exactly. This also shows NT still builds the 1-min primary from minute data, not from ticks, which matters because the strategy's VWAP uses volume and tick volumes may differ.
- Import dialog (when approved): Tools → Import → Historical Data, NinjaTrader format, Data type Last, Time zone = whatever the tick file is in (Eastern). INFERRED.

---

## 5. The 0-H control (design only)

Purpose: measure the fill-optimism gap by changing **one thing**.

| Step | Run | Change from 0-S | Stop checks |
|---|---|---|---|
| P0 | Sample month, no import | none | TickPrep measure/build/verify pass on the March 2021 sample. |
| P1 | One-month import (March 2021) | import only | Minute-file hashes unchanged; 0-S on that month unchanged; one High run on the month to time it, measure memory, and see whether slippage is applied. |
| R0 | 0-S, full range, after full import | none | 1,190 trades, $197,327.60, total slippage 1190. Exact. |
| **R1** | **0-H** | Order fill resolution = High, Tick 1. **Slippage stays 2.** | Total slippage must still read 1190. If not, stop: F3 void clause, back to Amear. |
| R2 | Spec High | R1 plus slippage = 1 | Only if R1 passes. |
| R3–R4 | OppBand, Flat1559 at High | as R1 (and R2 if wanted) | Same checks. |

Report for R1 vs R0: trade count, number of trades whose entry or exit price changed, net, PF, max DD, and per-exit-type differences (XS / XL / session close). Last-Half-Hour Momentum is **not included** (R-VN3-1).

**Memory risk.** 16 GB RAM (OBSERVED), x64 NinjaTrader under ARM emulation, 5.4 years of ticks: a full-range High run may not fit. Fallbacks: year-by-year runs with lookback overlap, or a 1-second fill series (a departure from the spec). Both are Amear's call. INFERRED.
**Runtime:** no basis yet. Time P1 and scale it up.

---

## 6. Risks and open questions for Amear

**Risks**
1. Slippage may be ignored under High, which would trigger F3. REPORTED (forum).
2. The measured offsets might not equal NT's (the 1-min file's source isn't proven). INFERRED: implied raw prices matched on spot checks.
3. Importing ticks could change how NT builds the 1-min primary. R0 catches this.
4. A full-range High run could run out of memory.
5. The Portara licence is unknown.

**Questions to send Portara (Amear sends them)**
1. What roll dates and back-adjustment method does the continuous ENQ file use?
2. Do individual contract files cover the whole contract life or only the front-month window?
3. Are Eastern stamps DST-aware and at trade time?
4. What is the delivered size for ENQ 2014 → now, zipped and unzipped?
5. Are ticks filtered or cleaned?
6. Does the licence allow personal backtesting?
7. How is the data delivered, and how long does it take?
8. Can we have a free March 2021 sample?

**Open questions for Amear**
1. Buy Portara ENQ ticks for $695 (after the answers above)?
2. Where did the 1-min file come from? If it's NinjaTrader's `NQ ##-##` back-adjusted series, the offsets in `nt-implied-offsets.csv` are the expected answer.
3. If any measured offset differs from NT's, stop there, or force NT's values with `--offsets`?
4. Approve P1 (one-month import) once the sample passes?
5. R2: add the 1-tick-slippage spec run after the 0-H control?
6. Is "Baseline-H" a separate run from 0-H, or the same?
7. Memory fallback: year-by-year runs or a 1-second fill series?
8. Should the `.exe` files go into the repo, or source only with the rebuild command?
9. Should the High measurement runs wait for `r8j` (breakers), or go ahead as measurement-only?
