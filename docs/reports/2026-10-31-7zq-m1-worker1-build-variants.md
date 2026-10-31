# 7zq M1 — worker 1 — build two Noise-Area variants

## Task
Unit `Praxis_build-7zq` M1, worker 1. Create two NEW NinjaScript files, each a copy of
`ninjascript/PraxisNoiseAreaBreakout.cs` (@ 719ab11) with only the briefed edits:
`ninjascript/PraxisNoiseAreaBreakout_OppBand.cs` (File A) and
`ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` (File B).

## Mode
BUILD. Nothing staged, nothing committed (per the brief, the manager stages). No existing file modified.

## Criterion
Per the brief: each variant is byte-identical to the base except the listed edits; base hash unchanged;
the enum is not re-declared; every behaviour claim is labelled. NOT COMPILED: there is no NT8 on this Mac.

## Process log
1. Base checks: sha256 `35393823…2265` (matches the brief); 312 lines; `file` = "Unicode text, UTF-8 text";
   `xxd` starts `2372 6567` (`#reg`), so **no BOM**. CR count = 0, so **LF** endings. The file ends in `\n`.
   `git log -1` on the file = 719ab11.
2. Enum grep in `ninjascript/`: exactly one declaration, `PraxisNoiseAreaBreakout.cs:47`. `PraxisSignalConsumer.cs`
   has none.
3. NT8-help search (File B step 0). See the evidence below. **Finding: the brief's premise was partly wrong.**
   No NT8 help documentation (.chm/help) exists on disk. However, rescued NT8 *user folders* do exist at
   `/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8{,-full,-after-analyzer}`, and also under
   `/Volumes/PVM-Backup/...`. Their `bin/Custom` holds NT-shipped source that uses `Data.SessionIterator` and
   `ActualSessionEnd`, e.g. `Optimizers/@StrategyGenerator.cs:1800-1826` and `BarsTypes/@MinuteBarsType.cs:94-95`.
   That is a usage pattern, not documentation, and nothing was run. Per the brief, which says not to implement
   SessionIterator from memory and prescribes hard-coded edits B2/B3, I kept the **hard-coded fallback**. The
   header states truthfully that shipped source exists but the API's behaviour for this strategy is UNVERIFIED.
   **Routed up:** a session-aware version is now groundable in on-disk shipped source if Amear or the manager wants one.
4. Side observation (read-only): the rescued installed `bin/Custom/Strategies/PraxisNoiseAreaBreakout.cs`
   (both copies) has sha256 `c22f38fa…caa65`. That is not the base hash, but `diff --strip-trailing-cr` shows it is
   **identical modulo CR**: it is the base with CRLF endings (312 CRs). I matched the repo base (LF).
5. Citation check before writing the headers:
   - DECISION_LOG.md:464 carries `2026-10-31T00:46:43Z`, Amear's authorising row. Verified.
   - 3gm R14 = DEVIATION (unauthorised), at 3gm :63, :85, :361, :833. Verified. 3gm Q2 is at :858. Verified.
   - **Brief citation corrected:** the brief gives the spec as `docs/reports/2026-07-16-4uu-noise-area-strategy.md`
     L38/L49/L59, but those lines of that file are import/compile instructions and blank lines. The 3gm R14 section
     (:361-375) shows the lines come from **`docs/specs/2026-07-16-b2-noise-area-ruleset.md`** L38/L49/L59 ("opposite"
     boundary; "(a) opposite band"; "Stop @ Opp. Band"). File A cites the verified path.
   - **Brief citation corrected:** the brief gives the early-close notes as 3gm ":733, :845". Line 845 is blank; the
     early-close bullet is at **:842**. File B cites :733, :842.
