# Amear's rulings

Only Amear's own rulings, in his words, with the date. Newest section last. A ruling stands until he changes it. Spoken quotes are as the voice transcript caught them. Where a line is a reading and not his words, it says so.

Sources are in `archive/2026-11-15/` (the old decisions files) and `docs/reports/` (the call notes).

## What waits for his word (2026-11-08)

> "Only four things stop and wait for Amear's word: (a) spending money; (b) switching live trading on, or any order path to a funded account; (c) changing circuit-breaker values while real money is at stake; (d) installing keys, credentials or agent permissions."

Everything else: take the recommended option, say so, and carry on. His words:

> "When a unit or the master reaches a question that would otherwise go to Amear, it takes the recommended option [...] and continues. Amear may reverse any such decision later"

> "Messages to Amear are plain English. Account figures are shown in dollars at the contract size, not in points or percent alone."

Source: `archive/2026-11-15/DECISIONS.md`, entry D-2026-11-08-D (D1, D2, D10).

Also from that day: agents write every repo file; he does not edit repo files by hand. ("Agents write every repo file", same entry.)

## The trading rules

**The cost of the trade (2026-11-14).**

> "the maximum allowed loss for a trade, for now at least, I need it to be looked at as the cost of a trade [...] it needs to be defined. That's the maximum allowed, uh, maximum amount that's allowed to be risked, but that's also considered the cost of the trade. That is a the biggest, the number one rule here."

> "It doesn't have to be a dollar amount. It's uh, the percentage of the account."

> "the rules are to be predefined."

**Which balance (2026-11-15).** The current balance.

> "Whatever 1% is right now"

Reading: 1% of the current balance is the working figure ($100 on $10,000). He has not fixed the percentage as final.

**The stop (2026-11-15).** A stop-market order, sitting at the broker, placed at entry. Told that a stop-market fires automatically at the broker:

> "Okay, then that's what we use."

**Slippage past the stop (2026-11-15).**

> "It's it's calculated into the cost of the trade."

> "as long as it's predetermined and calculated, and by calculated I mean there's enough testing done."

**One strategy at a time (2026-11-15).**

> "from now on, we're testing one strategy. We're not doing them in bulk."

> "We're gonna test it in multiple ways. We're gonna look at every fucking order."

> "Yeah, one at a time."

**Noise-Area first, with a real stop (2026-11-15).**

> "right now, the noise area breakout one, which is the one that showed the most promise, even though it's not too great, [...] I want to get it like tested first"

On a design with no known maximum loss: "Then that's not compatible." Asked whether to keep the strategy's exit, add a hard stop-market order at entry, and retest: "Uh, yeah." On which version: "I'm I'm looking for steady first."

**Nothing goes to execution without enough backtest data (2026-11-15).**

> "as far as execution goes, and that's including scaling up, if there's nothing that was back tested with enough data. Then it doesn't, it doesn't happen."

**Fully automated, rule-based (2026-11-14).**

> "I'm currently committing to um, uh, non-discretionary trading, which is fully automated"

On 2026-11-15, asked whether to save an AI "sit out today" filter as a parked idea: "No." No AI in trade decisions. (Changed 2026-11-17: AI is allowed if backtested. See "AI in trade decisions" below.) (Widened 2026-11-18: his own chart marking outside trading hours is allowed, with automated execution. See "His own chart marking, automated execution" below.) (Paused 2026-11-19: he wants a strategy "fully executed by human" and to "temporarily retire" the idea of complete non-discretion. See "Human execution, automation paused" below.)

**Numbers that are not set yet.** They come from backtest data.

- Maximum trades per session (2026-11-14): "Too early to set that number is my point."
- Daily loss cap (2026-11-14): "it's just a rule for the time being until uh, we can get some actual like uh, data put together."
- Account drawdown kill switch (2026-11-15): "So let's say for now it would be for five percent." A placeholder, by his own words: "that's a fucking guess."
- Cutting risk after losses (2026-11-15): "I can't set these rules without backtesting"
- Hard stop time (2026-11-15): "That's entirely dependent on the strategy."

