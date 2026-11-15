#!/bin/bash
# Subagents never commit. Only the main-thread master commits, after the auditor passes.
INPUT=$(cat)
# Discriminator (rewritten 2026-07-25 from live PreToolUse payloads, CC 2.1.220).
# Three observed shapes on the Bash matcher:
#   plain session main thread   -> agent_id ABSENT, agent_type ABSENT
#   `--agent praxis-master`     -> agent_id ABSENT, agent_type "praxis-master"
#   praxis-manager subagent     -> agent_id PRESENT, agent_type "praxis-manager"
# agent_type is the reliable role field: present for every stack context, absent
# for ordinary non-stack sessions (which stay under .claude/hooks/gate-commit.sh).
# agent_id is retained only to distinguish the MAIN-THREAD master from a master
# spawned as a subagent — the intent is that only the main thread may commit.
AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT")
# No agent_type at all -> ordinary session, not the agent stack. Untouched.
[ -z "$AGENT" ] && exit 0
# The main-thread master is the only committer in the stack.
[ "$AGENT" = "praxis-master" ] && [ -z "$AGENT_ID" ] && exit 0
CMD=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
if echo "$CMD" | grep -qE '\bgit\s+(commit|push|merge|rebase|tag)\b'; then
  echo "BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes." >&2
  exit 2
fi
exit 0
