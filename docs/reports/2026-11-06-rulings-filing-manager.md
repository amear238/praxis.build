# 2026-11-06 — unit `2026-11-06-rulings-filing` — manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
File Amear's 2026-11-06 evening rulings 1–5 and loop a–e, verbatim, into DECISIONS.md (D-2026-11-06-B with a ruling-5 settlements table); ratify D-2026-11-04-B addendum 1's timing (addendum 4); amend the cost model to MFFU's NQ $4.68 / MNQ $1.90 (D-2026-11-06-C + `config/backtest-cost-model.json` v1.2.0); carry D-2026-08-06-A onto main from `parked/Praxis_build-r8j`; add standing criterion S13 to `specs/SPEC_RUBRIC.md`; append a go-live addendum to the Fusion walkthrough; add/update MANIFEST rows. Everything left UNSTAGED. Working directory `/Volumes/Sensidine/Praxis.build`, main, HEAD `e31b9a4`.

### Authorisation (S5) — both rows, extracted by `sed -n` (not retyped)
`DECISION_LOG.md:464` (WHO: amear; in the DECISION_LOG working tree, not yet in a commit):

```text
- [2026-11-06T20:08:28Z] **WHO: amear** | WHAT: **"RULINGS + LOOP — 2026-11-06 evening voice (WHO: amear). File first, then run."** — pasted into the Code session mid-turn; recorded VERBATIM here first (master's `date -u` read at 20:08:28Z in the same turn; the paste carries no clock); filing into DECISIONS.md follows by unit. Text: "Rulings 1. Bridge install (NEEDS AMEAR 2): the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot. 2. Fees: apply MFFU's published round trip — NQ $4.68, MNQ $1.90 — by new DECISIONS entry amending the cost model. Covered by my earlier "apply the best figure" ruling; settle this class yourself. 3. Commit gate: (a) RATIFY D-2026-11-04-B addendum 1's timing — unpark uqb for a fresh audit; (b) APPROVE the hook change so the gate accepts the auditor's async hand-back. First commit through it is the test; on failure, revert and I keep typing commits. 4. Walk-forward arm (b) and spec NEEDS AMEAR, under "We're not here to fuck around" — strictest reasonable defaults: small grid around the paper's published values (no wide search); ATR 14; exit policies BandOrVWAP / OppBand / Flat1559; in-sample objective = risk-adjusted return with a minimum trade count, never net profit; partial last window dropped; judged arm = (a) fixed rules; arm (b) counts only if it also passes PBO < 0.05. Report the exact values chosen back to me. 5. Handoff NEEDS AMEAR 1, 3–10, 15–17, 19: housekeeping or already answered — settle under R-1104-2. Defaults: test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match; my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched; VM agent reads and reports the NT8 version; Code + auditor judge 2a/2b and log the lift under my ruling; VM agent on Z: while Code runs = second session, coordinate. Loop, in order a. Gate: fresh audit of uqb; hook change; first self-commit as the test. b. Commit fees amendment + these rulings. c. Finish the cli-nt-bridge code read; write the VM install walkthrough + test 2a/2b spec + the first skill(s) as one VM handoff file on Z:. Tell me its exact path so I can point the VM session at it. d. Arm (a) and (b) build per the spec, Mac side, ready to run through the bridge once 2a passes. e. STATUS/HANDOFF as you go; return handoff for the Claude.ai chat at the end — committed, built, blocked, and only decisions that are mine. Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit. If a step needs a ruling, log it, skip it, continue." Master's readings, flagged as readings: (i) "Handoff NEEDS AMEAR 1, 3–10, 15–17, 19" refers to the numbering in `docs/reports/2026-11-06-voice-handoff-evening.md` §4 (1–10 = D-2026-11-06-A's ten; 11–19 carried) — so items 2 (who installs: ruled in 1), 11–12 (gate: ruled in 3), 13 (fees: ruled in 2), 14 (WF spec: ruled in 4), 18 (notes-4 not-ruled: still open) are handled or left as stated; (ii) ruling 3(a) ratifies the addendum's timing by his word — the filing unit writes that ratification as a WHO: amear addendum to D-2026-11-04-B, which is the named unblocking artifact for uqb; (iii) ruling 3(b) approves a code change to the gate hook — the first code change authorised since "Don't change the code without asking me"; its scope is exactly "accept the auditor's async hand-back", nothing else; (iv) ruling 4 sets defaults and asks for the exact values back — the master proposes values in the spec unit's report, he confirms; (v) "arm (a) and (b) build … Mac side, ready to run through the bridge once 2a passes" — the Mac-side build is strategy code on its own branch ("borrowed code on its own branch" applies to bridge-derived code; PRAXIS strategy changes — the tunables becoming inputs — are a code change he has now asked for in step d); (vi) the bridge-read index (`commit-idx-bridge`, PASS 20:08Z) is held as the candidate for the first self-commit test in step a; if the test fails he types it. Standing limitation on every figure above: fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed. | WHY: his rulings, by paste | WHERE: this row; DECISIONS.md entries to follow | WHEN: 20:08Z | HOW: verbatim record | STATE: recorded — filing unit next, then loop a→e
```

`DECISION_LOG.md:463` (WHO: praxis-master, the dispatch):

