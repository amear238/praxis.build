# 7zq M2 — DRAFT addendum to D-2026-10-31-A (third file) + DRAFT MANIFEST rows for M2

- Unit `Praxis_build-7zq`, milestone M2, worker 3. Mode BUILD (docs). Date 2026-10-31.
- Grades: OBSERVED · INFERRED · REPORTED BY AMEAR · UNVERIFIED · SPEC-SILENT.
- The strategy file `ninjascript/PraxisLastHalfHourMomentum.cs` was being written by a parallel worker while this was drafted.
  **This worker did not read it.** Everything said here about the file is the manager's **pinned design**, not an
  observation of the source. Grade: INFERRED until the M2 adversarial worker checks it against the file.
- **Revised by M2 worker 5 (fix) after the worker-4 adversarial review** (`docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md`):
  every sentence below on the file's previous-close, signal-bar and weekend behaviour now matches the revised `.cs` (read by worker 5).

> **NOT APPENDED.** None of this text is in `DECISIONS.md` or `MANIFEST.md` yet. It is a draft for the master, to be
> spliced into the M1 draft `docs/reports/2026-10-31-7zq-decisions-scope.md` (placeholder at its line 43). The rows
> below go into `MANIFEST.md` with M1's rows, on the same schedule: after commit 2 and before any 7zq commit.
> The S4 chain for tonight is DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): *"Run them now and I'll commit in the
> morning."* Same row, third file: *"Build the top-ranked one (Recommended)"*. OBSERVED:
> ```
> $ grep -n "00:46:43" DECISION_LOG.md | cut -c1-300
> 462:- [2026-10-31T10:47:43Z] WHO: praxis-master | WHAT: **7zq M1 AUDIT: PASS. No BLOCKING finding. S1, S2, S4 (narrow: chain traceable, draft-not-appended stated honestly, ordering question left to Amear), S6, S8, F2-claim, F3-sentence all PASS.** Transcribed from the auditor's return (91k tokens, 2
> 465:- [2026-10-31T00:49:35Z] WHO: praxis-master | WHAT: **PUSH VERIFIED; 7zq M1 DISPATCHED.** Amear reported pushing `4d7ca80` ("fc77f36..4d7ca80 main -> main"). Master re-ran after `git fetch -q origin`: `git rev-list --left-right --count origin/main...HEAD` = `0 0`; `git log --oneline -2` = `4d7ca
> 466:- [2026-10-31T00:46:43Z] **WHO: amear** | WHAT: **RULING REVERSED BY AMEAR: "Run them now and I'll commit in the morning."** Supersedes the 00:41:00Z row's item (1) only: `Praxis_build-7zq` (three backtest .cs files) IS dispatched tonight; commits 2 and 3 remain his, in the morning, unchanged. F
> ```
> The 300-character cut ends row 466 before the third-file ruling. The full row (`sed -n 466p DECISION_LOG.md`, OBSERVED) goes on:
> *"Follow-up ruling by AskUserQuestion this turn, third file: **"Build the top-ranked one (Recommended)"** — the research manager
> ranks its shortlist of three with reasons; the build proceeds on #1 tonight; Amear reads the shortlist in the morning and may
> swap, the other two surviving as written specs."* (Rows 462 and 465 match only because they quote that timestamp.)

---

## (a) Replacement text for the placeholder

Placeholder location, OBSERVED:
```
$ grep -n "M2 fills" docs/reports/2026-10-31-7zq-decisions-scope.md
43:- **Third file — one new researched NQ intraday strategy, built in milestone M2:** `[M2 fills: strategy name, source]`. The research manager ranks a shortlist of three; #1 is built; Amear may swap in the morning, and the other two survive as written specs (`2026-10-31T00:46:43Z`).
```

**Replace the backticked token `` `[M2 fills: strategy name, source]` `` with exactly this text:**

> **`PraxisLastHalfHourMomentum`** (`ninjascript/PraxisLastHalfHourMomentum.cs`, class and strategy name `PraxisLastHalfHourMomentum`), the last-half-hour market intraday momentum timing strategy `η(r_ROD)` of Baltussen, G., Da, Z., Lammers, S. & Martens, M. (2021), "Hedging demand and market intraday momentum", *Journal of Financial Economics* 142, 377–403, DOI 10.1016/j.jfineco.2021.04.029. *Rule:* at the close of the first 1-minute bar in [15:30, 15:59) of a weekday session (normally the 15:30-stamped bar), r = Close(that bar) / Close(most recent 16:00-stamped bar of a prior session) − 1; if r > 0 go long (`LHMomLong`), otherwise, including r = 0, go short (`LHMomShort`); market orders; flatten on the 15:59-stamped bar (`LHFlat1559`, which fills at the 16:00 bar's Open, ≈15:59 price); at most one trade per session; no signal on a Saturday/Sunday bar; sessions with no bar in that window (early close) are not traded; the only input is `Contracts`; compile-intended, not compiled. *Why #1:* it ranked first on the shortlist (`docs/reports/2026-10-31-7zq-m2-shortlist.md`) with a score of **15**, over **#2 TORB** (Tsai et al. 2019, *IEEE Access* 7) at **12** and **#3 5-minute ORB** (Zarattini & Aziz 2023, SSRN 4416622) at **10**. It is the only candidate whose full rule set was read in the primary source, it has zero free parameters, it has NQ-specific published evidence (1996-04-12 → 2020-05-01), and it is the most distinct from Noise-Area (one fixed 15:30 decision; no band, no checkpoint ladder, no VWAP exit). Caveats: the published results are gross of costs (p. 386) and for an equity-futures portfolio, not NQ alone. **Amear may swap to #2 or #3 after reading the shortlist.**

The rest of line 43 after the placeholder stays as it is ("The research manager ranks a shortlist of three; #1 is built;
Amear may swap in the morning, and the other two survive as written specs (`2026-10-31T00:46:43Z`).").

Sources for the facts in the replacement: shortlist §Candidate #1 (citation, DOI, Eq. 2/Eq. 12, Table A1 sample dates, p. 386 cost
quote) and §Ranking (totals 15/12/10, reasons 1–4), OBSERVED in that file this session. The rule's bar mechanics (15:30 decision,
15:59 flatten, exit names, `Contracts`-only input) are the manager's pinned design; the previous-close rule (16:00-stamped close),
first-bar-in-window signal and weekend skip were checked against the revised `.cs` by worker 5 (OBSERVED in the source; behaviour INFERRED, not compiled).

## (b) DRAFT MANIFEST rows (M2)

`MANIFEST.md` header, OBSERVED (`head -5 MANIFEST.md`):
```
# Build Manifest — PRAXIS

