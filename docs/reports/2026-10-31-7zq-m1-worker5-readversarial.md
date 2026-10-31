# 7zq M1 — worker 5 re-adversarial (final adversary)

## Task
Try to break A (`ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`), B (`ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs`), C (`docs/reports/2026-10-31-7zq-handtest-checklist.md`) and D (`docs/reports/2026-10-31-7zq-decisions-scope.md`) against the brief's criteria. Re-check worker 3's 11 defects.

## Mode
ADVERSARIAL. Read-only, except for this report. Nothing was compiled; there is no NT8 here. Every NT8-runtime statement below is INFERRED.

## Criterion
These are the brief's criteria, traceable to `specs/SPEC_RUBRIC.md` S1/S2/S4/S6/S8 and F2/F3:
- A/B diff scope and logic.
- A and B compile together with the base (static judgement only).
- C/D: S1, S2 and S8; the F3 sentence verbatim; the run-4 baseline; D marked PROPOSED; D's S6 statement; D's MANIFEST rows.

## Process log
1. Hashed the base against `git show 719ab11:`. `git status` on the artifacts. Read worker 3's defect list only (:160-177).
2. Ran `diff -u` base→A and base→B (pasted below). Read B's OnBarUpdate (:171-260) and FlattenAll (:323-329).
3. Traced A's ternary over 8 cases with a Python transliteration. Traced B over the 15:30, 15:59, 16:00 and 09:31 bars.
4. Scanned for paren balance (every imbalance is in a multi-line comment; the edited code lines A:233/A:241 balance). Checked BOM/encoding and namespace-level types. Grepped for stale "same-side" and 16:00 comments.
5. Checked citations: spec L34/38/49/57/59; 3gm :692, :733, :842, :849-854, :850, :857-861, :866, :1224, row R14 (:85); nt8 ref :130; voice notes :32/:33/:48/:52/:53; rubric :17/:30/:45/:59/:74-79/:94-99/:110; DECISION_LOG 10:10:15Z, 23:23:00Z, 23:30:00Z, 22:17:00Z, 08-29T00:10:00Z; F3 sentence `-F` grep; zyd :35.
6. Checked D's MANIFEST rows: column count, file existence, and the grep for the 7zq/zyd rows in MANIFEST.md and DECISIONS.md.

## Verification evidence

### Base integrity
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -        (git show 719ab11:...)
?? ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
?? ninjascript/PraxisNoiseAreaBreakout_OppBand.cs      (untracked; nothing staged)
```

### diff -u base → A (logic hunks; the full diff also changes header/comment/enum/Name/Description/Display)
```
-	public enum PraxisNoiseExitMode
-	{
-		OppBand,
-		BandOrVWAP
-	}
-	public class PraxisNoiseAreaBreakout : Strategy
+	public class PraxisNoiseAreaBreakout_OppBand : Strategy
-				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
+				ExitMode      = PraxisNoiseExitMode.OppBand;    // VARIANT 7zq default (base default BandOrVWAP, spec §4 p.13). The only knob.
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Max(curUpper, curVwap) : curUpper;
+					? Math.Max(curUpper, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curLower : curUpper);
 				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
