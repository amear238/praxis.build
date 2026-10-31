# 7zq M2 worker 5 — FIX report: PraxisLastHalfHourMomentum (A), hand-test checklist (B), decisions addendum (C)

## Task
Apply the fixes the manager pinned for the worker-4 adversarial findings (`docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md`, verdict BROKEN: MAJOR 1–2, MINOR 3–7) to A `ninjascript/PraxisLastHalfHourMomentum.cs`, B `docs/reports/2026-10-31-7zq-m2-handtest-checklist.md` and C `docs/reports/2026-10-31-7zq-m2-decisions-addendum.md`. Nothing else was redesigned.

## Mode
BUILD (fix). No NT8 on this Mac, so nothing was compiled. Behaviour claims are INFERRED or CANNOT-DETERMINE-STATICALLY. Data counts are OBSERVED (output pasted below).

## Criterion
Brief criteria for 7zq M2: S1 and S2 (claims match the artefact), S6, S8 and F3 (limitation sentence verbatim), plus the worker-4 findings.

## Findings addressed

| Finding | Fix | Where (line) |
|---|---|---|
| MAJOR 1: C says there is no fallback and no trade without a 15:30 bar | C now says the signal is taken on the first bar in [15:30, 15:59), that every weekday session with a window bar has a 15:30 bar (worker 4, OBSERVED), and that the fallback is still Amear's question. The rule text and MANIFEST row are rewritten to match. | C:39 (rule), C:62 (MANIFEST row), C:117-120 (Q4) |
| MAJOR 2 + MINOR 6: P(c,t−1) was `Close[1]`, which picks up 13:00 holiday prices and depends on the template's end time | `CloseMod = 16*60`. Every bar with `mod == CloseMod` sets `lastRegularClose`/`lastRegularCloseDate`. The signal uses `lastRegularClose`, and `<= 0` means no trade. The `Close[1]` capture is removed. A diagnostic Print fires if the close is more than 4 days old. D3 is rewritten with the 37/9/1 counts, the p. 381 reasoning and DECISION_LOG:365, marked NEEDS AMEAR, with the skip alternative. | A:128, A:178-181, A:224, A:227-229, A:231; D3 A:83-92 |
| MINOR 3: B's trade count ~30 too high | ≤ 1,304 (1,305 sessions with a 15:30 bar, minus the first). Costs recomputed: $3,859.84, $26,080, 52.16. | B:35-36, B:41-42 |
| MINOR 4: weekend stray bars inside the window | A skips the signal on Saturday/Sunday bars (D7 cites both counts: 19 from the manager, 18 from worker 4). B adds a weekend defect check. | A:219-221, D7 A:100-102; B:58 |
| MINOR 5: C claims a governing 16:00 ET flat time | Replaced with "sets no governing flat-time rule and neither resolves nor changes F2…; flattens on the 15:59 bar as a realisation of Deviation B's 16:00 flatten" | C:87-89 |
| MINOR 6 (B side) | B adds a read-back of the last and first regular-session bar stamps (expect 16:00 and 09:31; if 17:00, report it per DECISION_LOG:365) | B:57 |
| MINOR 7: double exit on the stale-flat bar | `return;` added straight after each `LHStaleFlat` exit, still inside `Bars.IsFirstBarOfSession`. D4 notes the remaining 16:00-bar/backstop collision as CANNOT-DETERMINE-STATICALLY. | A:195, A:201; D4 A:93-97 |
| Pin 5: rule→line map | Rewritten with the new line numbers and checked against the grep below | A:104-118 |

These are unchanged: the class and Name, the four signal names, SignalMod and FlatMod, D1, r==0 → short, Contracts as the only input, the F3 sentence, no BOM, LF line endings, and no new type.

## Process log
1. Read the worker-4 findings, A, B and C in full.
2. Hashed the staged pre-edit A: `18d70c4822bbccb2cc3a4caad028066a52d79970320f12aa811c77bce2a651ef`.
3. Rewrote A with the Write tool. Took the code lines from `grep -n` and filled the map from them.
4. Ran the manager's `m2-sessions.py` (output below). Ran an extra read-only check on weekend 16:00 bars (below).
5. Checked the B example dates in the import file (MLK 2024).
6. Edited B and C. Grepped both for leftover claims.
7. Ran the verification suite. Staged A, B and C, then this report, by explicit path.

## Verification evidence

