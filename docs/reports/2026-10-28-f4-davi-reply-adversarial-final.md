# F4 Davi-reply addendum: adversarial pass (final)

**Task.** Find where the F4 "Davi" addendum, its transcript, or its image copy fails S1, S2, S8 or the hard limits.
**Mode.** ADVERSARIAL. Read-only, except for this report.
**Date.** 2026-10-28.
**Criteria.** F4, S1, S2, S8 (`specs/SPEC_RUBRIC.md`), plus the brief's hard limits.
**Artifacts.** (a) `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` lines 541–778. (b) `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md`. (c) `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`.
Scratch directory: `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/adv8/`.

## Process log

1. Checked that the addendum is append-only. I hashed the first 537 lines of both the working-tree copy and the index copy, and ran numstat.
2. Re-ran the addendum's provenance commands (shasum, ls, xxd) and its search script, `w3search.sh`. I diffed the search output against the pasted output.
3. Used a Python script to check every `> ` line and every `"..."` fragment in the addendum against the transcript's `text` fence.
4. Viewed the image at full size and three zoomed crops (sips crops of scratch copies). I compared the image line by line with the fence and checked the glyph and layout notes.
5. Checked cited sources: §1, §1.1, §3.2 and §3.5 of the report, the `DECISION_LOG.md` row `2026-10-28T20:54:29Z`, the F4 text in `specs/SPEC_RUBRIC.md`, and the signal-flow line in `CLAUDE.md`.
6. Scanned the addendum for wording that implies F4 is closer to being met. Reviewed each mapping verdict and checked the statements against each other.

## Verification evidence

### V1. Append-only (hard limit). PASS

```
$ head -n 537 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git show :docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | wc -l
     537
$ git diff --numstat -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
241	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
```

### V2. Re-run of the pasted command blocks. Output identical

Provenance block, re-run:
```
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
00000000: e280 af50 4d2e 706e 67                   ...PM.png
  pixelWidth: 2866
  pixelHeight: 930
```
Search script, re-run verbatim to `rerun.txt` and diffed against the pasted lines 674–700:
```
$ diff pasted.txt rerun.txt && echo SEARCH_DIFF_EMPTY
SEARCH_DIFF_EMPTY
```
(The pasted output looks as if it lacks counts when shown in a terminal, but `cat -vet` shows `NinjaTrader^I0$` and so on. The counts are there, separated by tabs.)

### V3. Quote check against the fence (script `q.py`)

```
== blockquote lines (exact line match vs fence)
605 EXACT  606 EXACT  607 EXACT  608 EXACT  609 EXACT  610 EMPTY >  611 EXACT
644 EXACT  713 EXACT  714 EXACT  716 SUBSTR 732 EXACT  735 EXACT  737 EXACT
740 EXACT  742 EXACT  744 EXACT  756 SUBSTR
== double-quoted fragments NOT_IN_FENCE (all others IN_FENCE)
627 'Algo trading is permitted on all plans ...'        (prefix + ellipsis, OK)
636 'this specific automation pattern'                  (rubric F4, wraps a line there, OK)
637 'on a funded account'                               (rubric F4, OK)
638 'now' / 'Algo trading is now permitted at MFFU moving forward on all plans ...'  (§1 line 28, OK)
639 'on this account' (§3.2) / 'your ... accounts' (elision of the in-fence phrase, OK)
```
No quote attributed to the reply is altered. Comparing the image with the fence (full view plus crops of the preview, header/greetings and signature) found no differences. These match: `Hello amear,i`, `Hi !`, the long dash in `Frank — thanks`, the cut-off at `is f`, the bold `Davi`, the blue underlined URL, the absence of any timestamp, and the absence of wrapped lines.

### V4. Other checked facts (no break)

- `/usr/bin/grep -niow now fence.txt` matches nothing. `/usr/bin/grep -nE '[0-9]{4}|[0-9]+:[0-9]{2}'` matches only line 19, the URL. This confirms "no 'now' and no date".
- The `DECISION_LOG.md` row `2026-10-28T20:54:29Z` (line 435) has `WHO: amear`, "send a follow-up naming NinjaTrader 8 + Rithmic" and "Amear sends the follow-up himself". F's attribution is accurate.
- `specs/SPEC_RUBRIC.md` mtime is `Jul 30 11:50:39 2026`. Its unstaged diff is the R-A/R-B/R-C text from July, not this addendum.
- Scan for wording that implies F4 is met: the only hits for `confirm*`, `meets`, `satisf*`, `covers` and `complies` are inside quotes (`confirming`, `meets you well`) or inside "NOT satisfied" / "Not claimed" lines.

## Findings

### 1. BLOCKING (S8, internal contradiction). "one explicit grant" takes one of the two readings it says belong to Amear

