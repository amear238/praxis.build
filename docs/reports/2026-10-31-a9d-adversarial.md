# a9d adversarial (worker 3): break the Future-row research and the walkthrough

- **Unit:** `Praxis_build-a9d`, worker 3 of praxis-manager. **Mode:** ADVERSARIAL. **Date:** 2026-10-31.
- **Artifacts:** `docs/reports/2026-10-31-a9d-worker1-research.md` (1,270 lines as read) and `docs/reports/2026-10-31-a9d-walkthrough-future-row.md` (303 lines as read).
- **Criteria:** SPEC_RUBRIC S1, S2, S8, S9 (verbatim in the brief).
- **Discipline:** read-only throughout. The rescued sqlite was opened only with URI `file:...?mode=ro&immutable=1` via `python3 -I`. The `.bak_praxis*` files were not opened. There was no backtest, no replay and no trade simulation. No artifact, ledger, MANIFEST or memory file was edited. This file is the only one written. Scratch scripts are in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/w3/`.
- **Observer effect:** greps over `docs/` now also match the a9d files. That is expected and is not counted as a defect.

## Process log

1. I read both artifacts in full with `cat -n`.
2. I re-ran seven of the research's load-bearing evidence commands (minute listing, `NQCONT` count/first/last, the `NQCONT 09-25` count, the sqlite rows, the log↔trace pairing lines, the Config.xml merge line, the save-as-default greps). I also ran new probes: Config.xml record and connection keys, `od -c` on a real log file, exact `-T` mtimes, the 12-29 folders, a from-date tally of the trace requests, and a provider-download check on `NQ 09-26`.
3. I diffed the walkthrough's verbatim blocks against handoff lines 107-148.
4. I checked the MANIFEST diff (row count, columns, deletions, path existence).
5. I checked the walkthrough's cited sources (a20 results, a20 adversarial-1:65, walkthrough v2, seat-close:44, DECISION_LOG `14:59:37Z`, reference line ranges).

---

## Findings

### 1. BROKEN: walkthrough, Phase 1 and Phase 3 (lines 10, 73-114, 130-150). No guard keeps provider data out of the `NQCONT 09-25` folder while a data connection is up.

**Claim broken:** line 75 says "This phase **adds** a data folder; it deletes nothing and changes no instrument". Line 10 bans any step that alters a data folder without Amear's confirmation. But Phase 1 charts `NQCONT SEP25` (1.5) and Phase 3 runs the Analyzer on it, and no step reads or controls what the live connection writes into `db\minute\NQCONT 09-25\`. On the connected old install, every chart or Analyzer bars request went `(to Provider)`, and the provider's minute bars were written into the contract's own `db\minute\<name>\` folder. On Fusion the Simulated Data Feed is REPORTED connected (green). Two things are never read on Fusion: the save-live-data-as-historical setting, and each provider's symbol mapping for the Future `NQCONT`. If either resolves, provider or real-NQ minute bars land in the same folder that holds the back-adjusted import. The series is then mixed and silently differs from D-2026-07-17-A / D-2026-07-21-A. Step 1.4 lists that folder **before** 1.5 and Phase 3. Nothing re-lists it afterwards, so a write would never be seen.

**Evidence (pasted):**
```text
$ grep walkthrough for connect|feed|kinetick|simulated|provider|download   (only hits)
19:- Path: `Tools > Historical Data` (Ref §2). ... the reference names only the Import and Download sections ...
88:- STOP on any error line, ... `Unknown instrument` lines can come from a *provider* request ...
123:- **(b) `NQCONT ##-##`.** Expected **not** to help: Ref §6 says `##-##` requires provider support ...
286:3. NT8 reads on Fusion: its own time zone, Kinetick. ...   (Evidence block, not a step)

$ sed -n '20p' docs/reports/2026-10-20-a20-results.md        (Fusion, REPORTED by Amear)
Connections rows (name + dot colour, or no dot): Simulated Data Feed, green dot. Kinetick – End Of Day (Free), no dot. Playback, no dot. Simulation, no dot.

$ grep Config.xml (OLD install only)
18:      <ConnectOnStartup>true</ConnectOnStartup>
27:      <Provider>Simulator</Provider>
120:      <RecordForPlayback>false</RecordForPlayback>
121:      <SaveDataAsHistorical>false</SaveDataAsHistorical>

$ provider download on the connected old install, 2026-08-29: NQ 09-26 folder mtimes, last files, trace
  31 Jul 17 2026
   8 Aug 29 2026
   3 Jul 20 2026
