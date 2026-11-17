# F4 Davi reply — adversarial confirm pass

**Task.** Check that five earlier defects are actually fixed, then review the whole addendum again from scratch.
**Mode.** ADVERSARIAL (read-only. The only file written is this report. Scratch files went to the session scratchpad.)
**Artifacts.** (a) the addendum, `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` lines 541–776; (b) `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md`; (c) `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`.
**Criteria.** F4, S1, S2 and S8 (`specs/SPEC_RUBRIC.md`), plus the hard limits in the brief.

---

## Process log

1. Checked the hard limits: the history hash, numstat, and whether SPEC_RUBRIC was touched.
2. Re-ran every fenced command in the addendum and diffed the output against what was pasted.
3. Wrote a script that checks every blockquote and every inline `"…"` quote in the addendum against the transcript fence, `CLAUDE.md`, the 537 history lines and the rubric.
4. Compared the transcript with the image, both at full size and in two zoomed crops (`sips`).
5. Checked these facts at their source: the DECISION_LOG row, the agent `tools:` lines, the URL against §1's table, the PNG dimensions, and dates and "now" in the fence.
6. Re-checked the five earlier defects. Then looked for contradictions and checked each verdict for wording that was too generous or too harsh.

## Verification evidence

**Hard limits**
```
$ head -n 537 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git diff --numstat -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
239	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ stat -f '%Sm' specs/SPEC_RUBRIC.md
Jul 30 11:50:39 2026          # its unstaged diff is the R-A/R-B/R-C block at line 263, not F4
```

**A's provenance block, re-run. The output matches what was pasted.**
```
$ shasum
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ ls
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
$ xxd
00000000: e280 af50 4d2e 706e 67                   ...PM.png
$ sips -g pixelWidth -g pixelHeight ...png
  pixelWidth: 2866
  pixelHeight: 930
```

**C's search block.** I took the script from addendum lines 657–666, changed only the temp filename, ran it, and diffed the result against the pasted output at lines 672–698.
```
SEARCH OUTPUT IDENTICAL
script matches w3search.sh
fence = transcript lines 15-39
```

**Quote check (script `advQ.py`)**
```
== blockquote lines
605 FENCE  606 FENCE  607 FENCE  608 FENCE  609 FENCE  611 FENCE  642 FENCE
711 FENCE  712 FENCE  714 FENCE  730 FENCE  733 FENCE  735 FENCE  738 FENCE
740 FENCE  742 FENCE  754 FENCE
== inline double-quoted strings (substantive ones)
['CLAUDE.md'] 'Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript Fil…'
['CLAUDE.md'] 'TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU'
['FENCE'] 'custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded acco…'
['FENCE(prefix, ellipsis)'] 'Algo trading is permitted on all plans ...'
['FENCE'] 'integrate your trading bot or automated strategy via the Tradovate API'
['FENCE'] 'your MyFundedFutures Tradovate evaluation and funded accounts'
['FENCE'] 'simulated-funded, and live account stages'
['HIST'] 'Algo trading is now permitted at MFFU moving forward on all plans ...'
MISSING 'this specific automation pattern' / 'on a funded account'   -> rubric wording, SPEC_RUBRIC.md:60-61 (verified)
MISSING 'your ... accounts'  -> elision of a FENCE string
(other MISSING rows are shell-quote fragments from the script fence, not quotations)
```
```
$ sed -n 21p CLAUDE.md
Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU
$ grep -n 'TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU' CLAUDE.md
4:- Automated trading infrastructure: TradingView → n8n → NinjaTrader 8 → Rithmic → MFFU
backtick strings vs transcript: is f:4  Thank you for contacting:1  Thank you so much for reaching out:1  eda.daniel.david:1
§1 FRANK@ address present in history: 1
URL in fence vs §1 table line 37: IDENTICAL
```

**Fact checks**
```
DECISION_LOG.md:435 [2026-10-28T20:54:29Z] WHO: amear | WHAT: **F4 evidence: FILE the MFFU "Davi" reply AND send a follow-up naming NinjaTrader 8 + Rithmic. F4 stays FROZEN.** … HOW: … Amear sends the follow-up himself
praxis-worker: tools: Read, Grep, Glob, Bash, Write, Edit, TodoWrite
praxis-manager: tools: Agent(praxis-worker), Read, Grep, Glob, Bash, Write, Edit, TodoWrite
fence: word "now" -> 0 hits; digits -> "1" (preview), "8444599" (URL); "today" x2 (lines 9, 11) — relative, not a date
```
The image matches the transcript. The zoomed crops confirm `is specific is f`, `Hello amear,i` and `I'll be happy to assist you today.`

---

## Earlier defects: are they fixed?

| # | Defect | Status | Basis |
|---|---|---|---|
| i | "one explicit grant" | **Partly fixed** | The phrase is gone. Line 623 now reads "The only grant in the reply that names a platform", which still counts grants. See finding 1. |
| ii | "per CLAUDE.md" paraphrase | **Fixed** | Line 621 now matches `CLAUDE.md:21` byte for byte. The NT8 point is now its own sentence, sourced to the Identity line (`CLAUDE.md:4`, also byte-exact). |
| iii | "New conditions" heading | **Fixed** | The heading is now "D. Conditions the reply states (for the record only)", and line 722 says "three similar restrictions". |
| iv | §1.1 attributed to Frank | **Fixed** | Line 723 now reads "in the relay recorded in §1 (whose respondent §1's table records as Frank)". That links §1.1 to Frank only through §1's table, and the history's own wording at line 226 ("the relayed reply") supports the link. It does not attribute §1.1 to Frank directly. |
| v | Unobservable universals | **Partly fixed** | Line 582 is now labelled as an attestation. The fetch negatives and the "drafted" claim still go beyond it. See finding 3. |

