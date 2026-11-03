# Hun74: Chapter IV modules and selected finite-field interfaces

Date and reviewer: 2026-09-10, root; self-review.
The user requested a Chapter IV audit, import of useful definitions and results, and designation of the book as a terminology and definition source.

## Coverage and Evidence

The separately selected [Hun74-U007](Yin_U007.md#hun74-u007) retains the 2026-09-11 Chapter III principal-ideal, polynomial-Euclidean and Bezout-coefficient interfaces for C_F0039, without extending the Chapter IV audit or claiming a whole Chapter III review.

The later selected [Hun74-U006](Yin_U006.md#hun74-u006) retains the Chapter V finite-field extension, irreducible-degree and Frobenius interfaces inspected for the actual Salem construction.
Its statement/applicability scope does not extend the earlier Chapter IV proof audit.
The [actual realization consumer](../../../claims/Yin_C_G0164_v1.md#argument) uses that interface separately from the PID decomposition in U006.

<a id="psi-left-module-terminology"></a>
### Left-module homomorphism terminology, 2026-10-12

At the user's request, the authoring AI agent directly rendered and reread Definition IV.1.2, printed p.170 / PDF p.196, and Exercise IV.4.5, printed p.206 / PDF p.232, in the retained printing.
Definition IV.1.2 names an additive map preserving the left action an R-module homomorphism, with f(ra)=rf(a).
The p.170 examples give a ring its module structure by ordinary multiplication.
Exercise IV.4.5 identifies Hom_R(R,R) with the opposite ring; the right-multiplication interpretation follows locally because a homomorphism of the left regular module satisfies f(a)=af(1).
The exact wording of the exercise is not being quoted as a definition of right multiplication.

Let U be a unital complex algebra, X_i in U, and N=U tensor_C U^op.
Right multiplication by X_i tensor 1 minus 1 tensor X_i^op defines Psi_i:N -> N and is an endomorphism of N as a left module over itself.
Associativity gives Psi_i(rk)=r Psi_i(k).
This is ordinary left multiplication in N, distinct from any separately specified Hochschild coefficient actions.
The existing [U001](Yin_U001.md#module-conventions) and [U004](Yin_U004.md#hun74-u004) retain their earlier inspection scopes.
This is a targeted terminology and application self-check, not a renewed whole-chapter or independent audit.
Search stopped after the exact local definition and relevant exercise were inspected; no new source acquisition was needed.

The complete chapter, printed pp. 168–229 / local PDF pp. 194–255, was read in rendered pages.
Throughout this chapter, **PDF page = printed page + 26**.
The title/copyright pages and both chapter boundaries were checked.
The extracted text has pervasive character-mapping corruption; it was not used as evidence for formulas or as a reliable negative search.
Temporary page renders are reproducible reading aids, not additional source versions.

The seven units below review the main definitions, numbered results, proofs and proof sketches, with explicit elementary completions and retained foundational inputs.
Exercise pages were surveyed, but **their solutions have not been audited exhaustively**.
Only selected exercise consequences expressly reconstructed in a unit are accepted through that reconstruction.
This is neither a whole-book audit nor an independent or formal verification.

| Unit | Printed pages (PDF pages) | Scope and assessment |
| --- | --- | --- |
| [Hun74-U001](Yin_U001.md#hun74-u001) | §IV.1, 169–180 (195–206) | Modules, quotients, sums and exactness; main results audited within scope. |
| [Hun74-U002](Yin_U002.md#hun74-u002) | §IV.2, 180–190 (206–216) | Free modules, division-ring bases and dimension; main results audited within scope. |
| [Hun74-U003](Yin_U003.md#hun74-u003) | §IV.3, 190–199 (216–225) | Lifting, extension and splitting criteria; main results audited within scope. |
| [Hun74-U004](Yin_U004.md#hun74-u004) | §IV.4, 199–207 (225–233) | Hom variance, bimodules, algebraic duals; main results audited within scope, with explicit left/right conventions. |
| [Hun74-U005](Yin_U005.md#hun74-u005) | §IV.6, 218–226 (244–252) | PID structure theory; main proof chain audited with local completions and associate-class convention. |

## Inputs for Current Research

| Need | Exact reusable source interface | Current use boundary |
| --- | --- | --- |
| A basis containing a prescribed independent set over a division ring | [IV.2.4](Yin_U002.md#division-ring-bases), p. 183; right-module conversion is explicit | Supplies the already-used standard basis theorem in Yin_C_F0035-P1. |
| A coefficient functional and the induced tensor map | [IV.4.11](Yin_U004.md#algebraic-dual), p. 204; IV.5.2, p. 209 | Same Yin_C_F0035 source supplement identifies the existing algebraic argument; no continuity or boundedness of the functional is asserted. |
| Module, bimodule, Hom, dual, algebra and tensor terminology | [Definition-group index](../../../definitions/index.md#modules-hom-and-algebraic-tensors) | Definitions remain in these source units. Concrete choices of M, affiliated algebra or division subring remain with each consuming theorem. |

The tensor equalizer itself is a project argument in Yin_C_F0035; Hungerford is not cited as stating that exact equalizer theorem.
No new C IDs, mathematical Roles or proof-status promotions result from this audit.
The book's terminology role does not make it a style model or certify uninspected chapters.

## Corrections and Reuse Limits

- **Unitary modules:** in the source this means that the ring identity acts as the identity, not a Hilbert-space unitarity condition.
  Sections IV.1 and IV.5 allow more general modules unless qualified.
  The p. 212 countercheck explains the omitted qualification in the alternate construction and the restricted form accepted here.
- **Noncommutative coefficients:** Hom duals change sides.
  Tensor factors must have compatible right/left actions.
  Corollary IV.5.12 uses a basis-induced opposite-side action, which must not replace an already specified natural action silently.
- **Dimension and topology:** division-ring dimension, free-module rank and finite complex operator rank are different notions.
  All tensors and functionals here are algebraic.
  No Hilbert/Banach completion or bounded extension follows from this chapter.
- **PID results:** Section IV.6 requires its commutative PID and unitary-module hypotheses.
  Its prime decompositions are indexed by associate classes.
  Two compressed proof cases are completed in U006.

Search record: local primary pages supplied the mathematical evidence.
A publisher search on 2026-09-10 verified the work identity and chapter span at the [Springer record](https://link.springer.com/book/10.1007/978-1-4612-6101-8).
The bounded query `Hungerford Algebra errata page 212 tensor unitary modules` returned secondary errata/solution leads but no verified author or publisher correction of this passage.
Those leads were not used as mathematical inputs.
The search stopped because the direct primary reading and elementary countercheck settled the precise qualification needed here; author confirmation and an exhaustive errata search are not claimed.

## Review and Downstream Record

This source audit is the authoritative record of the source-reading operation, corrections and acceptance scopes.
The central audit index registers the seven unit IDs; the definition index supplies navigation; the role indexes record the user's designation.
A dated source supplement at Yin_C_F0035 attaches the accepted standard inputs to its unchanged proof.
Its extraction provenance and existing independent review remain separate.
Historical audits retain their original evidence scopes; the supplement clarifies that candidate-stage review wording in the preserved proof was superseded by the completed review already linked from the Claim index.

Documentation validation: `python scripts/check-research-records.py` passed for 252 Markdown files and 3,431 local links/anchors; `git diff --check` passed.
Comparison with the pre-integration snapshot verified that the complete preceding fraction/tensor ledger text is preserved.
These checks validate record integrity, not the mathematical proofs.
