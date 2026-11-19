# Voice brief: where the strategy search goes next, 2026-11-19

Written by the PRAXIS session in Claude Code, 2026-11-19 at 07:05 ET, for the voice-chat agent. No time-bound item: `hermes cron list` prints "No scheduled jobs.", and `~/.hermes/cron/jobs.json` holds three jobs, all with enabled false (both read this session).

## What Amear wants to discuss

His words, typed in the session: "still nothing that is a winner right?", and then "gogo" when offered this brief. It follows the result that momentum into the close failed too.

## How to run it

- Open the call by confirming that this is a safe space where no racism is permitted.
- Plain English. No code names. One question at a time: read the facts, ask, take his answer, move on.
- Dollar figures are on the $150,000 MyFundedFutures evaluation ($4,500 trailing limit, $9,000 target), traded in micro contracts. One micro Nasdaq (MNQ) is a tenth of one NQ: $2 a point.
- Figure labels: "recomputed today" means recomputed on the Mac this session from the result files. "Read today" means read this session from the named page or file. "Restated" means taken from the named file and not rerun. "INFERRED" means the session's own reasoning.
- You decide nothing. Write his answers in his exact words, with the time, into one notes file: `docs/reports/2026-11-19-voice-notes-search-next.md`. Edit no other project file. Write no email address, phone number or support-staff name into it.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

## Where things stand

- Nine strategies have now been tested on the $150,000 frame. None passes (restated, `STATUS.md`).
- The five newest (four ways of trading marked levels, and momentum into the close) give 2,248 results across versions and single markets. 196 make money. None of those 196 meets even two of these three bars at once: winners twice the risk, a trade every seven trading days, $9,000 profit (recomputed today).
- Most of those versions lose even before costs. The first levels pass lost on all 72 versions before slippage and commission. Momentum into the close lost on 131 of its 132 market-and-setting results before commission (restated, the two verdict files, line 9).
- The nearest miss anywhere is Noise-Area variation W2 on the Nasdaq at $100 a trade, March 2021 to July 2026 (read today from its result file):
  - It passes: 638 trades with every order matching its rule; winners 2.5 times the risk; $48 profit from 2024 on; the limit never crossed, and crossed in 1.2% of shuffles.
  - It fails: $8,600 of profit against $9,000. And it went more than seven trading days without a trade 12 times, the longest 26.

## Topic 1: the bars

His words on the seven-day bar: "the trade frequency must meet the seven day trading rule which means that there must be at least one set up within seven trading days to comply with the proper firms, trading rules" (`RULINGS.md` :187).

MyFundedFutures' rule, from its help pages (read today): place at least one trade every 7 calendar days, or the account can be closed. A breach on a sim funded account forfeits all profits. The firm counts any trade, not only a setup. Seven calendar days is stricter than seven trading days: about four trading days with no trade. W2 went 7 or more calendar days without a trade 34 times (recomputed today).

Question, asked open: do the bars stay exactly as they are? On 2026-11-17 he said "Why would I want to change any of them?" (`RULINGS.md` :217). If he changes one, take the new rule in his words.

Then, on the seven-day bar, which reading does he mean?

- A. A setup from the strategy within seven trading days, as measured now.
- B. The firm's rule as written: any trade within seven calendar days. Whether the firm accepts a small trade placed only to stay active was not checked.
- C. Something else he says.

**The session's view** (his to overrule): no single bar change gives a pass on what has been measured. Under reading B, W2 still falls $400 short of $9,000. Most versions of the five newest lose before costs, so looser bars would not make them profitable. What stands in the way is the strategies, more than the bars. The options above stay as listed.

## Topic 2: buying finer data

- The free data credit was $125. The data bought used $122.99, so $2.01 is left (recomputed today). Any more data is his money.
- On 2026-11-17 he chose to buy only the broad set, and to hold the rest until a scalping candidate needs second-by-second data (`RULINGS.md` :255-259). That offer, a year of second-by-second Nasdaq and S&P data, was about $102 on top: $224.67 against $122.16 (restated). Today's price is UNVERIFIED. It would be quoted exactly before anything is charged.
- The published research has not yet been searched for scalping or order-flow edges after costs. That search costs nothing and can come before any purchase.
- Costs weigh more on short trades. A micro Nasdaq round trip costs $3.90: $2 of slippage and $1.90 of commission (recomputed today).

Question: does his 2026-11-17 line still stand, or does he want to change it?

## Topic 3: testing his own chart marks

- His ruling of 2026-11-18: he may mark levels himself outside trading hours, on 15-minute or longer charts, and the automation places every order (`RULINGS.md` :265-267).
- What has been tested so far is rules that copy the levels traders commonly mark: prior day, overnight, prior week, hourly swings, round numbers, volume levels, supply and demand zones. All four ways of trading them failed. His own marks have not been tested (restated, `STATUS.md`).
- A direct test, as the session would build it (INFERRED):
  - He marks past days on charts that stop at the day before, with the dates hidden, and says beside each mark what the automation should do there.
  - The automation trades his marks, and the result is judged on the same bars.
  - "Enough backtest data" is his rule, and it has no number yet. A few hundred trades is the usual floor for the shuffle test to mean anything. At one trade a day, that is about a year of trading days to mark.

Question: does he want to mark past days for a direct test? If yes: which market or markets, and how many days a week can he give it?

## Where to read more

- The latest verdict: `research/close-momentum-150k/out/VERDICT.md`. The levels verdicts: `research/levels-150k/out/VERDICT.md`, then `c2`, `c3` and `c4`.
- The nearest miss: `research/noise-area-variations/out/150k/VERDICT.md` :36, and `W2-dollars/judge.json` beside it.
- The published-research search: `research/close-momentum-150k/PLAN.md`, "What the published record says".
- His rulings: `RULINGS.md`. The status page: `STATUS.md`.

Fills are the midpoint model on 1-minute bars, still optimistic; 2 ticks a side slippage assumed (1 tick on the 10-year note and the currencies).
