# Voice notes: PRAXIS restructure rulings (2026-11-14)

Recorded by the voice-chat agent from the voice session held between about 9:44 and 10:01 AM ET on 2026-11-14, run from `docs/reports/2026-11-14-voice-brief-pivot.md`. Amear's words are quoted exactly as the voice transcript captured them, speech fillers included. The transcript has no per-line timestamps, so every ruling carries the session window, not an exact minute.

This is the only repo file the voice agent wrote. It is NOT committed and NOT in MANIFEST.md; the Code session does both.

## Rulings, verbatim

**R1 — Noon search loop held.** (~9:47 AM ET)
> "I want it held, and I'll stop that. In time."
Later: "stopped the loop already."
Status: Amear says he stopped `praxis-search-loop` himself. The voice agent could not see `~/.hermes/cron/jobs.json` and has NOT verified it.

**R2 — Prop firms set aside for now.** (~9:49 AM ET)
> "let's take out prop firms uh, from the equation for now."
Parked, not decided: option A (change the account) and option E (the MFFU written answer on unattended automation, F4).

**R3 — "The cost of the trade" is the number one rule.** (~9:52 AM ET)
> "the maximum allowed loss for a trade, for now at least, I need it to be looked at as the cost of a trade, as in if the trade is executed, unless there's, uh, you know, let's say the the server crashes or something like that. Uh, it needs to be defined. That's the maximum allowed, uh, maximum amount that's allowed to be risked, but that's also considered the cost of the trade. That is a the biggest, the number one rule here."
> "It doesn't have to be a dollar amount. It's uh, the percentage of the account."
> "That's to be determined when um, we figure out. What's uh thing, but these are just a part of the rules."
Meaning as confirmed back to him: before entry every trade has a predefined maximum loss, set as a percentage of the account. Once the trade executes, that amount counts as spent. The only exception is a technical failure such as a server crash. The percentage is open (TBD). Contract size is worked back from the percentage and the stop distance.
Prompted by Amear's objection: "the rules are to be predefined. And uh, that that strategy does not seem to have a predefined rule ... if some uh, news event hits ... that could mean blowing up an account."
Consequence (voice agent, INFERRED): Noise-Area as tested (trailing-line and close exits, no hard per-trade dollar stop) does not meet R3. Every prior result was run without a hard stop.

**R4 — Recheck the five tested strategies against R3.** (~9:54 AM ET)
Accepting the voice agent's proposal: "Um, yeah, sure, we'll add that to the queue."
The five: three Noise-Area arms, Last-Half-Hour Momentum, the 2026-11-14 gap fade. Purpose: show exactly which past testing fails R3 on day one.
Context, Amear: "the fact that this rule is missing makes me very skeptical that I've been wasting my time for quite a while now."

**R5 — Option C accepted: fast Python screens on the Mac, NinjaTrader only for finalists.** (~9:57 AM ET)
**R6 — Option D accepted: lighter evidence standard for research screens; full audit gates stay for anything that can place an order.** (~9:57 AM ET)
> "Uh, yeah, I accept those as you uh, suggested them."
He accepted both as the voice agent stated them. The draft rule D-2026-11-14-A on the parked branch is the starting point for R5.

**R7 — Max trades per session: rule exists, number set from backtest data.** (~9:58 AM ET)
> "because I'm currently committing to um, uh, non-discretionary trading, which is fully automated,"
> "the max amount of trades, I don't really know what to set to yet because I need the data. As in, once a backtest is done, we need to check. Uh, you know, over a, a span of time, what was the maximum of opportunities not successful trades max amount of opportunities that were presented in a single day and maybe average that somehow."
> "Too early to set that number is my point."

**R8 — Daily loss cap: rule exists, number set later from data.** (~9:59 AM ET)
Asked whether the cap waits for data or is fixed now as a multiple of the cost of a trade, he answered:
> "Yeah, that's it's it's just a rule for the time being until uh, we can get some actual like uh, data put together."
See ambiguity Q1 below.

**R9 — Process instructions for the Code session.** (~10:00 AM ET)
> "if anything seems ambiguous or not well defined, I want it to put together another brief ... that I can come back here to the voice session to answer the questions."
> "I also want you to mention to it to create a skill ... if there's like multiple topics to be discussed, decisions ... where it would automatically give me a brief for a voice message. Or voice chat."

## Handoff to the Code session

Do these in order. Nothing here authorizes spending money, live trading, circuit-breaker changes with money at stake, or installing keys or permissions.

1. **Verify R1.** Confirm `praxis-search-loop` is disabled or held in `~/.hermes/cron/jobs.json`, and record what you see. If it is still enabled, ask Amear before changing it; the 12:00 PM ET run comes first.
2. **Record the rulings.** Log R1 to R9 in DECISIONS.md and DECISION_LOG.md, quoting this file. Add this file to MANIFEST.md. Commit. Note: on reading, the working tree on `main` already had uncommitted changes in nine tracked files plus `.claude/settings.json` that did not come from the voice session. Sort those out under the normal rules before committing this.
3. **Recheck the five strategies against R3 (R4).** For each one: does it have a predefined maximum loss per trade? If not, say so plainly. Where the trade lists exist, also report at 1 MNQ: the largest single losing trade, the average loss, and the longest run of consecutive losers. Label every figure by source (hand run / Mac recomputation / INFERRED).
4. **Make R3 the first filter in the search loop.** A candidate that cannot state its cost of the trade as a percentage of the account is rejected before profit is looked at. Every backtest must also report: the most setups in one day, the average setups per day, and the worst single-day loss at the chosen cost per trade (feeds R7 and R8).
5. **Apply R5 and R6.** Build on D-2026-11-14-A from the parked branch, and define the lighter research-screen standard in writing.
6. **Create the voice-brief skill (R9).** It triggers whenever two or more topics or decisions are waiting on Amear. It writes `docs/reports/YYYY-MM-DD-voice-brief-<topic>.md` in the same form as `2026-11-14-voice-brief-pivot.md`: plain English, contract size named, every figure labelled, the four always-wait items restated, and a "clock" item if anything is time-bound. Propose it to Amear for approval; do not self-certify.
7. **Do not resume the search loop** until steps 2 to 4 are done and Amear has ruled on the questions below.

## Open questions: write these into the next voice brief (R9)

- **Q1, R8 wording.** His "Yeah" could mean "wait for data" or agree to "a multiple of the cost of a trade." Recorded as wait-for-data. Confirm.
- **Q2, the R3 exception.** Is a stop filled past its level by a news gap or slippage still "the cost of the trade", or a breach like a server crash? It decides how the stop is sized and tested.
- **Q3, which balance R3 uses.** Starting balance, current balance, or high-water mark?
- **Q4, the target account.** With prop firms out "for now", what account does testing assume: a personal cash account, and at what size? Is the MFFU F4 follow-up still worth chasing?
- **Q5, the rest of the Floor Rule.** Hard stop time, the account drawdown kill switch, and the post-win protocol were not ruled on today.
- **Q6, R4 outcome.** Once the recheck is done: is any of the five worth rerunning with a hard stop, or are they dropped?

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed (carried from the source brief).
Filer's note (2026-11-14, unit 2026-11-14-pivot-rulings-filing, praxis-worker for praxis-manager under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
