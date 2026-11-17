# NinjaTrader 8 — spoken walkthrough for Amear

**For voice mode. You are the one clicking. Read one part at a time.**

Derived from `4uu-VM-brief-v3.md` (2026-08-15), which was written for an agent
with GUI automation. This version is for hands.

---

## Before anything — what is and is not authorised today

**Parts 1 through 5 are clear. Do them.** Creating the instrument, importing,
checking alignment, compiling — none of that runs a backtest, so none of it
touches the frozen criterion.

**Part 6 is where it gets conditional.** Frozen criterion **F3** says the fill
resolution and the slippage assumption must be **written down and committed
before the backtest runs**. That statement does not exist yet, because the
slippage number is yours and you have not given it.

So Part 6 has two modes and you pick one:

- **Control mode** — run it twice to *measure* how NinjaTrader behaves. This is
  evidence gathering, it is allowed now, and the numbers are not used as results.
- **Result mode** — the real backtest whose numbers feed everything downstream.
  **Not authorised until the slippage number is committed.**

Nothing on this page places an order, arms a strategy, or touches a funded
account. If a dialog ever looks like it might, stop.

---

## Part 0 — Restart NinjaTrader. Actually restart it.

Fully close NinjaTrader, not just the window. Reopen it.

Then: **Control Center → Log tab.** Look for `UCEERR_RENDERTHREADFAILURE`.

- **Not there** → good, carry on.
- **It is there** → close and relaunch again. If it comes back, **stop.** There is
  a rendering fault where dialogs silently swallow your clicks — you will think
  you set a field and you will not have. Do not work around it.

**Say out loud:** whether the log was clean.

---

## Part 1 — Create the instrument. This is the actual blocker.

`NQCONT` **does not exist in NinjaTrader.** That is why every previous run died.
There is an empty folder called `NQCONT` under the minute data directory — that is
a decoy NinjaTrader created from a filename, not partial progress.

**Tools → Instruments → add a new instrument.**

Name it exactly: **`NQCONT`**

| Field | Value |
|---|---|
| Type | Future |
| Tick size | `0.25` |
| Point value | `20` (so tick value is $5) |
| Currency | USD |
| Trading hours template | `CME US Index Futures RTH` |
| Exchange | CME or Globex, if it asks |

Confirm `NQCONT` now appears in the instruments list before you move on.

**If the dialog demands a field you are not sure about — set what you can and
stop.** A wrong tick size or point value corrupts every number downstream without
ever looking wrong. That is the worst failure available here.

**Do not hand-edit the sqlite database.** Ever. For any reason.

**Say out loud:** whether `NQCONT` is now in the list.

---

## Part 2 — Import the data

The file is already staged and already correctly named. You do not need to copy or
rename anything.

**Tools → Historical Data.**

That window is a **vertical accordion** — Loaded, Download, Import, Export, Get
Market Replay. It is not a row of tabs. **Expand the Import section.**

Select this file:

`C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`

| Setting | Value |
|---|---|
| Format | `NinjaTrader (end of bar timestamps)` |
| Data Type | `Last` |
| **Time zone of imported data** | **US Eastern** |
| Tick to minute/day generation | leave **unchecked** |

**Two things that have killed this before, both worth saying out loud:**

**One — there is no instrument field on that panel.** NinjaTrader works out the
instrument from the *filename*. `NQCONT.Last.txt` is `<instrument>.<datatype>`.
An earlier run named the copy `NQ 12-25.txt` and it went nowhere.

**Two — the time zone box defaults to UTC.** The file is already Eastern
wall-clock. Leaving it on UTC shifts every bar four or five hours and quietly
destroys the 9:30 anchor the whole strategy is built on. **This is the defect that
killed the July 24th run.** Set it to US Eastern and look at it twice.

Press Import.

**Say out loud:** the time zone you set, and the row count it reports.

---

## Part 3 — Confirm it actually landed

Three checks:

