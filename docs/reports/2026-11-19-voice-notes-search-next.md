# Voice notes: where the strategy search goes next, 2026-11-19

Answers to `docs/reports/2026-11-19-voice-brief-search-next.md`, from the voice call of 2026-11-19, about 07:10 to 07:35 ET. Per-answer times were not captured. The voice agent had no repo access and worked from a call pack (a copy of the brief, rulings, status and verdicts). These notes were written by the Claude Code session at 07:37 ET (read from `date`), from the handoff written after the call by the Claude.ai session that ran it. His words are as the transcript caught them, as that handoff relays them. The voice agent's own sentences are not his rulings; only his words are.

## Topic 1: the bars

**Re-running.** Told that 36 Noise-Area runs and the other strategies' versions had been tested, and asked whether he wanted them run again:

> "Then no, I don't want to run them again because it's just a waste of time."

Reading, not his words: nothing is re-run. He did not say in so many words that the bars stay. His 2026-11-17 line ("Why would I want to change any of them?") stands unless he changes it. Ask again in the next brief.

**The seven-day bar.** Asked which reading he meant (the strategy's own setup within seven trading days, or the firm's rule: any trade within seven calendar days), the transcript shows the reply "Affirms rule." Asked to be exact about a small trade placed only to stay active, it shows "Yeah."

Reading, not his words: the firm's rule, any trade within seven calendar days. Not confirmed in a sentence of his own. Whether the firm accepts a trade placed only to stay active was never checked.

**Risk size.**

> "So if if there is a $4,500 uh, max loss, uh, there could still be uh, uh, $225 risked per trade."

That size was already run. W2 at $225 a trade (the "room" version) crossed the $4,500 limit on 2022-11-29 and in 99.8% of shuffles. Its worst drop was $14,428 (recomputed today from `research/noise-area-variations/out/150k/W2-room/judge.json`).

**The nearest miss.**

> "Yeah, but $9,000 or less than $9,000 over a five-year period is fucking pathetic."

## Topic 2: buying finer data

Not answered.

## Topic 3: testing his own chart marks

Not answered. The pivot below changes its context. Reading, not his words: his marks would now be one possible part of a strategy he executes himself, not inputs to the automation.

## What he asked for during the call

### A check from 2023 onward

After asking when the markets "actually started to open up":

> "can you check, let's say that each of these accounts were to be tested from January 1st of 2023 till the nearest um, the nearest like date we have."

> "Test what the P&L would be and whether it would fall under the pass for criteria or not."

On the other strategies: "Yeah, do that for all of them. But when you check, just do the math. You don't need to actually run the, the thing, do you?"

The Claude.ai session did the math on the saved result files. The Claude Code session recomputed every figure below on 2026-11-19 with the handoff's script and the measurement files, and they matched. One correction: from 2023, every percentage and room version of Noise-Area crossed the limit in 100% of shuffles. The handoff's 99.8% is W2's room version over the full period.

**Noise-Area, 2023-01-03 to 2026-07-17 (905 trading days).** The 36 saved results were re-judged on trades from 2023 on, re-based to a $150,000 start. The fixed-dollar versions are exact. The percentage and room versions are approximate, because their size followed the balance built since 2021. **No run passes all five bars.**

| Version | Profit from 2023 (bar $9,000) | What fails |
|---|---:|---|
| V1, fixed $500 / percentage / room | $20,522 / $72,774 / $56,867 | survival (100% of shuffles; first cross 2023-03-03 at the fixed size); 8 days with no trade |
| W2, fixed $100 | $2,135 over 408 trades (2023: $2,087; from 2024: $48) | profit; 26 days with no trade. It passes winners (2.31 times the risk) and survival (never crossed; 3.5% of shuffles) |
| W3, fixed $150 | $2,288 | 26 days; crossed 2024-03-19 |
| V7, fixed $125 | $3,289 | 14 days; survival (34% of shuffles) |
| V2, V6, fixed | $107, $29 | |
| V3, V4, V5, V8, W1, W4, fixed | lose $797 to $4,255 | |
| Every percentage and room version | V1, V6 and V7 make money; V7-room the most after V1, $6,582 | survival: 100% of shuffles |

