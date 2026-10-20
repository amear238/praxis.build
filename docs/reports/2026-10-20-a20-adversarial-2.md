# a20 adversarial 2 (re-check): Fusion time-zone and Kinetick walkthrough

**Task:** re-check `docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md` (191 lines, mtime Oct 20 09:58, sha256 `0b55b7eb…8e38678`) after the fix for adversarial-1 F1–F15. Bead `Praxis_build-a20`.
**Mode:** ADVERSARIAL. Run by praxis-worker on 2026-10-20. Nothing edited, staged or unstaged. This is the only file written.
**Criterion:** S1, S2, S8, S9 note R3, and the survival rule against v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`).

## Process log

1. `cat -n` of the current file, the pre-fix copy (scratchpad, 181 lines, sha256 `a8b39494…42aa9d`), adversarial-1 and v3.
2. `diff pre-fix current`. There are 15 hunks, and each was checked below (§2).
3. Re-read every new citation at its cited line: update 2 `:25 :27 :55 :56 :60 :62 :67 :70 :89`, update 1 `:1-12 :48 :87 :105`, DECISION_LOG rows 393 / 402 / 415, the old `Config.xml` lines 14-45 and 203, `SPEC_RUBRIC.md:28-42`, `HANDOFF.md:7`, `:106` and its card headers, the capture notes `:30-50`, seat-close handover §4 / §7, the voice walkthrough `:144`, and the bead text (`bd show`).
4. Viewed all three images with the Read tool: `nt8-general-time-zone.png`, `windows-time-zone.png` and `20-connections-menu.png`.
5. Did a fresh attack on the whole file (§3).

## Evidence (pasted)

```
$ ls -la@ ~/VM-Rescue-2026-09-29/screenshots/ ; stat -f "%N birth=%SB mod=%Sm" ...
-rw-------@  1 admin  staff  472306 Sep 29 11:19 nt8-general-time-zone.png
-rw-------@  1 admin  staff  182342 Sep 29 11:19 windows-time-zone.png
/Users/admin/VM-Rescue-2026-09-29/screenshots/nt8-general-time-zone.png birth=Sep 29 11:19:29 2026 mod=Sep 29 11:19:29 2026
docs/reference/assets/nt8-2026-07-24/20-connections-menu.png birth=Jul 24 09:25:01 2026 mod=Jul 24 09:25:01 2026
9717d93 2026-07-24 09:28:54 -0400 docs(8yb): NT8 8.1.7.2 Windows layout + workflow reference
```
The image's own taskbar clock reads `11:15 AM 9/29/2026`, so line 8's "taken 11:15" matches the image. The file mtime is 11:19.

```
$ sed -n '14,45p;200,205p' ".../files/NinjaTrader 8/Config.xml" | cat -n   (row n = file line n+13)
      5	      <ConnectOnStartup>true</ConnectOnStartup>        -> file :18  (inside SimulatorOptions)
     12	      <Name>Simulated Data Feed</Name>                  -> file :25
     21	      <ConnectOnStartup>false</ConnectOnStartup>       -> file :34  (inside KinetickOptions)
     28	      <Name>Kinetick – End Of Day (Free)</Name>         -> file :41
$ grep -n "TimeZone" Config.xml
203:      <TimeZoneInfoSerializable />
```
K5's `:18` / `:25` and P3's `:203` are correct.

```
U2:25: **NinjaTrader 8.1.7.2 is installed and restored by route (a), faithful** (D-068).
U2:60: | 4 | NT8 8.1.7.2 from the saved MSI; ... Install REPORTED (... 8.1.7.2, status 0, 2026-10-19 13:03Z) ... **Machine ID: NOT YET KNOWN** |
U2:67: | 13 | ... After sign-in NT8 connected by itself to **"Simulation"** ... Amear accepted it on condition: no orders, no other connection (D-071). Still connected after the restore | ... Kinetick EOD: NOT YET KNOWN |
U2:89: - **Who started it:** NOT YET KNOWN. Amear said at 14:29Z that Parallels "still works when I log in" ... So the old VM can still be run today.
U1:87: ... NT8's own time-zone setting** (Tools > Options > General), which on the old install was the same fixed UTC−4 zone (VERIFIED, M5 report) ...
```
All of these match the walkthrough's use of them. U2:89's "Who started it: NOT YET KNOWN" is superseded by the later seat-close handover §4 `:28`: "**Amear started the old Parallels VM himself** (M-031)". The handover's §4 heading is at `:25`, so "§4" is correct.

```
$ bd show Praxis_build-a20
  ... Read NT8's own time zone (Tools, Options, General) and Kinetick EOD connection status.
  Change nothing; any mismatch goes to Amear. Source: seat-close handover 2026-10-20 §7 step 3; DECISION_LOG 2026-10-20.
