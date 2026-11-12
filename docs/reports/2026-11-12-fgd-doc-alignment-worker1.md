# 2026-11-12 — fgd-doc-alignment — ADVERSARIAL worker 1

## Task

Unit `2026-11-12-fgd-doc-alignment` (bead `Praxis_build-fgd`, part A). Mode: ADVERSARIAL. HEAD `006a08b`, branch main. Artifact: three appended sections headed "## Amendment note — 2026-11-12 (D-2026-11-12-A alignment)" in `docs/specs/2026-11-10-live-signal-topology.md` (body 1–114), `docs/specs/2026-07-16-b2-noise-area-ruleset.md` (body 1–111) and `docs/specs/2026-11-10-f2-session-flat-proposal.md` (body 1–81), plus the MANIFEST.md fgd rows. Governing sources: D-2026-11-12-A (DECISIONS.md:2205 to the line before :2280 in the working tree; at HEAD it runs from :2205 to the file's last line, :2278, E-4), Amendment 1 of the Phase 3 spec, Rule F2-1 (proposal :20) and the 15:00 disposition (proposal :30) (E-3), rubric F1/F2 (:63–97 at HEAD, E-3), DECISION_LOG.md:42 (same at HEAD and in the working tree, E-4). Six attacks, from the brief. Nothing was staged, committed or edited apart from this report. Line numbers in DECISIONS.md, DECISION_LOG.md and MANIFEST.md are working-tree lines as read during the review; "E-n" means a block in "Correction-1 re-run evidence (2026-11-12)" at the end of this report.

**The artifact changed while I was reviewing it.** At my first read the proposal file held invalid UTF-8 at line 95 (C3a). When I checked again, its mtime was 2026-11-12T08:12:44, and the topology and ruleset files had mtime 08:10:48 (C3b). I re-ran the checks shown in C1c on the current files at 08:15:12 (C1c; C2a reads its output). The grades below are for the files with these hashes: topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3` (C1c).

## Checks run (command + full output)

### C1a — additions only (attack 1)

```
$ cd /Volumes/Sensidine/Praxis.build && bash -c 'for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do echo "FILE $f"; echo "removed-lines(excluding ---header): $(git diff HEAD -- $f | grep "^-" | grep -vc "^--- a/")"; git diff HEAD -- $f | sed -n 1,8p; done; echo "MANIFEST hunks:"; git diff HEAD -U0 -- MANIFEST.md | grep "^@@"; echo "MANIFEST removed: $(git diff HEAD -- MANIFEST.md | grep "^-" | grep -vc "^--- a/")"'
FILE docs/specs/2026-11-10-live-signal-topology.md
removed-lines(excluding ---header): 0
diff --git a/docs/specs/2026-11-10-live-signal-topology.md b/docs/specs/2026-11-10-live-signal-topology.md
index eb0a670..fbda0f4 100644
--- a/docs/specs/2026-11-10-live-signal-topology.md
+++ b/docs/specs/2026-11-10-live-signal-topology.md
@@ -112,3 +112,89 @@ Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, po
 This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's decisions, so O4 parity now also covers emitter-vs-backtest equality); Block 3 (all nine breakers, Redis, PostgreSQL, the fallback script); Block 4 (the paper pass on MFFU sim runs on this path, D8(8)); Block 5 (live, D2(b)); Deviation A (strategy logic in NinjaScript, kept; now also the emitter); Deviation C (reversals are entries for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2 (the flat time and session boundary for #4/#5); rubric F4 (MFFU automation, FROZEN); rubric O2 (`praxispush`); rubric O4 (parity); the SHM thresholds that F1 blocks (`specs/SPEC_RUBRIC.md`:30).
 
 Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
FILE docs/specs/2026-07-16-b2-noise-area-ruleset.md
removed-lines(excluding ---header): 0
diff --git a/docs/specs/2026-07-16-b2-noise-area-ruleset.md b/docs/specs/2026-07-16-b2-noise-area-ruleset.md
index d6a5015..e60ef6a 100644
--- a/docs/specs/2026-07-16-b2-noise-area-ruleset.md
+++ b/docs/specs/2026-07-16-b2-noise-area-ruleset.md
@@ -109,3 +109,62 @@ Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`
 - **T5: instrument transfer** — SPY→NQ is unvalidated by this paper; NQ evidence is third-party (Quantitativo). Confirm the NQ port is treated as requiring its own Block-2 validation, not inheriting the paper's SPY numbers.
 
 *End ruleset spec. All numbered §1–§4 rules carry paper citations; all open items are isolated in §7.*
FILE docs/specs/2026-11-10-f2-session-flat-proposal.md
removed-lines(excluding ---header): 0
diff --git a/docs/specs/2026-11-10-f2-session-flat-proposal.md b/docs/specs/2026-11-10-f2-session-flat-proposal.md
index b78af57..3d3a26b 100644
--- a/docs/specs/2026-11-10-f2-session-flat-proposal.md
+++ b/docs/specs/2026-11-10-f2-session-flat-proposal.md
@@ -79,3 +79,33 @@ How the rule maps to R8 (DECISIONS.md:1583–1589): R8 opens "F2 unfreezes." and
 | OPEN-F2-5 | Adoption of Rule F2-1. | Amear's approval under A6; then a DECISIONS.md entry and the amended #4/#5 text in the breaker spec. |
 
 Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
MANIFEST hunks:
@@ -306,0 +307,8 @@
@@ -431,0 +440,11 @@
MANIFEST removed: 0
```

At review time (working tree), MANIFEST had two insertion hunks: 8 lines at 307–314 from another unit (wf-spec-amendment rows dated 2026-11-08 and 2026-11-09, E-5), and 11 at 440–450. Rows 446–450 are this unit's (C4, C6). Since the review, row 451 was added and the second hunk is now 12 lines (E-5). The whole-file cmp fails on MANIFEST because of the insertion at 307 (C1b). That is expected and is not a finding against this unit.

### C1b — body byte-identity, first run

```
$ cd /Volumes/Sensidine/Praxis.build && git rev-parse --short HEAD && for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md MANIFEST.md; do echo "== $f"; git diff HEAD --numstat -- $f; git diff HEAD -- $f | grep -c '^-[^-]'; echo "HEAD lines: $(git show HEAD:$f | wc -l)"; n=$(git show HEAD:$f | wc -l); head -n $n $f | cmp - <(git show HEAD:$f) && echo "BODY BYTE-IDENTICAL"; done
006a08b
== docs/specs/2026-11-10-live-signal-topology.md
86	0	docs/specs/2026-11-10-live-signal-topology.md
0
HEAD lines:      114
BODY BYTE-IDENTICAL
== docs/specs/2026-07-16-b2-noise-area-ruleset.md
59	0	docs/specs/2026-07-16-b2-noise-area-ruleset.md
0
HEAD lines:      111
BODY BYTE-IDENTICAL
== docs/specs/2026-11-10-f2-session-flat-proposal.md
30	0	docs/specs/2026-11-10-f2-session-flat-proposal.md
HEAD lines:       81
BODY BYTE-IDENTICAL
== MANIFEST.md
19	0	MANIFEST.md
0
HEAD lines:      431
stdin /dev/fd/13 differ: char 142364, line 307
```

(For the proposal, `grep -c` printed nothing on that line under zsh. C1a re-counted it under bash and got 0.)

### C1c — final re-run on the current files (after the 08:10/08:12 edits)

```
$ cd /Volumes/Sensidine/Praxis.build && date '+%Y-%m-%dT%H:%M:%S'; bash -c 'for p in "docs/specs/2026-11-10-live-signal-topology.md 114" "docs/specs/2026-07-16-b2-noise-area-ruleset.md 111" "docs/specs/2026-11-10-f2-session-flat-proposal.md 81"; do set -- $p; head -n $2 $1 | cmp - <(git show HEAD:$1) && echo "$1 body 1-$2 BYTE-IDENTICAL; total lines now $(wc -l < $1); sha1 $(shasum $1 | cut -c1-12)"; done'; python3 -I /tmp/fgdchk/quotes.py; python3 -I /tmp/fgdchk/deid.py | tail -n 1; grep -c 'Session flat gate' docs/specs/2026-11-10-live-signal-topology.md; grep -c 'Session window (operator lockout)' docs/specs/2026-11-10-live-signal-topology.md; grep -n 'D-2026-11-12-A adopts that text\|cannot sit in the strategy either' docs/specs/2026-11-10-live-signal-topology.md | cut -c1-5; grep -n 'OPEN-F2-5 is closed' docs/specs/2026-11-10-f2-session-flat-proposal.md | cut -c1-5
2026-11-12T08:15:12
docs/specs/2026-11-10-live-signal-topology.md body 1-114 BYTE-IDENTICAL; total lines now      200; sha1 5aea715d2ff4
docs/specs/2026-07-16-b2-noise-area-ruleset.md body 1-111 BYTE-IDENTICAL; total lines now      170; sha1 b68c098f4aa1
docs/specs/2026-11-10-f2-session-flat-proposal.md body 1-81 BYTE-IDENTICAL; total lines now      111; sha1 e1d2d72895b3
2026-11-10-live-signal-topology.md cited :41 block-at-note-line 133 byte-identical=True
2026-11-10-live-signal-topology.md cited :48 block-at-note-line 141 byte-identical=True
2026-11-10-live-signal-topology.md cited :54 block-at-note-line 149 byte-identical=True
2026-11-10-live-signal-topology.md cited :61 block-at-note-line 157 byte-identical=True
2026-11-10-live-signal-topology.md cited :62 block-at-note-line 165 byte-identical=True
2026-11-10-live-signal-topology.md cited :74 block-at-note-line 173 byte-identical=True
2026-11-10-live-signal-topology.md cited :78 block-at-note-line 181 byte-identical=True
2026-11-10-live-signal-topology.md cited :86 block-at-note-line 189 byte-identical=True
2026-07-16-b2-noise-area-ruleset.md cited :8 block-at-note-line 129 byte-identical=True
2026-07-16-b2-noise-area-ruleset.md cited :79 block-at-note-line 137 byte-identical=True
2026-07-16-b2-noise-area-ruleset.md cited :84 block-at-note-line 145 byte-identical=True
2026-07-16-b2-noise-area-ruleset.md cited :99 block-at-note-line 153 byte-identical=True
2026-07-16-b2-noise-area-ruleset.md cited :105 block-at-note-line 161 byte-identical=True
2026-11-10-f2-session-flat-proposal.md cited :8 block-at-note-line 92 byte-identical=True
2026-11-10-f2-session-flat-proposal.md cited :79 block-at-note-line 100 byte-identical=True
2026-11-10-f2-session-flat-proposal.md cited :3 block-at-note-line 108 byte-identical=True
topology line 124 == '> '+Phase3:212 : False
topology line 128 == '> '+Phase3:224 : False
TOTAL hits = 0
3
3
136:A
184:A
103:A
```

Attack 1: PASS. All three bodies are byte-identical to HEAD, and all three diffs remove 0 lines.

### C2a — quoted old lines vs HEAD (attack 2)

`/tmp/fgdchk/quotes.py` takes each fenced text block in each note and string-compares it with that file's HEAD blob (`git show HEAD:` plus the file's path) at the line named by the preceding `### :N` heading. For the proposal's `:3` block it uses the line named by "Read with :3". Output is in C1c: 16 of 16 blocks byte-identical=True. The script text is pasted in E-6.

