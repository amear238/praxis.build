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

// ==============================================================================================
// PRAXIS walk-forward ARM (b) — Noise-Area Breakout with tunables. Decision D-2026-11-07-B.
// Branch: arm-b/wf-tunables. Design authority: docs/specs/2026-11-06-walk-forward-values.md
// §3 (grid), §4 (stop), §9 (code design, tests T1-T13).
// STATUS: WRITTEN — not compiled, not run. (No C# compiler / NT8 on the Mac.)
//
// A copy of PraxisNoiseAreaBreakout.cs (base) logic with:
//   * Lookback and NoiseMult as inputs (base consts), band = ref * (1 +/- NoiseMult * sigma).
//   * ExitPolicy { BandOrVWAP, OppBand, Flat1559 }, declared in THIS file:
//       BandOrVWAP = base exits (long: Close <= max(Upper, VWAP); short: Close >= min(Lower, VWAP));
//       OppBand    = opposite band, as _OppBand.cs (long: Close <= Lower; short: Close >= Upper);
//       Flat1559   = BandOrVWAP exits, session flat decided at mod >= 959, as _Flat1559.cs.
//   * StopAtrMult: bar-close stop at entry fill -/+ StopAtrMult * ATR(AtrPeriod), daily ATR from
//     completed RTH sessions; exit by market order (fills next bar). No stop order is ever placed.
//     StopAtrMult = 0 = no stop and no ATR entry gate (acceptance tests T1-T3 only).
//   * Precedence on every bar: (1) session flat, (2) stop, (3) checkpoint exits and entries.
// Add to a 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template, as the base.
// ==============================================================================================

namespace NinjaTrader.NinjaScript.Strategies
{
	// Exit policy (spec §3). Declared here so the base file and its enum stay unchanged (spec §9).
	public enum PraxisNoiseArmBExitPolicy
	{
		BandOrVWAP,
		OppBand,
		Flat1559
	}

	public class PraxisNoiseAreaBreakoutArmB : Strategy
	{
		#region Fixed session clock (not exposed)
		private const int OpenMod    = 9 * 60 + 30;   // 570 = 09:30 ET
		private const int CloseMod   = 16 * 60;       // 960 = 16:00 ET
		private const int FlattenMod = CloseMod - 1;  // 959 = 15:59 ET (Flat1559 only, as _Flat1559.cs)
		private const int OracleMod  = 10 * 60;       // 600 = 10:00 ET checkpoint for the T6(ii) oracle prints
		private const int AtrPeriod  = 14;            // ATR period, fixed, not tuned (spec §3/§4)
		#endregion

		#region Per-day history store (completed sessions only — no look-ahead)
		private sealed class DayRecord
		{
			public double Open;                                  // Open_{t,09:30}
			public double Close1600;                             // Close_{t,16:00} (kept as base; not used for prevClose)
			public double High;                                  // session high (ATR true range)
			public double Low;                                   // session low  (ATR true range)
			public double PrevClose;                             // prior session's last close, = prevClose at this session's first bar (ATR true range)
			public readonly Dictionary<int, double> Closes =     // minute-of-day -> Close at that minute
				new Dictionary<int, double>();
		}

		private readonly List<DayRecord> history = new List<DayRecord>();  // oldest..newest
		private int HistoryCap { get { return Lookback + 15; } }           // >= 17 at every allowed Lookback, so >= AtrPeriod kept

		// Current (in-progress) session accumulators — NOT visible to sigma or ATR until the session closes.
		private DayRecord today;
		private double     todayOpen;
		private double     prevClose;
		private bool       haveDay;

		// Session-anchored VWAP (RTH only, anchored at the 09:30 open), as base.
		private double vwapCumPV;
		private double vwapCumVol;

		private double curUpper, curLower, curVwap, curSigma;
		private bool   haveBand;

		// Daily ATR over the last AtrPeriod completed sessions (computed on each session's first bar).
		private double atrSum;      // sum of the last AtrPeriod true ranges (exact: prices are 0.25 multiples)
		private double curAtr;      // atrSum / AtrPeriod
		private bool   haveAtr;     // history holds AtrPeriod completed sessions (each with its own PrevClose)

		// Stop state, fixed at the entry fill (not trailing). A reversal's entry fill overwrites it.
		private MarketPosition stopSide = MarketPosition.Flat;
		private double stopFill;
		private double stopAtrSum;
		private double stopLevel;
		private bool   haveStopLevel;

