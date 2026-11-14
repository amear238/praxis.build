# 2026-11-13 strategy-review-index, worker4 (Q1 part A): the 2026-11-01 Strategy Analyzer runs and their status

## Task

- Unit: `2026-11-13-strategy-review-index`, worker4, Q1 part A. Mode: BUILD (read-only research).
- Working dir `/Volumes/Sensidine/Praxis.build`, branch main, HEAD 9ff8a48.
- Scope: the four 2026-11-01 Strategy Analyzer runs (baseline/BandOrVWAP, OppBand, Flat1559, LastHalfHourMomentum), plus the run-3/run-4 record the brief named. For each run: settings as recorded, the headline figures quoted exactly with file:line, who produced them, and the current status with the record that set it.
- The only file written is this report. No existing file was edited and nothing was staged.
- Grades used here:
  - QUOTED: copied from the cited line.
  - INFERRED: my own reasoning, with the basis stated.
  - NOT IN RECORD: searched for and not found; the search is shown.
- This index does not rank the runs. Ruling R-1101-5 forbids a ranking (cited at three-strategy-results :12 and csv-analyses :20).

Abbreviations:
- **TSR** = `docs/reports/2026-11-01-three-strategy-results.md`
- **CSVA** = `docs/reports/2026-11-01-csv-analyses.md`
- **R3R** = `docs/reports/2026-10-30-run3-backtest-screenshot-record.md`
- **N2** = `docs/reports/2026-10-31-voice-session-notes-2.md`
- **DEC** = `DECISIONS.md`
- **DLOG** = `DECISION_LOG.md`

## Findings table

**Settings shared by the four 2026-11-01 runs:**
- Instrument `NQCONTROW SEP25`, Account `Backtest` on every CSV row (TSR :41).
- Shown in the screenshots (REPORTED BY AMEAR): Last / Minute / 1; date range `2021-03-08 -> 2026-07-17`; order fill resolution `Standard (Fastest)`; slippage `2`; commission template `PRAXIS`; Contracts 1. Sources: the OppBand settings table at TSR :86-:104, the Flat1559 rows at TSR :192-:210 and the LastHalfHourMomentum rows at TSR :310-:328.
- The commission rate inside the PRAXIS template is NOT SHOWN in any screenshot (TSR :105, :211, :329).
- The CSV Commission column is $2.96 on every row in all four files (TSR :77, :125, :231, :349).
- The baseline has no settings screenshot (TSR :37). Its settings rest on Amear's C4 notes at N2 :111: "NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · ... · Standard (Fastest) · ... · Slippage 2 · ... · BandOrVWAP · Contracts 1."

**Where the figures come from:**
- The four 2026-11-01 runs use the CSV comparison table at TSR :400-:405 ([K08], graded OBSERVED from the CSVs). Each run's "All" row confirms them: TSR :73, :116, :222 and :340.
- Max DD is the drawdown of closed-trade cumulative net (TSR :77).
- Input CSV rows are TSR :29-:32. Screenshot rows are TSR :33-:35.

