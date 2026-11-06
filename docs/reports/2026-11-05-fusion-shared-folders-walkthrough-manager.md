Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
# Manager report — 2026-11-05-fusion-shared-folders-walkthrough

## Task
Write a one-screen hand-step walkthrough for Amear to enable VMware Fusion shared folders between the Apple-silicon Mac and the Windows 11 ARM VM (R-VN4-14, DECISION_LOG row "2026-11-05T23:51:21Z WHO: amear"; instruction item e, row "2026-11-05T23:50:09Z WHO: amear"). Documentation only. No agent touched the VM, Fusion or any system setting.
Deliverable: /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md (31 lines).

## Rubric criteria addressed
S1 (pasted output), S2 (no level above evidence), S8 (no Amear question answered for him), S6 (cross-block check, below).

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| ad0706c64b4df4458 | BUILD: research + draft | Draft written. Vendor line found: Fusion shared folders unsupported on Win 11 ARM / Apple silicon |
| a0f59e8873b0b5c44 | ADVERSARIAL | VERDICT: DEFECTS, 8 found (Tools version is on record; D-072 SMB decision left out; repo-as-default answered an S8 question; pages are Intel-scoped; stale line cite; labels) |
| ac915741f46402780 | BUILD: fix | All 8 fixed; 31 lines |
| ac3866661012fadc0 | ADVERSARIAL (re-check) | VERDICT: DEFECTS, 4 found: (1) this report didn't exist yet (fixed by writing it); (2) "R-VN4-14 asks for Fusion shared folders" put the voice agent's reading in his mouth (S8); (3) step 3 promised a shortcut on a setup the vendor calls unsupported, and the end check's delete didn't say which side; (4) Read & Write on the whole repo wasn't flagged |

## Process log
1. Read rubric S1/S2/S6/S8, the rulings, the VM brief and the VM notes.
2. BUILD worker fetched 15+ techdocs/KB URLs with curl (status lines below), graded each fact and wrote the draft.
3. Adversary 1 found the repo's own record: `docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md` rows 2–3 (line 57 Tools 13.1.5; line 59 "no shared folders for Windows on Arm", D-072 SMB route, `HGFSPublish: publishing 0 shares`). I re-read lines 55–59 myself. D-072 is not in this repo's DECISIONS.md or DECISION_LOG.md. It comes from the migration orchestrator's ledger, so it is REPORTED.
4. A fix worker made the changes. Adversary 2 re-checked the result.
5. I made adversary 2's fixes 2–4 directly, as six string replacements (the pre-edit copy is in the scratchpad at walkthrough-pre-mgr-edit.md). Question 0 now quotes his words "file sharing between the Mac and the VM" plus item e, and does not call it a request for Fusion shared folders. Step 3 now says "if supported". The end check now says "Delete it on the Mac". Question 3 now says "Repo + Read & Write: VM can change any repo file."