The two "False" lines are a bug in my script, not in the note. The script adds a `> ` prefix (`q=='> '+p3[cite-1]`, E-6), but the Phase 3 lines already start with `> ` (C2c). C2b is the correct byte comparison.

### C2b — Phase 3 :212 / :224 quotes

```
$ cd /Volumes/Sensidine/Praxis.build && cmp <(sed -n '124p' docs/specs/2026-11-10-live-signal-topology.md) <(git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '212p') && echo "topology:124 == Phase3:212 BYTE-IDENTICAL"; cmp <(sed -n '128p' docs/specs/2026-11-10-live-signal-topology.md) <(git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '224p') && echo "topology:128 == Phase3:224 BYTE-IDENTICAL"
topology:124 == Phase3:212 BYTE-IDENTICAL
topology:128 == Phase3:224 BYTE-IDENTICAL
```

### C2c — Phase 3 names and amended lines at HEAD

```
$ cd /Volumes/Sensidine/Praxis.build && git status --short docs/specs/2026-11-05-phase3-build-specification.md; echo "--- P3 HEAD :97-105"; git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '97,105p' | cut -c1-90; echo "--- P3 HEAD :189,:212,:224"; git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n '189p;212p;224p'; echo "--- topo 124,128"; sed -n '124p;128p' docs/specs/2026-11-10-live-signal-topology.md
--- P3 HEAD :97-105
1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatte
2. Max trades per day — trade count hits daily max → disable order submission
3. Consecutive loss (“two and done”) — 2 consecutive losers in one session → identical to 
4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → 
7. Max position size — order quantity exceeds plan → reject
8. Stale signal filter — signal file older than X seconds → reject (prevents acting on del
9. Heartbeat dead-man switch — if n8n hasn’t confirmed system health in 5 minutes → disabl
--- P3 HEAD :189,:212,:224

> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.
> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
--- topo 124,128
> 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.
> 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
```

The Phase 3 spec has no working-tree change: `git status --short` printed nothing.

### C2d — rubric, DECISION_LOG:42 and commit citations

```
$ cd /Volumes/Sensidine/Praxis.build && echo "--- rubric HEAD grep"; git show HEAD:specs/SPEC_RUBRIC.md | grep -n '^## \|^### F2\|Unblocks when.\*\* A DECISIONS\|^15:00 disposition, and breaker' ; echo "--- rubric e3323a8 :30-31"; git show e3323a8:specs/SPEC_RUBRIC.md | sed -n '30,31p'; echo "--- c29d08b changed rubric?"; git show --stat c29d08b | grep -i rubric; echo "--- DECISION_LOG:42 fragments"; sed -n '42p' DECISION_LOG.md | grep -o '2026-07-16T19:29Z\|(1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)\|(3) FIRST build = pure paper replication with FIXED params\|trader (Amear) + orchestrator'
--- rubric HEAD grep
17:## FROZEN — nothing downstream may proceed until these clear
46:## PASSED — closed criteria
79:Filer's note, not a ruling: F2 is moved here out of FROZEN. F2's own unblock clause, from its text at `e3323a8` :30–31 joined with one space: "**Unblocks when.** A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to match." The governing rule is Rule F2-1, approved by Amear (D-2026-11-11-A V2, DECISIONS.md; DECISION_LOG 2026-11-11T18:19:40Z, WHO: amear). The 15:00 disposition and the amended #4/#5 text are in D-2026-11-12-A (DECISIONS.md) and Amendment 1 at the end of `docs/specs/2026-11-05-phase3-build-specification.md`, both committed at `e3323a8`; the #4/#5 text is the master's adoption of the F2 proposal's replacement text under D-2026-11-08-D D1, not Amear's words. The auditor graded the match (DECISION_LOG 2026-11-12T06:12:00Z, check 4: no contradiction left between the 11:30 close, the 15:00–18:00 disable and the 16:00 flat). Residuals named there and in bead `Praxis_build-fgd`, not contradictions: #4's backstop fires at 16:00:00 with no margin over the strategy's own flat (OPEN-F2-1); the 15:00–18:00 operator lockout overlaps #4's "alert if not" flat by 4:10. The breakers remain SPECIFIED ONLY. The move is made under A11 (rubric :3–6) and D-2026-11-08-D D1 as the master's decision, changeable by Amear.
81:### F2 — Session-flat time vs. breakers #4 and #5
93:**Unblocks when.** A DECISIONS.md entry names the governing rule and the
94:15:00 disposition, and breaker specs #4 and #5 are amended to match.
99:## OPEN — gradeable now
123:## Standing criteria — graded on every dispatch
256:## Process rulings — binding on the orchestrator
434:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
--- rubric e3323a8 :30-31
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
--- c29d08b changed rubric?
    rubric: F2 moved FROZEN to PASSED@e3323a8 (filer note under A11 and D-2026-11-08-D D1, changeable by Amear; Rule F2-1 approved by Amear in D-2026-11-11-A, breakers #4/#5 amended in D-2026-11-12-A); close flush - HANDOFF and STATUS 2026-11-12 cards, DECISION_LOG and DISPATCH_LOG rows; audit PASS
 specs/SPEC_RUBRIC.md | 33 ++++++++++++++++++---------------
--- DECISION_LOG:42 fragments
2026-07-16T19:29Z
trader (Amear) + orchestrator
(1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)
(3) FIRST build = pure paper replication with FIXED params
```

These verify:
- the rubric citations :93–94, :81 and :30–31@e3323a8;
- that F2 sits under PASSED (heading :46 comes before :81, and the next heading is :99);
- that c29d08b touched the rubric;
- every DECISION_LOG.md:42 fragment the ruleset note quotes, including WHO (the quoting line, ruleset :121, is pasted in E-8).

### C2e — DECISIONS.md citations (:2108, :1551, :1744–1745); the first paste below lacks the blank line :2260 that its `sed -n '2260,2279p'` prints first (E-4)

````
$ cd /Volumes/Sensidine/Praxis.build && sed -n '2260,2279p' DECISIONS.md; echo "--- 2108 (cut 300)"; sed -n '2108p' DECISIONS.md | cut -c1-300; echo "--- 1551 grep"; sed -n '1551p' DECISIONS.md | grep -o 'RTH = 09:30–16:00 ET'; echo "--- 1744-1745"; sed -n '1744,1745p' DECISIONS.md
Moving #4 from 11:30 to 16:00 and removing #5's system disable change breaker values, but no real money is at stake: no account exists. Source, copied by script from `docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md`:10 (committed at `9905804`; REPORTED BY the Claude.ai channel): "Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard." The order path is also walled to Sim accounts, copied by script from `ninjascript/PraxisSignalConsumer.cs`:39: "// HARD SCOPE WALL: refuses to run unless the attached account name starts with "Sim"". DECISION_LOG.md:854 cites D-2026-11-11-A for "Amear has no MFFU account"; that statement is not in D-2026-11-11-A; its source is the return handoff's :10, cited above. Once real money is at stake, any further change to these values waits for Amear (D2(c)).

**Level.** The nine breakers, #4 and #5 included, remain SPECIFIED ONLY: zero implemented, zero tested, zero tested under failure (Phase 3 import status note, :11). This entry changes text, not level.

**Rubric F2.** The unblock clause, copied by script from `specs/SPEC_RUBRIC.md`:30–31:

```text
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
```

