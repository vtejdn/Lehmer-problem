---
author: Yin
---

# Trace-dual toral coding, exact bilateral Fourier product and convolution boundary

This retains the complete original2026-10-07 [L104 proof](../ledger/Yin_L_G0104_v1.md).
The assigned review_matrix_completion agent authored the reconstruction; the coordinator contributed the convolution-power interpretation.
The companion multiplier cap is a separate proved input, not an uninspected source.
The exact old complete checks and limited companion-input check remain in the formal review linked by L104.
No source, computation or Task is newly executed.

## Statement

Let alpha be an algebraic unit, P monic irreducible of degree d,with no conjugate of modulus1,and m=log M(P)>0.
Fix any full order R in K=Q(alpha) containing Z[alpha],so alpha and alpha^(-1) belong to R.
Use the real trace pairing on K_infty=R^r times C^s,
[theta,x]=sum_real sigma(theta)x_sigma+2Re sum_complex sigma(theta)x_sigma.
Its complex covector is(2Re sigma(theta),-2Im sigma(theta)).
Let R^vee be its trace dual and X_R=K_infty/R^vee.
R^vee is a full lattice in K,contains R,and the complete character lattice of X_R is exactly R.
Multiplication by alpha induces a toral automorphism T.

With stable and expanding projections e_s,e_u,let h=[e_s1].
For j>=0 use r_j=A^j e_s1;for j<0 use r_j=-A^j e_u1.
The series sum_(j in Z)xi_j r_j converges uniformly over all two-sided fair-sign sequences.
Its quotient defines a continuous coding kappa and a T-invariant mixing probability nu_R.
The exact seam discrepancy is A r_-1-r0=-1 in R^vee.

For every theta in R,the signed Fourier coefficient is

    nuhat_R(theta)=product_(j>=0)cos(2pi u_j(theta))
       product_(j<0)cos(2pi v_j(theta)),
    abs(nuhat_R(theta))=c_P(theta).

For every nonzero theta it satisfies0<c_P(theta)<1.
Invariance and mixing give

    nuhat_R(alpha^n theta)=nuhat_R(theta), n in Z,
    nuhat_R(alpha^n theta+psi) tends to nuhat_R(theta)nuhat_R(psi).

The support is exactly the compact coding image.
Its differences generate a dense subgroup,so it is not contained in a coset of a proper closed subgroup; full torus support is not asserted.
The measure is non-atomic and non-Haar.
Its measure entropy satisfies h_(nu_R)(T)<=log2 by a complete finite-cylinder/partition proof.
No equality with the original finite algebraic-sum rate h1 or Mahler entropy m is asserted by this theorem.

For every integer k>=1,nu_R^(star k) remains invariant,mixing,non-atomic,non-Haar and has support differences generating a dense subgroup on the same actual automorphism.
The actual arithmetic recurrence cap q_P=cos(pi/norm(P)_1)<1 yields

    0<abs(nuhat_R^(star k)(theta))<=q_P^k for theta!=0,
    sup_(theta!=0)abs(nuhat_R^(star k)(theta))<=q_P^k tends to0.

