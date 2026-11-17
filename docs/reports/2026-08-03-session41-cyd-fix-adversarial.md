# Adversarial grade — `Praxis_build-cyd` fix unit artifacts

**Task:** Grade artifacts A–D against the sanctioned memory-correction pattern (P1 opens with the
correction / P2 superseded text verbatim / P3 nothing deleted), plus rubric S1/S2 on the appended errata.
**Mode:** ADVERSARIAL. Read-only. No repo state mutated; the only write is this file.
**Criterion:** `specs/SPEC_RUBRIC.md` S1 (pasted evidence, not description) and S2 (no claim above its evidence).
**Report path:** `/Volumes/Sensidine/Praxis.build/docs/reports/2026-08-03-session41-cyd-fix-adversarial.md`

---

## 0. Invariants — confirmed

```
$ git rev-parse HEAD
c1dec30c6516edcf7c79a78fce5c655e007d7ba2

$ git diff --cached --numstat
226	0	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
385	0	docs/reports/2026-07-26-session36-agent-key-audit.md
287	0	docs/reports/2026-07-26-session36-agent-key-lab.md
219	0	docs/reports/2026-07-26-session36-agent-key-s9-control.md
328	0	docs/reports/2026-07-26-session36-null-attack.md
131	0	docs/reports/2026-07-26-session36-worker-trigger-probe.md

$ git diff --cached --numstat | awk '{a+=$1; d+=$2; n++} END {print "paths="n" add="a" del="d}'
paths=6 add=1576 del=0
```

Exactly 6 paths / 1576 additions / 0 deletions. HEAD matches.

`git status --short` — the only `A ` (staged) entries are those same six session-36 reports. Nothing new
is staged; every fix-unit artifact is either gitignored or untracked (`??`):

```
$ git status --short
 M .claude/settings.json
 M .gitignore
 M AUDIT_LOG.md
 M DECISION_LOG.md
 M DISPATCH_LOG.md
 M HANDOFF.md
 M ISSUE_REGISTER.md
 M MANIFEST.md
 M STATUS.md
A  docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
A  docs/reports/2026-07-26-session36-agent-key-audit.md
A  docs/reports/2026-07-26-session36-agent-key-lab.md
A  docs/reports/2026-07-26-session36-agent-key-s9-control.md
A  docs/reports/2026-07-26-session36-null-attack.md
A  docs/reports/2026-07-26-session36-worker-trigger-probe.md
 M scripts/dispatch-log-writeahead.sh
 M specs/SPEC_RUBRIC.md
?? F
?? docs/reports/2026-07-26-session34-manifest-amendment.md
   [... untracked docs/reports/*.md elided for length; full list re-runnable ...]
?? docs/reports/2026-07-30-session41-cyd-audit.md
?? docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
?? docs/reports/2026-07-30-session41-cyd-worker1-hook-experiment.md
?? docs/reports/2026-07-30-session41-cyd-worker2-adversarial.md
?? docs/reports/2026-08-03-session41-cyd-fix-worker1.md
?? scripts/dispatch-log-close.sh
?? scripts/tests/test-dispatch-log-close.sh
```

Directory entry counts — manager 11, worker 5, as required. No new memory files:

```
$ ls -1 .claude/agent-memory/praxis-manager/ | wc -l
      11
$ ls -1 .claude/agent-memory/praxis-worker/ | wc -l
       5
```

```
$ ls -la .claude/agent-memory/praxis-manager/
-rw-r--r--  feedback_verdict_token_required.md      Jul 26 19:20
-rw-r--r--  feedback_workers_write_to_agent_memory.md Jul 27 16:29
-rw-r--r--  MEMORY.md                                Aug  3 16:52
-rw-r--r--  project_8sw_park_gate_boundary.md        Jul 26 15:15
-rw-r--r--  project_agent_type_mechanism.md          Jul 26 19:18
-rw-r--r--  project_commit_guard_bypass.md           Aug  3 16:52
-rw-r--r--  project_false_null_hazard.md             Jul 26 18:21
-rw-r--r--  project_manager_report_contract_gate.md  Jul 26 18:22
-rw-r--r--  project_master_write_guard_routing.md    Jul 26 14:20
-rw-r--r--  project_park_commit_paste_hazard.md      Jul 26 16:38
-rw-r--r--  project_s13_task_vs_agent.md             Jul 26 14:20
```

