# MFFU support thread, as pasted by Amear in the master session, 2026-11-15

Captured by praxis-master at 2026-11-15T16:16:42Z (`date -u`), from text Amear pasted into the Claude Code master session. Authority: DECISION_LOG row 2026-11-15T16:16:42Z (WHO: amear).
NOT AUDITED. NOT COMMITTED. This file is not F4's graded artifact until a praxis-auditor has graded it (SPEC_RUBRIC.md F4).

Redactions (the master's, under the standing rule that no repo file prints an email address or an MFFU staff name):
- Amear's email address, 2 places, replaced with `[Amear's address withheld]`.
- MFFU staff first names, 2 different people, 3 places, replaced with `[MFFU rep A]` (named in Amear's Nov 13 greeting, the one who answered on Nov 12) and `[MFFU rep B]` (the one who replied on Nov 13).
- The message bodies are otherwise copied as pasted. Blank lines collapsed to one. A stray line reading "11" between the two messages was in the paste and is kept.

Gaps, as observed in the paste:
- The Nov 12 replies from `[MFFU rep A]` are NOT in the paste. The Nov 13 "Yes." answers a question that refers to "your answer 1" and "your answer 2" of Nov 12. Without the Nov 12 text, the rule that "Yes." is conditioned on is unknown here.
- The paste shows no reply to questions 2-5 of the Nov 11 message, except through the Nov 12 answers that are missing.

---

amear Bani-Ahmad [Amear's address withheld]
Wed, Nov 11, 5:37 PM (4 days ago)
to support

Hello,

I don't have an account yet. I'm asking before I buy an evaluation.

An earlier email thread with your team ("Written policy confirmation — automated execution on funded account") was closed before my last question was answered, so I'm opening a new one.

Correction to that thread: I said my setup used Rithmic, which you do not offer. I will use the NinjaTrader connection described in your article "NinjaTrader: Login Instructions" (help article 10082979, account type "Simulation").

My setup: a NinjaTrader strategy sends each signal to a local n8n webhook on the same computer. n8n runs my risk checks (daily loss limit, max trades per session, session time limits) and, if they pass, writes a file. A second NinjaTrader strategy reads the file and places a bracket order (entry, stop-loss, profit target). NQ only, low frequency, my own account only, running on my own computer in a virtual machine. No copy trading, no third-party signals.

Questions (for the evaluation, and for Rapid, Pro and Builder Sim Funded):

1. Is this exact automated setup permitted on funded accounts, not just the evaluation?

2. Do funded accounts also use account type "Simulation" on the NinjaTrader connection?

3. Your Inactivity Rule article says traders on vacation should notify support if they will not trade for more than 7 days. My strategy can go more than 7 days without a signal. Can I notify support in that case too, or must the account place a trade at least every 7 days?

4. Does a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day count as holding overnight? It is never held past your 4:10 PM ET close.

5. My strategy is flat from 5 minutes before each Tier 1 news release until 3 minutes after it. On Rapid and Pro Sim Funded, does "trading on T1 news events is prohibited" mean anything more than that window, for example no trading at all that day? And are Builder Sim Funded accounts restricted or unrestricted for T1 news?

Please reply in writing so I have a record before I buy.

Thank you,
Amear Bani-Ahmad
11

amear Bani-Ahmad [Amear's address withheld]
Fri, Nov 13, 12:26 PM (2 days ago)
to support

Hi [MFFU rep A],

Thank you for your answers on Nov 12. The ticket closed before I could reply, so I'm reopening it with two short follow-ups. A written yes or no on each is all I need.

1. To confirm I've read your answer 2 correctly: may my automated strategy run unattended, with no one at the screen, on Evaluation and Sim Funded accounts (Rapid, Pro and Builder), as long as it follows the rule in your answer 1?

2. Your news trading policy lists "Builder Plans" under accounts where T1 news trading is permitted. Does that include Builder Sim Funded accounts, or only the Builder evaluation?

Thank you,
Amear Bani-Ahmad

[MFFU rep B] from MyFundedFutures
Fri, Nov 13, 12:36 PM (2 days ago)
to me

Hello amear. 👋 Thanks for reaching out to MyFundedFutures Support! My name is [MFFU rep B].

Kindly find the answers to your queries below.

Yes.
T1 news trading is allowed in the Builder plans in evaluation and Sim funded as well.
If you need any additional assistance or have more questions, don't hesitate to reach out via email or submit a ticket through our website. We're here to help!

Best regards,

MyFundedFutures Support

---

## Addendum 1 — second paste, captured 2026-11-15T17:47:54Z (`date -u`)

Captured by praxis-master from text Amear pasted into the Claude Code master session, in reply to the master's request for the Nov 12 answers. Authority: DECISION_LOG row 2026-11-15T17:47:54Z. NOT AUDITED. NOT COMMITTED. Nothing above this addendum was changed.

Redactions: the MFFU responder's name, 2 places (sender line and nothing else; the body signs with no name), replaced with `[MFFU responder C]`. No email address was in the paste. Body otherwise copied as pasted; blank lines collapsed to one.

Observations by the master (facts about the paste, not a reading of the policy):
- The header date is Wed, Nov 11, 5:38 PM, one minute after Amear's Nov 11 message at 5:37 PM (:18 above). It is not dated Nov 12.
- The sender name is not the name Amear's Nov 13 greeting uses for the Nov 12 answerer (`[MFFU rep A]`, :53 above). It is a third name.
- Its item 2 is about the NinjaTrader connection type. Amear's Nov 13 message (:57 above) refers to "your answer 2" as covering unattended running. The numbering does not match, so it is UNVERIFIED that this message is the "answer 1" and "answer 2" the Nov 13 "Yes." refers to.
- The gap at :12 above therefore stays open: a Nov 12 reply from `[MFFU rep A]` has not been pasted.

[MFFU responder C] from MyFundedFutures
Wed, Nov 11, 5:38 PM (4 days ago)
to me

Hi Amear,

Thank you for your detailed questions. I'll address each one based on our current policy.

1. Automated setup on funded accounts

Automated strategies are permitted on evaluation and funded accounts, subject to Fair Play rules: strategies must be tailored to your own settings, must not exploit favorable simulated fills, and high-frequency trading is prohibited. Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you've provided.

2. NinjaTrader connection type on funded accounts

I cannot confirm from available information whether funded accounts use the same "Simulation" connection type as evaluation accounts. This technical detail requires verification with our team.

3. Inactivity notification for low-frequency strategies

The 14-day recommended completion window for KYC is separate from the inactivity policy. Our inactivity rule applies after 7 consecutive calendar days without a trade. If your strategy may go longer than 7 days without a signal, contacting support to explain the situation is advisable, though I cannot guarantee an exemption or confirm that notification alone prevents closure.

4. Overnight positions

I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close.

5. T1 news restrictions

On Rapid Sim Funded and Pro Sim Funded, no positions or orders may remain open within the two-minute window before and after Tier 1 releases. Your strategy's 5-minute pre-release to 3-minute post-release flat window covers this requirement. The restriction does not prohibit trading at other times that day.

Builder Sim Funded accounts are unrestricted for T1 news trading, subject to Fair Play rules.

All evaluations, including Rapid and Pro evaluations, permit T1 news trading with Fair Play restrictions—the two-minute window does not apply at the evaluation stage.

Please let me know if this helps or if you have any further questions.

---

## Addendum 2 — full thread, fourth paste, captured 2026-11-15T17:52:40Z (`date -u`)

Captured by praxis-master from text Amear pasted into the Claude Code master session after the master asked whether a Nov 12 reply exists. Authority: DECISION_LOG row 2026-11-15T17:51:44Z. NOT AUDITED. NOT COMMITTED. Nothing above this addendum was changed.

This paste is the whole thread from Nov 11 to Nov 13, 15 messages, in the order pasted. It repeats messages already captured above (Amear's Nov 11 5:37 PM, the Nov 11 5:38 PM reply, and the Nov 13 pair). They are copied again here so that the thread reads in one piece.

Redactions (the master's, under the standing rule that no repo file prints an email address, a phone number or an MFFU staff name):
- Amear's email address, 6 places, replaced with `[Amear's address withheld]`.
- Placeholder counts in the message bodies below (from the line after the correction note to the end): address 6, phone 1, `[MFFU rep A]` 3, `[MFFU rep B]` 2, `[MFFU responder C]` 9, `[MFFU rep D]` 1.
- Amear's phone number, 1 place, replaced with `[Amear's phone number withheld]`.
- MFFU names, four different senders, replaced as follows. `[MFFU rep A]`: the person who answered on Nov 12 at 12:13 PM (same name as the greeting at :53 above). `[MFFU rep B]`: the person who replied on Nov 13 (same as :64 above). `[MFFU responder C]`: the sender of the six Nov 11 replies and the Nov 12 12:02 PM handoff line; each of its Nov 11 replies is footed "This answer was composed by [MFFU responder C], MyFundedFutures's AI Agent." `[MFFU rep D]`: the sender of the Nov 12 8:09 PM ticket-closure message.
- MFFU help-centre URLs are kept, since they are public pages.
- The message bodies are otherwise copied as pasted. Runs of blank lines are collapsed to one. The "intercom" line under each MFFU message was in the paste and is kept. An invisible character at the start of the second line of the closure message is not reproduced.

Correction to Addendum 1 (append-only; Addendum 1 is not edited): Addendum 1 recorded that it was UNVERIFIED whether the Nov 11 5:38 PM reply is the "answer 1" and "answer 2" that the Nov 13 "Yes." refers to, and that the gap at :12 stayed open. This paste shows the Nov 12 reply from `[MFFU rep A]` (12:13 PM, below). It has no numbers; its first paragraph and its second line are the two statements nearest to "answer 1" and "answer 2". Which statements Amear's Nov 13 message means by those labels is his reading, and it is not recorded here as settled. The gap at :12 is closed in the sense that the Nov 12 text is now on file.

amear Bani-Ahmad [Amear's address withheld]
Wed, Nov 11, 5:37 PM (4 days ago)
to support

Hello,

I don't have an account yet. I'm asking before I buy an evaluation.

An earlier email thread with your team ("Written policy confirmation — automated execution on funded account") was closed before my last question was answered, so I'm opening a new one.

Correction to that thread: I said my setup used Rithmic, which you do not offer. I will use the NinjaTrader connection described in your article "NinjaTrader: Login Instructions" (help article 10082979, account type "Simulation").

My setup: a NinjaTrader strategy sends each signal to a local n8n webhook on the same computer. n8n runs my risk checks (daily loss limit, max trades per session, session time limits) and, if they pass, writes a file. A second NinjaTrader strategy reads the file and places a bracket order (entry, stop-loss, profit target). NQ only, low frequency, my own account only, running on my own computer in a virtual machine. No copy trading, no third-party signals.

Questions (for the evaluation, and for Rapid, Pro and Builder Sim Funded):

1. Is this exact automated setup permitted on funded accounts, not just the evaluation?

2. Do funded accounts also use account type "Simulation" on the NinjaTrader connection?

3. Your Inactivity Rule article says traders on vacation should notify support if they will not trade for more than 7 days. My strategy can go more than 7 days without a signal. Can I notify support in that case too, or must the account place a trade at least every 7 days?

4. Does a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day count as holding overnight? It is never held past your 4:10 PM ET close.

5. My strategy is flat from 5 minutes before each Tier 1 news release until 3 minutes after it. On Rapid and Pro Sim Funded, does "trading on T1 news events is prohibited" mean anything more than that window, for example no trading at all that day? And are Builder Sim Funded accounts restricted or unrestricted for T1 news?

Please reply in writing so I have a record before I buy.

Thank you,
Amear Bani-Ahmad

[MFFU responder C] from MyFundedFutures
Wed, Nov 11, 5:38 PM (4 days ago)
to me

Hi Amear,

Thank you for your detailed questions. I'll address each one based on our current policy.

1. Automated setup on funded accounts

Automated strategies are permitted on evaluation and funded accounts, subject to Fair Play rules: strategies must be tailored to your own settings, must not exploit favorable simulated fills, and high-frequency trading is prohibited. Your described setup—NinjaTrader sending signals to n8n for risk checks, then placing bracket orders—falls within general automation permission. However, I cannot issue written approval for your specific configuration or guarantee that unattended execution is allowed without supervision. For an official compliance decision on your exact setup, our team can review the details you've provided.

2. NinjaTrader connection type on funded accounts

I cannot confirm from available information whether funded accounts use the same "Simulation" connection type as evaluation accounts. This technical detail requires verification with our team.

3. Inactivity notification for low-frequency strategies

The 14-day recommended completion window for KYC is separate from the inactivity policy. Our inactivity rule applies after 7 consecutive calendar days without a trade. If your strategy may go longer than 7 days without a signal, contacting support to explain the situation is advisable, though I cannot guarantee an exemption or confirm that notification alone prevents closure.

4. Overnight positions

I cannot confirm the exact definition of "overnight" for a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day. This requires clarification from our team, as the policy distinguishes between holding within a session versus holding through the daily close.

5. T1 news restrictions

On Rapid Sim Funded and Pro Sim Funded, no positions or orders may remain open within the two-minute window before and after Tier 1 releases. Your strategy's 5-minute pre-release to 3-minute post-release flat window covers this requirement. The restriction does not prohibit trading at other times that day.

Builder Sim Funded accounts are unrestricted for T1 news trading, subject to Fair Play rules.

All evaluations, including Rapid and Pro evaluations, permit T1 news trading with Fair Play restrictions—the two-minute window does not apply at the evaluation stage.

Please let me know if this helps or if you have any further questions.

This answer was composed by [MFFU responder C], MyFundedFutures's AI Agent.
intercom

amear Bani-Ahmad [Amear's address withheld]
Wed, Nov 11, 5:40 PM (4 days ago)
to support

Hi,

Thank you, that answers the news question clearly.

Yes, please have your team review my exact setup and give me a written decision. I'd like a written answer to these four points before I buy:

1. Is this exact setup permitted on funded accounts (Rapid, Pro and Builder Sim Funded): a NinjaTrader strategy sends signals to a local n8n webhook, n8n runs my risk checks and writes a file, and a second NinjaTrader strategy reads the file and places a bracket order. NQ only, low frequency, my own account, my own computer.

2. Is automated trading allowed while I am not actively watching the screen (the strategy runs unattended during the session, with its own risk limits)?

3. Do funded accounts use account type "Simulation" on the NinjaTrader connection, as in your article "NinjaTrader: Login Instructions"?

4. Does a position opened after 6:00 PM ET and closed before 9:30 AM ET the next day count as holding overnight? It is never held past your 4:10 PM ET close.

Thank you,
Amear Bani-Ahmad

[MFFU responder C] from MyFundedFutures
Wed, Nov 11, 5:41 PM (4 days ago)
to me

Hi Amear,

Thank you for the detailed description of your setup. I can explain the confirmed rules for each point below.

1. Automated strategy setup (Rapid, Pro and Builder Sim Funded)

Automated strategies are permitted on MFFU accounts, including Evaluation, Sim Funded and Live, provided they follow the applicable rules. High‑frequency trading is prohibited, and strategies must not attempt to exploit favorable simulated fills. However, a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information. Automation is allowed in principle, but individual setups are not automatically approved.

2. Running the strategy unattended during the session

Automation is permitted, but the policy does not confirm whether unattended execution without supervision is allowed or required. The absence of a supervision rule does not establish permission for a specific unattended configuration.

3. NinjaTrader connection account type

When connecting NinjaTrader to your MFFU account, the connection should be configured with the account type set to Simulation in the NinjaTrader connection properties. [1]

4. Holding a position from 6:00 PM to before 9:30 AM the next day

MFFU trading hours run from 6:00 PM to 4:10 PM Eastern Time. Positions must be closed by the 4:10 PM cutoff. A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close. [2]

Please let me know if this helps or if you have any further questions.

This answer was composed by [MFFU responder C], MyFundedFutures's AI Agent.
intercom

amear Bani-Ahmad [Amear's address withheld]
Wed, Nov 11, 7:43 PM (4 days ago)
to support

Hi,

Thank you. Your answers settle everything except one point, and I'd like a member of your team to answer it in writing before I buy:

Is a trader required to be present or supervising while an automated strategy runs on an Evaluation or Sim Funded account?

Your Fair Play article (Section 1: Automated Trading Protocols) has no supervision requirement, and your reply said the policy does not confirm it either way. A simple yes or no is all I need: if yes, please point me to where the rule is written.

Thank you,
Amear Bani-Ahmad

[MFFU responder C] from MyFundedFutures
Wed, Nov 11, 7:44 PM (4 days ago)
to me

Hi Amear,

No. The current policy does not require a trader to be present or supervising while an automated strategy runs on Evaluation or Sim Funded accounts.

Automated strategies are permitted, but the approved rules do not establish any supervision requirement or an exemption for unattended execution. The policy simply allows qualifying automated strategies while prohibiting practices such as high‑frequency trading and exploiting simulated fills.

Because the policy is silent on supervision, it cannot be confirmed that unattended operation is either required or officially permitted.

Please let me know if this helps or if you have any further questions. If you'd prefer to speak with a team member, just let me know and I'll connect you right away.

This answer was composed by [MFFU responder C], MyFundedFutures's AI Agent.
intercom

amear Bani-Ahmad [Amear's address withheld]
Wed, Nov 11, 7:49 PM (4 days ago)
to support

Hi,

Yes, please connect me with a team member.

One question for them: may an automated strategy that follows your rules run unattended (no one at the screen) on Evaluation and Sim Funded accounts? Your reply says the policy has no supervision requirement but cannot confirm unattended operation is officially permitted. I'd like a team member's written yes or no.

Thank you,
Amear Bani-Ahmad

[MFFU responder C] from MyFundedFutures
Wed, Nov 11, 7:50 PM (4 days ago)
to me

Hi Amear,

Automated trading is permitted on Evaluation and Sim Funded accounts, provided the strategy follows our Fair Play rules, including the prohibition on high-frequency trading and exploiting simulated fills.

However, unattended operation without a trader supervising is not explicitly confirmed as permitted or prohibited. General automation permission does not establish a supervision requirement or exemption.

Your request for a team member's written yes-or-no decision requires policy review. I cannot issue that approval or initiate the handoff directly from here.

Please let me know if you have any further questions. If you'd prefer to speak with a team member, just let me know and I'll connect you right away.

This answer was composed by [MFFU responder C], MyFundedFutures's AI Agent.
intercom

amear Bani-Ahmad [Amear's address withheld]
Thu, Nov 12, 12:01 PM (3 days ago)
to support

Hi,

Can I please speak to a real person on your team? Judging by how quickly the replies in this thread arrive (within about a minute each time), I assume I've been talking to an AI agent.

The answers I've received so far also contradict each other:

1. Account type: the first reply said it could not confirm whether funded accounts use the "Simulation" account type on the NinjaTrader connection. Two minutes later, the next reply said the connection should be set to "Simulation".

2. Evening entries: the first reply said it could not confirm whether a position opened after 6:00 PM ET and closed before 9:30 AM ET counts as holding overnight. The next reply said it stays within the permitted trading window and does not cross the daily close.

3. Speaking to a team member: the last reply said my request "requires policy review" and that it "cannot initiate the handoff", then in the same message offered to connect me to a team member "right away".

What I need is written confirmation from a person on your team that I can operate under these conditions:

- An automated strategy on NinjaTrader (native NinjaTrader connection), following your Fair Play rules: NQ only, low frequency, no high-frequency trading, my own account only.
- The strategy runs unattended, with no one at the screen, on Evaluation and Sim Funded accounts (Rapid, Pro and Builder).
- Positions may be opened after 6:00 PM ET and closed before 9:30 AM ET the next day, never held past your 4:10 PM ET close.
- The strategy is flat from 5 minutes before to 3 minutes after every Tier 1 news release.

If it's easier to discuss this by phone, you can reach me at [Amear's phone number withheld]. I'd still need the confirmation in writing afterwards.

Thank you,
Amear Bani-Ahmad

[MFFU responder C] from MyFundedFutures
Thu, Nov 12, 12:02 PM (3 days ago)
to me

I've passed your email and the conversation so far to our support team for review. Please reply to this same email thread if you have anything else to add. You don't need to start a new conversation.

intercom

[MFFU rep A] from MyFundedFutures
Thu, Nov 12, 12:13 PM (3 days ago)
to me

Hello amear, Thank you for contacting MyFundedFutures Support! My name is [MFFU rep A]. I will be happy to assist you today.

Traders may make use of automated trading strategies tailored to their own specific settings so long as these automated tools do not aim to exploit the favorable fills offered in the Simulated Environment.
As long as it adheres to response 1 then it's fine.
Trading Hours at MyFundedFutures: From 6:00 PM to 4:10 PM EST (Eastern Standard Time / NY Time) Note: Trading pauses briefly at 4:10 PM EST and resumes at 6:00 PM EST. The trading is closed for 1 hour and 50 minutes. Automatic closure of trades at 4:10 PM EST does not result in a breach of the account.
Please see the link below for our news trading policy. https://help.myfundedfutures.com/en/articles/8230009-news-trading-policy
intercom

[MFFU rep D] from MyFundedFutures
Thu, Nov 12, 8:09 PM (3 days ago)
to me

Thank you for stopping by! We are here to help you achieve goals and we see you’ve been inactive for some time, so this ticket is being closed.
Please, feel free to open a ticket again if something else is still needed.

70,000 traders trust MyFundedFutures because our rules are actually trader friendly and we offer the fastest payouts in the industry!

You can check out our post popular plan here.

intercom

amear Bani-Ahmad [Amear's address withheld]
Fri, Nov 13, 12:26 PM (2 days ago)
to support

Hi [MFFU rep A],

Thank you for your answers on Nov 12. The ticket closed before I could reply, so I'm reopening it with two short follow-ups. A written yes or no on each is all I need.

1. To confirm I've read your answer 2 correctly: may my automated strategy run unattended, with no one at the screen, on Evaluation and Sim Funded accounts (Rapid, Pro and Builder), as long as it follows the rule in your answer 1?

2. Your news trading policy lists "Builder Plans" under accounts where T1 news trading is permitted. Does that include Builder Sim Funded accounts, or only the Builder evaluation?

Thank you,
Amear Bani-Ahmad

[MFFU rep B] from MyFundedFutures
Fri, Nov 13, 12:36 PM (2 days ago)
to me

Hello amear. 👋 Thanks for reaching out to MyFundedFutures Support! My name is [MFFU rep B].

Kindly find the answers to your queries below.

Yes.
T1 news trading is allowed in the Builder plans in evaluation and Sim funded as well.
If you need any additional assistance or have more questions, don't hesitate to reach out via email or submit a ticket through our website. We're here to help!

Best regards,

MyFundedFutures Support

intercom

---

## Addendum 3 — corrections to the master's notes, written 2026-11-15T17:57:50Z (`date -u`)

Written by praxis-master after the first audit of this file (DECISION_LOG row 2026-11-15T17:57:50Z). Append-only: no line above this addendum was edited, so the wrong statements stay on the page beside their corrections. No message text is changed.

1. :134 says the fourth paste holds "15 messages". WRONG. It holds 14. Sender header lines counted from :145: 14.
2. :140 says `[MFFU responder C]` sent "the six Nov 11 replies". WRONG. It sent four replies dated Nov 11 (:177, :235, :279, :309) and the Nov 12 12:02 PM handoff line (:354).
3. :86 says the responder's name was replaced in "2 places (sender line and nothing else; the body signs with no name)". WRONG as written. Within Addendum 1's message the placeholder appears once, in the sender line at :94. "The body signs with no name" described the second paste as the master saw it in session: it ended at "Please let me know if this helps or if you have any further questions." The fourth paste shows two more lines under that same message, the AI-agent footer and "intercom" (:211-:212). The second paste did not contain them.
4. The original capture ends the Nov 13 reply at :78 with no "intercom" line; the fourth paste has one (:418). The first paste is not on disk and was not seen by the session that wrote this addendum, so whether it contained that line is UNVERIFIED.
5. :144, the sentence beginning "It has no numbers", is WITHDRAWN. The Nov 12 reply does contain a number: :369 reads "As long as it adheres to response 1 then it's fine." This file takes no position on which MFFU statements Amear's Nov 13 labels "answer 1" and "answer 2" refer to. The last sentence of :144 stands: the Nov 12 text is now on file.
6. :13, the words "except through the Nov 12 answers that are missing", are WITHDRAWN. They presumed what the Nov 12 answers cover. What the Nov 12 reply says is at :366-:372.

---

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
