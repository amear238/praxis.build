# 2026-11-10 D9 housekeeping -- manager report

Unit: 2026-11-10-d9-housekeeping. Author: praxis-manager. Started 2026-11-10T06:12:35Z (`date -u`).

## Task

Amear D9 (D-2026-11-08-D), verbatim: "D9  The 12 old staged paths are landed properly (audited) rather than unstaged. Root file "F" is traced, then removed and logged."
Scoping: DECISION_LOG.md row 2026-11-10T06:13:00Z items (1)-(5): land each path's STAGED blob; "properly" = S13 line where missing, the 2026-08-06 de-identification ruling, no personal contact data; minimal itemised redaction allowed; a file that cannot be cleaned by text edit stays out; MANIFEST rows; F content and sha256 pasted before removal.

Masking convention in this report. This report is itself headed for a public repo, so the text that was redacted is not reproduced here. In pasted output: `[M-word]` = a word naming the category of the withheld term; `[C-word]` = a clinical word; `[rep-local]` = the local part of a support representative's name-bearing email address; `[sha7]` = a short sha of a commit that introduced the withheld term; `[n]` = a line number, length or count tied to that term; `[date]` = its introduction date; `[personal-filename]` = a local filename naming health detail. The mask is applied inside the pipeline (`sed -E -f /tmp/d9-build/mask.sed`), so it is visible in the command. The unmasked diffs are at `/tmp/d9-offrepo/raw-diffs.txt` (off-repo; pre-round-2) and are reproducible at any time with `diff <(git show :<path>) /tmp/d9-final/<path>` while the real index holds the old blobs.

## Rubric criteria addressed

S1, S2, S4, S6, S13 (specs/SPEC_RUBRIC.md lines 121, 122, 124, 126, 133).

## Workers dispatched (id, mode, outcome)

| # | agent id | mode | scope | outcome |
|---|---|---|---|---|
| W0 | a910a33417b85f7d6 | ADVERSARIAL | leak scan, all 12 | died at 40-turn limit, no report written; superseded by W1-W3 |
| W1 | aca1c6b4c43f77cd2 | ADVERSARIAL | leak scan A: F4 evidence, F4 filing, transcript, PNG | FAIL: rep address x4 text + PNG must be excluded |
| W2 | a8ea9029417932ac8 | ADVERSARIAL | leak scan B1: r8j phase3 import, ISSUE_REGISTER diff, spec diff | FAIL: 14 r8j + 5 ISSUE_REGISTER findings |
| W3 | ad3b8f22270d030a2 | ADVERSARIAL | leak scan B2: 3 offset-correction + 2 nightly reports | 0 MUST-REDACT |
| W4 | a9b4822e455088c4e | BUILD | build /tmp/d9-final (round 1 edits) | PASS, no BEFORE mismatches; flagged a category word in the manager-dictated trailer (fixed by manager, one line) |
| W5 | a3473ed7b3cb02a06 | ADVERSARIAL | final copies, criteria a-f | FAIL: clinical filename, side channels, locators, dates, trailer list |
| W6 | abf97fd6f9f37adc8 | BUILD (fix) | round 2 edits | PASS, no mismatches |
| W7 | aa34e5177277e8aaf | ADVERSARIAL | recheck r8j + ISSUE_REGISTER finals | FAIL x3: one fixed (L357), two accepted with reasons below |

Worker reports are kept OFF the repo at `/tmp/d9-offrepo/` (leakscan-a, leakscan-b1, leakscan-b2, build, final-adversarial, fix2, recheck). Reason (decided by manager under D-2026-11-08-D D1): the scan and build reports quote the withheld strings verbatim (counts in Process log step 5); committing them would undo the redaction. They need no MANIFEST rows because they are not in the repo.

## Process log

