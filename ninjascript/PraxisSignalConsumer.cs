#region Using declarations
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using NinjaTrader.Cbi;
using NinjaTrader.Data;
using NinjaTrader.Gui;
using NinjaTrader.Gui.Chart;
using NinjaTrader.Gui.SuperDom;
using NinjaTrader.Gui.Tools;
using NinjaTrader.NinjaScript;
using NinjaTrader.Core.FloatingPoint;
#endregion

// PRAXIS B1-f (bead Praxis_build-ct5) — SIM-ONLY file-drop signal consumer.
//
// Signal path: TradingView -> n8n (local Docker) -> atomic tmp+rename into outbox ->
// launchd sweep -> /Users/admin/praxis-signals (Mac) -> Parallels shared folder ->
// THIS strategy inside the Win11 VM -> ONE sim bracket order per signal_id.
//
// DEDUP CONTRACT (B1-d Finding F2 / bead 9tl): the drop FILENAME is keyed on ts+signal_id,
// so a redelivered signal_id with a regenerated ts arrives as a NEW file. File-level dedup
// is insufficient. This strategy dedupes on the in-file `signal_id` JSON field via an
// in-memory HashSet backed by an append-only journal reloaded on startup, so an NT8
// restart does NOT replay already-actioned signals.
//
// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
// (e.g. Sim101). The guard is a const — there is no parameter to disable it.

namespace NinjaTrader.NinjaScript.Strategies
{
	public class PraxisSignalConsumer : Strategy
	{
		#region Hard scope wall (non-configurable)
		// SIM ONLY. This prefix check is intentionally a const with no property exposing it.
		private const string RequiredAccountPrefix = "Sim";
		private bool accountIsSim;
		#endregion

		#region Private state
		private const string LogPrefix        = "PRAXIS-B1f";
		private const int    MaxReadAttempts  = 5;
		private const string JournalFileName  = "praxis-processed-signals.log"; // .log so *.json scans never pick it up
		private const string TemplateFileName = "signal-template.json";          // pre-existing template in drop dir — never a signal

		private readonly object                  sync             = new object();
		private readonly Queue<string>           pendingQueue     = new Queue<string>();
		private readonly HashSet<string>         pendingSet       = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
		private readonly Dictionary<string, int> readAttempts     = new Dictionary<string, int>(StringComparer.OrdinalIgnoreCase);
		private readonly HashSet<string>         processedSignals = new HashSet<string>(StringComparer.Ordinal);

		private FileSystemWatcher   watcher;
		private System.Timers.Timer rescanTimer;
		private StreamWriter        journal;
		private string              journalPath;
		private string              processedDir;
		private string              duplicatesDir;
		private string              rejectedDir;
		private bool                draining;
		private bool                started;
		#endregion

		protected override void OnStateChange()
		{
			if (State == State.SetDefaults)
			{
				Description                              = "PRAXIS B1-f sim-only signal consumer: watches the Parallels-shared drop dir, dedupes on in-file signal_id (journal-backed), places ONE sim bracket order per signal.";
				Name                                     = "PraxisSignalConsumer";
				Calculate                                = Calculate.OnBarClose;
				EntriesPerDirection                      = 10;                       // allow several concurrent signals
				EntryHandling                            = EntryHandling.AllEntries;
				IsExitOnSessionCloseStrategy             = false;
				StartBehavior                            = StartBehavior.WaitUntilFlat;
				TimeInForce                              = TimeInForce.Gtc;
				BarsRequiredToTrade                      = 0;
				IsInstantiatedOnEachOptimizationIteration = false;

				SignalsPath        = @"\\Mac\praxis-signals";   // B1-c scoped share; use Z:\praxis-signals while whole-home share persists
				RescanSeconds      = 15;
				DefaultStopTicks   = 40;                        // NQ: 40 ticks = 10.00 pts
				DefaultTargetTicks = 80;                        // NQ: 80 ticks = 20.00 pts
				MaxQty             = 5;                         // sim sanity cap
			}
			else if (State == State.DataLoaded)
			{
				accountIsSim = Account != null
					&& !string.IsNullOrEmpty(Account.Name)
					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);

				if (!accountIsSim)
				{
					string acct = (Account == null || Account.Name == null) ? "<null>" : Account.Name;
					Log(LogPrefix + " REFUSED: account '" + acct + "' is not a Sim account (must start with '"
						+ RequiredAccountPrefix + "'). No signals will be processed. SIM ONLY.", LogLevel.Error);
					Print(LogPrefix + " REFUSED non-sim account '" + acct + "' — consumer disabled.");
				}
			}
			else if (State == State.Realtime)
			{
				if (!accountIsSim)
				{
					Log(LogPrefix + " realtime reached on non-sim account — watcher NOT started.", LogLevel.Error);
					return;
				}
				try
				{
					StartConsumer();
				}
				catch (Exception ex)
				{
					Log(LogPrefix + " FAILED to start consumer on '" + SignalsPath + "': " + ex.Message
						+ " — check the Parallels share path parameter.", LogLevel.Error);
					Print(LogPrefix + " start failure: " + ex);
				}
			}
			else if (State == State.Terminated)
			{
				StopConsumer();
			}
		}