```
625 The reply's one explicit grant names the **Tradovate API**: "custom Tradovate
626 API access with your MyFundedFutures Tradovate evaluation and funded accounts".
627 Its "Algo trading is permitted on all plans ..." bullet is unqualified; whether
628 that bullet sits under the Tradovate sentence or stands as a general permission
629 is not stated in the reply, and how to read it is Amear's ruling (S8).
```
The fence has three permission statements:
```
13:You can use custom Tradovate API access with your MyFundedFutures Tradovate e
14:• Automated trading solutions using an API are supported, allowing you to int
15:• Algo trading is permitted on all plans, including evaluation, simulated-fun
```
Line 15 says "is permitted", so it is a grant on its face. "One explicit grant" is true only if line 15 sits under the Tradovate sentence. Line 628–629 says that reading is undetermined and is Amear's to make. So the addendum states as fact (625) what it then says is his ruling (629). This is the kind of contradiction asked about in brief item 5. Its effect is to frame the general-permission reading as secondary before Amear has ruled. The same sentence pair also calls the bullet "unqualified" (627) and then says it may sit under the Tradovate sentence. "Unqualified" is literally true of the bullet's own words, so on its own that is MINOR.

### 2. MINOR (S2 wording). Section D is titled "New conditions", but the addendum itself says three of the four repeat §1.1

```
709 ### D. New conditions the reply states (for the record only)
718 So the reply states four conditions: ...
724 ... §1.1 of this report recorded three similar
725 restrictions from Frank's relay ...
```
"New" can only mean "newly received". Also, line 718 counts "You are responsible for the performance and reliability ..." as a condition. That is a characterisation, not something the text says.

### 3. MINOR (S2). §1.1's restrictions are attributed to "Frank's relay", but §1.1 does not name Frank

§1.1 (lines 40–46) reads "MFFU's three stated restrictions … Stated plainly, as relayed". `/usr/bin/grep -nic frank` on lines 40–50 returns `0`. Tying them to Frank is an inference from §1's Respondent row, and it is not labelled as one. In this chain, "relay" also means Amear → master. "Frank's relay" mixes up the sender and the relayer.

### 4. MINOR (S1/S2). A worker states unlabelled negatives about other agents

```
582 contact MFFU. This filing unit's manager and workers did neither.
772   send**. No agent in this filing unit drafted or sent it.
```
Transcript line 6 says the same. The addendum was "Written by. praxis-worker (BUILD)". A worker cannot observe what the manager or other workers did with their tools. These are unlabelled self-reports covering agents the writer could not see. The sentence that follows ("Whether any other agent did is ... UNVERIFIED") shows the right form. These claims should carry the same label or be attributed to whoever observed them.

### 5. MINOR (S1 precision). "per `CLAUDE.md`" is a paraphrase with an inserted term, not the file's text

```
addendum 621: TradingView alert → webhook → n8n → JSON file drop → NinjaScript FileSystemWatcher → bracket order (NinjaTrader 8) → Rithmic → MFFU.
CLAUDE.md:21: Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
```
"n8n workflow" became "n8n", and "(NinjaTrader 8)" was added. NinjaTrader 8 is supported elsewhere in `CLAUDE.md` (the Identity line), so nothing here is false. The text is not quoted, but it is attributed as if it were.

### Mapping verdicts (brief item 6). No break

| Row | Verdict | Assessment |
|---|---|---|
| F4 "this specific automation pattern" | DOES NOT ADDRESS | Defensible. It rests on what the reply names (0 hits for the PRAXIS components, V2), and the row explicitly leaves general-vs-specific to Amear. Not too harsh. It would be too generous only if the general bullet were read as specific, which the row does not do. |
| F4 "on a funded account" | PARTLY ADDRESSES | Fair. "funded accounts" and "simulated-funded, and live account stages" appear in the fence. The Tradovate scoping is left open. |
| §3.2 effective date | DOES NOT ADDRESS | Correct. No date and no "now" (V4). |
| §3.2 retroactivity | DOES NOT ADDRESS | Correct. There is no account identifier and nothing about opening dates. |

### Observations outside the graded criteria (not counted)

- The authorising `DECISION_LOG.md` row is not staged: `git show :DECISION_LOG.md | /usr/bin/grep -c '2026-10-28T20:54:29Z'` → `0`.
- Both evidence files are untracked: `git status --short docs/reports/evidence/ -uall` → `?? ...transcript.md`, `?? ...reply.png`.
- The transcript puts a blank line after `to me`. In the image, that gap is about 29 px (display scale), between the about 21 px gap between lines and the about 42 px gap between paragraphs. Whether to call it a gap is a judgement call, and it affects no quote.

## Files staged

None. I wrote only this report, which is not staged.

VERDICT: DEFECTS FOUND (1 blocking, 4 minor)

Result: FAIL
