# 2026-11-09 — unit `2026-11-09-rubric-unit` — praxis-manager report

## Task

D12 of D-2026-11-08-D orders this unit: "rubric unit (C2, C6, C8, and D1-D5 as a new "Autonomy" section)" (DECISIONS.md :1961–1962, pasted in the D-2026-11-08-D verbatim block). Four edits to `specs/SPEC_RUBRIC.md`, one appended MANIFEST.md row, this report. Brief from praxis-master; working tree `main` at HEAD `10354e5`. Nothing staged, committed or reset by this unit (brief standing rule 4).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

(The sentence above is the S13 house-style line. This report states no backtest or P&L figure.)

## Rubric criteria addressed

- S1: every claim below rests on pasted command output (sections "Verification evidence", "Final block", "Diff of record").
- S2: the C2 text records the exemption as RULED and NOT YET BUILT; the level claimed for this unit is WRITTEN (text edited and checked), not more.
- S4 / S5: each edit cites its ledger authorisation inline: C2, C6 and C8 under D-2026-11-08-C (DECISION_LOG `2026-11-08T19:12:30Z`, WHO: amear); D1–D5 under D-2026-11-08-D (DECISION_LOG `2026-11-08T19:57:00Z`, WHO: amear). Both entries were in DECISIONS.md, committed, before this unit began (`git status --porcelain -- DECISIONS.md` is empty, pasted below; the entries are at DECISIONS.md :1808 and :1891). The layout (minimum line shift; PASSED section above OPEN; Autonomy at the end) was decided by the master under D-2026-11-08-D D1, DECISION_LOG `2026-11-09T13:54:00Z` (working tree only, line 761, not in HEAD; pasted below).
- S6: see "S6 cross-block check".
- S8: the S8 table row is not edited; the S8 sentence added is the one the brief supplies, labelled as the master's reading.
- S13: the sentence appears once in this report, above. The rubric already carries it once inside S13 and no second copy was added (count pasted below).
- Header rule (rubric :3–6): every edit cites a logged Amear approval inline (see the diff of record).

## Workers dispatched

| id | mode | outcome |
|---|---|---|
| a3a28be59674ead34 (ADV1) | ADVERSARIAL, read-only, on the first installed version (412 lines) | `GRADE: NOT REFUTED`; 2 MINOR. Finding 1 led to one wording fix (below). |
| a64b978c986233a2f (ADV2) | ADVERSARIAL, read-only, on the final file (413 lines) and MANIFEST.md | `GRADE: NOT REFUTED`; 3 MINOR, none fixed in the rubric (reasons below). |

Both ran foreground (`run_in_background: false`), wrote nothing in the repo by their own account, and were told to write nothing under `.claude/agent-memory/`. No BUILD worker: the edits are a scripted doc transformation done by the manager (one Python script, `/tmp/rubric-unit/build.py`, reading the quotes from their source files by line number), so the quotes are never retyped.

## Process log

1. Captured the baseline before any edit: `wc -l` 355, HEAD 345, numstat `10 0`, the C8 hunk (pasted below). The hunk holds the R-A/R-B/R-C "No-verdict returns" text and nothing else, so C8 went ahead.
2. Snapshot of the pre-unit file copied to `/tmp/rubric-unit/rubric-before.md` (sha256 `bffddb6a…` taken before the copy, and identical after it); C8 lines 275–284 saved to `/tmp/rubric-unit/c8-before.txt`.
3. Built the new file in `/tmp` with `build.py`, checked it, and installed it with one `cp` (412 lines).
4. ADV1 on that file. MINOR 1: "still admits only a PASS-minted token" left out that the gate only checks while armed (hook :110). Fix: the words "whenever it is armed" were added, by editing `build.py` and rebuilding from the same snapshot. The rebuilt file differs from the ADV1-checked file only in that sentence (diff pasted below). Installed with a second `cp` (413 lines).
5. MANIFEST row 316 appended; then corrected in place from "now 412" to "now 413" after the fix (only line 316 written; lines 1–315 hash-equal before and after, pasted).
6. ADV2 on the final file. No further edit to the rubric.
7. Evidence re-captured after the last rubric edit; final block and diff of record captured after the last edit to any file except this report.

## Decisions taken in this unit

Each was decided by the manager under D-2026-11-08-D D1 and can be changed by Amear.

1. Where C2 goes: after the "*Note for whoever installs this:*" paragraph, not before it. Both places are next to the park rule. Putting it after the note leaves the note's five lines where they are, so less moves. The cost: the C8 hunk's first neighbour is now the C2 paragraph, not the note. The C8 lines themselves and the line after them are unchanged (hashes below).
2. How C6 is quoted: the brief allows one line, so the two source lines are joined with one space, inside a code span. The code span is used because the quote contains double quotes.
3. Three provenance lines, each labelled "Filer's note, not a ruling". They give the source line range of each scripted quote (C6, C2, D1–D5).
4. ADV2 MINOR (g) was not fixed in the rubric. Reasons are under "Adversarial findings".

## Verification evidence

### Before any edit (captured at unit start, pasted from that tool output)

~~~~
$ git rev-parse --short HEAD && wc -l specs/SPEC_RUBRIC.md && git show HEAD:specs/SPEC_RUBRIC.md | wc -l && git diff --numstat HEAD -- specs/SPEC_RUBRIC.md && git diff HEAD -- specs/SPEC_RUBRIC.md && wc -l MANIFEST.md && head -n 315 MANIFEST.md | openssl dgst -sha256 && ls docs/reports/2026-11-09* 2>/dev/null
10354e5
     355 specs/SPEC_RUBRIC.md
     345
10	0	specs/SPEC_RUBRIC.md
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index e1963d6..fa31f03 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -272,6 +272,16 @@ blocked, move on" wording. It is outside this repository and affects other
 projects, so it is **not** edited from here. This section is the binding text for
 PRAXIS work.

+**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
+row `2026-07-27T18:15Z`.**
+
+A grading agent that returns no explicit verdict has not graded. Absence of a
+verdict is treated as FAIL for the commit decision and never as PASS or as
+no-finding. It does NOT count toward the park rule's two-strike limit, which
+counts adverse verdicts on the work. A no-verdict unit may be re-dispatched only
+after material reduction, stated in the dispatch row; a second consecutive
+no-verdict return on the same bead counts as the second FAIL.
+
 **Absolutes are amended between sessions only — 2026-07-26 human ruling.**

 A rule declared absolute is **never amended inside the session that hits it.**
     315 MANIFEST.md
SHA2-256(stdin)= fea161a54d1628fa10188d26ffb6525db00b89953b0c10e4f5d108b2adb7042c
docs/reports/2026-11-09-c-d-filing-manager.md
docs/reports/2026-11-09-c-d-filing-resume-manager.md
docs/reports/2026-11-09-d11-sweep-manager.md
docs/reports/2026-11-09-d6-drawdown-check-manager.md
docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md

$ (excerpt of a longer command line; this part shown) sed -n '275,284p' specs/SPEC_RUBRIC.md > /tmp/rubric-unit/c8-before.txt; openssl dgst -sha256 /tmp/rubric-unit/c8-before.txt; git diff HEAD -- specs/SPEC_RUBRIC.md | grep '^+' | grep -v '^+++' | sed 's/^+//' | openssl dgst -sha256; openssl dgst -sha256 specs/SPEC_RUBRIC.md; cp specs/SPEC_RUBRIC.md /tmp/rubric-unit/rubric-before.md
SHA2-256(/tmp/rubric-unit/c8-before.txt)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(specs/SPEC_RUBRIC.md)= bffddb6a9b78a7349251c7abd8f4d0ae9dfb6a5ec2b288cc35972d6b3dd869e2
~~~~

The 10 added lines (275–284) are the "No-verdict returns" paragraph pair and nothing else. Re-derived from the snapshot (captured by `/tmp/rubric-unit/capture.sh before`):

~~~~
$ openssl dgst -sha256 /tmp/rubric-unit/rubric-before.md
SHA2-256(/tmp/rubric-unit/rubric-before.md)= bffddb6a9b78a7349251c7abd8f4d0ae9dfb6a5ec2b288cc35972d6b3dd869e2
[exit 0]

$ wc -l /tmp/rubric-unit/rubric-before.md
     355 /tmp/rubric-unit/rubric-before.md
[exit 0]

$ git hash-object /tmp/rubric-unit/rubric-before.md
fa31f03448fee446306e2bd5732896e883c6977b
[exit 0]

$ git show HEAD:specs/SPEC_RUBRIC.md > /tmp/rubric-unit/head.md; wc -l /tmp/rubric-unit/head.md; git hash-object /tmp/rubric-unit/head.md
     345 /tmp/rubric-unit/head.md
e1963d68479449b6ffc24cf353a08f2e9ba7da1d
[exit 0]

$ diff -u /tmp/rubric-unit/head.md /tmp/rubric-unit/rubric-before.md
--- /tmp/rubric-unit/head.md	2026-11-09 09:02:03
+++ /tmp/rubric-unit/rubric-before.md	2026-11-09 08:56:19
@@ -271,6 +271,16 @@
 blocked, move on" wording. It is outside this repository and affects other
 projects, so it is **not** edited from here. This section is the binding text for
 PRAXIS work.
