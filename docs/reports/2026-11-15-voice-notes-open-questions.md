# Voice notes: open questions from the restructure, 2026-11-15

Written by the Claude.ai Praxis project channel (Claude chat, linked to the Mac), 2026-11-15 about 09:30 ET, for the PRAXIS master.
Source: Amear's voice call that worked through `docs/reports/2026-11-15-voice-brief-open-questions.md`. The call ran between about 08:30 and 09:27 ET. The voice agent had no repo access, so it kept a list and this channel wrote it here at Amear's request ("when we close the chat, then you then write to the repo").
Times: the call transcript has no per-line clock times. Each ruling carries a window: **W1** = 08:28-09:08 ET, **W2** = 09:08-09:27 ET.
Quotes are Amear's words as the voice transcript recorded them (speech-to-text, unedited). Where a ruling is his "yes" to something the voice agent proposed, the proposal is quoted and labelled `AGENT PROPOSAL`. Nothing here is decided by this channel.

This file is not committed, and MANIFEST.md was not touched (the brief allows one notes file and no other repo edit). The master files, audits and commits it.

## 1. New working rule: one strategy at a time (W1)

> "from now on, we're testing one strategy. We're not doing them in bulk. We're not doing. I still want the top three in blah blah blah, but I want the uh, you know, the highest return one."
> "Uh, or the the best one, best candidate. We're gonna test it in multiple ways. We're gonna look at every fucking order."
> "See how it performed. And all that shit."

Later, on whether the second candidate waits for the first: "Yeah, one at a time." (W2)
"Best candidate" was asked twice (highest return, or best fit to his risk rules). He answered "That's fine. Keep going." (W1). He settled it for Noise-Area in section 9: "I'm I'm looking for steady first." (W2)

Context, his words: "I wasn't planning to fucking go live until I actually was confident anyway, so." (W1)

## 2. Test the single candidate on real MNQ data (W1)

AGENT PROPOSAL: "put 'test the single candidate on real MNQ data' on the list."
Amear: "Uh, yeah."
Background he raised: "I'm not actually sure that MMQ and NQ Have the exact same data." All current MNQ dollar figures are "MNQ derived, not an MNQ run" (`2026-11-14-r3-recheck-manager.md`).

## 3. Topic 1, the search loop: stays paused (W1)

> "ideally. Uh, the master puts together a set of questions that are exhaustive enough so that this loop can actually be ran um, reliably."

AGENT PROPOSAL: the loop stays paused; the master writes a full question set; once Amear answers it the loop has every rule it needs; Q1-Q6 start that list.
Amear: "Yeah."
The Nov 13 "Halt all runs until further notice" was not lifted.

## 4. Q1, daily-loss cap: wait-for-data, confirmed (W1)

> "yesterday I agreed to make sure that the uh, what do you call That there must be a stop limit set order at a level. That triggers once price passes that level."
> "As far as the actual figure on what that is, that entirely depends on whether we have a strategy that has been proven to work with MFFU or whatever, um, whatever, whatever like uh, brokerage I'm going to go with, okay, um, so I, I can't set a number right now."

Order type. He first said "stop limit". After the trade-off was explained: "Whichever, whichever is going to get me closest to the price that I want to stop at." Then, after being told a stop-market fires automatically at the broker: **"Okay, then that's what we use."** Read: stop-market order, sitting at the broker, placed at entry.

## 5. Q2, slippage past the stop: it is the cost of the trade (W1)

> "It's it's calculated into the cost of the trade."
> "It's, it's like whatever whatever uh, strategy is put together, back tested to be to give the highest hit rate. Uh, as long as it's predetermined and calculated, and by calculated I mean there's enough testing done. Then that could be a part of the, the cost of the trade."

Consequence (the agent's reading, not ruled): the test has to measure real stop slippage instead of assuming about 0.5 pt.

## 6. Q3, which balance: current balance (W1)

> "Whatever 1% is right now, but considering that um, considering that um, what the drawdown limits are if uh, it's through a prop firm."

Example he was answering: $10,000 at 1% = $100; $90 at $9,000; $110 at $11,000.

## 7. Q4, target account (W1)

> "Right now, we're testing for prop firms."

then, told this reverses yesterday's ruling:

> "Okay, you know what? Let's um, okay, let's keep yesterday's ruling then."

So prop firms stay out for now. Account size: **"Uh, I don't know, let's do 10 grand, I guess."** (personal account, $10,000)
MFFU written-confirmation follow-up: **"Yes, it is still worth chasing."** See section 12: MFFU had already answered.

## 8. Q5, rest of the Floor Rule (W1)

**Post-win protocol.**
> "What happens after a winning streak if it's if this is fully automated uh, you know I don't I don't see the need for uh, too much inter intervention after a winning streak unless you could persuade me that there is need for it."
> "Sure, but it's still it, it's like a part of the strategy is testing scaling up."
> "For now, I, I don't need rules for that because uh, this repo has already been, it already seems like it can't really handle the initial task that it was dedicated with. [...] as far as execution goes, and that's including scaling up, if there's nothing that was back tested with enough data. Then it doesn't, it doesn't happen."
> "I think that's pretty simple, right?"
Read: no waiting-period rule for now. Nothing goes into execution, scaling included, unless it has been backtested on enough data. Percentage scaling follows the current balance (Q3).

**Hard stop time.** "That's entirely dependent on the strategy."

**Account drawdown kill switch.** "I'm gonna say five percent." Then: "Actually, you know what? I'm not, that's a fucking guess. I haven't even done any objective calculations for that." / "so that depend entirely depends on the on the strategy." / **"So let's say for now it would be for five percent."**
Read: 5% from peak is a **placeholder** until a strategy's data sets it. Fact given in the call: four of the five rechecked strategies had a 10-trade losing run (OppBand's longest was 6); at 1% risk, all five would trip 5%.

