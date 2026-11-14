# Voice brief: PRAXIS updates, Fri 2026-11-13 7:30 PM ET to Sat 2026-11-14 9:30 AM ET

Written by praxis-master on 2026-11-14 at 9:40 AM ET, for Amear to go over with the voice agent. All times are Eastern. Sources: `git log`, DECISION_LOG.md rows 2026-11-14T01:23:10Z to 13:38:00Z, the top HANDOFF.md and STATUS.md cards, and `~/.hermes/cron/jobs.json`. All of these were read in this session.

## The short version

This was filing work plus one strategy test. Four commits landed on main, and all four are paperwork: your rulings, evidence files and ledgers. One strategy was tested and it failed. No trading code changed, no builds ran, and the contender count is still 0 of 3.

## What happened, in order

1. **8:16 PM: your rulings, given in the Claude.ai channel.** You removed the peer-review requirement, because five-year in-house backtests are the filter now. You paused builds until there are three strategy contenders, and you said the search loop runs in Claude Code. At 8:21 PM you told Hermes to halt all runs. At 8:25 PM you told the master session to go ahead and to write a 4 AM handoff for Hermes.
2. **8:58 PM, commit `b1815d2`:** the strategy-review evidence and the handoffs were filed.
3. **9:08 PM, commit `9a18fde`:** your rulings went into DECISIONS.md as D-2026-11-13-D. The contender bar and the overfitting guard went in as D-2026-11-13-E. The Claude.ai channel proposed D-2026-11-13-E and the master adopted it, so you can change it.
4. **About 9:23 PM:** the end-of-night ledger flush did not land, because its auditor stopped without giving a verdict. The 4 AM run carried that flush instead.
5. **4:00 AM: Hermes started a fresh session as planned.**
   - 4:48 AM, commit `bdb63b7`: 29 older evidence files from the messy working tree were filed. 7 were held back for content reasons; one carries email addresses, for example.
   - 5:09 AM, commit `244cfc3`: the ledger and handoff flush. This is still the latest commit on main.
6. **8:00 to 8:38 AM: the first search-loop run, on candidate 1, the opening gap fade.** The strategy fades the 9:30 gap back toward the prior 4:00 PM close.
   - The candidate could not be run in NinjaTrader from the Mac. Instead the master tested it with a quick Python pre-screen on the 1-minute data.
   - **The result is a fail.** The best version had a profit factor of about 1.01, and the bar is 1.10. At 1 MNQ it lost $254 over the full period, and its worst drawdown was $4,612. That is above the drawdown limit of every MFFU account; the 50K limit is $1,600.
   - Both auditors re-ran the numbers and got the same results. Both audits still failed, but only on paperwork: the reports made claims without pasting the output that proves them. Two failed audits trigger the park rule. The work sits on the branch `parked/Praxis_build-vn4` (`afa53c6`), and nothing from this run went to main.

## Points to go over with the voice agent

1. **Candidate 1 (bead `vn4`): resume it or leave it parked.** The strategy result is not in question. Resuming only fixes the evidence in the reports, and the strategy failed either way. Leaving it parked costs little.
2. **Should a Python pre-screen on the Mac be the loop's first filter?** The master decided this alone, and the rule that allows it (D-2026-11-14-A) exists only on the parked branch. Until you rule on it, the loop has no approved way to score a candidate from the Mac.
3. **The next loop run is at 12:00 PM today.** Hermes `praxis-search-loop` is enabled and scheduled. The handoff tells that run to write candidate 2's rules and then stop, because the pre-screen is not approved on main. If you want the loop to do more, or to stop, decide before noon.
4. **One step for you:** set the NinjaTrader commission to $4.68 round trip ($2.34 per side on each PRAXIS row).
5. **Still parked from before, and still waiting on you:** `ckh`, `diq`, `gfx` and `c2w`.
6. **Unchanged:** F3 and F4 are still frozen, and F4 still needs the written confirmation from MFFU. Live trading stays off.

## State of the working tree

The cards and ledger rows from this morning's 8 AM run exist in the working tree only. The next ledger flush puts them on main. This brief has not been committed either.
Filer's note (2026-11-14, unit 2026-11-14-pivot-rulings-filing, praxis-worker for praxis-manager under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
