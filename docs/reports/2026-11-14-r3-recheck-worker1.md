# 2026-11-14 R3 recheck — worker 1 of 2

## Task
Unit `2026-11-14-r3-recheck`, worker 1. Mode: BUILD (read-only research). The rule is R3 (`docs/reports/2026-11-14-voice-notes-pivot.md` :18-:24): every trade has a PREDEFINED maximum loss known before entry. R4 (:26-:29) asks for a recheck of five tested strategies against R3. This report gives facts only. It recommends no percentage, no cap and no strategy to keep (those are Amear's Q2/Q3/Q6).

Criterion: rubric S1 (every claim has pasted command output next to it), S2 (no level above what the evidence supports) and S8 (no answer to a question that belongs to Amear).

Every evidence block below is quoted from one of two files. `/tmp/praxis-r3/w1_shell.txt` holds the shell commands, run through a bash `run` wrapper that prints `$ cmd`, the output and the exit code. `/tmp/praxis-r3/w1_out.txt` holds the script output, pasted in full under "Script output". Section tags such as `[3]` refer to that output.

Script hash:
```
$ shasum -a 256 /tmp/praxis-r3/w1_r3.py /tmp/praxis-r3/w1_out.txt
8a8251cb838da1f501236f0b4bfb819f38b6f2efd8a4091acbc397c470a45a0c  /tmp/praxis-r3/w1_r3.py
6138d4c363bc6188fc926e51cc04b4ed9a7869c7e06d8383d5d6ad47f77acf5e  /tmp/praxis-r3/w1_out.txt
```
How it was run: `python3 -I /tmp/praxis-r3/w1_r3.py 2>&1 | tee /tmp/praxis-r3/w1_out.txt` (python exit 0). The script sets `sys.dont_write_bytecode = True` before it imports `scripts/wf/sessions.py`. Afterwards `ls scripts/wf/__pycache__` gives "No such file or directory" (pasted in Inputs).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Inputs (sha256)
```
$ git rev-parse --short HEAD
244cfc3

$ shasum -a 256 docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv research/search-loop/c1-gap-fade/RULES.md research/search-loop/c1-gap-fade/out/trades_V2_full.csv research/search-loop/c1-gap-fade/out/summary.json
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3  research/search-loop/c1-gap-fade/RULES.md
6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045  research/search-loop/c1-gap-fade/out/trades_V2_full.csv
71cd073391018c4a27b783547a8df4143f9948eea77ceb064d57bf2619c9a9a8  research/search-loop/c1-gap-fade/out/summary.json

$ sed -n 29,32p docs/reports/2026-11-01-three-strategy-results.md
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentum grid | `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9` |
```
All four committed CSVs match the report: `[1]` prints `match=True` ×4. **Citation correction:** the brief cited the results report at :26-:29. The sha256 table rows are at **:29-:32** (above). Lines :26-:28 are a blank line, the table header and the separator row.

Gap fade RULES.md is untracked here and byte-identical to the parked branch:
```
$ git status --short research/search-loop/c1-gap-fade/; git show parked/Praxis_build-vn4:research/search-loop/c1-gap-fade/RULES.md | diff - research/search-loop/c1-gap-fade/RULES.md; echo diff_exit=$?
?? research/search-loop/c1-gap-fade/
diff_exit=0
```
The RULES.md sha256 above (`f892a265…`) equals `inputs.rules_sha256` in summary.json (`"rules_sha256": "f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3"`, seen with `cat out/summary.json` this session).

Session calendar: `sessions.py` sha256 `9ee58ef9…` and bar file sha256 `307c5e8a…` (`[4]`). Both equal the values in summary.json `inputs`.

```
$ ls scripts/wf/__pycache__
ls: scripts/wf/__pycache__: No such file or directory
[exit 1]
```

## Cost basis and slippage (applies to (b) and (c) for all NT8 rows)
```
$ sed -n 1063p DECISIONS.md | grep -o 'Fees: apply[^.]*'
Fees: apply MFFU's published round trip — NQ $4
[exit 0]

$ sed -n 1063p DECISIONS.md | grep -o 'MNQ $1.90'
MNQ $1.90
```
The brief's exact grep stops at the first `.`, which is the decimal point in "$4.68", so it does not reach the MNQ figure. The script prints the longer span (`[2]`): `Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new `.

```
$ sed -n 51p docs/reports/2026-11-01-three-strategy-results.md
- **Entry fill pattern** (OBSERVED): ... Plain words: in this data, slippage is 2 ticks adverse from the bar open, clipped to the bar's range. No claim is made about how NT8 implements that.
```
(the full line is in `/tmp/praxis-r3/w1_shell.txt`. Lines :77 and :253 are printed in `[2]`: baseline session-close exits fill at the 16:00 CLOSE ±2 ticks, clamp model 423 of 423.) The fills therefore already include 2 ticks per side. 1 tick = 0.25 pt = $0.50 at MNQ, so 2 ticks/side = $2.00 per round trip at MNQ. That amount is already inside NQ gross / 10 and is **not** added again. Each headline below also carries a **sensitivity** line: the same figures with a further $2.00 per trade subtracted. That is the double-count case, not the base case.

Checks before conversion (from `[3]`, the same for all four NT8 lists):
- `Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []`
- `money fields in parentheses format: 0`. Negatives use a leading `-` (706 / 340 / 708 / 683 Profit fields).
- `Qty values [('1', N)]`. `Trade number strictly 1..N in file order: True`.
- `trades with entry date != exit date: 0` on all four lists.

Worked trade: the first losing row of the baseline, from `[3]`:
```
raw: {'Trade number': '1', 'Market pos.': 'Short', 'Qty': '1', 'Entry price': '16270.25', 'Exit price': '16297.25', 'Entry time': '2021-03-29 10:01:00 AM', 'Exit time': '2021-03-29 11:31:00 AM', 'Exit name': 'XS', 'Profit': '-$542.96', 'Commission': '$2.96', 'MAE': '$1050.00'}
points = (16297.25 - 16270.25) x -1 = -27.00
NQ gross = Profit + Commission = -542.96 + 2.96 = -540.00  (= points x 20 = -540.00)
MNQ net = NQ gross / 10 - 1.90 = -540.00 / 10 - 1.90 = -55.90
MAE at 1 MNQ = 1050.00 / 10 = 105.00
```

## Stop-order API grep (all four NinjaScript sources)
```
$ cd ninjascript; for f in ...4 files...; do for p in SetStopLoss SetProfitTarget SetTrailStop EnterLongStopMarket EnterShortStopMarket ExitLongStopMarket ExitShortStopMarket StopMarket; do printf "%s %s: " $f $p; grep -c $p $f; done; done
```
All 32 counts are `0`. The full output is in the Script output section, under the shell evidence file. The loop exit code is 1 because `grep -c` returns 1 on zero hits.

```
$ cd ninjascript; grep -nE "Calculate +=|IsExitOnSessionCloseStrategy +=|ExitMode +=" ...
PraxisNoiseAreaBreakout.cs:105:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout.cs:118:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; ...
PraxisNoiseAreaBreakout_OppBand.cs:128:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout_OppBand.cs:141:				ExitMode      = PraxisNoiseExitMode.OppBand;    ...
PraxisNoiseAreaBreakout_Flat1559.cs:138:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout_Flat1559.cs:151:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; ...
PraxisLastHalfHourMomentum.cs:145:				Calculate                                 = Calculate.OnBarClose;
```
(Excerpt. The full grep output is in the shell evidence below.) Every exit in all four sources is `ExitLong(...)` / `ExitShort(...)`. These are managed **market** orders submitted in `OnBarUpdate` under `Calculate.OnBarClose`. No resting stop order exists in any of the four files.

## Per strategy

### 1. PraxisNoiseAreaBreakout (baseline, BandOrVWAP)
**(a) Exit/stop logic.**
```
$ sed -n 196,221p ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

			double price = Close[0];             // the checkpoint stamp price (spec §2: evaluate at the stamp, not intrabar)
			...
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			...
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
$ sed -n 188,192p ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
```
(The full blocks are in the shell evidence.) The variable is named `stop`, but it is a trailing level: max(upper band, VWAP) for a long, min(lower band, VWAP) for a short. The level is compared only with the **close of the HH:00 / HH:30 checkpoint bar**. When the close is through it, a market exit is submitted. Price can run past the level for up to 30 minutes with no exit. The level moves with the band and VWAP. Nothing caps the distance from entry. The other exits are a reversal (a market order) and the 16:00 flat (a market order).
**Per-trade maximum loss known before entry: NO.** Kind: band/VWAP-based trailing level, checked at 30-minute bar closes and exited at market. It does not cap the loss.

**(b)/(c)/(e)** `[3]` and `[4]`, labelled [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]:
```
trades 1190 | losers (MNQ net < 0) 712 | zero-net 0 | winners 478
largest single loss $-542.40 on 2026-06-25 | average loss $-97.26
[streak] runs of max length 10: 2 -> [('2022-09-15', '2022-09-26', '-802.00'), ('2026-05-11', '2026-05-20', '-1070.50')]
worst session-date loss $-705.10 on 2022-10-13 (4 trades that day)
largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.085%
largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.362%
largest MAE at 1 MNQ $747.50 on 2026-06-25
sessions with >=1 trade 792 | most trades in one session 5 (on 2023-12-04 +2 other dates)
avg trades per session-with-a-trade 1.5025
losers by exit name (count, largest loss MNQ): [('Exit on session close', 65, '-359.90'), ('XL', 284, '-447.40'), ('XS', 363, '-542.40')]
SENSITIVITY (further $2.00/trade subtracted ...): largest loss $-544.40 (2026-06-25) | average loss $-98.03 over 721 losers | worst day $-713.10 (2022-10-13)
trades 1190 / N 1352 = 0.8802 per session | trade dates not in calendar: 0 []
```
Longest losing streak: 10 trades, reached twice. The two runs summed −$802.00 (2022-09-15..09-26) and −$1,070.50 (2026-05-11..05-20).
**(d) Fails R3 as tested.** It has no predefined per-trade maximum loss, and the trailing level is checked only at 30-minute bar closes with a market exit.

### 2. PraxisNoiseAreaBreakout_OppBand
**(a)**
```
$ sed -n 229,244p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
				if (price <= stop)
					ExitLong("XL", "");
			...
					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
				if (price >= stop)
					ExitShort("XS", "");
$ sed -n 30,33p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
// CONSEQUENCE (3gm Q2): with the opposite band, the OppBand exit condition (long: Close <= LowerBound;
//   short: Close >= UpperBound) coincides with the reversal trigger (Close < LowerBound /
//   Close > UpperBound). OppBand therefore becomes "reverse or hold to 16:00". A flat-only exit
//   happens only at exact equality, Close == band (INFERRED, not run).
```
The default is `ExitMode = OppBand` (:141). The exit level is the opposite band. It uses the same checkpoint-close test as the baseline (the same `isCheckpoint` / `Close[0]` structure, file :219 in the earlier grep) and the same market `ExitLong`/`ExitShort`. In the data, `exit names: [('Exit on session close', 792), ('XL', 10), ('XS', 8)]` (`[3]`). In practice, then, it holds to the session close.
**Per-trade maximum loss known before entry: NO.** Kind: band-based (opposite band) level, checked at 30-minute bar closes and exited at market. It does not cap the loss.

**(b)/(c)/(e)** [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]:
```
trades 810 | losers (MNQ net < 0) 346 | zero-net 0 | winners 464
largest single loss $-1,960.90 on 2025-04-08 | average loss $-232.61
[streak] runs of max length 6: 2 -> [('2021-11-17', '2021-11-24', '-1429.40'), ('2024-03-18', '2024-04-04', '-1302.90')]
worst session-date loss $-1,894.80 on 2025-04-08 (2 trades that day)
largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 3.922%
largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.307%
largest MAE at 1 MNQ $2,223.00 on 2025-04-08
sessions with >=1 trade 792 | most trades in one session 2 (on 2021-05-06 +17 other dates)
avg trades per session-with-a-trade 1.0227
losers by exit name (count, largest loss MNQ): [('Exit on session close', 328, '-1099.90'), ('XL', 10, '-1960.90'), ('XS', 8, '-907.90')]
SENSITIVITY (...): largest loss $-1,962.90 (2025-04-08) | average loss $-231.94 over 350 losers | worst day $-1,898.80 (2025-04-08)
trades 810 / N 1352 = 0.5991 per session | trade dates not in calendar: 0 []
```
**(d) Fails R3 as tested.** It has no predefined per-trade maximum loss. The opposite-band level is checked at checkpoint closes, filled at market, and in practice reverses or holds to 16:00.

### 3. PraxisNoiseAreaBreakout_Flat1559
**(a)** The exit block is the same as the baseline's (`sed -n 243,258p`: `Math.Max(curUpper, curVwap)` / `ExitLong("XL", "")`, `Math.Min(curLower, curVwap)` / `ExitShort("XS", "")`). The only change is the session flat:
```
$ sed -n 91p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs; sed -n 227p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
			if (mod >= FlattenMod)
```
**Per-trade maximum loss known before entry: NO.** Kind: same as the baseline (band/VWAP trailing level, checkpoint bar close, market exit).

**(b)/(c)/(e)** [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]:
```
trades 1190 | losers (MNQ net < 0) 715 | zero-net 0 | winners 475
largest single loss $-542.40 on 2026-06-25 | average loss $-96.45
[streak] runs of max length 10: 2 -> [('2022-09-15', '2022-09-26', '-815.50'), ('2026-05-11', '2026-05-20', '-1046.00')]
worst session-date loss $-683.70 on 2025-04-16 (3 trades that day)
largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.085%
largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.362%
largest MAE at 1 MNQ $747.50 on 2026-06-25
sessions with >=1 trade 792 | most trades in one session 5 (on 2023-12-04 +2 other dates)
avg trades per session-with-a-trade 1.5025
losers by exit name (count, largest loss MNQ): [('FlatEOD', 68, '-371.90'), ('XL', 284, '-447.40'), ('XS', 363, '-542.40')]
SENSITIVITY (...): largest loss $-544.40 (2026-06-25) | average loss $-97.24 over 724 losers | worst day $-689.70 (2025-04-16)
trades 1190 / N 1352 = 0.8802 per session | trade dates not in calendar: 0 []
```
**(d) Fails R3 as tested.** The reason is the same as the baseline's.

### 4. PraxisLastHalfHourMomentum (retired)
**(a)**
```
$ sed -n 46p ninjascript/PraxisLastHalfHourMomentum.cs; sed -n 205,212p ...; sed -n 230,235p ...
//   * Calculate.OnBarClose, managed orders, market orders only, EntriesPerDirection = 1.
			// ---- Flat on the 15:59 bar (or any later bar) — fills at the 16:00 bar Open (INFERRED). ----
			if (mod >= FlatMod)
			{
				if (Position.MarketPosition == MarketPosition.Long)
					ExitLong("LHFlat1559", "LHMomLong");
				else if (Position.MarketPosition == MarketPosition.Short)
					ExitShort("LHFlat1559", "LHMomShort");
				return;                          // never open a position at/after 15:59
			double r = Close[0] / lastRegularClose - 1.0;   // r_ROD = P(15:30)/P(last 16:00 close) - 1 (Eq. 2, p. 381)
			if (r > 0)
				EnterLong(Contracts, "LHMomLong");          // predictor > 0 -> long (Eq. 12, p. 385)
			else
				EnterShort(Contracts, "LHMomShort");        // "otherwise" (incl. r == 0) -> short (Eq. 12, p. 385)
```
The only exits are the time exit at 15:59 and the `LHStaleFlat` safety exit at :194/:200. There is no price level of any kind. In the data, `exit names: [('LHFlat1559', 1304)]` (`[3]`).
**Per-trade maximum loss known before entry: NO.** Kind: none. Only the holding time is bounded (about 29 minutes).

**(b)/(c)/(e)** [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]:
```
trades 1304 | losers (MNQ net < 0) 694 | zero-net 0 | winners 610
largest single loss $-555.40 on 2025-03-04 | average loss $-71.82
[streak] runs of max length 10: 3 -> [('2023-08-29', '2023-09-12', '-339.50'), ('2025-01-17', '2025-01-31', '-895.00'), ('2025-11-26', '2025-12-11', '-509.00')]
worst session-date loss $-555.40 on 2025-03-04 (1 trades that day)
largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.111%
largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.370%
largest MAE at 1 MNQ $694.00 on 2025-03-04
sessions with >=1 trade 1304 | most trades in one session 1 (on 2021-03-09 +1303 other dates)
avg trades per session-with-a-trade 1.0000
SENSITIVITY (...): largest loss $-557.40 (2025-03-04) | average loss $-72.08 over 711 losers | worst day $-557.40 (2025-03-04)
trades 1304 / N 1352 = 0.9645 per session | trade dates not in calendar: 0 []
```
**(d) Fails R3 as tested.** It has no stop of any kind. Loss is bounded only by the 15:59 time exit.

### 5. Gap fade (search-loop candidate 1, bead vn4, V2; Python pre-screen)
**(a)**
```
$ sed -n 16p research/search-loop/c1-gap-fade/RULES.md; sed -n 19,23p research/search-loop/c1-gap-fade/RULES.md
- Entry fill = O worsened by 0.5 points (2 ticks).
- Target: PC. Hit when a bar (the entry bar included) trades through PC by at least 1 tick: short needs low <= PC - 0.25; long needs high >= PC + 0.25. Exit fill = PC worsened by 0.5 points.
- Stop: distance = |O - PC|. Short stop = O + |O - PC|; long stop = O - |O - PC|. Hit when short high >= stop, long low <= stop. Exit fill = stop worsened by 0.5 points.
- If one bar hits both stop and target: the stop is taken.
- Time exit: if neither is hit, exit at the close of the last RTH bar of the day (normally the 16:00-stamped bar), worsened by 0.5 points.
```
The stop is a price level fixed at entry: entry price O ± the gap |O − PC|. It is tested against each 1-minute bar's high/low, which is how a resting stop would behave. Its size in points is set by the day's gap, so it differs from trade to trade. It is a Python simulation. No NinjaScript exists for it, so it has never been a resting order on any platform. From `[5]`:
```
stop distance |O-PC| points: min 28.75 | median 80.125 | max 234.5
stop distance at 1 MNQ ($2/pt, from O): min $57.50 | median $160.25 | max $469.00
max-distance trade date 2026-07-16; realized stop-out MNQ net would be -((d+1)*2+1.90) = $-472.90
stop trades with points != -(|O-PC| + 1.0): 0 []
any trade losing more than (|O-PC|+1)*2 + 1.90 at MNQ: 0 []
bar-file lookup: 347 exit bars needed, 0 missing
STOP exits whose exit bar OPENED beyond the stop (fill model still books stop+0.5): 0
```
**Per-trade maximum loss known before entry: YES, as specified.** Kind: gap-sized points (price-based). It is known at the moment of entry because O is the entry price, and it varies per trade (28.75–234.5 pt). In this list no trade lost more than (|O−PC| + 1.0 pt) × $2 + $1.90 at MNQ. None of the 286 stop exits had a bar that opened beyond the stop, so the fill model never met a gap-through in this data. That is what this data shows. It is not a test under failure. Whether the size satisfies "a percentage of the account" is not judged here (Q2/Q3).

**(c) Checks** (`[5]`): `mnq_net != points*2 - 1.90: 0`, `points != (exit_fill - entry_fill)*side: 0`, `entry_fill != O worsened 0.5 pt: 0`, `target exit_fill != PC worsened 0.5 pt: 0`, `stop exit_fill != stop worsened 0.5 pt: 0`, `time-exit fill != exit-bar close worsened 0.5 pt: 0` (61 time exits checked against the bar file). The 0.5 pt (2 ticks) per side is therefore inside `points` and is not added again.

**(b)/(e)** [Mac recomputation from the Python pre-screen trade list, MNQ derived]:
```
rows 648 | sides [('long', 295), ('short', 353)] | exit kinds [('stop', 286), ('target', 301), ('time', 61)]
trades 648 | losers (MNQ net < 0) 324 | zero-net 0 | winners 324
largest single loss $-472.90 on 2026-07-16 | average loss $-161.64
[streak] runs of max length 10: 1 -> [('2026-03-11', '2026-04-10', '-1951.50')]
worst session-date loss $-472.90 on 2026-07-16 (1 trades that day)
largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.946%
largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.315%
largest MAE at 1 MNQ $471.00 on 2026-07-16
sessions with >=1 trade 648 | most trades in one session 1 (on 2021-03-16 +647 other dates)
avg trades per session-with-a-trade 1.0000
SENSITIVITY (...): largest loss $-474.90 (2026-07-16) | average loss $-163.64 over 324 losers | worst day $-474.90 (2026-07-16)
trades / summary.json trading_days = 648 / 1354 = 0.4786
```
Entry date and exit date: the list has one `date` column, and RULES.md :22 keeps every exit inside RTH, so they are the same date by construction. The denominator 1354 is summary.json `trading_days`. That count includes 2 weekend-dated days (`weekend_trading_days ['2021-03-28', '2025-03-16']`) and 3 skipped days, so it is not the same basis as the NT8 N = 1352 (Mon–Fri).

V1/V3 per-trade lists (`[6]`): neither the repo nor the parked branch has one. `git ls-tree` of `parked/Praxis_build-vn4` lists only `trades_V2_full.csv`, and summary.json `in_sample` holds V1/V2/V3 aggregates only. Scratch **in-sample-only** lists do exist at `/tmp/praxis-c1/builder_is_trades_V{1,2,3}.csv`. They are written by `screen.py` :457, untracked, mutable, and not hashed in summary.json. For the record only:
```
/tmp/praxis-c1/builder_is_trades_V1.csv sha256 0dae9abe… | rows 456 | dates 2021-03-23..2024-12-31 | largest loss $-227.90 on 2024-11-07 | max |O-PC| 112.00 pt
/tmp/praxis-c1/builder_is_trades_V3.csv sha256 4de91f64… | rows 360 | dates 2021-03-15..2024-12-31 | largest loss $-133.90 on 2024-11-18 | max |O-PC| 65.00 pt
```
The per-trade figures above are V2 full-period only.

**(d) Meets R3's structure, size undecided.** Each trade has a price stop fixed at entry, and in this list no loss exceeded it. The size is gap-dependent (up to 234.5 pt, $472.90 realized at 1 MNQ), and it is a pre-screen simulation, not a platform order.

## Headline table (1 MNQ)
From `[7]`. NT8 rows: [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]. Gap fade: [Mac recomputation from the Python pre-screen trade list, MNQ derived].
```
  strategy                                         |    largest | longest losing streak              | worst day                | max trades/session
  PraxisNoiseAreaBreakout (baseline BandOrVWAP)    |   $-542.40 | 10 (2022-09-15..2022-09-26) $-802.00 | $-705.10 2022-10-13      | 5
  PraxisNoiseAreaBreakout_OppBand                  | $-1,960.90 | 6 (2021-11-17..2021-11-24) $-1,429.40 | $-1,894.80 2025-04-08    | 2
  PraxisNoiseAreaBreakout_Flat1559                 |   $-542.40 | 10 (2022-09-15..2022-09-26) $-815.50 | $-683.70 2025-04-16      | 5
  PraxisLastHalfHourMomentum (retired)             |   $-555.40 | 10 (2023-08-29..2023-09-12) $-339.50 | $-555.40 2025-03-04      | 1
  Gap fade V2 (pre-screen)                         |   $-472.90 | 10 (2026-03-11..2026-04-10) $-1,951.50 | $-472.90 2026-07-16      | 1
```
The streak column shows the first maximal run in trade order. Ties are listed per strategy above.

| strategy | per-trade max loss known before entry | (d) proposal |
|---|---|---|
| NoiseArea baseline | NO (band/VWAP trailing level, 30-min bar-close market exit) | Fails R3 as tested |
| NoiseArea OppBand | NO (opposite-band level, 30-min bar-close market exit) | Fails R3 as tested |
| NoiseArea Flat1559 | NO (as baseline) | Fails R3 as tested |
| LastHalfHourMomentum | NO (none; time exit only) | Fails R3 as tested |
| Gap fade V2 | YES as specified (gap-sized points, simulated stop) | Meets R3's structure, size undecided |

## Limits
- Every figure is a recomputation from trade lists. None comes from an MNQ run, none was tested under failure (server crash, gap-through, rejected order), and none was compiled. MNQ = NQ gross / 10 − $1.90 is a derived figure. That it equals an own MNQ run is not verified.
- The NT8 MAE column is NT8's own figure, untimed, and its method is UNVERIFIED (D6 :54, quoted in RULES.md :50). The gap-fade `mae_points` comes from the pre-screen's bars and was not recomputed here.
- The percentages of $50,000 and $150,000 are illustrations only. R3's percentage is undecided (Amear's Q2/Q3). Nothing here proposes a figure.
- "Worst day" groups trades by entry date, which equals exit date on every row checked. It is a closed-trade sum, not intraday equity.
- The gap-through check covers only the 286 stop exits in this data. It shows the fill model was never stressed. It does not show that a live stop would fill at the level.
- The brief's citation :26-:29 for the sha256 table is off by three lines (the rows are :29-:32). The brief's `grep -o 'Fees: apply[^.]*'` truncates at "$4" and does not show the $1.90. Both are corrected above with pasted output.
- A whole-disk `find / -name 'trades_V*' -not -path '*/System/*'` finished after the report was first written (background task, exit 0). It found exactly two files, both `trades_V2_full.csv` and both with the same sha256 `6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045`: `/private/tmp/praxis-c1-audit/rerun/out/trades_V2_full.csv` and `research/search-loop/c1-gap-fade/out/trades_V2_full.csv`. No full-period V1 or V3 per-trade list exists on this disk. The in-sample scratch files `/tmp/praxis-c1/builder_is_trades_V*.csv` do not match that pattern. They were found by `ls` instead.
- No tracked file was edited, nothing was staged, nothing was committed. Files written: `/tmp/praxis-r3/w1_r3.py`, `/tmp/praxis-r3/w1_out.txt`, `/tmp/praxis-r3/w1_shell.txt`, and this report (untracked).

