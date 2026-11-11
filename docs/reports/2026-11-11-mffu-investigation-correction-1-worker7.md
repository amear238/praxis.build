# Correction 1, worker 7: fixes for worker 6 findings

## Task
BUILD (fix), unit `2026-11-11-mffu-investigation-correction-1`, worker 7, HEAD 85a803f. I fixed seven listed defects inside `## Correction 1` of `docs/reports/2026-11-11-mffu-connection-investigation.md` and made one redaction in `docs/reports/2026-11-11-mffu-investigation-correction-1-worker6.md` (line 162). Lines 1-283 of the artifact were not changed (hashes below). I made no git index change: the staged set still has 1 path, the pre-existing png. Nothing under `.claude/` was written. The broker route, Q4 and "I will use" were not touched. No claim about rubric F4 status was added.

## Defects fixed
1. **Finding 1 (MAJOR), Q5.** I replaced Q5 with worker 6's text (flat T−5 to T+3; asks whether "prohibited" on Rapid/Pro means more than the window, and whether Builder Sim Funded is restricted). I checked T+3 first against design :22 and :66 (pasted). C3.1 row 5 now reads "uses the T+3 re-entry from the R6 design (:22)". I added "R4 source lines" (`news.txt:27-35`, `:50`, plus design :22 and :66) as a text block below the C3.2 table, followed by a short note on what the page leaves open.
2. **Finding 2 (MAJOR), Q3.** I replaced Q3 with worker 6's text (the vacation-notification line; the strategy can go more than 7 days without a signal). Row R3 now cites `consistency.txt:50`, quoted, with the open point graded UNVERIFIED. "R3 source lines" (`consistency.txt:44-50`) are pasted below the table.
3. **Finding 4.** The ticket's correction paragraph now reads `your article "NinjaTrader: Login Instructions" (help article 10082979, account type "Simulation")`.
4. **Finding 5, C2.3.** I made two read-only fetches (71, 72), each into a new, empty dir, and pasted URL, UTC time, code, bytes, counts, titles and article links above the fee line. The fee line now uses the NOT FOUND wording from the brief. One deviation from worker 6's note: the search page lists 10 article links, not only the login article. This is recorded in C2.3. One result is titled "Does MyFundedFutures Charge Activation Fees". I did not open it (fetch limit), so the grade stays NOT FOUND, not ruled out.
5. **Finding 6, privacy.** In the C1.3 grep paste, I replaced handoff output lines :65, :66 and :68 with `[3 lines of handoff output (:65, :66, :68, VM network details unrelated to MFFU) omitted from this paste]`, and appended `| grep -v -E '^(65|66|68):'` to the pasted command. Privacy grep on the artifact: 0.
6. **Findings 7 and 8, provenance.** I added a "**Provenance caveats.**" paragraph right after "**Line numbers.**". It says the handoff is untracked as of 85a803f, and that bf6fcc7 is only on `r6/announcement-research` and should be read with `git show bf6fcc7:<path>`. It also includes the line-135 and S13 sentences from the brief, with the `git ls-files --error-unmatch` and `git branch -a --contains bf6fcc7` output pasted.
7. **Worker 6 report, line 162.** The three literal values are now `'[VM MAC]' '[tailnet IP]' '[VM LAN IP]'`, and ` (values redacted by worker 7)` is appended to that line. This is the only diff hunk in that file. Privacy grep: 0.

## Verification evidence (command output)

