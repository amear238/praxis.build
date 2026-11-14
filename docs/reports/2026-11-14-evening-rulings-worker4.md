# Evening rulings, worker 4: ruling 2 (build pause) bead classification

## Task
Classify every open / in_progress / blocked bead against the build-pause clause in docs/reports/2026-11-13-hermes-handoff-strategy-search.md :51-:55 (read :51-:55 only).

## Mode
BUILD (read-only research; only this report written). No bead created/claimed/updated/closed. No tracked file or index edited.

## Criterion
S1 (full bd outputs pasted), classification table with reasons quoting the handoff clause; fgd, ckh, 4uu, gfx, c2w backed by bd show evidence.

## Handoff clause (verbatim, :53-:55)

```
- Stop the roughly 4-hour Hermes timer that restarts the build loop. While the pause holds, start no new build units: no NinjaScript for the trading path, breakers, monitor, n8n workflows, or walk-forward runs on existing strategies.
- These carry on during the pause: step 2, the search loop in step 4, the backtests that loop needs, ledger and close flushes, and pushes.
- **The pause ends when the loop records its third contender.** Hermes then stops the loop, sends Amear one Telegram message naming the three, and builds resume. Which contender goes forward is Amear's call (a strategy decision), so build work on any one of them waits for his pick.
```

## Process log
1. Read handoff :51-:55. 2. Ran the four bd list commands (pasted below, S1). 3. bd show on the named five plus beads whose title was not enough. 4. Classified.

## Verification evidence

### S1: bd outputs (rep first name, if any, replaced with [rep])