## Files staged
None (read-only unit; the report is left untracked as briefed).

## Result: PASS (facts produced; the (d) lines are proposals for the manager to check)

## Script output
### /tmp/praxis-r3/w1_out.txt (in full)
```
w1_r3.py run 2026-11-14T15:16:24Z python 3.14.7 flags isolated=1 dont_write_bytecode=True

=== [1] sha256 of committed grid CSVs vs docs/reports/2026-11-01-three-strategy-results.md :29-:32 (brief cited :26-:29; the table rows sit at :29-:32)
  report :29  07-10 AM  421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd
  report :30  07-57 AM  4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8
  report :31  07-59 AM  5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0
  report :32  08-00 AM  4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9
  2026-11-01-ninjatrader-grid-0710am.csv           421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  07-10 AM  match=True
  2026-11-01-ninjatrader-grid-0757am.csv           4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  07-57 AM  match=True
  2026-11-01-ninjatrader-grid-0759am.csv           5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  07-59 AM  match=True
  2026-11-01-ninjatrader-grid-0800am.csv           4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  08-00 AM  match=True

=== [2] quoted lines
  DECISIONS.md :1063 grep -o 'Fees: apply[^.]*' -> ["Fees: apply MFFU's published round trip — NQ $4"]
  DECISIONS.md :1063 'Fees: apply' + 60 chars -> ["Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new "]
  results report :51 -> - **Entry fill pattern** (OBSERVED): in baseline and Flat1559, every entry fill equals `clamp(open of the entry-stamped bar + 0.50 adverse, bar low, bar high)`: 1190 match / 0 no-match in each [K12, Item 1d]. Across all four CSVs (1190 + 810 + 1190 + 1304 entries [K03]), the adverse residual against that bar's OPEN is 0.50 on 4304, 0.25 on 78, 0.00 on 72 and -0.00 on 40 [K13]. Every fill with less
  results report :77 -> Max DD here is closed-trade cumulative net. Method (i) takes the peak from 0 and method (ii) the peak from the first trade, and the two give identical values. Baseline commission: 0 rows != $2.96; sum $3522.40 == 1190 x 2.96 [K03 `[4]`]. Baseline session-close exits fill at the CLOSE of the 16:00-stamped bar +/- 2 ticks: clamp model 423 of 423 [K12] (OBSERVED).
  results report :253 -> - **Baseline session-close comparison** [K12] (OBSERVED): the baseline's 423 16:00-stamped `Exit on session close` fills match `clamp(16:00 CLOSE -/+ 0.5 adverse, L, H)` on **423 of 423**, and the same rule on the 16:00 OPEN on 5 of 423.

=== [3] NT8 grid trade lists, 1 NQ per row

--- PraxisNoiseAreaBreakout (baseline BandOrVWAP)  (2026-11-01-ninjatrader-grid-0710am.csv)
  rows 1190 (expected 1190) | Qty values [('1', 1190)] | Market pos. [('Long', 556), ('Short', 634)] | Strategy ['PraxisNoiseAreaBreakout']
  Trade number strictly 1..N in file order: True
  Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []
  money fields in parentheses format: 0 | Profit fields with leading '-': 706
  trades with entry date != exit date: 0
  exit names: [('Exit on session close', 429), ('XL', 332), ('XS', 429)]
  losers by exit name (count, largest loss MNQ): [('Exit on session close', 65, '-359.90'), ('XL', 284, '-447.40'), ('XS', 363, '-542.40')]
  WORKED TRADE (first losing row of baseline):
    raw: {'Trade number': '1', 'Market pos.': 'Short', 'Qty': '1', 'Entry price': '16270.25', 'Exit price': '16297.25', 'Entry time': '2021-03-29 10:01:00 AM', 'Exit time': '2021-03-29 11:31:00 AM', 'Exit name': 'XS', 'Profit': '-$542.96', 'Commission': '$2.96', 'MAE': '$1050.00'}
    points = (16297.25 - 16270.25) x -1 = -27.00
    NQ gross = Profit + Commission = -542.96 + 2.96 = -540.00  (= points x 20 = -540.00)
    MNQ net = NQ gross / 10 - 1.90 = -540.00 / 10 - 1.90 = -55.90
    MAE at 1 MNQ = 1050.00 / 10 = 105.00
  first entry date 2021-03-29, last entry date 2026-07-15
    [streak] runs of max length 10: 2 -> [('2022-09-15', '2022-09-26', '-802.00'), ('2026-05-11', '2026-05-20', '-1070.50')]
  MNQ figures [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]
    trades 1190 | losers (MNQ net < 0) 712 | zero-net 0 | winners 478
    largest single loss $-542.40 on 2026-06-25 | average loss $-97.26
    longest losing streak 10 trades, 2022-09-15 .. 2022-09-26, summed $-802.00 (first in trade order; ties listed in [streak])
    worst session-date loss $-705.10 on 2022-10-13 (4 trades that day)
    largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.085%
    largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.362%
    largest MAE at 1 MNQ $747.50 on 2026-06-25
    sessions with >=1 trade 792 | most trades in one session 5 (on 2023-12-04 +2 other dates)
    avg trades per session-with-a-trade 1.5025
    trades-per-session distribution [(1, 499), (2, 209), (3, 66), (4, 15), (5, 3)]
    SENSITIVITY (further $2.00/trade subtracted = double-count case, NOT the base figure): largest loss $-544.40 (2026-06-25) | average loss $-98.03 over 721 losers | worst day $-713.10 (2022-10-13)

--- PraxisNoiseAreaBreakout_OppBand  (2026-11-01-ninjatrader-grid-0757am.csv)
  rows 810 (expected 810) | Qty values [('1', 810)] | Market pos. [('Long', 404), ('Short', 406)] | Strategy ['PraxisNoiseAreaBreakout_OppBand']
  Trade number strictly 1..N in file order: True
  Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []
  money fields in parentheses format: 0 | Profit fields with leading '-': 340
  trades with entry date != exit date: 0
  exit names: [('Exit on session close', 792), ('XL', 10), ('XS', 8)]
  losers by exit name (count, largest loss MNQ): [('Exit on session close', 328, '-1099.90'), ('XL', 10, '-1960.90'), ('XS', 8, '-907.90')]
  first entry date 2021-03-29, last entry date 2026-07-15
    [streak] runs of max length 6: 2 -> [('2021-11-17', '2021-11-24', '-1429.40'), ('2024-03-18', '2024-04-04', '-1302.90')]
  MNQ figures [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]
    trades 810 | losers (MNQ net < 0) 346 | zero-net 0 | winners 464
    largest single loss $-1,960.90 on 2025-04-08 | average loss $-232.61
    longest losing streak 6 trades, 2021-11-17 .. 2021-11-24, summed $-1,429.40 (first in trade order; ties listed in [streak])
    worst session-date loss $-1,894.80 on 2025-04-08 (2 trades that day)
    largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 3.922%
    largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.307%
    largest MAE at 1 MNQ $2,223.00 on 2025-04-08
    sessions with >=1 trade 792 | most trades in one session 2 (on 2021-05-06 +17 other dates)
    avg trades per session-with-a-trade 1.0227
    trades-per-session distribution [(1, 774), (2, 18)]
    SENSITIVITY (further $2.00/trade subtracted = double-count case, NOT the base figure): largest loss $-1,962.90 (2025-04-08) | average loss $-231.94 over 350 losers | worst day $-1,898.80 (2025-04-08)

--- PraxisNoiseAreaBreakout_Flat1559  (2026-11-01-ninjatrader-grid-0759am.csv)
  rows 1190 (expected 1190) | Qty values [('1', 1190)] | Market pos. [('Long', 556), ('Short', 634)] | Strategy ['PraxisNoiseAreaBreakout_Flat1559']
  Trade number strictly 1..N in file order: True
  Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []
  money fields in parentheses format: 0 | Profit fields with leading '-': 708
  trades with entry date != exit date: 0
  exit names: [('Exit on session close', 6), ('FlatEOD', 423), ('XL', 332), ('XS', 429)]
  losers by exit name (count, largest loss MNQ): [('FlatEOD', 68, '-371.90'), ('XL', 284, '-447.40'), ('XS', 363, '-542.40')]
  first entry date 2021-03-29, last entry date 2026-07-15
    [streak] runs of max length 10: 2 -> [('2022-09-15', '2022-09-26', '-815.50'), ('2026-05-11', '2026-05-20', '-1046.00')]
  MNQ figures [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]
    trades 1190 | losers (MNQ net < 0) 715 | zero-net 0 | winners 475
    largest single loss $-542.40 on 2026-06-25 | average loss $-96.45
    longest losing streak 10 trades, 2022-09-15 .. 2022-09-26, summed $-815.50 (first in trade order; ties listed in [streak])
    worst session-date loss $-683.70 on 2025-04-16 (3 trades that day)
    largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.085%
    largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.362%
    largest MAE at 1 MNQ $747.50 on 2026-06-25
    sessions with >=1 trade 792 | most trades in one session 5 (on 2023-12-04 +2 other dates)
    avg trades per session-with-a-trade 1.5025
    trades-per-session distribution [(1, 499), (2, 209), (3, 66), (4, 15), (5, 3)]
    SENSITIVITY (further $2.00/trade subtracted = double-count case, NOT the base figure): largest loss $-544.40 (2026-06-25) | average loss $-97.24 over 724 losers | worst day $-689.70 (2025-04-16)

--- PraxisLastHalfHourMomentum (retired)  (2026-11-01-ninjatrader-grid-0800am.csv)
  rows 1304 (expected 1304) | Qty values [('1', 1304)] | Market pos. [('Long', 698), ('Short', 606)] | Strategy ['PraxisLastHalfHourMomentum']
  Trade number strictly 1..N in file order: True
  Commission != $2.96: 0 rows | Profit != round((exit-entry)*side*20 - 2.96, 2): 0 rows []
  money fields in parentheses format: 0 | Profit fields with leading '-': 683
  trades with entry date != exit date: 0
  exit names: [('LHFlat1559', 1304)]
  losers by exit name (count, largest loss MNQ): [('LHFlat1559', 694, '-555.40')]
  first entry date 2021-03-09, last entry date 2026-07-17
    [streak] runs of max length 10: 3 -> [('2023-08-29', '2023-09-12', '-339.50'), ('2025-01-17', '2025-01-31', '-895.00'), ('2025-11-26', '2025-12-11', '-509.00')]
  MNQ figures [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]
    trades 1304 | losers (MNQ net < 0) 694 | zero-net 0 | winners 610
    largest single loss $-555.40 on 2025-03-04 | average loss $-71.82
    longest losing streak 10 trades, 2023-08-29 .. 2023-09-12, summed $-339.50 (first in trade order; ties listed in [streak])
    worst session-date loss $-555.40 on 2025-03-04 (1 trades that day)
    largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 1.111%
    largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.370%
    largest MAE at 1 MNQ $694.00 on 2025-03-04
    sessions with >=1 trade 1304 | most trades in one session 1 (on 2021-03-09 +1303 other dates)
    avg trades per session-with-a-trade 1.0000
    trades-per-session distribution [(1, 1304)]
    SENSITIVITY (further $2.00/trade subtracted = double-count case, NOT the base figure): largest loss $-557.40 (2025-03-04) | average loss $-72.08 over 711 losers | worst day $-557.40 (2025-03-04)

=== [4] session denominator, scripts/wf/sessions.py build_calendar (read-only, bytecode off)
  sessions.py sha256 9ee58ef9412b7d2c5f0ec397fc690fe882933db5644d1dd32c0609cab2dcea28 | bar file sha256 307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454
  N = 1352, first 2021-03-08, last 2026-07-17, keys ['K', 'N', 'cscv_S', 'cscv_block', 'cscv_rows', 'dropped', 'dropped_dates', 'oos_sessions', 'rule', 'schema', 'sessions', 'source', 'weekend_dates_dropped', 'windows']
  PraxisNoiseAreaBreakout (baseline BandOrVWAP)    trades 1190 / N 1352 = 0.8802 per session | trade dates not in calendar: 0 []
  PraxisNoiseAreaBreakout_OppBand                  trades 810 / N 1352 = 0.5991 per session | trade dates not in calendar: 0 []
  PraxisNoiseAreaBreakout_Flat1559                 trades 1190 / N 1352 = 0.8802 per session | trade dates not in calendar: 0 []
  PraxisLastHalfHourMomentum (retired)             trades 1304 / N 1352 = 0.9645 per session | trade dates not in calendar: 0 []
  __pycache__ present in scripts/wf after import: False

=== [5] Gap fade V2 (Python pre-screen), research/search-loop/c1-gap-fade/out/trades_V2_full.csv
  trades_V2_full.csv sha256 6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045 | summary.json sha256 71cd073391018c4a27b783547a8df4143f9948eea77ceb064d57bf2619c9a9a8
  summary.json kind 'PRE-SCREEN (not validated)' | trading_days 1354 | skipped_days [['2021-03-08', 'first trading day (no previous)'], ['2021-09-27', 'previous trading day 2021-09-09 is 18 days back'], ['2026-01-02', 'previous trading day 2025-12-12 is 21 days back']] | weekend_trading_days ['2021-03-28', '2025-03-16']
  summary.json top-level keys: ['unit', 'bead', 'kind', 'standing_limitation', 'run_timestamp_utc', 'inputs', 'pf_definition', 'trading_days', 'skipped_days', 'weekend_trading_days', 'in_sample', 'selection', 'selected_holdout', 'selected_full', 'd6', 'sanity_dd_100_m300_50_m100']
    in_sample -> variants ['V1', 'V2', 'V3']
  rows 648 | sides [('long', 295), ('short', 353)] | exit kinds [('stop', 286), ('target', 301), ('time', 61)]
  mnq_net != points*2 - 1.90: 0 []
  points != (exit_fill - entry_fill)*side: 0 []
  entry_fill != O worsened 0.5 pt: 0 []
  target exit_fill != PC worsened 0.5 pt: 0 []
  stop exit_fill != stop worsened 0.5 pt: 0 []
  stop trades with points != -(|O-PC| + 1.0): 0 []
  any trade losing more than (|O-PC|+1)*2 + 1.90 at MNQ: 0 []
  trades with date != exit date: 0 by construction (one 'date' column; exits within RTH per RULES.md :22)
  stop distance |O-PC| points: min 28.75 | median 80.125 | max 234.5
  stop distance at 1 MNQ ($2/pt, from O): min $57.50 | median $160.25 | max $469.00
  max-distance trade date 2026-07-16; realized stop-out MNQ net would be -((d+1)*2+1.90) = $-472.90
  bar-file lookup: 347 exit bars needed, 0 missing
  time-exit fill != exit-bar close worsened 0.5 pt: 0 []
  STOP exits whose exit bar OPENED beyond the stop (fill model still books stop+0.5): 0
    [streak] runs of max length 10: 1 -> [('2026-03-11', '2026-04-10', '-1951.50')]
  MNQ figures [Mac recomputation from the Python pre-screen trade list, MNQ derived]
    trades 648 | losers (MNQ net < 0) 324 | zero-net 0 | winners 324
    largest single loss $-472.90 on 2026-07-16 | average loss $-161.64
    longest losing streak 10 trades, 2026-03-11 .. 2026-04-10, summed $-1,951.50 (first in trade order; ties listed in [streak])
    worst session-date loss $-472.90 on 2026-07-16 (1 trades that day)
    largest single loss as % of $50,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.946%
    largest single loss as % of $150,000.00 (ILLUSTRATION ONLY, R3 percentage undecided): 0.315%
    largest MAE at 1 MNQ $471.00 on 2026-07-16
    sessions with >=1 trade 648 | most trades in one session 1 (on 2021-03-16 +647 other dates)
    avg trades per session-with-a-trade 1.0000
    trades-per-session distribution [(1, 648)]
    SENSITIVITY (further $2.00/trade subtracted = double-count case, NOT the base figure): largest loss $-474.90 (2026-07-16) | average loss $-163.64 over 324 losers | worst day $-474.90 (2026-07-16)
  trades / summary.json trading_days = 648 / 1354 = 0.4786

=== [6] V1/V3 per-trade lists
  /tmp/praxis-c1/builder_is_trades_V1.csv sha256 0dae9abe991cd78ef64ba507b55fd845bd3e9dda1f380151da8cd56d9e60cb00 | rows 456 | dates 2021-03-23..2024-12-31 | largest loss $-227.90 on 2024-11-07 | max |O-PC| 112.00 pt | IN-SAMPLE SCRATCH, untracked /tmp, not hashed in summary.json
  /tmp/praxis-c1/builder_is_trades_V2.csv sha256 985d5ec343053bbd8bdfd9b4b083b75168edf9e570b633c93c16fefd1287928e | rows 488 | dates 2021-03-16..2024-12-27 | largest loss $-366.40 on 2024-12-11 | max |O-PC| 181.25 pt | IN-SAMPLE SCRATCH, untracked /tmp, not hashed in summary.json
  /tmp/praxis-c1/builder_is_trades_V3.csv sha256 4de91f644bcac811d73b8ad50e0aaecc3651dd2299a44334035bf19ddb580a75 | rows 360 | dates 2021-03-15..2024-12-31 | largest loss $-133.90 on 2024-11-18 | max |O-PC| 65.00 pt | IN-SAMPLE SCRATCH, untracked /tmp, not hashed in summary.json

=== [7] headline table (1 MNQ; NT8 rows [Mac recomputation from the hand-run trade list, MNQ derived, not an MNQ run]; gap fade [Mac recomputation from the Python pre-screen trade list, MNQ derived])
  strategy                                         |    largest | longest losing streak              | worst day                | max trades/session
  PraxisNoiseAreaBreakout (baseline BandOrVWAP)    |   $-542.40 | 10 (2022-09-15..2022-09-26) $-802.00 | $-705.10 2022-10-13      | 5
  PraxisNoiseAreaBreakout_OppBand                  | $-1,960.90 | 6 (2021-11-17..2021-11-24) $-1,429.40 | $-1,894.80 2025-04-08    | 2
  PraxisNoiseAreaBreakout_Flat1559                 |   $-542.40 | 10 (2022-09-15..2022-09-26) $-815.50 | $-683.70 2025-04-16      | 5
  PraxisLastHalfHourMomentum (retired)             |   $-555.40 | 10 (2023-08-29..2023-09-12) $-339.50 | $-555.40 2025-03-04      | 1
  Gap fade V2 (pre-screen)                         |   $-472.90 | 10 (2026-03-11..2026-04-10) $-1,951.50 | $-472.90 2026-07-16      | 1

end
```