+
+**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
+row `2026-07-27T18:15Z`.**
+
+A grading agent that returns no explicit verdict has not graded. Absence of a
+verdict is treated as FAIL for the commit decision and never as PASS or as
+no-finding. It does NOT count toward the park rule's two-strike limit, which
+counts adverse verdicts on the work. A no-verdict unit may be re-dispatched only
+after material reduction, stated in the dispatch row; a second consecutive
+no-verdict return on the same bead counts as the second FAIL.
 
 **Absolutes are amended between sessions only — 2026-07-26 human ruling.**
 
[exit 1]

~~~~

### The ADV1 fix: what changed between the ADV1-checked file and the final file

The ADV1-checked file is `/tmp/rubric-unit/rubric-final-for-adv.md`, copied right after the first install. When ADV1 was dispatched, the live file's sha256 was `a401c8bc…262f` (same hash as that copy). The only difference from the final file is the fix:

~~~~
$ diff /tmp/rubric-unit/rubric-final-for-adv.md specs/SPEC_RUBRIC.md
296,297c296,298
< still admits only a PASS-minted token, the gate change is a later, trip-tested
< unit (D-2026-11-08-D D12: "park-commit gate exemption (C2, trip-tested)"), and
---
> still admits only a PASS-minted token whenever it is armed, the gate change is a
> later, trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
> trip-tested)"), and
[exit 1]
$ openssl dgst -sha256 /tmp/rubric-unit/rubric-final-for-adv.md
SHA2-256(/tmp/rubric-unit/rubric-final-for-adv.md)= a401c8bc4b49a9f11a0b6b289e30e1d13a59abd33ab010805472c33fe4ae262f
~~~~

### After the last rubric edit (captured by `/tmp/rubric-unit/capture.sh after`)

How to read the `diff <(git show HEAD:…) specs/SPEC_RUBRIC.md` hunks below, one at a time:
- `74c74`: HEAD's `## OPEN — gradeable now` becomes `## PASSED — closed criteria` (C6). This is the only HEAD-side line removed.
- `75a76,77`: the C6 line, plus a blank line.
- `88a91,94`: blank, `---`, blank, `## OPEN — gradeable now`. This is the OPEN heading and separator, moved to sit after O1 (C6). diff lines the blank lines up one place differently from how the script inserted them (after HEAD :88). The content is the same either way: O1's last line, blank, `---`, blank, OPEN heading, blank, `### O2`.
- `274a281,310`: lines 281–300 are the C2 block (20 lines). Lines 301–310 are the C8 hunk, byte-for-byte.
- `345a382,413`: the Autonomy section (blank line, heading, blank line, note, blank line, fenced D1–D5, blank line, S8 reading sentence).

The rebuild check deletes the inserted ranges (76–77, 90–93, 281–310, 382–413) and puts the OPEN heading back at 74. Its sha256 equals HEAD's. So every HEAD line is still present, in order, and only the OPEN heading has moved.

~~~~
$ date -u
Mon Nov  9 14:07:53 UTC 2026
[exit 0]

$ wc -l specs/SPEC_RUBRIC.md
     413 specs/SPEC_RUBRIC.md
[exit 0]

$ git show HEAD:specs/SPEC_RUBRIC.md | wc -l
     345
[exit 0]

$ grep -n '^## ' specs/SPEC_RUBRIC.md
17:## FROZEN — nothing downstream may proceed until these clear
74:## PASSED — closed criteria
93:## OPEN — gradeable now
117:## Standing criteria — graded on every dispatch
250:## Process rulings — binding on the orchestrator
383:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
[exit 0]

$ diff <(git show HEAD:specs/SPEC_RUBRIC.md) specs/SPEC_RUBRIC.md | grep '^[0-9]'
74c74
75a76,77
88a91,94
274a281,310
345a382,413
[exit 0]

$ diff <(git show HEAD:specs/SPEC_RUBRIC.md) specs/SPEC_RUBRIC.md | grep '^<'
< ## OPEN — gradeable now
[exit 0]

$ diff <(git show HEAD:specs/SPEC_RUBRIC.md) specs/SPEC_RUBRIC.md | grep -c '^>'
69
[exit 0]

$ sed -e '76,77d' -e '90,93d' -e '281,310d' -e '382,413d' -e '74s/^## PASSED — closed criteria$/## OPEN — gradeable now/' specs/SPEC_RUBRIC.md | openssl dgst -sha256; git show HEAD:specs/SPEC_RUBRIC.md | openssl dgst -sha256
SHA2-256(stdin)= 16a7f819c776adf9002234d4ef24aa5a9a2743461204594cd24ee7253b67341b
SHA2-256(stdin)= 16a7f819c776adf9002234d4ef24aa5a9a2743461204594cd24ee7253b67341b
[exit 0]

$ sed -n '301,310p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; openssl dgst -sha256 /tmp/rubric-unit/c8-before.txt; sed -n '275,284p' /tmp/rubric-unit/rubric-before.md | openssl dgst -sha256
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(/tmp/rubric-unit/c8-before.txt)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
[exit 0]

$ sed -n '300p;311p' specs/SPEC_RUBRIC.md; git show HEAD:specs/SPEC_RUBRIC.md | sed -n '275p'

**Absolutes are amended between sessions only — 2026-07-26 human ruling.**
**Absolutes are amended between sessions only — 2026-07-26 human ruling.**
[exit 0]

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '76,87p' | openssl dgst -sha256; sed -n '78,89p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '78p;89p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= 89d1118a7c9cf30612d90d0cb580070c0edfd78c3510fc62cd7b103b03b18bd8
SHA2-256(stdin)= 89d1118a7c9cf30612d90d0cb580070c0edfd78c3510fc62cd7b103b03b18bd8
### O1 — Walk-forward gate set for the replication arm
replication arm or the later optimisation arm.
[exit 0]

$ sed -n '1906,1927p' DECISIONS.md | openssl dgst -sha256; sed -n '389,410p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '16,37p' docs/reports/2026-11-08-amear-rulings-voice-2.md | openssl dgst -sha256; sed -n '388p;411p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= 1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9
SHA2-256(stdin)= 1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9
SHA2-256(stdin)= 1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9
```text
```
[exit 0]

$ sed -n '19,22p' docs/reports/2026-11-08-amear-answers-park-card.md | openssl dgst -sha256; sed -n '287,290p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '286p;291p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= e6d0f71b21d224168b82768342cd03dd25bd3e20d7d24c3863a96d58885a2cd0
SHA2-256(stdin)= e6d0f71b21d224168b82768342cd03dd25bd3e20d7d24c3863a96d58885a2cd0
```text
```
[exit 0]

