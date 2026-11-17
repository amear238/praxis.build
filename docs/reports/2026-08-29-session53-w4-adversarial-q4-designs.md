# Session 53 — W4 ADVERSARIAL: three artifacts attacked

**Task:** attack (1) the "error string names the bare root" falsification, (2) the
RTH-duration arithmetic falsifier, (3) the A1 positive-control design.
**Mode:** ADVERSARIAL. No artifact was improved. No file outside this one was touched.
**Criterion:** S1 (pasted output for every claim), S2 (every NT8 runtime statement graded),
S8 (no question of Amear's answered here), F2 (no session template proposed, selected or
endorsed anywhere below).

**Grading key.** VERIFIED = a named human observed it on the running install on a named
date. INFERRED = derived; the settling observation is named. Nobody in this session has
run NinjaTrader.

---

## VERDICT SUMMARY

| Artifact | Verdict |
|---|---|
| 1 — error string names the bare root ⇒ evidence against the rewrite framing | **UNSUPPORTED** |
| 2 — 450 ≠ 390 ⇒ display-conversion already falsified | **OVERSTATED** |
| 3 — A1 control is confounded without confirmed local data | defect is **REAL**; remedy is **PARTIAL** |

---

## ARTIFACT 1 — UNSUPPORTED

The claim has two legs. Both fail.

### Leg 1: "the recorded error string names the BARE ROOT." There is no session-52 error string on the record at all.

Every verbatim instance of the error in existence, repo and signals dir:

```
$ grep -rni "unknown instrument" docs/ 2>/dev/null | head -50
docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md:76:`Error on requesting bars series: 'Unknown instrument 'NQCONT''`
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:124:190:Error on requesting bars series: 'Unknown instrument 'NQCONT''
docs/reports/2026-08-29-session53-w1-q1-import-instructions.md:437:| M3 | NT8 created the empty `db\minute\NQCONT\` ... (v3 l.183–194) | **INFERRED** ...
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:8:CHECK A - THE ANALYZER "unknown instrument NQCONT"
docs/reports/2026-08-29-session53-vm-checks-A-and-B.md:43:asking for NQCONT 09-2025. Those are different strings, so "unknown instrument"
docs/reports/2026-08-29-session53-w2-q2-nqcont-definition.md:52,279-284,297,319,331,374,463,526  (all re-quotes of the same two sources)
```

```
$ grep -rni "unknown instrument" /Users/admin/praxis-signals/ 2>/dev/null | cut -c1-160
/Users/admin/praxis-signals/b2-data/4uu-VM-brief-v3.md:190:Error on requesting bars series: 'Unknown instrument 'NQCONT''
/Users/admin/praxis-signals/b2-data/outbound/4uu-VM-brief-v3.md:190:Error on requesting bars series: 'Unknown instrument 'NQCONT''
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md:66:  13:45:45  Error on requesting bars series: 'Unknown instrument 'NQCONT''
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md:67:  13:53:48  Error on requesting bars series: 'Unknown instrument 'NQCONT''
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md:68:  14:02:16  Error on requesting bars series: 'Unknown instrument 'NQCONT''
/Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md:69:  14:27:58  Error on requesting bars series: 'Unknown instrument 'NQCONT''
```

Root source, with its own attribution:

```
$ sed -n '50,72p' /Users/admin/praxis-signals/b2-data/inbound/4uu-VM-status-2026-07-25.md
## 4. THE ACTUAL BLOCKER — STEP 0b was never completed
`NQCONT` **does not exist as an instrument in NT8.** Evidence:
- `db\minute\NQCONT\` exists (created 7/24 13:50) but is **completely empty — zero files.** ...
- Three explicit log errors, across three separate NT8 sessions on 7/24:
  13:45:45  Error on requesting bars series: 'Unknown instrument 'NQCONT''
  13:53:48  ...
  14:02:16  ...
  14:27:58  ...
- I scanned every non-data file under `Documents\NinjaTrader 8\` ... It appears **only in
  `log\` and `trace\` files** — never in the instrument database.
```