### /tmp/praxis-r3/w1_shell.txt (in full)
```
$ git rev-parse --short HEAD
244cfc3
[exit 0]

$ shasum -a 256 docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv research/search-loop/c1-gap-fade/RULES.md research/search-loop/c1-gap-fade/out/trades_V2_full.csv research/search-loop/c1-gap-fade/out/summary.json
421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd  docs/reports/evidence/2026-11-01-ninjatrader-grid-0710am.csv
4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8  docs/reports/evidence/2026-11-01-ninjatrader-grid-0757am.csv
5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0  docs/reports/evidence/2026-11-01-ninjatrader-grid-0759am.csv
4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9  docs/reports/evidence/2026-11-01-ninjatrader-grid-0800am.csv
f892a265c99079365544a31c2f0fa85a6dff68ba72bfb450ffca391d4a774ba3  research/search-loop/c1-gap-fade/RULES.md
6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045  research/search-loop/c1-gap-fade/out/trades_V2_full.csv
71cd073391018c4a27b783547a8df4143f9948eea77ceb064d57bf2619c9a9a8  research/search-loop/c1-gap-fade/out/summary.json
[exit 0]

$ sed -n 29,32p docs/reports/2026-11-01-three-strategy-results.md
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-10 AM.csv` | baseline grid | `421c44e6cd9d417b432be1a5b440b0861782a3bba7e1961beba5b5421e0534bd` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-57 AM.csv` | OppBand grid | `4207ea99e7f1187b54ebe45c97822409629192ed12e7ee0dbaacb241c152b6e8` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 07-59 AM.csv` | Flat1559 grid | `5a3c4d783a44b33a18c4eb77f50444af1d4cf65ed4190038becc4c2007c868e0` |
| `/Users/admin/Desktop/NinjaTrader Grid 2026-11-01 08-00 AM.csv` | LastHalfHourMomentum grid | `4efd8ce8e95cc408f82d494fcf55238c25b9980b030a39eb25f4eaa5fbd180d9` |
[exit 0]

