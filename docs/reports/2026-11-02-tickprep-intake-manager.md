# 2026-11-02 — tickprep intake — manager report

Unit `2026-11-02-tickprep-intake` · praxis-manager · base HEAD `cb1a9a5` (branch main) · report written 2026-11-02.
Evidence grades used: OBSERVED (seen in this session on this Mac) / INFERRED (reasoned, not checked) / REPORTED BY AMEAR / REPORTED BY the VM agent / REPORTED BY the master / UNVERIFIED.

## Task

Amear's brief, item 3, as relayed by the master (DECISION_LOG `2026-11-02T21:23:45Z`, WHO: praxis-master; dispatched `2026-11-02T21:38:24Z`), under R-VN3-2 (`docs/reports/2026-11-01-voice-session-notes-3.md` lines 14–16, which do not authorise a purchase, an import or a run). Bring `praxis-tickprep` into the repo at a proposed path. Add MANIFEST rows and the sha256 of every file. Log the `.exe` question in DECISIONS as Amear's call. Do not run the tool. Import nothing into NT8. Source of the files: `/Users/admin/Downloads/drive-download-20261102T213740Z-1-001/`. This is untrusted input, so it was only read, hashed and copied.

What this unit did: copied the four files to `tools/tickprep/` (a path this unit proposed), wrote `tools/tickprep/SHA256SUMS`, appended DECISIONS.md entry `D-2026-11-02-B` and six MANIFEST rows, and wrote this report. Nothing was staged. Nothing went into git history.

## Rubric criteria addressed

From `specs/SPEC_RUBRIC.md`, standing table, quoted verbatim in the brief:
- S1: every claim in a report has pasted command output, not a description of output.
- S2: no component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S5: no approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation.
- S8: no question that belongs to Amear is answered on his behalf.
- Brief-specific checks: the files are byte-identical to the download; nothing was executed, compiled or imported; no file was deleted; no code, template or config changed elsewhere; the F1–F4 text is untouched; the pre-existing staged set of 12 paths is unchanged.

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| W1 (`aa4660dce3f9371ab`) | BUILD | copy 4 files + SHA256SUMS; append D-2026-11-02-B; append 6 MANIFEST rows; captures to scratchpad `w1-captures.txt` | returned `Result: PASS`; manager re-ran every check (below), all reproduced |
| A1 (`a53f991d6e4036506`) | ADVERSARIAL | D-2026-11-02-B, all hashes, MANIFEST rows, side effects; given the artifacts and criteria only, not W1's reasoning | `VERDICT: FAIL`: 3 MAJOR, 7 MINOR (below) |
| F1 (`a39f8c0de0855faba`) | BUILD (fix) | apply manager-written exact-text replacements (scratchpad `fix1/fix1.py`, single-occurrence asserts, own-lines-only guard); verify every new citation | returned `Result: PASS`: 3 prefix cmps exit 0, all citations MATCH; flagged 1 residual wording overstatement in NEEDS AMEAR 6, fixed by the manager as a single-line Edit |
| A2 (`a7d63bdcc69dbb872`) | ADVERSARIAL | this report plus the post-fix entry; byte comparison of pasted blocks against their capture files | `VERDICT: FAIL`: 2 MAJOR, 7 MINOR; all addressed (see "Adversarial findings") |
| A3 | ADVERSARIAL (narrow) | re-check that every A2 fix holds in the live files | `VERDICT: PASS`: 9/9 fixes hold; 2 MINOR + 2 NIT, applied after its return |

## Process log

