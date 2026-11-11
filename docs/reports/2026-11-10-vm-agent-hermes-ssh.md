# Unit 2026-11-10-vm-agent-hermes-ssh — manager report

## Task
Write the CODE- reply naming Hermes over SSH as the VM agent (terms T1–T7), handoff Amendment 3, DECISIONS.md entry D-2026-11-10-C and MANIFEST rows. Authority: Amear's proposal (DECISION_LOG 2026-11-10T20:42:00Z, WHO: amear) and the master's acceptance (DECISION_LOG 2026-11-10T20:43:00Z, decided by master under D-2026-11-08-D D1). Everything is left unstaged.

## Rubric criteria addressed
S1, S2, S4, S5, S6, S8, S13 (specs/SPEC_RUBRIC.md:124–136). Every acceptance check below traces to one of them.

## Workers dispatched
| # | Mode | Scope | Outcome | Report |
|---|---|---|---|---|
| 1 | BUILD | Drafted the CODE- reply (in the scratchpad, with a `__TS__` placeholder), Amendment 3, D-2026-11-10-C and the MANIFEST rows | PASS (self) | docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md |
| 2 | ADVERSARIAL | Attacked worker 1's four artifacts against the spec, the rubric and the Hermes skill | FAIL: 3 BLOCKING (F1–F3), 12 MINOR (F4–F15) | docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md |
| 3 | BUILD (fix) | Applied F1–F13 as the manager decided them; F14 and F15 were left to the manager | PASS (self) | docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md |
| 4 | ADVERSARIAL (re-check) | Confirmed F1–F13 closed; fresh attack; hygiene | PASS: 0 BLOCKING, 4 MINOR | docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md |

## Process log
- The manager read the rubric (S1–S13, D1–D5), DECISION_LOG :813–:814, the handoff (§0, §1, §3–§7), vm/replies/README.md, the Hermes skill (read-only), DECISIONS.md :1080–1095 and its tail, and the MANIFEST tail.
- **Placement rule.** The CODE- reply was drafted outside the repo and written into vm/replies/ only once, after worker 4's PASS. There were two reasons: (a) a reply is never edited (vm/replies/README.md), and (b) the skill's gate 1 opens as soon as such a file exists. The timestamp came from `date -u +%Y%m%dT%H%M%SZ` at placement (20261110T211738Z). The `__TS__` placeholder was then filled in the handoff bullet, the DECISIONS entry and the MANIFEST row.
- **F1 decision.** The manager did not widen T2(a)'s screen-STOP amendment beyond step 1 items 0 and 6, as the brief requires. Instead, T2(d) records the master's reading that step 3.3 is Amear's compile, which Hermes quotes, not a read Hermes makes from the screen. So the skill's screen-STOP rule does not fire there.
- **F3 wording.** Worker 3 narrowed the manager's "no file outside C:\praxis\" to "no venv outside C:\praxis\; no file outside what limit 10 names". The manager's version would have contradicted limit 10 (steps 3.2 and 3.4). Accepted.
- **Worker 4's four MINORs were not applied.** The placed text is therefore the text worker 4 attacked. They are carried forward under Could not do.
- The manager ran no ssh, vmps.sh, curl or VM command (S2: the VM side is Hermes's to observe in step 1).

## Verification evidence (command output)
```
$ git diff --numstat -- vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md
25	0	DECISIONS.md
16	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
$ git status --porcelain -- vm/replies docs/reports/2026-11-10-vm-agent-hermes-ssh*
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md
?? docs/reports/2026-11-10-vm-agent-hermes-ssh.md
?? vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
$ head -4 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
REPLY-TO: Amear's 2026-11-10 proposal (DECISION_LOG 2026-11-10T20:42:00Z, WHO: amear) and Z:\vm\2026-11-06-vm-handoff.md §0 settlement 3
WRITTEN-BY: Claude Code on the Mac (praxis-master, through unit 2026-11-10-vm-agent-hermes-ssh)
UTC: 20261110T211738Z
RESULT: DONE
$ tail -1 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md | grep -cxF '<the S13 sentence>'
1
$ grep -n "Amendment 3 (2026-11-10)" vm/2026-11-06-vm-handoff.md | cut -c1-200
23:- **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`), per the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md` 
$ grep -n "^## 2026-11-10 — D-2026-11-10-C" DECISIONS.md
2076:## 2026-11-10 — D-2026-11-10-C: VM agent = Hermes over SSH (settlement 3 changed; master under D1)
$ cmp <(git show HEAD:DECISIONS.md) <(head -2074 DECISIONS.md) && echo same
same
$ S13 counts (grep -cF)
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md 1
vm/2026-11-06-vm-handoff.md 1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md 1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker2.md 1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker3.md 1
docs/reports/2026-11-10-vm-agent-hermes-ssh-worker4.md 1
HEAD handoff 1
DECISIONS :2075-end 1
$ IPv4 grep on new reply + entry
   1 /dev/fd/11:8:127.0.0.1
   2 vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:56:127.0.0.1
$ grep -c 20261110T211738Z
vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md:2
vm/2026-11-06-vm-handoff.md:1
MANIFEST.md:1
DECISIONS.md:1
$ ls vm/replies
20261110T211738Z-CODE-vm-agent-hermes.md
README.md
```
Notes on the evidence:
- The MANIFEST figure of +16 is the 8 rows that were already uncommitted before this unit, plus 8 rows from this unit at :364–371.
- The handoff S13 count is 1 at HEAD and 1 now, so Amendment 3 added none.
- The only IP address in the new text is loopback 127.0.0.1.

