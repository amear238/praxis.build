# 2026-11-14 evening rulings, worker 1: research screen (ruling 1)

Task: find where the record states the OLD research screen quoted at
docs/reports/2026-11-13-hermes-handoff-strategy-search.md:41.
Mode: BUILD (read-only research; this report is the only file written). HEAD 9ff8a48.

## Commands and output

### Commands 1-2 (as briefed; plus the handoff line itself)

```
$ sed -n 41p docs/reports/2026-11-13-hermes-handoff-strategy-search.md | cut -c1-400
   1. **Research screen changed.** Strategy research no longer requires peer-reviewed evidence. In-house backtesting over the five-year data set is the filter instead. This changes the research standard every brief since April has used ("published, peer-reviewed evidence on NQ after 2018"). Indicator-based strategies are now in scope.

$ git grep -n -i -E 'peer.?review|post-2018|after 2018|since 2018|2018' HEAD -- DECISIONS.md specs docs/specs | cut -c1-260 | head -60

$ git grep -n -i -E 'peer.?review|post-2018|after 2018' HEAD -- docs/reports | cut -c1-260 | head -60
HEAD:docs/reports/2026-11-04-proof-of-concept-standard.md:225:| Chuk (2026), Noise-band Intraday Momentum in Nasdaq-100 Futures | https://api.crossref.org/works/10.2139/ssrn.7609644 | **abstract only**, not peer-reviewed, no sha recorded | L2 |
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:57:| A4 | Post-2018 / algo-impact survival | D2 §1, §4; D4 Hard Filter 4; D6 F4 | Edge decay is a property of the market, not of the operator. |
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:58:| A5 | Source tiering (peer-reviewed or institutional; no course sellers) | D1 credibility note; D4 "Source Requirements" | An epistemic standard, independent of execution mode. |
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:111:| CO-OC Reversal (D8 Strategy C) | CONDITIONAL PASS, NQ post-2018 gap | C9: breaker #4 at 11:30 cuts its 12:00–15:00 exit window [I] | No | The evidence gap is A4, not disqualifying. |
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:185:   - **Strongest reason:** fully systematic (D2 #4: 10/10), intraday-flat, post-2018 evidence intact through 2022 (D2 #4, Ai 2024 [V as stated]), and demoted with no non-C reason on record. [I]
HEAD:docs/reports/2026-11-13-research-filing-worker1.md:39:   - Ambiguous item, left and listed: "Bradshaw 2026" / "Bradshaw (2026)" in the kimi file (received :29, :93, :97, :103). Kimi presents it as a practitioner source on NQ gap fades, and the channel's a
HEAD:docs/reports/2026-11-13-research-filing-worker1.md:252:     3	Sources: We cited only peer-reviewed or institutional sources above: F
HEAD:docs/reports/2026-11-13-research-filing-worker2.md:246:Sources: We cited only peer-reviewed or institutional sources above: F$
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:17:1. **Top pick: Baltussen, Da, Lammers & Martens (2021), "Hedging demand and market intraday momentum", Journal of Financial Economics 142, 377-403, DOI 10.1016/j.jfineco.2021.04.029.** V
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:29:4. **Post-2020 evidence is weak.** The paper ends in 2020. The "still alive 2022-26" claim rests on a SpotGamma market commentary (practitioner, not peer-reviewed). "Bradshaw 2026" and "
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:46:Below we review each of the four original strategies (C1–C4) and propose two new ones, verifying their rules and evidence. We then tabulate and compare all candidates. Wherever possible 
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:54:Post-2018 evidence: We note any published or recent research confirming or disputing each edge, especially beyond 2018. If the original cite is unavailable, we list the evidence as “unve
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:60:Each candidate below is presented with: Name, Rules (exact), Mechanism, Published vs. estimated performance, Cost check, Fill optimism, Trade count (OOS), Post-2018 evidence/decay, Tunab
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:81:Post-2018 evidence: None found. We are not aware of any academic test of this exact VWAP+volatility band strategy on NQ or other indices. VWAP-based reversion is plausible but not establ
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:102:Post-2018 evidence: Mixed. Bradshaw (2026) shows this edge was negligible 2010–2019, better 2020–26. In SPY (the more studied S&P ETF), open-gap fade edge tends to erode over time (only
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:135:Post-2018 evidence: Strong. The Baltussen (2021) study covers up to 2020 and finds robust results. Moreover, a 2026 market commentary (SpotGamma) confirms first-vs-last-half-hour moment
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:161:Post-2018 evidence: None for equities. Only FX analogues exist. No sign of a time-of-day anomaly for NQ.
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:184:Post-2018 evidence: Strong. Baltussen (2021) covers up to 2020. SpotGamma (2026) reconfirms it persists into 2022-26.
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:207:Post-2018 evidence: None. The only study suggests open-gap reversal, not continuation. So we expect no edge or negative expectancy.
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:290:Combining strategies to reduce drawdown: No specific peer-reviewed study precisely shows “mean-reversion + momentum lowers drawdown.” However, the spirit is akin to diversification. For
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:320:Many reported figures (especially for C1, C2, C6) come from unpublished backtests or dealer notes. We have no peer-reviewed verification of their NQ performance. All such stats are “mus
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:327:Sources: We cited only peer-reviewed or institutional sources above: Fung et al. 2000, Baltussen et al. 2021, Gao et al. 2018, Grant et al. 2005, Bank of Canada staff, plus open-researc
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:69:- Post-2018 evidence and any sign of decay since publication.
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:70:- For C3: compare the Gao et al. version with the Baltussen et al. version. Which has stronger post-2018 evidence on US equity index futures, and which fits our constraints better?
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:81:Find peer-reviewed or institutional work on survival probability under a trailing (high-water-mark) drawdown limit, and recommend a method we can run on our own backtest trade lists 
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:84:Use peer-reviewed journals, NBER/SSRN working papers with institutional authors, central bank and exchange research (CME Group, Federal Reserve), prop-firm official pages, and open-s
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:87:a. Per candidate (C1 to C4, then new ones): name, sources with links, exact rules, mechanism, published performance (marked published or estimated), cost check at 1 MNQ showing the a
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:98:Research Report: Intraday Strategies and Risk Frameworks for Prop-Firm Trailing Drawdown ConstraintsExecutive SummaryThe structural architecture of proprietary trading firm evaluatio

$ git grep -c -i -E 'peer.?review|post-2018|after 2018' HEAD -- docs/reports
HEAD:docs/reports/2026-11-04-proof-of-concept-standard.md:1
HEAD:docs/reports/2026-11-08-strategy-filter-audit.md:4
HEAD:docs/reports/2026-11-13-research-filing-worker1.md:2
HEAD:docs/reports/2026-11-13-research-filing-worker2.md:1
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-kimi-research.md:14
HEAD:docs/reports/2026-11-13-return-handoff-claude-ai-strategy-research.md:6
```