		// T6(ii) oracle sessions: sigma / bands / ATR printed at their 10:00 checkpoint. Prints only.
		private static readonly DateTime[] OracleDates =
		{
			new DateTime(2021, 6, 15),
			new DateTime(2024, 12, 26),
			new DateTime(2026, 3, 18)
		};
		#endregion

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description  = "PRAXIS walk-forward arm (b) Noise-Area Breakout: base logic with tunable Lookback, noise multiplier, bar-close daily-ATR stop and exit policy (BandOrVWAP / OppBand / Flat1559). D-2026-11-07-B. WRITTEN, not compiled, not run.";
				Name         = "PraxisNoiseAreaBreakoutArmB";

				// As base: OnBarClose is required for the no-look-ahead guarantee.
				Calculate                                 = Calculate.OnBarClose;
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit session flat is primary
				ExitOnSessionCloseSeconds                 = 30;
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
				BarsRequiredToTrade                       = 20;
				IsInstantiatedOnEachOptimizationIteration = false;

				// Defaults = arm (a) values (spec §9 inputs table).
				Lookback    = 14;
				NoiseMult   = 1.0;
				StopAtrMult = 0.0;                                   // 0 = no stop: T1-T3 only; every grid value >= 1.5
				ExitPolicy  = PraxisNoiseArmBExitPolicy.BandOrVWAP;
				Contracts   = 1;

