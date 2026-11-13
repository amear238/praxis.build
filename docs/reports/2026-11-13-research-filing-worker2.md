# Unit 2026-11-13-research-filing, round 1: ADVERSARIAL worker 2 report

## Task

Find defects in the filing edits of unit 2026-11-13-research-filing (authority: DECISION_LOG 2026-11-13T19:40:54Z, decided by master under D-2026-11-08-D D1). The artifacts are the four filed channel files `docs/reports/2026-11-13-return-handoff-claude-ai-{strategy-research,kimi-research,session-close,vm-queue-results}.md`, their received copies in `/tmp/rf-pre/`, the MANIFEST commit blob `/tmp/rf-manifest-blob.md`, the working-tree `MANIFEST.md`, and the diff-stat snapshot `/tmp/rf-diffstat-before.txt`. Read-only: the only file written is this report. Nothing was staged, and no git command that touches the index was run.

## Mode

ADVERSARIAL. I was given the artifact and the rules the editor was held to. I was not given the editor's reasoning, except that I read the worker 1 report's de-identification notes to see which ambiguous items it listed.

## Criterion

specs/SPEC_RUBRIC.md S1 (:133), S2 (:134), S8 (:140), S13 (:145), using the house reading of S13 "once": the sentence is counted on standalone lines outside quoted commands, code blocks and pasted drafts.

## Checks

### (a) Diffs are deletions allowed by rule A only; each deleted line sits outside pasted material: PASS

- Every diff is pure deletion of one line that is byte-exactly the S13 sentence: strategy-research received :108, kimi-research received :42 and :330, session-close received :55, vm-queue-results received :45. There are no `c` (change) or `a` (add) hunks, so no placeholder replacements and no other edits were made.
- strategy-research :108. This is the last line of the file. It comes after a blank :107 and sits below the heading at :96, which says Appendix A holds the Gemini output unedited. I checked whether it could be part of the Gemini paste. (1) The Gemini appendix's thirteen lines (:96-:108) contain the S13 wording only at relative line 13, which is :108; no Gemini paragraph has the wording anywhere else. (2) The Gemini paragraphs run together with no blank lines between them ("line breaks as received"). :108 is set off by a blank line, the same layout the channel uses for the footer copy in session-close (:54 blank, :55 sentence) and in vm-queue-results (:44 blank, :45 sentence). Neither of those files has an appendix. (3) The Gemini brief is not in the repo (grep for "gemini" under docs/briefs and specs: rc=1), so I cannot rule out that it asked Gemini to print the sentence. That point is UNVERIFIED. The weight of the evidence is that :108 is the channel's own footer, outside the pasted output, so I do not count it as a defect.
- kimi-research :42. This is the channel's own text. It closes the channel's audit block (:8-:41: header "Original, filed unedited: ..." and "Auditor: Claude.ai channel", then the What holds, Defects and Recommended next steps sections). It comes before the heading at :44, which opens the Kimi appendix. The audit block is written by the channel and is not a brief or prompt for another tool. No code fence or block quote surrounds it: the files have no lines starting with `>` and kimi-research has no fences. Rule A therefore required deleting it.
- kimi-research :330. This is the last line, after a blank :329, inside the span of the Kimi appendix (:44 onward). The Kimi brief that the Kimi run answered (strategy-research received :34-:94, inside a code fence) does not contain the S13 wording. grep for `standard resolution|ticks/side|fills are|limitation|final line|footer` in :34-:94 returned rc=1. The Kimi output therefore was not asked for the sentence. Inside :44-:330 the wording occurs only at :330. It is the channel's footer, the same pattern as in the other three files. Deleting it was correct.
- session-close :55 and vm-queue-results :45. Each is the last line of a file that has no appendix, no fence and no block quote. Both are channel footers, and deleting them was correct.
- Trailing state. Every received file ended `...ed.\n`, with the S13 sentence as its last line. Every filed file now ends `<text>\n\n`, which is one trailing blank line (the blank line that came before the deleted footer). That is not "two blank lines in a row at the end of the file", so rule A did not call for removing a further blank line, and none was removed. The only new double blank in any file is kimi-research post :41-:42, in the middle of the file. Rule A's blank-line clause covers only the end of a file, so leaving it is correct, and the kimi MANIFEST row records it.

### (b) The S13 sentence appears on exactly one standalone line outside pasted material in each file: PASS

`grep -n -F` and `grep -n -x -F` each return exactly one line per filed file: strategy :5, kimi :5, session-close :5, vm-queue :7. Each kept copy is the first one, in the channel's own header text, before any section heading. No copy is left inside pasted material: neither filed file with an appendix keeps the sentence anywhere except :5.

### (c) PII scan: PASS

