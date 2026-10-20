# a20 adversarial 3 (final re-check): Fusion time-zone and Kinetick walkthrough

**Task:** final re-check of `docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md` (192 lines, sha256 `b9b30be4…4569da7d…cdd9f94`) after the fix for adversarial-2 findings 1–11. Bead `Praxis_build-a20`.
**Mode:** ADVERSARIAL. Run by praxis-worker on 2026-10-20. Nothing edited, staged or unstaged. This is the only file written.
**Criterion:** S1, S2, S8, S9 note R3, and the survival rule against v3 (`2026-10-20-fusion-analyzer-physical-click-walkthrough-v3.md`).

## Process log

1. Read the current file, adversarial-2, and v3 in full. Ran `diff <pre-fix2> <current>` (13 hunks, pasted below).
2. Confirmed that the pre-fix2 copy is the exact file adversarial-2 graded (sha256 match, below).
3. Re-checked the citations behind the changed lines: update 2 `:55 :56 :67`, `SPEC_RUBRIC.md:26-44`, DECISION_LOG row 415 and every 2026-10-20 row, `DECISIONS.md` for F2, `HANDOFF.md:7`, and capture notes `:28-75`.
4. Viewed all three source images with the Read tool.
5. Checked v3's phrases against the current file one by one with `grep -c`.
6. Ran a fresh attack on the whole file: labels, state-changing actions, branch coverage, and v3 removals.

## Verification evidence (pasted)

```
$ shasum -a 256 <current> <pre-fix2>
b9b30be41a05bd9cfcfc7d59b84569da7d730fa0920c0983a68710789cdd9f94  docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
0b55b7eba174c1f8eda209827074089bf5dcac07a458e76048f2c82894e38678  .../scratchpad/walkthrough-pre-fix2.md
```
The pre-fix2 hash matches the one adversarial-2 recorded at its `:3` (`0b55b7eb…8e38678`).

```
$ ls -la docs/reports/2026-10-20-a20-manager-report.md
ls: docs/reports/2026-10-20-a20-manager-report.md: No such file or directory
$ git status --short -- docs/reports/2026-10-20-a20-*
?? docs/reports/2026-10-20-a20-adversarial-1.md
?? docs/reports/2026-10-20-a20-adversarial-2.md
?? docs/reports/2026-10-20-a20-adversarial-3.md
?? docs/reports/2026-10-20-a20-fusion-tz-kinetick-walkthrough.md
```

```
$ sed -n '55p;67p' docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md
| 1 | Windows time zone on purpose; internet time on | **Done.** "(UTC-05:00) Eastern Time (US & Canada)", daylight saving On, "Set time automatically" On | REPORTED (Cowork, 2026-10-13 ~18:05Z, M-013). ...
| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server ... Amear accepted it on condition: no orders, no other connection (D-071). ...
```
U2:55 does not mention "Set time zone automatically".

```
$ grep -c 'F2' DECISIONS.md
0
$ grep -n '^- \[2026-10-20' DECISION_LOG.md | grep -i -c 'chart\|bar timestamp\|bar-timestamp'
0
$ sed -n 415p DECISION_LOG.md   (excerpt)
... APPROVED BY: amear, 2026-10-20, in-session AskUserQuestion: executor = **"You, by walkthrough"**, scope = **"Add the Windows zone"** ... (F2 governs ET session times; a zone change is a configuration decision that is his) ...
```

```
$ sed -n 7p HANDOFF.md   (excerpt)
... He reported: NT8 **`8.1.7.2, 64-bit`**, Machine ID **`DC242F5E75674D33D865C01BEF776371`** (the Parallels install was `077EF45C…`) ...
```

```
$ sed -n '33,55p' docs/reference/assets/nt8-2026-07-24/00-coworker-capture-notes.txt   (excerpt)
  Remove NinjaScript Assembly...
  Global Simulation Mode  (grayed/license-gated: ...)
  Client Dashboard
  Settings
Connections menu (top to bottom, as expanded):
  Kinetick – End Of Day (Free)
  Playback
  Simulated Data Feed   [green dot = currently connected]   -> "disconnect" link
  Simulation                                                 -> "configure" link
(Did not click disconnect or configure — layout capture only, per task constraints.)
```