```
$ bd list --status open
○ Praxis_build-1ys ● P0 agent-spawn-guard: worker terminal-layer rule bypassable by omitting subagent_type
○ Praxis_build-22q ● P0 [bug] commit-gate-enforcement-contradiction
○ Praxis_build-ckh ● P0 R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought
○ Praxis_build-dj2 ● P0 k7-ratification-spec-insert
○ Praxis_build-hwk ● P0 [bug] commit guards evadable: quoting the subcommand defeats the producer/grader separation
○ Praxis_build-s8g ● P0 [bug] Unguarded write path to .claude/agents/: master-write-guard exempts all subagents at line 8 and no hook registers on that directory
○ Praxis_build-1gd ● P1 [bug] b2-data §4.5 acceptance gate is unreachable: b2_stitch.py emits FLAG where spec requires FAIL
○ Praxis_build-2nh ● P1 live-signal-emission topology for the anchor strategy + breaker placement in the order path
○ Praxis_build-43n ● P1 [bug] S12 v1 remediation: dispatch-log-writeahead.sh has no SubagentStop closer — every session leaves orphan 'STATE: dispatched' rows cleared by hand
○ Praxis_build-4gx ● P1 [bug] praxis-manager ends its turn while its praxis-worker runs in background; in claude -p the worker result is lost
○ Praxis_build-aqf ● P1 [bug] Audit token not minted when auditor returns via hand-back tool (interactive sessions)
○ Praxis_build-cbf ● P1 [bug] F1 remediation: correct false praxis-worker agent-memory in place (open by naming prior claim + marking it refuted), then gitignore .claude/agent-memory/
○ Praxis_build-cyd ● P1 [bug] E5: 'four Bash hooks' rests on an UNGRADED out-of-repo plugin hook; premise has propagated into auto-loaded praxis-worker memory
○ Praxis_build-diq ● P1 PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired
○ Praxis_build-f5f ● P1 ledger-compaction: STATE.md as sole spawn-read + compact.sh archiver (PROJECT-KIT v0.1 retrofit #1)
○ Praxis_build-fx4 ● P1 MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step
○ Praxis_build-kgp ● P1 gate-commit.sh: quoted-region strip fails on multi-line commands, free text anchors false denials
○ Praxis_build-nvn ● P1 [bug] [bug] THIRD gate-commit.sh collision: compact.sh stages at session close, invalidating any live audit token via tree-binding
○ Praxis_build-sk8 ● P1 [bug] S9 registration-field positive control undischarged (matcher / command path in settings.json)
○ Praxis_build-vu8 ● P1 session-53 NQCONT/RTH corpus read — audited FAIL 1 on S1/S2
○ Praxis_build-y9c ● P1 PARKED: restage/C1 commit composition — audit FAIL 2, absolute park rule fired
○ Praxis_build-zd4 ● P1 praxispush security requirement silently dropped: re-provision the low-priv macOS user + move the signal drop dir, OR formally log the removal decision
○ Praxis_build-zyd ● P1 b2 backtest fill-resolution: pin the intrabar fill/bar-resolution assumption BEFORE running the 4uu Strategy Analyzer backtest
○ Praxis_build-37h ● P2 session-34 flush: AUDIT_LOG row o3d + session-34 DECISION_LOG appends + rubric S13
○ Praxis_build-67b ● P2 session-34 flush #2: AUDIT_LOG rows o3d + 37h, staged alone per runbook
○ Praxis_build-7bw ● P2 [bug] commit-tree-verify.sh false alarm after a park commit when a stale last-allowed record has the same command text (C2 finding B2)
○ Praxis_build-86t ● P2 [bug] master-write-guard allowlist gaps: denies praxis-master its own agent-memory dir and AUDIT_LOG.md
○ Praxis_build-9lj ● P2 [bug] gate-manager-output.sh grades the newest docs/reports/*.md, so concurrent managers get each other's reports graded
○ Praxis_build-ajj ● P2 b2-mc: Monte Carlo engine on pooled OOS trades, emit envelope distributions
○ Praxis_build-b5z ● P2 [bug] Import-file volume anomaly: 2021-03-08 RTH volume 4,322 (342 bars; 10:00 bar vol 8) vs 2026-07-17 RTH 284,681 (292 bars), ~66x — bears on D-2026-07-17-A volume-crossover roll; candidate back-month/mis-scaled early segment
○ Praxis_build-bev ● P2 teaching-agent: repo subagent that teaches Amear PRAXIS tasks + maintenance in his teaching style
○ Praxis_build-c2t ● P2 [bug] master-bash-guard.sh false-positives on a redirect char inside a quoted argument
○ Praxis_build-c2w ● P2 De-identification sweep: MFFU rep first name in committed MANIFEST rows and untracked reports
○ Praxis_build-cn4 ● P2 watcher-telegram-activation: close Telegram token rotation so b2data-watch + signals pings reach the trader
○ Praxis_build-fgd ● P2 F2 amendment S6 follow-ups F-1..F-9: specs/code still citing 11:30 close or 15:00-18:00 disable (topology :41/:48/:62/:74/:86, Noise-Area ruleset :8/:79/:84/:99/:105, WF values :65, Flat1559.cs :31, OPEN-F2-5)
○ Praxis_build-gfx ● P2 Close flush of the 2026-11-13 17:00Z run parked after two audit FAILs (HANDOFF/STATUS cards)
○ Praxis_build-lnb ● P2 agent-stack: praxis-manager has no worker agent type to dispatch
○ Praxis_build-nj1 ● P2 agent-stack: master-write-guard Write/NotebookEdit arms are dead code
○ Praxis_build-q36 ● P2 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference
○ Praxis_build-qtk ● P2 Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits
○ Praxis_build-xdr ● P2 b2-refdist: generate shm/reference_distributions.json + schema doc for Block-3 SHM consumer
○ Praxis_build-zi1 ● P2 b2-wfa: build + run walk-forward matrix, emit OOS window stats
○ Praxis_build-1tz ● P3 S13 wording: 'omits all three' imprecise — Task is not a live tool name in this repo; grant enumerates 9 vs 10 observed
○ Praxis_build-2vu ● P3 [bug] NT8 Historical Data downloader: wide-range bulk request spawns runaway error-dialog storm, pegs CPU, freezes UI
○ Praxis_build-518 ● P3 [bug] Win11 VM: NT8 WPF DirectWrite glyph-metrics failure (NotSupportedException in FontFace.GetDesignGlyphMetrics on every layout pass) — NO new window/menu/dialog can render; blocks B1-f GUI setup for human AND automation
○ Praxis_build-6di ● P3 Correct filelayer report: agent-key mid-session lockout claim is false
○ Praxis_build-9qx ● P3 audit-flush: add sanctioned RECONCILED <commit-sha> annotate verb + LANDED-RECONCILED flush-verify class
○ Praxis_build-aac ● P3 nt8-reference residual captures: RTH template hours + Export/Market-Replay + .zip + Flatten wording
○ Praxis_build-fpg ● P3 [bug] gate-manager-output.sh vocabulary gap: no Result token means 'complete, submitted for independent grading'
○ Praxis_build-rpy ● P3 mffu reply PNG held out of D9 (third-party full-name address); still staged in real index

--------------------------------------------------------------------------------
Total: 50 issues (50 open, 0 in progress)

Status: ○ open  ◐ in_progress  ● blocked  ✓ closed  ❄ deferred
$ bd list --status in_progress
◐ Praxis_build-4uu ● P2 b2-signal-repro: re-implement Noise-Area Breakout entry logic in NinjaScript + reconcile vs live/sim TV alerts
◐ Praxis_build-hlw ● P2 b2-data: acquire + validate NQ history, pin roll convention + cost model

--------------------------------------------------------------------------------
Total: 2 issues (0 open, 2 in progress)

Status: ○ open  ◐ in_progress  ● blocked  ✓ closed  ❄ deferred
$ bd list --status blocked
● Praxis_build-jcw ● P0 [bug] guard-evasion payload test + correct the read-only worker memory
● Praxis_build-a9d ● P1 Future-row loading plan: get NQCONT Future ($20/pt, 0.25 tick, CME US Index Futures RTH) to load the 1-min history 2021-03-08..2026-07-17 in the Strategy Analyzer; new baseline 0-S on it; save-as-default step; return handoff to Claude.ai channel
● Praxis_build-amd ● P1 Block 1 kickoff: signal delivery design (remote n8n -> local Mac)
● Praxis_build-10i ● P2 Telegram->Claude inbound control channel (n8n Trigger -> host launchd -> claude -p -> reply)
● Praxis_build-btb ● P2 [bug] B1-f consumer: stop-leg reject cascades to OCO-ID-reuse reject on target leg; also no pre-submit bracket-geometry validation (stop/target vs side vs entry)

--------------------------------------------------------------------------------
Total: 5 issues (0 open, 0 in progress)

Status: ○ open  ◐ in_progress  ● blocked  ✓ closed  ❄ deferred
$ bd ready
○ Praxis_build-ckh ● P0 R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought
○ Praxis_build-22q ● P0 [bug] commit-gate-enforcement-contradiction
○ Praxis_build-dj2 ● P0 k7-ratification-spec-insert
○ Praxis_build-s8g ● P0 [bug] Unguarded write path to .claude/agents/: master-write-guard exempts all subagents at line 8 and no hook registers on that directory
○ Praxis_build-hwk ● P0 [bug] commit guards evadable: quoting the subcommand defeats the producer/grader separation
○ Praxis_build-1ys ● P0 agent-spawn-guard: worker terminal-layer rule bypassable by omitting subagent_type
○ Praxis_build-aqf ● P1 [bug] Audit token not minted when auditor returns via hand-back tool (interactive sessions)
○ Praxis_build-4gx ● P1 [bug] praxis-manager ends its turn while its praxis-worker runs in background; in claude -p the worker result is lost
○ Praxis_build-diq ● P1 PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired
○ Praxis_build-vu8 ● P1 session-53 NQCONT/RTH corpus read — audited FAIL 1 on S1/S2
○ Praxis_build-1gd ● P1 [bug] b2-data §4.5 acceptance gate is unreachable: b2_stitch.py emits FLAG where spec requires FAIL
○ Praxis_build-nvn ● P1 [bug] [bug] THIRD gate-commit.sh collision: compact.sh stages at session close, invalidating any live audit token via tree-binding
○ Praxis_build-f5f ● P1 ledger-compaction: STATE.md as sole spawn-read + compact.sh archiver (PROJECT-KIT v0.1 retrofit #1)
○ Praxis_build-cyd ● P1 [bug] E5: 'four Bash hooks' rests on an UNGRADED out-of-repo plugin hook; premise has propagated into auto-loaded praxis-worker memory
○ Praxis_build-cbf ● P1 [bug] F1 remediation: correct false praxis-worker agent-memory in place (open by naming prior claim + marking it refuted), then gitignore .claude/agent-memory/
○ Praxis_build-43n ● P1 [bug] S12 v1 remediation: dispatch-log-writeahead.sh has no SubagentStop closer — every session leaves orphan 'STATE: dispatched' rows cleared by hand
○ Praxis_build-y9c ● P1 PARKED: restage/C1 commit composition — audit FAIL 2, absolute park rule fired
○ Praxis_build-sk8 ● P1 [bug] S9 registration-field positive control undischarged (matcher / command path in settings.json)
○ Praxis_build-kgp ● P1 gate-commit.sh: quoted-region strip fails on multi-line commands, free text anchors false denials
○ Praxis_build-zd4 ● P1 praxispush security requirement silently dropped: re-provision the low-priv macOS user + move the signal drop dir, OR formally log the removal decision
○ Praxis_build-2nh ● P1 live-signal-emission topology for the anchor strategy + breaker placement in the order path
○ Praxis_build-zyd ● P1 b2 backtest fill-resolution: pin the intrabar fill/bar-resolution assumption BEFORE running the 4uu Strategy Analyzer backtest
○ Praxis_build-fx4 ● P1 MFFU automation-compliance: confirm in writing that fully-automated trading is permitted before any live step
○ Praxis_build-c2w ● P2 De-identification sweep: MFFU rep first name in committed MANIFEST rows and untracked reports
○ Praxis_build-gfx ● P2 Close flush of the 2026-11-13 17:00Z run parked after two audit FAILs (HANDOFF/STATUS cards)
○ Praxis_build-fgd ● P2 F2 amendment S6 follow-ups F-1..F-9: specs/code still citing 11:30 close or 15:00-18:00 disable (topology :41/:48/:62/:74/:86, Noise-Area ruleset :8/:79/:84/:99/:105, WF values :65, Flat1559.cs :31, OPEN-F2-5)
○ Praxis_build-7bw ● P2 [bug] commit-tree-verify.sh false alarm after a park commit when a stale last-allowed record has the same command text (C2 finding B2)
○ Praxis_build-q36 ● P2 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference
○ Praxis_build-b5z ● P2 [bug] Import-file volume anomaly: 2021-03-08 RTH volume 4,322 (342 bars; 10:00 bar vol 8) vs 2026-07-17 RTH 284,681 (292 bars), ~66x — bears on D-2026-07-17-A volume-crossover roll; candidate back-month/mis-scaled early segment
○ Praxis_build-9lj ● P2 [bug] gate-manager-output.sh grades the newest docs/reports/*.md, so concurrent managers get each other's reports graded
○ Praxis_build-c2t ● P2 [bug] master-bash-guard.sh false-positives on a redirect char inside a quoted argument
○ Praxis_build-86t ● P2 [bug] master-write-guard allowlist gaps: denies praxis-master its own agent-memory dir and AUDIT_LOG.md
○ Praxis_build-67b ● P2 session-34 flush #2: AUDIT_LOG rows o3d + 37h, staged alone per runbook
○ Praxis_build-37h ● P2 session-34 flush: AUDIT_LOG row o3d + session-34 DECISION_LOG appends + rubric S13
○ Praxis_build-nj1 ● P2 agent-stack: master-write-guard Write/NotebookEdit arms are dead code
○ Praxis_build-lnb ● P2 agent-stack: praxis-manager has no worker agent type to dispatch
○ Praxis_build-qtk ● P2 Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits
○ Praxis_build-bev ● P2 teaching-agent: repo subagent that teaches Amear PRAXIS tasks + maintenance in his teaching style
○ Praxis_build-cn4 ● P2 watcher-telegram-activation: close Telegram token rotation so b2data-watch + signals pings reach the trader
○ Praxis_build-rpy ● P3 mffu reply PNG held out of D9 (third-party full-name address); still staged in real index
○ Praxis_build-fpg ● P3 [bug] gate-manager-output.sh vocabulary gap: no Result token means 'complete, submitted for independent grading'
○ Praxis_build-1tz ● P3 S13 wording: 'omits all three' imprecise — Task is not a live tool name in this repo; grant enumerates 9 vs 10 observed
○ Praxis_build-6di ● P3 Correct filelayer report: agent-key mid-session lockout claim is false
○ Praxis_build-aac ● P3 nt8-reference residual captures: RTH template hours + Export/Market-Replay + .zip + Flatten wording
○ Praxis_build-9qx ● P3 audit-flush: add sanctioned RECONCILED <commit-sha> annotate verb + LANDED-RECONCILED flush-verify class
○ Praxis_build-2vu ● P3 [bug] NT8 Historical Data downloader: wide-range bulk request spawns runaway error-dialog storm, pegs CPU, freezes UI
○ Praxis_build-518 ● P3 [bug] Win11 VM: NT8 WPF DirectWrite glyph-metrics failure (NotSupportedException in FontFace.GetDesignGlyphMetrics on every layout pass) — NO new window/menu/dialog can render; blocks B1-f GUI setup for human AND automation

--------------------------------------------------------------------------------
Ready: 47 issues with no active blockers

Status: ○ open  ◐ in_progress  ● blocked  ✓ closed  ❄ deferred
```

