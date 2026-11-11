# Unit 2026-11-11-mffu-investigation-correction-1 — worker 6 (ADVERSARIAL)

## Task
Adversarial review of `docs/reports/2026-11-11-mffu-connection-investigation.md` (1378 lines; Correction 1 starts at line 287) and the unit reports `-worker1.md` .. `-worker5.md` (plus `-manager.md` for name and S13 counts). HEAD 85a803f. Only this file was written. No git index change. Nothing under `.claude/` was touched.

## Criteria
The brief's attacks 1-10: append-only; name tokens and personal details; S13 placement; OBSERVED backed by a paste; S2 overstatement; F4 / broker route / Sim guard; S8/S5; the replacement ticket against Amear's required elements and the R6 design; the fee line; the Fix-9 restatement.

## Process log
1. Built the rep token at runtime from the staged png name (length 4) and never typed it. Ran the diff of the original against the artifact and the name counts.
2. Read Correction 1: standing positions, C1.1-C1.4, C2.3, C2.4, C3.1-C3.3.
3. Re-ran 34 pasted commands with a harness. The harness takes the pasted block that follows each exact `$ cmd` line in the artifact, runs the command, and runs `cmp` on the two.
4. Read the return handoff (thread facts), the R6 design (`git show bf6fcc7:...`), and the four MFFU captures at bf6fcc7 (news, trading-day, consistency, plans-site).
5. Did one read-only fetch: `/tmp/mffu-fetch-61/`, a new empty dir, MFFU help search "ninjatrader fee". The page was treated as untrusted and read with sed/grep only. I also grepped the existing worker-3 fetch of article 10082979 (`/tmp/mffu-fetch-31/page.html`) for fee terms.
6. Grepped Correction 1 and the reports for F4 claims, approvals, and personal or infrastructure details.

## Verification evidence

Attack 1, append-only (rep token filtered to [rep]):
```text
$ diff /tmp/mffu-orig.md <artifact> | grep -E '^[0-9]'
1a2
61c62
105,106c106,107
282a284,1378
$ (first hunk) 1a2
> > CORRECTED 2026-11-11 — read Correction 1 at the end before relying on any line below; do not send the section 7 ticket, use the Correction 1 ticket.
$ shasum -a 256 /tmp/mffu-orig.md
2cc7869aef2f45754cec73516a56e0409393ca6b24c6549fa5b50b00b5fa6ceb  /tmp/mffu-orig.md
```
The three changed body lines (61, 105, 106) are the de-identification. The banner matches allowed edit (a). Nothing else differs. PASS.

Attack 2, rep-token counts (`grep -ci "$N"`):
```text
docs/reports/2026-11-11-mffu-connection-investigation.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-manager.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-worker1.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-worker2.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-worker3.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-worker4.md 0
docs/reports/2026-11-11-mffu-investigation-correction-1-worker5.md 0
```
Personal details: no person's full name, phone number, street address, account ID or order number appears in Correction 1 or the reports (grep for Bani-Ahmad, email, phone and address patterns). The only email address is support@myfundedfutures.com. The ticket has no name and no signature ("Thank you."). Infrastructure details: see Finding 6.

Attack 3, S13 (`grep -cF`, last non-blank line equal to the sentence):
```text
artifact   count=2 lines=136 1378  lastexact=1   (line 136 = original line 135, in the body, allowed)
manager    count=0                lastexact=0
worker1    count=1 lines=57       lastexact=1
worker2    count=1 lines=70       lastexact=1
worker3    count=1 lines=253      lastexact=1
worker4    count=1 lines=66       lastexact=1
worker5    count=1 lines=52       lastexact=1
```

