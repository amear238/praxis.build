# a20 adversarial 1: Fusion time-zone and Kinetick walkthrough

**Task:** break `docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md` (bead `Praxis_build-a20`), 181 lines as read 2026-10-20.
**Mode:** ADVERSARIAL. Run by praxis-worker on 2026-10-20. Nothing edited, staged or unstaged. This is the only file written.
**Criterion:** S1, S2, S8, S9 note R3, and the survival rule (HANDOFF.md 1-40: carry over every v3 safety and provenance line, or justify dropping it).

## Process log

1. Read the artifact (`cat -n`, 181 lines), v3 (66 lines), HANDOFF 1-40 and 100-112, and the auditor grades at the foot of v2, v4 and v5. v1 has no grade section; the HANDOFF table gives its withdrawal reason.
2. Viewed all three cited images with the Read tool.
3. Re-read every cited text source at the cited line: capture notes, update 1, update 2, DECISION_LOG row 393, seat-close handover §4 and §7, voice walkthrough :136-171, the rescue Config.xml files, the r8j reports, the bead, and SPEC_RUBRIC F2.
4. Re-measured P7, P11 and P12 myself.
5. Did a line-by-line removal diff of v3 against the artifact (table at the end).

## Evidence (pasted)

```
$ ls -l /etc/localtime; date; date -u; cal 11 2026 | head -4; pgrep -fl vmware-vmx | cut -c1-150
lrwxr-xr-x  1 root  wheel  41 Mar 16  2026 /etc/localtime -> /var/db/timezone/zoneinfo/America/Toronto
Tue 20 Oct 2026 09:52:23 EDT
Tue 20 Oct 2026 13:52:23 UTC
   November 2026
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
20984 /Applications/VMware Fusion.app/Contents/Library/vmware-vmx ... version=26.0.1 ...
$ TZ=America/Toronto date -j -f "%Y-%m-%d %H:%M" "2026-11-01 12:00" "+%Z %z"
EST -0500
```
P11 and P12 reproduce.

```
$ (rescue copies) ls -la; shasum -a 256; sed -n '203p;34p'
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 files/NinjaTrader 8/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  files/NinjaTrader 8/Config.xml
      <ConnectOnStartup>false</ConnectOnStartup>
      <TimeZoneInfoSerializable />
-rw-r--r--@ 1 admin  staff  16879 Aug 29 12:00 files/NinjaTrader 8-full/Config.xml
7a040a1106eb6c674b0cb17c70132cdfc6cf64453dcc8f564f63514feee0edf6  files/NinjaTrader 8-full/Config.xml
      <ConnectOnStartup>false</ConnectOnStartup>
      <TimeZoneInfoSerializable />
$ grep -n "<Name>|Options>$" Config.xml (full)
16:    <SimulatorOptions>          (line 18: <ConnectOnStartup>true</ConnectOnStartup>)
25:      <Name>Simulated Data Feed</Name>
32:    <KinetickOptions>           (line 34: <ConnectOnStartup>false</ConnectOnStartup>)
41:      <Name>Kinetick – End Of Day (Free)</Name>
```
P3 and P8 reproduce. Line 34 is inside `KinetickOptions`.

```
$ cd ~/VM-Rescue-2026-09-29/files/"NinjaTrader 8-full"/db/minute/NQCONT && find . -type f | wc -l; ... awk sum
    1710
16608933
```
The P7 expected figures reproduce.

```
$ ls -la ~/VM-Rescue-2026-09-29/screenshots/
-rw-------@ 1 admin  staff  472306 Sep 29 11:19 nt8-general-time-zone.png
-rw-------@ 1 admin  staff  182342 Sep 29 11:19 windows-time-zone.png
$ grep -n ... rescue.ps1
8:$U     = 'C:\Users\amearbani-ahmad'
```

