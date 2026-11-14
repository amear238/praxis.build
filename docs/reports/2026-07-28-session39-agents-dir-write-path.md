# Does `master-write-guard.sh` fall open for a subagent writing to `.claude/agents/`?

**Bead:** `Praxis_build-s8g` (P0, bug) · **Session:** 39 · **Date:** 2026-07-28
**Manager:** praxis-manager · **HEAD:** `c1dec30` · **Branch:** main

---

## Task

Settle by experiment, not by reading, whether `scripts/master-write-guard.sh`
exempts a **subagent** writing to `.claude/agents/`. The master's static read
predicted "yes" from two observations (line 8 short-circuit; no hook registered
on that directory). This unit exists because a static read is not evidence —
this project has produced two confident wrong conclusions from well-cited
static reads.

**Answer: YES, CONFIRMED BY EXPERIMENT — and the hole is wider than the brief
supposed.** The guard exits 0 at line 8 *before `file_path` is ever extracted*,
so the exemption is **path-independent**: for a subagent this guard imposes no
restriction on any path whatsoever, not merely on `.claude/agents/`.

Separately, and more importantly: **`master-write-guard.sh` is the only hook on
this entire machine that matches `Write`/`Edit`/`NotebookEdit`, from any source.**
Nothing else covers the path.

---

## Rubric criteria addressed

| # | Criterion | How discharged |
|---|---|---|
| S1 | Pasted command output, not description | Every claim below carries raw stdout/stderr. No paraphrase. |
| S2 | No component reported above its evidence | OBSERVED / INFERRED split is stated explicitly per claim in §7. |
| S3 | Every gate claimed working deliberately tripped | ARM B and B2 trip the guard: `exit 2` + 161-byte `BLOCKED`. Trace pasted. |
| S9 | Invented-key positive control, both directions | ARM D (`agent_typeX`) and ARM E (`agent_idX`) — §3. |

Method authorised by Amear and used exclusively: synthetic `PreToolUse` payloads
piped to the guard on stdin. **No file was created, modified, moved or deleted
in the repo. Nothing was written to `.claude/agents/`.** A live write-attempt was
explicitly not authorised and was not performed.

---

## Workers dispatched

| Worker | Mode | Scope | Outcome |
|---|---|---|---|
| W1 | BUILD | Arms A–E + `bash -x` liveness traces against the guard | PASS — all 7 arms matched pre-registered predictions |
| W2 | ADVERSARIAL | Falsify "the path is uncovered"; enumerate every hook and permission rule from every source | CLAIM SURVIVES — no blocker found |

W2 was given the artifact and the criterion only. It was never shown W1's
payloads, reasoning, or conclusion. Both ran concurrently on isolated scratchpad
outputs, so neither could anchor on the other. Max-2-worker limit respected.

---

## Process log

1. Read `specs/SPEC_RUBRIC.md`; recorded baseline HEAD and staged index.
2. Recorded `.claude/agents/` mtimes as a breach tripwire **before** any work.
3. Enumerated every settings source myself (project, local, user, managed, plugins).
4. Dispatched W1 (BUILD) and W2 (ADVERSARIAL) concurrently.
5. **Ran all seven arms independently myself** rather than accept a summary.
6. Ran `bash -x` traces myself to identify the exact exit line.
7. Closed W1's self-declared open gap using live captured payloads (§5).
8. Closed W2's strongest residual uncertainty using live `permission_mode` (§6).
9. Re-verified mtimes and staged index unchanged at end.

---

## Verification evidence — pasted output only

### §1 Environment preconditions

A missing `jq` would make every arm exit 0 for the wrong reason and manufacture
a false null.

```
jq: jq-1.7.1-apple
guard sha256: bb0c66cd179c0213628b7fcd658a448522365c373e5f77ea6c7183ce2e664487  /Volumes/Sensidine/Praxis.build/scripts/master-write-guard.sh
```

### §2 The guard as read (unmodified; hash above matches W1's before/after)

