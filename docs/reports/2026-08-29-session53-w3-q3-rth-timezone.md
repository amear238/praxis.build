# Session 53 — W3/Q3: RTH session definition and its time-zone anchor (disk-only)

**Task:** Determine, FROM DISK ONLY, what the RTH session definition is and in which time zone it is anchored.
**Mode:** BUILD (read-only research). No file edited, created, or deleted except this report. Nothing staged, nothing committed.
**Criterion:** `specs/SPEC_RUBRIC.md` — S1 (pasted output, not description), S2 (no claim above its evidence level), S8 (no question belonging to Amear answered on his behalf).
**Date:** 2026-08-29
**Report path:** `/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-29-session53-w3-q3-rth-timezone.md`

---

## Scope and hard stops observed

This report does **not** propose, select, recommend, or endorse a trading-hours session template. That is build work gated on frozen criterion **F2** and is a hard stop. No argument is made here that F2 is satisfied, and no session template is suggested as one that "would work". Which session definition is **correct** is Amear's question (S8); this report ends with the evidence laid side by side and the decision left open.

---

## Process log

1. Confirmed both named files exist on disk and captured their sizes/line counts.
2. Grepped the b2 spec for RTH / session / hour-range tokens, then separately for every common time-zone token.
3. Pulled the §4.1 session-definition table and §4.2 timezone block verbatim with line numbers.
4. Ran the mandated grep verbatim against the nt8-windows-reference.
5. Located the "Residual gaps" section and quoted it verbatim.
6. Ran a bounded corroborating search across `docs/specs`, `docs/reference`, `config` for `8:30` / `Central` / `CT` to test whether any *other* disk artifact supplies a CT anchor.

---

## Verification evidence

### Q3a — What does the b2 spec fix as the RTH session definition?

Command:

```
grep -n "" /Volumes/Sensidine/Praxis.build/docs/specs/2026-07-15-b2-data-acquisition-spec.md | sed -n '76,92p'
```

Output:

```
76:Approximate expected 1-min bar counts (before gap-filling; sessions are the CME Nasdaq equity-index schedule):
77:
78:| Session | Definition (ET) | Expected 1-min bars / full day | Check |
79:|---------|-----------------|-------------------------------|-------|
80:| **RTH** | 09:30–16:00 | **390** bars/day (391 boundary-inclusive) | Median RTH day == 390 ± a few (holidays/half-days excluded) |
81:| **ETH** | Sun/day 18:00 → next 17:00, 1h break 17:00–18:00 | **~1,380** bars/day (23h × 60) | Median full ETH day in **[1,350, 1,380]** |
82:| **Half-days** | early close 13:00 ET (e.g. day after Thanksgiving) | RTH ~210 | Flag as expected, not a gap |
83:
84:- [ ] **Total bar count** in range: ~1,255 trading days × ~1,380 ETH bars ≈ **1.6–1.75M** ETH 1-min bars over the 5-yr pull. Order-of-magnitude check; a result off by >20% signals a session-template or depth problem.
85:- [ ] **Per-day median** RTH == 390, ETH within [1,350, 1,380]. Days far below → missing-bar problem (§4.3); days far above → duplicate/overlap problem (§4.4) or wrong session template.
86:
87:### 4.2 Timezone / session handling
88:
89:- [ ] Session boundaries land at the **correct ET wall-clock** across **both DST transitions each year** (spring-forward / fall-back) — confirm the 18:00 ET session open holds through March and November DST flips (a fixed-UTC misconfig drifts by 1h).
90:- [ ] The **17:00–18:00 ET daily maintenance break** shows **no bars** (matches the consumer's session-hours guard, runbook §6).
91:- [ ] RTH filter reproduces 09:30–16:00 ET exactly and yields the 390-bar median.
92:
```

