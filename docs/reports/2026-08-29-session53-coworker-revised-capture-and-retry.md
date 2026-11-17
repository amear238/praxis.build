PRAXIS - REVISED INSTRUCTIONS - 2026-08-29 - session 53
SUPERSEDES both the earlier task brief AND the halt-and-preserve note.

STATUS UPDATE, so you are not working blind: the state changes you flagged are
ACCOUNTED FOR. The system owner made them himself between roughly 11:39 and
12:18. There is no intrusion and no security question. You were still right to
stop - the baseline you were handed was stale, and stopping was the correct
call.

What changed is what we now want from that machine. We are no longer
diagnosing a broken chart. THE CHART IS RENDERING. We are now trying to
establish WHAT MADE IT WORK, before that information is lost.

Still change nothing. Everything below is read-only except step R1, which
loads a data series and stops.


P1. THE LOG ROWS ARE THE MOST VALUABLE THING ON THAT MACHINE. Do this first.

Control Center, Log tab. Transcribe EVERY row from 11:30 AM onward, verbatim
and in order: timestamp, level/category, full message text. Do not summarise,
do not skip repeats, do not truncate, do not fix apparent typos. Page back if
rows have scrolled. State the VM clock time when you finish.

WHY: several settings were changed in that window and we do not know which one
mattered, because they were not changed one at a time. This log is the only
durable record of the sequence. Human recollection of a GUI sequence is not a
substitute and we are not relying on it.


R1. RETRY THE STRATEGY ANALYZER. This is the whole question now.

Open the Strategy Analyzer. Select NQCONT. Set a 1-minute interval and a date
range inside 2026-01-01 to 2026-08-29. LOAD THE DATA SERIES AND STOP THERE.

DO NOT RUN A BACKTEST. Loading bars is not running a backtest. If it loads,
report that it loaded and stop. Running the strategy is blocked by a separate
gate that is not yours or mine to open.

Report, verbatim:
  - the exact instrument string the picker ends up showing
  - whether the data series loaded, or the exact error text if it did not
  - THE NEW LOG ROWS this attempt produces, with their timestamps

CRITICAL - READ THIS BEFORE REPORTING AN ERROR: an error string identical to
the previously recorded one is NOT evidence on its own. That exact string
already appears in our own documents from a July attempt. Only a log line with
a FRESH TIMESTAMP FROM YOUR ATTEMPT counts. If you report an error, report the
timestamp beside it, or the observation is worthless to us.


P2. SCREENSHOT before re-arranging anything: the already-open Instruments
properties dialog, the Log panel, the Instruments picker filtered "nq", and the
rendering chart including its title bar.


P3. THE RENDERING CHART - describe, do not touch. Title bar text verbatim,
interval, visible date range, and the timestamp plus OHLC of the most recent
visible candle. We need to know WHICH bars it serves, not just that it serves
some.


P4. INVENTORY. Tools, then Instruments, filter "nq". Every entry: exact name,
Type, Expiry if shown. Include the NQ-typed Stock and both NQCONT entries.


P5. Tools, then Historical Data, then Loaded. Every entry beginning "NQ":
exact full name, data type, record count. ALSO report the COLUMN HEADERS of
that list verbatim - they have never been recorded on our side and one of them
may be a Type column we have been guessing about.


P6. Connections. Which data feed is currently connected, and which are
configured. If the only intraday-capable feed is absent, several of our
assumptions change.


REPORT TO:
C:\Mac\Home\praxis-signals\b2-data\inbound\4uu-VM-capture-2026-08-29.md

Structure: P1, R1, P2, P3, P4, P5, P6. Mark every statement OBSERVED or NOT
CHECKED. Do not reconstruct what you think happened - report the record. If
something has an obvious explanation, give the observation and leave the
explanation out.

HARD LIMITS, unchanged: sim only, no orders, no backtest run, no import, no
rename, no delete, no settings changes in either direction, no web-fetch
workarounds. Real Windows paths only - your bash tool is an isolated Linux
sandbox that does not touch this machine.
