# Session 53 — W2 / Q2 — `NQCONT` instrument definition: what the corpus records, and a break attempt on the request-rewrite framing

**Task.** Answer Q2a–Q2d from the corpus alone. Find evidence FOR and AGAINST the
master's working framing. Actively hunt the disconfirming read.

**Mode.** ADVERSARIAL. Read-only. No file edited, created or deleted except this
report. Nothing staged, nothing committed. No template selected, no instrument
definition or spec touched.

**Criterion.** `specs/SPEC_RUBRIC.md` S1 (pasted output, not description), S2
(no component reported above its evidence), S8 (Amear's questions stay his).

**Grading convention used here, as the brief requires.** A claim about *what a
document says* is a **document fact** and is settled by the pasted grep. A claim
about *what NT8 does* is a **mechanism claim** and carries `VERIFIED` (named human,
dated) or `INFERRED` (with the single observation that would settle it). Nobody in
this session has run NinjaTrader. The three standing observations — OBS1, OBS2,
OBS3 — are **Amear's, by hand, on the Windows VM, 2026-08-29 and session 52**.

---

## Headline

**The framing does not survive intact.** Two independent breaks, both from
corpus text, neither requiring any new NT8 assumption:

1. **BREAK 1 — the framing's second premise is a display read, not a request
   read.** "Request name is `NQCONT 09-2025`" comes from the Strategy Analyzer's
   *instrument picker*. The only place the corpus records an actual bars-request
   string is a **Control Center Log line**, and **every verbatim instance of that
   line anywhere in the repo names the BARE root** — not a dated month — and all
   of them trace to a moment when `NQCONT` provably had **no instrument
   definition at all**. Session 52's error text is nowhere recorded verbatim.
2. **BREAK 2 — the corpus already records a contract month that does not match
   the resolved one.** **December 2025 was entered; September 2025 came out.**
   If the contract-month table drove the resolution, the resolved month would be
   December. So the four fields the master nominated as "where that would live"
   are, on the corpus's own record, *insufficient* to explain the rewrite.

**Q2c is answered honestly and it is a null: the corpus CANNOT discriminate**
between "data keyed to a name nothing asks for" and "data written to a store no
live instrument definition points at." The reason is specific and citable, not a
shrug — see Q2c.

---

## Process log

1. Read the session-52 investigation report in full.
2. Read the session-52 blank-chart diagnosis in full.
3. Read reference §1e, §1f, §2, §6 and the residual-gaps list.
4. Grepped the corpus repo-wide for `NQCONT`, `Unknown instrument`, `09-2025`,
   `sqlite`, and for merge / roll / expiry co-occurrence.
5. Read `DECISION_LOG.md` rows `2026-08-29T12:05:00Z`, `12:10:00Z`, `18:00:00Z`
   and `HANDOFF.md` §"Part 6 is blocked".
6. Read `docs/specs/2026-07-15-b2-data-acquisition-spec.md` §2.1 and §5 (the only
   corpus text that names an NT8 roll-configuration UI).
7. Ran null-proving greps for each of the four Q2a fields.
8. Re-ran every command pasted below and corrected four line-number/line-range
   errors in my own draft before finalising. One grep surfaced an untracked peer
   report from this same session (`…-session53-w1-q1-import-instructions.md`)
   that I had not been given; I read the relevant sections and cite it at
   BREAK 1.

---

# Q2a — the four fields of the `NQCONT` definition

## Field 1 — INSTRUMENT TYPE: `Future`. **RECORDED, and independently observed.**

Prescribed value, `docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md`:

```
$ grep -n "^| Name\|^| Type\|^| Tick\|^| Point\|^| Currency\|^| Trading\|^| Exchange" docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
91:| Name | `NQCONT` — exactly, all caps, no spaces |
92:| Type | `Future` |
93:| Tick size | `0.25` |
94:| Point value | `20` |
95:| Currency | `USD` |
96:| Trading hours | `CME US Index Futures RTH` |
97:| Exchange | `CME` or `Globex` if it asks |
```

That is an *instruction*, not an observation. The **observation** is separate and
stronger:

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'a \*\*duplicate `NQCONT` instrument existed[^.]*\.'
a **duplicate `NQCONT` instrument existed — one typed `Future`, one typed `Stock`.
```

**Grade: VERIFIED (Amear, VM, session 52, 2026-08-29)** that a `Future`-typed
`NQCONT` was visible in the Instruments manager. Tick size, point value, currency,
exchange and trading-hours template are **prescribed only — never read back**.

## Field 2 — EXPIRY / CONTRACT MONTHS: **PARTIALLY RECORDED. `December 2025` was entered. The saved state was never read back.**

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'no offset value was ever entered at all[^|]*mechanism\.'
no offset value was ever entered at all**, so the offset was never the mechanism.
```

```
$ sed -n '133,134p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
**What I can say, as INFERRED and weak:** December 2025 → September 2025 is a
**three-month backward shift**, which is one quarterly step on the March / June /
```

```
$ grep -n "refusal to save\|zero contract months" docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
92:That is consistent with every symptom you reported, including the refusal to save
93:with zero contract months — a Future without an expiry table has nothing to
```

**What is recorded:** a contract month of **December 2025** was entered; the
**offset field was left unpopulated**; and NT8 **refused to save with zero
contract months**, so at least one row exists.

**What is NOT recorded:** any verbatim read-back of the contract-month grid as it
now stands. The corpus's own note on the initial state is explicitly ungraded:

```
$ sed -n '145,147p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
The initial `NQCONT December 29` is also **UNVERIFIED** — plausibly a far-future
default (2029) auto-generated when no months were defined, but I have not confirmed
NT8 does that.
```

**Grade on "a `12-25` row is present in the definition right now": INFERRED.**
The observation that settles it is exactly Check A2 item 4, still unrun.

## Field 3 — MERGE POLICY: **NOT RECORDED IN CORPUS.**

Every mention across the four `NQCONT` documents is an option list, a
recommendation, or a request to go look — never a read value:

```
$ grep -ni "merge" docs/reports/2026-08-29-session52-*.md docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:126:## A6. Merge Policy
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:129:**Merge policy**. Options: `MergeBackAdjusted` · `MergeNonBackAdjusted` ·
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:130:`DoNotMerge` · `UseGlobalSetting`.
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:132:**INFERRED:** with a merge policy active and contract months that have no data, NT8
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:135:Set **`DoNotMerge`** — VERIFIED as *"single expiry only."* You have one nominal
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:155:  `Merge Policy = DoNotMerge`. Then chart **the dated symbol**, not the root.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:131:all — §6 documents Merge Policy and naming, not the contract-month editor.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:198:3. **Set Merge Policy = `DoNotMerge`.** VERIFIED as an option in reference §6:
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:199:   *"DoNotMerge (single expiry only)."* You have exactly one expiry and no real
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:253:   data stored under its bare name? Cite `instruments.htm`, `merge_policy.htm`.
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:281:contract-month editor** — the reference documents Merge Policy and naming
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:39:  3. Merge Policy
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:48:FALSIFIER: if the definition shows no expiry, no contract months and no merge
```

**NOT RECORDED IN CORPUS.** Not even the default is known for this instrument —
`UseGlobalSetting` is one of four options and the global setting was never read
either. **I am not filling this with a plausible default.**

## Field 4 — ROLL SETTINGS: **NOT RECORDED IN CORPUS for `NQCONT`.**

```
$ grep -ni "roll\b\|rollover\|roll-over\|roll date" docs/reports/2026-08-29-session52-*.md docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:137:a roll-date rule selecting the prior quarterly. **I cannot distinguish these and
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:142:supported. If it was `0` or blank, the offset is not the mechanism and the roll
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:163:only metadata for rollover and display — which is what I'd expect from a system
docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md:196:   **December 2025**, **offset `0`**, roll date **after 2026-07-20** (your data's
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:17:  **2026-01-01 → 2026-08-29**, no bars at any zoom or scroll position.
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:136:expiry and no real rollover; merging can only add artefacts.
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:154:  single contract month, offset `0`, roll date after 2026-07-20,
docs/reports/2026-08-29-session52-blank-chart-diagnosis.md:167:information and it means the offset or roll-date semantics (Q4, still
```

Every hit is prescriptive ("set roll date after 2026-07-20") or hypothetical.
**No roll setting for `NQCONT` was ever read.**

**⚠️ A trap worth naming, because it is easy to mis-cite.** The corpus *does*
contain a roll configuration — and it is for a **different instrument**:

```
$ sed -n '44p' docs/specs/2026-07-15-b2-data-acquisition-spec.md
| **Roll trigger** | **Volume/OI crossover** — roll to the next contract on the day the incoming month's volume (confirmed by open interest) overtakes the front month. | NT8 Instrument → *Roll-over* tab: roll by **Volume** (with OI confirmation), NOT a fixed calendar/expiry offset. |
```

```
$ sed -n '114p' docs/specs/2026-07-15-b2-data-acquisition-spec.md
1. **Set the continuous-contract roll (§2) BEFORE downloading.** NT8 → *Tools → Instruments* → search `NQ` → open the futures instrument → *Roll-over* tab: set roll trigger = **Volume** (OI-confirmed), adjustment = **Difference**. Save. (If the trader has NOT yet locked §2, stop and get the lock — the roll setting determines what gets downloaded.)
```

That is `NQ`, not `NQCONT`, and it is a *spec prescription from 2026-07-15*, not
an observation. Note also that the layout reference — built from 20 screenshots of
this actual install — **never captured a Roll-over tab**; §6 documents only naming
and Merge Policy. **Grade on "an NT8 instrument editor in 8.1.7.2 has a Roll-over
tab": INFERRED.** The observation that settles it: open `Tools > Instruments` →
`Edit` on any future and read the tab strip.

### Q2a summary table

| Field | Corpus value | Source | Grade |
|---|---|---|---|
| Instrument type | `Future` | `DECISION_LOG.md:359`; walkthrough-v2:92 | VERIFIED (Amear, session 52) that a `Future`-typed `NQCONT` exists |
| Expiry / contract months | `December 2025` entered; offset **blank**; NT8 refused to save with zero rows | `DECISION_LOG.md:359`; investigation:92-93, 133-134 | Entry VERIFIED (Amear, session 52); **current saved state INFERRED — never read back** |
| Merge policy | **NOT RECORDED IN CORPUS** | null-grep above | — |
| Roll settings | **NOT RECORDED IN CORPUS** (for `NQCONT`) | null-grep above | — |

---

# Q2b — does the corpus document merge policy / expiry as the driver of root→month resolution?

**No. The corpus documents merge policy as a STITCHING rule, not a RESOLUTION
rule — and it documents nothing at all about root→month rewriting.**

Reference §6, the only authority on merge policy in this repo:

```
$ sed -n '188,190p' docs/reference/2026-07-24-nt8-windows-reference.md
**Merge Policy** (how contract months stitch at rollover — matters for backtests spanning a roll):
- **Global:** `Tools > Options > Market Data > Merge policy`. **Per-instrument:** `Tools > Instruments` → select → **Edit** → **Merge policy**.
- Options: **MergeBackAdjusted** (back-adjust to next front month, seamless) · **MergeNonBackAdjusted** (raw, visible roll gaps) · **DoNotMerge** (single expiry only) · **UseGlobalSetting** (per-instrument, inherit global).
```

"How contract months stitch at rollover" is a claim about **combining series that
already resolved**. It is not a claim about **which symbol a root request becomes**.
The nearest adjacent corpus statement is §2's cross-check note, which says merge
policy affects *display*, not *naming*:

```
$ grep -n "Merge Policy affects what.s shown" docs/reference/2026-07-24-nt8-windows-reference.md
117:- Cross-check by charting the instrument for the imported range (Merge Policy affects what's shown — §6).
```

The corpus's own author states plainly that the resolution mechanism is
undocumented here:

```
$ sed -n '129,131p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
I do not know NT8's contract-offset semantics with enough confidence to state
them, and the reference does not cover the Add-Instrument dialog's expiry fields at
all — §6 documents Merge Policy and naming, not the contract-month editor.
```

**One corpus sentence does assert a mechanism, and it is ungraded — flagging it
rather than relying on it:**

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'Root cause is NT8[^|]*configuration\*\*'
Root cause is NT8's data-series **auto-rollover defaulting to December 2025 with no explicit configuration**
```

That sentence sits in a `WHY:` field with no grade attached, and it is **in
tension with the very observation the same row reports** — the resolved month was
**September 2025**, not December 2025. I do not treat it as evidence. Noting it
as a latent S2 exposure in the ledger; **not fixing it, not my scope.**

**Answer to Q2b: the corpus documents NO mechanism by which merge policy or the
expiry configuration drives root-to-contract-month resolution.**

---

# Q2c — THE BREAK ATTEMPT

## The framing, restated so the premises are separable

> P1. Storage name is `NQCONT` (OBS1).
> P2. Request name is `NQCONT 09-2025` (OBS2).
> C.  ∴ the defect is not in how data was WRITTEN, but in something REWRITING
>     THE REQUEST from root to contract month.

Verbatim, from the ledger:

```
$ sed -n '363p' DECISION_LOG.md | grep -o 'The defect is therefore NOT[^|]*contract month\.\*\*'
The defect is therefore NOT in how the data was written; **it is that something rewrites the request from the root into a contract month.**
```

## BREAK 1 — P2 is a picker DISPLAY, and the one verbatim error string in the corpus names the BARE root

The only error text quoted verbatim anywhere in this repo:

```
$ grep -rni "unknown instrument" --exclude-dir=.git --exclude="2026-08-29-session53-w2-q2-nqcont-definition.md" . | cut -c1-155
DECISION_LOG.md:363:- [2026-08-29T18:00:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK 1 CLOSED AFTER FOUR ASKS. 
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:76:`Error on requesting bars series: 'Unknown instrument 'NQCONT''`
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:8:CHECK A - THE ANALYZER "unknown instrument NQCONT"
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:43:asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:124:190:Error on requesting bars series: 'Unknown instrument 'NQCONT''
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:437:| M3 | NT8 created the empty `db\minute\NQCONT\` from the import filename and then faile
```

*(This report is excluded from its own grep. Lines are cut at 155 chars —
`DECISION_LOG.md:363` is a single very long ledger row and contains prose about
the error, not a quoted error string; the full row is pasted separately below.)*

**Five hits. Exactly two are a verbatim error string, both are the same string,
and both trace to the same 2026-07-24 NT8 log** — walkthrough-v2 l.76, and the
peer W1 report quoting `4uu-VM-brief-v3.md` l.190. The remaining hits are the
master's own paraphrase. Two things follow, and both hurt the framing.

**(a) The error names the ROOT, not the month.** `'Unknown instrument 'NQCONT''`.
If the bars layer had rewritten the request to `NQCONT 09-2025`, the natural
lookup failure would name the *rewritten* string. It names the root. So the
strongest available reading of the error is *"the root itself did not resolve"* —
which is the opposite of *"the root was silently replaced by something that then
failed."* The master's own brief reproduces this same bare-root phrasing for
session 52 (`vm-checks-A-and-B.md:8`), so the paraphrase chain has carried the
bare name throughout.

**(b) That verbatim line was captured when `NQCONT` DID NOT EXIST as an
instrument.** Context, same file:

```
$ sed -n '68,77p' docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
**This is the actual blocker.** Every previous attempt died here. `NQCONT` does
not exist in your instrument database — confirmed 2026-07-25 by scanning the
4.4 MB `NinjaTrader.sqlite` where instruments actually live. It appears only in
log files, never in the database.

There *is* an empty folder named `NQCONT` under the minute-data directory.
**That's a decoy** — NinjaTrader made it from a filename, then failed because the
instrument was unknown. The log says so four times:
`Error on requesting bars series: 'Unknown instrument 'NQCONT''`
```

So the corpus records this exact error string as **the documented signature of
"no instrument definition resolves this name"** — four occurrences, 2026-07-25,
with no rewrite involved and no contract month in sight.

**Independent corroboration from the peer W1 unit this session** (read after my
own grep surfaced it; not coordinated):

```
$ sed -n '437p' docs/reports/2026-08-29-session53-w1-q1-import-instructions.md
| M3 | NT8 created the empty `db\minute\NQCONT\` from the import filename and then failed on unknown instrument (v3 l.183–194) | **INFERRED** — strongest partial support in the corpus: v3 l.190 quotes `Error on requesting bars series: 'Unknown instrument 'NQCONT'''`, attributed to 7/24 logs and a 7/25 scan. I have not read those logs; they are on the Windows machine. | Reading `log\log.20260724.*` on the NT8 VM directly. |
```

W1 reached the same grade independently — `INFERRED`, settled only by reading
`log\log.20260724.*` on the VM. **Two seats, same conclusion, neither has seen
the log.**

**Consequence for the framing: P2 is not established.** Nothing in the corpus
records session 52's error string verbatim. The picker's *display* of
`NQCONT 09-2025` is a UI rendering; the corpus has already burned this project
once on treating a display field as a report of the resolved symbol —

```
$ sed -n '35,38p' docs/reports/2026-08-29-session52-blank-chart-diagnosis.md
1. **VERIFIED (reference §6):** *"NT8 can also display months as a month
   abbreviation — the chart during capture read `MNQ SEP26`."* So the resolved
   expiry surfaces **in the chart title**, in a different format than you typed.
   You have been reading the input field, not the output.
```

— and that argument was then refuted by OBS3 (title bar reads plain `NQCONT`).
Using a *different* display field to establish the request string is the same
error class run in mirror image.

**Grade: the claim "the Strategy Analyzer's bars request was for the string
`NQCONT 09-2025`" is INFERRED, not VERIFIED.** The single observation that
settles it: **`Control Center > Log` tab, read the `Error on requesting bars
series` line verbatim, including the quoted symbol.** Reference §2 confirms that
is where these errors land:

```
$ grep -n "Errors appear in the Control Center" docs/reference/2026-07-24-nt8-windows-reference.md
115:- **Errors appear in the Control Center `Log` tab** (formatting/naming problems show here).
```

## BREAK 2 — the recorded contract month does not match the resolved month

**December 2025 was entered. September 2025 came out.** (Evidence pasted at Q2a
Field 2.) The master's brief asserts the four fields are where the rewrite lives:

```
$ sed -n '42,46p' docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
WHY THIS FOUR: your data is filed under the bare name NQCONT. The Analyzer is
asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
is the correct answer to the wrong question. Something rewrites the request from
the root name into a contract month. These four fields are where that would
live.
```

But the corpus already contains an instance in which the contract-month field was
populated with `December 2025` and the resolution came out `September 2025`. **A
lookup table cannot be the mechanism if its contents disagree with its output.**
So even if Check A2 returns four clean values, those values are on the corpus's
own record **insufficient** to explain the observed month. The check is still
worth running — but the master's stated falsifier ("if the definition shows no
expiry, no contract months and no merge policy, then nothing in the definition
explains the rewrite") is **too weak**: the December→September mismatch means the
definition may fail to explain the rewrite *even when populated*.

## The Q2c alternative, stated at full strength: "record count under a name" ≠ "queryable bars series for a live definition"

**Corpus evidence FOR the alternative — three items.**

**(i) The corpus explicitly documents a `db\minute\NQCONT\` folder existing with
NO instrument definition behind it.** Same pasted block as BREAK 1(b): *"There is
an empty folder named `NQCONT` … That's a decoy — NinjaTrader made it from a
filename."* This is the precise shape of the alternative — the data directory is
populated by the *filename* path, independently of whether any definition points
at it. **Grade: the claim "NT8 creates/uses a `db\minute\<name>\` folder derived
from a filename regardless of instrument definitions" is INFERRED** — the corpus
records the folder's existence-without-definition as fact, and attributes the
cause without having observed it. Observation that settles it: nothing further
needed for the *existence* half; it is already established by the 2026-07-25
sqlite scan plus the folder.

**(ii) `Loaded` is a DATA manager, not a DEFINITION manager, and the corpus never
enumerated what it lists.** Reference §1e and §1f are two different windows:

```
$ sed -n '69,79p' docs/reference/2026-07-24-nt8-windows-reference.md
### 1e. Historical Data window
- **What it's for:** access/manage all historical + Market Replay data; Import, Export, Download, and inspect Loaded data.
- **Open:** `Tools > Historical Data`.
- ⚠️ **LIVE — CORRECTION to the Help Guide:** in 8.1.7.2 this window is a **vertical accordion** with stacked expand/collapse sections **Loaded · Download · Import · Export · Get Market Replay data** — **not** the horizontal Import/Export/Edit/Download *tab* strip the public Guide implies. ([`15-historical-data-loaded.png`](assets/nt8-2026-07-24/15-historical-data-loaded.png))
- Cite: https://ninjatrader.com/support/helpguides/nt8/historical_data_manager.htm

### 1f. Instruments manager
- **What it's for:** add/remove/edit instruments in the local DB (single master instance shared across providers); per-instrument settings (e.g. Merge Policy). ([`18-instruments-manager.png`](assets/nt8-2026-07-24/18-instruments-manager.png))
- **Open:** `Tools > Instruments`. Grid columns: Name / Type / Description, with an "All" filter and a search box; add/edit/remove at the bottom.
- Cite: https://ninjatrader.com/support/helpguides/nt8/instruments.htm
```

`Loaded` manages *data*. Instrument *definitions* live in a separate window whose
grid columns the reference does enumerate (Name / Type / Description). **The
reference never enumerates `Loaded`'s columns**, and the session-52 author flagged
that gap himself:

```
$ sed -n '106,110p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
**UNVERIFIED:** whether `Loaded` can *chart* a series, or only list and manage it.
The reference explicitly records the `Export` and `Get Market Replay` sections as
never expanded during capture; `Loaded` was captured but its capabilities were not
enumerated.
```

**So OBS1 establishes "the data store is keyed to the bare string `NQCONT`". It
does NOT establish "a live instrument definition named `NQCONT` has a queryable
bars series."** Those are different windows and different objects, and the corpus
says so.

**(iii) OBS1 was taken while the name was AMBIGUOUS — and after a same-named
definition had been deleted.** Two same-named instruments existed (`Future` and
`Stock`); `Loaded` lists by **name**; therefore a single `NQCONT` row with
1,857,362 records **cannot say which definition the import bound to**. And the
deletion happened in session 52, while OBS1 was taken in session 53 — so the
store demonstrably **survived** the deletion of a same-named definition.

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'The `Stock` duplicate was confirmed empty[^.]*\.'
The `Stock` duplicate was confirmed empty against Historical Data and deleted.
```

Note the circularity this creates: "confirmed empty **against Historical Data**"
is a `Loaded`-style check, keyed by name — and both instruments shared the name.
**Grade: "the `Stock` duplicate held no data" is INFERRED, not VERIFIED**, because
the discriminating capability (per-definition attribution in `Loaded`) has never
been shown to exist. Observation that would settle it: whether `Loaded` displays
an instrument **Type** column alongside Name — a single screenshot answers it.

**Corpus evidence AGAINST the alternative — stated fairly, and it is real.**

The import **succeeded** — 1,857,362 records landed. Reference §2 records that an
import against an unknown instrument fails loudly:

```
$ sed -n '102p' docs/reference/2026-07-24-nt8-windows-reference.md
**⚠️ LIVE — the instrument gotcha, now confirmed by evidence:** the **Import** section has **no instrument field** (Format / Data Type / Time Zone / Import only — [`16-historical-data-import.png`](assets/nt8-2026-07-24/16-historical-data-import.png)); the **Download** section *does* have an Instrument field ([`17-historical-data-download.png`](assets/nt8-2026-07-24/17-historical-data-download.png)). So NT8 derives the import's target instrument **from the filename**, not from any dialog field. This is exactly what blocked the 4uu import (`NQ-continuous-1min.nt8import.txt` → "Instrument is not supported by repository").
```

So **some** definition named `NQCONT` existed and accepted the import. That is a
genuine point for the master: this is not the July "no definition at all" state.
**But it does not close the question**, because two definitions named `NQCONT`
existed at some point in session 52 and the corpus never records which one
predated the import:

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'UNVERIFIED AND NOT INVESTIGATED[^.]*\.'
UNVERIFIED AND NOT INVESTIGATED: how a `Stock`-typed `NQCONT` came to exist.
```

## Q2c verdict — **the corpus CANNOT discriminate, and here is exactly why**

To choose between the two readings you would need **one** of:

- a `Loaded` row attributed to an instrument **Type**, not just a Name — the
  reference never enumerated `Loaded`'s columns; or
- the **verbatim** session-52 error string with its quoted symbol — nowhere in
  the corpus; or
- the **order of creation** of the `Future` and `Stock` definitions relative to
  the import — explicitly recorded as uninvestigated.

**All three are absent. The corpus does not decide this. I am not guessing.**

What the corpus *does* decide, cleanly:

- ✅ The framing's **P1 is VERIFIED** (Amear, 2026-08-29).
- ❌ The framing's **P2 is INFERRED from a display field, not observed** — and the
  only verbatim error string in the repo points the other way.
- ❌ The framing's **conclusion is therefore not established**, and its proposed
  location for the mechanism (the four definition fields) is already contradicted
  once by the December→September mismatch.

**The reading the corpus supports best is weaker and less satisfying than either
candidate: `db\minute\NQCONT\` is a data store keyed to a bare string, and no
observation yet made establishes that any live instrument definition's bars-lookup
path reaches it.** Whether that is because a rewrite intercepts the request, or
because the store was written under a definition that no longer serves it, is
**open**.

**One convergent note, offered as INFERRED and not asserted:** the alternative
reading also accounts for OBS3 (blank chart, plain `NQCONT` title, 1-minute
interval, correct window) **without** requiring the chart to perform any rewrite —
which is the thing the master correctly refuses to assume, having been refuted on
exactly that once. The framing, by contrast, must leave OBS3 unexplained; the
ledger says so itself:

```
$ sed -n '363p' DECISION_LOG.md | grep -o 'EXPLICITLY NOT UNIFIED WITH THE BLANK CHART[^|]*same rewrite\.'
EXPLICITLY NOT UNIFIED WITH THE BLANK CHART:** the tempting move is to say one defect produces both symptoms, and the master already made that exact over-extension last session and was refuted — the chart title bar reads plain `NQCONT` with no suffix, which is inconsistent with the chart performing the same rewrite.
```

**I am not claiming the unification. I am reporting that one candidate can carry
both symptoms and the other cannot, and that this is a reason to test rather than
a reason to believe.** The observation that discriminates: **read the Control
Center `Log` tab verbatim after re-opening the blank chart.** If the log shows
`Unknown instrument 'NQCONT'` at chart-open time too, one defect covers both.

---

# Q2d — does OBS2 constrain the surviving theories?

**Yes, but narrowly — and less than the ledger's phrasing implies.**

```
$ sed -n '359p' DECISION_LOG.md | grep -o 'The auto-resolution to `NQCONT 09-2025` PERSISTED[^.]*\.'
The auto-resolution to `NQCONT 09-2025` PERSISTED afterward, unchanged.
```

**What OBS2 kills, cleanly:** any theory in which the *presence of the `Stock`
duplicate* **causes** the picker's root→month auto-resolution. Deleting it changed
nothing. That is a proper R3-shaped control — toggle the candidate, observe no
change, the candidate was never the mechanism. **VERIFIED (Amear, session 52).**

**What OBS2 does NOT kill, and this is the load-bearing distinction:**

1. **It tested RESOLUTION behaviour. It said nothing about DATA OWNERSHIP.**
   Deleting a definition cannot retroactively change which definition the import
   bound to. If the 1.86M bars were written under the `Stock` definition's
   bare-name store, deleting that definition would leave the store exactly where
   OBS1 later found it — **which is consistent with OBS1, not excluded by it.**
   The corpus's own decoy-folder precedent shows a `db\minute\NQCONT\` folder
   outliving the absence of any definition.
2. **It does not establish that the `Stock` copy was empty.** As shown at Q2c(iii),
   "confirmed empty against Historical Data" is a name-keyed check performed while
   two instruments shared the name. **INFERRED, not VERIFIED.**
3. **It says nothing about the chart.** The picker and the chart resolve
   independently — the master established that himself when correcting the
   session-52 over-extension.

**Net: OBS2 removes one causal story and leaves the write-path question wholly
untouched.** The ledger's framing —"a second independent defect, not the cause"—
is correct **as to the auto-resolution** and is **not evidence** that the write
path was clean.

---

## What would settle this, cheapest first (reported, NOT dispatched — these are Amear's to run or decline)

1. **`Control Center > Log`, verbatim, the `Error on requesting bars series` line
   including the quoted symbol.** Decides BREAK 1 outright. Reference §2:115
   confirms that is where the error lands.
2. **Does `Loaded` show an instrument `Type` column?** One screenshot. Decides
   whether OBS1 can ever attribute the records to a definition.
3. **Check A2 as already briefed** — still worth running, but its falsifier needs
   widening per BREAK 2.

**Not proposed, per the hard limit:** no session template, no instrument edit, no
spec change. **S8:** nothing above is a decision; the offset question, the F2
ruling and every fix selection remain Amear's.

---

## Second finding, reported not fixed (per scope rule)

`DECISION_LOG.md:359` carries an **ungraded mechanism claim** in its `WHY:` field
— *"Root cause is NT8's data-series auto-rollover defaulting to December 2025 with
no explicit configuration"* — which is (a) unattributed to any observation and
(b) in tension with the same row's own report that the resolved month was
**September 2025**. Rubric S2 exposure. **Not edited. Not my scope.**

---

## Files staged

**None.** This report is written to
`/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-29-session53-w2-q2-nqcont-definition.md`
and left **UNSTAGED and uncommitted**. No `git add`, no `git commit`, no other
file created, edited or deleted. Nothing written under `.claude/agent-memory/`.

## Result

**BREAK FOUND.** The framing's first premise holds; its second premise is
INFERRED from a picker display and is contradicted by the only verbatim error
string in the corpus, which names the bare root and is documented as the signature
of an *absent* definition. Its nominated mechanism location is separately
undercut by the recorded December→September mismatch. **On Q2c the corpus cannot
discriminate between the two readings, and the three artifacts that would
discriminate are all absent — that null is the honest answer.**
