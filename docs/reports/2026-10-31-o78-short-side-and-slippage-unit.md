# o78: why run 4's shorts lost while longs won, and what NT8's "Total slippage" measures

**Unit:** `Praxis_build-o78` · **Date:** 2026-10-31 · **Author:** praxis-manager · **Mode:** read-only research. No code was changed and no NT8 backtest was run. See S6 for one scope deviation by a worker.

## Task

- **(A)** A code-level symmetry read of the long and short paths in `ninjascript/PraxisNoiseAreaBreakout.cs`. Hypotheses, each with a falsifier, for why run 4's shorts lost (−$1,404.56 on 627 trades) while its longs won (+$4,541.40 on 584).
- **(B)** What the NT8 Strategy Analyzer Summary row "Total slippage" measures, and in what unit. Whether Slippage = 2 lands on every market fill. Sources on disk only.

## Rubric criteria addressed (`specs/SPEC_RUBRIC.md`, verbatim)

- **S1:** "Every claim in a report has pasted command output, not a description of output." Every block under Verification evidence below was produced by running the command shown when this report was built. Nothing in those blocks was retyped.
- **S2:** "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure." Every claim carries one of these labels:
  - OBSERVED (read on disk this session);
  - OBSERVED-from-screenshot (run 3, INVALID template);
  - REPORTED (Amear; run 4);
  - INFERRED;
  - UNVERIFIED.
- **S6:** see `## S6`.
- **S8:** "No question that belongs to Amear is answered on his behalf." `## NEEDS AMEAR` lists readbacks only. PRAXIS recommends no action on the strategy, the cost model or the instrument.
- **S9:** "Any config field a guarantee depends on is positive-controlled … A field that parses is not a field that is honoured." The Analyzer's Slippage = 2 field is **not shown to be honoured** until one fill price has been read against its bar's Open. That read has not happened, so per-fill application stays UNVERIFIED (B4).

## Bottom line