| run | date / source file | run-specific settings | trades | net | PF | max DD | win % | avg trade | produced by | status (record) |
|---|---|---|---|---|---|---|---|---|---|---|
| Baseline `PraxisNoiseAreaBreakout`, Exit mode BandOrVWAP (re-run "0-S", C4) | 2026-11-01. CSV `NinjaTrader Grid 2026-11-01 07-10 AM.csv` (TSR :29). C4 is under N2 :94, "2026-11-01 session" | BandOrVWAP, Contracts 1 (N2 :111). No screenshot (TSR :37) | 1190 | $197327.60 | 1.29 | -$45282.04 | 40.67% | $165.82 | Amear's hand run in the NT8 Strategy Analyzer, exported to CSV. C4 values are "from Amear's screenshot" (N2 :110). Recomputed Mac-side by praxis-manager workers: "all 22 compared values MATCH" (TSR :67). Gate 0 re-check MATCH (CSVA :41) | No DEC line retires or adopts it. It is one of the walk-forward exit policies: "exit policies BandOrVWAP / OppBand / Flat1559" (D-2026-11-06-B Ruling 4, DEC :1077). Bead q36 (OPEN): "the Future-row baseline is judged on its own" |
| OppBand `PraxisNoiseAreaBreakout_OppBand` | 2026-11-01. CSV `... 07-57 AM.csv` (TSR :30). Screenshot 7.57.06 (TSR :33) | Exit mode OppBand (TSR :103) | 810 | $210182.40 | 1.26 | -$50748.88 | 58.02% | $259.48 | Amear's hand run, plus a Summary($)/Settings screenshot. Mac recomputation: TSR :116. Screenshot reconciliation "48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE" (TSR :121). Gate 0 MATCH (CSVA :42) | No retirement found. Definition ruled in D-2026-11-07-A Q4, DEC :1222: "Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs." It is one of the walk-forward exit policies (DEC :1077) |
| Flat1559 `PraxisNoiseAreaBreakout_Flat1559` | 2026-11-01. CSV `... 07-59 AM.csv` (TSR :31). Screenshot 7.58.40 (TSR :34) | Exit mode BandOrVWAP (TSR :209). Flattens on the 15:59 bar | 1190 | $193017.60 | 1.28 | -$40637.04 | 40.50% | $162.20 | Amear's hand run, plus a screenshot. Mac recomputation: TSR :222. Reconciliation "48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE" (TSR :227). Gate 0 MATCH (CSVA :43) | No retirement found. D-2026-11-02-C R-VN3-4, DEC :504: "the fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is unchanged." D-2026-11-07-A Q5, DEC :1223: "Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs." |
| LastHalfHourMomentum `PraxisLastHalfHourMomentum` | 2026-11-01. CSV `... 08-00 AM.csv` (TSR :32). Screenshot 8.00.21 (TSR :35) | No Exit mode option. Contracts 1 (TSR :327-:328) | 1304 | -$76009.84 | 0.84 | -$99806.96 | 47.62% | -$58.29 | Amear's hand run, plus a screenshot. Mac recomputation: TSR :340. Reconciliation "48 MATCH, 3 MISMATCH, 3 NOT DERIVABLE" (TSR :345). Gate 0 MATCH (CSVA :44) | **RETIRED**: D-2026-11-02-A, DEC :368. Status line DEC :371 is quoted below. Bead `Praxis_build-afe` is CLOSED |
| Run 3 (before 11-01; context only), `PraxisNoiseAreaBreakout` BandOrVWAP | 2026-10-30 (R3R :3) | Instrument `NQCONT` (R3R :16). Start 2021-03-08 / End 2026-07-17 (R3R :20-:21). Trading hours **CME FX Futures RTH** (R3R :22). PRAXIS (R3R :25). Standard (Fastest) (R3R :28). Slippage 2 (R3R :30). Contracts 1 (R3R :15) | 1075 (R3R :55) | $1,281.61 (R3R :41) | 1.04 (R3R :45) | −$4,051.57 (R3R :46) | 38.05% (R3R :56) | $1.19 (R3R :61) | Amear's screenshot, transcribed by praxis-master: "OBSERVED BY THE MASTER in the image Amear pasted" (R3R :3) | **INVALID**: "Run 3 is recorded as INVALID, not as a result." (R3R :106). Retired as a baseline by R-VM-6 (DLOG :647). There is no DEC entry for R-VM-6 (the grep below returned nothing) |
| Run 4 (before 11-01; context only) | after the 2026-10-30T22:22Z ruling (R3R :106) | `NQCONT 1-min · BandOrVWAP · 1 contract · Slippage 2 · Standard · PRAXIS commission · trading hours CME US Index Futures RTH` (R3R :110) | 1,211 | $3,136.84 | 1.08 | −$4,108.84 | NOT IN RECORD on R3R :111 | $2.59 | "REPORTED BY AMEAR from his screenshot; no Claude has seen the image" (R3R :109). Figures at R3R :111 | Retired as a baseline, not voided. DLOG :647: "R-VM-6 RULED: \"Stands — retire the stock-row runs.\"". No DEC entry |

## Status lines

- **LastHalfHourMomentum.**
  - DEC :368: "## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)"
  - DEC :371: "**Status:** RULED by Amear — R-VN3-1. Ledger authorisation (S5): DECISION_LOG row `2026-11-02T21:23:45Z` (WHO: amear). Appended 2026-11-02 by praxis-manager, unit `2026-11-02-r-vn3-1-filing`."
  - The entry's context line cites TSR :405 (DEC :378).
- **OppBand, Flat1559 and the baseline.**
  - DEC :389: "Filer's reading, not a ruling: notes-3 line 10 names only \"the last half hour\", so the two Noise-Area variants (OppBand, Flat1559) and the baseline are outside this entry."
  - I found no DEC line that retires, adopts or promotes any of the three.
  - The rulings that touch them define the variants or list them as exit policies (DEC :504, :1077, :1222, :1223). The evidence does not support reading those rulings as "active candidate" or "selected", and I make no such claim.
