# 2026-11-07 — unit 2026-11-07-arm-b-code — manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

**Level: WRITTEN — statically checked (T6(i)) — not compiled, not run.** This Mac has no C# compiler. The master OBSERVED `dotnet`, `csc`, `mcs` and `mono` all "not found" (DECISION_LOG `2026-11-07T16:04:00Z`). Nothing in this report is a compile result or a backtest result. The trade counts quoted below (1,190 / 810 / 1,190) come from the committed runs of the three base files, which spec T1–T3 name as the targets. This file did not produce them.

## Task

Write `ninjascript/PraxisNoiseAreaBreakoutArmB.cs`, the arm (b) tunable variant of the committed Noise-Area strategy. Authority: D-2026-11-07-B (DECISIONS.md:1292-1462) and spec `docs/specs/2026-11-06-walk-forward-values.md` §3/§4/§9 (:44-226). Authorisation: DECISION_LOG `[2026-11-07T16:04:00Z] WHO: praxis-master`. Run the T6(i) static check on the Mac. Run two adversarial passes: (A) test-escape hunt; (B) m = 0 equivalence. Append two MANIFEST rows. Stage nothing and commit nothing. The master cuts `arm-b/wf-tunables` and commits through the gate.

## Rubric criteria addressed (verbatim from specs/SPEC_RUBRIC.md:107-119)

