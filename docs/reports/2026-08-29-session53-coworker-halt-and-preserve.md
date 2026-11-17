PRAXIS - HALT AND PRESERVE - 2026-08-29 - session 53
SUPERSEDES the earlier brief. Tasks 2, 3 and 4 are CANCELLED. Do not run them.

You were right to stop and flag. Do not proceed with the experiment. The
baseline you were given no longer describes the machine, so any result you
produced now would be uninterpretable - we would not be able to tell your
effect from someone else's.

CHANGE NOTHING FROM THIS POINT. Specifically:
  - Do NOT change Merge policy, in either direction. It currently reads
    "Do not merge". Leave it exactly as it is. We did not set it and we do
    not yet know who did.
  - Do NOT delete the Stock-typed NQCONT, or the NQ-typed Stock entry.
  - Do NOT close, refresh or re-open the chart that is rendering.
  - Do NOT close the Instruments properties dialog that was already open.
  - Do NOT run a backtest, an import, or a data repair.

Your only job now is to PRESERVE AND DESCRIBE. All of this is read-only.

P1. THE LOG ROWS ARE THE MOST IMPORTANT ARTIFACT ON THAT MACHINE RIGHT NOW.
Control Center, Log tab. Transcribe EVERY row from 11:50 AM onward, verbatim
and in order: timestamp, category/level, and the full message text. Do not
summarise, do not skip repeats, do not truncate. If rows scroll off, page
back. Also state the current VM clock time when you finish, so we can bound
the window.

P2. SCREENSHOT, do not re-arrange windows first. Capture, as they sit:
  - the Instruments properties dialog that was already open
  - the Log panel showing the 11:58-12:01 rows
  - the Instruments picker filtered "nq", showing every entry
  - the chart that is rendering candles, INCLUDING its title bar and the
    data-series settings if they are already visible

P3. INVENTORY, read-only. Tools, then Instruments, filter "nq". List EVERY
entry: exact name, Type, and Expiry if shown. Include the NQ-typed Stock.

P4. THE RENDERING CHART - describe without touching. Report its title bar
text verbatim, its interval, its visible date range, and the timestamp and
OHLC of the most recent visible candle. We need to know WHICH bars it is
serving, not merely that it is serving some.

P5. Tools, then Historical Data, then Loaded. List every entry beginning
"NQ": exact full name, data type, record count. Report the COLUMN HEADERS of
that list verbatim as well - we have never had them recorded.

P6. Connections. Report which data feed is currently connected and which are
configured. This is not incidental: if the only intraday-capable feed is
absent, several of our assumptions change.

REPORT TO:
C:\Mac\Home\praxis-signals\b2-data\inbound\4uu-VM-forensics-2026-08-29.md

Mark every statement OBSERVED or NOT CHECKED. Do not explain what you think
happened. We specifically do not want a reconstruction - we want the record.
If something looks like it has an obvious explanation, report the observation
and leave the explanation out.
