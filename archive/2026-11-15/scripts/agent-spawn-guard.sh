#!/bin/bash
# Enforces the PRAXIS spawn hierarchy on the Agent tool.
#
# Frontmatter cannot do this. Established by live experiment (CC 2.1.220):
# a subagent's own `tools: Agent(...)` allowlist is SILENTLY IGNORED when that
# agent is spawned as a child -- it inherits the PARENT's spawnable roster.
# The same allowlist IS enforced when the agent runs as the main thread.
# Consequence: praxis-manager spawned by praxis-master can reach praxis-auditor,
# which the producer/grader separation forbids. Only a PreToolUse hook can stop it.
#
# Payload shape observed live on the Agent matcher (2026-07-26, CC 2.1.220):
#   tool_name                 -> "Agent"
#   .agent_type               -> the CALLER's agent type ("praxis-master" main
#                                thread: agent_id ABSENT; "praxis-manager"
#                                subagent: agent_id PRESENT)
#   .tool_input.subagent_type -> the TARGET agent type being spawned
#
# FAIL SAFE: exit 0 on anything not positively identified as a forbidden spawn.
INPUT=$(cat)

# Not the Agent tool -> not our business.
TOOL=$(jq -r '.tool_name // ""' <<<"$INPUT" 2>/dev/null)
[ "$TOOL" = "Agent" ] || exit 0

CALLER=$(jq -r '.agent_type // ""' <<<"$INPUT" 2>/dev/null)
TARGET=$(jq -r '.tool_input.subagent_type // ""' <<<"$INPUT" 2>/dev/null)

# Caller not identifiable, or no target -> allow.
[ -z "$CALLER" ] && exit 0
[ -z "$TARGET" ] && exit 0

# The worker is the terminal layer. `disallowedTools: Agent` is its own control;
# this is the second, independent mechanism -- deliberately not a single point.
if [ "$CALLER" = "praxis-worker" ]; then
  echo "BLOCKED: praxis-worker is the terminal layer and may not spawn." >&2
  exit 2
fi

# Producer/grader separation: the manager produces, the auditor grades.
# The manager must never be able to pick or brief its own grader.
if [ "$CALLER" = "praxis-manager" ] && [ "$TARGET" = "praxis-auditor" ]; then
  echo "BLOCKED: praxis-manager may not spawn the auditor. The master spawns praxis-auditor independently." >&2
  exit 2
fi

exit 0