6. Created both files with `cp -n` from the base, then made the Edit-tool changes listed in the hunk tables.
7. File A item 8 sweep. Grep for `same-side|same side|OppBand|opp. band|opposite|band only|PREFERRED|DEFAULT|curUpper|curLower`.
   Everything I found and fixed:
   - base L45 (enum-block comment) "OppBand = … same-side band": rewritten to OPPOSITE band, DEFAULT in this variant.
   - base L46 "… (§4 p.13). DEFAULT.": changed to "Base default.", because DEFAULT is OppBand in this file.
   - base L204 "closes to FLAT on the same-side band/VWAP trail": item 4.
   - base L207/L215 "OppBand mode = band only.": items 5 and 6.
   - base L299 Display Description: item 7.
   - Remaining after the fix, and correct: header L24 ("base used the same-side band", historical); L54 base
     header "opposite-band cross" (reversal, true); L224 "BandOrVWAP = same-side band/VWAP trail" (true); L244
     "cross to the OPPOSITE bound … flips" (reversal, true).
   - Left byte-identical, but flagged: base L225 (new L246) "an ExitLong above followed by Close<Lower still
     reverses correctly". In OppBand-opposite mode this same-bar ExitLong + EnterShort now happens on **every**
     reversal. How NT8 managed mode resolves it is CANNOT-DETERMINE-STATICALLY (3gm D3/R21/R12, :840). It already
     happened in the base, because Close<Lower implies Close<=Upper, so the frequency is not new. I did not change it.
8. **Deviation from the brief's literal claim, flagged:** the prescribed line-209/217 text
   (`? Math.Max(curUpper, curVwap) : curLower;` and its short counterpart) also changes the **BandOrVWAP fallback**
   for the case `vwapCumVol == 0`: the base fell back to the same-side band, the variant to the opposite band.
   So "BandOrVWAP mode unchanged" is not strictly true. I kept the prescribed code and qualified the header:
   "unchanged … with one degenerate exception … INFERRED unreachable on NQ RTH data". Making it exactly unchanged
   would need a restructured ternary (e.g. `ExitMode == BandOrVWAP ? (vwapCumVol > 0 ? max : curUpper) : curLower`),
   which is outside the allowed edits. **Manager's call.**
9. File B: FlattenMod const added; flatten check changed to `mod >= FlattenMod`; comments updated; line-108 comment
   updated (optional item 4, done). The base L196 checkpoint line (new L226, `mod < CloseMod`) is byte-identical,
   with no diff hunk there. It is now redundant for 959 but harmless: the 15:59 bar has Minute 59, so it is never a
   checkpoint anyway, and 960 is already caught by the flatten `return`.
10. File B line-order check (static, from source): `today.Closes[mod] = Close[0]` (L196), `if (mod == CloseMod)
    today.Close1600 = …` (L197-198), VWAP accumulation and `BuildBand(mod)` all come **before** the flatten check
    (L219). So on both the 15:59 and 16:00 bars the minute close, Close1600, VWAP and the band are recorded before
    the `return`, exactly as in the base. History and band inputs are unaffected (STATIC by line order; the runtime
    effect is INFERRED).
11. In File B's enum-comment block I kept the base L45 OppBand meaning (same-side) and appended "(as in the base;
    3gm R14 DEVIATION, unchanged in this variant)". This is an addition beyond "keep the meaning". It is comment-only.

### Behaviour notes (none run; all labels apply)
- File A: with the opposite band, the OppBand exit coincides with the reversal trigger. A flat-only exit happens only at
  `Close == band` exactly (INFERRED).
- File B: FlatEOD is submitted on the 15:59-stamped bar's close and fills at the 16:00 bar's open, same day (INFERRED).
  Whether NT8's `IsExitOnSessionCloseStrategy` / `ExitOnSessionCloseSeconds = 30` exit *also* fires, or how it interacts
  with the 15:59 FlatEOD (a 3gm-S4 analogue), is CANNOT-DETERMINE-STATICALLY.
- File B on the 16:00 bar: `mod >= 959` still holds, so FlattenAll runs again. If the 15:59 exit has filled, the position
  is flat and this is a no-op (INFERRED). If it has not filled, the managed-mode handling of a second ExitLong("FlatEOD")
  is CANNOT-DETERMINE-STATICALLY.
