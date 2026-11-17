# Unit 2026-11-11-hermes-replies-grading — manager report

Date: 2026-11-11. Repo HEAD at start: 85a803f (branch main). Manager: praxis-manager. Nothing staged, nothing committed.

## Summary

Grades are worker 1's, recounted by the manager (E6), re-run in part by the manager (E1-E5) and in part by adversarial worker 2 (see Adversarial findings). "N/A" = NOT APPLICABLE; "not on disk" = NOT ASSESSABLE FROM DISK (things like the T5(a) pre-check or the end-of-run message to Amear, which leave no trace in the files).

| Reply file | Items asked | Done | Not done | N/A | Not on disk |
|---|---|---|---|---|---|
| `vm/replies/20261110T214542Z-STATUS.md` (STARTED) | 10 | 4 | 0 | 4 | 2 |
| `vm/replies/20261110T214834Z-self-report.md` (step 1) | 42 | 30 | 3 | 2 | 7 |
| `vm/replies/20261110T224920Z-2b-skill-job.md` (step 2) | 28 | 18 | 3 | 1 | 6 |
| `vm/replies/20261110T215014Z-STATUS.md` (FINISHED) | 13 | 5 | 1 | 4 | 3 |

Overall grade of what Hermes did, in plain English: Hermes did the substance of steps 1 and 2. It wrote STARTED first and FINISHED last (by write time). It ran the same-user check, which showed the SSH user and the NinjaTrader owner are the same Windows account. It ran the one healthz GET, which returned status 200 with `{"status":"ok"}`, and it did not judge the result. It put both screen reads under Could not do with the exact reason text. It copied the six step-0 answers word for word, and it copied the skill byte-identical into its skills folder. It missed the bookkeeping that the CODE- reply added. Neither content reply states the Z:-to-Mac swap in `## Commands typed` (T3). Neither says which clock its timestamp came from (T3(c)). Item 8 is answered twice (T4(d)). The 2b reply is named from the VM clock, which reads about an hour ahead of the Mac, so by file name it sorts after FINISHED. On S2, two things go beyond the evidence: "Could not do: none" sits over an empty AddOns output block, and every VM output is Hermes's own typing, not a capture Code has seen. Seven items are NOT DONE. None of them breaks a §1 hard limit, as far as the disk shows.

Note on numbering: the master's brief named "T3 same-user check" and "T2 Z: swap". In the CODE- reply itself, T2 is screen reads, T3 is "Z: is the Mac folder" (the swap statement, and T3(c) the ts source), T4 is the same-user check (item 0a), and T6 is healthz. This report grades by the reply's own numbering.

## Task

Grade the four untracked files Hermes wrote on 2026-11-10 item by item against the handoff (steps 1 and 2, §1 limits, §7, Amendment 3 at `vm/2026-11-06-vm-handoff.md:23`) and the CODE- reply's terms T1-T7. Compare every UTC stamp with the file mtimes and with the VM clock reads the replies carry. Record the step 2 facts about the VM. Flag personal data. Have one adversarial worker re-run at least five checks. Append MANIFEST rows. Everything stays read-only on the Mac apart from the reports and MANIFEST.md. Nothing on the VM, no SSH, no Hermes, nothing staged.

## Rubric criteria addressed

- S1: every claim below rests on a pasted block in Verification evidence (command output), or on a named block in a worker report.
- S2: every VM output is graded REPORTED BY Hermes. Code observed only the Mac files' bytes and metadata. Clock conclusions are labelled OBSERVED or INFERRED.
- S6: see S6 cross-block check.
- S13: the S13 sentence is the last standalone line of every report in this unit, once (E9).

## Workers dispatched (id, mode, outcome)

(filled at end)

## Process log

1. Read the rubric (S1, S2, S6 and S13 at `specs/SPEC_RUBRIC.md:124`, :125, :129 and :136), the four reply files, the CODE- reply, the handoff's §0, §1, §2, §3, §4 and §7, and the reporter skill. Wrote this report's skeleton before dispatching anything.
2. Dispatched worker 1 (BUILD, foreground) with the item list, the T-numbering correction, and read-only scope. Its permitted reads under `/Users/admin/.hermes` were limited to the one skill directory.
3. On its return: read its grade tables (worker 1 report lines 25-240), not only its summary. Re-ran the timestamp differences, the skill-copy hash and birth times, the T2(a) reason text, the item 9 diff, the swap/ts-source search, the personal-data scan, the host-name tracked count and the NT8 StartTime arithmetic (E1-E5). All reproduce.
4. Re-counted worker 1's grade table with `grep -c` (E6). The counts match its own. A first recount with a zsh `echo "$rows" | wc -l` overcounted A and D by one each, because zsh's `echo` expands the literal `\n` in rows A1 and D1. That was a defect in my command, not in the report, and `grep -c` replaced it.
5. Negative tests (E3): the swap-statement grep hits the CODE- reply 4 times, so its exit 1 on the two Hermes replies is not a dead pattern. The S13 count check prints 0 on a file without the sentence. noclobber refuses to overwrite (tested on a /tmp copy, hash unchanged).
6. S6: looked for Code activity inside Hermes's STARTED-to-FINISHED window (E7). Found DISPATCH_LOG:2453.
7. Checked worker 1's memory-file slip (E8).
8. Dispatched worker 2 (ADVERSARIAL, background). It was given the sources and criteria, and told to form its own view before reading worker 1's tables, then to re-run at least five checks and challenge generous grades.

