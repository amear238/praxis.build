#region Using declarations
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Globalization;
using System.Linq;
using System.Xml.Serialization;
using System.Windows.Media;
using NinjaTrader.Cbi;
using NinjaTrader.Data;
using NinjaTrader.Gui;
using NinjaTrader.Gui.Chart;
using NinjaTrader.NinjaScript;
using NinjaTrader.Core.FloatingPoint;
#endregion

// PRAXIS 7zq M2 (bead Praxis_build-7zq) — LAST-HALF-HOUR MARKET INTRADAY MOMENTUM backtest Strategy.
// WRITTEN, NOT COMPILED, NOT TESTED. No NT8 toolchain on the Mac; every behaviour note below is
// INFERRED or CANNOT-DETERMINE-STATICALLY unless marked OBSERVED (paper text or import-file scan).
// TEST MATERIAL, NOT A RULING. Revised by M2 worker 5 after the worker-4 adversarial review.
//
// SOURCE: Baltussen, G., Da, Z., Lammers, S., Martens, M. (2021), "Hedging demand and market intraday
//   momentum", Journal of Financial Economics 142, 377-403. DOI 10.1016/j.jfineco.2021.04.029.
//   Strategy replicated: the timing strategy eta(r_ROD). Shortlist: docs/reports/2026-10-31-7zq-m2-shortlist.md
//   (candidate #1). Page cites are journal pages (= PDF page + 376) except where a PDF page is given.
//   * Hours: NQ trades on the cash hours 09:30-16:00 (Table 1, p. 383; Table A1, PDF p. 19).
//   * Signal: r_ROD,t = P(c-30,t) / P(c,t-1) - 1, previous day's close to 30 minutes before today's
//     close (Eq. 2, p. 381). For NQ, c = 16:00, so the signal price is the 15:30 price.
//   * Position: long if the predictor is > 0, "otherwise" short; earns the last half-hour return
//     (Eq. 12, p. 385). r_ROD == 0 therefore goes SHORT (Eq. 12 "otherwise").
//   * Holding: the last half hour, 15:30 -> 16:00 close. Flat at the close; at most one trade a day.
//   * Data hygiene: the paper removes non-business days and early-close days from the sample (p. 381).
//   * Costs: the paper does not consider transaction costs (p. 386).
//   * Reported result: equity-futures 1/N portfolio eta(r_ROD) Sharpe 1.73 (Table 6, p. 387). No NQ-alone P&L.
//   * Tunable strategy parameters in the paper: NONE. This file exposes ONLY Contracts (sizing).
//
// INSTRUMENT / SESSION ASSUMPTIONS: NQ futures, 1-MINUTE series, RTH session template 09:30-16:00 ET,
//   and the platform time zone = ET (Time[0] is read as ET wall-clock). If either is wrong, every
//   minute-of-day constant below is wrong. Bars are END-STAMPED: the first RTH bar is stamped 09:31 and
//   the 16:00-stamped bar is the regular session's last. The 15:30-stamped bar covers 15:29-15:30, so its
//   Close is the 15:30 price. DECISION_LOG:365 records the template printing 8:30 AM-4:00 PM Central
//   (= 17:00 ET), unadjudicated; SignalMod/FlatMod/CloseMod are clock-based and hold either way.
//
// PINNED DESIGN (fixed by the manager, implemented exactly):
//   * Calculate.OnBarClose, managed orders, market orders only, EntriesPerDirection = 1.
//   * Fixed constants (not Inputs): SignalMod = 15*60+30 (930), FlatMod = 16*60-1 (959), CloseMod = 16*60 (960).
//   * Previous close P(c,t-1): on every WEEKDAY bar stamped 16:00 (mod == CloseMod), lastRegularClose = Close[0]
//     and lastRegularCloseDate = Time[0].Date. At the signal bar the value used is therefore the most
//     recent 16:00-stamped close of a PRIOR session (today's 16:00 bar comes after 15:30). No 16:00 bar
//     seen yet (first session of the data) -> lastRegularClose = 0 -> no trade.
//   * Signal: once per session, on the FIRST bar with SignalMod <= mod < FlatMod (normally the 15:30 bar),
//     on a weekday only, if flat and lastRegularClose > 0: r = Close[0]/lastRegularClose - 1;
//     r > 0 -> EnterLong, else -> EnterShort. signalDoneToday is reset on the first bar of each session.
//   * Exit: any bar with mod >= FlatMod while not flat -> ExitLong/ExitShort("LHFlat1559").
//     First bar of a session while not flat (should never happen) -> exit "LHStaleFlat" + Print warning,
//     then return at once so no second exit or entry is submitted on that bar.
//   * IsExitOnSessionCloseStrategy = true is a BACKSTOP only (ExitOnSessionCloseSeconds = 30, as the base).
//
// FILL CONSEQUENCES (INFERRED, not observed in NT8):
//   * Entry is decided on the 15:30 bar's close and fills at the 15:31-stamped bar's Open, about the
//     15:30 price (the paper's entry price). The fill is one bar after the decision.
//   * Exit is decided on the 15:59 bar's close and fills at the 16:00-stamped bar's Open, about the 15:59
//     price. So the final minute 15:59 -> 16:00 of the paper's window is NOT earned.
//   * M1 (PraxisNoiseAreaBreakout_Flat1559.cs) found that an exit decided ON the 16:00 bar fills in the
//     next session (INFERRED). That is why FlatMod is 15:59 and not 16:00.
//   Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
//   (Fill resolution and slippage are Strategy Analyzer run settings; this file does not set them.)
//
// LOOK-AHEAD NOTE: the decision reads Close[0] of the 15:30 bar under OnBarClose, i.e. only a completed
//   bar, and a 16:00 close captured on an EARLIER bar. No future bar is read; the order fills one bar
//   later (15:31 Open).
//
// EARLY-CLOSE / HOLIDAY SESSIONS: no bar reaches 15:30, so no signal and no trade that day, which matches
//   the paper dropping those days. Such a session also has no 16:00 bar, so it never sets lastRegularClose.
//   How the RTH template builds those days is CANNOT-DETERMINE-STATICALLY.
//
// KNOWN DEVIATIONS from the paper:
//   D1. Missing 15:30 bar (no trades that minute): the next bar before 15:59 is used as the signal bar,
//       so the signal price and entry are later than 15:30. (Import file: every weekday session with a
//       bar in [15:30,15:59) has a 15:30 bar, OBSERVED by worker 4; D1 is a fallback, not a live path.)
//   D2. The last minute 15:59 -> 16:00 is not earned (exit fills at the 16:00 bar's Open, INFERRED).
//   D3. P(c,t-1) = the most recent 16:00-stamped close of a prior session, NOT the prior session's last
//       bar. Why: the import data has 37 weekday sessions ending 13:00 (CME halts on NYSE holidays),
//       9 ending 13:15 (early closes) and 1 ending 14:03 (data gap), OBSERVED by the manager
//       ("last-bar stamp counts (non-16:00): [(1300, 37), (1315, 9), (1403, 1)]"). The paper drops
//       non-business and early-close days (p. 381), so its "previous day's close" is the prior regular
//       day's 16:00 close (INFERRED). A 16:00-stamped close is also robust to whether the template ends
//       at 16:00 or 17:00 ET (DECISION_LOG:365); the prior session's last bar is not (INFERRED).
//       Diagnostic only: a Print warning if that close is more than 4 calendar days old at the signal
//       bar. No staleness rule is in the paper, so the warning changes nothing.
//       NEEDS AMEAR: keep this, or skip the day after any non-regular session?
//   D4. Missing 15:59 bar: the 16:00 bar triggers the exit, which may fill in the next session (INFERRED);
//       on that 16:00 bar the session-close backstop may also fire (double exit, CANNOT-DETERMINE-
//       STATICALLY; 0 weekday cases in the import file, OBSERVED by worker 4). The first-bar
//       "LHStaleFlat" exit (followed by return) and the session-close backstop are the safety nets.
//   D5. The paper's 1/N multi-future portfolio, roll rule and low-volume-day filter (p. 381) are not ported;
//       this is NQ alone, 1 fixed contract size, on whatever continuous series the Analyzer supplies.
//   D6. Costs: the paper is gross of costs (p. 386); this backtest charges whatever the Analyzer run sets.
//   D7. SAFETY: no signal on a Saturday/Sunday bar. The import data has weekend stray bars inside
//       15:30-15:58 (manager OBSERVED 19 in all data; worker 4 counted 18 in 2021-03-08 -> 2026-07-17).
//       Whether the RTH template keeps them is CANNOT-DETERMINE-STATICALLY; the paper has no weekend days.
//
// RULE -> CODE-LINE MAP (line numbers in THIS file; verified with grep -n after writing):
//   Fixed signal time 15:30 (Eq. 2, p. 381) ............ SignalMod const        L126
//   Fixed flat time 15:59 (pinned; holding p. 385) ..... FlatMod const          L127
//   Regular close stamp 16:00 (D3) ..................... CloseMod const         L128
//   P(c,t-1) = most recent 16:00 close (Eq. 2, D3) ..... mod == CloseMod test   L178, capture L180
//   Daily reset of the once-per-session flag ........... signalDoneToday reset  L187
//   Stale position on a new session (safety net) ....... LHStaleFlat + return   L194-195, L200-201
//   Flat at 15:59 (holding = last half hour) ........... LHFlat1559 exits       L209, L211
//   Signal window SignalMod <= mod < FlatMod .......... window test            L216
//   No signal on Saturday/Sunday (D7) .................. weekend test           L219-221
//   No prior 16:00 close -> no trade ................... lastRegularClose <= 0  L224
//   Stale prior close > 4 days (diagnostic only, D3) ... Print warning          L227
//   r_ROD = P(15:30)/P(prev close) - 1 (Eq. 2) ......... r computation          L231
//   r > 0 -> long (Eq. 12, p. 385) ..................... EnterLong              L233
//   otherwise (incl. r == 0) -> short (Eq. 12) ......... EnterShort             L235