```
$ for p in ...; do grep -c -- "$p" <current>; done      (v3 phrase survival)
click once                                     0
Never click OK                                 2
Don't quit it yourself                         1
Don't restart it                               1
Whether NT8 on Fusion does the same is unknown 1
Then stop. Don                                 1
Don't interpret it                             1
Nothing gets decided on this alone             2
Second try                                     0
stay on disk                                   0
DC242F5E                                       2
at that time                                   1
13:35                                          0
```

**Images, as I saw them.**
- `nt8-general-time-zone.png`: the window is titled "Settings", with a "?" and a red X at the top right. Categories: General (highlighted), Trading, Strategies, Automated trading interface, Market data. Time zone is a drop-down reading "(UTC-04:00) Georgetown, La Paz, Manaus, San Juan", visible without scrolling. The bottom buttons read OK, Cancel, Apply (Apply greyed). Taskbar clock: 11:15 AM 9/29/2026. Line 8 and line 116 match the image.
- `20-connections-menu.png`: rows Kinetick – End Of Day (Free) (no dot), Playback, Simulated Data Feed (green dot, "disconnect" on the right), Simulation. "configure" sits on its own line at the bottom right. No "connect" link is visible anywhere.
- `windows-time-zone.png`: the Time & language landing page, 11:14 AM, Tuesday September 29 2026, Time zone Georgetown, a "Date & time" card, a "Find a setting" search box, and minimise, maximise and X at the top right.

`diff <pre-fix2> <current>`: 13 hunks, at lines 4, 13, 33, 40, 50, 52 (added), 63, 73, 82, 89, 115-116, 125 and 189. All are quoted in §1 and §2.

## §1. Adversarial-2 findings 1–11

| # | Status | Current line, quoted |
|---|---|---|
| 1 | RESOLVED | `:116` "On the old Parallels install the three buttons at the bottom right read **OK · Cancel · Apply**, with Cancel in the **middle** … (screenshot, above). On Fusion, **read the word before you click.**" Matches the image. |
| 2 | RESOLVED | `:40` "Related: F2 in `specs/SPEC_RUBRIC.md` (FROZEN, `:30-34`) states the breaker and flatten times in ET and is not settled. This walkthrough doesn't touch it." The "so …" mechanism claim is gone. "Not settled" is supported: `DECISIONS.md` has 0 F2 hits, and F2 unblocks only on a DECISIONS.md entry. |
| 3 | RESOLVED | `:13` "That wording matches PRAXIS's own 09-29 request (`2026-09-29-vm-migration-concerns.md:35`, item B2), echoed back in migration update 1 `:87` (lineage INFERRED). No observation of either install shows 'Options'." |
| 4 | PARTIAL | `:4` "revised in place on 2026-10-20 after two adversarial passes … Both fix diffs are pasted in the manager report." The revision is now disclosed. But the manager report doesn't exist (`ls` above). No pre-fix sha256 is given. Both pre-fix copies exist only in the ephemeral scratchpad. See finding M1. |
| 5 | RESOLVED | `:125` "**If clicking Log (step 5) or Connections (step 9) didn't respond:** try it once more … **Any other step that didn't respond: stop and tell me.**" |
| 6 | RESOLVED | `:115` "… Click **Cancel**, check the window is gone, and stop (N6)." `:63` N6 now includes "or the Time zone row is off-screen". |
| 7 | RESOLVED | `:73` "`Config.xml:18` reads `ConnectOnStartup` `true` for 'Simulated Data Feed' (name at `:25`; VERIFIED, old install only). That this connects it at startup is INFERRED. Whether a dot here is acceptable is Amear's call (D-071 says no other connection)" |
| 8 | RESOLVED, with a new overstatement | `:52` W7 was added. Its "Differs from P4 (REPORTED)" is wrong for one of its two halves. See M4. |
| 9 | RESOLVED | `:82` "VM clock = Mac clock (within a minute or two)" |
| 10 | RESOLVED | `:89` "(out of scope, by your ruling as relayed, REPORTED)". `:189` "(your ruling relayed by praxis-master in the a20 dispatch, REPORTED; it isn't in `DECISION_LOG.md`). PRAXIS's reason: …". The negative holds: 0 chart or bar-timestamp hits in the 10-20 rows. |
| 11 | PARTIAL | `:50` "If the DST switch is 'not visible', a screenshot of the page is the next request. Nothing else this run." This is the text adversarial-2 proposed, but it doesn't work as intended. See M5. |

