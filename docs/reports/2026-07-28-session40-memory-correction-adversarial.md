# Session 40 — Adversarial audit: worker memory correction-in-place

**Mode:** ADVERSARIAL (read-only except this report)
**Date:** 2026-07-28
**Artifact:** `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/project_commit-guards-block-scratch-repos.md`
plus its index `/Volumes/Sensidine/Praxis.build/.claude/agent-memory/praxis-worker/MEMORY.md`

---

## Criterion

Human ruling dated 2026-07-28:

> correct the false worker memory IN PLACE ... the file must OPEN by naming the claim it previously
> carried and marking it refuted. ... removing the file would erase both the false claim AND the
> record that an agent briefed read-only wrote to the working tree anyway.

Graded as four independent sub-tests C1–C4, then a residual-defect hunt, then one mandatory liveness check.

---

## Sub-tests

### C1 — Does the file OPEN by naming the specific prior claim and marking it refuted? **PASS**

The first body content after the YAML frontmatter, at lines 8–14, is:

```
# CORRECTION FIRST — READ BEFORE ACTING ON ANYTHING BELOW

**The claim this file previously carried is REFUTED.** It read, verbatim:

> "and this project's `no-commit-guard.sh` still correctly blocks a worker from
> committing in the REAL repo through any route (that part of its purpose is
> intact; only the scratch-repo false-positive is being routed around)."
```

No substantive content precedes it. The frontmatter `description:` (line 3) also leads with
`CORRECTED — ... is REFUTED`, so even a reader who treats frontmatter as content hits the correction
first. Strict "opens" test satisfied.

### C2 — Is the record preserved that an agent briefed READ-ONLY wrote to the tree anyway? **PASS (thin)**

Lines 16–20:

```
That sentence is preserved here rather than deleted, because it is both the false
claim and the record that it was written into a durable, auto-loaded directory by
an agent that had been briefed **read-only**. Correction-in-place is this
project's sanctioned pattern; deletion would erase the incident along with the
error.
```

The directory is in the working tree and untracked, so "wrote to the working tree" is accurate:

```
$ git status --porcelain -- .claude/agent-memory/
?? .claude/agent-memory/
```

Verdict PASS. Noted as **thin**, not failing: the file records *one* such agent. The manager-side
memory records two separate incidents —
`.claude/agent-memory/praxis-manager/feedback_workers_write_to_agent_memory.md:11-15`:

```
**Why:** it has now happened twice. In session 36 an adversarial worker briefed
read-only wrote a memory file anyway, planting a false universal negative
("`no-commit-guard.sh` blocks a worker committing in the REAL repo through any
route") plus an evasion recipe. In session 38 the BUILD worker on
`Praxis_build-jcw`, told to write only to the scratchpad, edited that same file
```

The audited file does not carry the second incident. The criterion asks only that the record be
preserved, and it is.

### C3 — Is the false claim still legible (preserved, not deleted)? **PASS**

Quoted verbatim in a blockquote at lines 12–14 (reproduced under C1), and again referenced at line 46
(`universal negative ("through any route") asserted from a static read`). Nothing was excised.

### C4 — Does `MEMORY.md`'s index line restate the false claim, or carry the correction? **PASS**

```
$ grep -rn "any route" /Volumes/Sensidine/Praxis.build/.claude/agent-memory/
.../praxis-worker/MEMORY.md:4:- [Commit guards are a tripwire, not a barrier](project_commit-guards-block-scratch-repos.md) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted
.../praxis-worker/project_commit-guards-block-scratch-repos.md:3:description: CORRECTED — this file's original claim that no-commit-guard.sh blocks a worker commit "through any route" is REFUTED by measurement; ...
.../praxis-worker/project_commit-guards-block-scratch-repos.md:13:> committing in the REAL repo through any route (that part of its purpose is
.../praxis-worker/project_commit-guards-block-scratch-repos.md:36:no "any route" coverage and there never was — the guards key on command text, and
.../praxis-worker/project_commit-guards-block-scratch-repos.md:46:universal negative ("through any route") asserted from a static read.
```

