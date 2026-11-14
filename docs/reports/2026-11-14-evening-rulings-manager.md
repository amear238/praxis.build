# 2026-11-14 evening-rulings: manager report (filed by praxis-master from the manager's inline return)

Filer's note (praxis-master, 2026-11-14T02:0xZ): the praxis-manager for unit `2026-11-14-evening-rulings` could not write this file. Its Write tool refused it with "Subagents should return findings as text, not write report files", and it returned the report inline in its final message. The master copied that inline return below. Apart from this note and the title line, the content is the manager's. The master edited no figure, pointer or result in it.

Result: BLOCKED: manager report file `docs/reports/2026-11-14-evening-rulings-manager.md` not written (tool-refused); its content is returned inline. The entries and the staging are complete and adversary PASS.

## Task
Two entries appended at the end of DECISIONS.md:
- **D-2026-11-13-D:** Amear's five evening rulings, filed WHO: amear, REPORTED BY the Claude.ai channel.
- **D-2026-11-13-E:** the contender bar and overfitting guard, PROPOSED BY the Claude.ai channel, adopted by the master under D-2026-11-08-D D1, changeable by Amear, and not his ruling.

The final text (160 lines) is at `/tmp/praxis-rl/entries.md`, working-tree DECISIONS.md :2458-:2617, and blob :2366-:2525. The uncommitted D-2026-11-12-B block was not touched. MANIFEST.md, the real index and every bead are untouched. Nothing is committed.

## Rubric criteria addressed
S1, S2, S4, S5, S6, S8, S13. F3 and F4 are cross-checked only; neither is claimed cleared.

## Workers dispatched
| id | mode | outcome |
|---|---|---|
| first two dispatches | BUILD | Hit the 40-turn limit with no report; re-split into the four below |
| worker1 | BUILD | Ruling 1: where the old research screen is written |
| worker4 | BUILD | Ruling 2: 57 beads classified |
| worker5 | BUILD | Rulings 4 and 5; found 5 handoff-vs-record mismatches |
| worker2 | BUILD | Walk-forward spec and values vs the bar |
| worker6 | BUILD | F3/F4, 4uu, fgd, ckh, D7, drawdown gate, commission |
| worker3 | ADVERSARIAL | FAIL: 1 blocking, 5 minor; all fixed |
| worker7 | ADVERSARIAL | PASS; 7 minor, all fixed |
| worker8 | ADVERSARIAL | FAIL, because HEAD moved; rebuilt on the new HEAD; 3 minor fixed |
| worker9 | ADVERSARIAL | PASS; 1 minor S2 point, fixed afterwards and checked by me only |

## Process log
- **IDs:** HEAD's last entry is D-2026-11-13-C, and `git grep -n -E 'D-2026-11-13-[DE]' HEAD | wc -l` gives `0`. The only other file naming D/E is the master's own resume handoff (`docs/reports/2026-11-14-hermes-resume-0400.md` :41, :67), which points at this unit.
- **Citations:** all four handoff citations (:1010, :1551-:1555, :1735-:1740, :2076) say what the handoff claims, so there was nothing to stop for. The :2076 heading is quoted inline in backticks so it cannot be parsed as an entry heading.
- **My own re-checks corrected three citations:** the window design is at values :82 (not :85), D7's sentence is at :1943-:1944, and the OppBand entry times run from 10:01 to 11:31.
- **Adversary fixes:**
  - The blocking one: D's Status no longer credits rulings (1)-(5) to Amear. Only his quoted words are his; the numbered wording is the channel's.
  - Reading "go from here" as approval of filing the rulings is labelled as the master's reading from row :944.
  - The inference that row :942 item (3) covers the skip list is labelled INFERRED.
  - The timer is labelled as REPORTED BY the master, not observed.
  - The pointers to the unwritten manager report were replaced with worker2, worker5 and worker6 report paths.
- **HEAD moved:** another unit committed `b1815d2` (MANIFEST plus 15 reports, including the handoff; DECISIONS.md unchanged). I rebuilt the blob and index on `b1815d2`, and updated the entry to say the handoff is committed there, byte-identical to the copy I quoted.