Only `MEMORY.md` and `project_commit_guard_bypass.md` carry an Aug 3 mtime; the other nine are untouched.
Worker dir likewise: only `MEMORY.md` is Aug 3.

Both memory trees are gitignored, so **no git baseline exists** for P2/P3 diffing:

```
$ git ls-files .claude/agent-memory/
(empty)
$ git check-ignore -v .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
.gitignore:26:.claude/agent-memory/	.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md
```

P2/P3 therefore had to be established by (a) quotes of the pre-fix text in reports written *before* the
fix, and (b) line-offset arithmetic. Both were done. See §1.

---

## 1. Artifact A — `praxis-manager/project_commit_guard_bypass.md`

### P1 — PASS

The file opens at line 8, immediately after frontmatter, with a heading that names the withdrawn claim:

```
  8	# CORRECTION FIRST — READ BEFORE ACTING ON ANYTHING BELOW
  9	
 10	**This file previously told you there were FOUR live Bash PreToolUse hooks. There are
 11	THREE.** The count "four" is WITHDRAWN. Every superseded passage is preserved verbatim
 12	below and marked where it stands; nothing has been deleted.
```

The `description:` frontmatter at line 3 also leads with `CORRECTED 2026-07-30 — ... THREE live Bash
PreToolUse hooks (the count "four" is withdrawn ...)`. A reader meets the correction before any body
content. The audit's A-1 finding ("does not open with its correction") is repaired.

### P2 / P3 — PASS on everything verifiable, by pre-fix quote + offset arithmetic

The audit (`docs/reports/2026-07-30-session41-cyd-audit.md`, written 2026-07-30, i.e. *before* the fix)
quotes six pre-fix lines verbatim:

```
$ awk 'NR>=84 && NR<=93 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-30-session41-cyd-audit.md
84	```
85	  8: Under bead `Praxis_build-jcw` the commit-guard evasion lead was settled by
86	 ...
87	 20: name what enforces it, because these four hooks do not.
88	 22: **The inventory trap — this is the reusable part.** `.claude/settings.json`
89	 23: registers three Bash-matcher PreToolUse hooks. There is a **fourth**, from the
90	 ...
91	 29: > **CORRECTION 2026-07-30 (`Praxis_build-cyd`) — the paragraph immediately above is
92	 30: > WRONG on its specific, RIGHT on its lesson. It is preserved, not deleted.**
93	```
```

Mapping those onto the current file:

| pre-fix line | current line | offset | byte-identical? |
|---|---|---|---|
| 8 | 21 | +13 | yes |
| 20 | 33 | +13 | yes |
| 22 | 41 | +19 | yes |
| 23 | 42 | +19 | yes |
| 29 | 48 | +19 | yes |
| 30 | 49 | +19 | yes |

The offset is +13 for everything above the second insertion point and +19 below it. Current lines 8–20
are 13 new lines (the correction header) and current lines 35–40 are 6 new lines (the in-place
correction block plus blank). 13 + 6 = 19. **The offsets are exactly consistent with pure insertion and
admit no deletion** anywhere in the quoted span. Current file is 87 lines; 87 − 19 = 68, the implied
pre-fix length.

### DEFECT A-1 — an unmarked four-hook residue survives at line 25, in an auto-loaded file

Full enumeration of every `four` / `fourth` / `4` / `three` token in the file:

```
$ grep -nio -E "four|fourth|FOUR|4|three|THREE|3" .claude/agent-memory/praxis-manager/project_commit_guard_bypass.md | sort -t: -k1,1n
3:3        3:four     3:THREE
10:FOUR
11:four    11:THREE
25:three
33:four
35:3      36:four    37:FOUR   37:THREE   38:three
42:fourth 42:three
48:3
51:fourth
57:three
65:three
66:fourth
69:3
75:three
```

Judgment, token by token:

| line | token | verdict |
|---|---|---|
| 3 | `3` (date `2026-07-30`), `four`, `THREE` | MARKED — frontmatter is the withdrawal itself |
| 10, 11 | `FOUR`, `four`, `THREE` | MARKED — the withdrawal statement |
| **25** | **`three`** | **UNMARKED — see below** |
| 33 | `four` ("because these four hooks do not") | MARKED — in-place correction at 35–39 immediately follows, and the header at 18–19 names this paragraph |
| 35, 48, 69 | `3` (dates `2026-08-03`, `2026-07-30`; rubric `R3`) | not a count |
| 36, 37, 38 | `four`, `FOUR`, `THREE`, `three` | MARKED — the correction text |
| 42 | `fourth`, `three` | MARKED — correction block at 48–75 immediately follows; header names "The inventory trap" |
| 51 | `fourth` ("there is no live fourth hook") | MARKED — the negation |
| 57 | `three` (plugins stamped) | not a hook count |
| 65 | `three` ("the count is three") | correct |
| 66 | `fourth` ("a fourth hook *can appear*") | correct — hypothetical future |
| 75 | `three` ("three days") | not a hook count |

Every *literal* "four"/"fourth" is marked. But line 25 carries the count arithmetically:

```
 21	Under bead `Praxis_build-jcw` the commit-guard evasion lead was settled by
 22	experiment: **CONFIRMED**. Piping synthetic payloads into each guard separately
 23	(exit 0 = not gated, exit 2 = gated) showed `git 'commit' -m "…"` returns exit 0
 24	from every live Bash PreToolUse hook, while the plain form returns exit 2 from
 25	three of them.
```

"them" = "every live Bash PreToolUse hook". There are three. So this asserts that **all three** live
hooks return exit 2 on a plain commit. That is false, and the same file says so 52 lines later:

```
 77	Conversely, **counting hooks over-counts the defence**: `master-bash-guard.sh`
 78	sits on the Bash matcher beside the commit guards but is a shell-*redirection*
 79	guard — it exits 0 on a plain commit from every identity.
```

Verified at source. The three Bash-matcher PreToolUse registrations in `.claude/settings.json` are
`no-commit-guard.sh`, `gate-commit.sh`, `master-bash-guard.sh`:

```
$ python3 -c "import json;d=json.load(open('.claude/settings.json'));print(json.dumps(d['hooks']['PreToolUse'],indent=2))"
  { "matcher": "Bash", ... "$CLAUDE_PROJECT_DIR"/scripts/no-commit-guard.sh ... }
  { "matcher": "Bash", ... "$CLAUDE_PROJECT_DIR"/.claude/hooks/gate-commit.sh ... }
  { "matcher": "Write|Edit|NotebookEdit", ... master-write-guard.sh ... }
  { "matcher": "Bash", ... "$CLAUDE_PROJECT_DIR"/scripts/master-bash-guard.sh ... }
  { "matcher": "Agent", ... agent-spawn-guard.sh ... }
```

Of those three, only two contain any commit logic:

```
$ grep -n "commit" scripts/no-commit-guard.sh | head -3
2:# Subagents never commit. Only the main-thread master commits, after the auditor passes.
20:if echo "$CMD" | grep -qE '\bgit\s+(commit|push|merge|rebase|tag)\b'; then
21:  echo "BLOCKED: subagents leave work staged. The master commits after praxis-auditor passes." >&2

$ grep -n "commit" .claude/hooks/gate-commit.sh | head -3
2:# PreToolUse gate (matcher: Bash). Denies `git commit` in an ARMED repo unless a
31:  *git*commit*) ;;   # cheap pre-filter only; precise command-position check below
51:GITCOMMIT="${BINPRE}"'git[[:space:]]+([^;&|`]*[[:space:]])?commit([[:space:];&|)`]|$)'

$ grep -n "commit" scripts/master-bash-guard.sh || echo "NO MATCH for 'commit'"
NO MATCH for 'commit'
```

`master-bash-guard.sh` in full — its only `exit 2` is behind a redirection regex, and it short-circuits
to `exit 0` for any subagent and any non-`praxis-master` identity:

```
$ cat -n scripts/master-bash-guard.sh
     7	[ -n "$AGENT_ID" ] && exit 0
     8	[ "$AGENT" = "praxis-master" ] || exit 0
    12	if echo "$CMD" | grep -qE '(^|[^>])>{1,2}[[:space:]]*[^&]|(^|\s)(sed|tee|patch|dd)\s+.*-i|\bcat\s*<<'; then
    17	  exit 2
    18	fi
    19	exit 0
```

**Therefore: two of three, not three of three.** Line 25 is only true if a fourth hook exists — it is a
direct arithmetic residue of the withdrawn count.

Aggravating, not cosmetic:

1. The file is auto-loaded **in full** into every `praxis-manager` context. A manager reading top-down
   meets "three of them gate a plain commit" as a live, unqualified experimental result.
2. Line 25 carries **no** marker, and the top-of-file correction actively points away from it. Lines
   18–19 read `See the in-body corrections at the "Why this matters" paragraph and at "The inventory
   trap".` — an enumeration of exactly two sites. Line 25 is in neither.
3. It falsifies the file's own opening guarantee at lines 11–12: `Every superseded passage is preserved
   verbatim below and marked where it stands.` This one is not marked.
4. The audit had already put a flag next to this exact arithmetic, in the sibling file:
   ```
   $ awk 'NR==76 {print}' docs/reports/2026-07-30-session41-cyd-audit.md
   parenthetical "(three of which gate commits)" is corroborated by nothing outside the file itself.
   ```
   The fix did not carry that finding across to the manager file.

**A verdict: P1 PASS, P2 PASS, P3 PASS, but one unmarked live-voice residue of the withdrawn count
remains at `:25`. FAIL.**

---

## 2. Artifact B — `praxis-worker/MEMORY.md`

Current entry present and the count reads three:

```
  4	- [Commit guards: tripwire, not barrier](project_commit-guards-block-scratch-repos.md) — none of the 3 LIVE Bash hooks gate a quoted subcommand; the "4th" is a phantom; thrice corrected
```

Three superseded lines are preserved at `:6`, `:7`, `:8`. Grading each.

### `:7` (2026-07-28 prior-prior) — VERBATIM, VERIFIED, cited in-repo

The memory cites `docs/reports/2026-07-28-session40-memory-correction-adversarial.md:85`. That line
exists and byte-matches:

```
$ awk 'NR==85 {print}' docs/reports/2026-07-28-session40-memory-correction-adversarial.md
.../praxis-worker/MEMORY.md:4:- [Commit guards are a tripwire, not a barrier](project_commit-guards-block-scratch-repos.md) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted

$ python3 - <<'EOF'   # strip the wrappers and compare payloads byte-for-byte
...
MEM: '- [Commit guards are a tripwire, not a barrier](project_commit-guards-block-scratch-repos.md) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted'
REP: '- [Commit guards are a tripwire, not a barrier](project_commit-guards-block-scratch-repos.md) — CORRECTED: a quoted subcommand bypasses all four Bash hooks (measured); the old "blocks through any route" claim is refuted'
IDENTICAL: True
```

### `:6` (2026-07-30 immediate predecessor) — VERBATIM, VERIFIED out-of-repo only

Exact-string search of the local transcript corpus (JSON-escape-aware):

```
WORKER_L6: 7 transcript(s)
    .../abd15179-18bf-47be-a6d8-8c15c68685f4.jsonl
    .../abd15179-18bf-47be-a6d8-8c15c68685f4/subagents/agent-a229b22279a086894.jsonl
    .../abd15179-18bf-47be-a6d8-8c15c68685f4/subagents/agent-a9e9b9144a2b96487.jsonl
    .../b09d4cee-.../subagents/agent-a5f2fba395dedf0de.jsonl
    .../b09d4cee-.../subagents/agent-a9264c2aae40660b4.jsonl
    .../b09d4cee-.../subagents/agent-aa372dd82171bf961.jsonl
    .../b09d4cee-.../subagents/agent-aec59be37409697c2.jsonl
```

Three hits sit in session `abd15179`, which is **not** the fix session — genuine independent
corroboration. The `:9` NOTE's claim that the immediate predecessor already carried the short title
("Commit guards: tripwire, not barrier") is therefore **CONFIRMED**, and the audit's contrary
attribution at `:145` is correctly overturned. Good catch by the fix.

In-repo, only the *tail* of `:6` is citable:

```
$ awk 'NR>=195 && NR<=197 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-28-session40-agent-memory-disposition.md
195	`MEMORY.md`'s index line was also corrected: it had carried the inflated "bypasses all four Bash
196	hooks" and is now `quoted subcommand gated by none of 4 Bash hooks (3 gate commits); present-tense
197	only, twice corrected` — also shortening it from 221 chars toward the ~150 index guideline.
```

The title/link prefix is not corroborated by any in-repo file.

### DEFECT B-1 — `:8` is labelled unrecoverable when it is fully recoverable

```
  5	  <!-- ... Recovered verbatim from the session transcript corpus; report cites where each was previously quoted. -->
  8	  - superseded earlier (oldest recovered, PARTIAL — tail not recovered verbatim): `- [Commit guards block scratch repos](project_commit-guards-block-scratch-repos.md) — gate-commit.sh/no-commit-guard.sh match word …`
```

The tail **is** recovered verbatim, from the same corpus the header cites, in two sessions that predate
the fix unit. Search excluding the fix session `b09d4cee` entirely:

```
FILE: .../d3643d42-.../subagents/agent-a09bf095bcde628fa.jsonl
FRAG: e/agent-memory/praxis-worker/MEMORY.md","old_string":"- [Commit guards block scratch repos](project_commit-guards-block-scratch-repos.md) — gate-commit.sh/no-commit-guard.sh match word \"commit\" anywhere, any cwd; use quoted hash-object workaround for scratch positive controls","new_string":"- [Commit guards are a tripwire, not a barrier](...

FILE: .../b9c7174b-.../subagents/agent-a796a319b97a56749.jsonl
FRAG: ...\n- [Commit guards block scratch repos](project_commit-guards-block-scratch-repos.md) — gate-commit.sh/no-commit-guard.sh match word \"commit\" anywhere, any cwd; use quoted hash-object workaround for scratch positive controls
```

The first is an `Edit` tool call's own `old_string` field, timestamped `2026-07-27T20:04:11.159Z` — the
strongest possible provenance for "this is exactly what the line said before it was changed." The full
recovered line:

```
- [Commit guards block scratch repos](project_commit-guards-block-scratch-repos.md) — gate-commit.sh/no-commit-guard.sh match word "commit" anywhere, any cwd; use quoted hash-object workaround for scratch positive controls
```

So the memory (a) elides text that exists and is recoverable, and (b) states a false reason for the
elision. This is the brief's "presented as partial when it is complete" case. P3 ("nothing is deleted")
is not met for the oldest line: the tail is gone and is recorded as unrecoverable. It also reproduces
the failure mode named in this very directory's own `feedback_scoped-hedge-vs-universal-negative.md`
("underclaim breaks S2 too") — a file that, per the transcript fragments above, sits one line above the
elided entry.

### DEFECT B-2 (minor) — the header over-promises citations

`:5` says `report cites where each was previously quoted`. Of the three preserved lines, only `:7`
carries an inline citation. `:6` and `:8` carry none, and the transcript paths that do substantiate them
are not recorded anywhere in the worker file.

**B verdict: current entry correct; `:7` verbatim and cited; `:6` verbatim; `:8` truncated with a false
unrecoverability label. FAIL.**

---

## 3. Artifact C — `praxis-manager/MEMORY.md`

Current entry present, count reads three, and nothing above it was disturbed — the audit (2026-07-30)
quotes the entry at line 9, and it is still line 9 with identical text:

```
$ awk 'NR==120 {print}' docs/reports/2026-07-30-session41-cyd-audit.md
praxis-manager/MEMORY.md:9: - [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all 3 LIVE Bash hooks; the "4th" plugin hook is a phantom (enabled ≠ loaded); frontmatter is the real extra source

$ awk 'NR==9 {print}' .claude/agent-memory/praxis-manager/MEMORY.md
- [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all 3 LIVE Bash hooks; the "4th" plugin hook is a phantom (enabled ≠ loaded); frontmatter is the real extra source
```

Identical text at an identical line number in a pre-fix artifact ⇒ no entry above line 9 was deleted.
All 12 original index entries remain; the fix added only lines 10–12 (a comment, the preserved line, a
recovery note).

### The preserved line at `:11` — VERBATIM, VERIFIED

```
 11	  - superseded 2026-07-30 (immediate predecessor): `- [Commit-guard bypass](project_commit_guard_bypass.md) — `git 'commit'` evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks.`
 12	  <!-- RECOVERY NOTE: the audit (docs/reports/2026-07-30-session41-cyd-audit.md:147) recorded this prior line as UNVERIFIED/unrecoverable because no file under docs/reports/ quotes it. That is true of docs/reports/ and FALSE overall — the line was recovered verbatim from the session transcript corpus, earliest occurrence 2026-07-27, in .../subagents/agent-a09bf095bcde628fa.jsonl (3 further occurrences in 3 other transcripts). It is NOT lost. -->
```

The cited transcript exists and contains the string:

```
$ ls -la /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/d3643d42-.../subagents/agent-a09bf095bcde628fa.jsonl
-rw------- 536650 Jul 27 16:30 ...agent-a09bf095bcde628fa.jsonl

$ grep -c "evades all four Bash hooks (measured); settings.json is not a complete hook inventory, plugins add hooks." <that file>
2
```

Earliest-occurrence claim confirmed — that file carries the earliest timestamp in the whole corpus:

```
2026-07-27T20:30:03.507Z .../d3643d42-.../subagents/agent-a09bf095bcde628fa.jsonl
2026-07-28T16:15:51.310Z .../ffb8751c-.../subagents/agent-a81988d393938a947.jsonl
2026-07-30T16:20:27.969Z .../b09d4cee-.../subagents/agent-aec59be37409697c2.jsonl
2026-08-03T20:48:09.076Z .../b09d4cee-.../subagents/agent-a9264c2aae40660b4.jsonl
2026-08-03T20:50:36.635Z .../b09d4cee-.../subagents/agent-a5f2fba395dedf0de.jsonl
2026-08-03T20:56:54.644Z .../b09d4cee-.../subagents/agent-aa372dd82171bf961.jsonl
```

The audit's `:147` characterisation is also accurately reported — with one omission (see D):

```
$ awk 'NR>=147 && NR<=148 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-30-session41-cyd-audit.md
147	The prior *manager* index line is **UNVERIFIED** — no report quotes it, and the path is untracked, so I
148	cannot confirm what it previously said or whether it carried the count at all.
```

### DEFECT C-1 (minor) — the parenthetical count does not reproduce

`:12` says `(3 further occurrences in 3 other transcripts)`. Measured now: **6 transcripts total, i.e. 5
"other"** (list above). Three of the six are same-session `b09d4cee` transcripts dated 2026-08-03 —
echoes generated by the fix unit itself, two of which (20:48:09Z, 20:50:36Z) predate the memory file's
own mtime of Aug 3 16:52 local = 20:52Z. Excluding the fix session entirely gives 2 other transcripts,
not 3. No filter is stated, so the figure is not reproducible either way. The load-bearing claims
(verbatim, earliest, "NOT lost") all hold; only the count is off.

### DEFECT C-2 — the verbatim claims are not repo-citable (the brief's focus)

Repo-wide search for the preserved manager line:

```
$ grep -rn "evades all four Bash hooks" .
docs/reports/2026-08-03-session41-cyd-fix-worker1.md:314:    11	  - superseded 2026-07-30 (immediate predecessor): ...
docs/reports/2026-08-03-session41-cyd-fix-worker1.md:336:$ grep -c "evades all four Bash hooks (measured); ..." .claude/agent-memory/praxis-manager/MEMORY.md
```

The only in-repo occurrences are inside the fix unit's **own** report — self-citation. Same for worker
`:6` (title prefix) and worker `:8`. Their true source is `~/.claude/projects/**/*.jsonl`: outside the
repo, outside version control, machine-local, and subject to transcript pruning. I verified the strings
are there **today**; a future reader holding only this repo cannot. The manager file at least records a
transcript path; the worker file records none. Both assert "recovered verbatim" at a confidence the repo
alone cannot sustain.

**C verdict: current entry correct, nothing deleted, `:11` genuinely verbatim; count in `:12` wrong;
verbatim provenance is out-of-repo and self-cited in-repo. PASS with defects.**

---

## 4. Artifact D — `docs/reports/2026-07-30-session41-cyd-four-hook-claim.md`

### Append-only — CONFIRMED

```
$ wc -c docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
   24617
$ wc -l docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
     467
$ head -c 21718 docs/reports/2026-07-30-session41-cyd-four-hook-claim.md | wc -l
     421
```

21718 bytes = exactly 421 newlines, so byte 21718 is the newline terminating line 421 and the append
begins at line 422. Boundary inspected directly:

```
$ head -c 21718 ... | tail -c 200
 the escalation item is the R3 toggle. It is the only remaining step that would move
the phantom finding from *strongly evidenced* to *proven*, and it is not mine or the manager layer's to
authorise.

$ tail -c +21719 ... | head -c 300

---

## ERRATA 2 — 2026-08-03, `Praxis_build-cyd` fix unit (append-only; body above byte-unchanged)
...
```

Line 403 unchanged:

```
$ awk 'NR==403 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
403	## Result: PASS
```

**Independent** corroboration of prefix integrity — the audit was written 2026-07-30, *before* the
append, and cites two specific line numbers in this report:

```
$ awk 'NR>=104 && NR<=106 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-30-session41-cyd-audit.md
104	The subject report asserts the opposite. `docs/reports/2026-07-30-session41-cyd-four-hook-claim.md:385`
105	describes the worker file as "third correction **prepended**"; line 387 describes the manager file as
106	"Corrected in place by **the same pattern**."
```

Both still match at those exact line numbers:

```
$ awk 'NR==385 {print}' docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
| .../praxis-worker/project_commit-guards-block-scratch-repos.md | Corrected in place — third correction prepended, superseded text preserved verbatim, ... |
$ awk 'NR==387 {print}' docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
| .../praxis-manager/project_commit_guard_bypass.md | **Scope addition, declared.** ... Corrected in place by the same pattern. ... |
```

**S2 caveat, stated:** the file is untracked, so no git baseline exists. Byte count, line count, the
`:403` string, and the two pre-fix line citations are all consistent with a pure append, but an
**equal-length in-place substitution inside the prefix would not be caught** by these checks. The prefix
sha256 is `75e1f31c0764c315847d0edcecdcce55c36692effedd3d2ab0f1900c9ecc5d58`, which matches the "BEFORE"
hash recorded at `docs/reports/2026-08-03-session41-cyd-fix-worker1.md:147` — but that record is the
producer's own and is **not independent evidence**. Residual: UNVERIFIED at the byte level, strongly
evidenced at the structural level.

### Errata accuracy against `:33`, `:405`, `:408` — all three CORRECT

I read the subject lines myself.

**E2-1 vs `:33`.** Errata quotes `"declared, enabled, present on disk, and never loaded."`

```
33	The disputed fourth is a **phantom**: declared, enabled, present on disk, and never loaded. The chain
```
Exact. Its supporting references also check out:
```
29	| …of which actually **resolve and load** against this repo | **0** | **Strongly evidenced, R3-UNGRADED** — three convergent read-only lines |
36	**Explicitly UNGRADED:** the proposition *"its registration never enters the runtime registry."*
```
`:29` does mark it R3-UNGRADED; `:36` does declare it explicitly UNGRADED. The errata's point — that
`:33` states as flat fact what `:29`/`:36` mark ungraded — is sound. ACCURATE.

**E2-2 vs `:405`.** Errata quotes `"Established by direct read and independently re-run"`.

```
405	**What PASS covers:** the count is settled at **three** live Bash-matcher hooks, established by direct
406	read and independently re-run; ...
```
Exact (modulo the line break). Its side claim that the verdict table `:31` leaves the status cell empty:
```
31	| **Live Bash-matcher hooks gating this repo** | **3** | |
```
Empty. ACCURATE. ("deliberately" is an intent attribution the line itself cannot establish — noted, not
scored.)

**E2-3 vs `:408`.** Errata quotes `"The memory is corrected in place by the sanctioned pattern"`.

```
408	frontmatter surface is enumerated and closed; the memory is corrected in place by the sanctioned
409	pattern; ...
```
Exact. Its characterisation of the audit is also accurate:
```
$ awk 'NR>=80 && NR<=82 {printf "%d\t%s\n", NR, $0}' docs/reports/2026-07-30-session41-cyd-audit.md
80	`.claude/agent-memory/praxis-manager/project_commit_guard_bypass.md` places the correction at line 29,
81	mid-file. The body opens with the uncorrected original, and asserts the withdrawn count in live voice
82	at line 20, nine lines before any in-body correction marker:
$ awk 'NR==144 {print}' docs/reports/2026-07-30-session41-cyd-audit.md
without a preserved record. Property 2 is not met for either `MEMORY.md`, and the entry title was also
```
`:29` mid-file ✓, `:20` live ✓, "both `MEMORY.md` index lines" ✓ (audit says "either"). ACCURATE.

### Audit `Result: FAIL` — CONFIRMED

```
$ grep -n "Result:" docs/reports/2026-07-30-session41-cyd-audit.md
11:## Result: FAIL
```

The errata records this at `:427–429` (`"An independent audit of this report returned **Result: FAIL**"`,
`Check A FAIL, Check B FAIL`) and reaffirms at `:464` that it stands. Correct.

### DEFECT D-1 — dangling citation

```
454	reason. These four defects are repaired under the `Praxis_build-cyd` fix unit; see
455	`docs/reports/2026-08-03-session41-cyd-fix.md`.
```

```
$ ls -la docs/reports/2026-08-03-session41-cyd-fix.md
ls: docs/reports/2026-08-03-session41-cyd-fix.md: No such file or directory
```

The file on disk is `2026-08-03-session41-cyd-fix-worker1.md`. An errata whose entire subject is
citation discipline ships a citation that does not resolve.

### DEFECT D-2 — the errata over-claims its own repair

`:454` — "These four defects are repaired under the `Praxis_build-cyd` fix unit." Defect A-1 above shows
the repair of `project_commit_guard_bypass.md` is **incomplete**: an unmarked residue of the withdrawn
count survives at `:25` of an auto-loaded file, and the file's own opening guarantee that every
superseded passage is "marked where it stands" is false because of it. "Repaired" is above the evidence.

### DEFECT D-3 (minor) — "ERRATA 2" with no ERRATA 1 in this file

```
$ grep -in "errata" docs/reports/2026-07-30-session41-cyd-four-hook-claim.md
16:established pattern · **C** append an errata to the session-40 report, body byte-unchanged · **D** this
301:Identical prefix hash. Existing body, including the errata already present, is byte-unchanged.
409:pattern; the report errata is proven append-only by prefix hash; and the index and `HEAD` invariants
415:to Amear. The experiment is written up in the errata and above; it was not run.
425:## ERRATA 2 — 2026-08-03, `Praxis_build-cyd` fix unit (append-only; body above byte-unchanged)
466:**What is NOT changed by this errata:** the hook count. ...
```

`:301`'s "the errata already present" refers to the *session-40* report (per `:16`), not this one. This
file has no ERRATA 1. A reader hunting for it finds nothing.

### Minor note, not scored

E2-4 (`:459`) says the audit's ground was "no file under `docs/reports/` quotes it". The audit `:147`
gives **two** grounds: "no report quotes it, **and the path is untracked**". The errata names one and
calls it "correct" — incomplete, not inaccurate.

**D verdict: append-only proven at the structural level; errata quotes and characterisations of `:33`,
`:405`, `:408` are all accurate; audit FAIL correctly recorded. But one dangling citation and one
overclaim of repair. FAIL.**

---

## Summary table

| Artifact | P1 | P2 | P3 | Result |
|---|---|---|---|---|
| A `praxis-manager/project_commit_guard_bypass.md` | PASS | PASS | PASS | **FAIL** — unmarked four-hook residue at `:25` |
| B `praxis-worker/MEMORY.md` | n/a | `:7` verified, `:6` verified, `:8` truncated | **not met for `:8`** | **FAIL** |
| C `praxis-manager/MEMORY.md` | n/a | `:11` verified verbatim | PASS | PASS with defects (`:12` count wrong; provenance out-of-repo) |
| D `2026-07-30-...-four-hook-claim.md` | n/a | append-only proven | PASS | **FAIL** — dangling citation, repair overclaimed |

## Things I tried that did NOT break the artifacts

- Attacked P1 on artifact A: the correction really is the first body content, before any prose.
- Attacked P2/P3 on artifact A by offset arithmetic — +13/+19 is exactly consistent with insertion only;
  no deletion is possible in the audit-quoted span.
- Attacked the worker `:7` preserved line byte-for-byte against its cited source — IDENTICAL.
- Attacked the manager `:11` "recovered verbatim" claim by going to the named jsonl — it is there, twice,
  and the earliest-occurrence date is right.
- Attacked the `:9` NOTE's title-change reversal of the audit — the transcript record backs the memory,
  not the audit.
- Attacked every one of the errata's three self-quotes against the real `:33`, `:405`, `:408` — all
  accurate, including the `:29`/`:31`/`:36`/`:387` cross-references.
- Attacked the append-only claim with an independent pre-fix artifact (audit `:104–106` citing `:385`
  and `:387`) — holds.

## Files staged

None. This run was read-only. The only file written is this report, which is untracked and unstaged.

## Result: FAIL