1. **(A) The code has no long/short asymmetry.**
   - Every decision site is either a mirror pair or shared by both sides (E2; W1's table; W3 checked 8 of 8 code blocks byte-for-byte).
   - So a side-asymmetric result must come from an asymmetric input (market drift, gap mix, data) or from engine handling. Such an input can act *through* the symmetric rules: the gap-dependent band distance in A1 row 2, or the stop/trail mechanics in H3/H4. Which one is not established (W4-1).
   - Every candidate cause below is INFERRED. Each one names the Trades-tab readback that would falsify it.
2. **(B) Best reading, INFERRED: runs 3 and 4 executed on a Stock-typed `NQCONT`** (DB `InstrumentType` 1; the mapping 1 → Stock is itself INFERRED). That instrument is worth $1 per point and has a 0.01 tick, unlike the NQ future ($20 per point, 0.25 tick). On that reading:
   - "Total slippage" = 4 × 0.01 × trades. With a $1 point value, points and dollars are the same number.
   - The slippage inside run 4's net is **$48.44**, not $24,220.
   - Every price-derived $ figure in runs 3 and 4 is in $1/pt, which is 1/20 of real NQ dollars.
   - **What supports it:**
     - The definition exists in the old Parallels DB (E5).
     - All four slippage totals match exactly (E5).
     - All five extreme trades fit $1/pt and no other point-value / tick combination tried (E5; W3's brute force).
     - Run 4's largest winner matches one import-file trade to the cent (E6).
   - **What caps confidence:**
     - The Fusion instrument list has not been read.
     - The aggregate residues are not zero (E6).
     - Run 4's figures are REPORTED.
3. **No NT8 text on disk defines the unit, or says which order types the Slippage field applies to (E4, E7).** The claim "applies to market and stop fills, not limit fills" first appears on disk in a "Claude's estimate" bullet (voice notes `:42`). It is **UNVERIFIED**.

## A. Symmetry read

### A1. Decision sites

Line numbers refer to the base file (sha256 `35393823…2265`, 312 lines; E1). The code lines are pasted in E2.

| # | Site | Long | Short | Verdict |
|---|---|---|---|---|
| 1 | Entry test | `:226-227` `price > curUpper && MP != Long` → `EnterLong` | `:228-229` `price < curLower && MP != Short` → `EnterShort` | **SYMMETRIC.** Both inequalities are strict. The `if/else-if` order cannot matter: `curUpper ≥ curLower` always holds, since refUpper ≥ refLower and σ ≥ 0, so both tests can never be true at once. That is INFERRED from algebra plus W1's random-trial simulation, not observed in NT8. |
| 2 | Band construction | `:261,:263` `refUpper = Max(todayOpen, prevClose)`, `Upper = refUpper·(1+kσ)` | `:262,:264` `refLower = Min(…)`, `Lower = refLower·(1−kσ)` | **SYMMETRIC in return space.** In price space the upper band sits \|gap\|·σ further from its own reference than the lower band does (median 0.19–0.50 pt, p90 0.90–1.50, max 6.84 pt; W3 E4). Measured from the session open, this sample's gap mix (683 gap-up vs 610 gap-down days) puts the long trigger closer on 53–57% of days (W3 E5). Neither effect is a code asymmetry; the formula is the spec's own. Whether "closer" helps or hurts is not established. |
| 3 | Exit stop (BandOrVWAP) | `:208-211` `stop = Max(curUpper, curVwap)`; exit if `price <= stop` | `:216-219` `stop = Min(curLower, curVwap)`; exit if `price >= stop` | **SYMMETRIC.** An exact mirror: max ↔ min and `<=` ↔ `>=`. The VWAP trail is mirrored in code. Its *effect* depends on where VWAP sits relative to price, which is a property of the market (H4). |
| 4 | `vwapCumVol == 0` fallback | `:208` guard `&& vwapCumVol > 0`, else `curUpper` | `:216` same guard, else `curLower` | **SYMMETRIC.** `:265`'s `Close[0]` fallback for `curVwap` never reaches either stop, because of the guard. |
| 5 | Same-bar exit then reverse | exit block `:205-212`, then `:228` `EnterShort` (`MP` is still Long before the fill) | `:213-220`, then `:226` `EnterLong` | **SYMMETRIC in code.** How NT8 fills an exit plus a reverse is not determinable statically (3gm R21), but it is mirrored on both sides. |
| 5b | Exit to flat, no same-bar re-entry | price in `(curUpper, curVwap]` → `:211` exits; `:226` is blocked because pre-fill `MP == Long` | mirror: `[curVwap, curLower)` → `:219`; `:228` blocked | **SYMMETRIC.** |
| 6 | 16:00 flatten | `:189-193` side-neutral gate; `:287-288` `ExitLong("FlatEOD")` | `:289-290` `ExitShort("FlatEOD")` | **SYMMETRIC.** |
| 7 | Session, VWAP and σ bookkeeping; checkpoint gate | `:147-176`, `:196-201`, `:244-260` | shared | **SIDE-NEUTRAL.** One σ (an absolute value), one VWAP and one reference pair feed both sides. |

### A2. Hypotheses for the short-side loss

All mechanisms below are INFERRED. Run 3's by-side numbers are OBSERVED-from-screenshot but come from an **INVALID template** (E3). Run 4's by-side numbers beyond net and trade count are **not on record**, and no trade list exists for either run.

| H | Hypothesis | What is on record | Falsifying readback (run-4 Trades / Summary) |
|---|---|---|---|
| H1 | **Code asymmetry** | **None found.** Rows 1–7 above, E2. | One short trade whose exit stamp or price does not match the first stamp where Close ≥ min(Lower, VWAP), while the mirrored long logic holds on its trades. |
| H2 | **Market drift:** NQ rose over 2021-03 → 2026-07, so a symmetric breakout loses on shorts | On the import file (OBSERVED data read, E6): 2021 +23.2%, **2022 −28.2%**, 2023 +36.0%, 2024 +17.1%, 2025 +14.0%, 2026 YTD +10.7%. Whether Fusion's data is this file is UNVERIFIED. **Weakened** by W3's replication (H9). | Short P&L by year. If shorts also lose in 2022, a falling year, drift alone is falsified. |
| H3 | **Down-breaks at :00/:30 revert:** shorts are stopped more often | Run 3 (INVALID template): % profitable S **32.55%** vs L **43.87%**; avg MAE S $56.27 vs L $47.73; avg MFE S $78.82 vs L $64.90; avg winner S $101.69 vs L $76.89 (E3). Shorts won *bigger* but *less often*. | Run-4 % profitable and avg MAE by side. If the short win rate is ≥ the long win rate, H3 is falsified. |
| H4 | **The VWAP trail cuts shorts sooner** in up-drifting sessions | Run 3 (INVALID template): avg bars in trade S 97.83 vs L 115.64 (E3). | Run-4 exit reason by side (`XS`/`XL` trail vs `FlatEOD` vs NT8 "Exit on session close" vs reversal) and avg bars by side. If short exits are not disproportionately trail exits, H4 is falsified. |
| H5 | **Costs differ by side** | **Not supported as a cause.** Run 3 by side (INVALID template): $2.96 and 0.04 per trade on both sides (E5). Run 4 totals (REPORTED): $3,584.56 = 1,211 × 2.96 and 48.44 = 1,211 × 0.04, so the per-trade cost is flat in aggregate (E3, E5). Run-4 by-side costs are not on record. | Run-4 commission by side ≠ 627 × $2.96 or 584 × $2.96. |
| H6 | **Scale, not cause: the run is in $1/pt (B)** | An accounting identity, arithmetic only (E6). If the $1/pt, 3.00/RT model holds, run-4 shorts are **+476.44 pts before costs**. Costs (627 × 3.00 = 1,881 pts, assumed) exceed that. Under the $1/pt model each trade is charged 3.00 pts. The locked F3 real-NQ cost is 1.148 pts/RT: commission is 20× heavier in points, slippage 25× lighter, so the total is **2.6×**. Re-costed at $20/pt with $2.96 + $20/RT, run-4 shorts are **−$4,867.12** and longs **+$112,459.36**. This inherits the residue caveat (B3) and is **not a result**. The sign of each side does not change. | Readback B-2/B-3 (point value). If the run was at $20/pt, H6 falls away. |
| H7 | **The $1,792.50 outlier decides the split** | It is a **long** (2025-04-09, 12:31 → 16:00; matched to the cent, E6, INFERRED). Without it longs are still +$2,748.90 vs shorts −$1,404.56 (E6). | The Trades tab's largest winner is a short, or the split flips when it is removed. |
| H8 | **NT8's same-bar exit + reverse handling is side-specific** | The code is mirrored (row 5), so by construction it is not side-specific. | A reversal row whose fill pattern differs between L→S and S→L. |
| H9 | **NT8 run vs clean-model divergence on the short side** (data, session or holiday handling, fill engine, or instrument) | W3 replicated the strategy in Python on the import file (OBSERVED as W3's capture, **not re-run by the manager, outside the brief; see S6**, INFERRED quality, not NT8). It reproduced run 4's largest winner exactly and the long side roughly (581 vs 584 trades). It did **not** reproduce the short side: 597–599 vs 627 trades, and **+$1,750 to +$2,073** vs −$1,404.56 at $1/pt (E8). Candidate sources, all UNVERIFIED: (a) Fusion data ≠ the import file. (b) Holiday handling. (c) Weekend rows: the import file holds **127 rows dated Saturday across 66 dates**, 58 of them inside 09:31–16:00 on 44 dates within the run window. 6 are on 2024-01-20, one printing 3,100 (W3 F9; W4-E3). The rescued RTH templates list Mon–Fri sessions only, so these rows would probably be excluded (INFERRED). (d) **The trading-hours template.** The rescued Parallels `CME US Index Futures RTH` template is Mon–Fri **08:30–16:00, Eastern** (OBSERVED on disk by W4, W4-E6; mtime Aug 29). If Fusion's copy is the same, `IsFirstBarOfSession` (`:147-159`) lands on 08:31, so `todayOpen` and the VWAP anchor would come from the 08:31 bar, not the 09:30 open the spec requires (INFERRED). **Counter-evidence (REPORTED):** on Fusion, under the RTH template, Amear saw the 16:00 bar followed by 9:31 (`docs/reports/2026-10-30-3gm-worker1-checklist.md:530`). Fusion's template is UNVERIFIED. | Export the run-4 Trades tab and diff it against the replication's trade list. If the extra or divergent trades are not concentrated on the short side, H9 is falsified. |

The ranking is not established. H3 and H4 describe the run-3 profile, and H9 is the only hypothesis with a direct quantitative conflict on record. Which of them to pursue is Amear's decision.

## B. "Total slippage": unit and per-fill application

### B1. Candidate definitions

Each candidate assumes 4 slippage ticks per round trip (2 fills × 2 ticks). It is checked against run 4's 48.44 and run 3's 43, 20.88 (L) and 22.12 (S); the arithmetic is in E5.

| Rank | Candidate | All 4 match | Instrument on disk | Extreme-trade test | Verdict |
|---|---|---|---|---|---|
| 1 | **Points at tick 0.01 ≡ $ at tick 0.01 and $1/pt** (Stock-typed NQCONT) | ✓ | ✓ NQCONT with `InstrumentType` 1 (INFERRED Stock), point value 1.0, tick 0.01, `US Equities RTH`, in all three old-DB copies (E5) | ✓ all 5 fit (P + 3.00) on a 0.25 grid. ✗ aggregate residues 0.09–0.21 (E6) | **Best reading, INFERRED** |
| 2 | Ticks / 100 | ✓ | No such unit on disk. The XML units are Currency, Percent, Pips, Points, Ticks. | n/a | Equal to rank 1 only because the tick is 0.01. Not a known NT8 unit (UNVERIFIED). |
| ✗ | Points at tick 0.25 (1,211) · $ at 0.25 tick, $20/pt (24,220) · $ at 0.01 tick, $20/pt (968.80) · raw ticks (4,844) · $ at 0.25 tick, $1/pt (1,211) | ✗ | — | $20/pt fails all 5 extremes, with or without slippage (E5) | Rejected |

### B2. Implied slippage cost inside run 4's net

| Reading | Slippage $ |
|---|---|
| **Best reading ($1/pt, 0.01 tick)** | **$48.44**. If the best reading holds (INFERRED), what was simulated is 0.02 pt/side, not the locked F3 assumption: 2 ticks/side = $10/side at $20/pt (F3 artifact `:226`, DECISION_LOG `:442`). |
| Future NQCONT, every fill slipped 2 ticks | $24,220. Inconsistent with every displayed figure. |
| 0.01 tick at $20/pt | $968.80. Fails the extreme-trade test. |

### B3. The open anomaly

Under the best reading, every trade's P&L + 3.00 should be a multiple of 0.25, so the totals should be too. They are not: (net + 3n) mod 0.25 = 0.09 (run 4), 0.19 / 0.15 (run-4 S / L), 0.11 / 0.15 / 0.21 (run 3 all / S / L) (E6; W2). The $20/pt model fails the same test.

Possible causes, all UNVERIFIED:
- some fills not at a 0.25-grid bar price;
- per-trade costs differing from the Commission row;
- Fusion data ≠ the import file;
- a transcription error in run 4, which is REPORTED.

### B4. Per-fill application

1. All six order calls are managed market orders (3gm D3, labelled INFERRED there).
2. The claim "the Analyzer slippage applies to market and stop fills, not limit fills" has **no NT8 source on disk**. Its earliest appearance is a "Claude's estimate" bullet (E7). **UNVERIFIED.**
3. The totals equal exactly 2 ticks on each of 2 fills per trade under the best reading. That is *consistent with* every fill being slipped, but it is a sum, not an observation of any fill.
4. Per S9, Slippage = 2 parses and a non-zero total is displayed, but **honoured-on-every-fill is UNVERIFIED** until one fill is read against its bar's Open (readback B-2).
5. The Analyzer log XML repeats every summary field under each PerformanceUnit, including fields that never change (TotalNetProfit). There is no `TotalSlippageValue` twin (E9). So switching the display unit **may not** change Total slippage. W2's original "unit-dependent" claim is withdrawn (W3 F3).

### B5. Cross-block reach (flag only; nothing touched)

If the best reading is confirmed, it reaches every artifact built on run-3/run-4 dollar figures or on the assumption that "2 ticks/side was simulated":
- the F3 cost model and its ruling D-2026-10-30-A;
- the 3gm D3 cost bounds;
- the run-3 record and the run-4 voice-note figures;
- any 7zq backtests run on the same NQCONT.

None of these was edited. What to do about them is Amear's decision, routed by the master.

## S6

**Cross-block check.** This unit touched no file outside its own reports. The four `docs/reports/2026-10-31-o78-*.md` files are new; the post-skeleton change scan is in E10, and the B5 reach above is a flag only. No approved deviation is introduced by this unit, so there is nothing to test against other blocks. **Two disclosed process deviations:**
1. **Worker 3 (adversarial) ran a Python replication of the strategy on the import file.** That exceeds the brief's "no backtest". It was Python only: not NT8, and no code or repo file was changed. The manager did **not** re-run it. Its outputs appear here only as W3's capture (E8), labelled INFERRED and out of scope, and only under H9. The one replication fact used elsewhere, the 2025-04-09 largest-winner match, was re-checked by the manager with a plain data read (E6), not a replay.
2. **The manager appended correction notes** to the W1 and W2 reports. Nothing was edited above them, and the original text is preserved. They record W3 F3–F8 so that neither worker report stands uncorrected.

## NEEDS AMEAR (readbacks only — nothing to decide here)

1. **Fusion, `Tools > Instruments`, filter `NQCONT` (and `NQ`).** For every row, read Type, Tick size, Point value, Trading hours and Expiry. Also read which NQCONT the Analyzer's instrument field named for run 4. Also read `Tools > Trading Hours > CME US Index Futures RTH`: its time zone and each session's begin and end time (H9 d).
2. **Run 4's largest winner (Trades tab).** If the best reading holds, expect: Long; entry ≈ **18,691.27** (= 18,691.25 + 0.02) on 2025-04-09 around 12:31; exit ≈ **20,486.73** at 16:00; profit $1,792.50. Also read the exit name (`FlatEOD` or NT8's "Exit on session close") and whether the exit price carries the −0.02. The 1,792.50 match needs a fill at the 16:00 bar's Close; the 16:01 Open is 20,487.75 (W4-10). A 0.04 slip on the entry alone gives the same total, so the profit figure does not show how the slippage splits between entry and exit. An entry ending in `.27` shows the 0.01 tick and slippage directly. Other outcomes: `18,691.75` means a 0.25 tick with 2 ticks honoured; `18,691.25` means no slippage.
3. **Any one run-4 trade:** entry price vs the Open of the bar after the signal bar. Expect +0.50 pt (0.25 tick, Slippage honoured), +0.02 (0.01 tick) or +0.00 (not applied); a short is the mirror. Also check whether Profit = (exit − entry) × 1 − $2.96, or × 20 − $2.96.
4. **Summary "Total slippage":** any tooltip or help text NT8 shows, and its value under each display unit (Currency / Points / Ticks). If it is the same in every unit, the switch does not settle the unit (B4.5).
5. **Run-4 Trades-tab export** (or by-side figures: % profitable, avg MAE/MFE, avg bars, exit-reason split, P&L by year). This is the falsifier for H2–H4 and H9.
6. **Import file:** it holds 127 rows dated Saturday across 66 dates (58 inside 09:31–16:00), including 6 on 2024-01-20, one at 3,100 (W3 F9, W4-3). Whether Fusion's RTH template excludes them is UNVERIFIED. Whether to clean the file is his call.

## Workers dispatched

| Id | Mode | Report | Outcome |
|---|---|---|---|
| W1 `a1cd68e1526d6589d` | BUILD | `docs/reports/2026-10-31-o78-worker1-symmetry.md` | Returned PASS. Survived W3 on code symmetry (8 of 8 blocks byte-identical). Corrected by W3: F4 (H9 missing, MAJOR), F5 and F6 (MINOR). |
| W2 `a9ad2b40ddcfc1d27` | BUILD | `docs/reports/2026-10-31-o78-worker2-slippage-unit.md` | Returned PASS. Survived W3: the DB rows, the $20/pt exclusion, no NT8 text on disk, and the origin of the market/stop claim. Corrected by W3: F3 (unit-dependence claim withdrawn, MAJOR), F7 and F8 (MINOR). |
| W3 `aa1c5554c90b68566` | ADVERSARIAL | `docs/reports/2026-10-31-o78-worker3-adversarial.md` | VERDICT BROKEN on the manager's synthesis claim (F1 "20× heavier" wrong; F2 "entirely costs" overclaimed). W1 and W2 survive with corrections. Exceeded scope with a Python replication (S6). |
| W4 `ae73270cb6e608184` | ADVERSARIAL on this report | `docs/reports/2026-10-31-o78-worker4-report-adversarial.md` | VERDICT SURVIVED-WITH-CORRECTIONS: 3 MAJOR (W4-1, W4-2, W4-3), 9 MINOR, 0 CRITICAL, no S8 breach. 12 of 15 blocks re-ran byte-identical; the other 3 differ for observer-effect or fence reasons. All 12 findings accepted and folded in. |

## Process log

1. Read the rubric (S1/S2/S6/S8/S9), the bead and the `.cs` (`:120-312`). Hash confirmed (E1). Created a report skeleton early, because the stop-gate grades the newest report.
2. Probed the disk. Found the rescued Parallels NT8 tree (`/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/`) with `db/NinjaTrader.sqlite`, Analyzer log XMLs, `bin/Custom` and an MSI. No extraction tools are present (7z, cabextract, ilspy, mono, dotnet: none).
3. Dispatched W1 (A) and W2 (B) in parallel, both BUILD.
4. Read both reports. Re-ran W2's sqlite, grid, extreme-trade and candidate checks myself (E5); all matched.
5. Dispatched W3 (ADVERSARIAL) on both artifacts and on my own synthesis claim (pre-cost short points). W3 broke the synthesis claim (F1/F2) and W2's unit-dependence claim (F3), and added H9 (F4).
6. Re-verified W3's load-bearing data facts myself (E6): the 2025-04-09 bars, yearly drift, cost arithmetic and residues. All matched. I did not re-run W3's replication (S6).
7. Appended correction notes to the W1 and W2 reports. Built this report with a script that runs every evidence command fresh. Staged the files, then dispatched W4 on this report.
8. W4 returned SURVIVED-WITH-CORRECTIONS. I applied all 12 fixes (W4's replacement text, plus the REPORTED counter-evidence to W4-2), rebuilt this report with fresh evidence, and re-staged it together with W4's report.

## Verification evidence

All blocks below were produced by running the shown command when this report was built (generated by `scratchpad/build_o78.py`). The scratchpad path is `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/`, abbreviated `$S` here.

**E1. File identity**
```
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs; wc -l ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
```

**E2. Paired decision lines (long/short)**
```
$ /usr/bin/grep -n "price > curUpper\|price < curLower\|Math.Max(curUpper\|Math.Min(curLower\|price <= stop\|price >= stop\|double refUpper\|double refLower\|curUpper = \|curLower = \|curVwap  = \|ExitLong(\|ExitShort(\|EnterLong(\|EnterShort(\|mod >= CloseMod\|vwapCumVol > 0)" ninjascript/PraxisNoiseAreaBreakout.cs
185:			if (vwapCumVol > 0)
189:			if (mod >= CloseMod)
208:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
209:					? Math.Max(curUpper, curVwap) : curUpper;
210:				if (price <= stop)
211:					ExitLong("XL", "");
216:				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
217:					? Math.Min(curLower, curVwap) : curLower;
218:				if (price >= stop)
219:					ExitShort("XS", "");
226:			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
228:			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
261:			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
262:			double refLower = Math.Min(todayOpen, prevClose);
263:			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
264:			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
265:			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
```

**E3. Run-4 figures (REPORTED, voice notes `:53`) and run-3 Summary by side (OBSERVED-from-screenshot, INVALID template)**
```
$ sed -n '53p' docs/reports/2026-10-28-voice-session-notes.md
- 2021-03-08 → 2026-07-17 · **1,211 trades** (584 long / 627 short) · **net $3,136.84** · gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 (= 1,211 × 2.96 ✓) · **PF 1.08** · **max DD −$4,108.84** · avg trade $2.59 · longs +$4,541.40 / shorts −$1,404.56 · largest winner $1,792.50 · total slippage 48.44.
```
```
$ sed -n '40,77p' docs/reports/2026-10-30-run3-backtest-screenshot-record.md
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
```

**E4. On-disk search for a definition.** Observer effect: the o78 reports themselves now match, because they quote the phrase. Every hit is PRAXIS commentary; W2 classified each one (W2 §(a)). The rescued NT8 tree has slippage text only in two Analyzer logs, and those are settings, not definitions.
```
$ /usr/bin/grep -rIl --ignore-case "total slippage\|totalslippage" --exclude-dir=.git . /Users/admin/praxis-signals | sort
./.claude/state/handoff-latest.md
./DECISIONS.md
./DECISION_LOG.md
./HANDOFF.md
./STATUS.md
./docs/reports/2026-10-28-voice-session-notes.md
./docs/reports/2026-10-30-run3-backtest-screenshot-record.md
./docs/reports/2026-10-30-zyd-f3-artifact.md
./docs/reports/2026-10-30-zyd-rulings-append.md
./docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md
./docs/reports/2026-10-31-7zq-handtest-checklist.md
./docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md
./docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
./docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
./docs/reports/2026-10-31-o78-worker1-symmetry.md
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md
./docs/reports/2026-10-31-o78-worker3-adversarial.md
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md
```
```
$ /usr/bin/grep -rIl --ignore-case "slippage" --include="*.cs" --include="*.resx" --include="*.xml" --include="*.txt" "/Users/admin/VM-Rescue-2026-09-29/files" | sort
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
```

**E5. NQCONT definitions (old Parallels DB, read-only), price grid, extreme-trade test, candidate units, per-trade cost by side**
```
$ python3 -I "$S/mgr_verify.py"
== NinjaTrader.sqlite
   (135, 'NQ', 0, 20.0, 0.25, 'CME US Index Futures ETH')
   (699839150754593, 'NQ', 1, 1.0, 0.01, 'US Equities RTH')
   (699839150754594, 'NQCONT', 0, 20.0, 0.25, 'CME US Index Futures RTH')
   (699839150754605, 'NQCONT', 1, 1.0, 0.01, 'US Equities RTH')
== NinjaTrader.sqlite.bak_praxis
   (135, 'NQ', 0, 20.0, 0.25, 'CME US Index Futures ETH')
   (699839150754593, 'NQ', 1, 1.0, 0.01, 'US Equities RTH')
   (699839150754594, 'NQCONT', 0, 20.0, 0.25, 'CME US Index Futures RTH')
   (699839150754596, 'NQCONT', 1, 1.0, 0.01, 'US Equities RTH')
== NinjaTrader.sqlite.bak_praxis2
   (135, 'NQ', 0, 20.0, 0.25, 'CME US Index Futures ETH')
   (699839150754593, 'NQ', 1, 1.0, 0.01, 'US Equities RTH')
   (699839150754594, 'NQCONT', 0, 20.0, 0.25, 'CME US Index Futures RTH')
   (699839150754595, 'NQCONT', 1, 1.0, 0.01, 'US Equities RTH')
import OHLC values 7429448 off 0.25 grid 0
r3 win $20/0.25 (P+2.96)%5==0: False | $1/0.01 2tk/side (P+3.00)%0.25==0: True
r3 L win $20/0.25 (P+2.96)%5==0: False | $1/0.01 2tk/side (P+3.00)%0.25==0: True
r3 loss $20/0.25 (P+2.96)%5==0: False | $1/0.01 2tk/side (P+3.00)%0.25==0: True
r3 L loss $20/0.25 (P+2.96)%5==0: False | $1/0.01 2tk/side (P+3.00)%0.25==0: True
r4 win (REPORTED) $20/0.25 (P+2.96)%5==0: False | $1/0.01 2tk/side (P+3.00)%0.25==0: True
r4 1211 ticks/100= 48.44 pts@0.01= 48.44 pts@0.25= 1211.00 $@0.25x$20= 24220
r3 1075 ticks/100= 43 pts@0.01= 43.00 pts@0.25= 1075.00 $@0.25x$20= 21500
r3L 522 ticks/100= 20.88 pts@0.01= 20.88 pts@0.25= 522.00 $@0.25x$20= 10440
r3S 553 ticks/100= 22.12 pts@0.01= 22.12 pts@0.25= 553.00 $@0.25x$20= 11060
r3 avg MAE $52.13 -> pts @$20: 2.6065 @$1: 52.13
r3 commission/trade L,S: 2.96 2.96 slip/trade L,S: 0.04 0.04
```

**E6. The 2025-04-09 largest-winner match, NQ yearly drift (import file), the pre-cost/re-costed arithmetic, residues**
```
$ python3 -I "$S/mgr_verify2.py"
2025-04-09 rows (time;O;H;L;C;V):
   20250409 123000;18699.75;18707;18684.25;18693.25;973
   20250409 123100;18691.25;18702;18664.5;18698.25;1256
   20250409 160000;20516;20552.5;20481.5;20486.75;17227
largest-winner check: 16:00 close - 12:31 open - 3.00 = 1792.50 | at $20/pt minus 2.96 = 35907.04
yearly RTH first 09:31 open -> last 16:00 close, % (2026 partial):
   2021 16032.75 19755.25 23.2
   2022 19813.25 14232.25 -28.2
   2023 14329 19492.5 36.0
   2024 19350.75 22660.75 17.1
   2025 22787.75 25980.25 14.0
   2026 26207 29016 10.7
r4 S pre-cost pts if $1/pt & 3.00/RT: 476.44 | re-costed $20/pt, 2.96 comm + $20/RT slip: -4867.12 | residue (net+3n) mod 0.25: 0.19
r4 L pre-cost pts if $1/pt & 3.00/RT: 6293.40 | re-costed $20/pt, 2.96 comm + $20/RT slip: 112459.36 | residue (net+3n) mod 0.25: 0.15
r3 S pre-cost pts if $1/pt & 3.00/RT: 219.40 | re-costed $20/pt, 2.96 comm + $20/RT slip: -8308.88 | residue (net+3n) mod 0.25: 0.15
r3 L pre-cost pts if $1/pt & 3.00/RT: 4287.21 | re-costed $20/pt, 2.96 comm + $20/RT slip: 73759.08 | residue (net+3n) mod 0.25: 0.21
cost/RT in points: $1 model 3.00 | real NQ locked F3 (2.96+20)/20 = 1.148 | ratio 2.613
run4 avg trade L 7.776 S -2.24 gap 10.016
```
```
$ python3 -I -c "print('longs without the 1792.50 outlier:', round(4541.40-1792.50,2), '| shorts:', -1404.56)"
longs without the 1792.50 outlier: 2748.9 | shorts: -1404.56
```

**E7. Origin of "market and stop fills, not limit fills".** Observer effect: this grep matches its own pasted lines in this report and in W2/W3/W4, so a re-run returns more self-hits. The non-self hits are the evidence: voice notes `:42`, 3gm-worker2 `:60`, and DECISION_LOG if listed.
```
$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "market and stop fills" . | cut -c1-220
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md:73:    -./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and 
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md:74:    -./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer 
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md:77:    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:334:**E7. Origin of "mar
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md:81:    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:344:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and 
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md:82:    +./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:345:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer 
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:42:3. **No NT8 text on disk defines the unit, or says which order types the Slippage field applies to (E4, E7).** The claim "applies to market and stop fills,
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:112:2. The claim "the Analyzer slippage applies to market and stop fills, not limit fills" has **no NT8 source on disk**. Its earliest appearance is a "Claude
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:334:**E7. Origin of "market and stop fills, not limit fills"**
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:336:$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "market and stop fills" . | cut -c1-220
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:337:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:42:3. **No NT8 text on disk defines the unit, or says which order types the Slippage field a
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:112:2. The claim "the Analyzer slippage applies to market and stop fills, not limit fills" h
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:334:**E7. Origin of "market and stop fills, not limit fills"**
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:340:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:336:$ /usr/bin/grep -rIn --ignore-case --exclude-dir=.git "market and stop fills" . | cut -c
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:341:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:338:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and st
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:342:./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:339:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer sl
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:344:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and stop fills, not limit fills" has no NT8 source on disk.** Its first 
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md:345:./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer slippage applies to market and stop fills, not limit fills"
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:60:- Run 3 cost arithmetic (Claude's estimate): commission ≈ 1,075 × $2.96 = $3,182. Slippage ≈ 1,075 × 2 sides × 2 ticks × $5 = $21,500, **if NT8 applied slip
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:36:7. **"Applies to market and stop fills, not limit fills" has no NT8 source on disk.** Its first on-disk appearance is the voice notes `:42`, inside a "Claude's es
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:296:## Origin of "NT8 Analyzer slippage applies to market and stop fills, not limit fills"
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:300:./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:60:- Run 3 cost arithmetic (Claude's estimate): ... In NT8 the Analyzer slippage applies to market a
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md:301:./docs/reports/2026-10-28-voice-session-notes.md:42:- Run 3 cost arithmetic (Claude's estimate): ... In NT8 the Analyzer slippage applies to market and stop fill
./docs/reports/2026-10-28-voice-session-notes.md:42:- Run 3 cost arithmetic (Claude's estimate): commission ≈ 1,075 × $2.96 = $3,182. Slippage ≈ 1,075 × 2 sides × 2 ticks × $5 = $21,500, **if NT8 applied slippage to ever
./DECISION_LOG.md:444:- [2026-10-30T21:37:30Z] WHO: praxis-master | WHAT: **DISPATCH ORDER FOR THIS SESSION, decided before the first spawn: (1) `Praxis_build-3gm` fidelity check FIRST — read-only grading of `ninjascript
```

**E8. W3's replication output (W3's capture, quoted from its report; NOT re-run by the manager; outside the brief, see S6)**
````
$ sed -n '127,150p' docs/reports/2026-10-31-o78-worker3-adversarial.md
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
````

**E9. Analyzer log XML: a unit-twin exists for net profit but not for slippage (positive / negative control)**
```
$ for f in "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/"*.xml; do printf '%s TotalNetProfitValue=%s TotalSlippageValue=%s TotalSlippage=%s Slippage=%s\n' "$(basename "$f")" "$(/usr/bin/grep -c TotalNetProfitValue "$f")" "$(/usr/bin/grep -c TotalSlippageValue "$f")" "$(/usr/bin/grep -c '<TotalSlippage>' "$f")" "$(/usr/bin/grep -o '<Slippage>[^<]*' "$f" | head -1)"; done
@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml TotalNetProfitValue=5 TotalSlippageValue=0 TotalSlippage=0 Slippage=<Slippage>0
@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml TotalNetProfitValue=5 TotalSlippageValue=0 TotalSlippage=0 Slippage=<Slippage>0
```

**E10. Scope: repo files modified after this unit's skeleton was created (local 08:42:52; window opens 08:42:30), and who wrote DISPATCH_LOG.** STATUS/DECISION_LOG/HANDOFF (mtime 08:42:03) were written by the master at dispatch, before the window; they do not appear. DISPATCH_LOG rows are the SubagentStart/SubagentStop hook, keyed to this unit's worker ids.
```
$ find . -path ./.git -prune -o -path ./.beads -prune -o -type f -newermt "2026-10-31 08:42:30" -print | sort
./DISPATCH_LOG.md
./docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
./docs/reports/2026-10-31-o78-worker1-symmetry.md
./docs/reports/2026-10-31-o78-worker2-slippage-unit.md
./docs/reports/2026-10-31-o78-worker3-adversarial.md
./docs/reports/2026-10-31-o78-worker4-report-adversarial.md
```
```
$ git diff -U0 -- DISPATCH_LOG.md | tail -6 | cut -c1-200
+- [2026-10-31T12:48:41Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a1cd68e1526d6589d, matched 1 open row(s) | WHERE: closes corr=a1cd68e152
+- [2026-10-31T12:53:38Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a9ad2b40ddcfc1d27, matched 1 open row(s) | WHERE: closes corr=a9ad2b40dd
+- [2026-10-31T12:54:58Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 0ced412 corr=aa1c5554c90b68566 | WHEN: spawn | HOW: awaiting terminal state
+- [2026-10-31T13:06:27Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=aa1c5554c90b68566, matched 1 open row(s) | WHERE: closes corr=aa1c5554c9
+- [2026-10-31T13:12:14Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 0ced412 corr=ae73270cb6e608184 | WHEN: spawn | HOW: awaiting terminal state
+- [2026-10-31T13:20:33Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=ae73270cb6e608184, matched 1 open row(s) | WHERE: closes corr=ae73270cb6
```
```
$ stat -f '%N mtime=%Sm birth=%SB' -t '%H:%M:%S' STATUS.md DECISION_LOG.md HANDOFF.md docs/reports/2026-10-31-o78-*.md
STATUS.md mtime=08:42:03 birth=08:42:03
DECISION_LOG.md mtime=08:42:03 birth=08:42:03
HANDOFF.md mtime=08:42:03 birth=08:42:03
docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md mtime=09:11:53 birth=08:42:52
docs/reports/2026-10-31-o78-worker1-symmetry.md mtime=09:07:53 birth=08:48:28
docs/reports/2026-10-31-o78-worker2-slippage-unit.md mtime=09:07:53 birth=08:53:24
docs/reports/2026-10-31-o78-worker3-adversarial.md mtime=09:06:16 birth=09:06:16
docs/reports/2026-10-31-o78-worker4-report-adversarial.md mtime=09:20:17 birth=09:20:17
```

## Adversarial findings

W3, on the worker reports and the manager's synthesis (full table in `docs/reports/2026-10-31-o78-worker3-adversarial.md`):

| F | Target | Severity | Disposition |
|---|---|---|---|
| F1 | Synthesis: "20× heavier relative to P&L" | MAJOR | **Accepted.** H6 now says commission is 20× heavier, slippage 25× lighter, total 2.6× (E6). |
| F2 | Synthesis: short loss "entirely" costs | MAJOR | **Accepted.** H6 is reframed as an accounting identity; H9 added. |
| F3 | W2: TotalSlippage unit-dependent | MAJOR | **Accepted.** Withdrawn; B4.5 and readback 4 amended (E9). |
| F4 | W1: no engine/data-divergence hypothesis | MAJOR | **Accepted.** H9 added; H2 weakened. |
| F5 | W1: "shorts trigger easier" | MINOR | **Accepted.** A1 row 2. |
| F6 | W1: algebra labelled OBSERVED; elided commands | MINOR | **Accepted.** A1 row 1 relabelled; correction note on W1. |
| F7 | W2: type mapping labelled OBSERVED | MINOR | **Accepted.** Correction note on W2. |
| F8 | W2: understated largest-winner match | MINOR | **Accepted.** Re-verified (E6); NEEDS AMEAR 2. |
| F9 | Import file: Saturday 2024-01-20 bar at 3,100 | MINOR | Reported. Under H9 and NEEDS AMEAR 6. |

W4 (adversarial on this report, `docs/reports/2026-10-31-o78-worker4-report-adversarial.md`): VERDICT SURVIVED-WITH-CORRECTIONS. All 12 findings accepted:
- **W4-1 (MAJOR):** Bottom line 1 contradicted A1 row 2 and H3/H4. Rewritten.
- **W4-2 (MAJOR):** the rescued RTH template is 08:30–16:00 Eastern. Added as H9(d), with the REPORTED Fusion counter-evidence, and added to NEEDS AMEAR 1.
- **W4-3 (MAJOR):** the Saturday rows were understated: 127 rows on 66 dates, not 6. H9(c) and NEEDS AMEAR 6 fixed.
- **W4-4 to W4-12 (MINOR):**
  - the 597–599 count;
  - E8's four-backtick fence;
  - E7's observer note;
  - E10's stat paste;
  - B2's condition;
  - H5's run-3/run-4 split;
  - "Exit on session close" in H4 and NEEDS AMEAR 2;
  - the six checks listed;
  - B1's INFERRED type label.

**Negative tests.**
- The extreme-trade gate does discriminate. The $20/pt arm returns `False` for all five trades while the $1/pt arm returns `True` (E5); both arms fired.
- The unit-twin check fires positive on `TotalNetProfitValue` and negative on `TotalSlippageValue` in the same files (E9).

## Files staged

```
$ git diff --cached --name-status -- 'docs/reports/2026-10-31-o78*'
A	docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md
A	docs/reports/2026-10-31-o78-worker1-symmetry.md
A	docs/reports/2026-10-31-o78-worker2-slippage-unit.md
A	docs/reports/2026-10-31-o78-worker3-adversarial.md
A	docs/reports/2026-10-31-o78-worker4-report-adversarial.md
```

## Report contract

`scripts/gate-manager-output.sh` requires a `Result:` token from PASS/FAIL/BLOCKED, and the brief asks for `Result: DONE` as the last line. Both are given:
- The token below is the manager's six-step stress-test outcome. It is not a grade; the auditor grades.
- The last line is the brief's.

Stress-test Result: PASS. The six checks:
(1) worker report files read;
(2) verification re-run by the manager (E5, E6);
(3) diff and scope read (E10, Files staged);
(4) adversarial workers W3 and W4;
(5) negative tests fired both arms;
(6) every claim rests on output captured this session.
W3 returned VERDICT BROKEN on the pre-correction synthesis; F1/F2 were accepted and corrected. W4 returned VERDICT SURVIVED-WITH-CORRECTIONS; all 12 findings, W4-1 to W4-12, were dispositioned.

Result: DONE

## Audit-1 corrections (2026-10-31)

Append-only correction for audit 1 (FAIL on S1, strike one on `Praxis_build-o78`). Lines 1–494 above are unchanged. The best reading (B1, bottom line 2) is not touched. Bottom line 3 (`:42`) is RESTATED here, not deleted, as a bounded negative:

**No NT8 text defining "Total slippage" or naming the order types the Slippage field applies to was found in the SEARCHED SET: (a) this repo; (b) the rescued NT8 tree's `*.cs *.resx *.xml *.txt` files; (c) the strings of the compressed `NinjaTrader.Install.msi`. The interior of the MSI and of the 103 rescued DLLs (none is `NinjaTrader.Core.dll`) is CANNOT-DETERMINE-STATICALLY: no extraction tool is present.**

Precision notes on that sentence, from the output in C2–C5 below:
- "103 rescued DLLs" counts the whole rescue root, `/Users/admin/VM-Rescue-2026-09-29`. Only 39 of them are under `NinjaTrader 8-full`, and 44 are a Fontforge `bin` directory that is not NT8. No `NinjaTrader.Core.dll` exists anywhere under the rescue root (C3).
- "(b) the rescued NT8 tree" means `NinjaTrader 8-full`, the tree named in the brief. The sibling tree `NinjaTrader 8` (the one holding `bin/Custom/NinjaTrader.Custom.dll`) was searched the same way. It returns the same two Analyzer logs and nothing else (C2).
- "(c) the strings of the MSI" means `strings -a`, which reads 8-bit runs only. UTF-16 text inside the MSI was not searched. That is part of the CANNOT-DETERMINE interior.

All commands below were run 2026-10-31 at about 13:30Z by the manager, with no workers. `grep` on this host is a ugrep wrapper. Where the result could depend on that, `/usr/bin/grep` was run as well.

**C1. Repo.** This unit's own reports (`2026-10-31-o78*`) are excluded by the `grep -v`, because they quote the phrase. This section also quotes it, and it sits inside an excluded file. The command is the brief's, with `| cut -c1-150` added so each line fits the paste. The hit count, without `head`, comes first.
```
$ grep -rn "Total slippage\|TotalSlippage" --include="*.md" --include="*.txt" --include="*.cs" /Volumes/Sensidine/Praxis.build | grep -v "2026-10-31-o78" | wc -l
      26
$ /usr/bin/grep -rn "Total slippage\|TotalSlippage" --include="*.md" --include="*.txt" --include="*.cs" /Volumes/Sensidine/Praxis.build | /usr/bin/grep -v "2026-10-31-o78" | wc -l
      26
$ grep -rn "Total slippage\|TotalSlippage" --include="*.md" --include="*.txt" --include="*.cs" /Volumes/Sensidine/Praxis.build | grep -v "2026-10-31-o78" | head -20 | cut -c1-150
/Volumes/Sensidine/Praxis.build/DECISIONS.md:290:3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a decision): does NT8 apply Slippage 
/Volumes/Sensidine/Praxis.build/STATUS.md:13:**2026-10-31 morning, update:** Amear reversed the overnight hold ("Run them now"); commits 2 and 3 lande
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:449:- [2026-10-30T22:17:00Z] WHO: praxis-master | WHO OBSERVED: praxis-master (image read); image supp
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:450:- [2026-10-30T22:22:00Z] **WHO: amear** | WHO OBSERVED: amear (his screenshots; the master saw onl
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:455:- [2026-10-30T22:52:00Z] WHO: praxis-master | WHO COMMITTED: amear (typed) | WHAT: **`Praxis_build
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:463:- [2026-10-31T13:29:11Z] WHO: praxis-master | WHAT: **o78 AUDIT: FAIL — STRIKE ONE ON BEAD `Prax
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:464:- [2026-10-31T13:22:52Z] WHO: praxis-master | WHAT: **o78 RETURNED `Result: DONE`; AUDIT DISPATCHE
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:465:- [2026-10-31T12:40:24Z] WHO: praxis-master | WHAT: **7zq COMMITTED@0ced412 AND PUSHED — verifie
/Volumes/Sensidine/Praxis.build/.claude/state/handoff-latest.md:13:○ Praxis_build-o78 ● P1 Run-4 follow-up: why shorts lose while longs win (code-
/Volumes/Sensidine/Praxis.build/HANDOFF.md:29:3. **`Praxis_build-o78`** — short-side symmetry read + "Total slippage" unit from on-disk sources only
/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/project_instrument_def_grid_test.md:7:On o78 (2026-10-31), the "Total slippage 48.
/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-auditor/project_nt8_rescue_tree_bounds.md:11:- Strategy Analyzer log XMLs store summary st
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md:59:1,304 sits only 4 above B's lower bound of 1,300. Commission 
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-rulings-append.md:84:+3. Readback, open from `2026-10-30T22:22:00Z` (WHO: amear) (not a de
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-handtest-checklist.md:42:  NT's "Total slippage" figure ≈ trades × 4 / 100 ≤ **52.
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-handtest-checklist.md:51:| Commission · Profit factor · Max drawdown · Total slippag
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:94:| Total slippage | 48.44 | ____ | ____ |
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:178:| Total slippage | 48.44 | ____ |
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:195:| Net · PF · Max DD · Total slippage | ____ | ____ |
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:257:| Total slippage | 48.44 | ____ |
```
All 26 hits by file:line, without `head`. The order differs from the run above because the ugrep wrapper does not sort, so this one is piped through `sort`.
```
$ /usr/bin/grep -rn "Total slippage\|TotalSlippage" --include="*.md" --include="*.txt" --include="*.cs" /Volumes/Sensidine/Praxis.build | /usr/bin/grep -v "2026-10-31-o78" | cut -d: -f1-2 | sort
/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-auditor/project_nt8_rescue_tree_bounds.md:11
/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-manager/project_instrument_def_grid_test.md:7
/Volumes/Sensidine/Praxis.build/.claude/state/handoff-latest.md:13
/Volumes/Sensidine/Praxis.build/DECISIONS.md:290
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:449
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:450
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:455
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:463
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:464
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md:465
/Volumes/Sensidine/Praxis.build/HANDOFF.md:29
/Volumes/Sensidine/Praxis.build/STATUS.md:13
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-28-voice-session-notes.md:48
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-run3-backtest-screenshot-record.md:60
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-run3-backtest-screenshot-record.md:95
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-f3-artifact.md:242
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-f3-artifact.md:477
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-rulings-append.md:84
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-30-zyd-worker10-closing-adversarial.md:58
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:178
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:195
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:257
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-handtest-checklist.md:94
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-handtest-checklist.md:42
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-handtest-checklist.md:51
/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md:59
```
All 26 are `.md` files written by PRAXIS: ledgers, handoff, agent memory and reports. None is NT8 text.

**C2. Rescued NT8 trees, text files.**
```
$ grep -rln "Total slippage\|TotalSlippage\|lippage" --include="*.cs" --include="*.resx" --include="*.xml" --include="*.txt" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full" | head -20
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
[exit 0 0]
$ /usr/bin/grep -rln "Total slippage\|TotalSlippage\|lippage" --include="*.cs" --include="*.resx" --include="*.xml" --include="*.txt" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full" | head -20
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
[exit 0 0]
```
Sibling tree, same arguments (`S="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8"`):
```
$ ls "$S" | head
Config.xml
UI.xml
bin
db
strategyanalyzerlogs
templates
workspaces
$ /usr/bin/grep -rln "Total slippage\|TotalSlippage\|lippage" --include="*.cs" --include="*.resx" --include="*.xml" --include="*.txt" "$S" | head -20
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml
[exit 0 0]
```
The only hits are the two Analyzer run logs. They hold the settings and results of PRAXIS's own runs, not NT8's definitions (E4, E9, C6).

**C3. DLL inventory.**
```
$ find "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full" -name "*.dll" | wc -l
      39
$ find "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full" -name "NinjaTrader.Core.dll"
(no output)
[exit 0]
$ find "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full" -iname "*.dll" | wc -l
      39
$ find /Users/admin/VM-Rescue-2026-09-29 -iname "*.dll" | wc -l
     103
$ find /Users/admin/VM-Rescue-2026-09-29 -iname "NinjaTrader.Core.dll"
(no output)
$ find /Users/admin/VM-Rescue-2026-09-29 -iname "*.dll" | sed "s#/[^/]*$##" | sort | uniq -c | sort -rn | head
  44 /Users/admin/VM-Rescue-2026-09-29/files/Settings/Roaming-Weintek/EasyBuilder/Fontforge/EBproTmp/fontforge/bin
   5 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/tmp
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/zh-Hans
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/ru-RU
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/pt-PT
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/ko-KR
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/it-IT
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/fr-FR
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/es-ES
   2 /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/bin/Custom/de-DE
```
The brief expected 103 under `NinjaTrader 8-full`. The count there is 39. The 103 matches the rescue root, and W2's "dlls scanned: 103" (W2 `:109`). `NinjaTrader.Core.dll` is absent at both scopes.

**C4. Extraction and decompile tools.**
```
$ for t in 7z 7za cabextract msiextract ilspy ilspycmd mono dotnet; do printf "%s: " "$t"; command -v "$t" || echo none; done
7z: none
7za: none
cabextract: none
msiextract: none
ilspy: none
ilspycmd: none
mono: none
dotnet: none
```

**C5. The MSI.**
```
$ find /Users/admin/VM-Rescue-2026-09-29 -name "*.msi" | head
/Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi
$ ls -la /Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi
-rw-r--r--@ 1 admin  staff  85770240 Jul  9 10:33 /Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi
$ file /Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi
/Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi: Composite Document File V2 Document, Little Endian, Os: Windows, Version 6.2, MSI Installer, Code page: 0, Title: Installation Database, Subject: NinjaTrader 8.1.7.2, Author: NinjaTrader, LLC, Keywords: 88a3ff132587a1811cb2ed42a54cd2564b2eca95, Comments: This installer database contains the logic and data required to install NinjaTrader., Template: x64;1033, Revision Number: {637E6686-C37C-4A1F-A17E-E70FFBC52747}, Create Time/Date: Tue Jun 16 17:01:12 2026, Last Saved Time/Date: Tue Jun 16 17:01:12 2026, Number of Pages: 500, Number of Words: 2, Name of Creating Application: WiX Toolset (6.0.2.0), Security: 2
$ strings -a /Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi | grep -c "lippage"
0
[exit 0 1]
$ strings -a /Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi | grep "lippage" | head -20
(no output)
[exit 0 1 0]
```
`file` reports a WiX-built MSI (a Composite Document File). Its payload is not readable with any tool found in C4. So zero `strings` hits bounds only the 8-bit strings of the container. It does not bound the files inside.

**C6. E9 correction: the `TotalSlippage` field is present.** E9's `grep -c '<TotalSlippage>'` returned 0 because it looked for an XML tag. The log stores summary fields pipe-delimited.
```
$ grep -c "TotalSlippage" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml"
5
$ grep -o "|TotalSlippage;[^|]*|" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_07_17_01.xml" | head -5
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
$ grep -c "TotalSlippage" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml"
5
$ grep -o "|TotalSlippage;[^|]*|" "/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/strategyanalyzerlogs/@@@PraxisNoiseAreaBreakout_2026_08_29_27.xml" | head -5
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
|TotalSlippage;0;0;0|
```
`TotalSlippage` appears on 5 lines in each log. Every value is `0;0;0`, which matches both logs' `<Slippage>0` (E9). E9's `TotalNetProfitValue=5` and `TotalSlippageValue=0` columns are unaffected. So is B4.5's "no `TotalSlippageValue` twin". Only the `TotalSlippage=0` column was wrong.

**What changes and what does not.** UNCHANGED by this correction:
- A1 symmetry (no long/short code asymmetry);
- B1 and bottom line 2, the best reading, which stays INFERRED;
- B4.4, honoured-on-every-fill, which stays UNVERIFIED;
- `## NEEDS AMEAR` readbacks 1–6.

SUPERSEDED:
- bottom line 3 (`:42`) and B4.2's "has **no NT8 source on disk**" (`:112`, E7's negative), superseded by the bounded negative at the top of this section;
- E9's `TotalSlippage=0` column (`:397-398`), superseded by C6's count of 5 per log.

Result: CORRECTED
