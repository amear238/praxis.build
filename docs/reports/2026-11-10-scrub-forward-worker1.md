# 2026-11-10 scrub-forward, worker 1 (BUILD)

## Task

Unit 2026-11-10-scrub-forward, bead Praxis_build-8ux. Mode: BUILD. Replace the one withheld term (masked below as XTERMX) with "session window" at its single occurrence in each of three files, in the working tree and in prepared landing blobs built from HEAD 0eea766. Also append a de-identification note to the end of the sweep-manager report. No commit, and no command that writes the git index.

Files touched (working tree only, nothing staged):
- DECISION_LOG.md, line 47 (HEAD line 47)
- HANDOFF.md, working-tree line 1319 (HEAD line 1099)
- docs/reports/2026-11-09-d11-sweep-manager.md, line 635, plus the appended note (new lines 2232-2235)

Landing blobs (not staged) are at /tmp/scrub-final/DECISION_LOG.md, /tmp/scrub-final/HANDOFF.md, /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md. Pre-edit working-tree copies are at /tmp/scrub-pre/<same paths>.

Standing caveat carried with this unit: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Steps

1. Loaded the term into a shell variable with `eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"` and confirmed it was set (`TERM-nonempty`). Sourced `/tmp/scrub-mask.sh`. The term was never printed. Every diff shown here went through `| M`.
2. Step A (before): counted occurrences and found their line numbers in the working tree and in HEAD. Result: 1 matching line per file and 1 occurrence per file (grep -o), at the line numbers in the brief. The sweep-manager report ended in a single `\n`.
3. Saved the pre-edit working copies to /tmp/scrub-pre/ and checked them with cmp.
4. Step B: edited each working copy with perl. The term was passed as `T="$TERM"`. The pattern was `s/\Q$t\E/session window/i`, restricted to the target line, and it was set to `die` if that line did not match (none died). Then appended the note text from /tmp/scrub-note.txt to the report. That file starts with `\n` because the report already ended in `\n`, so exactly one blank line comes before the heading.
5. Step C: wrote `git show HEAD:<path>` to /tmp/scrub-final/<path>, applied the same perl edit at the HEAD line (47, 1099, 635), and appended the same note to the report blob. Checked the report blob with cmp and the HANDOFF and DECISION_LOG lines with diff (results below).
6. Steps D and E: verification, below. Used no git command that writes (only `git show`, `git diff`, `git ls-files -s`, all read-only).
7. Process note: the first attempt to write this report used a shell heredoc. The PreToolUse hook gate-commit.sh denied it because the prose contained the word for recording a change in git next to a ` -- ` pathspec. Nothing ran. The report was then put together from template files written with the Write tool.

## Verification evidence (command output)

All output below is masked. In the compact block, the change is shown as a 40-character window around the edit instead of the full table row.

