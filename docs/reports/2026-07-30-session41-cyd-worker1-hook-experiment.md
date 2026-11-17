# Session 41 — worker1 — Does a FOURTH `PreToolUse matcher=Bash` hook fire against this repo?

**Date:** 2026-07-30 · **Role:** praxis-worker · **Mode:** BUILD (experimental grading)
**Repo:** `/Volumes/Sensidine/Praxis.build` · **HEAD:** `c1dec30` (unchanged)
**Graded against:** `specs/SPEC_RUBRIC.md` S1, S2, S9 + ruling R3

## Task

Settle by experiment whether a fourth `PreToolUse matcher=Bash` hook exists and
fires against this repo, beyond the three registered in `.claude/settings.json`.

## Headline

A fourth registration **exists on disk** but **is never loaded**, therefore never
registered and never fires. The live Bash-matcher count is **3, not 4**.

The reason is not that the hook declines to match — it is that the plugin
carrying it fails to load: `opsera-devsecops` is installed and enabled but is
**absent from its marketplace**, so Claude Code never reads its `hooks.json`.

---

## 1. Re-verification at source

### 1.1 In-repo registrations

```
$ jq -r '[.hooks.PreToolUse[] | select(.matcher=="Bash")] | length' .claude/settings.json
3
```

```
$ jq -r '[.hooks | to_entries[] | .value[] | .hooks[]] | length' .claude/settings.json
13
```

Both match the manager's stated figures. The three commands:

```
$ jq -r '.hooks.PreToolUse[] | select(.matcher=="Bash") | .hooks[] | .command' .claude/settings.json
"$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh
"$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh
"$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh
```

### 1.2 Every settings layer that could contribute a fourth

```
$ for f in ~/.claude/settings.json ~/.claude/settings.local.json \
    <repo>/.claude/settings.json <repo>/.claude/settings.local.json \
    "/Library/Application Support/ClaudeCode/managed-settings.json" \
    /etc/claude-code/managed-settings.json; do ...; done
=== /Users/admin/.claude/settings.json
0
=== /Users/admin/.claude/settings.local.json
ABSENT
=== /Volumes/Sensidine/Praxis.build/.claude/settings.json
3
=== /Volumes/Sensidine/Praxis.build/.claude/settings.local.json
ABSENT
=== /Library/Application Support/ClaudeCode/managed-settings.json
ABSENT
=== /etc/claude-code/managed-settings.json
ABSENT
```

No settings layer other than the project file contributes a Bash matcher.

### 1.3 Plugins — Bash matchers across EVERY `hooks.json` on disk

I widened the manager's search from the six install paths to every `hooks.json`
anywhere under `~/.claude/plugins` (20 files):

```
$ find /Users/admin/.claude/plugins -name 'hooks.json' | sort | while read f; do
    n=$(jq -r '[(.hooks.PreToolUse // [])[] | select((.matcher // "")|test("Bash"))] | length' "$f"); echo "$n  $f"; done
0  /Users/admin/.claude/plugins/cache/claude-code-warp/warp/2.1.0/hooks/hooks.json
0  /Users/admin/.claude/plugins/cache/claude-code-warp/warp/2.2.0/hooks/hooks.json
1  /Users/admin/.claude/plugins/cache/claude-plugins-official/opsera-devsecops/1.0.0/hooks/hooks.json
0  /Users/admin/.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/hooks/hooks.json
0  /Users/admin/.claude/plugins/cache/claude-plugins-official/superpowers/6.2.0/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-code-warp/plugins/oz-harness-support/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-code-warp/plugins/warp/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/explanatory-output-style/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/hookify/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/learning-output-style/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/ralph-loop/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official.bak/plugins/security-guidance/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/explanatory-output-style/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/learning-output-style/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-loop/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/claude-plugins-official/plugins/security-guidance/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/mempalace/.claude-plugin/hooks/hooks.json
0  /Users/admin/.claude/plugins/marketplaces/mempalace/.codex-plugin/hooks.json
```

**Confirms the manager: exactly one.** Six plugins installed, all six
`enabledPlugins: true` — verified:

```
$ jq -r '.enabledPlugins' /Users/admin/.claude/settings.json
{
  "superpowers@claude-plugins-official": true,
  "context7@claude-plugins-official": true,
  "opsera-devsecops@claude-plugins-official": true,
  "n8n-mcp-skills@n8n-mcp-skills": true,
  "praxis-progress@praxis-local": true,
  "warp@claude-code-warp": true
}
```

### 1.4 DIVERGENCE (minor, non-material)

The manager reported enumerating `hooks/hooks.json` "across all six install
paths". Only **three of six** install paths contain such a file:

```
=== .../superpowers/6.2.0
.../superpowers/6.2.0/hooks/hooks.json
=== .../context7/unknown
ls: .../context7/unknown/hooks/hooks.json: No such file or directory
=== .../opsera-devsecops/1.0.0
.../opsera-devsecops/1.0.0/hooks/hooks.json
=== .../n8n-mcp-skills/1.4.0
ls: .../n8n-mcp-skills/1.4.0/hooks/hooks.json: No such file or directory
=== .../praxis-progress/0.1.0
ls: .../praxis-progress/0.1.0/hooks/hooks.json: No such file or directory
=== .../warp/2.2.0
.../warp/2.2.0/hooks/hooks.json
```

Reported per instruction. Does not change the conclusion (the three absent ones
could not have contributed a matcher anyway).

### 1.5 Script identity

```
$ ls -l .../opsera-devsecops/1.0.0/hooks/pre-commit-scan.sh
-rwxr-xr-x@ 1 admin  staff  3305 Apr  2 17:46 .../pre-commit-scan.sh
$ wc -c -l .../pre-commit-scan.sh
      68    3305 .../pre-commit-scan.sh
```

Matches the manager's `-rwxr-xr-x`, 3305 bytes, 68 lines.

---

## 2. What the script does (read in full, 68 lines)

| Question | Answer (from source) |
|---|---|
| Payload fields read | `tool_input.command`, falling back to top-level `command` (line 8, via `python3`) |
| Command pattern | `grep -qE 'git\s+commit'` — **unanchored**, no `\b`, no word boundary (line 11) |
| Exit codes | `0` (no match, line 12), `0` (fresh flag, line 26), `2` (deny, line 68) |
| Repo-relative logic | **None.** It never reads `cwd` and never touches the repo. Fully repo-agnostic. |
| Observable side effect on the NON-matching path | **None whatsoever** — no log file, no temp file, no stderr |
| Side effects on other paths | stderr banner (deny); `rm -f /tmp/.opsera-pre-commit-scan-passed` |

**Consequence for S2:** because the non-matching path is byte-silent and
side-effect-free, *silence from this hook in a live session is not evidence of
anything.* This is exactly the manufactured-null trap the brief warns about.

---

## 3. Script-level experiment (piped payloads)

Technique per `docs/reports/2026-07-26-session34-manifest-amendment.md:198-206`.
Each arm run with `cd /Volumes/Sensidine/Praxis.build`; stdout and stderr
captured to separate files.

**Payload provenance — UNVERIFIED, stated plainly.** I did **not** capture a
live `PreToolUse` payload this session; no raw-payload capture exists in-repo.
My payloads are **synthetic**, built to the shape `no-commit-guard.sh:4` attests
was taken "from live PreToolUse payloads, CC 2.1.220". I independently confirmed
the running version is that version:

```
$ claude --version
2.1.220 (Claude Code)
```

This is corroboration, not a fresh capture. Mitigation: the script reads only
one field, and I tested **both** shapes it accepts (arms A1 and A4).

### 3.1 Results

```
$ bash run_arms.sh
A1_positive    exit=2   stdout=0B stderr=2189B
A2_negative    exit=0   stdout=0B stderr=0B
A3_empty       exit=0   stdout=0B stderr=0B
A4_fallback    exit=2   stdout=0B stderr=2189B
A5_malformed   exit=0   stdout=0B stderr=0B
A6_prose       exit=2   stdout=0B stderr=2189B
A7_evasion     exit=0   stdout=0B stderr=0B
--- flag file after all arms ---
ls: /tmp/.opsera-pre-commit-scan-passed: No such file or directory
```