- File B early-close days and a missing 15:59 bar: as the header says (INFERRED).
- File B: the `return;` comment "never open a new position at/after the close" is byte-identical. It now also covers
  the 15:59 bar, which is never a checkpoint, so no entry it used to allow is blocked (STATIC from L226). Wording left as is.

## Verification evidence

### NT8-help search (File B step 0)
First run, `find ~ -maxdepth 5 -iname '*ninjatrader*' 2>&1 | head -50`: all 50 lines it showed were bfs
`Operation not permitted` lines, e.g.:
```
== find ~ ninjatrader ==
bfs: error: /Users/admin/.Trash: Operation not permitted.
bfs: error: /Users/admin/Pictures/Photos Library.photoslibrary: Operation not permitted.
bfs: error: /Users/admin/Library/com.apple.aiml.instrumentation: Operation not permitted.
... (47 more of the same form; head -50 cut off before any match)
== find /Applications /Library ninjatrader ==
bfs: error: /Library/Caches/com.apple.amsengagementd.classicdatavault: Operation not permitted.
... (permission errors only, no matches)
== grep SessionIterator repo ==
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:661:$ /usr/bin/grep -nE 'Unrealized|Realized|Commission|Slippage|Fill|AvgPrice|Bars\.IsLastBarOfSession|IsLastBarOfSession|SessionIterator|ActualSessionEnd' ninjascript/PraxisNoiseAreaBreakout.cs
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md:667:- A wider probe (`Unrealized|Realized|Commission|Slippage|Fill|AvgPrice|IsLastBarOfSession|SessionIterator|ActualSessionEnd`) returns **no lines**.
== grep ActualSessionEnd repo ==
./docs/reports/2026-10-30-3gm-worker2-timing-orders-count.md
== file/CRLF ==
0
```
Rerun with permission-error lines filtered (errors still merged with 2>&1, then grep -v):
```
== find ~ -maxdepth 5 -iname '*ninjatrader*' (permission-error lines filtered) ==
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-after-analyzer
/Users/admin/VM-Rescue-2026-09-29/files/Installers/NinjaTrader.Install.msi
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/cache/NinjaTrader-v8.1-2483f6d5.Reflection.dat
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/cache/NinjaTrader.Vendor-v8.1-eb3190f5.Reflection.dat
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/cache/NinjaTrader.Core-v8.1-a62978b.Reflection.dat
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/cache/NinjaTrader.Gui-v8.1-9219b7dd.Reflection.dat
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/NinjaTrader.sqlite.bak_praxis
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/NinjaTrader.sqlite.bak_praxis2
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/db/NinjaTrader.sqlite
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/db/NinjaTrader.sqlite.bak_praxis
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/db/NinjaTrader.sqlite.bak_praxis2
/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/db/NinjaTrader.sqlite
rc-pipe done
== find /Applications /Library /opt -maxdepth 4 ==
== find /Volumes/Sensidine -maxdepth 4 ==
== mdfind ==
/Volumes/Sensidine/Praxis.build/Redemtion/Research Results/2nd round/Building a Resilient Bridge_ An n8n-to-NinjaTrader Pipeline for Prop Firm Traders Prioritizing Compliance and Maintenance Over Latency.md
/Volumes/PVM-Backup/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/templates/Commission/NinjaTrader Brokerage Monthly.xml
... (templates/skins/tmp resources; full list in session transcript)
/Volumes/PVM-Backup/VM-Rescue-2026-10-11/files/Users/amearbani-ahmad/Documents/NinjaTrader 8
```
Help-file and SessionIterator probe inside the rescued folder (read-only):
```
== help/doc files ==
== SessionIterator in .cs ==
./NinjaTrader 8/bin/Custom/SuperDomColumns/@Volume.cs
./NinjaTrader 8/bin/Custom/Indicators/@FibonacciPivots.cs
./NinjaTrader 8/bin/Custom/Indicators/@CamarillaPivots.cs
./NinjaTrader 8/bin/Custom/Indicators/@VolumeProfile.cs
./NinjaTrader 8/bin/Custom/Indicators/@BarTimer.cs
./NinjaTrader 8/bin/Custom/Indicators/@PriorDayOHLC.cs
./NinjaTrader 8/bin/Custom/Indicators/@CurrentDayOHL.cs
./NinjaTrader 8/bin/Custom/Indicators/@Correlation.cs
./NinjaTrader 8/bin/Custom/Indicators/@Pivots.cs
./NinjaTrader 8/bin/Custom/MarketAnalyzerColumns/@ChartNetChange.cs
./NinjaTrader 8/bin/Custom/MarketAnalyzerColumns/@DaysUntilRollover.cs
./NinjaTrader 8/bin/Custom/Optimizers/@StrategyGenerator.cs
./NinjaTrader 8/bin/Custom/BarsTypes/@RangeBarsType.cs
./NinjaTrader 8/bin/Custom/BarsTypes/@MinuteBarsType.cs
... (head -20)
== ActualSessionEnd in .cs ==
./NinjaTrader 8/bin/Custom/Optimizers/@StrategyGenerator.cs:1820:					startTimeForLongExits		= sessionIterator.ActualSessionEnd.AddMinutes(-(SessionMinutesOffsetForLongExits + SessionMinutesForLongExits));
./NinjaTrader 8/bin/Custom/BarsTypes/@MinuteBarsType.cs:94:				if (bars.TradingHours.Sessions.Count > 0 && barTimeStamp > SessionIterator.ActualSessionEnd) // Cut last bar in session down to session end on odd session end time
(+ @FibonacciPivots/@CamarillaPivots/@VolumeProfile/@Pivots storedSession.ActualSessionEnd)
--- @StrategyGenerator.cs grep -n -i sessionIterator (excerpt)
1305:		private		Data.SessionIterator				sessionIterator;
1800:					sessionIterator = new(strategy.BarsArray[0]);
1801:					sessionIterator.GetNextSession(strategy.Times[0][0], true);
1820:					startTimeForLongExits		= sessionIterator.ActualSessionEnd.AddMinutes(-(SessionMinutesOffsetForLongExits + SessionMinutesForLongExits));
--- rescued installed copy vs repo base
c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65  NinjaTrader 8/bin/Custom/Strategies/PraxisNoiseAreaBreakout.cs
c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65  NinjaTrader 8-full/bin/Custom/Strategies/PraxisNoiseAreaBreakout.cs
$ diff --strip-trailing-cr ninjascript/PraxisNoiseAreaBreakout.cs ".../NinjaTrader 8/bin/Custom/Strategies/PraxisNoiseAreaBreakout.cs" && echo "IDENTICAL modulo CR"
IDENTICAL modulo CR
312
```
Conclusion: there is no NT8 help documentation on disk, but there is NT-shipped source that uses SessionIterator.
Session-aware APIs remain UNVERIFIED for this strategy, so File B uses the hard-coded fallback.

