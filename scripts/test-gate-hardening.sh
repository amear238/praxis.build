#!/bin/bash
# Verification for bead v6y gate hardening. Exercises .claude/hooks/gate-commit.sh
# DIRECTLY by piping crafted PreToolUse JSON to it (same technique as the
# 2026-07-08 install verification). All staging/committing happens in a THROWAWAY
# git repo under the session scratchpad — the real repo's index is never touched.
#
# Usage: bash scripts/test-gate-hardening.sh [scratch-dir]
# Prints PASS/FAIL per test; exits 0 only if all pass.
set -u

HOOKS_DIR=$(cd "$(dirname "$0")/../.claude/hooks" && pwd -P)
GATE="$HOOKS_DIR/gate-commit.sh"
MINT="$HOOKS_DIR/audit-approve.sh"
SCRATCH="${1:-${TMPDIR:-/tmp}/v6y-gate-test}"
SREPO="$SCRATCH/repo"
JSON='{"tool_input":{"command":"git commit -m \"test\""}}'
FAKE_PID=""
FAILS=0

cleanup() { [ -n "$FAKE_PID" ] && kill "$FAKE_PID" 2>/dev/null; }
trap cleanup EXIT

new_repo() {
  rm -rf "$SREPO"
  mkdir -p "$SREPO/.claude/state"
  ( cd "$SREPO" \
    && git init -q \
    && git config user.email test@test && git config user.name test \
    && echo base > base.txt && git add base.txt \
    && git commit -qm "base" )
  touch "$SREPO/.claude/state/orchestrator-active"
}

# run_gate -> sets RC and ERR (stderr text)
run_gate() {
  ERR=$(printf '%s' "$JSON" | CLAUDE_PROJECT_DIR="$SREPO" bash "$GATE" 2>&1 >/dev/null)
  RC=$?
}

mint() { ( cd "$SREPO" && CLAUDE_PROJECT_DIR="$SREPO" bash "$MINT" test-bead >/dev/null ); }

verdict() { # verdict <name> <want_rc> <got_rc> [required-stderr-substring]
  local name=$1 want=$2 got=$3 substr=${4:-}
  if [ "$got" = "$want" ] && { [ -z "$substr" ] || printf '%s' "$ERR" | grep -q "$substr"; }; then
    echo "PASS  $name (exit $got)"
  else
    echo "FAIL  $name (want exit $want${substr:+ + msg '$substr'}, got exit $got; stderr: $ERR)"
    FAILS=$((FAILS + 1))
  fi
}

echo "== v6y gate hardening tests (scratch repo: $SREPO) =="

# A. valid token + unchanged staged tree -> allow
new_repo
( cd "$SREPO" && echo a1 > a.txt && git add a.txt )
mint
run_gate
verdict "A: valid token, unchanged staged tree -> allow" 0 "$RC"

# E (part 1, continues A's repo): allow consumed the token; commit; token gone; replay denied
TOKENS=$(ls "$SREPO/.claude/state"/audit-pass-* 2>/dev/null | wc -l | tr -d ' ')
( cd "$SREPO" && git commit -qm "gated commit" )
if [ "$TOKENS" = "0" ]; then TOKGONE=0; else TOKGONE=1; fi
run_gate  # replay the same commit
if [ "$TOKGONE" = "0" ] && [ "$RC" = "2" ]; then
  echo "PASS  E: token consumed after gated commit; replay -> deny (exit $RC)"
else
  echo "FAIL  E: token files remaining=$TOKENS, replay exit=$RC (want 0 files, exit 2)"
  FAILS=$((FAILS + 1))
fi

# B. valid token, then stage an EXTRA file -> deny
new_repo
( cd "$SREPO" && echo b1 > b.txt && git add b.txt )
mint
( cd "$SREPO" && echo extra > extra.txt && git add extra.txt )
run_gate
verdict "B: extra file staged after mint -> deny" 2 "$RC" "denied"

# C. valid token, then MODIFY an already-staged file -> deny
new_repo
( cd "$SREPO" && echo c1 > c.txt && git add c.txt )
mint
( cd "$SREPO" && echo c2-tampered > c.txt && git add c.txt )
run_gate
verdict "C: staged file modified after mint -> deny" 2 "$RC" "denied"

# D. no token -> deny  [regression]
new_repo
( cd "$SREPO" && echo d1 > d.txt && git add d.txt )
run_gate
verdict "D: no token -> deny" 2 "$RC" "no audit PASS token"

# G (bonus). legacy empty token + matching PASS row -> deny via tree binding
new_repo
( cd "$SREPO" && echo g1 > g.txt && git add g.txt )
HASH=$(cd "$SREPO" && git diff --cached | shasum -a 256 | awk '{print $1}')
touch "$SREPO/.claude/state/audit-pass-$HASH"          # old-format token: no tree=
echo "2026-07-10T00:00:00Z legacy $HASH PASS" >> "$SREPO/AUDIT_LOG.md"
run_gate
verdict "G: legacy tree-less token -> deny (tree binding)" 2 "$RC" "staged tree no longer matches"

# F. simulated second claude process cwd'd into the repo -> deny
# Spawn `exec -a claude sleep` via a throwaway parent so the fake is reparented
# to pid 1 — i.e. NOT a descendant of this session's claude, matching how the
# gate distinguishes foreign sessions (ancestry walk to our own claude pid).
# stdout/stderr must be detached and the pid passed via file, not a $() pipe —
# an inherited substitution pipe kills the fake when the parent exits.
new_repo
( cd "$SREPO" && echo f1 > f.txt && git add f.txt )
mint
bash -c "cd '$SREPO' && { exec -a claude sleep 30 >/dev/null 2>&1 & echo \$! > '$SCRATCH/fake.pid'; }"
FAKE_PID=$(cat "$SCRATCH/fake.pid")
sleep 1  # let reparenting settle
run_gate
verdict "F: second live claude cwd'd in repo -> deny" 2 "$RC" "another live claude session"
kill "$FAKE_PID" 2>/dev/null; FAKE_PID=""

# F sanity inverse: with the fake gone, the untouched token still allows
sleep 1
run_gate
verdict "F2: fake session gone, token intact -> allow" 0 "$RC"

# H. no-weakening regressions: unarmed repo unaffected; non-commit passthrough;
#    -a-style form still denied before any token/session work
new_repo
rm -f "$SREPO/.claude/state/orchestrator-active"
( cd "$SREPO" && echo h1 > h.txt && git add h.txt )
run_gate
verdict "H1: unarmed repo (no orchestrator-active) -> allow" 0 "$RC"
touch "$SREPO/.claude/state/orchestrator-active"
SAVE_JSON=$JSON
JSON='{"tool_input":{"command":"git status"}}'
run_gate
verdict "H2: non-commit command passthrough -> allow" 0 "$RC"
JSON='{"tool_input":{"command":"git commit -am \"sweep\""}}'
run_gate
verdict "H3: -am form -> deny (form check intact)" 2 "$RC" "short flag sweeps"
JSON=$SAVE_JSON

echo
if [ "$FAILS" = "0" ]; then
  echo "ALL TESTS PASS"
  exit 0
else
  echo "$FAILS TEST(S) FAILED"
  exit 1
fi
