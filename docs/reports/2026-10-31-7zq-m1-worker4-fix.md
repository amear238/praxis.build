# 7zq M1 — worker 4 FIX report

**Task:** fix defects D1–D12 (manager's numbering of `docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md`) in
A `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`, B `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`,
C `docs/reports/2026-10-31-7zq-handtest-checklist.md`, D `docs/reports/2026-10-31-7zq-decisions-scope.md`.
**Mode:** BUILD (fix). **Date:** 2026-10-31. **Unit:** Praxis_build-7zq M1, worker 4.
**Criterion:** the worker-3 defect list; SPEC_RUBRIC S1 (citations), S2 (claim scope), S8 (no answers for Amear); brief D2 (BandOrVWAP exactly base behaviour).

Nothing compiled or run (no NT8 on the Mac). Nothing staged. Files touched: A, B, C, D, and this report. Base `.cs` not touched (hash below).

## Process log

1. Read the worker-3 report, `diff -u` base→A and base→B, C and D in full.
2. Checked sources before citing them:
   - Spec `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (OBSERVED, `sed -n 30,40p;47,60p`):
     - L34 `## 2. Breakout trigger — PAPER-VERIFIED (§3, p. 9)`
     - L38 `- **Positions per session:** **NOT capped at one.** A position is held until the close or until price crosses to the **opposite** boundary, at which point it is closed **and reversed** … (p. 9). … 1.3 trades/day (base opp-band stop) … 1.8 … (Table 4, p. 16). Stops, too, are evaluated only at the semi-hourly stamps (p. 9).`
     - L49 `| Stop / exit variants tested | (a) opposite band; (b) max(VWAP, band); (c) = (b) + vol-target sizing | Tables 1–3, pp. 11–15 |`
     - L57 `## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)`
     - L59 `- **Base stop:** trailing stop at the **opposite** Noise-Area boundary (… base model = "Stop @ Opp. Band", Table 1). Evaluated only at semi-hourly stamps.`
   - 3gm `docs/reports/2026-10-30-3gm-fidelity-check.md` (OBSERVED, grep):
     - `73:| R2 | §A L17 — Lookback 14, fixed | spec L31, L46 · §3 p. 6 | 73,74 | FAITHFUL |`
     - `83:| R12 | §A L27 — reversal via NT8 managed reverse | spec L38 · §3 p. 9 | 106,107; 222,229 | CANNOT-DETERMINE-STATICALLY |`
     - `85:| R14 | §A L29 — OppBand exit | spec L38, L49, L59 · §3 p. 9 / Table 1 | 44,46; 205,220 | DEVIATION (unauthorised) |`
     - `92:| R21 | §C L53 — reversal; exit + reverse on the same bar | spec L38, L62 · §3 p. 9 | 203,229 | CANNOT-DETERMINE-STATICALLY |`
     - `850:- **R2. Reversals.** Trades tab: any Qty > 1, …` (readback list; the brief said ~:851, the line is **:850**)
     - `852:- **R4. Template hours.** …`; `:692` "Template hours were never captured."; `728: S2`, `729: S3`.
   - D9: `docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md:25-26` and `:153-165` cite `@StrategyGenerator.cs:1800-1826` using `Data.SessionIterator` / `ActualSessionEnd`; `ls` confirms the three rescued folders `/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8`, `…-after-analyzer`, `…-full` exist (OBSERVED). I did not re-open StrategyGenerator.cs myself; the line range is as worker 1 reports it.
   - D10: `ls docs/reports/2026-10-31-7zq-*` shows no `…-worker2-checklist-scope.md` (OBSERVED).
   - Base line numbers cited in D's new change lists (`:44-46, :101, :102, :108, :118, :188, :204, :207, :208, :215, :216, :225, :299`) re-read with `sed -n` on the base (OBSERVED; they match).
3. Edits made with the Edit tool only. The `.cs` edits are comments plus the two D2 code lines.
4. Stale-phrase scan over A/B/C/D for `no NT8 help`, `R2/R12`, `exactly like the base`, `exactly as the base`, `degenerate exception`, `§4 p.9 / Table`, the worker2 row, `short reverses at`: **0 hits** (pasted below).

## Defect → fix table (new file:line)

| # | Defect | Fix | New location |
|---|---|---|---|
| D1 | Flat1559 fills at the 16:00 bar's Open (~15:59 price); not stated | Kept the F2 statement verbatim and added the "Consequence: …" sentence. In C, replaced the "exit time 16:00" expectation with an Open-vs-Close exit-price readback for 3 FlatEOD rows (Data Box, 2-tick slippage). Added NEEDS AMEAR item, unanswered, no recommendation | B:34-35 (header), B:224-226 (flatten comment); C:203-204 (blockquote), C:224-229 (B.4), C:264-274 (B.5a table), C:298-301 (NEEDS AMEAR 6); D:37, D:39, D:51 (F2), D:65 (NEEDS AMEAR 7), D MANIFEST row for B (:72) |
| D2 | BandOrVWAP `vwapCumVol == 0` fallback changed | The two lines now read `: (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper)` / `? curUpper : curLower)`. The `double stop = …` lines are byte-identical to the base (diff shows them as context). Header paragraph replaced. C and D wording made consistent | A:233, A:241; A:34-35 header; C:129-131; D:30 |
| D3 | Unlabelled "still reverses correctly" | Appended the label. 3gm R12 (:83) and R21 (:92) are both CANNOT-DETERMINE-STATICALLY (verified) | A:249-251 |
| D4 | C:152 "a short reverses at Close < Lower" | Now "the long reverses to short at `Close < Lower` (a short exits at `Close >= Upper` and reverses to long at `Close > Upper`)" | C:154-155 |
| D5 | Paper "§4 p.9" | Now "§3 p. 9 / Table 1 … (as cited by 3gm R14; spec L57 heads its exit section '(§3, pp. 9–14)')". Spec lines pasted above | A:27-28 |
| D6 | "3gm R2" for reversals | C and D now say "3gm table rows R12/R21; reversal readback = 3gm readback R2 (NEEDS AMEAR, `…3gm-fidelity-check.md:850`)" | C:164-165; D:32 |
| D7 | 16:00 = last bar as fact | "INFERRED to be the session's last bar (pending 3gm readback R4, template hours; 3gm `:692`)" | D:34 |
| D8 | Change lists omit Description/comment edits | Added a "Non-logic edits" bullet per variant, and qualified "everything else byte-for-byte" | D:31 (A), D:36 (B), D:42 (both) |
| D9 | "No NT8 help on disk" too broad | Reworded to the brief's sentence, with the @StrategyGenerator.cs:1800-1826 cite | B:26-29; C:244-246; D:38 |
| D10 | Phantom worker2 row | Removed it. Added the worker4 and worker5 rows (worker5 marked "written after this draft") and a note that worker 2 delivered C and D but no sub-report. Manager row kept | D:78, D:79, D:81 |
| D11 | "Exactly like the base" on early-close days | Now "decision logic on that day is identical to the base; carried-in position/state can differ (INFERRED)" | B:37-40; C:240-242; D:38; D MANIFEST row B |
| D12 | Trade-count prediction read as fact | "Predicted trade count (INFERRED, not a fact): 1,211" plus the caveat that S2/S3 carries can change next-morning entries and reversals, so the count may differ | C:232-236 |

## Verification evidence (pasted output)

### Stale-phrase scan + fix locations
```
-- stale-phrase scan (expect no hits)
-- fix locations
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:27://   Paper: SSRN 4824172 §3 p. 9 / Table 1 "Stop @ Opp. Band" (as cited by 3gm R14; spec L57 heads
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:34:// BandOrVWAP mode is unchanged from the base, including the vwapCumVol == 0 fallback (same-side band).
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:233:					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:241:					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:250:			//     (INFERRED; same-bar exit+reverse resolution is CANNOT-DETERMINE-STATICALLY, 3gm R12/R21 —
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:26:// SESSION-AWARE API: no NT8 documentation of SessionIterator behaviour for this use was found;
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:34:// Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00,
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:38://   variant's decision logic on that day is identical to the base. The position/state carried into
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:224:			//      Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after
docs/reports/2026-10-31-7zq-decisions-scope.md:30:  - *Change:* `:209` `: curUpper` → `: (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper)` (long stop = L
docs/reports/2026-10-31-7zq-decisions-scope.md:31:  - *Non-logic edits (strings and comments):* the `Description` string (base `:101`, a VARIANT sentence appended); `Name
docs/reports/2026-10-31-7zq-decisions-scope.md:32:  - *Consequence (INFERRED):* the long exit (`Close <= Lower`) coincides with the reversal trigger (`Close < Lower`, `:2
docs/reports/2026-10-31-7zq-decisions-scope.md:34:  - *Why:* 3gm D2(c), CANNOT-DETERMINE-STATICALLY, scenarios S1–S5. The base's FlatEOD market exit is submitted on the
docs/reports/2026-10-31-7zq-decisions-scope.md:36:  - *Non-logic edits (strings and comments):* the `Description` string (base `:101`, a VARIANT sentence appended); `Name
docs/reports/2026-10-31-7zq-decisions-scope.md:37:  - *Consequence:* the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00, INFERRED), one 
docs/reports/2026-10-31-7zq-decisions-scope.md:38:  - *Limits:* on early-close sessions ending before 15:59 ET the decision logic that day is identical to the base (backs
docs/reports/2026-10-31-7zq-decisions-scope.md:39:  - **This variant does not change the governing flat time.** It changes only when the exit order is submitted inside a 
docs/reports/2026-10-31-7zq-decisions-scope.md:51:- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. The governing flat time 
docs/reports/2026-10-31-7zq-decisions-scope.md:65:7. **Flat1559 fill price:** is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of t
docs/reports/2026-10-31-7zq-decisions-scope.md:78:| /docs/reports/2026-10-31-7zq-m1-worker4-fix.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 fix sub-report (worker4
docs/reports/2026-10-31-7zq-decisions-scope.md:79:| /docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 re-ADVERSARIA
docs/reports/2026-10-31-7zq-decisions-scope.md:81:Note: worker 2 delivered the checklist and this draft but no sub-report (it hit its turn cap before writing one), so the
docs/reports/2026-10-31-7zq-handtest-checklist.md:154:- A long now exits at `Close <= Lower`, and the long reverses to short at `Close < Lower` (a short
docs/reports/2026-10-31-7zq-handtest-checklist.md:165:  = 3gm readback R2 (NEEDS AMEAR, `docs/reports/2026-10-30-3gm-fidelity-check.md:850`)):** at a reversal stamp the
docs/reports/2026-10-31-7zq-handtest-checklist.md:203:> **Consequence:** the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00,
docs/reports/2026-10-31-7zq-handtest-checklist.md:232:- **Predicted trade count (INFERRED, not a fact): 1,211**, because the entry code is unchanged: the last
docs/reports/2026-10-31-7zq-handtest-checklist.md:241:  identical to the base**. The position/state carried into that day can differ, because earlier days
docs/reports/2026-10-31-7zq-handtest-checklist.md:244:  session-aware close (SessionIterator / ActualSessionEnd) was not used: no NT8 documentation of
docs/reports/2026-10-31-7zq-handtest-checklist.md:264:**B.5a — Exit-price check (3 FlatEOD rows).** Pick 3 FlatEOD rows from the Flat1559 run. For each, read
docs/reports/2026-10-31-7zq-handtest-checklist.md:298:6. **Flat1559 — fill price of the 16:00 flat.** File B's exit fills at the Open of the 16:00-stamped
docs/reports/2026-10-31-7zq-handtest-checklist.md:299:   bar, which is about a 15:59 price (INFERRED; B.5a tests it). Is a fill at the 16:00 bar's Open
$ C line refs
129:**defaults to OppBand**. The BandOrVWAP branch is unchanged, including its `vwapCumVol == 0` fallback
188:**Expected: identical to run 4 / your 0-S run, number for number** (INFERRED; the BandOrVWAP branch is
189:unchanged). If it differs, the variant changed more than the OppBand branch. **Stop and report the
```

### `diff -u ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs` (full)
```diff
--- ninjascript/PraxisNoiseAreaBreakout.cs	2026-07-16 15:39:15
+++ ninjascript/PraxisNoiseAreaBreakout_OppBand.cs	2026-10-31 06:25:09
@@ -15,6 +15,31 @@
 using NinjaTrader.Core.FloatingPoint;
 #endregion
 
+// ==============================================================================================
+// VARIANT of PraxisNoiseAreaBreakout.cs @ 719ab11 — bead Praxis_build-7zq, authorised by
+// DECISION_LOG 2026-10-31T00:46:43Z. TEST MATERIAL, NOT A RULING. NOT COMPILED (no NT8 on the Mac).
+//
+// CHANGE: the OppBand trailing stop is corrected to the paper's OPPOSITE band:
+//   long stop = LowerBound (curLower), short stop = UpperBound (curUpper).
+//   The base used the same-side band (base lines 209/217). That is recorded as DEVIATION
+//   (unauthorised) in docs/reports/2026-10-30-3gm-fidelity-check.md row R14.
+//   Spec: docs/specs/2026-07-16-b2-noise-area-ruleset.md L38/L49/L59.
+//   Paper: SSRN 4824172 §3 p. 9 / Table 1 "Stop @ Opp. Band" (as cited by 3gm R14; spec L57 heads
+//   its exit section "(§3, pp. 9–14)").
+// DEFAULT ExitMode = OppBand in this variant, so the mode under test runs without re-setting an input.
+// CONSEQUENCE (3gm Q2): with the opposite band, the OppBand exit condition (long: Close <= LowerBound;
+//   short: Close >= UpperBound) coincides with the reversal trigger (Close < LowerBound /
+//   Close > UpperBound). OppBand therefore becomes "reverse or hold to 16:00". A flat-only exit
+//   happens only at exact equality, Close == band (INFERRED, not run).
+// BandOrVWAP mode is unchanged from the base, including the vwapCumVol == 0 fallback (same-side band).
+//   The OppBand fallback in the ternary is mode-guarded, so only ExitMode == OppBand takes the opposite band.
+// Base Q2 stays OPEN for Amear.
+// ENUM DEPENDENCY: PraxisNoiseExitMode is declared ONCE, in PraxisNoiseAreaBreakout.cs. This variant
+//   reuses it, so it REQUIRES PraxisNoiseAreaBreakout.cs to stay installed in the same
+//   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
+// ---- Original base header follows, unchanged. ----
+// ==============================================================================================
+
 // PRAXIS B2 (bead Praxis_build-4uu) — NOISE-AREA BREAKOUT backtest Strategy.
 //
 // PURPOSE: faithful, self-contained NT8 Strategy Analyzer replication of the intraday
@@ -42,15 +67,13 @@
 namespace NinjaTrader.NinjaScript.Strategies
 {
 	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
-	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
-	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
-	public enum PraxisNoiseExitMode
-	{
-		OppBand,
-		BandOrVWAP
-	}
+	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
+	// This variant reuses it, so it REQUIRES PraxisNoiseAreaBreakout.cs to stay installed in the same
+	// Custom\Strategies folder. Re-declaring it here would be CS0101 (INFERRED, not compiled).
+	// OppBand    = base model, trailing stop at the OPPOSITE band (paper Table 1). DEFAULT in this variant.
+	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). Base default.
 
-	public class PraxisNoiseAreaBreakout : Strategy
+	public class PraxisNoiseAreaBreakout_OppBand : Strategy
 	{
 		#region Fixed session clock (trader-locked; not exposed)
 		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
@@ -98,8 +121,8 @@
 		{
 			if (State == State.SetDefaults)
 			{
-				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET.";
-				Name         = "PraxisNoiseAreaBreakout";
+				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET. VARIANT: OppBand stop at the OPPOSITE band (paper Table 1); default ExitMode=OppBand.";
+				Name         = "PraxisNoiseAreaBreakout_OppBand";
 
 				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
 				Calculate                                 = Calculate.OnBarClose;
@@ -115,7 +138,7 @@
 				// --- Paper-fixed parameters (spec §3): Lookback=14 and BandSigmaMult=1.0 are now
 				//     private consts (field region), not settable Inputs — Analyzer cannot vary them
 				//     (paper-fixed, not optimizable this pass — DECISION_LOG 2026-07-16). ---
-				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
+				ExitMode      = PraxisNoiseExitMode.OppBand;    // VARIANT 7zq default (base default BandOrVWAP, spec §4 p.13). The only knob.
 				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.
 
 				// Band / VWAP plots — purely for the Strategy-Analyzer visual reconcile (report §checklist).
@@ -201,20 +224,21 @@
 			MarketPosition mp = Position.MarketPosition;
 
 			// (1) TRAILING-STOP / EXIT — evaluated ONLY at the stamp (spec §4 p.9). Reversal (2) below
-			//     handles the opposite-band cross; this closes to FLAT on the same-side band/VWAP trail.
+			//     handles the opposite-band cross. This closes to FLAT on the trail: BandOrVWAP = same-side
+			//     band/VWAP trail; OppBand = opposite band (coincides with the reversal below, INFERRED).
 			if (mp == MarketPosition.Long)
 			{
-				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
+				// Long trailing stop: BandOrVWAP = max(UpperBound, VWAP) (spec §4 p.13); OppBand = LowerBound, the OPPOSITE band (paper Table 1; 3gm R14).
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Max(curUpper, curVwap) : curUpper;
+					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
 				if (price <= stop)
 					ExitLong("XL", "");
 			}
 			else if (mp == MarketPosition.Short)
 			{
-				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
+				// Short trailing stop: BandOrVWAP = min(LowerBound, VWAP) (spec §4 p.13); OppBand = UpperBound, the OPPOSITE band (paper Table 1; 3gm R14).
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Min(curLower, curVwap) : curLower;
+					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
 				if (price >= stop)
 					ExitShort("XS", "");
 			}
@@ -222,7 +246,9 @@
 			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
 			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
 			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
-			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
+			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly
+			//     (INFERRED; same-bar exit+reverse resolution is CANNOT-DETERMINE-STATICALLY, 3gm R12/R21 —
+			//     in OppBand mode this co-occurs on every reversal).
 			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
 				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
 			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
@@ -296,7 +322,7 @@
 		// They live as private consts (see field region) so the Strategy Analyzer cannot vary them.
 
 		[NinjaScriptProperty]
-		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-side band; BandOrVWAP = max/min(band, VWAP), the paper's PREFERRED model (spec §4 p.13). Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 1)]
+		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at the OPPOSITE band (paper Table 1), DEFAULT in this variant; BandOrVWAP = max/min(band, VWAP) (spec §4 p.13).", GroupName = "02. Praxis (tunable)", Order = 1)]
 		public PraxisNoiseExitMode ExitMode { get; set; }
 
 		[NinjaScriptProperty]
```

### `diff -u ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` (full)
```diff
--- ninjascript/PraxisNoiseAreaBreakout.cs	2026-07-16 15:39:15
+++ ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs	2026-10-31 06:25:20
@@ -14,6 +14,39 @@
 using NinjaTrader.NinjaScript;
 using NinjaTrader.Core.FloatingPoint;
 #endregion
+
+// ==============================================================================================
+// VARIANT of PraxisNoiseAreaBreakout.cs @ 719ab11 — bead Praxis_build-7zq, authorised by
+// DECISION_LOG 2026-10-31T00:46:43Z. TEST MATERIAL, NOT A RULING. NOT COMPILED (no NT8 on the Mac).
+//
+// CHANGE: the flatten decision moves from the 16:00-stamped bar (mod >= 960) to mod >= 959
+//   (FlattenMod = CloseMod - 1). The managed market exit is then submitted on the close of the
+//   15:59-stamped 1-min bar, so it fills at the 16:00 bar's open on the same day (INFERRED:
+//   Calculate.OnBarClose + end-stamped bars + next-bar-open fill; base behaviour is 3gm S1-S5).
+// SESSION-AWARE API: no NT8 documentation of SessionIterator behaviour for this use was found;
+//   NT-shipped source on disk uses it, but its behaviour here is UNVERIFIED (rescued NT8 user folder,
+//   e.g. @StrategyGenerator.cs:1800-1826, Data.SessionIterator / ActualSessionEnd). So this variant
+//   uses the hard-coded 15:59 ET fallback instead.
+//
+// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The
+// governing flat time stays 16:00 ET. The variant changes only WHEN the exit order is submitted
+// inside the backtest, so the fill lands the same day.
+// Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00,
+//   INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET.
+//
+// EARLY-CLOSE DAYS (INFERRED): a session that ends before 15:59 ET never reaches mod 959, so this
+//   variant's decision logic on that day is identical to the base. The position/state carried into
+//   that day can still differ, because earlier days flattened differently (INFERRED; 3gm S2/S3).
+//   There is no explicit flatten, only the
+//   IsExitOnSessionCloseStrategy backstop. An entry is still possible on the last bar if it falls on
+//   a :00/:30 stamp (3gm fidelity check :733, :842).
+// MISSING 15:59 BAR (no trades that minute): the 16:00 bar triggers the flatten, as in the base (INFERRED).
+// IsExitOnSessionCloseStrategy = true is kept as the backstop.
+// ENUM DEPENDENCY: PraxisNoiseExitMode is declared ONCE, in PraxisNoiseAreaBreakout.cs. This variant
+//   reuses it, so it REQUIRES PraxisNoiseAreaBreakout.cs to stay installed in the same
+//   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
+// ---- Original base header follows, unchanged. ----
+// ==============================================================================================
 
 // PRAXIS B2 (bead Praxis_build-4uu) — NOISE-AREA BREAKOUT backtest Strategy.
 //
@@ -42,20 +75,20 @@
 namespace NinjaTrader.NinjaScript.Strategies
 {
 	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
-	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
+	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
+	// This variant reuses it, so it REQUIRES PraxisNoiseAreaBreakout.cs to stay installed in the same
+	// Custom\Strategies folder. Re-declaring it here would be CS0101 (INFERRED, not compiled).
+	// OppBand    = base model, trailing stop at the same-side band the breakout came through (as in the
+	//              base; 3gm R14 DEVIATION, unchanged in this variant).
 	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
-	public enum PraxisNoiseExitMode
-	{
-		OppBand,
-		BandOrVWAP
-	}
 
-	public class PraxisNoiseAreaBreakout : Strategy
+	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
 	{
 		#region Fixed session clock (trader-locked; not exposed)
 		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
 		private const int OpenMod  = 9 * 60 + 30;   // 570
 		private const int CloseMod = 16 * 60;       // 960
+		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
 		#endregion
 
 		#region Per-day history store (completed sessions only — no look-ahead)
@@ -98,14 +131,14 @@
 		{
 			if (State == State.SetDefaults)
 			{
-				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET.";
-				Name         = "PraxisNoiseAreaBreakout";
+				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET. VARIANT: flat order submitted on the 15:59 bar so it fills 16:00 same session.";
+				Name         = "PraxisNoiseAreaBreakout_Flat1559";
 
 				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
 				Calculate                                 = Calculate.OnBarClose;
 				EntriesPerDirection                       = 1;
 				EntryHandling                             = EntryHandling.AllEntries;
-				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
+				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit flat (submitted 15:59) is primary
 				ExitOnSessionCloseSeconds                 = 30;
 				StartBehavior                             = StartBehavior.WaitUntilFlat;
 				TimeInForce                               = TimeInForce.Day;
@@ -186,7 +219,12 @@
 				Values[2][0] = curVwap;
 
 			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
-			if (mod >= CloseMod)
+			//      VARIANT 7zq: decided on the 15:59-stamped bar (mod >= FlattenMod), so the market exit
+			//      fills at the 16:00 bar's open (INFERRED). The governing flat time is unchanged at 16:00 ET.
+			//      Consequence: the exit fills at the Open of the 16:00-stamped bar (the first trade after
+			//      ~15:59:00, INFERRED), one minute earlier in price than a 16:00:00 close; the position is
+			//      still flat by 16:00 ET.
+			if (mod >= FlattenMod)
 			{
 				FlattenAll("16:00 session flat");
 				return;                          // never open a new position at/after the close
```

### Hashes, line counts, status
```
$ shasum -a 256
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
42df06faf65f65d9395c7d2e57b0c97c01a31642040052ba3380c10d955749cc  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
e6e508a659998d2c80121b159491627c5ac54f75b839c754bf55fe2820e03199  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
$ wc -l
     312 ninjascript/PraxisNoiseAreaBreakout.cs
     338 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
     350 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
    1000 total
$ git status --porcelain -- ninjascript/ docs/reports/ | grep 10-31
?? docs/reports/2026-10-31-7zq-decisions-scope.md
?? docs/reports/2026-10-31-7zq-handtest-checklist.md
?? docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md
?? docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md
?? docs/reports/2026-10-31-7zq-m1-worker4-fix.md
$ git status --porcelain -- ninjascript/
?? ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
?? ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
$ git diff --cached --name-only | grep -c '10-31\|ninjascript'
0
```
The base hash matches the required `35393823…2265`. The `.cs` files are absent from the `grep 10-31` view only because their names don't contain "10-31". The second command shows them. All are untracked and none are staged.

## Notes for the re-adversarial (worker 5)

- D2 trace (INFERRED, not compiled): BandOrVWAP with `vwapCumVol > 0` → `Math.Max/Min(...)` (base); BandOrVWAP with `vwapCumVol == 0` → inner ternary's false arm → `curUpper` (long) / `curLower` (short) = base. OppBand → `curLower` (long) / `curUpper` (short). The enum has only two members, so no third path exists.
- The 3 brief-dictated "Consequence" sentences are verbatim in B (×2), C (×1, blockquote) and D (×3: D:37, D:39, D:51).
- Not changed (out of scope / left as is): B's `Description` string still says "so it fills 16:00 same session". That is true for the bar stamp but silent on price. The brief's D1 targets the F2 statement, so I left the string alone to keep the edits minimal. C:202-204 ("should then fill at the **16:00 bar's open**, same day") is consistent with the consequence. Worker 3's out-of-scope findings (base has no MANIFEST row; DECISION_LOG rows 462-465 out of order) are not addressed here.
- UNVERIFIED: `@StrategyGenerator.cs:1800-1826`. I cite it from worker 1's report (pasted grep at worker1 :161-165) and did not re-open the file.

## NEEDS AMEAR (carried into C and D, unanswered)

- Is a fill at the 16:00 bar's Open (~15:59 price) acceptable as the backtest realisation of the 16:00 flat, or does he want another mechanism (e.g. a finer secondary series)? (C NEEDS AMEAR 6; D NEEDS AMEAR 7.) No recommendation made.

## Files staged

None. Modified (untracked): A, B, C, D. Created: this report.

## Result: PASS

D1–D12 are fixed in A/B/C/D and there are no stale-phrase hits. The base hash is unchanged. The `.cs` edits are comments plus the two D2 code lines. Nothing is staged, compiled or run.
