# Praxis_build-a9d — walkthrough: load 1-minute history onto the Future `NQCONT` row, re-baseline 0-S, save as default

> Revised 2026-10-31 by a9d worker 4 after the adversarial review (findings 1-13) in `docs/reports/2026-10-31-a9d-adversarial.md`. New: step 0.8 (connections, read-only), folder re-lists in 1.5 and 3.4, STOPs added in 0.3, 0.7, 3.2, 3.3, 4.1, 4.2, a Phase 4 precondition, and the missing step parts filled in. No STOP was softened; grades were only lowered.

**Pre-registered walkthrough — NOT a backtest report. F3 stays FROZEN until a backtest report carries the limitation sentence.**

- Unit: `Praxis_build-a9d`, worker 2 (BUILD, documentation). Date: 2026-10-31. Ungraded.
- Ruling it serves: DECISION_LOG `2026-10-31T14:59:37Z` (Amear): Future row only; load the 1-minute history; run 0-S on it as the new baseline; save the Analyzer settings as default.
- Amear performs every step by hand at the Fusion VM. Claude cannot see or touch the VM. **Fusion itself has never been read by Claude: every expectation about Fusion below is INFERRED** unless it is marked REPORTED (Amear said it) or OBSERVED (Claude read it on the Mac or on the rescued old install).
- Research cited as "Q1".."Q6" / "Open n" = `docs/reports/2026-10-31-a9d-worker1-research.md` (sections Q1-Q6, Open / UNVERIFIED list). "Ref §2 / §6" = `docs/reference/2026-07-24-nt8-windows-reference.md` (Import, lines 91-123; continuous/merge, lines 180-194).
- Every step has: **Path** · **Read back** (verbatim, spoken or typed) · **Expect** (graded) · **Falsifier** · **STOP**. On any STOP: do nothing further, read back what is on screen, and return to Claude Code. A STOP is a result, not a failure.
- Standing prohibitions for the whole document: no deletion of any instrument, data folder, file or template unless a separate, explicitly confirmed Amear step says so (none in Phases 0, 1, 3). **No change to any trading-hours template (F2 FROZEN)** — this walkthrough only *reads* a Trading hours field and *selects* `CME US Index Futures RTH`. Never rename or move the original import file.

---

## Phase 0 — Inventory (read-only; changes nothing)

Close every dialog in this phase with Cancel / the window X, never with OK or Save (button labels UNVERIFIED — if the only way out is a save button, STOP and say what the buttons read).

**0.1 Historical Data, what is loaded.**
- Path: `Tools > Historical Data` (Ref §2). The section that lists stored data (in research called `Loaded`) is **UNVERIFIED** — the reference names only the Import and Download sections. Read back the section names you see, then open whichever lists stored instruments.
- Read back: every instrument name listed under minute / Last; for `NQCONT` and for anything named `NQCONT 09-25` or `NQCONT SEP25`: first date, last date, and bar count if shown.
- Expect (INFERRED from Q1/Q6, old install): `NQCONT` from 2021-03-07 to 2026-07-20; nothing under `NQCONT 09-25` / `NQCONT SEP25`.
- Falsifier: minute data already present for `NQCONT 09-25`.
- STOP if data already exists under `NQCONT 09-25` (the premise of Phase 1 is wrong). Do not click any Delete control.

**0.2 Both instrument rows, full property sheets.**
- Path: `Tools > Instruments`, filter `NQCONT`; select each row → **Edit** (Ref §6) → read → Cancel.
- Read back, for EACH row: how many `NQCONT` rows the list shows; type; point value; tick size; Trading hours field; **Merge policy** (Ref §6 options: MergeBackAdjusted / MergeNonBackAdjusted / DoNotMerge / UseGlobalSetting); the contract months / rollover table, every row (expiry, rollover date); description and exchange if shown.
- Expect (REPORTED by Amear, DECISION_LOG `2026-10-31T14:59:37Z`): two rows. Stock: point value 1, tick 0.01, `US Equities RTH`, 0 rollovers. Future: point value 20, tick 0.25, `CME US Index Futures RTH`, one rollover (`NQCONT SEP25`). Merge policy on Fusion: unknown. On the old install it is REPORTED twice with conflicting values (`Use Global Setting`, then `Do not merge`) (Q2 item 4, Open 12). Future rollover row INFERRED as expiry 09-25, rollover 2025-12-01 (Q1 item 3, blob decode).
- Falsifier: a third `NQCONT` row; a different point value / tick on either row.
- STOP if the row count is not two, or if the Future row's Trading hours field is not `CME US Index Futures RTH`.

**0.3 Global merge policy.**
- Path: `Tools > Options > Market Data > Merge policy` (Ref §6). In this NT8 build the window may be titled "Settings" with a "Market data" category (recorded in `docs/reports/2026-10-20-a20-adversarial-1.md:65`); exact path on Fusion UNVERIFIED.
- Read back: the merge policy value, verbatim. Close without saving.
- Expect (INFERRED): `MergeBackAdjusted` — OBSERVED on the old install's `Config.xml` (Q6 evidence); Fusion unread.
- Falsifier: any other value. A different one of the four Ref §6 values is recorded as an input to 1.5 and Phase 1 does not change it.
- STOP if the value is not one of the four Ref §6 options (MergeBackAdjusted / MergeNonBackAdjusted / DoNotMerge / UseGlobalSetting), if no merge policy field can be found, or if the window can only be closed with a save button.