- **S1 | Every claim in a report has pasted command output, not a description of output.** Met: every number in `## Verification evidence` is pasted output. Where a block's header line paraphrases the command rather than reproducing it (E4, E6, E7, E9), that block says so. The worker outcomes and adversarial findings are my summaries of the workers' returned reports and are labelled as such; only text in quotation marks is verbatim. Every finding I acted on was re-checked by a command I ran myself, pasted below. (Corrected after a report adversary, W6, see below.)
- **S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.** Met: the file is reported as WRITTEN only (header comment :22, Description :110, this report :5). T1–T13 are not run. The T1–T3 equivalence is argued by logic diff (pass B), not by a run.
- **S4 | Every deviation from the plan has a DECISIONS.md entry with a traceable authorisation chain, written before the work, not after.** Met for the work done: D-2026-11-07-B was committed at 43b34b1 before this dispatch. Where the code adds something the spec text does not state, it is listed under "Additions beyond the spec text" below with the reason. None of those changes a trade. One open point may be a deviation: the early-close checkpoint (Still the master's, item 1). It is listed for the master, not decided here, and no DECISIONS.md entry was written.
- **S6 | Cross-block check: every approved deviation is tested against the specs of every other block it touches, not only its own.** See `## S6 cross-block check`.
- **S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: [the sentence — carried once, at line 3 of this report; not repeated here so that "once" holds]** Met: line 3. The probe in E9 counts it as 1. The code file holds no backtest figure.

## Workers dispatched

Spawn and close times are from the SubagentStart/SubagentStop hook rows in DISPATCH_LOG.md (E7).

| # | id | mode | given | outcome |
|---|---|---|---|---|
| W1 | a62d9c20c6a9ec05b | BUILD | full design, base + variants + spec | wrote the file, 461 lines, sha `b04f4488…2a63`. Self-checks clean. Six wording/syntax departures from the brief, none behavioural |
| W2 | a7fd134e7741a41fe | ADVERSARIAL A (test-escape hunt) | file + spec §3/§4/§9 + the three committed files only | **VERDICT: FAIL**. 1 BLOCKING (ATR warm-up opens at s17, not s16), 3 MINOR, NOTEs |
| W3 | a4f79d9f2118a9253 | ADVERSARIAL B (m = 0 equivalence) | file + spec + the three committed files only | **VERDICT: PASS**. No BLOCKING difference for T1, T2 or T3. 17 shared differences graded NON-BLOCKING or COSMETIC |
| W4 | ad816d85d3e9e4734 | BUILD (fix) | the BLOCKING defect + an exact fix | applied. 462 lines, sha `923e0dc9…4028` (final) |
| W5 | a30cab8c6c10d8e0c | ADVERSARIAL A2 (warm-up trace + full re-hunt on the fixed file) | file + spec + the s1-drop fact | **VERDICT: PASS**. 0 BLOCKING/MAJOR, 1 MINOR, 4 NOTEs. Traced against the data file |

The outcome column summarises each worker's returned report; it is not pasted output. W1's line count and sha, and the 70-brace count of W1's file, are pasted in E10. The counts "17 shared differences", "1 MINOR, 4 NOTEs" and "six departures" are the workers' own, not re-run.

There were six workers: five on the code (three adversarial passes: W2, W3, W5) and one adversarial pass on this report (W6, a-id ab7d784d2bfc3c282, VERDICT: FAIL on pointers, header disclosure and qualifiers; fixed in place, listed under "Adversarial findings"). That is within the ≤6 limit and meets the minimum of 2 adversarial passes.

## Process log

1. 16:03Z: baseline checked. HEAD = afea575; the three base shas match the brief; the real index holds 12 files, none of them under `ninjascript/` (E1).
2. I read spec §3/§4/§9 in full (:44-226), the base file in full, and both variants' comment-stripped diffs against the base, then skimmed D-2026-11-07-B for code obligations. Finding: spec T6(ii) (:190) puts two print duties on the code that the brief does not list. (a) σ / UpperBound / LowerBound / ATR(14) at the 10:00 checkpoint of three sessions "named in the code unit's report before the run". (b) Fill, ATR and level at every entry. Both were added. The sessions are named in this report: 2021-06-15, 2024-12-26, 2026-03-18.
3. 16:03:57Z: W1 dispatched with the full design: precedence, the stop check form, the policy branches, the ATR method, the prints and the reset. Returned 16:06:48Z.
4. I read the file in full myself, then ran the T6(i) greps and the comment-stripped diff.
5. **16:08:00Z (`date -u`): `## Does NOT cover / UNVERIFIED` written** (items 1–12, below, unchanged since). W2 was dispatched at 16:08:17Z and W3 at 16:08:30Z, both after that.
6. W3 returned PASS at 16:11:10Z. W2 returned FAIL at 16:14:01Z: the base returns on `CurrentBar < 1`, so session 1 is never committed, so `history.Count >= AtrPeriod + 1` first holds at s17. **Checked before acting.** `docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md:89` records R19, "first session never committed" (E5). Spec §4 says "ATR(14) needs 15 completed sessions (14 true ranges and one prior close)", and §5 (:85) says "from s16 at lookback 10 and 14". The prior close of s2 is `Close[1]` at s2's first bar, the last bar of s1. So the defect is real.
7. 16:14:52Z: W4 applied the fix. Each `DayRecord` now carries its own `PrevClose` (`= prevClose`, :196). `ComputeAtr` requires `history.Count >= AtrPeriod` and uses `rec.PrevClose` (:378-392). I diffed the code before and after the fix (E5). Only the intended lines changed. The raw brace count fell 70 (E10, W1's file) → 68 (W4's self-check, not re-pasted), but the code-only count is 65/65 both before and after (E5), so the two braces were in `//` comments.
8. 16:16:10Z: W5 dispatched (A2) on the fixed file. It returned PASS at 16:22:20Z. It traced s1…s16 against the data file `/Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt` and found `haveAtr` first true at s16 (2021-03-29). I re-checked the session numbering and the oracle dates on that file myself (E6).
9. Negative test: I wrote a mechanical form of the T6(i) checks: a branch scanner (`S/branchscan.awk`), a literal-quantity grep, a NoiseMult-in-stop grep and a forbidden-identifier grep. On the real file it reports only the two exemptions spec :190 allows. On four one-line mutants it trips every time (E4).
10. MANIFEST rows appended (:269-270, E8). Report written. Token probe run (E9).

## Verification evidence

All blocks are pasted output. `S` = `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/d2d7d756-0ed5-4816-acfb-8ded37620b9d/scratchpad`.

### E1. Baseline, before any worker (16:03Z)

~~~
$ git rev-parse HEAD && shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs && wc -l ninjascript/PraxisNoiseAreaBreakout*.cs && git status --short ninjascript/ && git diff --cached --name-only | wc -l
afea57569ca282f45011286d79258045906d2c03
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
42df06faf65f65d9395c7d2e57b0c97c01a31642040052ba3380c10d955749cc  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
7cb71320082e4c34166287072f36b26745cb0b9721d1a837cde2f2bf3ecd916c  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
     312 ninjascript/PraxisNoiseAreaBreakout.cs
     350 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
     338 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
    1000 total
      12
~~~

### E2. Final state: base shas after, the new file's size and sha, T6(i) greps, order calls, index

Annotation: in the header line of the input-use grep, zsh's `echo` ate the `\b` characters. The command as run was `grep -n -E "\bLookback\b|NoiseMult|StopAtrMult|ExitPolicy\b|AtrPeriod|atrSum|stopAtrSum" … | grep -v -E "^[0-9]+:[[:space:]]*//" | grep -v "Description =" | sed 's#[[:space:]]*//.*$##; s/[[:space:]]\{1,\}/ /g'`. The order and `-w 14` blocks were run through `sed 's/[[:space:]]\{1,\}/ /g'`, which the echoed header lines do not show.

~~~
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs ninjascript/PraxisNoiseAreaBreakout_OppBand.cs ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
42df06faf65f65d9395c7d2e57b0c97c01a31642040052ba3380c10d955749cc  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
7cb71320082e4c34166287072f36b26745cb0b9721d1a837cde2f2bf3ecd916c  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
$ wc -l ninjascript/PraxisNoiseAreaBreakoutArmB.cs; shasum -a 256 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
     462 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028  ninjascript/PraxisNoiseAreaBreakoutArmB.cs
$ grep -n -E "BandSigmaMult|const int Lookback|PraxisNoiseExitMode" ninjascript/PraxisNoiseAreaBreakoutArmB.cs; echo "exit=$?"
exit=1
$ grep -n -w 14 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
54: private const int AtrPeriod = 14; // ATR period, fixed, not tuned (spec §3/§4)
125: Lookback = 14;
241: // Early-close last bar (12:00 / 12:15 / 14:03): NT8's Exit on session close flattens there
376: // sessions (14 true ranges plus one prior close). The data's first session is never committed (as base),
$ grep -n -E "EnterLong|EnterShort|ExitLong|ExitShort" ninjascript/PraxisNoiseAreaBreakoutArmB.cs
257: ExitLong("XStop", "");
265: ExitShort("XStop", "");
288: ExitLong("XL", "");
299: ExitShort("XS", "");
307: EnterLong(Contracts, "L");
309: EnterShort(Contracts, "S");
425: ExitLong("FlatEOD", "");
427: ExitShort("FlatEOD", "");
$ grep -n -E "SetStopLoss|StopMarket|StopLimit|SetTrailStop|SetProfitTarget" ninjascript/PraxisNoiseAreaBreakoutArmB.cs; echo "exit=$?"
exit=1
$ grep -n -E "Lookback|NoiseMult|StopAtrMult|ExitPolicy|AtrPeriod|atrSum|stopAtrSum" ninjascript/PraxisNoiseAreaBreakoutArmB.cs | grep -v -E "^[0-9]+:[[:space:]]*//" | grep -v "Description ="
40: public enum PraxisNoiseArmBExitPolicy
54: private const int AtrPeriod = 14;
70: private int HistoryCap { get { return Lookback + 15; } }
86: private double atrSum;
87: private double curAtr;
88: private bool haveAtr;
93: private double stopAtrSum;
110: Description = "PRAXIS walk-forward arm (b) Noise-Area Breakout: base logic with tunable Lookback, noise multiplier, bar-close daily-ATR stop and exit policy (BandOrVWAP / OppBand / Flat1559). D-2026-11-07-B. WRITTEN, not compiled, not run.";
125: Lookback = 14;
126: NoiseMult = 1.0;
127: StopAtrMult = 0.0;
128: ExitPolicy = PraxisNoiseArmBExitPolicy.BandOrVWAP;
160: atrSum = 0.0;
165: stopAtrSum = 0.0;
171: "{0} INPUTS Lookback={1} NoiseMult={2:R} StopAtrMult={3:R} ExitPolicy={4} Contracts={5}",
172: Name, Lookback, NoiseMult, StopAtrMult, ExitPolicy, Contracts));
234: int flatMod = (ExitPolicy == PraxisNoiseArmBExitPolicy.Flat1559) ? FlattenMod : CloseMod;
250: if (StopAtrMult > 0.0 && haveStopLevel && !isSessionLastBar
255: if (AtrPeriod * (stopFill - Close[0]) >= StopAtrMult * stopAtrSum)
263: if (AtrPeriod * (Close[0] - stopFill) >= StopAtrMult * stopAtrSum)
283: if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
294: if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
303: bool atrGateOpen = (StopAtrMult <= 0.0) || haveAtr;
323: if (!(StopAtrMult > 0.0) || !haveAtr)
329: stopAtrSum = atrSum;
331: ? stopFill - StopAtrMult * (stopAtrSum / AtrPeriod)
332: : stopFill + StopAtrMult * (stopAtrSum / AtrPeriod);
341: #region Band construction (as base; Lookback and NoiseMult are inputs)
350: for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
360: if (cnt < Lookback)
366: curUpper = refUpper * (1.0 + NoiseMult * curSigma);
367: curLower = refLower * (1.0 - NoiseMult * curSigma);
380: haveAtr = history.Count >= AtrPeriod;
385: for (int i = history.Count - AtrPeriod; i <= history.Count - 1; i++)
390: atrSum = sum;
391: curAtr = atrSum / AtrPeriod;
405: "{0} ORACLE {1} 10:00 Lookback={2} NoiseMult={3:R} {4} {5}",
406: Name, Time[0].Date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture), Lookback, NoiseMult, band, atr));
436: public int Lookback { get; set; }
441: public double NoiseMult { get; set; }
446: public double StopAtrMult { get; set; }
450: public PraxisNoiseArmBExitPolicy ExitPolicy { get; set; }
$ git status --short ninjascript/
?? ninjascript/PraxisNoiseAreaBreakoutArmB.cs
$ git diff --cached --name-only | grep -c ninjascript
0
$ git diff --cached --name-only | wc -l
      12
