# Opening range breakout on the $150,000 frame: the verdict

Written 2026-11-17. Data: NQ 1-minute bars. Measured on 2021-03-08 to 2023-12-31 at one micro contract ($2 a point), midpoint fills, 2 ticks of slippage on market orders, $1.90 commission a contract.

## The answer

**None of the 108 versions measured is good enough to send to the full test. The opening range breakout fails on the $150,000 frame before the final run.**

The reason is the same squeeze that killed Noise-Area, now measured directly:

- The versions whose average winner is at least twice the risk win only about a quarter of the time. Their losing runs reach 14 to 19 trades in a row.
- Losing runs that long force a small size. To keep the $4,500 limit crossed in no more than 1 shuffle in 40, the best of them can risk only about **$61 a trade**.
- At $61 a trade, its 2021 to 2023 record projects to about **$9,700 over the five and a half years**. That is barely above the $9,000 bar, with no margin. The plan asked for 25% margin, set before the run.
- Its edge also shrinks every year: about 42 times the risk in 2021, 35 in 2022, and 7 in 2023.
- At $61 a trade, any day whose stop is wider than about 29 points cannot be traded with even one micro. A real run would skip many days, so the projection is kinder than the real result would be.

The versions that survive best (smallest losing runs) win often but small. Their average winner is about the same as the risk, so they fail the 2-to-1 bar.

## The closest versions

| Version | Trades | Win rate | Average winner vs risk | Longest losing run | Safe risk a trade | Projected profit, full period | Against the $9,000 bar |
|---|---:|---:|---:|---:|---:|---:|---:|
| 15-minute range, the range's direction, stop at half the range, target 10 times the risk | 701 | 25% | 3.6 | 19 | $61 | $9,726 | 1.08 |
| Same, held to the close | 701 | 25% | 3.6 | 19 | $61 | $9,429 | 1.05 |
| 5-minute range, first break, stop at the far side, target 5 times the risk | 705 | 33% | 2.3 | 14 | $76 | $8,280 | 0.92 |
| 15-minute range, first break, stop at half the range, target 10 times the risk | 692 | 25% | 3.6 | 14 | $60 | $7,747 | 0.86 |
| For comparison: 30-minute range, first break, far-side stop, trailing stop | 621 | 49% | 1.0 | 8 | $144 | $10,757 | 1.20, but fails 2-to-1 |

56 of the 108 versions made money on 2021 to 2023 at one micro, before the account test.

## How it was checked

- The engine and a separate rule check were written test-first (43 tests).
- An agent that did not write the code re-derived 30 trades by hand from the raw minute lines, and its own simulator matched the engine on 45 settings. It found no defects.
- Every one of the 108 measuring runs had zero rule breaks. Two runs gave identical files.
- I recomputed two versions myself: trades, net and average winner match exactly; the drawdown figure is within 2% (shuffle noise).

## What this does not show

- 1-minute bars make fills look better than they would be live.
- The final run on 2021 to 2026 was not made, because nothing qualified. 2024 to 2026 was not looked at in this pass. It was seen before, in candidate 2.
- The safe size uses 1 shuffle in 40, half the 5% bar, as margin chosen before the run. At the bar itself the size could be somewhat larger, and so could the projection. But the best version that keeps 2-to-1 still has no real margin, and its 2023 is close to flat.
