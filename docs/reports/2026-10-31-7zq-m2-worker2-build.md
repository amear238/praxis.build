# 7zq M2 worker 2: BUILD of `PraxisLastHalfHourMomentum.cs`

## Task
Unit Praxis_build-7zq, phase M2, worker 2. Mode: **BUILD**. Write one new NinjaScript backtest strategy, `ninjascript/PraxisLastHalfHourMomentum.cs`. It implements Baltussen, Da, Lammers & Martens (2021), JFE 142, 377–403, timing strategy η(r_ROD), as candidate #1 of `docs/reports/2026-10-31-7zq-m2-shortlist.md`, following the manager's pinned design.

No NT8 toolchain on this Mac, so the file is **WRITTEN, NOT COMPILED, NOT TESTED**. Every runtime-behaviour statement below is INFERRED or CANNOT-DETERMINE-STATICALLY.

## Design as built
- `public class PraxisLastHalfHourMomentum : Strategy`, `Name = "PraxisLastHalfHourMomentum"`, namespace `NinjaTrader.NinjaScript.Strategies`. No other type is declared, and there is no nested type.
- The usings block is copied verbatim from `PraxisNoiseAreaBreakout.cs`.
- SetDefaults matches the base: `Calculate.OnBarClose`, `EntriesPerDirection = 1`, `EntryHandling.AllEntries`, `IsExitOnSessionCloseStrategy = true` (backstop), `ExitOnSessionCloseSeconds = 30` (the base value), `StartBehavior.WaitUntilFlat`, `TimeInForce.Day`, `BarsRequiredToTrade = 20`. `BarsRequiredToTrade` is kept from the base. It does not matter here because the first session cannot trade anyway: it has no prior close.
- Inputs: only `Contracts` (int, default 1, `[Range(1, int.MaxValue)]`). Constants: `SignalMod = 15 * 60 + 30` (930) and `FlatMod = 16 * 60 - 1` (959).
- State: `prevSessionClose` (0 means unknown) and `signalDoneToday`. Both are also reset in `State.DataLoaded`. `DataLoaded` also prints the base's warning when the series is not 1-minute.
- `OnBarUpdate` order:
  1. `mod = Time[0].Hour*60 + Time[0].Minute`.
  2. On `Bars.IsFirstBarOfSession`: reset `signalDoneToday`; set `prevSessionClose = CurrentBar > 0 ? Close[1] : 0`; if not flat, Print a warning and exit with `"LHStaleFlat"`.
  3. If `mod >= FlatMod`: send the `ExitLong/ExitShort("LHFlat1559", ...)` exit for the side held, then `return`.
  4. Signal window `SignalMod <= mod && mod < FlatMod`, evaluated once per session. Set `signalDoneToday = true` whether or not a trade is taken. Require flat and `prevSessionClose > 0`. Then `r = Close[0]/prevSessionClose - 1`: if `r > 0`, `EnterLong(Contracts, "LHMomLong")`; otherwise `EnterShort(Contracts, "LHMomShort")`.
- The header carries: the source citation with page cites, copied from the shortlist; the pinned design; the RTH 09:30–16:00 ET and platform-TZ = ET assumptions; end-stamped bars; fill consequences (INFERRED); the look-ahead note; early-close handling (CANNOT-DETERMINE-STATICALLY for the template); deviations D1–D6; the rule→line map; `WRITTEN, NOT COMPILED, NOT TESTED`; and the verbatim sentence `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.` A note after that sentence says fill resolution and slippage are Analyzer run settings, not set in code.

## Rule→line map
These line numbers were checked with `grep -n` (output below) and match the header map at lines 88–98.