**Images, as seen.**
- `nt8-general-time-zone.png`: an NT8 window titled "Settings". The categories are General (highlighted), Trading, Strategies, Automated trading interface, Market data. The Time zone row reads "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" in a **drop-down box with a ▼ chevron at its right edge**. Language, Skin and Symbology are also drop-downs with right-edge ▼ chevrons. The Properties pane's own scroll arrows are a tiny ▲▼ pair at the **top**-right of the Properties header. The buttons at the bottom right are OK, Cancel, Apply, with Apply greyed. The taskbar clock reads 11:15 AM 9/29/2026.
- `windows-time-zone.png`: the Windows 11 Settings "Time & language" page, account "amearbani-ahmad, Local Account", 11:14 AM, Tuesday September 29 2026. Time zone "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan", Region United States. **No DST switch is visible** on this page.
- `20-connections-menu.png`: the Connections list reads Kinetick – End Of Day (Free), Playback, Simulated Data Feed (green dot, "disconnect" link), Simulation. Below them is a "configure" link.

## Findings

### F1. BLOCKING (S2): the N2 meaning is contradicted by the walkthrough's own P3
- **Line 54:** `| N2. "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" | The old install's zone came across (P2). ...`
- **Line 21 (P3):** the old `Config.xml` has an **empty** zone field, `<TimeZoneInfoSerializable />`. I re-read this at line 203 of both copies (pasted above). The file is dated Aug 29 12:00, before the 09-29 screenshot. So the old install's NT8 showed Georgetown while storing **no** explicit zone, which is the walkthrough's own "follow Windows" inference.
- **Why it breaks.** Restoring that Config.xml would carry across "empty", not "Georgetown". If Fusion's NT8 shows Georgetown while Windows shows Eastern, the old install's setting did **not** simply "come across". The cause is unknown. The pre-registered meaning states a causal claim with no label, and the table's own premise contradicts it. Amear's decision would rest on this row.
- **Smallest fix:** "The same label the old install displayed (P2). How it got here is NOT KNOWN: the old Config.xml stores no zone (P3)."

### F2. BLOCKING (state-change hazard): step 8's fallback sends Amear toward a drop-down arrow
- **Line 106:** `If you can't see the Time zone row, click the small **down arrow** at the right edge of the list a few times.`
- **Line 105:** `**Don't click that box or any other box, tick or slider.**`
- **Evidence (image):** in `nt8-general-time-zone.png` the most prominent "small down arrows at the right edge" are the ▼ chevrons of the drop-down boxes: Time zone, Language, Skin and Symbology. The list's own scroll arrows are a tiny ▲▼ pair at the **top** right of the Properties header, not at its foot.
- **Why it breaks.** Read literally, the fallback asks for a click on the Time zone drop-down's own arrow. That opens the box this walkthrough exists to read, and a following click selects a new zone. It contradicts line 105 one bullet earlier. "Cancel discards it" is INFERRED and untested.
- **Smallest fix:** remove the fallback. "If you can't see the Time zone row, don't scroll or click anything in the list. Click Cancel, check the window is gone, and stop (N5)."

### F3. BLOCKING (S8): N2 answers half of open question 1, and that half rests on P13
- **Line 54:** `| **Amear decides, before 2026-11-01** (bead due 10-31) |`
- **Line 174:** `1. ... which zone should NinjaTrader use, and should that be settled before 2026-11-01?`
- **Why it breaks.** The table sets the deadline that open question 1 says is Amear's to set ("not answered here", line 172). The urgency also assumes that a label mismatch changes NT8's behaviour after 11-01. That is P13, which line 31 says is "INFERRED only ... No conclusion below depends on it."
- **Smallest fix:** "**Amear decides**, including when (open question 1)."

### F4. MINOR (survival): two v3 return fields dropped without justification
- v3 `:42` `Licence tooltip appeared: yes / no` and v3 `:43` `Dialog text (if B):` are not in the artifact's return block (lines 141-164).
- The artifact still tells Amear to note the tooltip (line 98) and copy any dialog text (line 96). The form has nowhere to put either.
- **Fix:** add `Licence tooltip appeared (where): yes / no` and `Dialog text (step, exact):`.