| File Path | Type | Phase | Date Created | Purpose |
|-----------|------|-------|-------------|---------|
| /.gitignore | Config | 0 | 2026-05-08 | Git ignore patterns |
```
The conventions are copied from M1's draft rows (`docs/reports/2026-10-31-7zq-decisions-scope.md:69-80`): `.cs` = `Source`, docs = `Report`,
Phase `2`, leading `/`.

| /ninjascript/PraxisLastHalfHourMomentum.cs | Source | 2 | 2026-10-31 | Praxis_build-7zq M2 new researched NQ intraday strategy (third file of D-2026-10-31-A): Baltussen, Da, Lammers & Martens (2021) JFE 142:377–403 last-half-hour momentum η(r_ROD). Signal on the first bar in [15:30, 15:59) of a weekday session (normally 15:30): long if Close(signal bar)/most recent prior 16:00-stamped close − 1 > 0, else short (incl. 0); market orders; entry fills at the next bar's open (normally 15:31); flatten on the 15:59 bar (LHFlat1559); IsExitOnSessionCloseStrategy backstop; LHStaleFlat safety exit (should never fire); at most one trade per session, none on Sat/Sun bars; input Contracts only; backtest-only, no live-signal path; compile-intended, not compiled on the Mac |
| /docs/reports/2026-10-31-7zq-m2-shortlist.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 researched shortlist of three non-Noise-Area NQ intraday strategies (#1 Baltussen et al. 2021 η(r_ROD), 15; #2 Tsai et al. 2019 TORB, 12; #3 Zarattini & Aziz 2023 ORB, 10), with rule sets, cited results, NQ 1-min mapping and NEEDS AMEAR; #1 built, Amear may swap |
| /docs/reports/2026-10-31-7zq-m2-worker1-research.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 research sub-report (worker1): process log with commands and outputs behind the shortlist. NOT authoritative; sub-report to the 7zq M2 manager report |
| /docs/reports/2026-10-31-7zq-m2-worker2-build.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 build sub-report (worker2, PraxisLastHalfHourMomentum.cs); written after this draft. NOT authoritative; sub-report to the 7zq M2 manager report |
| /docs/reports/2026-10-31-7zq-m2-worker3-docs.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 docs sub-report (worker3): process log for the M2 hand-test checklist and this decisions addendum. NOT authoritative; sub-report to the 7zq M2 manager report |
| /docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 ADVERSARIAL sub-report (worker4); written after this draft. NOT authoritative; sub-report to the 7zq M2 manager report |
| /docs/reports/2026-10-31-7zq-m2-worker5-fix.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 fix sub-report (worker5) — file created and staged 2026-10-31. NOT authoritative; sub-report to the 7zq M2 manager report |
| /docs/reports/2026-10-31-7zq-m2-handtest-checklist.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 one-page hand-test checklist for Amear at the Fusion VM for PraxisLastHalfHourMomentum: install + F5 (stop on error), run-4 Analyzer settings with sources, INFERRED expectations (≤ 1,304 trades from the import-file session count, LHFlat1559 exits, cost arithmetic, out-of-sample note), readbacks; carries the R-F3-3 limitation sentence verbatim. Nothing compiled or run |
| /docs/reports/2026-10-31-7zq-m2-decisions-addendum.md | Report | 2 | 2026-10-31 | Praxis_build-7zq M2 DRAFT replacement text for the third-file placeholder in D-2026-10-31-A (decisions-scope.md:43), these MANIFEST rows, the S6 cross-block check and NEEDS AMEAR; NOT appended |
| /docs/reports/2026-10-31-7zq-m2-new-strategy.md | Report | 2 | 2026-10-31 | Manager report for Praxis_build-7zq M2 (shortlist + PraxisLastHalfHourMomentum.cs + checklist + addendum); written after this draft; ungraded at time of row |

## (c) S6 cross-block check (stated, not decided)

Rubric headings, OBSERVED:
```
$ grep -n "^### F" specs/SPEC_RUBRIC.md
17:### F1 — Signal-path topology vs. circuit-breaker placement
30:### F2 — Session-flat time vs. breakers #4 and #5
45:### F3 — Backtest fill resolution vs. acquired data granularity
59:### F4 — MFFU automation compliance
```
**Touches Block 2 only.** This is a backtest-only research artefact for the Block-2 arm's hand test, run in the Strategy Analyzer.
Like M1's entry (decisions-scope `:54`), it sits outside the replication arm, so **O1** (`specs/SPEC_RUBRIC.md:74`) is not answered or changed.
- **F1 — Signal-path topology vs. circuit-breaker placement** (`:17`): untouched. There is no live-signal code. By design the file
  never touches `PraxisSignalConsumer` or the signals drop directory (INFERRED from the pinned design; the .cs was not read by this worker).
- **F2 — Session-flat time vs. breakers #4 and #5** (`:30`): untouched. This unit sets no governing flat-time rule and neither
  resolves nor changes F2: no governing rule is yet written (`specs/SPEC_RUBRIC.md` F2 criterion; DECISION_LOG:365 context). The
  backtest flattens on the 15:59 bar as a realisation of Deviation B's 16:00 flatten. The 15:00 disposition is not addressed.
  **Stated for Amear, not decided:** this strategy holds positions only between 15:30 and 16:00 ET. That is entirely inside breaker
  #5's window ("breaker #5 disables everything 15:00–18:00 ET", `:32`, OBSERVED). If it were ever taken toward live, the
  F2 governing rule would decide whether it can trade at all. Nothing here takes it toward live.
- **F3 — Backtest fill resolution vs. acquired data granularity** (`:45`): untouched. No backtest is run or reported. The checklist
  carries the limitation sentence verbatim: `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
  It is not the backtest report F3 waits for.