| Rule (paper cite) | Code | Line |
|---|---|---|
| Signal time 15:30, c−30 (Eq. 2, p. 381) | `const int SignalMod` | 106 |
| Flat at 15:59 (pinned; LH holding, p. 385) | `const int FlatMod` | 107 |
| P(c,t−1) = prior session's last close (Eq. 2) | `prevSessionClose = (CurrentBar > 0) ? Close[1] : 0.0` | 161 |
| First session: no prior close → no trade | same line, `CurrentBar > 0` guard; `prevSessionClose <= 0` check | 161, 192 |
| Once-per-session flag reset | `signalDoneToday = false` | 157 |
| Stale position safety net | `ExitLong/ExitShort("LHStaleFlat", ...)` | 167, 172 |
| Flat at 15:59 | `ExitLong/ExitShort("LHFlat1559", ...)` | 180, 182 |
| Signal window | `inSignalWindow = SignalMod <= mod && mod < FlatMod` | 187 |
| r_ROD (Eq. 2, p. 381) | `double r = Close[0] / prevSessionClose - 1.0` | 195 |
| r > 0 → long (Eq. 12, p. 385) | `if (r > 0) EnterLong(Contracts, "LHMomLong")` | 196–197 |
| otherwise (incl. r == 0) → short (Eq. 12) | `else EnterShort(Contracts, "LHMomShort")` | 198–199 |

## Verification evidence (pasted)
```
== ninjascript/PraxisLastHalfHourMomentum.cs
ninjascript/PraxisLastHalfHourMomentum.cs: Unicode text, UTF-8 text
00000000: 2372 65                                  #re
CR count: 0
== ninjascript/PraxisNoiseAreaBreakout.cs
ninjascript/PraxisNoiseAreaBreakout.cs: Unicode text, UTF-8 text
00000000: 2372 65                                  #re
CR count: 0
== sha/wc
18d70c4822bbccb2cc3a4caad028066a52d79970320f12aa811c77bce2a651ef  ninjascript/PraxisLastHalfHourMomentum.cs
     209 ninjascript/PraxisLastHalfHourMomentum.cs
== type inventory
ninjascript/PraxisLastHalfHourMomentum.cs:102:	public class PraxisLastHalfHourMomentum : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout.cs:53:	public class PraxisNoiseAreaBreakout : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:65:		private sealed class DayRecord
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:47://   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:78:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:85:	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:98:		private sealed class DayRecord
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:39://   Custom\Strategies folder. Re-declaring the enum here would be CS0101 (INFERRED, not compiled).
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:70:	// enum PraxisNoiseExitMode { OppBand, BandOrVWAP } is declared ONCE, in PraxisNoiseAreaBreakout.cs.
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:76:	public class PraxisNoiseAreaBreakout_OppBand : Strategy
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:88:		private sealed class DayRecord
ninjascript/PraxisSignalConsumer.cs:44:	public class PraxisSignalConsumer : Strategy
ninjascript/PraxisSignalConsumer.cs:487:		private sealed class ParsedSignal
== order/const grep
45://   * Fixed constants (not Inputs): SignalMod = 15*60+30 (930), FlatMod = 16*60-1 (959).
46://   * Previous close P(c,t-1): on Bars.IsFirstBarOfSession (CurrentBar > 0), prevSessionClose = Close[1],
49://   * Signal: once per session, on the FIRST bar with SignalMod <= mod < FlatMod (normally the 15:30 bar),
50://     if flat and prevSessionClose > 0: r = Close[0]/prevSessionClose - 1; r > 0 -> EnterLong,
51://     else -> EnterShort. signalDoneToday is reset on the first bar of each session.
52://   * Exit: any bar with mod >= FlatMod while not flat -> ExitLong/ExitShort("LHFlat1559").
62://     next session (INFERRED). That is why FlatMod is 15:59 and not 16:00.
88://   Fixed signal time 15:30 (Eq. 2, p. 381) ............ SignalMod const       L106
89://   Fixed flat time 15:59 (pinned; holding p. 385) ..... FlatMod const         L107
90://   P(c,t-1) = prior session's last close (Eq. 2) ...... prevSessionClose =    L161
95://   Signal window SignalMod <= mod < FlatMod .......... window test           L187
97://   r > 0 -> long (Eq. 12, p. 385) ..................... EnterLong             L196-197
98://   otherwise (incl. r == 0) -> short (Eq. 12) ......... EnterShort            L198-199
106:		private const int SignalMod = 15 * 60 + 30;   // 930 — the 15:30 bar (c - 30, Eq. 2 p. 381)
107:		private const int FlatMod   = 16 * 60 - 1;    // 959 — the 15:59 bar; exit fills at the 16:00 bar Open (INFERRED)
111:		private double prevSessionClose;   // P(c,t-1): Close of the prior session's last bar; 0 = unknown
143:						+ BarsPeriod.BarsPeriodType + ". SignalMod/FlatMod assume end-stamped 1-min bars.");
145:				prevSessionClose = 0.0;
161:				prevSessionClose = (CurrentBar > 0) ? Close[1] : 0.0;
167:					ExitLong("LHStaleFlat", "LHMomLong");
172:					ExitShort("LHStaleFlat", "LHMomShort");
177:			if (mod >= FlatMod)
180:					ExitLong("LHFlat1559", "LHMomLong");
182:					ExitShort("LHFlat1559", "LHMomShort");
186:			// ---- Signal: first bar of the session inside [SignalMod, FlatMod), normally the 15:30 bar. ----
187:			bool inSignalWindow = SignalMod <= mod && mod < FlatMod;
192:			if (Position.MarketPosition != MarketPosition.Flat || prevSessionClose <= 0)
195:			double r = Close[0] / prevSessionClose - 1.0;   // r_ROD = P(15:30)/P(prev close) - 1 (Eq. 2, p. 381)
197:				EnterLong(Contracts, "LHMomLong");          // predictor > 0 -> long (Eq. 12, p. 385)
199:				EnterShort(Contracts, "LHMomShort");        // "otherwise" (incl. r == 0) -> short (Eq. 12, p. 385)
== braces
{       12
}       12
(      109
)      110
== tail byte
00000000: 7d0a                                     }.
```
Paren imbalance traced line by line. Strings and `//` comments were stripped before counting code parens:
```
RAW 71: 1/0: //   those days. How the RTH session template builds those days (last bar stamp, whether the session is
RAW 72: 0/1: //   shortened at all) is CANNOT-DETERMINE-STATICALLY.
CODE 142: 1/0
RAW 142: 1/0: 					Print(Name + " WARNING: expected a 1-MINUTE series; got " + BarsPeriod.Value + " "
CODE 143: 0/1
RAW 143: 0/1: 						+ BarsPeriod.BarsPeriodType + ". SignalMod/FlatMod assume end-stamped 1-min bars.");
RAW 186: 0/1: 			// ---- Signal: first bar of the session inside [SignalMod, FlatMod), normally the 15:30 bar. ----
```
The only net mismatch is the half-open interval `[SignalMod, FlatMod)` in the line-186 comment. Code parens balance; 142/143 is one Print call split over two lines. Braces balance at 12/12.

