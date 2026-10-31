# 7zq M1 — two Noise-Area variant strategies, hand-test checklist, scope draft (manager report)

Unit `Praxis_build-7zq`, phase M1 · manager: praxis-manager · 2026-10-31 · authorised by DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): "Run them now and I'll commit in the morning."

**Level of every deliverable (S2): WRITTEN. Not compiled, not tested.** There is no NT8 toolchain on this Mac. Compiling (F5) on the Fusion VM is Amear's step 1. Every behaviour claim here is INFERRED or CANNOT-DETERMINE-STATICALLY.

## Task

M1 builds two variants of `ninjascript/PraxisNoiseAreaBreakout.cs` (base @719ab11, unchanged). With them come a hand-test checklist (C) and a draft DECISIONS.md entry plus draft MANIFEST rows (D). D is a draft only: it is NOT appended to DECISIONS.md or MANIFEST.md. The vol-target variant is deliberately not built (it would pre-empt 3gm Q1). M2, the new strategy, is out of scope here.

## Rubric criteria addressed

S1, S2, S4, S6, S8. F2 (FROZEN, not decided). F3 (FROZEN; no backtest; the limitation sentence appears verbatim in Step 0). Wording is quoted in the brief; the rubric table is at `specs/SPEC_RUBRIC.md:107-114`.

## Deliverables (all staged with `git add`, one path at a time, never committed)

| ID | File | Status |
|---|---|---|
| A | `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs` | written, 338 lines |
| B | `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs` | written, 350 lines |
| C | `docs/reports/2026-10-31-7zq-handtest-checklist.md` | written |
| D | `docs/reports/2026-10-31-7zq-decisions-scope.md` | draft; the master appends it |
| E | this file | — |

## Workers dispatched (id, mode, outcome)

| # | Agent id | Mode | Outcome | Sub-report |
|---|---|---|---|---|
| 1 | a387dd8496cce7a08 | BUILD (A, B) | returned; both files written | `2026-10-31-7zq-m1-worker1-build-variants.md` |
| 2 | a4424e241caefe50b | BUILD (C, D) | **hit the 40-turn cap with no hand-back.** It did write C and D to disk, but no sub-report. C and D were then attacked by workers 3 and 5. | none (D notes this; no worker2 MANIFEST row) |
| 3 | ac47edf0c2d710508 | ADVERSARIAL (A–D) | `VERDICT: BROKEN`: 1 MAJOR, 10 MINOR | `2026-10-31-7zq-m1-worker3-adversarial.md` |
| 4 | a4148f055db30ec33 | BUILD (fix D1–D12) | returned; all 12 fixed | `2026-10-31-7zq-m1-worker4-fix.md` |
| 5 | a5c953c0c23e01e87 | ADVERSARIAL (re-attack) | `VERDICT: BROKEN`: 3 MINOR, all in D's MANIFEST block; A and B met every code criterion | `2026-10-31-7zq-m1-worker5-readversarial.md` |

That is 5 workers, which is the cap. Worker 5's three MINORs were one-line doc edits, so the manager fixed them directly (see Process log).

## Process log

1. **Base hash.** Matches the brief and commit 719ab11 (Evidence §1).
2. **Design decision forced by compilation (INFERRED, not compiled).** The base declares `public enum PraxisNoiseExitMode` at namespace level (base :47-51). NT8 compiles everything in `bin\Custom` into one assembly, so a byte copy would declare the type twice (CS0101).
   - Both variants therefore delete the enum declaration and reuse the base's copy.
   - Consequence: **each variant requires `PraxisNoiseAreaBreakout.cs` to stay installed.**
   - This puts hunks in the diff beyond the brief's literal allow-list (enum lines removed). The deviation is disclosed in both file headers, in C (A.2/B.2 compile-error instructions) and in D.
   - Worker 1 grepped `ninjascript/`: the base is the only declaration.
3. **Flat1559 design.** No NT8 documentation of SessionIterator / ActualSessionEnd behaviour was found. Worker 1 found NT-shipped source that uses them in rescued NT8 user folders. Their behaviour for this strategy is UNVERIFIED, so B uses the brief's fallback `mod >= CloseMod - 1` via a new constant `FlattenMod`.
4. **Worker 3's MAJOR (accepted).** B's market exit fills at the **Open of the 16:00-stamped bar**: the first trade after about 15:59:00, one minute earlier in price than a 16:00:00 close (INFERRED).
   - It is now stated in B (header + flatten comment), in C, and in D.
   - C gained an exit-price readback.
   - The question of whether that is acceptable is Amear's: C NEEDS AMEAR item 6, D item 7.
