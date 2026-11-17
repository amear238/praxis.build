# Noise-Area breakout variations: design

Date: 2026-11-17. Status: approved by Amear ("approve on both."). No backtest is run until the plan made from this is started in a new session.

## Why

Amear's view, 2026-11-17: no rule-based strategy will win often. So the winners must be big enough to pay for the losers. He wants variations of the Noise-Area breakout backtested until one is found that could be profitable. Deeper testing of that one comes afterwards and is a separate piece of work.

## Goal

Find out whether any variation of the Noise-Area breakout passes all the bars below on the held NQ 1-minute data. Name the best one as the finalist, or say plainly that none passed.

## Not goals

- No NinjaTrader work, no order code, no live or sim trading.
- No tuning of a finalist. That is the next stage.
- No other strategy family. Only variations of the Noise-Area breakout.

## What would make this a failure even if it "works"

- A variation picked because it scored best out of a large number tried (luck, not edge).
- A result that uses information the strategy could not have had at the time (look-ahead).
- A trade whose loss at the stop is bigger than the set cost of the trade.
- Bars moved after seeing results.

## What Amear decided (2026-11-17)

1. The original Noise-Area rules are the starting point. They can be changed.
2. Any trading hours MyFundedFutures allows may be used: 6:00 PM to 4:10 PM Eastern, flat before 4:10 PM.
3. The 2-to-1 bar: the average winning trade must be at least twice the money risked on it. Winners run. There is no fixed profit target requirement.
4. Frequency: there must be at least one setup within every seven trading days.
5. Approach 3 below.
6. Variations of this one strategy do not have to be run one at a time. "One at a time" was about different strategies.
7. A multi-agent setup: one agent tests, an orchestrator checks the result against the bars.
8. The work is planned in this session and run in a new one.

## Approaches considered

1. **One variation at a time, blind.** Pick, fix, run, judge, pick again. Slow, and every next pick is a guess.
2. **Big sweep.** Run every combination and take the best. Fast, but the best of a big sweep is usually luck.
3. **Measure first, then a short fixed list.** Chosen by Amear. One measuring pass shows where big winners actually occur. A short list of variations is fixed from that evidence before any is run.

## Constraints

- Amear's trading rules: the cost of the trade is a set percentage of the current balance, fixed before entry. Every entry has a stop-market order resting from the moment it fills. Slippage past the stop is counted in the cost. Fully rule-based.
- Research runs in Python on the Mac, standard library only, run as `python3 -I -B`.
- Data: the held NQ continuous 1-minute file, all Globex hours, over the range the project's loader already uses (2021-03-08 to 2026-07-17). Path from `PRAXIS_DATA`, default as in `research/noise-area-stop/retest.py`.
- Work goes in its own git worktree on its own branch. Code in `research/noise-area-variations/`.
- No timestamps typed by hand. Plain English in anything Amear reads. Dollars at the contract size.

## The bars

A variation passes only if it passes every bar. The bars are not blended into one score.

| Bar | Rule | Source |
|---|---|---|
| Rule check | Every simulated order matches the variation's written rule. Every entry has a stop-market order. No loss at the stop is above the planned cost by more than the tested slippage allowance. A second run gives the same trades. | CLAUDE.md, his trading rules |
| 2-to-1 | For each trade, R = net result after costs divided by the planned cost of that trade. The average R of the winning trades is 2.0 or more. | Amear, 2026-11-17 |
| Frequency | No stretch of more than seven trading days in a row without an entry. A skipped signal is not an entry. | Amear, 2026-11-17 |
| Profit | Total net profit is at least double the drawdown limit: $4,000 on the stand-in account. | Amear, 2026-11-15 |
| Survival | The trailing $2,000 limit is crossed in at most 5% of 10,000 shuffled orders of the trading days. | Amear, 2026-11-15 |

Calls made by Claude, for Amear to correct:

- **Account frame.** The stand-in from 2026-11-15: a $50,000 account with a $2,000 end-of-day trailing limit. The same definitions and shuffle method as `research/intraday-momentum-long/run.py` (`trailing`, `shuffled`, seed 20261115). Results are also shown for the personal $10,000 account, for information only.
- **The Nov 15 profit and survival bars stay.** The 2-to-1 bar alone does not show profit: the earlier $50-risk retest already scores 2.0 and Amear called that result pathetic.
- **Fills.** Judged on the "harsh-stops" model from `retest.py` (stops fill at the worst price of their minute, 2 ticks of slippage per side on market orders). The "kind" model is reported beside it.
- **Later-years check.** Besides the full period, the 2-to-1 bar and a profit above zero must also hold on 2024-01-01 to 2026-07-17 alone. These years were not used in the measuring pass. They are not truly unseen: earlier runs of Noise-Area and candidate 1 covered them, and the report says so.
- **Size and the cost of the trade.** Micro contracts (MNQ, $2 a point). The variation's rule sets the stop. The loss per contract at the stop is the stop distance plus 2 ticks of slippage on each side plus commission. Contracts = the risk budget (the set percentage of the current balance) divided by that loss, rounded down. Fewer than one contract: the signal is skipped and counted. The planned cost of a trade is contracts times that loss per contract. This is the money risked, and it is what R is divided by.
- **Loss past the stop.** On the "kind" fill model no loss at the stop may be above the planned cost, except when the market opens a bar already past the stop. On the "harsh-stops" model the overshoot cannot be capped, so it is reported: how many stops lost more than planned, and the worst one as a multiple of the planned cost. The profit, 2-to-1 and survival bars are judged with those losses in.
- **Crossing the limit in the real order of days.** If the account crosses the trailing $2,000 limit in the real order of days, the variation fails the survival bar whatever the shuffle figure is. The run carries on to the end so the full figures are still shown.
- **How many variations.** At most eight in the first list. If none passes, one second list of at most eight may be fixed, using only the measuring pass and the first list's results on 2021 to 2023. After that the question goes back to Amear. The report always states how many variations were tried in total.

