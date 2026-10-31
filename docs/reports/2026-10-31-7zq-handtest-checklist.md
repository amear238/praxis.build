# 7zq hand-test checklist — Noise-Area variants (OppBand, Flat1559) + Step 0 control

**Unit:** Praxis_build-7zq, milestone M1 (worker 2). **Date:** 2026-10-31.
**For:** Amear, at the Fusion VM, NinjaTrader 8 (8.1.7.2).

> **Nothing here was compiled or run. Every "expected" line is an INFERRED prediction**, made by
> reading source code on a Mac without NinjaTrader. Your readbacks are the evidence. Where a
> prediction and your screen disagree, your screen wins — write down what you see.

Evidence grades used: OBSERVED (read directly from a file or screen) · INFERRED (reasoned, not seen)
· REPORTED BY AMEAR (you said or read it) · UNVERIFIED (not checked) · CANNOT-DETERMINE-STATICALLY
(only a run can settle it).

**Do the pages in this order:** Step 0 → File A (OppBand) → File B (Flat1559). Step 0 uses only the
base strategy, so do it **before** copying any new file in. NinjaTrader compiles every NinjaScript
file at once, so a broken new file can stop the base from compiling too
(`docs/reference/2026-07-24-nt8-windows-reference.md:130`, from the NT8 Help Guide).

**What this is not.** It is not a backtest report and not the walk-forward. The walk-forward hold
stays. F3 stays FROZEN until a backtest report carries the limitation sentence (DECISION_LOG
`2026-10-31T10:10:15Z`). Claude writes that report from your Step 0 numbers.

---

## Step 0 — Standard vs High fill-resolution control (base strategy only)

**Why:** your ruling R-F3-1, DECISION_LOG `2026-10-30T23:23:00Z` (bead `Praxis_build-zyd`, open for this
run): run the run-4 setup twice, changing only `Order fill resolution` (Standard, then High), and
compare the trade lists. If they are identical, (c) becomes OBSERVED and F3 moves forward by your edit.
If they differ, the void clause fires and (c) is re-decided cold.

> **Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.**

(That is the approved limitation sentence, R-F3-3. Every backtest report carries it.)

**0.1 — FIRST: check the trading-hours template.** In the Strategy Analyzer, `Trading hours` must
read **`CME US Index Futures RTH`**. Run 3 was ruled INVALID because it was set to `CME FX Futures RTH`
(DECISION_LOG `2026-10-30T22:22:00Z`, WHO: amear). The saved "Praxis Backtest" template carried the
wrong value before you re-saved it, so look at the field. Don't trust the template.

**0.2 — Set every field to run 4.** These are REPORTED BY AMEAR. Source:
`docs/reports/2026-10-28-voice-session-notes.md` :33 (settings), :32 (commission template), :48 (run-3
screenshot fields), :52 (run 4 = run 3 except trading hours). That file is untracked in git. The same
values are in DECISION_LOG `2026-10-30T22:17:00Z` (run-3 screenshot) and `2026-10-30T22:22:00Z` (run 4:
"nothing else changed").

| Field | Run-4 value | Tick when set |
|---|---|---|
| Strategy | PraxisNoiseAreaBreakout | ☐ |
| Instrument | NQCONT | ☐ |
| Price based on | Last | ☐ |
| Type / Value | Minute / 1 | ☐ |
| Start → End | 2021-03-08 → 2026-07-17 | ☐ |
| Trading hours | CME US Index Futures RTH | ☐ |
| Exit mode | BandOrVWAP | ☐ |
| Contracts | 1 | ☐ |
| Include commission | ✓ (template PRAXIS, $1.48/side) | ☐ |
| Slippage | 2 | ☐ |
| Order fill resolution | **Standard** (run 0-S) / **High** (run 0-H) | ☐ |
| Exit on session close | ✓ | ☐ |
| Time in force | DAY | ☐ |