**Variable to test, not a rule.**
> "Which is after two after two losses, the risk goes from 1% risk to 0.5% risk. Once a win occurs, scaled back to 1%."
He then tried a 0.3% second step and dropped it, and ended: **"uh, no no no no I can't set these rules without backtesting"**. The agent recorded: after two losses in a row, risk 1% -> 0.5%, back to 1% after a win, to be tested on the single candidate.

## 9. Q6, the five rechecked strategies (W2)

> "Yeah, yes, they, they should all be. However, right now, the noise area breakout one, which is the one that showed the most promise, even though it's not too great, should be, uh, It's, it's, I, I want to take that one live first or maybe not live but I want to get it like tested first and maybe test like another candidate that seems promising."

AMBIGUOUS: the question was "retested with a real stop, or all thrown out?" "they should all be" reads as retested, given the rest of the sentence. Confirm with Amear.

**Spec first, then retest with stops:**
> "So then I think that we gotta go back to where we found these fucking strategies. And um, uh, determine like what it was specced out to be. And then t retest them with the stop losses, no? And by the way, that's a question."
The agent answered yes and noted the source paper (Zarattini, Aziz and Barbon) appears to use an interval-checked trailing exit at band/VWAP and no hard stop, so a hard stop is a new variable. On the design having no known max loss: "Then that's not compatible. What kind of, who the fuck wants to trade like that?"
AGENT PROPOSAL: keep the strategy's exit, add a hard stop-market order at entry so the maximum loss is known before the trade, and retest. Amear: **"Uh, yeah."**

**Which version first:** "I'm I'm looking for steady first." The agent mapped that to **Flat1559** (steadiest per this channel's read of the filed figures, below). Amear did not object. Confirm the version name with him.

Facts given, from `2026-11-01-three-strategy-results.md` and `2026-11-01-csv-analyses.md` (1 NQ, 2021-03 to 2026-07, optimistic fills; divide by 10 for a rough MNQ figure):

| | Baseline | OppBand | Flat1559 |
|---|---|---|---|
| Net | $197,327.60 | $210,182.40 | $193,017.60 |
| Max DD (closed-trade) | -$45,282.04 | -$50,748.88 | -$40,637.04 |
| Largest loss | -$5,407.96 | -$19,592.96 | -$5,407.96 |
| 2026 net (partial) | -$3,151.84 | +$12,163.40 | -$3,531.84 |

All three peaked 2025-04-10 and are unrecovered at the last trade, 2026-07-15 (461 days). These filed figures supersede the brief's UNVERIFIED net-profit numbers (about $17,824 / $19,719); filed/10 is about $19,733 / $21,018.

## 10. Topic 3, the parked items (W2)

- **Voice-brief skill (`Praxis_build-61o`).** Amear: "I don't fucking give a shit, to be honest." No word to resume, so it **stays parked**.
- **Gap fade (`Praxis_build-vn4`).** Told it gets retested with a real stop after Noise-Area under Q6, Amear said: "Okay." No separate ruling.

## 11. Two gaps in this morning's brief (this channel's check, not Amear's rulings)

1. The gap fade's $472.90 largest loss is likely understated: the test books every stop at level + 0.5 pt, yet the bar traded past the stop on 273 of 286 stop exits (max 45.5 pt). 1-minute bars cannot show where a real fill would have landed. The voice agent first gave a "$91 extra" figure and then retracted it as overstated.
2. The brief labels its loss figures "at 1 MNQ"; the source labels them "MNQ derived, not an MNQ run".

## 12. MFFU email: hand to the master (W2)

> "Okay, still still add those to the handoff though." / "For the Praxis Master to go for those."

Gmail thread "Pre-purchase question: automated NinjaTrader strategy on evaluation and funded accounts", thread id `1a1ccc24a09baa1f`, 14 messages. Latest: from "[MFFU support rep, name withheld] from MyFundedFutures" ([support address withheld]), 2026-11-13T17:36:47Z, message id `1a1d5fbc33f686ab`, still UNREAD.
As the voice agent read it: unattended automated strategies are allowed on Evaluation and Sim Funded accounts (Rapid, Pro, Builder), provided the strategy does not exploit favourable simulated fills; T1 news trading is allowed on Builder plans, in the evaluation and in Sim Funded. **Read MFFU's exact words in the thread before filing; this channel did not quote them.** This looks like it answers the Q4 follow-up ("still worth chasing").

## 13. Loose ends

- Email this morning: Amear said to disregard everything outside the Praxis repo.
- The master owes the exhaustive question set (section 3) before any loop restart.

Filer's note (2026-11-15, unit 2026-11-15-rulings-filing, praxis-worker for praxis-manager under D-2026-11-08-D D1, per DECISION_LOG 2026-11-15T14:38:00Z): the limitation sentence below was appended at filing under rubric S13. The blank line above it was also added, so the note does not read as part of the last bullet. The text above is unchanged except line 122, where one name and one address were replaced with bracketed placeholders.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
