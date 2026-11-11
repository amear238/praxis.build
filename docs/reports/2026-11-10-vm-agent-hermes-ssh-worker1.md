# Worker 1 report — unit 2026-11-10-vm-agent-hermes-ssh

## Task
Draft the CODE- reply naming Hermes over SSH as the VM agent (placeholder `__TS__`, kept in scratchpad, not in `vm/replies/`); add handoff Amendment 3 (one §0 bullet); append DECISIONS.md D-2026-11-10-C; append six MANIFEST rows; this report.

## Mode
BUILD. Nothing staged by me (brief forbids `git add`). No ssh, vmps.sh, curl or n8n call. `~/.hermes` read only.

## Criterion
specs/SPEC_RUBRIC.md S1, S2, S4, S5, S6, S8, S13; D1–D2 (:440–447). Authority: DECISION_LOG.md:813 (2026-11-10T20:42:00Z, WHO: amear) and :814 (20:43:00Z, master under D1).

## Process log
1. Read DECISION_LOG.md:805–814, Hermes's skill `praxis-vm-over-ssh` (read only), handoff §0, §1, step 1, step 2, steps 3–4 (incl. 3.3, 4.2, 4.3, commission paragraph :268), §7, `vm/replies/README.md`, both VM skills under `vm/skills/`, DECISIONS.md:1080–1095 and :2040–2074, topology doc :88–114, the walkthrough, rubric :118–142 and :428–464, MANIFEST tail.
2. Wrote the draft: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-vm-agent-hermes.draft.md` (61 lines). Four header lines exactly as briefed; §7 sections in order (all "none"); then `## Terms: Hermes over SSH is the VM agent` with T1–T7 and sub-points; a "What this reply does not do" paragraph; the S13 sentence as the last line.
3. Inserted one bullet at handoff :23 (after Amendment 2 at :22) by script; nothing else changed or struck.
4. Extracted Amear's words from DECISION_LOG.md:813 by script (text between `verbatim excerpt: "` and `" The SSH key, firewall rule`) into a scratch file; appended D-2026-11-10-C to DECISIONS.md with the quote substituted by script. Byte-exact check below.
5. Appended six MANIFEST rows at the end. Lines 1–363 checked byte-identical to the pre-edit copy.

## Conflicts (i)–(v) and how each was resolved (all marked in the draft "master's reading under D1, changeable by Amear")
- **(i) Ordering** → T4(a): STARTED; item 0 = run item 7's process check, then Trading Hours under Could not do (or item 0's STOP path unchanged if NT8 is not running); item 0a = T4 same-user check; items 1–9 (item 7 pastes the same output or a re-run); item 10 = T6 GET; then the self-report. T4(b): NT8 not running → item 0 STOP path governs; item 0a still gives `whoami` and Documents, owner "could not read: NT8 not running"; items 1–10 answered; RESULT STOP, FINISHED, wait.
- **(ii) Skills directory** → T1(c): exactly one SKILL.md copy in step 2 and one in step 4, into the skills directory reported in step 1 item 2; source = Mac copy `vm/skills/<name>/SKILL.md` (T3); nothing else outside `vm/replies/` on the Mac. I added "if a file of that name is already there, STOP; do not overwrite" (noclobber spirit) — **not in the brief; manager may strike.**
- **(iii) Handoff-wins/STOP** → T1(b): differences in this reply are intended, Amendment 3 makes them part of the handoff, not by themselves a reason to STOP; Hermes names each it relied on in its end-of-run message; any other disagreement keeps the skill's rule.
- **(iv) Item 1** → T1(a): Hermes gives its own identity, says it is not the settlement-3 agent, cites this reply.
- **(v) Item 8 vs T4** → T4(d): answered once; the other item cross-references.

## Other conflicts found
- **(vi) Z: paths inside the two VM skills.** `praxis-nt8-bridge-backtest` has `certutil -hashfile Z:\ninjascript\...` and says "If this skill and the handoff's step 4 disagree, STOP and reply; do not choose." Resolved in T3(a): the swap applies to both skills too, so skill and step 4 do not disagree on it. (Added by me; flag.)
- **(vii) Fresh PowerShell per call.** The skill's helper opens a fresh PowerShell each call, so `$D` from `praxis-vm-reporter` command 1 does not carry to commands 2–4; that skill says "Type these by hand" and test 2b requires commands "exactly as typed". Resolved in T3(b): prefix `$D = ...;`, paste as sent, wrapper included; Code and praxis-auditor judge 2b against what was sent. (Added by me; flag. Whether that still meets 2b's format criterion is for Code and the auditor.)
- **(viii) Step 4.3 "as Amear decides".** The go-2a reply is still required by step 4 gate (b); T2(e) keeps it and leaves the skill's screen rule in force in step 4 until go-2a says otherwise.
- **(ix) Step 3.3.** The handoff has the VM agent paste Amear's words when he says he compiled; T2's "Amear's screen reads reach Code from Amear" could be read against that. T2(d) keeps 3.3's own path.
- **(x) Not resolved (harmless):** `<ts>` — handoff uses PowerShell's UTC form, the skill uses the Mac's `date -u +%Y%m%dT%H%M%SZ`; same format. Skill's fixed WRITTEN-BY version string is UNVERIFIED; §7 asks for "your identity, as in step 1".
- **(xi) T4(c) mismatch path** (answer the rest read-only, RESULT STOP, FINISHED, no step 2) is my choice following item 0's pattern; the brief said only "STOP". Flag.
- **(xii) Loopback address.** `127.0.0.1` appears 3 times in added text: in T6 (required by the brief) and in Amear's verbatim quote. No other IP, no key path, no fingerprint (scan below). The handoff's own :8 carries a LAN address; I cite only its line number, not its text.
- **(xiii) Uncommitted citation.** DECISION_LOG.md:813–814 exist only in the working copy (HEAD has 810 lines, below); D-2026-11-10-C says so. The commit should carry DECISION_LOG through :814 for the citation to resolve.
- Handoff line refs in D-2026-11-10-C (:23, :91, :125, :241) are post-Amendment-3 numbering.