The index line carries the correction and explicitly marks the old claim refuted. It does not restate
it as true. PASS. (The index line's own wording is itself defective — see R2.)

**C1–C4: four PASS.** The ruling's structural requirements are met.

---

## Residual defect hunt

The artifact contains no pasted command output anywhere — its entire evidentiary basis is a
six-row exit-code table. I reconstructed that table's basis from the guard sources and re-ran three
of the four guards directly. `gate-commit.sh` was **deliberately not executed**: line 151 runs
`find "$STATE" -name 'audit-pass-*' -mmin +30 -exec rm -f {} +` against `.claude/state`, and line 170
runs `git write-tree`. Executing it would have violated my read-only brief. Its column below is
source-read, not measurement.

### R1 — FALSE universal negative. Type (a). **The correction replaced one universal negative with another.**

Artifact, lines 35–37:

> So: **no route claim holds.** A quoted subcommand is gated by *nothing*. There is
> no "any route" coverage and **there never was** — the guards key on command text, and
> text is trivially re-spelled.

"there never was" is false. Before bead 587 (2026-07-12), `gate-commit.sh` matched with a bare
`*git*commit*` glob and nothing else — no quote-scrub, no command-position anchor. The narrowing that
*created* the quoted-subcommand hole is visible in the diff:

```
$ git -C /Volumes/Sensidine/Praxis.build log --oneline --date=short --pretty='%h %ad %s' -- '.claude/hooks/gate-*'
8a872d9 2026-07-12 Praxis_build-587: gate form-check anchors tip-write matcher at command position (BINPRE path/backslash prefix), 27/27 gate tests. ...
fec1722 2026-07-10 Praxis_build-v6y: gate hardening — token binds staged tree (write-tree), strict single-use consumption, one-session-per-repo denial. ...
291826f 2026-07-08 Orchestrator scaffold self-install + Jul 6 ledger reconciliation
```

Diff of 8a872d9 (dumped to scratchpad and read; excerpt):

```
-# The commit match is deliberately broad (`*git*commit*`): it also catches
-# `git -C <dir> commit`, `git --work-tree=... commit`, and chained forms
...
 case "$CMD" in
-  *git*commit*) ;;
+  *git*commit*) ;;   # cheap pre-filter only; precise command-position check below
   *) exit 0 ;;
 esac
+SCRUB=$(printf '%s' "$CMD" | sed -e "s/'[^']*'//g" -e 's/"[^"]*"//g')
+ANCHOR='(^|[;&|(`])[[:space:]]*'
...
```

Running the artifact's own six table rows through the reconstructed pre-587 matcher:

```
$ bash <scratchpad>/globtest.sh
pre-587 gate-commit exit=2   for: git commit -m "x"
pre-587 gate-commit exit=2   for: git 'commit' -m "x"
pre-587 gate-commit exit=2   for: git "commit" -m 'x'
pre-587 gate-commit exit=2   for: "git" commit -m 'x'
pre-587 gate-commit exit=0   for: git com'mit' -m 'x'
pre-587 gate-commit exit=2   for: git -C . commit
```

Three of the artifact's four "quoted subcommand" rows were gated by `gate-commit.sh` before
2026-07-12. Coverage existed; it was removed by a deliberate hardening change sixteen days before the
measurement. The correct scoped claim is: *as of the current script text (post-8a872d9), a quoted
subcommand is not matched by any of the four Bash-matcher hooks.*

This is the exact failure mode the artifact cites against itself at lines 44–46
(`[[scoped-hedge-vs-universal-negative]] — the original error here was exactly a universal negative`).
The file diagnoses the disease in its own final paragraph and then reproduces it two paragraphs earlier.

**What would settle it:** the pasted output above already does.

### R2 — Summary line inconsistent with its own table. Type (c). The `master-bash-guard` column is vacuous.

Frontmatter line 3 and `MEMORY.md` line 4 both say **"bypasses all four Bash PreToolUse hooks."**
The table's `master-bash-guard` column is `0` in **every** row — including the plain `git commit` row.
A hook that returns 0 for the gated form was never a commit gate; there is nothing there to "bypass".
Counting it inflates the apparent hole from three real commit gates to four.

Source confirms it never inspects commit syntax at all — `scripts/master-bash-guard.sh:12` matches
shell redirection / in-place edits only, and lines 7–8 scope it to the main-thread `praxis-master`:

```
[ -n "$AGENT_ID" ] && exit 0
[ "$AGENT" = "praxis-master" ] || exit 0
...
if echo "$CMD" | grep -qE '(^|[^>])>{1,2}[[:space:]]*[^&]|(^|\s)(sed|tee|patch|dd)\s+.*-i|\bcat\s*<<'; then
```

Measured against a **plain-form** commit under three different identities — never gates:

```
p1_plain_noagent   no-commit-guard=0  master-bash-guard=0  opsera=2
p2_plain_worker    no-commit-guard=2  master-bash-guard=0  opsera=2
p5_plain_master_mainthread: no-commit-guard=0  master-bash-guard=0  opsera=2
```

**Settles it:** the above. Honest wording is "all three Bash hooks that gate commits", or
"all four Bash-matcher hooks, one of which never gated commits in the first place".

### R3 — The table presents as a function of command form what is actually a function of payload identity. Type (b)+(c).

The artifact's table has one independent variable, `command form`. Measured, that is wrong for the
`no-commit-guard` column. `scripts/no-commit-guard.sh:16,18` short-circuit on identity before the
command text is ever read:

```
[ -z "$AGENT" ] && exit 0
[ "$AGENT" = "praxis-master" ] && [ -z "$AGENT_ID" ] && exit 0
```

So the table's row-1 cell `no-commit-guard = 2` for plain `git commit` holds **only** for a subagent
payload. With no `agent_type` (the shape that script's own comment block calls "plain session main
thread"), or with main-thread `praxis-master`, the same command form returns **0**:

```
$ for p in p1_plain_noagent p2_plain_worker p3_quoted_worker p4_dashC_worker; do ... done
p1_plain_noagent   no-commit-guard=0  master-bash-guard=0  opsera=2
p2_plain_worker    no-commit-guard=2  master-bash-guard=0  opsera=2
p3_quoted_worker   no-commit-guard=0  master-bash-guard=0  opsera=0
p4_dashC_worker    no-commit-guard=0  master-bash-guard=0  opsera=0
(gate-commit.sh deliberately NOT executed: it rm -f's files under .claude/state and runs git write-tree)

$ p=p5_plain_master_mainthread
no-commit-guard=0
master-bash-guard=0
opsera=2
```

The artifact never states which `agent_type`/`agent_id` its synthetic payloads carried. As written the
table is **not reproducible** — a future agent replaying it from a non-subagent context gets a
different row 1 and will conclude the memory is wrong about everything, including the part that is right.

**Settles it:** the pasted matrix above. Fix is to add the payload identity as a stated precondition.

### R4 — Two of the four `2` cells depend on unrecorded external state. Type (b).

- `gate-commit.sh:59` — `[ -f "$STATE/orchestrator-active" ] || exit 0`. Disarmed, every gate-commit
  cell is 0.
- opsera `pre-commit-scan.sh:16-27` — returns 0 if `/tmp/.opsera-pre-commit-scan-passed` exists and is
  under 300 s old.

Both preconditions happen to hold right now, so the table reproduces *today*:

```
$ ls -la /Volumes/Sensidine/Praxis.build/.claude/state/orchestrator-active
-rw-r--r--@ 1 admin  staff  0 Jul 26 09:53 /Volumes/Sensidine/Praxis.build/.claude/state/orchestrator-active
$ ls -la /tmp/.opsera-pre-commit-scan-passed
ls: /tmp/.opsera-pre-commit-scan-passed: No such file or directory
```

Not a falsity — an unrecorded precondition on a durable, auto-loaded instruction. It will silently
stop being true.

### R5 — Hook-aggregation behaviour asserted as fact, no evidence. Type (b). **NOT OBSERVED.**

Artifact lines 74–76:

> Test each guard in a SEPARATE invocation: when two hooks both deny, only the last to finish
> surfaces its stderr, and that masking has already caused wrong diagnoses here.

This is a claim about the Claude Code hook runner's stderr aggregation across multiple denying
PreToolUse hooks, stated flatly. The file shows no transcript. I did not verify it — doing so requires
triggering a live double denial, which I judged out of scope for a read-only brief. Mark **UNVERIFIED**
in place, or attach the transcript that produced the "wrong diagnoses" it cites.
**Settles it:** a captured transcript of one Bash call denied simultaneously by two Bash-matcher hooks.

### R6 — Ambiguous-to-false sentence contradicted by the file's own row 6. Type (c).

> So: **no route claim holds.**

Parsed as written ("no route-claim holds"), the file's own table refutes it one row later: row 6
`git -C . commit` shows `gate-commit = 2`. Some routes *are* gated. The intended reading is presumably
"the 'any route' claim does not hold". In a file whose entire purpose is to stop an ambiguous absolute
from propagating, this sentence should not survive.

### R7 — Minor: index-line length and slug drift.

```
$ awk '{printf "%d chars: %s\n", length($0), substr($0,1,60)}' .../praxis-worker/MEMORY.md
193 chars: - [S9 positive-control harness](project_s9-positive-control-
147 chars: - [agent_type source](project_agent-type-source.md) — sett
172 chars: - [Scoped hedge vs universal negative](feedback_scoped-hedge
221 chars: - [Commit guards are a tripwire, not a barrier](project_comm
```

The corrected entry is 221 chars against a ~150-char index guideline (it is the longest of the four).
Also `name: commit-guards-block-scratch-repos` in frontmatter no longer matches the file's own
conclusion or its index title ("tripwire, not a barrier"). Keeping the filename is correct under
correction-in-place — renaming would break the incident record — but the `name:` slug and title now
disagree. Cosmetic; flagged, not weighted in the verdict.

### R8 — Loose but operationally correct. Type (b), no action needed.

> `.claude/hooks/gate-commit.sh` and `scripts/no-commit-guard.sh` are PreToolUse
> Bash hooks that inspect the raw command TEXT and key off `$CLAUDE_PROJECT_DIR` /
> the caller's `agent_type`/`agent_id` — neither checks which repo the command
> actually targets.

The "/" conflates two different scripts: `no-commit-guard.sh` reads only `agent_id`/`agent_type` and
never `CLAUDE_PROJECT_DIR`; `gate-commit.sh` reads `CLAUDE_PROJECT_DIR` (line 57) and never the agent
fields. I read both in full: **the operative conclusion is correct** — neither inspects cwd or the
command's target repo, so a scratch-repo commit denies identically. Verified by source read.

### R9 — Harness advice is true but incomplete in a way that can mislead. Type (b).

> The **`Write` tool is not matched by Bash-matcher hooks**

True as stated. But this repo registers a `Write|Edit|NotebookEdit` PreToolUse hook that the harness
section does not mention:

```
  event PreToolUse
    matcher= 'Bash'   -> "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh
    matcher= 'Bash'   -> "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh
    matcher= 'Write|Edit|NotebookEdit' -> "$CLAUDE_PROJECT_DIR"/scripts/master-write-guard.sh
    matcher= 'Bash'   -> "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh
    matcher= 'Agent'  -> "$CLAUDE_PROJECT_DIR"/scripts/agent-spawn-guard.sh
```

`scripts/master-write-guard.sh:8-16` denies main-thread `praxis-master` writes outside ledgers/specs/
reports. An agent reading "Write is not matched by Bash-matcher hooks" as "Write is a free path" would
be wrong for that identity. Not false; incomplete.

### Out-of-scope observation (reported, not acted on)

`.claude/agent-memory/praxis-manager/project_8sw_park_gate_boundary.md:31-35` carries an overlapping
guard map ("four PreToolUse hooks share matcher `Bash`") that was **not** in my audit scope and was not
graded here. If the ruling's correction is meant to be system-wide, that file should get the same
treatment. I did not touch it.

---

## Liveness check (mandatory, run not inferred)

**Claim under test:** an enabled `opsera-devsecops` plugin registers `pre-commit-scan.sh` as a Bash
PreToolUse hook from `~/.claude/plugins/`.

**1. Does the file exist?**

```
$ find ~/.claude/plugins -maxdepth 6 -iname '*pre-commit-scan*'
/Users/admin/.claude/plugins/cache/claude-plugins-official/opsera-devsecops/1.0.0/hooks/pre-commit-scan.sh
/Users/admin/.claude/plugins/cache/claude-plugins-official/opsera-devsecops/1.0.0/skills/pre-commit-scan
```

**2. Is it registered as a Bash PreToolUse hook?**
`/Users/admin/.claude/plugins/cache/claude-plugins-official/opsera-devsecops/1.0.0/hooks/hooks.json`:

```json
{
  "description": "Opsera pre-commit security gate — blocks git commits until a security scan passes",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/hooks/pre-commit-scan.sh" }
        ]
      }
    ]
  }
}
```

**3. Is the plugin enabled?** `/Users/admin/.claude/settings.json`:

```
$ grep -rn "enabledPlugins" -A 12 /Users/admin/.claude/settings.json
/Users/admin/.claude/settings.json:7:  "enabledPlugins": {
/Users/admin/.claude/settings.json-8-    "superpowers@claude-plugins-official": true,
/Users/admin/.claude/settings.json-9-    "context7@claude-plugins-official": true,
/Users/admin/.claude/settings.json-10-    "opsera-devsecops@claude-plugins-official": true,
/Users/admin/.claude/settings.json-11-    "n8n-mcp-skills@n8n-mcp-skills": true,
/Users/admin/.claude/settings.json-12-    "praxis-progress@praxis-local": true,
/Users/admin/.claude/settings.json-13-    "warp@claude-code-warp": true
/Users/admin/.claude/settings.json-14-  },
```

Installed at user scope, version 1.0.0 (`installed_plugins.json:23-32`).

**4. Does it actually deny?** Executed against a plain-form payload (safe: the `rm -f` branch is only
entered when the flag file exists, and it does not):

```
p1_plain_noagent   ... opsera=2
p2_plain_worker    ... opsera=2
p3_quoted_worker   ... opsera=0
p4_dashC_worker    ... opsera=0
```

**5. Corollary claim — "any inventory built by reading `.claude/settings.json` alone will miss it."**
Confirmed. The repo settings file has no `enabledPlugins` key at all:

```
=== /Volumes/Sensidine/Praxis.build/.claude/settings.json
  top-level keys: ['agent', 'env', 'hooks', 'permissions']
