# Session 41 — CYD worker 2 — ADVERSARIAL: "three Bash hooks, fourth is a phantom"

- **Task:** break the claim that exactly three `PreToolUse` `matcher=Bash` hooks are live
  against this repo and that `pre-commit-scan.sh` (opsera-devsecops) is a phantom.
- **Mode:** ADVERSARIAL
- **Criterion:** `specs/SPEC_RUBRIC.md` S1 (pasted output), S2 (no over-claim),
  S9 + ruling R3 (mechanism claims graded by toggling, not inspection).
- **Result: BOTTOM LINE SURVIVES — SUPPORT BREAKS IN FOUR PLACES.**

Environment fixed at the top so every number below is attributable:

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2

$ claude --version ; which -a claude
2.1.220 (Claude Code)
/Users/admin/.local/bin/claude
/Users/admin/.local/bin/claude
```

---

## Verdict

The **bottom line survives**: three Bash-matcher hooks, opsera does not resolve, the
"four Bash hooks" figure is wrong. I could not break it. But the claim is *right for
partly unsound reasons*, its enumeration was true by luck rather than by coverage, and
the decisive experiment is forbidden to me, so the load-bearing step is UNGRADED.

---

## Crack 1 — the enumeration as stated is incomplete; the missing source is agent frontmatter

The claim scopes the search space to "`.claude/settings.json` plus installed-plugin
`hooks/hooks.json`". That is not the whole space. This Claude Code build also registers
`PreToolUse` Bash hooks declared in **agent-definition frontmatter**. Both the loader
path and a real firing are attested in this machine's own corpus:

```
$ grep -in "hook" /Users/admin/.claude/debug/588e253c-91e7-4e8c-bc38-5f5ca3739819.txt | head -30
76:2026-07-26T13:57:30.736Z [ERROR] Skipping frontmatter hooks for main-thread agent 'agent-with-hook':
   the folder its definition file came from is not trusted (source: projectSettings, trust key: ...)
```

```
$ grep -rho "PreToolUse:Bash hook error: \[[^]]*\]" \
    /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build 2>/dev/null \
  | sed 's/.*\[//; s/\]$//' | grep -o '[A-Za-z0-9_-]*\.sh' | sort | uniq -c | sort -rn
 314 gate-commit.sh
 157 master-bash-guard.sh
 122 no-commit-guard.sh
  27 deny-b.sh
  23 deny-a.sh
   8 guard-rel.sh
   2 pre-commit-scan.sh
