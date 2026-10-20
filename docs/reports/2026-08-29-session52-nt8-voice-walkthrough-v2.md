# NinjaTrader 8 — spoken walkthrough, v2

**v2 replaces the first version, which gave you settings tables instead of
click-paths. Everything here is grounded in
`docs/reference/2026-07-24-nt8-windows-reference.md`, which was built from 20
screenshots of your actual install (8.1.7.2, Windows 11 VM) on 2026-07-24.**

Where I know a thing from those screenshots I say **confirmed**. Where I'm going
on the Help Guide only, I say **unverified**. Don't let me blur those.

---

## Orientation — 30 seconds, then we start

**The Control Center is the root window.** It's the one that's always open. Every
other window comes from one of two menus on its top bar:

- **`New`** → working windows. Chart, Strategy Analyzer, NinjaScript Editor.
- **`Tools`** → managers and utilities. Instruments, Historical Data, Trading Hours.

That's the whole navigation model. If you're lost, go back to the Control Center.

**Its tabs, left to right:** Orders · Executions · Strategies · Positions ·
Accounts · **Log** · Messages.

**The `Log` tab is where things go to fail quietly.** Import errors, compile
errors, connection problems. When something doesn't work and doesn't tell you why,
that's the first place you look. We'll come back to it repeatedly.

### One thing that will alarm you, and shouldn't

**Confirmed on your install:** NinjaScript Editor, Strategy Analyzer, Strategy
Builder and a few others show a tooltip saying *"Please upgrade to a Lease or
Lifetime license to unlock this feature."*

**Every one that was actually opened during the capture opened and worked
normally.** The gating is tooltip-only on this install. Ignore the tooltip.

### One thing that should alarm you

**A chart window carries Chart Trader — live `Buy Mkt` and `Sell Mkt` buttons,
near the right edge of the canvas.** During the screenshot capture it was opened
by accident. Nothing was clicked.

When we get to the chart step in Part 4, **keep your clicks to the left two-thirds
of the chart.** Don't go exploring near the right edge.

---

## Part 0 — Restart, then check the log

1. Close NinjaTrader completely. Not the window — the application.
2. Reopen it.
3. Control Center → click the **`Log`** tab.
4. Scan for `UCEERR_RENDERTHREADFAILURE`.

**If you see it:** close and relaunch once more. If it returns, **stop and tell
me.** That's a rendering fault where dialogs accept your click but don't register
it — you'll set a field, it'll look set, and it won't be. Everything downstream
would be built on a lie. Not worth working around.

**Say out loud:** "log clean" or read me the error line.

---

## Part 1 — Create the `NQCONT` instrument

**This is the actual blocker.** Every previous attempt died here. `NQCONT` does
not exist in your instrument database — confirmed 2026-07-25 by scanning the
4.4 MB `NinjaTrader.sqlite` where instruments actually live. It appears only in
log files, never in the database.

There *is* an empty folder named `NQCONT` under the minute-data directory.
**That's a decoy** — NinjaTrader made it from a filename, then failed because the
instrument was unknown. The log says so four times:
`Error on requesting bars series: 'Unknown instrument 'NQCONT''`

**Steps:**

1. Control Center → **`Tools`** menu → **`Instruments`**.
2. The Instruments manager opens. **Confirmed layout:** a grid with columns
   **Name / Type / Description**, an **"All"** filter dropdown, and a **search
   box**.
3. **The add / edit / remove buttons are at the BOTTOM of that window.** Not the
   top. That's where people hunt.
4. Click **add**.
5. Fill in:

| Field | Value |
|---|---|
| Name | `NQCONT` — exactly, all caps, no spaces |
| Type | `Future` |
| Tick size | `0.25` |
| Point value | `20` |
| Currency | `USD` |
| Trading hours | `CME US Index Futures RTH` |
| Exchange | `CME` or `Globex` if it asks |

6. Save, then **use the search box to find `NQCONT` in the grid.** Don't move on
   until you've seen it listed.

