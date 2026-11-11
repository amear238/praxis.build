# Unit 2026-11-11-mffu-investigation-correction-1 — manager report

Result: PASS

## Task
This unit makes an append-only correction to `docs/reports/2026-11-11-mffu-connection-investigation.md` (282 lines when filed; untracked; written by Hermes on gemini-3.8-flash, REPORTED BY Amear via the Claude.ai channel; unaudited). It makes four edits: (a) one banner line under the H1; (b) itemised de-identification of an MFFU support rep's first name; (c) `## Correction 1 (2026-11-11, unit 2026-11-11-mffu-investigation-correction-1)` appended at the end, holding the master's fixes 1-9; (d) the S13 sentence once, as the last standalone line.

Authority: Amear's go relayed by the Claude.ai channel (chat 2026-11-11 17:27Z, "U do them"). The master's plan is DECISION_LOG row 2026-11-11T17:32:05Z, decided by master under D-2026-11-08-D D1.

Limits held:
- Nothing was staged or committed. The real index still holds only its one held-out path.
- No VM commands, NT8 connection change, email or post.
- No edits to DECISIONS.md, the ledgers, the rubric, the topology doc, the strategy filter audit, .cs, config, scripts, hooks, settings or .claude/.
- Rubric F4 stays FROZEN / NOT MET. The broker route is not decided, and no change to the Sim guard is proposed (D2(b)).

## Rubric criteria addressed
- S1 (specs/SPEC_RUBRIC.md :124): every correction item carries the command and its pasted output.
- S2 (:125): breakers and the live path are regraded to SPECIFIED, and the #7 MaxQty reject to partly IMPLEMENTED.
- S5 (:128): no approval is inferred. Thread facts are graded REPORTED BY the Claude.ai channel.
- S8 (:131): the guard change, the Q4 wording and the route are left to Amear.
- S13 (:136): the sentence appears once, as the last standalone line of the target and of every unit report.
- F4 (:48-57) is cited verbatim in Correction 1 and is not graded.

## Workers dispatched
| Id | Mode | Scope | Outcome |
|---|---|---|---|
| worker1 (1st, a835002d) | BUILD | fixes 1, 2, 6, 8, 9 | Hit its 40-turn cap and wrote no file. Scope split and re-dispatched. |
| worker2 (1st, adec6cd8) | BUILD | fixes 3, 4, 7 | Hit its 40-turn cap and wrote no file. Its fetch dirs /tmp/mffu-fetch-1..12 were not used as evidence. Re-dispatched. |
| worker3 | BUILD | fix 5 (ticket) | PASS. Drafted C3.1-C3.3 (/tmp/mffu-corr/w3.md). |
| worker1 (re-dispatch) | BUILD | fixes 1, 2, 9, D-2026-11-10-B | PASS. C1.1-C1.4. |
| worker4 | BUILD | fixes 6, 8 | PASS. C4.1-C4.14; 38 citations re-run: 18 REPRODUCED, 7 NOT REPRODUCED, 13 DIFFERENT. |
| worker2 (re-dispatch) | BUILD | fixes 3, 7 | PASS. C2.1-C2.4. Fetches /tmp/mffu-fetch-41..45. |
| worker5 | BUILD | fix 4 | PASS. C5.1-C5.4. |
| worker6 | ADVERSARIAL | whole assembled Correction 1 and ticket | FAIL: 0 BLOCKER, 2 MAJOR, 8 MINOR. |
| worker7 | BUILD (fix) | worker6 findings 1, 2, 4, 5, 6, 7, 8 and the redaction in worker6's report | PASS. Fetches /tmp/mffu-fetch-71..72. |
| worker8 | ADVERSARIAL | re-check of worker7's edits | FAIL: 3 MAJOR, 4 MINOR. Two MAJORs were fixed by the manager. One was a false positive. |

## Process log
- 17:33:39Z: the target was copied to /tmp/mffu-orig.md before any edit. sha256 `2cc7869aef2f45754cec73516a56e0409393ca6b24c6549fa5b50b00b5fa6ceb` on both copies. HEAD 85a803f. The index holds one path.
- The first worker1 and worker2 both hit the 40-turn cap with nothing on disk. Their scope was split four ways, with an instruction to write files within the first 3 calls (S1/no-verdict handling: re-dispatched after material reduction).
- The manager applied edits (a) and (b) by line number, using a name variable built at runtime from the index path. The rep name was never typed.
- The manager assembled Correction 1: a preamble (/tmp/mffu-corr/w0.md), then w1, w4, w2, w5, w3, then the S13 line. A snapshot was kept at /tmp/mffu-assembled-v1.md.
- worker6 attacked the assembly. worker7 fixed its findings, and the manager verified the body hash was unchanged. worker8 re-checked.
- The manager applied two single-line fixes for worker8's findings:
  - C2.3: the pasted `grep -o` lacked `-E`, so the command could not produce the pasted output. `-E` was added, and the re-run reproduces the 10 links.
  - Ticket: "(10 November 2026)" became "(my latest emails in it were on 10 November 2026)", because handoff :11 shows a "Re: Re: Re:" subject and the thread predates 10 November.
