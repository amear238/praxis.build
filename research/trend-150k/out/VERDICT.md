# Trend-following on the $150,000 frame: the verdict

Written 2026-11-18. Eleven markets: the Nasdaq, S&P 500 and Russell 2000 indexes, crude oil, gold, the 10-year note, the 30-year bond, and the euro, yen, pound and Australian dollar. Micro contracts where a micro exists. Measured on 2018 to 2023, midpoint fills, plan `../PLAN.md`.

## The answer

**Neither version is good enough to send to the full test. Trend-following fails on the $150,000 frame before the final run, the same way the opening range breakout did.**

- **Same-day** (enter after the US open, flat by 3:55 PM): **none of the 72 versions makes money**, in any year from 2018 to 2023. The best loses about $6,100 over the period at the largest safe size. Its average winner is a sixth of the risk, and the best version anywhere reaches 0.62 of the risk, against the bar of 2.
- **Multi-week** (held for days or weeks, daily bars): **16 of the 36 versions make money**, but none is close to a pass. The best projects to about **$6,700** over 2018 to 2026 at the safe size, three quarters of the $9,000 bar. Its average winner is 0.66 of the risk, against the bar of 2, and it once went 20 trading days without a new trade, against the bar of 7. The ten versions that trade often enough for the seven-day bar all lose money.

So both versions fail the 2-to-1 bar in every version measured, before any later data is looked at. No locked list was written and the full test was not run: there is nothing in the measurements that could pass it.

## Why

- **Same-day.** The trend over the past weeks says almost nothing about the next six hours. Win rates sit at 46 to 47%, winners and losers are the same size, and costs make every version lose. A stop set from the daily range is rarely reached inside one session, so most trades end at 3:55 PM with a small gain or loss: winners cannot grow to twice the risk. Only the Nasdaq on its own made money, in 16 of the 72 versions.
- **Multi-week.** A real but small edge. It wins about a third of the time, and the opposite signal closes most trades before the trailing stop does. The average winner stays under the risk. The edge also comes and goes by year: about +26, -12, +30, -6, +12 and 0 times the risk in 2018 to 2023 for the best version. And with eleven markets open at once, losing days stack up, so the $4,500 limit allows only about $91 of risk a trade.

## The nearest versions

| Version | Trades | Win rate | Average winner vs risk | Longest losing run | Most days with no new trade | Safe risk a trade | Projected profit 2018-2026 | Against $9,000 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multi-week: 60-day trend, stop 4 times the daily range, trail 2 times the stop | 949 | 34% | 0.66 | 18 | 20 | $91 | $6,738 | 0.75 |
| Multi-week: 60-day trend, stop 3 times, trail 2 times | 1,000 | 35% | 0.80 | 18 | 16 | $70 | $5,556 | 0.62 |
| Multi-week: 120-day trend, stop 4 times, trail 2 times | 700 | 34% | 0.72 | 21 | 28 | $94 | $4,736 | 0.53 |
| Same-day: 60-day trend, 9:35 entry, stop 2 times the daily range, trail 1 time | 17,025 | 47% | 0.16 | 20 | 0 | $17 | -$6,087 | - |

Safe risk a trade: the most that keeps the $4,500 limit crossed in no more than 1 in 40 shuffles of the 2018 to 2023 days. Full tables: `MEASURE.md`.

## The checks

- The data reader and both engines were written test first (39 tests), and so was the measuring pass (8 tests).
- The rule check was written by a separate agent from the plan alone, without seeing the engines (38 tests). Run against real trades, it found three faults in the engines, all fixed and tested:
  - A touch of the stop that differed by a rounding speck was read as a miss. Found on the euro, October 2018; it kept trades open days too long.
  - A market with no bar that day (Good Friday) was marked at the day before's low. This made the results look worse than they were, not better.
  - Three small mismatches with the plan's literal wording on the last bar and on holiday early closes.
- It found one fault in itself, also fixed and tested: on a holiday early close it held the trade until the evening reopen, past the plan's 4 PM.
- After the fixes, all 108 measured settings were replayed with no break (`check_all.json`). The measurement reproduces byte for byte on a second run.
- Trades were read by hand: the first multi-week Nasdaq trade and a week of same-day S&P trades, against the raw bars.

## What this does not show

- Fills on 1-minute and daily bars look better than live, so the real result would be a little worse, not better.
- The multi-week version cannot run on MyFundedFutures, which closes every position by 4:10 PM. A pass would have shown an edge, not a tradable account.
- The grids were the plan's, fixed before any result. A faster exit, a different signal or a different market list was not tried, and trying them now would be fitting to this data.