The type inventory shows only `PraxisLastHalfHourMomentum` for the new file. The file starts `#re` with no BOM, has 0 CRs (LF line endings), and ends with `}\n`. All of this matches the base.

Staging:
```
A  ninjascript/PraxisLastHalfHourMomentum.cs
A  ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs
A  ninjascript/PraxisNoiseAreaBreakout_OppBand.cs
```
The two `PraxisNoiseAreaBreakout_*` rows were already staged before this session; they show as `A ` in the session-start git status. This worker did not touch them.

## Deviations
These are stated in the header as D1–D6.
- **D1.** If the 15:30 bar is missing, the next bar before 15:59 is used, so the signal and entry come later.
- **D2.** The minute 15:59→16:00 is not earned: the exit fills at the 16:00 bar's Open (INFERRED).
- **D3.** On the day after an early close, P(c,t−1) is the prior session's last bar. The paper is SPEC-SILENT on this. **NEEDS AMEAR.**
- **D4.** If the 15:59 bar is missing, the 16:00 bar triggers the exit, which may fill next session (INFERRED). The safety nets are `LHStaleFlat` and the session-close backstop. How those two interact is CANNOT-DETERMINE-STATICALLY.
- **D5.** Not ported: the 1/N portfolio, the roll rule and the low-volume filter. This is NQ alone.
- **D6.** The paper is gross of costs; this backtest charges whatever costs the Analyzer run sets.
- The build adds nothing beyond the pinned design. Two choices were mine: `BarsRequiredToTrade = 20`, kept from the base; and `signalDoneToday = true` is set even when no trade is taken (not flat, or no prior close), so that a later bar cannot trigger.

## Files staged
- `ninjascript/PraxisLastHalfHourMomentum.cs` (new; sha256 `18d70c48…a651ef`; 209 lines)
- `docs/reports/2026-10-31-7zq-m2-worker2-build.md` (this report)

## Result: PASS
PASS means the static checks pass. It is not a compile result. Compile and behaviour in NT8 are UNVERIFIED.