$ grep -n "Options" docs/reports/2026-10-20-seat-close-handover.md      -> (no output)
$ grep '^- \[2026-10-20' DECISION_LOG.md | grep -ci 'options'          -> 1  (row 397: "the optional run2 re-backup question", not a menu)
$ grep -rln "Tools, Options" docs/ HANDOFF.md STATUS.md
docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
docs/reports/2026-09-29-vm-migration-concerns.md
docs/reports/2026-10-20-a20-adversarial-1.md
$ grep -n "Tools, Options" docs/reports/2026-09-29-vm-migration-concerns.md
35:| **B2** | **Record four settings as screenshots:** (1) Windows time zone (Settings, Time & language); (2) NT8 time zone (Tools, Options, General); (3) Merge Policy (Tools, Options, Market Data); ...
```

```
$ sed -n '30,34p' specs/SPEC_RUBRIC.md
### F2 — Session-flat time vs. breakers #4 and #5
**Criterion.** One governing rule, written down, resolving: breaker #4 closes
positions at 11:30 ET; breaker #5 disables everything 15:00–18:00 ET;
Deviation B flattens at 16:00 ET. State what happens to an open position at
$ grep -n "^\- \[2026-08-29" DECISION_LOG.md | grep -i "eastern\|time zone\|ET,"   (excerpt)
... **So "the expected flat-by-16:00 Eastern session close" is not an established requirement — it is one of the three candidates F2 was frozen to adjudicate.**
```

```
$ for r in HEAD ":0"; do git show $r:DECISION_LOG.md | grep -c '2026-09-29T15:45:00Z'; done; grep -c '2026-09-29T15:45:00Z' DECISION_LOG.md
HEAD: 0
:0: 0
worktree: 3
$ wc -l DECISION_LOG.md ; grep -n -i "bar timestamp\|bar-timestamp\|no chart" DECISION_LOG.md   (rows 395-415)
     415 DECISION_LOG.md
     (no ruling excluding charts or bar timestamps; row 415 records scope = "Add the Windows zone")