**0.3 — Run 0-S (Standard).** Click Run. This run should reproduce run 4 exactly (INFERRED: same file,
same settings, same data). Run-4 baseline (REPORTED BY AMEAR, notes :53): **1,211 trades (584 L / 627 S)
· net $3,136.84 · PF 1.08 · max DD −$4,108.84 · total slippage 48.44.**
**If 0-S does not match run 4, stop.** Some setting or the data differs from run 4. Write down which
fields you re-checked.

**0.4 — Run 0-H (High).** Change **only** `Order fill resolution` to `High`. Before you click Run,
write down exactly what NinjaTrader shows:
- Extra fields? A research note says High adds a second, finer price series used only for fills, picked
  by a type and value (finest is 1 tick). It also says High asks the data provider for that data
  (`docs/reports/2026-08-07-f3-fill-resolution-research-UNGRADED.md:45-55`). That file is **ungraded
  input, not a finding**. What 8.1.7.2 actually shows is UNVERIFIED.
- What happens when no tick data exists is UNVERIFIED (same file, :61-64).
- **Do not pick a value for any extra field on my say-so.** What to set is your call (NEEDS AMEAR 4).
  Write down the default it shows and the value you used.
- Any error, warning, or request for data? Write it down word for word. Under the void clause, "NT8
  errors or demands a secondary series rather than falling back silently" voids the assumption
  (D-2026-10-30-A, quoting DECISION_LOG `2026-08-29T00:10:00Z`). Whether this run is the trigger is
  your call.

Then click Run.

**0.5 — Read back both runs.**

| Readback | Run 4 (reported) | 0-S Standard | 0-H High |
|---|---|---|---|
| Total trades | 1,211 | ____ | ____ |
| Long / Short | 584 / 627 | ____ / ____ | ____ / ____ |
| Net profit | $3,136.84 | ____ | ____ |
| Profit factor | 1.08 | ____ | ____ |
| Max drawdown | −$4,108.84 | ____ | ____ |
| Total slippage | 48.44 | ____ | ____ |
| High: extra fields shown / value used | — | — | ____ |
| High: any error / warning / data request (verbatim) | — | — | ____ |

**Trade lists.** Your ruling compares trade lists, not just totals. Matching totals are necessary but
not proof. On the Trades tab, write down the first 5 and last 5 trades of each run (entry time, exit
time, exit name, profit). If the grid lets you export it (right-click; UNVERIFIED for this grid),
export both, and Claude can diff all rows on the Mac.

| # | 0-S entry time · exit time · exit name · profit | 0-H entry time · exit time · exit name · profit |
|---|---|---|
| first 1–5 | ____ | ____ |
| last 1–5 | ____ | ____ |