So: **four log lines, all timestamped 2026-07-24, all read out of `log\` by Amear on
2026-07-25** (VERIFIED — Amear, 2026-07-25; the timestamps and the scan are his transcription).
Everything else in the corpus is a re-quote of those four lines. The session-52 chain is:

- **VERIFIED — Amear, session 52 (2026-08-29):** the Analyzer instrument *picker* resolves
  bare `NQCONT` to `NQCONT 09-2025`. That is how session 52 recorded symptom B, and it is a
  *picker resolution*, not an error string:
  ```
  $ sed -n '16,20p' docs/reports/2026-08-29-session52-blank-chart-diagnosis.md
  - **B** — Strategy Analyzer instrument picker auto-resolves bare `NQCONT` to
    **`NQCONT 09-2025`**.
  ```
- **UNVERIFIED:** the wording of any error thrown by the Analyzer in session 52. No file in
  either tree records it. The string in the brief's OBS2 is a paraphrase in a summary, with
  no capture behind it.

**The three defects that follow, in order of severity:**

1. **Date and state mismatch (attack (a) — legitimate, and fatal).** The four verbatim lines
   are from 2026-07-24, when — per the same 7/25 scan — `NQCONT` was **absent from
   `NinjaTrader.sqlite` entirely** and `db\minute\NQCONT\` was **empty**. In that state there
   was no instrument definition to resolve, therefore no contract-month table to rewrite
   through, therefore naming the root is the *only* string NT8 could have produced.
   **INFERRED** (settling observation: the 2026-07-25 sqlite scan, quoted above). By session 52
   the state is provably different — data is present (~1.86M records, OBS1) and *at least two*
   `NQCONT` definitions existed, since a `Stock`-typed duplicate was deleted (OBS2). Reasoning
   from a July error to an August failure crosses a state change that the corpus itself
   documents. **They are not the same error instance, and the artifact does not establish that
   they carry the same error text.**

2. **Priming contamination.** The document Amear was working from during session 52 displays
   that exact string:
   ```
   $ sed -n '74,77p' docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
   ...NinjaTrader made it from a filename, then failed because the instrument was unknown.
   The log says so four times:
   `Error on requesting bars series: 'Unknown instrument 'NQCONT''`
   ```
   A paraphrased report of "unknown instrument NQCONT" made while reading a page that prints
   `Unknown instrument 'NQCONT'` cannot be distinguished from a re-reading of that page. This
   is not a claim that Amear misreported. It is a claim that the artifact has no way to tell
   the difference, and it built a falsification on the difference.

3. **The inference step is not settleable by this corpus (attack (c)).** The claim needs the
   premise *"if NT8 rewrote the request, the error text would name the rewritten string."*
   That is a statement about where inside NT8 the exception message is constructed. An equally
   consistent alternative: the picker resolves to a month for *display*, and the lookup fails
   earlier, at the master-instrument level, on the root token — in which case a root-named
   error is exactly what the rewrite framing predicts too. **UNVERIFIED, and the corpus cannot
   settle it.** The only NT8-internals reference held here is
   `docs/reference/2026-07-24-nt8-windows-reference.md`, built from 20 screenshots of the UI;
   it documents windows and fields, not exception construction. **So the error wording does
   not discriminate between the two framings in either direction** — it is not evidence for
   the rewrite framing either.

**Verdict: UNSUPPORTED.** Not "the framing is right and the artifact is wrong" — the artifact
cites a July error to refute an August framing, the August error text does not exist on the
record, and even a verbatim August capture would not settle the question absent knowledge of
NT8 internals that nobody here has. The correct disposition of the artifact's subject is
*undetermined*. The fastest thing that would change that is a verbatim capture of the
session-52 Analyzer error out of `log\log.20260829.*` — Amear's to read, not mine to predict
(S8).

---

## ARTIFACT 2 — OVERSTATED

### The arithmetic is right. Recomputed independently:

```
$ python3 -c "..."
spec RTH ET  09:30-16:00 = 390 min
observed     08:30-16:00 = 450 min
09:30 ET -> CT = 08:30 ; 16:00 ET -> CT = 15:00
08:30 CT -> ET = 09:30 ; 16:00 CT -> ET = 17:00
delta minutes = 60
```

Spec side confirmed verbatim:

```
$ sed -n '76,82p;88,93p' docs/specs/2026-07-15-b2-data-acquisition-spec.md
| Session | Definition (ET) | Expected 1-min bars / full day | Check |
| **RTH** | 09:30–16:00 | **390** bars/day (391 boundary-inclusive) | Median RTH day == 390 ...
- [ ] RTH filter reproduces 09:30–16:00 ET exactly and yields the 390-bar median.
```

Offset check across both 2026 DST transitions — ET and CT are 1 h apart on every date tested,
so within US zones the endpoints map as the artifact says:

```
(2026, 3, 8) ET 09:30 -> CT 08:30 offsetdiff_h 1.0
(2026, 3, 8) ET 16:00 -> CT 15:00 offsetdiff_h 1.0
(2026, 11, 1) ET 09:30 -> CT 08:30 offsetdiff_h 1.0
(2026, 11, 1) ET 16:00 -> CT 15:00 offsetdiff_h 1.0
(2026, 6, 15) ET 09:30 -> CT 08:30 offsetdiff_h 1.0
(2026, 6, 15) ET 16:00 -> CT 15:00 offsetdiff_h 1.0
```

So the narrow proposition — *the printed template hours are not a zone rendering of the
spec's 09:30–16:00 ET* — survives attack, **conditional on OBS4 being a faithful reading of a
single session row** (VERIFIED — Amear, 2026-08-29, by hand, no screenshot).

### Three ways the claim over-reaches.

**(i) "Duration is preserved under zone conversion" is not universally true.** It holds here
only because US Eastern and US Central share transition rules and US transitions occur at
02:00 local on a Sunday, outside any 09:30–16:00 weekday window. Where the rules differ, wall
-clock spans are not preserved:

```
--- counterexample: session crossing a US spring-forward, zone with different rule ---
ET wall 01:00-04:00 real duration min = 180.0
same instants in London wall clock: 06:00 08:00
```

An ET wall-clock span printed as three hours renders as two hours of London wall clock. The
premise is safe *in this instance* and unsafe *as stated*. A caveat, not a break.

**(ii) It does not falsify the hypothesis Check B1 actually tests — so "before any toggle is
performed" is wrong.** B1 asks whether the *printed* hours are a display conversion of the
template's **own stored definition**. Nothing requires that stored definition to be the spec's
RTH. `08:30–16:00` Central is the exact zone rendering of a `09:30–17:00` Eastern stored
definition (from the arithmetic above: `16:00 CT -> ET = 17:00`). So a display-conversion
explanation remains fully alive; only the *identity with the spec's session* is dead. The
artifact refutes a proposition B1 was not testing, then declares B1's toggle unnecessary. The
toggle still discriminates, and it costs one read.

**(iii) The thing "falsified" was already on the record as an untested assumption**, so the
word carries less than it appears to:

```
$ grep -n "Nobody has ever confirmed\|assumed 09:30" docs/reports/2026-08-29-session52-nt8-voice-walkthrough-v2.md
113:**`CME US Index Futures RTH`** template. **Nobody has ever confirmed its actual
117:Read me the printed hours. It may print in **Central**, in which case 08:30–15:00
```

Line 113 states the mapping was assumed and never checked. The vendor template and the PRAXIS
spec RTH are two different objects with two different authors; there is **no established fact
that a NinjaTrader vendor default must encode a PRAXIS spec definition**, and a 450-minute
vendor session that simply is not the spec's RTH is a coherent, contradiction-free reading.
Discovering they differ closes a flagged gap. It does not overturn a load-bearing claim.

**Residual misread classes not excluded by the corpus** (raised, not asserted): a template may
carry several session rows, and which row was read is not recorded; the zone control at the
top of the window and the row values may not be the same object — precisely what B1 step 1 vs
step 2 separates. **UNVERIFIED** — the reference documents `Tools > Trading Hours` as a window,
never its row layout.

**Verdict: OVERSTATED.** Arithmetic SOUND; scope of the conclusion too wide; the "no toggle
needed" corollary is wrong. **Which session definition governs this system is not addressed
here and is not mine to address** (S8, F2 frozen). Nothing above proposes, selects or endorses
a template.

---

## ARTIFACT 3 — the defect is REAL; the proposed remedy is PARTIAL

A1 as written:

```
$ sed -n '18,30p' docs/reports/2026-08-29-session53-vm-checks-A-and-B.md
A1. POSITIVE CONTROL. Run this one first.

