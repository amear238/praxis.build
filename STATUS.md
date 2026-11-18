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

Candidate 1's checks: a rule check written by a separate agent from the plan alone (71 tests) set 20 literal readings; the engine adopted them test first, and the check then replayed 779,621 trades with no break. The measurement reproduces byte for byte. Published record searched first: no level method shows profit after costs (`research/levels-150k/PLAN.md`).

Earlier, on the $50,000 stand-in: none of Noise-Area's twelve passed; candidate 1 and four variations, none passed.

## What is running

Nothing. Candidate 2's measuring pass ran once: no version passes the gate (`research/levels-150k/out/c2/MEASURE.md`; draft verdict beside it, not yet committed). Its independent rule check is written and merged (88 tests). Two runs were stopped by Claude Code for low memory on 2026-11-18, because they ran at the same time: the check against every candidate 2 trade (`check_all.py 2`) and the second measuring run for the byte-for-byte comparison. Run them one at a time, then commit the verdict.

## What is next, in order

1. **The widened research pass** (task `Praxis_build-8h5`; ruling in `RULINGS.md`, "His own chart marking, automated execution"). Plan with the bars locked: `research/levels-150k/PLAN.md`. The candidates, in the order fixed before any result, one at a time:
   - 1, fade the first touch of a marked level: failed (above).
   - **2, break and retest**: a level closed through on the 15-minute chart, then the first return to it, traded with the break. Exact rule in the plan's amendment; engine `retest.py`. Measured once: no version passes the gate. **Next session, one job at a time (two at once ran the machine out of memory):** (a) `python3 -I -B research/levels-150k/check_all.py 2`, which must print clean; (b) copy `research/levels-150k/out/c2/measure.json` aside, rerun `measure.py 2`, compare the two byte for byte; (c) fill the checks section of `out/c2/VERDICT.md` (a draft) and commit.
   - 3, value area traversal (the "80% rule"); 4, acceleration through a level. Each one's exact rule is written into the plan only after the one before fails. Outline for 3, to be fixed in the amendment: P0 a tick outside the prior session's value area; two consecutive 30-minute closes inside it, the second bar starting by 2:00 PM; market entry at the next minute toward the far edge; stop d beyond the near edge; target the far edge; grid k 0.1, 0.2, 0.4 x a minimum planned reward-to-risk of 0, 2 or 3. The same separate agent extends `rule_check.py` from the amendment alone.
   - A version that passes the gate goes on a locked list (at most 12), then the full run 2018 to 2026 on the five bars, then Amear's blind marking check: 40 past market-days, charts cut at 9:30, his marks against the rule's. His marks drive orders only if they match at 80% both ways; otherwise the rule's levels do.
2. Before any final run on micros: confirm MyFundedFutures lists every micro used.
3. Results for the stop-distance versions and candidates 2 to 4 of the old shortlist sit on worktree branches not merged into main.

## What waits on Amear

1. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible (2026-11-18, his ruling): "mark out the charts or spreads" is read as marking levels on price charts. Trading one market against another (a spread) is not in the pass unless he says so.

Decided without waiting, reversible (2026-11-18, trend build): where the plan's words left a choice, the engines follow the independent check's literal reading. The last bar of the data and a holiday early close are at the close with no slippage. The day's worst open loss counts the whole minute in which the stop fills.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, parts of `research/`, and the voice-brief skill.
