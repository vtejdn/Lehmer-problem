---
author: Yin
---

# G0001: the adjoint ratio spectrum, degree amplification and the subgroup boundary

Date: 2026-10-07.

The complete mathematical proof is now retained in [C236](../claims/Yin_C_G0236_v1.md#adjoint-degree-amplification).
This original dated input remains available with its full mathematics; formal review accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-adjoint-subgroup-author-finding).
Bounded direct assessment by assigned AI assess_shortness_route for Yin.
The coordinating AI proposed the adjoint route and supplied the reciprocal-core invariant subgroup below.
No new source, numerical scan or computational certificate is used.

The unnormalized reduced-adjoint entropy already has finite sublevel sets on irreducible nontorsion units.
It therefore cannot carry a hypothetical sequence of original entropies tending to zero.
Dividing this entropy by the original degree restores an equivalent gap question, with constants differing by at most two.
Nevertheless, for reciprocal inputs the reduced adjoint flow contains the original squared flow as an actual invariant subgroup.
The finite-sublevel assertion concerns the whole adjoint family, not its subgroup closure.

## Inputs and source boundary

Let alpha be a nontorsion algebraic unit of degree d>=2, with monic irreducible polynomial P and distinct conjugates alpha_1,...,alpha_d.
Write m=log M(P)>0 and Delta=|disc P|.
Where periodic counts or the all-power class are used, assume deg(alpha^n)=d for every n>=1.
The existence reduction to such endpoints is [L G0059](Yin_L_G0059_v1.md#all-positive-power-existence-descent).
It does not say that each original input already has this property.

The only analytic arithmetic bound used is the accepted external Dobrowolski statement recorded in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md): there are absolute c>0 and d_0>=3 such that every nonzero nontorsion algebraic integer of degree d>=d_0 satisfies

    m >= c (log log d / log d)^3.                       (1)