-					? Math.Min(curLower, curVwap) : curLower;
+					? Math.Min(curLower, curVwap) : (ExitMode == PraxisNoiseExitMode.OppBand ? curUpper : curLower);
```
Every other hunk is a comment, the header, `Description`, `Name`, or the `Display` Description. Run of record: `diff -u ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs`; the hunks are @@ -15,6 +15,31 / -42,15 +67,13 / -98,8 +121,8 / -115,7 +138,7 / -201,20 +224,21 / -222,7 +246,9 / -296,7 +322,7.

### diff -u base → B (logic hunks)
```
-	public enum PraxisNoiseExitMode { OppBand, BandOrVWAP }      (5 lines removed)
-	public class PraxisNoiseAreaBreakout : Strategy
+	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
+		private const int FlattenMod = CloseMod - 1;   // 959 = 15:59 ET — variant 7zq: submit the flat one bar early
-			if (mod >= CloseMod)
+			if (mod >= FlattenMod)
```
The other hunks are the header, comments, `Description`, `Name`, and the trailing comment of `IsExitOnSessionCloseStrategy` (the value stays `true`). The hunks are @@ -14,6 +14,39 / -42,20 +75,20 / -98,14 +131,14 / -186,7 +219,12.

### A: 8-case stop trace
I transliterated A:232-233 / A:240-241 and base :208-209 / :216-217 into Python, with U=110, L=90, V=105:
```
OppBand cv=1.0 LONG base=110.0 A=90.0 DIFF | SHORT base=90.0 A=110.0 DIFF
OppBand cv=0.0 LONG base=110.0 A=90.0 DIFF | SHORT base=90.0 A=110.0 DIFF
BandOrVWAP cv=1.0 LONG base=110.0 A=110.0 SAME | SHORT base=90.0 A=90.0 SAME
BandOrVWAP cv=0.0 LONG base=110.0 A=110.0 SAME | SHORT base=90.0 A=90.0 SAME
```
- OppBand: long stop = Lower, short stop = Upper, for both vwapCumVol cases. This matches the criterion.
- BandOrVWAP with vwapCumVol>0: the true-arm expression is textually identical to the base, so it is identical for every value of V.
- BandOrVWAP with vwapCumVol==0: the false arm's inner guard sends it to `curUpper` / `curLower`, as in the base.
- **Worker 3 defect 2 is CLOSED.**

### B: trace (code at B:197-237)
| Bar | mod | Bookkeeping (B:197-216) | Flatten (B:227) | Checkpoint (B:234) | Result |
|---|---|---|---|---|---|
| 15:30 | 930 | Closes[930], VWAP | 930<959, no | :30 and 930<960, yes | normal exit/reverse/entry; the last checkpoint |
| 15:59 | 959 | Closes[959], VWAP | yes: FlattenAll → ExitLong/ExitShort("FlatEOD") (B:323-328), return | not reached | flat decision; no entry possible |
| 16:00 | 960 | Closes[960], Close1600 set (B:201) | yes: FlattenAll (no-op if the 15:59 order filled at this bar's open, INFERRED), return | not reached | Close1600 still recorded, so prevClose/gap logic is unaffected |
| next 09:31 | 571 | IsFirstBarOfSession → CommitDay, reset (B:179-193) | no | minute 31, no | the same as the base |

There is no entry at or after 15:59. IsExitOnSessionCloseStrategy = true is kept. The bookkeeping runs before the flatten `return`, so day history is identical to the base.

### Compile-together (static)
```
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout.cs:53:	public class PraxisNoiseAreaBreakout : Strategy
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:85:	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:76:	public class PraxisNoiseAreaBreakout_OppBand : Strategy
(DayRecord is nested in each class; no "generated code" region; no BOM — first bytes "#re" in all three)
```
- There is no duplicate namespace-level type, and the `Name` strings are distinct.
- Paren-imbalance awk over A and B: every hit is a comment line that continues onto the next line. The edited code lines A:233 and A:241 do not appear, so they balance.
- Nothing claims a compile: A:20, B:20, C:6 and D:45 all say "NOT COMPILED" or "not compiled".

### Worker 3 defects: CLOSED / OPEN
| # | Status | Evidence |
|---|---|---|
| 1 B price consequence | CLOSED | B:34-35 and B:224-226 say "fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00, INFERRED), one minute earlier in price". The same text is at C:203-204, D:37, D:39 and D:51. C:225-230 and B.5a (C:264-275) add the exit-price readback. |
| 2 BandOrVWAP cv==0 | CLOSED | 8-case trace above. |
| 3 A:247-249 label | CLOSED | A:250-251: "(INFERRED; same-bar exit+reverse resolution is CANNOT-DETERMINE-STATICALLY, 3gm R12/R21 — in OppBand mode this co-occurs on every reversal)". |
| 4 C:152 short-reversal wording | CLOSED | C:154-155: "the long reverses to short at `Close < Lower` (a short exits at `Close >= Upper` and reverses to long at `Close > Upper`)". |
| 5 A:27 §4→§3 | CLOSED | A:27 reads "SSRN 4824172 §3 p. 9 / Table 1". Spec:57 is `## 4. Exit policy + session-flat — PAPER-VERIFIED (§3, pp. 9–14)`. |
| 6 R2/R12/R21 mix | CLOSED | C:164-165 and D:32 now say "3gm table rows R12/R21; … 3gm readback R2 (… :850)". 3gm:850 = `- **R2. Reversals.** …`. |
| 7 D:33 last-bar fact | CLOSED | D:34: "which is INFERRED to be the session's last bar (pending 3gm readback R4, template hours; 3gm `:692` …)". 3gm:692 = "**Template hours were never captured.**" |
| 8 byte-for-byte enumeration | CLOSED | D:31 and D:36 now list Description :101, Name :102, header, enum comments, :204/:207/:215/:225/:118/:299 (A), and :108/:188 region/FlattenMod (B). D:41-42 adds the enum removal. I checked these against the diff hunks; the line numbers match the base. |
| 9 "no NT8 docs on disk" | CLOSED | B:26, C:244-245 and D:38 now say "no NT8 documentation of SessionIterator behaviour for this use was found". `grep -rln "SessionIterator\|ActualSessionEnd" docs specs` hits only 7zq reports and 3gm-worker2:661/:667. Those two lines are a grep of the base and return "no lines". The narrowed claim holds. |
| 10 MANIFEST rows for missing files | PARTIALLY OPEN, see defect 3 | The worker2 row is gone, and D:79 (worker5) is marked "written after this draft". This report now exists. D:75 (`2026-10-31-7zq-m1-variants.md`) still does not exist (`ls: … No such file or directory`), and its row is not itself marked as written later. |
| 11 early-close "exactly like base" | CLOSED | B:37-39, C:240-242 and D:38: "decision logic on that day is identical to the base … position/state carried into that day can differ". |

