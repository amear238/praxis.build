REPLY-TO: Z:\vm\2026-11-06-vm-handoff.md §1 limit 9 (install of Python and git), lifted by Amear for this install
WRITTEN-BY: Claude (Claude.ai Praxis channel, Cowork session), driving the VM over SSH from the Mac (host praxis-vm), commands run from the Mac via osascript
UTC: 20261111T172933Z
RESULT: DONE

## Authority (WHO: amear; REPORTED BY the Claude.ai channel)
- Voice, 2026-11-11 ~16:5xZ, on whether to snapshot first: "Okay, you know what? Let's forget about the snapshot. Let's have it execute those things first." Then: "Hermes is going to give me a uh, a physical button to accept or deny, so don't worry about that."
- Chat, 2026-11-11 12:27 ET (17:27Z), on the two open items (file the 2026-11-10 note; install Python and git in the VM): "U do them".
- No new snapshot was taken (Amear's choice). The last snapshot Amear reported is `pre-cli-nt-bridge-2026-11-06` (C9), which predates the SSH setup.

## Commands typed (from the Mac)
1. `ssh praxis-vm 'whoami; winget --version; <IsInRole Administrator>; Get-Process NinjaTrader ...'`
2. `ssh praxis-vm 'winget install -e --id Python.Python.3.12 --scope machine --silent --accept-package-agreements --accept-source-agreements --disable-interactivity --override "/quiet InstallAllUsers=1 PrependPath=1 Include_launcher=1"; ...; winget install -e --id Git.Git --scope machine --silent --accept-package-agreements --accept-source-agreements --disable-interactivity'`
3. `ssh praxis-vm 'python --version; (Get-Command python).Source; py -0p; git --version; (Get-Command git).Source; Get-Process NinjaTrader ...; $env:PROCESSOR_ARCHITECTURE'`

## Output
1. `[VM machine name]\amear` / `v1.29.380` / `True` / NinjaTrader `9600 2026-11-10 5:46:59 PM`
2. Python: "Found Python 3.12 [Python.Python.3.12] Version 3.12.10 … Downloading https://www.python.org/ftp/python/3.12.10/python-3.12.10-arm64.exe … Successfully verified installer hash … Successfully installed", `PYTHON_EXIT=0`. Git: "Found Git [Git.Git] Version 2.56.0.4 … Downloading https://github.com/git-for-windows/git/releases/download/v2.56.0.windows.4/Git-2.56.0.4-arm64.exe … Successfully verified installer hash … Successfully installed", `GIT_EXIT=0`.
3. `Python 3.12.10` at `C:\Program Files\Python312-arm64\python.exe` (`py -0p`: `-V:3.12-arm64 *`); `git version 2.56.0.windows.4` at `C:\Program Files\Git\cmd\git.exe`; NinjaTrader still pid 9600, start time unchanged; `PROCESSOR_ARCHITECTURE=ARM64`.

## What I saw on screen
none (SSH only).

## Limits kept
NinjaTrader not started, stopped or touched (same pid and start time before and after). No connection change (D-071). No orders. No pip run, no clone, no bridge files. No Windows restart. Nothing else installed. Only new files under `vm/replies/`.

## Could not do / open
- **Architecture (UNVERIFIED risk for step 3.5):** the VM is Windows on ARM64 and winget installed the ARM64 builds. Whether the bridge's dependencies (notably `pyarrow`, also `numpy`) have win_arm64 wheels at versions meeting the bridge's floors is not checked. If step 3.5 fails on a build-from-source, the fallback is an x64 Python (runs under emulation) — that is Amear's call, not taken here.
