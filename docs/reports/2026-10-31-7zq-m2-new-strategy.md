# 7zq M2 — new researched NQ intraday strategy: shortlist, pick, build (manager report)

**Unit:** `Praxis_build-7zq` phase M2 · praxis-manager · 2026-10-31 (10:44Z → 11:20Z) · base HEAD `fab2855`.
**Deliverable level: WRITTEN.** It has not been compiled or tested, and no backtest was run. This Mac has no NT8 toolchain. Every NT8 behaviour claim below is INFERRED or CANNOT-DETERMINE-STATICALLY. The compile on the Fusion VM is Amear's step 1.
Grades: OBSERVED (in pasted output) · INFERRED · REPORTED BY AMEAR · UNVERIFIED · SPEC-SILENT · CANNOT-DETERMINE-STATICALLY.

## Task
Research a shortlist of three published NQ-applicable intraday strategies, excluding Noise-Area and its variants. Score and rank them, build #1 as a NinjaScript backtest strategy, and write the hand-test checklist and the DECISIONS/MANIFEST addendum. Authorisation: DECISION_LOG `2026-10-31T00:46:43Z` (Amear: "Run them now and I'll commit in the morning"; "Build the top-ranked one").

## Rubric criteria addressed
S1, S2, S4, S6, S8 (`specs/SPEC_RUBRIC.md:107-114`) and F3 (FROZEN, `:45`). The F3 sentence is carried verbatim in the .cs and the checklist (Evidence E6).

## 1. Shortlist summary, pick, and why
Full file: `docs/reports/2026-10-31-7zq-m2-shortlist.md`. Scores are 0–3 on each of (a) completeness, (b) data fit, (c) independence from Noise-Area, (d) evidence, (e) simplicity.

| # | Strategy | Source | Text | a/b/c/d/e | Total |
|---|---|---|---|---|---|
| 1 | Last-half-hour market intraday momentum `η(r_ROD)` | Baltussen, Da, Lammers, Martens 2021, *JFE* 142:377–403 | full PDF (co-author site), sha `623ba824…ec57` | 3/3/3/3/3 | **15** |
| 2 | Timely Opening Range Breakout (TORB) | Tsai et al. 2019, *IEEE Access* | full PDF (open access), sha `058bd5e8…e46a`; results tables are images (unread) | 2/3/2/2/3 | 12 |
| 3 | 5-min ORB on QQQ | Zarattini & Aziz 2023 (SSRN) | abstract only; rules from a GitHub README → **UNVERIFIED-from-secondary** | 2/2/2/2/2 | 10 |

**Pick = #1.** Reasons:
- Every rule element is stated in the paper. NQ hours are 09:30–16:00 (Appendix A row, Evidence E2). The signal is Eq. 2 and the sign rule is Eq. 12.
- It needs only RTH 1-minute bars.
- It is a different signal family from Noise-Area: no band around the open, no checkpoint ladder, no VWAP exit.
- The paper has NQ-specific evidence: a regression over 1996-04-12 → 2020-05-01, and Sharpe 1.73 for the equity-futures portfolio (Table 6, p. 387).
- It has zero tunable parameters.

Caveats carried into the docs:
- The paper's results are gross of costs (p. 386, Evidence E2).
- There is no P&L for NQ alone.
- The test range 2021-03 → 2026-07 lies entirely after the paper's sample. This is INFERRED from the dates and makes the test out-of-sample.
- #2 and #3 are both opening-range breakouts, so the shortlist spans only two signal families. A third family (e.g. a gap fade) was not researched.
- Gao, Han, Li & Zhou 2018 was abstract-only.