- worker8's third MAJOR, that the provenance paste drops the remote branch line, was a false positive. The paste already carried it. The manager inserted it before checking, which duplicated the line, then deleted the duplicate. This is a static-read slip by the manager, recorded here. The final paste matches the live 2-line output (evidence below).
- MANIFEST.md: 10 rows appended at the end, at lines 378-387.

### De-identification (edit b): every replaced line
| Original line | Now line | Before (name masked) | After |
|---|---|---|---|
| 61 | 62 | `FILE the MFFU '[rep]' reply` (quoted DECISION_LOG.md:435 label) | `FILE the MFFU [2026-10-28 F4] reply` |
| 105 | 106 | `("[rep]" reply, 2026-10-28)` | `(the 2026-10-28 F4 reply filing)` |
| 106 | 107 | `` `docs/reports/2026-10-28-f4-[rep]-reply-adversarial-final.md` `` | `the 2026-10-28 F4 reply filing (adversarial-final report)` |

Name-token count in the target was 3 before and 0 after. It is 0 in every unit report (evidence below). Line 62 is no longer a verbatim quote of DECISION_LOG.md:435, and Correction 1 says so. The ledger is unchanged.

## Verification evidence (command output)

Baseline (17:33:39Z):
```text
2cc7869aef2f45754cec73516a56e0409393ca6b24c6549fa5b50b00b5fa6ceb  /tmp/mffu-orig.md
2cc7869aef2f45754cec73516a56e0409393ca6b24c6549fa5b50b00b5fa6ceb  docs/reports/2026-11-11-mffu-connection-investigation.md
     282 /tmp/mffu-orig.md
85a803f
token length: 4
target count:        3
```

After edits (a) and (b):
```text
before:        3
after:        0
     283
```

Fix 1, re-read by the manager (`nl -ba ninjascript/PraxisSignalConsumer.cs | sed -n '39,48p;636,640p'; grep -n RequiredAccountPrefix ...`):
```text
    39	// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"
    40	// (e.g. Sim101). The guard is a const — there is no parameter to disable it.
    41	
    42	namespace NinjaTrader.NinjaScript.Strategies
    43	{
    44		public class PraxisSignalConsumer : Strategy
    45		{
    46			#region Hard scope wall (non-configurable)
    47			// SIM ONLY. This prefix check is intentionally a const with no property exposing it.
    48			private const string RequiredAccountPrefix = "Sim";
   636			{
   637				// Defense in depth: re-assert the sim wall at the order boundary.
   638				if (!accountIsSim || Account == null
   639					|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
   640				{
48:		private const string RequiredAccountPrefix = "Sim";
100:					&& Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase);
106:						+ RequiredAccountPrefix + "'). No signals will be processed. SIM ONLY.", LogLevel.Error);
639:				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
```

Fix 2 and D-2026-11-10-B, re-read by the manager (topology :9, :24, :41; the D-2026-11-10-B entry):
```text
     9	Level words, used exactly: SPECIFIED (written in a spec only), WRITTEN (code or config exists, not run), TESTED (run, behaviour observed), TESTED UNDER FAILURE (deliberately tripped, block observed), UNVERIFIED (not observed in this unit, or the records disagree). Specified is not implemented is not tested.
    24	| 1.8 | Redis / PostgreSQL breaker state | Two Redis containers run on the host, both under other compose projects' names; the PRAXIS workflow has no Redis node (1.7), so no breaker state store is wired to the signal path. | SPECIFIED only (Phase 3 spec :107) | [E9], [E10] |
    41	Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.
--- D-2026-11-10-B
2047:## 2026-11-10 — D-2026-11-10-B: live-signal topology adopted as the working design (rubric F1; bead Praxis_build-1hv)
0
```
The `0` is the Rithmic count inside the entry's own text. The entry adopts the path at :41 by reference, and that path ends `→ Rithmic → account` (C1.4).

