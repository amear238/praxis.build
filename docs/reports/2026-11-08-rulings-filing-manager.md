# 2026-11-08 rulings filing (U1) — manager report. Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task
Unit `2026-11-08-rulings-filing` (U1): append D-2026-11-08-A (Amear's rulings R1–R9, 2026-11-08 voice session) to DECISIONS.md; add 3 MANIFEST.md rows. Unstaged. Done; see Result.

## Rubric criteria addressed
S1, S2, S4, S5, S8, S13 (verbatim from specs/SPEC_RUBRIC.md, quoted in the master's brief).

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| W1 a779cbcc4c5b078fc | BUILD | draft written to scratchpad `entry-draft.md` (44 lines, placeholders `@@PASTE@@`/`@@BODYSHA@@`); reported two brief discrepancies (filing notes at :86-90 not :84-88; values spec :72 is the ATR line in §4) — both confirmed by the manager (E2) |
| W2 a9ac1ae27d19a8dd3 (round 1, draft) | ADVERSARIAL | `VERDICT: REFUTED` — 4 MAJOR, 6 MINOR, all labelling / S8; every pointer CHECKED-CLEAN |
| W3 a6ab426522da7fdd1 (round 2, assembled draft) | ADVERSARIAL | `VERDICT: REFUTED` — 1 MAJOR, 8 MINOR; fenced block hash and every pointer CHECKED-CLEAN |
| W4 a0a03c7663daaca34 (round 3, inserted text) | ADVERSARIAL | `VERDICT: REFUTED` — 1 MAJOR, 4 MINOR (labels); append-only, hash, S13, MANIFEST format CHECKED-CLEAN |

## Process log
1. Baseline captured (E1). Sources 1–8 read by the manager directly (E2–E9 below hold the pasted reads).
2. Precedent check for a MANIFEST /DECISIONS.md row (E10): the 2026-11-07 rulings filing added row `MANIFEST.md:263` (`| /DECISIONS.md | Log | 2 | 2026-11-07 | D-2026-11-04-B addendum 5 … D-2026-11-07-A (DECISIONS.md:1203-1290 …) appended …`). That precedent is FOLLOWED: one /DECISIONS.md row is added. Observed alongside, not fixed: the later 11-07 appends (D-2026-11-07-B at :1292, its addenda at :1464, :1480, :1518) have no /DECISIONS.md MANIFEST row (`grep -n 'DECISIONS.md' MANIFEST.md | tail -3` ends at :263).
3. Draft worker W1 (BUILD) → scratchpad draft; adversary W2 (ADVERSARIAL) on the draft; fixes by the manager; paste inserted by script; MANIFEST rows appended by script. Done: W1 draft → W2 round 1 → manager fixes → splice (`splice.py`: paste inserted from the `sed -n '12,79p'` bytes, body hashed from the assembled text) → W3 round 2 → manager fixes → ONE append to DECISIONS.md (a blank line, then `cat entry-assembled.md`, appended with >>) → MANIFEST rows appended by Python → W4 round 3 on the inserted text → manager fixes confined to lines after :1533 / :289 → E3 re-capture.

## Verification evidence

**E1 — baseline (before any write).**
```
$ git rev-parse HEAD origin/main
6c233d1c5f6c5b07e21970cb6d7df7b9bf5dd983
6c233d1c5f6c5b07e21970cb6d7df7b9bf5dd983
$ git status --porcelain > $S/porcelain-before.txt; wc -l
      89 .../scratchpad/porcelain-before.txt
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ wc -l DECISIONS.md MANIFEST.md
    1532 DECISIONS.md
     289 MANIFEST.md
$ sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
10	0	specs/SPEC_RUBRIC.md
```

**E2 — rulings file layout (re-read after W1 reported it had grown).**
```
$ wc -l docs/reports/2026-11-08-amear-rulings-voice.md
      94 docs/reports/2026-11-08-amear-rulings-voice.md
$ sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ grep -n '^[0-9]\. \*\*\|^\*\*Correction\|^## ' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-80
84:## Master's filing notes (not rulings; the master's readings, changeable by A
86:1. **R8 and the rubric file.** `specs/SPEC_RUBRIC.md:3-4`: "The build side do
87:2. **R1 and the rescued template.** `docs/reports/2026-10-31-o78-worker4-repo
88:3. **R4 and the values spec.** `docs/specs/2026-11-06-walk-forward-values.md:
89:4. **R6 and R7 vs the one-manager rule.** Parallel means a separate worktree 
90:5. **Sequencing.** The DECISIONS.md entry for these rulings is written and ve
94:**Correction 1 (praxis-master, 2026-11-08 ~14:30Z, append-only).** Line 9 abo
```
The paste range 12–79 and its hash are unchanged; the file grew at its foot (Correction 1 now at :94, so Correction 1's own "`wc -l` = 90" was true when written, not now). The brief's ":84-88" for the filing notes is :86-90 (OBSERVED above); the entry uses :86-90.

**E3 — final state (captured after all writes; `$S` = this session's scratchpad).**
~~~~
$ cmp <(git show HEAD:DECISIONS.md) <(head -n 1532 DECISIONS.md)
[rc=0]
$ cmp <(git show HEAD:MANIFEST.md) <(head -n 289 MANIFEST.md)
[rc=0]
$ wc -l DECISIONS.md MANIFEST.md
    1645 DECISIONS.md
     293 MANIFEST.md
    1938 total
[rc=0]
$ sed -n '1533p' DECISIONS.md | wc -c
       1
[rc=0]
$ sed -n '1534p' DECISIONS.md
## 2026-11-08 — D-2026-11-08-A: Amear's nine rulings R1–R9 (voice session, Claude.ai channel, 2026-11-08) — rulings WHO: amear; filed by praxis-manager
[rc=0]
$ sed -n '1544p;1613p' DECISIONS.md
```text
```
[rc=0]
$ sed -n '1545,1612p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
[rc=0]
$ sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
[rc=0]
$ cmp <(sed -n '1545,1612p' DECISIONS.md) <(sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md)
[rc=0]
$ sed -n '1534,1645p' DECISIONS.md | grep -c 'Fills are optimistic'
1
[rc=0]
$ sed -n '1534,1645p' DECISIONS.md | grep -n 'Fills are optimistic' | cut -c1-40
5:**Standing limitation:** Fills are opt
[rc=0]
$ sed -n '1534,1645p' DECISIONS.md | grep -c '^- \*\*FLAG [1-6] '
6
[rc=0]
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
[rc=0]
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
10	0	specs/SPEC_RUBRIC.md
[rc=0]
$ git diff --numstat -- DECISIONS.md MANIFEST.md
113	0	DECISIONS.md
4	0	MANIFEST.md
[rc=0]
$ diff $S/porcelain-before.txt $S/porcelain-after.txt
2a3
>  M DECISIONS.md
5a7
>  M MANIFEST.md
86a89
> ?? docs/reports/2026-11-08-rulings-filing-manager.md
[rc=1]
$ git status --porcelain -- docs/reports/2026-11-08-amear-rulings-voice.md docs/reports/2026-11-08-strategy-filter-audit.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
[rc=0]
$ sed -n '290,293p' MANIFEST.md | awk -F'|' '{print NF-1, $2}'
6  /docs/reports/2026-11-08-amear-rulings-voice.md 
6  /docs/reports/2026-11-08-strategy-filter-audit.md 
6  /docs/reports/2026-11-08-rulings-filing-manager.md 
6  /DECISIONS.md 
[rc=0]
~~~~

**E4 — pointer reads behind the entry (compact re-captures; full reads were made earlier in-session).**
~~~~
(captured with LC_ALL=en_US.UTF-8 so cut -c counts characters)
$ sed -n '718p' DECISION_LOG.md | cut -c1-40
- [2026-11-08T14:02:11Z] **WHO: amear** 
[rc=0]
$ sed -n '719p;720p' DECISION_LOG.md | cut -c1-48
- [2026-11-08T14:22:00Z] WHO: praxis-master | WH
- [2026-11-08T14:30:00Z] WHO: praxis-master | WH
[rc=0]
$ sed -n '2024p' DISPATCH_LOG.md | cut -c1-48
- [2026-11-08T14:24:00Z] WHO: praxis-master | WH
[rc=0]
$ git show 29c3e13:docs/reports/2026-10-31-o78-worker4-report-adversarial.md | sed -n '208,212p' | cut -c1-110
**W4-E6. Rescued trading-hours templates** (regular Sessions block; the first entries in each file are holiday
```
-----CME US Index Futures RTH
TimeZone ['Eastern Standard Time']
[('Monday', '830', 'Monday', '1600'), ('Tuesday', '830', 'Tuesday', '1600'), ('Wednesday', '830', 'Wednesday',
[rc=0]
$ /usr/bin/grep -n 'higher win rate' docs/reports/2026-11-04-voice-session-notes-4.md | cut -c1-120
36:1. **Research brief:** a non-discretionary, codeable strategy with a higher win rate / smoother equity (mean-reversio
[rc=0]
$ sed -n '736p' DECISIONS.md | cut -c1-90
## 2026-11-04 — D-2026-11-04-A: R-1104-1..3 — commit permission; housekeeping is Code's; R
[rc=0]
$ sed -n '752p' DECISIONS.md | cut -c1-75
**R-1104-3 — judged go/no-go version; tick-data purchase condition.** Fills
[rc=0]
$ sed -n '1092p' DECISIONS.md | cut -c1-200
| 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | It is a second session. Coordinate: Code does not run agents while the VM session writes; handover goes through t
[rc=0]
$ bd show Praxis_build-9lj | head -1
○ Praxis_build-9lj [BUG] · gate-manager-output.sh grades the newest docs/reports/*.md, so concurrent managers get each other's reports graded   [● P2 · OPEN]
[rc=0]
$ bd show Praxis_build-v6y | head -1
✓ Praxis_build-v6y [BUG] · Gate/concurrency gap: audit token does not bind the staged tree; parallel sessions can inject files into a repo tip write   [● P1 · CLOSED]
[rc=0]
$ /usr/bin/grep -n 'DECISIONS.md' MANIFEST.md | tail -3 | cut -c1-110
290:| /docs/reports/2026-11-08-amear-rulings-voice.md | Report | 2 | 2026-11-08 | Amear's rulings R1–R9 (voice
292:| /docs/reports/2026-11-08-rulings-filing-manager.md | Report | 2 | 2026-11-08 | Manager report for unit 2
293:| /DECISIONS.md | Log | 2 | 2026-11-08 | D-2026-11-08-A (DECISIONS.md:1534-1645; Amear's nine rulings R1–R
[rc=0]
$ /usr/bin/grep -n '^### F' specs/SPEC_RUBRIC.md
17:### F1 — Signal-path topology vs. circuit-breaker placement
30:### F2 — Session-flat time vs. breakers #4 and #5
45:### F3 — Backtest fill resolution vs. acquired data granularity
59:### F4 — MFFU automation compliance
[rc=0]
~~~~
Observer effect: the last `grep -n 'DECISIONS.md' MANIFEST.md | tail -3` above now returns this unit's own rows. The same command run BEFORE the MANIFEST write returned rows :246, :248, :263 (row :263 = `| /DECISIONS.md | Log | 2 | 2026-11-07 | D-2026-11-04-B addendum 5 … D-2026-11-07-A (DECISIONS.md:1203-1290 …) appended …`) — that is the precedent followed.

**E5 — negative tests (do the two gates actually block?).**
~~~~
NEG1 (VOID — first attempt): sed '1s/R1/R7/' on a copy of the block body → cmp rc=0, sha unchanged 73518316…a263.
     The mutation was a no-op (body line 1 contains no "R1"); this proves nothing and is recorded as void.
NEG1b: sed '1s/AMEAR/AMEAX/' on a copy of the block body
  cmp: .../neg/body.txt .../neg/body-mut.txt differ: char 29, line 1   cmp rc=1
  SHA2-256(stdin)= f6741add443ae6b71c37ae94842a5ac2d06abf227d225004bfb02fe8b78671cd   (≠ 73518316…a263)
NEG2: one trailing space added to line 1203 of a copy of DECISIONS.md's first 1532 lines
  cmp <(git show HEAD:DECISIONS.md) prefix.txt → differ: char 212608, line 1203   cmp rc=1
NEG3: block range off by one (sed -n '1545,1613p', includes the closing fence)
  SHA2-256(stdin)= 1a4c220db48993f0cfda17d9466c74b0e909a3c73232dc526b66be101244dc4c   (≠ 73518316…a263)
~~~~
Both checks trip on a one-byte change and on an off-by-one range.

## Adversarial findings
Three adversarial rounds; each worker got only the artifact, the sources and the criteria, not the drafter's reasoning. Every pointer was CHECKED-CLEAN in all three rounds; every defect was a label / S8 / wording defect. All fixes were applied by the manager by script (`fix.py`, `fix2.py`, `fix3.py`, `fix4.py` in the scratchpad; each replacement asserted to match exactly once; after insertion, edits were confined to lines after 1533).
- **Round 1 (W2, `VERDICT: REFUTED`, 4 MAJOR / 6 MINOR).** MAJOR 1: R8's "does not name a governing rule or a 15:00 disposition" answered FLAG 6's own question in the filer's voice, and "That artifact does not yet exist" was the master's note-1 reading presented as a bare fact → both reworded and pointed at FLAG 6. MAJOR 2: R1 dropped "ET" from his "If the live template starts 08:30 ET", and mislabelled filing note 2's sentence as the filer's → note 2 quoted under its own label, his condition quoted, TimeZone-field point labelled INFERRED. MAJOR 3: R7's "not changed by it" picked the master's reading outside the note-4 label; 9lj is a grading bug, not the source of the rule → moved inside the note-4 label; the R6 "not queued behind it" vs settlement 9 tension recorded. MAJOR 4: candidate readings in FLAGS 2–4 without the filer's label → labelled. MINOR 5 (missed R4 conflicts: "trading day" vs "session", net-of-costs, per-day vs per-trade win rate) → added as FLAG 5 and folded into FLAGS 2–3. MINORs 6–10 (O1 extension unlabelled; R5–R9 audit mapping is the master's, rulings file :3; R6 pre-conditions are U2 only; note-5 sentence unlabelled; header "filed WHO: amear") → all fixed.
- **Round 2 (W3, `VERDICT: REFUTED`, 1 MAJOR / 8 MINOR).** MAJOR: "*Supersedes:* filter C3" was unlabelled and C3's cell (audit :88) also carries "avg win ÷ avg loss < 1.5 fails regardless of win rate", which R5's words do not name → changed to *Bears on:* with that identification labelled INFERRED and the extra clause left unsettled. **This weakens a sentence in the master's brief** ("note it supersedes filter C3"); the brief's wording would have been a reading past his words (S2/S8). MINORs: R2/R3 sub-part assignment and R9 → §4.4 labelled; "15:00–18:00 ET window" gloss removed from inside the note-1 paraphrase; "RTH" removed from the :92 quote; "until Amear says otherwise note 4 is the operating reading" re-labelled; Copy-check wording made not to claim a check before it ran; "conflicts" → "checks"; label forms; R3 vs Q8 recorded side by side.
- **Round 3 (W4 a0a03c7663daaca34, on the INSERTED text, `VERDICT: REFUTED`, 1 MAJOR / 4 MINOR).** MAJOR: R8's "Plainly: the F2 state line … changes by Amear's hand …" is filing note 1's reading presented as fact → labelled "Master's reading (filing note 1), changeable by Amear". MINORs: "it is the observation that decides" labelled INFERRED; R4's sub-part mapping labelled; MANIFEST row :290 no longer calls Correction 1 a "reading"; three label forms normalised. **Round-3 fixes were NOT re-attacked by a fourth adversary** (turn budget); the post-fix checks are E3 only (cmp, hash, S13 count, `grep -c 'Plainly'` = 0).

## S6 cross-block check
F1–F4 headers at `specs/SPEC_RUBRIC.md`:17/:30/:45/:59 (E4); this unit wrote nothing there — `git diff --numstat HEAD -- specs/SPEC_RUBRIC.md` = `10	0` (E1 and E3, identical: the pre-existing July hunk). The entry records interactions only: R8↔F2 (FLAG 6, nothing unblocked), R2/R3↔O1 (:74, not discharged here), R4↔O4 (:94, FLAG 3), R1↔values spec :72/:206. No spec, rubric, VM or ledger file changed (E3 porcelain diff).

## Files staged
None. The real index is untouched (E3: `12 files changed, 5726 insertions(+), 2 deletions(-)`). Working-tree changes, unstaged: `M DECISIONS.md` (113 lines appended, :1533 blank + :1534–1645), `M MANIFEST.md` (4 rows, :290–293), `?? docs/reports/2026-11-08-rulings-filing-manager.md` (this file).

## Does NOT cover
- No ruling is acted on: no VM handoff edit (U3), no breaker proposal (U4), no research (U5), no housekeeping (U2), no MFFU read.
- The rulings file and the strategy filter audit stay untracked; MANIFEST rows do not track them.
- The later 11-07 appends (D-2026-11-07-B and addenda 1–2, DECISIONS.md:1292–1532) have no /DECISIONS.md MANIFEST row; observed, not fixed.
- The rulings file's line 9 and the three ledger rows still say "13–83" beside Correction 1; not edited (not this unit's files).
- No grade: the auditor is the master's to spawn.

## Still the master's
1. Whether the R5 wording change (round 2: "supersedes" → labelled "bears on", C3's third clause left open) is acceptable against the brief, which asked for "supersedes".
2. Three tensions the entry records side by side but does NOT list under NEEDS AMEAR, because the brief limits that list: (a) R3 "Gate 6 (WFE) applies to arm (b) only" vs Q8 "both arms are judged against all six Phase 3 gates" (values spec :121); (b) R6 "Runs in parallel with the walk-forward, not queued behind it" vs settlement 9 (DECISIONS.md:1092, a master's decision under R-1104-2); (c) whether R2/R3 discharge O1. (a) and (b) involve his own rulings or a settlement he can change; whether to route them to Amear is the master's call.
3. Audit §6 Q3's yes/no ("Do you want this audit filed as an input to F2?") is not answered by R8's words; recorded in the entry, not flagged.
4. Whether the round-3 fixes need a fresh adversarial pass before audit.

## Questions only Amear can answer
The entry's NEEDS AMEAR list, FLAGS 1–6 (DECISIONS.md, inside :1534–1645): 1 R4 vs the §6 selection statistic (gate only, or §6 too); 2 the gate-2 Sharpe base and which §6 terms carry over; 3 where R4's win-rate rule applies and its counting unit; 4 whether the 4% DD equity-base item stays open; 5 "trading day" vs values-spec session i; 6 whether R8 changes F2's state in the rubric and whether the master's filing-note-1 reading is right. None is resolved.

Result: PASS at level WRITTEN — entry and MANIFEST rows written and verified on disk (append-only cmp rc 0, block sha = 73518316…a263, S13 once, index untouched, porcelain diff = the three allowed lines). Not graded; the master spawns the auditor.

## Correction 1 (2026-11-08, unit 2026-11-08-rulings-filing-correction-1) — S1 cure after audit FAIL 1

Written by praxis-manager, unit `2026-11-08-rulings-filing-correction-1`. This section is append-only: lines 1–221 above are unchanged (sha256 before and after in C1.5). It cures audit FAIL 1 on S1 ("Every claim in a report has pasted command output, not a description of output.", `specs/SPEC_RUBRIC.md:107`). The skeleton line first written at :225 has been replaced by this text. Every change is below line 221.

### C1.1 Baseline (pasted, first command of this unit)

~~~~text
$ wc -l docs/reports/2026-11-08-rulings-filing-manager.md; head -n 221 … | shasum -a 256; tail -n 1 … | cut -c1-200; git diff --cached --stat | tail -1; git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'; git rev-parse --short HEAD
     221 docs/reports/2026-11-08-rulings-filing-manager.md
fd44d0771dbba38a070dc2459091fb2873a8d952bd1c42de9c65963a6e5b58a8  -
Result: PASS at level WRITTEN — entry and MANIFEST rows written and verified on disk (append-only cmp rc 0, block sha = 73518316…a263, S13 once, index untouched, porcelain diff = the three allowed
 12 files changed, 5726 insertions(+), 2 deletions(-)
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-rulings-filing-manager.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
6c233d1
~~~~

This report is untracked (`??`), so the brief's `git show :0:` comparison has nothing to read. The `head -n 221` sha256 is the append-only proof instead.

### C1.2 Pointer reads (pasted)

**Method.** The pointers come from D-2026-11-08-A as read this unit with `sed -n '1534,1645p' DECISIONS.md`. The list is every `file:line` or `file:range` the entry makes outside its fenced block. It includes all the pointers the brief named, plus rulings :9, :61, :74, :76, :79, :94, the `29c3e13` o78 read, the F1–F4 header grep, the beads and the block sha. One script made the reads (`cap.sh`, in the session scratchpad, not in the repo). It ran under `LC_ALL=en_US.UTF-8`, so `cut -c1-300` counts characters. The first run under the C locale cut through multibyte characters and gave invalid UTF-8; it was discarded and re-run. Lines longer than 300 characters are CUT at 300, as each command shows. Where the entry quotes text past column 300, block Q after the reads shows it with `grep -oF` on the cited line. Output blocks use `~~~~` fences, because two sources contain triple backticks. After each paste, a `Verdict:` line says whether the line matches the entry's use. The verdict lines are the manager's, not output.

**P-V:72**

~~~~text
$ sed -n '72p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **ATR computation** — SETTLED: the simple mean of the true ranges of the last 14 completed RTH sessions, TR = max(session high, prior session close) − min(session low, prior session close). It is computed inside the strategy from the 1-minute bars, in the same no-look-ahead store as the band (`Pra
~~~~

Verdict: MATCHES. The entry's use (R1 Bears-on; S6): §4's ATR line "the last 14 completed RTH sessions".

**P-V:92**

~~~~text
$ sed -n '92p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **Statistic** — SETTLED, **as the in-sample selection objective only**: annualised Sharpe of daily net P&L. For the in-sample sessions i = 1…n: d_i = sum of the net P&L (after commission and slippage) of trades exited in session i, 0 if none. S = mean(d) / sd(d) × √252, sd with n − 1, risk-free ra
~~~~

Verdict: MATCHES. The entry's use (FLAG 1, FLAG 2, FLAG 5): every quoted fragment from :92, including the ones past column 300, is shown at :92 in block Q below (grep -oF hits).

**P-V:93**

~~~~text
$ sed -n '93p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **This statistic does NOT define the gate "OOS Sharpe ≥ 1.0".** The gate's Sharpe definition and its equity base stay OPEN under ruling 9: "Notes-4 unruled items stay open; none block anything." They are notes-4 items (D-2026-11-06-B item 18, DECISIONS.md:1101; REPORTED BY `docs/reports/2026-11-07
~~~~

Verdict: MATCHES. "The gate's Sharpe definition and its equity base stay OPEN under ruling 9" (FLAG 2). The entry says it cites DECISIONS.md:978 (FLAG 4); that is shown in block Q.

**P-V:121,127**

~~~~text
$ sed -n '121,127p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **Gates** — RULED (Q8: "Q8 both arms are judged against all six Phase 3 gates; arm (b) must also pass PBO < 0.05."). The six gates (REPORTED BY `docs/specs/2026-11-05-phase3-build-specification.md:80-85`, under "Pass gates (non-negotiable):" at `:78`):
  1. OOS profit factor ≥ 1.30
  2. OOS Sharpe ≥ 1.0
  3. Max drawdown ≤ 4% of equity
  4. ≥ 250 aggregate OOS trades
  5. ≥ 60% of walk-forward windows profitable
  6. Walk-forward efficiency ≥ 0.50
~~~~

Verdict: MATCHES. Q8 "both arms are judged against all six Phase 3 gates" is at :121 (R2/R3). The six gates are at :122–127, with gate 2 "OOS Sharpe ≥ 1.0" at :123 (FLAG 3). There is no win-rate gate.

**P-V:128**

~~~~text
$ sed -n '128p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **Judged arm = (a)** — RULED (ruling 4 of 2026-11-06: "judged arm = (a) fixed rules"). Q8 says "both arms are judged against all six Phase 3 gates". Both are his words. This file does not reconcile them.
~~~~

Verdict: MATCHES. "Judged arm = (a)" against Q8 (R2/R3).

**P-V:132**

~~~~text
$ sed -n '132p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
  - Not covered, OPEN, not resolved here: (i) the equity base and the Sharpe definition of the "OOS Sharpe ≥ 1.0" gate — ruling 9 (notes-4; WF spec NEEDS AMEAR 7); the notes-4 source (DECISIONS.md:978) scopes the equity base as "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)"
~~~~

Verdict: MATCHES. (i) is the gate's Sharpe and equity base, OPEN (FLAG 2). (ii) is gate 6 for arm (a), and (iii) is GO on arm (b) (R2/R3). The DECISIONS.md:978 cite (FLAG 4) is in block Q.

**P-V:133**

~~~~text
$ sed -n '133p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
  - The WFE formula for arm (b) (WF spec NEEDS AMEAR 8, second half) — OPEN (ruling 9; the O1 gate set, REPORTED BY the return handoff :74): a WFE formula is part of the gate set. Not resolved here.
~~~~

Verdict: MATCHES. "The WFE formula for arm (b) … OPEN" (R2/R3).

**P-V:134**

~~~~text
$ sed -n '134p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
  - Whether Q8 discharges O1 is left to the master and the auditor. This file does not resolve O1.
~~~~

Verdict: MATCHES. "Whether Q8 discharges O1 is left to the master and the auditor" (R2/R3).

**P-V:135**

~~~~text
$ sed -n '135p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **Max-DD gate base** — RULED (D-2026-11-05-A item 3, DECISIONS.md:814: "the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit."). It stands as written. Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that it
~~~~

Verdict: MATCHES. RULED under D-2026-11-05-A item 3, DECISIONS.md:814 (FLAG 4). Block Q shows the line's tail, "that item stays OPEN". The entry's "kept OPEN" paraphrases it and is not a quotation.

**P-V:137**

~~~~text
$ sed -n '137p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **No tier chosen** — RULED (Q9: "Q9 no tier chosen. Report the per-tier table; I pick after paper results."). **The tier pick is OPEN** — his, after paper results.
~~~~

Verdict: MATCHES. "The tier pick is OPEN" (FLAG 2).

**P-V:139**

~~~~text
$ sed -n '139p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
- **Worst drawdown per window** (WF spec NEEDS AMEAR 21) — SETTLED, strictest reasonable: measured on closed-trade equity and on end-of-day equity, each both from the window's start and carried across windows; the worst of these four is judged. Intrabar equity is not in the bridge's trade lists (bri
~~~~

Verdict: MATCHES as a paraphrase. The line says "Both 1 NQ and 1 MNQ figures are reported" (block R). The entry's "the 1 NQ / 1 MNQ figure" is the filer's shorthand, not in quotation marks, and the exact string is not in the file (grep rc 1, block Q).

**P-V:206**

~~~~text
$ sed -n '206p' docs/specs/2026-11-06-walk-forward-values.md | cut -c1-300
    - (iii) Policy-rule oracle, for non-stop exits. For each trade, the script walks the checkpoints after the entry's decision checkpoint, up to and including the exit decision bar d (T8's definition). A checkpoint here is HH:00/HH:30, inside RTH, and not a session-flat bar F. The script finds the 
~~~~

Verdict: MATCHES. T12(iii): "the session's typical-price VWAP from the 09:30 bar" (block Q).

**P-A:3**

~~~~text
$ sed -n '3p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
**Date:** 2026-11-08. **By:** Claude.ai Praxis channel (research agent), at Amear's brief of the same date.
~~~~

Verdict: MATCHES. By the Claude.ai channel research agent (R5).

**P-A:4**

~~~~text
$ sed -n '4p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
**Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. No decision, spec or ruling is changed. The 2026-11-08 ruling RTH = 09:30–16:00 ET is not reopened.
~~~~

Verdict: MATCHES. "recommendation only … **PROPOSED**" (R5).

**P-A:88**

~~~~text
$ sed -n '88p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
| C3 | R:R shape: 3:1 on a 50% partial plus runner (low frequency); 1.5:1 (higher frequency); "avg win ÷ avg loss < 1.5 fails regardless of win rate" | D4 Hard Filter 2; D5 Gap 3; D6 F2 | Copied from the discretionary reference style. D1 had called those figures "reference only — not required". §4.1
~~~~

Verdict: MATCHES. C3's cell, including "avg win ÷ avg loss < 1.5 fails regardless of win rate" (R5).

**P-A:127**

~~~~text
$ sed -n '127p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
### 4.1 The fixed R:R shape (3:1 partial plus runner; 1.5:1)
~~~~

Verdict: MATCHES. The §4.1 heading (R5).

**P-A:144**

~~~~text
$ sed -n '144p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
- **Live consequence.** The higher-win-rate research Amear asked for on 2026-11-04 (notes-4, "New work" item 1) would be gutted by C3. Mean-reversion strategies typically run average win ÷ average loss below 1.5 [I]. That brief should not inherit C3.
~~~~

Verdict: MATCHES. The higher-win-rate research, notes-4 "New work" item 1 (R5).

**P-A:165**

~~~~text
$ sed -n '165p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
### 4.4 Overnight-hold parking
~~~~

Verdict: MATCHES. §4.4 "Overnight-hold parking" (R9).

**P-A:175**

~~~~text
$ sed -n '175p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
## 5. Step 5: ranked re-evaluation list (PROPOSED)
~~~~

Verdict: MATCHES. The §5 heading, the ranked re-evaluation list (R6 "candidates at §5").

**P-A:211,214**

~~~~text
$ sed -n '211,214p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-300
1. **R:R filter:** retire the 3:1 / 1.5:1 shape filter for all future strategy research, including the higher-win-rate brief, and judge by net expectancy, out-of-sample gates and MFFU drawdown survival instead?
2. **Re-evaluation:** test the two §5 candidates on the existing minute data, research and backtest only, nothing bought?
3. **Breakers #2, #3, #4 and the system-wide part of #5:** their values were set for a human trader and truncate several strategies, including the baseline's published close-flat. This is F2's frozen question. Do you want this audit filed as an input to F2? Filing it decides nothing.
4. **Overnight-hold strategies (FOMC Even-Week):** these only work on a venue that allows multi-day holds. Park permanently, or revisit if a second venue or own capital is ever on the table?
~~~~

Verdict: MATCHES. Q1–Q4 map to R5, R6, R8 and R9. Block Q shows Q3's "Do you want this audit filed as an input to F2?" at :213.

**P-R:3,4**

~~~~text
$ sed -n '3,4p' specs/SPEC_RUBRIC.md | cut -c1-300
Authority: the scoping agent (Claude.ai) via Amear. The build side does not
edit this file. It proposes changes; Amear applies them.
~~~~

Verdict: MATCHES. "The build side does not edit this file. It proposes changes; Amear applies them." (R8, FLAG 6).

**P-R:17**

~~~~text
$ sed -n '17p' specs/SPEC_RUBRIC.md | cut -c1-300
### F1 — Signal-path topology vs. circuit-breaker placement
~~~~

Verdict: MATCHES. The F1 header (S6).

**P-R:30**

~~~~text
$ sed -n '30p' specs/SPEC_RUBRIC.md | cut -c1-300
### F2 — Session-flat time vs. breakers #4 and #5
~~~~

Verdict: MATCHES. The F2 header (S6).

**P-R:41,43**

~~~~text
$ sed -n '41,43p' specs/SPEC_RUBRIC.md | cut -c1-300
**Unblocks when.** A DECISIONS.md entry names the governing rule and the
15:00 disposition, and breaker specs #4 and #5 are amended to match.
**Blocks.** Block 3. Block 4 paper trading.
~~~~

Verdict: MATCHES. The unblock condition at :41–42 is verbatim as quoted in R8. "Blocks." is at :43.

**P-R:45**

~~~~text
$ sed -n '45p' specs/SPEC_RUBRIC.md | cut -c1-300
### F3 — Backtest fill resolution vs. acquired data granularity
~~~~

Verdict: MATCHES. The F3 header (S6).

**P-R:59**

~~~~text
$ sed -n '59p' specs/SPEC_RUBRIC.md | cut -c1-300
### F4 — MFFU automation compliance
~~~~

Verdict: MATCHES. The F4 header (S6).

**P-R:74,79**

~~~~text
$ sed -n '74,79p' specs/SPEC_RUBRIC.md | cut -c1-300
### O1 — Walk-forward gate set for the replication arm
Walk-forward efficiency ≥ 0.50 is one of six non-negotiable Block 2 pass gates
and is undefined without an in-sample optimisation step. Deviation D removed
optimisation from the first pass. **Required:** a written statement of which
gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
replication arm or the later optimisation arm.
~~~~

Verdict: MATCHES. O1 (R2/R3; S6 ":74").

**P-R:94,99**

~~~~text
$ sed -n '94,99p' specs/SPEC_RUBRIC.md | cut -c1-300
### O4 — Backtest-vs-live configuration parity
Deviation C permits reverse-and-re-enter. Breakers #2 and #3 cap trades and end
the session after two consecutive losers. Block 4's gate compares live to
backtest within ±15% win rate and ±25% average trade P&L. **Required:** a
written statement of whether the Block 2 backtest runs with breakers applied,
without them, or both — and how the Block 4 gate is satisfiable if they differ.
~~~~

Verdict: MATCHES. O4 (S6 ":94"). "within ±15% win rate" runs across :96–97 (FLAG 3).

**P-H:61,67**

~~~~text
$ sed -n '61,67p' docs/reports/2026-11-07-return-handoff-claude-ai-2.md | cut -c1-300
1. **B1 — session start.** The oracle fits the three committed 2026-11-01 base runs on all 3,190 trades (1190 + 810 + 1190, `scripts/wf/oracle/tests/test_baseruns.py:28–30`) for the m = 0 band/VWAP/policy part when sessions start at the 08:31-stamped bar. At 09:31 the baseline run fits 864/1190 entr
   - Is 08:31–16:00 the session you mean by "RTH" (Q6, D-2026-11-07-A), or do arm (a)/(b) anchor at the 09:30 open?
   - Which NT8 trading-hours template did the 2026-11-01 runs use, and will arm (b) use the same one? On record, REPORTED BY AMEAR (screenshots and his notes): `Trading hours` = `CME US Index Futures RTH` for the runs in `docs/reports/2026-11-01-three-strategy-results.md:89`, `:195`, `:313`; the VM 
   - The master has a hypothesis about the cause (`21:42:00Z` item (2)). It is UNVERIFIED.
   - No spec wording changes before your word (`21:42:00Z` item (5)). The lines that bear on it: T12(iii) "VWAP from the 09:30 bar" (`docs/specs/2026-11-06-walk-forward-values.md:206`) and §4 "RTH sessions" (`:72`).
2. **Tier pick** (Q9): yours after paper results, not now (`docs/reports/2026-11-07-wf-mac-side-maths-manager.md:591`).
3. **Ruling-9 notes-4 items, still open:** the gate 2 Sharpe definition and its equity base (values spec §6 `:93`, §8 `:132`); the gate 6 WFE formula, and whether gate 6 applies to arm (a) (`:132–133`); whether GO / HOLD / REJECT may rest on arm (b) (maths report `:592–594`).
~~~~

Verdict: MATCHES. B1 is at :61 (R1, :61-65). Both bears-on pointers (:206, :72) are at :65. §4 item 3 is at :67, and block Q shows its three sub-parts.

**P-N4:35,36**

~~~~text
$ sed -n '35,36p' docs/reports/2026-11-04-voice-session-notes-4.md | cut -c1-300
## New work requested by Amear
1. **Research brief:** a non-discretionary, codeable strategy with a higher win rate / smoother equity (mean-reversion class) that fits MFFU's $1,500 trailing drawdown better than the Noise-Area's rare-big-winner profile. Same research standard as `docs/briefs/2026-11-04-research-briefs-tickdata-rep
~~~~

Verdict: MATCHES. The heading "New work requested by Amear" is at :35, and item 1 is at :36 (R5).

**P-D:736**

~~~~text
$ sed -n '736p' DECISIONS.md | cut -c1-300
## 2026-11-04 — D-2026-11-04-A: R-1104-1..3 — commit permission; housekeeping is Code's; R-1104-3 "Yeah" (brief's framing: High fill resolution + breakers on as the judged version); tick-data purchase condition (proof of concept)
~~~~

Verdict: MATCHES. The D-2026-11-04-A heading (R6).

**P-D:748**

~~~~text
$ sed -n '748p' DECISIONS.md | cut -c1-300
**R-1104-2 — housekeeping is Code's.**
~~~~

Verdict: MATCHES. The R-1104-2 heading (evidence grades, settlement 9 label).

**P-D:752**

~~~~text
$ sed -n '752p' DECISIONS.md | cut -c1-71
**R-1104-3 — judged go/no-go version; tick-data purchase condition.** F
[manager note, not output] (cut at 71 characters, not 300: the rest of :752 is the standing limitation sentence. S13 wants that sentence once per report, and it is already on line 1.)
~~~~

Verdict: MATCHES. The R-1104-3 heading (R6).

**P-D:814**

~~~~text
$ sed -n '814p' DECISIONS.md | cut -c1-300
- *"3. Max-DD gate base: the lower of 4% of the MFFU account size and MFFU's trailing drawdown limit. Revisit if a personal account is used."*
~~~~

Verdict: MATCHES. Max-DD gate base, item 3 (FLAG 4).

**P-D:948**

~~~~text
$ sed -n '948p' DECISIONS.md | cut -c1-300
  - reading (voice agent, notes-4): **R-1104-3 defined:** PoC = full pipeline (TradingView → n8n → NT8 → Rithmic → MFFU sim) running on sim in live markets = Block 4. **No historical tick-data purchase; proceed without it.** The PROPOSED 12-item checklist from report C is not adopted; items 1–7, 10,
~~~~

Verdict: MATCHES. "No historical tick-data purchase", which the line itself labels "reading (voice agent, notes-4)" (R6).

**P-D:978**

~~~~text
$ sed -n '978p' DECISIONS.md | cut -c1-300
**Not ruled (stay open, from notes-4 `## Not ruled on`):** past use of the GitHub login (item 24; no remedy requested); second Rithmic read-only connection (item 23); CME Atlassian wiki as a source (item 19); equity base for the 4% DD gate (item 5) and Sharpe definition (item 4); O1 gate set / WFE w
~~~~

Verdict: MATCHES. Block Q shows "equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)" at :978 (FLAG 4).

**P-D:1092**

~~~~text
$ sed -n '1092p' DECISIONS.md | cut -c1-300
| 9 — VM agent on Z: | "VM agent on Z: while Code runs = second session, coordinate" | It is a second session. Coordinate: Code does not run agents while the VM session writes; handover goes through the VM handoff file. | pending: VM handoff file (loop step c) |
~~~~

Verdict: MATCHES. Settlement 9: "Code does not run agents while the VM session writes; handover goes through the VM handoff file" (R7).

**P-VR:7**

~~~~text
$ sed -n '7p' vm/replies/README.md | cut -c1-300
- **Session markers:** `<ts>-STATUS.md` holding `STARTED` before the VM agent's first step, and `FINISHED` when it stops. Code starts no agent between the two (one-session rule).
~~~~

Verdict: MATCHES. The STARTED/FINISHED markers (R7).

**P-VH:37**

~~~~text
$ sed -n '37p' vm/2026-11-06-vm-handoff.md | cut -c1-300
11. **One-session rule.** While you work on Z:, Code dispatches nothing (DECISIONS.md:1092, settlement 9: "Code does not run agents while the VM session writes; handover goes through the VM handoff file."). Signal it: before your first step, write `Z:\vm\replies\<ts>-STATUS.md` holding the line `STA
~~~~

Verdict: MATCHES. The one-session rule, which quotes settlement 9 (R7).

**P-RF:3**

~~~~text
$ sed -n '3p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
Filed verbatim by praxis-master at 2026-11-08T14:02Z from the message Amear pasted into the Claude Code session (`date -u` read 14:02:11Z on receipt). Evidence grade: OBSERVED (the text in the fenced block is the message as received in this session, copied without edits; nothing has been acted on at
~~~~

Verdict: MATCHES. Written by praxis-master (Status line). Block Q shows "§6 of … (questions 1–4)" (evidence grades).

**P-RF:9**

~~~~text
$ sed -n '9p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
The paste, verbatim (lines 13–83 of this file are the message; nothing in them is the master's):
~~~~

Verdict: MATCHES. "lines 13–83" (Status line's Correction 1 pointer).

**P-RF:61**

~~~~text
$ sed -n '61p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
HOUSEKEEPING (Code's job, not Amear's)
~~~~

Verdict: MATCHES. The HOUSEKEEPING header, the start of "rulings file lines 61–74".

**P-RF:74**

~~~~text
$ sed -n '74p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
- Stale bead title on Praxis_build-867.
~~~~

Verdict: MATCHES. The last housekeeping item, the end of 61–74.

**P-RF:76**

~~~~text
$ sed -n '76p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
STILL OPEN FOR AMEAR (next session)
~~~~

Verdict: MATCHES. The STILL OPEN header, the start of 76–79.

**P-RF:79**

~~~~text
$ sed -n '79p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
language summary of what those lines do.
~~~~

Verdict: MATCHES. The last line of the paste, the end of 76–79.

**P-RF:86,90**

~~~~text
$ sed -n '86,90p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
1. **R8 and the rubric file.** `specs/SPEC_RUBRIC.md:3-4`: "The build side does not edit this file. It proposes changes; Amear applies them." F2's unblock condition (`:41-42`) is "A DECISIONS.md entry names the governing rule and the 15:00 disposition, and breaker specs #4 and #5 are amended to matc
2. **R1 and the rescued template.** `docs/reports/2026-10-31-o78-worker4-report-adversarial.md:208-219` (committed `29c3e13`) prints a RESCUED copy of `CME US Index Futures RTH.xml` as Monday–Friday `830`–`1600`, TimeZone `Eastern Standard Time` (REPORTED BY that worker). The live VM template is UNV
3. **R4 and the values spec.** `docs/specs/2026-11-06-walk-forward-values.md:92` defines Sharpe as the IN-SAMPLE SELECTION objective only (daily net P&L in dollars at 1 NQ, 0 on no-trade sessions, √252, n − 1, rf 0, "needs no equity base"); `:93` and `:132` say the gate "OOS Sharpe ≥ 1.0" definition
4. **R6 and R7 vs the one-manager rule.** Parallel means a separate worktree and branch (R7). Dispatch stays serial: one praxis-manager at a time (bug `Praxis_build-9lj`), and no dispatch while a `vm/replies/<ts>-STATUS.md` holds `STARTED` without `FINISHED` (settlement 9).
5. **Sequencing.** The DECISIONS.md entry for these rulings is written and verified on disk before any unit that depends on them is dispatched (`bd memories master-s4-entry-before-code`).
~~~~

Verdict: MATCHES. Notes 1–5 are at :86–:90. Block Q shows note 1's "not exist yet" and note 2's quoted re-run sentence. Note 3: the entry's "names the same checks" is a paraphrase (grep rc 1, block Q). :88's tail (block R) lists the §6 and win-rate checks, so the paraphrase holds. It drops "R4 fills the gate definition" (adversary finding 3, confirmed).

**P-RF:94**

~~~~text
$ sed -n '94p' docs/reports/2026-11-08-amear-rulings-voice.md | cut -c1-300
**Correction 1 (praxis-master, 2026-11-08 ~14:30Z, append-only).** Line 9 above says the paste occupies "lines 13–83 of this file". That was a hand count made while writing and is WRONG. OBSERVED after writing: `wc -l` = 90; the fence lines are 11 and 80 (`grep -n '^\`\`\`'`); the paste body is line
~~~~

Verdict: MATCHES. The Correction 1 sha 73518316…a263 (block Q).

**P-DL:718,720**

~~~~text
$ sed -n '718,720p' DECISION_LOG.md | cut -c1-160
- [2026-11-08T14:02:11Z] **WHO: amear** | WHAT: **NINE RULINGS R1–R9 FROM HIS 2026-11-08 VOICE SESSION (Claude.ai channel), PLUS A HOUSEKEEPING LIST AND A "STIL
- [2026-11-08T14:22:00Z] WHO: praxis-master | WHAT: **SESSION OPEN; READ DONE; U1 `2026-11-08-rulings-filing` DISPATCHING.** Ledgers read: STATUS.md 11-07 eveni
- [2026-11-08T14:30:00Z] WHO: praxis-master | WHAT: **CORRECTION 1 to rows `14:02:11Z` and `14:22:00Z` and to DISPATCH_LOG `14:24:00Z`: the paste's line range i
~~~~

Verdict: MATCHES. :718 is WHO amear, :719 is praxis-master and :720 is the Correction 1 row. Block Q shows "12–79" at :720. :718 and :719 carry "13-83" with an ASCII hyphen (block R). The entry's "13–83" uses an en dash for the same range.

**P-DSP:2024**

~~~~text
$ sed -n '2024p' DISPATCH_LOG.md | cut -c1-300
- [2026-11-08T14:24:00Z] WHO: praxis-master | WHAT: U1 `2026-11-08-rulings-filing` dispatched — praxis-manager appends D-2026-11-08-A to DECISIONS.md (Amear's R1–R9 of the 2026-11-08 voice session, verbatim by script from `docs/reports/2026-11-08-amear-rulings-voice.md:13-83`; the master's five fili
~~~~

Verdict: MATCHES. The U1 dispatch row. Block R shows it carries "13-83" (ASCII hyphen), as the entry says.

**P-O78:208,219 at 29c3e13**

~~~~text
$ git show 29c3e13:docs/reports/2026-10-31-o78-worker4-report-adversarial.md | sed -n '208,219p' | cut -c1-300
**W4-E6. Rescued trading-hours templates** (regular Sessions block; the first entries in each file are holiday partials)
```
-----CME US Index Futures RTH
TimeZone ['Eastern Standard Time']
[('Monday', '830', 'Monday', '1600'), ('Tuesday', '830', 'Tuesday', '1600'), ('Wednesday', '830', 'Wednesday', '1600'), ('Thursday', '830', 'Thursday', '1600'), ('Friday', '830', 'Friday', '1600')]
-----US Equities RTH
TimeZone ['Eastern Standard Time']
[('Monday', '930', 'Monday', '1600'), ('Tuesday', '930', 'Tuesday', '1600'), ('Wednesday', '930', 'Wednesday', '1600'), ('Thursday', '930', 'Thursday', '1600'), ('Friday', '930', 'Friday', '1600')]
$ stat -f '%N mtime=%Sm' ".../templates/TradingHours/CME US Index Futures RTH.xml" ".../CME US Index Futures ETH.xml"
.../CME US Index Futures RTH.xml mtime=Aug 29 11:52:00 2026
.../CME US Index Futures ETH.xml mtime=Jul  9 10:37:20 2026
```
~~~~

Verdict: MATCHES. CME US Index Futures RTH, Monday–Friday 830–1600, TimeZone Eastern Standard Time (R1, REPORTED BY that worker).

**P-F-headers**

~~~~text
$ grep -n '^### F' specs/SPEC_RUBRIC.md
17:### F1 — Signal-path topology vs. circuit-breaker placement
30:### F2 — Session-flat time vs. breakers #4 and #5
45:### F3 — Backtest fill resolution vs. acquired data granularity
59:### F4 — MFFU automation compliance
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
10	0	specs/SPEC_RUBRIC.md
~~~~

Verdict: MATCHES. F1–F4 are at :17, :30, :45 and :59, and the numstat is "10 0" (S6).

**P-beads**

~~~~text
$ bd show Praxis_build-v6y | head -2 | cut -c1-300
✓ Praxis_build-v6y [BUG] · Gate/concurrency gap: audit token does not bind the staged tree; parallel sessions can inject files into a repo tip write   [● P1 · CLOSED]
Owner: Amear Bani-Ahmad · Assignee: Amear Bani-Ahmad · Type: bug
$ bd show Praxis_build-9lj | head -2 | cut -c1-300
○ Praxis_build-9lj [BUG] · gate-manager-output.sh grades the newest docs/reports/*.md, so concurrent managers get each other's reports graded   [● P2 · OPEN]
Owner: Amear Bani-Ahmad · Type: bug
~~~~

Verdict: MATCHES. The v6y title is verbatim and CLOSED (R7). The 9lj title is verbatim and OPEN (R7).

**P-block-sha**

~~~~text
$ sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ sed -n '1545,1612p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ sed -n '1544p;1613p' DECISIONS.md | sed 's/`/´/g'
´´´text
´´´
[manager note, not output] (backticks in the two fence lines shown as ´ so this block does not break; raw bytes are three U+0060)
~~~~

Verdict: MATCHES. The block body is byte-identical to rulings :12–79 (equal sha). Block Q shows the raw fence bytes as od -c output.



**Block Q: quoted fragments past column 300, checked on the cited line** (`cap2.sh`; each `grep -oF` prints the fragment if it is on that line, or `(no match, rc=1)`)

~~~~text
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF as\ the\ in-sample\ selection\ objective\ only
as the in-sample selection objective only
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF $'For the in-sample sessions i = 1\342\200\246n'
For the in-sample sessions i = 1…n
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF d_i\ =\ sum\ of\ the\ net\ P\&L
d_i = sum of the net P&L
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF after\ commission\ and\ slippage
after commission and slippage
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF trades\ exited\ in\ session\ i
trades exited in session i
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF 0\ if\ none
0 if none
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF $'S = mean(d) / sd(d) \303\227 \342\210\232252'
S = mean(d) / sd(d) × √252
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF $'sd with n \342\210\222 1'
sd with n − 1
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF risk-free\ rate\ 0
risk-free rate 0
$ sed -n 92p docs/specs/2026-11-06-walk-forward-values.md | grep -oF dollar\ P\&L\ at\ 1\ NQ\ needs\ no\ equity\ base
dollar P&L at 1 NQ needs no equity base
$ sed -n 93p docs/specs/2026-11-06-walk-forward-values.md | grep -oF DECISIONS.md:978
DECISIONS.md:978
$ sed -n 132p docs/specs/2026-11-06-walk-forward-values.md | grep -oF DECISIONS.md:978
DECISIONS.md:978
$ sed -n 132p docs/specs/2026-11-06-walk-forward-values.md | grep -o "(ii)[^;]*;\|(iii).*" | cut -c1-200
(ii) whether "Walk-forward efficiency ≥ 0.50" applies to arm (a), which has no optimisation (WF spec NEEDS AMEAR 8) — Q8's words name all six gates for both arms but do not say how WFE is computed
(iii) whether GO / HOLD / REJECT may rest on arm (b) — ruling 9; the O1 gate set, REPORTED BY the return handoff :74 (WF spec NEEDS AMEAR 9).
$ sed -n 135p docs/specs/2026-11-06-walk-forward-values.md | grep -o "Whether it closes.*" | cut -c1-300
Whether it closes the notes-4 item "equity base for the 4% DD gate (item 5)" (DECISIONS.md:978) is NOT decided here; that item stays OPEN (ruling 9; list (C)).
$ sed -n 139p docs/specs/2026-11-06-walk-forward-values.md | grep -oF 1\ NQ\ /\ 1\ MNQ
(no match, rc=1)
$ sed -n 206p docs/specs/2026-11-06-walk-forward-values.md | grep -oF the\ session\'s\ typical-price\ VWAP\ from\ the\ 09:30\ bar
the session's typical-price VWAP from the 09:30 bar
$ sed -n 213p docs/reports/2026-11-08-strategy-filter-audit.md | grep -oF Do\ you\ want\ this\ audit\ filed\ as\ an\ input\ to\ F2\?
Do you want this audit filed as an input to F2?
$ sed -n 67p docs/reports/2026-11-07-return-handoff-claude-ai-2.md | grep -oF whether\ GO\ /\ HOLD\ /\ REJECT\ may\ rest\ on\ arm\ \(b\)
whether GO / HOLD / REJECT may rest on arm (b)
$ sed -n 67p docs/reports/2026-11-07-return-handoff-claude-ai-2.md | grep -oF whether\ gate\ 6\ applies\ to\ arm\ \(a\)
whether gate 6 applies to arm (a)
$ sed -n 978p DECISIONS.md | grep -oF equity\ base\ for\ the\ 4%\ DD\ gate\ \(item\ 5\)\ and\ Sharpe\ definition\ \(item\ 4\)
equity base for the 4% DD gate (item 5) and Sharpe definition (item 4)
$ sed -n 87p docs/reports/2026-11-08-amear-rulings-voice.md | grep -oF If\ the\ T7\ readback\ shows\ 08:30\,\ R1\'s\ re-run\ clause\ fires\ for\ the\ three\ 2026-11-01\ runs.
If the T7 readback shows 08:30, R1's re-run clause fires for the three 2026-11-01 runs.
$ sed -n 86p docs/reports/2026-11-08-amear-rulings-voice.md | grep -oF not\ exist\ yet
not exist yet
$ sed -n 88p docs/reports/2026-11-08-amear-rulings-voice.md | grep -oF names\ the\ same\ checks
(no match, rc=1)
$ sed -n 94p docs/reports/2026-11-08-amear-rulings-voice.md | grep -oF 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ sed -n 3p docs/reports/2026-11-08-amear-rulings-voice.md | grep -o "§6 of[^)]*)"
§6 of `docs/reports/2026-11-08-strategy-filter-audit.md` (questions 1–4)
$ sed -n 718p DECISION_LOG.md | grep -oF $'13\342\200\22383'
(no match, rc=1)
$ sed -n 719p DECISION_LOG.md | grep -oF $'13\342\200\22383'
(no match, rc=1)
$ sed -n 720p DECISION_LOG.md | grep -oF $'12\342\200\22379'
12–79
12–79
12–79
$ sed -n 2024p DISPATCH_LOG.md | grep -oF $'13\342\200\22383'
(no match, rc=1)
$ sed -n 718p DECISION_LOG.md | grep -o "audit §6 Q[1-4]" | sort -u
audit §6 Q1
audit §6 Q2
audit §6 Q3
audit §6 Q4
$ sed -n 719p DECISION_LOG.md | grep -oF research/announcement-drift
research/announcement-drift
$ sed -n 719p DECISION_LOG.md | grep -o "U[2-5] [^;.]\{0,60\}" | cut -c1-90
U2 HOUSEKEEPING — the 12 staged paths (identify each, then un
U3 — VM handoff amendment 2: step-0 line "read the live `CME 
U4 — F2 breaker-values PROPOSAL (R8) as a spec draft, PROPOSE
U5 — R6 research unit on branch `research/announcement-drift`
U5 are dispatched only after U1's entry is OBSERVED on disk by 
$ sed -n 1544p\;1613p DECISIONS.md | od -c | head -2
0000000    `   `   `   t   e   x   t  \n   `   `   `  \n                
0000014
~~~~

Block Q has five `(no match, rc=1)` lines, from three causes. All three are resolved in block R:
- `:139` "1 NQ / 1 MNQ": the entry's shorthand, not a quotation (P-V:139 verdict).
- note 3's "names the same checks": the entry's paraphrase (P-RF:86,90 verdict).
- `13–83` at DECISION_LOG :718, :719 and DISPATCH_LOG :2024: these lines use an ASCII hyphen, `13-83`.

**Block R: follow-up reads and manager re-runs of the adversary's findings** (R1 to R5, in run order; all five are pasted)

R1. In this capture, the three-ledger loop failed: zsh does not word-split `$p`, so `set --` got one argument. Its sed errors are pasted as they ran. The loop was re-run under `bash -c` as R2 and R3.

~~~~text
$ sed -n 139p docs/specs/2026-11-06-walk-forward-values.md | grep -o ".\{0,60\}MNQ.\{0,60\}"
ternative: closed-trade equity only. Changeable by him. **1 MNQ figures** (WF spec NEEDS AMEAR 22, method; and 29) — SETT
LED: derived from the 1 NQ trade list. Per trade, MNQ net = (NQ gross ÷ 10) − $1.90, where NQ gross = NQ net +
 that run's NQ commission. ÷ 10 because MNQ is $2 a point and NQ $20 a point; the 2 ticks/side slippage
 scales the same way. That this equals an own MNQ run is INFERRED. Both 1 NQ and 1 MNQ figures are reported (
item 29). Alternative: an own MNQ run, which needs MNQ data (not on hand, REPORTED BY the unit brief; not checked 
$ grep -n "1 NQ / 1 MNQ" docs/specs/2026-11-06-walk-forward-values.md | cut -c1-12
$ sed -n p DECISION_LOG.md 718 | grep -o '13.\{1,3\}83' | od -c | head -1
sed: DECISION_LOG.md 718: No such file or directory
sed: DECISION_LOG.md 718: No such file or directory
$ sed -n p DECISION_LOG.md 719 | grep -o '13.\{1,3\}83' | od -c | head -1
sed: DECISION_LOG.md 719: No such file or directory
sed: DECISION_LOG.md 719: No such file or directory
$ sed -n p DISPATCH_LOG.md 2024 | grep -o '13.\{1,3\}83' | od -c | head -1
sed: DISPATCH_LOG.md 2024: No such file or directory
sed: DISPATCH_LOG.md 2024: No such file or directory
$ sed -n 88p docs/reports/2026-11-08-amear-rulings-voice.md | cut -c300-900
inition and its equity base were OPEN under ruling 9. R4 fills the gate definition. Whether R4's "equity base = the account size actually traded" also changes the §6 selection statistic, and where R4's win-rate rule applies (the spec's six gates at `:121-127` carry no win-rate gate; win rate appears in the Block 4 ±15% gate, `specs/SPEC_RUBRIC.md:96-97`, O4), is for the filing unit to check and FLAG, not resolve — R4's own instruction.
--- adversary finding 1 re-run
$ sed -n '1534,1543p;1614,1645p' DECISIONS.md | grep -c 'unfreezes'
0
$ sed -n 86p docs/reports/2026-11-08-amear-rulings-voice.md | grep -oF 'still blocking Block 3 and Block 4'
still blocking Block 3 and Block 4
--- adversary finding 2 re-run
$ sed -n '1534,1543p;1614,1645p' DECISIONS.md | grep -c -e 'File each' -e 'one entry' -e 'single entry'
0
--- adversary finding 4 re-run
$ sed -n 2024p DISPATCH_LOG.md | grep -o -e 'R8[^;]\{0,60\}' -e 'F2[^;]\{0,60\}' -e 'FLAGS[^;]\{0,80\}'
FLAGS for Amear, nothing resolved), adds MANIFEST rows for the rulings file, the untr
$ sed -n 719p DECISION_LOG.md | grep -o 'NEEDS AMEAR[^;]\{0,160\}'
$ sed -n 1,8p docs/reports/2026-11-08-rulings-filing-manager.md | grep -o 'NEEDS AMEAR[^.]\{0,200\}'
--- adversary finding 7 re-run
$ sed -n 1625p DECISIONS.md | grep -o 'The master treats R8.\{0,200\}'
The master treats R8 as unblocking a PROPOSAL unit on breakers #2, #3, #4, #5-system and #8, values returned PROPOSED, and NOT as unblocking Block 3 or Block 4 work (F2 "Blocks." :43). Master's reading (filing note 1), c
~~~~


R2. A pattern with the word "lines" in front: it matched nothing, because the ledgers write `:13-83`.

~~~~text
$ sed -n 718p DECISION_LOG.md | grep -o "lines 13.\{1,3\}83" | head -1 | od -c | head -1
$ sed -n 719p DECISION_LOG.md | grep -o "lines 13.\{1,3\}83" | head -1 | od -c | head -1
$ sed -n 2024p DISPATCH_LOG.md | grep -o "lines 13.\{1,3\}83" | head -1 | od -c | head -1
$ sed -n 719p DECISION_LOG.md | grep -o -e "FLAG[^;]\{0,120\}" -e "R8[^;]\{0,100\}" | cut -c1-160
R8 bears on it, see the flag above), F3 (fill resolution
FLAGS not resolutions, MANIFEST rows for the rulings file + the strategy-filter audit (+ its own report)
R8) as a spec draft, PROPOSED, returned to Amear
~~~~


R3. The same loop with an unanchored pattern. It shows the hyphen form at all three lines, and the R8/F2 context on :719.

~~~~text
$ sed -n 718p DECISION_LOG.md | grep -o ".\{0,30\}13.\{1,3\}83.\{0,10\}"
-11-08-amear-rulings-voice.md:13-83` (written
$ sed -n 719p DECISION_LOG.md | grep -o ".\{0,30\}13.\{1,3\}83.\{0,10\}"
script from the rulings file :13-83, the mast
$ sed -n 2024p DISPATCH_LOG.md | grep -o ".\{0,30\}13.\{1,3\}83.\{0,10\}"
-11-08-amear-rulings-voice.md:13-83`; the mas
$ sed -n 719p DECISION_LOG.md | grep -o ".\{0,200\}R8 bears on it" | cut -c1-260
ail through `22:18:00Z`, DISPATCH_LOG tail, DECISIONS.md headers through addendum 2 at :1518, `specs/SPEC_RUBRIC.md` in full (348 lines). FROZEN RESTATED: F1 (topology), F2 (session-flat vs #4/#5 — R8 bears on it
~~~~


R4. Does the original report's Task section (:1–8) name the brief's NEEDS AMEAR limit? This is the re-run for adversary finding 4. It printed nothing: no match.

~~~~text
$ sed -n 1,8p docs/reports/2026-11-08-rulings-filing-manager.md | grep -o -e ".\{0,80\}R8.\{0,120\}" -e ".\{0,60\}FLAG.\{0,100\}" | cut -c1-220
~~~~

R5. The line numbers the adversary cites: rulings :13 and :50, DECISION_LOG :719's "U1 FILING", and DECISIONS.md :1546.

~~~~text
$ sed -n "13p;50p" docs/reports/2026-11-08-amear-rulings-voice.md
WHO: amear. File each as a DECISIONS.md entry citing this session.
R8  F2 unfreezes. Breaker values set for manual trading are redone
$ sed -n 719p DECISION_LOG.md | grep -o "U1 FILING[^;]\{0,60\}" | cut -c1-90
U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9 verbatim by scr
$ sed -n 1546p DECISIONS.md
WHO: amear. File each as a DECISIONS.md entry citing this session.
~~~~


### C1.3 Adversary on the inserted entry: worker `a2b9565bc2e68d666` (praxis-worker, ADVERSARIAL), its own output, verbatim

The brief gave it: the entry (DECISIONS.md :1534–1645), the rulings file, the sources listed in C1.2, S1, S2 and S8 verbatim, and the labelling rule. It did not get the first unit's reasoning or this unit's pointer reads. The block below is the worker's final message exactly as returned. The only change is that the harness's two-space indent was removed from each line. The worker made 12 tool calls and wrote no files. The worker's block contains triple-backtick lines, so it is fenced with `~~~~`.

~~~~text
VERDICT: REFUTED

1. MAJOR: FLAG 6 does not set two texts side by side. DECISIONS.md:1645 (FLAG 6), against the entry's own claim at :1638, "Each flag sets two texts side by side." FLAG 6 reads: "Does R8 change F2's state in `specs/SPEC_RUBRIC.md` — do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition — and is master's reading (filing note 1), changeable by Amear, right? The rubric is his to edit (:3-4). Not resolved here." It quotes nothing. Amear's own words, "F2 unfreezes" (block, rulings file :50), never appear outside the block. They are never set against filing note 1, which says the master "treats F2 as still blocking Block 3 and Block 4 work" (rulings file :86). So the most consequential flag is framed in the rubric's unblock-artifact terms, not his plain words.
```
$ sed -n '1645p' DECISIONS.md | grep -c 'unfreezes'
```
Not run. Evidence that the phrase appears nowhere outside the block: the R8 bullet (DECISIONS.md:1625, quoted in full in my first read) says only "The block carries R8's words on #4 and #5". Block line, file :50: `R8  F2 unfreezes. Breaker values set for manual trading are redone`

2. MAJOR: "File each as a DECISIONS.md entry" is read without a label. Block line DECISIONS.md:1546 (rulings file :13) says `WHO: amear. File each as a DECISIONS.md entry citing this session.` The filing puts all nine rulings in ONE entry, D-2026-11-08-A. No sentence outside the block says so, and nothing labels the one-entry choice as the master's plan (DECISION_LOG :719, "U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9"). That plan line is not cited for this choice.
```
$ sed -n '1534,1645p' DECISIONS.md | grep -n -e 'File each' -e 'each as' -e 'one entry' -e 'single entry'
13:WHO: amear. File each as a DECISIONS.md entry citing this session.
```
(Line 13 of the excerpt is DECISIONS.md:1546, inside the block.) The counter-case: earlier filings such as D-2026-11-06-B also combine several rulings in one entry. Even so, the reading is unlabelled, and the entry says "No ruling is read past its words" (:1617).

3. MINOR: the entry describes filing note 3 as only "names the same checks" (DECISIONS.md:1621: "Master's reading (filing note 3, :88), changeable by Amear, names the same checks."). Note 3 also picks a reading on FLAG 2's subject, and the entry drops it. Rulings file :88: "…were OPEN under ruling 9. R4 fills the gate definition. Whether R4's…". That sentence is not carried or labelled, so the master's lean on FLAG 2 is hidden from Amear.

4. MINOR: one claim about the brief has no pointer. DECISIONS.md:1624 says "this unit's brief limits that list to the R4 flags and the R8/F2 question". The dispatch row names only the R4 flags. DISPATCH_LOG.md:2024 (cut -c1-800): "…the R4-vs-values-spec §6/§8 check written as FLAGS for Amear, nothing resolved…". Nothing on disk that I read says R8/F2 is part of the brief's limit. UNVERIFIED. As a result, R6 "Runs in parallel" vs settlement 9, and R3 vs Q8 (two of Amear's own rulings, :1620), go to the master instead of NEEDS AMEAR.

5. MINOR: some identifications carry no label. They are not marked INFERRED and not quoted from a source.
   - :1620, R2/R3 "*Bear on:* values spec §8 :128 … O1 (`specs/SPEC_RUBRIC.md:74-79`)". The handoff :67 cites only `:132–133` and the maths report; :128 and O1 are the filer's own picks.
   - :1622, R5 "*Bears on:* the higher-win-rate brief requested in …notes-4.md:36". Matching his "higher-win-rate brief" to notes-4 item 1 is the filer's link.
   - :1636, S6 "Interactions: R8↔F2 …; R2/R3↔O1 (:74); R4↔O4 (:94; FLAG 3); R1↔values spec :72 and :206". None of these is labelled.

6. MINOR: FLAG 4 (:1643) quotes only one side. It quotes :93 and :135, but R4's side is a paraphrase ("R4's words name Sharpe and win rate, not the drawdown gate"), with no R4 text.

7. MINOR: in the R8 bullet (:1625), the sentence "The master treats R8 as unblocking a PROPOSAL unit on breakers #2, #3, #4, #5-system and #8 … NOT as unblocking Block 3 or Block 4 work" has no "(filing note 1), changeable by Amear" label. It sits between two labelled sentences.

8. NOTE: the evidence-grades line (:1540) says Amear's words are "the fenced block below and nothing else". The entry then quotes his words outside the block: "(§4 item 3)", "Gate 6 (WFE) applies to arm (b) only", and older rulings such as Q8 and settlement 9's default. All are quotations, so it is wording only.

9. NOTE: R5 is listed as "Answers" audit Q1 (:1622). Q1 proposes "judge by net expectancy, out-of-sample gates and MFFU drawdown survival instead". R5's replacement test is different: "fully rule-based, net positive after costs, … every MFFU condition". The entry does not note that "out-of-sample gates" is missing from R5. It does not adopt Q1's version either.
```
A211: …and judge by net expectancy, out-of-sample gates and MFFU drawdown survival instead?
```

Copy check (attack 2), clean:
```
$ sed -n '12,79p' docs/reports/2026-11-08-amear-rulings-voice.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ sed -n '1545,1612p' DECISIONS.md | openssl dgst -sha256
SHA2-256(stdin)= 73518316d7465c6abc8139d0b3b4192912047e352c43799124436b6c8a1da263
$ sed -n '1544p;1613p' DECISIONS.md
```text
```
```
S13 / S6, clean:
```
$ sed -n '12,79p' <rulings> | grep -c 'Fills are optimistic'  → 0
$ sed -n '1534,1645p' DECISIONS.md | grep -c 'Fills are optimistic'  → 1
$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md  → 10	0	specs/SPEC_RUBRIC.md
```
Beads, clean: v6y title matches verbatim, `[● P1 · CLOSED]`. 9lj title matches verbatim, `[● P2 · OPEN]`. The bd memories `amear-conditional-commitment` and `master-s4-entry-before-code` both exist.

CHECKED-CLEAN:
- values spec: :72, :92 (FLAG 1 ellipsis quote faithful), :93, :121, :121-127, :123, :128, :132 (i)/(ii)/(iii), :133, :134, :135, :137, :139, :206; section headings §4 at :67, §6 at :89, §8 at :119.
- audit: :3, :4, :88, :127, :144, :165, :175 (the two §5 candidates = R6's two studies), :211, :212, :213 ("Do you want this audit filed as an input to F2?"), :214.
- rubric: :3-4, :17, :30, :41-42, :43, :45, :59, :74-79, :94, :96-97 ("±15% win rate" is at :97).
- return handoff: :61-65, :65 (both bears-on pointers), :67 (all three sub-parts quoted).
- notes-4: :35, :36.
- DECISIONS.md: :736, :748, :752, :814, :948 (marked "reading (voice agent)"), :978, :1092 (column 3 is the master's under R-1104-2, confirmed by the table preamble).
- vm/replies/README.md:7; vm/2026-11-06-vm-handoff.md:37.
- DECISION_LOG :718 (13-83; per-ruling "audit §6 Q1–Q4" mapping present), :719 (13-83; U2–U5 contents and the U5-after-MFFU-T1 order), :720.
- DISPATCH_LOG :2024 (13-83).
- 29c3e13 o78 report :208-219 (830–1600, Eastern Standard Time).
- rulings file :3, :9, :86-90 (notes 1–5 at the stated lines), :94 (Correction 1 sha).
- The block is byte-identical (sha above).
- Status words RECORDED / OBSERVED / UNVERIFIED / CLOSED / OPEN were not raised above what their sources support.
~~~~

**Manager stress-test of the adversary's block.** This is the manager's reading; the evidence is in block R.
- Finding 1 (MAJOR). The adversary's own command for this finding says "Not run". The manager ran a wider version in R1: `sed -n '1534,1543p;1614,1645p' DECISIONS.md | grep -c 'unfreezes'` gives `0`, so "F2 unfreezes" appears nowhere in the entry outside the block. R5 shows rulings :50 carries `R8  F2 unfreezes`. R1 shows filing note 1 (:86) carries "still blocking Block 3 and Block 4". The finding REPRODUCES: FLAG 6 does not set Amear's "F2 unfreezes" beside note 1's reading.
- Finding 2 (MAJOR). R1: the same out-of-block range gives `0` for 'File each' / 'one entry' / 'single entry'. R5: rulings :13 and DECISIONS.md :1546 both read "File each as a DECISIONS.md entry citing this session", and DECISION_LOG :719 reads "U1 FILING — D-2026-11-08-A in DECISIONS.md: R1–R9". The finding REPRODUCES. The one-entry filing of nine rulings is the master's plan; the entry neither labels nor cites that choice.
- Finding 3 (MINOR). R1 pastes :88's tail. Note 3 carries "R4 fills the gate definition", and the entry's "names the same checks" does not carry it. The finding REPRODUCES.
- Finding 4 (MINOR). R1: DISPATCH_LOG :2024 names "FLAGS for Amear" for the R4 check only. R4: the original report's Task section has no such limit. The R8/F2 half of the entry's ":1624 brief limits that list" claim has no on-disk source this unit found. The finding REPRODUCES as UNVERIFIED. The U1 brief may have said it in the master's dispatch message, which is not on disk; this unit did not see that message.
- Finding 7 (MINOR). R1 shows the sentence as quoted. The finding REPRODUCES.
- Findings 5, 6, 8, 9 are about how the entry's own text is worded or labelled. The manager did not re-run them past the entry text pasted in C1.2 and the adversary's quotes. They are NOT independently reproduced here.
- The adversary's copy check, S13 check and bead check match this unit's own P-block-sha, P-F-headers and P-beads pastes.

**Disposition (item 3 of the brief).** The adversary's verdict is REFUTED. Two MAJOR findings (1, 2) reproduce on the manager's re-run. Lines 1534–1645 of DECISIONS.md were NOT edited by this unit. The cure is the master's to dispatch: a further append to DECISIONS.md (a correction to D-2026-11-08-A). It would need to (a) set "F2 unfreezes" beside filing note 1 inside FLAG 6, and (b) label the one-entry filing as the master's plan with a pointer to DECISION_LOG :719. It could also carry findings 3, 4 and 7. Whether one entry satisfies "File each", and whether F2 unfreezes, are Amear's questions (S8). This unit answers neither.

### C1.4 The earlier worker figures are descriptions under S1

The original report's "Workers dispatched" table (:9–16) and "Adversarial findings" (:193–197) give worker outcomes, such as counts of MAJOR and MINOR findings and "CHECKED-CLEAN in all three rounds". Those workers' blocks were NOT pasted, so under S1 they are DESCRIPTIONS, not evidence. This unit does not reconstruct or invent their output. For grading purposes, the fresh adversary block in C1.3 is the pasted worker evidence that replaces them. C1.2 and block Q replace the claim at :194 ("Every pointer was CHECKED-CLEAN in all three rounds") and the entry's "each re-read with `sed -n` this session (OBSERVED)". Note: :193–197 describes three adversarial rounds, all `VERDICT: REFUTED`, and says the fixes were applied after each one (the manager read :9–16 and :193–197 this unit with `sed -n`, cut at 400 characters). Against the entry as it now stands, this unit's adversary still finds two MAJOR defects (C1.3). This unit does not establish which is true: the fixes brought those defects in, or the earlier rounds missed them.

### C1.5 Index and tree checks (pasted)

Before: see C1.1 (index `12 files changed, 5726 insertions(+), 2 deletions(-)`; porcelain 5 lines; `wc -l` 221; prefix sha `fd44d077…58a8`).

After:

~~~~text
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git status --porcelain | grep -E 'DECISIONS|MANIFEST|2026-11-08'
 M DECISIONS.md
 M MANIFEST.md
?? docs/reports/2026-11-08-amear-answers-flags.md
?? docs/reports/2026-11-08-amear-rulings-voice.md
?? docs/reports/2026-11-08-rulings-filing-manager.md
?? docs/reports/2026-11-08-strategy-filter-audit.md
$ wc -l docs/reports/2026-11-08-rulings-filing-manager.md
    1060 docs/reports/2026-11-08-rulings-filing-manager.md
$ head -n 221 docs/reports/2026-11-08-rulings-filing-manager.md | shasum -a 256
fd44d0771dbba38a070dc2459091fb2873a8d952bd1c42de9c65963a6e5b58a8  -
$ sed -n '1534,1645p' DECISIONS.md | shasum -a 256; git rev-parse --short HEAD
97423fc6b4eaa8fbca5efece744a221557c34fe2a87343a6e6e9652ef8a817ee  -
6c233d1
$ # negative test, scratch copy only: flip one byte on line 5, re-hash the prefix
$ cp docs/reports/2026-11-08-rulings-filing-manager.md $S/neg.md && sed -i '' '5s/^/X/' $S/neg.md && head -n 221 $S/neg.md | shasum -a 256
849c75a6de166bada7b18fdf56051ee3cb2d804a39aea63344129bc6a5d11d22  -
~~~~

**P-HANDOFF:7** (pointer in the entry's HOUSEKEEPING paragraph, DECISIONS.md:1628; it restates his item; captured late, after C1.5)

~~~~text
$ sed -n '7p' HANDOFF.md | cut -c1-300   (LC_ALL=en_US.UTF-8)
**Gate route — what works, OBSERVED today by the master (REPORTED BY master in the rows named; where no row is named, the source is the master's dispatch brief to this unit only, and this unit found no ledger row by `grep`). These were meant for `bd remember`; three attempts with `>` in the body wer
$ sed -n 1628p DECISIONS.md | grep -o 'HANDOFF.md line 7[^;]*'
HANDOFF.md line 7, append-only
$ sed -n '7p' HANDOFF.md | grep -o -e 'bd remember.\{0,120\}' | head -1
bd remember`; three attempts with `>` in the body were denied, so they live here:**
~~~~

Verdict: MATCHES. The entry only names "HANDOFF.md line 7, append-only" as his housekeeping item, which is his words. Line 7 is the gate-route paragraph and carries "meant for `bd remember`; three attempts … wer[e]", the save-failed text his item refers to. The entry makes no claim about it beyond his item.


**Observer note.** The `wc -l` above (1060) was taken before this note and the lines after it were appended, so it is lower than the final count. The prefix sha is the figure that matters, and it is unchanged: `fd44d077…58a8` before and after. In the negative test, one byte changed on line 5 of a scratch copy moves the prefix sha to `849c75a6…1d22`. The append-only check therefore does catch an in-prefix edit. The index line is unchanged: `12 files changed, 5726 insertions(+), 2 deletions(-)`. Porcelain shows one path that was not there before, `?? docs/reports/2026-11-08-amear-answers-flags.md`. This unit did NOT create it. Its line 1 reads "AMEAR'S ANSWERS A1–A11 TO THE D-2026-11-08-A FLAGS"; line 3 reads "Filed verbatim by praxis-master … received while the U1 correction unit was running". `stat` shows mtime 2026-11-08T09:46:12 local, which is 14:46Z. The adversary was read-only and created no scratch directory. This unit did not read that file past its first four lines. Whether it settles FLAGS 1–6 or adversary findings 1–2 is for the master to check. The DECISIONS.md :1534–1645 sha (`97423fc6…17ee`) was not taken at the start of this unit, so it is not offered as a before/after proof. The proof that the entry was not edited is that this unit has no write to DECISIONS.md, and that its block sha is still `73518316…a263` (P-block-sha).

Result: PASS at level WRITTEN, for this unit's scope: the S1 cure of this report. Every pointer D-2026-11-08-A makes outside its fenced block is pasted with a verdict (C1.2, blocks Q and R). The fresh adversary block is pasted verbatim (C1.3). The earlier worker figures are restated as DESCRIPTIONS (C1.4). Index and prefix checks are pasted (C1.5). The ARTIFACT that this report files, D-2026-11-08-A, is REFUTED by this unit's adversary on two MAJOR counts that reproduce on re-run (C1.3 findings 1 and 2). This unit does not cure them. The cure is the master's to dispatch, as a further DECISIONS.md append.

**Does NOT cover (Correction 1).**
- Any edit to DECISIONS.md :1534–1645, or any DECISIONS append. Adversary findings 1–7 stay open for the master.
- Whether one entry satisfies "File each as a DECISIONS.md entry", and whether "F2 unfreezes" changes F2's rubric state. Both are Amear's (S8).
- The new master file `docs/reports/2026-11-08-amear-answers-flags.md` and anything it rules.
- Independent reproduction of adversary findings 5, 6, 8 and 9.
- Reconstruction of the earlier W1–W4 worker output; it was not pasted and is not recoverable from this report.
- MANIFEST, ledgers, STATUS, HANDOFF, specs, vm, `.claude/`, the rulings file and the strategy filter audit: none was touched.
- A self-grade. The auditor grades this.