## Stage 1: the measuring pass

Places no trades and keeps no account. Uses 2021-03-08 to 2023-12-31 only.

For every time price closes outside the noise band, anywhere in the 6:00 PM to 4:00 PM window, record:

- date, time, side, the band width at that moment, and which part of the day it falls in (evening 6 PM to 2 AM, overnight 2 AM to 9:30 AM, morning 9:30 to 11:30, midday 11:30 to 2 PM, afternoon 2 PM to 4 PM);
- for each of a small set of stop distances (half the band width, the full band width, back to the anchor price, the opposite band), how far price then ran in favour, measured in multiples of that stop distance, before the stop would have been hit or the session went flat, and where price stood at the flat.

One breakout is the first close outside the band after price was inside it (or after the session starts). It is not counted again until price has closed back inside the band.

The 6:00 PM band: the anchor price is the 6:00 PM open alone. The band width at each minute is the average, over the last 14 sessions, of the move from that session's 6:00 PM open to the same minute. A variation that uses this band uses it for the whole of its trading hours, and its VWAP starts at 6:00 PM too. The two bands are never mixed inside one variation.

Breakouts are measured two ways: on the half-hour marks only (the original rule) and on any minute. The band is built two ways: anchored at the 9:30 AM open (the original rule) and anchored at the 6:00 PM open, so the evening and overnight hours have a band of their own.

Output: one table per stop distance, by part of day and side, showing how many breakouts there were, what share reached 2, 3 and 5 times the risk before being stopped, and the average result if held to the flat. Also the longest stretch of trading days with no breakout in each part of the day, for the frequency bar.

## Stage 2: fix the list

From the tables, write up to eight variations. Each is a settings file that states every rule in full: hours, band anchor, entry rule, stop placement, exit rule, sides, most trades per day, risk percentage, flat time. Each file gives the one-line reason from the measuring pass for trying it. All settings files are committed before any variation is run. Nothing in them changes afterwards.

Levers the list may use: trading hours; band anchor; band width multiplier; half-hour or any-minute entry; stop placement; exit rule (the original band-or-VWAP trailing exit, holding to the flat, or a trailing stop measured in multiples of the risk); long, short or both; most trades per day; risk percentage. Every variation is flat by 4:00 PM Eastern at the latest and takes no entry between 4:00 PM and 6:00 PM.

## Stage 3: run and judge

All variations in the list are run on the full period. They may be run side by side. For each: the trade list, the five bars, results year by year, win rate, average winner and average loser in dollars and in multiples of the risk, longest losing run, skipped signals, worst drop.

## Stage 4: verdict

One plain-English table of all variations against the five bars. If one or more passes, the one with the widest margin on the survival bar is named the finalist and the work stops for Amear. If none passes, the second list is allowed once; then the verdict is that Noise-Area is dead under these bars.

## The agents

Three roles. Checks are about numbers and rules only, never about the form of a report.

| Role | Does | Model, effort |
|---|---|---|
| Lead (the session Amear starts) | Holds the plan. Fixes the variation list from the measuring tables. Recomputes every bar from the raw trade lists with its own short script. Writes the verdict and updates STATUS.md. Writes no engine code. | Fable 5.2, high |
| Tester | Writes the measuring pass and the backtest engine, test first, then runs them. Hands back trade lists and result files. Does not judge pass or fail. | Opus 5.5, high |
| Checker | Did not write the engine. Reads the engine for look-ahead and for orders that break a variation's rule. Picks trades at random from each list and re-derives them by hand from the price data. Reports only defects with the evidence. | Fable 5.2, high |

A different model for the tester and the checker gives the check a second pair of eyes. The backtest runs themselves are plain Python: the model does not change their numbers.

Needs Amear's word before the new session starts: the project settings file blocks general-purpose helper agents. The tester and checker need that block lifted, or two named agents added. Either is an agent permission.

## Left to the builder

- Whether to extend the loaders in `scripts/wf/oracle/` (built for a 9:31 AM session start) or write a small loader for the full Globex day. The noise band for the 9:30 anchor must reproduce `band.py` exactly; a test proves it.
- File layout inside `research/noise-area-variations/`.
- The exact set of stop distances and day parts in the measuring pass may be widened, not narrowed.
- How holidays and half days are handled, stated in the code and tested.

## Known state

- Results for the stop-distance versions and for candidates 2 to 4 sit on worktree branches that are not merged into main. This work does not touch them.
