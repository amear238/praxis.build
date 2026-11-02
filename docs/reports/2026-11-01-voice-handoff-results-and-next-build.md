# Voice handoff — three-strategy results, backtest options, next build (2026-11-01)

Written by Claude Code (praxis-master) for the Claude voice/chat agent. Assume the reader has seen nothing. Amear asked for it with "give me handoff to continue build and discuss the backtest option in the voice chat".

## 0. Rules for the voice agent

- **Discuss and record. Don't decide for Amear.** Every choice in §5 and §6 is his. Write down each ruling in his own words.
- **No code, template or config changes** come out of this conversation. Rulings go back to Claude Code, which logs them and dispatches the work.
- **No "which strategy is best" verdict** from the voice agent (ruling R-1101-5). Lay out the facts and the trade-offs, and let him choose.
- **Frozen criteria (hard stops):**
  - **F1:** signal-path vs circuit-breaker placement.
  - **F2:** session-flat time vs breakers #4 and #5. No trading-hours template edits.
  - **F3:** fill-resolution assumption. Every backtest report must carry the sentence below.
  - **F4:** MFFU written confirmation that the automation is allowed.

  Work that depends on a frozen item waits. Amear can override, but only explicitly, and the override gets logged.
- The limitation sentence every backtest result carries: **"Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed."**
- **What to bring back:** write `docs/reports/2026-11-01-voice-session-notes-3.md` with three parts: his rulings numbered R-VN3-1, R-VN3-2 and so on, any numbers he reads off screens (graded REPORTED BY AMEAR), and anything left undecided. Then tell him: "To start Code on it, tell it to read the notes-3 file first."

## 1. Where things stand

- **Baseline is locked** on the Future row `NQCONTROW SEP25`: $20/pt, tick 0.25, rollover 2021-03-01, Do not merge. The run used the PRAXIS commission template at $2.96 per round trip.
- Analyzer settings are saved as his default template. NT8 is 8.1.8.4, which he updated himself.
- This morning he installed and ran three new strategies on the VM. That was off-plan by his own ruling, which lifted R-VM-5. The High-resolution control run (0-H) is deferred.
- Claude Code processed all four exported trade lists and his three screenshots, and the work passed audit. It is committed and pushed as `8ca9861`. The full report is `docs/reports/2026-11-01-three-strategy-results.md`, and a short summary is in §3 of `docs/reports/2026-10-31-voice-session-notes-2.md`.

## 2. Results — all three runs VALID

Every setting visible in his screenshots matches the required list. Two things can't be seen in the screenshots: the $2.96 rate inside the PRAXIS template, and the full strategy names (the dropdown cuts them off). The trade lists confirm both: $2.96 on every row, and the full name on every row. Every run shows Qty 1, no duplicate entries, and never more than one position open.

| | Baseline (Noise-Area, BandOrVWAP exit) | OppBand | Flat1559 | Last-Half-Hour Momentum |
|---|---|---|---|---|
| Trades (long / short) | 1,190 (556 / 634) | 810 (404 / 406) | 1,190 (556 / 634) | 1,304 (698 / 606) |
| Net profit | $197,327.60 | $210,182.40 | $193,017.60 | −$76,009.84 |
| Longs / shorts net | $136,314 / $61,013 | $138,454 / $71,728 | $138,509 / $54,508 | −$24,736 / −$51,274 |
| Profit factor | 1.29 | 1.26 | 1.28 | 0.84 |
| Max drawdown | −$45,282.04 | −$50,748.88 | −$40,637.04 | −$99,806.96 |
| Win rate | 40.7% | 58.0% | 40.5% | 47.6% |
| Avg trade | $165.82 | $259.48 | $162.20 | −$58.29 |
| Largest win (% of net) | $35,887 (18.2%) | $36,087 (17.2%) | $36,472 (18.9%) | $3,852 (n/a, net negative) |
| Largest loss | −$5,407.96 | −$19,592.96 | −$5,407.96 | −$5,537.96 |
| Avg time in trade | ~120 min | ~291 min | ~120 min | ~29 min |

Figures come from the trade lists and were checked against his screenshots. The long/short split and time in trade are from his Summary screenshots.

## 3. What each strategy is, and what the run showed (facts, not verdicts)

**Baseline: Noise-Area Breakout (BandOrVWAP).** This is the paper replication. It enters when price breaks out of a "noise band" around the open, checked at :01 and :31 each half hour. It exits when price comes back to the band or VWAP, whichever is tighter, or at the session close.

**OppBand.** The same entries, but the stop is moved to the opposite band, which is much wider.
- The wide stop almost never triggers: 792 of the 810 trades exit at the session close, and only 18 hit the stop.
- Trades are held about 2.4 times longer (291 vs 120 min). Fewer re-entries means fewer trades.
- The win rate jumps to 58%, but the average loss is about −$2,351, against about −$965 for the baseline.
- The worst single trade is −$19,593 (a long on 2025-04-08). The baseline's worst is −$5,408.

**Flat1559.** Identical to the baseline except that it closes out one minute before the bell.
- All 1,190 entries are the same as the baseline's. Only the 423 end-of-day exits differ, and together they cost $4,310 over five years.
- **One subtlety:** the trade list prints these exits as 4:00 PM, but the price is the opening price of the last one-minute bar, i.e. the 15:59:00 price. That is an inference from how the bars are stamped. The baseline's session-close exit uses that bar's closing price instead.