		protected override void OnBarUpdate()
		{
			// Belt-and-braces drain; primary marshalling is TriggerCustomEvent from watcher/timer threads.
			if (State == State.Realtime && started)
				DrainQueue();
		}

		#region Startup / shutdown
		private void StartConsumer()
		{
			if (started)
				return;

			if (string.IsNullOrWhiteSpace(SignalsPath) || !Directory.Exists(SignalsPath))
				throw new DirectoryNotFoundException("Signals directory not found: '" + SignalsPath + "'");

			processedDir  = Path.Combine(SignalsPath, "processed");
			duplicatesDir = Path.Combine(processedDir, "duplicates");
			rejectedDir   = Path.Combine(SignalsPath, "rejected");
			journalPath   = Path.Combine(SignalsPath, JournalFileName);
			Directory.CreateDirectory(processedDir);
			Directory.CreateDirectory(duplicatesDir);
			Directory.CreateDirectory(rejectedDir);

			LoadJournal();
			journal = new StreamWriter(new FileStream(journalPath, FileMode.Append, FileAccess.Write, FileShare.Read), Encoding.UTF8)
			{
				AutoFlush = true
			};

			// FileSystemWatcher: Created + Renamed (atomic tmp->rename upstream may surface either way through the share).
			watcher = new FileSystemWatcher(SignalsPath, "*.json")
			{
				IncludeSubdirectories = false,
				NotifyFilter          = NotifyFilters.FileName | NotifyFilters.LastWrite | NotifyFilters.Size
			};
			watcher.Created += OnFsCreated;
			watcher.Renamed += OnFsRenamed;
			watcher.Error   += OnFsError;
			watcher.EnableRaisingEvents = true;

			// Periodic rescan = missed-event insurance (WatchPaths-style backstop, same philosophy as B1-b-fu).
			rescanTimer = new System.Timers.Timer(Math.Max(5, RescanSeconds) * 1000.0) { AutoReset = true };
			rescanTimer.Elapsed += (s, e) => ScanDirectory("rescan");
			rescanTimer.Start();

			started = true;
			Print(LogPrefix + " STARTED on account '" + Account.Name + "', dir '" + SignalsPath + "', "
				+ processedSignals.Count + " journaled signal_ids loaded, rescan every " + RescanSeconds + "s.");
			Log(LogPrefix + " consumer started (sim account " + Account.Name + ").", LogLevel.Information);

			// Startup catch-up scan: anything already sitting in the drop dir.
			ScanDirectory("startup catch-up");
		}

		private void StopConsumer()
		{
			try
			{
				if (watcher != null)
				{
					watcher.EnableRaisingEvents = false;
					watcher.Created -= OnFsCreated;
					watcher.Renamed -= OnFsRenamed;
					watcher.Error   -= OnFsError;
					watcher.Dispose();
					watcher = null;
				}
				if (rescanTimer != null)
				{
					rescanTimer.Stop();
					rescanTimer.Dispose();
					rescanTimer = null;
				}
				if (journal != null)
				{
					journal.Flush();
					journal.Dispose();
					journal = null;
				}
				if (started)
					Print(LogPrefix + " stopped.");
			}
			catch (Exception ex)
			{
				Print(LogPrefix + " shutdown error (non-fatal): " + ex.Message);
			}
			finally
			{
				started = false;
			}
		}
		#endregion

