# Handoff to the voice agent — 2026-11-01, commission fix + baseline re-run on Fusion

**From:** praxis-master (Claude Code), written 2026-11-01T11:26Z at Amear's request.
**For:** the voice agent working with Amear at the Fusion VM, and for Amear himself.
**Assume nothing was read before this.** This brief is self-contained. The previous brief
(`docs/reports/2026-10-31-voice-handoff-future-row-walkthrough.md`) and the full walkthrough
(`docs/reports/2026-10-31-a9d-walkthrough-future-row.md`, on `main` at `d2ff631`) are the authority
for anything this brief does not cover; this brief tells you only what to do **now**.

Evidence grades: OBSERVED (read from a file or screen) · INFERRED (reasoned) · REPORTED BY AMEAR ·
UNVERIFIED. Claude has never seen the Fusion screen. **Amear's screen wins over every Expect line.**

**Where to write results:** append to `docs/reports/2026-10-31-voice-session-notes-2.md` under a new
heading `## 3. 2026-11-01 session — commission fix and re-run`. Same shape as before: step number,
what was read back verbatim, pass / STOP, Amear's rulings in his words with the time. If file access is
lost again, Amear pastes the summary into Claude Code and the master writes it.

---

## 0. Where things stand (one paragraph)

Yesterday Amear created a new **Future** instrument row on Fusion named **`NQCONTROW`** (his own; the two
existing `NQCONT` rows — one Stock, one Future — are untouched), imported the 1-minute history onto it as
`NQCONTROW 09-25.Last.txt` (1,711 daily files, 2021-03-07 → 2026-07-20), set the 09-25 contract's rollover
date to 2021-03-01 and merge policy to Do not merge, confirmed both spot-check bars match the file exactly,
and ran one Strategy Analyzer backtest — **run 0-S on `NQCONTROW SEP25`** with the run-4 settings and the
RTH template. Result: 1,190 trades (556 L / 634 S), net $200,850, profit factor 1.30, max drawdown −$44,545,
total slippage 1,190, **commission $0.00**. The walkthrough's STOP fired on the commission ($0, not
1,190 × $2.96), so Phase 4 (save settings as default) was **not** entered. Nothing is broken; the STOP was
the designed outcome.

Amear's rulings since then (logged, DECISION_LOG 2026-10-31 18:21Z block):
- **R-A9D-1:** `NQCONTROW` is his row, created before the import. Fine as is.
- **R-A9D-2:** this Future-row run is the new baseline, judged on its own. Old run 4 (Stock row) is retired.
  The 1,190-vs-1,211 trade-count difference is bead `Praxis_build-q36`, **not a blocker**. Do not chase it
  in this session.
- **R-A9D-3:** commission fix approved as: **readback first → one edit → re-run 0-S** as the baseline run.

## 1. Why commission is $0 (INFERRED — the readback below tests it)

The `PRAXIS` commission template was created on 2026-10-28 as "minimum 0, per unit $1.48 per side,
assigned to Sim101" (10-28 voice notes, line 32) — on a day when `NQCONT` resolved to the **Stock** row.
NT8 commission templates carry rates per instrument type (and optionally per instrument). So the $1.48
rate is most likely bound to the Stock type or to the `NQCONT` instrument, and a Future-typed
`NQCONTROW` has no rate → $0.00. **If the readback shows something else, write down what it shows and
STOP — Claude names the edit, not the agent.**

## 2. What to do now — in order, one step per exchange

Narration rules (unchanged from yesterday): one step per exchange; read the Path, ask for the readback,
give the Expect only after Amear has read the screen; **every STOP is literal** — Amear does nothing
further in NT8, reads back the screen, and the session returns to Claude Code; no trading-hours template is
ever edited (F2 FROZEN); no run other than the one named here; no Delete control anywhere.

### Step C1 — Commission readback (READ-ONLY; close with Cancel or X)
- **Path:** NinjaTrader Control Center → `Tools` → `Commissions`. In the left list select `PRAXIS`.
- **Read back, verbatim, every row the right-hand grid shows:** for each row its instrument type (or
  instrument name if the dialog is per-instrument), `Per unit`, `Per order`, `Minimum`, and any other
  column present. Also read back the list of templates in the left pane, and whether there is an
  "instrument" selector / "Add instrument" style control anywhere in the dialog.
- **Expect (INFERRED):** one or more rows; a row for Stock (or for `NQCONT`) with Per unit 1.48; **no row
  for Future and no row for `NQCONTROW`**.
- **Falsifier:** a Future row (or `NQCONTROW` row) already showing 1.48 → STOP; the $0 cause is elsewhere
  (e.g. the Analyzer's own Commission field or the account's template binding) — bring the readback back.
- **Close with Cancel.** Nothing is changed in C1.