Key grep on A:
```
$ grep -n "CloseMod\|lastRegularClose\|DayOfWeek\|LHStaleFlat\|return;" ninjascript/PraxisLastHalfHourMomentum.cs
43://   (= 17:00 ET), unadjudicated; SignalMod/FlatMod/CloseMod are clock-based and hold either way.
47://   * Fixed constants (not Inputs): SignalMod = 15*60+30 (930), FlatMod = 16*60-1 (959), CloseMod = 16*60 (960).
48://   * Previous close P(c,t-1): on EVERY bar stamped 16:00 (mod == CloseMod), lastRegularClose = Close[0]
49://     and lastRegularCloseDate = Time[0].Date. At the signal bar the value used is therefore the most
51://     seen yet (first session of the data) -> lastRegularClose = 0 -> no trade.
53://     on a weekday only, if flat and lastRegularClose > 0: r = Close[0]/lastRegularClose - 1;
56://     First bar of a session while not flat (should never happen) -> exit "LHStaleFlat" + Print warning,
75://   the paper dropping those days. Such a session also has no 16:00 bar, so it never sets lastRegularClose.
96://       "LHStaleFlat" exit (followed by return) and the session-close backstop are the safety nets.
107://   Regular close stamp 16:00 (D3) ..................... CloseMod const         L128
108://   P(c,t-1) = most recent 16:00 close (Eq. 2, D3) ..... mod == CloseMod test   L178, capture L180
110://   Stale position on a new session (safety net) ....... LHStaleFlat + return   L194-195, L200-201
114://   No prior 16:00 close -> no trade ................... lastRegularClose <= 0  L224
128:		private const int CloseMod  = 16 * 60;        // 960 — the 16:00 bar; its Close is the regular close P(c) (D3)
132:		private double   lastRegularClose;       // P(c,t-1): Close of the most recent 16:00-stamped bar; 0 = none yet
133:		private DateTime lastRegularCloseDate;   // date of that bar (diagnostic only)
165:						+ BarsPeriod.BarsPeriodType + ". SignalMod/FlatMod/CloseMod assume end-stamped 1-min bars.");
167:				lastRegularClose     = 0.0;
168:				lastRegularCloseDate = DateTime.MinValue;
178:			if (mod == CloseMod)
180:				lastRegularClose     = Close[0];
181:				lastRegularCloseDate = Time[0].Date;
193:					Print(Name + " WARNING: still LONG on first bar of session " + Time[0] + "; exiting LHStaleFlat.");
194:					ExitLong("LHStaleFlat", "LHMomLong");
195:					return;
199:					Print(Name + " WARNING: still SHORT on first bar of session " + Time[0] + "; exiting LHStaleFlat.");
200:					ExitShort("LHStaleFlat", "LHMomShort");
201:					return;
212:				return;                          // never open a position at/after 15:59
218:				return;
219:			System.DayOfWeek dow = Time[0].DayOfWeek;   // D7: weekend stray bars never signal
220:			if (dow == System.DayOfWeek.Saturday || dow == System.DayOfWeek.Sunday)
221:				return;
224:			if (Position.MarketPosition != MarketPosition.Flat || lastRegularClose <= 0)
225:				return;
227:			if ((Time[0].Date - lastRegularCloseDate).TotalDays > 4)   // diagnostic only (D3); no behaviour change
228:				Print(Name + " WARNING: prior 16:00 close is from " + lastRegularCloseDate.ToString("yyyy-MM-dd")
231:			double r = Close[0] / lastRegularClose - 1.0;   // r_ROD = P(15:30)/P(last 16:00 close) - 1 (Eq. 2, p. 381)
```
Map lines that the grep pattern does not cover, checked with a second grep this session: SignalMod L126, FlatMod L127, `signalDoneToday = false` L187, LHFlat1559 L209/L211, `bool inSignalWindow` L216, EnterLong L233, EnterShort L235. All 14 map entries match.

