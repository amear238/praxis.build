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

Four candidates tested 2026-11-15 against Amear's bars on a 50K account with a $2,000 trailing limit (stand-in). Profit bar: at least $4,000. Survival bar: limit crossed in at most 5% of 10,000 shuffled orders. Headroom: profit divided by the drop in the worst 5% of shuffles; both bars together need 2 or more, at any risk size (reported only, never used to set risk). Code and tests: `research/intraday-momentum-long/`, `research/orb-5min/`, `research/half-hour-momentum/`, `research/fast-mean-reversion/`.

| | Profit | Per year | Trades | Skipped | Worst losing run | Unseen 2025-26 | Shuffles crossed | Headroom |
|---|---|---|---|---|---|---|---|---|
| 1, long-only momentum | $5,317 pass | 1.9% | 315 | 1,029 | 10 | $278 | 24.5% fail | 2.04 |
| 2, 5-minute opening range breakout | $8,055 pass | 2.8% | 1,348 | 1 | 19 | -$3,763 | 100% fail | 0.16 |
| 3, first half hour into the last | -$22,157 fail | -10.4% | 1,254 | 34 | 14 | -$3,640 | 100% fail | -0.87 |
| 4, Carver's fast mean reversion | -$9,296 fail | -3.8% | 809 | 366 | 17 | $8,426 | 100% fail | -0.31 |

None passes. Candidate 1's four variations also failed survival (53.8% to 100%). Candidate 4 (Carver's Strategy 27, adapted to one trade at a time with a stop, held at most to the next day's close) lost in 2022, 2023 and 2024; 521 of 809 trades ended at the stop. Its unseen years made $8,426 from a fresh $50,000; inside the full run the balance had fallen, so 366 signals cost more than 1% and were skipped. Candidates 1 to 3 charged stop slippage in their results but sized trades on the stop distance alone, so a full stop cost slightly over 1%; candidate 4 counts it in the size, as ruled. No pass or fail changes. Earlier: Noise-Area with a real stop does not pass ("a pathetic result").

## What is next, in order

1. The research shortlist is used up: its first and third entries failed, the Carver days-to-weeks system is out (no swing trading), and the gap fade and the Asim rules are parked by Amear. Next is a fresh research pass for candidates whose published record shows profit large against losing runs after costs, judged the same way.
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