**Answer Q3a:** The spec fixes RTH as **09:30–16:00**, carrying an expected **390 one-minute bars per full day** (391 boundary-inclusive). Line 91 restates it as a hard acceptance check: *"RTH filter reproduces 09:30–16:00 ET exactly and yields the 390-bar median."* Note the internal self-consistency: 09:30→16:00 is 6h30m = 390 minutes, which matches the stated bar count exactly.

Also relevant, from the spec's header table:

```
grep -n "" /Volumes/Sensidine/Praxis.build/docs/specs/2026-07-15-b2-data-acquisition-spec.md | sed -n '18,19p'
```

```
18:| Session template | Both **ETH** (globex full session) and **RTH** derivable; pull ETH so RTH is a subset filter, never re-pulled |
19:| Timezone | Store/interpret in exchange time; NT8 charts in the platform TZ. Session handling per §4 |
```

The spec's own architecture is that **ETH is pulled and RTH is a downstream subset filter**, not a separately pulled series (line 18, restated at line 117).

---

### Q3b — In which time zone is that definition anchored?

The spec **does** name a zone. This is **not** a gap on the zone-naming question, and I am reporting that as found rather than forcing a null.

The zone is established in two places, quoted verbatim above:

- **Line 78** — the table's column header is literally `| Session | Definition (ET) | ...`. The hour ranges in that table are therefore declared to be ET by the column header itself.
- **Line 91** — `RTH filter reproduces 09:30–16:00 ET exactly` — the zone token is inline with the hours, so it does not depend on inheriting the column header.

Supporting count of the ET token across the spec:

```
$ grep -c "ET" /Volumes/Sensidine/Praxis.build/docs/specs/2026-07-15-b2-data-acquisition-spec.md
13
```

**Answer Q3b: the b2 spec anchors RTH 09:30–16:00 in ET.** The anchor is explicit, appears in both a column header and inline with the hours, and is reinforced by the DST check at line 89 which is written in ET wall-clock terms.

**Two honest sub-gaps, reported without resolution:**

1. **`ET` is never expanded anywhere in the spec.**
   ```
   $ grep -n "Eastern" /Volumes/Sensidine/Praxis.build/docs/specs/2026-07-15-b2-data-acquisition-spec.md
   === Eastern exit: 1 (1 = zero) ===
   ```
   Zero matches. The abbreviation is standard and unambiguous in this domain, so I flag this as a precision note, not a substantive gap.

2. **`exchange time` at line 19 is an undefined term — this IS a gap.** It appears exactly once:
   ```
   $ grep -nc "exchange time" .../2026-07-15-b2-data-acquisition-spec.md
   1
   19:| Timezone | Store/interpret in exchange time; NT8 charts in the platform TZ. Session handling per §4 |
   ```
   The spec instructs storage/interpretation in "exchange time" and separately labels its session table "(ET)", but never states anywhere on disk whether those two are the same zone. It also never names the "platform TZ". I am **not** resolving what "exchange time" denotes for CME — that resolution is exactly the kind of inference this task forbids, and it bears directly on the open question.

---

### Q3c — What does the nt8-windows-reference record about `Tools > Trading Hours`?

Mandated command, run verbatim:

```
grep -ni "trading hours\|time zone\|timezone\|central\|CST\|CDT\|Eastern\|ET\b" /Volumes/Sensidine/Praxis.build/docs/reference/2026-07-24-nt8-windows-reference.md
```

Output (full, unedited):