```
$ grep -n "Close\[1\]" ninjascript/PraxisLastHalfHourMomentum.cs
rc=1                      (no match anywhere: not in code, not in comments)
$ grep -c prevSessionClose ...           -> 0
braces  { 13   } 13
parens whole file ( 138  ) 140; code-only (comments stripped) ( 38  ) 38 — the 2 extra ')' are half-open interval
  notation in comments: "[15:30,15:59)" at A:81 and "[SignalMod, FlatMod)" at A:215
$ file ninjascript/PraxisLastHalfHourMomentum.cs
ninjascript/PraxisLastHalfHourMomentum.cs: Unicode text, UTF-8 text
$ head -c 3 ... | xxd
00000000: 2372 65                                  #re          (no BOM)
CR: 0
$ shasum -a 256 ninjascript/PraxisLastHalfHourMomentum.cs
bacd30d0c0d5e5072e89a1a2b62a038a39e5908d66ddc84884d34760f9bcbcfa  ninjascript/PraxisLastHalfHourMomentum.cs
$ wc -l
     245 ninjascript/PraxisLastHalfHourMomentum.cs
non-ASCII outside // comments: only A:238 "#region Properties (sizing only — ...)" (region label; the original had the same line)
```
Types:
```
$ grep -n "enum \|class \|struct " ninjascript/*.cs
ninjascript/PraxisLastHalfHourMomentum.cs:122:	public class PraxisLastHalfHourMomentum : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout.cs:53:	public class PraxisNoiseAreaBreakout : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:65:		private sealed class DayRecord
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:47://   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:78:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:85:	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:98:		private sealed class DayRecord
ninjascript/PraxisSignalConsumer.cs:44:	public class PraxisSignalConsumer : Strategy
ninjascript/PraxisSignalConsumer.cs:487:		private sealed class ParsedSignal
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:39://   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:70:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:76:	public class PraxisNoiseAreaBreakout_OppBand : Strategy
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:88:		private sealed class DayRecord
```
A declares only one type. `System.DayOfWeek` is fully qualified to avoid any name clash with a NinjaScript member (INFERRED; not compiled).

The F3 sentence:
```
$ grep -c -F 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' A  -> 1
$ grep -c -F '...same...' B  -> 1
```
Claims removed from C:
```
$ grep -n "nearest bar\|stays 16:00\|no trade without" docs/reports/2026-10-31-7zq-m2-decisions-addendum.md
rc=1   (none)
$ grep -n "1,334\|3,949\|26,680\|previous session's last" docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
rc=1   (none)
wc -l: B 61, C 130
```
The manager's session script:
```
$ python3 -I .../scratchpad/m2-sessions.py ~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt
weekday sessions in range: 1352  with 15:30 bar: 1305  with 16:00 bar: 1305
weekend bars in 15:30-15:58 window (all data): 19
last-bar stamp counts (non-16:00): [(1300, 37), (1315, 9), (1403, 1)]
13:00-last sessions: ['20210531', '20210705', '20210906', '20211125', '20220117', '20220221'] ...
exit=0
```
The B MLK example comes from the import file:
```
20240112 160000;19464.75;19468.25;19452.75;19461;8034      (Fri)
20240115 130000;19457;19459;19457;19458.75;84               (Mon, MLK, 13:00 last bar)
20240116 153000;19418.25;19419.25;19414.25;19417.25;958
```
An extra check, outside the brief, on weekend bars stamped 16:00 (these feed the capture):
```
weekend bars stamped 16:00 (all data): 1 ['20211031']
```

## Open items (reported, not fixed: outside the pinned fix)
- The 16:00 capture has no weekday guard, as the brief pinned it. The data has one Sunday bar stamped 16:00 (2021-10-31, OBSERVED). If the RTH template keeps that bar, Monday 2021-11-01's P(c,t−1) would be that stray bar's price, not Friday 2021-10-29's 16:00 close. Whether the template keeps it is CANNOT-DETERMINE-STATICALLY. A guard is a one-line change, and it is the manager's or Amear's call.
- D3 (the 16:00 close versus skipping the day after a non-regular session) and D1 (fallback versus exact 15:30) stay NEEDS AMEAR. The breaker #5 overlap (C Q10) stays unanswered.
- D4's 16:00-bar double exit (LHFlat1559 plus the session-close backstop when the 15:59 bar is missing) is documented, not changed. There are 0 weekday cases in the import file (worker 4).
- C's MANIFEST row for this report still reads "ROW ONLY IF THE FILE IS CREATED". The file now exists. The row was left as written.

## Files staged
`ninjascript/PraxisLastHalfHourMomentum.cs`, `docs/reports/2026-10-31-7zq-m2-handtest-checklist.md`, `docs/reports/2026-10-31-7zq-m2-decisions-addendum.md`, `docs/reports/2026-10-31-7zq-m2-worker5-fix.md`. Nothing was committed.

## Result
PASS. All seven findings were addressed as pinned. Compile and runtime behaviour are not verified: no NT8 on the Mac.
