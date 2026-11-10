# 2026-11-10 scrub-forward (bead Praxis_build-8ux): manager report

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Forward de-identification of the withheld term in the 3 tracked files that still hold it at HEAD `0eea766`. The term is a brand name and is never typed, printed or pasted here. The work is one in-place line edit per file, replacing the term with "session window" (Amear's words, DECISIONS.md:1144). No history rewrite, no force-push, no commit, and the real git index is not touched. The landing blobs are at `/tmp/scrub-final/<path>`: HEAD plus the scrub edit only, plus the appended note for the report.

How the term is handled: `eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"` sets SRC and TERM. Only `TERM-nonempty` and counts are ever shown. Any display that could include the line text goes through a literal, case-insensitive mask (`/tmp/scrub-mask.sh`, function `M`). The mask replaces the term with `XTERMX` and aborts if TERM is empty. The first mask attempt read the environment variable TERM, which is not exported in this shell. It matched the empty string, which the output showed (path-only output, so nothing leaked). It was replaced by the helper, which passes `T="$TERM"` explicitly, and the helper's probe is pasted below.

## Rubric criteria addressed

- **S1:** every claim below has pasted output.
- **S2:** the level claimed is "edited and verified in the working tree and in the landing blobs". It is not "landed": nothing is committed.
- **S4:** authority is D-2026-08-06-A (DECISIONS.md:1144-1152) plus the master decision of record, DECISION_LOG row 2026-11-10T09:08:00Z (working tree line 791). Both were written before this work.
- **S6:** see the section below.
- **S13:** the sentence appears once, at the top.
- **Unit-specific criterion:** see V3 to V6.

## Workers dispatched (id, mode, outcome)

| id | mode | scope | outcome |
|---|---|---|---|
| a5317c974c14c6f07 | BUILD | 3 one-line edits in the working tree, landing blobs in /tmp/scrub-final, appended note in the d11 report; report docs/reports/2026-11-10-scrub-forward-worker1.md | PASS. Re-verified by the manager in V3 to V5. |
| a224cf40a9efdafd5 | ADVERSARIAL | Re-derived TERM on its own with its own mask; positive controls; diff shape; wider scan; S6 hunt; report docs/reports/2026-11-10-scrub-forward-adversarial.md | Checks 1-7 and 9 PASS. Check 8 (S6) FAIL, on a documentation dependency (see Adversarial findings). |

## Process log

1. Read DECISION_LOG row 2026-11-10T09:08:00Z, DECISIONS.md:1140-1155 and the D9 method (d9-housekeeping-manager.md:352-358, 722-745), all with the mask applied.
2. Located the 3 occurrences at HEAD by path and line (V1). Read the lines with the mask applied (V2).
3. Scanned the working tree, untracked and ignored files under docs/, and the index (V6).
4. Dispatched the BUILD worker. Its first report write was denied by gate-commit.sh because of a word sequence in its text. Nothing ran, and it rewrote the report.
5. Re-ran every verification myself (V3 to V5).
6. Appended MANIFEST.md row 341 myself. This is a single-line ledger edit (V7).
7. Dispatched the ADVERSARIAL worker with the artifact and the criterion only, not the build worker's reasoning.
8. Confirmed the adversarial worker changed no repo file other than its own report (V8).

## Verification evidence (command output)

### V0. Term extraction and mask liveness
```
$ eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"; [ -n "$TERM" ] && echo TERM-nonempty; echo "len=${#TERM}"
TERM-nonempty
len=7
$ . /tmp/scrub-mask.sh; echo "probe: x${TERM}y" | M; echo "probe-upper: x$(echo "$TERM" | tr a-z A-Z)y" | M
probe: xXTERMXy
probe-upper: xXTERMXy
$ grep -noE '^[A-Za-z_]+=' /tmp/d9-build/evidence.sh | head -20
2:SRC=
3:TERM=
```

### V1. Occurrences at HEAD (path:line only)
```
$ git rev-parse --short HEAD
0eea766
$ git grep -ilF -- "$TERM" HEAD -- . | M
HEAD:DECISION_LOG.md
HEAD:HANDOFF.md
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md
$ git grep -niF -- "$TERM" HEAD -- . | cut -d: -f1-3 | M
HEAD:DECISION_LOG.md:47
HEAD:HANDOFF.md:1099
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md:635
$ git grep -ciF -- "$TERM" HEAD -- . | M
HEAD:DECISION_LOG.md:1
HEAD:HANDOFF.md:1
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md:1
```
(The first run of these used the broken mask, which matched the empty string. The output was path-only, and it was re-derived with the fixed mask; the values are the same.)

### V2. Before state: working-tree position, counts, numstat
```
== DECISION_LOG.md HEAD-lines=788 WT-lines=791 WT-count=1 WT-pos=47
3	0	DECISION_LOG.md
== HANDOFF.md HEAD-lines=1554 WT-lines=1774 WT-count=1 WT-pos=1319
220	0	HANDOFF.md
== docs/reports/2026-11-09-d11-sweep-manager.md HEAD-lines=2231 WT-lines=2231 WT-count=1 WT-pos=635
$ cmp <(sed -n 1319p HANDOFF.md) <(git show HEAD:HANDOFF.md | sed -n 1099p) && echo identical
identical
```
(The d11 report had no numstat line: working tree == HEAD.)

### V3. Itemised edits: before/after, masked (diff of HEAD vs landing blob)
```
=== HANDOFF.md
$ diff <(git show HEAD:HANDOFF.md) /tmp/scrub-final/HANDOFF.md | M
1099c1099
< - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
---
> - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/session window breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
$ diff /tmp/scrub-pre/HANDOFF.md HANDOFF.md | M  (working-tree delta from the edit)
1319c1319
< - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
---
> - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/session window breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
=== docs/reports/2026-11-09-d11-sweep-manager.md
$ diff <(git show HEAD:docs/reports/2026-11-09-d11-sweep-manager.md) /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md | M
635c635
< - ax4 ("which of {11:30 gate, 16:00 flat, XTERMX disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02 (breakers #4/#5); NOTE only.
---
> - ax4 ("which of {11:30 gate, 16:00 flat, session window disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02 (breakers #4/#5); NOTE only.
2231a2232,2235
> 
> ## De-identification note 2026-11-10
> 
> Line 635 was redacted in place on 2026-11-10 under D-2026-08-06-A (DECISIONS.md:1144-1152) and the master's decision of record (DECISION_LOG row 2026-11-10T09:08:00Z): one withheld term was replaced with "session window" (Amear's words). No other line of this report was changed. History was not rewritten; earlier commits keep the original text.
$ cmp /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md docs/reports/2026-11-09-d11-sweep-manager.md && echo "report landing == working copy"
report landing == working copy
```
DECISION_LOG.md line 47 is a single long row, so only the edited fragment is shown. The rest of the line is proven byte-identical.
```
$ diff <(git show HEAD:DECISION_LOG.md) /tmp/scrub-final/DECISION_LOG.md | M | cut -c1-60
47c47
< | 2026-07-25 (session 30) | WHO: Claude.ai master/scoping
---
> | 2026-07-25 (session 30) | WHO: Claude.ai master/scoping
$ git show HEAD:DECISION_LOG.md | sed -n 47p | M | grep -o 'Q2 Dev-B[^;]*;'
Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers OPEN, never considered at approval;
$ sed -n 47p /tmp/scrub-final/DECISION_LOG.md | M | grep -o 'Q2 Dev-B[^;]*;'
Q2 Dev-B 16:00 flat vs 11:30/session window breakers OPEN, never considered at approval;
$ cmp <(git show HEAD:DECISION_LOG.md | sed -n 47p | M | sed 's#11:30/XTERMX breakers#X#') <(sed -n 47p /tmp/scrub-final/DECISION_LOG.md | sed 's#11:30/session window breakers#X#') && echo identical-outside-fragment
identical-outside-fragment
$ diff /tmp/scrub-pre/DECISION_LOG.md DECISION_LOG.md | M | cut -c1-12   (working-tree delta from the edit)
47c47
< | 2026-07-25
---
> | 2026-07-25
```

Itemised edit table:

| path | HEAD line | working-tree line | before (masked) | after |
|---|---|---|---|---|
| DECISION_LOG.md | 47 | 47 | `11:30/XTERMX breakers` | `11:30/session window breakers` |
| HANDOFF.md | 1099 | 1319 | `11:30/XTERMX breakers` | `11:30/session window breakers` |
| docs/reports/2026-11-09-d11-sweep-manager.md | 635 | 635 | `16:00 flat, XTERMX disable}` | `16:00 flat, session window disable}`, plus appended note lines 2232-2235 |

### V4. Counts after (expect 0), and line counts
```
DECISION_LOG.md: counts: HEAD=1 landing=0 wt=0 pre=1 | lines: HEAD=788 landing=788 wt=791
HANDOFF.md: counts: HEAD=1 landing=0 wt=0 pre=1 | lines: HEAD=1554 landing=1554 wt=1774
docs/reports/2026-11-09-d11-sweep-manager.md: counts: HEAD=1 landing=0 wt=0 pre=1 | lines: HEAD=2231 landing=2235 wt=2235
```
Counter liveness: `pre=1` and `HEAD=1` come from the same `grep -ciF -- "$TERM"`. The adversarial worker also injected the term into each landing stream, as-is and upper-cased, and got 1 each time (see Adversarial findings).

### V5. numstat after (vs before in V2) and the real index
```
$ git diff --numstat HEAD -- DECISION_LOG.md
4	1	DECISION_LOG.md
$ git diff --numstat HEAD -- HANDOFF.md
221	1	HANDOFF.md
$ git diff --numstat HEAD -- docs/reports/2026-11-09-d11-sweep-manager.md
5	1	docs/reports/2026-11-09-d11-sweep-manager.md
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ find /tmp/scrub-final -type f
/tmp/scrub-final/DECISION_LOG.md
/tmp/scrub-final/HANDOFF.md
/tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md
```

### V6. Wider scan (counts and safe paths only; taken before the edit)
```
tracked WT files with term:
       3
DECISION_LOG.md
HANDOFF.md
docs/reports/2026-11-09-d11-sweep-manager.md
untracked docs/ files with term:
       0
untracked docs/ total files:       73
ignored docs/ files with term:        0
index blobs with term:
       3
```
The 3 index blobs are the unstaged HEAD copies of the same 3 files. The index is the master's to rebuild from /tmp/scrub-final. After the edit, the adversarial worker re-ran the scan and reported 0 of 77 untracked files under docs/. My own re-run after the edit, with the 3 new reports present, is below. Its 76 differs from the worker's 77, and this is not explained; both counts are 0 for the term.
```
$ echo "tracked WT files with term: $(git ls-files -z | xargs -0 grep -ilF -- "$TERM" 2>/dev/null | wc -l | tr -d ' ')"
tracked WT files with term: 0
$ echo "untracked docs/ files with term: ... of ..."
untracked docs/ files with term: 0 of 76
report self-check: term=0 placeholder-token=0 s13=1 result=1 vsec=1
docs/reports/2026-11-10-scrub-forward-worker1.md term=0
docs/reports/2026-11-10-scrub-forward-adversarial.md term=0
MANIFEST.md term=0
```

### V7. MANIFEST row
```
$ wc -l MANIFEST.md
     341 MANIFEST.md
$ diff /tmp/scrub-pre/MANIFEST.md MANIFEST.md | cut -c1-120
340a341
> | /docs/reports/2026-11-10-scrub-forward-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-scr
$ diff <(sed -n 307,314p /tmp/scrub-pre/MANIFEST.md) <(sed -n 307,314p MANIFEST.md) && echo "rows 307-314 unchanged"
rows 307-314 unchanged
```

### V8. The adversarial worker changed nothing it should not have
```
4	1	DECISION_LOG.md
221	1	HANDOFF.md
5	1	docs/reports/2026-11-09-d11-sweep-manager.md
9	0	MANIFEST.md
report-unchanged-since-worker1
ledger-lines-unchanged-since-worker1
```

## Adversarial findings

Worker a224cf40a9efdafd5 derived TERM and its mask on its own. Its full pasted output is in docs/reports/2026-11-10-scrub-forward-adversarial.md. Summary of its returns:

1. Term at HEAD in 3 files (the counter is live on history): PASS.
2. 0 in every landing blob and working copy. Prefixes of 4, 5 and 6 characters and space/hyphen/underscore variants also give 0: PASS.
3. Positive control: the term injected as-is and upper-cased gives 1 for every landing blob: PASS.
4. Each landing blob differs from HEAD only by the swap on the edited line, plus note lines 2232-2235 for the report. A perl substitution on the HEAD line matched the landing line byte for byte: PASS.
5. The working-copy lines equal the landing lines. The edited line is the only removed line (numstat 4/1, 221/1, 5/1): PASS.
6. Report cmp identical: PASS.
7. Wider scan 0, and the index holds only the PNG: PASS.
8. S6: FAIL, on a documentation dependency. docs/reports/2026-11-07-rulings-filing-manager.md:113-118 defines "superset token probe v2" (tokprobe2), and 5 later reports reuse it. Its candidate set is seeded from the tokens of `HEAD:DECISION_LOG.md:47`, and it uses that line as a known location for its liveness arm. Once these blobs land, the method re-run as written against the new HEAD can no longer see the term and could report clean. No gate, hook or hash depends on the lines: the only removed-line check in scripts covers AUDIT_LOG.md. The script itself is not in the repo.
9. MANIFEST row 341 is correct, and rows 307-314 are unchanged: PASS.

Minor finding: the appended note and MANIFEST:341 cite DECISION_LOG row 2026-11-10T09:08:00Z. That row is in the working tree (line 791) but not in HEAD or in the DECISION_LOG landing blob. The citation only resolves if the master's commit also carries the DECISION_LOG flush through 09:08Z.

Outside the criterion (reported, not edited): the term is still in the beads database (3 occurrences, including bead `ax4`'s title), and the beads remote is the same public repository. Five other branch tips still contain the term in history. The worker also notes that two of its searches showed DECISIONS.md:1144 in tool output. That line holds the category word and is already public at HEAD. Nothing was written from it.

Manager disposition of finding 8: I confirmed it by reading the adversarial report's evidence lines (211-262), with the mask applied. It is real. The brief limits my edits to the 3 HEAD files ("Do not edit other files; list them as open items"), and the rulings-filing report is append-only. The remedy is open item 1 below, for the master. Adding the pointer would make it a later unit's artifact, so no fix worker was dispatched.

## S6 cross-block check

Graded by name, the question is: does any spec, hook, or other tracked text quote or depend on the exact edited lines?
- **Hooks and scripts:** these name the files: .claude/hooks/precompact-handoff.sh (it tails DECISION_LOG `- [` rows only), scripts/master-write-guard.sh and scripts/master-bash-guard.sh (both allow-list the ledgers), scripts/audit-log-annotate.sh, scripts/audit-log-flush-verify.sh (its append-only removed-line check covers AUDIT_LOG.md only), scripts/praxis-inbound-control-watch.sh and scripts/tests/test-gate-handback.sh. None hashes, byte-compares or quotes DECISION_LOG.md:47, HANDOFF.md:1099 or d11-sweep-manager.md:635. Grep output:
```
scripts/master-write-guard.sh:14:  *DISPATCH_LOG.md|*DECISION_LOG.md|*ISSUE_REGISTER.md|*HANDOFF.md|*STATUS.md) exit 0 ;;
scripts/master-bash-guard.sh:14:    *DISPATCH_LOG.md*|*DECISION_LOG.md*|*ISSUE_REGISTER.md*|*HANDOFF.md*|*/specs/*|*/docs/reports/*) exit 0 ;;
.claude/hooks/precompact-handoff.sh:18:  grep '^- \[' "$ROOT/DECISION_LOG.md" 2>/dev/null | tail -3 || true
scripts/audit-log-flush-verify.sh:49:[ "$REMOVED" = "0" ] || die "flush must be append-only — staged diff removes/edits $REMOVED existing line(s)"
```
- **Line-number citations:** these cite the edited locations: DECISIONS.md:1150, DECISION_LOG.md:491 and :678, docs/reports/2026-11-07-rulings-filing-manager.md:23 and :114. The edits change no line counts (DECISION_LOG 788 = 788 and HANDOFF 1554 = 1554 at HEAD vs landing), so every location citation still resolves. DECISIONS.md:1148-1152 describes the term as present at those lines. That entry is now historical: the master's DECISION_LOG row 09:08Z supersedes its "stand as-is" clause, and the master appends the closing ledger row.
- **Dependency found:** yes. The tokprobe2 de-identification method (rulings-filing-manager.md:113-118, reused in 5 reports) seeds from, and liveness-checks against, `HEAD:DECISION_LOG.md:47`. After landing, it must be pinned to `0eea766` or re-seeded from the gitignored source the way the D9 method is. This is open item 1.
- **Specs:** no spec quotes the edited text. The breaker #5 behaviour (15:00-18:00 ET disable) is unchanged, because only the label in three prose lines changed.

## Open items (for the master; not edited by this unit)

1. **S6 pointer:** a pointer note is needed so that tokprobe2 (docs/reports/2026-11-07-rulings-filing-manager.md:113-118) reads `0eea766:DECISION_LOG.md:47`, not `HEAD:`, or re-seeds from the gitignored source.
2. **DECISION_LOG flush:** the commit that lands these blobs should carry the DECISION_LOG flush through row 2026-11-10T09:08:00Z, because the d11 report note and MANIFEST:341 cite it.
3. **Bead titles:** the beads database still holds the term (3 occurrences, including the `ax4` title), and its remote is public. A bead-title edit plus a `bd dolt push` needs the master's call.
4. **History:** history and the other branch tips keep the term. That stays Amear's call (bead 8ux).
5. **MANIFEST rows for the worker reports:** docs/reports/2026-11-10-scrub-forward-worker1.md and docs/reports/2026-11-10-scrub-forward-adversarial.md have no MANIFEST rows yet. The brief allowed one row, for this report.

## Files staged

Nothing staged; the real index is untouched (V5). Working-tree edits: DECISION_LOG.md:47, HANDOFF.md:1319 (HEAD :1099), docs/reports/2026-11-09-d11-sweep-manager.md:635 plus note lines 2232-2235, MANIFEST.md:341. New files: this report, docs/reports/2026-11-10-scrub-forward-worker1.md, docs/reports/2026-11-10-scrub-forward-adversarial.md. Landing blobs: /tmp/scrub-final/DECISION_LOG.md, /tmp/scrub-final/HANDOFF.md, /tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md.

Result: PASS

Basis: every unit-specific criterion is met with pasted evidence: counts are 0 in all 3 landing blobs and all 3 working copies, and every blob differs from HEAD only on the edited line, plus the note. The S6 test was run and answered by name. Its one finding (a documentation dependency) is outside this unit's edit scope and is open item 1. The adversarial worker graded that check FAIL, and that grade is kept above, not softened.

## Correction 1

Bead Praxis_build-8ux. Authority: DECISION_LOG row 2026-11-10T09:24:00Z (master, under D-2026-11-08-D D1, written before this work). Scope: open items 1, 3 and 5 above, as items (a)-(c) below. Lines 1-258 of this report were not edited. The hashes are in C1-V0 and C1-V9.

The term was handled as before: `eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"`, `TERM-nonempty`, counts only, and `/tmp/scrub-mask.sh` (function M) on anything that could carry text. SRC was never printed. Bead text is shown only as short masked fragments, because the full descriptions hold other text that this report must not carry.

### Rubric criteria addressed (Correction 1)

- **S1:** every claim below rests on pasted output. The final state is re-pasted last, in C1-V8, after the final edit.
- **S2:** the level claimed is "edited and verified in the working tree, the beads database and the landing blob". Nothing is landed or pushed. For beads the claim covers **current fields only**: bead history still holds the term (C1-V8).
- **S6:** see "S6 cross-block check (Correction 1)" below.
- **S13:** not re-added. The sentence appears once, at line 3.

### Items

**(a) S6 pointer.** docs/reports/2026-11-07-rulings-filing-manager.md was tracked and identical to HEAD (450 lines) before the edit. A section "## Pointer note 2026-11-10 (filer's note, not a ruling)" was appended at lines 451-454, and nothing above it changed. The note says that tokprobe2 seeds from `HEAD:DECISION_LOG.md:47` and liveness-checks the whole of `HEAD:DECISION_LOG.md` (plus the pinned `7d9be8e:HANDOFF.md`). A re-run must read the `0eea766:` forms instead, or extract the term from the gitignored source the way the d9-housekeeping V5 method does. Landing blob: /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md = HEAD + the note, `cmp`-identical to the working copy. The first version of the note said that the liveness arm "runs on that location" (:47). The adversarial worker showed that it runs on the whole file (LIVENESS line 120), so the note was rewritten before it landed. Every sentence of the final note is checked in C1-V1.

**(b) Beads.** Before the edit there were 3 occurrences across the 129 beads, open and closed: Praxis_build-r8j `description` (1, status closed) and Praxis_build-ax4 `description` (2, status open). Titles, notes and comments held none. The predecessor's "including the `ax4` title" is not borne out: the observed title count was 0 (C1-V4). The other `bd show` hits (2nh, qtk, yra, and ax4's dependency block) are r8j's description embedded as a dependency, not separate sources. Edits: `bd update Praxis_build-r8j --body-file <NEW>` and `bd update Praxis_build-ax4 --body-file <NEW>`. NEW was computed by `perl s/\Q$TERM\E/session window/gi` and never typed or printed. No comment held the term, so no comment edit was needed. No `bd dolt push`, no `bd sync`, and no git write was run.

**(c) MANIFEST.** Rows were appended at lines 342 (worker1 report), 343 (adversarial report) and 344. Row 344 is a third, MODIFIED-style row for the rulings-filing report, because (a) modified that tracked file. The precedent is the "MODIFIED" rows at :205-212, and the project rule is "Update MANIFEST.md when creating or modifying files". Row 343 first said "finding 8". The adversarial report files it as Check 8, so the row was corrected to "Check 8". Rows 307-314 are unchanged by this correction (C1-V8).

**(d)** This section. The final evidence is re-pasted last (C1-V8 and C1-V9).

### Workers dispatched (Correction 1)

| id | mode | scope | outcome |
|---|---|---|---|
| a37f385143edfaac8 | ADVERSARIAL (foreground) | Attack (a)-(c) and the index, given the artifacts and S1/S2/S6 only; report docs/reports/2026-11-10-scrub-forward-c1-adversarial.md | A PASS, B PASS on current fields, C FAIL (row 343 "finding 8"), D PASS. Findings handled below. |

The (a)-(c) edits were made by the manager: each is a pure doc or ledger append, or a single `bd update` per bead. No BUILD worker was used (the brief allowed this: "you may do it yourself with at most one worker").

### Process log (Correction 1)

1. Recorded the hash of lines 1-258 (C1-V0) and wrote the Correction 1 skeleton first.
2. (a): checked :113-121 masked, the counts at 0eea766, at the working copy and at 7d9be8e, and SRC's ignore status. Wrote the note. The first attempt was a heredoc in Bash, and gate-commit.sh denied it: "Commit denied: a pathspec after ' -- ' commits a different set than what was audited". The note text contained the word "commit", and the same command held a `grep -ciF -- `. Nothing ran. The note was written with the Write tool, and the command was re-run without ` -- `.
3. (b): dumped `bd list --all --json`, `bd show --json` for all 129 beads and `bd comments --json` for the 11 beads with comments. Located the term by id and field, built NEW, proved it is substitution-only (C1-V4), ran `bd update`, then re-dumped everything (C1-V8).
4. (c): appended 3 MANIFEST rows.
5. Dispatched one ADVERSARIAL worker in the foreground.
6. Checked its findings myself (C1-V6). Fixed the row 343 label and the liveness wording in the note. Rebuilt the landing blob and the working copy.
7. Re-pasted all final evidence last.

### Verification evidence (command output), Correction 1

#### C1-V0. Hash of lines 1-258 before the first append
```
$ head -n 258 docs/reports/2026-11-10-scrub-forward-manager.md | openssl dgst -sha256
SHA2-256(stdin)= 1d93d164ac19ebfd50360d48a2d1add55733fa34c3c707f6c370a034ae588c3f
```

#### C1-V1. (a) The note's facts
```
$ sed -n 113,118p docs/reports/2026-11-07-rulings-filing-manager.md | M
**De-identification probe.** Superset token probe v2: `scratchpad/tokprobe2.sh`.
- **Candidate set:** alpha tokens of length ≥ 4 on HEAD:DECISION_LOG.md:47, which is one known location per D-2026-08-06-A. From these it removes the tokens of HEAD:DECISIONS.md and HEAD:SPEC_RUBRIC.md, intersects with 7d9be8e:HANDOFF.md (the other introducing commit), and removes the tokens of `a42038e^`:DECISION_LOG.md.
- **Storage:** the candidates are held in a shell variable only.
- **Liveness:** the liveness arm runs the same per-file loop on the two known locations.
- **Output:** counts and line numbers only.
~~~
$ grep -n '^LIVENESS' docs/reports/2026-11-07-rulings-filing-manager.md | cut -d' ' -f1-2
120:LIVENESS HEAD:DECISION_LOG.md
121:LIVENESS 7d9be8e:HANDOFF.md
$ git show 0eea766:DECISION_LOG.md | sed -n 47p | grep -ciF "$TERM"
1
$ sed -n 47p DECISION_LOG.md | grep -ciF "$TERM"          (working copy)
0
$ sed -n 47p /tmp/scrub-final/DECISION_LOG.md | grep -ciF "$TERM"
0
$ git show HEAD:DECISION_LOG.md | grep -niF "$TERM" | cut -d: -f1     (lines with the term at HEAD)
47
$ git show 0eea766:DECISION_LOG.md | grep -ciF "$TERM"    (whole file)
1
$ grep -ciF "$TERM" /tmp/scrub-final/DECISION_LOG.md     (whole file, landing)
0
$ git show 7d9be8e:HANDOFF.md | grep -ciF "$TERM"
1
$ sed -n 352p docs/reports/2026-11-10-d9-housekeeping-manager.md | M
### V5. The withheld term: extracted at runtime from the gitignored source into $TERM, never typed or printed; counts only
$ git check-ignore -q "$SRC" && echo SRC-gitignored; git ls-files --error-unmatch "$SRC" >/dev/null 2>&1 && echo SRC-tracked || echo SRC-untracked
SRC-gitignored
SRC-untracked
$ grep -ciF "$TERM" /tmp/c1-note.txt
0
```
The note refers to the term only as "the withheld term"; its full text is in the C1-V8 diff. The rest of the note: "bead Praxis_build-8ux; DECISION_LOG row 2026-11-10T09:08:00Z" resolves at working-tree DECISION_LOG.md:791, but not yet at HEAD (open item C1-3). "No line above this note was changed" is shown by the diff in C1-V8.

#### C1-V2. (a) The landing blob and the working copy
```
$ { git show HEAD:docs/reports/2026-11-07-rulings-filing-manager.md; cat /tmp/c1-note.txt; } > /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md
$ cp /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md docs/reports/2026-11-07-rulings-filing-manager.md
$ cmp /tmp/scrub-final/<p> <p> && echo "landing == working copy"; wc -l <p>
landing == working copy
     454 docs/reports/2026-11-07-rulings-filing-manager.md
```
Before the edit, the file was identical to HEAD: `cmp <(git show HEAD:<p>) <p> && echo wt-identical-to-HEAD` printed `wt-identical-to-HEAD`, `git diff --numstat HEAD -- <p>` printed nothing, and `wc -l` was 450.

#### C1-V3. (b) Locating the term in beads (before)
```
$ bd list --all --json > /tmp/c1-bd-all.json; jq length
129
list-json term count: 3
$ jq ... (id, field holding the term)
Praxis_build-r8j description
Praxis_build-ax4 description
$ per-field counts (title, description, notes)
Praxis_build-r8j title 0
Praxis_build-r8j description 1
Praxis_build-r8j notes 0
Praxis_build-ax4 title 0
Praxis_build-ax4 description 2
Praxis_build-ax4 notes 0
$ bd show <id> --json for all 129: files with term
Praxis_build-2nh.json
Praxis_build-ax4.json
Praxis_build-r8j.json
Praxis_build-qtk.json
Praxis_build-yra.json
show-json total term occurrences: 7
$ json paths holding the term
-- 2nh: dependencies.0.description
-- ax4: description, dependencies.0.description
-- r8j: description
-- qtk: dependencies.0.description
-- yra: dependencies.0.description
$ ids of the embedded dependency blocks (2nh, qtk, yra)
   3 Praxis_build-r8j
$ bd comments <id> --json for the 11 beads with comment_count>0
comment files with term: 0      (11 files, 16239 bytes total)
$ status before
Praxis_build-r8j closed 2026-11-06T14:39:28Z
Praxis_build-ax4 open 2026-07-25T16:15:16Z
```
Of the 7 `bd show` hits, 4 are r8j's description embedded in the dependency block of ax4, 2nh, qtk and yra. That leaves 3 sources: r8j (1) and ax4 (2).

#### C1-V4. (b) NEW is the before text with only the term replaced, and the updates
```
Praxis_build-r8j before=1 new=0 bytes 977->984
Praxis_build-ax4 before=2 new=0 bytes 953->967
$ M </tmp/c1-bd-before/Praxis_build-r8j.desc | sed 's/XTERMX/session window/g' | cmp - /tmp/c1-bd-new/Praxis_build-r8j.desc
  identical: only the term changed
  bd update Praxis_build-r8j --body-file <new> rc=0
$ M </tmp/c1-bd-before/Praxis_build-ax4.desc | sed 's/XTERMX/session window/g' | cmp - /tmp/c1-bd-new/Praxis_build-ax4.desc
  identical: only the term changed
  bd update Praxis_build-ax4 --body-file <new> rc=0
```
The byte deltas (+7 for 1 occurrence, +14 for 2) match a 7-character term replaced by the 14-character "session window".

#### C1-V6. The manager's check of the adversarial findings
```
$ grep -niE 'finding 8|^### Check 8|finding 1' docs/reports/2026-11-10-scrub-forward-adversarial.md | cut -c1-90
33:| 8 | S6: no gate would trip, and no verbatim quote of the edited fragments exists outs
176:### Check 8 (S6)
$ bd history Praxis_build-r8j > /tmp/c1-hist.txt; wc -c; grep -oiF "$TERM" | wc -l      (text form)
   48472
r8j history file occurrences: 0
$ bd history Praxis_build-r8j --json > /tmp/c1-hist.json; echo "bytes=$(wc -c </tmp/c1-hist.json)"; grep -oiF "$TERM" /tmp/c1-hist.json | wc -l
rc=0 bytes=  291107 err=       0
json occurrences: 156
$ jq 'type, length' /tmp/c1-hist.json
"array" 158
$ sed -n 6p scripts/gate-manager-output.sh
LATEST=$(ls -t "$DIR"/docs/reports/*.md 2>/dev/null | head -1)
$ ls -t docs/reports/*.md | head -3      (taken after the worker returned, before the fixes)
docs/reports/2026-11-10-scrub-forward-c1-adversarial.md
docs/reports/2026-11-07-rulings-filing-manager.md
docs/reports/2026-11-10-scrub-forward-manager.md
```
My first history probe (`bd history r8j --json`, short id) printed 0 for both beads. That 0 was a wrong-argument artifact. The text form truncates descriptions and also gives 0. The full-id `--json` form gives 156, which matches the worker's figure. The worker's figure stands.

### Adversarial findings (Correction 1)

Worker a37f385143edfaac8. Its pasted output is in docs/reports/2026-11-10-scrub-forward-c1-adversarial.md.

1. **C FAIL, row 343 said "finding 8".** Confirmed (C1-V6: the adversarial report has "### Check 8 (S6)" at :176 and no "finding 8"). Fixed: the row now says "Check 8" (C1-V8 tail).
2. **A, imprecision in the note.** The note said that the liveness arm runs on line 47, but line 120 shows it runs on the whole of `HEAD:DECISION_LOG.md`. Confirmed and fixed: the note now names the whole file for the liveness arm and line 47 for the seed. The term is on line 47 only at HEAD (C1-V1).
3. **B, bead history keeps the term.** `bd history <id> --json` returns it 156 times for r8j (I re-ran this: C1-V6) and 310 times for ax4 (the worker's figure; I did not re-run ax4 in JSON form). The worker also reports the term in the embedded Dolt store and in 4 gitignored backup files under .beads/, and that Dolt has an `origin` remote. This is within the decision ("no dolt history rewrite"). The claim made here is therefore "current fields: 0", not "beads clean". Open item C1-1.
4. **S6, gate cross-effect.** gate-manager-output.sh grades only the newest-mtime report (C1-V6, line 6). Appending to the old rulings-filing report made it the newest file for a while, and its own `Result: PASS` (old line 450) would then have satisfied the gate for this manager's return. Handled here: this report is written last, so it is the newest (C1-V8 `ls -t`). The fragility is general. Open item C1-2.

### S6 cross-block check (Correction 1)

The question, by name: does any spec, hook, script or other tracked text depend on the edited bead text, on the end of the rulings-filing report, or on MANIFEST row positions after :341?
- **Hooks and scripts:** grepping scripts/ and .claude/hooks/ for `rulings-filing-manager`, `r8j` and `ax4` gives no hits. Two files match `.description`: gate-commit.sh:547 and scripts/tests/test-gate-handback.sh:74-117. Both read the `.input.description` of a tool call, not bead text:
```
.claude/hooks/gate-commit.sh:547:        | .input.description? ] as $d
scripts/tests/test-gate-handback.sh:79:DESC9=$(jq -r '.message.content[] | select(type == "object" and .type == "tool_use") | .input.description' "$HB
```
- **The gate that does depend on the last report:** scripts/gate-manager-output.sh (finding 4 above). Handled by write order. Open item C1-2.
- **tokprobe2 reusers:** the worker reports that 4 of the 5 reusing reports cite rulings:113 and that none cites DECISION_LOG.md:47 directly. The pointer note sits in the file they cite.
- **Specs:** the bead edits change a label in two prose descriptions. The breaker #5 behaviour (15:00-18:00 ET disable) is unchanged. The ax4 title, which names that window by its hours, was not touched.
- **MANIFEST:** rows were appended after :341, so no earlier row moved. Rows 307-314 are unchanged versus the pre-correction copy (C1-V8).

### Open items (Correction 1; for the master, not edited here)

1. **C1-1, bead history and the remote.** Bead history (`bd history --json`), the Dolt store and the .beads backups still hold the term. The decision for this correction schedules a `bd dolt push` at session close. That push publishes the new values. Whether it also pushes history that the remote does not already hold has not been checked.
2. **C1-2, gate-manager-output.sh picks LATEST by mtime.** Any append to an older report can make that report the one graded. A more robust fix (for example, gating on the path named in the manager's return) is a hook change and outside this scope.
3. **C1-3, DECISION_LOG flush.** The pointer note and MANIFEST row 344 cite DECISION_LOG rows 2026-11-10T09:08:00Z and 09:24:00Z. Both are in the working tree only. This is the same point as open item 2 above.
4. **C1-4, no MANIFEST row for docs/reports/2026-11-10-scrub-forward-c1-adversarial.md.** The brief allowed 2 rows plus one for (a). This file was created by this correction's worker.
5. **C1-5, wording in r8j.** The mechanical replacement gives "the session window window AS A SPEC" in r8j (C1-V8 fragment). It reads oddly, but it is what the decided substitution produces, and it was not hand-edited.
6. **C1-6, MANIFEST rows 307-314 versus HEAD.** They differ from HEAD because of working-tree edits that were made before this unit (MANIFEST.md was already `M` at session start). They are unchanged by this unit and by this correction.

### Files staged (Correction 1)

Nothing staged, and the real index is untouched (C1-V8: the PNG only). Working-tree edits: docs/reports/2026-11-07-rulings-filing-manager.md (lines 451-454 appended), MANIFEST.md (rows 342-344 appended) and this report (Correction 1 appended). Beads database: descriptions of Praxis_build-r8j and Praxis_build-ax4 (not pushed). New file: docs/reports/2026-11-10-scrub-forward-c1-adversarial.md (written by the worker). New landing blob: /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md.

#### C1-V8. Final evidence, re-pasted last (run after the final edit to every file except this report's own tail)
```
TERM-nonempty
$ for f in $(find /tmp/scrub-final -type f | sort); do term count; done      (landing blobs)
/tmp/scrub-final/DECISION_LOG.md term=0
/tmp/scrub-final/HANDOFF.md term=0
/tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md term=0
/tmp/scrub-final/docs/reports/2026-11-09-d11-sweep-manager.md term=0
$ for each edited or new working copy: term count
DECISION_LOG.md term=0
HANDOFF.md term=0
docs/reports/2026-11-09-d11-sweep-manager.md term=0
docs/reports/2026-11-07-rulings-filing-manager.md term=0
MANIFEST.md term=0
docs/reports/2026-11-10-scrub-forward-manager.md term=0
docs/reports/2026-11-10-scrub-forward-worker1.md term=0
docs/reports/2026-11-10-scrub-forward-adversarial.md term=0
docs/reports/2026-11-10-scrub-forward-c1-adversarial.md term=0
positive control, same counter, term injected into the rulings landing blob stream: 1
positive control, upper-cased: 1

$ diff <(git show HEAD:docs/reports/2026-11-07-rulings-filing-manager.md) /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md | M
450a451,454
> 
> ## Pointer note 2026-11-10 (filer's note, not a ruling)
> 
> The "superset token probe v2" method at lines 113-118 above seeds its candidate set from `HEAD:DECISION_LOG.md:47` (line 114). Its liveness arm (line 116) runs on the whole of `HEAD:DECISION_LOG.md` and on `7d9be8e:HANDOFF.md`, as the two LIVENESS lines at 120-121 show; in `HEAD:DECISION_LOG.md` the withheld term is on line 47 only. From the scrub-forward commit on (bead Praxis_build-8ux; DECISION_LOG row 2026-11-10T09:08:00Z), `DECISION_LOG.md:47` no longer carries the withheld term. A re-run must therefore read `0eea766:DECISION_LOG.md:47` for the seed and `0eea766:DECISION_LOG.md` for the liveness arm, instead of the `HEAD:` forms, or extract the term from the gitignored source, as docs/reports/2026-11-10-d9-housekeeping-manager.md V5 does. The `7d9be8e:HANDOFF.md` arm is pinned to a commit and is not affected. No line above this note was changed.
$ cmp /tmp/scrub-final/docs/reports/2026-11-07-rulings-filing-manager.md docs/reports/2026-11-07-rulings-filing-manager.md && echo landing-equals-working-copy
landing-equals-working-copy
$ cmp <(head -n 450 docs/reports/2026-11-07-rulings-filing-manager.md) <(git show HEAD:docs/reports/2026-11-07-rulings-filing-manager.md) && echo lines-1-450-identical-to-HEAD
lines-1-450-identical-to-HEAD

$ git diff --numstat HEAD (each edited tracked path)
5	1	DECISION_LOG.md
221	1	HANDOFF.md
5	1	docs/reports/2026-11-09-d11-sweep-manager.md
4	0	docs/reports/2026-11-07-rulings-filing-manager.md
12	0	MANIFEST.md
$ git ls-files --error-unmatch docs/reports/2026-11-10-scrub-forward-manager.md >/dev/null 2>&1 || echo untracked
untracked (no numstat line; new file)

$ wc -l MANIFEST.md; tail -n 3 MANIFEST.md | cut -c1-140
     344 MANIFEST.md
| /docs/reports/2026-11-10-scrub-forward-worker1.md | Report | 2 | 2026-11-10 | BUILD worker report for unit 2026-11-10-scrub-forward (bead 
| /docs/reports/2026-11-10-scrub-forward-adversarial.md | Report | 2 | 2026-11-10 | ADVERSARIAL worker report for unit 2026-11-10-scrub-forw
| /docs/reports/2026-11-07-rulings-filing-manager.md | Report | 2 | 2026-11-10 | MODIFIED (bead Praxis_build-8ux Correction 1; DECISION_LOG 
$ diff /tmp/c1-manifest-pre.md MANIFEST.md | cut -c1-60
341a342,344
> | /docs/reports/2026-11-10-scrub-forward-worker1.md | Repo
> | /docs/reports/2026-11-10-scrub-forward-adversarial.md | 
> | /docs/reports/2026-11-07-rulings-filing-manager.md | Rep
$ diff <(sed -n 307,314p /tmp/c1-manifest-pre.md) <(sed -n 307,314p MANIFEST.md) && echo ...
rows 307-314 unchanged vs pre-correction copy
$ diff <(sed -n 307,314p /tmp/scrub-pre/MANIFEST.md) <(sed -n 307,314p MANIFEST.md) && echo ...
rows 307-314 unchanged vs pre-unit copy
$ grep -c "finding 8" MANIFEST.md; sed -n 343p MANIFEST.md | grep -o "S6 hunt ([^:]*:"
0
S6 hunt (Check 8:

$ beads after: bd list --all --json; bd show <id> --json for every id; bd comments <id> --json where comment_count>0
beads: 129
show files: 129 comment files: 11
AFTER  list=0 show=0 comments=0
BEFORE list=3 show=7 comments=0
positive control (as-is, list stream): 1
positive control (upper, show stream): 1
Praxis_build-r8j status=closed status/priority/title unchanged vs before-dump
  stored description == computed NEW
  before (masked): c max-trades/day, the XTERMX 
  after:  c max-trades/day, the session window window
Praxis_build-ax4 status=open status/priority/title unchanged vs before-dump
  stored description == computed NEW
  before (masked): ero mention of 11:30, XTERMX,
  before (masked): :30 gate, 16:00 flat, XTERMX 
  after:  ero mention of 11:30, session window,
  after:  :30 gate, 16:00 flat, session window 
history (not edited; open item C1-1): r8j bd history --json term=156

$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ ls -t docs/reports/*.md | head -2
docs/reports/2026-11-10-scrub-forward-manager.md
docs/reports/2026-11-07-rulings-filing-manager.md
$ report gate self-check on docs/reports/2026-11-10-scrub-forward-manager.md
term=0 placeholder-token=0 verification-evidence-heading=1 s13=1
```

The numstat for DECISION_LOG.md is 5/1. In V5 it was 4/1. The extra added line is the master's row 2026-11-10T09:24:00Z (working-tree line 792), which was written before this correction; this correction did not edit DECISION_LOG.md. MANIFEST.md 12/0 is the 9 lines added before this correction (V8) plus the 3 rows added here.

#### C1-V9. Hash of lines 1-258 after the final append
```
$ head -n 258 docs/reports/2026-11-10-scrub-forward-manager.md | openssl dgst -sha256      (before, C1-V0)
SHA2-256(stdin)= 1d93d164ac19ebfd50360d48a2d1add55733fa34c3c707f6c370a034ae588c3f
$ head -n 258 docs/reports/2026-11-10-scrub-forward-manager.md | openssl dgst -sha256      (after)
SHA2-256(stdin)= 1d93d164ac19ebfd50360d48a2d1add55733fa34c3c707f6c370a034ae588c3f
```

Correction 1 Result: PASS

Basis: the criteria for (a)-(d) are met, and each rests on pasted output. The term count is 0 in all 4 landing blobs, all edited working copies, and every current bead field (list, show and comments, open and closed), and the positive controls give 1. The rulings-filing landing blob is HEAD plus the note, and lines 1-450 are identical to HEAD. MANIFEST rows 342-344 were appended, and rows 307-314 are unchanged. The index holds the PNG only, and lines 1-258 of this report hash the same before and after. S2 limit: beads are clean in current fields only. Bead history still holds the term (open item C1-1). The adversarial C FAIL and the A imprecision were fixed and re-verified in C1-V8. They were not softened.
