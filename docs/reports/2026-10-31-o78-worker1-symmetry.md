# o78 worker 1: long-vs-short symmetry read of `PraxisNoiseAreaBreakout.cs`

## Task
Unit `Praxis_build-o78`, worker 1. Read the code for long-vs-short symmetry. Then give hypotheses, each with a falsifier, for why run 4's shorts lost (−$1,404.56 on 627 trades) while longs won (+$4,541.40 on 584). This is not a fidelity re-check.

## Mode
BUILD, read-only research. This report is the only file written. Nothing is staged by me, and nothing is committed.

## Criterion
- `specs/SPEC_RUBRIC.md:107` S1: every claim has pasted command output.
- `:108` S2: nothing is reported at a higher evidence level than it has.
- `:114` S8: no question that belongs to Amear is answered for him.

```
$ grep -n -E "^\| *S(1|2|8) |..." specs/SPEC_RUBRIC.md
107:| S1 | Every claim in a report has pasted command output, not a description of output. |
108:| S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure. |
114:| S8 | No question that belongs to Amear is answered on his behalf. |
```

## Process log
1. Confirmed the file hash and line count, then read the whole file (`cat -n`).
2. Captured every decision site with `sed -n` and `grep -n` (pasted below).
3. Skimmed the 3gm fidelity check: the D3 table, R21 and R29 only. Its D3 says all six order calls are managed market orders. It labels that INFERRED.
4. Pasted the run-3 Summary rows and the run-4 voice-note rows.
5. Ran arithmetic with `python3 -c`: band distance in price space, per-side cost per trade, expectancy, and outlier share. Ran a 1M-trial random check that `curUpper ≥ curLower` and that both entry conditions can never hold at once.

## Verification evidence: file identity

```
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs && wc -l ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
```
The hash matches the brief's `35393823…2265` (OBSERVED).

---

## 1. Decision-site table

| # | Site | Long code | Short code | Verdict |
|---|---|---|---|---|
| 1 | Entry test | `:226-227` `price > curUpper && MP != Long` → `EnterLong` | `:228-229` `price < curLower && MP != Short` → `EnterShort` | **SYMMETRIC**. Both use strict inequalities. The `if/else-if` order cannot matter: both conditions true at once needs `curUpper < curLower`, which cannot happen (1a). |
| 2 | Band construction | `:261,263` `refUpper = Max(open, prevClose)`; `Upper = refUpper·(1+σ)` | `:262,264` `refLower = Min(open, prevClose)`; `Lower = refLower·(1−σ)` | **SYMMETRIC in simple-return space.** In **price** space the up-distance `refUpper·σ` exceeds the down-distance `refLower·σ` by `|gap|·σ` (1b). At ref 15000, gap 50, σ 0.005 that is **0.25 pt = 1 tick**, or 0.33% of the distance. The formula is the spec's own. The sign is the same on gap-up and gap-down days. Direction: the short trigger sits slightly *closer* to its ref. Magnitude: negligible. |
| 3 | Exit stop (BandOrVWAP) | `:208-211` `stop = Max(curUpper, curVwap)`; exit if `price <= stop` | `:216-219` `stop = Min(curLower, curVwap)`; exit if `price >= stop` | **SYMMETRIC.** An exact mirror: max↔min and `<=`↔`>=`. |
| 4 | `vwapCumVol == 0` fallback | `:208` guard `&& vwapCumVol > 0` → else `curUpper` | `:216` same guard → else `curLower` | **SYMMETRIC.** The guard is identical. `:265` `curVwap = … : Close[0]` is computed once for both sides. Because of the guard, the `Close[0]` fallback never reaches either stop. |
| 5 | Reversal: exit then entry on the same bar | `:205-212` exit long, then `:228` `EnterShort` if `price < curLower` (`MP` is still `Long` before the fill) | `:213-220` exit short, then `:226` `EnterLong` if `price > curUpper` | **SYMMETRIC in code.** The fill outcome is CANNOT-DETERMINE-STATICALLY (3gm R21), but the code is mirrored, so any NT8 effect would be mirrored too. |
| 5b | Exit to flat with no same-bar re-entry: price between the band and VWAP | Long, `curVwap > curUpper`, price in `(curUpper, curVwap]`: `:211` exits. `:226` is blocked because pre-fill `MP == Long`. Flat until the next stamp. | Short, `curVwap < curLower`, price in `[curVwap, curLower)`: `:219` exits. `:228` is blocked because pre-fill `MP == Short`. | **SYMMETRIC (mirrored).** |
| 6 | 16:00 flatten | `:189-193` side-neutral gate; `:287-288` `ExitLong("FlatEOD")` | same gate; `:289-290` `ExitShort("FlatEOD")` | **SYMMETRIC.** |
| 7 | Session, VWAP and σ bookkeeping | `:147-161` open/prevClose/VWAP reset; `:171-176` typical-price VWAP; `:244-260` σ = mean of `Math.Abs(c/o − 1)` | (shared) | **SIDE-NEUTRAL.** One σ, one VWAP and one ref pair feed both sides. The absolute value removes the sign. |
| 8 | Checkpoint gate | `:196-201` `isCheckpoint`; `price = Close[0]`; `mp` | (shared) | **SIDE-NEUTRAL.** |