### F5. MINOR (S1): "VERIFIED by PRAXIS today" claims carry no pasted output
- P1, P2, P3, P7, P8 and P11 (lines 19-29) say "VERIFIED by PRAXIS today/at 13:35Z", with no command output in the file and no companion build report. `ls docs/reports | grep a20` lists only the walkthrough and this file.
- I re-ran P3, P7, P8, P11 and P12, and all reproduce (pasted above). The facts hold; the evidence isn't in the report.
- **Fix:** add a short evidence appendix, or a pointer to one.

### F6. MINOR (S2): the "old Parallels install" attribution of the 09-29 screenshots has no stated basis
- **Line 7:** `two screenshots from the **old Parallels install**`.
- The walkthrough gives no reason. A basis does exist. `rescue.ps1:8` reads `$U = 'C:\Users\amearbani-ahmad'`, and the Windows screenshot shows account "amearbani-ahmad". Fusion's NT8 folder is `C:\Users\amear\...` (update 2 `:97`). Fusion's NT8 was installed 2026-10-19 (update 2 `:60`), after 09-29. DECISION_LOG row 393 has `WHEN: 2026-09-29, during the live Parallels session`.
- **Fix:** cite one of these, labelled.

### F7. MINOR (S2/R3): line 11 attributes the bead's "Options" to the Help Guide, and the real source isn't cited
- **Line 11:** `The bead says "Tools, Options, General". That is the NinjaTrader Help Guide's name ... (INFERRED)`.
- The traceable source is update 1 `:87`: `NT8's own time-zone setting (Tools > Options > General), which on the old install was the same fixed UTC−4 zone (VERIFIED, M5 report)`. That source labels the "Options" path VERIFIED for the old install, and the screenshot shows "Settings". The walkthrough neither cites nor reconciles the conflict.
- **Fix:** cite update 1 `:87` as the bead's source and note the conflict with the screenshot.

### F8. MINOR (hazard): Global Simulation Mode is a silent toggle, and the stop rule doesn't catch it
- **Line 102:** `If anything other than a window called **Settings** (or **Options**) appears, **stop and tell me.**`
- **Line 116:** `**If any step above didn't respond:** try it once more, the same way.`
- A misclick on Global Simulation Mode, the item just above Settings on the old install, opens **no** window (INFERRED: it toggles). So the "anything appears" stop doesn't fire. To Amear it looks like "didn't respond", and line 116 sends him back into the same menu. On the old install it was greyed and licence-gated (capture notes `:45-46`). Its state on Fusion is unknown.
- **Fix:** "If you clicked and no Settings window opened, don't retry. Stop and tell me which item you think you clicked."

### F9. MINOR (S2, stale): line 87 says "The old Parallels VM can still be started" with no label
- The source is update 2 `:89` (10-19). Since then Amear ruled that A1, A2 and A4-A10 can be deleted (handover §4). `ls -d "/Volumes/Back Up 2T/Windows 11.pvm"` now returns `No such file or directory`. `/Volumes/PVM-Backup/2026-10-11` and `/Applications/Parallels Desktop.app` are still present.
- The step-1 instruction itself is unaffected.
- **Fix:** "(The old Parallels VM could still be started on 10-19, update 2 `:89`; REPORTED.)"

### F10. MINOR (S2): a Machine ID match is read as "same install"
- **Line 89:** `The same values mean it's the same install.`
- **Line 169:** `It means this isn't the install you checked this morning.`
- The Machine ID identifies the machine. A reinstall on the same VM would keep it (INFERRED), and a mismatch could also be a misread.
- **Fix:** "same machine", and "isn't the machine, or was misread".

### F11. MINOR (citation): P5 cites update 2 `:62` for "the restore was reported faithful"
- `:62` records the restore **choice**, "(a) Faithful, Amear's call". The completion is `:25` ("installed and restored by route (a), faithful") and `:70`.
- **Fix:** cite `:25`.

