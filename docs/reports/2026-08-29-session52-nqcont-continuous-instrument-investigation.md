# NQCONT continuous-instrument resolution — investigation response

**Answering the questionnaire of 2026-08-29. Read the limitation first; it governs
how much of this you should trust.**

Evidence grades used throughout, and they are not decorative:

- **VERIFIED** — confirmed against a document or a measurement in this session.
- **INFERRED** — reasoning from verified facts. Could be wrong. Named as such.
- **UNVERIFIED** — I do not know. Not guessed at.

---

## LIMITATION — Question 6 is not executable from this seat

**Question 6 asks me to find and cite official NinjaTrader docs and forum threads.
I have no web-capable tool.** My tools here are file read/write, shell, and
subagent dispatch. No fetch, no search, no browser.

This is not a surprise — it is on the record. `docs/reports/2026-08-07-f3-fill-
resolution-research-UNGRADED.md` opens by noting that the F3 research had to be
commissioned *through a browser* because *"the praxis agent types were found to
hold no web tools."* Same wall, same seat.

**A subagent will not help** — they inherit the same toolset.

**So Q6 needs a browser research pass**, exactly as F3's did. What that pass should
be asked is specified at the end of this document.

**I also cannot inspect the NT8 database.** `Documents\NinjaTrader 8\` lives on the
Windows VM; the Parallels share maps Mac→Windows, not the reverse. Checked this
session: `/Users/admin/Documents/NinjaTrader 8` does not exist. Every on-disk claim
below is from your report, not my observation.

**What I do have** is `docs/reference/2026-07-24-nt8-windows-reference.md` — built
from 20 screenshots of your actual install on 2026-07-24, with live-UI corrections
marked where they contradict the public Help Guide. That is real documentation of
this specific machine, and it carries more weight than the public guide.

---

## Q1 — Is "Future" correct for a flat continuous series?

**VERIFIED, from the reference §6:**

> **Continuous contract:** the `<ROOT> ##-##` designation (e.g. `NQ ##-##`), a
> rolling front-month series. **Requires provider support** (historically Kinetick
> / eSignal / IQFeed).

**This is the answer, and it is not the one you were hoping for.**

NT8's continuous mechanism is a **feed-side** construct. `NQ ##-##` is a rolling
series the *data provider* assembles and serves. It is **not a container you can
import synthetic stitched bars into.**

**INFERRED:** there is therefore no NT8 instrument type that means *"futures-like
instrument, correct tick and point value, no expiry, accepts imported flat bars."*
`Future` gives you the right contract economics and **necessarily** drags in
contract-month resolution. That coupling is the whole of your problem.

**So "Future" is not wrong — it is the only type with the right economics, and it
has a side effect you now have to work around.** Whether a non-expiring type can
be made to carry a $20 point value is Q-B below, and it is **UNVERIFIED**.

---

## Q2 — Is data keyed to the literal name, or is a dated symbol substituted?

**INFERRED, high confidence — it is the second, and your own evidence is what
establishes it.**

The chain:

1. **VERIFIED (reference §2):** the import filename convention is
   `<instrument>.<DataType>.txt`, and for a dated contract the instrument token
   carries the month **with a space** — the documented example is
   `ES 12-09.Bid.txt`, and for PRAXIS NQ the reference gives `NQ 12-25.Last.txt`.