My own scan (script and output below) found:
- No email addresses, IPv4, IPv6, MAC addresses, private hostnames, SSH key names or paths, or `C:\Users\`, `/Users/` or `/home/` paths. No placeholders were added, which is correct because none were needed.
- False positives: two `@` hits in kimi-research :217 and :230 are price and size notation (`@15:30`, `@25k`), not handles. The four "win-rate" hits come from the `WIN-` hostname pattern matching the word "win-rate". One Windows path, vm-queue-results :5, is a project working directory on the VM with no user-name segment, so it is not personal.
- People words: session-close :48 refers to "the human rep" with no name. The other hits are the word "support" in the sense of evidence.
- Full read of session-close (54 lines) and vm-queue-results (44 lines): no private person is named. The names that appear are Amear (stays), the channel, the VM agent, praxis-master, and organisations or products (MFFU, NT8, CME). "PID 11820" is an operating-system process id.
- Capitalised name-pair scan of strategy-research and kimi-research: every hit is a term, an organisation, or a published-author citation (for example the Baltussen, Da, Lammers and Martens 2021 JFE paper, and Gao, Han, Li and Zhou 2018). Those stay under rule B.
- Ambiguous citations, left in place, as rule B requires: (1) a two-surname author pair dated 2026, cited by the Gemini output, that the channel could not identify and marks withdrawn. It appears 3 times in strategy-research, 2 in kimi-research and 1 in session-close, and is a cited (possibly non-existent) source, not a private person in PRAXIS's dealings. (2) A single-surname practitioner source dated 2026 in kimi-research (post :29, :92, :96, :102; received :29, :93, :97, :103), which Kimi cites for gap-fade backtests. It is a cited author of a public source, not a private person. Worker 1 lists both.

Result: zero unreplaced hits apart from published-paper authors, the two ambiguous citations above, and Amear.

### (d) The last five MANIFEST rows match their diffs, contain no level words, and use the existing format: PASS

- Line numbers match the diffs. The rows say: strategy "received :108 deleted ... kept once, at :5"; kimi "received :42 and :330 deleted ... kept once, at :5 ... two adjacent blank lines at :41-:42"; session-close "received :55 ... kept once, at :5"; vm-queue "received :45 ... kept once, at :7". Each matches (a) and (b).
- `grep -n -i -w -E 'built|tested|verified|working|viable|retired|decided'` over the last five rows returns rc=1, meaning no hits.
- Format matches the existing rows: 5 fields; a path with a leading slash; `Report | 3 | 2026-11-13`. This is the same as the neighbouring rows and the earlier return-handoff rows (MANIFEST :389, :427).
- Content claims, each checked against the file text:
  - Strategy row. Gemini output as received is in Appendix A, :96. The channel's audit is section 2, at :15 (that heading line is not pasted below because it carries a word this report may not use; the script prints only section 3 and the appendices). The "read-only repo cross-check" is at :26, which begins "Repo cross-check (OBSERVED by the channel, read-only, 2026-11-13)". The backtest-order recommendation is section 3, at :28. The Kimi brief is in Appendix B, inside a code fence at :34-:94.
  - Kimi row. The audit has three sections: What holds (:15), Defects (:24) and Recommended next steps (:35). The Kimi output is Appendix A, at post :43 (received :44).
  - Session-close row. Amear's instruction is section 1. The correction withdrawing the recommendation to backtest PraxisLastHalfHourMomentum, citing D-2026-11-02-A, is section 2, at :18-:20. The status table of candidates from both runs is at :28-:35. The other updates are section 4.
  - VM-queue row. It states that it replaces the VM bridge queue bullet (file :3). It reports runs T1-T3 by the VM Claude Code session, pasted by Amear (:5). The per-run trades, net, profit factor and max drawdown are in the table at :13-:17. Deviations are section 2, the INFERRED reading is section 3, and the items left are section 4.
  - Manager row. The manager report exists (29 lines) and has Process log, Verification evidence and Adversarial findings headings.

### (e) Blob checks: PASS

N=453. `head -n 453` of the blob cmp-equals HEAD:MANIFEST.md. The blob's last 5 lines cmp-equal the working tree's last 5. The blob has 458 lines, which is N+5, and ends with a newline. `git diff MANIFEST.md` shows 28 added rows and 0 removed. The 5 last added rows cmp-equal the blob's last 5. The other 23 added rows all belong to earlier units, and none mentions this unit or its four files. They are interleaved in three hunks (HEAD :304, :429, :443), which is why HEAD is not a byte prefix of the working tree. That layout predates this unit: the snapshot shows `MANIFEST.md | 23 +++++` before the unit started. The snapshot holds counts only, so "same as before" is shown by count (23 before, 23 non-unit rows now) and by their paths, not by a byte comparison with a pre-unit copy, which does not exist.

### (f) No tracked file other than MANIFEST.md changed: PASS

The diff-stat comparison differs only in MANIFEST.md (23 to 28, this unit's 5 rows), DISPATCH_LOG.md (23 to 28) and the totals line. The 5 new DISPATCH_LOG rows (19:42:27Z to 19:47:00Z, all after the snapshot at 19:41:56Z) are all `hook-recorded at SubagentStart` or `hook-recorded at SubagentStop` spawn and close rows, not authored content. As a supplementary check, every other modified tracked file has an mtime of 17:37:18Z to 17:41:04Z, before the authority row, except DECISION_LOG.md at 19:41:05Z. That is earlier than the snapshot (19:41:56Z), and its diff-stat count is unchanged at 13.

## Defects

None found.

Observations, which are not defects and were not acted on:
1. Each of the four filed files now ends with one trailing blank line (`\n\n`), the blank line that came before the deleted footer. Rule A only asked for a blank line to be removed when two remained at the end, so this is allowed. A later reader may still notice it.
2. Whether strategy-research received :108 was echoed by Gemini rests on a brief that is not in the repo (UNVERIFIED). The layout and the channel's four-file footer pattern point to channel text.
3. Check (f) works on diff-stat counts plus mtimes. A same-count content edit to a tracked file during the unit would not show up in the diff-stat comparison, but it would show up as an mtime after 19:41:56Z, and none does apart from MANIFEST.md and DISPATCH_LOG.md.
4. The worker reports for this unit (worker 1 and this one) have no MANIFEST rows. The brief asked for exactly five rows, so this is for the manager to decide.

## Verification evidence (command output)

### E1. Checks (a) and (b): diffs, tails, structure, S13 counts, brief and appendix scans

Script `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/ab.sh`:

```
#!/bin/bash
# Checks (a) and (b). Run: bash ab.sh
cd /Volumes/Sensidine/Praxis.build || exit 2
S='Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.'
for f in strategy-research kimi-research session-close vm-queue-results; do
  X=2026-11-13-return-handoff-claude-ai-$f.md
  echo "=== diff /tmp/rf-pre/$X docs/reports/$X"
  diff /tmp/rf-pre/$X docs/reports/$X; echo "diff rc=$?"
  echo "line counts pre/post: $(wc -l < /tmp/rf-pre/$X | tr -d ' ') / $(wc -l < docs/reports/$X | tr -d ' ')"
  echo "pre tail -c 4:"; tail -c 4 /tmp/rf-pre/$X | od -c | head -n 1
  echo "post tail -c 4:"; tail -c 4 docs/reports/$X | od -c | head -n 1
  echo "pre structure (headings, fences, block quotes; lines with the word v-e-r-d-i-c-t filtered, count follows):"
  /usr/bin/grep -n -E '^(#|```|~~~|>)' /tmp/rf-pre/$X | /usr/bin/grep -v -i 'v[e]rdict' | cut -c1-110
  echo "  filtered structure lines: $(/usr/bin/grep -E '^(#|```|~~~|>)' /tmp/rf-pre/$X | /usr/bin/grep -c -i 'v[e]rdict')"
  echo "pre consecutive-blank-line pairs (line no. of second blank):"; awk 'p=="" && $0=="" {print "  pre " NR} {p=$0}' /tmp/rf-pre/$X
  echo "post consecutive-blank-line pairs:"; awk 'p=="" && $0=="" {print "  post " NR} {p=$0}' docs/reports/$X
  echo "--- (b) post grep -n -F"; /usr/bin/grep -n -F "$S" docs/reports/$X
  echo "--- (b) post grep -n -x -F"; /usr/bin/grep -n -x -F "$S" docs/reports/$X
