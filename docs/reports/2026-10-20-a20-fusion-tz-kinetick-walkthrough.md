# Walkthrough a20: time zones and Kinetick, read only (Fusion VM)

**For:** Amear, by hand. Not for Cowork or any automation.
**Written:** 2026-10-20 by praxis-worker for praxis-manager, bead `Praxis_build-a20`. First version for this bead, revised in place on 2026-10-20 after four adversarial passes (`2026-10-20-a20-adversarial-1.md`, `-2.md`, `-3.md`, and a narrow fourth pass whose findings are in the manager report). Every fix diff is pasted in the manager report. It supersedes no earlier walkthrough. Modelled on walkthrough v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`), the only walkthrough graded PASS. Auditor grade appended below when given.
**Question it answers:** what time zone does Windows on the Fusion VM use, is its automatic daylight-saving switch on, what time zone does NinjaTrader itself use, and is Kinetick End Of Day connected?
**Scope:** read the About box, read NinjaTrader's Settings window, look at the Connections list, read Windows' Date & time page. Write down what you see. **No** chart opened, **no** bar timestamps read, **no** Strategy Analyzer, **no** setting changed, **no** connection made or dropped, **no** orders. Every window is left with **Cancel**, **Escape** or its **X**. **Never OK, never Apply, never Enter.**
**Menu path source:** two screenshots from the **old Parallels install**, both read by PRAXIS today (2026-10-20):
- `~/VM-Rescue-2026-09-29/screenshots/nt8-general-time-zone.png` (taken 2026-09-29 11:15). It shows NinjaTrader's window titled **Settings**, not "Options". Its categories run General, Trading, Strategies, Automated trading interface, Market data. General has a **Time zone** row. The buttons at the bottom read **OK · Cancel · Apply**, in that order.
- `docs/reference/assets/nt8-2026-07-24/20-connections-menu.png` (2026-07-24). It shows the Connections list with **Kinetick – End Of Day (Free)** on top and a green dot on the one connected row.

**Why "old Parallels install"** (INFERRED from these dates): the Settings screenshot dates from 2026-09-29, and `DECISION_LOG.md` row 2026-09-29T15:45:00Z places that day's captures "during the live Parallels session". The Connections screenshot dates from 2026-07-24. Fusion's NT8 was installed 2026-10-19 (update 2 `:60`, REPORTED), after both.

The Tools menu ending in **Settings** comes from the capture notes for that same old install (REPORTED, Cowork, `00-coworker-capture-notes.txt:33-48`). The bead says "Tools, Options, General". That wording matches PRAXIS's own 09-29 request (`2026-09-29-vm-migration-concerns.md:35`, item B2), echoed back in migration update 1 `:87` (lineage INFERRED). No observation of either install shows 'Options'. The old install's screenshot shows a window titled **Settings**, and its Tools menu ended in Settings (capture notes, REPORTED). Step 7 covers both names. Fusion runs the same version per Amear's read this morning (8.1.7.2, REPORTED). Step 3 below checks that. Steps 7 and 9 check the menus themselves.

Pasted evidence for every VERIFIED item here: `docs/reports/2026-10-20-a20-manager-report.md`, Verification evidence section.

> You don't need to read the next two sections before clicking. They are here so that what each result means was fixed **before** anyone looked.

## What we already have, and how sure we are

| # | Premise | Label and source |
|---|---|---|
| P1 | Old Parallels install: Windows zone **"(UTC-04:00) Georgetown, La Paz, Manaus, San Juan"** | VERIFIED by PRAXIS today from the screenshot `~/VM-Rescue-2026-09-29/screenshots/windows-time-zone.png` (Time & language page, 11:14 AM, 2026-09-29). **Old install only** |
| P2 | Old Parallels install: NinjaTrader's own Time zone was that **same** Georgetown zone | VERIFIED by PRAXIS today from `nt8-general-time-zone.png` (above). **Old install only.** Previously REPORTED by the migration side (`DECISION_LOG.md` row 2026-09-29T15:45:00Z) |
| P3 | Old install's `Config.xml` has an **empty** zone field (`<TimeZoneInfoSerializable />`) | VERIFIED by PRAXIS today, line 203 of both rescue copies (`~/VM-Rescue-2026-09-29/files/NinjaTrader 8/` and `…/NinjaTrader 8-full/`, identical files). That "empty" means "follow Windows" is INFERRED: it fits P1 and P2 |
| P4 | Fusion Windows zone **"(UTC-05:00) Eastern Time (US & Canada)"**, daylight saving **On**, "Set time automatically" On | REPORTED (Cowork, 2026-10-13 ~18:05Z, via migration update 2 `:55`). Amear's decision to keep Eastern with DST: REPORTED (update 1 §4). **Step 13 observes it** |
| P5 | Fusion NinjaTrader's own Time zone | **NOT YET KNOWN** (update 2 `:56`). Whether the old `Config.xml` is the one Fusion's NinjaTrader uses is also not known: the restore was reported faithful (update 2 `:25`), but the whole folder was not byte-checked (`:70`). **Step 8 observes it** |
| P6 | NQCONT was imported as **US Eastern** | REPORTED, not observed: recorded by praxis-master in the session-52 card (`HANDOFF.md:106`), which records "imported (ET, `Last`…)". The original reporter isn't identified there. The walkthrough Amear used told him to choose "US Eastern" (`2026-08-29-session52-nt8-voice-walkthrough-v2.md:144`), and an instruction isn't an observation. PRAXIS found no screenshot or quote of the import window's setting (searched: `DECISION_LOG.md` 2026-08-29 rows, `HANDOFF.md`, the session-52 voice walkthroughs). The bead's cited sources, the session-42 r8j import report and the session-44 offset-correction reports, are about Phase-3 spec text and don't mention NQCONT. The import was done on the **old Parallels install** |
| P7 | NQCONT's files are on Fusion: 1,710 files, 16,608,933 bytes | Fusion count REPORTED (Amear, update 2 `:27`). The figures it was matched against were VERIFIED by PRAXIS today in the old install's rescue copy (`…/NinjaTrader 8-full/db/minute/NQCONT`) |
| P8 | Old install: Kinetick EOD showed **no dot** on 2026-07-24 (VERIFIED, screenshot). No dot = not connected is INFERRED from the capture-note legend, which marks only the green dot (`00-coworker-capture-notes.txt:53`, REPORTED), and set not to connect at startup | VERIFIED by PRAXIS today: the screenshot, and `ConnectOnStartup` `false` in the old `Config.xml` line 34. **Old install only** |
| P9 | Fusion connections: NinjaTrader connected itself to **"Simulation"**, and Amear accepted that on condition: no orders, no other connection | REPORTED (update 2 `:67`, D-071). Kinetick EOD on Fusion: **NOT YET KNOWN**. **Step 10 observes it** |
| P10 | Fusion Windows: Windows 11 Pro 25H2, build 26200.9457, on 2026-10-13 | REPORTED (Cowork `winver`, update 1 `:48`). Today's build: NOT YET KNOWN. The route to the Date & time page is INFERRED from general Windows 11 knowledge and the old install's screenshot (P1) |
| P11 | The Mac's own clock is set to Toronto time (Eastern, with daylight saving) | VERIFIED by PRAXIS today: `/etc/localtime` reads `America/Toronto` and local time printed as EDT at 13:48Z; Fusion's `vmware-vmx` process was running at 14:09Z (both pasted in the manager report). That this is the Mac running Fusion is INFERRED from that process |
| P12 | Until **2026-11-01**, Eastern-with-DST and the old fixed UTC−4 show the **same clock time**. From 11-01 they differ by one hour | INFERRED (calendar). **So today's clock cannot tell them apart. Only the zone's name can** |
| P13 | How NinjaTrader shifts bars across a DST change for a given zone setting | INFERRED only. PRAXIS has no evidence. **No conclusion below depends on it.** The bead's "a mismatch could shift every bar by an hour" is also INFERRED, never tested |
| P14 | Typed text arrives garbled in this VM. Clicks and single keys work | REPORTED (M-026, migration side) |

## What each result means (written 2026-10-20, before any read was made)

**Rule for every row:** any mismatch goes to Amear as a decision. This walkthrough proposes **no fix**. Related: F2 in `specs/SPEC_RUBRIC.md` (FROZEN, `:30-34`) states the breaker and flatten times in ET and is not settled. This walkthrough doesn't touch it. A zone change is Amear's configuration decision.

**(W) Windows zone and its daylight-saving switch** (step 13)

| What you see | What it means | What happens next |
|---|---|---|
| W1. "(UTC-05:00) Eastern Time (US & Canada)", DST switch **On** | P4 is now observed, not just reported | Nothing changes. Compare with (N) |
| W2. Eastern Time, DST switch **Off** | From the zone's rules, Windows runs UTC−5 all year (INFERRED), which is one hour behind Eastern today. Step 4 should show the VM clock an hour behind the Mac | Mismatch with P4. **Amear decides.** No change made here |
| W3. "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" | The old install's zone is on Fusion. This contradicts P4 | **Amear decides.** |
| W4. Any other zone | Not what anyone reported | **Amear decides.** |
| W5. No DST switch shown, or it's greyed out | Can't tell the DST state. Windows may hide or grey it for some zones or settings (INFERRED) | Send what's on screen. Amear decides whether to look again. |
| W5a. The DST switch is 'not visible' (off-screen; you didn't scroll) | Can't tell | Send what's on screen. Amear decides whether a scrolled look is the next run |
| W6. The page isn't where step 12 says, or looks different | The route is wrong for this Windows (P10 is INFERRED) | Stop at that point. Send what you saw. No other route is tried |
| W7. 'Set time automatically' **Off**, or 'Set time zone automatically' **On** | 'Set time automatically' Off differs from P4 (REPORTED). P4 doesn't report 'Set time zone automatically'. With it On, Windows may change the zone by itself (INFERRED) | Report it. **Amear decides.** |

**(N) NinjaTrader's own Time zone** (step 8)

| What you see | What it means | What happens next |
|---|---|---|
| N1. Same label as Windows' (W) | NinjaTrader and Windows agree on the label. This doesn't show *why*: following Windows and an explicit choice of the same zone look the same | See "All agree" below |
| N2. "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan" | The same label the old Parallels install displayed (P2). How it got here is NOT KNOWN: the old Config.xml stores no zone (P3). Same clock as Eastern today. One hour apart from 2026-11-01 (P12, INFERRED) | **Amear decides**, including when (open question 1). |
| N3. Any other label that differs from Windows' | NinjaTrader and Windows disagree | **Amear decides.** |
| N4. The Time zone box is blank | Not seen before. Meaning unknown | Send it. **Amear decides** whether to look again |
| N5. No **Settings** and no **Options** in the Tools menu, no **General** category, or no **Time zone** row | The menu path (old install) doesn't match this install | Stop at that point. Send what you saw. No other route is tried |
| N6. Can't read it (window didn't open, text cut off), or the Time zone row is off-screen | Can't tell | Send what you saw. Nothing gets decided on this alone |

**(K) Kinetick End Of Day** (step 10)

| What you see | What it means | What happens next |
|---|---|---|
| K1. Kinetick row present, **no dot** | Not connected (INFERRED from the capture-note legend: green dot = connected). Matches the old install's setting, *if* that setting was restored (P8; INFERRED for Fusion) | Report it. Amear decides whether that's what he wants |
| K2. Kinetick row with a **green** dot | Connected | Report it. **Don't disconnect.** Amear decides |
| K3. A dot of any other colour | Some other connection state (INFERRED) | Copy the colour and any text. Amear decides |
| K4. No Kinetick row | It isn't set up on this install | Report it. Amear decides |
| K5. A dot on any row other than "Simulation" | A connection beyond the one Amear accepted (P9, D-071). On the old Parallels install, `Config.xml:18` reads `ConnectOnStartup` `true` for 'Simulated Data Feed' (name at `:25`; VERIFIED, old install only). That this connects it at startup is INFERRED. Whether a dot here is acceptable is Amear's call (D-071 says no other connection) | Report it. **Don't disconnect.** Amear decides |
| K6. Can't tell | — | Send what you saw |
| K7. The Connections menu doesn't open, or isn't in the menu bar | Can't tell | Stop. Send what you saw. No other route is tried |
| K8. Simulation has no dot | Differs from update 2 `:67` (REPORTED connected) | Report it. Amear decides |

**Clock and Log checks** (steps 4, 6, 11)

| What you see | What it means | What happens next |
|---|---|---|
| VM clock = Mac clock (within a minute or two) | Windows is at UTC−4 today (if both clocks are synced). **It cannot show Eastern versus fixed UTC−4** (P12) | Nothing on its own |
| VM clock one hour behind the Mac | Fits W2 (INFERRED) | Report it. Amear decides |
| A difference of more than a minute or two | Not explained | Report it. Amear decides |
| Mac clock not readable | Write 'not read' | Nothing on its own |
| No new Log rows between steps 6 and 11 | No change showed in the Log. The Log doesn't record everything, so this isn't proof that nothing changed (INFERRED) | Nothing on its own |
| New Log rows between steps 6 and 11 | Something happened in NinjaTrader during the reads | Copy them exactly. Don't interpret them. Amear and PRAXIS read them |

**All agree** (W1 + N1 + P6's "US Eastern"): the **labels** agree. That's all it shows. It does **not** show that bar timestamps are right, because no chart was read (out of scope, by your ruling as relayed, REPORTED). It doesn't show how NinjaTrader handles the 11-01 change (P13). And P6 is still only reported. Nothing gets decided on this alone.

**Anything else, or a mix:** send it as copied. Amear decides.

## Before you start (about 2 minutes)

1. **Only one NinjaTrader.** Parallels must not be running on the Mac. If it is, **stop here and tell me. Don't quit it yourself.** We restart this later. (You started the old Parallels VM yourself this month: M-031, REPORTED in the seat-close handover §4. On 10-19 it could still be run: update 2 `:89`, REPORTED.)
2. **NinjaTrader is open in the Fusion VM**, with the Control Center visible. **Don't restart it.** On 2026-09-29 the migration side reported that NT8 on the **old Parallels VM** deleted its older log files when it started (REPORTED). Whether NT8 on Fusion does the same is unknown.
3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. Copy what the screen shows, character by character. PRAXIS compares it with this morning's read (`HANDOFF.md:7`, REPORTED by you). Close the box with the **X** at its top-right. **Check that the box is gone.** If it's still there, stop and tell me.
4. If the VM fills the whole Mac screen, move the pointer to the very top edge to show the Mac's menu bar and clock. Don't click there.
   **Note the clocks.** Write down the Windows time (bottom-right of the VM screen) **and** the Mac's time (top-right of the Mac screen), read together. You'll compare them with each other, and against the Log tab later.

## The NinjaTrader reads (about 3 minutes)

**Throughout:** click only with the mouse or trackpad. **Click once.** Don't type anything. The migration side reports that typed strings arrive garbled on this VM, while clicks and single keys work (M-026, REPORTED). **Never press Enter.** In a NinjaTrader window, Enter may press OK (INFERRED).

**If a dialog or error box appears at any point:** copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.** Then stop and tell me.

**A licence tooltip** ("Please upgrade to a Lease or Lifetime license…") may appear over some menu items. **Note whether it appears. Don't act on it.**

5. In the Control Center, click the **Log** tab.
6. Write down the **time and message of the newest row**, and when you wrote it. Leave the tab showing.
7. In the Control Center menu bar, click **Tools**. The list opens. Click **Settings**, the **last** item (on the old Parallels install, REPORTED, capture notes). If Settings is there but not last, click it anyway. Take care: on the old Parallels install the items just above it were Client Dashboard and **Global Simulation Mode** (REPORTED, capture notes), and Global Simulation Mode is a switch (INFERRED). If there's no **Settings** but there is **Options**, click **Options**. If there's neither, press **Esc** once and stop (N5). If anything other than a window called **Settings** (or **Options**) appears, **stop and tell me. Don't undo it yourself.** If you clicked and no Settings (or Options) window opened, **don't try again**. Stop and tell me which item you think you clicked.
8. The Settings window opens. On the left, under **Categories**, **General** should already be highlighted (it was on the old Parallels install). If it isn't, click the word **General**.
   - On the right, find the row **Time zone**. **Write down the text in the box beside it, exactly.**
   - **Don't click that box or any other box, tick or slider.** Don't use the scroll wheel with the pointer over any box.
   - If you can't see the **Time zone** row, don't scroll and don't click anything in the list. Click **Cancel**, check the window is gone, and stop (N6).
   - Now **click Cancel**. On the old Parallels install the three buttons at the bottom right read **OK · Cancel · Apply**, with Cancel in the **middle** and OK right next to it on the left (screenshot, above). On Fusion, **read the word before you click.** **Never click OK. Never click Apply.**
   - **Check that the Settings window is gone.** If it's still there, stop and tell me. Don't try another way to close it.
9. In the Control Center menu bar, click **Connections**. A short list opens.
10. **Read it. Don't click anything in it.** Clicking a name in this list connects or disconnects it (INFERRED). Don't click the small 'disconnect' or 'configure' links either: what they do on Fusion hasn't been observed. Keep the pointer still on the word **Connections**.
    - Write down **every row's name**, and for each one: **is there a dot, and what colour?**
    - **Kinetick – End Of Day (Free)** is the row we're after. If it isn't there, write that down.
    - Then press **Esc** once. **Check that the list is gone.** If it's still open, click the word **Connections** once more. If it's still there, stop and tell me.
11. Look at the **Log** tab again. Did any new row appear after the one from step 6? If yes, copy its time and message exactly.

**If clicking Log (step 5) or Connections (step 9) didn't respond:** try it once more, the same way. Then stop. Don't troubleshoot, restart NT8, or try other routes. **Any other step that didn't respond: stop and tell me.**

## The Windows read (about 2 minutes)

Windows' Settings app **saves a change the instant you click**. There is no Cancel (INFERRED, general Windows 11 knowledge; this route has not been seen on Fusion, P10). So on this page, **read only: don't touch any switch, drop-down, or the "Sync now" or "Change" buttons.**

12. **Open Date & time by clicks.** Right-click the **clock** at the bottom-right of the VM screen. In the small menu, click **Adjust date and time**.
    - If that item isn't in the menu, press **Esc** once. Then click the **Start** button, click **Settings** (the gear), click **Time & language** in the left-hand list, then click **Date & time**. Don't use the search box.
    - If neither works, stop and tell me (W6).
13. The **Date & time** page shows. Don't scroll. If you can't see the whole page, write 'not visible' for what's missing. Don't scroll, and don't resize the window. Write down exactly:
    - **Time zone**: the text in its box.
    - **Adjust for daylight saving time automatically**: **On** or **Off**, or "not shown", or "greyed out".
    - **Set time automatically**: On or Off.
    - **Set time zone automatically**: On or Off.
    - If any of these isn't visible, write "not visible". Don't scroll to find it.
    - A screenshot of this page is welcome.
14. Close the **Windows** Settings window with its **X** at the top-right. Not the minimise line, which is two buttons to the left of the X. **Check that the window is gone.** If it's still there, stop and tell me.

## Closing up

15. If a "save?" prompt appears anywhere, choose **No** or **Cancel**.
16. Leave NinjaTrader running as it was. Nothing else to undo.

## What to send back

```
Parallels running at start: yes / no
NT8 version (Help, About):
Machine ID (Help, About):
About box gone after X: yes / no
Windows clock at start:
Mac clock at start:
Newest Log row before reads (time + message, and when noted):
Tools menu had: Settings / Options / neither
NT8 Time zone (exact text):
Settings window gone after Cancel: yes / no
Connections rows (name + dot colour, or no dot):
Kinetick - End Of Day row: present, dot colour / present, no dot / absent
Connections list gone after Esc: yes / no
New Log rows after reads (time + message):
Windows Time zone (exact text):
Adjust for daylight saving time automatically: On / Off / not shown / greyed / not visible
Set time automatically: On / Off / not visible
Set time zone automatically: On / Off / not visible
Windows Settings window gone after X: yes / no
Anything that didn't respond, or wasn't where this said:
Retried (step 5 / step 9): yes / no, result:
Where you stopped, if early (step number):
Screenshots taken: yes / no
Licence tooltip appeared (where): yes / no
Dialog text (step, exact):
```

**Don't interpret it. Send it as copied.** The meanings are fixed in the tables above, and every mismatch is your decision.

- **Version not 8.1.7.2:** send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking.
- **Machine ID not `DC242F5E…6371`:** send it anyway. It means this isn't the machine you checked this morning, or it was misread. You decide what follows.
- This doesn't touch the NQCONT "unknown instrument" error. That's a separate defect, reported to reproduce on Fusion, and still open. Nothing here requests bars.

## Open questions for Amear (not answered here)

1. If NinjaTrader's zone differs from Windows' (N2, N3): which zone should NinjaTrader use, and should that be settled before 2026-11-01?
2. If Windows isn't Eastern with DST On (W2 to W5): keep it as found, or change it? Update 1 §4 reports your decision as Eastern with DST (REPORTED).
3. Kinetick EOD: is the state you see the state you want?
4. On 2026-08-29, did you pick "US Eastern" in the import window yourself? PRAXIS has the instruction and a card saying "ET", but no record of what the window showed (P6).
5. Do you want a bar-timestamp check later? You ruled it out of this one (your ruling relayed by praxis-master in the a20 dispatch, REPORTED; it isn't in `DECISION_LOG.md`). PRAXIS's reason: a chart requests bars and touches the NQCONT defect.
6. If NinjaTrader follows Windows: should it keep following, or should its zone be set on purpose?

---

## Auditor grade: `Result: PASS` (two audits, both PASS), 2026-10-20

> **PROVENANCE:** transcribed by praxis-master from the messages returned by two `praxis-auditor` runs. The auditor cannot write files. Nothing above this line was edited after the grades.

**Why there are two audits.** The first audit stopped at its turn limit with no verdict. That counts as FAIL for the commit decision and not toward the park rule (rulings R-A to R-C). It was re-dispatched with a material reduction, split in two (`DECISION_LOG` 2026-10-20T14:33:33Z).

**Audit A: the walkthrough as instructions.**
- R-SAFE, R-PROV, R-SURV, R-BRANCH and S8 all PASS. No blocking findings.
- The auditor did its own line-by-line removal diff against v3. It confirms that v3's "stop here and tell me. Don't quit it yourself." survives word for word (L96), and that the provenance line is carried and strengthened.
- Minor findings, not fixed in this file:
  1. Close rules are mixed: Close at L106 and No at L146, beside Cancel/Escape/X. Both are non-saving and carried from v3.
  2. **Step 8 has no inline fallback for "no General category".** That case is only in N5. **If General is missing: click Cancel, check the window is gone, stop.**
  3. "Not visible" rows exist only for the DST switch. Other unreadable fields fall to the catch-all at L92.
  4. §V of the manager report does not note that the version source changed (now HANDOFF:7, Amear's read).
  5. **L90 and L191 call Amear's scope choice a "ruling". It was not one: he picked the middle of three offered scopes** (`DECISION_LOG` 14:28:55Z correction).

**Audit B: the evidence (manager report and P1–P14).**
- S1, S2 and S9-R3 all PASS. No blocking findings.
- The auditor viewed all three screenshots and confirmed every described detail. It re-ran the Config.xml lines (identical in both rescue copies) and E3 (0 NQCONT mentions in the four cited r8j reports). It checked HANDOFF:106 and voice-walkthrough-v2:144, and spot-checked update 2 `:55` and `:67` and capture notes `:53`. All hold.
- Minor findings:
  1. One pasted grep block in manager report §E2 is a silent subset of the real output, missing four lines. The missing lines support the attribution.
  2. P8 pairs a 07-24 screenshot with a 09-29 Config.xml without dating the setting.
- **Master re-ran the Config.xml, cmp, E3 and HANDOFF:106 checks itself in this turn. All reproduce.**

**Status: cleared for Amear to run.**