```text
- [2026-11-06T20:12:00Z] WHO: praxis-master | WHAT: **DISPATCH DECISION — two units in parallel on disjoint files: `2026-11-06-rulings-filing` (loop "file first" + step b content) and `2026-11-06-gate-async-handback` (step a hook change).** Evidence read this turn (Read tool, OBSERVED): `.claude/hooks/gate-commit.sh` 628 lines — `handback_check` (lines 399–455) accepts two shapes: the auditor's `tool_result` carrying the hash line (sync), or a column-0 `<agent-message from="<id>">` frame in a `type=="user"` record or a `queued_command` attachment (background). In THIS harness the auditor's result arrives as a `<task-notification>` block (`<task-id>`, `<result>`) — 418 occurrences of `task-notification` in the session transcript `~/.claude/projects/-Volumes-Sensidine-Praxis-build/8eda06af-….jsonl` (OBSERVED count) — which the function never scans; hence both denials. `audit-provenance.sh` (177 lines) is unaffected: ap_verify checks 1–6 passed both times (the denial text names only the hand-back check). Tokens expire 30 min after mint (line 532) — the bridge token (minted ~20:07Z) will be dead before the fix lands; the first self-commit test therefore needs a fresh reduced re-audit of whichever index is tested (hash unchanged = cheap). `config/backtest-cost-model.json` v1.1.0: `commission_round_turn_usd` 2.96, NQ only; its own header forbids number edits without a DECISIONS entry — ruling 2 supplies it. SPEC_RUBRIC F3 (lines 45–58) governs fill resolution and slippage, not the commission figure; the rubric text itself is untouched by a commission amendment (hard limit "F1–F4 untouched" read as: the four frozen criteria and their artifacts are not edited; D-2026-10-30-A's slippage/fill assumptions stand). RULINGS-FILING unit writes: D-2026-11-06-B (rulings 1–5 + loop verbatim from row 20:08:28Z, readings labelled, R-1104-2 settlements of handoff items 1, 3–10, 15–17, 19 with his defaults), D-2026-11-04-B addendum 4 (ratification of addendum 1's timing, WHO: amear — the named unblocking artifact for `uqb`), D-2026-11-06-C (fees: NQ $4.68 / MNQ $1.90 round turn; JSON → v1.2.0 with recomputed totals; slippage/fill unchanged; limitation sentence unchanged), D-2026-08-06-A carried onto main from the parked branch WITHOUT its leak, SPEC_RUBRIC standing criterion S13 (limitation sentence on every report — settlement of item 5), Fusion walkthrough go-live line appended (item 1), MANIFEST rows incl. a pre-named row for the gate unit's report; checks whether `parked/Praxis_build-r8j` was ever pushed (item 15 — deletion, if any, is the master's later step). GATE unit writes: `handback_check` third shape for the task-notification frame, read ONLY from non-tool_result text of `type=="user"` records (a Bash tool_result in the master's own transcript could otherwise carry a forged frame), positive and negative controls on a scratchpad COPY of the transcript (never the live one), unit-test harness, report; no MANIFEST/DECISIONS edits (owned by the other unit); nothing committed — the hook-change commit is typed by Amear (the gate cannot pass its own fix), then the first self-commit is the test (ruling 3b). Master's readings flagged as readings in the rulings row stand. | WHY: Amear 20:08:28Z "File first, then run" + loop a/b; S5; S9 on the hook | WHERE: DECISIONS.md, config JSON, specs/SPEC_RUBRIC.md, walkthrough, MANIFEST (unit 1); `.claude/hooks/gate-commit.sh`, scripts/tests, report (unit 2) | WHEN: ~20:12Z (estimate; last `date -u` 20:08:28Z) | HOW: two praxis-managers | STATE: open — dispatching both
```

## Rubric criteria addressed (verbatim, `specs/SPEC_RUBRIC.md`)
- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S5 | No approval is inferred from a verbal or in-session exchange. The ledger append is the authorisation.
- S8 | No question that belongs to Amear is answered on his behalf.
- S6 (cross-block) — section below.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| acb285efbe4aac4e5 | ADVERSARIAL, read-only, over DECISIONS.md 1051–1163 | `VERDICT: REFUTED` — 0 BLOCKING, 4 MAJOR, 5 MINOR; fixes applied (Process log step 5) |
| aa63a354a1b0b1562 | ADVERSARIAL, read-only, re-check after fixes + MANIFEST:244, S13, walkthrough, JSON | `VERDICT: NOT REFUTED` — 0 BLOCKING, 2 MAJOR, 4 MINOR; fixes applied or routed to the master (step 6) |

No BUILD worker: every edit is a document append or a named-field JSON edit, done by the manager by script (string replacements asserted unique; quotes inserted by script from the source row).

