# Momentum into the close: the verdict

Written 2026-11-18. The eleven markets of the levels and trend passes, measured on 2018 to 2023 at midpoint fills. Rule: `../PLAN.md`, "The exact rule" and its amendment before any engine code. Full tables: `MEASURE.md`. Pre-screen: `PRESCREEN.md`.

## The answer

**Momentum into the close fails before the full run. No version is worth sending to the full test.**

- All 12 versions lose money on the eleven markets together. Every one of the 132 single markets and settings loses, and 131 of them lose even before commissions.
- The 7-day bar is met, as designed: never more than 3 days without a trade on the eleven markets.
- The bar of winners at twice the risk and the bar of profit pull against each other:
  - With a stop far enough away to survive the last half hour (0.2 of the daily range), 90% of trades reach the close, but winners average 0.39 of the risk on all markets and 0.56 on the Nasdaq.
  - With a stop near enough for big winners (0.025 of the daily range), winners average 2.25 times the risk, but 90% of trades are stopped out, and the version loses 0.63 of the risk a trade.
- The Nasdaq, the one market the published figures and the pre-screen pointed to, loses at every setting. On the rest-of-day signal, its versions with winners over twice the risk (stop 0.025 or 0.05) lose 0.26 and 0.50 of the risk a trade. Its best version (rest-of-day signal, stop 0.2) loses 0.016 of the risk a trade: about level before commissions, with winners of 0.56 the risk.
- No market made money in both halves at any setting, so no stable set exists.

So no version passes the gate the plan set before the run. No locked list was written, and the full test was not run.

## Why

The edge is real but small. Before any stop or cost, the Nasdaq's last half hour went the way of the day's move by 9.0 ticks a trade on average (`PRESCREEN.md`), against a round trip of 7.8 ticks. The half hour's ordinary swings are far larger. A stop inside those swings is hit by noise nine times in ten, and each stop costs its slippage and commission. A stop outside them turns the half hour into a small bet whose winners are a fraction of the risk. Either way the costs are larger than what is left of the edge.

| Setting (all eleven markets) | Trades 2018-2023 | Win rate | Average winner vs risk | Per trade after costs | Most days with no trade |
|---|---:|---:|---:|---:|---:|
| rest of day, stop 0.025 | 15,556 | 7.5% | 2.25 | -0.63 | 3 |
| rest of day, stop 0.05 | 15,556 | 19.1% | 1.23 | -0.42 | 3 |
| rest of day, stop 0.1 | 15,556 | 31.1% | 0.69 | -0.23 | 3 |
| rest of day, stop 0.2 | 15,556 | 35.0% | 0.39 | -0.12 | 3 |
| both signals agree, stop 0.2 | 11,988 | 34.8% | 0.37 | -0.12 | 3 |

| Setting (the Nasdaq alone) | Trades | Win rate | Average winner vs risk | Per trade after costs | Before commission |
|---|---:|---:|---:|---:|---:|
| rest of day, stop 0.025 | 1,405 | 12.5% | 4.18 | -0.50 | -0.46 |
| rest of day, stop 0.05 | 1,405 | 25.1% | 2.10 | -0.26 | -0.20 |
| rest of day, stop 0.1 | 1,405 | 40.8% | 1.08 | -0.08 | -0.03 |
| rest of day, stop 0.2 | 1,405 | 47.3% | 0.56 | -0.02 | +0.01 |

Stops are fractions of the 14-day average daily range. Per trade figures are in units of the money risked on the trade. All 12 settings and all markets are in `MEASURE.md`.

How trades end, rest of day, all eleven markets: at stop 0.025, 90.4% at the stop and 9.6% at the close; at stop 0.2, 10.2% at the stop and 89.8% at the close.

## The checks

- The engine (`closemom.py`) was written test first: 34 tests, all passing. 31 faults were planted in it one at a time, and every one fails a test. The first planting let five through (the five-minute windows, yesterday's close taken from the bar's open, the signal from its close); tests were added until all were caught.
- The pre-screen (`prescreen.py`): 19 tests, 16 planted faults all caught; its second run is byte for byte the same.
- The rule check was written by a separate agent from the plan alone, without seeing the engine or the pre-screen: 107 tests, 76 faults planted in it, all caught. Its readings C1 to C18 are in `../rule_check.py`.
- Three readings differed from the engine, and the engine and pre-screen were changed to the check's literal reading, tests first:
  - C1 and C2: a trading day is a New York weekday with minute bars in it, the plan's words. The engine had asked for a bar between the open and the close.
  - C5: "today's bars" is every bar of the day, the evening included, all of one contract with yesterday's close. The engine had checked only the bars it read. This drops the days whose evening starts a new contract.
  - C6: a side needs the signal more than a millionth of a tick away from yesterday's close.
  The pre-screen and the measurement were rerun. About 1% fewer trades; the answer did not change.
- The check replayed every trade of every setting at all three fills, and the account on two sizes: 516,900 trades and 154,161 sized trades, no break (`check_all.json`).
- On the real Nasdaq trades of rest of day, stop 0.2 (1,405 trades), nine faults planted one at a time were each caught: an exit or an entry moved a tick, a trade deleted, a trade added, a stop a tick wider, a side flipped, an entry a minute late, the worst a tick worse, yesterday's close a tick off.
- The measurement reproduces byte for byte on a second run, run alone.
- The first trade was read by hand against the raw minutes: Nasdaq, 3 January 2018, rest of day, stop 0.2.
  - **Signal.** Yesterday's close, the 4:00 PM open on 2 January, was 6,520.50. The 3:29 PM minute closed at 6,583.25, above it: a long.
  - **Entry.** The 3:30 PM minute opened at 6,583.25. With two ticks of slippage the buy is 6,583.75, the minute's high, so it stands.
  - **Stop.** The 14-day average daily range was 54.27; 0.2 of it is 10.85, rounded down to 10.75. The stop was 6,573.00. The lowest minute before 4:00 PM reached 6,580.75, so it was not hit.
  - **Exit.** The 4:00 PM minute opened at 6,583.75. Less two ticks: 6,583.25, a loss of 0.5 points. The worst point was 3.0 points down, at 3:59 PM.

## What this does not show

- Fills on 1-minute bars. The market orders at the last half hour's start and at the close fill at the minute's open plus slippage. A real order at the close can do better (a market-on-close order joins the closing price), and that alone would cut a tick or two of the 7.8. It would not turn a loss of 0.26 of the risk a trade into a profit.
- The days the paper finds the effect strongest, when option dealers are short options, cannot be picked out from our data.