### Citation spot-checks (C and D)
```
nt8 ref :130  - Compilation compiles **ALL** NinjaScript files in the library, not just the open file.      (C:17 ✓)
3gm :850      - **R2. Reversals.** Trades tab: any Qty > 1, and any two exit rows with the same timestamp…   (C:165, D:32 ✓)
3gm :692      **Template hours were never captured.** …                                                     (D:34 ✓)
3gm :857      - **Q1. Sizing.** Is the replication target paper variant (b) … or (c) …                       (D:44 ✓)
3gm :1224     **Corrected :585 (last sentence) and :733 (first sentence):** "The flatten branch fires only on a bar with `mod >= 960` …  (C:243 ✓)
spec:38       … **1.3 trades/day** (base opp-band stop) rising to **1.8 trades/day** with the VWAP stop (Table 4, p. 16)  (C:160-162 ✓)
rubric:110    | S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain…  (D:22 ✓)
rubric:17/30/45/59 = F1/F2/F3/F4 headings; :74-79 O1; :94-99 O4 (D:50-55 ✓; the working-tree rubric diff is @@ -265,0 +266,10, after all of these)
DECISION_LOG:462 (10:10:15Z) " F3 stays FROZEN until a backtest report carries the limitation sentence…"  (C:20-21, D:52 ✓)
DECISION_LOG:461 (23:30:00Z) "(M1) no MANIFEST row for `docs/reports/2026-10-30-zyd-rulings-append…"         (D:82 "owed per F3 audit minor M1" ✓)
zyd :35       Added rose 54 → 61 (+7 = 1 blank + 6 block lines); deleted stays 0.                           (D:82 "+7 lines" ✓)
```

### F3 sentence, run-4 baseline
```
docs/reports/2026-10-31-7zq-handtest-checklist.md:32:> **Fills are optimistic; Standard resolution on 1-minute bars; 2 t[icks/side slippage assumed.**]
DECISIONS.md:302: … Every backtest report carries: `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
voice :33  PraxisNoiseAreaBreakout · NQCONT · Last · Minute 1 · … ExitMode BandOrVWAP · Contracts 1 · Include commission True · … Slippage 2 · Order fill resolution Standard
voice :32  Commission template PRAXIS … per unit $1.48 per side
voice :48  … Exit on session close ✓ …      DECISION_LOG 22:17:00Z: … Time in force DAY …
voice :52  Settings are the same as run 3 except Trading hours = CME US Index Futures RTH
voice :53  2021-03-08 → 2026-07-17 · 1,211 trades (584 long / 627 short) · net $3,136.84 · … PF 1.08 · max DD −$4,108.84
voice :54  … (1,211 → 48.44)
```
The table at C:47-61 and the baseline at C:64-65 match these exactly. The F3 sentence is verbatim (the `-F` grep matched).

