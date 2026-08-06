# Session 36 — Controlled experiment: does a root `"agent"` key in project `.claude/settings.json` set `agent_type` in PreToolUse payloads?

**Task:** Three-arm controlled experiment (plus one positive control), run entirely in a scratch lab outside the repo.
**Mode:** BUILD (controlled experiment)
**Date:** 2026-07-26
**Claude Code version under test:** `2.1.220 (Claude Code)` (verified this session via `claude --version`)

---

## RESULT HEADLINE

**NULL RESULT. The hypothesis is refuted by direct measurement.**

A root-level `"agent": "praxis-master"` key in a project's `.claude/settings.json` did **not** set `agent_type` in the PreToolUse hook payload. `agent_type` was **absent entirely** from the payload in all three arms, including ARM A. Arms A, B, and C were **byte-for-byte indistinguishable** in every measured dimension.

The `.claude/settings.json` sha256 in the repo **matches** the expected value `eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a`. No LOUD warning needed.

---

## Constants held across all arms

Verified from each nested session's `system/init` stream line (pasted below), not asserted:

```
=== ARM A init ===
{"model": "claude-sonnet-5", "permissionMode": "bypassPermissions", "cwd": "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab", "agents": ["claude", "Explore", "general-purpose", "Plan", "statusline-setup"], "tools": ["Bash"]}
=== ARM B init ===
{"model": "claude-sonnet-5", "permissionMode": "bypassPermissions", "cwd": "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab", "agents": ["claude", "Explore", "general-purpose", "Plan", "statusline-setup"], "tools": ["Bash"]}
=== ARM C init ===
{"model": "claude-sonnet-5", "permissionMode": "bypassPermissions", "cwd": "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab", "agents": ["claude", "Explore", "general-purpose", "Plan", "statusline-setup"], "tools": ["Bash"]}
=== ARM P init ===
{"model": "claude-sonnet-5", "permissionMode": "bypassPermissions", "cwd": "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab", "agents": ["claude", "Explore", "general-purpose", "Plan", "statusline-setup"], "tools": ["Bash"]}
```

- **`--agent` was NOT passed in any arm.** That flag is the known confound and was deliberately excluded.
- **`--settings` was NOT passed in any arm.** The thing under test is a *project-level* `.claude/settings.json`, and that is what was used.
- Same prompt shape, same model (`claude-sonnet-5`), same `--permission-mode bypassPermissions`, same cwd, same tool allowlist (`Bash`), same guard path, fresh `claude` process per arm.
- **`--permission-mode bypassPermissions` is stated plainly as a held constant.** It applies only to throwaway nested processes in a scratch directory outside the repo. No repo file was reachable by the probe command, which wrote only to the lab.

**LAB** = `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab`

---

## Harness validation (done BEFORE any arm was run)

### 1. Dumper self-test — it correctly distinguishes present/absent `agent_type`

```
dumper exit=0
dumper exit=0
--- payloads.jsonl ---
{"arm":"SELFTEST","agent_id_present":false,"agent_id_value":"null","agent_type_present":true,"agent_type_value":"praxis-master","keys":["agent_type","session_id","tool_input","tool_name"],"command":"echo hi > /tmp/z"}
{"arm":"SELFTEST","agent_id_present":false,"agent_id_value":"null","agent_type_present":false,"agent_type_value":"null","keys":["session_id","tool_input","tool_name"],"command":"echo hi > /tmp/z"}
--- dumper.err ---
```

The dumper always exits 0, so it can never itself deny a call.

### 2. Real guard, driven directly with synthetic payloads

```
=== synthetic master-shape payload ===
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
guard exit=2
=== synthetic no-agent_type payload ===
guard exit=0
```

### 3. Real guard, driven with the EXACT probe command and lab path used in ARM A

```
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
guard exit with REAL lab path=2
```

This rules out the lab path accidentally hitting one of the guard's exemption globs (`*DISPATCH_LOG.md*`, `*DECISION_LOG.md*`, `*ISSUE_REGISTER.md*`, `*HANDOFF.md*`, `*/specs/*`, `*/docs/reports/*`).

---

## Arm-differs-only-in-key-name proof

```
=== diff settings.A.json settings.B.json ===
2c2
< "agent": "praxis-master",
---
> "zzz_bogus_agent_key": "praxis-master",
(diff exit=1)
=== diff settings.A.json settings.C.json ===
2d1
< "agent": "praxis-master",
(diff exit=1)
```

A vs B: the value (`"praxis-master"`) and the position (line 2, first root key) are identical; only the key **name** differs. A vs C: the line is removed outright. All three parsed as VALID JSON via `jq -e`.

ARM A's active `.claude/settings.json`, pasted as it was on disk at launch:

```json
{
"agent": "praxis-master",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab/dumper.sh", "timeout": 30 },
          { "type": "command", "command": "/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh", "timeout": 30 }
        ]
      }
    ]
  }
}
```

---

## Flat observations, one arm at a time

### ARM A — `"agent": "praxis-master"`

Dumped payload line:
```
{"arm":"A","agent_id_present":false,"agent_id_value":"null","agent_type_present":false,"agent_type_value":"null","keys":["cwd","effort","hook_event_name","permission_mode","prompt_id","session_id","tool_input","tool_name","tool_use_id","transcript_path"],"command":"echo probeA > /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/2488feec-6500-4e04-b743-262c306cfabb/scratchpad/s9lab/outA.txt"}
```
- `agent_id` key PRESENT? **no**. Value: n/a.
- `agent_type` key PRESENT? **no**. Value: n/a.
- Full sorted key list: `cwd, effort, hook_event_name, permission_mode, prompt_id, session_id, tool_input, tool_name, tool_use_id, transcript_path`

BLOCKED string in stream:
```
=== ARM A: grep -c BLOCKED in A.jsonl ===
0
```

Probe file:
```
=== ARM A: ls outA.txt ===
-rw-r--r--@ 1 admin  wheel  7 Jul 26 18:07 /private/tmp/.../s9lab/outA.txt
=== outA.txt content ===
probeA
```

Nested exit code:
```
NESTED EXIT CODE=0
```
stderr was empty. Stream was 14 lines (not truncated; no `head`/`less` in the pipeline, output went straight to a file).

### ARM B — `"zzz_bogus_agent_key": "praxis-master"`

```
{"arm":"B","agent_id_present":false,"agent_id_value":"null","agent_type_present":false,"agent_type_value":"null","keys":["cwd","effort","hook_event_name","permission_mode","prompt_id","session_id","tool_input","tool_name","tool_use_id","transcript_path"],"command":"echo probeB > /private/tmp/.../s9lab/outB.txt"}
=== ARM B: grep -c BLOCKED in B.jsonl ===
0
=== ARM B: ls outB.txt ===
-rw-r--r--@ 1 admin  wheel  7 Jul 26 18:07 /private/tmp/.../s9lab/outB.txt
=== ARM B: stderr ===
=== ARM B: stream lines ===
      14
NESTED EXIT CODE=0
```

### ARM C — key absent entirely

```
{"arm":"C","agent_id_present":false,"agent_id_value":"null","agent_type_present":false,"agent_type_value":"null","keys":["cwd","effort","hook_event_name","permission_mode","prompt_id","session_id","tool_input","tool_name","tool_use_id","transcript_path"],"command":"echo probeC > /private/tmp/.../s9lab/outC.txt"}
=== ARM C: grep -c BLOCKED in C.jsonl ===
0
=== ARM C: ls outC.txt ===
-rw-r--r--@ 1 admin  wheel  7 Jul 26 18:08 /private/tmp/.../s9lab/outC.txt
=== ARM C: stderr ===
=== ARM C: stream lines ===
      13
NESTED EXIT CODE=0
```

No arm produced any settings-parse warning:
```
=== grep -ci 'unrecognized|unknown key|invalid setting' across arms ===
A: 0
B: 0
C: 0
```

---

## Comparison

| | ARM A `"agent"` | ARM B `"zzz_bogus_agent_key"` | ARM C absent |
|---|---|---|---|
| dumper hook fired | yes | yes | yes |
| `agent_id` present | no | no | no |
| `agent_type` present | **no** | no | no |
| payload key list | identical | identical | identical |
| BLOCKED string count | 0 | 0 | 0 |
| probe file created | yes | yes | yes |
| nested exit code | 0 | 0 | 0 |

**A is indistinguishable from B, and B is a deliberately meaningless key name.** A is also indistinguishable from C, which has no key at all. The `"agent"` root settings key had no observable effect of any kind.

Per the stated decision rule — a mechanism may be declared confirmed only if ARM A produced BLOCKED, arms B and C did not, and dumped `agent_type` differed accordingly — **the mechanism is NOT confirmed. It is affirmatively disconfirmed on the measured field.** `agent_type` was absent in ARM A, so the guard's `[ "$AGENT" = "praxis-master" ] || exit 0` line short-circuits by construction; the guard *could not* have fired regardless.

---

## Positive control (ARM P) — proves the silence in A/B/C is real, not a dead harness

The concern: in arms A/B/C the guard exits 0 whenever `agent_type` is absent, so guard silence is *expected* whether or not the guard ran at all. To close that gap I ran a fourth, separately-labelled control using ARM C's settings with the second hook slot replaced by a wrapper that discards the real payload and feeds the **real guard** a synthetic payload carrying `agent_type: "praxis-master"` and the real command string, passing the guard's exit code through.