## Process log
1. Read the two rows, D-2026-11-04-B (773; addendum 1 at 796), addenda 2–3 (834, 859), D-2026-11-06-A (991–1050), handoff §4, fee check, cost model, walkthrough, rubric 45–58 and 103–119.
2. Extracted the paste with `extract.py` (text between `Text: "` and `" Master's readings`; each delimiter asserted to occur once). Drafted the four entries in the scratchpad; `fill.py` inserted the paste, the readings, ruling 3(a) and ruling 2 by script and asserted each of the 14 marked fragments is a substring of the paste (`quotes_checked 14`). Appended once (`1163 DECISIONS.md`, prefix cmp rc=0).
3. JSON: 8 asserted-unique string replacements; validated; totals recomputed by script (`24.68 4.936 24.68 4.936 1.9`).
4. S13: one row inserted after the `| S12 |` line. Walkthrough: 6 lines appended. MANIFEST: row 205 suffix + 6 rows appended. The brief said "update-in-place" for the config, SPEC_RUBRIC and DECISIONS rows; those paths' existing rows declare an "append-only registry" (MANIFEST 116, 117, 153) and DECISIONS gets one row per entry (213–238), so I appended UPDATE/AMENDMENT rows for them (MANIFEST 246–248). Only the gate-commit.sh row (205) was edited in place. This deviates from the brief's wording; the master may convert it.
5. Adversary 1 → REFUTED. Applied fixes in place inside this unit's own uncommitted append (lines 1–1050 still byte-equal to HEAD): the settlement-source sentence (the 20:12:00Z row gives content for items 1, 5, 15, 16 only); item 3 labelled a working definition; item 6 keeps "what tests 2a/2b need"; item 8 points at D-2026-11-06-A item 2; item 19 "proposed", not "to be committed"; the D-C order claim labelled an attestation; the `2.96` list re-run with a filename filter (the brief's `grep -v DECISIONS.md` also drops lines that only mention DECISIONS.md); the code-change rule's source labelled; the preface notes "0 redactions"; MANIFEST:244 "proposed for commit". Finding 4 (report missing) is cured by this file.
6. Adversary 2 → NOT REFUTED. Applied: item 19 now says which of his two statements governs may itself be Amear's question; the readings block is labelled as ending before the row's closing sentence; item 8's identifications are marked as the filer's; walkthrough line 34 is tagged REPORTED BY amear and the closure labelled the master's settlement. Not applied (routed): S13's wording, which is the brief's exact text (see Flags).
7. Evidence captured by one runner (`/bin/zsh -c` per line, cwd = repo root) after all edits; pasted below unedited.

## Verification evidence
Every block below is one command from the runner with its real output, in order. Scratchpad paths are this unit's: `extract.py` (the extractor), `rubric.pre.md` and `manifest.pre.md` (copies taken immediately before this unit's edits).

