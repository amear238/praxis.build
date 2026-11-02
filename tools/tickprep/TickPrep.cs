// TickPrep: match per-contract NQ tick files to a back-adjusted 1-minute file, then
// write one adjusted tick file that reproduces those minute bars exactly.
//
// Commands
//   measure <minuteFile> <contracts.csv> <outDir> [--tz-in Eastern|UTC]
//       Builds 1-min bars from each contract's ticks, finds each contract's additive
//       offset, and assigns every minute of <minuteFile> to the contract + offset that
//       reproduces it. Writes report.txt, offsets.csv, segments.csv, assign.bin.
//   build   <minuteFile> <contracts.csv> <outDir> <outTickFile> [--tz-in ...]
//       Re-reads the ticks and writes only ticks whose minute is assigned to their
//       contract, shifted by that contract's offset. Strict: ticks in minutes that are
//       missing from <minuteFile> are NOT written (holes/gaps stay as they are).
//   verify  <minuteFile> <tickFile>
//       Rebuilds 1-min bars from <tickFile> and compares them with <minuteFile>.
//
// contracts.csv: name,path   (one line per contract, any order; '#' lines ignored)
// Minute file: NinjaTrader minute format, bar END time stamps: yyyyMMdd HHmmss;o;h;l;c;v
// Tick files:  NinjaTrader tick format: yyyyMMdd HHmmss[ fffffff];price;volume
// All times are compared in the minute file's time zone (US Eastern for Praxis).
// Read-only on inputs; writes only into <outDir> and <outTickFile>.
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;

static class TickPrep
{
    const long TicksPerMinute = TimeSpan.TicksPerMinute;
    static readonly CultureInfo Inv = CultureInfo.InvariantCulture;
    static TimeZoneInfo eastern = TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time");
    static bool inputIsUtc = false;
    static readonly Dictionary<string, long> forced = new Dictionary<string, long>();

    struct Bar { public long O, H, L, C, V; }   // prices in quarter-points (x4) to stay exact

    static int Main(string[] args)
    {
        try
        {
            var a = new List<string>(args);
            int tz = a.IndexOf("--tz-in");
            if (tz >= 0) { inputIsUtc = a[tz + 1].Equals("UTC", StringComparison.OrdinalIgnoreCase); a.RemoveRange(tz, 2); }
            int fo = a.IndexOf("--offsets");   // optional CSV contract,offset_points to force offsets
            if (fo >= 0)
            {
                foreach (var l in File.ReadLines(a[fo + 1]))
                {
                    var p = l.Split(',');
                    if (p.Length < 2 || l.StartsWith("#") || l.StartsWith("contract,")) continue;
                    forced[p[0].Trim()] = (long)(decimal.Parse(p[1], Inv) * 4m);
                }
                a.RemoveRange(fo, 2);
            }
            switch (a.Count > 0 ? a[0] : "")
            {
                case "measure": Measure(a[1], a[2], a[3]); return 0;
                case "build": Build(a[1], a[2], a[3], a[4]); return 0;
                case "verify": return Verify(a[1], a[2]);
                default:
                    Console.Error.WriteLine("usage: TickPrep measure|build|verify ... (see header of TickPrep.cs)");
                    return 2;
            }
        }
        catch (Exception e) { Console.Error.WriteLine("ERROR: " + e.Message); return 1; }
    }

    // ---------- parsing ----------
    static long Q(string s, int start, int len)   // price text -> quarter points, exact for 0.25 steps
    {
        decimal d = decimal.Parse(s.Substring(start, len), NumberStyles.Float, Inv);
        decimal q = d * 4m;
        if (q != decimal.Truncate(q)) throw new FormatException("price not on 0.25 grid: " + s);
        return (long)q;
    }
    static string P(long q) { return (q / 4m).ToString("0.##", Inv); }