```
5:**Target install (version-stamped):** NinjaTrader **8.1.7.2 (64-bit)**, Windows 11 VM (Parallels).
11:2. **Live-install half** — 20 screenshots + capture notes taken on this VM on 2026-07-24 08:14–08:44 ET by the Cowork agent (sim-only, no orders/compile/run). Raw captures + the coworker's `00-notes.txt` are in [`assets/nt8-2026-07-24/`](assets/nt8-2026-07-24/).
31:- **New menu** ([`09-new-menu.png`](assets/nt8-2026-07-24/09-new-menu.png)): Basic Entry · FX Pro · Option Chain · Order Ticket · SuperDOM Dynamic · SuperDOM Static · Alerts Log · Calendar · **Chart** · Depth Chart · FX Board · FX Correlation · Hot List Analyzer · Level II · Market Analyzer · Market Watch · News · Pulse · **Strategy Analyzer** · T&S · Account Data · Trade Performance · **NinjaScript Editor** · NinjaScript Output · Strategy Builder.
32:- **Tools menu** (from notes): Instruments · Instrument Lists · Database Management · Hot Keys · **Historical Data** · Commissions · Risk · **Trading Hours** · Import · Export · Remove NinjaScript Assembly… · Global Simulation Mode *(license-gated)* · Client Dashboard · Settings.
40:- **What it's for:** root window, always open while NT8 runs; centralized view of accounts, orders, executions, positions, logs; toggles global app features.
47:  - **Accounts** — account rows incl. **Sim101** (cash, P&L, buying power); right-click to Edit/Reset a sim account. ([`07-cc-accounts.png`](assets/nt8-2026-07-24/07-cc-accounts.png))
70:- **What it's for:** access/manage all historical + Market Replay data; Import, Export, Download, and inspect Loaded data.
72:- ⚠️ **LIVE — CORRECTION to the Help Guide:** in 8.1.7.2 this window is a **vertical accordion** with stacked expand/collapse sections **Loaded · Download · Import · Export · Get Market Replay data** — **not** the horizontal Import/Export/Edit/Download *tab* strip the public Guide implies. ([`15-historical-data-loaded.png`](assets/nt8-2026-07-24/15-historical-data-loaded.png))
85:- **What it's for:** configure/connect/disconnect market-data and brokerage connections; per-provider + aggregate status (bottom-left of Control Center).
98:3. **Time Zone of Imported Data** — the zone the file's timestamps are in (set to match the source file exactly).
102:**⚠️ LIVE — the instrument gotcha, now confirmed by evidence:** the **Import** section has **no instrument field** (Format / Data Type / Time Zone / Import only — [`16-historical-data-import.png`](assets/nt8-2026-07-24/16-historical-data-import.png)); the **Download** section *does* have an Instrument field ([`17-historical-data-download.png`](assets/nt8-2026-07-24/17-historical-data-download.png)). So NT8 derives the import's target instrument **from the filename**, not from any dialog field. This is exactly what blocked the 4uu import (`NQ-continuous-1min.nt8import.txt` → "Instrument is not supported by repository").
150:4. **Time frame:** **Start date** / **End date** · **Trading hours** = **session template dropdown** — for PRAXIS RTH select **"CME US Index Futures RTH"** · **Break at EOD**.
156:- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)
167:3. In the Configured instance set: **Data Series** · **Account = Sim101** · **Strategy Parameters** · **Calculate** mode.
168:4. Set **"Enabled" = True** to run (False = attached but inactive).
189:- **Global:** `Tools > Options > Market Data > Merge policy`. **Per-instrument:** `Tools > Instruments` → select → **Edit** → **Merge policy**.
205:**Reset Sim101** (clears sim state between backtests): `Accounts` tab → right-click **Sim101** → **Edit** → set **"Initial cash"** → **"Reset"**. (Sim accounts are USD-only.)
213:1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*
214:2. Historical Data **Export** and **Get Market Replay data** accordion sections — not expanded/captured. *(§1e)*
218:## Asset index
---GREP EXIT:0---
```

Section-heading inventory, to confirm `Tools > Trading Hours` has no documented section of its own:

