# Hermes replies grading — worker 4 (ADVERSARIAL on the worker 3 revision)

## Task

MODE: ADVERSARIAL. Unit 2026-11-11-hermes-replies-grading, worker 4. Artifact: `docs/reports/2026-11-11-hermes-replies-grading-worker1.md` (W1 below) as revised in place by fix worker 3 (its section "## Fix log (worker 3, 2026-11-11)"). Job: check whether the revision resolves W2-1..W2-7 (worker 2's report, section "## Result", lines 318–332 only, printed in V1); check fix-log claims S1 (a)–(c); re-run the per-file counts; look for grades the revision left too generous or made inconsistent; sample rows not named in the fix log; check the S13 line. Read-only on the Mac. Nothing was run on the VM, no ssh, no Hermes. Nothing staged; the git commands in V11 run with `GIT_OPTIONAL_LOCKS=0` so they do not refresh the index. This file is the only file written. Every evidence block (V0–V14) was produced by the `run` function printed in V0: it prints `$ ` plus the command string, then `eval`s that same string with stderr merged. V0–V13 came from one `/bin/bash -s` call; V14 from a second call that defined the same function and prints its definition again. Source line citations: handoff = `vm/2026-11-06-vm-handoff.md`, CODE- = `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md`, SKILL = `vm/skills/praxis-vm-reporter/SKILL.md`, B = the self-report, C = the 2b reply, W1:n = line n of the artifact.

## Rubric criteria addressed

- S1 (every claim has pasted command output; unit rule: each block shows the exact command as run, no placeholders, and its raw output). This file: every verdict below cites a V block. The artifact: checked in "Fix-by-fix verdicts" S1 (a)–(c) and W4-6.
- S2 (no component reported above its evidence). Checked row by row for the seven W2 items and for rows not in the fix log; findings W4-1 to W4-5.

## Fix-by-fix verdicts

| Item | Revised row(s) | Verdict | Basis |
|---|---|---|---|
| W2-1 | B7 (W1:59) | RESOLVED, with an evidence error (W4-5) | NOT ASSESSABLE FROM DISK now quotes handoff:311 in full ("every command, exactly as typed", V3) and ties to B42. The grade fits: whether B:19's "Read directly from vm/..." was a typed command or a file-read tool is not on disk. But the row also lists the Mac-side skill copy (2b:36) as a command missing from B's `## Commands typed`. The copy's birth time 21:49:07Z is after B's write at 21:48:54Z (V7), and it belongs to step 2, so it cannot be missing from B |
| W2-2 | B17 (W1:69) | OVER-CORRECTED (W4-1) | NOT DONE "OBSERVED" rests on reading CODE-:47 "Before step 1 item 1, as a new item in the self-report" as a position in the file. That reading is not marked, and the ASKED cell adds the gloss "— placement of item 0a in the file", the same kind of insertion W2-2 objected to ("run"). The same reply's very next term, T4(a) (CODE-:48, V4), is headed "Step 1 order for Hermes" and orders (2) item 0, (3) "Item 0a, this check", (4) "Items 1–9". That reads "before item 1" as an order of actions. The T4 sentence's object is a list of commands (`whoami`; owner; Documents path), and §7 lays out a reply by section, not by item (handoff:310–314, V3). Inside `## Commands typed` and `## Output`, item 0a is command 2, ahead of every item 3–8 command (V6). The file positions are OBSERVED; what T4 asks is a READING. The level the source supports is: both readings printed and the grade marked READING (or OPEN), with the action-order reading already covered by B19 |
| W2-3 | B36, B37 (W1:88–89); S2 item 2 (W1:165) | RESOLVED; the dependent C27 is not (W4-3) | Both rows OPEN — FOR THE MASTER. The literal text is cited (handoff:37, :27, :23, V3). Reading A is printed as not a grade. S2 item 2 and Result (W1:1119, :1129) agree (V2, V12) |
| W2-4 | C13 (W1:114) | RESOLVED | NOT ASSESSABLE FROM DISK, citing S2 item 3. C:20–21 is an empty fence pair (V2 row text; the source line is SKILL:40 "each item and why, or `none`", V5) |
| W2-5 | C18 (W1:119) | RESOLVED | NOT ASSESSABLE FROM DISK because C11 and C22 are NOT ASSESSABLE (V2) |
| W2-6 | A2a, A2b (W1:38–39); also B20 (W1:72) | NOT RESOLVED (partly) (W4-2) | A2b fixes limit 11's "before your first step". A2a still grades handoff:93 "Write ... `STARTED` first" and T4(a)(1) DONE on file order only. To do so its ASKED restates them as "STARTED written before every other Hermes file". handoff:93 is the line before "Report each item below" (handoff:95, V3), and T4(a) puts "(1) Write STARTED" before "(2) Item 0: run item 7's process check" (CODE-:48, V4). Both are action-order requirements, the same unknown as A2b. File order is a necessary condition, not the requirement. B20 grades the same T4(a)(1) DONE the same way. W2-6's core objection ("backed by file order only") still applies to A2a |
| W2-7 | B43 (W1:95); B44 (W1:96) added under it | B43 RESOLVED; B44 too generous (W4-4) | B43: limit 3 quoted from handoff:31 ("Do not start, close or restart NinjaTrader", "Starting it is Amear's", V3) with handoff:106. NOT ASSESSABLE FROM DISK — ESCALATE TO MASTER. The adverse scenarios match the E19 table (my arithmetic: 17:46:59 local at −05:00 is 22:46:59Z, minus +1 h is 21:46:59Z, 23 s after STARTED's 21:46:36Z, V7). B44: see W4-4 |

Fix-log S1 claims:

- S1 (a), W1:5. RESOLVED. The staged-state claim cites E25, which pastes `git status --porcelain -- vm docs/reports` and the repo-wide `git diff --cached --stat`, with exact commands. My re-run (V11) gives the same one staged path, the PNG at 254350 bytes, and HEAD `85a803f`. The "no other file written" part is labelled the worker's own statement.
- S1 (b), W1:21 and :249. PARTLY RESOLVED (W4-6). For E1–E24 the claim is reworded honestly: the script is not pasted. For E25–E29, W1:21 says they "were produced by the `run` function whose definition is pasted with them". W1's own E27 preamble says that for E26/E27 the second definition "was not printed" (V12). E29 carries no definition (V12 count 0). In E25 and E28 the `run ()` text appears with no `$` command line that produced it.
- S1 (c), W1:29–31. RESOLVED in form: the scope decision is now a READING resting on SKILL:11 and limit 11's wording (V5, V3), and the other reading is named. Note, not counted: the counter-reading has support the decision does not weigh. handoff:301 "Every reply is a Markdown file in `Z:\vm\replies\` named `<ts>-<slug>.md`" (V3) fits `<ts>-STATUS.md`. SKILL:11 is the step-2 skill, and its "this one reply file" is the 2b reply, so it separates STATUS files from that one reply, not from replies in general. Eight NOT APPLICABLE grades (A6–A9, D9–D12) rest on this reading. The report labels them READING, so this is not an S2 break.

## Counts re-run

V9 counts rows that start `| A`, `| B`, `| C` or `| D`, followed by a number and an optional `a`/`b`, by `/usr/bin/grep -c` per grade (the ` — ESCALATE TO MASTER` suffix is counted under its base grade). Result: A 11 = 4/0/4/3/0; B 44 = 29/4/1/8/2; C 28 = 16/3/1/8/0; D 13 = 5/1/4/3/0 (done / not done / n.a. / not assessable / open). That equals the report's table (W1:153–156, printed in V9) and its Result line (W1:1127). Every row's grade cell is one of the five grades (V9: 0 others), and every row has exactly 4 cells (V9: 0 malformed). So the counts are consistent with the rows as written. If W4-1 to W4-4 are accepted, the counts change: A2a, B17, B20, C27 and B44 move.

## Further findings

- W4-1 (W2-2 over-corrected). See the W2-2 row. B17 `NOT DONE` is graded at OBSERVED level on an unmarked reading of CODE-:47, and its ASKED cell carries an inserted gloss. Harsher than the source supports.
- W4-2 (W2-6 partly unresolved; too generous). See the W2-6 row. A2a DONE and B20 DONE grade handoff:93 / T4(a)(1) ("STARTED first", before item 0's process check) on file order alone. The action order is not on disk (A2b's own finding).
- W4-3 (too generous, left in place). C27 (W1:128) `NOT APPLICABLE`, "READING as B36: step 2 needs neither python nor git". B36 is now OPEN — FOR THE MASTER, and the report says "A worker's reading may not clear a §1 hard limit" (W1:88) and "step 2 should not have run" on the literal text (V2). C27 still clears limit 9 for step 2 on that same reading. Result note 3 (W1:1134) discloses this, but disclosure does not change the grade. The grade the report's own rule supports is OPEN — FOR THE MASTER.
- W4-4 (too generous, new row). B44 (W1:96) `DONE` for limit 12. (1) The evidence does not test the claim. E26 greps for `breaker`, `#5` and `circuit`, which describe the breaker. The forbidden string is the breaker's source title, which DECISIONS.md:1142 says is "a medication brand name" (V8). A file holding that brand name without any of the three words would also give count 0. The four-file result may still be true: E1 prints every line, and E21's capitalised-word list shows no brand. But that is INFERRED from reading the text, not OBSERVED by E26, and the row does not cite it. (2) The ASKED is "anywhere", and the row grades DONE from four files. The same report splits that kind of universal elsewhere: D4 DONE / D5 NOT ASSESSABLE (W1:138–139), and C16 NOT ASSESSABLE (W1:117) (V2). The level the evidence supports is DONE (INFERRED, four files only) plus a NOT ASSESSABLE FROM DISK row for "anywhere" else.
- W4-5 (evidence error, grade unaffected). B7 (W1:59) cites "the Mac-side skill copy (2b:36 ...)" as not listed in B's `## Commands typed`. The copy's birth time 21:49:07Z is after B's write at 21:48:54Z (V7), and handoff:127 puts the copy in step 2.
- W4-6 (S1, fix-log claim (b) partly met). W1:21 says E25–E29 were produced by the `run` function "whose definition is pasted with them". For E26/E27 the definition was not printed (W1's E27 preamble, V12). For E29 none is shown (V12). The `run ()` text in E25/E28 has no command line showing how it was printed. That is a description of provenance, not a paste.

Rows not named in the fix log, sampled against the sources:
- B13 (T2(a) reason, exact). REPRODUCES: the required text is 70 characters, appears once quoted in CODE-:36, and appears after ": " on B:112 and B:113 (V10). DONE holds.
- B30 (item 9 word for word). REPRODUCES: diff of handoff:65–70 column 3 against B:20–25 with only the item labels stripped exits 0 (V10). DONE holds.
- C8 (commands 1–5 as typed). REPRODUCES: diff of SKILL:19–23 against C:8–12, with the T3(b) wrapper removed from lines 2–4 only, exits 0 (V10). DONE holds.
- B20 (T4(a)(1) and (6)). Too generous on the (1) half: see W4-2.
- C24 / D3 (name order NOT DONE). Defensible. handoff:317 says "Files expected, in order" (V3) and the names sort out of order (V7). Whether "in order" means name order is a reading, but the row states the observed fact. Not counted.

S13 line of the artifact: the two-halves sentence occurs once, on line 1167, and `tail -1` equals it (V13). E29's "1158" figures are labelled as pre-paste.

## Verification evidence (command output)

### V0 — definition of the run function used for V0–V13 (one /bin/bash -s call)

~~~~text
$ declare -f run
run () 
{ 
    printf '$ %s\n' "$1";
    eval "$1" 2>&1
}
~~~~

### V1 — worker 2 Result section, the seven defect lines (first 120 characters)

~~~~text
$ sed -n '318,332p' /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker2.md | /usr/bin/grep -E '^- W2-[1-7]:' | cut -c1-120
- W2-1: B7 DONE should be NOT ASSESSABLE FROM DISK. "Every command" is a completeness claim, the ASKED column was narrow
- W2-2: B17 NOT ASSESSABLE should be NOT DONE (OBSERVED). T4 asks for placement "Before step 1 item 1 ... in the self-re
- W2-3: B36 NOT APPLICABLE and B37 DONE rest on a worker's own reading that adds a condition to §1 limit 9. Handoff:23 s
- W2-4: C13 DONE contradicts worker 1's own S2 item 3 (W1:111 vs W1:161). It should be NOT ASSESSABLE. Mitigation: the r
- W2-5: C18 DONE sits above its own NOT ASSESSABLE parts C11 and C22 (W1:116 vs W1:109, W1:120).
- W2-6: A2 DONE is backed by file order only. Limit 11's "before your first step" is not on disk, and the 54 s gap betwe
- W2-7: There is no graded row for §1 limit 3 / handoff:106. Worker 1's own E19 (extended in V5) places NT8's start 10–5
~~~~

### V2 — artifact rows and prose lines cited (W1:n)

~~~~text
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker1.md; for n in 38 39 59 69 71 72 88 89 95 96 114 116 117 119 128 138 139 165 1127 1134; do printf "W1:%s: " $n; sed -n "${n}p" "$F"; done
W1:38: | A2a | handoff:93 "Write ... `STARTED` first"; T4(a)(1) (CODE-:48, E4): STARTED written before every other Hermes file | DONE | E17: by mtime A 21:46:36Z is before B 21:48:54Z, C 21:49:56Z and D 21:50:17Z. By name, 214542Z sorts before every other Hermes file. OBSERVED |
W1:39: | A2b | Limit 11 (handoff:39, E2): STARTED written "before your first step" | NOT ASSESSABLE FROM DISK | The name stamp 21:45:42Z is 54 s before the write 21:46:36Z (E18). No command in B or C carries a time of when it ran (E1, E13), so whether any VM command ran before 21:46:36Z cannot be told from disk. The adverse NT8 StartTime scenarios are in B43 |
W1:59: | B7 | §7 (handoff:311, E27): "`## Commands typed` — every command, exactly as typed." | NOT ASSESSABLE FROM DISK | "Every" is a completeness claim the disk cannot show: B lists 8 numbered commands at B:29–51 (E13), but whether these are all the commands run is not recorded, which is B42's own finding ("Whether anything else was done on the VM is not recorded"). Not listed: the Mac-side read of the handoff (self-report:19 "Read directly from vm/2026-11-06-vm-handoff.md §2 table:") and the Mac-side skill copy (2b:36 "Copied `vm/skills/...`"); `## Commands typed` (B:27–51) holds no `vm/`, `/Volumes` or `/Users` path (E27, count 0). T3 (CODE-:42, E4) puts the swap statement inside `## Commands typed`, so §7's "every command" and T3 together point at Mac-side reads belonging there; B34 grades the swap statement |
W1:69: | B17 | T4 (CODE-:47, E27): "Before step 1 item 1, as a new item in the self-report" — placement of item 0a in the file | NOT DONE | E27: `### Item 1: Identity` is at self-report:8; item 0a appears first at self-report:32 (command, "2. Same-user check (Item 0a):") and :62 (output). So item 0a is placed after item 1 in the self-report. OBSERVED. Execution order is a separate question, graded in B19 (NOT ASSESSABLE FROM DISK) |
W1:71: | B19 | T4(a)(2)–(5) execution order: item 0 → 0a → items 1–9 → item 10 | NOT ASSESSABLE FROM DISK | The listed order of commands 1–8 (B:29–51) agrees with T4(a). The order of execution is not recorded |
W1:72: | B20 | T4(a)(1) and (6): STARTED first, self-report written after | DONE | E17: A 21:46:36Z, then B 21:48:54Z. OBSERVED |
W1:88: | B36 | Limit 9 (handoff:37, E2): "Do not install anything else — not Python, not git ... If a tool is missing, STOP and report it." Python and git are missing (B:75, B:87) | OPEN — FOR THE MASTER | Literal text: NOT DONE. Limit 9 says "If a tool is missing, STOP and report it"; handoff:27 says "Every limit holds for the whole of this file"; handoff:23 says "no term relaxes a §1 hard limit" (E2). On that text B's RESULT should have been STOP, and step 2 should not have run. A worker's reading may not clear a §1 hard limit, so this report does not settle it. Reading A (worker 1, printed for the master, not a grade): the STOP is the alternative to installing and applies when a step needs the tool; step 1 item 5 asks for "the output, or the error. Step 3 needs git." (handoff:116), and steps 1–2 use neither tool, so no STOP was due before step 3. Reading B (literal): the STOP was due in step 1. Under either reading, B does not flag the missing tools as a step-3 blocker anywhere (E1, B:111–113). That gap is OBSERVED |
W1:89: | B37 | T2(a) (CODE-:36): items 0 and 6 "do NOT by themselves make RESULT STOP. If every other item is answered, step 1 may end DONE" | OPEN — FOR THE MASTER | Depends on B36. Items 1–5 and 7–10 are all answered (B21–B32), so T2(a)'s own condition holds. But T2(a) is a CODE- term, and handoff:23 says no term relaxes a §1 hard limit (E2). Under reading A of B36, `RESULT: DONE` (B:4) is allowed; under the literal reading B, it should be STOP |
W1:95: | B43 | §1 limit 3 (handoff:31, E27): "**Do not start, close or restart NinjaTrader.** ... Starting it is Amear's."; with handoff:106 (E27): "**NT8 must already be running.**" | NOT ASSESSABLE FROM DISK — ESCALATE TO MASTER | No file records who started NT8 or when Hermes's first VM command ran. Adverse indicator (E19, INFERRED arithmetic on REPORTED B:59 `9600 2026-11-10 5:46:59 PM`): under (zone −05:00, VM offset +1 h) and (zone −04:00, offset 0) the NT8 StartTime is 21:46:59Z, 23 s after STARTED's mtime 21:46:36Z, i.e. NT8 started after the session had begun; only (−04:00, +1 h) puts it before the session (20:46:59Z). The (−05:00, 0) and −06:00 rows put it after B's own mtime, which is impossible if B:59 is a real capture. The self-report lists no command that starts NT8 (E13: 8 commands, all reads; E27: no `Start-Process`, `Invoke-Item`, "launch" or "start NT8" line in the four files), and nothing on disk records who started it. The VM zone and clock offset are not known (Timestamps) |
W1:96: | B44 | §1 limit 12 (handoff:40, E27): "Never write the source title of circuit breaker #5 anywhere — not in a reply, not in a file name ..." | DONE | E26: `breaker`, `#5` and `circuit` each have count 0 in all four files, and the combined grep exits 1 (no line matches). The four file names (E17) contain none of them either. OBSERVED for the four files only; "anywhere" else (VM, notes, the rest of the Mac) was not inspected |
W1:114: | C13 | SKILL.md:40 `## Could not do` — "each item and why, or `none`" | NOT ASSESSABLE FROM DISK | C:39 `none` has the required form, but whether `none` is true depends on whether command 2 succeeded, and its output block is empty (C:20–21, E15). S2 item 3 finds that "`none` asserts more than the block shows", so the content of this section cannot be graded DONE from disk |
W1:116: | C15 | T1(c) (CODE-:33): "exactly one file ... If a file of that name is already there, STOP and reply; do not overwrite it" | DONE | E20: the directory holds only `SKILL.md`. The directory and the file both have birth 2026-11-10T21:49:07Z, so the directory was created at copy time and no earlier file of that name was there to overwrite (INFERRED from OBSERVED birth times) |
W1:117: | C16 | T1(c): "Nothing else is written outside `vm/replies/` on the Mac" | NOT ASSESSABLE FROM DISK | Only the one directory may be inspected (brief). The rest of the Mac was not checked |
W1:119: | C18 | Step 2.3 (handoff:129): "Perform the skill's job exactly as it is written" | NOT ASSESSABLE FROM DISK | Its parts are not all assessable: C8 (commands as typed) is DONE, but C11 (output pasted unedited) and C22 (record and stop if anything fails or looks different, for the empty command-2 block) are NOT ASSESSABLE FROM DISK. A whole cannot be DONE while two of its parts are not assessable. C:15–33 show outputs for all 5 commands: REPORTED |
W1:128: | C27 | Limit 9 in step 2 | NOT APPLICABLE | READING as B36: step 2 needs neither python nor git (C:8–12 are PowerShell built-ins) |
W1:138: | D4 | Nothing written after FINISHED — `vm/replies/` and the skill-copy directory, by mtime | DONE | E17 (D newest in `vm/replies/`); E20 (skill copy 21:49:07Z, before D 21:50:17Z). OBSERVED for those two directories only |
W1:139: | D5 | Nothing written after FINISHED — anywhere else (VM, rest of the Mac) | NOT ASSESSABLE FROM DISK | Not inspected (scope) |
W1:165: 2. B:4 `RESULT: DONE`. On limit 9's literal text (handoff:37, with handoff:27 and :23) it over-claims: RESULT should have been STOP. It is allowed only under reading A of B36, and a worker's reading may not clear a §1 hard limit. B36 and B37 are OPEN — FOR THE MASTER.
W1:1127: Per-file counts (asked / done / not done / not applicable / not assessable / open for the master): A 11/4/0/4/3/0; B 44/29/4/1/8/2; C 28/16/3/1/8/0; D 13/5/1/4/3/0 (E28, after fix worker 3's revision). Worker 1's pre-fix counts were A 10/4/0/4/2; B 42/30/3/2/7; C 28/18/3/1/6; D 13/5/1/4/3 (E24).
W1:1134: 3. (fix worker 3, found and not fixed: outside the brief's defect list) C27 grades limit 9 in step 2 NOT APPLICABLE "READING as B36". B36 is now OPEN — FOR THE MASTER, and under its literal reading step 2 should not have run at all, so C27 depends on the same open question. C27 and the Timestamps section were not changed.
~~~~

### V3 — handoff lines cited

~~~~text
$ H=/Volumes/Sensidine/Praxis.build/vm/2026-11-06-vm-handoff.md; for n in 23 27 31 37 39 93 95 106 127 301 303 310 311 312 313 314 316 317 318 319 320; do printf "handoff:%s: " $n; sed -n "${n}p" "$H"; done
handoff:23: - **Amendment 3 (2026-11-10):** the VM agent is now Hermes, driving the VM over SSH from the Mac (host alias `praxis-vm`), per the CODE- reply `vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md` (on the VM, `Z:\vm\replies\20261110T211738Z-CODE-vm-agent-hermes.md`). That reply's terms T1–T7, with their sub-points, are part of this file for Hermes; where they differ from the text above or below, they govern for Hermes, except that no term relaxes a §1 hard limit. Authority: Amear's proposal, DECISION_LOG `2026-11-10T20:42:00Z` (WHO: amear), accepted by the master, DECISION_LOG `2026-11-10T20:43:00Z` (decided by master under D-2026-11-08-D D1, changeable by Amear); DECISIONS.md D-2026-11-10-C; unit `2026-11-10-vm-agent-hermes-ssh`, repo HEAD `55979ee`. Nothing above or below is edited or struck by this amendment; the "Read by" line keeps settlement 3's wording, which T1 replaces for Hermes.
handoff:27: Every limit holds for the whole of this file. If a step seems to need breaking one, STOP and write a reply saying which limit and why.
handoff:31: 3. **No connection changes (D-071).** No new NT8 connection, no reconnect, no disconnect. Amear: "D-071 untouched" (DECISIONS.md:1063); "Hard limits unchanged: nothing bought, no new data connection, F1–F4 untouched, borrowed code on its own branch, old as-is set out of every commit." (DECISIONS.md:1063). Why it matters here: `reconnect`, `playbackrun` and AutoReconnect all call `Connection.Connect`, and `playbackrun`, on its baseline stage when `require` is playback, disconnects every non-Playback connection (`report:184`; the D-071 consequence is INFERRED, `report:188`). **Do not start, close or restart NinjaTrader.** Starting it may bring connections up; whether it does on this VM is UNVERIFIED. If a step needs NT8 running and it is not, STOP and reply. Starting it is Amear's.
handoff:37: 9. **Do not install anything else** — not Python, not git, not a package manager. If a tool is missing, STOP and report it. Do not change PowerShell's execution policy; if `Activate.ps1` is blocked, use the README's fallback, `.venv\Scripts\python -m nt8bridge …` (`README.md:48@9664d9b`).
handoff:39: 11. **One-session rule.** While you work on Z:, Code dispatches nothing (DECISIONS.md:1092, settlement 9: "Code does not run agents while the VM session writes; handover goes through the VM handoff file."). Signal it: before your first step, write `Z:\vm\replies\<ts>-STATUS.md` holding the line `STARTED`. When you stop, for any reason, write a new `<ts>-STATUS.md` holding the line `FINISHED`. Code starts no agent between those two files.
handoff:93: Write `Z:\vm\replies\<ts>-STATUS.md` with `STARTED` first.
handoff:95: Report each item below. Observe only: open no settings dialog, click no Connect or Disconnect. **Amendment 2:** one exception — item 0 opens the Trading Hours window, read-only.
handoff:106:    - **NT8 must already be running.** Check with item 7's command first. If NT8 is not running, do not start it (limit 3): answer this item "could not read: NT8 not running", answer items 1–9 as written, set the self-report's `RESULT:` line to `STOP` (that self-report is the STOP reply of section 7), write `FINISHED`, and wait for Code. Do not go on to step 2. (The STOP is this file's reading of limit 3, not Amear's word.)
handoff:127: 1. Copy `Z:\vm\skills\praxis-vm-reporter\SKILL.md` into your skills directory, following the convention you reported in step 1. Do not guess the convention. If you have no skills directory, or loading needs something you cannot do, STOP and say so in the reply.
handoff:301: Every reply is a Markdown file in `Z:\vm\replies\` named `<ts>-<slug>.md`. A reply is never edited after it is written. To correct one, write a new reply that names the old file.
handoff:303: Each reply — yours and Code's — has these lines first, in this order:
handoff:310: Then these sections:
handoff:311: - `## Commands typed` — every command, exactly as typed.
handoff:312: - `## Output` — the output, pasted unedited, in a fenced block per command.
handoff:313: - `## What I saw on screen` — only for things you read from NT8's windows; copy the text exactly.
handoff:314: - `## Could not do` — each item and why, or "none".
handoff:316: Files expected, in order (Code writes the `CODE-` ones):
handoff:317: 1. `<ts>-STATUS.md` — `STARTED`
handoff:318: 2. `<ts>-self-report.md` — step 1
handoff:319: 3. `<ts>-2b-skill-job.md` — step 2
handoff:320: 4. `<ts>-STATUS.md` — `FINISHED`
~~~~

### V4 — CODE- reply lines cited

~~~~text
$ C=/Volumes/Sensidine/Praxis.build/vm/replies/20261110T211738Z-CODE-vm-agent-hermes.md; for n in 36 42 47 48; do printf "CODE-:%s: " $n; sed -n "${n}p" "$C"; done
CODE-:36: - **T2(a) Step 1 only.** Items 0 and 6 go under `## Could not do` with the reason "Hermes drives the VM over SSH and has no screen access; Amear reads it". They do NOT by themselves make RESULT STOP. If every other item is answered, step 1 may end DONE and step 2 may follow. This reply amends the skill's screen-STOP rule for those two items only; everywhere else the skill's rule stands. Step 3.3 needs no amendment, because it is not a read Hermes makes from an NT8 window (T2(d)).
CODE-:42: **T3. Z: is the Mac folder.** Z: reads use the Mac copy at the same relative path under `/Volumes/Sensidine/Praxis.build`, read-only (for example `shasum -a 256` for `certutil -hashfile Z:\...`). Each reply states the swap, word for word, in `## Commands typed`. Writes to `Z:\vm\replies\` = new files in the Mac folder `vm/replies/`, noclobber, never edited. That includes the STATUS files.
CODE-:47: **T4. Same-user check (step 1, new item 0a).** Before step 1 item 1, as a new item in the self-report: `whoami`; the NT8 process owner (for example `Get-CimInstance Win32_Process -Filter "Name='NinjaTrader.exe'" | Invoke-CimMethod -MethodName GetOwner`); `[Environment]::GetFolderPath('MyDocuments')`. If the SSH user is not the user that owns the NinjaTrader process, STOP: the Documents, AddOns and NT8Bridge paths would be another user's. The exact command form is untried (UNVERIFIED).
CODE-:48: - **T4(a) Step 1 order for Hermes** (master's reading under D1, changeable by Amear). (1) Write STARTED. (2) Item 0: run item 7's process check; then record Trading Hours under `## Could not do` (T2(a)); or, if NT8 is not running, item 0's STOP path stands unchanged. (3) Item 0a, this check. (4) Items 1–9; item 7 pastes the same output or a re-run. (5) Item 10, the T6 GET. (6) Write the self-report.
~~~~

### V5 — SKILL.md lines cited

~~~~text
$ S=/Volumes/Sensidine/Praxis.build/vm/skills/praxis-vm-reporter/SKILL.md; for n in 11 15 40; do printf "SKILL:%s: " $n; sed -n "${n}p" "$S"; done
SKILL:11: - Read only. Change nothing in NT8, nothing in Windows, nothing on Z: except this one reply file and your `<ts>-STATUS.md` files.
SKILL:15: - If anything below fails or looks different, record it and stop. Do not fix it.
SKILL:40: - `## Could not do` — each item and why, or `none`.
~~~~

### V6 — self-report structure: item headings, numbered commands, output headings, sections

~~~~text
$ /usr/bin/grep -n -E '^### Item|^[0-9]\. |^### Command|^## ' /Volumes/Sensidine/Praxis.build/vm/replies/20261110T214834Z-self-report.md
6:## Identity and Environment (Items 1, 2)
8:### Item 1: Identity
14:### Item 2: Skills loading convention
18:## Step-0 Answers (Item 9)
27:## Commands typed
29:1. NT8 process check (Items 0, 7):
32:2. Same-user check (Item 0a):
35:3. Python version (Item 3):
38:4. PowerShell version (Item 4):
41:5. Git version (Item 5):
44:6. NT8 file version (Item 6 per T2(b)):
47:7. Documents folder (Item 8):
50:8. n8n healthz check (Item 10 per T6):
53:## Output
55:### Command 1 (NT8 process check - Items 0, 7)
62:### Command 2 (Same-user check - Item 0a)
73:### Command 3 (Python version - Item 3)
78:### Command 4 (PowerShell version - Item 4)
85:### Command 5 (Git version - Item 5)
90:### Command 6 (NT8 file version - Item 6 per T2(b))
96:### Command 7 (Documents folder - Item 8)
101:### Command 8 (n8n healthz check - Item 10 per T6)
108:## What I saw on screen
111:## Could not do
~~~~

### V7 — birth and modify times (UTC) of the four Hermes files and the skill copy

~~~~text
$ cd /Volumes/Sensidine/Praxis.build/vm/replies; for f in 20261110T214542Z-STATUS.md 20261110T214834Z-self-report.md /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md 20261110T224920Z-2b-skill-job.md 20261110T215014Z-STATUS.md; do TZ=UTC stat -f '%SB birth | %Sm modify | %N' -t '%Y-%m-%dT%H:%M:%SZ' "$f"; done; printf 'name order: '; ls -1 2026111*Z-*.md | /usr/bin/grep -v CODE | tr '\n' ' '; echo
2026-11-10T21:46:36Z birth | 2026-11-10T21:46:36Z modify | 20261110T214542Z-STATUS.md
2026-11-10T21:48:54Z birth | 2026-11-10T21:48:54Z modify | 20261110T214834Z-self-report.md
2026-11-10T21:49:07Z birth | 2026-11-10T21:49:07Z modify | /Users/admin/.hermes/skills/praxis-vm-reporter/SKILL.md
2026-11-10T21:49:56Z birth | 2026-11-10T21:49:56Z modify | 20261110T224920Z-2b-skill-job.md
2026-11-10T21:50:17Z birth | 2026-11-10T21:50:17Z modify | 20261110T215014Z-STATUS.md
name order: 20261110T214542Z-STATUS.md 20261110T214834Z-self-report.md 20261110T215014Z-STATUS.md 20261110T224920Z-2b-skill-job.md 
~~~~

### V8 — limit 12: what the forbidden title is (descriptor only), and the patterns E26 searched

~~~~text
$ /usr/bin/grep -n -o -F 'titles circuit breaker #5 with a medication brand name' /Volumes/Sensidine/Praxis.build/DECISIONS.md; printf 'E26 pattern list in artifact (count of lines): '; /usr/bin/grep -c -F 'for p in breaker "#5" circuit' /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker1.md
1142:titles circuit breaker #5 with a medication brand name
E26 pattern list in artifact (count of lines): 1
~~~~

### V9 — per-file grade counts re-run from the table rows; malformed-row checks; the report counts table

~~~~text
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker1.md; for L in A B C D; do printf '%s rows=' $L; /usr/bin/grep -c -E "^\| ${L}[0-9]+[ab]? \|" "$F"; for G in 'DONE' 'NOT DONE' 'NOT APPLICABLE' 'NOT ASSESSABLE FROM DISK' 'OPEN — FOR THE MASTER'; do printf '  %s | %s = ' $L "$G"; /usr/bin/grep -c -E "^\| ${L}[0-9]+[ab]? \| [^|]* \| ${G}( — ESCALATE TO MASTER)? \|" "$F"; done; done; printf 'rows whose grade cell is none of the five: '; /usr/bin/grep -E '^\| [ABCD][0-9]+[ab]? \|' "$F" | /usr/bin/grep -v -c -E '^\| [ABCD][0-9]+[ab]? \| [^|]* \| (DONE|NOT DONE|NOT APPLICABLE|NOT ASSESSABLE FROM DISK|OPEN — FOR THE MASTER)( — ESCALATE TO MASTER)? \|'; printf 'rows without exactly 4 cells: '; /usr/bin/grep -E '^\| [ABCD][0-9]+[ab]? \|' "$F" | awk -F'|' 'NF!=6{c++} END{print c+0}'; sed -n '151,156p' "$F"
A rows=11
  A | DONE = 4
  A | NOT DONE = 0
  A | NOT APPLICABLE = 4
  A | NOT ASSESSABLE FROM DISK = 3
  A | OPEN — FOR THE MASTER = 0
B rows=44
  B | DONE = 29
  B | NOT DONE = 4
  B | NOT APPLICABLE = 1
  B | NOT ASSESSABLE FROM DISK = 8
  B | OPEN — FOR THE MASTER = 2
C rows=28
  C | DONE = 16
  C | NOT DONE = 3
  C | NOT APPLICABLE = 1
  C | NOT ASSESSABLE FROM DISK = 8
  C | OPEN — FOR THE MASTER = 0
D rows=13
  D | DONE = 5
  D | NOT DONE = 1
  D | NOT APPLICABLE = 4
  D | NOT ASSESSABLE FROM DISK = 3
  D | OPEN — FOR THE MASTER = 0
rows whose grade cell is none of the five: 0
rows without exactly 4 cells: 0
| File | Asked | DONE | NOT DONE | NOT APPLICABLE | NOT ASSESSABLE FROM DISK | OPEN — FOR THE MASTER |
|---|---|---|---|---|---|---|
| A STARTED | 11 | 4 | 0 | 4 | 3 | 0 |
| B self-report | 44 | 29 | 4 | 1 | 8 | 2 |
| C 2b-skill-job | 28 | 16 | 3 | 1 | 8 | 0 |
| D FINISHED | 13 | 5 | 1 | 4 | 3 | 0 |
~~~~

### V10 — sampled rows not in the fix log: B13, B30, C8

~~~~text
$ cd /Volumes/Sensidine/Praxis.build/vm; R='Hermes drives the VM over SSH and has no screen access; Amear reads it'; printf 'B13: required length=%s; quoted in CODE-:36 count=' ${#R}; sed -n 36p replies/20261110T211738Z-CODE-vm-agent-hermes.md | /usr/bin/grep -c -F -- "\"$R\""; for n in 112 113; do printf 'B13: self-report:%s holds ": <required>" count=' $n; sed -n ${n}p replies/20261110T214834Z-self-report.md | /usr/bin/grep -c -F -- ": $R"; done; diff <(sed -n '65,70p' 2026-11-06-vm-handoff.md | awk -F' [|] ' '{print $3}') <(sed -n '20,25p' replies/20261110T214834Z-self-report.md | sed -E 's/^- Item [0-9] \([^)]*\): //'); echo "B30 diff exit=$?"; diff <(sed -n '19,23p' skills/praxis-vm-reporter/SKILL.md | sed -E 's/^[0-9]\. `//; s/`( — this is `<ts>`\.)?$//') <(sed -n '8,12p' replies/20261110T224920Z-2b-skill-job.md | sed -E 's/^[0-9]\. //' | sed -E "2,4s/^\\\$D = \[Environment\]::GetFolderPath\('MyDocuments'\); //"); echo "C8 diff exit=$?"
B13: required length=70; quoted in CODE-:36 count=1
B13: self-report:112 holds ": <required>" count=1
B13: self-report:113 holds ": <required>" count=1
B30 diff exit=0
C8 diff exit=0
~~~~

### V11 — staged state and HEAD, read-only (no optional index locks)

~~~~text
$ export GIT_OPTIONAL_LOCKS=0; git -C /Volumes/Sensidine/Praxis.build rev-parse --short HEAD; git -C /Volumes/Sensidine/Praxis.build diff --cached --stat; git -C /Volumes/Sensidine/Praxis.build diff --cached --name-status
85a803f
 docs/reports/evidence/2026-10-28-mffu-davi-reply.png | Bin 0 -> 254350 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
A	docs/reports/evidence/2026-10-28-mffu-davi-reply.png
~~~~

### V12 — artifact S1 provenance text (W1:21, W1:249), the E27 preamble admission, run definitions present, Result lines on B36/B37

~~~~text
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker1.md; for n in 21 249 1119 1129; do printf "W1:%s: " $n; sed -n "${n}p" "$F"; done; /usr/bin/grep -n -o 'that second definition was not printed' "$F"; printf 'lines starting "run () " in the artifact: '; /usr/bin/grep -n '^run () ' "$F" | cut -d: -f1 | tr '\n' ' '; echo; printf 'lines starting "run () " in the E29 block (W1:1153-1167): '; sed -n '1153,1167p' "$F" | /usr/bin/grep -c '^run () '; printf 'lines "$ declare -f run" in the artifact: '; /usr/bin/grep -c -F '$ declare -f run' "$F"
W1:21: - S1: every claim below cites an evidence block E1–E29 in "Verification evidence"; each block shows a `$ ` command line followed by output. For E1–E24 (worker 1) the producing script is not pasted in this report, so the blocks themselves do not show that the output came from that command string; each can be checked by re-running the printed command. E25–E29 (fix worker 3) were produced by the `run` function whose definition is pasted with them.
W1:249: E1–E24 (worker 1): each block shows a `$ ` line with a command string, followed by output. The script that produced them is not pasted in this report, so the blocks do not by themselves show that the output was produced by that exact string; each command can be re-run to check. E25–E29 (fix worker 3) were produced by the `run` function whose `declare -f` definition is pasted at E25: it prints `$ ` plus the command string, then `eval`s that same string with stderr merged into stdout, under `/bin/bash` on the Mac.
W1:1119: - limit 9 (B36, B37: OPEN — FOR THE MASTER, both readings printed)
W1:1129: For the master: B36 and B37 (limit 9 vs `RESULT: DONE`) are OPEN; B43 (who started NT8, and whether before STARTED) is escalated.
1046:that second definition was not printed
lines starting "run () " in the artifact: 936 1082 
lines starting "run () " in the E29 block (W1:1153-1167): 0
lines "$ declare -f run" in the artifact: 0
~~~~

### V13 — artifact S13 line: occurrences (two-halves variable), line number, total lines, last line

~~~~text
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker1.md; A='Fills are optimistic; Standard resolution'; B=' on 1-minute bars; 2 ticks/side slippage assumed.'; S="$A$B"; printf 'grep -cF: '; /usr/bin/grep -cF -- "$S" "$F"; printf 'line: '; /usr/bin/grep -nF -- "$S" "$F" | cut -d: -f1; printf 'wc -l: '; wc -l < "$F" | tr -d ' '; printf 'tail -1 equals S: '; [ "$(tail -1 "$F")" = "$S" ] && echo YES || echo NO
grep -cF: 1
line: 1167
wc -l: 1167
tail -1 equals S: YES
~~~~

### V14 — this file before the Result section and the final line are appended: run definition, S13 count (expected 0), host name count (expected 0)

~~~~text
$ declare -f run
run () 
{ 
    printf '$ %s\n' "$1";
    eval "$1" 2>&1
}
$ F=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-11-hermes-replies-grading-worker4.md; A='Fills are optimistic; Standard resolution'; B=' on 1-minute bars; 2 ticks/side slippage assumed.'; S="$A$B"; printf 'S13 sentence occurrences so far: '; /usr/bin/grep -cF -- "$S" "$F"; H=$(sed -n 64p /Volumes/Sensidine/Praxis.build/vm/replies/20261110T214834Z-self-report.md | cut -d'\' -f1); printf 'Windows host name (derived from self-report:64, not printed) occurrences, case-insensitive: '; /usr/bin/grep -ciF -- "$H" "$F"; printf 'lines so far: '; wc -l < "$F" | tr -d ' '
S13 sentence occurrences so far: 0
Windows host name (derived from self-report:64, not printed) occurrences, case-insensitive: 0
lines so far: 294
~~~~

## Result

Result: FAIL

W2 items: W2-1 RESOLVED (evidence error W4-5); W2-2 OVER-CORRECTED (W4-1); W2-3 RESOLVED (the dependent C27 is not: W4-3); W2-4 RESOLVED; W2-5 RESOLVED; W2-6 NOT RESOLVED, partly (W4-2); W2-7 RESOLVED for B43, and the new B44 is too generous (W4-4). Fix-log S1: (a) RESOLVED; (b) PARTLY (W4-6); (c) RESOLVED in form (note only). The counts table matches the rows as written (V9). The artifact's S13 line occurs once and is its last line (V13).

- W4-1: B17 (W1:69) NOT DONE at OBSERVED level rests on an unmarked reading of CODE-:47 as file position. Its ASKED cell carries the inserted gloss "placement of item 0a in the file". T4(a) (CODE-:48) reads "before item 1" as action order, and inside `## Commands typed` and `## Output` item 0a comes ahead of every other item command (V4, V6). Harsher than the source supports. It should print both readings and be graded READING or OPEN.
- W4-2: A2a (W1:38) and B20 (W1:72) DONE grade handoff:93 "STARTED first" and T4(a)(1) on file order only, after restating them as "before every other Hermes file". Both are action-order requirements (handoff:95; CODE-:48 (1) before (2)), and the action order is not on disk (A2b). Too generous.
- W4-3: C27 (W1:128) NOT APPLICABLE clears limit 9 for step 2 on the B36 reading, which the report itself leaves OPEN and says a worker may not settle (W1:88). Too generous; it should be OPEN — FOR THE MASTER.
- W4-4: B44 (W1:96) DONE for limit 12. E26 greps the descriptors `breaker`/`#5`/`circuit`, not the source title, which is a medication brand name (DECISIONS.md:1142, V8). E26 cannot detect the title. The row also grades "anywhere" DONE from four files, unlike D4/D5 and C16. Too generous: it should be DONE (INFERRED, four files, from E1/E21) plus NOT ASSESSABLE FROM DISK for anywhere else.
- W4-5: B7 (W1:59) lists the step-2 skill copy (2b:36) as missing from B's `## Commands typed`. The copy was born at 21:49:07Z, after B was written at 21:48:54Z (V7). Evidence error; the grade stands.
- W4-6: W1:21 says E25–E29 were produced by a `run` function "whose definition is pasted with them". For E26/E27 the definition "was not printed" (W1:1046), E29 shows none, and the `run ()` text at W1:936 and :1082 has no command line that printed it (V12). Description, not paste (S1).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
