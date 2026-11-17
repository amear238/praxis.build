# Blank NQCONT chart + Analyzer auto-resolve — one defect, not two

**Follow-on to `2026-08-29-session52-nqcont-continuous-instrument-investigation.md`.
Append-only.**

Grades: **VERIFIED** = confirmed against `docs/reference/2026-07-24-nt8-windows-
reference.md` (20 screenshots of this install) or measured this session.
**INFERRED** = reasoning from verified facts. **UNVERIFIED** = not known.

---

## The two reports are the same defect, and the dates prove it

**Reported:**

- **A** — plain chart, instrument field reads bare `NQCONT`, range
  **2026-01-01 → 2026-08-29**, no bars at any zoom or scroll position.
- **B** — Strategy Analyzer instrument picker auto-resolves bare `NQCONT` to
  **`NQCONT 09-2025`**.

**Now put B's resolved contract next to A's window:**

| | |
|---|---|
| Analyzer resolves to | **September 2025** |
| Chart window requested | **January 2026 → August 2026** |
| Your imported data spans | **2021-03-07 → 2026-07-20** (VERIFIED, brief §A2) |

**INFERRED, high confidence:** the chart is resolving to a dated contract too. The
Data Series field displays the root you typed; **it does not display what NT8
resolved it to.**

Two things support this rather than one:

1. **VERIFIED (reference §6):** *"NT8 can also display months as a month
   abbreviation — the chart during capture read `MNQ SEP26`."* So the resolved
   expiry surfaces **in the chart title**, in a different format than you typed.
   You have been reading the input field, not the output.
2. **B proves the substitution is systemic.** It happens in the Analyzer's picker,
   in the instrument dialog, and — on this reading — in the chart. It is not a
   quirk of one dialog. **It is what `Future` type does**, exactly as Q1 concluded:
   contract-month resolution is inseparable from the type.

**So your Part 4 fix does not apply here because the range was never the problem.**
The chart is asking for `NQCONT 09-25`, which has **zero bars** — nothing was ever
imported under that name — and which sits *before* your window regardless.

---

## ⛔ The check I asked for is still unrun, and it gates everything below

**`Tools > Historical Data` → expand `Loaded` → read the exact instrument name the
~1,857,362 records are filed under.**

Thirty seconds. It is the only observation that separates *"data exists, keyed to
an unreachable name"* from *"data is not where we think it is at all."*

**Every fix below assumes the first.** If `Loaded` shows something dated, or shows
nothing, the whole analysis is wrong and none of the fixes should be attempted.

**Please run this before anything else.**

---

# Symptom A — checks, in order, cheapest first

## A1. ⭐ Read the chart's TITLE BAR, not the Data Series field

The window title / tab label. Does it say `NQCONT`, or `NQCONT 09-25`, or
`NQCONT SEP25`?

**VERIFIED** that the title carries the expiry in abbreviated form (§6, the
`MNQ SEP26` capture).

**If the title carries an expiry → diagnosis confirmed, stop testing, go to the
fixes.** This one observation likely closes the question.

## A2. Check the chart interval — it may be Daily

**VERIFIED (§1d):** the chart opened during capture was on **`MNQ SEP26`, Daily**.
**Daily may be this install's default for a new chart.**

You imported **minute** bars only.

**UNVERIFIED:** whether NT8 synthesises daily bars from imported minute data.
§2 documents tick→minute/day generation as an *import-time option for tick data*,
and says nothing about minute→daily.

**So a Daily chart over minute-only data is a live candidate for a blank render,
independently of the naming problem.** Right-click → `Data Series…` and confirm
**Type = Minute, Value = 1**.

**This is worth checking even after A1 confirms** — you may be looking at two
stacked causes.

## A3. Chart the dated symbol explicitly

Type **`NQCONT 09-25`** into the chart's instrument field directly.

- **Also blank** → consistent, confirms no data under the dated name. Expected.
- **Renders bars** → my model is wrong. Stop and tell me.

## A4. Connection status

**VERIFIED (§0, §1h):** Simulated Data Feed showed connected (green) during
capture; aggregate status sits **bottom-left of the Control Center**.

**UNVERIFIED:** whether NT8 renders purely local historical data with no connection
active. It may attempt a provider request and fail quietly.

Check the indicator. If disconnected, connect the **Simulated Data Feed** and
re-open the chart.

## A5. Trading Hours template — a known unverified gap

**VERIFIED as an open gap:** reference §4 and residual gap #1 both record that the
**`CME US Index Futures RTH` template's actual printed hours were never
captured.** We have assumed 09:30–16:00 ET and never confirmed it.

A session template that excludes your bars' timestamps renders an empty chart with
no error.

`Tools > Trading Hours` → find that template → **read me the printed hours and the
time zone they are printed in.** It may print in Central.

## A6. Merge Policy

**VERIFIED (§6):** per-instrument at `Tools > Instruments` → select → **Edit** →
**Merge policy**. Options: `MergeBackAdjusted` · `MergeNonBackAdjusted` ·
`DoNotMerge` · `UseGlobalSetting`.

**INFERRED:** with a merge policy active and contract months that have no data, NT8
may attempt to stitch across empty expiries and render nothing.

Set **`DoNotMerge`** — VERIFIED as *"single expiry only."* You have one nominal
expiry and no real rollover; merging can only add artefacts.

---

# Symptom B — what it tells us, and what to do

**No further diagnosis needed. B is the confirmation, not a new problem.**

It establishes that root→expiry substitution happens at the **instrument-lookup
layer**, shared by the Analyzer picker, the chart, and the instrument dialog.

**Consequence: it cannot be worked around from inside any dialog.** There is no
checkbox for "don't resolve." The fix has to change what the instrument *is*, or
change where the data *lives*.

That is the fix list from the prior document, unchanged and now better supported:

- **FIX A** — re-import as **`NQCONT 12-25.Last.txt`** (space before the month),
  single contract month, offset `0`, roll date after 2026-07-20,
  `Merge Policy = DoNotMerge`. Then chart **the dated symbol**, not the root.
  *Works with the resolution instead of against it.*
- **FIX B** — rebuild as a **non-expiring instrument type**, so there is no
  resolution at all and the existing `db\minute\NQCONT\` folder is found.
  **Requires the point-value check first** — confirm a 1.00-point move on 1
  contract shows as **$20.00**, not $1.00. If point value is not honoured, abandon
  B; a silently 20×-wrong P&L is worse than a blank chart.
- **FIX C** — reusing the real `NQ 12-25` symbol. **Still not an option.** It is
  what created the mislabelled 95 MB file already on the machine.

**Note on Fix A and Symptom B together:** if the Analyzer insists on resolving to
`09-2025` even after you define `12-25` as the only contract month, that is new
information and it means the offset or roll-date semantics (Q4, still
**UNVERIFIED**) are driving the selection. **Tell me the exact offset value you
entered** — that question is still open and still free to answer.

---

## Report back

1. **`Loaded` section — the exact instrument name.** ← gates everything
2. **Chart title bar text** — bare or dated?
3. **Chart interval** — Minute/1, or Daily?
4. Connection indicator — connected?
5. `CME US Index Futures RTH` printed hours and their time zone
6. The offset value you entered in the contract-month editor

Items 1 and 2 will probably close this on their own.
