# Runbook: AUDIT_LOG flush commits (bead 30h, 2026-07-10)

## The strand problem
`audit-approve.sh` appends its PASS row AFTER hashing (`git diff --cached`) and
tree-binding (`git write-tree`) the staged diff — so a commit can never contain
its own audit row, and folding a prior row into the next feature commit was
rejected as smuggled self-approval. Result: every PASS row strands uncommitted
in the working tree. Resolution (RUN_DECISIONS 2026-07-09 option a): a dedicated
**flush commit** that stages AUDIT_LOG.md ALONE, graded by the auditor in
FLUSH-MODE with machine verification that each added row maps to a real,
already-landed audited commit.

## Flush procedure (orchestrator)
1. Confirm single-writer (no other claude session cwd'd in this repo).
2. Stage the log alone, by explicit pathspec: `git add AUDIT_LOG.md` — nothing else.
3. Optional pre-check: `bash scripts/audit-log-flush-verify.sh` (auditor re-runs it anyway).
4. Dispatch orchestrator-auditor with the words **"flush mode"** + the flush bead id.
   It requires: staged set exactly AUDIT_LOG.md, append-only diff, flush-verify
   exit 0, 2+ independent row spot-checks — then mints normally.
5. Plain `git commit -m "<bead>: audit-trail flush (N rows through <last-ts>)"`.

## VOID annotations
AUDIT_LOG.md is written ONLY by `audit-approve.sh` — plus exactly one other
sanctioned writer: `scripts/audit-log-annotate.sh`. It APPENDS (never edits)
one line: `<utc-ts> ANNOTATION VOID <row-hash-prefix> <reason citing DECISION_LOG>`.
Use it when a mint is declared void (e.g. row 19927e89…, minted against wrong
staged content in the 2026-07-10 concurrency incident). Flush verification then
classifies the covered row VOID-ANNOTATED instead of demanding a landed commit.
The script refuses non-VOID verbs, multi-line/forged reasons, ambiguous
prefixes, and duplicate annotations. Never hand-edit the log.

## The perpetual rolling row
Minting the flush's own token appends a NEW row to the working tree after the
staged snapshot. That single row always strands and lands in the NEXT flush.
This is accepted by design — expect AUDIT_LOG.md to show exactly one modified
(unstaged) row immediately after every flush commit. Do not "fix" it.