(The wrapper's own exit 1 is the trailing `ls` failing on the absent flag file.)

| Arm | `tool_input.command` | exit | stderr |
|---|---|---|---|
| A1 POSITIVE | `git commit -m 'x'` | **2** | 2189 B |
| A2 NEGATIVE | `ls -la` | 0 | 0 B |
| A3 EMPTY | *(empty stdin)* | 0 | 0 B |
| A4 FALLBACK | top-level `command` key | **2** | 2189 B |
| A5 MALFORMED | non-JSON | 0 | 0 B |
| A6 PROSE | `echo 'the runbook says to git commit later'` | **2** | 2189 B |
| A7 EVASION | `git -c user.name=x commit -m 'y'` | **0** | 0 B |

The three firing arms emit a byte-identical banner:

```
$ md5 -q A1_positive.err A4_fallback.err A6_prose.err
8f3a17ef0a1cc50748baf83b050e4287
8f3a17ef0a1cc50748baf83b050e4287
8f3a17ef0a1cc50748baf83b050e4287
$ head -3 A1_positive.err
OPSERA SECURITY GATE: A security scan is required before committing.

MANDATORY INSTRUCTIONS — Follow these steps exactly. DO NOT skip or substitute any step.
```

### 3.2 Arm NOT run, and why (S2)

The **fresh-flag branch** (lines 17–29, the `exit 0` + stdout path) is
**UNTESTED**. Exercising it requires creating `/tmp/.opsera-pre-commit-scan-passed`,
which is outside my permitted scratch directory and is shared mutable state that
would open a real 5-minute gate-bypass window. `run_arms.sh` contains a guard
that aborts if the flag exists; the flag was absent before and after (shown
above), so no arm mutated it.

---

## 4. LIVENESS PROOF

A silent exit 0 proves nothing. Three independent proofs the script executed and
parsed **my** input:

**(a) A firing positive arm** — A1: exit 2, 2189 B of banner. Not a null.

**(b) `bash -x` trace showing the field being extracted** (line 5 is decisive):

```
$ bash -x pre-commit-scan.sh < A1_positive.json   ;  exit=2
1:++ cat
2:+ input='{"session_id":"synthetic-s41",...,"tool_input":{"command":"git commit -m '\''x'\''",...}}'
4:++ python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get('\''tool_input'\'',{})...'
5:+ command='git commit -m '\''x'\'''
6:+ echo 'git commit -m '\''x'\'''
7:+ grep -qE 'git\s+commit'
8:+ scan_flag=/tmp/.opsera-pre-commit-scan-passed
9:+ '[' -f /tmp/.opsera-pre-commit-scan-passed ']'
10:+ cat
45:+ exit 2
```

**(c) A payload variation that provably changes the trace** — same file, one
field differs; the negative arm exits at line 8 instead of reaching the banner:

```
$ bash -x pre-commit-scan.sh < A2_negative.json   ;  exit=0
5:+ command='ls -la'
6:+ echo 'ls -la'
7:+ grep -qE 'git\s+commit'
8:+ exit 0
```

**Liveness: ACHIEVED.** The script runs, reads `tool_input.command`, and denies.

---

## 5. Two defects in the script (reported, not fixed — out of scope)

- **A6 FALSE POSITIVE.** `git\s+commit` is unanchored, so the benign command
  `echo 'the runbook says to git commit later'` is denied (exit 2). Any command
  merely *mentioning* the phrase is blocked.
- **A7 FALSE NEGATIVE.** `git -c user.name=x commit -m 'y'` is a **real commit**
  and is **allowed** (exit 0), because an option sits between `git` and `commit`.
  The in-repo `no-commit-guard.sh` shares the same `\bgit\s+(commit|...)` shape
  and is UNVERIFIED but likely to share this gap. **Not tested — flagged only.**
- **Fails OPEN** on empty (A3) and malformed (A5) input.

---

## 6. THE MECHANISM QUESTION (S9 / ruling R3)

R3 grades "X is covered by mechanism Y" by toggling Y. **I am hard-forbidden
from toggling any plugin or settings file, and I did not.** So I looked for a
non-mutating observation route. **I found one, and it answers the question.**

### 6.1 Route 1 — corpus of genuine denials (corroborating)

I classified every `PreToolUse:Bash hook error` record across all transcripts,
restricting to *genuine* denials (`is_error: true` AND body starts with the
error prefix — this excludes agents' own grep output quoting hook errors, which
contaminated my first pass and which I corrected):

```
GENUINE PreToolUse:Bash denial tool_results: 121
histogram (scripts named per genuine denial): {1: 121}
```

Every hook script ever named in a denial, anywhere:

```
 335 [...]/.claude/hooks/gate-commit.sh
 113 [...]/scripts/no-commit-guard.sh
  91 /Volumes/Sensidine/Praxis.build/scripts/master-bash-guard.sh
  61 [...]/scripts/master-bash-guard.sh
  23 [...]/.claude/hooks/deny-b.sh
  23 [...]/.claude/hooks/deny-a.sh
   6 [...]/scripts/guard-rel.sh
```

`pre-commit-scan.sh` **never appears**. Separately, every occurrence of the
string `OPSERA SECURITY GATE` in any transcript under this repo's project dir
resolves to either a `Read` of the script file or a prior worker's own piped
experiment — **not one is a live denial**:

```
agent-af154152e71dca875.jsonl:46  producing tool : Read   (pre-commit-scan.sh)
agent-a78afba2e53785774.jsonl:34  producing tool : Read   (pre-commit-scan.sh)
agent-a04d042c95a06879f.jsonl:31  producing tool : Bash   (cat of hooks.json)
...
```

On its own this is only corroboration — see §6.3.

### 6.2 Route 2 — the debug log (DECISIVE)

`~/.claude/debug/588e253c-...txt` records plugin load. Only **two** plugins ever
had a `hooks.json` read:

```
$ grep -n 'Read hooks.json for plugin' ~/.claude/debug/588e253c-....txt
38: [DEBUG] Read hooks.json for plugin superpowers (enabled=true): .../superpowers/6.2.0/hooks/hooks.json
39: [DEBUG] Read hooks.json for plugin warp (enabled=true): .../warp/2.2.0/hooks/hooks.json
```

opsera is absent from that list because it **fails to load**:

```
$ grep -n 'opsera' ~/.claude/debug/588e253c-....txt
42: [DEBUG] Plugin not available for MCP: opsera-devsecops@claude-plugins-official - error type: plugin-not-found
43: [DEBUG] Plugin loading errors: Plugin opsera-devsecops not found in marketplace claude-plugins-official
52: [DEBUG] Plugin loading errors: Plugin opsera-devsecops not found in marketplace claude-plugins-official
```

**The cause, verified in CURRENT state (today):** the plugin is installed and
enabled, but its marketplace no longer lists it.

```
$ grep -ric 'opsera' ~/.claude/plugins/marketplaces/claude-plugins-official/.claude-plugin/marketplace.json
0
$ ls ~/.claude/plugins/marketplaces/claude-plugins-official/plugins | grep -i opsera
(no output)
```

Enabled + installed ≠ loaded. The `hooks.json` is never read, so the fourth
Bash-matcher registration **never enters the hook registry**.

### 6.3 What I could NOT confirm — the masking confound is UNVERIFIED

The brief supplies a known confound: when several `PreToolUse` hooks deny in
parallel, only the last to finish surfaces. **I could not confirm this**, and it
matters, because if true it would mean an opsera denial could fire and be hidden.

The prior `dualdeny` lab looked like the right precedent, but it did **not** run
two hooks simultaneously — each session had only one registered:

```
=== 16204fd6-....jsonl
  deny-a mentions: 0
  deny-b mentions: 3
  surfaced denial: PreToolUse:Bash hook error: [$CLAUDE_PROJECT_DIR/.claude/hooks/deny-b.sh]
=== 68d2adf0-....jsonl
  deny-a mentions: 3
  deny-b mentions: 0
  surfaced denial: PreToolUse:Bash hook error: [$CLAUDE_PROJECT_DIR/.claude/hooks/deny-a.sh]
```

So `{1: 121}` is equally consistent with "denials are masked" and with "two
hooks never denied the same call". **I mark masking UNVERIFIED.** I did not
construct a deliberate dual-trip because the brief forbids running commands
intended to be blocked.

This is why §6.2, not §6.1, carries the conclusion: the debug log observes
non-loading *upstream* of any masking, so it is immune to this confound.

### 6.4 Incidental live observation

My first Bash call this session was blocked — its heredoc text happened to
contain the trigger substring. The record (my subagent transcript, line 49):

```
line 49: tool=Bash is_error=True
   gate-commit msg present  : True
   no-commit-guard msg pres.: False
   OPSERA banner present    : False
   content: "PreToolUse:Bash hook error: [\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/gate-commit.sh]: Commit denied: ..."
```

A live Bash command containing `git commit` reached the hook chain and opsera
did not surface. Given §6.3 this is **not** independently decisive; it is
consistent with §6.2. No real commit was attempted.

### 6.5 Grading

| Claim | Status |
|---|---|
| A fourth Bash-matcher registration exists **on disk** | **PROVEN** (§1.3) |
| The script, when executed, matches `git commit` and denies | **PROVEN** (§3, §4) |
| The opsera plugin **loads and its hook fires live against this repo** | **DISPROVEN** by §6.2 — but see caveat |
| R3-style toggle demonstration | **UNGRADED — not performed** |
| Parallel-deny masking confound | **UNVERIFIED** (§6.3) |

**Caveat on §6.2 (S2 discipline).** The debug log is dated **2026-07-26**, four
days before today, and its session's cwd was a scratchpad probe dir, **not** this
repo. I did not capture a fresh `--debug` from today (doing so spawns a second
Claude session against this tree, which `CLAUDE.md` forbids). The finding
transfers because plugin loading is *user-scoped* — it derives from
`~/.claude/settings.json` + the user-scope marketplace, neither of which is
repo-dependent — and because I verified the *cause* (marketplace absence) in
current state today. Reported as: **non-loading directly observed 2026-07-26;
cause verified current 2026-07-30**; not as a fresh in-repo observation.

### 6.6 The experiment that would settle R3 properly, and what it would change

Not run — outside my authority. Recorded as the deliverable for this step.

1. **Repair the marketplace entry** so `opsera-devsecops` resolves (re-add the
   plugin to `claude-plugins-official`, or re-point the install at a marketplace
   that lists it). *This is the toggle* — note the meaningful toggle here is
   ON, not OFF; one cannot disable a plugin that never loaded.
2. Start a session with `claude --debug` and confirm the line
   `Read hooks.json for plugin opsera-devsecops (enabled=true)` now appears.
   **Expected change:** that line is currently absent (§6.2).
3. **Defeat the masking confound before the trip test** — otherwise the result
   is uninterpretable. Do the trip test in a *scratch repo* with none of the
   three in-repo guards present, so opsera is the only Bash hook that can deny.
   The opsera script is repo-agnostic (§2: it never reads `cwd`), so a scratch
   repo is a faithful venue.
4. Issue a benign command containing the trigger substring (e.g. the A6 prose
   arm — it denies without any commit being attempted).
   **Expected change:** `PreToolUse:Bash hook error: [.../pre-commit-scan.sh]:
   OPSERA SECURITY GATE...` appears; today the corpus has 0 such records in 121.
5. Restore the marketplace to its prior state.

**Precondition:** steps 1 and 5 mutate live plugin configuration. They require
Amear's explicit authorization. I did not perform them.

---

## 7. Answer to the unit question

**A fourth `PreToolUse matcher=Bash` hook exists on disk but does not fire
against this repo, because the plugin carrying it never loads.**
The effective live count is **3**.

Anyone auditing this repo's Bash-hook coverage should treat the opsera gate as
**absent**, not as defence-in-depth. Its false-negative on `git -c ... commit`
(§5) is moot while it does not load, but would matter if the plugin were ever
repaired.

## 8. Compliance

- Nothing staged. `git add` never run. Index untouched.
- `HEAD` still `c1dec30`.
- No plugin, settings file, guard script, agent def, hook script, or anything
  under `/Users/admin/.claude/` was created, modified or deleted.
- Nothing written under `.claude/agent-memory/`.
- No real `git commit` attempted; no command issued with intent to be blocked.
- Scratch files confined to the session scratchpad.
- This report is left **unstaged** per brief.

## Result: PASS