```
$ grep -n "^#\{1,4\} " /Volumes/Sensidine/Praxis.build/docs/reference/2026-07-24-nt8-windows-reference.md
1:# NinjaTrader 8 (Windows) — Layout & Workflow Reference
19:## 0. Fast orientation (this install at a glance)
37:## 1. UI Layout / Windows
39:### 1a. Control Center
52:### 1b. NinjaScript Editor
58:### 1c. Strategy Analyzer
63:### 1d. Chart
69:### 1e. Historical Data window
75:### 1f. Instruments manager
80:### 1g. Instrument Lists
84:### 1h. Connections
91:## 2. Import Historical Data — NT8 Native Format
124:## 3. Compile a NinjaScript Strategy
142:## 4. Configure + Run Strategy Analyzer (Backtest)
160:## 5. Add a Strategy to a Chart on Sim101
180:## 6. Continuous / Custom-Instrument Setup (Futures)
195:## 7. Sim Account Operations — Flatten / Cancel All (Sim Safety)
212:## Residual gaps (for a future capture pass)
218:## Asset index
221:## Help Guide source index
```

**Answer Q3c.** The reference records `Tools > Trading Hours` in exactly **three** places, and none of them documents the window's contents:

- **Line 32** — it appears only as an *item in the Tools menu listing*, sourced "(from notes)". It is a menu entry, nothing more.
- **Line 156** — an explicit TODO stating the template's printed hours were **not captured**.
- **Line 213** — the same item repeated in the Residual gaps list.

There is **no `### Tools > Trading Hours` section** in the heading inventory. The window was never opened or screenshotted in the 2026-07-24 capture pass.

**Does the corpus document a TIME ZONE SELECTOR / dropdown that CHANGES the displayed session values in `Tools > Trading Hours`? — NOT DOCUMENTED.** Plainly: no such selector is described anywhere in this file.

Two near-misses that must not be mistaken for it, since both surfaced in the mandated grep:

- **Line 98 / 102 — "Time Zone of Imported Data".** This is a field in the **Historical Data → Import** accordion section, described as "the zone the file's timestamps are in (set to match the source file exactly)". It governs how an import file's timestamps are interpreted. It is a **different window** from `Tools > Trading Hours` and says nothing about how a session template renders.
- **Line 150 — "session template dropdown".** This is the **Trading hours** field inside the Strategy Analyzer's Time-frame panel, where one *picks a template* (e.g. "CME US Index Futures RTH"). It is a template selector, **not** a time-zone selector, and the reference does not describe it as re-rendering any hours.

**Evidence grading (mandatory).** Nobody in this session has run NinjaTrader.
- *Claim: NT8's `Tools > Trading Hours` window contains a time-zone control that re-renders the displayed session hours.* — **UNVERIFIED / not on disk.** This mechanism is not documented in the corpus and was not observed by anyone in this session. **The single observation that would settle it:** open `Tools > Trading Hours`, select the `CME US Index Futures RTH` template, screenshot the panel showing both the hour fields and whatever zone control sits beside them, then change that control to a second zone and screenshot again — if the hour fields change value, the control re-renders; if they do not, it does not.
- *Claim: the template printed `8:30 AM` to `4:00 PM` with time zone shown as `Central` on 2026-08-29.* — **VERIFIED-BY-REPORT, single observer, un-screenshotted.** Observed by **Amear** on **2026-08-29** by hand in `Tools > Trading Hours`. This is the only runtime evidence in existence on this question. It is a hand reading, not a capture; no artifact of it exists on disk under `assets/`.

---

### Q3d — The "Residual gaps" section

Command:

```
grep -n "" /Volumes/Sensidine/Praxis.build/docs/reference/2026-07-24-nt8-windows-reference.md | sed -n '210,217p'
```

Output:

```
210:---
211:
212:## Residual gaps (for a future capture pass)
213:1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*
214:2. Historical Data **Export** and **Get Market Replay data** accordion sections — not expanded/captured. *(§1e)*
215:3. `.zip` direct-import support — undocumented, untested. *(§2)*
216:4. Exact right-click wording for **Flatten Account / Flatten Everything / Close Position**. *(§7)*
217:
```

**Answer Q3d: CONFIRMED, with a wording correction.**

