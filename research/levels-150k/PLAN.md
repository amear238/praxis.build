# Marked levels, automated orders: the plan for the widened research pass

Written 2026-11-18, before any code or result of this pass. Amear's ruling of 2026-11-18 (RULINGS.md, "His own chart marking, automated execution"): he may mark levels or zones himself, outside trading hours, on 15-minute or longer charts; the automation places every entry, stop and exit during the session. Task `Praxis_build-8h5`.

## In plain English

- Before the session, levels are marked on the chart: yesterday's high and low, the overnight high and low, last week's high and low, recent swing highs and lows, round numbers, last session's volume levels, and supply and demand zones.
- During the session, the automation rests an order at each level. When price comes to a level, it buys at support or sells at resistance, with a stop-market order just beyond the level, and a target several times the risk.
- His hand marks cannot be replayed on 2018 to 2026. So every kind of level is first drawn by a written rule a computer can follow, and that rule is backtested against the same five pass/fail tests as before.
- If a version passes, he marks 40 past days blind, with the chart cut off at the session's start. His marks drive orders only if they match the rule's closely enough for the backtest to stand for them. Until then the rule's own levels drive the orders, and his marks are logged beside them so he can learn.

## The bars (unchanged from the last three passes; not moved to fit a result)

The $150,000 MyFundedFutures evaluation frame: $4,500 end-of-day trailing limit, the intraday low counted against it. Each version is judged on all five, reported separately, never blended:

1. Every simulated order matches the version's written rule (an independent replay, zero breaks).
2. The average winning trade is at least twice the money risked on it, and the version makes a profit on 2024-01-01 onward alone (its winners there also at least twice the risk).
3. Never more than seven trading days without a new trade (counted on the whole portfolio).
4. Net profit at least $9,000.
5. The $4,500 trailing limit crossed in at most 5% of 10,000 shuffles of whole days (seed 20261115), and never in the real order.

Fills: midpoint stop fills judged (ruled 2026-11-17); kind and harsh reported beside. Judged by `research/noise-area-variations/gates.judge(limit=4500)` and `run_150k.info`, unchanged, as the trend pass was.

His trading rules hold in every version: the cost of each trade is a set percentage of the account's realised balance, fixed before entry; a stop-market order rests at the broker from the moment of entry; one strategy at a time; nothing goes to execution without enough backtest data. Every position is flat by 3:55 PM New York time, so MyFundedFutures' 4:10 PM close never acts.

## What the published record says

The search (2026-11-18) found no level-based method with a published record of profit after costs. What is published:

- **Prices bounce at support and resistance more often than they cross, and more so after earlier bounces.** Garzarelli, Cristelli, Pompa, Zaccaria and Pietronero, "Memory effects in stock price dynamics: evidences of technical trading", Scientific Reports 4, 4487 (2014); arXiv 1110.5197. Statistical, not a profit test.
- **Trends tend to stall at support, resistance and round numbers, and to speed up once through them.** Take-profit orders cluster at round numbers, stop-loss orders just beyond. Osler, "Support for resistance: technical analysis and intraday exchange rates", FRBNY Economic Policy Review (2000); Osler, "Currency orders and exchange rate dynamics", Journal of Finance 58(5), 1791-1819 (2003). Currency dealers' order books, intraday.
- **Support and resistance levels sit where the limit order book is deepest.** Kavajecz and Odders-White, "Technical analysis and liquidity provision", Review of Financial Studies 17(4), 1043-1071 (2004).
- **Breakouts of a trading range made money on daily index data before costs** (Brock, Lakonishok and LeBaron, Journal of Finance, 1992); later studies found that faded after costs and after the late 1980s.
- **Market Profile's "80% rule"** (value area traversal) is claimed at 80%; the one reported backtest (a futures forum, TradeStation) found about 62%. No published study.
- **Failed breakouts ("Turtle Soup", Connors and Raschke, Street Smarts, 1995)**: rules published, no reliable win rate.
- **Prior day and overnight highs and lows**: only practitioner counts (for example, the day session reaches the overnight high or low on about 95% of days). One independent stock test of a prior-day high/low breakout found +0.007R a trade before costs and -0.037R after.
- **Our own record**: the session sweep (NQ, the overnight high or low swept then reclaimed, faded with a 2R target, 2021-2026) lost 0.16R a trade after costs and 0.03R before. Fading the overnight range after a reclaim had no edge even before costs.