1. 06:12:35Z baseline: HEAD = origin/main = 23556aa; index fingerprint 5bfab445...bda95 (Verification evidence V1).
2. S13 check on the 11 text blobs: sentence count 0 in all (V2). S13 applies to the 10 under docs/reports/; not to ISSUE_REGISTER.md or the spec.
3. Leak scan W0 died at its turn cap; re-split into W1/W2/W3 (foreground, parallel).
4. Manager checks of the findings: looked at the PNG with the Read tool (it shows the representative's full-name address in the From line; nothing else private: no tabs, other windows or numbers). Confirmed what is already public at HEAD (V4): the ruling text "no drug names" (4 files), the category word (14 files incl. `DECISIONS.md:1142`, `specs/SPEC_RUBRIC.md`), the FRANK@ relay address and the Gmail thread id (DECISION_LOG.md); the full-name rep address is NOT at HEAD. The withheld term itself is at HEAD in 3 tracked files (V5, counts only).
5. Built /tmp/d9-final (W4). Moved the four worker reports off-repo after counting the withheld strings in them (V6).
6. W5 adversarial on the finals found more; W6 fixed them; W7 rechecked; manager fixed L357 (one line, quote integrity).
7. MANIFEST rows 329-339 appended (V8). F traced and removed (V9).

## Per-path decisions and edits

Authority for every landing: D9 (DECISIONS.md:1955, D-2026-11-08-D, at HEAD) plus master scoping 06:13Z items (2)-(4). De-identification authority: Amear 2026-08-06 "de-identify it — session window, no drug names" (DECISION_LOG 2026-08-06T20:18:56Z; DECISIONS.md:1147 "No drug name shall enter any tracked artifact"). Choices inside that latitude are labelled "decided by manager under D-2026-11-08-D D1".

| # | path | staged status | lands? | edits | working tree |
|---|---|---|---|---|---|
| 1 | ISSUE_REGISTER.md | MM | yes | L63: 4 word-level redactions (below); no trailer (not a report) | left alone (MM) |
| 2 | docs/reports/2026-08-06-session42-r8j-phase3-import.md | A | yes | 26 lines edited in place + 2 trailer lines | same edits mirrored, `cmp` clean |
| 3 | docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | A | yes | L597, L733, L757 + 2 trailer lines | mirrored, `cmp` clean |
| 4 | docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md | A | yes | S13 trailer only | mirrored |
| 5 | docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md | A | yes | S13 trailer only | mirrored |
| 6 | docs/reports/2026-08-07-session44-r8j-offset-correction.md | A | yes | S13 trailer only | mirrored |
| 7 | docs/reports/2026-10-28-f4-davi-reply-filing.md | AM | yes | note + S13 trailer (no in-place edit) | left alone (AM) |
| 8 | docs/reports/2026-10-28-nightly-checks-plan-review-note.md | A | yes | S13 trailer only | mirrored |
| 9 | docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md | AM | yes | S13 trailer only | left alone (AM) |
| 10 | docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md | A | yes | L18 + 2 trailer lines | mirrored |
| 11 | docs/reports/evidence/2026-10-28-mffu-davi-reply.png | A | **NO** | cannot be cleaned by a text edit: the From line shows a support representative's full-name email address | untouched; still in the real index (this unit may not change the index) |
| 12 | docs/specs/2026-08-08-ledger-compaction-spec.md | M | yes | none; byte copy of the staged blob | tree already equals staged |

### Itemised edits (before masked, after verbatim)

r8j phase3 import (path 2), line numbers of the staged blob (line count unchanged by in-place edits):
- L7: "a [M-word] brand name" -> "a personal term"
- L109: "[[M-word] BRAND NAME]" -> "[WITHHELD TERM]"
- L146: "The word-count delta is [n], exactly accounted for" -> "The word-count delta is exactly accounted for"
- L147: "(`<term> window` = 2 words → `Afternoon session window` = 3)." -> "(the authorised retitle of breaker #5 accounts for it)."
- L297: "**line [n]**" and "now cites line [n] with" -> "**line [withheld 2026-11-10, D9]**", "now cites line [withheld 2026-11-10, D9] with"
- L315: "`HANDOFF.md` line [n] (in" -> "`HANDOFF.md` line [withheld 2026-11-10, D9] (in"
- L357: "\"[M-word]-window justification" -> "\"[withheld]-window justification" (a verbatim quote of the rubric's F2 text; the bracket marks the redaction; W7 found an intermediate "session-window" form misquoted it, fixed by manager)
- L385: "committed [date] and pushed:" -> "committed and pushed:"
- L388-390: per-ref line numbers and the two [sha7] revisions -> "[withheld 2026-11-10, D9]"
- L402: "So the brand name is publicly visible on GitHub right now, and has been since [date]." -> "So the term is publicly visible on GitHub right now."
- L406: "`[sha7]`/`[sha7]`" -> "the two introducing commits"
- L503: "`DECISION_LOG.md:[n]`" -> "`DECISION_LOG.md` (line [withheld 2026-11-10, D9])"
- L594: "| /usr/bin/awk '[step]')" -> "| [final extraction step withheld 2026-11-10, D9])" (pasted command)
- L596-597: term-length probe command and its output -> "$ [term-length probe withheld 2026-11-10, D9]" / "[output withheld 2026-11-10, D9]"
- L645: grep pattern "[M-word] BRAND NAME" -> "[placeholder string withheld 2026-11-10, D9]" (pasted command)
- L684: "[[M-word] BRAND NAME] window" -> "[WITHHELD TERM] window" (captured output)
- L1013: "The redacted [n]-letter term" -> "The redacted term" (captured file listing)
- L1185: a local gitignored filename naming health detail -> "./Redemtion/Intitialization-April 2026/[personal filename withheld 2026-11-10, D9].rtf" (captured `find` output)
- L1654: "once, at line [n]." -> "once."
- L1671: "[n]:" -> "[withheld 2026-11-10, D9]:" (captured output)
- L1675: "the [M-word] brand name enters" -> "the withheld term enters"
- L1816: "pre-existing occurrence at line [n]," -> "pre-existing occurrence,"
- L1817: "committed [date], inherited unchanged" -> "committed earlier, inherited unchanged"
- L1829: "... 3 full-path `Redemtion/` citations with 2 marked. The unmarked one is" -> "`DECISION_LOG.md` also has a pre-existing citation-form issue (details withheld 2026-11-10, D9); it is"
- L1830: "line [n] — the same pre-existing committed row." -> "the same pre-existing committed row."
- Appended after one blank line: the "Edited 2026-11-10 under D9 ..." line listing exactly those lines (W7 confirmed the list equals the diff) and the S13 line.
- Kept, decided by manager under D1: L38 Amear's ruling quote "de-identify it — session window, no drug names" (his verbatim words, already public at HEAD in 4 files); L283 quotes the DECISIONS.md entry wording "No drug name" (already public at `DECISIONS.md:1147`); "XREDACTEDX window" at L600/L681 (captured masked output; residual one-token signal, accepted because the term is already public at HEAD regardless -- open item 1).

f4 compliance evidence (path 3): L597 and L733 "[rep-local]@myfundedfutures.intercom-mail.com" -> "[rep-address]@myfundedfutures.intercom-mail.com"; L757 "(`[rep-local]`)" -> "(`[rep-address]`)"; trailer note + S13. The prefix hash of lines 1-537 cited by the filing report is unaffected (all edits are after line 537).

Transcript (path 10): L18 "[rep-local]@..." -> "[rep-address]@..."; trailer note + S13.

F4 filing (path 7): no in-place edit; appended note that the PNG is not committed and that fence hash 8e14a690... no longer matches the committed transcript; S13.

ISSUE_REGISTER (path 1), staged line 63: "titled with a [M-word] brand name in" -> "titled with a personal term [de-identified 2026-11-10, D9] in"; "the de-identified form \"[M-word]-window\" (" -> "a de-identified form ("; "ruling that [C-word] content" -> "ruling that personal content".
Kept, decided by manager under D1: L68 sender `FRANK@myfundedfutures.intercom-mail.com` (vendor relay with a first name only, which category 6 of the brief allows; already public at HEAD in DECISION_LOG.md) and the Gmail thread id (not an account number, credential or contact datum; already public at HEAD). L63 still cites `specs/SPEC_RUBRIC.md:38-40`, where the category word is public at HEAD; accepted because the category word is already public in 14 HEAD files and the cite adds no new disclosure (W7 finding 2, accepted with this reason).

Exclusion, decided by manager under D1: the full-name rep address was judged a third party's identifying contact datum, so the PNG stays out and the text copies are redacted. A FRANK@-style first-name relay address was judged acceptable. If Amear rules vendor relay addresses publishable, the PNG can land later unchanged.

### AM/MM unstaged deltas (not landed; reported per master item 2)

`git diff --stat` in V7. ISSUE_REGISTER.md: +6 lines, rows dated 2026-08-15 and 2026-08-29 (session 51 and 53 issues: the continuous-NQ acceptance gate, a read-only overseer write, the manager-output gate token match). f4 filing: +74 lines, the praxis-auditor's audit of 2026-10-28T21:29:28Z (evidence re-run, per-criterion table, BLOCKING and MINOR findings, NOT CHECKED). nightly rebuild: +67 lines, the auditor's re-audit of 2026-10-28T21:32:09Z (re-captures, criteria, new BLOCKING and MINOR). The landed copies of the two reports therefore do not carry their audits; that is master item (2) as written. The landing does not claim either report passed its audit.

## Root file F trace

F was 15 bytes, `# DISPATCH LOG\n`, sha256 a97839204ed8ef9f69e50ba0b7a40483beb3562616d753cabe0eb05c65a52d2b, mtime 2026-07-28T16:09:13Z (12:09:13 EDT), untracked, not ignored (V9). History: `git log --all -- F` shows only 9c47b1a, "WIP: Claude Code rate-limit checkpoint (f3c55a3e)", 2026-08-15, on ref `refs/claude/checkpoint-f3c55a3e`, not on any branch and not on origin (`git ls-remote origin | grep -c checkpoint` = 0); its blob has the same sha256. Content equals the header line of the session-39 dispatch-log-closer fixtures (`# DISPATCH LOG` appears in all five 2026-07-28-session39 closer reports), and the mtime falls between the session-39 closer-negative-tests report (16:08:04Z) and the live-vs-piped-attack report (16:12:00Z). Origin: INFERRED a stray fixture write from session 39's DISPATCH_LOG closer tests; the creating command was never observed (same as HANDOFF.md:817 says). Removed with `rm F` 2026-11-10; `ls -la F` after: "No such file or directory". The copy inside the local checkpoint ref is untouched.

## MANIFEST

HEAD MANIFEST.md had a row only for the f4 compliance evidence (row 132). Rows appended after line 328: 329-338 for the other 10 landing paths, 339 for this report. No edit at or above line 328 (hunk headers in V8; the `@@ -306,0 +307,8 @@` hunk is pre-existing uncommitted work from earlier units, not this unit's). No row for the PNG (not landing) or the off-repo worker reports.

## S4 / S6 cross-block check

S4: D9 is a DECISIONS.md entry at HEAD (`DECISIONS.md:1955`, block D-2026-11-08-D), written 2026-11-08 before this work; the master's 06:13Z row scopes it; redaction authority is the 2026-08-06 ruling (DECISIONS.md:1147, DECISION_LOG 2026-08-06T20:18:56Z). The manager's D1 choices (PNG exclusion, kept quotes, kept FRANK@/thread id, worker reports off-repo) have no DECISIONS.md entry of their own; they are in this report only. The master may want to log them. Graded: PASS for the landings, with that note.

S6: the ledger-compaction spec change (+12/-2) lands byte-for-byte (V3 cmp). It rewords one retain bullet, adds row K7 `[PROPOSED]` (compact.sh stages only, never commits) and note C-9, which records two collisions and resolves neither: K7 vs. staging being a `.git/` write, and K7 vs. the commit gate (`.claude/hooks/gate-commit.sh:167-176` binds the audit token to the staged tree). It touches the supervision block's commit-gate spec by RECORDING a collision, not by changing the gate; K7 stays PROPOSED, so landing ratifies nothing. It touches no trading-block spec (no B1-B4/F1-F4 content, no breaker values). The r8j report's edits change no spec (they are report text). Graded: S6 PASS for this unit; the C-9 collision is carried open, as the spec itself says.

S13: 10 of 10 docs/reports paths carry the sentence exactly once in the landing copy (V10). S2: nothing here is claimed tested beyond the greps and cmp shown; the de-identification is "scanned by four adversarial passes", not "proven clean".

## Adversarial findings

- W1/W2 (round 1): rep full-name address x4 + PNG; category words, locators (line numbers, shas), term length, one-word arithmetic in r8j; category word and [C-word] in ISSUE_REGISTER. All fixed or excluded.
- W5 (round 2): a personal filename naming health detail (r8j L1185), "[n]-letter" (L1013), `awk` one-word step (L594), word-count delta (L146), HANDOFF line locators (L297, L315), `DECISION_LOG.md:[n]` (L503), the "unmarked one" pointer (L1829), introduction dates (L385, L402, L1817), trailer list missing L684. All fixed by W6. (W4, the builder, had earlier flagged the manager's own trailer wording as containing a category word; fixed by the manager before W5 ran.)
- W7 (round 3): L357 misquote created by the round-1 edit -> fixed with a bracketed redaction; ISSUE_REGISTER cite of SPEC_RUBRIC:38-40 -> accepted (reason above); FRANK@ -> accepted (reason above). W7 also reports the withheld term is in a third tracked file at HEAD (confirmed by manager, V5) -> open item 1.
- Negative/positive control: the same counters that read 0 on the landing copies read non-zero on the staged blobs (V5, V10), so the zeros are not a dead grep.

## Files staged

None by this unit. The real index is not changed (fingerprint start and end in V1 and the final block). Working-tree changes by this unit: the 7 TREE=yes report files (edits mirrored), MANIFEST.md rows 329-339, this report, `F` removed.

## Open items

1. The withheld term is committed at HEAD in 3 tracked files, one of them added by a commit dated 2026-11-09, after the forward-only ruling (V5, counts only; the file name is given to the master in the return message, not here). The category word is public at HEAD in 14 files. E1 (retroactive scrub / history rewrite) remains Amear's.
2. The PNG remains in the real index as `A`. The landing commit must be built so it excludes it (e.g. a temp index from the /tmp/d9-final bytes), or the PNG must be unstaged by whoever is allowed to change the index.
3. The 4 old staged paths that are AM/MM keep unstaged working-tree deltas (two of them hold auditor sections with BLOCKING findings); not landed by D9.
4. Manager D1 choices (above) have no DECISIONS.md entry.
5. W0 died at its turn cap without a report; W1-W3 replaced it.

## Verification evidence (command output)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

Result: PASS

Evidence follows, V1-V10 then the final block, appended by shell. Inside pasted output the standing sentence is shown as `[S13 sentence]` so the report carries it once; the masks above also apply.

### V1. Baseline (captured at 06:12:35Z, first command of the unit)
```
$ date -u; git rev-parse HEAD origin/main; git diff --cached --name-only | openssl dgst -sha256
Tue Nov 10 06:12:35 UTC 2026
23556aa7999c1b0763fd746a73fba63300ea911b
23556aa7999c1b0763fd746a73fba63300ea911b
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
```
### V2. S13 sentence count in the staged blobs (re-run now)
```
$ for p in <11 text paths>; do git show :$p | grep -c "Fills are optimistic"; done
ISSUE_REGISTER.md: 0
docs/reports/2026-08-06-session42-r8j-phase3-import.md: 0
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md: 0
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md: 0
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md: 0
docs/reports/2026-08-07-session44-r8j-offset-correction.md: 0
docs/reports/2026-10-28-f4-davi-reply-filing.md: 0
docs/reports/2026-10-28-nightly-checks-plan-review-note.md: 0
docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md: 0
docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md: 0
docs/specs/2026-08-08-ledger-compaction-spec.md: 0
```
### V3. Per-path diff, staged blob vs landing copy (masked)
```
$ diff <(git show :docs/reports/2026-08-06-session42-r8j-phase3-import.md) /tmp/d9-final/docs/reports/2026-08-06-session42-r8j-phase3-import.md | sed -E -f mask.sed
7c7
< with a [M-word] brand name. It is referred to here only as "the redacted term". It is not
---
> with a personal term. It is referred to here only as "the redacted term". It is not
109c109
< 6c6   [redacted title]  vs  [[M-word] BRAND NAME]
---
> 6c6   [redacted title]  vs  [WITHHELD TERM]
146,147c146,147
< One difference. It is the authorised one. The word-count delta is [n], exactly accounted for
< (`<term> window` = 2 words → `Afternoon session window` = 3).
---
> One difference. It is the authorised one. The word-count delta is exactly accounted for
> (the authorised retitle of breaker #5 accounts for it).
297c297
<   **line [n]**; `HEAD:HANDOFF.md` line 237 is blank. **Fixed by W7** — now cites line [n] with
---
>   **line [withheld 2026-11-10, D9]**; `HEAD:HANDOFF.md` line 237 is blank. **Fixed by W7** — now cites line [withheld 2026-11-10, D9] with
315c315
< `HANDOFF.md` line [n] (in `HEAD`, the index and `origin/main`; line 237 in the current uncommitted worktree).
---
> `HANDOFF.md` line [withheld 2026-11-10, D9] (in `HEAD`, the index and `origin/main`; line 237 in the current uncommitted worktree).
357c357
< "[M-word]-window justification … now unsupported and never revisited" — the de-identified
---
> "[withheld]-window justification … now unsupported and never revisited" — the de-identified
385c385
< committed [date] and pushed:
---
> committed and pushed:
388,390c388,390
< term's line number in HANDOFF.md — HEAD: [n] | index: [n] | origin/main: [n] | worktree: [n]
< term's line number in DECISION_LOG.md — HEAD: [n] | worktree: [n]
< revisions: [sha7] (DECISION_LOG.md), [sha7] (HANDOFF.md)  — verified absent in each parent
---
> term's line number in HANDOFF.md — [withheld 2026-11-10, D9]
> term's line number in DECISION_LOG.md — [withheld 2026-11-10, D9]
> revisions: [withheld 2026-11-10, D9]  — verified absent in each parent
402c402
< So the brand name is publicly visible on GitHub right now, and has been since [date].
---
> So the term is publicly visible on GitHub right now.
406c406
< `[sha7]`/`[sha7]` and force-updating `origin/main`?** Not answered. Both files are on this
---
> the two introducing commits and force-updating `origin/main`?** Not answered. Both files are on this
503c503
< > `DECISION_LOG.md:[n]` — see the closing de-identification checks. The two that are re-established
---
> > `DECISION_LOG.md` (line [withheld 2026-11-10, D9]) — see the closing de-identification checks. The two that are re-established
594c594
< $ TERM=$(textutil -convert txt -stdout "$SRC" | /usr/bin/sed -n '48p' | /usr/bin/sed -E 's/^[[:space:]]*5\.[[:space:]]*//' | /usr/bin/awk '[step]')
---
> $ TERM=$(textutil -convert txt -stdout "$SRC" | /usr/bin/sed -n '48p' | /usr/bin/sed -E 's/^[[:space:]]*5\.[[:space:]]*//' | [final extraction step withheld 2026-11-10, D9])
596,597c596,597
< $ echo "TERM length = ${#TERM} chars"
< TERM length = [n] chars
---
> $ [term-length probe withheld 2026-11-10, D9]
> [output withheld 2026-11-10, D9]
645c645
< $ /usr/bin/grep -l "[M-word] BRAND NAME" /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/3da2915b-cd0b-48a5-af31-55340cdff654.jsonl /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/3da2915b-cd0b-48a5-af31-55340cdff654/subagents/*.jsonl 2>/dev/null
---
> $ /usr/bin/grep -l "[placeholder string withheld 2026-11-10, D9]" /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/3da2915b-cd0b-48a5-af31-55340cdff654.jsonl /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/3da2915b-cd0b-48a5-af31-55340cdff654/subagents/*.jsonl 2>/dev/null
684c684
< > 	5.	[[M-word] BRAND NAME] window — clock enters 3:00–6:00 PM ET → disable everything
---
> > 	5.	[WITHHELD TERM] window — clock enters 3:00–6:00 PM ET → disable everything
1013c1013
< # The redacted [n]-letter term must not appear in the file (case-insensitive).
---
> # The redacted term must not appear in the file (case-insensitive).
1185c1185
< ./Redemtion/Intitialization-April 2026/[personal-filename].rtf
---
> ./Redemtion/Intitialization-April 2026/[personal filename withheld 2026-11-10, D9].rtf
1654c1654
< The staged `DECISION_LOG.md` blob **does contain the redacted term**, once, at line [n]. That line
---
> The staged `DECISION_LOG.md` blob **does contain the redacted term**, once. That line
1671c1671
< [n]:
---
> [withheld 2026-11-10, D9]:
1675c1675
< "the [M-word] brand name enters no tracked artifact" is satisfied for this change. It is **not**
---
> "the withheld term enters no tracked artifact" is satisfied for this change. It is **not**
1816,1817c1816,1817
< **`DECISION_LOG.md` NEG=1, and that is not hidden.** It is the pre-existing occurrence at line [n],
< committed [date], inherited unchanged from `HEAD` — escalation **E1**, which remains open and
---
> **`DECISION_LOG.md` NEG=1, and that is not hidden.** It is the pre-existing occurrence,
> committed earlier, inherited unchanged from `HEAD` — escalation **E1**, which remains open and
1829,1830c1829,1830
< `DECISION_LOG.md` also shows 3 full-path `Redemtion/` citations with 2 marked. The unmarked one is
< line [n] — the same pre-existing committed row. It is not introduced by this change and
---
> `DECISION_LOG.md` also has a pre-existing citation-form issue (details withheld 2026-11-10, D9); it is
> the same pre-existing committed row. It is not introduced by this change and
1882a1883,1885
> 
> Edited 2026-11-10 under D9 (de-identification under the 2026-08-06 ruling; decided by manager under D-2026-11-08-D D1): lines 7, 109, 146, 147, 297, 315, 357, 385, 388-390, 402, 406, 503, 594, 596-597, 645, 684, 1013, 1185, 1654, 1671, 1675, 1816, 1817, 1829 and 1830 had a category word for the term, a locator or date of the published term, a term side channel, or a personal filename replaced; l
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md) /tmp/d9-final/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | sed -E -f mask.sed
597c597
< `[rep-local]@myfundedfutures.intercom-mail.com` are recorded **as displayed
---
> `[rep-address]@myfundedfutures.intercom-mail.com` are recorded **as displayed
733c733
<    > Davi from MyFundedFutures <[rep-local]@myfundedfutures.intercom-mail.com>
---
>    > Davi from MyFundedFutures <[rep-address]@myfundedfutures.intercom-mail.com>
757c757
<    (`[rep-local]`) also differs from the relayed Frank sender in §1
---
>    (`[rep-address]`) also differs from the relayed Frank sender in §1
776a777,779
> 
> Edited 2026-11-10 under D9 (decided by manager under D-2026-11-08-D D1): lines 597, 733 and 757 had a support representative's name-bearing address replaced by [rep-address]; line 733 is quoted text edited after capture. The evidence PNG docs/reports/evidence/2026-10-28-mffu-davi-reply.png is not committed, because it shows the same address. The prefix hash of lines 1-537 cited elsewhere is unaf
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md) /tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md | sed -E -f mask.sed
546a547,548
> 
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md) /tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md | sed -E -f mask.sed
195a196,197
> 
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-08-07-session44-r8j-offset-correction.md) /tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction.md | sed -E -f mask.sed
301a302,303
> 
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-10-28-f4-davi-reply-filing.md) /tmp/d9-final/docs/reports/2026-10-28-f4-davi-reply-filing.md | sed -E -f mask.sed
391a392,394
> 
> Note 2026-11-10 under D9 (decided by manager under D-2026-11-08-D D1): the PNG named above, docs/reports/evidence/2026-10-28-mffu-davi-reply.png, is not committed, because it shows a support representative's name-bearing address; its hashes above describe a file kept off the repo. The committed transcript has that address replaced on its line 18, so the fence hash 8e14a690... above no longer mat
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-10-28-nightly-checks-plan-review-note.md) /tmp/d9-final/docs/reports/2026-10-28-nightly-checks-plan-review-note.md | sed -E -f mask.sed
184a185,186
> 
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md) /tmp/d9-final/docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md | sed -E -f mask.sed
1333a1334,1335
> 
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md) /tmp/d9-final/docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md | sed -E -f mask.sed
18c18
< Davi from MyFundedFutures <[rep-local]@myfundedfutures.intercom-mail.com>
---
> Davi from MyFundedFutures <[rep-address]@myfundedfutures.intercom-mail.com>
71a72,74
> 
> Edited 2026-11-10 under D9 (decided by manager under D-2026-11-08-D D1): line 18 is verbatim text with the support representative's name-bearing address replaced by [rep-address]; the source PNG is not committed. Itemised in docs/reports/2026-11-10-d9-housekeeping-manager.md.
> Appended 2026-11-10 under D9 (S13): [S13 sentence]
$ diff <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md | sed -E -f mask.sed
$ cmp <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md; echo rc=$?
rc=0
$ ISSUE_REGISTER.md: word-level changed spans (python difflib on tokens, masked)
lines staged/final: 70 70
L63 replace: <titled with a [M-word] brand name in>  ->  <titled with a personal term [de-identified 2026-11-10, D9] in>
L63 replace: <ledgers currently use the de-identified>  ->  <ledgers currently use a de-identified>
L63 delete: <the de-identified form "[M-word]-window" (`specs/SPEC_RUBRIC.md:38-40`),>  ->  <a de-identified form (`specs/SPEC_RUBRIC.md:38-40`),>
L63 replace: <2026-07-24 ruling that [C-word] content>  ->  <2026-07-24 ruling that personal content>
```
### V4. Already public at HEAD (counts per file)
```
$ git grep -c "no drug names" HEAD -- . ; git grep -c "<category word>" HEAD -- . | wc -l; git grep -c "<rep-local>" HEAD -- .; git grep -c "FRANK@" HEAD -- .
HEAD:DECISIONS.md:1
HEAD:DECISION_LOG.md:1
HEAD:HANDOFF.md:1
HEAD:STATUS.md:1
files with category word at HEAD: [n]
files with rep-local at HEAD: [n]
HEAD:DECISION_LOG.md:1
HEAD:DECISION_LOG.md:1
```
### V5. The withheld term: extracted at runtime from the gitignored source into $TERM, never typed or printed; counts only
```
$ TERM=$(textutil ... | sed -n 48p | ... ); [ -n "$TERM" ] && echo TERM-nonempty
TERM-nonempty
$ git grep -ilF -- "$TERM" HEAD | wc -l
3
$ for each landing copy: grep -ciF -- "$TERM"; positive control: TERM injected into the same stream
./ISSUE_REGISTER.md NEG=0 LIVENESS=1
./docs/reports/2026-08-06-session42-r8j-phase3-import.md NEG=0 LIVENESS=1
./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md NEG=0 LIVENESS=1
./docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md NEG=0 LIVENESS=1
./docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md NEG=0 LIVENESS=1
./docs/reports/2026-08-07-session44-r8j-offset-correction.md NEG=0 LIVENESS=1
./docs/reports/2026-10-28-f4-davi-reply-filing.md NEG=0 LIVENESS=1
./docs/reports/2026-10-28-nightly-checks-plan-review-note.md NEG=0 LIVENESS=1
./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md NEG=0 LIVENESS=1
./docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md NEG=0 LIVENESS=1
./docs/specs/2026-08-08-ledger-compaction-spec.md NEG=0 LIVENESS=1
```
### V6. Worker reports moved off-repo: withheld-string counts (counted before the move)
```
$ for f in leakscan-a leakscan-b1 leakscan-b2 build; do grep -ci <category word>; grep -c <rep-local>; grep -cE <sha7>; done; mv ... /tmp/d9-offrepo/
leakscan-a: M-word=1 rep-local=9 sha7=0
leakscan-b1: M-word=20 rep-local=0 sha7=5
leakscan-b2: M-word=1 rep-local=0 sha7=0
build: M-word=28 rep-local=4 sha7=4
$ ls /tmp/d9-offrepo
2026-11-10-d9-housekeeping-build.md
2026-11-10-d9-housekeeping-final-adversarial.md
2026-11-10-d9-housekeeping-fix2.md
2026-11-10-d9-housekeeping-leakscan-a.md
2026-11-10-d9-housekeeping-leakscan-b1.md
2026-11-10-d9-housekeeping-leakscan-b2.md
2026-11-10-d9-housekeeping-recheck.md
raw-diffs.txt
$ ls docs/reports/2026-11-10-d9-*
docs/reports/2026-11-10-d9-housekeeping-manager.md
```
### V7. Unstaged deltas of the AM/MM paths
```
$ git diff --stat -- ISSUE_REGISTER.md docs/reports/2026-10-28-f4-davi-reply-filing.md docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
 ISSUE_REGISTER.md                                  |  6 ++
 docs/reports/2026-10-28-f4-davi-reply-filing.md    | 74 ++++++++++++++++++++++
 ...026-10-28-nightly-checks-plan-review-rebuild.md | 67 ++++++++++++++++++++
 3 files changed, 147 insertions(+)
```
### V8. MANIFEST
```
$ git show HEAD:MANIFEST.md | grep -nF <basename> (per landing path; only hit shown)
ISSUE_REGISTER.md: HEAD-rows=
docs/reports/2026-08-06-session42-r8j-phase3-import.md: HEAD-rows=
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md: HEAD-rows=132,
docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md: HEAD-rows=
docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md: HEAD-rows=
docs/reports/2026-08-07-session44-r8j-offset-correction.md: HEAD-rows=
docs/reports/2026-10-28-f4-davi-reply-filing.md: HEAD-rows=
docs/reports/2026-10-28-nightly-checks-plan-review-note.md: HEAD-rows=
docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md: HEAD-rows=
docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md: HEAD-rows=
docs/specs/2026-08-08-ledger-compaction-spec.md: HEAD-rows=
$ git diff HEAD -U0 -- MANIFEST.md | grep "^@@"
@@ -306,0 +307,8 @@
@@ -320,0 +329,11 @@
$ sed -n 329,339p MANIFEST.md
| /ISSUE_REGISTER.md | Log | 0 | 2026-05-11 | Append-only issue register (markdown fallback ledger). Row added 2026-11-10 by unit 2026-11-10-d9-housekeeping (Amear D-2026-11-08-D D9): the file had no MANIFEST row; D9 lands its old staged 35-line addition (rows of 2026-08-06/07), with two de-identification edits on staged line 63. The working-tree delta beyond the staged blob is not part of D9 |
| /docs/reports/2026-08-06-session42-r8j-phase3-import.md | Report | 3 | 2026-08-06 | Session-42 manager report for Praxis_build-r8j (Phase 3 spec import, de-identified). Landed 2026-11-10 under D9 from the old staged set, with de-identification edits (category words, locators and side channels of the withheld term, one personal filename) itemised in docs/reports/2026-11-10-d9-housekeeping-manager.md, and the S13 line appended |
| /docs/reports/2026-08-07-session44-r8j-offset-correction.md | Report | 3 | 2026-08-07 | Session-44 manager report for the r8j offset correction. Landed 2026-11-10 under D9 from the old staged set; S13 line appended, no other edit |
| /docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md | Report | 3 | 2026-08-07 | Session-44 worker 1 report for the r8j offset correction. Landed 2026-11-10 under D9 from the old staged set; S13 line appended, no other edit |
| /docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md | Report | 3 | 2026-08-07 | Session-44 adversarial report for the r8j offset correction. Landed 2026-11-10 under D9 from the old staged set; S13 line appended, no other edit |
| /docs/specs/2026-08-08-ledger-compaction-spec.md | Spec | 0 | 2026-08-09 | Ledger-compaction spec (file first committed 2026-08-09; it had no MANIFEST row). Row added 2026-11-10 under D9: the old staged +12/-2 change lands byte-for-byte |
| /docs/reports/2026-10-28-f4-davi-reply-filing.md | Report | 0 | 2026-10-28 | F4 filing report for the MFFU support reply of 2026-10-28 (copy, hash and verbatim transcript of the reply, adversarial check). Landed 2026-11-10 under D9 from the old staged set with a dated note: the evidence PNG it names is not committed (it shows a support representative's name-bearing address) and the transcript's fence hash no longer matches after the line-18 redaction; S13 line appended. The working-tree delta beyond the staged blob is not part of D9 |
| /docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md | Evidence | 0 | 2026-10-28 | Verbatim transcript of the MFFU support reply of 2026-10-28. Landed 2026-11-10 under D9 with the representative's name-bearing address replaced by [rep-address] on line 18 and a dated note; S13 line appended. The source PNG stays out of the repo |
| /docs/reports/2026-10-28-nightly-checks-plan-review-note.md | Report | 2 | 2026-10-28 | Nightly-checks plan review note. Landed 2026-11-10 under D9 from the old staged set; S13 line appended, no other edit |
| /docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md | Report | 2 | 2026-10-28 | Nightly-checks plan review, rebuild. Landed 2026-11-10 under D9 from the old staged set; S13 line appended, no other edit. The working-tree delta beyond the staged blob is not part of D9 |
| /docs/reports/2026-11-10-d9-housekeeping-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-d9-housekeeping (Amear D-2026-11-08-D D9): per-path landing decisions for the 12 old staged paths, itemised de-identification edits, PNG exclusion, MANIFEST rows 329-339, root file F trace and removal, S4/S6 check |
```
### V9. Root file F (F lines captured earlier in this unit, before removal; removal output; trace re-run now)
```
$ ls -la F && xxd F && openssl dgst -sha256 F && git log --all --oneline -- F
-rw-r--r--@ 1 admin  staff  15 Jul 28 12:09 F
00000000: 2320 4449 5350 4154 4348 204c 4f47 0a    # DISPATCH LOG.
SHA2-256(F)= a97839204ed8ef9f69e50ba0b7a40483beb3562616d753cabe0eb05c65a52d2b
9c47b1a WIP: Claude Code rate-limit checkpoint (f3c55a3e)
$ TZ=UTC stat -f %Sm F <session39 reports> (captured before removal)
2026-07-28T16:09:13Z  (F)
2026-07-28T16:12:00Z  (docs/reports/2026-07-28-session39-live-vs-piped-attack.md)
2026-07-28T16:08:04Z  (docs/reports/2026-07-28-session39-closer-negative-tests.md)
$ git status --porcelain -- F; git check-ignore -v F; echo ignored-rc=$?; rm F; ls -la F
?? F
ignored-rc=1
ls: F: No such file or directory
$ git for-each-ref --contains 9c47b1a; git ls-remote origin | grep -c checkpoint; git show 9c47b1a:F | openssl dgst -sha256
9c47b1a55ed40b4edf1d6ea413e4a545bc1a4b72 commit	refs/claude/checkpoint-f3c55a3e
0
SHA2-256(stdin)= a97839204ed8ef9f69e50ba0b7a40483beb3562616d753cabe0eb05c65a52d2b
$ grep -rlF "# DISPATCH LOG" docs/reports/2026-07-28-session39-*.md
docs/reports/2026-07-28-session39-closer-negative-tests.md
docs/reports/2026-07-28-session39-dispatch-log-closer-adversarial.md
docs/reports/2026-07-28-session39-dispatch-log-closer-build.md
docs/reports/2026-07-28-session39-dispatch-log-closer.md
docs/reports/2026-07-28-session39-live-vs-piped-attack.md
```
### V10. Landing copies: per-file counters (S13 | category word | rep-local | sha7 | clinical-filename words | length/date tokens); working-tree mirrors
```
./ISSUE_REGISTER.md | S13=0 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-08-06-session42-r8j-phase3-import.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-08-07-session44-r8j-offset-correction.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-10-28-f4-davi-reply-filing.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-10-28-nightly-checks-plan-review-note.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md | S13=1 | 0 | 0 | 0 | 0 | 0
./docs/specs/2026-08-08-ledger-compaction-spec.md | S13=0 | 0 | 0 | 0 | 0 | 0
$ positive control, same counters on the staged blobs:
docs/reports/2026-08-06-session42-r8j-phase3-import.md | S13=0 | 6 | 0 | 2 | 1 | 2
docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | S13=0 | 0 | 3 | 0 | 0 | 0
docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md | S13=0 | 0 | 1 | 0 | 0 | 0
ISSUE_REGISTER.md | S13=0 | 1 | 0 | 0 | 0 | 0
$ cmp <tree> /tmp/d9-final/<path> for the 7 TREE=yes paths
identical: docs/reports/2026-08-06-session42-r8j-phase3-import.md
identical: docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
identical: docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md
identical: docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md
identical: docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md
identical: docs/reports/2026-08-07-session44-r8j-offset-correction.md
identical: docs/reports/2026-10-28-nightly-checks-plan-review-note.md
```

## Final evidence block (pasted last, after every edit)
```
$ date -u
Tue Nov 10 06:46:04 UTC 2026
$ cd /tmp/d9-final; find . -type f | sort | xargs openssl dgst -sha256
SHA2-256(./ISSUE_REGISTER.md)= 15daefbebcf54d75462c6b551bb48faa449226292d689de294096ff1f712bac4
SHA2-256(./docs/reports/2026-08-06-session42-r8j-phase3-import.md)= 63cbf06897ae72c1146ce82ee41491b7d27dd50e6b13a9969b1f043e2b436650
SHA2-256(./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md)= 54422a448d326e955772b6eb89337ee56e81d7b89c677be4cfeb9c8f0aef4c02
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md)= 3bf5e13d14af85d10af4b2c89f3ed4ad7f4b2ed9d442807e3afcde733c0b742f
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md)= ced9e8d0f480e9630eece1f44dce2607c7ee98919f7ad1127f446d80dc3aee59
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction.md)= 281ca1ce810af350a8c948a3d42aa339ce88fff44ddd570a868863e7b839a528
SHA2-256(./docs/reports/2026-10-28-f4-davi-reply-filing.md)= f5368c511f7ec675814c0d6b7ecce5334aa0f2c7f26c780780cec07d1efb4989
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-note.md)= 16d8b8b882fbfbf42406f34d72be9737fa2007a372366b9c3ecf046225fe8ef4
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md)= 463188f80bd93d984eaf131f79cc8b843e223cf4d161d2ce1b08dc5ac8f63ece
SHA2-256(./docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md)= 8d97d3d6c38f0b24f6dc01e6d90ed95aad15d08c8c4ecd67a6de39152cbf3531
SHA2-256(./docs/specs/2026-08-08-ledger-compaction-spec.md)= 27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6
EXCLUDED: docs/reports/evidence/2026-10-28-mffu-davi-reply.png -- shows a support representative's full-name email address; a binary image cannot be cleaned by a text edit (decided by manager under D-2026-11-08-D D1). Still in the real index:
$ git ls-files -s docs/reports/evidence/2026-10-28-mffu-davi-reply.png
100644 458f3dafa0b54d3be6e3d054098a73e014608106 0	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ git diff HEAD -U0 -- MANIFEST.md | grep "^@@"
@@ -306,0 +307,8 @@
@@ -320,0 +329,11 @@
$ git diff --cached --name-only | openssl dgst -sha256
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
$ git rev-parse HEAD
23556aa7999c1b0763fd746a73fba63300ea911b
$ ls -la F
ls: F: No such file or directory
```

## Correction 1 (2026-11-10)

Started `date -u` = Tue Nov 10 06:53:03 UTC 2026 (fresh, first command of this correction). This correction was written after audit FAIL 1, under the master's correction brief, and covers items A-E only. It is append-only: lines 1-510 above are unchanged (their sha256 is pasted in C1-E), and this section is the only addition to the report. The masks and the S13 convention of the report above still apply. This section does not repeat the standing sentence in any form; the sentence is line 143, directly under the `Verification evidence (command output)` heading.

Real-index fingerprint at the start of this correction (the same command is re-run at the end, in C1-E):
```
$ git diff --cached --name-only | openssl dgst -sha256
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
```

Source note: the brief cites DECISION_LOG.md row 2026-11-10T06:53:00Z for the audit findings and the scope. That row is not on disk. The first check at 06:53:03Z found nothing, and the re-run below finds nothing either; the newest 2026-11-10 row is 06:47:00Z. This correction therefore works from the brief's own text for items A-E.
```
$ grep -n '06:53' DECISION_LOG.md | wc -l | tr -d ' '; grep -o '^- \[2026-11-10T[0-9:]*Z\]' DECISION_LOG.md | tail -1; date -u
0
- [2026-11-10T06:47:00Z]
Tue Nov 10 07:09:22 UTC 2026
```

Sensitive strings: the withheld term, the category word, the rep-local part and the rep's full-name address are each read at runtime into a shell variable from the original unit's off-repo script `/tmp/d9-build/evidence.sh` (lines 2-3, 25, 26 and 89). This is the same runtime-variable method as V5. None of them is typed or printed; only counts are pasted. The generator is `/tmp/d9-corr1/body.sh <part>` (off-repo). Disclosure: while I was locating those lines, one inspection command piped evidence.sh line 89 through `mask.sed`. That file does not mask the line's literal counter patterns, so the stem and the rep-local pattern showed up in my own tool output. They were not written to any file. The leak counts on this section, the spec landing copy and MANIFEST line 339 are pasted in C1-E.

### C1-A. S6 re-run against the gate at HEAD 23556aa (the MAJOR)

```
$ git rev-parse HEAD origin/main
23556aa7999c1b0763fd746a73fba63300ea911b
23556aa7999c1b0763fd746a73fba63300ea911b
```
```
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '165,177p'
# --- C2 park-commit candidate (D-2026-11-08-C C2). HEAD of ROOT must be EXACTLY
# refs/heads/parked/Praxis_build-[a-z0-9]+ (explicit class, no locale ranges).
# symbolic-ref failure (detached HEAD, error) leaves PARK=0 = no exemption.
# No exemption either when GIT_DIR / GIT_WORK_TREE / GIT_COMMON_DIR is set in
# this hook's own environment (the HEAD read would not be ROOT's; adversarial
# case G1, 2026-11-09), or for a subagent caller (agent_id KEY present in the
# payload, any value of any type incl. null, or a payload parse error; subagents
# never commit — scripts/no-commit-guard.sh). Those cases take the token route.
# The ref must also exist under exactly that name (for-each-ref): no unborn HEAD, no case-folded alias.
PARK=0
_pk_ref=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) || _pk_ref=""
# HEAD must name the parked ref DIRECTLY: the unfollowed read must equal the
# followed one (a symref chain HEAD -> WIP|main -> parked/... gets no exemption).
$ git show HEAD:.claude/hooks/gate-commit.sh | awk 'NR>=750 && NR<=761 {printf "%d: %s\n", NR, substr($0,1,100)}'
750:     fi
751:   fi
752:   # staged-TREE binding: the index must still produce the exact tree the token
753:   # was minted against — extra/missing/changed paths in the mint→commit gap deny.
754:   MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
755:   NOW_TREE=$(git_idx write-tree 2>/dev/null)
756:   if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
757:     rm -f "$TOKEN"
758:     echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (
759:     exit 2
760:   fi
761:   # Fix E (A1/A3): record what was allowed, for scripts/commit-tree-verify.sh
$ git show HEAD:.claude/hooks/gate-commit.sh | grep -n 'write-tree\|^  MINT_TREE\|NOW_TREE'
9:#   1. staged-TREE binding — token carries `tree=<git write-tree>` from mint time;
32:#      GIT_INDEX_FILE set in this hook's own env, denies. Hash + write-tree run
254:  # Fix C (A2): the gate hashes and write-trees ROOT; the Bash call runs in the
754:  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
755:  NOW_TREE=$(git_idx write-tree 2>/dev/null)
756:  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
758:    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MINT_TREE:-missing/legacy-token}, current tree=${NOW_TREE:-unresolvable}). Something changed the index after mint — re-stage exactly the audited set and re-dispatch the orchestrator-auditor." >&2
$ git diff --stat HEAD -- .claude/hooks/gate-commit.sh | wc -l
       0
$ for c in $(git log --format=%h -- .claude/hooks/gate-commit.sh); do printf '%s %s ' $c "$(git log -1 --format=%cs $c)"; git show $c:.claude/hooks/gate-commit.sh | grep -n 'NOW_TREE=' | cut -c1-20 | tr '\n' ' '; echo; done
23556aa 2026-11-10 755:  NOW_TREE=$(git 
933ef70 2026-11-06 690:  NOW_TREE=$(git 
84b1a58 2026-11-06 603:  NOW_TREE=$(git 
8a872d9 2026-07-12 170:  NOW_TREE=$(cd  
fec1722 2026-07-10 143:  NOW_TREE=$(cd  
291826f 2026-07-08 
$ git show 8a872d9:.claude/hooks/gate-commit.sh | awk 'NR>=167 && NR<=176 {printf "%d: %s\n", NR, substr($0,1,100)}'
167:   # staged-TREE binding: the index must still produce the exact tree the token
168:   # was minted against — extra/missing/changed paths in the mint→commit gap deny.
169:   MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
170:   NOW_TREE=$(cd "$ROOT" && git write-tree 2>/dev/null)
171:   if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
172:     rm -f "$TOKEN"
173:     echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (
174:     exit 2
175:   fi
176:   rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
$ git show HEAD:.claude/hooks/gate-commit.sh | awk 'NR>=654 && NR<=668 {printf "%d: %s\n", NR, substr($0,1,100)}'
654: # --- C2 park-commit exemption (D-2026-11-08-C C2). Reached only after every
655: # check above passed for a PARK candidate. HEAD is re-read and must be the same
656: # parked ref; any change or error denies (fail closed).
657: if [ "$PARK" = 1 ]; then
658:   _pk_ref2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) |
659:   _pk_nr2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q --no-recurse HEAD 2>
660:   if [ -n "$_pk_ref2" ] && [ -n "$_pk_nr2" ] && [ "$_pk_ref2" = "$_pk_ref" ] && [ "$_pk_nr2" = "$_pk
661:     echo "Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branc
662:     exit 0
663:   fi
664:   echo "Commit denied: HEAD moved during the park-commit check (was '${_pk_ref}', now '${_pk_ref2:-u
665:   exit 2
666: fi
667: 
668: # --- Token + AUDIT_LOG checks: only a fresh token whose hash also appears as a
$ git show HEAD:.claude/hooks/gate-commit.sh | grep -n '^if \[ -f "$TOKEN" \]'
681:if [ -f "$TOKEN" ]; then
```

Further gate evidence: the temp-index route, the deny that fires first, the unarmed exit, and the spec's first commit.
```
$ echo "8a872d9 GIT_INDEX_FILE refs: $(git show 8a872d9:.claude/hooks/gate-commit.sh | grep -c GIT_INDEX_FILE)   HEAD GIT_INDEX_FILE refs: $(git show HEAD:.claude/hooks/gate-commit.sh | grep -c GIT_INDEX_FILE)"
8a872d9 GIT_INDEX_FILE refs: 0   HEAD GIT_INDEX_FILE refs: 31
$ git show HEAD:.claude/hooks/gate-commit.sh | awk 'NR==128 || (NR>=422 && NR<=429) || (NR>=678 && NR<=681) || (NR>=775 && NR<=779) {printf "%d: %s\n", NR, substr($0,1,100)}'
128: [ -f "$STATE/orchestrator-active" ] || exit 0
422: # git under the selected index (REAL => GIT_INDEX_FILE removed from env)
423: git_idx() {
424:   if [ "$IDX" = "REAL" ]; then
425:     (cd "$ROOT" && env -u GIT_INDEX_FILE git "$@")
426:   else
427:     (cd "$ROOT" && GIT_INDEX_FILE="$IDX" git "$@")
428:   fi
429: }
678: HASH=$(git_idx diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none 
679: TOKEN="$STATE/audit-pass-$HASH"
680: # (caller identity / STACK_MASTER is computed above, before the form checks)
681: if [ -f "$TOKEN" ]; then
775:   rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
776:   exit 0
777: fi
778: echo "Commit denied: no audit PASS token for this exact staged diff under index '$IDX' (the staged s
779: exit 2
$ git show 8a872d9:.claude/hooks/gate-commit.sh | awk '(NR>=152 && NR<=154) || (NR>=179 && NR<=180) {printf "%d: %s\n", NR, substr($0,1,100)}'
152: HASH=$(cd "$ROOT" && git diff --cached | shasum -a 256 | awk '{print $1}')
153: TOKEN="$STATE/audit-pass-$HASH"
154: if [ -f "$TOKEN" ]; then
179: echo "Commit denied: no audit PASS token for this exact staged diff (the staged set may have changed
180: exit 2
$ git log --format='%h %cs' --diff-filter=A -- docs/specs/2026-08-08-ledger-compaction-spec.md
28b3922 2026-08-09
```

What the output shows:

1. At HEAD, `gate-commit.sh:165-177` is C2 park-commit code (the `PARK=0` candidate block), not the staged-tree binding.
2. At HEAD the staged-tree binding is at `:752-760`: comment 752-753, `MINT_TREE` 754, `NOW_TREE` 755, the compare 756, the deny 757-759 and `fi` 760. The working-tree gate equals HEAD (`git diff --stat` is empty).
3. C-9's `:167-176` matches gate `8a872d9` (2026-07-12). There, :167-175 is the same binding and :176 consumes the token. That gate was current when the spec was first committed (`28b3922`, 2026-08-09, pasted above). The gate grew in `84b1a58` and `933ef70` (both 2026-11-06) and again in `23556aa`.

S6 re-grade. This supersedes the `:167-176` citation and the "+12/-2" wording in the S6 paragraph above (line 118), and it replaces this section's own first draft, which the adversarial check found wrong (C1-F, finding 1).

(a) Landing the spec still only RECORDS the C-9 collision. It adds K7 `[PROPOSED]` and note C-9, changes no gate code, and ratifies nothing. That part of line 118 stands.

(b) Does the collision still hold at HEAD? Only on one of the gate's routes.
- **Real-index token route:** yes. A compact.sh run that stages into the real index between mint and commit changes `diff --cached`. The token lookup is keyed on that diff's hash (`:678-681`), so it finds no token and the gate denies at `:778`. That deny comes before the tree binding at `:754-759` is reached. The binding catches only a tree change whose diff hash still matches. At `8a872d9` the order was the same (hash `:152-154`, deny `:179`), so C-9's line cite pointed at the second check even then. Its conclusion, "denies that commit", is right for this route.
- **Temp-index token route:** no. This route arrived after the spec. `8a872d9` has 0 `GIT_INDEX_FILE` references and HEAD has 31. On this route, `git_idx` (`:423-429`) computes the hash (`:678`) and `NOW_TREE` (`:755`) from the selected temp index. A compact.sh run that stages into the real index changes neither value, so the commit is NOT denied, and the compaction stays staged in the real index, outside that commit. This is the route the master uses for landings, for example `/tmp/idx-d9`.
- **C2 park route:** no. On a branch named `parked/Praxis_build-<id>`, the exemption allows the commit at `:657-662` (`exit 0`) before any token lookup (`:678-681`). Whatever compact.sh staged into that branch's index rides into the commit unaudited, which is by design on that route. Whether the minter refuses to mint on a parked branch was not observed here.
- **Unarmed:** with no `.claude/state/orchestrator-active` marker, the gate exits 0 at `:128`. No route is gated then.

(c) Item B's dictated pointer note ends "The C-9 collision itself is unchanged." By (b), that holds only for the real-index token route. I appended the note verbatim as the brief directs (C1-B). Making it accurate would change spec text beyond the dictated words, which the brief rules out. That is left to the master (open item C1-G.1).

Graded: S6 is now tested against the current gate, and the result is recorded here. Landing the spec changes no other block's behaviour, so on the cross-block test S6 PASSES for this unit. But the C-9 text, and the last sentence of the dictated pointer note, under-describe the current gate: they are accurate only on the real-index token route. The C-9 collision is still carried open, and it is now wider than C-9 says.

### C1-B. Pointer note appended to the spec (landing copy and working tree)

Before the edit (output as captured in this correction, before the append):
```
$ S=docs/specs/2026-08-08-ledger-compaction-spec.md; tail -c 1 $S | xxd | head -1; tail -c 1 /tmp/d9-final/$S | xxd | head -1; cmp $S /tmp/d9-final/$S && echo CMP-BEFORE-EQUAL; openssl dgst -sha256 $S /tmp/d9-final/$S
00000000: 0a                                       .
00000000: 0a                                       .
CMP-BEFORE-EQUAL
SHA2-256(docs/specs/2026-08-08-ledger-compaction-spec.md)= 27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6
SHA2-256(/tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md)= 27ad8286fecad451fd5775dd8279a5f8a390d3a1792f707821218e3dbce0f5e6
```
I appended one blank line and the pointer note to the landing copy with `printf '\n%s\n' "$NOTE" >> /tmp/d9-final/<spec>`, then copied the landing copy over the working-tree file (`cp`). The range in the note is the one observed in C1-A, `:752-760`. Nothing else in the spec changed:
```
$ git diff --numstat HEAD -- docs/specs/2026-08-08-ledger-compaction-spec.md
14	2	docs/specs/2026-08-08-ledger-compaction-spec.md
$ diff <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md
111a112,113
> 
> Pointer note appended 2026-11-10 under D9 (D-2026-11-08-D): C-9's `.claude/hooks/gate-commit.sh:167-176` was written against an older gate; as of commit 23556aa the staged-tree binding it describes is at `.claude/hooks/gate-commit.sh:752-760`. The C-9 collision itself is unchanged.
$ cmp docs/specs/2026-08-08-ledger-compaction-spec.md /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md && echo identical
identical
```

### C1-C. S1 fixes

C1-C.1. The V4 rows that were masked as `[n]` (V4 above), now unmasked as counts. The variables are read at runtime from `/tmp/d9-build/evidence.sh`: line 25 holds the V4 category-word counter, line 26 the V4 rep-local counter, and line 89 the V10 stem.
```
$ EV=/tmp/d9-build/evidence.sh; CAT=$(sed -n 25p $EV | awk '{print $11}'); STEM=$(sed -n 89p $EV | grep -oE 'grep -ci [a-z]+ ' | head -1 | awk '{print $3}'); REP=$(sed -n 26p $EV | awk '{print $10}' | tr -d "'")
$ [ -n "$CAT" ] && [ -n "$STEM" ] && [ -n "$REP" ] && echo vars-nonempty; case "$CAT" in "$STEM"*) echo CAT-begins-with-STEM;; esac
vars-nonempty
CAT-begins-with-STEM
$ git grep -il -- "$CAT" HEAD -- . | wc -l | tr -d " "     # V4 row "files with category word at HEAD" (evidence.sh line 25 form)
11
$ git grep -il -- "$STEM" HEAD -- . | wc -l | tr -d " "    # same, with the shorter stem used by the V10 counter
12
$ git show HEAD:DECISIONS.md | sed -n 1142p | grep -ci -- "$CAT"; git show HEAD:specs/SPEC_RUBRIC.md | grep -ci -- "$CAT"
1
1
$ git grep -l -- "$REP" HEAD -- . | wc -l | tr -d " "      # V4 row "files with rep-local at HEAD"
0
$ ADDR=$(git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -oiE -- "${REP}[A-Za-z0-9._-]*@[A-Za-z0-9.-]*[A-Za-z]" | sort -u); printf "%s\n" "$ADDR" | grep -c .
1
$ git grep -ilF -- "$ADDR" HEAD -- . | wc -l | tr -d " "  # HEAD files holding the full-name rep address
0
$ git grep -hiF -- "$ADDR" HEAD -- . | wc -l | tr -d " "  # HEAD lines holding it
0
$ git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | grep -ciF -- "$ADDR"   # positive control: old staged blob
2
$ grep -rilF -- "$ADDR" /tmp/d9-final | wc -l | tr -d " "  # landing copies holding it
0
```

So the V4 row "files with category word at HEAD" is **11** (the shorter V10 stem gives 12). The V4 row "files with rep-local at HEAD" is **0**. The rep's full-name address is in **0** HEAD files and 0 HEAD lines. The positive control, the old staged f4 evidence blob, gives 2 lines, so the 0 is not a dead grep.

Correction to line 36 and open item 1 (line 135): both say the category word is public at HEAD in "14 files". At HEAD the number is 11 (12 with the stem). The 14 is the stem's count in the REAL INDEX, not at HEAD (pasted in C1-F). The two named examples, `DECISIONS.md:1142` and `specs/SPEC_RUBRIC.md`, are confirmed (1 and 1 above).

C1-C.2. Line 127 restated. Line 127 says the counters that read 0 on the landing copies "read non-zero on the staged blobs (V5, V10)". For V5 (the withheld term) that is wrong. No old staged blob held the withheld term: all 11 staged text blobs give count 0, the same as the 11 landing copies (both below). The V5 positive control is:
- the injection liveness already in V5 (`LIVENESS=1` on every file);
- the HEAD files: the same `$TERM` and the same `grep -iF` find the term in 3 tracked files at HEAD, once each.

File names are withheld, as in open item 1. The sha256 of the name list is pasted so the set can be checked again. For V10 (category word, rep-local, sha7, filename words, length/date tokens), line 127 stands: V10's staged-blob rows show non-zero counts.
```
$ eval "$(sed -n 2,3p /tmp/d9-build/evidence.sh)"   # sets SRC and TERM exactly as V5 did; TERM never printed
$ [ -n "$TERM" ] && echo TERM-nonempty
TERM-nonempty
$ git grep -ilF -- "$TERM" HEAD -- . | wc -l | tr -d " "
3
$ i=0; git grep -ciF -- "$TERM" HEAD -- . | while IFS= read -r l; do i=$((i+1)); echo "HEAD-file-$i count=${l##*:}"; done
HEAD-file-1 count=1
HEAD-file-2 count=1
HEAD-file-3 count=1
$ git grep -ilF -- "$TERM" HEAD -- . | openssl dgst -sha256 | awk "{print \$2}"   # names withheld; hash of the name list
49962ad565dc0a19862b8266a0f05019e24d7ac6e42909f196efbb93c56c6765
$ for p in $(cd /tmp/d9-final && find . -type f | sort | sed "s|^\./||"); do echo ":$p count=$(git show :$p | grep -ciF -- "$TERM")"; done
:ISSUE_REGISTER.md count=0
:docs/reports/2026-08-06-session42-r8j-phase3-import.md count=0
:docs/reports/2026-08-07-f4-mffu-compliance-evidence.md count=0
:docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md count=0
:docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md count=0
:docs/reports/2026-08-07-session44-r8j-offset-correction.md count=0
:docs/reports/2026-10-28-f4-davi-reply-filing.md count=0
:docs/reports/2026-10-28-nightly-checks-plan-review-note.md count=0
:docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md count=0
:docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md count=0
:docs/specs/2026-08-08-ledger-compaction-spec.md count=0
$ for p in $(cd /tmp/d9-final && find . -type f | sort | sed "s|^\./||"); do echo "/tmp/d9-final/$p count=$(grep -ciF -- "$TERM" /tmp/d9-final/$p)"; done
/tmp/d9-final/ISSUE_REGISTER.md count=0
/tmp/d9-final/docs/reports/2026-08-06-session42-r8j-phase3-import.md count=0
/tmp/d9-final/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md count=0
/tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md count=0
/tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md count=0
/tmp/d9-final/docs/reports/2026-08-07-session44-r8j-offset-correction.md count=0
/tmp/d9-final/docs/reports/2026-10-28-f4-davi-reply-filing.md count=0
/tmp/d9-final/docs/reports/2026-10-28-nightly-checks-plan-review-note.md count=0
/tmp/d9-final/docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md count=0
/tmp/d9-final/docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md count=0
/tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md count=0
```

C1-C.3. MANIFEST row numbers. Everywhere this report gives MANIFEST row numbers, they are **working-tree line numbers**:
- line 39 and line 131: "329-339";
- line 112: "329-338" and "339";
- V8: `@@ -320,0 +329,11 @@` and `sed -n 329,339p`;
- line 426: the old text of the report's own row, pasted in V8;
- line 503: the hunk header in the final block.

The working tree also holds the 8 uncommitted U7 rows at 307-314, which are not in the commit. In the commit index `/tmp/idx-d9` (HEAD's 320 lines plus these 11 rows), the same 11 rows are **321-331**:
```
$ git show HEAD:MANIFEST.md | wc -l
     320
$ diff <(GIT_INDEX_FILE=/tmp/idx-d9 git show :MANIFEST.md | sed -n '321,331p' | cut -d'|' -f2) <(sed -n '329,339p' MANIFEST.md | cut -d'|' -f2) && echo same-paths-in-same-order
same-paths-in-same-order
$ GIT_INDEX_FILE=/tmp/idx-d9 git show :MANIFEST.md | awk 'NR>=321 && NR<=331 {split($0,a,"|"); print NR":"a[2]}'
321: /ISSUE_REGISTER.md 
322: /docs/reports/2026-08-06-session42-r8j-phase3-import.md 
323: /docs/reports/2026-08-07-session44-r8j-offset-correction.md 
324: /docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md 
325: /docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md 
326: /docs/specs/2026-08-08-ledger-compaction-spec.md 
327: /docs/reports/2026-10-28-f4-davi-reply-filing.md 
328: /docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md 
329: /docs/reports/2026-10-28-nightly-checks-plan-review-note.md 
330: /docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md 
331: /docs/reports/2026-11-10-d9-housekeeping-manager.md 
```

### C1-D. MANIFEST working-tree line 339 (this report's own row)

Line 339 claimed "MANIFEST rows 329-339". I made two edits to that row only, each a python one-row replace of list index 338 with an assert that the old phrase occurs exactly once.

First edit, as run inline:
```
p='/Volumes/Sensidine/Praxis.build/MANIFEST.md'
L=open(p,encoding='utf-8').read().split('\n')
old=', MANIFEST rows 329-339, '
assert L[338].count(old)==1, L[338].count(old)
L[338]=L[338].replace(old,', MANIFEST rows for the 11 landing paths and this report, ')
L[338]=L[338].replace('S4/S6 check |','S4/S6 check; Correction 1 appended 2026-11-10 (S6 re-run against the gate at 23556aa, C-9 pointer note, S1 counts) |')
assert L[338].endswith('(S6 re-run against the gate at 23556aa, C-9 pointer note, S1 counts) |')
open(p,'w',encoding='utf-8').write('\n'.join(L))
```
Second edit (after C1-F finding 7: only 10 landing paths got new rows, because the f4 evidence already had HEAD row 132):
```
$ cat /tmp/d9-corr1/row339.py
p='/Volumes/Sensidine/Praxis.build/MANIFEST.md'
L=open(p,encoding='utf-8').read().split('\n')
old='MANIFEST rows for the 11 landing paths and this report'
new='MANIFEST rows for 10 landing paths (the f4 compliance evidence already had HEAD row 132) and this report'
assert L[338].count(old)==1
L[338]=L[338].replace(old,new)
open(p,'w',encoding='utf-8').write('\n'.join(L))
```

No other MANIFEST line was touched. The hunk headers are unchanged. Against the audited index blob, only the one row differs (2 diff lines: 1 removed, 1 added):
```
$ git diff HEAD -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -320,0 +329,11 @@
$ sed -n '339p' MANIFEST.md
| /docs/reports/2026-11-10-d9-housekeeping-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-d9-housekeeping (Amear D-2026-11-08-D D9): per-path landing decisions for the 12 old staged paths, itemised de-identification edits, PNG exclusion, MANIFEST rows for 10 landing paths (the f4 compliance evidence already had HEAD row 132) and this report, root file F trace and removal, S4/S6 check; Correction 1 appended 2026-11-10 (S6 re-run against the gate at 23556aa, C-9 pointer note, S1 counts) |
$ wc -l < MANIFEST.md
     339
$ diff <(GIT_INDEX_FILE=/tmp/idx-d9 git show :MANIFEST.md) <(git show HEAD:MANIFEST.md; sed -n 329,339p MANIFEST.md) | grep -c '^[<>]'   # vs the audited index blob: only the one row differs
2
$ sed -n '334p' MANIFEST.md | grep -o 'the old staged +12/-2 change lands byte-for-byte'
the old staged +12/-2 change lands byte-for-byte
```

### C1-F. Adversarial findings (one praxis-worker, ADVERSARIAL, foreground; report off-repo at `/tmp/d9-offrepo/2026-11-10-d9-housekeeping-corr1-adversarial.md`)

The worker was given the artifacts and the criteria only. It re-ran every pasted command and found no output that differs. It found 0 privacy hits, the 510-line prefix hash unchanged, an S13 count of 1, the spec `cmp` equal, both hunk headers as stated and one changed MANIFEST row. Its index fingerprint was `5bfab445…bda95` at start and end. Its findings, and what was done:

1. MAJOR: the first draft said the collision "still holds at HEAD on the token route" and that C-9 "stays true as written". That is false on the temp-index route, and the park route was assumed rather than shown. I re-checked it (C1-A, second block, pasted) and rewrote the S6 re-grade: route-by-route, with the temp-index and unarmed routes added.
2. MINOR: on the token route, the deny that fires first is the hash-keyed lookup (`:678-681` then `:778`), not `:754-759`. Folded into C1-A (b).
3. MAJOR: "C1-E" was cited but did not exist yet, and the end fingerprint and leak counts were not pasted. The draft was reviewed before the final block was written; C1-E is now below, with the leak counts.
4. MINOR: "No output supports 14" was false. I re-checked it:
```
$ (CAT and STEM set as in C1-C.1)
$ git grep --cached -il -- "$STEM" | wc -l | tr -d " "   # real index, stem
14
$ git grep --cached -il -- "$CAT" | wc -l | tr -d " "    # real index, category word
13
$ git grep -il -- "$STEM" HEAD -- . | wc -l | tr -d " "  # HEAD, stem
12
```
   C1-C.1 now says the 14 is the stem's count in the real index.
5. MINOR: the row-number cite list was wrong (line 7 has no row numbers; line 112 says 329-338 and 339). Fixed in C1-C.3.
6. MINOR: four claims were described rather than pasted (the DECISION_LOG grep, the spec's first commit, the cmp before the edit, the python edit), and ":167-176" was called the binding when 176 is the token consumption. All are now pasted (PART H, C1-A second block, C1-B, C1-D), and C1-A item 3 is reworded.
7. MINOR: MANIFEST:339's "rows for the 11 landing paths" could be read as 11 new rows. Reworded (C1-D, second edit).

### C1-G. Open items for the master (not edited; outside items A-E)

1. The spec's C-9, and the last sentence of the dictated pointer note ("The C-9 collision itself is unchanged."), hold only on the real-index token route (C1-A (b)). Amending either is spec text beyond item B.
2. MANIFEST working-tree line 334 (the spec's row; index row 326) still says "the old staged +12/-2 change lands byte-for-byte". After item B the landing copy is the staged blob plus the 2-line pointer note, which is +14/-2 against HEAD (C1-B). The brief says to touch no other MANIFEST line, so the row is left as is.
3. `/tmp/idx-d9` was built before this correction. Its MANIFEST, spec and report blobs no longer match the working tree or `/tmp/d9-final`. It was only read here (C1-C.3, C1-D), never written.

Result line: this correction adds no `Result:` line, and line 145 (`Result: PASS`) still governs. Items A-E are done. The open items in C1-G are flagged, not hidden; they do not reverse the cross-block grade in C1-A.

### C1-E. Final evidence (pasted last, after every edit)

Every edit of this correction (spec note, MANIFEST line 339, report section) was made before this block was generated. The variables are set as in C1-C (TERM via evidence.sh lines 2-3, CAT line 25, STEM line 89, REP line 26, ADDR from the old staged f4 evidence blob) and are never printed. `S13=$(sed -n 143p <report>)`. The `wc -l` line was run after this block was appended, and its value was checked against the file.
```
$ date -u
Tue Nov 10 07:09:54 UTC 2026
$ cd /tmp/d9-final; find . -type f | sort | xargs openssl dgst -sha256; cd /Volumes/Sensidine/Praxis.build
SHA2-256(./ISSUE_REGISTER.md)= 15daefbebcf54d75462c6b551bb48faa449226292d689de294096ff1f712bac4
SHA2-256(./docs/reports/2026-08-06-session42-r8j-phase3-import.md)= 63cbf06897ae72c1146ce82ee41491b7d27dd50e6b13a9969b1f043e2b436650
SHA2-256(./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md)= 54422a448d326e955772b6eb89337ee56e81d7b89c677be4cfeb9c8f0aef4c02
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md)= 3bf5e13d14af85d10af4b2c89f3ed4ad7f4b2ed9d442807e3afcde733c0b742f
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md)= ced9e8d0f480e9630eece1f44dce2607c7ee98919f7ad1127f446d80dc3aee59
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction.md)= 281ca1ce810af350a8c948a3d42aa339ce88fff44ddd570a868863e7b839a528
SHA2-256(./docs/reports/2026-10-28-f4-davi-reply-filing.md)= f5368c511f7ec675814c0d6b7ecce5334aa0f2c7f26c780780cec07d1efb4989
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-note.md)= 16d8b8b882fbfbf42406f34d72be9737fa2007a372366b9c3ecf046225fe8ef4
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md)= 463188f80bd93d984eaf131f79cc8b843e223cf4d161d2ce1b08dc5ac8f63ece
SHA2-256(./docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md)= 8d97d3d6c38f0b24f6dc01e6d90ed95aad15d08c8c4ecd67a6de39152cbf3531
SHA2-256(./docs/specs/2026-08-08-ledger-compaction-spec.md)= 814e7180a8da7d79e62bb58a0822c01debcf704024087cb648f17f4c535a3472
$ diff <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md
111a112,113
> 
> Pointer note appended 2026-11-10 under D9 (D-2026-11-08-D): C-9's `.claude/hooks/gate-commit.sh:167-176` was written against an older gate; as of commit 23556aa the staged-tree binding it describes is at `.claude/hooks/gate-commit.sh:752-760`. The C-9 collision itself is unchanged.
$ cmp /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md docs/specs/2026-08-08-ledger-compaction-spec.md && echo identical
identical
$ grep -cxF -- "$S13" docs/reports/2026-11-10-d9-housekeeping-manager.md    # S13: the standing sentence as a whole line
1
$ grep -nF -- "$(echo "$S13" | cut -d';' -f1)" docs/reports/2026-11-10-d9-housekeeping-manager.md | cut -d: -f1 | tr '\n' ' '; echo   # line numbers holding its first clause: 143 = the sentence, 159 = the V2 command (pre-existing, above line 510)
143 159 
$ head -n 510 docs/reports/2026-11-10-d9-housekeeping-manager.md | openssl dgst -sha256   # lines 1-510 unchanged (same value as before this correction)
SHA2-256(stdin)= fced09de9df3abc497b570c84d45951a898827a70f05e22162c22b0259ee0559
$ for f in "tail -n +511 docs/reports/2026-11-10-d9-housekeeping-manager.md" "cat /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md" "sed -n 339p MANIFEST.md"; do echo "$f | TERM=$(eval "$f" | grep -ciF -- "$TERM") CAT=$(eval "$f" | grep -ci -- "$CAT") STEM=$(eval "$f" | grep -ci -- "$STEM") REP=$(eval "$f" | grep -ci -- "$REP") ADDR=$(eval "$f" | grep -ciF -- "$ADDR") S13clause=$(eval "$f" | grep -cF -- "$(echo "$S13" | cut -d";" -f1)")"; done
tail -n +511 docs/reports/2026-11-10-d9-housekeeping-manager.md | TERM=0 CAT=0 STEM=0 REP=0 ADDR=0 S13clause=0
cat /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md | TERM=0 CAT=0 STEM=0 REP=0 ADDR=0 S13clause=0
sed -n 339p MANIFEST.md | TERM=0 CAT=0 STEM=0 REP=0 ADDR=0 S13clause=0
$ grep -n '^Result:' docs/reports/2026-11-10-d9-housekeeping-manager.md; grep -n '^## Verification evidence (command output)' docs/reports/2026-11-10-d9-housekeeping-manager.md
145:Result: PASS
141:## Verification evidence (command output)
$ git diff HEAD -U0 -- MANIFEST.md | grep '^@@'; sed -n '339p' MANIFEST.md | cut -c1-80
@@ -306,0 +307,8 @@
@@ -320,0 +329,11 @@
| /docs/reports/2026-11-10-d9-housekeeping-manager.md | Report | 2 | 2026-11-10 
$ wc -l < docs/reports/2026-11-10-d9-housekeeping-manager.md   # run after this block was appended
     913
$ git diff --cached --name-only | openssl dgst -sha256
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
$ git rev-parse HEAD
23556aa7999c1b0763fd746a73fba63300ea911b
```

## Correction 1b (2026-11-10)

Why. The pointer note dictated by the master for Correction 1 ended "The C-9 collision itself is unchanged." C1-A (b) showed that this holds only on the real-index token route, so the sentence over-claims (S2). C1-G.1 flagged it and C1-G.2 flagged MANIFEST line 334. DECISION_LOG row 2026-11-10T07:11:00Z (master, under D-2026-11-08-D D1) decided this bounded correction: replace only the note's last sentence (landing copy and working tree), fix the MANIFEST line 334 text, append this section, and paste all final-blob evidence last. No worker was dispatched; the brief said none was needed. Lines 1-913 of this report are unchanged (prefix hash in C1b-D).

Scope of the claim. The route statements in the new sentence come from reading the gate's code at 23556aa (pasted below). No gate was trip-tested for this correction, and the new note says so ("not trip-tested").

### C1b-A. Spec pointer note: last sentence replaced (landing copy and working tree)

Gate ranges at HEAD that the new sentence cites, re-pasted in this correction:
```
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '423,429{=;p;}' | paste - - | cut -c1-120
423	git_idx() {
424	  if [ "$IDX" = "REAL" ]; then
425	    (cd "$ROOT" && env -u GIT_INDEX_FILE git "$@")
426	  else
427	    (cd "$ROOT" && GIT_INDEX_FILE="$IDX" git "$@")
428	  fi
429	}
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '654,663{=;p;}' | paste - - | cut -c1-120
654	# --- C2 park-commit exemption (D-2026-11-08-C C2). Reached only after every
655	# check above passed for a PARK candidate. HEAD is re-read and must be the same
656	# parked ref; any change or error denies (fail closed).
657	if [ "$PARK" = 1 ]; then
658	  _pk_ref2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q HEAD 2>/dev/null) || _pk_ref2=""
659	  _pk_nr2=$(cd "$ROOT" 2>/dev/null && env -u GIT_INDEX_FILE git symbolic-ref -q --no-recurse HEAD 2>/dev/null) || _p
660	  if [ -n "$_pk_ref2" ] && [ -n "$_pk_nr2" ] && [ "$_pk_ref2" = "$_pk_ref" ] && [ "$_pk_nr2" = "$_pk_ref" ]; then
661	    echo "Commit allowed without an audit token: park-commit exemption (D-2026-11-08-C C2) for branch '${_pk_ref#ref
662	    exit 0
663	  fi
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '676,682{=;p;}' | paste - - | cut -c1-120
676	# file into an opaque base85 patch) and --ignore-submodules=none (a repo
677	# diff.ignoreSubmodules=all can no longer hide a gitlink).
678	HASH=$(git_idx diff --cached --no-ext-diff --no-textconv --no-color --text --ignore-submodules=none --no-relative | 
679	TOKEN="$STATE/audit-pass-$HASH"
680	# (caller identity / STACK_MASTER is computed above, before the form checks)
681	if [ -f "$TOKEN" ]; then
682	  NOW=$(date +%s)
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '750,760{=;p;}' | paste - - | cut -c1-120
750	    fi
751	  fi
752	  # staged-TREE binding: the index must still produce the exact tree the token
753	  # was minted against — extra/missing/changed paths in the mint→commit gap deny.
754	  MINT_TREE=$(sed -n 's/^tree=//p' "$TOKEN" | head -1)
755	  NOW_TREE=$(git_idx write-tree 2>/dev/null)
756	  if [ -z "$MINT_TREE" ] || [ -z "$NOW_TREE" ] || [ "$MINT_TREE" != "$NOW_TREE" ]; then
757	    rm -f "$TOKEN"
758	    echo "Commit denied: staged tree no longer matches the tree the audit token was minted against (minted tree=${MI
759	    exit 2
760	  fi
$ git show HEAD:.claude/hooks/gate-commit.sh | sed -n '775,779{=;p;}' | paste - - | cut -c1-120
775	  rm -f "$TOKEN"   # single-use: consumed at allow time, before the commit runs
776	  exit 0
777	fi
778	echo "Commit denied: no audit PASS token for this exact staged diff under index '$IDX' (the staged set may have chan
779	exit 2
```
What these lines show: `git_idx` runs git under the selected index (`:423-429`); the token is looked up by the hash of `git_idx diff --cached` (`:678-681`); with no token for that hash the gate denies (`:778-779`); with a token, `NOW_TREE` comes from `git_idx write-tree` and must equal the minted tree (`:754-759`); a confirmed park candidate exits 0 at `:657-662`, which comes before the token lookup at `:678-681`.

Removed sentence: "The C-9 collision itself is unchanged." It was replaced, in place, by two sentences, using a python edit on the landing copy that asserted the old sentence occurred exactly once, at the end of the file. The landing copy was then copied over the working-tree file. Nothing else in the spec changed:
```
$ diff <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md
111a112,113
> 
> Pointer note appended 2026-11-10 under D9 (D-2026-11-08-D): C-9's `.claude/hooks/gate-commit.sh:167-176` was written against an older gate; as of commit 23556aa the staged-tree binding it describes is at `.claude/hooks/gate-commit.sh:752-760`. Read from the gate's code at 23556aa, not trip-tested: the collision holds for a token commit made from the real index, where a changed staged diff finds no token keyed on its hash (`:678-681`) and is denied at `:778`; a temp-index commit is checked against that index's own hash and tree (`git_idx` at `:423-429`, used at `:678` and `:755`), so staging in the real index does not by itself cause a deny there. A commit on a `parked/Praxis_build-<id>` branch is allowed at `:657-662` (C2) before any token check.
$ git diff --numstat HEAD -- docs/specs/2026-08-08-ledger-compaction-spec.md
14	2	docs/specs/2026-08-08-ledger-compaction-spec.md
$ cmp /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md docs/specs/2026-08-08-ledger-compaction-spec.md && echo identical
identical
```

### C1b-B. MANIFEST line 334 (the spec's row)

Only the clause "the old staged +12/-2 change lands byte-for-byte" was changed. The numstats it now states (HEAD to staged blob, and HEAD to landing copy):
```
$ git show HEAD:docs/specs/2026-08-08-ledger-compaction-spec.md > /tmp/d9-1b-scripts/spec-head.md; git show :docs/specs/2026-08-08-ledger-compaction-spec.md > /tmp/d9-1b-scripts/spec-staged.md
$ git diff --no-index --numstat /tmp/d9-1b-scripts/spec-head.md /tmp/d9-1b-scripts/spec-staged.md
12	2	/tmp/d9-1b-scripts/{spec-head.md => spec-staged.md}
$ git diff --no-index --numstat /tmp/d9-1b-scripts/spec-head.md /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md
14	2	/tmp/{d9-1b-scripts/spec-head.md => d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md}
$ diff /tmp/d9-1b-scripts/MANIFEST.before MANIFEST.md | cut -c1-90   # MANIFEST.before = cp taken just before the edit
334c334
< | /docs/specs/2026-08-08-ledger-compaction-spec.md | Spec | 0 | 2026-08-09 | Ledger-comp
---
> | /docs/specs/2026-08-08-ledger-compaction-spec.md | Spec | 0 | 2026-08-09 | Ledger-comp
$ git diff HEAD -U0 -- MANIFEST.md | grep '^@@'
@@ -306,0 +307,8 @@
@@ -320,0 +329,11 @@
```
The hunk headers are unchanged from C1-E (`@@ -306,0 +307,8 @@` and `@@ -320,0 +329,11 @@`), so line 334 is still inside the added D9 block, and no HEAD line is touched.

### C1b-C. Status of the Correction 1 open items

- C1-G.1 (note over-claims): closed by C1b-A. C-9's own text in the spec is not amended; the dated note now states the per-route reading.
- C1-G.2 (MANIFEST line 334): closed by C1b-B.
- C1-G.3 (`/tmp/idx-d9` built before Correction 1): still open, and wider now. Its spec and MANIFEST blobs also predate this correction. Not written here; the master rebuilds it (DECISION_LOG 07:11:00Z).

S6, restated: PASS for this unit on the cross-block test. Landing the spec changes no gate behaviour, and the pointer note now states the C-9 collision per route as read from the gate code at 23556aa (a code read, not a trip test). The collision itself stays open.

### C1b-D. Final evidence (pasted last, after every edit)

Every edit of this correction (spec note in both copies, MANIFEST line 334, sections C1b-A to C1b-C) was made before this block was generated. `S13=$(sed -n 143p <report>)`. TERM is set by evaluating evidence.sh lines 2-3 in the shell; CAT, STEM and REP are set from evidence.sh lines 25, 89 and 26 as in C1-C. None of them is printed. The `wc -l` value is the line count of the report after this block was appended: I computed it as (count before the append) + (lines in this block), then re-ran `wc -l` on the finished file and checked that the two matched.
```
$ date -u
Tue Nov 10 07:13:20 UTC 2026
$ cd /tmp/d9-final; find . -type f | sort | xargs openssl dgst -sha256; cd /Volumes/Sensidine/Praxis.build
SHA2-256(./ISSUE_REGISTER.md)= 15daefbebcf54d75462c6b551bb48faa449226292d689de294096ff1f712bac4
SHA2-256(./docs/reports/2026-08-06-session42-r8j-phase3-import.md)= 63cbf06897ae72c1146ce82ee41491b7d27dd50e6b13a9969b1f043e2b436650
SHA2-256(./docs/reports/2026-08-07-f4-mffu-compliance-evidence.md)= 54422a448d326e955772b6eb89337ee56e81d7b89c677be4cfeb9c8f0aef4c02
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-adversarial.md)= 3bf5e13d14af85d10af4b2c89f3ed4ad7f4b2ed9d442807e3afcde733c0b742f
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction-worker1.md)= ced9e8d0f480e9630eece1f44dce2607c7ee98919f7ad1127f446d80dc3aee59
SHA2-256(./docs/reports/2026-08-07-session44-r8j-offset-correction.md)= 281ca1ce810af350a8c948a3d42aa339ce88fff44ddd570a868863e7b839a528
SHA2-256(./docs/reports/2026-10-28-f4-davi-reply-filing.md)= f5368c511f7ec675814c0d6b7ecce5334aa0f2c7f26c780780cec07d1efb4989
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-note.md)= 16d8b8b882fbfbf42406f34d72be9737fa2007a372366b9c3ecf046225fe8ef4
SHA2-256(./docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md)= 463188f80bd93d984eaf131f79cc8b843e223cf4d161d2ce1b08dc5ac8f63ece
SHA2-256(./docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md)= 8d97d3d6c38f0b24f6dc01e6d90ed95aad15d08c8c4ecd67a6de39152cbf3531
SHA2-256(./docs/specs/2026-08-08-ledger-compaction-spec.md)= b98698bb825c3cdf670603047b2a74f3fe4ca4627e5dcdab2cd3ad64aabc8a06
$ diff <(git show :docs/specs/2026-08-08-ledger-compaction-spec.md) /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md
111a112,113
> 
> Pointer note appended 2026-11-10 under D9 (D-2026-11-08-D): C-9's `.claude/hooks/gate-commit.sh:167-176` was written against an older gate; as of commit 23556aa the staged-tree binding it describes is at `.claude/hooks/gate-commit.sh:752-760`. Read from the gate's code at 23556aa, not trip-tested: the collision holds for a token commit made from the real index, where a changed staged diff finds no token keyed on its hash (`:678-681`) and is denied at `:778`; a temp-index commit is checked against that index's own hash and tree (`git_idx` at `:423-429`, used at `:678` and `:755`), so staging in the real index does not by itself cause a deny there. A commit on a `parked/Praxis_build-<id>` branch is allowed at `:657-662` (C2) before any token check.
$ cmp /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md docs/specs/2026-08-08-ledger-compaction-spec.md && echo identical
identical
$ grep -cF -- "$S13" docs/reports/2026-11-10-d9-housekeeping-manager.md    # S13: the standing sentence, read from line 143
1
$ grep -c '^Result:' docs/reports/2026-11-10-d9-housekeeping-manager.md; grep -n '^Result:' docs/reports/2026-11-10-d9-housekeeping-manager.md
1
145:Result: PASS
$ head -n 913 docs/reports/2026-11-10-d9-housekeeping-manager.md | openssl dgst -sha256   # lines 1-913 as Correction 1 left them (same value before this correction)
SHA2-256(stdin)= 7547899e9a72965e6b372f95b8db09f1b59e94c851d86e482a0a8761620db1e7
$ tail -n +914 docs/reports/2026-11-10-d9-housekeeping-manager.md > /tmp/d9-1b-scripts/c1b-section.txt; sed -n 334p MANIFEST.md > /tmp/d9-1b-scripts/man334.txt   # c1b-section = this section above this block
$ for f in /tmp/d9-1b-scripts/c1b-section.txt /tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md /tmp/d9-1b-scripts/man334.txt; do echo "$f $(cnt $f)"; done   # cnt = case-insensitive grep -c per variable; values never printed
/tmp/d9-1b-scripts/c1b-section.txt TERM=0 CAT=0 STEM=0 REP=0
/tmp/d9-final/docs/specs/2026-08-08-ledger-compaction-spec.md TERM=0 CAT=0 STEM=0 REP=0
/tmp/d9-1b-scripts/man334.txt TERM=0 CAT=0 STEM=0 REP=0
$ wc -l < docs/reports/2026-11-10-d9-housekeeping-manager.md
     1058
$ sed -n '334p;339p' MANIFEST.md
| /docs/specs/2026-08-08-ledger-compaction-spec.md | Spec | 0 | 2026-08-09 | Ledger-compaction spec (file first committed 2026-08-09; it had no MANIFEST row). Row added 2026-11-10 under D9: it lands as the old staged blob (+12/-2 vs HEAD) plus a dated 2-line pointer note, +14/-2 vs HEAD in all |
| /docs/reports/2026-11-10-d9-housekeeping-manager.md | Report | 2 | 2026-11-10 | Manager report for unit 2026-11-10-d9-housekeeping (Amear D-2026-11-08-D D9): per-path landing decisions for the 12 old staged paths, itemised de-identification edits, PNG exclusion, MANIFEST rows for 10 landing paths (the f4 compliance evidence already had HEAD row 132) and this report, root file F trace and removal, S4/S6 check; Correction 1 appended 2026-11-10 (S6 re-run against the gate at 23556aa, C-9 pointer note, S1 counts) |
$ git diff --cached --name-only | openssl dgst -sha256
SHA2-256(stdin)= 5bfab44568757ae2652fd4a4c7aa19844745e7995c0cdc28110c8d1165bdda95
$ git rev-parse HEAD
23556aa7999c1b0763fd746a73fba63300ea911b
```