$ sed -n 1063p DECISIONS.md | grep -o 'Fees: apply[^.]*'
Fees: apply MFFU's published round trip — NQ $4
[exit 0]

$ sed -n 1063p DECISIONS.md | grep -o 'MNQ $1.90'
MNQ $1.90
[exit 0]

$ sed -n 51p docs/reports/2026-11-01-three-strategy-results.md
- **Entry fill pattern** (OBSERVED): in baseline and Flat1559, every entry fill equals `clamp(open of the entry-stamped bar + 0.50 adverse, bar low, bar high)`: 1190 match / 0 no-match in each [K12, Item 1d]. Across all four CSVs (1190 + 810 + 1190 + 1304 entries [K03]), the adverse residual against that bar's OPEN is 0.50 on 4304, 0.25 on 78, 0.00 on 72 and -0.00 on 40 [K13]. Every fill with less than 0.50 adverse slip equals the bar's adverse extreme [K14]. Every LastHalfHourMomentum fill that is not open +/- 2 ticks (218 of entries + exits) equals the bar high for a buy or the bar low for a sell [K15]. Plain words: in this data, slippage is 2 ticks adverse from the bar open, clipped to the bar's range. No claim is made about how NT8 implements that.
[exit 0]

$ git status --short research/search-loop/c1-gap-fade/; git show parked/Praxis_build-vn4:research/search-loop/c1-gap-fade/RULES.md | diff - research/search-loop/c1-gap-fade/RULES.md; echo diff_exit=$?
?? research/search-loop/c1-gap-fade/
diff_exit=0
[exit 0]

