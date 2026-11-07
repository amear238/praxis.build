# VM handoff — 2026-11-06: tests 2b and 2a, cli-nt-bridge install

## 0. Header

- **Written by:** Claude Code on the Mac (praxis-master, through unit `2026-11-06-vm-handoff`, written by praxis-manager).
- **Read by:** the Claude agent running inside the Windows VM — "the VM agent". That is the master's working definition, not an observation (DECISIONS.md:1086, settlement 3). Your first reply confirms or corrects it.
- **Date:** 2026-11-06. **Repo HEAD when written:** `234e4bc`. Amended 2026-11-07 (amendment 1, unit `2026-11-07-vm-handoff-amendment`) at repo HEAD `43b34b1`.
- **Path:** on the Mac, `vm/2026-11-06-vm-handoff.md` in the repo. On the VM, `Z:\vm\2026-11-06-vm-handoff.md`. That Z: is the repo root is INFERRED from Amear's words "Praxis.build shared" and "\\192.168.1.204\Praxis.build mapped as Z:" (DECISIONS.md:1004, item 3; DECISION_LOG `2026-11-06T22:11:54Z`). Amear confirms it when he points you here.
- **Standing limitation:** Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
- **The one rule:** Reply by writing files under `Z:\vm\replies\`; never edit anything else on Z:.
- **Amendment 1 (2026-11-07):** applies D-2026-11-07-A rulings 5, 6, 7(4), 7(5), 7(7), 7(11), 7(12), 8 and 10 (DECISIONS.md:1229–1234); adds section 9 (the master's proposal, not for the VM agent).

`report:` below means `docs/reports/2026-11-06-cli-nt-bridge-code-read.md` (committed in `234e4bc`; on the VM, `Z:\docs\reports\2026-11-06-cli-nt-bridge-code-read.md`). Its Corrections 1–2 (`report:2860–3200`) supersede lines 3, 5, 29, 32, 81, 135, 165–167, 236 and 240. `README.md:N@9664d9b` means line N of the bridge's README at commit `9664d9b`.

**Nothing in this file has been tried.** The install, the skills and both tests are untried. No step here is known to work. Each "you should see" is what the source text predicts, not something anyone has seen.

**Where the authority comes from (quoted):**
- Amear, D-2026-11-06-A item 2 (DECISIONS.md:1003): "Order: read the bridge's code read-only; write an install walkthrough; VMware snapshot first; then install. Direction: the walk-forward runs in NT8 through the bridge, not in a Mac-side Python copy." Tests: "a. cli-nt-bridge (MIT) drives the baseline from the terminal and reproduces 1,190 trades / ~$197,327 net on NQCONTROW. b. The VM agent loads a written skill and follows it correctly on a simple job."
- Amear, D-2026-11-06-B ruling 1 (DECISIONS.md:1063): "the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot."
- Amear's ruling-5 defaults (DECISIONS.md:1063): "test 2a reference = 1,190 trades / $197,327.60 on NQCONTROW SEP25, exact match; my "lift completely once confirmed" ruling covers what tests 2a/2b need (bridge install + its import), D-071 untouched; VM agent reads and reports the NT8 version; Code + auditor judge 2a/2b and log the lift under my ruling; VM agent on Z: while Code runs = second session, coordinate."
- Amear, D-2026-11-07-A rulings 5–8 and 10 (DECISIONS.md:1229–1234; ledger DECISION_LOG `2026-11-07T12:55:00Z`, WHO: amear), quoted where applied: section 1 limits 4, 6, 8; section 2; steps 3.4, 3.5, 4.2, 4.3, 4.6; section 8.

## 1. Hard limits for the VM agent

Every limit holds for the whole of this file. If a step seems to need breaking one, STOP and write a reply saying which limit and why.

1. **Account:** Sim101 only, or the sim account Amear names. No live account, ever. No step runs until item 5 is answered (section 2), except steps 1 and 2, which touch no account: steps 3 and 4 wait on Amear's words naming the account. Which account the tests use is still Amear's question (bridge NEEDS AMEAR 8, `report:232`).
2. **No orders.** Place, change, cancel or flatten nothing.
3. **No connection changes (D-071).** No new NT8 connection, no reconnect, no disconnect. Amear: "D-071 untouched" (DECISIONS.md:1063); "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." (DECISIONS.md:1063). Why it matters here: `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun`, on its baseline stage when `require` is playback, disconnects every non-Playback connection (`report:184`; the D-071 consequence is INFERRED, `report:188`). **Do not start, close or restart NinjaTrader.** Starting it may bring connections up; whether it does on this VM is UNVERIFIED. If a step needs NT8 running and it is not, STOP and reply. Starting it is Amear's.
4. **Bridge commands you must not use.** Amear: "(4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(4)). `flatten` has no Sim-only check (`report:178`). This file's own limit for these steps, not his words: the only bridge commands it permits are `backtest` and `ntstatus` (step 4). Not `doctor`, `deploy`, `compile`, `reload`, `restart`, `watchdog`, `configure`, `satemplate`, `analyzerrun`, or any other.
5. **Do not install** `addon/AutoReconnect.cs` or `addon/ChartDataSeriesSwitcher.cs` (`report:41`, `report:42`; bridge NEEDS AMEAR 1, `report:225`).
6. **No NT8 Guard** (`guard/`). Amear: "(5) NT8 Guard out." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(5)). It adds scheduled tasks, a saved NT8 password, auto-login and auto-kill/relaunch (`report:152–159`; bridge NEEDS AMEAR 5, `report:229`).
7. **Nothing bought.** No licence, subscription, data feed or add-on purchase.
8. **`pip`.** Amear: "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(11)). See step 3.5. Mismatch: the bridge declares version floors, not pins, with no lock file (`report:143`), so "pinned requirements" names no file on this bridge. Step 3.5 keeps a STOP before `pip` until Code names the pinned list, which may name only the four base packages and the clone's own `-e .`, installed with `--no-deps` (INFERRED, not his word). Whether more counts is **Amear's** question, not Code's.
9. **Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it. Do not change PowerShell's execution policy; if `Activate.ps1` is blocked, use the README's fallback, `.venv\Scripts\python -m nt8bridge …` (`README.md:48@9664d9b`).
10. **Write only under `Z:\vm\replies\`** on the share. Never edit, move or delete any other file on Z:. Off the share, write only what a step names: the clone, its venv and `2a-config.json` under `C:\praxis\` (steps 3–4), exactly two files into NT8's `bin\Custom\AddOns` (step 3.2), and the two SKILL.md copies into your skills directory (steps 2 and 4). NT8's own compile output (step 3.3) and the `NT8Bridge` folders the loaded AddOn creates (step 3.4) are NT8's writes, not yours. The two bridge commands of step 4 write their own request and result files under `Documents\NinjaTrader 8\NT8Bridge\` (`report:52`, `report:67`); that is expected.
11. **One-session rule.** While you work on Z:, Code dispatches nothing (DECISIONS.md:1092, settlement 9: "Code does not run agents while the VM session writes; handover goes through the VM handoff file."). Signal it: before your first step, write `Z:\vm\replies\<ts>-STATUS.md` holding the line `STARTED`. When you stop, for any reason, write a new `<ts>-STATUS.md` holding the line `FINISHED`. Code starts no agent between those two files.
12. **De-identification.** Never write the source title of circuit breaker #5 anywhere — not in a reply, not in a file name, not in a commit message, not in a note (D-2026-08-06-A, DECISIONS.md:1131 and :1142; ruling DECISION_LOG `2026-08-06T20:18:56Z`, WHO: amear). If you meet it in a document, do not copy it.
13. **No edits in NT8 beyond the steps.** Do not change a strategy, commission template, instrument, data series or workspace unless a step says so. A setting that differs from the list in step 4 is reported, not fixed.

`<ts>` everywhere means UTC time from PowerShell: `(Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")` — for example `20261107T091500Z`.

## 2. Hand step 0 — Amear, on the Mac

Before the VM agent does anything below, take a VMware Fusion snapshot of the VM. Source: ruling 1, "after a VMware snapshot" (DECISIONS.md:1063); R-VN4-13, "Yeah, just do the snapshot." (DECISIONS.md:960). Whose hand, in your words: "Snapshot is my hand step: confirmed." (DECISIONS.md:1232, D-2026-11-07-A ruling 8).

- [ ] Fusion → select the VM → Snapshots → Take Snapshot. Name: `pre-cli-nt-bridge-2026-11-06`. (Menu path not checked by Code; use Fusion's own snapshot command if it differs.)
- **You should see:** the snapshot listed in the VM's Snapshots window with that name and today's date.
- Then tell the VM session, in your own words, six things. The VM agent pastes what you say, word for word, into its first reply, and Code files it as yours:
  1. the snapshot is taken, and its name;
  2. how the bridge source reaches the VM: the anonymous HTTPS clone in step 3.1 (the master's proposal, DECISION_LOG `2026-11-06T22:11:54Z`), the README's SSH clone, or a copy through Z: (bridge NEEDS AMEAR 11, `report:235`);
  3. whether the install copies only the two AddOn files of step 3.2 (bridge NEEDS AMEAR 1, `report:225`);
  4. whether the unauthenticated request folders the install creates are acceptable for these tests (bridge NEEDS AMEAR 3, `report:227`);
  5. which sim account (bridge NEEDS AMEAR 8, `report:232`);
  6. who performs the one in-NT8 compile (NinjaScript Editor → F5) — Amear by hand, or the VM agent driving NT8's window? The first compile is a step inside NT8, not a terminal command (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"; `report:31`: "Installing means copying C# into `bin\Custom\AddOns` and compiling it in NT8"; `report:140`). Ruling 1 settles the terminal install and its order; it does not say whose hand presses F5.
- Anything you leave out, the VM agent does not assume. Step 3 does not start until items 1–6 are answered in your words.

## 3. Step 1 — VM agent self-report (test 2b, part 1)

Write `Z:\vm\replies\<ts>-STATUS.md` with `STARTED` first.

Report each item below. Observe only: open no settings dialog, click no Connect or Disconnect.

1. Your identity: product name, model and version, as you know them. Say whether you are "the Claude agent running inside the Windows VM" (settlement 3) or something else.
2. How you load skills: the full path of your skills directory, and the file layout you expect there (for example `<dir>\<name>\SKILL.md`). Report your own convention. Do not guess it.
3. `python --version` — paste the output. The bridge needs "Python 3.10+" (`README.md:35@9664d9b`; `report:143`).
4. `$PSVersionTable.PSVersion` — paste the output.
5. `git --version` — paste the output, or the error. Step 3 needs git.
6. NT8 version from NinjaTrader → Help → About (D-2026-11-06-A item 1). Amear's own words cover this one read: "VM agent reads and reports the NT8 version" (ruling 5, DECISIONS.md:1063). The Help → About route is the master's (DECISION_LOG `2026-11-06T22:11:54Z`). It is the only NT8 window step 1 opens. If NT8 is not running, do not start it (limit 3): write "could not read: NT8 not running". Copy the text exactly. The bridge report "observes no value of the VM's NT8 build" (`report:2965`). The repo carries REPORTED values that differ by date: 8.1.7.2 from installer events, 2026-10-19 (`report:2966`); 8.1.8.4 per Amear, 2026-10-31 (`report:2967`); 8.1.8.4 per Claude Code on the VM, 2026-11-02 (`report:2968`). Code has observed none of them.
7. Is NT8 running? `Get-Process NinjaTrader -ErrorAction SilentlyContinue | Select-Object Id,StartTime` — paste the output.
8. Your Documents folder: `[Environment]::GetFolderPath('MyDocuments')` — paste the output. NT8's folders sit under it.
9. Amear's step-0 words (the six items of section 2). Paste them word for word. If you got none, say so.

**Reply:** `Z:\vm\replies\<ts>-self-report.md`, in the format of section 7.
**You should see:** every item answered, or marked "could not read" with the reason.

## 4. Step 2 — load the first skill (test 2b, part 2)

1. Copy `Z:\vm\skills\praxis-vm-reporter\SKILL.md` into your skills directory, following the convention you reported in step 1. Do not guess the convention. If you have no skills directory, or loading needs something you cannot do, STOP and say so in the reply.
2. Load the skill the way you normally would. Say in the reply how you did it.
3. Perform the skill's job exactly as it is written: list NT8's `bin\Custom\AddOns` folder, check whether the `NT8Bridge\trigger` and `NT8Bridge\result` folders exist, and write the reply in the skill's required format.

**Reply:** `Z:\vm\replies\<ts>-2b-skill-job.md`, in the skill's own format (its "Required reply format" section).
**PASS criterion for 2b:** the reply exists, and it matches the skill's required format — every required line present, in order, the outputs pasted, not described. Code and praxis-auditor judge it (settlement 8, DECISIONS.md:1091). You do not grade yourself.
**You should see:** before the install, the `trigger` and `result` folders do not exist (`False`). That is expected.

Then write `<ts>-STATUS.md` with `FINISHED`, and stop. Wait for `Z:\vm\replies\<ts>-CODE-2b-verdict.md`.

## 5. Step 3 — install cli-nt-bridge

**Gate:** start only when all of these hold. (a) `Z:\vm\replies\<ts>-CODE-2b-verdict.md` exists and holds the line `2b: PASS`. (b) The same file holds the line `SNAPSHOT: confirmed` — Code writes it only after reading Amear's step-0 words in your self-report. (c) Amear's words answer section 2 items 2–6 (route, file set, request folders, sim account, who compiles), and the answers let the steps run as written: item 3 accepts the two files of 3.2, item 4 accepts the request folders, item 5 names a sim account. A no, a different file set, a condition, or anything unclear is not a yes: STOP, quote his words in a reply, and wait. Do not adapt the steps. If any fails, do not start. Write `STARTED` first.

What the install is: copy C# into `bin\Custom\AddOns` and compile it in NT8 (`report:31`, `report:140`). Amear's lift covers it: "bridge install + its import" (DECISIONS.md:1089, settlement 6). The commands below are untried.

**3.1 Get the source.** Outside the share, pinned to `9664d9b`:
```
New-Item -ItemType Directory -Force C:\praxis | Out-Null
git clone https://github.com/eman007/cli-nt-bridge C:\praxis\bridge-src
git -C C:\praxis\bridge-src checkout 9664d9b
git -C C:\praxis\bridge-src rev-parse HEAD
```
- **You should see:** `9664d9b255bfa34b120d88a481afe7741a4115e6` from the last line (the pinned commit, `report:2973`).
- The README clones over SSH (`README.md:41@9664d9b`: `git clone git@github.com:eman007/cli-nt-bridge.git`), which "needs a GitHub key" (`report:142`). The block above is the anonymous HTTPS clone the master proposed (DECISION_LOG `2026-11-06T22:11:54Z`). Run it only if Amear's step-0 words chose it. If he chose another route, follow his words and paste what you typed. How the source reaches the VM is his (bridge NEEDS AMEAR 11, `report:235`).
- If `git` is missing or the clone asks for a login: STOP, reply.
- **Reply line:** paste all four commands' output.

**3.2 Copy exactly two files.** The AddOn is one class split across two files (`report:40`). The README deploys only one (`README.md:52@9664d9b`: `python -m nt8bridge deploy --strategy addon/NT8BridgeServer.cs --kind addon`). `NT8BridgeServer.cs` calls `RunPlaybackRun`, which is defined only in `NT8BridgeServerPlayback.cs`, so "A one-file deploy should therefore fail to compile" (`report:141`, INFERRED, not tried). Copy by hand; do not use `deploy`:
First list the folder:
```
$D = [Environment]::GetFolderPath('MyDocuments')
Get-ChildItem "$D\NinjaTrader 8\bin\Custom\AddOns" | Select-Object Name,Length,LastWriteTime
```
- If a file of either name is already there, STOP now, before copying, and reply (`deploy` would replace a same-named file "without asking", `report:146`; you must not).
Only then copy, and list again:
```
Copy-Item C:\praxis\bridge-src\addon\NT8BridgeServer.cs "$D\NinjaTrader 8\bin\Custom\AddOns\"
Copy-Item C:\praxis\bridge-src\addon\NT8BridgeServerPlayback.cs "$D\NinjaTrader 8\bin\Custom\AddOns\"
Get-ChildItem "$D\NinjaTrader 8\bin\Custom\AddOns" | Select-Object Name,Length,LastWriteTime
```
- Do not copy `AutoReconnect.cs` or `ChartDataSeriesSwitcher.cs` (section 1, limit 5).
- **You should see:** both names in the listing.
- **Reply line:** paste both listings.

**3.3 Compile in NT8 — wait for Amear's word on section 2, item 6.** The README's first compile is a step inside NT8 (`README.md:54@9664d9b`: "In NinjaTrader, open the NinjaScript Editor and **compile (F5)**"). NT8 compiles "the whole tree" (`report:141`). The bridge's own `compile` command is not permitted (section 1, limit 4). Who presses F5 is Amear's (item 6). This file assumes neither path. Follow only the path his words name:
- **If he does it by hand:** after 3.2, wait. Do nothing in NT8. When Amear tells you he has compiled, paste his words, word for word, and the result he gives you (clean, or the error lines) into the reply.
- **If he lets you drive NT8's window for this compile:** open the NinjaScript Editor, press F5, and copy what the editor shows. Do nothing else in NT8's windows. His word covers this one compile only; it does not cover the Strategy Analyzer tab (step 4.3).
- **If his words do not clearly name one of the two:** STOP and reply. Do not choose.
- **You should see:** no compile errors. If there are any, copy every error line (file, line, message) into the reply, and STOP. Do not edit any `.cs` file.
- **Reply line:** Amear's item-6 words, then "Compile by: Amear" or "Compile by: VM agent", then "Compile: clean" or the error lines.

**3.4 Check the request folders.** The AddOn polls `<UserDataDir>\NT8Bridge\trigger` and writes to `\result` (`report:47`; folders `report:145`):
```
$D = [Environment]::GetFolderPath('MyDocuments')
Test-Path "$D\NinjaTrader 8\NT8Bridge\trigger"; Test-Path "$D\NinjaTrader 8\NT8Bridge\result"
```
- **You should see:** `True` and `True` once NT8 has loaded the compiled AddOn. If `False`, restart nothing; reply with the output.
- These folders take requests from any process running as your Windows user, with no authentication (`report:173`; Correction 1, C1-3, `report:2868`: who can write them on the VM is UNVERIFIED). Whether that is acceptable is Amear's question (bridge NEEDS AMEAR 3, `report:227`).
- **Go-live (not these tests).** Amear: "Go-live checklist additions: remove the unauthenticated bridge request folders (or add auth) before real money; unmap Z: and turn off the SMB share." (DECISIONS.md:1234, D-2026-11-07-A ruling 10). Both items are in the go-live checklist of `docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md` (`:35` unmap Z: and the share; `:38` the request folders). They bind before real money. Whether the folders are acceptable for these tests stays section 2, item 4.

**3.5 Python CLI.** The README (`README.md:43–45@9664d9b`):
```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,report]"
```
- The base dependencies are `jsonschema`, `numpy`, `pyarrow` and `tzdata` (floors only, no lock file); "pip would download them on the VM" (`report:143`, INFERRED). The `[dev,report]` extras add `pytest>=7` and `matplotlib>=3` (`pyproject.toml:14–15@9664d9b`). The README's line also creates a venv in the clone (`README.md:43@9664d9b`).
- **Amear's rule:** "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(11)).
- **Mismatch.** The bridge declares version floors, not pins: `jsonschema>=4, numpy>=1.24, pyarrow>=14, tzdata`, no lock file (`report:143`; the line above). His "pinned requirements" therefore names no file on this bridge. What "pinned" means here is the master's reading, per DECISION_LOG `2026-11-07T15:19:00Z` (WHO: praxis-master): "what "pinned" means on this bridge is the master's reading (INFERRED, labelled)". The list and the flags below are this unit's reading on the master's dispatch — INFERRED, not Amear's word; changeable by him.
- **What Code's reply may name, and nothing else.** `<ts>-CODE-cli-setup.md` may name only (i) the bridge's four declared base dependencies, `jsonschema`, `numpy`, `pyarrow`, `tzdata` (`report:143`), each written `name==version`; and (ii) the local install of the clone itself at `9664d9b`, `-e .`, which downloads nothing by itself and is exempt by name from the `==` rule. No extras: not `[dev]`, not `[report]`. His "only" is not softened.
- **His question, not Code's.** Whether the base packages' own dependencies (for example `jsonschema`'s) or the build backend (`pyproject.toml` declares `[build-system]` `requires = ["setuptools>=61"]`, `build-backend = "setuptools.build_meta"`, `report:2386–2388`, [C02]) count as "the bridge's pinned requirements" is **Amear's** question. This file does not answer it; Code's reply does not answer it either.
- **Prevention (INFERRED — this unit's reading, not his word; changeable by him).** Code's commands install the four packages with `pip install --no-deps` and the clone with `pip install --no-deps --no-build-isolation -e .`, so `pip` fails rather than fetching anything unnamed. `pip help install` on the Mac's pip 26.2.1 (OBSERVED 2026-11-07; whitespace collapsed, wrapped lines joined): "--no-deps Don't install package dependencies." and "--no-build-isolation Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already installed if this option is used." The VM's pip and its flags are UNVERIFIED.
- **Consequence (INFERRED; nothing tried).** Without their own dependencies the packages may fail to install or import; without `setuptools` in the venv the `-e .` build may fail. Then STOP and reply with the output; Code takes the dependency / build-backend question to Amear. Do not add a package, drop a flag, or retry another way.
- **Detection, after the fact.** If `pip`'s output shows any download other than the four named packages, STOP and reply. This only detects; the flags are the prevention.
- **The venv.** His words: "into its own venv under C:\praxis\" (DECISIONS.md:1231, D-2026-11-07-A ruling 7(11)). The README creates `.venv` inside the clone (`README.md:43@9664d9b`), i.e. `C:\praxis\bridge-src\.venv`, which lies under `C:\praxis\` (INFERRED fit — this file's reading, not Amear's word; changeable by him).
- **Now:** run `python --version` in `C:\praxis\bridge-src` and paste it. Create no venv. Then **STOP before `pip`.** Write `Z:\vm\replies\<ts>-STOP-pip.md`: it reports the `python --version` output and states that you wait for Code's pinned list (ruling 7(11)). It asks nothing. Write `FINISHED`.
- **Then** wait for `<ts>-CODE-cli-setup.md`. It quotes ruling 7(11) and names the exact commands: the venv command and every `pip` command, with the flags above. If that reply names any package other than the four, any extra, a package not written `name==version` (other than `-e .`), or a `pip` command without `--no-deps` (and, for `-e .`, `--no-build-isolation`), STOP and reply. Otherwise: write `STARTED`; type only those commands; write `<ts>-cli-setup.md` with their output; write `FINISHED`. Run nothing else from the clone. With no `cli-setup.md`, step 4 does not start (its gate needs it).

**Reply for step 3:** `Z:\vm\replies\<ts>-install.md` (3.1–3.4 outputs, and 3.5's `python --version`), then `<ts>-STOP-pip.md`.

## 6. Step 4 — test 2a spec

**Gate:** start only after all of these exist: (a) your `<ts>-cli-setup.md` reply; (b) `Z:\vm\replies\<ts>-CODE-go-2a.md`, which names who sets the Strategy Analyzer tab by hand and who reads the tab and the PRAXIS commission template back (4.3), as Amear decides it, and quotes the sim account named in Amear's step-0 words (section 2, item 5); (c) Amear's step-0 words name the sim account (section 2, item 5). Whether the 2a NT8 run is covered is answered in his words: "2a run: YES, covered by my lift. A test that needs a run includes the run." (DECISIONS.md:1229, D-2026-11-07-A ruling 5). Ruling 5 does not mention D-071, so limit 3 stands unchanged. Which strategy copy is answered by ruling 7(7) (step 4.2). Write `STARTED` first.

**Load the second skill.** Copy `Z:\vm\skills\praxis-nt8-bridge-backtest\SKILL.md` into your skills directory, the same way as in step 2, load it, and follow it. It is the short form of this step. If the skill and this step disagree, STOP and reply; do not choose.

**4.1 The reference (settlement 4, DECISIONS.md:1087).** "Exact match on 1,190 trades / $197,327.60, `NQCONTROW SEP25`". The record is `docs/reports/2026-11-01-three-strategy-results.md:73` (`| All | 1190 | $197327.60 |`), instrument `:86` (`NQCONTROW SEP25`).

**4.2 The strategy copy — hash it first.** Amear's hard STOP: "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(7)). Which copy is answered: the committed base. The VM copies were never hash-checked (`docs/reports/2026-11-01-three-strategy-results.md:108`; `report:128`). The HEAD hash, from the committed file, not the Mac working tree (captured 2026-11-07 at HEAD `43b34b1`, OBSERVED):
```
$ git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256
35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265  -
```
On the VM, hash the copy NT8 compiles, and the repo copy as seen through Z::
```
$D = [Environment]::GetFolderPath('MyDocuments')
certutil -hashfile "$D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs" SHA256
certutil -hashfile Z:\ninjascript\PraxisNoiseAreaBreakout.cs SHA256
```
- Compare each hash with the HEAD hash above, ignoring case and spaces.
- The NT8 copy (`bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs`) is the one his words name: "the VM's installed copy" (DECISIONS.md:1231, D-2026-11-07-A ruling 7(7)). If it differs from HEAD, STOP — his words.
- The Z: copy is this file's extra check, not his words: Z: is the Mac working tree, not HEAD (INFERRED, as Z: = repo root in §0). If it differs, STOP too.
- The HEAD blob is LF-only, 14318 bytes (OBSERVED at `43b34b1`: `git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | wc -c` → `14318`; `… | grep -c $'\r'` → `0`). On a mismatch, also report each copy's byte size and whether it holds a CR, read-only (untried):
```
(Get-Item "$D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs").Length
[IO.File]::ReadAllText("$D\NinjaTrader 8\bin\Custom\Strategies\PraxisNoiseAreaBreakout.cs").Contains("`r")
(Get-Item Z:\ninjascript\PraxisNoiseAreaBreakout.cs).Length
[IO.File]::ReadAllText("Z:\ninjascript\PraxisNoiseAreaBreakout.cs").Contains("`r")
```
  Still STOP. Fix nothing.
- On any STOP here: paste the outputs, write the STOP reply, write `FINISHED`, and do nothing further in the VM session — not only in NT8 — until a new Code reply. Do not copy, edit or recompile the strategy. Scope: INFERRED — the master's reading, not Amear's word; changeable by him. The master's filing note calls ruling 7(7) "a hard STOP condition for the VM session" (`docs/reports/2026-11-07-amear-rulings-morning.md`:42; DECISIONS.md:1268 records that as the master's reading). Amear's words do not say step or session.
- If the file is not at that path, search `"$D\NinjaTrader 8\bin\Custom"` for `PraxisNoiseAreaBreakout.cs`, report every path found, and STOP.

**4.3 The hand-set Strategy Analyzer tab.** `backtest` "presses Run on a Strategy Analyzer tab **already open and set up by hand**" (`report:28`). It needs an open Strategy Analyzer window (`report:59`). It never sets the backtest type (`report:64`). And "No explicit bridge field sets 1-minute Standard fill resolution, 2 ticks/side slippage or the PRAXIS commission template" (`report:89`). Correction 1, C1-2 (`report:2866`): the tab can be set by hand (route a); routes b–d are UNVERIFIED. Who sets the tab by hand — Amear, or you driving NT8's window — is not decided here. Whether you may drive NT8's window is asked only for the compile (section 2, item 6), and an answer there does not reach this tab: Code's go-2a reply names who sets it, and who reads it and the template back, as Amear decides. Whether a hand-set tab counts is answered in his words: "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then." (DECISIONS.md:1230, D-2026-11-07-A ruling 6). The state this records is set out in 4.6.

Where each row comes from: row 1 (Strategy) from `report:93` (strategy `PraxisNoiseAreaBreakout`); row 2 (Backtest type) from `report:114`; rows 3–21, all 19, from Amear's C4 line (`docs/reports/2026-10-31-voice-session-notes-2.md:111`, REPORTED BY amear: "Settings, same as the 10-31 run: NQCONTROW SEP25 · Last · Minute 1 · 2021-03-08 → 2026-07-17 · CME US Index Futures RTH · Break at EOD ✓ · Include commission ✓ PRAXIS · Max bars look back 256 · Bars required 20 · Standard (Fastest) · Fill limit on touch ☐ · Slippage 2 · Entries per direction 1 · All entries · Exit on session close ✓ · Set order quantity Strategy · DAY · BandOrVWAP · Contracts 1."):

| # | Setting | Value |
|---|---|---|
| 1 | Strategy | `PraxisNoiseAreaBreakout` (`report:93`) |
| 2 | Backtest type | Backtest (`report:114`) |
| 3 | Instrument | `NQCONTROW SEP25` |
| 4 | Price based on | Last |
| 5 | Type / Value | Minute / 1 |
| 6 | Start date → End date | 2021-03-08 → 2026-07-17 |
| 7 | Trading hours | CME US Index Futures RTH |
| 8 | Break at EOD | ✓ |
| 9 | Include commission | ✓, template `PRAXIS` |
| 10 | Maximum bars look back | 256 |
| 11 | Bars required to trade | 20 |
| 12 | Order fill resolution | Standard (Fastest) |
| 13 | Fill limit orders on touch | ☐ (off) |
| 14 | Slippage | 2 |
| 15 | Entries per direction | 1 |
| 16 | Entry handling | All entries |
| 17 | Exit on session close | ✓ |
| 18 | Set order quantity | Strategy |
| 19 | Time in force | DAY |
| 20 | Exit mode | BandOrVWAP |
| 21 | Contracts | 1 |

**Commission — the run's own, not the amended one.** The PRAXIS template held Minimum 0.00 / Per unit 1.48 on a Future row and a `NQCONTROW SEP25` row (`docs/reports/2026-10-31-voice-session-notes-2.md:104–106`, REPORTED BY amear). The reference CSV shows $2.96 on every trade: `commission/trade={'2.96': 1190}` (`docs/reports/2026-11-01-csv-analyses.md:51`). Use that. The amended MFFU $4.68 is NOT used for this reproduction (D-2026-11-06-B, S6 cross-block, DECISIONS.md:1104: "An exact-match reproduction (item 4) therefore needs the commission used then, not the amended $4.68"). Whoever Code's go-2a reply names reads the PRAXIS template (Tools → Commissions → PRAXIS, the path Amear used, `docs/reports/2026-10-31-voice-session-notes-2.md:99`) without changing it; you report the rows. If it does not show 1.48 per unit on those rows, STOP and reply.

Once the tab is set, whoever go-2a names reads every row of the table back from the screen; you record what is read, and by whom. Any row that differs from the table: STOP and reply; do not run.

**4.4 The bridge config file.** `backtest` reads only `params` from the request (`report:63`). The other config fields are "reference fields" (`README.md:182@9664d9b`), and the AddOn never reads `slippageTicks` or `commission` (`report:63`). Copy the example and edit only the values:
```
Copy-Item C:\praxis\bridge-src\config\config.json C:\praxis\2a-config.json
```
Set: `"strategy": "PraxisNoiseAreaBreakout.cs"`, `"typeName": "PraxisNoiseAreaBreakout"`, `"instrument": "NQCONTROW SEP25"`, `"barType": {"type": "Minute", "value": 1}`, `"from": "2021-03-08"`, `"to": "2026-07-17"`, `"commission": "PRAXIS"`, `"slippageTicks": 2`, `"params": {"ExitMode": "BandOrVWAP", "Contracts": 1}`. Leave `capital` as it is. `params` is injected by property name; `ExitMode` and `Contracts` are the strategy's two declared inputs (`report:113`).

**4.5 Run — the only two bridge commands permitted.** From `C:\praxis\bridge-src`, venv active (if `Activate.ps1` was blocked, type `.venv\Scripts\python -m nt8bridge` in place of `python -m nt8bridge`, limit 9):
```
python -m nt8bridge ntstatus
python -m nt8bridge backtest --config C:\praxis\2a-config.json --timeout 1800
```
- In the code, the `ntstatus` result includes `"ntVersion"`, set from `NtCoreVersion()` (Correction 2, C2-3, `report:2959–2960`). Whether that string equals the build Help → About shows is UNVERIFIED (`report:2962`). Record both.
- `--timeout` exists in the README's form (`README.md:174@9664d9b`, `--timeout 300`). The value 1800 is this file's untried choice for a five-year 1-minute run. If it times out, reply. Do not retry with other flags.
- No `--pdf`: that needs the `report` extra (`README.md:45@9664d9b`).
- The result is written to `<UserDataDir>\NT8Bridge\result\backtest_<id>.json` (`report:67`). The response shape is `{id, status, strategy, metrics:{totalTrades, profitFactor, netProfit, maxDrawdown}, trades:[...]}` (`report:65`). Whether `netProfit` (`CumProfit`) is net of the template commission is UNVERIFIED (`report:68`). The trade list is capped at 5000 (`report:66`), above 1190 (`report:127`).

**4.6 Pass / fail.**
- **PASS** = `metrics.totalTrades` is exactly `1190` AND `metrics.netProfit` is exactly `197327.60` (to the cent).
- This PASS is the numbers check only. Amear's test reads "drives the baseline from the terminal" (DECISIONS.md:1003). His words on a hand-set tab: "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then." (DECISIONS.md:1230, D-2026-11-07-A ruling 6).
- **The recorded state.** A 2a PASS on a hand-set tab = "bridge reproduces the baseline" = a PARTIAL PASS of the in-VM automation lift (D-2026-11-06-A item 2, DECISIONS.md:1003). It is NOT "driven from the terminal". The full lift needs a run whose settings come from the bridge/config, not his hands. His words do not say a partial pass lifts any part of the restriction (DECISIONS.md:1264). Who sets the tab by hand is still not in his words ("not my hands" (DECISIONS.md:1230, D-2026-11-07-A ruling 6) may mean his hands set it — INFERRED, DECISIONS.md:1264); it stays the go-2a reply's question.
- **FAIL** = anything else the run returns: another number, an error, or a timeout. (A hash, template or setting mismatch stops the step before the run, at 4.2–4.3.)
- On PASS or FAIL, paste the whole result JSON in the reply — at least `id`, `status`, `strategy` and `metrics`, and the first and last three `trades` entries — and the `ntstatus` output.
- Code and praxis-auditor judge 2a (settlement 8, DECISIONS.md:1091: "Code + praxis-auditor judge 2a/2b and log the lift under his ruling"). You report; you do not declare the lift.

**Reply:** `Z:\vm\replies\<ts>-2a-result.md`. Then `FINISHED`.

## 7. Reply format and the reply files expected

Every reply is a Markdown file in `Z:\vm\replies\` named `<ts>-<slug>.md`. A reply is never edited after it is written. To correct one, write a new reply that names the old file.

Each reply — yours and Code's — has these lines first, in this order:
```
REPLY-TO: Z:\vm\2026-11-06-vm-handoff.md step <n>
WRITTEN-BY: <your identity, as in step 1>
UTC: <ts>
RESULT: DONE | STOP | FAIL
```
Then these sections:
- `## Commands typed` — every command, exactly as typed.
- `## Output` — the output, pasted unedited, in a fenced block per command.
- `## What I saw on screen` — only for things you read from NT8's windows; copy the text exactly.
- `## Could not do` — each item and why, or "none".

Files expected, in order (Code writes the `CODE-` ones):
1. `<ts>-STATUS.md` — `STARTED`
2. `<ts>-self-report.md` — step 1
3. `<ts>-2b-skill-job.md` — step 2
4. `<ts>-STATUS.md` — `FINISHED`
5. `<ts>-CODE-2b-verdict.md` — Code; holds `2b: PASS` or `2b: FAIL`, and `SNAPSHOT: confirmed` only if Amear's step-0 words say so
6. `<ts>-STATUS.md` — `STARTED`
7. `<ts>-install.md` — step 3.1–3.4
8. `<ts>-STOP-pip.md` — step 3.5; reports `python --version`; waits for Code's pinned list
9. `<ts>-STATUS.md` — `FINISHED`
10. `<ts>-CODE-cli-setup.md` — Code; quotes ruling 7(11) and names the exact commands: venv, then `pip` for only `jsonschema`, `numpy`, `pyarrow`, `tzdata` (each `==version`, `--no-deps`) and the clone's `-e .` (`--no-deps --no-build-isolation`); no extras (step 3.5)
11. `<ts>-STATUS.md` — `STARTED`
12. `<ts>-cli-setup.md` — step 3.5, the named commands only
13. `<ts>-STATUS.md` — `FINISHED`
14. `<ts>-CODE-go-2a.md` — Code; names who sets and who reads back the tab and the PRAXIS template, and quotes the sim account from Amear's step-0 words
15. `<ts>-STATUS.md` — `STARTED`
16. `<ts>-2a-result.md` — step 4
17. `<ts>-STATUS.md` — `FINISHED`

Any STOP: write the STOP reply, then `FINISHED`, then wait.

## 8. What his words settle, and what is still his

This file answers none of these. Where a row is settled, the answer is Amear's words, quoted with their line; this file only points to them. Where a row is not settled, it is his. The bridge report's NEEDS AMEAR (`report:225–236`), each mapped:

| # | Question (short) | Settled? |
|---|---|---|
| 1 | Lift for importing the AddOn; which files | Partly. The lift covers "bridge install + its import" (settlement 6, DECISIONS.md:1089). The file set is not in his words: this file proposes only the two the AddOn needs (`report:40`, `report:141`), and asks him at step 0 (item 3). **Amear's.** |
| 2 | Is the install an "import"; order; whose hand | Install via terminal and the order are settled by ruling 1 ("the VM agent installs cli-nt-bridge via terminal, after a VMware snapshot") and settlement 6; the one in-NT8 compile step is **Amear's** (step 0 item 6). Step 3.3 waits on it. |
| 3 | Is an unauthenticated file-drop folder acceptable | **Amear's.** Asked at step 0 (item 4); step 3 waits on it. Ruling 10 bears on it ("before real money" (DECISIONS.md:1234, D-2026-11-07-A ruling 10)) but does not answer it for these tests (INFERRED — the master's reading (DECISION_LOG 2026-11-07T15:19:00Z, WHO: praxis-master), not Amear's word; changeable by him). Step-0 item 4 stays. |
| 4 | Rule out `playbackrun`, `reconnect`, `flatten`, `strategies`, `ghostorders`, AutoReconnect | Settled by his words — "(4) playbackrun/reconnect/flatten/strategies/ghostorders/AutoReconnect stay forbidden until live-trading design says otherwise." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(4)). Remains: this file's narrower command list for these steps (limit 4). |
| 5 | NT8 Guard in or out | Settled by his words — "(5) NT8 Guard out." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(5)). Remains: nothing for these steps (limit 6). |
| 6 | Which NT8 build is on the VM | Who reads it is settled (settlement 7: the VM agent reads, Code records). The value is pending your step 1. |
| 7 | Which strategy copy / hash | Settled by his words — "(7) 2a uses the committed base PraxisNoiseAreaBreakout.cs; the VM's installed copy must hash-match HEAD, or STOP." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(7)). Remains: step 4.2 gathers the hashes; the Z: check is this file's extra. |
| 8 | Which account the tests use | **Amear's.** Sim101 or the sim account he names; asked at step 0 (item 5). Steps 3 and 4 wait on it (limit 1). |
| 9 | Snapshot before the import; his hand step? | Settled by his words — "Snapshot is my hand step: confirmed." (DECISIONS.md:1232, D-2026-11-07-A ruling 8). Remains: the order (ruling 1, "after a VMware snapshot") is unchanged; he takes it at step 0. |
| 10 | Does a hand-set tab count for "drives the baseline from the terminal" | Settled by his words — "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal". The full in-VM automation lift needs a run whose settings come from the bridge/config, not my hands. Log it as a partial pass until then." (DECISIONS.md:1230, D-2026-11-07-A ruling 6). Remains: who sets the tab by hand stays **Amear's** → go-2a (4.6). |
| 11 | How the source reaches the VM; may `pip` download | `pip` half settled by his words — "(11) pip may download only the bridge's pinned requirements, into its own venv under C:\praxis\." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(11)); floors, not pins: see step 3.5 for the mismatch. Whether the base packages' own dependencies and the build backend (`setuptools>=61`) count as "the bridge's pinned requirements" is **Amear's** (step 3.5). Route half ("How the source reaches the VM") stays **Amear's**, step-0 item 2; the HTTPS clone is only the master's proposal. |
| 12 | How each walk-forward arm runs through the bridge | Settled by his words — "(12) you propose how each arm runs through the bridge after 2a passes." (DECISIONS.md:1231, D-2026-11-07-A ruling 7(12)). Remains: the master proposes; see section 9 — a proposal, not in force. No walk-forward is run here. |

Settled since 2026-11-06:
- Whether the 2a NT8 run on the VM needs his separate word (D-2026-11-06-A NEEDS AMEAR 6, DECISIONS.md:1046): the run half is answered in his words — "2a run: YES, covered by my lift. A test that needs a run includes the run." (DECISIONS.md:1229, D-2026-11-07-A ruling 5). The D-071 half is not: "The D-071 half of that question is not answered by ruling 5's words." (DECISIONS.md:1263). Limit 3 stands.

Still not decided here:
- Whether 2a/2b have passed. Code and praxis-auditor judge that (settlement 8). A 2a PASS on a hand-set tab is logged as a partial pass per ruling 6 (step 4.6). Recording the lift is "under my ruling" — his.

## 9. PROPOSED by the master (ruling 7(12)) — not for the VM agent to execute; takes effect only by Amear's word after 2a passes

Amear, D-2026-11-07-A ruling 7 (DECISIONS.md:1231): "(12) you propose how each arm runs through the bridge after 2a passes."

**Status.** This section is the master's proposal under ruling 7(12). It is not his word and it is not in force. VM agent: run nothing in it; no step above points here. Nothing in it has been tried. It states no backtest or P&L figure; the standing limitation in §0 applies to every run it proposes. Grades: OBSERVED (run on the Mac at HEAD `43b34b1`, output pasted here), REPORTED BY <source:line>, INFERRED, UNVERIFIED.

**9.1 Arm (a) — fixed rules, the judged arm.**
- One full-span `backtest` of the committed base `ninjascript/PraxisNoiseAreaBreakout.cs`, sha256 `35393823e9bc146e95dcb1d9f6fe5785a3c72ee3a3fb71287f33fe2242752265` at HEAD `43b34b1` (OBSERVED: `git show HEAD:ninjascript/PraxisNoiseAreaBreakout.cs | shasum -a 256` gives that hash). The 4.3 tab settings, except the commission. Before it, the 4.2 hash check, or STOP (the master's, by analogy with 7(7); his words name 2a).
- Commission: the walk-forward $4.68 (D-2026-11-06-C; `config/backtest-cost-model.json`:19, `"commission_round_turn_usd": 4.68`, OBSERVED by `grep -n`).
- Reported on the 17 out-of-sample windows plus the full-span total (REPORTED BY `docs/specs/2026-11-06-walk-forward-values.md`:42, §2; windows §5).
- **The $4.68 commission is a HAND STEP.** `backtest` reads only `params` from the request, and the AddOn never reads `commission` or `slippageTicks` (REPORTED BY `report:63`; 4.4). So $4.68 must sit on the tab's commission template (mechanism REPORTED BY the code read; UNVERIFIED on the VM). The PRAXIS template held 1.48 per unit (REPORTED BY amear, `docs/reports/2026-10-31-voice-session-notes-2.md:104–106`; no 2a read exists yet, 4.3), so a $4.68 template is a changed or a second template in NT8 (INFERRED). Whose hand, and which template: **Amear's**.
- Ruling 6 (DECISIONS.md:1230): "Strategy Analyzer tab: a hand-set tab may be used for 2a and counts as "bridge reproduces the baseline". It does NOT count as "driven from the terminal"." Walk-forward runs on a hand-set tab inherit that status (INFERRED, the master's; his words name 2a).

**9.2 Arm (b) — acceptance tests, then the 81.**
- **Precondition.** `ninjascript/PraxisNoiseAreaBreakoutArmB.cs` from branch `arm-b/wf-tunables` is installed on the VM, and its installed copy hash-matches that branch's HEAD, or STOP. This is the 7(7) rule applied by analogy (INFERRED, the master's; his words name 2a and the base file).
- The branch does not exist yet (OBSERVED): `git rev-parse --verify -q arm-b/wf-tunables; echo $?` printed `1`; `git branch -a | grep -c arm-b` printed `0`.
- How the file reaches the VM, and who installs and compiles it in NT8: **Amear's** (like step-0 items 2 and 6).
- The tab's strategy (arm (b)'s class in place of the base) is also on the tab, not in the request, so it is a hand step too (INFERRED from `report:63`).
- Then acceptance tests T1–T13 (spec §9), run with `backtest` but not decided by its result alone (spec lines checked by `sed -n`): T5(i) and T6(ii) read the strategy's prints in NT8's Output window (spec :156, :188, :190); T1–T3 and T13 compare NT8's own trade lists, with quantity (and, for T13, each row's commission), because the bridge's trades carry neither (spec :180, :212; `report:66`); the oracle scripts of T6(ii) and T8–T12 run on the Mac over the exported trade lists and the data file (spec :225); T6(i) is a static read on the Mac, not a run (spec :190, :225). How those reach the Mac: 9.4 item 9.
- The T-runs use $2.96 and the 81 use $4.68 (9.3), so the tab's commission template changes between them. That change is a hand step too; whose hand is **Amear's** (INFERRED mechanism, as 9.1).
- Then 81 `backtest` requests differing only in `params`: the five inputs Lookback, NoiseMult, StopAtrMult, ExitPolicy, Contracts, all five in every request (spec §7). Example (spec :157): `{"Lookback":18,"NoiseMult":1.2,"StopAtrMult":2.25,"ExitPolicy":"Flat1559","Contracts":1}`. One config file per request, as 4.4 (INFERRED). Full span each.
- Each configuration's result JSON, trades included, is saved and copied to `Z:\vm\replies\wf\<config-id>.json`. This is a new path under the reply folder; the one rule (§0) allows writing under `Z:\vm\replies\`. That the VM agent does the copy, from `<UserDataDir>\NT8Bridge\result\backtest_<id>.json` (`report:67`), is the master's proposal. The `<config-id>` scheme is not set here.
- Window selection (spec §5–§6) and CSCV/PBO (spec §7) run on the Mac from those trade lists. RULED, ruling 4 Q7 (DECISIONS.md:1225): "Q7 NT8 full-span runs per configuration through the bridge, window selection and PBO on the Mac from NT8's trade lists. That keeps one copy of the strategy (NT8); only the selection maths runs on the Mac."

**9.3 Commission by run kind — quoted, not chosen anew.** D-2026-11-07-B (DECISIONS.md:1456): "Walk-forward runs use $4.68 (`config/backtest-cost-model.json`:19, `"commission_round_turn_usd": 4.68`). Acceptance runs use $2.96, the committed reference runs' figure." Spec §9 (:159): "Every acceptance run uses the committed $2.96 commission, so the reference figures apply; every walk-forward run uses $4.68 (§7)." Arm (a) is a walk-forward run (spec §2, §7; INFERRED).

**9.4 UNVERIFIED mechanisms, each named.**
1. Timeouts for full-span runs: 1800 s (4.5) is untried. No other value is proposed.
2. Whether one hand-set tab serves many consecutive `backtest` runs.
3. Whether `params` reaches the `[NinjaScriptProperty]` inputs of the arm (b) class: mechanism REPORTED BY `report:72` and `report:113` (code read, not run). The class does not exist yet.
4. Whether the tab's backtest type persists: `backtest` never sets it (`report:64`).
5. The 5000-trade cap (`report:66`) against each configuration's trade count. Spec §7 treats a run of exactly 5,000 trades as truncated.
6. Whether `netProfit` (`CumProfit`) is net of the template commission (`report:68`). Spec §7 settles the gross case.
7. Whether the trade list carries what CSCV needs. `report:66`: "Each trade carries pnl, side, entry and exit time and price, and exit name. There is no per-trade commission or quantity." T1–T3 and T13 read quantity from NT8's own trade lists, not the bridge's (spec :180, :212); how those lists reach the Mac is item 9.
8. The copy to Z: (9.2): the master's proposal; untried.
9. How the NT8 Output-window text and NT8's own trade lists are captured on the VM and moved to Z: is not set here — UNVERIFIED. The only bridge commands permitted are `backtest` and `ntstatus` (limit 4); the `backtest` response shape (`report:65`) carries neither (INFERRED). Who does it, and by what route: **Amear's**.

**9.5 Not answered here.** §8 rows 1, 2, 3 and 8, and row 11's route half, stay **Amear's**; row 6 is a pending value from step 1 (DECISIONS.md:1278). Nothing in §9 answers them, nor who sets the tab by hand, nor the account. §9 takes effect only by his word, after 2a passes.
