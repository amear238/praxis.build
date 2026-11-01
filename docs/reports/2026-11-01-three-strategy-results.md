# Three-strategy results readback - 2026-11-01

- Unit: `2026-11-01-three-strategy-results`
- Authorisation: the two DECISION_LOG rows stamped 2026-11-01T13:07:23Z (the master's dispatch row, and the `WHO: amear` row with rulings R-1101-1..6).
- Author: Claude Code (praxis-manager unit, workers).
- Status: NOT audited at the time of writing.

Stated limitation:

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

This report does not grade F3, and it makes no claim that F3 is unfrozen; that needs an auditor grade. F2 (FROZEN): the early-close findings are only recorded here. No trading-hours template or session-flat rule is changed, proposed or decided. No strategy code or config was changed (Amear's brief). The report states facts and open questions only. Per R-1101-5 it gives no ranking of the strategies and no verdict between them.

## Evidence grades

- **OBSERVED**: read in data or command output in this session. Every value from a CSV or the bar file is OBSERVED, and the appendix holds the command and its output.
- **INFERRED**: reasoned from observed facts. The basis is stated each time.
- **REPORTED BY AMEAR**: values from Amear's screenshots or his notes. The screenshot values were transcribed from his images by worker A and checked by the manager. This writer did not open the images.
- **UNVERIFIED**: not checked in this session.

Appendix references look like `[K03]`. Every command in the appendix was re-run from cwd `/` with `zsh -c`, exactly as pasted, and its fresh output is pasted under it.

## Inputs

All seven files are on Amear's Desktop. They are read-only and were not copied, moved or modified (R-1101-6 default: cite path + sha256, no copies). [K01] OBSERVED:

| file | role | sha256 |
|---|---|---|
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentum grid | `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9` |
| `/Users/admin/Desktop/Screenshot 2026-11-01 at 7.57.06 AM.png` (U+202F before AM) | OppBand Summary($) + Settings | `7ea26c0dd07904be0e4d95853f31a92de5d09f4f87f941f153706cabd1674fb2` |
| `/Users/admin/Desktop/Screenshot 2026-11-01 at 7.58.40 AM.png` (U+202F before AM) | Flat1559 Summary($) + Settings | `237c0e7150ad28600ffc6fa30e18cc8adafb43ebf5539813a7c7d21e54da8413` |
| `/Users/admin/Desktop/Screenshot 2026-11-01 at 8.00.21 AM.png` (U+202F before AM) | LastHalfHourMomentum Summary($) + Settings | `fca590ccb570cd6bcf24cac80492cebe6242d4f1f03f9806b9fa2ccf6297db5f` |

- No baseline screenshot exists. The baseline's settings and totals rest on Amear's C4 notes in `docs/reports/2026-10-31-voice-session-notes-2.md` section 3 (REPORTED BY AMEAR).
- Bar file: `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt`, 1857362 lines [K01] (OBSERVED).
- **Hash cross-check against the master's 13:07Z list: all four CSV hashes MATCH in full** [K01] (OBSERVED for the files). The master's dispatch brief to this unit (not a repo file) lists `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd`, `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8`, `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` and `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9`. The master recorded the screenshots by prefix only (`7ea26c0d`, `237c0e71`, `fca590cc`), and those prefixes match [K01].
- Scripts: every script used is session scratch under `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/` and is **not in the repo**. Their sha256 values are in [K02] (OBSERVED). `screens.txt` is worker A's hand transcription of the Summary($) values (REPORTED BY AMEAR).
- Mapping from each CSV's `Strategy` column, all rows, [K03] `[1] Strategy` (OBSERVED): 07-10 = `PraxisNoiseAreaBreakout` (1190 rows), 07-57 = `PraxisNoiseAreaBreakout_OppBand` (810), 07-59 = `PraxisNoiseAreaBreakout_Flat1559` (1190), 08-00 = `PraxisLastHalfHourMomentum` (1304). Instrument `NQCONTROW SEP25` and Account `Backtest` on every row.

## Bar-file clock

The bar file's time zone was not given, so it was established empirically before any bar-based check used it.

- **Offset test** [K10] (OBSERVED): baseline + Flat1559 entries (n=2380) were compared with the OPEN of the bar stamped at the entry time shifted by -3h..+3h. At offset +0h, 2338 are 2 ticks adverse, 18 are 1 tick adverse and 24 are exact, with 0 "other" and 0 "nobar". The split is the same in DST (1572: 1544 / 12 / 16) and non-DST (808: 794 / 6 / 8). At every other offset the "other" column holds at least 2086 of 2380.
- **Daily break** [K10] (OBSERVED): the most frequent intraday gap is last stamp 1700 -> first stamp 1801. It occurs 704 times on DST dates and 317 times on non-DST dates, at the same stamps in both.
- **Volume profile** [K11] (OBSERVED): on weekdays the largest mean 1-minute volumes are at stamps 1600 (DST 7439 / non-DST 7538) and 0931 (4959 / 5092), against 0930 (915 / 940). The same stamps lead in both DST and non-DST.
- **Conclusion (INFERRED** from the three facts above): the bar file and the grid CSVs use the same clock (offset 0), and that clock follows DST. The bars are end-stamped: the volume spike sits on the 09:31 stamp, not the 09:30 one. The identification as **US Eastern** wall time rests on general market-hours knowledge: cash open 09:30 ET, cash close 16:00 ET, CME daily halt 17:00-18:00 ET. That part is **UNVERIFIED** against an exchange document in this session. The NT8 platform time-zone setting is UNVERIFIED.
- **Entry fill pattern** (OBSERVED): in baseline and Flat1559, every entry fill equals `clamp(open of the entry-stamped bar + 0.50 adverse, bar low, bar high)`: 1190 match / 0 no-match in each [K12, Item 1d]. Across all four CSVs (1190 + 810 + 1190 + 1304 entries [K03]), the adverse residual against that bar's OPEN is 0.50 on 4304, 0.25 on 78, 0.00 on 72 and -0.00 on 40 [K13]. Every fill with less than 0.50 adverse slip equals the bar's adverse extreme [K14]. Every LastHalfHourMomentum fill that is not open +/- 2 ticks (218 of entries + exits) equals the bar high for a buy or the bar low for a sell [K15]. Plain words: in this data, slippage is 2 ticks adverse from the bar open, clipped to the bar's range. No claim is made about how NT8 implements that.

## Data holes (shared by all four runs)

- **Two whole-day holes, NEW** [K20] (OBSERVED): `2021-09-09 19:59 -> 2021-09-27 00:01` (gap 17 days, 4:02) and `2025-12-14 18:59 -> 2026-01-01 18:01` (gap 17 days, 23:02).
- **48 weekdays with no bar stamped 09:31..16:00** [K16 first line, K19] (OBSERVED). No CSV has a trade on any of them: 48 of 48 have `trades=[]` [K19]. They include the hole dates. The dates that still have some bars are listed in [K19]. Nine of them fall near the quarterly contract roll (INFERRED from timing): 2021-06-10, 2021-12-09, 2022-03-10, 2022-06-09, 2022-09-08, 2024-12-16, 2025-03-17, 2025-09-15, 2026-06-12. The roll link is INFERRED from the Mar/Jun/Sep/Dec timing only, and the holiday identity of the other dates is INFERRED from calendar knowledge.
- **The holes sit inside the 14-day lookback** of the NoiseAreaBreakout sessions right after them. INFERRED from the dates. The effect on the bands was **not analysed**.
- **Known gaps are wider than recorded** [K18] (OBSERVED; s2's own KNOWN/NEW tags in [K16] are wrong for these three, so this uses s3):
  - "2024-07-19 10:01" is really 10 missing RTH stamps, 09:58-10:07.
  - "2024-08-02 12:01" is really 8 stamps, 11:55-12:02.
  - "2026-07-17 11:01-12:01" is really 68 stamps, 10:59-12:06.
  - 2023-04-05 matches its description: 117 missing RTH stamps, 14:04-16:00.
- Missing stamps inside sessions, whole range: 184 stamps in 67 runs [K16]. 51 of those runs are on 2021-03-08..10 [K17], before the first NoiseAreaBreakout trade (2021-03-29 [K03 `[1] date span`]).

## Baseline re-derivation (07-10 CSV vs Amear's C4 values)

[K05] (CSV = OBSERVED; the `amear=` values are REPORTED BY AMEAR, from his C4 Summary and the C5 exit-name readback in notes-2 section 3): **all 22 compared values MATCH**. They are trades 1190, L 556 / S 634, net $197327.60, gross profit $878467.36, gross loss -$681139.76, commission $3522.40, PF 1.29, max DD -$45282.04 (both methods), avg trade $165.82, avg win $1815.02, avg loss -$964.79, W/L/E 484/706/0, largest win $35887.04, largest loss -$5407.96, long net $136314.24, short net $61013.36, and the exit counts Exit on session close 429, XS 429, XL 332. The CSV has no exit name outside that list.

Baseline CSV totals [K03] (OBSERVED):

| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 1190 | $197327.60 | $878467.36 | -$681139.76 | $3522.40 | 1.29 | 484/706/0 | 40.67% | $35887.04 | -$5407.96 | $165.82 | -$45282.04 | -$45282.04 |
| Long | 556 | $136314.24 | $414160.00 | -$277845.76 | $1645.76 | 1.49 | 250/306/0 | 44.96% | $35887.04 | -$4457.96 | $245.17 | -$27173.72 | -$27173.72 |
| Short | 634 | $61013.36 | $464307.36 | -$403294.00 | $1876.64 | 1.15 | 234/400/0 | 36.91% | $15802.04 | -$5407.96 | $96.24 | -$38498.00 | -$38498.00 |

Max DD here is closed-trade cumulative net. Method (i) takes the peak from 0 and method (ii) the peak from the first trade, and the two give identical values. Baseline commission: 0 rows != $2.96; sum $3522.40 == 1190 x 2.96 [K03 `[4]`]. Baseline session-close exits fill at the CLOSE of the 16:00-stamped bar +/- 2 ticks: clamp model 423 of 423 [K12] (OBSERVED).

## Run 1: OppBand (`PraxisNoiseAreaBreakout_OppBand`, 07-57 CSV, screenshot 7.57.06)

### a. Settings vs the required list

| field | required (C4 line [K23]) | shown (screenshot, REPORTED BY AMEAR) | status |
|---|---|---|---|
| Backtest type | not in the C4 line | Backtest | no requirement listed |
| Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
| Price based on / Type / Value | Last / Minute / 1 | Last / Minute / 1 | MATCH |
| Date range | 2021-03-08 -> 2026-07-17 | 2021-03-08 -> 2026-07-17 | MATCH |
| Trading hours | CME US Index Futures RTH | CME US Index Futures RTH | MATCH |
| Break at EOD | checked | checked | MATCH |
| Include commission | checked | checked | MATCH |
| Commission template | PRAXIS | PRAXIS | MATCH |
| Maximum bars look back | 256 | 256 | MATCH |
| Bars required to trade | 20 | 20 | MATCH |
| Order fill resolution | Standard (Fastest) | Standard (Fastest) | MATCH |
| Fill limit orders on touch | unchecked | unchecked | MATCH |
| Slippage | 2 | 2 | MATCH |
| Entries per direction | 1 | 1 | MATCH |
| Entry handling | All entries | All entries | MATCH |
| Exit on session close | checked | checked | MATCH |
| Set order quantity | Strategy | Strategy | MATCH |
| Time in force | DAY | DAY | MATCH |
| Exit mode | code default `OppBand` (`PraxisNoiseAreaBreakout_OppBand.cs:141` [K21]) | OppBand | MATCH |
| Contracts | 1 (code default `:142` [K21]) | 1 | MATCH |
| commission rate inside PRAXIS | $2.96 per round trip (unit brief) | not shown | NOT SHOWN |
| full strategy name | `PraxisNoiseAreaBreakout_OppBand` | prefix `PraxisNoiseAreaBreakout_Opp` (dropdown truncated) | NOT SHOWN |

Grades for the table above: the "shown" column is REPORTED BY AMEAR. Worker A transcribed it from his screenshot, the manager checked it, and this writer did not open the image. The "required" column is the C4 settings line in notes-2 line 111 [K23] (REPORTED BY AMEAR). For the strategy's own options, R-1101-4 makes the code default the requirement, and the defaults are cited from the **repo** source [K21]. The installed VM copies were not hash-checked (R-1101-1), so whether they carry the same defaults is UNVERIFIED. The status column compares those two lists. The screenshot also shows Display = Summary ($).

**R-1101-4 test: 0 mismatches among the fields shown -> VALID on the shown fields; NOT SHOWN: the commission rate inside the PRAXIS template, and the full strategy name.** The NOT SHOWN items are not upgraded to pass. CSV facts that bear on them, OBSERVED, given separately: the Commission column is $2.96 on every row (0 rows differ) [K03 `[4]`], and the Strategy column reads `PraxisNoiseAreaBreakout_OppBand` on all 810 rows [K03 `[1]`].

### b. Totals from the CSV (OBSERVED, [K03])

| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 810 | $210182.40 | $1009483.80 | -$799301.40 | $2397.60 | 1.26 | 470/340/0 | 58.02% | $36087.04 | -$19592.96 | $259.48 | -$50748.88 | -$50748.88 |
| Long | 404 | $138454.16 | $484987.24 | -$346533.08 | $1195.84 | 1.40 | 256/148/0 | 63.37% | $36087.04 | -$19592.96 | $342.71 | -$27645.64 | -$27645.64 |
| Short | 406 | $71728.24 | $524496.56 | -$452768.32 | $1201.76 | 1.16 | 214/192/0 | 52.71% | $15802.04 | -$10477.96 | $176.67 | -$51652.92 | -$51652.92 |

- Max DD is closed-trade cumulative net, and methods (i) and (ii) give identical values. **It equals NT8's Max. drawdown in all 3 OppBand cells** (All/Long/Short; NT8 values REPORTED BY AMEAR) [K06], and in all 9 cells across the three runs. This states the CSV method only. NT8's own drawdown method is not documented here and is not asserted.
- Screenshot reconciliation (Summary($) values REPORTED BY AMEAR, [K07]): 48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE. The 3 MISMATCH are "Avg. bars in trade": shown 291.45 / 290.22 / 292.68 against CSV means 292.45 / 291.22 / 293.68, so shown = CSV mean - 1.00 [K06]. The 3 NOT DERIVABLE are "Total slippage": shown 810 / 404 / 406, which equal the trade counts, but the CSV has no slippage column [K06].

### c. Commission (OBSERVED, [K03 `[4]`])

- Rows with Commission != $2.96: 0. Sum $2397.60 == 810 x 2.96 (True).
- Rows with any Clearing / Exchange / IP / NFA fee != $0.00: 0.
- The negative test of this check is in the manager report and is not repeated here.

### d. Exit names, counts and exit time of day (OBSERVED, [K03 `[5]`])

- Entry names: S 406, L 404.
- Exit names: Exit on session close 792, XL 10, XS 8. **No `FlatEOD` exit appears.** The repo source has `ExitLong("FlatEOD")` / `ExitShort("FlatEOD")` at `PraxisNoiseAreaBreakout_OppBand.cs:314/316` [K21].
- Exit on session close by time: 16:00 784, 12:15 5, 12:00 2, 14:03 1. XL and XS exits are spread over 7 distinct times each [K03].
- Session-close fill reference [K13]: on the 784 16:00-stamped session-close exits, the fill is within 0.50 of the **CLOSE** of the 16:00-stamped bar on 784 of 784, and within 0.50 of that bar's OPEN on 33.

### e. Qty, duplicates, overlaps (OBSERVED, [K03 `[6]`])

Qty != 1: 0. Duplicate entry times: none. Overlapping positions (next entry before this exit): 0. A same-timestamp exit followed by an entry happens 18 times, with first examples (16, 17), (27, 28).

### f. Early-close and short-session exits (OBSERVED, [K24])

| date | last RTH bar that day | trade # | side | entry -> exit | exit name | Bars |
|---|---|---|---|---|---|---|
| 2021-11-26 | 13:15 | #90 | Short | 11:01 -> 12:15 | Exit on session close | 75 |
| 2023-04-05 | 14:03 | #312 | Short | 10:01 -> 14:03 | Exit on session close | 243 |
| 2024-07-03 | 13:15 | #514 | Long | 11:01 -> 12:15 | Exit on session close | 75 |
| 2024-11-29 | 13:15 | #576 | Long | 11:31 -> 12:15 | Exit on session close | 45 |
| 2024-12-24 | 13:15 | #583 | Long | 10:01 -> 12:15 | Exit on session close | 135 |
| 2025-01-20 | 13:00 | #594 | Long | 10:01 -> 12:00 | Exit on session close | 120 |
| 2025-06-19 | 13:00 | #652 | Short | 10:01 -> 12:00 | Exit on session close | 120 |
| 2025-07-03 | 13:15 | #657 | Long | 10:01 -> 12:15 | Exit on session close | 135 |

- 2023-04-05 at 14:03: the day's last RTH bar is 14:03 and the next bar is 20:01 [K15] (OBSERVED). That this is a data gap and not an early close is INFERRED (the date is on the known-gap list [K18]).
- The two 12:00 exits (2025-01-20, 2025-06-19) are on sessions whose bar data runs to 13:00 [K24]. On those dates the baseline and Flat1559 had already left by XL / XS [K24].

### g. Trades touching data gaps (OBSERVED, [K16] and [K18])

- Trades with a missing stamp between entry and exit [K16]: 6 of 810.
  - #205: 2022-08-03 11:26 (NEW)
  - #525: 2024-07-25 10:43-10:45 and 10:48-10:49 (NEW)
  - #529: 2024-08-02 11:55-12:02. s2 tags it NEW, but it is the KNOWN 2024-08-02 gap, wider than recorded [K18].
  - #546: 2024-09-19 13:55-13:57 (NEW)
  - #700: 2025-10-13 13:51 (NEW)
  - #800: 2026-06-11 10:33-10:44 (NEW)
- On 2024-08-02, the 12:00 decision stamp and the 12:01 fill stamp are both missing while #529 is open [K16].
- On 2023-04-05, #312 exits at 14:03 with Exit on session close, the last bar before the known gap [K18]. INFERRED: the gap set its exit time.
- On 2024-07-19, #523 enters at 10:31, after the 09:58-10:07 gap [K18].
- The whole-day holes, the 48 no-RTH weekdays (no trades) and the wider known gaps are in "Data holes" above.

### h. First 5 / last 5 trades (OBSERVED, [K04])

| set | # | side | entry -> exit | entry/exit price | entry -> exit name | profit | Bars |
|---|---|---|---|---|---|---|---|
| first 5 | 1 | Short | 2021-03-29 10:01 -> 16:00 | 16270.25/16371.00 | S -> Exit on session close | -$2017.96 | 360 |
| first 5 | 2 | Long | 2021-03-31 10:01 -> 16:00 | 16468.50/16504.00 | L -> Exit on session close | $707.04 | 360 |
| first 5 | 3 | Long | 2021-04-05 10:01 -> 16:00 | 16892.50/16998.50 | L -> Exit on session close | $2117.04 | 360 |
| first 5 | 4 | Long | 2021-04-13 10:01 -> 16:00 | 17358.00/17391.25 | L -> Exit on session close | $662.04 | 360 |
| first 5 | 5 | Short | 2021-04-14 11:31 -> 16:00 | 17296.50/17223.75 | S -> Exit on session close | $1452.04 | 270 |
| last 5 | 806 | Short | 2026-07-01 11:01 -> 16:00 | 30192.50/30081.75 | S -> Exit on session close | $2212.04 | 300 |
| last 5 | 807 | Short | 2026-07-02 11:01 -> 16:00 | 29839.75/29536.50 | S -> Exit on session close | $6062.04 | 300 |
| last 5 | 808 | Short | 2026-07-07 10:01 -> 16:00 | 29468.25/29393.00 | S -> Exit on session close | $1502.04 | 360 |
| last 5 | 809 | Long | 2026-07-14 11:31 -> 16:00 | 29885.50/29787.25 | L -> Exit on session close | -$1967.96 | 270 |
| last 5 | 810 | Short | 2026-07-15 11:01 -> 16:00 | 29631.50/29701.00 | S -> Exit on session close | -$1392.96 | 300 |

## Run 2: Flat1559 (`PraxisNoiseAreaBreakout_Flat1559`, 07-59 CSV, screenshot 7.58.40)

### a. Settings vs the required list

| field | required (C4 line [K23]) | shown (screenshot, REPORTED BY AMEAR) | status |
|---|---|---|---|
| Backtest type | not in the C4 line | Backtest | no requirement listed |
| Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
| Price based on / Type / Value | Last / Minute / 1 | Last / Minute / 1 | MATCH |
| Date range | 2021-03-08 -> 2026-07-17 | 2021-03-08 -> 2026-07-17 | MATCH |
| Trading hours | CME US Index Futures RTH | CME US Index Futures RTH | MATCH |
| Break at EOD | checked | checked | MATCH |
| Include commission | checked | checked | MATCH |
| Commission template | PRAXIS | PRAXIS | MATCH |
| Maximum bars look back | 256 | 256 | MATCH |
| Bars required to trade | 20 | 20 | MATCH |
| Order fill resolution | Standard (Fastest) | Standard (Fastest) | MATCH |
| Fill limit orders on touch | unchecked | unchecked | MATCH |
| Slippage | 2 | 2 | MATCH |
| Entries per direction | 1 | 1 | MATCH |
| Entry handling | All entries | All entries | MATCH |
| Exit on session close | checked | checked | MATCH |
| Set order quantity | Strategy | Strategy | MATCH |
| Time in force | DAY | DAY | MATCH |
| Exit mode | code default `BandOrVWAP` (`PraxisNoiseAreaBreakout_Flat1559.cs:151` [K21]) | BandOrVWAP | MATCH |
| Contracts | 1 (code default `:152` [K21]) | 1 | MATCH |
| commission rate inside PRAXIS | $2.96 per round trip (unit brief) | not shown | NOT SHOWN |
| full strategy name | `PraxisNoiseAreaBreakout_Flat1559` | prefix `PraxisNoiseAreaBreakout_Flat` (dropdown truncated) | NOT SHOWN |

Grades for the table above: the "shown" column is REPORTED BY AMEAR. Worker A transcribed it from his screenshot, the manager checked it, and this writer did not open the image. The "required" column is the C4 settings line in notes-2 line 111 [K23] (REPORTED BY AMEAR). For the strategy's own options, R-1101-4 makes the code default the requirement, and the defaults are cited from the **repo** source [K21]. The installed VM copies were not hash-checked (R-1101-1), so whether they carry the same defaults is UNVERIFIED. The status column compares those two lists. The screenshot also shows Display = Summary ($).

**R-1101-4 test: 0 mismatches among the fields shown -> VALID on the shown fields; NOT SHOWN: the commission rate inside the PRAXIS template, and the full strategy name.** The NOT SHOWN items are not upgraded to pass. CSV facts that bear on them, OBSERVED, given separately: the Commission column is $2.96 on every row (0 rows differ) [K03 `[4]`], and the Strategy column reads `PraxisNoiseAreaBreakout_Flat1559` on all 1190 rows [K03 `[1]`].

### b. Totals from the CSV (OBSERVED, [K03])

| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 1190 | $193017.60 | $871258.28 | -$678240.68 | $3522.40 | 1.28 | 482/708/0 | 40.50% | $36472.04 | -$5407.96 | $162.20 | -$40637.04 | -$40637.04 |
| Long | 556 | $138509.24 | $416257.96 | -$277748.72 | $1645.76 | 1.50 | 249/307/0 | 44.78% | $36472.04 | -$4457.96 | $249.12 | -$23774.12 | -$23774.12 |
| Short | 634 | $54508.36 | $455000.32 | -$400491.96 | $1876.64 | 1.14 | 233/401/0 | 36.75% | $15742.04 | -$5407.96 | $85.98 | -$38778.00 | -$38778.00 |

- Max DD is closed-trade cumulative net, and methods (i) and (ii) give identical values. **It equals NT8's Max. drawdown in all 3 Flat1559 cells** (All/Long/Short; NT8 values REPORTED BY AMEAR) [K06]. This states the CSV method only. NT8's own drawdown method is not documented here and is not asserted.
- Screenshot reconciliation (Summary($) values REPORTED BY AMEAR, [K07]): 48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE. The 3 MISMATCH are "Avg. bars in trade": shown 120.12 / 133.94 / 108.00 against CSV means 121.12 / 134.94 / 109.00, so shown = CSV mean - 1.00 [K06]. The 3 NOT DERIVABLE are "Total slippage": shown 1190 / 556 / 634, which equal the trade counts, but the CSV has no slippage column [K06].

### c. Commission (OBSERVED, [K03 `[4]`])

- Rows with Commission != $2.96: 0. Sum $3522.40 == 1190 x 2.96 (True).
- Rows with any Clearing / Exchange / IP / NFA fee != $0.00: 0.
- The negative test of this check is in the manager report and is not repeated here.

### d. Exit names, counts, exit time of day, and the FlatEOD fill test

- Entry names: S 634, L 556 [K03 `[5]`] (OBSERVED).
- Exit names: XS 429, FlatEOD 423, XL 332, Exit on session close 6 [K03 `[5]`] (OBSERVED).
- FlatEOD by time: 16:00 on all 423. Exit on session close by time: 12:15 5, 14:03 1. XS and XL exits are spread over 11 distinct times each [K03 `[5]`] (OBSERVED).

**FlatEOD fill test** [K12] (OBSERVED). Each FlatEOD exit price is compared with four bar prices. "adv" = adverse to the exit order, "fav" = favourable, in ticks:

| reference | n | exact | adv1t | adv2t | fav1t | fav2t | other | nobar |
|---|---|---|---|---|---|---|---|---|
| bar 16:00 OPEN | 423 | 10 | 11 | 402 | 0 | 0 | 0 | 0 |
| bar 16:00 CLOSE | 423 | 4 | 7 | 5 | 2 | 1 | 404 | 0 |
| bar 15:59 CLOSE | 423 | 29 | 110 | 99 | 8 | 2 | 175 | 0 |
| bar 15:59 OPEN | 423 | 4 | 10 | 11 | 5 | 10 | 383 | 0 |

- Clamp rule `clamp(16:00 OPEN -/+ 0.5 adverse, L, H)`: match **423 of 423**. The same rule on the 16:00 CLOSE: match 5 of 423 [K12].
- Discriminating subset, where the 15:59 CLOSE differs from the 16:00 OPEN: 319 trades. Against the 16:00 OPEN, 0 of them fall in "other"; against the 15:59 CLOSE, 175 do [K12].
- Independent re-derivation [K13]: the FlatEOD fill is within 0.50 of the 16:00-stamped bar's OPEN on 423 of 423, and within 0.50 of its CLOSE on 19.
- **Baseline session-close comparison** [K12] (OBSERVED): the baseline's 423 16:00-stamped `Exit on session close` fills match `clamp(16:00 CLOSE -/+ 0.5 adverse, L, H)` on **423 of 423**, and the same rule on the 16:00 OPEN on 5 of 423.
- **Pairwise difference, Flat1559 vs baseline** [K09, K12 Item 3] (OBSERVED): all 1190 entries are identical (side, entry time, entry price, entry name). 423 rows differ, all of them `Exit on session close` -> `FlatEOD`. Exit time differs on 0 of them and exit price on 418. Direction-signed exit difference in points: zero 5, positive 215, negative 203, sum -215.50, min -68.00, median 0.25, max 38.75. **Sum of the profit difference (Flat1559 - baseline): -$4310.00.** On 397 of 423 pairs, the exit difference equals (16:00 bar OPEN - 16:00 bar CLOSE).
- **Plain words.** The FlatEOD prices equal the OPEN of the 16:00-stamped bar, 2 ticks adverse, clipped to the bar range (OBSERVED). If the bars are end-stamped, that is the price at 15:59:00 wall clock (INFERRED, from the bar-clock section). The baseline's session-close prices equal the CLOSE of the same bar (OBSERVED). The grid records the exit time as 16:00:00 for both [K12], written `4:00:00 PM` on all 423 FlatEOD rows and all 423 16:00 baseline session-close rows [K25] (OBSERVED). The code intends to submit the flat on the 15:59 bar: `FlattenMod = CloseMod - 1` at `PraxisNoiseAreaBreakout_Flat1559.cs:91`, `if (mod >= FlattenMod)` at `:227`, `ExitLong/ExitShort("FlatEOD")` at `:326/:328` [K21]. That the order is in fact submitted on the 15:59 bar close is **UNVERIFIED** in data. No claim is made about NT8 internals.

### e. Qty, duplicates, overlaps (OBSERVED, [K03 `[6]`])

Qty != 1: 0. Duplicate entry times: none. Overlapping positions (next entry before this exit): 0. A same-timestamp exit followed by an entry happens once, (666, 667).

### f. Early-close and short-session exits (OBSERVED, [K24])

| date | last RTH bar that day | trade # | side | entry -> exit | exit name | Bars |
|---|---|---|---|---|---|---|
| 2021-11-26 | 13:15 | #122 | Short | 11:01 -> 12:15 | Exit on session close | 75 |
| 2023-04-05 | 14:03 | #454 | Short | 10:01 -> 14:03 | Exit on session close | 243 |
| 2024-07-03 | 13:15 | #742 | Long | 11:01 -> 12:15 | Exit on session close | 75 |
| 2024-11-29 | 13:15 | #834 | Long | 11:31 -> 12:15 | Exit on session close | 45 |
| 2024-12-24 | 13:15 | #843 | Long | 10:01 -> 12:15 | Exit on session close | 135 |
| 2025-01-20 | 13:00 | #863 | Long | 10:01 -> 10:31 | XL | 31 |
| 2025-06-19 | 13:00 | #955 | Short | 10:01 -> 11:01 | XS | 61 |
| 2025-07-03 | 13:15 | #963 | Long | 10:01 -> 12:15 | Exit on session close | 135 |

- 2023-04-05 at 14:03: the day's last RTH bar is 14:03 and the next bar is 20:01 [K15] (OBSERVED). That this is a data gap and not an early close is INFERRED (the date is on the known-gap list [K18]).
- On the two 13:00 sessions (2025-01-20, 2025-06-19), Flat1559 had left by XL / XS before 12:00 [K24].

### g. Trades touching data gaps (OBSERVED, [K16] and [K18])

- Trades with a missing stamp between entry and exit [K16]: 3 of 1190.
  - #286: 2022-08-03 11:26 (NEW)
  - #763: 2024-08-02 11:55-12:02. s2 tags it NEW, but it is the KNOWN 2024-08-02 gap, wider than recorded [K18].
  - #789: 2024-09-19 13:55-13:57 (NEW)
- On 2024-08-02, the 12:00 decision stamp and the 12:01 fill stamp are both missing while #763 is open [K16].
- On 2023-04-05, #454 exits at 14:03 with Exit on session close, the last bar before the known gap [K18]. INFERRED: the gap set its exit time.
- On 2024-07-19, #754 enters at 10:31, after the 09:58-10:07 gap [K18].
- The whole-day holes, the 48 no-RTH weekdays (no trades) and the wider known gaps are in "Data holes" above.

### h. First 5 / last 5 trades (OBSERVED, [K04])

| set | # | side | entry -> exit | entry/exit price | entry -> exit name | profit | Bars |
|---|---|---|---|---|---|---|---|
| first 5 | 1 | Short | 2021-03-29 10:01 -> 11:31 | 16270.25/16297.25 | S -> XS | -$542.96 | 91 |
| first 5 | 2 | Long | 2021-03-31 10:01 -> 16:00 | 16468.50/16514.75 | L -> FlatEOD | $922.04 | 360 |
| first 5 | 3 | Long | 2021-04-05 10:01 -> 16:00 | 16892.50/16995.25 | L -> FlatEOD | $2052.04 | 360 |
| first 5 | 4 | Long | 2021-04-13 10:01 -> 12:01 | 17358.00/17320.50 | L -> XL | -$752.96 | 121 |
| first 5 | 5 | Long | 2021-04-13 12:31 -> 13:01 | 17327.50/17319.50 | L -> XL | -$162.96 | 31 |
| last 5 | 1186 | Short | 2026-07-07 10:01 -> 12:31 | 29468.25/29532.75 | S -> XS | -$1292.96 | 151 |
| last 5 | 1187 | Short | 2026-07-07 15:31 -> 16:00 | 29320.25/29389.00 | S -> FlatEOD | -$1377.96 | 30 |
| last 5 | 1188 | Long | 2026-07-14 11:31 -> 12:01 | 29885.50/29785.50 | L -> XL | -$2002.96 | 31 |
| last 5 | 1189 | Short | 2026-07-15 11:01 -> 11:31 | 29631.50/29641.25 | S -> XS | -$197.96 | 31 |
| last 5 | 1190 | Short | 2026-07-15 12:01 -> 13:31 | 29579.75/29605.25 | S -> XS | -$512.96 | 91 |

## Run 3: LastHalfHourMomentum (`PraxisLastHalfHourMomentum`, 08-00 CSV, screenshot 8.00.21)

### a. Settings vs the required list

| field | required (C4 line [K23]) | shown (screenshot, REPORTED BY AMEAR) | status |
|---|---|---|---|
| Backtest type | not in the C4 line | Backtest | no requirement listed |
| Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
| Price based on / Type / Value | Last / Minute / 1 | Last / Minute / 1 | MATCH |
| Date range | 2021-03-08 -> 2026-07-17 | 2021-03-08 -> 2026-07-17 | MATCH |
| Trading hours | CME US Index Futures RTH | CME US Index Futures RTH | MATCH |
| Break at EOD | checked | checked | MATCH |
| Include commission | checked | checked | MATCH |
| Commission template | PRAXIS | PRAXIS | MATCH |
| Maximum bars look back | 256 | 256 | MATCH |
| Bars required to trade | 20 | 20 | MATCH |
| Order fill resolution | Standard (Fastest) | Standard (Fastest) | MATCH |
| Fill limit orders on touch | unchecked | unchecked | MATCH |
| Slippage | 2 | 2 | MATCH |
| Entries per direction | 1 | 1 | MATCH |
| Entry handling | All entries | All entries | MATCH |
| Exit on session close | checked | checked | MATCH |
| Set order quantity | Strategy | Strategy | MATCH |
| Time in force | DAY | DAY | MATCH |
| Exit mode | no such option: no `ExitMode =` line matches in `PraxisLastHalfHourMomentum.cs` [K21] | no Exit mode field; Contracts is the only strategy parameter shown | not applicable |
| Contracts | 1 (code default `PraxisLastHalfHourMomentum.cs:155` [K21]) | 1 | MATCH |
| commission rate inside PRAXIS | $2.96 per round trip (unit brief) | not shown | NOT SHOWN |
| full strategy name | `PraxisLastHalfHourMomentum` | `PraxisLastHalfHourMomentum` with the last character clipped (worker A's reading) | NOT SHOWN |

Grades for the table above: the "shown" column is REPORTED BY AMEAR. Worker A transcribed it from his screenshot, the manager checked it, and this writer did not open the image. The "required" column is the C4 settings line in notes-2 line 111 [K23] (REPORTED BY AMEAR). For the strategy's own options, R-1101-4 makes the code default the requirement, and the defaults are cited from the **repo** source [K21]. The installed VM copies were not hash-checked (R-1101-1), so whether they carry the same defaults is UNVERIFIED. The status column compares those two lists. The screenshot also shows Display = Summary ($).

**R-1101-4 test: 0 mismatches among the fields shown -> VALID on the shown fields; NOT SHOWN: the commission rate inside the PRAXIS template, and the full strategy name.** The NOT SHOWN items are not upgraded to pass. CSV facts that bear on them, OBSERVED, given separately: the Commission column is $2.96 on every row (0 rows differ) [K03 `[4]`], and the Strategy column reads `PraxisLastHalfHourMomentum` on all 1304 rows [K03 `[1]`].

### b. Totals from the CSV (OBSERVED, [K03])

| side | trades | net | gross profit | gross loss | commission | PF | W/L/E | % profitable | largest win | largest loss | avg trade | max DD (i) | max DD (ii) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All | 1304 | -$76009.84 | $411326.84 | -$487336.68 | $3859.84 | 0.84 | 621/683/0 | 47.62% | $3852.04 | -$5537.96 | -$58.29 | -$99806.96 | -$99806.96 |
| Long | 698 | -$24736.08 | $195212.48 | -$219948.56 | $2066.08 | 0.89 | 337/361/0 | 48.28% | $3407.04 | -$5537.96 | -$35.44 | -$41000.28 | -$41000.28 |
| Short | 606 | -$51273.76 | $216114.36 | -$267388.12 | $1793.76 | 0.81 | 284/322/0 | 46.86% | $3852.04 | -$5242.96 | -$84.61 | -$77254.32 | -$77254.32 |

- Max DD is closed-trade cumulative net, and methods (i) and (ii) give identical values. **It equals NT8's Max. drawdown in all 3 LastHalfHourMomentum cells** (All/Long/Short; NT8 values REPORTED BY AMEAR) [K06]. This states the CSV method only. NT8's own drawdown method is not documented here and is not asserted.
- Screenshot reconciliation (Summary($) values REPORTED BY AMEAR, [K07]): 48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE. The 3 MISMATCH are "Avg. bars in trade": shown 29.00 / 29.00 / 28.99 against CSV means 30.00 / 30.00 / 29.99, so shown = CSV mean - 1.00 [K06]. The 3 NOT DERIVABLE are "Total slippage": shown 1304 / 698 / 606, which equal the trade counts, but the CSV has no slippage column [K06].

### c. Commission (OBSERVED, [K03 `[4]`])

- Rows with Commission != $2.96: 0. Sum $3859.84 == 1304 x 2.96 (True).
- Rows with any Clearing / Exchange / IP / NFA fee != $0.00: 0.
- The negative test of this check is in the manager report and is not repeated here.

### d. Entry/exit names and times, fill reference, sessions, direction, Bars

- Entry names: LHMomLong 698, LHMomShort 606. Exit names: LHFlat1559 1304 [K03 `[5]`] (OBSERVED). `LHStaleFlat` does not appear as an exit name (0 rows), although the repo source has `ExitLong/ExitShort("LHStaleFlat")` at `PraxisLastHalfHourMomentum.cs:194/200` [K21].
- Entry time of day: 15:31 on all 1304. Exit time of day: 16:00 on all 1304. Trades with entry or exit outside 15:30-16:00 of the same day: 0 [K15] (OBSERVED).
- **LHFlat1559 fill reference** [K13] (OBSERVED): the fill is within 0.50 of the OPEN of the 16:00-stamped bar on 1304 of 1304, and within 0.50 of that bar's CLOSE on 66. The 218 fills (entries + exits) that are not open +/- 2 ticks all equal the bar high for a buy or the bar low for a sell [K15], i.e. clipped to the bar range [K14]. The code sets `FlatMod = 16 * 60 - 1` (the 15:59 bar) at `PraxisLastHalfHourMomentum.cs:127` and exits with `"LHFlat1559"` at `:209/:211` [K21]. That the exit order is submitted on the 15:59 bar is the code's intent and is UNVERIFIED in data.
- **Sessions** [K15] (OBSERVED): 1352 RTH sessions (weekday dates with at least one bar stamped 09:31..16:00), first 2021-03-08, last 2026-07-17. 1304 trades on 1304 distinct dates; no date has more than one trade; no trade date falls outside the session list. Sessions with a trade: 1304. **Sessions with none: 48**, classified as:
  - 1 first session (2021-03-08): no prior 16:00 close in the data;
  - 37 sessions whose last RTH bar is 13:00;
  - 9 sessions whose last RTH bar is 13:15 (early closes: INFERRED from calendar knowledge);
  - 1 session, 2023-04-05, whose last RTH bar is 14:03 (a data gap, not an early close: INFERRED, see Run 1 f).
- Separately, and not part of the 1352: 48 weekdays have no bar stamped 09:31..16:00 at all [K16, K19] (see "Data holes"). The range has 1400 weekdays [K20].
- **Direction** [K15] (OBSERVED): recomputed from the code rule (15:30-bar close vs the most recent prior weekday 16:00 close), disagreements with the CSV side: 0 of 1304. Sessions with a zero return: none.
- **Bars** [K15, K20] (OBSERVED): Bars = 30 on 1303 trades and 25 on trade #2 (2021-03-10). On every trade, Bars equals the count of bar-file stamps from entry to exit inclusive (difference 0 on 1304 of 1304). Trade #2 is missing the stamps 15:33, 15:44, 15:46, 15:50 and 15:58. INFERRED: 15:31..16:00 inclusive is 30 one-minute stamps, so a full trade shows 30, not about 29. The screenshot's 29.00 is the CSV mean - 1.00 (b above).

### e. Qty, duplicates, overlaps (OBSERVED, [K03 `[6]`])

Qty != 1: 0. Duplicate entry times: none. Overlapping positions (next entry before this exit): 0. Same-timestamp exit followed by an entry: 0.

### f. Early-close and short-session exits (OBSERVED)

None. Every LastHalfHourMomentum exit is at 16:00 [K15], and the run has no trade on any session that ends before 15:30: 37 + 9 + 1 = 47 such sessions, summed from the three counts in [K15] (INFERRED arithmetic).

### g. Trades touching data gaps (OBSERVED, [K16] and [K18])

- Trades with a missing stamp between entry and exit [K16]: 1 of 1304, trade #2 (2021-03-10: 15:33, 15:44, 15:46, 15:50, 15:58, all NEW).
- Trades on the known-gap dates [K18]: #825 (2024-07-19), #835 (2024-08-02) and #1304 (2026-07-17), each 15:31 -> 16:00 with Bars=30. Their entries come after the gap extents 09:58-10:07, 11:55-12:02 and 10:59-12:06 (INFERRED from the times). On 2023-04-05 the run has no trade (the session ends 14:03).
- The whole-day holes, the 48 no-RTH weekdays (no trades) and the wider known gaps are in "Data holes" above.

### h. First 5 / last 5 trades (OBSERVED, [K04])

| set | # | side | entry -> exit | entry/exit price | entry -> exit name | profit | Bars |
|---|---|---|---|---|---|---|---|
| first 5 | 1 | Long | 2021-03-09 15:31 -> 16:00 | 16255.75/16197.50 | LHMomLong -> LHFlat1559 | -$1167.96 | 30 |
| first 5 | 2 | Short | 2021-03-10 15:31 -> 16:00 | 16173.75/16159.50 | LHMomShort -> LHFlat1559 | $282.04 | 25 |
| first 5 | 3 | Long | 2021-03-11 15:31 -> 16:00 | 16491.25/16451.50 | LHMomLong -> LHFlat1559 | -$797.96 | 30 |
| first 5 | 4 | Short | 2021-03-12 15:31 -> 16:00 | 16315.00/16344.75 | LHMomShort -> LHFlat1559 | -$597.96 | 30 |
| first 5 | 5 | Long | 2021-03-15 15:31 -> 16:00 | 16414.00/16480.25 | LHMomLong -> LHFlat1559 | $1322.04 | 30 |
| last 5 | 1300 | Short | 2026-07-13 15:31 -> 16:00 | 29419.25/29503.50 | LHMomShort -> LHFlat1559 | -$1687.96 | 30 |
| last 5 | 1301 | Long | 2026-07-14 15:31 -> 16:00 | 29797.75/29807.75 | LHMomLong -> LHFlat1559 | $197.04 | 30 |
| last 5 | 1302 | Short | 2026-07-15 15:31 -> 16:00 | 29642.75/29697.00 | LHMomShort -> LHFlat1559 | -$1087.96 | 30 |
| last 5 | 1303 | Short | 2026-07-16 15:31 -> 16:00 | 29147.00/29201.50 | LHMomShort -> LHFlat1559 | -$1092.96 | 30 |
| last 5 | 1304 | Short | 2026-07-17 15:31 -> 16:00 | 28795.25/28818.25 | LHMomShort -> LHFlat1559 | -$462.96 | 30 |

## Comparison (OBSERVED, [K08])

Baseline vs the three runs, from the CSVs. Listed in file order. This is not a ranking (R-1101-5).

| run | trades | net | PF | max DD (i) | max DD (ii) | win % | avg trade | largest win | largest win as % of net |
|---|---|---|---|---|---|---|---|---|---|
| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |
| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | 58.02% | $259.48 | $36087.04 | 17.17% |
| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | 40.50% | $162.20 | $36472.04 | 18.90% |
| LHMOM (LastHalfHourMomentum) | 1304 | -$76009.84 | 0.84 | -$99806.96 | -$99806.96 | 47.62% | -$58.29 | $3852.04 | -5.07% (not meaningful) |

- LastHalfHourMomentum's net is negative, so its "largest win as % of net" (-5.07%) is not meaningful as a share [K08 note].
- The two max-DD methods give the same value in every run, so the screenshots do not discriminate between them [K08]. The baseline has no screenshot; its -$45,282.04 comparison is against Amear's C4 note (REPORTED BY AMEAR).

## Observations (flagged, not interpreted)

1. **Early-close exit stamps.** On the 13:15 sessions (early closes, INFERRED from calendar knowledge), `Exit on session close` is stamped 12:15 while the bar data runs to 13:15 (5 trades in each of baseline, OppBand and Flat1559) [K24]. On the two 13:00 sessions 2025-01-20 and 2025-06-19, OppBand's #594 and #652 exit at 12:00 while the data runs to 13:00 [K24] (OBSERVED). The VM agent's hypothesis that the trading-hours template is on Central rather than Eastern time is recorded only as a hypothesis. It was not tested here (UNVERIFIED). F2 is FROZEN and nothing is proposed.
2. **Two 17-day data holes**: 2021-09-09 -> 2021-09-27 and 2025-12-14 -> 2026-01-01 [K20] (OBSERVED).
3. **Three known gaps are wider than recorded** (2024-07-19, 2024-08-02, 2026-07-17) [K18] (OBSERVED).
4. **Summary "Avg. bars in trade" = CSV mean - 1.00 in all 9 cells** across the three screenshots [K06] (CSV OBSERVED; shown values REPORTED BY AMEAR).
5. **LastHalfHourMomentum Bars is 30, not about 29**, on 1303 of 1304 trades. Bars equals the inclusive count of bar stamps from entry to exit on every trade in all four CSVs [K15, K20] (OBSERVED).
6. **OppBand largest loss -$19592.96**: trade 627, Long, 2025-04-08 10:01 -> 3:31 PM, exit XL, MAE $22230.00, Bars 331 [K22] (OBSERVED). OppBand's median Bars is 330.0, against 61.0 for baseline and Flat1559 and 30.0 for LastHalfHourMomentum [K04] (OBSERVED).
7. **FlatEOD in code, not in two of the CSVs.** `PraxisNoiseAreaBreakout.cs:288/290` and `PraxisNoiseAreaBreakout_OppBand.cs:314/316` contain `ExitLong/ExitShort("FlatEOD")` [K21], but the baseline and OppBand CSVs have no `FlatEOD` exit. Their 16:00 exits are all `Exit on session close` (423 and 784) [K03] (OBSERVED).
8. **Flat1559 vs baseline**: identical entries on 1190 of 1190 rows. The rows differ only on 423 16:00 exits (`Exit on session close` -> `FlatEOD`), and the net difference is -$4310.00 [K09] (OBSERVED).
9. **CSV file times are later than the times in their names**: the 07-10 file has mtime 08:06; the 07-57, 07-59 and 08-00 files have mtime 08:02 [K01] (OBSERVED). What that means is not inferred here.
10. **The .cs copies installed on the VM were not hash-checked** (R-1101-1). Every code default and line number cited here is from the repo source [K21]. Whether the VM ran the same code is UNVERIFIED.

## Open questions for Amear

These are listed only. This report does not answer them.

1. Early-close sessions: session-close exits are stamped 12:15 (and 12:00 on two 13:00 sessions) while the bar data runs to 13:15 / 13:00 (bar-file clock; US Eastern UNVERIFIED). Does he want this examined? It touches F2 (FROZEN); nothing is proposed here.
2. The two 17-day data holes (Sep 2021, Dec 2025), the nine weekdays with no RTH bars that fall near the quarterly roll (roll link INFERRED from timing only), and the three known gaps that are wider than recorded: accept as-is for these runs, or have the data re-sourced/re-imported?
3. Flat1559: the FlatEOD fills price at the OPEN of the 16:00-stamped bar (the 15:59:00 price if bars are end-stamped), but the grid shows 4:00:00 PM. Does that meet his "flat at 15:59" intent?
4. LastHalfHourMomentum: no trade on the 47 short sessions and the first session; Bars is 30 not ~29. Is that the behaviour he intended?
5. The NOT SHOWN settings items (the $2.96 rate inside the PRAXIS template; full strategy names truncated in the dropdown): does he accept the CSV evidence for them, or want a screenshot?
6. The baseline has no Settings screenshot; its settings rest on his C4 notes. Does he want one?
7. Hash-check of the three .cs files installed on the VM (not done; R-1101-1)?
8. Archive copies of the Desktop CSVs/screenshots into the repo? (R-1101-6 default: no copies; the question went unanswered.)

## Appendix: Commands and outputs

Each command below was run from cwd `/` with `zsh -c`, exactly as pasted. The outputs are from the second fresh run; it is byte-identical (`cmp`) to the first run for all 25 commands. Non-ASCII bytes are shown as `?` where a command pipes through `tr`. Scripts and outputs are session scratch, not in the repo.

### K01 - Input hashes, CSV mtimes, bar-file line count

```sh
shasum -a 256 /Users/admin/Desktop/NinjaTrader\ Grid\ 2026-11-01\ *.csv /Users/admin/Desktop/Screenshot\ 2026-11-01\ at\ 7.57.06*AM.png /Users/admin/Desktop/Screenshot\ 2026-11-01\ at\ 7.58.40*AM.png /Users/admin/Desktop/Screenshot\ 2026-11-01\ at\ 8.00.21*AM.png | LC_ALL=C tr -c '\n -~' '?'; ls -l /Users/admin/Desktop/NinjaTrader\ Grid\ 2026-11-01\ *.csv | LC_ALL=C tr -c '\n -~' '?'; wc -l "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt"
```

```text
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
7ea26c0dd07904be0e4d95853f31a92de5d09f4f87f941f153706cabd1674fb2  /Users/admin/Desktop/Screenshot 2026-11-01 at 7.57.06???AM.png
237c0e7150ad28600ffc6fa30e18cc8adafb43ebf5539813a7c7d21e54da8413  /Users/admin/Desktop/Screenshot 2026-11-01 at 7.58.40???AM.png
fca590ccb570cd6bcf24cac80492cebe6242d4f1f03f9806b9fa2ccf6297db5f  /Users/admin/Desktop/Screenshot 2026-11-01 at 8.00.21???AM.png
-rw-------@ 1 admin  staff  256796 Nov  1 08:06 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
-rw-------@ 1 admin  staff  191423 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
-rw-------@ 1 admin  staff  261564 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
-rw-------@ 1 admin  staff  293775 Nov  1 08:02 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
 1857362 /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
```

### K02 - Script hashes (session scratch, not in the repo)

```sh
shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/screens.txt /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/tz.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/eod.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/vol.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/c/eod.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/c/clamp.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/lib.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s1_lhmom.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s2_gaps.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s3_follow.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s4_extents.py | sed 's#/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/#<scratch>/#'
```

```text
667f8cbcd70ea0491353d4fcb986cbe80912a92c41f0783c8932a901492e9d00  <scratch>/a/tsr.py
1d38b0911e954685446755bb560cecc0e52dcfb6489aa4fb186b43c20117a44d  <scratch>/a/screens.txt
56a887c6e0e4c0ae098a75e8de9ed999382b29b0760afcb722db06543826372c  <scratch>/b/tz.py
830383214179269033ded9b7dacf26d6f80fd1a5e4228cbf99e9143fd3462c03  <scratch>/b/eod.py
1ab7ce3af33cad73bc1036756512b1d50fc9acb3b262f8838e3d03b3aa5bb94b  <scratch>/b/vol.py
84e7bd3c00bdd1ee407c9646fbb1e7039479b807b95832437fb9dc47685e004a  <scratch>/c/eod.py
36212984a9ad985228ab0b7575ca17b4c27bd59e215e889a236d3af3d8a642d9  <scratch>/c/clamp.py
e89e08880ad3f4881671a5a2595459d132a63ee6ead76a03d778d54c00c4c7cc  <scratch>/d/lib.py
66a8b7610af33caee54552ad10c780080149ad52edb141caaf636a67ddda76e5  <scratch>/d/s1_lhmom.py
d78f9ed6860e23d65efd44682f2b7e125ecf0ccb2e1707ca788e350f5de5f69a  <scratch>/d/s2_gaps.py
c2dc021143b505bea6e93d0b0b2a62b62e92071be8bd6cbeb07a6bca618eb1f7  <scratch>/d/s3_follow.py
58066c64aa4740aa94b9b3fe180e9c48b75affe08fab763afde901f4464245d2  <scratch>/d/s4_extents.py
```

### K03 - CSV readback: mapping, totals, max DD, commission, exit names, Qty/overlap (tsr.py main, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py main "BASELINE=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "OPPBAND=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "LHMOM=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | grep -E '^(=+ |\[1\] (sha256|Strategy|date span)|\[2\] |\[3\] |\[4\] |\[5\] |\[6\] (Qty|duplicate|overlapping|same-timestamp))'
```

```text
============================== BASELINE | NinjaTrader Grid 2026-11-01 07-10 AM.csv
[1] sha256 421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd | bytes 256796 | data rows 1190 | header cols 24 | last header col empty: True
[1] Strategy {'PraxisNoiseAreaBreakout': 1190} Instrument {'NQCONTROW SEP25': 1190} Account {'Backtest': 1190}
[1] date span: first entry 2021-03-29 10:01:00 last exit 2026-07-15 13:31:00
[2] Cum. net profit == running sum of Profit on every row: True | mismatching rows: []
[2] All   trades=1190 net=$197327.60 GP=$878467.36 GL=-$681139.76 comm=$3522.40 PF=1.29 W/L/E=484/706/0 pct=40.67% largestW=$35887.04 largestL=-$5407.96 avgT=$165.82 avgW=$1815.02 avgL=-$964.79 avgBars=121.12
[3] All   MaxDD closed-trade: (i) peak-from-0 = -$45282.04 | (ii) peak-from-first-trade = -$45282.04
[2] Long  trades=556 net=$136314.24 GP=$414160.00 GL=-$277845.76 comm=$1645.76 PF=1.49 W/L/E=250/306/0 pct=44.96% largestW=$35887.04 largestL=-$4457.96 avgT=$245.17 avgW=$1656.64 avgL=-$907.99 avgBars=134.94
[3] Long  MaxDD closed-trade: (i) peak-from-0 = -$27173.72 | (ii) peak-from-first-trade = -$27173.72
[2] Short trades=634 net=$61013.36 GP=$464307.36 GL=-$403294.00 comm=$1876.64 PF=1.15 W/L/E=234/400/0 pct=36.91% largestW=$15802.04 largestL=-$5407.96 avgT=$96.24 avgW=$1984.22 avgL=-$1008.24 avgBars=109.00
[3] Short MaxDD closed-trade: (i) peak-from-0 = -$38498.00 | (ii) peak-from-first-trade = -$38498.00
[4] rows Commission != $2.96: 0 [] | sum commission $3522.40 == trades x 2.96 ( $3522.40 ): True
[4] rows with any Clearing/Exchange/IP/NFA fee != $0.00: 0 []
[5] entry names {'S': 634, 'L': 556}
[5] exit names {'XS': 429, 'Exit on session close': 429, 'XL': 332}
[5]   exit ToD for XS                     top: [('10:31', 74), ('11:31', 48), ('12:01', 37), ('11:01', 37), ('14:31', 37), ('12:31', 36), ('15:01', 35), ('14:01', 34)] | distinct ToDs: 11
[5]   exit ToD for Exit on session close  top: [('16:00', 423), ('12:15', 5), ('14:03', 1)] | distinct ToDs: 3
[5]   exit ToD for XL                     top: [('11:01', 52), ('10:31', 51), ('12:31', 37), ('13:31', 37), ('12:01', 35), ('11:31', 26), ('13:01', 23), ('15:01', 20)] | distinct ToDs: 11
[6] Qty != 1: 0
[6] duplicate entry times: []
[6] overlapping positions (next entry < this exit): 0 []
[6] same-timestamp exit-then-entry: 1 | first 5: [(666, 667)]
============================== OPPBAND | NinjaTrader Grid 2026-11-01 07-57 AM.csv
[1] sha256 4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8 | bytes 191423 | data rows 810 | header cols 24 | last header col empty: True
[1] Strategy {'PraxisNoiseAreaBreakout_OppBand': 810} Instrument {'NQCONTROW SEP25': 810} Account {'Backtest': 810}
[1] date span: first entry 2021-03-29 10:01:00 last exit 2026-07-15 16:00:00
[2] Cum. net profit == running sum of Profit on every row: True | mismatching rows: []
[2] All   trades=810 net=$210182.40 GP=$1009483.80 GL=-$799301.40 comm=$2397.60 PF=1.26 W/L/E=470/340/0 pct=58.02% largestW=$36087.04 largestL=-$19592.96 avgT=$259.48 avgW=$2147.84 avgL=-$2350.89 avgBars=292.45
[3] All   MaxDD closed-trade: (i) peak-from-0 = -$50748.88 | (ii) peak-from-first-trade = -$50748.88
[2] Long  trades=404 net=$138454.16 GP=$484987.24 GL=-$346533.08 comm=$1195.84 PF=1.40 W/L/E=256/148/0 pct=63.37% largestW=$36087.04 largestL=-$19592.96 avgT=$342.71 avgW=$1894.48 avgL=-$2341.44 avgBars=291.22
[3] Long  MaxDD closed-trade: (i) peak-from-0 = -$27645.64 | (ii) peak-from-first-trade = -$27645.64
[2] Short trades=406 net=$71728.24 GP=$524496.56 GL=-$452768.32 comm=$1201.76 PF=1.16 W/L/E=214/192/0 pct=52.71% largestW=$15802.04 largestL=-$10477.96 avgT=$176.67 avgW=$2450.92 avgL=-$2358.17 avgBars=293.68
[3] Short MaxDD closed-trade: (i) peak-from-0 = -$51652.92 | (ii) peak-from-first-trade = -$51652.92
[4] rows Commission != $2.96: 0 [] | sum commission $2397.60 == trades x 2.96 ( $2397.60 ): True
[4] rows with any Clearing/Exchange/IP/NFA fee != $0.00: 0 []
[5] entry names {'S': 406, 'L': 404}
[5] exit names {'Exit on session close': 792, 'XS': 8, 'XL': 10}
[5]   exit ToD for Exit on session close  top: [('16:00', 784), ('12:15', 5), ('12:00', 2), ('14:03', 1)] | distinct ToDs: 4
[5]   exit ToD for XL                     top: [('13:31', 2), ('15:01', 2), ('15:31', 2), ('14:31', 1), ('12:31', 1), ('11:31', 1), ('11:01', 1)] | distinct ToDs: 7
[5]   exit ToD for XS                     top: [('12:31', 2), ('15:31', 1), ('11:31', 1), ('15:01', 1), ('13:31', 1), ('12:01', 1), ('14:01', 1)] | distinct ToDs: 7
[6] Qty != 1: 0
[6] duplicate entry times: []
[6] overlapping positions (next entry < this exit): 0 []
[6] same-timestamp exit-then-entry: 18 | first 5: [(16, 17), (27, 28), (100, 101), (110, 111), (120, 121)]
============================== FLAT1559 | NinjaTrader Grid 2026-11-01 07-59 AM.csv
[1] sha256 5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0 | bytes 261564 | data rows 1190 | header cols 24 | last header col empty: True
[1] Strategy {'PraxisNoiseAreaBreakout_Flat1559': 1190} Instrument {'NQCONTROW SEP25': 1190} Account {'Backtest': 1190}
[1] date span: first entry 2021-03-29 10:01:00 last exit 2026-07-15 13:31:00
[2] Cum. net profit == running sum of Profit on every row: True | mismatching rows: []
[2] All   trades=1190 net=$193017.60 GP=$871258.28 GL=-$678240.68 comm=$3522.40 PF=1.28 W/L/E=482/708/0 pct=40.50% largestW=$36472.04 largestL=-$5407.96 avgT=$162.20 avgW=$1807.59 avgL=-$957.97 avgBars=121.12
[3] All   MaxDD closed-trade: (i) peak-from-0 = -$40637.04 | (ii) peak-from-first-trade = -$40637.04
[2] Long  trades=556 net=$138509.24 GP=$416257.96 GL=-$277748.72 comm=$1645.76 PF=1.50 W/L/E=249/307/0 pct=44.78% largestW=$36472.04 largestL=-$4457.96 avgT=$249.12 avgW=$1671.72 avgL=-$904.72 avgBars=134.94
[3] Long  MaxDD closed-trade: (i) peak-from-0 = -$23774.12 | (ii) peak-from-first-trade = -$23774.12
[2] Short trades=634 net=$54508.36 GP=$455000.32 GL=-$400491.96 comm=$1876.64 PF=1.14 W/L/E=233/401/0 pct=36.75% largestW=$15742.04 largestL=-$5407.96 avgT=$85.98 avgW=$1952.79 avgL=-$998.73 avgBars=109.00
[3] Short MaxDD closed-trade: (i) peak-from-0 = -$38778.00 | (ii) peak-from-first-trade = -$38778.00
[4] rows Commission != $2.96: 0 [] | sum commission $3522.40 == trades x 2.96 ( $3522.40 ): True
[4] rows with any Clearing/Exchange/IP/NFA fee != $0.00: 0 []
[5] entry names {'S': 634, 'L': 556}
[5] exit names {'XS': 429, 'FlatEOD': 423, 'XL': 332, 'Exit on session close': 6}
[5]   exit ToD for XS                     top: [('10:31', 74), ('11:31', 48), ('12:01', 37), ('11:01', 37), ('14:31', 37), ('12:31', 36), ('15:01', 35), ('14:01', 34)] | distinct ToDs: 11
[5]   exit ToD for FlatEOD                top: [('16:00', 423)] | distinct ToDs: 1
[5]   exit ToD for XL                     top: [('11:01', 52), ('10:31', 51), ('12:31', 37), ('13:31', 37), ('12:01', 35), ('11:31', 26), ('13:01', 23), ('15:01', 20)] | distinct ToDs: 11
[5]   exit ToD for Exit on session close  top: [('12:15', 5), ('14:03', 1)] | distinct ToDs: 2
[6] Qty != 1: 0
[6] duplicate entry times: []
[6] overlapping positions (next entry < this exit): 0 []
[6] same-timestamp exit-then-entry: 1 | first 5: [(666, 667)]
============================== LHMOM | NinjaTrader Grid 2026-11-01 08-00 AM.csv
[1] sha256 4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9 | bytes 293775 | data rows 1304 | header cols 24 | last header col empty: True
[1] Strategy {'PraxisLastHalfHourMomentum': 1304} Instrument {'NQCONTROW SEP25': 1304} Account {'Backtest': 1304}
[1] date span: first entry 2021-03-09 15:31:00 last exit 2026-07-17 16:00:00
[2] Cum. net profit == running sum of Profit on every row: True | mismatching rows: []
[2] All   trades=1304 net=-$76009.84 GP=$411326.84 GL=-$487336.68 comm=$3859.84 PF=0.84 W/L/E=621/683/0 pct=47.62% largestW=$3852.04 largestL=-$5537.96 avgT=-$58.29 avgW=$662.36 avgL=-$713.52 avgBars=30.00
[3] All   MaxDD closed-trade: (i) peak-from-0 = -$99806.96 | (ii) peak-from-first-trade = -$99806.96
[2] Long  trades=698 net=-$24736.08 GP=$195212.48 GL=-$219948.56 comm=$2066.08 PF=0.89 W/L/E=337/361/0 pct=48.28% largestW=$3407.04 largestL=-$5537.96 avgT=-$35.44 avgW=$579.27 avgL=-$609.28 avgBars=30.00
[3] Long  MaxDD closed-trade: (i) peak-from-0 = -$41000.28 | (ii) peak-from-first-trade = -$41000.28
[2] Short trades=606 net=-$51273.76 GP=$216114.36 GL=-$267388.12 comm=$1793.76 PF=0.81 W/L/E=284/322/0 pct=46.86% largestW=$3852.04 largestL=-$5242.96 avgT=-$84.61 avgW=$760.97 avgL=-$830.40 avgBars=29.99
[3] Short MaxDD closed-trade: (i) peak-from-0 = -$77254.32 | (ii) peak-from-first-trade = -$77254.32
[4] rows Commission != $2.96: 0 [] | sum commission $3859.84 == trades x 2.96 ( $3859.84 ): True
[4] rows with any Clearing/Exchange/IP/NFA fee != $0.00: 0 []
[5] entry names {'LHMomLong': 698, 'LHMomShort': 606}
[5] exit names {'LHFlat1559': 1304}
[5]   exit ToD for LHFlat1559             top: [('16:00', 1304)] | distinct ToDs: 1
[6] Qty != 1: 0
[6] duplicate entry times: []
[6] overlapping positions (next entry < this exit): 0 []
[6] same-timestamp exit-then-entry: 0 | first 5: []
```

### K04 - CSV readback: first/last 5, Bars (tsr.py main, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py main "BASELINE=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "OPPBAND=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "LHMOM=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | grep -E '^(=+ |\[9\]|\[10\] (Bars min|LHMOM (Bars d|entry|exit)))'
```

```text
============================== BASELINE | NinjaTrader Grid 2026-11-01 07-10 AM.csv
[9] first 5:
[9]    #1 Short 2021-03-29 10:01->2021-03-29 11:31 16270.25/16297.25 S->XS -$542.96 bars=91
[9]    #2 Long 2021-03-31 10:01->2021-03-31 16:00 16468.50/16504.00 L->Exit on session close $707.04 bars=360
[9]    #3 Long 2021-04-05 10:01->2021-04-05 16:00 16892.50/16998.50 L->Exit on session close $2117.04 bars=360
[9]    #4 Long 2021-04-13 10:01->2021-04-13 12:01 17358.00/17320.50 L->XL -$752.96 bars=121
[9]    #5 Long 2021-04-13 12:31->2021-04-13 13:01 17327.50/17319.50 L->XL -$162.96 bars=31
[9] last 5:
[9]    #1186 Short 2026-07-07 10:01->2026-07-07 12:31 29468.25/29532.75 S->XS -$1292.96 bars=151
[9]    #1187 Short 2026-07-07 15:31->2026-07-07 16:00 29320.25/29393.00 S->Exit on session close -$1457.96 bars=30
[9]    #1188 Long 2026-07-14 11:31->2026-07-14 12:01 29885.50/29785.50 L->XL -$2002.96 bars=31
[9]    #1189 Short 2026-07-15 11:01->2026-07-15 11:31 29631.50/29641.25 S->XS -$197.96 bars=31
[9]    #1190 Short 2026-07-15 12:01->2026-07-15 13:31 29579.75/29605.25 S->XS -$512.96 bars=91
[10] Bars min/max/median: 30 360 61.0
============================== OPPBAND | NinjaTrader Grid 2026-11-01 07-57 AM.csv
[9] first 5:
[9]    #1 Short 2021-03-29 10:01->2021-03-29 16:00 16270.25/16371.00 S->Exit on session close -$2017.96 bars=360
[9]    #2 Long 2021-03-31 10:01->2021-03-31 16:00 16468.50/16504.00 L->Exit on session close $707.04 bars=360
[9]    #3 Long 2021-04-05 10:01->2021-04-05 16:00 16892.50/16998.50 L->Exit on session close $2117.04 bars=360
[9]    #4 Long 2021-04-13 10:01->2021-04-13 16:00 17358.00/17391.25 L->Exit on session close $662.04 bars=360
[9]    #5 Short 2021-04-14 11:31->2021-04-14 16:00 17296.50/17223.75 S->Exit on session close $1452.04 bars=270
[9] last 5:
[9]    #806 Short 2026-07-01 11:01->2026-07-01 16:00 30192.50/30081.75 S->Exit on session close $2212.04 bars=300
[9]    #807 Short 2026-07-02 11:01->2026-07-02 16:00 29839.75/29536.50 S->Exit on session close $6062.04 bars=300
[9]    #808 Short 2026-07-07 10:01->2026-07-07 16:00 29468.25/29393.00 S->Exit on session close $1502.04 bars=360
[9]    #809 Long 2026-07-14 11:31->2026-07-14 16:00 29885.50/29787.25 L->Exit on session close -$1967.96 bars=270
[9]    #810 Short 2026-07-15 11:01->2026-07-15 16:00 29631.50/29701.00 S->Exit on session close -$1392.96 bars=300
[10] Bars min/max/median: 30 360 330.0
============================== FLAT1559 | NinjaTrader Grid 2026-11-01 07-59 AM.csv
[9] first 5:
[9]    #1 Short 2021-03-29 10:01->2021-03-29 11:31 16270.25/16297.25 S->XS -$542.96 bars=91
[9]    #2 Long 2021-03-31 10:01->2021-03-31 16:00 16468.50/16514.75 L->FlatEOD $922.04 bars=360
[9]    #3 Long 2021-04-05 10:01->2021-04-05 16:00 16892.50/16995.25 L->FlatEOD $2052.04 bars=360
[9]    #4 Long 2021-04-13 10:01->2021-04-13 12:01 17358.00/17320.50 L->XL -$752.96 bars=121
[9]    #5 Long 2021-04-13 12:31->2021-04-13 13:01 17327.50/17319.50 L->XL -$162.96 bars=31
[9] last 5:
[9]    #1186 Short 2026-07-07 10:01->2026-07-07 12:31 29468.25/29532.75 S->XS -$1292.96 bars=151
[9]    #1187 Short 2026-07-07 15:31->2026-07-07 16:00 29320.25/29389.00 S->FlatEOD -$1377.96 bars=30
[9]    #1188 Long 2026-07-14 11:31->2026-07-14 12:01 29885.50/29785.50 L->XL -$2002.96 bars=31
[9]    #1189 Short 2026-07-15 11:01->2026-07-15 11:31 29631.50/29641.25 S->XS -$197.96 bars=31
[9]    #1190 Short 2026-07-15 12:01->2026-07-15 13:31 29579.75/29605.25 S->XS -$512.96 bars=91
[10] Bars min/max/median: 30 360 61.0
============================== LHMOM | NinjaTrader Grid 2026-11-01 08-00 AM.csv
[9] first 5:
[9]    #1 Long 2021-03-09 15:31->2021-03-09 16:00 16255.75/16197.50 LHMomLong->LHFlat1559 -$1167.96 bars=30
[9]    #2 Short 2021-03-10 15:31->2021-03-10 16:00 16173.75/16159.50 LHMomShort->LHFlat1559 $282.04 bars=25
[9]    #3 Long 2021-03-11 15:31->2021-03-11 16:00 16491.25/16451.50 LHMomLong->LHFlat1559 -$797.96 bars=30
[9]    #4 Short 2021-03-12 15:31->2021-03-12 16:00 16315.00/16344.75 LHMomShort->LHFlat1559 -$597.96 bars=30
[9]    #5 Long 2021-03-15 15:31->2021-03-15 16:00 16414.00/16480.25 LHMomLong->LHFlat1559 $1322.04 bars=30
[9] last 5:
[9]    #1300 Short 2026-07-13 15:31->2026-07-13 16:00 29419.25/29503.50 LHMomShort->LHFlat1559 -$1687.96 bars=30
[9]    #1301 Long 2026-07-14 15:31->2026-07-14 16:00 29797.75/29807.75 LHMomLong->LHFlat1559 $197.04 bars=30
[9]    #1302 Short 2026-07-15 15:31->2026-07-15 16:00 29642.75/29697.00 LHMomShort->LHFlat1559 -$1087.96 bars=30
[9]    #1303 Short 2026-07-16 15:31->2026-07-16 16:00 29147.00/29201.50 LHMomShort->LHFlat1559 -$1092.96 bars=30
[9]    #1304 Short 2026-07-17 15:31->2026-07-17 16:00 28795.25/28818.25 LHMomShort->LHFlat1559 -$462.96 bars=30
[10] Bars min/max/median: 25 30 30.0
[10] LHMOM entry ToD distribution: [('15:31', 1304)]
[10] LHMOM exit ToD distribution: [('16:00', 1304)]
[10] LHMOM Bars distribution: [(25, 1), (30, 1303)]
```

### K05 - Baseline re-derivation vs Amear's C4 values (tsr.py baseline)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py baseline "BASELINE=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv"
```

```text
trades                   amear=1190           csv=1190           MATCH
long_trades              amear=556            csv=556            MATCH
short_trades             amear=634            csv=634            MATCH
net                      amear=$197,327.60    csv=$197327.60     MATCH
gross_profit             amear=$878,467.36    csv=$878467.36     MATCH
gross_loss               amear=-$681,139.76   csv=-$681139.76    MATCH
commission               amear=$3,522.40      csv=$3522.40       MATCH
pf                       amear=1.29           csv=1.29           MATCH
max_dd                   amear=-$45,282.04    csv(i)=-$45282.04     csv(ii)=-$45282.04     MATCH (i) peak-from-0 MATCH (ii) peak-from-first
avg_trade                amear=$165.82        csv=$165.82        MATCH
avg_win                  amear=$1,815.02      csv=$1815.02       MATCH
avg_loss                 amear=-$964.79       csv=-$964.79       MATCH
wins                     amear=484            csv=484            MATCH
losses                   amear=706            csv=706            MATCH
even                     amear=0              csv=0              MATCH
largest_win              amear=$35,887.04     csv=$35887.04      MATCH
largest_loss             amear=-$5,407.96     csv=-$5407.96      MATCH
long_net                 amear=$136,314.24    csv=$136314.24     MATCH
short_net                amear=$61,013.36     csv=$61013.36      MATCH
x_Exit on session close  amear=429            csv=429            MATCH
x_XS                     amear=429            csv=429            MATCH
x_XL                     amear=332            csv=332            MATCH
exit names in CSV not in Amear's list: []
```

### K06 - Screenshot reconciliation: non-MATCH cells and max DD cells (tsr.py recon)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py recon /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/screens.txt "OPPBAND=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "LHMOM=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | grep -E 'max_dd|MISMATCH|NOT DERIVABLE|TALLY'
```

```text
OPPBAND   All   max_dd          shot=-$50,748.88    csv=(i)-$50748.88 (ii)-$50748.88   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
OPPBAND   All   total_slippage  shot=810            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 810: True)
OPPBAND   All   avg_bars        shot=291.45         csv=292.45                         MISMATCH
OPPBAND   Long  max_dd          shot=-$27,645.64    csv=(i)-$27645.64 (ii)-$27645.64   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
OPPBAND   Long  total_slippage  shot=404            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 404: True)
OPPBAND   Long  avg_bars        shot=290.22         csv=291.22                         MISMATCH
OPPBAND   Short max_dd          shot=-$51,652.92    csv=(i)-$51652.92 (ii)-$51652.92   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
OPPBAND   Short total_slippage  shot=406            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 406: True)
OPPBAND   Short avg_bars        shot=292.68         csv=293.68                         MISMATCH
FLAT1559  All   max_dd          shot=-$40,637.04    csv=(i)-$40637.04 (ii)-$40637.04   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
FLAT1559  All   total_slippage  shot=1190           csv=n/a                            NOT DERIVABLE from CSV (equals trade count 1190: True)
FLAT1559  All   avg_bars        shot=120.12         csv=121.12                         MISMATCH
FLAT1559  Long  max_dd          shot=-$23,774.12    csv=(i)-$23774.12 (ii)-$23774.12   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
FLAT1559  Long  total_slippage  shot=556            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 556: True)
FLAT1559  Long  avg_bars        shot=133.94         csv=134.94                         MISMATCH
FLAT1559  Short max_dd          shot=-$38,778.00    csv=(i)-$38778.00 (ii)-$38778.00   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
FLAT1559  Short total_slippage  shot=634            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 634: True)
FLAT1559  Short avg_bars        shot=108.00         csv=109.00                         MISMATCH
LHMOM     All   max_dd          shot=-$99,806.96    csv=(i)-$99806.96 (ii)-$99806.96   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
LHMOM     All   total_slippage  shot=1304           csv=n/a                            NOT DERIVABLE from CSV (equals trade count 1304: True)
LHMOM     All   avg_bars        shot=29.00          csv=30.00                          MISMATCH
LHMOM     Long  max_dd          shot=-$41,000.28    csv=(i)-$41000.28 (ii)-$41000.28   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
LHMOM     Long  total_slippage  shot=698            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 698: True)
LHMOM     Long  avg_bars        shot=29.00          csv=30.00                          MISMATCH
LHMOM     Short max_dd          shot=-$77,254.32    csv=(i)-$77254.32 (ii)-$77254.32   MATCH method (i) peak-from-0; MATCH method (ii) peak-from-first
LHMOM     Short total_slippage  shot=606            csv=n/a                            NOT DERIVABLE from CSV (equals trade count 606: True)
LHMOM     Short avg_bars        shot=28.99          csv=29.99                          MISMATCH
TALLY {'MATCH': 144, 'NOT': 9, 'MISMATCH': 9}
```

### K07 - Screenshot reconciliation: verdict count per run (tsr.py recon)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py recon /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/screens.txt "OPPBAND=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "LHMOM=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | awk '$1!="TALLY"{v=($0 ~ /MISMATCH/)?"MISMATCH":($0 ~ /NOT DERIVABLE/)?"NOT_DERIVABLE":($0 ~ /MATCH/)?"MATCH":"OTHER"; n[$1" "v]++} END{for(k in n) print k, n[k]}' | sort
```

```text
FLAT1559 MATCH 48
FLAT1559 MISMATCH 3
FLAT1559 NOT_DERIVABLE 3
LHMOM MATCH 48
LHMOM MISMATCH 3
LHMOM NOT_DERIVABLE 3
OPPBAND MATCH 48
OPPBAND MISMATCH 3
OPPBAND NOT_DERIVABLE 3
```

### K08 - Comparison table (tsr.py compare)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py compare /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/screens.txt "BASELINE=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "OPPBAND=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "LHMOM=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
```

```text
run       trades            net    PF       maxDD(i)      maxDD(ii)     win%   avgTrade       largestWin   LW%ofNet
BASELINE    1190     $197327.60  1.29     -$45282.04     -$45282.04   40.67%    $165.82        $35887.04     18.19%
OPPBAND      810     $210182.40  1.26     -$50748.88     -$50748.88   58.02%    $259.48        $36087.04     17.17%
FLAT1559    1190     $193017.60  1.28     -$40637.04     -$40637.04   40.50%    $162.20        $36472.04     18.90%
LHMOM       1304     -$76009.84  0.84     -$99806.96     -$99806.96   47.62%    -$58.29         $3852.04     -5.07%
max-DD method that matched the screenshot (All column):
  BASELINE  no screenshot; Amear's C4 note says -$45,282.04 -> both (i) and (ii) (methods give the same value here; not discriminated)
  OPPBAND   shot=-$50748.88 -> both (i) and (ii) (methods give the same value here; not discriminated)
  FLAT1559  shot=-$40637.04 -> both (i) and (ii) (methods give the same value here; not discriminated)
  LHMOM     shot=-$99806.96 -> both (i) and (ii) (methods give the same value here; not discriminated)
note: LW%ofNet is largest winning trade / total net x 100; for a negative net the sign is negative and the ratio is not meaningful as a share.
```

### K09 - Flat1559 vs baseline row diff (tsr.py diff)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/a/tsr.py diff "BASELINE=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "FLAT1559=/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv"
```

```text
rows BASELINE 1190 FLAT1559 1190
rows with identical side/entry time/entry price/entry name: 1190
rows whose exit time/price/name/profit differ: 423
  by exit-name pair: [(('Exit on session close', 'FlatEOD'), 423)]
  exit time differs on: 0 | exit price differs on: 418
  sum of profit difference (FLAT1559 - BASELINE): -$4310.00
  per-trade exit-price change in ticks, signed in the position's favour: 169 distinct values; min -272 max 155
```

### K10 - Bar-file clock: daily break and entry-vs-OPEN offset tables (b/tz.py, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/tz.py "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" | grep -E -A4 '^(intraday gaps|ENTRY vs OPEN  offset)'
```

```text
intraday gaps 30min..6h, top by (US-DST?, last stamp before, first stamp after):
  dst=True  1700 -> 1801  n=704
  dst=False  1700 -> 1801  n=317
  dst=True  1300 -> 1801  n=19
  dst=False  1300 -> 1801  n=13
--
ENTRY vs OPEN  offset -3h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      0      0      0      0      2   2376      2
  DST         1572      0      0      0      0      2   1568      2
  nonDST       808      0      0      0      0      0    808      0
ENTRY vs OPEN  offset -2h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      2      0      2      4      2   2370      0
  DST         1572      2      0      2      2      0   1566      0
  nonDST       808      0      0      0      2      2    804      0
ENTRY vs OPEN  offset -1h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      0      2      0      2      0   2374      2
  DST         1572      0      2      0      2      0   1566      2
  nonDST       808      0      0      0      0      0    808      0
ENTRY vs OPEN  offset +0h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380     24     18   2338      0      0      0      0
  DST         1572     16     12   1544      0      0      0      0
  nonDST       808      8      6    794      0      0      0      0
ENTRY vs OPEN  offset +1h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      2      4      0      6      4   2364      0
  DST         1572      0      4      0      4      4   1560      0
  nonDST       808      2      0      0      2      0    804      0
ENTRY vs OPEN  offset +2h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      2      6      2      4      2   2122    242
  DST         1572      0      6      0      2      2   1408    154
  nonDST       808      2      0      2      2      0    714     88
ENTRY vs OPEN  offset +3h  (BASELINE+FLAT1559 entries, n=2380)
  subset         n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  ALL         2380      4      4      4      0      4   2086    278
  DST         1572      2      2      4      0      4   1386    174
  nonDST       808      2      2      0      0      0    700    104
```

### K11 - Bar-file clock: volume profile and short-session last stamps (b/vol.py)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/vol.py "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv"
```

```text
== Mean 1-min volume by bar-END stamp HHMM, weekdays, split by US DST ==
dst=True days=932  top6 stamps: 1600:7439, 0931:4959, 0932:3620, 1601:3232, 0933:3176, 0936:3018
   0828:208  0829:220  0830:230  0831:1034  0929:759  0930:915  0931:4959  0932:3620  1559:1975  1600:7439  1601:3232  1602:1419  1614:390  1615:408  1616:263
dst=False days=441  top6 stamps: 1600:7538, 0931:5092, 0932:3780, 0933:3234, 1601:3077, 0936:3052
   0828:210  0829:212  0830:240  0831:1082  0929:731  0930:940  0931:5092  0932:3780  1559:1935  1600:7538  1601:3077  1602:1267  1614:351  1615:370  1616:283
== early-close / odd days: weekday bar stamps 11:00-15:00 present (first, last, count, gaps>1min) ==
  20211126 1100 1315 136 []
  20240703 1100 1315 136 []
  20241129 1100 1315 136 []
  20241224 1100 1315 136 []
  20250703 1100 1315 136 []
  20230405 1100 1403 184 []
== BASELINE entry clock range: min 10:01 max 15:31
```

### K12 - Entry clamp, FlatEOD fill test, baseline session-close test, pairing (b/eod.py, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/b/eod.py "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" | grep -E '^(== Item 1d|  (BASELINE|FLAT1559) match| trades with exit name|FLAT1559 FlatEOD|BASELINE session-close \(|  reference|  bar1|  clamp|  discriminating|    disc|== Item 3|  unique keys|  identical|  differing|    \(|  FlatEOD trades paired|  of those|  \(flat exit|  direction-signed|  sum in|  pairs where)'
```

```text
== Item 1d: entry slippage clipped to bar range? fill == clamp(open + 0.5*dir, low, high) on bar stamped entry time ==
  BASELINE match 1190 nomatch 0
  FLAT1559 match 1190 nomatch 0
 trades with exit name 'FlatEOD': 423; exit clock times {'16:00:00': 423}
FLAT1559 FlatEOD exit price vs reference (signed: + = adverse to the exit order, i.e. long sells lower / short buys higher)
  reference                                       n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  bar16:00 OPEN                                 423     10     11    402      0      0      0      0
  bar16:00 CLOSE                                423      4      7      5      2      1    404      0
  bar15:59 CLOSE                                423     29    110     99      8      2    175      0
  bar15:59 OPEN                                 423      4     10     11      5     10    383      0
  clamp(16:00 OPEN -/+ 0.5 adverse, L, H) match 423 of 423
  clamp(16:00 CLOSE -/+ 0.5 adverse, L, H) match 5 of 423
  discriminating subset (15:59 CLOSE != 16:00 OPEN): 319
    disc vs bar16:00 OPEN                       319      8      8    303      0      0      0      0
    disc vs bar15:59 CLOSE                      319     27    107      0      8      2    175      0
    disc vs bar16:00 CLOSE                      319      3      5      3      2      1    305      0
 trades with exit name 'Exit on session close': 6; exit clock times {'12:15:00': 5, '14:03:00': 1}
 trades with exit name 'Exit on session close': 429; exit clock times {'16:00:00': 423, '12:15:00': 5, '14:03:00': 1}
BASELINE session-close (16:00-stamped only) exit price vs reference (signed: + = adverse to the exit order, i.e. long sells lower / short buys higher)
  reference                                       n  exact  adv1t  adv2t  fav1t  fav2t  other  nobar
  bar16:00 OPEN                                 423      3      3      5     10      3    399      0
  bar16:00 CLOSE                                423      2      3    418      0      0      0      0
  bar15:59 CLOSE                                423      7      3      7      3      3    400      0
  bar15:59 OPEN                                 423      2      2      1      3      2    413      0
  clamp(16:00 OPEN -/+ 0.5 adverse, L, H) match 5 of 423
  clamp(16:00 CLOSE -/+ 0.5 adverse, L, H) match 423 of 423
  discriminating subset (15:59 CLOSE != 16:00 OPEN): 319
    disc vs bar16:00 OPEN                       319      2      2      3     10      3    299      0
    disc vs bar15:59 CLOSE                      319      6      2      5      3      3    300      0
    disc vs bar16:00 CLOSE                      319      0      1    318      0      0      0      0
== Item 3: BASELINE vs FLAT1559 pairing ==
  unique keys (entry time, side): base 1190 flat 1190; in both 1190; base-only 0; flat-only 0
  identical (entry time, side, entry px, exit time, exit px): 772; differing: 418
  identical by exit name: {'XS/XS': 429, 'XL/XL': 332, 'Exit on session close/Exit on session close': 6, 'Exit on session close/FlatEOD': 5}
  differing, by (base exit name, base exit HH:MM, flat exit name, flat exit HH:MM):
    ('Exit on session close', '16:00', 'FlatEOD', '16:00')  n=418
  FlatEOD trades paired with baseline 'Exit on session close' at 16:00 same day: 423 of 423 FlatEOD
  of those, baseline exit time == flat exit time: 423
  (flat exit - base exit) raw points: zero 5, pos 211, neg 207; sum 435.00
  direction-signed (flat - base)*dir points (+ = Flat1559 better): n 423 zero 5 pos 215 neg 203 sum -215.50 min -68.00 median 0.25 max 38.75
  sum in $ at $20/pt: -4310.00
  pairs where (flat exit - base exit) == (bar16:00 OPEN - bar16:00 CLOSE): 397 of 423
```

### K13 - Session-close fill reference, all four runs (c/eod.py, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/c/eod.py "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | grep -E '^(entry adverse|== |   ALL    (O|C)@16:00)'
```

```text
entry adverse residual vs OPEN of bar stamped entry time (points): [('0.50', 4304), ('0.25', 78), ('0.00', 72), ('-0.00', 40)]
== FLAT1559: exit name 'FlatEOD', n=423
   ALL    O@16:00  n=423 missing=0 |diff|<=0:10 <=0.25:21 <=0.5:423 ; signed adverse slip top: [('0.50', 402), ('0.25', 11), ('-0.00', 8), ('0.00', 2)]
   ALL    C@16:00  n=423 missing=0 |diff|<=0:4 <=0.25:13 <=0.5:19 ; signed adverse slip top: [('1.25', 10), ('2.75', 9), ('2.50', 9), ('-1.25', 9)]
== FLAT1559: exit name 'Exit on session close', n=6
   ALL    O@16:00  n=0 missing=6 |diff|<=0:0 <=0.25:0 <=0.5:0 ; signed adverse slip top: []
   ALL    C@16:00  n=0 missing=6 |diff|<=0:0 <=0.25:0 <=0.5:0 ; signed adverse slip top: []
== BASELINE: exit name 'Exit on session close', n=429
   ALL    O@16:00  n=423 missing=6 |diff|<=0:3 <=0.25:16 <=0.5:24 ; signed adverse slip top: [('2.25', 10), ('-0.25', 10), ('-1.75', 9), ('-1.50', 9)]
   ALL    C@16:00  n=423 missing=6 |diff|<=0:2 <=0.25:5 <=0.5:423 ; signed adverse slip top: [('0.50', 418), ('0.25', 3), ('-0.00', 2)]
== OPPBAND: exit name 'Exit on session close', n=792
   ALL    O@16:00  n=784 missing=8 |diff|<=0:7 <=0.25:22 <=0.5:33 ; signed adverse slip top: [('2.25', 16), ('-1.50', 14), ('-0.25', 12), ('-1.75', 11)]
   ALL    C@16:00  n=784 missing=8 |diff|<=0:3 <=0.25:9 <=0.5:784 ; signed adverse slip top: [('0.50', 775), ('0.25', 6), ('-0.00', 3)]
== LHMOM: exit name 'LHFlat1559', n=1304
   ALL    O@16:00  n=1304 missing=0 |diff|<=0:36 <=0.25:78 <=0.5:1304 ; signed adverse slip top: [('0.50', 1226), ('0.25', 42), ('-0.00', 23), ('0.00', 13)]
   ALL    C@16:00  n=1304 missing=0 |diff|<=0:15 <=0.25:46 <=0.5:66 ; signed adverse slip top: [('-4.50', 19), ('-1.25', 19), ('0.25', 19), ('-1.00', 18)]
```

### K14 - Fills that are not open +/- 2 ticks: clipped to the bar extreme? (c/clamp.py, first section)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/c/clamp.py "/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv" | sed -n '2,/^== early/p'
```

```text
NinjaTrader Grid 2026-11-01 07-10 AM.csv
    entry adv=-0.00 fill==bar adverse extreme:True 5
    entry adv=0.00 fill==bar adverse extreme:True 7
    entry adv=0.25 fill==bar adverse extreme:True 9
    exit[Exit on session close] adv=-0.00 fill==bar adverse extreme:True 2
    exit[Exit on session close] adv=0.25 fill==bar adverse extreme:True 3
NinjaTrader Grid 2026-11-01 07-57 AM.csv
    entry adv=-0.00 fill==bar adverse extreme:True 1
    entry adv=0.00 fill==bar adverse extreme:True 3
    entry adv=0.25 fill==bar adverse extreme:True 4
    exit[Exit on session close] adv=-0.00 fill==bar adverse extreme:True 3
    exit[Exit on session close] adv=0.25 fill==bar adverse extreme:True 6
NinjaTrader Grid 2026-11-01 07-59 AM.csv
    entry adv=-0.00 fill==bar adverse extreme:True 5
    entry adv=0.00 fill==bar adverse extreme:True 7
    entry adv=0.25 fill==bar adverse extreme:True 9
    exit[FlatEOD] adv=-0.00 fill==bar adverse extreme:True 8
    exit[FlatEOD] adv=0.00 fill==bar adverse extreme:True 2
    exit[FlatEOD] adv=0.25 fill==bar adverse extreme:True 11
NinjaTrader Grid 2026-11-01 08-00 AM.csv
    entry adv=-0.00 fill==bar adverse extreme:True 29
    entry adv=0.00 fill==bar adverse extreme:True 55
    entry adv=0.25 fill==bar adverse extreme:True 56
    exit[LHFlat1559] adv=-0.00 fill==bar adverse extreme:True 23
    exit[LHFlat1559] adv=0.00 fill==bar adverse extreme:True 13
    exit[LHFlat1559] adv=0.25 fill==bar adverse extreme:True 42

== early session-close exits: bars around them
```

### K15 - LastHalfHourMomentum sessions, no-trade classification, direction, Bars (d/s1_lhmom.py, selected lines)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s1_lhmom.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | grep -E '^(RTH sessions|LHMOM trades|trade entry dates|sessions with an LHMOM|Entry names|Entry time|\(e\)|  no prior|  session ends|  last-stamp|  (2021-11-26|2023-04-05|2024-07-03|2024-11-29|2024-12-24|2025-01-20|2025-06-19|2025-07-03) |direction vs|sessions with r|\(d\)|Bars minus|trades with Bars|   \(2,|fills not equal)'
```

```text
RTH sessions (weekday dates with >=1 bar stamped 09:31..16:00) in range: 1352 first 2021-03-08 last 2026-07-17
LHMOM trades: 1304 distinct entry dates: 1304 dates with >1 trade: []
trade entry dates that are NOT a session: []
sessions with an LHMOM trade: 1304  sessions with none: 48
Entry names: {'LHMomLong': 698, 'LHMomShort': 606} Exit names: {'LHFlat1559': 1304}
Entry time-of-day: {'15:31': 1304}  Exit time-of-day: {'16:00': 1304}
(e) trades with entry/exit outside 15:30-16:00 same day: 0 []
  no prior 16:00 close in data (first session): 1: ['2021-03-08']
  session ends before 15:30 (last RTH bar 13:00): 37: ['2021-05-31', '2021-07-05', '2021-09-06', '2021-11-25', '2022-01-17', '2022-02-21', '2022-05-30', '2022-06-20', '2022-07-04', '2022-09-05', '2022-11-24', '2023-01-16', '2023-02-20', '2023-05-29', '2023-06-19', '2023-07-04', '2023-09-04', '2023-11-23', '2024-01-15', '2024-02-19', '2024-05-27', '2024-06-19', '2024-07-04', '2024-09-02', '2024-11-28', '2025-01-20', '2025-02-17', '2025-05-26', '2025-06-19', '2025-07-04', '2025-09-01', '2025-11-27', '2026-01-19', '2026-02-16', '2026-05-25', '2026-06-19', '2026-07-03']
  session ends before 15:30 (last RTH bar 13:15): 9: ['2021-11-26', '2022-11-25', '2023-07-03', '2023-11-24', '2024-07-03', '2024-11-29', '2024-12-24', '2025-07-03', '2025-11-28']
  session ends before 15:30 (last RTH bar 14:03): 1: ['2023-04-05']
  2021-11-26 Fri last=13:15 nbars0931-1600=225 nextbar_after=None LHMOM_trade=no
  2023-04-05 Wed last=14:03 nbars0931-1600=273 nextbar_after=2023-04-05 20:01:00 LHMOM_trade=no
  2024-07-03 Wed last=13:15 nbars0931-1600=225 nextbar_after=2024-07-03 18:01:00 LHMOM_trade=no
  2024-11-29 Fri last=13:15 nbars0931-1600=225 nextbar_after=2024-11-29 17:58:00 LHMOM_trade=no
  2024-12-24 Tue last=13:15 nbars0931-1600=225 nextbar_after=None LHMOM_trade=no
  2025-01-20 Mon last=13:00 nbars0931-1600=210 nextbar_after=2025-01-20 18:01:00 LHMOM_trade=no
  2025-06-19 Thu last=13:00 nbars0931-1600=210 nextbar_after=2025-06-19 18:01:00 LHMOM_trade=no
  2025-07-03 Thu last=13:15 nbars0931-1600=225 nextbar_after=2025-07-03 18:01:00 LHMOM_trade=no
  last-stamp counts: {'13:00': 37, '13:15': 9, '14:03': 1}
direction vs code rule (15:30-bar close vs most recent prior weekday 16:00 close): mismatches 0 []
sessions with r == 0 exactly: []
(d) Bars column distribution: {30: 1303, 25: 1}
Bars minus count of bar-file stamps in [entry,exit] inclusive: {0: 1304}
trades with Bars!=30 or stamps!=30 or span!=29min: 1
   (2, '2021-03-10 15:31:00', '2021-03-10 16:00:00', 'Bars', 25, 'barfile stamps entry..exit incl', 25, 'missing', ['15:33', '15:44', '15:46', '15:50', '15:58'])
fills not equal to Open +/- 2 ticks (adverse): 218  breakdown (which, fill==bar High(buy)/Low(sell), fill==Open): {('E', True, True): 84, ('X', True, True): 36, ('X', True, False): 42, ('E', True, False): 56}
```

### K16 - Missing stamps inside sessions and trades that span them (d/s2_gaps.py, March-2021 runs and the 48-date list omitted)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s2_gaps.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | grep -v -E '^    2021-03-(08|09|10) |^   20[0-9-]+ (Mon|Tue|Wed|Thu|Fri)$'
```

```text
weekdays in range with ZERO bars stamped 09:31..16:00: 48
weekend bars stamped 09:31..16:00 in range: 201 total volume 360 max per-date bars 6

all missing 1-min stamps inside sessions (09:31..session last bar), range 2021-03-08 2026-07-17 : 184 in 67 runs
    2021-08-24 11:21-11:21 NEW len=1
    2021-08-24 13:35-13:35 NEW len=1
    2021-08-25 15:03-15:14 NEW len=12
    2022-05-23 12:58-12:58 NEW len=1
    2022-08-03 11:26-11:26 NEW len=1
    2022-08-30 09:51-09:51 NEW len=1
    2024-07-19 09:58-10:07 NEW len=10
    2024-07-25 10:43-10:45 NEW len=3
    2024-07-25 10:48-10:49 NEW len=2
    2024-08-02 11:55-12:02 NEW len=8
    2024-08-05 10:47-10:48 NEW len=2
    2024-09-19 13:55-13:57 NEW len=3
    2025-10-13 13:51-13:51 NEW len=1
    2026-04-02 09:36-09:36 NEW len=1
    2026-06-11 10:33-10:44 NEW len=12
    2026-07-17 10:59-12:06 NEW len=68
2023-04-05 stamps 14:04..16:00 present: 0
2026-07-17 stamps 11:01..12:01 present: []

== BASELINE: trades 1190; trades with >=1 missing stamp between entry and exit (inclusive, weekday 09:31-16:00): 3
    #286 2022-08-03 11:26-11:26 NEW
    #763 2024-08-02 11:55-12:02 NEW
    #789 2024-09-19 13:55-13:57 NEW
   trades spanning more than one date: 0 []
== OPPBAND: trades 810; trades with >=1 missing stamp between entry and exit (inclusive, weekday 09:31-16:00): 6
    #205 2022-08-03 11:26-11:26 NEW
    #525 2024-07-25 10:43-10:45 NEW; 2024-07-25 10:48-10:49 NEW
    #529 2024-08-02 11:55-12:02 NEW
    #546 2024-09-19 13:55-13:57 NEW
    #700 2025-10-13 13:51-13:51 NEW
    #800 2026-06-11 10:33-10:44 NEW
   trades spanning more than one date: 0 []
== FLAT1559: trades 1190; trades with >=1 missing stamp between entry and exit (inclusive, weekday 09:31-16:00): 3
    #286 2022-08-03 11:26-11:26 NEW
    #763 2024-08-02 11:55-12:02 NEW
    #789 2024-09-19 13:55-13:57 NEW
   trades spanning more than one date: 0 []
== LHMOM: trades 1304; trades with >=1 missing stamp between entry and exit (inclusive, weekday 09:31-16:00): 1
    #2 2021-03-10 15:33-15:33 NEW; 2021-03-10 15:44-15:44 NEW; 2021-03-10 15:46-15:46 NEW; 2021-03-10 15:50-15:50 NEW; 2021-03-10 15:58-15:58 NEW
   trades spanning more than one date: 0 []

missing decision (:00/:30) and fill (:01/:31) stamps inside session spans:
    2024-07-19 10:00:00 NEW []
    2024-07-19 10:01:00 KNOWN []
    2024-08-02 12:00:00 NEW ['BASELINE#763 open', 'OPPBAND#529 open', 'FLAT1559#763 open']
    2024-08-02 12:01:00 KNOWN ['BASELINE#763 open', 'OPPBAND#529 open', 'FLAT1559#763 open']
    2026-07-17 11:00:00 NEW []
    2026-07-17 11:01:00 KNOWN []
    2026-07-17 11:30:00 KNOWN []
    2026-07-17 11:31:00 KNOWN []
    2026-07-17 12:00:00 KNOWN []
    2026-07-17 12:01:00 KNOWN []

NAB-family trades with entry or exit stamp minute not in {:01,:31} (exits at 16:00 also listed separately as count):
  BASELINE: at 16:00: {'exit Exit on session close': 423}; other: 6 [(122, 'exit', '2021-11-26 12:15:00', 'Exit on session close'), (454, 'exit', '2023-04-05 14:03:00', 'Exit on session close'), (742, 'exit', '2024-07-03 12:15:00', 'Exit on session close'), (834, 'exit', '2024-11-29 12:15:00', 'Exit on session close'), (843, 'exit', '2024-12-24 12:15:00', 'Exit on session close'), (963, 'exit', '2025-07-03 12:15:00', 'Exit on session close')]
  OPPBAND: at 16:00: {'exit Exit on session close': 784}; other: 8 [(90, 'exit', '2021-11-26 12:15:00', 'Exit on session close'), (312, 'exit', '2023-04-05 14:03:00', 'Exit on session close'), (514, 'exit', '2024-07-03 12:15:00', 'Exit on session close'), (576, 'exit', '2024-11-29 12:15:00', 'Exit on session close'), (583, 'exit', '2024-12-24 12:15:00', 'Exit on session close'), (594, 'exit', '2025-01-20 12:00:00', 'Exit on session close'), (652, 'exit', '2025-06-19 12:00:00', 'Exit on session close'), (657, 'exit', '2025-07-03 12:15:00', 'Exit on session close')]
  FLAT1559: at 16:00: {'exit FlatEOD': 423}; other: 6 [(122, 'exit', '2021-11-26 12:15:00', 'Exit on session close'), (454, 'exit', '2023-04-05 14:03:00', 'Exit on session close'), (742, 'exit', '2024-07-03 12:15:00', 'Exit on session close'), (834, 'exit', '2024-11-29 12:15:00', 'Exit on session close'), (843, 'exit', '2024-12-24 12:15:00', 'Exit on session close'), (963, 'exit', '2025-07-03 12:15:00', 'Exit on session close')]
```

### K17 - Count of missing-stamp runs on 2021-03-08..10 (d/s2_gaps.py)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s2_gaps.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | grep -cE '^    2021-03-(08|09|10) [0-9:]+-[0-9:]+ (NEW|KNOWN) len='
```

```text
51
```

### K18 - Known gaps, actual extents and the trades on those dates (d/s3_follow.py sections 1-2)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s3_follow.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | sed -n '/^(1)/,/^(3)/p'
```

```text
(1) known-gap descriptions vs actual missing runs in 09:31-16:00:
   2023-04-05 described (14, 3)-(20, 1): missing RTH stamps 117: first 14:04 last 16:00
      BASELINE#454 Short 10:01 S -> 14:03 Exit on session close Bars=243
      OPPBAND#312 Short 10:01 S -> 14:03 Exit on session close Bars=243
      FLAT1559#454 Short 10:01 S -> 14:03 Exit on session close Bars=243
   2024-07-19 described (10, 1)-(10, 1): missing RTH stamps 10: first 09:58 last 10:07
      BASELINE#754 Short 10:31 S -> 11:01 XS Bars=31
      BASELINE#755 Short 11:31 S -> 12:01 XS Bars=31
      BASELINE#756 Short 12:31 S -> 15:31 XS Bars=181
      OPPBAND#523 Short 10:31 S -> 16:00 Exit on session close Bars=330
      FLAT1559#754 Short 10:31 S -> 11:01 XS Bars=31
      FLAT1559#755 Short 11:31 S -> 12:01 XS Bars=31
      FLAT1559#756 Short 12:31 S -> 15:31 XS Bars=181
      LHMOM#825 Short 15:31 LHMomShort -> 16:00 LHFlat1559 Bars=30
   2024-08-02 described (12, 1)-(12, 1): missing RTH stamps 8: first 11:55 last 12:02
      BASELINE#763 Short 10:01 S -> 12:31 XS Bars=143
      BASELINE#764 Short 13:01 S -> 14:31 XS Bars=91
      BASELINE#765 Short 15:01 S -> 15:31 XS Bars=31
      OPPBAND#529 Short 10:01 S -> 16:00 Exit on session close Bars=352
      FLAT1559#763 Short 10:01 S -> 12:31 XS Bars=143
      FLAT1559#764 Short 13:01 S -> 14:31 XS Bars=91
      FLAT1559#765 Short 15:01 S -> 15:31 XS Bars=31
      LHMOM#835 Short 15:31 LHMomShort -> 16:00 LHFlat1559 Bars=30
   2026-07-17 described (11, 1)-(12, 1): missing RTH stamps 68: first 10:59 last 12:06
      LHMOM#1304 Short 15:31 LHMomShort -> 16:00 LHFlat1559 Bars=30

(2) trades on other dates with a missing :00/:01/:30/:31 stamp:
    2021-03-08
    2021-03-10
      LHMOM#2 Short 15:31 LHMomShort -> 16:00 LHFlat1559 Bars=25

(3) zero-RTH weekdays: bars at any time that date, and any CSV trade:
```

### K19 - Weekdays with no RTH bars: dates that have some bars, and trade count (d/s3_follow.py section 3)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s3_follow.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | grep -E 'bars_any_time=' | awk '{n++; if ($0 ~ /trades=\[\]$/) e++} !/bars_any_time=0 /{print} END{print "zero-RTH weekdays listed:", n, "| with trades=[]:", e}'
```

```text
   2021-04-02 Fri bars_any_time=552 trades=[]
   2021-06-10 Thu bars_any_time=241 trades=[]
   2021-12-09 Thu bars_any_time=299 trades=[]
   2022-03-10 Thu bars_any_time=298 trades=[]
   2022-06-09 Thu bars_any_time=240 trades=[]
   2022-09-08 Thu bars_any_time=215 trades=[]
   2022-12-26 Mon bars_any_time=359 trades=[]
   2023-01-02 Mon bars_any_time=359 trades=[]
   2023-04-07 Fri bars_any_time=555 trades=[]
   2023-12-25 Mon bars_any_time=359 trades=[]
   2024-01-01 Mon bars_any_time=359 trades=[]
   2024-12-16 Mon bars_any_time=299 trades=[]
   2024-12-25 Wed bars_any_time=359 trades=[]
   2025-01-01 Wed bars_any_time=359 trades=[]
   2025-01-09 Thu bars_any_time=930 trades=[]
   2025-03-17 Mon bars_any_time=241 trades=[]
   2025-09-15 Mon bars_any_time=241 trades=[]
   2026-01-01 Thu bars_any_time=359 trades=[]
   2026-04-03 Fri bars_any_time=551 trades=[]
   2026-06-12 Fri bars_any_time=1 trades=[]
zero-RTH weekdays listed: 48 | with trades=[]: 48
```

### K20 - Bar-file holes over 3 days; Bars column vs bar stamps (d/s4_extents.py)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s4_extents.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d
```

```text
weekdays 2021-03-08..2026-07-17 inclusive: 1400
bar-file holes longer than 3 days (last bar before -> first bar after):
    2021-09-09 19:59:00 -> 2021-09-27 00:01:00 gap 17 days, 4:02:00
    2021-12-23 17:00:00 -> 2021-12-26 18:01:00 gap 3 days, 1:01:00
    2022-12-23 17:00:00 -> 2022-12-26 18:01:00 gap 3 days, 1:01:00
    2022-12-30 17:00:00 -> 2023-01-02 18:01:00 gap 3 days, 1:01:00
    2023-12-22 17:00:00 -> 2023-12-25 18:01:00 gap 3 days, 1:01:00
    2025-12-14 18:59:00 -> 2026-01-01 18:01:00 gap 17 days, 23:02:00
  2021-06-10: bars that date 241 first 00:00:00 last 23:59:00
  2025-03-17: bars that date 241 first 00:00:00 last 23:59:00
  2026-06-12: bars that date 1 first 00:00:00 last 00:00:00
Bars column vs count of bar-file stamps in [entry,exit] inclusive, per CSV:
   BASELINE: diff counts {0: 1190} examples []
   OPPBAND: diff counts {0: 810} examples []
   FLAT1559: diff counts {0: 1190} examples []
   LHMOM: diff counts {0: 1304} examples []
```

### K21 - Code defaults and exit names in the repo source (not the VM copies)

```sh
grep -n -E '^\s*(ExitMode|Contracts) *=|IsExitOnSessionCloseStrategy *=|ExitOnSessionCloseSeconds *=|Exit(Long|Short)\("|const int (FlattenMod|FlatMod) |if \(mod >= FlattenMod\)' /Volumes/Sensidine/Praxis.build/ninjascript/PraxisNoiseAreaBreakout.cs /Volumes/Sensidine/Praxis.build/ninjascript/PraxisNoiseAreaBreakout_OppBand.cs /Volumes/Sensidine/Praxis.build/ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs /Volumes/Sensidine/Praxis.build/ninjascript/PraxisLastHalfHourMomentum.cs | sed 's#/Volumes/Sensidine/Praxis.build/ninjascript/##' | LC_ALL=C tr -c '\n -~' '?' | sort -t: -k1,1 -k2,2n
```

```text
PraxisLastHalfHourMomentum.cs:55://   * Exit: any bar with mod >= FlatMod while not flat -> ExitLong/ExitShort("LHFlat1559").
PraxisLastHalfHourMomentum.cs:58://   * IsExitOnSessionCloseStrategy = true is a BACKSTOP only (ExitOnSessionCloseSeconds = 30, as the base).
PraxisLastHalfHourMomentum.cs:127:??private const int FlatMod   = 16 * 60 - 1;    // 959 ??? the 15:59 bar; exit fills at the 16:00 bar Open (INFERRED)
PraxisLastHalfHourMomentum.cs:148:????IsExitOnSessionCloseStrategy              = true;   // BACKSTOP only; the explicit 15:59 flat is primary
PraxisLastHalfHourMomentum.cs:149:????ExitOnSessionCloseSeconds                 = 30;     // same value as PraxisNoiseAreaBreakout.cs
PraxisLastHalfHourMomentum.cs:155:????Contracts = 1;   // position sizing only (NOT a rule knob); the paper is unit exposure (Eq. 12)
PraxisLastHalfHourMomentum.cs:194:?????ExitLong("LHStaleFlat", "LHMomLong");
PraxisLastHalfHourMomentum.cs:200:?????ExitShort("LHStaleFlat", "LHMomShort");
PraxisLastHalfHourMomentum.cs:209:?????ExitLong("LHFlat1559", "LHMomLong");
PraxisLastHalfHourMomentum.cs:211:?????ExitShort("LHFlat1559", "LHMomShort");
PraxisNoiseAreaBreakout.cs:108:????IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
PraxisNoiseAreaBreakout.cs:109:????ExitOnSessionCloseSeconds                 = 30;
PraxisNoiseAreaBreakout.cs:118:????ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec ??4 p.13 ??? paper's PREFERRED exit. The only knob.
PraxisNoiseAreaBreakout.cs:119:????Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (??3 p.15) not ported here.
PraxisNoiseAreaBreakout.cs:211:?????ExitLong("XL", "");
PraxisNoiseAreaBreakout.cs:219:?????ExitShort("XS", "");
PraxisNoiseAreaBreakout.cs:288:????ExitLong("FlatEOD", "");
PraxisNoiseAreaBreakout.cs:290:????ExitShort("FlatEOD", "");
PraxisNoiseAreaBreakout_Flat1559.cs:44:// IsExitOnSessionCloseStrategy = true is kept as the backstop.
PraxisNoiseAreaBreakout_Flat1559.cs:91:??private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET ??? variant 7zq: submit the flat one bar early
PraxisNoiseAreaBreakout_Flat1559.cs:141:????IsExitOnSessionCloseStrategy              = true;   // backstop; explicit flat (submitted 15:59) is primary
PraxisNoiseAreaBreakout_Flat1559.cs:142:????ExitOnSessionCloseSeconds                 = 30;
PraxisNoiseAreaBreakout_Flat1559.cs:151:????ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec ??4 p.13 ??? paper's PREFERRED exit. The only knob.
PraxisNoiseAreaBreakout_Flat1559.cs:152:????Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (??3 p.15) not ported here.
PraxisNoiseAreaBreakout_Flat1559.cs:227:???if (mod >= FlattenMod)
PraxisNoiseAreaBreakout_Flat1559.cs:249:?????ExitLong("XL", "");
PraxisNoiseAreaBreakout_Flat1559.cs:257:?????ExitShort("XS", "");
PraxisNoiseAreaBreakout_Flat1559.cs:326:????ExitLong("FlatEOD", "");
PraxisNoiseAreaBreakout_Flat1559.cs:328:????ExitShort("FlatEOD", "");
PraxisNoiseAreaBreakout_OppBand.cs:131:????IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
PraxisNoiseAreaBreakout_OppBand.cs:132:????ExitOnSessionCloseSeconds                 = 30;
PraxisNoiseAreaBreakout_OppBand.cs:141:????ExitMode      = PraxisNoiseExitMode.OppBand;    // VARIANT 7zq default (base default BandOrVWAP, spec ??4 p.13). The only knob.
PraxisNoiseAreaBreakout_OppBand.cs:142:????Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (??3 p.15) not ported here.
PraxisNoiseAreaBreakout_OppBand.cs:235:?????ExitLong("XL", "");
PraxisNoiseAreaBreakout_OppBand.cs:243:?????ExitShort("XS", "");
PraxisNoiseAreaBreakout_OppBand.cs:314:????ExitLong("FlatEOD", "");
PraxisNoiseAreaBreakout_OppBand.cs:316:????ExitShort("FlatEOD", "");
```

### K22 - OppBand largest loss row

```sh
grep -F -- '-$19592.96' "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" | LC_ALL=C tr -c '\n -~' '?'
```

```text
627,NQCONTROW SEP25,Backtest,PraxisNoiseAreaBreakout_OppBand,Long,1,19483.25,18503.75,2025-04-08 10:01:00 AM,2025-04-08 3:31:00 PM,L,XL,-$19592.96,$187449.08,$2.96,$0.00,$0.00,$0.00,$0.00,$22230.00,$2180.00,$21772.96,331,?
```

### K23 - The C4 settings line used as the required list (notes-2 line 111; non-ASCII shown by Unicode name)

```sh
python3 -I -c "import sys,unicodedata; l=open(sys.argv[1],encoding='utf-8').read().splitlines()[110]; print(''.join(c if ord(c)<128 else '<'+unicodedata.name(c)+'>' for c in l))" /Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-voice-session-notes-2.md
```

```text
- Settings, same as the 10-31 run: NQCONTROW SEP25 <MIDDLE DOT> Last <MIDDLE DOT> Minute 1 <MIDDLE DOT> 2021-03-08 <RIGHTWARDS ARROW> 2026-07-17 <MIDDLE DOT> CME US Index Futures RTH <MIDDLE DOT> Break at EOD <CHECK MARK> <MIDDLE DOT> Include commission <CHECK MARK> PRAXIS <MIDDLE DOT> Max bars look back 256 <MIDDLE DOT> Bars required 20 <MIDDLE DOT> Standard (Fastest) <MIDDLE DOT> Fill limit on touch <BALLOT BOX> <MIDDLE DOT> Slippage 2 <MIDDLE DOT> Entries per direction 1 <MIDDLE DOT> All entries <MIDDLE DOT> Exit on session close <CHECK MARK> <MIDDLE DOT> Set order quantity Strategy <MIDDLE DOT> DAY <MIDDLE DOT> BandOrVWAP <MIDDLE DOT> Contracts 1.
```

### K24 - NoiseAreaBreakout trades on short-session days, with the day's last RTH bar (d/s3_follow.py section 7)

```sh
python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d/s3_follow.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/tsr/d | sed -n '/^(7)/,/^(8)/p'
```

```text
(7) NAB trades on short-session days (last RTH bar < 16:00):
   2021-11-26 last RTH bar 13:15
      BASELINE#122 Short 11:01 S -> 12:15 Exit on session close Bars=75
      OPPBAND#90 Short 11:01 S -> 12:15 Exit on session close Bars=75
      FLAT1559#122 Short 11:01 S -> 12:15 Exit on session close Bars=75
   2023-04-05 last RTH bar 14:03
      BASELINE#454 Short 10:01 S -> 14:03 Exit on session close Bars=243
      OPPBAND#312 Short 10:01 S -> 14:03 Exit on session close Bars=243
      FLAT1559#454 Short 10:01 S -> 14:03 Exit on session close Bars=243
   2024-07-03 last RTH bar 13:15
      BASELINE#742 Long 11:01 L -> 12:15 Exit on session close Bars=75
      OPPBAND#514 Long 11:01 L -> 12:15 Exit on session close Bars=75
      FLAT1559#742 Long 11:01 L -> 12:15 Exit on session close Bars=75
   2024-11-29 last RTH bar 13:15
      BASELINE#834 Long 11:31 L -> 12:15 Exit on session close Bars=45
      OPPBAND#576 Long 11:31 L -> 12:15 Exit on session close Bars=45
      FLAT1559#834 Long 11:31 L -> 12:15 Exit on session close Bars=45
   2024-12-24 last RTH bar 13:15
      BASELINE#843 Long 10:01 L -> 12:15 Exit on session close Bars=135
      OPPBAND#583 Long 10:01 L -> 12:15 Exit on session close Bars=135
      FLAT1559#843 Long 10:01 L -> 12:15 Exit on session close Bars=135
   2025-01-20 last RTH bar 13:00
      BASELINE#863 Long 10:01 L -> 10:31 XL Bars=31
      OPPBAND#594 Long 10:01 L -> 12:00 Exit on session close Bars=120
      FLAT1559#863 Long 10:01 L -> 10:31 XL Bars=31
   2025-06-19 last RTH bar 13:00
      BASELINE#955 Short 10:01 S -> 11:01 XS Bars=61
      OPPBAND#652 Short 10:01 S -> 12:00 Exit on session close Bars=120
      FLAT1559#955 Short 10:01 S -> 11:01 XS Bars=61
   2025-07-03 last RTH bar 13:15
      BASELINE#963 Long 10:01 L -> 12:15 Exit on session close Bars=135
      OPPBAND#657 Long 10:01 L -> 12:15 Exit on session close Bars=135
      FLAT1559#963 Long 10:01 L -> 12:15 Exit on session close Bars=135

(8) dates with ANY NAB trade entry, per CSV, count of distinct dates: {'BASELINE': 792, 'OPPBAND': 792, 'FLAT1559': 792, 'LHMOM': 1304}
```

### K25 - Exit-time text in the CSVs for the FlatEOD (Flat1559) and 16:00 session-close (baseline) exits

```sh
cut -d, -f10,12 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" | grep -F ',FlatEOD' | sed 's/^[0-9-]* //' | sort | uniq -c; cut -d, -f10,12 "/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" | grep -F ',Exit on session close' | sed 's/^[0-9-]* //' | sort | uniq -c
```

```text
 423 4:00:00 PM,FlatEOD
   5 12:15:00 PM,Exit on session close
   1 2:03:00 PM,Exit on session close
 423 4:00:00 PM,Exit on session close
```
