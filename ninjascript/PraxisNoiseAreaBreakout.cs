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

// PRAXIS B2 (bead Praxis_build-4uu) — NOISE-AREA BREAKOUT backtest Strategy.
//
// PURPOSE: faithful, self-contained NT8 Strategy Analyzer replication of the intraday
// momentum "Noise Area" strategy of Zarattini/Aziz/Barbon, SSRN 4824172 (SFI RP 24-97,
// 3-Feb-2025 revision). Canonical ruleset spec: docs/specs/2026-07-16-b2-noise-area-ruleset.md.
// Traceability: docs/reports/2026-07-16-4uu-noise-area-strategy.md.
//
// This is NOT the file-drop signal consumer (PraxisSignalConsumer.cs) — it carries no order
// pipeline, no JSON, no share watcher. It computes the band itself from bar history and trades
// it inside the backtester. Only house style / namespace / usings were borrowed from the consumer.
//
// TRADER-LOCKED CHOICES (DECISION_LOG 2026-07-16, session 16 — OVERRIDE any conflicting note in
// the spec discrepancy table §5):
//   * Session-flat = 16:00 ET cash close (paper §4 p.9/12; NOT the 09:30-11:30 PRAXIS window).
//   * Positions/session = REVERSE & re-enter on an opposite-band cross (paper §2 p.9; NOT one/session).
//   * FIRST build = PURE PAPER REPLICATION, FIXED params: Lookback=14, band = 1xσ (NO noise
//     multiplier as a tunable), NO ATR stop. The ONLY selectable knob is the exit form (ExitMode).
//
// INSTRUMENT: NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick). Add this strategy to a
// 1-MINUTE NQ series with an RTH (09:30-16:00 ET) session template in the Strategy Analyzer.
//
// NO LOOK-AHEAD: Calculate.OnBarClose + the 14-day σ lookback reads only COMPLETED prior sessions
// (the current day is never in the history store until its session ends). See BuildBand().

namespace NinjaTrader.NinjaScript.Strategies
{
	// Exit form — the ONLY tunable this pass (spec §6 param-map row "exit policy"; §4 p.9,13).
	// OppBand    = base model, trailing stop at the same-side band the breakout came through.
	// BandOrVWAP = paper's PREFERRED model, trailing stop at max/min(band, VWAP) (§4 p.13). DEFAULT.
	public enum PraxisNoiseExitMode
	{
		OppBand,
		BandOrVWAP
	}

	public class PraxisNoiseAreaBreakout : Strategy
	{
		#region Fixed session clock (trader-locked; not exposed)
		// Minute-of-day (ET) constants. Session Open = 09:30, cash Close = 16:00 (spec §1, §4).
		private const int OpenMod  = 9 * 60 + 30;   // 570
		private const int CloseMod = 16 * 60;       // 960
		#endregion

		#region Per-day history store (completed sessions only — no look-ahead)
		// One record per COMPLETED RTH session: the 09:30 open and the close at every
		// minute-of-day seen that session. σ at a checkpoint is the 14-day mean of
		// |Close_{HH:MM}/Open_{09:30} − 1| over these records (spec §1 eqs. pp.6-7).
		private sealed class DayRecord
		{
			public double Open;                                  // Open_{t,09:30}
			public double Close1600;                             // Close_{t,16:00} (prev-close ref, spec §1 p.7)
			public readonly Dictionary<int, double> Closes =     // minute-of-day -> Close at that minute
				new Dictionary<int, double>();
		}

		// spec §1/§3 p.6 — FIXED 14 trading days. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const int Lookback = 14;
		// spec §1 p.7 / §5 D1 — paper half-width is EXACTLY 1xσ. paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		private const double BandSigmaMult = 1.0;

		private readonly List<DayRecord> history = new List<DayRecord>();  // oldest..newest
		private int HistoryCap { get { return Lookback + 15; } }           // keep a small surplus over Lookback

		// Current (in-progress) session accumulators — NOT visible to σ until the session closes.
		private DayRecord today;
		private double     todayOpen;      // Open_{t,09:30}
		private double     prevClose;      // Close_{t-1,16:00}  (overnight-gap ref, spec §1 p.7)
		private bool       haveDay;

		// Session-anchored VWAP (spec §4 p.13, footnote 2: RTH data only, anchored at 09:30 open).
		private double vwapCumPV;
		private double vwapCumVol;

		// Last computed band/VWAP for the current bar (recomputed every bar for the plots;
		// order actions still fire ONLY at HH:00/HH:30 checkpoints — spec §2 p.9).
		private double curUpper, curLower, curVwap, curSigma;
		private bool   haveBand;
		#endregion

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adjustment; act only at HH:00/HH:30; reverse on opposite-band cross; flat at 16:00 ET.";
				Name         = "PraxisNoiseAreaBreakout";

