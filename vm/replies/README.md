# Z:\vm\replies — reply convention

This folder is the only place on the share the VM agent may write. Code (on the Mac) also writes its own replies here, named `<ts>-CODE-<slug>.md`, with the same header.

- **Name:** `<ts>-<slug>.md`, where `<ts>` is UTC from PowerShell: `(Get-Date).ToUniversalTime().ToString("yyyyMMdd'T'HHmmss'Z'")`.
- **Never edit or delete a reply.** To correct one, write a new reply that names the old file.
- **Session markers:** `<ts>-STATUS.md` holding `STARTED` before the VM agent's first step, and `FINISHED` when it stops. Code starts no agent between the two (one-session rule).
- **Format:** the first four lines are `REPLY-TO:`, `WRITTEN-BY:`, `UTC:`, `RESULT: DONE | STOP | FAIL`. Then `## Commands typed`, `## Output` (pasted, unedited), `## What I saw on screen` (if any), `## Could not do`.
- **Order and full rules:** `Z:\vm\2026-11-06-vm-handoff.md`, section 7.

This README holds no reply. The folder is empty of replies when the handoff is written.