**The other strategies** were measured only to the end of 2023: the levels, momentum and trend passes from 2018, the opening range breakout from 2021-03-08. So only 2023 can be sliced. The figure is 2023's net, in units of risk, times the safe size: the size that keeps the limit crossed in at most 1 of 40 shuffles. All markets together. These are projections, not replays. The winners and the longest stretch with no trade are for the whole 2018 to 2023 measurement.

| Strategy (versions) | Positive in 2023 | Best 2023 profit |
|---|---:|---|
| Momentum into the close (12) | 0 | lost $610 |
| Levels 1, fade the first touch (72) | 5 | $1,873 (winners 0.54 of the risk, 137 days with no trade) |
| Levels 2, break and retest (72) | 1 | $153 |
| Levels 3, value area (9) | 8 | $1,374 (winners 0.74, 29 days) |
| Levels 4, acceleration (24) | 1 | $46 |
| Trend, same day (72) | 0 | lost $30 |
| Trend, multi-week (36) | 11 | $764 (20 days) |
| Opening range breakout (108) | 29 | $1,833 (winners 0.98; picked after the fact) |

No single market reaches $9,000 either. The closest is the euro in the fade test, about $8,814, from 2 trades in six years (1,272 days with no trade).

### The pivot

After being told nothing passes from 2023 either:

> "at this point, I would like to uh, find a strategy I want to like uh, temporarily retire the um, idea of completely non-discretionary but I want to find a strategy that is fully executed by human"

> "uh, but there has to be like some sort of a Um, there has to be like some sort of a ability to um, like if eventually I, I would like to slowly uh, teach an AI model, whether it be a visual model or something like that, to be able to assist with the execution. If I'm actually pulling the trigger myself or doing some intervention or checks, that's totally fine. Um, the reality is, uh, I feel like getting a full strategy to operate with AI execution on its own is pretty ambitious since, uh, market makers spend billions of dollars a year to, uh, have algo traders and, or al algorithmic, uh, bots in the markets to do fake outs. Manipulate markets and all that shit. So, um, I think I'm ready to retire the idea of uh, full automation."

> "Especially when I'm not directly engineering it. So, what I want the code agent to now do, or actually, what's better than the code agent, since this is not a coding task, um, is uh, I would like the, uh, to run a couple. Uh, research agents uh, to find strategies that a you know steak and potatoes day trader would adopt. The thing is, is there's a lot of influencer bullshit that teach strategies, and they could show like wins in the short term, that's something I fell for before, and then I've lost accounts. Um, so yeah. uh, I I think What I would like you to do at this point is to give me two handoffs, one for the code agent to update everything, and then two for the um, for one agent or two agents in the Claude AI chat to do some research on these. Um, I think the best thing is for the Claude AI chat is to interview me prior.."

Readings, not his words:
1. The 2026-11-14 commitment to fully automated execution is paused. He said "temporarily retire" once and "retire" once. Both are recorded as said; this is not a permanent change.
2. A human places the orders. An AI model, a visual model for example, may later assist "slowly" with execution, checks or interventions. AI in trade decisions was already allowed if backtested (2026-11-17).
3. The research is not coding work. It goes to research agents in the Claude.ai chat, after an interview of him (the second handoff).
4. "Steak and potatoes" means ordinary, widely used day-trading strategies, vetted against influencer material, whose short-term wins have fooled him before.

## Voice-agent statements to treat with care

- It said "from memory" that the percentage runs risked around one percent of $150,000. Only V1 did ($1,500 a trade). W2's percentage version risked $300 at the start (`research/noise-area-variations/out/150k/VERDICT.md`, "Same percentage of the account").
- It said the worst drop at the $225 size was about $14,400. That is right: $14,428.

## For the next session

- Nothing is re-run. His rulings from this call are filed in `RULINGS.md`, "Human execution, automation paused (2026-11-19)".
- What the pivot leaves open is listed in `STATUS.md`, "What waits on Amear". A next voice brief is written only if he asks, one question at a time.
- The interview and the research run in the Claude.ai chat.