**Code-level asymmetry found: none that bears on behaviour.** Row 2's price-space difference is spec-mandated, 1 tick at representative levels, and slightly favours short triggers. It cannot plausibly explain a ~$10/trade gap between the sides.

### Pasted code (all from `ninjascript/PraxisNoiseAreaBreakout.cs`)

```
=== sed -n '226,229p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
=== sed -n '261,265p' ninjascript/PraxisNoiseAreaBreakout.cs
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
=== sed -n '205,220p' ninjascript/PraxisNoiseAreaBreakout.cs
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
=== sed -n '189,193p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}
=== sed -n '285,291p' ninjascript/PraxisNoiseAreaBreakout.cs
		private void FlattenAll(string reason)
		{
			if (Position.MarketPosition == MarketPosition.Long)
				ExitLong("FlatEOD", "");
			else if (Position.MarketPosition == MarketPosition.Short)
				ExitShort("FlatEOD", "");
		}
=== sed -n '147,161p' ninjascript/PraxisNoiseAreaBreakout.cs
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;
				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;

				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
				vwapCumVol = 0.0;
				haveDay    = true;
			}
=== sed -n '196,201p' ninjascript/PraxisNoiseAreaBreakout.cs
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

			double price = Close[0];             // the checkpoint stamp price (spec §2: evaluate at the stamp, not intrabar)
			MarketPosition mp = Position.MarketPosition;
=== sed -n '171,176p' ninjascript/PraxisNoiseAreaBreakout.cs
			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}
=== grep -n vwapCumVol
89:		private double vwapCumVol;
159:				vwapCumVol = 0.0;
175:				vwapCumVol += vol;
185:			if (vwapCumVol > 0)
208:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
216:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
265:			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
=== grep -n Enter/Exit
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
```

The σ loop (`:244-260`, from the full `cat -n` read): `sumAbs += Math.Abs(c / rec.Open - 1.0);` at `:253`, and `curSigma = sumAbs / cnt;` at `:260`. Both are side-neutral.

### 1a. Can both entry conditions be true? Is `curUpper ≥ curLower` always?
`refUpper ≥ refLower > 0` and `σ ≥ 0` give `refUpper·(1+σ) ≥ refLower·(1−σ)`. The two are equal only when σ = 0 and there is no gap, and then strict `>` and strict `<` cannot both hold. Random check:

```
$ python3 -c "... 1M trials: o∈[5000,25000], prevClose=o·U(0.95,1.05), σ∈[0,0.05] ..."
trials 1000000 U<L 0 both-entry-true 0
```
The 3gm D3 reaches the same result independently: "From lines 263–264, `curLower ≤ curUpper`" (pasted in §3 below).