### Commands 3-5 (as briefed, run under zsh)

```
$ grep -n -i -E 'peer.?review|post-2018|after 2018' DECISION_LOG.md | cut -c1-260 | head -20
940:- [2026-11-13T21:03:55Z] WHO: praxis-master | WHAT: **Strategy-review index manager returned `Result: PASS`** (report `docs/reports/2026-11-13-strategy-review-index-manager.md`, 594 lines; workers 1-7; adversary round 1 49/51 MATCH with 2 MISMATCH and 6 S2
944:- [2026-11-14T01:28:05Z] WHO: amear | REPORTED BY: the Claude.ai channel, in `docs/reports/2026-11-13-hermes-handoff-strategy-search.md` :5-:17, which Amear pasted into this session and then approved here ("go from here", 01:25:40Z row) | WHAT: **Amear's 2

$ grep -rn -i -E 'peer.?review|post-2018' .claude CLAUDE.md STATUS.md HANDOFF.md 2>/dev/null | cut -c1-260 | head -20
.claude/state/handoff-latest.md:62:- [2026-11-13T21:03:55Z] WHO: praxis-master | WHAT: **Strategy-review index manager returned `Result: PASS`** (report `docs/reports/2026-11-13-strategy-review-index-manager.md`, 594 lines; workers 1-7; adversary round 1 49/51

$ grep -rn -F 'peer-reviewed evidence on NQ' . --include=*.md | grep -v '/.git/' | cut -c1-200
(eval):7: no matches found: --include=*.md
```