```text
$ git rev-parse --short HEAD
e31b9a4

$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/rf/extract.py DECISION_LOG.md | cmp - <(sed -n '1063p' DECISIONS.md); echo rc=$?
rc=0

$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/rf/extract.py DECISION_LOG.md | shasum -a 256; sed -n '1063p' DECISIONS.md | shasum -a 256
4c44e8ed685145ebba683a513e71180d846330b430fd1e51a56451b2fe10e73e  -
4c44e8ed685145ebba683a513e71180d846330b430fd1e51a56451b2fe10e73e  -

$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/rf/extract.py DECISION_LOG.md | sed 's/NQ \$4\.68/NQ $4.69/' | cmp - <(sed -n '1063p' DECISIONS.md); echo rc=$?
stdin /dev/fd/13 differ: char 173, line 1
rc=1

$ cmp <(head -1050 DECISIONS.md) <(git show HEAD:DECISIONS.md); echo rc=$?
rc=0

$ git diff --numstat HEAD -- DECISIONS.md MANIFEST.md config/backtest-cost-model.json specs/SPEC_RUBRIC.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
113	0	DECISIONS.md
10	1	MANIFEST.md
10	8	config/backtest-cost-model.json
6	0	docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
11	0	specs/SPEC_RUBRIC.md

$ python3 -I -c 'import json,sys; json.load(open(sys.argv[1]))' config/backtest-cost-model.json; echo rc=$?
rc=0

$ git diff HEAD -- config/backtest-cost-model.json
diff --git a/config/backtest-cost-model.json b/config/backtest-cost-model.json
index 6fdd9eb..3e514c1 100644
--- a/config/backtest-cost-model.json
+++ b/config/backtest-cost-model.json
@@ -1,9 +1,9 @@
 {
   "$schema_note": "PRAXIS Block-2 backtest cost + instrument model. Single source of truth consumed by BOTH the NT8 Strategy Analyzer (VM) backtest config and the Python (Mac) Monte Carlo layer. Encodes trader-locked decision D-2026-07-15-B (Q5). Do NOT hand-edit numbers without a corresponding DECISIONS.md entry. v1.1.0 number changes are authorised by DECISIONS.md D-2026-10-30-A.",
-  "version": "1.1.0",
+  "version": "1.2.0",
   "created": "2026-07-15",
-  "amended": "2026-10-30",
-  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5); amended by D-2026-10-30-A (slippage + fill resolution)",
+  "amended": "2026-11-06",
+  "decision_ref": "DECISIONS.md D-2026-07-15-B (Q5); amended by D-2026-10-30-A (slippage + fill resolution); amended by D-2026-11-06-C (commission)",
   "bead": "Praxis_build-hlw",
   "instrument": {
     "symbol": "NQ",
@@ -16,18 +16,20 @@
     "ticks_per_point": 4
   },
   "cost_model": {
-    "commission_round_turn_usd": 2.96,
+    "commission_round_turn_usd": 4.68,
     "commission_basis": "round_turn",
-    "commission_note": "Applied once per completed round-turn (entry+exit) per contract. If the backtest engine expresses commission per-side, use 1.48 USD/side.",
+    "commission_note": "Applied once per completed round-turn (entry+exit) per contract. If the backtest engine expresses commission per-side, use 2.34 USD/side. 4.68 is MFFU's published NQ 'Total Cost Round Trip' (MFFU does not split it into commission, exchange, clearing, NFA or platform fees; docs/reports/2026-11-05-mffu-fee-check.md:7). See DECISIONS.md D-2026-11-06-C.",
+    "commission_round_turn_usd_mnq": 1.90,
+    "commission_mnq_note": "MNQ round turn per MFFU's published table (docs/reports/2026-11-05-mffu-fee-check.md:7). Recorded for the per-tier DD table of the walk-forward spec; the instrument block above is NQ and every total in this block is NQ. See DECISIONS.md D-2026-11-06-C.",
     "slippage_ticks_per_side": 2,
     "slippage_usd_per_side": 10.0,
     "slippage_round_turn_ticks": 4,
     "slippage_round_turn_usd": 20.0,
     "fill_resolution": "Standard",
     "fill_resolution_note": "NT8 Strategy Analyzer 'Order fill resolution' = Standard on 1-minute bars (no secondary series). Every strategy order is a managed Enter*/Exit* call with no price argument, evaluated OnBarClose at HH:00/HH:30 checkpoints or on any bar with minute-of-day >= 16:00 for FlatEOD, plus the platform session-close exit (IsExitOnSessionCloseStrategy, clock-triggered, INFERRED) (no Set*/Submit*/limit/stop call — OBSERVED in code). That NT8 realises these calls as market orders, so intrabar High/Low ordering does not decide, at a checkpoint with a given position state, whether an order is sent, is INFERRED; 3gm D4 hypothesis 5 (INFERRED) holds that fill resolution could still change how same-bar exit+reverse pairs and the 16:00 orders resolve; via position state (3gm D4 hypothesis 2, INFERRED) that could change which later entries fire. Fill assumed at the next bar's open (INFERRED). CONDITIONAL under the void clause of DECISION_LOG 2026-08-29T00:10:00Z. Proposed limitation wording for backtest reports: 'Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.' Python MC assumes fills already reflect this via the exported NT8 trade list. See DECISIONS.md D-2026-10-30-A.",
-    "total_cost_per_round_turn_usd": 22.96,
-    "total_cost_per_round_turn_ticks": 4.592,
-    "total_cost_breakdown_note": "22.96 = 2.96 commission + 20.00 slippage (4 ticks x 5.00). In ticks: 0.592 commission-equivalent + 4.0 slippage = 4.592 ticks round-turn."
+    "total_cost_per_round_turn_usd": 24.68,
+    "total_cost_per_round_turn_ticks": 4.936,
+    "total_cost_breakdown_note": "24.68 = 4.68 commission + 20.00 slippage (4 ticks x 5.00). In ticks: 0.936 commission-equivalent + 4.0 slippage = 4.936 ticks round-turn."
   },
   "applies_to": [
     "All P&L distributions (NT8 WFA fills + Python Monte Carlo)",

$ git diff -U0 HEAD specs/SPEC_RUBRIC.md | /usr/bin/grep '^@@'
@@ -118,0 +119 @@ without them, or both — and how the Block 4 gate is satisfiable if they differ
@@ -265,0 +267,10 @@ PRAXIS work.

$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/rf/rubric.pre.md specs/SPEC_RUBRIC.md; echo rc=$?
118a119
> | S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." Reports with no such figure carry it too, as house style, until the void clause of D-2026-10-30-A fires. Settled under R-1104-2 on 2026-11-06 (D-2026-11-06-B item 5); source: the flush auditor's finding that the rule was written nowhere (DECISION_LOG 2026-11-06T15:19:51Z). |
rc=1

$ cmp <(head -31 docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md) <(git show HEAD:docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md); echo rc=$?
rc=0

$ sed -n '32,37p' docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md

## Addendum 2026-11-06 (ruling 5 / item 1; appended, nothing above edited)
- **Questions 0–3: closed.** SMB was chosen and set up by Amear's hand (REPORTED BY amear, D-2026-11-06-A item 3: Mac File Sharing on, `Praxis.build` shared, the VM maps it as `Z:`). Closure is the master's settlement under R-1104-2 after ruling 5 delegated the item (D-2026-11-06-B; DECISION_LOG 2026-11-06T20:08:28Z, WHO: amear).
- [ ] **Go-live checklist, his words:** "unmap Z: and turn the share off before real money" (D-2026-11-06-A item 3).
- **The Steps above are moot:** Fusion shows no Sharing pane (D-2026-11-06-A item 3, "no Sharing pane, as flagged", REPORTED BY amear).
- Source: D-2026-11-06-B, ruling 5 settlements table, item 1 and item 10.

$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/rf/manifest.pre.md MANIFEST.md; echo rc=$?
205c205
< | /.claude/hooks/gate-commit.sh | Config | 2 | 2026-11-04 | MODIFIED (R-1104-1, D-2026-11-04-B item 4): commit gate also accepts a provenance-verified praxis-auditor token and a `GIT_INDEX_FILE=<abs path>` temp-index commit, hashing/write-treeing THAT index; main-thread praxis-master needs a praxis-auditor token (legacy token refused for it); legacy orchestrator-auditor route, pathspec/-a/--amend, single-session and tree binding unchanged; see also the /.claude/hooks/ row |
---
> | /.claude/hooks/gate-commit.sh | Config | 2 | 2026-11-04 | MODIFIED (R-1104-1, D-2026-11-04-B item 4): commit gate also accepts a provenance-verified praxis-auditor token and a `GIT_INDEX_FILE=<abs path>` temp-index commit, hashing/write-treeing THAT index; main-thread praxis-master needs a praxis-auditor token (legacy token refused for it); legacy orchestrator-auditor route, pathspec/-a/--amend, single-session and tree binding unchanged; see also the /.claude/hooks/ row; UPDATE 2026-11-06: handback_check third shape, unit 2026-11-06-gate-async-handback, ungraded |
242a243,248
> | /docs/reports/2026-11-06-rulings-filing-manager.md | Report | 2 | 2026-11-06 | Manager report for unit 2026-11-06-rulings-filing (D-2026-11-06-B rulings 1–5 + loop a–e verbatim with ruling-5 settlements; D-2026-11-04-B addendum 4; D-2026-11-06-C cost model v1.2.0; D-2026-08-06-A carried from parked/Praxis_build-r8j; SPEC_RUBRIC S13; Fusion walkthrough addendum); ungraded at time of row |
> | /docs/reports/2026-10-28-voice-session-notes.md | Report | 2 | 2026-10-28 | Amear's 2026-10-28 voice notes (written by Claude from a voice/chat session; not an audited report); source of the in-VM automation ruling (ruling 1, line 7; ledger DECISION_LOG 2026-10-30T21:36:00Z WHO: amear); proposed for commit under ruling 5 / item 19 (master's settlement; hard-limit conflict flagged in D-2026-11-06-B), file unedited |
> | /docs/reports/2026-11-06-gate-async-handback-manager.md | Report | 2 | 2026-11-06 | Manager report for unit 2026-11-06-gate-async-handback (ruling 3b: handback_check accepts the task-notification frame); ungraded at time of row |
> | /config/backtest-cost-model.json | Config | 2 | 2026-07-15 | UPDATE ROW 2026-11-06 (append-only registry; supersedes the earlier rows' commission and totals): v1.2.0, commission $4.68 RT NQ (MFFU published round trip; $2.34/side), new commission_round_turn_usd_mnq $1.90, total $24.68 / 4.936 ticks RT; slippage and fill resolution unchanged (D-2026-10-30-A); authorised by DECISIONS.md D-2026-11-06-C (ruling 2) |
> | /specs/SPEC_RUBRIC.md | Spec | 0 | 2026-07-26 | AMENDMENT ROW 3 (append-only registry — adds to the earlier rows for this path). 2026-11-06: standing criterion S13 (the standing limitation sentence on every report and on every DECISIONS entry stating a backtest or P&L figure), settled under R-1104-2 (D-2026-11-06-B item 5) |
> | /DECISIONS.md | Log | 2 | 2026-11-06 | D-2026-11-06-B (Amear's evening rulings 1–5 and loop a–e, verbatim from DECISION_LOG 2026-11-06T20:08:28Z WHO: amear; ruling-5 settlements as the master's decisions under R-1104-2), D-2026-11-04-B addendum 4 (ratification of addendum 1's timing; unblocking artifact for Praxis_build-uqb), D-2026-11-06-C (cost model commission amendment) and D-2026-08-06-A (carried from parked/Praxis_build-r8j @ f258a5d) appended (DECISIONS.md:1051-1163) |
rc=1

$ /usr/bin/grep -rn '2\.96' --include='*.md' --include='*.json' --include='*.py' --include='*.cs' . | awk -F: '$1 !~ /^\.\/(docs\/reports\/|DECISIONS\.md$|DECISION_LOG\.md$|Redemtion\/)/' | cut -d: -f1,2
./specs/SPEC_RUBRIC.md:50
./STATUS.md:22
./STATUS.md:129
./STATUS.md:286
./STATUS.md:385
./STATUS.md:401
./docs/specs/2026-11-05-phase3-build-specification.md:76
./docs/specs/2026-07-15-block2-backtesting-scope-proposal.md:129
./docs/specs/2026-11-05-walk-forward-spec.md:45
./docs/specs/2026-11-05-walk-forward-spec.md:191
./docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:25
./MANIFEST.md:96
./MANIFEST.md:153
./MANIFEST.md:230
./HANDOFF.md:147
./HANDOFF.md:1181

$ grep -rn '2\.96' --include='*.md' --include='*.json' --include='*.py' --include='*.cs' . | grep -v '^./docs/reports/' | grep -v DECISIONS.md | grep -v DECISION_LOG.md | wc -l
      11

$ git branch -r --contains f258a5d; echo rc=$?
rc=0

$ git ls-remote --heads origin 'parked/*'; echo rc=$?
bd6f4215374032997deda6cbf548ad694ac85eb7	refs/heads/parked/Praxis_build-a9d
29c3e137857532f78c3d72ed997d732015b47a53	refs/heads/parked/Praxis_build-o78
rc=0

$ cmp <(sed -n '1131p' DECISIONS.md) <(git show parked/Praxis_build-r8j:DECISIONS.md | sed -n '245p'); echo rc=$?
rc=0

$ cmp <(sed -n '1134,1163p' DECISIONS.md) <(git show parked/Praxis_build-r8j:DECISIONS.md | sed -n '246,275p'); echo rc=$?
rc=0

$ sed -n '1133p' DECISIONS.md
(carried from `parked/Praxis_build-r8j` @ f258a5d on 2026-11-06 under ruling 5 / item 16; text unchanged except as noted) Noted: this preface line is the only addition; 0 redactions.

$ for w in letter character syllable spell 'begins with' 'starts with' length 'long name' 'short name' abbreviat initial capital; do printf '%s=%s ' "$w" "$(sed -n '1131,1163p' DECISIONS.md | /usr/bin/grep -c -i -- "$w")"; done; echo; printf 'liveness medication=%s\n' "$(sed -n '1131,1163p' DECISIONS.md | /usr/bin/grep -c -i medication)"
letter=0 character=0 syllable=0 spell=0 begins with=0 starts with=0 length=0 long name=0 short name=0 abbreviat=0 initial=0 capital=0 
liveness medication=5

$ for w in medication drug pill dose prescri brand; do printf '%s=%s ' "$w" "$(/usr/bin/grep -c -i -- "$w" docs/reports/2026-10-28-voice-session-notes.md)"; done; echo
medication=0 drug=0 pill=0 dose=0 prescri=0 brand=0 

$ git ls-files --error-unmatch docs/reports/2026-10-28-voice-session-notes.md; echo rc=$?
rc=1
error: pathspec 'docs/reports/2026-10-28-voice-session-notes.md' did not match any file(s) known to git
Did you forget to 'git add'?

$ git show 104c58e:specs/SPEC_RUBRIC.md | /usr/bin/grep -c '| S13 |'; git branch -a --contains 104c58e
1
  parked/Praxis_build-37h

$ /usr/bin/grep -c '| S13 |' specs/SPEC_RUBRIC.md
1

$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)

$ git diff --cached --name-only -- DECISIONS.md MANIFEST.md config/backtest-cost-model.json specs/SPEC_RUBRIC.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md docs/reports/2026-10-28-voice-session-notes.md | wc -l
       0
```