20260827.Last.ncd
20260828.Last.ncd
2026-08-29 10:30:20:630 Cbi.Instrument.RequestBars (to Provider): instrument='NQ SEP26' from='8/23/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:28:27:137|1|2|Using HDS (hds-us-nt-016.ninjatrader.com/31655)
```
`SaveDataAsHistorical=false` and the provider symbol mapping are OBSERVED only on the old install, and only for the first. Neither is read on Fusion. Under S9 that is UNVERIFIED.

**Proposed replacement text.** Insert as step 0.8 and add re-reads:
> **0.8 Connections and live-data recording (read-only).**
> - Path: Control Center bottom-left connection status / `Connections` menu (Ref §1), then `Tools > Settings > Market data` (path UNVERIFIED; see 0.3).
> - Read back: every connection with its dot colour; the value of any setting about saving or recording live/real-time data as historical (label UNVERIFIED; on the old install the stored keys were `SaveDataAsHistorical` and `RecordForPlayback`, both `false`). In `Tools > Instruments`, Future `NQCONT`, Edit: any per-provider symbol-mapping fields, verbatim. Cancel.
> - Expect (INFERRED from the old install's Config.xml and 10-20 a20 results): only Simulated Data Feed connected; save-as-historical off; no provider mapping of `NQCONT` to a real symbol.
> - Falsifier: save-as-historical on; any connection besides Simulated Data Feed up; any mapping to `NQ` or another real root.
> - STOP on any falsifier. Do **not** disconnect anything or change the setting: that is Amear's decision, recorded separately (D-071 / a20 open item 1).
>
> Add to 1.5 and to 3.1 (after Run): "Re-list `db\minute\NQCONT 09-25\`. Read back the item count and the last file name. STOP if the count changed from 1.4, or if any file is dated after `20260720.Last.ncd`."

### 2. MAJOR: research Q2 item 7 (line 614). Its claim is contradicted by its own pasted Evidence B (S1/S2).

**Claim:** "After 11:26, the bare-`NQCONT` minute requests ask the provider only for `7/20/2026` to `8/28/2026`."
**Evidence (re-tallied from the same trace files the research pastes):**
```text
$ grep "instrument='NQCONT' from=" trace.20260829.0000{0,1}.txt | grep "1 Minute" | (time >= 11:26) | from-date | sort | uniq -c
   6 1/2/2026
   1 12/31/2025
  11 7/20/2026
   1 8/24/2026
