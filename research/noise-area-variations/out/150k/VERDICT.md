# Noise-Area on a $150,000 MyFundedFutures evaluation account: the verdict

Written 2026-11-17. Data: NQ 1-minute bars, 2021-03-08 to 2026-07-17, micro contracts at $2 a point.

## The answer

**None of the 36 runs passes. On the $150,000 account, with midpoint fills, Noise-Area still fails the five bars.**

The bigger account helps survival a great deal and still does not produce a pass. The nearest miss is W2 at $100 a trade: it clears the rule check, the 2-to-1 bar and survival (the limit never crossed; crossed in 1.2% of shuffles), and fails two bars: profit of $8,600 against the $9,000 bar, and 26 trading days without a trade against 7.

## The account used

From MyFundedFutures' help pages, read 2026-11-17: every $150,000 plan (Rapid, Pro, Builder) has a **$4,500** loss limit that follows the end-of-day balance and a **$9,000** profit target. The $6,000 limit mentioned on the call is not on their site. Builder was used as the kinder plan: it has no consistency rule in the evaluation. Details: `../../variations-150k/LIST.md`.

So the bars were: every order matches its rule; average winner at least twice the risk with a profit on 2024 to 2026; never more than seven trading days without a trade; profit at least $9,000; the $4,500 limit never crossed in the real order of days and crossed in at most 5% of 10,000 shuffles. Judged on midpoint fills: a stop fills halfway between its price and the worst price of its minute.

## What was run

The same twelve variations as before (V1 to V8, W1 to W4), with no rule changed. Their risk was written for a $50,000 account, and it can be carried to $150,000 in three ways, so each was run all three ways. The list was committed before any run (commit `cf43580`).

## The 36 against the five bars

### Same dollars a trade (`-dollars`)

| | Risk at the start | Rule check | 2-to-1 | Seven-day rule | Profit (bar: $9,000) | Survival (bar: 5% of shuffles) | All five |
|---|---:|---|---|---|---|---|---|
| V1 | $500 | pass | pass: winners 2.0 times the risk (2.2 from 2024); 2024 to 2026 made $6,305 | FAIL: 8 days | pass: $53,271 | FAIL: crossed 2021-08-19; 100% | no |
| V2 | $125 | pass | FAIL: winners 2.9 times the risk (2.7 from 2024); 2024 to 2026 lost $2,246 | FAIL: 14 days | pass: $10,484 | FAIL: crossed 2024-01-17; 59.8% | no |
| V3 | $75 | pass | pass: winners 4.0 times the risk (4.1 from 2024); 2024 to 2026 made $112 | FAIL: 26 days | FAIL: $3,379 | FAIL: never crossed; 21.0% | no |
| V4 | $125 | pass | FAIL: winners 3.5 times the risk (3.4 from 2024); 2024 to 2026 lost $4,674 | FAIL: 8 days | FAIL: $5,473 | FAIL: crossed 2023-12-08; 98.6% | no |
| V5 | $125 | pass | FAIL: winners 3.2 times the risk (2.9 from 2024); 2024 to 2026 lost $4,175 | FAIL: 14 days | pass: $9,972 | FAIL: crossed 2024-01-08; 55.6% | no |
| V6 | $125 | pass | FAIL: winners 2.3 times the risk (2.4 from 2024); 2024 to 2026 lost $2,124 | FAIL: 14 days | FAIL: $4,399 | FAIL: crossed 2024-02-15; 64.2% | no |
| V7 | $125 | pass | FAIL: winners 2.3 times the risk (2.2 from 2024); 2024 to 2026 lost $470 | FAIL: 14 days | pass: $11,353 | FAIL: crossed 2024-03-12; 26.7% | no |
| V8 | $125 | pass | FAIL: winners 5.5 times the risk (6.0 from 2024); 2024 to 2026 lost $911 | pass: 6 days | FAIL: $2,848 | FAIL: crossed 2021-12-07; 100% | no |
| W1 | $100 | pass | FAIL: winners 3.5 times the risk (3.2 from 2024); 2024 to 2026 lost $2,042 | FAIL: 29 days | FAIL: $7,604 | FAIL: crossed 2024-03-13; 13.3% | no |
| W2 | $100 | pass | pass: winners 2.5 times the risk (2.4 from 2024); 2024 to 2026 made $48 | FAIL: 26 days | FAIL: $8,600 | pass: never crossed; 1.2% | no |
| W3 | $150 | pass | pass: winners 2.3 times the risk (2.3 from 2024); 2024 to 2026 made $2,790 | FAIL: 26 days | pass: $11,253 | FAIL: crossed 2024-03-19; 25.1% | no |
| W4 | $100 | pass | FAIL: winners 4.0 times the risk (3.7 from 2024); 2024 to 2026 lost $2,779 | FAIL: 14 days | FAIL: $4,569 | FAIL: crossed 2024-01-17; 70.6% | no |