## §2. Regression hunt (`diff pre-fix2 current`)

- **No safety line was weakened.** Hunks 115-116 and 125 strengthen safety: the button layout is labelled, and the retry scope is narrowed to two harmless clicks. No hunk removes a Never-OK, Cancel, stop or "Don't disconnect" line.
- **No new state-changing action was added.** No new click, key or control appears in any step.
- **One small provenance regression, at hunk 33 (P11).** "VERIFIED by PRAXIS at 13:35Z today" became "VERIFIED by PRAXIS today (… output pasted in the manager report)". The same row still says "Fusion's VM process was running on it **at that time**", so `:33` now refers to a time that no longer appears. That file doesn't exist either. See M2.
- **One new overstatement, at hunk 52 (W7).** See M4.
- **No question of Amear's is answered.** Hunks 40, 73, 89 and 189 move text *away* from answering for him. W5's new "Nothing else this run" (hunk 50) is a mild exception. See M5.

## §3. Fresh attack

### (a) In-step facts: labels, and old-install facts read as Fusion's

Checked and holding:
- `:111`: "Settings, the **last** item (on the old Parallels install, REPORTED, capture notes)". Global Simulation Mode and Client Dashboard are just above it. The capture notes confirm the order.
- `:112`: "(it was on the old Parallels install)".
- `:116`: the button layout is labelled old-install.
- `:96`: the log-purge fact names the old Parallels VM and marks Fusion as unknown. This is v3's line, verbatim.
- `:103`: "Enter may press OK (INFERRED)".
- `:129`: "saves a change the instant you click … (INFERRED …)".
- `:141`: minimise is two buttons left of the X. This is a generic Windows fact and matches the old image.
- `:113`, `:118`, `:121`: the bare expectations "On the right, find the row Time zone", "A short list opens" and the Kinetick row name come from the sources at `:7-9`, which are labelled old-install. Their failure cases each have a stop row (N5, K7).

I found **no** old-install fact stated as Fusion's in a way that matches the v1/v2 failure pattern (a *reason* or *behaviour* asserted on Fusion). Minor label issues are in M6 and M7.

### (b) Actions that could change state

Checked and holding:
- OK, Apply and Enter are forbidden at `:6`, `:103`, `:105` and `:116`.
- Every window has a close-and-confirm check: `:97`, `:117`, `:122`, `:141`.
- The Connections rows and links are read-only, and the pointer stays parked on the header (`:119`).
- Esc is used only on a menu (`:111`, `:122`, `:132`), never inside the Settings window.
- The scroll wheel is forbidden over any box, and the "can't see" fallback is no-scroll (`:114-115`). The Sounds group's x-clear buttons and Volume slider fall under "any other box, tick or slider".
- On Windows Settings, every switch, drop-down, Sync now and Change is forbidden (`:129`), as are scrolling and resizing (`:134`), and the search box (`:132`).
- Retries are limited to the Log tab and the Connections header (`:125`).
- The dialog rule keeps "Never click OK. Then stop" (`:105`).

One gap: v3's "click once" was dropped. See M3.

### (c) Branch table

The tables (`:38-91`) come before every step (`:93` onward). W, N and K each have rows for "not where it says" (W6, N5, K7) and "can't tell" (W5, N6, K6). The version and Machine ID branches (`:179-180`) sit after the steps, as in v3, and were also written before the reads.

