# Resume worker 2 report: unit 2026-11-13-research-filing-resume, adversary round 2

## Task

Cold adversary, round 2 (last round), for unit 2026-11-13-research-filing-resume. Authority: DECISION_LOG.md rows 2026-11-13T19:40:54Z (allowed edits to the four filed return-handoff files) and 2026-11-13T19:58:43Z (resume plan), both praxis-master under D-2026-11-08-D D1. Grade checks (a)-(g) from the brief with my own commands, and check the resume manager report (docs/reports/2026-11-13-research-filing-resume-manager.md) against its own rules. Round 2's grades and the manager report's final Result line are not yet in that report and are not graded here.

## Mode

ADVERSARIAL. Read-only apart from this report. Scratch work in /tmp/rfr-adv2/ only. No git add, commit, stash, reset or checkout; the index was not written. Nothing written under .claude/ (find output in E9). The two Downloads originals were read only through diff, cmp, shasum, grep, sed and od; nothing in /Users/admin/Downloads was executed.

## Criterion

specs/SPEC_RUBRIC.md S1 (:133), S2 (:134), S8 (:140), S13 (:145). House reading of S13 once: standalone lines outside quoted commands, code blocks and pasted drafts. The S13 sentence used in every grep below is read from /tmp/rfr-adv2/s13.txt, cut out of rubric :145 (E1), so command lines do not print it.

## Checks

### (a) Rebuild of strategy and kimi received files; Downloads diffs: PASS

