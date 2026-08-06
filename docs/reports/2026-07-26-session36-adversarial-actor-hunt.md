# Session 36 — Adversarial actor hunt: master-bash-guard reachability from a subagent

## Task
Attack the claim that the `BLOCKED: shell write from praxis-master.` string emitted by
`scripts/master-bash-guard.sh` cannot be produced from inside a spawned subagent.

## Mode
ADVERSARIAL.

## Criterion
`specs/SPEC_RUBRIC.md` S9 — "Any config field a guarantee depends on is positive-controlled:
confirm a visible script fires at that field, then confirm an invented key at the same position
produces byte-identical silence."

## Claim under attack
"From inside a spawned subagent, there exists no way to cause that BLOCKED string to be emitted,
because every subagent's PreToolUse payload carries a non-empty `.agent_id`. Therefore the S9
positive control cannot be run from a subagent."

---

## 1. Attacks attempted (verbatim commands and complete output)

Runner identity: this report was produced by a `praxis-worker` subagent of session
`2488feec-6500-4e04-b743-262c306cfabb` (env `CLAUDE_CODE_CHILD_SESSION=1`, `CLAUDE_CODE_VERSION=2.1.220 (Claude Code)`,
`which -a claude` -> `/Users/admin/.local/bin/claude` twice, same path). Every command below was
issued as a Bash tool call from inside that subagent.

Guard script identity (the file every attack below actually executed):

```
$ ls -li /Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh; shasum -a 256 /Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh
33619 -rwx--x--x@ 1 admin  staff  850 Jul 25 16:45 /Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh
2dd67afcaefb84136a460d02cb7380acaf64c4f6bcce181f9850c02dfbb63101  /Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh
```

### Attack A — plain shell redirect from this subagent (baseline)

```
$ echo probeA > /private/tmp/.../scratchpad/probeA.txt; cat /private/tmp/.../scratchpad/probeA.txt
probeA
```

No BLOCKED. **What this does NOT establish:** nothing about `.agent_id`. My `agent_type` is
`praxis-worker`, so line 8 (`[ "$AGENT" = "praxis-master" ] || exit 0`) short-circuits regardless of
what `.agent_id` contains. Silence here is the exact ambiguity S9 exists to forbid.

### Attack B — confirm the real `.claude/settings.json` PreToolUse "Bash" block dispatches on my calls

Command run (no git binary is invoked; the string is free text inside `echo`):

```
$ echo "probeB harmless string containing git commit as free text"
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh]: BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
```

Establishes, live: the repo's `.claude/settings.json` `PreToolUse`/matcher `Bash` registration does
fire on this subagent's Bash calls, and my payload satisfies `agent_type` non-empty AND
NOT(`agent_type`=="praxis-master" AND `agent_id` empty). It does **not** reveal my `agent_id`.
My own PreToolUse payload was **not observed** — there is no read path to it without editing a hook,
which was out of bounds.

### Attack C — nested `claude` CLI launched from this subagent's Bash tool, running as `praxis-master`

Harness (created only under the scratchpad; nothing under `scripts/` or `.claude/` was touched):
`harness2-settings.json` registers two PreToolUse/Bash hooks — a scratchpad payload dumper, then the
**real** `/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh` by absolute path. cwd is the
scratchpad, so the repo's own settings are NOT loaded and no second session is cwd'd in the tree.

```
$ cd "$S" && claude -p "Run exactly this one Bash command and nothing else, then reply DONE. The command is: echo probeF > $S/probeF.txt" \
  --agent praxis-master --agents "$(cat "$S/agents.json")" \
  --settings "$S/harness2-settings.json" --tools Bash --model sonnet \
  --permission-mode bypassPermissions --output-format stream-json --verbose > "$S/c3.out.jsonl" 2>"$S/c3.err"; echo "EXIT=$?"
EXIT=0
```

Captured live payload (from the dumper hook, same PreToolUse dispatch that fed the guard):

