# Session 34 — MANIFEST.md AMENDMENT ROW 3 (S13 registry entry)

Manager: praxis-manager. Date: 2026-07-26. Baseline HEAD: `c1dec30`.

## Task

Append exactly one row to `MANIFEST.md` — AMENDMENT ROW 3 for `/specs/SPEC_RUBRIC.md`,
registering the session-34 S13 + provenance change. Reproduce the master-supplied
row byte-exactly. Touch no other file. Do not commit. Do not stage. Leave in the
working tree.

Routed here because `scripts/master-write-guard.sh` denied the write to
`praxis-master`, verbatim:

```
BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/MANIFEST.md'.
```

That is the guard working as designed. Confirmed by controlled trip test below.

## Rubric criteria addressed

Read from `specs/SPEC_RUBRIC.md` before planning. All three exist verbatim; no
rubric gap.

- **S1** (line 107) — "Every claim in a report has pasted command output, not a description of output."
- **S2** (line 108) — "No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure."
- **S13** (line 119) — "No `WebSearch`, `WebFetch`, or `Task` in this repo."
- **S9** (line 115) applied to the guard trip test (invented-key control).
- **S3** (line 109) applied — the gate was deliberately tripped.

## Workers dispatched

| id | mode | scope | outcome |
|---|---|---|---|
| `aa61a0754e5113593` | ADVERSARIAL | Grade MANIFEST.md:118 — mechanical integrity, factual accuracy vs. staged rubric, S2 overclaim, scope creep, secrets | FAIL — 4 defects (1 major) |
| `a1efe9c75ba348c95` | ADVERSARIAL / negative trip test | Prove `master-write-guard.sh` actually denies praxis-master on MANIFEST.md; S9 invented-key control; fail-direction; cross-hook attribution | PASS — gate confirmed load-bearing |

Neither worker was given the other's reasoning. Neither was told how the edit was
produced. Both were read-only on the repo.

The edit itself (a single-line append) was performed by the manager directly, per
the single-line exception in the manager contract. Method: the row was written to
a scratchpad file and appended with `cat >>`, to avoid any editor-level
normalisation of the em-dashes, smart quotes and backticks in the row text.

## Process log

1. Read `specs/SPEC_RUBRIC.md` in full. Confirmed S1, S2, S13 present verbatim.
2. Read `MANIFEST.md` lines 100–117 and the table header at line 3. Confirmed
   three prior rows for `/specs/SPEC_RUBRIC.md` at 115, 116, 117.
3. Captured pre-state: 117 lines, 54762 bytes, ends with newline,
   sha256 `5c56d47f6f2f365de571b143cabb1fa67e91c25f000c61ebc5777b033c6fb070`.
4. Wrote the row verbatim to scratchpad `amendment-row-3.txt`, appended it.
   Post-state sha256 `4fa82511d929c5edc74ef9fa32d6711639d88f42344094ae803fc3d7b0d2abbd`.
5. Ran the four required verifications (below).
6. Dispatched two ADVERSARIAL workers concurrently.
7. Re-verified the two substantive worker findings independently (below) rather
   than relaying them.

## Verification evidence (pasted output only)

### Pre-state

```
$ python3 -c "d=open('MANIFEST.md','rb').read(); print('bytes:',len(d)); print('ends_with_newline:',d.endswith(b'\n')); print('last20:',repr(d[-20:]))"
bytes: 54762
ends_with_newline: True
last20: b' timestamp window |\n'

$ shasum -a 256 MANIFEST.md
5c56d47f6f2f365de571b143cabb1fa67e91c25f000c61ebc5777b033c6fb070  MANIFEST.md
```

### 1. `git diff --numstat MANIFEST.md`

```
1	0	MANIFEST.md
```

One line added, zero removed. No existing row edited.

### 2. `tail -c 400 MANIFEST.md`

```
 have. The section additionally carries a CORRECTION by append — `docs/reports/2026-07-25-agent-stack-install-filelayer.md:39` claims installing the key mid-session "would lock the session out", which is FALSE and was the stated reason the key was deferred; the key takes effect at session start only. Line not edited; correction rides in DECISION_LOG 2026-07-26T17:33Z and bead Praxis_build-6di |
```

### 3. `git status --short`