    static long ParseStamp(string line, out int afterTime)
    {
        int y = Int(line, 0, 4), mo = Int(line, 4, 2), d = Int(line, 6, 2);
        int h = Int(line, 9, 2), mi = Int(line, 11, 2), s = Int(line, 13, 2);
        long t = new DateTime(y, mo, d, h, mi, s).Ticks;
        int i = 15;
        if (line[i] == ' ') { t += Int(line, 16, 7); i = 23; }      // 7-digit fraction = 100 ns units
        afterTime = i;                                               // index of ';'
        return t;
    }
    static int Int(string s, int start, int len)
    {
        int v = 0;
        for (int i = start; i < start + len; i++) { int c = s[i] - '0'; if (c < 0 || c > 9) throw new FormatException("bad digit in: " + s); v = v * 10 + c; }
        return v;
    }

    static readonly Dictionary<long, long> utcHourCache = new Dictionary<long, long>();
    static long ToEastern(long t)
    {
        if (!inputIsUtc) return t;
        long hour = t / TimeSpan.TicksPerHour;
        long shift;
        if (!utcHourCache.TryGetValue(hour, out shift))
        {
            var utc = new DateTime(hour * TimeSpan.TicksPerHour, DateTimeKind.Utc);
            shift = TimeZoneInfo.ConvertTimeFromUtc(utc, eastern).Ticks - utc.Ticks;
            utcHourCache[hour] = shift;
        }
        return t + shift;
    }

    // Bar END stamp for a tick: (end-1min, end]  -> a tick exactly on a minute belongs to the bar ending then.
    static long BarEnd(long t) { return ((t - 1) / TicksPerMinute + 1) * TicksPerMinute; }

    static Dictionary<long, Bar> LoadMinute(string path)
    {
        var m = new Dictionary<long, Bar>(2000000);
        foreach (var line in File.ReadLines(path))
        {
            if (line.Length < 16) continue;
            int i; long t = ParseStamp(line, out i);
            var f = line.Substring(i + 1).Split(';');
            m[t] = new Bar { O = Q(f[0], 0, f[0].Length), H = Q(f[1], 0, f[1].Length), L = Q(f[2], 0, f[2].Length), C = Q(f[3], 0, f[3].Length), V = long.Parse(f[4], Inv) };
        }
        return m;
    }

    static IEnumerable<KeyValuePair<long, string>> Ticks(string path)   // (eastern time, original line)
    {
        foreach (var line in File.ReadLines(path))
        {
            if (line.Length < 16) continue;
            int i; long t = ToEastern(ParseStamp(line, out i));
            yield return new KeyValuePair<long, string>(t, line);
        }
    }
    static void TickFields(string line, out long priceQ, out long vol)
    {
        int i; ParseStamp(line, out i);
        int j = line.IndexOf(';', i + 1);
        priceQ = Q(line, i + 1, j - i - 1);
        vol = long.Parse(line.Substring(j + 1).Trim(), Inv);
    }

    static Dictionary<long, Bar> BarsFromTicks(string path, out long nTicks)
    {
        var bars = new Dictionary<long, Bar>();
        nTicks = 0;
        foreach (var kv in Ticks(path))
        {
            long p, v; TickFields(kv.Value, out p, out v);
            long e = BarEnd(kv.Key);
            Bar b;
            if (bars.TryGetValue(e, out b)) { if (p > b.H) b.H = p; if (p < b.L) b.L = p; b.C = p; b.V += v; }
            else b = new Bar { O = p, H = p, L = p, C = p, V = v };
            bars[e] = b;
            nTicks++;
        }
        return bars;
    }

    static List<KeyValuePair<string, string>> LoadContracts(string csv)
    {
        var list = new List<KeyValuePair<string, string>>();
        foreach (var raw in File.ReadLines(csv))
        {
            var line = raw.Trim();
            if (line.Length == 0 || line.StartsWith("#") || line.StartsWith("name,")) continue;
            int c = line.IndexOf(',');
            list.Add(new KeyValuePair<string, string>(line.Substring(0, c).Trim(), line.Substring(c + 1).Trim()));
        }
        return list;
    }

