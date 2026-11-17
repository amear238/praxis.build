# Trend-following on the $150,000 frame: the plan

Written 2026-11-17, before any trend code or result. Amear's rulings of 2026-11-17 (RULINGS.md): test the trend-follower on the $150,000 account; markets beyond NQ are allowed where they can be backtested; two versions side by side, same-day and multi-week; data bought from Databento (the broad set).

## The bars (unchanged from the Noise-Area and opening range runs; not moved to fit a result)

Each version is judged on all five, reported separately, never blended:

1. Every simulated order matches the version's written rule (an independent replay, zero breaks).
2. The average winning trade is at least twice the money risked on it, and the version makes a profit on 2024-01-01 onward alone.
3. Never more than seven trading days without a new trade (counted on the whole portfolio of markets).
4. Net profit at least $9,000.
5. The $4,500 end-of-day trailing limit crossed in at most 5% of 10,000 shuffles (seed 20261115).

Fills: midpoint stop fills judged (as ruled 2026-11-17), kind and harsh reported beside. Every market order: 1 tick of slippage per side on the currencies and the 10-year note; 2 ticks on everything else.

## Data

- Databento CME, volume-ranked front month. 1-minute bars 2018-01-01 to 2026-11-15 (eleven markets); daily bars front and second month 2010-06-06 to 2026-11-15. Saved, not committed, in `market-data/databento`.
- Rolls. The daily series is back-adjusted by adding the front-to-second gap on each roll day (the day the front contract changes), so a roll is not a fake move. Signals are computed on the adjusted series. Fills and stops are on the actual contract's prices.
- Russell 2000 starts in mid-2017 (CME relisted it then).
- Days Databento marks as reduced quality are listed in the measuring report. They are kept unless a check shows broken bars.

## Instruments (traded as micros where a micro exists, so size can be fine-grained)

| Market | Traded as | Dollars a point | Tick | Commission a contract, round trip |
|---|---|---:|---:|---:|
| Nasdaq 100 | MNQ | 2 | 0.25 | 1.90 |
| S&P 500 | MES | 5 | 0.25 | 1.90 |
| Russell 2000 | M2K | 5 | 0.10 | 1.90 |
| Crude oil | MCL | 100 | 0.01 | 1.90 |
| Gold | MGC | 10 | 0.10 | 1.90 |
| 10-year note | ZN | 1,000 | 1/64 | 5.00 |
| 30-year bond | ZB | 1,000 | 1/32 | 5.00 |
| Euro | M6E | 12,500 | 0.0001 | 1.90 |
| Yen | MJY | 1,250,000 | 0.000001 | 1.90 |
| Pound | M6B | 6,250 | 0.0001 | 1.90 |
| Aussie dollar | M6A | 10,000 | 0.0001 | 1.90 |

Choice: commissions are the conservative round figure used before for MNQ. ZN and ZB have no micro, so their size is coarse. To check before the final run: that MyFundedFutures lists every one of these micros (its list was read only second-hand on 2026-11-17).

## The two versions

Both have the same core: **the direction of the recent trend sets the side, a stop-market order rests at entry, sized so a stop-out costs the set risk, and a trailing stop lets winners run.**

**A. Same-day.** For each market, each trading day:
- Side: the sign of the back-adjusted close-to-close return over the lookback L, known at the prior day's close. Long if up, short if down.
- Entry: at a fixed time after the US open (the first bar stamped 09:35 ET, or 10:00 ET in the measuring pass), next-bar open, slippage against.
- Stop: a set multiple of the market's average daily range (14 prior days), resting at entry.
- Exit: the trailing stop, or flat at 15:55 ET. One trade per market a day at most. Nothing held past 16:00 ET, so MyFundedFutures' 4:10 PM close never acts.

**B. Multi-week.** On daily bars:
- Side: the sign of the return over the lookback L, read at each day's close.
- Entry: at the next day's open when the side changes, or when a stopped-out market's signal is still on after a wait of one day.
- Stop: a set multiple of the average daily range, resting at entry. It trails as the position runs (it only moves toward the price) and is checked on each day's high and low. A gap through the stop fills at the open.
- Exit: the stop, or the opposite signal (close at the next open).
- Held overnight. As Amear chose, it is judged on the $150,000 numbers even though MyFundedFutures would not allow it. The report says so on its first line.

**Portfolio and risk, both versions.** All markets run at once. Each trade risks the set percentage of the account's realised balance, split equally across the markets with a position open or opening. Choice: risk per trade is in dollars at the contract size. Size is rounded down to whole contracts, and a trade needing less than one contract is skipped and listed.

**Shuffles.** Positions overlap across markets, so the shuffle test reorders whole days of portfolio profit and loss, not single trades. Choice, made before the run: day order, 10,000 shuffles, the same seed.

## How the search runs (the same method as the last two)

1. Measuring pass on 2018-01-01 to 2023-12-31 only, at fixed small size: the lookback L (20, 60, 120, 250 days), the stop multiple (0.5, 1, 2 average daily ranges for A; 2, 3, 4 for B), the trail (0.5, 1, 2 times the stop distance), per market and for the portfolio. Report trades, win rate, average winner against risk, longest losing run, and profit by year.
2. A locked list of at most 12 versions per kind, written before the full run. Each risk size is set from the measuring pass's losing runs so the limit has margin.
3. Full run 2018 to 2026 (B also from 2010 on daily data), the five bars, side by side, plain English, dollars.
4. Checks: the engine written test-first; a separate rule check written from this plan, not the engine; two identical runs; trades read by hand.

## What this cannot show

- 1-minute and daily bars make fills look better than live, more so for stops on daily bars (B).
- Version B is not tradable on MyFundedFutures as it stands; a pass would mean the edge exists, not that the account can run it.
- The data starts in 2018 for A. That covers before Covid, the crash, the 2022 rate shock and now, but not a long history.
