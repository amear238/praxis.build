# CSV analyses of the four 2026-11-01 backtest runs

**Stated limitation (F3):** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

This report does not change the status of F3 or of any frozen item.

- **Date:** 2026-11-01
- **Unit:** `2026-11-01-csv-analyses`
- **Authorisation:** the two `DECISION_LOG.md` rows stamped 2026-11-01T21:20:40Z: Amear's words "ok run them", read by the master as §6.A of `docs/reports/2026-11-01-voice-handoff-results-and-next-build.md`, and the master's dispatch of this unit to praxis-manager.
- **Author:** praxis-manager unit (workers W1 scripts, W3 writer, W3b and W5 exact-text corrections; single-line edits by the manager to the appendix note, twice, and to this line)
- **Grade:** ungraded at time of writing

## Grading key

- **OBSERVED** = read off pasted output in Appendix A of this report.
- **INFERRED** = reasoning from observed facts, stated with its basis.
- **UNVERIFIED** = not checked.

Cite forms: `[Kxx]` is the Appendix A block of that id. `[prior report Lnn]` is line nn of `docs/reports/2026-11-01-three-strategy-results.md` (audited at 8ca9861); every fact cited that way is OBSERVED in the prior report, not re-checked in this unit.

Run ids: **R0** = PraxisNoiseAreaBreakout (baseline), **R1** = PraxisNoiseAreaBreakout_OppBand, **R2** = PraxisNoiseAreaBreakout_Flat1559, **R3** = PraxisLastHalfHourMomentum. Runs are always listed in the order R0, R1, R2, R3, which is input-file order. That order is not a ranking (ruling R-1101-5).

## Inputs and reproduction

| Run | Strategy | Input file (in `$HOME/Desktop/`) | sha256 prefix | Trades | Trade date span |
|---|---|---|---|---|---|
| R0 | PraxisNoiseAreaBreakout | `NinjaTrader Grid 2026-11-01 07-10 AM.csv` | `421c44e6cd9d` | 1190 | 2021-03-29 .. 2026-07-15 |
| R1 | PraxisNoiseAreaBreakout_OppBand | `NinjaTrader Grid 2026-11-01 07-57 AM.csv` | `4207ea99e7f1` | 810 | 2021-03-29 .. 2026-07-15 |
| R2 | PraxisNoiseAreaBreakout_Flat1559 | `NinjaTrader Grid 2026-11-01 07-59 AM.csv` | `5a3c4d783a44` | 1190 | 2021-03-29 .. 2026-07-15 |
| R3 | PraxisLastHalfHourMomentum | `NinjaTrader Grid 2026-11-01 08-00 AM.csv` | `4efd8ce8e95c` | 1304 | 2021-03-09 .. 2026-07-17 |

- OBSERVED [K01, K04]: the sha256 prefixes are the `# Rn=` header lines of K04; the full digests are in K01. Trades and date spans are the `trades=` and `span` fields of K04.
- OBSERVED [K02]: line counts are 1191, 811, 1191 and 1305; K04 prints `rows=1190`, `rows=810`, `rows=1190` and `rows=1304` with `header_fields=24`, consistent with one header line per file (INFERRED) [K02, K04].
- OBSERVED [K10]: each file's Strategy column holds one name, the one in the table: `strategy=PraxisNoiseAreaBreakout rows=1190`, `strategy=PraxisNoiseAreaBreakout_OppBand rows=810`, `strategy=PraxisNoiseAreaBreakout_Flat1559 rows=1190`, `strategy=PraxisLastHalfHourMomentum rows=1304`. The script's short labels are in K04.
- OBSERVED [K03]: the analysis script `analyze.py` (sha256 prefix `d3cd15e0c9f1`) and runner `run.sh` (prefix `cb922a822b5b`) sit in the session scratchpad, not in the repo.

**Gate 0, reference totals reproduced.** OBSERVED [K04]; the reference values are the net, PF and max DD of the comparison table in the prior report [prior report L402-L405], supplied in the dispatch brief:

| Run | net | PF | maxDD | reference (net/PF/maxDD) | result |
|---|---|---|---|---|---|
| R0 | 197327.60 | 1.29 | -45282.04 | 197327.60/1.29/-45282.04 | MATCH |
| R1 | 210182.40 | 1.26 | -50748.88 | 210182.40/1.26/-50748.88 | MATCH |
| R2 | 193017.60 | 1.28 | -40637.04 | 193017.60/1.28/-40637.04 | MATCH |
| R3 | -76009.84 | 0.84 | -99806.96 | -76009.84/0.84/-99806.96 | MATCH |

K04 ends `GATE0: PASS` (OBSERVED [K04]).

**Parser facts.** OBSERVED [K04], in each of the four files:

- Qty 1 on every trade: `qty={1: 1190}`, `qty={1: 810}`, `qty={1: 1190}`, `qty={1: 1304}`.
- Commission 2.96 on every trade: `commission/trade={'2.96': 1190}`, `{'2.96': 810}`, `{'2.96': 1190}`, `{'2.96': 1304}`.
- No trade with Profit==0: `Profit==0 trades=0` for all four.
- No trade whose entry and exit years differ: `entry year != exit year: 0 trades` for all four.
- File order equals exit-time order: `file order == Exit-time order: non-decreasing=True, stable-sort-identical=True` for all four, with `exit<entry rows=0`.
- Each row's Profit re-derives from prices, side, the $20 multiplier, Qty and fees with `0 rows` mismatching, and `Cum.net column vs running sum mismatches=0`.

## Limitations

- **F3:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- **Partial calendar years.** The trade spans are 2021-03-29 .. 2026-07-15 for R0, R1 and R2 and 2021-03-09 .. 2026-07-17 for R3 (OBSERVED [K04]). INFERRED from those spans: the 2021 and 2026 rows in §1 and §3 cover only part of a calendar year, so they are not full-year figures.
- **Data holes.** There are two 17-day data holes, 2021-09-09 -> 2021-09-27 and 2025-12-14 -> 2026-01-01 (OBSERVED in the prior report, not re-checked in this unit [prior report L55, L413]). INFERRED: the 2021, 2025 and 2026 figures contain no trades from inside those spans, and any calendar-day count in §4 that crosses a hole includes the hole's days.
- **Drawdown basis.** Drawdowns are on closed-trade cumulative net only, with the peak starting from 0 (OBSERVED [K08], block header). There is no intra-trade excursion. INFERRED: the equity low reached inside an open trade may sit below the closed-trade figures in §4.
- **Recorded trade lists only.** Every figure is computed from the four recorded trade lists. Nothing was re-run (INFERRED from the commands pasted in [K01]-[K11]: each is `shasum`, `wc`, `awk`, `grep` or the analysis script given the four CSV paths; none starts a backtest).
- **Scripts outside the repo.** The scripts live in the session scratchpad, not the repo, with their sha256 in K03 (OBSERVED [K03]). INFERRED: re-running Appendix A needs that scratchpad and the four Desktop CSVs.

## §1 P&L by year

Net per exit year, OBSERVED [K05]:

