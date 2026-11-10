# Adversarial report: unit 2026-11-10-scrub-forward (landing blobs for the in-place de-identification)

## Task

Try to break this claim: three in-place one-line edits replace the withheld term with "session window". The edits are DECISION_LOG.md:47, HANDOFF.md:1099 (working tree 1319), and docs/reports/2026-11-09-d11-sweep-manager.md:635, plus a "De-identification note 2026-11-10" appended to that report. The landing blobs are in /tmp/scrub-final/.

Mode: ADVERSARIAL. I only read the repo. The one file I wrote is this report. I ran no index-writing git command.

Criterion (unit-specific plus rubric S6):
- After the edit, a case-insensitive literal count of the term is 0 in all three landing blobs and all three working copies.
- Each landing blob differs from HEAD only on the edited line, plus the appended note in the report.
- No spec, hook, or other tracked text quotes or depends on the exact edited text.

How I handled the term: I loaded it at runtime with `eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"`, inside my own sourced helper /tmp/adv-scrub/env.sh. It was never printed. Every output that could show it went through my own mask, `mask() { T="$TERM" perl -pe 'BEGIN{$t=$ENV{T}; die "empty" unless length $t} s/\Q$t\E/XTERMX/gi'; }`. Its length is 7.

Process disclosure: two of my searches for the string "session window" printed DECISIONS.md:1144 in my tool output. That line holds Amear's already-public verbatim ruling, which contains the category word. Nothing was written from it, and this report does not contain that word.

Standing note required by the brief:

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Checks

| # | Check | Outcome |
|---|---|---|
| 1 | TERM is non-empty; the counter finds it in 3 files at HEAD | PASS |
| 2 | Count is 0 in every landing blob and working copy; prefix and suffix fragments (4, 5, 6 chars) and separator variants are 0 in the landing blobs | PASS |
| 3 | Positive control: injecting the term, as-is or upper-cased, gives a count of 1 for every blob | PASS |
| 4 | Each diff from HEAD is exactly the edited line (plus 2232-2235 in the report); after substitution the HEAD line is byte-identical to the landing line | PASS |
| 5 | The working-copy line equals the landing line; the edited line is the only removed line in each `git diff HEAD` | PASS |
| 6 | The report's landing blob is byte-identical to its working copy | PASS |
| 7 | Wider scan: 0 tracked files, 0 of 77 untracked files; only the PNG is staged | PASS |
| 8 | S6: no gate would trip, and no verbatim quote of the edited fragments exists outside the edited lines. One tracked-text dependency on the edited line exists (Finding 1) | FAIL |
| 9 | MANIFEST: line 341 is the scrub-forward-manager row; rows 307-314 are unchanged from /tmp/scrub-pre | PASS |

## Verification evidence (command output)

All output below is masked. The masked placeholder is XTERMX.

### Check 1
```
TERM-nonempty
len=7
HEAD:DECISION_LOG.md
HEAD:HANDOFF.md
HEAD:docs/reports/2026-11-09-d11-sweep-manager.md
       3
```

### Checks 2 and 3
```
== DECISION_LOG.md
landing: 0  wc: 0  HEAD: 1
prefix5 landing: 0  wc: 0  HEAD: 1
posctl: 1  upper: 1
lines HEAD      788 landing      788 wc      791
== HANDOFF.md
landing: 0  wc: 0  HEAD: 1
prefix5 landing: 0  wc: 0  HEAD: 1
posctl: 1  upper: 1
lines HEAD     1554 landing     1554 wc     1774
== docs/reports/2026-11-09-d11-sweep-manager.md
landing: 0  wc: 0  HEAD: 1
prefix5 landing: 0  wc: 0  HEAD: 1
posctl: 1  upper: 1
lines HEAD     2231 landing     2235 wc     2235
```
Partial forms (occurrence counts; pre = prefix of k characters, suf = suffix of k characters):
```
k=4 DECISION_LOG.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
k=4 HANDOFF.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
k=4 docs/reports/2026-11-09-d11-sweep-manager.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
k=6 DECISION_LOG.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
k=6 HANDOFF.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
k=6 docs/reports/2026-11-09-d11-sweep-manager.md pre: HEAD 1 land 0 | suf: HEAD 1 land 0
DECISION_LOG.md sep-variants landing total: 0
HANDOFF.md sep-variants landing total: 0
docs/reports/2026-11-09-d11-sweep-manager.md sep-variants landing total: 0
```
Each HEAD fragment count of 1 is the term itself: there is exactly one occurrence per file, and the full-term count at HEAD is also 1. In the landing blobs every fragment count is 0, so no partial form survives. The separator variants put a space, a hyphen, or an underscore at each internal position.