### F12. MINOR (S2): P6 doesn't say who reported, and its negative has no scope
- **Line 24:** `REPORTED, not observed: the session-52 card ...`. It doesn't say who relayed "ET" (the brief's label rule asks for who and where). It also says `PRAXIS found no screenshot or quote of the import window's setting` without saying what was searched.
- The voice walkthrough `:171` told Amear: `**Say out loud:** the time zone you set`. A spoken report may therefore exist in the session-52 transcript. My grep of DECISION_LOG rows 345-361 found no "Eastern" or "time zone".
- The r8j reports named in the brief do **not** support the ET import at all. Their only "UTC" hits are inside the word "outcome" or a date-format note (grep pasted in the process notes below). The walkthrough rightly doesn't cite them.
- **Fix:** "recorded by praxis-master in the session-52 card. The original reporter is not identified. Searched: DECISION_LOG 2026-08-29 rows, HANDOFF."

### F13. MINOR (R3): line 36 cites F2 for something F2 doesn't contain
- **Line 36:** `ET session times are governed by F2 in specs/SPEC_RUBRIC.md`.
- F2 (`SPEC_RUBRIC.md:30-41`) is a FROZEN item about the conflict between breakers #4 and #5 and the 16:00 flatten. It says nothing about time-zone settings.
- **Fix:** drop the clause. "A zone change is Amear's configuration decision" stands on its own.

### F14. MINOR (practicality): two problems if the VM is full-screen in Fusion
- **Line 90**, `the Mac's time (top-right of the Mac screen)`: in macOS full screen the menu bar and clock are hidden until the pointer reaches the top edge (INFERRED).
- **Lines 125 and 132**, maximise and then the X at top right: a maximised window's X then sits where the macOS menu bar slides down (INFERRED).
- **Fix:** add one line: "If the VM fills the whole Mac screen, move the pointer to the very top to show the Mac clock. Don't click there."

### F15. MINOR (branch gaps)
- (a) No K row for "the Connections menu didn't open or isn't in the menu bar". Only line 116 and "Anything else" cover it.
- (b) No clock row for "Mac clock not readable". Also, a one-minute skew at a minute boundary falls under "Any other difference: Not explained", which sends noise to Amear.
- (c) No K row for "Simulation has no dot".
- (d) Old `Config.xml:18` has `SimulatorOptions` with `ConnectOnStartup` `true`. If the old Config is the one in use, a green dot on "Simulated Data Feed" (a K5 hit) is the predictable result. Flagging that would also bear on P5.
- (e) Step 7 says `Click **Settings**, the **last** item`. "Last" is an old-install position given without a label, and there is no branch for "Settings exists but isn't last". The Options fallback goes into a window whose button order (line 107) is evidenced only for "Settings".

### Checked and holding (tried, no break)
- P1, P2, P3, P4 (`:55`), P7, P8, P9 (`:67`), P10 (update 1 `:48`), P11, P12 and P14 (`:58`) say what is claimed at the cited line, with the right label.
- P2's "previously REPORTED" matches row 393 (`RECORDED, NOT INTERPRETED. These are migration-agent REPORTS`).
- HANDOFF `:7` (Machine ID) and `:106` (`imported (ET, \`Last\`...`) match.
- Voice walkthrough `:144` reads `US Eastern`.
- Seat-close §4 says "Amear started the old Parallels VM himself (M-031)".
- Migration-side VERIFIED items (Config.xml, NQCONT figures) were re-read rather than relayed.
- No branch proposes a fix. K2 and K5 say "Don't disconnect". Every window closes with Cancel, Esc or X, each followed by a confirm-closed check (lines 89, 108, 113, 132).
- Never OK, never Apply, never Enter (lines 6, 94, 107). The Windows page is read-only and avoids Sync now and Change (line 120).
- The branch tables come before the reads, and both N and W have "not where it says" rows (N5, W6) and "can't tell" rows (N6, W5).

