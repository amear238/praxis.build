# Voice notes: where the strategy search goes next, 2026-11-17

Answers to `docs/reports/2026-11-17-voice-brief-where-next.md`, from the voice call that ended before 10:38 ET (read from `date`). Per-answer times were not captured. His words are as the voice transcript caught them; "[...]" marks words cut that were not part of the answer.

## Topic 1: which account

> "Hundred and fifty thousand."

Told that most firms use a $4,500 trailing limit at that size and some MFFU plans use $6,000: "Assume that." Later in the call:

> "No, I want it to get rerun on a $150,000 MFFU account. Uh, evaluation rules."

Asked which plan (Rapid or Pro):

> "Whichever one would give a would would would uh, favor the strategy, [...]"

> "That's the full instruction."

Reading, not his words: a $150,000 MyFundedFutures evaluation account, on whichever plan's rules are kinder to the strategy. The voice agent named the Pro plan from the 2026-11-13 research: $6,000 end-of-day trailing drawdown, no daily loss limit, up to 9 minis, a 50% consistency rule. Those figures are two reports old and the reports disagree ($4,500 vs $6,000). Check MFFU's current help pages before the run and pick the kinder plan from what they say now. This brings a prop-firm frame back, newer than the 2026-11-14 and 2026-11-15 rulings that set prop firms aside.

## Topic 2: the bars

> "Why would I want to change any of them?"

Reading: the five bars stay. At $150,000 with a $6,000 limit, "profit at least double the limit" becomes $12,000 (at $4,500 it would be $9,000).

**Fills.** Told that harsh fills take the worst price of the minute:

> "So then let's uh, test it with the average fill."

Offered the midpoint between the stop price and the worst price of the minute, or a fixed slip:

> "The average one, which is in between."

Reading: a stop fills at the midpoint between its price and the worst price of its minute. This replaces the harsh model as the judged fill.

**Profit on 2024 to 2026 alone.**

> "Yes, keep it, man."

## Topic 3: which strategy

> "Noise area is going to be tested again. With the uh, account size, uh, but I would like to before that run goes, I would like the uh, I would like you to look into the repo and or ask uh, or look at the reports and uh, which ones would have passed on a personal account."

**The look into the repo, done 2026-11-17 before the run.** Answer: none passes on the personal $10,000 account. Its drawdown figure was never set; the 5% placeholder is $500, and every version that traded much fell further than that. Only Noise-Area was ever run at $10,000 (figures from `research/noise-area-variations/out/variations/*/*-10000.json` and `research/noise-area-stop/out/`):

| Run at $10,000 | Profit | Worst drop from a high | Note |
|---|---:|---:|---|
| Original rules, 1% risk (2026-11-15 retest), kind fills | $16,680 | $3,402 (15.1%) | his verdict then: "thats a pathetic result" |
| Same, harsh stop fills | $13,892 | $3,215 (16.9%) | |
| V1, kind / harsh | $18,235 / lost $1,789 | 33.4% / 41.7% | |
| V8, kind / harsh | $4,446 / lost $866 | 9.8% / 17.6% | 27 trading days without a trade on kind |
| The other ten | lost up to $552, or no trades | | 0 to 20 trades in five years: one micro contract too big for the risk |

Intraday momentum, the opening-range breakout and the other candidates were run only on the $50,000 frame at about $500 a trade. They were not rerun at $10,000: the price file is outside the folders shared with the voice-call session. Amear then gave the $150,000 instruction above in place of a $10,000 rerun.

## Topic 4: files held back for personal data

Not discussed. Still waiting.

## For the next session

Rerun Noise-Area on the $150,000 MFFU evaluation frame (kinder plan, figures checked on MFFU's site first), midpoint fills judged, the five bars and the 2024-to-2026 check unchanged. No backtest was run in this session.