### Same number of losers inside the limit (`-room`)

| | Risk at the start | Rule check | 2-to-1 | Seven-day rule | Profit (bar: $9,000) | Survival (bar: 5% of shuffles) | All five |
|---|---:|---|---|---|---|---|---|
| V1 | $1125 | pass | pass: winners 2.0 times the risk (2.2 from 2024); 2024 to 2026 made $12,099 | FAIL: 8 days | pass: $141,373 | FAIL: crossed 2021-04-22; 100% | no |
| V2 | $281 | pass | FAIL: winners 2.6 times the risk (2.3 from 2024); 2024 to 2026 lost $9,200 | FAIL: 8 days | pass: $26,146 | FAIL: crossed 2022-11-09; 100% | no |
| V3 | $169 | pass | FAIL: winners 3.4 times the risk (3.2 from 2024); 2024 to 2026 lost $5,774 | FAIL: 8 days | pass: $10,320 | FAIL: crossed 2023-11-24; 100% | no |
| V4 | $281 | pass | FAIL: winners 3.4 times the risk (3.2 from 2024); 2024 to 2026 lost $10,024 | FAIL: 8 days | pass: $18,084 | FAIL: crossed 2021-09-08; 100% | no |
| V5 | $281 | pass | FAIL: winners 3.0 times the risk (2.7 from 2024); 2024 to 2026 lost $13,475 | FAIL: 8 days | pass: $24,181 | FAIL: crossed 2022-11-08; 100% | no |
| V6 | $281 | pass | FAIL: winners 2.1 times the risk (2.2 from 2024); 2024 to 2026 lost $4,953 | FAIL: 8 days | pass: $19,336 | FAIL: crossed 2022-11-09; 100% | no |
| V7 | $281 | pass | FAIL: winners 2.1 times the risk (1.9 from 2024); 2024 to 2026 lost $5,628 | FAIL: 8 days | pass: $27,532 | FAIL: crossed 2021-12-02; 100% | no |
| V8 | $281 | pass | FAIL: winners 5.2 times the risk (5.5 from 2024); 2024 to 2026 lost $7,250 | pass: 6 days | FAIL: $7,860 | FAIL: crossed 2021-07-19; 100% | no |
| W1 | $225 | pass | FAIL: winners 3.0 times the risk (2.7 from 2024); 2024 to 2026 lost $11,076 | FAIL: 8 days | pass: $18,124 | FAIL: crossed 2022-11-28; 100% | no |
| W2 | $225 | pass | FAIL: winners 2.3 times the risk (2.1 from 2024); 2024 to 2026 lost $8,585 | FAIL: 8 days | pass: $17,221 | FAIL: crossed 2022-11-29; 99.8% | no |
| W3 | $338 | pass | FAIL: winners 2.1 times the risk (2.0 from 2024); 2024 to 2026 lost $2,922 | FAIL: 8 days | pass: $22,702 | FAIL: crossed 2022-11-23; 100% | no |
| W4 | $225 | pass | FAIL: winners 3.8 times the risk (3.5 from 2024); 2024 to 2026 lost $10,132 | pass: 7 days | pass: $11,219 | FAIL: crossed 2022-10-27; 100% | no |

### Same percentage of the account (`-pct`)