This entry names the governing rule (Rule F2-1) and the 15:00 disposition, and records the amendment of #4 and #5. It does not grade the clause and does not change F2's state. The F2 state move is a later, separate unit after this unit is audited and committed; DECISION_LOG.md:854 item (4), copied by script: "(4) the rubric F2 state move is a later, separate unit after this one is audited and committed (F1 precedent `b4c3291` → `d30ab4d`)." A6 ties F2's state change to Amear's approval (DECISIONS.md:1744–1745); whether A6 is triggered is not graded here. Citation note, not an edit: the proposal :8 cites the unblock clause as (`specs/SPEC_RUBRIC.md`:43–44); the clause is at :30–31.

**What this entry does not do.** It builds nothing: no code, no n8n workflow, no NinjaScript, no Redis or PostgreSQL. It edits no rubric line and no spec other than the Phase 3 spec's appended Amendment 1; the F2 proposal, the topology document, the walk-forward spec and values, and the Noise-Area ruleset are not edited. It sets no value for #1, #2, #3, #6, #7, #8 or #9. It decides no D2 item. It does not decide OPEN-F2-1 to OPEN-F2-4 (proposal :75–78) or how #5's operator lockout is enforced (topology doc OPEN-T8, :105). D-2026-11-10-B's statement that the F2 proposal is "PROPOSED, not adopted" (DECISIONS.md:2068) is superseded for the #4/#5 text by this entry; that entry is not edited.