Sources: `archive/2026-11-15/DECISIONS.md`, entry D-2026-11-14-B; `docs/reports/2026-11-15-voice-notes-open-questions.md`.

## The account

**Prop firms are out for now (2026-11-14).**

> "let's take out prop firms uh, from the equation for now."

Confirmed 2026-11-15: "let's keep yesterday's ruling then."

**Test against a personal $10,000 account (2026-11-15).**

> "Uh, I don't know, let's do 10 grand, I guess."

**Test the candidate on real MNQ data (2026-11-15).** Asked to put it on the list: "Uh, yeah."

**The drawdown limit.** His 2026-11-08 ruling set it against MyFundedFutures accounts:

> "Max-DD gate = backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit."

On 2026-11-15, asked whether to park the MyFundedFutures permission rule while prop firms are set aside and re-set the drawdown gate against the personal $10,000 account: "Yeah." The new figure is not set yet. It is a testing value: propose it and carry on.

Source for the 2026-11-08 text: `docs/specs/2026-11-06-walk-forward-values.md` line 135.

## How the work is done

**Fast screens on the Mac, NinjaTrader for finalists (2026-11-14).** Offered "Screen candidates quickly in Python on the Mac, and keep NinjaTrader only for confirming finalists" and a lighter standard for research, with full checks kept for anything that can place an order:

> "Uh, yeah, I accept those as you uh, suggested them."

**Unclear things go back to him as a voice brief (2026-11-14).**

> "if anything seems ambiguous or not well defined, I want it to put together another brief ... that I can come back here to the voice session to answer the questions."

**No automation inside the Windows machine (2026-10-30).** He builds there by hand, with steps given one at a time. Not re-quoted here; source: `archive/2026-11-15/DECISION_LOG.md`, row 2026-10-30T21:36:00Z.

**Voice calls open with the safe-space confirmation (2026-11-15).**

> "Safe-space opener: yes, standing rule for every voice call on this project."

Every voice call on this project opens by confirming it is a safe space where no racism is permitted.

## The restructure (2026-11-15)

> "I want to go through a restructuring on how the Praxis master is doing the workflows. This is what caused hiccups months ago that stalled out this project. [...] So the project being about audits, doing audits and all that bullshit, I am ready to let go of that or to do some sort of intervention. Do consider that your ability now is significantly better than it was when that directory was put together. So I think I'm ready to start simplifying things"

On checks that fail work for format reasons: "to either get fixed or to fucking stop that bullshit."

The restructure was written up by the voice agent and he approved it: "Yeah." He then ordered it: "Carry out the section "Instruction for the PRAXIS master: restructure", in the order of work it gives." What it says, in plain English:

- **The one goal:** one strategy that passes backtesting on the personal $10,000 account under his trading rules, then the full pipeline on a sim account in live markets. Other work is frozen.
- **Stopped:** the manager, worker and checker agents; written reports for each piece of work; the rule that set work aside after two failed checks; the many tracking files.
- **In their place:** tests are the check. One independent check, by an agent that did not write the code, only for anything that can place an order. One status page. This list.
- **Unchanged:** the four things that wait for his word; his trading rules; one session per working tree; the safe-space rule; plain English, no code names, one step at a time.

On removing the old locks and archiving the agent files (agent permissions): "Yes, remove the locks".

Left as they were, his "not now": the gap-fade retest and the voice-brief skill.

Asked whether to restart the strategy search with the cost-of-the-trade rule built in, alongside the Noise-Area retest: "Yeah."

Source: `docs/reports/2026-11-15-voice-notes-restructure.md`.

## Noise-Area with a real stop (2026-11-15)

Shown the retest (1 micro contract, $10,000 start, March 2021 to July 2026, stop at 1% of the balance: about $16,700 net on kind fills, $13,900 with stops filled badly, worst drop about 15% from the high point, which put the account below $10,000 in late 2021):

