# Voice brief: does the project need a restructuring intervention, 2026-11-15

Written by the PRAXIS master (Claude Code), 2026-11-15 at 13:02 ET, for the voice-chat agent. No time-bound item.
Format follows the voice-brief skill Amear approved on 2026-11-14. That skill is parked on branch `parked/Praxis_build-61o` and is not on main.

## What Amear wants to discuss

His words, typed in the master session today: "now do we need to discuss an intevention in restucturing this project?" Then: "ok put together the handoff to have trhis discussion with the voice agent."

## How to run it

- Plain English. Dollar figures at the contract size. One MNQ is a tenth of one NQ. This brief contains no profit or loss figure.
- Every fact below is labelled: "checked today" means the master ran the check in this session; "restated" means read from a file.
- You decide nothing. Write Amear's rulings verbatim, with the time, into ONE notes file: `docs/reports/2026-11-15-voice-notes-restructure.md`. Edit no other repo file.
- Do not write any email address, phone number or MFFU staff name into the notes file.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
- Hand step for Amear, not a question: the voice agent was closed today at his choice; he restarts it for this call.

## The facts behind the question (all checked today unless labelled)

- Nothing landed on main today. Main is at `d9fc5f0`, the same as yesterday evening. Three interactive sessions ran today.
- Four pieces of work were parked in two days: the gap-fade test (`vn4`), the voice-brief skill (`61o`), his Nov 15 rulings filing (`205`), and the Noise-Area paper read (`2l3`). Restated from the handoff cards: in each case the auditor passed the substance and failed the reports on form, for example missing pasted output, or a support rep's first name inside a pasted file path.
- There are 9 parked branches on the remote in total.
- Both loops are paused. The Hermes job file shows the search loop and the build loop disabled and paused; `hermes cron list` prints "No scheduled jobs."
- Strategy contenders recorded: 0 of 3 (restated from STATUS).
- The MFFU permission criterion, called F4, was graded today by an independent auditor: NOT MET. Detail in topic 1.
- The paper read found, in the paper's words, no hard stop for Noise-Area (restated from the handoff card; that work is parked, not landed).

## Topic 1. The MFFU permission rule (F4)

F4 reads: "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." It has been open since August (restated from the rubric and the August evidence report).
What the auditor found in the Nov 11 to 13 email thread, which Amear pasted today:
- The only MFFU reply that names his exact setup came from their AI agent, and it says: "I cannot issue written approval for your specific configuration."
- Two human replies followed. Nov 12: "As long as it adheres to response 1 then it's fine." Nov 13: "Yes." to his question about running unattended on Evaluation and Sim Funded accounts. Neither names n8n, the file drop or the second strategy.
- Live accounts are addressed only by the AI agent.
- The recorded design still ends at Rithmic. MFFU has written that they do not offer Rithmic.
- Yesterday he set prop firms aside "for now" (ruling R2, restated).
Options: A. Keep F4 as written and send MFFU one more question that names the setup. B. Reword F4 to what MFFU will put in writing, and say what that is. C. Set F4 aside while prop firms are set aside, and name the account that testing assumes instead. D. Something else.

## Topic 2. The two-failure park rule

Fact: the rule is absolute. Two audit failures park a unit, whatever failed. All four recent parks came from report form, not from the result (restated, as above). A parked unit waits for a human to resume it.
Options: A. Keep the rule as it is. B. Keep it for substance, and let a form-only failure be cured and re-audited once more. C. Shorten what a report must contain, so there is less form to fail. D. Something else.
The master's view: the rule is doing what it was written to do, and the cost is that correct work is not reaching main. It rests on the four parks above. Which trade he wants is his.

## Topic 3. The order of work

Fact: builds are paused until three contenders exist; the search loop that finds contenders is paused; the loop does not yet apply his cost-of-the-trade rule; his six questions from Nov 14 (Q1 to Q6) and the 16 open items of the parked Nov 15 rulings are unanswered or unfiled.
Asked open, because the sources name no options: what should the system work on first, and what should stop?

## Topic 4. The four parked items

Fact: he said "not now" today for `205`, `61o` and `vn4`. `2l3` needs five lines masked, one audit and a commit. `205` holds his own Nov 15 rulings, which are therefore not on main.
Options for each: A. Resume. B. Leave parked. C. Close and drop.

## Topic 5. Anything else he wants changed

Asked open: the roles (master, manager, worker, auditor), the amount of logging, how often he is asked things, or anything not listed here.

## Where to read more

- `HANDOFF.md`, the top two cards.
- `docs/reports/evidence/2026-11-15-mffu-thread-pasted-by-amear.md`: the full MFFU thread, names withheld, audited today, not yet committed. The Nov 12 human reply is at :362-:372.
- `specs/SPEC_RUBRIC.md` :33-:42 (F4) and :264-:278 (the park rule).
- `docs/reports/2026-11-15-voice-notes-open-questions.md`: this morning's call notes.

## Superseded, 2026-11-15 13:08 ET

Replaced by `docs/reports/2026-11-15-voice-brief-restructure-v2.md` after a seven-point review Amear pasted into the master session (DECISION_LOG 2026-11-15T18:08:34Z). Use version 2 for the call. This version is kept, unedited above this note, as the record.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
