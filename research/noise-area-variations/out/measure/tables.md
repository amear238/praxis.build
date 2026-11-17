# Noise-Area breakouts: the measuring pass

Trading days 2021-03-08 to 2023-12-31. No trades were placed; this only measures what price did after each breakout.

A breakout is the first close outside the noise band after a close inside it (or the first close of the day, if it is already outside). It is not counted again until price closes back inside. The entry price is the open of the next minute. "Reached 2 times the risk" means price moved in favour by at least twice the stop distance before the stop was hit. The average result is in multiples of the stop distance, holding to the day's last bar (4 PM, or earlier on a short day); a stopped breakout counts as minus one. A stop under 10 points is too tight to use, so those breakouts are left out of the shares and the average, and counted in their own column. "Measured" is the number the shares are taken over.

"On the half hour" looks at closes on the hour and half hour only (the original rule). "Any minute" looks at every one-minute close. The band is built either from the 9:30 AM open (the original rule) or from the 6:00 PM open; the 9:30 AM band starts at 9:31 AM, so it has no evening or overnight rows.

## Stop at half the band width

The stop sits half the band's width away from the entry price.

| Band built from the | Breakouts looked for | Part of the day | Side | All breakouts | Measured | Left out, stop under 10 points | Reached 2 times the risk | Reached 3 times the risk | Reached 5 times the risk | Average result if held to 4 PM, in risks | Longest stretch with no breakout, trading days |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 191 | 191 | 0 | 38.7% | 33.5% | 16.2% | 0.68 | 14 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 179 | 179 | 0 | 37.4% | 29.1% | 17.9% | 0.29 | 25 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 370 | 370 | 0 | 38.1% | 31.4% | 17.0% | 0.49 | 10 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 87 | 87 | 0 | 24.1% | 10.3% | 2.3% | 0.29 | 34 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 70 | 70 | 0 | 22.9% | 11.4% | 0.0% | -0.04 | 49 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 157 | 157 | 0 | 23.6% | 10.8% | 1.3% | 0.14 | 24 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 39 | 39 | 0 | 17.9% | 10.3% | 2.6% | 0.53 | 71 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 41 | 41 | 0 | 12.2% | 4.9% | 0.0% | 0.33 | 90 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Both | 80 | 80 | 0 | 15.0% | 7.5% | 1.2% | 0.43 | 28 |
| 9:30 AM open | On the half hour | Whole day | Buy (closed above) | 317 | 317 | 0 | 32.2% | 24.3% | 10.7% | 0.55 | 14 |
| 9:30 AM open | On the half hour | Whole day | Sell (closed below) | 290 | 290 | 0 | 30.3% | 21.4% | 11.0% | 0.22 | 18 |
| 9:30 AM open | On the half hour | Whole day | Both | 607 | 607 | 0 | 31.3% | 22.9% | 10.9% | 0.39 | 7 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 928 | 779 | 149 | 30.3% | 22.6% | 11.3% | 0.10 | 10 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 902 | 781 | 121 | 29.8% | 22.7% | 13.2% | 0.06 | 14 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1830 | 1560 | 270 | 30.1% | 22.6% | 12.2% | 0.08 | 8 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 443 | 443 | 0 | 28.7% | 14.0% | 1.4% | 0.34 | 27 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 446 | 446 | 0 | 20.2% | 11.9% | 1.8% | -0.07 | 37 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 889 | 889 | 0 | 24.4% | 12.9% | 1.6% | 0.13 | 19 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 265 | 265 | 0 | 11.3% | 4.9% | 0.8% | 0.34 | 43 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 292 | 292 | 0 | 7.9% | 2.7% | 0.0% | 0.14 | 49 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Both | 557 | 557 | 0 | 9.5% | 3.8% | 0.4% | 0.24 | 20 |
| 9:30 AM open | Any minute | Whole day | Buy (closed above) | 1636 | 1487 | 149 | 26.4% | 16.9% | 6.5% | 0.21 | 8 |
| 9:30 AM open | Any minute | Whole day | Sell (closed below) | 1640 | 1519 | 121 | 22.8% | 15.7% | 7.3% | 0.04 | 14 |
| 9:30 AM open | Any minute | Whole day | Both | 3276 | 3006 | 270 | 24.6% | 16.3% | 6.9% | 0.13 | 6 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Buy (closed above) | 487 | 241 | 246 | 31.5% | 25.3% | 16.2% | 0.12 | 57 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Sell (closed below) | 477 | 232 | 245 | 29.3% | 21.6% | 16.8% | 0.22 | 37 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Both | 964 | 473 | 491 | 30.4% | 23.5% | 16.5% | 0.17 | 26 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 312 | 303 | 9 | 35.0% | 25.1% | 15.2% | 0.03 | 18 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 315 | 310 | 5 | 33.5% | 25.8% | 14.2% | -0.04 | 20 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Both | 627 | 613 | 14 | 34.3% | 25.4% | 14.7% | -0.00 | 7 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 134 | 134 | 0 | 33.6% | 15.7% | 5.2% | 0.42 | 30 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 114 | 114 | 0 | 28.9% | 16.7% | 3.5% | -0.02 | 35 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 248 | 248 | 0 | 31.5% | 16.1% | 4.4% | 0.22 | 19 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 73 | 73 | 0 | 11.0% | 1.4% | 0.0% | 0.25 | 82 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 85 | 85 | 0 | 15.3% | 3.5% | 0.0% | -0.06 | 42 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 158 | 158 | 0 | 13.3% | 2.5% | 0.0% | 0.08 | 34 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 53 | 53 | 0 | 11.3% | 1.9% | 0.0% | 0.28 | 47 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 43 | 43 | 0 | 4.7% | 0.0% | 0.0% | 0.13 | 69 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Both | 96 | 96 | 0 | 8.3% | 1.0% | 0.0% | 0.21 | 30 |
| 6:00 PM open | On the half hour | Whole day | Buy (closed above) | 1059 | 804 | 255 | 30.0% | 19.9% | 11.4% | 0.16 | 8 |
| 6:00 PM open | On the half hour | Whole day | Sell (closed below) | 1034 | 784 | 250 | 28.1% | 19.4% | 11.1% | 0.05 | 17 |
| 6:00 PM open | On the half hour | Whole day | Both | 2093 | 1588 | 505 | 29.0% | 19.6% | 11.3% | 0.10 | 3 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Buy (closed above) | 2551 | 1284 | 1267 | 29.0% | 24.1% | 17.8% | 0.45 | 27 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Sell (closed below) | 2555 | 1233 | 1322 | 35.8% | 26.0% | 19.7% | 0.58 | 24 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Both | 5106 | 2517 | 2589 | 32.3% | 25.0% | 18.8% | 0.51 | 17 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 1730 | 1696 | 34 | 31.2% | 22.8% | 14.1% | -0.09 | 11 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 1760 | 1730 | 30 | 34.8% | 24.9% | 14.4% | 0.13 | 10 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Both | 3490 | 3426 | 64 | 33.0% | 23.8% | 14.2% | 0.02 | 6 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 623 | 623 | 0 | 29.5% | 16.7% | 5.9% | 0.15 | 21 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 620 | 620 | 0 | 23.1% | 12.9% | 6.0% | -0.17 | 19 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1243 | 1243 | 0 | 26.3% | 14.8% | 6.0% | -0.01 | 7 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 361 | 361 | 0 | 15.5% | 2.2% | 0.6% | 0.19 | 27 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 426 | 426 | 0 | 12.4% | 3.3% | 0.9% | -0.18 | 36 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 787 | 787 | 0 | 13.9% | 2.8% | 0.8% | -0.01 | 20 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 341 | 341 | 0 | 8.5% | 1.5% | 0.0% | 0.16 | 31 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 317 | 317 | 0 | 5.7% | 0.3% | 0.0% | -0.03 | 28 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Both | 658 | 658 | 0 | 7.1% | 0.9% | 0.0% | 0.07 | 19 |
| 6:00 PM open | Any minute | Whole day | Buy (closed above) | 5606 | 4305 | 1301 | 27.2% | 18.9% | 11.8% | 0.15 | 8 |
| 6:00 PM open | Any minute | Whole day | Sell (closed below) | 5678 | 4326 | 1352 | 29.1% | 19.6% | 12.3% | 0.17 | 5 |
| 6:00 PM open | Any minute | Whole day | Both | 11284 | 8631 | 2653 | 28.1% | 19.2% | 12.0% | 0.16 | 2 |

