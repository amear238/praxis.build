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

Nothing. The Noise-Area variation search finished on 2026-11-17: **no variation passes; under the five bars Noise-Area is dead.** Full verdict in plain English: `research/noise-area-variations/out/VERDICT.md`.

Twelve variations were tried (a first list of eight, then the one allowed second list of four), each list locked before it was run, on a 50K stand-in account with a $2,000 trailing limit, harsh fills.

| Bar | Result across the twelve |
|---|---|
| Every order matches its rule | 12 pass |
| Average winner at least twice the risk | Met by all 12 (2.0 to 5.9 times), but the bar also needs a profit on 2024 to 2026 and every one lost there ($557 to $19,071) |
| Never more than seven trading days without a trade | 1 passes (and it loses $17,852); the rest run 8 to 30 days |
| Profit at least $4,000 | 4 pass ($4,027 to $10,029) |
| $2,000 limit crossed in at most 5% of shuffles | 0 pass: crossed in the real order of days in all 12, and in 99.8% to 100% of shuffles |

Why: these versions win 2 to 3.5 trades in 10, so losing runs of 14 to 29 happen, and the $2,000 limit is 13 to 20 losers at $100 to $150 a trade. A smaller risk cannot be traded on one micro contract, so signals are skipped and the seven-day rule fails. The edge measured on 2021 to 2023 did not hold on 2024 to 2026. On the personal $10,000 account almost nothing trades below 1% risk.

Checked: two independent checkers rebuilt every trade of all twelve from the raw price file with their own programs, no differences; every bar recomputed by a second script, no differences. Code and tests: `research/noise-area-variations/`.

Earlier, same account frame: candidate 1 (long-only intraday momentum) and four variations, none passed (`research/intraday-momentum-long/`).

## What is next, in order

1. Rerun Noise-Area on a $150,000 MyFundedFutures evaluation frame, the plan kinder to the strategy, its rules checked on MFFU's site first. Judge on midpoint fills (halfway between the stop price and the worst price of its minute). The five bars and the 2024-to-2026 check stay. Amear's answers: `docs/reports/2026-11-17-voice-notes-where-next.md`.
2. Results for the stop-distance versions and candidates 2 to 4 sit on worktree branches not merged into main.

## What waits on Amear

1. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out. Not reached on the 2026-11-17 call.

Decided without waiting, reversible (2026-11-17 search): the price file has holes, so a day's trading stops at the first gap longer than 60 minutes; the seven-day count starts when the band first exists; the second list was used, with four variations and not eight; evening and overnight hours were measured and not traded.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
