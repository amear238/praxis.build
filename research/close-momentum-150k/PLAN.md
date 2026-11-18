# Momentum into the close on the $150,000 frame: the plan

Written 2026-11-18, before any code or result of this pass. Task `Praxis_build-8h5`. The marked-levels plan is finished (all four candidates failed, `../levels-150k/PLAN.md`), so this pass first searched the published record for a family that can meet all the bars at once.

## In plain English

- Each market, each day: if price is up from yesterday's close to 30 minutes before today's close, buy for the last 30 minutes. If it is down, sell. A stop-market order rests from entry. Flat at the close.
- Why this one: it is the strongest published effect not yet tested here. It trades every day on every market, so the 7-day bar is met by design.
- Written before any result: by the published paper's own figures, the edge before costs is about the size of our costs. Only the Nasdaq clears them on that arithmetic. A trade held 30 minutes also has small winners, so the bar of winners at twice the risk needs a tight stop.

## The bars (unchanged; not moved to fit a result)

The same five as the levels and trend passes, on the $150,000 MyFundedFutures evaluation frame ($4,500 end-of-day trailing limit, the intraday low counted): every order matches the rule on an independent replay; the average winner at least twice the risk, with a profit on 2024-01-01 onward alone (its winners there also at least twice the risk); never more than seven trading days without a new trade (whole portfolio); net profit at least $9,000; the trailing limit crossed in at most 5% of 10,000 shuffles of whole days (seed 20261115) and never in the real order. Midpoint stop fills judged, kind and harsh reported beside. Judged by `research/noise-area-variations/gates.judge(limit=4500)` and `run_150k.info`, unchanged.

His trading rules hold: the cost of each trade is a set percentage of the realised balance, fixed before entry; a stop-market order rests from entry; one strategy at a time; nothing goes to execution without enough backtest data.

## What the published record says (search of 2026-11-18)

The need: profit after costs, trades often enough for the 7-day bar across eleven markets, winners at least twice the risk, and every position flat by MyFundedFutures' 4:10 PM New York close.

**Ruled out by the record:**

- **The drift before Fed announcements** (Lucca and Moench, Journal of Finance, 2015): gone after 2015 (Kurov, Wolfe and Gilbert, "The disappearing pre-FOMC announcement drift", Finance Research Letters 40, 2021); none from 2011 to 2017 (Ben Dor and Rosa, 2019). Eight a year in any case. This was the parked task `Praxis_build-ckh`.
- **The drift before other scheduled releases** (Kurov, Sancetta, Strasser and Wolfe, "Price drift before U.S. macroeconomic news", JFQA 54(1), 2019): 9 of 20 releases drift in the 30 minutes before, in the direction of the coming surprise, so the side cannot be known in advance. It weakens once early access to the figures ends (Wolfe, Kurov and Sancetta, "Drift begone!").
- **The overnight drift** (Boyarchenko, Larsen and Whelan, Review of Financial Studies, 2023): the S&P 500 futures return earned around the European open, 2 to 3 AM New York time. Flat in 2021 to 2025 (Federal Reserve Bank of New York, Liberty Street Economics, "The disappearing overnight drift", July 2026).
- **The Treasury auction cycle** (Lou, Yan and Zhang, Review of Financial Studies 26(8), 2013): notes cheapen over the days before an auction and recover after, a few basis points. It needs a hold of several days, which the 4:10 PM close forbids.
- **Currencies weaken in their own trading hours** (Breedon and Ranaldo, Journal of Money, Credit and Banking 45(5), 2013): a few hundredths of a percent a day, below the cost of a micro currency round trip.
- **Crude oil after the weekly inventory report** (Geman and Li, Journal of Energy Markets): the move is over within about 25 minutes and reverts quickly.
- **Already tested here and failed:** Noise-Area (Zarattini, Aziz and Barbon, 2024), the opening range breakout (Zarattini and Aziz, 2023), the session sweep, trend-following, and the four marked-level candidates.

**Still standing: market intraday momentum.**

- Gao, Han, Li and Zhou, "Market intraday momentum", Journal of Financial Economics 129, 2018: on the S&P 500 fund, 1993 to 2013, the first half-hour's return predicts the last half-hour's, out of sample, and after reasonable costs.
- Baltussen, Da, Lammers and Martens, "Hedging demand and market intraday momentum", Journal of Financial Economics 142, 377-403, 2021: over 60 futures, 1974 to May 2020. The return from the previous close to 30 minutes before today's close predicts the last 30 minutes, in all four asset classes. The cause they give is hedging by option dealers and leveraged funds: the effect is strong on days those dealers are short options, and absent on days they are long. Table 6, before costs, trading the sign of that return: equity index futures 6.86% a year (standard deviation 3.96%, right 55% of days), government bonds 2.16%, commodities 4.34%, currencies 0.85%. The authors do not count costs; they write that S&P 500 futures stay positive after a one-tick cost. Table 5, 2000 to 2020 alone: equities, bonds and commodities still significant, currencies not.
- Li, Sakkas and Urquhart, Journal of Financial Markets 57, 2022: the first half-hour predicts the last half-hour in 16 developed stock markets.
- Wen, Indriawan, Lien and Xu, Energy Journal 44(5), 2023: crude oil; on inventory report days the third half-hour predicts the last.
- Against: Rosa (Journal of Futures Markets, 2022) finds the overnight version's predictability gone out of sample. A 2025 Aalto University master's thesis (20 futures, 2008 to 2024) reportedly finds most such strategies not worth trading after costs, bonds and currencies most of all, with most of the effect in the last ten minutes. Read only through a search summary; the page refused automated reading.