## Stop at the full band width

The stop sits the band's full width away from the entry price.

| Band built from the | Breakouts looked for | Part of the day | Side | All breakouts | Measured | Left out, stop under 10 points | Reached 2 times the risk | Reached 3 times the risk | Reached 5 times the risk | Average result if held to 4 PM, in risks | Longest stretch with no breakout, trading days |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 191 | 191 | 0 | 27.2% | 12.6% | 2.6% | 0.23 | 14 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 179 | 179 | 0 | 29.6% | 18.4% | 5.6% | 0.22 | 25 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 370 | 370 | 0 | 28.4% | 15.4% | 4.1% | 0.23 | 10 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 87 | 87 | 0 | 3.4% | 0.0% | 0.0% | 0.15 | 34 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 70 | 70 | 0 | 4.3% | 0.0% | 0.0% | -0.00 | 49 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 157 | 157 | 0 | 3.8% | 0.0% | 0.0% | 0.08 | 24 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 39 | 39 | 0 | 2.6% | 0.0% | 0.0% | 0.28 | 71 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 41 | 41 | 0 | 0.0% | 0.0% | 0.0% | 0.20 | 90 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Both | 80 | 80 | 0 | 1.2% | 0.0% | 0.0% | 0.24 | 28 |
| 9:30 AM open | On the half hour | Whole day | Buy (closed above) | 317 | 317 | 0 | 17.7% | 7.6% | 1.6% | 0.21 | 14 |
| 9:30 AM open | On the half hour | Whole day | Sell (closed below) | 290 | 290 | 0 | 19.3% | 11.4% | 3.4% | 0.17 | 18 |
| 9:30 AM open | On the half hour | Whole day | Both | 607 | 607 | 0 | 18.5% | 9.4% | 2.5% | 0.19 | 7 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 928 | 900 | 28 | 24.8% | 14.8% | 5.8% | 0.09 | 10 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 902 | 880 | 22 | 27.8% | 18.2% | 8.0% | 0.05 | 13 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1830 | 1780 | 50 | 26.3% | 16.5% | 6.9% | 0.07 | 8 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 443 | 443 | 0 | 5.0% | 0.7% | 0.0% | 0.21 | 27 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 446 | 446 | 0 | 7.2% | 0.4% | 0.0% | -0.07 | 37 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 889 | 889 | 0 | 6.1% | 0.6% | 0.0% | 0.07 | 19 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 265 | 265 | 0 | 0.8% | 0.0% | 0.0% | 0.17 | 43 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 292 | 292 | 0 | 0.7% | 0.0% | 0.0% | 0.06 | 49 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Both | 557 | 557 | 0 | 0.7% | 0.0% | 0.0% | 0.12 | 20 |
| 9:30 AM open | Any minute | Whole day | Buy (closed above) | 1636 | 1608 | 28 | 15.4% | 8.5% | 3.2% | 0.14 | 8 |
| 9:30 AM open | Any minute | Whole day | Sell (closed below) | 1640 | 1618 | 22 | 17.2% | 10.0% | 4.3% | 0.02 | 13 |
| 9:30 AM open | Any minute | Whole day | Both | 3276 | 3226 | 50 | 16.3% | 9.2% | 3.8% | 0.08 | 4 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Buy (closed above) | 487 | 402 | 85 | 31.6% | 22.6% | 16.9% | 0.02 | 12 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Sell (closed below) | 477 | 407 | 70 | 33.7% | 25.3% | 15.2% | -0.03 | 16 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Both | 964 | 809 | 155 | 32.6% | 24.0% | 16.1% | -0.01 | 6 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 312 | 312 | 0 | 30.1% | 17.3% | 8.0% | -0.15 | 18 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 315 | 315 | 0 | 27.0% | 16.5% | 8.3% | 0.01 | 20 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Both | 627 | 627 | 0 | 28.5% | 16.9% | 8.1% | -0.07 | 7 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 134 | 134 | 0 | 10.4% | 3.7% | 1.5% | 0.21 | 30 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 114 | 114 | 0 | 11.4% | 2.6% | 0.9% | 0.07 | 35 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 248 | 248 | 0 | 10.9% | 3.2% | 1.2% | 0.14 | 19 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 73 | 73 | 0 | 1.4% | 0.0% | 0.0% | 0.13 | 82 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 85 | 85 | 0 | 0.0% | 0.0% | 0.0% | -0.05 | 42 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 158 | 158 | 0 | 0.6% | 0.0% | 0.0% | 0.03 | 34 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 53 | 53 | 0 | 0.0% | 0.0% | 0.0% | 0.14 | 47 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 43 | 43 | 0 | 0.0% | 0.0% | 0.0% | 0.10 | 69 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Both | 96 | 96 | 0 | 0.0% | 0.0% | 0.0% | 0.12 | 30 |
| 6:00 PM open | On the half hour | Whole day | Buy (closed above) | 1059 | 974 | 85 | 24.2% | 15.4% | 9.8% | 0.01 | 6 |
| 6:00 PM open | On the half hour | Whole day | Sell (closed below) | 1034 | 964 | 70 | 24.4% | 16.4% | 9.2% | -0.00 | 7 |
| 6:00 PM open | On the half hour | Whole day | Both | 2093 | 1938 | 155 | 24.3% | 15.9% | 9.5% | 0.00 | 2 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Buy (closed above) | 2551 | 2026 | 525 | 31.0% | 23.2% | 16.5% | 0.10 | 12 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Sell (closed below) | 2555 | 2032 | 523 | 33.7% | 22.8% | 14.8% | 0.02 | 8 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Both | 5106 | 4058 | 1048 | 32.3% | 23.0% | 15.7% | 0.06 | 3 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 1730 | 1730 | 0 | 31.0% | 19.0% | 9.1% | -0.14 | 11 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 1760 | 1760 | 0 | 27.4% | 16.7% | 9.2% | 0.04 | 10 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Both | 3490 | 3490 | 0 | 29.2% | 17.9% | 9.2% | -0.05 | 6 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 623 | 623 | 0 | 13.5% | 5.6% | 0.5% | 0.07 | 21 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 620 | 620 | 0 | 12.6% | 3.9% | 1.0% | -0.07 | 19 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1243 | 1243 | 0 | 13.0% | 4.7% | 0.7% | 0.00 | 7 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 361 | 361 | 0 | 0.6% | 0.0% | 0.0% | 0.11 | 27 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 426 | 426 | 0 | 1.9% | 0.0% | 0.0% | -0.09 | 36 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 787 | 787 | 0 | 1.3% | 0.0% | 0.0% | 0.00 | 20 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 341 | 341 | 0 | 0.3% | 0.0% | 0.0% | 0.08 | 31 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 317 | 317 | 0 | 0.0% | 0.0% | 0.0% | -0.01 | 28 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Both | 658 | 658 | 0 | 0.2% | 0.0% | 0.0% | 0.04 | 19 |
| 6:00 PM open | Any minute | Whole day | Buy (closed above) | 5606 | 5081 | 525 | 24.6% | 16.4% | 9.8% | 0.01 | 6 |
| 6:00 PM open | Any minute | Whole day | Sell (closed below) | 5678 | 5155 | 523 | 24.3% | 15.2% | 9.1% | 0.00 | 5 |
| 6:00 PM open | Any minute | Whole day | Both | 11284 | 10236 | 1048 | 24.5% | 15.8% | 9.4% | 0.01 | 2 |