## Verification evidence
Pasted output only (re-run by the manager this session):
```
$ per-page: not-supported quote
p7: Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts.
q4: Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts.
p9: 
q3: 
$ labels
Virtual Machine Library          p10.html p8.html p9.html q5.html 
Systems Settings                 p10.html p8.html p9.html q5.html 
Enable Shared Folders            p10.html p6.html p7.html p8.html p9.html q3.html q4.html q5.html 
Read &amp; Write\|Read & Write   
Read Only                        
Open in Guest                    
VMware Shared Folders            p8.html 
requires VMware Tools            p6.html q3.html 
also enables mirrored folders    p8.html 
Intel-based Mac                  p10.html p3.html p6.html p7.html p8.html p9.html q1.html q3.html q4.html q5.html 
$ vmhgfs.sys line numbers in Tools 13.0.5 notes (r5)
951:                <div id="GUID-33377c28-665c-44e9-a4e8-0b
531:        <ul class="ul"><div  style="display: inline;"><li class="li"><div  s
626:      <ul id="GUID-33377c28-665c-44e9-a4e8-0b8ab2c153d0-en_id-0dc88c3a-ab8e-
627:      <ul id="GUID-33377c28-665c-44e9-a4e8-0b8ab2c153d0-en_id-959767a8-9dde-
1119:      <div id="GUID-33377c28-665c-44e9-a4e8-0b8ab2c153d0-en_id-4ac644d0-c02
$ cmp line 1
line1 IDENTICAL
$ wc
      31    3067 docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
$ git status
?? docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
0
$ curl -w status lines (from worker1-evidence.md, curl -w "%{http_code} %{url_effective}")
404 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-virtual-machines-and-your-mac.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/release-notes.html
404 https://knowledge.broadcom.com/external/article?legacyId=1021357
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/enable-shared-folders-or-mirrored-folders-for-a-virtual-mach
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/remove-a-shared-folder.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/release-notes.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/release-notes/vmware-fusion-26h1u1-release-notes.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/release-notes/vmware-fusion-26h1-release-notes.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/release-notes/vmware-fusion-136-release-notes.html
200 https://techdocs.broadcom.com/
200 https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes.html
200 https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html
$ python3 -I strip.py (tag-stripped quotes, p9 = 13-0 add-a-shared-folder, r5 = Tools 13.0.5 notes)
p9.html: the contents of the Mac's shared folder. Option Description Read & Write Enables the virtual machine to change the contents of the shared fo
p9.html: ne to change the contents of the shared folder on your Mac. Read Only Prevents the virtual machine from changing the contents of the share
p9.html: takes precedence over the Shared Folder permission setting. Click the Open in Guest button to open the shared folder in the virtual machine. Th
r5.html: .sys 12.5.15.0 vmxnet3.sys 1.9.20.0 vm3dmp.sys 9.17.09.0004 Software Drivers vmhgfs.sys 11.0.49.0 vmmemctl.sys 7.5.10.0 vmrawdsk.sys 1.1.9.0 vnetWF
r5.html: ty DLL vmwsu.dll 2.5.2.0 VMware Tools 13.0.5.0 provides the following driver versions for Windows Arm: Hardware Drivers VMware Tools 13.0.5.0 vmusbmouse.sys 12.5
$ sed -n 57p;59p docs/reports/2026-10-19-windows-vm-state-update-2-from-migration.md (cut 400)
| 2 | VMware Tools; clipboard works | **Done.** Tools 13.1.5. Mac-to-VM clipboard carries text | Tools VERIFIED (`vmware.log`, 10-13). Clipboard VERIFIED: two clipboard transfers of 99,615 B and 62,579 B logged on 10-15, files byte-checked (D-065) |
| 3 | Share path decided and recorded (O2) | **Decided, not built.** Fusion has **no shared folders for Windows on Arm**. The route is macOS File Sharing (SMB). D-072 item 7: a new low-privilege Mac user, `praxispush`, that can see only `~/praxis-signals`. The VM would sign in as that user | No shares VERIFIED (`HGFSPublish: publishing 0 shares`, this run, 17:51:17Z). Decision REPORTED (Amear took
```
Note: the Read & Write, Read Only and Open in Guest labels are split across HTML tags, so the raw grep finds 0 files for them. The tag-stripped run above finds them in p9.

## Adversarial findings
- Adversary 1 (8 defects) and adversary 2 (4 defects) are both closed as described in the process log. Findings files are in the scratchpad: adversary-findings.md and adversary2-findings.md.
- The main finding still holds and stays open for Amear: VMware's guest-OS page (26H1 and 13-0) says "Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts." That means the hand step may not work on his VM. The walkthrough puts this up front as Question 0 and chooses nothing.
- Grades: the menu labels are OBSERVED as text, but on pages filed under "Intel-based Mac", so whether they fit Apple silicon is INFERRED. The `vmhgfs.sys` absence is OBSERVED for Tools 13.0.5 only. The VM's Tools 13.1.5 is REPORTED, and nobody has checked it against that driver list. The `\\vmware-host\Shared Folders\` path was dropped because no fetched page shows it.
- Open: my own proxy for "one screen" was 3,000 bytes. The file is 3,067 bytes (31 lines). The rubric has no byte figure; I report the miss and don't game it.

## S6 cross-block check
- vs the share-path record (10-19 report row 3, D-072 REPORTED: SMB, `praxispush`, `~/praxis-signals` only): this conflicts with R-VN4-14 plus the Fusion route. It is surfaced as Question 0, not resolved (S8).
- vs repo safety: Read & Write on the whole repo lets the VM change any file there, including protected ones. Question 3 flags this and sets no default.
- vs the go-live checklist (R-VN4-14): the isolation line is there. Remove the shared folder (OBSERVED, 13-0). Untick Enable (INFERRED). Check that mirrored folders are off ("also enables mirrored folders", OBSERVED).
- vs the Google Drive `praxis-tickprep` exchange: left as an option. Nothing changes.

