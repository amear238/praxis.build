# Manager report — unit 2026-11-11-v-rulings-filing

Result: PASS

## Task
File D-2026-11-11-A (Amear's rulings V1–V7 and MFFU's replies) and D-2026-11-11-B (limit 9 lift, Python/git install, record only) at the end of DECISIONS.md; de-identify the return-handoff file and the install reply; S13 addendum on the return-handoff file; MANIFEST rows. Authority: DECISION_LOG.md:828 (2026-11-11T18:19:40Z, WHO: amear) and :829 (18:20:00Z, praxis-master, the unit plan and four D1 decisions).

## Rubric criteria addressed
S1, S2, S4, S5, S8, S13 (specs/SPEC_RUBRIC.md).

## Workers dispatched (id, mode, outcome)
| id | mode | scope | outcome |
|---|---|---|---|
| worker1 | BUILD | D-2026-11-11-A and -B appended to DECISIONS.md, quotes copied by script | done; manager re-ran checks |
| worker2 | BUILD | de-identification of the two files; S13 addendum on the return-handoff file | done; manager re-ran checks |
| worker3 | ADVERSARIAL | attack on both entries and the de-identification | FAIL: 2 MAJOR, 10 MINOR |
| worker4 | BUILD | MANIFEST rows | done |
| worker5 | BUILD | fix pass 1 (13 fixes from worker3's findings) | done |
| worker6 | ADVERSARIAL | re-attack after worker5 | FAIL: 3 MAJOR, 6 MINOR |
| worker7 | BUILD | fix pass 2 (8 fixes) | done |
| worker8 | ADVERSARIAL | re-attack after worker7 | FAIL: 2 MAJOR, 10 MINOR |
| worker9 | BUILD | fix pass 3 (11 fixes) | done |
| worker10 | ADVERSARIAL | final attack (a)–(k) after worker9 | PASS: 0 MAJOR, 8 MINOR |

## Process log
1. Read DECISION_LOG.md:828–829, the return-handoff file (136 lines), the install reply (28 lines) and its two STATUS files, rubric F2/F4, DECISIONS.md:2047–2099, handoff §1 limit 9 (:37), the F2 proposal, R6 design OPEN-1 and the trading-day capture at bf6fcc7.
2. Partitioned by file: DECISIONS.md (workers 1, 5, 7, 9, serial), the two untracked files (worker 2 only), MANIFEST.md (workers 4, 5, 7, 9, serial). No two concurrent workers wrote one file. No worktree isolation: the inputs are untracked and would not exist in a worktree.
3. Every adversarial worker got the artifacts, the rubric criteria and the requirement list, never a build worker's reasoning.
4. Manager edits (pure doc edits, each one line): :2156 citation split (REPORTED at :2089, UNVERIFIED at :2085) after worker5; removed one duplicated sentence on :2156 after worker7; relabelled the two two-line quotes at :2129 and :2156 as "line break and the next line's leading indent joined as one space" after worker10 (its closest-to-a-break MINOR). Each edit followed by the append-only check (0 '-' lines vs HEAD).
5. Fix dispositions that kept the brief's text: the entry headings, "F2 stays FROZEN / NOT MET" for F4, "closing the A6 hold", and the "also needs breaker specs #4 and #5" wording are from the master's brief or DECISION_LOG.md:828; they were kept, attributed, and qualified (OPEN-F2-5 not closed; "also" not read as any part of the clause met) instead of removed.

## Verification evidence (command output)

Final sweep (manager, after the last edit):
```
$ grep -n "^## 2026-11-11" DECISIONS.md; wc -l
2101:## 2026-11-11 — D-2026-11-11-A: Amear's rulings V1–
2176:## 2026-11-11 — D-2026-11-11-B: VM handoff §1 limit 
    2203 DECISIONS.md
$ git diff HEAD --stat -- DECISIONS.md; minus-lines; hunk
 1 file changed, 104 insertions(+)
0
@@ -2099,0 +2100,104 @@ Fills 
$ S13 per entry (standalone / total / last-line)
A: 1 / 1 / 1
B: 1 / 1 / 1
$ D1 block heading
2151:**Decided by master under D-2026-11-08-D D1, changeable by Amear.**
2153: 1. The per-firm settings profile, the channel's proposal at return-han
2154: 2. The V7 strategy list at return-handoff :110, copied by script: "the
2155: 3. MFFU's "we do not offer Rithmic" (return-handoff :120) contradicts 
2156: 4. The VM-to-n8n path (O1, return-handoff :71) stays open. The channel
```
```
DECISIONS.md 2100-2203 lines=104 IPv4(all)=   1 127.0.0.1  non127=0 MAC=0 sshpath=0
MANIFEST.md 388-403 lines=16 IPv4(all)= non127=0 MAC=0 sshpath=0
N-test on original A: MAC=1 sshpath=1
machine-name (runtime, len 15) in DECISIONS/MANIFEST/A/B/unit reports: 0
```
Joined-quote check after the manager's relabel:
```
A6 joined quote in source: True | in entry: True
D2(d) joined quote in source: True | in entry: True
minus vs HEAD: 0
    2203 DECISIONS.md
```
MANIFEST:
```
     403 MANIFEST.md
lines 1-387 identical to pre-unit snapshot
0
388:  /DECISIONS.md 
389:  /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md 
390:  /vm/replies/20261111T172933Z-python-git-install.md 
391:  /vm/replies/20261111T172802Z-STATUS.md 
392:  /vm/replies/20261111T172940Z-STATUS.md 
393:  /docs/reports/2026-11-11-v-rulings-filing-manager.md 
394:  /docs/reports/2026-11-11-v-rulings-filing-worker1.md 
395:  /docs/reports/2026-11-11-v-rulings-filing-worker2.md 
396:  /docs/reports/2026-11-11-v-rulings-filing-worker3.md 
397:  /docs/reports/2026-11-11-v-rulings-filing-worker4.md 
398:  /docs/reports/2026-11-11-v-rulings-filing-worker5.md 
399:  /docs/reports/2026-11-11-v-rulings-filing-worker6.md 
400:  /docs/reports/2026-11-11-v-rulings-filing-worker7.md 
401:  /docs/reports/2026-11-11-v-rulings-filing-worker8.md 
402:  /docs/reports/2026-11-11-v-rulings-filing-worker9.md 
403:  /docs/reports/2026-11-11-v-rulings-filing-worker10.md 
lines 2101-2174 lines 2176-2203 lines 1-2099 
all listed paths checked
```
S13 in reports, and the index:
```
2026-11-10-return-handoff-claude-ai-voice-rulings.md: 1/1
2026-11-11-v-rulings-filing-worker1.md: 1/1
2026-11-11-v-rulings-filing-worker10.md: 1/1
2026-11-11-v-rulings-filing-worker2.md: 1/1
2026-11-11-v-rulings-filing-worker3.md: 1/1
2026-11-11-v-rulings-filing-worker4.md: 1/1
2026-11-11-v-rulings-filing-worker5.md: 1/1
2026-11-11-v-rulings-filing-worker6.md: 1/1
2026-11-11-v-rulings-filing-worker7.md: 1/1
2026-11-11-v-rulings-filing-worker8.md: 1/1
2026-11-11-v-rulings-filing-worker9.md: 1/1
$ index
docs/reports/evidence/[2026-10-28 MFFU reply image, filename withheld]
```
(The one staged path is the held-out PNG that was staged before this unit; this unit staged nothing.)

De-identification (deliverable 3). Diff against the /tmp copies, original lines masked:
```
== docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
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
== vm/replies/20261111T172933Z-python-git-install.md
17c17
< [original line masked]
---
> 1. `[VM machine name]\amear` / `v1.29.380` / `True` / NinjaTrader `9600 2026-11-10 5:46:59 PM`
```
Changed lines, before-text described: return-handoff :65 (the VM's LAN IPv4 address; the VM NIC's MAC address); :66 (the Mac's LAN IPv4 address; the Mac's tailnet IPv4 address; 127.0.0.1 and the n8n URL kept); :68 (the SSH private-key file path; the VM IPv4 address and the user value in the ssh-config mapping; Host alias `praxis-vm` kept, already in 15 tracked files); install reply :17 (the VM's Windows machine name; `\amear` kept). Post-edit counts and line counts:
```
     138 docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
      28 vm/replies/20261111T172933Z-python-git-install.md
A S13 standalone 1 total-lines-containing 2; last line standalone 1
-- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
66:127.0.0.1
108:8.1.8.4
108:127.0.0.1
MAC 0 ; .ssh lines:
68:~/.ssh/config
100.x tailnet: 0
-- vm/replies/20261111T172933Z-python-git-install.md
18:2.56.0.4
18:2.56.0.4
MAC 0 ; .ssh lines:
100.x tailnet: 0

HEAD tracked files with Bani-Ahmad:       22; with n8n URL:       23; praxis-vm:       15
```
The remaining IPv4-regex matches are version strings: `8.1.8.4` is the NT8 file version (A:108), `2.56.0.4` is the git version (B:18). IPv4 addresses other than 127.0.0.1: 0. MAC: 0. Private-key paths: 0 (`~/.ssh/config` is the config file, kept). Machine name: 0 (count above). The A:5 "Standing limitation:" line contains the S13 sentence inline; the standalone count is 1 (the last line).

Negative tests (manager): each check catches a planted failure.
```
N1 S13 standalone (expect 0): 0; last-line S13 (expect 0): 0
N2 2026-11-10-return-handoff-claude-ai-voice-rulings.md: IPv4-non-loopback-non-version hits=4 MAC=1 keypath=1
N2 20261111T172933Z-python-git-install.md: IPv4-non-loopback-non-version hits=0 MAC=0 keypath=0
N3 true quote found: yes
N3 mutated quote found: no (check blocks)
N4 minus-lines on mutated copy (expect 1): 1
N2b machine-name pattern on original B (expect >=1): 1; on edited B (expect 0): 0
```
(N1: entry A with its S13 line removed; N2: scan on the pre-edit /tmp copies; N3: a one-character mutation of the V2 quote; N4: a one-word edit planted at DECISIONS.md:2047 in a scratch copy.) A first N4 run planted the edit on a line that did not contain the target word and printed 0. It was re-run on :2047 and printed 1, as above.

## Adversarial findings
- worker3 (FAIL). MAJOR 1: "answers the A6 hold" read as a grade beside "F2 stays FROZEN". Fixed by worker5, then refined by workers 7 and 9: filed as closing the A6 hold (Amear's approval, the first of OPEN-F2-5's three parts); OPEN-F2-5 not closed; the A6 trigger not graded. MAJOR 2: entry B did not state the S4/S5 order failure or the Hermes-only D2(d) reading. Fixed (worker5): both stated as fact, and an Open-for-Amear item added. 10 MINOR: fixed or noted (worker5 fixes 2–12).
- worker6 (FAIL). M1 "also requires" in the entry's own voice; M2 OPEN-F2-5 implied closed; M3 a sentence in decision 4 that is not in DECISION_LOG.md:829. All fixed by worker7. MINORs: Rithmic citation re-pointed to DECISIONS.md:2054, O2 added to Open for Amear, MANIFEST descriptions fixed.
- worker8 (FAIL). M1: the "also" came back through the DECISION_LOG quote. Fixed by worker9: the quote is kept and the entry states it does not read "also" as any part of the clause being met. M2: the header-export item was widened. Fixed: "outgoing V1 message ... if the auditor wants headers". m1–m10: fixed by worker9 (context moved out of decision 4, "uses SSH keys" restored, duplicates removed, "VM handoff" wording, MANIFEST :389/:401). The headings stay exactly as the brief gives them (m4 not applied to the heading; a V4-from-chat sentence was added under Authority instead).
- worker10 (PASS, 0 MAJOR). The manager fixed one MINOR (the joined-quote labels). Seven MINORs remain, recorded and not fixed: "U do them" scope is stated only in install reply :8; :2108 and :2129 pull in two directions on A6; some context remains inside the numbered master decisions; the S6 line says "Rule F2-1 approved" without its qualifier; the install started at 17:28:02Z by its STARTED file, while entry B gives 17:29:33Z, the reply's stamp; cli-nt-bridge is paired with Amear's bash-tool question, but the file does not say it is the tool he meant; "D2(d)" for further channel SSH driving is the filer's reading and is not labelled as such.
- For the master (outside this unit's write set, not edited):
  (1) The Mac's LAN IPv4 address removed from return-handoff :66 is already in 8 HEAD-tracked files, including DECISIONS.md, DECISION_LOG.md and vm/2026-11-06-vm-handoff.md (`git grep -lF` count 8). worker3 also reports a removed address at DECISIONS.md:1004/:1016 and DECISION_LOG.md:517.
  (2) The VM machine name is in 2 untracked files of the open Hermes-grading unit: docs/reports/2026-11-11-hermes-replies-grading-worker1.md and vm/replies/20261110T214834Z-self-report.md. It is in 0 files at HEAD.
  (3) F2 proposal :8 cites the rubric's unblock clause at :43–44; it is at :30–31 now.
  (4) Whether vm/replies files fall under S13 is unstated. The install reply has no S13 line, by the brief.
  (5) worker10 note: master decision 1 adopts the profile direction that the channel left for Amear to confirm (O2). The entry lists O2 under Open for Amear.
  (6) Entry B records that the install (17:29:33Z) came before any ledger append. No filing repairs that.

## S6 cross-block check
- Block 2: decision 2 makes the V7 list the NT8 backtest plan's working scope and moves R6's first pass into NT8. The handoff step 3.5 pip step on ARM64 wheels is UNVERIFIED (entry B).
- Block 3: D-2026-11-10-B's Rithmic route is recorded as contradicted by MFFU's reply and not re-decided. The VM-to-n8n path stays open, and the tunnel keys are D2(d). Breakers #4 and #5 are not amended.
- Rubric F2: stays FROZEN. Rule F2-1 is approved on the words put to Amear, and OPEN-F2-5 is not closed.
- Rubric F4: stays FROZEN / NOT MET. The replacement ticket (investigation C3.3) is Amear's to send.
- R6 OPEN-1: still open. MFFU's 23:08:17Z reply did not answer it.
- D-2026-11-10-C: entry B records that the Claude.ai channel, not Hermes, drove the install. D-2026-11-10-C's D2(d) reading covers Hermes only.

## Files staged
None staged (hard limit: no git add). Working-tree changes:
- DECISIONS.md: :2100–2203 appended; D-2026-11-11-A at :2101–2174, D-2026-11-11-B at :2176–2203.
- docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md: :65, :66, :68 edited; :137–138 appended.
- vm/replies/20261111T172933Z-python-git-install.md: :17 edited.
- MANIFEST.md: :388–403 appended.
- This report and the reports of workers 1–10.
- The STATUS files 20261111T172802Z and 20261111T172940Z: unchanged, rows only.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