### bd show evidence, the five named beads (head -25, lines cut to 200 chars)

```
$ bd show Praxis_build-fgd | head -25
○ Praxis_build-fgd · F2 amendment S6 follow-ups F-1..F-9: specs/code still citing 11:30 close or 15:00-18:00 disable (topology :41/:48/:62/:74/:86, Noise-Area ruleset :8/:79/:84/:99/:105, WF values :6
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-12 · Updated: 2026-11-13

DESCRIPTION

  Named, not fixed, in docs/reports/2026-11-12-f2-breaker-amendment-manager.md
  'Follow-ups (named, not fixed)'. Also auditor residuals: #4 backstop fires  
  at 16:00:00 with no margin over the strategy flat (OPEN-F2-1); 15:00-18:00  
  operator lockout overlaps the 4:10 'alert if not flat' step.                



NOTES

  2026-11-13 17:00Z run: OPEN-A1 landed 9bf653a (D-2026-11-13-B, option a,    
  CONDITIONAL; strike ended at 1). OPEN-A2 landed 661e073 (D-2026-11-13-C,    
  option b with a 16:00 default; first audit PASS). Remaining: F-4/F-5 wait   
  for parked diq; F-6 optional; F-8 not edited under D1; residuals OPEN-F2-1  
  and the 15:00-18:00 lockout overlap with the 4:10 alert step.               




$ bd show Praxis_build-ckh | head -25
○ Praxis_build-ckh · R6 research P0 under D7: Pre-Announcement Drift and Announcement-Day Premium on existing 1-minute data, own worktree, nothing bought   [● P0 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-09 · Updated: 2026-11-12

DESCRIPTION

  D-2026-11-08-D D7 fired on D6 (f10603a): at 1 MNQ the three 2026-11-01      
  strategies fail every MFFU tier on the committed values-spec per-window     
  drawdown measure. D7 pulls R6 (D-2026-11-08-A R6, DECISIONS.md:1572-1579)   
  forward to P0. Scope per R6: existing 1-minute data only, nothing bought (R-
  1104-3); runs in parallel with the walk-forward in a separate git worktree  
  on its own branch (R7, v6y); before any build read the MFFU T1 news rule and
  whether an evening entry counts as the same trading day. Noise-Area baseline
  continues through VM tests for the record (D7).                             



NOTES

  2026-11-12 PARKED (absolute park rule, audit-fail-x2): step 2 S4 entry D-   
  2026-11-12-B on parked/Praxis_build-ckh @ 9bf0516 (pushed). FAIL 1 S1       
  manager report :24/:72/:179 (cured by Correction 1). FAIL 2 S1 in original  
  adversary report worker1 :156 placeholder arg, output cut with ... at :133- 
  :314, :154 unpasted claim. A human resumes; cure recipe in HANDOFF top card 
  and DECISION_LOG 09:44:01Z/09:53:00Z. No R6 code exists.                    

$ bd show Praxis_build-4uu | head -25
◐ Praxis_build-4uu · b2-signal-repro: re-implement Noise-Area Breakout entry logic in NinjaScript + reconcile vs live/sim TV alerts   [● P2 · IN_PROGRESS]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: task
Created: 2026-07-15 · Started: 2026-07-16 · Updated: 2026-07-23

DESCRIPTION

  WHY: Q1 CONFIRMED re-implement path (DECISION_LOG 2026-07-15T21:10Z). Re-   
  implement the Zarattini-Aziz-Barbon NQ clock-anchored Noise-Area breakout   
  entry logic in NinjaScript so it runs in the NT8 Strategy Analyzer;         
  reconcile a sample of generated signals against known live/sim TradingView  
  alerts. NEEDS trader-confirmation gap: canonical ruleset + parameter ranges 
  + exit-policy form. ACCEPTANCE: NinjaScript strategy compiles, emits signals
  matching the paper/spec ruleset, sample reconciled. Ref docs/specs/2026-07- 
  15-block2-backtesting-scope-proposal.md §6 §6.3.                            



NOTES

  SESSION 24 (2026-07-23, Mac-side prep — VM steps still trader hands): (1)   
  RECONCILE REFERENCE SETTLED — trader chose SPEC-CONSISTENCY checks          
  (AskUserQuestion): 4uu reconcile = self-contained §B checks (entries only at
  HH:00/HH:30, long-above/short-below band, opposite-band cross REVERSES, flat
  by 16:00, band widens+re-anchors each 09:30, trade-freq sanity). No external
  TV-alert corpus exists (paper re-implementation, never on TV); none         

$ bd show Praxis_build-gfx | head -25
○ Praxis_build-gfx · Close flush of the 2026-11-13 17:00Z run parked after two audit FAILs (HANDOFF/STATUS cards)   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-13 · Updated: 2026-11-13

DESCRIPTION

  Ledger close flush (DECISION_LOG, DISPATCH_LOG, HANDOFF, STATUS) failed     
  audit twice on the master's own card wording: FAIL 1 (17:41:08Z row) three  
  phrases; FAIL 2 (re-audit af2e9b6c15d9672bd): HANDOFF line on 9bf653a omits 
  the fix manager's Result PASS and says it 'cured them' though fault (f) was 
  settled by master ruling; HANDOFF brief-lessons line puts four paraphrased  
  brief rules in quotation marks. Parked per the absolute park rule; a human  
  resumes.                                                                    




$ bd show Praxis_build-c2w | head -25
○ Praxis_build-c2w · De-identification sweep: MFFU rep first name in committed MANIFEST rows and untracked reports   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-13 · Updated: 2026-11-13

DESCRIPTION

  OBSERVED 2026-11-13 (research-filing cure, DECISION_LOG 2026-11-            
  13T20:34:10Z): the MFFU support rep first name survives in HEAD MANIFEST.md 
  :327-:328 (committed before 9ff8a48), in the untracked report               
  docs/reports/2026-11-13-open-a2-worker1.md (once), and in the file name of  
  the one path staged in the real index (2026-10-28 evidence PNG) and of the  
  uncommitted 2026-10-28 F4 reply-filing report. Amear ruled 2026-08-07 that  
  de-identification is forward-only (history not rewritten). Task: decide     
  under D1 how to treat the committed rows (amendment row vs leave) and rename
  or redact the uncommitted files before they are committed.                  




```

