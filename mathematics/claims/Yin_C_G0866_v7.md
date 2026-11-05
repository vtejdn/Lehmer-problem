---
author: Yin
---
# Mahler-preserving norm descent and finite raw-p2 attainment

This fixed result concerns every algebraic integer unit alpha>1 which occurs as the Mahler measure of an algebraic number, without a Salem-only restriction.
The coordinating root proposed testing the Dixon--Dubickas block mechanism against the actual-own-degree raw-p2 quantity.
The strategy_full_goal_reassessment contributor developed the membership-atom, relative-norm, Cauchy, binomial-degree and finite-attainment deductions below.
These are proof contributions, not independent review; the [selected whole assessment](#decision-whole-independent-review-2026-11-05) adopts this version using the [independent R1088 v7 finding](../audits/reviews/Yin_R_G1088_v7.md#block-descent-whole).

The compatible Galois block-product mechanism is attributed to Dixon--Dubickas; it is not claimed as a project invention.
The raw-M2-monotone reduction for every starting realization and its finite-infimum consequence are the local deductions proved here.
The adopted [v6 Cayley result](Yin_C_G0866_v6.md#decision-whole-independent-review-2026-11-05) and all earlier versions retain their exact fixed statements, assessments and source/review limits.
Neither that particular construction's obstruction nor its prior review is a premise or review of the present general inverse-measure result.
The extraction source is [D1's block inquiry](../drafts/Yin_D_G0001.md#p2-mahler-preserving-block-descent), which is provenance rather than a proof dependency.

<a id="source-scope"></a>
## Exact source comparison and retained limits

The inspected source is Dixon and Dubickas, [The values of Mahler measures, author manuscript dated 28 September 2004](../literature/pdf/DD04--author-20040928.pdf), 24 pages, at the [DD04-U001 scope](../audits/literature/DD04/Yin_U001.md#dd04-u001).
Theorem 1 on p.2 supplies the stated binomial existence bound; the basal definitions are on p.5; Lemma 3 and Theorems 4--5 with their selected proofs are on pp.6--8.
The source's large-root stabilizer and unit statements in Lemma 2 were also checked at their displayed scope, and the subset-count explanation in Corollary 8 was read as a comparison.
The original external ancestors and the complete paper were not audited.
The source supplies the block mechanism and the distinction between a globally basal object and a particular block construction.
The inspected passages do not supply the raw-M2 comparison or a raw-M2-monotone passage to a globally basal realization.
The argument needed for the stronger quantified reduction below is supplied explicitly, rather than inferred from Theorem 1's existence assertion.

The nearest existing project calculation is [C855 v2's ordinary norm descent](Yin_C_G0855_v2.md#raw-p-two-norm-descent).
Its power-collapse fibers have equal absolute values and give an exact raw-norm formula.
The present fibers need only stay on the same side of the unit circle, so the corresponding statement is the Cauchy inequality below.
[C866 v1](Yin_C_G0866_v1.md#statement) concerns radicals of monomials in Salem conjugates; merely lying in the Salem splitting field does not supply that multiplicative hypothesis.
These comparisons do not import a new statement about arbitrary units in a splitting field.

## Statement

Let alpha>1 be an algebraic integer unit of degree d which is a Mahler measure of an algebraic number, and let L_alpha be the normal closure of Q(alpha) over Q inside C.
For every nonzero algebraic beta with M(beta)=alpha, there exists an algebraic integer unit gamma such that

    gamma in Q(beta) intersect L_alpha,
    M(gamma)=alpha,
    deg(gamma)<=min{deg(beta), binom(d,floor(d/2))},
    M_2(gamma)<=M_2(beta).                                (BD1)

Every raw quantity uses its own actual algebraic degree and all places, as in C855 v2.
Explicitly, for nonzero zeta with own field K_zeta=Q(zeta) and degree D_zeta, set

    M_2(zeta)^2=D_zeta sum_v n_v (log|zeta|_v)^2,
    n_v=[(K_zeta)_v:Q_(v_0)].

The absolute values extend the ordinary rational absolute values, and a complex place has local degree two.
For units the finite terms vanish and this is D_zeta times the sum over all complex embeddings.
The proof first shows beta is a unit, so thereafter

    M_2(beta)^2=n sum_(i=1)^n log^2|beta_i|,
    n=deg(beta),

with all complex embeddings counted, including both members of every nonreal pair.
No degree-normalized Weil height or FM13 operator identity is substituted for this quantity.
The statement is not restricted to Salem alpha, although that is the immediate intended use.

For each fixed alpha, let F_alpha be the finite coefficient candidate set defined in [the attainment argument](#finite-raw-attainment).
Then the already displayed reduction also gives the exact finite-attainment conclusion

    inf_{beta: M(beta)=alpha} M_2(beta)
       =min_{q in F_alpha} M_2(any root of q).

Thus this infimum is attained in L_alpha at an actual degree at most binom(d,floor(d/2)).
The candidate set and bound depend on alpha; no uniform cheap realization or raw-monotone reduction to a globally basal polynomial is asserted.

<a id="argument"></a>
## Why the starting realization is already a unit

Let the primitive irreducible integer polynomial of beta have degree n, leading coefficient a_n and constant coefficient a_0, and let k be its number of roots of modulus greater than one.
Both coefficients are nonzero because beta is nonzero.
If k=0 or k=n, its Mahler measure is respectively |a_n| or |a_0|, an integer; an algebraic unit alpha>1 cannot be such an integer.
Thus 0<k<n.

In the splitting field F of beta, alpha is plus or minus a_n times the product of these k large roots.
Put N=[F:Q].
The Galois action counts every root equally often and gives

    |Norm_(F/Q)(alpha)|
       =|a_n|^(N-Nk/n) |a_0|^(Nk/n).                     (BD2)

The left side is one because alpha is a unit, and both exponents on the right are positive integers.
Hence |a_n|=|a_0|=1 and beta is an algebraic integer unit.
This is the elementary norm mechanism behind the relevant unit assertion of the source; it needs no uninspected external height estimate.

Replace beta by beta^(-1) if necessary so that its number k of large conjugates satisfies 1<=k<=n/2.
This is always possible: the numbers of positive and negative logarithmic moduli sum to at most n, and both are positive for a nontorsion unit.
Conjugates on the unit circle are counted in neither number.
For a unit, inversion preserves M, raw M_2, actual degree and the field Q(beta).
Write beta_tilde for the selected orientation, so the eventual intersection in (BD1) is unchanged.

<a id="membership-atoms"></a>
## Membership atoms give the coarsest compatible block system

Let Omega be the n distinct conjugates of beta_tilde in their splitting field F, G=Gal(F/Q), and Delta the subset of its k large roots.
Let Sigma be the d distinct conjugates of alpha in F.
Since F is normal and contains alpha, it also contains L_alpha.

Every automorphism fixing alpha preserves Delta.
Indeed alpha is a rational sign times the product of the roots in Delta, and among all k-element subsets that product has strictly largest absolute value at Delta: replacing a large root by a root of modulus at most one strictly decreases the absolute product.
Thus for each a in Sigma the set

    Delta_a=g Delta for any g with g(alpha)=a

is well defined.
The Galois action satisfies g Delta_a=Delta_(g a).
For xi in Omega define its membership subset

    Gamma_xi={a in Sigma: xi in Delta_a}.                 (BD3)

Partition Omega into the nonempty fibers B of the map xi->Gamma_xi; these will be called its membership atoms in this calculation.
The partition is G-invariant and Delta is a union of its atoms.
Conversely, any G-invariant partition of Omega for which Delta is a union of blocks must also make every Delta_a a union of blocks.
Each such block is therefore contained in a membership atom.
Thus the atom partition is the coarsest Galois block partition compatible with the original large-root set; this is a precise minimum within the block constructions of this particular beta_tilde.

Transitivity on Omega makes all atoms have the same size e and makes the action on the set of atoms transitive.
If there are b atoms, then n=eb.
For each atom B put delta_B=product_(xi in B) xi.
These products are pairwise distinct.
For a proof, equality of two products defines a G-invariant equivalence relation on atoms.
Each atom lies wholly in Delta or wholly outside it, and |delta_B|>1 holds exactly in the first case.
Merging equal-product atoms would therefore produce a strictly coarser G-invariant partition still compatible with Delta, contrary to the coarsest property just proved.

Consequently the delta_B are exactly the b conjugates of any one of them.
They are algebraic integer units, and their product polynomial is the monic irreducible minimal polynomial of degree b, with constant coefficient plus or minus one.
In particular b is the actual degree of the output, not the number of terms before unnoticed multiplicities are removed.

<a id="relative-norm"></a>
## Field containment and the ordinary relative norm

Choose the atom B_0 containing beta_tilde and set gamma=delta_(B_0).
An automorphism fixing beta_tilde preserves B_0 and hence gamma; therefore gamma belongs to Q(beta_tilde)=Q(beta).
The subgroup H=Gal(F/L_alpha) fixes Sigma pointwise and hence preserves every membership atom in (BD3), so it fixes gamma as well.
This gives

    gamma in Q(beta) intersect L_alpha.                 (BD4)

More precisely let J be the set stabilizer of B_0.
The distinctness of the products shows G_gamma=J.
Also J acts transitively on B_0, since an element carrying beta_tilde to any xi in B_0 must preserve the block containing them.
It follows from the ordinary subgroup/field correspondence that

    [Q(beta_tilde):Q(gamma)]=e,
    gamma=Norm_(Q(beta_tilde)/Q(gamma))(beta_tilde).       (BD5)

Thus this block product is an ordinary relative norm to its actual own field, with its exact fiber size retained.
No radical, ambient-degree normalization or unidentified root-of-unity factor is introduced.

<a id="mahler-and-raw-comparison"></a>
## Exact Mahler preservation and the raw Cauchy comparison

Put x_xi=log|xi| for xi in Omega and y_B=sum_(xi in B)x_xi=log|delta_B|.
For each atom all x_xi are positive, or all are nonpositive; the latter case may include both negative and zero values.
Therefore

    sum_B max(0,y_B)=sum_(xi in Omega) max(0,x_xi)
                   =log alpha.                         (BD6)

This proves M(gamma)=alpha with no loss of a multiplicity or of a leading coefficient.
Using n=eb and the actual output degree b gives

    M_2(gamma)^2
       =b sum_B (sum_(xi in B) x_xi)^2
       <=be sum_(xi in Omega) x_xi^2
       =M_2(beta_tilde)^2=M_2(beta)^2.                  (BD7)

Equality in this Cauchy step holds precisely when the logarithmic moduli are constant within every block.
That special equal-modulus situation is the type already used in C855 v2; the same-side condition needed for (BD6) does not force equality in (BD7).

<a id="binomial-degree-bound"></a>
## The binomial bound for every starting unit realization

The G-equivariance of (BD3) and transitivity on Omega imply that all Gamma_xi have the same cardinality r.
Counting pairs (xi,a) with xi in Delta_a gives

    n r=d k,  1<=r<=floor(d/2).                          (BD8)

The upper bound uses the explicit orientation choice k<=n/2, not a global basal-minimality assumption.
Different atoms have different subsets Gamma_xi, all of cardinality r.
Thus

    b<=binom(d,r)<=binom(d,floor(d/2)).                 (BD9)

Together with b<=n, (BD4), (BD6) and (BD7), this proves every quantifier in (BD1).
In particular the binomial bound is available for the block endpoint of every unit realization, rather than merely for an unspecified globally basal realization from the external existence theorem.
It is still an exponential degree cap in the measure's degree; no replacement by d is obtained.

<a id="finite-raw-attainment"></a>
## Fixed-alpha attainment in a finite coefficient list

Let B_d=binom(d,floor(d/2)) and let F_alpha be the set of monic irreducible integer polynomials q of degrees b with 1<=b<=B_d such that q has constant coefficient plus or minus one, splits in L_alpha, and M(q)=alpha.
This set is finite.
For each coefficient c_(b-j) of any such q, every j-fold product of its roots has absolute value at most M(q)=alpha, and hence

    |c_(b-j)|<=binom(b,j) alpha, 0<=j<=b.               (BD10)

For finitely many b, (BD10) is a finite list of possible integer coefficients.
If an explicit integer search box is desired, any specified rational A>alpha may replace alpha in these inequalities.
The equation M(q)=alpha, irreducibility, the unit condition and splitting in the actual L_alpha remain required filters; merely satisfying the coefficient bounds is not a realization.
The set is nonempty by (BD1), since alpha was assumed to be a Mahler measure.

The raw M_2 value of a root of an irreducible polynomial is independent of which conjugate is chosen.
Since every beta with M(beta)=alpha has a block endpoint represented in F_alpha with no larger raw quantity, while every root represented in F_alpha is itself one of the original allowed realizations, one obtains the exact equality

    inf_{beta: M(beta)=alpha} M_2(beta)
       =min_{q in F_alpha} M_2(any root of q).           (BD11)

Thus the infimum is attained in L_alpha, at an actual degree at most B_d.
This is an existence and finite-candidate conclusion; no claimed algorithm for deciding exact equality between different sums of squared logarithms is needed for it.
The finite list and its bound depend on alpha and d, so this does not give a uniform bound as the measure varies.

<a id="basal-boundary"></a>
## The basal gap and the remaining original-input return

In the source, basal irreducibility minimizes degree over all irreducible realizations of the same Mahler measure, with the specified orientation of large roots.
The atom construction only minimizes the number of blocks obtainable by multiplying conjugates of the current beta_tilde along a compatible Galois partition.
It does not prove that this particular gamma is globally basal, and it does not identify the minimizer in (BD11) with a globally basal realization.

For a Salem alpha of degree d, alpha itself realizes its measure, so a globally basal irreducible realization certainly has degree at most d.
Theorem 4 places it in L_alpha, but neither that statement nor Theorem 5 compares its raw M_2 with an arbitrary starting beta.
The stronger assertion

    for every beta with M(beta)=alpha there is gamma
    with M(gamma)=alpha, deg(gamma)<=d and
    M_2(gamma)<=M_2(beta)                                (BD12)

has not been proved here or located in the inspected source passages.
No counterexample to (BD12) is asserted either.
Replacing the binomial cap in (BD1) by d merely by invoking the basal definition would be an unsupported step.

Even a degree-at-most-d realization with the same measure has only the general upper estimate M_2<=sqrt(2d) log alpha, obtained by bounding the positive and negative square sums separately by (log alpha)^2.
The Salem realization itself has exactly this square-root-degree cost.
Neither global degree minimality nor the finite attainment result supplies a degree-independent upper comparison with log alpha.

Finally, the block endpoint is a product of conjugates of beta, not a proven radical monomial in the conjugates of alpha.
Membership in L_alpha or the source's labeling of conjugates by subsets of Sigma supplies no such multiplicative identity.
Consequently C866 v1 cannot be applied to this general unit endpoint without a separately proved hypothesis.
The established reduction removes unrestricted external extensions from the fixed-alpha search while leaving the full unit problem in L_alpha and its binomial degree cost.
It does not automatically supply a realization with small raw M_2, a uniform original total-Mahler return, or a resolution of G0001.

## Assessment history

### Decision whole-independent-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:52 |
| status | proved |
| reason | Adopt the complete BD1--BD11 block reduction and finite raw-M2 attainment after independent whole R1088 v7. Every realization of an algebraic integer unit Mahler value descends by an actual relative norm to the intersection of its own field and the measure's normal closure, preserving total measure and not increasing the actual-degree raw quantity. The membership atoms give the binomial degree cap and a finite nonempty coefficient set attaining the fixed-value infimum. The global basal replacement BD12, a uniform cheap realization and unrestricted G0001 completion remain unproved; DD04 supplies the attributed block mechanism, not an unverified raw-norm comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire BD1 and explicit BD11: every unit Mahler value alpha>1 and every nonzero realization beta, actual all-place normalization, field intersection, exact measure preservation, degree/raw comparison and fixed-value finite attainment. |
| argument | [Complete argument](#argument) | Complete BD2--BD11, unit proof and orientation, equivariant atoms and distinct products, exact ordinary norm, same-side measure equality, actual-degree Cauchy, incidence count and both directions of finite attainment. |
| dependency | [Raw normalization interface](Yin_C_G0855_v2.md#raw-p-two-norm-descent) | Only the own-field all-place convention SC16--SC17 and equal-modulus comparison; no universal floor, analytic theorem or original source proof is imported. |
| support | [DD04 block mechanism](../audits/literature/DD04/Yin_U001.md#dd04-u001) | Selected 2004 author-manuscript block, basal and subset mechanisms as attribution and comparison, with complete local proofs of every needed quantified step; no full-paper or external-ancestor audit. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1088_v7.md#block-descent-whole) | Whole BD1--BD11, all fields/degrees and source interfaces, finite attainment, and the explicit unproved BD12, monomial-interface and original-Task limits. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-05)