### Command 5 re-run in bash, plus wider sweeps

```
$ grep -rn -F "peer-reviewed evidence on NQ" . --include="*.md" | grep -v /.git/ | cut -c1-200   (bash; zsh globbed the unquoted *.md)
./docs/reports/2026-11-13-voice-handoff-strategy-review.md:62:Why it happened: every research run screened ideas by published, peer-reviewed evidence on NQ after 2018. Classic indicator strategies rar
./docs/reports/2026-11-13-hermes-handoff-strategy-search.md:41:   1. **Research screen changed.** Strategy research no longer requires peer-reviewed evidence. In-house backtesting over the five-year d

$ git grep -n -i -E "peer.?review|post-2018|after 2018" HEAD -- . ":!docs/reports" ":!DECISION_LOG.md" | cut -c1-260 | head -40
HEAD:docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:11:3. **Sources.** Vendor documentation, exchange documentation, peer-reviewed papers, and public GitHub repositories count. **Forum posts (Reddit, Elite Trader, NinjaTrader forum) may be used a
HEAD:docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:72:**Sources:** peer-reviewed and SSRN papers on backtest overfitting and deflated performance (Bailey & López de Prado — deflated Sharpe, probability of backtest overfitting, minimum backtest l

$ git grep -c -i -E "peer.?review|post-2018|after 2018" HEAD -- . ":!docs/reports"
HEAD:docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md:2

$ grep -n -o -i -E ".{120}(peer.?review|post-2018|after 2018).{120}" DECISION_LOG.md
940:was tested (four 2026-11-01 hand runs, D6/D7), research runs, indicators (record shows no systematic look; screening by post-2018 peer-reviewed NQ evidence excluded them; no ruling excludes indicators), VM agent 11-12/11-13 (second-hand only; three 
944:iscussed. I also want it to run a loop of looking into non-discretionary strategies. I want to remove the guardrails of peer-reviewed, since we would be able to backtest over the last 5 years of data. So the restriction of it being peer-reviewed is no
944:ut on the VM by hand ("Those rules are for you, not for me"). The rulings as the handoff lists them at :40-:45: (1) the peer-review screen is removed, and in-house backtests over the five-year data are the filter instead; (2) builds pause until three 
```

### Follow-up commands (bash; excerpts of real output, trimmed with cut, file:line kept)