Small gaps, all covered by `:91` "Anything else … Amear decides":
- the Simulation row missing entirely;
- a K3 dot colour without saying which row;
- the "not visible" DST state, which has a send-back option (`:166`) but no row of its own (M5);
- a retry having happened (M3).

### (d) v3 removal diff

Every v3 clause is either present or replaced, except two:

| v3 clause | Current | Verdict |
|---|---|---|
| `:4` "Supersedes v2 … Both stay on disk unedited" | `:4` "revised in place … Both fix diffs are pasted in the manager report" | Acceptable *only if* that report exists and pastes both full diffs (M1) |
| `:6` scope "No … settings changed, no orders" | `:6`, strengthened | Carried |
| `:7` old-install source and version check | `:7-13` | Carried |
| `:11` Parallels "Don't quit it yourself" | `:95` | Carried |
| `:12` log purge, old VM, Fusion unknown | `:96`, verbatim | Carried |
| `:13` About, X | `:97`. "Owed on Fusion" is replaced by this morning's read (HANDOFF `:7`) | Justified, but see M3 (contamination) |
| `:14` clock | `:99`, plus the Mac clock | Carried |
| `:18`, `:25` Log before and after | `:109-110`, `:123` | Carried |
| `:19` "Use the mouse or trackpad and **click once**. Don't type anything … (M-026, REPORTED)" | `:103` keeps mouse-only and M-026. **"click once" is gone** (`grep -c` = 0) | **Dropped, no reason given** (M3) |
| `:20` licence tooltip | `:107` | Carried |
| `:23` dialog: Cancel or Close, Never click OK | `:105`, plus "stop" | Carried |
| `:27` "Then stop. Don't troubleshoot, restart NT8, or try other routes." | `:125` | Carried |
| `:31` save prompt No or Cancel | `:145` | Carried |
| `:32` leave running | `:146` | Carried |
| `:45` "Second try (if C)" return field | **No equivalent** (`grep -c` = 0). Retries are allowed at `:125`, but no field records them | **Dropped** (M3) |
| `:52` "Don't interpret it. Send it as copied." | `:177` | Carried |
| `:53` "Nothing gets decided on this alone" | `:63`, `:89` | Carried |
| `:54` version line | `:179`, verbatim | Carried |
| `:51` NQCONT separate defect | `:181` | Carried |

## Findings

No finding is BLOCKING. None of them puts state at risk if Amear runs the walkthrough as it stands. M1 is a precondition for the auditor's S1 grade, not a defect in the walkthrough's steps.

### M1. MINOR, gates S1 (F5 / adversarial-2 #4 partial): every VERIFIED item and both fix diffs point at a file that doesn't exist
- `:15` "Pasted evidence for every VERIFIED item here: `docs/reports/2026-10-20-a20-manager-report.md`". `:4` "Both fix diffs are pasted in the manager report." `:33` "output pasted in the manager report".
- Evidence: `ls` gives "No such file or directory". Both pre-fix copies are only in the session scratchpad.
- Smallest fix: the manager report must exist before audit. It needs the pasted evidence (adversarial-2 §4 items 1-10), both full diffs, and the sha256 values of both pre-fix copies (`0b55b7eb…` is pre-fix2). Without it, the walkthrough's S1 can't be graded PASS.