**Against our costs (arithmetic before any data).** Table 6's yearly figures are about 2.7 hundredths of a percent a day for equity index futures, 1.7 for commodities, 0.9 for bonds and 0.3 for currencies, before costs. Our round trip (two market orders at the slippage of `specs.py`, plus commission) costs about 1.3 hundredths of a percent on the micro Nasdaq at 15,000 (2.8 at its 2018 price of 7,000), 3.1 on the micro S&P at 4,500, 3.9 on the micro Russell, 8.4 on micro crude, 3.3 on micro gold, 3.2 on the 10-year note, 10 on the bond, and 3 to 6 on the micro currencies. Only the Nasdaq clears the average, and only at recent prices.

So this is the one family left in the record that can trade every week on eleven markets. The record says its edge is thin, and the costs may take it. It is tested because it is the best left, not because it is likely to pass.

## Data and markets

The eleven markets of `research/trend-150k/specs.py` (micros where one exists; the same commissions, slippage and size caps), Databento 1-minute bars 2018-01-01 to 2026-11-15, daily bars from 2010. Read with `mdata.py` and `specs.py`, unchanged. All times New York.

| Markets | Open O | Close C | Following the paper's hours |
|---|---|---|---|
| NQ, ES, RTY | 9:30 | 16:00 | the cash index hours |
| ZN, ZB | 8:20 | 15:00 | the end of the daily settlement period |
| 6E, 6J, 6B, 6A | 8:20 | 15:00 | the same |
| CL | 9:00 | 14:30 | the same |
| GC | 8:20 | 13:30 | the same |

Choice, reversible: the stock index trades are closed at 4:00 PM, not 3:55 PM as in the earlier plans, because the effect is measured to the 4:00 PM close. That is still ten minutes before MyFundedFutures' 4:10 PM close.

## The exact rule

For each market, each trading day d (a New York weekday with minute bars in it):

