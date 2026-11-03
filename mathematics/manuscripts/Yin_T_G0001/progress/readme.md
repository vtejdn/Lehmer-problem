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
The [computation attachment](supplement/readme.md) can be copied out of the repository and verifies the latest finite table with Python's standard library.

## Source-layout maintenance, 2026-10-16

The entry and five active TeX sections now use sentence-oriented source layout, preserving the report's words, formulas, paragraph structure, strategy hierarchy, result scopes and historical execution account.
The documented in-directory latexmk command succeeded after the changes and produced the 28-page `main.pdf`.
The final TeX and BibTeX logs have no unresolved references or citations, missing characters or box warnings.
The launcher retains its nonfatal Windows Perl locale fallback.
This maintenance did not rerun the certificate attachment or research computations, perform rendered-page inspection, or create a new mathematical review.

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
A standard TeX Live installation supplies pdfLaTeX, BibTeX, latexmk, AMS mathematics, mathtools, Latin Modern, geometry, microtype, enumitem, booktabs, longtable, array, natbib, xurl, xcolor and hyperref.
There are no external figures or repository-specific TeX packages.
This is a multi-file document, so the native compiler is used.

PDF and ordinary TeX products stay beside the source and remain Git-ignored.
Inspection products belong in ignored `build/`.
There is no second reading copy.
The former thematic section sources have been replaced by `overview.tex`, `entropy.tex`, `growth.tex`, `determinants.tex` and `arithmetic.tex`.
Earlier source revisions remain in Git history; fixed mathematical evidence retains its original scope.

To verify the finite comparison, run `python supplement/verify.py`; it reads the supplied JSON beside the script and needs no network, optimizer or research-repository import.
Its mathematical and execution scope is recorded in the [attachment README](supplement/readme.md).

Build recorded on 2026-10-18: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed with TeX Live 2026, pdfTeX 1.40.29 and latexmk 4.88, producing **28 A4 pages and 473,572 bytes**.
The final TeX and BibTeX logs have no errors, unresolved references or citations, warnings, overfull/underfull boxes or missing characters.
This was a build/reference check after the M20 visible-locator repair; it performed no page rendering or visual inspection and adds no mathematical review.

## Authoring check of the strategy revision

The checked revision is the strategy-structured 11 October 2026 working source entered through `main.tex`, with all five section files listed above and the unchanged twelve-entry `references.bib`.
The check covered the complete manuscript, including retained passages: definition organization, introduction before use, mathematical meaning and normalization, source attribution, first-use citations, and the stated boundaries between complete proofs, proof outlines, conditional results and finite certificates.
The primitive associate `p_Z`, the independent difference digits, and the actual order and walk in the Fourier subsection were made explicit.
The transition-collapse statement was checked against the fixed-input L125 result; the hitting and neutral-localization statements retain their original assumptions and input-dependent constants.
This is the authoring agent's presentation and consistency check, not a new independent mathematical review or a recursive re-audit of every source proof.

The four writing layers were applied throughout: general mathematical rules, Yin's author-wide policy, any actually applicable subfield choice, and this report's specific choices.
The broad human-mathematician audience and existing MSY23 model are retained; no new terminology exemption or substantial external prose reuse is introduced.

The final native build succeeded with TeX Live 2026, pdfTeX 1.40.29, latexmk 4.88 and BibTeX: **28 A4 pages, 473,603 bytes**.
The final LaTeX log has no errors, unresolved citations or references, duplicate labels, missing glyphs, package warnings, or overfull/underfull boxes.
There are 110 unique labels, 53 explicit cross-reference uses, 34 result environments, eight definition environments and twelve cited bibliography entries.
All 76 labels from the previous report remain represented.
The PDF's 85 internal links resolve.

The final pages were rendered with Poppler at 110 dpi and visually checked, including the one-page contents, the two-page overall summary, all strategy and subsidiary-strategy transitions, formulas, the finite certificate table and the one-page bibliography.
Extraction and page-boundary checks found no blank pages, replacement characters, internal research identifiers or out-of-page characters.

The unchanged standalone certificate verifier was rerun successfully for this revision: 304 original directions, five exact finite-family optima, two strict improvements, and the sixth feasible primal with its correctly rejected lag-9 dual.
This run did not execute the optimizer, the historical floating tableau or older return-core computations.
The attachment maps the current proposition, equation and table numbers to its checks.

## Local build verification

Checked at 2026-11-02T16:52 UTC.
Source revision: the report dated 11 October 2026, with all six TeX inputs and the standalone supplement program and certificate data unchanged.
The in-directory build succeeded with MiKTeX pdfTeX 1.40.27, BibTeX and latexmk invoked through its installed Perl script, producing 28 A4 pages.
Perl must be available to the latexmk launcher; direct invocation of the installed latexmk Perl script provides the same build procedure when the launcher cannot find that engine.
The final log has no unresolved references or citations, missing characters or box warnings.
All 28 rendered pages were inspected, with detailed checks of the dense formulas and finite-comparison table.

The command `python -B supplement/verify.py` passed all 304 source columns, five exact finite-family optima and two strict improvements, and correctly rejected the sixth dual certificate.
This is a build and certificate check at the supplement's stated finite scope.
