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

Candidate 1, long-only intraday momentum, tested 2026-11-15 under Amear's two-branch instruction (50K account, $2,000 limit as a stand-in). Code and tests: `research/intraday-momentum-long/`.

- **Profit (his bar: at least $4,000):** $5,317 over March 2021 to July 2026. Pass, narrowly.
- **Survival:** the $2,000 trailing limit was never crossed in the real order of days (closest: $602 of room, Dec 2022). With the trading days shuffled 10,000 ways, it was crossed in 24.5% of them. No pass number yet; his to set.
- **The catch:** the stop at the lower band is far from the entry, and it grows as NQ rises: about $480 per micro contract in 2021, about $1,020 in 2026. At 1% of $50,000 ($500), 1,029 of 1,344 signals were skipped as too big to take. In the unseen years it made only 33 trades and $278.
- Earlier, Noise-Area with a real stop: does not pass ("a pathetic result", 2026-11-15). Code: `research/noise-area-stop/`.

## What is next, in order

1. Restart the strategy search with the cost-of-the-trade rule built in. One strategy at a time.
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