- **Run 3, run 4 and the Stock-row 0-S run.** DLOG :647: "Runs 3, 4 and Stock-row 0-S are retired as baselines (and as evidence about fills), not voided". This appears in DLOG only.
- **Report grades (outside scope; I did not open the audit).**
  - TSR :6: "Status: NOT audited at the time of writing."
  - CSVA :20 says TSR was "audited at 8ca9861". UNVERIFIED here.
  - CSVA's own grade line, CSVA :11: "**Grade:** ungraded at time of writing".

## Evidence

All commands ran from the working dir. Output is pasted as returned; where I selected lines from a longer output, the label says so.

```
$ sed -n '396,405p' docs/reports/2026-11-01-three-strategy-results.md   (from the run of sed -n '81,108p;396,434p')
## Comparison (OBSERVED, [K08])

Baseline vs the three runs, from the CSVs. Listed in file order. This is not a ranking (R-1101-5).

| run | trades | net | PF | max DD (i) | max DD (ii) | win % | avg trade | largest win | largest win as % of net |
|---|---|---|---|---|---|---|---|---|---|
| BASELINE (`PraxisNoiseAreaBreakout`, BandOrVWAP) | 1190 | $197327.60 | 1.29 | -$45282.04 | -$45282.04 | 40.67% | $165.82 | $35887.04 | 18.19% |
| OPPBAND | 810 | $210182.40 | 1.26 | -$50748.88 | -$50748.88 | 58.02% | $259.48 | $36087.04 | 17.17% |
| FLAT1559 | 1190 | $193017.60 | 1.28 | -$40637.04 | -$40637.04 | 40.50% | $162.20 | $36472.04 | 18.90% |
| LHMOM (LastHalfHourMomentum) | 1304 | -$76009.84 | 0.84 | -$99806.96 | -$99806.96 | 47.62% | -$58.29 | $3852.04 | -5.07% (not meaningful) |
```

```
$ grep -n -E '^## |^### |^\| All|Settings|commission|Commission|slippage|Slippage|Order fill|date range|From|To |Contracts|Quantity' docs/reports/2026-11-01-three-strategy-results.md | sed -n '1,120p'   (selected lines)
73:| All | 1190 | $197327.60 | $878467.36 | -$681139.76 | $3522.40 | 1.29 | 484/706/0 | 40.67% | $35887.04 | -$5407.96 | $165.82 | -$45282.04 | -$45282.04 |
116:| All | 810 | $210182.40 | $1009483.80 | -$799301.40 | $2397.60 | 1.26 | 470/340/0 | 58.02% | $36087.04 | -$19592.96 | $259.48 | -$50748.88 | -$50748.88 |
125:- Rows with Commission != $2.96: 0. Sum $2397.60 == 810 x 2.96 (True).
222:| All | 1190 | $193017.60 | $871258.28 | -$678240.68 | $3522.40 | 1.28 | 482/708/0 | 40.50% | $36472.04 | -$5407.96 | $162.20 | -$40637.04 | -$40637.04 |
231:- Rows with Commission != $2.96: 0. Sum $3522.40 == 1190 x 2.96 (True).
340:| All | 1304 | -$76009.84 | $411326.84 | -$487336.68 | $3859.84 | 0.84 | 621/683/0 | 47.62% | $3852.04 | -$5537.96 | -$58.29 | -$99806.96 | -$99806.96 |
349:- Rows with Commission != $2.96: 0. Sum $3859.84 == 1304 x 2.96 (True).
```

```
$ grep -n 'NinjaTrader Grid 2026-11-01' docs/reports/2026-11-01-three-strategy-results.md | head -4 | cut -c1-90
29:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `42
30:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `420
31:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a
32:| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentu
```

