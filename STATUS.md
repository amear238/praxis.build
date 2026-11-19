# PRAXIS status

Last updated: 2026-11-19.

## The goal

As written before 2026-11-19: one strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets.

**Under review after the voice call of 2026-11-19.** What changed, in his words: "I want to like uh, temporarily retire the um, idea of completely non-discretionary but I want to find a strategy that is fully executed by human", and "I think I'm ready to retire the idea of uh, full automation." An AI model may later assist "slowly" with execution. The new goal wording is his to give (`RULINGS.md`, "Human execution, automation paused").

Frozen, as before: MyFundedFutures follow-up, the Hermes timer, the project kit, extras on the Windows machine. The signal path built earlier stays as it is.

## What is done

- The signal path from a signal file to a NinjaTrader order was built and signed off on sim earlier in the year.
- The restructure of 2026-11-15: the old agent chain and its files are in `archive/2026-11-15/`, unchanged. One session does the work. Tests are the check.
- Data (2026-11-17): Databento, eleven markets, 1-minute bars from 2018 and daily bars from 2010, $122.99 of the $125 free credit (bill confirmed by him 2026-11-18). Saved, not committed, in `market-data/databento`.

**Every automated candidate failed the five bars on the $150,000 MyFundedFutures frame** ($4,500 end-of-day trailing limit, $9,000 target, midpoint fills). Verdicts: each folder's `out/VERDICT.md` under `research/`.

| Strategy (2026) | Result |
|---|---|
| Noise-Area, 12 variations at 3 sizes (11-17) | none of 36 passes; nearest $8,600 and 26 days with no trade |
| Opening range breakout, 108 versions (11-17) | none worth a final run |
| Session sweep, his pasted idea (11-17) | loses about $0.16 per $1 risked after costs |
| Trend-following, same-day and multi-week, 11 markets (11-18) | same-day: 0 of 72 make money; multi-week best $6,738, winners 0.66 of the risk |
| Marked levels 1 to 4: fade, break and retest, value area, acceleration (11-18) | all fail before the full run; nearly every version loses even before costs |
| Momentum into the close (11-18) | all 12 versions lose on all 11 markets |

**From 2023 onward (2026-11-19, his request; math on the saved results, nothing rerun).** Noise-Area, 2023-01-03 to 2026-07-17: no run passes. W2 at $100 makes $2,135; V1 makes $20,522 to $72,774 but crosses the limit in 100% of shuffles. The others were measured only to 2023, so only 2023 was sliced: the best is $1,873 (fade the first touch), and momentum into the close and same-day trend have no version that made money. Figures: `docs/reports/2026-11-19-voice-notes-search-next.md`.

Checks: each rule check was written by a separate agent from the plan alone and replayed every trade with no break (1,937,028 trades across the levels and momentum passes). Every measurement reproduces byte for byte.

## What is running

Nothing. Heavy jobs one at a time: two at once ran the machine out of memory on 2026-11-18.

## What is next, in order

1. **The interview, then the research, in the Claude.ai chat** (task `Praxis_build-iiu`, from the second handoff of 2026-11-19). His words: research agents "to find strategies that a you know steak and potatoes day trader would adopt", and "the best thing is for the Claude AI chat is to interview me prior". Not coding work. Its results are written into the project docs.
2. **Paused, not closed:** the widened research pass for automated strategies (task `Praxis_build-8h5`). Also paused with it: confirming that MyFundedFutures lists every micro used, and the results for the old shortlist on unmerged worktree branches.

## What waits on Amear

1. **Not answered on the call of 2026-11-19:** buying finer data (his 2026-11-17 line has the money wait for a scalping idea), and marking past days himself for a direct test.
2. **Not yet decided for a human-executed strategy.** These are questions, not rulings. They decide how the research results are judged. They go in the next voice brief, one at a time, written when he asks.
   - The five bars were set for backtested, rule-based strategies. Do they apply as they stand? His 2026-11-17 "bars stay" was about the automated search.
   - Does "nothing goes to execution without enough backtest data" (2026-11-15) still hold?
   - Do the cost-of-the-trade rule, the stop-market order at entry, and one strategy at a time still hold?
   - The account: still the $150,000 MyFundedFutures evaluation (2026-11-17), or another?
   - The seven-day bar: the firm's rule (any trade within seven calendar days) was not confirmed in a sentence of his own.
   - The floor: maximum trades, daily loss cap, drawdown kill switch, hard stop time and what follows a win are not set (`RULINGS.md`, "Numbers that are not set yet"). Who enforces each when a human places the orders? No values proposed.

## Decided without waiting, reversible

- 2026-11-19: the free search of published research for scalping and order-flow edges is paused until he gives a direction. It was framed as part of the automated search.
- 2026-11-19: the files held back for personal data (a support-reply screenshot showing a third party's name and address, and 7 older reports) stay out of the repo.
- 2026-11-18: "mark out the charts or spreads" read as marking levels on price charts. Momentum into the close: stock index trades close at 4:00 PM. Candidate 4: the midpoint fill ruling covers a stop order that enters a trade. Trend build: engines follow the independent check's literal reading where the plan left a choice.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, parts of `research/`, and the voice-brief skill.