### 1b. Price-space band distance (ref 15000, gap 50 pt, σ 0.005)
```
$ python3 -c "ref_lo=15000.0; gap=50.0; s=0.005; ref_hi=ref_lo+gap; up=ref_hi*s; dn=ref_lo*s; ..."
up-dist pts 75.25 down-dist pts 75.0 diff pts 0.25 diff ticks 1.0 diff as frac of up 0.0033222591362126247
mirror check: gap*sigma = 0.25
log-space: ln(1+s)=0.0049875  -ln(1-s)=0.0050125
```
- In price space the long trigger sits `|gap|·σ` further from its ref than the short trigger does: 1 tick here.
- In log space the effect runs the other way: the lower band is slightly further, 0.0050125 vs 0.0049875.
- Both effects are tiny. Neither one is a code deviation.

---

## 2. Hypotheses for the short-side loss (all INFERRED)

There is no trade list on record, so none of these hypotheses is tested here. Each falsifier names a readback; whether to run it, and what to do after, is Amear's decision (S8).

**H1: Code asymmetry. INFERRED: none found.** Every decision site in §1 is a mirror pair or side-neutral. The only price-space difference (row 2) is 1 tick and favours shorts.
- *What would still falsify the symmetry claim:* any short trade in the run-4 Trades tab whose exit
  - (a) is not at a :00/:30 stamp or 16:00, or
  - (b) fires at a stamp where Close < `min(LowerBound, SessionVWAP)` on the chart plots (`:122-124` plot Upper/Lower/VWAP), or
  - (c) any short entry at a stamp where Close ≥ the LowerBound plot.
- Also: a reversal bar where long→short and short→long resolve differently in NT8. For example, short→long shows a clean 2-row reverse while long→short shows a double close or an ignored entry (3gm R21 is CANNOT-DETERMINE-STATICALLY).

**H2: Market drift. INFERRED.** A trend-following breakout in a market that rose over the window earns on the up-breaks and pays on the down-breaks.
- *UNVERIFIED in this session:* the NQ level path from 2021-03 to 2026-07. No price series was read.
- *Falsifier:* split run-4 short P&L by calendar year (Trades tab, or Analyzer "Display: Yearly", Short column) and compare it with NQ's yearly return. If shorts lose in down years (e.g. 2022, UNVERIFIED as a down year) as much as in up years, H2 is falsified.

**H3: Short entries after down-moves that revert. INFERRED.** Down-breaks at :00/:30 are bought back, so shorts hit adverse excursion and give back their favourable excursion. Run-3 evidence comes from an INVALID template, so it only suggests:
- short Avg. MAE $56.27 vs long $47.73;
- short Avg. ETD $81.42 vs long $59.69;
- short win rate 32.55% vs long 43.87%;
- yet the short avg winning trade is larger ($101.69 vs $76.89).

The short loss comes from win rate, not from win size:
```
run3 win-rate gap L-S 0.11319999999999997  avg win S-L 24.799999999999997
run3 S expectancy check -2.6011899999999955  L 5.217603
```
*Falsifier:* the run-4 Summary Long/Short columns for Avg. MAE, Avg. MFE, Avg. ETD and Percent profitable. If the run-4 short MAE ≤ long MAE and the short win rate ≈ the long win rate, H3 is falsified for run 4.

**H4: The VWAP trail sits closer for shorts in up-drifting sessions. INFERRED.** In a session that drifts up, a down-break leaves VWAP above the price. The short stop is `min(Lower, VWAP)`, so it equals `curLower` until VWAP falls below the band. Any bounce back above the lower band at a stamp exits. Shorts would then be cut sooner. Run-3 (INVALID template) shows short avg bars 97.83 vs long 115.64:
```
run3 bars ratio S/L 0.8459875475613974
```
*Falsifier:* the run-4 Summary "Avg. bars in trade" / "Avg. time in market" by side. If short ≥ long, H4 is falsified. A finer test: in the Trades tab, the exit-name split by side, `XS` vs `FlatEOD` against `XL` vs `FlatEOD`. If shorts reach FlatEOD as often as longs, H4 weakens.

