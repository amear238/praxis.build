# Unit 2026-11-11-mffu-investigation-correction-1 — worker 3 report

## Task
Draft the replacement for the §7 MFFU support ticket in `docs/reports/2026-11-11-mffu-connection-investigation.md` (lines 223-248). Output is correction text at `/tmp/mffu-corr/w3.md`, to be pasted verbatim into the target's `## Correction 1` as C3.1 / C3.2 / C3.3. Authority: master's plan, DECISION_LOG 2026-11-11T17:32:05Z, decided by master under D-2026-11-08-D D1. Mode: BUILD. The target file was not edited. Nothing was staged, and git's index was not touched.

## Rubric criteria
- F4 (subject matter only; this unit does not grade it): "Written confirmation from MFFU that this specific automation pattern is permitted on a funded account." F4 stays FROZEN. Nothing in this unit changes that.
- S2: each rule statement is graded at the level its evidence supports (C3.2).
- S8: no question that belongs to Amear is answered for him. The ticket describes the native NinjaTrader connection as the setup Amear intends to use (REPORTED BY Amear's brief). The broker route is not decided here.
- S13: the standing limitation line closes this report and is not in w3.md.

## Process log
1. Built the rep-name variable at runtime from the staged PNG path (length 4). Every pasted read was filtered through `sed "s/$N/[rep]/Ig"`. The name was never typed.
2. STEP 1: read all 136 lines of `docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md`. Relevant lines are pasted below. Lines 13-15, 37-42, 84-86 and 98-103 are left out: they are fences, greetings and the two signature lines carrying a personal name.
3. Read `/tmp/mffu-orig.md`. It is identical to the target (`diff -q` printed nothing). Read lines 1-40, 100-130 and 200-260.
4. STEP 2: ran the ten requested `grep -rn -i` patterns over `docs/` and `specs/` (counts below). The R6 design `docs/specs/2026-11-09-r6-announcement-research-design.md` is **not on main**. It is on branch `r6/announcement-research` at commit `bf6fcc7`, so it was read with `git show bf6fcc7:...`, along with its raw MFFU captures under `docs/reports/evidence/2026-11-09-r6-mffu-*.txt`.
5. Found the earlier MFFU written reply (2026-10-28 screenshot transcript, tracked at `docs/reports/evidence/2026-10-28-mffu-[rep]-reply-transcript.md`). Only its unnamed permission lines (27-33) are pasted, because other lines carry personal names.
6. No on-disk content capture of article 10082979 exists. `docs/reports/2026-11-05-mffu-fee-check.md:43` records only that a fetch returned 200. So I fetched it plus three rule pages, 4 of the allowed 5 fetches, each into a new empty dir: `/tmp/mffu-fetch-31` .. `-34`. Text was pulled out with sed/grep only, and nothing from the pages was executed.
7. STEP 3: drafted w3.md and trimmed the ticket from 327 to 269 words (261 without the Subject line). That is still above the ~250 aim. I stopped trimming rather than drop a required item.
8. A scratch word-count file `/tmp/mffu-corr-ticket-count.txt` was created by mistake and deleted in the next command. It is outside the two allowed files and is reported here for completeness.

## Verification evidence (command output)

### E1 — handoff file (nl -ba, rep name filtered)
```
     9	### V1 — MFFU follow-up email: SENT (F4; rubric F4 Owner = Amear)
    11	- Sent 2026-11-10T19:29:01Z from Amear's Gmail as a reply in the existing MFFU support thread (Gmail message id `1a1c6ef68efc93d2`, thread `19f9edc188595b0c`; subject "Re: Re: Re: Written policy confirmation — automated execution on funded account"; to the support rep's MFFU Intercom address). OBSERVED by the channel vi
    16	Thanks for confirming that algorithmic trading is allowed on all plans. Your reply mentioned the Tradovate API, but my setup is different, so I want to describe it exactly and get a written answer for this specific configuration before I trade it on a funded account.
    20	1. Platform and data: NinjaTrader 8, connected through Rithmic.
    22	2. Signal generation: a NinjaTrader 8 strategy I wrote (the "emitter") watches NQ and, when its rules trigger, sends a signal to a local n8n workflow (a webhook) running on my own computer.
    24	3. Risk checks: the n8n workflow runs my own risk checks (daily loss limit, max trades per session, session time limits) and, if they pass, writes the signal to a file in a local folder.
    26	4. Order placement: a second NinjaTrader 8 strategy (the "consumer") reads that file and places the order as a bracket order (entry, stop loss and take profit) through Rithmic, on my account only.
    32	1. Is this exact setup (NinjaTrader 8 automated strategies placing bracket orders over Rithmic, with signals passing through a local n8n webhook and a file drop) permitted on a MyFundedFutures funded account?
    34	2. Is it also permitted during the evaluation?
    36	3. Are there any rules on automated trading that apply to this setup, for example around news events, trading hours, or order frequency?
    43	- F4 stays FROZEN. This covers the outgoing half of the unblock condition (55979ee). Still needed: MFFU's dated written reply, with headers, saying the pattern is permitted on the funded account. ...
    48	- Context REPORTED BY the channel from MFFU's public help pages during the session, NOT verified in this repo: MFFU auto-closes open positions at 4:10 PM ET on regular days; trading restarts at the 6:00 PM ET open; holiday early closes are not auto-liquidated (manual close). Filer to verify before citing.
    64	- `vmrun list`: 1 running VM, `/Volumes/VMs/Windows 11 Fusion.vmwarevm/Windows 11 Fusion.vmx`. ...
    66	- n8n (`n8n-compose-n8n-1`) publishes `127.0.0.1:5678` only; ...
    81	### V6 — Second MFFU email: SENT (asks R6 OPEN-1)
    83	- Sent 2026-11-10T22:49:22Z, same thread (`19f9edc188595b0c`), Gmail message id `1a1c7a6d7d0d0dec`. OBSERVED by the channel via the Gmail connector at 22:53Z. ...
    89	Some of my strategies enter a position in the evening, after the 6:00 PM ET Globex open, and close it the next morning before 9:30 AM ET, ahead of a scheduled economic release. The position is always closed well before the 4:10 PM ET session close, and it is never held through the 4:10 PM to 6:00 PM ET break.
    93	1. Does a position opened after 6:00 PM ET and closed the next morning count as holding overnight under MFFU rules, or is it inside a single trading day?
    95	2. Is this allowed on evaluation accounts, Sim Funded accounts (Rapid, Pro and Builder), and live accounts?
    97	3. These trades close at least 5 minutes before any T1 news release. Is that enough to comply with the news rule?
   112	## MFFU replies to V1 and V6 — OBSERVED by the Claude.ai channel via the Gmail connector, 2026-11-11T17:00Z (thread `19f9edc188595b0c`; rep names replaced by `[rep]`)
   114	### Reply to V1 — 2026-11-10T19:43:42Z, from support@myfundedfutures.com (message `1a1c6fce04330f0d`), verbatim:
   120	 1. Kindly be informed that we do not offer Rithmic at MFFu
   121	2. Kindly be informed that automated trading is allowed provided you abide by our rules and policies : https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
   122	3. Kindly reach out to tradovate concerning inquiries concerning API as they are best regulated on advsing in that regards
   123	4. You can trade using your strategy at the evaluation phase
   130	- Channel's reading (INFERRED): the D-2026-11-10-B pattern, as worded (NT8 over Rithmic), cannot run at MFFU. Funded-account permission for the pattern is not stated; item 4 names the evaluation only. F4 stays NOT MET. ...
   132	### Reply to V6 — 2026-11-10T23:08:17Z, from support@myfundedfutures.com (message `1a1c7b82f130416b`)
   133	- Not an answer: a request for identity verification (full name, address, email, phone, and account ID or recent order number or last 4 of card). OPEN-1 (evening entry vs overnight) is NOT answered.
   135	### Ticket closed — 2026-11-11T15:20:34Z (message `1a1cb3255cf62d16`)
   136	- "we see you've been inactive for some time, so this ticket is being closed." Any re-ask needs a new ticket or a reply that reopens it (Amear's hands; the verification details are his to give).
```
(Lines 11, 43, 64, 66, 83 and 130 were cut at about 330 characters, marked with `...`.) Dates in ET: V1 reply 14:43 ET and V6 reply 18:08 ET, both on 10 November 2026. That is why the ticket says "(10 November 2026)".

### E2 — old §7 ticket (`/tmp/mffu-orig.md`, nl -ba; `diff -q` against the target printed nothing)
```
   225	*Below is the exact text to be copied and submitted by Amear directly from his authenticated MFFU user dashboard. It contains no personal details, uses plain English, and specifically targets the three open compliance questions.*
   232	I am preparing to trade an automated trading strategy using NinjaTrader 8 Desktop connected to my MFFU account via the native "NinjaTrader" connection (as described in your help article "NinjaTrader: Login Instructions"). 
   234	The strategy runs on NinjaTrader Desktop and places bracket orders (market entries with automated resting stop-loss and take-profit orders).
   239	Your previous reply confirmed that automated strategy trading is permitted during the evaluation phase. Can you confirm that this exact same setup (automated execution via NinjaTrader Desktop) is also fully permitted on Funded accounts once passed, provided all standard trading rules are followed?
   242	Your rules prohibit holding positions overnight. If an automated position is opened during the evening session (for example, entering after 6:00 PM ET) and is completely closed before the 9:30 AM ET market open the following morning, does this comply with your rules, or is any trade held past 5:00 PM ET considered "holding overnight"?
   245	Regarding Tier 1 economic news events: if the strategy automatically closes all open positions at least 5 minutes prior to the scheduled news release, and places no new trades until after the release window passes, does this fully satisfy your news trading policy?
```

### E3 — STEP 2 grep counts over docs/ and specs/
```
=== 4:10:       12 hits
=== inactiv:        4 hits
=== Tier 1:        8 hits
=== T1 :      144 hits
=== news:       30 hits
=== Simulation:      182 hits
=== 10082979:        4 hits
=== overnight:      100 hits
=== 6:00 PM:       24 hits
=== OPEN-1:       11 hits
```
Selected hits (rep name filtered):
```
docs/specs/2026-11-10-f2-session-flat-proposal.md:52:| MFFU flat time | MFFU auto-closes at 4:10 PM ET (R6 step 1, `bf6fcc7`). | Rule F2-1's 16:00 is 10 minutes inside it. MFFU also warns about orders after 4:10 PM (trading-day.txt:15) [E15]. |
docs/reports/2026-11-10-f1-f2-proposal-manager.md:214:10: Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
docs/reports/2026-11-10-f1-f2-proposal-manager.md:215:12: At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days. ...
docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md:136:- "we see you've been inactive for some time, so this ticket is being closed." ...
docs/reports/2026-11-10-f4-grading-worker3.md:99:● Tier 1 Economic Data Trading: Engaging in trades during tier 1 economic data releases is restricted.
docs/reports/2026-11-05-mffu-fee-check.md:43:200 119638 10082979-ninjatrader-login-instructions
docs/reports/2026-11-09-d11-sweep-manager.md:1902:| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
```
The R6 design is on a branch, not main:
```
$ ls docs/specs/2026-11-09-r6*
(eval):1: no matches found: docs/specs/2026-11-09-r6*
$ git ls-tree -r --name-only r6/announcement-research | grep ...
docs/specs/2026-11-09-r6-announcement-research-design.md
```

### E4 — R6 design (`git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | nl -ba`)
```
    14	| T1 news rule | T1 = "FOMC Meetings, FOMC Minutes, Employment Report, CPI" (news.txt:38). Flat from 2 minutes before to 2 minutes after (news.txt:27-28). The policy text restricts "Rapid Sim Funded" and "Pro Sim Funded" and leaves "All evaluations" and "Builder Plans" unrestricted (news.txt:30-35). Conflicts: the 2026 T1 image banner says "strictly prohibited on sim funded accounts" without naming plans, ...
    15	| Evening entry vs trading day | "Trades may be placed beginning at 6:00 PM EST ... can remain open until the New York session closes at 4:10 PM EST" (trading-day.txt:10). ... MFFU never says "trading day" for an evening entry. | session window OBSERVED; "same trading day" UNVERIFIED ...
    16	| Flat-by time | "automatically closed at 4:10 PM EST on regular (non-holiday) trading days" (trading-day.txt:12). No 16:59 rule in the 27 page blocks of the committed captures (zero hits, OBSERVED, report Correction 1 C3); ...
    19	**Time zone [D1].** MFFU writes "EST" year-round, ... This design reads MFFU's "EST" as US Eastern local time (EST in winter, EDT in summer). INFERRED: ...
    22	- (i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage.
    96	- Inactivity (7 calendar days): of 173 gaps between consecutive event dates in range, 90 exceed 7 days and the longest is 37 (E8). A standalone event strategy therefore fails the inactivity rule on Sim Funded accounts. ...
   110	| OPEN-1 | MFFU terms (F4 channel, owner Amear) | "Holding overnight will breach" is glossed by the FAQ as "closed before the daily session close", which an 18:05→08:25 hold meets; no MFFU text says it in terms of an evening entry. A written MFFU answer is needed before any funded use. | OPEN |
```

### E5 — committed MFFU raw captures at bf6fcc7 (`git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-<f>.txt | nl -ba`)
```
--- trading-day.txt
     1	URL: https://help.myfundedfutures.com/en/articles/9558251-permitted-times-to-trade
     2	FETCHED_UTC: Mon Nov  9 09:06:22 UTC 2026
     3	HTTP: 200
    10	Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
    12	At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days. Holiday trading hours will be communicated to traders including closure of open positions.
    15	Note: Make sure that you don’t force a trade multiple times on the market after 4:10 PM EST, as this will sometimes cause the order to go through and disqualify your trading account.
   763	URL: https://help.myfundedfutures.com/en/articles/14290805-builder-plan-50k-a-comprehensive-guide
  1108	Q: Can I hold positions overnight?
  1109	No. All positions must be closed before the end of the trading session. Any open positions at session close will be automatically closed by the platform.
  1110	Q: What is the inactivity rule on the sim funded account?
  1111	If you do not place a trade within 7 consecutive calendar days on your sim funded account, the account will be closed due to inactivity. There is no inactivity rule on the live account.
--- consistency.txt (second page block)
    34	URL: https://help.myfundedfutures.com/en/articles/16596524-inactivity-rule-one-time-payment-model
    35	FETCHED_UTC: Mon Nov  9 09:06:24 UTC 2026
    44	Inactivity Rule Changes (Effective August 25th)
    45	New accounts purchased under the one-time payment model are subject to a new inactivity policy:
    46	If a trader does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts.
    47	An inactivity breach on a Sim Funded account results in the forfeiture of all profits.
    50	Traders taking a vacation should notify the customer support team if they will not be trading for more than 7 days.
--- news.txt
     1	URL: https://help.myfundedfutures.com/en/articles/8230009-news-trading-policy
     2	FETCHED_UTC: Mon Nov  9 09:06:22 UTC 2026
    20	Ensuring no open positions or orders are active in the order book 2 minutes before and after any data release.
    27	No positions or orders (including limit orders) can be open 2 minutes before and after the release.
    28	All positions must be flattened at least two minutes prior to the scheduled ⁠T1 News event. For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00
    30	Restricted Accounts: Trading on T1 News events is prohibited for the following:
    31	Rapid Sim Funded
    32	Pro Sim Funded
    33	Unrestricted Accounts: Trading on T1 News events is permitted for the following:
    34	All evaluations
    35	Builder Plans
    38	For All Traders: FOMC Meetings, FOMC Minutes, Employment Report, CPI
    50	The above are the T1 news events to be avoided on all news-restricted accounts. See above for detailed list.
--- plans-site.txt
     1	URL: https://myfundedfutures.com/plans/rapid
     2	FETCHED_UTC: Mon Nov  9 09:07:41 UTC 2026
    23	Q: Can I hold positions overnight on Rapid?
    24	A: No. Rapid is intended for intraday futures trading. All positions must be closed before the daily session close. Holding overnight will breach the account.
--- adversarial.txt
   332	T1 news trading is allowed during the Evaluation and Sim Funded stages. You may open and hold positions through any scheduled T1 news event without limitation.
   484	News trading is fully unrestricted during the evaluation and sim funded stage. You may open and hold positions through any scheduled news event without limitation.
```
"5:00 PM" grep over all seven captures (trading-day, plans-site, plans, news, adversarial, consistency, drawdown) for `5:00 ?PM|5 ?PM|16:59|4:59`:
```
adversarial:542:The price limits are updated at 5:05 PM EST after each trading session and can be found on the CME Price Limits page.
(end 5PM grep)
```

### E6 — earlier MFFU written reply (tracked transcript `docs/reports/evidence/2026-10-28-mffu-[rep]-reply-transcript.md`, unnamed lines only)
```
    27	You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
    28	• Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
    29	• Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
    30	• High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
    31	• For live accounts, automated trading must comply with CME guidelines.
    33	You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
```

### E7 — read-only re-fetches (help.myfundedfutures.com only; 4 of 5 allowed)
```
/tmp/mffu-fetch-31 2026-11-11T17:36:12Z HTTP=200 bytes=  119637 sha=b11ea9877ae69e26 https://help.myfundedfutures.com/en/articles/10082979-ninjatrader-login-instructions
/tmp/mffu-fetch-32 2026-11-11T17:36:12Z HTTP=200 bytes=   95713 sha=b3abf2d40c4184e5 https://help.myfundedfutures.com/en/articles/16596524-inactivity-rule-one-time-payment-model
/tmp/mffu-fetch-33 2026-11-11T17:36:13Z HTTP=200 bytes=   95780 sha=5f368e64afeaec43 https://help.myfundedfutures.com/en/articles/9558251-permitted-times-to-trade
/tmp/mffu-fetch-34 2026-11-11T17:36:13Z HTTP=200 bytes=  107224 sha=eb1886344139e447 https://help.myfundedfutures.com/en/articles/8230009-news-trading-policy
```
(sha = first 16 hex chars of sha256 of page.html.) All four pages are server-rendered: the article text is in the HTML. Extraction: `sed -e 's/<[^>]*>/\n/g'`, entity decode via sed, blank lines dropped, `nl -ba`.
```
--- fetch-31 (10082979)
    84	NinjaTrader: Login Instructions
    87	August 24, 2026
    99	If you choose to trade on NinjaTrader Desktop, follow these steps to set up your MyFundedFutures connection:
   106	Among the available connections, find and select 
   107	NinjaTrader
   108	, then click add.
   109	Under the Configured window, click My NinjaTrader. In the properties window, enter your Username and Password using your MFFU credentials (available on your MFFU dashboard). Lastly, set the account type to “Simulation”, click Apply, and then OK.
   110	Once you’re back on your NinjaTrader Dashboard, click Connections again and select My NinjaTrader to connect to your MFFU account.
  grep -n -i -E 'evaluation|funded|live' (visible-text hits only; lines 1, 2 and 137 are JSON-LD / app JSON):
   120	Get Funded to trade on NinjaTrader
   121	If you have any questions regarding NinjaTrader setup or encounter connection issues, please contact our support team on the live chat or at 
--- fetch-32 (16596524)
    90	Inactivity Rule Changes (Effective August 25th)
    91	New accounts purchased under the one-time payment model are subject to a new inactivity policy: 
    92	If a trader does not place a trade for 
    93	7 consecutive calendar days
    94	, the account could be closed. This includes simulated funded accounts. 
    95	An inactivity breach on a Sim Funded account results in the forfeiture of all profits. 
    98	Traders taking a vacation should notify the customer support team if they will not be trading for more than 7 days.
--- fetch-33 (9558251)
    88	Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
    90	At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days. Holiday trading hours will be communicated to traders including closure of open positions. 
--- fetch-34 (8230009)
   107	No positions or orders (including limit orders) can be open 2 minutes before and after the release.
   108	All positions must be flattened at least two minutes prior to the scheduled ⁠T1 News event. 
   109	For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00
   115	Rapid Sim Funded
   116	Pro Sim Funded
   121	All evaluations
   122	Builder Plans
   126	: FOMC Meetings, FOMC Minutes, Employment Report, CPI
   140	The above are the T1 news events to be avoided on all news-restricted accounts. See above for detailed list. 
```

### E8 — checks on the drafts
```
$ awk '/^```text/{f=1;next} /^```/{f=0} f' /tmp/mffu-corr/w3.md | wc -w
     269
$ ... | grep -v '^Subject:' | wc -w
     261
$ awk '/^```text/{f=1;next} /^```/{f=0} f' /tmp/mffu-corr/w3.md | grep -n -i -E "5:00|amear|bani|@|phone|address|account id|19f9|signature|rep\]|$N" ; echo "ticket-hits-exit=$?"
ticket-hits-exit=1
$ grep -c 'ticks/side slippage' /tmp/mffu-corr/w3.md
0
```
Exit 1 means no match. The ticket has no 5:00, no name, no "@" (so no email address), no phone, no address, no account ID, no thread ID and no rep name. An earlier run of the same check also included two other personal names seen in on-disk transcripts. It also matched nothing. Those names are deliberately not written here.

### E9 — rep-name counts (`grep -ci "$N"`, N built at runtime)
```
$ echo "w3.md: $(grep -ci "$N" /tmp/mffu-corr/w3.md)"; echo "report: $(grep -ci "$N" $R)"
w3.md: 0
report: 0
```
(R = this report. The count was run before this block was added. The block adds only `$N`, never the name.)

## Findings outside scope (reported, not fixed)
1. The target's line 19 says the "Simulation" account type is set "for evaluations". Today's fetch of article 10082979 does not say evaluations (E7: no "evaluation" match in the visible text). That is why ticket question 2 asks MFFU.
2. MFFU's 2026-10-28 written reply already says "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages." (E6 line 29). Whether that line stands alone or sits under the Tradovate-API sentence is Amear's to read (S8; 2026-10-28 adversarial-final report lines 84-85). The new ticket acknowledges only the two answers the brief names. Ticket question 1 asks about "this exact setup", which is what F4 needs. Adding the October line to the acknowledgement is the master's or Amear's choice.
3. Ticket question 3 ("or can I notify support instead?") touches the inactivity article's Vacations note (E7 fetch-32 line 98). That note covers vacations. It does not say whether it covers a running strategy that simply had no signal, so the question stays.
4. The inactivity article covers accounts "purchased under the one-time payment model" (on or after 2026-08-25). Which model Amear's accounts use is UNVERIFIED.
5. The R6 design and its MFFU captures exist only on branch `r6/announcement-research` (`bf6fcc7`), not on main. C3.2 cites them by commit.

## Files written
- `docs/reports/2026-11-11-mffu-investigation-correction-1-worker3.md` (this report; not staged)
- `/tmp/mffu-corr/w3.md` (the correction text)
- Fetch dirs: `/tmp/mffu-fetch-31`, `/tmp/mffu-fetch-32`, `/tmp/mffu-fetch-33`, `/tmp/mffu-fetch-34`

## Result: PASS
w3.md has C3.1, C3.2 and C3.3. Every reason and every grade cites a line pasted above. The ticket asks the five required questions, uses 4:10 PM ET, has no name or personal detail and signs off "Thank you." Caveat: the ticket is 269 words (261 without the Subject line), over the ~250 aim. F4 stays FROZEN.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