```bash
 4 INPUT=$(cat)
 6 AGENT_ID=$(jq -r '.agent_id // ""' <<<"$INPUT")
 7 AGENT=$(jq -r '.agent_type // ""' <<<"$INPUT")
 8 [ -n "$AGENT_ID" ] && exit 0
 9 [ "$AGENT" = "praxis-master" ] || exit 0
10 FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')
```

### §3 All seven arms — my own independent run

Every payload is identical apart from the single field named. Common shape:

```
{"session_id":"s39","cwd":"/Volumes/Sensidine/Praxis.build","agent_id":"<X>","agent_type":"<Y>","tool_name":"Write","tool_input":{"file_path":"<Z>","content":"x"}}
```

with `<Z>` = `/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md`
except in ARM C.

```
ARM A   EXIT=0  STDERR_BYTES=0  STDERR=[]
ARM A2  EXIT=0  STDERR_BYTES=0  STDERR=[]
ARM B   EXIT=2  STDERR_BYTES=161  STDERR=[BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md'.]
ARM B2  EXIT=2  STDERR_BYTES=161  STDERR=[BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md'.]
ARM C   EXIT=0  STDERR_BYTES=0  STDERR=[]
ARM D   EXIT=0  STDERR_BYTES=0  STDERR=[]
ARM E   EXIT=2  STDERR_BYTES=161  STDERR=[BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md'.]

=== payloads validate as JSON ===
A: valid JSON
A2: valid JSON
B: valid JSON
B2: valid JSON
C: valid JSON
D: valid JSON
E: valid JSON
```

| Arm | Single varied field | Exit | Confirms / refutes |
|---|---|---|---|
| A | `agent_id` non-empty + `agent_type=praxis-worker` | 0 | Subagent-shaped write to `.claude/agents/` ALLOWED. Two fields differ vs B, so alone it proves nothing about *which* — hence A2. |
| A2 | `agent_id` non-empty **only** (vs B) | 0 | **ISOLATION: non-empty `agent_id` alone flips deny → allow.** |
| B | `agent_id` key absent | 2 | **LIVENESS / S3 trip.** Guard denies this exact path for the main thread. |
| B2 | `agent_id` = `""` | 2 | Empty string == absent. Exemption requires NON-EMPTY. |
| C | `file_path` = `DISPATCH_LOG.md` | 0 | Allowlist allow, reached line 14 — **not** an early bail. |
| D | `agent_type` → `agent_typeX` | 0 | **S9:** guard keys on the literal name `agent_type`. |
| E | `agent_id` → `agent_idX` | 2 | **S9:** removing the real key restores the deny. `agent_id` IS the exempting field. |

**The decisive pair is A2 vs E.** The payloads differ only in the spelling of the
`agent_id` key and they split 0 vs 2.

W1 independently hashed each stderr rather than eyeballing it — silent arms
A/A2/C/D are `e3b0c442…b855` (sha256 of the empty byte string, byte-identical to
a true no-op); denying arms B/B2/E are all `14f3490f…`. (W1 reports 162 bytes
where I report 161; the difference is my `$(…)` stripping the trailing newline.
Same string.)

### §4 Liveness traces — which line does it exit at?

An exit 0 is otherwise indistinguishable from a script that never ran.

```
########## ARM A2 TRACE (subagent) ##########
+ INPUT='{"session_id":"s39",…"agent_id":"agent_01H8XKQ","agent_type":"praxis-master"…}'
++ jq -r '.agent_id // ""'
+ AGENT_ID=agent_01H8XKQ
++ jq -r '.agent_type // ""'
+ AGENT=praxis-master
+ '[' -n agent_01H8XKQ ']'
+ exit 0
EXIT=0
```

Exits at **line 8**. `FILE` is never extracted; the `case` allowlist is never
reached. The path being written is *never consulted*.

```
########## ARM B TRACE (main-thread master) ##########
+ '[' -n '' ']'
+ '[' praxis-master = praxis-master ']'
++ jq -r '.tool_input.file_path // .tool_input.path // empty'
+ FILE=/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md
+ '[' -z /Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md ']'
+ case "$FILE" in
+ echo 'BLOCKED: praxis-master may only write ledgers, specs, and reports. …'
BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/.claude/agents/praxis-master.md'.
+ exit 2
EXIT=2
```

