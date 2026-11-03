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


The [retained primary paper](../../../literature/pdf/AD99--published.pdf) identify this exact edition.
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

<a id="complete-salem-packet-specialization"></a>
### Direct complete-Salem-packet specialization

Let alpha>1 be a genuine Salem number of original degree d=2t>=4 and total measure m=log alpha.
Let L be its normal closure and choose one root beta_j from each of its t distinct inverse pairs.
Every beta_j is an algebraic integer unit with h_abs(beta_j)=m/(2t).
The tuple is multiplicatively independent without a normal-trace or full-kernel hypothesis.
Indeed, for a relation product_j beta_j^(a_j)=1 and a selected index i, send beta_i to alpha by an automorphism of L.
Every other selected root goes to a circle root, since inverse pairing is preserved and the selected pairs are distinct.
Taking absolute values gives alpha^(a_i)=1, hence a_i=0; repeat for every i.

The selected roots and their inverses contain all roots, so Q(beta_1,...,beta_t)=L.
Thus the actual joint degree is D=[L:Q], not d, and D<=2^t t! from the faithful inverse-pair permutation action.
For actual full signed-symmetric root action C2 wreath S_t, equality holds: D=2^t t!.
At t>=3 this is a genuine high-subdegree benchmark: the off-pair subdegree is d-2, and the actual trace field of degree t is not Galois because its S_(t-1) stabilizer is not normal in S_t.
These are conditional counts on that actual root action, not a new field realization or an assertion that every Salem polynomial has that group.

The packet's logarithmic geometry is sparse but pays an exact rank factor.
At every embedding of L exactly one selected coordinate has logarithmic absolute value +m or -m and all other coordinates have logarithmic absolute value zero.
Each chosen beta_j takes each original root value at exactly D/d embeddings.
Consequently

    h(1:beta_1:...:beta_t)=m/2,
    sum_j h_abs(beta_j)=m/2,
    max_j h_abs(beta_j)=m/(2t).                         (2)

More generally, for every integer vector a=(a_1,...,a_t), the same complete embedding count gives

    h_abs(product_j beta_j^(a_j))
      =(m/(2t)) sum_j |a_j|.                           (3)

All finite-place terms are zero because these are units.
Thus the disjoint logarithmic supports do not permit replacing projective height m/2 by the maximum coordinate height m/(2t).
Equations(2)--(3) are direct finite embedding calculations for this application, not a source theorem with an assumed rank-uniform constant.

Applying(1) with the actual n=t gives

    m >= 2t c_prod(t)^(1/t) D^(-1/t)
             [log(3D)]^(-kappa(t)).                   (4)

In the full-group benchmark the degree-only prefactor is

    2t/(2^t t!)^(1/t)=t/(t!)^(1/t),

which stays between 1 and e and tends to e.
This favorable factorial cancellation does not remove either c_prod(t)^(1/t) or the logarithmic loss with kappa(t).
One may always replace the unspecified positive c_prod(t) by min(c_prod(t),1); with that legitimate guaranteed choice the recorded bound's right side tends to zero because the logarithmic loss grows without bound.
This does not bound the optimal possible source constant from above; it says that the inspected theorem supplies no uniform compensating lower estimate for it.
The separately explicit Del09 substitution below gives a fully numerical failure without any unknown-constant issue.

### Exact missing input and the bounded stop

A sufficient new estimate on the actual full signed-symmetric Salem packets would be a constant c>0, independent of t and the input, such that

    D product_j h_abs(beta_j) >= c^t.                  (5)

No such assertion follows from(1).
On this benchmark(5) is quantitatively equivalent, up to an absolute factor e, to a uniform Salem measure gap on that very class.
Indeed its left side is m^t t!/t^t, so(5) gives m>=c t/(t!)^(1/t)>=c.
Conversely a measure gap m>=delta gives that left side at least(delta/e)^t, using t!>=(t/e)^t.
Thus(5) is a substantive new height theorem, not a cheap additional group hypothesis or a source-constant substitution.
The ordinary rank-two result cannot cover this near-linear off-pair subdegree by its fixed sublinear-power criterion, while fixed-rank conclusions cannot silently use n=t.

The bounded feasibility test is complete: the exact current source penalties do not produce a positive degree-uniform bound from the full packet.
No parameter search, group construction, projection computation or source-proof reconstruction is warranted by this substitution alone.
Further work on(5) would need a genuinely new proof using the complete sparse logarithmic geometry, with total logarithmic penalty O(t); the present source screen supplies no such proof.
The separate original-projection frontier remains an independent question; neither the old Newton Toeplitz identities in L9/L10 nor C161's incomplete coefficient-field orbit is a substitute arithmetic upper bound.
No C, T, E or S decision is changed by this source unit.
