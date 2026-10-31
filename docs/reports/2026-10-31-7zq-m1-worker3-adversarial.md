# 7zq M1 — worker 3 ADVERSARIAL report

**Task:** break artifacts A (`ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`), B (`ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`), C (`docs/reports/2026-10-31-7zq-handtest-checklist.md`), D (`docs/reports/2026-10-31-7zq-decisions-scope.md`) against base `ninjascript/PraxisNoiseAreaBreakout.cs` @ 719ab11.
**Mode:** ADVERSARIAL. Read-only, except for this file. Nothing staged, nothing modified.
**Criterion:** the brief's A/B/C/D criteria; SPEC_RUBRIC S1, S2, S8; F3 sentence verbatim; run-4 numbers from the voice notes.
**Date:** 2026-10-31 (shell: `Sat Oct 31 10:17:33 UTC 2026` / `06:17:33 EDT`).

---

## Process log (what I ran, condensed)

1. `diff -u` base vs A, and base vs B. Read the base with `cat -n`. Read C and D in full.
2. Grepped each DECISION_LOG timestamp D/C cite, in the working copy, in HEAD and in fab2855.
3. `git log --oneline -1` on 4d7ca80, 4ec75ea, fab2855 and 719ab11. sha256 of the base vs `git show 719ab11:`. Checked that DECISIONS.md has no D-2026-10-31-A. Checked the MANIFEST header.
4. Checked rubric line numbers. Ran `sed` on the voice notes :28-56. Grepped the F3 sentence (`-F`).
5. Grepped ninjascript/ for namespace-level types, `Name =` strings, encoding and BOM.
6. Checked these citations: 3gm :692, :716-735, :842, :849-866, :1224, rows R2/R12/R14/R21; spec L38/L49/L59 and section headings; nt8 reference :10, :128-131; F3 research :45-64.

## Verification evidence (pasted, abridged to the relevant lines)

**Diff base→A (logic hunk):**
```
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Max(curUpper, curVwap) : curUpper;
+					? Math.Max(curUpper, curVwap) : curLower;
...
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Min(curLower, curVwap) : curLower;
+					? Math.Min(curLower, curVwap) : curUpper;
```
**Diff base→B (logic hunk):**
```
+		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
-			if (mod >= CloseMod)
+			if (mod >= FlattenMod)
```
**DECISION_LOG timestamps:**
```
== 2026-10-30T22:58:00Z: working=1 HEAD=1 fab2855=1
== 2026-10-31T00:41:00Z: working=1 HEAD=1 fab2855=1
== 2026-10-31T00:46:43Z: working=1 HEAD=1 fab2855=1
== 2026-10-31T00:49:35Z: working=1 HEAD=1 fab2855=1
== 2026-10-30T23:23:00Z: working=2 HEAD=2 fab2855=2
== 2026-10-30T22:40:00Z: working=1 HEAD=1 fab2855=1
== 2026-10-31T10:10:15Z: working=1 HEAD=0 fab2855=0
== 2026-10-30T22:22:00Z: working=2 HEAD=2 fab2855=2
== 2026-10-30T22:17:00Z: working=1 HEAD=1 fab2855=1
== 2026-08-29T00:10:00Z: working=5 HEAD=5 fab2855=5
Sat Oct 31 10:17:33 UTC 2026
Sat Oct 31 06:17:33 EDT 2026
```
`10:10:15Z` is **real**. It is UTC (06:10 EDT), 7 minutes before my clock read, and it is not in the future. The row reads: "COMMITS 2 AND 3 LANDED AND PUSHED — `4ec75ea` … and `fab2855` …; `git log --oneline -3` = fab2855 / 4ec75ea / 4d7ca80". It is uncommitted, which is correct: D:13 says the live file is still being appended.