The gate is armed and does block. The exit 0s above are **decisions, not silence**.

### §5 The load-bearing premise, closed by live capture

W1 correctly refused to close one link: *do real subagents actually receive a
non-empty `agent_id`?* Under the synthetic-only method it could not know, and
flagged it as UNVERIFIED. That honesty is what made it checkable.

I closed it with **real payloads captured from live traffic** by the
`capture-agent.sh` hook already registered on `PreToolUse:Agent` — including the
payloads generated by this unit's own two dispatches. Not synthetic:

```
=== identity fields of EVERY captured event (real payloads, not synthetic) ===
   2 ts_ok agent_id=a27539a76d8129628  agent_type=praxis-manager  tool=Agent  subagent_type=praxis-worker
   1 ts_ok agent_id=aa9dd789c8548df5a  agent_type=praxis-manager  tool=Agent  subagent_type=praxis-worker
   1 ts_ok agent_id=<ABSENT>  agent_type=praxis-master  tool=Agent  subagent_type=praxis-manager
```

Two facts, both OBSERVED:

1. A **subagent**'s `PreToolUse` payload carries a **non-empty `agent_id`**.
2. The **main thread**'s payload has `agent_id` **absent** — which independently
   validates ARM B's construction as a faithful model of the main thread, rather
   than a shape I invented to make the control fire.

The guard's line-5 comment is therefore correct, and the exemption is reachable
in practice, not merely in theory.

### §6 Permission layer — no coverage, and no prompt in this mode

```
=== .claude/settings.local.json permissions (full) ===
{
  "allow": [
    "Bash(claude --version)",
    "Bash(git -C /Volumes/Sensidine/Praxis.build log -5 --oneline)",
    "Bash(git -C /Volumes/Sensidine/Praxis.build status --short)"
  ]
}

=== any rule mentioning agents/ or Write across ALL settings sources ===
--- .claude/settings.json ---
(no Write/Edit/agents rule)
--- .claude/settings.local.json ---
(no Write/Edit/agents rule)
--- /Users/admin/.claude/settings.json ---
(no Write/Edit/agents rule)
```

W2's strongest residual uncertainty was that Claude Code special-cases
`.claude/**` in the edit-permission dialog, so in `default` mode the write might
still surface a prompt to Amear. Settled from the same live capture:

```
=== permission_mode in REAL captured payloads ===
   2 agent_type=praxis-manager agent_id=a27539a76d8129628 permission_mode=bypassPermissions
   1 agent_type=praxis-manager agent_id=aa9dd789c8548df5a permission_mode=bypassPermissions
   1 agent_type=praxis-master agent_id=<ABSENT> permission_mode=bypassPermissions
```

**This session runs in `bypassPermissions`, for subagents as well as the main
thread.** The permission dialog is not a backstop here. This is a property of
*this session*, not a universal one — a session launched in `default` mode may
behave differently, and that remains untested.

### §7 Hook inventory on `Write` / `Edit` — separately-labelled finding

Per ruling R3, "X is covered by mechanism Y" is graded by toggling Y. Toggling
requires editing a settings file, which hard limit 4 forbids, so I discharged it
the only way available: enumerate every candidate from every source, then feed
each the subagent payload and require a **firing positive control** for every
claimed no-op. My memory records that reading `.claude/settings.json` alone
under-counts, because enabled plugins register hooks too — so plugins were
enumerated from `enabledPlugins`, not assumed absent.

```
=== locate ENABLED plugin roots and their hook events ===
--- superpowers ---   .../superpowers/6.1.1/hooks/hooks.json -> events: SessionStart
--- context7 ---      NO hooks.json
--- opsera-devsecops --- .../opsera-devsecops/1.0.0/hooks/hooks.json -> events: PreToolUse
     PreToolUse matcher=Bash
--- n8n-mcp-skills ---  NO hooks.json
--- praxis-progress --- NO hooks.json
--- warp ---            NO hooks.json
```

```
=== settings files present ===
PRESENT: .claude/settings.json
PRESENT: .claude/settings.local.json
PRESENT: /Users/admin/.claude/settings.json
ABSENT : /Users/admin/.claude/settings.local.json
ABSENT : /Library/Application Support/ClaudeCode/managed-settings.json
```