1. Baseline captured before any write: HEAD `cb1a9a5`; 12 staged paths (snapshot `scratchpad/staged.pre.txt`); `tools/` absent; DECISIONS.md 401 lines (HEAD 364, plus 37 from the other unit's D-2026-11-02-A); MANIFEST.md 190 lines. Pre-unit copies: `scratchpad/DECISIONS.pre.md` (sha256 `90f50d07…`), `scratchpad/MANIFEST.pre.md` (`1dbb812c…`). The scratchpad is machine-local at `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/` and is not in the repo.
2. The skeleton report was created first, so the stop gate always had a file of this unit's to grade.
3. The manager read the README, the headers and the CSV, and ran the two greps itself, before writing W1's brief.
4. W1 BUILD → manager re-run (Verification evidence §1–§3) → A1 ADVERSARIAL found 3 MAJOR + 7 MINOR → the manager checked A1's key claims itself (the case-insensitive "option C" search, the DECISION_LOG rows stamped `2026-11-02T21:23:45Z` / `21:36:22Z` / `21:38:24Z`, `TickPrep.cs` 205–218 and 353–358; pasted in §6) → the manager wrote exact replacement text → F1 applied and verified it → the manager made one single-line Edit (NEEDS AMEAR 6, "next best") → re-run (§4) → A2 ADVERSARIAL on this report found 2 MAJOR + 7 MINOR → the manager made three single-line Edits in D-2026-11-02-B (zip sentence, NEEDS AMEAR 5 and 9 grading) and reworded this report → final re-run (§4, §5, §6) → A3, a narrow re-check of the A2 fixes.
5. Observed mid-unit, not caused by this unit: `docs/reports/2026-11-01-voice-session-notes-3.md` changed at 16:53:12 local, after this unit started (16:40:03). It went from 27 to 47 lines and now carries R-VN3-3 to R-VN3-6 and an "Undecided / open" list (§4 `find -newer` output; `stat` below). Its line 42 lists the `.exe` question as Amear's call, the same as NEEDS AMEAR 1 here (§6). Neither this unit nor its workers wrote to it; each brief barred writes to `docs/reports/`. This is the manager's own claim and has no proof beyond the briefs. R-VN3-3..6 are now recorded at DECISION_LOG `2026-11-02T21:54:14Z` (WHO: amear) (§6). That row says notes-3 was rewritten by the voice agent, 27 → 47 lines. This unit did not file those rulings, and D-2026-11-02-B does not rely on them. Whether R-VN3-3 (proceed with the data's holes and gaps) bears on NEEDS AMEAR 9 is Amear's call.

See §6 for the `stat`, `wc -l` and ledger-row captures.

## Verification evidence

All blocks below are the manager's own re-runs, pasted from capture files and not edited. Notes on a block sit outside it.

### §1. Task 1: copy, cmp, hashes, SHA256SUMS (taken after W1 returned)

```
$ cmp "$D/MakeSynth.cs" tools/tickprep/MakeSynth.cs; echo exit=$?
exit=0
$ cmp "$D/README.md" tools/tickprep/README.md; echo exit=$?
exit=0
$ cmp "$D/TickPrep.cs" tools/tickprep/TickPrep.cs; echo exit=$?
exit=0
$ cmp "$D/nt-implied-offsets.csv" tools/tickprep/nt-implied-offsets.csv; echo exit=$?
exit=0
$ shasum -a 256 "$D"/* "$D.zip" tools/tickprep/*
398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001/MakeSynth.cs
81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001/README.md
104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001/TickPrep.cs
69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001/nt-implied-offsets.csv
78e386891faa7f32ddec3c2f330f24978ed394fed95a99fb6acffa6166fa09f2  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001.zip
398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507  tools/tickprep/MakeSynth.cs
81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5  tools/tickprep/README.md
5aca84487edd132089914674e6713699aa8184646d854a84b15d5fc9b7542b5f  tools/tickprep/SHA256SUMS
104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545  tools/tickprep/TickPrep.cs
69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9  tools/tickprep/nt-implied-offsets.csv
$ (cd tools/tickprep && cat SHA256SUMS && shasum -a 256 -c SHA256SUMS)
398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507  MakeSynth.cs
81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5  README.md
104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545  TickPrep.cs
69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9  nt-implied-offsets.csv
MakeSynth.cs: OK
README.md: OK
TickPrep.cs: OK
nt-implied-offsets.csv: OK
exit=0
$ git show HEAD:DECISIONS.md | wc -l; wc -l DECISIONS.md
     364
     478 DECISIONS.md
$ head -n 401 DECISIONS.md | cmp - $S/DECISIONS.pre.md; echo exit=$?
exit=0
$ git show HEAD:DECISIONS.md | cmp - <(head -n 364 DECISIONS.md); echo exit=$?
exit=0
$ shasum -a 256 $S/DECISIONS.pre.md $S/MANIFEST.pre.md   # pre-unit snapshots
90f50d075d8c455adc62212d542648d2ed8cb13d4552fb7dd040907e23ddbe93  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/DECISIONS.pre.md
1dbb812cfe35b69f95e9027771d4a4deb1b74f57f8838232e8e51d1c08cde247  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/MANIFEST.pre.md
$ head -n 190 MANIFEST.md | cmp - $S/MANIFEST.pre.md; echo exit=$?
exit=0
$ wc -l MANIFEST.md
     196 MANIFEST.md
$ git diff --cached --name-only | wc -l; git diff --cached --name-only | diff - $S/staged.pre.txt; echo exit=$?
      12
exit=0
$ git status --short tools/ DECISIONS.md MANIFEST.md
 M DECISIONS.md
 M MANIFEST.md
?? tools/
$ git status --short --untracked-files=all tools/
?? tools/tickprep/MakeSynth.cs
?? tools/tickprep/README.md
?? tools/tickprep/SHA256SUMS
?? tools/tickprep/TickPrep.cs
?? tools/tickprep/nt-implied-offsets.csv
$ git diff --numstat DECISIONS.md MANIFEST.md
114	0	DECISIONS.md
9	1	MANIFEST.md
$ ls -la tools/tickprep/
total 72
drwxr-xr-x@ 7 admin  staff    224 Nov  2 16:41 .
drwxr-xr-x@ 3 admin  staff     96 Nov  2 16:41 ..
-rw-rw-r--@ 1 admin  staff   3732 Nov  2 13:29 MakeSynth.cs
-rw-rw-r--@ 1 admin  staff   2219 Nov  2 13:29 README.md
-rw-r--r--@ 1 admin  staff    322 Nov  2 16:41 SHA256SUMS
-rw-rw-r--@ 1 admin  staff  18785 Nov  2 13:30 TickPrep.cs
-rw-rw-r--@ 1 admin  staff    645 Nov  2 13:29 nt-implied-offsets.csv
```

The four download-side hashes equal the full hashes quoted in the master's dispatch brief to this unit, character for character. The brief's text is REPORTED BY the master and not pasted here; DECISION_LOG `2026-11-02T21:38:24Z` carries only abbreviated forms (`398868cf…1507` etc.; pasted in §6, second block). `cmp` printed nothing and exited 0 four times, so the copies are byte-identical (OBSERVED). `cp -p` also carried over the macOS `com.apple.quarantine` / `com.apple.provenance` xattrs and the 13:29/13:30 mtimes (see `ls -l@` in §2b). git does not track either.

### §2. Tasks 2 and 3: read, don't run (repo copies; manager capture)

```
$ sed -n 1,21p TickPrep.cs | cat -n
     1	// TickPrep: match per-contract NQ tick files to a back-adjusted 1-minute file, then
     2	// write one adjusted tick file that reproduces those minute bars exactly.
     3	//
     4	// Commands
     5	//   measure <minuteFile> <contracts.csv> <outDir> [--tz-in Eastern|UTC]
     6	//       Builds 1-min bars from each contract's ticks, finds each contract's additive
     7	//       offset, and assigns every minute of <minuteFile> to the contract + offset that
     8	//       reproduces it. Writes report.txt, offsets.csv, segments.csv, assign.bin.
     9	//   build   <minuteFile> <contracts.csv> <outDir> <outTickFile> [--tz-in ...]
    10	//       Re-reads the ticks and writes only ticks whose minute is assigned to their
    11	//       contract, shifted by that contract's offset. Strict: ticks in minutes that are
    12	//       missing from <minuteFile> are NOT written (holes/gaps stay as they are).
    13	//   verify  <minuteFile> <tickFile>
    14	//       Rebuilds 1-min bars from <tickFile> and compares them with <minuteFile>.
    15	//
    16	// contracts.csv: name,path   (one line per contract, any order; '#' lines ignored)
    17	// Minute file: NinjaTrader minute format, bar END time stamps: yyyyMMdd HHmmss;o;h;l;c;v
    18	// Tick files:  NinjaTrader tick format: yyyyMMdd HHmmss[ fffffff];price;volume
    19	// All times are compared in the minute file's time zone (US Eastern for Praxis).
    20	// Read-only on inputs; writes only into <outDir> and <outTickFile>.
    21	using System;
$ sed -n 1,5p MakeSynth.cs | cat -n
     1	// Test helper: make fake per-contract tick files from a back-adjusted minute file.
     2	// Inside its active window a contract's bars = file bars - offset (exact match);
     3	// outside it (its overlap with neighbours) prices are 1 tick higher, so they must NOT match.
     4	// Usage: MakeSynth <minuteFile> <outDir> <utc:0|1>
     5	using System;
$ /usr/bin/grep -n -i "ninjatrader\|sqlite\|Documents\|AppData\|Registry\|Process\.\|Environment\.\|WebClient\|Http\|Socket\|Delete(\|Move(" TickPrep.cs MakeSynth.cs; echo exit=$?
TickPrep.cs:17:// Minute file: NinjaTrader minute format, bar END time stamps: yyyyMMdd HHmmss;o;h;l;c;v
TickPrep.cs:18:// Tick files:  NinjaTrader tick format: yyyyMMdd HHmmss[ fffffff];price;volume
exit=0
$ /usr/bin/grep -n "File\.\(Create\|Write\|Open\|AppendAll\|Copy\)\|new StreamWriter\|new FileStream\|Directory\.\|Path\.Combine\|File\.Exists" TickPrep.cs MakeSynth.cs
TickPrep.cs:177:        Directory.CreateDirectory(outDir);
TickPrep.cs:276:        File.WriteAllText(Path.Combine(outDir, "report.txt"), rep.ToString());
TickPrep.cs:277:        File.WriteAllText(Path.Combine(outDir, "segments.csv"), seg.ToString());
TickPrep.cs:280:        File.WriteAllText(Path.Combine(outDir, "offsets.csv"), off.ToString());
TickPrep.cs:281:        using (var w = new BinaryWriter(File.Create(Path.Combine(outDir, "assign.bin"))))
TickPrep.cs:297:        using (var r = new BinaryReader(File.OpenRead(Path.Combine(outDir, "assign.bin"))))
TickPrep.cs:309:        if (File.Exists(outTickFile)) throw new IOException("output exists, refusing to overwrite: " + outTickFile);
TickPrep.cs:316:        using (var w = new StreamWriter(outTickFile, false, new UTF8Encoding(false), 1 << 20))
MakeSynth.cs:35:            string path = Path.Combine(a[1], c.Item1 + ".Last.txt");
MakeSynth.cs:36:            using (var w = new StreamWriter(path, false, new UTF8Encoding(false)))
MakeSynth.cs:59:        File.WriteAllText(Path.Combine(a[1], "contracts.csv"), list.ToString());
$ /usr/bin/grep -n "DllImport\|extern \|Assembly\|Reflection\|unsafe\|Marshal\|System\.Net\|System\.Diagnostics\|Microsoft\.Win32" TickPrep.cs MakeSynth.cs; echo exit=$?
exit=1
$ /usr/bin/grep -n "^using" TickPrep.cs MakeSynth.cs
TickPrep.cs:21:using System;
TickPrep.cs:22:using System.Collections.Generic;
TickPrep.cs:23:using System.Globalization;
TickPrep.cs:24:using System.IO;
TickPrep.cs:25:using System.Linq;
TickPrep.cs:26:using System.Text;
MakeSynth.cs:5:using System;
MakeSynth.cs:6:using System.Collections.Generic;
MakeSynth.cs:7:using System.Globalization;
MakeSynth.cs:8:using System.IO;
MakeSynth.cs:9:using System.Text;
$ cat -n nt-implied-offsets.csv
     1	contract,offset_points,active_from_roll
     2	NQ 03-21,3335.5,2020-12-10
     3	NQ 06-21,3342.75,2021-03-11
     4	NQ 09-21,3353.75,2021-06-10
     5	NQ 12-21,3365,2021-09-09
     6	NQ 03-22,3364.5,2021-12-09
     7	NQ 06-22,3368.5,2022-03-10
     8	NQ 09-22,3333.75,2022-06-09
     9	NQ 12-22,3257.25,2022-09-08
    10	NQ 03-23,3146,2022-12-12
    11	NQ 06-23,3015.75,2023-03-13
    12	NQ 09-23,2839.25,2023-06-12
    13	NQ 12-23,2642,2023-09-11
    14	NQ 03-24,2432.25,2023-12-11
    15	NQ 06-24,2184.75,2024-03-11
    16	NQ 09-24,1924,2024-06-17
    17	NQ 12-24,1689,2024-09-16
    18	NQ 03-25,1403,2024-12-16
    19	NQ 06-25,1199.5,2025-03-17
    20	NQ 09-25,985,2025-06-16
    21	NQ 12-25,747.5,2025-09-15
    22	NQ 03-26,491,2025-12-15
    23	NQ 06-26,282.25,2026-03-16
    24	NQ 09-26,0,2026-06-12
$ file *
MakeSynth.cs:           ASCII text
README.md:              Unicode text, UTF-8 text
SHA256SUMS:             ASCII text
TickPrep.cs:            ASCII text
nt-implied-offsets.csv: CSV text
$ head -1 nt-implied-offsets.csv | od -c | head
0000000    c   o   n   t   r   a   c   t   ,   o   f   f   s   e   t   _
0000020    p   o   i   n   t   s   ,   a   c   t   i   v   e   _   f   r
0000040    o   m   _   r   o   l   l  \n                                
0000050
$ for f in *; do printf "%s CR=" $f; tr -cd "" < $f | wc -c; done
MakeSynth.cs CR=       0
README.md CR=       0
SHA256SUMS CR=       0
TickPrep.cs CR=       0
nt-implied-offsets.csv CR=       0
$ /usr/bin/grep -n -i "buy\|purchas\|portara\|import\|run\|running\|self-test" README.md
3:This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C).
9:- `MakeSynth.cs` / `MakeSynth.exe` — self-test helper. It makes fake contract tick files from the 1-min file with known offsets.
13:## Use (after Amear approves and buys the data)
14:1. Write `contracts.csv`, one line per contract: `NQ 06-21,C:\path\to\portara\file.txt`. Use the same names as `nt-implied-offsets.csv`.
23:Any import into NinjaTrader is a separate step, and it needs Amear's OK.
25:## Self-test result (2026-11-02)
$ /usr/bin/grep -n -i "buy\|purchas\|portara\|import\|run\|running" TickPrep.cs MakeSynth.cs | head -20; echo exit=$?
TickPrep.cs:193:            // the offset with the longest unbroken run of matching minutes (comparing only minutes
TickPrep.cs:211:            string why = "longest run";
TickPrep.cs:216:            string runner = ranked.Count > 1 ? string.Format(Inv, "{0} (run {1:N0})", P(ranked[ranked[0].Key == chosen ? 1 : 0].Key), ranked[ranked[0].Key == chosen ? 1 : 0].Value) : "none";
TickPrep.cs:217:            rep.AppendLine(string.Format(Inv, "{0,-8} ticks {1,12:N0}  raw bars {2,8:N0}  offset {3,9} [{4}]  exact minutes {5,8:N0}  longest run {6,8:N0}  next best: {7}",
TickPrep.cs:257:        // segments: runs of the same contract, ignoring unmatched minutes inside a run
exit=0
$ sed -n 19,23p MakeSynth.cs | cat -n
        // name, file start, file end, active start, active end (bar-end times, Eastern), offset
        var cs = new[] {
            Tuple.Create("NQ 03-21", from,                       new DateTime(2021,3,19,17,0,0), from,                        new DateTime(2021,3,10,18,0,0), 3400.00m),
            Tuple.Create("NQ 06-21", new DateTime(2021,3,7),     new DateTime(2021,6,18,17,0,0), new DateTime(2021,3,10,18,0,0), new DateTime(2021,6,10,12,0,0), 3390.25m),
            Tuple.Create("NQ 09-21", new DateTime(2021,6,1),     to,                             new DateTime(2021,6,10,12,0,0), to,                          3380.50m),
$ sed -n 32p README.md
`C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /optimize+ /out:TickPrep.exe TickPrep.cs`
```

Annotation, outside the block, not an edit of it: in the block above, three printed command lines are corrupted by zsh `echo`. In the CR-count loop, `"\r"` printed as a raw carriage return byte, so it looks like `tr -cd ""`. In the two `run\b` greps, `\b` printed as a 0x08 backspace byte. The block is pasted byte-for-byte, so those raw bytes are present in this file. The commands that ran were correct. §2b below re-captures both with `printf`, which does not interpret escapes.

### §2b. Clean re-capture (`printf` echo)

```
$ for f in *; do printf "%s CR=" $f; tr -cd "\r" < $f | wc -c; done
MakeSynth.cs CR=       0
README.md CR=       0
SHA256SUMS CR=       0
TickPrep.cs CR=       0
nt-implied-offsets.csv CR=       0
exit=0
$ /usr/bin/grep -n -i "buy\|purchas\|portara\|import\|\brun\b\|running\|self-test" README.md
3:This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C).
9:- `MakeSynth.cs` / `MakeSynth.exe` — self-test helper. It makes fake contract tick files from the 1-min file with known offsets.
13:## Use (after Amear approves and buys the data)
14:1. Write `contracts.csv`, one line per contract: `NQ 06-21,C:\path\to\portara\file.txt`. Use the same names as `nt-implied-offsets.csv`.
23:Any import into NinjaTrader is a separate step, and it needs Amear's OK.
25:## Self-test result (2026-11-02)
exit=0
$ /usr/bin/grep -n -i "buy\|purchas\|portara\|import" TickPrep.cs MakeSynth.cs
exit=1
$ ls -l@ . | head -20
total 72
-rw-rw-r--@ 1 admin  staff   3732 Nov  2 13:29 MakeSynth.cs
	com.apple.provenance	   11 
	com.apple.quarantine	   51 
-rw-rw-r--@ 1 admin  staff   2219 Nov  2 13:29 README.md
	com.apple.provenance	   11 
	com.apple.quarantine	   51 
-rw-r--r--@ 1 admin  staff    322 Nov  2 16:41 SHA256SUMS
	com.apple.provenance	   11 
-rw-rw-r--@ 1 admin  staff  18785 Nov  2 13:30 TickPrep.cs
	com.apple.provenance	   11 
	com.apple.quarantine	   51 
-rw-rw-r--@ 1 admin  staff    645 Nov  2 13:29 nt-implied-offsets.csv
	com.apple.provenance	   11 
	com.apple.quarantine	   51 
exit=0
```

**Header blocks.** `TickPrep.cs` lines 1–20 and `MakeSynth.cs` lines 1–4 are pasted in §2 (the first `using` lines are 21 and 5).

**The required grep, hit by hit (OBSERVED: exactly two hits, exit 0):**
- `TickPrep.cs:17`: a comment describing the input minute-file format ("NinjaTrader minute format"). It is not code and touches nothing.
- `TickPrep.cs:18`: a comment describing the tick-file format ("NinjaTrader tick format"). It is not code and touches nothing.
- `MakeSynth.cs`: no hits.

**Supplementary greps (OBSERVED).** Write calls appear only under `outDir` / `outTickFile` (TickPrep) and `a[1]` (MakeSynth). `TickPrep.cs:309` refuses to overwrite `outTickFile`. The `measure` outputs (`:276`–`:281`) and MakeSynth's outputs (`:36`, `:59`) have no such guard. `DllImport` / `extern` / Reflection / `System.Net` / `System.Diagnostics` / `Microsoft.Win32` get 0 hits (exit 1). The `using` lines are System, Collections.Generic, Globalization, IO, Linq and Text only.

**Grade of README line 4** (*"It doesn't touch NinjaTrader. It reads the tick files and the 1-min file and writes only to the output paths you give it."*): consistent with the source read. That is INFERRED, not tested. The greps match the listed patterns only. They do not prove that no other I/O path exists, and no compiled binary was examined because none exists here.

**CSV.** 24 lines (header + 23 contracts, NQ 03-21 … NQ 09-26), shown in full by `cat -n` in §2. `file` reports `CSV text` with no CRLF note. `od -c` shows the first line ends in `\n` only, with no `\r`. The CR count is 0 for all five files (§2b). The CSV has LF line endings (OBSERVED). Amear's report that the Desktop copy is 24 bytes larger "because of line endings" is REPORTED BY AMEAR. 24 lines × 1 CR = 24 bytes is consistent with CRLF→LF (INFERRED; the Desktop copy was not examined).

**Task 3: limit sentences.** Quoted with line numbers from the README grep in §2b and in D-2026-11-02-B §h (pasted in §5):
- README:3, Portara: *"This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C)."*
- README:13, buying and approval: *"## Use (after Amear approves and buys the data)"*
- README:14, Portara path in the usage example: *"`NQ 06-21,C:\path\to\portara\file.txt`"*
- README:23, import: *"Any import into NinjaTrader is a separate step, and it needs Amear's OK."*
- README:25–29, running: the self-test section, quoted in full in D-2026-11-02-B §h.
- The `.cs` sources have no buy/purchase/portara/import hits (§2b, exit 1). The "run" hits in TickPrep.cs (`:193`, `:211`, `:216`, `:217`, `:257`) are the algorithm's "longest run" of matching minutes, not runs of the tool.

**Has anything crossed an R-VN3-2 limit?** OBSERVED from the four files: nothing records a purchase, an NT8 import, or a run on purchased Portara data. The folder does record one run: the VM-side self-test (README:25–29). That is REPORTED BY the VM agent and not reproduced here. It used fake per-contract tick files generated from an unidentified 1-min file. Whether that counts as a "run" under R-VN3-2 is NEEDS AMEAR 3; it is not decided here. README:10 reports a read of "a copy of `NinjaTrader.sqlite`" on 2026-10-31 (REPORTED BY the VM agent). That is a read, not an import. This side did nothing that crosses a limit (manager's own claim; see "No process launched").

### §3. Task 5: MANIFEST type vocabulary (pre-unit snapshot) and full `git diff MANIFEST.md` (post-fix)

```
$ /usr/bin/grep -o "| [A-Z][a-z]* | [0-9] |" $S/MANIFEST.pre.md | sort | uniq -c | /usr/bin/grep -w "Source\|Data\|Docs\|Report"
   1 | Data | 0 |
   1 | Data | 1 |
   1 | Docs | 0 |
   1 | Docs | 1 |
  20 | Report | 0 |
  21 | Report | 1 |
  59 | Report | 2 |
   4 | Source | 2 |
   1 | Source | 3 |
exit=0
$ git diff MANIFEST.md
diff --git a/MANIFEST.md b/MANIFEST.md
index a57ec1d..2651ea6 100644
--- a/MANIFEST.md
+++ b/MANIFEST.md
@@ -161,7 +161,7 @@
 | /docs/reports/2026-10-31-7zq-m1-worker4-fix.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 fix sub-report (worker4): fixes the manager's defect list D1–D12 (built from the worker3 adversarial report's defects 1–11) in the two variants, the checklist and this draft. NOT authoritative; sub-report to the 7zq M1 manager report |
 | /docs/reports/2026-10-31-7zq-m1-worker5-readversarial.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M1 re-ADVERSARIAL sub-report (worker5) on the worker4 fixes; written after this draft. NOT authoritative; sub-report to the 7zq M1 manager report |
 | /docs/reports/2026-10-30-zyd-rulings-append.md | Report | 2 | 2026-10-30 | Praxis_build-zyd manager sub-report: appended the "Rulings 2026-10-30" block (R-F3-1/2/3, DECISION_LOG 2026-10-30T23:23:00Z) to D-2026-10-30-A in DECISIONS.md, append-only (prefix byte-identical, +7 lines); committed in 4ec75ea without a MANIFEST row — row owed per F3 audit minor M1 |
-| /ninjascript/PraxisLastHalfHourMomentum.cs | Source | 2 | 2026-10-31 | Praxis_build-7zq M2 new researched NQ intraday strategy (third file of D-2026-10-31-A): Baltussen, Da, Lammers & Martens (2021) JFE 142:377–403 last-half-hour momentum η(r_ROD). Signal on the first bar in [15:30, 15:59) of a weekday session (normally 15:30): long if Close(signal bar)/most recent prior 16:00-stamped close − 1 > 0, else short (incl. 0); market orders; entry fills at the next bar's open (normally 15:31); flatten on the 15:59 bar (LHFlat1559); IsExitOnSessionCloseStrategy backstop; LHStaleFlat safety exit (should never fire); at most one trade per session, none on Sat/Sun bars; input Contracts only; backtest-only, no live-signal path; compile-intended, not compiled on the Mac |
+| /ninjascript/PraxisLastHalfHourMomentum.cs | Source | 2 | 2026-10-31 | Praxis_build-7zq M2 new researched NQ intraday strategy (third file of D-2026-10-31-A): Baltussen, Da, Lammers & Martens (2021) JFE 142:377–403 last-half-hour momentum η(r_ROD). Signal on the first bar in [15:30, 15:59) of a weekday session (normally 15:30): long if Close(signal bar)/most recent prior 16:00-stamped close − 1 > 0, else short (incl. 0); market orders; entry fills at the next bar's open (normally 15:31); flatten on the 15:59 bar (LHFlat1559); IsExitOnSessionCloseStrategy backstop; LHStaleFlat safety exit (should never fire); at most one trade per session, none on Sat/Sun bars; input Contracts only; backtest-only, no live-signal path; compile-intended, not compiled on the Mac — RETIRED by R-VN3-1 (2026-11-02), kept as record |
 | /docs/reports/2026-10-31-7zq-m2-shortlist.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 researched shortlist of three non-Noise-Area NQ intraday strategies (#1 Baltussen et al. 2021 η(r_ROD), 15; #2 Tsai et al. 2019 TORB, 12; #3 Zarattini & Aziz 2023 ORB, 10), with rule sets, cited results, NQ 1-min mapping and NEEDS AMEAR; #1 built, Amear may swap |
 | /docs/reports/2026-10-31-7zq-m2-worker1-research.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 research sub-report (worker1): process log with commands and outputs behind the shortlist. NOT authoritative; sub-report to the 7zq M2 manager report |
 | /docs/reports/2026-10-31-7zq-m2-worker2-build.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 build sub-report (worker2, PraxisLastHalfHourMomentum.cs); written after this draft. NOT authoritative; sub-report to the 7zq M2 manager report |
@@ -186,3 +186,11 @@
 | /docs/reports/2026-11-01-voice-handoff-results-and-next-build.md | Report | 2 | 2026-11-01 | voice-agent handoff: three-strategy results, backtest options, build backlog (2026-11-01); praxis-master |
 | /docs/reports/2026-11-01-csv-analyses.md | Report | 2 | 2026-11-01 | CSV-only analyses of the four 2026-11-01 runs (P&L by year, top 5/10 winners removed, long vs short by year, drawdown profile, slippage arithmetic model at 3/4 ticks/side); facts and open questions only; ungraded at time of row |
 | /docs/reports/2026-11-01-csv-analyses-manager.md | Report | 2 | 2026-11-01 | Manager report for unit 2026-11-01-csv-analyses; ungraded at time of row |
+| /docs/reports/2026-11-01-voice-session-notes-3.md | Report | 2 | 2026-11-02 | Voice-session notes 3 (2026-11-02): rulings R-VN3-1 (LastHalfHourMomentum scrapped) and R-VN3-2 (prepare High fill-resolution backtest), written by the chat/voice agent. NOTE: untracked in git at the time of this row |
+| /docs/reports/2026-11-02-r-vn3-1-filing-manager.md | Report | 2 | 2026-11-02 | Manager report for unit 2026-11-02-r-vn3-1-filing (R-VN3-1 filing: DECISIONS D-2026-11-02-A, bead Praxis_build-afe, MANIFEST rows); ungraded at time of row |
+| /tools/tickprep/TickPrep.cs | Source | 2 | 2026-11-02 | praxis-tickprep tool source (measure/build/verify: match Portara per-contract NQ tick files to a back-adjusted 1-min file and write one adjusted tick file); sha256 104dc9d9135d; copied byte-identical from the Drive download 2026-11-02; VM original UNVERIFIED; not run; not compiled; .exe absent, see D-2026-11-02-B |
+| /tools/tickprep/MakeSynth.cs | Source | 2 | 2026-11-02 | praxis-tickprep self-test helper source (makes fake per-contract tick files from a 1-min file with known offsets); sha256 398868cfdfb1; copied byte-identical from the Drive download 2026-11-02; VM original UNVERIFIED; not run; not compiled; .exe absent, see D-2026-11-02-B |
+| /tools/tickprep/README.md | Docs | 2 | 2026-11-02 | praxis-tickprep README (purpose, use steps, VM self-test result, rebuild command), written by the VM agent; sha256 81534da86c2e; copied byte-identical from the Drive download 2026-11-02; VM original UNVERIFIED; not run |
+| /tools/tickprep/nt-implied-offsets.csv | Data | 2 | 2026-11-02 | expected per-contract NQ offsets from NinjaTrader's rollover table (VM agent's read of a copy of NinjaTrader.sqlite, 2026-10-31), LF line endings; sha256 69e1a00975cf; copied byte-identical from the Drive download 2026-11-02; VM original UNVERIFIED; not run; the VM Desktop copy differs by line endings (REPORTED BY AMEAR) |
+| /tools/tickprep/SHA256SUMS | Data | 2 | 2026-11-02 | sha256 manifest of the four files, generated in the repo 2026-11-02; not run; sha256 5aca84487edd |
+| /docs/reports/2026-11-02-tickprep-intake-manager.md | Report | 2 | 2026-11-02 | Manager report for unit 2026-11-02-tickprep-intake (praxis-tickprep source intake: tools/tickprep/, DECISIONS D-2026-11-02-B, MANIFEST rows); ungraded at time of row |
exit=0
```

The hunk at row 164 and the two rows for notes-3 and the r-vn3-1 report belong to the other unit. They were present before this unit started, and `head -n 190 MANIFEST.md | cmp - MANIFEST.pre.md` exits 0 (§4). This unit's six rows are the last six. The brief said "six-column format"; the table actually has 5 data columns (6 pipes), and the rows follow the table. For the README, `Docs` was used because it is the existing type name ("Doc" does not occur).

### §4. Task 4 prefix proof and Task 6 verification (final, after all fixes)

```
$ git show HEAD:DECISIONS.md | wc -l
     364
exit=0
$ wc -l $S/DECISIONS.pre.md DECISIONS.md MANIFEST.md
     401 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/DECISIONS.pre.md
     481 DECISIONS.md
     196 MANIFEST.md
    1078 total
exit=0
$ head -n 401 DECISIONS.md | cmp - $S/DECISIONS.pre.md
exit=0
$ git show HEAD:DECISIONS.md | cmp - <(head -n 364 DECISIONS.md)
exit=0
$ head -n 190 MANIFEST.md | cmp - $S/MANIFEST.pre.md
exit=0
$ tail -n 1 $S/DECISIONS.pre.md | cut -c1-80
3. Is `PraxisLastHalfHourMomentum` also out of the R-VN3-2 High fill-resolution 
exit=0
$ /usr/bin/grep -n "^## 2026-11-02 — D-2026-11-02-" DECISIONS.md
368:## 2026-11-02 — D-2026-11-02-A: R-VN3-1 — `PraxisLastHalfHourMomentum` RETIRED from the active candidate set (retire, not delete)
405:## 2026-11-02 — D-2026-11-02-B: R-VN3-2 — praxis-tickprep source intake into tools/tickprep/ (source only; not run; .exe absent)
exit=0
$ git diff -U0 HEAD -- specs/SPEC_RUBRIC.md | /usr/bin/grep -c "^[-+]#\{2,3\} F[1-4]"
0
exit=1
$ sed -n "17p;30p;45p;59p" specs/SPEC_RUBRIC.md
### F1 — Signal-path topology vs. circuit-breaker placement
### F2 — Session-flat time vs. breakers #4 and #5
### F3 — Backtest fill resolution vs. acquired data granularity
### F4 — MFFU automation compliance
exit=0
$ git diff --cached --name-only | wc -l
      12
exit=0
$ git diff --cached --name-only | diff - $S/staged.pre.txt
exit=0
$ git status --short tools/ DECISIONS.md MANIFEST.md
 M DECISIONS.md
 M MANIFEST.md
?? tools/
exit=0
$ git status --short --untracked-files=all tools/
?? tools/tickprep/MakeSynth.cs
?? tools/tickprep/README.md
?? tools/tickprep/SHA256SUMS
?? tools/tickprep/TickPrep.cs
?? tools/tickprep/nt-implied-offsets.csv
exit=0
$ git diff --numstat DECISIONS.md MANIFEST.md
117	0	DECISIONS.md
9	1	MANIFEST.md
exit=0
$ ls -la tools/tickprep/
total 72
drwxr-xr-x@ 7 admin  staff    224 Nov  2 16:41 .
drwxr-xr-x@ 3 admin  staff     96 Nov  2 16:41 ..
-rw-rw-r--@ 1 admin  staff   3732 Nov  2 13:29 MakeSynth.cs
-rw-rw-r--@ 1 admin  staff   2219 Nov  2 13:29 README.md
-rw-r--r--@ 1 admin  staff    322 Nov  2 16:41 SHA256SUMS
-rw-rw-r--@ 1 admin  staff  18785 Nov  2 13:30 TickPrep.cs
-rw-rw-r--@ 1 admin  staff    645 Nov  2 13:29 nt-implied-offsets.csv
exit=0
$ (cd tools/tickprep && shasum -a 256 -c SHA256SUMS)
MakeSynth.cs: OK
README.md: OK
TickPrep.cs: OK
nt-implied-offsets.csv: OK
exit=0
$ for n in 191 192 193 194; do printf "%s: " $n; sed -n ${n}p MANIFEST.md | /usr/bin/grep -c -F "copied byte-identical from the Drive download 2026-11-02; VM original UNVERIFIED; not run"; done
191: 1
192: 1
193: 1
194: 1
exit=0
$ find /Volumes/Sensidine/Praxis.build /Users/admin/Downloads/drive-download-20261102T213740Z-1-001 -newer $S/staged.pre.txt -type f -not -path "*/.git/*" -not -path "*/.beads/*" 2>/dev/null | /usr/bin/grep -v "/.claude/state/" | head -30
/Volumes/Sensidine/Praxis.build/DECISIONS.md
/Volumes/Sensidine/Praxis.build/MANIFEST.md
/Volumes/Sensidine/Praxis.build/DECISION_LOG.md
/Volumes/Sensidine/Praxis.build/DISPATCH_LOG.md
/Volumes/Sensidine/Praxis.build/tools/tickprep/SHA256SUMS
/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-01-voice-session-notes-3.md
/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-02-tickprep-intake-manager.md
exit=0
$ ls -la /Users/admin/Downloads/drive-download-20261102T213740Z-1-001/
total 64
drwx------@   6 admin  staff    192 Nov  2 16:37 .
drwx------@ 178 admin  staff   5696 Nov  2 16:37 ..
-rw-rw-r--@   1 admin  staff   3732 Nov  2 13:29 MakeSynth.cs
-rw-rw-r--@   1 admin  staff   2219 Nov  2 13:29 README.md
-rw-rw-r--@   1 admin  staff  18785 Nov  2 13:30 TickPrep.cs
-rw-rw-r--@   1 admin  staff    645 Nov  2 13:29 nt-implied-offsets.csv
exit=0
$ ls -t docs/reports/*.md | head -2
docs/reports/2026-11-02-tickprep-intake-manager.md
docs/reports/2026-11-01-voice-session-notes-3.md
exit=0
```

Baseline (pre-unit snapshots vs HEAD; this is the other unit's change, present before this unit started):

```
$ git diff --no-index --numstat $S/rpt/DECISIONS.head.md $S/DECISIONS.pre.md | cut -f1,2
37	0
exit=0
$ git diff --no-index --numstat $S/rpt/MANIFEST.head.md $S/MANIFEST.pre.md | cut -f1,2
3	1
exit=0
```

Notes on §4:
- The DECISIONS prefix holds against both baselines: HEAD's 364 lines, and the 401 lines present before this unit appended (the other unit's D-2026-11-02-A ends at line 401). Both `cmp` runs exit 0. This unit added 80 lines (402–481). numstat shows 117 = 37 (other unit) + 80 (this unit).
- MANIFEST numstat 9/1 = the other unit's 3/1 (2 new rows + 1 changed row, baseline block above), plus this unit's 6 rows.
- `find -newer`: DECISION_LOG.md and DISPATCH_LOG.md are master-owned and the dispatch hook writes them; this unit did not edit them. notes-3 is explained in Process log 5. The `tools/` copies do not appear because `cp -p` preserved their 13:29/13:30 mtimes. `specs/SPEC_RUBRIC.md` (mtime 11:50:39, before the unit) is not listed, so this unit did not modify it. Its F-header lines 17/30/45/59 are unchanged, and the working tree has no F-header diff against HEAD (count 0).
- The newest-report line at the end of §4 was captured before this report was written. This report is written last, so it becomes the newest file.

### §5. D-2026-11-02-B as it stands (post-fix), verbatim

```
$ sed -n "402,\$p" DECISIONS.md

---

## 2026-11-02 — D-2026-11-02-B: R-VN3-2 — praxis-tickprep source intake into tools/tickprep/ (source only; not run; .exe absent)

**Date:** 2026-11-02
**Status:** RECORDS AN INTAKE. This entry is NOT a ruling by Amear and authorises nothing. The intake was asked for in Amear's filing brief, recorded by the master at DECISION_LOG `2026-11-02T21:23:45Z` (WHO: praxis-master, "FILING BRIEF (four items)", item 3) and dispatched at DECISION_LOG `2026-11-02T21:38:24Z` (WHO: praxis-master); R-VN3-2 itself is DECISION_LOG `2026-11-02T21:23:45Z` (WHO: amear). None of these rows authorises a purchase, an NT8 import, a run, or adding the `.exe` files. Appended 2026-11-02 by praxis-manager, unit `2026-11-02-tickprep-intake`.
**Ruling it serves:** R-VN3-2 (`docs/reports/2026-11-01-voice-session-notes-3.md` line 16): *"It does not authorize a purchase, an import or a run."*

**Evidence grades used below:** OBSERVED (seen by this unit on this Mac, 2026-11-02) / INFERRED (reasoned, not checked) / REPORTED BY AMEAR / REPORTED BY the VM agent (the agent that wrote the tool on the Windows VM) / UNVERIFIED (not checked by anyone on record).

**a. Provenance chain:**
1. Windows VM, where an agent wrote the tool — REPORTED BY the VM agent (README line 5: *"Belongs in the Praxis.build repo; copied here 2026-11-02 because the repo wasn't reachable from the VM."*) and REPORTED BY AMEAR.
2. Google Drive folder id `1YaM4I3BKt_nNKWdUnOkj4kJzCeBEwLe_`, uploaded by an agent on Amear's side — REPORTED BY AMEAR. Not opened by this unit.
3. Downloaded to `~/Downloads/drive-download-20261102T213740Z-1-001/` — by Amear, REPORTED BY AMEAR (DECISION_LOG `2026-11-02T21:38:24Z`: *"it int he downloads"*). OBSERVED: the folder exists and holds exactly four files, `MakeSynth.cs` (3,732 bytes), `README.md` (2,219), `TickPrep.cs` (18,785), `nt-implied-offsets.csv` (645).
4. Copied by this unit (`cp -p`) to `tools/tickprep/` — OBSERVED: `cmp` of each download file against its repo copy printed nothing, exit 0, for all four.

**b. Hashes (sha256, OBSERVED, hashed in the repo 2026-11-02; each equals the download-side hash):**
- `tools/tickprep/MakeSynth.cs` — `398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507`
- `tools/tickprep/README.md` — `81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5`
- `tools/tickprep/TickPrep.cs` — `104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545`
- `tools/tickprep/nt-implied-offsets.csv` — `69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9`
- `tools/tickprep/SHA256SUMS` (generated in the repo by this unit from the four lines above, relative names; `shasum -a 256 -c SHA256SUMS` passes) — `5aca84487edd132089914674e6713699aa8184646d854a84b15d5fc9b7542b5f`
- Zip `~/Downloads/drive-download-20261102T213740Z-1-001.zip` — `78e386891faa7f32ddec3c2f330f24978ed394fed95a99fb6acffa6166fa09f2` (OBSERVED, re-hashed by this unit). The zip was not extracted to disk. Its member list (`unzip -l`: the same four names and sizes) and the sha256 of each member read to stdout (`unzip -p <zip> <member> | shasum -a 256`) equal the folder's four hashes above (OBSERVED, re-run by the manager 2026-11-02).

**c. VM-side originals — UNVERIFIED.** No VM-side hash of any of the four files is on record. The master's dispatch brief states they were never hashed on the VM; DECISION_LOG `2026-11-02T21:36:22Z` says the VM-side sha256 of the `.exe`s and of the original CSV *"are not obtainable here"*. Neither statement is verified by this unit. That the Mac copies equal the VM files cannot be shown from this side. The hashes of `TickPrep.exe` and `MakeSynth.exe` are unknown.

**d. Line endings of `nt-implied-offsets.csv`:**
- REPORTED BY AMEAR: the `.cs` sizes equal the VM copies; `nt-implied-offsets.csv` is *"24 bytes smaller than the Desktop copy because of line endings; the contents are the same"*.
- OBSERVED (repo copy): `file` prints `CSV text` (no CRLF terminators reported); `wc -l` prints 24; `wc -c` prints 645; the file contains 0 CR bytes (`tr -cd '\r' | wc -c` → 0).
- INFERRED (arithmetic only, the Desktop copy was not checked): 24 lines × 1 CR byte = 24 bytes, CONSISTENT with a CRLF→LF conversion somewhere between the VM Desktop and this Mac.
- Consequence: by Amear's own report the repo csv is NOT byte-identical to the VM Desktop copy. Its hash in (b) identifies the LF copy only.

**e. `.exe` status:** `TickPrep.exe` and `MakeSynth.exe` are ABSENT — OBSERVED (not in the download folder, not in the repo). Not uploaded — REPORTED BY AMEAR: retyping ~39,000 encoded characters by hand was judged unsafe. README line 8 and line 9 list both `.exe` files as part of the tool. README line 32 (verbatim, `sed -n 32p`):
`` `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /optimize+ /out:TickPrep.exe TickPrep.cs` ``
That is the only rebuild command in the README; it builds `TickPrep.exe` only. No command for `MakeSynth.exe` is given (OBSERVED from the README, 32 lines). Nothing was compiled by this unit.

**f. What the tool is for** — the author's description, REPORTED BY the VM agent; the summary of what the code does is INFERRED from a source read. NOT tested, not compiled, not run.
- README line 3: *"This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C)."*
- README line 4: *"It doesn't touch NinjaTrader. It reads the tick files and the 1-min file and writes only to the output paths you give it."*
- `TickPrep.cs` lines 1–2: *"TickPrep: match per-contract NQ tick files to a back-adjusted 1-minute file, then / write one adjusted tick file that reproduces those minute bars exactly."*
- `TickPrep.cs` lines 5, 9, 13 name three commands: `measure <minuteFile> <contracts.csv> <outDir> [--tz-in Eastern|UTC]`, `build   <minuteFile> <contracts.csv> <outDir> <outTickFile> [--tz-in ...]`, `verify  <minuteFile> <tickFile>`. Lines 6–8: measure *"finds each contract's additive / offset, and assigns every minute of <minuteFile> to the contract + offset that / reproduces it."* Lines 10–12: build is *"Strict: ticks in minutes that are / missing from <minuteFile> are NOT written (holes/gaps stay as they are)."* Line 14: verify *"Rebuilds 1-min bars from <tickFile> and compares them with <minuteFile>."*
- `TickPrep.cs` line 20: *"Read-only on inputs; writes only into <outDir> and <outTickFile>."*
- `MakeSynth.cs` line 1: *"Test helper: make fake per-contract tick files from a back-adjusted minute file."*

**g. NT-touch / write-path grading (greps run on the repo copies, OBSERVED):**
- `/usr/bin/grep -n -i "ninjatrader\|sqlite\|Documents\|AppData\|Registry\|Process\.\|Environment\.\|WebClient\|Http\|Socket\|Delete(\|Move(" TickPrep.cs MakeSynth.cs` → exactly two hits, `TickPrep.cs:17` and `TickPrep.cs:18`, both comments naming the NinjaTrader text format (*"Minute file: NinjaTrader minute format, ..."*, *"Tick files:  NinjaTrader tick format: ..."*).
- `/usr/bin/grep -n "File\.\(Create\|Write\|Open\|AppendAll\|Copy\)\|new StreamWriter\|new FileStream\|Directory\.\|Path\.Combine" TickPrep.cs MakeSynth.cs` → TickPrep: `:177` `Directory.CreateDirectory(outDir)`; `:276`, `:277`, `:280` `File.WriteAllText(Path.Combine(outDir, ...))` for report.txt, segments.csv, offsets.csv; `:281` `File.Create(Path.Combine(outDir, "assign.bin"))`; `:297` `File.OpenRead(... "assign.bin")` (a read); `:316` `new StreamWriter(outTickFile, false, ...)`. MakeSynth: `:35` `string path = Path.Combine(a[1], c.Item1 + ".Last.txt");` and `:36` `using (var w = new StreamWriter(path, false, new UTF8Encoding(false)))`; `:59` `File.WriteAllText(Path.Combine(a[1], "contracts.csv"), ...)`. Writes go only under `outDir` / `outTickFile` (TickPrep) and `a[1]` (MakeSynth).
- `TickPrep.cs:309`: *"if (File.Exists(outTickFile)) throw new IOException("output exists, refusing to overwrite: " + outTickFile);"* — the overwrite refusal covers `outTickFile` only. OBSERVED in source: the measure outputs in `outDir` (`:276`–`:281`) and MakeSynth's outputs (`:36`, `:59`) have no such guard.
- Grade of the README line-4 claim (*"It doesn't touch NinjaTrader ... writes only to the output paths you give it"*): consistent with the source read — INFERRED, not tested. The greps match listed patterns only; they do not prove that no other I/O API is used.
- README line 10: the offsets came from *"NinjaTrader's NQ rollover table (copy of `NinjaTrader.sqlite`, read 2026-10-31)"* — REPORTED BY the VM agent. A read of a copy, not an import. Not verifiable from here.

**h. R-VN3-2 limits — status:**
- README line 3: *"This tool prepares Portara per-contract NQ tick files for `NQCONTROW 09-25` (High fill resolution, option C)."*
- README line 13: *"## Use (after Amear approves and buys the data)"*
- README line 23: *"Any import into NinjaTrader is a separate step, and it needs Amear's OK."*
- README lines 25–29: *"## Self-test result (2026-11-02)"* / *"- Test data: fake H21/M21/U21 contracts, 2021-03-07 to 2021-06-21. The window spans the DST change and the cut-short 2021-06-10 roll."* / *"- Offsets recovered exactly: 3400 / 3390.25 / 3380.5."* / *"- All 99,705 rebuilt bars matched the file, with none missing or extra."* / *"- UTC-stamped input gave the same result as Eastern."*
- `TickPrep.cs` header (lines 1–20) does not mention Portara, buying data or importing into NT8 (OBSERVED).
- Status (OBSERVED from the four files): nothing in the folder records a purchase — README line 13 presupposes one *"after Amear approves and buys the data"*. Nothing records an NT8 import — README line 23 says that is a separate step needing Amear's OK. Nothing records a run on purchased Portara tick data. The one run the folder records is the VM-side self-test (next bullet), and its 1-min input file is not identified.
- The self-test (README lines 25–29) is a VM-side run — REPORTED BY the VM agent; not reproduced here. Per README line 26 the *contracts* (the per-contract tick files) were fake. Per README line 9 and `MakeSynth.cs` line 26 (`foreach (var line in File.ReadLines(a[0]))`, the minute file given on the command line) they were generated from "the 1-min file". Whether that minute file was real market data is UNVERIFIED (README line 11 ties the offsets to NinjaTrader's back-adjusted `NQ ##-##`). The offsets it reports (3400 / 3390.25 / 3380.5) match the constants hard-coded in `MakeSynth.cs` lines 21–23 (`3400.00m`, `3390.25m`, `3380.50m`; OBSERVED in source). That shows consistency, not that the run happened. The README does not say which 1-min file the self-test used (OBSERVED).
- R-VN3-2's text (notes-3 line 16): *"It does not authorize a purchase, an import or a run."* Whether the VM self-test counts as a "run" under that line is NOT for this entry to decide (NEEDS AMEAR 3).

**S6 cross-block — no block's spec changes:**
- **F1 — Signal-path topology** (`specs/SPEC_RUBRIC.md:17-28`): untouched. FROZEN.
- **F2 — Session-flat time vs breakers #4 and #5** (`specs/SPEC_RUBRIC.md:30-43`): untouched. FROZEN.
- **F3 — Backtest fill resolution** (`specs/SPEC_RUBRIC.md:45-57`): untouched. The void clause of D-2026-10-30-A stands.
- **F4 — MFFU automation compliance** (`specs/SPEC_RUBRIC.md:59-70`): untouched. FROZEN.
- No code, template or config changed; `tools/tickprep/` is new source, not built, not wired to anything.

**NEEDS AMEAR (questions only):**
1. `.exe` ruling: source only with the rebuild steps, or the binaries too? If binaries: how do they reach this repo (the hand-retyping route was judged unsafe), and who hashes them on the VM so the repo copy can be checked against the original?
2. Is the Portara data purchase that README line 13 presupposes authorised? (R-VN3-2 does not authorise a purchase.)
3. The VM-side self-test (README lines 25–29) ran the tool on synthetic tick files built from an unidentified 1-min file. Does it count as a "run" under R-VN3-2, and is its result accepted as reported or to be re-run under approval?
4. Should the VM-side originals (the four files and both `.exe`) be hashed on the VM to close the UNVERIFIED link in the provenance chain?
5. `nt-implied-offsets.csv`: is the LF repo copy the canonical one, given Amear reports that the Desktop/VM copy differs by line endings?
6. `--offsets` FORCES offsets. `TickPrep.cs` lines 45–55 parse it before the command switch (line 45: *"int fo = a.IndexOf("--offsets");   // optional CSV contract,offset_points to force offsets"*; line 52: *"forced[p[0].Trim()] = (long)(decimal.Parse(p[1], Inv) * 4m);"*). In measure, line 212: *"if (forced.ContainsKey(contracts[k].Key)) { chosen = forced[contracts[k].Key]; why = "FORCED by --offsets"; }"* — for every contract whose `contracts.csv` name equals a CSV `contract` value exactly (both sides `Trim()`med, lines 52 and 169; the `forced` dictionary at line 34 uses the default, case-sensitive comparer), the measured longest-run offset is replaced by the CSV value. A contract with no exact match keeps its measured offset; that is not an error, and its report.txt line shows `[longest run]` instead of `[FORCED by --offsets]` (INFERRED from the source read). That value is then used to assign minutes (line 236), written to `offsets.csv` (lines 278–280) and `assign.bin` (lines 281–286), which build reads (lines 297–305). README line 15 passes `[--offsets nt-implied-offsets.csv]` to `measure`; README line 17 says *"Check that the offsets match `nt-implied-offsets.csv`"*. With `--offsets`, the offsets written for listed contracts equal the CSV by construction (INFERRED from the source read); report.txt prints the exact-minute count and longest run for the chosen offset, i.e. the forced one when forcing applies; the measured winner then appears only as the "next best" entry, and only when more than one offset was measured — with one, "next best" prints `none` and the measured winner does not appear (lines 214–218). `--offsets` is not in the header's command list (lines 5, 9). Should `measure` be run with or without forced offsets when the time comes?
7. README line 3 says *"`NQCONTROW 09-25` (High fill resolution, option C)"*. Which option list is "option C" from? A case-insensitive search (`/usr/bin/grep -rn -i "option C" docs/reports/*.md`) finds three candidate meanings, none confirmed as the README's: `docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:175` *"Option C (measured haircut from a tick sample)"* (a fill-resolution option, in an UNGRADED report); `docs/reports/2026-07-15-b2-q1-strategy-exportability.md:42` *"Phase 3 spec Block 2 Option C"* (a data-sourcing option); and the Kinetick connection option C in `docs/reports/2026-10-20-a20-kinetick-research.md` (line 127, *"C. Connect at startup"*). The VM agent's R-VN3-2 plan file is absent from this Mac (DECISION_LOG `2026-11-02T21:38:24Z`). The label is unresolved here.
8. Which 1-min file is the input to `measure` / `build` / `verify`? README line 11 is conditional (*"If the 1-min file is NinjaTrader's back-adjusted `NQ ##-##`, the offsets the tool measures should equal these."*). And which 1-min file did the VM self-test use?
9. `verify` exits 0 when no price differs and no extra bars exist. Minute-file bars with no ticks are printed (`TickPrep.cs` line 355) but do not change the exit code (line 357: `return priceDiff == 0 && extra == 0 ? 0 : 3;`) — INFERRED from the source read; not compiled or run. How many unmatched or missing minutes are acceptable before the output is used?
10. Is `tools/tickprep/` the path Amear wants? The brief asked for a proposed path; this unit proposed it and copied the files there.
exit=0
```

### §6. Post-A1/A2 checks (zip members, notes-3 and ledger rows, TickPrep.cs excerpts)

In the block below, `$Z` is `/Users/admin/Downloads/drive-download-20261102T213740Z-1-001.zip` and `$S` is the scratchpad (both set in the same shell; not echoed).

```
$ unzip -l $Z
Archive:  /Users/admin/Downloads/drive-download-20261102T213740Z-1-001.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
     2219  11-02-2026 13:29   README.md
     3732  11-02-2026 13:29   MakeSynth.cs
    18785  11-02-2026 13:30   TickPrep.cs
      645  11-02-2026 13:29   nt-implied-offsets.csv
---------                     -------
    25381                     4 files
exit=0
$ for m in MakeSynth.cs README.md TickPrep.cs nt-implied-offsets.csv; do printf "%s " $m; unzip -p $Z $m | shasum -a 256; done
MakeSynth.cs 398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507  -
README.md 81534da86c2ecec38506a3a78ac2f1d283a7fa1ab15648b2f74930a10e95aeb5  -
TickPrep.cs 104dc9d9135d3e27cab2d35019606ca8f112d7586cdcbe98a32ee0e4d13e6545  -
nt-implied-offsets.csv 69e1a00975cf84c22d3918600b0912d1fc042a0d8f291e614d446fd8ee8220d9  -
exit=0
$ stat -f "%Sm %N" -t "%H:%M:%S" $S/staged.pre.txt docs/reports/2026-11-01-voice-session-notes-3.md DECISION_LOG.md specs/SPEC_RUBRIC.md
16:40:03 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/staged.pre.txt
16:53:12 docs/reports/2026-11-01-voice-session-notes-3.md
16:54:36 DECISION_LOG.md
11:50:39 specs/SPEC_RUBRIC.md
exit=0
$ wc -l docs/reports/2026-11-01-voice-session-notes-3.md
      47 docs/reports/2026-11-01-voice-session-notes-3.md
exit=0
$ /usr/bin/grep -n "praxis-tickprep" docs/reports/2026-11-01-voice-session-notes-3.md
42:- `praxis-tickprep` (from the VM agent): whether the two .exe files are committed, or only the source with rebuild steps, is Amear's call.
exit=0
$ /usr/bin/grep -n "2026-11-02T21:54:14Z" DECISION_LOG.md | cut -c1-200
463:- [2026-11-02T21:54:14Z] WHO: amear | WHAT: **RULINGS R-VN3-3 TO R-VN3-6 ENTERED — notes-3 rewritten by the voice agent (27 → 47 lines, mtime 16:53:12 local; lines 1–17 unchanged, so D-2026-
exit=0
$ /usr/bin/grep -n "^- \[2026-11-02T21:\(23:45\|36:22\|38:24\)Z\]" DECISION_LOG.md | cut -c1-110
465:- [2026-11-02T21:38:24Z] WHO: praxis-master | WHAT: **ITEM 3 DISPATCHED — unit `2026-11-02-tickprep-inta
466:- [2026-11-02T21:36:22Z] WHO: praxis-master | WHAT: **ITEMS 1+4 AUDIT DISPATCHED; ITEM 3 PARTLY UNBLOCKED 
467:- [2026-11-02T21:23:45Z] WHO: amear | WHAT: **RULINGS R-VN3-1 AND R-VN3-2 ENTERED — from `docs/reports/2
468:- [2026-11-02T21:23:45Z] WHO: praxis-master | WHAT: **FILING BRIEF (four items) — dispatch plan.** Amear
exit=0
$ sed -n 205,218p tools/tickprep/TickPrep.cs
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
exit=0
$ sed -n 353,358p tools/tickprep/TickPrep.cs
        Console.WriteLine(string.Format(Inv, "ticks {0:N0}  bars from ticks {1:N0}  span {2:yyyy-MM-dd HH:mm} .. {3:yyyy-MM-dd HH:mm}", n, built.Count, new DateTime(from), new DateTime(to)));
        Console.WriteLine(string.Format(Inv, "OHLC identical: {0:N0}  OHLC different: {1:N0}  (of identical, volume differs: {2:N0})", same, priceDiff, volDiff));
        Console.WriteLine(string.Format(Inv, "bars only in ticks: {0:N0}  minute-file bars inside the span with no ticks: {1:N0}", extra, missing));
        foreach (var s in samples) Console.WriteLine(s);
        return priceDiff == 0 && extra == 0 ? 0 : 3;
    }
exit=0
```

```
$ /usr/bin/grep -n "^- \[2026-11-02T21:38:24Z\]" DECISION_LOG.md | /usr/bin/grep -o "\`[0-9a-f]\{8\}…[0-9a-f]\{4\}\`"
`398868cf…1507`
`81534da8…aeb5`
`104dc9d9…6545`
`69e1a009…20d9`
exit=0
$ /usr/bin/grep -c "398868cfdfb10b0774606af7481066b3faf3ecdf7c984c644d19173b357a1507" DECISION_LOG.md
0
exit=1
```

### §7. Negative test: the checksum gate trips on a one-file change

A scratch copy of the five `tools/tickprep/` files was made in `$S/neg-tickprep/` (`$S` is the scratchpad). One CR+LF pair was appended to the copy's CSV, a two-byte line-ending change. It is smaller than the 24-byte difference Amear reports between the VM Desktop copy and this one. `shasum -c` must then fail for exactly that file, and the repo copy must still pass. Nothing in the repo was mutated.

```
$ cd $S/neg-tickprep && shasum -a 256 -c SHA256SUMS
MakeSynth.cs: OK
README.md: OK
TickPrep.cs: OK
nt-implied-offsets.csv: OK
exit=0
$ cd $S/neg-tickprep && printf "\r\n" >> nt-implied-offsets.csv && shasum -a 256 -c SHA256SUMS
MakeSynth.cs: OK
README.md: OK
TickPrep.cs: OK
nt-implied-offsets.csv: FAILED
shasum: WARNING: 1 computed checksum did NOT match
exit=1
$ cmp /Volumes/Sensidine/Praxis.build/tools/tickprep/nt-implied-offsets.csv $S/neg-tickprep/nt-implied-offsets.csv
cmp: EOF on /Volumes/Sensidine/Praxis.build/tools/tickprep/nt-implied-offsets.csv
exit=1
$ (cd /Volumes/Sensidine/Praxis.build/tools/tickprep && shasum -a 256 -c SHA256SUMS)
MakeSynth.cs: OK
README.md: OK
TickPrep.cs: OK
nt-implied-offsets.csv: OK
exit=0
```

## Adversarial findings

**A1** (ADVERSARIAL, given the artifacts and criteria only). Full log at `scratchpad/a1/a1-findings.txt`, 1,406 lines, machine-local. All 64-hex values in the entry and all 12-hex MANIFEST prefixes matched A1's own hashes. All four `cmp` runs exited 0. The three prefix cmps exited 0. Staged count stayed 12. Defects, each with its disposition:
- D1 MAJOR (S2), entry :427 *"The four files were never hashed on the VM."*, stated as fact without a record. **Fixed:** now "No VM-side hash … is on record". The master's statement and DECISION_LOG `21:36:22Z` *"are not obtainable here"* are both attributed, and neither is verified.
- D2 MAJOR (S2), :460, :461 and :474 called the self-test a run "on FAKE data". README:26 says only the contracts were fake; they were built from an unidentified 1-min file. **Fixed** at all three places.
- D3 MAJOR, :478: the "option C" search was case-sensitive and pointed Amear at the one irrelevant hit. **Fixed:** the case-insensitive search now lists three candidate meanings, none confirmed. The manager re-ran the search; F1 confirmed the list is complete for `docs/reports/*.md`.
- D4 MINOR: the MakeSynth `:35–:36` quote stitched two lines together. **Fixed:** each line is quoted separately.
- D5 MINOR: the required phrase in MANIFEST row 194 was broken. **Fixed:** the §4 phrase check gives 1 for each of rows 191–194.
- D6 MINOR: the Status line said no DECISION_LOG row was cited. **Fixed:** it now cites `21:23:45Z` (master filing brief, item 3), `21:38:24Z` (dispatch) and `21:23:45Z` (WHO: amear, R-VN3-2), and states that none of them authorises a purchase, an import, a run or adding the `.exe` files.
- D7 MINOR: "Downloaded by Amear … OBSERVED". **Fixed:** "by Amear" is now REPORTED BY AMEAR; the folder itself is OBSERVED.
- D8 MINOR: NEEDS AMEAR was missing which 1-min file is the input, the acceptable number of missing minutes (`verify` exit code, `:355`/`:357`), and confirmation of the path. **Fixed:** these were added as items 8, 9 and 10.
- D9 MINOR: item 6 was imprecise about `--offsets` matching and "next best". **Fixed:** exact, case-sensitive, trimmed matching (`:34`, `:52`, `:169`). With one measured offset, "next best" prints `none`; this follows F1's residual note and the manager's single-line Edit, with `:209–:216` pasted in §6.
- D10: this report was still a skeleton at the time. **Superseded** by this document.

**A2** (ADVERSARIAL on this report and the post-fix entry): Full log at `scratchpad/a2/a2-findings.txt` (machine-local). A2 found no break in: all four cmp, `shasum -c`, the three prefix cmps, the required NT grep, staged count 12 with `diff` exit 0, numstat 117/0 and 9/1, the MANIFEST phrase check, F1–F4 body diff, S5/S8, NEEDS AMEAR 1–10 matching between the report and the entry, and A1 fixes D1–D8 in the live files. Seven of nine pasted blocks were byte-identical to their capture files. Defects and dispositions:
- A2-1 MAJOR (S2): the entry (then line 425) and this report said the zip was "NOT opened", but A1 had run `unzip -l` and `unzip -p | shasum`. **Fixed:** the manager re-ran both (§6, OBSERVED: same four names and sizes, member hashes equal the folder's). The entry line was rewritten (single-line Edit), and the "No process launched" wording corrected.
- A2-2 MAJOR (S1, drift): this report said R-VN3-3..6 were not in the ledger, but DECISION_LOG `2026-11-02T21:54:14Z` (WHO: amear) records them. **Fixed:** Process log 5 and the note to the master now cite that row (§6).
- A2-3 MINOR: notes-3 line 45 should be line 42, and "27 to 47 lines" was unpasted. **Fixed:** §6 pastes `wc -l` and the line-42 grep.
- A2-4 MINOR: blocks were not byte-faithful (a CR became a line break during assembly), the corruption annotation said two lines where there were three, and the `stat` block had no capture file. **Fixed:** `rpt/build.py` now reads and writes with `newline=""`; the annotation now says three; the `stat` capture moved into §6 (`mgr-extra.txt`).
- A2-5 MINOR: "`:209–:216` shown above" was not pasted. **Fixed:** pasted in §6.
- A2-6 MINOR: the baseline MANIFEST 3/1 was mis-described as "3 added + 1 changed". **Fixed:** now "2 new rows + 1 changed row".
- A2-7 MINOR: `rpt/build.py` was not named as an interpreter run. **Fixed** in "No process launched".
- A2-8 MINOR: the DECISION_LOG row numbers had drifted, and "equal the master's hashes in the brief (OBSERVED)" pointed at an unpasted brief. **Fixed:** rows are cited by stamp, and the brief's hashes are graded REPORTED BY the master.
- A2-9 MINOR (S2): the `verify` exit-code behaviour was stated without a grade, and NEEDS AMEAR 5 stated the Desktop difference as fact. **Fixed:** "INFERRED from the source read; not compiled or run" was added in the entry (item 9), and the same grade in this report's NEEDS AMEAR 9, and item 5 now reads "given Amear reports that …" (single-line Edits).

**A3** (narrow ADVERSARIAL re-check of the A2 fixes): A3 (`a89f8a69390d29ec3`) returned `VERDICT: PASS` (its `Result:` line read "NO BREAK FOUND"). All nine A2 fixes HOLD in the live files. 9/9 pasted blocks matched their captures byte-for-byte. The three prefix cmps exit 0, staged count 12. Its log is at `scratchpad/a3/a3-findings.txt` (machine-local). It raised two new MINORs and two NITs, all applied after it returned and not re-checked by a further adversary. N1: the interpreter list in "No process launched" was incomplete; it now lists every script. N2: the DECISION_LOG abbreviated hashes were unpasted; they are now in §6, second block. NIT: the A2-9 quote did not match the entry's wording; now aligned. NIT: `$Z` was undefined; now defined above §6. Also added after A3: §7, the negative test.

## S6 cross-block check

This unit changes no block's spec. F1–F4 are all FROZEN; F3's void clause (D-2026-10-30-A) stands. The F-header lines are unchanged and `specs/SPEC_RUBRIC.md` was not modified by this unit (§4). `tools/tickprep/` is new, unbuilt source. Nothing in the repo calls it. Nothing in the signal path (n8n, NinjaScript, breakers) references it, and no code, template or config changed. D-2026-11-02-B carries the same F1/F2/F3/F4 lines as D-2026-11-02-A (§5). Potential cross-block reach, which is a NEEDS AMEAR question and not a change: the tool exists to prepare data for the F3 High-fill-resolution backtest. Using it on real data would need a purchase and a run that R-VN3-2 does not authorise.

## No process launched (manager's own claim; a negative cannot be proven by a command)

Nothing from the download folder or from `tools/tickprep/` was executed, compiled (`csc`, `mono`, `dotnet`) or imported by the manager. Every worker brief prohibited it. Python scripts run in this unit, all from the scratchpad:
- `fix1/fix1.py` (F1, `python3 -I`): input DECISIONS.md and MANIFEST.md only.
- `rpt/tplfix.py`, `rpt/tplfix2.py` and `rpt/build.py` (manager, `python3 -I`): input `rpt/tpl.txt` and the scratchpad capture files; `build.py` writes this report.
- Two stdin snippets (manager): `python3 -` without `-I`, which patched `rpt/build.py`, and `python3 -I -`, which patched `rpt/tplfix2.py` and `rpt/a2.txt`.
- `a2/blocks.py` and `a3/blocks.py` (A2 and A3, `python3 -I`, as reported by A3): they read this report and the capture files.

None of these reads the download folder or `tools/tickprep/`. The zip was not extracted to disk. A1 and the manager only listed it (`unzip -l`) and read its members to stdout to hash them (`unzip -p … | shasum -a 256`; §6). No `.exe` exists on this side (§1 `ls`). Grade: manager's claim, not verifiable by command.

## Files staged

This unit staged nothing, as the brief required: the pre-existing staged set must stay untouched. Its outputs are left in the working tree: `tools/tickprep/` (5 untracked files), DECISIONS.md lines 402–481 and MANIFEST.md rows 191–196 (unstaged modifications), and this report (untracked). Captured after the final edit:

```
$ git diff --cached --name-status
M	ISSUE_REGISTER.md
A	docs/reports/2026-08-06-session42-r8j-phase3-import.md
A	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
A	docs/reports/2026-08-07-session44-r8j-offset-correction.md
A	docs/reports/2026-10-28-f4-davi-reply-filing.md
A	docs/reports/2026-10-28-nightly-checks-plan-review-note.md
A	docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
A	docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
M	docs/specs/2026-08-08-ledger-compaction-spec.md
exit=0
$ git diff --cached --name-only -- tools DECISIONS.md MANIFEST.md docs/reports/2026-11-02-tickprep-intake-manager.md | wc -l
       0
exit=0
```

## NEEDS AMEAR (questions only; also in D-2026-11-02-B, numbered the same)

1. `.exe` ruling: source only with the rebuild steps, or the binaries too? If binaries, how do they reach this repo, and who hashes them on the VM?
2. Is the Portara data purchase presupposed by README:13 authorised? R-VN3-2 does not authorise a purchase.
3. Does the VM-side self-test (synthetic ticks from an unidentified 1-min file) count as a "run" under R-VN3-2? Is its result accepted as reported, or re-run under approval?
4. Should the VM-side originals (the four files and both `.exe`) be hashed on the VM, to close the UNVERIFIED link in the chain?
5. Is the LF repo copy of `nt-implied-offsets.csv` canonical?
6. Should `measure` be run with or without `--offsets` (forced offsets)?
7. Which option list is "option C" (README:3) from?
8. Which 1-min file is the input, and which did the self-test use?
9. How many unmatched or missing minutes are acceptable? (`verify`'s exit code ignores missing minutes; INFERRED from the source read, `TickPrep.cs:357`; not compiled or run.)
10. Is `tools/tickprep/` the path Amear wants?

Also for the master, not Amear: notes-3 grew mid-unit (Process log 5). Its R-VN3-3..6 are at DECISION_LOG `2026-11-02T21:54:14Z`. D-2026-11-02-B was written without them.

## Self-assessment per criterion (producer's own view; the auditor grades)

- S1: every factual claim points to a pasted block in §1–§5, or is labelled as a REPORTED or manager claim. Pointer: Verification evidence. Known limit: worker capture files are machine-local, so the claims rest on the manager's re-runs pasted here.
- S2: the self-test is REPORTED BY the VM agent; the README line-4 claim is INFERRED, not tested; the VM originals are UNVERIFIED; the tool is not compiled, not run, not tested. Pointer: §2b, §5 §c/§f/§g/§h, A1 D1/D2 fixes.
- S5: D-2026-11-02-B states that it is not a ruling and authorises nothing. It cites the ledger rows of the brief, and no approval is drawn from notes-3 or from chat. Pointer: §5 Status line.
- S8: ten questions are listed, none answered and none with a recommendation. Pointer: NEEDS AMEAR above and §5.
- Brief checks: byte-identical (§1 cmp ×4, `shasum -c`); nothing executed (manager's claim above); no deletion (only appends and adds; the numstat deletion column for DECISIONS is 0, and MANIFEST's single "1" is the other unit's row-164 change, a replace and not a delete, present before this unit); F1–F4 untouched (§4); staged set 12 = baseline (§4 `diff` exit 0).

**Result: PASS**