**Commits / hash / DECISIONS:**
```
4d7ca80 docs: 3gm fidelity check of PraxisNoiseAreaBreakout.cs vs Noise-Area spec, audited PASS ...
4ec75ea docs(F3): D-2026-10-30-A fill resolution Standard + [N]=2 ticks/side, CONDITIONAL ...
fab2855 chore(ledger): DECISION_LOG.md flush 2026-07-26 to 2026-10-30, ruled by Amear 2026-10-30T23:31:00Z
719ab11 Praxis_build-4uu (b2-signal-repro): paper-faithful NQ Noise-Area breakout NinjaScript strategy (Mac-side)
decisions hits: 0
3:| File Path | Type | Phase | Date Created | Purpose |
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -          (git show 719ab11:)
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
```
**Rubric lines:**
```
17: ### F1 — Signal-path topology vs. circuit-breaker placement
30: ### F2 — Session-flat time vs. breakers #4 and #5
45: ### F3 — Backtest fill resolution vs. acquired data granularity
59: ### F4 — MFFU automation compliance
74: ### O1 — Walk-forward gate set for the replication arm
94: ### O4 — Backtest-vs-live configuration parity
110: | S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after. |
```
**Voice notes (file line = L(n)+27; the file is untracked, `error: pathspec ... did not match`):**
```
L5+27 (=32)  Commission template PRAXIS ... per unit $1.48 per side.
L6+27 (=33)  Strategy Analyzer settings: PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · trading hours CME US Index Futures RTH · ExitMode BandOrVWAP · Contracts 1 · Include commission True · Account Sim101 · Slippage 2 · Order fill resolution Standard.
L13+27 (=40) | 3 (full history, same settings) | 2021-03-08 → 2026-07-17 | 1,075 | ...
L21+27 (=48) ... Break at EOD ✓ · Exit on session close ✓ · Fill limit on touch ☐.
L25+27 (=52) Settings are the same as run 3 except Trading hours = CME US Index Futures RTH.
L26+27 (=53) 2021-03-08 → 2026-07-17 · 1,211 trades (584 long / 627 short) · net $3,136.84 · ... PF 1.08 · max DD −$4,108.84 · ... total slippage 48.44.
```
C's run-4 baseline (C:64-65), the settings table (C:47-61) and its line cites (:32/:33/:48/:52/:53) all **match**. `Time in force DAY` is not in the notes. It is in the 22:17:00Z row, which C cites: `...Set order quantity Strategy, Time in force DAY, Fill limit orders on touch ☐...`.

**F3 sentence:**
```
docs/reports/2026-10-31-7zq-handtest-checklist.md:32:> **Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.**
```
The sentence is verbatim. R-F3-3 appears in DECISION_LOG:458: `R-F3-3, closes NEEDS AMEAR 4):** limitation sentence APPROVED as proposed — *"Fills are optimist`.

**Compile scan (attack 6):**
```
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout.cs:53:	public class PraxisNoiseAreaBreakout : Strategy
ninjascript/PraxisSignalConsumer.cs:44:	public class PraxisSignalConsumer : Strategy
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:76:	public class PraxisNoiseAreaBreakout_OppBand : Strategy
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:80:	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
(all four files: namespace NinjaTrader.NinjaScript.Strategies)
Name = "PraxisNoiseAreaBreakout" / "_OppBand" / "_Flat1559" / "PraxisSignalConsumer" — unique
encoding: all UTF-8, CRLF=0, first bytes 237265 ("#re", no BOM) — identical to the base, which compiled clean on the VM (voice notes :31)
```
Statically: no duplicate type, no duplicate Name, one enum declaration, and the variants resolve the enum through the shared namespace. The nested `private sealed class DayRecord` is class-scoped, so the repeats are legal. **No compile break found.** Not compiled; this is a static judgement only.

**On-disk NT8 doc:**
```
docs/reference/2026-07-24-nt8-windows-reference.md   (tracked)
10: 1. **Web-docs half** — official NT8 Help Guide (https://ninjatrader.com/support/helpguides/nt8/), researched against 8
SessionIterator hits in docs/: only the three 7zq files + 3gm-worker2 (a grep of the base, 0 lines)
```
**3gm template hours:** `692: **Template hours were never captured.**`. S5 (:731): "The template actually ends after 16:00 ET; FlatEOD fills the same day at 16:01".
**3gm row namespaces:** `73:| R2 | §A L17 — Lookback 14, fixed | ... | FAITHFUL |`, `83:| R12 | ... reversal via NT8 managed reverse | ... CANNOT-DETERMINE-STATICALLY |`, `92:| R21 | ... exit + reverse on the same bar | ... CANNOT-DETERMINE-STATICALLY |`, `850:- **R2. Reversals.** Trades tab: any Qty > 1 ...`.
**Spec sections:** `34:## 2. Breakout trigger — PAPER-VERIFIED (§3, p. 9)`, `57:## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)`. 3gm R14 cites `§3 p. 9 / Table 1`.
**Draft-row targets:**
```
ls: docs/reports/2026-10-31-7zq-m1-variants.md: No such file or directory
ls: docs/reports/2026-10-31-7zq-m1-worker2-checklist-scope.md: No such file or directory
```