So the strongest published mechanism is the bounce at a marked level: an order resting at the level, a stop just beyond it. That is candidate 1. It also fits his ruling best: the marks are levels and zones, and the automation's job is to rest orders at them.

## The candidates, in order (one strategy at a time)

1. **Fade the first touch of a marked level** (this plan's exact rule below). All seven kinds of level are variations of this one strategy, measured side by side.
2. **Break and retest.** A level closed through on the 15-minute chart, then the first return to it from the other side, traded in the direction of the break (Osler's acceleration plus role reversal).
3. **Value area traversal** (the "80% rule"): the session opens outside the prior session's value area and closes two 30-minute periods back inside; target the other edge.
4. **Acceleration through a level**: a 15-minute close beyond a marked level, entered with a stop order, target three times the risk. Closest to the opening range breakout and Noise-Area, which failed; last.

Out, already tested: the opening range breakout, Noise-Area, the session sweep, trend-following. A later candidate's exact rule is written as an amendment here before its code, only after the one before it has failed.

## How a hand-marked method is backtested

1. Each kind of level is drawn by a written rule (below), from data before 9:30 AM New York time only.
2. The rule's versions are measured and judged like any strategy.
3. **Only for a version that passes all five bars: the blind marking check.** 40 market-days drawn at random (seed 20261118) from 2024-01-01 onward, on the version's markets. For each, he sees the 15-minute and 60-minute charts of the ten trading days before, cut off at 9:30 AM, with no date and nothing after. He marks the levels he would trade. A rule level counts as matched when he marked a level within 0.1 of the market's average daily range of it (a zone: when his zone overlaps it). Reported: the share of the rule's levels he matched, the share of his levels the rule also drew, and the version's result on those 40 days with his levels in place of the rule's.
4. **Which levels drive orders.** His marks drive orders only when both shares are at least 80%. Otherwise the rule's levels drive the orders, and his marks are logged beside them for learning, until a later blind check reaches 80%. (Decided without waiting, reversible: it follows his rule that nothing goes to execution without enough backtest data.)
5. Later, only for a finalist: the marks go to the signal path as a levels file read by the NinjaScript watcher, the same file-drop design as now.

## Data and markets

The eleven markets of `research/trend-150k/specs.py`, traded as micros where a micro exists, with its dollars a point, ticks, commissions ($1.90 a micro, $5.00 for ZN and ZB, round trip), slippage (1 tick per market order for the four currencies and ZN, 2 ticks for the rest) and size caps (90 micros, 9 for ZN and ZB, a trade). To check before any final run: that MyFundedFutures lists every micro used.

Databento 1-minute bars, the volume-ranked front month, 2018-01-01 to 2026-11-15; daily bars from 2010 for the average daily range. Checked 2026-11-18: the minute data changes contract only at 7 or 8 PM New York time, never inside the 9:30 to 4:00 window, and every change joins a daily roll with a known price gap (NQ 35 of 35, CL 106 of 106). Read with `research/trend-150k/mdata.py` and `specs.py`, unchanged.

## Candidate 1: fade the first touch of a marked level. The exact rule

Written for the engine and for the independent check, which is written from this section alone.

**Clock.** Times are New York time. A minute bar's stamp is its start. A minute's session date is the calendar date of its New York wall-clock stamp plus 7 hours (so 6:00 PM Sunday to 4:59 PM Monday is Monday's session). A trading date is a session date with at least one minute stamped from 9:30 to before 3:55 PM. S(D) is every minute whose session date is D. The previous trading date of D is the latest trading date before it.

**One contract a day.** The traded contract on D is the contract of D's first minute stamped at or after 9:30. Every level for D is drawn on that contract's prices. A minute of an older contract is moved by the gaps of the daily rolls from its contract to the traded one (`mdata.back_adjust`'s rolls: the second month's close minus the front's on the bar before the roll), and rounded to the tick. A minute whose contract cannot be joined that way is not used, and a level that needs it is not drawn that day.

**Reference values for D.** P0 = the open of D's first minute stamped at or after 9:30. ATR = the mean of high minus low over the 14 back-adjusted daily bars ending at the last daily bar dated (UTC) before D; none until 14 exist. Stop distance d = k x ATR rounded down to the tick, at least one tick.

**The seven kinds of level** (each drawn from minutes stamped before 9:30 on D; prices on the tick grid):

- **PD, prior day:** the high and the low of S(previous trading date).
- **ON, overnight:** the high and the low of the minutes of S(D) stamped before 9:30.
- **PW, prior week:** the high and the low of every S(D') for the trading dates D' in the ISO week before D's.
- **SW, swing points:** hourly bars on the clock (each holds the minutes stamped in one hour, hh:00 to before hh+1:00) from the minutes of S(D') for the 5 trading dates before D and of S(D) up to the bar ending 9:00, in time order; an hour with no minute has no bar. A swing high is a bar whose high is above the highs of the 3 bars before it and the 3 bars after it; a swing low mirrors. It is drawn when no later minute before 9:30 on D has traded through it (a high: a minute's high at least one tick above it).
- **RN, round numbers:** every multiple of the market's step: NQ 100, ES 50, RTY 25, CL 1.00, GC 25, ZN 0.5, ZB 1, 6E, 6B and 6A 0.0050. For the yen, the futures price of every half yen in dollar-yen: 1 / (0.5 x n), rounded to the tick.
- **VP, prior session's volume:** from S(previous trading date): each minute's volume split equally over the tick prices from its low to its high. The point of control is the price with the most volume (a tie: the one nearest the session's midpoint, then the lower). The value area starts at the point of control and adds, one tick at a time, whichever of the next price above and the next price below holds more volume (a tie: both), until it holds at least 70% of the session's volume. Levels: the value area's top, the point of control, the value area's bottom.
- **SD, supply and demand zones:** hourly bars as for SW, from the 10 trading dates before D and S(D) up to the bar ending 9:00. A60 = the mean of their ranges. A demand zone: a base of 1 to 3 consecutive bars, each with a range at most 0.5 x A60, followed at once by a bar with a range at least 2 x A60 that closes above the base's highest high; the zone runs from the base's lowest low to its highest high. A supply zone mirrors (the impulse closes below the base's lowest low). Where bases of different lengths fit before the same impulse bar, the longest that fits is taken. A zone is drawn when no minute after its impulse bar and before 9:30 on D has traded into it (demand: a low at least one tick below the zone's top; supply mirrors). Its level is the near edge (demand: the top; supply: the bottom).
- **ALL:** every level of the seven kinds at once.

**Which levels are armed at 9:30.** No ATR or no P0: nothing is armed that day. A level below P0 is support (a long); above P0, resistance (a short). A demand zone is armed only as support and a supply zone only as resistance; one on the other side of P0 is not armed. A level within d of P0, or further than 2 x ATR from P0, is not armed. On each side, levels are taken nearest P0 first, and a level within d of one already taken is dropped (in ALL, the nearer to P0 wins whatever its kind). Each armed level trades at most once a day.

**Stop for a trade.** A line level L: the stop is d beyond it (long: L - d). A zone: d beyond its far edge (demand: the zone's bottom - d), so its distance from entry is the zone's width plus d. The trade's stop distance is entry minus stop (long) or stop minus entry (short).

**Entry.** A resting limit order at each armed level from the minute stamped 9:30 to the last minute stamped before 3:00 PM. A long at L fills on the first such minute whose low is at least one tick below L, at L exactly, never better; a short mirrors with the high. At most one position per market at a time. A level traded through by one tick while a position is open, or on the minute a trade exits, is spent with no trade. When one minute trades through two armed levels, the one nearer the minute's open fills, and the other is spent.

**Exit.** A resting stop-market order at the stop and, unless the target is "none", a resting limit at the target = entry plus T times the stop distance (long). Each minute from the entry minute on, in this order:

1. Flat: a minute stamped at or after 3:55 PM closes the trade at its open with one slippage against, kept inside the minute's range (reason "flat").
2. Stop (checked on the entry minute too). Long: if the minute opens at or below the stop it is a gap and the reference is the open; else if the low reaches the stop the reference is the stop. Kind: the reference minus one slippage, not below the low. Midpoint (judged): halfway between the reference and the low, rounded down to the tick. Harsh: the low. Shorts mirror with the high, the tick above.
3. Target (not on the entry minute): the minute's high at least one tick above the target (long), filled at the target exactly (reason "target").

If the minutes end before 3:55 (an early close), the trade closes at the last minute's close with no slippage (reason "flat").

**Money.** Loss for one contract = (stop distance + one slippage) x dollars a point + one commission. Risk = realised balance at the start of the day x risk % / 100 (every market is flat overnight). Contracts = risk / loss for one contract, rounded down, at most the cap; under one contract, the trade is skipped and listed. Planned cost = contracts x loss for one contract. Net = (exit - entry) x side x dollars a point x contracts - commission x contracts, to the cent. Day record: start, end, and low = start + the sum of every trade's worst open loss that day, all at once, never above the lower of start and end. A trade's worst open loss is (its adverse extreme - entry) x side x dollars a point x contracts - commission x contracts, the adverse extreme taken over every minute from its entry minute to its exit minute (the low for a long, the high for a short), except that a flat exit's minute counts only at its fill.

## How the search runs

1. **Measuring pass on 2018-01-01 to 2023-12-31 only**, midpoint fills, every figure in R at one contract (as `research/trend-150k/measure.py`): the eight kinds (the seven and ALL) x stop k (0.1, 0.2, 0.4) x target T (3, 5, none): 72 settings, every market. Reported: trades, win rate, average winner and loser in R, net R after costs and before costs, R by year, longest losing run, most trading days with no new trade, worst day, the size that keeps the $4,500 limit crossed in no more than 1 in 40 shuffles of the days, and the profit projected to 2018-2026 at that size.
2. **Market sets, fixed now.** Each setting is measured on all eleven markets, and on the markets whose net R is positive at that setting in both 2018-2020 and 2021-2023. Nothing else is chosen from the measuring pass.
3. **The squeeze, tested before any full run.** A setting goes on the locked list only if, in the measuring pass, its average winner is at least 2R, it never goes more than 7 trading days without a trade, and its projected profit at the 1-in-40 size is at least $9,000. If none does, candidate 1 fails before the full run and candidate 2 is written up.
4. **A locked list** of at most 12 versions, each a setting, a market set and a risk % set from the measuring pass, committed before the full run.
5. **Full run** on 2018-01-01 to 2026-11-15, all five bars, midpoint judged, kind and harsh beside, plain English and dollars.
6. **Checks.** The engine written test first. The rule check written by a separate agent from this plan alone, without seeing the engine, run against every trade of every measured setting. Two identical runs. Trades read by hand against the raw minutes.

## What this cannot show

- On 1-minute bars the order of events inside a minute is unknown. The rules take the worse side every time: a limit fills only when traded through, the stop is checked before the target, no target on the entry minute. A resting limit can still go unfilled live when the backtest fills it.
- The volume levels are built from 1-minute bars, not trades at each price; the real profile differs.
- Round numbers are the futures prices, not the cash market's (the yen is the exception, by construction).
- 72 settings on eleven markets invite a lucky pick. The profit bar on 2024 onward, which the measuring pass never sees, is the main guard.
- The rule stands for his marking only as far as the blind check shows; until then it stands for itself.