```
 M .claude/settings.json
M  AUDIT_LOG.md
MM DECISION_LOG.md
MM DISPATCH_LOG.md
 M MANIFEST.md
M  specs/SPEC_RUBRIC.md
?? .claude/agent-memory/
?? docs/reports/2026-07-26-session34-p0-flush-audit.md
```

`MANIFEST.md` is ` M` — worktree-modified, **not staged**. Correct.
`.claude/settings.json` is ` M` — **not staged**. Correct and unchanged by this unit.
The other five entries pre-dated this unit of work.

Independently confirmed by the adversarial worker:

```
$ git diff --cached --name-only
AUDIT_LOG.md  DECISION_LOG.md  DISPATCH_LOG.md  specs/SPEC_RUBRIC.md
```

Neither `MANIFEST.md` nor `.claude/settings.json` appears in the staged set.

### 4. Header row + appended row, column count

```
$ sed -n '3p;118p' MANIFEST.md
| File Path | Type | Phase | Date Created | Purpose |
| /specs/SPEC_RUBRIC.md | Spec | 0 | 2026-07-26 | AMENDMENT ROW 3 (append-only registry — supersedes all three earlier rows for this path). Session-34 adds standing criterion **S13**: no `WebSearch`, `WebFetch` or `Task` on the main thread in this repo. This is a STANDING CONSTRAINT, NOT A DEFECT — the main thread is bound to the `praxis-master` definition by the top-level `"agent"` key in `.claude/settings.json` (installed by Amear's hand, local, uncommitted, machine-specific BY INTENT and never staged), and that definition's grant omits all three. The failure mode S13 guards against is a future session reading the absence as breakage and "repairing" it by widening the grant or pulling the key. Work needing web research is dispatched to a subagent whose own definition grants the tool, or handed to Amear. Also adds the S13 PROVENANCE section recording Amear's three-point S9 positive control — no key = 29 tools with both fetch tools present; key installed = 10 tools with both absent, matching praxis-master's grant; key renamed to `agentX` = 29 tools and both return — the third arm being the invented-key control S9 requires, which is what makes the key NAME load-bearing rather than incidental. EVIDENCE IS RELAYED, NOT REPRODUCED: Amear ran that control; the build side did not re-run it and does not claim to have. The section additionally carries a CORRECTION by append — `docs/reports/2026-07-25-agent-stack-install-filelayer.md:39` claims installing the key mid-session "would lock the session out", which is FALSE and was the stated reason the key was deferred; the key takes effect at session start only. Line not edited; correction rides in DECISION_LOG 2026-07-26T17:33Z and bead Praxis_build-6di |

$ awk 'NR==3||NR==118{n=gsub(/\|/,"|"); print "line "NR": pipes="n"  columns_between="n-1}' MANIFEST.md
line 3: pipes=6  columns_between=5
line 118: pipes=6  columns_between=5

$ wc -l MANIFEST.md
     118 MANIFEST.md
```

5 columns, matching the header. No stray `|` inside the description.

### Byte-exactness and encoding (adversarial worker `aa61a0754e5113593`)

```
$ diff <(sed -n '118p' MANIFEST.md) .../amendment-row-3.txt
DIFF_EXIT=0

$ tail -c 20 MANIFEST.md | xxd
00000010: 6920 7c0a                                i |.

$ grep -c $'\r' MANIFEST.md
0

$ file MANIFEST.md
MANIFEST.md: Unicode text, UTF-8 text, with very long lines (1723)
```

Byte-identical to the intended text. Last line of file. Exactly one trailing
newline. No CRLF introduced. Em-dashes and smart quotes preserved.

### Secrets scan (adversarial worker)

```
$ grep -oE '(https?://|/Users/|/Volumes/|sk-|token|secret|password|api[_-]?key|[A-Za-z0-9+/]{32,}=*)' <line 118>
(exit 1 — no matches)
```

None. All paths in the row are repo-relative.

## Negative test — the gate actually blocks (S3, S9)

Worker `a1efe9c75ba348c95`, by direct stdin invocation of
`scripts/master-write-guard.sh` (attribution unambiguous — no other hook was in
the path).

Registration: `.claude/settings.json` lines 71–80, `PreToolUse`, matcher
`Write|Edit|NotebookEdit`. Fields the script actually reads, read from the
script, not inferred: `.agent_id` (any non-empty value ⇒ `exit 0`),
`.agent_type` (must equal `praxis-master` or `exit 0`),
`.tool_input.file_path // .tool_input.path`. **`.tool_name` is never read** —
tool filtering is done entirely by the settings matcher.