    // ---------- measure ----------
    static void Measure(string minuteFile, string contractsCsv, string outDir)
    {
        Directory.CreateDirectory(outDir);
        var file = LoadMinute(minuteFile);
        var contracts = LoadContracts(contractsCsv);
        var rep = new StringBuilder();
        rep.AppendLine("TickPrep measure  " + DateTime.Now.ToString("s", Inv));
        rep.AppendLine("minute file: " + minuteFile + "  bars: " + file.Count);
        rep.AppendLine("time zone of tick input: " + (inputIsUtc ? "UTC (converted to Eastern)" : "same as minute file"));

        var raw = new List<Dictionary<long, Bar>>();
        var offsets = new long[contracts.Count];
        for (int k = 0; k < contracts.Count; k++)
        {
            long n; var bars = BarsFromTicks(contracts[k].Value, out n);
            raw.Add(bars);
            // Candidate offsets = (file - raw) where all four OHLC differences agree.
            // The source contract matches every minute of its active window at one offset, so pick
            // the offset with the longest unbroken run of matching minutes (comparing only minutes
            // where both the file and this contract have a bar). A merely steady calendar spread
            // also produces runs, but they break whenever the spread ticks.
            var runs = new Dictionary<long, int>(); var total = new Dictionary<long, int>();
            long runOff = long.MinValue; int runLen = 0;
            foreach (var t in bars.Keys.OrderBy(x => x))
            {
                Bar f; if (!file.TryGetValue(t, out f)) continue;
                var r = bars[t];
                long d = f.C - r.C;
                bool exact = f.O - r.O == d && f.H - r.H == d && f.L - r.L == d;
                if (!exact) { runOff = long.MinValue; runLen = 0; continue; }
                int c; total.TryGetValue(d, out c); total[d] = c + 1;
                if (d == runOff) runLen++; else { runOff = d; runLen = 1; }
                int best0; runs.TryGetValue(d, out best0); if (runLen > best0) runs[d] = runLen;
            }
            var ranked = runs.OrderByDescending(x => x.Value).ToList();
            long chosen = ranked.Count > 0 ? ranked[0].Key : 0;
            string why = "longest run";
            if (forced.ContainsKey(contracts[k].Key)) { chosen = forced[contracts[k].Key]; why = "FORCED by --offsets"; }
            offsets[k] = chosen;
            int tc; total.TryGetValue(chosen, out tc);
            int rl; runs.TryGetValue(chosen, out rl);
            string runner = ranked.Count > 1 ? string.Format(Inv, "{0} (run {1:N0})", P(ranked[ranked[0].Key == chosen ? 1 : 0].Key), ranked[ranked[0].Key == chosen ? 1 : 0].Value) : "none";
            rep.AppendLine(string.Format(Inv, "{0,-8} ticks {1,12:N0}  raw bars {2,8:N0}  offset {3,9} [{4}]  exact minutes {5,8:N0}  longest run {6,8:N0}  next best: {7}",
                contracts[k].Key, n, bars.Count, P(chosen), why, tc, rl, runner));
        }

        // assign each file minute to the contract whose shifted bar matches OHLC exactly (earliest listed wins ties)
        var keys = file.Keys.OrderBy(x => x).ToArray();
        var assign = new short[keys.Length];
        int unmatched = 0, ties = 0, noTicks = 0;
        short prevOwner = -1;
        for (int i = 0; i < keys.Length; i++)
        {
            assign[i] = -1;
            var f = file[keys[i]];
            var hits = new List<short>();
            bool anyRaw = false;
            for (int k = 0; k < contracts.Count; k++)
            {
                Bar r; if (!raw[k].TryGetValue(keys[i], out r)) continue;
                anyRaw = true;
                long d = offsets[k];
                if (r.O + d == f.O && r.H + d == f.H && r.L + d == f.L && r.C + d == f.C) hits.Add((short)k);
            }
            if (hits.Count > 1) ties++;
            if (hits.Count > 0) { assign[i] = hits.Contains(prevOwner) ? prevOwner : hits[0]; prevOwner = assign[i]; }
            else if (anyRaw) unmatched++;
            else noTicks++;
        }

        rep.AppendLine();
        rep.AppendLine(string.Format(Inv, "file minutes: {0:N0}   matched exactly: {1:N0}   ticks exist but no exact match: {2:N0}   no ticks from any contract: {3:N0}   matched by >1 contract (tie -> neighbour's contract): {4:N0}",
            keys.Length, keys.Length - unmatched - noTicks, unmatched, noTicks, ties));
        // unmatched minutes that fall inside the covered span are the ones that matter
        long spanFrom = long.MaxValue, spanTo = long.MinValue;
        for (int i = 0; i < keys.Length; i++) if (assign[i] >= 0) { spanFrom = Math.Min(spanFrom, keys[i]); spanTo = Math.Max(spanTo, keys[i]); }
        var inside = new List<long>();
        for (int i = 0; i < keys.Length; i++) if (assign[i] < 0 && keys[i] >= spanFrom && keys[i] <= spanTo) inside.Add(keys[i]);
        rep.AppendLine(string.Format(Inv, "unmatched minutes inside the covered span: {0:N0} (these get NO ticks in a strict build)", inside.Count));
        foreach (var g in inside.GroupBy(t => new DateTime(t).Date).Take(30))
            rep.AppendLine(string.Format(Inv, "  {0:yyyy-MM-dd ddd}: {1} minutes, first {2:HH:mm}, last {3:HH:mm}", g.Key, g.Count(), new DateTime(g.First()), new DateTime(g.Last())));

        // segments: runs of the same contract, ignoring unmatched minutes inside a run
        var seg = new StringBuilder("contract,offset,first_bar_end,last_bar_end,minutes\n");
        rep.AppendLine();
        rep.AppendLine("Segments (contract runs in file order):");
        int start = -1; short cur = -2; int count = 0; long last = 0;
        Action flush = () =>
        {
            if (cur < 0) return;
            string line = string.Format(Inv, "{0},{1},{2:yyyy-MM-dd HH:mm},{3:yyyy-MM-dd HH:mm},{4}", contracts[cur].Key, P(offsets[cur]), new DateTime(keys[start]), new DateTime(last), count);
            seg.AppendLine(line); rep.AppendLine("  " + line.Replace(",", "  "));
        };
        for (int i = 0; i < keys.Length; i++)
        {
            if (assign[i] < 0) continue;
            if (assign[i] != cur) { flush(); cur = assign[i]; start = i; count = 0; }
            count++; last = keys[i];
        }
        flush();

        File.WriteAllText(Path.Combine(outDir, "report.txt"), rep.ToString());
        File.WriteAllText(Path.Combine(outDir, "segments.csv"), seg.ToString());
        var off = new StringBuilder("contract,offset_points,path\n");
        for (int k = 0; k < contracts.Count; k++) off.AppendLine(string.Format(Inv, "{0},{1},{2}", contracts[k].Key, P(offsets[k]), contracts[k].Value));
        File.WriteAllText(Path.Combine(outDir, "offsets.csv"), off.ToString());
        using (var w = new BinaryWriter(File.Create(Path.Combine(outDir, "assign.bin"))))
        {
            w.Write(keys.Length);
            for (int i = 0; i < keys.Length; i++) { w.Write(keys[i]); w.Write(assign[i]); }
            w.Write(contracts.Count);
            for (int k = 0; k < contracts.Count; k++) { w.Write(contracts[k].Key); w.Write(offsets[k]); }
        }
        Console.Write(rep.ToString());
    }