### Hashes, line counts, encoding, enum, order, status (post-build)
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
82b78a82674421fa6b2285db5cc661c5b6883f73dd7192af411baedabf55aeeb  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
0fe9810f5cd5b5493bf2d5db15518faceb6d48b199c1e8acbb3fbc636408469c  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
     336 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
     342 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
     990 total
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs: Unicode text, UTF-8 text, with very long lines (363)
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:  Unicode text, UTF-8 text, with very long lines (370)
00000000: 2372 6567 696f 6e20 5573 696e 6720 6465  #region Using de
00000000: 2372 6567 696f 6e20 5573 696e 6720 6465  #region Using de
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:0
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:0
00000000: 0a7d 0a                                  .}.
--- enum decls in ninjascript/
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:73:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:70:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
--- File B order check
23://   (FlattenMod = CloseMod - 1). The managed market exit is then submitted on the close of the
86:		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
197:				today.Close1600 = Close[0];
217:			//      VARIANT 7zq: decided on the 15:59-stamped bar (mod >= FlattenMod), so the market exit
219:			if (mod >= FlattenMod)
221:				FlattenAll("16:00 session flat");
226:			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
315:		private void FlattenAll(string reason)
--- porcelain
?? ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
?? ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
```
(The "very long lines" note comes from the lengthened Description strings; the base already had long lines, at
lines 101 and 299. The "0" lines are CR counts: no CRLF.)

**Base hash unchanged:** `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` before and after.
`git status --porcelain -- ninjascript/` shows only the two new untracked files. The base and PraxisSignalConsumer.cs
are not modified.

### `diff -u ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`
```diff
--- ninjascript/PraxisNoiseAreaBreakout.cs	2026-07-16 15:39:15
+++ ninjascript/PraxisNoiseAreaBreakout_OppBand.cs	2026-10-31 06:11:56
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
+//   Paper: SSRN 4824172 §4 p.9 / Table 1 "Stop @ Opp. Band".
+// DEFAULT ExitMode = OppBand in this variant, so the mode under test runs without re-setting an input.
+// CONSEQUENCE (3gm Q2): with the opposite band, the OppBand exit condition (long: Close <= LowerBound;
+//   short: Close >= UpperBound) coincides with the reversal trigger (Close < LowerBound /
+//   Close > UpperBound). OppBand therefore becomes "reverse or hold to 16:00". A flat-only exit
+//   happens only at exact equality, Close == band (INFERRED, not run).
+// BandOrVWAP mode in this file is unchanged from the base, with one degenerate exception: if
+//   vwapCumVol == 0 at a checkpoint (no volume since 09:30), the ternary's fallback is now the opposite
+//   band, where the base fell back to the same-side band. INFERRED unreachable on NQ RTH data; not run.
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
+					? Math.Max(curUpper, curVwap) : curLower;
 				if (price <= stop)
 					ExitLong("XL", "");
 			}
 			else if (mp == MarketPosition.Short)
 			{
-				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
+				// Short trailing stop: BandOrVWAP = min(LowerBound, VWAP) (spec §4 p.13); OppBand = UpperBound, the OPPOSITE band (paper Table 1; 3gm R14).
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Min(curLower, curVwap) : curLower;
+					? Math.Min(curLower, curVwap) : curUpper;
 				if (price >= stop)
 					ExitShort("XS", "");
 			}