$ sed -n '34,35p' docs/reports/2026-11-08-amear-answers-park-card.md | sed '1s/^C6  //;2s/^ *//' | paste -sd' ' -; sed -n '76p' specs/SPEC_RUBRIC.md | grep -o '`"Discharged.*`$'
"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.
`"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
[exit 0]

$ git status --porcelain -- DECISIONS.md docs/reports/2026-11-08-amear-answers-park-card.md docs/reports/2026-11-08-amear-rulings-voice-2.md .claude/hooks/gate-commit.sh; echo status-done
status-done
[exit 0]

$ /usr/bin/grep -n -i 'park' .claude/hooks/gate-commit.sh; echo grep-exit=$?; sed -n '108,110p' .claude/hooks/gate-commit.sh
grep-exit=1
ROOT="${CLAUDE_PROJECT_DIR:-.}"
STATE="$ROOT/.claude/state"
[ -f "$STATE/orchestrator-active" ] || exit 0
[exit 0]

$ grep -n '^| S8 |' specs/SPEC_RUBRIC.md; git show HEAD:specs/SPEC_RUBRIC.md | grep -n '^| S8 |'
128:| S8 | No question that belongs to Amear is answered on his behalf. |
122:| S8 | No question that belongs to Amear is answered on his behalf. |
[exit 0]

$ grep -c 'Fills are opt[i]mistic; Standard resolution on 1-minute bars' specs/SPEC_RUBRIC.md; git show HEAD:specs/SPEC_RUBRIC.md | grep -c 'Fills are opt[i]mistic; Standard resolution on 1-minute bars'
1
1
[exit 0]

$ for t in 2026-11-08T19:12:30Z 2026-11-08T19:57:00Z 2026-11-09T13:54:00Z 2026-07-27T18:15Z; do printf '%s HEAD=%s WT=%s line=%s\n' "$t" "$(git show HEAD:DECISION_LOG.md | grep -c "^- \[$t\]")" "$(grep -c "^- \[$t\]" DECISION_LOG.md)" "$(grep -n "^- \[$t\]" DECISION_LOG.md | cut -d: -f1)"; done
2026-11-08T19:12:30Z HEAD=1 WT=1 line=743
2026-11-08T19:57:00Z HEAD=1 WT=1 line=744
2026-11-09T13:54:00Z HEAD=0 WT=1 line=761
2026-07-27T18:15Z HEAD=1 WT=1 line=89
[exit 0]

$ grep '^- \[2026-11-08T19:12:30Z\]' DECISION_LOG.md | cut -c1-120; grep '^- \[2026-11-08T19:57:00Z\]' DECISION_LOG.md | cut -c1-120
- [2026-11-08T19:12:30Z] **WHO: amear** | WHAT: **C1–C10, ANSWERS TO THE 2026-11-08 PARK CARD, pasted by Amear (from the
- [2026-11-08T19:57:00Z] **WHO: amear** | WHAT: **D1–D12, VOICE SESSION 2 (Claude.ai channel), pasted by Amear while U8 
[exit 0]

$ wc -l MANIFEST.md; head -n 315 MANIFEST.md | openssl dgst -sha256; git show HEAD:MANIFEST.md | sed -n '307p' | openssl dgst -sha256; sed -n '315p' MANIFEST.md | openssl dgst -sha256; sed -n '316p' MANIFEST.md
     316 MANIFEST.md
SHA2-256(stdin)= fea161a54d1628fa10188d26ffb6525db00b89953b0c10e4f5d108b2adb7042c
SHA2-256(stdin)= f57376e5c86edb6e76d2e83ffa6d30af4939cc1576641f43efc2b396e81869fd
SHA2-256(stdin)= f57376e5c86edb6e76d2e83ffa6d30af4939cc1576641f43efc2b396e81869fd
| /docs/reports/2026-11-09-rubric-unit-manager.md | Report | 2 | 2026-11-09 | Manager report for unit 2026-11-09-rubric-unit (Amear D-2026-11-08-D D12; C2, C6, C8 of D-2026-11-08-C; D1-D5 of D-2026-11-08-D): specs/SPEC_RUBRIC.md edited (HEAD 345 lines, now 413): the July R-A/R-B/R-C hunk landed byte-for-byte (C8); O1 moved under a new "PASSED — closed criteria" heading (C6); the C2 park-commit exemption quoted and recorded as RULED and NOT YET BUILT; a new Autonomy section with D1-D5 copied by script; untracked (`??`) at time of row, ungraded |
[exit 0]

~~~~

## Adversarial findings

### ADV1 (a3a28be59674ead34), on the first installed version. Its returned text, verbatim:

~~~~
I could not refute the claim. The working-tree rubric differs from HEAD by the four permitted edits and nothing else, and every quote is verbatim. I found two minor defects and no major one.

**(a) C8 hunk: byte-identical.** The snapshot hash checks out, and the snapshot differs from HEAD only by the 10-line hunk. Removing the added lines from the working tree reproduces the snapshot exactly:
```
bffddb6a...dd869e2  /tmp/rubric-unit/rubric-before.md
bffddb6a...dd869e2  recon_before.md
RECON==BEFORE
BEFORE-minus-C8==HEAD
```
The surrounding text is unchanged. The park note's "PRAXIS work." is still followed by the hunk, now with the C2 block in between. "**Absolutes are amended…" still comes straight after it.

**(b) O1 block: byte-identical.** The same rebuild proves it. In the diff, O1's lines appear only as unchanged context (`74c74,76` and `88a91,94` are the only hunks near it).

**(c) Quotes: all verbatim.**
- C2: `e6d0f71b...a2cd0` for both the source and the working tree, `C2-IDENTICAL`.
- C6: identical after joining the two lines, `C6-MATCH`.
- D1–D5: `1e402342...5b5d9` for both, `D1D5-IDENTICAL`.
- D12: the quote is in DECISIONS.md at :1963–1964 (joined) and :1986.
- The three headings and the S8 sentence match the brief byte for byte (the S8 sentence hashes `fb196292…` on both sides).
- DECISIONS.md and the answers file are clean against HEAD.

**(d) Labels: every non-quote sentence is labelled.**
- Line 76: "Filer's note, not a ruling".
- Lines 283–284: "Filer's note, not a ruling".
- Lines 293–298: "State of the build (filer's statement, not a ruling…)".
- Lines 384–385: "Filer's note, not a ruling".
- Line 412: "(master's reading…)".
- The rest are headings or `---`. No sentence is unlabelled.

**(e) Nothing else moved.** The only line removed from HEAD is line 74 `## OPEN — gradeable now`. Rebuilding the snapshot, then removing C8, gives HEAD (both lines shown under (a)).

**(f) Ledger rows: both exist and are committed in HEAD** (`count=2`):
```
743:- [2026-11-08T19:12:30Z] **WHO: amear** | WHAT: **C1–C10, ANSWERS TO THE 2026-11-08 PARK CARD…
744:- [2026-11-08T19:57:00Z] **WHO: amear** | WHAT: **D1–D12, VOICE SESSION 2…
```
Row 743 contains `D-2026-11-08-C`.

**(g) Defects.**
- **MINOR: the hook claim is too broad.** The text says gate-commit.sh "still admits only a PASS-minted token" with no condition. The hook only checks while a state file exists (line 110: `[ -f "$STATE/orchestrator-active" ] || exit 0`). With that file absent, any commit goes through without a token. When the gate is checking, the claim holds: line 647 requires an AUDIT_LOG PASS row, and line 629 says the stack master needs "only a praxis-auditor PASS". The rest of the sentence also holds. The hook has no park exemption (`grep -i park` found nothing, exit 1). Park step 1 is "Commit the work to a branch `parked/<bead-id>`", and the master can't do that without a PASS token. The text does not claim bead Praxis_build-8sw is closed.
- **MINOR: C8 is never cited by name.** Searching the file for `C8` finds nothing. The hunk does cite DECISION_LOG row 89 (`2026-07-27T18:15Z … APPROVED BY: amear`), so the header rule is arguably met. A cite inside the hunk was impossible anyway, since it had to land byte-for-byte.

Two process notes:
- One of my read-only greps was blocked by mint-guard because it named a token-minting script. I did not try another route, so the legacy token-minting route is UNVERIFIED beyond what gate-commit.sh shows.
- "Copied by script" in the filer's notes is UNVERIFIED as to method; the content matches.

Scratch files are in `/tmp/rubric-adv/` (head.md, wt.md, recon_before.md, before_minus_c8.md, c2_src.txt, c2_wt.txt, d_src.txt, d_wt.txt). Nothing in the repo was written.

GRADE: NOT REFUTED
Result: PASS
~~~~

ADV1 shortened its hashes in its own text. The full values for the same checks are in the manager's re-run above.

### ADV2 (a64b978c986233a2f), on the final file and MANIFEST.md. Its returned text, verbatim. The spoken-summary block it added after its last line is left out.

~~~~
I could not refute the claim. The rubric differs from HEAD by exactly the four permitted edits, every quote matches its source by hash, and the MANIFEST conditions all hold. I found three MINOR defects and no MAJOR ones.

**(a) C8 hunk.** The snapshot is intact: sha256 `bffddb6a9b78a7349251c7abd8f4d0ae9dfb6a5ec2b288cc35972d6b3dd869e2`, blob `fa31f03448fee446306e2bd5732896e883c6977b`, HEAD blob `e1963d68479449b6ffc24cf353a08f2e9ba7da1d`. That matches the recorded start-of-unit index line. The snapshot differs from HEAD only by `273a274,283` (the 10-line hunk). Hashes:
```
sed -n '274,283p' before  -> 58671c1d1b1541c561ded276c254bb56d8131da01006ba23ea8b7c7a4472f647
sed -n '300,309p' working -> 58671c1d1b1541c561ded276c254bb56d8131da01006ba23ea8b7c7a4472f647
```
In the working file it sits after the C2 paragraph and before "**Absolutes are amended between sessions only**". The C2 paragraph comes directly after the park-rule "*Note for whoever installs this:*" paragraph, so C8 is no longer directly after that note.

**(b) O1 block.** HEAD 76–88 and working 78–90 both hash to `78a5b2f6c83a724753d8f030b3de06b714eb14d300e75ac09f5619c8c92718a2`.

**(c) Quotes, all hash-equal to source:**
- **C2** (answers file 19–22 vs the fenced block): `e6d0f71b21d224168b82768342cd03dd25bd3e20d7d24c3863a96d58885a2cd0` on both sides.
- **C6** (34–35, label and indent stripped, joined with one space, vs line 76): `bf03465205a1ca5e51053781d2c7fb5e5f3012af20222b58f05881a27c219275` on both sides.
- **D1–D5** (DECISIONS.md 1906–1927 vs the 22-line fenced block): `1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9` on both sides.
- **D12** quote "park-commit gate exemption (C2, trip-tested)": present in DECISIONS.md 1963–1964 joined, and in rubric 297–298.

**(d) Added lines that are not quotes:**
- 74 `## PASSED — closed criteria`: a heading.
- 76: labelled "Filer's note, not a ruling", cites C6 and 19:12:30Z.
- 91 `---` and 93 OPEN heading: moved structure (the HEAD heading line).
- 281: the C2 heading, carrying its citation.
- 283–284: labelled "Filer's note, not a ruling".
- 293–299: labelled "filer's statement, not a ruling".
- 383: the Autonomy heading, carrying its citation.
- 385–386: labelled "Filer's note, not a ruling".
- 413: labelled "master's reading … changeable by Amear".
- 300–309: the C8 ruling text. It is not labelled as a note, but its own header cites DECISION_LOG `2026-07-27T18:15Z` (row 89 reads `APPROVED BY: amear`).

