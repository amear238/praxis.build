# Bead 587 — gate-commit.sh form matcher: command-position anchoring

Date: 2026-07-12
Bead: Praxis_build-587 (bug filed session 6, two live false denials)
Files: `.claude/hooks/gate-commit.sh`, `scripts/test-gate-hardening.sh`, `MANIFEST.md`

## What was wrong

After the v6y hardening (fec1722), the gate's entry matcher was a bare substring
glob over the whole Bash command string:

```sh
case "$CMD" in
  *git*commit*) ;;
  *) exit 0 ;;
esac
```

Any command whose text contained `git` anywhere followed later by `commit`
anywhere fell through into the full gate pipeline. While armed, a command like
`bd close 587 --reason="fixed the git commit gate"` reached the token lookup,
found no token (there is none for such a command), and was DENIED with
"no audit PASS token" — a false positive on quoted free text that merely
*mentions* the words. This happened live twice in session 6. Fail direction was
closed (nuisance, not a bypass), but it blocked routine bead bookkeeping.

## The fix (new anchoring approach)

The glob is kept as a cheap pre-filter only. A precise matcher now runs right
after it, in two steps:

1. **Quote stripping.** Single- and double-quoted regions are removed from the
   command string (`sed "s/'[^']*'//g; s/\"[^\"]*\"//g"`) so free text inside
   arguments can never anchor a match — including free text containing
   separators like `;` or `(`. An unbalanced leftover quote merely over-matches
   (fail closed).
2. **Command-position regex** over the stripped string. `git ... commit` gates
   only when `git` sits in command position — start of string/line, or
   immediately after a separator (`;`, `&`/`&&`, `|`/`||`, subshell `(` which
   also covers `$(`, backtick) — optionally behind `VAR=...` assignments and/or
   one common wrapper word (`command|builtin|exec|env|sudo|nohup|nice|time|xargs`
   with optional args), and with the binary itself allowed in path form
   (`/usr/bin/git`, `../bin/git` — any non-separator run ending in `/`) or
   backslash-escaped (`\git`), composing with the VAR=/wrapper prefixes.
   `commit` must be a whole word after `git` within the same command segment,
   so `git -C <dir> commit` still gates while `git diff gate-commit.sh` does
   not.

**No-weakening escape hatch:** a nested-shell/eval invocation in command
position (`sh|bash|zsh|dash|ksh|eval`) whose raw command text matched the
`*git*commit*` pre-filter keeps the old broad gating — nested `-c '...'` command
strings are not introspected; they deny by default. Without this,
`bash -c 'git commit -m x'` would have been un-gated by quote stripping.

Everything downstream is untouched: `-a`/`--all`/`--include`/`--amend` form
denials, pathspec-after-`--` denial, one-commit-per-call, single-session lsof
check, token freshness/AUDIT_LOG/tree-binding verification, single-use token
consumption. The fix narrows only WHERE the pattern may match, never WHAT is
gated.

## Audit round (coordinator FAIL, 4 defects — all fixed)

The first version anchored on the literal token `git`, which WEAKENED the gate:
`/usr/bin/git commit`, `cd /tmp && /usr/bin/git commit`, `\git commit`, and
`GIT_DIR=.git /usr/bin/git commit` all exited 0 while armed (the old broad glob
had caught them). Fix: a `BINPRE` prefix `(\\|[^[:space:];&|` +backtick+ `]*/)?`
now precedes the binary name in both the GITCOMMIT and NESTSHELL patterns —
optional backslash escape or any path ending in `/` — and, because it sits
inside the existing `ANCHOR+PRE+...` sequence, it composes with `VAR=...`
assignments and wrapper words (defect 3). Regression tests J8–J11 (armed DENY)
and I5 (quoted free-text mention of a path form still allows) were added
TDD-first: J8–J11 red (exit 0) against the defective anchor, all green after.

## TDD order

Regression tests (I/J series) were written first and run against the unfixed
hook: I1–I3 FAILED (exit 2, "no audit PASS token") exactly reproducing the
session-6 incidents; I4 passed (unarmed path exits before token lookup); all
J-series no-weakening tests passed. The matcher was then fixed and the full
suite rerun. The audit-round defects were likewise reproduced red-first
(J8–J11) before the BINPRE fix.

## Test matrix (after fix — `bash scripts/test-gate-hardening.sh`, exit 0)

| Test | Description | Result |
|---|---|---|
| A | valid token, unchanged staged tree -> allow | PASS |
| E | token consumed after gated commit; replay -> deny | PASS |
| B | extra file staged after mint -> deny | PASS |
| C | staged file modified after mint -> deny | PASS |
| D | no token -> deny (plain tip-write form, armed) | PASS |
| G | legacy tree-less token -> deny (tree binding) | PASS |
| F | second live claude cwd'd in repo -> deny | PASS |
| F2 | fake session gone, token intact -> allow | PASS |
| H1 | unarmed repo -> allow | PASS |
| H2 | non-commit command passthrough -> allow | PASS |
| H3 | -am form -> deny (form check intact) | PASS |
| I1 (new) | armed, `bd close` w/ quoted vcs words in reason -> allow | PASS |
| I2 (new) | armed, `echo` w/ quoted words + separators inside quotes -> allow | PASS |
| I3 (new) | armed, `bd create` w/ single-quoted words -> allow | PASS |
| I4 (new) | unarmed, `bd close` w/ quoted words -> allow | PASS |
| I5 (new, audit round) | armed, `echo` w/ quoted `/usr/bin/git commit` mention -> allow | PASS |
| J1 (new) | chained after `&&` -> deny | PASS |
| J2 (new) | chained after `;` -> deny | PASS |
| J3 (new) | piped form -> deny | PASS |
| J4 (new) | subshell form -> deny | PASS |
| J5 (new) | `git -C <dir> commit` -> deny | PASS |
| J6 (new) | `VAR=...` assignment prefix -> deny | PASS |
| J7 (new) | nested shell `-c` string -> deny (fail closed) | PASS |
| J8 (new, audit round) | `/usr/bin/git commit` absolute-path form -> deny | PASS |
| J9 (new, audit round) | `cd /tmp && /usr/bin/git commit` chained path form -> deny | PASS |
| J10 (new, audit round) | `\git commit` backslash-escaped form -> deny | PASS |
| J11 (new, audit round) | `GIT_DIR=.git /usr/bin/git commit` VAR= + path form -> deny | PASS |

27/27 PASS (11 pre-existing + 16 new). TDD red runs: 19/22 first round (I1–I3
red), 23/27 audit round (J8–J11 red against the literal-`git` anchor).

Acceptance-criteria coverage: (1) command-position anchoring — matcher rewrite +
I-series; (2a) I1–I5; (2b) D + J1–J6 (J7–J11 no-weakening incl. audit-round
bypass class); (3) A–H3 all green.

## Files touched

- `/Volumes/Sensidine/Praxis.build/.claude/hooks/gate-commit.sh` — precise
  matcher block added after the glob pre-filter; header comment updated.
- `/Volumes/Sensidine/Praxis.build/scripts/test-gate-hardening.sh` — I1–I4 and
  J1–J7 regression tests; header comment updated.
- `/Volumes/Sensidine/Praxis.build/MANIFEST.md` — rows for both files bumped
  (v3 hooks / v2 test script) + row for this report.
- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-12-587-gate-form-check-fix.md`
  — this report.

Staged, not committed, per dispatch constraints. No `.claude/state/*` touched;
all hook exercising was done via simulated PreToolUse stdin against a throwaway
scratch repo.