				// OnBarClose is REQUIRED for the no-look-ahead guarantee: σ reads only closed bars.
				Calculate                                 = Calculate.OnBarClose;
				EntriesPerDirection                       = 1;
				EntryHandling                             = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
				ExitOnSessionCloseSeconds                 = 30;
				StartBehavior                             = StartBehavior.WaitUntilFlat;
				TimeInForce                               = TimeInForce.Day;
				BarsRequiredToTrade                       = 20;
				IsInstantiatedOnEachOptimizationIteration = false;

				// --- Paper-fixed parameters (spec §3): Lookback=14 and BandSigmaMult=1.0 are now
				//     private consts (field region), not settable Inputs — Analyzer cannot vary them
				//     (paper-fixed, not optimizable this pass — DECISION_LOG 2026-07-16). ---
				ExitMode      = PraxisNoiseExitMode.BandOrVWAP; // spec §4 p.13 — paper's PREFERRED exit. The only knob.
				Contracts     = 1;                  // position sizing only (NOT a rule knob); paper uses vol-target sizing (§3 p.15) not ported here.

				// Band / VWAP plots — purely for the Strategy-Analyzer visual reconcile (report §checklist).
				AddPlot(Brushes.DodgerBlue, "UpperBound");
				AddPlot(Brushes.DodgerBlue, "LowerBound");
				AddPlot(Brushes.Goldenrod,  "SessionVWAP");
			}
			else if (State == State.Configure)
			{
				// (No secondary data series required — single 1-min primary series.)
			}
			else if (State == State.DataLoaded)
			{
				if (BarsPeriod.BarsPeriodType != BarsPeriodType.Minute || BarsPeriod.Value != 1)
					Print(Name + " WARNING: expected a 1-MINUTE series; got " + BarsPeriod.Value + " "
						+ BarsPeriod.BarsPeriodType + ". Minute-of-day band construction assumes 1-min bars (spec §1).");
			}
		}

		protected override void OnBarUpdate()
		{
			if (CurrentBar < 1)
				return;

			int mod = Time[0].Hour * 60 + Time[0].Minute;   // minute-of-day of THIS (closed) bar

			// ---- Session rollover: on the first bar of a new RTH session, close out the prior
			// day into history (so σ sees it ONLY once complete — no look-ahead), then reset. ----
			if (Bars.IsFirstBarOfSession)
			{
				CommitDay();                    // push yesterday into history

				today     = new DayRecord();
				todayOpen = Open[0];            // Open_{t,09:30} (spec §1) — first RTH bar's open
				today.Open = todayOpen;
				// prevClose = last bar of the prior session (its 16:00 close). Close[1] is that bar.
				prevClose = (CurrentBar >= 1) ? Close[1] : todayOpen;
				if (prevClose <= 0) prevClose = todayOpen;

				vwapCumPV  = 0.0;              // re-anchor VWAP at the 09:30 open (spec §4 p.13 fn.2)
				vwapCumVol = 0.0;
				haveDay    = true;
			}

			if (!haveDay)
				return;                         // haven't seen a session open yet in this run

			// ---- Per-bar bookkeeping: record this minute's close + advance session VWAP. ----
			today.Closes[mod] = Close[0];       // minute-of-day -> close (spec §1: Close_{t,HH:MM})
			if (mod == CloseMod)
				today.Close1600 = Close[0];

			double vol = Volume[0];
			if (vol > 0)
			{
				vwapCumPV  += ((High[0] + Low[0] + Close[0]) / 3.0) * vol;   // typical-price VWAP
				vwapCumVol += vol;
			}

			// ---- Build the band for THIS bar's minute-of-day (for plots every bar; orders only at checkpoints). ----
			BuildBand(mod);
			if (haveBand)
			{
				Values[0][0] = curUpper;
				Values[1][0] = curLower;
			}
			if (vwapCumVol > 0)
				Values[2][0] = curVwap;

			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");
				return;                          // never open a new position at/after the close
			}

			// ---- Act ONLY at semi-hourly checkpoints HH:00 / HH:30, strictly inside RTH (spec §2 p.9). ----
			bool isCheckpoint = (Time[0].Minute == 0 || Time[0].Minute == 30) && mod > OpenMod && mod < CloseMod;
			if (!isCheckpoint || !haveBand)
				return;

			double price = Close[0];             // the checkpoint stamp price (spec §2: evaluate at the stamp, not intrabar)
			MarketPosition mp = Position.MarketPosition;

			// (1) TRAILING-STOP / EXIT — evaluated ONLY at the stamp (spec §4 p.9). Reversal (2) below
			//     handles the opposite-band cross; this closes to FLAT on the same-side band/VWAP trail.
			if (mp == MarketPosition.Long)
			{
				// Long trailing stop = max(UpperBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Max(curUpper, curVwap) : curUpper;
				if (price <= stop)
					ExitLong("XL", "");
			}
			else if (mp == MarketPosition.Short)
			{
				// Short trailing stop = min(LowerBound, VWAP)  (spec §4 p.13). OppBand mode = band only.
				double stop = (ExitMode == PraxisNoiseExitMode.BandOrVWAP && vwapCumVol > 0)
					? Math.Min(curLower, curVwap) : curLower;
				if (price >= stop)
					ExitShort("XS", "");
			}

			// (2) ENTRY / REVERSAL — long above the Upper Bound, short below the Lower Bound (spec §2 p.9).
			//     A cross to the OPPOSITE bound while holding flips the position (NT8 managed reverse:
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
			if (price > curUpper && Position.MarketPosition != MarketPosition.Long)
				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
			else if (price < curLower && Position.MarketPosition != MarketPosition.Short)
				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
		}

		#region Band construction (spec §1, pp.6-7)
		// σ_{t,09:30→HH:MM} = mean over the last `Lookback` COMPLETED days of
		//   | Close_{t-i,HH:MM} / Open_{t-i,09:30} − 1 |            (spec §1 step 1-2)
		// Bounds with overnight-gap adjustment (spec §1 step 3, p.7):
		//   Upper = max(Open_{t,09:30}, Close_{t-1,16:00}) · (1 + k·σ)
		//   Lower = min(Open_{t,09:30}, Close_{t-1,16:00}) · (1 − k·σ),  k = BandSigmaMult (=1.0 paper).
		private void BuildBand(int mod)
		{
			haveBand = false;
			if (todayOpen <= 0)
				return;

			double sumAbs = 0.0;
			int cnt = 0;
			// Walk newest->oldest completed days; take up to Lookback that recorded this minute-of-day.
			for (int d = history.Count - 1; d >= 0 && cnt < Lookback; d--)
			{
				DayRecord rec = history[d];
				double c;
				if (rec.Open > 0 && rec.Closes.TryGetValue(mod, out c))
				{
					sumAbs += Math.Abs(c / rec.Open - 1.0);     // spec §1 step 1
					cnt++;
				}
			}
			if (cnt < Lookback)                                 // require a full 14-day sample (spec §3 fixed N)
				return;

			curSigma = sumAbs / cnt;                            // spec §1 step 2
			double refUpper = Math.Max(todayOpen, prevClose);   // spec §1 p.7 gap adjustment
			double refLower = Math.Min(todayOpen, prevClose);
			curUpper = refUpper * (1.0 + BandSigmaMult * curSigma);
			curLower = refLower * (1.0 - BandSigmaMult * curSigma);
			curVwap  = (vwapCumVol > 0) ? vwapCumPV / vwapCumVol : Close[0];
			haveBand = true;
		}
		#endregion

		#region Session commit / flatten
		// Push the completed in-progress day into the history store (trim to HistoryCap). Called on
		// the first bar of each new session, so the day just ended becomes available to σ — and never
		// before it is complete (the no-look-ahead invariant).
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

		#region Properties (paper-fixed defaults; ExitMode is the only intended knob)
		// Lookback and BandSigmaMult are paper-fixed, not optimizable this pass (DECISION_LOG 2026-07-16).
		// They live as private consts (see field region) so the Strategy Analyzer cannot vary them.

		[NinjaScriptProperty]
		[Display(Name = "Exit mode (ONLY tunable)", Description = "OppBand = trailing stop at same-side band; BandOrVWAP = max/min(band, VWAP), the paper's PREFERRED model (spec §4 p.13). Default BandOrVWAP.", GroupName = "02. Praxis (tunable)", Order = 1)]
		public PraxisNoiseExitMode ExitMode { get; set; }

		[NinjaScriptProperty]
		[Range(1, 20)]
		[Display(Name = "Contracts", Description = "Position size in NQ contracts (sizing only, NOT a rule knob). Paper uses 2% vol-target sizing (§3 p.15), not ported this pass.", GroupName = "02. Praxis (tunable)", Order = 2)]
		public int Contracts { get; set; }

		[Browsable(false)]
		[XmlIgnore]
		public double SessionSigma { get { return curSigma; } }   // exposed for debugging/reconcile only
		#endregion
	}
}