No explicit choice of c or d_0, Voutier refinement, or proof of the original theorem is adopted here.
The source audit also supplies the elementary coefficient bound |a_j|<=binom(d,j) M(P) and Kronecker's measure-one characterization.
The entropy/Mahler identification uses the accepted rational formula of [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) and the rationalization interface of [DGB16-U001](../audits/literature/DGB16/Yin_U001.md#dgb16-u001).
The finite-index identity below is the proved [powered-order formula](Yin_L_G0059_v1.md#powered-order-index).

<a id="adjoint-ratio-spectrum"></a>
## An integral reduced adjoint flow

Set D=d(d-1) and

    R(t)=product_(i!=j)(t-alpha_i/alpha_j).

Each ratio is an algebraic integer because alpha_j is a unit.
The multiset is Galois invariant, so R is monic in Z[t]; paired inverse ratios give constant term 1.
Its degree is D.
Thus its companion matrix is unimodular and defines a free integral flow of rank D.

There is also a literal adjoint realization.
On O=Z[alpha], let A be multiplication by alpha.
Conjugation T -> A T A^(-1) acts invertibly on End_Z(O), with eigenvalues alpha_i/alpha_j for all i,j.
Its fixed lattice C is saturated, being the kernel of an integral homomorphism.
It has rank d: over Q, a commuting operator is determined by its value on the cyclic vector 1, so the centralizer consists of multiplications by elements of Q(alpha).
The quotient End_Z(O)/C is free of rank D, is invariant in both time directions, and its characteristic polynomial is R.
In particular it has the same algebraic entropy as the companion flow.
Denote this entropy by h_ad.

The full adjoint action has d eigenvalues 1.
Its periodic determinant is always zero.
All nonzero periodic determinants below belong to the reduced quotient or to the companion of R, not the full adjoint action.

Finally, R has a root of unity exactly when some distinct alpha_i, alpha_j have equal positive powers.
By the embedding-fiber identity in L G0059, this is equivalent to deg(alpha^n)<d for some n>=1.
Thus the all-power hypothesis is precisely what excludes cyclotomic roots from this reduced ratio polynomial; R can still be reducible and have repeated noncyclotomic roots.

<a id="adjoint-degree-amplification"></a>
## Exact entropy comparison and finite sublevel sets

Put x_i=log|alpha_i|.
Since alpha is a unit, sum_i x_i=0, and m=(1/2)sum_i |x_i|.
The ratio spectrum gives

    h_ad = sum_(i<j) |x_i-x_j|,
    d m <= h_ad <= 2(d-1)m.                            (2)

For the lower inequality, the triangle inequality gives

    2h_ad=sum_(i,j)|x_i-x_j|
          >=sum_i |sum_j(x_i-x_j)|
          =d sum_i|x_i|=2dm.

For the upper inequality, each |x_i| appears in d-1 unordered pairs.
These comparisons require neither reciprocity nor power-degree preservation.
The upper constant is attained when the log-moduli are x,-x,0,...,0, as for a Salem input.

For every real H, only finitely many monic irreducible nontorsion unit polynomials P have h_ad<=H.
Indeed, (1)--(2) imply for large d that

    h_ad >= c d (log log d / log d)^3 -> infinity.      (3)

Thus d is bounded on such a sublevel set.
Then M(P)<=exp(H/d), and the integer coefficient bound gives only finitely many P.
In particular the unnormalized adjoint family has an attained positive minimum.
To see attainment without any compactness assertion, choose one input and minimize over its finite, nonempty entropy sublevel set; all other inputs have larger entropy.

Any hypothetical sequence m(P_j)->0 has d_j->infinity: a bounded degree and, eventually, M(P_j)<=2 would give finitely many polynomials with positive measure.
Equation (3) therefore yields h_ad(P_j)-> infinity.
More generally, an infinite sequence of distinct such minimal polynomials eventually leaves every bounded adjoint-entropy sublevel set.
This conclusion is unconditional and does not decide whether the original sequence with m(P_j)->0 exists.

<a id="normalized-adjoint-equivalence"></a>
## The normalization that restores the original problem

For a(P)=h_ad(P)/d, (2) becomes

    m(P) <= a(P) <= 2(1-1/d)m(P) < 2m(P).             (4)

On any chosen class of these inputs, a uniform positive lower bound for a is equivalent to one for m: a>=epsilon implies m>=epsilon/2, and m>=epsilon implies a>=epsilon.
Vanishing sequences and convergence of positive series of these quantities are equivalent by the same comparison.
On all-power-stable units this is an equivalent gap question, not a new uniform bound.
By the existence descent in L G0059, the infimum of positive m is unchanged on passing from all nontorsion units to this endpoint class.

The division in (4) is by the original degree d, not the rank D of the reduced flow.
Normalizing by that rank instead gives

    m/(d-1) <= h_ad/D <= 2m/d,

which is comparable to the absolute logarithmic height m/d.
Neither normalization is automatically the ordinary algebraic entropy of a new integral flow; it must be stated explicitly.

<a id="reciprocal-adjoint-subgroup"></a>
## The reciprocal core reappears as an actual invariant subgroup

Suppose in addition P is reciprocal.
The map sigma:alpha->alpha^(-1) is an involutive field automorphism of K=Q(alpha).
It preserves O: alpha^(-1) belongs to O because alpha is a unit, and applying sigma again gives equality sigma(O)=O.
For z in O let m_z be multiplication by z and define

    W={m_z sigma:z in O} subset End_Z(O).

This is a free rank-d subgroup, and direct composition gives

    Ad_A(m_z sigma)=m_(alpha^2 z) sigma.                (5)

Moreover W intersects C trivially.
Commuting m_z sigma with m_alpha would give z(alpha-alpha^(-1))=0; nontorsion excludes alpha=alpha^(-1), so z=0.
Hence W embeds in the reduced adjoint quotient as an actual invariant subgroup isomorphic to multiplication by alpha^2 on O.
Its entropy is exactly 2m: the full degree-d powered polynomial has roots alpha_i^2 and its logarithmic measure is 2m, including any powering multiplicities.
Under the all-power assumption this powered polynomial P^[2] is itself irreducible of degree d.

Equivalently, the ordered pair (alpha_i,alpha_i^(-1)) contributes alpha_i^2 to R, so P^[2] divides R in Z[t].
This also confirms the entropy contribution directly.
No assertion that the image of W is primitive, or that the integral flow splits as a direct sum, is made.

Consequently the positive gap and finite sublevels for whole adjoint flows supply no logical inference of the corresponding properties for their invariant-subgroup closure.
This is not an unconditional counterexample to a subgroup entropy gap.
If small original reciprocal entropies existed, (5) would give small subgroup entropies 2m inside whole adjoint flows whose entropy tends to infinity.
Using an entropy addition theorem must preserve this distinction; monotonicity only bounds the subgroup entropy above by the whole.

<a id="adjoint-periodic-index-boundary"></a>
## Finite periodic counts retain an arithmetic question

Assume all positive powers preserve degree and let B be either reduced-adjoint matrix above.
For n>=1, the finite number of fixed points of its dual toral automorphism is

    F_n=|det(B^n-I)|
       =product_(i!=j)|(alpha_i/alpha_j)^n-1|
       =|disc P^[n]|=Delta I_n^2,                     (6)

where I_n=[Z[alpha]:Z[alpha^n]].
The toral fixed-point formula follows from the lattice index of the nonsingular integer map B^n-I.
In the product, the denominator has absolute value |Norm(alpha)|^(n(d-1))=1, and the numerator pairs into the powered discriminant.
This proves (6) without an entropy limit theorem.

The elementary bound |z^n-1|<=2 max(1,|z|)^n gives, for every n,

    log Delta+2log I_n <= n h_ad+D log 2,
    m >= [log Delta+2log I_n-D log 2]/[2n(d-1)].       (7)

Thus an adequately strong lower estimate for the actual indices could provide a finite Mahler certificate.
Integer positivity F_n>=1 or I_n>=1 alone does not supply such an estimate; (7) retains both its quadratic degree cost D log2 and the factor n(d-1).
In fact the ordinary d by d powered Vandermonde estimate already replaces D log2 in (7) by d log d, which is no larger.
The direct proof and full integral quotient/torsion structure are retained in [L G0061](Yin_L_G0061_v1.md#adjoint-normalized-target-boundary).
Thus forming the ratio-spectrum flow does not improve this finite certificate for the same index input.

There is an elementary asymptotic identity at limsup scope:

    limsup_(n->infinity) (log F_n)/n=h_ad,
    limsup_(n->infinity) (log Delta+2log I_n)/(nd)=a(P). (8)

The upper bound follows from (7).
For the lower bound, collect the finitely many unit-circle eigenvalues into a vector z in a torus.
None is 1.
There are integers q_j->infinity with z^(q_j)->1: compactness supplies powers with arbitrarily small positive return, and if their exponents stayed bounded some fixed positive power would be exactly 1; in that finite-order case its multiples also give unbounded returns.
Thus z^(q_j+1)->z, where every coordinate differs from 1.
Along n_j=q_j+1 all the unit-circle logarithmic factors stay bounded.
Each remaining eigenvalue rho satisfies log|rho^n-1|/n->log^+|rho|.
Summing proves the lower limsup.
If there are no unit-circle eigenvalues, the ordinary limit follows directly.

For algebraic unit-circle eigenvalues, this elementary argument establishes only the limsup.
The complete fixed-input limit is available at the accepted War05/Baker scope reused in [L G0061](Yin_L_G0061_v1.md#adjoint-index-growth); its additional Diophantine input is not reproduced here.
Both versions are pointwise in P and supply no convergence rate uniform in d or P.
Their degree-normalized value is already the equivalent quantity (4).
Equations (6)--(7) leave actual finite order-index growth as a possible arithmetic input, but entropy amplification, integrality and a fixed-flow asymptotic alone do not provide the missing uniform estimate.

## Verification and limits

Original drafting, actual subgroup contribution and remaining whole-review accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-adjoint-subgroup-author-finding).
The original 2026-10-07 date, actual contributions and full check scopes remain there, with current finding-specific relationships.
No new source, computation, uniform arithmetic estimate or resolution of G0001 is asserted.
