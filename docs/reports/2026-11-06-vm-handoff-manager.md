# Manager report — unit `2026-11-06-vm-handoff`

**Date:** 2026-11-06 · **Repo HEAD:** `234e4bc` (main) · **Written by:** praxis-manager · **Grades:** OBSERVED = command output pasted below; REPORTED = someone's statement; INFERRED = reasoning.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Task

Write the one VM handoff file Amear points the VM session at (`vm/2026-11-06-vm-handoff.md`; VM path `Z:\vm\2026-11-06-vm-handoff.md`, INFERRED from his share wording), the first two skills (`vm/skills/<name>/SKILL.md`), a reply-convention README (`vm/replies/README.md`), MANIFEST rows for every new file, and this report. Everything is left unstaged. Loop step c of D-2026-11-06-B.

## Authorisation (S5), quoted

- **D-2026-11-06-A item 2** (DECISIONS.md:1003, WHO: amear): "Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy." Tests: "a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. b. The VM agent loads a written skill and follows it correctly on a simple job."
- **D-2026-11-06-A item 3** (DECISIONS.md:1004, WHO: amear): "Praxis.build shared; admin Read & Write; staff Read Only; Everyone No Access. VM: \\192.168.1.204\Praxis.build mapped as Z:".
- **D-2026-11-06-B ruling 1** (DECISIONS.md:1063, WHO: amear): "the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot."
- **Ruling 5 defaults** (DECISIONS.md:1063): "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match; my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched; VM agent reads and reports the NT8 version; Code + auditor judge 2a/2b and log the lift under my ruling; VM agent on Z: while Code runs = second session, coordinate."
- **Settlements** (DECISIONS.md:1085–1092; column 3 is the master's decision under R-1104-2, not Amear's word):
  - item 3 (:1086): "The master adopts a working definition: the Claude agent running inside the Windows VM (a definition, not an observation; the VM agent's first reply confirms or corrects it). Its skills directory is reported by the VM agent itself in its first reply."
  - item 4 (:1087): "Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`; reference record `docs/reports/2026-11-01-three-strategy-results.md:73` (`:86` instrument)."
  - item 6 (:1089): "His lift covers the bridge install and its import; D-071 untouched. His words also say "what tests 2a/2b need"; whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6) stays in his words and is neither narrowed nor extended here."
  - item 7 (:1090): "The VM agent reads and reports it; Code records it."
  - item 8 (:1091): "Code + praxis-auditor judge 2a/2b and log the lift under his ruling".
  - item 9 (:1092): "It is a second session. Coordinate: Code does not run agents while the VM session writes; handover goes through the VM handoff file."
- **Hard limits** (DECISIONS.md:1063, WHO: amear): "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit."
- **Commission flag (f)** (DECISIONS.md:1104, S6 cross-block): "An exact-match reproduction (item 4) therefore needs the commission used then, not the amended $4.68."
- **Dispatch row** DECISION_LOG `[2026-11-06T22:11:54Z] WHO: praxis-master`, WHAT (excerpt, item 2): "VM HANDOFF unit (ruling 1, D-2026-11-06-A item 2 order, step c): ONE file at `vm/2026-11-06-vm-handoff.md` in the repo — the share IS the repo root (D-2026-11-06-A item 3: "Praxis.build shared" → VM path `Z:\vm\2026-11-06-vm-handoff.md`, INFERRED from his words; he confirms when he points the VM session at it) — plus skills under `vm/skills/<name>/SKILL.md`, replies expected under `vm/replies/`." The row was at line 463 when this unit read it; the adversary found it at 464 later (a row landed above it in the working tree meanwhile). It is cited by timestamp.

## Rubric criteria addressed (verbatim, `specs/SPEC_RUBRIC.md`)

- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S8 | No question that belongs to Amear is answered on his behalf.
- S13 (:119) — the standing limitation sentence, once per report (above, under the header; once in the handoff at its line 9).

## Workers dispatched

| id | Mode | Scope | Outcome |
|---|---|---|---|
| `ad46dbde3f09edc33` | ADVERSARIAL, read-only | the four `vm/` files vs DECISIONS.md, the bridge report, README@9664d9b, the baseline sources; S1/S2/S8/S13 + de-identification | `VERDICT: FAIL` — 3 MAJOR, 11 MINOR (full return below) |

The four `vm/` files were written by the manager directly. They are docs, not production code, and the 60-turn budget did not fit a BUILD worker plus a capture split. Only one adversary was dispatched, as the brief allows.

## Process log

1. Read the authorisation sources (DECISIONS.md:991–1106, DECISION_LOG dispatch row, rubric S1/S2/S8/S13), the bridge report (Summary, Q1–Q5, NEEDS AMEAR 221–236, Corrections 1–2 at 2860–2975), README@9664d9b lines 30–100 and 160–190, `config/config.json`, `pyproject.toml:10–16`, notes-2:88–115 and :161, three-strategy-results:73/:86/:108, csv-analyses:51, and the strategy's lines 116–120 and 298–306.
2. Wrote the handoff (sections 0–8), the two skills and the replies README.
3. Checked every DECISIONS.md line number cited. Fixed four that were wrong: item 2 → :1003, item 3 → :1004, S6 → :1104, de-identification → :1131/:1142.
4. Ran a quote checker (`quotecheck.py`, in the scratchpad) over every `"…"` string of 12+ characters, against DECISIONS.md, DECISION_LOG.md, the bridge report, the README and notes-2. It found two quotes that did not match: an ellipsis join and a capital letter. Both fixed. What is left MISSING is text this unit wrote (commands, reply templates, the pip question), not quotes from a source.
5. Ran the adversary. It returned FAIL. All 14 findings were fixed by a scripted pass (`fix1.py`, 25 exact-once replacements; `fix2.py`, 6). Each fix is grep-confirmed below.
6. Appended five MANIFEST rows. Captured the evidence.

**Deviation from the brief (S8 over the brief's letter).** The brief said to clone anonymously over HTTPS. The adversary's MAJOR 3 shows that doing so answers bridge NEEDS AMEAR 11, "How should the source reach the VM?", by acting on it. Ruling 5's list does not reach that question. So the handoff now asks Amear in his step-0 words: the route (HTTPS clone is labelled the master's proposal), the two-file set (NEEDS AMEAR 1), whether the request folders are acceptable (NEEDS AMEAR 3), and the sim account (NEEDS AMEAR 8). Step 3 waits on items 1–4 of those words, plus a Code verdict carrying `SNAPSHOT: confirmed`. Step 4 now also waits on a Code reply naming who sets the Strategy Analyzer tab. The master should know the walkthrough now has one more Amear touchpoint than the brief described.

## Verification evidence

Commands run from `/Volumes/Sensidine/Praxis.build`. Output pasted unedited.

~~~~
$ git rev-parse --short HEAD
234e4bc
$ wc -l vm/2026-11-06-vm-handoff.md vm/skills/praxis-vm-reporter/SKILL.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md vm/replies/README.md
     284 vm/2026-11-06-vm-handoff.md
      42 vm/skills/praxis-vm-reporter/SKILL.md
      40 vm/skills/praxis-nt8-bridge-backtest/SKILL.md
      11 vm/replies/README.md
     377 total
$ shasum -a 256 vm/2026-11-06-vm-handoff.md vm/skills/praxis-vm-reporter/SKILL.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md vm/replies/README.md
92e71e08c7bf82b685fd2099f02bfa6b843fd8b0bc341f7310a15d69c69feff5  vm/2026-11-06-vm-handoff.md
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  vm/skills/praxis-vm-reporter/SKILL.md
cf2445605114dabc79b80fb870f2aab00c0c708bfa85ac8a344e85c92d5181ad  vm/skills/praxis-nt8-bridge-backtest/SKILL.md
eac55350b2fb1ce49f6d6516a5db3e6fc98098197bbebc8de055395315f141de  vm/replies/README.md
$ git status --porcelain --untracked-files=all vm/
?? vm/2026-11-06-vm-handoff.md
?? vm/replies/README.md
?? vm/skills/praxis-nt8-bridge-backtest/SKILL.md
?? vm/skills/praxis-vm-reporter/SKILL.md
$ git diff --numstat MANIFEST.md
5	0	MANIFEST.md
$ git diff --numstat MANIFEST.md | wc -l
       1
$ shasum -a 256 ninjascript/PraxisNoiseAreaBreakout.cs
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
$ git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ git diff --quiet HEAD -- docs/reports/2026-11-06-cli-nt-bridge-code-read.md; echo rc=$?
rc=0
$ /usr/bin/grep -c -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/s13.txt vm/2026-11-06-vm-handoff.md
1
$ git -C /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge rev-parse HEAD
9664d9b255bfa34b120d88a481afe7741a4115e6
$ git show HEAD:MANIFEST.md | cmp - /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/MANIFEST.before; echo rc=$?
rc=0
$ git diff --no-index --numstat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/MANIFEST.before MANIFEST.md; echo rc=$?
5	0	/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/MANIFEST.before => MANIFEST.md
rc=1
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.v1.md
489faf5c58dbb887851884d62d6b6ab41a2f6657233320b897a323c8c316e729  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.v1.md
$ git diff --no-index --numstat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.v1.md vm/2026-11-06-vm-handoff.md; echo rc=$?
42	25	/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.v1.md => vm/2026-11-06-vm-handoff.md
rc=1
$ ls docs/reports/2026-11-06-vm-handoff-manager.md; echo rc=$?
ls: docs/reports/2026-11-06-vm-handoff-manager.md: No such file or directory
rc=1

$ for p in 'baseline stage when `require` is playback' 'exactly two files into NT8' 'Do not change PowerShell' 'five things' 'SNAPSHOT: confirmed' 'observes no value of the VM' 'Run it only if Amear' 'First list the folder' 'pytest>=7' 'CODE-cli-setup.md' 'names who sets the Strategy Analyzer tab' 'Load the second skill' 'do not run.' 'yours and Code' 'asked at step 0'; do printf '%s => ' "$p"; /usr/bin/grep -n -F -- "$p" vm/2026-11-06-vm-handoff.md | cut -d: -f1 | tr '\n' ' '; echo; done
baseline stage when `require` is playback => 27 
exactly two files into NT8 => 34 
Do not change PowerShell => 33 
five things => 47 
SNAPSHOT: confirmed => 89 247 
observes no value of the VM => 66 
Run it only if Amear => 101 
First list the folder => 106 
pytest>=7 => 140 
CODE-cli-setup.md => 142 252 
names who sets the Strategy Analyzer tab => 148 
Load the second skill => 150 
do not run. => 199 
yours and Code => 229 
asked at step 0 => 276 279 