| | Risk at the start | Rule check | 2-to-1 | Seven-day rule | Profit (bar: $9,000) | Survival (bar: 5% of shuffles) | All five |
|---|---:|---|---|---|---|---|---|
| V1 | $1500 | pass | pass: winners 2.0 times the risk (2.2 from 2024); 2024 to 2026 made $5,575 | FAIL: 8 days | pass: $191,012 | FAIL: crossed 2021-04-19; 100% | no |
| V2 | $375 | pass | FAIL: winners 2.6 times the risk (2.3 from 2024); 2024 to 2026 lost $18,510 | FAIL: 8 days | pass: $31,737 | FAIL: crossed 2021-08-17; 100% | no |
| V3 | $225 | pass | FAIL: winners 3.4 times the risk (3.2 from 2024); 2024 to 2026 lost $8,054 | FAIL: 8 days | pass: $12,719 | FAIL: crossed 2022-01-28; 100% | no |
| V4 | $375 | pass | FAIL: winners 3.4 times the risk (3.2 from 2024); 2024 to 2026 lost $15,980 | FAIL: 8 days | pass: $23,950 | FAIL: crossed 2021-08-20; 100% | no |
| V5 | $375 | pass | FAIL: winners 3.0 times the risk (2.7 from 2024); 2024 to 2026 lost $23,140 | FAIL: 8 days | pass: $30,274 | FAIL: crossed 2021-08-20; 100% | no |
| V6 | $375 | pass | FAIL: winners 2.1 times the risk (2.2 from 2024); 2024 to 2026 lost $5,596 | FAIL: 8 days | pass: $26,814 | FAIL: crossed 2021-11-19; 100% | no |
| V7 | $375 | pass | FAIL: winners 2.1 times the risk (1.9 from 2024); 2024 to 2026 lost $10,955 | FAIL: 8 days | pass: $35,683 | FAIL: crossed 2021-11-19; 100% | no |
| V8 | $375 | pass | FAIL: winners 5.2 times the risk (5.5 from 2024); 2024 to 2026 lost $7,876 | pass: 6 days | FAIL: $8,795 | FAIL: crossed 2021-07-15; 100% | no |
| W1 | $300 | pass | FAIL: winners 3.0 times the risk (2.7 from 2024); 2024 to 2026 lost $16,675 | FAIL: 8 days | pass: $22,741 | FAIL: crossed 2022-10-28; 100% | no |
| W2 | $300 | pass | FAIL: winners 2.3 times the risk (2.1 from 2024); 2024 to 2026 lost $11,043 | FAIL: 8 days | pass: $24,197 | FAIL: crossed 2021-12-02; 100% | no |
| W3 | $450 | pass | FAIL: winners 2.1 times the risk (2.0 from 2024); 2024 to 2026 lost $5,911 | FAIL: 8 days | pass: $31,564 | FAIL: crossed 2021-11-22; 100% | no |
| W4 | $300 | pass | FAIL: winners 3.8 times the risk (3.5 from 2024); 2024 to 2026 lost $12,771 | pass: 7 days | pass: $14,532 | FAIL: crossed 2022-10-05; 100% | no |

### Other figures

