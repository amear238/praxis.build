# Noise-Area variations: the verdict

Written 2026-11-17. Data: NQ 1-minute bars, 2021-03-08 to 2026-07-17, micro contracts at $2 a point.

## The answer

**No variation of the Noise-Area breakout passes. Under these five bars, Noise-Area is dead.**

Twelve variations were tried in total: a first list of eight (locked at commit `c4340ac`) and the one allowed second list of four (locked at commit `7a54805`). Each list was fixed and committed before any of its variations was run. There is no finalist.

Every one of the twelve fails the survival bar, and not narrowly: the $2,000 trailing limit is crossed in the real order of days in every variation, and in 100% of the shuffled orders for almost all of them (the bar is 5%). Every one also loses money from 2024 to 2026 on the judged fills. Only one passes the seven-day rule, and it loses $17,852.

## The twelve against the five bars

Account: the $50,000 stand-in with a $2,000 end-of-day trailing limit. Fills: the harsh model (a stop fills at the worst price of its minute). "Times the risk" is the result of a trade divided by the money risked on it.

| | Rule check | 2-to-1 | Seven-day rule | Profit (bar: $4,000) | Survival (bar: 5% of shuffles) | All five |
|---|---|---|---|---|---|---|
| V1 | pass | FAIL: winners average 2.0 times the risk (2.2 from 2024), but 2024 to 2026 lost $19,071 | FAIL: 8 days | pass: $10,029 | FAIL: limit crossed 2021-04-22; 100% | no |
| V2 | pass | FAIL: winners average 2.9 times the risk (2.6 from 2024), but 2024 to 2026 lost $5,989 | FAIL: 14 days | FAIL: $3,453 | FAIL: limit crossed 2021-08-20; 100% | no |
| V3 | pass | FAIL: winners average 4.0 times the risk (4.3 from 2024), but 2024 to 2026 lost $2,492 | FAIL: 30 days | FAIL: lost $2,116 | FAIL: limit crossed 2023-01-12; 100% | no |
| V4 | pass | FAIL: winners average 3.5 times the risk (3.5 from 2024), but 2024 to 2026 lost $8,617 | FAIL: 9 days | FAIL: lost $3,456 | FAIL: limit crossed 2021-09-01; 100% | no |
| V5 | pass | FAIL: winners average 3.2 times the risk (2.9 from 2024), but 2024 to 2026 lost $6,687 | FAIL: 14 days | FAIL: $3,534 | FAIL: limit crossed 2022-11-11; 100% | no |
| V6 | pass | FAIL: winners average 2.2 times the risk (2.4 from 2024), but 2024 to 2026 lost $4,394 | FAIL: 14 days | FAIL: $402 | FAIL: limit crossed 2022-01-25; 100% | no |
| V7 | pass | FAIL: winners average 2.2 times the risk (2.1 from 2024), but 2024 to 2026 lost $4,116 | FAIL: 14 days | pass: $4,162 | FAIL: limit crossed 2021-12-03; 100% | no |
| V8 | pass | FAIL: winners average 5.9 times the risk (6.7 from 2024), but 2024 to 2026 lost $6,838 | pass: 7 days | FAIL: lost $17,852 | FAIL: limit crossed 2021-07-16; 100% | no |
| W1 | pass | FAIL: winners average 3.4 times the risk (3.1 from 2024), but 2024 to 2026 lost $2,509 | FAIL: 26 days | pass: $4,027 | FAIL: limit crossed 2022-11-16; 100% | no |
| W2 | pass | FAIL: winners average 2.5 times the risk (2.4 from 2024), but 2024 to 2026 lost $2,368 | FAIL: 26 days | FAIL: $3,460 | FAIL: limit crossed 2022-11-23; 99.8% | no |
| W3 | pass | FAIL: winners average 2.3 times the risk (2.3 from 2024), but 2024 to 2026 lost $557 | FAIL: 26 days | pass: $4,796 | FAIL: limit crossed 2022-11-11; 100% | no |
| W4 | pass | FAIL: winners average 4.0 times the risk (3.7 from 2024), but 2024 to 2026 lost $5,597 | FAIL: 14 days | FAIL: lost $2,239 | FAIL: limit crossed 2022-10-31; 100% | no |

How to read the 2-to-1 column: the average winner is at least twice the risk in every variation. The bar fails because it also needs a profit above zero on 2024 to 2026 alone, and none has one.

What each variation is: `variations/LIST.md` (V1 to V8) and `variations/LIST2.md` (W1 to W4). In short: V1 is the original rules with a stop at 1% risk; V2 to V8 are the strongest cell of the measuring pass at about $125 a trade with different stops, exits and trade counts; W1 to W4 are one trade a day at $100 to $150 with a trailing stop, a wider stop, or a narrower band.

## The other figures