    // ---------- build ----------
    static void Build(string minuteFile, string contractsCsv, string outDir, string outTickFile)
    {
        var contracts = LoadContracts(contractsCsv);
        var owner = new Dictionary<long, short>();
        long[] offsets;
        using (var r = new BinaryReader(File.OpenRead(Path.Combine(outDir, "assign.bin"))))
        {
            int n = r.ReadInt32();
            for (int i = 0; i < n; i++) { long t = r.ReadInt64(); short a = r.ReadInt16(); if (a >= 0) owner[t] = a; }
            int nc = r.ReadInt32();
            offsets = new long[nc];
            for (int k = 0; k < nc; k++)
            {
                string name = r.ReadString(); offsets[k] = r.ReadInt64();
                if (k >= contracts.Count || contracts[k].Key != name) throw new InvalidOperationException("contracts.csv changed since measure");
            }
        }
        if (File.Exists(outTickFile)) throw new IOException("output exists, refusing to overwrite: " + outTickFile);

        // contracts are written one after another, so their owned minutes must not interleave
        var order = Enumerable.Range(0, contracts.Count)
            .Where(k => owner.Values.Contains((short)k))
            .OrderBy(k => owner.Where(x => x.Value == k).Min(x => x.Key)).ToList();
        long prev = long.MinValue, written = 0;
        using (var w = new StreamWriter(outTickFile, false, new UTF8Encoding(false), 1 << 20))
        {
            foreach (int k in order)
            {
                foreach (var kv in Ticks(contracts[k].Value))
                {
                    short o; if (!owner.TryGetValue(BarEnd(kv.Key), out o) || o != k) continue;
                    if (kv.Key < prev) throw new InvalidOperationException("ticks out of time order at " + new DateTime(kv.Key).ToString("s", Inv) + " (contract runs interleave)");
                    prev = kv.Key;
                    long p, v; TickFields(kv.Value, out p, out v);
                    var dt = new DateTime(kv.Key);
                    w.Write(dt.ToString("yyyyMMdd HHmmss", Inv)); w.Write(' ');
                    w.Write((kv.Key % TimeSpan.TicksPerSecond).ToString("0000000", Inv)); w.Write(';');
                    w.Write(P(p + offsets[k])); w.Write(';'); w.Write(v.ToString(Inv)); w.Write('\n');
                    written++;
                }
            }
        }
        Console.WriteLine(string.Format(Inv, "wrote {0:N0} ticks to {1}", written, outTickFile));
    }