```
keys= ['agent_type', 'cwd', 'effort', 'hook_event_name', 'permission_mode', 'prompt_id', 'session_id', 'tool_input', 'tool_name', 'tool_use_id', 'transcript_path']
agent_id_present= False agent_id= None | agent_type= 'praxis-master'
cmd= 'echo probeF > /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c3
```

Guard output, verbatim from the nested session's stream:

```
{"type":"user","message":{"role":"user","content":[{"type":"tool_result","content":"PreToolUse:Bash hook error: [/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh]: BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n","is_error":true,"tool_use_id":"toolu_01PnkKCxy8gVGFLkLmm4Rcaw"}]},...,"tool_use_result":"Error: PreToolUse:Bash hook error: [/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh]: BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n","tool_result_meta":[{"id":"toolu_01PnkKCxy8gVGFLkLmm4Rcaw","non_execution_kind":"permission-rule"}]}
```

```
$ ls -la "$S/probeF.txt"
ls: .../probeF.txt: No such file or directory
```

An earlier identical run (`c1`, with `--include-hook-events`) produced the same string as a hook
lifecycle record:

```
{"type": "system", "subtype": "hook_response", "hook_name": "PreToolUse:Bash", "hook_event": "PreToolUse", "output": "BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n", "stdout": "", "stderr": "BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n", "exit_code": 2, "outcome": "error", ...}
```

### Attack D — subagent whose own `agent_type` is `praxis-master` (tests the claim's premise)

Depth-1: nested main thread spawns subagent `praxis-master`, which runs the redirect.

```
agent_id_present= True agent_id= 'a530cc121d2d37552' | agent_type_present= True agent_type= 'praxis-master'
   cmd= 'echo probeE > .../probeE.txt'
agent_id_present= False agent_id= None | agent_type_present= False agent_type= None
   cmd= 'echo probeMain > .../probeMain.txt'
=== BLOCKED occurrences in c2 stream ===
0
-rw-r--r--@ 1 admin  wheel   7 Jul 26 18:00 .../probeE.txt
-rw-r--r--@ 1 admin  wheel  10 Jul 26 18:00 .../probeMain.txt
```

Depth-2: main thread -> `praxis-mid` -> `praxis-master` -> redirect.

```
agent_id_present= True agent_id= 'aea6ef2edb28e8096' | agent_type= 'praxis-master' | cmd= 'echo probeG > /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build
=== BLOCKED in c4 ===
(count: 0)
-rw-r--r--@ 1 admin  wheel  7 Jul 26 18:01 .../probeG.txt
{"parent_tool_use_id": "toolu_01TMU4NSkHeATif1HXzD7fHq", "result": {"tool_use_id": "toolu_015spdFDvNps83y2YUa6HmpW", "type": "tool_result", "content": "(Bash completed with no output)", "is_error": false}}
```

Both subagent shapes carried a non-empty 17-hex-char `agent_id` and produced byte-identical silence
from the guard (`(Bash completed with no output)`, file written, zero BLOCKED occurrences), even
though `agent_type` was exactly `praxis-master`. The claim's **premise survived every shape I could
construct.**

### Attack E — run the nested session against the repo's own `.claude/settings.json` registration: STOPPED

This is the only remaining gap (real script + real registration in one run). It requires a second
Claude session whose hooks resolve `$CLAUDE_PROJECT_DIR` to this repo. Blocked by CLAUDE.md, quoted
verbatim (`CLAUDE.md:30`, under `## Do Not`):

```
- Run multiple Claude sessions against this working tree — one session per repo; parallel work goes in its own `git worktree` (docs/runbooks/2026-07-10-single-session-rule.md)
```

Line of attack stopped, not worked around. Related observed state: `.claude/state/orchestrator-active`
exists and `.claude/state/run-mode` contains `interactive`.

### Attacks considered and not reachable
- `Agent` tool from this worker: `praxis-worker.md` frontmatter sets `disallowedTools: Agent`, and
  `scripts/agent-spawn-guard.sh` denies `praxis-worker` as caller. I hold no Agent tool; not attempted.