- Rebuilt in /tmp/rfr-adv2/rebuilt/ with sed `r` (a different method from the manager's awk), positions read from worker 1's diff headers at :142, :146, :148 (`108d107`, `42d41`, `330d328`) and text cut from :143, :147, :149 (first two bytes removed). Hashes: strategy 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14, kimi 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54; both equal the brief's values (test exit 0). The three inserted lines cmp equal to the rubric sentence (E1). Negative controls (one line early) give other hashes (E2).
- Full diffs, Downloads original against filed twin: session-close `55d54`, vm-queue `45d44`, one deleted line each, and that line cmp equals the S13 sentence. `sed 'Nd'` of each original cmp equals its filed twin (exit 0), so nothing else differs (E3). Each original carried the sentence standalone twice (:5 and :55; :7 and :45); the first copy was kept.

### (b) S13 sentence once per filed file, standalone, outside quoted or pasted material, first copy: PASS

- grep -x and grep substring both give one line per file: strategy :5, kimi :5, session-close :5, vm-queue :7 (E4). No other line holds the sentence as a substring. The only fence is strategy :34-:94; :5 is before it. No 4-space or tab-indented lines in any file. The kept line sits in the channel's own header text below the title and Written-by line in every file (E4).
- Loose matches (1-minute bars, ticks/side, fill optimism) at strategy :41, :50, :67 and session-close :19, :32 are prose, not copies of the sentence (E4).

### (c) PII scan of the four filed files: PASS

- Zero hits for email, IPv4, MAC, SSH key names or key material words, user-home paths, /Volumes, /private or /tmp paths, private hostnames, Tailscale or VPN names, at-handles, honorific plus name, and no bracketed placeholders (E5).
- False positives, with reasons: IPv6-pattern hits kimi :69 (`15:30:`, a rule time window), vm-queue :28 (`12:32:48`, an NT8 restart time) and :31 (`17:36:47`, a bridge.log UTC time); path hit vm-queue :5 (`C:\praxis\vm-bridge`, a project folder on the VM with no user-name segment); `win-rate` hits from the hostname pattern; account-word hits are ordinary words (the case-insensitive pattern let lowercase words through).
- Names: every capitalised token across the four files was listed (482 after dropping the two ambiguous items and four words this report may not print, E6). Person-like tokens are published-paper or cited authors, a theory or ratio name (Kelly, Markowitz, Sharpe), the pronoun He (strategy :13, refers to Amear), and Amear. The two ambiguous cited items (a two-surname pair dated 2026 that the channel and Kimi could not identify, and a single-surname practitioner source dated 2026) are cited authors of sources, not private persons in PRAXIS's dealings; they occur 6 times in kimi, 1 in session-close, 3 in strategy (E6). session-close :48 names no one at the firm.

### (d) The 7 unit MANIFEST rows: PASS

- All 7 rows (:477-:483) have 7 pipe-separated fields, the same as neighbours :470-:476, with path, `Report`, `3`, `2026-11-13` (E7).
- Writer named in each: 4 rows `written by the Claude.ai Praxis channel`, 1 `written by praxis-manager for unit 2026-11-13-research-filing-resume`, 2 `written by praxis-worker for unit 2026-11-13-research-filing`. DISPATCH_LOG rows 2792-2799 show praxis-worker spawns at 19:42:27Z and 19:47:00Z and praxis-manager spawns, which fits (E7).
- Unit and DECISION_LOG named in all 7; 19:40:54Z in all 7, 19:58:43Z in row 5. All 7 end `; ungraded at time of row |` (count 7).
- Level words (substring, case-insensitive) in the 7 rows: none (grep exit 1). Across all 30 added MANIFEST lines there is 1 substring hit, `UNVERIFIED` in the earlier walk-forward-values row, which is one of the 23 rows from before this unit (E7).
- Rows 1-4 against files and diffs: deleted received lines (:108; :42 and :330; :55; :45) and kept lines (:5, :5, :5, :7) match (a) and (b). Content claims match the files: strategy headings :7, :15, :28, :32, :96, the repo cross-check line marked read-only, and the backtest-order line in section 3; kimi :15, :24, :35, :43 and two adjacent blank lines at :41-:42; session-close :7, :16-:22 (withdrawal citing D-2026-11-02-A), table :28-:35, :46; vm-queue :3 (replaces the VM bridge queue bullet), :5 (pasted by Amear), table :13-:17, :25, :33 (INFERRED reading), :38.
- Rows 5-7 against their reports: row 5's list (rebuild with hashes E1, Downloads diffs E2, S13 counts E3, PII scan E4, MANIFEST change and blob E5-E7, tracked-file comparison E8, round 1 grades at :553-:571) is present in the manager report. Row 6 matches worker 1's report (diffs :102-:178, PII :47-:100, rows and blob :180-:296, sha256 :212-:222). Row 7 matches worker 2's report (checks (a)-(f) at :17-:58, diff-stat E5 at :561).

### (e) Blob: PASS

460 lines; first 453 cmp equal HEAD:MANIFEST.md (exit 0); last 7 cmp equal MANIFEST.md's last 7 (exit 0); whole blob cmp equal HEAD plus the last 7 (exit 0); ends in a newline. git diff MANIFEST.md: 0 removed lines, 30 added; the first 23 added lines cmp equal the first 23 added lines of the MANIFEST hunk in /tmp/rfr/gitdiff-before.patch (exit 0); MANIFEST.md :1-:480 cmp equal the baseline copy (exit 0). Blob sha256: e2189a430dd5da269e36a1f210dd4b2172cb8272c0c8bcafbdfa28ec015614d7 (E8).

### (f) Only MANIFEST.md changed among tracked files since the baseline: FAIL

At 2026-11-13T20:14:33Z, two of the 14 tracked modified files differ from /tmp/rfr/tracked-sha-before.txt: MANIFEST.md (this unit's edit) and DISPATCH_LOG.md (dd16a2d8... before, ebbea6b7... now). The set of tracked modified paths is unchanged (cmp exit 0). DISPATCH_LOG.md's first bytes equal the baseline copy (prefix cmp exit 0); it gained 5 rows after baseline line 2799, each with WHY `hook-recorded at SubagentStart` or `hook-recorded at SubagentStop` (non-hook rows among them: 0). The row text is in scripts/dispatch-log-writeahead.sh :109 (spawn rows; bound to SubagentStart at .claude/settings.json :135-:140) and scripts/dispatch-log-close.sh :287 (close rows; bound to SubagentStop at settings.json :145 onward, file line :159). Four rows are the ones in the manager's E8; the fifth, 20:11:40Z praxis-worker spawn corr=a6783c300b286cc33, is new since E8 and is INFERRED to be the spawn of this adversary. No authored change was found. Reported, not excused (E8).

### (g) Stub manager report: PASS

sha256 eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f (match exit 0); untracked (ls-files exit 1; listed by --others --exclude-standard; not in HEAD), no index entry (E8).

### Resume manager report against its own rules

- `Result:` line: one, at :590 (interim; the final line comes after this round). Section `## Verification evidence (command output)` at :47. The S13 sentence: one standalone line, :592, the last line; the two other substring hits, :191 and :195, are diff output lines starting with `< ` inside a fence. None of the three forbidden words (grep -i -F from a pattern file, exit 1). Neither ambiguous cited-author item appears (count 0); the only author surname is in pasted kimi :217 output, a published citation. Every output line of the ten /tmp/rfr/*.out files it pastes appears in the report (0 missing lines each, E9).
- Quotation spot-check, 13 strings: 12 byte-exact (`once`, `(in progress)`, `< `, `2 ticks/side slippage`, `15:30:`, `@15:30`, `@25k`, `rep who answered on 11-12`, `hook-recorded at SubagentStart`, `hook-recorded at SubagentStop`, `(pending)`, and the 7 copied round-1 grade lines at :558-:564, which all match lines of the round-1 report by grep -x). 1 not byte-exact: defect 1.
- None of these make row 5's description wrong, so (d) stays PASS.

## Defects

1. Manager report :321, quotation not byte-exact. The quoted VM folder path holds byte 0x0B (vertical tab) where the source, vm-queue :5, holds a backslash followed by `v`. The quoted text, as a fixed string, occurs 0 times in vm-queue (E9). This breaks the report's rule that quotation marks go only around byte-exact source text. The PII code block at :284 has the right bytes; only the prose line is wrong. Line :321 is the only line with that byte.
2. Check (f): DISPATCH_LOG.md changed after the baseline (5 hook-recorded rows, one more than at round 1). It is not an authored edit; the step-4 criterion is still not met as written.
3. Minor, manager report :321: it calls `@15:30` price and size shorthand. At kimi :217 it is a clock time (`long @15:30`). It is still not a handle, so the PII result stands; the reason given for this one item is wrong.

Observations, not defects:
- The rebuild in (a) matches hashes that come only from worker 1's report (its /tmp/rf-pre copies are gone). It shows the filed files agree with that report; it cannot show the report's pre-copy hashes are true. Round 1 raised this too.
- Reading strategy received :108 and kimi received :330 as channel footers rather than pasted output is INFERRED. The Kimi brief (strategy :34-:94) has no instruction to end output with the sentence (E4); the Gemini brief is not in the repo.
- Worker 1's report, which the 19:58:43Z row puts in the commit, names both ambiguous cited-author items in full at its :38-:39. Outside checks (a)-(g); reported for the master.
- Manager report :533 describes hook behaviour without pasting the hook. The bindings in settings.json (:135 SubagentStart to dispatch-log-writeahead.sh; :145 SubagentStop to dispatch-log-close.sh) and the row text in those scripts (E8) support it.
- DISPATCH_LOG: corr=a8a6966c3548284a8 has a close row at 20:03:55Z and then a new spawn row at 20:09:58Z, so an open row is left for the resume manager. Hook behaviour, out of scope.

## Verification evidence (command output)

All scripts ran under bash with `set -v`, so each command line is printed before its output (`$(...)` substitutions are echoed as extra lines). Scripts and outputs are in /tmp/rfr-adv2/. Lines that would print the whole S13 sentence were cut or replaced in the scripts; no pasted line holds it.

### E1. S13 scratch file from rubric :145; worker 1 diff lines equal it (./s13make.sh)

```
cd /Volumes/Sensidine/Praxis.build
sed -n '145p' specs/SPEC_RUBRIC.md | grep -o '"Fills[^"]*"' | tr -d '"' > /tmp/rfr-adv2/s13.txt
wc -c /tmp/rfr-adv2/s13.txt
      91 /tmp/rfr-adv2/s13.txt
cmp /tmp/rfr-adv2/s13.txt /tmp/rfr/s13.txt; echo "cmp vs manager s13 exit=$?"
cmp vs manager s13 exit=0
sed -n '143p;147p;149p' docs/reports/2026-11-13-research-filing-worker1.md | sed 's/^< //' | cmp - <(cat /tmp/rfr-adv2/s13.txt /tmp/rfr-adv2/s13.txt /tmp/rfr-adv2/s13.txt); echo "cmp worker1 diff lines 143,147,149 vs rubric sentence x3 exit=$?"
cat /tmp/rfr-adv2/s13.txt /tmp/rfr-adv2/s13.txt /tmp/rfr-adv2/s13.txt
cmp worker1 diff lines 143,147,149 vs rubric sentence x3 exit=0
```

### E2. Check (a): rebuild of strategy and kimi received files, hashes, negative controls (./rebuild.sh)

```
W=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-research-filing-worker1.md
R=/Volumes/Sensidine/Praxis.build/docs/reports
O=/tmp/rfr-adv2/rebuilt
mkdir -p "$O"
sed -n '141,150p' "$W" | cut -c1-40
diff /tmp/rf-pre/2026-11-13-return-hando
108d107
< Fills are optimistic; Standard resolut
diff exit=1
diff /tmp/rf-pre/2026-11-13-return-hando
42d41
< Fills are optimistic; Standard resolut
330d328
< Fills are optimistic; Standard resolut
diff exit=1
# strategy: header at :142 "108d107", text at :143; kimi: headers :146 "42d41" and :148 "330d328", text :147 :149
sed -n '143p' "$W" | cut -c3- > "$O/strat.ins"
sed -n '147p' "$W" | cut -c3- > "$O/kimi1.ins"
sed -n '149p' "$W" | cut -c3- > "$O/kimi2.ins"
sed -n '142p;146p;148p' "$W" | sed -E 's/^([0-9]+)d([0-9]+)$/old=\1 after-new=\2/'
old=108 after-new=107
old=42 after-new=41
old=330 after-new=328
sed "107r $O/strat.ins" "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" > "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md"
sed -e "41r $O/kimi1.ins" -e "328r $O/kimi2.ins" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" > "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md"
wc -l "$O"/2026-11-13-return-handoff-claude-ai-*.md
     330 /tmp/rfr-adv2/rebuilt/2026-11-13-return-handoff-claude-ai-kimi-research.md
     108 /tmp/rfr-adv2/rebuilt/2026-11-13-return-handoff-claude-ai-strategy-research.md
     438 total
shasum -a 256 "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md"
8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14  /tmp/rfr-adv2/rebuilt/2026-11-13-return-handoff-claude-ai-strategy-research.md
97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54  /tmp/rfr-adv2/rebuilt/2026-11-13-return-handoff-claude-ai-kimi-research.md
[ "$(shasum -a 256 < "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -c1-64)" = 8e8621e02fb70760cc2f3e6544b604ba89b1188a9ad55e2e222a23b2a045de14 ]; echo "strategy match exit=$?"
shasum -a 256 < "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -c1-64
strategy match exit=0
[ "$(shasum -a 256 < "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -c1-64)" = 97d08993f78500e6a0b9c5e61382c202d296e6d5731f76ba6589afc58e2e4f54 ]; echo "kimi match exit=$?"
shasum -a 256 < "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -c1-64
kimi match exit=0
grep -n -x -F -f /tmp/rfr-adv2/s13.txt "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -d: -f2
5
108
5
42
330
diff "$O/2026-11-13-return-handoff-claude-ai-strategy-research.md" "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" | cut -c1-12; echo "exit=${PIPESTATUS[0]}"
108d107
< Fills are 
exit=1
diff "$O/2026-11-13-return-handoff-claude-ai-kimi-research.md" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" | cut -c1-12; echo "exit=${PIPESTATUS[0]}"
42d41
< Fills are 
330d328
< Fills are 
exit=1
# negative controls: kimi with the second insert one line early; strategy with no trailing newline change
sed -e "41r $O/kimi1.ins" -e "327r $O/kimi2.ins" "$R/2026-11-13-return-handoff-claude-ai-kimi-research.md" | shasum -a 256
249dc173f0021cbaf42417e64410968350e0c8e4f4b4118b3386bb5988e08430  -
sed "106r $O/strat.ins" "$R/2026-11-13-return-handoff-claude-ai-strategy-research.md" | shasum -a 256
785e9d5eb822055d461a326518ccf5431ab14e05e6911839dfd1a99ac419b995  -
```

### E3. Check (a): Downloads originals against filed twins (./dl.sh; the deleted line is replaced by a marker in the diff display and compared to the sentence by cmp)

```
D=/Users/admin/Downloads
R=/Volumes/Sensidine/Praxis.build/docs/reports
shasum -a 256 "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" "$R"/2026-11-13-return-handoff-claude-ai-*.md
e9e9674f37d4e41072581a3099efc074d9f140c8c2a507c63557c4d8ac52cf1d  /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md
535743ca6ad5a154c8926b6dc9efc7b62f59de862fe31106ced444bfe90f09ca  /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
1efd9485762cc2944e47d3be6a5249161a4d3c301ea1caf439561a40b002bde3  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
4ac03c59ad9197b0f2a8449983f858be4939b343e46706453e7b505d9cba43c2  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
6b283621f61f8db60052bbf379bb83336de802f199c130321cc0e6931df3b306  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
ba2d8613698bfd555b8d274e9f3c9f76c753bf8ba075d86b8fdb87d47c18345a  /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
wc -l -c "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
      55    6572 /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md
      45    5409 /Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
     100   11981 total
diff "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$R/2026-11-13-return-handoff-claude-ai-session-close.md" | sed 's/^< Fills are optimistic.*/< [S13 sentence line, cut here]/'; echo "diff exit=${PIPESTATUS[0]}"
55d54
< [S13 sentence line, cut here]
diff exit=1
diff "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$R/2026-11-13-return-handoff-claude-ai-session-close.md" | sed -n '2p' | cut -c3- | cmp - /tmp/rfr-adv2/s13.txt; echo "deleted line equals S13 sentence exit=$?"
deleted line equals S13 sentence exit=0
diff "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" "$R/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" | sed 's/^< Fills are optimistic.*/< [S13 sentence line, cut here]/'; echo "diff exit=${PIPESTATUS[0]}"
45d44
< [S13 sentence line, cut here]
diff exit=1
diff "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" "$R/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" | sed -n '2p' | cut -c3- | cmp - /tmp/rfr-adv2/s13.txt; echo "deleted line equals S13 sentence exit=$?"
deleted line equals S13 sentence exit=0
cmp <(sed '55d' "$D/2026-11-13-return-handoff-claude-ai-session-close.md") "$R/2026-11-13-return-handoff-claude-ai-session-close.md"; echo "session-close = Downloads minus :55 exit=$?"
sed '55d' "$D/2026-11-13-return-handoff-claude-ai-session-close.md"
session-close = Downloads minus :55 exit=0
cmp <(sed '45d' "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md") "$R/2026-11-13-return-handoff-claude-ai-vm-queue-results.md"; echo "vm-queue = Downloads minus :45 exit=$?"
sed '45d' "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
vm-queue = Downloads minus :45 exit=0
grep -n -x -F -f /tmp/rfr-adv2/s13.txt "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" | cut -d: -f2
5
55
7
45
grep -c -F -f /tmp/rfr-adv2/s13.txt "$D/2026-11-13-return-handoff-claude-ai-session-close.md" "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
/Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-session-close.md:2
/Users/admin/Downloads/2026-11-13-return-handoff-claude-ai-vm-queue-results.md:2
sed -n '53,54p' "$D/2026-11-13-return-handoff-claude-ai-session-close.md" | cut -c1-60 | od -c | head -4
0000000    -       *   *   A   m   e   a   r       a   s   k   e   d    
0000020    w   h   e   n       P   R   A   X   I   S       c   a   n    
0000040    g   o       l   i   v   e   .   *   *       T   h   e       c
0000060    h   a   n   n   e   l   '   s       a   n   s  \n  \n        
sed -n '43,44p' "$D/2026-11-13-return-handoff-claude-ai-vm-queue-results.md" | cut -c1-60
4. **Open:** what restarted NT8 at 12:32 PM.

```

### E4. Check (b): S13 placement, fences, indented lines, file heads with the kept line filtered out (./s13check.sh); loose matches, Kimi brief scan, strategy content lines, level-word location in added MANIFEST lines, DISPATCH_LOG rows 2792-2799 (./extra.sh; the level-word regex in two command lines is a search pattern)

```
cd /Volumes/Sensidine/Praxis.build/docs/reports
for f in strategy-research kimi-research session-close vm-queue-results; do g=2026-11-13-return-handoff-claude-ai-$f.md; printf '%s x-lines: ' "$f"; grep -n -x -F -f /tmp/rfr-adv2/s13.txt "$g" | cut -d: -f1 | tr '\n' ' '; printf '| substring lines: '; grep -n -F -f /tmp/rfr-adv2/s13.txt "$g" | cut -d: -f1 | tr '\n' ' '; printf '| loose "optimistic" lines: '; grep -n -i -E 'fills? (are|is) optimistic|1-minute bars|ticks/side' "$g" | cut -d: -f1 | tr '\n' ' '; printf '| fences: '; grep -n -E '^\s*(```|~~~)' "$g" | cut -d: -f1 | tr '\n' ' '; printf '| indented-4 lines: '; grep -c -E '^(    |\t)' "$g"; done
strategy-research x-lines: 5 | substring lines: 5 | loose "optimistic" lines: 5 41 50 67 | fences: 34 94 | indented-4 lines: 0
kimi-research x-lines: 5 | substring lines: 5 | loose "optimistic" lines: 5 | fences: | indented-4 lines: 0
session-close x-lines: 5 | substring lines: 5 | loose "optimistic" lines: 5 19 32 | fences: | indented-4 lines: 0
vm-queue-results x-lines: 7 | substring lines: 7 | loose "optimistic" lines: 7 | fences: | indented-4 lines: 0
sed -n '19p' 2026-11-13-return-handoff-claude-ai-session-close.md | grep -o -i -E '.{0,40}ticks/side.{0,30}'
 SEP25), $2.96 round-trip commission, 2 ticks/side slippage: 1,304 trades, net -
for f in strategy-research kimi-research session-close vm-queue-results; do g=2026-11-13-return-handoff-claude-ai-$f.md; echo "== $f :1-8"; sed -n '1,8p' "$g" | grep -v -x -F -f /tmp/rfr-adv2/s13.txt | cut -c1-120; done
== strategy-research :1-8
# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: replacement-strategy research (Gemini run + aud

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:25 ET. File it as written unless a de-identification check 


## 1. What happened (REPORTED BY the Claude.ai channel)

== kimi-research :1-8
# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: Kimi Deep Research follow-up + audit

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:35 ET. Follows docs/reports/2026-11-13-return-handoff-claud



Original, filed unedited: `claude/PRAXIS_Kimi_DeepResearch_Strategy_Verification_2026-11-13_ORIGINAL.md` (also Appendix 
== session-close :1-8
# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13 session close: research outcome, correction, and

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:45 ET. File it as written unless a de-identification check 


## 1. Amear's instruction (REPORTED BY the channel, chat 2026-11-13 14:35 ET)

== vm-queue-results :1-8
# Follow-up to the 2026-11-13 session-close handoff: VM bridge queue results (T1-T3)

Written by the Claude.ai Praxis channel, 2026-11-13 about 14:45 ET. Read with `docs/reports/2026-11-13-return-handoff-cl

Source: the VM Claude Code session's own report, pasted to this channel by Amear at 14:37 ET (REPORTED BY Amear; the cha


cd /Volumes/Sensidine/Praxis.build
R=docs/reports
for n in 41 50 67; do sed -n "${n}p" $R/2026-11-13-return-handoff-claude-ai-strategy-research.md | /usr/bin/grep -o -i -E '.{0,50}(1-minute bars|ticks/side).{0,30}'; done
2) on NQ. Our backtest, 2021-03-08 to 2026-07-17, 1-minute bars: 1,173 trades, profit factor 
2021 to July 2026. No tick data. Backtests run on 1-minute bars with standard fill resolution
- Rate fill optimism low, medium or high for 1-minute bars, with the reason (intrabar st
sed -n '32p' $R/2026-11-13-return-handoff-claude-ai-session-close.md | /usr/bin/grep -o -i -E '.{0,50}(1-minute bars|ticks/side).{0,30}'
r target and intrabar stop fill optimistically on 1-minute bars. |
sed -n '34,94p' $R/2026-11-13-return-handoff-claude-ai-strategy-research.md | /usr/bin/grep -n -i -E 'end (with|each)|limitation|sentence|footer|closing|final line|standing' | cut -c1-80; echo "exit=${PIPESTATUS[1]}"
40:Find strategies that trade on most days, have win rates of 55% or higher (or 
exit=0
sed -n '13p' $R/2026-11-13-return-handoff-claude-ai-strategy-research.md | cut -c1-90
- Also this session (voice, REPORTED BY): MFFU follow-up email sent 17:26Z in the pre-purc
/usr/bin/grep -n -o -E 'Repo cross-check \(OBSERVED by the channel, read-only, 2026-11-13\)|^Backtest order:' $R/2026-11-13-return-handoff-claude-ai-strategy-research.md
26:Repo cross-check (OBSERVED by the channel, read-only, 2026-11-13)
30:Backtest order:
git diff MANIFEST.md | /usr/bin/grep '^+[^+]' | /usr/bin/grep -i -E 'built|tested|verified|working|viable|retired|decided' | cut -d'|' -f2
 /docs/specs/2026-11-06-walk-forward-values.md 
git diff MANIFEST.md | /usr/bin/grep '^+[^+]' | /usr/bin/grep -o -i -E '.{0,20}(built|tested|verified|working|viable|retired|decided).{0,10}'
AL; live template UNVERIFIED); §6 gate
sed -n '2792,2799p' DISPATCH_LOG.md | cut -c1-150
- [2026-11-13T19:41:48Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a36ab2e34b73
- [2026-11-13T19:42:27Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=ad36d6148e73b
- [2026-11-13T19:42:30Z] WHO: praxis-manager | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a36ab2e34b73584f4, mat
- [2026-11-13T19:45:54Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=ad36d6148e73b03c9, matc
- [2026-11-13T19:45:54Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a36ab2e34b73
- [2026-11-13T19:47:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=abb2520a90118
- [2026-11-13T19:53:06Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a36ab2e34b73
- [2026-11-13T19:59:23Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a8a6966c3548
/usr/bin/grep -n -E '"Subagent(Start|Stop)"' .claude/settings.json
135:    "SubagentStart": [
145:    "SubagentStop": [
sed -n '135,155p' .claude/settings.json | /usr/bin/grep -n -o -E '"command": *"[^"]*"'
6:"command": "./scripts/dispatch-log-writeahead.sh"
17:"command": "./scripts/gate-manager-output.sh"
/usr/bin/grep -c -F 'hook-recorded at SubagentStart' scripts/dispatch-log-writeahead.sh
1
/usr/bin/grep -c -F 'hook-recorded at SubagentStop' scripts/dispatch-log-writeahead.sh
0
```

### E5. Check (c): PII pattern scan of the four filed files (./pii.sh)

```
cd /Volumes/Sensidine/Praxis.build/docs/reports
F="2026-11-13-return-handoff-claude-ai-strategy-research.md 2026-11-13-return-handoff-claude-ai-kimi-research.md 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
/usr/bin/grep -n -o -i -E '[a-z0-9._%+-]+(@| ?\[at\] ?)[a-z0-9.-]+\.[a-z]{2,}' $F; echo "email exit=$?"
email exit=1
/usr/bin/grep -n -o -E '(^|[^0-9.])[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' $F; echo "ipv4 exit=$?"
ipv4 exit=1
/usr/bin/grep -n -o -i -E '([0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}|[0-9a-f]{0,4}::[0-9a-f]{0,4}|fe80|fd[0-9a-f]{2}:' $F; echo "ipv6 exit=$?"
2026-11-13-return-handoff-claude-ai-kimi-research.md:69:15:30:
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:28:12:32:48
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:31:17:36:47
ipv6 exit=0
/usr/bin/grep -n -o -i -E '([0-9a-f]{2}[:.-]){5}[0-9a-f]{2}|([0-9a-f]{4}\.){2}[0-9a-f]{4}' $F; echo "mac exit=$?"
mac exit=1
/usr/bin/grep -n -o -i -E 'id_[a-z0-9]+|\.pem|\.ppk|\.pub\b|\.key\b|\.ssh|authorized_keys|known_hosts|private key|ssh-[a-z0-9]+|ssh [a-z0-9_.-]+@|BEGIN [A-Z ]*KEY|api[_ -]?key|token|password|passwd|secret' $F; echo "ssh/key exit=$?"
ssh/key exit=1
/usr/bin/grep -n -o -i -E '/Users/[^ `)]*|/home/[^ `)]*|[a-z]:\\[^ `)]*|~/[^ `)]*|\\\\[a-z0-9_.-]+\\|/Volumes/[^ `)]*|/private/[^ `)]*|/tmp/[^ `)]*' $F; echo "path exit=$?"
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
path exit=0
/usr/bin/grep -n -o -i -E 'https?://[^ )>]+|www\.[^ )]+|[a-z0-9-]+\.(local|lan|internal|home|corp|ts\.net|tailscale|duckdns\.org|ngrok[a-z.]*)\b|\b(desktop|laptop|win)-[a-z0-9]{4,}\b|tailscale|tailnet|wireguard|vpn|hostname|ssid|wi-?fi|port [0-9]{2,5}|:[0-9]{4,5}\b' $F; echo "host/net exit=$?"
2026-11-13-return-handoff-claude-ai-strategy-research.md:106:win-rate
2026-11-13-return-handoff-claude-ai-kimi-research.md:106:win-rate
2026-11-13-return-handoff-claude-ai-kimi-research.md:314:win-rate
2026-11-13-return-handoff-claude-ai-session-close.md:26:win-rate
host/net exit=0
/usr/bin/grep -n -o -E '(^|[^A-Za-z0-9])@[A-Za-z_][A-Za-z0-9_]+' $F; echo "handle exit=$?"
handle exit=1
/usr/bin/grep -n -o -i -E '\b(account|acct|id|login|user(name)?)[ #:=]+[A-Z0-9-]{5,}' $F; echo "account-id exit=$?"
2026-11-13-return-handoff-claude-ai-strategy-research.md:77:account trail
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account balance
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:Account SizeProfit
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account equity
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account value
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account failure
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account value
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account deployed
2026-11-13-return-handoff-claude-ai-strategy-research.md:98:account achieves
2026-11-13-return-handoff-claude-ai-strategy-research.md:106:account before
2026-11-13-return-handoff-claude-ai-strategy-research.md:106:account remains
2026-11-13-return-handoff-claude-ai-strategy-research.md:106:account thresholds
2026-11-13-return-handoff-claude-ai-kimi-research.md:22:account trails
2026-11-13-return-handoff-claude-ai-kimi-research.md:308:user guidelines
2026-11-13-return-handoff-claude-ai-session-close.md:41:account trails
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:17:id excepted
account-id exit=0
/usr/bin/grep -n -o -E '\b(Mr|Mrs|Ms|Dr|Prof)\.? [A-Z][a-z]+' $F; echo "honorific exit=$?"
honorific exit=1
/usr/bin/grep -n -o -E '\[[A-Z][A-Z _-]*\]' $F; echo "bracket-placeholder exit=$?"
bracket-placeholder exit=1
```

### E6. Check (c): names; ambiguous items read by position into a scratch file, not printed (./names2.sh, the 182-column token list is cut from this paste because it holds a word this report may not print; ./names3.sh gives the count after dropping those words and lists person-like tokens)

```
cd /Volumes/Sensidine/Praxis.build/docs/reports
K=2026-11-13-return-handoff-claude-ai-kimi-research.md
sed -n '29p' $K | /usr/bin/grep -o -E '"[A-Z][a-z]+ 2026"' | tr -d '"' | cut -d' ' -f1 > /tmp/rfr-adv2/amb.txt
sed -n '13p' $K | /usr/bin/grep -o -E '\([A-Z][a-z]+ & [A-Z][a-z]+\)' | tr -d '()' | tr '&' '\n' | tr -d ' ' >> /tmp/rfr-adv2/amb.txt
wc -l /tmp/rfr-adv2/amb.txt
       3 /tmp/rfr-adv2/amb.txt
