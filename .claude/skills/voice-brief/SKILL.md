---
name: voice-brief
description: "Write a brief that the voice-chat agent reads to Amear. Use when two or more topics, decisions or open questions are waiting on Amear; when Amear asks for a brief for the voice agent or for voice chat; or when a unit hits something ambiguous or not well defined that only Amear can settle."
---

# Voice brief

**Status: APPROVED by Amear, 2026-11-14** (DECISION_LOG.md 2026-11-14T16:05:30Z, WHO: amear).
The option he chose with it, verbatim ("I" is the master): "On any question that really is yours, I may add one short paragraph labelled as my view. Questions that aren't yours stay out of the brief, and I decide them."

**Authority.** Amear's ruling R9: D-2026-11-14-B, section R9 (HEAD DECISIONS.md :2586; the entry starts at HEAD :2527).
The filer read R9 as two instructions (HEAD DECISIONS.md :2591, the filer's reading, not his words):
R9(a): anything ambiguous or not well defined goes back to him as a voice brief.
R9(b): a skill that writes the brief when several topics or decisions are waiting.
The form to copy is `docs/reports/2026-11-14-voice-brief-pivot.md`, except where this file says otherwise.

## Who uses it

The master. Not the voice-chat agent. A unit that hits an ambiguity reports it
to the master in its report; the master runs this skill.

## Steps

1. **Gather what is waiting.** Read each source below and note what it shows.
   - HANDOFF.md, top card, the line labelled **Questions that are Amear's**,
     and any earlier card it points to.
   - DECISIONS.md, the newest entries at HEAD: any open-question list (Q1, Q2 and so on).
     An entry only in the working tree is labelled "uncommitted".
   - STATUS.md, the first (newest) line labelled **Waiting on Amear**.
   - Time-bound items. Run `hermes cron list` AND read `~/.hermes/cron/jobs.json`.
     Report what each one shows, separately. Do not infer one from the other.
     On 2026-11-14 `hermes cron list` printed "No scheduled jobs." while jobs.json existed.
   - Anything a unit flagged as ambiguous that only Amear can settle (R9(a)).
   - Drop any candidate that a later ruling already settled: check DECISIONS.md
     entries and DECISION_LOG.md "WHO: amear" rows newer than the card that lists it.
     Name the settling line in the DECISION_LOG row for the brief.
   Then run each candidate through the filter in "Which questions go in" below.
   Hand steps waiting on him (things for his hands, not questions) go in one short
   line under "How to run it". They are not questions.
2. **Re-verify every figure and every state before you write it.**
   Re-run the command or recompute the figure in this session where you can.
   A figure you only re-read in a report is labelled "restated from <file> :<line>".
   Anything you did not check this session at all is marked UNVERIFIED in the brief.
3. **Write the brief** at `docs/reports/YYYY-MM-DD-voice-brief-<topic>.md`.
   Use these sections, in this order:
   a. **Title with the date.** Under it, one line of provenance:
      who wrote it, when (date and ET time), and that it is for the voice-chat agent.
   b. **What Amear wants to discuss.** His words verbatim, if he gave any.
      If he gave none, say so in one line.
   c. **How to run it.** Always include all of these:
      - Plain English. Dollar figures, always with the contract size. One MNQ is a tenth of one NQ.
      - Every figure labelled by source: hand run, Mac recomputation, INFERRED,
        reported by the channel, restated from a report, or UNVERIFIED.
      - The voice agent decides nothing. It writes Amear's rulings verbatim, with the time,
        into ONE notes file: `docs/reports/YYYY-MM-DD-voice-notes-<topic>.md`.
        It edits no other repo file.
      - The four things that always wait for his explicit word, in full:
        spending money; switching live trading on, or any order path to a funded account;
        changing circuit-breaker values while real money is at stake;
        installing keys, credentials or agent permissions.
   d. **The topics.** One heading per topic. For each: the facts, then the options as
      neutral choices (A, B, C). Where the source gives no options, list only the readings
      the source names, or ask the question open. Do not invent a menu that frames it.
      On a question that passes "Which questions go in", the master may add ONE short
      paragraph labelled "The master's view". It states the facts it rests on, and the
      options stay listed neutrally beside it. A question that fails the filter stays
      out of the brief and is decided under D1 (D5).
   e. **One thing with a clock on it.** Only when something is time-bound.
      If nothing is, leave the section out and add "No time-bound item." to the provenance line.
   f. **Where to read more.** File paths, with line numbers where they help.
   g. **Last line**, once, standalone:
      `Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.`
4. **Keep it short.** Under about 80 lines. It is read aloud.
5. **Answer nothing.** Rubric S8: "No question that belongs to Amear is answered on his behalf."
   Do not pick an option, a number or a reading for him.
   A view may appear only as "The master's view" on a question that passes the filter (see 3d).
6. **After writing.**
   - Log a DECISION_LOG.md row for the brief.
   - Give Amear the path to the brief.
   - When the notes file comes back, file its rulings as a DECISIONS.md entry,
     "WHO: amear, REPORTED BY the voice-chat agent". Do it through a unit,
     the manager, an auditor and a gated commit, as D-2026-11-14-B was filed.

## Which questions go in

The brief lists ONLY questions that are Amear's. They are:
- D2 items (D-2026-11-08-D D2, the four always-wait items above);
- rubric waivers;
- strategy and account choices he has reserved for himself;
- things his own rulings explicitly left open for him (for example Q1-Q6 of D-2026-11-14-B).

**Filter test.** For each candidate, ask in order. Stop at the first yes.
1. Is it one of the four D2 items? Yes: it goes in.
2. Does it ask him to waive a rubric line? Yes: it goes in.
3. Did he reserve it, or did a ruling of his leave it open for him? Name the file and line.
   Yes, with a citation: it goes in.
4. Did a unit flag it as ambiguous (R9(a))? It goes in only if its answer would set
   one of the things in 1-3 (a D2 item, a rubric waiver, or a choice he reserved),
   with that file and line named. A flag alone admits nothing.
If every answer is no, it fails. Do not put it in the brief.
Decide it under D1, take the recommended option, and log it in DECISION_LOG.md as
"decided by master under D-2026-11-08-D D1". Amear can reverse it later.
Putting a question that fails this filter to him, with or without a recommendation, is a defect (D5).

**The wider list.** Amear approved this filter list with the skill (DECISION_LOG.md 2026-11-14T16:05:30Z).
Rubric :470 is not edited. D1 still holds: work does not wait on a briefed question
unless a ruling of his says it waits (cite it).

## What this skill does not do

- It does not commit. Filing goes through a unit, a manager, an auditor and a gated commit.
- It does not decide. Not for Amear, and not for the voice-chat agent.
- It does not replace D1. Questions that are not Amear's are default-decided, not briefed (D5).
- It does not answer Q1-Q6 of D-2026-11-14-B or any other question of his.
- It does not install, enable or register anything, and it changes no settings.