1. **Reference prices.** "The price at time t" is the open of the first minute bar stamped at or after t and before t + 5 minutes; if there is none, there is no price at t. "The last price before t" is the close of the last bar stamped at or after t − 5 minutes and before t; if there is none, there is none.
2. **Yesterday's close** Y = the price at C on the trading day before d. Choice: if that bar and today's bars are of different contracts (a roll in between), no trade that day.
3. **Signals**, read before entry:
   - S1, rest of day: the last price before C − 30 minutes, against Y (Baltussen and others' strongest).
   - S2, first half hour: the last price before O + 30 minutes, against Y (Gao and others').
   - S3, both: S1 and S2 agree; no trade when they differ.
   Above Y: long. Below Y: short. Equal: no trade.
4. **Entry.** A market order at the price at C − 30 minutes, with slippage against. No price at C − 30, or no price at C (an early close): no trade.
5. **Stop.** A stop-market order rests from the entry minute, at distance d = k × A from the entry fill, rounded down to the tick, at least one tick. A is the average of high minus low over the 14 daily bars before d. It fills as in the earlier plans: midpoint between the stop and the minute's extreme, judged; kind and harsh beside; a minute that opens beyond the stop fills at its open.
6. **Exit.** If the stop has not filled by then, a market order at the price at C, with slippage against. One trade per market per day. No target.
7. **Size.** The cost of each trade, the stop distance plus the slippage of one market order plus commission, is the set percentage of the realised balance, split across the markets trading that day, as in the trend plan.

The grid of the measuring pass: three signals (S1, S2, S3) × four stops (k = 0.025, 0.05, 0.1, 0.2) = 12 settings, on all eleven markets.

## How the search runs (the same method as the last passes)

1. **A pre-screen, before the engine.** For each market and signal, 2018 to 2023 only, no stop: the average of side × (price at C − entry price) in ticks before costs, the share of days right, and the round-trip cost in ticks, for 2018-2020 and 2021-2023 apart. It decides one thing only, fixed now: if the edge before costs is at or below zero on all eleven markets, for all three signals, in both halves, the family is dropped without an engine. A stop cannot make money out of a side with no edge.
2. Otherwise, the usual: an independent rule check written by a separate agent from this plan alone; the engine written test first, with faults planted; the measuring pass on 2018 to 2023; a locked list written before the full run; the full run judged on all five bars; every trade replayed; a byte-for-byte second run; the first trade read by hand.

## What this cannot show

- Fills on 1-minute bars. A market order at 3:30 and at 4:00 PM is filled at the minute's open plus slippage. At the close the real queue can be better or worse.
- The dealers' option positions are not in our data, so the days the paper finds strongest cannot be picked out.
- The paper's figures run to May 2020. Ours run from 2018, mostly after it.

## The pre-screen's result, 2026-11-18 (`out/PRESCREEN.md`)

The drop rule does not fire, so the full method runs, on the grid and markets fixed above, unchanged. What it shows, 2018 to 2023, no stop:

- Only the Nasdaq on the rest-of-day signal (S1) clears costs: 9.5 ticks before costs a trade, against a round trip of 7.8, so +1.7 ticks after, positive in both halves (10.8 and 8.2). That is the one market the paper's figures pointed to before any data was read.
- Every other market and signal loses after costs. The S&P and the Russell are positive before costs on S1 (3.1 and 2.9 ticks) but below their costs (5.5 and 7.8). Bonds and currencies are positive before costs on all three signals, by under 1.2 ticks, against costs of 2.3 to 5.0. Crude and gold have no edge before costs.
- The first-half-hour signal (S2) loses on the Nasdaq in 2021 to 2023 (-17.4 ticks before costs).

Checked: 17 tests, 16 faults planted in the pre-screen and all caught; the first two Nasdaq days of 2018 read by hand against the raw minutes; a second run byte for byte the same.

## Amendment, 2026-11-18, before any engine code: the fills, the size, and what each trade records

Written after the pre-screen and before the engine, so the independent check and the engine read the same words. It spells out rules 4 to 6 and replaces rule 7.

**Ticks.** tick, slip (= slippage ticks × tick), pv, comm and max_qty are the market's in `specs.py`. eps = tick × 10⁻⁶ in every comparison. floor_tick(x) = floor(x / tick + 10⁻⁶) × tick; ceil_tick(x) = ceil(x / tick − 10⁻⁶) × tick. Prices are used raw, never rounded, except where a rule says floor_tick or ceil_tick.

**Entry (rule 4).** The entry bar is the bar that gives the price at C − 30. side = +1 long, −1 short. entry = the entry bar's open + side × slip, then held inside that bar: no higher than its high, no lower than its low.

**Stop distance (rule 5).** A = the mean of (high − low) of the 14 daily bars (back-adjusted, `specs.load`) whose UTC date is before day d; fewer than 14 such bars: no trade. dist = max(floor_tick(k × A), tick). stop = entry − side × dist, raw.

**The minutes the stop watches.** Every minute bar from the entry bar itself up to, not including, the exit bar (the bar that gives the price at C). On each, in time order, for a long (a short mirrors it, with high for low, ≥ for ≤, and ceil_tick for floor_tick):
- if open ≤ stop + eps: it fills, reference = the open, gap = true;
- else if low ≤ stop + eps: it fills, reference = the stop, gap = false;
- the fill: midpoint (judged) = floor_tick((reference + low) / 2); kind = max(reference − slip, low); harsh = low.
The first minute that fills ends the trade: reason "stop".

**Exit (rule 6).** If the stop has not filled, the trade closes at the exit bar's open − side × slip, held inside that bar's high and low: reason "close", gap = false. The exit bar is not checked for the stop.

**Each trade records:** market; date (the New York date d, ISO); signal ("S1", "S2" or "S3"); side; y (yesterday's close Y); s1 (the S1 price, the last price before C − 30) and s2 (the S2 price, the last price before O + 30), each None when that bar is missing; atr (A); dist; entry_ts (the entry bar's time stamp); entry; stop; exit_ts (the time stamp of the minute it closes in: the stop's minute or the exit bar); exit; reason; gap; points = (exit − entry) × side; worst = the lowest of (the adverse extreme − entry) × side over the minutes from the entry bar to the exit minute, where a stop's minute counts whole and the exit bar counts only at its fill, (exit − entry) × side. The adverse extreme is the low for a long and the high for a short.

**Size (replaces rule 7).** As the levels plan's account (`research/levels-150k/fade.account`, which the gate's account check already replays): every trade of a date is sized from the realised balance at the start of that date; risk = balance × risk % / 100; loss a contract = (dist + slip) × pv + comm; quantity = the whole number of contracts that loss fits into risk, at most max_qty; under one contract: skipped. Not split across markets. Rule 7's "split across the markets, as in the trend plan" was written before any sizing code and would have needed a new, unchecked account; this keeps the one already checked.

**The settings.** {"name": "S1-k0.025", "signal": "S1", "k": 0.025, "atr_days": 14}, and so on: the three signals × k in (0.025, 0.05, 0.1, 0.2), 12 in all. Fills: midpoint on all 12 for the measuring pass; the check replays all 12 at all three fills and the account at two sizes.

**Measured as the levels candidates were** (`research/levels-150k/measure.py`): every figure in R at one contract; the eleven markets together and the stable set (the markets with net R above zero in 2018-2020 and in 2021-2023 at that setting); the gate: average winner at least 2R, never more than 7 days with no trade, projected profit at least $9,000.
