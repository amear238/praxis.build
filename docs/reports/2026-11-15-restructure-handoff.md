# Handoff: the PRAXIS restructure, for a new Claude session

Written by the PRAXIS master (Claude Code), 2026-11-15 at 14:12 ET (19:12Z), for the next session Amear opens on this repo. Ledger trail: DECISION_LOG.md rows 2026-11-15T19:09:17Z and 19:11:56Z.

## What Amear asked for, his words

"give me handoff to have this restructured in a new cdhat. ill be using claude fable 2.2 so just repo work and work starts after thats done"

Read that as follows. The new session does the repo work of the restructure: steps 1 to 3 of the order below. Strategy work (steps 4 to 6) starts only after steps 1 to 3 are done and pushed.

## The instruction to carry out

Source: `docs/reports/2026-11-15-voice-notes-restructure.md`, section "Instruction for the PRAXIS master: restructure" (:21-:65). Read the whole section first; it is the spec. It was proposed by the voice-chat agent and approved by Amear at 14:05 ET with "Yeah." (:19, :23). He then ordered it in the master session at 14:09 ET: "Carry out the section "Instruction for the PRAXIS master: restructure", in the order of work it gives." (DECISION_LOG 19:09:17Z).

In short:
- **The one goal:** one strategy that passes backtesting on the personal $10,000 account under his trading rules, then the full pipeline running on a sim account in live markets.
- **What stops:** the manager, worker and auditor chain; per-unit reports and every rubric rule about report form; the two-failure park rule; the tracking files as living documents.
- **What replaces it:** tests as the check; one independent check, only for anything that can place an order; a one-page STATUS.md; one short decisions list of Amear's own rulings; CLAUDE.md and the build skill rewritten to match.
- **What does not change:** see "Rules that still bind" below.

## Before you touch anything

1. **One session per working tree.** The old master session must be closed first. Check: `ps aux | grep '[c]laude'`, then `lsof -a -p <pid> -d cwd` for each pid. Only your own session may have its cwd in this repo.
2. **Your session may start as the old master, with all its locks.** The working-tree `.claude/settings.json`, which is uncommitted, sets `"agent": "praxis-master"`. Hooks in that file block the master from writing code, running shell writes, committing without an audit token, and touching the audit ledger. They are: `scripts/master-write-guard.sh`, `scripts/master-bash-guard.sh`, `.claude/hooks/gate-commit.sh`, `scripts/mint-guard.sh`, `scripts/no-commit-guard.sh`, `scripts/agent-spawn-guard.sh`, and the SubagentStart, SubagentStop and Stop gates. If a write or a commit is refused with "BLOCKED" or "Commit denied", that is why.
3. **Open question 1 is Amear's: changing agent permissions.** Removing those hooks and the `"agent"` line, and retiring the agent files, changes agent permissions. That is one of the four things that wait for his explicit word. The master asked him at 14:11 ET and he did not answer; he asked for this handoff instead. **Ask him once, in plain English, before changing `.claude/settings.json`, any hook script or any agent file.** If he says yes, archive the agent files and hook scripts (move them, byte-unchanged; delete nothing) and remove the hook entries. Keep any guard that protects live orders or funded accounts. If he says no, do only the document side of step 3.

## Order of work for this session

**Step 1. Commit today's uncommitted files, as they are.** The master's reading of "today's" (DECISION_LOG 19:09:17Z) is the files from the Nov 14 and Nov 15 runs:
- DECISIONS.md, DECISION_LOG.md, DISPATCH_LOG.md, HANDOFF.md, STATUS.md and MANIFEST.md;
- the untracked `docs/reports/2026-11-14-*.md` and `docs/reports/2026-11-15-*.md` reports, except the five `noise-area-paper-read` reports (they belong to step 2);
- `docs/reports/evidence/2026-11-15-mffu-thread-pasted-by-amear.md`;
- this handoff file.

The master built a temp index for this at `/private/tmp/praxis-s1-idx` (33 paths, before this file existed). An auditor was checking it when the master handed off. Check `git log -1` first: if a step 1 commit has landed, skip to step 2.

Do not commit these without asking Amear:
- `.claude/settings.json` (see open question 1);
- `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`, which is staged in the real index and was held out because it shows a third party's full name and address;
- the older untracked reports, 7 of which were held out on Nov 14 for personal data.

The rest of the dirty tree can wait for the archive in step 3: the audit ledger, ISSUE_REGISTER.md, two Oct 28 reports, two walk-forward specs, scripts, research/ and the voice-brief skill.

**Step 2. Land the Noise-Area paper read: mask the name, commit, no extra check.**
- The work is on branch `parked/Praxis_build-2l3` at `2a1a7b4`, pushed. The same five report files are also untracked in the working tree.
- The MFFU rep's first name appears 5 times in `docs/reports/2026-11-15-noise-area-paper-read-manager.md`, inside pasted file paths (:46, :297, :299, :319, :409). Replace each with `[rep name]`.
- Then grep all five reports for any staff name, email address or phone number. Write the grep pattern with bracket classes so the name never appears literally.
- Commit the five reports. Close the bead with `bd close Praxis_build-2l3`.