$ /usr/bin/grep -n -F -e 'STATUS.md` files' vm/skills/praxis-vm-reporter/SKILL.md | cut -c1-60; /usr/bin/grep -n -F -e 'names who sets' -e 'do not run.' -e 'NT8Bridge' vm/skills/praxis-nt8-bridge-backtest/SKILL.md | cut -c1-60; /usr/bin/grep -n -F 'CODE-<slug>' vm/replies/README.md | cut -c1-60
11:- Read only. Change nothing in NT8, nothing in Windows, n
13:Start only if `Z:\vm\replies\` holds your `<ts>-cli-setup
21:- Write only under `Z:\vm\replies\` and `C:\praxis\2a-con
31:3. Read back every one of the 21 settings in the handoff'
3:This folder is the only place on the share the VM agent ma
~~~~

The handoff's line numbers in the adversary's return refer to v1 (`489faf5c…`, 25 lines fewer). The fixes added 42 lines and removed 25, giving the final file (`92e71e08…`, 284 lines).

## Adversarial findings

### Full return of worker `ad46dbde3f09edc33` (ADVERSARIAL, read-only, over v1), pasted unedited

~~~~
I found three MAJOR and eleven MINOR breaks. The commission, the settings, the hash, the protected name and the limitation sentence all hold. I wrote no files, so there is no report path.

## Findings

**1. MAJOR: the install is not gated on the snapshot.** Files: `vm/2026-11-06-vm-handoff.md:83`, `:64`, `:76`.
- Ruling 1 says "installs cli-nt-bridge via terminal, after a VMware snapshot" (DECISIONS.md:1063).
- Step 3's only gate is `Z:\vm\replies\<ts>-CODE-2b-verdict.md exists and its first line is 2b: PASS` (:83).
- The snapshot only shows up as self-report item 10: "Did you get Amear's snapshot sentence (step 0)? Paste it." (:64). An answer of "no" does not stop anything.
- The 2b PASS test only checks format: "the reply exists, and it matches the skill's required format" (:76). Nothing tells Code to check the snapshot sentence before writing PASS.
- So the agent can say "no snapshot", get 2b PASS, and install. That breaks Amear's ruling.

**2. MAJOR: a fact contradicts Correction 2 (a false "nobody has").** `vm/2026-11-06-vm-handoff.md:60` says "Amear reported 8.1.8.4 (`report:2967`); no one has observed it on this VM (`report:2965`)."
- report:2965 only says `This report observes no value of the VM's NT8 build.`
- The very next lines list readings taken on the VM. report:2967: `Amear's 2026-10-31 notes say "The NT8 version reads 8.1.8.4."` Correction 2 also cites an in-VM agent's 8.1.7.2 from MsiInstaller events, and "Claude Code on the VM" writing "NinjaTrader 8.1.8.4".
- Amear reading the version is an observation. The handoff turns "this report saw none" into "no one ever saw it", which Correction 2 replaced on purpose.

**3. MAJOR (S8): one of Amear's open questions is answered by acting on it.** Files: `vm/2026-11-06-vm-handoff.md:90`, `:95`, `:262`.
- Bridge NEEDS AMEAR 11 (report:235): "How should the source reach the VM? Options: the README's SSH clone…, an anonymous HTTPS clone on the VM, or a copy through the Z: share."
- The handoff runs `git clone https://github.com/eman007/cli-nt-bridge C:\praxis\bridge-src` (:90). It calls this "the master's dispatch choice" and says "If Amear names another route, follow his" (:95). Section 8 marks it "**Amear's.**" but goes ahead anyway (:262).
- The master has no delegation for this. Ruling 5 covers "Handoff NEEDS AMEAR 1, 3–10, 15–17, 19", which is the numbering of the 11-06 voice-session handoff, not the bridge report's list.
- The same question's pip half is handled as STOP-and-ask (:130). The source-route half is handled as do-it-now.

**4. MINOR: the install also goes ahead on two other open questions.**
- Bridge NEEDS AMEAR 1 ("which files", :252) is open, and the two-file install goes ahead anyway.
- Bridge NEEDS AMEAR 3 (is an unauthenticated drop folder acceptable, :254) is open, and step 3 creates that folder. From then on, any process running as the VM user can drop `flatten`.
- Both can be defended, because ruling 1 orders the install. But section 8 calls them "**Amear's**" while the steps act on them.

**5. MINOR: the pip question understates what pip would install.** `vm/2026-11-06-vm-handoff.md:129` says the last line installs "`jsonschema`, `numpy`, `pyarrow` and `tzdata`".
- The `.[dev,report]` extras also install pytest and matplotlib:
```
dev = ["pytest>=7"]
report = ["matplotlib>=3"]
```
- README:45 itself says `report adds matplotlib for --pdf`. Amear would be asked about pip with an incomplete package list.

**6. MINOR: the 2a skill is orphaned.** A grep of the handoff for `praxis-nt8-bridge-backtest` gives 0 hits. Step 4 never says to load `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`, even though the skill's line 8 claims "Source: … step 4."

**7. MINOR: the step 3.2 check comes after the copy.** The copy commands (:102–103) come before the listing (:104). The rule "If a file of either name is already there, STOP before copying" (:106) only comes after the block. An agent typing the block in order copies first.

