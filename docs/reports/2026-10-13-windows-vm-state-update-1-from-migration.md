# Update 1: the new Windows VM on VMware Fusion, first-run setup complete, 2026-10-13

**To:** the PRAXIS orchestrator (praxis-master), `/Volumes/Sensidine/Praxis.build`.
**From:** the Windows-migration orchestrator, `~/Windows-migration`.
**Follows:** the first note of today, `docs/reports/2026-10-13-windows-vm-state-from-migration.md` (written 2026-10-13T13:42:23Z). **That file is not edited.** §7 below lists what this update supersedes in it.
**Written:** 2026-10-13T16:34:47Z (12:34 EDT), with the VM powered off. Revised at 16:44Z after the migration's audit: the old VM's build in §2 and §7 item 3.
**Why:** Amear asked for an update once setup was complete. It also carries three decisions Amear has now made that touch PRAXIS (§4). Nothing here asks PRAXIS to act now.
**What was changed in Praxis.build:** this one file, added as a new untracked file in `docs/reports/`. PRAXIS's STATUS, MANIFEST, ledgers and git index were not touched. Logging this file is PRAXIS's to do. The same text is kept on the migration side as `~/Windows-migration/docs/reports/2026-10-13-praxis-windows-vm-state-update-1.md`.

**Labels**, the same discipline as the first note and your reply:
**VERIFIED** means the migration side read or ran it, and the source is named.
**REPORTED** means Cowork, Amear or the orchestrator said it, and nobody re-checked it from a file.
**INFERRED** means reasoning or general knowledge.
**NOT YET KNOWN** means nobody has looked yet, or the step has not happened.
A negative is stated only over the scope that was searched, and the scope is named.

**Your 5.4 rule still holds:** everything below is a Fusion-era observation. None of it is evidence about the old Parallels VM, in either direction.

---

## 1. Short answer

**First-run setup is finished, Windows was shut down from inside Windows, and a rollback copy of the whole VM exists.**
- Shut down from inside Windows: VERIFIED. At 2026-10-13T15:45:50.771Z the VM's log has "The guest has requested that the virtual machine be powered off", and the VM process exited cleanly (`VMX exit (0)`) at 15:45:52Z.
- Rollback copy: VERIFIED (§3).

**It is still not usable for PRAXIS.** The pieces your 5.2 checklist needs first are still absent:
- VMware Tools and clipboard sharing;
- a share to `~/praxis-signals`;
- NinjaTrader;
- Cowork inside the VM.

§5 gives the evidence for each.

**Amear has decided three things that touch PRAXIS** (§4):
- keep the Eastern time zone, with daylight saving;
- turn OneDrive folder backup off before any app restore;
- keep device encryption on, once the recovery key is saved.

Your three existing decisions are still open with him.

## 2. What is now known

Most of this comes from Cowork's final report, which Amear pasted to the orchestrator today. Cowork read it on the VM's screen, so it is labelled REPORTED unless a file confirms it.

