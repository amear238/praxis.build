# Adversarial review — F4 report addendum "MFFU 'Davi' reply (screenshot)"

## Task
Try to break the addendum appended at line 541 onward of
`docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`, checked against F4, S1, S2 and S8
and against the required and forbidden content lists in the brief.

## Mode
ADVERSARIAL. Read-only on the repo apart from this report. The artifact was not edited. Nothing was staged or committed.

## Criterion
- F4: "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account."
- S1: pasted output, not described output. S2: no claim above evidence. S8: no Amear question answered on his behalf.

## Process log
1. Read the addendum (lines 541–759), the transcript, and the image (2866x930, read visually).
2. Byte-compared every `> ` quote line against the transcript fence (`/usr/bin/grep -Fxc`). Lines that failed the exact-line match were then checked as substrings. Every inline `"..."` quote in §C–F was also checked as a substring.
3. Re-ran the provenance block and the `w3search.sh` block, then diffed my output against the pasted output.
4. Proved append-only against the staged blob.
5. Located the DECISION_LOG row. Checked that SPEC_RUBRIC.md was not touched (mtime and diff).
6. Scanned the addendum for forbidden or over-claiming wording. Judged each verdict.

## Verification evidence

### V1. Quote byte-compare (exact line vs fence, 25 fence lines)
```
add-line 58 (file 598): exact-line-count=1
add-line 59 (file 599): exact-line-count=1
add-line 60 (file 600): exact-line-count=1
add-line 61 (file 601): exact-line-count=1
add-line 62 (file 602): exact-line-count=1
add-line 64 (file 604): exact-line-count=1
add-line 92 (file 632): exact-line-count=1
add-line 161 (file 701): exact-line-count=1
add-line 162 (file 702): exact-line-count=1
add-line 164 (file 704): exact-line-count=0
add-line 180 (file 720): exact-line-count=1
add-line 183 (file 723): exact-line-count=1
add-line 185 (file 725): exact-line-count=1
add-line 187 (file 727): exact-line-count=1
add-line 189 (file 729): exact-line-count=1
add-line 197 (file 737): exact-line-count=0
```
The two exact-line misses are verbatim whole-sentence substrings of a longer fence line:
```
You are responsible for the performance and reliability of your automated system.	substr-lines=1
Hi Frank — thanks for confirming, that's helpful.	substr-lines=1
```
Inline `"..."` quotes in §C–F, as substring counts against the fence:
```
0	Algo trading is now permitted at MFFU moving forward on all plans ...
1	Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
1	integrate your trading bot or automated strategy via the Tradovate API
1	simulated-funded, and live account stages
1	You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
1	your MyFundedFutures Tradovate evaluation and funded accounts
0	this specific automation pattern      (rubric text, not a fence quote)
0	on this account / on a funded account (report/rubric text, not fence quotes)
```
Visual spot-check against the image: the B quotes, the D quotes and the E quotes ("Hello amear,i", "Hi ! ... Michael", signature "Davi-MyFundedFutures Support", the preview cut at "is f") all match the image.

### V2. Re-run of the provenance block, diffed against the pasted output (lines 568–574)
```
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
00000000: e280 af50 4d2e 706e 67                   ...PM.png
--- diff pasted vs mine:
IDENTICAL
```

### V3. Re-run of `w3search.sh` (verbatim, output to my scratch), diffed against the pasted output (lines 662–688)
```
IDENTICAL
--- word-internal api?
13:API
14:API
14:API
```
I also ran a wider null search on the fence, to cover variants the addendum's patterns could miss:
```
hook	0
rithm	0
ninja	0
trading ?view	0
n8n	0
platform	0
third	0
bridge	0
connect	0
```
(`nt ` returned 1. That pattern was mine and too loose: it matches the end of "account ". It is not a hit for NT8.)

### V4. Append-only
```
$ git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ head -n 537 <file> | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
staged blob lines: 537
git diff --numstat (worktree vs index): 222	0
git diff --cached --numstat:            537	0   (file is newly added; index holds the 537-line original)
removed-line count in git diff: 0
```

