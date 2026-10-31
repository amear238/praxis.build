# Handoff to the voice agent — 2026-10-31 backtest session on Fusion

**From:** praxis-master (Claude Code session ended 2026-10-31 ~14:00Z under the park rule).
**For:** the voice agent working with Amear at the Fusion VM, and for Amear himself.
**Written by the master from the files on disk; nothing here was compiled or run.** Every prediction
below is INFERRED. **Amear's screen wins.** Write down what it shows, especially where it disagrees.

Evidence grades: OBSERVED (read from a file or a screen) · INFERRED (reasoned) · REPORTED BY AMEAR ·
UNVERIFIED · CANNOT-DETERMINE-STATICALLY (only a run settles it).

**Where to write the session's results:** a new file `docs/reports/2026-10-31-voice-session-notes.md`,
same shape as `docs/reports/2026-10-28-voice-session-notes.md` (rulings = Amear's; screen values =
REPORTED BY AMEAR; Claude's arithmetic labelled as Claude's). The next Claude Code session reads it first.

---

## 0. What exists now (repo state, OBSERVED at 14:00Z)

- `main` = `origin/main` = **`0ced412`**. Four commits landed today, all typed by Amear:
  `4ec75ea` (F3 artifact: DECISIONS `D-2026-10-30-A`, cost model v1.1.0), `fab2855` (ledger flush),
  `0ced412` (the three strategy files below + `D-2026-10-31-A` + MANIFEST rows), and the park commit
  `29c3e13` on branch `parked/Praxis_build-o78` (not on `main`).
