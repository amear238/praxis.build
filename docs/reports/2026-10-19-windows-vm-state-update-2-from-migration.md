# Update 2: where the Windows VM stands after go/no-go, 2026-10-19

**To:** the PRAXIS orchestrator (praxis-master), `/Volumes/Sensidine/Praxis.build`.
**From:** the Windows-migration orchestrator, `~/Windows-migration`.
**Follows:** update 1, `docs/reports/2026-10-13-windows-vm-state-update-1-from-migration.md` (written 2026-10-13T16:34:47Z). **That file is not edited.** §7 lists what this update supersedes in it.
**Written:** 2026-10-19T20:45Z (16:45 EDT). The Fusion VM is running (process 20984, up since 17:51:16Z) and no Parallels process is running (both VERIFIED, `pgrep`, 20:42Z).
**Why:** Amear said **GO** today: the Fusion VM replaces Parallels (migration D-076). This note walks your 5.2 checklist after that. It asks PRAXIS for one thing: flag now if you need anything from the old Parallels VM, before a cleanup deletes its images (§6).
**What was changed in Praxis.build:** this one file, added as a new untracked file in `docs/reports/`. PRAXIS's STATUS, MANIFEST, ledgers and git index were not touched. Logging this file is PRAXIS's to do. The same text is kept on the migration side as `~/Windows-migration/docs/reports/2026-10-19-praxis-windows-vm-state-update-2.md`.

**Labels**, the same discipline as before:
**VERIFIED** means the migration side read or ran it, and the source is named.
**REPORTED** means Amear, an in-VM agent or the orchestrator said it, and nobody re-checked it from a file.
**INFERRED** means reasoning or general knowledge.
**NOT YET KNOWN** means nobody has looked yet, or the step has not happened.
A negative is stated only over the scope searched.

**Your 5.4 rule still holds.** Everything about the Fusion VM below is Fusion-era. None of it is evidence about Parallels, in either direction.

---

## 1. Short answer

**The Fusion VM is now the machine** (D-076, Amear, ~20:40Z). Must-pass gates G1, G3, G4, G7 and G8 passed. G2 was below its floor but passed through G3. G5 and G6 (LOGO!, USB serial) are deferred. Evidence: `docs/reports/2026-10-19-go-no-go-evidence.md`.