		#region Journal (persisted dedup — reload on startup so restart does not replay)
		// Append-only, one line per actioned signal: signal_id <TAB> utc-ts <TAB> filename <TAB> status
		// Retention: permanent within the file (effectively an unbounded idempotency window). At sim
		// signal volumes this stays tiny; archive manually if it ever grows large. Rejected files are
		// NOT journaled — a corrected redelivery of a previously-malformed signal_id may still trade.
		private void LoadJournal()
		{
			processedSignals.Clear();
			if (!File.Exists(journalPath))
				return;
			foreach (string line in File.ReadAllLines(journalPath))
			{
				if (string.IsNullOrWhiteSpace(line))
					continue;
				int tab = line.IndexOf('\t');
				string id = tab > 0 ? line.Substring(0, tab) : line.Trim();
				if (id.Length > 0)
					processedSignals.Add(id);
			}
		}

		private void JournalWrite(string signalId, string fileName, string status)
		{
			if (journal == null)
				return;
			journal.WriteLine(signalId + "\t" + DateTime.UtcNow.ToString("o", CultureInfo.InvariantCulture)
				+ "\t" + fileName + "\t" + status);
			journal.Flush();
		}
		#endregion

		#region File-event plumbing (threading: FSW/timer threads only enqueue + TriggerCustomEvent)
		private void OnFsCreated(object sender, FileSystemEventArgs e) { EnqueueFile(e.FullPath); }

		private void OnFsRenamed(object sender, RenamedEventArgs e)
		{
			if (e.FullPath != null && e.FullPath.EndsWith(".json", StringComparison.OrdinalIgnoreCase))
				EnqueueFile(e.FullPath);
		}

		private void OnFsError(object sender, ErrorEventArgs e)
		{
			// Buffer overflow or share hiccup — the rescan timer is the recovery path.
			Print(LogPrefix + " FileSystemWatcher error (rescan timer will recover): "
				+ (e.GetException() == null ? "unknown" : e.GetException().Message));
		}

		private void ScanDirectory(string reason)
		{
			try
			{
				if (!started || !Directory.Exists(SignalsPath))
					return;
				string[] files = Directory.GetFiles(SignalsPath, "*.json", SearchOption.TopDirectoryOnly);
				foreach (string f in files)
					EnqueueFile(f);
			}
			catch (Exception ex)
			{
				Print(LogPrefix + " " + reason + " scan failed: " + ex.Message);
			}
		}

		private void EnqueueFile(string fullPath)
		{
			if (string.IsNullOrEmpty(fullPath) || !fullPath.EndsWith(".json", StringComparison.OrdinalIgnoreCase))
				return;
			string name = Path.GetFileName(fullPath);
			if (string.Equals(name, TemplateFileName, StringComparison.OrdinalIgnoreCase))
				return; // never treat the template as a signal

			lock (sync)
			{
				if (pendingSet.Contains(fullPath))
					return;
				pendingSet.Add(fullPath);
				pendingQueue.Enqueue(fullPath);
			}
			// Marshal onto the strategy thread per NT8 threading rules — order methods are
			// never called from the watcher/timer threads.
			try { TriggerCustomEvent(o => DrainQueue(), null); }
			catch (Exception ex) { Print(LogPrefix + " TriggerCustomEvent failed (will drain on rescan/bar): " + ex.Message); }
		}

		private void DrainQueue()
		{
			if (State != State.Realtime || !started || !accountIsSim || draining)
				return;
			draining = true;
			try
			{
				while (true)
				{
					string path;
					lock (sync)
					{
						if (pendingQueue.Count == 0)
							break;
						path = pendingQueue.Dequeue();
						pendingSet.Remove(path);
					}
					try { ProcessFile(path); }
					catch (Exception ex)
					{
						Print(LogPrefix + " unexpected error processing '" + Path.GetFileName(path) + "': " + ex);
						Log(LogPrefix + " unexpected processing error on " + Path.GetFileName(path) + ": " + ex.Message, LogLevel.Error);
					}
				}
			}
			finally { draining = false; }
		}
		#endregion

