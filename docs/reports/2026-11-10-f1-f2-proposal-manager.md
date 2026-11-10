# 2026-11-10 — Unit 2026-11-10-f1-f2-proposal — praxis-manager report

Result: PASS

Grading of this result is the auditor's, spawned by the master; this line is the manager's own return under the report contract, not a grade.

## Task

Authorisation: DECISION_LOG.md row 2026-11-10T13:03:00Z (praxis-master, decided under D-2026-11-08-D D1), items (2) "Unit 1 = F1 topology + F2 PROPOSAL" and (3) A6. That row is in the working tree, not in HEAD (adversarial F1 finding 4); the master commits it.

Produce (A) `docs/specs/2026-11-10-live-signal-topology.md` (rubric F1), (B) `docs/specs/2026-11-10-f2-session-flat-proposal.md` (rubric F2, PROPOSED only), (C) this report, (D) MANIFEST rows. No code, no VM, no n8n change, no ledger edit, no index operation.

## Rubric criteria addressed

F1 (`specs/SPEC_RUBRIC.md`:19–30), F2 proposal side (:32–45), O4 touched (:108–113, not answered), standing S1, S2, S6, S8, S13.

## Workers dispatched (id, mode, outcome)

| id | mode | scope | outcome |
|---|---|---|---|
| a3a7eb658b94718cc | ADVERSARIAL | both files, targets 1–4 + S13 | Hit its 40-turn limit with no findings file written (`/tmp/f1f2ev/adversarial.md` absent). Discarded; scope split and re-dispatched with a 25-call budget and write-as-you-go. |
| af378f333dca85f89 | ADVERSARIAL | topology doc, targets 1–4 | 1 BLOCKING (evidence pointer to an empty report), 6 MINOR. Findings file `/tmp/f1f2ev/adv-f1.md` (outside the repo by design: the brief allows three repo files). |
| a59b1fc3ff29563e2 | ADVERSARIAL | F2 proposal, targets 1–6 | 3 BLOCKING, 5 MINOR; targets 1, 5, 6 NOT REFUTED. Findings file `/tmp/f1f2ev/adv-f2.md`. |

The manager wrote (A) and (B) itself: they are documents, not production code, and the evidence had already been gathered in the manager's context; a BUILD worker would have had to re-gather it. Logged here as a process choice; the adversarial workers were briefed with the artifacts and criteria only, never the manager's reasoning.

## Process log

1. Read the rubric (F1–F4, O4, S1–S13) and `git show HEAD:` of the Phase 3 import (:11, :21–26, :91–111).
2. Gathered evidence: NinjaScript headers and order calls; consumer validation and submission; n8n container and the PRAXIS workflow node list (read-only `n8n list:workflow` / `export:workflow` to stdout, filtered to PRAXIS names; nothing changed); sweep daemon and drop dir; D-2026-07-09-D, D-2026-11-10-A; R8, A6, A9, D1, D2, D8; G11/G21/H02 rows; R6 `bf6fcc7` design and MFFU capture; d6 drawdown report; strategy filter audit; three beads.
3. Wrote this skeleton, then (A) and (B), then a capture script (`/tmp/f1f2ev/ev.sh`, outside the repo) whose output is pasted below verbatim.
4. Adversarial round (three dispatches, one failed, see above). Fixed every finding (section "Adversarial findings").
5. Appended three MANIFEST rows at the end of the file.
6. Re-ran the capture after the last fix; hashes taken last.

Observation not acted on: the strategy filter audit row A15 (audit :68) calls F4 "closed"; the rubric still lists F4 under FROZEN (`specs/SPEC_RUBRIC.md`:61, [E28]). Outside this unit; flagged for the master.

## Verification evidence (command output)

Produced by `zsh /tmp/f1f2ev/ev.sh` after the final document edit. Tags [E1]–[E30] are the ones the two documents cite. Output is filtered only where stated in the command (PRAXIS-named workflows and containers only; a public address in E29 replaced by `<URL-REDACTED>`; long lines cut with `cut -c`). Lines that carry the withheld term were not printed (rubric :37–42, bead `Praxis_build-ax4` description, filter audit :94 are cited by line number only).

```
[E1]
$ git rev-parse --short HEAD
a587a27

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | awk 'NR>=97 && NR<=109 {print NR": "$0}' | cut -c1-260
97: 1. Daily loss limit — unrealized + realized P&L drops below threshold → cancel all, flatten, disable for session
98: 2. Max trades per day — trade count hits daily max → disable order submission
99: 3. Consecutive loss (“two and done”) — 2 consecutive losers in one session → identical to max trades
100: 4. Session time gate — clock hits 11:30 ET → close positions, disable until next session
101: 5. Afternoon session window — clock enters 3:00–6:00 PM ET → disable everything
102: 6. Trailing drawdown proximity — account approaches MFFU’s $1,500 EOD trailing drawdown → reduce size or halt
103: 7. Max position size — order quantity exceeds plan → reject
104: 8. Stale signal filter — signal file older than X seconds → reject (prevents acting on delayed signals after a system hiccup)
105: 9. Heartbeat dead-man switch — if n8n hasn’t confirmed system health in 5 minutes → disable new orders
106: 
107: State management: Redis for real-time state checks (is the gate open or closed?), PostgreSQL for durable audit trail (every breaker trip logged with timestamp and context). Both run in Docker on your server. n8n queries Redis at the start of every workflo
108: 
109: The deterministic fallback script. A standalone Python script that runs independently of n8n. It polls the broker API directly, checks hardcoded thresholds (daily loss, max trades, session time), and can issue flatten commands or send alerts. No LLM. No i

$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n 11p | cut -c1-330
> **STATUS — the nine circuit breakers below are SPECIFIED ONLY.** As of 2026-11-05: **zero implemented, zero tested, zero tested under failure.** Specified ≠ implemented ≠ tested ≠ tested under failure. Basis, checked 2026-11-05: `grep -rniE "breaker|circuit" ninjascript/` returns one hit, a source comment in `ninjascript/Praxi