| Exit year | R0 | R1 | R2 | R3 |
|---|---|---|---|---|
| 2021 | 13557.84 | 1609.20 | 14427.84 | -1934.24 |
| 2022 | 81034.80 | 95046.60 | 75649.80 | 17388.88 |
| 2023 | 39829.00 | 22937.52 | 36164.00 | -10656.12 |
| 2024 | 48603.28 | 59367.12 | 48353.28 | -23974.08 |
| 2025 | 17454.52 | 19058.56 | 21954.52 | -38002.64 |
| 2026 | -3151.84 | 12163.40 | -3531.84 | -18831.64 |
| ALL | 197327.60 | 210182.40 | 193017.60 | -76009.84 |

Highest-net and lowest-net year within each run, OBSERVED [K05] (the script's own lines):

- R0: highest-net year 2022 (81034.80); lowest-net year 2026 (-3151.84)
- R1: highest-net year 2022 (95046.60); lowest-net year 2021 (1609.20)
- R2: highest-net year 2022 (75649.80); lowest-net year 2026 (-3531.84)
- R3: highest-net year 2022 (17388.88); lowest-net year 2025 (-38002.64)

INFERRED from the Limitations spans: the lowest-net year for R0, R1 and R2 is a partial year (2026 or 2021).

Trades, PF, win rate and average trade per year are in K05. The `p=0` column is 0 in every row (OBSERVED [K05]). The year × side breakdown is in section `K06a` of K06.

## §2 Top winners removed

Trades are sorted by Profit, ties are broken by lower trade#, and dates are exit dates (OBSERVED [K07], block header). Every cut in K07 prints `no tie at cut`, so the N-th and (N+1)-th trades differ at each cut (OBSERVED [K07]).

**R0** (full net=197327.60, PF=1.29). OBSERVED [K07]:

| Removal | sum removed | remaining net | remaining PF | share of full net |
|---|---|---|---|---|
| 5 largest winners | 85960.20 | 111367.40 | 1.16 | 43.6% |
| 10 largest winners | 122575.40 | 74752.20 | 1.11 | 62.1% |
| 5 largest losers | -23504.80 | 220832.40 | 1.34 | -11.9% |

**R1** (full net=210182.40, PF=1.26). OBSERVED [K07]:

| Removal | sum removed | remaining net | remaining PF | share of full net |
|---|---|---|---|---|
| 5 largest winners | 89810.20 | 120372.20 | 1.15 | 42.7% |
| 10 largest winners | 127260.40 | 82922.00 | 1.10 | 60.5% |
| 5 largest losers | -60219.80 | 270402.20 | 1.37 | -28.7% |

**R2** (full net=193017.60, PF=1.28). OBSERVED [K07]:

| Removal | sum removed | remaining net | remaining PF | share of full net |
|---|---|---|---|---|
| 5 largest winners | 84795.20 | 108222.40 | 1.16 | 43.9% |
| 10 largest winners | 120220.40 | 72797.20 | 1.11 | 62.3% |
| 5 largest losers | -23504.80 | 216522.40 | 1.33 | -12.2% |

**R3** (full net=-76009.84, PF=0.84). OBSERVED [K07]:

| Removal | sum removed | remaining net | remaining PF | share of full net |
|---|---|---|---|---|
| 5 largest winners | 17070.20 | -93080.04 | 0.81 | n/a (net <= 0) |
| 10 largest winners | 31160.40 | -107170.24 | 0.78 | n/a (net <= 0) |
| 5 largest losers | -25254.80 | -50755.04 | 0.89 | n/a (net <= 0) |

Why R3 prints "n/a (net <= 0)". OBSERVED [K07]: R3's full net is -76009.84, which is at or below zero, and the label itself reads `n/a (net <= 0)`. OBSERVED [K11]: the script's rule is `share = "n/a (net <= 0)" if full <= 0 else pct(s, full)`, so a share is printed only when full net is above zero.

The trades removed at each cut (trade#, exit date, side, Profit) are listed in K07. The largest single winner in each run, OBSERVED [K07]: R0 `#921 2025-04-09 L 35887.04`; R1 `#629 2025-04-09 L 36087.04`; R2 `#921 2025-04-09 L 36472.04`; R3 `#999 2025-04-04 S 3852.04`.

## §3 Long vs short by year

Net and PF per side per exit year. OBSERVED [K06], section `K06b`; section `K06a` of K06 prints the same cells per year and side.

**R0**:

| Exit year | Long net | Long PF | Short net | Short PF |
|---|---|---|---|---|
| 2021 | 8457.28 | 1.35 | 5100.56 | 1.18 |
| 2022 | 48430.64 | 1.92 | 32604.16 | 1.34 |
| 2023 | 40388.48 | 1.97 | -559.48 | 0.99 |
| 2024 | 28454.20 | 1.59 | 20149.08 | 1.28 |
| 2025 | 17339.92 | 1.28 | 114.60 | 1.00 |
| 2026 | -6756.28 | 0.86 | 3604.44 | 1.06 |
| ALL | 136314.24 | 1.49 | 61013.36 | 1.15 |

**R1**:

| Exit year | Long net | Long PF | Short net | Short PF |
|---|---|---|---|---|
| 2021 | 6008.52 | 1.17 | -4399.32 | 0.88 |
| 2022 | 41585.76 | 1.57 | 53460.84 | 1.53 |
| 2023 | 41767.28 | 1.84 | -18829.76 | 0.74 |
| 2024 | 19327.08 | 1.30 | 40040.04 | 1.62 |
| 2025 | 19821.68 | 1.25 | -763.12 | 0.99 |
| 2026 | 9943.84 | 1.22 | 2219.56 | 1.03 |
| ALL | 138454.16 | 1.40 | 71728.24 | 1.16 |

**R2**:

| Exit year | Long net | Long PF | Short net | Short PF |
|---|---|---|---|---|
| 2021 | 8667.28 | 1.35 | 5760.56 | 1.20 |
| 2022 | 45230.64 | 1.86 | 30419.16 | 1.32 |
| 2023 | 38948.48 | 1.93 | -2784.48 | 0.94 |
| 2024 | 28829.20 | 1.59 | 19524.08 | 1.28 |
| 2025 | 21589.92 | 1.35 | 364.60 | 1.00 |
| 2026 | -4756.28 | 0.90 | 1224.44 | 1.02 |
| ALL | 138509.24 | 1.50 | 54508.36 | 1.14 |

**R3**:

| Exit year | Long net | Long PF | Short net | Short PF |
|---|---|---|---|---|
| 2021 | -8474.28 | 0.71 | 6540.04 | 1.35 |
| 2022 | 3852.56 | 1.11 | 13536.32 | 1.26 |
| 2023 | -7756.64 | 0.79 | -2899.48 | 0.89 |
| 2024 | -14712.56 | 0.70 | -9261.52 | 0.80 |
| 2025 | -8455.92 | 0.83 | -29546.72 | 0.58 |
| 2026 | 10810.76 | 1.62 | -29642.40 | 0.44 |
| ALL | -24736.08 | 0.89 | -51273.76 | 0.81 |

Years with a negative side net, within each run, OBSERVED [K06], section `K06b`; 2021 and 2026 are partial years (INFERRED, see Limitations):

- R0: Long in 2026; Short in 2023.
- R1: Long in no year; Short in 2021, 2023 and 2025.
- R2: Long in 2026; Short in 2023.
- R3: Long in 2021, 2023, 2024 and 2025; Short in 2023, 2024, 2025 and 2026.

Trade counts and average trade per side are in sections `K06a` and `K06b` of K06. The side trade counts are also in K04 (`sides=`).

## §4 Drawdown profile

Basis, OBSERVED [K08] block header: closed-trade cumulative net, with the peak starting from 0. Dates are exit dates, and the starting peak is the entry date of trade 1. `d` is calendar days and `tr` is the trade-index difference. A trade whose cum equals the peak re-sets the peak.

**Maximum-drawdown episode per run.** OBSERVED [K08]. In every run the maximum-drawdown episode is `deep1`, and K08 prints `depth equals Gate 0 max DD`.

| Run | episodes | max-DD depth | peak | trough | peak->trough | recovery | to last trade | longest under water |
|---|---|---|---|---|---|---|---|---|
| R0 | 69 (unrecovered=1) | -45282.04 | 2025-04-10 #922 | 2026-06-03 #1171 | 419d/249tr | not recovered (open at last trade 2026-07-15) | 461d/268tr | 461d (UNRECOVERED, counted to last trade exit 2026-07-15) |
| R1 | 53 (unrecovered=1) | -50748.88 | 2025-04-10 #630 | 2026-03-11 #758 | 335d/128tr | not recovered (open at last trade 2026-07-15) | 461d/180tr | 461d (UNRECOVERED, counted to last trade exit 2026-07-15) |
| R2 | 72 (unrecovered=1) | -40637.04 | 2025-04-10 #922 | 2026-06-03 #1171 | 419d/249tr | not recovered (open at last trade 2026-07-15) | 461d/268tr | 461d (UNRECOVERED, counted to last trade exit 2026-07-15) |
| R3 | 16 (unrecovered=1) | -99806.96 | 2022-05-04 #278 | 2026-07-17 #1304 | 1535d/1026tr | not recovered (open at last trade 2026-07-17) | 1535d/1026tr | 1535d (UNRECOVERED, counted to last trade exit 2026-07-17) |

- OBSERVED [K08]: every run's deepest drawdown is unrecovered at its last trade. In every run the longest time under water is that same `deep1` episode, counted to the last trade's exit.
- INFERRED from the above: each run's "time under water" is a span to that run's last trade exit (2026-07-15 for R0, R1 and R2; 2026-07-17 for R3; OBSERVED [K08]), not a completed duration. The true duration is unknown.
- OBSERVED [K08]: R3's `deep1` trough is its last trade, `#1304` on 2026-07-17.
- INFERRED from the dates in K08 and the holes cited in Limitations: the `deep1` spans of R0, R1 and R2 (from 2025-04-10) cross the 2025-12-14 -> 2026-01-01 hole. R3's `deep1` span (from 2022-05-04) also crosses it. R1 `deep2` (2021-07-27 to 2022-02-24) and R3 `deep2` (2021-05-10 to 2022-01-31) cross the 2021-09-09 -> 2021-09-27 hole.

**Five deepest drawdowns per run.** OBSERVED [K08]; peak cum values are in K08.

R0:

| episode | depth | peak | trough | peak->trough | recovery (peak->recovery) |
|---|---|---|---|---|---|
| deep1 | -45282.04 | 2025-04-10 #922 | 2026-06-03 #1171 | 419d/249tr | not recovered |
| deep2 | -17831.36 | 2022-08-30 #303 | 2022-10-13 #344 | 44d/41tr | 2023-04-27 #468 (240d/165tr) |
| deep3 | -11964.20 | 2022-01-07 #150 | 2022-01-28 #170 | 21d/20tr | 2022-02-11 #181 (35d/31tr) |
| deep4 | -11624.80 | 2025-04-04 #915 | 2025-04-09 #920 | 5d/5tr | 2025-04-09 #921 (5d/6tr) |
| deep5 | -10309.72 | 2024-03-07 #665 | 2024-04-11 #697 | 35d/32tr | 2024-04-19 #703 (43d/38tr) |

R1:

| episode | depth | peak | trough | peak->trough | recovery (peak->recovery) |
|---|---|---|---|---|---|
| deep1 | -50748.88 | 2025-04-10 #630 | 2026-03-11 #758 | 335d/128tr | not recovered |
| deep2 | -30919.96 | 2021-07-27 #44 | 2022-01-27 #120 | 184d/76tr | 2022-02-24 #134 (212d/90tr) |
| deep3 | -24125.92 | 2025-04-04 #625 | 2025-04-08 #627 | 4d/2tr | 2025-04-09 #629 (5d/4tr) |
| deep4 | -13951.56 | 2023-02-13 #286 | 2023-04-24 #322 | 70d/36tr | 2023-05-26 #338 (102d/52tr) |
| deep5 | -13610.92 | 2024-08-02 #529 | 2024-08-07 #531 | 5d/2tr | 2024-08-22 #535 (20d/6tr) |

R2:

| episode | depth | peak | trough | peak->trough | recovery (peak->recovery) |
|---|---|---|---|---|---|
| deep1 | -40637.04 | 2025-04-10 #922 | 2026-06-03 #1171 | 419d/249tr | not recovered |
| deep2 | -17176.36 | 2022-08-30 #303 | 2022-10-13 #344 | 44d/41tr | 2023-04-27 #468 (240d/165tr) |
| deep3 | -13534.20 | 2022-01-07 #150 | 2022-01-28 #170 | 21d/20tr | 2022-02-11 #181 (35d/31tr) |
| deep4 | -11049.80 | 2025-04-04 #915 | 2025-04-09 #920 | 5d/5tr | 2025-04-09 #921 (5d/6tr) |
| deep5 | -9939.72 | 2024-03-07 #665 | 2024-04-11 #697 | 35d/32tr | 2024-04-19 #703 (43d/38tr) |

R3:

| episode | depth | peak | trough | peak->trough | recovery (peak->recovery) |
|---|---|---|---|---|---|
| deep1 | -99806.96 | 2022-05-04 #278 | 2026-07-17 #1304 | 1535d/1026tr | not recovered |
| deep2 | -12305.28 | 2021-05-10 #44 | 2021-10-07 #137 | 150d/93tr | 2022-01-31 #214 (266d/170tr) |
| deep3 | -5318.68 | 2022-02-25 #232 | 2022-03-09 #240 | 12d/8tr | 2022-04-22 #270 (56d/38tr) |
| deep4 | -2281.84 | 2021-03-09 (start) | 2021-03-12 #4 | 3d/4tr | 2021-03-24 #12 (15d/12tr) |
| deep5 | -1875.92 | 2022-04-26 #272 | 2022-04-28 #274 | 2d/2tr | 2022-05-02 #276 (6d/4tr) |

## §5 Slippage sensitivity (arithmetic model)

This is arithmetic on the recorded trade list, not a re-run. It ignores fills that were clipped to the bar range: the prior report found baseline and Flat1559 entry fills equal to the entry bar's open + 0.50 adverse, clamped to the bar low/high [prior report L51], and LastHalfHourMomentum fills equal to the bar high for a buy or the bar low for a sell [prior report L357] (OBSERVED in the prior report, not re-checked in this unit; no OppBand finding is cited). It also assumes the same trades occur at higher slippage (INFERRED; untested).

- **Formula** (OBSERVED [K09], block header): `adj = Profit - (k-2)*2*$5.00*Qty`, where k is ticks per side. The 2-ticks/side premise comes from the F3 limitation sentence; the prior report shows the open + 0.50 adverse pattern for baseline and Flat1559 entries (OBSERVED in the prior report, not re-checked in this unit [prior report L51]). For exits it is UNVERIFIED in this unit; the trade lists do not state it.
- **Qty** (OBSERVED [K09]): the Qty distribution is `{1: 1190}`, `{1: 810}`, `{1: 1190}` and `{1: 1304}` for R0..R3.
- **Tick value** (INFERRED from two observations): every entry and exit price is on the 0.25 grid (`off 0.25 grid=0` in all four files, while the 0.50-grid control fires, e.g. `off 0.50 grid (control)=1240`; OBSERVED [K10]), and every Profit re-derives with the $20 multiplier (OBSERVED [K04]). 0.25 × $20 is the `$5.00` per tick in the formula.
- **k = 2 check** (OBSERVED [K09]): for all four runs, the k=2 line prints `recorded net ...: equal`, so the model at k=2 reproduces the recorded net. INFERRED: at k=2 the formula deducts 0 by construction, so this checks the summing only, not the 2-tick premise.

OBSERVED [K09]:

| Run | k (ticks/side) | net | PF | total deduction |
|---|---|---|---|---|
| R0 | 2 (recorded; equal) | 197327.60 | 1.29 | 0.00 |
| R0 | 3 (arithmetic model) | 185427.60 | 1.27 | 11900.00 |
| R0 | 4 (arithmetic model) | 173527.60 | 1.25 | 23800.00 |
| R1 | 2 (recorded; equal) | 210182.40 | 1.26 | 0.00 |
| R1 | 3 (arithmetic model) | 202082.40 | 1.25 | 8100.00 |
| R1 | 4 (arithmetic model) | 193982.40 | 1.24 | 16200.00 |
| R2 | 2 (recorded; equal) | 193017.60 | 1.28 | 0.00 |
| R2 | 3 (arithmetic model) | 181117.60 | 1.26 | 11900.00 |
| R2 | 4 (arithmetic model) | 169217.60 | 1.24 | 23800.00 |
| R3 | 2 (recorded; equal) | -76009.84 | 0.84 | 0.00 |
| R3 | 3 (arithmetic model) | -89049.84 | 0.82 | 13040.00 |
| R3 | 4 (arithmetic model) | -102089.84 | 0.80 | 26080.00 |

INFERRED from the formula: with Qty 1 on every trade, the arithmetic model takes the same fixed amount off every trade at a given k. The trade count and the order of trades are unchanged, and any trade whose entry or exit would differ at higher slippage is not modelled.

## §6 What this report does not do

- It gives no ranking, no comparison verdict and no recommendation, and it applies no superlative label to any run (ruling R-1101-5). Runs appear in R0..R3 file order only.
- Nothing about the trading-hours template or the session-flat rule (F2, frozen) was changed, proposed or decided.
- No backtest was re-run. Every figure is read from the four recorded trade lists (see Limitations).
- No code or config was changed. Outside the session scratchpad, this unit writes this report, its manager report `docs/reports/2026-11-01-csv-analyses-manager.md` and three appended MANIFEST.md rows (UNVERIFIED in this report; the manager report pastes `git status`).
- It does not grade F3 and makes no claim that F3 is unfrozen or satisfied.

## §7 Open questions for Amear

These questions are left open. This report does not answer any of them.

1. Does Amear want 1-tick/side slippage shown as well? The Block 2 spec under F3 in `specs/SPEC_RUBRIC.md` names 1-tick slippage, and the four runs assume 2 ticks/side (the F3 limitation sentence).
2. Does he want the partial years 2021 and 2026 shown as-is, as in §1 and §3, or handled another way?
3. Does the clipped-fill gap in the §5 arithmetic model matter to him, relative to the deferred 0-H control (Standard vs High fill resolution)?
4. Does he want drawdown measured on another basis, such as intra-trade excursion or a prop-firm trailing-drawdown rule, instead of or alongside the closed-trade basis in §4?
5. Several of the largest winners and losers in K07 fall on nearby exit dates between 2025-04-01 and 2025-04-11. Examples: R0 `#915 2025-04-04`, `#919 2025-04-09` and `#921 2025-04-09`; R1 `#625 2025-04-04`, `#627 2025-04-08`, `#629 2025-04-09` and `#631 2025-04-11`; R3 `#996 2025-04-01` and `#999 2025-04-04` (OBSERVED [K07]). Does he want a by-day or by-week view of the large trades?
6. Does he want the trades and drawdown spans next to the two data holes (prior report L413) flagged or set apart in a later view?

## Appendix A — Verification evidence (pasted command output)

Each command was passed as one argument to `zsh -c` with cwd `/` (the runner executes `( cd / && zsh -c "$cmd" )`). To re-run one by hand, paste it into a zsh shell whose cwd is `/`; do not wrap it in single quotes, because K10 contains single quotes. The first line of each block (`$ <command>`) is the command as run. The last line, `[exit N]`, is appended by the runner and is not command output. The `# Rn=` header lines (K04 to K09) are printed by the analysis script. Each block below is the evidence file, unedited.

### K01 — sha256 of the four input CSVs

```text
$ shasum -a 256 "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
[exit 0]
```

### K02 — line counts of the four input CSVs (header + trades)

```text
$ wc -l "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
    1191 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv
     811 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv
    1191 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv
    1305 /Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv
    4498 total
[exit 0]
```

### K03 — sha256 of the analysis script and runner

```text
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/run.sh
d3cd15e0c9f103906867f9b0125b07fcb4001950f6cb8bcbdc2ec6a036c26ab6  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py
cb922a822b5b00f68e65d78f48c5e293cf3c0c775e4d8151e30753bdfa247afe  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/run.sh
[exit 0]
```

### K04 — Gate 0 totals vs reference + parser checks

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py gate0 "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K04 Gate 0 + parser checks ==
R0 baseline NAB: trades=1190 net=197327.60 PF=1.29 maxDD=-45282.04 | ref 197327.60/1.29/-45282.04 -> MATCH
  rows=1190 header_fields=24 (last='') width_mismatch=0 trade#_seq_1..n=True
  line_endings: CRLF=1191 LF=1191 CR=1191 (all-CRLF=True)
  money parsed strictly ^-?\$d+.dd$ (no thousands sep/parens): all rows OK; Cum.net column vs running sum mismatches=0; sum(Profit)==last Cum=True
  sides={'Short': 634, 'Long': 556} qty={1: 1190} instruments=['NQCONTROW SEP25'] commission/trade={'2.96': 1190}
  Profit==0 trades=0; (exit-entry)*side*$20*qty-comm-fees != Profit: 0 rows
  file order == Exit-time order: non-decreasing=True, stable-sort-identical=True, equal-exit-time adjacent ties=0; exit<entry rows=0
  entry year != exit year: 0 trades; span 2021-03-29 .. 2026-07-15
R1 NAB_OppBand: trades=810 net=210182.40 PF=1.26 maxDD=-50748.88 | ref 210182.40/1.26/-50748.88 -> MATCH
  rows=810 header_fields=24 (last='') width_mismatch=0 trade#_seq_1..n=True
  line_endings: CRLF=811 LF=811 CR=811 (all-CRLF=True)
  money parsed strictly ^-?\$d+.dd$ (no thousands sep/parens): all rows OK; Cum.net column vs running sum mismatches=0; sum(Profit)==last Cum=True
  sides={'Short': 406, 'Long': 404} qty={1: 810} instruments=['NQCONTROW SEP25'] commission/trade={'2.96': 810}
  Profit==0 trades=0; (exit-entry)*side*$20*qty-comm-fees != Profit: 0 rows
  file order == Exit-time order: non-decreasing=True, stable-sort-identical=True, equal-exit-time adjacent ties=0; exit<entry rows=0
  entry year != exit year: 0 trades; span 2021-03-29 .. 2026-07-15
R2 NAB_Flat1559: trades=1190 net=193017.60 PF=1.28 maxDD=-40637.04 | ref 193017.60/1.28/-40637.04 -> MATCH
  rows=1190 header_fields=24 (last='') width_mismatch=0 trade#_seq_1..n=True
  line_endings: CRLF=1191 LF=1191 CR=1191 (all-CRLF=True)
  money parsed strictly ^-?\$d+.dd$ (no thousands sep/parens): all rows OK; Cum.net column vs running sum mismatches=0; sum(Profit)==last Cum=True
  sides={'Short': 634, 'Long': 556} qty={1: 1190} instruments=['NQCONTROW SEP25'] commission/trade={'2.96': 1190}
  Profit==0 trades=0; (exit-entry)*side*$20*qty-comm-fees != Profit: 0 rows
  file order == Exit-time order: non-decreasing=True, stable-sort-identical=True, equal-exit-time adjacent ties=0; exit<entry rows=0
  entry year != exit year: 0 trades; span 2021-03-29 .. 2026-07-15
R3 LastHalfHourMomentum: trades=1304 net=-76009.84 PF=0.84 maxDD=-99806.96 | ref -76009.84/0.84/-99806.96 -> MATCH
  rows=1304 header_fields=24 (last='') width_mismatch=0 trade#_seq_1..n=True
  line_endings: CRLF=1305 LF=1305 CR=1305 (all-CRLF=True)
  money parsed strictly ^-?\$d+.dd$ (no thousands sep/parens): all rows OK; Cum.net column vs running sum mismatches=0; sum(Profit)==last Cum=True
  sides={'Long': 698, 'Short': 606} qty={1: 1304} instruments=['NQCONTROW SEP25'] commission/trade={'2.96': 1304}
  Profit==0 trades=0; (exit-entry)*side*$20*qty-comm-fees != Profit: 0 rows
  file order == Exit-time order: non-decreasing=True, stable-sort-identical=True, equal-exit-time adjacent ties=0; exit<entry rows=0
  entry year != exit year: 0 trades; span 2021-03-09 .. 2026-07-17
GATE0: PASS
[exit 0]
```

### K05 — by exit year: trades, net, PF, win rate, Profit==0, avg

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py year "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K05 By exit year (win% = Profit>0 / trades; p=0 = count Profit==0) ==
-- R0 baseline NAB (entry-year != exit-year trades: 0)
year       n          net    PF   win%  p=0        avg
2021     146     13557.84  1.25  43.8%    0      92.86
2022     245     81034.80  1.54  42.9%    0     330.75
2023     225     39829.00  1.46  43.6%    0     177.02
2024     232     48603.28  1.40  40.1%    0     209.50
2025     213     17454.52  1.11  39.4%    0      81.95
2026     129     -3151.84  0.97  31.0%    0     -24.43
ALL     1190    197327.60  1.29  40.7%    0     165.82
highest-net year 2022 (81034.80); lowest-net year 2026 (-3151.84)
-- R1 NAB_OppBand (entry-year != exit-year trades: 0)
year       n          net    PF   win%  p=0        avg
2021     105      1609.20  1.02  56.2%    0      15.33
2022     165     95046.60  1.55  66.1%    0     576.04
2023     163     22937.52  1.19  56.4%    0     140.72
2024     153     59367.12  1.46  60.1%    0     388.02
2025     139     19058.56  1.10  56.1%    0     137.11
2026      85     12163.40  1.11  47.1%    0     143.10
ALL      810    210182.40  1.26  58.0%    0     259.48
highest-net year 2022 (95046.60); lowest-net year 2021 (1609.20)
-- R2 NAB_Flat1559 (entry-year != exit-year trades: 0)
year       n          net    PF   win%  p=0        avg
2021     146     14427.84  1.27  44.5%    0      98.82
2022     245     75649.80  1.51  42.9%    0     308.77
2023     225     36164.00  1.41  42.2%    0     160.73
2024     232     48353.28  1.41  40.1%    0     208.42
2025     213     21954.52  1.13  39.4%    0     103.07
2026     129     -3531.84  0.97  31.0%    0     -27.38
ALL     1190    193017.60  1.28  40.5%    0     162.20
highest-net year 2022 (75649.80); lowest-net year 2026 (-3531.84)
-- R3 LastHalfHourMomentum (entry-year != exit-year trades: 0)
year       n          net    PF   win%  p=0        avg
2021     194     -1934.24  0.96  44.8%    0      -9.97
2022     247     17388.88  1.20  55.5%    0      70.40
2023     247    -10656.12  0.83  44.1%    0     -43.14
2024     248    -23974.08  0.75  48.0%    0     -96.67
2025     234    -38002.64  0.69  44.0%    0    -162.40
2026     134    -18831.64  0.73  49.3%    0    -140.53
ALL     1304    -76009.84  0.84  47.6%    0     -58.29
highest-net year 2022 (17388.88); lowest-net year 2025 (-38002.64)
[exit 0]
```

### K06 — by exit year x side; long vs short by year

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py yearside "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K06a By exit year x side (win% = Profit>0 / trades; p=0 = count Profit==0) ==
-- R0 baseline NAB (entry-year != exit-year trades: 0)
year   side      n          net    PF   win%  p=0        avg
2021   Long     82      8457.28  1.35  48.8%    0     103.14
2022   Long     91     48430.64  1.92  45.1%    0     532.20
2023   Long    112     40388.48  1.97  53.6%    0     360.61
2024   Long    105     28454.20  1.59  42.9%    0     270.99
2025   Long     98     17339.92  1.28  41.8%    0     176.94
2026   Long     68     -6756.28  0.86  33.8%    0     -99.36
ALL    Long    556    136314.24  1.49  45.0%    0     245.17
2021   Short    64      5100.56  1.18  37.5%    0      79.70
2022   Short   154     32604.16  1.34  41.6%    0     211.72
2023   Short   113      -559.48  0.99  33.6%    0      -4.95
2024   Short   127     20149.08  1.28  37.8%    0     158.65
2025   Short   115       114.60  1.00  37.4%    0       1.00
2026   Short    61      3604.44  1.06  27.9%    0      59.09
ALL    Short   634     61013.36  1.15  36.9%    0      96.24
-- R1 NAB_OppBand (entry-year != exit-year trades: 0)
year   side      n          net    PF   win%  p=0        avg
2021   Long     63      6008.52  1.17  65.1%    0      95.37
2022   Long     69     41585.76  1.57  68.1%    0     602.69
2023   Long     82     41767.28  1.84  67.1%    0     509.36
2024   Long     77     19327.08  1.30  62.3%    0     251.00
2025   Long     67     19821.68  1.25  64.2%    0     295.85
2026   Long     46      9943.84  1.22  47.8%    0     216.17
ALL    Long    404    138454.16  1.40  63.4%    0     342.71
2021   Short    42     -4399.32  0.88  42.9%    0    -104.75
2022   Short    96     53460.84  1.53  64.6%    0     556.88
2023   Short    81    -18829.76  0.74  45.7%    0    -232.47
2024   Short    76     40040.04  1.62  57.9%    0     526.84
2025   Short    72      -763.12  0.99  48.6%    0     -10.60
2026   Short    39      2219.56  1.03  46.2%    0      56.91
ALL    Short   406     71728.24  1.16  52.7%    0     176.67
-- R2 NAB_Flat1559 (entry-year != exit-year trades: 0)
year   side      n          net    PF   win%  p=0        avg
2021   Long     82      8667.28  1.35  48.8%    0     105.70
2022   Long     91     45230.64  1.86  45.1%    0     497.04
2023   Long    112     38948.48  1.93  52.7%    0     347.75
2024   Long    105     28829.20  1.59  42.9%    0     274.56
2025   Long     98     21589.92  1.35  41.8%    0     220.31
2026   Long     68     -4756.28  0.90  33.8%    0     -69.95
ALL    Long    556    138509.24  1.50  44.8%    0     249.12
2021   Short    64      5760.56  1.20  39.1%    0      90.01
2022   Short   154     30419.16  1.32  41.6%    0     197.53
2023   Short   113     -2784.48  0.94  31.9%    0     -24.64
2024   Short   127     19524.08  1.28  37.8%    0     153.73
2025   Short   115       364.60  1.00  37.4%    0       3.17
2026   Short    61      1224.44  1.02  27.9%    0      20.07
ALL    Short   634     54508.36  1.14  36.8%    0      85.98
-- R3 LastHalfHourMomentum (entry-year != exit-year trades: 0)
year   side      n          net    PF   win%  p=0        avg
2021   Long    118     -8474.28  0.71  41.5%    0     -71.82
2022   Long    114      3852.56  1.11  51.8%    0      33.79
2023   Long    134     -7756.64  0.79  44.8%    0     -57.89
2024   Long    136    -14712.56  0.70  49.3%    0    -108.18
2025   Long    127     -8455.92  0.83  46.5%    0     -66.58
2026   Long     69     10810.76  1.62  62.3%    0     156.68
ALL    Long    698    -24736.08  0.89  48.3%    0     -35.44
2021   Short    76      6540.04  1.35  50.0%    0      86.05
2022   Short   133     13536.32  1.26  58.6%    0     101.78
2023   Short   113     -2899.48  0.89  43.4%    0     -25.66
2024   Short   112     -9261.52  0.80  46.4%    0     -82.69
2025   Short   107    -29546.72  0.58  41.1%    0    -276.14
2026   Short    65    -29642.40  0.44  35.4%    0    -456.04
ALL    Short   606    -51273.76  0.81  46.9%    0     -84.61
== K06b Long vs short by exit year (trades, net, PF, avg trade) ==
-- R0 baseline NAB
year  |   nL        netL  PF_L      avgL |   nS        netS  PF_S      avgS
2021  |   82     8457.28  1.35    103.14 |   64     5100.56  1.18     79.70
2022  |   91    48430.64  1.92    532.20 |  154    32604.16  1.34    211.72
2023  |  112    40388.48  1.97    360.61 |  113     -559.48  0.99     -4.95
2024  |  105    28454.20  1.59    270.99 |  127    20149.08  1.28    158.65
2025  |   98    17339.92  1.28    176.94 |  115      114.60  1.00      1.00
2026  |   68    -6756.28  0.86    -99.36 |   61     3604.44  1.06     59.09
ALL   |  556   136314.24  1.49    245.17 |  634    61013.36  1.15     96.24
-- R1 NAB_OppBand
year  |   nL        netL  PF_L      avgL |   nS        netS  PF_S      avgS
2021  |   63     6008.52  1.17     95.37 |   42    -4399.32  0.88   -104.75
2022  |   69    41585.76  1.57    602.69 |   96    53460.84  1.53    556.88
2023  |   82    41767.28  1.84    509.36 |   81   -18829.76  0.74   -232.47
2024  |   77    19327.08  1.30    251.00 |   76    40040.04  1.62    526.84
2025  |   67    19821.68  1.25    295.85 |   72     -763.12  0.99    -10.60
2026  |   46     9943.84  1.22    216.17 |   39     2219.56  1.03     56.91
ALL   |  404   138454.16  1.40    342.71 |  406    71728.24  1.16    176.67
-- R2 NAB_Flat1559
year  |   nL        netL  PF_L      avgL |   nS        netS  PF_S      avgS
2021  |   82     8667.28  1.35    105.70 |   64     5760.56  1.20     90.01
2022  |   91    45230.64  1.86    497.04 |  154    30419.16  1.32    197.53
2023  |  112    38948.48  1.93    347.75 |  113    -2784.48  0.94    -24.64
2024  |  105    28829.20  1.59    274.56 |  127    19524.08  1.28    153.73
2025  |   98    21589.92  1.35    220.31 |  115      364.60  1.00      3.17
2026  |   68    -4756.28  0.90    -69.95 |   61     1224.44  1.02     20.07
ALL   |  556   138509.24  1.50    249.12 |  634    54508.36  1.14     85.98
-- R3 LastHalfHourMomentum
year  |   nL        netL  PF_L      avgL |   nS        netS  PF_S      avgS
2021  |  118    -8474.28  0.71    -71.82 |   76     6540.04  1.35     86.05
2022  |  114     3852.56  1.11     33.79 |  133    13536.32  1.26    101.78
2023  |  134    -7756.64  0.79    -57.89 |  113    -2899.48  0.89    -25.66
2024  |  136   -14712.56  0.70   -108.18 |  112    -9261.52  0.80    -82.69
2025  |  127    -8455.92  0.83    -66.58 |  107   -29546.72  0.58   -276.14
2026  |   69    10810.76  1.62    156.68 |   65   -29642.40  0.44   -456.04
ALL   |  698   -24736.08  0.89    -35.44 |  606   -51273.76  0.81    -84.61
[exit 0]
```

### K07 — top-5/top-10 winners and top-5 losers removed

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py topn "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K07 Top-N removed (sort by Profit; ties broken by lower trade#; side L/S; date=exit date) ==
-- R0 baseline NAB full net=197327.60 PF=1.29
  remove 5 largest winners: N-th=7602.04 (N+1)-th=7507.04 -> no tie at cut
    removed: #921 2025-04-09 L 35887.04; #1026 2025-10-10 S 15802.04; #1172 2026-06-05 S 15142.04; #841 2024-12-18 S 11527.04; #915 2025-04-04 S 7602.04
    sum removed=85960.20 remaining net=111367.40 remaining PF=1.16 share of full net=43.6%
  remove 10 largest winners: N-th=7067.04 (N+1)-th=6447.04 -> no tie at cut
    removed: #921 2025-04-09 L 35887.04; #1026 2025-10-10 S 15802.04; #1172 2026-06-05 S 15142.04; #841 2024-12-18 S 11527.04; #915 2025-04-04 S 7602.04; #1177 2026-06-11 L 7507.04; #1180 2026-06-16 S 7427.04; #302 2022-08-26 S 7347.04; #1132 2026-03-31 L 7267.04; #780 2024-09-03 S 7067.04
    sum removed=122575.40 remaining net=74752.20 remaining PF=1.11 share of full net=62.1%
  remove 5 largest losers: N-th=-4007.96 (N+1)-th=-3902.96 -> no tie at cut
    removed: #1182 2026-06-25 S -5407.96; #342 2022-10-13 S -5337.96; #919 2025-04-09 L -4457.96; #234 2022-04-27 L -4292.96; #1001 2025-09-05 L -4007.96
    sum removed=-23504.80 remaining net=220832.40 remaining PF=1.34 share of full net=-11.9%
-- R1 NAB_OppBand full net=210182.40 PF=1.26
  remove 5 largest winners: N-th=11252.04 (N+1)-th=7912.04 -> no tie at cut
    removed: #629 2025-04-09 L 36087.04; #699 2025-10-10 S 15802.04; #797 2026-06-05 S 15142.04; #581 2024-12-18 S 11527.04; #800 2026-06-11 L 11252.04
    sum removed=89810.20 remaining net=120372.20 remaining PF=1.15 share of full net=42.7%
  remove 10 largest winners: N-th=7162.04 (N+1)-th=7067.04 -> no tie at cut
    removed: #629 2025-04-09 L 36087.04; #699 2025-10-10 S 15802.04; #797 2026-06-05 S 15142.04; #581 2024-12-18 S 11527.04; #800 2026-06-11 L 11252.04; #607 2025-02-27 S 7912.04; #625 2025-04-04 S 7602.04; #802 2026-06-16 S 7427.04; #215 2022-08-26 S 7347.04; #175 2022-05-18 S 7162.04
    sum removed=127260.40 remaining net=82922.00 remaining PF=1.10 share of full net=60.5%
  remove 5 largest losers: N-th=-9062.96 (N+1)-th=-8832.96 -> no tie at cut
    removed: #627 2025-04-08 L -19592.96; #531 2024-08-07 L -10982.96; #638 2025-04-30 S -10477.96; #631 2025-04-11 S -10102.96; #237 2022-10-13 S -9062.96
    sum removed=-60219.80 remaining net=270402.20 remaining PF=1.37 share of full net=-28.7%
-- R2 NAB_Flat1559 full net=193017.60 PF=1.28
  remove 5 largest winners: N-th=7927.04 (N+1)-th=7282.04 -> no tie at cut
    removed: #921 2025-04-09 L 36472.04; #1026 2025-10-10 S 15742.04; #1172 2026-06-05 S 14367.04; #841 2024-12-18 S 10287.04; #1177 2026-06-11 L 7927.04
    sum removed=84795.20 remaining net=108222.40 remaining PF=1.16 share of full net=43.9%
  remove 10 largest winners: N-th=6682.04 (N+1)-th=6622.04 -> no tie at cut
    removed: #921 2025-04-09 L 36472.04; #1026 2025-10-10 S 15742.04; #1172 2026-06-05 S 14367.04; #841 2024-12-18 S 10287.04; #1177 2026-06-11 L 7927.04; #780 2024-09-03 S 7282.04; #915 2025-04-04 S 7267.04; #302 2022-08-26 S 7132.04; #1132 2026-03-31 L 7062.04; #1180 2026-06-16 S 6682.04
    sum removed=120220.40 remaining net=72797.20 remaining PF=1.11 share of full net=62.3%
  remove 5 largest losers: N-th=-4007.96 (N+1)-th=-3902.96 -> no tie at cut
    removed: #1182 2026-06-25 S -5407.96; #342 2022-10-13 S -5337.96; #919 2025-04-09 L -4457.96; #234 2022-04-27 L -4292.96; #1001 2025-09-05 L -4007.96
    sum removed=-23504.80 remaining net=216522.40 remaining PF=1.33 share of full net=-12.2%
-- R3 LastHalfHourMomentum full net=-76009.84 PF=0.84
  remove 5 largest winners: N-th=3227.04 (N+1)-th=3037.04 -> no tie at cut
    removed: #999 2025-04-04 S 3852.04; #975 2025-02-28 L 3407.04; #213 2022-01-28 L 3307.04; #1156 2025-11-20 S 3277.04; #929 2024-12-18 S 3227.04
    sum removed=17070.20 remaining net=-93080.04 remaining PF=0.81 share of full net=n/a (net <= 0)
  remove 10 largest winners: N-th=2707.04 (N+1)-th=2642.04 -> no tie at cut
    removed: #999 2025-04-04 S 3852.04; #975 2025-02-28 L 3407.04; #213 2022-01-28 L 3307.04; #1156 2025-11-20 S 3277.04; #929 2024-12-18 S 3227.04; #169 2021-11-22 S 3037.04; #207 2022-01-20 S 2847.04; #1284 2026-06-17 S 2772.04; #996 2025-04-01 L 2727.04; #231 2022-02-24 L 2707.04
    sum removed=31160.40 remaining net=-107170.24 remaining PF=0.78 share of full net=n/a (net <= 0)
  remove 5 largest losers: N-th=-4317.96 (N+1)-th=-4182.96 -> no tie at cut
    removed: #977 2025-03-04 L -5537.96; #772 2024-05-01 L -5327.96; #1007 2025-04-16 S -5242.96; #209 2022-01-24 S -4827.96; #496 2023-03-22 L -4317.96
    sum removed=-25254.80 remaining net=-50755.04 remaining PF=0.89 share of full net=n/a (net <= 0)
[exit 0]
```

### K08 — drawdown profile: max-DD episode, five deepest, longest underwater

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py dd "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K08 Drawdown profile (closed-trade cum net, peak from 0; dates = exit dates, start peak = entry date of trade 1;
   d = calendar days, tr = trade-index difference; a trade with cum == peak re-sets the peak) ==
-- R0 baseline NAB (episodes=69, unrecovered=1)
  MAX-DD episode = deep1 (depth equals Gate 0 max DD)
  deep1: depth=-45282.04 peak=2025-04-10 #922 cum=218745.88 trough=2026-06-03 #1171 | peak->trough 419d/249tr | recovery: not recovered (open at last trade 2026-07-15); to last trade 461d/268tr
  deep2: depth=-17831.36 peak=2022-08-30 #303 cum=104603.12 trough=2022-10-13 #344 | peak->trough 44d/41tr | recovery=2023-04-27 #468 peak->recovery 240d/165tr
  deep3: depth=-11964.20 peak=2022-01-07 #150 cum=22831.00 trough=2022-01-28 #170 | peak->trough 21d/20tr | recovery=2022-02-11 #181 peak->recovery 35d/31tr
  deep4: depth=-11624.80 peak=2025-04-04 #915 cum=193616.60 trough=2025-04-09 #920 | peak->trough 5d/5tr | recovery=2025-04-09 #921 peak->recovery 5d/6tr
  deep5: depth=-10309.72 peak=2024-03-07 #665 cum=137376.60 trough=2024-04-11 #697 | peak->trough 35d/32tr | recovery=2024-04-19 #703 peak->recovery 43d/38tr
  LONGEST UNDERWATER: 461d (UNRECOVERED, counted to last trade exit 2026-07-15) = deep1, depth=-45282.04
-- R1 NAB_OppBand (episodes=53, unrecovered=1)
  MAX-DD episode = deep1 (depth equals Gate 0 max DD)
  deep1: depth=-50748.88 peak=2025-04-10 #630 cum=227700.20 trough=2026-03-11 #758 | peak->trough 335d/128tr | recovery: not recovered (open at last trade 2026-07-15); to last trade 461d/180tr
  deep2: depth=-30919.96 peak=2021-07-27 #44 cum=15514.76 trough=2022-01-27 #120 | peak->trough 184d/76tr | recovery=2022-02-24 #134 peak->recovery 212d/90tr
  deep3: depth=-24125.92 peak=2025-04-04 #625 cum=211575.00 trough=2025-04-08 #627 | peak->trough 4d/2tr | recovery=2025-04-09 #629 peak->recovery 5d/4tr
  deep4: depth=-13951.56 peak=2023-02-13 #286 cum=109413.44 trough=2023-04-24 #322 | peak->trough 70d/36tr | recovery=2023-05-26 #338 peak->recovery 102d/52tr
  deep5: depth=-13610.92 peak=2024-08-02 #529 cum=159919.16 trough=2024-08-07 #531 | peak->trough 5d/2tr | recovery=2024-08-22 #535 peak->recovery 20d/6tr
  LONGEST UNDERWATER: 461d (UNRECOVERED, counted to last trade exit 2026-07-15) = deep1, depth=-50748.88
-- R2 NAB_Flat1559 (episodes=72, unrecovered=1)
  MAX-DD episode = deep1 (depth equals Gate 0 max DD)
  deep1: depth=-40637.04 peak=2025-04-10 #922 cum=210700.88 trough=2026-06-03 #1171 | peak->trough 419d/249tr | recovery: not recovered (open at last trade 2026-07-15); to last trade 461d/268tr
  deep2: depth=-17176.36 peak=2022-08-30 #303 cum=100453.12 trough=2022-10-13 #344 | peak->trough 44d/41tr | recovery=2023-04-27 #468 peak->recovery 240d/165tr
  deep3: depth=-13534.20 peak=2022-01-07 #150 cum=22751.00 trough=2022-01-28 #170 | peak->trough 21d/20tr | recovery=2022-02-11 #181 peak->recovery 35d/31tr
  deep4: depth=-11049.80 peak=2025-04-04 #915 cum=184411.60 trough=2025-04-09 #920 | peak->trough 5d/5tr | recovery=2025-04-09 #921 peak->recovery 5d/6tr
  deep5: depth=-9939.72 peak=2024-03-07 #665 cum=130341.60 trough=2024-04-11 #697 | peak->trough 35d/32tr | recovery=2024-04-19 #703 peak->recovery 43d/38tr
  LONGEST UNDERWATER: 461d (UNRECOVERED, counted to last trade exit 2026-07-15) = deep1, depth=-40637.04
-- R3 LastHalfHourMomentum (episodes=16, unrecovered=1)
  MAX-DD episode = deep1 (depth equals Gate 0 max DD)
  deep1: depth=-99806.96 peak=2022-05-04 #278 cum=23797.12 trough=2026-07-17 #1304 | peak->trough 1535d/1026tr | recovery: not recovered (open at last trade 2026-07-17); to last trade 1535d/1026tr
  deep2: depth=-12305.28 peak=2021-05-10 #44 cum=5069.76 trough=2021-10-07 #137 | peak->trough 150d/93tr | recovery=2022-01-31 #214 peak->recovery 266d/170tr
  deep3: depth=-5318.68 peak=2022-02-25 #232 cum=17788.28 trough=2022-03-09 #240 | peak->trough 12d/8tr | recovery=2022-04-22 #270 peak->recovery 56d/38tr
  deep4: depth=-2281.84 peak=2021-03-09 (start) cum=0.00 trough=2021-03-12 #4 | peak->trough 3d/4tr | recovery=2021-03-24 #12 peak->recovery 15d/12tr
  deep5: depth=-1875.92 peak=2022-04-26 #272 cum=20554.88 trough=2022-04-28 #274 | peak->trough 2d/2tr | recovery=2022-05-02 #276 peak->recovery 6d/4tr
  LONGEST UNDERWATER: 1535d (UNRECOVERED, counted to last trade exit 2026-07-17) = deep1, depth=-99806.96
[exit 0]
```

### K09 — slippage arithmetic at 2/3/4 ticks per side + Qty distribution

```text
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py slip "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"
# R0=07-10 AM.csv 421c44e6cd9d
# R1=07-57 AM.csv 4207ea99e7f1
# R2=07-59 AM.csv 5a3c4d783a44
# R3=08-00 AM.csv 4efd8ce8e95c
== K09 Slippage: recorded at 2 ticks/side; adj = Profit - (k-2)*2*$5.00*Qty ==
-- R0 baseline NAB Qty distribution: {1: 1190}
  k=2 net=197327.60 PF=1.29 total deduction=0.00 (recorded net 197327.60: equal)
  k=3 net=185427.60 PF=1.27 total deduction=11900.00
  k=4 net=173527.60 PF=1.25 total deduction=23800.00
-- R1 NAB_OppBand Qty distribution: {1: 810}
  k=2 net=210182.40 PF=1.26 total deduction=0.00 (recorded net 210182.40: equal)
  k=3 net=202082.40 PF=1.25 total deduction=8100.00
  k=4 net=193982.40 PF=1.24 total deduction=16200.00
-- R2 NAB_Flat1559 Qty distribution: {1: 1190}
  k=2 net=193017.60 PF=1.28 total deduction=0.00 (recorded net 193017.60: equal)
  k=3 net=181117.60 PF=1.26 total deduction=11900.00
  k=4 net=169217.60 PF=1.24 total deduction=23800.00
-- R3 LastHalfHourMomentum Qty distribution: {1: 1304}
  k=2 net=-76009.84 PF=0.84 total deduction=0.00 (recorded net -76009.84: equal)
  k=3 net=-89049.84 PF=0.82 total deduction=13040.00
  k=4 net=-102089.84 PF=0.80 total deduction=26080.00
[exit 0]
```

### K10 — strategy name per file; entry/exit prices on the 0.25 grid (0.50 grid as firing control)

```text
$ for f in "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv" "$HOME/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv"; do print -r -- "== ${f:t}"; awk -F, 'NR>1{s[$4]++; for(i=7;i<=8;i++){n++; if($i*4!=int($i*4)) q++; if($i*2!=int($i*2)) h++}} END{for(k in s) print "strategy=" k " rows=" s[k]; print "prices checked=" n " off 0.25 grid=" q+0 " off 0.50 grid (control)=" h+0}' "$f"; done
== NinjaTrader Grid 2026-11-01 07-10 AM.csv
strategy=PraxisNoiseAreaBreakout rows=1190
prices checked=2380 off 0.25 grid=0 off 0.50 grid (control)=1240
== NinjaTrader Grid 2026-11-01 07-57 AM.csv
strategy=PraxisNoiseAreaBreakout_OppBand rows=810
prices checked=1620 off 0.25 grid=0 off 0.50 grid (control)=810
== NinjaTrader Grid 2026-11-01 07-59 AM.csv
strategy=PraxisNoiseAreaBreakout_Flat1559 rows=1190
prices checked=2380 off 0.25 grid=0 off 0.50 grid (control)=1242
== NinjaTrader Grid 2026-11-01 08-00 AM.csv
strategy=PraxisLastHalfHourMomentum rows=1304
prices checked=2608 off 0.25 grid=0 off 0.50 grid (control)=1316
[exit 0]
```

### K11 — share-of-net rule in the analysis script (source line)

```text
$ grep -n "share = " /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/csva/w1/analyze.py
196:    share = "n/a (net <= 0)" if full <= 0 else pct(s, full)
[exit 0]
```