## Verification evidence (pasted output, final version)
```
b1815d2bb8d9df74f94f262a4cdaa1a2f5da8767   (HEAD = origin/main)
WT-APPENDED-EXACTLY-ENTRIES
WT-PREFIX-UNCHANGED
HEAD-PREFIX-OK
WT-TAIL-EQUALS-BLOB-TAIL
M	DECISIONS.md
160	0	DECISIONS.md
f1d1db1ca1b747f51b0059553c01d19cfb34c3dcc0556b94c0e350556547a83c  -
100644 b11ecfd9caa8bfe40a1fc567878f9b33dc2d81b7 0	DECISIONS.md
b11ecfd9caa8bfe40a1fc567878f9b33dc2d81b7
       0      (git grep D-2026-11-13-[DE] HEAD | wc -l)
rep-name: 0
92 / 160      (S13 line numbers: last line of D, last line of E)
handoff 9p MATCH / 13,15p MATCH / 41,45p MATCH / 67,69p MATCH / 71,88p MATCH
HEAD DECISIONS 1010p MATCH / 1551,1555p MATCH / 1735,1740p MATCH; inline :2076 count 1
```
- **Ruling 1 hits:**
  - `git grep -n -i -E 'peer.?review|post-2018|after 2018' HEAD -- DECISIONS.md specs docs/specs | wc -l` gives `0`.
  - The filter audit :57 ("Post-2018 / algo-impact survival") and :58 ("Source tiering (peer-reviewed or institutional; no course sellers)") are both PROPOSED (:4).
  - The `Redemtion/` folder is gitignored (`.gitignore:7`): the 2026-04-30 plan :53 and the 2026-05-06 prompts :47-:48.
  - The quoted phrase "peer-reviewed evidence on NQ" appears only in the voice handoff :62 and the handoff :41.
- **Negative tests:** a one-byte change in a scratch copy tripped the quote-match check (`MISSING`) and the tail diff (`differs`). A two-path name-status sample failed the single-path check.

## Adversarial findings
Record-level findings written into D, recorded and not repaired:
- "every brief since April" overstates the record.
- The handoff's "dispatched by Hermes over SSH as on 2026-11-13" is unsupported; the 11-13 results came from "the VM Claude Code session" (vm-queue results :5).
- The 1,173-trade hand-run reference has no primary record in the repo.
- Flat1559 has no 09:30 run.
- Test 2a's 1,190-trade reference is one of the baselines R1 calls suspect, if Amear's 08:30 account holds.

## S6 cross-block check
- **Walk-forward spec and values (HEAD):**
  - Both cover only the Noise-Area arms. The pause stops zi1, ajj and xdr.
  - The bar is weaker than the Block 2 gates: PF 1.10 against OOS PF ≥ 1.30, and 200 trades against ≥ 250. It has no Sharpe gate, and a variant cap stands in for PBO.
  - A later 252/63/63 walk-forward would reuse both the tuning span and the held-out span as OOS data.
  - Spec :31 and values :124 still say 4%, from before A4.
- **D7 and ckh:** ckh is PARKED ("A human resumes"), while handoff :111 makes its two ideas loop candidates. That conflict is named, not resolved. Whether D7's "continues through the VM tests" survives the pause is also open.
- **fgd:** its `_Flat1559.cs` and breaker items pause; its spec-text items are UNCLEAR.
- **F3 is FROZEN and is NOT claimed cleared.** It blocks "`4uu`. Everything downstream of `4uu`." Ruling 2 pauses 4uu, which is in progress. Whether the loop's new-strategy backtests are downstream of 4uu is an **open question for Amear**.
- **F4:** it blocks Blocks 4 and 5; nothing here touches either.
- **Also named:** the commission mismatch ($4.68 is the NQ rate, while drawdown is measured at 1 MNQ, where the rate is $1.90). A4 checks every tier, while the bar needs one account size. There is a tension between the :1010 ruling and Hermes as the VM agent. All three are left for Amear.

## Files staged
Temp index `/tmp/praxis-rl/idx` on HEAD `b1815d2`: `M DECISIONS.md` only.

## For the master
- The entries cite `docs/reports/2026-11-14-evening-rulings-worker2.md`, `-worker5.md` and `-worker6.md`. They are untracked, and the temp index holds only DECISIONS.md, so they need filing with MANIFEST rows, which another manager owns.
- Worker reports 1-9 are untracked as well.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
