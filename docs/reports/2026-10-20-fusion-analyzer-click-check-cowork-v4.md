# Task for Claude Cowork (Fusion VM): does the Strategy Analyzer open when clicked?

**From:** the PRAXIS orchestrator, via Amear. **Date:** 2026-10-20.
**Rewritten from:** PRAXIS walkthrough v3, which was written for Amear's own hand.

## Hard limits (read first)

- **Read and click only.** Don't change any setting, pick any instrument, run any backtest, place or modify any order, or connect or disconnect anything.
- **Don't restart, close or reopen NinjaTrader.** On 2026-09-29 NT8 on the *old* Parallels VM was reported to delete its older log files at startup. Nobody knows whether NT8 on this VM does the same.
- **Don't type text.** Typed strings have been reported to arrive garbled on this VM, while clicks and single keys work (M-026, reported by the migration side). Use clicks only.
- **Never click OK** on a dialog you didn't expect. Use **Cancel**, or **Close** / the **X** if that's the only choice.
- **Don't troubleshoot.** If something doesn't work, record it and stop. Don't try another route.
- **Take a screenshot after every click** and keep them all.

## Why the controls matter

Earlier on the old VM, some automated clicks had no effect at all, with no window, no dialog and no log row. So "the Analyzer didn't open" means nothing unless we first know your clicks are arriving. Steps 2 and 3 are that check. **Report exactly what you saw, not what you expected.**

## Steps

1. **Starting state.** Confirm NinjaTrader's Control Center is open and visible. If NinjaTrader isn't running, **stop and report**. Don't start it. Note the Windows clock time.

2. **Click control 1: the About box.** In the Control Center menu bar, click **Help**.
   - Did the Help menu visibly open? (yes / no)
   - Click **About**. Did the About box open? (yes / no)
   - If it opened, record the **version** and the **Machine ID** exactly as shown, then close it with the **X**.
   - **If either answer is no, stop here and report.** The rest can't be interpreted.

3. **Click control 2: the Log tab.** In the Control Center, click the **Log** tab.
   - Did the view switch to the Log tab? (yes / no)
   - Record the time and message of the **newest row**. Leave the Log tab showing.

4. **The check.** In the Control Center menu bar, click **New**.
   - Did the New menu visibly open? (yes / no). **If no, stop and report.**
   - Click **Strategy Analyzer**, once.

5. **Wait 15 seconds**, then screenshot. A licence tooltip ("Please upgrade to a Lease or Lifetime license…") may appear. Note whether it did. Don't act on it.

6. **Record which happened:**
   - **(A)** A Strategy Analyzer window opened.
   - **(B)** A dialog or error box appeared. Copy its text exactly. Then click **Cancel**, or **Close** if that's the only button. Never OK.
   - **(C)** Nothing visible happened.

7. **Log tab again.** List every row newer than the one from step 3, with time and message copied exactly.

8. **If (C):** repeat step 4 once (New, then Strategy Analyzer). Record the result. Then stop.

9. **If (A):** screenshot the Analyzer window, then close it with its **X**. Don't touch anything inside it first. If a "save?" prompt appears, choose **No** or **Cancel**.

10. Leave NinjaTrader running as you found it.

## Report back (return this in chat; there's no shared folder on this VM)

Mark every item **OBSERVED** (you saw it, with a screenshot) or **NOT CHECKED**.

```
Clock at start:
Help menu opened on click (yes/no):
About box opened (yes/no):
NT8 version:
Machine ID:
Log tab switched on click (yes/no):
Newest Log row before check (time + message):
New menu opened on click (yes/no):
Result: A / B / C
Licence tooltip appeared (yes/no):
Dialog text (if B):
New Log rows after click (time + message):
Second try (if C): A / B / C
Screenshots taken (count):
Anything that didn't respond to a click:
How you clicked (tool/method used):
```

Don't interpret the result. Just report it.

---

## Auditor grade — `Result: FAIL` (S2; S1 and S8 PASS), 2026-10-20

> **PROVENANCE:** transcribed by praxis-master, the producer, from `praxis-auditor`'s returned message. The auditor cannot write files. Nothing above this line was edited after the grade.

**Not cleared for use.** S2 charges: (1) the menu paths and tooltip text are Parallels-install observations (reference `:5`), used for Fusion without saying so, and v3 `:7` disclosed this while v4 drops it; (2) "Steps 2 and 3 are that check" overstates the controls. HANDOFF `:19` shows target-dependent click failures, so passing controls don't show the final Strategy Analyzer click arrived. Further gaps: the Log-tab control has no stop gate; the About box is closed via the title-bar X, the control class that failed in session 53; three items dropped from v3: "Nothing gets decided on this alone", the version-mismatch warning, and the instruction for Amear to keep Parallels closed. Master re-checked HANDOFF `:19` and the v3/v4 differences: the charges reproduce.
