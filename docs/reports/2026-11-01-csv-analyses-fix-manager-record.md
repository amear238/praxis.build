## Verification evidence

```
$ diff /private/tmp/claude-501/-Volumes-Sensidine-Praxis-build/8eda06af-cf5e-49ca-8017-37e3b279ea79/scratchpad/snap/csva-pre-fix.md docs/reports/2026-11-01-csv-analyses.md
37c37
< **Gate 0, reference totals reproduced.** OBSERVED [K04]:
---
> **Gate 0, reference totals reproduced.** OBSERVED [K04]; the reference values are the net, PF and max DD of the comparison table in the prior report [prior report L401-L404], supplied in the dispatch brief:
89c89
< Trades, PF, win rate and average trade per year are in K05. The `p=0` column is 0 in every row (OBSERVED [K05]). The year × side breakdown is in K06a.
---
> Trades, PF, win rate and average trade per year are in K05. The `p=0` column is 0 in every row (OBSERVED [K05]). The year × side breakdown is in section `K06a` of K06.
133c133
< Net and PF per side per exit year. OBSERVED [K06b]; K06a prints the same cells per year and side.
---
> Net and PF per side per exit year. OBSERVED [K06], section `K06b`; section `K06a` of K06 prints the same cells per year and side.
183c183
< Years with a negative side net, within each run, OBSERVED [K06b]:
---
> Years with a negative side net, within each run, OBSERVED [K06], section `K06b`; 2021 and 2026 are partial years (INFERRED, see Limitations):
190c190
< Trade counts and average trade per side are in K06a and K06b. The side trade counts are also in K04 (`sides=`).
---
> Trade counts and average trade per side are in sections `K06a` and `K06b` of K06. The side trade counts are also in K04 (`sides=`).
$ wc -l docs/reports/2026-11-01-csv-analyses.md
     695 docs/reports/2026-11-01-csv-analyses.md
$ git status --short docs/reports/2026-11-01-csv-analyses.md
?? docs/reports/2026-11-01-csv-analyses.md
```

S6 cross-block check: not applicable; process record only, excluded from the commit.

Result: PASS

## 2026-11-01T21:57:27Z — fix 2 (line 37 cite, DECISION_LOG row 2026-11-01T21:56:40Z)

Verification evidence for fix 2 (pasted output):

```
$ diff .../snap/csva-pre-fix2.md docs/reports/2026-11-01-csv-analyses.md
37c37
< **Gate 0, reference totals reproduced.** OBSERVED [K04]; the reference values are the net, PF and max DD of the comparison table in the prior report [prior report L401-L404], supplied in the dispatch brief:
---
> **Gate 0, reference totals reproduced.** OBSERVED [K04]; the reference values are the net, PF and max DD of the comparison table in the prior report [prior report L402-L405], supplied in the dispatch brief:
diff_exit=1
$ wc -l docs/reports/2026-11-01-csv-analyses.md
     695 docs/reports/2026-11-01-csv-analyses.md
```

S6 cross-block check: not applicable; process record only, excluded from the commit.

Result: PASS (scoped to the mechanical check: one hunk, line 37 only, 695 lines)
Filer's note (2026-11-14, unit 2026-11-14-dirty-tree-cna-filing, praxis-master under D-2026-11-08-D D1): the limitation sentence below was appended at filing under rubric S13; the text above is unchanged.
Fills are optimistic; Standard resolution on 1-minute bars; 2 ticks/side slippage assumed.
