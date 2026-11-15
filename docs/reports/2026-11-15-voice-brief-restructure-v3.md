# Voice brief, version 3: does the project need a restructuring intervention, 2026-11-15

Written by the PRAXIS master (Claude Code), 2026-11-15 at 13:16 ET, for the voice-chat agent. It replaces version 2 (13:08 ET), after Amear's typed rulings of 13:15 ET. No time-bound item.

## What Amear wants to discuss

His words, typed in the master session today: "now do we need to discuss an intevention in restucturing this project?" Then: "ok put together the handoff to have trhis discussion with the voice agent."

## How to run it

- Open the call by confirming that this is a safe space where no racism is permitted. This is Amear's standing rule for every voice call on this project, approved by him today.
- Plain English. Say the plain names used below. Do not read out code names, branch names or line numbers; they appear only in the last section, which is for looking things up.
- This brief contains no profit or loss figure.
- "Checked today" means the master ran the check in this session. "Restated" means read from a project file.
- You decide nothing. Write Amear's rulings in his exact words, with the time, into ONE notes file: `docs/reports/2026-11-15-voice-notes-restructure.md`. Edit no other project file.
- Do not write any email address, phone number or support-staff name into the notes file.
- Four things always wait for his explicit word: spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.

## The facts behind the question

- Nothing has reached the main branch today. It is where it was yesterday evening. Three working sessions ran today. (Checked today.)
- Four pieces of work were set aside in two days: the gap-fade test, the voice-brief skill, the filing of his Nov 15 rulings, and the Noise-Area paper read. In each case the independent checker passed the work itself and failed the written reports on form, for example missing pasted output, or a support rep's first name inside a pasted file path. (Restated from the handoff cards.)
- The strategy search and the build schedule are both paused. (Checked today.)
- Since his Nov 15 ruling, strategies are tested one at a time, not in bulk, and Noise-Area is retested first, with a real stop. (His ruling, restated from this morning's call notes and confirmed by him in writing today.)

## Topic 1. The rule that sets work aside after two failed checks

Fact: the rule is absolute. Two failed checks set a piece of work aside, whatever the failure was. Work that is set aside waits for a person to pick it up. All four recent cases failed on how the report was written, not on the result.
Options: A. Keep the rule as it is. B. Keep it for failures of substance, and allow one more fix-and-recheck when only the report's form failed. C. Shorten what a report must contain, so there is less form to fail. D. Something else.
The master's view: the rule is doing what it was written to do, and the cost is that correct work is not reaching the main branch. That rests on the four cases above. Which trade he wants is his.

## Topic 2. The work that is set aside

Fact: earlier today he said "not now" to three of the four: the gap-fade test, the voice-brief skill, and the filing of his Nov 15 rulings. That stands and is not asked again. One consequence to know: his Nov 15 rulings are therefore not yet on the main branch.
The one fresh question is the Noise-Area paper read. It needs a name masked in five places, one check, and a commit. What it found, in the paper's own words: no hard stop.
Options for the paper read: A. Pick it up now. B. Leave it. C. Wait for his answer on topic 1, since a change to that rule may settle it.

## Topic 3. What the system works on first

Fact: strategies are tested one at a time, and Noise-Area is retested first, with a real stop (his Nov 15 ruling). The strategy search is paused, and it does not yet apply his cost-of-the-trade rule. His six questions from Nov 14 are unanswered.
Options, proposed in the review he pasted: A. Unpause the strategy search with his cost-of-the-trade rule built in. B. Answer his six questions from Nov 14 first. C. Fix the rule in topic 1 first and let the set-aside work land. D. Something else.

## Topic 4. The MFFU permission rule

The project's rule reads: "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." An independent checker graded it today against the email thread he pasted: not met.
- The only MFFU reply that names his exact setup came from their AI agent, and it says: "I cannot issue written approval for your specific configuration."
- Two replies from people followed. Nov 12: "As long as it adheres to response 1 then it's fine." Nov 13: "Yes." to his question about running unattended on Evaluation and Sim Funded accounts. Neither names the workflow tool, the file drop or the second strategy.
- Live accounts are addressed only by the AI agent.
- The recorded design still ends at a broker connection MFFU has written that they do not offer.
- On Nov 14 he set prop firms aside "for now". On Nov 15 he ruled that testing assumes a personal $10,000 account while prop firms stay out. (Restated.)
A knock-on effect: the walk-forward drawdown gate is still set from MFFU's limits. His ruling reads: "backtest max drawdown must stay below 80% of the ruled limit, i.e. below the lower of 3.2% of the MFFU account size and 80% of MFFU's trailing drawdown limit."
Options: A. Keep the rule as written and send MFFU one more question that names the setup. B. Reword the rule to what MFFU will put in writing, and say what that is. C. Set it aside while prop firms are set aside. Testing already assumes the personal $10,000 account. The one question under this option: should the drawdown gate be re-set against that account? D. Something else.

## Topic 5. Anything else he wants changed

Asked open: the roles, the amount of logging, how often he is asked things, or anything not listed here.

## For looking things up. Do not read this section aloud.

- Plain names to code names: gap-fade test = `Praxis_build-vn4`; voice-brief skill = `Praxis_build-61o`; Nov 15 rulings filing = `Praxis_build-205` (entry D-2026-11-15-A); paper read = `Praxis_build-2l3`; MFFU permission rule = rubric F4; set-aside rule = the park rule; his six questions = Q1 to Q6 of D-2026-11-14-B; safe-space rule = D-2026-11-15-B.
- His Nov 15 rulings used above: `docs/reports/2026-11-15-voice-notes-open-questions.md` :16 (one at a time), :63 ($10,000 personal account), :93 (hard stop at entry); typed rulings, DECISION_LOG 2026-11-15T14:37:18Z and 18:15:44Z.
- `HANDOFF.md`, top two cards. `specs/SPEC_RUBRIC.md` :33-:42 and :264-:278.
- `docs/reports/evidence/2026-11-15-mffu-thread-pasted-by-amear.md`, the full MFFU thread, names withheld; the Nov 12 reply from a person is at :362-:372.
- `docs/specs/2026-11-06-walk-forward-values.md` :135, the drawdown gate.
- The line below is the project's standing line for every report. It does not apply to this brief's content.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