```
===== DECISION_LOG.md
$ diff <(git show HEAD:DECISION_LOG.md) /tmp/scrub-final/DECISION_LOG.md | M   [hunk headers + 40-char context around the change]
47c47
< 	bypassed); Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers OPEN, never conside
> 	bypassed); Q2 Dev-B 16:00 flat vs 11:30/session window breakers OPEN, never conside
diff body line count: 4
$ git diff --numstat HEAD -- DECISION_LOG.md
4	1	DECISION_LOG.md
$ grep -ciF -- "$TERM" DECISION_LOG.md  ->  0
$ grep -ciF -- "$TERM" /tmp/scrub-final/DECISION_LOG.md  ->  0
wc -l HEAD / landing / working: 788 / 788 / 791
$ diff /tmp/scrub-pre/DECISION_LOG.md DECISION_LOG.md | M   [hunk headers]
47c47
pre-vs-wt diff body line count: 4
===== HANDOFF.md
$ diff <(git show HEAD:HANDOFF.md) /tmp/scrub-final/HANDOFF.md | M   [hunk headers + 40-char context around the change]
1099c1099
< 	`ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers), `zd4` (P1, Q6 pra
> 	`ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/session window breakers), `zd4` (P1, Q6 pra
diff body line count: 4
$ git diff --numstat HEAD -- HANDOFF.md
221	1	HANDOFF.md
$ grep -ciF -- "$TERM" HANDOFF.md  ->  0
$ grep -ciF -- "$TERM" /tmp/scrub-final/HANDOFF.md  ->  0
wc -l HEAD / landing / working: 1554 / 1554 / 1774
$ diff /tmp/scrub-pre/HANDOFF.md HANDOFF.md | M   [hunk headers]
1319c1319
pre-vs-wt diff body line count: 4
===== docs/reports/2026-11-09-d11-sweep-manager.md
$ diff <(git show HEAD:docs/reports/2026-11-09-d11-sweep-manager.md) /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md | M   [hunk headers + 40-char context around the change]
635c635
2231a2232,2235
< 	ax4 ("which of {11:30 gate, 16:00 flat, XTERMX disable} governs the anchor
> 	ax4 ("which of {11:30 gate, 16:00 flat, session window disable} governs the anchor
> 	> 
> 	> 
diff body line count: 9
$ git diff --numstat HEAD -- docs/reports/2026-11-09-d11-sweep-manager.md
5	1	docs/reports/2026-11-09-d11-sweep-manager.md
$ grep -ciF -- "$TERM" docs/reports/2026-11-09-d11-sweep-manager.md  ->  0
$ grep -ciF -- "$TERM" /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md  ->  0
wc -l HEAD / landing / working: 2231 / 2235 / 2235
$ diff /tmp/scrub-pre/docs/reports/2026-11-09-d11-sweep-manager.md docs/reports/2026-11-09-d11-sweep-manager.md | M   [hunk headers]
635c635
2231a2232,2235
pre-vs-wt diff body line count: 9
===== landing-vs-working checks
cmp report landing == working: identical
HANDOFF wt:1319 vs landing:1099 -> empty diff
DECISION_LOG wt:47 vs landing:47 -> empty diff
===== index
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ git ls-files -s -- docs/reports/evidence/2026-10-28-mffu-davi-reply.png
100644 458f3dafa0b54d3be6e3d054098a73e014608106 0	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```

Full masked diff for the sweep-manager report (HEAD vs landing blob; the working copy is byte-identical to the landing blob per cmp above):

```
635c635
< - ax4 ("which of {11:30 gate, 16:00 flat, XTERMX disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02 (breakers #4/#5); NOTE only.
---
> - ax4 ("which of {11:30 gate, 16:00 flat, session window disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02 (breakers #4/#5); NOTE only.
2231a2232,2235
> 
> ## De-identification note 2026-11-10
> 
> Line 635 was redacted in place on 2026-11-10 under D-2026-08-06-A (DECISIONS.md:1144-1152) and the master's decision of record (DECISION_LOG row 2026-11-10T09:08:00Z): one withheld term was replaced with "session window" (Amear's words). No other line of this report was changed. History was not rewritten; earlier commits keep the original text.
```

Numstat readings: DECISION_LOG.md and HANDOFF.md already carried uncommitted rows before this unit (3/0 and 220/0 at step A). After the edit they read 4/1 and 221/1, so this unit added exactly one changed line to each. The pre-vs-working diff for each file is one `NcN` hunk of 4 lines. The report went from 0/0 to 5/1: one changed line plus four appended lines.

## Result: PASS

- Term count after the edit is 0 in all 3 working copies and 0 in all 3 landing blobs (it was 1 each in HEAD and in the working tree before).
- The report landing blob is byte-identical to the working copy. The HANDOFF wt:1319 and landing:1099 lines are identical. The DECISION_LOG line 47 is identical in both.
- The index is unchanged. `git diff --cached --name-only` lists only the PNG, and its staged blob is 458f3dafa0b54d3be6e3d054098a73e014608106.