$ git rev-parse HEAD; git branch --show-current
afea57569ca282f45011286d79258045906d2c03
main
~~~

**T6(i) reading against spec :190, line by line (each point cites E2/E3/E4 lines):**

| T6(i) clause | Base line(s) | ArmB line(s) | Holds? |
|---|---|---|---|
| no `BandSigmaMult`, no `const int Lookback` | :74, :76 | none (forbidden grep exit=1; also no `PraxisNoiseExitMode`) | yes |
| the only other literal `14` is `AtrPeriod` | :74 | :54 `AtrPeriod`; :125 is a `SetDefaults` assignment (excluded); :241 and :376 are comments (excluded) | yes |
| base :79 `HistoryCap` reads the property | :79 | :70 `Lookback + 15` | yes |
| base :247 loop bound reads the property | :247 | :350 `cnt < Lookback` | yes |
| base :257 sample check reads the property | :257 | :360 `if (cnt < Lookback)` | yes |
| base :263/:264 band multiplier reads the property, both bounds | :263, :264 | :366, :367 `NoiseMult * curSigma` | yes |
| stop level reads `StopAtrMult` and ATR, never `NoiseMult` | — | check :255, :263 (`StopAtrMult * stopAtrSum`); level :331-332; `NoiseMult` appears only at :126 (SetDefaults), :171-172 (readback string and arguments), :341 (`#region` text), :366-367 (band), :405-406 (oracle print), :441 (property) | yes |
| ATR reads `AtrPeriod` | — | :380, :385, :391 | yes |
| every base read of `ExitMode` (:208, :216) reads `ExitPolicy` | :208, :216 | :283, :294 | yes |
| 15:59 flatten conditioned on `ExitPolicy == Flat1559` and the minute only | `_Flat1559.cs` :91, :227 | :234-235 `flatMod = (ExitPolicy == Flat1559) ? FlattenMod : CloseMod; if (mod >= flatMod)` | yes |
| no `ExitPolicy` read and no order call inside a `StopAtrMult` branch, except the stop's own level/check/`XStop` and the ATR entry gate | — | branch scan (E4, real file): only :257, :265 (`XStop`, inside the stop `if` at :250) and :307, :309 (entries, inside the ATR entry gate `if (atrGateOpen)` at :304) | yes |
| every `EnterLong`/`EnterShort` passes `Contracts` | :227, :229 | :307, :309 | yes |
| every `ExitLong`/`ExitShort` (`XL`, `XS`, `FlatEOD`, `XStop`) passes no quantity | :211, :219, :288, :290 | :257, :265, :288, :299, :425, :427, all `(name, "")` | yes |
| no order call has a literal quantity | — | E4 C2 on the real file: no hit | yes |
| no resting stop order | — | `SetStopLoss|StopMarket|StopLimit|SetTrailStop|SetProfitTarget` grep exit=1 (E2) | yes |