### bd show evidence, beads whose title was not enough (head -25, cut to 200 chars, blank lines dropped)

```
$ bd show Praxis_build-2nh | head -25 (blank lines dropped)
○ Praxis_build-2nh · live-signal-emission topology for the anchor strategy + breaker placement in the order path   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-11-10
DESCRIPTION
  Q1 (CRITICAL) from master-agent cross-block audit. OPEN-GAP: Dev A moved the
  Noise-Area strategy into NinjaScript (PraxisNoiseAreaBreakout.cs) but that  
  file is a SELF-CONTAINED BACKTEST strategy (its own header lines 25-27: 'NOT
  the file-drop signal consumer, no order pipeline, no JSON, no share         
  watcher'); it calls EnterLong/EnterShort directly in the backtester.        
  PraxisSignalConsumer.cs is the n8n-path consumer but does NOT compute the   
  Noise-Area signal. NO decision anywhere states what emits the LIVE anchor   
  signal now that the only implementation is NT8-internal. Dev A found the    
  strategy is NOT TradingView-exportable + no Pine source exists — so         
  TradingView cannot emit it either. CONSEQUENCE: if NT8 computes the live    
  signal internally, it never traverses n8n → the Block-3 breakers (specified 
  as n8n workflow / pre-file-write gates per                                  
  STRATEGY_HEALTH_MONITOR_SPEC.md:12 + CLAUDE.md architecture) sit OUTSIDE the
  order path and are bypassed — the just-milestone-signed Block-1 pipe goes   
  unused for the anchor strategy. ACCEPTANCE: a DECISIONS entry stating (a)   
  what emits the live anchor signal, (b) where the nine breakers are enforced 
  under that topology, (c) if NT8-internal, how breakers gate NT8 order       
  submission. BLOCKS 4uu (SHM thresholds off the backtest are meaningless     
  until breaker placement is known).                                          
$ bd show Praxis_build-zyd | head -25 (blank lines dropped)
○ Praxis_build-zyd · b2 backtest fill-resolution: pin the intrabar fill/bar-resolution assumption BEFORE running the 4uu Strategy Analyzer backtest   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-07-25
DESCRIPTION
  GATE raised 2026-07-25 by the Claude.ai master/scoping agent. The Noise-Area
  breakout enters on band-touch and exits on opposite-band/VWAP — both        
  INTRABAR events. Decided data is NT8 default-provider MINUTE bars (D-2026-  
  07-15-B Q4) with $2.96 RT + 1-tick-slippage High fill (Q5). On minute bars  
  the NT8 Strategy Analyzer must ASSUME an intrabar High-vs-Low touch order;  
  for an intrabar entry+exit strategy that assumption can flip P&L sign.      
  UNRESOLVED: is minute resolution + a defined fill assumption adequate, or   
  does 4uu need tick/second data or an explicit intrabar-fill rule?           
  ACCEPTANCE: a written decision (DECISIONS.md) fixing (a) bar/data resolution
  for the backtest, (b) the intrabar fill assumption NT8 will use, (c) why    
  that does not bias the entry/exit of THIS strategy. Master-agent rationale: 
  'a backtest built on the wrong fill resolution, feeding SHM thresholds never
  checked against the breakers that will truncate them, is worse than no      
  backtest — it produces a number you will believe.' BLOCKS 4uu.              
BLOCKS
  ← ◐ Praxis_build-4uu: b2-signal-repro: re-implement Noise-Area Breakout entry logic in NinjaScript + reconcile vs live/sim TV alerts ● P2
$ bd show Praxis_build-hlw | head -25 (blank lines dropped)
◐ Praxis_build-hlw · b2-data: acquire + validate NQ history, pin roll convention + cost model   [● P2 · IN_PROGRESS]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: task
Created: 2026-07-15 · Started: 2026-07-15 · Updated: 2026-07-17
DESCRIPTION
  WHY: backtest needs vetted NQ history (source/granularity per Q4) + pinned  
  roll convention and cost model (Q5) via DECISIONS.md. ACCEPTANCE: history   
  acquired+validated, roll+cost committed. Depends: b2-spec-gaps. Ref         
  docs/specs/2026-07-15-block2-backtesting-scope-proposal.md §6 §6.2, §1.3.   
NOTES
  2026-07-17 (D-2026-07-17-A): NT8-native pull ABANDONED — install lacks      
  Vol/OI+Difference continuous. Method pivot: coworker exports individual NQ  
  quarterly contracts (1-min OHLCV + daily vol/OI) to b2-data/raw/; Claude    
  builds the Vol/OI-crossover+Difference stitch in Python Mac-side, re-imports
  to NT8. Locked roll convention UNCHANGED. OPEN RISK: OI may be absent from  
  free provider -> volume-only fallback needs trader OK.                      
DEPENDS ON
$ bd show Praxis_build-ajj | head -25 (blank lines dropped)
○ Praxis_build-ajj · b2-mc: Monte Carlo engine on pooled OOS trades, emit envelope distributions   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-15 · Updated: 2026-07-15
DESCRIPTION
  WHY: Monte Carlo (shuffle+bootstrap, 10k each proposal) on pooled OOS trades
  produces depth/duration/RoR/CAR-MDD distributions. ACCEPTANCE: MC run,      
  distributions reported. Depends: b2-wfa. Ref docs/specs/2026-07-15-block2-  
  backtesting-scope-proposal.md §6 §6.5, §2.                                  
DEPENDS ON
  → ○ Praxis_build-zi1: b2-wfa: build + run walk-forward matrix, emit OOS window stats ● P2
BLOCKS
  ← ○ Praxis_build-xdr: b2-refdist: generate shm/reference_distributions.json + schema doc for Block-3 SHM consumer ● P2
$ bd show Praxis_build-xdr | head -25 (blank lines dropped)
○ Praxis_build-xdr · b2-refdist: generate shm/reference_distributions.json + schema doc for Block-3 SHM consumer   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-15 · Updated: 2026-07-15
DESCRIPTION
  WHY: Block-3 SHM reads reference distributions; generate + git-track +      
  schema-check against what the SHM build will consume. ACCEPTANCE:           
  reference_distributions.json generated, schema-checked, committed. Depends: 
  b2-wfa, b2-mc. Ref docs/specs/2026-07-15-block2-backtesting-scope-          
  proposal.md §6 §6.6.                                                        
NOTES
  Q6 SUB-INPUT PENDING (D-2026-07-15-B): risk-of-ruin sizing basis = MFFU     
  account + trailing-DD. Exact MFFU account size + trailing-DD limit numbers  
  NOT yet supplied by trader — required before RoR can compute. Ask trader for
  these when this bead is dispatched.                                         
DEPENDS ON
  → ○ Praxis_build-zi1: b2-wfa: build + run walk-forward matrix, emit OOS window stats ● P2
$ bd show Praxis_build-zi1 | head -25 (blank lines dropped)
○ Praxis_build-zi1 · b2-wfa: build + run walk-forward matrix, emit OOS window stats   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-15 · Updated: 2026-07-15
DESCRIPTION
  WHY: walk-forward analysis (§1, 252/63/63 proposal, >=12 OOS windows) is the
  core Block-2 evidence. ACCEPTANCE: WFA runs to completion, OOS window stats 
  emitted, config committed. Depends: b2-data, b2-signal-repro. Ref           
  docs/specs/2026-07-15-block2-backtesting-scope-proposal.md §6 §6.4, §1.     
DEPENDS ON
  → ✓ Praxis_build-6bw: b2-stitch: Python Vol/OI-crossover + Difference continuous NQ series (ahead-of-data build) ● P2
  → ◐ Praxis_build-hlw: b2-data: acquire + validate NQ history, pin roll convention + cost model ● P2
  → ○ Praxis_build-1gd: (BUG) b2-data §4.5 acceptance gate is unreachable: b2_stitch.py emits FLAG where spec requires FAIL ● P1
  → ✓ Praxis_build-6hu: b2-data OI_BLANK: NT8 daily export has NO open-interest column — Vol/OI-crossover roll blocked, trader decision needed ● P1
  → ◐ Praxis_build-4uu: b2-signal-repro: re-implement Noise-Area Breakout entry logic in NinjaScript + reconcile vs live/sim TV alerts ● P2
BLOCKS
  ← ○ Praxis_build-ajj: b2-mc: Monte Carlo engine on pooled OOS trades, emit envelope distributions ● P2
  ← ○ Praxis_build-xdr: b2-refdist: generate shm/reference_distributions.json + schema doc for Block-3 SHM consumer ● P2
$ bd show Praxis_build-q36 | head -25 (blank lines dropped)
○ Praxis_build-q36 · 0-S on NQCONTROW SEP25 gives 1,190 trades (556 L / 634 S) vs retired run 4's 1,211 (584/627) on the Stock row — explain the difference   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-10-31 · Updated: 2026-10-31
DESCRIPTION
  WHY: Amear ruling 2026-10-31T18:2xZ: the Future-row baseline is judged on   
  its own; run 4 (Stock-typed NQCONT, 1 USD/pt, 0.01 tick) is retired (R-VM-  
  6). The trade-count difference is logged here, not blocking Phase 4. WHAT IS
  KNOWN (DECISION_LOG 18:19:03Z): both pre-registered spot bars equal the     
  import file exactly on NQCONTROW; the import file has 0 off-grid prices in  
  1,857,362 rows (tick rounding FALSIFIED); the strategy reads only bar prices
  and session boundaries (IsFirstBarOfSession, minute-of-day; no fills, tick  
  size or P&L), so identical bars in identical sessions must give identical   
  counts. Therefore the per-session bar set differs between the rows or bars  
  differ where the spot checks did not look. CANDIDATES with falsifiers: (A)  
  first in-session bar differs (09:30 vs 09:31 stamped) between the rows under
  the same CME US Index Futures RTH template — read the first bar after the   
  session break on 2026-07-17 on both instruments; (B) the extra Saturday file
  20221112.Last.ncd (32 B) creating a one-bar session — inspect 0-S trades    
  around 2022-11-11..15; (C) daily-file grouping at import (instrument default
  template US Equities RTH vs CME US Index Futures RTH) dropping/adding       
  boundary bars — compare per-day bar counts for one day on both rows; (D)    
  Generate-Minute-bars-from-tick left ticked at import — effect UNVERIFIED. A 
  diagnostic re-run on the Stock row needs Amear's separate approval (R-VM-5).
$ bd show Praxis_build-qtk | head -25 (blank lines dropped)
○ Praxis_build-qtk · Dev-D no-optimization-first-pass vs WFE>=0.50: define the replication-arm gate set + where GO/HOLD/REJECT sits   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-25 · Updated: 2026-07-25
DESCRIPTION
  Q5 (MEDIUM) from master-agent cross-block audit. OPEN-GAP. WFE>=0.50 (OOS/IS
  optimized ratio; DECISIONS.md:183 D-2026-07-15-B Q3) is undefined with no   
  optimization step. Dev D (DECISION_LOG 2026-07-16 item 3) removed           
  optimization from the first pass and deferred WFA (252/63/63) to a later    
  separate arm. So WFE + the optimize-set attach to the DEFERRED optimization 
  arm, not the replication arm (4uu). But which gate set the replication arm  
  sits on, and whether GO/HOLD/REJECT lives on the replication arm or the     
  optimization arm, was never re-specified. There is no fixed 'six non-       
  negotiable gates' list in the repo — only a 7-item NON-BINDING candidate    
  checklist (scope proposal:99-113, adopted 'WORKING' per DECISIONS.md:181).  
  ACCEPTANCE: DECISIONS entry partitioning the Block-2 gate set across        
  replication vs optimization arms and stating which arm carries              
  GO/HOLD/REJECT. BLOCKS 4uu closure. Depends on block3-4-spec-import.        
DEPENDS ON
  → ✓ Praxis_build-r8j: block3-4-spec-import: import the Phase 3 Build Specification (nine NUMBERED circuit breakers + their placement in the order path, the Block-4 live-vs-backtest acceptance gate, 
$ bd show Praxis_build-a9d | head -25 (blank lines dropped)
● Praxis_build-a9d · Future-row loading plan: get NQCONT Future ($20/pt, 0.25 tick, CME US Index Futures RTH) to load the 1-min history 2021-03-08..2026-07-17 in the Strategy Analyzer; new baseline 0-
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-10-31 · Updated: 2026-10-31
DESCRIPTION
  WHY: Amear's rulings R-VM-1..5 (DECISION_LOG 2026-10-31T14:59:37Z): Future  
  row only; Stock row ($1/pt, 0.01 tick) retired as baseline — runs 3/4/0-S   
  all ran on it (REPORTED on screen). The Future row (NQCONT ##-##) threw an  
  unknown-instrument-family error and refused a 2021-03 start; INFERRED: the  
  import landed on the Stock row (NT8 Import has no instrument field — maps by
  file name; two NQCONT rows exist since session 52). WHAT: (1) research on   
  disk (nt8 reference §2/§6, b2-data spec, session 52/53 rows, rescued NT8    
  db/minute folder layout) how NT8 assigns imported minute data when two      
  instruments share a name, and the options to make the Future row hold the   
  bars (rename import file to the expiry form 'NQCONT 09-25', delete/rename   
  the Stock row, rollover collection for ##-##, merge policy); (2) a pre-     
  registered step-by-step walkthrough for Amear with readbacks and stop       
  conditions, no deletions without his explicit step; (3) the save-as-default 
  control confirmed from on-disk sources or marked UNVERIFIED with a readback;
  (4) MANIFEST rows owed (voice handoff, voice notes, this unit); (5) after   
  the baseline lands: the return handoff for the Claude.ai channel. No        
  backtests meanwhile (R-VM-5).                                               
$ bd show Praxis_build-amd | head -25 (blank lines dropped)
● Praxis_build-amd · Block 1 kickoff: signal delivery design (remote n8n -> local Mac)   [● P1 · BLOCKED]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: task
Created: 2026-07-08 · Started: 2026-07-08 · Updated: 2026-07-08
DESCRIPTION
  Design doc deciding how signals reach the local NinjaTrader watcher from the
  remote n8n host. Options from HANDOFF: SFTP push, rsync cron, HTTP-response 
  + local poller, or relocate n8n local. Must honor D-2026-07-04-A build-first
  reorder (Block 1 = full signal path on sim immediately). Acceptance:        
  decision doc in docs/, DECISIONS.md entry appended, bead per chosen         
  implementation task created. Report: docs/reports/-block1-delivery-         
  design.md. Stage, do not commit.                                            
NOTES
  Design doc committed 2032bc1 (docs/design/2026-07-08-block1-signal-         
  delivery.md). Recommendation: event-driven SFTP/SCP push over private tunnel
  (scores 31/35). Blocked on trader sign-off; on approval: append DECISIONS.md
  entry + create beads B1-a..e. Open questions in doc: Mac NAT reality,       
  Tailscale-vs-WireGuard under no-cloud-API rule, NT8 Windows-VM path.        
$ bd show Praxis_build-10i | head -25 (blank lines dropped)
● Praxis_build-10i · Telegram->Claude inbound control channel (n8n Trigger -> host launchd -> claude -p -> reply)   [● P2 · BLOCKED]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: feature
Created: 2026-07-09 · Started: 2026-07-15 · Updated: 2026-07-15
DESCRIPTION
  WHY: trader wants to send messages FROM Telegram back INTO Claude Code (esp.
  to steer/monitor unattended autonomous runs from phone). Outbound (notify.sh
  -> n8n webhook -> Telegram) already works and is confirmed delivering.      
  WRINKLE: n8n runs in Docker; claude CLI + repo are on the host, so the      
  container cannot run 'claude -p' directly. DESIGN (reuse B1-c pattern): n8n 
  Telegram Trigger node -> writes the message as a command file into a host-  
  watched dir -> a host launchd watcher runs 'claude -p ""' in the repo ->    
  captures output -> posts reply via notify.sh. OPEN DECISION (needs trader): 
  authority scope of the channel. RECOMMEND read/report/status ONLY (current  
  bead, bd ready, run audit, pause/stop an autonomous run) per praxis-build-  
  manager sec G (headless=read/report only) + sec F human gates; NOT          
  write/commit/credential authority. SECURITY: restrict Telegram Trigger to   
  the trader's own user/chat ID only; no arbitrary command execution.         
  ACCEPTANCE: trader texts a status command, receives the correct reply in    
  Telegram, within the agreed authority scope; unauthorized senders rejected. 
  Design doc under docs/design/ before build.                                 
$ bd show Praxis_build-btb | head -25 (blank lines dropped)
● Praxis_build-btb [BUG] · B1-f consumer: stop-leg reject cascades to OCO-ID-reuse reject on target leg; also no pre-submit bracket-geometry validation (stop/target vs side vs entry)   [● P2 · BLOCKED
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: bug
Created: 2026-07-15 · Started: 2026-07-15 · Updated: 2026-07-15
DESCRIPTION
  WHY: 2026-07-15 10:35:37 ET Sim101 — valid-schema signal with stop          
  29864/target 29894 both ABOVE market (long entry 29826.75): entry filled,   
  stop rejected ('sell stop above market'), then profit target rejected 'OCO  
  ID bb0a21acd0a4474da5595c3a56a8dfa1 cannot be reused', strategy correctly   
  flattened + self-terminated (GOOD safety behavior — document it). NEEDS: (1)
  investigate whether target-after-stop-reject reuses a dead OCO group id in  
  PraxisSignalConsumer.cs bracket submission (possible code bug) vs NT8       
  cascade artifact; (2) add pre-submit validation: for long stop<entry<target,
  for short target<entry<stop — reject signal to rejected/ with reason instead
  of firing a doomed bracket. ACCEPTANCE: root cause of OCO reuse documented; 
  geometry validation implemented + unit-style reasoning in report; malformed-
  geometry signal -> journal REJECTED, no orders. VERIFY: auditor reviews code
  diff; sim test with bad-geometry payload. Evidence: trader NT8 Log          
  screenshot 2026-07-15 10:45, docs/reports/2026-07-14-b1f-t1-t3-mac-run.md   
NOTES
$ bd show Praxis_build-cn4 | head -25 (blank lines dropped)
○ Praxis_build-cn4 · watcher-telegram-activation: close Telegram token rotation so b2data-watch + signals pings reach the trader   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-07-20 · Updated: 2026-07-20
DESCRIPTION
  WHY: the new b2data-watch daemon (3q4) and the signals stale/backlog daemons
  notify via notify.sh -> ORCH_N8N_WEBHOOK, but Telegram delivery is verified 
  DRY-RUN ONLY (B1-c-fu) pending a Telegram token rotation. Today             
  notifications land in ~/praxis-signals/b2-data/reports/ + landing-log.txt in
  the share (fully functional) but NOT on the trader's phone. WHAT:           
  rotate/confirm the Telegram bot token in the n8n webhook + notify.sh path,  
  live-fire a test ping end-to-end (b2data landing + signals stale-heartbeat),
  confirm the trader receives it. ACCEPTANCE: a real landing/status event     
  produces a Telegram message on the trader's phone; documented. Relates: B1- 
  c-fu (STATUS blocker), 10i (inbound control).                               
$ bd show Praxis_build-dj2 | head -25 (blank lines dropped)
○ Praxis_build-dj2 · k7-ratification-spec-insert   [● P0 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-08-09 · Updated: 2026-08-09
DESCRIPTION
  Insert the K7 row verbatim into docs/specs/2026-08-08-ledger-compaction-    
  spec.md §3 (compact.sh stages only; never invokes git commit; never writes  
  into .git/ — commits stay human-typed through gate-commit.sh). Compress §3  
  to hold body <=60 lines total (## CONFORMANCE currently at line 61) and add 
  a matching CONFORMANCE entry (C-9). SCOPE CLOSED: nothing else may change in
  this file or any other. The acceptance paragraph (holds the 30,000-token    
  positive control, the sole empirical test of ratified K1) is PROTECTED — may
  not be deleted, relocated, or compressed. No body line may be relocated into
  CONFORMANCE to make the count. If the insertion cannot fit within the cap   
  without touching the protected paragraph, HALT AND REPORT overflow rather   
  than choosing an alternative. The five acceptance checks must be inlined as 
  literal text in the report (no 'Suite v3' — it does not exist as a script). 
  Stage the spec file only (git add pathspec-scoped to this file), do NOT     
  commit. Prohibited: touching gate-commit.sh, any guard/hook/agent-definition
  file, P0 beads s8g/hwk/1ys, or Block 2. VERIFY: auditor re-measures body    
  line count directly (wc -l / awk to the CONFORMANCE header), diffs the      
  acceptance paragraph byte-for-byte against pre-state 28b3922 to confirm it  
  is untouched, and confirms git status shows only this one file staged.      
  REPORT: docs/reports/2026-08-09-session48-k7-ratification.md                
$ bd show Praxis_build-diq | head -25 (blank lines dropped)
○ Praxis_build-diq · PARKED: wf-spec-amendment (values spec v2.2 + WF spec A4) - audit FAIL 2, absolute park rule fired   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-11-08 · Updated: 2026-11-08
DESCRIPTION
  Unit 2026-11-08-wf-spec-amendment and its corrections 1-3. Audit FAIL 1     
  (17:08Z: S1 described-not-pasted and a false claim in the report; two       
  unlabelled editor readings; A5 second half and tier pick without OPEN grade;
  S4 on brief-form departures, master scope ruling). Re-audit FAIL 2 (about   
  17:24Z): F1-S1 and S1 - the U7 report Correction 1 calls its pasted spec    
  diff the current diff of record, but correction-3 edited values :12 after   
  that paste, so the pasted values-spec blob (7d0a9c8, not a valid object) is 
  not the staged blob (bfc235f5); every other check PASSED, including         
  fidelity, open items, labels, line stability, pointers, ledger flush, de-   
  identification and S4 under the master scope ruling. Root cause is the      
  master's sequencing: correction-3 was dispatched after correction-2 had     
  pasted its diff. Work is UNCOMMITTED in the working tree: M docs/specs/2026-
  11-06-walk-forward-values.md (21/21), M docs/specs/2026-11-05-walk-forward- 
  spec.md (5/5), M MANIFEST.md rows 299-304, untracked docs/reports/2026-11-  
  08-wf-spec-amendment-manager.md and its correction-1/2/3 reports;           
  DECISION_LOG rows 16:12Z-17:21Z are in the working tree too. The park commit
  to parked/ could not be made: the commit gate needs an audit PASS token and 
  a park never has one (bead Praxis_build-8sw). A human resumes it; the master
  does not. Ledger: DECISION_LOG 2026-11-08T17:25:00Z.                        
$ bd show Praxis_build-vu8 | head -25 (blank lines dropped)
○ Praxis_build-vu8 · session-53 NQCONT/RTH corpus read — audited FAIL 1 on S1/S2   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: task
Created: 2026-08-29 · Updated: 2026-08-29
DESCRIPTION
  Read-only corpus read answering Q1-Q4 on NQCONT resolution and the RTH      
  session anchor. Manager self-graded PASS; independent praxis-auditor        
  returned FAIL on S1 (three blocks presented as pasted command output are not
  the output: a grep returning 10 lines shows 2 with line 33 silently         
  rewritten; a placeholder command string stands in for a real one) and S2    
  (containment section says one foreign file appeared when two did; one       
  ungraded mechanism presupposition in 4e). S8 and S9/R3 PASS. Master re-ran  
  all three charges independently and they reproduce. FAIL 1 of 2 — park rule 
  fires on FAIL 2. Shot disposition is Amear's.                               
```