@@ -296,7 +320,7 @@
 		// They live as private consts (see field region) so the Strategy Analyzer cannot vary them.
 
 		[NinjaScriptProperty]
-		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-side band; BandOrVWAP = max/min(band, VWAP), the paper's PREFERRED model (spec §4 p.13). Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 1)]
+		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at the OPPOSITE band (paper Table 1), DEFAULT in this variant; BandOrVWAP = max/min(band, VWAP) (spec §4 p.13).", GroupName = "02. Praxis (tunable)", Order = 1)]
 		public PraxisNoiseExitMode ExitMode { get; set; }
 
 		[NinjaScriptProperty]
```

### `diff -u ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`
```diff
--- ninjascript/PraxisNoiseAreaBreakout.cs	2026-07-16 15:39:15
+++ ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs	2026-10-31 06:12:18
@@ -14,6 +14,34 @@
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
+// SESSION-AWARE API: UNVERIFIED. No NT8 help documentation was found on disk. NT-shipped source in a
+//   rescued NT8 user folder uses Data.SessionIterator / ActualSessionEnd, but its behaviour for this
+//   strategy has not been verified, so this variant uses the hard-coded 15:59 ET fallback instead.
+//
+// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The
+// governing flat time stays 16:00 ET. The variant changes only WHEN the exit order is submitted
+// inside the backtest, so the fill lands the same day.
+//
+// EARLY-CLOSE DAYS (INFERRED): a session that ends before 15:59 ET never reaches mod 959, so this
+//   variant behaves exactly as the base there. There is no explicit flatten, only the
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
@@ -42,20 +70,20 @@
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
@@ -98,14 +126,14 @@
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
@@ -186,7 +214,9 @@
 				Values[2][0] = curVwap;
 
 			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
