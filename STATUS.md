# PRAXIS status

Last updated: 2026-11-18.

## The goal

One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets.

Work that does not move toward that is frozen: MyFundedFutures follow-up, the Hermes timer, the project kit, extras on the Windows machine.

## What is done

- The signal path from a signal file to a NinjaTrader order was built and signed off on sim earlier in the year.
- The restructure of 2026-11-15: the old agent chain and its files are in `archive/2026-11-15/`, unchanged. One session does the work. Tests are the check.
- Data (2026-11-17): Databento, eleven markets, 1-minute bars from 2018 and daily bars from 2010. Charged $122.99 (Amear confirmed the bill on 2026-11-18), inside the $125 free credit, so none of his money. Saved, not committed, in `market-data/databento`. NQ matches the NinjaTrader file; all 729 rolls joined.

**Every candidate so far has failed the five bars on the $150,000 MyFundedFutures frame** ($4,500 end-of-day trailing limit, $9,000 target, midpoint fills):

| Strategy | Result | Verdict |
|---|---|---|
| Noise-Area, 12 variations at 3 sizes (2026-11-17) | none of 36 passes; nearest: $8,600 profit and 26 days with no trade | `research/noise-area-variations/out/150k/VERDICT.md` |
| Opening range breakout, 108 versions (2026-11-17) | none worth a final run; safe size about $61 a trade | `research/orb-150k/out/VERDICT.md` |
| Session sweep, Amear's pasted idea (2026-11-17) | loses about $0.16 per $1 risked after costs | `research/session-sweep/` |
| **Trend-following, 11 markets, same-day and multi-week (2026-11-18)** | **neither worth a final run.** Same-day: 0 of 72 versions make money. Multi-week: best projects to $6,738 against $9,000, average winner 0.66 of the risk against 2; every version meeting the seven-day bar loses | `research/trend-150k/out/VERDICT.md` |

The trend build's checks: a rule check written by a separate agent from the plan alone found three faults in the engines and one in itself, all fixed test first. It then replayed all 108 measured settings with no break (about 1.29 million trades). The measurement reproduces byte for byte. 113 tests across the folder.

Earlier, on the $50,000 stand-in: none of Noise-Area's twelve passed; candidate 1 and four variations, none passed.

## What is running

Nothing.

## What is next, in order

1. A fresh research pass for the next candidate (task `Praxis_build-8h5`). Decided without waiting, reversible: four families have now failed on the same frame. The common squeeze is that winners at least twice the risk come with long losing runs, and the $4,500 limit then allows too little size to reach $9,000. So the pass looks for published records where the profit is large compared with the losing runs, after costs, on any of the eleven markets already bought. Under the 2026-11-17 ruling, AI-made decisions are allowed if backtested the same way.
2. Before any final run on micros: confirm MyFundedFutures lists every micro used.
3. Results for the stop-distance versions and candidates 2 to 4 sit on worktree branches not merged into main.

## What waits on Amear

1. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible (2026-11-18, trend build): where the plan's words left a choice, the engines follow the independent check's literal reading. The last bar of the data and a holiday early close are at the close with no slippage. The day's worst open loss counts the whole minute in which the stop fills.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, parts of `research/`, and the voice-brief skill.
