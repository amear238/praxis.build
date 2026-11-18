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

Nothing. The $150,000 rerun finished on 2026-11-17: **none of the 36 runs passes.** Full verdict in plain English: `research/noise-area-variations/out/150k/VERDICT.md`.

The account, from MyFundedFutures' site: every $150,000 plan has a **$4,500** end-of-day trailing limit and a **$9,000** target (the $6,000 from the call is not there). Builder was used as the kinder plan. The same twelve variations, each at three risk sizes, list locked before the run, judged on midpoint fills.

| Bar | Result across the 36 |
|---|---|
| Every order matches its rule | 36 pass |
| Average winner at least twice the risk, with a profit on 2024 to 2026 | 6 pass; the other 30 lost money from 2024 on |
| Never more than seven trading days without a trade | 5 pass (the any-minute version, and the narrower band at the two larger sizes); the rest run 8 to 29 days |
| Profit at least $9,000 | 27 pass |
| $4,500 limit crossed in at most 5% of shuffles | 1 passes |

Nearest miss: one trade a day with a trailing stop at $100 a trade. It survives (limit never crossed; 1.2% of shuffles) and keeps 2-to-1, and fails on profit ($8,600 against $9,000) and on 26 trading days without a trade.

Why: the half-hour versions went 8 trading days without a breakout in late 2025 with nothing skipped, so the seven-day rule fails whatever the account. Small risk survives and earns too little; larger risk earns enough and crosses the limit in every shuffle. 2026 lost money in every run.

For information, not a bar: started on a random day, the middle sizes reached +$9,000 before the limit in a fifth to nearly half of cases, after about half a year.

Earlier, on the $50,000 stand-in with harsh fills: none of the twelve passed (`research/noise-area-variations/out/VERDICT.md`); candidate 1 and four variations, none passed (`research/intraday-momentum-long/`).

Also checked 2026-11-17, on Amear's question about the session-sweep idea he pasted (overnight high or low taken out in the New York morning, then faded, stop past the spike, 2-to-1 target, 2021 to 2026): it loses, about $0.16 per $1 risked after costs over 1,011 trades, and the 4-hour trend filter does not rescue it. The 1.68 profit factor quoted from a vendor blog was on currencies and gold, with no costs. Measurement: `research/session-sweep/`.

Opening range breakout on the same $150,000 frame, 2026-11-17: **none of 108 versions is good enough to send to the final run.** The versions with winners at least twice the risk have losing runs of 14 to 19, so the limit only allows about $61 a trade, which projects to about $9,700 over five and a half years with a shrinking edge. Verdict: `research/orb-150k/out/VERDICT.md`.

## What is next, in order

1. Trend-following, two versions side by side on the $150,000 frame: same-day (flat by 3:55 PM) and multi-week. Plan, bars locked before any result: `research/trend-150k/PLAN.md`.
   - Data bought and checked (2026-11-17): Databento, eleven markets, 1-minute bars 2018 on and daily bars 2010 on, worst-case $124.64 of the $125 free credit, none of Amear's money. Saved, not committed, in `market-data/databento`. NQ matches the NinjaTrader file (97% of 1.86M minutes within two ticks); all 729 rolls joined.
   - Built, test first: data reader (11 tests), multi-week engine (14), same-day engine (9). No backtest run yet.
   - Next: the independent rule check, then the measuring pass on 2018 to 2023, then the locked list.
   - Before any result: note in the plan that risk is a set % of the realised balance per trade, not split across markets (the engines already do this). Still to build: the runner and judge (reuse the survival code in `research/intraday-momentum-long/run.py`), the specs for the 11 micros. Confirm MFFU lists every micro before the final run.
2. Earlier: Amear's word on where the search goes now that Noise-Area and the opening range breakout have both failed on the $150,000 frame. Until then: a fresh research pass for the next candidate (task `Praxis_build-8h5`).
3. Results for the stop-distance versions and candidates 2 to 4 sit on worktree branches not merged into main.

## What waits on Amear

1. **Files held back from the repo for personal data:** one screenshot of a support reply that shows a third party's name and address, and 7 older reports. Commit, mask, or leave out. Not reached on the 2026-11-17 call.

Decided without waiting, reversible (2026-11-17, the $150,000 rerun): Builder as the kinder plan; each variation run at three risk sizes; the limit judged with no stopping point, as the bar was set, with MyFundedFutures' stopping point reported beside it; when a minute opens past the stop, the midpoint is taken from that open.

Decided without waiting, reversible (2026-11-17 search): the price file has holes, so a day's trading stops at the first gap longer than 60 minutes; the seven-day count starts when the band first exists; the second list was used, with four variations and not eight; evening and overnight hours were measured and not traded.

## Where things are

- Amear's rulings, in his words: `RULINGS.md`.
- Everything older: `archive/2026-11-15/` and git history.
- Open task list: `bd ready`.
- Uncommitted on this machine, left as they are: two Oct 28 reports and two walk-forward spec files with edits, older reports, `research/`, and the voice-brief skill.
