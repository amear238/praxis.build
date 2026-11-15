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

On 2026-11-15, asked whether to save an AI "sit out today" filter as a parked idea: "No." No AI in trade decisions.

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

