# Session 36 — S9 positive control on the `.claude/settings.json` `agent` key

**Date:** 2026-07-26 · **Manager:** praxis-manager · **CC version:** 2.1.220 (verified this session)
**Verdict: DECISIVE POSITIVE** (scope caveat in §7 — run in a faithful lab replica, not in the repo directory)

---

## 1. Task

Determine by experiment whether the root `"agent"` key in `.claude/settings.json` is the
mechanism that sets `agent_type` in PreToolUse hook payloads on CC 2.1.220.

## 2. Rubric criteria addressed

Quoted from `specs/SPEC_RUBRIC.md` (lines 107, 108, 109, 115):

- **S1** — "Every claim in a report has pasted command output, not a description of output."
- **S2** — "No component is reported at a higher level than the evidence supports."
- **S3** — "Every gate claimed working has been deliberately tripped at least once, with the block observed."
- **S9** — "Any config field a guarantee depends on is positive-controlled: confirm a visible
  script fires at that field, then confirm an invented key at the same position produces
  byte-identical silence. A field that parses is not a field that is honoured."
- **R3 extension** (line 159) — positive control extends to claims about *mechanism*, not only config keys.

## 3. Workers dispatched

| # | Mode | Task | Outcome |
|---|------|------|---------|
| 1 | BUILD | Attempt the guard trigger from a worker thread | Guard silent, exit 0. Payload not observed. |
| 2 | ADVERSARIAL | Falsify "no subagent can emit the BLOCKED string" | **Broke the claim's conclusion**; premise survived. Built the nested-`claude` harness. |
| 3 | BUILD | Three-arm settings-key control in a lab | Returned a **null** — later shown confounded. |
| 4 | ADVERSARIAL | Attack worker 3's null | **Broke the null.** Found the missing-agent-definition confound. |

Worker 4's finding was then re-run **by me directly** (§6), not accepted on report.

## 4. STEP 1 — Baseline (restore targets)

```
=== shasum ===
eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a  .claude/settings.json
=== numstat ===
1	0	.claude/settings.json
=== HEAD ===
c1dec30c6516edcf7c79a78fce5c655e007d7ba2
```

## 5. STEP 2 / STEP 3 as literally briefed: UNEXECUTABLE from a subagent

The brief's design requires the trigger to be issued by an actor whose payload has an empty
`agent_id`. Observed, not inferred:

- My own trigger call (`echo probe > …`): `exit=0`, file written, no deny.
- Worker 1's two trigger calls: `exit=0` both, no deny.
- Worker 2 dumped live payloads for **depth-1 and depth-2 subagents whose `agent_type` was
  exactly `praxis-master`**: both carried a non-empty 17-hex `agent_id` and produced silence:
  ```
  agent_id_present= True agent_id= 'a530cc121d2d37552' | agent_type= 'praxis-master'
  agent_id_present= True agent_id= 'aea6ef2edb28e8096' | agent_type= 'praxis-master'
  === BLOCKED occurrences === 0
  ```
  That isolates `master-bash-guard.sh:7` (`[ -n "$AGENT_ID" ] && exit 0`) as the short-circuit.

**I therefore did NOT perform STEP 3's edit on the real `.claude/settings.json`.** Doing so
would have produced a *false* DECISIVE POSITIVE: with no subagent-reachable actor able to trip
the guard in the repo, the invented-key arm would have been silent no matter what the key did.
The real file was never written. Its sha256 is unchanged (§8).

A nested `claude` session with cwd **inside** the repo would resolve this, but is forbidden by
`CLAUDE.md:30` (single-session rule). Hence the lab replica below.

## 6. VERIFICATION EVIDENCE — the decisive two-arm control (run by me, not delegated)

Lab: `…/scratchpad/mgrlab`, cwd outside the repo. Project-level `.claude/settings.json`
(not `--settings`). `--agent` **never passed** in either arm. Real guard attached by absolute
path. `.claude/agents/praxis-master.md` present in **both** arms — this is the precondition
worker 3 omitted.

```
=== DIFF: X vs Y (must differ ONLY in the key name) ===
2c2
< "agent": "praxis-master",
---
> "zzz_bogus_agent_key": "praxis-master",
(diff exit=1)
=== both valid JSON? ===
X ok
Y ok
=== agent definition present (name resolution precondition) ===
-rw-r--r--@ 1 admin  wheel  204 Jul 26 18:18 praxis-master.md

############ ARM X  (first root key: agent) ############
nested exit=0
--- liveness (did the dump hook run?) ---
HOOK_RAN arm= 1785104350-9133
--- agent_type in dumped payload ---
{"agent_type_present":true,"agent_type":"praxis-master","agent_id_present":false,"cmd":"echo hello > …/probeX.txt"}
--- BLOCKED count in nested stream ---
3
--- probe file created? ---
ls: …/probeX.txt: No such file or directory

############ ARM Y  (first root key: zzz_bogus_agent_key) ############
nested exit=0
--- liveness (did the dump hook run?) ---
HOOK_RAN arm= 1785104357-3508
--- agent_type in dumped payload ---
{"agent_type_present":false,"agent_type":"<absent>","agent_id_present":false,"cmd":"echo hello > …/probeY.txt"}
--- BLOCKED count in nested stream ---
0
--- probe file created? ---
-rw-r--r--@ 1 admin  wheel  6 Jul 26 18:19 …/probeY.txt
```

