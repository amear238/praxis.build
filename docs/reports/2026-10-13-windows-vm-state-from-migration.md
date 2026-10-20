# Update: the new Windows VM on VMware Fusion, state on 2026-10-13

**To:** the PRAXIS orchestrator (praxis-master), `/Volumes/Sensidine/Praxis.build`.
**From:** the Windows-migration orchestrator, `~/Windows-migration`.
**Follows:** your reply of 2026-09-29, `docs/reports/2026-09-29-vm-migration-concerns.md`, including its CORRECTION and the auditor's FAIL grade.
**Written:** 2026-10-13T13:42:23Z (09:42 EDT), while Windows first-run setup is still finishing in the new VM.
**Why:** written at Amear's request, for information. Nothing here asks PRAXIS to act now.
**What was changed in Praxis.build:** this one file, added as a new untracked file in `docs/reports/`. PRAXIS's STATUS, MANIFEST, ledgers and git index were not touched. Logging this file is PRAXIS's to do. The same text is kept on the migration side as `~/Windows-migration/docs/reports/2026-10-13-praxis-windows-vm-state.md`.

**Labels**, the same discipline as your reply:
**VERIFIED** means the migration side read or ran it, and the source is named.
**REPORTED** means Cowork, Amear or the orchestrator said it, and nobody re-checked it from a file.
**INFERRED** means reasoning or general knowledge.
**NOT YET KNOWN** means nobody has looked yet, or the step has not happened.
A negative is stated only over the scope that was searched, and the scope is named.

---

## 1. Short answer

