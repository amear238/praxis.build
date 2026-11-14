Filed by praxis-manager (unit 2026-11-14-pivot-rulings-filing): worker 1's own Write of this file was refused by a hook, so the manager wrote the body below exactly as worker 1 returned it, with the return channel's HTML escapes (`&lt;` `&gt;` `&amp;`) put back as the literal characters.

# Unit 2026-11-14-pivot-rulings-filing: worker 1 report

**Task:** draft DECISIONS.md D-2026-11-14-B (Amear's R1-R9, voice session 2026-11-14), add S13 lines to two voice files, write 6 MANIFEST rows, and stage it all in temp index /tmp/praxis-pv/idx built from HEAD 244cfc3.
**Mode:** BUILD. **Criteria:** S1, S2, S4, S5, S6, S8, S13.

## Process log
- The entry was built by `/tmp/praxis-pv/build-entry.sh` from `/tmp/praxis-pv/entry.tpl.txt`. Block quotes were filled in by `sed -n` on the notes and brief, and inline quotes by `grep -o` on DECISION_LOG :971 and HEAD DECISIONS :2482. Output: `/tmp/praxis-pv/entry.txt` (88 lines).
- The DECISIONS blob is HEAD's blob + one blank line + the entry. The MANIFEST blob is HEAD's MANIFEST + `/tmp/praxis-pv/rows.txt`. Both were written with `hash-object -w` and staged with `update-index --cacheinfo`. The three voice files were staged from the working tree the same way. The working-tree DECISIONS.md and MANIFEST.md got the same appends. The originals of the voice files were saved to /tmp/praxis-pv/orig/ before the appends.
- No commit was made. The real index was not touched. This worker did not write the three unit reports. This report was not written to disk either: subagent .md report writes are refused, so the manager files this text.

## Evidence (pasted)
```
fence  1  N sed -n 10,11p         lines=2 cmp rc=0
fence  2  N sed -n 15p            lines=1 cmp rc=0
fence  3  N sed -n 19,21p;23p     lines=4 cmp rc=0
fence  4  N sed -n 27p;29p        lines=2 cmp rc=0
fence  5  N sed -n 33p            lines=1 cmp rc=0
fence  6  B sed -n 34,35p         lines=2 cmp rc=0
fence  7  N sed -n 37,39p         lines=3 cmp rc=0
fence  8  N sed -n 43p            lines=1 cmp rc=0
fence  9  N sed -n 47,48p         lines=2 cmp rc=0
fence 10  N sed -n 64,69p         lines=6 cmp rc=0
negative control (fence 1 vs notes 10p only):
cmp: EOF on stdin
rc=1
```
(The fences were extracted from the staged blob, lines 2527-2614. N = staged notes and B = staged pivot brief, taken from `git show :path`.) Inline quotes, `grep -cF` in their source:
```
pause the noon search loop until I decide in DECISION_LOG:971 1
It passes the drawdown gate at 1 MNQ for at least one MFFU account size. in HEAD DECISIONS:2482 1
stopped the loop already in notes:11          1
for now in notes:15                           1
Meaning as confirmed back to him in notes:22  1
Consequence (voice agent, INFERRED) in notes:24 1
until steps 2 to 4 are done in notes:60       1
Written confirmation from MFFU that this specific automation pattern is permitted on a funded account in rubric:34-35 joined 1
Revisit if a personal account is used. in HEAD WF spec:31 1
KEEP: #1 daily loss limit in HEAD DECISIONS:1587 1
stop-loss + take-profit in HEAD phase3:54     1
```
Blob and working-tree checks:
```
staged DECISIONS lines:     2614
ckh-line check: wt lines=    2706 HEAD=2525
first 2525 vs HEAD cmp rc=0
D-2026-11-12-B count: blob=2 HEAD=2
blob 2527-2614 vs entry cmp rc=0
wt tail 249 (HEAD tail 160 + blank + entry 88) vs blob tail cmp rc=0
MANIFEST prefix vs HEAD cmp rc=0
MANIFEST blob tail6 vs rows cmp rc=0
wt MANIFEST tail9 vs blob tail9 cmp rc=0
entry wc -l:       88
S13 sentence in entry: 1; last line: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
```
S13 appends (working-tree DECISIONS.md before append had 2617 lines, so 2706 is 2617 + 89):
```
2026-11-14-voice-brief-overnight.md prefix cmp rc=0 orig_lines=      34 new_lines=      36
2026-11-14-voice-notes-pivot.md prefix cmp rc=0 orig_lines=      71 new_lines=      73
pivot brief unchanged rc=0
2026-11-14-voice-brief-overnight.md grep -cx = 1
2026-11-14-voice-brief-pivot.md grep -cx = 1
2026-11-14-voice-notes-pivot.md grep -cx = 1
```
Digit audit of the entry: `awk` printed every digit-bearing token outside the fences, 212 lines, to `/tmp/praxis-pv/digit-audit.txt` (sha256 46e36e12...fa5). The tokens are line cites (:N), dates, stamps, ids (R1-R9, Q1-Q6, D-..., F3/F4, A4, `73d67fad7ec9`, `afa53c6`, `244cfc3`), item, ruling and Block numbers, breaker #1/#2, "Phase 3" (a spec name), inline quotes, and the S13 sentence. One count is not a cite: "the 949 lines of DECISION_LOG.md", which the brief allowed (HEAD `git show 244cfc3:DECISION_LOG.md | wc -l` = 949). The entry has no dollar amount and no percentage.
Name and email sweep (counts only):
```
:DECISIONS.md                                        email=0 tok=0
:MANIFEST.md                                         email=0 tok=2
:docs/reports/2026-11-14-voice-brief-overnight.md    email=0 tok=0
:docs/reports/2026-11-14-voice-brief-pivot.md        email=0 tok=0
:docs/reports/2026-11-14-voice-notes-pivot.md        email=0 tok=0
/tmp/praxis-pv/entry.txt                             email=0 tok=0
/tmp/praxis-pv/rows.txt                              email=0 tok=0
HEAD DECISIONS tok count (baseline): 0  HEAD MANIFEST: 2
```
The 2 token hits in MANIFEST are already in HEAD's rows. The new rows add 0.
Staging (from `/tmp/praxis-pv/evidence-worker1.txt`, sha256 82ce9544...16d42):
```
$ git diff --cached 244cfc3 --name-status
M	DECISIONS.md
M	MANIFEST.md
A	docs/reports/2026-11-14-voice-brief-overnight.md
A	docs/reports/2026-11-14-voice-brief-pivot.md
A	docs/reports/2026-11-14-voice-notes-pivot.md
$ git diff --cached 244cfc3 --numstat
89	0	DECISIONS.md
6	0	MANIFEST.md
36	0	docs/reports/2026-11-14-voice-brief-overnight.md
49	0	docs/reports/2026-11-14-voice-brief-pivot.md
73	0	docs/reports/2026-11-14-voice-notes-pivot.md
$ git diff --cached 244cfc3 | shasum -a 256
f2a896a79b794d435bc9c49a0ca0e7aa2c7b1fccb56ff823016170381f67d904  -
$ git diff --cached --name-status   (real index; evidence filename token redacted)
A	docs/reports/evidence/2026-10-28-mffu-<tok>-reply.png
```

## S6 grep output (TRIMMED to the lines the entry cites; full 36 lines in `/tmp/praxis-pv/s6-grep.txt`, sha256 045ac87e...eef)
```
244cfc3:docs/specs/2026-11-05-phase3-build-specification.md:97:1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
244cfc3:docs/specs/2026-11-05-phase3-build-specification.md:98:2. Max trades per day — trade count hits daily max → disable order submission
244cfc3:docs/specs/2026-11-10-live-signal-topology.md:58:| 1 | Daily loss limit | n8n gate node, before Write Signal File: Redis flag `gate:daily_loss` (closed when realised + unrealised P&L ≤ −thresh
244cfc3:docs/specs/2026-11-10-live-signal-topology.md:59:| 2 | Max trades per day | n8n gate node, before Write Signal File: Redis counter of entries this session; gate closes when count = max. | Same
--- HEAD DECISIONS.md
1587:    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
```
D-2026-11-08-A R8 at HEAD :1583-:1584: "Breaker values set for manual trading are redone / for the automated book: #2 max ... trades/day" (the trade count is left out here, see the open item). The Phase 3 spec :140 sits under "### Block 5: Graduated Live Deployment" (awk heading lookup). The walk-forward spec and values are read at HEAD: spec :31 and :67, values :51 and :73.

## Files staged (temp index /tmp/praxis-pv/idx only)
DECISIONS.md (blob 0c13dca, entry at lines 2527-2614), MANIFEST.md (3cabfc0), and the three voice files. The three unit reports are NOT staged.

## Open items
- R7 against D-2026-11-08-A R8 (breaker #2's value): a named tension, not resolved. It is Amear's.
- Whether Block 5's per-trade sizing percentage (Phase 3 :140) is R3's percentage: Amear's.
- This worker did not re-observe the search loop's paused state. The last readback is the master's row 14:50:10Z.
- The manager must write this report to `docs/reports/2026-11-14-pivot-rulings-filing-worker1.md`. The MANIFEST row for it is already staged.

**Result: PASS**

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