Every one is labelled or cited.

**(e) Nothing else changed.** I deleted 75–76, 91–94, 280–309 and 382–413 and put the OPEN heading back at 74. The result is `16a7f819c776adf9002234d4ef24aa5a9a2743461204594cd24ee7253b67341b`, equal to HEAD. Keeping 300–309 instead gives `bffddb6a…3dd869e2`, equal to the snapshot. The only line removed on the HEAD side is `74c74,76 < ## OPEN — gradeable now`. The S8 row (now line 128) is untouched.

**(f) Ledger rows.** Both exist with WHO: amear:
- `743:- [2026-11-08T19:12:30Z] **WHO: amear** | WHAT: **C1–C10, ANSWERS TO THE 2026-11-08 PARK CARD, pasted by Amear …` (names D-2026-11-08-C)
- `744:- [2026-11-08T19:57:00Z] **WHO: amear** | WHAT: **D1–D12, VOICE SESSION 2 …` (names D-2026-11-08-D)

**(g) False or overstated claims.**
- `grep -n -i park .claude/hooks/gate-commit.sh` finds nothing (exit 1), so "no line of which mentions park" is true. Line 110 confirms the gate is only armed while the orchestrator-active marker exists, so "whenever it is armed" is right.
- **MINOR: the C2 build-state sentence overstates the hook.** "still admits only a PASS-minted token" is broader than what the hook does. I copied its matcher lines 96–107 into `/tmp/rubric-adv2/re.sh` and ran it on test strings (the hook itself was not run):
  ```
  GATED: git commit -m x
  UNGATED (hook exits 0 before arming check): git 'commit' -m x
  UNGATED (hook exits 0 before arming check): git commit-tree T -p HEAD -m x
  UNGATED (hook exits 0 before arming check): git update-ref refs/heads/parked/b1 abc
  ```
  So the hook only stops the form it recognises as a commit. Plumbing that writes a parked/ branch never reaches its token check. "Cannot be done by the master" therefore holds only for the sanctioned commit form. Whether `master-bash-guard.sh` blocks those other forms is UNVERIFIED: a grep for commit-tree, update-ref or parked found nothing in it or in `no-commit-guard.sh`, but that proves nothing if it works from an allowlist. The sentence understates nothing. The wording was set by the brief.
- The sentence does not claim bead 8sw is closed. "Closes Praxis_build-8sw." appears only inside Amear's quoted C2.

**(h) MANIFEST.**
- 316 lines. `head -n 315 | sha256` = `fea161a54d1628fa10188d26ffb6525db00b89953b0c10e4f5d108b2adb7042c`, which matches. Line 315 is EQUAL to HEAD line 307.
- Lines 314–316 all have 6 pipes, and row 316 uses the same `Report | 2 | 2026-11-09` columns as row 315.
- Row 316's facts check out: 345 and 413 lines, C2/C6/C8/D1–D5/D12, and the report is untracked (`??`). The report itself is a stub that says "Result: BLOCKED (provisional)".
- **MINOR: no rubric amendment row.** Earlier rubric edits got an "AMENDMENT ROW" on `/specs/SPEC_RUBRIC.md` (row 298, commit `6c4c10931ab87949d501cfdc873d3762153ab6a1`). There is no row 5, so that path's history ends before this edit. The brief asked for this shape.
- **MINOR, outside scope: stale line references.** The rubric gained 6 lines above S7, so DECISIONS.md:1887 (`:121` S7, `:252` park step 1) and :1989 (`:122` S8) now point at the wrong lines. Those are now 127, 258 and 128.

**Incident:** on one of my calls the real commit gate hook blocked my command ("one git commit per Bash call") because test strings were in the command text. Nothing ran, and I rebuilt the strings at runtime afterwards.

GRADE: NOT REFUTED
Result: PASS
~~~~

### How each finding was resolved

