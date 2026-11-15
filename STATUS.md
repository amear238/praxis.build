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

The Noise-Area retest with a real stop. First results are in (2026-11-15), on 1 micro contract, $10,000 start, March 2021 to July 2026, the version that goes flat at 15:59, stop set at 1% of the current balance:

| Fills | Net profit | Profit factor | Worst drawdown | Largest loss |
|---|---|---|---|---|
| Kind (filled at the stop price) | $16,680 | 1.25 | 15.1% | $286 |
| Stops filled at the worst price of the minute | $13,892 | 1.20 | 16.9% | $306 |
| Every order filled at the worst price of the minute | account wiped | 0.35 | 100% | $162 |

- The stop does not hurt the strategy: with no stop it made $15,161 and its largest loss was $649.
- The profit ends when slippage reaches about 3 to 4 points per side. The tests assume half a point.
- The worst drawdown is about 15%, three times the 5% placeholder kill switch.
- 2021 and 2026 were close to flat. Most of the profit came in 2022 to 2025.
- The Python engine reproduces all three NinjaTrader trade lists from 2026-11-01, trade for trade.
- Code and tests: `research/noise-area-stop/`. Not yet tested on real micro-contract data.

## What is next, in order

1. Finish the Noise-Area retest: test it on real micro-contract data, and check real slippage on stops.
2. Restart the strategy search with the cost-of-the-trade rule built in. One strategy at a time.
3. Set the MyFundedFutures permission rule aside, and re-set the drawdown limit against the personal $10,000 account. The new figure is proposed and work carries on.

## What waits on Amear

1. **The drawdown.** The strategy's worst drawdown (15%) is far above the 5% placeholder. Either the limit moves, the risk per trade drops below 1%, or this strategy does not pass.
2. **The independent check for order code.** The settings file still blocks general-purpose helper agents. An independent check needs one. This is an agent permission, so it needs his word before any code that can place an order is checked.
3. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible: the retest ran on 1-minute bars with kind and harsh fills, labelled as such (he was offered the choice and raised no objection). "Steady first" was taken as the version that goes flat at 15:59.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
