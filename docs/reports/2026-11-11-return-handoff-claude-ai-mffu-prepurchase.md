# RETURN HANDOFF — Claude.ai channel, 2026-11-11: MFFU pre-purchase thread (WHO: amear)

Written by the Claude.ai Praxis channel at 2026-11-12T00:35Z for praxis-master to file. Not a DECISIONS.md entry; edits no ledger. Email text below was OBSERVED by the channel via the Gmail connector (Gmail thread `1a1ccc24a09baa1f`); on disk it is REPORTED BY the channel. MFFU's support rep display name is replaced by `[rep]`; no email addresses are written here (MFFU's public support address is named only as "MFFU support").

Standing limitation: Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.

## Authority
- Amear, chat 2026-11-11 17:37 ET, on sending the redrafted ticket (report `docs/reports/2026-11-11-mffu-connection-investigation.md` C3.3) as a new email with a "no account yet" first line: "yep".
- Amear, chat 17:40 ET, on replying to ask for a team review: "go".
- Amear has no MFFU account. The email was sent as a pre-purchase question to MFFU support, not from a dashboard.

## Messages (UTC)
1. 2026-11-11T22:37:27Z, Amear → MFFU support, subject "Pre-purchase question: automated NinjaTrader strategy on evaluation and funded accounts". The C3.3 text, with these changes by the channel: first line "I don't have an account yet. I'm asking before I buy an evaluation."; the "Thank you for confirming…" paragraph dropped; risk checks named (daily loss limit, max trades per session, session time limits); "No copy trading, no third-party signals." added; "so I have a record before I buy" added to the closing. Five questions as C3.3.
2. 2026-11-11T22:38:25Z, MFFU support ([rep]) → Amear. Verbatim:
```text
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
```
3. 2026-11-11T22:40:44Z, Amear → MFFU support (same thread): asks the team for a written decision on (1) the exact setup on Rapid, Pro and Builder Sim Funded; (2) unattended execution; (3) "Simulation" account type on funded accounts; (4) evening entry vs overnight.
4. 2026-11-11T22:41:33Z, MFFU support ([rep]) → Amear. Verbatim:
```text
1. Automated strategy setup (Rapid, Pro and Builder Sim Funded)
 Automated strategies are permitted on MFFU accounts, including Evaluation, Sim Funded and Live, provided they follow the applicable rules. High‑frequency trading is prohibited, and strategies must not attempt to exploit favorable simulated fills. However, a specific technical configuration (such as NinjaTrader → n8n webhook → file‑based order execution) cannot be approved in writing from the available information. Automation is allowed in principle, but individual setups are not automatically approved.
 2. Running the strategy unattended during the session
 Automation is permitted, but the policy does not confirm whether unattended execution without supervision is allowed or required. The absence of a supervision rule does not establish permission for a specific unattended configuration.
 3. NinjaTrader connection account type
 When connecting NinjaTrader to your MFFU account, the connection should be configured with the account type set to Simulation in the NinjaTrader connection properties.
 4. Holding a position from 6:00 PM to before 9:30 AM the next day
 MFFU trading hours run from 6:00 PM to 4:10 PM Eastern Time. Positions must be closed by the 4:10 PM cutoff. A trade opened after 6:00 PM and closed before 9:30 AM the following day remains within the permitted trading window and does not cross the daily close.
```

## Channel's reading (INFERRED; the filer grades)
- Both replies came within about a minute of the outgoing mail; they read as automated assistant replies (INFERRED, not confirmed).
- R6 OPEN-1 (evening entry vs overnight): answered in writing by MFFU support (message 4, point 4): within the permitted window, does not cross the daily close. Whether an automated-assistant reply counts as MFFU's written answer for the rubric is Amear's call.
- T1 news: message 2, point 5 answers it per plan (2-minute window on Rapid/Pro Sim Funded only; Builder and evaluations unrestricted).
- F4: still NOT MET. MFFU support states it will not approve a specific configuration in writing, and does not confirm unattended execution. Whether F4's bar can be met through email support, or must be revised, is Amear's (rubric is his).