## v3 removal diff (v3 line, then disposition in a20)

| v3 | Content | a20 |
|---|---|---|
| 1 | Title | adapted (L1) |
| 3 | For Amear by hand, not Cowork | carried verbatim (L3) |
| 4 | Written/supersedes, both stay on disk unedited, grade appended when given | adapted (L4). First version, so "supersedes" doesn't apply. Grade line carried |
| 5 | Question | adapted (L5) |
| 6 | Scope: no instrument picked, no backtest, no settings changed, no orders | adapted (L6): no chart, no bar timestamps, no Analyzer, no setting, no connection, no orders. "No instrument picked" is implied by "no chart" and L170 "Nothing here requests bars". Acceptable |
| 7 | Menu path source; screenshots from the **old Parallels install**; same version REPORTED; "Step 3 below checks that" | carried and adapted (L7-11). Source now Amear's read this morning (HANDOFF `:7`) |
| 11 | Only one NT8; "stop here and tell me. Don't quit it yourself." We restart later | **carried verbatim** (L87), plus a parenthetical (see F9) |
| 12 | Don't restart NT8; old Parallels VM log purge (REPORTED); Fusion unknown | **carried verbatim** (L88) |
| 13 | About box, write version and Machine ID, close with X; "update 2 lists both as still owed" | adapted (L89). The owed note is replaced by this morning's REPORTED values, which is justified since they are now read. Confirm-closed check added. New overclaim, see F10 |
| 14 | Note the clock, compare with Log later | carried and extended (L90, Mac clock added) |
| 18 | Log tab, newest row, leave tab showing | carried (L100-101) |
| 19 | Click once, don't type; M-026 REPORTED | carried (L94) |
| 20 | Wait 15 s; licence tooltip "Note whether it appears. Don't act on it." | the wait is Analyzer-specific and doesn't apply. Tooltip **carried** (L98) |
| 23 | (B) dialog: copy text or screenshot; Cancel, or Close if it's the only button; **Never click OK** | carried (L96), plus "stop and tell me" |
| 25 | Log again after, copy new rows | carried (L114) |
| 27 | Retry once, same way; then stop; no troubleshooting, restart or other routes | carried verbatim (L116). Interacts badly with a silent toggle (F8) |
| 31 | Close via X; "save?" means No or Cancel; don't touch anything first | adapted (L136, L105, L108, L132) |
| 32 | Leave NT8 running | carried (L137) |
| 37-38 | Return: version, Machine ID | carried (L143-144) |
| 39-40 | Clock at start; newest Log row | carried (L146-148) |
| 41 | Result A/B/C | Analyzer-specific, so replaced by the read fields |
| **42** | **Licence tooltip appeared: yes / no** | **DROPPED, no justification (F4)** |
| **43** | **Dialog text (if B)** | **DROPPED, no justification (F4)** |
| 44 | New Log rows after | carried (L155) |
| 45 | Second try (if C) | adapted ("Anything that didn't respond", L161) |
| 46 | Screenshot taken | carried (L163) |
| 51 | (A) meaning; Parallels question REPORTED; NQCONT defect separate, reported on Fusion, open | NQCONT line **carried** (L170). The Analyzer meaning doesn't apply |
| 52 | "Don't interpret it. Send it as copied." | carried (L166) |
| 53 | "Nothing gets decided on this alone." | carried (L58, L78, L81) |
| 54 | Version not 8.1.7.2: "send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking." | **carried verbatim** (L168) |

Process note for F12: `grep -n -i "eastern\|time zone\|timezone\|UTC"` over the r8j files returned only `...correction.md:62:| # | id | mode | outcome |` and `...phase3-import.md:54/60/771/962/1445` (the words "outcomes" and "Outcome", and a `%SZ` format note). None mentions an ET import.

## Result

ADVERSARIAL VERDICT: DEFECTS FOUND (3 blocking, 12 minor)