### Check 4
```
=== DECISION_LOG.md
47c47
< | 2026-07-25 (session 30) | WHO: Claude.ai master/scoping agent ... (line truncated at 400 chars by cut)
---
> | 2026-07-25 (session 30) | WHO: Claude.ai master/scoping agent ... (line truncated at 400 chars by cut)
=== HANDOFF.md
1099c1099
< - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
---
> - Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/session window breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
=== docs/reports/2026-11-09-d11-sweep-manager.md
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
Character-level check. For each file, I applied a perl substitution (term -> "session window") to the HEAD line and compared it with `cmp` against the landing line:
```
DECISION_LOG.md:47 HEAD-term-count 1
  cmp IDENTICAL (swap-only)
  bytes HEAD     3098 land     3105
HANDOFF.md:1099 HEAD-term-count 1
  cmp IDENTICAL (swap-only)
  bytes HEAD      141 land      148
docs/reports/2026-11-09-d11-sweep-manager.md:635 HEAD-term-count 1
  cmp IDENTICAL (swap-only)
  bytes HEAD      192 land      199
T8-internal, the n8n-gated breakers are bypassed); Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers OPEN, never considered at approval; Q3 Dev-C reverse-reenter vs breake
T8-internal, the n8n-gated breakers are bypassed); Q2 Dev-B 16:00 flat vs 11:30/session window breakers OPEN, never considered at approval; Q3 Dev-C reverse-reenter vs breake
DL-rest-identical
HO-rest-identical
RPT-rest-identical
00000000: 0a                                       .
00000000: 0a                                       .
```
"rest-identical" means a diff with the edited line deleted from both sides, and the note lines 2232-2235 also deleted from the report's landing blob, came out empty. Each line grows by +7 bytes, which is 14 minus 7. Both versions of the report end with a newline.

### Check 5
```
DL-wc47-eq-landing47
HO-wc1319-eq-landing1099
== DECISION_LOG.md numstat: 4	1	DECISION_LOG.md
removed lines:
-| 2026-07-25 (session 30) | WHO: Claude.ai master/scoping agent (cross-block architecture audit, relayed by trader Amear) + orchestrator (session 30) + indepen
hunks:
@@ -47 +47 @@ Append-only. Non-trivial orchestrator judgments.
@@ -788,0 +789,3 @@ Append-only. Non-trivial orchestrator judgments.
== HANDOFF.md numstat: 221	1	HANDOFF.md
removed lines:
-- Also open: `ax4` (P1, Q2 Dev-B 16:00 flat vs 11:30/XTERMX breakers), `zd4` (P1, Q6 praxispush never provisioned). `bd dep cycles` = none.
hunks:
@@ -0,0 +1,220 @@
@@ -1099 +1319 @@ Resume cards go here, newest on top.
== docs/reports/2026-11-09-d11-sweep-manager.md numstat: 5	1	docs/reports/2026-11-09-d11-sweep-manager.md
removed lines:
-- ax4 ("which of {11:30 gate, 16:00 flat, XTERMX disable} governs the anchor strategy and what manages an open position 15:00-16:00") — same content as G11/H02
hunks:
@@ -635 +635 @@ Open beads (54) whose id is absent from the report: `1tz 1ys 2nh 2vu 37h 43n 4gx
@@ -2231,0 +2232,4 @@ Result: PASS (the producer's result after the correction, not a grade): the inve
```

### Check 6
```
RPT-cmp-IDENTICAL
```

### Check 7
```
tracked wt files with term:        0
untracked under docs/:        0 of       75 files
untracked all repo:        0 of       77
docs/reports/2026-11-10-scrub-forward-manager.md: exists=y count=0
docs/reports/2026-11-10-scrub-forward-worker1.md: exists=y count=0
MANIFEST.md: exists=y count=0
cached:
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```
Beyond what the brief asked (out of scope, for information only; see the Notes below):
```
ignored files (excluding .git) with term:       14 of      364     # all under the gitignored Redemtion/ source tree
issues.jsonl HEAD count: 0  wc: 0
show count: 2                    # bd show Praxis_build-ax4
list count:        3             # bd list --all --json, occurrences
remote refs: refs/dolt/data, refs/heads/__dolt_remote_info__ present on origin; .beads/config.yaml sync.remote = the same GitHub repo
branch tips with the term (files): arm-b/wf-tunables 2, parked/Praxis_build-37h 2, parked/Praxis_build-a9d 2, parked/Praxis_build-o78 2, r6/announcement-research 2 (and their origin/ copies)
```