    // ---------- verify ----------
    static int Verify(string minuteFile, string tickFile)
    {
        var file = LoadMinute(minuteFile);
        long n; var built = BarsFromTicks(tickFile, out n);
        long same = 0, priceDiff = 0, volDiff = 0, extra = 0;
        var samples = new List<string>();
        foreach (var kv in built)
        {
            Bar f; if (!file.TryGetValue(kv.Key, out f)) { extra++; continue; }
            var b = kv.Value;
            if (b.O == f.O && b.H == f.H && b.L == f.L && b.C == f.C) { same++; if (b.V != f.V) volDiff++; }
            else { priceDiff++; if (samples.Count < 20) samples.Add(string.Format(Inv, "  {0:yyyy-MM-dd HH:mm} file {1}/{2}/{3}/{4} ticks {5}/{6}/{7}/{8}", new DateTime(kv.Key), P(f.O), P(f.H), P(f.L), P(f.C), P(b.O), P(b.H), P(b.L), P(b.C))); }
        }
        long from = built.Count > 0 ? built.Keys.Min() : 0, to = built.Count > 0 ? built.Keys.Max() : 0;
        long missing = file.Keys.Count(k => k >= from && k <= to && !built.ContainsKey(k));
        Console.WriteLine(string.Format(Inv, "ticks {0:N0}  bars from ticks {1:N0}  span {2:yyyy-MM-dd HH:mm} .. {3:yyyy-MM-dd HH:mm}", n, built.Count, new DateTime(from), new DateTime(to)));
        Console.WriteLine(string.Format(Inv, "OHLC identical: {0:N0}  OHLC different: {1:N0}  (of identical, volume differs: {2:N0})", same, priceDiff, volDiff));
        Console.WriteLine(string.Format(Inv, "bars only in ticks: {0:N0}  minute-file bars inside the span with no ticks: {1:N0}", extra, missing));
        foreach (var s in samples) Console.WriteLine(s);
        return priceDiff == 0 && extra == 0 ? 0 : 3;
    }
}
