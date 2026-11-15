#!/bin/bash
# SubagentStop gate on praxis-manager. Deterministic. Not a judgement call.
# Blocks the return if the report contract was not honoured.
INPUT=$(cat)
DIR="${CLAUDE_PROJECT_DIR:-.}"
LATEST=$(ls -t "$DIR"/docs/reports/*.md 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
  echo "BLOCKED: no report file in docs/reports/. The report contract is not optional." >&2
  exit 2
fi

if grep -qiE '\bTBD\b' "$LATEST"; then
  echo "BLOCKED: '$LATEST' contains TBD. A row with TBD in WHY or HOW is not a valid row." >&2
  exit 2
fi

if ! grep -qi 'Verification evidence' "$LATEST"; then
  echo "BLOCKED: '$LATEST' has no Verification evidence section." >&2
  exit 2
fi

if ! grep -qiE 'Result:\s*(PASS|FAIL|BLOCKED)' "$LATEST"; then
  echo "BLOCKED: '$LATEST' has no explicit Result: PASS|FAIL|BLOCKED line." >&2
  exit 2
fi

if grep -qiE '^\s*FROZEN' "$DIR"/specs/SPEC_RUBRIC.md 2>/dev/null; then
  if ! grep -qiE 'S6|cross-block' "$LATEST"; then
    echo "BLOCKED: report does not address standing criterion S6 (cross-block check)." >&2
    exit 2
  fi
fi
exit 0
