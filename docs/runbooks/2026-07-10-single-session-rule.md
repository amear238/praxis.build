# Runbook: Single Claude Session Per Repo Working Tree (2026-07-10)

## The incident (3 lines)
On 2026-07-10 a second, parallel Claude session staged 7 unrelated files into this repo's shared `.git/index` in the gap between audit-token mint and `git commit`.
The tip commit recorded the wrong file set under an audited commit message, and the drift left orphaned (never-consumed) audit tokens in `.claude/state/`.
Root cause: the commit gate bound the token to the staged *diff text* at mint time only, and nothing stopped two sessions from sharing one index.

## The rule
**Run exactly ONE Claude session per repo working tree.** If parallel work is genuinely needed, give each extra session its own `git worktree` (own index, own checkout):

```bash
git worktree add ../Praxis.build-wt-<task> main   # per parallel session
git worktree remove ../Praxis.build-wt-<task>     # when done
```

Never point a second session's cwd at `/Volumes/Sensidine/Praxis.build` while another session is live.

## Enforcement now in place (bead v6y, `.claude/hooks/gate-commit.sh` + `audit-approve.sh`)
1. **Staged-tree binding** — `audit-approve.sh` records `tree=$(git write-tree)` inside the token; the gate recomputes `git write-tree` at commit time and denies on any mismatch (extra paths, missing paths, content changes). Legacy tree-less tokens are denied and deleted.
2. **Single-session check** — the gate scans `lsof -a -d cwd` for any live `claude` process (identified by `ps` argv[0], not lsof's truncated names) whose cwd is inside this repo and which is not part of this session's own process tree (ancestry walk to our own claude pid). Match → deny, without consuming the token. Check errors fail CLOSED (deny); close the other session and rerun.
3. **Single-use + orphan sweep** — the matched token is deleted at allow time (before the commit runs) so it can never be replayed; tokens older than 30 min are swept even if their hash never matches again.

## If the gate denies you
- "another live claude session (pid ...)": close that session (or move it to a worktree), rerun the commit — the token was NOT consumed.
- "staged tree no longer matches": the index was touched after mint. Re-stage exactly the audited set and re-dispatch the orchestrator-auditor for a fresh token.
- Verification suite: `bash scripts/test-gate-hardening.sh` (throwaway repo, never touches the real index).