## 2. Design (as built)
File: `ninjascript/PraxisLastHalfHourMomentum.cs`, 245 lines, sha `9f4953a8…9cec` (Evidence E4). Class and `Name` = `PraxisLastHalfHourMomentum`, the only type declared (E5).
- **Signal.** `Calculate.OnBarClose`. Once per weekday session, on the first bar in [15:30, 15:59), normally the 15:30-stamped bar: r = Close(15:30) / (most recent weekday 16:00-stamped close) − 1. If r > 0, `EnterLong` "LHMomLong"; otherwise, including r = 0 (Eq. 12 "otherwise"), `EnterShort` "LHMomShort". Market orders.
- **Exit.** `ExitLong/ExitShort` "LHFlat1559" on the bar with mod ≥ 15:59. `IsExitOnSessionCloseStrategy = true` is a backstop. A safety exit "LHStaleFlat" on the first bar of a session is followed by `return`.
- **Inputs.** `Contracts` only.
- **Fills (INFERRED).** Entry fills at the Open of the 15:31 bar, about the 15:30 price. Exit fills at the Open of the 16:00 bar, about the 15:59 price. So the paper's final minute (15:59 → 16:00) is not earned.
- **Header.** Carries the citation with pages, the rule→line map (14 entries, verified, E7), assumptions, and deviations D1–D7.
- **Who chose what.** The design was pinned by the manager before the build. Worker 2 built it, worker 5 applied the fixes, and I made two edits in place (§3).