```
$ git ls-files Redemtion | wc -l; git check-ignore -v Redemtion/
       0
.gitignore:7:Redemtion/	Redemtion/

$ git ls-files --error-unmatch docs/reports/2026-11-13-voice-handoff-strategy-review.md docs/reports/2026-11-13-hermes-handoff-strategy-search.md
error: pathspec 'docs/reports/2026-11-13-voice-handoff-strategy-review.md' did not match any file(s) known to git
error: pathspec 'docs/reports/2026-11-13-hermes-handoff-strategy-search.md' did not match any file(s) known to git

$ sed -n 12,14p "Redemtion/Intitialization-April 2026/# TRADING COMEBACK PLAN — THREE-PATH ARCHITECTURE.rtf"   (D1)
**Generated:** April 30, 2026\
**Source session:** Clinical session with Mythos \'97 trading behavioral review\
**Status:** Pre-execution briefing document \'97 carry to separate workstreams\
$ grep -n -i -E "peer.?review|post-2018|after 2018|since 2018" (D1) | cut -c1-260
53:Search for verified, low-discretionary or systematic trading strategies for index futures. Source exclusively from peer-reviewed quantitative finance literature, institutional research, and recognized industry authorities. Exclude retail YouTube educators a
65:- **Source credibility note on Waqar Asim:** ...

$ (D4) Redemtion/Research Prompts/PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts.md
3:**Generated:** May 6, 2026
47:| Standalone VWAP/Bollinger reversion on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
48:| Opening gap fade on NQ | **EXCLUDED** — no peer-reviewed NQ evidence post-2018 | — |
75:## UNIVERSAL HARD FILTERS — APPLY TO ALL THREE AGENTS
118:### 4. Verifiable Performance Data
120-Published back-test or live-track results with: win rate, profit factor (or payoff ratio), Sharpe ratio, max drawdown, trade frequency, and sample size. Minimum 200 trades in sample. Performance data must cover 2018–2025 (the algo-density era). Strategies 
142:## SOURCE REQUIREMENTS — APPLY TO ALL THREE AGENTS
144:**Tier 1 — Primary (required for any strategy to be included):**
145:- Peer-reviewed publications: Journal of Financial Economics, Review of Financial Studies, Journal of Finance, JFQA, ...

$ (D6) Redemtion/Research Results/PHASE_2_STRATEGY_DECISION_Compiled_Round_3.md
19:| F1: Evidence | Tier-1 peer-reviewed, sample ≥200 trades |
22:| F4: Post-2018 | Published or strongly implied persistence |
(same rows in "Redemtion/Intitialization-April 2026/PRAXIS PHASE 2 — STRATEGY DECISION INPUT.rtf" :28, :31)

$ grep -n -i -E "Generated:" "Redemtion/Intitialization-April 2026/"* ...
# TRADING COMEBACK PLAN — THREE-PATH ARCHITECTURE.rtf:12:**Generated:** April 30, 2026\
AUTOMATED TRADING INFRASTRUCTURE.rtf:12:**Generated:** May 5, 2026\
PHASE 1 OUTPUT SUMMARY.rtf:12:**Generated:** May 4, 2026\
PHASE 3 OUTPUT SUMMARY.rtf:12:**Generated:** May 8, 2026 (consolidated)\
PRAXIS INITIALIZATION PLAN- April2026.md:14:**Generated:** May 2, 2026\
PRAXIS PHASE 2 — EXPANDED STRATEGY SEARCH: THREE-AGENT DEEP RESEARCH.rtf:12:**Generated:** May 6, 2026\
PRAXIS_PHASE_3_OUTPUT_SUMMARY.md:3:**Generated:** May 8, 2026 (consolidated)

$ sed -n 56,58p docs/reports/2026-11-08-strategy-filter-audit.md | cut -c1-260
| A3 | Published performance data; ≥200 trades in sample | D1 "Back-test data required"; D4 Hard Filter 4; D6 F1 | Validation needs an evidence
| A4 | Post-2018 / algo-impact survival | D2 §1, §4; D4 Hard Filter 4; D6 F4 | Edge decay is a property of the market, not of the operator. |
| A5 | Source tiering (peer-reviewed or institutional; no course sellers) | D1 credibility note; D4 "Source Requirements" | An epistemic standa
(audit :3-:4: "By: Claude.ai Praxis channel (research agent), at Amear's brief"; "Every outcome below is **PROPOSED** pending Amear's approval.")

$ git log --diff-filter=A --format="%h %ad %s" --date=short -- docs/reports/2026-11-08-strategy-filter-audit.md docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md | cut -c1-160
19ae6c8 2026-11-08 docs: D-2026-11-08-A Amear rulings R1-R9 (voice 2026-11-08) with Correction 1; answers A1-A11 file; strategy filter audit (input, PROPOSED); 
84b1a58 2026-11-06 gate: praxis-auditor PASS mints the master's commit token (R-1104-1; D-2026-11-04-B + addenda 1-3); research set A/B/C + summaries + briefs +

$ git show HEAD:DECISIONS.md | grep -n -i -E "filter audit|..." | cut -c1-220   (relevant line)
1751:A9  File the 2026-11-08 strategy filter audit as an input to F2.

$ git show bf6fcc7:docs/specs/2026-11-09-r6-announcement-research-design.md | grep -n -i -E "peer|publish|2018" | cut -c1-260
59:- "Ai 2024" is not pinned in the repo (DECISIONS.md :1576). Taken as Ai, Bansal & Guo, "Macroeconomic Announcement Premium", Oxford Research Encyclopedia of Economics and Finance (2024-05-22) — the only 2024 item with that title [D1]. Abstract: "During the 
62:**2A — as published (hold through the release).** Long 1 MNQ from the close of the 18:05 ET bar on E−1 to the close of the 16:05 ET bar on E. BLOCKED BY MFFU RULE on Rapid and Pro Sim Funded (§0). Run only as a research benchmark, never deployable on a Sim 

$ git show HEAD:DECISIONS.md | sed -n 1940,1944p
D7  If D6 fails at every tier at 1 MNQ: do not design breaker values
    to fit the drawdown ceiling (that is curve-fitting). Report it, and
    pull R6's research (higher-win-rate, steadier-equity strategies)
    forward to P0. The Noise-Area baseline continues through the VM
    tests for the record, but a GO on MFFU is not expected from it.

$ sed -n 1,3p docs/reports/2026-11-13-voice-handoff-strategy-review.md; sed -n 62p (same) | cut -c1-260
# Voice handoff: strategy review with Amear, 2026-11-13
Written by praxis-master for the voice-chat agent. ...
Why it happened: every research run screened ideas by published, peer-reviewed evidence on NQ after 2018. Classic indicator strategies rarely have that kind of evidence, so they were filtered out before anyone tested them (index :125). ...

$ sed -n 125p docs/reports/2026-11-13-strategy-review-index-manager.md | cut -c240-900
... Screening in the research runs was by published post-2018 NQ evidence, and indicator-style entries were excluded on that ground (E3.3). No indicator-driven strategy has been coded or backtested.
(index :120: "Standalone VWAP/Bollinger reversion on NQ: "**EXCLUDED** — no peer-reviewed NQ evidence post-2018" (Redemtion Phase 2 table :47, E3.3).")
```

