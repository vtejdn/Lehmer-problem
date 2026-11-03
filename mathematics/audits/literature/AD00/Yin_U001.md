---
author: Yin
---
# AD00-U001: global cyclotomic Frobenius and height costs

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

Date: 2026-10-15.
Root records strategy_critique's SOURCE-only reading and additionally read actual retained PDF pages 4--6, containing printed 3--5.
This is the classical global-Frobenius method antecedent for the new local inquiry; it is not a proof of a new non-Galois extension.

<a id="ad00-u001"></a>
## Read; accepted classical statement and method scope

## Source and inspection

Source edition: Francesco Amoroso and Roberto Dvornicich, A lower bound for the height in abelian extensions, institutional author manuscript,13 PDF pages including a repository cover and printed1--12. Published Journal of Number Theory80(2)(2000),260--272 is a different pagination.

Source passages: Printed1--6: height definitions/introduction, Lemmas1--3, Proposition1 and the beginning of Proposition 2. Lemma2 and Proposition1 start printed3/PDF4; Lemma3 is printed5/PDF6.

Inspection: Exact source statements and the selected local-to-product-formula proof read. Original strong-approximation and other foundational proofs were not recursively audited.
No complete Lemma4 optimization or later corollary review.

The normalization is the absolute logarithmic Weil height h; for a primitive degree-d minimal polynomial its total logarithmic Mahler measure is d*h.
Use the source Notations on printed 2 / PDF 3: m>=3 and m is NOT congruent 2 modulo 4, and K_m=Q(zeta_m).
These guards also apply to the p=2 branches below.
Lemma 2 supplies ONE global sigma_p in Gal(K_m/Q).
If p does not divide m, then p divides gamma^p-sigma_p(gamma) for every integral gamma.
If p divides m, it instead divides gamma^p-sigma_p(gamma^p).
In the latter case equality can trigger descent after multiplying gamma by a root of unity to a proper cyclotomic subfield.
These are different differences and cannot be interchanged.

For p>=3, Proposition 1 states for nonzero alpha in K_m not a root of unity:

    h(alpha)>=log(p/2)/(p+1) if p does not divide m;
    h(alpha)>=log(p/2)/(2p) otherwise.

Its inspected proof clears denominators locally using Lemma 1, uses the global automorphism at all places, and applies the product formula.
In the first branch the Archimedean contribution is (p+1)h(alpha)+log2 and the p-adic contribution supplies log p.
Nonvanishing of alpha^p-sigma(alpha) uses nontorsion.
The ramified branch uses 2p h(alpha), together with root-of-unity descent when its difference vanishes.
The statement is accepted at its classical scope; reading this proof with its external inputs is not an independent audit of all those inputs.

Lemma 3 retains the p=2 distinctions: for integral gamma and the source sigma_2, if 4 does not divide m then 4 divides gamma^4-sigma_2(gamma^2); if 4 divides m then 4 divides gamma^2-sigma_2(gamma^2).
The selected beginning of Proposition 2 shows how the stronger modulus enters the height cost.
No later optimization theorem or its exact final constant is adopted by this unit.

The method therefore directly attributes a global-conjugate comparison with complete height normalization and ramification branches.
It does not permit independently choosing incompatible local automorphisms in a general number field, nor does it bound the coefficients of an arbitrary polynomial representative of sigma(alpha).
Any new bounded-extension, conjugacy-count or original-degree estimate must be proved in the project material.
The unit is used for classical method credit and exact prior scope, not as a substitute for those new proofs.

The [retained author manuscript](../../../literature/pdf/AD00--author.pdf) identifies the inspected source edition.
The repository cover's retrieval date is not the paper's publication date.
There is no printed contents list.
A bounded author-URL attempt hit a redirect limit before the institutional copy succeeded; the failed request is not another inspected edition.
No equality of author and publisher bytes is asserted.

## Actual source correction

2026-10-15T12:39.
The source-only final comparison identified the omitted source Notations m>=3 and m not congruent 2 modulo 4.
The corrected statement restores those actual hypotheses, particularly for Lemma 3.
Proposition 1 and the displayed congruences are unchanged.
The earlier reading did not include these restored hypotheses; its historical inspection scope is not enlarged.
