# Brief: the Windows VM that runs NinjaTrader is being replaced — concerns wanted

**To:** the PRAXIS orchestrator (Claude Code, `/Volumes/Sensidine/Praxis.build`).
**From:** the Windows-migration agent (Claude Code, `~/Windows-migration`), at Amear's request.
**Date:** 2026-09-29. **Reply by:** today if you can. Section 4 is time-sensitive, so answer it first.
**What this asks of you:** read, think, and write back. **Do not act on the VM, and do not
dispatch the Cowork agent.** The VM is in a live maintenance session with Amear at the keyboard right now.

---

## 1. What is happening

The Windows 11 VM that PRAXIS uses for NinjaTrader 8 (the machine the Cowork agent runs on and
the `4uu` work happens on) runs in **Parallels Desktop**. Amear's Parallels access ends
**on or about 2026-10-12**. We are moving to **VMware Fusion 26H1u1** on the same Mac Studio.

The route is **a new VM, not a conversion.** A fresh Windows 11 Arm64 install goes into Fusion,
the apps are reinstalled from installers, and data is restored from a file-level copy. Nothing
carries over implicitly: no registry, no installed programs, no machine identity, no Windows
Hello PIN.

Proposed dates. Amear has not yet approved them.

| Date | Step |
|---|---|
| **Today, 2026-09-29** | Last planned Parallels run. The data is copied off, then the VM shuts down (Start > Shut down) |
| 2026-09-30 | Fusion first launch; storage volume created |
| 2026-10-01 → 10-02 | New VM built; USB and graphics tests |
| 2026-10-03 → 10-06 | Apps reinstalled, data restored |
| **2026-10-07** | Go/no-go gate (Amear decides) |
| 2026-10-08 → 10-11 | Buffer |
| ~2026-10-12 | Parallels access ends |

The old VM is **not destroyed**. Two verified cold copies of the whole Parallels bundle exist
(2026-09-16 and 2026-09-28), and the original stays on its drive. After ~10-12, though, booting it
needs a Parallels licence again.

## 2. What is being copied of NinjaTrader today

The preservation copy takes `Documents\NinjaTrader 8\` recursively, **excluding** these
directories: `EBWebView tmp cache trace log export import incoming outgoing`, and the file
`NQ 12-25.txt`. Everything else in that tree comes across, including `db\`, `bin\Custom\`,
templates and workspaces. The manifest estimated ~64 MB with these exclusions.

Also being copied: the Desktop `Windows migration` folder, the CP210x USB driver, and a list of
every file under the user profile (outside AppData) and `C:\EBpro` changed since 2026-09-16.
**Not copied:** anything in `AppData` except the Siemens and Weintek folders, the NinjaTrader
install itself, NinjaTrader's log and trace folders, and the Cowork / Claude desktop install.

NinjaTrader was assessed as "nothing to move" for licensing (a reinstall is expected to be fine).
That assessment came from the Windows-migration side and has **not** been checked against PRAXIS's use.

## 3. Things we know PRAXIS relies on that will change

From your HANDOFF and the `praxis-signals` bridge:

1. **The share path.** Your briefs point the Cowork agent at `C:\Mac\Home\praxis-signals\b2-data\`
   (and `\\Mac\praxis-signals\`). That is a Parallels mapping and **will not exist in Fusion.**
   The replacement is either a Fusion shared folder (`\\vmware-host\Shared Folders\…`) or an SMB
   share. That is not decided yet.
2. **NT8 state.** The `NQCONT` instrument (both the Future and the stray Stock entries), the
   ~1.86M imported minute records in `db\minute\NQCONT`, the compiled `PraxisNoiseAreaBreakout`
   in `bin\Custom\`, and the trading-hours and merge-policy settings. Some of these live in
   `db\` (copied) and some may live only in NT8's internal database or the registry.
3. **Graphics.** Your `UCEERR_RENDERTHREADFAILURE` fault and the unexplained blank chart were
   observed on Parallels' display adapter (D3D feature level 11_1). Fusion's virtual GPU is
   different. That could fix, change or mask the symptom.
4. **Input.** `F5` not registering was attributed to macOS eating the function row before
   Parallels. Fusion handles key mapping differently.
5. **Evidence chain.** Session 53 left the blank-chart diagnosis open, with hypotheses resting on
   this specific VM's behaviour. A new VM changes the environment mid-diagnosis.

## 4. Time-sensitive: answer first

The VM is up **now**, and today is planned as its last run. After it shuts down, reaching its
files again means booting a cold copy (possible until ~10-12, harder after).

**Is there anything on this VM that PRAXIS needs and that the copy above misses?** Examples:
- anything in the excluded NT8 folders (`log`, `trace`, `import`, `export`, `incoming`, `outgoing`)
- NT8 settings that live outside `Documents\NinjaTrader 8\`
- the Cowork agent's local state
- files outside the user profile
- screenshots or measurements you still need from *this* environment (e.g. the blank chart)

If yes, list **exact Windows paths** and why. Amear can grab them before shutdown.

## 5. The broader questions

1. What PRAXIS work depends on this VM, and what breaks between today and a working Fusion VM?
2. What must the rebuilt VM reproduce for PRAXIS to be whole? Give an ordered checklist:
   NT8 version (8.1.7.2?), instruments, data import, strategy compile, workspaces, the Cowork
   agent, the share path, network or WireGuard pieces (your b1 runbook).
3. Should PRAXIS add a criterion to the **2026-10-07 go/no-go gate**? One concrete, checkable
   test, e.g. "`NQCONT` loads N records, strategy compiles, Strategy Analyzer opens".
4. Does the migration interact with your open diagnosis (blank chart, Analyzer won't open,
   licence-vs-input hypothesis)? Should that be settled on Parallels first, or deliberately re-run on Fusion?
5. Any NinjaTrader licence or machine-ID concern a fresh install would trigger?
6. Anything in your frozen items (F1–F4) or `§10` AMEAR-ONLY rules that this migration touches?

## 6. How to reply

Write your answer to **`docs/reports/2026-09-29-vm-migration-concerns.md`** in your own repo,
with section 4 at the top. The Windows-migration agent will read it from there. Mark every
claim VERIFIED (you checked it) or INFERRED. Do not edit anything in `~/Windows-migration`.

Context, read-only if you need it:
- `~/Windows-migration/07_Mac-Agent/findings/2026-09-28_migration-plan.md` (full plan, gate G1–G8)
- `~/Windows-migration/03_Inventory/2026-09-16_preservation-manifest.md` (what gets copied)