Reading of the evidence (each line points at a block above):
- Byte fidelity: extractor output vs `DECISIONS.md:1063` → `rc=0`; sha256 both `4c44e8ed…e73e`; the negative control changes one character (`$4.68`→`$4.69`) → `differ: char 173` `rc=1`, so the cmp trips.
- Append-only: `head -1050` vs `HEAD:DECISIONS.md` `rc=0`; walkthrough `head -31` vs HEAD `rc=0`; the rubric diff vs the pre-copy is `118a119` only; the MANIFEST diff vs the pre-copy is `205c205` + `242a243,248` only.
- SPEC_RUBRIC hunks. BEFORE (captured earlier this session with the same command): `@@ -265,0 +266,10 @@ PRAXIS work.` AFTER (above): the July hunk, now `@@ -265,0 +267,10 @@`, plus exactly one new hunk `@@ -118,0 +119 @@`.
- Numstat vs HEAD: DECISIONS 113/0; JSON 10/8; rubric 11/0 (1 mine + 10 pre-existing July lines); walkthrough 6/0; MANIFEST 10/1 (7/1 mine + 3 pre-existing rows from other units).
- JSON valid `rc=0`. Slippage, fill_resolution and their notes appear only as context lines in the diff, so they are unchanged.
- The `2.96` list: 16 lines with the filename filter. The brief's form gives 11 here under `/bin/zsh -c`; in the Bash tool, where `grep` is the ugrep wrapper, it printed 38 KB because the `^./docs/reports/` filter does not match that output's prefix. Neither form is complete; D-2026-11-06-C uses the 16.
- Parked branch (item 15): `git branch -r --contains f258a5d` is empty, `rc=0`; `ls-remote` lists a9d and o78 only. No branch on origin holds f258a5d today. A push followed by a deletion in the past is not visible to these commands.
- De-identification: heading cmp `rc=0` and body cmp (1134–1163 vs parked 246–275) `rc=0`. **Redactions: 0**; no title, length or form hint was found in the entry. Probe counts are all 0, and the liveness probe `medication=5` shows the probes read the right text. The 10-28 notes file is 0 on six probes.
- The limitation sentence appears once as this report's own sentence (line 3); its other two occurrences (lines 110 and 127) are inside pasted command output.
- Nothing staged by this unit: the index stat line is `12 files changed, 5726 insertions(+), 2 deletions(-)` (the pre-existing index, unchanged), and 0 of this unit's paths are in the index.