**H5: Costs differ by side. INFERRED: not a cause.**
```
run3 comm/trade L 2.96 S 2.9600000000000004
run3 slip/trade L 0.04 S 0.04
```
Commission per trade and the NT8 slippage figure per trade are identical by side in run 3. Run-4 per-side costs are NOT on record.
*Falsifier:* the run-4 Summary Commission and Total slippage Long/Short columns. If they divided by 584 and 627 differ, H5 is falsified.

**H6: One outlier decides the split. INFERRED.** The run-4 largest winner ($1,792.50) is 57% of net. Its side is NOT on record.
```
long net ex-1792.50 if long 2748.8999999999996
short net ex-1792.50 if short -3197.06
1792.50/net 0.5714349472717767
```
If that trade is long, longs stay positive without it (+$2,748.90). If it is short, shorts would be −$3,197.06 without it. Either way the sign of the split holds. *Falsifier/readback:* the run-4 Summary "Largest winning trade" Long/Short columns, and the ranked Trades tab.

**H7: Gap-direction mix (code symmetric, sample not). INFERRED.** On a gap-up day `refLower = prevClose` (`:262`). A short then triggers only after the price has filled the gap *and* dropped σ further: a deep, late entry that may revert. The mirror holds for longs on gap-down days. If the window had more gap-up days, shorts more often enter on these extended moves.
- *Falsifier:* for each run-4 short entry, the sign of (today 09:30 open − prior 16:00 close), from the Trades tab entry date plus the chart. If losing shorts are no more frequent on gap-up days than on gap-down days, H7 is falsified.
- No trade list exists, so this is not tested.

**H8: Unresolved NT8 same-bar exit+reverse. INFERRED: symmetric, so not side-specific by construction.** Every reversal also meets the exit condition (3gm D3, pasted). The NT8 resolution is mirrored in code. It could only explain the split if NT8 itself treats Sell-short-from-long differently from Buy-to-cover-into-long. *Falsifier:* the H1(c) readback.

Count context: run 4 is 48.2% long by count and run 3 is 48.6% long, so the trade-count split is similar.
```
run4 net/trade L 7.776369863013698 S -2.240127591706539
run4 L+S net 3136.8399999999997 count 1211
run3 net/trade L 5.213045977011494 S -2.603254972875226
run4 L share of trades 0.48224607762180016 run3 0.4855813953488372
```

---

## 3. Evidence labels and pasted sources

