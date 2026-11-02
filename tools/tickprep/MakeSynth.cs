// Test helper: make fake per-contract tick files from a back-adjusted minute file.
// Inside its active window a contract's bars = file bars - offset (exact match);
// outside it (its overlap with neighbours) prices are 1 tick higher, so they must NOT match.
// Usage: MakeSynth <minuteFile> <outDir> <utc:0|1>
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Text;

static class MakeSynth
{
    static readonly CultureInfo Inv = CultureInfo.InvariantCulture;
    static void Main(string[] a)
    {
        bool utc = a[2] == "1";
        var et = TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time");
        var from = new DateTime(2021, 3, 7); var to = new DateTime(2021, 6, 21);
        // name, file start, file end, active start, active end (bar-end times, Eastern), offset
        var cs = new[] {
            Tuple.Create("NQ 03-21", from,                       new DateTime(2021,3,19,17,0,0), from,                        new DateTime(2021,3,10,18,0,0), 3400.00m),
            Tuple.Create("NQ 06-21", new DateTime(2021,3,7),     new DateTime(2021,6,18,17,0,0), new DateTime(2021,3,10,18,0,0), new DateTime(2021,6,10,12,0,0), 3390.25m),
            Tuple.Create("NQ 09-21", new DateTime(2021,6,1),     to,                             new DateTime(2021,6,10,12,0,0), to,                          3380.50m),
        };
        var bars = new List<string[]>();
        foreach (var line in File.ReadLines(a[0]))
        {
            var t = DateTime.ParseExact(line.Substring(0, 15), "yyyyMMdd HHmmss", Inv);
            if (t <= from || t > to) continue;
            bars.Add(line.Split(';'));
        }
        var list = new StringBuilder();
        foreach (var c in cs)
        {
            string path = Path.Combine(a[1], c.Item1 + ".Last.txt");
            using (var w = new StreamWriter(path, false, new UTF8Encoding(false)))
            {
                int idx = 0;
                foreach (var b in bars)
                {
                    idx++;
                    var end = DateTime.ParseExact(b[0], "yyyyMMdd HHmmss", Inv);
                    if (end <= c.Item2 || end > c.Item3) continue;
                    bool active = end > c.Item4 && end <= c.Item5;
                    // outside its window the contract trades at a drifting spread: steady for
                    // stretches of ~30 minutes, then a tick or two different
                    decimal adj = c.Item6 - (active ? 0m : 0.25m * (1 + ((idx / 30) % 7)));
                    long v = long.Parse(b[5], Inv), v1 = Math.Max(1, v / 4);
                    // O, H, L, C at +1s, +15s, +30s, +59.5s inside (end-1min, end]
                    var start = end.AddMinutes(-1);
                    Tick(w, start.AddSeconds(1), decimal.Parse(b[1], Inv) - adj, v1, utc, et);
                    Tick(w, start.AddSeconds(15), decimal.Parse(b[2], Inv) - adj, v1, utc, et);
                    Tick(w, start.AddSeconds(30), decimal.Parse(b[3], Inv) - adj, v1, utc, et);
                    Tick(w, start.AddMilliseconds(59500), decimal.Parse(b[4], Inv) - adj, v - 3 * v1 > 0 ? v - 3 * v1 : 1, utc, et);
                }
            }
            list.AppendLine(c.Item1 + "," + path);
        }
        File.WriteAllText(Path.Combine(a[1], "contracts.csv"), list.ToString());
    }
    static void Tick(StreamWriter w, DateTime t, decimal p, long v, bool utc, TimeZoneInfo et)
    {
        if (utc) t = TimeZoneInfo.ConvertTimeToUtc(DateTime.SpecifyKind(t, DateTimeKind.Unspecified), et);
        w.Write(t.ToString("yyyyMMdd HHmmss", Inv) + " " + (t.Ticks % TimeSpan.TicksPerSecond).ToString("0000000", Inv) + ";" + p.ToString("0.##", Inv) + ";" + v.ToString(Inv) + "\n");
    }
}