done
echo "=== Kimi brief (strategy-research received :34-:94, fenced) asks for the S13 wording?"
sed -n '34,94p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-strategy-research.md | /usr/bin/grep -n -i -E 'standard resolution|ticks/side|fills are|limitation|final line|footer'; echo "rc=$?"
echo "=== S13 wording inside Gemini appendix (received :96-:108), relative line numbers"
sed -n '96,108p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-strategy-research.md | /usr/bin/grep -n -i -E 'standard resolution|ticks/side|fills are'; echo "rc=$?"
echo "=== S13 wording inside Kimi appendix (received :44-:330), relative line numbers"
sed -n '44,330p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-kimi-research.md | /usr/bin/grep -n -i -E 'standard resolution|ticks/side|fills are'; echo "rc=$?"
echo "=== Gemini brief present anywhere under docs/briefs or specs?"
/usr/bin/grep -rn -l -i 'gemini' /Volumes/Sensidine/Praxis.build/docs/briefs /Volumes/Sensidine/Praxis.build/specs 2>/dev/null; echo "rc=$?"
echo "=== context, strategy-research received :105-:108 (first 70 chars)"
sed -n '105,108p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-strategy-research.md | cut -c1-70 | cat -e
echo "=== context, kimi received :5-:9, :38-:46, :326-:330 (first 70 chars)"
sed -n '5,9p;38,46p;326,330p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-kimi-research.md | cut -c1-70 | cat -e
echo "=== context, session-close received :52-:55 and vm-queue received :42-:45 (first 70 chars)"
sed -n '52,55p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-session-close.md | cut -c1-70 | cat -e
sed -n '42,45p' /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | cut -c1-70 | cat -e
```

Command and full output:

```
$ bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/ab.sh
=== diff /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-strategy-research.md docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md
108d107
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff rc=1
line counts pre/post: 108 / 107
pre tail -c 4:
0000000    e   d   .  \n                                                
post tail -c 4:
0000000    t   .  \n  \n                                                
pre structure (headings, fences, block quotes; lines with the word v-e-r-d-i-c-t filtered, count follows):
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: replacement-strategy research (Gemi
7:## 1. What happened (REPORTED BY the Claude.ai channel)
28:## 3. Channel recommendation (the channel's, not an Amear ruling; master decides under D1)
32:## Appendix B: Kimi Deep Research follow-up brief (as given to Amear, 2026-11-13 14:10 ET)
34:```
94:```
96:## Appendix A: Gemini Deep Research output, unedited (as Amear supplied it; line breaks as received)
  filtered structure lines: 1
pre consecutive-blank-line pairs (line no. of second blank):
post consecutive-blank-line pairs:
--- (b) post grep -n -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
--- (b) post grep -n -x -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
=== diff /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-kimi-research.md docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md
42d41
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
330d328
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff rc=1
line counts pre/post: 330 / 328
pre tail -c 4:
0000000    e   d   .  \n                                                
post tail -c 4:
0000000    e   .  \n  \n                                                
pre structure (headings, fences, block quotes; lines with the word v-e-r-d-i-c-t filtered, count follows):
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13: Kimi Deep Research follow-up + audi
15:## What holds
24:## Defects
35:## Recommended next steps (channel's recommendation; master decides under D1, changeable by Amear)
44:## Appendix A: Kimi Deep Research output, unedited (as Amear supplied it)
  filtered structure lines: 1
pre consecutive-blank-line pairs (line no. of second blank):
  pre 7
post consecutive-blank-line pairs:
  post 7
  post 42
--- (b) post grep -n -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
--- (b) post grep -n -x -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
=== diff /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-session-close.md docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md
55d54
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff rc=1
line counts pre/post: 55 / 54
pre tail -c 4:
0000000    e   d   .  \n                                                
post tail -c 4:
0000000    e   .  \n  \n                                                
pre structure (headings, fences, block quotes; lines with the word v-e-r-d-i-c-t filtered, count follows):
1:# Return handoff: Claude.ai Praxis channel to praxis-master, 2026-11-13 session close: research outcome, cor
7:## 1. Amear's instruction (REPORTED BY the channel, chat 2026-11-13 14:35 ET)
16:## 2. CORRECTION to files 1 and 2 (governs)
24:## 3. Research outcome, 2026-11-13 (for the record, so it is not repeated)
46:## 4. Today's other updates (REPORTED BY the channel)
  filtered structure lines: 0
pre consecutive-blank-line pairs (line no. of second blank):
post consecutive-blank-line pairs:
--- (b) post grep -n -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
--- (b) post grep -n -x -F
5:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
=== diff /tmp/rf-pre/2026-11-13-return-handoff-claude-ai-vm-queue-results.md docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md
45d44
< Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
diff rc=1
line counts pre/post: 45 / 44
pre tail -c 4:
0000000    e   d   .  \n                                                
post tail -c 4:
0000000    M   .  \n  \n                                                
pre structure (headings, fences, block quotes; lines with the word v-e-r-d-i-c-t filtered, count follows):
1:# Follow-up to the 2026-11-13 session-close handoff: VM bridge queue results (T1-T3)
9:## 1. Results (as reported by the VM agent)
25:## 2. What went differently from the plan (REPORTED BY the VM agent)
33:## 3. What this means (the channel's reading, INFERRED, not a ruling)
38:## 4. What's left (from the VM agent, with channel notes)
  filtered structure lines: 0
pre consecutive-blank-line pairs (line no. of second blank):
post consecutive-blank-line pairs:
--- (b) post grep -n -F
7:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
--- (b) post grep -n -x -F
7:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
=== Kimi brief (strategy-research received :34-:94, fenced) asks for the S13 wording?
rc=1
=== S13 wording inside Gemini appendix (received :96-:108), relative line numbers
13:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
rc=0
=== S13 wording inside Kimi appendix (received :44-:330), relative line numbers
287:Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
rc=0
=== Gemini brief present anywhere under docs/briefs or specs?
rc=1
=== context, strategy-research received :105-:108 (first 70 chars)
The 11:00 AM ET window directly aligns with the 16:00 GMT London marke$
The predictable nature of intraday reversals surrounding major benchma$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
=== context, kimi received :5-:9, :38-:46, :326-:330 (first 70 chars)
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
$
$
Original, filed unedited: `claude/PRAXIS_Kimi_DeepResearch_Strategy_Ve$
Auditor: Claude.ai channel, 2026-11-13. VERIFIED = checked against a s$
2. If it is net positive, run the bootstrap survival check against eac$
3. Only then code a contrasting strategy (gap fade or VWAP) and test t$
4. Verify MFFU's drawdown table from its own help pages before any pur$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
$
## Appendix A: Kimi Deep Research output, unedited (as Amear supplied $
$
Verified and Candidate Strategies for Intraday NQ Futures$
Drawdown measurement: We must compute the continuous equity high-water$
MFFU rules: We assume no changes beyond those cited. If MFFU updates r$
Sources: We cited only peer-reviewed or institutional sources above: F$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
=== context, session-close received :52-:55 and vm-queue received :42-:45 (first 70 chars)
- **Still waiting on Amear (unchanged):** a ruling on parked `ckh` (th$
- **Amear asked when PRAXIS can go live.** The channel's answer (an es$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
3. **Later, not today:** Analyzer tabs for `PraxisNoiseAreaBreakout_Fl$
4. **Open:** what restarted NT8 at 12:32 PM.$
$
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/si$
```

### E2. Check (c): PII pattern scan of the four filed files

Script `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/pii.sh`:

```
#!/bin/bash
# PII scan over the four filed files. Usage: bash pii.sh <dir>
cd "$1" || exit 2
F="2026-11-13-return-handoff-claude-ai-strategy-research.md 2026-11-13-return-handoff-claude-ai-kimi-research.md 2026-11-13-return-handoff-claude-ai-session-close.md 2026-11-13-return-handoff-claude-ai-vm-queue-results.md"
run() { echo "## $1"; shift; /usr/bin/grep "$@" $F; echo "(rc=$?)"; }
run email -n -o -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
run at-handles -n -o -E '(^|[^A-Za-z0-9])@[A-Za-z0-9_]+'
run ipv4 -n -o -E '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'
run ipv6 -n -o -i -E '\b([0-9a-f]{1,4}:){3,7}[0-9a-f]{0,4}\b|::[0-9a-f]{1,4}\b'
run mac -n -o -i -E '\b([0-9a-f]{2}[:-]){5}[0-9a-f]{2}\b'
run hostnames -n -o -i -E '[A-Za-z0-9-]+\.(local|lan|internal|home|corp)\b|[A-Za-z0-9]+-PC\b|DESKTOP-[A-Za-z0-9]+|WIN-[A-Za-z0-9]+|LAPTOP-[A-Za-z0-9]+|MacBook[A-Za-z0-9-]*|hostname|tailscale|\.ts\.net'
run user-paths -n -o -i -E 'C:\\Users\\[^ `]*|/Users/[^ `]*|/home/[^ `]*|C:\\[^ `]*'
run ssh-keys -n -o -i -E 'id_rsa|id_ed25519|id_ecdsa|\.pem\b|\.ppk\b|\.ssh\b|ssh-(rsa|ed25519)|authorized_keys|known_hosts'
run placeholders -n -o -E '\[(rep|user|ip|key|name|host)\]'
run people-words -n -o -i -E '.{0,40}\b(rep|support|named|Hi |Thanks|user name|username|Dear|regards|wrote:)\b.{0,40}'
```

Command and full output:

```
$ bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/pii.sh /Volumes/Sensidine/Praxis.build/docs/reports
## email
(rc=1)
## at-handles
2026-11-13-return-handoff-claude-ai-kimi-research.md:217: @15
2026-11-13-return-handoff-claude-ai-kimi-research.md:230: @25k
(rc=0)
## ipv4
(rc=1)
## ipv6
(rc=1)
## mac
(rc=1)
## hostnames
2026-11-13-return-handoff-claude-ai-strategy-research.md:106:win-rate
2026-11-13-return-handoff-claude-ai-kimi-research.md:106:win-rate
2026-11-13-return-handoff-claude-ai-kimi-research.md:314:win-rate
2026-11-13-return-handoff-claude-ai-session-close.md:26:win-rate
(rc=0)
## user-paths
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
(rc=0)
## ssh-keys
(rc=1)
## placeholders
(rc=1)
## people-words
2026-11-13-return-handoff-claude-ai-kimi-research.md:85:e extreme tuning). No strong literature support. Mechanism (mean reversion to VWAP) may
2026-11-13-return-handoff-claude-ai-kimi-research.md:197:as marginal. There is no known academic support for a continuation.
2026-11-13-return-handoff-claude-ai-kimi-research.md:307:C6 large open continuation (lack of support).
2026-11-13-return-handoff-claude-ai-kimi-research.md:314:ltussen et al.). This has the strongest support: multi-year evidence on futures, trades
2026-11-13-return-handoff-claude-ai-session-close.md:48:purchase thread, addressed to the human rep who answered on 11-12. It asks for (1) 
(rc=0)
```

Same scan over the received copies (no hit was present before and removed; the at-sign hits sit one line later because the :42 deletion had not happened yet):

```
$ bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/pii.sh /tmp/rf-pre | /usr/bin/grep -E '^##|rc=|@|C:'
## email
(rc=1)
## at-handles
2026-11-13-return-handoff-claude-ai-kimi-research.md:218: @15
2026-11-13-return-handoff-claude-ai-kimi-research.md:231: @25k
(rc=0)
## ipv4
(rc=1)
## ipv6
(rc=1)
## mac
(rc=1)
## hostnames
(rc=0)
## user-paths
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:5:C:\praxis\vm-bridge
(rc=0)
## ssh-keys
(rc=1)
## placeholders
(rc=1)
## people-words
(rc=0)
```

### E3. Checks (c) and (d): content claims, format, ambiguous-citation counts

Script `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/claims.sh`:

```
#!/bin/bash
# Check (d) content claims, plus the ambiguous-citation counts for (c). Run: bash claims.sh
cd /Volumes/Sensidine/Praxis.build/docs/reports || exit 2
A=2026-11-13-return-handoff-claude-ai-strategy-research.md
B=2026-11-13-return-handoff-claude-ai-kimi-research.md
C=2026-11-13-return-handoff-claude-ai-session-close.md
D=2026-11-13-return-handoff-claude-ai-vm-queue-results.md
echo "## strategy: cross-check, sections, fence"; /usr/bin/grep -n -E '^Repo cross-check|^## 3\.|^## Appendix|^```' $A | cut -c1-60
echo "## kimi: audit sections, appendix"; /usr/bin/grep -n -E '^## (What holds|Defects|Recommended|Appendix)|^Auditor:|^Original, filed' $B | cut -c1-60
echo "## session-close: sections, table, withdrawal"; /usr/bin/grep -n -E '^## |^\| Candidate|Withdrawn|D-2026-11-02-A' $C | cut -c1-60
echo "## vm-queue: replaces bullet, pasted by Amear, table, sections"; /usr/bin/grep -n -E 'replaces its|pasted to this channel by Amear|^\| Run|^\| T[123]|^## ' $D | cut -c1-60
echo "## manager report headings"; wc -l < 2026-11-13-research-filing-manager.md; /usr/bin/grep -n -E '^## ' 2026-11-13-research-filing-manager.md
echo "## lines starting with > in the four files"; /usr/bin/grep -c -E '^>' $A $B $C $D
echo "## earlier return-handoff MANIFEST rows (cols 1-4)"; /usr/bin/grep -n 'return-handoff-claude-ai' ../../MANIFEST.md | awk -F' \\| ' '{print $1, "|", $2, "|", $3, "|", $4}'
echo "## ambiguous citation counts"
/usr/bin/grep -c 'Dean & Francis' $A $B $C $D
/usr/bin/grep -n 'Bradshaw' $B | cut -d: -f1 | tr '\n' ' '; echo
```

Command and full output:

```
$ bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/claims.sh
## strategy: cross-check, sections, fence
26:Repo cross-check (OBSERVED by the channel, read-only, 202
28:## 3. Channel recommendation (the channel's, not an Amear
32:## Appendix B: Kimi Deep Research follow-up brief (as giv
34:```
94:```
96:## Appendix A: Gemini Deep Research output, unedited (as 
## kimi: audit sections, appendix
8:Original, filed unedited: `claude/PRAXIS_Kimi_DeepResearch
9:Auditor: Claude.ai channel, 2026-11-13. VERIFIED = checked
15:## What holds
24:## Defects
35:## Recommended next steps (channel's recommendation; mast
43:## Appendix A: Kimi Deep Research output, unedited (as Am
## session-close: sections, table, withdrawal
7:## 1. Amear's instruction (REPORTED BY the channel, chat 2
16:## 2. CORRECTION to files 1 and 2 (governs)
18:Files 1 and 2 recommend backtesting `PraxisLastHalfHourMo
20:- Retired by Amear's ruling R-VN3-1, filed as D-2026-11-0
24:## 3. Research outcome, 2026-11-13 (for the record, so it
28:| Candidate | Status | Why |
30:| Last-half-hour momentum (Baltussen, Da, Lammers & Marte
46:## 4. Today's other updates (REPORTED BY the channel)
## vm-queue: replaces bullet, pasted by Amear, table, sections
3:Written by the Claude.ai Praxis channel, 2026-11-13 about 
5:Source: the VM Claude Code session's own report, pasted to
9:## 1. Results (as reported by the VM agent)
13:| Run | ExitMode | Trades | Net | Profit factor | Max dra
15:| T1 | BandOrVWAP | 1,173 | $176,392.92 | 1.2615 | -$38,9
16:| T2 | OppBand | 1,112 | $188,618.48 | 1.2861 | -$37,906.
17:| T3 | BandOrVWAP | 1,173 | $176,392.92 | 1.26 | -$38,905
25:## 2. What went differently from the plan (REPORTED BY th
33:## 3. What this means (the channel's reading, INFERRED, n
38:## 4. What's left (from the VM agent, with channel notes)
## manager report headings
      29
3:## Task
6:## Rubric criteria addressed
9:## Workers dispatched
12:## Process log
15:## Verification evidence (command output)
18:## Adversarial findings
21:## S6 cross-block check
24:## Files staged
## lines starting with > in the four files
2026-11-13-return-handoff-claude-ai-strategy-research.md:0
2026-11-13-return-handoff-claude-ai-kimi-research.md:0
2026-11-13-return-handoff-claude-ai-session-close.md:0
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:0
## earlier return-handoff MANIFEST rows (cols 1-4)
216:| /docs/reports/2026-11-04-return-handoff-claude-ai.md | Report | 2 | 2026-11-04
236:| /docs/reports/2026-11-06-return-handoff-claude-ai.md | Report | 2 | 2026-11-06
257:| /docs/reports/2026-11-07-return-handoff-claude-ai.md | Report | 2 | 2026-11-07
288:| /docs/reports/2026-11-07-return-handoff-claude-ai-2.md | Report | 2 | 2026-11-07
389:| /docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md | Report | 3 | 2026-11-11
427:| /docs/reports/2026-11-11-return-handoff-claude-ai-mffu-prepurchase.md | Report | 3 | 2026-11-12
477:| /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md | Report | 3 | 2026-11-13
478:| /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | Report | 3 | 2026-11-13
479:| /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | Report | 3 | 2026-11-13
480:| /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | Report | 3 | 2026-11-13
## ambiguous citation counts
2026-11-13-return-handoff-claude-ai-strategy-research.md:3
2026-11-13-return-handoff-claude-ai-kimi-research.md:2
2026-11-13-return-handoff-claude-ai-session-close.md:1
2026-11-13-return-handoff-claude-ai-vm-queue-results.md:0
29 92 96 102 
```

Last five MANIFEST rows (full text):

```
$ tail -n 5 /Volumes/Sensidine/Praxis.build/MANIFEST.md
| /docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md | Report | 3 | 2026-11-13 | Return handoff written by the Claude.ai Praxis channel: the Gemini Deep Research output as received (Appendix A) and the channel's audit of it, a read-only repo cross-check, the channel's backtest-order recommendation, and the Kimi follow-up brief (Appendix B, in a code block); duplicate S13 line at received :108 deleted (S13 sentence kept once, at :5); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md | Report | 3 | 2026-11-13 | Return handoff written by the Claude.ai Praxis channel: the channel's audit of a Kimi Deep Research run (what holds, defects, recommended next steps) and the Kimi output as received (Appendix A); duplicate S13 lines at received :42 and :330 deleted (S13 sentence kept once, at :5; the :42 deletion leaves two adjacent blank lines at :41-:42, left as is); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-session-close.md | Report | 3 | 2026-11-13 | Session-close return handoff written by the Claude.ai Praxis channel: Amear's instruction as reported by the channel, the channel's correction withdrawing its recommendation to backtest PraxisLastHalfHourMomentum (citing D-2026-11-02-A), a status table of the candidates from the Gemini and Kimi runs, and the channel's list of the day's other updates; duplicate S13 line at received :55 deleted (S13 sentence kept once, at :5); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-return-handoff-claude-ai-vm-queue-results.md | Report | 3 | 2026-11-13 | Follow-up return handoff written by the Claude.ai Praxis channel, replacing the session-close handoff's VM bridge queue bullet: VM bridge queue runs T1-T3 as reported by the VM Claude Code session and pasted to the channel by Amear (trades, net, profit factor, max drawdown per run), deviations from the plan, the channel's INFERRED reading, and items left; duplicate S13 line at received :45 deleted (S13 sentence kept once, at :7); no other line changed; filed by unit 2026-11-13-research-filing, DECISION_LOG 2026-11-13T19:40:54Z; ungraded at time of row |
| /docs/reports/2026-11-13-research-filing-manager.md | Report | 3 | 2026-11-13 | Manager report written by praxis-manager for unit 2026-11-13-research-filing (DECISION_LOG 2026-11-13T19:40:54Z): the unit's process log, verification evidence and adversarial findings for the filing of the four 2026-11-13 return-handoff files and their MANIFEST rows; ungraded at time of row |
```

### E4. Checks (d) and (e): level words, column shape, blob and diff checks

Script `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/blob.sh`:

```
#!/bin/bash
# Checks (d) and (e). Run: bash blob.sh
cd /Volumes/Sensidine/Praxis.build || exit 2
SP=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad
N=$(git show HEAD:MANIFEST.md | wc -l | tr -d ' '); echo "N=$N"
echo "blob lines: $(wc -l < /tmp/rf-manifest-blob.md | tr -d ' ') (expect $((N+5)))"
echo "working-tree MANIFEST.md lines: $(wc -l < MANIFEST.md | tr -d ' ')"
git show HEAD:MANIFEST.md > $SP/head-manifest.md
head -n $N /tmp/rf-manifest-blob.md | cmp - $SP/head-manifest.md && echo "cmp: head -n $N of blob == HEAD:MANIFEST.md"
tail -n 5 /tmp/rf-manifest-blob.md | cmp - <(tail -n 5 MANIFEST.md) && echo "cmp: blob last 5 == working-tree last 5"
echo "blob tail -c 3:"; tail -c 3 /tmp/rf-manifest-blob.md | od -c | head -n 1
echo "git diff MANIFEST.md added rows: $(git diff MANIFEST.md | grep -c '^+[^+]')"
echo "git diff MANIFEST.md removed rows: $(git diff MANIFEST.md | grep -c '^-[^-]')"
echo "hunk headers:"; git diff MANIFEST.md | grep '^@@'
git diff MANIFEST.md | grep '^+[^+]' | sed 's/^+//' > $SP/added.txt
echo "added rows minus the last 5 (path column only):"
head -n $(( $(wc -l < $SP/added.txt) - 5 )) $SP/added.txt | awk -F'|' '{print "  " $2}'
echo "count: $(head -n $(( $(wc -l < $SP/added.txt) - 5 )) $SP/added.txt | wc -l | tr -d ' ')"
echo "any of those 23 rows mention this unit or the four filed files?"
head -n 23 $SP/added.txt | grep -c -E 'research-filing|2026-11-13-return-handoff'
tail -n 5 $SP/added.txt | cmp - <(tail -n 5 /tmp/rf-manifest-blob.md) && echo "cmp: last 5 added rows of git diff == blob last 5"
echo "snapshot before unit, MANIFEST line:"; grep 'MANIFEST' /tmp/rf-diffstat-before.txt
echo "--- (d) level words in last 5 rows:"
tail -n 5 MANIFEST.md | grep -n -i -w -E 'built|tested|verified|working|viable|retired|decided'; echo "rc=$?"
echo "--- (d) column shape of last 8 rows: field count and cols 3-5"
tail -n 8 MANIFEST.md | awk -F' \\| ' '{print NF, "|", $2, "|", $3, "|", $4}'
echo "--- (d) per-row claims: received line numbers and kept-line numbers"
tail -n 5 MANIFEST.md | grep -o -E 'received :[0-9]+( and :[0-9]+)?|kept once, at :[0-9]+|blank lines at :[0-9]+-:[0-9]+'
```

Command and full output:

```
$ bash /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/dcac04b1-7eb1-4373-8ace-68706ad67635/scratchpad/blob.sh
N=453
blob lines: 458 (expect 458)
working-tree MANIFEST.md lines: 481
cmp: head -n 453 of blob == HEAD:MANIFEST.md
cmp: blob last 5 == working-tree last 5
blob tail -c 3:
0000000        |  \n                                                    
git diff MANIFEST.md added rows: 28
git diff MANIFEST.md removed rows: 0
hunk headers:
@@ -304,6 +304,14 @@
@@ -429,6 +437,12 @@
@@ -443,11 +457,25 @@
added rows minus the last 5 (path column only):
   /docs/specs/2026-11-06-walk-forward-values.md 
   /docs/specs/2026-11-05-walk-forward-spec.md 
   /docs/reports/2026-11-08-wf-spec-amendment-manager.md 
   /docs/reports/2026-11-08-wf-spec-amendment-correction-1-manager.md 
   /docs/reports/2026-11-08-wf-spec-amendment-correction-2-manager.md 
   /docs/reports/2026-11-08-wf-spec-amendment-correction-3-manager.md 
   /docs/reports/2026-11-09-wf-spec-amendment-resume-manager.md 
   /docs/reports/evidence/2026-11-09-u7-diff-of-record.patch 
   /docs/reports/2026-11-12-r6-engine-entry-manager.md 
   /docs/reports/2026-11-12-r6-engine-entry-worker1.md 
   /docs/reports/2026-11-12-r6-engine-entry-worker2.md 
   /DECISIONS.md 
   /docs/reports/2026-11-12-r6-engine-entry-correction-1-manager.md 
   /docs/reports/2026-11-12-r6-engine-entry-correction-1-worker1.md 
   /docs/reports/2026-11-12-o3-block1-scope-manager.md 
   /docs/reports/2026-11-12-o3-block1-scope-worker1.md 
   /docs/reports/2026-11-12-o3-block1-scope-correction-1-manager.md 
   /docs/reports/2026-11-12-o3-block1-scope-correction-1-worker1.md 
   /docs/reports/2026-11-12-o3-block1-scope-correction-2-manager.md 
   /docs/reports/2026-11-12-o3-block1-scope-correction-2-worker2.md 
   /docs/reports/2026-11-13-o4-parity-manager.md 
   /docs/reports/2026-11-13-open-a1-manager.md 
   /docs/reports/2026-11-13-open-a1-worker1.md 
count: 23
any of those 23 rows mention this unit or the four filed files?
0
cmp: last 5 added rows of git diff == blob last 5
snapshot before unit, MANIFEST line:
 MANIFEST.md                                        |  23 +++++
--- (d) level words in last 5 rows:
rc=1
--- (d) column shape of last 8 rows: field count and cols 3-5
5 | Report | 3 | 2026-11-13
5 | Log | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
5 | Report | 3 | 2026-11-13
--- (d) per-row claims: received line numbers and kept-line numbers
received :108
kept once, at :5
received :42 and :330
kept once, at :5
blank lines at :41-:42
received :55
kept once, at :5
received :45
kept once, at :7
```

### E5. Check (f): diff-stat comparison, new DISPATCH_LOG rows, mtimes

```
$ cd /Volumes/Sensidine/Praxis.build && git diff --stat > /tmp/rf-diffstat-adv.txt; diff /tmp/rf-diffstat-before.txt /tmp/rf-diffstat-adv.txt; echo "diff rc=$?"
5c5
<  DISPATCH_LOG.md                                    |  23 +++++
---
>  DISPATCH_LOG.md                                    |  28 ++++++
8c8
<  MANIFEST.md                                        |  23 +++++
---
>  MANIFEST.md                                        |  28 ++++++
15c15
<  14 files changed, 523 insertions(+), 32 deletions(-)
---
>  14 files changed, 533 insertions(+), 32 deletions(-)
diff rc=1
$ cd /Volumes/Sensidine/Praxis.build && git diff DISPATCH_LOG.md | /usr/bin/grep -E '^\+- \[2026-11-13T19:(4[2-9]|5[0-9])' | cut -c1-150
+- [2026-11-13T19:42:27Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=ad36d6148e73
+- [2026-11-13T19:42:30Z] WHO: praxis-manager | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=a36ab2e34b73584f4, ma
+- [2026-11-13T19:45:54Z] WHO: praxis-worker | WHAT: subagent closed | WHY: hook-recorded at SubagentStop, keyed close for corr=ad36d6148e73b03c9, mat
+- [2026-11-13T19:45:54Z] WHO: praxis-manager | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=a36ab2e34b7
+- [2026-11-13T19:47:00Z] WHO: praxis-worker | WHAT: subagent spawned | WHY: hook-recorded at SubagentStart | WHERE: session 661e073 corr=abb2520a9011
$ cd /Volumes/Sensidine/Praxis.build && TZ=UTC stat -f '%Sm %N' -t '%Y-%m-%dT%H:%M:%SZ' .claude/settings.json AUDIT_LOG.md DECISIONS.md DECISION_LOG.md DISPATCH_LOG.md HANDOFF.md ISSUE_REGISTER.md MANIFEST.md STATUS.md docs/reports/2026-10-28-f4-[rep]-reply-filing.md docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md docs/specs/2026-11-05-walk-forward-spec.md docs/specs/2026-11-06-walk-forward-values.md scripts/dispatch-log-writeahead.sh /tmp/rf-diffstat-before.txt; date -u +%Y-%m-%dT%H:%M:%SZ
2026-11-13T17:37:18Z .claude/settings.json
2026-11-13T17:37:18Z AUDIT_LOG.md
2026-11-13T17:37:18Z DECISIONS.md
2026-11-13T19:41:05Z DECISION_LOG.md
2026-11-13T19:47:00Z DISPATCH_LOG.md
2026-11-13T17:41:03Z HANDOFF.md
2026-11-13T17:37:18Z ISSUE_REGISTER.md
2026-11-13T19:44:22Z MANIFEST.md
2026-11-13T17:41:04Z STATUS.md
2026-11-13T17:37:18Z docs/reports/2026-10-28-f4-[rep]-reply-filing.md
2026-11-13T17:37:18Z docs/reports/2026-10-28-nightly-checks-plan-review-rebuild.md
2026-11-13T17:37:18Z docs/specs/2026-11-05-walk-forward-spec.md
2026-11-13T17:37:18Z docs/specs/2026-11-06-walk-forward-values.md
2026-11-13T17:37:18Z scripts/dispatch-log-writeahead.sh
2026-11-13T19:41:56Z /tmp/rf-diffstat-before.txt
2026-11-13T19:53:06Z
```

## Files staged

None. This report is the only file written, and it is left unstaged.

## Result

No defect found in checks (a) to (f); see the four observations under Defects.

Result: PASS

Filer's note (unit 2026-11-13-research-filing-cure, DECISION_LOG 2026-11-13T20:25:43Z): a private person's name in a file name inside pasted command output at :584 and :594 was replaced by [rep] after the output was captured; no other byte of the output changed.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
