# Candidate 2, break and retest: the verdict

Written 2026-11-18. The same eleven markets, levels and grid as candidate 1, measured on 2018 to 2023 at midpoint fills. Rule: the plan's amendment of 2026-11-18 (`../../PLAN.md`). Full tables: `MEASURE.md`.

## The answer

**Candidate 2 fails before the full run. No version is worth sending to the full test.**

- All 72 versions lose money on the eleven markets together. Before costs, three come out slightly ahead, the best by 0.02 of the risk a trade, and costs take all of it.
- The 14 versions whose average winner reaches twice the risk (the tightest stop, with the far target or none) win 21 to 23% of trades and lose 0.20 to 0.25 of the risk a trade.
- 98 of 792 single markets and settings make money, about 1 in 8, more than candidate 1's 1 in 23. The edge, where there is one, is small and patchy.
- The nearest version: all seven kinds at once, stop 0.2 of the daily range, target 5 times the risk, on the Nasdaq alone (the only market that made money in both halves at that setting). It fails all three tests of the gate, narrowly. Its average winner is 1.65 times the risk, against 2. It once went 8 trading days without a trade, against 7. It projects to $8,403, against $9,000. Its profit is uneven: in units of the risk, +19, -8 and -11 in 2018 to 2020, then +43, +35 and +5.

So no version passes the gate the plan set before the run. No locked list was written, and the full test was not run.

## Why

Trading with the break, rather than against the level, removed most of candidate 1's loss: before costs, every kind of level comes out near zero instead of 0.10 to 0.13 of the risk behind. But near zero is all it is. Winners large enough for the 2-to-1 bar come only with tight stops, and tight stops are mostly hit: about one trade in five wins. With the wider stops, about 45% win, but the average winner is only 0.6 of the risk, because most trades end at the 3:55 PM close before a target is reached.

| Kind of level | Best setting | Trades 2018-2023 | Win rate | Average winner vs risk | Per trade after costs | Per trade before costs | Most days with no trade |
|---|---|---:|---:|---:|---:|---:|---:|
| Prior day high and low | stop 0.4 x daily range, target 3 | 1,140 | 45% | 0.63 | -0.05 | -0.02 | 14 |
| Overnight high and low | stop 0.4, target 3 | 997 | 46% | 0.63 | -0.04 | -0.01 | 15 |
| Prior week high and low | stop 0.2, target 5 | 1,394 | 38% | 1.19 | -0.06 | -0.01 | 8 |
| Hourly swing highs and lows | stop 0.4, target 3 | 1,838 | 46% | 0.65 | -0.01 | +0.02 | 9 |
| Round numbers | stop 0.4, target 3 | 2,241 | 45% | 0.63 | -0.04 | -0.01 | 9 |
| Prior session volume levels | stop 0.4, target 3 | 1,269 | 45% | 0.61 | -0.04 | -0.01 | 13 |
| Supply and demand zones | stop 0.2, target 3 | 59 | 41% | 1.02 | -0.05 | -0.02 | 109 |
| All seven at once | stop 0.4, target 3 | 3,839 | 45% | 0.63 | -0.03 | 0.00 | 5 |

Per trade figures are in units of the money risked on the trade.

## The checks

(Filled in after the independent rule check.)

## What this does not show

- Fills on 1-minute bars; the retest limit fills only when price trades a tick through the level.
- The levels are the written rule's, not Amear's hand marks. The blind marking check was not reached.
- The near miss on the Nasdaq is one setting out of 72 on one market out of eleven, picked after the fact. Choosing it now would be fitting to this data; the gate was set so that does not happen.
