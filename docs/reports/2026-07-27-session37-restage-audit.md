# Session 37 — Cold audit of the staged restage split

**Auditor:** praxis-auditor (independent). Producer reasoning not read.
**Target:** staged index at HEAD `c1dec30`, branch `main`, 2026-07-27.
**Claim record graded:** `/Volumes/Sensidine/Praxis.build/docs/reports/2026-07-27-session37-restage-split.md` (untracked).

**Result: FAIL** — S1, S2, S3, S6. No commit token minted.

The index itself is clean. The report describing it is not.

---

## Verdict table

| Criterion | Verdict | Evidence / gap |
|---|---|---|
| S1 — Every claim in a report has pasted command output, not a description of output. | **FAIL** | The "Negative test — does the detector actually fire" section (lines 223-241) and the entire "Adversarial findings" section (242-296) contain **zero code fences**. Fence line numbers in the whole file: `68 80 84 105 116 127 131 142 148 154 159 169 178 187 194 200 209 216 335 343` — nothing between 216 and 335. Quantitative claims made with no output: "the detector reported 4 paths where 1 was claimed, 1 deletion where 0 was claimed, and flagged the mode flip"; "A secret scan across the staged diff returned only the word 'token'"; "a full `git ls-tree -r HEAD` versus `git ls-files -s` comparison". The scratch repo was deleted, so the control arms are also unreproducible. |
| S2 — No component is reported at a higher level than the evidence supports. | **FAIL** (producer report only; MANIFEST rows PASS) | Line 21 self-grades S1 as "Met. Every assertion below is backed by output the manager re-ran and pasted in this session." Falsified by the fence-line list above. Line 356 asserts "its detector was **proven** to fire on a deliberately wrong index" — the artifact contains no observation of that firing. That is asserted-level evidence reported at proven level. The six MANIFEST rows, by contrast, are correctly levelled — see section B below. |
| S3 — Every gate claimed working has been deliberately tripped at least once, with the block observed. | **FAIL** | Honest half: lines 236-239 explicitly decline S3 for the commit gate — "S3 is therefore **not** discharged for the commit gate by this unit, and no claim is made that it was." Failing half: line 240 claims "What is discharged is the index detector's positive control." That trip is described, never shown. A gate whose trip is asserted in prose, in a repo since deleted, has not been observed by this auditor. |
| S6 — Cross-block check: every approved deviation is tested against the specs of every other block it touches. | **FAIL** | The S6 section (297-330) is structurally serious and checks six blocks. But item 4, "Citation ordering", is one-directional: it verifies that the second commit's ledger rows will cite reports landing first. It never checks the reverse. Two of the six MANIFEST rows being committed cite `/docs/reports/2026-07-26-session34-manifest-amendment.md` (`:198-206` in the s9-control row and the audit row; `:163-164` in the audit row). That file is **untracked and not in HEAD**: `git ls-files --error-unmatch docs/reports/2026-07-26-session34-manifest-amendment.md` → `error: pathspec ... did not match any file(s) known to git`. The registry therefore lands with a citation that does not resolve on arrival — the exact failure item 4 exists to prevent. (The other cross-file citation, `docs/reports/2026-07-26-agent-stack-v2-triptests.md`, **is** tracked and its lines 54/128/142 resolve as quoted.) |
| S7 — Nothing is committed while any audit box is unchecked. | **PASS** | `git rev-parse HEAD` → `c1dec30c6516edcf7c79a78fce5c655e007d7ba2`, dated `2026-07-26 12:51:42 -0400`. `git log --since=2026-07-26T23:00` returns empty — no commit created. Nothing was committed. Per the 2026-07-26 per-change ruling, unrelated open items elsewhere do not bear. This audit returns FAIL, so the box for this change stays unchecked and the commit must not proceed. |

---

## A. Index composition and purity — PASS

```
$ git diff --cached --raw
:100644 100644 b09de40 39e4b94 M	MANIFEST.md
:000000 100644 0000000 b0363e8 A	docs/reports/2026-07-26-session36-adversarial-actor-hunt.md
:000000 100644 0000000 9c175d8 A	docs/reports/2026-07-26-session36-agent-key-audit.md
:000000 100644 0000000 1911583 A	docs/reports/2026-07-26-session36-agent-key-lab.md
:000000 100644 0000000 ac53d5a A	docs/reports/2026-07-26-session36-agent-key-s9-control.md
:000000 100644 0000000 de38b27 A	docs/reports/2026-07-26-session36-null-attack.md
:000000 100644 0000000 276c781 A	docs/reports/2026-07-26-session36-worker-trigger-probe.md
```

Exactly 7 paths. Every deletion column in `--numstat` is `0`. All modes `100644` on both
sides — the raw output is the check that catches a mode-only flip, which `--numstat`
would miss. `git diff --cached --summary` emits only `create mode 100644` lines, no
`mode change` line.

Nothing smuggled. `git status --porcelain` still shows all six other reports as `??`,
including both `Praxis_build-8sw` artefacts:

```
?? docs/reports/2026-07-26-session35-8sw-audit-round1.md
?? docs/reports/2026-07-26-session35-8sw-gate-park-conflict.md
```

## B. The six MANIFEST rows — PASS, with one defect named

Six added rows, one per staged report path, 1:1, no row describing any other file.
Every quoted verdict string was grepped against its source. All resolve byte-for-byte:

| Row | Standing claimed | Quote checked | Found |
|---|---|---|---|
| s9-control | HIGHEST-STANDING | `BLOCKED: shell write from praxis-master. Use Edit on a ledger, or dispatch a worker.` | :117, :136 |
| s9-control | payload "reproduced from source bytes at line 96" | `{"agent_type_present":true,...,"cmd":"echo hello > …/probeX.txt"}` | line 96, exact, elision included |
| s9-control | caveat carried not discharged | `Confirmed by reading, **not** separately trip-tested` / `Scope caveat (S2):` / `Two of the four workers hit a false null in this one task.` | :185 / :215 / :162 |
| null-attack | REFUTED the lab | `## RESULT: THE NULL IS FALSE. COUNTEREXAMPLE PRODUCED.` / `**BREAK FOUND**` | :10 / :326 |
| agent-key-audit | AUTHORITATIVE AS AN AUDIT VERDICT | `**Result: FAIL** — S1, S2, S4, S5, S7, S9. No token minted.` | line 5, byte-exact incl. `**` |
| agent-key-lab | SUPERSEDED INTERMEDIATE | `**NULL RESULT. The hypothesis is refuted by direct measurement.**` at :12; result line `**PASS** — ... decisive **negative** answer` at :285 | both |
| agent-key-lab | "grep for definition/resolve/praxis-master.md returns zero matches" | re-run: `grep -c -i 'definition\|resolve\|praxis-master.md'` → `0` | confirmed |
| actor-hunt | INTERMEDIATE, not superseded | `**FAIL (claim broken).** The claim's conclusion is falsified; its premise is not.` | :226 |
| worker-trigger-probe | LOWEST-STANDING | `Payload shape remains UNVERIFIED.` :123; `exit=0` :30,:40; `CLAUDE_CODE_VERSION=2.1.220 (Claude Code)` :57 | all |
| worker-trigger-probe | s9-control logs it as worker 1 | `Guard silent, exit 0. Payload not observed.` | s9-control :29 |

No row elevates a superseded artefact. The lab row demotes correctly and states the
confounder the lab itself never names. The `.claude/agent-memory/praxis-worker/project_agent-type-source.md`
correction the s9-control and lab rows both rely on is real — the file opens
`**This file previously recorded the opposite claim. That claim is REFUTED. Do not act on it.**`

**Defect (graded under S6, not S2):** two rows cite an untracked file as supporting
evidence. Its content on disk does support them (`session34-manifest-amendment.md:198-206`
shows the `agent_type` exit 2 / 142 B vs `agent_typeX` exit 0 / 0 B invented-key control;
`:163-164` shows "no other hook was in / the path"), so the claim is not false — but the
committed registry will point at a path the repository does not contain.

## C. Working-tree preservation — PASS

Index blob equals HEAD blob for all three, i.e. fully unstaged, not partially:

```
.claude/settings.json idx=4521f908d81018cd3d185e1d2eb7f426b5a58b88 head=4521f908d81018cd3d185e1d2eb7f426b5a58b88
DECISION_LOG.md       idx=824ec4e97f22b7e280a4112c454279a3d4e71a7c head=824ec4e97f22b7e280a4112c454279a3d4e71a7c
ISSUE_REGISTER.md     idx=bbe4055065ce34d74b7c389ffe1d90129bb2a5d1 head=bbe4055065ce34d74b7c389ffe1d90129bb2a5d1
```

Edits survive in the working tree, `git diff --numstat` → `1 0` / `32 0` / `4 0`, and the
payload is intact:

```
+"agent": "praxis-master",
```

`git diff --cached --numstat` for those three paths returns empty. Discarded-edit failure
mode did not occur.

## D. Producer report honesty — MIXED

Credited, and genuinely so:
- Lines 236-239 refuse to claim S3 on the commit gate and say why.
- F1 self-reports its own adversarial worker writing two files into the project tree,
  and declines to delete them. Both files exist; `.claude/agent-memory/` is untracked
  as a whole, so `git status --short` is indeed unaffected.
- F2 grades the worker's "still correctly blocks ... through any route" as an
  unsupported universal negative, then reads the source and marks its own bypass
  hypothesis "a hypothesis read off the source and not observed". The two cited lines
  are accurate: `gate-commit.sh:45` is the quote-scrubbing `sed`, `no-commit-guard.sh:20`
  is `\bgit\s+(commit|push|merge|rebase|tag)\b`.
- It also grades its own worker's S1 miss.

Overclaims found, all in the same place — evidence the manager did not produce itself:
- Line 21: "Every assertion below is backed by output the manager re-ran and pasted in
  this session." False for lines 223-296.
- Line 356: the detector "was **proven** to fire on a deliberately wrong index."
- The adversarial results are relayed as conclusions ("came back CONFIRMED", "returned
  only the word 'token'") — accepted on report, which is precisely what process-log
  item 6 says was not done for verification numbers.

Sections 1-7 (lines 61-222) are the strong part and are fully fenced. The failure is
that the one section licensing belief in those silences is the one section with no output.

## Token

**No commit token was minted.** This audit returns FAIL; a token is not minted on a FAIL,
and `.claude/state/` contains no token file.

## Scope

Graded: index composition, the six MANIFEST rows, working-tree preservation, producer
honesty. Not graded, per brief: the internal substance of the six session-36 reports.

**Result: FAIL**
