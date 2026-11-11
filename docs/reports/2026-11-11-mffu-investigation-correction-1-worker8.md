# Worker 8 — ADVERSARIAL re-check of Correction 1 (unit 2026-11-11-mffu-investigation-correction-1)

## Task
Mode: ADVERSARIAL. Artifact: `docs/reports/2026-11-11-mffu-connection-investigation.md` (1453 lines, HEAD 85a803f). Scope: (i) the C3.3 replacement ticket, with the C3.1 table and the C3.2 table and source lines; (ii) the C2.3 fee paragraph and its last line, "Platform or routing fee ..."; (iii) the C1.3 grep paste of the return-handoff file; (iv) the "**Provenance caveats.**" paragraph. The job was to find defects, not to confirm. No network was used. Pages that other workers fetched earlier were re-read from the copies they saved under `/private/tmp/mffu-fetch-*/page.html`. Every paste was filtered through `sed "s/$N/[rep]/Ig"`.

## Criteria
- S1: every pasted command in scope is re-run and compared with its paste. A mismatch is MAJOR.
- Ticket required elements (Amear's brief). Every factual statement in the ticket must match a source: the MFFU captures at bf6fcc7, the R6 design, or the handoff (thread subject and date checked verbatim).
- Privacy grep on the artifact = 0. The "omitted" note in (iii) must be honest.
- Fee line: NOT FOUND is acceptable only if the pages read would plausibly state such a fee.
- Nothing in scope says F4 is met, closed or nearly met, and nothing makes a broker-route decision.

## Verification evidence (command output)

Privacy grep and rep-name count on the artifact:
```text
$ grep -c -i -E "$PRIV" docs/reports/2026-11-11-mffu-connection-investigation.md    # PRIV = the brief's privacy pattern, verbatim (not pasted here so this report does not match itself)
0
$ grep -c -i "$N" docs/reports/2026-11-11-mffu-connection-investigation.md
0
```

(iv) Provenance re-run:
```text
$ git ls-files --error-unmatch docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md
error: pathspec 'docs/reports/2026-11-10-return-handoff-claude-ai-voice-rulings.md' did not match any file(s) known to git
Did you forget to 'git add'?
rc=1
$ git branch -a --contains bf6fcc7
+ r6/announcement-research
  remotes/origin/r6/announcement-research
```

(iii) C1.3 re-run, compared with the paste after removing the bracketed omission note:
```text
$ grep -n -i -E '19:43|abide|evaluation phase|Rithmic|inactiv|closed' <handoff> | grep -v -E '^(65|66|68):' > /tmp/w8-c13.txt
$ diff /tmp/w8-pasted-c13.txt /tmp/w8-c13.txt && echo IDENTICAL
C1.3 IDENTICAL (      15 lines)
== unfiltered grep line numbers
16 20 26 32 51 55 65 66 68 89 93 114 120 121 123 130 135 136
== handoff lines 65,66,68: privacy-pattern hits / MFFU mentions
3
0
```
The omission note is honest. Exactly lines 65, 66 and 68 are dropped. All three carry network identifiers, and none mentions MFFU. Line 66 is about the n8n container on the Mac, not the VM. That small wording slip is not a finding.

C3.2 source-line pastes, re-run and hashed:
```text
$ { git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-consistency.txt | nl -ba | sed -n '44,50p';
    git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-news.txt | nl -ba | sed -n '27,35p;50p';
    git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | nl -ba | sed -n '22p;66p'; } | md5
adeff9a469fc6fcb479a4fe9f2dec235
$ (numbered lines pasted in the artifact between "R3 source lines" and "### C3.3") | md5
adeff9a469fc6fcb479a4fe9f2dec235
```

(ii) Fee fetches, re-read from the saved pages (no network):
```text
== 71 bytes   119655 feecount 0
== 72 bytes    86605 feecount 9
== href BRE as pasted
$ grep -o 'href="[^"]*/articles/[0-9]+-[^"]*"' mffu-fetch-72/page.html | sort -u | wc -l
       0
== href ERE
$ grep -o -E 'href="[^"]*/articles/[0-9]+-[^"]*"' mffu-fetch-72/page.html | sort -u
(10 links; same list as the artifact, lines 1120-1129)
== 43 bytes    76567 feecount 3
== 44 bytes   102298 feecount 17
== 45 bytes   120020 feecount 1
== 2 bytes   111605 feecount 1     (Overview of Supported Platforms at MFFU, saved 12:36 local)
== 3 bytes   101001 feecount 0     (Connecting to Different Platforms at MFFU, saved 12:36 local)
```
The byte counts for 43, 44, 45, 71 and 72 match the artifact. The fee-term counts for 71 (0) and 72 (9) match. The curl commands for 43-45 are pasted as `curl ...`, so they cannot be re-run as written, and network was not allowed.

Thread facts (handoff and the 2026-10-28 transcript):
```text
handoff:11  Sent 2026-11-10T19:29:01Z ... as a reply in the existing MFFU support thread (... thread `19f9edc188595b0c`; subject "Re: Re: Re: Written policy confirmation — automated execution on funded account" ...)
handoff:12  Outgoing body, verbatim ... (quoted earlier reply omitted; it is the reply already on disk):
handoff:16  Thanks for confirming that algorithmic trading is allowed on all plans. Your reply mentioned the Tradovate API ...
2026-10-28-mffu-[rep]-reply-transcript.md:27  You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts ...
2026-10-28-mffu-[rep]-reply-transcript.md:29  • Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
f4 filing:129  -rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
```

The F4 and broker-route scan of the in-scope lines, plus a check of the ticket for personal details:
```text
(only hits) handoff:130 quoted inside C1.3 "F4 stays NOT MET"; C3.1 item 4 "...which is what F4 asks for"; Line-numbers paragraph (sha256 substring)
== ticket PII-ish count (Amear|Bani|@|order number|last 4)
0
```

Required ticket elements, checked against the C3.3 text:
- Refers to the earlier thread: yes.
- Rithmic correction, native connection, article 10082979, "Simulation": yes.
- The pattern (emitter, local n8n webhook, risk checks, file, consumer placing bracket orders): yes.
- NQ only, low frequency, VM: yes.
- Plans (evaluation, Rapid, Pro, Builder Sim Funded): yes.
- Q1-Q5 cover funded permission, Simulation, 7-day rule, evening entry with the 4:10 PM close, and T-5 vs the T1 rule: yes.
- No 5:00 PM: yes.
- No name, signature or personal detail: yes.
- Does not re-ask what MFFU answered in writing: yes.
- Builder Q5: justified, because the news.txt:33-35 text conflicts with the banner on the page, as R6 design line 14 records. It is not a question the public pages fully answer.

## Findings

1. **MAJOR. Artifact line 1119 (C2.3, fetch 72): the pasted command does not produce the pasted output.**
   - The paste shows `grep -o 'href="[^"]*/articles/[0-9]+-[^"]*"' | sort -u` followed by ten article links.
   - In basic regex (BSD and GNU grep without `-E`), `+` is a literal character. Re-run on the saved page, the command gives 0 lines. The ten links appear only with `-E` (evidence above).
   - The listed links are correct, but the command as pasted is not the one that produced them.
   - Fix: change the pasted command to `grep -o -E ...`.

2. **MAJOR. Artifact lines 296-300 (Provenance caveats): the `git branch -a --contains bf6fcc7` paste is truncated without saying so.**
   - The real output has two lines: `+ r6/announcement-research` and `  remotes/origin/r6/announcement-research`. The paste shows only the first and has no omission marker.
   - The claim itself still holds: main does not contain bf6fcc7. But by the S1 rule, a mismatch is MAJOR.
   - Fix: paste both lines.

3. **MAJOR. C3.3 ticket, first paragraph: the thread is dated "(10 November 2026)", and the sources show it began earlier.**
   - Handoff:11 records the subject as "Re: Re: Re: Written policy confirmation ..." and V1 as "a reply in the existing MFFU support thread".
   - Handoff:12 says the earlier reply quoted in that thread is "the reply already on disk". That is the 2026-10-28 reply: its transcript lines 27-29 carry the "Tradovate API" and "all plans" wording that V1 (handoff:16) thanks MFFU for. Its screenshot is dated Oct 28.
   - So the thread existed by 2026-10-28. 10 November is only the date of Amear's last two emails in it. No source dates the thread to 10 November.
   - The subject is quoted with the "Re: Re: Re:" prefix removed. That is an acceptable base subject, and not a finding on its own.
   - Fix: write "(my latest emails in it were on 10 November 2026)", or drop the date.

4. **MINOR. C2.3 artifact line 1133: "The linked articles were not opened (fetch limit)" understates what the session read.**
   - "Overview of Supported Platforms at MFFU" (8528335) and "Connecting to Different Platforms at MFFU" (8528337) are two of the ten links. Both were fetched in this unit: `/private/tmp/mffu-fetch-2` and `-3`, saved 12:36 local, about 17:36Z.
   - Their fee-term counts are 1 and 0. The single hit is product copy, not a fee.
   - The NOT FOUND grade on line 1135 is still honest. The pages read include the MFFU NinjaTrader article, the page most likely to state such a fee. The fee line can be made stronger.
   - Fix: cite fetches 2 and 3, and drop "not opened" for those two.

5. **MINOR. C3.3 Q5, "flat from 5 minutes before each Tier 1 release until 3 minutes after it": this matches R6 design line 22, but not design line 66.**
   - Line 66 is the paste the worker added: "exit at the close of the bar stamped T−5; re-enter ... (fills at T−4 and T+4)".
   - Simulated fills put the position flat from T−4 to T+4. That still clears T±2, so the answer MFFU gives is not affected.
   - Fix (optional): "exits 5 minutes before each Tier 1 release and re-enters 3 minutes after it".

6. **MINOR. C3.3 setup paragraph, "a local n8n webhook on the same computer": there is no source for this, and it is looser than the observed layout.**
   - C3.2 R9 cites handoff:64/66: NT8 runs in a VM, and n8n runs in a container on the Mac host. Handoff:66 records that the VM-to-webhook path fails as configured today (INFERRED there).
   - "Same computer" is true of the physical host. Amear's brief says "local n8n webhook", not "same computer".
   - Fix (optional): "a local n8n webhook on my own machine".

7. **MINOR. C3.3 Q5 quote: the ticket quotes MFFU as "trading on T1 news events is prohibited".** The capture (news.txt:30) reads "Trading on T1 News events is prohibited". The case of "News" differs inside quotation marks. This is cosmetic.

**No defect found in:**
- C1.3: the paste re-runs identically, and the omission note is honest.
- The C3.2 source pastes: their md5 matches the re-run.
- The C3.1 table.
- The privacy grep (0) and the rep-name count (0).
- F4 and broker-route wording: no in-scope line says F4 is met, closed or nearly met. "I will use" is out of scope by the brief.
- Ticket required elements: all present.
- Q3's quote of the vacation line: it matches consistency.txt:50, and the page title "Inactivity Rule - One-Time Payment Model" supports "Inactivity Rule article".

Not re-runnable: the `curl ...` commands for fetches 43-45, 71 and 72 (elided in the artifact, and network was not allowed). Their saved pages were re-read instead.

## Result
FAIL (3 MAJOR: findings 1, 2, 3; 0 BLOCKER; 4 MINOR).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