**Positive trip.** caller `praxis-master`, path `/Volumes/Sensidine/Praxis.build/MANIFEST.md`:

| case | exit | stderr bytes |
|---|---|---|
| Write | **2** | 142 |
| Edit | **2** | 142 |
| NotebookEdit | **2** | 142 |

```
BLOCKED: praxis-master may only write ledgers, specs, and reports. Dispatch praxis-manager for '/Volumes/Sensidine/Praxis.build/MANIFEST.md'.
```

`cmp` against the master-reported block string: **byte-identical**, both
sha256 `199babf7ed980961e596b2c8df9dbc446f8cc745245da940448cd099b342b9bc`,
142 bytes = 141 message + trailing `0a`. Zero character-level differences.

**Negative control A** — caller `praxis-manager`, same path: exit 0, 0 B stdout,
0 B stderr. Also `praxis-worker`: exit 0. Also `praxis-master` **with `agent_id`
present** (i.e. a *spawned* master rather than the main thread): exit 0.

**Negative control B** — caller `praxis-master`, allowed paths
`DECISION_LOG.md`, `DISPATCH_LOG.md`, `ISSUE_REGISTER.md`, `HANDOFF.md`,
`STATUS.md`, `specs/SPEC_RUBRIC.md`, `docs/reports/x.md`: all exit 0, silent.
Denied for contrast: `CLAUDE.md` exit 2, `src/thing.cs` exit 2.

**S9 invented-key control.** Payloads differ by exactly one inserted byte
(`diff` on the char stream: `63a64 > X`):

| key | exit | stderr |
|---|---|---|
| `agent_type` | **2** | 142 B |
| `agent_typeX` | **0** | 0 B |

Byte-identical silence at the same position. `.agent_type` is genuinely
load-bearing. Supplementary: `file_pathX` ⇒ exit 0 silent (the path read is also
load-bearing, which closes the fall-through risk); `agent_idX` ⇒ still exit 2
(correctly not read); `tool_namez` ⇒ still exit 2 (confirms `.tool_name` is not
read).

**Fail direction — the guard fails OPEN, in every case.** Not "fail safe": it
allows. Empty stdin ⇒ 0. `</dev/null` ⇒ 0. Truncated JSON ⇒ 0 (leaks 130 B of
`jq: parse error` to stderr). Non-JSON ⇒ 0 (106 B `jq: parse error`).
`agent_type` absent / `""` / `null` ⇒ 0. `file_path` absent / `""` /
`tool_input` absent ⇒ 0. This matches the direction already recorded for
`agent-spawn-guard.sh` in the rubric's R3 note, item 2.

## S6 cross-block check

The change is one append to an append-only file registry. It touches no block
spec, no signal path, no breaker, no NinjaScript, no n8n workflow, no launchd
job. Blocks 1–5 are unaffected.

The two consumers of `MANIFEST.md` are `CLAUDE.md:14` (the rule that mandates a
row when a file is modified — satisfied by this row) and the auditor, which reads
the registry to check that shipped files are declared. Neither is regressed: the
table structure is unchanged (5 columns), the append-only property is preserved
(0 deletions), and the row's supersession semantics match the convention already
established at lines 115–117.

One adjacent gap observed, out of scope, not repaired, reported here so it is not
lost: `docs/reports/2026-07-26-session34-p0-flush-audit.md` is untracked and has
no `MANIFEST.md` row. That is a separate `CLAUDE.md:14` obligation belonging to
whoever created it.

## Adversarial findings

Worker `aa61a0754e5113593` returned FAIL with four defects. All four are in the
**content of the row**, which the brief required to be reproduced byte-exactly.
None is a defect in the execution. Two were re-verified by the manager directly
rather than relayed; the raw output is below.

### D1 (MAJOR, S2) — "that definition's grant omits all three" is not supported for `Task`

```
$ grep -n '^tools:' .claude/agents/praxis-master.md
8:tools: Agent(praxis-manager, praxis-auditor, praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite, AskUserQuestion

$ grep -rn '\bTask\b' .claude/agents/ .claude/settings.json specs/SPEC_RUBRIC.md | grep -v 'Sections:' | grep -v 'Task /'
specs/SPEC_RUBRIC.md:119:| S13 | **No `WebSearch`, `WebFetch`, or `Task` in this repo.** ...
```