The claim in the brief was that the section lists *"RTH template exact hours (Tools>Trading Hours)"* as NOT captured. The section **does** carry that item, as **entry 1** of 4, at **line 213**. The substance of the claim holds.

The exact on-disk wording differs from the paraphrase and is worth recording precisely, because the difference is load-bearing:

> `1. `Tools > Trading Hours` — exact printed hours of the **CME US Index Futures RTH** template (confirm 09:30–16:00 ET). *(§4)*`

Two things the verbatim text says that the paraphrase drops:

1. It names the template specifically — **"CME US Index Futures RTH"** — not RTH generically.
2. It states the *purpose* of the future capture as **"(confirm 09:30–16:00 ET)"**. The reference file therefore recorded, on 2026-07-24, an **unconfirmed expectation** that this template would turn out to equal 09:30–16:00 ET. It is written as a check still to be performed, not as a finding.

The paired TODO at line 156 is more explicit still and adds a detail absent from line 213:

```
156:- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)
```

Note the phrase **"record the printed CT hours here"**. The author of the reference anticipated, as of 2026-07-24, that this window would print in **CT** and that an **equivalence** would need establishing against the spec's ET figures. That anticipation was never discharged — the hours were never captured, and no CT value was ever recorded in this file.

Corroborating bounded search — is a CT/Central anchor supplied anywhere else in specs, reference, or config?

```
$ grep -rnE "8:30|Central|\bCT\b" --include="*.md" --include="*.json" \
    /Volumes/Sensidine/Praxis.build/docs/specs \
    /Volumes/Sensidine/Praxis.build/docs/reference \
    /Volumes/Sensidine/Praxis.build/config
/Volumes/Sensidine/Praxis.build/docs/reference/2026-07-24-nt8-windows-reference.md:156:- 🔲 **TODO (residual gap):** the **"CME US Index Futures RTH"** template's exact printed session hours were **not** captured. Verify **09:30–16:00 ET** equivalence via `Tools > Trading Hours` and record the printed CT hours here. (Tracked in the follow-up bead — see footer.)
```

**Exactly one hit, and it is the TODO itself.** Across all of `docs/specs`, `docs/reference`, and `config` there is **no `8:30`, no `Central`, and no CT hour value on disk** — the sole `CT` token is the unfulfilled instruction to go record one.

---

### Q3e — Arithmetic relationship (neutral observation only)

The two sides:

| Side | Source | Hours | Zone token | Status |
|---|---|---|---|---|
| Spec | b2 spec L78/L80/L91 | 09:30 – 16:00 | **ET**, explicit | On disk |
| Observation | Amear, 2026-08-29, `Tools > Trading Hours` | 8:30 AM – 4:00 PM | **Central**, as displayed | Hand reading, not on disk, not screenshotted |

Both sides carry a zone token, so they are **comparable in principle**. Stating the arithmetic, and nothing beyond it:

**Durations.**
- Spec: 09:30 → 16:00 = **6h 30m = 390 minutes**. This matches the spec's own stated 390 bars/day (line 80), so the spec is internally consistent.
- Observed: 8:30 AM → 4:00 PM = **7h 30m = 450 minutes**.
- **Difference: 60 minutes.** The observed window is one hour longer.

**Endpoint-by-endpoint, converting the spec's ET figures into the observed side's Central frame at the standard one-hour offset (ET = CT + 1h):**
- Spec **open** 09:30 ET → **08:30** in the Central frame. Observed open **8:30 AM Central**. → **These agree exactly.**
- Spec **close** 16:00 ET → **15:00** in the Central frame. Observed close **4:00 PM = 16:00 Central**. → **These differ by one hour.**

**Neutral characterisation.** The two are **INCONSISTENT**, and the inconsistency is **asymmetric and localised to the close**. The opens reconcile exactly under a one-hour zone offset; the closes do not, and the duration gap of 60 minutes is entirely attributable to that one endpoint. This is *not* the signature of a whole-window zone-labelling slip — a pure zone mislabel would shift *both* endpoints together and preserve the 390-minute duration. Here the duration itself changes.