### Check 8 (S6)
Fragment search (file lists; matches in HEAD and in the working tree are identical):
```
== [11:30/]                      DECISION_LOG.md, HANDOFF.md   (only DL:47 and HO wc:1319 — the edited lines themselves)
== [Dev-B 16:00 flat vs 11:30]   DECISION_LOG.md, HANDOFF.md   (same two lines)
== [ disable} governs]           docs/reports/2026-11-09-d11-sweep-manager.md (line 635 only)
== [11:30 gate, 16:00 flat]      docs/reports/2026-11-09-d11-sweep-manager.md (line 635 only)
== [governs the anchor strategy] / [which of {] / [manages an open position 15:00-16:00]: line 635 only
== [16:00 flat, ] 11 files; context of every hit inspected — none quotes the edited text:
DECISIONS.md:352/355, 7zq reports, d11 report :67/:832/:841 — "realises the 16:00 flat, or ..." (Q-text, not the edited line)
HANDOFF.md:1454, STATUS.md:413 — "reverse/re-enter, 16:00 flat, ExitMode ..."
3gm reports — "16:00 flat, no entry at/after close" / "(16:00 flat, reverse on opposite cross ..."
d11 report :635 — the edited line itself
```
Hashes and line citations:
```
DECISION_LOG.md blob fdc918748b3f sha 41a275db8f7d: blob-cited 0 wt 0; sha-cited 0 wt 0
HANDOFF.md blob 35df61a865db sha 92c2e575f567: blob-cited 0 wt 0; sha-cited 0 wt 0
docs/reports/2026-11-09-d11-sweep-manager.md blob 28762ac824a2 sha ce2090cd3f33: blob-cited 0 wt 0; sha-cited 0 wt 0
--- line citations
DECISION_LOG.md:491:DECISION_LOG.md:47
DECISION_LOG.md:678:DECISION_LOG.md:47
MANIFEST.md:341:DECISION_LOG.md:47
MANIFEST.md:341:HANDOFF.md:1099
MANIFEST.md:341:d11-sweep-manager.md:635
docs/reports/2026-11-07-rulings-filing-manager.md:23:DECISION_LOG.md:47
docs/reports/2026-11-07-rulings-filing-manager.md:114:DECISION_LOG.md:47
```
The line counts of the ledgers are equal between landing and HEAD: DECISION_LOG 788/788 and HANDOFF 1554/1554. Every line-number citation therefore still points at the same line.

Context of the :47 citations (masked):
```
== DECISION_LOG.md:491
... a dictionary-rare word from the de-identified source appears in two files already in HEAD (`HEAD:DECISION_LOG.md:47` and HANDOFF) — ... a de-identification sweep unit is owed.
== DECISION_LOG.md:678
... reads 0 at a line KNOWN to hold the breaker #5 source title (HEAD DECISION_LOG.md:47), so it cannot detect the title; its token probe v2 ...
== docs/reports/2026-11-07-rulings-filing-manager.md:23
... Its positive arm, however, read 0 at a known title location (HEAD:DECISION_LOG.md:47). ...
== docs/reports/2026-11-07-rulings-filing-manager.md:114
- **Candidate set:** alpha tokens of length ≥ 4 on HEAD:DECISION_LOG.md:47, which is one known location per D-2026-08-06-A. From these it removes the tokens of HEAD:DECISIONS.md and HEAD:SPEC_RUBRIC.md, intersects with 7d9be8e:HANDOFF.md (the other introducing commit), and removes the tokens of `a42038e^`:DECISION_LOG.md.
```
Reuse of the tokprobe2 method, counted from the tracked files that cite it:
```
docs/reports/2026-11-07-arm-b-code-manager.md            "Method of ...rulings-filing-manager.md:113-118, with the same script"
docs/reports/2026-11-07-arm-b-spec-addendum-manager.md    "Method of ...rulings-filing-manager.md:113-118 ... liveness arm on the two known locations"
docs/reports/2026-11-07-vm-handoff-amendment-manager.md   "the method of ...rulings-filing-manager.md:113–118"
docs/reports/2026-11-07-wf-mac-side-maths-manager.md      bash <SP>/tokprobe2.sh ... (2 runs)
docs/reports/2026-11-07-wf-values-fresh-manager.md        "token probe v2 ... the method of ...rulings-filing-manager.md :113–118"
scratchpad/tokprobe2.sh: not in the repo (ls: No such file or directory); no spec/script/hook/rubric references it.
```
Gates. I read .claude/hooks/gate-commit.sh in full (780 lines). It checks the following:
- the command form;
- the caller identity;
- for the stack master: that the hooks dir is unchanged from HEAD;
- the single-session rule;
- the token, AUDIT_LOG row, provenance, and staged-tree binding.