| | Trades | Win rate | Longest losing run | Skipped signals | Worst drop from a high | Profit on kind fills | Profit on harsh fills | Evaluations passed / failed / not finished | Typical days to pass |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| V1-dollars | 1,435 | 33% | 19 | 0 | $32,482 | $94,247 | $14,975 | 28% / 70% / 2% | 34 |
| V2-dollars | 874 | 30% | 15 | 395 | $8,406 | $16,794 | $3,833 | 25% / 26% / 48% | 330 |
| V3-dollars | 767 | 24% | 21 | 855 | $4,444 | $7,916 | lost $1,514 | 0% / 0% / 100% | none |
| V4-dollars | 974 | 26% | 17 | 99 | $10,172 | $14,241 | lost $3,344 | 23% / 41% / 36% | 244 |
| V5-dollars | 729 | 28% | 21 | 269 | $8,624 | $15,344 | $3,305 | 25% / 27% / 48% | 302 |
| V6-dollars | 897 | 32% | 14 | 510 | $6,431 | $11,115 | $1,024 | 3% / 29% / 68% | 622 |
| V7-dollars | 884 | 35% | 14 | 406 | $5,849 | $18,573 | $3,700 | 26% / 15% / 59% | 397 |
| V8-dollars | 1,620 | 18% | 29 | 5,111 | $11,013 | $35,751 | lost $21,022 | 5% / 86% / 10% | 102 |
| W1-dollars | 634 | 27% | 21 | 704 | $5,726 | $12,238 | $4,031 | 17% / 28% / 55% | 441 |
| W2-dollars | 638 | 34% | 21 | 676 | $3,776 | $11,868 | $4,606 | 10% / 0% / 90% | 589 |
| W3-dollars | 649 | 35% | 13 | 615 | $5,576 | $13,777 | $7,864 | 19% / 29% / 51% | 520 |
| W4-dollars | 840 | 23% | 29 | 365 | $6,632 | $11,056 | lost $2,072 | 9% / 31% / 59% | 363 |
| V1-room | 1,435 | 33% | 19 | 0 | $104,836 | $295,467 | $28,839 | 23% / 77% / 0% | 6 |
| V2-room | 987 | 31% | 15 | 0 | $22,725 | $39,446 | $8,403 | 45% / 45% / 10% | 118 |
| V3-room | 1,001 | 26% | 17 | 20 | $14,363 | $24,855 | lost $2,944 | 27% / 59% / 14% | 188 |
| V4-room | 1,001 | 26% | 17 | 19 | $26,773 | $45,227 | lost $7,874 | 23% / 71% / 6% | 83 |
| V5-room | 795 | 28% | 15 | 0 | $25,095 | $37,460 | $8,221 | 33% / 63% / 4% | 88 |
| V6-room | 1,047 | 33% | 14 | 2 | $17,224 | $34,216 | $5,820 | 42% / 48% / 10% | 135 |
| V7-room | 1,000 | 36% | 14 | 0 | $15,877 | $44,606 | $8,748 | 41% / 48% / 10% | 126 |
| V8-room | 1,687 | 19% | 29 | 880 | $29,907 | $100,900 | lost $50,996 | 20% / 78% / 2% | 30 |
| W1-room | 795 | 28% | 15 | 0 | $19,698 | $30,768 | $5,965 | 38% / 57% / 4% | 135 |
| W2-room | 795 | 34% | 19 | 0 | $14,428 | $31,921 | $5,817 | 36% / 60% / 4% | 163 |
| W3-room | 795 | 36% | 15 | 0 | $15,158 | $34,522 | $12,226 | 35% / 57% / 8% | 103 |
| W4-room | 922 | 23% | 17 | 8 | $20,071 | $28,696 | lost $4,584 | 23% / 70% / 7% | 122 |
| V1-pct | 1,435 | 33% | 19 | 0 | $168,952 | $454,269 | $33,488 | 22% / 78% / 0% | 3 |
| V2-pct | 987 | 31% | 15 | 0 | $35,006 | $59,062 | $11,132 | 32% / 64% / 4% | 51 |
| V3-pct | 1,001 | 26% | 17 | 19 | $20,099 | $31,984 | lost $4,603 | 23% / 66% / 11% | 116 |
| V4-pct | 1,001 | 26% | 17 | 19 | $38,452 | $59,583 | lost $8,926 | 27% / 69% / 4% | 34 |
| V5-pct | 795 | 28% | 15 | 0 | $40,542 | $53,611 | $11,820 | 33% / 65% / 2% | 49 |
| V6-pct | 1,049 | 32% | 14 | 0 | $24,219 | $43,969 | $7,573 | 29% / 67% / 4% | 62 |
| V7-pct | 1,000 | 36% | 14 | 0 | $24,170 | $65,488 | $10,009 | 41% / 54% / 4% | 67 |
| V8-pct | 1,687 | 19% | 29 | 880 | $37,028 | $142,516 | lost $67,466 | 22% / 77% / 1% | 19 |
| W1-pct | 795 | 28% | 15 | 0 | $29,364 | $38,342 | $6,610 | 33% / 63% / 4% | 89 |
| W2-pct | 795 | 34% | 19 | 0 | $19,358 | $40,702 | $8,142 | 35% / 61% / 4% | 99 |
| W3-pct | 795 | 36% | 15 | 0 | $23,084 | $49,762 | $15,844 | 32% / 64% / 4% | 57 |
| W4-pct | 923 | 23% | 17 | 6 | $26,815 | $35,612 | lost $10,983 | 34% / 62% / 4% | 98 |

"Evaluations" is for information, not a bar: an evaluation started on every one of the 1,367 trading days, counted as passed when it reached +$9,000 before touching the limit, with MyFundedFutures' rule that the limit stops rising at $150,100. "Not finished" means the data ran out first. It is approximate: it reuses each day's result from the long run.

## Why it still fails

