# PRAXIS status

Last updated: 2026-11-17.

## The goal

One strategy that passes backtesting on the personal $10,000 account under Amear's trading rules. Then the full pipeline running on a sim account in live markets.

Work that does not move toward that is frozen: MyFundedFutures follow-up, the Hermes timer, the project kit, extras on the Windows machine.

## What is done

- The signal path from a signal file to a NinjaTrader order was built and signed off on sim earlier in the year.
- Five strategies were backtested. Four have no fixed maximum loss per trade, so none of them meets Amear's rules as tested.
- The Noise-Area paper was read. In its own words it has no hard stop: it exits at the close, at the opposite band, or on a moving stop.
- The restructure of 2026-11-15: the old agent chain, its lock scripts and the old tracking files are in `archive/2026-11-15/`, unchanged. One session now does the work. Tests are the check.

## What is running

Candidate 1 (long-only intraday momentum) and four variations, tested 2026-11-15 against Amear's bars on a 50K account with a $2,000 trailing limit (stand-in). Profit bar: at least $4,000. Survival bar: limit crossed in at most 5% of 10,000 shuffled orders. Code and tests: `research/intraday-momentum-long/`.

| | Profit | Per year | Skipped | Survival (shuffles crossed) |
|---|---|---|---|---|
| Candidate 1, stop at lower band | $5,317 pass | 1.9% | 1,029 | 24.5% fail |
| V1 tighter stop (day's starting level) | $19,993 pass | 6.5% | 7 | 100% fail |
| V2 tighter stop, long and short | $22,445 pass | 7.2% | 11 | 100% fail |
| V3 tighter stop, held to the close | $16,795 pass | 5.6% | 6 | 100% fail |
| V4 tighter stop, 0.5% risk | $6,746 pass | 2.4% | 568 | 53.8% fail |

None passes. At 1% risk a trade risks $500, so four losers in a row use the whole $2,000 limit, and every version has losing runs of 6 to 12. Earlier: Noise-Area with a real stop does not pass ("a pathetic result").

## What is next, in order

1. Noise-Area variation search (Amear, 2026-11-17). Design and plan are written and approved; nothing has been run. Start it in a new session with the plan: `docs/superpowers/plans/2026-11-17-noise-area-variations.md`. Bars: average winner at least twice the money risked, never more than seven trading days without a trade, profit at least $4,000, the $2,000 limit crossed in at most 5% of shuffles, every order matching its rule. Task: `Praxis_build-7yq`.
2. Results for the stop-distance versions and candidates 2 to 4 sit on worktree branches not merged into main.

## What waits on Amear

1. Nothing on agents: the block on general-purpose helper agents was lifted on his word, 2026-11-17.
2. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out.

Decided without waiting, reversible: the retest ran on 1-minute bars with kind and harsh fills, labelled as such (he was offered the choice and raised no objection). "Steady first" was taken as the version that goes flat at 15:59.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
