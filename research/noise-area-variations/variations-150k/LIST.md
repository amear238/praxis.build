# The $150,000 rerun list

Fixed on 2026-11-17 before any run. Nothing in this folder changes after this commit.

Amear's ruling (2026-11-17): rerun Noise-Area on a $150,000 MyFundedFutures evaluation account, on the plan kinder to the strategy; the five bars stay; stops are judged on the midpoint fill; profit on 2024 to 2026 alone stays a bar.

## The account, from MyFundedFutures' help pages (read 2026-11-17)

All three $150,000 plans (Rapid, Pro, Builder) have the same evaluation money rules: a **$4,500** maximum loss limit that follows the end-of-day balance, and a **$9,000** profit target. The $6,000 figure in the call notes is not on their site. The plans differ only here:

| | Rapid | Pro | Builder |
|---|---|---|---|
| Daily loss limit | none | none | $2,500, pauses trading for the rest of the day, does not close the account |
| Consistency rule in the evaluation | 50% | 50% | none |
| Fewest trading days | 2 | 2 | 1 |
| Most contracts | 10 minis / 100 micros | 9 minis / 90 micros | 9 minis / 90 micros |

**Plan used: Builder.** It is the kinder one: no consistency rule in the evaluation, and its daily limit only pauses a bad day. The run does not model the pause; it counts the days that lost $2,500 or more so it can be seen whether the pause would ever have applied. It also reports the most micro contracts held, against the 90 allowed.

## The bars on this account

The same five. Only the dollar figures move with the limit:

1. Every order matches its rule.
2. The average winner is at least twice the risk, over all years and over 2024 to 2026, and 2024 to 2026 alone makes a profit.
3. Never more than seven trading days without a trade.
4. Profit at least twice the limit: **$9,000**.
5. The $4,500 limit, following the end-of-day balance with no stopping point, is never crossed in the real order of days, and is crossed in at most 5% of 10,000 shuffled orders.

Judged on the **midpoint fill**: a stop fills halfway between its price and the worst price of its minute. When the minute opens already past the stop, halfway between that open and the worst price. No further slippage on a stop; entries and other exits keep 2 ticks. Kind and harsh fills are run too, for information.

Not bars, reported for information: bar 5 again with MyFundedFutures' rule that the limit stops rising once it is $100 above the starting balance; and how many evaluations would have passed (reached +$9,000 before the limit) if one had been started on each trading day.

## The list: the same twelve variations, each at three sizes

The twelve are V1 to V8 (`../variations/LIST.md`) and W1 to W4 (`../variations/LIST2.md`), unchanged except for the size of the risk. No new entry, exit, stop or band rule. The risk was written as a percentage of a $50,000 account with a $2,000 limit, and that cannot be carried to $150,000 with a $4,500 limit in only one way, so each is run all three ways (written by `../make_150k_list.py`):

| Ending | Meaning | V1 | V2, V4 to V8 | V3 | W1, W2, W4 | W3 |
|---|---|---|---|---|---|---|
| `-pct` | same percentage of the account | $1,500 | $375 | $225 | $300 | $450 |
| `-room` | same number of losers inside the limit | $1,125 | $281 | $169 | $225 | $338 |
| `-dollars` | same dollars a trade | $500 | $125 | $75 | $100 | $150 |

Dollars a trade at the start; the risk stays a set percentage of the current balance.

What to expect, written before the run: `-pct` has less room than before (12 losers inside the limit where there were 16) but skips the fewest signals; `-dollars` has the most room (36 losers) and the same skips as before, but must make $9,000 where $4,000 was the bar; `-room` sits between. Thirty-six runs is three times as many chances for a lucky pass as twelve: a pass at one size only, with its two sister sizes far from passing, is to be read with that in mind.