1. **The seven-day rule fails on its own, with nothing skipped.** At the larger sizes almost no signal is skipped, and the half-hour versions still went 8 trading days without a breakout, from 2025-11-25 to 2025-12-04. That is the strategy, not the account. Only the any-minute version (V8) and the narrower band (W4, exactly 7 days) keep the rule, and both fail on profit after 2023 and on survival.
2. **Survival and profit pull in opposite directions.** At the same dollars a trade the limit holds 30 to 60 losers, and survival gets close or passes (W2 1.2% of shuffles, W1 13%, V3 21%). But $75 to $150 a trade makes too little: only five of those twelve reach $9,000, and at that size one micro contract is again too big for many signals (600 to 850 skipped), so the gaps run to 14 to 29 days. At the larger sizes the profit bar is met by almost all, and the limit is crossed in every one, in 100% of shuffles.
3. **2024 to 2026 still lose.** On midpoint fills 30 of the 36 lost money from 2024 on. The six that did not are V1 (all three sizes) and V3, W2 and W3 at the same dollars, the last three by $48 to $2,790. 2026 is a losing year in every run looked at.
4. **Fills still decide a lot, and no fill model rescues it.** On kind fills no run passes either. W2 at $100 fails only the seven-day rule (26 days). V8 fails only survival, at every size, crossed in 100% of shuffles. On harsh fills none comes close.

## The nearest misses

| | Fails | By how much |
|---|---|---|
| W2 at $100 a trade | profit; seven-day rule | $8,600 against $9,000; 26 days against 7. Its profit from 2024 on is $48. |
| W3 at $150 a trade | seven-day rule; survival | 26 days; limit crossed 2024-03-19 and in 25% of shuffles |
| V3 at $75 a trade | profit; seven-day rule; survival | $3,379; 26 days; never crossed in the real order but in 21% of shuffles |
| W4 at $300 a trade | 2024 to 2026; survival | lost $12,771 from 2024; limit crossed in 100% of shuffles |

The 26-day gap in W2 and W3 is the end of the data, 2026-06-12 to 2026-07-17: the band had grown so wide in points that one micro contract cost more than $100 to $150 to stop out, so every signal was skipped.

## Other things the run showed

- **MyFundedFutures' own limit is easier than the bar.** Their limit stops rising once the account is $4,600 up. Judged that way, W2 at $100 is crossed in 0.5% of shuffles, W1 at $100 in 5.8%, V7 at $125 in 9.2%. The bar as Amear set it has no stopping point, and that is what was judged.
- **As an evaluation to pass once**, the picture is different from five years of survival: the mid-size runs reached +$9,000 before the limit in 20% to 45% of start dates (V2 at $281: 45%), typically after about half a year of trading. W2 at $100 never failed an evaluation in the data, and passed only 10% of them before the data ran out (typically 589 trading days).
- The most contracts held was 120 micros in V1 at $1,500 a trade, over the 90 allowed; 74 in V1 at $1,125; 25 or fewer in every other run.
- A day lost $2,500 or more only in V1 (467, 299 and 13 days at the three sizes). Builder's daily pause would have applied there and was not modelled. V1 fails survival within weeks either way.

## What was checked

- Every run was made twice and gave the same trades.
- Every trade of all 108 results (36 runs, three fill models) was replayed against the written rules by the separate replay in `gates.py`: no breaks.
- The midpoint fill and the $4,500 bars have hand-worked tests (`test_engine.py`, `test_gates.py`, `test_run_150k.py`); all tests pass.
- An independent checker, which did not write the code, read the raw price file with its own program and checked all 36 runs: every one of the 23,945 midpoint stop fills (price, the first minute that reached the stop, trailing stops rebuilt minute by minute); the money on all 106,360 trades across the three fill models; every daily figure the survival bar reads; and the five bars themselves. No differences. It did not rebuild the entries, sizes or skips; those are covered by the replay above.

## What to keep in mind

- 2024 to 2026 were already seen by earlier runs. They are not a fresh test.
- Thirty-six runs give three times the chances of twelve. It did not matter: nothing passed.
- The full trade lists are large and are not in the repo. `run_150k.py` rewrites them; each list's fingerprint is in its `judge.json`.
- The price file has holes; a day's trading stops at the first hole longer than 60 minutes, as before.

## What this does not say

It does not say a $150,000 evaluation could not be passed once with this strategy: at the middle sizes a fifth to nearly half of start dates did. It says no version keeps a $4,500 trailing limit, a seven-day rule, a 2-to-1 winner and a profit after 2023 together over five years.
