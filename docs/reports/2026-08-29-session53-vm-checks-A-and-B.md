PRAXIS - session 53 - TWO VM CHECKS. Both read-only. Change no setting.

Issued by praxis-master, 2026-08-29. Executor: Amear, by hand, on the Windows VM.
This file exists on disk so the brief survives transmission. Prior briefs were
garbled twice in the clipboard path; a citable artifact is the fix.


CHECK A - THE ANALYZER "unknown instrument NQCONT"

Standing facts, observed, not recalled:
  - Data is filed under the exact bare name NQCONT, no dated suffix,
    approx 1,857,362 records, in db\minute\NQCONT. (Amear, today.)
  - The Strategy Analyzer resolves bare NQCONT to NQCONT 09-2025 and throws
    unknown-instrument. (Amear, session 52.)
  - A Stock-typed duplicate NQCONT was deleted and the resolution persisted
    UNCHANGED, so the duplicate was not the cause. (Amear, session 52.)

A1. POSITIVE CONTROL. Run this one first.

Open Strategy Analyzer. Select any built-in NT8 instrument that already has
data - the standard NQ front-month contract is fine. Set the SAME 1-minute
interval and the SAME date range you used for NQCONT. Run it.

  - If it ALSO errors on requesting bars: the fault is in the data-series
    layer, not in NQCONT specifically. That supports the "records built but no
    usable bars series" idea.
  - If it RUNS CLEAN: the fault is specific to NQCONT's own definition, and the
    bars-series idea is dead.

FALSIFIER: a clean run on the control kills the bars-series theory outright.

A2. READ NQCONT'S DEFINITION, verbatim. Change nothing.

Tools, then Instruments. Find NQCONT. Open its properties. Read back, exactly
as printed, four things:

  1. Instrument type
  2. Expiry, or contract month, if any field carries one
  3. Merge Policy
  4. Whether any contract-month rows are listed beneath it, such as 09-25

WHY THIS FOUR: your data is filed under the bare name NQCONT. The Analyzer is
asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
is the correct answer to the wrong question. Something rewrites the request from
the root name into a contract month. These four fields are where that would
live.

FALSIFIER: if the definition shows no expiry, no contract months and no merge
policy, then nothing in the definition explains the rewrite and the framing
above is wrong. That is a useful answer, not a failed check.


CHECK B - THE RTH TEMPLATE HOURS

Standing fact: the CME US Index Futures RTH template prints 8:30 AM to 4:00 PM,
time zone shown as Central. (Amear, today.)

B1. TIME-ZONE TOGGLE. This tests whether the printed hours are a display
conversion or the actual stored definition.

Tools, then Trading Hours. Select the CME US Index Futures RTH template.

  1. Read the TIME ZONE control at the top of that window. Report its value.
  2. Read the session rows as printed now.
  3. Change ONLY the time zone control to Eastern. Read the same rows again.
  4. Set the time zone control back to what it was. Save nothing.

  - If the numbers CHANGE when the zone changes: the print is a converted
    display, and 4:00 PM Central was never a literal 4:00 PM setting.
  - If the numbers DO NOT change: the print is the definition and the hours are
    literal.

FALSIFIER: unchanged numbers kill the display-conversion explanation.

DO NOT change, correct or create any session template yet. Which session close
governs this system is NOT DECIDED - 11:30 Eastern (breaker #4), 16:00 Eastern
(Deviation B) and the 15:00 to 18:00 Eastern disable window (breaker #5)
contradict each other, and that contradiction is exactly what rubric criterion
F2 is frozen on. Measuring the template is fine. Choosing one is blocked until
F2 is ruled. The artifact that unblocks it: a DECISIONS.md entry naming the
governing rule and the 15:00 disposition, with breaker specs #4 and #5 amended
to match.


DO NOT RE-TEST. Both already refuted by your own observation:
  - the chart title bar carries no dated suffix
  - the chart interval is 1 minute, not Daily