## Stop back at the anchor price

The stop sits at the price the band is built around (the opening price it is anchored to).

| Band built from the | Breakouts looked for | Part of the day | Side | All breakouts | Measured | Left out, stop under 10 points | Reached 2 times the risk | Reached 3 times the risk | Reached 5 times the risk | Average result if held to 4 PM, in risks | Longest stretch with no breakout, trading days |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 191 | 191 | 0 | 11.0% | 3.1% | 0.0% | 0.16 | 14 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 179 | 179 | 0 | 13.4% | 4.5% | 0.0% | 0.06 | 25 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 370 | 370 | 0 | 12.2% | 3.8% | 0.0% | 0.11 | 10 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 87 | 87 | 0 | 1.1% | 0.0% | 0.0% | 0.10 | 34 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 70 | 70 | 0 | 1.4% | 0.0% | 0.0% | 0.00 | 49 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 157 | 157 | 0 | 1.3% | 0.0% | 0.0% | 0.05 | 24 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 39 | 39 | 0 | 0.0% | 0.0% | 0.0% | 0.22 | 71 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 41 | 41 | 0 | 0.0% | 0.0% | 0.0% | 0.11 | 90 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Both | 80 | 80 | 0 | 0.0% | 0.0% | 0.0% | 0.16 | 28 |
| 9:30 AM open | On the half hour | Whole day | Buy (closed above) | 317 | 317 | 0 | 6.9% | 1.9% | 0.0% | 0.15 | 14 |
| 9:30 AM open | On the half hour | Whole day | Sell (closed below) | 290 | 290 | 0 | 8.6% | 2.8% | 0.0% | 0.05 | 18 |
| 9:30 AM open | On the half hour | Whole day | Both | 607 | 607 | 0 | 7.7% | 2.3% | 0.0% | 0.10 | 7 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 928 | 927 | 1 | 22.4% | 14.1% | 4.5% | 0.22 | 10 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 902 | 897 | 5 | 23.9% | 14.7% | 5.5% | 0.00 | 13 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1830 | 1824 | 6 | 23.1% | 14.4% | 5.0% | 0.12 | 8 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 443 | 443 | 0 | 2.5% | 0.2% | 0.0% | 0.14 | 27 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 446 | 446 | 0 | 4.9% | 0.0% | 0.0% | -0.01 | 37 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 889 | 889 | 0 | 3.7% | 0.1% | 0.0% | 0.06 | 19 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 265 | 265 | 0 | 0.0% | 0.0% | 0.0% | 0.15 | 43 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 292 | 292 | 0 | 0.3% | 0.0% | 0.0% | 0.05 | 49 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Both | 557 | 557 | 0 | 0.2% | 0.0% | 0.0% | 0.10 | 20 |
| 9:30 AM open | Any minute | Whole day | Buy (closed above) | 1636 | 1635 | 1 | 13.4% | 8.1% | 2.6% | 0.19 | 7 |
| 9:30 AM open | Any minute | Whole day | Sell (closed below) | 1640 | 1635 | 5 | 14.5% | 8.1% | 3.0% | 0.01 | 13 |
| 9:30 AM open | Any minute | Whole day | Both | 3276 | 3270 | 6 | 13.9% | 8.1% | 2.8% | 0.10 | 4 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Buy (closed above) | 487 | 469 | 18 | 30.7% | 24.1% | 14.9% | -0.00 | 12 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Sell (closed below) | 477 | 460 | 17 | 32.0% | 22.0% | 13.0% | 0.07 | 9 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Both | 964 | 929 | 35 | 31.3% | 23.0% | 14.0% | 0.03 | 5 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 312 | 312 | 0 | 26.6% | 15.7% | 5.4% | -0.06 | 18 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 315 | 315 | 0 | 23.5% | 14.6% | 6.7% | -0.04 | 20 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Both | 627 | 627 | 0 | 25.0% | 15.2% | 6.1% | -0.05 | 7 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 134 | 134 | 0 | 5.2% | 0.7% | 0.0% | 0.13 | 30 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 114 | 114 | 0 | 6.1% | 1.8% | 0.0% | 0.02 | 35 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 248 | 248 | 0 | 5.6% | 1.2% | 0.0% | 0.08 | 19 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 73 | 73 | 0 | 0.0% | 0.0% | 0.0% | 0.14 | 82 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 85 | 85 | 0 | 0.0% | 0.0% | 0.0% | -0.02 | 42 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 158 | 158 | 0 | 0.0% | 0.0% | 0.0% | 0.06 | 34 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 53 | 53 | 0 | 0.0% | 0.0% | 0.0% | 0.12 | 47 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 43 | 43 | 0 | 0.0% | 0.0% | 0.0% | 0.09 | 69 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Both | 96 | 96 | 0 | 0.0% | 0.0% | 0.0% | 0.11 | 30 |
| 6:00 PM open | On the half hour | Whole day | Buy (closed above) | 1059 | 1041 | 18 | 22.5% | 15.7% | 8.4% | 0.01 | 6 |
| 6:00 PM open | On the half hour | Whole day | Sell (closed below) | 1034 | 1017 | 17 | 22.4% | 14.7% | 8.0% | 0.02 | 7 |
| 6:00 PM open | On the half hour | Whole day | Both | 2093 | 2058 | 35 | 22.4% | 15.2% | 8.2% | 0.02 | 2 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Buy (closed above) | 2551 | 2192 | 359 | 30.9% | 23.6% | 16.6% | 0.08 | 12 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Sell (closed below) | 2555 | 2187 | 368 | 32.9% | 23.0% | 14.4% | -0.03 | 6 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Both | 5106 | 4379 | 727 | 31.9% | 23.3% | 15.5% | 0.02 | 3 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 1730 | 1730 | 0 | 30.0% | 18.0% | 8.6% | -0.13 | 11 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 1760 | 1760 | 0 | 27.0% | 16.1% | 9.1% | 0.02 | 10 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Both | 3490 | 3490 | 0 | 28.5% | 17.0% | 8.9% | -0.05 | 6 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 623 | 623 | 0 | 12.0% | 4.3% | 0.3% | 0.07 | 21 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 620 | 620 | 0 | 10.6% | 2.7% | 0.8% | -0.07 | 19 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1243 | 1243 | 0 | 11.3% | 3.5% | 0.6% | -0.00 | 7 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 361 | 361 | 0 | 0.6% | 0.0% | 0.0% | 0.11 | 27 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 426 | 426 | 0 | 1.6% | 0.0% | 0.0% | -0.05 | 36 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 787 | 787 | 0 | 1.1% | 0.0% | 0.0% | 0.02 | 20 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 341 | 341 | 0 | 0.0% | 0.0% | 0.0% | 0.09 | 31 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 317 | 317 | 0 | 0.0% | 0.0% | 0.0% | -0.01 | 28 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Both | 658 | 658 | 0 | 0.0% | 0.0% | 0.0% | 0.04 | 19 |
| 6:00 PM open | Any minute | Whole day | Buy (closed above) | 5606 | 5247 | 359 | 24.3% | 16.3% | 9.8% | 0.01 | 6 |
| 6:00 PM open | Any minute | Whole day | Sell (closed below) | 5678 | 5310 | 368 | 23.9% | 15.1% | 9.1% | -0.02 | 5 |
| 6:00 PM open | Any minute | Whole day | Both | 11284 | 10557 | 727 | 24.1% | 15.7% | 9.4% | -0.00 | 2 |