Thus those generic dynamical properties force no uniform optimized Fourier amplitude floor.
The convolution changes the digit law to k independent signs per time; it is not an original-binary counterexample.
The order torus is distinct from the original rational additive flow.
The absolutely summable hyperbolic coding and seam do not give a unit-circle/Salem extension.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:13 |
| status | open |
| reason | Complete original full-order trace-dual, bilateral coding, Fourier/mixing and same-automorphism convolution proof retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire arbitrary full-order trace-dual toral coding and exact signed Fourier theorem, mixing/support/nonatom/entropy-factor properties and same-automorphism convolution cap, preserving changed-digit, rational-flow and hyperbolicity limits. |
| argument | [Complete argument](#argument) | Full original1–8: integral trace matrix/double dual, exact complex covectors and seam, uniform two-sided convergence/factor mixing, all Fourier nonzero/strict guards, Vandermonde support and atom arguments, finite-cylinder/Fano entropy cost and every convolution property. |
| dependency | [Actual integral-multiplier recurrence cap](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) | Exact uniform cos(pi/norm(P)_1) cap for every nonzero O_K multiplier and hence every theta in R; no quantitative cap is inferred merely from pointwise c_P(theta)<1. |
| support | [Unit-circle same-witness obstruction](Yin_C_G0297_v1.md#unit-circle-trace-witness-decay) | Exact prior trace-frequency exponential obstruction at positive measure, only to delimit the absent neutral-coordinate extension of this hyperbolic construction. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:17 |
| status | proved |
| reason | Adopt the whole original arbitrary-full-order trace-dual coding/Fourier/mixing/support/entropy-factor and same-automorphism convolution proof after actual complete self-review; retain the changed digit law, no entropy equality, actual arithmetic cap and hyperbolic/rational-flow limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire arbitrary full-order trace-dual toral coding and exact signed Fourier theorem, mixing/support/nonatom/entropy-factor properties and same-automorphism convolution cap, preserving changed-digit, rational-flow and hyperbolicity limits. |
| argument | [Argument](#argument) | Full original1–8: integral trace matrix/double dual, exact complex covectors and seam, uniform two-sided convergence/factor mixing, all Fourier nonzero/strict guards, Vandermonde support and atom arguments, finite-cylinder/Fano entropy cost and every convolution property. |
| dependency | [Dependency](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) | Exact uniform cos(pi/norm(P)_1) cap for every nonzero O_K multiplier and hence every theta in R; no quantitative cap is inferred merely from pointwise c_P(theta)<1. |
| support | [Support](Yin_C_G0297_v1.md#unit-circle-trace-witness-decay) | Exact prior trace-frequency exponential obstruction at positive measure, only to delimit the absent neutral-coordinate extension of this hyperbolic construction. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-toral-coding-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:59 |
| status | proved |
| reason | Adopt the actual fresh complete mathematical review, formed before the full old-account comparison, at every original statement/proof/necessary-input boundary. Preserve all old decisions and self/unknown facts; no substantive repair, source-depth expansion or unrestricted completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire arbitrary full-order trace-dual toral coding and exact signed Fourier theorem, mixing/support/nonatom/entropy-factor properties and same-automorphism convolution cap, preserving changed-digit, rational-flow and hyperbolicity limits. |
| argument | [Argument](#argument) | Full original1–8: integral trace matrix/double dual, exact complex covectors and seam, uniform two-sided convergence/factor mixing, all Fourier nonzero/strict guards, Vandermonde support and atom arguments, finite-cylinder/Fano entropy cost and every convolution property. |
| dependency | [Dependency](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) | Exact uniform cos(pi/norm(P)_1) cap for every nonzero O_K multiplier and hence every theta in R; no quantitative cap is inferred merely from pointwise c_P(theta)<1. |
| support | [Support](Yin_C_G0297_v1.md#unit-circle-trace-witness-decay) | Exact prior trace-frequency exponential obstruction at positive measure, only to delimit the absent neutral-coordinate extension of this hyperbolic construction. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0541_v1.md#current-toral-coding-finding) | Exact current statement, complete original retained proof and all selected interfaces, self-reviewed; every historical finding keeps its own old input, scope and relationship. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0548_v1.md#f-g300) | Entire actual statement and complete original proof independently inspected, with exact domains, all useful old whole/partial obligations, original source-depth, failed comparisons, costs and limit order; no new mathematical experiment or reconstructed historical isolation. |


## Complete retained argument

<a id="argument"></a>
Let alpha be an algebraic unit with monic irreducible polynomial P of degree d, with no conjugate on the unit circle and m=log M(P)>0.
Fix a full order R in K=Q(alpha) containing Z[alpha].
Thus alpha and alpha^(-1) belong to R.
One may take either R=Z[alpha] or the full ring of integers O_K; the latter includes every integral multiplier in K.
These choices may have different character lattices and are not silently identified.

<a id="trace-torus-dual-normalization"></a>
### 1. The trace dual fixes the lattice and every complex sign

Write K_infty=K tensor_Q (the real field)=R^r x C^s, where R^r here denotes real coordinates and not the order R, with one representative of each nonreal embedding pair.
Its real trace pairing is

    [theta,x]=sum_real sigma(theta)x_sigma
                  +2 Re sum_complex sigma(theta)x_sigma.

For sigma(theta)=a+ib and x_sigma=u+iv, the corresponding Euclidean covector is (2a,-2b), because the product contributes 2(au-bv).
There is no implicit complex conjugation in this trace pairing.

Define the order codifferent and the torus by

    R^vee={x in K_infty:[theta,x] in Z for every theta in R},
    X_R=K_infty/R^vee.

The trace matrix in an integral basis of R is an integral nonsingular matrix.
Hence R^vee is a full lattice, R is contained in R^vee, and the double trace dual of R is R itself.
In particular the complete character group of X_R is exactly R, with

    chi_theta([x])=exp(2pi i[theta,x]),  theta in R.       (1)

This also proves that the displayed definition of R^vee gives elements of K, not extra real vectors: its coordinates are the inverse rational trace matrix applied to integer vectors.
The nonsingularity follows from separability and the embedding matrix.
No maximal-order assumption is needed.

Multiplication by alpha preserves R^vee in both directions, since [theta,alpha x]=[alpha theta,x] and alpha R=R.
It induces a toral automorphism T, whose dual action on the characters is theta -> alpha theta.
If R=Z[alpha], (1) does not by itself represent every multiplier in O_K; choosing R=O_K does.

<a id="bilateral-homoclinic-sign-coding"></a>
### 2. An absolutely convergent two-sided coding

Let e_s and e_u be the coordinate projections onto the stable and expanding embedding coordinates, and let A be multiplication by alpha on K_infty.
Hyperbolicity gives e_s+e_u=I.
The point

    h=[e_s 1] in X_R

is homoclinic.
For nonnegative j use the representative r_j=A^j e_s1; for negative j use r_j=-A^j e_u1.
These represent A^j h, since A^j1 belongs to R, which is contained in R^vee.
Their norms decay geometrically in the corresponding directions, so sum_(j in Z)||r_j|| is finite.

For a two-sided fair-sign sequence xi define

    kappa(xi)=[sum_(j in Z) xi_j r_j],
    nu_R=kappa_*(fair Bernoulli product law).             (2)

The convergence is uniform over all sign sequences.
Thus kappa is a continuous map from the compact product space into X_R.
If (sigma xi)_j=xi_(j-1), then

    T kappa(xi)=kappa(sigma xi).                         (3)

Indeed A r_j=r_(j+1) except at j=-1, where A r_-1-r_0=-1.
The discrepancy is therefore -xi_-1 times 1, an element of R^vee.
This explicitly checks the sign and the single crossing of the stable/expanding seam.

Consequently nu_R is T-invariant and mixing.
For completeness, the Bernoulli shift is mixing because functions of finitely many coordinates become independent after sufficiently large shifts; approximation by such functions in L2 extends this to all bounded measurable functions.
Pullback by the measurable factor kappa proves the same mixing property for nu_R.
No external coding theorem is used.

<a id="toral-bilateral-fourier-identity"></a>
### 3. The exact coefficient and its basic constraints

For theta in R put

    u_j(theta)=sum_stable sigma(theta) sigma(alpha)^j,
    v_j(theta)=sum_expanding sigma(theta) sigma(alpha)^j,

including both members of complex pairs.
These numbers are real and u_j+v_j=Tr_(K/Q)(theta alpha^j) is integral for every integer j.
Independence in (2) and uniform convergence give

    nuhat_R(theta)
      =product_(j>=0) cos(2pi u_j(theta))
         product_(j<0) cos(2pi v_j(theta)),
    |nuhat_R(theta)|=c_P(theta).                         (4)

The minus sign in r_j for j<0 disappears in the cosine.
Thus the integer-multiplier product is the Fourier coefficient of an actual invariant probability measure, with the exact normalization used by the trace witness.

Every finite cosine factor is nonzero.
Each trace subsum is an algebraic integer; a cosine zero would make it a nonintegral rational in 1/4+(1/2)Z.
The tails are positive in absolute value because their arguments decay geometrically, and the sum of their squares converges.
Hence

    0<c_P(theta)<1 for every nonzero theta in R.         (5)

To justify the strict upper inequality, if all stable-side factors had absolute value 1 then u_j(theta) would lie in (1/2)Z for all j>=0.
Since it tends to zero, it would eventually vanish.
A Vandermonde matrix on the distinct stable conjugates then forces every stable coefficient sigma(theta) to vanish, impossible for theta!=0.
There is at least one stable coordinate because alpha is a unit and m>0.

Invariance and mixing now supply exact additional identities:

    nuhat_R(alpha^n theta)=nuhat_R(theta) for n in Z,
    nuhat_R(alpha^n theta+psi)
        ->nuhat_R(theta)nuhat_R(psi) as n->infinity.      (6)

The second is just the mixing identity applied to two characters, with no complex conjugation in the displayed product.
It implies the analogous limit for absolute values.
It does not say that all large character coefficients tend to zero: the first identity already prevents that along each nonzero alpha orbit.

<a id="coding-support-and-nonatomicity"></a>
### 4. Support, nonatoms, and an entropy bound with its limit

The support is exactly the compact image kappa({-1,1}^Z), since every cylinder has positive Bernoulli probability.
It need not be replaced by the whole torus.
Nevertheless its differences generate a dense subgroup.
Flipping one digit gives 2A^j h as a difference of two support points.
A character annihilating all these differences would satisfy 2u_j(theta) in Z for all j>=0.
Stable decay and the same Vandermonde argument force theta=0.
Characters separate closed subgroups of a finite-dimensional torus, so the subgroup generated by the differences is dense.
In particular the support is not contained in a coset of a proper closed subgroup.
This is not a proof that the support itself is all of X_R.

The law is non-atomic.
If a mixing invariant probability under an invertible map has an atom of mass p>0, that atom has a finite periodic orbit, because all its orbit atoms have the same mass.
Along multiples of the period, mixing applied to the atom's indicator gives p=p^2.
The law would therefore be a point mass.
That is impossible by (5), since a point mass has modulus-one Fourier coefficients.
The law is also not Haar, since all its nontrivial Fourier coefficients are nonzero.

Its measure entropy obeys h_(nu_R)(T)<=log2 as a direct factor bound.
One proof is to pull back any finite partition with q>=2 atoms to the sign space and approximate it by a partition depending on coordinates [-b,b], with conditional entropy error at most epsilon.
This approximation exists by finite-cylinder approximation of measurable sets; its error bound follows by conditioning on the disagreement event, at cost at most h_bin(p)+p log(q-1).
The one-atom partition is trivial.
The n-block entropy is then at most (n+2b)log2+n epsilon.
Divide by n and let epsilon tend to zero, then take the supremum over finite partitions.

No equality between this measure entropy, the finite algebraic-sum entropy rate h_1, or the Mahler entropy m is asserted.
Such an equality is not needed for (4)--(6), and a compact factor of the two-sided sign process does not supply it automatically.
The torus here is dual to the integral order R, not to the original rational additive flow on K.

<a id="same-torus-convolution-fourier-boundary"></a>
### 5. Invariance and mixing alone cannot force a large optimized coefficient

Let

    c_R^*=sup_(theta in R, theta!=0)c_P(theta).

The integer-recurrence argument in the companion [multiplier note](Yin_C_G0298_v1.md#uniform-multiplier-recurrence-cap) proves, for every nonzero multiplier in O_K and hence in R,

    c_P(theta)<=q_P:=cos(pi/||P||_1)<1.                 (7)

Here ||P||_1>=3 in the present nontorsion unit domain.
That proof is a genuine arithmetic input: rounding the bilateral recurrence within distance 1/||P||_1 forces an integer recurrence error of absolute value less than one, hence zero; boundedness in both time directions and hyperbolicity then force the multiplier to vanish.
We reuse its proved cap, rather than obtaining a quantitative cap merely from the pointwise strict inequalities (5).

For k>=1 form nu_R^(star k), the distribution of the sum of k independent coded points.
It is still T-invariant and mixing: apply the coding to k independent Bernoulli sequences and then add in the torus.
Its Fourier coefficients satisfy

    nuhat_R^(star k)(theta)=nuhat_R(theta)^k,
    0<|nuhat_R^(star k)(theta)|<=q_P^k for theta!=0,
    sup_(theta!=0)|nuhat_R^(star k)(theta)|<=q_P^k->0.    (8)

Every member is non-Haar and non-atomic, by the same arguments above, and its support differences still generate a dense subgroup.
All this occurs on the SAME actual hyperbolic toral automorphism.
Thus invariance, mixing, non-Haar behavior, nonatoms and absence of a proper supporting subgroup do not force a uniform positive lower bound on the optimized Fourier amplitude.

The digit law has changed: the kth convolution uses a sum of k independent fair signs at each time.
It is not the original fair-binary law and is not a counterexample to a lower bound restricted to c_P(theta) for that law.
It isolates exactly why the digit-specific arithmetic must remain in any attempt to compare an optimized coefficient with the cubic Mahler deficit.
No existence or nonexistence assertion for small positive Mahler measures follows.

The construction requires hyperbolicity.
With unit-circle conjugates the stable-plus-expanding seam need not differ by a lattice vector, and the absolutely summable homoclinic series above does not cover the missing neutral coordinates.
The separate unit-circle trace-witness obstruction in L G0102 remains in force; no Salem extension is inferred from this torus model.
