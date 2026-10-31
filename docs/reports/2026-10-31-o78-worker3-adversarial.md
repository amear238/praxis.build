# o78 worker 3: adversarial attack on worker 1 (symmetry), worker 2 (slippage unit), and manager synthesis claim 3

## Task
Unit `Praxis_build-o78`, worker 3. Break the claims in:
- `docs/reports/2026-10-31-o78-worker1-symmetry.md` (W1);
- `docs/reports/2026-10-31-o78-worker2-slippage-unit.md` (W2);
- the manager's synthesis claim 3 ("short side positive in points before costs … loss is entirely the $2.96 + $0.04 … 20× heavier relative to P&L than on real NQ").

## Mode
ADVERSARIAL. Read-only. This report is the only file I wrote in the repo. Nothing was staged or committed. My scratch scripts are in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/` (`w3_db.py`, `w3_bars.py`, `w3_w1diff.py`, `w3_more.py`, `w3_sim.py`, `w3_sim_ignore.py`, `w3_sim_eod.py`).

## Criterion
From `specs/SPEC_RUBRIC.md`:
- S1: "Every claim in a report has pasted command output."
- S2: "No component is reported at a higher level than the evidence supports."
- S8: "No question that belongs to Amear is answered on his behalf."
- S9: "A field that parses is not a field that is honoured."

## Process log
1. Hashed the `.cs` file (`35393823…2265`, which matches). Read lines 138–312 myself and diffed every W1 `sed -n` block byte-for-byte against the source.
2. Re-queried all three sqlite copies with `mode=ro&immutable=1` (via `python3 -I`):
   - the NQCONT masters and instruments;
   - the InstrumentType census;
   - the Strategies, Strategy2Instrument and Executions linkage.
   I also parsed every `strategyanalyzerlogs/*.xml` under the rescue (Instrument field) and partitioned the summary fields by whether they change across PerformanceUnit.
3. Ran bar-file statistics on `NQCONT.Last.txt` (sha256 `307c5e8a…e16e454`):
   - RTH range and run-up;
   - stamp-entry→16:00 extremes;
   - yearly path and gap mix;
   - |gap|·σ in points;
   - band distance from the open;
   - a random-entry MAE scale.
4. Exact-match search for the run-4 largest winner. Brute-forced (point value × tick × slippage) models for the five extreme trades.
5. Wrote a Python replication of `OnBarUpdate`/`BuildBand`. It is not NT8, and its fill model is assumed (see F4). I ran 3 variants against the run-4 window.
6. Checked the synthesis arithmetic and re-costed it at real-NQ terms.
7. Viewed the run-3 screenshot `docs/reports/evidence/2026-10-30-run3-strategy-analyzer-summary.webp` myself.

## Verification evidence (pasted)

### E1. W1 code blocks: byte-for-byte diff against the source
```
block 226-229: BYTE-IDENTICAL
block 261-265: BYTE-IDENTICAL
block 205-220: BYTE-IDENTICAL
block 189-193: BYTE-IDENTICAL
block 285-291: BYTE-IDENTICAL
block 147-161: BYTE-IDENTICAL
block 196-201: BYTE-IDENTICAL
block 171-176: BYTE-IDENTICAL
blocks checked 8
108 'IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary'
109 'ExitOnSessionCloseSeconds                 = 30;'
```

### E2. sqlite re-query (newest DB shown; both `.bak` copies give the same structure, with the Stock NQCONT under Ids 754596 and 754595)
```
=== DB NinjaTrader.sqlite 4505600
  MI NQCONT: [(699839150754594, 'NQCONT', 0, 20.0, 0.25, 'CME US Index Futures RTH', -10200), (699839150754605, 'NQCONT', 1, 1.0, 0.01, 'US Equities RTH', 1)]
  INST NQCONT: [(699839150770811, 23, 599266080000000000, 699839150754594, 99, 0.0), (699839150770940, 23, 638922816000000000, 699839150754594, 99, 0.0), (699839150770941, 9, 662353632000000000, 699839150754605, 99, 0.0)]
  Strategy2Instrument all rows: [(699839150764686, 395507798, 0), (699839150764686, 395507799, 0), (699839150764686, 395507801, 0), (699839150764686, 395507802, 0), (699839150765778, 395507797, 0)]
  S2I rows pointing at NQCONT instrument ids: []
  Executions by instrument: [(699839150764686, 14)]
  Executions on NQCONT ids: (0,)
  type 0 (366, 84135.20950819673) ['CL', 'ES', 'GC', 'NQ']
  type 1 (1040, 1.0) ['AAPL', 'CL', 'ES', 'MSFT', 'NQ', 'QQQ', 'SPY']
  type 2 (52, 1.0) ['TRINQ', 'VIX']
  type 4 (64, 0.79890625) ['EURUSD']
  type1 rows with PointValue!=1: (0,)  type0 rows with PointValue==1: (15,)
(all 5 Strategies rows are PraxisSignalConsumer)
=== Analyzer log XMLs (all under VM-Rescue)
NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml Instrument ['NQ SEP26'] Slippage ['0'] Commission? ['false']
NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml Instrument ['NQ SEP26'] Slippage ['0'] Commission? ['false']
NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml Instrument ['NQ SEP26'] Slippage ['0'] Commission? ['false']
NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml Instrument ['NQ SEP26'] Slippage ['0'] Commission? ['false']
```

### E3. XML field partition across PerformanceUnit
```
XML @@@PraxisNoiseAreaBreakout_2026_07_17_01.xml units ['Currency', 'Percent', 'Pips', 'Points', 'Ticks']
FIELDS IDENTICAL ACROSS ALL UNITS: ['AverageBarsInTrade', 'AverageNumTradesPerDay', 'AverageTimeInMarket', 'Commission', 'GrossLoss', 'GrossProfit', 'LongestFlatPeriod', 'MaxConsecLosers', 'MaxConsecWinners', 'MaxTime2Recover', 'NumEvenTrades', 'NumLosingTrades', 'NumWinningTrades', 'PercentProfitable', 'Performance', 'Probability', 'ProfitFactor', 'RSquared', 'SharpeRatio', 'SortinoRatio', 'TotalNetProfit', 'TotalNumTrades', 'TotalSlippage', 'UlcerIndex']
FIELDS THAT DIFFER ACROSS UNITS: ['AverageEtd', 'AverageLosingTrade', 'AverageMae', 'AverageMfe', 'AverageTrade', 'AverageWinningTrade', 'GrossLossValue', 'GrossProfitValue', 'LargestLosingTrade', 'LargestWinningTrade', 'MaxDrawdown', 'ProfitPerMonth', 'RatioAvgWinAvgLoss', 'TotalNetProfitValue']
  TotalNetProfit {'Currency': ('17005', '22360', '-5355'), 'Percent': ('17005', '22360', '-5355'), 'Pips': ('17005', '22360', '-5355'), 'Points': ('17005', '22360', '-5355'), 'Ticks': ('17005', '22360', '-5355')}
  TotalSlippage {'Currency': ('0', '0', '0'), 'Percent': ('0', '0', '0'), 'Pips': ('0', '0', '0'), 'Points': ('0', '0', '0'), 'Ticks': ('0', '0', '0')}
  AverageMae {'Currency': ('1967.9924', '1823.8571', '2130.7258'), 'Percent': ('0.0036', '0.0033', '0.0039'), 'Pips': ('393.5985', '364.7714', '426.1452'), 'Points': ('98.3996', '91.1929', '106.5363'), 'Ticks': ('393.5985', '364.7714', '426.1452')}
```

### E4. Bar-file statistics
```
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
RTH days 1494 first 20210308 last 20260720
TOP5 RTH high-low: [(16851.5, '20240120'), (2184.5, '20250409'), (1688.0, '20250407'), (1620.5, '20260609'), (1383.75, '20250408')]
RTH days with high-low >= 1792.5: 2  >= 758.25: 20  median range 217.75
TOP5 stamp-entry->16:00 trades (pts): [(2027.25, 'L', '20250409', 110000), (1931.5, 'L', '20250409', 120000), (1853.0, 'L', '20250409', 113000), (1805.5, 'L', '20250409', 100000), (1805.25, 'L', '20250409', 103000)]
YEARLY RTH first-open -> last-close: {'2021': (16032.75, 19755.25, 23.2), '2022': (19813.25, 14232.25, -28.2), '2023': (14329.0, 19492.5, 36.0), '2024': (19350.75, 22660.75, 17.1), '2025': (22787.75, 25980.25, 14.0), '2026': (26207.0, 29016.0, 10.7)}
gap-up days 683 gap-down days 610 median |gap| pts 58.5 p90 222.0
|gap|*sigma pts at 120000 median 0.357 p90 1.459 max 6.72
|gap|*sigma pts at 153000 median 0.504 p90 1.496 max 6.84
|gap|*sigma pts at 100000 median 0.19 p90 0.902 max 3.56
random stamp entries 15951 mean MAE long pts 58.98 short 54.35 mean |move| over <=106 bars 56.18 share of entries with MAE_long <= 2.61 pts 0.043
```

### E5. Exact match, band distance from the open, synthesis arithmetic, model brute force
```
rows dated 20240120 (+ 20240119 >=15:58): 71
20250409 long hits delta==1795.50: [(123000, '16:00close', Decimal('1795.50'))] short hits: [] | 16:00 close 20486.75 last bar t 160000
   stamp fills (next-bar open): [(100000, '18681.25'), (103000, '18681.5'), (110000, '18459.5'), (113000, '18633.75'), (120000, '18555.25'), (123000, '18691.25'), (130000, '18766.5'), (133000, '19634.25'), (140000, '20112.5'), (143000, '20275'), (150000, '20011.75'), (153000, '20386')]
20250407 long hits delta==1795.50: [] short hits: [] ...
20250408 long hits delta==1795.50: [] short hits: [] ...
stamp 100000 days 338 mean(U-open) 117.04 mean(open-L) 121.08 median(U-open) 74.68 median(open-L) 84.49 mean gap 4.41 share days long-trigger closer to open 0.53
stamp 120000 days 332 mean(U-open) 162.1 mean(open-L) 165.13 median(U-open) 117.42 median(open-L) 129.26 mean gap 3.65 share days long-trigger closer to open 0.527
stamp 153000 days 208 mean(U-open) 181.09 mean(open-L) 195.08 median(U-open) 145.31 median(open-L) 160.07 mean gap 14.68 share days long-trigger closer to open 0.567
--- synthesis arithmetic
run4 S pre-cost pts 476.44 run3 S 219.4 run4 L 6293.4 run4 S costs 1881.0 pts/trade S 0.7599
cost in POINTS per RT: $1/pt model 3.0 | real NQ $20/pt, 2.96 comm + 2 ticks/side slip ($20/RT): 1.148 | real NQ, comm only: 0.148 | ratio $1/real(locked) 2.613 | commission-only ratio 20.0 | slippage ratio $1/real 0.04
run4 S at real NQ $20/pt: comm only 7672.88 | comm + 2 ticks/side -4867.12
run3 S at real NQ $20/pt: comm only 2751.12 | comm + 2 ticks/side -8308.88
run4 L at real NQ $20/pt: comm only 124139.36 | comm + 2 ticks/side 112459.36
residue (net + 3n) mod 0.25 run4 S: 0.19 run4 L: 0.15
per-trade side gap run4 L-S $ 10.016 -> pts at $1: 10.016 pts at $20: 0.501
--- alternative models for extremes (P in $): need (P + cost) % (20*0.25) == 0 at $20/pt; solve cost mod 5 for each
{'r3 W': '-0.25', 'r3 L-W': '-3.00', 'r3 Loss': '4.25', 'r3 L-Loss': '3.00', 'r4 W': '-2.50'} <- required per-trade cost mod $5; a single constant cost needs all equal
  FITS ALL 5: pv 1 tick 0.01 slip ticks/side 2 cost/RT 3.00
  (any model not printed above fails at least one of the 5 extremes)
```
The brute force covered point value {20, 5, 2, 1} × tick {0.25, 0.01} × slippage {0, 1, 2} ticks/side, with a $2.96 commission.

### E6. Python replication of the strategy (INFERRED quality; not NT8)
Assumptions:
- Fill model: stamp orders fill at the next bar's open, and the 16:00 flat fills at the 16:00 close.
- Costs: 0.02/side slippage and 2.96 commission, at $1/pt.
- Weekend bars are excluded.
- Data identity with Fusion is UNVERIFIED.
```
SIM slip/side 0.02 window 20210308 20260717
  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1180, '9230.25', '5690.25')
  long  (581, '5683.00', '3940.00')
  short (599, '3547.25', '1750.25')
  largest win 1 1792.50 20250409 123100 -> 160000 | largest loss 1 -325.75 20260702
  REPORTED run 4: n 1211 (L 584 / S 627), net 3136.84, L +4541.40, S -1404.56, largest win 1792.50
SIM[reversal-entry-IGNORED variant] slip/side 0.02 window 20210308 20260717
  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1177, '9300.25', '5769.25')
  long  (580, '5635.25', '3895.25')
  short (597, '3665.00', '1874.00')
SIM[flat-at-last-bar-of-every-session variant] slip/side 0.02 window 20210308 20260717
  all  n, gross_pts(entry-slipped), net$ at $1/pt: (1179, '9895.50', '6358.50')
  long  (581, '6028.75', '4285.75')
  short (598, '3866.75', '2072.75')
  largest win 1 1792.50 20250409 123100 -> 160000 | largest loss 1 -325.75 20260702
```
(The column label "gross_pts(entry-slipped)" is stale. After the patch, gross is raw bar-price points, and net = gross − 0.04·n − 2.96·n. Check: 9230.25 − 1180×3.00 = 5690.25.)

### E7. Run-3 screenshot (viewed by me) and record lines
In the screenshot:
- `Display: Summary ($)`.
- Total slippage reads `43 | 20.88 | 22.12` with no `$`, while Commission reads `$3,182.00` and Total Fees reads `$0.00`.
- The Instrument field reads the bare `NQCONT`.
- Trading hours is `CME FX Futures RTH`, Slippage is `2`, and Exit on session close is checked.

Record lines:
```
5:**Window:** NinjaTrader 8 Strategy Analyzer, Display = `Summary ($)`, ...
60:| Total slippage | **43** | 20.88 | 22.12 |
67:| Largest winning trade | $580.25 | $373.00 | $580.25 |
68:| Largest losing trade | −$319.25 | −$318.00 | −$319.25 |
75:| Avg. MAE | $52.13 | $47.73 | $56.27 |
--- market-and-stop claim, rescue bin      (grep -rIl slippage over NinjaTrader 8-full/bin → no output)
--- 2024-01-20 Saturday rows (bad prints)
995796:20240120 135800;3100;3100;3100;3100;2
6
```

## Findings

| id | target claim | severity | evidence | required correction (exact replacement text) |
|---|---|---|---|---|
| F1 | Synthesis: "…which on a $1/pt instrument is 20× heavier relative to P&L than on real NQ" | **MAJOR** | E5: only the commission is 20× heavier in points (0.148 → 2.96). The simulated slippage is **25× lighter** (0.04 pt/RT vs 1.00 pt/RT under the locked 2 ticks/side). Total cost per trade is 3.00 pts vs 1.148 pts = **2.613×**, not 20×. Re-costed on real-NQ terms with the locked F3 model, run-4 shorts are **−$4,867.12** and run-3 shorts **−$8,308.88**. | "IF the $1/pt reading holds, the short side was positive in points before costs (run 4: −1,404.56 + 627 × 3.00 = +476.44 pts, 0.76 pt/trade; run 3: +219.40 pts). On a $1/pt instrument the $2.96 commission weighs 20× more in points than on real NQ. The simulated slippage (0.04 pt/RT), however, is 25× lighter than the locked 2 ticks/side (1.00 pt/RT). Net, the run charged 3.00 pts/trade, 2.6× the locked real-NQ cost of 1.148 pts. Re-costed at $20/pt under the locked F3 model, run-4 shorts are −$4,867.12 and run-3 shorts −$8,308.88 (arithmetic only; inherits the residue caveat)." |
| F2 | Synthesis: "so the reported short-side loss is **entirely** the $2.96 commission + $0.04 slippage per trade" | **MAJOR** | (a) E5: residue `(−1404.56 + 627×3.00) mod 0.25 = 0.19`, so model C does not hold exactly for the run-4 shorts. (b) Run-4 per-side commission and slippage are NOT on record (W1 §3); 627 × 3.00 is assumed. (c) E6 (INFERRED, not NT8): a replication of the same code on the import file, with the same costs, gives shorts **+1,750.25 to +2,072.75** after costs, against the REPORTED −1,404.56. That leaves ~3,150–3,480 pts of short shortfall that costs do not explain. Longs come out at +3,940 to +4,285.75 vs REPORTED +4,541.40. | "Arithmetic only: under the $1/pt reading, run-4 short costs (627 × 3.00 = 1,881 pts, assumed; per-side costs are not on record) exceed the short side's pre-cost result (+476.44 pts). That is an accounting identity, not a cause. A Python replication of the strategy on the import file (INFERRED, not NT8, fill model assumed) gives shorts +1,750 to +2,073 after the same costs. So most of the reported short loss is not explained by costs, and the cause is open." |
| F3 | W2 bottom line 1 and §(b): "OBSERVED: NT8 serializes TotalSlippage once per PerformanceUnit, so the Summary value is unit-dependent". Also readback 4: "this one switch settles the unit … Expected … Points 48.44 and Ticks 4,844" | **MAJOR** (S2) | E3: every summary field is repeated per unit, including fields that never change. TotalNetProfit `17005` and TotalNumTrades are identical in all five units. Unit-dependent quantities live in separate fields (`TotalNetProfitValue`, `GrossProfitValue`) or are inherently per-unit (`AverageMae` 1967.99 / 98.40 / 393.60). There is **no `TotalSlippageValue`**, and TotalSlippage sits in the unit-invariant group with Commission and TotalNetProfit. Per-unit storage therefore does not imply unit dependence. The structure points the other way, though with TotalSlippage = 0 nothing is calibrated. | "OBSERVED: the Analyzer log XML repeats every summary field, TotalSlippage included, under each PerformanceUnit. That includes fields that never change with the unit (TotalNetProfit 17005 and TotalNumTrades 132 are identical in all five). Unit-dependent quantities are carried in separate fields (TotalNetProfitValue, GrossProfitValue, AverageMae, …), and no TotalSlippageValue exists. So the XML does not show that Total slippage changes with the display unit; its structure groups it with the fixed fields. Both logs have TotalSlippage 0, so nothing is calibrated either way." Readback 4 should become: "Switch Currency → Points → Ticks and read Total slippage in each. If it reads 48.44 in every unit, the switch does **not** settle the unit; use readbacks 1–3 instead." |
| F4 | W1 hypothesis set H1–H8 and §1 conclusion ("Code-level asymmetry found: none that bears on behaviour"). Specifically, H2–H4 offered as the market-side explanations, with no hypothesis covering engine or data divergence. | **MAJOR** (completeness, not over-label) | E6: replicating the symmetric code on the same data reproduces run 4's largest winner **to the cent** (+1,792.50, long, 2025-04-09, 12:31 fill → 16:00 close) and the long side roughly (581 vs 584 trades). It does **not** reproduce the short side (598–599 vs 627 trades, +1,750 to +2,073 vs −1,404.56). The extra NT8 trades fall almost entirely on the short side (+28–29 shorts vs +3 longs). On this data, market drift does not by itself make shorts lose. Separately, E4 shows W1's "UNVERIFIED" inputs were checkable on disk: 2022 is −28.2%; gap-up days outnumber gap-down 683 to 610. | Add to W1 §2: "**H9: The NT8 run diverges from a clean model on the short side (data, session/holiday handling, fill engine, or instrument type). INFERRED.** A Python replication of the symmetric code on the import file (sha256 307c5e8a…) reproduces run 4's largest winner exactly and the long side roughly. It does not reproduce the short side (598–599 trades, +$1,750 to +$2,073 at $1/pt, vs REPORTED 627 trades, −$1,404.56). *Falsifier:* export the run-4 Trades tab and diff it against the replication's trade list. If the extra or divergent trades are not concentrated on the short side, H9 is falsified." Also downgrade H2 to "weakened: on the import file a clean replication's shorts are profitable". |
| F5 | W1 row 2 / H1: "the short trigger sits slightly closer … slightly favours short triggers … cannot plausibly explain a ~$10/trade gap" (the brief's paraphrase: "makes shorts trigger slightly easier") | MINOR | **Relative to its own reference:** correct. **Relative to the session open, in this sample:** backwards. E5 gives mean(U−open) < mean(open−L) at every stamp (12:00: 162.10 vs 165.13), with the long trigger closer on 53–57% of days. That is the gap mix (683 up / 610 down); the code is not involved. **Magnitude:** median \|gap\|·σ is 0.19–0.50 pt, p90 0.90–1.50, max 6.84 (E4). At $20/pt the side gap is 0.50 pt/trade, the same order, so "cannot plausibly explain" holds only under $1/pt (10.0 pts/trade), a point value W1 declined to adopt. | "In price space the upper band sits \|gap\|·σ further from its own reference than the lower band (median 0.19–0.50 pt, p90 0.90–1.50 pt, max 6.84 pt, 2021–2026, at 10:00/12:00/15:30). Measured from the session open, where price starts, this sample's gap mix (683 gap-up vs 610 gap-down days) makes the long trigger closer on average (12:00: 162.10 vs 165.13 pts) and on 53–57% of days. Neither is a code asymmetry. Whether 'closer' helps or hurts P&L is not established. Its size relative to the side gap depends on the open point-value question (0.50 pt/trade at $20/pt; 10.0 pts at $1/pt)." |
| F6 | W1 §3 "`curUpper ≥ curLower` … OBSERVED by algebra plus a 1M-trial random check". W1 also pastes elided commands: `python3 -c "... 1M trials ..."`, `grep -n Enter/Exit`, `grep -n -E "^\| *S(1\|2\|8) \|..."` | MINOR (S2/S1) | W1 lines 155, 162, 138, 15, 244 (read above). Algebra is not observation. Elided commands cannot be re-run. | "INFERRED (algebra) and simulated (1M random trials; full command pasted below). Not observed in NT8." Paste the full commands. |
| F7 | W2 bottom line 2: "OBSERVED … type 0 = **Future** … type 1 = **Stock**" | MINOR (S2) | E2: the type→name mapping is W2's own INFERRED at line 193. Re-run: type 1 has 1,040 rows, all PointValue 1.0, including AAPL/MSFT/QQQ/SPY plus stock-typed duplicates of CL/ES/NQ. The mapping is solid, but it is inferred. | "type 1 (INFERRED = Stock: 1,040 rows, all PointValue 1.0, containing AAPL, MSFT, QQQ, SPY)"; likewise "type 0 (INFERRED = Future)". |
| F8 | W2 bottom line 6 / grid limits: "the extreme-trade test cannot by itself tell '0.04 slippage + 2.96 commission' apart from 'trade P&L shown before all costs'" | MINOR (understated) | E5/E6: the run-4 largest winner maps to one specific trade in the import file. The 2025-04-09 12:30 stamp fills at 18,691.25 and exits at the 16:00 close of 20,486.75, a gross of 1,795.50; displayed = 1,795.50 − 3.00 = 1,792.50. "Before all costs" would display 1,795.50. Conditional on Fusion's data being this file (UNVERIFIED). | Add: "The run-4 largest winner matches one trade in the import file to the cent once 3.00 of costs are deducted (2025-04-09, long, 12:31 open 18,691.25 → 16:00 close 20,486.75). 'Before all costs' would show 1,795.50, so it is disfavoured for that trade (INFERRED; assumes Fusion data = import file)." |
| F9 | Out of scope (reported, not fixed): the import file | MINOR | E7: there are 6 rows dated **Saturday 2024-01-20**, one at `3100` (13:58) while real prices are ~17,500, giving an RTH range of 16,851.5 pts (E4). Harmless if the RTH template excludes Saturday (UNVERIFIED). | Note only. Whether to clean the file is Amear's call. |

## Claims that SURVIVED (re-run output above)
- **W1 code-level symmetry (S).** 8/8 pasted blocks are byte-identical (E1). My own read of lines 138–291 found no long/short asymmetry. I checked:
  - exit-before-entry ordering, and the pre-fill `MarketPosition` used by both blocks;
  - `FlattenAll` and `IsExitOnSessionClose` (side-neutral);
  - Max/Min with VWAP on the far side (mirrored), and ties (exits inclusive, entries strict, on both sides);
  - the else-if order and the VWAP guard.

  The NT8 reversal resolution (R21/H8) cannot by itself make the split: ignoring the entry on reversal moves shorts only from +1,750.25 to +1,874.00 (E6).
- **W1 H6 arithmetic** holds. The side is still "not on record", but the replication says long (INFERRED).
- **W2 (a)**: no NT8 text on disk defines Total slippage. My grep over the rescue `bin` returns nothing (E7).
- **W2 (b)**: there are two NQCONT masters (Future 20/0.25, Stock 1/0.01) in all three DBs (E2).
- **No on-disk record of which NQCONT runs 3/4 used.** Strategy2Instrument and Executions reference only instruments 699839150764686/765778 (0 NQCONT executions). All 4 XMLs are `NQ SEP26`. The screenshot Instrument field reads bare `NQCONT`.
- **W2 per-trade grid test.** Of 24 (point value, tick, slippage) models, only $1/0.01/2-ticks fits all five extremes. The per-trade cost each extreme requires (mod $5) differs, so no constant commission rescues $20/pt (E5).
- **W2 magnitude argument, both ways.**
  - At $1/pt the run-3 avg MAE is 52.13 pts. Random stamp entries give 54–59 pts, and the real-NQ log gives AverageMae of 98.40 pts.
  - At $20/pt it would be 2.61 pts; only 4.3% of random entries are that small (E3, E4).
  - $1,792.50 at $1/pt is possible: 2 RTH days have a range ≥ 1,792.5, and an exact trade exists (E4, E5).
- **"43" has no unit.** I viewed the screenshot: Total slippage has no `$`, while the $ rows carry `$` (E7).
- **"ticks/100 is not an NT8 unit".** It is not one of the five on-disk PerformanceUnits (E3), and W2 already marks it UNVERIFIED.
- **W2 (d)** ("market and stop, not limit"): no NT8 source on disk (E7 grep); the origin is voice notes `:42` "Claude's estimate".
- **Synthesis arithmetic**: 476.44, 219.40 and 6,293.40 are correct (E5). Only the inference drawn from them is broken (F1, F2).
- **S8**: neither worker report decides anything for Amear. Both route readbacks to him, and W2 explicitly leaves the $107,592 figure's meaning to him. The synthesis contains no S8 violation.
- **W2 run-3/run-4 inputs and W1 run-3 rows** match the record and the screenshot (E7).

## Files staged
None. One file was written: `docs/reports/2026-10-31-o78-worker3-adversarial.md`. It is not `git add`-ed. Scratch scripts are in the scratchpad named above.

Per-artifact: W1 SURVIVED-WITH-CORRECTIONS (F4, F5, F6) · W2 SURVIVED-WITH-CORRECTIONS (F3 breaks its bottom line 1 and readback 4; F7, F8) · Synthesis claim 3 BROKEN (F1, F2).

VERDICT: BROKEN
Result: PASS
