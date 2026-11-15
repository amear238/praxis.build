# PRAXIS status

Last updated: 2026-11-15.

## The goal

One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets.

Work that does not move toward that is frozen: MyFundedFutures follow-up, the Hermes timer, the project kit, extras on the Windows machine.

## What is done

- The signal path from a signal file to a NinjaTrader order was built and signed off on sim earlier in the year.
- Five strategies were backtested. Four have no fixed maximum loss per trade, so none of them meets Amear's rules as tested.
- The Noise-Area paper was read. In its own words it has no hard stop: it exits at the close, at the opposite band, or on a moving stop.
- The restructure of 2026-11-15: the old agent chain, its lock scripts and the old tracking files are in `archive/2026-11-15/`, unchanged. One session now does the work. Tests are the check.

## What is running

Candidates tested 2026-11-15 against Amear's bars on a 50K account with a $2,000 trailing limit (stand-in). Profit bar: at least $4,000. Survival bar: limit crossed in at most 5% of 10,000 shuffled orders. Headroom: profit divided by the drop in the worst 5% of shuffles; both bars together need 2 or more, at any risk size. Code and tests: `research/intraday-momentum-long/`, `research/orb-5min/`, `research/half-hour-momentum/`.

| | Profit | Per year | Skipped | Survival (shuffles crossed) | Headroom |
|---|---|---|---|---|---|
| Candidate 1, long-only momentum, stop at lower band | $5,317 pass | 1.9% | 1,029 | 24.5% fail | 2.04 |
| V1 to V4, tighter stops, both sides, held to close, 0.5% risk | $6,746 to $22,445 pass | 2.4% to 7.2% | 7 to 568 | 53.8% to 100% fail | |
| Candidate 2, 5-minute opening range breakout, long and short | $8,055 pass | 2.8% | 1 | 100% fail | 0.16 |
| Candidate 3, first half hour into the last half hour, long and short | -$22,157 fail | -10.4% | 34 | 100% fail | -0.87 |

None passes. Candidate 2 (Zarattini and Aziz, 2023) has almost no edge after costs: profit factor 1.02, losing runs of 19, a $20,318 worst drop, $16,829 in 2021 to 2024 and -$3,763 in the unseen 2025 to 2026. Candidate 3 (Gao, Han, Li and Zhou, 2018, with a stop added) lost in every year, before costs as well as after; a close cousin (Baltussen and others, 2021) already lost $76,010 in NinjaTrader on 2026-11-01. Candidate 1's headroom of 2.04 means at about 0.77% risk it would sit exactly on both bars; that is choosing the risk after the result, so it is not counted as a pass. Earlier: Noise-Area with a real stop does not pass ("a pathetic result").

## What is next, in order

1. A different route, not another published intraday rule (the voice agent's caution, borne out by candidates 2 and 3). Candidate 4: Carver's fast mean reversion, every hold closed by the end of the next trading day (the voice agent's default, his to overrule). Settings fixed before the run, same bars plus headroom. Needs a loader for the overnight bars, which the data file already holds (only the regular-hours loader exists), and a shuffle of whole trades rather than days.
2. Set the MyFundedFutures permission rule aside, and re-set the drawdown limit against the personal $10,000 account. The new figure is proposed and work carries on.

## What waits on Amear

1. **The independent check for order code.** The settings file still blocks general-purpose helper agents. An independent check needs one. This is an agent permission, so it needs his word before any code that can place an order is checked.
2. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out. The voice agent suggests masking the screenshot and committing the seven.

Decided without waiting, reversible: the retest ran on 1-minute bars with kind and harsh fills, labelled as such (he was offered the choice and raised no objection). "Steady first" was taken as the version that goes flat at 15:59. Overnight candidates are judged on the same 50K stand-in with the $2,000 trailing limit, so every candidate is measured on one yardstick (his open question; he can switch it to a personal account).

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