> "thats a pathetic result"

Reading, not his words: Noise-Area does not pass, and the work moves to the next candidate. The other two versions were run the same way and are no better (worst drop 15% and 21%).

## First candidate and how it is judged (2026-11-15)

Pasted by Amear in the Claude Code session, verbatim:

> "Run the first candidate from the mechanical strategy research report: long-only intraday momentum on the held NQ 1-minute data. Stop-market order at entry at the lower band, fixed-percent risk, 2 ticks of slippage per side, settings locked before the run, 2025 to 2026 kept unseen as the final check."

> "Branch A, profit: total backtest profit must be at least double the prop firm's maximum drawdown, whatever that limit is. Use a 50K account with a $2,000 limit as the stand-in until a firm is chosen."

> "Branch B, survival: run the account day by day under the firm's trailing loss rule, using the same $2,000 stand-in. Report whether the limit is ever crossed, and run the shuffled-order simulation to show how often it would be."

> "Do not blend the two branches into one score. Amear set the Branch A bar himself. Branch B has no pass number yet: report the figures and let Amear set it."

Reading, not his words: this brings a prop-firm account back as the test frame (a 50K stand-in), newer than the Nov 14 and Nov 15 rulings that set prop firms aside and used a personal $10,000 account. The research report it names was not found in the repo; the candidate was read as the noise-band breakout, long side only.

## Pass bars for every candidate (2026-11-15)

From the voice call, handed over in his paste block:

> "Amear set the pass bars himself: profit at least double the prop maximum drawdown, and the trailing limit crossed in at most 5% of 10,000 shuffled orders. Propose and test variations of candidate 1, each fixed before the run, and report the results side by side in plain English."