### V5. DECISION_LOG row
```
435:- [2026-10-28T20:54:29Z] WHO: amear | WHAT: **F4 evidence: FILE the MFFU "Davi" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.** ... | HOW: AskUserQuestion, option "File it + follow up"; praxis-manager files it, praxis-auditor grades it; Amear sends the follow-up himself | STATE: dispatched — filing
```
(The middle of the row is elided here. The `grep -n` output above was pasted in full when run.) Staging state of that row:
`git diff --cached -- DECISION_LOG.md | grep -c 20:54:29Z` returned `0`, and `git diff -- DECISION_LOG.md | grep -c 20:54:29Z` returned `1`.

### V6. SPEC_RUBRIC untouched
```
2026-07-30T11:50:39 specs/SPEC_RUBRIC.md
git diff -- specs/SPEC_RUBRIC.md, +/- lines matching F4|MFFU|frozen: (none)
```

## Findings

1. **MINOR (S2, false universal).** Line 562 says: "Every quote in this addendum is taken from inside that file's `text` fence." That is false. Line 626 quotes Frank's §1 line, "Algo trading is now permitted at MFFU moving forward on all plans ...", and that line is not in the fence (V1: substring count 0). It comes from §1 line 28 of the same report. The quote itself is accurate. The provenance sentence is the part that over-generalises.

2. **MINOR (S2/S8-adjacent, a reading stated as fact).** The phrase "your MyFundedFutures Tradovate evaluation and funded accounts" can be parsed two ways. "Tradovate" may modify both nouns, or it may modify only "evaluation", with "funded accounts" standing alone. The addendum states the first parse as fact twice: line 625 "The first mention is tied to **Tradovate** accounts" and line 627 "it is conditioned on Tradovate accounts". The image does not settle the parse. Which accounts that sentence reaches bears directly on whether a Rithmic account is covered, and that is Amear's ruling. The narrow reading is the conservative one, so no verdict changes. It should still be labelled a reading.

3. **MINOR (S1/S2, unscoped universal negatives).** Line 577 says "No agent read this message in Gmail. No agent contacted MFFU." Line 753 says "No agent drafted or sent it." The writer can attest only for itself. No evidence covering every agent is pasted. A repo scan found no follow-up draft, which supports the claim but does not prove it: `find -newermt 2026-10-28` plus `grep 'Hi Davi|Dear Davi|Subject:.*(NinjaTrader|Rithmic)'` matched only files that quote the "Hi Frank" preview. The DECISION_LOG row does support "his to send" ("Amear sends the follow-up himself").

4. **MINOR (completeness, anomaly E.2).** Line 726 says "The body opens twice", and only the "Hello" and "Hi !" lines are quoted. The image shows three stacked opening blocks. The omitted middle line, "Thank you for contacting MyFundedFutures Support! I'll be happy to assist you today.", repeats the "Thank you so much for reaching out to MyFundedFutures Support" in the Michael line. That repetition is extra evidence for the boilerplate inference, and it is left out. This does not overclaim.

Observation, not counted (outside F4/S1/S2/S8): the addendum's 222 lines and the authorising DECISION_LOG row are both **unstaged** (V4, V5). If S5 ("authorisation staged") is graded on this landing, it will fail until both are staged.

### Checked and held (no break)
- All 16 blockquote lines and all fence-sourced inline quotes match byte-for-byte (V1). They match the image.
- The provenance and search blocks reproduce exactly (V2, V3). The positive controls fire. The `API` hits are whole-word only.
- Append-only is proven (V4). SPEC_RUBRIC is untouched (V6). The DECISION_LOG row exists with WHO: amear, F4 FROZEN, and the NT8 + Rithmic follow-up (V5).
- Verdicts:
  - F4 specific pattern / §3.5: DOES NOT ADDRESS. Correct, because the reply names only the Tradovate API.
  - "on a funded account": PARTLY ADDRESSES. Defensible, because funded and live stages are named and no account is identified. This is not generous.
  - §3.2 effective date: DOES NOT ADDRESS. Correct, and the absence of "now" is handled without inference.
  - Retroactivity: DOES NOT ADDRESS. A literal and conservative call. Present-tense "all plans" could be read as covering existing accounts, but that reading would be Amear's to make.
- Nothing claims a date, headers or thread order. The forbidden-wording scan found no "satisfies", "closer", "confirms PRAXIS" or similar. §D makes no PRAXIS assessment. The F list covers NOT discharged/satisfied/unfrozen, S8 coverage, and the follow-up row.
- Required content: every item is present.

## Files staged
None. This report is written but not staged.

Result: FAIL

VERDICT: DEFECTS FOUND (0 blocking, 4 minor)
