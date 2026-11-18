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
| Trend-following, 11 markets, same-day and multi-week (2026-11-18) | neither worth a final run. Same-day: 0 of 72 versions make money. Multi-week: best projects to $6,738 against $9,000, average winner 0.66 of the risk against 2 | `research/trend-150k/out/VERDICT.md` |
| **Marked levels, candidate 1: fade the first touch (2026-11-18)** | **fails before the full run.** Seven kinds of level (prior day, overnight, prior week, hourly swings, round numbers, volume levels, supply and demand zones) and all at once, 72 versions on 11 markets: every one loses, even before costs. Price kept going through levels more often than it bounced | `research/levels-150k/out/VERDICT.md` |
| **Marked levels, candidate 2: break and retest (2026-11-18)** | **fails before the full run.** All 72 versions lose on the eleven markets together; before costs the best is 0.02 of the risk a trade ahead, and costs take it. The nearest (all kinds, Nasdaq alone) misses all three tests narrowly: average winner 1.65 of the risk against 2, 8 days with no trade against 7, $8,403 against $9,000 | `research/levels-150k/out/c2/VERDICT.md` |
| **Marked levels, candidate 3: value area traversal, the "80% rule" (2026-11-18)** | **fails before the full run.** Price reached the far edge in 35% of trades, not 80%. The 3 versions with no filter lose, before costs too; asking for 2 or 3 to 1 leaves winners at 0.46 to 1.25 of the risk and weeks with no trade. Nearest (Nasdaq alone): $10,117 projected, but winners 1.51 of the risk and 84 days with no trade | `research/levels-150k/out/c3/VERDICT.md` |
| **Marked levels, candidate 4: acceleration through a level (2026-11-18)** | **fails before the full run.** A stop order one tick past the 15-minute bar that closes through a level, target 3 times the risk: 23 of 24 versions lose, even before costs; only 2.4% of trades reach the target, two in three close at 3:55 PM, winners 0.46 to 1.17 of the risk. Nearest (all kinds, Nasdaq alone): 7 days with no trade, but winners 1.03 of the risk and $8,005 | `research/levels-150k/out/c4/VERDICT.md` |

Checks on candidates 1 to 4: each rule check was written by a separate agent from the plan alone. The checks replayed every trade with no break: 779,621 trades for candidate 1, 470,619 for 2, 28,599 for 3, 141,289 for 4. Every measurement reproduces byte for byte, and planted faults in real trades were caught. Published record searched first: no level method shows profit after costs (`research/levels-150k/PLAN.md`).

Earlier, on the $50,000 stand-in: none of Noise-Area's twelve passed; candidate 1 and four variations, none passed.

## What is running

Nothing. Run the heavy jobs one at a time: two at once ran the machine out of memory on 2026-11-18. One alone peaks near 6 GB.

## What is next, in order

1. **The widened research pass** (task `Praxis_build-8h5`; ruling in `RULINGS.md`, "His own chart marking, automated execution"). The marked-levels plan is finished: all four candidates, fixed in order before any result, failed at the gate (`research/levels-150k/PLAN.md`). The blind marking check was never reached, because no version passed.
   - **Next: choose the next family before any code.** In all four level candidates and in trend-following, the versions that trade often enough for the 7-day bar win on average less than twice the risk. A written search of the published record comes first, for a method with profit after costs that can meet all three gate bars at once. One option already on the task list, parked in the old agent chain with a design but no code: the drift before scheduled announcements (task `Praxis_build-ckh`). Alone it trades too rarely for the 7-day bar.
2. Before any final run on micros: confirm MyFundedFutures lists every micro used.
3. Results for the stop-distance versions and candidates 2 to 4 of the old shortlist sit on worktree branches not merged into main.

## What waits on Amear

1. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible (2026-11-18, his ruling): "mark out the charts or spreads" is read as marking levels on price charts. Trading one market against another (a spread) is not in the pass unless he says so.

Decided without waiting, reversible (2026-11-18, candidate 4): his midpoint fill ruling ("the average one, which is in between") is read as covering a stop order that enters a trade, not only one that exits.

Decided without waiting, reversible (2026-11-18, trend build): where the plan's words left a choice, the engines follow the independent check's literal reading. The last bar of the data and a holiday early close are at the close with no slippage. The day's worst open loss counts the whole minute in which the stop fills.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, parts of `research/`, and the voice-brief skill.