## Verification evidence (command output)

(filled at end)

## Adversarial findings

(filled at end)

## S6 cross-block check

The approved deviation is D-2026-11-10-C: Hermes over SSH as the VM agent. It was tested here against the blocks it touches outside its own CODE- reply:

1. **Handoff §1 limit 11 and T5 (one-session rule): Code side.** T5 says "Code dispatches nothing in that window". The window runs from STARTED (name 21:45:42Z, mtime 21:46:36Z) to FINISHED (name 21:50:14Z, mtime 21:50:17Z). Evidence, all OBSERVED (E7): no commits fall inside 21:00Z-23:00Z. DECISION_LOG:818 records the master's session close at "21:47Z (estimated; no `date -u` read)", and that row says "From that marker on, Code dispatches nothing until FINISHED (T5)". DISPATCH_LOG:2453 records a hook-written `SubagentStop` at **2026-11-10T21:50:16Z**, inside the window and one second before FINISHED's mtime. It carries an unmatched token, and no spawn row exists for it. INFERRED: a Code subagent was still running, or ended, inside Hermes's window. When it was spawned is not recorded, so whether Code *dispatched* inside the window is not settled. This is a finding about Code's side of T5, not about Hermes. It is left to the master.
2. **Handoff §1 limit 10 (writes).** The one write outside `vm/replies/` is the SKILL.md copy at `/Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md`. Its hash equals `vm/skills/praxis-vm-reporter/SKILL.md`, and the directory and file share birth time 21:49:07Z (E2, OBSERVED). That fits T1(c)'s "exactly one file". Writes elsewhere on the Mac or on the VM were not inspected (scope).
3. **Handoff §1 limit 3 (D-071, no connection changes) and limit 4 (bridge commands).** None of the 13 VM commands the replies list is a connect, reconnect or bridge command (worker 1 E13). Level: REPORTED BY Hermes; what was actually sent is not on disk.
4. **Block 3 / F1 live-signal topology (D-2026-11-10-B, DECISIONS.md:2047) and OPEN-T1.** The healthz GET from the VM returned 200 `{"status":"ok"}` (REPORTED). Per T6(a), that does not settle OPEN-T1, because an SSH PowerShell session is not an NT8 strategy and `/healthz` is not the webhook. Neither this report nor the replies observe whether that 127.0.0.1:5678 listener is the Mac's n8n through the tunnel or something on the VM itself. One sentence, as asked: the result shows that something answered on the VM's loopback port 5678; no design conclusion follows.

## Personal data and commit-safety flags (for the master)

- **Windows machine host name** (a `DESKTOP-` name) on self-report lines 64, 68 and 71. It is in **0** tracked files today (E4). Worker 1's report quotes it on 15 lines (E4), and worker 2's report may quote it too. Committing either the self-report or those worker reports would put it in git for the first time. Whether that is acceptable is the master's call. The reply files were not edited.
- No IP address other than `127.0.0.1` (E4: the only other dotted-quad hits are the NT8 version `8.1.8.4`). No key path, fingerprint, credential or token (E4).
- Third-party names: the model name `gemini-3.8-flash` (self-report :2, :11; 2b :2), and "Microsoft Store" inside the pasted Python error text (self-report :75). No person other than Amear. The SSH alias `praxis-vm` is already committed (worker 1 E22).
- Windows user `amear` and Mac paths under `/Users/admin/`: acceptable per brief, noted only.
- Scope slip by worker 1: it wrote an agent-memory file and an index line, outside its report-only limit, then deleted both (its own return). `.claude/agent-memory/` is git-ignored (`.gitignore:26`), so git status cannot show this. Its index `MEMORY.md` was modified today at 16:12:48Z, has 10 lines, and contains no `hermes` or `2026-11-11` line (E8). That the index is byte-identical to its earlier state is UNVERIFIED, because no baseline was taken. Nothing tracked was touched.

## Files staged

None. This unit stages nothing; the master decides.

Result: (pending)

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
