# Handoff to the voice agent — 2026-10-31, Future-row loading walkthrough on Fusion

**From:** praxis-master (Claude Code, third session of 2026-10-31; written 17:05Z at Amear's request).
**For:** the voice agent working with Amear at the Fusion VM, and for Amear himself.
**What this is:** the narration brief for a pre-registered, twice-audited hand walkthrough. The walkthrough text is
appended below this brief in the clipboard copy, byte-for-byte from `main` (`head -n 257` of
`docs/reports/2026-10-31-a9d-walkthrough-future-row.md` at commit `d2ff631`; its Evidence appendix is omitted
from the paste, not from the repo). **The walkthrough is the authority. This brief only tells you how to use it.**

Evidence grades: OBSERVED (read from a file or a screen) · INFERRED (reasoned) · REPORTED BY AMEAR ·
UNVERIFIED · CANNOT-DETERMINE-STATICALLY. Fusion has never been read by Claude: every expectation in the
walkthrough is INFERRED unless marked otherwise. **Amear's screen wins.** Write down what it shows, especially
where it disagrees with an Expect line.

**Where to write the session's results:** a new file `docs/reports/2026-10-31-voice-session-notes-2.md`, same
shape as `docs/reports/2026-10-31-voice-session-notes.md` (rulings = Amear's; screen values = REPORTED BY
AMEAR; Claude's arithmetic labelled as Claude's). Claude Code reads it first next session and appends each
readback to the ledger from it.

---

## 0. What exists now (repo state, OBSERVED 17:00:45Z)

- `main` = `origin/main` = **`8bfa544`**. Commits today after the park: `29c3e13` (o78 report, fast-forward
  merge), `d2ff631` (a9d merge: plan, walkthrough, research, adversarial, 6 MANIFEST rows), `a91a636` (the two
  voice-session files from this morning), then three ledger commits `2665523` / `6d1acb0` / `8bfa544` (same
  message; the Step 5 command ran three times, each picking up one new ledger row — harmless).
- **Both parked beads were resumed by Amear's ruling, not re-dispatched** (DECISION_LOG `16:50:30Z`):
  - `Praxis_build-o78` — accepted as parked, **CLOSED** 17:02Z. Its answers: no long/short code asymmetry in
    `PraxisNoiseAreaBreakout.cs`; the run-3/4 dollars and slippage were at $1/pt, 0.01 tick, because the
    Analyzer ran the Stock-typed `NQCONT` row (confirmed on Amear's screen 14:29–14:52Z).
  - `Praxis_build-a9d` — accepted as parked, **OPEN, executing**. Its product is the walkthrough below.
- **Standing rulings from this morning (14:59:37Z, R-VM-1..6):** Future row only; load it first; 0-S on it is the
  new baseline; save the Analyzer settings as default afterwards; **no other backtests until then**; the three
  new strategy files stay uninstalled; `D-2026-10-30-A` (Standard resolution, 2 ticks/side) stands.
- **Frozen, untouched:** F1, F2, F4. F3: assumption committed, still FROZEN until a backtest report carries the
  limitation sentence — the walkthrough is **not** that report.

## 1. The finding the walkthrough acts on (grades as marked)

- Fusion holds two `NQCONT` instrument rows (REPORTED BY AMEAR, screenshots this morning): a **Stock** row
  ($1/pt, 0.01 tick, `US Equities RTH`) and a **Future** row ($20/pt, 0.25 tick, `CME US Index Futures RTH`,
  one contract month shown as `NQCONT SEP25`).
- NT8's Import has no instrument field; it files bars under the instrument named by the file name. The file was
  `NQCONT.Last.txt`, so the bars went under plain `NQCONT` — the Stock row's folder (OBSERVED on the rescued
  old install: `db/minute/NQCONT` 1,710 files, `NQCONT 09-25` empty; INFERRED for Fusion — Phase 0 tests it).
- The fix the walkthrough takes, Phase 1: import a **copy** of the file named `NQCONT 09-25.Last.txt` so the
  bars land under the Future's contract month, then chart `NQCONT SEP25` and compare two pre-registered bars
  against the file. Nothing is deleted. The original file is never renamed or moved.

## 2. How to narrate it (the rules the audits graded)

1. **One step per exchange.** Read the step's Path, then ask for the Read back. Give the Expect and Falsifier
   only after Amear has read the screen, or he will read the expectation instead of the screen.
2. **Every STOP is literal.** On a STOP: Amear does nothing further in NT8, reads back what is on screen, and
   the session returns to Claude Code with the notes file. **A STOP is a result, not a failure.** Do not reason
   past one, do not offer a workaround, do not soften it. Two earlier walkthroughs failed audit for exactly
   that (HANDOFF.md, 2026-10-20 card: "a rewrite meant to fix one thing silently lost or degraded another").
3. **Phase 0 is read-only.** Every dialog closes with Cancel or the window X, never OK/Save. No Delete control
   is clicked anywhere in this document.
4. **GATE 1 (start of Phase 1) needs Amear's words, in writing, before step 1.1:** "Phase 0 passed with no STOP;
   I approve importing a copy named `NQCONT 09-25.Last.txt`; the import settings will be Format ___ / Data Type
   ___ / Time Zone ___, identical to the original `NQCONT` import." **The three settings are not on disk
   anywhere; Claude does not supply them.** If Amear cannot state them, Phase 1 does not start (that is a STOP
   in 0.7). The only on-disk hint is the old-install instruction set — Format `NinjaTrader (end of bar
   timestamps)`, Data Type `Last`, Time Zone `US Eastern` — which is what he was told to use on 2026-08-29, not
   a record of what he did.
5. **Phase 2 is never a default.** It exists only if Phase 1 STOPs, and each option needs its own separate
   written confirmation from Amear before anything is clicked. Option (c) can delete data folders. Do not
   recommend one.
6. **Phase 3 is one run — 0-S on `NQCONT SEP25` with the run-4 settings.** No other run. Record every field read
   back before Run. The Stock-row signature is total slippage **48.44** (= 1,211 × 4 × 0.01); if it appears
   again, STOP before Phase 4. The Future-row expectation is a multiple of 302.75 (= 1,211 × 0.25) if NT8
   reports slippage in points — unit UNVERIFIED, so write the number and the unit shown, nothing else.
7. **Phase 4 (save as default) is Amear's choice between (i) a new template name and (ii) overwriting
   "Praxis Backtest".** Claude does not choose. Read the control's menu items back verbatim before anything is
   clicked; any prompt that mentions deleting, removing, replacing or a trading-hours template is a STOP.
8. **No trading-hours template is edited, ever (F2 FROZEN).** The walkthrough only *selects*
   `CME US Index Futures RTH`.
9. **Run description to carry verbatim** into the 0-S run (F3 limitation sentence): *"Fills are optimistic;
   Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."*

## 3. Known traps on this VM (from the record, not new)

- Function keys may not reach the VM (F5 did not register on 2026-08-29); use on-screen controls.
- License tooltips ("upgrade to a Lease or Lifetime license") are advisory on this install — Editor and
  Analyzer open regardless. Do not conclude a license block from a tooltip.
- An empty Log after an import is **not** evidence of success (the old install wrote 1,710 files with no Log
  line). The success readback is the folder listing in 1.4 and the chart in 1.5.
- The 1-minute file is end-stamped Eastern; the first RTH bar is **09:31**, not 09:30. The two spot-check bars
  in the walkthrough are `20210308 100000` (O 15968.75, V 8) and `20260717 093100` (O 28605.25, V 4963).

## 4. What to bring back to Claude Code (in the notes file)

- For every step executed: the step number, what was read back (verbatim where the walkthrough says verbatim),
  pass / STOP, and the STOP's readback if any.
- GATE 1 text as Amear wrote it, with the three import settings.
- Phase 3: the full Summary table from step 3.2 with the "Amear reads" column filled; the 3.3 readbacks (R1 exit
  names and counts, R2 Qty/duplicates/"ignored" messages, R6 early-close dates; first 5 and last 5 trades).
- Phase 4: the template control's menu items verbatim; Amear's choice (i)/(ii) in his words; the 4.3 re-open
  readback.
- Any rulings Amear makes, in his words, with the time.
- Anything on screen that was not asked for but looked wrong.
- Screenshots stay with the voice agent; transcribe the values.

## 5. What is NOT in scope for this session

- No run other than 0-S on `NQCONT SEP25`. The 0-H (High resolution) control on the Future row is a later
  dispatch. The three new strategy files (`_OppBand`, `_Flat1559`, `PraxisLastHalfHourMomentum`) stay
  uninstalled (R-VM-5).
- No instrument deletion, no Stock-row removal, no merge-policy change unless a Phase 2 option is separately
  confirmed in writing by Amear.
- No decision on F1/F2/F4; no edit to `specs/SPEC_RUBRIC.md`.
- Owed by Claude Code, not by this session: the MANIFEST row for this handoff and for the notes-2 file (the
  master's write guard blocks MANIFEST; text in DECISION_LOG `2026-10-31T17:05:39Z`); the return handoff for the
  Claude.ai channel once the baseline lands (R-VM ruling 4).

---

*The walkthrough follows in the clipboard copy. Its first line is
`# Praxis_build-a9d — walkthrough: load 1-minute history onto the Future NQCONT row, re-baseline 0-S, save as default`.
If that line is not directly below this one, the paste was cut: ask Amear to paste
`docs/reports/2026-10-31-a9d-walkthrough-future-row.md` from the repo before continuing.*
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