		#region Per-file processing
		private void ProcessFile(string fullPath)
		{
			string fileName = Path.GetFileName(fullPath);
			if (!File.Exists(fullPath))
				return; // already moved (duplicate enqueue race)

			string text;
			try
			{
				text = File.ReadAllText(fullPath, Encoding.UTF8);
			}
			catch (IOException ioex)
			{
				// File may still be materializing across the share — retry via rescan, cap attempts.
				int attempts;
				lock (sync)
				{
					readAttempts.TryGetValue(fullPath, out attempts);
					readAttempts[fullPath] = ++attempts;
				}
				if (attempts < MaxReadAttempts)
				{
					Print(LogPrefix + " signal_id=? file '" + fileName + "' not readable yet (attempt "
						+ attempts + "/" + MaxReadAttempts + ") — deferred to rescan: " + ioex.Message);
					return;
				}
				RejectFile(fullPath, "?", "unreadable after " + MaxReadAttempts + " attempts: " + ioex.Message);
				return;
			}
			lock (sync) { readAttempts.Remove(fullPath); }

			// Parse (strict hand-rolled flat-JSON parser — see report; no external packages).
			Dictionary<string, object> fields;
			try
			{
				fields = ParseFlatJson(text);
			}
			catch (Exception pex)
			{
				RejectFile(fullPath, "?", "malformed JSON: " + pex.Message);
				return;
			}

			ParsedSignal sig;
			string error = ValidateSignal(fields, out sig);
			string sid = (sig != null && !string.IsNullOrEmpty(sig.SignalId)) ? sig.SignalId
				: (fields.ContainsKey("signal_id") && fields["signal_id"] is string ? (string)fields["signal_id"] : "?");
			if (error != null)
			{
				RejectFile(fullPath, sid, error);
				return;
			}

			// ---- DEDUP on in-file signal_id (contract 9tl / B1-d F2) ----
			if (processedSignals.Contains(sig.SignalId))
			{
				Print(LogPrefix + " signal_id=" + sig.SignalId + " DUPLICATE (file '" + fileName
					+ "') — no order placed, exactly-once contract held.");
				JournalWrite(sig.SignalId, fileName, "DUPLICATE");
				MoveTo(fullPath, duplicatesDir, sig.SignalId);
				return;
			}

			// Record BEFORE submitting (at-most-once: a crash between journal write and submit
			// loses the order but can never double-fire it — correct bias for an order pipeline).
			processedSignals.Add(sig.SignalId);
			JournalWrite(sig.SignalId, fileName, "ACCEPTED");

			bool submitted = SubmitBracket(sig);
			if (submitted)
			{
				Print(LogPrefix + " signal_id=" + sig.SignalId + " ACCEPTED: " + sig.Side + " " + sig.Qty
					+ " " + sig.Symbol + " ref=" + sig.Price.ToString(CultureInfo.InvariantCulture)
					+ " stop=" + sig.ResolvedStop.ToString(CultureInfo.InvariantCulture)
					+ " target=" + sig.ResolvedTarget.ToString(CultureInfo.InvariantCulture)
					+ " (file '" + fileName + "')");
				MoveTo(fullPath, processedDir, sig.SignalId);
			}
			else
			{
				// signal_id stays journaled (at-most-once). Trader intervention needed to re-fire.
				Log(LogPrefix + " signal_id=" + sig.SignalId + " order submission FAILED after journaling — "
					+ "will NOT auto-retry (exactly-once bias). File moved to rejected/.", LogLevel.Error);
				MoveTo(fullPath, rejectedDir, sig.SignalId);
			}
		}

		private void RejectFile(string fullPath, string signalId, string reason)
		{
			Print(LogPrefix + " signal_id=" + signalId + " REJECTED (file '" + Path.GetFileName(fullPath)
				+ "'): " + reason + " — NO order.");
			Log(LogPrefix + " rejected signal_id=" + signalId + ": " + reason, LogLevel.Warning);
			MoveTo(fullPath, rejectedDir, signalId);
		}

		private void MoveTo(string fullPath, string destDir, string signalId)
		{
			try
			{
				if (!File.Exists(fullPath))
					return;
				Directory.CreateDirectory(destDir);
				string dest = Path.Combine(destDir, Path.GetFileName(fullPath));
				if (File.Exists(dest))
					dest = Path.Combine(destDir, Path.GetFileNameWithoutExtension(fullPath) + "."
						+ DateTime.UtcNow.ToString("yyyyMMddTHHmmssfff", CultureInfo.InvariantCulture) + ".json");
				File.Move(fullPath, dest);
			}
			catch (Exception ex)
			{
				Print(LogPrefix + " signal_id=" + signalId + " could not move '" + Path.GetFileName(fullPath)
					+ "' to " + destDir + ": " + ex.Message + " (dedup still holds via journal).");
			}
		}
		#endregion