Attack 4, re-runs (harness output; IDENTICAL means `cmp` exit 0):
```text
[1] IDENTICAL nl -ba ninjascript/PraxisSignalConsumer.cs | sed -n '36,50p;632,642p'
[2] IDENTICAL grep -n RequiredAccountPrefix ninjascript/PraxisSignalConsumer.cs
[3] IDENTICAL topology sed -n '9p;24p'
[4] IDENTICAL topology sed -n '29p;39p'
[5] IDENTICAL git ls-files | grep -i -E 'n8n|workflow|emitter|redis'
[6] IDENTICAL ls ninjascript/
[7] IDENTICAL ls ninjascript | grep -i emitter; echo exit=$?
[8] DIFF      grep -n -i -E 'redis|breaker|MaxQty|...' ninjascript/*.cs | head -40   (order only, see below)
[9] IDENTICAL handoff grep '19:43|abide|...'
[10] IDENTICAL handoff sed -n '132,133p'
[11] IDENTICAL grep -n 'D-2026-11-10-B' DECISIONS.md | head
[12] IDENTICAL sed -n '2047,2075p' DECISIONS.md | grep -c -i rithmic
[13] IDENTICAL topology sed -n '41p'
[14] IDENTICAL grep -n -i rithmic topology | cut -c1-200
[15] IDENTICAL nl -ba specs/SPEC_RUBRIC.md | sed -n "48,57p"
[16] IDENTICAL nl -ba specs/SPEC_RUBRIC.md | sed -n "15,18p;58p"
[17] IDENTICAL grep -c -F 'webhook -> n8n' specs/SPEC_RUBRIC.md
[18] IDENTICAL grep -c -i rithmic specs/SPEC_RUBRIC.md
[19] IDENTICAL strategy-filter-audit sed -n '62p'
[20] IDENTICAL cost-model sed -n '19p'
[21] IDENTICAL cost-model sed -n '21p'
[22] IDENTICAL DECISIONS.md sed -n '950p'
[23] IDENTICAL strategy-filter-audit sed -n '68p'
[24] IDENTICAL vm-handoff sed -n '20p'
[25] IDENTICAL MANIFEST wc/grep (377 / 0 / 0 / 375)
[26] same     git show HEAD:MANIFEST.md counts (369 / 367 / 448 / 0 / 0), compared by eye
[27] IDENTICAL grep -c "^|---" MANIFEST.md; grep -c "^## " MANIFEST.md
[28] DIFF      git show --stat a587a27 | head -15   (only the blank separator line my extractor captured)
[29] DIFF      head -3 0710am.csv   (CRLF in the file, LF in the paste; same visible text)
[30] IDENTICAL git show HEAD:walk-forward-spec | grep -n -i "intraday trailing"
[31] IDENTICAL git ls-files --error-unmatch walk-forward-spec; echo exit=$?
[32] IDENTICAL topology sed -n '14p'
[33] IDENTICAL DECISIONS.md sed -n '539p'
[34] DIFF      grep -rIl ... Redemtion   (same 8 files, different order)
== diff 8
10a11
> ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 ...
16d16
< ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 ...
```
Lines checked by hand against the files: capture `trading-day.txt:10`, `:12`, `:1109`, `:1111`; `plans-site.txt:24`; `news.txt:27-38`, `:50`; `adversarial.txt:542` ("5:05 PM EST ... CME Price Limits"); R6 design lines 14, 22, 96, 110; topology :22, :23, :26, :27; phase3 spec :102. Every one matches the quote in Correction 1. I sampled 18 OBSERVED grades in Correction 1 (lines 332, 379-387, 485, 841, 962-968, 1092, 1100, 1150, 1153, 1287-1289, 1337-1342). Each has a paste or a quoted source line with its location in the same item. There are no content mismatches, so no MAJOR under attack 4.

Attack 5, S2: all nine breakers are SPECIFIED (line 379). The emitter, the POST, the n8n gates and Redis are SPECIFIED (380-384). The consumer is IMPLEMENTED; TESTED is attributed to topology :27 with "this unit did not re-run it" (387). The #7 MaxQty reject is "partly IMPLEMENTED" (385). If anything that understates it, because topology :27 records the consumer as TESTED on Sim. No overstatement found.

Attack 6, F4 / route / guard:
```text
303: - Rubric F4 stays FROZEN / NOT MET. ...
748/752: quotes audit row A15 "(F4 closed; repo F4 evidence)" and calls it wrong
1317: "So MFFU would not be answering about 'this specific automation pattern', which is what F4 asks for."
(reports) worker4:31 "The audit row's 'F4 closed' contradicts the rubric's FROZEN listing"
```
No line says F4 is met, nearly met, or that the ticket will close it. Line 304 says the route is not decided. Line 305 says no Sim-guard change is proposed. C1.1 states "This correction does not propose it, draft it or estimate it." PASS.

Attack 7, S8/S5: the only approval is line 289: "Amear's go relayed by the Claude.ai channel (chat 2026-11-11 17:27Z, "U do them"), master's plan ... decided by master under D-2026-11-08-D D1". It names its relay chain and its decider. No question is answered for Amear. Q4's 9:30 AM wording comes from Amear's brief (see Finding 3).