```
8 of the 19 requests do not start at 7/20. The research's own block shows `11:33:54:114 ... instrument='NQCONT' from='1/2/2026'` and `11:59:19:301 ... from='12/31/2025'`.
**Proposed replacement text:** "After 11:26, 11 of the 19 bare-`NQCONT` 1-minute provider requests start at `7/20/2026`, the date of the last local file. The other 8 start at `1/2/2026` (6), `12/31/2025` (1) or `8/24/2026` (1) (OBSERVED, Evidence B). The 7/20 starts are consistent with NT8 already holding local bars up to that date (INFERRED, weak: the start date also varies with the requested range). So the error does not, on its own, prove that local bars are absent."

### 3. MAJOR: research Q2 item 1 (line 602) and walkthrough 1.5 (line 104). A pairing inferred from timing is graded OBSERVED (S2).

**Claim:** "**OBSERVED: the display form and the stored name are the same contract.**" The walkthrough repeats it as "OBSERVED pairing in old-install logs".
**What was actually observed:** a trace line naming `NQCONT SEP25` and a log line naming `NQCONT 09-25`, 128 ms apart. Nothing on disk states the mapping. The identity is an inference from co-timing, and all of Phase 1 rests on it (`NQCONT SEP25` reading the `NQCONT 09-25` folder).
```text
2026-08-29 10:00:22:727|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 09-25''
2026-08-29 10:00:22:599 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT SEP25' from='6/20/2026 12:00:00 AM' to='6/20/2026 12:00:00 AM' period='1 Minute'
2026-08-29 09:54:01:461|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT 12-29''
2026-08-29 09:54:01:419 Cbi.Instrument.RequestBars (to Provider): instrument='NQCONT DEC29' ...
2026-08-29 10:00:22 (ls -T)  db/minute/NQCONT 09-25 created
```
**Proposed replacement (research):** "**OBSERVED:** at 10:00:22 the trace names `NQCONT SEP25` and, 128 ms later, the log names `NQCONT 09-25`. At 09:54:01 the pair is `NQCONT DEC29` / `NQCONT 12-29`. The folder `db/minute/NQCONT 09-25/` was created at 10:00:22. **INFERRED (strong, from co-timing; no source states it):** the picker's `NQCONT SEP25` is `NQCONT 09-25` internally." **Walkthrough 1.5:** replace "OBSERVED pairing in old-install logs" with "INFERRED pairing from co-timed old-install log/trace lines, Q2 item 1".

### 4. MAJOR: walkthrough 3.2 (lines 173-177) and Phase 4 (line 196). A Stock-row run can still reach save-as-default.

Only the trade count and the L/S split carry a STOP ("→ STOP before Phase 4"). The slippage falsifier ("48.44 again (still the Stock row)") and the commission falsifier have **no STOP**, and Phase 4 states no precondition. A run with 1,211 trades, 584/627 and slippage 48.44 is exactly the Stock-row signature that this unit exists to remove. It would pass straight into 4.2 and be saved as the default, which is the trap R-VM-3 names.
```text
176:- **Total slippage 48.44 → 1,211.00**: run 4's 48.44 = 1,211 × 4 × 0.01 (Stock tick). Falsifier: 48.44 again (still the Stock row) or a value not a multiple of 1,211 × 0.25.
175:- **Commission unchanged**: per-trade template, independent of point value. Falsifier: any other value.
196:## Phase 4 — Save the settings as default
```
**Proposed replacement text:** at the end of 3.2: "**STOP before Phase 4** if total slippage reads 48.44 or any value that is not a multiple of 302.75 (= 1,211 × 0.25), if commission differs from $3,584.56, or if any 3.1 field read back differently. Do not open the template control." At the top of Phase 4: "**Precondition:** 3.1, 3.2 and 3.3 completed with no STOP. Otherwise do not touch the template control."

### 5. MAJOR: walkthrough line 9. It claims every step has all five parts. Seven steps do not (S2 on the document's own claim; brief item d).

Line 9: "Every step has: **Path** · **Read back** · **Expect** (graded) · **Falsifier** · **STOP**." As written:
- **0.3** (l.36): "Falsifier: any other value. Not a STOP; record it". No STOP.
- **0.7** (l.64-69): no Falsifier, no STOP.
- **1.3** (l.90-94): no Falsifier line.
- **3.1** (l.134-150): no Expect line and no Falsifier.
- **3.3** (l.180-192): no Expect, no Falsifier, no STOP.
- **4.1** (l.198-199): no Expect, no Falsifier, no STOP.
- **4.2** (l.201-205): no Expect, no Falsifier, no STOP.
```text
heuristic field count per step (R=Read back, E=Expect, F=Falsifier, S=STOP mentions; 0.3's S1 is the literal "Not a STOP"):
**0.3 Global merge policy.** | R1 E1 F1 S1
**0.7 Import dialog, current values (do  | R1 E1 F0 S1
**1.3 Instrument list after the import.* | R1 E1 F0 S1
**3.1 Settings.** Path: Strategy Analyze | R1 E0 F0 S1
**3.3 Further readbacks, verbatim from ` | R1 E0 F0 S0
**4.1 What the control offers.** Path: S | R0 E0 F0 S0
**4.2 Amear's choice (S8 — he decides) | R1 E0 F0 S0
```
**Proposed replacement text** (one line each):
- 0.3: "STOP: none. This value is a recorded input to 1.5 and is not a gate (stated exception to line 9)." Also amend line 9 to "…STOP, or a stated exception."
- 0.7: "Falsifier: none, this is an inventory. STOP if Amear cannot state the three original import settings at GATE 1. Phase 1 then does not start."
- 1.3: "Falsifier: a row count other than 2, or any row type/point value/tick that differs from 0.2."
- 3.1: "Expect: every field equals the table except Instrument = `NQCONT SEP25` (REPORTED table). Falsifier: any field differs on read-back."
- 3.3: "Expect: R1 exit names from {FlatEOD, XL, XS, Exit on session close} (INFERRED from `PraxisNoiseAreaBreakout.cs:211-290`). Falsifier: any other exit name, or any Qty > 1. STOP before Phase 4 on either."
- 4.1: "Expect: UNVERIFIED (Q5 item 3). Falsifier/STOP: no item that saves a default. Then stop, read the menu back, and return to Claude Code."
- 4.2: "Expect: a confirmation prompt or none (UNVERIFIED). STOP if any prompt mentions deleting, replacing or a trading-hours template."

### 6. MINOR: research Q1 item 4 versus item 6 (lines 24-32). The alternative owner of the bare folder is not ruled out explicitly.

Item 4 says the bare name "is the full name of the **Stock** row" and "none were ever filed under any of its contract names". Item 6 says no source says which master owns the folder. The one alternative left open is the Future master's `Expiry 1900-01-01` instrument row (`699839150770811`). If its full name were bare `NQCONT` rather than `NQCONT ##-##`, the Future would own the folder. The research has the argument that rules this out, but never makes it: the Analyzer offers exactly three entries (`NQCONT`, `NQCONT SEP25`, `NQCONT ##-##`, REPORTED) for exactly three `Instruments` rows (OBSERVED below). The Stock row's only row is 2099, so the 1900 row has to be `##-##`. The 0.01-tick slippage (48.44, REPORTED) then puts the bare-name Analyzer run on the Stock row.
```text
master 699839150754594 [(699839150770811, 23, 599266080000000000, ...594), (699839150770940, 23, 638922816000000000, ...594)]
master 699839150754605 [(699839150770941, 9, 662353632000000000, ...605)]
== the one type-1 master owning a 1900 row
(699839150754470, 'MHI', 1, 699839150764320, 599266080000000000)
```
**Proposed addition to Q1 item 4:** "The alternative, that the Future's 1900-01-01 row is named bare `NQCONT`, is ruled out INFERRED (moderate). Three picker entries (REPORTED) match three `Instruments` rows (OBSERVED), the Stock row's only row is 2099, and `##-##` is therefore the 1900 row. No source states the 1900 row's full name. The one type-1 master that owns a 1900 row is `MHI`, unrelated."

### 7. MINOR: research Q4 / walkthrough Phase 2(c). The research missed a datum that makes "deleting a row deletes its data" more likely.

`NQCONT DEC29` was requested at Daily period three times, and Daily requests do create `db/day/<name>` folders: `db/day/NQCONT 09-25` was created 11:34:21, the second of the SEP25 Daily request at 11:34:21:023. Yet no `*12-29*` folder exists anywhere in `db/`, and the sqlite no longer holds a 12-29 row. That is consistent with NT8 removing a contract's data folders when the contract row is removed (INFERRED; another cause cannot be excluded).
```text
2026-08-16 08:18:24:455 Cbi.Instrument.RequestBars (to Provi    [NQCONT DEC29 ... Daily]
2026-08-29 09:44:55:802 Cbi.Instrument.RequestBars (to Provi
2026-08-29 09:50:02:084 Cbi.Instrument.RequestBars (to Provi
(eval):1: no matches found: .../db/*/*12-29*
drwxr-xr-x@   2 admin  staff    64 Aug 29 11:34:21 2026 .    [db/day/NQCONT 09-25]
```
**Proposed addition to Q4 item 2 and Phase 2(c):** "Datum (INFERRED): `NQCONT 12-29` was requested at Daily period three times, yet no `12-29` folder survives and no 12-29 contract row remains. Removing a row or contract month may remove its data folders. Treat Stock-row removal, and any edit that removes a Future contract month, as a possible deletion of `db\minute\NQCONT\` or `db\minute\NQCONT 09-25\`."

### 8. MINOR: research line 11. The CRLF disclosure cites the wrong block and the wrong file (S1).

"The NT8 log and trace files are CRLF (see the `od -c` in Q1 evidence C)". That `od -c` is in **Q2** Evidence A, and it ran on `Install.xml` (the first `ls` entry), not on a log `.txt` or a trace file. Re-run: the log `.txt` is CRLF, so the claim holds for logs. The trace file's first 64 bytes contain no line end, so the claim is unshown for traces.
```text
ls -1 "$R/log/" | head -1
Install.xml
od -c log.20260829.00000.en.txt | head -4   ...   )  \r  \n   2   0   2
od -c trace.20260829.00000.txt | head -4    ...   *   *   * (no line end in first 64 bytes)
```
**Replacement:** "The NT8 log `.txt` files are CRLF (`od -c` of `log.20260829.00000.en.txt`). The trace files were not checked byte-wise. Every extract was piped through `tr -d '\r'` anyway."

### 9. MINOR: walkthrough 0.7 (line 68). It attributes the UTC default to Ref §2, which says nothing about it.

"Ref §2 / walkthrough v2 say the Time Zone box defaults to UTC." `grep -i UTC` on the reference returns nothing. The only source is `docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:163` ("the time zone box defaults to UTC").
**Replacement:** "(walkthrough v2:163 says the Time Zone box defaults to UTC; Ref §2 is silent)".

### 10. MINOR: walkthrough 1.2 (line 88) and 3.1 (line 150). The STOP rules conflict on `Unknown instrument`.

1.2 says "STOP on any error line" and also says `Unknown instrument` lines may be provider noise: "record them verbatim, do not interpret". The reader cannot tell whether to stop. 3.1 STOPs on any `unknown instrument` error after Run. On the old install such errors came with every provider request, including bare-`NQCONT` requests while local bars existed (Q2 item 7), so a good run may STOP. That is conservative, but it is undefined.
**Replacement (1.2):** "STOP on any error line, including `Unknown instrument`. Record it verbatim and return; Claude Code decides whether it is provider noise." **(3.1):** "After Run, if an `unknown instrument` line appears **and** the Analyzer produced results, record both. Do not STOP on the line alone. STOP only if no results were produced."

### 11. MINOR: walkthrough 1.5 (lines 105-111). The falsifier list has no catch-all, no 2026-blank case and no title expectation.

These cases are listed: equality, a constant offset, a different-minute shift, a blank 2021 chart. Not listed:
- (a) values that differ in some other way;
- (b) a blank or partial **2026-07** range, which is serving truncated at the 2025-09 expiry or the 2025-12-01 rollover;
- (c) a chart title that is not `NQCONT SEP25`, or a rollover prompt.

At the VM Amear has only the two file lines. So "equals a *different* minute" cannot be evaluated there, and a time-zone shift will look like "differs". Line 114 ("Only if 1.1-1.5 all pass") partly covers this, but the step itself does not say STOP.
**Replacement (append to the 1.5 falsifier list):** "Any other difference, a blank or partial 2026-07 range, a title other than `NQCONT SEP25`, or any rollover or contract prompt (click nothing; read it back) → **STOP**."

### 12. MINOR: research Q1 item 1 / Q6. The 11:43:45 mass rewrite is not examined, and it bears on walkthrough 1.2's Expect.

All 1,710 `.ncd` files carry mtime `Aug 29 11:43:45`, ten minutes **after** the sqlite's last write (11:33:53). There is no log or trace line about an import between 11:34:06 and 11:47:58.
```text
-rw-r--r--@ 1 admin staff 4505600 Aug 29 11:33:53 2026 .../db/NinjaTrader.sqlite
-rw-r--r--@ 1 admin staff    1529 Aug 29 11:43:45 2026 20210307.Last.ncd
(log, 11:35-11:49) 2026-08-29 11:47:58:561|0|4|Error on requesting bars series: 'Unknown instrument 'NQCONT''   [first log line after 11:34:06]
```
So on the old install, whatever wrote the folder (INFERRED: a re-import) left no Log line. Walkthrough 1.2's "Expect: … no error in the Log" is therefore not a success signal. **Replacement (1.2 Expect):** "A confirmation window (Ref §2). An empty Log is NOT evidence of success: on the old install the 11:43:45 write left no Log line. The success readback is 1.4."

### 13. MINOR: MANIFEST row for the voice notes. It cites labels the notes do not contain.

The row says the notes record "his typed rulings R-VM-1..5". The notes contain no `R-VM` string; the labels come from DECISION_LOG `2026-10-31T14:59:37Z`.
```text
$ grep -c 'R-VM' docs/reports/2026-10-31-voice-session-notes.md
0
```
**Replacement:** "…and his typed rulings 1-5 (labelled R-VM-1..5 in DECISION_LOG `2026-10-31T14:59:37Z`) (unaudited)…".

---

## Checks that held

**Re-run of the research's load-bearing commands. Output is identical to the pasted output, value for value:**
```text
drwxr-xr-x@ 1712 admin  staff  54784 Aug 29 11:43 NQCONT
drwxr-xr-x@    2 admin  staff     64 Aug 29 10:00 NQCONT 09-25
ls -1 NQCONT | wc -l      1710
head -1                    20210307.Last.ncd
tail -1                    20260720.Last.ncd
ls -1 "NQCONT 09-25" | wc -l      0
103:      <GlobalMergePolicy>MergeBackAdjusted</GlobalMergePolicy>
(699839150754594, 'NQCONT', 0, 20.0, 0.25, 3, 'CME US Index Futures RTH', -10200, 278)
(699839150754605, 'NQCONT', 1, 1.0, 0.01, 3, 'US Equities RTH', 1, 246)
(699839150754593, 'NQ', 1, 1.0, 0.01, 3, 'US Equities RTH', 1, 246)
master ...594 Instruments: 770811 (1900-01-01), 770940 (2025-09-01); master ...605: 770941 (2099-12-01)
max Instruments Id overall: 699839150770941
Future UserData first 64 bytes: 22 00 00 00 00 00 00 00 01 00 00 00 17 00 00 00 37 00 00 00 01 00 2d 00 ... (matches research hex row 0000-0020)
log/trace pairing lines 09:54:01 and 10:00:22: identical to research Q2 Evidence B
save-as-default greps: reference hits 150/156/213 only; docs-wide non-a9d hits = voice-notes:55, :56, run3-record:107, zyd-worker10:55 (same four the research pasted; extra hits are the a9d files themselves)
templates/StrategyAnalyzer/ on the rescued install: empty
```

**Verbatim copies in the walkthrough (diff against the handoff):**
```text
--- diff handoff 107-118 vs walkthrough 136-147     IDENTICAL-table
--- diff handoff 120-122 vs walkthrough 156-158     IDENTICAL-baseline
--- diff handoff 131 vs walkthrough 152             IDENTICAL-limitation
--- diff handoff 140-148 vs walkthrough 182-190     IDENTICAL-readbacks
```

**MANIFEST diff (`git diff -- MANIFEST.md`):**
```text
deleted lines (^-[^-]):   0
added rows:               6
columns per added row:    6 5        (all six rows have 5 columns)
staged MANIFEST changes:  0
ls: all present except /docs/reports/2026-10-31-a9d-adversarial.md (this file; exists once written)
```
Every added path starts with `/`.

**Other checks that held:**
- **S8, walkthrough.** GATE 1 (l.75) makes Amear state the import settings, and "Claude does not supply them" (l.69). Every Phase 2 option needs a separate written confirmation (l.120). 4.2 leaves the choice between overwrite and new name to Amear, and "Claude does not choose" (l.204). Merge policy is not changed in Phase 1 (l.112), which matches the 19:00 row's "deliberately NOT changed pending a ruling". No step decides anything that is Amear's.
- **S8, research.** Q2 item 5 and Q4 item 2 leave DoNotMerge and Stock-row removal to Amear.
- **F2.** No step edits or saves a trading-hours template. 0.6, 1.5 and 3.1 only *select* `CME US Index Futures RTH`.
- **Deletion.** No step deletes an instrument, folder, file or template. 1.1 copies the import file and never renames the original. 0.1 says "Do not click any Delete control". Phase 2(c) says "Never delete the `db\minute\NQCONT\` folder".
- **Back-adjustment offset detection (1.5).** The 2021-03-08 bar sits before the 2025-12-01 rollover, so an offset applied only to pre-rollover bars would show in the 2021 bar ("same constant added to all four of O/H/L/C"). Storage truncation is caught by the 1.4 count.
- **Time-zone check.** Fusion NT8 is "UTC-05:00 Eastern Time US and Canada" (a20 results:19, REPORTED). The winter bar 2021-03-08 10:00 EST therefore discriminates a fixed-UTC−4 or UTC import, which the summer 2026-07-17 bar cannot. The walkthrough chose the right bar.
- **Arithmetic.** 1,211 × 2.96 = 3,584.56. 1,211 × 4 × 0.01 = 48.44. 1,211 × 4 × 0.25 = 1,211.00. 4 × 0.25 × 20 = 20.
- **Reference line ranges.** §2 runs from l.91 to l.123 and §6 from l.180 to l.194.
- **Ruling row.** DECISION_LOG `14:59:37Z` contains the Stock/Future readback values that 0.2 cites as its Expect.
- **Shell traps.** Neither file contains `"$#`. `comm -3 <(...)` ran under `bash -v`. The `<script>` placeholder in research l.7 is a template, not a command.
- **Q2 item 4, Q3, Q5 grading.** Merge-policy semantics are INFERRED or SPEC-SILENT, expiry filtering is SPEC-SILENT, and the save-as-default label is UNVERIFIED. None is graded above its source.

**Not tested:**
- Whether NT8 actually writes Sim-feed or provider data into `NQCONT 09-25`. Finding 1 rests on the old install's observed download behaviour plus the missing guard, not on a Fusion observation.
- Whether a rollover prompt appears when charting an expired contract (UNVERIFIED).

Result: FAIL — 1 BROKEN, 4 MAJOR
