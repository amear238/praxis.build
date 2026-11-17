# Adversarial re-check — F4 Davi-reply addendum (after the worker-5 fix)

## Task
Re-check the section `## Addendum 2026-10-28 — MFFU "Davi" reply (screenshot)`
(line 541 to end, file currently 770 lines) of
`docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`. Confirm the four prior
defects are fixed, that the fixes added no new problem, and re-grade the whole
addendum against S2, S8, the "F4 not met / not closer" limit and the "no PRAXIS
assessment" limit.

## Mode
ADVERSARIAL. Read-only. The only file written is this report. Nothing staged.

## Criterion
S2 (no claim above the evidence), S8 (Amear's questions not answered for him),
no wording that implies F4 is met or closer, no assessment of PRAXIS against the
reply's conditions. Plus: head-537 sha256 matches and 0 deletions.

## Process log
1. Checked the frozen-prefix hash and numstat, and compared them against the index copy.
2. Read the addendum (lines 530–770), the transcript, and the PNG. The image matches the fence line for line.
3. Rebuilt the fence the same way as `w3search.sh`. Re-ran the search and its positive controls. Re-hashed the PNG and its Desktop source.
4. Tested every `> ` blockquote line against the fence. Traced each inline `"..."` quote to the fence, §1, or SPEC_RUBRIC.
5. Checked the DECISION_LOG row `2026-10-28T20:54:29Z` against the addendum's claims about Amear's ruling.
6. Grepped for forbidden wording (satisf, discharg, closer, confirms, complies, narrow, progress).
7. Searched every log for a source for the new "Gmail connector was unavailable" claim.

## Verification evidence

Frozen prefix and append-only:
```text
$ wc -l docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
     770
$ head -n 537 <file> | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ git show :<file> | shasum -a 256 ; git show :<file> | wc -l
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
     537
$ git diff --numstat -- <file>
233	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ git diff --cached --numstat -- <file>
537	0	docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
```
The hash matches. There are 0 deletions against the index. The staged copy is exactly the 537-line frozen prefix.

Evidence hash (re-run):
```text
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
```

Search re-run. It matches the addendum's pasted output exactly:
```text
      25
NinjaTrader	0 / NT8	0 / Ninja	0 / Rithmic	0 / webhook	0 / n8n	0 / TradingView	0 / Tradovate	2 / API	2
13:Tradovate 13:API 13:Tradovate 14:API 14:Tradovate 14:API
CLAUDE.md: NinjaTrader 2 NT8 0 Ninja 4 Rithmic 3 webhook 1 n8n 4 TradingView 3 ; STATUS.md NT8: 40
```

Blockquotes against the fence. All 17 are verbatim:
```text
L602 L603 L604 L605 L606 L608 L636 L705 L706 L724 L727 L729 L732 L734 L736  FENCE-EXACTLINE
L708 L748  FENCE-SUBSTR
```

Inline quoted strings by source (abridged):
```text
SEC1  | Algo trading is now permitted at MFFU moving forward on all plans
OTHER | thank you for contacting / reaching out        <- see finding 4
OTHER | this specific automation pattern / on a funded account  (SPEC_RUBRIC.md:60-61, OK)
OTHER | on this account  (§3.2 line 119, OK)
(all others: FENCE)
```

Source for the Gmail-connector claim:
```text
$ /usr/bin/grep -c "Gmail connector\|connector was unavailable" DECISION_LOG.md DISPATCH_LOG.md AUDIT_LOG.md STATUS.md
DECISION_LOG.md:0
DISPATCH_LOG.md:0
AUDIT_LOG.md:0
STATUS.md:0
```
The claim appears only in the worker-written transcript (line 6), in the addendum itself, and in the worker-5 fix report.

## Findings

1. **MINOR (S2). Defect 3 is NOT fixed, and the fix added a new unsourced fact.** Lines 579–582:
   > No agent in this filing chain (master → manager → workers) read this message in Gmail; the Gmail connector was unavailable this session and the screenshot is the only source used. No agent in this chain contacted MFFU.

   Narrowing the claim to "this filing chain" still leaves it as a universal that the writer, a worker, cannot observe for the master or the manager. No dispatch or decision row is cited for it.
   The fix also adds "the Gmail connector was unavailable this session" as a fact. That claim has 0 hits in DECISION_LOG, DISPATCH_LOG, AUDIT_LOG and STATUS (pasted above), and the DECISION_LOG row `20:54:29Z` does not state it. It also does not say whose session is meant. It is UNVERIFIED but not marked so.
   The same class of universal was left untouched at lines 611–613:
   > No agent fetched it. … the policy-article URL in §1's table, which was also never fetched.

   "Never fetched" has no scope at all. Line 764, "No agent in this filing unit drafted or sent it", is narrowed in the same way and is still unobservable. The DECISION_LOG row does support "his to send".

2. **MINOR (S2, S8-adjacent). Defect 2 is only partly fixed.** The table rows now say "On the most natural reading, 'Tradovate' qualifies both …" (lines 629 and 631). That ranks the two parses with no evidence, and which parse holds bears directly on the NT8/Rithmic coverage question that belongs to Amear.
   The unhedged scope claim also survives at line 621:
   > The reply frames its permission around the **Tradovate API**

   "Its permission", singular and meaning the whole reply, conflicts with row 1 (line 628), which calls "Algo trading is permitted on all plans …" "a **general** permission". It also conflicts with F (line 760): "a general permission, or a Tradovate-framed permission". Whether the general bullet sits under the Tradovate lead sentence is exactly the S8 question, and line 621 settles it as fact. Each row still ends by deferring to Amear, so S8 is not outright answered.

3. **MINOR (S2, internal count). Defect 4 is fixed in content, but the count claim it contradicts was kept.** Line 730:
   > **Two greetings.** The body opens twice, with a third opener between the two greetings:

   It then quotes three opening blocks (L732, L734, L736). "Opens twice" together with "a third opener" is self-contradictory. The image shows three stacked openers. All three quotes are now present and verbatim.

4. **MINOR (S2). The repaired provenance sentence is literally false again.** Lines 562–564 say every quote "of the Davi reply or of the screenshot" comes from the fence. Line 738 puts a composite paraphrase in quotation marks as Davi's text:
   > So there are also two separate "thank you for contacting / reaching out" openers

   That string is not in the fence (`grep -cF` = 0). It has a lowercase "t" and a slash composite. Also, the §1 sender address `FRANK@myfundedfutures.intercom-mail.com` quoted at line 752 is not covered by the provenance accounting. That is an omission, not a falsehood. The Frank-line clause itself is now correct: the quote is from §1, line 28.

5. **MINOR (S2, new). "Reply"-wide negatives go further than the visible text.** Line 623 says "It **never mentions** NinjaTrader, Rithmic, …". Line 630 says "No date or effective date appears anywhere in the reply". Line 631 says "Nothing in the reply mentions …". The search covered only the visible fence. Transcript line 70 says:
   > Whether the body continues below `MyFundedFutures`. … a quoted section that Gmail has hidden or collapsed cannot be ruled out.

   The addendum's UNVERIFIED list in A (lines 585–591) leaves this item out. Each negative should be scoped to "the visible text".

### Checked and held (no break)
- **F4 not met / not closer.** The forbidden-wording grep found only the negations in F (lines 757–758, 765). Row 1 says "It is not narrowed here." Row 2's verdict, "PARTLY ADDRESSES", is about F4's "on a funded account" clause. It rests on a textual fact (funded accounts are named) and says that no account of Amear's is identified. I do not read it as partial discharge.
- **No PRAXIS assessment.** D compares only reply against reply ("three similar restrictions" from §1.1, lines 40–46, which exist as described) and says it is out of scope. Line 765 disclaims compliance. The pattern description at line 617 is taken from CLAUDE.md.
- **Amear's ruling (F).** DECISION_LOG `2026-10-28T20:54:29Z` contains "send a follow-up naming NinjaTrader 8 + Rithmic", "F4 stays FROZEN" and "Amear sends the follow-up himself". The addendum's claims match.
- **SPEC_RUBRIC.** The unstaged 10-line diff is the R-A/R-B/R-C no-verdict section. It is unrelated to F4 and was modified 2026-07-30. The F4 text at lines 59–61 is unchanged.
- **Sizes, hashes, the U+202F `xxd` bytes, the search output, and the URL** all match §1 line 37 and are reproduced or consistent.

## Files staged
None. This report is written but not staged.

VERDICT: DEFECTS FOUND (0 blocking, 5 minor)

Result: FAIL
