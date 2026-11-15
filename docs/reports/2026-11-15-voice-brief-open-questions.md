# Voice brief: the open questions from the restructure, 2026-11-15

Written by the PRAXIS master (Claude Code), 2026-11-15 about 08:30 ET, for the voice-chat agent. No time-bound item.
Format follows the voice-brief skill Amear approved on 2026-11-14. That skill file is parked on branch `parked/Praxis_build-61o` and is not on main yet.

## What Amear wants to discuss

His words: "check the inbox then give me handoff for voice man". He named no topic, so this brief covers everything that is waiting on him.

## How to run it

- Plain English. Dollar figures at the contract size. One MNQ is a tenth of one NQ.
- Every figure is labelled by its source.
- You decide nothing. Write Amear's rulings verbatim, with the time, into ONE notes file: `docs/reports/2026-11-15-voice-notes-open-questions.md`. Edit no other repo file.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
- Inbox result, checked this morning: nothing new. No Telegram message since Nov 13 at 8:21 PM ("Halt all runs until further notice"). No new VM reply since Nov 11. No new commits since yesterday's park. His email was not checked, because the Gmail connector failed to connect.

## Topic 1. Resume the search loop, or keep it paused?

Facts (checked this morning): the Hermes job file shows the search loop and the build loop both paused. `hermes cron list` prints "No scheduled jobs." He paused the loop yesterday "until I decide".
Options: A. Keep it paused. B. Resume it now. C. Resume it once the cost-of-the-trade filter (R3) is written into it.
The master's view: the loop does not yet reject a candidate that has no predefined maximum loss per trade. That change still needs a decisions entry, then a build. Restarting it before then would test ideas under the old rules.

## Topic 2. His six open questions from yesterday (Q1-Q6)

Quoted from the committed rulings, DECISIONS.md :2595-:2600 at HEAD.
- **Q1, the daily-loss cap wording.** His "Yeah" could mean "wait for data", or agreement to "a multiple of the cost of a trade". It is recorded as wait-for-data. Confirm.
- **Q2, the exception to the cost-of-the-trade rule.** If a news gap or slippage fills a stop past its level, is that still "the cost of the trade", or a breach like a server crash? The answer decides how stops are sized and tested.
  Fact for Q2, restated from `docs/reports/2026-11-14-r3-recheck-manager.md` :115: in the gap-fade test, price traded past the stop on 273 of 286 stop exits, by up to 45.5 points.
- **Q3, which balance the percentage uses.** Starting balance, current balance, or high-water mark?
- **Q4, the target account.** With prop firms out "for now", what account does testing assume? A personal cash account, and at what size? Is the MFFU written-confirmation follow-up still worth chasing?
- **Q5, the rest of the Floor Rule.** Hard stop time, the account drawdown kill switch, and the after-a-win protocol.
- **Q6, the five rechecked strategies.** Rerun any of them with a hard stop, or drop them?
  Facts for Q6, at 1 MNQ, restated from the same report, :9-:13 and :17-:21:
  - Noise-Area baseline: no predefined stop. Largest single loss $542.40, worst day $705.10, up to 5 trades a session.
  - Noise-Area OppBand: no predefined stop. Largest loss $1,960.90, worst day $1,894.80.
  - Noise-Area Flat1559: no predefined stop. Largest loss $542.40, worst day $683.70.
  - Last-Half-Hour Momentum (already retired): no stop, time exit only. Largest loss $555.40.
  - Gap fade V2: a gap-sized stop, but only in a Python test rule. Largest loss $472.90.
  - Net profit, UNVERIFIED: baseline about $17,824, OppBand about $19,719, Momentum minus $9,692.60. These are the master's figures from yesterday's session, and no filed report contains them. Treat them as rough until they are re-run.

The master offers no view on Q1-Q6. They set his own risk rules.

## Topic 3. Two parked items: pick them up, or leave them?

- **Voice-brief skill** (`Praxis_build-61o`). He approved it. Both audits passed the skill file itself. Both failed on the job report: one command was shortened and one pasted output was trimmed. The park rule says a person resumes it.
- **Opening gap fade** (`Praxis_build-vn4`). It failed its pre-screen on Nov 14. Q6 may settle it.
Options: A. Resume both. B. Resume the skill only. C. Leave both parked.
The master's view: the skill fix is paperwork only. Re-running two commands and pasting their full output would clear it.

## Where to read more

- Rulings and Q1-Q6: `DECISIONS.md`, entry D-2026-11-14-B, HEAD :2527-:2615
- Recheck: `docs/reports/2026-11-14-r3-recheck-manager.md`
- Yesterday's pivot brief: `docs/reports/2026-11-14-voice-brief-pivot.md`
- Skill park: `bd show Praxis_build-61o`

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