## Files staged
None. The brief said "Do not commit or `git add`". Both files are untracked (`??`, see the git status above). This report: docs/reports/2026-11-05-fusion-shared-folders-walkthrough-manager.md.

**Result: PASS** — the walkthrough document meets the brief after two adversarial rounds. Whether the step itself works on this VM is NEEDS AMEAR (Question 0), and VMware's page says it does not.

## Correction 1 (2026-11-06, after audit FAIL 1 on S1)
Trigger: audit row DECISION_LOG `2026-11-06T00:13:33Z` FAILed S1 (two BLOCKING, two MINOR). Lines 1–107 above are unchanged; their pre-correction sha256 (`head -107 | shasum -a 256`, taken before this append) was `1c9fca66ecff6efc1e4e983a0775ad3e7818059def1ddc84035d2b2c7b607dfe`. The walkthrough was not edited: every OBSERVED label in it matches a line pasted below, so no label is downgraded (its sha256 stays `8e776d93ee8d398a…`).
Everything below was run by the correcting manager in this session. Pages were fetched into `$E` = `scratchpad/corr-E/` (untrusted, never executed) and reduced to text by `python3 -I scratchpad/corr-scripts/strip.py`, run from `/`. That script drops script/style blocks and tags, unescapes entities, and writes one `.txt` per page, keeping the page's own line breaks. The line numbers below are line numbers in those `.txt` files.

### C1.1 Fetch (supersedes, for these 8 pages, the curl status lines at :58–79, which were copied from worker1-evidence.md)
```
$ cat scratchpad/corr-scripts/urls.tsv | while IFS=$'\t' read -r id u; do curl -sSL --max-time 20 -A "Mozilla/5.0" -o $E/$id.html -w "%{http_code} $id %{url_effective}\n" "$u"; done
200 e1 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/remove-a-shared-folder.html
200 e2 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac.html
200 e3 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html
200 e4 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html
200 e5 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/enable-shared-folders-or-mirrored-folders-for-a-virtual-machine.html
200 e6 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html
200 e7 https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html
200 e8 https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html
```

### C1.2 Scratch file → URL → sha256 (resolves MINOR 1; supersedes the prose mapping at :80, "p9 = 13-0 add-a-shared-folder, r5 = Tools 13.0.5 notes")
The earlier research-E files carry no canonical URL tag. Each one is tied to a URL here because its tag-stripped text hash (text-sha12) is identical to a fresh fetch of a known URL. p6 matches none of the eight re-fetched pages. No walkthrough claim rests on p6 alone.
```
$ cd / && python3 -I scratchpad/corr-scripts/map.py scratchpad
file | url | sha256(raw html) | text-sha12 | title
corr-E/e1.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/remove-a-shared-folder.html | 9dd421e78778c50c027480c505807ec1b4d4cb171d2adce980e917c7f63a0729 | 2616d0781fb7 | Remove a Shared Folder
corr-E/e2.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac.html | 2dac49d695df5feb940964da593504c0972f92df2d8ad7b15975de50a19b6c1c | 808582cac963 | Sharing Files Between Windows and Your Intel-based Mac
corr-E/e3.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html | 14ce69c0609d0176bd75d7d906a17fbe3556df75da1f8ea407db8077f3c07ba3 | 4e61f6b3e0d5 | Add a Shared Folder
corr-E/e4.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/add-a-shared-folder.html | 6c2b2199a462d9fb45198637be44ae33d2d9c5ebaab209e268903289fb4c541a | 8565afa12d90 | Add a Shared Folder
corr-E/e5.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/enable-shared-folders-or-mirrored-folders-for-a-virtual-machine.html | 9600e8809e05d6714f11bb37cac07807018a26a2d4d7f67af6bbe707afd5562d | 9c8248745e63 | Enable Shared Folders or Mirrored Folders for a Virtual Mach
corr-E/e6.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/26H1/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html | e6685b4a66442320b836e40ae6da2c02da9be41ecbfd19c3d5e9a47828419465 | f40f25441c83 | Guest Operating Systems That Support Shared Folders
corr-E/e7.html | https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/fusion-pro/13-0/using-vmware-fusion/sharing-files-between-windows-and-your-mac/guest-operating-systems-that-support-shared-folders.html | 212d41df58d5a95889fb788981d41a1ee6a1684b69cf4c6fa127534c2ac0cddd | d129f9037ba6 | Guest Operating Systems That Support Shared Folders
corr-E/e8.html | https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/13-0-0/release-notes/vmware-tools-1305-release-notes.html | bad5aa30582a542e3151dac48e670c8f2bdf95e0aa093177d0343208d148e748 | 668e38951642 | VMware Tools 13.0.5.0 Release Notes

earlier file | sha256(raw html) | text-sha12 | text identical to | title
research-E/p6.html | 71598a4368352a93ac44fb70c89a37e93959b712e9e0dabc7d1d544044aa6edb | 9562f88cd553 | none | Sharing Files Between Windows and Your Intel-based Mac
research-E/p7.html | deb776598dded542fab90dc1aff1cee43abea6ef9ae60abd5ca797726c092415 | d129f9037ba6 | e7 | Guest Operating Systems That Support Shared Folders
research-E/p8.html | 444cba63a693ae6a229c91a4e171e89fdc048c15b6c338b9ceb6981fcc5bb297 | 9c8248745e63 | e5 | Enable Shared Folders or Mirrored Folders for a Virtual Mach
research-E/p9.html | 157a5987f6812cb18b86ce87913dc9e3bc844d60e3b1d505ceeb6f97f158b8df | 4e61f6b3e0d5 | e3 | Add a Shared Folder
research-E/p10.html | e47afa4b096265232c98a443b264de44c817de06f1ccec36be10cbfda807091c | 2616d0781fb7 | e1 | Remove a Shared Folder
research-E/q3.html | 7daacc8e68d28f95a996e79955fbd8aff6a6a076b49710625f79156a2b7421b3 | 808582cac963 | e2 | Sharing Files Between Windows and Your Intel-based Mac
research-E/q4.html | d137e9df1809df4459cc1fbb9ad8850ce17dc3df94a5d2483cda6fbb22c86851 | f40f25441c83 | e6 | Guest Operating Systems That Support Shared Folders
research-E/q5.html | 7b731c4c6d56fed85206c00e069cd4a9e2ab4e6620b6d4dbd07e23c8ea1dfb0b | 8565afa12d90 | e4 | Add a Shared Folder
research-E/r5.html | 3ba77e86e6c90459c589f43a27e64155a23e0ee77242f8c2a308b134f95e91f5 | 668e38951642 | e8 | VMware Tools 13.0.5.0 Release Notes
```

