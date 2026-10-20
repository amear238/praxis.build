# Walkthrough v3: open the Strategy Analyzer by physical click (Fusion VM)

**For:** Amear, by hand. Not for Cowork or any automation.
**Written:** 2026-10-20 by praxis-master (seat 48550). Supersedes v2 (audited FAIL on S1/S2; grade at the foot of the v2 file) and v1 (withdrawn). Both stay on disk unedited. Auditor grade appended below when given.
**Question it answers:** does the Strategy Analyzer window open on the Fusion VM when you click it yourself?
**Scope:** read the About box, open the Analyzer, look, close. **No** instrument picked, **no** backtest, **no** settings changed, **no** orders.
**Menu path source:** `docs/reference/2026-07-24-nt8-windows-reference.md`: §0 "Control Center tabs" (Log), §1c "Open: `New > Strategy Analyzer`", §2 "Errors appear in the Control Center `Log` tab". Those screenshots come from the **old Parallels install**. Fusion runs the same version per the migration side (8.1.7.2, REPORTED). Step 3 below checks that.

## Before you start (about 2 minutes)

1. **Only one NinjaTrader.** Parallels must not be running on the Mac. If it is, **stop here and tell me. Don't quit it yourself.** We restart this later.
2. **NinjaTrader is open in the Fusion VM**, with the Control Center visible. **Don't restart it.** On 2026-09-29 the migration side reported that NT8 on the **old Parallels VM** deleted its older log files when it started (REPORTED). Whether NT8 on Fusion does the same is unknown.
3. **Read the About box first.** In the Control Center menu bar, click **Help**, then **About**. Write down the **version** and the **Machine ID** exactly as shown. Close the box with the **X** at its top-right. Migration update 2 lists both as still owed on Fusion.
4. **Note the clock.** Write down the Windows time (bottom-right of the VM screen). You'll compare it against the Log tab later.

## The check (about 2 minutes)

5. In the Control Center, click the **Log** tab. Note the time on the **newest row** and leave the tab showing.
6. In the Control Center menu bar, click **New**, then click **Strategy Analyzer**. Use the mouse or trackpad and **click once**. Don't type anything. The migration side reports that typed strings arrive garbled on this VM, while clicks and single keys work (M-026, REPORTED).
7. **Wait 15 seconds** and watch the screen. A licence tooltip ("Please upgrade to a Lease or Lifetime license…") may appear. **Note whether it appears. Don't act on it.**
8. Record which of these happened:
   - **(A) A Strategy Analyzer window opened.**
   - **(B) A dialog or error box appeared.** Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.**
   - **(C) Nothing at all happened.**
9. Look at the **Log** tab again. Did any new row appear after the time from step 5? If yes, copy its time and message exactly.

**If (C):** try once more, the same way (New, then Strategy Analyzer, one click). Then stop. Don't troubleshoot, restart NT8, or try other routes.

## Closing up

10. **If (A):** take one screenshot of the Analyzer window. Then close it with the **X** at its top-right. If a "save?" prompt appears, choose **No** or **Cancel**. Don't touch anything inside the window first.
11. Leave NinjaTrader running as it was. Nothing else to undo.

## What to send back

```
NT8 version (Help > About):
Machine ID (Help > About):
Clock at start:
Newest Log row before click (time):
Result: A / B / C
Licence tooltip appeared: yes / no
Dialog text (if B):
New Log rows after click (time + message):
Second try (if C): A / B / C
Screenshot taken: yes / no
```

## What each result means

- **(A) Opens:** the Analyzer opens on Fusion, so the licence-gate theory is dead **on Fusion**. The Parallels question stands as relayed: on 2026-09-29 the migration side reported the Analyzer opening on a physical click there (REPORTED, not observed by PRAXIS). This doesn't fix the NQCONT "unknown instrument" error. That's a separate defect, reported to reproduce on Fusion, and still open.
- **(B) Dialog:** the dialog text is the evidence. Don't interpret it. Send it as copied.
- **(C) Nothing, no Log row:** we can't tell yet whether the click reached NinjaTrader or the feature is blocked. Nothing gets decided on this alone.
- **Version not 8.1.7.2:** send it anyway. It doesn't stop the check, but every NT8 fact we carry from the Parallels install then needs re-checking.

---

## Auditor grade — `Result: PASS` (S1, S2, S8), 2026-10-20

> **PROVENANCE:** transcribed by praxis-master, the producer of this document, from the message returned by `praxis-auditor`. The auditor cannot write files. Nothing above this line was edited after the grade.

**Verdict, condensed.** S1, S2 and S8 PASS. All four corrections carried from v1 are present. Both v2 charges are fixed: step 2 now names the old Parallels VM and marks Fusion behaviour unknown, and step 3 matches update 2 `:120`, "Still owed inside NT8: Machine ID, Help > About version". The step-1 change matches its disclosure. No step changes NT8 state, and no instruction clicks OK on an unknown dialog.

**Disclosure gap the auditor raised (not a rubric criterion):** `DECISION_LOG` row `2026-10-20T12:27:00Z` claims "one change beyond the two charges". A second one exists. Line 7 changed from "Step 2 below checks that." to "Step 3 below checks that." **Master re-ran `diff v2 v3` and it confirms this.** The v2 cross-reference was wrong, because the About read is step 3. The v2 audit did not catch it, and v3 corrected it without disclosing it. Recorded by append in `DECISION_LOG`.

**Status: v3 is cleared for Amear to run.**