## Adversarial findings
Both returns are transcribed below in full from the hand-back text (the workers were read-only and could not write report files). Adversary 2 reports writing one scratchpad file outside the repo (`…/scratchpad/parked_dec.md`) against its brief; nothing in the repo.

### acb285efbe4aac4e5 — full return
The four entries copy Amear's words exactly, but several labels and evidence claims don't hold up, so the artifact fails on "correctly labelled". Everything was read-only: no file was written, edited or staged, and no report file was made.

**Findings**

1. **Not broken: Amear's words are byte-identical.** I cut the paste out of DECISION_LOG.md:464 by script and compared it with the two text blocks:
   ```
   paste block == paste: True 2295 2295
   readings block == row readings: True 1414 1414
   ```
   Every double-quoted fragment attributed to him in D-B, addendum 4 and D-C is a substring of the paste: lines 1072, 1074–1079, 1087, 1089–1092, 1097, 1113 and 1124 all report `IN PASTE`. That includes the table's "Amear's default" column and addendum 4's quote of ruling 3(a). The other quotes are correctly attributed to §4, D-2026-11-06-A, addendum 1, the r8j report :367 or the fee check.

2. **MAJOR (S5, labelling): most of the settlements column is called "the master's decision" with no ledger record from the master.** The dispatch row (DECISION_LOG:463) gives content for items 1, 5, 15 and 16 only. It says nothing for items 3, 4, 6–10, 17 or 19. A grep of DECISION_LOG, DISPATCH_LOG, HANDOFF and STATUS for the settlement texts ("Claude agent running inside", "does not run agents while", "to be committed with this unit", "deletion decision") found nothing. The filing manager wrote these, and DECISIONS.md:1083 labels them as the master's.