| | Trades | Win rate | Average winner | Average loser | Longest losing run | Skipped signals | Worst drop from a high | Profit on kind fills | $10,000 account (information only), harsh / kind |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| V1 | 1,435 | 33% | $1,296 | $631 | 19 | 0 | $47,844 | $146,466 | lost $1,789 (973 trades) / $18,235 (1,371 trades) |
| V2 | 884 | 30% | $307 | $126 | 15 | 341 | $11,101 | $13,588 | lost $107 (2 trades) / lost $48 (2 trades) |
| V3 | 746 | 23% | $227 | $72 | 21 | 959 | $6,485 | $6,684 | no trades |
| V4 | 965 | 25% | $371 | $131 | 17 | 141 | $15,314 | $16,850 | lost $552 (19 trades) / lost $374 (20 trades) |
| V5 | 736 | 28% | $348 | $131 | 15 | 229 | $12,136 | $15,251 | lost $107 (2 trades) / lost $48 (2 trades) |
| V6 | 903 | 32% | $224 | $103 | 14 | 496 | $7,602 | $10,372 | lost $107 (2 trades) / lost $48 (2 trades) |
| V7 | 893 | 34% | $243 | $120 | 14 | 362 | $7,980 | $17,276 | lost $102 (2 trades) / lost $38 (2 trades) |
| V8 | 1,504 | 18% | $475 | $116 | 29 | 14,403 | $24,254 | $47,217 | lost $866 (169 trades) / $4,446 (476 trades) |
| W1 | 661 | 28% | $280 | $100 | 22 | 581 | $6,984 | $9,527 | no trades |
| W2 | 657 | 33% | $206 | $93 | 22 | 586 | $4,784 | $9,622 | no trades |
| W3 | 677 | 35% | $286 | $140 | 14 | 507 | $7,045 | $13,369 | no trades |
| W4 | 835 | 23% | $325 | $100 | 29 | 394 | $10,236 | $9,743 | no trades |

On the $10,000 account almost nothing trades below 1% risk: 0.25% of $10,000 is $25, and one micro contract with a stop 10 points away already risks about $23. V8's skipped count is high because it is counted every minute price stays outside the band.

## Why it fails

1. **Survival.** These variations win 2 to 3.5 trades in 10. Losing runs of 14 to 29 in a row happened in every one. At $100 to $150 a trade the $2,000 limit is 13 to 20 losers, and on harsh fills a stopped trade loses about 1.2 times what was planned. A smaller risk does not fix it, because one micro contract cannot be cut any smaller: the signal is skipped, and then the seven-day rule fails (V3: 959 skipped, a 30-day stretch).
2. **The edge is gone after 2023.** On 2021 to 2023 most variations made money on harsh fills (V2 $9,442, V5 $10,221). On 2024 to 2026 every one lost. The measuring pass and both lists were chosen on 2021 to 2023; the later years did not hold up.
3. **The seven-day rule.** Half-hour breakouts sat exactly at seven days on 2021 to 2023 and went over it later. By mid-2026 the band is so wide in points that most signals cost more than the risk allows and are skipped: 42 skipped signals between 2026-06-26 and 2026-07-15 in V2 alone.
4. **How stops fill decides the profit.** On kind fills (a stop fills at its price plus 2 ticks) all twelve make more than $4,000. On harsh fills only four do. On harsh fills between 4 and 7 trades in 10 lost more than planned, the worst 3.3 to 8.9 times the plan. Even on kind fills none passes: survival fails in every one (the best, W2, crosses the limit in 88% of shuffles) and so does the seven-day rule in all but V8.

## What was checked

- An independent checker, which did not write the code, rebuilt every trade, every skipped signal and every daily figure of all eight first-list variations from the raw price file with its own program, on both fill models: no differences. It also re-derived 64 sampled trades one by one: no mismatches. A second independent checker did the same for the four second-list variations (all eight result files rebuilt in full, 32 sampled trades): no mismatches.
- The lead recomputed every bar from the raw trade lists with a separate script (`lead_check.py`, output `out/variations/lead-check.txt`): no differences from the judge on any of the twelve.
- Before any run, the tester and two independent checks of the engine and the judge found seven defects (among them: the seven-day count included the days before the band exists, and the survival test let 5.02% pass). All were fixed and re-checked: 15,600 random runs against an independent simulator, no differences.
- Every run was made twice and gave the same trades. The baseline settings with no stop reproduce the 15 November retest trade for trade (1,173 trades).

## What to keep in mind

- 2024 to 2026 were not used to choose either list, but they are not truly unseen: earlier Noise-Area and candidate 1 runs covered them.
- The second list was chosen knowing the first list's results on 2021 to 2023 only, as the design allows.
- The price file has holes (hours missing on a few days, ten weekdays missing in September 2021). A day's trading stops at the first hole longer than 60 minutes. Days with nothing in the file are not counted as trading days.
- On early-close days the band uses every bar in the file, where the NinjaTrader loader cuts the last hour. The checker measured this and two similar choices: they move a variation's profit by a few hundred to about $3,300, and change no verdict.
- A stop under 10 points is never traded. The stop distance is fixed at the decision and rests that far from the actual fill.
- The evening and overnight hours were measured and not traded: overnight breakouts are flat or losing, and evening ones are stopped out 9 times in 10 and cannot keep the seven-day rule alone.

## What this does not say

It does not say the Noise-Area idea never makes money: on kind fills at 1% risk it made $146,466 with a worst drop of $64,600. It says no version of it found here fits a $2,000 trailing limit, a seven-day rule and a 2-to-1 bar together. Per the design, the question now goes back to Amear.