**0.4 Data folders on disk.**
- Path: Windows Explorer → `Documents\NinjaTrader 8\db\minute\`.
- Read back: every folder name; for `NQCONT`: file count (Explorer status bar "N items"), first and last file name; whether `NQCONT 09-25` exists and its item count.
- Expect (INFERRED from Q1/Q6, old install): `NQCONT` ≈ 1,710 files, `20210307.Last.ncd` … `20260720.Last.ncd`, ≈ 16-19 MB; `NQCONT 09-25` empty or absent.
- Falsifier: `NQCONT` count far from 1,710, or `NQCONT 09-25` non-empty.
- STOP if `NQCONT 09-25` already holds files.

**0.5 Import file on the VM.**
- Path: Explorer → the folder holding `NQCONT.Last.txt` on Fusion (location on Fusion UNVERIFIED; on the old install it was `C:\Mac\Home\praxis-signals\b2-data\`, session-52 walkthrough v2). Turn on file name extensions (Windows 11: `View > Show > File name extensions`, UNVERIFIED) so `.txt` is visible.
- Read back: full path; exact file name; size in bytes (right-click → Properties). Optional: Command Prompt `certutil -hashfile "<full path>" SHA256`, read the hash.
- Expect: 95,900,139 bytes and the SHA-256 in Evidence (OBSERVED on the Mac copy; the VM copy is INFERRED to be the same file).
- Falsifier: different size or hash.
- STOP if the size or hash differs — Phase 1 would import a different series.

**0.6 Read-only chart baseline on plain `NQCONT` (Stock row).**
- Path: new 1-minute chart of `NQCONT` (menu path UNVERIFIED — use the way you opened the 10-28 chart), Data Series: Last, Minute 1, Trading hours `CME US Index Futures RTH`, custom range 2021-03-08 → 2021-03-12; then 2026-07-17 → 2026-07-17. Read OHLC by hovering / the Data Box (control UNVERIFIED).
- Read back: Open, High, Low, Close of the bar stamped **2021-03-08 10:00** and of the bar stamped **2026-07-17 09:31**.
- Expect: equal to the two file lines in Evidence (spot-check bars below). The 2026-07-17 09:31 Open 28605.25 is REPORTED as already matching (10-28 notes, 2026-10-30 bar-time check). The 2021 bar is INFERRED.
- Falsifier: any value differs.
- STOP if they differ: the Stock row's data then does not equal the file, and the Phase 1 comparison has no baseline.

**Spot-check bars (copied from Evidence; the file is end-stamped ET, `date HHMMSS;Open;High;Low;Close;Volume`):**
- 2021-03-08 10:00 (EST, before the 2021-03-14 DST change): `20210308 100000;15968.75;15976.5;15962;15976.5;8` (file line 649)
- 2026-07-17 09:31 (EDT, first RTH bar): `20260717 093100;28605.25;28659;28599.5;28644.25;4963` (file line 1855934)
- Observed, not interpreted: the 2021 bar's volume is 8.

**0.7 Import dialog, current values (do NOT click Import).**
- Path: `Tools > Historical Data` → **Import** accordion section (Ref §2).
- Read back verbatim: Format; Data Type; Time Zone of Imported Data.
- **The import settings used for the existing Fusion `NQCONT` data are NOT on disk.** `docs/reports/2026-10-28-voice-session-notes.md` records no Format / Data Type / Time Zone (Evidence grep). The only on-disk import settings are the old-install instructions in `docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:140-145` — Format `NinjaTrader (end of bar timestamps)`, Data Type `Last`, Time Zone of Imported Data `US Eastern` — plus the REPORTED line "NQCONT was imported as ET" (`docs/reports/2026-10-20-seat-close-handover.md:44`, old install). The 2026-10-30 bar-time PASS (bar times match the file, no hour shift) is consistent with `US Eastern` but does not prove what the dialog held.
- Expect (INFERRED): the three fields Format / Data Type / Time Zone of Imported Data are present (Ref §2 lists them); the dialog may show its default rather than the last-used values (walkthrough v2:163 says the Time Zone box defaults to UTC; Ref §2 is silent).
- Falsifier: any of the three fields is missing, or opening the section starts an import or a file picker by itself.
- STOP on any falsifier, or if the section can only be closed with an Import / OK button. STOP also if Amear cannot state the three original import settings at GATE 1: Phase 1 then does not start.
- Phase 1 gate input: Amear states in writing which Format / Data Type / Time Zone he used for the existing `NQCONT` import. Claude does not supply them.

**0.8 Connections and live-data recording (read-only).**
- Path: Control Center bottom-left connection status, and the `Connections` menu on the Control Center menu bar (Ref §1h, lines 84-86; menu items at line 33). Then the settings window: `Tools > Settings` (Ref line 32 lists `Settings` in the Tools menu), category "Market data" (recorded at `docs/reports/2026-10-20-a20-adversarial-1.md:65`); the exact path on Fusion is UNVERIFIED (see 0.3). Then `Tools > Instruments`, Future `NQCONT`, **Edit**. Close every window with Cancel / X.
- Read back: every connection with its dot colour (or no dot); the label and value of any setting about saving or recording live / real-time data as historical (label UNVERIFIED; on the old install the stored keys were `SaveDataAsHistorical` and `RecordForPlayback`, both `false`, adversarial finding 1); in the Future `NQCONT` Edit sheet, any per-provider symbol-mapping fields, verbatim.
- Expect (INFERRED from the old install's `Config.xml` and `docs/reports/2026-10-20-a20-results.md:21`, REPORTED; the adversarial file cites it as line 20): only Simulated Data Feed connected (green); save-as-historical off; no provider mapping of `NQCONT` to a real symbol. Note (OBSERVED on the old install, adversarial finding 1 and Evidence): with `Provider` = Simulator, a chart request went `(to Provider)` and NT8 wrote provider files `20260823`..`20260828` into `db/minute/NQ 09-26/` at 10:30 on 2026-08-29. A Simulated-Data-Feed-only connection therefore does **not** rule out a write into `NQCONT 09-25`; the re-lists in 1.5 and 3.4 are the guard.
- Falsifier: save-as-historical (or record) on; any connection besides Simulated Data Feed up; any mapping of `NQCONT` to `NQ` or another real root; the setting cannot be found (then its value is unknown).
- STOP on any falsifier. Read back and return to Claude Code. **Do not disconnect anything and do not change any setting in this step.**
- **Option for Amear only (S8 — his decision, not an instruction):** disconnecting the data connection(s) before Phase 1, or changing the save-as-historical setting, is Amear's call. Claude does not recommend either. If Amear chooses one, he first confirms in writing, separately: "I choose to [disconnect ___ / set ___ to ___]; I have read back its current state as ___ so it can be restored." Only then is it done, and 0.8 is read back again.

---

## Phase 1 — Non-destructive path: a second copy imported under `NQCONT 09-25`

**GATE 1 — Amear confirms in writing before any step in this phase:** "Phase 0 passed with no STOP; I approve importing a copy named `NQCONT 09-25.Last.txt`, which adds data to the install; the import settings will be Format ___ / Data Type ___ / Time Zone ___, identical to the original `NQCONT` import." This phase **adds** a data folder; it deletes nothing and changes no instrument, template or merge policy.

**1.1 Make the copy.**
- Path: Explorer, folder from 0.5. Select `NQCONT.Last.txt` → Copy → Paste in the same folder; rename **the copy only** to `NQCONT 09-25.Last.txt` (one space, `09-25`, `.Last.txt`; name form INFERRED from Ref §2 `<ROOT> <MM-YY>` and Q2 item 2). Never rename or move the original.
- Read back: both file names exactly as Explorer shows them with extensions on; both sizes in bytes.
- Expect: `NQCONT.Last.txt` and `NQCONT 09-25.Last.txt`, both 95,900,139 bytes.
- Falsifier / STOP: the original is gone or renamed; the copy reads `… .txt.txt` or `NQCONT.Last - Copy…`; sizes differ.

**1.2 Import.**
- Path: `Tools > Historical Data` → Import section (Ref §2). Set Format / Data Type / Time Zone to the three values Amear wrote at GATE 1; read them back before clicking. Click **Import** → select `NQCONT 09-25.Last.txt` → **Open**.
- Read back: the three field values as set; the confirmation window text verbatim; then the Control Center **Log** tab, every line from the import, verbatim.
- Expect (Ref §2): a confirmation window. An empty Log is NOT evidence of success: on the old install the 11:43:45 write of all 1,710 files left no Log line (adversarial finding 12; research Q1 item 1). The success readback is 1.4.
- Falsifier: `Instrument is not supported by repository` (the 4uu error, Ref §2) or any other error line; no confirmation window.
- STOP on any error line, including `Unknown instrument`. Record it verbatim and return; Claude Code decides whether it is provider noise (Q2 item 7). STOP also if any field differs from the GATE 1 values.

**1.3 Instrument list after the import.**
- Path: `Tools > Instruments`, filter `NQCONT`.
- Read back: number of rows; any row not seen in 0.2; for each row, type, point value and tick size as the list shows them.
- Expect (INFERRED): the same two rows as 0.2.
- Falsifier: a row count other than 2, or any row type / point value / tick that differs from 0.2.
- STOP on any falsifier, and in particular if **any new instrument row** appeared. The Stock row's origin is UNVERIFIED (Q4 item 5) and an import may create instruments. Do not delete the new row; report it.

**1.4 Files on disk after the import.**
- Path: Explorer → `Documents\NinjaTrader 8\db\minute\`.
- Read back: the folder list (any new folder?); `NQCONT 09-25` item count, first and last file name, and the newest `Date modified` in that folder (sort by Date modified); `NQCONT` item count. These are the reference values for the re-lists in 1.5 and 3.4.
- Expect (INFERRED, Q3 test (i) / Q6 item 6): `NQCONT 09-25` ≈ 1,710 files, `20210307.Last.ncd` … `20260720.Last.ncd`; `NQCONT` count identical to 0.4.
- Falsifier: `NQCONT 09-25` holds far fewer files, or only dates near 2025 → NT8 truncated to the contract's life (Q3, SPEC-SILENT).
- STOP if the count is far fewer than ≈ 1,710, if the `NQCONT` count changed, or if a folder other than `NQCONT 09-25` appeared.

**1.5 Chart the Future contract.**
- Path: new 1-minute chart, instrument **`NQCONT SEP25`** (the picker's display of `NQCONT 09-25`, INFERRED pairing from co-timed old-install log/trace lines, Q2 item 1 — not OBSERVED; this step tests it). Data Series: Last, Minute 1, Trading hours: select `CME US Index Futures RTH` (select only; the template is not edited). Range 2021-03-08 → 2021-03-12; then 2026-07-01 → 2026-07-17.
- Read back: the instrument string in the Data Series dialog and the chart title, both verbatim; whether candles render for each range; any Log lines verbatim; any prompt (rollover, contract) verbatim, clicking nothing; OHLC of the **2021-03-08 10:00** bar and of the **2026-07-17 09:31** bar.
- Expect (INFERRED; Q3 test (ii); merge effect SPEC-SILENT, Open 4): instrument string and title read `NQCONT SEP25`; candles in both ranges; OHLC exactly equal to the two spot-check lines in Phase 0. Candles that equal the imported file, after an import that wrote only `NQCONT 09-25`, are the on-Fusion test of the `SEP25` = `09-25` pairing (INFERRED).
- Falsifier and meaning:
  - Exact equality → no re-adjustment by NT8. PASS.
  - The same constant added to all four of O/H/L/C → NT8 re-adjusted the already back-adjusted series (D-2026-07-17-A / D-2026-07-21-A) under the merge policy. **STOP → Phase 2.**
  - Values equal a *different* minute of the file → a time-zone shift at import. **STOP.**
  - Blank chart for 2021, or `Unknown instrument 'NQCONT 09-25'` → expiry filters serving, or merge/rollover mapping intervenes (Q3). **STOP → Phase 2.**
  - Any other difference, a blank or partial 2026-07 range, an instrument string or title other than `NQCONT SEP25` (the `SEP25` = `09-25` pairing then fails on Fusion), or any rollover or contract prompt (click nothing; read it back) → **STOP**.
- **Re-list after the chart (finding 1 guard).** Path: Explorer → `Documents\NinjaTrader 8\db\minute\NQCONT 09-25\`. Read back: item count, first and last file name, any file whose name carries today's date (e.g. `20261031.Last.ncd`) or any date after `20260720`, and the newest `Date modified`. Expect (INFERRED): identical to 1.4. Falsifier: the count, first or last file changed; any file named after `20260720.Last.ncd`; a `Date modified` later than the 1.4 readback. **STOP** on any falsifier: the folder may now mix provider bars with the import. Delete nothing.
- Merge policy: **do not change it in this phase**, whatever 0.2/0.3 showed.

**1.6 Exit from Phase 1.**
- Path: this document; no NT8 action.
- Read back: the result of each of 0.1-0.8 and 1.1-1.5 (pass, or the STOP and its readback).
- Expect: all pass.
- Falsifier: any STOP in Phase 0 or in 1.1-1.5.
- STOP on any falsifier: return to Claude Code; Phase 2 only as Amear decides. Only if all pass: go to Phase 3. Phase 2 is skipped.

---

## Phase 2 — Alternatives, only if Phase 1 STOPped (none executed by default)

Amear decides. **Each option needs its own explicit written Amear confirmation, recorded before acting.** Nothing here is the default. After any option, repeat 1.3-1.5 and read back.

- **(a) Per-instrument Merge policy = DoNotMerge on the Future row.** Path: `Tools > Instruments` → Future `NQCONT` → Edit → Merge policy → `DoNotMerge` (Ref §6: "single expiry only"). This **edits an instrument**. Before: read back the current value (from 0.2) so it can be set back. Fits the "constant offset" failure in 1.5. Expect (INFERRED): no offset afterwards. Falsifier: offset persists → STOP. Does not address a blank 2021 chart caused by an expiry filter.
- **(b) `NQCONT ##-##`.** Expected **not** to help: Ref §6 says `##-##` requires provider support (Open 6); the 2026-10-31 attempt refused a March 2021 start and raised an "unknown instrument" error (REPORTED, 10-31 voice notes); the one-row rollover table may leave no contract before 2025-12-01 (Q2 item 6, Open 5). Listed for completeness.
- **(c) Rename or remove the Stock `NQCONT` row.** Consequences SPEC-SILENT (Q4 item 2, Open 7): not known whether bare `NQCONT` would then resolve to the Future, or whether `db\minute\NQCONT\` would be orphaned or deleted. Not required to reach the Future row (Q4 item 1). Never a default. **Never delete the `db\minute\NQCONT\` folder.** Datum (INFERRED, adversarial finding 7; research Q4 item 2): `NQCONT 12-29` was requested at Daily period three times, yet no `12-29` folder survives and no 12-29 contract row remains. Removing a row or contract month may remove its data folders. Treat Stock-row removal, and any edit that removes a Future contract month, as a possible deletion of `db\minute\NQCONT\` or `db\minute\NQCONT 09-25\`.

No option deletes any instrument, data folder or template without a further, separate Amear step. No option touches any trading-hours template (F2 FROZEN).

---

## Phase 3 — Baseline run 0-S on `NQCONT SEP25`

Precondition: Phase 1 passed (or a Phase 2 option was confirmed by Amear and 1.3-1.5 then passed).

**3.1 Settings.** Path: Strategy Analyzer, strategy `PraxisNoiseAreaBreakout` (base). The run-4 settings, verbatim from `docs/reports/2026-10-31-voice-handoff-backtest-session.md:107-118`:

| Field | Value |
|---|---|
| Instrument · Price based on · Type / Value | NQCONT · Last · Minute / 1 |
| Start → End | 2021-03-08 → 2026-07-17 |
| **Trading hours** | **CME US Index Futures RTH** — look at the field; run 3 was INVALID on `CME FX Futures RTH` |
| Contracts | 1 |
| Include commission | ✓, template PRAXIS ($1.48/side = $2.96 round trip) |
| Slippage | 2 |
| Order fill resolution | Standard (High only in run 0-H) |
| Exit on session close | ✓ |
| Time in force | DAY |
| Exit mode (files base/1/2 only) | BandOrVWAP for base and file 2; **OppBand** for file 1 (its default) |

**The one deliberate difference from run 4: Instrument = `NQCONT SEP25`** (not plain `NQCONT`). Everything else as the table; Order fill resolution **Standard** (this is 0-S). Read back every field before clicking Run.
- Expect (REPORTED table, handoff:107-118): every field equals the table except Instrument = `NQCONT SEP25`.
- Falsifier: any field differs on read-back; the instrument field does not read `NQCONT SEP25`; the Analyzer refuses the 2021-03-08 start; after Run, any `unknown instrument` / bars-request error line, or no results.
- STOP before Run if any field differs, if the instrument field does not read `NQCONT SEP25`, or if the Analyzer refuses the 2021-03-08 start. STOP after Run on any `unknown instrument` / bars-request error line, **whether or not results were produced**: record the line and, if present, the results verbatim, and return; Claude Code decides whether the line is provider noise (Q2 item 7). Phase 4 is not entered on this STOP; Phase 2 only as Amear decides.

Run description to carry verbatim: **"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."**

**3.2 Summary readback.** Path: Strategy Analyzer, this run's summary display (display name UNVERIFIED). Read back: the "Amear reads" column below. Expect / Falsifier: the table and the basis lines below; STOP: only on the conditions listed in this step's STOP line below (otherwise continue to Phase 4). Run-4 source text, verbatim (`…handoff…:120-122`):

Run-4 baseline to compare against (REPORTED BY AMEAR): **1,211 trades (584 L / 627 S) · net $3,136.84 ·
gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 ·
largest winner $1,792.50 · total slippage 48.44.**

| Field | run 4 (Stock row, REPORTED) | expected (INFERRED) | Amear reads |
|---|---|---|---|
| Total trades | 1,211 | 1,211 | |
| Long / short | 584 / 627 | 584 / 627 | |
| Net profit | $3,136.84 | not predictable from run 4 | |
| Gross profit | $41,447.47 | not predictable from run 4 | |
| Gross loss | −$38,310.63 | not predictable from run 4 | |
| Commission | $3,584.56 | $3,584.56 (= 1,211 × $2.96) | |
| Profit factor | 1.08 | not predictable from run 4 | |
| Max drawdown | −$4,108.84 | not predictable from run 4 | |
| Total slippage | 48.44 | 1,211.00 if NT8 reports it in points (= 1,211 × 4 ticks × 0.25); unit UNVERIFIED | |
| Largest winner | $1,792.50 | not predictable from run 4 | |

Basis and falsifiers (all INFERRED):
- **Same trade list** if the bars and the trading-hours template are identical: the strategy uses market orders only (`EnterLong`/`EnterShort`/`ExitLong`/`ExitShort`, `ninjascript/PraxisNoiseAreaBreakout.cs:211-290`) and has no TickSize / PointValue reference in its logic (Evidence grep). Falsifier: any other trade count or L/S split → the bars or session differ → STOP before Phase 4.
- **Commission unchanged**: per-trade template, independent of point value. Falsifier: any other value.
- **Total slippage 48.44 → 1,211.00**: run 4's 48.44 = 1,211 × 4 × 0.01 (Stock tick). Falsifier: 48.44 again (still the Stock row) or a value not a multiple of 1,211 × 0.25.
- **Net / gross / PF / max DD / largest winner cannot be predicted from run 4**: price-P&L dollars scale ×20, but the slippage cost rises from $0.04 to $20 per trade (4 ticks × 0.25 × $20). No number is invented here.
- Observed comment error, not edited: `PraxisNoiseAreaBreakout.cs:36` says "$5.00 / point"; NQ is $20 / point (the Future row is REPORTED at point value 20, tick 0.25).
- **STOP before Phase 4** if total trades ≠ 1,211 or L/S ≠ 584 / 627; if total slippage reads 48.44 (the Stock-row signature) or any value that is not a multiple of 302.75 (= 1,211 × 0.25); if commission differs from $3,584.56; or if any 3.1 field read back differently. Do not open the template control.

**3.3 Further readbacks, verbatim from `…handoff…:140-148`** (run 0-H is not part of this walkthrough). Path: Strategy Analyzer, this run's trades list (display name UNVERIFIED). Read back: the block below.
- Expect: R1 exit names drawn from {`FlatEOD`, `XL`, `XS`} (OBSERVED in `ninjascript/PraxisNoiseAreaBreakout.cs:211-290`, Evidence) plus NT8's own names for the session-close exit and for the closing leg of a reversal (the code reverses by `EnterLong` while short, `:224-225`), believed to read `Exit on session close` and `Close position` (names UNVERIFIED); no Qty > 1 (INFERRED: `Contracts` = 1, table 3.1).
- Falsifier: any other exit name, or any Qty > 1.
- **STOP before Phase 4** on either falsifier: read the row(s) back verbatim and return.

- **Read back both runs:** total trades, L/S, net, PF, max DD, total slippage; plus the **first 5 and
  last 5 trades** of each (entry time, exit time, exit name, profit). If the grid exports (right-click;
  UNVERIFIED), export both — Claude Code diffs rows on the Mac. Totals matching is necessary, not proof
  (open question NEEDS AMEAR 5: what counts as "identical").
- **On the 0-S run, also read (these settle the base's own open items):**
  - **R1** exit names counted (FlatEOD / Exit on session close / XL / XS / Close position / other);
    for end-of-day rows, exit time (16:00 or 09:31?) and whether exit date = entry date.
  - **R2** any Qty > 1; two exit rows with one timestamp; "ignored" order messages in the Log tab.
  - **R6** trades entered on early-close dates (from the template, R-I2): exit name, date, time.

Run-4's first/last 5 trades are not on disk, so this run's are recorded without a comparison column.

**3.4 Re-list the contract folder after the run (finding 1 guard).**
- Path: Explorer → `Documents\NinjaTrader 8\db\minute\NQCONT 09-25\`.
- Read back: item count, first and last file name, any file whose name carries today's date or any date after `20260720`, and the newest `Date modified`.
- Expect (INFERRED): identical to the 1.4 readback (and to the 1.5 re-list).
- Falsifier: the count, first or last file changed; any file named after `20260720.Last.ncd`; a `Date modified` later than the 1.4 readback.
- **STOP before Phase 4** on any falsifier: the run may have read, and the folder may now hold, provider bars mixed with the import. Delete nothing.

---

## Phase 4 — Save the settings as default

**Precondition:** 3.1, 3.2, 3.3 and 3.4 completed with no STOP. Otherwise do not touch the template control.

**4.1 What the control offers.** Path: Strategy Analyzer Settings pane, the template control (a `template` label at the lower right was transcribed from the run-3 screenshot, Q5 item 2; control label **UNVERIFIED**, Q5 item 3, Open 10).
- First readback: **"What does the Analyzer's template control offer: Save / Save as default / Load / Remove?"** — read every item verbatim. Click nothing yet.
- Expect: UNVERIFIED (Q5 item 3): an item that saves the current settings as the default (Amear's ruling 3 records the belief "Template → Save as default", voice notes line 55).
- Falsifier: no item that saves a default; or the control cannot be found.
- STOP on either: read the menu back verbatim, click nothing, and return to Claude Code.

**4.2 Amear's choice (S8 — he decides).** The existing template **"Praxis Backtest"** (saved and set as default 2026-10-28, re-saved 2026-10-30 with the corrected session, REPORTED, Q5 item 1) holds the Stock-row `NQCONT`. Overwriting it alters a template. Options:
- (i) save the current settings under a **new name** and set that as default; or
- (ii) **overwrite** "Praxis Backtest".
Either needs Amear's explicit confirmation, recorded before clicking. Claude does not choose. Do not Remove any template.
- Path: the item from 4.1 that matches Amear's confirmed choice.
- Read back: the name saved under; the exact menu item clicked; any prompt text verbatim.
- Expect: a confirmation prompt or none (UNVERIFIED).
- Falsifier: any prompt that mentions deleting, removing, replacing, or a trading-hours template; the name saved under differs from the one Amear confirmed.
- STOP on any falsifier, even under option (ii): do not answer the prompt, read it back verbatim, and return. Amear confirms again before anything further.

**4.3 Verify.** Path: close the Strategy Analyzer; reopen it.
- Read back: the Instrument field, and every run-4 field from the 3.1 table.
- Expect (INFERRED): Instrument `NQCONT SEP25`; every field pre-filled as in 3.1 (Trading hours `CME US Index Futures RTH`, Slippage 2, Standard, PRAXIS commission, dates 2021-03-08 → 2026-07-17).
- Falsifier: Instrument reads plain `NQCONT`, or any field differs → the default did not take; STOP and read back.

**The walkthrough ends at this readback.**

---

## Evidence

Every spot-check line and verbatim settings block above came from the commands below, run on the Mac on 2026-10-31. Output is appended by `tee`, not retyped. The body above was built by a generator that splices `sed -n` ranges of the handoff into a template (so the settings and readback blocks are byte-copies). Evidence command as run (S = this session's scratchpad directory): `bash -v "$S/a9d-evidence.sh" 2>&1 | tee -a "$W"`, with `W=/Volumes/Sensidine/Praxis.build/docs/reports/2026-10-31-a9d-walkthrough-future-row.md`. The script echoes each of its own lines (`bash -v`), so the commands appear interleaved with their output.

````text
cd /Volumes/Sensidine/Praxis.build
F="$HOME/praxis-signals/b2-data/NQCONT.Last.txt"
wc -l "$F"
 1857362 /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
ls -l "$F"
-rw-r--r--@ 1 admin  staff  95900139 Jul 23 13:02 /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
shasum -a 256 "$F"
307c5e8af1da42b7606d666f14e4f34228feec50d19dd52d25396aae1b16e454  /Users/admin/praxis-signals/b2-data/NQCONT.Last.txt
cmp "$F" "$HOME/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt" && echo cmp-identical
cmp-identical
head -1 "$F"
20210307 180100;16120.5;16167;16120.5;16154.75;17
tail -1 "$F"
20260720 112700;29005.5;29020.75;29003.5;29016;308
echo ----- spot-check bars
----- spot-check bars
/usr/bin/grep -n -m1 '^20210308 100000;' "$F"
649:20210308 100000;15968.75;15976.5;15962;15976.5;8
/usr/bin/grep -n -m1 '^20260717 093100;' "$F"
1855934:20260717 093100;28605.25;28659;28599.5;28644.25;4963
echo ----- run-4 settings, baseline, limitation sentence, readbacks
----- run-4 settings, baseline, limitation sentence, readbacks
sed -n '107,122p' docs/reports/2026-10-31-voice-handoff-backtest-session.md
| Field | Value |
|---|---|
| Instrument · Price based on · Type / Value | NQCONT · Last · Minute / 1 |
| Start → End | 2021-03-08 → 2026-07-17 |
| **Trading hours** | **CME US Index Futures RTH** — look at the field; run 3 was INVALID on `CME FX Futures RTH` |
| Contracts | 1 |
| Include commission | ✓, template PRAXIS ($1.48/side = $2.96 round trip) |
| Slippage | 2 |
| Order fill resolution | Standard (High only in run 0-H) |
| Exit on session close | ✓ |
| Time in force | DAY |
| Exit mode (files base/1/2 only) | BandOrVWAP for base and file 2; **OppBand** for file 1 (its default) |

Run-4 baseline to compare against (REPORTED BY AMEAR): **1,211 trades (584 L / 627 S) · net $3,136.84 ·
gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 ·
largest winner $1,792.50 · total slippage 48.44.**
sed -n '131,132p' docs/reports/2026-10-31-voice-handoff-backtest-session.md
**"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."**

sed -n '140,148p' docs/reports/2026-10-31-voice-handoff-backtest-session.md
- **Read back both runs:** total trades, L/S, net, PF, max DD, total slippage; plus the **first 5 and
  last 5 trades** of each (entry time, exit time, exit name, profit). If the grid exports (right-click;
  UNVERIFIED), export both — Claude Code diffs rows on the Mac. Totals matching is necessary, not proof
  (open question NEEDS AMEAR 5: what counts as "identical").
- **On the 0-S run, also read (these settle the base's own open items):**
  - **R1** exit names counted (FlatEOD / Exit on session close / XL / XS / Close position / other);
    for end-of-day rows, exit time (16:00 or 09:31?) and whether exit date = entry date.
  - **R2** any Qty > 1; two exit rows with one timestamp; "ignored" order messages in the Log tab.
  - **R6** trades entered on early-close dates (from the template, R-I2): exit name, date, time.
echo ----- import settings on disk: 10-28 notes, old-install instructions, REPORTED ET
----- import settings on disk: 10-28 notes, old-install instructions, REPORTED ET
/usr/bin/grep -n -i -E 'import|time zone|format|data type' docs/reports/2026-10-28-voice-session-notes.md
20:- Reading: the long-running "blank chart" is at least partly a date-range effect. The imported series ends in July 2026, so a default load of recent days requests bars that don't exist. The bar timestamps have not been checked yet. The "unknown instrument NQCONT" Strategy Analyzer defect has not been re-tested yet.
24:- Import file `~/praxis-signals/b2-data/NQ-continuous-1min.nt8import.txt` has `20260717 093100;28605.25;…;4963` and `20260717 093200;28644.25;…`. **NT8 matches the file bar for bar. There is no hour shift and no minute shift.**
sed -n '140,145p' docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
| Field | Set it to |
|---|---|
| Format | `NinjaTrader (end of bar timestamps)` |
| Data Type | `Last` |
| **Time Zone of Imported Data** | **`US Eastern`** |
| (tick-only checkboxes) | leave unchecked — this is minute data |
sed -n '44p' docs/reports/2026-10-20-seat-close-handover.md
3. NT8 reads on Fusion: its own time zone, Kinetick. Fusion is Eastern with DST; the old VM was fixed UTC−4; NQCONT was imported as ET.
echo ----- strategy order calls and tick/point references
----- strategy order calls and tick/point references
/usr/bin/grep -n -E 'EnterLong|EnterShort|ExitLong|ExitShort|TickSize|PointValue' ninjascript/PraxisNoiseAreaBreakout.cs
36:// INSTRUMENT: NQ futures. TickSize 0.25, $5.00 / point (=$1.25 / tick). Add this strategy to a
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");
echo ----- ruling row
----- ruling row
/usr/bin/grep -n -o '2026-10-31T14:59:37Z.\{0,200\}' DECISION_LOG.md
465:2026-10-31T14:59:37Z] **WHO: amear** | SOURCE: `docs/reports/2026-10-31-voice-session-notes.md` (voice session 14:29–14:52Z; rulings typed by Amear 14:54–14:55Z; pasted into this session by Amear with the instruction
````

**Evidence added by a9d worker 4 (2026-10-31), for steps 0.7, 0.8, 1.5, 3.4 and 4.1.** Read-only; the rescued install was only listed and grepped. Output appended by `tee -a`, not retyped. Command as run (S = this session's scratchpad `.../scratchpad/w4`): `bash -v "$S/w4-evidence.sh" 2>&1 | tee -a "$W"`. Evidence for findings 2, 3, 6, 7, 8 and 12 is pasted in `docs/reports/2026-10-31-a9d-adversarial.md` and is cited there, not re-pasted.

````text
cd /Volumes/Sensidine/Praxis.build
R="/Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full"
echo ----- finding 1: provider-written files in the old install, NQ 09-26, newest 8 by name, exact mtimes
----- finding 1: provider-written files in the old install, NQ 09-26, newest 8 by name, exact mtimes
ls -l -T "$R/db/minute/NQ 09-26/" | tail -8
-rw-r--r--@ 1 admin  staff   2525 Jul 20 11:26:23 2026 20260719.Last.ncd
-rw-r--r--@ 1 admin  staff   4903 Jul 20 11:26:23 2026 20260720.Last.ncd
-rw-r--r--@ 1 admin  staff   2520 Aug 29 10:30:20 2026 20260823.Last.ncd
-rw-r--r--@ 1 admin  staff   9898 Aug 29 10:30:20 2026 20260824.Last.ncd
-rw-r--r--@ 1 admin  staff   9878 Aug 29 10:30:20 2026 20260825.Last.ncd
-rw-r--r--@ 1 admin  staff   9935 Aug 29 10:30:20 2026 20260826.Last.ncd
-rw-r--r--@ 1 admin  staff   9916 Aug 29 10:30:20 2026 20260827.Last.ncd
-rw-r--r--@ 1 admin  staff   7423 Aug 29 10:30:20 2026 20260828.Last.ncd
echo ----- the provider request and an HDS line on 2026-08-29
----- the provider request and an HDS line on 2026-08-29
/usr/bin/grep -h -a -E "instrument='NQ SEP26' from='8/23/2026" "$R"/trace/trace.20260829.0000*.txt | tr -d '\r' | head -3
2026-08-29 10:30:20:630 Cbi.Instrument.RequestBars (to Provider): instrument='NQ SEP26' from='8/23/2026 12:00:00 AM' to='8/28/2026 12:00:00 AM' period='1 Minute'
/usr/bin/grep -h -a 'Using HDS' "$R"/log/*.txt | tr -d '\r' | /usr/bin/grep '^2026-08-29' | head -1
2026-08-29 09:28:27:137|1|2|Using HDS (hds-us-nt-016.ninjatrader.com/31655)
echo ----- old-install Config.xml connection and recording keys
----- old-install Config.xml connection and recording keys
/usr/bin/grep -n -a -E 'ConnectOnStartup|<Provider>|RecordForPlayback|SaveDataAsHistorical' "$R/Config.xml" | tr -d '\r'
18:      <ConnectOnStartup>true</ConnectOnStartup>
27:      <Provider>Simulator</Provider>
34:      <ConnectOnStartup>false</ConnectOnStartup>
43:      <Provider>Provider7</Provider>
53:      <ConnectOnStartup>false</ConnectOnStartup>
62:      <Provider>Playback</Provider>
120:      <RecordForPlayback>false</RecordForPlayback>
121:      <SaveDataAsHistorical>false</SaveDataAsHistorical>
echo ----- reference: Tools menu, Connections menu, section 1h
----- reference: Tools menu, Connections menu, section 1h
sed -n '32,33p' docs/reference/2026-07-24-nt8-windows-reference.md
- **Tools menu** (from notes): Instruments · Instrument Lists · Database Management · Hot Keys · **Historical Data** · Commissions · Risk · **Trading Hours** · Import · Export · Remove NinjaScript Assembly… · Global Simulation Mode *(license-gated)* · Client Dashboard · Settings.
- **Connections menu** ([`20-connections-menu.png`](assets/nt8-2026-07-24/20-connections-menu.png)): Kinetick – End Of Day (Free) · Playback · Simulated Data Feed *(green = connected, "disconnect" link)* · Simulation *("configure" link)*.
sed -n '84,87p' docs/reference/2026-07-24-nt8-windows-reference.md
### 1h. Connections
- **What it's for:** configure/connect/disconnect market-data and brokerage connections; per-provider + aggregate status (bottom-left of Control Center).
- **Open:** `Connections` menu on the Control Center menu bar. ([`20-connections-menu.png`](assets/nt8-2026-07-24/20-connections-menu.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/connections_menu.htm
echo ----- reference mentions of UTC, count
----- reference mentions of UTC, count
/usr/bin/grep -c -i 'UTC' docs/reference/2026-07-24-nt8-windows-reference.md
0
echo ----- walkthrough v2 line 163, a20 results line 21, a20 adversarial-1 line 65
----- walkthrough v2 line 163, a20 results line 21, a20 adversarial-1 line 65
sed -n '163p' docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
**Two — the time zone box defaults to UTC, and that killed the 7/24 run.** The
sed -n '21p' docs/reports/2026-10-20-a20-results.md
Connections rows (name + dot colour, or no dot): Simulated Data Feed, green dot. Kinetick – End Of Day (Free), no dot. Playback, no dot. Simulation, no dot.
sed -n '65p' docs/reports/2026-10-20-a20-adversarial-1.md
- `nt8-general-time-zone.png`: an NT8 window titled "Settings". The categories are General (highlighted), Trading, Strategies, Automated trading interface, Market data. The Time zone row reads "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" in a **drop-down box with a ▼ chevron at its right edge**. Language, Skin and Symbology are also drop-downs with right-edge ▼ chevrons. The Properties pane's own scroll arrows are a tiny ▲▼ pair at the **top**-right of the Properties header. The buttons at the bottom right are OK, Cancel, Apply, with Apply greyed. The taskbar clock reads 11:15 AM 9/29/2026.
echo ----- voice notes line 55, ruling 3
----- voice notes line 55, ruling 3
sed -n '55p' docs/reports/2026-10-31-voice-session-notes.md
3. **Reminder Amear asked for:** once the Future row loads and the new baseline run is done, **save those Strategy Analyzer settings as the default**, so he isn't re-entering them every run and can't silently fall back to the Stock row through human error. The return handoff (item 4) must carry this as an explicit step. How NT8 saves Analyzer defaults (believed to be a Template → Save as default control) is UNVERIFIED; Code confirms the control before it goes in a step.
````