Open Strategy Analyzer. Select any built-in NT8 instrument that already has
data - the standard NQ front-month contract is fine. Set the SAME 1-minute
interval and the SAME date range you used for NQCONT. Run it.

  - If it ALSO errors on requesting bars: the fault is in the data-series
    layer, not in NQCONT specifically. That supports the "records built but no
    usable bars series" idea.
  - If it RUNS CLEAN: the fault is specific to NQCONT's own definition, and the
    bars-series idea is dead.
```

### The defect is REAL, and the corpus makes it concrete rather than hypothetical.

Note first what A1 does *not* get wrong: it does say *"that already has data."* The defect is
not an absent precondition. It is that (a) the precondition is unverifiable at the moment of
the click, and (b) the very next clause — *"the standard NQ front-month contract is fine"* —
asserts the precondition is satisfied for a specific instrument, with nothing behind the
assertion. In practice the concrete recommendation overrides the abstract condition.

What the corpus says about what data this install actually holds:

```
$ grep -rni "MNQ\|Kinetick\|Loaded" docs/reference/2026-07-24-nt8-windows-reference.md
25:- **Data feed:** Kinetick – End Of Day (Free) available; Simulated Data Feed connected during capture (green dot).
33:- **Connections menu** (20-connections-menu.png): Kinetick – End Of Day (Free) · Playback · Sim
65:- **Open:** `New > Chart` (confirmed live — capture opened on `MNQ SEP26`, Daily).
```

- **VERIFIED — Amear, 2026-07-24 (20-screenshot capture):** the only market-data connections
  present are Kinetick End Of Day (Free), Playback, and Sim; the Simulated Data Feed was the
  one connected.
- **VERIFIED — same capture:** the one chart opened, on `MNQ SEP26`, was on the **Daily**
  interval — not 1-minute.
- **INFERRED** (settling observation: the connection list at reference l.25/33, plus the
  absence of any import other than `NQCONT.Last.txt` anywhere in the corpus): a built-in NQ
  front-month on this install is unlikely to hold local **1-minute** history. A feed named
  *End Of Day* is an end-of-day feed. **UNVERIFIED** whether Kinetick's free EOD tier serves
  any intraday history at all — a vendor-plan fact, and nobody here has connected it.

Now apply A1's own decision rule. A control with no local minute data fails **for a reason
that has nothing to do with the data-series layer**, and A1 reads that failure as *"supports
the 'records built but no usable bars series' idea."* The confound does not merely add noise —
**it pushes the reading in one specific wrong direction, toward confirming the hypothesis
under test.** That is the worst orientation a control can have. Defect: **REAL.** It is not
manufactured; it is the difference between a positive control and a coin flip.

### The remedy — read `Loaded` first, pick an instrument confirmed present with the needed range — helps, and does not close it.

Three residual holes, each with a citation:

**1. It is UNVERIFIED that `Loaded` prints what the remedy needs it to print.** The reference
documents the section's existence, never its columns:

```
$ sed -n '69,73p' docs/reference/2026-07-24-nt8-windows-reference.md
### 1e. Historical Data window
- **What it's for:** access/manage all historical + Market Replay data; Import, Export, Download, and inspect Loaded data.
- **Open:** `Tools > Historical Data`.
- **LIVE — CORRECTION to the Help Guide:** ... vertical accordion ... **Loaded · Download · Import · Export · Get Market Replay data**
```

and session 52 flagged the same gap independently:

```
$ sed -n '106,109p' docs/reports/2026-08-29-session52-nqcont-continuous-instrument-investigation.md
**UNVERIFIED:** whether `Loaded` can *chart* a series, or only list and manage it.
The reference explicitly records the `Export` and `Get Market Replay` sections as
never expanded during capture; `Loaded` was captured but its capabilities were not
enumerated.
```

A row count alone does not establish **interval** (1-minute vs daily), **data type** (`Last`
vs `Bid`/`Ask`), or **date coverage**. The remedy silently assumes `Loaded` surfaces all
three. If it surfaces only Name and record count, the remedy confirms nothing beyond
"something is filed under this name" — the same class of fact that produced the NQCONT
situation in the first place.

**2. The remedy can return no eligible control at all, and A1 has no fallback.** If the only
1-minute import ever performed on this install is `NQCONT.Last.txt`, `Loaded` may contain
exactly one usable row, and it is the instrument under test. In that branch A1 is **unrunnable,
not repaired** — and A1 is currently written as *"Run this one first,"* an unconditional
instruction with no "if no control exists, report that and stop" exit. A brief that cannot
fail gracefully invites an answer to be invented for it.

**3. "The SAME date range you used for NQCONT" is not recoverable from the corpus.** No file
records the Analyzer date range used in session 52. Adjacent context shows the pressure:

```
$ grep -rn "1,857,362" docs/reports/2026-08-29-session53-w1-q1-import-instructions.md | cut -c1-120
96:81:1,857,362 bars · 2021-03-07 → 2026-07-20 · ET wall-clock · full ETH session (RT
```

The imported data ends **2026-07-20**, while the blank chart's window was
**2026-01-01 → 2026-08-29** (session-52 blank-chart report, l.16-17). So "the same range" and
"a range the control demonstrably covers" can be mutually exclusive, and A1 gives no rule for
which constraint to break. Holding the range constant is what makes it a control; changing it
is what makes it runnable.

**Net:** the remedy removes the largest and most misleading part of the confound — an
instrument with zero local data producing a false confirm. It does not remove the interval /
data-type / coverage part, it has no branch for "no control exists," and it collides with the
"same date range" clause. **PARTIAL.** The single observation that would collapse holes 1 and
2 together: an enumeration of `Loaded`'s actual column headers and its full row list — one
screenshot, and it is already the outstanding gate session 52 asked for twice and never got
(`...blank-chart-diagnosis.md:52`, `:175`). That observation is Amear's to make; I am not
choosing which instrument he should pick (S8).

---

## Scope discipline

- No trading-hours session template is proposed, selected, corrected, endorsed or reasoned
  toward anywhere above. F2 remains frozen and untouched.
- No question belonging to Amear is answered here. Observations that would settle the open
  points are named; none is predicted.
- Second-order findings noticed and **reported, not fixed**: (i) the `~1,857,362` figure in
  OBS1 is identical to the Mac-side stitch row count at
  `docs/reports/2026-07-22-1u6-tz-et-conversion.md:58` — consistent, but the corpus cannot
  distinguish a fresh reading from recognition of a familiar number; (ii)
  `vm-checks-A-and-B.md` l.42-46 states the rewrite framing as settled fact (*"Something
  rewrites the request from the root name into a contract month"*) while its own FALSIFIER at
  l.48-50 treats it as open.

## Files staged

**None.** This report is written and left unstaged. Nothing was added to the index and no
history was written. No edit to any other file, nothing under `.claude/agent-memory/`.

## Result

**Artifact 1: UNSUPPORTED · Artifact 2: OVERSTATED · Artifact 3: defect REAL, remedy PARTIAL.**
