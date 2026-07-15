# B2 Data Acquisition Spec — NQ Minute History

**Bead:** Praxis_build-hlw (b2-data)
**Date:** 2026-07-15
**Status:** Mac-side spec COMPLETE. Physical pull + validation is VM-GATED (see §5, §6).
**Locks consumed:** DECISIONS.md D-2026-07-15-B (Q4 data, Q5 cost, Q7 WFA windows, Q8 platform).
**Scope boundary:** The history pull runs inside NinjaTrader 8 on the Win11 ARM VM (D-2026-07-09-B). This document makes that pull a mechanical, checkable step. It does NOT assert any data has been downloaded or validated.

---

## 1. Instrument, granularity, depth

| Field | Value |
|-------|-------|
| Instrument | **NQ** — E-mini Nasdaq-100 futures (CME) |
| Contract form | **Continuous / front-month rolled** (see §2 roll convention) |
| Granularity | **1-minute bars** (NT8 default-provider minute data; Q4 — no paid-data budget) |
| Session template | Both **ETH** (globex full session) and **RTH** derivable; pull ETH so RTH is a subset filter, never re-pulled |
| Timezone | Store/interpret in exchange time; NT8 charts in the platform TZ. Session handling per §4 |

### 1.1 Concrete date range (≥4-year depth)

- **Pull start:** **2021-07-15**
- **Pull end:** **2026-07-14** (last complete trading day before today, 2026-07-15)
- **Nominal span:** ~5.0 calendar years ≈ **~1,255 trading days**.

**Why 5 years, not exactly 4:** The Q7 WFA is rolling **252 IS / 63 OOS / 63 step** (trading days). Window count = `floor((N_days - 252) / 63) + 1`.