Other worker claims re-run by the manager (a587a27; MANIFEST counts; walk-forward spec Rapid row):
```text
a587a27 docs: housekeeping 2b (D11 G18, G30; bead zd4) - four 2026-11-01 NinjaTrader grid trade lists archived unaltered into docs/reports/evidence with hashes equal to the readback; D-2026-11-10-A praxispush user deferred with its accepted risk (rubric O2, decided by master under D1, changeable by Amear); reports; MANIFEST rows; DECISION_LOG flush through 10:22Z
--- MANIFEST
     377
0
0
118:| Rapid · 25K | $25,000 | $1,000 | $1,000 (Eval EOD; Sim-Funded intraday trailing) | min(1,000, 1,000) = **$1,000** (equal) | REPORTED BY MFFU's page https://myfundedfutures.com/plans/rapid, fetched 2026-11-05 |
```
worker4's table tally, re-counted by the manager from the table rows:
```text
rows=38 REPRODUCED=18 NOT=7 DIFFERENT=13
```

worker8 MAJOR 1, re-run: with `-E`, the saved fetch-72 page yields the ten links that are pasted. The C2.3 line now reads:
```text
1119:article links on the page (grep -o -E 'href="[^"]*/articles/[0-9]+-[^"]*"' | sort -u):
0
```
(The `0` is the count of the old, broken `grep -o 'href=` form remaining in the target.)

worker8 MAJOR 2 (false positive). Final provenance paste at target lines 299-302, then the live command:
```text
$ git branch -a --contains bf6fcc7
+ r6/announcement-research
  remotes/origin/r6/announcement-research
$ git rev-parse --short HEAD
       2
```
(`2` is `git branch -a --contains bf6fcc7 | wc -l` live, which matches the two pasted lines.)

worker8 MAJOR 3, source: handoff :11 (cut at 220 characters):
```text
    11	- Sent 2026-11-10T19:29:01Z from Amear's Gmail as a reply in the existing MFFU support thread (Gmail message id `1a1c6ef68efc93d2`, thread `19f9edc188595b0c`; subject "Re: Re: Re: Written policy confirmation — a
```

Negative control. A copy of the target was planted with the name token, a fake LAN IP and MAC, and a changed body line 49. Every check tripped:
```text
NEG name=1 net=1 last_is_s13=0 body_hash_match=no
1a2
49c50
61c62
105,106c106,107
282a284,1455
```

Final state (2026-11-11T18:10:13Z). The diff against the pristine copy shows only the banner, the three de-identified lines and the appended section:
```text
$ diff ... | grep -E "^[0-9]"
1a2
61c62
105,106c106,107
282a284,1453
    1453
$ name/net/S13 counts
2026-11-11-mffu-connection-investigation.md name=0 net=0 s13=2 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker1.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker2.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker3.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker4.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker5.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker6.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker7.md name=0 net=0 s13=1 last_is_s13=1
2026-11-11-mffu-investigation-correction-1-worker8.md name=0 net=0 s13=1 last_is_s13=1
Correction 1 starts at line 287
```
The target's s13=2 breaks down as follows: original body line 135 (now 136) quotes the wording inside a bullet. That line is left as filed, since the body is append-only, and Correction 1's provenance paragraph and C4.11 say so. The one standalone occurrence is the last line. The F4 scan of Correction 1 returned two lines, 473 and 477. Both quote the strategy filter audit's "(F4 closed ...)" to state that it is wrong (the rubric lists F4 under FROZEN).

Guarded paths: `git diff --name-only HEAD -- DECISIONS.md specs/SPEC_RUBRIC.md ninjascript config <topology> <filter audit> scripts .claude/hooks` printed only `scripts/dispatch-log-writeahead.sh`. Its mtime is `2026-07-28T12:46:11`, and the session-start status already listed it as modified, so the change predates this unit. `find .claude -newer /tmp/mffu-orig.md -type f` printed nothing. Index and working tree:
```text
docs/reports/evidence/2026-10-28-mffu-[rep]-reply.png
 M MANIFEST.md
?? docs/reports/2026-11-11-mffu-connection-investigation.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-manager.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker2.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker3.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker6.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker7.md
?? docs/reports/2026-11-11-mffu-investigation-correction-1-worker8.md
```
(The index path is shown with the name masked by the runtime variable.)