5. **Worker 3's MINOR #2 (accepted; code fix).** The first A ternary changed BandOrVWAP's `vwapCumVol == 0` fallback. Worker 4 made the fallback mode-guarded. Worker 5 traced all 8 cases (mode × vwapCumVol × side): BandOrVWAP equals the base in every case.
6. **The manager's own single-line edits** (pure doc and string changes, no logic):
   - B `Description` string: "fills 16:00" became "fills at the 16:00 bar's open (~15:59 price)".
   - D: the manager-report row is now marked "written after this draft".
   - D: the "D1–D12" cite was corrected to the manager's numbering.
   - D: the owed `zyd-rulings-append` row was moved back inside the table, above the Note paragraph. The Note is labelled "not a MANIFEST row".
   - All three D fixes are verified in Evidence §6.
7. **Premise drift (OBSERVED).** While M1 ran, Amear committed `4ec75ea` (commit 2) and `fab2855` (commit 3), both at 06:09 EDT. So the brief's check `git diff --cached --numstat` (expected `61 0 / 36 0 / 13 12`) now prints **nothing**: those changes are committed, not staged.
   - The equivalent proof is in Evidence §5. `git show --numstat 4ec75ea` shows exactly `61 0 DECISIONS.md`, `36 0 MANIFEST.md`, `13 12 config/backtest-cost-model.json`, so the audited content landed as audited.
   - `git diff --quiet HEAD --` over the protected files returns exit 0: the worktree equals HEAD.
8. **Brief citation corrections found by workers.**
   - Spec L38/L49/L59 are in `docs/specs/2026-07-16-b2-noise-area-ruleset.md`, not in the 4uu report.
   - The 3gm early-close note is at :842, not :845.
   - The paper section is §3 p.9 / Table 1, per 3gm R14 (the brief said §4).
   - 3gm readback R2 is at :850.
   - The files use the corrected cites.

## Verification evidence

Pasted outputs are in `## Evidence` at the end of this file. Summary of what was re-run by the manager in this session:
- base sha256 (unchanged)
- both full diffs
- `wc -l`
- `git status --porcelain`
- the protected-file check against commit `4ec75ea` and HEAD
- grep checks on D's fixes

Adversarial evidence, including worker 5's Python trace of the 8 ternary cases, is in the worker 3 and worker 5 reports. The S1 checks of C and D's citations (run-4 settings/baseline vs voice notes :32-54, DECISION_LOG timestamps, shas, rubric line ranges, F3 sentence verbatim) were done with pasted output in those reports.

**Negative test (step 5).** The only gate in M1's control is the protected-file constraint. Its trip condition, a protected path in the index or a worktree diff against HEAD, was checked directly and found clean (Evidence §5). The real gate on these files is the NT8 compile, and it cannot be tripped on this Mac: CANNOT-DETERMINE-STATICALLY. C tells Amear to stop and report the exact text of any F5 error, CS0101 included.

## Adversarial findings

- **Worker 3 (BROKEN, 11 defects).** 1 MAJOR: B's fill price. 10 MINOR, including:
  - the BandOrVWAP degenerate branch
  - an unlabelled reversal claim in A
  - a direction typo in C
  - a wrong paper section
  - a wrong R2 cite
  - "16:00 is last bar" stated as fact
  - incomplete change lists
  - "no NT8 help on disk" too broad
  - MANIFEST rows for nonexistent files
  - early-close "exactly like base"

  All were fixed by worker 4; worker 5 found 10 of 11 CLOSED and #10 partly open.
