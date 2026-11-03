---
author: Yin
---

<a id="dr97-u005"></a>
# DR97-U005: External Interfaces, Version Evidence, and the Miy22 Relationship

- Source: [DR97](../../../literature/pdf/DR97.pdf), 10-page published version.

- Locators: Section 2.1, pp. 614-616; Lemma 10, p. 620; Section 4, pp. 621-622; bibliography, p. 622.
  The related Miy22 passages are its abstract, Introduction p. 2, and references [10], [12], [13] on p. 24.
- Record: 2026-09-08, interface reviewer, for [DR97 rational-series source audit](readme.md#dr97-rational-series-source-audit).
- Kind and coverage: supporting theorem-interface checks, source relationship, and bounded version/bibliographic review.
  This is **not** a full-proof audit of the external sources.
  Each interface has its own acceptance and inspection boundary below.

## Formal-series inputs

DR97 explicitly presents Theorems 2-4 without their proofs, referring to its reference [2].
For the finite-alphabet, commutative-field setting used in the audited main chains, [DR97-U001](Yin_U001.md#dr97-u001) reconstructs the required interfaces: residual spaces, recognizable/rational equivalence, tensor-product realization of a Hadamard product, and minimality giving matrix coefficients as two-sided residuals.
Therefore these exact interfaces do not remain dependent on an unaudited book statement.

The source's arbitrary-commutative-ring formulation, semiring extension, and historical priority reports are outside that local reconstruction.
The finite-alphabet restriction in U001 is essential.
Minimal representation states cannot be allowed to retain nonzero transitions on nonreduced words that are invisible to the input and output vectors.

A search for the Berstel-Reutenauer author version located the 2010 typeset book draft, but access failed through the web fetch and a TLS trust failure through direct download.
No TLS bypass was attempted and no book artifact was retained.
The local reconstruction resolves the needed field interfaces, so this access issue does not impose an unresolved premise on them.

## Haagerup inequality accepted for the analytic chain

The required original statement was checked in [Haa79](../../../literature/pdf/Haa79.pdf), Lemma 1.4 and its following remark, printed pp. 285-286, PDF pp. 7-8.
For a finitely generated free group with its reduced word length, put $\chi_m=1_{\{|g|=m\}}$.
With counting measure, left convolution $\lambda$, and the usual square-root $\ell^2$ norm, the lemma gives, for finite-support $f$,

$$
\|\lambda(f)\|\leq\sum_{m\geq0}(m+1)\|f\chi_m\|_2.
$$

In particular, a homogeneous $f$ of degree $m$ satisfies $\|\lambda(f)\|\leq(m+1)\|f\|_2$.
The remark allows infinite-support $f$ when the displayed weighted sum converges.

This supplies exactly DR97 Lemma 10's operator estimate.
If $\sum_{|g|=m}|a_g|^2\leq Mc^m$ with $c<1$, then $\|\lambda(a_m)\|\leq\sqrt M(m+1)c^{m/2}$, a summable bound.
No unchanged-rate estimate after taking a square root is needed.
The statement, conventions, and applicability were checked against text and rendered pages; it is accepted as an established external input.
Its original proof, including Lemma 1.3, was not independently audited.

## Malcev-Neumann foundation and optional free-field identification

**Foundation used in Section 4.**
Let $k$ be a commutative field, and let $G$ carry a total order preserved by both left and right multiplication.
Series $\sum_{g\in G}a_gg$ with well-ordered support form a division ring $k((G))$ under coefficientwise addition and convolution.
For fixed $g$, each convolution coefficient is a finite sum.
This exact statement and these conventions were checked in the published exposition [Coh06b](https://api.pageplace.de/preview/DT0400.9780511893841_A23680440/preview-9780511893841_A23680440.pdf), Section 4, Theorem 4.1 and its preceding paragraph, printed p. 9, PDF p. 25 of the 33-page published preview.

The source sketches inversion by extracting the least support element and summing powers of the remaining positive-support series.
It refers the detailed proof to earlier sources.
This is direct reading of a published exposition, not inspection of the original Malcev or Neumann proofs.
The exact theorem is accepted as the foundational ambient-algebra input; no weakening to a merely one-sided order is made.
The separate finite-positive-alphabet support argument is reconstructed in U005.
The attempted AMS access to Neumann's original paper returned HTTP 403; no original-proof coverage is claimed.

**Optional identification.**
The original statement of [Lew74](https://www.researchgate.net/publication/246182799_Fields_of_Fractions_for_Group_Algebras_of_Free_Groups), Section III, Theorem 2, printed p. 343, was checked in the author-uploaded published article text.
If $F$ is free on $X$, $R=k\langle X\rangle$, and $D$ is a Malcev-Neumann series field for $F$ over commutative $k$, then

$$
U(R)=U(kF)\cong\operatorname{Div}_{D}(kF)
$$

as fields containing the specified group algebra.
Here $U$ denotes the universal field of fractions, and $\operatorname{Div}$ is the smallest division subring containing $kF$.
The preceding paragraphs and introduction specify the coefficient field and embeddings.

This primary statement supports DR97's optional free-field interpretation.
The theorem's original proof, Hughes-free uniqueness, and universal-field construction were not audited.
The statement is accepted for this identification only.
Theorem 12, when rationality is defined as division closure inside $D$, does not require it.
No local Lew74 PDF was retained: the AMS download returned HTTP 403 and the author-page PDF link failed, while the published article's text remained readable.

## What transfers to Miy22

[Miy22](../../../literature/pdf/Miy22.pdf) identifies DR97 as the reduced-free-group predecessor in its abstract and Introduction p. 2, and cites it as reference [10].
Its bounded result is an analogue for a finite semicircular tuple, while its affiliated theorem follows the direction of the later Linnell extension cited there as [12].
This directly read relationship does not identify DR97's Malcev-Neumann division ring with an affiliated-operator algebra.

| Interface | DR97 | Miy22 and the existing audit | Reuse boundary |
| --- | --- | --- | --- |
| Coefficient model | Reduced words of a free group | Fock word vectors represented by monic Chebyshev word polynomials; [Miy22-U001](../Miy22/Yin_U001.md#miy22-u001) | Free-group generators are unitary; semicircular generators are self-adjoint and obey different word recurrences. |
| Finite-rank test | Tree Fredholm commutator $[\mathcal F,a]$ | Commutators $[r_i^*,a]$ with right annihilation operators; [Miy22-U003](../Miy22/Yin_U003.md#miy22-u003) | Both encode residual information; equality of the actual operators or ranks is not asserted. |
| Formal representation | Minimal matrix coefficient series inherit reduced support | Finite coefficient residuals and minimality; [Miy22-U002](../Miy22/Yin_U002.md#miy22-u002) | The formal-state mechanism transfers after changing the coefficient basis. |
| Analytic realization | Group-word evaluation of the transition matrix, with nonreduced transitions zero | Additional matrix realization of the Chebyshev word basis; [Miy22-U004](../Miy22/Yin_U004.md#miy22-u004) | Direct substitution of a formal word by its Chebyshev word polynomial is not multiplicative. |
| Scalar inverse closure | DR97 Definition 1 calls this rational closure; Theorem 7 equates it with all matrix closures | Miy22 calls the scalar version division closure and the matrix version rational closure; [Miy22-U005](../Miy22/Yin_U005.md#miy22-u005) | Translate the closure terminology and ambient algebra before combining statements. |
| Beyond bounded operators | Well-ordered-support algebra and Theorem 12 | Closed densely defined affiliated operators and bounded fraction defects; [Miy22-U006-U006](../Miy22/Yin_U006.md#miy22-u006) | Affiliation, regular denominators, and exact operator domains require the separate Miy22 machinery. |

The shared analytic strategy is finite residual dimension, minimal realization, decay from rational square coefficients, homogeneous norm estimates, and scalar Schur inversion.
This is a comparison of recorded mechanisms, not a new transfer theorem or proof of equivalence between the two operator models.
In particular, the optional free-field identification in Miy22 reference [13] is a different interface from Lew74 and is not discharged by this DR97 audit.

## Version comparison and bibliography evidence

The primary audit locators remain those of the 10-page journal artifact.
A 14-page [author-hosted typeset version](../../../literature/pdf/DR97--author.pdf), linked from [Duchamp's publication page](https://www-lipn.univ-paris13.fr/~duchamp/), was retained as comparison evidence.
Its opening footnote identifies the published article; its preparation/revision date is not stated.
It is not treated as an erratum or a replacement primary version.

Selected text comparison covers author pp. 9-13, corresponding to journal pp. 619-622.
Rendered author pp. 10 and 13 were inspected for the specific issues below.
This was not a complete proof audit of the author version.

- The author p. 10 repeats the unrestricted residual norm assertion of Lemma 10(ii), the same unspecified norm-bound exponent, and an incompletely parenthesized Schur expression.
  It supplies no unambiguous corrected formula for these passages.
- Author p. 11 still cites Lemma 11(i) in the initial decay argument for Proposition 9, where homogeneous decay comes from Lemma 10.
- Author p. 13 repeats reference [8]'s year 1994 and its misleading English journal name for Fliess's *Matrices de Hankel*.

For the last item, the coordinating agent's bibliographic query and a direct check of [Fliess's 1981 paper bibliography, reference 18](https://www.numdam.org/item/?id=BSMF_1981__109__3_0), identify *J. Math. Pures Appl.* **53** (1974), 197-222, and list an erratum in **54** (1975), p. 481.
This is secondary bibliographic evidence about the 1974 source and its erratum; neither of those artifacts was inspected.
It corrects source discovery and does not reopen the independently reconstructed finite-alphabet, field-coefficient interfaces merely because the historical source had an erratum.

## Search evidence, limitations, and downstream effects

On 2026-09-08 the interface search began from the exact dependencies in DR97, not a general literature survey.
Queries included the original Haagerup title and homogeneous inequality; Berstel-Reutenauer minimal representations; Lewin's title; Malcev-Neumann well-ordered support and Neumann's 1949 title; and the DR97 title/DOI and authors with `erratum`, `correction`, and `corrigendum`.
The [publisher record](https://link.springer.com/article/10.1007/s002220050154), Duchamp's page, and its linked author version were inspected.
No DR97 correction notice was identified in those inspected sources or query results.
This bounded search does not establish that no correction exists.

The search stopped once the exact analytic input, ambient division-ring theorem, optional free-field statement, and concrete version comparison were available.
The numerical and algebraic repairs in the other DR97 units remain local audit findings, not author-confirmed errata.
No author was contacted, no unpublished material was transmitted, and no proof-assistant or external human review was performed.

U006 supplies declared external trust boundaries and notation conversion for U003-U005 and the integrated audit.
The existing Miy22 proof assessments are unchanged: this comparison neither invalidates them nor upgrades their separately retained foundations.
No new project theorem, research route, or novelty claim is registered.

On the same date, the Malcev-Neumann reconstruction agent independently reviewed the consumed Malcev-Neumann and Lew74 interfaces, and the analytic reconstruction agent reviewed the completed unit against U003-U005's needs.
A wording ambiguity suggesting a finite coefficient field was corrected to a finite alphabet with field coefficients; no unresolved interface objection was identified.
These checks reviewed the unit's statements and applicability boundaries, not the external original proofs.

## Source and inspection

Source edition: DR97, the retained ten-page published Inventiones mathematicae 128 (1997), pp. 613-622, DOI 10.1007/s002220050154. Printed page equals PDF page plus 612. The separately retained 14-page author typeset version has an unstated preparation/revision date and was compared only at the selected passages recorded in U006; it does not replace the primary version.

Passages: Section 2.1, printed pp. 614-616; Lemma 10, p. 620; Section 4, pp. 621-622; bibliography p. 622. Related Miy22 abstract, Introduction p. 2, and references [10], [12], [13], p. 24; exact external and author-version locators remain in the body.

Inspection: 2026-09-08: exact Haa79, Coh06b and optional Lew74 statements and applicability checked, with independent internal interface reviews; their original proofs were not fully audited. Selected author-version passages were compared only at the recorded locations. Fliess's 1974 article and 1975 erratum were not inspected; their identity is secondary bibliographic evidence. Bounded searches and access failures do not assert exhaustive errata coverage; no external human review or formal verification.