```

```
$ ls -l /etc/localtime; date; date -u; TZ=America/Toronto date -j -f "%Y-%m-%d %H:%M" "2026-11-01 12:00" "+%Z %z"; ... "2026-10-31 12:00" ...; pgrep -fl vmware-vmx
lrwxr-xr-x  1 root  wheel  41 Mar 16  2026 /etc/localtime -> /var/db/timezone/zoneinfo/America/Toronto
Tue 20 Oct 2026 10:06:54 EDT
Tue 20 Oct 2026 14:06:54 UTC
EST -0500
EDT -0400
20984 /Applications/VMware Fusion.app/Contents/Library/vmware-vmx -E en -s vmx.stdio.keep=
```
P11 and P12 reproduce.

**Images, as seen by me.** `nt8-general-time-zone.png` shows a window titled "Settings" with General highlighted. Time zone is a drop-down reading Georgetown. Buttons: **OK, Cancel, Apply** (Apply greyed). Below General's rows is a Sounds group, and each sound box has a small **x** clear button at its right edge, plus a Volume slider. `windows-time-zone.png` shows the Time & language page with account amearbani-ahmad, 11:14 AM, Georgetown, and no DST switch on that page. `20-connections-menu.png` lists Kinetick – End Of Day (Free) with no dot, Playback, Simulated Data Feed with a green dot and "disconnect", Simulation, and "configure".

## §1. F1–F15: are they resolved?

| F | Status | Current line, quoted |
|---|---|---|
| F1 | RESOLVED | `:58` "The same label the old Parallels install displayed (P2). How it got here is NOT KNOWN: the old Config.xml stores no zone (P3)." |
| F2 | RESOLVED | `:114` "If you can't see the **Time zone** row, don't scroll and don't click anything in the list. Click **Cancel**, check the window is gone, and stop (N5)." (See finding 6 on N5's meaning.) |
| F3 | RESOLVED | `:58` "**Amear decides**, including when (open question 1)." |
| F4 | RESOLVED | `:172` "Licence tooltip appeared (where): yes / no", `:173` "Dialog text (step, exact):" |
| F5 | PARTIAL | `:15` points to the manager report. That report doesn't exist yet, which is expected per the brief. K5 adds a **new** VERIFIED item (Config `:18`/`:25`) that it must also cover. See §4 |
| F6 | RESOLVED | `:11` "**Why "old Parallels install"** (INFERRED from these dates) …". The basis checks out (file dates above, U2:60). Caveat in finding 4: the cited row is worktree-only |
| F7 | PARTIAL | `:13` "Its source is migration update 1 `:87` …" is unlabelled, and it is not the traceable origin. See finding 3 |
| F8 | RESOLVED | `:110` "If you clicked and no Settings (or Options) window opened, **don't try again**." and `:124` "(except step 7)" |
| F9 | RESOLVED | `:94` "On 10-19 it could still be run: update 2 `:89`, REPORTED." |
| F10 | RESOLVED | `:96` "same machine". `:179` "isn't the machine you checked this morning, or it was misread" |
| F11 | RESOLVED | `:27` "(update 2 `:25`)" |
| F12 | RESOLVED | `:28` "The original reporter isn't identified there … (searched: …)" |
| F13 | NOT RESOLVED | Adversarial-1 asked for the clause to be dropped. The fix rewrote it into a stronger inference instead. See finding 2 |
| F14 | RESOLVED | `:97` full-screen pointer line. `:133` "Don't scroll, and don't resize the window" (the maximise step is gone) |
| F15 | PARTIAL | (a) K7 `:74`, (c) K8 `:75`, (d) K5 `:72` and (e) `:110` are resolved. (b) is partial: `:81` "to the minute" against `:83` "more than a minute or two" leaves a 1-to-2-minute difference with no row (finding 9) |

## §2–§3. Findings (regression hunt + fresh attack)

### 1. BLOCKING (S2, old-install evidence stated as Fusion fact, v2-FAIL precedent): step 8 gives the Settings button layout as present-tense fact
- **Line 115:** `Now **click Cancel**. The three buttons at the bottom right read **OK · Cancel · Apply**: Cancel is the **middle** one, with OK right next to it on the left.`
- **Evidence:** the only source for this layout is the 09-29 **old Parallels** screenshot (`:8`). I viewed it, and it does read OK, Cancel, Apply. No Fusion observation exists: `:27` has P5 "NOT YET KNOWN", and U2:60 says "Version in Help > About: not read" as of 10-19. Nearby lines in the same step are labelled: `:111` "(it was on the old Parallels install)", and `:110` "(on the old Parallels install, REPORTED, capture notes)". This one, which guides the single most dangerous click in the walkthrough, is not.
- **Why it breaks.** This is the exact pattern v2 was audited FAIL for. DECISION_LOG row 402 reads: "step 2 gives the 09-29 log purge as a reason on Fusion … and the step doesn't name the install, which is the error v1 was withdrawn for." It is also the failure the brief names: "carrying old Parallels-install evidence onto Fusion as if it were Fusion's". The pre-fix copy had the same line, so adversarial-1 missed it. "Read the word before you click" reduces the hazard but doesn't fix the label.
- **Smallest fix:** "On the old Parallels install the three buttons read OK · Cancel · Apply, with Cancel in the middle (screenshot, above). On Fusion, read the word before you click."

### 2. MINOR (S2/R3, F13 not resolved): F2 is cited as fixing the zone, and the project's own ledger says F2 hasn't settled it
- **Line 40:** `F2 in specs/SPEC_RUBRIC.md (FROZEN) states the breaker and flatten times in ET (11:30 ET, 15:00–18:00 ET, 16:00 ET), so the zone those times are read in is not a setting to change here.`
- **Evidence:** `SPEC_RUBRIC.md:30-34` (pasted) is F2's *criterion*: the rule that a governing decision must still resolve. DECISION_LOG (2026-08-29) says "the expected flat-by-16:00 Eastern session close" "is one of the three candidates F2 was frozen to adjudicate." The "so …" is a mechanism claim (F2 constrains the NT8/Windows zone) with no label and no test. Read loosely, it also leans on Amear's open questions 1, 2 and 6 by implying ET is fixed.
- **Smallest fix:** drop the F2 sentence, as adversarial-1 asked. "This walkthrough changes nothing. A zone change is Amear's configuration decision" stands on its own.

### 3. MINOR (S2/R3, F7 partial): line 13 attributes the bead's "Options" to update 1 as fact, and the verbatim origin is PRAXIS's own 09-29 request
- **Line 13:** `The bead says "Tools, Options, General". Its source is migration update 1 :87, which calls it 'Tools > Options > General' (REPORTED, migration side). … The two disagree.`
- **Evidence:** the bead's stated sources are the seat-close handover §7 step 3 and DECISION_LOG 2026-10-20, and neither contains "Options" (grep pasted). The exact comma form "Tools, Options, General" appears only in `2026-09-29-vm-migration-concerns.md:35`, PRAXIS's own B2 request. Update 1 `:87` is answering that request ("PRAXIS should know this **for your B2**"). So the "Options" name traces back to PRAXIS's own unobserved wording, echoed back by the migration side. It is not an independent second source that "disagrees" with the screenshot. Every old-install observation (the screenshot and the capture notes) says **Settings**.
- **Smallest fix:** "The bead's 'Tools, Options, General' matches PRAXIS's own 09-29 B2 request (`2026-09-29-vm-migration-concerns.md:35`), echoed in update 1 `:87` (INFERRED lineage). No observation of either install shows 'Options'. Step 7 covers both names anyway."

### 4. MINOR (provenance / survival): the file was revised in place, its header still says "First version", and the changes are undisclosed
- **Line 4:** `First version for this bead, so it supersedes nothing.`
- **Evidence:** the pre-fix copy (sha256 `a8b39494…`) survives only in `/private/tmp/.../scratchpad/`, which is ephemeral and outside the repo. The current file has 15 diff hunks against it. No line in the file mentions adversarial-1 or the revision. Adversarial-1's line citations (`Line 54`, `Line 106`, …) now point at different text. v3 `:4` carried "Supersedes v2 … Both stay on disk unedited", and the v3 auditor raised an undisclosed change as a disclosure gap. Separately, line 11's DECISION_LOG row `2026-09-29T15:45:00Z` exists only in the unstaged worktree (`HEAD: 0`, `:0: 0`, worktree 3).
- **Smallest fix:** add one line to the header: "Revised in place 2026-10-20 after adversarial-1 (F1–F15). Pre-fix copy sha256 `a8b39494…`. The diff is in the manager report." Keep the pre-fix copy somewhere durable.

### 5. MINOR (contradiction, retry hazard): the general retry rule conflicts with the step-level "stop" rules, and it is wider than v3's
- **Line 124:** `If any step above (except step 7) didn't respond: try it once more, the same way.`
- **Line 116 (step 8):** `If it's still there, stop and tell me. Don't try another way to close it.` **Line 96 (step 3):** `If it's still there, stop and tell me.`
- **Evidence:** v3 `:27` scoped its retry to the single Analyzer click ("If (C): try once more, the same way (New, then Strategy Analyzer, one click)"). Adversarial-1 graded the carry-over "carried verbatim", but its scope widened. A "Cancel didn't respond" retry is a second click beside OK (step 8). If the first click registered late, the second lands on whatever sits behind the closed window.
- **Smallest fix:** "(except steps 3, 7 and 8, which say stop)", or scope the retry to steps 5 and 9 only.