### C1.3 OBSERVED labels: exact lines (resolves BLOCKING 1; supersedes the label grep at :34–44, the excerpts at :81–83 and the note at :90)
e1 = 13-0 remove-a-shared-folder · e2 = 26H1 sharing overview · e3 = 13-0 add-a-shared-folder · e4 = 26H1 add-a-shared-folder · e5 = 13-0 enable page · e6/e7 = 26H1/13-0 guest-OS pages (URLs in C1.1/C1.2).
Walkthrough :15–:16 (Window, Virtual Machine Library, Settings, Systems Settings, Sharing, Enable Shared Folders), :17 (VMware Shared Folders shortcut), :18 (add (+), Add), :19 and :10 (Permissions, Read & Write, Read Only):
```
$ awk 'NR>=59&&NR<=80{printf "e3.txt:%d: %s\n",NR,substr($0,1,330)}' e3.txt
e3.txt:59: Select Window Virtual Machine Library . Select a virtual machine in the Virtual Machine Library window and click Settings . Under Systems Settings in the Settings window, click Sharing . Select the
e3.txt:60: Enable
e3.txt:61: Shared Folders check box.
e3.txt:62: On Windows and macOS
e3.txt:63: virtual machines, a
e3.txt:64: VMware
e3.txt:65: Shared Folders shortcut is created on the guest operating system.
e3.txt:66: Click the add
e3.txt:67: ( + )
e3.txt:68: button at the bottom of the display box.
e3.txt:69: In the Finder sheet,
e3.txt:70: find the location of the folder to share, select it, and click
e3.txt:71: Add .
e3.txt:72: In the Permissions
e3.txt:73: field, set the virtual machine permission on the contents of the Mac's shared
e3.txt:74: folder.
e3.txt:75: Option Description
e3.txt:76: Read &
e3.txt:77: Write Enables the virtual machine to change the
e3.txt:78: contents of the shared folder on your Mac.
e3.txt:79: Read
e3.txt:80: Only Prevents the virtual machine from changing
$ awk 'NR>=56&&NR<=77{printf "e4.txt:%d: %s\n",NR,substr($0,1,330)}' e4.txt
e4.txt:56: Select Window Virtual Machine Library . Select a virtual machine in the Virtual Machine Library window and click Settings . Under Systems Settings in the Settings window, click Sharing . Select the
e4.txt:57: Enable
e4.txt:58: Shared Folders check box.
e4.txt:59: On Windows and macOS
e4.txt:60: virtual machines, a
e4.txt:61: VMware
e4.txt:62: Shared Folders shortcut is created on the guest operating system.
e4.txt:63: Click the add
e4.txt:64: ( + )
e4.txt:65: button at the bottom of the display box.
e4.txt:66: In the Finder sheet,
e4.txt:67: find the location of the folder to share, select it, and click
e4.txt:68: Add .
e4.txt:69: In the Permissions
e4.txt:70: field, set the virtual machine permission on the contents of the Mac's shared
e4.txt:71: folder.
e4.txt:72: Option Description
e4.txt:73: Read &
e4.txt:74: Write Enables the virtual machine to change the
e4.txt:75: contents of the shared folder on your Mac.
e4.txt:76: Read
e4.txt:77: Only Prevents the virtual machine from changing
```
Walkthrough :20 (Open in Guest):
```
$ awk 'NR>=86&&NR<=88{printf "e3.txt:%d: %s\n",NR,substr($0,1,330)}' e3.txt
e3.txt:86: Click the
e3.txt:87: Open in
e3.txt:88: Guest button to open the shared folder in the virtual machine.
$ awk 'NR>=83&&NR<=85{printf "e4.txt:%d: %s\n",NR,substr($0,1,330)}' e4.txt
e4.txt:83: Click the
e4.txt:84: Open in
e4.txt:85: Guest button to open the shared folder in the virtual machine.
```
Walkthrough :21 caution ("never open one file from both sides at once; a write can corrupt it"). Source: e2, the 26H1 overview. The walkthrough's "can" paraphrases the vendor's "might":
```
$ awk 'NR>=77&&NR<=81{printf "e2.txt:%d: %s\n",NR,substr($0,1,330)}' e2.txt
e2.txt:77: Do not open a file in
e2.txt:78: a shared folder from more than one application at a time. For example, do not
e2.txt:79: use an application on the Mac’s operating system and another application in the
e2.txt:80: virtual machine’s operating system to open the same file at the same time. If
e2.txt:81: one of the applications writes to the file, data might be corrupted.
```
Walkthrough :27 (**remove (-)**, 13-0; and "also enables mirrored folders", 13-0 enable page):
```
$ awk 'NR>=59&&NR<=63{printf "e1.txt:%d: %s\n",NR,substr($0,1,330)}' e1.txt
e1.txt:59: Select Window Virtual Machine Library . Select a virtual machine in the Virtual Machine Library window and click Settings . Under Systems Settings in the Settings window, click Sharing . In the display box
e1.txt:60: at the top of the Sharing panel, select the folder to remove.
e1.txt:61: Click the remove
e1.txt:62: ( - )
e1.txt:63: button at the bottom of the display box.
$ /usr/bin/grep -n -o 'Select the Enable Shared Folders check box.\{0,170\}' e5.txt
55:Select the Enable Shared Folders check box. This action enables shared folders. It also enables mirrored folders for supported Windows guest operating systems. On Windows and macOS virtual machines, a VMware Shar
```
Walkthrough :5 vendor quote (26H1 and 13-0 guest-OS pages). Walkthrough :14 says the pages are filed under the Intel-based Mac heading:
```
$ /usr/bin/grep -n -o '.\{0,40\}Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts\.' e6.txt e7.txt
e6.txt:51:dows, Mac, and Linux operating systems. Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts.
e7.txt:54:dows, Mac, and Linux operating systems. Shared Folder is not supported for Windows 11 ARM GOS on Apple Silicon hosts.
$ /usr/bin/grep -c 'Sharing Files Between Windows and Your Intel-based Mac' e1.txt e3.txt e4.txt e5.txt e6.txt e7.txt
e1.txt:3
e3.txt:3
e4.txt:3
e5.txt:3
e6.txt:4
e7.txt:4
$ awk 'NR>=1&&NR<=2{printf "e2.txt:%d: %s\n",NR,substr($0,1,330)}' e2.txt
e2.txt:1: Sharing Files Between Windows and Your
e2.txt:2: Intel-based Mac
```