---

## Attack-by-attack results

**1. OppBand same-bar ExitLong + EnterShort.** This pattern is **not new**. In the base, when the position is long and `price < curLower`, the XL test `price <= stop` is always true in both modes. In OppBand, `stop = curUpper ≥ curLower`. In BandOrVWAP, `stop = max(curUpper, vwap) ≥ curUpper`, because `curLower = refLower(1−σ) ≤ refUpper(1+σ) = curUpper`. So base:211 and base:229 both fire on every reversal bar, and run 4 already exercised this path. A changes how often it happens: in OppBand nearly every exit becomes this pair. How NT8 resolves a market XL plus a reversing entry (Qty 2, an extra "Close position" row, or an ignored entry) is CANNOT-DETERMINE-STATICALLY. C:161-163 and D:31 label it. A does not (defect 3). C A.5 asks for the right readbacks (Qty > 1, two exits at one timestamp, "Ignored" messages).

**2. BandOrVWAP fallback.** The arm after `:` is shared by `ExitMode == OppBand` and by `BandOrVWAP && vwapCumVol == 0`, so BandOrVWAP changes in the zero-volume case (defect 2). A:33-35 discloses this. C and D do not.

**3. Stale semantics.** A has no remaining "same-side" claim for OppBand: A:24 and A:35 describe the base, and A:227 is the BandOrVWAP clause. A:247-249 keeps the base's unqualified "still reverses correctly" (defect 3). A:27 has a wrong paper section (defect 5).

**4. Flat1559 trace.**
- 15:30 is a checkpoint (930 < 959). An XL/XS or entry submitted there fills at 15:31.
- 15:59 bar (959): the bar's close is recorded, then `FlattenAll` runs, then `return`. No entry.
- 16:00 bar (960): `Close1600` is recorded (`mod == CloseMod`, unchanged; it is dead per 3gm). `FlattenAll` runs on a position that is already flat, because the FlatEOD fill is processed at this bar's open, so no second FlatEOD. Then `return`.
- First bar of the next session: `CommitDay`, and `prevClose = Close[1]`, the 16:00 close. Unchanged.

No entry can happen at or after 959: the only path to Enter* is past the `return`, and 959 is not a :00/:30 stamp anyway. `:196 mod < CloseMod` is now redundant but consistent; the last checkpoint stays 15:30. Whether the session-close backstop also fires is CANNOT-DETERMINE-STATICALLY, and C:222 states it as an INFERRED expectation. **There is no logic break, but there is a disclosure break (defect 1):** the fill is the 16:00-stamped bar's Open, which is a ~15:59:00 price.

**5. Early close / missing 15:59 bar.** The statements are correct and labelled INFERRED (B:34-38, C:229-233, D:35). Small gaps: defect 11, plus a missing-16:00-bar edge case that no artifact mentions. In that case B flattens at 15:59 and the order's next bar is the next session. NQ RTH practically always has a 16:00 bar, so this is low severity and is not counted in the defect list.

**6. Compile.** NO BREAK FOUND (evidence above).

**7. C predictions.** Every EXPECTED block is headed "all INFERRED" (C:151, C:218). The trade-count line C:223-226 carries the S2/S3/S4 exception and points to the R1 readback, which is adequate. The run-4 numbers and the F3 sentence are verified. Defect 4 (wording) and defect 6 (citation) are in C.

**8. D citations.** All timestamps exist, including 10:10:15Z. All shas resolve. The rubric line numbers are right. The MANIFEST columns match the header. D does not claim the entry is in DECISIONS.md: D:3 says "NOT APPENDED", and the grep returns 0. Defects 7, 8 and 10 are in D.

**9. S8.** NO BREAK FOUND. C:255 and D:55 list questions only. C:76 refuses to choose High's fields. D:60 raises the S4 timing question instead of ruling on it. The master's pick of the two variants is recorded with a swap offer, and that matches 22:58:00Z.

---

## Out-of-scope findings (reported, not fixed)

- The base `ninjascript/PraxisNoiseAreaBreakout.cs` has **no MANIFEST row**: `grep -n "NoiseArea" MANIFEST.md` finds only reference and report rows.
- DECISION_LOG.md rows 462-465 are out of chronological order: 10:10:15Z, then 00:49:35Z, then 00:46:43Z, then 00:41:00Z (line numbers from the grep above).

