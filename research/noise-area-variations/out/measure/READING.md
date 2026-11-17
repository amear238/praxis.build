# Reading the measuring pass

Written by the lead before any variation was chosen. Period: 2021-03-08 to 2023-12-31. No trades were placed. The figures come from `tables.md` and from the breakout files beside it (`events-*.json`), which are the same measuring pass. No variation is named here.

How to read the numbers: "risk" is the distance from the entry to the stop. A result of 2 means price moved twice that distance in favour. "Held to the close" means the breakout is kept until 4 PM unless the stop is hit first. Where a figure is "after costs", 2 ticks of slippage each way and the commission have been taken off. On the $50,000 stand-in account, 1% risk is $500 a trade and 0.25% is $125.

## Where breakouts pay

**The original band (built from the 9:30 AM open), checked on the half hour, with the stop half the band's width away.** This is the strongest cell in the whole pass.

- 607 breakouts in about 700 trading days, a little under one a day.
- 31% reached twice the risk, 23% reached three times, 11% reached five times.
- Held to the close: 37% end as winners, the average winner is 2.6 times the risk, and the average over all of them is +0.33 of the risk after costs.
- Morning breakouts (9:30 to 11:30) are the best part: 38% reach twice the risk, the average winner is 4.2 times the risk, and the average is +0.42 after costs. Only 28% end as winners.
- Buys do better than sells: +0.49 against +0.16 after costs over the whole day.
- The longest stretch with no breakout is exactly 7 trading days for both sides together over the whole day. It is 14 for buys alone, 18 for sells alone, and 10 for the morning alone.

**The tighter the stop, the better the result in multiples of the risk.** Same band, same half-hour breakouts, whole day, after costs: stop at the opposite band +0.05, stop back at the day's open +0.08, stop a full band width away +0.16, stop half a band width away +0.33. With the wider stops the average winner held to the close is under twice the risk (1.3 for a full width, 0.8 for the open, 0.4 for the opposite band), so they cannot meet the 2-to-1 bar.

## Where they do not

- **The same band checked every minute.** Five times as many breakouts (3,006 with a usable half-width stop), but the average is +0.06 after costs. In the morning 82% are stopped out. The half-hour wait filters out most of the false starts.
- **Midday and afternoon breakouts rarely run far.** With the half-width stop, 24% of midday and 15% of afternoon breakouts reach twice the risk; with a full-width stop almost none do. They still end slightly positive on average when held to the close.
- **The 6 PM band, overnight (2 AM to 9:30 AM).** About 30% reach twice the risk, but held to the close the average is zero or negative after costs on every stop tried.
- **The 6 PM band, evening (6 PM to 2 AM).** Checked every minute with the half-width stop it shows +0.38 after costs, but the shape is a lottery: 89% are stopped out and the 11% that win average 13 times the risk. Half of all evening breakouts are left out because the stop would be under 10 points. Checked on the half hour the edge disappears (+0.04).
- **The 6 PM band during the day.** Morning buys show +0.37 (134 breakouts); sells and every other daytime cell are near zero.

## Frequency

The seven-trading-day rule is met only by taking both sides over the whole day:

| Band and check | Stop | Whole day, both sides | Best single part of the day |
|---|---|---:|---:|
| 9:30 AM band, half hour | half width | 7 days | morning: 10 days |
| 9:30 AM band, every minute | half width | 6 days | morning: 8 days |
| 6 PM band, half hour | half width | 3 days | overnight: 7 days |
| 6 PM band, every minute | half width | 2 days | overnight: 6 days; evening: 17 days |

No single part of the day on the 9:30 AM band, and no single side, stays inside seven days. The evening alone does not either once the too-tight stops are left out.

## Stop distances in points, and what they mean for size

One micro contract loses $2 a point. With the half-width stop on the 9:30 AM band (half hour), the stop is typically 34 points away over the whole day (28 in the morning); one in ten is over 62 points.

- At $125 of risk a trade (0.25%), one contract fits when the stop is up to 61 points: about 11% of breakouts would be skipped.
- At $100 (0.2%), up to 48 points: about 25% skipped.
- At $250 (0.5%), up to 123 points: almost none skipped.

A skipped breakout is not an entry, so a small risk figure costs frequency. A tighter stop needs fewer dollars a contract.

## What this means for the bars

- **2-to-1.** Only the half-width stop (or tighter) on the 9:30 AM band shows an average winner above twice the risk together with a positive result after costs.
- **Survival.** With about 6 in 10 breakouts losing, runs of 10 to 15 losers in a row are to be expected over five years. The $2,000 limit is 4 losers at $500 a trade and 16 at $125. Survival will be decided mostly by the risk percentage and by how many trades a day are allowed.
- **Frequency and survival pull against each other**: lower risk skips more breakouts.
- These are hold-to-the-close measurements on 2021 to 2023, one breakout per move outside the band, with the stop measured from the next minute's open. A backtest with an account, sizing and re-entries will differ.