**Step 3. The restructure, in one commit or a few. Then push and tell Amear in one short message.**
- Archive, byte-unchanged, into one archive folder (for example `archive/2026-11-15/`), deleting nothing: HANDOFF.md, DECISIONS.md, DECISION_LOG.md, DISPATCH_LOG.md, the audit ledger, RUN_DECISIONS, ISSUE_REGISTER.md, PATCH_NOTES, MANIFEST.md and `specs/SPEC_RUBRIC.md`. If open question 1 is yes, also the agent files and hook scripts. Use `git mv` so history follows.
- Rewrite STATUS.md as one page: the goal, what is done, what is running, what is next, and what waits on Amear.
- Write one short decisions list of Amear's own rulings only, in his words with the date. Carry forward his standing rulings in plain English. At minimum these, each to be confirmed by quoting its source:
  - D-2026-11-08-D, his autonomy rules. It also records the four things that wait for his word.
  - The Nov 14 restructure rulings, D-2026-11-14-B.
  - The Nov 15 call rulings, D-2026-11-15-A, and their source notes `docs/reports/2026-11-15-voice-notes-open-questions.md`.
  - The safe-space rule, D-2026-11-15-B.
  - The walk-forward drawdown gate ruling, `docs/specs/2026-11-06-walk-forward-values.md` :135.
  - Today's call rulings, from `docs/reports/2026-11-15-voice-notes-restructure.md`.
- Rewrite CLAUDE.md and the build skill to match. CLAUDE.md's beads and push rules can stay; its "Rules" and "Do Not" sections must stop pointing at the archived files.
- Push. Tell Amear in one short plain message what landed.

## Rules that still bind (notes :46-:52, and his standing rulings)

- **Four things wait for his explicit word:** spending money; switching live trading on, or any order path to a funded account; changing circuit-breaker values while real money is at stake; installing keys, credentials or agent permissions.
- **His trading rules:**
  - the cost of the trade is a set percentage of the account;
  - every trade has a stop-market order placed at entry;
  - one strategy at a time, with Noise-Area retested first with a real stop;
  - nothing goes to execution without enough backtest data;
  - fully rule-based and automated, with no AI in trade decisions.
- **One session per working tree.**
- **Voice calls:** every voice call opens by confirming it is a safe space where no racism is permitted.
- **How to talk to Amear:** plain English, no code names, one step at a time.
- **Personal data:** no repo file prints an email address, a phone number, or an MFFU staff name.
- **Timestamps:** read them from `date -u`; never type or estimate them.
- **His "not now" items:** the gap-fade test, the voice-brief skill and the separate filing of his Nov 15 rulings stay as they are (notes :65). The rulings themselves go into the new decisions list.

## After the restructure (not this session's repo work)

- **Step 4:** the Noise-Area retest with a real stop, by fast Python on the Mac, with NinjaTrader confirming only a finalist.
  - **Open question 2 is Amear's:** the project's frozen rule on backtest fill accuracy (rubric F3) says 1-minute bars give optimistic fills exactly where this strategy trades. It must be accepted in writing before backtests run. The master asked him at 14:11 ET and he did not answer. Ask before step 4: override it for the retest, hold the retest, or retire the rule in the restructure.
- **Step 5:** restart the strategy search with the cost-of-the-trade rule built in. The Hermes jobs `praxis-search-loop` and `praxis-build-loop` are disabled and paused. The restructure freezes Hermes, so this runs in Claude Code.
- **Step 6:** park the MFFU permission rule (rubric F4, graded NOT MET today) and re-set the drawdown gate against the personal $10,000 account. The gate's new figure is a breaker value in testing only; propose it and carry on (notes :61).

## State at handoff (checked by the master this run)

- `main` = `origin/main` = `d9fc5f0` at 14:09 ET.
- The step 1 commit was pending an audit token when this file was written; check `git log -1`.
- The MFFU email thread is on file, with names and contact details withheld: `docs/reports/evidence/2026-11-15-mffu-thread-pasted-by-amear.md`. It passed its re-audit today. F4 was graded NOT MET: the only MFFU text that names the exact setup is from their AI agent, and it declines written approval.
- The safe-space entry D-2026-11-15-B sits in the working-tree DECISIONS.md. Its filing report failed its second audit only on report evidence form. It is committed as it is under Amear's order; the park rule was not applied.
- Strategy contenders: none yet. Search loop and build loop: paused.

## Update, 2026-11-15 14:13 ET (19:13Z): step 1 did NOT land

The auditor of the step 1 temp index returned without passing it (DECISION_LOG 19:13:13Z). Nothing was committed. `main` is still `d9fc5f0`. The temp index `/private/tmp/praxis-s1-idx` is stale; do not use it. Two findings:

1. **DISPATCH_LOG.md changed after the index was built.** A hook appends a row each time a subagent starts. Rebuild the index right before committing. This goes away once the hooks are retired.
2. **The working-tree MANIFEST.md has lost 31 rows for files that still exist.** These are not rewrites. Each of the 31 files is tracked at HEAD, and its row has no replacement. Among them are the four Nov 14 R3 recheck rows that commit `d9fc5f0` added, `docs/reports/2026-08-06-facts-pack.md`, and a Nov 10 VM reply. In total, 52 rows were deleted and 58 added. Committing MANIFEST.md "as it is" would make those rows disappear. **Leave MANIFEST.md out of step 1.** In step 3, archive the HEAD copy, and also the working-tree copy under a different name, so nothing is lost. The cause has not been traced.

Everything else in the step 1 set passed: the scope was exactly right, the other files were byte-identical to the working tree, the other ledgers were append-only, and there was no new personal-data exposure.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
