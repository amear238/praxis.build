---
name: praxis-vm-reporter
description: Test 2b simple job for the PRAXIS VM agent — list NT8's AddOns folder, check the NT8Bridge trigger/result folders exist, and write one reply file under Z:\vm\replies\ in the required format. Read-only on NT8.
---

# praxis-vm-reporter

Source: `Z:\vm\2026-11-06-vm-handoff.md`, step 2. Nothing here has been tried.

## Limits (all apply)
- Read only. Change nothing in NT8, nothing in Windows, nothing on Z: except this one reply file and your `<ts>-STATUS.md` files.
- No orders, no account actions, no connect/reconnect/disconnect (D-071). Sim101 or the sim account Amear names only.
- No bridge commands. No installs, no downloads, nothing bought.
- Write only under `Z:\vm\replies\`. Never write the source title of circuit breaker #5.
- If anything below fails or looks different, record it and stop. Do not fix it.

## The job
Type these by hand in PowerShell, one at a time, and keep each output exactly:
1. `$D = [Environment]::GetFolderPath('MyDocuments'); $D`
2. `Get-ChildItem "$D\NinjaTrader 8\bin\Custom\AddOns" | Select-Object Name,Length,LastWriteTime`
3. `Test-Path "$D\NinjaTrader 8\NT8Bridge\trigger"`
4. `Test-Path "$D\NinjaTrader 8\NT8Bridge\result"`
5. `(Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")` — this is `<ts>`.

Before the bridge is installed, 3 and 4 are expected to print `False`.

## Required reply format
File: `Z:\vm\replies\<ts>-2b-skill-job.md`. Lines 1–5 exactly, in this order:
```
REPLY-TO: Z:\vm\2026-11-06-vm-handoff.md step 2
WRITTEN-BY: <your identity, as in your self-report>
UTC: <ts>
RESULT: DONE | STOP | FAIL
SKILL: praxis-vm-reporter loaded from <full path of the SKILL.md you loaded>
```
Then these four sections, in this order:
- `## Commands typed` — commands 1–5, exactly as typed.
- `## Output` — one fenced block per command, output pasted unedited.
- `## How I loaded this skill` — two or three sentences.
- `## Could not do` — each item and why, or `none`.

Do not grade the result. Code and praxis-auditor judge test 2b.