**Negative tests (the gates trip).**
```
$ ls vm/replies/*-CODE-*.md        # before placement: Hermes gate 1 stays closed
(eval):1: no matches found: vm/replies/*-CODE-*.md
$ set -o noclobber; echo x > vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md   # second write to a placed reply
(eval):1: file exists: vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md
exit=1
```

## Adversarial findings
- **Worker 2, BLOCKING.** All three were fixed by worker 3, and worker 4 confirmed each closed with the line quoted.
  - F1: step 3.3 STOP-vs-continue clash. Fixed in T2(d).
  - F2: the one-session rule ran in one direction only. Fixed by T5(a).
  - F3: a fresh shell loses the working folder and the venv, with a risk of a venv outside C:\praxis\. Fixed in T3(b).
- **Worker 2, MINOR F4–F13.** Applied.
  - T3(c) `<ts>` source; T1(b) read §0 Amendment 3.
  - T1(c) copied skills used only under the skill's gates.
  - Step 4.3 set-up labelled as the master's reading.
  - Settlement 7 named.
  - T2(e) go-2a precedence.
  - Amendment 3's §1 carve-out.
  - The S2 label fixes.
  - The :1912–1916 citation.
- **F14.** The reply was placed only after the adversarial PASS. Placeholders are filled; the counts are above.
- **F15** is outside this unit's files and is named for the master below.
- **Worker 4, MINOR, not applied** (each fails safe). See Could not do.

## S6 cross-block check
D-2026-11-10-C carries the S6 paragraph (DECISIONS.md:2076 onward). It covers four things:
- **Block 2.** Handoff tests 2b (steps 1–2) and 2a (step 4.3 hand reads stay with Amear; ruling 6's partial-pass reading unchanged).
- **Block 3.** D-2026-11-10-B and OPEN-T1. The T6 GET from a PowerShell session is not the NT8 webhook path, so it does not settle OPEN-T1. That the live design would depend on an SSH session staying up is left as a Block 3 question.
- **The go-live list** in docs/reports/2026-11-05-fusion-shared-folders-walkthrough.md. The SSH key, the firewall rule and the tunnel are PROPOSED as go-live items, not added; that file is not edited.
- **The interplay** between limit 10 / limit 11 and the skill's gates.

Worker 4 spot-checked 20 citations in the new text, and all pointed where they say (its report).

## Files touched (left unstaged)
- vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md (new)
- vm/2026-11-06-vm-handoff.md (+1 line, :23)
- DECISIONS.md (+25 lines, :2075–2099)
- MANIFEST.md (+8 rows at the end, :364–371)
- docs/reports/2026-11-10-vm-agent-hermes-ssh.md
- docs/reports/2026-11-10-vm-agent-hermes-ssh-worker1.md to -worker4.md

The real index still holds only docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png.

## Could not do / carried forward
1. **Step 4.5 Help → About (worker 4, minor 1).** Handoff :284 "Record both" needs a Help → About read in step 4. T2 lifts the screen-STOP rule only for step 1 items 0 and 6, as the brief requires, so step 4 would end STOP. A later CODE-go-2a reply can settle this (T2(e) "until it says otherwise").
2. **Step 2 `<ts>` (worker 4, minor 2).** T3(c) lets `<ts>` come from either clock, but the reporter skill takes `<ts>` from its own command 5. Code should grade test 2b against that skill's text.
3. **Skill copy folder (worker 4, minor 3).** T1(c) does not name creating the folder the skill copy needs, and a re-run of step 2 would STOP on "already there". This fails safe.
4. **T5(a) Code-side close rule (worker 4, minor 4).** The rule that a Code session seeing a newer STARTED closes lives only in the reply. It is absent from the DECISIONS pointer and from HANDOFF.md, which timer runs read; HANDOFF.md is outside this unit's files. How Hermes detects a running Code session is UNVERIFIED.
5. **F15 (for the master).** DECISION_LOG.md:814, a public-repo file outside this unit, pairs the SSH username with the host alias. No IP address or key path is in it.
6. **D-2026-11-10-C cites rows that are not committed yet.** It cites DECISION_LOG.md:813–814, which are uncommitted, so the commit must carry DECISION_LOG through :814.
7. **Nothing on the VM side was observed by Code.** SSH, the key, the firewall, the tunnel, n8n and /healthz all stay REPORTED BY Amear or UNVERIFIED.
8. **Gate 1 is open.** Placing the reply opens Hermes's gate 1 before the auditor grades it. If the audit fails, the cure is a new correcting CODE- reply, never an edit.

## Result
Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