### M2. MINOR (regression, provenance): P11 lost its timestamp but still says "at that time"
- `:33` "VERIFIED by PRAXIS today (…; output pasted in the manager report). That this is the Mac running Fusion is INFERRED: Fusion's VM process was running on it **at that time**". Pre-fix2 read "at 13:35Z today".
- Smallest fix: restore the measured time (13:35Z, or whatever the manager report's pasted run shows).

### M3. MINOR (survival): v3's "click once" and "Second try" field were dropped without a reason, and step 3 prints the expected values it asks Amear to read
- **"click once"** (v3 `:19`) has no counterpart; `:103` reads only "click only with the mouse or trackpad". A double-click on **Cancel** (`:116`) closes Settings with the first click. The second click then lands on whatever is behind it in the Control Center. On Fusion that layout is unknown: it could be a chart, possibly with Chart Trader buttons (INFERRED, not observed). Fix: add "Click once." to the `:103` Throughout line.
- **"Second try"** (v3 `:45`): `:125` allows retries, but the send-back form has no field for them. Fix: add "Retried (step 5 / step 9): yes / no, result:".
- **Contamination:** `:97` asks Amear to "Write down the version and the Machine ID exactly as shown" and, in the same step, prints the full expected `DC242F5E75674D33D865C01BEF776371`. A matching copy then can't be told apart from a transcription. This is the hazard DECISION_LOG `2026-08-29T19:50:00Z` names ("a matching string is not evidence"). v3 printed no expected value. Fix: drop the expected values from step 3, and leave the comparison to `:179-180`, done by PRAXIS on receipt.

### M4. MINOR (S2): W7 says "Set time zone automatically On" differs from P4, but P4 is silent on it
- `:52` "W7. 'Set time automatically' **Off**, or 'Set time zone automatically' **On** | Differs from P4 (REPORTED)". U2:55, pasted above, reports only DST On and "Set time automatically" On.
- Fix: "'Set time automatically' Off differs from P4. P4 doesn't report 'Set time zone automatically'. With it On, Windows may change the zone by itself (INFERRED)."

### M5. MINOR (practicality, slight S8 lean): the W5 addition can't do what it says, and it contradicts its own row
- `:50` "Amear decides whether to look again. If the DST switch is 'not visible', a screenshot of the page is the next request. Nothing else this run."
- A screenshot of the unscrolled page shows exactly what was already "not visible". Step 13 (`:140`) already invites a screenshot. So the only real next step is a second, scrolled look, which the same cell gives to Amear and then closes off with "Nothing else this run". The W5 condition column ("No DST switch shown, or it's greyed out") also doesn't cover "not visible" (off-screen), which `:166` offers as a separate answer.
- Fix: give "not visible" its own row: "Can't tell. Send what's on screen. Amear decides whether a scrolled look is the next run."

### M6. MINOR (S2, errs toward caution): step 10 states unlabelled what the "configure" and "connect" links do
- `:119` "Clicking a name in this list connects or disconnects it (INFERRED), and so do the small "connect", "disconnect" and "configure" links." The INFERRED tag covers only the first clause. In the image, "configure" is on its own line, and no "connect" link is visible. The capture notes say only "Did not click disconnect or configure". Nothing observed says "configure" connects or disconnects anything.
- Fix: "… (INFERRED). Don't click the small 'disconnect' or 'configure' links either: what they do on Fusion hasn't been observed."

### M7. MINOR (S2): "not connected" is graded VERIFIED, but what was verified is "no dot"
- `:30` P8 "Old install: Kinetick EOD was **not connected** (no dot, 2026-07-24) … VERIFIED". `:69` K1 "no dot | Not connected".
- That a green dot means connected is the Cowork capture-note legend ("[green dot = currently connected]", REPORTED). `ConnectOnStartup` `false` is a startup setting, not the state on 07-24.
- Fix: "no dot (VERIFIED). No dot = not connected per the capture-note legend (REPORTED)." Also add "(REPORTED legend)" to K1.

### M8. NIT (S2): the clock row says "Windows gives EDT today"
- `:82`: equal clocks show that Windows is at UTC−4 local time, assuming both clocks are synced. They don't show EDT, which is the point the same cell makes next.
- Fix: "Windows is at UTC−4 today (if both clocks are synced)."

## Result

NO BLOCKING DEFECT. Adversarial-2 findings 1-3 and 5-10 are resolved (8 with a new overstatement, M4). Findings 4 and 11 are partial. The fix2 diff weakens no safety line. The v3 survival diff shows two unjustified drops ("click once" and the "Second try" field), both minor. M1 must be closed before the auditor can grade S1.

ADVERSARIAL VERDICT: DEFECTS FOUND (0 blocking, 8 minor)