This is a **NOT COMPARABLE** case in one narrower respect that must be stated: the spec's line 19 instructs storage/interpretation in **"exchange time"**, a term the spec never defines and which is nowhere reconciled on disk against its own "(ET)" table label. So while the *table* is comparable to the observation, the spec's *storage/interpretation* rule is not comparable to anything, because its zone is undefined.

**I draw no conclusion about which side is correct, and propose no fix.** Specifically I am not asserting that the template is wrong, that the spec is wrong, that the observation was misread, that some control was set to a non-default value, or that any particular template should be selected instead. Each of those is either Amear's call (S8) or gated on frozen **F2**. The evidence is laid out; the decision stays open.

---

## Adjacent disk finding (outside the two named files) — reported, not resolved

The brief scoped reading to two files. A bounded corroborating search surfaced two other on-disk mentions, recorded here for completeness and explicitly **not** used to resolve anything above:

```
$ grep -o "CME US Index Futures[^|]\{0,220\}" STATUS.md DECISION_LOG.md
STATUS.md:CME US Index Futures RTH) so continuous data never collides w/ native NQ and the 09:30 alignment check works; **Time Zone = US Eastern pinned (NOT UTC).** New Step 0b = create NQCONT; ...
DECISION_LOG.md:CME US Index Futures RTH template prints `8:30 AM – 4:00 PM`, time zone shown as `Central`. THE MASTER DECLINES TO CONFIRM THIS AS A GENUINE MISMATCH, BECAUSE BOTH HALVES OF THAT CONFIRMATION ARE UNOBSERVED**
```

- **STATUS.md** records `Time Zone = US Eastern pinned (NOT UTC)` as part of the trader-chosen `NQCONT` custom-instrument plan. Read in its surrounding context, this is the **import-side** zone pin (the "Time Zone of Imported Data" field, reference line 98), which is a **distinct setting** from whatever zone a session template displays in. I am not treating it as an answer to Q3b and am not reconciling it against the Central observation.
- **DECISION_LOG.md** already carries today's observation and already records that the master **declines** to confirm it as a genuine mismatch on the grounds that both halves are unobserved. This report is consistent with that posture and does not disturb it.

---

## Summary of answers

- **Q3a** — RTH is fixed at **09:30–16:00**, 390 bars/day, restated as a hard acceptance check at line 91. ETH is pulled; RTH is a downstream subset filter.
- **Q3b** — The zone **is** anchored, explicitly, as **ET** (line 78 column header; line 91 inline). **Not a gap.** Sub-gap: `exchange time` at line 19 is undefined and never reconciled to "(ET)".
- **Q3c** — `Tools > Trading Hours` appears only as a menu item and twice as a TODO; it has no documented section. A time-zone selector that changes displayed session values is **NOT DOCUMENTED**.
- **Q3d** — **CONFIRMED** at line 213 (entry 1 of 4), with the on-disk wording naming the template and framing the item as "(confirm 09:30–16:00 ET)" — an unconfirmed expectation, not a finding. Line 156 additionally anticipated recording **CT** hours; never done.
- **Q3e** — **INCONSISTENT**, asymmetrically: opens agree exactly under a one-hour offset, closes differ by one hour, duration differs by 60 minutes (390 vs 450). No conclusion drawn as to which is correct.

## Files staged

**None.** This was a read-only research task. No file was edited, created, or deleted except this report, which is left **unstaged and uncommitted**. No `git add`, no `git commit`. Nothing was written under `.claude/agent-memory/`.

## Result

**PASS** — all five sub-questions answered from disk with pasted command output; the one genuine gap (undefined "exchange time", plus the never-captured CT hours) reported as a gap; the frozen-F2 and S8 boundaries held.