$ sed -n 16p research/search-loop/c1-gap-fade/RULES.md; sed -n 19,23p research/search-loop/c1-gap-fade/RULES.md
- Entry fill = O worsened by 0.5 points (2 ticks).
- Target: PC. Hit when a bar (the entry bar included) trades through PC by at least 1 tick: short needs low <= PC - 0.25; long needs high >= PC + 0.25. Exit fill = PC worsened by 0.5 points.
- Stop: distance = |O - PC|. Short stop = O + |O - PC|; long stop = O - |O - PC|. Hit when short high >= stop, long low <= stop. Exit fill = stop worsened by 0.5 points.
- If one bar hits both stop and target: the stop is taken.
- Time exit: if neither is hit, exit at the close of the last RTH bar of the day (normally the 16:00-stamped bar), worsened by 0.5 points.
- At most one trade per day. No other filter.
[exit 0]

$ cd ninjascript; for f in PraxisNoiseAreaBreakout.cs PraxisNoiseAreaBreakout_OppBand.cs PraxisNoiseAreaBreakout_Flat1559.cs PraxisLastHalfHourMomentum.cs; do for p in SetStopLoss SetProfitTarget SetTrailStop EnterLongStopMarket EnterShortStopMarket ExitLongStopMarket ExitShortStopMarket StopMarket; do printf "%s %s: " $f $p; grep -c $p $f; done; done
PraxisNoiseAreaBreakout.cs SetStopLoss: 0
PraxisNoiseAreaBreakout.cs SetProfitTarget: 0
PraxisNoiseAreaBreakout.cs SetTrailStop: 0
PraxisNoiseAreaBreakout.cs EnterLongStopMarket: 0
PraxisNoiseAreaBreakout.cs EnterShortStopMarket: 0
PraxisNoiseAreaBreakout.cs ExitLongStopMarket: 0
PraxisNoiseAreaBreakout.cs ExitShortStopMarket: 0
PraxisNoiseAreaBreakout.cs StopMarket: 0
PraxisNoiseAreaBreakout_OppBand.cs SetStopLoss: 0
PraxisNoiseAreaBreakout_OppBand.cs SetProfitTarget: 0
PraxisNoiseAreaBreakout_OppBand.cs SetTrailStop: 0
PraxisNoiseAreaBreakout_OppBand.cs EnterLongStopMarket: 0
PraxisNoiseAreaBreakout_OppBand.cs EnterShortStopMarket: 0
PraxisNoiseAreaBreakout_OppBand.cs ExitLongStopMarket: 0
PraxisNoiseAreaBreakout_OppBand.cs ExitShortStopMarket: 0
PraxisNoiseAreaBreakout_OppBand.cs StopMarket: 0
PraxisNoiseAreaBreakout_Flat1559.cs SetStopLoss: 0
PraxisNoiseAreaBreakout_Flat1559.cs SetProfitTarget: 0
PraxisNoiseAreaBreakout_Flat1559.cs SetTrailStop: 0
PraxisNoiseAreaBreakout_Flat1559.cs EnterLongStopMarket: 0
PraxisNoiseAreaBreakout_Flat1559.cs EnterShortStopMarket: 0
PraxisNoiseAreaBreakout_Flat1559.cs ExitLongStopMarket: 0
PraxisNoiseAreaBreakout_Flat1559.cs ExitShortStopMarket: 0
PraxisNoiseAreaBreakout_Flat1559.cs StopMarket: 0
PraxisLastHalfHourMomentum.cs SetStopLoss: 0
PraxisLastHalfHourMomentum.cs SetProfitTarget: 0
PraxisLastHalfHourMomentum.cs SetTrailStop: 0
PraxisLastHalfHourMomentum.cs EnterLongStopMarket: 0
PraxisLastHalfHourMomentum.cs EnterShortStopMarket: 0
PraxisLastHalfHourMomentum.cs ExitLongStopMarket: 0
PraxisLastHalfHourMomentum.cs ExitShortStopMarket: 0
PraxisLastHalfHourMomentum.cs StopMarket: 0
[exit 1]

