# F4 — MFFU "Davi" reply addendum — worker 3 report

## Task
Append an addendum titled `## Addendum 2026-10-28 — MFFU "Davi" reply (screenshot)`, with sections A–F, to
`docs/reports/2026-08-07-f4-mffu-compliance-evidence.md`. The file is append-only history.

## Mode
BUILD. No `git add` or commit, as the brief instructs. Nothing written under `.claude/`. No URL fetched. Email not touched.
`specs/SPEC_RUBRIC.md`, `DECISION_LOG.md` and the ledgers were read only.

## Criterion
F4 (`specs/SPEC_RUBRIC.md`, read only): "Written confirmation from MFFU that this specific automation pattern is
permitted on a funded account." Owner: Amear. Authorising row: `DECISION_LOG.md` `2026-10-28T20:54:29Z`, `WHO: amear`.
The addendum files the evidence only. It does not discharge F4, and F4 stays FROZEN.

## Process log
1. Read the transcript, the image copy (viewed; it matches the transcript fence line for line), the target's §0, §1, §1.1, §3.2, §3.5 and §8–9, rubric F4 and the authorising row.
2. Pre-append: the target had 537 lines and ended in `0a`. Its sha256 matched the brief (`ffda2e09…84cb1`). Its index state was `A` (staged).
3. Hashed and listed the source and the copy. `xxd` confirms bytes `e2 80 af` (U+202F) before `PM.png` in the source filename.
4. Extracted the fence to the scratchpad file `w3fence.txt` (25 lines). Ran `/usr/bin/grep -ci` for the 9 patterns. Results: 0 lines for NinjaTrader, NT8, Ninja, Rithmic, webhook, n8n and TradingView; 2 lines for Tradovate; 2 lines for API.
   - Positive control on `CLAUDE.md`: 6 of the 7 zero-hit patterns fire. `NT8` has 0 lines in `CLAUDE.md` as well, so I added `STATUS.md` as the NT8 control (40 lines). This goes beyond the brief and is disclosed in the addendum.
5. Built the addendum from heredoc pieces plus the captured command output (provenance, script, search output), so every pasted output block is real output.
6. Quote check: every `> ` quote line is an exact fence line (`grep -Fx`). The two partial-line quotes and the inline table quotes are exact fence substrings (`grep -F`, 1 hit each).
7. Forbidden-word scan (`TBD|effectively|confirms|satisf|cleared|discharg|closer`): the only hits are the required negations in §F ("NOT discharged", "NOT satisfied").
8. Appended with `cat >>`, then ran the checks below.

Mapping verdicts given:
- "this specific automation pattern" / §3.5: DOES NOT ADDRESS.
- "on a funded account": PARTLY ADDRESSES (it names funded accounts, but tied to Tradovate).
- §3.2 effective date: DOES NOT ADDRESS.
- §3.2 retroactivity / "on this account": DOES NOT ADDRESS.

Second finding, reported and not acted on: none.

## Verification evidence

```text
$ head -n 537 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | shasum -a 256
ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1  -
$ wc -l docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
     759 docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
$ git diff --stat -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
 .../2026-08-07-f4-mffu-compliance-evidence.md      | 222 +++++++++++++++++++++
 1 file changed, 222 insertions(+)
$ git diff -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md | /usr/bin/grep -c "^-"
1
$ git status --short -- docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
AM docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
```

The `head -n 537` hash equals the brief's pre-append hash `ffda2e095083802c59c951ed72da79bb978acb7cdd38e6437578b09b42c84cb1`, so no existing byte changed.
The status `AM` means the index holds the prior 537-line version and the worktree holds 759 lines. The append is unstaged, per the brief's "do not git add".

Full `git diff -- <target>` (worktree vs index). The only `-` line is the `--- a/` header:

`````diff
diff --git a/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md b/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
index e8d9e72..42ed196 100644
--- a/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
+++ b/docs/reports/2026-08-07-f4-mffu-compliance-evidence.md
@@ -535,3 +535,225 @@ FROZEN in `specs/SPEC_RUBRIC.md`, which was not touched. Whether a general
 permission for "algo trading," relayed and unread by any agent, satisfies a
 criterion written as "*this specific* automation pattern," is Amear's ruling and
 nobody else's.
+
+---
+
+## Addendum 2026-10-28 — MFFU "Davi" reply (screenshot)
+
+**Date.** 2026-10-28. **Authorisation of record.** `DECISION_LOG.md` row
+`2026-10-28T20:54:29Z`, `WHO: amear`. **Written by.** praxis-worker (BUILD), as
+an append. No byte above this addendum was changed.
+
+This addendum files a second MFFU support reply. It records what that reply
+says and maps it against F4 and against §3.2 and §3.5 of this report. It does
+**not** change F4's state. F4 remains FROZEN in `specs/SPEC_RUBRIC.md`.
+
+### A. Provenance
+
+- **Source.** Amear supplied the reply as a screenshot. Source filename:
+  `/Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23<U+202F>PM.png`. The
+  character before `PM` is U+202F NARROW NO-BREAK SPACE, bytes `e2 80 af`
+  (shown by the `xxd` line below).
+- **Repo copy.** `docs/reports/evidence/2026-10-28-mffu-davi-reply.png`.
+- **Size.** 254350 bytes (source and copy).
+- **sha256.** `15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992`
+  (source and copy, identical).
+- **Transcript.** `docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md`.
+  Every quote in this addendum is taken from inside that file's `text` fence.
+
+Command output, pasted as run on 2026-10-28:
+
+```text
+$ shasum -a 256 /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* docs/reports/evidence/2026-10-28-mffu-davi-reply.png
+15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
+15af54100ba44ddfe67dda5698c4a80ba6a93f5470c5e148cd6043dc92302992  docs/reports/evidence/2026-10-28-mffu-davi-reply.png
+$ ls -l /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* docs/reports/evidence/2026-10-28-mffu-davi-reply.png
+-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 /Users/admin/Desktop/Screenshot 2026-10-28 at 4.53.23 PM.png
+-rw-r--r--@ 1 admin  staff  254350 Oct 28 16:53 docs/reports/evidence/2026-10-28-mffu-davi-reply.png
+$ printf '%s' /Users/admin/Desktop/Screenshot\ 2026-10-28\ at\ 4.53.23* | tail -c 9 | xxd
+00000000: e280 af50 4d2e 706e 67                   ...PM.png
+```
+
+**This is a screenshot relay.** No agent read this message in Gmail. No agent
+contacted MFFU. These things are **not visible** in the screenshot and are
+**UNVERIFIED**:
+
+- the date and time of either message shown;
+- the full headers (From/Reply-To/To/Cc, Message-ID, SPF/DKIM/DMARC results);
+- the subject line of the thread;
+- the thread order beyond the two messages shown, including where the "Frank"
+  reply of §1 sits relative to this one;
+- the full text of Amear's preceding message. Only its collapsed preview is
+  visible, and the preview is cut off at `is f`.
+
+The sender display name `Davi from MyFundedFutures` and the address
+`eda.daniel.david@myfundedfutures.intercom-mail.com` are recorded **as displayed
+only**. They are not header-verified.
+
+### B. What the reply states
+
+The substantive lines, verbatim from the transcript fence. **UNVERIFIED as to
+sender, date and headers** (see A). The text itself is as shown in the image.
+
+> You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution.
+> • Automated trading solutions using an API are supported, allowing you to integrate your trading bot or automated strategy via the Tradovate API. This enables your custom software to submit orders, manage positions, and retrieve market data directly from your account.
+> • Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.
+> • High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
+> • For live accounts, automated trading must comply with CME guidelines.
+>
+> You are responsible for the performance and reliability of your automated system. For more details, see: https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices
+
+**URL: UNFETCHED.** `https://help.myfundedfutures.com/en/articles/8444599-fair-play-and-prohibited-trading-practices`
+is the link's displayed text only. Its href is not visible in the screenshot. No
+agent fetched it. Its displayed text is the same string as the policy-article
+URL in §1's table, which was also never fetched.
+
+### C. Mapping against F4, §3.2 and §3.5
+
+The PRAXIS pattern (per `CLAUDE.md`): TradingView alert → webhook → n8n → JSON
+file drop → NinjaScript FileSystemWatcher → bracket order (NinjaTrader 8) →
+Rithmic → MFFU.
+
+The reply frames its permission around the **Tradovate API**: "custom Tradovate
+API access with your MyFundedFutures Tradovate evaluation and funded accounts".
+It **never mentions** NinjaTrader, Rithmic, webhooks, n8n or TradingView. The
+search below shows this.
+
+| Point | Verdict | Quoted line(s) and reason |
+|---|---|---|
+| F4 "this specific automation pattern" (and §3.5, specific vs general) | **DOES NOT ADDRESS** | The only specific pattern the reply names is the Tradovate API: "You can use custom Tradovate API access with your MyFundedFutures Tradovate evaluation and funded accounts for fully automated order execution." and "integrate your trading bot or automated strategy via the Tradovate API". PRAXIS routes orders through NinjaTrader 8 and Rithmic, and the reply names neither (0 lines, see search). The remaining line, "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages.", is a **general** permission. That is the same specific-vs-general gap §3.5 already recorded for Frank's relayed line. It is not narrowed here. |
+| F4 "on a funded account" | **PARTLY ADDRESSES** | Funded accounts are named: "your MyFundedFutures Tradovate evaluation and funded accounts" and "simulated-funded, and live account stages". The first mention is tied to **Tradovate** accounts and the Tradovate API. Whether Amear's account is a Tradovate account is not established in this addendum. Neither line names Amear's specific account. |
+| §3.2 effective date | **DOES NOT ADDRESS** | No date or effective date appears anywhere in the reply. As a plain textual fact, Davi's line "Algo trading is permitted on all plans, including evaluation, simulated-funded, and live account stages." has **no "now" and no date**, unlike Frank's relayed line in §1 ("Algo trading is now permitted at MFFU moving forward on all plans ..."). That absence does not supply an effective date. It also does not show that the "now" in Frank's line was wrong or was withdrawn. |
+| §3.2 retroactivity / "on this account" | **DOES NOT ADDRESS** | Nothing in the reply mentions when an account was opened, whether the permission applies to accounts opened before a change, or any account identifier. The second-person "your ... accounts" in "your MyFundedFutures Tradovate evaluation and funded accounts" is generic. It identifies no account, and it is conditioned on Tradovate accounts. |
+
+**Amear's truncated follow-up.** The preview of Amear's preceding message reads,
+in full as visible:
+
+> Hi Frank — thanks for confirming, that's helpful. Two follow-ups so I can be sure I'm building within the rules rather than assuming. 1. Does this specific is f
+
+The full text of his questions is **not visible**. This addendum therefore does
+not say whether the reply answers them.
+
+**Search.** The commands below extract the transcript fence and count matching
+lines for each pattern with `/usr/bin/grep -ci`. `grep -c` counts **lines**, not
+occurrences. The `-o` listing shows the individual matches: `Tradovate` and
+`API` each occur three times, across 2 lines. The same zero-hit patterns are then
+run against `CLAUDE.md` as a positive control. `NT8` has 0 lines in `CLAUDE.md`
+as well, so `STATUS.md` is used as its control.
+
+Script (`w3search.sh`, run from the repo root with `bash`):
+
+````text
+F=/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/w3fence.txt
+awk '/^```text/{f=1;next} /^```/{f=0} f' docs/reports/evidence/2026-10-28-mffu-davi-reply-transcript.md > "$F"
+wc -l < "$F"
+for p in NinjaTrader NT8 Ninja Rithmic webhook n8n TradingView Tradovate API; do printf '%s\t' "$p"; /usr/bin/grep -ci "$p" "$F"; done
+echo '--- matching lines for Tradovate|API (line:match)'
+/usr/bin/grep -nio 'tradovate\|api' "$F"
+echo '--- positive control: same zero-hit patterns against CLAUDE.md'
+for p in NinjaTrader NT8 Ninja Rithmic webhook n8n TradingView; do printf '%s\t' "$p"; /usr/bin/grep -ci "$p" CLAUDE.md; done
+echo '--- positive control for NT8 (0 in CLAUDE.md): STATUS.md'
+/usr/bin/grep -ci NT8 STATUS.md
+````
+
+Output, pasted as run (the first line is the fence's line count):
+
+````text
+      25
+NinjaTrader	0
+NT8	0
+Ninja	0
+Rithmic	0
+webhook	0
+n8n	0
+TradingView	0
+Tradovate	2
+API	2
+--- matching lines for Tradovate|API (line:match)
+13:Tradovate
+13:API
+13:Tradovate
+14:API
+14:Tradovate
+14:API
+--- positive control: same zero-hit patterns against CLAUDE.md
+NinjaTrader	2
+NT8	0
+Ninja	4
+Rithmic	3
+webhook	1
+n8n	4
+TradingView	3
+--- positive control for NT8 (0 in CLAUDE.md): STATUS.md
+40
+````
+
+All seven zero-hit patterns score 0 in the fence. Six of them fire in
+`CLAUDE.md`. The seventh, `NT8`, fires in `STATUS.md` (40 lines). So each zero
+is a true null, not a broken pattern. The case-insensitive `API` pattern could
+also match inside other words. The `-o` listing shows that every `API` hit is on
+line 13 or 14 of the fence, which are the two Tradovate API lines quoted in B.
+
+### D. New conditions the reply states (for the record only)
+
+Quoted verbatim:
+
+> • High-frequency trading is not allowed, and automated tools must not exploit favorable fills in the simulated environment.
+> • For live accounts, automated trading must comply with CME guidelines.
+
+> You are responsible for the performance and reliability of your automated system.
+
+So the reply states four conditions: no high-frequency trading; automated tools
+must not exploit favorable fills in the simulated environment; live accounts
+must comply with CME guidelines; and the trader is responsible for the system's
+performance and reliability.
+
+**PRAXIS is NOT assessed against these conditions here. That is out of scope for
+this addendum.** For the record only: §1.1 of this report recorded three similar
+restrictions from Frank's relay (no HFT; no exploiting sim-environment fill
+favorability; live automation must follow CME guidelines). No comparison of
+PRAXIS against either set is made here.
+
+### E. Anomalies
+
+1. **Name mismatch.** The body says:
+   > Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.
+
+   The sender and the signature say Davi:
+   > Davi from MyFundedFutures <eda.daniel.david@myfundedfutures.intercom-mail.com>
+
+   > Davi-MyFundedFutures Support
+2. **Two greetings.** The body opens twice:
+   > Hello amear,i hope this mail meets you well.
+
+   > Hi ! Thank you so much for reaching out to MyFundedFutures Support. My name is Michael and I am here to help you with any support you may need today.
+
+   **Inference, not observed:** the two greetings plus the "Michael" vs "Davi"
+   mismatch suggest templated or boilerplate text, put together from more than
+   one canned block. Nothing in the image shows how the reply was composed.
+3. **Different rep from §1.** The rep recorded earlier in this report is
+   "Frank" (§1, relayed, UNVERIFIED). Amear's preceding message, as previewed,
+   is addressed to Frank:
+   > Hi Frank — thanks for confirming, that's helpful.
+
+   The reply comes from "Davi", not Frank. The displayed address local part
+   (`eda.daniel.david`) also differs from the relayed Frank sender in §1
+   (`FRANK@myfundedfutures.intercom-mail.com`). Both addresses are display or
+   relay only, and neither is header-verified.
+
+### F. Not claimed
+
+- Not claimed: that F4 is discharged. F4 is **NOT discharged**, **NOT
+  satisfied** and **NOT unfrozen**. `specs/SPEC_RUBRIC.md` was not touched by
+  this addendum.
+- Not claimed: that a general permission, or a Tradovate-framed permission,
+  covers the PRAXIS NinjaTrader 8 / Rithmic path. That is **Amear's ruling**
+  (S8). He has ruled to send MFFU a follow-up naming NinjaTrader 8 + Rithmic
+  (`DECISION_LOG.md` row `2026-10-28T20:54:29Z`). That follow-up is **his to
+  send**. No agent drafted or sent it.
+- Not claimed: that PRAXIS complies with the conditions in D.
+- Not claimed: anything about the date of this reply, or its position in the
+  thread relative to Frank's reply or to Amear's messages.
+- Not claimed: that the sender name, address, or the MFFU affiliation is
+  verified. All are as displayed in a screenshot.
+- Not claimed: anything about what the help-center URL says. It was not fetched.
`````

## Files staged
None by this worker. Modified in the worktree (unstaged):
- `docs/reports/2026-08-07-f4-mffu-compliance-evidence.md` (+222 lines, append only)
- this report (untracked)

Scratch files (not in the repo) are in `/private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/e2d12a7c-ea8d-4471-9c36-a46d92b1a310/scratchpad/`: `w3fence.txt`, `w3search.sh`, `w3search.out`, `w3prov.out`, `addendum.md`.

Result: PASS