- 4-year floor (~1,008 td) → `floor((1008-252)/63)+1 = 13` OOS windows — only just clears the ≥12 target with zero margin and no indicator warmup budget.
- 5-year pull (~1,255 td) → `floor((1255-252)/63)+1 = 16` OOS windows, **and** leaves headroom for the longest indicator lookback warmup (the IS window's first bars need prior bars to prime ATR / lookback channel; a bare 4-yr pull would spend OOS windows on warmup).

**Depth-shortfall rule (Q4):** If the default provider returns **fewer than ~1,008 trading days** (the 4-yr / ≥12-window floor), the operator MUST log the actual first available bar timestamp and resulting window count in the pull report and flag it — a shortfall is **logged, not silently accepted** (D-2026-07-15-B Q4). Do not shrink the WFA window sizes to manufacture windows.

---

## 2. Roll convention — RECOMMENDED (trader to lock)

> **STATUS: RECOMMENDED — trader to lock.** Roll construction materially changes backtest P&L, so it is trader-gated for final lock, not self-certified. The recommendation below is the default the operator should build unless the trader overrides.

### 2.1 Recommendation

| Dimension | Recommendation | NT8 setting |
|-----------|----------------|-------------|
| **Roll trigger** | **Volume/OI crossover** — roll to the next contract on the day the incoming month's volume (confirmed by open interest) overtakes the front month. | NT8 Instrument → *Roll-over* tab: roll by **Volume** (with OI confirmation), NOT a fixed calendar/expiry offset. |
| **Back-adjustment** | **Back-adjusted (Difference / "Panama" method)** — splice contracts and shift the older history by the cumulative roll gap so there is **no artificial price jump** at each roll seam. | NT8 roll-over adjustment type = **Difference** (not *None*, not *Ratio*). |

### 2.2 Why this fits a breakout strategy

The Block-2 strategy optimizes `{lookback, noise multiplier, stop-ATR multiplier, exit policy}` (Q7) — a **volatility/channel breakout** that measures signals as **absolute point distances** (channel width, ATR-scaled stops, noise bands).

- **Back-adjustment (Difference) is required, not optional.** An **unadjusted** splice leaves a raw price gap at every roll (the front/next spread, often tens of NQ points). To a breakout detector that gap is indistinguishable from a real range expansion → **fabricated breakout signals and fake stop-outs at every roll boundary** (~4/year). Difference back-adjustment removes the seam while **preserving the true point size** of every historical move — exactly the quantity the breakout logic and the ATR/point-based stops depend on.
- **Why Difference, not Ratio:** Ratio (percentage) back-adjustment preserves returns but **distorts absolute point distances** — it would rescale historical channel widths and ATR values, corrupting the very inputs being optimized. Since sizing/P&L is held in points → ticks → R-multiples (Q6), the percentage fidelity Ratio buys is irrelevant here, while the point distortion it introduces is directly harmful.
- **Why volume/OI roll, not calendar:** Rolling on the liquidity crossover keeps the continuous series on the **actually-traded** contract, so fills, slippage (Q5, 1 tick/side), and the High-resolution intrabar path reflect real book depth. A fixed calendar roll can sit on a thin expiring month for extra days, poisoning fill realism.

**Known cost of Difference back-adjustment (disclosed):** absolute historical price levels are synthetic (early bars may print far from the real 2021 quote, and deep-history prices can even go negative over very long spans). This is acceptable because the strategy trades **relative** structure (breakouts, ATR-scaled stops), never an absolute price threshold. Any rule that ever compares to an absolute price level would break under back-adjustment — none is planned; flag it if one is introduced.

---

## 3. Roll-point sanity checks (post-pull)

The operator confirms the continuous series was constructed as specified:

- [ ] **Roll count:** ~4 rolls/year (NQ quarterly cycle H/M/U/Z → Mar/Jun/Sep/Dec). Over ~5 yr expect **~20 roll seams**. Materially fewer/more → wrong trigger.
- [ ] **Seam continuity:** At each roll timestamp the bar-to-bar price delta is **within normal 1-min volatility** (no multi-point step discontinuity). A visible gap at a roll = back-adjustment did NOT apply → re-pull with Difference.
- [ ] **Roll timing:** Each roll lands **near** the volume/OI crossover for that quarter (not weeks early/late) — spot-check 2–3 rolls against the exchange volume crossover.
- [ ] **Monotonic timestamps across seams:** no timestamp overlap or reversal where one contract ends and the next begins.

---

## 4. Validation criteria (VM operator checks after pull)

Each criterion is objectively checkable against the exported series. Record PASS/FAIL + the measured number in the pull report.

### 4.1 Bar-count ranges

Approximate expected 1-min bar counts (before gap-filling; sessions are the CME Nasdaq equity-index schedule):

| Session | Definition (ET) | Expected 1-min bars / full day | Check |
|---------|-----------------|-------------------------------|-------|
| **RTH** | 09:30–16:00 | **390** bars/day (391 boundary-inclusive) | Median RTH day == 390 ± a few (holidays/half-days excluded) |
| **ETH** | Sun/day 18:00 → next 17:00, 1h break 17:00–18:00 | **~1,380** bars/day (23h × 60) | Median full ETH day in **[1,350, 1,380]** |
| **Half-days** | early close 13:00 ET (e.g. day after Thanksgiving) | RTH ~210 | Flag as expected, not a gap |

- [ ] **Total bar count** in range: ~1,255 trading days × ~1,380 ETH bars ≈ **1.6–1.75M** ETH 1-min bars over the 5-yr pull. Order-of-magnitude check; a result off by >20% signals a session-template or depth problem.
- [ ] **Per-day median** RTH == 390, ETH within [1,350, 1,380]. Days far below → missing-bar problem (§4.3); days far above → duplicate/overlap problem (§4.4) or wrong session template.

### 4.2 Timezone / session handling

- [ ] Session boundaries land at the **correct ET wall-clock** across **both DST transitions each year** (spring-forward / fall-back) — confirm the 18:00 ET session open holds through March and November DST flips (a fixed-UTC misconfig drifts by 1h).
- [ ] The **17:00–18:00 ET daily maintenance break** shows **no bars** (matches the consumer's session-hours guard, runbook §6).
- [ ] RTH filter reproduces 09:30–16:00 ET exactly and yields the 390-bar median.

### 4.3 Gap-detection rule

- [ ] **Intra-session gap:** within a single trading session, any interval where consecutive 1-min bar timestamps differ by **> 1 minute** is a gap. Emit a gap list (timestamp, duration). **Expected/benign:** the 17:00–18:00 break, weekend close (Fri 17:00 ET → Sun 18:00 ET), CME holidays. **Anomalous:** any intra-session gap > ~3 min not on the holiday/break calendar → investigate before use.
- [ ] Gap total: anomalous-gap minutes should be a **tiny fraction** (< ~0.1%) of session minutes. A large fraction → provider data hole; log depth-shortfall.

### 4.4 Duplicate / missing-bar handling

- [ ] **Duplicates:** zero bars sharing an identical timestamp. Any duplicate timestamp → dedup and record how many (usually a roll-seam overlap artifact).
- [ ] **Missing bars policy:** the export is **left un-synthesized** (no forward-filled phantom bars) — the WFA runs on real bars only. If any downstream tool requires a continuous grid, gap-fill is a **separate, logged** transform, never baked into the source artifact.
- [ ] **Monotonic non-decreasing timestamps** end-to-end (superset of the §3 seam check).

### 4.5 Acceptance gate

The pulled series is accepted for WFA when: bar-count medians pass (§4.1), TZ/session boundaries pass (§4.2), anomalous-gap fraction is < ~0.1% (§4.3), zero unresolved duplicates (§4.4), roll seams pass (§3), **and** depth ≥ ~1,008 trading days (else shortfall logged per §1.1). Any FAIL → fix the pull config and re-pull; do not proceed to b2-wfa on a failed series.

---

## 5. VM operator runbook — pull + export

**Host:** NinjaTrader 8 on the Parallels Win11 ARM VM (D-2026-07-09-B). All steps are TRADER/operator-touch inside the VM; the Mac cannot execute them.

1. **Set the continuous-contract roll (§2) BEFORE downloading.** NT8 → *Tools → Instruments* → search `NQ` → open the futures instrument → *Roll-over* tab: set roll trigger = **Volume** (OI-confirmed), adjustment = **Difference**. Save. (If the trader has NOT yet locked §2, stop and get the lock — the roll setting determines what gets downloaded.)
2. **Download the minute history.** NT8 → *Tools → Historical Data* (Data window) → *Download* tab → instrument `NQ` (continuous) → data type **Minute**, interval **1** → date range **2021-07-15 → 2026-07-14** → run. Default provider only (Q4 — no paid feed). Let it complete; large multi-year minute pulls take time.
3. **Verify load on a chart.** Open a `NQ` 1-min chart spanning the full range; confirm it renders start→end without an obvious blank stretch (quick visual pre-check before the §4 numeric checks).
4. **Export the artifact.** Export the 1-min series to a delimited file (NT8 Historical Data → *Export*, or Grid → export). Include full timestamp (date + HH:MM), OHLCV. Export **ETH (full session)** so RTH is a downstream filter.
5. **Landing location:** write the export to the VM→Mac shared path so it reaches the repo host — **`\\Mac\praxis-signals\b2-data\NQ-1min-2021-07-15_2026-07-14.csv`** (the same Parallels share used by the signal path; a dedicated `b2-data\` subfolder keeps history artifacts out of the live signal drop). Record the exact filename, row count, and file size in the pull report.
6. **Run the §3–§4 checks** against the export (spreadsheet or the Python layer on the Mac once the file syncs) and fill in PASS/FAIL + measured numbers. Attach the gap list and roll-seam spot-checks.
7. **Report back:** first bar timestamp, last bar timestamp, total row count, per-day RTH/ETH medians, anomalous-gap count, duplicate count, roll-seam results, and depth-vs-floor (≥1,008 td?). This report is the evidence that closes the VM-gated half of bead hlw.

---

## 6. What remains VM-gated

Everything in §5 (the physical download + the §3/§4 validation execution) happens **inside the VM** and is **not done** by this spec. Mac-side deliverables complete now: this spec, the roll recommendation (pending trader lock), and the machine-readable cost model (`config/backtest-cost-model.json`). The b2-data bead is **half-open**: Mac-side spec landed; VM operator pull + validation + roll-lock still required before b2-wfa (Praxis_build-zi1) can run.
