# Praxis_build-30h — AUDIT_LOG flush path (P2 bug)

Date: 2026-07-10 · Implementer report · Base: fec1722 (main)

## Root cause recap
`.claude/hooks/audit-approve.sh` computes the staged-diff hash (line 17) and the
staged-tree binding (`git write-tree`, line 21) BEFORE appending the PASS row to
`AUDIT_LOG.md` (line 27). The row therefore always postdates the audited
snapshot: a commit can never contain its own audit row, and staging a prior row
into the next feature commit is smuggled self-approval (auditor-rejected).
All rows after `2026-07-09T14:20:09Z` (16 rows through `16:21:33Z v6y`) were
stranded uncommitted. Additionally, row `2026-07-10T15:00:22Z Praxis_build-22r
19927e89…` was minted against wrong staged content during the concurrency
incident and declared VOID (DECISION_LOG 2026-07-10T15:20Z halt / 15:35Z
resolution). Resolution pre-decided (RUN_DECISIONS option a): dedicated flush
commit type + auditor FLUSH-MODE; the flush's own mint row rolls forward
perpetually (accepted).

## Deliverables
1. **`scripts/audit-log-flush-verify.sh`** — machine half of FLUSH-MODE.
   Enforces staged set == exactly `AUDIT_LOG.md` and an append-only diff, then
   classifies every added line (first match wins): `VOID-ANNOTATED` (covered by
   an ANNOTATION VOID line) → `SUPERSEDED` (later PASS row, same bead — benign
   unconsumed re-mint) → `LANDED` (commit citing the bead id, or any
   wrap-message commit for `session-*-wrap` rows, authored at/after the mint
   timestamp) → `LANDED-WRAP` (no citing commit, but the FIRST commit after the
   mint is a wrap commit within the 30-min token TTL — the wrap consumed a
   token minted under the bead it closed; real case: 3i7 mint 15:40:27Z →
   session-2 wrap b64aa62 at 15:40:41Z) → `ANNOTATION` (the line is itself an
   annotation referencing a real PASS row). Any unclassifiable line is quoted
   and the script exits 1; exit 0 only when all classify. Per-row table printed.
2. **`scripts/audit-log-annotate.sh`** — the only sanctioned non-audit-approve
   writer. Appends exactly one `<utc-ts> ANNOTATION VOID <hash-prefix> <reason>`
   line. Refuses: any verb but VOID, missing/multi-line/non-ASCII reasons,
   reasons embedding a 64-hex digest (PASS-row/token forgery vector), prefixes
   not matching exactly one PASS row, duplicate annotation of the same row.
3. **`.claude/agents/orchestrator-auditor.md`** — FLUSH-MODE section (staged
   set exactly AUDIT_LOG.md; run flush-verify, exit 0 required; 2+ independent
   row spot-checks against history; DECISION_LOG existence check for VOID rows;
   mint normally; rolling row accepted). Outside flush mode: staged
   AUDIT_LOG.md = automatic FAIL, encoded in procedure step 3.
4. **`docs/runbooks/2026-07-10-audit-log-flush.md`** — strand problem, flush
   procedure, VOID annotation usage, perpetual rolling row. MANIFEST updated.

## Annotation line added (real repo, working tree, UNSTAGED)
```
2026-07-10T16:34:02Z ANNOTATION VOID 19927e89 minted against wrong staged content during the 2026-07-10 concurrency incident; declared VOID by DECISION_LOG 2026-07-10T15:20Z (halt) and 2026-07-10T15:35Z (resolution); superseding 22r mint 2026-07-10T15:08:29Z landed as 1c53a18
```

## Verify (scratch clone under session scratchpad; real index never touched)
Setup: `git clone --no-hardlinks <repo> scratchpad/30h/repo`, copied the real
working-tree AUDIT_LOG.md in, staged it THERE only.