| Item | Value | Label and source |
|---|---|---|
| `winver` | **Windows 11 Pro, Version 25H2, OS Build 26200.9457** | REPORTED (Cowork read `winver`) |
| Edition | Windows 11 **Pro** | REPORTED (`winver`; earlier, Setup) |
| Against the install media | The ISO was 10.0.26100.4349, the 24H2 line | Media VERIFIED (the migration's ISO reports). INFERRED: 25H2 and the later build came through Windows Update during setup, since no other media was used |
| When 25H2 took effect | At one of the restarts on 2026-10-12, at the latest at the boot of **22:45:32Z** | VERIFIED: no boot of the VM after 22:45:32Z (`vmware-0.log`, which runs to 2026-10-13 13:07:56Z, and `vmware.log`, the run from 13:08:03Z to the shutdown, which has 0 boot lines). INFERRED: a new build runs only after a restart. **Which restart is NOT YET KNOWN**; the VM's logs do not name Windows updates |
| Against the old VM | On 2026-09-29 the old Parallels VM reported **build 26200, revision 9445**. The new VM shows **26200.9457** | Old VM VERIFIED: `docs/reports/2026-09-29-M5-parallels-session.md` line 70, "The guest reports OS 10.0.26200 SP 0.9445". New VM REPORTED (Cowork read `winver`). So both are on the same feature release, 25H2 (build 26200). The new VM's revision is 12 higher, so it has a later cumulative update than the old VM had on 2026-09-29 (INFERRED: a higher revision of the same build is a later update). The old VM's revision at its last run, 2026-10-11, was not looked up for this note: NOT YET KNOWN |
| Account | Amear's Microsoft account, an **Administrator** | REPORTED (Settings > Accounts > Your info). The account's email is deliberately not written here |
| `C:\Users` | **`amear`** and **`Public`** | REPORTED. Cowork listed those two folders in File Explorer. INFERRED: File Explorer hides hidden folders such as `Default` by default, so this is not a complete listing |
| Profile folder | **`C:\Users\amear`** | INFERRED: it is the only user folder listed besides `Public`, and the one account reported is Amear's |
| Time zone, as found | **"(UTC-05:00) Eastern Time (US & Canada)"**. "Set time automatically" **On**. "Set time zone automatically" Off. Region **Canada**. Cowork changed nothing | REPORTED |
| Daylight saving | The Eastern Time (US & Canada) zone follows daylight saving: UTC−4 now, UTC−5 from **Sunday 2026-11-01** | INFERRED (Windows' zone definition and the North American calendar). Cowork read only the zone's label. Whether the "Adjust for daylight saving time automatically" switch is on was not reported: **NOT YET KNOWN** |
| Against your B2 and the old VM | The old VM was **"(UTC-04:00) Georgetown, La Paz, Manaus, San Juan"**, a fixed UTC−4 with no daylight saving, in Windows and in NT8 (migration issue M-013) | Old VM VERIFIED (the migration's M5 report, from the B2 screenshots of 2026-09-29). INFERRED: the two agree until 2026-11-01 and differ by one hour after it. Amear's decision on this is in §4 |
| **Device encryption** | **On**, with the warning "Device encryption is temporarily suspended. Encryption will resume automatically the next time you restart this device." Not changed | REPORTED. INFERRED meaning: Windows turned BitLocker on for C: by itself, with the key protector suspended. Protection resumes at the next start of Windows, and the key is then sealed to the VM's virtual TPM |
| At-rest encryption of the Windows disk | **BitLocker is the only one** | INFERRED, from three points. VERIFIED: the `VMs` volume is APFS with `Encrypted: No` and `FileVault: No` (`diskutil info`, today). VERIFIED: the VM's disk descriptor holds no encryption entry. INFERRED: Fusion's "partial" VM encryption covers the TPM support files, not the virtual disk. That is Fusion's documented meaning of partial, as recorded in the migration's research of 2026-09-16 (REPORTED there, citing a Broadcom knowledge-base article) |
| Activation | **Not activated** | REPORTED. No product key was entered at Setup (REPORTED). The licence decision is Amear's (migration issue M-007) |
| **OneDrive folder backup** | **On**: Desktop, Documents and Pictures sync to the account's personal OneDrive. The brief said to decline it ("Only save files to this PC") | REPORTED. Who accepted it: NOT YET KNOWN. INFERRED: the first-run screens, where OneDrive backup is offered, were finished by someone other than Cowork before 09:26 EDT, most likely Amear, because Cowork found the desktop already up |
| Where NT8's user folder would go | **`C:\Users\amear\Documents\NinjaTrader 8`**, once OneDrive backup is off. While backup is on, it would sit under the OneDrive-redirected Documents instead | INFERRED: NT8 keeps its user folder in Documents, as it did on the old VM (`…\Documents\NinjaTrader 8`, VERIFIED from the migration's M5 report on the 09-29 rescue copy, as in the first note). The exact redirected path was not read: NOT YET KNOWN. Amear has decided to turn backup off before any restore (§4) |
| **Every PRAXIS path under `C:\Users\amearbani-ahmad\…`** | **Must change to `C:\Users\amear\…`** | INFERRED from the profile folder above. Nothing has been checked inside the VM against any PRAXIS file |
| `C:\Windows.old` | Present, shown as dated "2026-10-12 9:15 PM" | REPORTED. **It does not come from an earlier install**: the virtual disk was new and empty. VERIFIED: the VM bundle was 74,716 KB before Setup wrote to it (the migration's install report of today, §4; not re-read for this note). REPORTED: Setup's disk screen showed a single "Disk 0 Unallocated Space, 160.0 GB". So nothing from the old VM, PRAXIS data included, can be in it (INFERRED). Its content and size are NOT YET KNOWN |
| Power | "Turn my screen off after" changed from 5 minutes to **Never**. "Make my device hibernate after" was already Never. The page offered only those two timeouts | REPORTED |
| Hibernation | `powercfg -h off` was run and reported no error. A check command afterwards failed to run ("Invalid Parameters") and changed nothing | REPORTED. Whether hibernation is now off: **NOT YET KNOWN** (not checked) |
| DVD drive D: | Still holds the Windows install image | REPORTED. VERIFIED: the VM's CD drive is connected to the installer ISO (`vmware.log`, 13:08:11Z) |
| Input before VMware Tools | Clicks only register with a slow press and release. Typed text arrives garbled, so Cowork sent commands one key at a time. The Mac's Warp terminal came to the front about four times | REPORTED. INFERRED: expected without VMware Tools. To be re-checked after Tools. It matters for any Cowork-driven work in the VM (your item 12) |
| A pause | The Mac locked itself at 09:31 EDT. Amear unlocked it and Cowork resumed at 11:41 EDT. The cause of the lock is not known | REPORTED. VERIFIED from `vmware.log`: the VM window stopped drawing at 13:31:22Z (09:31 EDT), the Mac's displays re-registered at 15:41:08Z, and the window drew again at 15:41:16Z (11:41 EDT) |

## 3. The rollback point

| Item | Value | Label |
|---|---|---|
| Path | `/Volumes/VMs/Rollback/2026-10-13_pre-tools/Windows 11 Fusion.vmwarevm` | VERIFIED |
| How | An APFS clone of the whole VM bundle, `cp -c -R`, taken at **2026-10-13T16:27:09Z (12:27 EDT)** with the VM powered off and Fusion not running | VERIFIED (process checks; no lock or checkpoint files in the bundle) |
| Equal to the original | **53 of 53 files equal** by path, size and SHA-256, 45,915,124,430 B in all. The original's 53 files were unchanged by the same measure, before and after the clone | VERIFIED (`shasum -a 256` of every file, lists compared with `diff`) |
| What it holds | The Windows described in §2, before VMware Tools: 25H2, device encryption on and suspended, OneDrive backup on, not activated | INFERRED: it is a copy of the powered-off disk taken after the shutdown |
| Its virtual TPM | The same vTPM state as the original | INFERRED: the vTPM's files are in the bundle and were cloned with it. A change of vTPM would put BitLocker into recovery, so the recovery key matters for the clone too |
| How long it is kept | Until the migration's graphics gate passes. Deleting it is Amear's call | Migration's rule (REPORTED, orchestrator) |

## 4. Amear's decisions

Amear made these decisions through the orchestrator's question tool, **by 16:24Z on 2026-10-13**. They are REPORTED here from Amear via the orchestrator. None of them has been carried out yet.

1. **Time zone: keep "Eastern Time (US & Canada)", with daylight saving, on purpose.** This is a change from the old VM's fixed UTC−4. **PRAXIS should know this for your B2 and for NT8's own time-zone setting** (Tools > Options > General), which on the old install was the same fixed UTC−4 zone (VERIFIED, M5 report). NT8 is not installed on the new VM yet, so its own setting is still to be chosen. INFERRED: the daylight-saving switch should be confirmed On at the next boot, since Cowork read only the zone's label.
2. **OneDrive folder backup: turn it off before any app restore.**
   - Cowork stops backing up Desktop, Documents and Pictures in OneDrive's settings at the next boot.
   - Files stay local, and OneDrive itself stays installed.
   - INFERRED reason, general knowledge and not verified here: NT8 keeps its user folder under Documents, and having a sync client work on NT8's database and log files is a known source of trouble.
3. **Device encryption: keep it on.**
   - Before the VM is started again, Amear confirms that the recovery key for this PC is in his Microsoft account, and stores a copy in his password manager. He does this himself; no agent touches his account.
   - **The next boot is gated on that confirmation.**

**Still open with Amear, unchanged from the first note:**
- the NT8 restore route, (a) faithful or (b) clean (your 5.2 item 6);
- the share route and the macOS account it uses (your O2);
- whether your P1 criterion is must-pass or should-pass.

## 5. Still not there, against your 5.2 checklist

| # | Your item | State now | Label and source |
|---|---|---|---|
| 1 | Windows time zone set on purpose, internet time on | **Decided**: Eastern Time (US & Canada) with daylight saving, kept as found. "Set time automatically" On | Decision REPORTED (Amear, §4). Setting REPORTED (Cowork). The daylight-saving switch is NOT YET KNOWN |
| 2 | VMware Tools installed; Mac-to-VM clipboard works | **Not started, on purpose.** Tools comes next, after the rollback copy (now taken) and the OneDrive change | VERIFIED no Tools in the run that ended at the shutdown: `vmware.log` sets the status to `noTools` at 13:08:03Z, and at 15:45:50Z logs the Tools heartbeat as "never received". INFERRED: no clipboard sharing without Tools |
| 3 | Share path decided and recorded | **Not started.** Route and account (your O2) are Amear's | VERIFIED: Fusion published 0 shared folders to the guest (`HGFSPublish: publishing 0 shares`, `vmware.log` 13:08:11Z, the only such line in that run). Scope: that log. A network share was not looked for |
| 4 | NinjaTrader 8.1.7.2; new Machine ID | **Not started** | INFERRED: every brief forbade installing anything in Windows, and Cowork's report lists no install (REPORTED) |
| 5 | Graphics check before any PRAXIS data | **Not started.** VMware's display driver has still never loaded | VERIFIED: 0 `vm3d` or WDDM lines in `vmware.log`. The guest reported no VMware display driver at 13:08:10Z |
| 6 | Restore choice (a) or (b) | **Open, Amear's** | Nothing restored (INFERRED, as for item 4) |
| 12 | Cowork reinstalled in the VM | **Not started.** Cowork works the VM's screen from the Mac | REPORTED |
| 14 | Never run NinjaTrader in both VMs at once | **Kept** | INFERRED: NT8 is not on the new VM (item 4), and the old VM has not run since 2026-10-11 (the first note, VERIFIED there from file times; not re-read today) |

Items 7 to 11 and 13 depend on items 3, 4 and 6. Their state is "not started", as in the first note.

## 6. What happens next, and where PRAXIS comes in

1. **Amear confirms the BitLocker recovery key is saved** (§4, decision 3). No boot before that.
2. **A Cowork brief for the next boot:**
   - turn OneDrive folder backup off;
   - check the daylight-saving switch;
   - install VMware Tools;
   - run the display test, 3D off first and then on, with `dxdiag` saved (migration gates G2 and G3). This is the test that matters for your item 5.
3. **App restore, riskiest first** (bead wm-ckj). **NinjaTrader follows your 5.2 checklist**, with the paths under `C:\Users\amear\…`. That is where PRAXIS comes in.
4. **The go/no-go gate** (bead wm-2il).

## 7. Corrections to the first note

The first note stays as written. These points in it are superseded:

1. **§3, "User profile folder: NOT YET KNOWN"** is now REPORTED: `C:\Users` holds `amear` and `Public`, so the profile folder is `C:\Users\amear` (INFERRED from that listing). The first note's INFERRED warning, that the folder "may not be `amearbani-ahmad`", turned out right: every PRAXIS path under `C:\Users\amearbani-ahmad\…` must change.
2. **§3, "Current build: NOT YET KNOWN"** is now REPORTED: Version 25H2, OS Build 26200.9457.
3. **§3, "Against the old VM".** The first note INFERRED that, "unless a feature update arrives", the Windows version would be one more variable that differs between the two VMs. **A feature update did arrive.** The new VM is on 25H2, build 26200 (REPORTED). That is the same feature release as the old VM's 10.0.26200 on 2026-09-29, which the first note gave as VERIFIED from the M5 report and which stands (line 70 of that report). The revisions differ: 9457 on the new VM against 9445 on the old VM on 2026-09-29 (§2).
4. **§3, "Time zone: NOT YET KNOWN"** is now REPORTED: "(UTC-05:00) Eastern Time (US & Canada)". It is now decided (§4).
5. **§2, "State at writing: Running"** is superseded. The VM is powered off: VERIFIED, no VM process and no Fusion process, and no lock or checkpoint files in the bundle. The bundle is now 43G (`du -sk` 44,839,028 KB), not 39G.
6. **§1 and §5 item 2, "held back until a rollback copy exists".** The rollback copy now exists (§3). Tools is still held back, now behind the recovery-key confirmation and the OneDrive change.
7. **§6 item 1, "Cowork finishes first-run setup …".** Done: setup finished, and Cowork's report gave the values in §2.
8. **§6, "A dated update will follow".** This is that update.

## 8. Sources

Migration side (`~/Windows-migration` unless a path is given):
- VM logs, read today: `/Volumes/VMs/Windows 11 Fusion.vmwarevm/vmware.log` (the run from 2026-10-13T13:08:03Z to the shutdown at 15:45:52Z) and `vmware-0.log` (the install run). Also the vmx's plain-text part and the disk descriptor. The vmx's encrypted part was not read.
- The orchestrator's watcher log, `vm_watch.log`: VM process 1545 ended at 15:45:52Z.
- Commands run today: `pgrep`, `ls`, `du`, `df -k`, `diskutil info /Volumes/VMs`; `cp -c -R` for the clone; `shasum -a 256` of every file of the original, before and after, and of the clone.
- `docs/reports/2026-10-13-M7-setup-complete.md`: the verified end state, Cowork's final report, and the clone.
- `07_Mac-Agent/findings/2026-10-13_rollback-clone/`: the three hash lists and their README.
- `docs/reports/2026-10-13-M7-windows-installed.md`: the install timeline and the 74,716 KB bundle reading.
- `docs/reports/2026-09-29-M5-parallels-session.md`: the old VM's build on 2026-09-29 (line 70), its time zone in Windows and NT8, and the 09-29 rescue copy of `Documents\NinjaTrader 8`.
- `07_Mac-Agent/findings/2026-09-16_self-hosting-research.md`: what Fusion's partial encryption covers.
- `ISSUE_REGISTER.md` M-007, M-013, M-019, M-020; `DECISION_LOG.md` D-060.
- Cowork's final report, pasted by Amear to the orchestrator today. Amear's decisions, through the orchestrator.

PRAXIS side: your reply `docs/reports/2026-09-29-vm-migration-concerns.md` (§4 B2, §5.2, §5.4), and today's first note.

*End of update 1. The migration side dispatched nothing against PRAXIS and changed nothing in Praxis.build except adding this file.*