## Classification

Clause keys used in the reason column (quoted from handoff :53-:54):
- P = "start no new build units: no NinjaScript for the trading path, breakers, monitor, n8n workflows, or walk-forward runs on existing strategies."
- C = "These carry on during the pause: step 2, the search loop in step 4, the backtests that loop needs, ledger and close flushes, and pushes."

Reading notes (worker's, not ruled):
- Only :51-:55 was read. What "step 2" and "the search loop in step 4" contain is NOT read here; the brief's gloss "filing (step 2)" is taken from the brief, UNVERIFIED against the handoff.
- The P list after the colon may be exhaustive or illustrative. Harness / guard / agent-stack work is a build in this project's vocabulary but is not on the list. Those beads are marked UNCLEAR as one group rather than guessed.
- The pause is worded "start no new build units". The two in_progress beads (4uu, hlw) have no unit shown running (4uu updated 2026-07-23, hlw 2026-07-17); classification is on what dispatching them next would be.
- Grade: EXPLICIT = bead text names the clause category; INFERRED = worker's reading from title/description.

| id | title (short) | status | class | grade | reason |
|---|---|---|---|---|---|
| Praxis_build-4uu | b2-signal-repro: Noise-Area entry logic in NinjaScript | in_progress | PAUSES | INFERRED | P "NinjaScript ... walk-forward runs on existing strategies": NinjaScript re-implementation of the existing Noise-Area strategy; zi1 (walk-forward) depends on it. Per 2nh it is a backtest strategy, not the order path, so the "trading path" half is not the match. |
| Praxis_build-zi1 | b2-wfa: build + run walk-forward matrix | open | PAUSES | EXPLICIT (walk-forward) / INFERRED (existing strategy, via 4uu dependency) | P "walk-forward runs on existing strategies". |
| Praxis_build-ajj | b2-mc: Monte Carlo on pooled OOS trades | open | PAUSES | INFERRED | P "walk-forward runs on existing strategies": consumes zi1's OOS output, no input without it. |
| Praxis_build-xdr | b2-refdist: reference distributions for Block-3 SHM consumer | open | PAUSES | INFERRED | P "monitor": output is for the strategy health monitor; also downstream of zi1/ajj. |
| Praxis_build-btb | B1-f consumer OCO reject + bracket-geometry validation | blocked | PAUSES | EXPLICIT | P "NinjaScript for the trading path": fix in PraxisSignalConsumer.cs bracket submission (bead text). |
| Praxis_build-10i | Telegram->Claude inbound channel | blocked | PAUSES | EXPLICIT | P "n8n workflows": "n8n Telegram Trigger node" (bead text). |
| Praxis_build-fgd | F2 amendment follow-ups F-1..F-9 | open | PAUSES (in part) | INFERRED | P "NinjaScript for the trading path, breakers": remaining items include Flat1559.cs :31 and breaker residuals (OPEN-F2-1 backstop at 16:00:00). The pure spec-text items (F-4/F-5 wait on parked diq) are UNCLEAR on their own. |
| Praxis_build-gfx | Close flush of the 2026-11-13 17:00Z run, parked | open | CARRIES ON | EXPLICIT | C "ledger and close flushes": bead text "Ledger close flush (DECISION_LOG, DISPATCH_LOG, HANDOFF, STATUS)". Parked; bead says "a human resumes". |
| Praxis_build-37h | session-34 flush | open | CARRIES ON | EXPLICIT (title) | C "ledger and close flushes". |
| Praxis_build-67b | session-34 flush #2 | open | CARRIES ON | EXPLICIT (title) | C "ledger and close flushes". |
| Praxis_build-c2w | De-identification sweep (MFFU rep first name) | open | CARRIES ON | INFERRED | C "step 2" (filing, per brief gloss): renaming/redacting uncommitted files "before they are committed" is a filing precondition. Committed-row treatment is a D1 decision, not a build. |
| Praxis_build-rpy | mffu reply PNG held out of D9; still staged | open | CARRIES ON | INFERRED (title only) | C "step 2" (filing): disposition of a staged file. |
| Praxis_build-fx4 | MFFU automation-compliance in writing | open | NOT BUILD | INFERRED (title only) | Written confirmation from MFFU: an email / Amear step. Not in P. |
| Praxis_build-vu8 | session-53 NQCONT/RTH corpus read, FAIL 1 | open | NOT BUILD | EXPLICIT | "Read-only corpus read" (bead text); "Shot disposition is Amear's". |
| Praxis_build-b5z | Import-file volume anomaly | open | NOT BUILD | INFERRED (title only) | Data investigation, not in P. |
| Praxis_build-q36 | 0-S trade-count difference, explain | open | NOT BUILD | INFERRED | Explanation work; bead says "A diagnostic re-run on the Stock row needs Amear's separate approval (R-VM-5)". A re-run would be a backtest of an existing strategy, which is in neither list. |
| Praxis_build-1tz | S13 wording | open | NOT BUILD | INFERRED (title only) | Rubric wording edit. |
| Praxis_build-6di | Correct filelayer report | open | NOT BUILD | INFERRED (title only) | Report correction. |
| Praxis_build-aac | nt8-reference residual captures | open | NOT BUILD | INFERRED (title only) | Reference-doc captures on the VM (Amear hand steps). |
| Praxis_build-2vu | NT8 Historical Data downloader error storm | open | NOT BUILD | INFERRED (title only) | VM/NT8 environment fault, not a build unit. |
| Praxis_build-518 | Win11 VM NT8 WPF glyph failure | open | NOT BUILD | INFERRED (title only) | VM environment fault (blocks B1-f GUI setup). |
| Praxis_build-ckh | R6 research P0: Pre-Announcement Drift / Announcement-Day Premium | open | UNCLEAR | INFERRED | Not "existing strategies" (new R6 strategies, so P's walk-forward clause does not reach it). Fits C "the search loop ... the backtests that loop needs" only if step 4's loop absorbs R6, and step 4 was not read. The bead says "before any build read the MFFU T1 news rule", so R6 includes build steps. Parked; "A human resumes". |
| Praxis_build-2nh | live-signal-emission topology + breaker placement | open | UNCLEAR | INFERRED | Acceptance is "a DECISIONS entry", a decision, not code. Its subject is P's "breakers". |
| Praxis_build-zyd | pin intrabar fill/bar-resolution before 4uu backtest | open | UNCLEAR | INFERRED | A DECISIONS entry scoped to 4uu (paused). The same assumption may be needed by C "the backtests that loop needs". |
| Praxis_build-qtk | replication-arm gate set / GO-HOLD-REJECT | open | UNCLEAR | INFERRED | A DECISIONS entry; "BLOCKS 4uu closure" (paused), not code. |
| Praxis_build-hlw | b2-data: acquire + validate NQ history | in_progress | UNCLEAR | INFERRED | Data plumbing that feeds zi1 (paused) and maybe the loop's backtests (C). Not in P. |
| Praxis_build-1gd | b2_stitch.py FLAG vs FAIL acceptance gate | open | UNCLEAR | INFERRED | Python data-tool fix; zi1 depends on it. Not in P. |
| Praxis_build-a9d | Future-row loading plan + new baseline 0-S | blocked | UNCLEAR | INFERRED | Research plus an Amear walkthrough (not build), ending in a baseline backtest of the existing Noise-Area strategy, which is not a walk-forward run. ckh text: "Noise-Area baseline continues through VM tests for the record (D7)". |
| Praxis_build-amd | Block 1 signal delivery design | blocked | UNCLEAR | INFERRED | What remains is trader sign-off (not build). The follow-on beads B1-a..e would be signal-path builds (P). |
| Praxis_build-cn4 | watcher-telegram-activation (token rotation) | open | UNCLEAR | INFERRED | Rotating the token "in the n8n webhook + notify.sh path" may count as P "n8n workflows" / "monitor". It is also a credential hand step. |
| Praxis_build-zd4 | praxispush low-priv user + move signal drop dir, OR log removal | open | UNCLEAR | INFERRED | Moving the drop dir touches the trading path (P). The alternative branch is a decision log entry (not build). |
| Praxis_build-diq | PARKED wf-spec-amendment (values v2.2 + WF A4) | open | UNCLEAR | INFERRED | A walk-forward spec text amendment, not a "walk-forward run" (P). Parked; "A human resumes". |
| Praxis_build-y9c | PARKED restage/C1 commit composition | open | UNCLEAR | INFERRED (title only) | Possibly C filing/pushes, possibly harness. Not shown. |
| Praxis_build-dj2 | k7-ratification-spec-insert | open | UNCLEAR | INFERRED | Ledger-compaction spec edit (harness), not in P. |
| Praxis_build-f5f | ledger-compaction STATE.md + compact.sh | open | UNCLEAR | INFERRED (title only) | Harness tooling build related to ledgers. Not in P, and not itself a "flush" (C). |
| Praxis_build-9qx | audit-flush RECONCILED verb + flush-verify class | open | UNCLEAR | INFERRED (title only) | Tooling for flushes, not a flush (C). Not in P. |
| Praxis_build-bev | teaching-agent subagent | open | UNCLEAR | INFERRED (title only) | Agent-stack build, not in P. |
| Praxis_build-1ys, -22q, -hwk, -s8g, -43n, -4gx, -aqf, -cbf, -cyd, -kgp, -nvn, -sk8, -7bw, -86t, -9lj, -c2t, -lnb, -nj1, -fpg, -jcw (20 beads) | harness: guards, hooks, agent-stack, agent memory | open (jcw blocked) | UNCLEAR | INFERRED (titles only) | Builds on the agent harness, not the trading system. None is on the P list, and none is a C item. Whether "start no new build units" covers them depends on whether the P list is exhaustive. |

### Counts
- PAUSES: 7 (4uu, zi1, ajj, xdr, btb, 10i, fgd in part)
- CARRIES ON: 5 (gfx, 37h, 67b, c2w, rpy)
- NOT BUILD: 9 (fx4, vu8, b5z, q36, 1tz, 6di, aac, 2vu, 518)
- UNCLEAR: 36 (16 named rows + 20 harness beads)
- Total: 57 = 50 open + 2 in_progress + 5 blocked (bd ready's 47 is a subset of open)

## Files staged
None. This report is untracked and was written only by this worker. No bead touched.

## Result
PASS (classification delivered; 36 UNCLEAR beads are routed up for a ruling, not decided here).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
