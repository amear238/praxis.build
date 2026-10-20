# a20 manager report: Fusion time-zone + Kinetick walkthrough

**Bead:** `Praxis_build-a20` (P1, due 2026-10-31). **Written:** 2026-10-20 by praxis-manager. **Baseline HEAD:** `e53dcbb`.
**Deliverable:** `docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md` (new). **Nothing committed.** Only the two a20 files are staged; the 9 carried F4/r8j paths were not touched.
**Not an audit grade.** The Result line at the foot is the manager's stress-test outcome, which the report contract requires. It doesn't substitute for the master's independent audit. The walkthrough isn't cleared for Amear until the auditor grades it.

## Task

Produce a read-only, Cancel-only walkthrough for Amear to click by hand on the Fusion VM. It reads (W) the Windows time zone and its automatic-DST switch, (N) NT8's own time zone and (K) Kinetick EOD connection status. It has a branch table written before the reads, provenance labels on every premise, and no fix steps. It is modelled on v3, with a removal diff against v3. Scope rulings: Amear's, as relayed in the master's brief and DECISION_LOG row `2026-10-20T13:29:00Z`.

## Rubric criteria addressed

- **S1** "Every claim in a report has pasted command output, not a description of output." Evidence is pasted below for every VERIFIED item in the walkthrough.
- **S2** "No component is reported at a higher level than the evidence supports." Every premise is labelled. Three full adversarial passes attacked overstatement specifically.
- **S8** "No question that belongs to Amear is answered on his behalf." Every branch ends "Amear decides". There are no fix steps. Six open questions are listed unanswered.
- **S9 note R3** "a mechanism named in a comment, a brief, or a report is a claim, and a claim is graded by experiment, not by inspection." It was applied to the bead's own premises. The bead's cited source for "NQCONT imported as ET" was checked by grep and **does not support it** (§E3). The bead's menu path "Tools, Options, General" was checked against the only on-disk capture and **does not match it**: the window is titled "Settings" (§E1). NT8/Windows behaviour the walkthrough can't test (DST handling, what a click does) is labelled INFERRED, and no conclusion depends on it.
- **Survival rule** (HANDOFF.md 2026-10-20 card). The removal diff against v3 is in §V.

## Workers dispatched

| # | Mode | Scope | Outcome |
|---|---|---|---|
| W1 | BUILD | research + draft | **Budget-killed at its 40-turn limit.** The walkthrough draft was written. Its worker report (`2026-10-20-a20-worker1-research.md`) was **never written**, so the research half counts as NO RESULT. The manager re-verified every premise the draft cites (§E1–E6). |
| W2 | ADVERSARIAL | attack the draft | `DEFECTS FOUND (3 blocking, 12 minor)`, file `2026-10-20-a20-adversarial-1.md` |
| W3 | BUILD | fix adversarial-1 F1–F15 | All 15 applied (§D1). It flagged an error in the manager's brief: the brief said both screenshots date from 09-29, and the Connections one is 07-24. The worker corrected it. |
| W4 | ADVERSARIAL | re-check + regression hunt | `DEFECTS FOUND (1 blocking, 10 minor)`, file `2026-10-20-a20-adversarial-2.md` |
| W5 | BUILD | fix adversarial-2 findings 1–11 + P11 | All applied (§D2) |
| W6 | ADVERSARIAL | fresh full attack + regression | `DEFECTS FOUND (0 blocking, 8 minor)`, file `2026-10-20-a20-adversarial-3.md` |
| W7 | BUILD | fix adversarial-3 M2–M8 | All applied (§D3) |
| W8 | ADVERSARIAL (narrow) | the fix-3 diff only; returned a message, no file | §A4 |

## Process log

1. Read SPEC_RUBRIC, v3, and the grade sections of v1/v2/v4/v5. Read HANDOFF 1–40, the seat-close handover, migration updates 1 and 2, and DECISION_LOG rows 393, 411 and 415. Captured the baseline staged numstat (§F).
2. **Early finding, before dispatch.** The r8j session-42/44 reports the bead names as the source for "NQCONT imported as ET" are about Phase-3 spec text. This was passed to W1 as a lead to confirm or refute. It was confirmed (§E3).
3. W1 drafted, then hit its turn limit. The manager viewed all three cited images itself and re-ran every text citation (§E1–E6).
4. W2 → W3 → W4 → W5 → W6 → W7 → W8. After each fix, the manager diffed pre/post itself (§D1–D3) and re-ran the v3 phrase-survival check.
5. **Negative test of the survival check** (§E7). Deleting two v3 safety clauses from a scratch copy makes the check report two new zeros. Limit: it catches verbatim loss only, not weakened meaning. The adversarial passes cover that gap, and adversarial-2 caught a meaning-level carry-over (the Settings button order) that the phrase check couldn't.
6. The manager corrected the header disclosure line itself (one line, §D4). It then staged the two a20 files with exact-path `git add --`.

## Verification evidence

All blocks below are command output captured this session. **Observer note:** where a block's subject is an a20 file, it records that file at capture time. Later fixes changed the walkthrough after some captures; §D1–D4 give the diffs, and §E8 is taken against the final file.

### E1. Images, viewed by the manager with the Read tool (an observation of the image; no command output exists for pixels)

- `~/VM-Rescue-2026-09-29/screenshots/nt8-general-time-zone.png`: NT8 window titled **Settings**. Categories: General (highlighted), Trading, Strategies, Automated trading interface, Market data. The **Time zone** row reads `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan` in a drop-down box. The Properties pane's scroll arrows are a small pair at its top-right. The bottom-right buttons read **OK, Cancel, Apply**. Log rows are dated `9/29/2026 11:13`; the taskbar reads `11:15 AM 9/29/2026`.
- `~/VM-Rescue-2026-09-29/screenshots/windows-time-zone.png`: Windows 11 Settings, **Time & language** page, account `amearbani-ahmad`, `11:14 AM Tuesday, September 29, 2026`, Time zone `(UTC-04:00) Georgetown, La Paz, Manaus, San Juan`, Region United States. No DST switch is on this page.
- `docs/reference/assets/nt8-2026-07-24/20-connections-menu.png`: the Connections list reads Kinetick – End Of Day (Free) (no dot), Playback, Simulated Data Feed (green dot, `disconnect`), Simulation, and a `configure` link.
```
$ ls -l (screenshot file dates)
-rw-------@ 1 admin  staff  472306 Sep 29 11:19 /Users/admin/VM-Rescue-2026-09-29/screenshots/nt8-general-time-zone.png
-rw-------@ 1 admin  staff  182342 Sep 29 11:19 /Users/admin/VM-Rescue-2026-09-29/screenshots/windows-time-zone.png
-rw-r--r--@ 1 admin  staff  215902 Jul 24 09:25 docs/reference/assets/nt8-2026-07-24/20-connections-menu.png
```