- **F4 — MFFU automation compliance** (`:59`): untouched. Nothing is MFFU-facing: no live or funded account, Sim-only Analyzer use.
- Walk-forward hold: unchanged.

## (d) Status

**This text is NOT yet in `DECISIONS.md` or `MANIFEST.md`.** This worker did not touch either file. The S4 authorisation chain for
tonight is DECISION_LOG `2026-10-31T00:46:43Z` (WHO: amear): "Run them now and I'll commit in the morning", and, for the third file,
"Build the top-ranked one (Recommended)" (grep pasted at the top). The rest of the chain is as M1's draft states (`decisions-scope.md:47`).

## (e) NEEDS AMEAR

These are your questions. None is answered here.
1. **Swap:** keep #1 (Baltussen `η(r_ROD)`), or swap to #2 (TORB) or #3 (Zarattini & Aziz ORB)? The shortlist notes that #2 and #3
   are both opening-range breakouts (one family).
2. **r = 0 → short.** The build goes short when r is exactly 0, reading Eq. 12's "otherwise" (INFERRED). Keep it, or stand aside? (Shortlist Q1.4.)
3. **Which prior close (D3)?** The build now uses the **most recent 16:00-stamped close of a prior session**, not the prior session's
   last bar. The import data has 37 weekday sessions ending 13:00 (CME halts on NYSE holidays), 9 ending 13:15 and 1 ending 14:03
   (OBSERVED, manager's session scan). The paper drops non-business and early-close days (p. 381), so its "previous day's close" is
   read as the prior regular day's 16:00 close (INFERRED); a 16:00 stamp is also robust to the template ending at 16:00 or 17:00 ET
   (DECISION_LOG:365, unadjudicated). A Print warning fires if that close is > 4 days old (diagnostic only). **Alternative:** skip the
   day after any non-regular session. Keep the 16:00-close rule, or switch to the skip?
4. **Missing 15:30 bar (fallback).** The signal is taken on the **first** bar in [15:30, 15:59), so a missing 15:30 bar falls back to
   the next bar in the window (deviation D1). In the import data every weekday session with a bar in that window has a 15:30 bar
   (worker 4, OBSERVED), so the fallback does not fire on weekdays there. Keep the fallback, or require the 15:30 bar exactly?
   (Shortlist Q1.3.) Weekend bars in the window never signal (D7).
5. **Exit realisation: 15:59 flatten vs session-close exit.** The build sends the exit on the 15:59 bar, so it fills at the 16:00 bar's
   Open (≈15:59 price), with exit-on-session-close only as a backstop. The paper earns through the 16:00 close. Is a fill at the 16:00
   bar's Open acceptable? (Shortlist Q1.2; same question as M1's Flat1559 item 7.)
6. **15:30 reference price.** The design uses Close of the 15:30-stamped bar; the alternative is Open of the 15:31 bar. The paper's
   minute-price choice is SPEC-SILENT. (Shortlist Q1.1.)
7. **Variant `η(r_ONFH, r_ROD)`** (trade only when the first-half-hour and rest-of-day signs agree): also build it, or not? Not built. (Shortlist Q1.5.)
8. **Roll convention.** Does NQCONT's roll matter compared with the paper's volume-based roll? (Shortlist Q1.6.)
9. **First session of the series** has no prior close. The design skips it (INFERRED necessity; shortlist Q1.7).
10. **Breaker #5 overlap** (from (c)): the strategy trades only inside the 15:00–18:00 ET window that breaker #5 disables. Is it
    research-only by design, or should that be weighed before it is ranked against anything headed for live?