**8. MINOR: write-scope limits contradict the steps.**
- Limit 10 (:34) names only `Z:\vm\replies\` and `C:\praxis\`, but step 3.2 writes to `Documents\NinjaTrader 8\bin\Custom\AddOns`.
- The 2a skill's line 21 says "Write only under Z:\vm\replies\ (and C:\praxis\2a-config.json)". But `backtest` writes `trigger/backtest_<id>.json` and creates the folders: `run_backtest` calls `ntio.ensure_bridge_dirs()`, whose comment reads `"""Create <NT8>/NT8Bridge/{trigger,result}…`.
- The reporter skill's line 11 says "nothing on Z: except the one reply file", which conflicts with the STATUS files.

**9. MINOR: the format rules don't agree with each other.**
- Section 7 (:214–216) says every reply starts with `REPLY-TO:`, but the gate at :83 needs Code's verdict file to start with `2b: PASS`.
- `vm/replies/README.md:3` says Code replies are "prefixed `CODE-`", but the names are `<ts>-CODE-…`.

**10. MINOR: the pip-approved run has no session markers.** Section 7, items 10→11 (:239–240), lists no STARTED/FINISHED and no reply file around running the pip command Code names (:131). The venv is never created by any step, yet 4.5 assumes "venv active". `Activate.ps1` may also need an execution-policy change, and no limit covers that.

**11. MINOR: no gate on who sets the Strategy Analyzer tab.** Step 4.3 (:156) says "Who sets the tab by hand (Amear, or you if you can drive the GUI) is not decided here." The step 4 gate (:137) does not require that to be decided first. The two files also disagree on a mismatch: the 2a skill's line 31 says STOP, while the handoff's 4.6 counts it as FAIL and still runs.

**12. MINOR: a safety reason drops its conditions.** Line :27 says "`playbackrun` disconnects every non-Playback connection". report:184 says this happens only on the baseline stage, "when `require` is playback and not `checkOnly`", and report:188 grades it INFERRED. The rule it supports is stricter, so no harm is done.

**13. Checks that held (Q4, Q6, Q7):**
- **Settings:** the 21-row table matches notes-2:111.
- **Commission:** "Per unit 1.48" and $2.96 are right (notes-2:104–106; csv-analyses:51 `commission/trade={'2.96': 1190}`; 1190 × 2.96 = $3,522.40, which matches three-strategy-results:73). $4.68 is excluded.
- **Pass mark:** PASS is exactly `1190` / `197327.60`.
- **Hash:** it matches.
```
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  ninjascript/PraxisNoiseAreaBreakout.cs
```
  The same hash comes from `git show HEAD:…`. Last commit to the file: 719ab11.
- **Limitation sentence (S13):** it appears once in the handoff, at line 9. It also appears once in the 2a skill (line 10) and not at all in the reporter skill or `replies/README.md`.
- **Protected name:** absent from all four files. Method: I took the words that commits a42038e and 7d9be8e both introduced. All the non-dictionary candidates scored 0 hits in the four files; the only two hits were dictionary words. I did not print the name.

**14. Citation checks that held (Q3, Q5):**
- **Bridge report lines:** 28, 31, 40–42, 47, 59, 63–68, 89, 113, 114, 127, 128, 140–146, 152–159, 173, 178, 184, 188, 2866, 2868, 2959–2962, 2967 and 2973 all say what the handoff says.
- **README lines:** 35, 41, 43–45, 52, 54, 174 and 182 match at `9664d9b255bfa34b120d88a481afe7741a4115e6`.
- **Ledger lines:** the DECISIONS.md lines (960, 1063 "Hard limits unchanged…", 1086–1092, 1104) match. The DECISION_LOG dispatch row is at line 464, not 463; the handoff cites it by timestamp, so that is fine.
- **Limits (Q1):** every limit you listed is present in the handoff.
- **S2:** nothing is claimed as working. Line 14 says "Nothing in this file has been tried." The only S2 break is the false negative in finding 2.

VERDICT: FAIL
~~~~

### Disposition (each fix grep-confirmed in the Verification evidence above)

| # | Sev | Fix (final handoff line) |
|---|---|---|
| 1 | MAJOR | Step 3 gate (:89) now needs `2b: PASS` **and** `SNAPSHOT: confirmed` in Code's verdict, written only after Code reads Amear's step-0 words in the self-report. It also needs his words on items 2–4. Section 7 item 5 (:247). |
| 2 | MAJOR | :66 now quotes `report:2965` exactly and lists the three REPORTED values with dates (`report:2966–2968`). It ends "Code has observed none of them." |
| 3 | MAJOR | Source route asked at step 0, item 2 (:47 ff.). The HTTPS clone is labelled "the master's proposal" and runs "only if Amear's step-0 words chose it" (:101). Section 8 row 11 updated (:279). |
| 4 | MINOR | File set (NEEDS AMEAR 1) and request folders (NEEDS AMEAR 3) asked at step 0, items 3–4; step 3 waits on them. Section 8 rows 1 and 3 (:276 area). |
| 5 | MINOR | :140 lists `pytest>=7` and `matplotlib>=3` (`pyproject.toml:14–15@9664d9b`). The pip question names the extras. |
| 6 | MINOR | Step 4 now loads `praxis-nt8-bridge-backtest` (:150); if it and step 4 disagree, STOP. |
| 7 | MINOR | 3.2 now lists first, STOPs on a same-named file, then copies and lists again (:106 ff.). |
| 8 | MINOR | Limit 10 (:34) names the AddOns copy, the venv and the bridge's own request/result writes. Both skills updated. |
| 9 | MINOR | Section 7 says the header applies to "yours and Code's" replies (:229). The gate checks "holds the line `2b: PASS`". README names `<ts>-CODE-<slug>.md`. |
| 10 | MINOR | `CODE-cli-setup.md` → STARTED → `cli-setup.md` → FINISHED (:142, section 7 items 10–13, :252). Limit 9 (:33) forbids execution-policy changes and points to the README:48 fallback. |
| 11 | MINOR | Step 4 gate (:148) needs `CODE-go-2a.md` to name who sets the tab, as Amear decides. 4.3 now STOPs on a mismatch (:199). 4.6 FAIL covers run results only. |
| 12 | MINOR | :27 now carries the baseline-stage condition and the INFERRED grade. |

**What was not re-tested.** Findings 1–12 are fixed in text, and each fix is present (grep above). The fixed version (`92e71e08…`) has had **no independent adversarial pass**: the brief allows one adversary, and it read v1. Whether the fixes bring in new defects has not been checked by anyone but the writer. Each round of wording-level fixes has bred new MINOR findings in past units. The master decides whether a fresh read-only pass or the auditor grades v2.

**Negative test (stress-test step 5).** Not applicable as a trip test: this unit has no gate or hook to trip. The handoff's gates are text instructions to an agent that has not run them. No one has tried them, so whether they hold is untested (S2).

## S6 cross-block check

- F1–F4 (`specs/SPEC_RUBRIC.md` F-sections): untouched. No code, template, hook, config or strategy file was edited. `ninjascript/PraxisNoiseAreaBreakout.cs` was only hashed.
- D-2026-11-06-C (cost model $4.68) vs test 2a: the handoff keeps 2a on the run's own PRAXIS template (1.48 per unit, $2.96 per trade), per DECISIONS.md:1104. The amended figure is not used for the reproduction. The cost model file is not touched.
- D-071, the 2026-11-05T23:50:09Z limits and the 2026-10-28 in-VM ruling: no limit is lifted by this unit. Step 4 waits on Amear's word on D-2026-11-06-A NEEDS AMEAR 6.
- Nothing was sent toward the VM, `Z:`, the share, or NT8. Nothing was downloaded. Nothing was run from the clone: only `git rev-parse`, `awk`, `sed` and `grep` read it.
- The parallel praxis-auditor's files (`.claude/`, `scripts/`, DECISIONS.md, ledgers): not touched by this unit.

## Files staged

None. All new files are untracked and MANIFEST.md is modified in the working tree only. The real index is unchanged from the unit's start:

~~~~
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
~~~~

New files (untracked): `vm/2026-11-06-vm-handoff.md`, `vm/skills/praxis-vm-reporter/SKILL.md`, `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`, `vm/replies/README.md`, and this report, `docs/reports/2026-11-06-vm-handoff-manager.md`. Modified (unstaged): `MANIFEST.md` (+5 rows).

## Result

**Result: FAIL**

Why FAIL and not PASS: the one adversarial pass permitted returned `VERDICT: FAIL` (3 MAJOR, 11 MINOR) on v1. All of its findings are fixed in text and grep-confirmed. But the fixed v2 has not survived an independent attack, and "Survives all six: mark PASS" is not met. Partial is FAIL. Every deliverable exists, and the mechanical checks pass (S13 count 1, Mac hash, unchanged index, MANIFEST +5/−0). What it needs: one fresh read-only adversary or the auditor over v2, sha `92e71e08c7bf82b685fd2099f02bfa6b843fd8b0bc341f7310a15d69c69feff5`. Separately, the master should note the S8 deviation: step 0 now carries four questions to Amear.

## Correction 1 (2026-11-06, after audit FAIL 1; appended, nothing above edited)

### Authorisation, quoted

DECISION_LOG.md row `[2026-11-06T22:45:00Z] WHO: praxis-master` (working tree), WHAT, excerpt: "**UNIT `2026-11-06-vm-handoff` — AUDIT FAIL 1 (S8 + S1; S2 PASS); ONE correction dispatched (strike 1 of 2).** … **BLOCKING S8:** step 3.3 (handoff :122) has the VM agent "open the NinjaScript Editor and compile (F5)" — ruling 1 says "installs cli-nt-bridge via terminal"; the bridge README (:54@9664d9b) makes the FIRST compile a hand step inside NT8 … No ruling covers the agent driving NT8's GUI. **S1:** manager report :47–48 describes two results ("fixed four [line numbers] that were wrong"; the quote checker's two mismatches) without pasted output; "14 findings fixed" vs 12 in the pasted return. MINOR: sim account asked (step 0 item 5) but no step gates on the answer …; :171 "every setting from Amear's C4 line" — 19 of 21 rows are from notes-2:111, row 1 (Strategy) unsourced, row 2 from report:114; value mismatches 0; step 1 item 8 reads NT8's Connections list — read-only, but nothing covers it. … Correction scope: handoff in place (its own uncommitted text; before/after shas + full diff pasted): step 0 item 6 = the F5 question in his words; step 3.3 becomes "wait for his word; if he says hand step, he compiles and tells the VM session; if he allows GUI, the agent compiles"; §8 row 2 reworded …; step 4 (and any account-touching step) gated on item 5 as well; :171 attribution split (19 from notes-2:111, Strategy from report:93, Backtest type from report:114); step 1 item 8 either removed or labelled … (prefer removal — nothing needs it). Skills updated to match. Report: append `## Correction 1` with the two missing outputs pasted, the 12-vs-14 count corrected, the diff of the handoff edits, and a fresh read-only adversary over the edited handoff (its FULL return pasted) — the auditor re-attacks after."

### Rubric criteria addressed (verbatim, `specs/SPEC_RUBRIC.md`)

- S1 | Every claim in a report has pasted command output, not a description of output.
- S2 | No component is reported at a higher level than the evidence supports. Specified ≠ implemented ≠ tested ≠ tested under failure.
- S8 | No question that belongs to Amear is answered on his behalf.

### Workers dispatched

| id | Mode | Scope | Outcome |
|---|---|---|---|
| `a19e9d3fb95731faf` | ADVERSARIAL, read-only | the edited handoff (sha `616bff24…`) + both skills + replies README; S8 inventory, gate consistency, compile path, account gate, citations, de-identification, S2 | `VERDICT: FAIL` — 3 MAJOR, 9 MINOR, 0 BLOCKING (full return below) |

The edits were made by the manager directly, as in the first pass: docs, not production code, written as exact-once scripted replacements (`c1fix.py` 15, `c1fix2.py` 2 + 4, a one-line grammar fix, then `c1fix3.py` 17 + 6 after the adversary). Scripts are in the scratchpad.

### Process log

1. Copied the four `vm/` files and this report to `scratchpad/orig/` before any edit (they are untracked, so `git diff` cannot show the change). The handoff copy's hash is the brief's `92e71e08…` (pasted below).
2. Applied the audit's fixes: (a) step 0 item 6, in the brief's words, with `README.md:54@9664d9b`, `report:31`, `report:140`; (b) step 3.3 split into the two paths Amear may choose, plus a STOP when his words name neither; (c) section 8 row 2 reworded; (d) 4.3's "if you can drive the GUI" aligned with item 6, and the go-2a reply now names who reads the tab and the template back; (e) the step 3 gate lists items 2–6. MINOR 1: limit 1 and both gates wait on item 5. MINOR 2: the attribution is split by row. MINOR 3: step 1 item 8 is removed; the Help → About read is kept and its cover is stated.
3. Re-ran the two S1 checks (below).
4. Dispatched one adversary. It returned FAIL with 3 MAJOR and 9 MINOR findings, none BLOCKING.
5. Fixed the 3 MAJOR findings and 7 of the MINOR ones (two in part). This was `c1fix3.py`: 31 changed diff lines in the handoff and 12 in the 2a skill, as counted below. **This fixed text has not been re-attacked.** The brief allows one adversary, and it read `616bff24…`, not the final `9c9fa56e…`.
6. Re-ran the quote checker on the final file and captured all the evidence below in one runner pass (`c1-run.py`, each command run with `/bin/bash -c` from the repo root).

**Deviation from the brief's letter (limit 1).** The brief quotes "no step runs until item 5 is answered". Read literally, that would also block step 1 (the self-report) and step 2 (test 2b). Neither touches an account. And step 1 item 9 tells the agent to report it if Amear's words are missing. So limit 1 reads: "No step runs until item 5 is answered (section 2), except steps 1 and 2, which touch no account: steps 3 and 4 wait on Amear's words naming the account." The adversary checked the exception and found it sound (its "Account exception" item). The master may tighten it to the literal form.

**Corrected count (S1, the first section's step 5).** The first section's step 5 says "All 14 findings were fixed". The real count is **12**: 3 MAJOR and 9 MINOR. Items 13 and 14 of that return are "Checks that held", not findings. The adversary's own opening ("three MAJOR and eleven MINOR") and the first section's workers table ("3 MAJOR, 11 MINOR") both count those two as findings. The disposition table above lists exactly 12. The count is pasted below.

### Verification evidence

Commands run from `/Volumes/Sensidine/Praxis.build` through the runner. Output pasted unedited. `orig/*.md` are the pre-edit copies; `handoff.c1a.md` and `bt.c1a.md` are the copies taken just before `c1fix3.py`, i.e. the text the adversary attacked.

**S1 item 1, the DECISIONS.md line numbers.** For each cited line, the check tests that a phrase the handoff attributes to it is on that line. It prints only line number, HIT/MISS and the anchor phrase, never the line itself, because :1142 is next to the protected-title material. The final handoff no longer cites :1090: the step 1 item 6 citation was moved to Amear's ruling-5 words at :1063 (adversary finding 8). Its TSV row is still in the table and still HITs. The four lines the first pass corrected (:1003, :1004, :1104, and :1131/:1142) all HIT.

**S1 item 2, the quote checker over the edited handoff.** The script (`cat` below) flags every `"…"` string of 12+ characters that does not appear in the five sources. The first pass's two mismatches are recovered from that unit's own transcript (block 2 below). The transcript is the first-pass manager's session file under `~/.claude/projects/`. It is machine-local and not version-controlled, so the citation holds only on this Mac. At jsonl line 144 (22:19:41Z) the run lists `MISSING 8: Praxis.build shared … mapped as Z:`, which is the ellipsis join, and `MISSING 99: a one-file deploy should therefore fail to compile`, which is the capital letter: the source has "A one-file …" (count 1) and not the lower-case form (count 0). At line 156 (22:19:55Z) the next run lists neither (count 0). What can be shown is today's run: 49 OK, 18 MISSING. The 18 MISSING are this unit's own text, none of them quotes from a source:
- commands and paths (`$D\…`, `yyyyMMdd…`);
- reply templates ("Compile by: Amear", "Compile: clean", "could not read…");
- the pip question this file asks;
- a skill heading ("Required reply format");
- "you should see".

Line 274 is a pairing artefact: the regex paired the closing quote of `"import"` with the next opening quote. The ruling-1 quote on that line is checked on its own just after the list: 2 hits in DECISIONS.md.

Block 1, this correction's captures:

~~~~
$ git rev-parse --short HEAD
234e4bc
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/handoff.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/bt.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/rep.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/readme.md
92e71e08c7bf82b685fd2099f02bfa6b843fd8b0bc341f7310a15d69c69feff5  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/handoff.md
cf2445605114dabc79b80fb870f2aab00c0c708bfa85ac8a344e85c92d5181ad  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/bt.md
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/rep.md
eac55350b2fb1ce49f6d6516a5db3e6fc98098197bbebc8de055395315f141de  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/readme.md
$ shasum -a 256 vm/2026-11-06-vm-handoff.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md vm/skills/praxis-vm-reporter/SKILL.md vm/replies/README.md
9c9fa56e6760036d11cc5f94fa1bc5c52c02228ff1a77b272204568a7e99233f  vm/2026-11-06-vm-handoff.md
e06c40c4c9dbc99d15988ce5823602d263a4f359d4e6ec1017be920ea84f2b08  vm/skills/praxis-nt8-bridge-backtest/SKILL.md
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  vm/skills/praxis-vm-reporter/SKILL.md
eac55350b2fb1ce49f6d6516a5db3e6fc98098197bbebc8de055395315f141de  vm/replies/README.md
$ wc -l /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/handoff.md vm/2026-11-06-vm-handoff.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/bt.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md
     284 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/handoff.md
     288 vm/2026-11-06-vm-handoff.md
      40 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/bt.md
      40 vm/skills/praxis-nt8-bridge-backtest/SKILL.md
     652 total
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/handoff.md vm/2026-11-06-vm-handoff.md; echo rc=$?
12c12
< `report:` below means `docs/reports/2026-11-06-cli-nt-bridge-code-read.md` (committed in `234e4bc`; on the VM, `Z:\docs\reports\2026-11-06-cli-nt-bridge-code-read.md`). Its Corrections 1–2 (`report:2860–3200`) supersede lines 29, 32, 81 and 165–167. `README.md:N@9664d9b` means line N of the bridge's README at commit `9664d9b`.
---
> `report:` below means `docs/reports/2026-11-06-cli-nt-bridge-code-read.md` (committed in `234e4bc`; on the VM, `Z:\docs\reports\2026-11-06-cli-nt-bridge-code-read.md`). Its Corrections 1–2 (`report:2860–3200`) supersede lines 3, 5, 29, 32, 81, 135, 165–167, 236 and 240. `README.md:N@9664d9b` means line N of the bridge's README at commit `9664d9b`.
25c25
< 1. **Account:** Sim101 only, or the sim account Amear names. No live account, ever. Which account the tests use is still Amear's question (bridge NEEDS AMEAR 8, `report:232`).
---
> 1. **Account:** Sim101 only, or the sim account Amear names. No live account, ever. No step runs until item 5 is answered (section 2), except steps 1 and 2, which touch no account: steps 3 and 4 wait on Amear's words naming the account. Which account the tests use is still Amear's question (bridge NEEDS AMEAR 8, `report:232`).
27c27
< 3. **No connection changes (D-071).** No new NT8 connection, no reconnect, no disconnect. Amear: "D-071 untouched" (DECISIONS.md:1063); "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." (DECISIONS.md:1063). Why it matters here: `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun`, on its baseline stage when `require` is playback, disconnects every non-Playback connection (`report:184`; the D-071 consequence is INFERRED, `report:188`).
---
> 3. **No connection changes (D-071).** No new NT8 connection, no reconnect, no disconnect. Amear: "D-071 untouched" (DECISIONS.md:1063); "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." (DECISIONS.md:1063). Why it matters here: `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun`, on its baseline stage when `require` is playback, disconnects every non-Playback connection (`report:184`; the D-071 consequence is INFERRED, `report:188`). **Do not start, close or restart NinjaTrader.** Starting it may bring connections up; whether it does on this VM is UNVERIFIED. If a step needs NT8 running and it is not, STOP and reply. Starting it is Amear's.
34c34
< 10. **Write only under `Z:\vm\replies\`** on the share. Never edit, move or delete any other file on Z:. Off the share, write only what a step names: the clone, its venv and `2a-config.json` under `C:\praxis\` (steps 3–4), and exactly two files into NT8's `bin\Custom\AddOns` (step 3.2). The two bridge commands of step 4 write their own request and result files under `Documents\NinjaTrader 8\NT8Bridge\` (`report:52`, `report:67`); that is expected.
---
> 10. **Write only under `Z:\vm\replies\`** on the share. Never edit, move or delete any other file on Z:. Off the share, write only what a step names: the clone, its venv and `2a-config.json` under `C:\praxis\` (steps 3–4), exactly two files into NT8's `bin\Custom\AddOns` (step 3.2), and the two SKILL.md copies into your skills directory (steps 2 and 4). NT8's own compile output (step 3.3) and the `NT8Bridge` folders the loaded AddOn creates (step 3.4) are NT8's writes, not yours. The two bridge commands of step 4 write their own request and result files under `Documents\NinjaTrader 8\NT8Bridge\` (`report:52`, `report:67`); that is expected.
47c47
< - Then tell the VM session, in your own words, five things. The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours:
---
> - Then tell the VM session, in your own words, six things. The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours:
52,53c52,54
<   5. which sim account (bridge NEEDS AMEAR 8, `report:232`).
< - Anything you leave out, the VM agent does not assume. Step 3 does not start until items 1–4 are answered in your words.
---
>   5. which sim account (bridge NEEDS AMEAR 8, `report:232`);
>   6. who performs the one in-NT8 compile (NinjaScript Editor → F5) — Amear by hand, or the VM agent driving NT8's window? The first compile is a step inside NT8, not a terminal command (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"; `report:31`: "Installing means copying C# into `bin\Custom\AddOns` and compiling it in NT8"; `report:140`). Ruling 1 settles the terminal install and its order; it does not say whose hand presses F5.
> - Anything you leave out, the VM agent does not assume. Step 3 does not start until items 1–6 are answered in your words.
66c67
< 6. NT8 version from NinjaTrader → Help → About (D-2026-11-06-A item 1; settlement 7, DECISIONS.md:1090: "The VM agent reads and reports it; Code records it."). Copy the text exactly. The bridge report "observes no value of the VM's NT8 build" (`report:2965`). The repo carries REPORTED values that differ by date: 8.1.7.2 from installer events, 2026-10-19 (`report:2966`); 8.1.8.4 per Amear, 2026-10-31 (`report:2967`); 8.1.8.4 per Claude Code on the VM, 2026-11-02 (`report:2968`). Code has observed none of them.
---
> 6. NT8 version from NinjaTrader → Help → About (D-2026-11-06-A item 1). Amear's own words cover this one read: "VM agent reads and reports the NT8 version" (ruling 5, DECISIONS.md:1063). The Help → About route is the master's (DECISION_LOG `2026-11-06T22:11:54Z`). It is the only NT8 window step 1 opens. If NT8 is not running, do not start it (limit 3): write "could not read: NT8 not running". Copy the text exactly. The bridge report "observes no value of the VM's NT8 build" (`report:2965`). The repo carries REPORTED values that differ by date: 8.1.7.2 from installer events, 2026-10-19 (`report:2966`); 8.1.8.4 per Amear, 2026-10-31 (`report:2967`); 8.1.8.4 per Claude Code on the VM, 2026-11-02 (`report:2968`). Code has observed none of them.
68,70c69,70
< 8. Connected to what: read the Control Center's Connections list as it stands (name and status of each). Read only.
< 9. Your Documents folder: `[Environment]::GetFolderPath('MyDocuments')` — paste the output. NT8's folders sit under it.
< 10. Amear's step-0 words (the five items of section 2). Paste them word for word. If you got none, say so.
---
> 8. Your Documents folder: `[Environment]::GetFolderPath('MyDocuments')` — paste the output. NT8's folders sit under it.
> 9. Amear's step-0 words (the six items of section 2). Paste them word for word. If you got none, say so.
89c89
< **Gate:** start only when all of these hold. (a) `Z:\vm\replies\<ts>-CODE-2b-verdict.md` exists and holds the line `2b: PASS`. (b) The same file holds the line `SNAPSHOT: confirmed` — Code writes it only after reading Amear's step-0 words in your self-report. (c) Amear's words answer section 2 items 2–4 (route, file set, request folders). If any fails, do not start. Write `STARTED` first.
---
> **Gate:** start only when all of these hold. (a) `Z:\vm\replies\<ts>-CODE-2b-verdict.md` exists and holds the line `2b: PASS`. (b) The same file holds the line `SNAPSHOT: confirmed` — Code writes it only after reading Amear's step-0 words in your self-report. (c) Amear's words answer section 2 items 2–6 (route, file set, request folders, sim account, who compiles), and the answers let the steps run as written: item 3 accepts the two files of 3.2, item 4 accepts the request folders, item 5 names a sim account. A no, a different file set, a condition, or anything unclear is not a yes: STOP, quote his words in a reply, and wait. Do not adapt the steps. If any fails, do not start. Write `STARTED` first.
122c122,125
< **3.3 Compile in NT8.** Open the NinjaScript Editor and compile (F5) (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"). NT8 compiles "the whole tree" (`report:141`).
---
> **3.3 Compile in NT8 — wait for Amear's word on section 2, item 6.** The README's first compile is a step inside NT8 (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"). NT8 compiles "the whole tree" (`report:141`). The bridge's own `compile` command is not permitted (section 1, limit 4). Who presses F5 is Amear's (item 6). This file assumes neither path. Follow only the path his words name:
> - **If he does it by hand:** after 3.2, wait. Do nothing in NT8. When Amear tells you he has compiled, paste his words, word for word, and the result he gives you (clean, or the error lines) into the reply.
> - **If he lets you drive NT8's window for this compile:** open the NinjaScript Editor, press F5, and copy what the editor shows. Do nothing else in NT8's windows. His word covers this one compile only; it does not cover the Strategy Analyzer tab (step 4.3).
> - **If his words do not clearly name one of the two:** STOP and reply. Do not choose.
124c127
< - **Reply line:** "Compile: clean" or the error lines.
---
> - **Reply line:** Amear's item-6 words, then "Compile by: Amear" or "Compile by: VM agent", then "Compile: clean" or the error lines.
141c144
< - So: run `python --version` in `C:\praxis\bridge-src` and paste it. Create no venv yet. Then **STOP before `pip`.** Write `Z:\vm\replies\<ts>-STOP-pip.md` asking: "May `pip` download the bridge's packages on the VM — the four base packages, and the `dev`/`report` extras (pytest, matplotlib) or not (bridge NEEDS AMEAR 11)?" Write `FINISHED`. Wait for a Code reply that quotes Amear's answer.
---
> - So: run `python --version` in `C:\praxis\bridge-src` and paste it. Create no venv yet. Then **STOP before `pip`.** Write `Z:\vm\replies\<ts>-STOP-pip.md` asking: "May `pip` download the bridge's packages on the VM — the four base packages, and the `dev`/`report` extras (pytest, matplotlib) or not (bridge NEEDS AMEAR 11)?" Write `FINISHED`. Wait for a Code reply that quotes Amear's answer. If he says no, Code's reply quotes that; no `cli-setup.md` is written, and step 4 does not start (its gate needs it).
144c147
< **Reply for step 3:** `Z:\vm\replies\<ts>-install.md` (3.1–3.4 outputs), then `<ts>-STOP-pip.md`.
---
> **Reply for step 3:** `Z:\vm\replies\<ts>-install.md` (3.1–3.4 outputs, and 3.5's `python --version`), then `<ts>-STOP-pip.md`.
148c151
< **Gate:** start only after all of these exist: (a) your `<ts>-cli-setup.md` reply; (b) `Z:\vm\replies\<ts>-CODE-go-2a.md`, which also names who sets the Strategy Analyzer tab by hand (4.3), as Amear decides it. Code writes (b) only once Amear's answer on whether the 2a NT8 run is covered is on the ledger. His words: "covers what tests 2a/2b need (bridge install + its import)". Settlement 6 leaves "whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6)" in his words, "neither narrowed nor extended" (DECISIONS.md:1089). Write `STARTED` first.
---
> **Gate:** start only after all of these exist: (a) your `<ts>-cli-setup.md` reply; (b) `Z:\vm\replies\<ts>-CODE-go-2a.md`, which also names who sets the Strategy Analyzer tab by hand and who reads the tab and the PRAXIS commission template back (4.3), and which strategy copy is meant (bridge NEEDS AMEAR 7, `report:231`), as Amear decides it; (c) Amear's step-0 words name the sim account (section 2, item 5). Code writes (b) only once Amear's answer on whether the 2a NT8 run is covered is on the ledger. His words: "covers what tests 2a/2b need (bridge install + its import)". Settlement 6 leaves "whether that reaches the 2a NT8 run on the VM (D-2026-11-06-A NEEDS AMEAR 6)" in his words, "neither narrowed nor extended" (DECISIONS.md:1089). Write `STARTED` first.
166c169
< - If the NT8 copy differs, STOP. Paste both outputs and reply. Do not copy, edit or recompile the strategy. Which copy is meant is Amear's question (bridge NEEDS AMEAR 7, `report:231`).
---
> - If either copy differs, STOP. Paste both outputs and reply. Do not copy, edit or recompile the strategy. Which copy is meant is Amear's question (bridge NEEDS AMEAR 7, `report:231`); step 4 runs only on the copy go-2a names as his.
169c172
< **4.3 The hand-set Strategy Analyzer tab.** `backtest` "presses Run on a Strategy Analyzer tab already open and set up by hand" (`report:28`). It needs an open Strategy Analyzer window (`report:59`). It never sets the backtest type (`report:64`). And "No explicit bridge field sets 1-minute Standard fill resolution, 2 ticks/side slippage or the PRAXIS commission template" (`report:89`). Correction 1, C1-2 (`report:2866`): the tab can be set by hand (route a); routes b–d are UNVERIFIED. Who sets the tab by hand (Amear, or you if you can drive the GUI) is not decided here. Whether a hand-set tab counts for "drives the baseline from the terminal" is Amear's question (bridge NEEDS AMEAR 10, `report:234`).
---
> **4.3 The hand-set Strategy Analyzer tab.** `backtest` "presses Run on a Strategy Analyzer tab already open and set up by hand" (`report:28`). It needs an open Strategy Analyzer window (`report:59`). It never sets the backtest type (`report:64`). And "No explicit bridge field sets 1-minute Standard fill resolution, 2 ticks/side slippage or the PRAXIS commission template" (`report:89`). Correction 1, C1-2 (`report:2866`): the tab can be set by hand (route a); routes b–d are UNVERIFIED. Who sets the tab by hand — Amear, or you driving NT8's window — is not decided here. Whether you may drive NT8's window is asked only for the compile (section 2, item 6), and an answer there does not reach this tab: Code's go-2a reply names who sets it, and who reads it and the template back, as Amear decides. Whether a hand-set tab counts for "drives the baseline from the terminal" is Amear's question (bridge NEEDS AMEAR 10, `report:234`).
171c174
< Every setting, from Amear's C4 line (`docs/reports/2026-10-31-voice-session-notes-2.md:111`, REPORTED BY amear: "Settings, same as the 10-31 run: NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · Break at EOD ✓ · Include commission ✓ PRAXIS · Max bars look back 256 · Bars required 20 · Standard (Fastest) · Fill limit on touch ☐ · Slippage 2 · Entries per direction 1 · All entries · Exit on session close ✓ · Set order quantity Strategy · DAY · BandOrVWAP · Contracts 1."):
---
> Where each row comes from: row 1 (Strategy) from `report:93` (strategy `PraxisNoiseAreaBreakout`); row 2 (Backtest type) from `report:114`; rows 3–21, all 19, from Amear's C4 line (`docs/reports/2026-10-31-voice-session-notes-2.md:111`, REPORTED BY amear: "Settings, same as the 10-31 run: NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · Break at EOD ✓ · Include commission ✓ PRAXIS · Max bars look back 256 · Bars required 20 · Standard (Fastest) · Fill limit on touch ☐ · Slippage 2 · Entries per direction 1 · All entries · Exit on session close ✓ · Set order quantity Strategy · DAY · BandOrVWAP · Contracts 1."):
175c178
< | 1 | Strategy | `PraxisNoiseAreaBreakout` |
---
> | 1 | Strategy | `PraxisNoiseAreaBreakout` (`report:93`) |
197c200
< **Commission — the run's own, not the amended one.** The PRAXIS template held Minimum 0.00 / Per unit 1.48 on a Future row and a `NQCONTROW SEP25` row (`docs/reports/2026-10-31-voice-session-notes-2.md:104–106`, REPORTED BY amear). The reference CSV shows $2.96 on every trade: `commission/trade={'2.96': 1190}` (`docs/reports/2026-11-01-csv-analyses.md:51`). Use that. The amended MFFU $4.68 is NOT used for this reproduction (D-2026-11-06-B, S6 cross-block, DECISIONS.md:1104: "An exact-match reproduction (item 4) therefore needs the commission used then, not the amended $4.68"). Read the PRAXIS template (Tools → Commissions → PRAXIS, the path Amear used, `docs/reports/2026-10-31-voice-session-notes-2.md:99`) without changing it, and report the rows. If it does not show 1.48 per unit on those rows, STOP and reply.
---
> **Commission — the run's own, not the amended one.** The PRAXIS template held Minimum 0.00 / Per unit 1.48 on a Future row and a `NQCONTROW SEP25` row (`docs/reports/2026-10-31-voice-session-notes-2.md:104–106`, REPORTED BY amear). The reference CSV shows $2.96 on every trade: `commission/trade={'2.96': 1190}` (`docs/reports/2026-11-01-csv-analyses.md:51`). Use that. The amended MFFU $4.68 is NOT used for this reproduction (D-2026-11-06-B, S6 cross-block, DECISIONS.md:1104: "An exact-match reproduction (item 4) therefore needs the commission used then, not the amended $4.68"). Whoever Code's go-2a reply names reads the PRAXIS template (Tools → Commissions → PRAXIS, the path Amear used, `docs/reports/2026-10-31-voice-session-notes-2.md:99`) without changing it; you report the rows. If it does not show 1.48 per unit on those rows, STOP and reply.
199c202
< Once the tab is set, read every row of the table back from the screen and record what it shows. Any row that differs from the table: STOP and reply; do not run.
---
> Once the tab is set, whoever go-2a names reads every row of the table back from the screen; you record what is read, and by whom. Any row that differs from the table: STOP and reply; do not run.
207c210
< **4.5 Run — the only two bridge commands permitted.** From `C:\praxis\bridge-src`, venv active:
---
> **4.5 Run — the only two bridge commands permitted.** From `C:\praxis\bridge-src`, venv active (if `Activate.ps1` was blocked, type `.venv\Scripts\python -m nt8bridge` in place of `python -m nt8bridge`, limit 9):
218a222
> - This PASS is the numbers check only. Amear's test reads "drives the baseline from the terminal" (DECISIONS.md:1003). Whether a run on a hand-set tab meets that is his (bridge NEEDS AMEAR 10, `report:234`). Test 2a is not judged passed until his word on it is on the ledger.
256c260
< 14. `<ts>-CODE-go-2a.md` — Code; after Amear's word on the 2a run and on who sets the tab
---
> 14. `<ts>-CODE-go-2a.md` — Code; after Amear's word on the 2a run, on who sets and reads back the tab, and on the strategy copy
270c274
< | 2 | Is the install an "import"; order; whose hand | Settled by ruling 1 ("the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot") and settlement 6. |
---
> | 2 | Is the install an "import"; order; whose hand | Install via terminal and the order are settled by ruling 1 ("the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot") and settlement 6; the one in-NT8 compile step is **Amear's** (step 0 item 6). Step 3.3 waits on it. |
275,276c279,280
< | 7 | Which strategy copy / hash | **Amear's.** Step 4.2 gathers the hashes; it does not choose the copy. |
< | 8 | Which account the tests use | **Amear's.** Sim101 or the sim account he names; asked at step 0 (item 5). |
---
> | 7 | Which strategy copy / hash | **Amear's.** Step 4.2 gathers the hashes; it does not choose the copy. Step 4 waits on his word on it (go-2a). |
> | 8 | Which account the tests use | **Amear's.** Sim101 or the sim account he names; asked at step 0 (item 5). Steps 3 and 4 wait on it (limit 1). |
278c282
< | 10 | Does a hand-set tab count for "drives the baseline from the terminal" | **Amear's.** Correction 1 C1-2 (`report:2866`) changes the premise; it answers nothing. Who sets the tab by hand is also his; step 4 waits on it. |
---
> | 10 | Does a hand-set tab count for "drives the baseline from the terminal" | **Amear's.** Correction 1 C1-2 (`report:2866`) changes the premise; it answers nothing. Who sets the tab by hand is also his; step 4 waits on it. The 2a verdict waits on his word on this row (4.6). |
284c288
< - Whether 2a/2b have passed. Code and praxis-auditor judge that (settlement 8). Recording the lift is "under my ruling" — his.
---
> - Whether 2a/2b have passed. Code and praxis-auditor judge that (settlement 8), and 2a only after Amear's word on row 10. Recording the lift is "under my ruling" — his.
rc=1
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/bt.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md; echo rc=$?
13c13
< Start only if `Z:\vm\replies\` holds your `<ts>-cli-setup.md` reply and a `<ts>-CODE-go-2a.md` reply that names who sets the Strategy Analyzer tab. Otherwise stop. If this skill and the handoff's step 4 disagree, STOP and reply; do not choose.
---
> Start only if `Z:\vm\replies\` holds your `<ts>-cli-setup.md` reply and a `<ts>-CODE-go-2a.md` reply that names who sets the Strategy Analyzer tab and who reads the tab and the PRAXIS template back, and which strategy copy is meant, and Amear's step-0 words name the sim account (handoff section 2, item 5). Otherwise stop. If this skill and the handoff's step 4 disagree, STOP and reply; do not choose.
16,17c16,17
< - Sim101 or the sim account Amear names. No live account. No orders.
< - No connection changes (D-071): no connect, reconnect or disconnect.
---
> - Sim101 or the sim account Amear names. No live account. No orders. Nothing here runs until his words name the account (item 5).
> - No connection changes (D-071): no connect, reconnect or disconnect. Do not start, close or restart NinjaTrader; if it is not running, STOP and reply.
29,31c29,31
<    - NT8 copy differs or is missing → STOP and reply.
< 2. Read the PRAXIS commission template without changing it. It must show Per unit 1.48 (the run's own $2.96 per trade, not the amended $4.68). Otherwise STOP and reply.
< 3. Read back every one of the 21 settings in the handoff's step 4.3 table from the open Strategy Analyzer tab. Any mismatch → STOP and reply; do not run.
---
>    - Either copy differs → STOP and reply. NT8 copy missing → search `"$D\NinjaTrader 8\bin\Custom"` for it, report every path found, and STOP.
> 2. The person go-2a names reads the PRAXIS commission template without changing it. It must show Per unit 1.48 on the Future row and the `NQCONTROW SEP25` row (the run's own $2.96 per trade, not the amended $4.68). Otherwise STOP and reply.
> 3. The person go-2a names reads back every one of the 21 settings in the handoff's step 4.3 table from the open Strategy Analyzer tab; record what is read, and by whom. Any mismatch → STOP and reply; do not run.
33c33
< 5. From `C:\praxis\bridge-src`, venv active, type:
---
> 5. From `C:\praxis\bridge-src`, venv active (if `Activate.ps1` was blocked, use `.venv\Scripts\python -m nt8bridge` in place of `python -m nt8bridge`), type:
37c37
< 6. PASS only if `metrics.totalTrades` = `1190` AND `metrics.netProfit` = `197327.60` exactly. Any other number, an error or a timeout is FAIL.
---
> 6. PASS only if `metrics.totalTrades` = `1190` AND `metrics.netProfit` = `197327.60` exactly. Any other number, an error or a timeout is FAIL. This is the numbers check only: whether 2a passes also waits on Amear's word on bridge NEEDS AMEAR 10 (handoff 4.6).
rc=1
$ cmp /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/rep.md vm/skills/praxis-vm-reporter/SKILL.md; echo rc=$?
rc=0
$ cmp /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/orig/readme.md vm/replies/README.md; echo rc=$?
rc=0
$ shasum -a 256 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.c1a.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bt.c1a.md
616bff2451fbcb5008132f72a20db73a29b279a601ead9118d22ee5b6e395c9c  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.c1a.md
b56ff2d7d8a7fdb193b99084132d69bc946748496fca2cdb1ff3094a4698ede1  /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bt.c1a.md
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/handoff.c1a.md vm/2026-11-06-vm-handoff.md | /usr/bin/grep -c '^[<>]'
31
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bt.c1a.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md | /usr/bin/grep -c '^[<>]'
12
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/c1-lncheck.tsv
960	Yeah, just do the snapshot.
1003	Order: read the bridge's code read-only
1004	Praxis.build shared
1063	installs cli-nt-bridge via terminal, after a VMware snapshot
1086	working definition
1087	Exact match on 1,190 trades
1089	neither narrowed nor extended
1090	The VM agent reads and reports it; Code records it.
1091	Code + praxis-auditor judge 2a/2b
1092	Code does not run agents while the VM session writes
1104	An exact-match reproduction (item 4) therefore needs the commission used then
1131	D-2026-08-06-A
1142	Phase 3 build specification
$ awk -F'\t' 'NR==FNR{a[$1]=$2;next} (FNR in a){print FNR, (index($0,a[FNR])>0?"HIT":"MISS"), a[FNR]}' /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/c1-lncheck.tsv DECISIONS.md
960 HIT Yeah, just do the snapshot.
1003 HIT Order: read the bridge's code read-only
1004 HIT Praxis.build shared
1063 HIT installs cli-nt-bridge via terminal, after a VMware snapshot
1086 HIT working definition
1087 HIT Exact match on 1,190 trades
1089 HIT neither narrowed nor extended
1090 HIT The VM agent reads and reports it; Code records it.
1091 HIT Code + praxis-auditor judge 2a/2b
1092 HIT Code does not run agents while the VM session writes
1104 HIT An exact-match reproduction (item 4) therefore needs the commission used then
1131 HIT D-2026-08-06-A
1142 HIT Phase 3 build specification
$ /usr/bin/grep -o -E '(DECISIONS\.md:[0-9]+|and :[0-9]+)' vm/2026-11-06-vm-handoff.md | sort | uniq -c
   2 DECISIONS.md:1003
   1 DECISIONS.md:1004
   6 DECISIONS.md:1063
   1 DECISIONS.md:1086
   1 DECISIONS.md:1087
   3 DECISIONS.md:1089
   2 DECISIONS.md:1091
   1 DECISIONS.md:1092
   1 DECISIONS.md:1104
   1 DECISIONS.md:1131
   1 DECISIONS.md:960
   1 and :1142
$ cat /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/quotecheck.py
import re,sys
srcs=sys.argv[2:]
text="".join(open(p,encoding="utf-8").read() for p in srcs)
norm=lambda s:s.replace("**","")
T=norm(text)
for i,l in enumerate(open(sys.argv[1],encoding="utf-8"),1):
    for q in re.findall(r'"([^"]{12,})"',l):
        status="OK " if norm(q) in T else "MISSING"
        print(f"{status} {i}: {q[:110]}")
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/quotecheck.py vm/2026-11-06-vm-handoff.md DECISIONS.md DECISION_LOG.md docs/reports/2026-11-06-cli-nt-bridge-code-read.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge/README.md docs/reports/2026-10-31-voice-session-notes-2.md | awk '{print $1}' | sort | uniq -c
  18 MISSING
  49 OK
$ python3 -I /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/quotecheck.py vm/2026-11-06-vm-handoff.md DECISIONS.md DECISION_LOG.md docs/reports/2026-11-06-cli-nt-bridge-code-read.md /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge/README.md docs/reports/2026-10-31-voice-session-notes-2.md | /usr/bin/grep '^MISSING'
MISSING 14: you should see
MISSING 39: yyyyMMdd'T'HHmmss'Z'
MISSING 67: could not read: NT8 not running
MISSING 73: could not read
MISSING 81: Required reply format
MISSING 109: $D\NinjaTrader 8\bin\Custom\AddOns
MISSING 114: $D\NinjaTrader 8\bin\Custom\AddOns\
MISSING 115: $D\NinjaTrader 8\bin\Custom\AddOns\
MISSING 116: $D\NinjaTrader 8\bin\Custom\AddOns
MISSING 127: Compile by: Amear
MISSING 127: Compile by: VM agent
MISSING 127: Compile: clean
MISSING 132: $D\NinjaTrader 8\NT8Bridge\trigger
MISSING 132: $D\NinjaTrader 8\NT8Bridge\result
MISSING 144: May `pip` download the bridge's packages on the VM — the four base packages, and the `dev`/`report` extras (py
MISSING 165: $D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs
MISSING 170: $D\NinjaTrader 8\bin\Custom
MISSING 274: ; order; whose hand | Install via terminal and the order are settled by ruling 1 (
$ /usr/bin/grep -c -F 'the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot' DECISIONS.md
2
$ git -C /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge rev-parse HEAD
9664d9b255bfa34b120d88a481afe7741a4115e6
$ sed -n 54p /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/bridge-src/cli-nt-bridge/README.md
2. In NinjaTrader, open the NinjaScript Editor and **compile (F5)**. After this one compile the AddOn loads on every NinjaTrader start, and strategy compiles no longer need F5.
$ /usr/bin/grep -c -E '^\*\*[0-9]+\. (MAJOR|MINOR)' docs/reports/2026-11-06-vm-handoff-manager.md
12
$ /usr/bin/grep -n -E '^\*\*[0-9]+\. ' docs/reports/2026-11-06-vm-handoff-manager.md | cut -c1-40
143:**1. MAJOR: the install is not gated
150:**2. MAJOR: a fact contradicts Corre
155:**3. MAJOR (S8): one of Amear's open
161:**4. MINOR: the install also goes ah
166:**5. MINOR: the pip question underst
174:**6. MINOR: the 2a skill is orphaned
176:**7. MINOR: the step 3.2 check comes
178:**8. MINOR: write-scope limits contr
183:**9. MINOR: the format rules don't a
187:**10. MINOR: the pip-approved run ha
189:**11. MINOR: no gate on who sets the
191:**12. MINOR: a safety reason drops i
193:**13. Checks that held (Q4, Q6, Q7):
205:**14. Citation checks that held (Q3,
$ /usr/bin/grep -n -E '^\*\*C[12]-[0-9]' docs/reports/2026-11-06-cli-nt-bridge-code-read.md | cut -c1-48
2864:**C1-1. Line 29, "The bridge lists no NT8 p
2866:**C1-2. Line 29, "plausible only if the tab
2868:**C1-3. Line 32, Summary item 6 is graded "
2927:**C2-1. Line 81: the refusal paths are cite
2929:**C2-2. Lines 3 and 240 count one adversari
2955:**C2-3. Lines 165–167 (Q4, NT8 version): th
2973:**C2-4. Line 5: the two sha256 prefixes are
2975:**C2-5. Lines 135 and 236 (ADV4's MINOR ite
$ /usr/bin/grep -F '[2026-11-06T22:11:54Z]' DECISION_LOG.md | /usr/bin/grep -c -F 'Help > About'
1
$ sed -n 1003p DECISIONS.md | /usr/bin/grep -c -F 'drives the baseline from the terminal'
1
$ sed -n 1063p DECISIONS.md | /usr/bin/grep -c -F 'VM agent reads and reports the NT8 version'
1
$ /usr/bin/grep -c -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/s13.txt vm/2026-11-06-vm-handoff.md
1
$ /usr/bin/grep -c -F -f /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/s13.txt docs/reports/2026-11-06-vm-handoff-manager.md
1
$ /usr/bin/grep -c -i medic vm/2026-11-06-vm-handoff.md vm/skills/praxis-nt8-bridge-backtest/SKILL.md vm/skills/praxis-vm-reporter/SKILL.md vm/replies/README.md
vm/2026-11-06-vm-handoff.md:0
vm/skills/praxis-nt8-bridge-backtest/SKILL.md:0
vm/skills/praxis-vm-reporter/SKILL.md:0
vm/replies/README.md:0
$ git diff --numstat MANIFEST.md
5	0	MANIFEST.md
$ git status --porcelain --untracked-files=all vm/ docs/reports/2026-11-06-vm-handoff-manager.md
?? docs/reports/2026-11-06-vm-handoff-manager.md
?? vm/2026-11-06-vm-handoff.md
?? vm/replies/README.md
?? vm/skills/praxis-nt8-bridge-backtest/SKILL.md
?? vm/skills/praxis-vm-reporter/SKILL.md
$ git diff --cached --stat | tail -1
 12 files changed, 5726 insertions(+), 2 deletions(-)
$ /usr/bin/grep -c -F 'Connections list' vm/2026-11-06-vm-handoff.md
0
$ for p in '1. **Account:**' '3. **No connection changes' '  6. who performs' 'Step 3 does not start until items 1–6' '6. NT8 version from' '8. Your Documents' '**Gate:** start only when all' '**3.3 Compile in NT8' '**Gate:** start only after all' 'Who sets the tab by hand —' 'Where each row comes from' '- This PASS is the numbers check' '| 2 | Is the install' '| 7 | Which strategy' '| 8 | Which account' '| 10 | Does a hand-set' '- Whether 2a/2b have passed'; do printf '%s => ' "$p"; /usr/bin/grep -n -F -- "$p" vm/2026-11-06-vm-handoff.md | cut -d: -f1 | tr '\n' ' '; echo; done
1. **Account:** => 25 
3. **No connection changes => 27 
  6. who performs => 53 
Step 3 does not start until items 1–6 => 54 
6. NT8 version from => 67 
8. Your Documents => 69 
**Gate:** start only when all => 89 
**3.3 Compile in NT8 => 122 
**Gate:** start only after all => 151 
Who sets the tab by hand — => 172 
Where each row comes from => 174 
- This PASS is the numbers check => 222 
| 2 | Is the install => 274 
| 7 | Which strategy => 279 
| 8 | Which account => 280 
| 10 | Does a hand-set => 282 
- Whether 2a/2b have passed => 288 
~~~~

Block 2, the first pass's two quote mismatches, recovered:

~~~~
$ sed -n 144p /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/subagents/agent-a15bfc5cde09918e4.jsonl | /usr/bin/grep -o -E '"timestamp":"[^"]*"'
"timestamp":"2026-11-06T22:19:41.757Z"
$ sed -n 144p /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/subagents/agent-a15bfc5cde09918e4.jsonl | /usr/bin/grep -o -E 'MISSING (8|99): [^\\]*'
MISSING 8: Praxis.build shared … mapped as Z:
MISSING 99: a one-file deploy should therefore fail to compile
$ sed -n 156p /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/subagents/agent-a15bfc5cde09918e4.jsonl | /usr/bin/grep -o -E '"timestamp":"[^"]*"'
"timestamp":"2026-11-06T22:19:55.681Z"
$ sed -n 156p /Users/admin/.claude/projects/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/subagents/agent-a15bfc5cde09918e4.jsonl | /usr/bin/grep -o -E 'MISSING (8|99): [^\\]*' | wc -l
       0
$ /usr/bin/grep -c -F 'A one-file deploy should therefore fail to compile' docs/reports/2026-11-06-cli-nt-bridge-code-read.md
1
$ /usr/bin/grep -c -F 'a one-file deploy should therefore fail to compile' docs/reports/2026-11-06-cli-nt-bridge-code-read.md
0
~~~~

Reading the evidence:
- Before: the handoff `92e71e08…` (284 lines), the 2a skill `cf244560…`, the reporter skill `6dd6b25d…` and the README `eac55350…`.
- After: the handoff `9c9fa56e…` (288 lines) and the 2a skill `e06c40c4…`.
- The reporter skill and the README are byte-identical (`cmp` rc=0). Neither repeats a changed step: the reporter skill has no compile or Connections text.
- The 4.3 table rows 2–21 are not in the diff. Row 1 gains only the `(report:93)` cite, so the values are unchanged; the adversary also counted 0 mismatches.
- `Connections list` is 0, so item 8 is gone.
- The protected-title proxy count (`medic`) is 0 in all four files.
- MANIFEST.md is unchanged by this correction: still `5 0`, the first pass's five rows.
- The S13 count for this report (1) was taken **before** this section was appended. This section quotes the sentence nowhere, and the grep reads its pattern from a file, so the command text does not match itself.

### Adversarial findings

#### Full return of worker `a19e9d3fb95731faf` (ADVERSARIAL, read-only, over `616bff24…`), pasted unedited

The harness's two-space indent and its trailing `agentId`/`usage` lines are removed. Nothing else is changed.

~~~~
Adversarial read-only attack on the VM handoff file set. I wrote no files.

**Hash (artifact under attack):**
```
616bff2451fbcb5008132f72a20db73a29b279a601ead9118d22ee5b6e395c9c  vm/2026-11-06-vm-handoff.md
b56ff2d7d8a7fdb193b99084132d69bc946748496fca2cdb1ff3094a4698ede1  vm/skills/praxis-nt8-bridge-backtest/SKILL.md
6dd6b25db78d8d06bc596c5ae9df85c6d7ce0815472d138eecbb33fb517128b0  vm/skills/praxis-vm-reporter/SKILL.md
eac55350b2fb1ce49f6d6516a5db3e6fc98098197bbebc8de055395315f141de  vm/replies/README.md
```
The handoff's hash is not the `149600606f16…` the brief names. I can't check that it is a "later" edit, so I attacked the file as it is now (`?? vm/`, untracked).

## Findings

1. **MAJOR (S8): the gates require Amear to answer, not to say yes.** At handoff:54 and :89, items 3, 4 and 5 have no branch for a "no" or an unclear answer.
   - :54 reads "Step 3 does not start until items 1–6 are answered in your words." Gate (c) at :89 reads "Amear's words answer section 2 items 2–6 … If any fails, do not start."
   - Items 2 and 6 do have branches: :101 "Run it only if Amear's step-0 words chose it" and :125 "If his words do not clearly name one of the two: STOP".
   - Items 3 (file set), 4 (whether the unauthenticated folders are acceptable) and 5 (account) have no such rule. A "No, not acceptable" on item 4 still counts as an answer. The install would then go ahead and create the folders (step 3.4) against his word. A grep for `not acceptable|declin|says no` found no branch.

2. **MAJOR (S8): the 2a PASS criterion quietly settles NEEDS AMEAR 10.** See handoff:221, skill-2a:37, and handoff:287.
   - Amear's test reads "cli-nt-bridge (MIT) **drives the baseline from the terminal** and reproduces 1,190 trades" (DECISIONS.md:1003).
   - 4.6 reads "PASS = `metrics.totalTrades` is exactly `1190` AND `metrics.netProfit` is exactly `197327.60`". That drops the "from the terminal" condition.
   - Section 8 row 10 (:281) calls a hand-set tab counting **Amear's** question. But gate (b) at :151 only waits on who sets and reads the tab and on whether the 2a run is covered. Nothing waits on NEEDS AMEAR 10 (report:234), not the run and not the judgement.
   - :287 gives "Whether 2a/2b have passed" to Code and the auditor with no carve-out. If they rule PASS on the numbers alone, NEEDS AMEAR 10 is answered for him.

3. **MAJOR (S8 and D-071): starting NT8 is covered by nothing.**
   - Step 1 item 6 (:67, Help → About) comes before item 7 (:68, "Is NT8 running?").
   - Steps 3.3 (VM agent path) and 4 need NT8 running. No step says who starts NT8 or what to do if it is closed.
   - Grepping for `launch|start nt|not running|log in` returns only :28, :30, :68, :102 and :134. None of them is a launch rule.
   - The report says the VM "holds the Rithmic connection" (report:228). Starting NT8 may bring connections up, which would breach "no new data connection" (DECISIONS.md:1063). Whether it auto-connects on this VM is UNVERIFIED. This is a GUI and connection action with no ruling and no wait. Step 1's "could not read" fallback (:73) covers only step 1.

4. **MINOR: the list of superseded lines is incomplete (handoff:12).** It reads "Corrections 1–2 … supersede lines 29, 32, 81 and 165–167". The report's own headings also correct other lines:
   ```
   C2-2. Lines 3 and 240 …   C2-4. Line 5 …   C2-5. Lines 135 and 236 …
   ```
   Line 236 is NEEDS AMEAR 12, which section 8 row 12 maps.

5. **MINOR: limit 1 calls steps 1 and 2 read-only, but they write (handoff:25 and :34).** :25 says "steps 1 and 2, which are read-only". Step 2.1 (:77) copies a SKILL.md into the skills directory, which is off the share.
   - Limit 10's list of off-share writes (:34) leaves out the skill copies in steps 2 and 4.
   - It also leaves out the compile output, and the NT8Bridge folders the AddOn creates when it loads in step 3. :34 credits those folders only to "the two bridge commands of step 4".
   - Both points are still sound on accounts: neither step touches one.

6. **MINOR: the account answer is gated but never used.** Item 5 is gated at :89(c), :151(c) and skill-2a:13. No step uses the account: there is no account row in the 21-row table and no account in 4.4 or 4.5. The gate is formal only.

7. **MINOR: the 2a skill and handoff step 4 drift apart.**
   - skill:29 says "NT8 copy differs or is missing → STOP". Handoff :170 says to search `bin\Custom`, report every path, then STOP.
   - skill:30 checks only "Per unit 1.48". Handoff :200 also requires Minimum 0.00 on the Future row and the `NQCONTROW SEP25` row.
   - skill:40 fixes "`RESULT: DONE`" even when its own step 6 says FAIL. Handoff 4.6 has no `2a-NUMBERS:` line.
   - Neither file handles a Z: copy whose hash differs from the Mac hash.
   - Because handoff :153 says "If the skill and this step disagree, STOP", these gaps could cause spurious STOPs.

8. **MINOR (attribution): the master's settlement text is cited as authority (handoff:67).** It reads "Settlement 7 covers this one read … 'The VM agent reads and reports it; Code records it.'" That quote is column 3 (DECISIONS.md:1090), which is the master's text. Amear's column-2 words, "VM agent reads and reports the NT8 version", do cover the read. Neither names Help → About; that route is the master's (22:11:54Z row: "record NT8 version via Help > About"). :82 and :224 lean on settlement 8's column 3 the same way.

9. **MINOR (provenance): Amear's words reach Code only through the VM agent.**
   - :47 reads "The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours".
   - `SNAPSHOT: confirmed` (:89(b)) rests on that relayed text.
   - Gate (c) is judged by the VM agent itself, not by Code.

10. **MINOR: two outputs and one path have no home.**
    - Step 3.5's `python --version` output has no named reply file. :147 lists only install.md for 3.1–3.4, then STOP-pip.
    - If Amear refuses `pip`, section 7 has no file and no stop for that path.

11. **MINOR: the venv instructions conflict.** :210 and skill:33 say "venv active, type `python -m nt8bridge …`". Limit 9 (:33) uses the fallback `.venv\Scripts\python -m nt8bridge …` when `Activate.ps1` is blocked. The exact text to type conflicts.

12. **MINOR: section 8 row 7 contradicts step 4.2.** Row 7 (:278) says step 4.2 "does not choose the copy". But 4.2 goes ahead whenever the NT8 copy's hash matches the repo's. That treats the repo copy as the reference.

## Checks that held

- **S8, snapshot:** Amear's hand step. Code writes `SNAPSHOT: confirmed` only from his words (:250). "the VM cannot snapshot itself" is labelled as the master's reading, and that phrase is in the 22:11:54Z row.
- **S8, source route:** the HTTPS clone is labelled the master's proposal and is conditional on his choice (:101). Confirmed in the 22:11:54Z row.
- **S8, pip:** a hard STOP before `pip` (:144), then a Code reply that must quote Amear (:145).
- **S8, compile (F5):**
  - Neither path is assumed.
  - The bridge's `compile` is excluded (:28, :122).
  - An unclear answer leads to STOP (:125).
  - Compile errors are copied and lead to STOP, with no `.cs` edits (:126).
  - The VM agent's permission covers "this one compile only" (:124).
- **S8, Strategy Analyzer tab, Commissions read and backtest run:** these wait on go-2a "as Amear decides" (:151, :172, :200, :202). The 2a NT8 run waits on NEEDS AMEAR 6, quoted correctly against DECISIONS.md:1089.
- **S8, NT8 version read:** covered by Amear's ruling-5 words, "VM agent reads and reports the NT8 version" (DECISIONS.md:1063).
- **Gates line up:**
  - step 0 items 1–6 map to gates (b) and (c) at :89, to 3.3 for item 6, and to step 4 gate (c) for item 5;
  - the 17-file list in section 7 matches the steps;
  - the 2a skill's gate matches the handoff's :151;
  - step 1's items 1–9 are numbered consistently, and item 9 points to "the six items of section 2".
- **Account exception (limit 1):** steps 1 and 2 touch no account (folder listing, Get-Process, About). Steps 3 and 4 do wait (:89(c), :151(c)).
- **Citations checked and found matching:**
  - DECISIONS.md:960, :1003, :1004, :1063 (rulings 1 and 5, and the hard-limits sentence quoted verbatim), :1086, :1087, :1089, :1090, :1091, :1092, :1104, :1131, :1142;
  - DECISION_LOG 22:11:54Z (HTTPS proposal, "the VM cannot snapshot itself") and 2026-08-06T20:18:56Z (WHO: amear, at line 167);
  - report:28, 31, 40, 41, 42, 47, 52, 59, 63, 64, 65, 66, 67, 68, 89, 93, 113, 114, 127, 128, 140, 141, 142, 143, 145, 146, 152/159, 173, 178, 184, 188, 2866, 2868, 2959, 2960, 2962, 2965–2968, 2973;
  - NEEDS AMEAR numbers 1, 3, 5, 7, 8, 10 and 11 at report:225, 227, 229, 231, 232, 234 and 235 are all correct;
  - README.md@9664d9b lines 35, 41, 43–45, 48, 52, 54, 174 and 182 match. The clone's `rev-parse HEAD` is `9664d9b255bfa34b120d88a481afe7741a4115e6`;
  - pyproject.toml:14–15 are `dev = ["pytest>=7"]` and `report = ["matplotlib>=3"]`;
  - `RunPlaybackRun` is defined only in the Playback file, at :2489;
  - the config keys exist in `config/config.json`;
  - `backtest` accepts `--config` and `--timeout` (cli.py:1181 and :1187);
  - notes-2:99, :104–106 and :111; three-strategy-results:73, :86 and :108; csv-analyses:51 (`{'2.96': 1190}`).
- **Step 4.3 table:**
  - row 1 matches report:93 (`PraxisNoiseAreaBreakout`);
  - row 2 matches report:114 ("Backtest type: Backtest");
  - rows 3–21 are 19 values, in the same order as notes-2:111;
  - **value mismatches: 0.**
- **Strategy hash:** `35393823e9bc…2752265` is the hash of the working-tree file, and the file is unmodified (last commit `719ab11`).
- **De-identification (counts only):** `medic` 0 in all four files. I took the words of the source's breaker #5 lines that do not appear in DECISIONS.md or SPEC_RUBRIC (23 words) and searched the four files for them: 0 hits in each. Limitation: this check assumes the title sits on a line that names 5.
- **S13:** the full sentence matches 1 line in the handoff. `Fills are optimistic` occurs once.
- **S2:** :14 "Nothing in this file has been tried"; Z: as repo root is marked INFERRED (:8); the menu path is marked unchecked (:45); `ntVersion` equal to About is UNVERIFIED (:215); `CumProfit` net of commission is UNVERIFIED (:218). I found no claim of anything tried, observed or settled beyond its evidence, apart from findings 2, 8 and 12.

VERDICT: FAIL
~~~~

#### Disposition (final handoff lines; `c1fix3.py`; not re-attacked)

| # | Sev | Disposition |
|---|---|---|
| 1 | MAJOR | **Fixed.** Step 3 gate (c) (:89) now needs answers that let the steps run as written: item 3 accepts the two files, item 4 accepts the folders, item 5 names an account. "A no, a different file set, a condition, or anything unclear is not a yes: STOP, quote his words in a reply, and wait. Do not adapt the steps." |
| 2 | MAJOR | **Fixed.** 4.6 (:222): "This PASS is the numbers check only." It quotes his "drives the baseline from the terminal" (DECISIONS.md:1003, count 1 above) and says 2a "is not judged passed until his word on it is on the ledger". Section 8 row 10 (:282) and the "Whether 2a/2b have passed" bullet (:288) carry the same wait. 2a skill step 6 matches. |
| 3 | MAJOR | **Fixed.** Limit 3 (:27): "**Do not start, close or restart NinjaTrader.** … If a step needs NT8 running and it is not, STOP and reply. Starting it is Amear's." Step 1 item 6 (:67): "If NT8 is not running, do not start it (limit 3)". The 2a skill's limits match. |
| 4 | MINOR | **Fixed.** :12 lists lines 3, 5, 29, 32, 81, 135, 165–167, 236 and 240, matching the eight C1/C2 headings pasted above. |
| 5 | MINOR | **Fixed.** Limit 1 drops "read-only", keeping only "which touch no account". Limit 10 (:34) adds the two SKILL.md copies, and says NT8's compile output and the AddOn-created `NT8Bridge` folders are NT8's own writes. |
| 6 | MINOR | **Not changed.** The account gate is what the audit's MINOR 1 asked for. No step trades, so no step uses the account; the wait is kept on purpose. |
| 7 | MINOR | **Partly fixed.** In the 2a skill, step 1 now covers either copy differing and the missing-file search; step 2 names the Future and `NQCONTROW SEP25` rows. Handoff 4.2 says "either copy differs". **Not changed:** the skill's `RESULT: DONE` and `2a-NUMBERS:` line. The extra line adds to the handoff rather than contradicting it. `RESULT: DONE` with a numbers FAIL is a residual ambiguity for the auditor. |
| 8 | MINOR | **Fixed for :67.** It now quotes Amear's ruling-5 words, "VM agent reads and reports the NT8 version" (DECISIONS.md:1063, count 1 above), and labels Help → About as the master's route (DECISION_LOG `2026-11-06T22:11:54Z`, count 1 above). **Not changed:** :82 and :224. Settlement 8's text echoes Amear's own ruling-5 words, which the header quotes at line 19 ("Code + auditor judge 2a/2b and log the lift under my ruling"). |
| 9 | MINOR | **Not changed.** By design, Amear's words reach Code through the VM agent's word-for-word paste (settlement 9: handover goes through the handoff file). This is a residual provenance limit; Amear can confirm on the ledger. |
| 10 | MINOR | **Fixed.** 3.5 adds: if he says no, Code's reply quotes that, no `cli-setup.md` is written, and step 4 does not start. "Reply for step 3" now includes 3.5's `python --version`. |
| 11 | MINOR | **Fixed.** 4.5 and 2a skill step 5 give the `.venv\Scripts\python -m nt8bridge` form for when `Activate.ps1` was blocked (limit 9). |
| 12 | MINOR | **Fixed.** The step 4 gate (b) (:151) now needs go-2a to name which strategy copy is meant (NEEDS AMEAR 7, `report:231`). 4.2 runs "only on the copy go-2a names as his". Section 8 row 7 (:279), section 7 item 14 and the 2a skill gate match. |

No finding was BLOCKING. The 3 MAJOR and 7 MINOR fixes (two of them partial) were made after the attack. **The fixed text (`9c9fa56e…`, 31 changed diff lines; 2a skill `e06c40c4…`, 12) was not re-attacked by anyone.**

What the adversary confirmed held, on the audit's own findings:
- The compile path: neither path is assumed, the bridge `compile` is excluded, an unclear answer means STOP, and the permission covers "this one compile only".
- The step 0 → gate → section 8 mapping.
- The account exception.
- Step 1 renumbered 1–9, with item 9 → "the six items of section 2".
- The 4.3 attribution: row 1 from report:93, row 2 from report:114, rows 3–21 from notes-2:111 (19 rows, 0 value mismatches).
- All cited DECISIONS, DECISION_LOG, report and README lines.
- De-identification 0.
- S13: 1.

### Negative test (stress-test step 5)

Not applicable as a trip test: this unit has no hook or gate to trip. The handoff's gates are text instructions to an agent that has not run them, so whether they hold is untested (S2).

### S6 cross-block check

- F1–F4: untouched. No code, template, hook, config or strategy file was edited.
- D-2026-11-06-C ($4.68) vs 2a: unchanged. The 2a commission text (1.48 per unit, $2.96 per trade) is not in the diff except that the skill now names its rows.
- D-071 and the in-VM ban: no limit was lifted. This correction only adds waits: compile hand, account, NT8 start, strategy copy, and NEEDS AMEAR 10 on the 2a verdict.
- Nothing was sent toward the VM, Z:, SMB or NT8. Nothing was run from the bridge clone (`git rev-parse` and `sed -n` only).
- MANIFEST.md, DECISIONS.md, the ledgers, STATUS, HANDOFF, specs, scripts and `.claude/` were not touched. Agent memory was not written.

### Files staged (Correction 1)

None. The four `vm/` files and this report are untracked (porcelain `??` above). The index is unchanged from the unit's start: `git diff --cached --stat | tail -1` printed ` 12 files changed, 5726 insertions(+), 2 deletions(-)` (last line of the evidence block).

Edited in this correction: `vm/2026-11-06-vm-handoff.md`, `vm/skills/praxis-nt8-bridge-backtest/SKILL.md`, and this report (append only). Unchanged: `vm/skills/praxis-vm-reporter/SKILL.md`, `vm/replies/README.md`.

### Result (Correction 1)

**Result (Correction 1): FAIL**

Why FAIL and not PASS:
- Every item the audit named is fixed, with evidence: the BLOCKING S8 compile fix in its five parts, MINORs 1–3, and both S1 re-runs with the corrected count of 12.
- The one adversary allowed then returned `VERDICT: FAIL`, with 3 MAJOR findings against the edited text.
- Those three, and seven of the MINOR ones, are fixed in text, but no independent attack has run on the final `9c9fa56e…`. The stress-test bar, "survives all six", is not met. Grading the post-attack fixes as passed would put them above their evidence (S2).
- What it needs: the auditor's re-attack over handoff `9c9fa56e6760036d11cc5f94fa1bc5c52c02228ff1a77b272204568a7e99233f` and 2a skill `e06c40c4c9dbc99d15988ce5823602d263a4f359d4e6ec1017be920ea84f2b08`.
- This correction added Amear touchpoints: step 0 item 6; waits on starting NT8, the strategy copy and NEEDS AMEAR 10.