```

`guard-rel.sh` fired 8 times as a **frontmatter** hook — its own message says so:

```
PreToolUse:Bash hook error: [./scripts/guard-rel.sh]: FMHOOK-BLOCKED-REL: bash refused by frontmatter hook (relative...
```

I then closed the surface myself. No repo agent declares a `hooks:` key:

```
$ for f in /Volumes/Sensidine/Praxis.build/.claude/agents/*.md; do echo "## $f"; \
    awk 'NR==1&&$0=="---"{fm=1;next} fm&&$0=="---"{exit} fm{print}' "$f"; done
## orchestrator-auditor.md   name/description/disallowedTools/model
## praxis-auditor.md         name/description/model/memory/tools/disallowedTools/maxTurns
## praxis-manager.md         name/description/model/memory/skills/tools/maxTurns
## praxis-master.md          name/description/model/memory/skills/tools/initialPrompt
## praxis-tutor.md           name/description/disallowedTools/model
## praxis-worker.md          name/description/model/memory/tools/disallowedTools/maxTurns
(no `hooks:` key in any of the six)

$ ls -la /Users/admin/.claude/agents/
ls: /Users/admin/.claude/agents/: No such file or directory
```

**Defect:** "exactly three" is correct, but the claim reached it without ever considering
frontmatter hooks. Frontmatter hooks are *trust-gated*, not config-gated — a trusted
agent definition adds a fourth Bash hook with no edit to `.claude/settings.json`. The
claim's enumeration would not notice.

Remaining layers I swept and found empty, so the enumeration is otherwise complete:

```
$ for p in "/Library/Application Support/ClaudeCode/managed-settings.json" \
           "/Library/Application Support/Claude Code/managed-settings.json" \
           "/etc/claude-code/managed-settings.json" \
           "$HOME/.config/claude-code/settings.json"; do printf '%-60s ' "$p"; \
    [ -e "$p" ] && echo EXISTS || echo absent; done
/Library/Application Support/ClaudeCode/managed-settings.json absent
/Library/Application Support/Claude Code/managed-settings.json absent
/etc/claude-code/managed-settings.json                       absent
/Users/admin/.config/claude-code/settings.json               absent

$ find /Volumes/Sensidine/Praxis.build -name "settings*.json" -not -path "*/node_modules/*"
/Volumes/Sensidine/Praxis.build/.claude/settings.json          # no settings.local.json

$ ls /Volumes/Sensidine/Praxis.build/.mcp.json
ls: /Volumes/Sensidine/Praxis.build/.mcp.json: No such file or directory
```

`~/.claude/settings.json` carries **no `hooks` key at all** (only statusLine,
enabledPlugins, extraKnownMarketplaces, effortLevel, tui, theme, voice) — verified by
reading it in full. `~/.claude.json` likewise:

```
$ python3 -c "import json;d=json.load(open('/Users/admin/.claude.json'));\
print('top-level hooks key present:', 'hooks' in d);\
p=d.get('projects',{});print('praxis hooks:', p.get('/Volumes/Sensidine/Praxis.build',{}).get('hooks','<none>'));\
print('any project with hooks key:', [k for k,v in p.items() if 'hooks' in v] or 'NONE')"
top-level hooks key present: False
praxis hooks: <none>
any project with hooks key: NONE
```

The repo-local marketplace `praxis-local` → `/Volumes/Sensidine/Praxis.build/plugins`
(a live marketplace pointing *inside this repo*, which is a genuine hook-injection surface)
ships no hooks:

```
$ find /Volumes/Sensidine/Praxis.build/plugins -type f
/Volumes/Sensidine/Praxis.build/plugins/.claude-plugin/marketplace.json
/Volumes/Sensidine/Praxis.build/plugins/praxis-progress/scripts/progress-data.sh
/Volumes/Sensidine/Praxis.build/plugins/praxis-progress/.claude-plugin/plugin.json
/Volumes/Sensidine/Praxis.build/plugins/praxis-progress/commands/progress.md
(no hooks.json; plugin.json has no hooks key)
```

Of the six enabled plugins, only three ship a `hooks.json`, and only opsera's declares
`matcher: Bash`:

```
$ cat .../superpowers/6.2.0/hooks/hooks.json   -> SessionStart only
$ cat .../warp/2.2.0/hooks/hooks.json          -> SessionStart, Stop, Notification,
                                                  PermissionRequest, UserPromptSubmit,
                                                  PostToolUse, StopFailure  (7, no PreToolUse)
$ cat .../opsera-devsecops/1.0.0/hooks/hooks.json
{ "hooks": { "PreToolUse": [ { "matcher": "Bash",
    "hooks": [ { "type": "command",
                 "command": "${CLAUDE_PLUGIN_ROOT}/hooks/pre-commit-scan.sh" } ] } ] } }
```

---

## Crack 2 — the false-null defect (rubric S9 / attack surface 3). This one is real.

**Any step of the form "no `pre-commit-scan.sh` record in the corpus, therefore it never
fired" is unsound**, and the reason is specific to this script: it exits 0 on everything
that is not a commit command, and an exit-0 hook writes nothing anywhere.

Verified exit-0-on-benign directly (full matrix in Crack 4):

```
rc=0  git status
rc=0  git add -A
```

The corpus only ever records *blocks*. Positive control that blocks are recorded — a hook
I caused to fire in this session, minutes ago, by accident:

```
$ echo 'git commit -m x' | grep -qE 'git\s+commit' && echo MATCHED || echo "NO MATCH"
PreToolUse:Bash hook error: ["$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh]:
BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes.
```

That firing is in the transcript (`grep -c "no-commit-guard" <this session jsonl>` → `9`).
So blocking hooks *are* observable. **But that control does not extend to silent exit-0
firings, which is opsera's normal mode.** Zero records is therefore equally consistent
with "never registered" and "registered, fired on every Bash call, always exited 0."

Two further reasons no second corpus rescues it:

```
$ for f in scripts/no-commit-guard.sh scripts/master-bash-guard.sh .claude/hooks/gate-commit.sh; do
    echo "## $f"; grep -n "log\|LOG\|tee\|>>" "$f" | head; done
## scripts/no-commit-guard.sh        (no matches at all — writes no log)
## scripts/master-bash-guard.sh      line 12 = a detection regex, not a write
## .claude/hooks/gate-commit.sh      lines 4/147/148 = comments; 162/164 = grep + stderr
```

None of the three live guards writes a log file. And **this session emits no debug log**:
pid 4747 runs without `--debug`, and the debug directory holds exactly one file, four days old:

```
$ ls -la /Users/admin/.claude/debug/
-rw-r--r--@ 1 admin staff 53556 Jul 26 09:57 588e253c-91e7-4e8c-bc38-5f5ca3739819.txt
lrwxr-xr-x@ 1 admin staff    67 Jul 26 09:57 latest -> .../588e253c-....txt

$ ps -eo pid,lstart,command | grep claude | grep -v grep
 4747 Thu 30 Jul 12:10:27 2026     claude --dangerously-skip-permissions
```

**Report this as a defect in the claim's support even though the bottom line holds.**

---

## Crack 3 — staleness: the only direct load-failure record is 4 days old and from another cwd

The one artifact that states the mechanism is dated **2026-07-26T13:57Z**, from a session
whose cwd was a scratch probe dir, not this repo:

```
$ grep -in "opsera\|pre-commit-scan" /Users/admin/.claude/debug/588e253c-....txt
42:2026-07-26T13:57:30.723Z [DEBUG] Plugin not available for MCP: opsera-devsecops@claude-plugins-official - error type: plugin-not-found
43:2026-07-26T13:57:30.723Z [DEBUG] Plugin loading errors: Plugin opsera-devsecops not found in marketplace claude-plugins-official
...
$ grep -in "Registered\|Read hooks.json" .../588e253c-....txt
38: Read hooks.json for plugin superpowers (enabled=true): .../superpowers/6.2.0/hooks/hooks.json
39: Read hooks.json for plugin warp (enabled=true):        .../warp/2.2.0/hooks/hooks.json
55: Loading hooks from plugin: superpowers
56: Loading hooks from plugin: warp
57: Registered 8 hooks from 5 plugins
```

(8 = superpowers 1 + warp 7; 5 of the 6 enabled plugins resolved; opsera is the sixth.
Zero hooks from opsera.)

This matters because **the marketplace was re-fetched today, after that log was written** —
`lastUpdated: 2026-07-30T16:17:53.392Z`, `marketplace.json` mtime `Jul 30 11:50`. A refresh
could have re-added opsera and silently invalidated the claim. So I re-established the
premise *currently* rather than inheriting it:

```
$ python3 -c "import json;d=json.load(open('.../marketplaces/claude-plugins-official/.claude-plugin/marketplace.json'));\
n=[p['name'] for p in d['plugins']];print('total:',len(n));\
print('opsera-ish:',[x for x in n if 'opsera' in x.lower() or 'devsecops' in x.lower()]);\
print('renames:',d.get('renames'))"
total: 276
opsera-ish: ['aws-agents-for-devsecops']
renames: {'adlc': 'agentforce-adlc', 'airwallex': 'airwallex-agentos', 'convex-backend': 'convex',
          'vals': 'valtown', 'wordpress.com': 'build-with-wordpress', 'qodo-skills': 'qodo'}
```

I specifically attacked the **rename route** (a rename map could resolve
`opsera-devsecops` to a *different* plugin that does carry a Bash hook) — no opsera entry.
I also attacked the **second-marketplace / stale-cache route**:

```
$ grep -n "opsera" .../marketplaces/claude-plugins-official.bak/.claude-plugin/marketplace.json
NO MATCH
$ ls .../marketplaces/claude-plugins-official.bak/plugins/opsera-devsecops
No such file or directory
$ grep -ril "opsera" /Users/admin/.claude/plugins/marketplaces/ 2>/dev/null
(no output — zero files)
```

`.bak` is not a registered marketplace name in `known_marketplaces.json` anyway. Premise
holds **as of 2026-07-30**, on artifacts I regenerated today. Had I accepted the Jul 26
log alone, the claim would have been about the past.

### Live corroboration I generated (this is the strongest evidence in the file)

My own shell's parent process **is** this session's Claude:

```
$ echo "self=$$ ppid=$PPID"; ps -o pid,ppid,command -p $PPID
self=53556 ppid=4747
  PID  PPID COMMAND
 4747 46800 claude --dangerously-skip-permissions
```

PID 4747 stamped in-use markers into three plugins at 12:17 today, and none into opsera:

```
$ find /Users/admin/.claude/plugins/cache -name "4747" -maxdepth 5 -exec ls -la {} \;
-rw-r--r--@ 1 admin staff 51 Jul 30 12:17 .../claude-code-warp/warp/2.2.0/.in_use/4747
-rw-r--r--@ 1 admin staff 51 Jul 30 12:17 .../claude-plugins-official/context7/unknown/.in_use/4747
-rw-r--r--@ 1 admin staff 51 Jul 30 12:17 .../claude-plugins-official/superpowers/6.2.0/.in_use/4747

$ ls -la .../opsera-devsecops/1.0.0/.in_use/
-rw-r--r--@ 1 admin staff 52 May  9 08:31 85561
-rw-r--r--@ 1 admin staff 52 May  9 08:32 85985
$ cat .../opsera-devsecops/1.0.0/.in_use/85561
{"pid":85561,"procStart":"Sat May  9 12:31:23 2026"}
$ ps -p 85561 -p 85985
  PID TTY           TIME CMD          (neither pid running)
```

**Limitation I must state under S2:** `.in_use` appears only for github-sourced
marketplace plugins — `n8n-mcp-skills` and `praxis-progress` are directory-sourced and
have **no** `.in_use` directory at all despite being enabled. So marker-absence is
probative only *within the github-sourced class*. Opsera is in that class, and that class
supplies three live positive controls from the very PID executing this report. That is
why I rate this the strongest available evidence — but it evidences *"not loaded"*, and
"therefore not in the hook registry" remains one inferential step beyond it.

---

## Crack 4 — the phantom is also a bad gate (attack surface 4)

Synthetic `PreToolUse` payloads piped straight into the script. Payload files were built
by `/private/tmp/.../scratchpad/payload-runner.sh` so the intercepted literal phrase never
appeared in a Bash command string. `rc=2` = blocked, `rc=0` = allowed through.

```
$ bash /private/tmp/.../scratchpad/payload-runner.sh
hook: /Users/admin/.claude/plugins/cache/claude-plugins-official/opsera-devsecops/1.0.0/hooks/pre-commit-scan.sh
--- A. commands that SHOULD be gated ---
rc=2  expect=block  canonical                    cmd=[git commit -m 'x']
rc=2  expect=block  extra spaces                 cmd=[git   commit -m 'x']
rc=2  expect=block  env prefix                   cmd=[GIT_AUTHOR_NAME=z git commit]
rc=0  expect=block  -C repo dir BEFORE verb      cmd=[git -C /tmp commit -m 'x']
rc=2  expect=block  --work-tree before verb      cmd=[git --work-tree=/tmp --git-dir=/tmp/.git commit -m x]
rc=0  expect=block  -c option before verb        cmd=[git -c user.name=z commit -m x]
rc=0  expect=block  --no-pager before verb       cmd=[git --no-pager commit -m x]
rc=2  expect=block  chained after &&             cmd=[echo hi && git commit -m x]
rc=0  expect=block? commit via alias-ish ci      cmd=[git ci -m x]

--- B. benign commands that should NOT be gated ---
rc=0  expect=allow  git status                   cmd=[git status]
rc=0  expect=allow  git add                      cmd=[git add -A]
rc=2  expect=allow  grep for the phrase          cmd=[grep -rn "git commit" docs/]
rc=2  expect=allow  echo mentioning phrase       cmd=[echo 'how do I git commit']
rc=0  expect=allow  reading a log file           cmd=[cat /var/log/git-commit.log]

--- C. degraded-environment behaviour ---
rc=0 expect=block  no-python3-on-PATH (fail-open?)
rc=0 expect=allow  malformed JSON stdin
```

The detector is `grep -qE 'git\s+commit'` (line 12 of the script). Consequences:

- **Four bypasses.** Any global git option between verb and subcommand defeats it:
  `-C`, `-c`, `--no-pager` all pass. So does the `ci` alias.
- **Two false positives.** Merely *mentioning* the phrase — `grep -rn "git commit" docs/`,
  `echo 'how do I git commit'` — is blocked with exit 2.
- **Fail-open on a missing interpreter.** The script extracts the command with an inline
  `python3`. With `PATH=/nonexistent`, a canonical commit returns **rc=0**. The gate
  disables itself silently rather than failing closed.
- **One right answer for the wrong reason.** `--work-tree=... --git-dir=/tmp/.git commit`
  is caught only because the path substring `.git commit` happens to match the regex.

A hypothesis I tested that did **not** pan out, reported per S2: I expected `\s` to be
unsupported in BSD ERE, which would have meant the gate never matched anything. It works:

```
$ bash /private/tmp/.../scratchpad/grep-test.sh
grep binary: /usr/bin/grep
grep (BSD grep, GNU compatible) 2.6.0-FreeBSD
MATCH   | single space (the canonical case) | subject=[git commit -m x]
MATCH   | multiple spaces                   | subject=[git   commit -m x]
MATCH   | tab separator                     | subject=[git	commit -m x]
NOMATCH | literal-s form gitsscommit        | subject=[gitsscommit]
MATCH   | POSIX class control on single space
```

---

## Crack 5 — "exactly three" is not decidable by observing denials

The repo's own agent docs note that when several `PreToolUse` hooks deny in parallel only
one message survives (`praxis-master.md:69`, `praxis-manager.md:65`). I observed exactly
that: the `grep` command in Crack 2 ran against all three Bash hooks and surfaced
**one** message (`no-commit-guard.sh`). So a fourth Bash hook that denied could be masked,
and one that exited 0 is invisible by Crack 2. Counting live Bash hooks by watching
runtime behaviour is structurally incapable of returning "exactly three" — the count is
sound only because it comes from reading the config, which is inspection, not S9 proof.

All three configured guards *are* independently attested as live, which the claim gets right:

```
$ bash /private/tmp/.../scratchpad/count-firings.sh
no-commit-guard.sh     genuine PreToolUse:Bash hook-error records = 124
gate-commit.sh         genuine PreToolUse:Bash hook-error records = 316
master-bash-guard.sh   genuine PreToolUse:Bash hook-error records = 159
pre-commit-scan.sh     genuine PreToolUse:Bash hook-error records = 4
```

The four `pre-commit-scan.sh` hits are **not** firings — I resolved every one. Two are my
own scratch scripts echoed into this session's transcript, and two are prose from a
sibling agent using an elided path (`[.../pre-commit-scan.sh]`, with literal `...`, inside
a sentence proposing a mutation experiment). Genuine runtime records carry an unelided
command string:

```
$ bash /private/tmp/.../scratchpad/inspect-opsera-hits.sh | head -8
1  PreToolUse:Bash hook error: [\" followed by the raw command\n# string as configured in settings.json...
      -> my own count-firings.sh source, echoed back
3  PreToolUse:Bash hook error: [.../pre-commit-scan.sh]:\n   OPSERA SECURITY GATE...` appears; today the
   corpus has 0 such records in 121.\n5. Restore the marketplace to its prior state.
      -> prose, elided path, another agent's write-up
```

**Genuine runtime firings of `pre-commit-scan.sh`: zero.**

---

## UNGRADED under S9 / ruling R3

R3 requires a mechanism claim to be graded by toggling the mechanism and showing behaviour
change. **I may not toggle.** So I state plainly:

1. **"Its hook registration never enters the runtime registry" is UNGRADED.** It is
   supported by three convergent read-only lines of evidence (marketplace absence
   re-verified today; the loader's own `plugin-not-found` + `Registered 8 hooks from 5
   plugins` in the Jul 26 debug log; live `.in_use` divergence under PID 4747). None is a
   toggle. Per R3 I decline to call inspection proof.
2. **The experiment that would decide it, written up as the deliverable:** restore
   `opsera-devsecops` to a marketplace the machine trusts (or add a marketplace carrying
   it), start a session with `--debug`, and show (a) `Read hooks.json for plugin
   opsera-devsecops (enabled=true)`, (b) the registered-hook count rising from 8 to 9,
   (c) an `.in_use/<pid>` marker appearing under `opsera-devsecops/1.0.0`, and (d) a
   canonical commit producing `PreToolUse:Bash hook error: [<abs path>/pre-commit-scan.sh]:
   OPSERA SECURITY GATE`; then revert. Steps 1 and 5 mutate live plugin configuration and
   require Amear's authorisation. **Not run.**
3. **The live session's hook registry could not be read directly.** No read-only API
   exposes it, and launching a nested `claude --debug` would itself write `.in_use`
   markers and could trigger a marketplace re-fetch — i.e. mutation. Not attempted.

## Corpus contamination notice

My probing wrote the strings `OPSERA SECURITY GATE` and `pre-commit-scan.sh` into this
session's transcripts. Any future corpus search for opsera firings **must** exclude
records after `2026-07-30 12:30` or it will find my artefacts and mistake them for evidence.

## Files staged

**None.** Nothing added, nothing committed; `HEAD` remains `c1dec30`. This report is
written to the working tree and deliberately left unstaged. Scratch files confined to
`/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/b09d4cee-.../scratchpad/`
(`grep-test.sh`, `payload-runner.sh`, `payloads/`, `count-firings.sh`,
`inspect-opsera-hits.sh`). No plugin, marketplace, settings file, guard script, agent
definition, or `.claude/agent-memory/` file was read-modified or written.

## Result: NO BREAK FOUND on the bottom line — SUPPORT BREAKS (Cracks 1–5)