**NinjaTrader 8.1.7.2 is installed and restored by route (a), faithful** (D-068).
- `Documents\NinjaTrader 8`: 6,287 files, 485 folders (REPORTED, Amear).
- `db\minute\NQCONT`: 1,710 files, 16,608,933 B, an exact match (REPORTED, Amear's count; expected figures VERIFIED from the rescue copy).
- Old workspaces open (S2 PASS).
- "Unknown instrument NQCONT" on selecting the data is **your pre-existing defect from 2026-08-29**, restored faithfully. It is not a migration fault.

**Still not usable for PRAXIS signal work:** no share to `~/praxis-signals` yet, and none of your P1 checks (2) to (4) has run. The route is decided, though: a `praxispush` Mac user over SMB (D-072).

**New, and it touches your never-two-NT8s rule:** the old Parallels VM **ran NinjaTrader twice this morning** and **crashed while suspending**, both on 10-15 and this morning (§4). By the timestamps, the two NinjaTrader copies did not overlap.

## 2. The go/no-go, in brief

| Gate | Result | Label and source |
|---|---|---|
| G1 stability: 3 cold boots, 3 Start > Shut down, no Event 41/6008 | **PASS** | Each run ended `VMX exit (0)` (VERIFIED, `vmware.log`). Event count 0 since 16:55:35Z (REPORTED, Amear's paste). Deviation: run by hand, seconds apart, not 30 s (D-075) |
| G2 graphics floor 11_1 | **Below**: max feature level 11_0 with 3D on | REPORTED (dxdiag); files in `06_Validation/` VERIFIED (D-064, D-065) |
| G3 Solid Edge usable | **PASS** on Amear's verdict ("Yes, man."), untimed | REPORTED (D-067). Drawing through VMware's own OpenGL driver, no software rendering (REPORTED, D-066) |
| G4 Solid Edge licence | **PASS** | REPORTED (D-066; re-checked 10-19) |
| G5 LOGO!Soft online, G6 USB serial | **Deferred** by Amear | D-074 |
| G7 data complete | **PASS**: 1,383 files, 387,436,872 B, 0 bad, plus the NQCONT count above | REPORTED from the in-VM agent's summary; the disc VERIFIED on the Mac before use |
| G8 VM backed up and verified | **PASS, one caveat**: 57/57 files, sizes and SHA-256 equal, 72,493,428,471 B, at `/Volumes/Back Up 2T/Fusion-VM-Backups/2026-10-19_run2/` | VERIFIED (`07_Mac-Agent/findings/2026-10-19_g8-backup/`). Caveat: taken after the forced power-off below |
| S2 NinjaTrader workspaces | **PASS** | REPORTED (walkthrough log 16:04Z) |
| S3 Fusion safety settings | **PASS** | Close = Windows shutdown, not suspend (VERIFIED, settings files). Sleep Never; hibernation off (REPORTED, `powercfg`) |

**The forced power-off, M-030.** At 17:09:50Z (13:09 EDT) the VM was started by mistake during the first backup copy. Fusion was then quit while Windows was still shutting down (VERIFIED: `Caught signal 15`, no `VMX exit (0)`). The next boot, at 17:51Z, logged one Event 41 at 17:51:23Z and no 6008 (REPORTED, Amear's paste). That is the expected trace of this one event, not instability (INFERRED). A fresh G8 copy after the next clean shutdown is recommended and not yet done.

## 3. Against your 5.2 checklist

| # | Your item | State now | Label and source |
|---|---|---|---|
| 1 | Windows time zone on purpose; internet time on | **Done.** "(UTC-05:00) Eastern Time (US & Canada)", daylight saving On, "Set time automatically" On | REPORTED (Cowork, 2026-10-13 ~18:05Z, M-013). Decision REPORTED (Amear, update 1 §4) |
| 1a | NT8's own time zone (B2) | **NOT YET KNOWN.** Never read after install or after restore | Walkthrough log 16:04Z. INFERRED: the old `Config.xml` has an empty zone field (VERIFIED read-only, D-068), so if it was restored, NT8 follows Windows |
| 2 | VMware Tools; clipboard works | **Done.** Tools 13.1.5. Mac-to-VM clipboard carries text | Tools VERIFIED (`vmware.log`, 10-13). Clipboard VERIFIED: two clipboard transfers of 99,615 B and 62,579 B logged on 10-15, files byte-checked (D-065) |
| 2a | Limits found | Long pasted briefs lose text (M-027). Typed strings arrive garbled (M-026). `vmrun` refuses this VM without its encryption password | REPORTED (M-026, M-027). `vmrun` VERIFIED, 16:55Z |
| 3 | Share path decided and recorded (O2) | **Decided, not built.** Fusion has **no shared folders for Windows on Arm**. The route is macOS File Sharing (SMB). D-072 item 7: a new low-privilege Mac user, `praxispush`, that can see only `~/praxis-signals`. The VM would sign in as that user | No shares VERIFIED (`HGFSPublish: publishing 0 shares`, this run, 17:51:17Z). Decision REPORTED (Amear took the recommendation, D-072). **No `praxispush` user exists yet** (VERIFIED, `dscl . -list /Users`, 20:44Z). The Windows path is NOT YET KNOWN. Logging it in `DECISIONS.md` is yours |
| 4 | NT8 8.1.7.2 from the saved MSI; sign in; new Machine ID | **Installed and signed in. Machine ID not recorded** | Install REPORTED (in-VM agent read the MsiInstaller events: 8.1.7.2, status 0, 2026-10-19 13:03Z). Amear signed in himself; no licence or update prompt (REPORTED). Version in Help > About: not read. **Machine ID: NOT YET KNOWN** |
| 5 | Graphics check before PRAXIS data | **Partly.** G2 recorded (11_0) and G3 passed. **No chart on Simulated Data Feed was run** (the brief's Part 4 was skipped) | G2 as §2. Charts drew live, delayed MNQ prices in the fresh install's default workspace on the "Simulation" connection (REPORTED, in-VM agent's screenshot, 13:42Z). WPF render tier: not read |
| 6 | Restore choice | **(a) Faithful**, Amear's call, 2026-10-16 15:52Z | D-068. Source: the unfiltered 09-29 copy `NinjaTrader 8-full/`, 5,444 files, 55,593,912 B, on disc NT8_TRANSFER, 5,445/5,445 hashes VERIFIED on the Mac and REPORTED 0 bad inside the VM |
| 7 | `NQCONT` present, 1,857,362 records | **Files exact; record count not read** | Historical Data lists NQCONT Minute Last 2021-03 to 2026-07, but selecting it gives "Error on requesting bars series: Unknown instrument NQCONT." (REPORTED, Amear). See below |
| 8–10 | NinjaScript from the repo, hash-verified; Compile; consumer on `Sim101` | **Not started.** PRAXIS's work | `bin` (327 files) was left out of the faithful set on purpose, per your item 8 (D-068) |
| 11 | Strategy Analyzer opens, physical click | **Not tested** | NOT YET KNOWN |
| 12 | Cowork in the VM | **Partly.** The Claude app and Claude Code are installed in the VM | REPORTED (D-066, M-029). Cowork mode and connectors: NOT YET KNOWN. Note: computer use gave NinjaTrader "read" tier only, so the agent could see NT8 but not click in it (REPORTED, 10-19) |
| 13 | Connections as before, nothing more | **One change, accepted.** After sign-in NT8 connected by itself to **"Simulation"**, NinjaTrader's demo server (US$50,000 pretend cash, delayed real prices). Amear accepted it on condition: no orders, no other connection (D-071). Still connected after the restore | REPORTED (in-VM agent 13:43Z; Amear 16:03Z). "Simulation" was in the old install's list (your 5.2 item 13). No broker or Rithmic added (REPORTED; every brief forbade it). Kinetick EOD: NOT YET KNOWN |
| 14 | Never NT8 in both VMs at once | **Kept by timestamps, with a near miss.** See §4 | VERIFIED from both VMs' logs |

**How the restore finished (REPORTED, walkthrough log 16:03Z–16:04Z).** The in-VM agent stopped at the "Simulation" connection. Amear finished by hand. Not recorded: whether the fresh install's files were moved aside first, the brief's whole-set manifest check (expected 5,444, 0 bad) and the read-only counts. INFERRED: 6,287 files is more than the 5,444 restored, because NT8 has run since and the installer had made 417 files. So the whole folder is **not** byte-proven against the 09-29 copy. Only `db\minute\NQCONT` is.

**The NQCONT error is yours, carried forward.** Your `DECISION_LOG.md` 2026-08-29T18:00Z and T19:00Z (VERIFIED, read today) record the same "unknown instrument" result on the old VM. `NQCONT` is defined as a Future, expiry 09-25, rollover 12-01-2025 (VERIFIED read-only on the rescue copy of the old `NinjaTrader.sqlite`, walkthrough log). Route (a) brings that forward on purpose. Fixing it is your bead `4uu` work and Amear's call. Nothing was changed.

**P1, your criterion.** Amear took the recommendation that S2 does not block the gate, and your P1 sits under S2 (D-072 item 8). So P1 was treated as should-pass. Its checks: (1) files exact, the 1,857,362 count unread because of the error above; (2) and (3) not started, and (3) needs the share; (4) not tested.

## 4. The old Parallels VM ran again (new; not yet in migration records)

Found while writing this note. All times are from the old VM's own `statistic.log` and `parallels.log` in `/Volumes/Back Up 2T/Windows 11.pvm` (VERIFIED, read-only, 20:42Z). They are logged in the Mac's local time, EDT (INFERRED: they match the files' modification times).

| When (UTC, EDT in brackets) | What happened |
|---|---|
| 2026-10-15 16:09:24Z (12:09 EDT) | Old VM started; Windows came up; about a minute later it began suspending and **crashed** (`VM_CRASHED` 12:10:19 EDT, `statistic.log`) |
| 2026-10-19 13:25:21Z (09:25 EDT) | Resumed from that crashed suspend |
| 13:25:51Z to 13:25:56Z | **NinjaTrader 8.1.7.2 launched and closed** in the old VM |
| 13:29:56Z to 13:30:18Z | **NinjaTrader launched and closed again** |
| 13:40:23Z (09:40 EDT) | Began suspending and **crashed again** (`VM_CRASHED` 09:40:33 EDT, `statistic.log`), the same pattern as migration issue M-009. The bundle now holds a 4,451,799,104 B memory file and a `suspended.png` |

- **Against your item 14.** NT8 in the Fusion VM started at 13:34:51Z (REPORTED, in-VM agent's step log). The old VM's NT8 had closed at 13:30:18Z. So no overlap, by about 4.5 minutes. Both VMs were running at once, though. What the old NT8 did in those 5 and 22 seconds, sign-in or connection, is NOT YET KNOWN.
- **Who started it:** NOT YET KNOWN. Amear said at 14:29Z that Parallels "still works when I log in", though the subscription is cancelled (REPORTED, I-011). So the old VM can still be run today.
- **For your 5.4 evidence:** the original `.pvm` is no longer the 10-11 state. It has two more NT8 starts on its disk, and it holds a crashed, partial suspend, not a shutdown (INFERRED: NT8 writes a dated log file at every start). The cleanly stopped 10-11 state survives only in the cold copy `/Volumes/PVM-Backup/2026-10-11/`.
- Separately, Fusion tried to start an empty early Fusion VM from `~/.Trash` at ~12:48Z (D-070). It is 9.1 MB and holds no Windows (VERIFIED by `du`; "no Windows" INFERRED from the size). Amear cancelled it.

## 5. Other points PRAXIS should know

| Item | State | Label and source |
|---|---|---|
| OneDrive folder backup | **Off** for Desktop, Documents, Pictures. NT8's folder is `C:\Users\amear\Documents\NinjaTrader 8`, not under OneDrive | Off REPORTED (Cowork, 10-13, M-020). Path REPORTED (in-VM agent, `GetFolderPath`, 10-16 and 10-19). Eight older Documents files stayed online-only (M-022); none is NT8's (INFERRED: NT8 was not installed then) |
| BitLocker / device encryption | **On** (Windows' own), recovery key saved by Amear. The VM's encryption password is in his password manager | On REPORTED (10-13). Key REPORTED (D-061). Password REPORTED (D-073). No recovery screen at any reported boot (REPORTED for 10-13; INFERRED since, as no record mentions one). **Current protection status never read: NOT YET KNOWN** |
| Windows build | 25H2, 26200.9457 on 10-13. Today's: NOT YET KNOWN | REPORTED (10-13) |
| Activation | **Not activated** (LicenseStatus 5). Not a gate item | REPORTED (in-VM agent, 10-19, M-007) |
| LOGO! and USB serial | **Deferred.** ARM64 CP210x driver installed; no cable tested | D-074, I-019 |
| Rollback clone | `/Volumes/VMs/Rollback/2026-10-13_pre-tools/` kept ("keep for now") | VERIFIED present, 20:42Z |
| Daylight saving | From **2026-11-01** the Fusion VM is UTC−5, while every old-VM timestamp is fixed UTC−4 | INFERRED (calendar). Matters when comparing old and new logs |

## 6. What's next, and where PRAXIS comes in

1. **A cleanup of the old Parallels VM images is being briefed** (`docs/briefs/2026-10-19-handoff-old-vm-cleanup.md`, VERIFIED present, not yet run). Old VM images are delete candidates. Nothing is deleted until Amear says yes to an exact list. Candidates:
   - `/Volumes/Back Up 2T/Windows 11.pvm` (the original, now in a crashed suspend, §4);
   - `/Volumes/PVM-Backup/2026-09-28/` (re-verified today, 43/43 SHA-256);
   - `/Volumes/PVM-Backup/2026-10-11/` (the cleanly stopped 10-11 state);
   - two older copies on the NUC share, `/Volumes/amear/archive/Windows 11.pvm` (May 2025) and `/Volumes/amear/Back-Up-2T-backup-2026-08-26/Windows 11.pvm`.
   Kept, per the brief: the rescue folders `VM-Rescue-2026-09-29` (with `NinjaTrader 8`, `-full` and `-after-analyzer`) and `VM-Rescue-2026-10-11`, the three transfer discs, and one Fusion VM backup. The brief checks `Praxis.build/docs/reports/` for a reply before deleting.

   **PRAXIS should flag now if it needs anything from the old VM.** Your 5.4 rule treats it as evidence. Once these images are gone, nothing can re-observe Parallels behaviour. That includes the blank chart, the Analyzer click (B3) and the old `UCEERR_RENDERTHREADFAILURE` fault. Items that live only on the old disk:
   - NT8 log rows written after 11:28 EDT on 09-29 (first note, item 1);
   - whatever today's two NT8 starts wrote (INFERRED);
   - Windows event-log entries written after the rescue copies were taken (INFERRED).
2. **A fresh G8 backup** after the next clean Start > Shut down (about 2 minutes). Amear's call.
3. **O2:** create `praxispush`, share only `~/praxis-signals` over SMB, and map it in Windows. Each needs its own step (D-072). Then your items 3, 10 and P1(3).
4. **Still owed inside NT8:** Machine ID, Help > About version, NT8's own time zone (closes M-013), Kinetick EOD, and the 1,857,362 count if the defect allows. Each is a read with Cancel, no change.
5. **Then your items 8 to 12**, with paths under `C:\Users\amear\…`.

**Decisions still Amear's:** whether `NQCONT` is fixed (your `4uu`); activation (M-007); when the rollback clone goes.

## 7. Corrections to update 1

Update 1 stays as written. These points in it are superseded:

1. **§2, the old VM's revision at its last run, "NOT YET KNOWN".** VERIFIED now: 10.0.26200, revision **9457** on 2026-10-11 (old VM `statistic.log`). That is the same as the new VM's 9457. So on 10-13 both VMs ran the same Windows build.
2. **§5 item 14, "the old VM has not run since 2026-10-11".** True when written. Superseded: it ran on 10-15 and 10-19 (§4).
3. **§2, NOT YET KNOWN items now answered:** daylight-saving switch On (REPORTED, 10-13 ~18:05Z); hibernation off (REPORTED, `powercfg /a`, 10-19); NT8's folder is local, as OneDrive backup is off (§5).
4. **§5 items 2 and 3.** Tools is in (§3). Fusion shared folders were tested and do not exist for Windows on Arm (D-065); SMB is the route (D-072).
5. **§2, input "to be re-checked after Tools".** Clicks and single keys work; typed strings still arrive garbled (M-026).
6. **§4, "Still open with Amear":** all three decided. Route (a) (D-068); O2 `praxispush` (D-072); P1 should-pass by way of S2 (D-072).

## 8. Sources

Migration side (`~/Windows-migration`):
- `docs/reports/2026-10-19-go-no-go-evidence.md`, `-walkthrough-log.md`, `-decisions-owed.md`; `2026-10-16-nt8-faithful-restore-prep.md`.
- `DECISION_LOG.md` D-060 to D-076; `ISSUE_REGISTER.md` M-007, M-013, M-019 to M-030, I-011, I-019.
- `06_Validation/nt8-restore-{log,report}-2026-10-19-partial.txt` (in-VM agent text, pasted by Amear).
- `docs/briefs/2026-10-16-in-vm-agent-nt8-faithful-restore.md`, `2026-10-19-*`; `07_Mac-Agent/findings/2026-10-19_*`.
- Read today: the Fusion `vmware.log` (run from 17:51:16Z); the old VM's `statistic.log`, `parallels.log` and file times; `pgrep`, `ls`, `du`, `dscl`.
- `git log --oneline -15` (HEAD `0888f0f`; today's records not yet committed).

PRAXIS side, read only: `docs/reports/2026-09-29-vm-migration-concerns.md` §5.2 to §5.5; `DECISION_LOG.md` 2026-08-29T18:00Z and T19:00Z.

*End of update 2. The migration side dispatched nothing against PRAXIS and changed nothing in Praxis.build except adding this file.*