## Findings

### 1. MINOR (S2/S8, left over from defect i). "The only grant … that names a platform" counts grants, and the count depends on how the bullets are read
```
623: The only grant in the reply that names a platform names the **Tradovate API**: "custom Tradovate
625: Its "Algo trading is permitted on all plans ..." bullet is unqualified; whether
626: that bullet sits under the Tradovate sentence or stands as a general permission
627: is not stated in the reply, and how to read it is Amear's ruling (S8).
fence 14: • Automated trading solutions using an API are supported, allowing you to integrate … via the Tradovate API.
```
Bullet 1 (fence line 14) names the Tradovate API on its own. "The only grant" is true only if bullet 1 sits under the opening sentence. That is the same question about how the bullets relate to the sentence that lines 626–627 leave to Amear for bullet 3. Read the bullets as standalone and two grants name a platform. Line 625 also calls the algo bullet "unqualified" in the same sentence that says whether it is qualified is undetermined. The substantive point, that Tradovate is the only platform named, holds on both readings: the search shows Tradovate on lines 13–14 and 0 for every other platform. So this is not a false fact, and it is MINOR.

### 2. MINOR (S2/S8). Row 1 gives one label to a gap that differs by reading
```
634: … whether it stands as a general permission or sits under the Tradovate sentence is Amear's ruling
     (S8, see above). On either reading it names no specific pattern, which is the same specific-vs-general
     gap §3.5 already recorded for Frank's relayed line.
```
If the bullet sits under the Tradovate sentence, it is a permission scoped to the Tradovate API. The gap is then the wrong specific pattern, not specific against general. "On either reading … the same specific-vs-general gap" holds only on the general reading. The DOES NOT ADDRESS verdict stands on both readings, so the verdict is not affected. MINOR.

### 3. MINOR (S1/S2, left over from defect v). Negatives about the unit's conduct are not covered by the attestation
```
582: On the manager's attestation, this filing unit's manager and workers did neither [read Gmail / contact MFFU]:
     no brief in this unit asked for Gmail access, email drafting or contact with MFFU …
615: This filing unit did not fetch it (the brief forbids it).
770: On the same manager's attestation (see A), no agent in this filing unit drafted or sent it.
776: Not claimed: anything about what the help-center URL says. It was not fetched.
```
A's attestation covers two acts: reading Gmail and contacting MFFU. Lines 615 and 776 state that the URL was not fetched, a claim about the unit's tool calls, with no label. Line 776 gives no scope at all. Line 770 points to A to support "drafted", but on drafting A only says that no brief asked for it, which is not an attestation about what anyone did. Neither the master's brief nor the manager's attestation is on disk. A attaches "not on disk" only to the brief. MINOR, the same severity earlier rounds gave this class of claim (`…-adversarial-final.md` #4, `…-adversarial-recheck.md` #1).

### 4. MINOR (internal consistency). "Preceding" conflicts with the F disclaimer about thread position
```
591: - the full text of Amear's preceding message. Only its collapsed preview is
639: **Amear's truncated follow-up.** The preview of Amear's preceding message reads,
752: … Amear's preceding message, as previewed,
772: - Not claimed: anything about the date of this reply, or its position in the
773:   thread relative to Frank's reply or to Amear's messages.
```
Three times the addendum says Amear's message precedes the reply. Then F disclaims any claim about where the reply sits relative to Amear's messages. In display order, "preceding" is observed: the collapsed message sits above. Without timestamps, chronological order is inferred from Gmail's layout. Not false, but the two statements contradict each other as worded. MINOR.

### Checked and not broken
- **Hard limits.** Lines 1–537 are unchanged and nothing was deleted. Nothing says or implies that F4 is met, satisfied or closer to discharge. A search for satisf, discharg, closer, confirm, covers, complies, progress and toward finds them only in negations, in the F list, or inside quoted text. PRAXIS is not assessed against the conditions in D (lines 721, 725, 771).
- **Quotes.** Every quote matches its source byte for byte: the fence, `CLAUDE.md:4`, `CLAUDE.md:21`, §1 and the rubric. The `...` elisions are clean prefixes, and the URL is byte-identical to §1's.
- **Pasted output.** Both pasted command blocks reproduce exactly.
- **Transcript.** It matches the image, including the quirks (`amear,i`, `Hi !`, `is f`, Michael/Davi). The em-dash and apostrophe codepoints are labelled UNVERIFIED.
- **Verdicts.**
  - Row 1, DOES NOT ADDRESS: neither too harsh nor too generous. NT8 and Rithmic each score 0.
  - Row 2, PARTLY ADDRESSES: fair. "funded accounts" is present, and the Tradovate scoping and Amear's account are left open.
  - Row 3, DOES NOT ADDRESS: correct. The fence has no date, and "today" is relative.
  - Row 4, DOES NOT ADDRESS: correct. There is no account identifier and no word on retroactivity.
- **S8.** Every reading-dependent question is sent to Amear. The F description of his ruling matches DECISION_LOG:435.
- **Facts.** These all match their sources: the PNG at 2866x930 and 254350 bytes, the sha256, the U+202F byte, the worker `tools:` line, the search counts ("3 occurrences across 2 lines"), and the controls (six of seven fire in `CLAUDE.md`, NT8 has 40 lines in `STATUS.md`).

**Not graded (outside the brief's scope).** `docs/reports/evidence/` is untracked (`?? docs/reports/evidence/`). If the addendum is committed without it, the addendum's references to the PNG and the transcript will point to files that are not in the repo.

---

## Files staged
None. This worker writes only this report and does not stage it.

VERDICT: DEFECTS FOUND (0 blocking, 4 minor)

Result: PASS