Source checks (bf6fcc7, read with git show):
```text
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | nl -ba | sed -n '22p;66p'
    22	- (i) Flat from T−5 min to T+3 min around every T1 release, on every account and stage.
    66	- For every T1 release at time T on day E (CPI/NFP 08:30, FOMC statement or FOMC Minutes 14:00): exit at the close of the bar stamped T−5; re-enter long at the close of the bar stamped T+3 (fills at T−4 and T+4, outside T±2).
$ git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-news.txt | nl -ba | sed -n '27,35p;50p'
    27	No positions or orders (including limit orders) can be open 2 minutes before and after the release.
    28	All positions must be flattened at least two minutes prior to the scheduled ⁠T1 News event. For example, if news is at 8:30, positions must be closed by 8:28:00 or earlier, and may only be reopened after 8:32:00
    29	​
    30	Restricted Accounts: Trading on T1 News events is prohibited for the following:
    31	Rapid Sim Funded
    32	Pro Sim Funded
    33	Unrestricted Accounts: Trading on T1 News events is permitted for the following:
    34	All evaluations
    35	Builder Plans
    50	The above are the T1 news events to be avoided on all news-restricted accounts. See above for detailed list.
$ git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt | nl -ba | sed -n '44,50p'
    44	Inactivity Rule Changes (Effective August 25th)
    45	New accounts purchased under the one-time payment model are subject to a new inactivity policy:
    46	If a trader does not place a trade for 7 consecutive calendar days, the account could be closed. This includes simulated funded accounts.
    47	An inactivity breach on a Sim Funded account results in the forfeiture of all profits.
    48	Because there is no monthly billing to pause or cancel under this new payment model, staying active within this 7-day window is required to keep a one-time payment evaluation account in good standing.
    49	Vacations
    50	Traders taking a vacation should notify the customer support team if they will not be trading for more than 7 days.
$ git ls-files --error-unmatch docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md; echo "exit=$?"
error: pathspec 'docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md' did not match any file(s) known to git
Did you forget to 'git add'?
exit=1
$ git branch -a --contains bf6fcc7
+ r6/announcement-research
  remotes/origin/r6/announcement-research
```

Fetches (untrusted HTML, only searched):
```text
$ mkdir /tmp/mffu-fetch-71 && ... curl ... https://help.myfundedfutures.com/en/articles/10082979-ninjatrader-login-instructions
2026-11-11T18:01:20Z
200 119655
0
<title data-next-head="">NinjaTrader: Login Instructions | My Funded Futures Help Center</title>
$ mkdir /tmp/mffu-fetch-72 && ... curl ... 'https://help.myfundedfutures.com/en/?q=ninjatrader+fee'
2026-11-11T18:01:22Z
200 86605
9
<title data-next-head="">Search results: ninjatrader fee | My Funded Futures Help Center</title>
(10 article hrefs; full list pasted in the artifact's C2.3)
```

Final checks:
```text
hash before: a472333e4fed937e2af170ff4e3a78601a08536082de14a7a3794240274877e6
hash after:  a472333e4fed937e2af170ff4e3a78601a08536082de14a7a3794240274877e6  -
S13 count (grep -c -F on the artifact): 2
  at lines: 136, 1453   (136 = original line 135 + banner; 1453 = last line)
$ tail -1 <artifact> | cmp - <(tail -1 <this report>) && echo ...
artifact last line == worker7 report last line (byte-identical)
diff vs /tmp/mffu-orig.md:
1a2
61c62
105,106c106,107
282a284,1453
diff vs pre-worker7 snapshot (hunk headers; all at line >= 291, inside Correction 1):
291a292,304
457c470
464,466c477
1094c1105,1112
1095a1114,1136
1329c1370
1339c1380
1345a1387,1418
1346a1420,1421
1360c1435
1368c1443
1370c1445
privacy artifact: 0
privacy worker6: 0
worker6 diff hunks:
162c162
N length: 4
rep artifact: 0
rep worker6: 0
ticket lines 1427-1449
ticket words:      331
staged paths (git diff --cached --name-only | wc -l): 1
```

The new ticket block, as printed by `sed -n '1427,1449p'`, is in the artifact's C3.3 and is not repeated here. The reprinted Q3, Q5 and correction paragraph match the Defects-fixed text above. Rep-name count for this report is in the return message (it is taken after this file is written).

## Result
PASS. All 7 defects fixed. Lines 1-283 hash equal. Privacy counts are 0 and 0. Ticket is 331 words. Fee line is NOT FOUND, with one recorded deviation: the search page lists 10 links, not 1.

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