		#region Validation
		private sealed class ParsedSignal
		{
			public string  SignalId;
			public string  Symbol;
			public string  Side;      // "BUY" | "SELL" (normalized upper)
			public int     Qty;
			public double  Price;     // reference/entry price from payload
			public double? Stop;      // optional in-file overrides
			public double? Target;
			public string  Ts;
			public double  ResolvedStop;
			public double  ResolvedTarget;
		}

		// Required per B1-d resolved contract: symbol, side(BUY|SELL), qty(>0), price(finite), signal_id, ts(ISO).
		// stop/target are OPTIONAL in-file overrides; absent -> derived from Default*Ticks off `price`.
		private string ValidateSignal(Dictionary<string, object> f, out ParsedSignal sig)
		{
			sig = new ParsedSignal();

			string s;
			if (!TryGetString(f, "signal_id", out s) || s.Trim().Length == 0)
				return "missing/empty required field 'signal_id'";
			sig.SignalId = s.Trim();

			if (!TryGetString(f, "symbol", out s) || s.Trim().Length == 0)
				return "missing/empty required field 'symbol'";
			sig.Symbol = s.Trim();

			if (!TryGetString(f, "side", out s))
				return "missing required field 'side'";
			sig.Side = s.Trim().ToUpperInvariant();
			if (sig.Side != "BUY" && sig.Side != "SELL")
				return "invalid 'side' (must be BUY or SELL): '" + s + "'";

			double d;
			if (!TryGetNumber(f, "qty", out d))
				return "missing/non-numeric required field 'qty'";
			if (double.IsNaN(d) || double.IsInfinity(d) || d <= 0 || d != Math.Floor(d))
				return "invalid 'qty' (must be positive integer): " + d.ToString(CultureInfo.InvariantCulture);
			if (d > MaxQty)
				return "'qty' " + d + " exceeds sim MaxQty cap " + MaxQty;
			sig.Qty = (int)d;

			if (!TryGetNumber(f, "price", out d) || double.IsNaN(d) || double.IsInfinity(d) || d <= 0)
				return "missing/invalid required field 'price'";
			sig.Price = d;

			if (!TryGetString(f, "ts", out s) || s.Trim().Length == 0)
				return "missing/empty required field 'ts'";
			DateTime tsParsed;
			if (!DateTime.TryParse(s, CultureInfo.InvariantCulture, DateTimeStyles.AdjustToUniversal | DateTimeStyles.AssumeUniversal, out tsParsed))
				return "unparseable 'ts': '" + s + "'";
			sig.Ts = s.Trim();

			if (f.ContainsKey("stop"))
			{
				if (!TryGetNumber(f, "stop", out d) || double.IsNaN(d) || double.IsInfinity(d) || d <= 0)
					return "invalid optional 'stop'";
				sig.Stop = d;
			}
			if (f.ContainsKey("target"))
			{
				if (!TryGetNumber(f, "target", out d) || double.IsNaN(d) || double.IsInfinity(d) || d <= 0)
					return "invalid optional 'target'";
				sig.Target = d;
			}

			// Instrument scope: payload symbol must match the chart instrument this strategy runs on.
			string chartSymbol = Instrument.MasterInstrument.Name; // e.g. "NQ"
			if (!string.Equals(sig.Symbol, chartSymbol, StringComparison.OrdinalIgnoreCase))
				return "symbol '" + sig.Symbol + "' does not match strategy instrument '" + chartSymbol + "'";

			// Resolve bracket levels (tick-rounded) and enforce side sanity.
			double tick = Instrument.MasterInstrument.TickSize;
			bool isBuy  = sig.Side == "BUY";
			double stop   = sig.Stop   ?? (isBuy ? sig.Price - DefaultStopTicks   * tick : sig.Price + DefaultStopTicks   * tick);
			double target = sig.Target ?? (isBuy ? sig.Price + DefaultTargetTicks * tick : sig.Price - DefaultTargetTicks * tick);
			stop   = Instrument.MasterInstrument.RoundToTickSize(stop);
			target = Instrument.MasterInstrument.RoundToTickSize(target);
			if (isBuy  && !(stop < sig.Price && sig.Price < target))
				return "BUY bracket not sane: need stop < price < target (stop=" + stop + " price=" + sig.Price + " target=" + target + ")";
			if (!isBuy && !(target < sig.Price && sig.Price < stop))
				return "SELL bracket not sane: need target < price < stop (target=" + target + " price=" + sig.Price + " stop=" + stop + ")";
			sig.ResolvedStop   = stop;
			sig.ResolvedTarget = target;

			return null;
		}