## Answers

**(a) Earliest dated statement of the screen, and its authority (WHO).**
- Peer-review part: the earliest dated text is D1, `Redemtion/Intitialization-April 2026/# TRADING COMEBACK PLAN — THREE-PATH ARCHITECTURE.rtf`:12 "Generated: April 30, 2026". At :53 it says: "Source exclusively from peer-reviewed quantitative finance literature, institutional research, and recognized industry authorities. Exclude retail YouTube educators and unverified course sellers." It has no post-2018 term and does not say NQ. Its stated authority is :13 "Source session: Clinical session with Mythos — trading behavioral review", with :14 "Status: Pre-execution briefing document". It is not an Amear ruling, and the lines I read do not name who wrote the text. OBSERVED for the wording and date. WHO is INFERRED (a document generated in a session, not a ruling).
- Post-2018 part as a hard screen: D4, `Redemtion/Research Prompts/PRAXIS_Phase2_Expanded_Strategy_Search_3Agent_Prompts.md`:3 "Generated: May 6, 2026". Hard Filter 4 (:118-:120) says "Performance data must cover 2018–2025 (the algo-density era)", and Source Requirements (:142-:145) says "Tier 1 — Primary (required for any strategy to be included): Peer-reviewed publications ...". The closest wording to the handoff's phrase is the D4 table at :47-:48: "EXCLUDED — no peer-reviewed NQ evidence post-2018". Those cells report a prior round's exclusion. D6 Compiled Round 3 :19/:22 restates it as F1 "Tier-1 peer-reviewed, sample ≥200 trades" and F4 "Post-2018: Published or strongly implied persistence". OBSERVED.
- All of D1-D8 are under `Redemtion/`, which is gitignored (`.gitignore:7`; `git ls-files Redemtion | wc -l` = 0). The old screen is therefore not in the versioned record at all. OBSERVED.