| Hook | Source | Matcher | Could it stop a subagent write to `.claude/agents/`? |
|---|---|---|---|
| `master-write-guard.sh` | repo settings | `Write\|Edit\|NotebookEdit` | **NO — the only Write-matching hook that exists, and it exits 0 at line 8 for every subagent.** |
| `no-commit-guard.sh` | repo settings | `Bash` | No — wrong matcher; never invoked on Write. |
| `gate-commit.sh` | repo settings | `Bash` | No — wrong matcher. |
| `master-bash-guard.sh` | repo settings | `Bash` | No — wrong matcher, and it is a shell-*redirection* guard, not a path guard. |
| `agent-spawn-guard.sh` | repo settings | `Agent` | No — wrong matcher. |
| `capture-agent.sh` | repo settings | `Agent` | No — log-only, `exit 0` unconditionally. Also a session-scoped scratchpad path: a phantom for any other session. |
| `pre-commit-scan.sh` | opsera-devsecops plugin | `Bash` | No — wrong matcher. |
| superpowers / warp | plugins | SessionStart / Stop etc. | No — not `PreToolUse` at all. |
| **permission rules** | all sources | — | **No — the only deny anywhere is `Agent(general-purpose)`.** |

W2 additionally grepped every repo hook script for the path:
`grep -rn '\.claude/agents\|agents/'` across `scripts/*.sh` and
`.claude/hooks/*.sh` → **zero hits.** No hook in this repo has any awareness of
`.claude/agents/`.

**Conclusion for the separate finding: exactly one hook matches Write/Edit on
this machine, it waves every subagent through unconditionally, and no permission
rule covers the path. Nothing at all covers it.**

---

## Adversarial findings (W2)

- **Verdict: CLAIM SURVIVES — no blocker found.** W2 was tasked to falsify "the
  path is uncovered" and could not.
- W2 hit the exact false-null trap this project has recorded before: its first
  counterfactual block returned `exit=127 command not found: timeout` on all five
  hooks — macOS has no `timeout` binary — which reads identically to "the hook
  never fired." It caught this itself, re-ran without the wrapper, and recorded
  the incident. Had it not, five hooks would have been reported as silent no-ops
  on the strength of a harness error.
- W2 required and obtained a **firing positive control for every hook** it
  declared a no-op, so none of its exit-0s are crash-silence.
- **New qualifier W2 surfaced (OBSERVED):** `praxis-auditor` and
  `orchestrator-auditor` carry `disallowedTools: Write, Edit` in their
  definitions. This is agent-scoped and tool-wide, not path-wise — and
  **`praxis-worker` and `praxis-manager` both have Write and Edit**, so it does
  not narrow this hole. Whether a *spawned* child's `disallowedTools` is even
  enforced is **UNVERIFIED**, and S10 already established that a child's
  `tools:` allowlist is silently discarded.
- **W2 self-reported a minor limit deviation:** it created extra scratch capture
  files (`t1–t4.err`, `o.out/err`, `p.out/err`, `cli-strings.txt`) in the session
  scratchpad, where its brief named a single output file. **Zero repo files
  touched**; `git status --short` byte-identical to session start;
  `git status -- .claude/agents/` returned 0 lines. Disclosed, not discovered.
  I verified the repo claim independently (§9).

---

## S6 cross-block check

The exemption is **path-independent** — the guard returns at line 8 before
`file_path` is read — so its blast radius is not confined to the directory named
in the brief. Every other block that assumes a hook mediates writes is touched:

- **Producer/grader separation (S10, S11).** The separation guarantee rests on
  agent definitions and on `.claude/settings.json` being stable. Both are
  writable by a subagent as far as the hook layer is concerned. A worker cannot
  *spawn* the auditor (that is enforced by `agent-spawn-guard.sh` on the `Agent`
  matcher, untouched by this finding), but nothing in the hook layer stops it
  editing the auditor's definition file.
- **S7 / commit gating.** Unaffected by this specific hole, but note it compounds
  a finding already on record: the four Bash guards are evaded by `git 'commit'`.
  Neither the write path nor the commit path is a control against a deliberate act.
