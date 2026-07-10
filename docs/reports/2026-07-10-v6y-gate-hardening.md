# Report: Praxis_build-v6y — Commit-Gate Hardening (2026-07-10)

Implementer report. P1 bug: parallel Claude session polluted the shared `.git/index` between audit-token mint and `git commit`; the tip write recorded the wrong file set under the audited message.

## The actual pre-existing gap (verified against the scripts at HEAD f0da783)

**1. Token bound to diff text only, checked only at hook time.** `gate-commit.sh` (old lines 53–55, 68–69):

```bash
HASH=$(cd "$ROOT" && git diff --cached | shasum -a 256 | awk '{print $1}')
TOKEN="$STATE/audit-pass-$HASH"
if [ -f "$TOKEN" ]; then
  ...
  rm -f "$TOKEN"   # single-use
  exit 0
fi
```

and `audit-approve.sh` (old line 18) minted a **contentless** token:

```bash
touch "$STATE/audit-pass-$HASH"
```

The hash is over `git diff --cached` **text relative to current HEAD**. That leaves two holes: (a) the hook allows, exits, and only THEN does the Bash tool execute `git commit` — anything a parallel session stages in that window is committed unaudited (the incident); (b) if HEAD moves between mint and commit, the diff text (and hash) shifts even when the index content is unrelated to what was audited. Nothing recorded or re-verified the actual **tree** being committed, and nothing anywhere enforced session exclusivity over the shared index.

**2. Token consumption gap — verified.** The `rm -f "$TOKEN"` on line 68 only fires when the commit-time hash EQUALS the mint-time hash. When the staged diff drifts (exactly the incident mode), the old token's filename never matches again and it lingers forever; even the 30-min expiry (old lines 58–62) only deleted the token it had already matched. Evidence in the repo: AUDIT_LOG.md rows 27–28 show PASS mints `c072de2…` (Praxis_build-22r, 15:08Z) and `7473a63…` (session-5-wrap, 15:16Z) whose token files still sat in `.claude/state/` after commits 1c53a18 and f0da783 landed, while the sibling 22r token `19927e8…` (15:00Z) was consumed normally. So consumption worked only on the exact-match path; drift-orphaned tokens were never cleaned. (Note: consumption happens at PreToolUse allow time — before the commit executes — which is the only reliable hook point and is strictly stronger than post-commit deletion: a second commit can never reuse the token.)

## Changes

### `.claude/hooks/gate-commit.sh`
- **Staged-tree binding**: after the existing freshness + AUDIT_LOG PASS checks, reads `tree=<id>` from the token and compares it to a fresh `git write-tree`. Any mismatch (extra paths, missing paths, content changes, unresolvable tree, or a legacy/forged token with no `tree=` line) → `rm -f` token + deny (exit 2) with an explicit message. Deterministic identifier chosen: `git write-tree` (the exact tree `git commit` would record), complementing the existing diff-text sha256 which still keys the token filename.
- **Single-session check** (new, after the form checks, BEFORE token lookup so a denial never consumes the token): enumerates `lsof -a -d cwd -Fpn` over all processes (lsof `-c claude` is unreliable — observed truncated names `claude.ex` and `2.1.206` for real sessions), keeps pids whose cwd is the repo root or below, excludes this session's own tree (PPID walk from `$$` finds our claude ancestor; candidates are excluded iff their ancestry reaches that pid), and flags any remainder whose `ps -o command=` argv[0] basename starts with `claude`. Foreign match → deny. lsof yielding no data, or unresolvable repo root → deny (fail CLOSED).
- **Orphaned-token sweep**: `find "$STATE" -name 'audit-pass-*' -mmin +30 -exec rm -f {} +` before token lookup, so drift-orphaned tokens can no longer accumulate.
- Everything else intact: armed-marker scoping (`orchestrator-active`), broad `*git*commit*` match, `-a`/`--all`/`--include`/`--amend`/pathspec/`git add`/double-commit form denials, 30-min freshness, AUDIT_LOG PASS-row requirement, allow-time consumption.

### `.claude/hooks/audit-approve.sh`
- Mints the token with content `tree=$(git write-tree)` instead of `touch`; refuses to mint if `write-tree` fails. Hash/AUDIT_LOG row format unchanged.

### New files
- `scripts/test-gate-hardening.sh` — verification suite below; throwaway repo under the session scratchpad, never touches the real index.
- `docs/runbooks/2026-07-10-single-session-rule.md` — single-session mandate, incident in 3 lines, enforcement summary, recovery steps.
- `CLAUDE.md` — new `## Do Not` line: no multiple Claude sessions against this working tree.
- `MANIFEST.md` — hooks row bumped to v2 + 3 new rows.

### Stale-token removal
Deleted the two already-consumed-in-spirit orphan tokens as part of this change (their commits 1c53a18 / f0da783 had already landed):
- `.claude/state/audit-pass-c072de2ce28f25064ef6c08479bee5889fae1efb516d054bd8a894e29dbdc436`
- `.claude/state/audit-pass-7473a63456b1eb461c6a8997b552b0bd1132324937945238b7d9392d87467337`

`.claude/state/` afterward contains only: `current-bead`, `iteration-count`, `max-iterations`, `orchestrator-active`, `run-mode` (all untracked state; no staging needed).

## Verification (full output, re-runnable by the auditor)

`bash scripts/test-gate-hardening.sh` (JSON piped directly into the hook, same technique as the 2026-07-08 install verification; A–F required by the bead, G/F2/H1–H3 added regressions):

```
== v6y gate hardening tests (scratch repo: /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/f2df5604-68eb-4a53-b74a-e80295d13719/scratchpad/v6y-gate-test/repo) ==
PASS  A: valid token, unchanged staged tree -> allow (exit 0)
PASS  E: token consumed after gated commit; replay -> deny (exit 2)
PASS  B: extra file staged after mint -> deny (exit 2)
PASS  C: staged file modified after mint -> deny (exit 2)
PASS  D: no token -> deny (exit 2)
PASS  G: legacy tree-less token -> deny (tree binding) (exit 2)
PASS  F: second live claude cwd'd in repo -> deny (exit 2)
PASS  F2: fake session gone, token intact -> allow (exit 0)
PASS  H1: unarmed repo (no orchestrator-active) -> allow (exit 0)
PASS  H2: non-commit command passthrough -> allow (exit 0)
PASS  H3: -am form -> deny (form check intact) (exit 2)

ALL TESTS PASS
```

Test F spawns `bash -c "cd <repo> && { exec -a claude sleep 30 >/dev/null 2>&1 & ... }"` so the fake is reparented to pid 1 (outside our session's process tree) and shows argv[0] `claude` — matching the implemented mechanism exactly. Live incidental confirmation: while probing, one of this session's own Bash calls containing an embedded `git commit -am` string was denied by the real armed hook at the form-check stage, proving the deployed gate is active and that form denials still run before any token/session work.

## Residual risk (for the auditor)
- The hook-allow → commit-execute window still exists in principle; it is now closed in practice by the single-session check (no other live claude can touch the index in the gap). Non-claude processes mutating the index are out of scope per the bead.
- The session check sees only processes lsof can enumerate for this user; enforcement is in-session by design — the runbook covers the human side.