**(b) DECISIONS.md entry, rubric line, or only briefs/reports?**
Only briefs and reports, plus the untracked Redemtion files. Command 1 (DECISIONS.md, specs/, docs/specs/ at HEAD, which includes specs/SPEC_RUBRIC.md) returned no lines, even for the bare token `2018`. No DECISIONS.md entry and no rubric line states the screen. OBSERVED.
The tracked places are:
- `docs/reports/2026-11-08-strategy-filter-audit.md`:57-:58. These list A4 "Post-2018 / algo-impact survival" and A5 "Source tiering (peer-reviewed or institutional ...)" as PROPOSED filters taken from D1/D2/D4/D6.
- D-2026-11-08-A A9 (HEAD DECISIONS.md:1751) only says "File the 2026-11-08 strategy filter audit as an input to F2". Reading that as "filed as an input, not adopted as a rule" is INFERRED from the words "as an input".
- `docs/briefs/2026-11-04-research-briefs-tickdata-repos-poc.md`:11 lists "peer-reviewed papers" as one accepted source type among several (vendor docs, exchange docs, GitHub repos, forums with limits). It is not a requirement, and it has no post-2018 term. OBSERVED.

**(c) R6 design and ruling D7.**
Neither states the screen. The R6 design at bf6fcc7 has only two hits: :59 (pinning "Ai 2024", a published encyclopedia entry) and :62 ("2A — as published", the hold-through variant). Neither is a peer-review or post-2018 requirement. D7 (HEAD DECISIONS.md:1940-:1944) says "pull R6's research (higher-win-rate, steadier-equity strategies) forward to P0", with no source or date screen. OBSERVED.

**(d) Does "every brief since April" match the record's dates?**
Only partly. "April" matches D1 (April 30, 2026), but D1 has only the peer-review sourcing instruction. The "after 2018" and NQ parts first appear as a screen on May 6, 2026 (D4). D4's search was deliberately cross-instrument (FX, CL, NG), so "on NQ" was not its screen. OBSERVED. On "every brief": the tracked 2026-11-04 brief :11 accepts non-peer-reviewed sources. The 11-13 strategy research brief (return-handoff :84) lists "prop-firm official pages, and open-s[ource]" next to peer-reviewed journals, and asks for post-2018 evidence (:69) as a field to report, not as a gate. R6/D7 state no screen. OBSERVED. I did not search for briefs dated between May 8 and Nov 4. UNVERIFIED.

## Findings

1. **F1 (misattributed quotation).** The quoted phrase "published, peer-reviewed evidence on NQ after 2018" is in no brief. Command 5 (re-run in bash) found it only in two files. One is `docs/reports/2026-11-13-voice-handoff-strategy-review.md`:62, where praxis-master paraphrases on 2026-11-13 ("every research run screened ideas by published, peer-reviewed evidence on NQ after 2018"), citing index :125. The other is the hermes handoff :41. Both files are untracked. The handoff puts the phrase in quotation marks as if it were the standard briefs used, but it is a master paraphrase written on 11-13. OBSERVED.
2. **F2 (date overclaim).** "Since April" holds only for the peer-review sourcing clause (D1, 2026-04-30). The post-2018 hard filter dates to 2026-05-06 (D4), and no source joins "on NQ" to it as a general screen. OBSERVED.
3. **F3 (scope overclaim).** "Every brief" is contradicted by tracked briefs that accept other source types (2026-11-04 brief :11; 11-13 brief :84) and by R6/D7, which carry no screen. OBSERVED.
4. **F4 (no versioned authority).** The old screen has no DECISIONS.md entry and no rubric line. Its only statements are in the gitignored `Redemtion/` tree (D1, D4, D6) and in a tracked audit that marks it PROPOSED (filter audit :4, :57-:58). So the ruling removes a screen the record never adopted as a rule. That reading is INFERRED.
5. **Process note.** Command 5 as given failed under zsh (`(eval):7: no matches found: --include=*.md`), because the unquoted glob is expanded by the shell. I re-ran it in bash with the glob quoted. Command 1 returned empty output, which is the result itself, not an error.
6. **Context (not a finding against the handoff).** Amear's own words for the new ruling are in DECISION_LOG.md:944: "I want to remove the guardrails of peer-reviewed, since we would be able to backtest over the last 5 years of data." OBSERVED (grep -o excerpt above).

Files staged: none. The only file written is this report. No tracked file, index, or bead was touched.

Result: PASS

Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