3. **MAJOR (internal contradiction, S8): the item 19 settlement breaks Amear's hard limit.** Line 1097 says the notes file "is to be committed with this unit" and also "does not resolve which governs". §4 item 19 calls that file "(old as-is set)", and his words say "old as-is set out of every commit". The MANIFEST row it points to has already decided it: `MANIFEST.md:244 … committed under ruling 5 / item 19 (D-2026-11-06-B), file unedited`. The file is still untracked (`?? docs/reports/2026-10-28-voice-session-notes.md`).

4. **MAJOR (S1): line 1099 claims "OBSERVED this unit; commands and output in the unit report", but that report doesn't exist.** None of the nine `docs/reports/2026-11-06-*` files belongs to `rulings-filing`. Running `git branch -r --contains f258a5d` myself printed nothing (rc=0), which is consistent with the claim. I did not reproduce the `ls-remote` part, so that is UNVERIFIED.

5. **MAJOR (S1/S2): the "`2.96` grep" list at line 1128 is incomplete but presented as the grep result.** Lines it misses that contain `$2.96`: STATUS.md:286 and :385, MANIFEST.md:96, HANDOFF.md:1181, and docs/specs/2026-11-05-walk-forward-spec.md:191. That last one reads "the ledger's current figure is the $2.96 round-turn commission", and it is in the spec that ruling 4 feeds. Lines with `$22.96` are also missing: STATUS.md:129, MANIFEST.md:153 and HANDOFF.md:147.

6. **MINOR (S2): the item 3 settlement (line 1086) states a fact with no evidence or grade.** "It is the Claude agent running inside the Windows VM" is presented as decided fact, but it is a question about his VM setup.

7. **MINOR: the item 8 settlement points "his ruling" at "(this entry)".** In his own words the lift ruling is "my 'lift completely once confirmed' ruling", which is D-2026-11-06-A item 2.

8. **MINOR: the item 6 settlement narrows his words.** He said "covers what tests 2a/2b need (bridge install + its import)". The settlement keeps only "install and import" and drops the NT8 run on the VM, which is what NEEDS AMEAR 6 asked about.

9. **MINOR: two small problems in D-2026-11-06-C.** It says it was "written before the JSON edit" with no evidence; D-2026-08-06-A's own amendment says such claims are not evidence. Also, the JSON's `$schema_note` still reads "v1.1.0 number changes are authorised by … D-2026-10-30-A".

10. **MINOR: "Don't change the code without asking me" (line 1128) is called "Amear's standing rule", but its source is unclear.** The only places it appears in the repo are the master's reading (iii) and voice-handoff:77, which has a lowercase "don't". No WHO: amear row was found.

11. **Not broken: de-identification.** A diff of the parked blob from line 245 against main from line 1131 shows only `+` lines, both from the added preface (a blank line and the "carried from…" line). Nothing was added that hints at the title, its length or its form. One oddity: the preface says "text unchanged except as noted" but notes nothing.

12. **Not broken: the cost model and line pointers.**
    - JSON sums: 24.68, 4.936 and 2.34 are all correct.
    - Unchanged fields: all `slippage_*`, `fill_resolution` and `fill_resolution_note` show `same` against HEAD.
    - Fee-check citations :7, :8, :9, :89, :96, :98 and :104 are accurate.
    - These pointers check out: :748, :796, :945, :852, :1131, rubric :119, walkthrough :33–37, three-strategy :73/:86, csv-analyses :51, and the `00:54:04Z` row (line 497).
    - The excluded items {2, 11–14, 18} match §4 and reading (i), and ruling 4 picks no value.

VERDICT: REFUTED

### aa63a354a1b0b1562 — full return
I found nothing that breaks S2, S5 or S8. There are six findings: two MAJOR (one curable before commit, one a routing risk) and four MINOR.

**Check 1 — settlements table.** Every row is labelled as the master's decision. Lines 1083 and 1085 say column 3 is "the master's decision under his delegation, not Amear's word". The stated source is accurate: the 20:12:00Z row gives the content of items 1, 5, 15 and 16 only, and lists 1, 3–10, 15–17, 19 as one range. The entry says the table is the first written record for the rest and that the master's ledger row is still owed. Every settled item is in his ruling 5 list. Items 2, 11–14 and 18 are not settled, and 18 is stated as open.

**Check 2 — item 19.** The entry and MANIFEST:244 both say "proposed for commit" and neither claims the file is committed. My command output:
```
error: pathspec 'docs/reports/2026-10-28-voice-session-notes.md' did not match any file(s) known to git
0   (staged count)
```
The conflict is flagged ("This entry does not resolve which governs").

**Check 3 — items 6 and 8.** Both quote his words exactly.

**Check 4 — the `2.96` list.** My grep returned the same 16 lines, in the same order, as the entry: `specs/SPEC_RUBRIC.md:50`, `STATUS.md:22/129/286/385/401`, `phase3-build-specification.md:76`, `block2-backtesting-scope-proposal.md:129`, `walk-forward-spec.md:45/191`, `research-briefs…:25`, `MANIFEST.md:96/153/230`, `HANDOFF.md:147/1181`. A grep across all file types found no other tracked file, only binary files under `.beads/`. The JSON diff matches D-2026-11-06-C field by field, and the totals check out (24.68, and 4.68 / 5 = 0.936).

**Check 5 — carried D-2026-08-06-A.** A difflib comparison of parked lines 245–275 against main lines 1131 onward shows one blank line plus the preface line added, and nothing else. I found no added hint of any kind, at any line.

**Check 6 — S13 and walkthrough.** Neither labels a REPORTED fact as OBSERVED. Finding 6 covers one unlabelled REPORTED statement in the walkthrough.