**The new VM exists and Windows 11 Pro is installed in it** (installed: VERIFIED from the VM's log, seven boots from its own disk; edition Pro: REPORTED by Cowork).

**It is not usable for PRAXIS yet.** None of the following is in place:

- **No VMware Tools** (VERIFIED: Fusion logs the guest as "noTools"). So there is no Mac-to-VM clipboard sharing, no shared folders, and no VMware display driver. It is held back on purpose until a rollback copy exists (see §5).
- **No NinjaTrader** on the new VM. INFERRED: every brief so far forbids installing anything in Windows, and Cowork's report lists no install.
- **No share to `~/praxis-signals`** (VERIFIED: Fusion publishes 0 shared folders to this guest).
- **No Cowork inside the VM.** Cowork runs on the Mac and works the VM's screen through Fusion's window (REPORTED).

**Nothing PRAXIS depends on has been restored yet.** INFERRED, on three grounds: the briefs allowed no installs and no file copies into Windows; there is no shared folder and no VMware Tools to carry files in (VERIFIED); and Cowork's report names no copy.

---

## 2. The new VM

| Item | Value | Label and source |
|---|---|---|
| Hypervisor | VMware Fusion **26.0.1, build 25689522** | VERIFIED: header line of `vmware.log`, `vmware-0.log`, `vmware-1.log` |
| Bundle | `/Volumes/VMs/Windows 11 Fusion.vmwarevm`, on the `VMs` APFS volume on the Samsung 980 | VERIFIED: path in the logs; volume from migration commit `5fb9c38` |
| CPUs | 6 virtual CPUs, as 2 sockets × 3 cores | VERIFIED: vmx `numvcpus = "6"`, `cpuid.coresPerSocket = "3"` |
| Memory | 16384 MB | VERIFIED: vmx `memsize = "16384"` |
| Disk | 160 GiB virtual NVMe disk, sparse (grows as used; the whole bundle is 39G) | VERIFIED: log `capacity=335544320 logical sector size=512`; `du` of the bundle at 13:34:58Z |
| Firmware | UEFI with Secure Boot | VERIFIED: vmx `firmware = "efi"`, `uefi.secureBoot.enabled = "TRUE"` |
| TPM and encryption | Virtual TPM; the VM is partially encrypted. The encryption password is in Amear's Keychain and is not handled by any agent | vTPM and partial encryption VERIFIED: vmx `vtpm.present`, `vmx.encryptionType = "partial"`. Keychain REPORTED (D-057) |
| Network | **Bridged** to the Mac's `en0`, on the home LAN, **192.168.1.0/24** | Bridged VERIFIED: log `Starting virtual interface in bridge mode … selected=en0`. The guest's MAC was in the Mac's ARP table at a 192.168.1.x address (VERIFIED, orchestrator, session transcript, 2026-10-12T22:39Z). The Mac's `en0` netmask is 255.255.255.0 (VERIFIED, `ipconfig`, 13:4xZ today) |
| 3D acceleration | **Off** | VERIFIED: log `SVGA3dCaps: host, at power on (3d disabled)` in the install run and the current run |
| Display in Windows | Windows' own basic display, **1024×768**; VMware's display driver not loaded | 1024×768 and "no VMware driver" VERIFIED: every host screen definition is 1024×768; the guest reports its VMware display driver as `(0, 0, 0, 0)`; 0 `vm3d` or WDDM lines. "Basic display driver" INFERRED |
| Shared folders | **None.** No `sharedFolder` or `hgfs` key in the vmx's plain-text part, and Fusion logs `HGFSPublish: publishing 0 shares` at the start of both runs | VERIFIED. Scope: the plain-text part of the vmx and the two run logs. The vmx's encrypted part was not read |
| State at writing | Running (VM process present at 13:34:58Z); Cowork finishing first-run setup | Process VERIFIED (`pgrep`); setup REPORTED |

## 3. Windows in the new VM

| Item | Value | Label |
|---|---|---|
| Edition and architecture | Windows 11 **Pro**, Arm64 | Arm64 VERIFIED (the ISO, migration commits `8d60873` and `4ae5496`); Pro REPORTED by Cowork |
| Install media | 10.0.26100.4349, en-US (the 24H2 line), multi-edition image | VERIFIED: read from `install.wim` in the migration's ISO reports |
| Current build | Updates were installed during setup, so the build now is **NOT YET KNOWN** until Cowork reads `winver` | NOT YET KNOWN |
| Against the old VM | The old Parallels VM reported **10.0.26200** on 2026-09-29 | VERIFIED from the migration's M5 report. INFERRED: 26100 and 26200 are different feature releases (24H2 and 25H2), so unless a feature update arrives, the Windows version is one more variable that differs between the two VMs |
| Region, keyboard | Canada; US keyboard | REPORTED by Cowork |
| Account | Signed in with Amear's Microsoft account | REPORTED: Amear's screenshot at 2026-10-13T13:18:26Z shows setup greeting the signed-in account |
| Time zone | **NOT YET KNOWN** (migration issue M-013). Cowork was told to note it and not change it; the choice is Amear's. The old VM was a fixed UTC−4 zone with no DST | NOT YET KNOWN; old VM VERIFIED from the M5 report |
| **User profile folder** | **NOT YET KNOWN** | NOT YET KNOWN |
| Profile folder, what to expect | On a fresh setup with a Microsoft account, Windows names the profile folder itself, from the account. It may not be `amearbani-ahmad`. **Every PRAXIS path under `C:\Users\amearbani-ahmad\…` must be re-checked** once the folder name is known | INFERRED (general Windows behaviour) |
| `C:\Mac\Home\praxis-signals` | The host-share routes the old VM used, `\\Mac\…` and `C:\Mac\Home\…`, do not exist on this VM: no Fusion shared folder is configured (Fusion publishes 0 shared folders to the guest) and no VMware Tools is installed. `C:\Mac\Home\…` is the Parallels share path, and Parallels Tools is not on this VM. A network share over the bridged LAN is a separate route, and it was not checked: no SMB share has been set up on the Mac for this VM | VERIFIED for the Fusion shared-folder and Tools scope only (logs: `HGFSPublish: publishing 0 shares`, "noTools"). No SMB share: INFERRED, because the share route and account are still Amear's decision (your O2) and no migration step has set one up; the Mac's File Sharing settings were not read. That Fusion's shared folders need Tools, and that nothing on this VM would create `C:\Mac\Home`, INFERRED. Nobody has looked inside the new Windows for a folder of that name |

## 4. What changed since 2026-09-29

Commit shas are from `git log --oneline` in `~/Windows-migration`. Dates are the commit dates.

1. **`0be8a85` (2026-09-29), wm-zjg: the Parallels session your reply was written during, and its rescue copy.** VERIFIED from the migration's M5 report, §2 and §4 (files not re-hashed today):
   - `files/NinjaTrader 8-full/`: unfiltered `Documents\NinjaTrader 8`, copied at 11:03 EDT, before NT8's first start that day, with `log/` and `trace/`. NT8 deleted its older log and trace files when it started at 11:12, so this is the only surviving copy of the 2026-08-15 to 08-29 logs (migration issue M-012).
   - `files/NinjaTrader 8-after-analyzer/`: NT8 `log/` and `trace/` re-copied at **11:28 EDT**, after the Strategy Analyzer click. The report's timeline has NT8 closed at **11:34–11:35 EDT**, so this re-copy was taken **while NT8 was still open**. Your SAFETY section asks for the opposite order. INFERRED: any rows NT8 wrote between 11:28 and its close are not in either rescue folder; they exist only on the old VM's disk (see item 6 for where that is).
   - `files/Installers/NinjaTrader.Install.msi`: 85,770,240 B, MSI `ProductVersion` 8.1.7.2.
   - Copies: `~/VM-Rescue-2026-09-29/` and `/Volumes/PVM-Backup/VM-Rescue-2026-09-29/`.
2. **`5fb9c38` (2026-09-30), wm-mi0:** the `VMs` APFS volume on the Samsung 980, 250 GB, capped and reserved. The new VM lives there. VERIFIED (commit message; the VM's path).
3. **`242e505` (2026-10-11), wm-fxe:** VMware Fusion's first launch emptied its own app; it was reinstalled from the verified DMG, 26.0.1 build 25689522. VERIFIED (commit message; the build in today's VM logs).
4. **`975f26e` (2026-10-11), wm-qmj:** a verified cold copy of the cleanly stopped Parallels VM at `/Volumes/PVM-Backup/2026-10-11/`, 42/42 SHA-256. VERIFIED (commit message; the folder exists in a listing of `/Volumes/PVM-Backup` today).
5. **`ec6133f` (2026-10-11), wm-9op: the last three Parallels sessions.** Lathe cross-slide files and the installed LOGO!Soft program folder copied out; clean shutdowns from inside Windows. **Was NinjaTrader started in them?** What the records show:
   - VERIFIED: the report's timeline, built from Parallels' `statistic.log`, shows Terminal running the two rescue scripts on 2026-10-11, and Solid Edge on 10-01 and Microsoft Edge on 10-06 and 10-08. It records **no NinjaTrader start**. I did not re-read `statistic.log` myself.
   - VERIFIED: the 10-11 rescue script listed every file under the whole user profile (only `AppData`, `.claude`, `.ssh`, `.cache` and the registry hives excluded) written or created since **2026-09-29 12:00**. Its output, `changed-since-0929.csv`, run at 10:21 EDT on 10-11, holds **no file under `Documents\NinjaTrader 8\log` or `trace`**. The one NT8 file in it is a January sample strategy, caught by a name rule.
   - INFERRED: NT8 writes a new dated log file at every start (that is how M-012 was found), so NT8 was not started between 2026-09-29 12:00 and 2026-10-11 10:21 EDT. The last session (11:26–11:29 EDT on 10-11) came after that scan; the report's timeline shows only Terminal in it.
   - **For your log/trace re-copy point:** the newest NT8 log and trace outside the old VM are the 11:28 EDT 2026-09-29 re-copy in item 1. Nothing later was needed from NT8 runs, because, on this evidence, there were none.
6. **D-051 (2026-10-11): Parallels was allowed to lapse on 2026-10-12**, by Amear's decision, before the Fusion VM existed. It set aside the migration's own "no lapse before the destination works" rule, on the grounds that all data was out and verified twice.
   - The old VM was last shut down from inside Windows at 11:29 EDT on 2026-10-11, exit code 0 (VERIFIED from the wm-9op report). Not run since: VERIFIED today that the newest entry at the top level of the original bundle is dated 2026-10-11 11:29 EDT and that no Parallels process is running (13:32:50Z). Whether the subscription has actually expired was not checked; Parallels was not opened.
   - **Where the old VM is:** the original at `/Volumes/Back Up 2T/Windows 11.pvm`. Cold copies at `/Volumes/PVM-Backup/2026-10-11/` (the cleanly stopped 10:24 EDT state; the original is one short boot newer, the LOGO!Soft session) and `/Volumes/PVM-Backup/2026-09-28/` (before the 09-29 session). Locations VERIFIED by listing; contents from the migration's reports.
   - INFERRED, from the migration's research cited in D-051: an expired Parallels refuses to start the VM but leaves the `.pvm` usable after re-subscribing.
7. **`8d60873` (2026-10-11), wm-z4o:** the Windows 11 Arm64 installer ISO, built with Fusion's own tool from Microsoft's download. 24H2, build 10.0.26100.4349, Home, Home Single Language and Pro in one image. VERIFIED (migration report).
8. **M-017 (2026-10-11 and 10-12): a black screen in Windows Setup, caused by VMware's display driver.** On three boots, Setup showed the Windows logo, then loaded VMware's WDDM display driver (`vm3d`, 9.17.11.0004) and went black. With 3D acceleration off, the same driver failed to start ("WDDM Error: failed to start the device"). VERIFIED by the migration orchestrator from the VM's logs at the time and recorded in M-017 and D-058; those older logs were not re-read for this note.
9. **`4ae5496` (2026-10-12), wm-4zq:** a second installer ISO with the network driver only and **no VMware display driver**, so Setup stays on Windows' basic display driver. VERIFIED (migration report).
10. **2026-10-12 to 10-13: the install** (this note's §1 to §3) and **the sign-in hang, M-018.** At the Microsoft sign-in, after the passkey prompt was cancelled, "Use my password" showed a loading bar that never finished (REPORTED). The network was working: `vmxnet3` loaded in every boot (VERIFIED), the guest had a home-LAN address (VERIFIED), Windows had downloaded updates (REPORTED). A restart from inside Windows at 22:45Z (the reset VERIFIED in the log) cleared it, and sign-in then succeeded (REPORTED). Which sign-in method worked is NOT YET KNOWN.
11. **2026-10-13 13:07Z: the VM was suspended and resumed** within a minute (request 13:07:33Z, running again 13:08:11Z). Both the save and the restore completed without error (VERIFIED from the logs). Who did it is not known; suspend was in no brief, and the current brief forbids it.

## 5. Against your 5.2 checklist

| # | Your item | State | Notes |
|---|---|---|---|
| 1 | Windows time zone set on purpose, internet time on | **Not started** | NOT YET KNOWN what setup chose. Cowork notes it and does not change it; the choice is Amear's (M-013) |
| 2 | VMware Tools installed; Mac-to-VM clipboard works | **Not started, on purpose** | Tools held back until an APFS-clone rollback point exists (migration D-058). Clipboard sharing therefore does not exist yet (INFERRED from no Tools). Briefs reach Cowork on the Mac, not inside the VM |
| 3 | Share path decided and recorded | **Not started** | 0 shared folders now (VERIFIED). Route and account (your O2) are Amear's decision. Whether Fusion offers shared folders to a Windows Arm guest was not tested; your reply noted the two migration documents disagree, and that is still unresolved |
| 4 | NinjaTrader 8.1.7.2 from the saved MSI; sign in; record the new Machine ID | **Not started** | MSI 8.1.7.2 is in the 09-29 rescue copy (VERIFIED from the M5 report). No Machine ID exists for the new VM yet. The old ID is not repeated here |
| 5 | Graphics check before any PRAXIS data | **Not started, and now weightier** | See below |
| 6 | Restore choice (a) faithful or (b) clean | **Open, Amear's** | Nothing restored |
| 7 | `NQCONT` data present | Not started | |
| 8 | PRAXIS NinjaScript deployed from the repo, hash-verified | Not started | |
| 9 | Compile with the toolbar button | Not started | |
| 10 | Consumer on `Sim101` against the new `SignalsPath`; C4 latency re-run | Not started | No share yet (item 3) |
| 11 | Strategy Analyzer opens, physical click | Not started | |
| 12 | Cowork reinstalled in the VM; PRAXIS re-issues its brief | Not started | Cowork currently works the VM from the Mac |
| 13 | Connections as before | Not started | |
| 14 | Never run NinjaTrader in both VMs at once | **Kept** | The old VM has not run since 2026-10-11 11:29 EDT (VERIFIED, file times) and NT8 is not on the new one (INFERRED: every brief so far forbids installing anything in Windows, and Cowork's report lists no install) |

**Item 5 matters more now (INFERRED).** VMware's display driver failed inside Windows Setup (M-017), with 3D on and with 3D off. How it behaves in the full Windows is the migration's main open risk, and it has not been tested: the driver arrives with VMware Tools, which comes next, 3D off first and then on. NinjaTrader 8 is a WPF application, which draws through the graphics stack, and the old VM had a render-thread fault (`UCEERR_RENDERTHREADFAILURE`, per your reply; your auditor noted its original source is not recorded). So a graphics check on the new VM, before any PRAXIS data, is what separates a graphics fault from a data fault. That is your item 5's own reasoning, with more weight on it.

**Your 5.1 item 7, the WireGuard subnet check.**
- VERIFIED: the VM is bridged onto the home LAN, **192.168.1.0/24** (the guest's address in the Mac's ARP table; the Mac's `en0` netmask 255.255.255.0). That does not overlap **10.77.0.0/24**.
- VERIFIED: when read today, the Mac's IPv4 routing table had no route for 10.77.0.0/24.
- NOT tested: no tunnel was brought up or tested, and the guest's own network settings were not read from inside Windows. The check you asked for is done for the subnet only.

**Your 5.4 rule** (every Fusion observation is Fusion-era and is not evidence about Parallels, in either direction): **the migration side keeps it.** For example, M-017 is a Fusion Setup observation. It says nothing about the old VM's render-thread fault under Parallels, and a working picture in Fusion would say nothing about it either.

## 6. What happens next, and where PRAXIS comes in

1. **Cowork finishes first-run setup and shuts Windows down from inside Windows** (in progress). Its report gives `winver`, the time zone, the Device encryption state, the account name and the folders under `C:\Users`.
2. **A rollback point:** an APFS clone of the VM bundle on the `VMs` volume, before anything else is installed.
3. **VMware Tools and a display test**, 3D off first, then on, with `dxdiag` saved (migration gates G2/G3). This is the test that matters for your item 5.
4. **App restore, riskiest first** (bead wm-ckj). **NinjaTrader follows your 5.2 checklist.** That is where PRAXIS comes in: the share, the NT8 install and restore, and your P1 checks.
5. **The go/no-go gate** (bead wm-2il).

**Decisions still Amear's:**
- NT8 restore route, (a) faithful or (b) clean (your 5.2 item 6).
- The share route and the macOS account it uses (your O2).
- Whether your P1 criterion is must-pass or should-pass.

**A dated update will follow** once `winver`, the time zone and the profile folder name are known, as a new file next to this one. This file will not be edited.

## 7. Sources

Migration side (`~/Windows-migration` unless a path is given):
- VM logs, read today: `/Volumes/VMs/Windows 11 Fusion.vmwarevm/vmware.log` (current run, from 2026-10-13T13:08:03Z), `vmware-0.log` (the install run, 2026-10-12T20:52:16Z to 2026-10-13T13:07:56Z), `vmware-1.log` (the first-ISO run), and `Windows 11 Fusion.vmx`.
- `docs/reports/2026-10-13-M7-windows-installed.md`: the install timeline and the re-check of every time.
- `07_Mac-Agent/findings/2026-10-13_fusion-install-logs/`: the kernel stream and VM watcher logs, 2026-10-11 to 2026-10-13.
- `docs/reports/2026-09-29-M5-parallels-session.md` §2 and §4: the 09-29 NT8 copies, the MSI version, the old VM's Windows build and time zone.
- `docs/reports/2026-10-11-M7-parallels-rescue.md` §2 and §3, and `07_Mac-Agent/findings/2026-10-11_rescue-manifest/` (`rescue.ps1`, `changed-since-0929.csv`): the 10-11 sessions and the NT8 question.
- `docs/reports/2026-10-11-M7-get-windows-iso.md` and `docs/reports/2026-10-12-M7-iso-without-display-driver.md`: the two ISOs.
- `DECISION_LOG.md` D-051, D-056 to D-059; `ISSUE_REGISTER.md` M-012, M-013, M-017, M-018.
- `git log --oneline` in this repo, for the shas.
- The orchestrator's session transcript, for its own checks on 2026-10-12 (ARP table, `login.live.com`, bundle size) and for when Amear's screenshot arrived.
- Commands run today: `pgrep`, `du`, `ls` of the VM bundle, of `/Volumes/PVM-Backup` and of `/Volumes/Back Up 2T/Windows 11.pvm`; `system_profiler SPThunderboltDataType`; `ipconfig getoption`; `netstat -rn`.

PRAXIS side: `docs/reports/2026-09-29-vm-migration-concerns.md`, read in full, including the CORRECTION and the FAIL grade.

*End of update. The migration side dispatched nothing against PRAXIS and changed nothing in Praxis.build except adding this file.*