MANIFEST rows (one per new file):
```text
378:| /docs/reports/2026-11-11-mffu-connection-investigation.md 
379:| /docs/reports/2026-11-11-mffu-investigation-correction-1-manager.md 
380:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md 
381:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker2.md 
382:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker3.md 
383:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md 
384:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md 
385:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker6.md 
386:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker7.md 
387:| /docs/reports/2026-11-11-mffu-investigation-correction-1-worker8.md 
0
```
(`0` = name tokens in the ten new rows.)

## Adversarial findings
worker6 (FAIL, 2 MAJOR / 8 MINOR):
- MAJOR 1: Q5 used T+2 while the R6 design says T+3. Fixed by worker7.
- MAJOR 2: Q3 re-asked what the inactivity page answers. Fixed by worker7, citing consistency capture :50.
- MINORs:
  - article number missing: fixed;
  - fee evidence thin: extended;
  - VM network details pasted from handoff :65/:66/:68: removed from the target and redacted in worker6's own report;
  - handoff untracked: caveat added;
  - bf6fcc7 not on main: caveat added;
  - manager S13: present now;
  - Q4 wording and "I will use": left, because both come from Amear's brief. See below.

worker8 (FAIL, 3 MAJOR / 4 MINOR):
- MAJOR 1 (missing `-E`): fixed.
- MAJOR 3 (thread date): fixed.
- MAJOR 2: a false positive (evidence above).
- MINORs, not fixed:
  - Q5's "flat T-5 to T+3" against the design's simulated fills at T-4/T+4. The ticket states the flat window, which is the design's :22 wording.
  - "on the same computer" has no explicit source. The brief says "local n8n webhook" and "own machine in a VM".
  - The capitalisation of "News" in a quoted MFFU rule.
  - C2.3 under-cites two platform articles that were fetched.

The final three manager edits were verified by re-run (above). No third adversarial pass was run on them.

Open for the master and Amear (S8: not answered here):
- Q4 asks only about an exit before 9:30 AM ET, wording from Amear's brief. The R6 design also has FOMC exits at 13:55 and 2S exits at 16:05 (worker6 MINOR 3). Whether Q4 should cover later same-day exits is Amear's call.
- The ticket says "I will use the NinjaTrader connection" (REPORTED BY Amear's brief), while the repo records the route as not decided.
- worker3 noted that MFFU's 2026-10-28 reply already says algo trading is permitted on all plans. The ticket acknowledges only the 2026-11-10 items. How to read the October reply against F4 is Amear's.

UNVERIFIED or REPORTED BY items in Correction 1:
- "MFFU accounts operate exclusively on the Tradovate backend": REPORTED BY Hermes / UNVERIFIED.
- "NinjaTrader acquired Tradovate": UNVERIFIED. The ninjatrader.com fetch shows a shared d/b/a, not an acquisition.
- "Simulation for evaluations" (line 19): not supported by the article.
- The §6 quote "wants to stay with MFFU if NT8 can connect another way": UNVERIFIED (source not on disk).
- "Most Rithmic prop firms use intraday trailing": REPORTED BY Amear. The on-disk research in the untracked `Redemtion/` RTF compares Topstep and Apex only.
- MFFU's current drawdown rule per plan: UNVERIFIED this unit.
- Whether an evening entry closed before 9:30 AM ET counts as overnight: UNVERIFIED (R6 OPEN-1).
- Which payment model Amear's accounts use (the scope of the inactivity article): UNVERIFIED.
- Platform or routing fee for MFFU's NinjaTrader connection: NOT FOUND. The "activation fees" article was not opened.
- MFFU's replies and the thread facts: REPORTED BY the Claude.ai channel. The handoff file is untracked.

## S6 cross-block check
- The correction touches Block 4/5 go-live: the Sim-only consumer guard is now named as a required, Amear-owned D2(b) change.
- It touches Block 3: breakers SPECIFIED only; topology :41 and D-2026-11-10-B still route via Rithmic, contradicted, route open.
- It touches Block 2 cost: $4.68 is INFERRED to be the full cost on MFFU's NinjaTrader connection. No re-run is ordered, and a587a27 is not a backtest.
- It touches rubric F4: still FROZEN / NOT MET.
- No spec, decision, code or config was changed, so no other block's spec is altered by this unit. The contradictions are recorded for the master to route.

## Files staged
None. Files written by this unit, all left in the working tree:
- the target `docs/reports/2026-11-11-mffu-connection-investigation.md`;
- this report;
- `docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md` … `-worker8.md`;
- MANIFEST.md lines 378-387.

Scratch files outside the repo: /tmp/mffu-orig.md, /tmp/mffu-assembled-v1.md, /tmp/mffu-corr/, /tmp/mffu-fetch-*.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