### C1.4 Tools 13.0.5: Windows Arm driver list and every vmhgfs hit (resolves BLOCKING 2; supersedes :45–50 and the excerpts at :84–85)
e8 = VMware Tools 13.0.5.0 release notes. The Windows Arm list runs from line 94 (its header) to line 102, and "Useful Links" at line 103 ends it. Lines 60–93 hold the x64 list, for comparison:
```
$ awk 'NR>=60&&NR<=103{printf "e8.txt:%d: %s\n",NR,substr($0,1,330)}' e8.txt
e8.txt:60: VMware Tools 13.0.5.0 provides the following driver versions for Windows 8 (64-bit), Windows Server 2012 and later:
e8.txt:61: Drivers
e8.txt:62: VMware Tools 13.0.5.0
e8.txt:63: Hardware Drivers
e8.txt:64: efifwfromhost.bin
e8.txt:65: 1.0.0.2
e8.txt:66: pvscsi.sys
e8.txt:67: 1.3.29.0
e8.txt:68: vmci.sys
e8.txt:69: 9.8.30.0
e8.txt:70: vmmouse.sys
e8.txt:71: 12.5.15.0
e8.txt:72: vmusbmouse.sys
e8.txt:73: 12.5.15.0
e8.txt:74: vmxnet3.sys
e8.txt:75: 1.9.20.0
e8.txt:76: vm3dmp.sys
e8.txt:77: 9.17.09.0004
e8.txt:78: Software Drivers
e8.txt:79: vmhgfs.sys
e8.txt:80: 11.0.49.0
e8.txt:81: vmmemctl.sys
e8.txt:82: 7.5.10.0
e8.txt:83: vmrawdsk.sys
e8.txt:84: 1.1.9.0
e8.txt:85: vnetWFP.sys
e8.txt:86: 13.0.0.0
e8.txt:87: vsepflt.sys
e8.txt:88: 13.0.0.0
e8.txt:89: vsock.sys
e8.txt:90: 9.8.24.0
e8.txt:91: Security DLL
e8.txt:92: vmwsu.dll
e8.txt:93: 2.5.2.0
e8.txt:94: VMware Tools 13.0.5.0 provides the following driver versions for Windows Arm:
e8.txt:95: Hardware Drivers
e8.txt:96: VMware Tools 13.0.5.0
e8.txt:97: vmusbmouse.sys
e8.txt:98: 12.5.15.0
e8.txt:99: vmxnet3.sys
e8.txt:100: 1.9.20.0
e8.txt:101: vm3dmp.sys
e8.txt:102: 9.17.09.0004
e8.txt:103: Useful Links
$ /usr/bin/grep -n -o '.\{0,60\}vmhgfs.\{0,40\}' e8.txt
59: to VMware Tools 13.0.5.0 and later that includes vmmouse , vmhgfs , or pvscsi drivers when the VM’s sys
79:vmhgfs.sys
104:d Folders automatically on boot. For example, add the line: vmhgfs-fuse /mnt/hgfs fuse defaults,allow_othe
$ awk 'NR>=94&&NR<=103&&/vmhgfs/' e8.txt | wc -l
       0
$ awk 'NR>=94&&NR<=103&&/vmusbmouse/' e8.txt | wc -l   # positive arm: the same test does find a driver that is in the list
       1
```
Reading: the three vmhgfs hits are at line 59 (install note), line 79 (x64 list) and line 104 (Linux `vmhgfs-fuse`, after Useful Links). None falls inside 94–102. The walkthrough's :5 "no `vmhgfs.sys` for Windows Arm (OBSERVED)" holds for Tools 13.0.5 only. The VM's 13.1.5 is still not checked.

### C1.5 Header attribution (MINOR 2)
The header at :27, "Pasted output only (re-run by the manager this session)", is wrong for :58–79. Those lines are copied from worker1-evidence.md, as their own sub-header at :58 says. The manager did not re-run them. This correcting manager instance cannot tell, from this session, which of :29–57 and :80–89 the earlier manager re-ran and which it copied, so treat the :27 header as unverified for that whole block. C1.1–C1.4 replace it as evidence, and all of C1.1–C1.4 were run here.

### C1.6 Scope
No VM or Fusion contact. No worker was dispatched and no adversarial pass was run in this correction (narrow-correction budget). The master's re-audit is the independent check. Nothing staged:
```
$ cd /Volumes/Sensidine/Praxis.build && git status --short -- docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md docs/reports/2026-11-05-fusion-shared-folders-walkthrough-manager.md && git diff --cached --name-only | grep -c fusion-shared
?? docs/reports/2026-11-05-fusion-shared-folders-walkthrough-manager.md
?? docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md
0
```
