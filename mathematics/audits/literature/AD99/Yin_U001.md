---
author: Yin
---
# AD99-U001: higher-rank height products and the complete Salem packet boundary

Date: 2026-10-18T12:03.
Human record author Yin.
The angular_envelope_review AI performed this bounded primary-source and applicability check under root's continuing G0001 assignment.
This is source reading and direct specialization, not a new Claim or an independent review of the original proof.

<a id="ad99-u001"></a>
## Read; accepted statement and bounded application check

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and Sinnou David, Le probleme de Lehmer en dimension superieure, Journal fur die reine und angewandte Mathematik 513 (1999), 145--179; actual published 35-page institutional copy.

Passages: Printed145--148/PDF1--4: height normalization, Definition1.2, Conjectures1.3--1.4 for distinction, and the complete Theorems1.5--1.6 statements with the displayed kappa(n).

Inspection: These complete pages were visually read because the retained PDF's embedded text is misencoded. Theorem1.6's hypotheses, all exponent positions, joint-degree convention and the Salem substitution below were checked. No original proof, effective value of c(n), whole-paper audit or uniform-rank theorem is claimed.


The [retained primary paper](../../../literature/pdf/AD99--published.pdf) identifies this exact edition.
The established Theorem1.6 is accepted for use at this statement/applicability scope.
It refines the source information behind [AM16's fixed-rank comparison](../AM16/Yin_U005.md); it does not replace that unit's own inspection or the stronger relative theorem in [Del09-U001](../Del09/Yin_U001.md#del09-u001).

<a id="ad99-height-obstruction-conventions"></a>
### Exact height and obstruction conventions

For a nonzero algebraic number x, h_abs(x) is the absolute logarithmic Weil height, with finite places and the usual local-degree weights.
It equals the total logarithmic Mahler measure of its primitive integer minimal polynomial divided by its degree.
For a tuple x=(x_1,...,x_n), the source's h(x) is the projective height of (1:x_1:...:x_n), not max_i h_abs(x_i) and not their product.
Explicitly, in any number field K containing the coordinates, it is the sum over places of [K_v:Q_v]/[K:Q] times log max(1,|x_1|_v,...,|x_n|_v), with the consistent standard absolute-value normalization.
The source records h(x)<=sum_i h_abs(x_i).
Its Definition1.2 sets delta(x) to the least total degree of a nonzero rational polynomial vanishing at x, equivalently the least degree of a rational hypersurface containing x in the stated torus embedding.
It has 1<=delta(x)<=n D^(1/n), where D=[Q(x_1,...,x_n):Q].
Theorem1.6 below uses D directly, so no obstruction-index estimate is substituted into its product bound.

### Exact selected statement

For every fixed integer n>=1 there exists c_prod(n)>0 such that, for every tuple of multiplicatively independent nonzero algebraic numbers x_1,...,x_n,

    product_(i=1)^n h_abs(x_i)
      >= c_prod(n)/D * [log(3D)]^(-n kappa(n)),
    D=[Q(x_1,...,x_n):Q],
    kappa(n)=(n+1)((n+1)!)^n-n.                         (1)

Here multiplicative independence means that product_i x_i^(a_i)=1 with integers a_i forces all a_i=0.
The source writes c(n) in both Theorems1.5 and1.6; this unit uses c_prod(n) for the latter and does not identify the two constants.
Theorem1.5 concerns projective height and the obstruction index, with logarithmic exponent kappa(n); Theorem1.6 has exponent n kappa(n) on the PRODUCT of coordinate heights.
The inspected statement supplies existence of c_prod(n), not an explicit uniform lower bound as n grows.
The rapidly growing kappa(n) is printed explicitly and cannot be discarded when taking n-th roots.
Neither adjacent conjecture is accepted as a theorem.

## Fixed complete-packet comparison

The complete project-specific packet embedding count, joint-degree/full-group benchmark, height equations, factorial cancellation and conditional-gap equivalence are retained in [C165's unselected complete-packet comparison](../../../claims/Yin_C_G0165_v1.md#complete-salem-packet-specialization).
The already fixed [C165 inverse-pair independence and exact monomial heights](../../../claims/Yin_C_G0165_v1.md#off-pair-salem-ratio-proof) supply those reused facts.
This source unit owns the exact AD99 statement and inspection limits above; the fixed supplement adopts no new mathematical status, source-proof inspection or rank-uniform constant.
