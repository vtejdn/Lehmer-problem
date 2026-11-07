# English progress report

Entry: [main.tex](main.tex).
The generated local output is `main.pdf`, beside the source.
This report, dated 11 October 2026, replaces the former account through L124 and incorporates completed mathematical work through [L_G355](../../../ledger/Yin_L_G0355_v1.md#unit-cap-fixed-scope).
The [recorded pause](../../../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-d221-closeout) belongs to that report's historical scope; the unrestricted Mahler-gap question remains unresolved.

The current account begins with overall progress, then has one main section for each of the four parent strategies: algebraic entropy, linear-group growth, group determinants, and arithmetic.
Its four subsidiary-strategy subsections follow the actual strategy hierarchy.
Important mathematical results are stated in theorem, proposition, lemma or corollary environments.
The [source map](source-map.md) records the strategy correspondence and every substantive group of results.
The project [citation applications map](../citation.md) records every external citation use in the current TeX with its passage, source evidence and limits.
The [computation attachment](supplement/readme.md) can be copied out of the repository.
Its standard-library verifier checks the finite optimization table; a separately implemented [return-core verifier](supplement/return-core.md) with NumPy and python-flint checks the original normalized words, complete 797507-state compact enumeration, original-digit ancestry and exact exclusions.

## Writing choices

Retain the user's explicit English language and human-mathematician audience.
The compiled report is self-contained in notation and explanations, with no internal Task, ledger, Claim or review identifiers, paths or instructions to consult internal files.
It gives full proofs of the principal elementary arithmetic interfaces and summarizes the longer adopted results at their exact scope; it is not presented as a replacement for every underlying complete proof.
The prose is newly composed, with no substantial external verbatim reuse.

The primary style model remains [MSY23](../../../audits/literature/MSY23/readme.md#presentation-observations), with the applicable report choices stated in this section.
Yin20 and ACSY24 retain their additional-model scopes, and Hun74 retains its algebra-terminology scope.
No other manuscript's overrides are transferred.
All logarithms are natural; Mahler measure is total, and the group determinant uses an unnormalized matrix trace.
Binary Shannon and collision entropy, algebraic entropy, a covariance lower certificate and actual covariance, and finite versus uniform conclusions are distinguished.
No boxed formulas are used.

The [typesetting bibliography](references.bib) is synchronized to canonical bibliographic identities.
Acquisition and audit prose is omitted from its reader-facing notes.
Consulted-version notes remain for GBV15, BV20, Dim19, Li26, Pri11 and Smy08.
Luc22 and Smy08 use the published article/collection entry types so their publication fields are printed.
This typesetting normalization changes neither the canonical bibliography nor source acceptance.

### Report structure

Scope: this G0001 progress report.

- The first numbered section is an overall progress summary.
  State the common mathematical objective, the principal progress across the strategies, and the remaining unresolved questions.
- Organize subsequent main sections by parent strategy and subsidiary strategies as subsections, using the actual strategy hierarchy to group related work.
  Shared preliminaries and cross-strategy synthesis may have separate sections when needed for clarity.
  Use mathematical names for reader-facing section titles; keep the correspondence to internal strategy IDs in the editorial source map.

## Reproducible build

From this directory:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The current source is `main.tex`, five `sections/*.tex` files, and `references.bib`.
A TeX installation must supply pdfLaTeX, BibTeX, latexmk, AMS mathematics, mathtools, Latin Modern, geometry, microtype, enumitem, booktabs, longtable, array, natbib, xurl, xcolor and hyperref.
There are no external figures or repository-specific TeX packages.
BibTeX and a Perl engine for latexmk are required.
If the launcher cannot locate Perl, invoke the installed latexmk Perl script with the available Perl engine.

PDF and ordinary TeX products stay beside the source and remain Git-ignored.
Inspection products belong in ignored `build/`.
There is no second reading copy.
The former thematic section sources have been replaced by `overview.tex`, `entropy.tex`, `growth.tex`, `determinants.tex` and `arithmetic.tex`.
Earlier source revisions remain in Git history; fixed mathematical evidence retains its original scope.

To verify the finite comparison, run `python supplement/verify.py`; it reads the supplied JSON beside the script and needs no network, optimizer or research-repository import.
Its mathematical and execution scope is recorded in the [attachment README](supplement/readme.md).

## Local build verification

On 4 November 2026, the current six TeX inputs and bibliography compiled in this directory with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, using MiKTeX pdfTeX 1.40.27, BibTeX and latexmk 4.88.
The result is a 29-page A4 `main.pdf`, including the explicit long-window certificate definition and ceiling argument in the growth section.
The final logs contain no unresolved references or citations, missing characters, warnings or overfull/underfull boxes.
Pages 16--18 were rendered and visually inspected, covering the changed passage and its transitions; the remaining pages were not newly inspected visually.
The manuscript-specific mathematical checking scope remains in [review.md](review.md).

The command `python -B supplement/verify.py` passed all 304 source columns, five exact finite-family optima and two strict improvements, and correctly rejected the sixth dual certificate.
That run checked the finite optimization attachment only.
The separately implemented [return-core attachment](supplement/return-core.md) now supplies and verifies the additional finite computational premise with all 797507 candidates, 1044588 ancestry nodes and seventy exact exclusions.
Its full check also passed after copying only its three reader-facing files to an isolated directory and running Python with -I -O; invalid-digit and altered-ancestry controls were rejected.
These are current attachment author checks, with historical manuscript proof reviews and independent maintenance acceptance distinct.