$ grep -rniE 'breaker|circuit' ninjascript/
ninjascript/PraxisNoiseAreaBreakout_Flat1559.cs:31:// This variant does NOT decide rubric F2 (session-flat time vs breakers #4/#5, FROZEN). The

$ ls -d n8n
ls: n8n: No such file or directory

[E2]
$ git ls-files | grep -i -E 'n8n|webhook|pine'
docs/reports/2026-05-11-sess2-step-0.5-webhook.md
docs/reports/2026-07-09-b1-b-n8n-file-write.md
docs/reports/2026-07-15-qxd-n8n-write-false-failure-fix.md

[E3]
$ sed -n '25,27p;101p;108p;188,191p' ninjascript/PraxisNoiseAreaBreakout.cs | cut -c1-200
// This is NOT the file-drop signal consumer (PraxisSignalConsumer.cs) — it carries no order
// pipeline, no JSON, no share watcher. It computes the band itself from bar history and trades
// it inside the backtester. Only house style / namespace / usings were borrowed from the consumer.
				Description  = "PRAXIS B2 Noise-Area Breakout (Zarattini SSRN 4824172) — paper-faithful NQ backtest strategy. 14-day per-minute-of-day noise band anchored at the 09:30 open with overnight-gap adju
				IsExitOnSessionCloseStrategy              = true;   // backstop; explicit 16:00 flat is primary
			// ---- 16:00 ET cash-close flat (spec §4 p.9/12; trader-locked). Applies before any entry. ----
			if (mod >= CloseMod)
			{
				FlattenAll("16:00 session flat");

$ grep -n -E 'EnterLong|EnterShort|ExitLong|ExitShort' ninjascript/PraxisNoiseAreaBreakout.cs
211:					ExitLong("XL", "");
219:					ExitShort("XS", "");
224:			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is
225:			//     the pre-fill state, so an ExitLong above followed by Close<Lower still reverses correctly.
227:				EnterLong(Contracts, "L");       // long breakout / reverse-to-long (spec §2)
229:				EnterShort(Contracts, "S");      // short breakout / reverse-to-short (spec §2)
288:				ExitLong("FlatEOD", "");
290:				ExitShort("FlatEOD", "");

[E4]
$ git log -1 --format='%h %s' a587a27 | cut -c1-160
a587a27 docs: housekeeping 2b (D11 G18, G30; bead zd4) - four 2026-11-01 NinjaTrader grid trade lists archived unaltered into docs/reports/evidence with hashes 

[E5]
$ git show c16f85f --stat --format='%h %s' | head -3
c16f85f ninjascript: add PraxisNoiseAreaBreakoutArmB.cs, walk-forward arm (b) tunable variant (WRITTEN, not compiled, not run)

 ninjascript/PraxisNoiseAreaBreakoutArmB.cs | 462 +++++++++++++++++++++++++++++

[E6]
$ grep -n -E 'WRITTEN, NOT COMPILED|Holding: the last half hour' ninjascript/PraxisLastHalfHourMomentum.cs
19:// WRITTEN, NOT COMPILED, NOT TESTED. No NT8 toolchain on the Mac; every behaviour note below is
32://   * Holding: the last half hour, 15:30 -> 16:00 close. Flat at the close; at most one trade a day.
141:				Description  = "PRAXIS 7zq M2 Last-half-hour market intraday momentum (Baltussen, Da, Lammers, Martens 2021, JFE 142, eta(r_ROD)). At 15:30 ET: long if (last 16:00 close)->15:30 return > 0, otherwise short; flat on the 15:59 bar. No tunable parameters. WRITTEN, NOT COMPILED, NOT TESTED.";

$ sed -n 110p docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-200
| Last-Half-Hour Momentum (D8 Strategy A; D4 "PASSED") | Built 10-31 as research-only "because it trades inside breaker #5's window" (repo, 10-31 handoff §0); retired by R-VN3-1 after net PF 0.84 (rep

[E7]
$ git show HEAD:DECISION_LOG.md | grep -E '^\| 2026-07-15T21:10Z' | grep 'TradingView-exportable' | cut -c1-420
| 2026-07-15T21:10Z | WHO: trader (Amear) + orchestrator (session 14) | WHAT: Block-2 Q1 CONFIRMED — strategy under test (Zarattini-Aziz-Barbon NQ Noise-Area clock-anchored breakout) is NOT TradingView-exportable; entry logic will be RE-IMPLEMENTED in NinjaScript and backtested in the NT8 Strategy Analyzer (scope-proposal path b). Unlocks Block-2 execution-bead dispatch | WHY: no Pine source anywhere in repo; live TV

$ git show HEAD:DECISION_LOG.md | grep -E '^\| 2026-07-16T19:29Z' | cut -c1-330
| 2026-07-16T19:29Z | WHO: trader (Amear) + orchestrator (session 16) | WHAT: Block-2 strategy definition LOCKED paper-faithful after Zarattini SSRN 4824172 sourced (commit 2a3f192, spec docs/specs/2026-07-16-b2-noise-area-ruleset.md) — (1) session-flat = 16:00 ET cash close (NOT the 11:30 PRAXIS window); (2) positions/session =

[E8]
$ ls -la /Users/admin/praxis-signals/praxis-processed-signals.log /Users/admin/praxis-signals/.heartbeat; ls -A /Users/admin/praxis-signals/incoming | wc -l
-rw-r--r--@ 1 admin  staff    11 Nov 10 08:25 /Users/admin/praxis-signals/.heartbeat
-rw-r--r--@ 1 admin  staff  1206 Jul 15 14:49 /Users/admin/praxis-signals/praxis-processed-signals.log
       0

[E9]
$ docker ps --format '{{.Names}} {{.Image}} {{.Status}}' | grep '^n8n-compose-n8n'
n8n-compose-n8n-1 n8n-custom:2.27.4 Up 42 hours

$ docker ps --format '{{.Names}}' | grep -c -i redis
2

[E10]
$ docker exec n8n-compose-n8n-1 n8n list:workflow 2>/dev/null | grep -i praxis
EmMbN4sslwIx1ydn|PRAXIS — Signal Webhook (Block 0)
Wq90beq5oysV1bpe|PRAXIS — Orchestrator Notify

$ docker exec n8n-compose-n8n-1 n8n export:workflow --id=EmMbN4sslwIx1ydn 2>/dev/null | python3 -I /tmp/f1f2ev/nodes.py
name: PRAXIS — Signal Webhook (Block 0) | active: True | updatedAt: 2026-07-16T19:22:05.322Z
  node: TradingView Signal Webhook | n8n-nodes-base.webhook
  node: Validate Signal Payload | n8n-nodes-base.code
  node: Is Payload Valid | n8n-nodes-base.if
  node: Respond 200 OK | n8n-nodes-base.respondToWebhook
  node: Telegram Notify Success | n8n-nodes-base.telegram
  node: Telegram Notify Write Failed | n8n-nodes-base.telegram
  node: Respond 400 Bad Request | n8n-nodes-base.respondToWebhook
  node: Telegram Notify Rejected | n8n-nodes-base.telegram
  node: Respond 500 Write Error | n8n-nodes-base.respondToWebhook
  node: Write Signal File | n8n-nodes-base.code
  redis/postgres nodes: 0

[E11]
$ sed -n 133p DECISIONS.md; grep -n -o 'is \*\*deferred to pre-live (Block 4–5)\*\*' DECISIONS.md
## D-2026-07-09-D — n8n Runs LOCALLY on the Mac for Block-1 Build-First; Public-Ingress Topology Deferred to Pre-Live
140:is **deferred to pre-live (Block 4–5)**

[E12]
$ grep -n -E '^OUTBOX=|^DROP=|heartbeat' scripts/praxis-signals-sweep.sh | head -6
4:# via a two-stage staging (incoming/) -> final promotion, and writes a heartbeat.
16:#  3. touch heartbeat (epoch seconds) so the stale-check job can detect a dead sweep
21:OUTBOX="${PRAXIS_OUTBOX:-/Users/admin/n8n-compose/local-files/outbox}"
22:DROP="${PRAXIS_DROP:-/Users/admin/praxis-signals}"
24:HEARTBEAT="$DROP/.heartbeat"
43:# 3. heartbeat

$ launchctl list | grep 'build.praxis.signals-sweep-daemon' | awk '{print ($1 ~ /^[0-9]+$/ ? "pid-present" : "no-pid"), $3}'
pid-present build.praxis.signals-sweep-daemon

[E13]
$ id praxispush; ls -ld /Users/admin/praxis-signals/
id: praxispush: no such user
drwxr-xr-x@ 14 admin  staff  448 Nov 10 01:54 /Users/admin/praxis-signals/

$ sed -n 2041p DECISIONS.md | cut -c1-260
**Accepted risk, plainly.** Until the trigger, the dedicated-user boundary of D-2026-07-09-C does not exist. Anything that can write as the primary account (admin), which owns the drop dir (OBSERVED above), can drop a signal file there; so can anything with wr

[E14]
$ sed -n '94p;164,165p;516,520p;527,528p;537,538p;638,641p;660,662p' ninjascript/PraxisSignalConsumer.cs | cut -c1-170
				MaxQty             = 5;                         // sim sanity cap
			// FileSystemWatcher: Created + Renamed (atomic tmp->rename upstream may surface either way through the share).
			watcher = new FileSystemWatcher(SignalsPath, "*.json")
			if (!TryGetString(f, "side", out s))
				return "missing required field 'side'";
			sig.Side = s.Trim().ToUpperInvariant();
			if (sig.Side != "BUY" && sig.Side != "SELL")
				return "invalid 'side' (must be BUY or SELL): '" + s + "'";
			if (d > MaxQty)
				return "'qty' " + d + " exceeds sim MaxQty cap " + MaxQty;
			DateTime tsParsed;
			if (!DateTime.TryParse(s, CultureInfo.InvariantCulture, DateTimeStyles.AdjustToUniversal | DateTimeStyles.AssumeUniversal, out tsParsed))
			if (!accountIsSim || Account == null
				|| !Account.Name.StartsWith(RequiredAccountPrefix, StringComparison.OrdinalIgnoreCase))
			{
				Log(LogPrefix + " signal_id=" + sig.SignalId + " ORDER REFUSED: account is not Sim. SIM ONLY.", LogLevel.Error);
					EnterLong(sig.Qty, entrySignal);
				else
					EnterShort(sig.Qty, entrySignal);

$ grep -n 'tsParsed' ninjascript/PraxisSignalConsumer.cs
537:			DateTime tsParsed;
538:			if (!DateTime.TryParse(s, CultureInfo.InvariantCulture, DateTimeStyles.AdjustToUniversal | DateTimeStyles.AssumeUniversal, out tsParsed))

[E15]
$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | awk 'NR==111 || NR==118 {print NR": "$0}' | cut -c1-520
111: | OPEN-2 | F2 (FROZEN); breakers #4 and #5 (Phase 3 spec :100-101); R8/A6 proposal unit | #4 "clock hits 11:30 ET → close positions, disable until next session": 1F (to 13:55) and 2S/2A (to 16:05) hold past 11:30. #5 "clock enters 3:00–6:00 PM ET → disable everything": 2S/2A hold 15:00-16:05. Entries at 18:05 are after #5 ends; whether #4's "next session" starts at 18:00 is undefined. 1N/1C (18:05→08:25) touch neither window. | OPEN (F2 changes state only when Amear approves the breaker proposal, A6) |
118: | A5 | R6 "trading day" = MFFU's definition | MFFU session 18:00 → 16:10 is the day for consistency, drawdown and inactivity counts. | Applied [D1] |

$ git show bf6fcc7:docs/reports/evidence/2026-11-09-r6-mffu-trading-day.txt | awk 'NR==10||NR==12||NR==15||(NR>=20&&NR<=22) {print NR": "$0}'
10: Trades may be placed beginning at 6:00 PM EST when the Globex session opens and can remain open until the New York session closes at 4:10 PM EST.
12: At MyFundedFutures, any open positions will be automatically closed at 4:10 PM EST on regular (non-holiday) trading days. Holiday trading hours will be communicated to traders including closure of open positions.
15: Note: Make sure that you don’t force a trade multiple times on the market after 4:10 PM EST, as this will sometimes cause the order to go through and disqualify your trading account.
20: During holiday trading hours, auto-liquidation will not occur at the half-time market close, and the trader is responsible for closing the positions.
21: Please note the times that you’re allowed to trade.
22: Failure to close the positions before the market closes will result in breaching of the account unless otherwise notified.

[E16]
$ sed -n 1452p DECISIONS.md
- F2 × Flat1559 is an interaction. A Flat1559 position runs past 11:30 (breaker #4), through 15:00 (breaker #5) and flattens before 16:00 (Deviation B). It is NOT resolved here.

[E17]
$ sed -n '1583,1589p;1744,1745p' DECISIONS.md
R8  F2 unfreezes. Breaker values set for manual trading are redone
    for the automated book: #2 max 2 trades/day, #3 two-and-done,
    #4 flat at 11:30, #5 as a disable of the system's own trading
    15:00–18:00, #8 inter-trade interval under 5 minutes.
    KEEP: #1 daily loss limit; #5 as a lockout on Amear's own
    interaction 15:00–18:00. New values come back to Amear as
    PROPOSED.
A6  FLAG 6: R8 starts the breaker PROPOSAL unit. F2's state changes
    when Amear approves the proposed values.

$ sed -n 1645p DECISIONS.md | cut -c1-260
- **FLAG 6 — R8 and F2's state.** Does R8 change F2's state in `specs/SPEC_RUBRIC.md` — do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition — and is master's reading (filing note 1), changeable by Amear, right? The rubric is his to edit (

[E18]
$ sed -n '133p;144,148p' docs/reports/2026-11-01-three-strategy-results.md
- Exit on session close by time: 16:00 784, 12:15 5, 12:00 2, 14:03 1. XL and XS exits are spread over 7 distinct times each [K03].
| 2021-11-26 | 13:15 | #90 | Short | 11:01 -> 12:15 | Exit on session close | 75 |
| 2023-04-05 | 14:03 | #312 | Short | 10:01 -> 14:03 | Exit on session close | 243 |
| 2024-07-03 | 13:15 | #514 | Long | 11:01 -> 12:15 | Exit on session close | 75 |
| 2024-11-29 | 13:15 | #576 | Long | 11:31 -> 12:15 | Exit on session close | 45 |
| 2024-12-24 | 13:15 | #583 | Long | 10:01 -> 12:15 | Exit on session close | 135 |

$ git show HEAD:DECISION_LOG.md | grep -n '2026-08-29T18:05:00Z' | cut -c1-330
365:- [2026-08-29T18:05:00Z] WHO: praxis-master (session 53) | WHO EXECUTED: amear (VM, by hand) | WHAT: **CHECK 3 MEASURED, NOT ADJUDICATED. The CME US Index Futures RTH template prints `8:30 AM – 4:00 PM`, time zone shown as `Central`. THE MASTER DECLINES TO CONFIRM THIS AS A GENUINE MISMATCH, BECAUSE BOTH HALVES OF THAT CONFI

[E19]
$ sed -n '4p;40,41p' docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-260
**Status:** recommendation only. Every outcome below is **PROPOSED** pending Amear's approval. No decision, spec or ruling is changed. The 2026-11-08 ruling RTH = 09:30–16:00 ET is not reopened.
4. **Breakers #2, #3, #4 and the system-wide half of #5 carry manual-era values into the automated book.**
   - Breaker #4 flattens at 11:30. That truncates the published Noise-Area (flat at the cash close, D2), CO-OC's exit window (D8) and the Announcement-Day Premium. [I]

$ sed -n '1751p;1777p' DECISIONS.md | cut -c1-200
A9  File the 2026-11-08 strategy filter audit as an input to F2.
- **A9.** *Answers:* routed item (3), audit §6 Q3's yes/no (`docs/reports/2026-11-08-strategy-filter-audit.md:213`, "Do you want this audit filed as an input to F2?"). *Effect:* the audit is an input 

[E20]
$ sed -n '39p;65p' docs/reports/2026-11-09-d6-drawdown-check-manager.md | cut -c1-200
**With the daily-loss cap at breaker #1's spec value:** NOT COMPUTABLE. No numeric spec value exists (evidence E4). A SENSITIVITY run at round caps is in Appendix A, last block. It is not a recommenda
6. **Breaker #1.** No numeric value exists, so the capped run at the spec value is not done. Sensitivity was run at $100 / $200 / $300 / $500 (1 MNQ) and $1,000 / $2,000 / $3,000 / $5,000 (1 NQ): roun

[E21]
$ sed -n 1551p DECISIONS.md
R1  RTH = 09:30–16:00 ET (answers §4 item 1, B1). Arms (a) and (b)

$ grep -n -E '^### F1|^### F2|^### O4|Unblocks when|^\*\*Blocks' specs/SPEC_RUBRIC.md | sed -n '1,4p'
19:### F1 — Signal-path topology vs. circuit-breaker placement
28:**Unblocks when.** `docs/specs/*-live-signal-topology.md` exists, is committed,
30:**Blocks.** Block 3 entirely. Any SHM threshold derivation.
32:### F2 — Session-flat time vs. breakers #4 and #5

[E22]
$ sed -n '63p;72p;99p' docs/reports/2026-11-09-d11-sweep-manager.md | cut -c1-240
| G11 | "do R8's words on #4 and #5 name F2's governing rule and 15:00 disposition" (raised 2026-11-08) | DECISIONS.md:1645 (rows W3-91) | WAITING (A6 answers FLAG 6 except the #4/#5 part, DECISIONS.md:1788) | NOT-D2: F2 wording; D2(c) need
| G21 | "how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7" (raised 2026-11-02) | DECISIONS.md:536; DECISIONS.md:694 (rows W3-34) | WAITING |
| H02 | ""whether #4's "next session" starts at 18:00 is undefined."" (raised 2026-11-09T10:02:44Z (bf6fcc7; AFTER cutoff)) | bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md:111 (rows W4-17) | WAITING (after the cutoff) | N

$ sed -n '536p;694p' DECISIONS.md | cut -c1-200
6. Not ruled (notes-3 line 40): how does Amear rule on handoff §5 items 1 (early-close stamps, F2), 5 (settings not visible in the screenshots), 6 (baseline settings screenshot), 7 (VM hash-check of t
26. Line 63: *"§3.3 items (strategy-file hash check, template early-close readback): do them or not?"* Same as C-6 (11-01 handoff §5 items 7 and 1). The 11-02 handoff §3.3 (lines 56–58) puts them unde

[E23]
$ sed -n '1912,1916p;1945,1954p' DECISIONS.md
D2  Only four things stop and wait for Amear's word: (a) spending
    money; (b) switching live trading on, or any order path to a
    funded account; (c) changing circuit-breaker values while real
    money is at stake; (d) installing keys, credentials or agent
    permissions. Everything else is D1.
D8  Brief §4 decisions: (3) start the VM session as soon as the VM
    handoff carries the step-0 answers (C3, C9, C10). (4) draft the F1
    live-signal topology doc alongside the F2 breaker PROPOSAL. (5) land
    the two staged MFFU evidence reports (2026-08-07, 2026-10-28) and
    grade them against F4's criterion. (6) the five P0 guard beads are
    accepted as known risk while only docs/specs move; fixed before any
    Block 3 code that can place orders. (7) the VM stays a hands-only
    executor; Mac is the only master. (8) "final step of this build" =
    Block 4 paper pass on MFFU sim (the standing proof-of-concept
    ruling). Block 5 live is a separate sign-off under D2(b).

[E24]
$ git show HEAD:DECISION_LOG.md | grep -E 'T23:50:09Z\] WHO: amear' | cut -c1-330
- [2026-11-05T23:50:09Z] WHO: amear | WHAT: **RULINGS + OVERNIGHT LOOP — 2026-11-05 18:46 ET, typed, verbatim:** "Rulings 1. Arm (b) stop: evaluated on bar close, exit by market order next bar — same rule as the breakers (R-VN4-2). Not a resting stop in the backtest. Minute data is sufficient for arm (b). No tick purchase. R-VN4

[E25]
$ bd show Praxis_build-2nh | sed -n 1p; bd show Praxis_build-ax4 | sed -n 1p; bd show Praxis_build-yra | sed -n 1p
○ Praxis_build-2nh · live-signal-emission topology for the anchor strategy + breaker placement in the order path   [● P1 · OPEN]
○ Praxis_build-ax4 · Dev-B 16:00 ET session-flat collides with breaker #4 (11:30 ET close) + breaker #5 (15:00-18:00 disable)   [● P1 · OPEN]
○ Praxis_build-yra · Dev-C reverse-and-re-enter vs breakers #2/#3 + Block-4 live-vs-backtest reconciliation   [● P1 · OPEN]

[E26]
$ grep -n -o 'Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15' DECISIONS.md; grep -n -o 'B1-f T1-T4 all PASS' DECISIONS.md
175:Block 1 (Foundation, build-first) milestone SIGNED OFF by Amear, 2026-07-15
175:B1-f T1-T4 all PASS

[E27]
$ git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n 24p | cut -c1-260
> - Row `[2026-11-05T23:51:21Z] WHO: amear` — this row is labelled REPORTED BY the voice agent (source: `docs/reports/2026-11-04-voice-session-notes-4.md`): R-VN4-2 breakers as resting stops?: "Until the account is live … resting stops." Asked which: "The latt

[E28]
$ grep -n '^Signal flow' CLAUDE.md
21:Signal flow: TradingView alert → webhook → n8n workflow → JSON file drop → NinjaScript FileSystemWatcher → bracket order → Rithmic → MFFU

$ sed -n '61p' specs/SPEC_RUBRIC.md
### F4 — MFFU automation compliance

[E29]
$ git show HEAD:HANDOFF.md | sed -n 1539p | sed -E 's#https?://[^ )`]+#<URL-REDACTED>#g'
- `936d7e4` — Step 0.5: n8n signal webhook published (workflow EmMbN4sslwIx1ydn @ <URL-REDACTED>)

[E30]
$ sed -n 132p docs/reports/2026-11-01-three-strategy-results.md | cut -c1-200; sed -n 82p ninjascript/PraxisSignalConsumer.cs; sed -n 224p ninjascript/PraxisNoiseAreaBreakout.cs
- Exit names: Exit on session close 792, XL 10, XS 8. **No `FlatEOD` exit appears.** The repo source has `ExitLong("FlatEOD")` / `ExitShort("FlatEOD")` at `PraxisNoiseAreaBreakout_OppBand.cs:314/316` 
				EntriesPerDirection                      = 10;                       // allow several concurrent signals
			//     EnterLong while short closes the short and goes long). Position.MarketPosition here is

$ sed -n '1907,1911p' DECISIONS.md; sed -n 2039p DECISIONS.md | grep -o 'DEFERRED, not dropped'; sed -n 2043p DECISIONS.md | grep -o 'stays with Amear'
D1  Default-decide. When a unit or the master reaches a question that
    would otherwise go to Amear, it takes the recommended option, logs
    it as "decided by master under D-2026-11-08-D D1", and continues.
    Amear may reverse any such decision later; the reversal is filed
    like any ruling. No unit waits on Amear except for D2 items.
DEFERRED, not dropped
stays with Amear
```

Additional checks run after the final edit. In the two S13 commands below, `<the S13 sentence>` stands for the full sentence and `<S13 prefix>` for its first three words; they are written that way here so the sentence occurs once in this report.

```
$ grep -c -x -F '<the S13 sentence>' docs/specs/2026-11-10-live-signal-topology.md; grep -c -F '<S13 prefix>' docs/specs/2026-11-10-live-signal-topology.md
1
1
$ grep -c -x -F '<the S13 sentence>' docs/specs/2026-11-10-f2-session-flat-proposal.md; grep -c -F '<S13 prefix>' docs/specs/2026-11-10-f2-session-flat-proposal.md
1
1
$ grep -n -o -E '^[0-9]\. [A-Z][^—]+—' <(git show HEAD:docs/specs/2026-11-05-phase3-build-specification.md | sed -n 97,105p)
1. Daily loss limit 
2. Max trades per day 
3. Consecutive loss (“two and done”) 
4. Session time gate 
5. Afternoon session window 
6. Trailing drawdown proximity 
7. Max position size 
8. Stale signal filter 
9. Heartbeat dead-man switch 
$ for each name: grep -c -F '<name>' docs/specs/2026-11-10-live-signal-topology.md
Daily loss limit : 1
Max trades per day : 1
Consecutive loss (“two and done”) : 1
Session time gate : 1
Afternoon session window : 1
Trailing drawdown proximity : 1
Max position size : 1
Stale signal filter : 2
Heartbeat dead-man switch : 1
$ git diff --numstat -- MANIFEST.md; git diff -- MANIFEST.md | grep -c '^-[^-]'
11	0	MANIFEST.md
0
$ git diff --cached --name-only
docs/reports/evidence/2026-10-28-mffu-davi-reply.png
```

## Adversarial findings

Each finding is from the workers' findings files (`/tmp/f1f2ev/adv-f1.md`, `/tmp/f1f2ev/adv-f2.md`), not their summaries. Every one was fixed or answered.

| # | From | Sev. | Finding | Fix made |
|---|---|---|---|---|
| T1 | adv-f1 1 | MINOR | Breaker #3 used straight quotes; Phase 3 :99 uses curly quotes. | Curly quotes restored; byte-exact name check above prints 1 for all nine. |
| T2 | adv-f1 2 | MINOR | B1(c) said "already decided"; D-2026-11-10-A is a deferral ("DEFERRED, not dropped", :2039; provisioning "stays with Amear", :2043). | B1 row now says the deferral is decided, provisioning is D2(d), B1 stays open as accepted risk. [E30] |
| T3 | adv-f1 3, adv-f2 | MINOR | Last-Half-Hour Momentum said "15:30 → 16:00 hold"; its `Description` says "flat on the 15:59 bar" (:141). | Both documents corrected. [E6] |
| T4 | adv-f1 4, adv-f2 1 | BLOCKING | [E*] tags pointed at an empty skeleton report. | Evidence section above pasted from the capture run after the final edit. The authorising DECISION_LOG row is in the working tree only; the master commits it. |
| T5 | adv-f1 5 | MINOR | #4/#5 clock checks only in n8n; a file written just before the cut-off, or dropped straight in (B1), is not refused after it. | Consumer ET clock check added to #4 and #5 rows, to the path line, and to option 1's unbuilt list; B1(a) now says #1, #2, #3, #6 do not apply to a straight-dropped file. |
| T6 | adv-f1 6 | MINOR | Exits have no instruction type; consumer only knows BUY/SELL and only calls `EnterLong`/`EnterShort`; an exit sent as SELL reverses. `EntriesPerDirection = 10` (:82) not cited under #7. | EXIT/FLATTEN types added to #1's dependencies, OPEN-T2 and option 1's unbuilt list; :82 cited under #7. [E14], [E30] |
| T7 | adv-f1 7 | MINOR | A committed record of a public webhook address (HANDOFF.md:1539) not cited in 1.9 / B5. | Cited in 1.9 (address not reproduced); level stays UNVERIFIED. [E29] |
| P1 | adv-f2 2 | BLOCKING | Proposed #5 lets the system trade 15:00–16:00, but the topology doc's #5 row blocked all entries in the window. | Topology #5 row now gives the placement as the Phase 3 text stands, and what changes under the proposal (window check removed, only the operator lockout remains). F2 doc says so beside its #4/#5 text. |
| P2 | adv-f2 3 | BLOCKING | "Closed by 16:00:00" while #4 only sends the close at 16:00:00. | Rule F2-1 now says the closing order is submitted no later than 16:00:00 ET and the position is confirmed flat before MFFU's 4:10 PM auto-close; proposed #4 says the same, with an alert if not flat. |
| P3 | adv-f2 4 | MINOR | 15:00 disposition unconditional; wrong on an early-close day at or before 15:00. | Disposition now says "on a full trading day", with the early-close case stated. |
| P4 | adv-f2 5 | MINOR | "The exchange's close" undefined. | Defined as the CME early close for NQ on that date as published; the time is stated as not checked. |
| P5 | adv-f2 6 | MINOR | Results lines are from the OppBand run, where the session-close backstop made all 792 exits; "already flattens at 16:00" overstated. | Block 2 row now says the explicit flatten is WRITTEN, cites the 792 backstop exits (results :132), and marks "the backtest flattens at 16:00 ET" UNVERIFIED. [E30] |
| P6 | adv-f2 7 | MINOR | R8's "F2 unfreezes." omitted; audit [I] tag dropped; 12:00 and 14:03 exits omitted; MFFU "EST" read as ET silently. | All four added (EST→ET labelled INFERENCE). |
| P7 | adv-f2 8 | MINOR | OPEN-F2-1, -2, -4 routed to Amear though not D2 items (D1, DECISIONS.md:1907–1911). | Re-routed to the master / R6 unit under D1, changeable by Amear; topology OPEN-T6 and OPEN-T8 likewise. Adoption (OPEN-F2-5) stays Amear's under A6. [E30] |

Not re-run by a second adversarial pass after the fixes (turn budget). The fixes are text changes checked by the post-edit capture and the name and S13 checks above.

## S6 cross-block check

Topology doc touches, by name: Block 1 (emitter changes from TradingView to NT8; CLAUDE.md:21 signal flow [E28]); Block 2 (emitter must reproduce the backtest; O4 parity widens); Block 3 (all nine breakers, Redis, PostgreSQL, fallback script, consumer checks, EXIT/FLATTEN types); Block 4 (paper pass on MFFU sim, D8(8)); Block 5 (live, D2(b)); Deviation A; Deviation C (reversals count for #2, bead `Praxis_build-yra`); Deviation G (D-2026-07-09-D); D-2026-11-10-A (bypass B1); rubric F2, F4, O2, O4; the SHM thresholds F1 blocks (:30).

F2 proposal touches, by name: Block 2 backtest session window (R1 RTH 09:30–16:00; `PraxisNoiseAreaBreakout.cs` 16:00 flatten; the OppBand run's backstop exits); walk-forward arm (b) Flat1559 exit policy; the Block 4 parity gate (rubric O4, `specs/SPEC_RUBRIC.md`:108–113); Deviation B; Deviation C with breakers #2 and #3; the R6 evening-entry strategy (Pre-Announcement Drift: 18:05 entries allowed; 16:05 holds conflict, OPEN-F2-2); Last-Half-Hour Momentum (retired, not reopened); breakers #8/#9 and the F1 topology (FLATTEN path); the Block 3 deterministic fallback script (session-time threshold 16:00); the D6 drawdown check; rubric F2 "Why frozen" (:37–42, cited by line only).

## Self-grade

| Criterion | Grade | Basis |
|---|---|---|
| F1 | Addressed, not cleared | Names the live emitter (section 2), all nine breakers by name (name check above, each count ≥ 1), placement upstream of `SubmitBracket` for each check, flatten actions stated as orders, five bypass routes. Clears only on commit plus auditor confirmation (:28–29). |
| F2 (proposal side) | Addressed, PROPOSED | One rule (Rule F2-1); 15:00 disposition stated; #4/#5 replacement text in the file only; G11, G21 item 1, H02, A9, MFFU 4:10 PM and breaker #1 inputs carried. No DECISIONS.md entry written; F2 stays FROZEN. |
| S1 | PASS (self) | Every repo claim carries an [E*] tag whose output is pasted above. |
| S2 | PASS (self) | All nine breakers SPECIFIED; the MaxQty cap WRITTEN and untested as a breaker; the Block 1 pipe TESTED on Sim (Parallels era), current VM UNVERIFIED; arm (b) WRITTEN; public ingress UNVERIFIED; "backtest flattens at 16:00 ET" UNVERIFIED. |
| S6 | PASS (self) | Section above, by name, for both documents. |
| S8 | PASS (self) | D2 items named as "waits for Amear": D2(b) live order path (OPEN-T9, B2), D2(c) breaker values with real money (OPEN-T4, #1, #6), D2(d) signing key and webhook credential (B1, B5), D2(a) a data subscription (option 2). Topology decided by master under D1, labelled changeable by Amear. Adoption of Rule F2-1 left to Amear under A6. |
| S13 | PASS (self) | The S13 sentence: one standalone line, exactly once, last line, in both documents (checks above) and in this report. |

## Files staged

None staged. All files are left in the working tree; the real index was not touched (`git diff --cached --name-only` above prints only the pre-existing PNG). Files written or modified by this unit:

```
$ wc -l docs/specs/2026-11-10-live-signal-topology.md; openssl dgst -sha256 docs/specs/2026-11-10-live-signal-topology.md
     114 docs/specs/2026-11-10-live-signal-topology.md
SHA2-256(docs/specs/2026-11-10-live-signal-topology.md)= 7e5f4cf5340917e81775818db0a7d972776ff23c4b24ad45a8d7455de074661f
$ wc -l docs/specs/2026-11-10-f2-session-flat-proposal.md; openssl dgst -sha256 docs/specs/2026-11-10-f2-session-flat-proposal.md
      81 docs/specs/2026-11-10-f2-session-flat-proposal.md
SHA2-256(docs/specs/2026-11-10-f2-session-flat-proposal.md)= 5c0128300cf41e2516dce5f0b8be9f7829ab59913e8c53aaec08034181d000d8
$ wc -l MANIFEST.md; openssl dgst -sha256 MANIFEST.md
     355 MANIFEST.md
SHA2-256(MANIFEST.md)= 16ad7719006d8909037f516e9009bd5c57febecdd337cd6580b2389d1ebd92eb
```

This report (`docs/reports/2026-11-10-f1-f2-proposal-manager.md`) cannot carry its own hash; the master computes it with `wc -l` and `openssl dgst -sha256` on the working-tree file. MANIFEST.md: 3 rows appended at the end (lines 353–355), 0 lines deleted (`git diff --numstat` above prints 11 added, 0 deleted; the other 8 added lines were already in the working tree before this unit).

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