It contains no ledger content check, no append-only check, and no check for removed lines. I grepped the remaining guards for DECISION_LOG, HANDOFF, d11-sweep, append-only, and removed-line logic:
- scripts/master-write-guard.sh:14 and master-bash-guard.sh:14 list these ledgers only as allowed write targets (`exit 0`).
- scripts/audit-log-flush-verify.sh:48-49 is the only removed-line check, and it is scoped to AUDIT_LOG.md (`git diff --cached -- AUDIT_LOG.md | grep -cE '^-([^-]|$)'`).
- dispatch-log-close.sh and dispatch-log-writeahead.sh enforce append-only on DISPATCH_LOG only.
- commit-tree-verify.sh, stop-gate.sh, and gate-manager-output.sh have no matches.
- precompact-handoff.sh only tails DECISION_LOG.

The git hooks (.beads/hooks/pre-commit and prepare-commit-msg) are 25-line beads wrappers that run `bd hooks run <name>`. The tracked .beads/issues.jsonl was last committed in 4b2c0b9 (2026-05-11) and holds 5 issues. No commit since then has re-exported the bead DB into a tracked file, so I see no route by which a commit would pull bead text in.

Conclusion: committing these landing blobs trips no gate on content. The only requirement is the usual audit token for the staged diff.

### Check 9
```
     341
| /docs/reports/2026-11-10-scrub-forward-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-scrub-forward (bead Praxis_build-8ux; D-2026-08-06-A, DECISION_LOG row 2026-11-10T09:08:00Z): forward in-place de-identification of one withheld term, replaced with "session window", at
HEAD lines:      332  pre lines:      340
307-314 wc==pre
--- diff pre vs wc
340a341
> | /docs/reports/2026-11-10-scrub-forward-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-scrub-forward (bead Praxis_build-8ux; D-202...
```
Compared with HEAD, MANIFEST also gains rows 307-314 (the pre-existing U7 rows, already present in /tmp/scrub-pre) and row 341. Rows 307-314 are byte-identical to /tmp/scrub-pre/MANIFEST.md.

## Findings

1. **S6 dependency: a tracked, reused de-identification method depends on the edited line.** docs/reports/2026-11-07-rulings-filing-manager.md:113-118 defines "superset token probe v2" (tokprobe2). Its candidate set is seeded from the tokens of `HEAD:DECISION_LOG.md:47`, and its liveness arm runs "on the two known locations", which are HEAD DECISION_LOG and HANDOFF. Five later tracked reports adopt this method by citation (listed in check 8). DECISION_LOG.md:678 and the rulings report :23 also name `HEAD DECISION_LOG.md:47` as the known positive location of the breaker #5 source title.

   After this landing, HEAD:DECISION_LOG.md:47 no longer holds the term. Anyone who re-runs the method as written against the new HEAD gets a candidate set without the term. Its liveness arm on the "known locations" also no longer tests the term. The probe can then return a clean result that does not mean what the documents say it means.

   So tracked text does depend on the edited line's content, and the criterion's clause "no ... other tracked text ... depends on the exact edited text" is not met. Severity is low: this is documentation, not a gate, and the script is not in the repo. A remedy (manager's call, not mine): add a pointer note that pins the seed and liveness locations to the pre-scrub commit `0eea766:DECISION_LOG.md:47` (and `0eea766:HANDOFF.md:1099`).

2. **Minor: a citation in the landing report does not resolve within the landing set.** The note appended to the report (landing line 2235) cites "DECISION_LOG row 2026-11-10T09:08:00Z". That row is in neither HEAD nor the DECISION_LOG landing blob; it exists only in the working copy (counts: HEAD 0, landing 0, working copy 1). MANIFEST:341 cites the same row. If the three landing blobs land without the DECISION_LOG flush, the authority cited at that commit points at a row the commit does not contain. It resolves once the flush lands; the order is the manager's choice.

Notes (outside the stated criterion; reported, not fixed):
- (a) The bead DB still holds the term: 3 occurrences in `bd list --all --json`, 2 of them in `bd show Praxis_build-ax4`. The beads sync remote is the same public GitHub repo, and refs/dolt/data exists on origin. If the beads data has been pushed, it is published there.
- (b) Five other branch tips hold the term in 2 files each, both locally and on origin. History is not rewritten by ruling, so this is expected, but it is not limited to main's history.
- (c) 14 files in the gitignored Redemtion/ tree hold the term. They are not tracked and not pushed.
- (d) In the working copy of HANDOFF.md, 220 pre-existing uncommitted lines sit at file position 0, before the header line (hunk `@@ -0,0 +1,220 @@`). This is not part of this unit; flagged only.

## Result: FAIL

All the mechanical claims hold: zero counts, swap-only diffs, working-copy consistency, the cmp checks, the MANIFEST checks, and no gate trips. The single failure is the S6 clause, because of Finding 1: a tracked, reused de-identification method is seeded from the edited line.

Self-check on this report (term count, then the count of the "to be determined" abbreviation):
```
0
0
```