2. **Your report:** the file was `NQCONT.Last.txt` — **no month token** — and the
   data landed in `db\minute\NQCONT\`, a folder with **no month suffix**.
3. **VERIFIED (reference §2):** minute data lands under
   `db\minute\<instrument>\`, so NT8 wrote it to the literal name it was given.
4. **Your report:** charting `NQCONT` resolves to `NQCONT September 25`.

**INFERRED conclusion:** the import keyed the bars to the bare string `NQCONT`.
The chart, resolving a **Future** through its contract-month table, asks for a
*dated* series — something like `NQCONT 09-25`. It looks in the expiry-suffixed
folder, finds nothing, and renders blank.

**The data is on disk, filed under a name nothing ever asks for.** Import writes by
literal filename; chart lookup reads by resolved expiry. The two never meet.

That is consistent with every symptom you reported, including the refusal to save
with zero contract months — a Future without an expiry table has nothing to
resolve *to*.

---

## Q3 — Can the data be loaded under the literal name?

**Partly VERIFIED, and this is your cheapest next move.**

**VERIFIED (reference §1e):** `Tools > Historical Data` is a vertical accordion
whose **`Loaded`** section exists to *"access/manage all historical data"* and
inspect what is loaded.

**UNVERIFIED:** whether `Loaded` can *chart* a series, or only list and manage it.
The reference explicitly records the `Export` and `Get Market Replay` sections as
never expanded during capture; `Loaded` was captured but its capabilities were not
enumerated.

### Do this before anything else — 30 seconds, and it discriminates

**`Tools > Historical Data` → expand `Loaded` → find the NQCONT records and read
me the exact instrument name they are filed under.**

- **Filed as bare `NQCONT`, ~1,857,362 records** → confirms Q2's diagnosis
  outright. Fix A or Fix B below applies, and you can stop guessing.
- **Filed as `NQCONT 09-25` or any dated form** → my diagnosis is **wrong**, the
  problem is elsewhere, and nothing below should be actioned until we re-think.

**One observation kills or confirms the whole analysis.** Make it first.

---

## Q4 — The offset field, and December → September

**UNVERIFIED. I am not going to guess at this one.**

I do not know NT8's contract-offset semantics with enough confidence to state
them, and the reference does not cover the Add-Instrument dialog's expiry fields at
all — §6 documents Merge Policy and naming, not the contract-month editor.

**What I can say, as INFERRED and weak:** December 2025 → September 2025 is a
**three-month backward shift**, which is one quarterly step on the March / June /
September / December cycle NQ trades on. That is *consistent with* an offset being
applied as "N contracts back from the nominal month." It is equally consistent with
a roll-date rule selecting the prior quarterly. **I cannot distinguish these and
will not pretend to.**

**What would settle it, and it is free:** tell me the **exact value you entered in
the offset field**. If it was `1`, the one-quarterly-step reading is strongly
supported. If it was `0` or blank, the offset is not the mechanism and the roll
date is.

The initial `NQCONT December 29` is also **UNVERIFIED** — plausibly a far-future
default (2029) auto-generated when no months were defined, but I have not confirmed
NT8 does that.

---

## Q5 — The standard single-entry configuration

**UNVERIFIED as to what is *standard*.** That is precisely a Q6 documentation
question and I cannot reach the docs.

**What I can tell you is which unknown is load-bearing**, because it decides
between the two fixes:

> **Does NT8 refuse to serve bars dated far outside a contract's notional life?**

Your data spans **2021-03-07 → 2026-07-20**. No single real quarterly contract
lives five years. If NT8 filters bars by expiry window, Fix A fails. If expiry is
only metadata for rollover and display — which is what I'd expect from a system
that stores bars in per-expiry folders and serves whatever is in them — Fix A works
regardless of dates.

**INFERRED, and stated as the weaker claim it is:** I expect expiry to be metadata,
not a filter, because §2's verification step is *"confirm files/bar counts exist
for the imported instrument"* — a folder-contents check with no mention of date
validation. **But this project has been wrong twice on well-cited static reads, and
this has exactly that shape. Test it; do not trust it.**

---

## Q6 — Official docs and forum threads

**Cannot execute. No web tools.** See the limitation at the top.

---

# DELIVERABLE — replacement procedure

**Gate: run the `Loaded` check from Q3 first.** Everything below assumes it shows
bare `NQCONT`.

## FIX A — give the filename a contract month, re-import *(try this first)*

**Rationale:** works *with* NT8's resolution instead of against it. Changes only a
filename. Costs one re-import.

1. On the Mac side, copy — **do not rename or move** the original:
   `NQ-continuous-1min.nt8import.txt` → `NQCONT 12-25.Last.txt`
   **Space before `12-25`.** That spacing is VERIFIED from the reference's
   documented examples (`ES 12-09.Bid.txt`, `NQ 12-25.Last.txt`).
2. `Tools > Instruments` → edit `NQCONT` → contract months: **one entry only**,
   **December 2025**, **offset `0`**, roll date **after 2026-07-20** (your data's
   last bar).
3. **Set Merge Policy = `DoNotMerge`.** VERIFIED as an option in reference §6:
   *"DoNotMerge (single expiry only)."* You have exactly one expiry and no real
   rollover — merging can only introduce artefacts.
4. `Tools > Historical Data > Import`: Format `NinjaTrader (end of bar
   timestamps)`, Data Type `Last`, **Time Zone `US Eastern`**, select the new file.
5. Chart **`NQCONT 12-25`** explicitly — the dated symbol, not the bare root.

**Report:** whether bars from **2021** appear, or only bars near Dec-2025. That
single answer resolves Q5 for good, and it is worth recording either way.

**Known risk:** if NT8 date-filters by expiry, you get a short window instead of
five years. **That is a real result** — report it, don't work around it.

## FIX B — non-expiring instrument type *(if A fails, and it needs one check)*

**Rationale:** removes contract-month resolution entirely, so bare-name lookup
finds the folder you already have. **No re-import needed.**

1. `Tools > Instruments` → create a new instrument, e.g. `NQCONT2`, with a type
   that has **no expiry** — `Index`, `CFD` or `Stock`, whichever the dialog offers
   that accepts a tick size and a point value.
2. Tick size `0.25`, point value `20`, currency `USD`, trading hours
   `CME US Index Futures RTH`.
3. Import `NQCONT2.Last.txt` and chart the bare name.

**⚠️ The check that decides whether B is usable at all — do not skip it.**
**UNVERIFIED:** whether NT8 honours **point value** for P&L on a non-Future type.
If it treats the instrument as 1 unit = $1, every P&L number is wrong by a factor
of 20 and *nothing on the surface will say so.*

**Test:** run a backtest, take one trade with a known entry and exit, and confirm a
**1.00-point move on 1 contract shows as $20.00**. If it shows $1.00, **abandon Fix
B** — a silently wrong point value is worse than a blank chart.

## FIX C — reuse the real `NQ 12-25` symbol — **DO NOT**

This is the tempting one and it is the one that causes lasting damage. It writes
**stitched continuous prices into the genuine December-2025 contract's data
store**, contaminating real Kinetick data with synthetic bars.

**This exact hazard is already live on your machine** — it is Part 8, item one of
the walkthrough: the mislabelled 95 MB `NQ 12-25.txt` from the July run, which
exists precisely because someone took this path. Hard to notice, hard to undo.

**Not an option.**

---

# What the browser research pass should be asked

Hand this to a seat with web access. Do not let it answer from memory — this is a
niche configuration and confident wrong answers about it are cheap to produce.

1. **In NT8 8.1.x, does charting a `Future` instrument by root name always resolve
   through the contract-month table to a dated expiry?** Can a Future ever serve
   data stored under its bare name? Cite `instruments.htm`, `merge_policy.htm`.
2. **Does NT8 filter imported historical bars by the contract's expiry window**,
   or serve whatever is in `db\minute\<instrument>\` regardless of date? **This is
   the load-bearing unknown** — it decides Fix A.
3. **What exactly does the contract-month `offset` field do?** Real example: entered
   December 2025, NT8 resolved to September 25.
4. **Documented practice for a synthetic continuous instrument used only for
   backtesting imported stitched data.** Search NinjaTrader forums and futures.io.
   This is a common algo-trader workflow; there should be threads.
5. **Does NT8 honour tick size and point value for P&L on non-Future instrument
   types** (Index / CFD / Stock)? Decides Fix B.
6. **Is `<ROOT> ##-##` ever usable with imported data**, or is it strictly
   provider-served? Reference §6 says provider support is required — **confirm or
   refute that.**

Require pasted source text and a URL per answer. Anything unsourced comes back
marked UNVERIFIED, same as here.

---

## Correction to the walkthrough

Part 1 of `2026-08-29-session52-nt8-voice-walkthrough-v2.md` says to create
`NQCONT` as `Future` and treats that as sufficient. **It is not.** It omits
contract months entirely, and contract months are mandatory for a Future.

**That is a defect in my document, not a mistake you made.** The walkthrough was
built from the operator brief and the layout reference; **neither covers the
contract-month editor** — the reference documents Merge Policy and naming
conventions but never captured the Add-Instrument expiry fields.

Part 1 is superseded by this document pending the `Loaded` check and the research
pass. The walkthrough is not edited — correction by append, per standing practice.
