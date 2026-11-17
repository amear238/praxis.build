# Voice brief: where the strategy search goes next, 2026-11-17

Written by the PRAXIS session in Claude Code, 2026-11-17 at 10:14 ET, for the voice-chat agent. No time-bound item: `hermes cron list` prints "No scheduled jobs.", and `~/.hermes/cron/jobs.json` holds three jobs, all with enabled false (both read this session).

## What Amear wants to discuss

His words, typed today: "write a voice brief on where to go next". It follows the result he was given this morning: no variation of the Noise-Area breakout passes his five bars.

## How to run it

- Open the call by confirming that this is a safe space where no racism is permitted.
- Plain English. No code names. One question at a time: read the facts, ask, give the options, take his answer, move on.
- Dollar figures are for micro contracts (MNQ, $2 a point; one MNQ is a tenth of one NQ) on the $50,000 stand-in account with a $2,000 trailing limit, unless a line says otherwise.
- Figure labels: "recomputed today" means recomputed on the Mac this session from the result files. "Restated" means read from the named commit or file and not rerun. Unless a line says "kind fills", a Noise-Area figure uses harsh fills: a stop fills at the worst price of its minute.
- You decide nothing. Write his answers in his exact words, with the time, into one notes file: `docs/reports/2026-11-17-voice-notes-where-next.md`. Edit no other project file. Write no email address, phone number or support-staff name into it.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

## Where things stand

- Noise-Area: twelve variations tried in two locked lists. None passes. All twelve cross the $2,000 limit in the real order of days, and in 99.8% to 100% of 10,000 shuffled orders; the bar is 5% (recomputed today).
- All twelve have an average winner of 2.0 to 5.9 times the risk. All twelve lost money on 2024 to 2026, between $557 and $19,071 (recomputed today).
- One of the twelve keeps the seven-trading-day rule, and it loses $17,852. The others go 8 to 30 trading days without a trade (recomputed today).
- They win 2 to 3.5 trades in 10. Losing runs of 14 to 29 in a row happened in every one. At $100 to $150 a trade, $2,000 is 13 to 20 losers (recomputed today).
- With kind fills (a stop fills at its price plus 2 ticks) all twelve make more than $4,000, from $6,684 to $146,466. Survival still fails in all twelve; the best crosses the limit in 88% of shuffles (recomputed today).
- Every other strategy tested on this account frame also failed survival. Closest: the long-only intraday momentum candidate, $5,317 profit, limit crossed in 24.5% of shuffles (restated, `STATUS.md` before today, commit 05d3756); and one of its stop-distance versions, $13,025, 26.6% (restated, commit e98c170). The opening-range breakout made $8,055 and crossed the limit in the first week (restated, commit 18b6055). Two more lost money (restated, commits 1e2e3ef and 5851707).
- On the personal $10,000 account, Noise-Area below 1% risk barely trades: 0.25% is $25, and one micro contract with a stop 10 points away already risks about $23 (recomputed today).

## Topic 1: which account is the target

His rulings point two ways. On 2026-11-14 and 2026-11-15: prop firms set aside, test against a personal $10,000 account (`RULINGS.md`, "The account"). Later on 2026-11-15 he set the pass bars against a $50,000 prop stand-in with a $2,000 limit (`RULINGS.md`, "First candidate and how it is judged"). On 2026-11-17 he tied the seven-day rule to prop firm trading rules. The drawdown figure for the personal account was never set; his 5% was, in his words, "a fucking guess".

Question: which account should the search be judged against from here?

- A. The $50,000 stand-in with the $2,000 trailing limit, as now.
- B. The personal $10,000 account, with a drawdown figure he sets.
- C. A different account size or limit that he names.

## Topic 2: the bars

The five bars are his: every order matches its rule; average winner at least twice the risk; a trade at least every seven trading days; profit at least double the drawdown limit; the limit crossed in at most 5% of shuffles. On this account they pull against each other. The versions tested win 2 to 3.5 trades in 10 and had losing runs of 14 to 29, so they need room for more losers than $2,000 gives at $100 to $150 a trade. Smaller risk gives that room, but one micro contract cannot be made smaller, so signals are skipped and the seven-day rule fails.

Question, asked open: do the bars stay exactly as they are, or does he want to change one? If he changes one, take the new rule in his words.

Two things inside the bars were calls made by Claude, which he can correct (design, "Calls made by Claude"): results are judged on harsh fills, and the 2-to-1 bar also needs a profit on 2024 to 2026 alone.

## Topic 3: which strategy

Question: what does the search test next?

- A. A different strategy family, chosen by a new research pass.
- B. One of the earlier candidates that came closest on survival (24.5% and 26.6% against a bar of 5%), with variations.
- C. Noise-Area again, only if Topic 1 or Topic 2 changed something.
- D. Something he names.

His standing rule: one strategy at a time (`RULINGS.md`, 2026-11-15).

**The session's view** (his to overrule): every strategy tested so far failed at the same place, the $2,000 limit, including the ones that made money. So Topic 1 and Topic 2 decide more than Topic 3 does. It rests on the figures under "Where things stand". The options above stay as listed.

## Topic 4: files held back for personal data

Still waiting from before: one screenshot of a support reply that shows a third party's name and address, and 7 older reports, are held out of the repository. The repository is public. Commit them, mask them, or leave them out? (`STATUS.md`, "What waits on Amear".)

## Where to read more

- The verdict, in plain English: `research/noise-area-variations/out/VERDICT.md`
- What the measuring pass found: `research/noise-area-variations/out/measure/READING.md`
- The two lists: `research/noise-area-variations/variations/LIST.md` and `LIST2.md`
- The design and its bars: `docs/superpowers/specs/2026-11-17-noise-area-variations-design.md`
- His rulings: `RULINGS.md`. The status page: `STATUS.md`.

Fills are harsh unless a line says kind; 1-minute bars; 2 ticks a side slippage assumed.
