# Candidate 3, value area traversal: the verdict

Written 2026-11-18. The same eleven markets as candidates 1 and 2, measured on 2018 to 2023 at midpoint fills. Rule: the plan's candidate 3 amendment of 2026-11-18 (`../../PLAN.md`), the "80% rule". Full tables: `MEASURE.md`.

## The answer

**Candidate 3 fails before the full run. No version is worth sending to the full test.**

- **The rule is named for 80%. Here price reached the far edge of the value area in 35% of trades.** The one published backtest found 62%. Measured at the widest stop with no reward filter, from the entry to 3:55 PM, whether or not the stop was hit first: 917 of 2,583 trades.
- The three versions with no reward-to-risk filter trade 2,583 times in six years and all lose, before costs too: 0.011 to 0.037 of the risk a trade behind before costs, 0.035 to 0.083 after.
- Asking for a planned 2 or 3 to 1 cuts the trades to between 10 and 818. The average winner stays at 0.46 to 1.25 times the risk, against 2, because most trades are closed at 3:55 PM before they reach the far edge. These versions also go 12 to 376 trading days without a trade, against 7.
- 25 of the 95 single markets and settings that trade make money.
- The nearest version: stop 0.1 of the daily range, planned reward at least 2 to 1, on the Nasdaq alone (the only market that made money in both halves at that setting). It passes the profit test, projecting to $10,117 against $9,000, on 85 trades in six years. It fails the other two. Its average winner is 1.51 times the risk, against 2, and it once went 84 trading days without a trade, against 7. It is one of 9 settings on one of 11 markets, picked after the fact.

So no version passes the gate the plan set before the run. No locked list was written, and the full test was not run.

## Why

Set-ups are common: on 64% of market-days the 9:30 price opens outside the prior session's value area. But only 24% of those set-ups become a trade, with two half-hour closes back inside by 2:30 PM. Once inside, price reaches the far edge about a third of the time. The stop sits beyond the near edge, and the entry comes only after two half-hour closes inside, so a win at the far edge is often small against the risk: the first trade below won 16 points against 25 risked. Without a filter, the average winner is 0.29 to 0.65 of the risk. With one, the trades become too few.

| Setting | Trades 2018-2023 | Win rate | Average winner vs risk | Per trade after costs | Per trade before costs | Most days with no trade |
|---|---:|---:|---:|---:|---:|---:|
| stop 0.1, no filter | 2,583 | 48% | 0.65 | -0.08 | -0.04 | 5 |
| stop 0.1, 2 to 1 | 818 | 37% | 1.16 | -0.09 | -0.03 | 12 |
| stop 0.1, 3 to 1 | 423 | 36% | 1.25 | -0.09 | -0.02 | 23 |
| stop 0.2, no filter | 2,583 | 51% | 0.46 | -0.05 | -0.02 | 5 |
| stop 0.2, 2 to 1 | 354 | 43% | 0.74 | -0.07 | -0.02 | 29 |
| stop 0.2, 3 to 1 | 116 | 37% | 0.89 | -0.09 | -0.03 | 72 |
| stop 0.4, no filter | 2,583 | 53% | 0.29 | -0.04 | -0.01 | 5 |
| stop 0.4, 2 to 1 | 63 | 38% | 0.46 | -0.10 | -0.07 | 142 |
| stop 0.4, 3 to 1 | 10 | 70% | 0.70 | +0.35 | +0.40 | 376 |

All eleven markets together. Stops are fractions of the 14-day average daily range. Per trade figures are in units of the money risked on the trade.

## The checks

- The engine (`traverse.py`) was written test first: 30 tests, all passing. 25 faults were planted in it one at a time, and every one fails a test. Three got through on the first try and were fixed: a close exactly at the far edge (a new test), the early close's worst open loss (now checked), and the first pair only (the planted fault did nothing and was replaced by a real one).
- The rule check was written by a separate agent from the amendment alone, without seeing the engine. It added 31 new tests, 119 in all, all passing. 38 faults planted in its candidate 3 rule were all caught, and 11 more in the parts it shares with candidates 1 and 2. Its eleven new readings, R28 to R38, are in `rule_check.py`. The engine already read the amendment the same way, so it needed no change.
- The agent moved some of candidates 1's and 2's check into shared parts. Both checks were then rerun on every trade: 779,621 and 470,619 trades, still clean.
- It replayed every trade of every setting, with all three fills, and the account on two sizes: 28,599 trades, no break (`check_all.json`).
- On the real Nasdaq trades of stop 0.4 with no filter (303 trades), six faults planted one at a time were each caught: an exit moved a tick, an entry moved a tick, a trade deleted, a signal stamped a minute late, a stop a tick wider, a day's set-up deleted.
- The measurement reproduces byte for byte on a second run, run alone.
- The first trade was read by hand against the raw minutes: Nasdaq, 9 January 2018, stop 0.4. The 9:30 price, 6,700.25, opened above the value area (6,669.25 to 6,689.50), so the trade is a short. The 9:30 and 10:00 half hours closed inside, at 6,673.75 and 6,685.25. The 10:30 minute opened at 6,685.50, and the sell filled at 6,685.25: the open less two ticks, held at the minute's low. The stop was 6,710.25 (0.4 of the 52.07 daily range, 20.75 points beyond the top edge). At 10:40 price traded a tick under the bottom edge, and the target filled at 6,669.25: 16 points won, against 25 risked.

## What this does not show

- Fills on 1-minute bars. The market entry fills at the next minute's open plus slippage; in a fast minute it can be worse.
- The value area is built from the whole prior session's volume, as in candidate 1. The classic rule uses the day session's time at each price. That is a different rule, and writing it now, after this result, would be choosing after the fact, so it was not tested.
- The levels are the written rule's, not Amear's hand marks. The blind marking check was not reached.
- The near miss on the Nasdaq is one setting out of 9 on one market out of 11, picked after the fact. Choosing it now would be fitting to this data.