-			if (mod >= CloseMod)
+			//      VARIANT 7zq: decided on the 15:59-stamped bar (mod >= FlattenMod), so the market exit
+			//      fills at the 16:00 bar's open (INFERRED). The governing flat time is unchanged at 16:00 ET.
+			if (mod >= FlattenMod)
 			{
 				FlattenAll("16:00 session flat");
 				return;                          // never open a new position at/after the close
```
(The File B hunk-1 alignment differs from File A's only in where diff places the blank line; the bytes have the same
structure: `#endregion`, blank, header, blank, original header.)

## Hunk-by-hunk mapping

### File A — `_OppBand.cs`
| Hunk | Content | Allowed edit |
|---|---|---|
| @@ -15,6 +15,31 @@ | New variant header block, inserted between `#endregion`+blank and the original header | A2 (+ shared enum note). Spec path corrected to the verified ruleset file (process log 5). The BandOrVWAP "unchanged" claim qualified with the vwapCumVol==0 exception (process log 8). |
| @@ -42,15 +67,13 @@ | Enum declaration (base 47-51) deleted; enum-dependency comment added; base L45 OppBand meaning → OPPOSITE; base L46 "DEFAULT" → "Base default"; class rename | Shared enum edit; A8 (L45/L46 semantic fixes); A1 (class) |
| @@ -98,8 +121,8 @@ | Description append; Name | A1 |
| @@ -115,7 +138,7 @@ | `ExitMode = PraxisNoiseExitMode.OppBand;` + comment | A3 |
| @@ -201,20 +224,21 @@ | base L204 comment (now 2 lines); L207 comment; L209 `: curLower`; L215 comment; L217 `: curUpper` | A4, A5, A6 |
| @@ -296,7 +320,7 @@ | Display Description (Name/GroupName/Order unchanged) | A7 |

### File B — `_Flat1559.cs`
| Hunk | Content | Allowed edit |
|---|---|---|
| @@ -14,6 +14,34 @@ | New variant header block (same placement as A) | B5 (+ shared enum note). The SessionIterator wording reflects the actual search result (process log 3). Early-close cite is :733/:842 (process log 5). |
| @@ -42,20 +70,20 @@ | Enum deleted + dependency comment; base L45 meaning kept with an "(as in the base; 3gm R14 …)" note; L46 kept verbatim; class rename; `FlattenMod` const | Shared enum edit (the L45 note is my addition, comment-only, process log 11); B1 (class); B2 (const) |
| @@ -98,14 +126,14 @@ | Description append; Name; line-108 comment | B1; B4 (optional, done) |
| @@ -186,7 +214,9 @@ | Flatten comment (+2 lines); `if (mod >= FlattenMod)` | B3 |

Not touched, as confirmed by the diff: base L196 `mod < CloseMod` (File B new L226), base L168-169 Close1600 bookkeeping,
the `return;` and its comment, FlattenAll, BandOrVWAP/OppBand code in File B, and all of File A's session clock.

## Files staged
None. The brief says the manager stages. New untracked files:
- `/Volumes/Sensidine/Praxis.build/ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`
- `/Volumes/Sensidine/Praxis.build/ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`
- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md` (this report)

## Result: PASS
Both files were built as briefed. The base hash is unchanged, nothing is staged, and the variants are NOT COMPILED.
For the manager:
1. The step-0 premise was wrong: NT-shipped SessionIterator source exists on disk. The fallback was kept.
2. The prescribed L209/L217 text changes the BandOrVWAP fallback when vwapCumVol==0. Disclosed in the header; your call.
3. Two brief citations were corrected: the spec path, and 3gm :845 → :842.