1. A confirmation window appeared.
2. Control Center → Log tab shows no import errors.
3. The folder `Documents\NinjaTrader 8\db\minute\NQCONT\` is now **non-empty**.

**An empty folder means the import did not complete.** Report it and stop — do not
carry on and hope.

**Say out loud:** whether that folder has files in it now.

---

## Part 4 — Bar-stamp alignment. Do not skip this one.

**This is the step that decides whether everything else is meaningful.**

Our data stamps the RTH-open minute at **09:30:00**. NinjaTrader sometimes treats
a minute bar's stamp as the bar's *close* instead of its open. If it does that
here, our 09:30 bar gets read as the 09:29-to-09:30 bar, and the entire
9:30-anchored band shifts by one bar. Every entry in the backtest would then be
wrong — **and wrong plausibly**, which is worse than wrong obviously.

**Open two charts, both for 2026-07-17:**

- native `NQ 12-25` (this has real Kinetick data)
- the imported `NQCONT`

In our imported data that day you should see:

```
09:29:00   Open 28598.5
09:30:00   Open 28608.75     ← this should be the FIRST RTH bar
```

- **Native RTH open lines up with our 09:30:00 bar** → aligned. Carry on.
- **Our 09:30:00 lands one bar early**, sitting at native's pre-open → **STOP. Do
  not run the Analyzer.** The Mac side re-stamps and re-emits the file.

**Never adjust timestamps inside NinjaTrader.**

**Say out loud:** the verdict — aligned, or one bar early — and the two prices you
actually read off the charts.

---

## Part 5 — Compile

Open the NinjaScript Editor, load `PraxisNoiseAreaBreakout.cs`, press **F5**.

**Change nothing in the code.** If it does not compile, read the errors out
verbatim — full text, file and line number — and stop. Do not fix it.

Optional but worth doing, and it is a two-second check: hash the deployed file.

```
certutil -hashfile "%USERPROFILE%\Documents\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs" SHA256
```

| What you should see | |
|---|---|
| Deployed copy, Windows line endings, 14,630 bytes | `c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65` |
| Same file with carriage returns stripped, 14,318 bytes | `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` |

**About the 312-byte difference — this is expected, not a problem.** The file is
312 lines. Windows adds one extra byte per line. 14,630 minus 14,318 is exactly
312. A previous run halted on this and burned a session. If you see a 312-byte
delta, that is line endings, and you proceed.

I verified the second hash independently against the repository copy this session.

**Say out loud:** compiled or failed, and confirm both `PraxisNoiseAreaBreakout`
and `PraxisSignalConsumer` show up in the strategy list.

---

## Part 6 — Strategy Analyzer

**Read the top of this page again before you start this part.**

**New → Strategy Analyzer.** Add `PraxisNoiseAreaBreakout` on the imported
`NQCONT` 1-minute series.

| Setting | Value |
|---|---|
| Session template | `CME US Index Futures RTH` (09:30–16:00 ET) |
| ExitMode | `BandOrVWAP` |
| Contracts | `1` |
| Date range | at least 3 months, ending at the newest data |

`Lookback = 14` and the sigma multiplier of `1.0` are compiled into the code. They
are not in the UI and not optimizable. That is expected — do not go hunting.

### The setting the brief never mentions, and this is the whole of F3

Find **Order Fill Resolution** in the execution settings. **The operator brief
does not specify it. Neither does the version before it.** That omission is
exactly what F3 exists to catch.

**Control mode — this is what to do today:**

Run it **twice**, changing **one thing only**:

1. Run once with **Order Fill Resolution = Standard**. Record trade count, net
   profit, and the first five trades.
2. Run again with **Order Fill Resolution = High**, everything else byte-identical.
   Record the same three things.

**Then tell me three things:**

- Did the two runs produce **identical** results?
- When you set it to **High**, did NinjaTrader **ask you for a secondary series**,
  throw an error, or just accept it silently?
- What did the trade counts come out as?

**Why this matters:** the strategy only ever transacts at the top and bottom of
the hour, using plain market orders — I verified that in the source this session.
It places no resting stop or target inside a bar. So fill resolution *should* make
no difference at all. If the two runs match, that stops being an argument and
becomes an observed fact, and F3 mostly dissolves. If they differ, that difference
is itself the finding and we stop and think.

**Nobody has ever watched NinjaTrader do this with only 1-minute data loaded.**
That is the single unverified thing in the whole chain.

**Result mode — not yet.** The moment these numbers get used as *results* rather
than as a control, F3 requires the slippage assumption committed first. That is
the number I keep asking you for, and your own rule applies: **pick it before you
see the equity curve.**

If the run produces **zero trades**, that is a real result. Report it. Do not widen
the date range, do not change parameters, do not go looking for activity.

---

## Part 7 — The consistency checks

These are the acceptance criteria for `4uu`. Full list is in
`4uu-reconcile-checklist.md` on the share. Check each and say what you actually
saw, not just pass or fail:

- Band **widens through the day** and **re-anchors every 09:30**; VWAP starts at
  the open and is RTH-only
- Entries fire **only at `HH:00` and `HH:30`**
- **Long above** the band, **short below**
- An opposite-band cross **reverses** the position — it does not merely exit
- **Flat by 16:00** every single day
- Trade frequency is sane in order of magnitude

---

## Part 8 — Two things to look at but not touch

**One.** There is a file at
`Documents\NinjaTrader 8\NQ 12-25.txt`, about 95 MB, left over from the July run.
It is the *stitched continuous series* wearing the filename of the *real December
2025 contract*. If it ever gets imported it contaminates genuine contract data
with stitched prices — hard to spot, hard to undo. It is fully superseded.

**Do not delete it yet.** Tell me its size and date. The call is yours and you have
not made it.

**Two.** There are two sqlite backups from July 24th —
`NinjaTrader.sqlite.bak_praxis` and `.bak_praxis2`. They suggest someone was
getting ready to hand-edit the instrument database. **Do not judge whether that
happened** — NinjaTrader rewrites its own database in normal operation. Just tell
me the size and date of those two plus the live `NinjaTrader.sqlite`.

---

## If you get stuck

Stop at the step and say where. Do not improvise past a blocked gate, do not
hand-edit NinjaTrader internals, and do not call a step done that you could not
actually see.

A blocked step reported honestly is worth more than a finished step reported
vaguely. Every number this produces feeds a decision about real money later.