`Task` appears nowhere in this repo as a tool name. The repo's own vocabulary for
the subagent-spawn tool is `Agent` — the `PreToolUse` matcher is `"Agent"`,
`permissions.deny` carries `Agent(general-purpose)`, S10 says `` `Agent(<type>)` ``,
S11 says "receives no `Agent` tool at all". Two readings, both defective:

- If `Agent` is the current name for the tool formerly called `Task`, then
  "grant omits all three" is **false** — the main thread holds it, and must, since
  dispatching the manager is praxis-master's entire function.
- If `Task` is a distinct tool absent from this build, the clause is vacuous, and
  asserting it as an observed property of the grant overstates.

Decisively: the relayed three-point control measured **only** `WebFetch` and
`WebSearch` (the rubric's own words: "29 tools with `WebFetch` and `WebSearch`
present … both absent"). **No control was ever run for `Task`.** The row states
all three as verified.

### D2 (MODERATE) — scope qualifier not in the criterion text

Rubric S13 headline reads "No `WebSearch`, `WebFetch`, or `Task` **in this
repo**." The MANIFEST row reads "no `WebSearch`, `WebFetch` or `Task` **on the
main thread** in this repo." The qualifier is inferable from S13's body but is
not in its headline, and the narrowing lands exactly where D1 bites.

### D3 (MODERATE) — the "10 tools" figure is unreconciled

```
$ grep '^tools:' .claude/agents/praxis-master.md | sed 's/^tools: //' | sed 's/Agent([^)]*)/Agent/' | tr ',' '\n' | sed 's/^ *//' | grep -n .
1:Agent
2:Read
3:Grep
4:Glob
5:Bash
6:Write
7:Edit
8:TodoWrite
9:AskUserQuestion
```

The row says "key installed = 10 tools with both absent, **matching
praxis-master's grant**." The on-disk grant enumerates **9**. Off by one,
unexplained. A reconciling explanation is easy to imagine (an implicit tool not
declared in frontmatter) — but imagining one is inference, and 10-vs-9 is exactly
the class of config-derived number S9 exists to positive-control.

### D4 (MINOR) — "and never staged" is unverifiable in form

The phrase is a MANIFEST-only addition; the rubric says only "local and
uncommitted, machine-specific by intent." Currently true —
`git log --oneline -S'"agent"' -- .claude/settings.json` returns nothing — but
index history is not reconstructible, so "never" cannot be evidenced.

### Claims independently confirmed TRUE

```
$ git diff --cached --numstat specs/SPEC_RUBRIC.md
16	0	specs/SPEC_RUBRIC.md

$ python3 -c "import json;d=json.load(open('.claude/settings.json'));print('keys:',list(d.keys()));print('agent:',d.get('agent'))"
keys: ['agent', 'env', 'hooks', 'permissions']
agent: praxis-master
```

S13 exists in the standing-criteria table at line 119 and names all three tools.
"Standing constraint, not a defect" is verbatim. The top-level `agent` key exists
and is `praxis-master`. The "S13 — provenance" section exists and carries the
29 / 10 / 29 three-point control and the `agentX` rename. The corrected claim is
at **exactly** line 39 of the filelayer report. `DECISION_LOG` 17:33Z rows exist.
Bead `Praxis_build-6di` exists and is P3. Exactly three prior rows for this path
(115, 116, 117), so "supersedes all three earlier rows" is correct. The staged
rubric diff is +16/-0, matching the brief.

### Where these defects originate — and why they were not fixed here

D1, D2 and D3 are faithful reflections of `specs/SPEC_RUBRIC.md:119` and its
provenance paragraph. The MANIFEST row is an accurate registry entry for an
upstream text that itself contains the overclaim. Two constraints bar repair from
here:

1. `specs/SPEC_RUBRIC.md` line 3: "Authority: the scoping agent (Claude.ai) via
   Amear. **The build side does not edit this file.** It proposes changes; Amear
   applies them."
2. The brief required byte-exact reproduction of a master-authored row. Editing
   it would be the manager authoring an acceptance-relevant claim — precisely
   what the manager contract forbids ("An acceptance bar authored by the party
   being graded is not an acceptance bar").

So the row stands as written, unstaged, and the finding escalates rather than
being silently absorbed. Per S8, the question that settles D1 and D3 is Amear's,
not the build side's: **does the 10-tool observation from the positive control
include `Agent`, and is `Task` a live tool name in that CLI version at all?**
Both defects close on that single output.

## Files staged

None. By instruction.

Files left modified in the working tree by this unit of work:

- `/Volumes/Sensidine/Praxis.build/MANIFEST.md` — +1 line, −0 lines, unstaged.

`.claude/settings.json` was not touched and remains unstaged.

## Adjacent findings from the trip test — reported, not repaired

Surfaced by the negative-test worker while instrumenting
`scripts/master-write-guard.sh`. Out of scope for this unit; recorded so they are
not lost.

1. **`AUDIT_LOG.md` is DENIED to praxis-master** (exit 2) despite being a ledger
   the master flushes, and despite being staged right now. The `case` allowlist
   omits it. Likely a real gap.
2. **Path-traversal bypass.** `*/specs/*` and `*/docs/reports/*` match anywhere
   in the string, so `…/specs/../MANIFEST.md` ⇒ exit 0, as does
   `/docs/reports/../../../MANIFEST.md`. Whether the harness normalises
   `file_path` before the hook sees it is **UNVERIFIED** — settling it requires a
   real repo write, which was out of scope.
3. **Suffix-only match.** `FAKE_STATUS.md` and `xDECISION_LOG.md` both ⇒ exit 0.
4. `docs/agent-spawn-guard.md:68` states `.claude/settings.local.json` does not
   exist. It does (contains `permissions.allow` only, no `hooks` key). Stale;
   does not change that document's conclusion.

## Evidence-provenance note (manager contract, item 6)

Everything asserted about the guard in this report was **observed in this
session** by direct stdin invocation with captured exit codes and byte counts —
not read off the script. The one place the evidence is weaker than the claim is
stated plainly: **no live `Write`/`Edit` `PreToolUse` payload has ever been
captured in this repo**, so `.tool_input.file_path` rests on the tool schema plus
the `file_pathX` S9 control rather than on an observed envelope. `.agent_type`
and `.agent_id`, by contrast, are observed live in
`docs/reports/2026-07-25-agent-stack-install.md:279-293` and `:505-520` and
`docs/reports/2026-07-26-agent-stack-v2-triptests.md:995-1022`.

Cross-hook interference was ruled out rather than assumed: only one `PreToolUse`
entry matches `Write` (`Write|Edit|NotebookEdit → master-write-guard.sh`); the
other four are `Bash` ×3 and `Agent` ×1. `~/.claude/settings.json` has no `hooks`
key; managed-settings is absent; `.claude/settings.local.json` has no `hooks`
key. And since the script was invoked directly on stdin, attribution of the
142-byte message is unambiguous regardless.

## Result: FAIL — S2

The mechanical task is complete and verified: the row is byte-exact, appended at
the end, 5 columns, +1/−0, unstaged, nothing else touched, and the guard that
routed the work here is proven to actually block. Every one of those claims has
pasted output above (S1 satisfied).

It is nonetheless FAIL, not PASS, because **S2 was handed to this unit as an
acceptance criterion and the artifact does not meet it.** The row asserts that
praxis-master's grant "omits all three" and that the observed 10-tool count
matches that grant; the first is unsupported for `Task` and possibly false, the
second is off by one against the file. The row's own hedge — "EVIDENCE IS
RELAYED, NOT REPRODUCED" — is scoped to the three-point control and does not
reach either claim. Reporting a two-tool control as covering three tools is
reporting a component above the level its evidence supports, which is the exact
wording of S2.

Marking this PASS on the strength of the mechanical checks would be grading 4
of 5 criteria as 5. The criterion is not softened and the row is not edited.

**Escalated to praxis-master.** The row is left in place, unstaged, for the master
to decide. The decision is not the manager's to make, and the underlying question
belongs to Amear (S8): whether the 10-tool observation includes `Agent`, and
whether `Task` is a live tool name in that CLI version. If `Task` is simply the
former name of `Agent`, S13's own text at `specs/SPEC_RUBRIC.md:119` needs the
same correction — and only Amear may make it (rubric line 3).
