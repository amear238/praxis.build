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

Candidate 1 (long-only intraday momentum) and eight variations, tested 2026-11-15 against Amear's bars on a 50K account with a $2,000 trailing limit (stand-in). Profit bar: at least $4,000. Survival bar: limit crossed in at most 5% of 10,000 shuffled orders. Code and tests: `research/intraday-momentum-long/` (`variations.py`, then `stop_distance.py` for D1-D4).

| | Profit | Per year | Skipped | Survival (shuffles crossed) |
|---|---|---|---|---|
| Candidate 1, stop at lower band, 1% | $5,317 pass | 1.9% | 1,029 | 24.5% fail |
| V1 stop at day's starting level, 1% | $19,993 pass | 6.5% | 7 | 100% fail |
| V4 same, 0.5% | $6,746 pass | 2.4% | 568 | 53.8% fail |
| D1 candidate 1, stop moved up instead of skipped, 1% | $9,729 pass | 3.4% | 0 | 84.8% fail |
| D2 stop set by the cost, one micro, 0.25% | $13,025 pass | 4.4% | 0 | 26.6% fail |
| D3 day's starting level or the cost, nearer one, 0.25% | $12,968 pass | 4.4% | 0 | 27.4% fail |
| D4 day's starting level, skip if too far, 0.25% | -$445 fail | -0.2% | 2,230 | 0.1% pass |

V2 (long and short) and V3 (held to the close) were like V1: 100% fail. None passes both. D2 is the best yet but crossed the limit in the real order too (April 2025 sell-off). The cost of each trade grows with the balance while the limit stays $2,000. On the personal $10,000 account, 0.25% is $25, an 11-point stop on one micro: too tight to trade. Earlier: Noise-Area with a real stop does not pass ("a pathetic result").

## What is next, in order

1. Restart the strategy search with the cost-of-the-trade rule built in. One strategy at a time. Candidate 1 is closed: a smaller cost for D2 would be picked from these results, and 2025-2026 has now been looked at for nine versions, so it is no longer an unseen check.
2. Set the MyFundedFutures permission rule aside, and re-set the drawdown limit against the personal $10,000 account. The new figure is proposed and work carries on.

## What waits on Amear

1. **The independent check for order code.** The settings file still blocks general-purpose helper agents. An independent check needs one. This is an agent permission, so it needs his word before any code that can place an order is checked.
2. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible: the retest ran on 1-minute bars with kind and harsh fills, labelled as such (he was offered the choice and raised no objection). "Steady first" was taken as the version that goes flat at 15:59.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