The call notes (the voice agent's words, approved by his paste): survival is "you accepted my suggestion, so the account may cross the trailing loss limit in at most 5% of the shuffled orders"; the two branches stay separate; each variation reports return as a percentage a year and skipped signals; "Don't move the bars to fit a result."


## Noise-Area variations and the 2-to-1 bar (2026-11-17)

Typed by Amear in the Claude Code session, verbatim:

> "last time i was here i realized that there is no trading stratagty that could be encoded and have a high hit rate. i would like fo ryou use superpoers top come upo with a plan to use a variation of the noise area break out stratagy for back testing. the origonal spec is to be used as starting point for variations but not the end all be all. if it follows mffus rules for market availabily or session availability that it can be tried. the minimum return i would persute is 2:1 R:R if it shows that it less than 2R the stratagy is dead or a variation must be tried."

**What 2-to-1 means.** Offered three readings (a fixed target at twice the risk; the average winner at least twice the risk; the average winner at least twice the average loser), he answered:

> "2."

Reading: the average winning trade must be at least twice the money risked on it. Winners run; no fixed target is required.

**Frequency.**

> "Another variable to introduce is that the trade frequency must meet the seven day trading rule which means that there must be at least one set up within seven trading days to comply with the proper firms, trading rules"

**How the search is run.** Offered three ways, the third being a measuring pass first and then a short list of variations fixed before any is run:

> "I can go with three. However, since we are focused on the one strategy, we don't really need to stick with the one at a time. I mentioned the one at a time specifically for like testing different strategies."

**Agents.**

> "I would like to have some sort of multi-agent setup for this, ideally, so that one agent is testing and one orchestrator can check if it meets the criteria."

**Where it runs.**

> "Once the plan is put together, I will start this in a new chat. So just to be clear, no back testing is going to be conducted in this chat."

Reading, not his words: this reopens Noise-Area after the 2026-11-15 "does not pass", for variations judged against the new bars. The design is `docs/superpowers/specs/2026-11-17-noise-area-variations-design.md`.

**Approval (2026-11-17).** Shown the design and asked for his word to lift the settings block on general-purpose helper agents, for the tester and the checker:

> "approve on both."

## Where next after Noise-Area (2026-11-17)

From the voice call on the brief `docs/reports/2026-11-17-voice-brief-where-next.md`. Full notes: `docs/reports/2026-11-17-voice-notes-where-next.md`.

**The account.**

> "No, I want it to get rerun on a $150,000 MFFU account. Uh, evaluation rules."

On which plan: "Whichever one would give a would would would uh, favor the strategy". Reading, not his words: a $150,000 MyFundedFutures evaluation on the plan kinder to the strategy, its rules checked on MFFU's site before the run. This is newer than the 2026-11-14 and 2026-11-15 rulings that set prop firms aside.

**The bars stay.** "Why would I want to change any of them?"

**Fills.** "So then let's uh, test it with the average fill." / "The average one, which is in between." Reading: a stop fills at the midpoint between its price and the worst price of its minute, in place of the harsh model.

**Profit on 2024 to 2026 alone stays a bar.** "Yes, keep it, man."

**Next strategy.** "Noise area is going to be tested again. With the uh, account size"

## AI in trade decisions (2026-11-17)

Typed by Amear in the Claude Code session, verbatim, after being told a neural-network strategy was out under the no-AI ruling:

> "as far as the ai decision stuff it can pass as long as it is back tested"

Reading, not his words: this replaces the 2026-11-15 "no AI in trade decisions" line. A model that makes or filters trade decisions is allowed if it passes the same backtest bars as any rule-based strategy. The trading rules still hold: cost of the trade set before entry, stop-market order at entry, fully automated.

## Trend-following on the $150,000 frame, and more markets (2026-11-17)

Typed by Amear in the Claude Code session, verbatim, after the recommendation to test a trend-follower with a hard stop at entry before any neural network:

> "lets test your recomendation on the 150k account."

> "also, i no longer want to stay in nq alone. we can spread to other futures and forex as long as there is the ability to back test."

Reading, not his words: the trend-follower is judged on the $150,000 MyFundedFutures frame and its bars. The search may now use other futures and forex, provided there is data to backtest them.

Then asked two questions in the session. Told that MyFundedFutures closes every position by 4:10 PM ET, so a weeks-long trend-follower cannot run on that account, and asked which version to test, he chose:

> "Both, side by side"

Reading: a same-day trend version (flat by 4:00 PM) and a multi-week version judged on the $150,000 numbers, reported separately.

Asked where data for markets beyond NQ should come from, he chose:

> "Buy it from a data vendor"

Reading: his yes to buying one-minute history for several markets, offered at about $20 to $100. The exact price is quoted to him before anything is charged.

**What data to buy (2026-11-17).** Offered the broad set (1-minute bars for eleven markets from 2018 plus daily bars from 2010, $122.16, inside the $125 free credit) against the broad set plus a year of second-by-second NQ and ES data for scalping ($224.67), with the advice to buy only the broad set and hold his extra $125 until a scalping strategy is chosen:

> "Okay, I have been overruled by your advice."

Reading: buy the broad set only, $122.16 of free credit. No money of his is spent. The extra $125 waits until a scalping candidate needs data.

## His own chart marking, automated execution (2026-11-18)

Typed by Amear in the Claude Code session, verbatim, after being told that Noise-Area, the opening range breakout, the session sweep and trend-following had all failed on the $150,000 frame:

> "i want to expand the limits of the stratagy at least till we find a stratagy to be one that allows for Technical analysis done by me the human outside of trading hours the strategy I would like to optimize for or what desire here is one where the actual execution intruders are done by the Automation process, and I mark out the charts or spreads myself what this will allow for my physical intervention and understanding of the strategy to potentially and eventuallydevelop skills to have that process even automated so it's not necessarily a fallback, but could even be a blessing in disguise in order for this to work in simplest way. i would propose something with highier time frame chrting like 15min +"

Reading, not his words: this widens the 2026-11-14 "fully automated" commitment, at least until a strategy is found. Amear may mark levels or zones on the charts himself, outside trading hours; the entries, stops and exits are then placed by the automation, with no hand on the order during the session. The aim includes learning the marking well enough to automate it later. Charts of 15 minutes or longer. Unchanged: the cost of each trade set before entry, a stop-market order at entry, one strategy at a time, and nothing goes to execution without enough backtest data, so the marking has to be written as a rule that can be backtested.

(Changed 2026-11-19: the orders are to be placed by a human, not the automation. Reading, not his words: his chart marking is now one possible part of a human-executed strategy. See "Human execution, automation paused" below.)

## Human execution, automation paused (2026-11-19)

From the voice call on the brief `docs/reports/2026-11-19-voice-brief-search-next.md`, about 07:10 to 07:35 ET. Full notes: `docs/reports/2026-11-19-voice-notes-search-next.md`. Spoken quotes are as the transcript caught them, as relayed by the Claude.ai session that ran the call. The voice agent's own sentences are not rulings.

**Nothing is re-run.** Asked whether the tested strategies should be run again:

> "Then no, I don't want to run them again because it's just a waste of time."

Reading, not his words: he did not say in so many words that the bars stay. His 2026-11-17 "Why would I want to change any of them?" stands unless he changes it.

**The seven-day bar.** Asked whether it means the strategy's own setup within seven trading days or the firm's rule (any trade within seven calendar days), the transcript shows "Affirms rule." Asked about a small trade placed only to stay active: "Yeah."

Reading, not his words: the firm's rule, any trade within seven calendar days. Not confirmed in a sentence of his own. Whether the firm accepts a trade placed only to stay active was never checked.

**The nearest miss.**

> "Yeah, but $9,000 or less than $9,000 over a five-year period is fucking pathetic."

**A check from 2023 onward.**

> "can you check, let's say that each of these accounts were to be tested from January 1st of 2023 till the nearest um, the nearest like date we have."

> "Test what the P&L would be and whether it would fall under the pass for criteria or not."

> "Yeah, do that for all of them. But when you check, just do the math. You don't need to actually run the, the thing, do you?"

Reading, not his words: done as math on the saved results. Nothing passes from 2023 either (the notes file).

**Human execution.**

> "at this point, I would like to uh, find a strategy I want to like uh, temporarily retire the um, idea of completely non-discretionary but I want to find a strategy that is fully executed by human"

> "I would like to slowly uh, teach an AI model, whether it be a visual model or something like that, to be able to assist with the execution. If I'm actually pulling the trigger myself or doing some intervention or checks, that's totally fine. Um, the reality is, uh, I feel like getting a full strategy to operate with AI execution on its own is pretty ambitious since, uh, market makers spend billions of dollars a year to, uh, have algo traders and, or al algorithmic, uh, bots in the markets to do fake outs. Manipulate markets and all that shit. So, um, I think I'm ready to retire the idea of uh, full automation."

> "Especially when I'm not directly engineering it. So, what I want the code agent to now do, or actually, what's better than the code agent, since this is not a coding task, um, is uh, I would like the, uh, to run a couple. Uh, research agents uh, to find strategies that a you know steak and potatoes day trader would adopt. The thing is, is there's a lot of influencer bullshit that teach strategies, and they could show like wins in the short term, that's something I fell for before, and then I've lost accounts."

> "I think the best thing is for the Claude AI chat is to interview me prior.."

Readings, not his words:
1. The 2026-11-14 commitment to fully automated execution is paused. He said "temporarily retire" once and "retire" once. Both stand as said; this is not recorded as permanent.
2. A human places the orders. An AI model, a visual model for example, may later assist "slowly" with execution, checks or interventions. AI in trade decisions was already allowed if backtested (2026-11-17).
3. The research is not coding work. It goes to research agents in the Claude.ai chat, after an interview of him.
4. "Steak and potatoes" means ordinary, widely used day-trading strategies, vetted against influencer material, whose short-term wins have fooled him before.

What this leaves open is listed as questions for him in `STATUS.md`, "What waits on Amear". Those questions are not rulings.