$ cd ninjascript; grep -nE "Calculate +=|IsExitOnSessionCloseStrategy +=|ExitMode +=" PraxisNoiseAreaBreakout.cs PraxisNoiseAreaBreakout_OppBand.cs PraxisNoiseAreaBreakout_Flat1559.cs PraxisLastHalfHourMomentum.cs
PraxisNoiseAreaBreakout.cs:105:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout.cs:108:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
PraxisNoiseAreaBreakout.cs:118:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
PraxisNoiseAreaBreakout.cs:208:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisNoiseAreaBreakout.cs:216:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisNoiseAreaBreakout_OppBand.cs:29:// DEFAULT ExitMode = OppBand in this variant, so the mode under test runs without re-setting an input.
PraxisNoiseAreaBreakout_OppBand.cs:35://   The OppBand fallback in the ternary is mode-guarded, so only ExitMode == OppBand takes the opposite band.
PraxisNoiseAreaBreakout_OppBand.cs:128:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout_OppBand.cs:131:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
PraxisNoiseAreaBreakout_OppBand.cs:141:				ExitMode      = PraxisNoiseExitMode.OppBand;    // VARIANT 7zq default (base default BandOrVWAP, spec §4 p.13). The only knob.
PraxisNoiseAreaBreakout_OppBand.cs:232:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisNoiseAreaBreakout_OppBand.cs:233:					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
PraxisNoiseAreaBreakout_OppBand.cs:240:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisNoiseAreaBreakout_OppBand.cs:241:					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
PraxisNoiseAreaBreakout_Flat1559.cs:44:// IsExitOnSessionCloseStrategy = true is kept as the backstop.
PraxisNoiseAreaBreakout_Flat1559.cs:138:				Calculate                                 = Calculate.OnBarClose;
PraxisNoiseAreaBreakout_Flat1559.cs:141:				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit flat (submitted 15:59) is primary
PraxisNoiseAreaBreakout_Flat1559.cs:151:				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
PraxisNoiseAreaBreakout_Flat1559.cs:246:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisNoiseAreaBreakout_Flat1559.cs:254:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
PraxisLastHalfHourMomentum.cs:58://   * IsExitOnSessionCloseStrategy = true is a BACKSTOP only (ExitOnSessionCloseSeconds = 30, as the base).
PraxisLastHalfHourMomentum.cs:145:				Calculate                                 = Calculate.OnBarClose;
PraxisLastHalfHourMomentum.cs:148:				IsExitOnSessionCloseStrategy              = true;   // BACKSTOP only; the explicit 15:59 flat is primary
[exit 0]