### Positive — all 17 added lines classified, exit 0
```
#   MINTED(UTC)           BEAD/KIND                  HASH      CLASS           EVIDENCE
1   2026-07-09T14:31:54Z  Praxis_build-3i7           229777e6  SUPERSEDED      re-mint @ 2026-07-09T15:35:00Z
2   2026-07-09T14:47:41Z  Praxis_build-dgt.1         e65d4dd6  LANDED          commit 4680386 @ 2026-07-09T14:47:59Z
3   2026-07-09T15:35:00Z  Praxis_build-3i7           eb7ca337  SUPERSEDED      re-mint @ 2026-07-09T15:40:27Z
4   2026-07-09T15:40:27Z  Praxis_build-3i7           5344b4ac  LANDED-WRAP     wrap commit b64aa62 @ 2026-07-09T15:40:41Z consumed mint (+14s)
5   2026-07-09T17:54:47Z  Praxis_build-dnt           d2e403d4  LANDED          commit dc5216c @ 2026-07-09T17:55:23Z
6   2026-07-09T19:59:15Z  session-3-wrap             1e984375  LANDED          commit f716d2d @ 2026-07-09T19:59:38Z
7   2026-07-09T20:29:15Z  Praxis_build-p7s           6b1b2ccc  LANDED          commit b5e022e @ 2026-07-09T20:29:35Z
8   2026-07-10T13:28:40Z  Praxis_build-4hd           adc9044a  LANDED          commit 7420ae5 @ 2026-07-10T13:28:55Z
9   2026-07-10T14:07:11Z  Praxis_build-3m8           62fc8782  LANDED          commit c19531b @ 2026-07-10T14:07:25Z
10  2026-07-10T14:17:57Z  Praxis_build-4wk           89213871  LANDED          commit d24537c @ 2026-07-10T14:18:18Z
11  2026-07-10T14:27:52Z  Praxis_build-63b           9433c408  LANDED          commit 5822420 @ 2026-07-10T14:28:07Z
12  2026-07-10T15:00:22Z  Praxis_build-22r           19927e89  VOID-ANNOTATED  annotation @ 2026-07-10T16:34:02Z
13  2026-07-10T15:05:24Z  Praxis_build-jpe           297c68d4  LANDED          commit e76f5c6 @ 2026-07-10T15:05:49Z
14  2026-07-10T15:08:29Z  Praxis_build-22r           c072de2c  LANDED          commit 1c53a18 @ 2026-07-10T15:08:40Z
15  2026-07-10T15:16:11Z  session-5-wrap             7473a634  LANDED          commit f0da783 @ 2026-07-10T15:18:11Z
16  2026-07-10T16:21:33Z  Praxis_build-v6y           4d289e13  LANDED          commit fec1722 @ 2026-07-10T16:21:54Z
17  2026-07-10T16:34:02Z  ANNOTATION                 -         ANNOTATION      covers PASS row 19927e89

FLUSH-VERIFY PASS: all 17 added line(s) classified — safe to audit as a flush commit
exit=0
```

### Negative — fabricated row for nonexistent bead, exit 1 naming it
```
18  2026-07-10T16:40:00Z  Praxis_build-fk9           a1ee359c  UNCLASSIFIED    no citing commit at/after mint, no later re-mint, no VOID annotation
FLUSH-VERIFY FAIL: 1 of 18 added line(s) UNCLASSIFIED:
  line 18: 2026-07-10T16:40:00Z Praxis_build-fk9 a1ee359c0386467e49d6a27b3cc2f69aef80b26ad942c54a94d00a2a7f74cf8b PASS
    -> no citing commit at/after mint, no later re-mint, no VOID annotation
negative-test exit=1
```

### Shape guard — extra staged file, exit 1
```
FLUSH-VERIFY FAIL: flush staged set must be EXACTLY AUDIT_LOG.md; got: AUDIT_LOG.md extra-file.txt
shape-guard exit=1
```

### Annotation guard — 5 misuse attempts, all refused (exit 1), log untouched
```
G1 non-VOID verb:      annotate REFUSED: only the VOID verb is sanctioned (got 'EDIT') — a new verb needs its own bead + auditor sign-off
G2 newline in reason:  annotate REFUSED: reason must be a single line — an embedded newline could forge additional log rows
G3 nonexistent prefix: annotate REFUSED: row-hash-prefix must match exactly ONE PASS row in AUDIT_LOG.md (matched 0)
G4 duplicate VOID:     annotate REFUSED: row 19927e89b820... already carries a VOID annotation (append-only — no re-edits, no retractions)
G5 64-hex in reason:   annotate REFUSED: reason may not embed a full 64-hex digest — it could collide with token/PASS-row matching
```

## Notes for the auditor
- Row 4 needs the LANDED-WRAP rule: no commit cites 3i7 at/after 15:40:27Z; the
  session-2 wrap commit b64aa62 (authored +14s, body: "AUDIT_LOG rolling rows
  left uncommitted by design pending bug 30h") consumed that mint. The rule is
  deliberately narrow: first-commit-after-mint, wrap message, ≤30-min TTL.
- Classification precedence VOID → SUPERSEDED → LANDED → LANDED-WRAP; exactly
  one class per line, machine-deterministic.
- AUDIT_LOG.md and DECISION_LOG.md remain modified/UNSTAGED in the real repo by
  design; the flush itself is a separate follow-up commit run by the orchestrator.
