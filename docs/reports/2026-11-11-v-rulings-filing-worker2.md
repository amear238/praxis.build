# Worker 2 report — unit `2026-11-11-v-rulings-filing`

## Task
Itemised de-identification of two untracked files before they are committed to a public repo, and one S13 addendum to file A.
- A = `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md`
- B = `vm/replies/20261111T172933Z-python-git-install.md`

## Mode
BUILD. Working dir `/Volumes/Sensidine/Praxis.build`, branch main, HEAD d056e91.

## Criterion
Remove VM and Mac network identifiers, the SSH key path, the ssh-config address/user mapping values and the VM machine name. Keep everything else byte-identical. Append the S13 addendum (two lines) to A only. Paste raw evidence (S1).

## Process log
1. Made `/tmp/vrf-deid/` and copied A and B into it before any edit. Recorded the sha256 of the originals (below; the copies' hashes match the pre-edit working files: A `7c278d90…`, B `e0f09b1f…`).
2. Ran the regex scan on the backup copies. Hits by line (described, not retyped):
   - A:65: one IPv4 (the VM's LAN address) and one MAC (the VM NIC MAC).
   - A:66: `127.0.0.1` (kept), the Mac's LAN IPv4 and the Mac's tailnet IPv4 (inside 100.64.0.0/10).
   - A:68: SSH key path `~/.ssh/<key name>` and the `~/.ssh/config` mapping: Host `praxis-vm` → the VM's LAN IPv4 (same value as A:65), User `<VM username>`.
   - A:108: `8.1.8.4` (NT8 file version; kept) and `127.0.0.1` (kept).
   - B:17: the VM's Windows machine name (a `desktop-` prefix plus a suffix) before `\amear`.
   - B:18: `2.56.0.4` twice (Git version; kept).
   - No `id_rsa`, `id_ed25519` or `.pem`. No `\\` UNC user prefixes. No other tailnet address.
   - The manager's pre-scan matched my scan on every item.
3. Proved the Host alias `praxis-vm` is already in tracked files: `git grep -c 'praxis-vm' HEAD | wc -l` → 15 files (for example `HEAD:DECISIONS.md:2`, `HEAD:docs/reports/2026-11-06-vm-handoff-manager.md:15`).
4. Did the edits with a script in `/tmp/vrf-deid-scripts/edit.sh`. Each value was pulled at runtime from the `/tmp` backup at its exact line (A:65, 66, 68; B:17), so no identifier was typed. Replacements were limited to those lines (perl `$.==N`) and used `\Q…\E` literal matching. The tailnet value was picked by a 100.64/10 range test, and the Mac LAN value is whatever is left on line 66 after removing 127.0.0.1 and the tailnet value. The machine-name pattern was built from B line 17 of the `/tmp` copy (the text between the opening backtick and the backslash).
5. Appended the two addendum lines to A with `printf '%s\n'`, so the file ends with a newline. Line 5 is unchanged (checked with `cmp`).
6. Verified with `/tmp/vrf-deid-scripts/verify.sh` (output pasted below).

### Difference from the precedent (worker 7, `docs/reports/2026-11-11-mffu-investigation-correction-1-worker7.md` item 7)
- Worker 7 used `[VM MAC]`, `[tailnet IP]`, `[VM LAN IP]` and added ` (values redacted by worker 7)` to the edited line.
- Here I used the placeholders the brief named instead: `[VM LAN address]`, `[MAC]`, `[Mac LAN address]`, `[Mac tailnet address]`, `[key file]`, `[VM user]`, `[VM machine name]`. I added **no** inline "redacted by" note, because the brief allowed no edits other than the replacements and the S13 addendum.
- Style kept the same as the precedent: each placeholder sits inside the original quoting (backticks stay where the value had backticks; the bare address on A:68 stays bare).

## Per-line table

| file:line | before (described) | after (pasted) |
|---|---|---|
| A:65 | VM LAN IPv4 in backticks | `` `[VM LAN address]` `` |
| A:65 | VM NIC MAC in backticks | `` `[MAC]` `` |
| A:66 | Mac LAN IPv4, followed by `:5678` | `` `[Mac LAN address]:5678` `` |
| A:66 | Mac tailnet IPv4 (100.64/10), followed by `:5678` | `` `[Mac tailnet address]:5678` `` |
| A:66 | `127.0.0.1:5678`, n8n URL | unchanged |
| A:68 | SSH private-key path `~/.ssh/<key name>` in backticks | ``key `[key file]` `` |
| A:68 | ssh-config mapping address (VM LAN IPv4, bare) | `→ [VM LAN address]` |
| A:68 | ssh-config User value in backticks | ``User `[VM user]` `` |
| A:68 | `~/.ssh/config`, Host `praxis-vm`, key comment | unchanged |
| A:137 | (new) | `Filer's addendum, 2026-11-11: standing limitation line added as house style (S13).` |
| A:138 | (new) | S13 sentence (see the last line of this report) |
| B:17 | VM Windows machine name before `\amear` | `` `[VM machine name]\amear` `` |

## Verification evidence
Raw output of `/tmp/vrf-deid-scripts/verify.sh`. In the diffs, every `<` line is replaced by `< [original line masked]` (sed `s/^< .*/< [original line masked]/`). Hunk headers (line numbers) and `>` lines are raw.

```
### sha256 before (backup copies) / after
7c278d90dfd8044c19caa77c00eb9b3def5cedf733d9af455fc7eb7638a6e64d  /tmp/vrf-deid/2026-11-10-return-handoff-claude-ai-voice-rulings.md
e0f09b1f1a746ec4657286ecf8f3b452cc5c8b3c2bfb472eb361b1f1472e2f5e  /tmp/vrf-deid/20261111T172933Z-python-git-install.md
2f5207a01f7da8dd64503969c8e5aee9ea582b9463970642c0668f6d006c7c41  docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
7f198ed3f8a2655bea4aaf123183d90a8a26e0bd460d2b12cc96c75a0f1f2a3f  vm/replies/20261111T172933Z-python-git-install.md
### diff A ('<' lines masked: only line numbers kept)
65,66c65,66
< [original line masked]
< [original line masked]
---
> - VM NIC on the LAN: `[VM LAN address]` at MAC `[MAC]` (arp). Ports 22, 445, 3389, 5985, 5986 closed from the Mac; ping fails.
> - n8n (`n8n-compose-n8n-1`) publishes `127.0.0.1:5678` only; from the Mac, `[Mac LAN address]:5678` and `[Mac tailnet address]:5678` are closed. `WEBHOOK_URL=https://n8n.myzerker626.win/`. **OPEN-T1 consequence (INFERRED, untried from the VM):** a VM-to-webhook check against the Mac's LAN or tailnet address fails as configured today.
68c68
< [original line masked]
---
> - Mac side already prepared (file times 2026-11-10T14:43 ET, maker not observed, presumably Hermes): key `[key file]` (comment `hermes-praxis-vm`), `~/.ssh/config` Host `praxis-vm` → [VM LAN address], User `[VM user]`. Port 22 on the VM still closed at 19:58Z.
136a137,138
> Filer's addendum, 2026-11-11: standing limitation line added as house style (S13).
> Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
### diff B ('<' lines masked)
17c17
< [original line masked]
---
> 1. `[VM machine name]\amear` / `v1.29.380` / `True` / NinjaTrader `9600 2026-11-10 5:46:59 PM`
### wc -l
     138 docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
      28 vm/replies/20261111T172933Z-python-git-install.md
     166 total
### docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
IPv4 non-127.0.0.1 matches (line:match):
108:8.1.8.4
IPv4 non-127 count: 1
127.0.0.1 count: 2
MAC count: 0
tailnet 100.64/10 count: 0
.ssh/ paths:
68:.ssh/config
id_rsa/id_ed25519/.pem count: 0
desktop- (ci) count: 0
machine-name (runtime pattern, ci, fixed) count: 0
placeholders:
65:[VM LAN address]
65:[MAC]
66:[Mac LAN address]
66:[Mac tailnet address]
68:[key file]
68:[VM LAN address]
68:[VM user]
### vm/replies/20261111T172933Z-python-git-install.md
IPv4 non-127.0.0.1 matches (line:match):
18:2.56.0.4
18:2.56.0.4
IPv4 non-127 count: 2
127.0.0.1 count: 0
MAC count: 0
tailnet 100.64/10 count: 0
.ssh/ paths:
(none)
id_rsa/id_ed25519/.pem count: 0
desktop- (ci) count: 0
machine-name (runtime pattern, ci, fixed) count: 0
placeholders:
17:[VM machine name]
### A lines 65,66,68 after
- VM NIC on the LAN: `[VM LAN address]` at MAC `[MAC]` (arp). Ports 22, 445, 3389, 5985, 5986 closed from the Mac; ping fails.
- n8n (`n8n-compose-n8n-1`) publishes `127.0.0.1:5678` only; from the Mac, `[Mac LAN address]:5678` and `[Mac tailnet address]:5678` are closed. `WEBHOOK_URL=https://n8n.myzerker626.win/`. **OPEN-T1 consequence (INFERRED, untried from the VM):** a VM-to-webhook check against the Mac's LAN or tailnet address fails as configured today.
- Mac side already prepared (file times 2026-11-10T14:43 ET, maker not observed, presumably Hermes): key `[key file]` (comment `hermes-praxis-vm`), `~/.ssh/config` Host `praxis-vm` → [VM LAN address], User `[VM user]`. Port 22 on the VM still closed at 19:58Z.
### B line 17 after
1. `[VM machine name]\amear` / `v1.29.380` / `True` / NinjaTrader `9600 2026-11-10 5:46:59 PM`
### A line 5 unchanged?
line 5 identical
### A last 3 lines
     1	- "we see you've been inactive for some time, so this ticket is being closed." Any re-ask needs a new ticket or a reply that reopens it (Amear's hands; the verification details are his to give).
     2	Filer's addendum, 2026-11-11: standing limitation line added as house style (S13).
     3	Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
00000000: 0a                                       .
standalone S13 in A (grep -cxF): 1
total S13 occurrences in A (grep -oF | wc -l): 2
S13 in B: 0
### lines other than 65,66,68 + appended identical in A?
A: all other 133 original lines identical
B: all other 27 lines identical
### tracked-file presence
      22
HEAD:.beads/issues.jsonl:1
HEAD:.claude/settings.json:1
HEAD:HANDOFF.md:2
HEAD:docs/design/2026-07-08-block1-signal-delivery.md:1
HEAD:docs/design/2026-07-09-b1-a-wireguard-ssh-runbook.md:1
HEAD:docs/reports/2026-05-11-sess2-step-0.5-webhook.md:3
HEAD:docs/reports/2026-05-11-sess2-step-0.6-telegram.md:1
HEAD:docs/reports/2026-07-08-block1-delivery-design.md:1
HEAD:docs/reports/2026-07-08-orch-notify.md:4
HEAD:docs/reports/2026-07-08-step-0.8-full-loop.md:2
### index unchanged for these paths
?? docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
?? vm/replies/20261111T172933Z-python-git-install.md
```

The `22` under "tracked-file presence" is `git grep -c 'Bani-Ahmad' HEAD | wc -l`, meaning 22 tracked files already contain it. The `HEAD:` lines are `git grep -c 'n8n.myzerker626.win' HEAD | head`.

The IPv4-shaped strings that remain are version strings, not addresses (context grep):
```
108:.md` — NT8 running (pid 9600, 8.1.8.4 file version),
18:nd Git [Git.Git] Version 2.56.0.4 … Downloa
18:ad/v2.56.0.windows.4/Git-2.56.0.4-arm64.exe
```

Total S13 in A is 2: line 5 (inside "Standing limitation: …", unchanged) and line 138 (standalone).

## Identifiers found but NOT edited (outside the brief's list; reported only)
1. **The VM username is still recoverable.** A:68 now reads User `[VM user]`, but the brief keeps B:17 `[VM machine name]\amear`, and that shows the same Windows account name. A:116 (`Hello amear,`) and the `WHO: amear` lines carry it as well. The `[VM user]` placeholder therefore hides nothing new. This is a consistency point for the manager. I made no edit.
2. Gmail message and thread ids (A:11, 83, 112, 114, 132, 135). Kept per the brief.
3. `support@myfundedfutures.com` (A:114, 132). This is a public company address. Kept.
4. Mac-side paths `/Volumes/VMs/Windows 11 Fusion.vmwarevm/…vmx` (A:64), `/Volumes/Sensidine/Praxis.build` (A:67) and `~/.hermes/hermes-agent` (A:63). Kept per the brief (vmx path) or not on the list.
5. Container name `n8n-compose-n8n-1`, NT8 pid 9600 and winget `v1.29.380`. These are not identifying. Kept.
6. The key comment `hermes-praxis-vm`. Kept per the brief.

## Files staged
None. I made no change to the git index (both paths are still `??`). Files written: A, B, and this report. I also wrote scratch files outside the repo: `/tmp/vrf-deid/` (original copies) and `/tmp/vrf-deid-scripts/` (edit.sh, verify.sh).

## Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