## Files staged

None. I created only this report, with the Write tool. It is unstaged.

## Result

The variants contain no compile-level or trade-logic break that I can show statically. The breaks are in claim scope (S2) and in one formal miss of a criterion.

1. **MAJOR (S2, bears on the F2 claim the auditor must grade).** Flat1559's realised exit is the Open of the 16:00-stamped bar. That bar spans 15:59:00–16:00:00 under B's own end-stamped premise (B:24-25), so the exit price is the first trade at or after **15:59:00**, one minute before the governing 16:00 flat. B:31 ("changes only WHEN the exit order is submitted"), C:197-198, D:36 and D:48 ("moves only the submission bar") leave this out. C:219 expects grid "exit time 16:00", and under Standard resolution the grid will show 16:00, so the readback cannot reveal the shift. This is inherent to the design the brief asked for. The defect is that no artifact states it.
2. **MINOR (formal criterion miss: "BandOrVWAP behaviour identical to base").** When `ExitMode == BandOrVWAP && vwapCumVol == 0`, A's fallback is now the opposite band (A:232-233 long, A:240-241 short; diff hunk above). A:33-35 discloses it as INFERRED-unreachable. C:129, C:184-185, D:30 and the D:67 MANIFEST row say flatly that "the BandOrVWAP branch is unchanged". A mode-guarded ternary would have kept BandOrVWAP identical.
3. **MINOR (labelling).** A:247-249 keeps the base's unqualified "an ExitLong above followed by Close<Lower still reverses correctly". 3gm grades that R12/R21 CANNOT-DETERMINE-STATICALLY, and in A it governs nearly every OppBand exit. A's header carries no CANNOT-DETERMINE label for the same-bar pair. C and D do.
4. **MINOR (C:152 misstatement).** "a short reverses at `Close < Lower`" is wrong. A short position reverses at `Close > Upper`. At `Close < Lower` it is the long that reverses to short.
5. **MINOR (S1 citation, A:27).** "Paper: SSRN 4824172 §4 p.9" should be paper §3: spec :34 and :57 say "(§3, p. 9)" and "(§3, pp. 9–14)", and 3gm R14 cites "§3 p. 9 / Table 1". §4 is the spec's own section number.
6. **MINOR (S1 citation, C:161 and D:31).** "3gm R2/R12/R21" mixes two numbering schemes. 3gm table row R2 (:73) is "Lookback 14, fixed — FAITHFUL". The reversal readback is NEEDS AMEAR R2 (:850).
7. **MINOR (S2, D:33).** "submitted on the close of the session's last bar (16:00)" is stated as fact. 3gm :692 says "Template hours were never captured", and S5 (:731) keeps open a template that ends after 16:00 ET. B's "bar before the session's last bar" premise rests on the same unverified template (R4 pending).
8. **MINOR (S2, D:30, D:34, D:39).** "Everything else is byte-for-byte the base" is not true of D's own change lists. They omit the `Description` string change (:101) in both variants, and B's :108 comment and its added :188-region comment lines. The criterion permits those edits; D's enumeration of them is incomplete.
9. **MINOR (S2, B:26, C:233, D:35).** "No NT8 help documentation was found on disk" is too broad. `docs/reference/2026-07-24-nt8-windows-reference.md` (tracked) is Help-Guide-derived (:10). The accurate claim is narrower: it has 0 hits for SessionIterator/ActualSessionEnd.
10. **MINOR (D:71, D:73).** Draft MANIFEST rows are written for two files that do not exist yet (`2026-10-31-7zq-m1-variants.md`, `...-worker2-checklist-scope.md`; `ls` errors pasted). Their Date Created is unverifiable until the files exist.
11. **MINOR (S2, B:34-35, C:230).** "Behaves exactly like the base" on early-close days holds for the code path only. If the base carried a position overnight into that day (3gm S2/S3) and B did not, the state entering the day differs, so the trades can differ. C:224-226 already makes this point for the trade count but not here.

Checked and holding: the compile scan; every DECISION_LOG timestamp (10:10:15Z is real UTC); the shas and the base hash; the rubric line numbers; the F3 sentence (verbatim); the run-4 settings and baseline; D not claiming DECISIONS.md was appended; S8; and the Flat1559 trace (no entry at or after the flatten bar, no double FlatEOD).

VERDICT: BROKEN