**Optional, same 0-S run (3gm readbacks, which settle the base's open questions).** The 3gm report's
wording names run 2/run 3 (`docs/reports/2026-10-30-3gm-fidelity-check.md:849-854`). Run 3 is INVALID,
so 0-S is the valid run to read them on:
- **R1 (16:00 exits):** count the exit-name column (FlatEOD / Exit on session close / XL / XS / Close
  position / other). For each end-of-day row, read the exit time (16:00 or 09:31) and whether the entry
  date equals the exit date. *These numbers are the baseline File B is compared against.*
- **R2 (reversals):** any Qty > 1. Any two exit rows with the same timestamp. "Ignored" order messages
  in the Log tab.
- **R4 (template hours):** `Tools > Trading Hours > CME US Index Futures RTH`. Write down the printed
  session hours and the holiday / early-close rows.
- **R6 (early-close days):** trades entered on an early-close date from R4. For each, write down the
  exit name, exit date and exit time.

---

## File A — `PraxisNoiseAreaBreakout_OppBand.cs`

**What changed vs the base (base unchanged at 719ab11):** in `OppBand` mode only, the trailing stop is
now the **opposite** band: a long's stop is the Lower band, a short's stop is the Upper band. The base
used the same-side band (base lines 209/217). The 3gm check graded that a DEVIATION (R14), because the
spec's base model is "Stop @ Opp. Band" (spec L38/L49/L59; paper Table 1). In this file `Exit mode`
**defaults to OppBand**. The BandOrVWAP branch is unchanged, including its `vwapCumVol == 0` fallback
(same-side band): the OppBand fallback is guarded by `ExitMode == OppBand` (OBSERVED in the source; not
compiled).

**A.1 — Install.** Copy the file into `Documents\NinjaTrader 8\bin\Custom\Strategies\`. **Keep
`PraxisNoiseAreaBreakout.cs` in that folder.** The variant borrows the base's `PraxisNoiseExitMode` type
and does not declare its own. Declaring it twice would be a duplicate-type compile error (INFERRED).

**A.2 — Compile.** Open `New > NinjaScript Editor` and press **F5**.
- Clean (no error rows, strategy appears in the list): tick ☐.
- **If F5 reports `CS0101`, or "type or namespace … `PraxisNoiseExitMode` … could not be found", stop.**
  Write down the exact error text, file name, line and column. Don't edit anything.
- Any other error: write down the same four things. Then, to get the base compiling again, move
  `PraxisNoiseAreaBreakout_OppBand.cs` out of the folder and F5 again (INFERRED, because NT8 compiles
  every file together).

Error text (if any): ______________________________________________

**A.3 — Settings.** Same as run 4 (Step 0 table, Standard) except:
- Strategy = **PraxisNoiseAreaBreakout_OppBand**.
- **Exit mode: confirm it shows `OppBand` by default.** Shows: ____ (it should; INFERRED from the
  design). Leave it on OppBand. Choosing a new strategy may reset fields to defaults (UNVERIFIED), so
  re-check every field in the Step 0 table.

**A.4 — EXPECTED (all INFERRED, direction vs run 4 only; size unknown).**
- A long now exits at `Close <= Lower`, and the long reverses to short at `Close < Lower` (a short
  exits at `Close >= Upper` and reverses to long at `Close > Upper`). These are almost the
  same condition, so OppBand becomes **"reverse, or hold to 16:00"**. A plain exit to flat happens only
  when the close lands exactly on the band.
- So: **very few or no XL / XS exits that are not followed by an opposite entry at the same time**;
  **longer average holds**; **more trades ending at end of day** (FlatEOD / session close).
- **Trade count probably lower than run 4's 1,211** (direction INFERRED; magnitude unknown). The spec's
  summary of the paper reports 1.3 trades/day with the opposite-band stop vs 1.8 with the VWAP stop
  (spec L38, Table 4 p.16; the paper's own data, not an NQ prediction).
- Net, PF and drawdown: no prediction.
- **Same-bar exit + reversal (CANNOT-DETERMINE-STATICALLY, 3gm table rows R12/R21; reversal readback
  = 3gm readback R2 (NEEDS AMEAR, `docs/reports/2026-10-30-3gm-fidelity-check.md:850`)):** at a reversal stamp the
  code sends both an exit (XL/XS) and an opposite entry. How NT8 resolves that pair can only be seen in
  a run.

**A.5 — WHAT TO READ BACK.**

| Readback | Run 4 (reported) | OppBand |
|---|---|---|
| Total trades | 1,211 | ____ |
| Long / Short | 584 / 627 | ____ / ____ |
| Net profit | $3,136.84 | ____ |
| Profit factor | 1.08 | ____ |
| Max drawdown | −$4,108.84 | ____ |
| Total slippage | 48.44 | ____ |
| Exit-name count: XL / XS / Close position / FlatEOD / Exit on session close / other | — | ____ |
| XL/XS rows with **no** opposite entry at the same timestamp | — | ____ |
| Rows with Qty > 1 | — | ____ |
| Two exit rows at one timestamp (count) | — | ____ |
| "Ignored" order messages in the Log tab (count + one example verbatim) | — | ____ |
| On reversal bars, is the closing exit named XL/XS or "Close position"? | — | ____ |
| End-of-day rows: exit time 16:00 or 09:31? entry date = exit date? | — | ____ |

**A.6 — Optional control (worth doing).** Same file, set `Exit mode` = **BandOrVWAP**, run again.
**Expected: identical to run 4 / your 0-S run, number for number** (INFERRED; the BandOrVWAP branch is
unchanged). If it differs, the variant changed more than the OppBand branch. **Stop and report the
numbers.**

| Control readback | 0-S (base) | OppBand file, ExitMode = BandOrVWAP |
|---|---|---|
| Trades / L / S | ____ | ____ |
| Net · PF · Max DD · Total slippage | ____ | ____ |

---

## File B — `PraxisNoiseAreaBreakout_Flat1559.cs`

> **This variant does NOT decide rubric F2 (FROZEN). The governing flat time stays 16:00 ET.** It only
> changes **when the exit order is submitted** inside the backtest, so the fill lands the same day.
> **Consequence:** the exit fills at the Open of the 16:00-stamped bar (the first trade after ~15:59:00,
> INFERRED), one minute earlier in price than a 16:00:00 close; the position is still flat by 16:00 ET.

**What changed vs the base (base unchanged at 719ab11):** the flatten decision now fires on the
**15:59-stamped bar** (`mod >= 959`) instead of the 16:00 bar (`mod >= 960`). The managed market exit
should then fill at the **16:00 bar's open, same day** (INFERRED). Why: the 3gm check could not say how
the base's 16:00 exit fills (D2(c), scenarios S1–S5). Its order may only have a "next bar" at the next
day's 09:31. `Exit mode` default is unchanged (**BandOrVWAP**).

**B.1 — Install.** Copy the file into `Documents\NinjaTrader 8\bin\Custom\Strategies\`. **Keep
`PraxisNoiseAreaBreakout.cs` in place** (same reason as A.1: it borrows `PraxisNoiseExitMode`).

**B.2 — Compile.** F5. Same rules as A.2: on `CS0101` or "`PraxisNoiseExitMode` could not be found",
**stop and report the exact error** (text, file, line, column). For any other error, report it, then
move the file out and F5 again.

Error text (if any): ______________________________________________

**B.3 — Settings.** Same as run 4 (Step 0 table, Standard) except Strategy =
**PraxisNoiseAreaBreakout_Flat1559**. Check `Exit mode` = BandOrVWAP. Re-check every field.

**B.4 — EXPECTED (all INFERRED, vs run 4).**
- End-of-day exits are named **FlatEOD** with **exit date = entry date**. The grid will probably show
  exit time 16:00 (the fill bar's stamp), but that time cannot show *which price* was used. The fill is
  predicted at the **Open** of the 16:00-stamped bar, i.e. the first trade after ~15:59:00 (INFERRED),
  not a 16:00:00 close. **The exit-price readback in B.5 is what tests this.** If the grid stamps them
  15:59 instead, write that down: it is not a failure. A failure is a 09:31 exit or an exit date later
  than the entry date.
- **No overnight rows. No "Exit on session close" rows on normal days.**
- **Predicted trade count (INFERRED, not a fact): 1,211**, because the entry code is unchanged: the last
  checkpoint is still 15:30, and 15:59 is not a checkpoint. **Caveat:** if the base carried positions
  overnight (3gm S2/S3) or produced an extra session-close row (S4), next-morning entries and reversals
  can differ, so the count may differ from 1,211. A carried position changes the next day's entries.
  Your R1 readback on 0-S tells you which case applies.
- Net, PF, drawdown: different **only through end-of-day exit prices**. The direction is unknown. It
  depends on how run 4's 16:00 exits actually filled (R1).
- If a day has no 15:59 bar, the 16:00 bar still triggers the flatten, as in the base.
- **Early-close days** (session ends before 15:59 ET): the variant's **decision logic on that day is
  identical to the base**. The position/state carried into that day can differ, because earlier days
  flattened differently (INFERRED). There is no explicit flatten; only the session-close backstop acts.
  An entry is possible on a last bar stamped :00/:30 (3gm :733/:842, as corrected at :1224; R6). A
  session-aware close (SessionIterator / ActualSessionEnd) was not used: no NT8 documentation of
  SessionIterator behaviour for this use was found; NT-shipped source on disk uses it, but its
  behaviour here is UNVERIFIED. So 15:59 is hard-coded.

**B.5 — WHAT TO READ BACK.**

| Readback | Run 4 / 0-S | Flat1559 |
|---|---|---|
| Total trades | 1,211 / ____ | ____ |
| Long / Short | 584 / 627 | ____ / ____ |
| Net profit | $3,136.84 | ____ |
| Profit factor | 1.08 | ____ |
| Max drawdown | −$4,108.84 | ____ |
| Total slippage | 48.44 | ____ |
| Exit-name count: FlatEOD / Exit on session close / XL / XS / Close position / other | (R1) ____ | ____ |
| End-of-day exit time seen (16:00 / 15:59 / 09:31 / other) | (R1) ____ | ____ |
| Rows with exit date ≠ entry date | (R1) ____ | ____ |
| First 5 trades: entry times match 0-S? (Y/N; first mismatch date) | — | ____ |
| R6: early-close-date rows: exit name · date · time | (R6) ____ | ____ |

**B.5a — Exit-price check (3 FlatEOD rows).** Pick 3 FlatEOD rows from the Flat1559 run. For each, read
the **exit price** from the Trades tab. Then on the chart, hover the **16:00-stamped bar** of that day and
read its **Open** and **Close** from the Data Box. Slippage is 2 ticks, so a sell exit is expected about
2 ticks below the price it filled against, and a buy exit about 2 ticks above (INFERRED). Write down
which one the exit price sits next to: the 16:00 bar's Open (~15:59 price, the prediction) or its Close
(the 16:00:00 price).

| Row | Date | Side (L/S) | Exit price | 16:00 bar Open | 16:00 bar Close | Nearer Open or Close (after 2 ticks)? |
|---|---|---|---|---|---|---|
| 1 | ____ | ____ | ____ | ____ | ____ | ____ |
| 2 | ____ | ____ | ____ | ____ | ____ | ____ |
| 3 | ____ | ____ | ____ | ____ | ____ | ____ |

---

## NEEDS AMEAR

These are your questions. Nothing here answers them.

1. **3gm Q2 — OppBand meaning.** Should the replication's OppBand mean the paper's opposite band? The
   options in 3gm (`docs/reports/2026-10-30-3gm-fidelity-check.md:858-861`): change base lines 209/217;
   keep it and rename the mode; drop it. File A is test material only. **It does not decide Q2.**
2. **Early-close handling.** Once you have read the template's early-close rows (R4) and the
   early-close trades (R6): should a session-aware flat be built (flatten on the session's actual last
   bar, not a fixed 15:59/16:00)? Should it go in the base, in Flat1559, or nowhere?
3. **3gm C3 — how the 16:00 flat is realised.** If File B shows same-day 16:00 fills: does the
   15:59-decision timing become how the replication realises the 16:00 flat (adopted into the base), or
   stay a test variant? 3gm notes this changes "act at the stamp" semantics (:866). F2 itself is
   untouched either way.
4. **Step 0 — High's extra fields.** If `High` shows a secondary-series type/value: which value do you
   want? Your ruling held "every other field", but these fields don't exist under Standard. And if NT8
   asks for data or errors: is that the void-clause trigger (D-2026-10-30-A leaves this to you)?
5. **Step 0 — what counts as "identical".** Is a match on totals plus first/last five trades enough, or
   do you want a full row-by-row diff (needs the grid export, UNVERIFIED) before (c) is called OBSERVED?
6. **Flat1559 — fill price of the 16:00 flat.** File B's exit fills at the Open of the 16:00-stamped
   bar, which is about a 15:59 price (INFERRED; B.5a tests it). Is a fill at the 16:00 bar's Open
   acceptable as the backtest realisation of the 16:00 flat, or do you want another mechanism (for
   example a finer secondary series)? Unanswered. No option is recommended here.