**If a field is demanded that isn't in that table — set what you can and stop.**
A wrong tick size or point value silently corrupts every number downstream. It
won't look wrong. It'll just be wrong.

**Never hand-edit `NinjaTrader.sqlite`.** For any reason.

**Say out loud:** whether `NQCONT` is in the grid now.

### Optional, and it closes a known gap

While you're in Tools: open **`Tools > Trading Hours`** and find the
**`CME US Index Futures RTH`** template. **Nobody has ever confirmed its actual
printed hours.** The reference flags this as an open gap — we've assumed
09:30–16:00 ET and never checked.

Read me the printed hours. It may print in **Central**, in which case 08:30–15:00
CT is what we want to see.

---

## Part 2 — Import the data

The file is already staged and already named correctly. **No copying, no
renaming.** That's done.

1. Control Center → **`Tools`** → **`Historical Data`**.
2. ⚠️ **This window is a vertical accordion, not tabs.** Stacked collapsible
   sections: **Loaded · Download · Import · Export · Get Market Replay data**.
   The public Help Guide shows a horizontal tab strip — **that's wrong for your
   version.** Confirmed on your install.
3. **Expand `Import`.** Not `Download`.

   **This trips people:** the `Download` section *has* an Instrument field. The
   `Import` section *doesn't*. If you're looking at a box asking for an
   instrument, **you're in the wrong section.**

4. The Import section has exactly four things — confirmed:

| Field | Set it to |
|---|---|
| Format | `NinjaTrader (end of bar timestamps)` |
| Data Type | `Last` |
| **Time Zone of Imported Data** | **`US Eastern`** |
| (tick-only checkboxes) | leave unchecked — this is minute data |

5. Click **`Import`**. A normal Windows file-picker opens.
6. Navigate to and select:
   `C:\Mac\Home\praxis-signals\b2-data\NQCONT.Last.txt`
7. Click **`Open`**.

### The two failures that have already happened here

**One — there is no instrument field, by design.** NinjaTrader works out the
target instrument **from the filename**. The form is
`<instrument>.<DataType>.txt`. So `NQCONT.Last.txt` means instrument `NQCONT`,
data type `Last`. The `.Last` token **must match** what you picked in the Data
Type dropdown.

The 7/23 run named its copy `NQ 12-25.txt` — no `.Last` token — and it failed with
*"Instrument is not supported by repository."*

**Two — the time zone box defaults to UTC, and that killed the 7/24 run.** The
file's timestamps are already Eastern wall-clock. Leaving it on UTC shifts every
bar by four or five hours, which destroys the 09:30 anchor the entire strategy is
built on — and it fails *silently*. Everything still runs. The numbers are just
wrong.

**Set it to US Eastern and look at it twice before you click Import.**

**Say out loud:** the time zone you set, and anything the confirmation window
tells you.

---

## Part 3 — Confirm the import landed

Three checks, all quick:

1. **A confirmation window appeared.**
2. Control Center → **`Log`** tab → no new import errors.
3. On disk: `Documents\NinjaTrader 8\db\minute\NQCONT\` is now **non-empty**.

**That third one is the real check.** An empty folder means the import didn't
complete, regardless of what any dialog said.

**If it's empty: stop.** Don't proceed and hope.

**Say out loud:** whether that folder has files in it.

---

## Part 4 — Bar-stamp alignment. This is the one that matters.

**If you skip one step in this document, don't let it be this one.**

Our file stamps the RTH-open minute as **09:30:00**. NinjaTrader sometimes treats
a minute bar's timestamp as the bar's **close** rather than its open. If it does
that here, our 09:30 bar gets read as the 09:29-to-09:30 bar, and the entire
09:30-anchored noise band shifts by one bar.

Every entry in the backtest would then be wrong — **and wrong plausibly.** It
would produce a clean-looking equity curve built on a one-bar offset. That's worse
than an obvious failure.

**Steps:**

1. Control Center → **`New`** → **`Chart`**.
2. Set the instrument to **`NQCONT`**, interval **1 minute**, and navigate to
   **2026-07-17**.
3. Open a second chart the same way, on **`NQ 12-25`** — that one has real
   Kinetick data to compare against.
4. **Keep your clicks away from the right edge** — Chart Trader lives there.

**In our imported `NQCONT` data on 2026-07-17 you should see:**

```
09:29:00   Open 28598.5
09:30:00   Open 28608.75     ← should be the FIRST RTH bar
```

**The verdict:**

- **Native `NQ 12-25` RTH open lines up with our 09:30:00 bar** → aligned.
  Proceed.
- **Our 09:30:00 sits one bar early**, matching native's *pre-open* → **STOP.**
  Do not run the Analyzer. The Mac side re-stamps the file and re-emits it.

**Never adjust timestamps inside NinjaTrader.** If it's misaligned, the fix
happens upstream.

**Say out loud:** the verdict, and the two prices you actually read off the
charts — not the ones printed above.

---

## Part 5 — Compile

1. Control Center → **`New`** → **`NinjaScript Editor`**.
2. Ignore the license tooltip.
3. The **NinjaScript Explorer tree is on the left.** Open
   `PraxisNoiseAreaBreakout.cs` from it.
4. Press **`F5`**. (Confirmed on your install. There's also a **Compile** button
   in the toolbar — Print, Print Preview, NinjaScript Output, Find, **Compile**,
   Open in Visual Studio.)

**Change nothing in the code.**

### Two things about compiling that surprise people

**One — F5 compiles every NinjaScript file in your library, not just the open
one.** So an error can appear from a file you never touched. That's normal.

**Two — errors appear in a panel at the bottom of the Editor.** Each row is
**filename · description · line and column**. Errors in the open file render
lighter; errors in other files render darker. **Double-click a row to jump to
it.** The offending code gets a red wavy underline. Compile messages also echo to
the Control Center `Log` tab.

**If it fails: read me the error rows verbatim** — filename, line number, full
text. Don't fix anything.

**If it succeeds:** confirm both `PraxisNoiseAreaBreakout` and
`PraxisSignalConsumer` are in the compiled strategy list.

### Optional hash check — two seconds, and it has burned a session before

```
certutil -hashfile "%USERPROFILE%\Documents\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs" SHA256
```

| Expect | |
|---|---|
| Deployed copy, Windows line endings, 14,630 bytes | `c22f38fa148e2175058286199821e679289b7f3779e402e9734a77f2523caa65` |
| Same file, carriage returns stripped, 14,318 bytes | `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` |

**The 312-byte gap is expected.** The file is 312 lines; Windows adds one byte per
line; 14,630 − 14,318 = 312 exactly. **A previous run halted on this and lost a
session.** If you see 312, that's line endings. Carry on.

I verified the second hash against the repo copy myself this session.

---

## Part 6 — Strategy Analyzer

**Read this whole part before you click anything.**

1. Control Center → **`New`** → **`Strategy Analyzer`**. Ignore the tooltip.
2. At the top there's a **Backtest type** control. Leave it on **`Backtest`**
   (the others are Optimization, Multi-Objective, Walk-Forward — not today).
3. **The configuration lives in the left-hand properties panel**, in groups.
   Confirmed groups, in order:

**Group: Strategy**
- Pick `PraxisNoiseAreaBreakout`. **Confirmed:** it sits under the custom category
  **"02. Praxis (tunable)"**, not with the samples.

**Group: Data Series**
- Instrument → `NQCONT`
- Price based on → `Last`
- Type → `Minute`
- Value → `1`

**Group: Time frame**
- Start date / End date → **at least 3 months**, ending at the newest data. The
  band needs 14 warm-up days.
- **Trading hours** → session template dropdown → `CME US Index Futures RTH`
- Break at EOD → leave default

**Group: Execution** ← **this is the group that matters today**
- Include commission
- **Order fill resolution**
- **Slippage (ticks)**
- Bars required to trade
- Max bars look back
- Entry handling

**`Lookback = 14` and the sigma multiplier `1.0` are compiled into the code.**
They are not in the UI and not optimizable. Don't go hunting for them.

### What to actually do today — the control experiment

**The operator brief never specifies `Order fill resolution`, `Slippage`, or
`Include commission`. Neither did the version before it.** That omission is the
whole of frozen criterion F3.

So today we don't produce a result. We produce a measurement.

**Run it twice, changing exactly one thing:**

**Run A** — set **`Order fill resolution` = `Standard`**. Click **`Run`**. Record:
total trades, net profit, and the first five trades.

**Run B** — change **only** `Order fill resolution` to **`High`**. Everything else
identical. Click **`Run`**. Record the same three things.

**Then tell me:**

1. Did the two runs produce **identical** trade lists?
2. When you set it to **`High`**, did NinjaTrader **ask you for a secondary data
   series**, throw an error, or just accept it silently?
3. What were the two trade counts?

**Why:** I read the strategy source this session. It only transacts at `HH:00` and
`HH:30` using plain market orders — no resting stop, no resting target, nothing
sitting inside a bar. So fill resolution *should* make no difference whatsoever.
If the two runs match, that stops being my argument and becomes an observed fact,
and F3 mostly dissolves.

**Question 2 is the one nobody has ever answered.** No one has watched NinjaTrader
handle `High` with only 1-minute data loaded. Whatever it does, tell me exactly
what you saw.

**What we're not doing today:** treating these numbers as *results*. The moment
they're results rather than a control, F3 requires the slippage assumption
committed first — and that's the number I still need from you. Your own rule:
pick it before you see the equity curve.

**If a run produces zero trades, that's a real result.** Report it. Don't widen the
date range, don't change parameters, don't go looking for activity.

---

## Part 7 — The consistency checks

These are the acceptance criteria for `4uu`. Settled 2026-07-23: there's no
external TradingView corpus to reconcile against, because this strategy is a paper
re-implementation that never ran on TV. These self-contained checks are the whole
test. Full list in `4uu-reconcile-checklist.md` on the share.

Look at a chart with the strategy applied and check each — **and tell me what you
saw, not just pass or fail**:

- Band **widens through the day** and **re-anchors every 09:30**; VWAP starts at
  the open, RTH only
- Entries fire **only at `HH:00` and `HH:30`**
- **Long above** the band, **short below**
- An opposite-band cross **reverses** the position — it doesn't just exit
- **Flat by 16:00**, every day
- Trade frequency is sane in order of magnitude

---

## Part 8 — Two things to report and not touch

**One — a mislabelled 95 MB file.**
`Documents\NinjaTrader 8\NQ 12-25.txt`, left from the July run. It's the
*stitched continuous series* wearing the filename of the *real December 2025
contract*. If it's ever imported it contaminates genuine contract data with
stitched prices — hard to spot, hard to undo. Fully superseded by
`NQCONT.Last.txt`.

**Don't delete it.** Tell me its size and date. The call is yours and you haven't
made it.

**Two — two sqlite backups.** `NinjaTrader.sqlite.bak_praxis` and `.bak_praxis2`,
both from 7/24, both live-DB size. They suggest someone was preparing to hand-edit
the instrument database.

**Don't judge whether anything happened** — NinjaTrader rewrites its own database
in normal operation, so a difference isn't evidence. Just read me size and date
for those two plus the live `NinjaTrader.sqlite`.

---

## If something goes wrong

Stop at that step and tell me where. Don't improvise past a blocked gate, don't
hand-edit NinjaTrader internals, don't mark a step done you couldn't actually see.

A blocked step reported honestly beats a finished step reported vaguely. Every
number this produces feeds a decision about real money later.

---

## Quick reference — every click path in one place

| Task | Path |
|---|---|
| Check the log | Control Center → `Log` tab |
| Create an instrument | `Tools` → `Instruments` → add (**bottom** of window) |
| Check session hours | `Tools` → `Trading Hours` |
| Import data | `Tools` → `Historical Data` → expand **`Import`** |
| Compile | `New` → `NinjaScript Editor` → **`F5`** |
| Backtest | `New` → `Strategy Analyzer` |
| Chart | `New` → `Chart` |