Precedence by line order inside `OnBarUpdate`: (1) session flat :234-239 (`return`); (2) stop :250-269 (`return` after `XStop`, so no checkpoint exit and no entry on the stop's decision bar); (3) checkpoint :272-310. The stop is not decided on the early-close last bar (`!isSessionLastBar`, :244/:250), given that `Bars.IsLastBarOfSession` is true on that bar, which is UNVERIFIED (item 4). The 16:00 bar, and the 15:59 bar under Flat1559, return at (1) before the stop.

### E3. Line-by-line code diff against the base (comments, blank lines and indentation removed)

`S/strip.sh` is `sed -e 's#[[:space:]]*//.*$##' -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' "$1" | grep -v '^$'`. I checked that no string literal in either file contains `//`: the only `"…//` matches are base :227/:229, where the `//` is a trailing comment after the string. The `Description` and `SetDefaults` hunks are excluded from T6(i) by spec :190 and appear here for completeness.

~~~
$ diff <(strip ninjascript/PraxisNoiseAreaBreakout.cs) <(strip ninjascript/PraxisNoiseAreaBreakoutArmB.cs)   # strip = scratchpad/strip.sh: delete // comments, blank lines, indentation
19c19
< public enum PraxisNoiseExitMode
---
> public enum PraxisNoiseArmBExitPolicy
20a21
> BandOrVWAP,
22c23
< BandOrVWAP
---
> Flat1559
24c25
< public class PraxisNoiseAreaBreakout : Strategy
---
> public class PraxisNoiseAreaBreakoutArmB : Strategy
26,28c27,32
< #region Fixed session clock (trader-locked; not exposed)
< private const int OpenMod  = 9 * 60 + 30;
< private const int CloseMod = 16 * 60;
---
> #region Fixed session clock (not exposed)
> private const int OpenMod    = 9 * 60 + 30;
> private const int CloseMod   = 16 * 60;
> private const int FlattenMod = CloseMod - 1;
> private const int OracleMod  = 10 * 60;
> private const int AtrPeriod  = 14;
34a39,41
> public double High;
> public double Low;
> public double PrevClose;
38,39d44
< private const int Lookback = 14;
< private const double BandSigmaMult = 1.0;
49a55,68
> private double atrSum;
> private double curAtr;
> private bool   haveAtr;
> private MarketPosition stopSide = MarketPosition.Flat;
> private double stopFill;
> private double stopAtrSum;
> private double stopLevel;
> private bool   haveStopLevel;
> private static readonly DateTime[] OracleDates =
> {
> new DateTime(2021, 6, 15),
> new DateTime(2024, 12, 26),
> new DateTime(2026, 3, 18)
> };
55,56c74,75
< Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET.";
< Name         = "PraxisNoiseAreaBreakout";
---
> Description  = "PRAXIS walk-forward arm (b) Noise-Area Breakout: base logic with tunable Lookback, noise multiplier, bar-close daily-ATR stop and exit policy (BandOrVWAP / OppBand / Flat1559). D-2026-11-07-B. WRITTEN, not compiled, not run.";
> Name         = "PraxisNoiseAreaBreakoutArmB";
66,67c85,89
< ExitMode      = PraxisNoiseExitMode.BandOrVWAP;
< Contracts     = 1;
---
> Lookback    = 14;
> NoiseMult   = 1.0;
> StopAtrMult = 0.0;
> ExitPolicy  = PraxisNoiseArmBExitPolicy.BandOrVWAP;
> Contracts   = 1;
79a102,124
> history.Clear();
> today         = null;
> todayOpen     = 0.0;
> prevClose     = 0.0;
> haveDay       = false;
> vwapCumPV     = 0.0;
> vwapCumVol    = 0.0;
> curUpper      = 0.0;
> curLower      = 0.0;
> curVwap       = 0.0;
> curSigma      = 0.0;
> haveBand      = false;
> atrSum        = 0.0;
> curAtr        = 0.0;
> haveAtr       = false;
> stopSide      = MarketPosition.Flat;
> stopFill      = 0.0;
> stopAtrSum    = 0.0;
> stopLevel     = 0.0;
> haveStopLevel = false;
> Print(string.Format(CultureInfo.InvariantCulture,
> "{0} INPUTS Lookback={1} NoiseMult={2:R} StopAtrMult={3:R} ExitPolicy={4} Contracts={5}",
> Name, Lookback, NoiseMult, StopAtrMult, ExitPolicy, Contracts));
89a135
> ComputeAtr();
92a139,140
> today.High = High[0];
> today.Low  = Low[0];
94a143
> today.PrevClose = prevClose;
101a151,152
> today.High      = Math.Max(today.High, High[0]);
> today.Low       = Math.Min(today.Low, Low[0]);
118c169,172
< if (mod >= CloseMod)
---
> if (mod == OracleMod && Array.IndexOf(OracleDates, Time[0].Date) >= 0)
> PrintOracle();
> int flatMod = (ExitPolicy == PraxisNoiseArmBExitPolicy.Flat1559) ? FlattenMod : CloseMod;
> if (mod >= flatMod)
120c174
< FlattenAll("16:00 session flat");
---
> FlattenAll("session flat");
122a177,197
> bool isSessionLastBar = Bars.IsLastBarOfSession;
> if (StopAtrMult > 0.0 && haveStopLevel && !isSessionLastBar
> && Position.MarketPosition == stopSide && Position.MarketPosition != MarketPosition.Flat)
> {
> if (stopSide == MarketPosition.Long)
> {
> if (AtrPeriod * (stopFill - Close[0]) >= StopAtrMult * stopAtrSum)
> {
> ExitLong("XStop", "");
> return;
> }
> }
> else if (stopSide == MarketPosition.Short)
> {
> if (AtrPeriod * (Close[0] - stopFill) >= StopAtrMult * stopAtrSum)
> {
> ExitShort("XStop", "");
> return;
> }
> }
> }
130,132c205,210
< double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
< ? Math.Max(curUpper, curVwap) : curUpper;
< if (price <= stop)
---
> double trail;
> if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
> trail = curLower;
> else
> trail = (vwapCumVol > 0) ? Math.Max(curUpper, curVwap) : curUpper;
> if (price <= trail)
137,139c215,220
< double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
< ? Math.Min(curLower, curVwap) : curLower;
< if (price >= stop)
---
> double trail;
> if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
> trail = curUpper;
> else
> trail = (vwapCumVol > 0) ? Math.Min(curLower, curVwap) : curLower;
> if (price >= trail)
141a223,225
> bool atrGateOpen = (StopAtrMult <= 0.0) || haveAtr;
> if (atrGateOpen)
> {
147c231,255
< #region Band construction (spec §1, pp.6-7)
---
> }
> protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity,
> MarketPosition marketPosition, string orderId, DateTime time)
> {
> if (execution.Order == null || execution.Order.OrderState != OrderState.Filled)
> return;
> string name = execution.Order.Name;
> if (name != "L" && name != "S")
> return;
> if (!(StopAtrMult > 0.0) || !haveAtr)
> return;
> bool isLong   = (name == "L");
> stopSide      = isLong ? MarketPosition.Long : MarketPosition.Short;
> stopFill      = execution.Order.AverageFillPrice;
> stopAtrSum    = atrSum;
> stopLevel     = isLong
> ? stopFill - StopAtrMult * (stopAtrSum / AtrPeriod)
> : stopFill + StopAtrMult * (stopAtrSum / AtrPeriod);
> haveStopLevel = true;
> Print(string.Format(CultureInfo.InvariantCulture,
> "{0} ENTRY {1} {2} FILL={3:R} ATR={4:R} LEVEL={5:R}",
> Name, time.ToString("yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture),
> isLong ? "LONG" : "SHORT", stopFill, curAtr, stopLevel));
> }
> #region Band construction (as base; Lookback and NoiseMult are inputs)
170,171c278,279
< curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
< curLower = refLower * (1.0 - BandSigmaMult * curSigma);
---
> curUpper = refUpper * (1.0 + NoiseMult * curSigma);
> curLower = refLower * (1.0 - NoiseMult * curSigma);
176c284,314
< #region Session commit / flatten
---
> #region Daily ATR (completed RTH sessions; no second series, no NT8 ATR indicator)
> private void ComputeAtr()
> {
> haveAtr = history.Count >= AtrPeriod;
> if (!haveAtr)
> return;
> double sum = 0.0;
> for (int i = history.Count - AtrPeriod; i <= history.Count - 1; i++)
> {
> DayRecord rec = history[i];
> sum += Math.Max(rec.High, rec.PrevClose) - Math.Min(rec.Low, rec.PrevClose);
> }
> atrSum = sum;
> curAtr = atrSum / AtrPeriod;
> }
> #endregion
> #region Oracle print (T6(ii))
> private void PrintOracle()
> {
> string band = haveBand
> ? string.Format(CultureInfo.InvariantCulture, "SIGMA={0:R} UPPER={1:R} LOWER={2:R}", curSigma, curUpper, curLower)
> : "NOBAND";
> string atr = haveAtr
> ? string.Format(CultureInfo.InvariantCulture, "ATR={0:R}", curAtr)
> : "NOATR";
> Print(string.Format(CultureInfo.InvariantCulture,
> "{0} ORACLE {1} 10:00 Lookback={2} NoiseMult={3:R} {4} {5}",
> Name, Time[0].Date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture), Lookback, NoiseMult, band, atr));
> }
> #endregion
> #region Session commit / flatten (as base)
195c333
< #region Properties (paper-fixed defaults; ExitMode is the only intended knob)
---
> #region Properties
197,198c335,337
< [Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-side band; BandOrVWAP = max/min(band, VWAP), the paper's PREFERRED model (spec §4 p.13). Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 1)]
< public PraxisNoiseExitMode ExitMode { get; set; }
---
> [Range(2, 60)]
> [Display(Name = "Lookback (sessions)", Description = "Completed sessions in the per-minute sigma mean. Default = arm (a) value; grid per spec §3.", GroupName = "02. Praxis (tunable)", Order = 1)]
> public int Lookback { get; set; }
199a339,349
> [Range(0.1, 5.0)]
> [Display(Name = "Noise multiplier", Description = "Band half-width multiplier on sigma. Default 1.0 (arm a). Grid {0.8, 1.0, 1.2}.", GroupName = "02. Praxis (tunable)", Order = 2)]
> public double NoiseMult { get; set; }
> [NinjaScriptProperty]
> [Range(0.0, 10.0)]
> [Display(Name = "Stop ATR multiplier", Description = "Stop at entry fill -/+ m x daily ATR, bar-close check, market exit. 0 = no stop (acceptance tests T1-T3 only). Grid {1.5, 2.25, 3.0}.", GroupName = "02. Praxis (tunable)", Order = 3)]
> public double StopAtrMult { get; set; }
> [NinjaScriptProperty]
> [Display(Name = "Exit policy", Description = "BandOrVWAP = max/min(band, VWAP) trail; OppBand = opposite band; Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar. Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 4)]
> public PraxisNoiseArmBExitPolicy ExitPolicy { get; set; }
> [NinjaScriptProperty]
201c351
< [Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). Paper uses 2% vol-target sizing (§3 p.15), not ported this pass.", GroupName = "02. Praxis (tunable)", Order = 2)]
---
> [Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only).", GroupName = "02. Praxis (tunable)", Order = 5)]
diff exit=1
~~~

### E4. Negative test: the T6(i) checks fire on mutants

Header paraphrase: the block was produced by `for f in <real file> mut/M1.cs … mut/M4.cs; do echo "===== …"; ./checks.sh $f; done 2>&1 | tee negtest.txt`, where `S/checks.sh` runs C1 `awk -f branchscan.awk`, C2 `grep -nE '(Enter|Exit)(Long|Short)\([[:space:]]*[0-9]'`, C3 `grep -nE NoiseMult | grep -E 'stopFill|stopAtrSum|stopLevel|atrSum|curAtr'` and C4 the forbidden-identifier grep. Mutants (one line each, from `sed` on the final file, in `S/mut/`): M1 `ExitPolicy` read under `StopAtrMult <= 0.0` (:283); M2 literal quantity `EnterLong(1, "L")` (:307); M3 `NoiseMult` in the long stop check (:255); M4 `XL` exit only when `StopAtrMult == 0.0` (:288). In M1 the scanner also lists :294 and :299. Its handling of a single-statement `if` runs on into the next lines there. That over-reports, which is the safe direction; it is a limit of the scanner, not a finding about the file.

~~~
===== PraxisNoiseAreaBreakoutArmB.cs (diff vs real: 0 line)
C1 branch scan:
IN-BRANCH(cond:250) 257: ExitLong("XStop", "");
IN-BRANCH(cond:250) 265: ExitShort("XStop", "");
IN-BRANCH(cond:304) 307: EnterLong(Contracts, "L");
IN-BRANCH(cond:304) 309: EnterShort(Contracts, "S");
C2 literal quantity:
C3 NoiseMult in stop:
C4 forbidden ids:
===== M1.cs (diff vs real: 1 line)
C1 branch scan:
IN-BRANCH(cond:250) 257: ExitLong("XStop", "");
IN-BRANCH(cond:250) 265: ExitShort("XStop", "");
IN-BRANCH(cond:283) 283: if (StopAtrMult <= 0.0 && ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
IN-BRANCH(cond:283) 294: if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
IN-BRANCH(cond:283) 299: ExitShort("XS", "");
IN-BRANCH(cond:304) 307: EnterLong(Contracts, "L");
IN-BRANCH(cond:304) 309: EnterShort(Contracts, "S");
C2 literal quantity:
C3 NoiseMult in stop:
C4 forbidden ids:
===== M2.cs (diff vs real: 1 line)
C1 branch scan:
IN-BRANCH(cond:250) 257: ExitLong("XStop", "");
IN-BRANCH(cond:250) 265: ExitShort("XStop", "");
IN-BRANCH(cond:304) 307: EnterLong(1, "L");
IN-BRANCH(cond:304) 309: EnterShort(Contracts, "S");
C2 literal quantity:
307: EnterLong(1, "L");
C3 NoiseMult in stop:
C4 forbidden ids:
===== M3.cs (diff vs real: 1 line)
C1 branch scan:
IN-BRANCH(cond:250) 257: ExitLong("XStop", "");
IN-BRANCH(cond:250) 265: ExitShort("XStop", "");
IN-BRANCH(cond:304) 307: EnterLong(Contracts, "L");
IN-BRANCH(cond:304) 309: EnterShort(Contracts, "S");
C2 literal quantity:
C3 NoiseMult in stop:
255: if (AtrPeriod * (stopFill - Close[0]) >= NoiseMult * stopAtrSum)
C4 forbidden ids:
===== M4.cs (diff vs real: 1 line)
C1 branch scan:
IN-BRANCH(cond:250) 257: ExitLong("XStop", "");
IN-BRANCH(cond:250) 265: ExitShort("XStop", "");
IN-BRANCH(cond:288) 288: { if (StopAtrMult == 0.0) ExitLong("XL", ""); }
IN-BRANCH(cond:304) 307: EnterLong(Contracts, "L");
IN-BRANCH(cond:304) 309: EnterShort(Contracts, "S");
C2 literal quantity:
C3 NoiseMult in stop:
C4 forbidden ids:
~~~

### E5. The s1-drop evidence the BLOCKING fix rests on, and the fix's code diff

~~~
$ sed -n 89p docs/reports/2026-10-30-3gm-worker3-adversarial-d1.md
- **R19 fallback unreachable.** .cs:140 returns when `CurrentBar < 1`, so `CurrentBar >= 1` always holds at .cs:155. **Claim confirmed.** The "first session never committed" consequence is also correct: `CommitDay` sees `today == null`.
$ diff S/armb.strip S/armb2.strip   # W1 final file (b04f4488) vs W4 fixed file (923e0dc9), both through S/strip.sh
41c41
< public double LastClose;
---
> public double PrevClose;
142a143
> today.PrevClose = prevClose;
152d152
< today.LastClose = Close[0];
287c287
< haveAtr = history.Count >= AtrPeriod + 1;
---
> haveAtr = history.Count >= AtrPeriod;
294,295c294
< double pc = history[i - 1].LastClose;
< sum += Math.Max(rec.High, pc) - Math.Min(rec.Low, pc);
---
> sum += Math.Max(rec.High, rec.PrevClose) - Math.Min(rec.Low, rec.PrevClose);
diff exit=1
$ grep -o "[{}]" S/armb.strip | sort | uniq -c; grep -o "[{}]" S/armb2.strip | sort | uniq -c   # code-only braces before / after
  65 {
  65 }
  65 {
  65 }
$ cmp S/armb2.strip S/armb3.strip; echo "cmp exit=$?"   # fixed file at fix time vs at final evidence time
cmp exit=0
~~~

### E6. Oracle sessions and session numbering, observed on the data file

The block's first header line paraphrases the loop; the loop as run printed `<date> 10:00-bar-lines=<n> rth-bars=<n>`. The second header line (in parentheses) is a description: the command was the `awk -F'[ ;]' … | uniq | python3 -I -c` pipeline shown in E10's first header, with `weekday() < 5` kept and `ds.index(t)+1` printed.

~~~
$ for d in 20210615 20241226 20260318; do grep -c "^$d 100000;" "$D"; awk -F"[ ;]" -v d=$d "\$1==d && \$2+0>=93100 && \$2+0<=160000" "$D" | wc -l; done   # D = /Users/admin/praxis-signals/b2-data/NQCONTROW 09-25.Last.txt
20210615 10:00-bar-lines=1 rth-bars=390
20241226 10:00-bar-lines=1 rth-bars=390
20260318 10:00-bar-lines=1 rth-bars=390
$ (Mon-Fri dates 20210308..20260717 with a 09:31-16:00 bar) -> session index
20210308 s1
20210329 s16
20210615 s70
20241226 s967
20260318 s1267
N = 1352
~~~

### E7. Worker spawn/close times (DISPATCH_LOG hook rows)

Header paraphrase: `<5 ids>` stands for the five ids in the table above and `...` for the regex `[^|]*|[^|]*| WHERE: [^|]*corr=` and the sed `s/^- \[([^]]*)\].*WHAT: subagent ([a-z]+).*/\1 \2/`.

~~~
$ for c in <5 ids>; do grep -o "^- \[[^]]*\] WHO: praxis-worker | WHAT: subagent [a-z]*...corr=$c" DISPATCH_LOG.md | sed -E "s/.../\1 \2/"; done
2026-11-07T16:03:57Z spawned 2026-11-07T16:06:48Z closed  <- a62d9c20c6a9ec05b
2026-11-07T16:08:17Z spawned 2026-11-07T16:14:01Z closed  <- a7fd134e7741a41fe
2026-11-07T16:08:30Z spawned 2026-11-07T16:11:10Z closed  <- a4f79d9f2118a9253
2026-11-07T16:14:52Z spawned 2026-11-07T16:15:41Z closed  <- ad816d85d3e9e4734
2026-11-07T16:16:10Z spawned 2026-11-07T16:22:20Z closed  <- a30cab8c6c10d8e0c
$ cat S/dnc_written_at.txt   # date -u at the moment the Does NOT cover section was written
2026-11-07T16:08:00Z
~~~

### E8. MANIFEST rows appended

~~~
$ git diff MANIFEST.md | grep "^[+-]" | cut -c1-200; sed -n 269,270p MANIFEST.md | cut -c1-60
--- a/MANIFEST.md
+++ b/MANIFEST.md
+| /ninjascript/PraxisNoiseAreaBreakoutArmB.cs | Source | 2 | 2026-11-07 | Walk-forward arm (b) tunable variant of PraxisNoiseAreaBreakout (inputs Lookback, NoiseMult, StopAtrMult, ExitPolicy {BandOrV
+| /docs/reports/2026-11-07-arm-b-code-manager.md | Report | 2 | 2026-11-07 | Manager report for unit 2026-11-07-arm-b-code; ungraded at time of row |
| /ninjascript/PraxisNoiseAreaBreakoutArmB.cs | Source | 2 |
| /docs/reports/2026-11-07-arm-b-code-manager.md | Report | 
~~~

### E9. De-identification token probe (counts only) and the S13 sentence count

Method of `docs/reports/2026-11-07-rulings-filing-manager.md:113-118`, with the same script, `S/tokprobe2.sh`. The candidates are held in a shell variable only, and the output is counts and line numbers only. The liveness arms run first, on the two known locations. The probe ran on this report while the report still held this block's placeholder line, so the report row covers every other line of the report. The candidate count is 12 here and 13 in the cited report because the candidate set is derived from HEAD files, and HEAD has moved since then; both liveness arms hit all 12. The S13 count line was printed by `printf "%s count=%s lines=%s\n" $f $(/usr/bin/grep -c -F "$SENT" $f) "$(/usr/bin/grep -n -F "$SENT" $f | cut -d: -f1 | tr '\n' ',')"`, where `$SENT` holds the standing sentence. The header shows it as `<standing sentence>` so that the sentence is not repeated. The block above ran before the W6 fixes. Re-run on the report after them (a Bash call, output pasted; this note itself adds no candidate token): `docs/reports/2026-11-07-arm-b-code-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none`.

~~~
$ bash S/tokprobe2.sh ninjascript/PraxisNoiseAreaBreakoutArmB.cs docs/reports/2026-11-07-arm-b-code-manager.md MANIFEST.md:269,270
candidates=12
LIVENESS HEAD:DECISION_LOG.md tokens_hit=12 confined_tokens_hit=2 lines=47,77,89,143,259,464,500,501,535,640,47,153,317,496,47,47,47,161,47,47,119,47,47,61,47,47,47,
LIVENESS 7d9be8e:HANDOFF.md tokens_hit=12 confined_tokens_hit=2 lines=9,7,9,302,9,23,277,24,426,20,9,14,9,9,15,20,
ninjascript/PraxisNoiseAreaBreakoutArmB.cs tokens_hit=0 confined_tokens_hit=0 lines=none
docs/reports/2026-11-07-arm-b-code-manager.md tokens_hit=0 confined_tokens_hit=0 lines=none
MANIFEST.md[269,270] tokens_hit=0 confined_tokens_hit=0 lines=none
$ /usr/bin/grep -c -F "<standing sentence>" <file>; /usr/bin/grep -n -F ... | cut -d: -f1
docs/reports/2026-11-07-arm-b-code-manager.md count=1 lines=3,
ninjascript/PraxisNoiseAreaBreakoutArmB.cs count=0 lines=
$ /usr/bin/grep -n -E "\$[0-9]|197,327|210,182|193,017" ninjascript/PraxisNoiseAreaBreakoutArmB.cs; echo "exit=$?"   # no figure in the code
exit=1
~~~

### E10. Data-file facts and W1's file (added after W6)

~~~
$ awk -F"[ ;]" '$1>=20210308 && $1<=20260717 && $2+0>=93100 && $2+0<=160000 {print $1}' "$D" | uniq | python3 -I -c "<count dates whose weekday() >= 5>"
weekend-dated dates with a 09:31-16:00 bar: 141 first three: ['20210314', '20210320', '20210328']
$ for d in 20241224 20250120 20250619; do awk -F"[ ;]" -v d=$d '$1==d && $2+0>=93100 && $2+0<=160000 {t=$2} END {print d, "last 09:31-16:00 bar stamp:", t}' "$D"; done
20241224 last 09:31-16:00 bar stamp: 131500
20250120 last 09:31-16:00 bar stamp: 130000
20250619 last 09:31-16:00 bar stamp: 130000
$ sed -n "1,4p;/braces/,+1p" S/t6i_greps.txt   # captured on W1's final file, before the fix
$ wc -l ninjascript/PraxisNoiseAreaBreakoutArmB.cs; shasum -a 256 ...
     461 PraxisNoiseAreaBreakoutArmB.cs
b04f44882ff261c1edf35ce436c7b4eb0e0a0ef9e421408747d0d870fbb22a63  PraxisNoiseAreaBreakoutArmB.cs
$ grep -n -E "BandSigmaMult|const int Lookback|PraxisNoiseExitMode" ninjascript/PraxisNoiseAreaBreakoutArmB.cs; echo "exit=$?"
$ braces
{ 70  } 70
~~~

## Does NOT cover / UNVERIFIED

Written before either adversarial pass was dispatched. Timestamp in the process log, from `date -u`.

1. **Compile.** Nothing here was compiled. There is no C# compiler on this Mac (the master OBSERVED `dotnet` / `csc` / `mcs` / `mono` not found). Whether NT8 accepts the file is UNVERIFIED. In particular: the `OnExecutionUpdate` override signature, `Bars.IsLastBarOfSession`, `Order.AverageFillPrice`, `OrderState.Filled` and the `[Range(0.0, 10.0)]` / `[Range(0.1, 5.0)]` attributes on doubles.
2. **NT8 event order (fill mechanics).** The stop is checked "from the bar the entry filled on" (spec T8). That assumes NT8, in a historical run, calls `OnExecutionUpdate` for the entry fill before it calls `OnBarUpdate` for the bar the entry filled on. UNVERIFIED. If the order is the other way round, the first stop check moves one bar later.
3. **Fill mechanics.** These are assumed, not observed: market exits (`XStop`, `XL`, `XS`, `FlatEOD`) fill at the next bar's open with 2 ticks of slippage; `AverageFillPrice` includes that slippage, as the trade list's fill does; a managed reversal fills its entry under the signal name `L` / `S` (the "Close position" leg is ignored by name); `OrderState` is `Filled` when the last execution arrives. All UNVERIFIED. T8's calibration step refits the fill rules from T1/T3.
4. **Early-close detection source.** The session-flat bar F on early-close days (12:00 / 12:15 / 14:03) is detected only by `Bars.IsLastBarOfSession`. That this is true on that bar in a historical run is UNVERIFIED. If it is false there, a stop could be decided on F. T9 catches that only if a first crossing falls on such a bar.
5. **Early-close checkpoint (a reading for the master, not decided here).** §4 / T8 say step (3), the checkpoint exits and entries, "is skipped on a bar where (1) … fired". The base runs its checkpoint code on an early-close last bar, including 12:00, which is a checkpoint. ArmB keeps the base behaviour so that the m = 0 path trades exactly as the base (T1–T3). On such a bar, ArmB only suppresses the stop decision. Whether NT8 acts on an order submitted there is UNVERIFIED. So is whether a resulting fill lands in the next session; if it did, the level would use the next session's ATR.
6. **`[Range]` and the bridge.** Whether `[Range]` rejects a value set through the bridge's `params` is UNVERIFIED. If it does not, a negative `StopAtrMult` would switch the stop and the ATR gate off with no error. The T5(i) readback print is the only guard.
7. **Optimizer reuse.** `IsInstantiatedOnEachOptimizationIteration = false` is kept from the base. ArmB resets its state at `State.DataLoaded`; that `DataLoaded` runs on every iteration is UNVERIFIED. This matters only if the Strategy Analyzer optimizer is used. The bridge's single runs are assumed to be separate instances (UNVERIFIED).
8. **Exact-tie comparison.** The stop check is `AtrPeriod × (fill − Close) ≥ m × atrSum`, which is the spec's `Close ≤ fill − m × ATR` rearranged. It is exact in binary only if fills, closes and true ranges are exact 0.25 multiples and m is a 0.25 multiple. That holds for the grid's m. That NT8's fill prices are exact 0.25 multiples is UNVERIFIED.
9. **Oracle sessions.** T6(ii) needs three sessions, named here before the run: 2021-06-15, 2024-12-26 (the session after the 2024-12-24 early close) and 2026-03-18. This unit chose them; the choice is changeable. That each is in the data file with a 10:00 bar, after s19, is INFERRED from the calendar only. The data file was not read in this unit.
10. **m = 0 equivalence (T1–T3).** At WRITTEN level this is argued by logic diff only. No run. The figures 1,190 / 810 / 1,190 trades and their nets are the committed runs' figures, not produced by this file.
11. **Everything T1–T13 runs.** T1–T5, T6(ii), T7 and T8–T13 run on the VM after 2a. None ran here. T6(i) is a reading and misses the things spec :191 lists, including a right property inside a wrong formula and a stop gated on m's magnitude.
12. **Not resolved here:** F2 × Flat1559 (a Flat1559 position runs past breaker #4's 11:30 and breaker #5's 15:00), as D-2026-11-07-B records at DECISIONS.md:1452.

**Post-pass updates.** These were added after the passes. Items 1–12 above are unchanged except for one pointer: item 11's `:190` was corrected to `:191` after W6 (the "Does NOT catch" line is :191).
- Item 9 is now OBSERVED, not INFERRED. On the data file the three sessions are s70, s967 and s1267, each with a 10:00 bar and 390 bars from 09:31 to 16:00 (E6). All three come after s20, the first session with a band at Lookback 18.
- Item 13 (W5 NOTE-3): the data file has weekend-dated bars inside 09:31–16:00: 141 such dates, first 2021-03-14 (E10). That the RTH session template drops them is INFERRED. If it does not, they enter the history store and the ATR, and they shift the warm-up.
- Item 14 (W2/W5): on early-close days the ATR true range uses the bars NT8 delivers for the session. That this means up to NT8's last bar, 12:00 / 12:15 / 14:03 (results report :133, :149-154), is INFERRED (item 4). The data file runs to 13:15 on 2024-12-24 and to 13:00 on 2025-01-20 and 2025-06-19 (E10). The T6(ii)/T8 oracle must cut those sessions where NT8 does, or it will disagree with correct code on those days and the 14 sessions after each.
- Item 15 (W3 S1): the enum's numeric order is {BandOrVWAP = 0, OppBand = 1, Flat1559 = 2}, as the brief specifies. The base enum is {OppBand = 0, BandOrVWAP = 1}. A bridge that sends the policy by number rather than by name would pick the wrong policy. How the bridge converts enums is UNVERIFIED.

## Adversarial findings and fixes

**W2, pass A: VERDICT: FAIL.**
- BLOCKING: the ATR gate opens at s17 instead of s16, because s1 is never committed and the gate required 15 records. **Fixed** by W4 (E5). Re-attacked by W5: `haveAtr` is first true at s16 (2021-03-29), with 14 true ranges from s2…s15. W5's trace, quoted: "sum 4170.0, ATR 297.857". That is W5's scratch-script output; I did not re-run it.
- MINOR: the early-close ATR may not match an oracle that reads the data file's bars → spec/oracle note, item 14. No code change.
- MINOR: the checkpoint code still runs on a 12:00 early-close last bar → Still the master's, item 1. No code change.
- MINOR: an entry decided on a session's last bar that fills on the next session's first bar would take the previous session's ATR. This is reachable only through the early-close case → already in item 5. No code change.
- Items (a)–(c) and (e)–(i): "no break", with line numbers. These agree with the T6(i) table above.

**W3, pass B: VERDICT: PASS.** No BLOCKING difference for T1 (BandOrVWAP vs the base), T2 (OppBand vs `_OppBand.cs`, including at `vwapCumVol == 0`) or T3 (Flat1559 vs `_Flat1559.cs`, `mod >= 959`). All 17 shared differences are graded NON-BLOCKING or COSMETIC, each with its guard line, for example the stop block guarded by `StopAtrMult > 0.0` at :250 and `OnExecutionUpdate` returning at :323. The SetDefaults settings are identical value for value. W3 ran before the fix. The fix touches only `ComputeAtr`, the `DayRecord` field and one bookkeeping line, none of which the m = 0 path reads for trading. W5 re-checked the m = 0 path after the fix: "matches the base and both variants line for line in what it does".

**W6, report adversary: VERDICT: FAIL.** Every pasted command it re-ran matched, and every ArmB pointer but one was correct. Its defects were: a D-2026-11-07-B `:161` pointer that did not say it counts inside the entry; spec `:190` where `:191` is meant; command headers paraphrased without saying so (E4, E6, E7, E9); the 70-brace count and the data-file facts unpasted; four NT8-behaviour sentences without a qualifier; an incomplete `NoiseMult` line list; and "nets quoted" where none are. **All fixed in place in this report.** The new evidence is in E10; the qualifiers are added where each sentence stands.

**W5, pass A2: VERDICT: PASS.** 0 BLOCKING/MAJOR. MINOR-1 = the early-close checkpoint (Still the master's, item 1). NOTE-1 = the spec's session numbers (Still the master's, item 2). NOTE-2 = item 14. NOTE-3 = item 13. NOTE-4: the file is untracked on `main`, not yet on `arm-b/wf-tunables`; that is by design, since the master cuts the branch.

**Additions beyond the spec text.** None changes a trade at any m; each was argued by W3 and re-read by W5.
- (1) Every state field is reset at `State.DataLoaded` (:145-167), because the base's `IsInstantiatedOnEachOptimizationIteration = false` reuses instances. On a fresh instance this is an identity.
- (2) The stop check is written as `AtrPeriod × (fill − Close) ≥ m × atrSum` (:255, :263). This is the spec's `Close <= fill − m × ATR` rearranged so that an exact tie compares exactly, which T8 demands ("A build whose floating-point comparison disagrees at an exact tie fails T8"). The printed level (:331-332) is the spec's form.
- (3) The print formats (:170-172, :335-338, :395-406).
- (4) The three oracle dates, chosen by this unit as spec :190 delegates.
- (5) `HistoryCap` keeps the base's getter syntax. `OracleMod = 10 * 60` is a named constant.

## Still the master's (spec readings, not decided here)

1. **Early-close checkpoint.** §4 and T8 say the checkpoint step "is skipped on a bar where (1) or (2) fired". On an early-close last bar that is also a checkpoint (12:00; on 2025-01-20 and 2025-06-19 per the results report :149-154), the base runs its checkpoint code. ArmB does the same, so that T1–T3 stay exact; it suppresses only the stop there (:244, :250). Skipping step (3) on that bar for all m could change the m = 0 trades against the committed files. Whether it would is UNVERIFIED, because it depends on what NT8 does with an order placed on the session-close bar. Skipping it only when m > 0 would put order calls inside a `StopAtrMult` branch, which T6(i) forbids. A ruling may need a DECISIONS.md entry. None was written.
2. **Spec session numbers are one session early.** The base never commits s1, so the band first exists at s(L+2), not s(L+1): s12 / s16 / s20 at Lookback 10 / 14 / 18 (W5 trace; consistent with E6's s16 = 2021-03-29 = T1's first entry). Spec §5 :85 ("from s19 at lookback 18") and T11 :200 ("Lookback 10 (band from s11) or 14 (band from s15)"; "at 18 the band (s19)") are each one session early. Consequence: T11(i) can be tested only at Lookback 10, in s12–s15, and the T6(ii)/T11 oracle must model the s1 drop. The ATR claim "from s16" stands. The code as written meets it, by reading and W5's trace (not run; subject to item 13).
3. Items 13–15 above (weekend bars, early-close cut in the oracle, enum numeric order) are inputs to the VM/oracle units, not code changes.

## Still Amear's

None raised by this unit. Every SETTLED value used here (the stop values, the `StopAtrMult = 0` input rule, ATR computation, level, evaluation, warm-up, no entry on the stop bar, precedence, file and enum names, the input ranges) remains a delegated settlement under R-1104-2 and is changeable by him, as spec §3/§4/§9 records. That is not a new question.

## S6 cross-block check

~~~
$ /usr/bin/find . -path ./.git -prune -o -type f -newermt "2026-11-07 16:00:00 UTC" -print | sort
./DISPATCH_LOG.md
./MANIFEST.md
./ninjascript/PraxisNoiseAreaBreakoutArmB.cs
$ stat -f "%Sm %N" -t "%Y-%m-%dT%H:%M:%S%z" specs/SPEC_RUBRIC.md DECISIONS.md MANIFEST.md ninjascript/*.cs
2026-11-06T15:19:10-0500 specs/SPEC_RUBRIC.md
2026-11-07T10:40:09-0500 DECISIONS.md
2026-11-07T11:24:17-0500 MANIFEST.md
2026-10-31T07:15:48-0400 ninjascript/PraxisLastHalfHourMomentum.cs
2026-07-16T15:39:15-0400 ninjascript/PraxisNoiseAreaBreakout.cs
2026-11-07T11:15:11-0500 ninjascript/PraxisNoiseAreaBreakoutArmB.cs
2026-10-31T06:29:18-0400 ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
2026-10-31T06:25:09-0400 ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
2026-07-15T15:52:29-0400 ninjascript/PraxisSignalConsumer.cs
$ git diff --name-only HEAD -- DECISIONS.md ninjascript/ vm/ specs/
specs/SPEC_RUBRIC.md
~~~

- **F1–F4 (specs/SPEC_RUBRIC.md FROZEN) untouched.** `specs/SPEC_RUBRIC.md` shows as modified against HEAD, but its mtime is 2026-11-06T15:19:10-0500. That is before this unit, and the file is not in the find list of files modified since 16:00Z. The modification is pre-existing.
- **F2 × Flat1559: named, not resolved.** A Flat1559 position runs past breaker #4's 11:30 and breaker #5's 15:00 and flattens on the 15:59 bar. This file implements Flat1559 exactly as `_Flat1559.cs` does (W3 T3 table) and adds no breaker logic. D-2026-11-07-B records the interaction as open at DECISIONS.md:1452 (line 161 of the entry).
- **F3 fill terms untouched.** No fill, slippage or commission setting is in the file. The SetDefaults settings match the base value for value (W3 S3; E3 shows no SetDefaults hunk other than Name, Description and the input defaults). The stop places no resting order (E2 grep exit=1) and exits through `ExitLong`/`ExitShort`, a market order per ruling 1 of 2026-11-05; that it fills on the next bar is UNVERIFIED (item 3).
- **Cost model untouched.** No fees or commission file is in the modified list. The only files modified since 16:00Z are the new file, MANIFEST.md (this unit's two rows) and DISPATCH_LOG.md. The DISPATCH_LOG rows are written by the SubagentStart/SubagentStop hook (`./scripts/dispatch-log-writeahead.sh`, wired at `.claude/settings.json:140`), not by this unit's workers (E7).
- **Base files untouched on main.** The shas before (E1) and after (E2) are identical. `git diff --name-only HEAD -- DECISIONS.md ninjascript/ vm/ specs/` lists only the pre-existing `specs/SPEC_RUBRIC.md`. The new file is untracked. The branch commit is meant to hold only the new file; the report and MANIFEST rows go to main.
- **Breaker / bridge blocks.** The file adds only print output (T5(i), T6(ii)). It writes no file and places no order outside the strategy's own position. The bridge's `params` must carry all five inputs by name (spec §7; items 6 and 15).

## Files staged

Nothing. This unit staged nothing and committed nothing. The real index still holds only the 12 pre-existing paths, none under `ninjascript/` (E2: `git diff --cached --name-only | wc -l` = 12, `| grep -c ninjascript` = 0). Working-tree changes left for the master:
- `ninjascript/PraxisNoiseAreaBreakoutArmB.cs`: new, untracked. 462 lines, sha256 `923e0dc9ca61caae918c44ab4a6e7ac4d6f8bebb55554fe581f7605f04054028`.
- `MANIFEST.md`: two rows appended, :269-270.
- `docs/reports/2026-11-07-arm-b-code-manager.md`: this report, untracked.

## Result: PASS

PASS at WRITTEN level only, against the brief's deliverables and the T6(i) static check. It is not a compile result, a test result or a backtest result. Open for the master: Still the master's items 1–2.