Attack 8, ticket thread facts (handoff, untracked file):
```text
11: subject "Re: Re: Re: Written policy confirmation — automated execution on funded account"
20: 1. Platform and data: NinjaTrader 8, connected through Rithmic.
120:  1. Kindly be informed that we do not offer Rithmic at MFFu
121: 2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://...8444599-...
123: 4. You can trade using your strategy at the evaluation phase
133: - Not an answer: a request for identity verification ... OPEN-1 (evening entry vs overnight) is NOT answered.
135: ### Ticket closed — 2026-11-11T15:20:34Z
```
The ticket's subject, date (10 November 2026), Rithmic correction and the two acknowledged answers all match. Ticket questions against the R6 design (`git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md`):
```text
    22	- (i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage.
    43	- Exit: sell at market on the close of the bar stamped T−5 min on day E (08:25 for 08:30 releases; 13:55 for FOMC). ...
    66	- For every T1 release ...: exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2).
    67	- Exit: close of the bar stamped 16:05 ET on E.
```
MFFU captures at bf6fcc7:
```text
news.txt    27	No positions or orders (including limit orders) can be open 2 minutes before and after the release.
news.txt    28	All positions must be flattened at least two minutes prior to the scheduled ⁠T1 News event. For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00
news.txt    30	Restricted Accounts: Trading on T1 News events is prohibited for the following:
news.txt 33-35	Unrestricted Accounts: ... All evaluations / Builder Plans
trading-day 1111	If you do not place a trade within 7 consecutive calendar days on your sim funded account, the account will be closed due to inactivity. There is no inactivity rule on the live account.
consistency   46	If a trader does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts.
consistency   50	Traders taking a vacation should notify the customer support team if they will not be trading for more than 7 days.
```
Q1 is not answered on a page (funded permission). Q2 is not answered (article 10082979 says nothing on account type for funded accounts). Q4 is not answered (design :110, OPEN-1). For Q3 and Q5, see Findings 1 and 2.

Attack 9, fee. Line 1094: "NOT FOUND (three public pages fetched and searched...)". My re-checks:
```text
$ sed 's/<[^>]*>/ /g' /tmp/mffu-fetch-31/page.html | /usr/bin/grep -c -i -E 'fee|commission|licen|routing|charge'   (article 10082979, worker-3 fetch, sha b11ea9877ae69e26)
0
$ curl ... 'https://help.myfundedfutures.com/en/?q=ninjatrader%20fee'  -> /tmp/mffu-fetch-61/page.html
2026-11-11T17:55:51Z
200 86607 https://help.myfundedfutures.com/en/?q=ninjatrader%20fee
Search results for:  ninjatrader fee               NinjaTrader  : Login Instructions       NinjaTrader   Download and Connection Guide… Now let’s connect to   NinjaTrader  .
```
MFFU's own search for "ninjatrader fee" returns only the login article, and that article has no fee terms. Together these support NOT FOUND over COULD NOT BE CHECKED. However, Correction 1 does not paste either check (Finding 5).

Attack 10, Fix-9: line 452 quotes item 2 "automated trading is allowed provided you abide by our rules and policies" and item 4 "You can trade using your strategy at the evaluation phase". Both match handoff :121/:123 as verbatim substrings. Line 452 also states: "The reply does not say in writing that this specific pattern is allowed on a funded account." PASS.

Additional checks:
```text
$ git ls-files --error-unmatch docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
error: pathspec '...' did not match any file(s) known to git
$ git log --format=%H HEAD | grep -c '^bf6fcc7'          -> 0
$ git for-each-ref --contains bf6fcc7                     -> r6/announcement-research, origin/r6/announcement-research
$ git ls-tree -r --name-only HEAD | grep -i 'r6-mffu'     -> (none)
$ for p in '[VM MAC]' '[tailnet IP]' '[VM LAN IP]'; git grep -l -F "$p" HEAD | wc -l   -> 0, 0, 0 (values redacted by worker 7)
```

## Findings

1. **MAJOR. Ticket Q5 misstates the strategy's re-entry time (artifact line 1370; also C3.1 table line 1329).** The ticket says "flat 5 minutes before each Tier 1 release, with no new trade until 2 minutes after". The R6 design says "Flat from T−5 min to T+3 min" (design :22), and 2S re-enters "at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2)" (:66). Line 1329 says the ticket "uses the T+2 re-entry from MFFU's two-minute rule". That puts MFFU's minimum in place of the strategy's own window, and C3.2 R5 (line 1341) quotes T+3 itself. Also, on its face the timing part of Q5 is answered by `news.txt:27-28` (flat 2 minutes before and after; "may only be reopened after 8:32:00"). What the page leaves open is whether "Trading on T1 News events is prohibited" for Rapid/Pro (news.txt:30-32) means more than the ±2-minute window, and the Builder conflict (news.txt:33-35 vs :50). **Fix:** change Q5 to "5. My strategy is flat from 5 minutes before each Tier 1 release until 3 minutes after it. On Rapid and Pro Sim Funded, does "trading on T1 news events is prohibited" mean anything more than that window, for example no trading at all that day? And are Builder Sim Funded accounts restricted or unrestricted?" Then change line 1329's "T+2 re-entry from MFFU's two-minute rule" to "T+3 re-entry from the R6 design (:22)".