- Editing/creating any hook, settings file, or agent definition to force the field: out of bounds.
- Producing `agent_id` present-but-empty-string: I found no CC-side lever. **Not observed.**

---

## 2. Verdict

**YES — the real BLOCKED string was emitted, from an execution path rooted in this subagent's Bash
tool call.** Verbatim:

```
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
```

emitted by `/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh` (sha256
`2dd67afc…3101`), exit code 2, against a live PreToolUse payload observed in the same dispatch to
have **no `agent_id` key** and `agent_type == "praxis-master"`.

---

## 3. What this does and does not establish

**Established (observed this session):**
- The claim's conclusion as written — "there exists no way, from inside a spawned subagent, to cause
  that BLOCKED string to be emitted" — is **false**. A subagent's Bash tool can launch a nested
  `claude` main-thread session running as `praxis-master`; that session's PreToolUse dispatch runs the
  real guard file and emits the real string. Blocking still happens under
  `--permission-mode bypassPermissions` (the tool did not execute; `probeF.txt` was never created).
- A payload with empty/absent `agent_id` + `agent_type == "praxis-master"` is producible from a
  subagent — via a new session, not via the subagent's own payload.
- The repo's real `.claude/settings.json` PreToolUse/`Bash` block does dispatch on subagent Bash calls
  (Attack B, `no-commit-guard.sh` fired from that same block).

**Not established:**
- The claim's premise stands: **I found no subagent whose own PreToolUse payload lacks `agent_id`.**
  Two live shapes (depth-1 and depth-2, `agent_type` exactly `praxis-master`) both carried non-empty
  `agent_id`. This is "I could not find one", not "none exists". I tested inline-defined agents in a
  foreign-cwd harness only; I did not test the repo's real agent definitions, background agents
  (`--bg`), `--resume`/`--fork-session`, SDK/stream-json input, or MCP-initiated tool calls.
- I never observed **this** session's own PreToolUse payload. My `agent_id` value is **not observed**.
- No run combined the real script *and* the repo's real registration. The registration half is
  evidenced only indirectly (Attack B).
- The S9 second half ("an invented key at the same position produces byte-identical silence") was not
  run at the config-key level: it requires editing the script or settings, which was out of bounds. The
  silences recorded in Attack D are field-*value* controls, not invented-*key* controls.

**Question for the master, not answered here:** whether an out-of-tree harness that executes the real
script file under a real CC PreToolUse dispatch satisfies S9's "confirm a visible script fires at that
field", or whether S9 requires the in-repo registration. That is a spec-interpretation call.

---

## 4. Surprises

1. A PreToolUse hook denial is reported to the calling model as `"non_execution_kind":"permission-rule"`
   and appears in the run's `permission_denials` array — a hook denial is indistinguishable from a
   permissions denial in that field, and it fires even under `bypassPermissions`.
2. `--settings <json-file>` accepts an absolute path to a hook script outside the session's project
   dir, and CC executes it. Hook scripts are therefore reachable by any session on the machine; the
   guard's protection is not bound to the repo it lives in.
3. Spawned subagents in CC 2.1.220 launch as background/async agents and their `agent_id`
   (17 hex chars, e.g. `aea6ef2edb28e8096`) is the same value surfaced to the parent as `agentId` in
   the Agent tool result text.
4. Piping the nested run through `head -c` killed it via SIGPIPE mid-session and produced a
   truncated, wrong-looking transcript. A truncated stream looks exactly like "the hook never fired".

---

## Files staged
None. `git add` and all index/history operations were out of bounds for this task; this report is
written but unstaged. Scratchpad-only artifacts (harness settings, payload dumper, captured
`payloads.jsonl` / `c1–c4.out.jsonl`) live under
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/`
and are outside the repo.

## Result
**FAIL (claim broken).** The claim's conclusion is falsified; its premise is not.