- **Worker 5 (BROKEN, 3 MINOR, D's MANIFEST block only).**
  1. A wrong "D1–D12" attribution.
  2. The owed zyd row sat outside the table.
  3. The manager-report row was not marked "written later".

  All three were fixed by the manager (Process log 6; Evidence §6). **No third adversarial pass was run on these three edits** because the 5-worker cap was reached. They are doc-only, and the master's auditor is the next check.
- **Confirmed by both adversaries, no break found:**
  - The same-bar ExitLong + EnterShort pair already exists in the base, in both modes (not new risk). In OppBand mode it now happens on every reversal. Its resolution is CANNOT-DETERMINE-STATICALLY (3gm R12/R21) and is labelled so in A and C.
  - B: no entry at or after the flatten bar.
  - B: `Close1600`, `prevClose` and `CommitDay` bookkeeping run before the `return`, so the band and history are unchanged.
  - B: line `:196 mod < CloseMod` is redundant but harmless.
  - Compile hazards: one enum, unique class names and `Name` strings, same encoding as the base (no BOM, LF).

## S6 cross-block check

Each deviation was tested against every block it touches, by name:
- **F1 (signal-path topology): untouched.** Both files are Strategy Analyzer backtest strategies. No live-signal code, no `PraxisSignalConsumer.cs` change (worktree equals HEAD, Evidence §5).
- **F2 (session-flat vs breakers #4/#5, FROZEN): not decided.** The governing flat time stays 16:00 ET. B moves only the bar on which the backtest exit order is submitted. Its price consequence (fill about 15:59 while still flat by 16:00) is disclosed and sent to Amear (C item 6 / D item 7). Nothing addresses breaker #4 (11:30) or #5 (15:00–18:00) or the 15:00 disposition.
- **F3 (fill resolution, FROZEN): untouched.** No backtest is run or reported. Step 0 of C carries the approved limitation sentence verbatim (worker 3 verified C:32).
- **F4 (MFFU compliance): untouched.** Nothing is MFFU-facing; Analyzer use only.
- **S4: partial, and this is a risk the master should weigh.** The bead text required the DECISIONS.md entry to be "written and staged BEFORE any .cs file". Tonight the entry exists only as the draft D, because DECISIONS.md was protected. The authorisation is DECISION_LOG `2026-10-31T00:46:43Z`.
  - The entry is **not** in DECISIONS.md (grep in Evidence §6 shows no 7zq lines there).
  - The master appends it. Commit 2 has now landed (4ec75ea), so that precondition is met.
  - Whether this ordering satisfies his constraint is Amear's question (D NEEDS AMEAR 5).

## Files staged

Each was staged with its own `git add`; Evidence §4 shows `A ` status:
- `ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`
- `ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`
- `docs/reports/2026-10-31-7zq-handtest-checklist.md`
- `docs/reports/2026-10-31-7zq-decisions-scope.md`
- `docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md`
- `docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md`
- `docs/reports/2026-10-31-7zq-m1-worker4-fix.md`
- `docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md`
- `docs/reports/2026-10-31-7zq-m1-variants.md` (this file, staged after writing)

No protected file was staged. The pre-existing unstaged changes to DECISION_LOG, DISPATCH_LOG, HANDOFF, STATUS, AUDIT_LOG, specs/SPEC_RUBRIC.md and settings.json were there at session start. They are not M1's, and M1 did not touch them.

Manager-contract token — Result: PASS (the producer's claim on the M1 deliverables at WRITTEN level only; this is not an audit, and the master's auditor grades).

Result: DONE

## NEEDS AMEAR

Unanswered; these are his. Full wording is in C `:283-300` and D `:59-65`.
1. **3gm Q2.** Should the replication's OppBand mean the paper's opposite band? File A is test material and does not decide it.
2. **3gm Q1.** Sizing (b) vs (c) is still open; no vol-target variant was built.
3. **Early-close handling.** After readbacks R4/R6: build a session-aware flat, and if so where?
4. **3gm C3.** If B shows same-day fills, is the 15:59 decision adopted into the base, or does it stay a variant?
5. **Flat1559 fill price.** Is a fill at the 16:00 bar's Open (about the 15:59 price) acceptable as the backtest realisation of the 16:00 flat, or does he want another mechanism?
6. **Step 0.** What value for High's extra fields, and what counts as "identical"?
7. **S4 ordering.** The DECISIONS entry was drafted alongside the .cs files, not appended before them. Does that meet his 22:58Z constraint?
8. **Third file (M2).** The swap after reading the shortlist stays his.

## Evidence

### §1 Base hash at unit start (before any worker)
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
719ab11
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -
61	0	DECISIONS.md
36	0	MANIFEST.md
13	12	config/backtest-cost-model.json
```
(The last line before the numstat is `git show 719ab11:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256`. The numstat is from unit start, before commit 2 landed.)

### §2 Final hashes and line counts (06:37 EDT, after all edits)
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
42df06faf65f65d9395c7d2e57b0c97c01a31642040052ba3380c10d955749cc  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
7cb71320082e4c34166287072f36b26745cb0b9721d1a837cde2f2bf3ecd916c  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
     338 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
     350 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
    1000 total
```

### §3 Full diffs (final)
```
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

```
--- ninjascript/PraxisNoiseAreaBreakout.cs	2026-07-16 15:39:15
+++ ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs	2026-10-31 06:29:18
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
+				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET. VARIANT: flat order submitted on the 15:59 bar so it fills at the 16:00 bar's open (~15:59 price), same session.";
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

### §4 `git status --porcelain` (06:37 EDT; this file staged afterwards, see the line under the block)
```
 M .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
MM ISSUE_REGISTER.md
 M STATUS.md
A  docs/reports/2026-08-06-session42-r8j-phase3-import.md
A  docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
A  docs/reports/2026-08-07-session44-r8j-offset-correction.md
AM docs/reports/2026-10-28-f4-davi-reply-filing.md
A  docs/reports/2026-10-28-nightly-checks-plan-review-note.md
AM docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
A  docs/reports/2026-10-31-7zq-decisions-scope.md
A  docs/reports/2026-10-31-7zq-handtest-checklist.md
A  docs/reports/2026-10-31-7zq-m1-worker1-build-variants.md
A  docs/reports/2026-10-31-7zq-m1-worker3-adversarial.md
A  docs/reports/2026-10-31-7zq-m1-worker4-fix.md
A  docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
A  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
M  docs/specs/2026-08-08-ledger-compaction-spec.md
A  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
A  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
?? F
?? docs/reports/2026-07-26-session36-manifest-and-memory.md
[... 64 further `??` lines, all pre-existing untracked docs/reports from 2026-07-26 → 2026-10-28 plus scripts/dispatch-log-close.sh and scripts/tests/test-dispatch-log-close.sh; none dated 2026-10-31 ...]
```
After writing this file, the manager runs `git add docs/reports/2026-10-31-7zq-m1-variants.md`. The status of this file is pasted in the return message, not here (observer effect: the file cannot paste its own staged status).

### §5 Protected-file proof (commit 2 landed mid-unit)
```
$ git log -4 --format='%h %ad %an %s' --date=iso
fab2855 2026-10-31 06:09:36 -0400 Amear Bani-Ahmad chore(ledger): DECISION_LOG.md flush 2026-07-26 to 2026-10-30, ruled by Amear 2026-10-30T23:31:00Z
4ec75ea 2026-10-31 06:09:22 -0400 Amear Bani-Ahmad docs(F3): D-2026-10-30-A fill resolution Standard + [N]=2 ticks/side, CONDITIONAL with Standard-vs-High control 2026-10-31; cost model v1.1.0; MANIFEST rows; audited PASS [Praxis_build-zyd]
4d7ca80 2026-10-30 18:50:53 -0400 Amear Bani-Ahmad docs: 3gm fidelity check ...
$ git diff --cached --numstat -- DECISIONS.md MANIFEST.md config/backtest-cost-model.json
(no output — those changes are now committed, not staged)
$ git show --numstat 4ec75ea | grep -E 'DECISIONS.md|MANIFEST.md|backtest-cost-model|zyd-rulings'
61	0	DECISIONS.md
36	0	MANIFEST.md
13	12	config/backtest-cost-model.json
154	0	docs/reports/2026-10-30-zyd-rulings-append.md
$ git diff --quiet HEAD -- DECISIONS.md MANIFEST.md config/backtest-cost-model.json ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisSignalConsumer.cs docs/reports/2026-10-30-zyd-rulings-append.md docs/reports/2026-10-30-zyd-f3-artifact.md docs/reports/2026-10-30-3gm-fidelity-check.md; echo "diff-quiet-vs-HEAD exit=$?"
diff-quiet-vs-HEAD exit=0
$ git diff --cached --name-only | grep -E '^(DECISIONS|MANIFEST|DECISION_LOG|DISPATCH_LOG|STATUS|HANDOFF)\.md|^config/|^specs/|^ninjascript/Praxis(NoiseAreaBreakout|SignalConsumer)\.cs|2026-10-30-'; echo "protected-in-index grep done"
protected-in-index grep done
```
mtimes (`stat -f "%Sm %N"`): DECISIONS.md Oct 30 19:25:06, MANIFEST.md Oct 30 19:13:21, config/backtest-cost-model.json Oct 30 19:13:01, STATUS.md Oct 30 20:42:36, base .cs Jul 16 15:39:15, PraxisSignalConsumer.cs Jul 15 15:52:29, specs/SPEC_RUBRIC.md Jul 30 11:50:39. All `docs/reports/2026-10-30-*.md` are dated Oct 30, between 17:54 and 19:25. Three files show later mtimes: DECISION_LOG.md Oct 31 06:10:46, HANDOFF.md Oct 31 06:10:46 and DISPATCH_LOG.md Oct 31 06:37:20. These are master/hook ledger writes around Amear's commits; no M1 worker was briefed to touch them, and none of the four worker reports lists them.

### §6 Manager's D fixes verified, and DECISIONS/MANIFEST not appended
```
$ grep -n -E 'written after this draft|D1–D12|^Note \(not' docs/reports/2026-10-31-7zq-decisions-scope.md
75:| /docs/reports/2026-10-31-7zq-m1-variants.md | Report | 2 | 2026-10-31 | Manager report for Praxis_build-7zq M1 (two Noise-Area variants
78:| /docs/reports/2026-10-31-7zq-m1-worker4-fix.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 fix sub-report (worker4): fixes the mana
79:| /docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 re-ADVERSARIAL sub-report (wor
82:Note (not a MANIFEST row — do not paste): worker 2 delivered the checklist and this draft but no sub-report (it hit its turn cap before
(table rows 71-80 contiguous; row 80 = /docs/reports/2026-10-30-zyd-rulings-append.md; line 81 blank; Note at 82)
$ grep -c 'zyd-rulings-append' MANIFEST.md
0
$ grep -n -E '7zq|_OppBand|_Flat1559' MANIFEST.md DECISIONS.md
(no output)
```
