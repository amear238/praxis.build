# Walkthrough: open the Strategy Analyzer by physical click (Fusion VM)

**For:** Amear, by hand. Not for Cowork or any automation.
**Written:** 2026-10-20 by praxis-master. Not auditor-graded.
**Question it answers:** does the Strategy Analyzer window open on the Fusion VM when you click it yourself?
**Scope:** open, look, close. **No** instrument picked, **no** backtest, **no** settings changed, **no** orders.
**Menu path source:** `docs/reference/2026-07-24-nt8-windows-reference.md` (lines 23, 60, 115), built from this NT8 install's own screenshots.

## Before you start (about 1 minute)

1. **Only one NinjaTrader.** Parallels must not be running on the Mac. If it is, quit it and stop here. Tell me and we restart this later.
2. **NinjaTrader is open in the Fusion VM**, with the Control Center visible.
3. **Note the clock.** Write down the Windows time (bottom-right of the VM screen). You'll compare it against the Log tab later.

## The check (about 2 minutes)

4. In the Control Center, click the **Log** tab. Note the time on the **newest row** and leave the tab showing.
5. In the Control Center menu bar, click **New**, then click **Strategy Analyzer**. Use the mouse or trackpad and **click once**. Don't use the keyboard: typed input into this VM is known to arrive garbled.
6. **Wait 15 seconds** and watch the screen. The licence tooltip ("Please upgrade to a Lease or Lifetime license…") may appear. **Ignore it.** It was there on 2026-07-24 when the Analyzer worked normally.
7. Record which of these happened:
   - **(A) A Strategy Analyzer window opened.**
   - **(B) A dialog or error box appeared.** Copy its text exactly, or take a screenshot. Then click **Cancel**, or **Close** if that's the only button. **Never click OK.**
   - **(C) Nothing at all happened.**
8. Look at the **Log** tab again. Did any new row appear after the time from step 4? If yes, copy its time and message exactly.

**If (C):** try once more, the same way (New, then Strategy Analyzer, one click). Then stop. Don't troubleshoot, restart NT8, or try other routes.

## Closing up

9. **If (A):** take one screenshot of the Analyzer window. Then close it with the **X** at its top-right. If a "save?" prompt appears, choose **No** or **Cancel**. Don't touch anything inside the window first.
10. Leave NinjaTrader running as it was. Nothing else to undo.

## What to send back

```
Clock at start:
Newest Log row before click (time):
Result: A / B / C
Dialog text (if B):
New Log rows after click (time + message):
Second try (if C): A / B / C
Screenshot taken: yes / no
```

## What each result means

- **(A) Opens:** the Analyzer works on Fusion and the licence-gate theory is dead here too. This doesn't fix the NQCONT "unknown instrument" error. That's a separate defect and still open.
- **(B) Dialog:** the dialog text is the evidence. Don't interpret it. Send it as copied.
- **(C) Nothing, no Log row:** we can't tell yet whether the click reached NinjaTrader or the feature is blocked. Nothing gets decided on this alone.