		private static bool TryGetString(Dictionary<string, object> f, string key, out string value)
		{
			object o;
			value = null;
			if (!f.TryGetValue(key, out o) || !(o is string))
				return false;
			value = (string)o;
			return true;
		}

		private static bool TryGetNumber(Dictionary<string, object> f, string key, out double value)
		{
			object o;
			value = double.NaN;
			if (!f.TryGetValue(key, out o) || !(o is double))
				return false;
			value = (double)o;
			return true;
		}
		#endregion

		#region Order submission (managed approach: Set* brackets are OCO'd by NT8 per entry signal)
		private bool SubmitBracket(ParsedSignal sig)
		{
			// Defense in depth: re-assert the sim wall at the order boundary.
			if (!accountIsSim || Account == null
				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
			{
				Log(LogPrefix + " signal_id=" + sig.SignalId + " ORDER REFUSED: account is not Sim. SIM ONLY.", LogLevel.Error);
				return false;
			}
			if (State != State.Realtime)
			{
				Print(LogPrefix + " signal_id=" + sig.SignalId + " refused: strategy not in Realtime state.");
				return false;
			}

			try
			{
				string entrySignal = "PRX-" + SanitizeSignalName(sig.SignalId);

				// Managed approach: Set* MUST precede the entry; NT8 submits the stop-loss and
				// profit-target as an OCO pair tied to this entry signal once the entry fills.
				SetStopLoss(entrySignal, CalculationMode.Price, sig.ResolvedStop, false);
				SetProfitTarget(entrySignal, CalculationMode.Price, sig.ResolvedTarget);

				if (sig.Side == "BUY")
					EnterLong(sig.Qty, entrySignal);
				else
					EnterShort(sig.Qty, entrySignal);

				Print(LogPrefix + " signal_id=" + sig.SignalId + " bracket submitted: entry=" + entrySignal
					+ " " + sig.Side + " qty=" + sig.Qty + " SL=" + sig.ResolvedStop + " PT=" + sig.ResolvedTarget
					+ " acct=" + Account.Name);
				return true;
			}
			catch (Exception ex)
			{
				Print(LogPrefix + " signal_id=" + sig.SignalId + " order submission threw: " + ex);
				return false;
			}
		}

		private static string SanitizeSignalName(string id)
		{
			var sb = new StringBuilder(id.Length);
			foreach (char c in id)
				sb.Append(char.IsLetterOrDigit(c) || c == '_' || c == '-' || c == '.' ? c : '_');
			string s = sb.ToString();
			return s.Length > 40 ? s.Substring(0, 40) : s;
		}
		#endregion

		#region Minimal strict flat-JSON parser
		// Neither the B1-0 nor B1-d evidence establishes that this NT8 install bundles a JSON
		// library, so this is a dependency-free strict parser for the known flat schema:
		// one object, string/number/bool/null values only. Nested objects/arrays => reject
		// (n8n's validate node never emits them). Throws FormatException on any deviation.
		private static Dictionary<string, object> ParseFlatJson(string text)
		{
			if (text == null)
				throw new FormatException("empty document");
			int i = 0;
			SkipWs(text, ref i);
			if (i >= text.Length || text[i] != '{')
				throw new FormatException("expected '{' at position " + i);
			i++;
			var result = new Dictionary<string, object>(StringComparer.Ordinal);
			SkipWs(text, ref i);
			if (i < text.Length && text[i] == '}')
			{
				i++;
			}
			else
			{
				while (true)
				{
					SkipWs(text, ref i);
					string key = ParseJsonString(text, ref i);
					SkipWs(text, ref i);
					if (i >= text.Length || text[i] != ':')
						throw new FormatException("expected ':' after key '" + key + "'");
					i++;
					SkipWs(text, ref i);
					result[key] = ParseJsonValue(text, ref i);
					SkipWs(text, ref i);
					if (i >= text.Length)
						throw new FormatException("unterminated object");
					if (text[i] == ',') { i++; continue; }
					if (text[i] == '}') { i++; break; }
					throw new FormatException("expected ',' or '}' at position " + i);
				}
			}
			SkipWs(text, ref i);
			if (i != text.Length)
				throw new FormatException("trailing content after object at position " + i);
			return result;
		}

		private static object ParseJsonValue(string t, ref int i)
		{
			if (i >= t.Length)
				throw new FormatException("unexpected end of document");
			char c = t[i];
			if (c == '"')
				return ParseJsonString(t, ref i);
			if (c == '{' || c == '[')
				throw new FormatException("nested objects/arrays not supported by the flat signal schema");
			if (c == 't' || c == 'f' || c == 'n')
			{
				if (string.CompareOrdinal(t, i, "true", 0, 4) == 0)  { i += 4; return true; }
				if (string.CompareOrdinal(t, i, "false", 0, 5) == 0) { i += 5; return false; }
				if (string.CompareOrdinal(t, i, "null", 0, 4) == 0)  { i += 4; return null; }
				throw new FormatException("invalid literal at position " + i);
			}
			// number
			int start = i;
			while (i < t.Length && (char.IsDigit(t[i]) || t[i] == '-' || t[i] == '+' || t[i] == '.' || t[i] == 'e' || t[i] == 'E'))
				i++;
			if (i == start)
				throw new FormatException("invalid value at position " + i);
			double d;
			if (!double.TryParse(t.Substring(start, i - start), NumberStyles.Float, CultureInfo.InvariantCulture, out d))
				throw new FormatException("invalid number '" + t.Substring(start, i - start) + "'");
			return d;
		}

		private static string ParseJsonString(string t, ref int i)
		{
			if (i >= t.Length || t[i] != '"')
				throw new FormatException("expected string at position " + i);
			i++;
			var sb = new StringBuilder();
			while (true)
			{
				if (i >= t.Length)
					throw new FormatException("unterminated string");
				char c = t[i++];
				if (c == '"')
					return sb.ToString();
				if (c == '\\')
				{
					if (i >= t.Length)
						throw new FormatException("unterminated escape");
					char e = t[i++];
					switch (e)
					{
						case '"':  sb.Append('"');  break;
						case '\\': sb.Append('\\'); break;
						case '/':  sb.Append('/');  break;
						case 'b':  sb.Append('\b'); break;
						case 'f':  sb.Append('\f'); break;
						case 'n':  sb.Append('\n'); break;
						case 'r':  sb.Append('\r'); break;
						case 't':  sb.Append('\t'); break;
						case 'u':
							if (i + 4 > t.Length)
								throw new FormatException("truncated \\u escape");
							sb.Append((char)ushort.Parse(t.Substring(i, 4), NumberStyles.HexNumber, CultureInfo.InvariantCulture));
							i += 4;
							break;
						default:
							throw new FormatException("invalid escape '\\" + e + "'");
					}
				}
				else
					sb.Append(c);
			}
		}

		private static void SkipWs(string t, ref int i)
		{
			while (i < t.Length && (t[i] == ' ' || t[i] == '\t' || t[i] == '\r' || t[i] == '\n'))
				i++;
		}
		#endregion

		#region Properties
		[NinjaScriptProperty]
		[Display(Name = "Signals directory (in-VM share path)", Description = @"Parallels share of /Users/admin/praxis-signals. Scoped share: \\Mac\praxis-signals. While the B1-0 whole-home share persists use Z:\praxis-signals.", GroupName = "01. Praxis", Order = 1)]
		public string SignalsPath { get; set; }

		[NinjaScriptProperty]
		[Range(5, 3600)]
		[Display(Name = "Rescan interval (seconds)", Description = "Missed-FSW-event insurance: periodic full *.json scan of the signals directory.", GroupName = "01. Praxis", Order = 2)]
		public int RescanSeconds { get; set; }

		[NinjaScriptProperty]
		[Range(1, 1000)]
		[Display(Name = "Default stop distance (ticks)", Description = "Used when the drop file has no 'stop' field; offset from payload 'price'.", GroupName = "01. Praxis", Order = 3)]
		public int DefaultStopTicks { get; set; }

		[NinjaScriptProperty]
		[Range(1, 2000)]
		[Display(Name = "Default target distance (ticks)", Description = "Used when the drop file has no 'target' field; offset from payload 'price'.", GroupName = "01. Praxis", Order = 4)]
		public int DefaultTargetTicks { get; set; }

		[NinjaScriptProperty]
		[Range(1, 10)]
		[Display(Name = "Max qty per signal (sim cap)", Description = "Signals with qty above this are rejected.", GroupName = "01. Praxis", Order = 5)]
		public int MaxQty { get; set; }
		#endregion
	}
}
