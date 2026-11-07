Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
# Fusion shared folders (Mac ↔ Win 11 ARM VM): hand step for Amear
Per R-VN4-14 (DECISION_LOG row "2026-11-05T23:51:21Z WHO: amear"), asked in row "2026-11-05T23:50:09Z WHO: amear". No agent touches the VM.

**READ FIRST.** VMware: *"Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts."* (OBSERVED). Tools 13.0.5 notes list no `vmhgfs.sys` for Windows Arm (OBSERVED; sharing driver INFERRED); the VM runs 13.1.5, not checked.

## Questions (NEEDS AMEAR)
0. **Conflict.** You asked for "file sharing between the Mac and the VM" (R-VN4-14) and this Fusion walkthrough (23:50:09Z, e). VMware and our 10-19 VM report ("no shared folders for Windows on Arm") say unsupported. It records an SMB route as yours: D-072, a low-privilege user `praxispush` seeing only `~/praxis-signals` (REPORTED; migration ledger, not this repo; user not created). Try these steps / D-072 SMB / keep Google Drive `praxis-tickprep`? Your call; nothing chosen.
1. **Snapshot first?** R-VN4-13 ("just do the snapshot") was NT8 add-ons, not this.
2. **Read & Write** (VM can change/add/delete Mac files) or **Read Only** (VM reads only)?
3. **Which folder?** E.g. the whole repo `/Volumes/Sensidine/Praxis.build`, or `~/praxis-signals` (D-072). Repo + Read & Write: VM can change any repo file. No default.

## Steps (Mac, VM on; needs VMware Tools; 13.1.5 per 10-19 report, REPORTED)
Labels quote pages filed under "Sharing Files Between Windows and Your Intel-based Mac" (OBSERVED; fit to Apple silicon INFERRED).
1. **Window > Virtual Machine Library**, select VM, **Settings**. You should see: its Settings window.
2. Under **Systems Settings** click **Sharing**. You should see: **Enable Shared Folders** box.
3. Tick it. You should see: ticked; if supported, a **VMware Shared Folders** shortcut in Windows.
4. **add (+)**, pick the folder you chose (question 3), **Add**. You should see: it listed.
5. **Permissions**: your answer to question 2. You should see: it on the folder.
6. **Open in Guest**. You should see: the folder in Windows. If not, stop; tell the master.
Caution (VMware): never open one file from both sides at once; a write can corrupt it.

## End check
`touch "<folder>/share-test-mac.txt"` on the Mac. You should see: it in the Windows shortcut. Delete it on the Mac.

## Go-live (R-VN4-14)
- [ ] before real money: isolate the VM — remove the shared folder (**remove (-)**, 13-0, OBSERVED), untick Enable (INFERRED); also check mirrored folders are off (13-0 enable page: "also enables mirrored folders", OBSERVED).

## Sources (2026-11-05; quotes and curl output pasted in docs/reports/2026-11-05-fusion-shared-folders-walkthrough-manager.md)
- techdocs.broadcom.com …/fusion-pro/<ver>/…/sharing-files-between-windows-and-your-mac/ pages (26H1: overview, guest-OS, add; 13-0: guest-OS, remove, enable), OBSERVED; Tools 13.0.5 release notes (OBSERVED)
- docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md rows 2-3 (REPORTED)

## Addendum 2026-11-06 (ruling 5 / item 1; appended, nothing above edited)
- **Questions 0–3: closed.** SMB was chosen and set up by Amear's hand (REPORTED BY amear, D-2026-11-06-A item 3: Mac File Sharing on, `Praxis.build` shared, the VM maps it as `Z:`). Closure is the master's settlement under R-1104-2 after ruling 5 delegated the item (D-2026-11-06-B; DECISION_LOG 2026-11-06T20:08:28Z, WHO: amear).
- [ ] **Go-live checklist, his words:** "unmap Z: and turn the share off before real money" (D-2026-11-06-A item 3).
- **The Steps above are moot:** Fusion shows no Sharing pane (D-2026-11-06-A item 3, "no Sharing pane, as flagged", REPORTED BY amear).
- Source: D-2026-11-06-B, ruling 5 settlements table, item 1 and item 10.
- [ ] **Go-live checklist addendum 2026-11-07, his words (ruling 10):** "remove the unauthenticated bridge request folders (or add auth) before real money" (verbatim at `docs/reports/2026-11-07-amear-rulings-morning.md`:29; ledger DECISION_LOG 2026-11-07T12:55:00Z, WHO: amear; D-2026-11-07-A). His second item, "unmap Z: and turn off the SMB share", is already covered at :35; not duplicated.