### Step C2 — STOP: send the C1 readback to Claude Code before any edit
Paste the readback into Claude Code. The master names the one edit. **Do not guess the edit.** The
expected edit, if C1 came back as expected, is in C3 — but C3 is not executed until Claude has confirmed
it against the readback.

### Step C3 — The one edit (only after C2)
- **Path:** `Tools` → `Commissions` → select `PRAXIS` → in the grid, the **Future** row (or add/select
  `NQCONTROW` if the dialog is per-instrument): set `Per unit` = **1.48**. `Per order` stays as it is on the
  Stock row. `Minimum` stays 0. OK.
- **Read back before OK:** the whole grid again, verbatim.
- **Any prompt mentioning delete / remove / replace / reset → STOP.**
- Also confirm (read-only) that account `Sim101` still has `PRAXIS` as its commission template:
  Control Center → `Accounts` tab → right-click `Sim101` → `Edit Account` → Commission field. Cancel.

### Step C4 — Re-run 0-S on `NQCONTROW SEP25` (the baseline run)
- Same Analyzer settings as yesterday's run (run-4 settings): instrument `NQCONTROW SEP25`, 1-minute, trading
  hours `CME US Index Futures RTH` (select only, never edit), Standard fill resolution, slippage 2,
  the same date range, same account `Sim101`, Commission = the template `PRAXIS` (read back which commission
  control the Analyzer shows and its value — if it has its own commission field and it is not `PRAXIS` /
  the template, read it back and STOP).
- **Run description, verbatim (F3 sentence):**
  `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
- **Read back every settings field before Run**, then Run.
- **Read back the full Summary**: total trades, longs/shorts, net profit, gross profit, gross loss,
  **commission**, profit factor, max drawdown, total slippage, avg trade, largest winner/loser, even trades,
  longs P&L / shorts P&L.
- **Expect (Claude's arithmetic):** trades 1,190 (556 L / 634 S), slippage 1,190, **commission $3,522.40**
  (= 1,190 × $2.96), net = $200,850 − $3,522.40 = **$197,327.60**, gross profit/loss unchanged.
- **STOP conditions:** commission still $0.00; commission ≠ 2.96 × total trades (± $1); total trades ≠ 1,190
  (the bars did not change, so the list must not either — if it did, STOP and read back); slippage ≠ 1,190;
  slippage 48.44 (that is the Stock-row signature — wrong instrument).

### Step C5 — Walkthrough 3.3 / 3.4 readbacks (unchanged from the walkthrough)
- Trades tab: exit names and counts; Qty per trade (expect 1); any duplicate entries; any "ignored"
  messages in the Log; early-close dates present; first 5 and last 5 trades (entry time, exit time, exit
  name, P&L).
- Write all of it down. These are the baseline's evidence rows; the report that unfreezes F3 is built from them.

### Step C6 — Phase 4: save the Analyzer settings as default (walkthrough Phase 4, as written)
- **4.1:** In the Analyzer settings panel, find the template / preset control. **Read back its menu items
  verbatim before clicking anything.**
- **4.2:** Amear chooses, in his own words: **(i)** save under a new template name, or **(ii)** overwrite
  `Praxis Backtest`. Claude does not choose. Any prompt mentioning deleting, removing, replacing, or a
  trading-hours template → STOP.
- **4.3:** Close the Analyzer, reopen it, load the template, read back the fields — they must match C4.

### Step C7 — Instruments readback (READ-ONLY, owed from yesterday; do it last)
- `Tools` → `Instruments` → `NQCONTROW` → Edit. Read back: instrument type, point value, tick size,
  trading hours template, contract months with rollover dates, merge policy. **Cancel.** Expected: Future,
  $20, 0.25, `CME US Index Futures RTH`, 09-25 with rollover 2021-03-01, Do not merge — all currently
  INFERRED/REPORTED, this is the first direct readback.

## 3. Known traps (from the record)
- Function keys may not reach the VM; use on-screen controls.
- License tooltips are advisory on this install; Editor and Analyzer open regardless.
- Empty Log after an action is not evidence of success — readbacks are.
- The 1-minute file is end-stamped Eastern. On the old Stock-row chart the first RTH bar was 09:31; on
  `NQCONTROW` Amear reported a 09:30 bar. **Do not investigate** — it is logged in bead `q36`.

## 4. Out of scope this session
- No run other than C4 (one re-run of 0-S). No 0-H / High-resolution run. No Stock-row diagnostic run.
- No chase of 1,190 vs 1,211. No edit to any trading-hours template. No instrument deletion, no merge or
  rollover changes beyond what Amear already did.
- The three new strategy files stay uninstalled (R-VM-5).

## 5. Bring back to Claude Code
- C1 grid verbatim; C3 grid verbatim after the edit; Sim101 commission binding.
- C4 full settings readback and full Summary; C5 readbacks; C6 menu items, Amear's (i)/(ii) in his words,
  the 4.3 re-open readback; C7 instrument readback.
- Amear's rulings with times; anything on screen that looked wrong.