- **S12 ledger integrity.** `AUDIT_LOG.md` and `DISPATCH_LOG.md` are writable by
  any subagent. Ledger append-only-ness is a convention here, not a mechanism.

I am **not** extrapolating these to demonstrated exploits — see the next section.

---

## What this does and does not establish

**OBSERVED (measured this session):**
- `master-write-guard.sh` exits 0 at line 8 for any payload with a non-empty
  `agent_id`, before `agent_type` is compared and before `file_path` is extracted.
- The same payload minus `agent_id` is denied with exit 2 and a 161-byte message.
- `agent_id` is the field responsible — renaming it restores the deny (ARM E).
- Real subagent `PreToolUse` payloads carry a non-empty `agent_id`; the main
  thread's does not.
- Exactly one hook on this machine matches `Write`/`Edit`/`NotebookEdit`.
- No permission rule anywhere covers `.claude/agents/`.
- This session's `permission_mode` is `bypassPermissions` for subagents.

**INFERRED / NOT TESTED — stated as such, deliberately not extrapolated:**
- **No write to `.claude/agents/` was ever attempted.** That a subagent's write
  would *succeed* end-to-end is a strong inference from the above, not an
  observation. It was not authorised and was not performed.
- The live payloads I captured are `PreToolUse:Agent` events. That the `Write`
  tool's envelope carries `agent_id` identically is an inference — well supported,
  since `agent_id`/`agent_type`/`tool_name` are clearly envelope fields shared
  across tools, but it is an inference.
- The R3 config-toggle was **not** performed; toggling a settings file is
  forbidden by hard limit 4. Coverage was established by exhaustive enumeration
  plus per-hook positive controls instead.
- `bypassPermissions` is a property of this session, not of the repo.
- Whether `disallowedTools` binds a spawned child is unverified.

**Secondary finding, reported not fixed (guard remediation is deferred cold by
ruling G-2):** ARM D shows the guard **fails open on unexpected payload shape**.
If a future Claude Code version renames, removes, or nests `agent_type`, the
guard silently allows everything with exit 0 and zero stderr — indistinguishable
from a healthy no-op. This matches the standing record that this guard family
fails OPEN, never closed.

---

## §9 Files staged / integrity

Staged index unchanged from the parked commit, start and end:

```
=== staged index at start ===
6 paths / 1576 / 0
=== staged index at end ===
6 paths / 1576 / 0
```

`.claude/agents/` mtimes — tripwire for hard limit 1. No file shows 2026-07-28:

```
Jul 10 12:35:39 2026 orchestrator-auditor.md
Jul 25 16:40:18 2026 praxis-auditor.md
Jul 26 10:08:33 2026 praxis-manager.md
Jul 26 10:54:17 2026 praxis-master.md
Jul 24 12:55:29 2026 praxis-tutor.md
Jul 26 10:08:33 2026 praxis-worker.md
```

Guard script unmodified — `git status --short scripts/ .claude/settings.json`
returns only entries **already present in the session-start snapshot**
(` M .claude/settings.json`, ` M scripts/dispatch-log-writeahead.sh`,
`?? scripts/dispatch-log-close.sh`, `?? scripts/tests/test-dispatch-log-close.sh`).
`scripts/master-write-guard.sh` does not appear. Its sha256 is
`bb0c66cd…4487` before and after.

**Files created by this unit: this report only.** Nothing staged. No commit, no
push, no branch, no checkout. Nothing written to `.claude/agent-memory/`.
No breach by me. W2's minor scratchpad deviation is disclosed above.

---

## Result

The master's static read was **correct** — and, unusually for this project, the
experiment widened rather than narrowed the finding: the exemption ignores the
file path entirely, and the covering mechanism the brief hoped to find does not
exist in any form, from any source.

The verdict below grades **this investigation's rigour**, not the existence of
the hole: seven single-variable arms, S9 controlled in both directions, the gate
tripped and traced, an independent adversarial falsification attempt that failed
honestly, a complete multi-source inventory with per-hook positive controls, and
the one premise both the master and W1 had to assume was closed with live
captured payloads rather than inference.

Result: PASS
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