### E2. Premise sources (capture notes, Config.xml, HANDOFF, migration updates, Mac clock)
```
$ sed -n 1,5p;33,48p docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt
﻿NinjaTrader 8 Layout Reference — Discovery Notes
Captured: 2026-07-24 (session start ~8:14 AM ET restart, captures through ~8:44 AM ET)
Output folder: C:\Mac\Home\praxis-signals\b2-data\inbound\nt8-layout-2026-07-24\

============================================================
Tools menu (top to bottom, as expanded):
  Instruments
  Instrument Lists
  Database Management
  Hot Keys
  Historical Data
  Commissions
  Risk
  Trading Hours
  Import
  Export
  Remove NinjaScript Assembly...
  Global Simulation Mode  (grayed/license-gated: "Please upgrade to a Lease or
                            Lifetime license to unlock this feature.")
  Client Dashboard
  Settings

$ grep -n TimeZone|ConnectOnStartup|Kinetick Config.xml (both rescue copies)
== /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
18:      <ConnectOnStartup>true</ConnectOnStartup>
34:      <ConnectOnStartup>false</ConnectOnStartup>
53:      <ConnectOnStartup>false</ConnectOnStartup>
203:      <TimeZoneInfoSerializable />
== /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml
18:      <ConnectOnStartup>true</ConnectOnStartup>
34:      <ConnectOnStartup>false</ConnectOnStartup>
53:      <ConnectOnStartup>false</ConnectOnStartup>
203:      <TimeZoneInfoSerializable />

$ shasum Config.xml x2
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  /Users/admin/VM-Rescue-2026-09-29/files/NinjaTrader 8-full/Config.xml

$ sed -n 7p;106p HANDOFF.md | cut -c1-600
**Analyzer check on Fusion: RESULT (A), IT OPENED.** Amear clicked it himself using walkthrough v3. He reported: NT8 **`8.1.7.2, 64-bit`**, Machine ID **`DC242F5E75674D33D865C01BEF776371`** (the Parallels install was `077EF45C…`), no licence tooltip, no new Log rows on open. **Grade: OBSERVED BY AMEAR. The master has not seen the screenshot.** **Read per the pre-registered branch, and no further:** the licence-gate theory is dead **on Fusion**. The Parallels question stands as relayed (09-29, the migration side reported it opening there; REPORTED). **The NQCONT unknown-instrument defect is unt
**`NQCONT` created · 1,857,362 records imported (ET, `Last`, confirmed in `db\minute\NQCONT`) · Part 5 compile `PASS`.**

$ sed -n 27p;55,56p;62p;67p;70p;103p;120p update-2
- `db\minute\NQCONT`: 1,710 files, 16,608,933 B, an exact match (REPORTED, Amear's count; expected figures VERIFIED from the rescue copy).
| 1 | Windows time zone on purpose; internet time on | **Done.** "(UTC-05:00) Eastern Time (US & Canada)", daylight saving On, "Set time automatically" On | REPORTED (Cowork, 2026-10-13 ~18:05Z, M-013). Decision REPORTED (Amear, update 1 §4) |
| 1a | NT8's own time zone (B2) | **NOT YET KNOWN.** Never read after install or after restore | Walkthrough log 16:04Z. INFERRED: the old `Config.xml` has an empty zone field (VERIFIED read-only, D-068), so if it was restored, NT8 follows Windows |
| 6 | Restore choice | **(a) Faithful**, Amear's call, 2026-10-16 15:52Z | D-068. Source: the unfiltered 09-29 copy `NinjaTrader 8-full/`, 5,444 files, 55,593,912 B, on disc NT8_TRANSFER, 5,445/5,445 hashes VERIFIED on the Mac and REPORTED 0 bad inside the VM |
| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server (US$50,000 pretend cash, delayed real prices). Amear accepted it on condition: no orders, no other connection (D-071). Still connected after the restore | REPORTED (in-VM agent 13:43Z; Amear 16:03Z). "Simulation" was in the old install's list (your 5.2 item 13). No broker or Rithmic added (REPORTED; every brief forbade it). Kinetick EOD: NOT 
**How the restore finished (REPORTED, walkthrough log 16:03Z–16:04Z).** The in-VM agent stopped at the "Simulation" connection. Amear finished by hand. Not recorded: whether the fresh install's files were moved aside first, the brief's whole-set manifest check (expected 5,444, 0 bad) and the read-only counts. INFERRED: 6,287 files is more than the 5,444 restored, because NT8 has run since and the installer had made 417 files. So the whole folder is **not** byte-proven against the 09-29 copy. Onl
| Daylight saving | From **2026-11-01** the Fusion VM is UTC−5, while every old-VM timestamp is fixed UTC−4 | INFERRED (calendar). Matters when comparing old and new logs |
4. **Still owed inside NT8:** Machine ID, Help > About version, NT8's own time zone (closes M-013), Kinetick EOD, and the 1,857,362 count if the defect allows. Each is a read with Cancel, no change.

$ sed -n 48p;56,58p update-1
| `winver` | **Windows 11 Pro, Version 25H2, OS Build 26200.9457** | REPORTED (Cowork read `winver`) |
| Time zone, as found | **"(UTC-05:00) Eastern Time (US & Canada)"**. "Set time automatically" **On**. "Set time zone automatically" Off. Region **Canada**. Cowork changed nothing | REPORTED |
| Daylight saving | The Eastern Time (US & Canada) zone follows daylight saving: UTC−4 now, UTC−5 from **Sunday 2026-11-01** | INFERRED (Windows' zone definition and the North American calendar). Cowork read only the zone's label. Whether the "Adjust for daylight saving time automatically" switch is on was not reported: **NOT YET KNOWN** |
| Against your B2 and the old VM | The old VM was **"(UTC-04:00) Georgetown, La Paz, Manaus, San Juan"**, a fixed UTC−4 with no daylight saving, in Windows and in NT8 (migration issue M-013) | Old VM VERIFIED (the migration's M5 report, from the B2 screenshots of 2026-09-29). INFERRED: the two agree until 2026-11-01 and differ by one hour after it. Amear's decision on this is in §4 |

$ ls -l /etc/localtime; date; date -u
lrwxr-xr-x  1 root  wheel  41 Mar 16  2026 /etc/localtime -> /var/db/timezone/zoneinfo/America/Toronto
Tue 20 Oct 2026 09:48:40 EDT
Tue 20 Oct 2026 13:48:40 UTC
```

Which connection `Config.xml:34` belongs to (line numbers in this block are offset by +4):
```
$ sed -n 5,60p Config.xml | grep -n -i "Name\|Provider\|ConnectOnStartup" (line numbers offset +4)
14:      <ConnectOnStartup>true</ConnectOnStartup>
21:      <Name>Simulated Data Feed</Name>
23:      <Provider>Simulator</Provider>
30:      <ConnectOnStartup>false</ConnectOnStartup>
37:      <Name>Kinetick – End Of Day (Free)</Name>
39:      <Provider>Provider7</Provider>
49:      <ConnectOnStartup>false</ConnectOnStartup>
56:      <Name>Playback Connection</Name>

```

### E3. "NQCONT imported as ET": the bead's cited sources do not mention NQCONT

