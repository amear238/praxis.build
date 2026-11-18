# Candidate 1, fading the first touch of a marked level: the verdict

Written 2026-11-18. Eleven markets, micro contracts where a micro exists, measured on 2018 to 2023 at midpoint fills, plan `../PLAN.md`. Full tables: `MEASURE.md`.

## The answer

**Candidate 1 fails before the full run. No version is worth sending to the full test.**

- All 72 versions lose money on the eleven markets together, and all 72 lose even before costs. The best loses 0.03 of the risk a trade after costs.
- The 14 versions whose average winner reaches twice the risk (the tightest stop, with the far target or none) are among the worst: they win 18 to 20% of trades and lose 0.29 to 0.38 of the risk a trade.
- Across 792 single markets and settings, 35 make money, about 1 in 23. Losing versions throw up a few winners like that by chance.
- The only versions that made money in both 2018-2020 and 2021-2023 are supply and demand zones on the Nasdaq and S&P 500. They traded about 50 times in six years and once went 199 trading days without a trade, against the bar of 7. The best projects to $7,000 at the safe size, against $9,000, and its average winner is 1.8 times the risk.

So no version passes the gate the plan set before the run. No locked list was written, and the full test was not run.

## Why

Price did not bounce at marked levels. Once it traded a tick through a level, it more often kept going. With all seven kinds at once, the tightest stop and a target three times the risk (2018 to 2023, where the 3:55 PM close cuts the fewest trades short), stops were hit 4.4 times as often as targets: 22,927 against 5,210. With no edge it would be about 3 times. Before costs every kind of level lost 0.10 to 0.13 of the risk a trade at its best setting. That fits the published finding that prices speed up once through a level (Osler, 2003), and the intraday momentum studies. It does not fit the bounce findings, which come from currency dealers' order books and stock data, not from futures with a resting order at the level.

| Kind of level | Best setting | Trades 2018-2023 | Win rate | Average winner vs risk | Per trade after costs | Per trade before costs | Most days with no trade |
|---|---|---:|---:|---:|---:|---:|---:|
| Prior day high and low | stop 0.4 x daily range, target 3 | 1,938 | 40% | 0.66 | -0.15 | -0.13 | 8 |
| Overnight high and low | stop 0.4, no target | 1,710 | 40% | 0.66 | -0.15 | -0.12 | 10 |
| Prior week high and low | stop 0.4, no target | 1,131 | 41% | 0.63 | -0.14 | -0.12 | 10 |
| Hourly swing highs and lows | stop 0.4, no target | 3,204 | 39% | 0.65 | -0.15 | -0.13 | 9 |
| Round numbers | stop 0.4, target 3 | 3,881 | 40% | 0.67 | -0.12 | -0.10 | 9 |
| Prior session volume levels | stop 0.4, no target | 2,189 | 41% | 0.65 | -0.12 | -0.10 | 6 |
| Supply and demand zones | stop 0.4, target 3 | 73 | 48% | 0.54 | -0.03 | -0.01 | 137 |
| All seven at once | stop 0.4, no target | 6,684 | 40% | 0.66 | -0.13 | -0.11 | 3 |

Per trade figures are in units of the money risked on the trade.

## The checks

- The level drawing, the trading and the measuring pass were written test first (29 + 32 + 7 tests). Every rule's test was seen to fail on a fault planted on purpose.
- The rule check was written by a separate agent from the plan alone, without seeing the engine (71 tests, 40 planted faults all caught). Where the plan's words left a choice it wrote down its literal reading (20 of them, in `rule_check.py`). The engine was then made to follow them, each change test first: half ticks round up, contracts are joined by the first rolls after a minute, hourly bars are UTC hours, swings need 5 prior days and zones 10, volume is split exactly, a tie between two levels in one minute goes to the one nearer the 9:30 price, contract counts are exact.
- It then replayed every trade of every measured setting, 779,621 trades with the kind and harsh fills on all-kinds-at-once, and the account on two sizes: no break (`check_all.json`). Corrupting one real trade's exit by a tick, deleting a trade, or deleting an armed level was each caught.
- The measurement reproduces byte for byte on a second run.
- The first trade (Nasdaq, 2 January 2018, short at the 6,500 round number) was read by hand against the raw minutes.

## What this does not show

- Fills on 1-minute bars; a limit order fills only when price trades a tick through it, which is the fair live assumption and also the one that favours continuation.
- The levels are the written rule's, not Amear's hand marks. The blind marking check was not reached, because no version passed.
- A speed check before the measuring pass ran two settings on the Nasdaq over 2018 to 2026, so it saw the held-back 2024 to 2026 data. Both lost. Nothing was chosen from it.
