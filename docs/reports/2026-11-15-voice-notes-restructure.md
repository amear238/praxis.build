# Voice notes: restructuring intervention, 2026-11-15

Voice-chat agent (Claude.ai, Praxis project) notes for the call run from `docs/reports/2026-11-15-voice-brief-restructure-v3.md`. Call opened 13:18 ET. Amear's rulings are recorded in his exact words, with the time. The agent decides nothing. No email address, phone number or support-staff name is written here.

## Opening

- 13:18 ET: Safe-space confirmation given at the open (standing rule, decisions entry D-2026-11-15-B).

## Rulings

Times between 13:18 and 14:03 ET are approximate; the rulings were spoken and are copied from the call transcript.

- Topic 1, set-aside rule (about 13:25 ET). His words: "Add it to the fucking ruling to whatever it is that's that's that's that's failing these ruling uh, these things because stupid format issues. Um, to either get fixed or to fucking stop that bullshit. Okay, if there's an extra layer of agent that needs to be added for what a failure should actually be considered, uh, then that needs to be addressed."
- Topic 2, Noise-Area paper read (about 13:35 ET). Asked whether to pick it up: "Yeah". Asked whether the name is masked first or committed as is: "I don't care. To be honest, I don't. I don't actually care." Agent's reading, not his words: mask the name and commit, no extra check.
- Side question (13:56 ET): asked whether a more discretionary but automated approach had been looked into. Told yes, and that the research kept AI out of trade decisions. Asked whether to save the morning "sit out today" AI filter as a parked idea: "No."
- Topic 3, what runs first (about 13:59 ET). The brief's "six questions unanswered" line was out of date; he answered them on this morning's call. Asked whether to restart the strategy search with the cost-of-the-trade rule built in, alongside the Noise-Area retest: "Yeah."
- Topic 4, MFFU permission rule (about 14:00 ET). Asked whether to park the rule while prop firms are set aside and re-set the drawdown gate against the personal $10,000 account: "Yeah."
- Topic 5, restructure (14:03 ET, typed). His words: "I want to go through a restructuring on how the Praxis master is doing the workflows. This is what caused hiccups months ago that stalled out this project. [...] So the project being about audits, doing audits and all that bullshit, I am ready to let go of that or to do some sort of intervention. Do consider that your ability now is significantly better than it was when that directory was put together. So I think I'm ready to start simplifying things".
- Restructure proposal (14:03 to 14:05 ET). The voice agent proposed the restructure set out below and asked whether to write it up as the instruction for the master. His answer, typed at 14:05 ET: "Yeah."

## Instruction for the PRAXIS master: restructure

PROPOSED BY: the voice-chat agent, on this call. APPROVED BY: Amear, 14:05 ET, "Yeah." (above). His reasons, in his words, are in the topic 5 line above.

Repo facts behind it, checked by the voice agent at 14:03 ET: on main since 2026-08-01, 610 changes to .md files against 24 .py and 5 .cs; 533 files in docs/reports; HANDOFF.md 2,359 lines, DECISIONS.md 2,918, STATUS.md 751.

### The one goal

One strategy that passes backtesting on the personal $10,000 account under his trading rules, then the full pipeline running on a sim account in live markets. Work that does not move toward that is frozen: MFFU follow-up, Hermes, the project kit, VM extras.

### What stops

1. The manager, worker and auditor chain. One builder session does the work. Retire or archive the agent files that are no longer used.
2. Per-unit written reports, and every rubric rule about how a report must look.
3. The rule that sets work aside after two failed checks. A failed check now means a failed test, and the builder fixes it and reruns.
4. The multiple tracking files as living documents: HANDOFF, DECISIONS, DECISION_LOG, DISPATCH_LOG, AUDIT_LOG, RUN_DECISIONS, ISSUE_REGISTER, PATCH_NOTES, MANIFEST. Move them to an archive folder, byte-unchanged. Delete nothing.

### What replaces it

1. Tests are the check. A result counts when the code runs, the numbers reproduce on a second run, and every simulated order matches the strategy's rule. Keep these strict.
2. One independent check, by an agent that did not write the code, only for anything that can place an order.
3. One status page, STATUS.md, rewritten to a single page: the goal, what is done, what is running, what is next, and what waits on Amear. Git history is the record of everything else.
4. One short decisions list for Amear's own rulings only, in his words with the date. Carry forward his standing rulings from the old files in plain English.
5. Rewrite CLAUDE.md and the build skill to match the above.

### What does not change

1. Four things wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; breaker values while real money is at stake; keys, credentials and agent permissions.
2. His trading rules: the cost of the trade as a set percentage of the account; a stop-market order on every trade at entry; one strategy at a time; Noise-Area retested first with a real stop; nothing goes to execution without enough backtest data; fully rule-based and automated, no AI in trade decisions.
3. One session per working tree.
4. The safe-space rule for voice calls.
5. Plain English to Amear, no code names, and one step at a time.

### Order of work

1. Commit today's uncommitted files first, as they are, so nothing is lost.
2. Land the Noise-Area paper read: mask the name, commit, no extra check.
3. Do the restructure above in one commit or a few, and push. Tell Amear in one short message when it is done.
4. Start the Noise-Area retest with a real stop, by fast Python on the Mac, with NinjaTrader confirming only a finalist.
5. Restart the strategy search with the cost-of-the-trade rule built in.
6. Park the MFFU permission rule and re-set the drawdown gate against the personal $10,000 account. The gate's new figure is a breaker value in testing only; propose it and carry on.

### Left as it was

His "not now" on the gap-fade test, the voice-brief skill and the separate filing of his Nov 15 rulings stands. Those rulings are carried into the new decisions list under item 4 above, so they are not lost.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