namespace NinjaTrader.NinjaScript.Strategies
{
	public class PraxisLastHalfHourMomentum : Strategy
	{
		#region Fixed session clock (paper-fixed; not exposed)
		// Minute-of-day (ET) of the END-STAMPED bar, Time[0].Hour * 60 + Time[0].Minute.
		private const int SignalMod = 15 * 60 + 30;   // 930 — the 15:30 bar (c - 30, Eq. 2 p. 381)
		private const int FlatMod   = 16 * 60 - 1;    // 959 — the 15:59 bar; exit fills at the 16:00 bar Open (INFERRED)
		private const int CloseMod  = 16 * 60;        // 960 — the 16:00 bar; its Close is the regular close P(c) (D3)
		#endregion

		#region Per-session state
		private double   lastRegularClose;       // P(c,t-1): Close of the most recent 16:00-stamped bar; 0 = none yet
		private DateTime lastRegularCloseDate;   // date of that bar (diagnostic only)
		private bool     signalDoneToday;        // the signal is evaluated at most once per session
		#endregion

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description  = "PRAXIS 7zq M2 Last-half-hour market intraday momentum (Baltussen, Da, Lammers, Martens 2021, JFE 142, eta(r_ROD)). At 15:30 ET: long if (last 16:00 close)->15:30 return > 0, otherwise short; flat on the 15:59 bar. No tunable parameters. WRITTEN, NOT COMPILED, NOT TESTED.";
				Name         = "PraxisLastHalfHourMomentum";