## Verification evidence (pasted command output)
Run in `/bin/bash --noprofile --norc` from the repo root (a zsh `grep` wrapper on this Mac adds xtrace noise). `$SP` = the session scratchpad `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad`; `$D` = `$SP/CODE-vm-agent-hermes.draft.md`. `$SP/s13.txt` holds the S13 sentence (copied from handoff :9, standing-limitation line, prefix stripped by `sed`), so the counts below use `grep -cFf` and the sentence is not repeated here. `$SP/scan.txt` holds the IP, key-path, key-name and fingerprint patterns for the last scan, kept out of this public file. `decisions.before`, `manifest.before`, `handoff.before` are `cp` copies taken just before each edit; `amear-quote.txt` is the scripted extract from DECISION_LOG.md:813.

```
$ wc -c < $SP/s13.txt
      91
$ git diff --numstat -- vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md
25	0	DECISIONS.md
14	0	MANIFEST.md
1	0	vm/2026-11-06-vm-handoff.md
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-<rep>-reply.png
$ head -4 $D
REPLY-TO: Amear's 2026-11-10 proposal (DECISION_LOG 2026-11-10T20:42:00Z, WHO: amear) and Z:\vm\2026-11-06-vm-handoff.md §0 settlement 3
WRITTEN-BY: Claude Code on the Mac (praxis-master, through unit 2026-11-10-vm-agent-hermes-ssh)
UTC: __TS__
RESULT: DONE
$ grep -n "Amendment 3" vm/2026-11-06-vm-handoff.md | cut -c1-120
23:- **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-
$ grep -cFf $SP/s13.txt $SP/CODE-vm-agent-hermes.draft.md
1
$ grep -cFf $SP/s13.txt vm/2026-11-06-vm-handoff.md
1
$ grep -cFf $SP/s13.txt DECISIONS.md
34
$ grep -cFf $SP/s13.txt MANIFEST.md
0
$ git diff -U0 -- vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md | grep "^+[^+]" | grep -cFf $SP/s13.txt
1
$ tail -1 $D | grep -cxFf $SP/s13.txt
1
$ tail -1 DECISIONS.md | grep -cxFf $SP/s13.txt
1
$ grep -n __TS__ $D vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md | sed "s|$SP/|\$SP/|" | cut -c1-110
$SP/CODE-vm-agent-hermes.draft.md:3:UTC: __TS__
$SP/CODE-vm-agent-hermes.draft.md:8:none. Code typed no command on the VM and did not connect to it. This repl
vm/2026-11-06-vm-handoff.md:23:- **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over
DECISIONS.md:2087:**What it decides.** The VM agent for every step of `vm/2026-11-06-vm-handoff.md` is Hermes,
MANIFEST.md:364:| /vm/replies/__TS__-CODE-vm-agent-hermes.md | Reply | 3 | 2026-11-10 | CODE- reply for unit 2
$ grep -o __TS__ $D | wc -l
       3
$ wc -l DECISIONS.md MANIFEST.md $D
    2099 DECISIONS.md
     369 MANIFEST.md
      61 /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/af9aea76-b226-4610-b3fb-538269d1a642/scratchpad/CODE-vm-agent-hermes.draft.md
    2529 total
$ git show HEAD:DECISION_LOG.md | wc -l
     810
$ sed -n 2082p DECISIONS.md | tr -d "\n" | shasum -a 256
d68a240074835bdb1027cd41d7caa6293360387d2c8c460a577d43ae1e3b8bda  -
$ shasum -a 256 < $SP/amear-quote.txt
d68a240074835bdb1027cd41d7caa6293360387d2c8c460a577d43ae1e3b8bda  -
$ cmp <(head -2074 DECISIONS.md) $SP/decisions.before && echo LINES_1_2074_IDENTICAL
LINES_1_2074_IDENTICAL
$ cmp <(head -363 MANIFEST.md) $SP/manifest.before && echo MANIFEST_1_363_IDENTICAL
MANIFEST_1_363_IDENTICAL
$ diff $SP/handoff.before vm/2026-11-06-vm-handoff.md | cut -c1-90
22a23
> - **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from
$ { git diff -U0 -- vm/2026-11-06-vm-handoff.md DECISIONS.md MANIFEST.md | grep "^+[^+]"; cat $D; } | grep -oEf $SP/scan.txt | sort | uniq -c
   3 127.0.0.1
```

Reading of the counts: MANIFEST's numstat 14 = 8 pre-existing uncommitted rows + my 6. The handoff's S13 count 1 is its pre-existing §0 line; my bullet adds none. DECISIONS.md's 34 = earlier entries + D-2026-11-10-C's one (added-text count 1). The draft holds `__TS__` 3 times (UTC line; twice in line 8 where it names itself). The only IP-like string is the loopback `127.0.0.1` (T6 and Amear's quote).

## Files staged
None by me. Working-tree changes: `vm/2026-11-06-vm-handoff.md` (+1), `DECISIONS.md` (+25), `MANIFEST.md` (+6 of its +14), this report (new). The draft is in the scratchpad only. Real index still holds only the PNG (above).

## Result: PASS
All five deliverables written. Open flags for the manager: (ii)'s added no-overwrite STOP, (vi), (vii), (xi), (xii), (xiii).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