| # | Finding | Resolution |
|---|---|---|
| ADV1-1 | The hook claim left out that the gate only checks while armed | FIXED. "whenever it is armed" added (fix diff pasted above). ADV2 confirmed the new wording against hook :110. |
| ADV1-2 | C8 is not cited by name in the rubric | NOT CHANGED. C8 had to land byte-for-byte, and the brief lists no C8 cite line ("Nothing else in the file changes"). The hunk keeps its own inline cite: DECISION_LOG `2026-07-27T18:15Z`, line 89, `APPROVED BY: amear` (pasted). The record that lands it is C8, D-2026-11-08-C, DECISION_LOG `2026-11-08T19:12:30Z`. One thing for the master and auditor to note: row 89's approval reads "direct in-session instruction". S5 says an in-session exchange is not an approval, so the authority for landing the hunk rests on C8's ledger row, not on row 89. |
| ADV2-g | "still admits only a PASS-minted token" overstates the hook. Quoted `git 'commit'` and plumbing (`commit-tree`, `update-ref`) never reach the token check (ADV2 ran the hook's matcher lines on test strings, not the hook itself). | NOT CHANGED IN THIS UNIT. Open for the master. The sentence is the brief's wording, given under the master's D1 decision (2). What it is there to record, that the exemption is ruled but not built, holds either way: gate-commit.sh has no line mentioning "park" (pasted). The way past the gate that ADV2 found is a known class of commit-guard bypass, not something this edit created, and using it would evade the gate, not perform park step 1. If the master wants the sentence narrowed (for example "...admits a recognised `git commit` only with a PASS-minted token..."), that is one more rubric edit and needs a fresh adversary. The finding is not hidden: the auditor sees it here. |
| ADV2-h1 | No MANIFEST amendment row for `/specs/SPEC_RUBRIC.md` itself | NOT CHANGED. The brief allows exactly one appended row, for this report, noting the rubric edit. Row 316 does note it. A separate rubric row is the master's call. |
| ADV2-h2 | DECISIONS.md pointers into the rubric are now stale | OUTSIDE SCOPE: this unit may not edit DECISIONS.md. The manager re-ran it: DECISIONS.md :1887 cites park step 1 as `:252` (now :258); :1989 cites S8 as `:122` (now :128). HEAD :121, :122 and :252 against working-tree :127, :128 and :258 are pasted below. Handed to the master as a follow-up. |

~~~~
$ sed -n '1887p' DECISIONS.md | grep -o '.\{50\}:\(121\|252\)[^0-9].\{30\}'
d while any audit box is unchecked." Park step 1 (:252): "Commit the work to a branch
$ sed -n '1989p' DECISIONS.md | grep -o '.\{60\}:122.\{40\}' | head -2
 D1–D5 change the scope of rubric S8 (`specs/SPEC_RUBRIC.md`:122, "No question that belongs to Amear is
$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '121p;122p;252p' | cut -c1-60; sed -n '127p;128p;258p' specs/SPEC_RUBRIC.md | cut -c1-60
| S7 | Nothing is committed while any audit box is unchecked
| S8 | No question that belongs to Amear is answered on his
1. Commit the work to a branch `parked/<bead-id>`. It does n
| S7 | Nothing is committed while any audit box is unchecked
| S8 | No question that belongs to Amear is answered on his
1. Commit the work to a branch `parked/<bead-id>`. It does n
~~~~

## S6 cross-block check

This unit edits process text only. No block spec (Blocks 1–5), breaker, strategy, cost model or signal-path component is touched. Each edit, checked against what else it reaches:
- C6 (O1 to PASSED): O1's own State line already read PASSED@a2f1067 at HEAD. The move changes no criterion text. O2–O4 stay under OPEN (headings pasted).
- C2: this is text only. No hook was touched (`git status --porcelain -- .claude/hooks/gate-commit.sh` is empty, pasted). The park rule's steps 1–3 are unchanged. The text says step 1 still cannot be done by the master until the trip-tested gate unit lands.
- C8: the "two-strike" wording reaches the park rule. It does not change the park rule's own text, which is byte-identical to HEAD (rebuild check).
- Autonomy (D1–D5): this reaches S8 (scope) and S7 / D3 (commits land on an audit PASS). Neither table row is edited. How S8 is read is labelled as the master's reading. D2 (b) and (c) bear on Blocks 3–5 (order path to a funded account; breaker values while real money is at stake), and the section quotes those words without changing any breaker spec. Downstream line pointers into this file have shifted. The two found in DECISIONS.md are listed above.
- FROZEN F1–F4 are not touched (line 17 heading and F-block lines are inside the HEAD-equal rebuild).

## Files staged

None. Brief standing rule 4 says this unit does not stage, commit or touch the index. The master builds a temp index. Files written by this unit, all left in the working tree:
- `specs/SPEC_RUBRIC.md` (modified; 345 → 413 lines against HEAD)
- `MANIFEST.md` (one row appended at line 316; lines 1–315 unchanged)
- `docs/reports/2026-11-09-rubric-unit-manager.md` (this report, untracked)

Scratch files outside the repo: `/tmp/rubric-unit/` (build.py, capture.sh, snapshots, evidence captures). Nothing was written under `.claude/agent-memory/`, and no other repo file was changed.

## Result

Result: PASS at level WRITTEN. The four edits are made and checked by hash. Two adversaries returned NOT REFUTED. One MINOR was fixed. Four MINORs are left open and handed to the master (table above). The C2 exemption itself is RULED and NOT BUILT. Bead Praxis_build-8sw is not closed by this unit. The manager does not grade its own output: the auditor grades.

## Final block (captured after the last edit to the rubric and MANIFEST.md; this report was then finished by appending this block and the diff of record)

A report cannot carry its own final sha256. This block is generated by appending command output to the report. Lines 1–N, where N is printed first below, are the report as it stood before the block was appended. The sha of the complete file is given to the master in the return message.

~~~~
N=466
$ head -n 466 docs/reports/2026-11-09-rubric-unit-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 5412fedf1f857a8fe7f6b481b0b7d16df6507a4c8c6329443e9cf029fbd6a9a4
$ date -u
Mon Nov  9 14:10:19 UTC 2026
[exit 0]

$ openssl dgst -sha256 specs/SPEC_RUBRIC.md MANIFEST.md
SHA2-256(specs/SPEC_RUBRIC.md)= 4436c425369d7472d7a216f26d95d1a5957bf19d2cb78271c5b8fde0e4b5ae9b
SHA2-256(MANIFEST.md)= a2c1afdc8f4655388e3a49227713b48c564da7c909f945ff706048b342c41042
[exit 0]

$ wc -l specs/SPEC_RUBRIC.md MANIFEST.md
     413 specs/SPEC_RUBRIC.md
     316 MANIFEST.md
     729 total
[exit 0]

$ head -n 315 MANIFEST.md | openssl dgst -sha256; sed -n '316p' MANIFEST.md | openssl dgst -sha256
SHA2-256(stdin)= fea161a54d1628fa10188d26ffb6525db00b89953b0c10e4f5d108b2adb7042c
SHA2-256(stdin)= 6417eaa757e2340fb2a382d1043e60f1c798cbaf967ab7168a487374c7c27322
[exit 0]

$ git status --porcelain -- specs/SPEC_RUBRIC.md MANIFEST.md docs/reports/2026-11-09-rubric-unit-manager.md
 M MANIFEST.md
 M specs/SPEC_RUBRIC.md
?? docs/reports/2026-11-09-rubric-unit-manager.md
[exit 0]

$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
69	1	specs/SPEC_RUBRIC.md
[exit 0]

~~~~

## Diff of record (pasted last, after every edit to specs/SPEC_RUBRIC.md)

~~~~
$ git diff HEAD -- specs/SPEC_RUBRIC.md
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index e1963d6..8a3234d 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -71,7 +71,9 @@ closure states it has not been confirmed by direct inquiry.
 
 ---
 
-## OPEN — gradeable now
+## PASSED — closed criteria
+
+Filer's note, not a ruling: O1 is moved here out of OPEN under Amear's C6 (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear), copied by script from `docs/reports/2026-11-08-amear-answers-park-card.md` :34–35 joined with one space: `"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
 
 ### O1 — Walk-forward gate set for the replication arm
 **State:** PASSED@a2f1067. Amear's ruling A8, D-2026-11-08-B (DECISION_LOG
@@ -86,6 +88,10 @@ optimisation from the first pass. **Required:** a written statement of which
 gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
 replication arm or the later optimisation arm.
 
+---
+
+## OPEN — gradeable now
+
 ### O2 — `praxispush` provisioning
 The signal directory was specified as a dedicated low-privilege macOS user, the
 rationale being structural blast-radius limitation. The build report places it
@@ -272,6 +278,36 @@ blocked, move on" wording. It is outside this repository and affects other
 projects, so it is **not** edited from here. This section is the binding text for
 PRAXIS work.
 
+**Park-commit exemption — C2, 2026-11-08 human ruling (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear).**
+
+Filer's note, not a ruling: Amear's words, copied by script from
+`docs/reports/2026-11-08-amear-answers-park-card.md` :19–22.
+
+```text
+C2  Park rule amendment (made between sessions, per the absolutes
+    rule): a park commit to parked/ branches is exempt from the
+    audit-token gate, because it never touches main. Closes
+    Praxis_build-8sw.
+```
+
+State of the build (filer's statement, not a ruling; read from the hook on
+2026-11-09, no line of which mentions "park", and not trip-tested here): the
+exemption is RULED and NOT YET BUILT, because `.claude/hooks/gate-commit.sh`
+still admits only a PASS-minted token whenever it is armed, the gate change is a
+later, trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
+trip-tested)"), and
+until that lands step 1 of the park rule still cannot be done by the master.
+
+**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
+row `2026-07-27T18:15Z`.**
+
+A grading agent that returns no explicit verdict has not graded. Absence of a
+verdict is treated as FAIL for the commit decision and never as PASS or as
+no-finding. It does NOT count toward the park rule's two-strike limit, which
+counts adverse verdicts on the work. A no-verdict unit may be re-dispatched only
+after material reduction, stated in the dispatch row; a second consecutive
+no-verdict return on the same bead counts as the second FAIL.
+
 **Absolutes are amended between sessions only — 2026-07-26 human ruling.**
 
 A rule declared absolute is **never amended inside the session that hits it.**
@@ -343,3 +379,35 @@ settled. Splitting the field makes that question answerable by reading. It does
 not make the answer trustworthy — for that, the authorisation chain in S4 and
 S5 (the ledger append *is* the authorisation) remains the only control, and it
 too is a record rather than a proof.
+
+## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
+
+Filer's note, not a ruling: Amear's words, copied by script from DECISIONS.md
+:1906–1927 (the D-2026-11-08-D verbatim block).
+
+```text
+STANDING RULE CHANGE — AUTONOMY
+D1  Default-decide. When a unit or the master reaches a question that
+    would otherwise go to Amear, it takes the recommended option, logs
+    it as "decided by master under D-2026-11-08-D D1", and continues.
+    Amear may reverse any such decision later; the reversal is filed
+    like any ruling. No unit waits on Amear except for D2 items.
+D2  Only four things stop and wait for Amear's word: (a) spending
+    money; (b) switching live trading on, or any order path to a
+    funded account; (c) changing circuit-breaker values while real
+    money is at stake; (d) installing keys, credentials or agent
+    permissions. Everything else is D1.
+D3  The Telegram commit-approval step in the Hermes setup is removed.
+    Commits land on an audit PASS. Telegram informs; it does not ask.
+D4  Loop: a Hermes timer starts a fresh Code session every four hours.
+    Each run reads HANDOFF.md, executes the next unit(s), and ends with
+    one Telegram message in plain English: what was done, what was
+    decided under D1, what is blocked under D2. No code names (F1, O1,
+    bead IDs) without a plain-language gloss. Rough weekly review with
+    Amear in the Claude.ai channel; nothing waits on it.
+D5  A message to Amear that asks a question with a recommendation
+    attached, on a non-D2 item, is a defect under D1. Log it, bead it,
+    take the recommendation.
+```
+
+S8 is read together with D1 and D2: what belongs to Amear is the D2 list (master's reading, D-2026-11-08-D filing note 1; changeable by Amear).
[exit 0]

~~~~

## Correction 1 (2026-11-09, after audit FAIL 1)

An independent audit graded this unit FAIL (strike 1). The master's correction brief (unit `2026-11-09-rubric-unit-correction-1`) orders three fixes to `specs/SPEC_RUBRIC.md` and nothing else: MAJOR 1 (header rule / S5, the C8 citation), MAJOR 2 (S2, the C2 build-state paragraph), and a MINOR (the C6 filer's note). This section is appended. Lines 1–607 of this report are byte-identical to the version the audit read (sha256 `d07ef92c…`, pasted in the final block below). Where those lines describe the rubric file as it stood before this correction, this section supersedes them. That covers the line ranges 281–310 and 382–413, the whole-file sha256 `4436c425…`, the 413-line count, the S6 sentence "The text says step 1 still cannot be done by the master until the trip-tested gate unit lands.", and the diff of record at :502. All of them are SUPERSEDED.

Method: the manager made the three edits directly, with one script (`/tmp/rubric-unit/corr1/edit.py`). The script copies C8's words from park-card :38 and the bead title from `bd show Praxis_build-8sw` output, and asserts both before writing. It wraps the new C2 paragraph at 80 columns. A pre-edit copy of the rubric is at `/tmp/rubric-unit/corr1/rubric-pre.md`. One worker was dispatched, in ADVERSARIAL mode, on the final rubric diff only. Nothing was staged or committed. Nothing was written under `.claude/agent-memory/`. No repo file other than the rubric and this report was touched.

### Workers dispatched (Correction 1)

| id | mode | scope | outcome |
|---|---|---|---|
| a4ea782fefaccb576 | ADVERSARIAL | final rubric diff vs pre-correction file; the three fixes as briefed; any new statement of a gate property | ADVERSARIAL OUTCOME: CLEAN (12 findings, all OK) |

### The changed rubric passages, before and after

**MAJOR 1: C8 citation (header rule / S5).** Before: there was no line here. Pre-correction :300 was blank, and the hunk's bold heading was at :301. After: a one-line filer's note is at :302, followed by a blank line at :303. The heading is now at :304. The hunk's 10 lines (:304–313, the bold heading through the blank line after "...counts as the second FAIL.") hash `11d560e6…` before and after (pasted below). The note's style (one long line, then a blank line, then the heading) matches the C6 filer's note at :76–78. After:

~~~~
Filer's note, not a ruling: this ruling lands under Amear's C8, "The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written." (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; docs/reports/2026-11-08-amear-answers-park-card.md :38).
~~~~

**MAJOR 2: C2 build-state paragraph (S2).** Pre-correction :293–299 (7 lines) are SUPERSEDED. That text claimed a property of the commit gate that the static read does not support, and it had a stray short line split at :298. Before (SUPERSEDED):

~~~~
State of the build (filer's statement, not a ruling; read from the hook on
2026-11-09, no line of which mentions "park", and not trip-tested here): the
exemption is RULED and NOT YET BUILT, because `.claude/hooks/gate-commit.sh`
still admits only a PASS-minted token whenever it is armed, the gate change is a
later, trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
trip-tested)"), and
until that lands step 1 of the park rule still cannot be done by the master.
~~~~

After (:293–300, 8 lines, none over 80 columns). It states no gate property. It says only the five things briefed: (i) filer's statement, not a ruling; (ii) the static grep, not trip-tested; (iii) the bead is OPEN, and its title, copied from `bd show` output by script; (iv) the D12 quote; (v) RULED and NOT YET BUILT.

~~~~
State of the build (filer's statement, not a ruling): a static read of
`.claude/hooks/gate-commit.sh` on 2026-11-09 found no line that mentions "park"
(`grep -c -i park .claude/hooks/gate-commit.sh` prints 0); it was not
trip-tested here. Bead `Praxis_build-8sw` is OPEN, and its title records that
the absolute park rule has no sanctioned commit path: "PARK RULE vs COMMIT GATE:
absolute park rule has no sanctioned commit path". The gate change is the later,
trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
trip-tested)"). So the exemption is RULED and NOT YET BUILT.
~~~~

**MINOR: C6 filer's note (:76).** The note now also says that the `C6  ` label and the leading indentation of park-card :35 were dropped. The backticked quote is unchanged (re-derived by script below). Before (SUPERSEDED):

~~~~
Filer's note, not a ruling: O1 is moved here out of OPEN under Amear's C6 (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear), copied by script from `docs/reports/2026-11-08-amear-answers-park-card.md` :34–35 joined with one space: `"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
~~~~

After:

~~~~
Filer's note, not a ruling: O1 is moved here out of OPEN under Amear's C6 (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear), copied by script from `docs/reports/2026-11-08-amear-answers-park-card.md` :34–35 joined with one space, with the `C6  ` label and the leading indentation dropped: `"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
~~~~

### Ledger pointers (information only)

- **MANIFEST row.** This unit's MANIFEST row is line 316 in the working tree (pasted below: `grep -n 'rubric-unit-manager' MANIFEST.md`). In the master's commit blob it is line 308: HEAD's MANIFEST.md has 307 lines (pasted below), plus 1. The working tree carries rows from other units that the master's surgical blob leaves out. MANIFEST.md was not edited by this correction.
- **DECISIONS.md :1887 and :1989** still cite rubric line numbers from HEAD: `:121` (S7) and `:252` (park step 1) on :1887, and `:122` (S8) on :1989 (pasted below). In the working tree those lines are now :127, :128 and :258. Correction 1 inserts nothing above :293, so those three targets did not move further. This is OUT OF SCOPE for this unit (DECISIONS.md may not be edited here) and goes to a follow-up for the master.
- Information from the adversary (finding 3): the briefed hunk hash `11d560e6…` covers 10 lines, the 9 text lines plus the blank line after them. The hunk is unchanged either way.

### S6 cross-block check (Correction 1)

Text only. No hook, block spec, breaker or signal-path file is touched (`git status --porcelain` on the hook, DECISIONS.md and the park card is empty, pasted below). The new C2 paragraph no longer says anything about what the master can or cannot do under the park rule. The park rule's own text is inside the HEAD-equal rebuild. FROZEN F1–F4, S1–S13 and O1–O4 are not touched (rebuild check and O1 hash below).

### Files staged (Correction 1)

None. Files written, left in the working tree: `specs/SPEC_RUBRIC.md` (modified; 345 → 416 lines against HEAD) and this report (appended only; still untracked). Scratch files: `/tmp/rubric-unit/corr1/`.

### Adversarial findings (Correction 1)

Worker a4ea782fefaccb576 (ADVERSARIAL), its returned text verbatim:

~~~~
Findings (read-only; nothing written, index not touched).

1. **Pre-file identity.** OK
   `shasum -a 256 /tmp/rubric-unit/corr1/rubric-pre.md` printed `4436c425369d7472d7a216f26d95d1a5957bf19d2cb78271c5b8fde0e4b5ae9b`. This matches the brief.

2. **Nothing else moved (criterion 2).** OK
   `diff /tmp/rubric-unit/corr1/rubric-pre.md specs/SPEC_RUBRIC.md` printed exactly three hunks: `76c76`, `293,299c293,300` and `300a302,303`. `wc -l` printed 413 for the pre-file and 416 for the current file. That is +1 from FIX B (7 lines became 8) and +2 from FIX A (note line plus blank). All other lines are byte-identical and in order.
   I also ran `git diff HEAD -- specs/SPEC_RUBRIC.md | diff - /tmp/rubric-unit/corr1/final.diff && echo FINALDIFF_MATCH`. It printed `FINALDIFF_MATCH`.

3. **FIX A: hunk hash.** OK
   I ran a grep for the heading line (pattern `^\*\*No-V*RD*CT returns — R-A / R-B / R-C`, redacted). It found start=301 in the pre-file and start=304 in the current file, with one occurrence in the current file. `sed -n "${n},$((n+9))p" | shasum -a 256` printed `11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4` for both files.
   Side note: heading through "...counts as the second FAIL." is 9 lines (current 304–312). The 9-line hash is `1f67c51a…f122`. The briefed hash covers those 9 lines plus the blank line after them (304–313). Either way the hunk is unchanged.

4. **FIX A: C8 words and placement.** OK
   - `sed -n 34,38p` on the park card shows line 38 is `C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.`
   - Rebuilding the quote by script (line 38 with the `C8  ` label removed), then `grep -cF "under Amear's C8, \"$c8\" (D-2026-11-08-C;"` on the rubric, printed `1`.
   - Placement in the current file: line 300 ends the previous paragraph, 301 is blank, 302 is the new note, 303 is blank, 304 is the heading.
   - The note is one long line. That matches the file's existing style for the one-line filer's note on line 76.

5. **FIX A / FIX C: DECISION_LOG pointer.** OK
   - `grep -n '2026-11-08T19:12:30Z' DECISION_LOG.md` printed `743:- [2026-11-08T19:12:30Z] **WHO: amear** | WHAT: **C1–C10, ANSWERS TO THE 2026-11-08 PARK CARD…`
   - `grep -n 'D-2026-11-08-C' DECISIONS.md` printed `1808:## 2026-11-08 — D-2026-11-08-C: Amear's answers C1–C10…`
   - `grep -n C8 DECISIONS.md` shows `1845:C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.` and `1864:- **C8** (:38).` The `:38` pointer is confirmed.

6. **FIX B: bead title.** OK
   `bd show Praxis_build-8sw | head -1` printed `○ Praxis_build-8sw [BUG] · PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path   [● P1 · OPEN]`. The quoted string "PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path" is the title field exactly. The bead is OPEN.

7. **FIX B: grep claim.** OK
   `grep -c -i park .claude/hooks/gate-commit.sh` printed `0`. This matches the text's "prints 0".

8. **FIX B: D12 words.** OK
   `grep -n 'park-commit gate exemption' DECISIONS.md` printed:
   - `1963: … manager memory off (C7), park-commit gate exemption`, continued on 1964 as `    (C2, trip-tested), housekeeping (D9), …`
   - `1986:- **D12** (:71–75). "Sequence after D6: … park-commit gate exemption (C2, trip-tested), …"`

   The quote "park-commit gate exemption (C2, trip-tested)" matches.

9. **FIX B: wrapping.** OK
   `awk '{print length": "NR}' | sed -n 293,300p` printed lengths 70, 79, 69, 77, 80, 80, 70, 60. All are 80 or under. I checked each break and the next word would push every line past 80. The only short line is the paragraph's last line.

10. **FIX B: no commit-gate property asserted (criterion 3).** OK, with a note
    - Scanning the changed lines (293–302 and 76) for `admit|block|requir|cannot|only|still|token|armed|exempt|built|enforc|allow|refus|reject` hit only the D12 quote and "So the exemption is RULED and NOT YET BUILT."
    - The old wording is gone: "still admits only a PASS-minted token whenever it is armed" and "cannot be done by the master".
    - The remaining claims are all ones the brief allows. One is the static grep, stated as such and as not trip-tested. One is the bead title, attributed to the title. One is the D12 quote, attributed to D12.
    - Note: "So the exemption is RULED and NOT YET BUILT" is an inference from a static grep and a bead title, not a test. The brief requires this wording under (v), so it is not a defect.

11. **FIX C.** OK
    - Diff at 76 shows only "joined with one space" changed to "joined with one space, with the `C6  ` label and the leading indentation dropped". The backticked quote at the end of the line is unchanged.
    - Rebuilding the quote by script gave the same text: park card line 34 without the `C6  ` label, plus one space, plus line 35 without its leading spaces. `grep -cF` for the full new phrase plus that quote printed `1`.
    - `sed -n 34,35p` shows line 35 has 4 leading spaces, so "leading indentation" is accurate.

12. **Typos and pointers in changed lines.** OK
    D-2026-11-08-C, D-2026-11-08-D, 2026-11-08T19:12:30Z, `WHO: amear`, `:38` and `:34–35` all point to the correct rows and lines (findings 4, 5 and 11). I found no typos.

ADVERSARIAL OUTCOME: CLEAN
agentId: a4ea782fefaccb576
~~~~

How each adversary note was handled: finding 3 (the hash spans 10 lines, including the trailing blank) is recorded under "Ledger pointers" above as information. Finding 10's note concerns wording that the brief requires under (v), so it is left as briefed. No fix worker was needed.

### Verification evidence (Correction 1; captured by `/tmp/rubric-unit/corr1/capture.sh`, output pasted as printed)

Pre-correction state, read from the copies saved before the edit script ran (`capture.sh before`):

~~~~
$ openssl dgst -sha256 /tmp/rubric-unit/corr1/rubric-pre.md /tmp/rubric-unit/corr1/report-pre.md; wc -l /tmp/rubric-unit/corr1/rubric-pre.md /tmp/rubric-unit/corr1/report-pre.md
SHA2-256(/tmp/rubric-unit/corr1/rubric-pre.md)= 4436c425369d7472d7a216f26d95d1a5957bf19d2cb78271c5b8fde0e4b5ae9b
SHA2-256(/tmp/rubric-unit/corr1/report-pre.md)= d07ef92cb296e9f63e5b9af4b2d1d91bc1afd9e83f672fb21460f38bcd0d395b
     413 /tmp/rubric-unit/corr1/rubric-pre.md
     607 /tmp/rubric-unit/corr1/report-pre.md
    1020 total
[exit 0]

$ sed -n '301,310p' /tmp/rubric-unit/corr1/rubric-pre.md | openssl dgst -sha256
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
[exit 0]

$ grep -c -i park .claude/hooks/gate-commit.sh
0
[exit 1]

$ bd show Praxis_build-8sw | head -5
○ Praxis_build-8sw [BUG] · PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path   [● P1 · OPEN]
Owner: Amear Bani-Ahmad · Type: bug
Created: 2026-07-26 · Updated: 2026-07-26

DESCRIPTION
[exit 0]

$ sed -n '38p' docs/reports/2026-11-08-amear-answers-park-card.md
C8  The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
[exit 0]

$ sed -n '34,35p' docs/reports/2026-11-08-amear-answers-park-card.md | cat -e
C6  "Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of$
    the OPEN section.$
[exit 0]

~~~~

After the last rubric edit (`capture.sh after`). No edit to the rubric was made after this capture.

~~~~
$ date -u
Mon Nov  9 14:16:59 UTC 2026
[exit 0]

$ wc -l specs/SPEC_RUBRIC.md; git show HEAD:specs/SPEC_RUBRIC.md | wc -l
     416 specs/SPEC_RUBRIC.md
     345
[exit 0]

$ grep -n '^## ' specs/SPEC_RUBRIC.md
17:## FROZEN — nothing downstream may proceed until these clear
74:## PASSED — closed criteria
93:## OPEN — gradeable now
117:## Standing criteria — graded on every dispatch
250:## Process rulings — binding on the orchestrator
386:## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
[exit 0]

$ diff /tmp/rubric-unit/corr1/rubric-pre.md specs/SPEC_RUBRIC.md | grep '^[0-9]'
76c76
293,299c293,300
300a302,303
[exit 0]

$ python3 -I /tmp/rubric-unit/corr1/reverse_corr1.py | openssl dgst -sha256; openssl dgst -sha256 /tmp/rubric-unit/corr1/rubric-pre.md
SHA2-256(stdin)= 4436c425369d7472d7a216f26d95d1a5957bf19d2cb78271c5b8fde0e4b5ae9b
SHA2-256(/tmp/rubric-unit/corr1/rubric-pre.md)= 4436c425369d7472d7a216f26d95d1a5957bf19d2cb78271c5b8fde0e4b5ae9b
[exit 0]

$ diff <(git show HEAD:specs/SPEC_RUBRIC.md) specs/SPEC_RUBRIC.md | grep '^[0-9]'
74c74
75a76,77
88a91,94
274a281,313
345a385,416
[exit 0]

$ diff <(git show HEAD:specs/SPEC_RUBRIC.md) specs/SPEC_RUBRIC.md | grep '^<'
< ## OPEN — gradeable now
[exit 0]

$ sed -e '76,77d' -e '90,93d' -e '281,313d' -e '385,416d' -e '74s/^## PASSED — closed criteria$/## OPEN — gradeable now/' specs/SPEC_RUBRIC.md | openssl dgst -sha256; git show HEAD:specs/SPEC_RUBRIC.md | openssl dgst -sha256
SHA2-256(stdin)= 16a7f819c776adf9002234d4ef24aa5a9a2743461204594cd24ee7253b67341b
SHA2-256(stdin)= 16a7f819c776adf9002234d4ef24aa5a9a2743461204594cd24ee7253b67341b
[exit 0]

$ git show HEAD:specs/SPEC_RUBRIC.md | sed -n '76,87p' | openssl dgst -sha256; sed -n '78,89p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '78p;89p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= 89d1118a7c9cf30612d90d0cb580070c0edfd78c3510fc62cd7b103b03b18bd8
SHA2-256(stdin)= 89d1118a7c9cf30612d90d0cb580070c0edfd78c3510fc62cd7b103b03b18bd8
### O1 — Walk-forward gate set for the replication arm
replication arm or the later optimisation arm.
[exit 0]

$ sed -n '304,313p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '301,310p' /tmp/rubric-unit/corr1/rubric-pre.md | openssl dgst -sha256; openssl dgst -sha256 /tmp/rubric-unit/c8-before.txt; sed -n '302,303p;314p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(stdin)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
SHA2-256(/tmp/rubric-unit/c8-before.txt)= 11d560e604b6d47a48fd96a4b05c22395fe660f388285ab641f8190898e902d4
Filer's note, not a ruling: this ruling lands under Amear's C8, "The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written." (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; docs/reports/2026-11-08-amear-answers-park-card.md :38).

**Absolutes are amended between sessions only — 2026-07-26 human ruling.**
[exit 0]

$ sed -n '19,22p' docs/reports/2026-11-08-amear-answers-park-card.md | openssl dgst -sha256; sed -n '287,290p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '286p;291p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= e6d0f71b21d224168b82768342cd03dd25bd3e20d7d24c3863a96d58885a2cd0
SHA2-256(stdin)= e6d0f71b21d224168b82768342cd03dd25bd3e20d7d24c3863a96d58885a2cd0
```text
```
[exit 0]

$ sed -n '1906,1927p' DECISIONS.md | openssl dgst -sha256; sed -n '392,413p' specs/SPEC_RUBRIC.md | openssl dgst -sha256; sed -n '391p;414p' specs/SPEC_RUBRIC.md
SHA2-256(stdin)= 1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9
SHA2-256(stdin)= 1e40234286aae17c8cf2c06005dd328640199562a12029ba08fde61205a5b5d9
```text
```
[exit 0]

$ sed -n '38p' docs/reports/2026-11-08-amear-answers-park-card.md | sed 's/^C8  //'; sed -n '302p' specs/SPEC_RUBRIC.md | grep -o -F "$(sed -n '38p' docs/reports/2026-11-08-amear-answers-park-card.md | sed 's/^C8  //')"
The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written.
[exit 0]

$ sed -n '34,35p' docs/reports/2026-11-08-amear-answers-park-card.md | sed '1s/^C6  //;2s/^ *//' | paste -sd' ' -; sed -n '76p' specs/SPEC_RUBRIC.md | grep -o '`"Discharged.*`$'
"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.
`"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
[exit 0]

$ grep -c -i park .claude/hooks/gate-commit.sh; bd show Praxis_build-8sw | head -1
0
○ Praxis_build-8sw [BUG] · PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path   [● P1 · OPEN]
[exit 0]

$ sed -n '293,300p' specs/SPEC_RUBRIC.md | paste -sd' ' - | grep -o -F "$(bd show Praxis_build-8sw | head -1 | sed 's/^[^·]*· //;s/   \[.*$//')"
PARK RULE vs COMMIT GATE: absolute park rule has no sanctioned commit path
[exit 0]

$ awk 'NR>=293 && NR<=300 && length>80 {print NR": "length}' specs/SPEC_RUBRIC.md; echo wrap-check-done
wrap-check-done
[exit 0]

$ git status --porcelain -- DECISIONS.md MANIFEST.md docs/reports/2026-11-08-amear-answers-park-card.md .claude/hooks/gate-commit.sh specs/SPEC_RUBRIC.md docs/reports/2026-11-09-rubric-unit-manager.md
 M MANIFEST.md
 M specs/SPEC_RUBRIC.md
?? docs/reports/2026-11-09-rubric-unit-manager.md
[exit 0]

$ grep -n 'rubric-unit-manager' MANIFEST.md | cut -d'|' -f1-3; git show HEAD:MANIFEST.md | wc -l
316:| /docs/reports/2026-11-09-rubric-unit-manager.md | Report 
     307
[exit 0]

$ awk 'NR==1887||NR==1989 {print NR}' DECISIONS.md; sed -n '1887p;1989p' DECISIONS.md | grep -n -o -E ':(121|122|252)[^0-9]'
1887
1989
1::121)
1::252)
2::122,
[exit 0]

~~~~

### Final block (Correction 1)

A report cannot carry its own final sha256. This block is made by appending command output. The report sha256 printed here is of the report as it stood just before this block was appended: lines 1 to N, where N is printed with it. Lines 1–607 are hashed separately to show they are byte-identical to the version the audit read. The sha256 and line count of the complete file go to the master in the return message.

~~~~
$ openssl dgst -sha256 specs/SPEC_RUBRIC.md; wc -l specs/SPEC_RUBRIC.md
SHA2-256(specs/SPEC_RUBRIC.md)= 96826c224cf6a195a5e77371e6e6309646151e30ce6c30589eadc0dcb69f80f0
     416 specs/SPEC_RUBRIC.md
[exit 0]

$ head -n 607 docs/reports/2026-11-09-rubric-unit-manager.md | openssl dgst -sha256; openssl dgst -sha256 /tmp/rubric-unit/corr1/report-pre.md
SHA2-256(stdin)= d07ef92cb296e9f63e5b9af4b2d1d91bc1afd9e83f672fb21460f38bcd0d395b
SHA2-256(/tmp/rubric-unit/corr1/report-pre.md)= d07ef92cb296e9f63e5b9af4b2d1d91bc1afd9e83f672fb21460f38bcd0d395b
[exit 0]

$ N=$(wc -l < docs/reports/2026-11-09-rubric-unit-manager.md); echo N=$N; openssl dgst -sha256 docs/reports/2026-11-09-rubric-unit-manager.md
N= 912
SHA2-256(docs/reports/2026-11-09-rubric-unit-manager.md)= ce6417260567e0427b98614837f8dd67e50cb0c0d88cb00792be84f870ef2b3f
[exit 0]

$ grep -c -F -f /tmp/rubric-unit/corr1/house.txt docs/reports/2026-11-09-rubric-unit-manager.md
1
[exit 0]

$ git diff --numstat HEAD -- specs/SPEC_RUBRIC.md
72	1	specs/SPEC_RUBRIC.md
[exit 0]

~~~~

### Diff of record (Correction 1; supersedes the diff of record at :502; pasted last, after the last edit to specs/SPEC_RUBRIC.md)

~~~~
$ git diff HEAD -- specs/SPEC_RUBRIC.md
diff --git a/specs/SPEC_RUBRIC.md b/specs/SPEC_RUBRIC.md
index e1963d6..3f3510a 100644
--- a/specs/SPEC_RUBRIC.md
+++ b/specs/SPEC_RUBRIC.md
@@ -71,7 +71,9 @@ closure states it has not been confirmed by direct inquiry.
 
 ---
 
-## OPEN — gradeable now
+## PASSED — closed criteria
+
+Filer's note, not a ruling: O1 is moved here out of OPEN under Amear's C6 (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear), copied by script from `docs/reports/2026-11-08-amear-answers-park-card.md` :34–35 joined with one space, with the `C6  ` label and the leading indentation dropped: `"Discharged" recorded as PASSED@a2f1067 is correct. O1 moves out of the OPEN section.`
 
 ### O1 — Walk-forward gate set for the replication arm
 **State:** PASSED@a2f1067. Amear's ruling A8, D-2026-11-08-B (DECISION_LOG
@@ -86,6 +88,10 @@ optimisation from the first pass. **Required:** a written statement of which
 gate set applies to the replication arm and whether GO/HOLD/REJECT sits on the
 replication arm or the later optimisation arm.
 
+---
+
+## OPEN — gradeable now
+
 ### O2 — `praxispush` provisioning
 The signal directory was specified as a dedicated low-privilege macOS user, the
 rationale being structural blast-radius limitation. The build report places it
@@ -272,6 +278,39 @@ blocked, move on" wording. It is outside this repository and affects other
 projects, so it is **not** edited from here. This section is the binding text for
 PRAXIS work.
 
+**Park-commit exemption — C2, 2026-11-08 human ruling (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear).**
+
+Filer's note, not a ruling: Amear's words, copied by script from
+`docs/reports/2026-11-08-amear-answers-park-card.md` :19–22.
+
+```text
+C2  Park rule amendment (made between sessions, per the absolutes
+    rule): a park commit to parked/ branches is exempt from the
+    audit-token gate, because it never touches main. Closes
+    Praxis_build-8sw.
+```
+
+State of the build (filer's statement, not a ruling): a static read of
+`.claude/hooks/gate-commit.sh` on 2026-11-09 found no line that mentions "park"
+(`grep -c -i park .claude/hooks/gate-commit.sh` prints 0); it was not
+trip-tested here. Bead `Praxis_build-8sw` is OPEN, and its title records that
+the absolute park rule has no sanctioned commit path: "PARK RULE vs COMMIT GATE:
+absolute park rule has no sanctioned commit path". The gate change is the later,
+trip-tested unit (D-2026-11-08-D D12: "park-commit gate exemption (C2,
+trip-tested)"). So the exemption is RULED and NOT YET BUILT.
+
+Filer's note, not a ruling: this ruling lands under Amear's C8, "The July SPEC_RUBRIC R-A/R-B/R-C hunk lands as written." (D-2026-11-08-C; DECISION_LOG 2026-11-08T19:12:30Z, WHO: amear; docs/reports/2026-11-08-amear-answers-park-card.md :38).
+
+**No-verdict returns — R-A / R-B / R-C, ruled 2026-07-27. Source: DECISION_LOG
+row `2026-07-27T18:15Z`.**
+
+A grading agent that returns no explicit verdict has not graded. Absence of a
+verdict is treated as FAIL for the commit decision and never as PASS or as
+no-finding. It does NOT count toward the park rule's two-strike limit, which
+counts adverse verdicts on the work. A no-verdict unit may be re-dispatched only
+after material reduction, stated in the dispatch row; a second consecutive
+no-verdict return on the same bead counts as the second FAIL.
+
 **Absolutes are amended between sessions only — 2026-07-26 human ruling.**
 
 A rule declared absolute is **never amended inside the session that hits it.**
@@ -343,3 +382,35 @@ settled. Splitting the field makes that question answerable by reading. It does
 not make the answer trustworthy — for that, the authorisation chain in S4 and
 S5 (the ledger append *is* the authorisation) remains the only control, and it
 too is a record rather than a proof.
+
+## Autonomy — D1–D5, 2026-11-08 human ruling (D-2026-11-08-D; DECISION_LOG 2026-11-08T19:57:00Z, WHO: amear)
+
+Filer's note, not a ruling: Amear's words, copied by script from DECISIONS.md
+:1906–1927 (the D-2026-11-08-D verbatim block).
+
+```text
+STANDING RULE CHANGE — AUTONOMY
+D1  Default-decide. When a unit or the master reaches a question that
+    would otherwise go to Amear, it takes the recommended option, logs
+    it as "decided by master under D-2026-11-08-D D1", and continues.
+    Amear may reverse any such decision later; the reversal is filed
+    like any ruling. No unit waits on Amear except for D2 items.
+D2  Only four things stop and wait for Amear's word: (a) spending
+    money; (b) switching live trading on, or any order path to a
+    funded account; (c) changing circuit-breaker values while real
+    money is at stake; (d) installing keys, credentials or agent
+    permissions. Everything else is D1.
+D3  The Telegram commit-approval step in the Hermes setup is removed.
+    Commits land on an audit PASS. Telegram informs; it does not ask.
+D4  Loop: a Hermes timer starts a fresh Code session every four hours.
+    Each run reads HANDOFF.md, executes the next unit(s), and ends with
+    one Telegram message in plain English: what was done, what was
+    decided under D1, what is blocked under D2. No code names (F1, O1,
+    bead IDs) without a plain-language gloss. Rough weekly review with
+    Amear in the Claude.ai channel; nothing waits on it.
+D5  A message to Amear that asks a question with a recommendation
+    attached, on a non-D2 item, is a defect under D1. Log it, bead it,
+    take the recommendation.
+```
+
+S8 is read together with D1 and D2: what belongs to Amear is the D2 list (master's reading, D-2026-11-08-D filing note 1; changeable by Amear).
[exit 0]

~~~~

Result: PASS at level WRITTEN. The three fixes are made by script and checked by hash and by re-derivation from the source files. The July hunk is byte-identical (`11d560e6…`). Reversing every edit gives HEAD (`16a7f819…`). The adversary returned CLEAN. The C2 exemption is still RULED and NOT YET BUILT, and the rubric no longer states any gate property. DECISIONS.md :1887 and :1989 pointers go to a follow-up. The manager does not grade its own output: the auditor grades.