/usr/bin/grep -c -w -F -f /tmp/rfr-adv2/amb.txt 2026-11-13-return-handoff-claude-ai-*.md
2026-11-13-return-handoff-claude-ai-kimi-research.md:6
2026-11-13-return-handoff-claude-ai-session-close.md:1
2026-11-13-return-handoff-claude-ai-strategy-research.md:3
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:0
/usr/bin/grep -o -h -E "\b[A-Z][a-z]+([-'][A-Z][a-z]+)?\b" 2026-11-13-return-handoff-claude-ai-*.md | sort -u | /usr/bin/grep -v -x -F -f /tmp/rfr-adv2/amb.txt | tr '\n' ' ' | fold -w 180; echo
for w in He Swiss Razor Kelly Markowitz Grant Li Han Da Choi Fung; do printf '%s: ' "$w"; /usr/bin/grep -h -o -E ".{0,45}\b$w\b.{0,25}" 2026-11-13-return-handoff-claude-ai-*.md | head -1; done
He:  12:27 ET and reported it matched real time. He looked at the NT8 Contro
Swiss: bon "Noise-Area" intraday momentum breakout (Swiss Finance Institute RP 24-
Razor: o equity source. (Bank of Canada FX fixings)	Razor-thin (est.)	Likely negat
Kelly: , position sizing must utilize a "fractional Kelly" approach mapped exclusi
Markowitz: ategies is a standard risk-control practice (Markowitz framework). We will moni
Grant: New C6. Opening-Bars Momentum (Inspired by Grant et al. 2005)
Li: omentum with a +/-0.30% threshold (Gao, Han, Li & Zhou 2018, JFE) | NOT 
Han: our momentum with a +/-0.30% threshold (Gao, Han, Li & Zhou 2018, JFE) | 
Da: 1. **Top pick: Baltussen, Da, Lammers & Martens (2021
Choi: y volatility or Sharpe metrics. For example, Choi (2021) notes maximum dra
Fung: formance: No published NQ figure. The cited “Fung et al. (JBF) 2000” is ab
/usr/bin/grep -c -w -F -f /tmp/rfr-adv2/amb.txt /Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-research-filing-resume-manager.md
0
cd /Volumes/Sensidine/Praxis.build/docs/reports
printf 'V%sdict\nRet%sred\nVer%sfied\nWork%sng\n' er i i i > /tmp/rfr-adv2/drop.txt
cat /tmp/rfr-adv2/amb.txt /tmp/rfr-adv2/drop.txt > /tmp/rfr-adv2/drop2.txt
/usr/bin/grep -o -h -E "\b[A-Z][a-z]+([-'][A-Z][a-z]+)?\b" 2026-11-13-return-handoff-claude-ai-*.md | sort -u | /usr/bin/grep -v -x -F -f /tmp/rfr-adv2/drop2.txt | wc -l
     482
/usr/bin/grep -o -h -E "\b[A-Z][a-z]+([-'][A-Z][a-z]+)?\b" 2026-11-13-return-handoff-claude-ai-*.md | sort -u | /usr/bin/grep -x -E 'Amear|Baltussen|Barbon|Boyarchenko|Chekhlov|Choi|Da|Fung|Gao|Grant|Han|He|Hu|Kelly|Krohn|Lammers|Li|Lucca-Moench|Ma|Markowitz|Martens|Sharpe|Zarattini-Aziz|Zhang|Zhou|Zhu' | tr '\n' ' '; echo
Amear Baltussen Barbon Boyarchenko Chekhlov Choi Da Fung Gao Grant Han He Hu Kelly Krohn Lammers Li Lucca-Moench Ma Markowitz Martens Sharpe Zarattini-Aziz Zhang Zhou Zhu 
```

### E7. Check (d): MANIFEST row format, writer, unit, DECISION_LOG, endings, level words, report rows, report headings (./rows.sh; the level-word regex in two command lines is a search pattern)

```
cd /Volumes/Sensidine/Praxis.build
wc -l MANIFEST.md
     483 MANIFEST.md
awk -F'|' 'NR>=470 {printf "%d NF=%d path=%s type=%s col3=%s date=%s last5=%s\n", NR, NF, $2, $3, $4, $5, substr($6, length($6)-26)}' MANIFEST.md
470 NF=7 path= /docs/reports/2026-11-13-o4-reduce3-worker1.md  type= Report  col3= 3  date= 2026-11-13  last5=-tree DECISIONS.md :2402). 
471 NF=7 path= /DECISIONS.md  type= Log  col3= 3  date= 2026-11-13  last5=ONLY; F3 and F4 untouched. 
472 NF=7 path= /docs/reports/2026-11-13-open-a1-manager.md  type= Report  col3= 3  date= 2026-11-13  last5=. Ungraded at time of row. 
473 NF=7 path= /docs/reports/2026-11-13-open-a1-worker1.md  type= Report  col3= 3  date= 2026-11-13  last5=. Ungraded at time of row. 
474 NF=7 path= /docs/reports/2026-11-13-open-a1-cure-manager.md  type= Report  col3= 3  date= 2026-11-13  last5= commands and full output. 
475 NF=7 path= /DECISIONS.md  type= Log  col3= 3  date= 2026-11-13  last5=ONLY; F3 and F4 untouched. 
476 NF=7 path= /docs/reports/2026-11-13-open-a2-manager.md  type= Report  col3= 3  date= 2026-11-13  last5=giene counts, entry text). 
477 NF=7 path= /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md  type= Report  col3= 3  date= 2026-11-13  last5=Z; ungraded at time of row 
478 NF=7 path= /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md  type= Report  col3= 3  date= 2026-11-13  last5=Z; ungraded at time of row 
479 NF=7 path= /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md  type= Report  col3= 3  date= 2026-11-13  last5=Z; ungraded at time of row 
480 NF=7 path= /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md  type= Report  col3= 3  date= 2026-11-13  last5=Z; ungraded at time of row 
481 NF=7 path= /docs/reports/2026-11-13-research-filing-resume-manager.md  type= Report  col3= 3  date= 2026-11-13  last5=s; ungraded at time of row 
482 NF=7 path= /docs/reports/2026-11-13-research-filing-worker1.md  type= Report  col3= 3  date= 2026-11-13  last5=6; ungraded at time of row 
483 NF=7 path= /docs/reports/2026-11-13-research-filing-worker2.md  type= Report  col3= 3  date= 2026-11-13  last5=n; ungraded at time of row 
sed -n '470,476p' MANIFEST.md | cut -c1-140
| /docs/reports/2026-11-13-o4-reduce3-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-o4-reduce3: che
| /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a1 (topology OPEN-A1, bead Praxis_build-
| /docs/reports/2026-11-13-open-a1-manager.md | Report | 3 | 2026-11-13 | Manager report for unit 2026-11-13-open-a1 (topology OPEN-A1, bead
| /docs/reports/2026-11-13-open-a1-worker1.md | Report | 3 | 2026-11-13 | ADVERSARIAL worker 1 report for unit 2026-11-13-open-a1: checks (a
| /docs/reports/2026-11-13-open-a1-cure-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a1-cure (topology OP
| /DECISIONS.md | Log | 3 | 2026-11-13 | AMENDMENT ROW (append-only registry). Unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead Praxis_build-f
| /docs/reports/2026-11-13-open-a2-manager.md | Report | 3 | 2026-11-13 | Evidence report for unit 2026-11-13-open-a2 (ruleset OPEN-A2, bead
tail -n 7 MANIFEST.md | /usr/bin/grep -n -o -i -E 'built|tested|verified|working|viable|retired|decided'; echo "level-word substring exit=$?"
level-word substring exit=1
git diff MANIFEST.md | /usr/bin/grep '^+' | /usr/bin/grep -c -i -E 'built|tested|verified|working|viable|retired|decided'
1
git diff MANIFEST.md | /usr/bin/grep '^+' | /usr/bin/grep -v '^+++' | tail -n 7 | cmp - <(tail -n 7 MANIFEST.md | sed 's/^/+/'); echo "last 7 added lines = last 7 rows exit=$?"
tail -n 7 MANIFEST.md | sed 's/^/+/'
last 7 added lines = last 7 rows exit=0
tail -n 7 MANIFEST.md | /usr/bin/grep -o -E 'written by [^:;,(]*|unit 2026-11-13-research-filing[a-z-]*|DECISION_LOG 2026-11-13T[0-9:]*Z|ungraded at time of row \|$' | sort | uniq -c
   7 DECISION_LOG 2026-11-13T19:40:54Z
   1 DECISION_LOG 2026-11-13T19:58:43Z
   7 ungraded at time of row |
   5 unit 2026-11-13-research-filing
   1 written by praxis-manager for unit 2026-11-13-research-filing-resume 
   2 written by praxis-worker for unit 2026-11-13-research-filing 
   4 written by the Claude.ai Praxis channel
tail -n 7 MANIFEST.md | /usr/bin/grep -c -E '; ungraded at time of row \|$'
7
for f in docs/reports/2026-11-13-research-filing-resume-manager.md docs/reports/2026-11-13-research-filing-worker1.md docs/reports/2026-11-13-research-filing-worker2.md docs/reports/2026-11-13-research-filing-manager.md docs/reports/2026-11-13-research-filing-resume-worker1.md; do printf '%s rows=' "$f"; /usr/bin/grep -c -F "| /$f |" MANIFEST.md; done
docs/reports/2026-11-13-research-filing-resume-manager.md rows=1
docs/reports/2026-11-13-research-filing-worker1.md rows=1
docs/reports/2026-11-13-research-filing-worker2.md rows=1
docs/reports/2026-11-13-research-filing-manager.md rows=0
docs/reports/2026-11-13-research-filing-resume-worker1.md rows=0
/usr/bin/grep -n -E '^(## |### |Result:)' docs/reports/2026-11-13-research-filing-worker2.md | cut -c1-140
3:## Task
7:## Mode
11:## Criterion
15:## Checks
17:### (a) Diffs are deletions allowed by rule A only; each deleted line sits outside pasted material: PASS
26:### (b) The S13 sentence appears on exactly one standalone line outside pasted material in each file: PASS
30:### (c) PII scan: PASS
40:Result: zero unreplaced hits apart from published-paper authors, the two ambiguous citations above, and Amear.
42:### (d) The last five MANIFEST rows match their diffs, contain no level words, and use the existing format: PASS
54:### (e) Blob checks: PASS
58:### (f) No tracked file other than MANIFEST.md changed: PASS
62:## Defects
72:## Verification evidence (command output)
74:### E1. Checks (a) and (b): diffs, tails, structure, S13 counts, brief and appendix scans
241:## Appendix A: Kimi Deep Research output, unedited (as Amear supplied $
260:### E2. Check (c): PII pattern scan of the four filed files
286:## email
288:## at-handles
292:## ipv4
294:## ipv6
296:## mac
298:## hostnames
304:## user-paths
307:## ssh-keys
309:## placeholders
311:## people-words
324:## email
326:## at-handles
330:## ipv4
332:## ipv6
334:## mac
336:## hostnames
338:## user-paths
341:## ssh-keys
343:## placeholders
345:## people-words
349:### E3. Checks (c) and (d): content claims, format, ambiguous-citation counts
377:## strategy: cross-check, sections, fence
384:## kimi: audit sections, appendix
391:## session-close: sections, table, withdrawal
400:## vm-queue: replaces bullet, pasted by Amear, table, sections
411:## manager report headings
421:## lines starting with > in the four files
426:## earlier return-handoff MANIFEST rows (cols 1-4)
437:## ambiguous citation counts
456:### E4. Checks (d) and (e): level words, column shape, blob and diff checks
561:### E5. Check (f): diff-stat comparison, new DISPATCH_LOG rows, mtimes
603:## Files staged
607:## Result
611:Result: PASS
/usr/bin/grep -n -E '^Result:' docs/reports/2026-11-13-research-filing-worker1.md docs/reports/2026-11-13-research-filing-resume-worker1.md docs/reports/2026-11-13-research-filing-manager.md
docs/reports/2026-11-13-research-filing-worker1.md:310:Result: PASS
docs/reports/2026-11-13-research-filing-resume-worker1.md:465:Result: BLOCKED (pending the cold adversary)
docs/reports/2026-11-13-research-filing-resume-worker1.md:597:Result: FAIL
docs/reports/2026-11-13-research-filing-manager.md:27:Result: BLOCKED (report in progress)
wc -l docs/reports/2026-11-13-research-filing-manager.md
      29 docs/reports/2026-11-13-research-filing-manager.md
```

### E8. Checks (e), (f), (g): blob, tracked files against the baseline, stub report, hook bindings (./blob.sh, ./tracked.sh, ./stub.sh, ./hooks.sh)

```
cd /Volumes/Sensidine/Praxis.build
wc -l /tmp/rf-manifest-blob.md
     460 /tmp/rf-manifest-blob.md
git show HEAD:MANIFEST.md | wc -l
     453
head -n 453 /tmp/rf-manifest-blob.md | cmp - <(git show HEAD:MANIFEST.md); echo "head-453 vs HEAD exit=$?"
git show HEAD:MANIFEST.md
head-453 vs HEAD exit=0
cmp <(tail -n 7 /tmp/rf-manifest-blob.md) <(tail -n 7 MANIFEST.md); echo "tail-7 exit=$?"
tail -n 7 /tmp/rf-manifest-blob.md
tail -n 7 MANIFEST.md
tail-7 exit=0
cmp /tmp/rf-manifest-blob.md <(git show HEAD:MANIFEST.md; tail -n 7 MANIFEST.md); echo "whole blob = HEAD + last 7 exit=$?"
git show HEAD:MANIFEST.md; tail -n 7 MANIFEST.md
whole blob = HEAD + last 7 exit=0
shasum -a 256 /tmp/rf-manifest-blob.md
e2189a430dd5da269e36a1f210dd4b2172cb8272c0c8bcafbdfa28ec015614d7  /tmp/rf-manifest-blob.md
tail -c 1 /tmp/rf-manifest-blob.md | od -An -c
          \n                                                            

git diff MANIFEST.md | /usr/bin/grep -c '^-[^-]'
0
git diff MANIFEST.md | /usr/bin/grep -c '^+[^+]'
30
git diff MANIFEST.md | /usr/bin/grep '^+[^+]' | head -n 23 > /tmp/rfr-adv2/earlier23.now
awk '/^diff --git a\/MANIFEST.md/{f=1;next} /^diff --git /{f=0} f' /tmp/rfr/gitdiff-before.patch | /usr/bin/grep '^+[^+]' > /tmp/rfr-adv2/manifest-added.before
wc -l /tmp/rfr-adv2/manifest-added.before
      28 /tmp/rfr-adv2/manifest-added.before
head -n 23 /tmp/rfr-adv2/manifest-added.before | cmp - /tmp/rfr-adv2/earlier23.now; echo "earlier 23 added lines unchanged vs baseline patch exit=$?"
earlier 23 added lines unchanged vs baseline patch exit=0
sed -n '24,28p' /tmp/rfr-adv2/manifest-added.before | cut -d'|' -f2
 /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md 
 /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md 
 /docs/reports/2026-11-13-research-filing-manager.md 
awk '/^diff --git a\/MANIFEST.md/{f=1;next} /^diff --git /{f=0} f' /tmp/rfr/gitdiff-before.patch | /usr/bin/grep -c '^-[^-]'
0
head -n 480 /tmp/rfr/MANIFEST.before.md | cmp - <(head -n 480 MANIFEST.md); echo "MANIFEST :1-:480 unchanged vs baseline copy exit=$?"
head -n 480 MANIFEST.md
MANIFEST :1-:480 unchanged vs baseline copy exit=0
shasum -a 256 /tmp/rfr/MANIFEST.before.md
4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656  /tmp/rfr/MANIFEST.before.md
/usr/bin/grep -F 'MANIFEST.md' /tmp/rfr/tracked-sha-before.txt
SHA2-256(MANIFEST.md)= 4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656
git diff MANIFEST.md | /usr/bin/grep '^@@'
@@ -304,6 +304,14 @@
@@ -429,6 +437,12 @@
@@ -443,11 +457,27 @@
cd /Volumes/Sensidine/Praxis.build
date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-13T20:14:33Z
git diff --name-only | while read f; do openssl dgst -sha256 "$f"; done > /tmp/rfr-adv2/tracked-sha-now.txt
diff /tmp/rfr/tracked-sha-before.txt /tmp/rfr-adv2/tracked-sha-now.txt; echo "diff exit=$?"
5c5
< SHA2-256(DISPATCH_LOG.md)= dd16a2d8a079d2434236e435379f14d222d6b3cd0014aa653be6eba387cc8970
---
> SHA2-256(DISPATCH_LOG.md)= ebbea6b7c39f2ee630eb15d038a6e51e11686ed194c71ffa6688f572cda4d126
8c8
< SHA2-256(MANIFEST.md)= 4140b0e9dded4887c09c34b55497101a2d2d54d484baa3e502401e96743e9656
---
> SHA2-256(MANIFEST.md)= 5e36b13f389c2990dbc3c649662a4f0983bd16f8a5bf23e6c0d11c32ef38593a
diff exit=1
git diff --stat > /tmp/rfr-adv2/diffstat-now.txt
diff /tmp/rfr/diffstat-before.txt /tmp/rfr-adv2/diffstat-now.txt; echo "diff exit=$?"
5c5
<  DISPATCH_LOG.md                                    |  30 ++++++
---
>  DISPATCH_LOG.md                                    |  35 +++++++
8c8
<  MANIFEST.md                                        |  28 ++++++
---
>  MANIFEST.md                                        |  30 ++++++
15c15
<  14 files changed, 536 insertions(+), 32 deletions(-)
---
>  14 files changed, 543 insertions(+), 32 deletions(-)
diff exit=1
git diff --name-only | wc -l
      14
git diff --name-only | cmp - <(sed -E 's/^SHA2-256\((.*)\)= .*/\1/' /tmp/rfr/tracked-sha-before.txt); echo "same tracked-modified path set exit=$?"
sed -E 's/^SHA2-256\((.*)\)= .*/\1/' /tmp/rfr/tracked-sha-before.txt
same tracked-modified path set exit=0
head -c $(wc -c < /tmp/rfr/DISPATCH_LOG.before.md) DISPATCH_LOG.md | cmp - /tmp/rfr/DISPATCH_LOG.before.md; echo "DISPATCH_LOG prefix = baseline exit=$?"
wc -c < /tmp/rfr/DISPATCH_LOG.before.md
DISPATCH_LOG prefix = baseline exit=0
diff /tmp/rfr/DISPATCH_LOG.before.md DISPATCH_LOG.md | cut -c1-170; echo "diff exit=${PIPESTATUS[0]}"
2799a2800,2804
> - [2026-11-13T20:02:04Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a20a17e4d551d2c5f | WHEN: spawn
> - [2026-11-13T20:03:55Z] WHO: praxis-manager | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a8a6966c3548284a8, matched 1 open row(s)
> - [2026-11-13T20:09:58Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a20a17e4d551d2c5f, matched 1 open row(s) 
> - [2026-11-13T20:09:58Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a8a6966c3548284a8 | WHEN: spaw
> - [2026-11-13T20:11:40Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a6783c300b286cc33 | WHEN: spawn
diff exit=1
diff /tmp/rfr/DISPATCH_LOG.before.md DISPATCH_LOG.md | /usr/bin/grep '^>' | /usr/bin/grep -v -c 'WHY: hook-recorded at Subagent'
0
git diff --quiet -- .claude/settings.json; echo "settings diff-quiet exit=$?"
settings diff-quiet exit=1
openssl dgst -sha256 .claude/settings.json
SHA2-256(.claude/settings.json)= 98ac1ec8802cd6c02a04d8f24382c72a53162bfac41ca41ccff13bf199d92115
cd /Volumes/Sensidine/Praxis.build
shasum -a 256 docs/reports/2026-11-13-research-filing-manager.md
eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f  docs/reports/2026-11-13-research-filing-manager.md
[ "$(shasum -a 256 < docs/reports/2026-11-13-research-filing-manager.md | cut -c1-64)" = eeef330ab3c52b323f3e214544f2292c657eb1424dd667c27e5f851079f54c5f ]; echo "stub sha match exit=$?"
shasum -a 256 < docs/reports/2026-11-13-research-filing-manager.md | cut -c1-64
stub sha match exit=0
git ls-files --error-unmatch docs/reports/2026-11-13-research-filing-manager.md; echo "ls-files exit=$?"
error: pathspec 'docs/reports/2026-11-13-research-filing-manager.md' did not match any file(s) known to git
Did you forget to 'git add'?
ls-files exit=1
git ls-files -s docs/reports/2026-11-13-research-filing-manager.md | wc -l
       0
git ls-files --others --exclude-standard docs/reports/2026-11-13-research-filing-manager.md
docs/reports/2026-11-13-research-filing-manager.md
git cat-file -e HEAD:docs/reports/2026-11-13-research-filing-manager.md; echo "in HEAD exit=$?"
fatal: path 'docs/reports/2026-11-13-research-filing-manager.md' exists on disk, but not in 'HEAD'
in HEAD exit=128
for f in docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-research-filing-worker1.md docs/reports/2026-11-13-research-filing-worker2.md docs/reports/2026-11-13-research-filing-resume-manager.md docs/reports/2026-11-13-research-filing-resume-worker1.md; do printf '%s index-entries=' "$f"; git ls-files -s "$f" | wc -l | tr -d ' '; done
docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md index-entries=0
docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md index-entries=0
docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md index-entries=0
docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md index-entries=0
docs/reports/2026-11-13-research-filing-worker1.md index-entries=0
docs/reports/2026-11-13-research-filing-worker2.md index-entries=0
docs/reports/2026-11-13-research-filing-resume-manager.md index-entries=0
docs/reports/2026-11-13-research-filing-resume-worker1.md index-entries=0
cd /Volumes/Sensidine/Praxis.build
sed -n '135,163p' .claude/settings.json | /usr/bin/grep -n -E '"Subagent|"matcher"|"command"'
1:    "SubagentStart": [
5:            "type": "command",
6:            "command": "./scripts/dispatch-log-writeahead.sh"
11:    "SubagentStop": [
13:        "matcher": "^praxis-manager$",
16:            "type": "command",
17:            "command": "./scripts/gate-manager-output.sh"
24:            "type": "command",
25:            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/dispatch-log-close.sh",
/usr/bin/grep -n -o -F 'WHY: hook-recorded at SubagentStart' scripts/dispatch-log-writeahead.sh
109:WHY: hook-recorded at SubagentStart
/usr/bin/grep -n -o -F 'WHY: hook-recorded at SubagentStop' scripts/dispatch-log-close.sh
287:WHY: hook-recorded at SubagentStop
```

### E9. Manager report rules, quotation spot-check, pasted-output completeness, writes under .claude (./mgr2.sh, ./quotes2.sh, ./pastes.sh, ./final.sh)

```
cd /Volumes/Sensidine/Praxis.build
M=docs/reports/2026-11-13-research-filing-resume-manager.md
printf 'v%sdict\nCOMMIT-%s\nCOMMIT-DIFF-%s\n' er INDEX SHA256 > /tmp/rfr-adv2/forbid.txt
wc -l /tmp/rfr-adv2/forbid.txt
       3 /tmp/rfr-adv2/forbid.txt
/usr/bin/grep -n -i -F -f /tmp/rfr-adv2/forbid.txt $M; echo "forbidden-word exit=$?"
forbidden-word exit=1
wc -l $M
     592 docs/reports/2026-11-13-research-filing-resume-manager.md
/usr/bin/grep -n '^Result:' $M
590:Result: BLOCKED (interim: adversary round 2 pending; step 4 not met as written, see E8)
/usr/bin/grep -n -x '## Verification evidence (command output)' $M
47:## Verification evidence (command output)
/usr/bin/grep -n -x -F -f /tmp/rfr-adv2/s13.txt $M | cut -d: -f1
592
/usr/bin/grep -n -F -f /tmp/rfr-adv2/s13.txt $M | cut -d: -f1 | tr '\n' ' '; echo
191 195 592 
sed -n '191p;195p' $M | cut -c1-2 | od -An -c
           <      \n   <      \n                                        

awk 'NR<190 || NR>196' $M | /usr/bin/grep -n -F -f /tmp/rfr-adv2/s13.txt | cut -d: -f1
585
awk '/^```/{c++} END{print "fence lines:", c}' $M
fence lines: 28
awk '/^```/{c++; next} c%2==1 && (NR==191 || NR==195){print NR": inside a fence"}' $M
191: inside a fence
195: inside a fence
tail -n 1 $M | cmp - /tmp/rfr-adv2/s13.txt; echo "last line = S13 sentence exit=$?"
last line = S13 sentence exit=0
sed -n '321p' $M | /usr/bin/grep -o -E '"C:[^"]*"' | od -c
0000000    "   C   :   \   p   r   a   x   i   s  \v   m   -   b   r   i
0000020    d   g   e   "  \n                                            
0000025
sed -n '5p' docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | /usr/bin/grep -o -E 'C:[^`]*' | od -c
0000000    C   :   \   p   r   a   x   i   s   \   v   m   -   b   r   i
0000020    d   g   e  \n                                                
0000024
sed -n '321p' $M | /usr/bin/grep -o -E '"C:[^"]*"' | tr -d '"' > /tmp/rfr-adv2/q-cpath.txt
/usr/bin/grep -c -F -f /tmp/rfr-adv2/q-cpath.txt docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
0
LC_ALL=C /usr/bin/grep -n "$(printf '\013')" $M | cut -d: -f1
printf '\013'
321
sed -n '321p' $M | /usr/bin/grep -o -E 'price and size shorthand \([^)]*\)'
price and size shorthand ("@15:30", "@25k" and so on)
sed -n '217p' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | /usr/bin/grep -o -E '.{0,25}@15:30.{0,10}'
30–10:00 > +0.30% → long @15:30; <–0.30% 
cd /Volumes/Sensidine/Praxis.build
M=docs/reports/2026-11-13-research-filing-resume-manager.md
sed -n '558,564p' $M > /tmp/rfr-adv2/r1grades.txt
/usr/bin/grep -c -x -F -f /tmp/rfr-adv2/r1grades.txt docs/reports/2026-11-13-research-filing-resume-worker1.md
7
/usr/bin/grep -c -F '(in progress)' docs/reports/2026-11-13-research-filing-manager.md
5
/usr/bin/grep -c -F '(pending)' docs/reports/2026-11-13-research-filing-resume-worker1.md
4
/usr/bin/grep -c -F 'rep who answered on 11-12' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
1
/usr/bin/grep -c -F '2 ticks/side slippage' docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
2
/usr/bin/grep -c -F '15:30:' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
1
/usr/bin/grep -c -F '@15:30' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
1
/usr/bin/grep -c -F '@25k' docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
1
/usr/bin/grep -c -F 'hook-recorded at SubagentStart' DISPATCH_LOG.md
1078
/usr/bin/grep -c -F 'hook-recorded at SubagentStop' DISPATCH_LOG.md
870
/usr/bin/grep -c -F 'once' specs/SPEC_RUBRIC.md
3
/usr/bin/grep -o -h -E "\b[A-Z][a-z]+([-'][A-Z][a-z]+)?\b" $M | sort -u | tr '\n' ' '; echo
Adversarial Agent All Allowed Amear An Appendix Authority Baselines Blob Both Channel Claude Code Consistency Content Cure Deep Defects Did Dispatched Downloads Dr During Each Evaluation False Files Fills First Follow From Gao Gemini Graded Grades House In Intraday Its Kimi Last Left Let Lost Made Maintain Manager Max Momentum Mr Mrs Ms Must Negative Net No Not Nothing Nov Observations Only Praxis Process Prof Profit Read Rebuild Recommended Removing Replaced Report Research Result Results Resume Return Round Rubric Rules Run Sensidine Session Sim Standa Standard Step Stub Task The This Timestamps Today Trades Two Unit Users Verification Volumes What Where Work Workers Za 
M=/Volumes/Sensidine/Praxis.build/docs/reports/2026-11-13-research-filing-resume-manager.md
for o in rebuild2 step1a step2b pii names rows2 manifest-edit blob step4 mem; do n=$(wc -l < /tmp/rfr/$o.out | tr -d ' '); printf '%s.out lines=%s ' $o $n; /usr/bin/grep -c -x -F -f /tmp/rfr/$o.out $M | tr '\n' ' '; awk 'NR==FNR{a[$0]=1;next} !($0 in a){c++} END{printf "out-lines-not-in-report=%d\n", c+0}' $M /tmp/rfr/$o.out; done
wc -l < /tmp/rfr/$o.out | tr -d ' '
rebuild2.out lines=47 142 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
step1a.out lines=34 111 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
step2b.out lines=32 38 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
pii.out lines=27 30 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
names.out lines=12 15 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
rows2.out lines=40 46 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
manifest-edit.out lines=19 45 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
blob.out lines=53 126 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
step4.out lines=49 62 out-lines-not-in-report=0
wc -l < /tmp/rfr/$o.out | tr -d ' '
mem.out lines=10 17 out-lines-not-in-report=0
cd /Volumes/Sensidine/Praxis.build
find .claude -newer /tmp/rfr-adv2/s13make.sh -type f | /usr/bin/grep -v -c '^.claude/state/'
0
find .claude -newer /tmp/rfr-adv2/s13make.sh -type f | /usr/bin/grep -c '^.claude/state/'
0
ls -lT /tmp/rfr-adv2/s13make.sh | cut -c30-
01 Nov 13 15:12:22 2026 /tmp/rfr-adv2/s13make.sh
```

## Files staged

None. This report (docs/reports/2026-11-13-research-filing-resume-worker2.md) is the only repo file written, and it is not staged. Scratch files are in /tmp/rfr-adv2/.

Result: FAIL

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
