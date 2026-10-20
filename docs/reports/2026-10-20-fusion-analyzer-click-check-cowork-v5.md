# Task for Claude Cowork (Fusion VM): does the Strategy Analyzer open when clicked?

**From:** the PRAXIS orchestrator, via Amear. **Date:** 2026-10-20.
**Rewritten from:** PRAXIS walkthrough v3 (written for Amear's own hand). Supersedes Cowork brief v4, which failed audit.
**Amear, before you paste:** make sure Parallels is **not** running on the Mac, and keep it closed while Cowork works. Cowork can't see the Mac.

**Where the menu paths come from:** a NinjaTrader reference built from screenshots of the **old Parallels VM** (NT8 8.1.7.2), in 2026-07. The migration side reports the same version is installed here (REPORTED). Nobody has confirmed the menus on this VM yet. Step 2 reads the version. If a menu item below isn't where this says, stop and report it. Don't search for it.

## Hard limits (read first)

- **Read and click only.** Don't change any setting, pick any instrument, run any backtest, place or modify any order, or connect or disconnect anything.
- **Don't restart, close or reopen NinjaTrader.** On 2026-09-29, NT8 on the *old* Parallels VM was reported to delete its older log files at startup. Nobody knows whether NT8 on this VM does the same.
- **Don't type text.** Typed strings have been reported to arrive garbled on this VM, while clicks and single keys work (M-026, reported by the migration side). Use clicks only.
- **Never click OK** on any dialog. Use **Cancel**, or **Close** / the **X** if that's the only choice.
- **Don't troubleshoot.** If something doesn't work, record it and stop. Don't try another route.
- **Take a screenshot after every click** and keep them all.

## Why the controls exist, and what they can't do

On the old VM, some automated clicks had no effect: no window, no dialog, no log row. Which clicks failed depended on what was being clicked. Steps 2–4 check that your clicks reach this NinjaTrader on menus and tabs. **They can't prove that your final click on "Strategy Analyzer" arrived.** So report exactly what you saw, not what you expected.

## Steps

1. **Starting state.** Confirm NinjaTrader's Control Center is open and visible. If NinjaTrader isn't running, **stop and report**. Don't start it. Note the Windows clock time.

2. **Control 1: the About box.** In the Control Center menu bar, click **Help**.
   - Did the Help menu visibly open? (yes / no). **If no, stop and report.**
   - Click **About**. Did the About box open? (yes / no). **If no, stop and report.**
   - Record the **version** and the **Machine ID** exactly as shown.
   - Close the About box with its **X**, or a button labelled **Close**. Not OK.
   - **Screenshot, and confirm the About box is gone and the Control Center isn't covered by anything.** If the box won't close after one try, **stop and report**. Don't continue with it open.

3. **Control 2: the Log tab.** In the Control Center, click the **Log** tab.
   - Did the view switch to the Log tab? (yes / no). **If no, stop and report.**
   - Record the time and message of the **newest row**. Leave the Log tab showing.

4. **Control 3 and the check.** In the Control Center menu bar, click **New**.
   - Did the New menu visibly open? (yes / no). **If no, stop and report.**
   - Click **Strategy Analyzer**, once.
   - Right after the click: **did the New menu close?** (yes / no / not sure). Screenshot.

5. **Wait 15 seconds**, then screenshot. A licence tooltip ("Please upgrade to a Lease or Lifetime license…") may appear. Note whether it did. Don't act on it.

6. **Record which happened:**
   - **(A)** A Strategy Analyzer window opened.
   - **(B)** A dialog or error box appeared. Copy its text exactly. Then click **Cancel**, or **Close** if that's the only button. Never OK.
   - **(C)** Nothing visible happened.

7. **Log tab again.** List every row newer than the one from step 3, with time and message copied exactly.

8. **If (C):** repeat step 4 once (New, then Strategy Analyzer), with the same questions. Record the result. Then stop.

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
About box closed, Control Center unobstructed (yes/no):
Log tab switched on click (yes/no):
Newest Log row before check (time + message):
New menu opened on click (yes/no):
New menu closed after Strategy Analyzer click (yes/no/not sure):
Result: A / B / C
Licence tooltip appeared (yes/no):
Dialog text (if B):
New Log rows after click (time + message):
Second try (if C): A / B / C, and did the New menu close
Screenshots taken (count):
Anything that didn't respond to a click:
Any menu item not where this brief said:
How you clicked (tool/method used):
Where you stopped, if early (step number):
```

Don't interpret the result. Just report it.

## How PRAXIS will read your result (context only; don't act on it)

- **(A) Opens:** the licence-gate theory is dead **on Fusion**. The Parallels question stands as relayed: on 2026-09-29 the migration side reported the Analyzer opening on a physical click there (REPORTED, not observed by PRAXIS). This doesn't touch the NQCONT "unknown instrument" error, which is a separate defect, reported to reproduce here, and still open.
- **(B) Dialog:** the dialog text is the evidence, as copied.
- **(C) Nothing:** **nothing gets decided on this alone**, even if every control passed. An automated click on the item may not have arrived. Amear then repeats the check by hand.
- **A stop at a control:** that's a result about automated clicks on this VM, not about the Analyzer.
- **Version not 8.1.7.2:** every NT8 fact PRAXIS carries from the Parallels install then needs re-checking.

---

## Auditor grade — `Result: FAIL` (survival check vs v3; S1, S2, S8 PASS), 2026-10-20

> **PROVENANCE:** transcribed by praxis-master, the producer, from `praxis-auditor`'s returned message. The auditor cannot write files. Nothing above this line was edited after the grade.

**Not cleared for use.** (1) v3 `:11` "stop here and tell me. Don't quit it yourself." was weakened to "make sure Parallels is not running", which invites quitting the old VM (update 2 `:33`: it "crashed while suspending"). No justification was given. (2) v3 `:54` "send it anyway. It doesn't stop the check" was dropped. (3) Step 9 closes the Analyzer via its X, the control class that failed in session 53 (HANDOFF `:19`), with no confirm-closed step, stop or report field. The disclosed residual named the About box only. (4) Minor: the New-menu-closes check is never labelled as partial evidence in the text. The master re-checked (1)-(3) against v3: they reproduce. The master's survival check had diffed v4 against v5 only.