**S6 cross-block.** Graded line by line in `docs/reports/2026-11-12-f2-breaker-amendment-manager.md` (S6 section); nothing is edited by it. Conflicts and the other follow-ups are named there as F-1 to F-9 (its subsection "Follow-ups (named, not fixed)"); that subsection is the full list, and this entry does not restate it. Bearings: rubric O4 (breakers-on vs breakers-off backtest; #4 and #5 now share the 16:00-flat clock of the current backtests, #2 and #3 still differ; O4's question is not answered here); OPEN-F2-1 (backtest flat on the 15:59 or the 16:00 bar); the Phase 3 fallback script's "session time" threshold (:109; the line states no value) is read by this entry as 16:00 under the amended #4; Block 4 and Block 5 (live path, D2(b)).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

--- 2108 (cut 300)
**V2 — Rule F2-1: APPROVED (A6).** (return-handoff :45–48.) The words put to Amear were the channel's summary, return-handoff :46: "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." Amear: "Uh, yeah, you have my approval." (return-ha
--- 1551 grep
RTH = 09:30–16:00 ET
--- 1744-1745
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.
````

```
$ cd /Volumes/Sensidine/Praxis.build && sed -n '1551p' DECISIONS.md | cut -c1-60
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) a
```

### C2f — D-2026-11-12-A body (DECISIONS.md:2205–2259)

````
$ cd /Volumes/Sensidine/Praxis.build && grep -n '^## D-2026-11-12-B\|^### D-2026-11-12-B\|D-2026-11-12-B' DECISIONS.md | head -3; echo "--- DECISIONS :2205 onward"; awk 'NR>=2205 && NR<2260' DECISIONS.md | awk '/D-2026-11-12-B/ && NR>1{exit} {print NR+2204": "$0}'
2280:## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, first pass only (Mac-side Python event simulator on the 1-minute file; master under D-2026-11-08-D D1)
2287:$ git show HEAD:DECISIONS.md | grep -c 'D-2026-11-12-B'
--- DECISIONS :2205 onward
2205: ## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Rule F2-1 (rubric F2; master under D-2026-11-08-D D1)
2206: 
2207: **Status:** Decided by master under D-2026-11-08-D D1, changeable by Amear. Not Amear's ruling. A spec amendment only: nothing is built.
2208: **Authority:** DECISION_LOG.md:854 (row 2026-11-12T05:29:00Z, WHO: praxis-master, unit `2026-11-12-f2-breaker-amendment`, Unit F2B); at filing that row sits in the working copy, after the 851 lines of DECISION_LOG.md at HEAD `9905804`. Rule F2-1's approval: D-2026-11-11-A, V2 (DECISIONS.md:2108–2116). D1: `specs/SPEC_RUBRIC.md`:437–442. Every quotation in this entry is copied by script, byte-identical to the cited line or to the stated part of it. The row's item (1), copied by script from DECISION_LOG.md:854:
2209: 
2210: ```text
2211: (1) the proposal's #4/#5 replacement text is adopted as the amended breaker spec, matching Rule F2-1; this is not D2(c) — no account exists and no real money is at stake (D-2026-11-11-A: Amear has no MFFU account; consumer Sim-only guard);
2212: ```
2213: 
2214: Its item (2), copied by script from the same line:
2215: 
2216: ```text
2217: (2) the Phase 3 spec is a faithful import, so its body lines :100–101 are NOT rewritten; the amendment is an appended, labelled amendment section plus at most one pointer line, and a new DECISIONS.md entry D-2026-11-12-A written BEFORE the spec edit (S4) records the adoption and names the governing rule and the 15:00 disposition;
2218: ```
2219: 
2220: **The governing rule: Rule F2-1.** Copied by script from `docs/specs/2026-11-10-f2-session-flat-proposal.md`:20 (called the proposal below):
2221: 
2222: ```text
2223: **Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system position is submitted no later than 16:00:00 ET (or no later than the exchange's early close on an early-close day), and the position must be confirmed flat before MFFU's 4:10 PM ET auto-close. The system opens no new position from that flat time until 18:00 ET, when the next session begins.**
2224: ```
2225: 
2226: **The 15:00 disposition.** Copied by script from proposal :30 (the whole line; its first two sentences are the ones D-2026-11-11-A quotes at DECISIONS.md:2114):
2227: 
2228: ```text
2229: **On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:00. (On an early-close day whose close is at or before 15:00, Rule F2-1 has already flattened it and no system position is open at 15:00.) It is managed by its own strategy's exits (for the Noise-Area: the band / VWAP trailing stop and reverse rule) and by the always-on breakers #1, #6 and #7, and its closing order is sent no later than 16:00:00 ET by Rule F2-1 (the strategy's own flat, backed by breaker #4), flat before 16:10 ET. New system entries between 15:00 and 16:00 are allowed under Rule F2-1, subject to breakers #1, #2, #3, #6, #7, #8 and #9. Between 15:00 and 18:00 ET Amear's own manual interaction is locked out (R8 KEEP, breaker #5 below).
2230: ```
2231: 
2232: **The amended breaker text.** The proposal's replacement text for breakers #4 and #5 is adopted as the amended breaker spec. Copied by script from proposal :36 and :38:
2233: 
2234: ```text
2235: > 4. Session flat gate — clock reaches 16:00:00 ET, or the exchange's early close on an early-close day if earlier → cancel working entry orders, send market orders closing all system positions, confirm flat before 4:10 PM ET (alert if not), and refuse new system entries until the next session opens at 18:00 ET.
2236: 
2237: > 5. Session window (operator lockout) — clock is in 3:00–6:00 PM ET → lock out manual order entry and manual changes to the system by the operator. The system's own trading is not disabled by this breaker; the system's no-entry period 16:00–18:00 ET is enforced by breaker #4.
2238: ```
2239: 
2240: They supersede the Phase 3 import's lines :100 and :101 (`docs/specs/2026-11-05-phase3-build-specification.md`), copied by script:
2241: 
2242: ```text
2243: 4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
2244: 5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
2245: ```
2246: 
2247: The Phase 3 spec is a faithful import, so :100 and :101 are not rewritten. The amendment is a labelled section appended at the end of that file ("Amendment 1 — 2026-11-12 — breakers #4 and #5 (Rule F2-1; D-2026-11-12-A)") No pointer line is added inside the body: a line there would shift the body's line numbers after :106, which other specs cite (topology doc :24, :61, :89; proposal :67). This entry is written to disk before that spec edit (S4).
2248: 
2249: **Why this is the master's decision, changeable by Amear.** Amear's approval (D-2026-11-11-A, V2) was given on the words put to him, "flat by 16:00 ET governs; a position open at 15:00 may stay open until 16:00; no new system entries 16:00–18:00 ET." (as copied at DECISIONS.md:2108). That entry records, copied by script from DECISIONS.md:2108: "The amended #4/#5 text does not exist" and "Whether his approval reaches the elements (a)–(f) listed below, which were not put to him in those words, is not graded here." Its element (f), copied by script from DECISIONS.md:2116: "(f) the proposed replacement text for breakers #4 and #5 (proposal :36, :38)." So his approval reached Rule F2-1 as summarised, and whether it reaches element (f) is ungraded. This entry does not read his approval as reaching (f). The adoption of the #4/#5 text is the master's, under D1, and Amear may change it. The master's reading (not graded by anyone else): the adopted text keeps the three parts of the summary — #4 flattens by 16:00 ET and refuses new system entries until 18:00 ET; #5 no longer disables the system's own trading, so a position open at 15:00 may stay open until 16:00.
2250: 
2251: **Not D2(c).** D2, copied by script from `specs/SPEC_RUBRIC.md`:443–447:
2252: 
2253: ```text
2254: D2  Only four things stop and wait for Amear's word: (a) spending
2255:     money; (b) switching live trading on, or any order path to a
2256:     funded account; (c) changing circuit-breaker values while real
2257:     money is at stake; (d) installing keys, credentials or agent
2258:     permissions. Everything else is D1.
2259: ```
````

### C2g — proposal :24, :40, :75–78; topology body lines that place #5

```
$ cd /Volumes/Sensidine/Praxis.build && P=docs/specs/2026-11-10-f2-session-flat-proposal.md; git show HEAD:$P | sed -n '24p' | grep -o 'Strategies may flat earlier than 16:00 by their own rules'; git show HEAD:$P | sed -n '40p'; git show HEAD:$P | sed -n '75,78p' | cut -c1-20; echo "--- topology body lines mentioning #5 or 4/5 or window"; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n '#5\|#4/#5\|#4, #5\|, 5\b\|window\|all nine' | cut -c1-230
Strategies may flat earlier than 16:00 by their own rules
Placement of both on the live path is in `docs/specs/2026-11-10-live-signal-topology.md`, section 3. That table places #5 as the Phase 3 text stands (a system entry block in the window) and states what changes under this proposal: if adopted, the system window check is removed and only the operator lockout remains. That document notes that #5's operator lockout cannot sit on the signal path, because manual orders never pass n8n (its bypass B3, OPEN-T8).
| OPEN-F2-1 | Backte
| OPEN-F2-2 | R6 var
| OPEN-F2-3 | Early-
| OPEN-F2-4 | Whethe
--- topology body lines mentioning #5 or 4/5 or window
41:Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → Write Signal File → outbox → sweep daemon → drop dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8
48:**What changes from the Block 1 architecture.** The emitter is NT8, not TradingView (CLAUDE.md "Signal flow: TradingView alert → webhook → …"). Deviation G's public-ingress question stops being on the anchor strategy's live pat
62:| 5 | Afternoon session window | As the Phase 3 text stands: an n8n gate node before Write Signal File plus the same consumer clock check as #4, refusing every system entry (including Noise-Area reversals) in the window. Under 
74:| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before the file write; #7/#8/#9 also in the consumer | emitter strategy; VM → n8n reach (OPEN-T1); EXIT/FLATTEN instruction types; consum
78:Option 3 has the fewest unbuilt parts, because NT8 already holds account P&L, position and clock. The decision rule puts the Phase 3 placement first unless the evidence shows the signal cannot pass through n8n, and it does not 
86:| B1 | A JSON file written straight into the drop dir `/Users/admin/praxis-signals`, into `incoming/`, or into the n8n outbox, by anything that can write as `admin`, or through any share that exposes the drop dir to the VM. D-2
88:| B3 | Manual orders typed into NT8, Rithmic or the MFFU platform. | No, never. | Nothing on this path can gate a human order. R8's KEPT half of #5 (lockout on Amear's own interaction) needs a separate mechanism, not designed h
112:This topology touches: Block 1 (the emitter changes from TradingView to NT8; the TESTED pipe is reused; Deviation G's ingress question leaves the anchor's live path); Block 2 (the emitter must reproduce the backtest strategy's
```

(Each line is cut at 230 characters by the command's own `cut -c1-230`. The full text of :78 and :86 is in the note's byte-identical blocks, checked in C1c.)

The note covers every topology body line that places #5 as a system check: :41, :48, :62, :74, :78 and :86 (E-7 pastes the matching fragment of each). :88 already keeps #5's lockout off the path, and :112 names only "rubric F2 (... #4/#5)". Neither needs a reading.

### C2h — other topology and ruleset lines that could be stale

```
$ cd /Volumes/Sensidine/Praxis.build && echo "--- topology body: 11:30|15:00|3:00|16:00|FROZEN|PROPOSED|F2"; git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | grep -n '11:30\|15:00\|3:00\|16:00\|FROZEN\|PROPOSED\|F2' | cut -c1-14; echo "--- ruleset body: 11:30|window"; git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | grep -n '11:30\|window' | cut -c1-160
--- topology body: 11:30|15:00|3:00|16:00|FROZEN|PROPOSED|F2
4:Unit: 2026-1
20:| 1.4 | R6 
58:| 1 | Daily
59:| 2 | Max t
61:| 4 | Sessi
62:| 5 | After
63:| 6 | Trail
101:| OPEN-T4 
105:| OPEN-T8 
112:This topol
--- ruleset body: 11:30|window
8:> **Scope note.** The paper studies **SPY** (the ETF), NOT NQ futures, and trades **all day** (every half-hour, flat at the 16:00 cash close). PRAXIS applies 
31:- **Lookback window:** **14 trading days**, fixed (`i = [1,14]`). No lookback grid is tested in the paper.
79:| D8 | Flat time | **16:00** — no 11:30 stop in paper | b2-q1 report notes a **"flat-by-11:30-ET baseline"** | ❌ **CONFLICT** — 11:30 is a **PRAXIS window ch
84:**Net:** The RTF prose is a faithful summary of the paper on band/gap/sizing/16:00-flat, but three PRAXIS framings are **NOT paper-derived and need trader de
99:Other implementation facts to hard-code (not optimize): checkpoints at `HH:00`/`HH:30`; `ref = max/min(Open_{9:30}, PrevClose)`; VWAP anchored at 09:30, mark
105:- **T1 (highest priority): session-flat time — 16:00 (paper) vs 11:30 (PRAXIS window).** The paper's entire performance record is full-day-to-16:00. A 09:30
```

```
$ cd /Volumes/Sensidine/Praxis.build && git show HEAD:docs/specs/2026-11-10-live-signal-topology.md | sed -n '4p;20p;101p;105p' | cut -c1-700
Unit: 2026-11-10-f1-f2-proposal (authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z, praxis-master, item (2)). Bead context: `Praxis_build-2nh`.
| 1.4 | R6 Pre-Announcement Drift, evening entry | A PROPOSED research design on branch `r6/announcement-research` (`bf6fcc7`); no strategy code. | SPECIFIED | [E15] |
| OPEN-T4 | Breaker values: #1 threshold, #2 max, #6 margin, #7 plan size, #8 X seconds. | A later PROPOSED values unit (R8, A6). Changing values while real money is at stake **waits for Amear (D2(c))**; today none is. |
| OPEN-T8 | How R8's lockout on Amear's own interaction 15:00–18:00 is enforced, since manual orders never pass n8n (B3). | Block 3 design under D1; it binds Amear's own conduct, so he may overrule it. |
```

Topology :105 is OPEN-T8, as the note cites. In the ruleset, only :31 is outside the note's set, and :31 is the lookback window, which has nothing to do with the session. The other five lines the grep finds are :8, :79, :84, :99 and :105, and the note covers all five (C1c). This report does not paste follow-up F-3's own text, so it does not grade F-3's list against them.

### C3a — proposal line 95 at first read: invalid UTF-8 (attack 2, citation for F-7)

````
$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-f2-session-flat-proposal.md; git show HEAD:$f | python3 -I -c 'import sys; sys.stdin.buffer.read().decode("utf-8"); print("HEAD valid utf-8")'; python3 -I -c '
import sys
b=open(sys.argv[1],"rb").read()
bad=[]
i=0
while i<len(b):
    try:
        b[i:].decode("utf-8"); break
    except UnicodeDecodeError as e:
        bad.append(i+e.start); i=i+e.start+1
print("invalid byte offsets:",bad)
for o in bad:
    ln=b[:o].count(b"\n")+1
    print("offset",o,"line",ln,"bytes around:",b[o-12:o+6].hex(" "))
' $f; grep -n 'SPEC_RUBRIC.md`:' $f | cut -c1-60 | od -c | sed -n 1,12p
HEAD valid utf-8
invalid byte offsets: [13567, 13568]
offset 13567 line 95 bytes around: 5f 52 55 42 52 49 43 2e 6d 64 60 3a 80 93 39 34 20 61
offset 13568 line 95 bytes around: 52 55 42 52 49 43 2e 6d 64 60 3a 80 93 39 34 20 61 74
````

At that read, the F-7 citation was `` `specs/SPEC_RUBRIC.md`: `` followed by bytes `80 93` and then `94` (the python output above). The digits "93" and the en-dash lead byte `e2` were missing, so the line number F-7 exists to fix was unreadable, and the file was not valid UTF-8. The command's last segment, the `grep`/`od -c`/`sed -n 1,12p` pipe, has no output in the paste above; that output was not kept. Its re-run (E-1) shows the repaired file only, not the pre-repair bytes, and its 12-row `od` window ends inside line 92, before line 95. A first quote-script run on this file is not evidenced here: its error output was not kept, and it is not reproducible after the repair.

### C3b — the same line after the concurrent edit, plus mtimes

```
$ cd /Volumes/Sensidine/Praxis.build && grep -n 'D-2026-11-12-A adopts that text' docs/specs/2026-11-10-live-signal-topology.md | cut -c1-12; grep -n 'cannot sit in the strategy either' docs/specs/2026-11-10-live-signal-topology.md | cut -c1-12; LC_ALL=C grep -n 'OPEN-F2-5 is closed' docs/specs/2026-11-10-f2-session-flat-proposal.md | cut -c1-40; grep -n 'whether A6 is triggered is not graded here' DECISIONS.md | cut -c1-8; grep -n 'is not graded here." Its element (f)' DECISIONS.md | cut -c1-8; grep -n 'the topology document, the walk-forward spec' DECISIONS.md | cut -c1-8; python3 -I -c 'import sys
for f in sys.argv[1:]:
    try: open(f,"rb").read().decode("utf-8"); print(f,"valid utf-8")
    except UnicodeDecodeError as e: print(f,"INVALID utf-8 at",e.start)' docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md MANIFEST.md
136:Aligned 
184:Aligned 
103:Aligned reading: OPEN-F2-5 is closed
2129:DEC
2272:Thi
2249:**W
2274:**W
docs/specs/2026-11-10-live-signal-topology.md valid utf-8
docs/specs/2026-07-16-b2-noise-area-ruleset.md valid utf-8
docs/specs/2026-11-10-f2-session-flat-proposal.md valid utf-8
MANIFEST.md valid utf-8
```

```
$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-f2-session-flat-proposal.md; ls -l -D '%Y-%m-%dT%H:%M:%S' $f; date '+%Y-%m-%dT%H:%M:%S'; sed -n '95p' $f | grep -o 'SPEC_RUBRIC.md`:[^ ]* at HEAD' | od -c | head -4; git diff HEAD --numstat -- $f; python3 -I /tmp/fgdchk/quotes.py 2>&1 | grep proposal; sed -n '2272p' DECISIONS.md | grep -o 'whether A6 is triggered is not graded here'
-rw-r--r--@ 1 admin  staff  15219 2026-11-12T08:12:44 docs/specs/2026-11-10-f2-session-flat-proposal.md
2026-11-12T08:14:47
0000000    S   P   E   C   _   R   U   B   R   I   C   .   m   d   `   :
0000020    9   3   –  **  **   9   4       a   t       H   E   A   D  \n
0000040
30	0	docs/specs/2026-11-10-f2-session-flat-proposal.md
2026-11-10-f2-session-flat-proposal.md cited :8 block-at-note-line 92 byte-identical=True
2026-11-10-f2-session-flat-proposal.md cited :79 block-at-note-line 100 byte-identical=True
2026-11-10-f2-session-flat-proposal.md cited :3 block-at-note-line 108 byte-identical=True
whether A6 is triggered is not graded here
```

```
$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-f2-session-flat-proposal.md; head -n 81 $f | cmp - <(git show HEAD:$f) && echo "proposal body 1-81 BYTE-IDENTICAL"; echo "removed: $(git diff HEAD -- $f | grep '^-' | grep -vc '^--- a/')"; sed -n '95p' $f; for g in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md; do ls -l -D '%Y-%m-%dT%H:%M:%S' $g | awk '{print $6, $7}'; done
proposal body 1-81 BYTE-IDENTICAL
removed: 0
Aligned reading: the F2 unblock clause quoted here is at `specs/SPEC_RUBRIC.md`:93–94 at HEAD `006a08b`, inside the section "### F2 — Session-flat time vs. breakers #4 and #5" (:81), which now sits under "## PASSED — closed criteria". It was at :30–31 at `e3323a8` (D-2026-11-12-A); the rubric change at `c29d08b` moved F2 into PASSED. The quoted words are unchanged. The second citation on this line, DECISIONS.md:1744–1745 (A6), is unchanged. The line's "changes no rubric state" is true of this file; rubric F2's state was moved at `c29d08b`, not by this file.
2026-11-12T08:10:48 docs/specs/2026-11-10-live-signal-topology.md
2026-11-12T08:10:48 docs/specs/2026-07-16-b2-noise-area-ruleset.md
```

After the edit, line 95 reads `:93–94` and matches C2d. The MANIFEST row for this path also says 93–94 (C6).

### C4 — F1: nine breaker names (attack 5)

```
$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-live-signal-topology.md; for n in "Daily loss limit" "Max trades per day" "Consecutive loss" "Session time gate" "Afternoon session window" "Trailing drawdown proximity" "Max position size" "Stale signal filter" "Heartbeat dead-man switch" "Session flat gate" "Session window (operator lockout)"; do printf '%-36s body(HEAD 1-114)=%s  note(115-end)=%s\n' "$n" "$(git show HEAD:$f | grep -cF "$n")" "$(sed -n '115,$p' $f | grep -cF "$n")"; done; echo "--- MANIFEST 440-450"; sed -n '440,450p' MANIFEST.md | cut -c1-260
Daily loss limit                     body(HEAD 1-114)=1  note(115-end)=0
Max trades per day                   body(HEAD 1-114)=1  note(115-end)=0
Consecutive loss                     body(HEAD 1-114)=1  note(115-end)=0
Session time gate                    body(HEAD 1-114)=1  note(115-end)=2
Afternoon session window             body(HEAD 1-114)=1  note(115-end)=2
Trailing drawdown proximity          body(HEAD 1-114)=1  note(115-end)=0
Max position size                    body(HEAD 1-114)=1  note(115-end)=0
Stale signal filter                  body(HEAD 1-114)=2  note(115-end)=0
Heartbeat dead-man switch            body(HEAD 1-114)=1  note(115-end)=0
Session flat gate                    body(HEAD 1-114)=0  note(115-end)=3
Session window (operator lockout)    body(HEAD 1-114)=0  note(115-end)=3
--- MANIFEST 440-450
| /docs/reports/2026-11-12-r6-engine-entry-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-r6-engine-entry (DECISION_LOG 2026-11-12T09:03:23Z item (c)): files D-2026-11-12-B (R6 step 2 engine authorised, first pass only: Mac-side Pyth
| /docs/reports/2026-11-12-r6-engine-entry-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-r6-engine-entry: quote, line-citation, invented-number, hold-time and S2/S4/S8/S13 check of D-2026-11-12-B; ungraded at time of ro
| /docs/reports/2026-11-12-r6-engine-entry-worker2.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 2 report for unit 2026-11-12-r6-engine-entry: narrow re-check of the cures to worker 1's findings in D-2026-11-12-B; ungraded at time of row |
| /DECISIONS.md | Log | 3 | 2026-11-12 | MODIFIED (unit 2026-11-12-r6-engine-entry; master under D-2026-11-08-D D1, DECISION_LOG rows 2026-11-12T09:03:23Z and 09:25:24Z): entry D-2026-11-12-B (R6 step 2 backtest engine authorised, first pass only: Mac-side Pyt
| /docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-r6-engine-entry-correction-1: S1 cure for the three audit findings on docs/reports/2026-11-12-r6-engine-entry-manager.md (:24, :72
| /docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-r6-engine-entry-correction-1: re-run of every command in the correction manager report against its pasted output, and
| /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to row 353 for this path). Unit 2026-11-12-fgd-doc-alignment (bead Praxis_build-fgd part A; master under D-2026-11-08-D D1, carries out D-2026
| /docs/specs/2026-07-16-b2-noise-area-ruleset.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (no earlier row for this path found by grep in this file). Unit 2026-11-12-fgd-doc-alignment (bead Praxis_build-fgd part A; master under D-2026-11-08-D D1): section "Amen
| /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-12 | AMENDMENT ROW (append-only registry — adds to row 354 for this path). Unit 2026-11-12-fgd-doc-alignment (bead Praxis_build-fgd part A; master under D-2026-11-08-D D1): section "Amen
| /docs/reports/2026-11-12-fgd-doc-alignment-manager.md | Report | 3 | 2026-11-12 | Manager report for unit 2026-11-12-fgd-doc-alignment (bead Praxis_build-fgd part A): per-follow-up disposition of F-1, F-2, F-3, F-7, F-9, additions-only proof, F1 nine-name ch
| /docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | Report | 3 | 2026-11-12 | ADVERSARIAL worker 1 report for unit 2026-11-12-fgd-doc-alignment: check of the three appended amendment notes against D-2026-11-12-A, Amendment 1 and the cited body lines; ung
```

Attack 5: PASS. The body still names all nine Phase 3 :97–105 names, each at least once. The note adds both amended names three times each; whole-file counts in C1c are 3 and 3. The body's lone "Consecutive loss" hit matches the Phase 3 name's prefix, which is how the grep was written.

### C5 — de-identification of the appended text (attack 6)

The pattern script is `/tmp/fgdchk/deid.py`. Its terms are not reproduced here. It scans only the appended lines of each file: topology from line 115, ruleset from 112, proposal from 82 (offsets 114, 111, 81 and the slice `[n:]`, E-6).

```
$ python3 -I /tmp/fgdchk/deid.py
2026-11-10-live-signal-topology.md: email-address = 0
2026-11-10-live-signal-topology.md: trader-surname = 0
2026-11-10-live-signal-topology.md: support-agent-first-name = 0
2026-11-10-live-signal-topology.md: paper-author-surnames = 0
2026-11-10-live-signal-topology.md: other-known-names = 0
2026-11-10-live-signal-topology.md: medication-brands = 0
2026-11-10-live-signal-topology.md: medication-generic-words = 0
2026-11-10-live-signal-topology.md: distinct capitalised words = 50
2026-07-16-b2-noise-area-ruleset.md: email-address = 0
2026-07-16-b2-noise-area-ruleset.md: trader-surname = 0
2026-07-16-b2-noise-area-ruleset.md: support-agent-first-name = 0
2026-07-16-b2-noise-area-ruleset.md: paper-author-surnames = 0
2026-07-16-b2-noise-area-ruleset.md: other-known-names = 0
2026-07-16-b2-noise-area-ruleset.md: medication-brands = 0
2026-07-16-b2-noise-area-ruleset.md: medication-generic-words = 0
2026-07-16-b2-noise-area-ruleset.md: distinct capitalised words = 33
2026-11-10-f2-session-flat-proposal.md: email-address = 0
2026-11-10-f2-session-flat-proposal.md: trader-surname = 0
2026-11-10-f2-session-flat-proposal.md: support-agent-first-name = 0
2026-11-10-f2-session-flat-proposal.md: paper-author-surnames = 0
2026-11-10-f2-session-flat-proposal.md: other-known-names = 0
2026-11-10-f2-session-flat-proposal.md: medication-brands = 0
2026-11-10-f2-session-flat-proposal.md: medication-generic-words = 0
2026-11-10-f2-session-flat-proposal.md: distinct capitalised words = 22
TOTAL hits = 0
```

The C1c re-run on the current files again printed `TOTAL hits = 0`. Next, the capitalised words in the appended text, to catch person names the pattern list does not hold:

```
$ cd /Volumes/Sensidine/Praxis.build && bash -c 'for p in "docs/specs/2026-11-10-live-signal-topology.md 115" "docs/specs/2026-07-16-b2-noise-area-ruleset.md 112" "docs/specs/2026-11-10-f2-session-flat-proposal.md 82"; do set -- $p; tail -n +$2 $1 | LC_ALL=C grep -oE "\b[A-Z][a-z]{2,}\b" | sort -u | tr "\n" " "; echo; done'
Added Afternoon Aligned Amear Amended Amendment Area Block Body Both Breakers Depends Deviation Each Every File Governing Its Level Names Noise Not Open Option Path Phase Read Redis Rithmic Rubric Rule Same Session Signal Since System That The This Two Unchanged Under Unit Upstream Users What Where Whether Write Yes 
Added Aligned Amear Amendment Area Block Body Each Entry Every Flat Items Its Level Net Noise Not Open Other Resolves Rule Scope Sharpe Strategies The This Trader Two Unchanged Unit What Whether Yes 
Added Adoption Aligned Amear Amendment Body Each Level Limits Phase Read Rubric Rule Session Status That The This Unchanged Under Unit What
```

The only person name is Amear. "Sharpe" is the ratio, inside the quoted body line :105 (E-7), and is not a paper author. "Users" is the `/Users/admin` path, inside the quoted body line :86. Attack 6: PASS.

### C6 — MANIFEST row references

```
$ cd /Volumes/Sensidine/Praxis.build && grep -n 'live-signal-topology.md |\|f2-session-flat-proposal.md |\|b2-noise-area-ruleset' MANIFEST.md | cut -c1-90; echo "--- full row 446-448 tails"; for n in 446 447 448; do sed -n "${n}p" MANIFEST.md | cut -c260-900; echo; done
353:| /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-10 | F1 live-sig
354:| /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-10 | F2 sess
446:| /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-12 | AMENDMENT R
447:| /docs/specs/2026-07-16-b2-noise-area-ruleset.md | Spec | 3 | 2026-11-12 | AMENDMENT 
448:| /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-12 | AMENDME
--- full row 446-448 tails
6-11-12-A): section "Amendment note — 2026-11-12 (D-2026-11-12-A alignment)" appended after line 114; body lines 1–114 unchanged. Aligned readings for :41, :48, :54, :61, :62, :74, :78, :86 (follow-ups F-1, F-2); OPEN-A1; F1 bearing stated, not graded. Breakers SPECIFIED ONLY |

ndment note — 2026-11-12 (D-2026-11-12-A alignment)" appended after line 111; body lines 1–111 unchanged. Aligned readings for :8, :79, :84, :99, :105 (follow-up F-3: 09:30–11:30 window and the 11:30 option) under the 2026-07-16T19:29Z lock item (1) and D-2026-11-12-A; OPEN-A2 (strategy-level 11:30 stop for a later arm, two readings, not chosen) |

ndment note — 2026-11-12 (D-2026-11-12-A alignment)" appended after line 81; body lines 1–81 unchanged. F-7: :8 rubric citation re-pointed to specs/SPEC_RUBRIC.md:93–94 at 006a08b; F-9: OPEN-F2-5 (:79) closed with D-2026-11-12-A's limits carried; :3 status read as historical |
```

The row cross-references are correct: 353 and 354 exist, and the grep finds no earlier ruleset row.

### C7 — S13 scope and footer position

```
$ cd /Volumes/Sensidine/Praxis.build && grep -n '^S13\|^\*\*S13\|S13 ' specs/SPEC_RUBRIC.md | head -3; awk '/S13/{f=1} f{print NR": "$0; c++} c>=8{exit}' specs/SPEC_RUBRIC.md | cut -c1-200; echo "--- last lines of each file"; for f in docs/specs/2026-11-10-live-signal-topology.md docs/specs/2026-07-16-b2-noise-area-ruleset.md docs/specs/2026-11-10-f2-session-flat-proposal.md; do echo "$f last: $(tail -n1 $f | cut -c1-80)"; echo "footer count: $(grep -c '^Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.$' $f)"; done; sed -n '1551p' DECISIONS.md | cut -c1-60
139:| S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." Reports with no such figure carry it too, as house style, until the void clause of D-2026-10-30-A fires. Settled under R-1104-2 on 2026-11-06 (D-2026-11-06-B item 5); source: the flush auditor's finding that the rule was written nowhere (DECISION_LOG 2026-11-06T15:19:51Z). |
139: | S13 | Every report under docs/reports/ and every DECISIONS.md entry that states a backtest or P&L figure carries, once, the standing limitation sentence: "Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed." Reports with no such figure carry it too, as house style, until the void clause of D-2026-10-30-A fires. Settled under R-1104-2 on 2026-11-06 (D-2026-11-06-B item 5); source: the flush auditor's finding that the rule was written nowhere (DECISION_LOG 2026-11-06T15:19:51Z). |
140: 
141: **S6 is the one that failed.** Six deviations were each approved in isolation
142: and four downstream components broke without anyone noticing. Every future
143: deviation gets graded against S6 explicitly, by name, in the report.
144: 
145: **S9 was referenced before it was written.** The 2026-07-26 brief carried
146: "S9 applies to everything in this brief" as a standing rule, but no S9 existed
--- last lines of each file
docs/specs/2026-11-10-live-signal-topology.md last: **F1 bearing (not a grade).** Rubric F1 (PASSED@b4c3291) asks that this document
footer count: 1
docs/specs/2026-07-16-b2-noise-area-ruleset.md last: | OPEN-A2 | Whether a strategy-level stop at 11:30 (a strategy rule, not a break
footer count: 0
docs/specs/2026-11-10-f2-session-flat-proposal.md last: That status is historical: Rule F2-1 is adopted (D-2026-11-12-A) and rubric F2 i
footer count: 1
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) a
```


S13 covers reports and DECISIONS.md entries, not specs. The footer still appears once in the topology and the proposal, now in the middle of each file (body :114 and :81). Not a finding.

## Attack-by-attack result

1. Additions only: **PASS** (C1a, C1b, C1c).
2. Quoted old lines: **PASS**, 16/16 byte-identical, plus Phase 3 :212/:224 (C1c, C2b). Other citations checked and correct: DECISIONS.md:2205, :2108, :1551, :1744–1745 (C2e, C2f); Phase 3 :212, :224 (C2c); SPEC_RUBRIC.md :93–94, :81, :30–31@e3323a8 (C2d); DECISION_LOG.md:42 (C2d); proposal :24, :20, :30 (C2g, E-3); topology :105 (C2h). The F-7 citation was broken at first read (Finding 1) and is now correct.
3. Support and design choices: no unsourced design choice in the placement readings. OPEN-A1 and OPEN-A2 leave both readings unchosen. Two MINOR over-statements (Findings 2, 3). No #5-as-system-check line is missed (C2g).
4. S2: breakers are stated SPECIFIED ONLY in all three notes. The OPEN-F2-5 "closed" lead is stronger than D-2026-11-12-A's limits (Finding 4, MINOR; the limits are disclosed in the same paragraph).
5. F1 names: **PASS** (C4).
6. De-identification: **PASS** (C5).

## Findings

1. **MAJOR (observed at first read; cured in the working tree at mtime 2026-11-12T08:12:44, while this review ran).** Proposal note line 95, the F-7 citation. At first read it was `` `specs/SPEC_RUBRIC.md`: `` + bytes `80 93` + `94`: invalid UTF-8, with "93" and the en-dash lead byte missing (C3a). F-7's whole purpose is this line number, so the follow-up was misstated, and the public file would have rendered replacement characters. The current file reads `:93–94` and is valid UTF-8 (C3b). Fix already applied by someone else. Suggestion: before staging, re-run `python3 -I -c 'open("docs/specs/2026-11-10-f2-session-flat-proposal.md","rb").read().decode("utf-8")'`, then cmp line 95 against the MANIFEST row 448 text. I did not make this edit, and I do not know who did.
2. **MINOR — topology :136 in the graded version, sha1 `5aea715d2ff4` (aligned reading for :41; source line in E-2).** "...('the n8n/consumer window check is then removed'); D-2026-11-12-A adopts that text." Read naturally, "that text" is the topology :62 row text (E-7). D-2026-11-12-A adopts something else, "The proposal's replacement text for breakers #4 and #5" (DECISIONS.md:2232). The same entry also says the topology document is not edited (:2274). Removing the check follows from the adopted #5 text, through proposal :40. Fix: "D-2026-11-12-A adopts the proposal's #4/#5 replacement text (DECISIONS.md:2232); proposal :40 states that, if adopted, the system window check is removed."
3. **MINOR — topology :184 in the graded version, sha1 `5aea715d2ff4` (aligned reading for :78; source line in E-2).** "its operator lockout cannot sit in the strategy either (B3, OPEN-T8)." B3 (:88) says "Nothing on this path can gate a human order", and "this path" is option 1's (E-9). OPEN-T8 (:105) leaves the enforcement open ("Block 3 design under D1"), and D-2026-11-12-A does not decide it (:2274). Ruling out a strategy-resident lockout narrows OPEN-T8 without a source. Fix: "#5 has no system check to move; where its operator lockout sits, including whether the strategy could carry it, is OPEN-T8 (:105)."
4. **MINOR — proposal :103 in the graded version, sha1 `e1d2d72895b3` (F-9; source line in E-2).** The note opens "OPEN-F2-5 is closed." without qualification. The item's decider is "Amear's approval under A6; then ... the amended #4/#5 text". D-2026-11-12-A records that "whether A6 is triggered is not graded here" (DECISIONS.md:2272). It also records that whether his approval reaches element (f), the #4/#5 text, is ungraded (:2249). The note carries both limits in the same paragraph, so this is not a false claim, but the lead sentence states the result at a higher level than its own caveats. Fix: "OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits:"
5. **MINOR (process) — the artifact changed during adversarial review.** Topology and ruleset mtime 2026-11-12T08:10:48; proposal 08:12:44 (C3b). My first reads came before at least the proposal edit (C3a and C3b differ). I re-ran the C1c checks at 08:15:12 (C1c). The grade binds only to sha1 prefixes topology `5aea715d2ff4`, ruleset `b68c098f4aa1`, proposal `e1d2d72895b3`. Fix: the manager should confirm the staged blobs match these hashes, or send any later edit for a fresh check. At correction-1 the topology and proposal are `5865a1121cd1` and `24598c3d73d8` and the ruleset is unchanged (E-2), so this grade does not cover the current topology and proposal.

Standing MAJOR findings on the current files: 0. MAJOR observed and since cured: 1. MINOR: 4.

The verdict below holds only for the hashes in Finding 5. If the staged blobs differ, it does not hold.

Verdict: PASS

## Correction-1 re-run evidence (2026-11-12)

Re-run 2026-11-12 by correction-1 (unit `2026-11-12-fgd-doc-alignment-correction-1`). One script, `/tmp/fgdc1/ev-worker1.sh`, run under bash; its output is pasted verbatim below. Every block reads the files as they are now, not as they were during the review: E-1 shows the repaired proposal, not the pre-repair bytes. E-2 rebuilds the graded topology and proposal and matches their sha1 prefixes before quoting from them. This block was run before correction-1 appended its two MANIFEST.md rows (:452–453); a fresh run now differs only in the timestamp line and the MANIFEST.md hunk header (`+440,12` becomes `+440,14`), shown in C8 of `docs/reports/2026-11-12-fgd-doc-alignment-correction-1-manager.md`.

````
re-run 2026-11-12 by correction-1, 2026-11-12T08:44:16, HEAD 006a08b, shell bash

### E-1 (C3a command, literal, re-run on the REPAIRED file: post-repair state, not the pre-repair bytes)
$ cd /Volumes/Sensidine/Praxis.build && f=docs/specs/2026-11-10-f2-session-flat-proposal.md; git show HEAD:$f | python3 -I -c 'import sys; sys.stdin.buffer.read().decode("utf-8"); print("HEAD valid utf-8")'; python3 -I -c '
import sys
b=open(sys.argv[1],"rb").read()
bad=[]
i=0
while i<len(b):
    try:
        b[i:].decode("utf-8"); break
    except UnicodeDecodeError as e:
        bad.append(i+e.start); i=i+e.start+1
print("invalid byte offsets:",bad)
for o in bad:
    ln=b[:o].count(b"\n")+1
    print("offset",o,"line",ln,"bytes around:",b[o-12:o+6].hex(" "))
' $f; grep -n 'SPEC_RUBRIC.md`:' $f | cut -c1-60 | od -c | sed -n 1,12p
HEAD valid utf-8
invalid byte offsets: []
0000000    8   :   T   h   i   s       f   i   l   e       i   s       a
0000020        p   r   o   p   o   s   a   l       o   n   l   y   .    
0000040    I   t       w   r   i   t   e   s       n   o       D   E   C
0000060    I   S   I   O   N   S   .   m   d       e   n  \n   6   1   :
0000100    |       B   l   o   c   k       4       p   a   r   i   t   y
0000120        g   a   t   e       (   r   u   b   r   i   c       O   4
0000140    ,       `   s   p   e   c   s   /   S   P   E   C   _   R   U
0000160    B   R   I   C   .   m   d   `   :  \n   6   9   :   |       R
0000200    u   b   r   i   c       F   2       "   W   h   y       f   r
0000220    o   z   e   n   "       (   `   s   p   e   c   s   /   S   P
0000240    E   C   _   R   U   B   R   I   C   .   m   d   `   :   3   7
0000260    –  **  **   4   2   )       |  \n   9   2   :   T   h   i   s
(exit 0)

### E-2 (graded versions rebuilt and hash-matched; source lines of Findings 2, 3, 4)
$ cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; P=docs/specs/2026-11-10-f2-session-flat-proposal.md; for f in $T docs/specs/2026-07-16-b2-noise-area-ruleset.md $P; do echo "current $f sha1 $(shasum $f | cut -c1-12)"; done; ls -l -D '%Y-%m-%dT%H:%M:%S' /tmp/fgd/note-topology.md | awk '{print $6, $7}'; echo "HEAD body + /tmp/fgd/note-topology.md sha1 $( (git show HEAD:$T; cat /tmp/fgd/note-topology.md) | shasum | cut -c1-12)"; (git show HEAD:$T; cat /tmp/fgd/note-topology.md) | grep -n -o '("the n8n/consumer window check is then removed"); D-2026-11-12-A adopts that text\.'; (git show HEAD:$T; cat /tmp/fgd/note-topology.md) | grep -n -o 'its operator lockout cannot sit in the strategy either (B3, OPEN-T8)\.'; echo "current proposal with the later lead-sentence edit reversed, sha1 $(sed "s/OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits\. Each step/OPEN-F2-5 is closed. Each step/" $P | shasum | cut -c1-12)"; sed "s/OPEN-F2-5 is closed on the records below, within D-2026-11-12-A's stated limits\. Each step/OPEN-F2-5 is closed. Each step/" $P | grep -n -o 'Aligned reading: OPEN-F2-5 is closed\. Each step'
current docs/specs/2026-11-10-live-signal-topology.md sha1 5865a1121cd1
current docs/specs/2026-07-16-b2-noise-area-ruleset.md sha1 b68c098f4aa1
current docs/specs/2026-11-10-f2-session-flat-proposal.md sha1 24598c3d73d8
2026-11-12T08:10:35 /tmp/fgd/note-topology.md
HEAD body + /tmp/fgd/note-topology.md sha1 5aea715d2ff4
136:("the n8n/consumer window check is then removed"); D-2026-11-12-A adopts that text.
184:its operator lockout cannot sit in the strategy either (B3, OPEN-T8).
current proposal with the later lead-sentence edit reversed, sha1 e1d2d72895b3
103:Aligned reading: OPEN-F2-5 is closed. Each step
(exit 0)

### E-3 (proposal :20 and :30; rubric F1/F2 span :63-97)
$ cd /Volumes/Sensidine/Praxis.build && P=docs/specs/2026-11-10-f2-session-flat-proposal.md; cmp <(git show HEAD:$P | sed -n 20p) <(sed -n 2223p DECISIONS.md) && echo "proposal HEAD :20 == DECISIONS.md :2223 (working tree) BYTE-IDENTICAL"; cmp <(git show HEAD:$P | sed -n 30p) <(sed -n 2229p DECISIONS.md) && echo "proposal HEAD :30 == DECISIONS.md :2229 (working tree) BYTE-IDENTICAL"; git show HEAD:$P | sed -n '20p;30p' | cut -c1-100; echo "--- rubric HEAD :63 :65 :81 :97 :99"; git show HEAD:specs/SPEC_RUBRIC.md | sed -n '63p;65p;81p;97p;99p' | cut -c1-100
proposal HEAD :20 == DECISIONS.md :2223 (working tree) BYTE-IDENTICAL
proposal HEAD :30 == DECISIONS.md :2229 (working tree) BYTE-IDENTICAL
**Rule F2-1. Deviation B's 16:00 ET session flat governs. The closing order for every open system po
**On a full trading day, at 15:00 ET an open system position stays open.** Nothing closes it at 15:0
--- rubric HEAD :63 :65 :81 :97 :99
Filer's note, not a ruling: F1 is moved here out of FROZEN. F1's own unblock clause, copied by scrip
### F1 — Signal-path topology vs. circuit-breaker placement
### F2 — Session-flat time vs. breakers #4 and #5
---
## OPEN — gradeable now
(exit 0)

### E-4 (DECISIONS.md and DECISION_LOG.md line numbers, working tree vs HEAD)
$ cd /Volumes/Sensidine/Praxis.build && git diff HEAD -U0 -- DECISIONS.md | grep '^@@'; echo "HEAD lines: $(git show HEAD:DECISIONS.md | wc -l)"; sed -n '2259,2261p' DECISIONS.md | cut -c1-60 | cat -n; for n in 2205 2232 2249 2272 2274 2280; do echo "$n: $(sed -n "${n}p" DECISIONS.md | cut -c1-70)"; done; cmp <(sed -n 42p DECISION_LOG.md) <(git show HEAD:DECISION_LOG.md | sed -n 42p) && echo "DECISION_LOG.md:42 working tree == HEAD"
@@ -2278,0 +2279,92 @@ Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippag
HEAD lines:     2278
     1	```
     2	
     3	Moving #4 from 11:30 to 16:00 and removing #5's system disab
2205: ## 2026-11-12 — D-2026-11-12-A: breakers #4 and #5 amended to match Ru
2232: **The amended breaker text.** The proposal's replacement text for brea
2249: **Why this is the master's decision, changeable by Amear.** Amear's ap
2272: This entry names the governing rule (Rule F2-1) and the 15:00 disposit
2274: **What this entry does not do.** It builds nothing: no code, no n8n wo
2280: ## 2026-11-12 — D-2026-11-12-B: R6 step 2 backtest engine authorised, 
DECISION_LOG.md:42 working tree == HEAD
(exit 0)

### E-5 (MANIFEST.md working tree, now)
$ cd /Volumes/Sensidine/Praxis.build && git diff HEAD -U0 -- MANIFEST.md | grep '^@@'; sed -n '307,314p' MANIFEST.md | cut -c1-100; for n in 353 354 446 447 448 449 450 451; do echo "$n: $(sed -n "${n}p" MANIFEST.md | cut -c1-80)"; done
@@ -306,0 +307,8 @@
@@ -431,0 +440,12 @@
| /docs/specs/2026-11-06-walk-forward-values.md | Spec | 2 | 2026-11-08 | AMENDMENT ROW (append-only
| /docs/specs/2026-11-05-walk-forward-spec.md | Spec | 3 | 2026-11-08 | AMENDMENT ROW (append-only r
| /docs/reports/2026-11-08-wf-spec-amendment-manager.md | Report | 2 | 2026-11-08 | Manager report f
| /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md | Report | 2 | 2026-11-08 | Man
| /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md | Report | 2 | 2026-11-08 | Man
| /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md | Report | 2 | 2026-11-08 | man
| /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md | Report | 2 | 2026-11-09 | Manager r
| /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch | Evidence | 2 | 2026-11-09 | Byte-exact
353: | /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-10 | F1 li
354: | /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-10 | F
446: | /docs/specs/2026-11-10-live-signal-topology.md | Spec | 3 | 2026-11-12 | AMEND
447: | /docs/specs/2026-07-16-b2-noise-area-ruleset.md | Spec | 3 | 2026-11-12 | AMEN
448: | /docs/specs/2026-11-10-f2-session-flat-proposal.md | Spec | 3 | 2026-11-12 | A
449: | /docs/reports/2026-11-12-fgd-doc-alignment-manager.md | Report | 3 | 2026-11-1
450: | /docs/reports/2026-11-12-fgd-doc-alignment-worker1.md | Report | 3 | 2026-11-1
451: | /docs/reports/2026-11-12-fgd-doc-alignment-worker2.md | Report | 3 | 2026-11-1
(exit 0)

### E-6 (the two check scripts used in C1c and C5)
$ ls -l -D '%Y-%m-%dT%H:%M:%S' /tmp/fgdchk/quotes.py /tmp/fgdchk/deid.py | awk '{print $6, $7}'; cat /tmp/fgdchk/quotes.py; echo "--- deid.py file offsets and slice"; grep -o '"docs/specs/[^"]*":[0-9]*' /tmp/fgdchk/deid.py; grep -n -o 'split("\\n")\[n:\]' /tmp/fgdchk/deid.py
2026-11-12T08:14:06 /tmp/fgdchk/deid.py
2026-11-12T08:12:21 /tmp/fgdchk/quotes.py
import re, subprocess, sys
files = {
 "docs/specs/2026-11-10-live-signal-topology.md":114,
 "docs/specs/2026-07-16-b2-noise-area-ruleset.md":111,
 "docs/specs/2026-11-10-f2-session-flat-proposal.md":81,
}
root="/Volumes/Sensidine/Praxis.build"
for f,n in files.items():
    head = subprocess.run(["git","-C",root,"show","HEAD:"+f],capture_output=True).stdout.decode().split("\n")
    cur = open(root+"/"+f,encoding="utf-8",errors="surrogateescape").read().split("\n")
    note = cur[n:]
    lastcite=None
    i=0
    while i < len(note):
        l=note[i]
        m=re.match(r"### :(\d+)",l)
        if m: lastcite=int(m.group(1))
        m2=re.search(r"Read with :(\d+)",l)
        if m2: lastcite=int(m2.group(1))
        if l=="```text":
            blk=note[i+1]
            assert note[i+2]=="```", (f,i)
            ok = blk==head[lastcite-1]
            print(f"{f.split('/')[-1]} cited :{lastcite} block-at-note-line {n+i+2} byte-identical={ok}")
            i+=3; continue
        i+=1
# Phase 3 quotes in topology note
p3 = subprocess.run(["git","-C",root,"show","HEAD:docs/specs/2026-11-05-phase3-build-specification.md"],capture_output=True).stdout.decode().split("\n")
topo = open(root+"/docs/specs/2026-11-10-live-signal-topology.md",encoding="utf-8",errors="surrogateescape").read().split("\n")
for ln,cite in ((124,212),(128,224)):
    q=topo[ln-1]
    print(f"topology line {ln} == '> '+Phase3:{cite} : {q=='> '+p3[cite-1]}")
--- deid.py file offsets and slice
"docs/specs/2026-11-10-live-signal-topology.md":114
"docs/specs/2026-07-16-b2-noise-area-ruleset.md":111
"docs/specs/2026-11-10-f2-session-flat-proposal.md":81
15:split("\n")[n:]
(exit 0)

### E-7 (topology body lines that place #5; ruleset :105 Sharpe)
$ cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; for n in 41 48 62 74 78 86; do echo "== topology HEAD :$n"; git show HEAD:$T | sed -n "${n}p" | grep -o '.\{0,60\}\(#5\|#4/#5\|all nine\|window check is then removed\).\{0,60\}' | cut -c1-160; done; echo "== ruleset HEAD :105"; git show HEAD:docs/specs/2026-07-16-b2-noise-area-ruleset.md | sed -n 105p | grep -o '.\{0,40\}Sharpe.\{0,40\}'
== topology HEAD :41
 dir → `PraxisSignalConsumer` → **[consumer-side checks #4, #5, #7, #8, #9]** → `SubmitBracket` → Rithmic → account.
== topology HEAD :48
e emitter posts from inside the local network. Breakers #4, #5, #8 and #9 gain a consumer-side check (section 3), because 
== topology HEAD :62
-11-10-f2-session-flat-proposal.md`, PROPOSED, not adopted) #5 becomes an operator lockout only, and the system no-entry p
eriod 16:00–18:00 moves into #4; the n8n/consumer window check is then removed. | As the text stands, the n8n check runs before the file w
r. | ET wall clock; the window. | SPECIFIED | F2. R8 splits #5 into a disable of the system's own trading (redone) and a l
== topology HEAD :74
); EXIT/FLATTEN instruction types; consumer clock check for #4/#5; n8n gate nodes; Redis gate keys; PostgreSQL trip log; acco
== topology HEAD :78
 reach the webhook. If the fallback is taken, what changes: all nine checks move into the strategy before its order calls; Redis
== topology HEAD :86
n from one that did not. | (a) The consumer-side checks #4, #5, #7, #8 and #9 still apply to such a file; #1, #2, #3 and #
== ruleset HEAD :105
ide the flat time AND accept that paper Sharpe/DD numbers do not transfer if truncated
(exit 0)

### E-8 (ruleset note line that quotes DECISION_LOG.md:42)
$ cd /Volumes/Sensidine/Praxis.build && sed -n '121p' docs/specs/2026-07-16-b2-noise-area-ruleset.md | fold -w 150
1. Amear's lock of the Block-2 strategy definition, DECISION_LOG.md:42 (row 2026-07-16T19:29Z, WHO: trader (Amear) + orchestrator), item (1), copied b
y script: "(1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window)". Its item (3), copied by script: "(3) FIRST build = pure paper replic
ation with FIXED params".
(exit 0)

### E-9 (topology: which path B3 at :88 refers to)
$ cd /Volumes/Sensidine/Praxis.build && T=docs/specs/2026-11-10-live-signal-topology.md; git show HEAD:$T | sed -n '41p' | cut -c1-110; git show HEAD:$T | sed -n '74p' | cut -c1-110; git show HEAD:$T | sed -n '78p' | grep -o 'So option 1 is recommended[^.]*'; git show HEAD:$T | sed -n '82p;88p' | cut -c1-150
Path: NT8 emitter (computes signal) → HTTP POST → n8n webhook → **[breaker gates, Redis, default closed]** → W
| **1 (recommended)** | NT8 emitter strategy posts to the local n8n webhook | n8n + Redis before the file writ
So option 1 is recommended, and option 3 is the fallback **only if** OPEN-T1 finds the VM cannot reach the webhook
## 5. Bypass routes: ways an order can reach submission without passing the gates
| B3 | Manual orders typed into NT8, Rithmic or the MFFU platform. | No, never. | Nothing on this path can gate a human order. R8's KEPT half of #5 (l
(exit 0)
````

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