## 3. Adversarial findings and fixes
Worker 4 (ADVERSARIAL; it got the artifacts and criteria, not the builder's reasoning) returned **`VERDICT: BROKEN`, 2 MAJOR + 5 MINOR**. The report is `docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md`.

| # | Sev | Finding | Fix (worker 5 unless noted) |
|---|---|---|---|
| 1 | MAJOR | The addendum said "no fallback" / "no trade without a 15:30 bar". The .cs does fall back to the first bar in the window. | Addendum corrected; the fallback goes to Amear (NEEDS AMEAR 4) |
| 2 | MAJOR | `Close[1]` at the first bar takes a 13:00 holiday-halt price as the previous close. The data has 37 sessions ending 13:00, 9 ending 13:15 and 1 ending 14:03 (**re-observed by me, E3**). | Previous close is now the most recent 16:00-stamped close (D3). This also holds whether the template ends at 16:00 or 17:00 ET (DECISION_LOG:365, unadjudicated). |
| 3 | MINOR | Trade-count estimate too high | Checklist now expects ≤ 1,304 (1,305 sessions with a 15:30 bar − 1; E3) |
| 4 | MINOR | Weekend stray bars fall in the signal window (I count 19 in all data, worker 4 counted 18; not reconciled) | Weekend skip in the signal path (D7) |
| 5 | MINOR | "Governing flat time stays 16:00" overstated F2 | Reworded: this unit sets no governing rule |
| 6 | MINOR | The template's end time is unconfirmed | Checklist read-back of the first and last bar stamps |
| 7 | MINOR | Possible double exit on a stale-exit bar | `return` after `LHStaleFlat` |

Worker 5 flagged one residual: a Sunday 16:00-stamped bar exists in the data (2021-10-31), and the 16:00 capture had no weekday check. **I fixed it myself** with a one-line weekday guard on the capture line (L178). I also made a one-word correction to the header comment (L48, "every WEEKDAY bar") and replaced one MANIFEST row note in the addendum. These are the manager's single-line exceptions. Line count is unchanged at 245, so the rule→line map still holds (E7).

**Residual (stated, not hidden):** the fix round and my edits were **not** re-attacked by a separate adversarial worker, because the 5-worker cap is used up. They were re-verified statically by me only (E4–E7). The auditor should treat the worker-5 diff and L178/L48 as un-adversaried.

## 4. S6 cross-block check
Detail is in the addendum, §(c).
- **Block 2 only.** This is a backtest research artefact for the hand test.
- **F1:** no live-signal code. The file does not touch `PraxisSignalConsumer.cs` or `signals/`.
- **F2:** no governing flat-time rule is set or changed. The 15:59 flatten is a backtest realisation only.
- **F3:** no backtest was run, and the limitation sentence is carried verbatim (E6).
- **F4:** nothing MFFU-facing.
- **Breaker #5 (found by worker 3, `specs/SPEC_RUBRIC.md:32`).** Breaker #5 disables everything 15:00–18:00 ET, and this strategy trades only inside that window. As specified, it can never pass breaker #5 on a live path. **Stated, not decided** (NEEDS AMEAR 10).

**S4.** The authorisation chain is DECISION_LOG `00:46:43Z` plus the draft addendum. **The DECISIONS.md entry is NOT yet appended.** The master's row at `2026-10-31T11:04:20Z` (R-7zq-1) schedules the append of `D-2026-10-31-A`, with M2's slot filled from this addendum, as one dispatch after M2 returns.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| w1 `af5d4bc9` | BUILD (research) | shortlist + process log; PASS on my re-check (E1, E2) |
| w2 `afa5bd07` | BUILD | .cs v1, 209 lines; superseded by the w5 fix |
| w3 `a0e79981` | BUILD (docs) | checklist + addendum; found breaker #5 |
| w4 `a55ee64a` | ADVERSARIAL | `VERDICT: BROKEN` 2 MAJOR / 5 MINOR |
| w5 `a5a2a4f9` | BUILD (fix) | all 7 addressed; flagged the Sunday-16:00 residual |

## Process log
1. **Baseline.** I captured hashes of the 38 protected paths before any dispatch. My first attempt was a false null: zsh does not word-split a variable, so `git diff --quiet` ran on a single bogus path and exited 0. I re-ran it as a bash array.
2. **w1 returned.** I re-hashed the downloads, then grepped the paper for the NQ trading hours, Eq. 2, and the cost disclaimer.
3. **w2 and w3 in parallel**, on disjoint files, from a design I pinned (class name, signal names, constants). I read the .cs myself.
4. **w4 adversarial.** I re-observed MAJOR 2 with my own session scan of the import file.
5. **w5 fix**, then my single-line edits, re-staging, and the final checks.

## NEEDS AMEAR
Unanswered. The full list is in the addendum §(e) and the shortlist's `## NEEDS AMEAR`.
1. **Swap.** Keep #1, or swap to #2 (TORB) or #3 (ORB)?
2. **r = 0 → short.** This reads Eq. 12's "otherwise" (INFERRED). Keep it, or stand aside?
3. **Previous close.** Most recent 16:00-stamped close (as built), or skip the day after any non-regular session?
4. **Missing 15:30 bar.** Fall back to the first bar in the window (as built), or require the 15:30 bar exactly?
5. **Exit realisation.** The 15:59 bar sends the exit, which fills at the 16:00 bar's Open. Your R-7zq-2 ruling (`11:04:20Z`) accepted this for **Flat1559**. Whether that ruling extends to this file is yours; I have not applied it here.
6. **15:30 reference price.** Close of the 15:30 bar (as built) or Open of the 15:31 bar? The paper is SPEC-SILENT.
7. **Variant `η(r_ONFH, r_ROD)`.** Build it or not? It is not built.
8. **Roll convention.** NQCONT vs the paper's volume-based roll.
9. **Breaker #5.** Is this strategy research-only by design, given it trades only inside 15:00–18:00 ET?
10. **Brief vs reality.** The brief required `git diff --quiet HEAD -- <protected>` = 0. It was already 1 before this unit started, because of other units' staged and unstaged work (E8). I report baseline-vs-end hash equality instead. This is for the master to accept or reject.

## Verification evidence
All outputs below are pasted from this session.

**E1 — downloads (re-hashed by me; refetched #1 into a fresh dir):**
```
623ba82490acd01546f568cf582de5a9b45dfbd97731cd548cb119d7a0acec57  ./baltussen-nd/intramom.pdf
058bd5e8b4a21eb312b2447f7ff04c9aacc764c6530580c45a120bcb8f89e46a  ./ieee-orb/paper.pdf
4f0ff1e00fdc3318f600a3c9441518544f3bfb567640ef8d865ab724d195480f  ./gh-brusco-readme/README.md
d0bd26e424a0c81bbca149e35566a3b9929a3cd207934e07638a99e78ca4ca80  ./arxiv-2605.04004-pdf/paper.pdf
./baltussen-nd/intramom.pdf:      PDF document, version 1.7, 23 pages
./ieee-orb/paper.pdf:             PDF document, version 1.5, 6 pages
./baltussen-jfe2021/paper.pdf:    HTML document text, ASCII text, with very long lines (5620), with no line terminators
refetch 200 application/pdf 2397917
623ba82490acd01546f568cf582de5a9b45dfbd97731cd548cb119d7a0acec57  .../baltussen-nd-refetch/intramom.pdf
```
Worker 1's recorded curl status lines (`docs/reports/2026-10-31-7zq-m2-worker1-research.md`):
```
50:ieee 200 application/pdf 8930514
60:balt 403 text/html; charset=UTF-8 5620
81:balt-nd 200 application/pdf 2397917
84:arxiv-orb 200 application/atom+xml; charset=utf-8 45323   (only 2605.04004 relevant)
```

**E2 — paper text (`intramom.txt`, pdftotext of the sha-623ba824 PDF):**
```
343:rebalanced. This corresponds to the trading hours of the             rROD,t =           − 1,                                              (2)
794:   Note that we do not consider transaction costs. Given                                                       tick (a cost level faced commonly by advanced investors
811:position otherwise. Timing strategy η (rONF H , rROD ) takes a long (short) position when both the ﬁrst half-hour return and the return until 30 minutes before
1375:  NASDAQ 100 futures∗                       NQ              1996-04-12            2020-05-01           6017           09:30–16:00               USA
```

**E3 — session scan of the import file** (my script `m2-sessions.py`, range 2021-03-08 → 2026-07-17):
```
weekday sessions in range: 1352  with 15:30 bar: 1305  with 16:00 bar: 1305
weekend bars in 15:30-15:58 window (all data): 19
last-bar stamp counts (non-16:00): [(1300, 37), (1315, 9), (1403, 1)]
13:00-last sessions: ['20210531', '20210705', '20210906', '20211125', '20220117', '20220221'] ...
```

**E4 — the .cs (final, staged):**
```
9f4953a8b25fe598a97690d53684f7f17e23506053ddc556e934288dfc439cec  ninjascript/PraxisLastHalfHourMomentum.cs
     245 ninjascript/PraxisLastHalfHourMomentum.cs
0
00000000: 2372 65                                  #re
open       13 close       13
```
These are, in order: the sha256, the line count, the CR count, the first three bytes (no BOM; "#re" = `#region`, same as the base), and brace balance. The sha differs from worker 5's `bacd30d0…` because of my two in-place edits (§3).

**E5 — duplicate-type grep** (positive control: the same grep fires on the base enum `PraxisNoiseExitMode`):
```
ninjascript/PraxisLastHalfHourMomentum.cs:122:	public class PraxisLastHalfHourMomentum : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:47:	public enum PraxisNoiseExitMode
ninjascript/PraxisNoiseAreaBreakout.cs:53:	public class PraxisNoiseAreaBreakout : Strategy
ninjascript/PraxisNoiseAreaBreakout.cs:65:		private sealed class DayRecord
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:85:	public class PraxisNoiseAreaBreakout_Flat1559 : Strategy
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:98:		private sealed class DayRecord
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:76:	public class PraxisNoiseAreaBreakout_OppBand : Strategy
ninjascript/PraxisNoiseAreaBreakout_OppBand.cs:88:		private sealed class DayRecord
ninjascript/PraxisSignalConsumer.cs:44:	public class PraxisSignalConsumer : Strategy
ninjascript/PraxisSignalConsumer.cs:487:		private sealed class ParsedSignal
```
The comment-only hits at Flat1559 `:47`/`:78` and OppBand `:39`/`:70` are omitted here. The only new type is `PraxisLastHalfHourMomentum`. `DayRecord` is nested and private in two files; that was M1's state and is not touched by M2.

**E6 — F3 sentence, verbatim count:**
```
ninjascript/PraxisLastHalfHourMomentum.cs:1
docs/reports/2026-10-31-7zq-m2-handtest-checklist.md:1
```

**E7 — rule→line map vs real lines (excerpt):**
```
108://   P(c,t-1) = most recent 16:00 close (Eq. 2, D3) ..... mod == CloseMod test   L178, capture L180
126:		private const int SignalMod = 15 * 60 + 30;   // 930 — the 15:30 bar (c - 30, Eq. 2 p. 381)
127:		private const int FlatMod   = 16 * 60 - 1;    // 959 — the 15:59 bar; exit fills at the 16:00 bar Open (INFERRED)
128:		private const int CloseMod  = 16 * 60;        // 960 — the 16:00 bar; its Close is the regular close P(c) (D3)
178:			if (mod == CloseMod && Time[0].DayOfWeek != System.DayOfWeek.Saturday && Time[0].DayOfWeek != System.DayOfWeek.Sunday)
209:					ExitLong("LHFlat1559", "LHMomLong");
211:					ExitShort("LHFlat1559", "LHMomShort");
216:			bool inSignalWindow = SignalMod <= mod && mod < FlatMod;
233:				EnterLong(Contracts, "LHMomLong");          // predictor > 0 -> long (Eq. 12, p. 385)
235:				EnterShort(Contracts, "LHMomShort");        // "otherwise" (incl. r == 0) -> short (Eq. 12, p. 385)
```

**E8 — protected paths: baseline (10:45:04Z, before any dispatch) vs end (11:16:02Z)**, 38 paths, from `scratchpad/m2-protect.sh`:
```
BASELINE                                                                 END
git diff --quiet HEAD exit=1                                             git diff --quiet HEAD exit=1
index-vs-HEAD diff sha:    7b3f3be00e0f0f92…                             7b3f3be00e0f0f92…   (identical)
index entries sha:         db21c38d032c0f37…                             db21c38d032c0f37…   (identical)
worktree-vs-HEAD diff sha: 47b8d49d7443a896…                             b8a2fd7b10322865…   (changed)
file-content sha:          9006e530863e3178…                             b8827868…           (changed)
```
- **Nothing protected was staged by M2.** The index is identical to the baseline.
- **Two protected files changed in the worktree during the run, neither by M2:**
  - `DISPATCH_LOG.md` (mtime 11:15:14Z) holds hook-written rows: `[2026-10-31T11:15:14Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop…`. These are the SubagentStart/Stop hook logging my workers.
  - `DECISION_LOG.md` (mtime 11:04:34Z) holds the master's own row `[2026-10-31T11:04:20Z] **WHO: amear** | PROPOSED BY: praxis-master … TWO RULINGS`.
- **No M2 edit to any protected file, OBSERVED.** The other protected paths' latest mtimes are 06:37–06:40 local (decisions-scope, m1-variants), which is before the baseline. Exit 1 on `git diff --quiet HEAD` was already present at baseline and comes from other units.
- **Positive control:** a one-byte change alters a file hash (`ec7cb1c70dc79405` → `d33974925b00ff93` for decisions-scope + "x").

**E9 — `git status --porcelain`, M2 files (all `A`, staged, uncommitted):**
```
A  docs/reports/2026-10-31-7zq-m2-decisions-addendum.md
A  docs/reports/2026-10-31-7zq-m2-handtest-checklist.md
A  docs/reports/2026-10-31-7zq-m2-shortlist.md
A  docs/reports/2026-10-31-7zq-m2-worker1-research.md
A  docs/reports/2026-10-31-7zq-m2-worker2-build.md
A  docs/reports/2026-10-31-7zq-m2-worker3-docs.md
A  docs/reports/2026-10-31-7zq-m2-worker4-adversarial.md
A  docs/reports/2026-10-31-7zq-m2-worker5-fix.md
A  ninjascript/PraxisLastHalfHourMomentum.cs
```
This report is staged after it is written (see Files staged).

## Files staged
The nine files in E9, plus this report `docs/reports/2026-10-31-7zq-m2-new-strategy.md`. Nothing is committed.

## Result
Stress-test Result: PASS at the WRITTEN level. The build survived adversarial review after fixes, but the fix round was not re-adversaried (§3 residual), and nothing was compiled, tested or backtested.
Result: DONE