```

**6. Is "four" the right count?** Confirmed. Enumerating PreToolUse hooks across every enabled plugin:

```
=== .../claude-code-warp/warp/2.2.0/hooks/hooks.json
   SessionStart / Stop / Notification / PermissionRequest / UserPromptSubmit / PostToolUse / StopFailure   (no PreToolUse)
=== .../opsera-devsecops/1.0.0/hooks/hooks.json
   PreToolUse   matcher='Bash'   -> ${CLAUDE_PLUGIN_ROOT}/hooks/pre-commit-scan.sh
=== .../superpowers/6.2.0/hooks/hooks.json
   SessionStart matcher='startup|clear|compact'   (no PreToolUse)
```

Three repo Bash-matcher hooks + one plugin = **exactly four Bash-matcher PreToolUse hooks**.

**Liveness check verdict: the fourth-hook claim is TRUE and fully confirmed** — file present, plugin
enabled, `PreToolUse`/`Bash` registration, and observed exit 2. This is the strongest part of the
artifact. Note the count is correct but the *characterisation* of all four as commit gates is not (R2).

Also verified while here: the repo's only deny rule is `permissions.deny: ["Agent(general-purpose)"]` —
no Bash deny rule exists, so the permission layer does not independently gate commits. This *supports*
the artifact's "gated by nothing" for the present tense; R1 is a historical claim, not a present one.

---

## Files staged / written

**In the repository: exactly one — this report.**

- `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-28-session40-memory-correction-adversarial.md`

Nothing under `.claude/agent-memory/` was created, edited, appended to, or deleted. No `git add`, no
index operation, no edit to `.gitignore`, `.claude/settings.json`, `.claude/hooks/`, or `scripts/`.
`gate-commit.sh` was not executed, specifically to avoid its `rm -f` on `.claude/state` and its
`git write-tree`.

Disclosed for completeness — synthetic hook payloads and one test script written **outside the repo**
in the session scratchpad, used purely as tool input:
`p1_plain_noagent.json`, `p2_plain_worker.json`, `p3_quoted_worker.json`, `p4_dashC_worker.json`,
`p5_plain_master_mainthread.json`, `globtest.sh`, `diff587.txt` under
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/abd15179-18bf-47be-a6d8-8c15c68685f4/scratchpad/`.

---

## Verdict

**C1, C2, C3, C4 all PASS.** The correction-in-place satisfies every structural requirement of the
2026-07-28 ruling: it opens with the refutation, quotes the false claim verbatim, preserves the
read-only-write incident, and the index line carries the correction rather than restating the error.
If the criterion were only C1–C4, this would be a clean pass.

It is not a clean pass, because the residual hunt found the artifact reproducing the very defect it
exists to correct. **R1** is a false universal negative — "there is no 'any route' coverage and there
never was" — refuted by the artifact's own subject matter: before commit `8a872d9` (2026-07-12), three
of its four quoted-subcommand rows were gated by `gate-commit.sh`'s `*git*commit*` glob. That sentence
is now standing instruction to every future `praxis-worker`. **R2** puts the file's headline at odds
with its own table (`master-bash-guard` is 0 in every row and never gated commits at all, so "bypasses
all four" is inflated), and **R3** shows the table's plain-form `2` flips to `0` under two legitimate
payload identities the file never records, making it non-reproducible as written.

A memory file whose purpose is to stop a false absolute from propagating must not ship a new one.

VERDICT: FAIL
