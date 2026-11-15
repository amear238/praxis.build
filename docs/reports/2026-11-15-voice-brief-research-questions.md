# Voice brief: questions before the strategy search, 2026-11-15

Written by the PRAXIS session in Claude Code, 2026-11-15 at 14:51 ET, for the voice-chat agent.

## What Amear wants

His words, typed today: "ask me questions via the voice chat befor ewht eresearch."

The strategy search starts after this call. The aim of the call is a full set of rules, so the search can run without stopping to ask him. Anything he does not answer gets a sensible default, and he is told which.

## How to run it

- Open the call by confirming that this is a safe space where no racism is permitted.
- Plain English. No code names.
- One question at a time. Read the fact, ask the question, give the options. Take his answer and move on.
- You decide nothing. Write his answers in his exact words, with the time, into one notes file: `docs/reports/2026-11-15-voice-notes-research-questions.md`. Edit no other project file.
- Do not write any email address, phone number or support-staff name into the notes file.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

## Where things stand (checked today)

- Noise-Area is finished. Retested with a real stop at 1% of the balance, on one micro contract, $10,000 start, March 2021 to July 2026: about $16,700 profit with stops filled at their price, about $13,900 with stops filled at the worst price of the minute. Worst drop about 15% from a high point, which put the account below $10,000 in late 2021. It wins about $1.20 for every $1 lost, and the profit is gone at 3 to 4 points of slippage per trade. Amear called it "a pathetic result". It does not pass.
- The test engine built today reproduces NinjaTrader's results trade for trade, and it can test any new strategy the same way, with good and bad fills.
- His rules already settled: the cost of each trade is a set percentage of the current balance, about 1% for now; a stop-market order at entry on every trade; one strategy at a time; nothing goes live without enough backtest data; fully automated and rule-based, no AI in trade decisions; personal $10,000 account; prop firms set aside for now.
- The only price data the project has is NQ futures, 1-minute bars, March 2021 to July 2026.

## The questions

### 1. What counts as a good result

He called Noise-Area pathetic. The search needs to know what would not be.
Ask: what is the least he would accept, on $10,000, as a yearly profit in dollars? For example $2,000 a year (20%), $5,000 (50%), or more.
Then: is a strategy that makes that much but has one losing year acceptable, or must every year make money?

### 2. How big a drop he can live with

Fact: his account kill switch is a 5% drop from the high point, set as a placeholder. At 1% per trade, five losers in a row reach it. Noise-Area had losing runs of 10 to 11 trades.
Ask: what is the largest drop from a high point he would accept, in dollars on $10,000? Options: A. $500 (5%, keep the placeholder; the search will likely need a risk per trade well under 1%). B. $1,000 (10%). C. $1,500 (15%). D. Something else.

### 3. Risk per trade and contract size

Fact: 1% of $10,000 is $100. On one micro contract, $100 allows a stop 50 points away. The smallest size is one micro contract, so a tighter stop than the strategy needs cannot be fixed by trading less.
Ask: A. Keep 1% per trade. B. Lower it, for example half a percent ($50), which limits the search to strategies with stops of 25 points or less. C. Something else.
Then: as the account grows, may the system add micro contracts to keep each trade at the same percentage, or stay at one micro contract until he says?

### 4. Surviving bad fills

Fact: 1-minute bars cannot show the exact fill. The engine tests each strategy twice: once with stops filled at their price, once at the worst price of the minute.
Ask: must a strategy still meet his bar from question 1 on the bad fills, or is it enough that it still makes money on them?

### 5. What markets

Fact: the project has only NQ data. Other markets (for example the S&P 500 futures, crude oil, gold) would need new data, which may cost money.
Ask: A. NQ and its micro contract only. B. Also look at other markets, and he decides on any data purchase when it comes up. C. Something else.

### 6. When it trades

Ask, one at a time:
- Day trades only, flat every day before the close, or may it hold overnight?
- Are there hours it must not trade, or hours he wants it flat? (The old plan had a 15:00 to 18:00 lockout for him.)
- Any limit on how often: is one trade a week fine, or does he want something that trades most days?

### 7. What kind of strategy

Ask: anything rule-based is open, or does he want to rule some out? For example: following trends, fading moves back to the average, breakouts at the open, trading around news times, short selling.
Then: should ideas come only from published, tested sources (papers, well-known traders' rules), or may the search build its own?

### 8. Guarding against curve-fitting

Fact: a strategy tuned on the same data it is judged on looks better than it will trade. The usual guard is to tune on the first years (2021 to 2024) and judge on years it never saw (2025 to 2026).
Ask: A. Keep that guard and judge only on the unseen years. B. Something else.

### 9. How much data is enough

Fact: he ruled nothing goes live without enough backtest data. Five years of NQ data is what the project has. Noise-Area made about 1,200 trades in that time.
Ask: is five years enough? Is there a minimum number of trades, for example 200?

### 10. How he wants to hear about it

Ask: A. Only when a strategy passes. B. A short line for every strategy tested, pass or fail. C. Something else.
Then: when one passes, the next steps are a NinjaTrader confirmation and then the full pipeline on a sim account in live markets. Does he want to see the results before each of those steps, or only before sim?

### 11. Anything else

Ask open: is there any rule, wish or worry about the search that these questions missed?

## For the notes file

Close the notes with one line listing any question he skipped, so the session can take a default and tell him.
