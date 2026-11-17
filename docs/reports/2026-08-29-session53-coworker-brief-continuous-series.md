PRAXIS - BRIEF FOR THE VM COWORKER - 2026-08-29 - session 53

READ ALL OF THIS FIRST. It is self-contained on purpose; assume you have no
memory of prior sessions and do not go looking for context elsewhere.

You are working on the Windows 11 VM that hosts NinjaTrader 8 (version 8.1.7.2,
64-bit). Use REAL WINDOWS PATHS only. Your bash tool is an isolated Linux
sandbox that does NOT touch this Windows machine - do not use /mnt paths and do
not try to reach NinjaTrader through it. Drive NT8 through the GUI.


=== HARD LIMITS. Never work around these. ===

1. SIM ONLY. No trade execution, no money movement, no enabling live or
   sim-funded auto-trading. Nothing in this brief requires an order.
2. DO NOT RUN A BACKTEST. Loading bars is not running a backtest. If the
   Analyzer successfully loads a data series, STOP THERE and report it. Running
   the strategy is blocked by a separate frozen gate and is not yours or mine
   to open.
3. RECOMPUTE, NEVER PASTE. If any hash or record count is asked for, read it
   yourself off the machine. Do not repeat a figure from this brief as though
   you had observed it.
4. NO WEB-FETCH WORKAROUNDS. If a domain is blocked, that is a hard stop. Use
   the NT8 Help Guide that is INSTALLED LOCALLY, not the web version.
5. REVERT WHAT YOU TOGGLE. Task 4 changes one setting and changes it back. No
   other setting is modified. Do not re-import data, do not rename anything in
   Historical Data, do not delete an instrument, do not edit the Expiry field.


=== BACKGROUND - what is already known, all of it observed by hand ===

There is an instrument named NQCONT. It is meant to carry a CONTINUOUS,
back-adjusted NQ futures series that was stitched together OUTSIDE NinjaTrader
in Python, then imported. The goal was: pick bare "NQCONT" in the Strategy
Analyzer and get the whole continuous series.

Observed so far:

  - Historical Data, Loaded section: approximately 1,857,362 records are filed
    under the EXACT BARE NAME "NQCONT", no dated suffix. Storage confirmed at
    %USERPROFILE%\Documents\NinjaTrader 8\db\minute\NQCONT
  - The Strategy Analyzer resolves bare "NQCONT" to "NQCONT 09-2025" and then
    throws: error on requesting bars series, unknown instrument NQCONT
  - Tools, Instruments, NQCONT properties show: Type = Future,
    Expiry = 09-25, Rollover date = 12-01-2025, Merge Policy = Use Global
    Setting
  - Clearing the Expiry field FAILED. NT8 refuses to save a Future-type
    instrument with zero contract-month entries.
  - A duplicate NQCONT typed "Stock" once existed, was confirmed empty, and was
    deleted. The resolution behaviour did NOT change afterward.
  - A plain chart on NQCONT renders BLANK. Its title bar reads plain "NQCONT"
    with no dated suffix, and the interval is confirmed 1 minute, not Daily.
    BOTH of those were already tested. DO NOT RE-TEST THEM.

So the data is stored under one name and requested under a different name.
That much is established.

THE OPEN QUESTION, which nobody here has answered and which you should NOT
guess at: does NT8's Future instrument type support a genuinely bare,
rollover-free continuous series at all - or does every Future-type instrument
necessarily resolve to some dated contract by design?


=== TASK 1 - ASK THE VENDOR DOCUMENTATION, NOT ME ===

Open the LOCALLY INSTALLED NT8 Help Guide (Control Center, then Help, then Help
Guide). Find and quote VERBATIM whatever it says on each of these. If a topic
is not covered, say "NOT COVERED" - an honest null is worth more than a
paraphrase.

  1a. Continuous contracts. Does NT8 have a first-class continuous-contract
      concept for futures? What is it called and how is it selected?
  1b. Instrument expiry / contract months. Is at least one contract month
      mandatory for a Future-type instrument? Quote the text.
  1c. Merge Policy. What do the options mean - specifically "Use Global
      Setting", "Merge Back Adjusted", and "Do Not Merge"? What does each do
      to which bars get served to a chart or the Analyzer?
  1d. How historical data is keyed. Is data stored per contract month, or per
      instrument root? Does the Instruments picker and the Historical Data
      store use the SAME name, or can they differ?

Report the Help Guide's page or section title alongside each quote.


=== TASK 2 - POSITIVE CONTROL. Run this before drawing any conclusion. ===

Open the Strategy Analyzer. Select a BUILT-IN NT8 instrument that already has
data on this machine - the standard NQ front-month contract is fine. Set the
SAME 1-minute interval and the SAME date range that was used for NQCONT. Let it
load the data series. DO NOT RUN THE STRATEGY.

  - If it ALSO errors on requesting bars, the fault is in the data-series layer
    generally and is not specific to NQCONT.
  - If it LOADS CLEAN, the fault is specific to NQCONT's own definition.

Report which, verbatim, including any error text.


=== TASK 3 - NAMESPACE INVENTORY ===

Tools, then Historical Data, then expand the Loaded section.

List EVERY entry whose name begins with "NQ". For each one report, exactly as
displayed: the full name, the data type (Last / Bid / Ask), and the record
count.

WHY THIS MATTERS: we need to know whether an entry named "NQCONT 09-25" exists
as a SEPARATE, probably empty, storage key sitting alongside the bare "NQCONT"
entry. If it does, then the Instruments picker and the Historical Data store
are using the same namespace and the data is simply filed under the wrong key
in it. If no such entry exists, that reading is wrong.

Do not create, rename or delete anything. Read and report.


=== TASK 4 - ONE TOGGLE, THEN PUT IT BACK ===

This is a controlled experiment, not a fix. The point is to see whether Merge
Policy is the mechanism or merely a suspicious-looking setting.

  4a. Record the current Merge Policy value for NQCONT (expected: Use Global
      Setting - confirm it yourself).
  4b. Retry loading NQCONT in the Strategy Analyzer. Record the exact error.
  4c. Change ONLY Merge Policy to "Do Not Merge". Change nothing else.
  4d. Retry loading NQCONT in the Strategy Analyzer. Record the exact result.
  4e. SET MERGE POLICY BACK to its original value from 4a. Confirm in the
      properties dialog that it reverted, and say so explicitly in your report.

Report 4b and 4d side by side. If the behaviour is IDENTICAL, Merge Policy was
never the mechanism and we stop suspecting it. If it CHANGES, say exactly how.

DO NOT LEAVE Merge Policy changed. The decision to persist that setting has not
been made and is not yours or mine to make.


=== WHAT NOT TO DO ===

  - Do not run a backtest even if the data loads.
  - Do not re-import the CSV or rename anything under db\minute.
  - Do not edit the Expiry or Rollover fields.
  - Do not create a new instrument.
  - Do not recommend a fix. Report what you observed. Someone else decides.


=== HOW TO REPORT ===

Write your findings to:
C:\Mac\Home\praxis-signals\b2-data\inbound\4uu-VM-status-2026-08-29.md

Structure it as Task 1 / Task 2 / Task 3 / Task 4, in that order. For every
statement, mark it either OBSERVED (you saw it on screen this session) or
QUOTED (it came out of the Help Guide). If you did not check something, write
NOT CHECKED. Do not fill gaps with reasoning - the gaps are more useful to us
than a smooth account.