The four r8j reports contain zero `NQCONT`, zero `US Eastern` and zero `Time Zone of Imported`. The phase-3 report's own title says it is a spec-text import. The only on-disk records are HANDOFF.md:106 (the session-52 master card), the voice-walkthrough **instructions**, and DECISION_LOG rows that never record the import zone. **Grade: REPORTED, not observed. Original reporter not identified.** The import was done on the old Parallels install.
```
$ grep -c -i "NQCONT" r8j reports; grep -n -i "import" (first 8)
== docs/reports/2026-08-06-session42-r8j-phase3-import.md NQCONT:0 'US Eastern':0 'Time Zone of Imported':0
== docs/reports/2026-08-07-session44-r8j-offset-correction.md NQCONT:0 'US Eastern':0 'Time Zone of Imported':0
== docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md NQCONT:0 'US Eastern':0 'Time Zone of Imported':0
== docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md NQCONT:0 'US Eastern':0 'Time Zone of Imported':0
# `Praxis_build-r8j` — Phase 3 Build Specification imported, de-identified

**Manager report.** Session 42, 2026-08-06. Baseline HEAD `5067d3261d6e463f8387699d847cd262398ffb9c`.
**Nothing committed. Everything staged.**

A note on the redacted term used throughout: the source document titles circuit breaker #5
with a medication brand name. It is referred to here only as "the redacted term". It is not
reproduced in this report, and every verification arm below extracted it into a shell
variable at runtime rather than typing it.

---


$ grep -n "US Eastern|records imported|1,857,362" DECISION_LOG.md HANDOFF.md STATUS.md (cut)
HANDOFF.md:52:**Check 1 (`Loaded` filing name) — `PASS` after four asks.** ~1,857,362 records filed under the **exact bare name `NQCONT`**, no suffix, in `db\minute\NQCONT`. Kills *"the data is not where we think."* **Check 3 (RTH template) — MEASURED, NOT ADJUDICATED:** prints `8:30 AM – 4:00 PM`, zone shown `Central`. **Check 
HANDOFF.md:106:**`NQCONT` created · 1,857,362 records imported (ET, `Last`, confirmed in `db\minute\NQCONT`) · Part 5 compile `PASS`.**
HANDOFF.md:120:**`Tools > Historical Data` → expand `Loaded` → read the exact instrument name the ~1,857,362 records are filed under.** It separates *"data exists, keyed to a name nothing asks for"* from *"the data is not where we think at all."* **Every proposed fix assumes the first.** Garbled in transmission twice; **a clean 
HANDOFF.md:933:- `f23b648` **1u6 CLOSED** — lossless UTC→ET conversion of the continuous NQ series. Fix: route front/back seam handoff on the source-tz (UTC) date (same basis as roll_dates), relabel to America/New_York only after routing+dedup → partition bit-identical to baseline, conversion is a pure 1:1 relabel. Attempt-1's ~
HANDOFF.md:936:**ET continuous series is ON DISK + ready to re-import:** `~/praxis-signals/b2-data/NQ-continuous-1min.csv` (1,857,362 bars, ET wall-clock, cols `Timestamp,O,H,L,C,Volume,SrcContract`). Trader re-import brief prepared + copied to clipboard this session (also scratchpad `trader-reimport-brief.txt`).
HANDOFF.md:947:- ✅ Coworker confirmed `NQ-continuous-1min.csv` present in the VM at `C:\Mac\Home\praxis-signals\b2-data\` — 1,857,362 rows, ET wall-clock, header matches spec. NT8 running with the Historical Data → Import dialog open. `PraxisNoiseAreaBreakout.cs` deployed (VM copy dated 7/17).
HANDOFF.md:959:- `c571c74` **8zd CLOSED** — `b2_stitch.py` now parses REAL NT8 exports (semicolon, headerless; daily `YYYYMMDD;O;H;L;C;V` + minute combined `YYYYMMDD HHMMSS`). Full-44 volume-only stitch emits continuous series (1,857,362 bars, 21 seams) + §4 report; caught+fixed a latent OI-alias substring bug; 5 no-overlap boun
HANDOFF.md:962:**⚠️ 1u6 (P2, PARKED — resume here first):** the stitch series is timestamped **UTC, not ET** (confirmed via DST-crossing test); the strategy is 09:30-ET anchored, so it MUST be converted to America/New_York. Attempt-1 did the zoneinfo conversion but it interacts fatally with `stitch()`'s date-window handoff → **s
STATUS.md:153:**Last updated:** 2026-07-25 (session 29 — **852 VM-agent delegation workspace LIVE EXECUTOR LEG PROVEN — 852 now closeable; wx7 external build-progress report SHIPPED (497088b). No new repo commit for the 852 proof (artifact lives outside the repo).** The Windows Claude-Code executor ran acceptance assignment `000
STATUS.md:164:- **🟢 hlw data-pull — COMPLETE (44/44 landed session 21) + stitched to lossless ET series (1u6, session 22):** all 22 daily + 22 minute files in `~/praxis-signals/b2-data/raw/`; continuous back-adjusted ET series built at `~/praxis-signals/b2-data/NQ-continuous-1min.csv` (1,857,362 bars, §4 PASS). No longer a block
STATUS.md:165:- **🔴 4uu NT8 re-import (Block-2 critical path) — TRADER/VM-gated:** the ET continuous series exists on disk but must be re-imported to NT8, then PraxisNoiseAreaBreakout.cs compiled + Strategy-Analyzer reconciled. This is the ONLY thing between here and the WFA/MC/refdist chain. Trader brief clipboarded (session 22
STATUS.md:186:- **🔴 4uu (P1, TRADER/VM) — RE-HANDED to the Cowork agent at session-27 close (brief clipboarded + `outbound/INSTRUCTIONS.md` current); AWAITING VM output in `inbound/`.** It did NOT run the re-import the prior time (layout-capture pass instead). On boot: `ls ~/praxis-signals/b2-data/inbound/` — if real import/comp
STATUS.md:200:- **🔴 FIRST ACTION — dispatch 4uu re-import v2 to the Cowork agent.** The brief is ready at share `~/praxis-signals/b2-data/4uu-VM-brief.md` (mirror `outbound/INSTRUCTIONS.md`) — hand it to the Cowork agent (clipboard/share). It fixes both 2026-07-24 failure causes: create dedicated custom instrument **`NQCONT`** (
STATUS.md:221:- **✅ 1u6 DONE (`f23b648`):** continuous series is now lossless ET (America/New_York), 1,857,362 bars, seam-gap 0, §4 PASS, 09:30-ET anchor verified. On disk at `~/praxis-signals/b2-data/NQ-continuous-1min.csv`. AUDIT_LOG flushed (`9608843`).
STATUS.md:231:- **🔴 FIRST DISPATCH — 1u6 (P2, parked):** the continuous series is UTC, must be America/New_York (09:30-ET-anchored strategy). Attempt-1 introduced silent seam data loss (see bead 1u6 notes for the confirmed root cause + full fix spec: lossless seam re-alignment + hard `distinct_instants(ET)==distinct_instants(UTC
DECISION_LOG.md:341:- [2026-08-15T14:41:00Z] WHO: praxis-master (session 51) | WHAT: **SCOPE RULING ON THE DISPATCH: a read-only measurement of already-acquired data is not work "depending on" a FROZEN criterion, and is dispatched. NO BUILD WORK IS UNFROZEN BY THIS ROW** | WHY: F3 is the adjacent frozen criterion — fill resoluti
DECISION_LOG.md:363:- [2026-08-29T18:00:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK 1 CLOSED AFTER FOUR ASKS. THE DATA IS FILED UNDER THE EXACT BARE NAME `NQCONT`, NO DATED SUFFIX. THE STORAGE-NAMING THEORY IS DEAD — AND THE MISMATCH DID NOT DISAPPEAR, IT MOVED UP ONE LAYER** | WHY: t
```

### E4. Who recorded the ET import (HANDOFF.md:98-110, DECISION_LOG 2026-08-29 rows)
```
$ sed -n 98,110p HANDOFF.md | cut -c1-400
## Resume card — 2026-08-29 (session 52) — **`4uu` MOVED ON THE VM FOR THE FIRST TIME IN FIVE WEEKS.** Instrument created, 1.86M bars imported, compile **PASS**. Analyzer **BLOCKED**. Blank chart **UNEXPLAINED**. **One commit, by Amear, UNPUSHED.**

**State, measured at close, not recalled:** `HEAD` = **`2e502ae`** — **it moved this session, from `c41a969`.** `origin/main...HEAD` = **`0 1` — ONE COMMIT AHEAD, NOT PUSHED.** 9 paths staged (unchanged), 0 stashes, **46 untracked**, `git write-tree` = `178364a6ff3b29d29055400157fa5e0ba2c6f42a`. Claude Code **`2.1.251`** — third distinct build in six sessions; one binary, PATH duplicate.

**The commit, verified not assumed:** `2e502ae` *"docs: land session-51 b2 gap-fraction measurement report [Praxis_build-1gd]"* — Amear, `10:04:43 -0400`, **one file, 520 insertions, pathspec-scoped.** It did **not** drag the F4 unit sitting at audit FAIL on C3. A **session-53 parallel handoff** (`docs/reports/2026-08-29-session53-parallel-handoff.md`, 12,893 B, `10:11:36`) also appeared during th

### ✅ WHAT ACTUALLY LANDED ON THE VM — the first real `4uu` progress since 2026-07-25

**`NQCONT` created · 1,857,362 records imported (ET, `Last`, confirmed in `db\minute\NQCONT`) · Part 5 compile `PASS`.**

**The compile grade rests on a file timestamp, and that is the whole lesson.** Amear reported it ambiguous — spinner ran and vanished, **NinjaScript Output blank throughout**. **That panel is not where compile results appear.** Verified from the layout reference: results surface in the **Editor's bottom error-list panel**, **red wavy underlines**, and the **Control Center `Log` tab** — `NinjaScrip

**Operational, carried:** **`F5` does not register on this VM keyboard** — inferred as macOS eating the function-key row before Parallels sees it, not an NT8 fault. **Use the toolbar `Compile` button.**

$ grep -n "2026-08-29" DECISION_LOG.md | grep -i "import\|Eastern\| ET" | cut -c1-400
365:- [2026-08-29T18:05:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK 3 MEASURED, NOT ADJUDICATED. The CME US Index Futures RTH template prints `8:30 AM – 4:00 PM`, time zone shown as `Central`. THE MASTER DECLINES TO CONFIRM THIS AS A GENUINE MISMATCH, BECAUSE BOTH HALVES OF THAT CONFIRMATION ARE UNOBSERVED** | WHY: Amear's arithmetic is correct on its f
367:- [2026-08-29T18:10:00Z] WHO: praxis-master (session 53) | WHAT: **SCOPE RULING AND DISPATCH: a read-only read of already-committed corpus artifacts is not work "depending on" a FROZEN criterion, and is dispatched. NO BUILD WORK IS UNFROZEN BY THIS ROW** | WHY: the two open items both hinge on facts that may already be on disk and unread — what granularity and target store the original import 
371:- [2026-08-29T19:00:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK A2 CLOSED, DECISIVE. `NQCONT` IS DEFINED AS `Type: Future`, `Expiry: 09-25`, `Rollover date: 12-01-2025`. THE REQUEST-REWRITE IS NOT AN INTERMEDIATE LAYER — IT IS THE INSTRUMENT DEFINITION ITSELF** | WHY: the master's framing at `18:00:00Z` was that *"something rewrites the request from
373:- [2026-08-29T19:05:00Z] WHO: praxis-master (session 53) | WHAT: **RULING BOUNDARY, STATED BEFORE THE COWORKER BRIEF GOES OUT: DIAGNOSTIC READS AND A REVERTED TOGGLE ARE MEASUREMENT; A PERSISTED INSTRUMENT-CONFIG CHANGE IS BUILD WORK ON `4uu` AND WAITS. `Merge Policy` IS THEREFORE NOT SET** | WHY: Amear asked whether `DoNotMerge` should be set regardless of how the continuous question resolves
375:- [2026-08-29T19:30:00Z] WHO: praxis-master (session 53) | WHO OBSERVED: vm coworker | WHAT: **🛑 HALT. THE VM STATE CONTRADICTS THE BRIEF'S BASELINE ON FOUR INDEPENDENT POINTS, AND THERE IS EVIDENCE OF ACTIVITY MINUTES BEFORE THE COWORKER STARTED. CAUSE UNESTABLISHED. TASKS 2–4 CANCELLED BEFORE EXECUTION** | WHY: **the coworker caught this on its FIRST screenshot, before touching anything, and
381:- [2026-08-29T20:10:00Z] WHO: praxis-master (session 53) | WHAT: **`Praxis_build-vu8` AUDITED `Result: FAIL` on S1 and S2. THE MANAGER SELF-GRADED `PASS`; THE INDEPENDENT AUDITOR DID NOT, AND THE MASTER RE-RAN ALL THREE CHARGES BEFORE ACCEPTING. FAIL 1 of 2. NOTHING COMMITTED** | WHY: the producer graded its own work `PASS` and that grade was never accepted — a producer does not grade its own 
387:- [2026-08-30T00:15:00Z] WHO: praxis-master (session 53) | WHAT: **🔴 MASTER'S ERROR, RECORDED NOT ABSORBED — THE "THE CHART RENDERS" PIVOT IS WITHDRAWN. IT DID NOT SURVIVE RE-CHECKING, AND THE MASTER REBUILT THE WHOLE SESSION PLAN ON A SINGLE UNREPLICATED OBSERVATION** | WHY: on being told a chart showed candles, the master wrote *"we are no longer diagnosing a broken chart — THE CHART IS REND
389:- [2026-08-30T19:55:00Z] WHO: praxis-master (orchestrator seat, opened ~2026-08-29T11:30Z) | WHAT: **SEAT CLOSE. ONE COMMIT LANDED — `2e502ae`. AND AT ITS OWN CLOSE THIS SEAT OBSERVED THAT THE WORKING TREE CARRIED CONCURRENT WORK UNDER THE SAME "SESSION 53" LABEL, FROM AN ACTOR THAT IS NOT THIS SEAT. NO DIAGNOSIS IS OFFERED** | WHY: `CLAUDE.md` forbids two Claude sessions against one working t
```

### E5. Screenshot dates, NQCONT rescue figures, clock/DST calendar, VM process, B2 wording, P6 negative search, chart-ruling search, "Options" in the handover
```
$ ls -l (screenshot file dates)
-rw-------@ 1 admin  staff  472306 Sep 29 11:19 /Users/admin/VM-Rescue-2026-09-29/screenshots/nt8-general-time-zone.png
-rw-------@ 1 admin  staff  182342 Sep 29 11:19 /Users/admin/VM-Rescue-2026-09-29/screenshots/windows-time-zone.png
-rw-r--r--@ 1 admin  staff  215902 Jul 24 09:25 docs/reference/assets/nt8-2026-07-24/20-connections-menu.png
$ git log --format="%h %ad %s" --date=short -- docs/reference/assets/nt8-2026-07-24/20-connections-menu.png
9717d93 2026-07-24 docs(8yb): NT8 8.1.7.2 Windows layout + workflow reference

$ NQCONT rescue copy: file count and byte sum
    1710
16608933

$ date; date -u; pgrep -fl vmware-vmx | cut -c1-90
Tue 20 Oct 2026 10:09:29 EDT
Tue 20 Oct 2026 14:09:29 UTC
20984 /Applications/VMware Fusion.app/Contents/Library/vmware-vmx -E en -s vmx.stdio.keep=
$ TZ=America/Toronto date (10-31 and 11-01 noon)
2026-10-31 EDT -0400
2026-11-01 EST -0500

$ sed -n 35p docs/reports/2026-09-29-vm-migration-concerns.md | cut -c1-260
| **B2** | **Record four settings as screenshots:** (1) Windows time zone (Settings, Time & language); (2) NT8 time zone (Tools, Options, General); (3) Merge Policy (Tools, Options, Market Data); (4) `Tools > Instruments`, filtered `nq`, showing every entry wi

$ P6 negative search: grep -n -i "eastern|time zone" DECISION_LOG.md rows dated 2026-08-29
0
$ grep -n -i "US Eastern" docs/reports/2026-08-29-session52-nt8-voice-walkthrough*.md HANDOFF.md
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:97:| **Time zone of imported data** | **US Eastern** |
docs/reports/2026-08-29-session52-nt8-voice-walkthrough.md:109:killed the July 24th run.** Set it to US Eastern and look at it twice.
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:144:| **Time Zone of Imported Data** | **`US Eastern`** |
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:169:**Set it to US Eastern and look at it twice before you click Import.**

$ chart/bar ruling in DECISION_LOG row 415?
(grep exit=1)

$ seat-close handover §7 step 3 and bead text: grep -c Options
0
```

### E6. Lines cited by the fixes (update 2 :25/:60/:89/:97; SPEC_RUBRIC F2), and the capture-note legend
```
$ sed -n 25p;60p;89p;97p update-2 | cut -c1-300
**NinjaTrader 8.1.7.2 is installed and restored by route (a), faithful** (D-068).
| 4 | NT8 8.1.7.2 from the saved MSI; sign in; new Machine ID | **Installed and signed in. Machine ID not recorded** | Install REPORTED (in-VM agent read the MsiInstaller events: 8.1.7.2, status 0, 2026-10-19 13:03Z). Amear signed in himself; no licence or update prompt (REPORTED). Version in Help >
- **Who started it:** NOT YET KNOWN. Amear said at 14:29Z that Parallels "still works when I log in", though the subscription is cancelled (REPORTED, I-011). So the old VM can still be run today.
| OneDrive folder backup | **Off** for Desktop, Documents, Pictures. NT8's folder is `C:\Users\amear\Documents\NinjaTrader 8`, not under OneDrive | Off REPORTED (Cowork, 10-13, M-020). Path REPORTED (in-VM agent, `GetFolderPath`, 10-16 and 10-19). Eight older Documents files stayed online-only (M-02

$ sed -n 30,34p specs/SPEC_RUBRIC.md
### F2 — Session-flat time vs. breakers #4 and #5
**Criterion.** One governing rule, written down, resolving: breaker #4 closes
positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET;
Deviation B flattens at 16:00 ET. State what happens to an open position at
15:00.
```
```
$ sed -n 49,56p docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt

Connections menu (top to bottom, as expanded):
  Kinetick – End Of Day (Free)
  Playback
  Simulated Data Feed   [green dot = currently connected]   -> "disconnect" link
  Simulation                                                 -> "configure" link
(Did not click disconnect or configure — layout capture only, per task constraints.)

```

### E7. v3 phrase-survival check, captured on the first draft, with the negative arm (two clauses deleted from a scratch copy)
```
$ for each v3 phrase: grep -c -F in v3 | in a20
For:** Amear, by hand. Not for Cowork or any automation. | v3=1 | a20=1
Auditor grade appended below when given. | v3=1 | a20=1
**Question it answers:** | v3=1 | a20=1
**Scope:** | v3=1 | a20=1
**No** setting | v3=0 | a20=0
**no** orders | v3=1 | a20=1
**Menu path source:** | v3=1 | a20=1
old Parallels install | v3=1 | a20=4
below checks that. | v3=2 | a20=1
**Only one NinjaTrader.** Parallels must not be running on the Mac. | v3=1 | a20=1
**stop here and tell me. Don't quit it yourself.** We restart this later. | v3=1 | a20=1
**Don't restart it.** | v3=1 | a20=1
NT8 on the **old Parallels VM** deleted its older log files | v3=1 | a20=1
Whether NT8 on Fusion does the same is unknown. | v3=1 | a20=1
Write down the **version** and the **Machine ID** exactly as shown. | v3=1 | a20=1
**Note the clock | v3=1 | a20=1
Write down the Windows time (bottom-right of the VM screen). | v3=1 | a20=0
Note the time on the **newest row** | v3=1 | a20=0
Don't type anything. The migration side reports that typed strings arrive garbled on this VM, while clicks and single keys work (M-026, REPORTED). | v3=1 | a20=1
**Note whether it appears. Don't act on it.** | v3=1 | a20=1
Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.** | v3=1 | a20=0
try once more, the same way | v3=1 | a20=0
Then stop. Don't troubleshoot, restart NT8, or try other routes. | v3=1 | a20=1
choose **No** or **Cancel** | v3=1 | a20=1
Leave NinjaTrader running as it was. Nothing else to undo. | v3=1 | a20=1
## What to send back | v3=1 | a20=1
Don't interpret it. Send it as copied. | v3=1 | a20=1
Nothing gets decided on this alone. | v3=1 | a20=1
send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking. | v3=1 | a20=1
That's a separate defect, reported to reproduce on Fusion, and still open. | v3=1 | a20=1
$ grep -n -i -F adapted-forms in a20
-- **no** setting
6:**Scope:** read the About box, read NinjaTrader's Settings window, look at the Connections list, read Windows' Date & time page. Write down what you see. **No** chart opened, **no** bar timestamps read, **no** Strategy
-- Write down the Windows time (bottom-right of the VM screen)
90:4. **Note the clocks.** Write down the Windows time (bottom-right of the VM screen) **and** the Mac's time (top-right of the Mac screen), read together. You'll compare them with each other, and against the Log tab lat
-- newest row
101:6. Write down the **time and message of the newest row**, and when you wrote it. Leave the tab showing.
-- copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that
96:**If a dialog or error box appears at any point:** copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.** Then stop and tell me.
-- try it once more, the same way
116:**If any step above didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes.
-- Step 3 below checks that
11:The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". That is the NinjaTrader 
```
```
$ NEGATIVE ARM: copy with two v3 safety clauses deleted
2
== 2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
ZERO | **No** setting
ZERO | Write down the Windows time (bottom-right of the VM screen).
ZERO | Note the time on the **newest row**
ZERO | Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.**
ZERO | try once more, the same way
== neg-copy.md
ZERO | **No** setting
ZERO | **stop here and tell me. Don't quit it yourself.** We restart this later.
ZERO | Write down the Windows time (bottom-right of the VM screen).
ZERO | Note the time on the **newest row**
ZERO | Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.**
ZERO | try once more, the same way
ZERO | send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking.
```

Five zeros are expected on every run: each is an adapted form, located in the second block above. The negative arm adds exactly the two deleted clauses as new zeros, so the check trips.

### E8. Final file: v3 phrase check, placeholder-token count, hash
```
$ v3 phrase check on final file, zero counts only
0 | **No** setting
0 | Write down the Windows time (bottom-right of the VM screen).
0 | Note the time on the **newest row**
0 | Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.**
0 | try once more, the same way
$ grep -c -i -w 'T[B]D' docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
0
$ shasum -a 256 docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md; wc -l
8885e50112f3c7fd1cff46f1b214a3189e821ef6a66d74f2f12dc37d512a319d  docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
     194
```

## Fix diffs (pre-fix copy → next version, `diff` output)

Pre-fix copies live in the session scratchpad (ephemeral), so the diffs are pasted here as the durable record. Hashes:
```
a8b3949471983fb7888c0d1ac4ada4a595dcdbeaa104450d94cbbfefa342aa9d  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dca9a339-0454-411e-ab12-e060aa87b73f/scratchpad/walkthrough-pre-fix.md
0b55b7eba174c1f8eda209827074089bf5dcac07a458e76048f2c82894e38678  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dca9a339-0454-411e-ab12-e060aa87b73f/scratchpad/walkthrough-pre-fix2.md
b9b30be41a05bd9cfcfc7d59b84569da7d730fa0920c0983a68710789cdd9f94  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dca9a339-0454-411e-ab12-e060aa87b73f/scratchpad/walkthrough-pre-fix3.md
```

### D1. Fix 1 (adversarial-1 F1–F15): 15 lines removed, 25 added
```
11c11
< The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". That is the NinjaTrader Help Guide's name, and the old install didn't show it (INFERRED). Fusion runs the same version per Amear's read this morning (8.1.7.2, REPORTED). Step 3 below checks that. Steps 7 and 9 check the menus themselves.
---
> **Why "old Parallels install"** (INFERRED from these dates): the Settings screenshot dates from 2026-09-29, and `DECISION_LOG.md` row 2026-09-29T15:45:00Z places that day's captures "during the live Parallels session". The Connections screenshot dates from 2026-07-24. Fusion's NT8 was installed 2026-10-19 (update 2 `:60`, REPORTED), after both.
12a13,16
> The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". Its source is migration update 1 `:87`, which calls it 'Tools > Options > General' (REPORTED, migration side). The old install's screenshot shows a window titled **Settings**, and its Tools menu had no 'Options' (capture notes, REPORTED). The two disagree. Step 7 covers both names. Fusion runs the same version per Amear's read this morning (8.1.7.2, REPORTED). Step 3 below checks that. Steps 7 and 9 check the menus themselves.
> 
> Pasted evidence for every VERIFIED item here: `docs/reports/2026-10-20-a20-manager-report.md`, Verification evidence section.
> 
23,24c27,28
< | P5 | Fusion NinjaTrader's own Time zone | **NOT YET KNOWN** (update 2 `:56`). Whether the old `Config.xml` is the one Fusion's NinjaTrader uses is also not known: the restore was reported faithful (update 2 `:62`), but the whole folder was not byte-checked (`:70`). **Step 8 observes it** |
< | P6 | NQCONT was imported as **US Eastern** | REPORTED, not observed: the session-52 card (`HANDOFF.md:106`) records "imported (ET, `Last`…)". The walkthrough Amear used told him to choose "US Eastern" (`2026-08-29-session52-nt8-voice-walkthrough-v2.md:144`), and an instruction isn't an observation. PRAXIS found no screenshot or quote of the import window's setting. The import was done on the **old Parallels install** |
---
> | P5 | Fusion NinjaTrader's own Time zone | **NOT YET KNOWN** (update 2 `:56`). Whether the old `Config.xml` is the one Fusion's NinjaTrader uses is also not known: the restore was reported faithful (update 2 `:25`), but the whole folder was not byte-checked (`:70`). **Step 8 observes it** |
> | P6 | NQCONT was imported as **US Eastern** | REPORTED, not observed: recorded by praxis-master in the session-52 card (`HANDOFF.md:106`), which records "imported (ET, `Last`…)". The original reporter isn't identified there. The walkthrough Amear used told him to choose "US Eastern" (`2026-08-29-session52-nt8-voice-walkthrough-v2.md:144`), and an instruction isn't an observation. PRAXIS found no screenshot or quote of the import window's setting (searched: `DECISION_LOG.md` 2026-08-29 rows, `HANDOFF.md`, the session-52 voice walkthroughs). The bead's cited sources, the session-42 r8j import report and the session-44 offset-correction reports, are about Phase-3 spec text and don't mention NQCONT. The import was done on the **old Parallels install** |
36c40
< **Rule for every row:** any mismatch goes to Amear as a decision. This walkthrough proposes **no fix**. ET session times are governed by F2 in `specs/SPEC_RUBRIC.md`, and a zone change is Amear's configuration decision.
---
> **Rule for every row:** any mismatch goes to Amear as a decision. This walkthrough proposes **no fix**. F2 in `specs/SPEC_RUBRIC.md` (FROZEN) states the breaker and flatten times in ET (11:30 ET, 15:00–18:00 ET, 16:00 ET), so the zone those times are read in is not a setting to change here. A zone change is Amear's configuration decision.
54c58
< | N2. "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" | The old install's zone came across (P2). Same clock as Eastern today. One hour apart from 2026-11-01 (P12, INFERRED) | **Amear decides, before 2026-11-01** (bead due 10-31) |
---
> | N2. "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" | The same label the old Parallels install displayed (P2). How it got here is NOT KNOWN: the old Config.xml stores no zone (P3). Same clock as Eastern today. One hour apart from 2026-11-01 (P12, INFERRED) | **Amear decides**, including when (open question 1). |
68c72
< | K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071) | Report it. **Don't disconnect.** Amear decides |
---
> | K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). On the old Parallels install, 'Simulated Data Feed' was set to connect at startup (old `Config.xml:18`, name at `:25`, VERIFIED, old install only). If that file is the one in use, a dot there is expected (INFERRED). Still Amear's call | Report it. **Don't disconnect.** Amear decides |
69a74,75
> | K7. The Connections menu doesn't open, or isn't in the menu bar | Can't tell | Stop. Send what you saw. No other route is tried |
> | K8. Simulation has no dot | Differs from update 2 `:67` (REPORTED connected) | Report it. Amear decides |
77c83,84
< | Any other difference | Not explained | Report it. Amear decides |
---
> | A difference of more than a minute or two | Not explained | Report it. Amear decides |
> | Mac clock not readable | Write 'not read' | Nothing on its own |
87c94
< 1. **Only one NinjaTrader.** Parallels must not be running on the Mac. If it is, **stop here and tell me. Don't quit it yourself.** We restart this later. (The old Parallels VM can still be started, and you started it yourself this month: M-031, REPORTED in the seat-close handover §4.)
---
> 1. **Only one NinjaTrader.** Parallels must not be running on the Mac. If it is, **stop here and tell me. Don't quit it yourself.** We restart this later. (You started the old Parallels VM yourself this month: M-031, REPORTED in the seat-close handover §4. On 10-19 it could still be run: update 2 `:89`, REPORTED.)
89,90c96,98
< 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. This morning you read 8.1.7.2, 64-bit, and Machine ID `DC242F5E75674D33D865C01BEF776371` (REPORTED by you, `HANDOFF.md:7`). The same values mean it's the same install. Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
< 4. **Note the clocks.** Write down the Windows time (bottom-right of the VM screen) **and** the Mac's time (top-right of the Mac screen), read together. You'll compare them with each other, and against the Log tab later.
---
> 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. This morning you read 8.1.7.2, 64-bit, and Machine ID `DC242F5E75674D33D865C01BEF776371` (REPORTED by you, `HANDOFF.md:7`). The same values mean it's the same machine. Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
> 4. If the VM fills the whole Mac screen, move the pointer to the very top edge to show the Mac's menu bar and clock. Don't click there.
>    **Note the clocks.** Write down the Windows time (bottom-right of the VM screen) **and** the Mac's time (top-right of the Mac screen), read together. You'll compare them with each other, and against the Log tab later.
102c110
< 7. In the Control Center menu bar, click **Tools**. The list opens. Click **Settings**, the **last** item. Take care: on the old Parallels install the items just above it were Client Dashboard and **Global Simulation Mode** (REPORTED, capture notes), and Global Simulation Mode is a switch (INFERRED). If there's no **Settings** but there is **Options**, click **Options**. If there's neither, press **Esc** once and stop (N5). If anything other than a window called **Settings** (or **Options**) appears, **stop and tell me. Don't undo it yourself.**
---
> 7. In the Control Center menu bar, click **Tools**. The list opens. Click **Settings**, the **last** item (on the old Parallels install, REPORTED, capture notes). If Settings is there but not last, click it anyway. Take care: on the old Parallels install the items just above it were Client Dashboard and **Global Simulation Mode** (REPORTED, capture notes), and Global Simulation Mode is a switch (INFERRED). If there's no **Settings** but there is **Options**, click **Options**. If there's neither, press **Esc** once and stop (N5). If anything other than a window called **Settings** (or **Options**) appears, **stop and tell me. Don't undo it yourself.** If you clicked and no Settings (or Options) window opened, **don't try again**. Stop and tell me which item you think you clicked.
106c114
<    - If you can't see the Time zone row, click the small **down arrow** at the right edge of the list a few times. If it still isn't there, stop (N5).
---
>    - If you can't see the **Time zone** row, don't scroll and don't click anything in the list. Click **Cancel**, check the window is gone, and stop (N5).
116c124
< **If any step above didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes.
---
> **If any step above (except step 7) didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes.
125c133
< 13. The **Date & time** page shows. Don't scroll. If you can't see the whole page, click the window's **maximise** button (the square, top right, left of the **X**). Write down exactly:
---
> 13. The **Date & time** page shows. Don't scroll. If you can't see the whole page, write 'not visible' for what's missing. Don't scroll, and don't resize the window. Write down exactly:
163a172,173
> Licence tooltip appeared (where): yes / no
> Dialog text (step, exact):
169c179
< - **Machine ID not `DC242F5E…6371`:** send it anyway. It means this isn't the install you checked this morning. You decide what follows.
---
> - **Machine ID not `DC242F5E…6371`:** send it anyway. It means this isn't the machine you checked this morning, or it was misread. You decide what follows.
```

### D2. Fix 2 (adversarial-2 findings 1–11, P11): 13 removed, 14 added
```
4c4
< **Written:** 2026-10-20 by praxis-worker for praxis-manager, bead `Praxis_build-a20`. First version for this bead, so it supersedes nothing. Modelled on walkthrough v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`), the only walkthrough graded PASS. Auditor grade appended below when given.
---
> **Written:** 2026-10-20 by praxis-worker for praxis-manager, bead `Praxis_build-a20`. First version for this bead, revised in place on 2026-10-20 after two adversarial passes (`2026-10-20-a20-adversarial-1.md`, `-adversarial-2.md`). Both fix diffs are pasted in the manager report. It supersedes no earlier walkthrough. Modelled on walkthrough v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`), the only walkthrough graded PASS. Auditor grade appended below when given.
13c13
< The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". Its source is migration update 1 `:87`, which calls it 'Tools > Options > General' (REPORTED, migration side). The old install's screenshot shows a window titled **Settings**, and its Tools menu had no 'Options' (capture notes, REPORTED). The two disagree. Step 7 covers both names. Fusion runs the same version per Amear's read this morning (8.1.7.2, REPORTED). Step 3 below checks that. Steps 7 and 9 check the menus themselves.
---
> The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". That wording matches PRAXIS's own 09-29 request (`2026-09-29-vm-migration-concerns.md:35`, item B2), echoed back in migration update 1 `:87` (lineage INFERRED). No observation of either install shows 'Options'. The old install's screenshot shows a window titled **Settings**, and its Tools menu ended in Settings (capture notes, REPORTED). Step 7 covers both names. Fusion runs the same version per Amear's read this morning (8.1.7.2, REPORTED). Step 3 below checks that. Steps 7 and 9 check the menus themselves.
33c33
< | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS at 13:35Z today (`/etc/localtime` reads `America/Toronto`; local time printed as EDT). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it at that time |
---
> | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS today (`/etc/localtime` reads `America/Toronto`; local time printed as EDT; output pasted in the manager report). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it at that time |
40c40
< **Rule for every row:** any mismatch goes to Amear as a decision. This walkthrough proposes **no fix**. F2 in `specs/SPEC_RUBRIC.md` (FROZEN) states the breaker and flatten times in ET (11:30 ET, 15:00–18:00 ET, 16:00 ET), so the zone those times are read in is not a setting to change here. A zone change is Amear's configuration decision.
---
> **Rule for every row:** any mismatch goes to Amear as a decision. This walkthrough proposes **no fix**. Related: F2 in `specs/SPEC_RUBRIC.md` (FROZEN, `:30-34`) states the breaker and flatten times in ET and is not settled. This walkthrough doesn't touch it. A zone change is Amear's configuration decision.
50c50
< | W5. No DST switch shown, or it's greyed out | Can't tell the DST state. Windows may hide or grey it for some zones or settings (INFERRED) | Send what's on screen. Amear decides whether to look again |
---
> | W5. No DST switch shown, or it's greyed out | Can't tell the DST state. Windows may hide or grey it for some zones or settings (INFERRED) | Send what's on screen. Amear decides whether to look again. If the DST switch is 'not visible', a screenshot of the page is the next request. Nothing else this run. |
51a52
> | W7. 'Set time automatically' **Off**, or 'Set time zone automatically' **On** | Differs from P4 (REPORTED). With 'Set time zone automatically' On, Windows may change the zone by itself (INFERRED) | Report it. **Amear decides.** |
62c63
< | N6. Can't read it (window didn't open, text cut off) | Can't tell | Send what you saw. Nothing gets decided on this alone |
---
> | N6. Can't read it (window didn't open, text cut off), or the Time zone row is off-screen | Can't tell | Send what you saw. Nothing gets decided on this alone |
72c73
< | K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). On the old Parallels install, 'Simulated Data Feed' was set to connect at startup (old `Config.xml:18`, name at `:25`, VERIFIED, old install only). If that file is the one in use, a dot there is expected (INFERRED). Still Amear's call | Report it. **Don't disconnect.** Amear decides |
---
> | K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). On the old Parallels install, `Config.xml:18` reads `ConnectOnStartup` `true` for 'Simulated Data Feed' (name at `:25`; VERIFIED, old install only). That this connects it at startup is INFERRED. Whether a dot here is acceptable is Amear's call (D-071 says no other connection) | Report it. **Don't disconnect.** Amear decides |
81c82
< | VM clock = Mac clock (to the minute) | Windows gives EDT today. **It cannot show Eastern versus fixed UTC−4** (P12) | Nothing on its own |
---
> | VM clock = Mac clock (within a minute or two) | Windows gives EDT today. **It cannot show Eastern versus fixed UTC−4** (P12) | Nothing on its own |
88c89
< **All agree** (W1 + N1 + P6's "US Eastern"): the **labels** agree. That's all it shows. It does **not** show that bar timestamps are right, because no chart was read (out of scope, by Amear's ruling). It doesn't show how NinjaTrader handles the 11-01 change (P13). And P6 is still only reported. Nothing gets decided on this alone.
---
> **All agree** (W1 + N1 + P6's "US Eastern"): the **labels** agree. That's all it shows. It does **not** show that bar timestamps are right, because no chart was read (out of scope, by your ruling as relayed, REPORTED). It doesn't show how NinjaTrader handles the 11-01 change (P13). And P6 is still only reported. Nothing gets decided on this alone.
114,115c115,116
<    - If you can't see the **Time zone** row, don't scroll and don't click anything in the list. Click **Cancel**, check the window is gone, and stop (N5).
<    - Now **click Cancel**. The three buttons at the bottom right read **OK · Cancel · Apply**: Cancel is the **middle** one, with OK right next to it on the left. Read the word before you click. **Never click OK. Never click Apply.**
---
>    - If you can't see the **Time zone** row, don't scroll and don't click anything in the list. Click **Cancel**, check the window is gone, and stop (N6).
>    - Now **click Cancel**. On the old Parallels install the three buttons at the bottom right read **OK · Cancel · Apply**, with Cancel in the **middle** and OK right next to it on the left (screenshot, above). On Fusion, **read the word before you click.** **Never click OK. Never click Apply.**
124c125
< **If any step above (except step 7) didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes.
---
> **If clicking Log (step 5) or Connections (step 9) didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes. **Any other step that didn't respond: stop and tell me.**
188c189
< 5. Do you want a bar-timestamp check later? You ruled it out of this one, because a chart requests bars and touches the NQCONT defect.
---
> 5. Do you want a bar-timestamp check later? You ruled it out of this one (your ruling relayed by praxis-master in the a20 dispatch, REPORTED; it isn't in `DECISION_LOG.md`). PRAXIS's reason: a chart requests bars and touches the NQCONT defect.
```

### D3. Fix 3 (adversarial-3 M2–M8): 9 removed, 11 added
```
30c30
< | P8 | Old install: Kinetick EOD was **not connected** (no dot, 2026-07-24), and set not to connect at startup | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
---
> | P8 | Old install: Kinetick EOD showed **no dot** on 2026-07-24 (VERIFIED, screenshot). No dot = not connected per the capture-note legend (REPORTED), and set not to connect at startup | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
33c33
< | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS today (`/etc/localtime` reads `America/Toronto`; local time printed as EDT; output pasted in the manager report). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it at that time |
---
> | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS at 14:09Z today (`/etc/localtime` reads `America/Toronto`; local time printed as EDT; output pasted in the manager report). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it at that time |
50c50,51
< | W5. No DST switch shown, or it's greyed out | Can't tell the DST state. Windows may hide or grey it for some zones or settings (INFERRED) | Send what's on screen. Amear decides whether to look again. If the DST switch is 'not visible', a screenshot of the page is the next request. Nothing else this run. |
---
> | W5. No DST switch shown, or it's greyed out | Can't tell the DST state. Windows may hide or grey it for some zones or settings (INFERRED) | Send what's on screen. Amear decides whether to look again. |
> | W5a. The DST switch is 'not visible' (off-screen; you didn't scroll) | Can't tell | Send what's on screen. Amear decides whether a scrolled look is the next run |
52c53
< | W7. 'Set time automatically' **Off**, or 'Set time zone automatically' **On** | Differs from P4 (REPORTED). With 'Set time zone automatically' On, Windows may change the zone by itself (INFERRED) | Report it. **Amear decides.** |
---
> | W7. 'Set time automatically' **Off**, or 'Set time zone automatically' **On** | 'Set time automatically' Off differs from P4 (REPORTED). P4 doesn't report 'Set time zone automatically'. With it On, Windows may change the zone by itself (INFERRED) | Report it. **Amear decides.** |
69c70
< | K1. Kinetick row present, **no dot** | Not connected. Matches the old install's setting, *if* that setting was restored (P8; INFERRED for Fusion) | Report it. Amear decides whether that's what he wants |
---
> | K1. Kinetick row present, **no dot** | Not connected (REPORTED legend: green dot = connected). Matches the old install's setting, *if* that setting was restored (P8; INFERRED for Fusion) | Report it. Amear decides whether that's what he wants |
82c83
< | VM clock = Mac clock (within a minute or two) | Windows gives EDT today. **It cannot show Eastern versus fixed UTC−4** (P12) | Nothing on its own |
---
> | VM clock = Mac clock (within a minute or two) | Windows is at UTC−4 today (if both clocks are synced). **It cannot show Eastern versus fixed UTC−4** (P12) | Nothing on its own |
97c98
< 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. This morning you read 8.1.7.2, 64-bit, and Machine ID `DC242F5E75674D33D865C01BEF776371` (REPORTED by you, `HANDOFF.md:7`). The same values mean it's the same machine. Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
---
> 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. Copy what the screen shows. Don't compare it with anything; PRAXIS compares it afterwards with this morning's read (`HANDOFF.md:7`, REPORTED by you). Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
103c104
< **Throughout:** click only with the mouse or trackpad. Don't type anything. The migration side reports that typed strings arrive garbled on this VM, while clicks and single keys work (M-026, REPORTED). **Never press Enter.** In a NinjaTrader window, Enter may press OK (INFERRED).
---
> **Throughout:** click only with the mouse or trackpad. **Click once.** Don't type anything. The migration side reports that typed strings arrive garbled on this VM, while clicks and single keys work (M-026, REPORTED). **Never press Enter.** In a NinjaTrader window, Enter may press OK (INFERRED).
119c120
< 10. **Read it. Don't click anything in it.** Clicking a name in this list connects or disconnects it (INFERRED), and so do the small "connect", "disconnect" and "configure" links. Keep the pointer still on the word **Connections**.
---
> 10. **Read it. Don't click anything in it.** Clicking a name in this list connects or disconnects it (INFERRED). Don't click the small 'disconnect' or 'configure' links either: what they do on Fusion hasn't been observed. Keep the pointer still on the word **Connections**.
170a172
> Retried (step 5 / step 9): yes / no, result:
```

### D4. Fix 4 (narrow pass §A4, plus the header disclosure): 5 lines changed, pre-fix4 sha256 `9ab80eb5…`
```
4c4
< **Written:** 2026-10-20 by praxis-worker for praxis-manager, bead `Praxis_build-a20`. First version for this bead, revised in place on 2026-10-20 after two adversarial passes (`2026-10-20-a20-adversarial-1.md`, `-adversarial-2.md`). Both fix diffs are pasted in the manager report. It supersedes no earlier walkthrough. Modelled on walkthrough v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`), the only walkthrough graded PASS. Auditor grade appended below when given.
---
> **Written:** 2026-10-20 by praxis-worker for praxis-manager, bead `Praxis_build-a20`. First version for this bead, revised in place on 2026-10-20 after four adversarial passes (`2026-10-20-a20-adversarial-1.md`, `-2.md`, `-3.md`, and a narrow fourth pass whose findings are in the manager report). Every fix diff is pasted in the manager report. It supersedes no earlier walkthrough. Modelled on walkthrough v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`), the only walkthrough graded PASS. Auditor grade appended below when given.
30c30
< | P8 | Old install: Kinetick EOD showed **no dot** on 2026-07-24 (VERIFIED, screenshot). No dot = not connected per the capture-note legend (REPORTED), and set not to connect at startup | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
---
> | P8 | Old install: Kinetick EOD showed **no dot** on 2026-07-24 (VERIFIED, screenshot). No dot = not connected is INFERRED from the capture-note legend, which marks only the green dot (`00-coworker-capture-notes.txt:53`, REPORTED), and set not to connect at startup | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
33c33
< | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS at 14:09Z today (`/etc/localtime` reads `America/Toronto`; local time printed as EDT; output pasted in the manager report). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it at that time |
---
> | P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS today: `/etc/localtime` reads `America/Toronto` and local time printed as EDT at 13:48Z; Fusion's `vmware-vmx` process was running at 14:09Z (both pasted in the manager report). That this is the Mac running Fusion is INFERRED from that process |
70c70
< | K1. Kinetick row present, **no dot** | Not connected (REPORTED legend: green dot = connected). Matches the old install's setting, *if* that setting was restored (P8; INFERRED for Fusion) | Report it. Amear decides whether that's what he wants |
---
> | K1. Kinetick row present, **no dot** | Not connected (INFERRED from the capture-note legend: green dot = connected). Matches the old install's setting, *if* that setting was restored (P8; INFERRED for Fusion) | Report it. Amear decides whether that's what he wants |
98c98
< 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. Copy what the screen shows. Don't compare it with anything; PRAXIS compares it afterwards with this morning's read (`HANDOFF.md:7`, REPORTED by you). Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
---
> 3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. Copy what the screen shows, character by character. PRAXIS compares it with this morning's read (`HANDOFF.md:7`, REPORTED by you). Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
```

### Verdict lines, as written by the adversarial workers
```
$ grep -n 'ADVERSARIAL VERDICT' 2026-10-20-a20-adversarial-1.md
204:ADVERSARIAL VERDICT: DEFECTS FOUND (3 blocking, 12 minor)
$ grep -n 'ADVERSARIAL VERDICT' 2026-10-20-a20-adversarial-2.md
196:ADVERSARIAL VERDICT: DEFECTS FOUND (1 blocking, 10 minor)
$ grep -n 'ADVERSARIAL VERDICT' 2026-10-20-a20-adversarial-3.md
228:ADVERSARIAL VERDICT: DEFECTS FOUND (0 blocking, 8 minor)
```

## Adversarial findings and disposition

### A1. Adversarial-1 (3 blocking, 12 minor). All fixed in D1, except where noted.
| # | Finding | Disposition |
|---|---|---|
| F1 B | N2 said "the old install's zone came across", but the old Config.xml stores no zone | Fixed: "How it got here is NOT KNOWN" |
| F2 B | Step 8's "small down arrow at the right edge" was the Time zone drop-down's own chevron (manager confirmed in E1) | Fixed: no scroll, no clicks; Cancel and stop |
| F3 B | N2 set a deadline ("before 2026-11-01") that is Amear's (S8) | Fixed: "Amear decides, including when" |
| F4 | Return form lacked v3's tooltip and dialog fields | Fixed |
| F5 | VERIFIED items lacked pasted output | Fixed: pointer to this report; evidence in §E |
| F6 | No basis given for "old Parallels install" | Fixed: dated basis, labelled INFERRED |
| F7 | "Options" was attributed to the Help Guide | Fixed in D1; corrected again in D2 (A2 #3) |
| F8 | Global Simulation Mode misclick looks like "didn't respond" | Fixed: step 7 says don't retry |
| F9 | "VM can still be started" was stale and unlabelled | Fixed: dated and REPORTED |
| F10 | Machine ID treated as "same install" | Fixed: "same machine" |
| F11 | Wrong restore citation `:62` | Fixed: `:25` (E6) |
| F12 | P6 didn't say who reported it, and its negative had no scope | Fixed |
| F13 | F2 citation claimed more than F2 says | **Manager modified the fix** (kept a precise citation, in D1). A2 #2 showed that was still a mechanism claim; reduced to "Related … doesn't touch it" in D2 |
| F14 | Full-screen VM hides the Mac clock; maximise | Fixed |
| F15 | Branch gaps (a–e) | Fixed (K7, K8, clock rows, K5 note, "last" labelled) |

### A2. Adversarial-2 (1 blocking, 10 minor). Fixed in D2.
| # | Finding | Disposition |
|---|---|---|
| 1 B | Step 8 stated the OK·Cancel·Apply order as a Fusion fact; its only source is the old-install screenshot. This is the v2-FAIL pattern, and adversarial-1 and the manager both missed it | Fixed: "On the old Parallels install … On Fusion, read the word before you click" |
| 2 | F2 clause still a mechanism claim | Fixed |
| 3 | "Options" lineage is PRAXIS's own B2 request, echoed (E5 shows `migration-concerns.md:35`; handover grep for Options = 0) | Fixed |
| 4 | Revised in place, header said "First version" | Fixed (header), updated again in D4 |
| 5 | Retry rule wider than v3 and conflicting with "stop" | Fixed: retry only steps 5 and 9 |
| 6 | Off-screen row routed to N5 | Fixed: N6 |
| 7 | K5 called a breach of D-071 "expected" | Fixed |
| 8 | No meaning for the two "Set … automatically" reads | Fixed: W7 |
| 9 | 1–2 min clock gap had no row | Fixed |
| 10 | Chart/bar exclusion attributed to Amear with a reason; not in DECISION_LOG (E5: grep of row 415 exit 1) | Fixed: ruling REPORTED as relayed; reason marked as PRAXIS's |
| 11 | "Don't scroll" may lose the DST datum | Fixed in D2, reworked in D3 (W5a) |

### A3. Adversarial-3 (0 blocking, 8 minor). Fixed in D3.
M1: this report didn't exist yet; it does now. M2: P11 timestamp; reworked in D4. M3: added "Click once.", the "Retried" field, and step 3 no longer prints the expected ID. M4: W7 corrected. M5: W5a row. M6: link behaviour unlabelled; now "hasn't been observed". M7: legend grade; reworked in D4. M8: "EDT" changed to "UTC−4 (if both clocks are synced)".

### A4. Narrow adversarial pass on D3 (0 blocking, 3 minor). Returned as a message (no file). Fixed in D4.
Its verdict line, verbatim: `ADVERSARIAL VERDICT: DEFECTS FOUND (0 blocking, 3 minor)`.
1. P11 merged two runs under one time: `/etc/localtime` was read at 13:48:40 UTC (E2), and `vmware-vmx` was observed at 14:09:29 UTC (E5). **Fixed:** both times stated separately.
2. P8 "no dot = not connected" was labelled REPORTED, but the legend marks only the green dot (E6, capture notes `:53`). **Fixed:** INFERRED (P8 and K1).
3. Step 3 "don't compare" contradicted the v3-carried bullets "Version not 8.1.7.2 … send it anyway" and "Machine ID not …". **Fixed in step 3.** The v3 bullets stay, because the survival rule binds them.

**Residual, disclosed:** D4 had no separate adversarial pass. Its five lines are the manager's own wording of A4's fixes plus the header count. The manager checked them by diff (D4) and by the final phrase check (E8).

## V. Removal diff against v3 (every v3 line, then its disposition in the final file)

| v3 line | Content | Final a20 |
|---|---|---|
| 3 | For Amear by hand, not Cowork | carried verbatim (L3) |
| 4 | Written/supersedes; prior versions kept; "Auditor grade appended below when given" | adapted (L4): no prior version; revision disclosed; grade line carried |
| 5 | Question it answers | adapted to the a20 question (L5) |
| 6 | Scope with explicit No's | adapted (L6): no chart, bar timestamps, Analyzer, setting, connection or orders; Cancel/Esc/X only; never OK/Apply/Enter. "No instrument picked" and "no backtest" were dropped as moot: nothing here opens an instrument picker or the Analyzer, and L183 says "Nothing here requests bars" |
| 7 | Menu path source, Parallels-install disclosure, version REPORTED, "Step 3 below checks that" | carried and strengthened (L7–13): both screenshots named as old install, with a dated basis; "Step 3 below checks that" verbatim |
| 11 | Only one NT8; "stop here and tell me. Don't quit it yourself." | carried verbatim (L96), plus a REPORTED note that Amear started Parallels this month |
| 12 | Don't restart; Parallels log purge REPORTED; Fusion unknown | carried verbatim (L97) |
| 13 | About box: version + Machine ID; X to close; owed per update 2 | carried (L98); "owed" note replaced, since Amear read both this morning (HANDOFF:7, REPORTED); confirm-closed check added (v4/v5 lesson) |
| 14 | Note the clock | carried and extended (L99–100, Mac clock added) |
| 18 | Log tab newest row | carried (L110–111) |
| 19 | Click once, don't type (M-026 REPORTED) | carried (L104, "Click once." restored in D3) |
| 20 | Wait 15 s; tooltip "Note whether it appears. Don't act on it." | wait dropped (Analyzer-specific); tooltip line carried (L108) |
| 21–24 | A/B/C outcomes; (B) copy text, Cancel/Close, **Never click OK** | (B) carried as the general dialog rule (L106), plus "stop and tell me"; A/C replaced by the read-specific branch tables |
| 25 | Log again after | carried (L124) |
| 27 | Retry once, then stop; no troubleshooting/restart/other routes | carried verbatim, scoped to steps 5 and 9 (L126); every other step: stop and tell me |
| 31 | Close via X; "save?" → No/Cancel; touch nothing first | adapted: confirm-closed checks after every close (L98, L118, L123, L142); save-prompt rule (L146) |
| 32 | Leave NT8 running as it was | carried verbatim (L147) |
| 36–47 | Send-back block | carried, with every v3 field kept or adapted (tooltip and dialog fields restored in D1; "Second try" → "Retried" in D3) |
| 51 | (A) meaning; Parallels Analyzer question REPORTED; NQCONT defect separate | Analyzer meaning dropped as out of scope; NQCONT-defect line carried (L183) |
| 52 | "Don't interpret it. Send it as copied." | carried verbatim (L179) |
| 53 | "Nothing gets decided on this alone." | carried (N6, the "All agree" paragraph) |
| 54 | Version not 8.1.7.2: "send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking." | carried verbatim (L181) |
| 58–66 | Auditor grade section of v3 | n/a: a20 is ungraded; L4 says the grade will be appended |

## S6 cross-block check

a20 is a read: no backtest (F3), no breaker or signal-path change (F1, F2), no account or order action (F4). It touches no other block's spec, and it records F2 as "Related … not settled … doesn't touch it" (L40). **Cross-block flag for Amear/master, not acted on:** DECISION_LOG row 365 (E4) records the CME US Index Futures RTH trading-hours template showing zone `Central` on the old install. The walkthrough doesn't read Trading Hours (out of scope). It is noted here because a zone question bears on F2's ET times.

## Files staged

The walkthrough was staged by `git add -- docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md`. This report is staged after it is written, by `git add -- docs/reports/2026-10-20-a20-manager-report.md`. Nothing else was added, unstaged or restaged.

**Before (baseline, captured at session start):**
```
118	0	DECISION_LOG.md
35	0	ISSUE_REGISTER.md
15	0	MANIFEST.md
1882	0	docs/reports/2026-08-06-session42-r8j-phase3-import.md
537	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
546	0	docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
195	0	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
301	0	docs/reports/2026-08-07-session44-r8j-offset-correction.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
```

**After staging the walkthrough, before this report existed:**
```
118	0	DECISION_LOG.md
35	0	ISSUE_REGISTER.md
15	0	MANIFEST.md
1882	0	docs/reports/2026-08-06-session42-r8j-phase3-import.md
537	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
546	0	docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
195	0	docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
301	0	docs/reports/2026-08-07-session44-r8j-offset-correction.md
194	0	docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
12	2	docs/specs/2026-08-08-ledger-compaction-spec.md
```

**Observer note:** this report's own numstat row can't be pasted inside itself, because the line count changes as the row is written. The final `git diff --cached --numstat`, including this file, is given in the manager's return message to the master.

**Orphans, disclosed, NOT staged (per the brief, stage only the two files):** `docs/reports/2026-10-20-a20-adversarial-1.md`, `-2.md` and `-3.md` are untracked. Two things cite them: the walkthrough header (L4) and this report. If they stay untracked, those citations dangle once committed. **Whether to stage them is the master's call.** The planned W1 report `2026-10-20-a20-worker1-research.md` was never created. Nothing was written under `.claude/agent-memory/`.

## Open questions that belong to Amear (not answered here)

1. If NT8's zone differs from Windows' (N2, N3): which zone should NT8 use, and by when?
2. If Windows isn't Eastern with DST On: keep it as found, or change it?
3. Kinetick EOD: is the state he sees the state he wants?
4. On 2026-08-29, did he set "US Eastern" in the import window himself? PRAXIS has an instruction and a master's card, but no observation (E3, E4).
5. Does he want a bar-timestamp check later (excluded from this unit by his relayed ruling)?
6. If NT8 follows Windows: keep following, or set the zone on purpose?

**For the master (ledger gap, not Amear's question):** the chart/bar-timestamp exclusion and its reason are in the dispatch brief only, not in DECISION_LOG row 415 (E5, grep exit 1). The bead's premise sources (the r8j reports) don't support "imported as ET" (E3). The bead text itself may need a correction note.

## Result

**Result: PASS.** This is the manager's stress-test outcome under the report contract, and it is not an audit grade. The walkthrough survived three full adversarial passes and one narrow pass. Every blocking finding (3 + 1) and every minor finding was fixed (one, F13, with a modified fix that was later reduced). The v3 removal diff is complete. The staged carried set is unchanged. Disclosed residuals: D4 had no separate adversarial pass; three adversarial files are unstaged orphans; and W1's research report was never produced. The walkthrough is **not cleared for Amear** until the master's auditor grades it.