- **Three new strategy files, on `main`, in `ninjascript/`:**
  1. `PraxisNoiseAreaBreakout_OppBand.cs` — the base with the OppBand stop corrected to the paper's
     opposite band; `Exit mode` defaults to **OppBand**.
  2. `PraxisNoiseAreaBreakout_Flat1559.cs` — the base with the end-of-day flat submitted on the 15:59
     bar so it fills the same day (at the 16:00 bar's open ≈ 15:59 price).
  3. `PraxisLastHalfHourMomentum.cs` — a new strategy (Baltussen, Da, Lammers & Martens 2021, *JFE*):
     one trade per day, entered at 15:30, flat at 15:59. Research-only (it trades inside breaker #5's
     window).
  The base `PraxisNoiseAreaBreakout.cs` is **unchanged** (sha `35393823…2265`, commit 719ab11).
- **Checklists** (plain language, one page each): `docs/reports/2026-10-31-7zq-handtest-checklist.md`
  (Step 0 control + files 1 and 2) and `docs/reports/2026-10-31-7zq-m2-handtest-checklist.md` (file 3).
  This handoff condenses them; the checklists have the blank tables to fill.
- **Status of every file: WRITTEN. Not compiled, not tested.** The VM compile is step 1.

---

## 1. ⚠️ BEFORE ANY RUN — the instrument question (new today, changes the meaning of every number)

The `o78` investigation (parked — see §9) found, and two auditors reproduced:

- NT8's "Total slippage" row equals **trades × 4 × 0.01** exactly in both runs so far
  (run 3: 1,075 → 43.00; run 4: 1,211 → 48.44; by side 522 → 20.88, 553 → 22.12).
- The old Parallels NT8 database (rescued copy on the Mac) holds **two** `NQCONT` instrument rows:
  a **Future** at $20/point, 0.25 tick — and a second one, instrument type 1 (Stock, INFERRED),
  at **$1/point, 0.01 tick, trading hours `US Equities RTH`**.
- All five extreme trades in runs 3/4 (largest/smallest winners and losers) fit $1/point on a 0.25
  price grid and do **not** fit $20/point. Run 4's largest winner, $1,792.50, equals one import-file
  trade to the cent: 2025-04-09, long, entry 18,691.25 at 12:31 → exit 20,486.75 at 16:00, minus
  $2.96 commission and $0.04 slippage (0.02/side).

**If Fusion's Analyzer ran the Stock-typed row:** every dollar figure so far is 1/20 of real NQ money
(run 4's $3,136.84 net would be ≈ $62.7k at $20/pt before re-costing); the slippage actually simulated
was 0.02 points per side, **not** the locked 2 ticks (0.50 points); commission stayed $2.96. The F3
cost model and `D-2026-10-30-A` would then need Amear's cold re-decision under its own void clause.
**This is INFERRED. Fusion has not been read.** Three readbacks settle it:

**R-I1. `Tools > Instruments`, filter `NQCONT` (and `NQ`).** For **every** row: Instrument type
(Future / Stock / …), Tick size, Point value, Trading hours template, Expiry. Then open the Strategy
Analyzer's instrument field and read which one it resolves. Write all of it down verbatim.
- Expect to find out whether the Fusion install carries the $1/pt row at all.

**R-I2. `Tools > Trading Hours > CME US Index Futures RTH`.** Time zone, and every session's begin and
end time; holiday / early-close rows if listed. (The rescued Parallels copy of this template reads
**Eastern Standard Time, Mon–Fri 08:30–16:00** — if Fusion's matches, the strategy anchors its session
at 08:31, not 09:30. Amear earlier reported seeing the 16:00 bar followed by 9:31 on the chart, which
argues the other way. Both are on record; the field decides.)

**R-I3. Run 4's largest winner, Trades tab.** Entry price:
- `18,691.27` ⇒ $1/pt, 0.01 tick, 2 ticks of slippage applied (the INFERRED reading);
- `18,691.75` ⇒ 0.25 tick with 2 ticks applied (the $20/pt future);
- `18,691.25` ⇒ no slippage applied.
Also: exit price, exit name (`FlatEOD` or "Exit on session close"), and whether Profit =
(exit − entry) × 1 − 2.96 or × 20 − 2.96.

**Nothing is decided on this.** If the Stock-typed row is what ran, the choice of what to do (switch the
Analyzer to the Future row and re-run; re-read the cost model) is Amear's. The voice agent records; it
does not rule.

---

## 2. Install order

1. **Do Step 0 (§3) first, with only the base file installed** — it is the base being measured, and
   NT8 compiles every file together, so a broken new file could stop the base compiling.
2. Then copy all three new files from `/Volumes/Sensidine/Praxis.build/ninjascript/` into
   `Documents\NinjaTrader 8\bin\Custom\Strategies\` on the VM, the same way the base was copied
   (Praxis.build → VM desktop → Strategies folder). **Leave the base file there** — files 1 and 2 use
   the base's `PraxisNoiseExitMode` type and do not declare their own.
3. `New > NinjaScript Editor`, **F5 once**. Clean = no error rows, three new strategies in the list.
4. **If F5 fails: STOP. Do not edit on the VM.** Write down the exact error text, code (e.g. `CS0101`,
   `CS0103`), file, line, column. Then move the failing file out of the folder and F5 again so the
   others compile. Report it; the fix is a Claude Code dispatch.
   - `CS0101` or "`PraxisNoiseExitMode` could not be found" on file 1 or 2 means the shared-enum
     assumption was wrong — that is the one error predicted as possible.
5. Hashes to confirm the copies, if the VM can hash (optional): OppBand `42df06fa…`, Flat1559
   `7cb71320…`, LastHalfHour `9f4953a8…` (first 8 hex of sha256; full values in DECISION_LOG
   `2026-10-31T11:49:28Z`). Files start with `#region`, no BOM.

---

## 3. Run settings — "run 4" (every run uses these unless a line says otherwise)

Confirm **every** field by eye each time; choosing a new strategy may reset fields (UNVERIFIED).

| Field | Value |
|---|---|
| Instrument · Price based on · Type / Value | NQCONT · Last · Minute / 1 |
| Start → End | 2021-03-08 → 2026-07-17 |
| **Trading hours** | **CME US Index Futures RTH** — look at the field; run 3 was INVALID on `CME FX Futures RTH` |
| Contracts | 1 |
| Include commission | ✓, template PRAXIS ($1.48/side = $2.96 round trip) |
| Slippage | 2 |
| Order fill resolution | Standard (High only in run 0-H) |
| Exit on session close | ✓ |
| Time in force | DAY |
| Exit mode (files base/1/2 only) | BandOrVWAP for base and file 2; **OppBand** for file 1 (its default) |

Run-4 baseline to compare against (REPORTED BY AMEAR): **1,211 trades (584 L / 627 S) · net $3,136.84 ·
gross profit $41,447.47 · gross loss −$38,310.63 · commission $3,584.56 · PF 1.08 · max DD −$4,108.84 ·
largest winner $1,792.50 · total slippage 48.44.**

---

## 4. Step 0 — Standard vs High control (base strategy only; Amear's ruling R-F3-1)

Purpose: `D-2026-10-30-A` is CONDITIONAL. Run the base twice, changing only `Order fill resolution`.
Identical trade lists ⇒ the Standard-resolution assumption becomes OBSERVED. Different ⇒ the void
clause fires and Amear re-decides cold. The approved limitation sentence every backtest report carries:
**"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."**

- **Run 0-S** (Standard): should reproduce run 4 exactly. If it does not, stop and list which fields
  were re-checked — something differs from run 4.
- **Run 0-H** (High): change only the resolution. **Before clicking Run**, write down exactly what NT8
  shows: any extra fields (a secondary series type/value), their defaults, any warning, error, or data
  request — verbatim. **Do not choose a value for an extra field on Claude's say-so** (open question
  NEEDS AMEAR 4). If NT8 errors or demands a secondary series rather than falling back silently, that
  is the void-clause wording; whether it triggers is Amear's call.
- **Read back both runs:** total trades, L/S, net, PF, max DD, total slippage; plus the **first 5 and
  last 5 trades** of each (entry time, exit time, exit name, profit). If the grid exports (right-click;
  UNVERIFIED), export both — Claude Code diffs rows on the Mac. Totals matching is necessary, not proof
  (open question NEEDS AMEAR 5: what counts as "identical").
- **On the 0-S run, also read (these settle the base's own open items):**
  - **R1** exit names counted (FlatEOD / Exit on session close / XL / XS / Close position / other);
    for end-of-day rows, exit time (16:00 or 09:31?) and whether exit date = entry date.
  - **R2** any Qty > 1; two exit rows with one timestamp; "ignored" order messages in the Log tab.
  - **R6** trades entered on early-close dates (from the template, R-I2): exit name, date, time.

---

## 5. File 1 — `PraxisNoiseAreaBreakout_OppBand`

**What it is.** In OppBand mode the trailing stop is now the **opposite** band (long stops at Lower,
short at Upper). The base used the same-side band — the fidelity check graded that a deviation from
the paper ("Stop @ Opp. Band", Table 1). BandOrVWAP mode is byte-for-byte the base.
**Settings:** run 4 + Strategy = this file; confirm `Exit mode` shows **OppBand**.
**Expected (INFERRED, direction only):** the opposite-band exit and the reversal trigger almost
coincide, so OppBand becomes "reverse, or hold to 16:00": very few XL/XS exits that are not followed by
an opposite entry at the same stamp; longer holds; more end-of-day exits; **probably fewer than 1,211
trades**. No prediction on net/PF/DD. How NT8 resolves a same-bar exit + opposite entry is
CANNOT-DETERMINE-STATICALLY — the readback shows it.
**Read back:** totals (trades, L/S, net, PF, max DD, total slippage); exit-name counts; XL/XS rows with
**no** opposite entry at the same timestamp; Qty > 1 rows; two exits at one timestamp; Log-tab
"ignored" messages (count + one verbatim); on reversal bars, is the closing exit named XL/XS or
"Close position"; end-of-day rows' exit time and date.
**Optional control, worth doing:** same file, `Exit mode` = BandOrVWAP → **expected identical to
run 0-S number for number.** If not, the variant changed more than intended — stop and report.

---

## 6. File 2 — `PraxisNoiseAreaBreakout_Flat1559`

**What it is.** The flatten decision fires on the **15:59** bar instead of the 16:00 bar, so the
market exit should fill at the 16:00 bar's **open** (≈ the 15:59 price), same day. Why: the fidelity
check could not tell how the base's 16:00 exit fills — its "next bar" may be the next morning's 09:31.
Amear ruled (R-7zq-2): test it as built. **It does not decide rubric F2; the governing flat time is
still 16:00 ET.** `Exit mode` default unchanged (BandOrVWAP).
**Expected (INFERRED):** end-of-day exits named **FlatEOD** with exit date = entry date; no overnight
rows; no "Exit on session close" rows on normal days; trade count probably 1,211 (entries unchanged) —
unless the base was carrying positions overnight, in which case counts differ. Net/PF/DD differ only
through end-of-day exit prices; direction unknown. Early-close days: no explicit flatten (hard-coded
15:59), only the session-close backstop — identical to the base on that day.
**Read back:** totals; exit-name counts; end-of-day exit time seen (16:00 / 15:59 / 09:31); rows with
exit date ≠ entry date; do the first 5 entry times match 0-S (Y/N, first mismatch date); early-close
rows (R6). **Exit-price check:** pick 3 FlatEOD rows; read each exit price; on the chart hover that
day's 16:00-stamped bar and read its Open and Close from the Data Box; after allowing 2 ticks of
slippage, is the exit price next to the Open (the prediction) or the Close?

---

## 7. File 3 — `PraxisLastHalfHourMomentum` (new strategy; research-only by ruling R-7zq-4)

**Rule (paper's η(r_ROD)):** at the close of the 15:30 bar, r = Close(15:30) ÷ Close(the most recent
weekday 16:00-stamped bar) − 1. r > 0 → long (`LHMomLong`); otherwise, r = 0 included → short
(`LHMomShort`). Flat on the 15:59 bar (`LHFlat1559`). One trade per weekday session that has a bar in
[15:30, 15:59); no trade on a day without one (early closes); Saturday/Sunday bars ignored; a 13:00
holiday-session close is never used as the previous close. `Contracts` is the only input. Market orders.
**Why this one:** ranked first of three on rule completeness, data fit, independence from the
Noise-Area logic, published NQ evidence, simplicity, zero tunables (shortlist:
`docs/reports/2026-10-31-7zq-m2-shortlist.md`; #2 TORB, #3 Zarattini–Aziz ORB stay as written specs).
Amear ruled: keep #1. The paper is gross of costs, its NQ sample ends 2020-05, so 2021-03 → 2026-07 is
entirely out of sample. Breaker #5 (15:00–18:00 disable) means it can never run live as specified —
hence research-only.
**Settings:** run 4 + Strategy = this file (no Exit mode field).
**Expected (INFERRED):** **≤ 1,304 trades** (1,305 sessions with a 15:30 bar in range, minus the first;
more would mean phantom weekend trades = defect); entries at ~15:31 (fill = 15:31 bar's open); every
exit `LHFlat1559` at the 16:00 bar (fill = its open); hold ≈ 29 minutes; long/short mix leans long
but neither side near 0%; **zero** `LHStaleFlat` and **zero** "Exit on session close" rows (any = defect);
commission ≤ $3,859.84; total slippage ≤ 52.16 on the runs-3/4 pattern. Net: no prediction.
**Read back:** totals (trades, L/S, net, gross profit, gross loss, commission, PF, max DD, total
slippage); exit names counted; exits not at the 16:00 bar (count + first date); entries not at 15:31
(count + first date); one trade's entry fill vs the 15:31 bar's Open and exit fill vs the 16:00 bar's
Open (Data Box); any entry on a day with no 15:30 bar; a regular day's first and last bar stamps on the
chart (expect 09:31 and 16:00 — if 17:00, report it); **defect checks:** any Saturday/Sunday entry;
2024-01-16 (day after MLK): the previous close used should be 2024-01-12's 16:00, not 2024-01-15's
13:00.

---

## 8. Why the short side lost in run 4 — what to read if time allows

The code has **no** long/short asymmetry (seven decision sites mirrored; auditor re-read). So the
cause is market, data, or engine. The falsifying readbacks, from the 0-S run's Trades tab or Summary:
short P&L by year (does it also lose in 2022, a falling year?); % profitable and avg MAE/MFE by side;
avg bars in trade by side; exit-reason split by side (trail XS vs FlatEOD vs reversal). A Trades-tab
export is the best single artifact. Also on record: the import file has 127 Saturday-dated rows
(58 inside 09:31–16:00) — whether Fusion's template excludes them is UNVERIFIED.

---

## 9. What is decided, what is open, what is parked

**Decided by Amear today (do not re-ask):** `[N]` = 2 ticks/side, Standard resolution, CONDITIONAL
with today's control (R-F3-1/2/3); 7zq's S4 ordering accepted (R-7zq-1); Flat1559's 15:59 fill
accepted for testing (R-7zq-2) and extended to file 3 (R-7zq-5); keep #1 as the third file (R-7zq-3);
file 3 is research-only (R-7zq-4); commit composition (R-7zq-6). Run 3 is INVALID; run 4 is the valid
baseline; walk-forward HELD; in-VM automation dropped; Trend box dropped; NT8 update skipped.

**Open and Amear's — record what he says, do not decide:** what OppBand should mean in the base
(3gm Q2); sizing variant (b) vs (c) (3gm Q1); early-close handling; whether the 15:59 timing goes into
the base; High's extra fields and what "identical" means for Step 0; file 3's r = 0 → short reading,
previous-close rule, missing-15:30 fallback, 15:30 reference price, the η(r_ONFH, r_ROD) variant, the
roll convention; whether to clean the Saturday rows; **and everything in §1 if the $1/pt reading
holds, including the F3 void clause.**

**Parked:** `Praxis_build-o78` (the short-side + slippage-unit report) sits on
`parked/Praxis_build-o78` = `29c3e13`, pushed. It failed audit twice on evidence *form* (an unbounded
"no NT8 text on disk" negative, then one mis-quoted command line in the correction); the substance in
§1 and §8 was reproduced by both auditors. The absolute park rule fired and the Code session ended.
**A human resumes it** — Amear rules how, in the next Code session. Read it with
`git show parked/Praxis_build-o78:docs/reports/2026-10-31-o78-short-side-and-slippage-unit.md`.

**Strike counts:** 7zq carries one audit FAIL (corrected, then PASS); o78 is parked at two.

**F-criteria:** F1, F2, F4 FROZEN, untouched. F3: the assumption is committed; it stays FROZEN until a
backtest report carries the limitation sentence — the Step 0 write-up is the first candidate.

**Master errors today, on the record (so the voice agent does not inherit them):** the master told
Amear the .cs files carry a UTF-8 BOM — they do not (`237265` is `#re`, not `efbbbf`); it carried an
unmeasured "103 DLLs" into a brief (39 under the NT8 folder); it wrote an impossible protected-file
check into one brief. All corrected by append in DECISION_LOG.

---

## 10. What to bring back to Claude Code

The notes file (§ top) with, per run: the full Summary values, the readback tables above, exit-name
counts, any verbatim errors/warnings, and any export file paths. Plus the three §1 readbacks first.
Rulings Amear makes at the VM go in the notes as his, dated and timed; the next Code session turns
them into `WHO: amear` ledger rows before acting on them.

Uncommitted on `main` at the handoff: today's ledger rows (`DECISION_LOG.md`, `DISPATCH_LOG.md`,
`HANDOFF.md`, `STATUS.md`) and this file — the next Code session's first commit — plus the 12-path old
carried staged set, untouched.

---

## Corrections appended 2026-10-31 14:59Z (praxis-master; findings relayed from the Claude.ai auditor channel via `2026-10-31-voice-session-notes.md`)

1. **§1, "run 4's $3,136.84 net would be ≈ $62.7k at $20/pt before re-costing" — WRONG and withdrawn.** It multiplied the whole net by 20, including the $3,584.56 commission, which is in dollars and does not scale. No figure in this document or elsewhere depends on it. No replacement is given: the Future-row baseline (ruling R-VM-2) supersedes every Stock-row dollar.
2. **§1 R-I2 omitted a third on-record reading of the RTH template:** 2026-08-29, on screen, **Central time, 08:30–16:00** (DECISION_LOG, session 52/53 rows). So three readings exist — Central 08:30–16:00 (on screen, 08-29), Eastern Standard Time 08:30–16:00 (rescued file), and Amear's 16:00→09:31 bar sequence (reported, 10-30). The 08-29 ledger row also blocks any template change until F2 is ruled.
3. **§3's settings table says only "NQCONT", which does not identify the row.** Fusion has two (`Tools > Instruments`): Stock ($1/pt, 0.01 tick) and Future ($20/pt, 0.25 tick, `NQCONT SEP25`). Amear ruled 14:54Z: **Future row only**; the Stock row is retired as a baseline.
4. The §1 readbacks were done 14:29–14:52Z: the Stock row is confirmed on screen as what runs 3/4/0-S used (REPORTED BY AMEAR). §1 is therefore no longer a hypothesis to test; it is the recorded state. The Future row did not load (`NQCONT ##-##`, "unknown instrument"-family error, exact text not captured).