### 6. MINOR (S2, branch mapping): "can't see the Time zone row" is routed to N5, whose meaning is "path doesn't match"
- **Line 114** routes to N5. **Line 61:** `N5. … or no **Time zone** row | The menu path (old install) doesn't match this install`.
- A row that is merely off-screen (small window, no scrolling allowed) isn't evidence that the path differs. N6 (`:62`, "Can't read it … text cut off | Can't tell") is the honest fit.
- **Smallest fix:** route `:114` to N6, or add to N5's meaning "or it's off-screen (can't tell which)".

### 7. MINOR (S8 lean, S2): K5's new note calls a breach of Amear's condition "expected", and labels a field reading as VERIFIED behaviour
- **Line 72:** `On the old Parallels install, 'Simulated Data Feed' was set to connect at startup (old Config.xml:18, name at :25, VERIFIED, old install only). If that file is the one in use, a dot there is expected (INFERRED).`
- **Evidence:** U2:67 records Amear's condition as "no other connection" (D-071). The XML value `true` is VERIFIED (pasted). "Set to connect at startup" reads behaviour off a field name, which is INFERRED, though the 07-24 screenshot's green dot is consistent with it. Calling an excluded connection "expected" pre-softens a row that Amear must judge.
- **Smallest fix:** "… `ConnectOnStartup` `true` (VERIFIED, old install only). That this connects it at startup is INFERRED. Whether a dot here is acceptable is Amear's call (D-071 says no other connection)."

### 8. MINOR (branch gap): two of the four step-13 reads have no pre-registered meaning
- **Lines 136-137** read "Set time automatically" and "Set time zone automatically". None of W1–W6 gives a meaning for Off / On respectively. P4 (`:26`) reports "Set time automatically" On. "Set time zone automatically **On**" would let Windows change the zone by itself (INFERRED), which bears directly on this bead. Only the catch-all `:90` covers these reads.
- **Smallest fix:** add W7 "Set time automatically Off, or Set time zone automatically On | Differs from P4 / zone may change by itself (INFERRED) | Report it. Amear decides."

### 9. MINOR (branch gap, F15b partial): a 1-to-2-minute clock difference has no row
- **Line 81:** `VM clock = Mac clock (to the minute)`. **Line 83:** `A difference of more than a minute or two`. A 1-minute difference (two clocks read across a minute boundary) matches neither row.
- **Smallest fix:** make `:81` "within a minute or two".

### 10. MINOR (S2/S8): the exclusion of charts and bar timestamps is attributed to Amear, with a reason, and no record supports either
- **Line 188:** `You ruled it out of this one, because a chart requests bars and touches the NQCONT defect.` Also `:88` "(out of scope, by Amear's ruling)".
- **Evidence:** the dispatch row 415 records Amear's choices as executor "You, by walkthrough" and scope "Add the Windows zone". No DECISION_LOG row up to 415 (the end of the file) records a chart or bar-timestamp ruling (grep pasted). The ruling may be real, since the brief relays it, but the "because …" puts a reason in Amear's mouth.
- **Smallest fix:** "Out of scope for this one, per your ruling relayed by praxis-master (REPORTED). PRAXIS's reason: a chart requests bars and touches the NQCONT defect." The manager report should cite where the ruling was given.

### 11. MINOR (practicality, UNVERIFIED): "don't scroll, don't resize" can lose the bead's key datum
- **Line 133:** `If you can't see the whole page, write 'not visible' for what's missing. Don't scroll, and don't resize the window.`
- The DST switch sits below the Time zone drop-down on Windows 11's Date & time page (INFERRED, general knowledge; not observed on Fusion). If the default window is short, the main reading of the bead comes back "not visible", and the run has to be repeated. W5 does route it to Amear, so this isn't a safety defect.
- **Smallest fix:** add to W5: "If the DST switch is 'not visible', a screenshot is the next request. Nothing else this run."

### Checked and holding (tried, no break)
- The Never OK / Apply / Enter lines (`:6`, `:102`, `:104`, `:115`) are all present. Every window has a close-and-confirm check (`:96`, `:116`, `:121`, `:140`). The dialog rule `:104` keeps "Never click OK" (v3 `:23`).
- Both "Don't disconnect" lines (K2 and K5) are present. "This walkthrough proposes no fix" (`:40`) and the open questions (`:184-189`) still leave every decision to Amear. N2's deadline has been handed back (F3).
- The step-8 fallback no longer points at any drop-down arrow. The Sounds group's per-row **x** clear buttons and the Volume slider (seen in the image) fall under `:113` "Don't click that box or any other box, tick or slider".
- Step 13 no longer tells Amear to maximise. The Windows page stays read-only, with Sync now and Change named (`:128`). The fallback route at `:131` matches the old-install image (Time & language, then Date & time) and forbids the search box (typing is garbled, P14).
- Step 7's Global Simulation Mode trap is closed by "don't try again" plus the `:124` exclusion. The capture notes confirm the order Global Simulation Mode, Client Dashboard, Settings, with GSM greyed on the old install.
- The branch tables (`:38-90`) precede every read. W, N and K each have "not where it says" rows (W6, N5, K7) and "can't tell" rows (W5, N6, K6).
- Survival against v3 is complete except for finding 4's provenance line. The licence-tooltip and dialog return fields are restored. The version line `:178` is carried verbatim. The NQCONT line `:180`, "Don't interpret it. Send it as copied." (`:176`) and "Nothing gets decided on this alone" (`:62`, `:88`) are all carried.
- All new citations resolve: U2 `:25 :60 :67 :89`, U1 `:87`, Config `:18 :25 :203`, `SPEC_RUBRIC:30-34`, `HANDOFF:7` (8.1.7.2, `DC242F5E…`) and `:106` (session-52 card, "imported (ET, `Last` …)"). Screenshot dates: 2026-09-29 11:19 file, image 11:15; 2026-07-24 09:25 file, commit 9717d93.

## §4. What the manager report must evidence (pasted output) for each VERIFIED item

1. P1: `windows-time-zone.png` shows Georgetown, Time & language, 11:14 AM 2026-09-29. Image read, plus `ls -l`.
2. P2 and line 8: `nt8-general-time-zone.png` has the title "Settings", the five categories, a Georgetown Time zone row, OK · Cancel · Apply, and the 11:15 taskbar clock.
3. P3: `sed -n 203p` on both rescue `Config.xml` copies, and `shasum -a 256` identical (`7a040a11…`).
4. P7: `find … NQCONT -type f | wc -l` = 1710, and the byte sum = 16,608,933.
5. P8: `20-connections-menu.png` shows no dot on Kinetick, and `Config.xml:34` `ConnectOnStartup` `false` inside `KinetickOptions`.
6. K5 (new): `Config.xml:18` `true` inside `SimulatorOptions`, and `:25` `Simulated Data Feed`.
7. P11: `ls -l /etc/localtime` → America/Toronto, `date` → EDT at about 13:35Z, and `pgrep vmware-vmx` at that time.
8. Line 11 (INFERRED, but the dates are measured): `stat`/`ls` file dates of both screenshots, and git commit 9717d93 for the 07-24 asset.
9. P6's negative search: the grep commands and their output over the DECISION_LOG 08-29 rows, HANDOFF, and the session-52 walkthroughs.
10. P12 (INFERRED): `TZ=America/Toronto date` for 10-31 → EDT and 11-01 → EST (pasted above).

## Result

ADVERSARIAL VERDICT: DEFECTS FOUND (1 blocking, 10 minor)