**Last-Half-Hour Momentum.** This is a new, researched strategy (Baltussen et al., 2021).
- **The rule:** if the market is up since yesterday's close at 15:30, buy at 15:31; if it's down, sell. Exit at about 16:00. One trade a day, about 30 minutes long.
- It lost money on both sides over this period: PF 0.84.
- Costs per trade are about $23: $2.96 commission plus 2 ticks of slippage each side, or $20. That is Claude Code's arithmetic and wasn't audited. Over 1,304 trades that's about $30,000 of the −$76,000.
- It didn't trade on 47 short sessions (early-close days), on the first day, or on the 2023-04-05 data-gap day. The "Bars" column reads 30, not 29.

## 4. Data and platform findings

1. **Early-close days:** on the 13:15 early-close days the session-close exits are stamped 12:15, an hour before the data ends. On two 13:00 days (2025-01-20 and 2025-06-19) they're stamped 12:00. The VM agent's guess is that the trading-hours template holds a Central time in an Eastern template. That guess is **not tested, and it touches F2 (frozen).** Nothing has been changed.
2. **Two 17-day holes with no bars at all:** 2021-09-09 → 09-27 and 2025-12-14 → 2026-01-01. No trades happen inside them. Each hole also sits inside the 14-day lookback the Noise-Area bands use for the sessions right after it, and that effect wasn't analysed.
3. **Three known gaps are wider than recorded:**
   - 2024-07-19 is missing 09:58–10:07.
   - 2024-08-02 is missing 11:55–12:02.
   - 2026-07-17 is missing 10:59–12:06.
4. **48 weekdays have no regular-session bars.** These are mostly holidays; nine fall near quarterly contract rolls (inferred from timing). No trades happen on them.
5. The screenshots' "Avg. bars in trade" is always exactly 1 less than the trade list's Bars column. It's harmless, just a counting difference.
6. **Not yet checked:** whether the strategy files installed on the VM are byte-identical to the repo copies.

## 5. Decisions only Amear can make (the report's open questions)

1. **Early-close stamps (F2, frozen).** Does he want this looked into? Any change to the template waits on F2.
2. **Data holes and gaps.** Accept the data as-is for these runs, or re-source and re-import the 17-day holes and the gaps?
3. **Flat1559.** Does a fill at the 15:59:00 price meet his "flat at 15:59" intent, even though the grid prints 4:00 PM?
4. **Last-Half-Hour Momentum.** Is skipping every early-close day, plus 30-bar holds, what he intended? Keep it, change it, or drop it?
5. **Settings not visible in the screenshots** (the $2.96 rate, full names). Is the trade-list evidence enough, or does he want screenshots?
6. **Baseline settings screenshot.** The baseline has none; its settings rest on his spoken readback. Does he want one?
7. **Hash-check of the three strategy files on the VM**?
8. **Archiving.** Copy the Desktop CSVs and screenshots into the project folder?

## 6. Backtest options to discuss (a menu, not a recommendation)

**A. Analysis Claude Code can do from the existing trade lists, with no VM time:**
- Profit and loss by year, to see whether one or two years carry the result.
- Results with the top 5 or 10 trades removed. The largest win is 17–19% of net for the Noise-Area runs, so this tests how much hangs on a few big days.
- Long side vs short side by year. Shorts are weaker in every Noise-Area run.
- Drawdown length and recovery time.
- Slippage sensitivity by arithmetic, e.g. 3 or 4 ticks per side.

**B. New runs he would do by hand on the VM:**
- **0-H control (Standard vs High fill resolution).** This is deferred; it probably needs data finer than 1-minute bars. Its outcome bears on F3.
- **Other variants of a strategy.** Any variant is a code change, so it is a new Claude Code build unit and needs his scope ruling first.
- **Re-runs after re-sourced data**, if he chooses that in §5.2.

**C. Pending explanations (beads):**
- **q36:** why the new baseline has 1,190 trades against the retired Stock-row run's 1,211.
- **b5z:** a volume anomaly in the 2021 portion of the import file.

## 7. Build backlog — for "continue build" (he picks the next unit)

**Strategy and backtest track:**
- **zyd:** pin down the fill-resolution assumption. This is tied to F3 and the 0-H control.
- **4uu:** reconcile the NinjaScript strategy against TradingView alerts. Blocked by F3.
- **q36** and **b5z:** the two data explanations in §6.C.
- **1gd:** the data-stitch acceptance gate can never be reached. It emits FLAG where the spec requires FAIL.

**Safety / spec track (these unfreeze F1/F2):**
- **r8j:** import the Phase 3 build spec into the repo: the nine circuit breakers and where they sit, plus the live-vs-backtest gate.
- Then a written decision on the session-flat rule (F2), and the live signal-path topology (F1).

**Compliance (Amear's own task):**
- **fx4 / F4:** email MFFU for written confirmation that full automation is allowed. Nothing goes live without it.
- **zd4:** the `praxispush` low-privilege user requirement. Re-provision it, or formally log its removal.

**Process tooling (the orchestration hooks themselves):** five P0 bugs in the commit and agent guards (22q, dj2, s8g, hwk, 1ys), plus several P1s. These don't affect trading results, but they protect the build process.

## 8. Housekeeping state (for Claude Code next time)

- `main` = `origin/main` = `8ca9861`.
- **Uncommitted:**
  - Ledger rows from after the commit.
  - This handoff file. Its MANIFEST row is owed; the master can't edit MANIFEST, so the next dispatch adds it.
  - An untracked manager process record, `docs/reports/2026-11-01-three-strategy-results-s2-fix-manager-record.md`.
  - The old 12-file staged set, which is still staged and has never been ruled on.
- **Process note:** today's audit took one "no verdict" (the auditor ran out of turns, which isn't a strike) and one S2 fail. The fail was four lines that called inferences "observed". It was fixed by changing labels only, and passed on re-audit.