$ sed -n 196,221p ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

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

[exit 0]

$ sed -n 188,192p ninjascript/PraxisNoiseAreaBreakout.cs
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
[exit 0]

$ sed -n 229,244p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop: BandOrVWAP = max(UpperBound, VWAP) (spec §4 p.13); OppBand = LowerBound, the OPPOSITE band (paper Table 1; 3gm R14).
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop: BandOrVWAP = min(LowerBound, VWAP) (spec §4 p.13); OppBand = UpperBound, the OPPOSITE band (paper Table 1; 3gm R14).
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
				if (price >= stop)
					ExitShort("XS", "");
			}
[exit 0]

$ sed -n 30,33p ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
// CONSEQUENCE (3gm Q2): with the opposite band, the OppBand exit condition (long: Close <= LowerBound;
//   short: Close >= UpperBound) coincides with the reversal trigger (Close < LowerBound /
//   Close > UpperBound). OppBand therefore becomes "reverse or hold to 16:00". A flat-only exit
//   happens only at exact equality, Close == band (INFERRED, not run).
[exit 0]

$ sed -n 243,258p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs; sed -n 228,231p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
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
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}
[exit 0]

$ sed -n 46p ninjascript/PraxisLastHalfHourMomentum.cs; sed -n 205,212p ninjascript/PraxisLastHalfHourMomentum.cs; sed -n 230,235p ninjascript/PraxisLastHalfHourMomentum.cs
//   * Calculate.OnBarClose, managed orders, market orders only, EntriesPerDirection = 1.
			// ---- Flat on the 15:59 bar (or any later bar) — fills at the 16:00 bar Open (INFERRED). ----
			if (mod >= FlatMod)
			{
				if (Position.MarketPosition == MarketPosition.Long)
					ExitLong("LHFlat1559", "LHMomLong");
				else if (Position.MarketPosition == MarketPosition.Short)
					ExitShort("LHFlat1559", "LHMomShort");
				return;                          // never open a position at/after 15:59

			double r = Close[0] / lastRegularClose - 1.0;   // r_ROD = P(15:30)/P(last 16:00 close) - 1 (Eq. 2, p. 381)
			if (r > 0)
				EnterLong(Contracts, "LHMomLong");          // predictor > 0 -> long (Eq. 12, p. 385)
			else
				EnterShort(Contracts, "LHMomShort");        // "otherwise" (incl. r == 0) -> short (Eq. 12, p. 385)
[exit 0]

$ ls /tmp/praxis-c1/builder_is_trades_V*.csv; git ls-files research/search-loop | wc -l; git ls-tree -r --name-only parked/Praxis_build-vn4 -- research/search-loop/c1-gap-fade
/tmp/praxis-c1/builder_is_trades_V1.csv
/tmp/praxis-c1/builder_is_trades_V2.csv
/tmp/praxis-c1/builder_is_trades_V3.csv
       0
research/search-loop/c1-gap-fade/D-2026-11-14-A.entry.md
research/search-loop/c1-gap-fade/RULES.md
research/search-loop/c1-gap-fade/out/summary.json
research/search-loop/c1-gap-fade/out/trades_V2_full.csv
research/search-loop/c1-gap-fade/screen.py
[exit 0]

$ ls scripts/wf/__pycache__
ls: scripts/wf/__pycache__: No such file or directory
[exit 1]

$ shasum -a 256 /tmp/praxis-r3/w1_r3.py /tmp/praxis-r3/w1_out.txt
8a8251cb838da1f501236f0b4bfb819f38b6f2efd8a4091acbc397c470a45a0c  /tmp/praxis-r3/w1_r3.py
6138d4c363bc6188fc926e51cc04b4ed9a7869c7e06d8383d5d6ad47f77acf5e  /tmp/praxis-r3/w1_out.txt
[exit 0]

$ sed -n 91p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs; sed -n 227p ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
			if (mod >= FlattenMod)
[exit 0]

```

### Late evidence: whole-disk find (background task budwtvhzz, exit 0)
```
$ grep -n trades_V <task output>
20:/private/tmp/praxis-c1-audit/rerun/out/trades_V2_full.csv
21:/Volumes/Sensidine/Praxis.build/research/search-loop/c1-gap-fade/out/trades_V2_full.csv
$ shasum -a 256 /private/tmp/praxis-c1-audit/rerun/out/trades_V2_full.csv research/search-loop/c1-gap-fade/out/trades_V2_full.csv
6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045  /private/tmp/praxis-c1-audit/rerun/out/trades_V2_full.csv
6d07b2454eba2bfcdfc059dcf75737256d50cbcbfd76d933e80a2c4d69352045  research/search-loop/c1-gap-fade/out/trades_V2_full.csv
```