## Stop at the opposite edge of the band

The stop sits at the other edge of the band: below the band for a buy, above it for a sell.

| Band built from the | Breakouts looked for | Part of the day | Side | All breakouts | Measured | Left out, stop under 10 points | Reached 2 times the risk | Reached 3 times the risk | Reached 5 times the risk | Average result if held to 4 PM, in risks | Longest stretch with no breakout, trading days |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 191 | 191 | 0 | 0.0% | 0.0% | 0.0% | 0.11 | 14 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 179 | 179 | 0 | 0.6% | 0.0% | 0.0% | 0.01 | 25 |
| 9:30 AM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 370 | 370 | 0 | 0.3% | 0.0% | 0.0% | 0.06 | 10 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 87 | 87 | 0 | 0.0% | 0.0% | 0.0% | 0.05 | 34 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 70 | 70 | 0 | 0.0% | 0.0% | 0.0% | -0.00 | 49 |
| 9:30 AM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 157 | 157 | 0 | 0.0% | 0.0% | 0.0% | 0.03 | 24 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 39 | 39 | 0 | 0.0% | 0.0% | 0.0% | 0.11 | 71 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 41 | 41 | 0 | 0.0% | 0.0% | 0.0% | 0.08 | 90 |
| 9:30 AM open | On the half hour | Afternoon, 2 to 4 PM | Both | 80 | 80 | 0 | 0.0% | 0.0% | 0.0% | 0.09 | 28 |
| 9:30 AM open | On the half hour | Whole day | Buy (closed above) | 317 | 317 | 0 | 0.0% | 0.0% | 0.0% | 0.09 | 14 |
| 9:30 AM open | On the half hour | Whole day | Sell (closed below) | 290 | 290 | 0 | 0.3% | 0.0% | 0.0% | 0.02 | 18 |
| 9:30 AM open | On the half hour | Whole day | Both | 607 | 607 | 0 | 0.2% | 0.0% | 0.0% | 0.06 | 7 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 928 | 928 | 0 | 5.6% | 1.6% | 0.3% | 0.05 | 10 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 902 | 902 | 0 | 7.2% | 2.4% | 0.7% | -0.07 | 13 |
| 9:30 AM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1830 | 1830 | 0 | 6.4% | 2.0% | 0.5% | -0.01 | 8 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 443 | 443 | 0 | 0.0% | 0.0% | 0.0% | 0.03 | 27 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 446 | 446 | 0 | 0.0% | 0.0% | 0.0% | 0.00 | 37 |
| 9:30 AM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 889 | 889 | 0 | 0.0% | 0.0% | 0.0% | 0.02 | 19 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 265 | 265 | 0 | 0.0% | 0.0% | 0.0% | 0.05 | 43 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 292 | 292 | 0 | 0.0% | 0.0% | 0.0% | 0.02 | 49 |
| 9:30 AM open | Any minute | Afternoon, 2 to 4 PM | Both | 557 | 557 | 0 | 0.0% | 0.0% | 0.0% | 0.04 | 20 |
| 9:30 AM open | Any minute | Whole day | Buy (closed above) | 1636 | 1636 | 0 | 3.2% | 0.9% | 0.2% | 0.05 | 7 |
| 9:30 AM open | Any minute | Whole day | Sell (closed below) | 1640 | 1640 | 0 | 4.0% | 1.3% | 0.4% | -0.03 | 13 |
| 9:30 AM open | Any minute | Whole day | Both | 3276 | 3276 | 0 | 3.6% | 1.1% | 0.3% | 0.01 | 4 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Buy (closed above) | 487 | 487 | 0 | 27.7% | 16.2% | 5.7% | -0.14 | 12 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Sell (closed below) | 477 | 477 | 0 | 27.7% | 18.7% | 9.0% | -0.04 | 9 |
| 6:00 PM open | On the half hour | Evening, 6 PM to 2 AM | Both | 964 | 964 | 0 | 27.7% | 17.4% | 7.4% | -0.09 | 5 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 312 | 312 | 0 | 15.4% | 5.4% | 1.6% | -0.02 | 18 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 315 | 315 | 0 | 14.0% | 7.0% | 1.6% | -0.09 | 20 |
| 6:00 PM open | On the half hour | Overnight, 2 AM to 9:30 AM | Both | 627 | 627 | 0 | 14.7% | 6.2% | 1.6% | -0.06 | 7 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Buy (closed above) | 134 | 134 | 0 | 0.0% | 0.0% | 0.0% | 0.06 | 30 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Sell (closed below) | 114 | 114 | 0 | 0.9% | 0.0% | 0.0% | 0.02 | 35 |
| 6:00 PM open | On the half hour | Morning, 9:30 to 11:30 AM | Both | 248 | 248 | 0 | 0.4% | 0.0% | 0.0% | 0.04 | 19 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Buy (closed above) | 73 | 73 | 0 | 0.0% | 0.0% | 0.0% | 0.08 | 82 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Sell (closed below) | 85 | 85 | 0 | 0.0% | 0.0% | 0.0% | 0.00 | 42 |
| 6:00 PM open | On the half hour | Midday, 11:30 AM to 2 PM | Both | 158 | 158 | 0 | 0.0% | 0.0% | 0.0% | 0.04 | 34 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Buy (closed above) | 53 | 53 | 0 | 0.0% | 0.0% | 0.0% | 0.06 | 47 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Sell (closed below) | 43 | 43 | 0 | 0.0% | 0.0% | 0.0% | 0.05 | 69 |
| 6:00 PM open | On the half hour | Afternoon, 2 to 4 PM | Both | 96 | 96 | 0 | 0.0% | 0.0% | 0.0% | 0.05 | 30 |
| 6:00 PM open | On the half hour | Whole day | Buy (closed above) | 1059 | 1059 | 0 | 17.3% | 9.1% | 3.1% | -0.05 | 6 |
| 6:00 PM open | On the half hour | Whole day | Sell (closed below) | 1034 | 1034 | 0 | 17.1% | 10.7% | 4.6% | -0.05 | 7 |
| 6:00 PM open | On the half hour | Whole day | Both | 2093 | 2093 | 0 | 17.2% | 9.9% | 3.9% | -0.05 | 2 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Buy (closed above) | 2551 | 2506 | 45 | 28.8% | 19.5% | 8.5% | -0.02 | 12 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Sell (closed below) | 2555 | 2508 | 47 | 26.9% | 18.0% | 9.9% | -0.16 | 6 |
| 6:00 PM open | Any minute | Evening, 6 PM to 2 AM | Both | 5106 | 5014 | 92 | 27.9% | 18.7% | 9.2% | -0.09 | 2 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Buy (closed above) | 1730 | 1730 | 0 | 18.7% | 7.9% | 1.7% | 0.01 | 11 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Sell (closed below) | 1760 | 1760 | 0 | 14.8% | 9.0% | 2.7% | -0.11 | 10 |
| 6:00 PM open | Any minute | Overnight, 2 AM to 9:30 AM | Both | 3490 | 3490 | 0 | 16.8% | 8.4% | 2.2% | -0.05 | 6 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Buy (closed above) | 623 | 623 | 0 | 1.8% | 0.2% | 0.0% | -0.00 | 21 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Sell (closed below) | 620 | 620 | 0 | 1.8% | 0.5% | 0.0% | -0.07 | 19 |
| 6:00 PM open | Any minute | Morning, 9:30 to 11:30 AM | Both | 1243 | 1243 | 0 | 1.8% | 0.3% | 0.0% | -0.04 | 7 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Buy (closed above) | 361 | 361 | 0 | 0.0% | 0.0% | 0.0% | 0.04 | 27 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Sell (closed below) | 426 | 426 | 0 | 0.0% | 0.0% | 0.0% | -0.01 | 36 |
| 6:00 PM open | Any minute | Midday, 11:30 AM to 2 PM | Both | 787 | 787 | 0 | 0.0% | 0.0% | 0.0% | 0.01 | 20 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Buy (closed above) | 341 | 341 | 0 | 0.0% | 0.0% | 0.0% | 0.03 | 31 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Sell (closed below) | 317 | 317 | 0 | 0.0% | 0.0% | 0.0% | -0.01 | 28 |
| 6:00 PM open | Any minute | Afternoon, 2 to 4 PM | Both | 658 | 658 | 0 | 0.0% | 0.0% | 0.0% | 0.01 | 19 |
| 6:00 PM open | Any minute | Whole day | Buy (closed above) | 5606 | 5561 | 45 | 19.0% | 11.2% | 4.4% | -0.00 | 6 |
| 6:00 PM open | Any minute | Whole day | Sell (closed below) | 5678 | 5631 | 47 | 16.8% | 10.9% | 5.2% | -0.12 | 5 |
| 6:00 PM open | Any minute | Whole day | Both | 11284 | 11192 | 92 | 17.9% | 11.1% | 4.8% | -0.06 | 2 |
