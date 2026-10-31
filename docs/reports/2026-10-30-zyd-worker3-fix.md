# Praxis_build-zyd — worker 3 fix pass

## Task
BUILD (fix pass) on the unstaged D-2026-10-30-A entry in `DECISIONS.md`, `config/backtest-cost-model.json` (`fill_resolution_note` only) and MANIFEST.md lines 133-143. Apply manager fixes F1–F12 exactly. Nothing staged, no commits.

## Fixes applied
- F1: heading and Status line replaced with the exact text in the brief (CONDITIONAL, void clause live; [N] LOCKED at 21:36:30Z, reaffirmed 22:22:00Z (WHO: amear)).
- F2: added `(WHO: amear)` after the 22:22:00Z cite in Context, (b), Rationale, the authorisation chain and NEEDS AMEAR 3. Rationale's short `22:22:00Z` became the full `2026-10-30T22:22:00Z` as the brief instructs.
- F3: Context now reads "filled at the next bar's open (INFERRED per 3gm D2(a) `:710`)".
- F4: the (c) clause was replaced with the brief's text. Line refs are backticked.
- F5: added "— plus (`:108`) IsExitOnSessionCloseStrategy = true — platform session-close exit, clock-triggered (INFERRED)" straight after the six-call-site inventory and its "each a managed … no price argument" description.
- F6: replaced the flat no-resting-order sentence with the OBSERVED/INFERRED version.
- F7: replaced the "meant to price" lead-in with the brief's text.
- F8: replaced the void-clause trigger sentence with the brief's text.
- F9: replaced the limitation label with the "PROPOSED wording, not ruled by Amear" text. The sentence itself is unchanged. Added NEEDS AMEAR item 4.
- F10: added the S6 F4 (MFFU) bullet after the Analyzer-template bullet.
- F11: set `cost_model.fill_resolution_note` to the brief's exact string. The edit was a whole-line JSON-encoded replacement, and no other key changed.
- F12: changed the zyd-artifact Purpose, the voice-notes Purpose and the config UPDATE row ("fill_resolution Standard (CONDITIONAL, void clause live)").

Prefix integrity: the sha256 of `head -n 132 MANIFEST.md` (ccb7c289…) and `head -n 246 DECISIONS.md` (c438920f…) were identical before and after the edits.

## Verification evidence
```
== 1
0
0
== 2
PARSE_OK
12
== 3
22.96 4.592 2 Standard
== 4
CONDITIONAL, void clause live	1
(WHO: amear)	6
INFERRED per 3gm D2(a)	1
mod >= CloseMod	1
:108	1
would not decide	1
Only the first is a slippage item	1
"the VM measurement"	1
PROPOSED wording	1
Approve or replace	1
F4 (MFFU	1
== 5
0
       6     # grep -o occurrences of 2026-10-30T22:22:00Z in entry
6            # grep -c lines
       1     # '2026-10-30T22:22:00Z (WHO: amear)' (Status line, unbackticked)
       5     # '2026-10-30T22:22:00Z` (WHO: amear)' (backticked: Context, (b), Rationale, chain, NA3)
== 6
'We accept Standard resolution on 1-minute bars. Band-edge slippage widened to [N]. Fills are optimistic and the report states so. If the VM measurement shows NT8 errors or demands a secondary series rather than falling back silently, this row is void and the assumption is re-decided cold.'
entry==00:10 True 289 289
21:36==00:10 True
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
f9144cb50aab2885e28daecefb4c3e80a900963769bf396d92c3318629884a79
non-ascii in a: []
== 7
      47
(tail -n 11 MANIFEST.md shows the 3 edited rows; see the manager's console)
```
Config removed lines vs HEAD (12): $schema_note, version, decision_ref, 4 slippage lines, fill_resolution, fill_resolution_note, 2 total_cost lines, total_cost_breakdown_note. All 12 come from the earlier build pass. HEAD already contained `fill_resolution_note`, so F11 added no new removed line.

## Deviations
- Check 2 returned 12, not the 9 the brief expected. Every removed line predates this pass (listed above). The brief's figure undercounts the earlier build.
- Check 5 literal-string count: 1 unbackticked plus 5 backticked equals all 6 occurrences tagged. In the 5 backticked cites the closing backtick sits between the timestamp and "(WHO: amear)", which matches the entry's existing backtick style.
- Because F4 and F6 are both applied verbatim, (c) now says "no Set*/Submit*/limit/stop call exists" twice. I did not de-duplicate it.
- F5 placement: after the six call sites and their shared description, so that "each a managed Enter*/Exit* call" does not read as covering `:108`.

## Files modified (unstaged, not git-added)
DECISIONS.md (D-2026-10-30-A entry only), config/backtest-cost-model.json (fill_resolution_note only), MANIFEST.md (rows 133-143 only), plus this report.

## Result: PASS