### S8 / fill-price NEEDS AMEAR
- C:298-301 (item 6): "Is a fill at the 16:00 bar's Open acceptable … or do you want another mechanism (for example a finer secondary series)? Unanswered. No option is recommended here."
- D:65 (item 7): the same question, ending "Unanswered; no option is recommended."
- Both are present and unanswered. I found no other NEEDS AMEAR item in C (1-6) or D (1-7) that is answered or carries a recommendation. C:76 explicitly declines to pick High's field value, and C:80-81 leaves the void-clause trigger to Amear.

### D: PROPOSED status and MANIFEST rows
```
D:3  > **DRAFT — NOT APPENDED.** …      D:21 **Status:** PROPOSED …
grep "zyd-rulings-append|7zq" MANIFEST.md DECISIONS.md ; grep "D-2026-10-31-A" DECISIONS.md   -> (no output)
MANIFEST.md:3 header fields=5 ; D rows 71-79 and 82: fields=5 each
ls docs/reports/2026-10-31-7zq-m1-variants.md -> No such file or directory
ls docs/reports/2026-10-30-zyd-rulings-append.md -> exists (birth Oct 30 19:25:41 2026; matches Date Created 2026-10-30)
D:81 "Note: worker 2 delivered the checklist and this draft but no sub-report … The manager report row (`2026-10-31-7zq-m1-variants.md`) stays; that file is written by the manager."
D:82 | /docs/reports/2026-10-30-zyd-rulings-append.md | Report | 2 | 2026-10-30 | …
```
D:51 (F2) still holds given the B price consequence. It states the ~15:59 fill-price consequence and does not name a governing rule. F1, F3 and F4 are all named, at D:50, D:52 and D:53.

### Cases tried that did NOT break
- Fixes broke no syntax: the parens balance on A:233/A:241.
- No comment contradicts the code. "same-side" survives only at A:24, A:34 and A:227, and each one describes the base or the BandOrVWAP branch. B:81-82 correctly says that B's OppBand is still same-side.
- B's bookkeeping, including Close1600, runs before the flatten return.
- 16:00-bar double FlattenAll: a no-op if the 15:59 order is already filled (INFERRED).
- Template ending after 16:00 ET: covered as INFERRED/pending R4 at D:34 and C:208-210.
- A flat-only exit only at equality: confirmed. With L ≤ U, every `price < curLower` while long also fires EnterShort.
- C's TIF DAY: sourced via DECISION_LOG 22:17:00Z, as C:44 says.

## Files staged
None. This report is untracked and not staged. No other file was modified.

## Result
BROKEN. All three defects are MINOR, and all are in D's draft MANIFEST block. A and B hold every code criterion.

Noted, not counted: the enum declaration removal (base :47-51) in A and B falls outside the literal diff allowance. The compile-together criterion forces it, and D:41 discloses it.

1. **MINOR (S1, D:78).** The worker4 row says "fixes D1–D12 from the worker3 adversarial report". Worker 3's defect list numbers 1–11 (worker3:163-173), and it has no D-prefix or item 12. Worker4:3 shows that D1–D12 is the *manager's* numbering ("manager's numbering of … worker3-adversarial.md"). The citation therefore points at a numbering that the named file does not contain.
2. **MINOR (MANIFEST hygiene, D:81-82).** The owed zyd row (D:82) comes after the prose "Note:" paragraph (D:81), so it is detached from the table at D:71-79. Rendered, it is not a table row. The master's instruction is to append "the rows below" verbatim. Done verbatim, the paste either drops the owed row or drags the Note paragraph into MANIFEST.md's table. The row content itself is correct: 5 fields, the file exists, the date matches, "+7" is verified, and M1 is verified.
3. **MINOR (criterion "every row names a file that exists now or is explicitly marked as written later", D:75).** `docs/reports/2026-10-31-7zq-m1-variants.md` does not exist. Its row says only "ungraded at time of row". The only marking is D:81's present-tense "that file is written by the manager". Compare D:79, which is explicitly marked "written after this draft". This is the residue of worker 3 defect 10.

VERDICT: BROKEN