2. **MAJOR. Ticket Q3 partly asks what an MFFU page already answers, and leaves out the page line that bears on it (line 1368; C3.2 R3 line 1339).** "Does anything besides a trade count as activity" is answered by `trading-day.txt:1111` ("If you do not place a trade within 7 consecutive calendar days ... closed") and `consistency.txt:46`. "Or can I notify support instead?" is partly answered by `consistency.txt:50`: "Traders taking a vacation should notify the customer support team if they will not be trading for more than 7 days." R3 cites :46 but not :50. The case the page leaves open is a strategy that has no signal for more than 7 days, which is not a vacation. **Fix:** change Q3 to "3. Your Inactivity Rule article says traders on vacation should notify support if they will not trade for more than 7 days. My strategy can go more than 7 days without a signal. Can I notify support in that case too, or must the account place a trade at least every 7 days?" Then add `consistency.txt:50` to R3.

3. **MINOR. Q4 covers only the 08:25 exits (line 1369).** Design :43 says 1F exits at 13:55 for FOMC, and 2S holds to 16:05 (:67). Both are evening entries closed after 9:30 AM ET. The 9:30 AM wording comes from Amear's brief, so this worker does not change it. **Fix:** the manager asks Amear (via the master) whether Q4 should read "closed the next day before your 4:10 PM ET close (as early as 8:25 AM, as late as 4:05 PM ET)".

4. **MINOR. The ticket omits the article number 10082979, a required element (line 1360).** It names the article only by its title, "NinjaTrader: Login Instructions". The title is correct (line 972). **Fix:** "...your article "NinjaTrader: Login Instructions" (help article 10082979, account type "Simulation")."

5. **MINOR. The NOT FOUND fee grade is supported, but the paste is thin (line 1094).** The three pasted pages are a search on "commissions", ninjatrader.com/pricing (not an MFFU page), and the Tradovate login article. None of them is the NinjaTrader connection article. The "Understanding Live Funded Account" article that lists "Round-Trip Commissions and Fees" was not opened. **Fix:** add the two checks above to C2.3: 10082979 has 0 fee/commission/licen/routing/charge terms, and MFFU's search for "ninjatrader fee" returns only the login article. Then reword to "NOT FOUND (MFFU's NinjaTrader article and MFFU's own help search for 'ninjatrader fee' were read; neither states such a fee and neither rules it out)".

6. **MINOR. Infrastructure details are pasted without need (lines 464-466, inside the C1.3 grep paste).** The grep pattern `closed` pulled in handoff :65, :66 and :68: the VM MAC `00:0c:29:...`, LAN IPs, the tailnet IP, and the SSH key path and user. No tracked file at HEAD carries the MAC, the tailnet IP or the VM IP (0/0/0). Committing the artifact would publish them. **Fix:** in that block, pipe the grep through `| grep -v -E '^(65|66|68):'`, or replace those three lines with `[3 unrelated lines (VM network) omitted]`.

7. **MINOR. The main source for the MFFU replies is untracked.** `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md` is not known to git. C1.3, C3.1 and C3.2 R7/R8 cite it by line number. **Fix:** the master stages the handoff with this artifact, or line 450 says the file is untracked as of 85a803f.

8. **MINOR. The "committed" MFFU captures are not on main (C3.1 line 1314 ff., C3.2 line 1333).** bf6fcc7 is reachable only from `r6/announcement-research`. No `r6-mffu` file is in the HEAD tree. **Fix:** add "(bf6fcc7 is on branch r6/announcement-research, not on main; read with `git show bf6fcc7:<path>`)" to the C3.2 "Capture" definition.

9. **MINOR. The manager report has no S13 sentence (`-manager.md`, 29 lines, count 0).** That report may still be in progress. **Fix:** end it with the S13 sentence as its last standalone line.

10. **MINOR (note). Route wording in the ticket (line 1360): "I will use the NinjaTrader connection".** Line 304 says the route is not decided, and attributes the ticket wording to Amear's brief (REPORTED BY). That is not a decision by the unit. It is flagged only so the master knows the text Amear sends states an intention the repo records as open. **Fix:** none required; the master can mention it to Amear.

Non-findings: the reorderings in re-runs [8] and [34] come from glob or filesystem order. The CRLF difference in [29] comes from the CSV's line endings. Content is identical in all three.

## Result
FAIL: 2 MAJOR (Findings 1, 2), 8 MINOR, 0 BLOCKER. Rep-token count is 0 in the artifact and in all six unit reports.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