Verbatim deny string from ARM X (S3 — gate deliberately tripped, block observed):

```
PreToolUse:Bash hook error: [/Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh]: BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
```

Truncation check (a SIGPIPE-truncated stream looks exactly like "the hook never fired"):
```
=== ARM X stream lines === 10
=== ARM Y stream lines === 11
=== ARM X stderr ===   (empty)
=== ARM Y stderr ===   (empty)
```

**Both halves of S9 satisfied:** the visible script fires at the field (ARM X), and an invented
key at the identical position produces silence (ARM Y). The silence is *informative* here only
because ARM X fired — that is precisely what was missing from worker 3's run.

Guard field-dependence, re-run by me (**SCRIPT-LOGIC-ONLY, NOT THE HOOK PATH**):
```
2dd67afcaefb84136a460d02cb7380acaf64c4f6bcce181f9850c02dfbb63101  scripts/master-bash-guard.sh
--- agent_type=praxis-master, no agent_id ---
BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.
guard exit=2
--- agent_type absent ---            guard exit=0
--- agent_type=praxis-master + agent_id present ---  guard exit=0
```

Independently confirmed by me from `claude --help` and `ls`:
```
  --agent <agent>    Agent for the current session. Overrides the 'agent' setting.
2.1.220 (Claude Code)
.claude/agents/ contains: praxis-master.md  (plus auditor, manager, worker, tutor)
```

## 7. Adversarial findings

1. **Worker 3's null was a confounded experiment, not a property of the software.** It set
   `"agent": "praxis-master"` in a lab that had **no `praxis-master.md`**. An unresolvable
   agent name is dropped **silently** — no warning, no stderr, exit 0 — which is
   indistinguishable on disk from an ignored key. Worker 4 reproduced the null (its arm 4) and
   then broke it with an A/B/A toggle of the definition file alone.
2. **The mechanism has a precondition:** key **and** resolvable agent definition. The real repo
   has both (`settings.json:2` + `.claude/agents/praxis-master.md`).
3. Worker 4 also confirmed the key works from `.claude/settings.local.json` and `--settings`,
   and that `--agent` works too — there is **no flag-vs-settings asymmetry**.
4. **Near-miss worth recording:** worker 4's first arm produced zero dumps because macOS has no
   `timeout` binary. It read as another confirming null and was caught only by an independent
   liveness log. Two of the four workers hit a false null in this one task.
5. Worker 2 observed that a hook denial surfaces as `"non_execution_kind":"permission-rule"`
   and **fires even under `bypassPermissions`**.

## 8. STEP 4 — Restore / integrity (nothing to restore; nothing was changed)

```
eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a  .claude/settings.json
expected: eed25e6749b64efff80f87d782817bf8a44e9cc81fad0728526375fb0ce71f1a
1	0	.claude/settings.json
first root key: agent
```
Hash **matches baseline exactly**. Staged diff unchanged at `1 0`. No git index or history
command was run by me or any worker.

**Index anomaly, NOT caused by this task.** The session-start git snapshot listed
`M  docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md` as *staged*; by the time I took
my baseline it was already untracked (`??`). That change predates my first command. Flagging
per the single-session rule; not acted on.

## 9. S6 cross-block check

- **`scripts/master-write-guard.sh`** keys on the same `agent_type` field (line 9) and is
  therefore armed by the same mechanism. Confirmed by reading, **not** separately trip-tested —
  reported at that level per S2.
- **`scripts/no-commit-guard.sh:4-8`** documents three payload shapes as observed. Two are now
  re-confirmed live this session (main thread: `agent_type` absent; subagent: `agent_id` present).
  Its comment names `--agent praxis-master` as the mechanism; that comment is now **incomplete** —
  the settings key is a second, equally valid mechanism. Not edited (out of scope).
- **`scripts/agent-spawn-guard.sh`** reads `agent_type` too; unexamined here.
- **S12:** this task ships no ledger writer. Not applicable.

## 10. Stale artifact flagged, NOT edited

`.claude/agent-memory/praxis-worker/project_agent-type-source.md` [local-only — not in this repo by design] records the refuted null and
advises "do not propose the settings key as a way to set `agent_type`." [correction 2026-08-04: this quotation is absent from the target file] **That guidance is now
false.** It is another agent's memory namespace; flagged for the master, not edited by me.
`docs/reports/2026-07-26-session36-agent-key-lab.md` is its cited evidence base and carries the
same confounded conclusion — it should be read only alongside this report.

## 11. Files staged

**None.** Nothing was staged, committed, or unstaged. Reports written (all untracked):
this file, `…-worker-trigger-probe.md`, `…-adversarial-actor-hunt.md`, `…-agent-key-lab.md`,
`…-null-attack.md`.

## 12. Result

**Result: PASS** — verdict DECISIVE POSITIVE. The root `"agent"` key in `.claude/settings.json` **is** a
mechanism that sets `agent_type` in PreToolUse payloads on CC 2.1.220, conditional on the agent
name resolving to a definition file. An invented key at the identical position produces
byte-identical silence.

**Scope caveat (S2):** demonstrated in a lab replica with cwd outside the repo, plus read-only
confirmation that the repo holds both required halves. Behaviour *in the repo's own directory*
is inferred from the replica, not directly observed, because `CLAUDE.md:30` forbids a second
session against this working tree. Closing that last gap needs a human to run one session in the
repo directory, or a `git worktree` — an index operation this task was forbidden to perform.