				AddPlot(Brushes.DodgerBlue, "UpperBound");
				AddPlot(Brushes.DodgerBlue, "LowerBound");
				AddPlot(Brushes.Goldenrod,  "SessionVWAP");
			}
			else if (State == State.Configure)
			{
				// (No secondary data series — ATR is built from the 1-min primary series.)
			}
			else if (State == State.DataLoaded)
			{
				if (BarsPeriod.BarsPeriodType != BarsPeriodType.Minute || BarsPeriod.Value != 1)
					Print(Name + " WARNING: expected a 1-MINUTE series; got " + BarsPeriod.Value + " "
						+ BarsPeriod.BarsPeriodType + ". Minute-of-day band construction assumes 1-min bars (spec §1).");

				// Reset every class-level state field. IsInstantiatedOnEachOptimizationIteration = false
				// reuses the instance across iterations (that DataLoaded runs per iteration is UNVERIFIED);
				// on a fresh instance this is an identity.
				history.Clear();
				today         = null;
				todayOpen     = 0.0;
				prevClose     = 0.0;
				haveDay       = false;
				vwapCumPV     = 0.0;
				vwapCumVol    = 0.0;
				curUpper      = 0.0;
				curLower      = 0.0;
				curVwap       = 0.0;
				curSigma      = 0.0;
				haveBand      = false;
				atrSum        = 0.0;
				curAtr        = 0.0;
				haveAtr       = false;
				stopSide      = MarketPosition.Flat;
				stopFill      = 0.0;
				stopAtrSum    = 0.0;
				stopLevel     = 0.0;
				haveStopLevel = false;

				// T5(i) readback: the five inputs, once.
				Print(string.Format(CultureInfo.InvariantCulture,
					"{0} INPUTS Lookback={1} NoiseMult={2:R} StopAtrMult={3:R} ExitPolicy={4} Contracts={5}",
					Name, Lookback, NoiseMult, StopAtrMult, ExitPolicy, Contracts));
			}
		}

		protected override void OnBarUpdate()
		{
			if (CurrentBar < 1)
				return;

			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar

			// ---- Session rollover (as base), plus the ATR update from completed sessions only. ----
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history
				ComputeAtr();                   // ATR from completed sessions only (no look-ahead)

				today     = new DayRecord();
				todayOpen = Open[0];
				today.Open = todayOpen;
				today.High = High[0];
				today.Low  = Low[0];
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;
				today.PrevClose = prevClose;

				vwapCumPV  = 0.0;
				vwapCumVol = 0.0;
				haveDay    = true;
			}

			if (!haveDay)
				return;

			// ---- Per-bar bookkeeping (as base) plus session high / low for ATR. ----
			today.Closes[mod] = Close[0];
			today.High      = Math.Max(today.High, High[0]);
			today.Low       = Math.Min(today.Low, Low[0]);
			if (mod == CloseMod)
				today.Close1600 = Close[0];

			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;
				vwapCumVol += vol;
			}

			BuildBand(mod);
			if (haveBand)
			{
				Values[0][0] = curUpper;
				Values[1][0] = curLower;
			}
			if (vwapCumVol > 0)
				Values[2][0] = curVwap;

			// ---- T6(ii) oracle print at 10:00 of the named sessions. Prints only; no order. ----
			if (mod == OracleMod && Array.IndexOf(OracleDates, Time[0].Date) >= 0)
				PrintOracle();

			// ---- (1) SESSION FLAT. 16:00 bar; under Flat1559 the 15:59 bar (as _Flat1559.cs). ----
			int flatMod = (ExitPolicy == PraxisNoiseArmBExitPolicy.Flat1559) ? FlattenMod : CloseMod;
			if (mod >= flatMod)
			{
				FlattenAll("session flat");
				return;
			}

			// Early-close last bar (12:00 / 12:15 / 14:03): NT8's Exit on session close flattens there
			// (that IsLastBarOfSession is true on that bar is UNVERIFIED). Used ONLY to suppress the stop
			// decision; no return here — the checkpoint code runs on such a bar exactly as in the base.
			bool isSessionLastBar = Bars.IsLastBarOfSession;

			// ---- (2) STOP — bar-close check on EVERY bar while in the entry's position. ----
			// Close <= fill - m*ATR (long) / Close >= fill + m*ATR (short), rearranged with ATR = atrSum/AtrPeriod
			// so a tie compares exactly in binary: prices are 0.25 multiples and every grid m is a 0.25 multiple.
			// Assumes the entry fill is processed (OnExecutionUpdate) before the fill bar's OnBarUpdate (UNVERIFIED).
			if (StopAtrMult > 0.0 && haveStopLevel && !isSessionLastBar
				&& Position.MarketPosition == stopSide && Position.MarketPosition != MarketPosition.Flat)
			{
				if (stopSide == MarketPosition.Long)
				{
					if (AtrPeriod * (stopFill - Close[0]) >= StopAtrMult * stopAtrSum)
					{
						ExitLong("XStop", "");
						return;                      // no checkpoint exit and no entry on the stop's decision bar
					}
				}
				else if (stopSide == MarketPosition.Short)
				{
					if (AtrPeriod * (Close[0] - stopFill) >= StopAtrMult * stopAtrSum)
					{
						ExitShort("XStop", "");
						return;                      // no checkpoint exit and no entry on the stop's decision bar
					}
				}
			}

			// ---- (3) CHECKPOINT — HH:00 / HH:30 strictly inside RTH (as base). ----
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

			double price = Close[0];
			MarketPosition mp = Position.MarketPosition;

			if (mp == MarketPosition.Long)
			{
				// OppBand: opposite band (Lower). BandOrVWAP / Flat1559: max(Upper, VWAP), band alone at zero volume.
				double trail;
				if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
					trail = curLower;
				else
					trail = (vwapCumVol > 0) ? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= trail)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// OppBand: opposite band (Upper). BandOrVWAP / Flat1559: min(Lower, VWAP), band alone at zero volume.
				double trail;
				if (ExitPolicy == PraxisNoiseArmBExitPolicy.OppBand)
					trail = curUpper;
				else
					trail = (vwapCumVol > 0) ? Math.Min(curLower, curVwap) : curLower;
				if (price >= trail)
					ExitShort("XS", "");
			}

			// Entry / reversal as base. With the stop on, no entry until ATR exists (spec §4 warm-up).
			bool atrGateOpen = (StopAtrMult <= 0.0) || haveAtr;
			if (atrGateOpen)
			{
				if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
					EnterLong(Contracts, "L");
				else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
					EnterShort(Contracts, "S");
			}
		}

		// ---- STOP LEVEL — fixed at the entry fill; uses StopAtrMult, never NoiseMult. ----
		protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity,
			MarketPosition marketPosition, string orderId, DateTime time)
		{
			if (execution.Order == null || execution.Order.OrderState != OrderState.Filled)
				return;

			string name = execution.Order.Name;
			if (name != "L" && name != "S")
				return;
			if (!(StopAtrMult > 0.0) || !haveAtr)
				return;

			bool isLong   = (name == "L");
			stopSide      = isLong ? MarketPosition.Long : MarketPosition.Short;
			stopFill      = execution.Order.AverageFillPrice;
			stopAtrSum    = atrSum;
			stopLevel     = isLong
				? stopFill - StopAtrMult * (stopAtrSum / AtrPeriod)
				: stopFill + StopAtrMult * (stopAtrSum / AtrPeriod);
			haveStopLevel = true;

			Print(string.Format(CultureInfo.InvariantCulture,
				"{0} ENTRY {1} {2} FILL={3:R} ATR={4:R} LEVEL={5:R}",
				Name, time.ToString("yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture),
				isLong ? "LONG" : "SHORT", stopFill, curAtr, stopLevel));
		}

		#region Band construction (as base; Lookback and NoiseMult are inputs)
		private void BuildBand(int mod)
		{
			haveBand = false;
			if (todayOpen <= 0)
				return;

			double sumAbs = 0.0;
			int cnt = 0;
			for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
			{
				DayRecord rec = history[d];
				double c;
				if (rec.Open > 0 && rec.Closes.TryGetValue(mod, out c))
				{
					sumAbs += Math.Abs(c / rec.Open - 1.0);
					cnt++;
				}
			}
			if (cnt < Lookback)
				return;

			curSigma = sumAbs / cnt;
			double refUpper = Math.Max(todayOpen, prevClose);
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + NoiseMult * curSigma);
			curLower = refLower * (1.0 - NoiseMult * curSigma);
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
			haveBand = true;
		}
		#endregion

		#region Daily ATR (completed RTH sessions; no second series, no NT8 ATR indicator)
		// TR_i = max(High_i, PrevClose_i) - min(Low_i, PrevClose_i); ATR = mean of the last AtrPeriod TRs.
		// Needs AtrPeriod completed sessions in history, each carrying its own prior close, = 15 completed
		// sessions (14 true ranges plus one prior close). The data's first session is never committed (as base),
		// but its last close is s2's PrevClose, so ATR first exists at s16.
		private void ComputeAtr()
		{
			haveAtr = history.Count >= AtrPeriod;
			if (!haveAtr)
				return;

			double sum = 0.0;
			for (int i = history.Count - AtrPeriod; i <= history.Count - 1; i++)
			{
				DayRecord rec = history[i];
				sum += Math.Max(rec.High, rec.PrevClose) - Math.Min(rec.Low, rec.PrevClose);
			}
			atrSum = sum;
			curAtr = atrSum / AtrPeriod;
		}
		#endregion

		#region Oracle print (T6(ii))
		private void PrintOracle()
		{
			string band = haveBand
				? string.Format(CultureInfo.InvariantCulture, "SIGMA={0:R} UPPER={1:R} LOWER={2:R}", curSigma, curUpper, curLower)
				: "NOBAND";
			string atr = haveAtr
				? string.Format(CultureInfo.InvariantCulture, "ATR={0:R}", curAtr)
				: "NOATR";
			Print(string.Format(CultureInfo.InvariantCulture,
				"{0} ORACLE {1} 10:00 Lookback={2} NoiseMult={3:R} {4} {5}",
				Name, Time[0].Date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture), Lookback, NoiseMult, band, atr));
		}
		#endregion

		#region Session commit / flatten (as base)
		private void CommitDay()
		{
			if (today != null && today.Open > 0 && today.Closes.Count > 0)
			{
				history.Add(today);
				while (history.Count > HistoryCap)
					history.RemoveAt(0);
			}
			today = null;
		}

		private void FlattenAll(string reason)
		{
			if (Position.MarketPosition == MarketPosition.Long)
				ExitLong("FlatEOD", "");
			else if (Position.MarketPosition == MarketPosition.Short)
				ExitShort("FlatEOD", "");
		}
		#endregion

		#region Properties
		// [Range] enforcement for values set through the bridge (not the UI) is UNVERIFIED.
		[NinjaScriptProperty]
		[Range(2, 60)]
		[Display(Name = "Lookback (sessions)", Description = "Completed sessions in the per-minute sigma mean. Default = arm (a) value; grid per spec §3.", GroupName = "02. Praxis (tunable)", Order = 1)]
		public int Lookback { get; set; }

		[NinjaScriptProperty]
		[Range(0.1, 5.0)]
		[Display(Name = "Noise multiplier", Description = "Band half-width multiplier on sigma. Default 1.0 (arm a). Grid {0.8, 1.0, 1.2}.", GroupName = "02. Praxis (tunable)", Order = 2)]
		public double NoiseMult { get; set; }

		[NinjaScriptProperty]
		[Range(0.0, 10.0)]
		[Display(Name = "Stop ATR multiplier", Description = "Stop at entry fill -/+ m x daily ATR, bar-close check, market exit. 0 = no stop (acceptance tests T1-T3 only). Grid {1.5, 2.25, 3.0}.", GroupName = "02. Praxis (tunable)", Order = 3)]
		public double StopAtrMult { get; set; }

		[NinjaScriptProperty]
		[Display(Name = "Exit policy", Description = "BandOrVWAP = max/min(band, VWAP) trail; OppBand = opposite band; Flat1559 = BandOrVWAP exits, flatten on the 15:59 bar. Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 4)]
		public PraxisNoiseArmBExitPolicy ExitPolicy { get; set; }

		[NinjaScriptProperty]
		[Range(1, 20)]
		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only).", GroupName = "02. Praxis (tunable)", Order = 5)]
		public int Contracts { get; set; }

		[Browsable(false)]
		[XmlIgnore]
		public double SessionSigma { get { return curSigma; } }   // exposed for debugging/reconcile only
		#endregion
	}
}