| Claim | Level |
|---|---|
| File hash, line numbers, code text, mirror structure | OBSERVED (pasted) |
| `curUpper ≥ curLower`, never both entries true | OBSERVED by algebra plus a 1M-trial random check (pasted). Not an NT8 run. |
| All six order calls are managed market orders | INFERRED (3gm D3's own label) |
| Run-3 Summary numbers | OBSERVED-from-screenshot, **INVALID template** (CME FX Futures RTH) |
| Run-4 net, count and per-side net | REPORTED by Amear (voice notes). Not observed by me. |
| Run-4 per-side MAE/MFE/bars/commission/largest trade | **NOT ON RECORD** |
| Trade list (either run) | **DOES NOT EXIST** |
| NQ direction over 2021-03→2026-07 | UNVERIFIED |
| Every behaviour mechanism in H1–H8 | INFERRED |

Run-4 source:
```
$ sed -n '45,60p' docs/reports/2026-10-28-voice-session-notes.md   (excerpt, lines 51-53)
## 2026-10-30 ~18:20 — Run 4 (the first valid full-history run; numbers from Amear's screenshot)
- Settings are the same as run 3 except **Trading hours = CME US Index Futures RTH**. Amear is re-saving the "Praxis Backtest" default template with the corrected session.
- 2021-03-08 → 2026-07-17 · **1,211 trades** (584 long / 627 short) · **net $3,136.84** · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 (= 1,211 × 2.96 ✓) · **PF 1.08** · **max DD −$4,108.84** · avg trade $2.59 · longs +$4,541.40 / shorts −$1,404.56 · largest winner $1,792.50 · total slippage 48.44.
```
The run-3 INVALID ruling is at line 47 of the same file:
```
- **Run 3 is INVALID. Trading hours were set to `CME FX Futures RTH`, not `CME US Index Futures RTH`.** ...
```

Run-3 source (rows used):
```
$ sed -n '30,90p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md   (rows used)
| Performance | All trades | Long trades | Short trades |
| Total net profit | $1,281.61 | $2,721.21 | −$1,439.60 |
| Commission | $3,182.00 | $1,545.12 | $1,636.88 |
| Total # of trades | 1075 | 522 | 553 |
| Percent profitable | 38.05% | 43.87% | 32.55% |
| Total slippage | **43** | 20.88 | 22.12 |
| Avg. winning trade | $87.80 | $76.89 | $101.69 |
| Avg. losing trade | −$52.00 | −$50.80 | −$52.93 |
| Avg. time in market | 106.49 min | 115.65 min | 97.84 min |
| Avg. bars in trade | 106.48 | 115.64 | 97.83 |
| Avg. MAE | $52.13 | $47.73 | $56.27 |
| Avg. MFE | $72.06 | $64.90 | $78.82 |
| Avg. ETD | $70.87 | $59.69 | $81.42 |
```

3gm D3 and R21 (skim only):
```
$ sed -n '737,760p' docs/reports/2026-10-30-3gm-fidelity-check.md   (excerpt)
- **No other order methods** (OBSERVED by the grep): no `Set*`, no `Submit*`, no Limit/StopMarket/StopLimit variants.
**Every reversal also meets the exit condition (OBSERVED in code; fuzz-confirmed).**
- From lines 263–264, `curLower ≤ curUpper`. A long is reversed only when `price < curLower`, and its stop is ≥ `curUpper`, so the exit on line 211 is also reached. The short case mirrors this.
- Whether NT8 submits both orders, and whether it then reverses cleanly, double-closes, or ignores the entry, is **INFERRED / CANNOT-DETERMINE-STATICALLY**.
$ sed -n '515,517p' ...
#### R21 — §C L53 — reversal; exit + reverse on the same bar
**Verdict: CANNOT-DETERMINE-STATICALLY.** Every reversal also meets the exit condition (OBSERVED in code; fuzz 0/129,174 here, 0/305,112 by W4). NT8's resolution is INFERRED: clean reverse, double close, or entry ignored.
$ sed -n '670,671p' ...
#### R29 — ties: exits <=/>=, entries strict >/<
**Verdict: SPEC-SILENT.** Equality is not addressed by the spec; incidence is low.
```

### Out-of-scope observation (reported, not fixed)
`:36` says "NQ futures … $5.00 / point (=$1.25 / tick)". That point value is UNVERIFIED here, so I made no $-per-tick conversion. 3gm already grades this comment as R25.

## Files staged
None. One report file was written: `docs/reports/2026-10-31-o78-worker1-symmetry.md`. It is not `git add`-ed.

## Decisions left to Amear (S8)
Whether to run any readback above, how to weigh the hypotheses, and whether any change to the short side is warranted. This report does not answer any of them.

Result: PASS


---

## Manager correction note (2026-10-31, appended; nothing above was edited)

The adversarial worker `docs/reports/2026-10-31-o78-worker3-adversarial.md` raised findings F4, F5 and F6 against this report. They are accepted, and the manager report `docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md` carries the corrected text. Where this report conflicts with W3 F4–F6, W3 governs:
- **F4 (MAJOR):** H1–H8 omit **H9, NT8 run vs clean-model divergence on the short side.** H2 is weakened. The NQ yearly returns are checkable on disk (2022 −28.2%).
- **F5 (MINOR):** "shorts trigger slightly easier" holds only relative to each band's own reference. Measured from the session open, this sample's gap mix makes the long trigger closer, on 53–57% of days. Whether the gap is small depends on the point value.
- **F6 (MINOR):** `curUpper ≥ curLower` is INFERRED (algebra) plus simulated (random trials), not OBSERVED. The elided commands at lines 15, 138, 155 and 162 cannot be re-run as pasted.
