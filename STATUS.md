# PRAXIS status

Last updated: 2026-11-15, 14:20 ET.

## The goal

One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets.

Work that does not move toward that is frozen: MyFundedFutures follow-up, the Hermes timer, the project kit, extras on the Windows machine.

## What is done

- The signal path from a signal file to a NinjaTrader order was built and signed off on sim earlier in the year.
- Five strategies were backtested. Four have no fixed maximum loss per trade, so none of them meets Amear's rules as tested.
- The Noise-Area paper was read. In its own words it has no hard stop: it exits at the close, at the opposite band, or on a moving stop.
- The restructure of 2026-11-15: the old agent chain, its lock scripts and the old tracking files are in `archive/2026-11-15/`, unchanged. One session now does the work. Tests are the check.

## What is running

Nothing. No strategy contender yet. The strategy search and the Hermes timer jobs were left paused by the last session (not re-checked today).

## What is next, in order

1. Retest Noise-Area with a real stop-market order placed at entry, in fast Python on the Mac. NinjaTrader confirms only a finalist. Start with the steadier version.
2. Restart the strategy search with the cost-of-the-trade rule built in. One strategy at a time.
3. Set the MyFundedFutures permission rule aside, and re-set the drawdown limit against the personal $10,000 account. The new figure is proposed and work carries on.

## What waits on Amear

1. **Backtest fill accuracy, before step 1.** The 1-minute price bars give fills that are too kind exactly where Noise-Area trades. The old rule froze backtests until that was accepted in writing. Choose: run the retest anyway and label the fills optimistic, hold the retest, or drop the rule.
2. **The independent check for order code.** The settings file still blocks general-purpose helper agents. An independent check needs one. This is an agent permission, so it needs his word before any code that can place an order is checked.
3. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.
4. **Which Noise-Area version is "steady first".** The call notes mapped it to the version that goes flat at 15:59. He did not object; not confirmed.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