```
$ sed -n '186p;192,194p;199p;201p;203p;209p;304p;310,312p;317p;319p;321p' docs/reports/2026-11-01-three-strategy-results.md | nl -ba | cut -c1-220   (nl numbers are positions within the selection, not file lines; blank and lookback rows omitted)
     2	| Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
     3	| Price based on / Type / Value | Last / Minute / 1 | Last / Minute / 1 | MATCH |
     4	| Date range | 2021-03-08 -> 2026-07-17 | 2021-03-08 -> 2026-07-17 | MATCH |
     6	| Order fill resolution | Standard (Fastest) | Standard (Fastest) | MATCH |
     7	| Slippage | 2 | 2 | MATCH |
     8	| Exit mode | code default `BandOrVWAP` (`PraxisNoiseAreaBreakout_Flat1559.cs:151` [K21]) | BandOrVWAP | MATCH |
    10	| Instrument | NQCONTROW SEP25 | NQCONTROW SEP25 | MATCH |
    11	| Price based on / Type / Value | Last / Minute / 1 | Last / Minute / 1 | MATCH |
    12	| Date range | 2021-03-08 -> 2026-07-17 | 2021-03-08 -> 2026-07-17 | MATCH |
    14	| Order fill resolution | Standard (Fastest) | Standard (Fastest) | MATCH |
    15	| Slippage | 2 | 2 | MATCH |
```

```
$ grep -n -E 'MATCH|MISMATCH' docs/reports/2026-11-01-csv-analyses.md | head -40   (first four lines)
41:| R0 | 197327.60 | 1.29 | -45282.04 | 197327.60/1.29/-45282.04 | MATCH |
42:| R1 | 210182.40 | 1.26 | -50748.88 | 210182.40/1.26/-50748.88 | MATCH |
43:| R2 | 193017.60 | 1.28 | -40637.04 | 193017.60/1.28/-40637.04 | MATCH |
44:| R3 | -76009.84 | 0.84 | -99806.96 | -76009.84/0.84/-99806.96 | MATCH |
```

```
$ sed -n '111p' docs/reports/2026-10-31-voice-session-notes-2.md | cut -c1-900
- Settings, same as the 10-31 run: NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · Break at EOD ✓ · Include commission ✓ PRAXIS · Max bars look back 256 · Bars required 20 · Standard (Fastest) · Fill limit on touch ☐ · Slippage 2 · Entries per direction 1 · All entries · Exit on session close ✓ · Set order quantity Strategy · DAY · BandOrVWAP · Contracts 1.
```

```
$ grep -n -E '^#|C4|0-S' docs/reports/2026-10-31-voice-session-notes-2.md | cut -c1-260 | head -20   (selected lines)
94:## 3. 2026-11-01 session — commission fix and re-run
110:### C4 — re-run 0-S on NQCONTROW SEP25: PASS (values from Amear's screenshot)
145:- **Totals match C4:** 1,190 trades · 556 L / 634 S · net $197,327.60 · 484 W / 706 L / 0 even.
```

```
$ grep -n -i -E 'trades|net|profit factor|drawdown|profitable|avg|commission|slippage|instrument|date range|fill' docs/reports/2026-10-30-run3-backtest-screenshot-record.md | head -40   (selected lines)
16:| Data Series | Instrument | NQCONT |
41:| Total net profit | $1,281.61 | $2,721.21 | −$1,439.60 |
45:| Profit factor | 1.04 | 1.18 | 0.93 |
46:| Max. drawdown | −$4,051.57 | −$1,713.82 | −$3,179.91 |
55:| Total # of trades | 1075 | 522 | 553 |
56:| Percent profitable | 38.05% | 43.87% | 32.55% |
61:| Avg. trade | $1.19 | $5.21 | −$2.60 |
110:2021-03-08 → 2026-07-17 · NQCONT 1-min · BandOrVWAP · 1 contract · Slippage 2 · Standard · PRAXIS commission · trading hours `CME US Index Futures RTH`.
111:1,211 trades (584 L / 627 S) · net $3,136.84 · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 · avg trade $2.59 · longs +$4,541.40 / shorts −$1,404.56 · largest winner $1,792.50 · total slippage 48.44.
```

```
$ sed -n '368,371p' DECISIONS.md | cut -c1-400
## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)

**Date:** 2026-11-02
**Status:** RULED by Amear — R-VN3-1. Ledger authorisation (S5): DECISION_LOG row `2026-11-02T21:23:45Z` (WHO: amear). Appended 2026-11-02 by praxis-manager, unit `2026-11-02-r-vn3-1-filing`.
```

