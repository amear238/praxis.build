# praxis-tickprep

This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C).
It doesn't touch NinjaTrader. It reads the tick files and the 1-min file and writes only to the output paths you give it.
Belongs in the Praxis.build repo; copied here 2026-11-02 because the repo wasn't reachable from the VM.

## Files
- `TickPrep.cs` / `TickPrep.exe` — the tool. The header of the `.cs` file documents it.
- `MakeSynth.cs` / `MakeSynth.exe` — self-test helper. It makes fake contract tick files from the 1-min file with known offsets.
- `nt-implied-offsets.csv` — expected offset for each contract, from NinjaTrader's NQ rollover table (copy of `NinjaTrader.sqlite`, read 2026-10-31).
  If the 1-min file is NinjaTrader's back-adjusted `NQ ##-##`, the offsets the tool measures should equal these.

## Use (after Amear approves and buys the data)
1. Write `contracts.csv`, one line per contract: `NQ 06-21,C:\path\to\portara\file.txt`. Use the same names as `nt-implied-offsets.csv`.
2. `TickPrep.exe measure "<1-min file>" contracts.csv <outDir> [--tz-in UTC] [--offsets nt-implied-offsets.csv]`
   This writes `report.txt`, `offsets.csv`, `segments.csv` and `assign.bin`.
   Check that the offsets match `nt-implied-offsets.csv`, and look at the unmatched minutes.
3. `TickPrep.exe build "<1-min file>" contracts.csv <outDir> "<out>\NQCONTROW 09-25.Last.txt"`
   The build is strict: it keeps only ticks from minutes present in the 1-min file and won't overwrite an existing output file.
4. `TickPrep.exe verify "<1-min file>" "<out>\NQCONTROW 09-25.Last.txt"`
   Every rebuilt bar must match the file (exit code 0).

Any import into NinjaTrader is a separate step, and it needs Amear's OK.

## Self-test result (2026-11-02)
- Test data: fake H21/M21/U21 contracts, 2021-03-07 to 2021-06-21. The window spans the DST change and the cut-short 2021-06-10 roll.
- Offsets recovered exactly: 3400 / 3390.25 / 3380.5.
- All 99,705 rebuilt bars matched the file, with none missing or extra.
- UTC-stamped input gave the same result as Eastern.

Rebuild from source with:
`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /optimize+ /out:TickPrep.exe TickPrep.cs`