```
NESTED EXIT CODE=0
=== ARM P: grep -c BLOCKED ===
3
=== ARM P: matching lines ===
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\n
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.\
=== ARM P: ls outP.txt ===
ls: /private/tmp/.../s9lab/outP.txt: No such file or directory
=== ARM P payload line ===
{"arm":"P","agent_id_present":false,"agent_id_value":"null","agent_type_present":false,"agent_type_value":"null","keys":["cwd","effort","hook_event_name","permission_mode","prompt_id","session_id","tool_input","tool_name","tool_use_id","transcript_path"],"command":"echo probeP > /private/tmp/.../s9lab/outP.txt"}
```

This establishes three things the null arms could not: the **second** entry in the `hooks` array does execute; the real guard at `/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh` runs and denies from this harness; and the deny string **does** surface in the `stream-json` transcript with the probe file left uncreated. Had the `"agent"` key set `agent_type`, ARM A would have looked like ARM P. It did not.

Note ARM P's dumper line still shows `agent_type` absent — as expected, since the dumper sees the *real* payload and only the wrapper substitutes a synthetic one.

---

## What this harness does NOT establish

1. **My lab is a DIFFERENT project directory from the real repo** (`/private/tmp/.../s9lab`, not `/Volumes/Sensidine/Praxis.build`). This result does not transfer automatically. It is evidence about how Claude Code 2.1.220 treats a root `"agent"` key in *a* project settings file; it is not a direct measurement of the repo's own settings file in the repo's own directory.
2. It says nothing about **other settings scopes** — user-level `~/.claude/settings.json`, `settings.local.json`, enterprise/managed settings, or a `--settings` file. Only project-level `.claude/settings.json` was tested.
3. It says nothing about **other key spellings or nestings** (`agentType`, `defaultAgent`, `agent.type`, an `agent` object rather than a string). Only the exact literal `"agent": "praxis-master"` at the root, first position, was tested.
4. It does not establish that `--agent praxis-master` sets `agent_type`. That claim rests on the earlier probe in this session, which I did not re-run here and therefore mark **UNVERIFIED by me in this arm set**. My arms deliberately excluded the flag.
5. **n=1 per arm.** No repetition, no interleaving of arm order. A flaky or ordering-dependent effect would not be detected — though the identical key lists across four independent processes argues against noise.
6. It says nothing about how PreToolUse behaves for **non-Bash tools** or for **subagent-originated** calls in the real repo; the matcher was `Bash` only and every measured payload came from a main-thread call.
7. Nested sessions ran under `bypassPermissions`. If `agent_type` propagation were somehow permission-mode dependent, this harness would not see it.

---

## Repo integrity

No file under `/Volumes/Sensidine/Praxis.build` was edited, created, deleted, moved, or chmod'd by this task except this report. No `git add`/`commit`/`restore`/`reset`/`stash` or any other index or history operation was run. `.claude/settings.json` was read only — never written.

Run at the very end of the work:

```
$ shasum -a 256 /Volumes/Sensidine/Praxis.build/.claude/settings.json
eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a  /Volumes/Sensidine/Praxis.build/.claude/settings.json

$ cd /Volumes/Sensidine/Praxis.build && git status --porcelain && git diff --cached --numstat
M  .claude/settings.json
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M ISSUE_REGISTER.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-manifest-amendment.md
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
?? docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
?? docs/reports/2026-07-26-session36-agent-key-audit.md
?? docs/reports/2026-07-26-session36-worker-trigger-probe.md
--- numstat ---
1	0	.claude/settings.json
```

The settings.json sha256 **matches** the expected restore target. Its staged diff is still `1 insertion, 0 deletions`.

**One incidental observation, NOT caused by me and NOT acted on:** the git status snapshot taken at the start of my session listed `M  docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md` as **staged**; at the end of my work that same path appears as **untracked (`??`)**. I ran no git index operations of any kind, so this is another worker's concurrent activity against the same working tree. Reporting it, not fixing it. It may be worth checking against the single-session rule in `docs/runbooks/2026-07-10-single-session-rule.md`.

---

## Files staged

None. Nothing was staged by this task. The only repo file written is this report, which is untracked.

Lab artifacts (outside the repo, for audit): `LAB/settings.{A,B,C,P}.json`, `LAB/dumper.sh`, `LAB/forced_master_wrapper.sh`, `LAB/payloads.jsonl`, `LAB/{A,B,C,P}.jsonl`, `LAB/{A,B,C,P}.stderr`.

## Result

**PASS** — the experiment ran cleanly and returned a decisive **negative** answer to the question under test. A root `"agent"` key in a project `.claude/settings.json` does not set `agent_type` in PreToolUse payloads on Claude Code 2.1.220 in this lab configuration. The settings key is not a viable substitute for the `--agent` CLI flag on the evidence collected here.

No arm was re-run, reconfigured, or rescued after seeing its result. `--agent` was never added.