```
$ grep -n -E 'Flat1559|OppBand|BandOrVWAP' DECISIONS.md | cut -c1-300 | head -30   (selected lines)
308:## 2026-10-31 — D-2026-10-31-A: 7zq scope extension — two Noise-Area backtest variants (OppBand, Flat1559) + one new researched NQ intraday strategy; vol-target variant deliberately NOT built
389:- Filer's reading, not a ruling: notes-3 line 10 names only "the last half hour", so the two Noise-Area variants (OppBand, Flat1559) and the baseline are outside this entry.
485:## 2026-11-02 — D-2026-11-02-C: R-VN3-3 to R-VN3-6 — data used as is; Flat1559 exit accepted; backtest with breakers on once built (O4, agent's reading confirmed in voice only); judge the version closest to live (O1)
504:- Voice agent's record (notes-3 line 23): the fill at the 15:59:00 price, printed as 4:00 PM in the grid, is accepted. Flat1559 is unchanged.
611:| R3–R4: OppBand, Flat1559 at High | 101 | **No question.** |
1222:   Q4 yes, OppBand = the paper's opposite band, as in _OppBand.cs.
1223:   Q5 yes, Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar, as in _Flat1559.cs.
```

```
$ sed -n '1077p' DECISIONS.md | cut -c1-700   (shortened here at "...")
- **Ruling 4 — walk-forward arm (b) and spec NEEDS AMEAR.** *Rules:* the defaults, verbatim: ""We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; ...
```

```
$ grep -n -E 'R-VM-6' DECISIONS.md | cut -c1-300 | head -5
(no output)
$ grep -n 'R-VM-6' DECISION_LOG.md | cut -c1-400 | head -4   (line 647, shortened here at "...")
647:- [2026-10-31T15:03:07Z] **WHO: amear** | PROPOSED BY: praxis-master (the open item R-VM-6 from the 14:59:37Z row) | ... | WHAT: **R-VM-6 RULED: "Stands — retire the stock-row runs."** ... Runs 3, 4 and Stock-row 0-S are retired as baselines (and as evidence about fills), not voided; ...
```

```
$ bd show Praxis_build-q36 2>&1 | head -20   (selected lines)
○ Praxis_build-q36 · 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference   [● P2 · OPEN]
  WHY: Amear ruling 2026-10-31T18:2xZ: the Future-row baseline is judged on
  its own; run 4 (Stock-typed NQCONT, 1 USD/pt, 0.01 tick) is retired (R-VM-
  6). The trade-count difference is logged here, not blocking Phase 4.
$ bd show Praxis_build-afe 2>&1 | head -4   (first line)
✓ Praxis_build-afe · R-VN3-1: PraxisLastHalfHourMomentum retired from the active candidate set (retire, not delete)   [● P2 · CLOSED]
```

De-identification check, run on this report before this block was inserted. The block adds no matching word.

```
$ grep -c -i -w "$(ls /Volumes/Sensidine/Praxis.build/docs/reports | grep '^2026-10-28-f4-' | head -1 | sed 's/^2026-10-28-f4-//; s/-.*//')" /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-strategy-review-index-worker4.md
0
```

## Gaps

1. **No DEC status for the baseline, OppBand or Flat1559.** No DECISIONS.md line retires, adopts or ranks any of the three. The grep above returns only design, definition and exit-policy lines, and DEC :389 explicitly puts the three outside D-2026-11-02-A. Beyond "not retired", the exit-policy rulings and the OPEN bead q36, their status is NOT IN RECORD.
2. **Baseline screenshot.** N2 :110 says the C4 values are "from Amear's screenshot". TSR :37 says "No baseline screenshot exists" among the Desktop inputs. The two may refer to different images (UNVERIFIED). The baseline settings rest only on N2 :111, REPORTED BY AMEAR.
3. **R-VM-6 is in DLOG only.** The retirement of runs 3 and 4 has no DECISIONS.md ID; the grep returned nothing.
4. **Run 4 win rate.** NOT IN RECORD on R3R :111. I did not search other files for it.
5. **Out of scope, flagged only.**
   - `docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md:51` names a later "T1 reference: hand run 1,173 trades, net $176,392.92, PF 1.26, max DD $38,905.64". It is not one of the four 11-01 runs, so it is not indexed here.
   - The same file at :18-:22 restates the LastHalfHourMomentum figures and its retirement under D-2026-11-02-A. That matches TSR :405 and DEC :368.
6. **Code identity not checked.** TSR's observation 10 says the .cs copies installed on the VM were not hash-checked. Whether the VM ran the repo code is UNVERIFIED there, and I did not check it either.
7. **TSR audit state.** TSR :6 reads "NOT audited at the time of writing", but CSVA :20 says TSR was "audited at 8ca9861". I did not open that audit (UNVERIFIED).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
