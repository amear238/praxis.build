# Candidate 4, acceleration through a level: the verdict

Written 2026-11-18. The same eleven markets as candidates 1 to 3, measured on 2018 to 2023 at midpoint fills. Rule: the plan's candidate 4 amendment of 2026-11-18 (`../../PLAN.md`). Full tables: `MEASURE.md`.

## The answer

**Candidate 4 fails before the full run. No version is worth sending to the full test.** It was the last of the four candidates the plan fixed before any result, so the marked-levels pass is finished.

- 23 of the 24 versions lose money on the eleven markets together, and 23 of 24 lose even before costs: 0.03 to 0.13 of the risk a trade behind after costs.
- The target is three times the risk, but the average winner is 0.46 to 1.17 times the risk, against the bar of 2. Only 2.4% of trades reach the target (all kinds at once, stop 0.2). Two in three are closed at 3:55 PM.
- The one version that makes money on all eleven markets (supply and demand zones, stop 0.2) has 73 trades in six years: 3.5 times the risk in all, with winners of 0.76 the risk, and 105 trading days without a trade, against 7.
- 36 of the 260 single markets and settings that trade make money.
- The nearest versions are on the Nasdaq alone, the market that made money in both halves at those settings. Each passes one test and fails two:
  - All kinds at once, stop 0.2: never more than 7 days without a trade, but winners average 1.03 times the risk, and it projects to $8,005 against $9,000.
  - Round numbers, stop 0.2: projects to $10,306, but winners average 1.02 times the risk, and it once went 17 days without a trade.

  Both are a setting and a market picked after the fact.

So no version passes the gate the plan set before the run. No locked list was written, and the full test was not run.

## Why

A level breaks often: at stop 0.2, 11% of the armed prior-day levels become a trade, and 6% with all kinds at once. But price does not then run far enough. The stop sits beyond the level, and the order to enter waits one tick beyond the break bar's high (low for a short). So by the time the entry fills, a third of the risk is already used: on average 0.34 of the risk lies between the level and the trigger, and 0.04 more between the trigger and the midpoint fill. A target three times the risk from there is far. Most trades end at 3:55 PM, ahead by less than the risk, or at the stop.

| Setting | Trades 2018-2023 | Win rate | Average winner vs risk | Per trade after costs | Per trade before costs | Most days with no trade |
|---|---:|---:|---:|---:|---:|---:|
| all kinds, stop 0.1 | 13,476 | 36% | 1.15 | -0.12 | -0.08 | 1 |
| all kinds, stop 0.2 | 9,048 | 42% | 0.77 | -0.06 | -0.03 | 1 |
| all kinds, stop 0.4 | 4,065 | 44% | 0.48 | -0.04 | -0.02 | 5 |
| prior day, stop 0.2 | 2,984 | 43% | 0.74 | -0.06 | -0.02 | 5 |
| round numbers, stop 0.2 | 4,873 | 42% | 0.78 | -0.06 | -0.03 | 4 |
| zones, stop 0.2 | 73 | 47% | 0.76 | +0.05 | +0.08 | 105 |

All eleven markets together. Stops are fractions of the 14-day average daily range. Per trade figures are in units of the money risked on the trade. All 24 settings are in `MEASURE.md`.

How trades end, all kinds at once, stop 0.2 (9,048 trades): 2.4% at the target, 30.3% at the stop, 67.3% closed at 3:55 PM. Of the 3,816 winners, 5.7% reached the target.

## The checks

- The engine (`accel.py`) was written test first: 24 tests, all passing. 34 faults were planted in it one at a time, and every one fails a test.
- The rule check was written by a separate agent from the amendment alone, without seeing the engine. It added 31 tests, 150 in all, all passing. 37 faults planted in its candidate 4 rule were all caught, and 6 more in the break code it moved into a shared part. Its readings R39 to R52 are in `rule_check.py`.
- One reading differed from the engine, R40: "one tick above the break bar's high" is the raw high plus a tick, never rounded to the tick grid. The euro, yen and Australian dollar data sit half a tick off the grid at times, so the two readings gave different triggers there. The engine was changed to the check's literal reading, with a new test and a new planted fault. The measurement was rerun; only those three markets moved, by small amounts, and the answer did not change.
- The check replayed every trade of every setting, with all three fills on the all-kinds settings, and the account on two sizes: 141,289 trades, no break (`check_all.json`).
- The agent moved some of candidate 2's check into a shared part, so candidates 1's and 2's checks were rerun on every trade: 779,621 and 470,619 trades, still clean and unchanged.
- On the real Nasdaq trades of prior day, stop 0.2 (382 trades), seven faults planted one at a time were each caught: an exit moved a tick, an entry moved a tick, a trade deleted, a break stamped a minute late, a trigger a tick further, a stop a tick wider, an armed level deleted.
- The measurement reproduces byte for byte on a second run, run alone, both before and after the change to the trigger.
- The first trade was read by hand against the raw minutes: Nasdaq, 12 January 2018, prior day, stop 0.2.
  - **Set-up.** The 9:30 price, 6,709.50, was below the prior day's high of 6,728.75. That high was armed for a long on a break up, with the stop 10.50 points below it at 6,718.25: 0.2 of the 53.46 daily range, rounded down to the tick.
  - **Break.** The 9:30 and 9:45 quarter hours closed below 6,729.00, one tick above the level. The 10:00 quarter hour closed at 6,732.00. Its highest minute reached 6,733.00, at 10:08, so the trigger was 6,733.25.
  - **Entry.** At 10:15 price traded up to 6,736.00. The buy filled at 6,734.75: halfway between the trigger and that high, rounded up to the tick.
  - **Exit.** The risk was 16.50 points and the target 6,784.25. The target was not reached. At 3:55 PM the trade closed at 6,770.00, the 6,770.50 open less two ticks: 35.25 points won, about 2.1 times the risk.

## What this does not show

- Fills on 1-minute bars. The entry stop fills at the midpoint between its price and the minute's extreme, the fill Amear ruled for stops, read here as covering a stop that enters. In a fast break the real fill can be worse.
- Cancelling the entry when price reaches the stop first needs an order rule the signal path does not have yet. It did not matter here, as no version passed.
- The levels are the written rule's, not Amear's hand marks. The blind marking check was not reached.
- The near misses on the Nasdaq are 2 of 24 settings on one market of 11, picked after the fact. Choosing them now would be fitting to this data.