**Findings**
1. **MAJOR (S2, curable before commit)** — DECISIONS line ~1100: the item 15 findings say "OBSERVED this unit; commands and output in `docs/reports/2026-11-06-rulings-filing-manager.md`", but that file doesn't exist:
   ```
   ls: docs/reports/2026-11-06-rulings-filing-manager.md: No such file or directory
   ```
   The findings themselves reproduce: `git branch -r --contains f258a5d` printed nothing with rc=0, and `ls-remote` shows only `parked/Praxis_build-a9d` and `parked/Praxis_build-o78`. The evidence pointer must exist before commit.
2. **MAJOR (S8, routing risk)** — line ~1097, item 19: "Until the master resolves the conflict" gives the master the call between two of Amear's own statements. One is his item 19 delegation. The other is his hard limit "old as-is set out of every commit", which he called "unchanged". Which one governs is a question about his intent, and he said "If a step needs a ruling, log it, skip it, continue". Nothing is decided yet, so S8 is not broken, but the next step would answer for him.
3. **MINOR (S2)** — line 1069: the master's readings block is called "verbatim from the same row", but it ends before the row's final sentence ("Standing limitation on every figure above: …"). The script check showed the readings are a prefix of the row text, not equal to it. The paste itself (line 1063) is byte-identical.
4. **MINOR** — `SPEC_RUBRIC.md:119` (S13) says the rule "was written nowhere". Amear ruled it at DECISIONS.md:302: "Every backtest report carries: …". S13 does not cite that ruling. It also widens his "every backtest report" to all reports and to DECISIONS entries (figure-free reports "as house style"). Item 5 was delegated to the master, so this is allowed, but the extension isn't labelled as the master's.
5. **MINOR** — item 8 (line 1091) says "auditor" means praxis-auditor and "my ruling" means D-2026-11-06-A item 2, without marking these as the filer's identifications. Item 6's first sentence is narrower than "what tests 2a/2b need", but its second sentence restores his full words.
6. **MINOR (S2)** — walkthrough line 34 states "set up by Amear's hand (Mac File Sharing on, … maps it as `Z:`)" with no REPORTED tag, while line 36 does tag REPORTED BY amear. It also cites the closure only to the WHO: amear row, without saying the settlement is the master's.

One rule slip on my side: I wrote one file outside the repo, `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/parked_dec.md` (a copy of the parked DECISIONS.md for the diff). The brief said to create no file. Nothing in the repo was written, staged or deleted. I wrote no report file because the brief said read-only.

VERDICT: NOT REFUTED

## S6 cross-block check
- **Test 2a × cost amendment.** The 2a reference (1,190 / $197,327.60) ran at $2.96 per trade (`docs/reports/2026-11-01-csv-analyses.md:51`). An exact match needs that commission, not $4.68; at $4.68 the fee check's arithmetic gives $195,280.80 (`docs/reports/2026-11-05-mffu-fee-check.md:9`). Recorded in D-2026-11-06-B; the 2a spec unit sets it.
- **F1–F4.** Not edited. `specs/SPEC_RUBRIC.md:50` (F3 text, "$2.96 round-trip") is listed for the master and not changed. D-2026-10-30-A's slippage and fill resolution are untouched (JSON context lines above).
- **Walk-forward spec.** `docs/specs/2026-11-05-walk-forward-spec.md:191` still says the ledger's current figure is $2.96; listed for the master. The per-tier DD table gets MNQ $1.90 from the new JSON field.
- **Gate unit.** None of its files was touched. Its MANIFEST row is pre-named and marked ungraded.

## Flags for the master (not decided here)
1. **S13 collides with an older S13.** `parked/Praxis_build-37h` (104c58e) holds a different `| S13 |` row (count 1, evidence above). Main now has the new S13. If 37h is ever carried, the IDs clash. Renumbering is the master's call.
2. **S13 wording vs DECISIONS.md:302.** Adversary 2 points out that D-2026-10-30-A already has Amear's "Every backtest report carries: …". So "the rule was written nowhere" is contestable, and S13 widens it to all reports and to DECISIONS entries. The text is the brief's, inserted exactly.
3. **Item 19 conflict.** Ruling 5 delegates "Commit the notes file, or leave?". His hard limit says "old as-is set out of every commit", and §4 labels the file "(old as-is set)". Which governs may be Amear's question (S8). The file stays untracked, and its MANIFEST row says "proposed".
4. **Settlement record owed.** The 20:12:00Z row gives content only for items 1, 5, 15 and 16. The settlements for items 3, 4, 6–10, 17 and 19 come from the brief and are first written in D-2026-11-06-B. A master DECISION_LOG row is owed.
5. **Carried entry's location pointers.** D-2026-08-06-A cites two file:line locations that held the name as of 2026-08-06. They are kept as written, since they are not a title or a length/form hint. Whether a location pointer belongs on main is the master's call.
6. **JSON `$schema_note`** still says "v1.1.0 number changes are authorised by … D-2026-10-30-A". It was not in the field list, so it was not edited.
7. **MANIFEST in-place vs append** (Process log step 4).

## Files staged
None. This unit changed, unstaged: `DECISIONS.md`, `MANIFEST.md`, `config/backtest-cost-model.json`, `specs/SPEC_RUBRIC.md`, `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md`, plus this report (new, untracked). The cached-stat tail line, pasted in the evidence block above: ` 12 files changed, 5726 insertions(+), 2 deletions(-)`.

## Result
**Result: PASS** — the producer's result, ungraded; the seven flags above are for the master and the auditor.