				// OnBarClose: the decision reads only the completed 15:30 bar (look-ahead note in header).
				Calculate                                 = Calculate.OnBarClose;
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy              = true;   // BACKSTOP only; the explicit 15:59 flat is primary
				ExitOnSessionCloseSeconds                 = 30;     // same value as PraxisNoiseAreaBreakout.cs
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
				BarsRequiredToTrade                       = 20;
				IsInstantiatedOnEachOptimizationIteration = false;

				Contracts = 1;   // position sizing only (NOT a rule knob); the paper is unit exposure (Eq. 12)
			}
			else if (State == State.Configure)
			{
				// (No secondary data series required — single 1-min primary series.)
			}
			else if (State == State.DataLoaded)
			{
				if (BarsPeriod.BarsPeriodType != BarsPeriodType.Minute || BarsPeriod.Value != 1)
					Print(Name + " WARNING: expected a 1-MINUTE series; got " + BarsPeriod.Value + " "
						+ BarsPeriod.BarsPeriodType + ". SignalMod/FlatMod/CloseMod assume end-stamped 1-min bars.");

				lastRegularClose     = 0.0;
				lastRegularCloseDate = DateTime.MinValue;
				signalDoneToday      = false;
			}
		}

		protected override void OnBarUpdate()
		{
			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed, end-stamped) bar

			// ---- Regular close capture (D3): every 16:00-stamped bar. Used only on a LATER session's signal bar. ----
			if (mod == CloseMod && Time[0].DayOfWeek != System.DayOfWeek.Saturday && Time[0].DayOfWeek != System.DayOfWeek.Sunday)
			{
				lastRegularClose     = Close[0];
				lastRegularCloseDate = Time[0].Date;
			}

			// ---- Session rollover: reset the daily flag, sweep any stale position. ----
			if (Bars.IsFirstBarOfSession)
			{
				signalDoneToday = false;

				// Should never happen (15:59 flat + session-close backstop). Exit at once, say so, and stop
				// processing this bar so no second exit or entry is submitted on it (worker-4 finding 7).
				if (Position.MarketPosition == MarketPosition.Long)
				{
					Print(Name + " WARNING: still LONG on first bar of session " + Time[0] + "; exiting LHStaleFlat.");
					ExitLong("LHStaleFlat", "LHMomLong");
					return;
				}
				else if (Position.MarketPosition == MarketPosition.Short)
				{
					Print(Name + " WARNING: still SHORT on first bar of session " + Time[0] + "; exiting LHStaleFlat.");
					ExitShort("LHStaleFlat", "LHMomShort");
					return;
				}
			}

			// ---- Flat on the 15:59 bar (or any later bar) — fills at the 16:00 bar Open (INFERRED). ----
			if (mod >= FlatMod)
			{
				if (Position.MarketPosition == MarketPosition.Long)
					ExitLong("LHFlat1559", "LHMomLong");
				else if (Position.MarketPosition == MarketPosition.Short)
					ExitShort("LHFlat1559", "LHMomShort");
				return;                          // never open a position at/after 15:59
			}

			// ---- Signal: first bar of the session inside [SignalMod, FlatMod), normally the 15:30 bar. ----
			bool inSignalWindow = SignalMod <= mod && mod < FlatMod;
			if (signalDoneToday || !inSignalWindow)
				return;
			System.DayOfWeek dow = Time[0].DayOfWeek;   // D7: weekend stray bars never signal
			if (dow == System.DayOfWeek.Saturday || dow == System.DayOfWeek.Sunday)
				return;
			signalDoneToday = true;              // once per session, traded or not

			if (Position.MarketPosition != MarketPosition.Flat || lastRegularClose <= 0)
				return;

			if ((Time[0].Date - lastRegularCloseDate).TotalDays > 4)   // diagnostic only (D3); no behaviour change
				Print(Name + " WARNING: prior 16:00 close is from " + lastRegularCloseDate.ToString("yyyy-MM-dd")
					+ ", more than 4 days before " + Time[0] + ".");

			double r = Close[0] / lastRegularClose - 1.0;   // r_ROD = P(15:30)/P(last 16:00 close) - 1 (Eq. 2, p. 381)
			if (r > 0)
				EnterLong(Contracts, "LHMomLong");          // predictor > 0 -> long (Eq. 12, p. 385)
			else
				EnterShort(Contracts, "LHMomShort");        // "otherwise" (incl. r == 0) -> short (Eq. 12, p. 385)
		}

		#region Properties (sizing only — the paper has zero tunable parameters)
		[NinjaScriptProperty]
		[Range(1, int.MaxValue)]
		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). The paper's Eq. 12 is unit exposure.", GroupName = "02. Praxis", Order = 1)]
		public int Contracts { get; set; }
		#endregion
	}
}
