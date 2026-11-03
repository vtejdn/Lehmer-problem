---
author: Yin
---

# Finite-coset obstruction for actual tail supersolutions and canonical first-hit ratios

Human author Yin.
Contributor original_signed_asymptotic developed the one-prescribed-coset theorem, its arbitrary finite-index subgroup reduction and the actual canonical first-hit consequence.
The argument is extracted from [D9 FE1--FE9](../drafts/Yin_D_G0009.md#finite-coset-tail-obstruction), which records the changed finite-arithmetic candidate test and its bounded reuse search.
The mutable Draft is extraction provenance, not a proof dependency.
The unchanged theorem is adopted through [whole independent R1050](../audits/reviews/Yin_R_G1050_v1.md#whole-finite-coset-finding), as selected by the [current decision](#decision-whole-reviewed-2026-10-28).

The adopted [C827 statement and proof](Yin_C_G0827_v1.md#decision-whole-reviewed-2026-10-27) exclude a single radial envelope with bounded central angular distortion.
The present statement permits unrelated envelopes in different congruence classes and requires comparability on only one prescribed class.
Their relative sizes need not be bounded, so C827's one-envelope hypothesis is not silently imposed.
The finite-word translation mechanism and its original-law scope are reused, with the additional congruence restrictions and all intermediate legality costs proved below.
This is a project deduction, not a claim of literature priority; no new source theorem, native computation or finite graph is a premise.

## Statement

Use P=t^4-t^3-t^2-t+1, its exterior root beta, upper neutral root zeta, O=Z[beta], B=1/(beta-1), S=beta B and the adopted actual strict core

    D={x in O: |x_+|<B, |x_-|<S},       rho(x)=|x(zeta)|.

Here x_+ and x_- are the beta and beta^(-1) real embeddings, respectively.
The original digit weights are pi_(-1)=pi_1=1/4 and pi_0=1/2.
P_D is the original kernel x->beta x+e killed on leaving D, and B_0 is its restriction to D minus{0}, with entry into zero killed and no row renormalization.
Let p_n=P_D^n(0,0) be the COMPLETE original return probabilities, R their generating-function radius, and R_f the radius of the complete first-return series.
The entire limit p_n^(1/n)->1/R is the adopted C555 interface selected in C827.
All fixed input and certificate scopes are those of [C827's exact input table](Yin_C_G0827_v1.md#exact-inputs-reuse-and-boundaries), including C400's actual strict-core equality, C790's actual unit and C511's canonical first-hit family.

Let I be ANY finite-index additive subgroup of O, not necessarily an ideal, and let C be ANY prescribed coset of I.
Fix t>0, a finite F subset D containing zero, and a pointwise finite positive W on D minus{0} satisfying

    t B_0 W(x)<=W(x),              x in D outside F.      (FE1)

Suppose only on the states in the chosen coset C there are epsilon>0, r_*>0, 0<c<=C_0<infinity and an arbitrary function a:[r_*,infinity)->(0,infinity) such that

    c a(rho(x))<=W(x)<=C_0 a(rho(x))
    for x in C intersect D, |x_+|,|x_-|<=epsilon,
    rho(x)>=r_*.                                        (FE2)

Then t<=R.
No comparison on any other coset, no relation between different radial envelopes, and no regularity of a is required.
In particular, allowing an independent positive radial envelope a_C in each residue class cannot yield FE1 at t>R, even when the ratios between the different a_C are unbounded.

The same exclusion holds if, on the selected coset alone, W(x)=a_C(rho(x))G_C(x_+,x_-,x(zeta)/rho(x)) for all sufficiently large-radius states with real coordinates in an open neighborhood U_C of(0,0), where G_C:U_C times S^1 ->(0,infinity) is continuous.
Other cosets may have unrelated radial functions, continuous factors and neighborhoods.
A fixed finite collection of congruence observations is included by taking its common finite-index refinement.

For the actual critical H=H_R and Q(x,y)=R P_D(x,y)H(y)/H(x), let Q_0 be killed on zero.
No uniform multiplicative drift Q_0(W/H)<=q W/H outside finite F with 0<q<1 is possible when FE2 holds on even one finite-index coset.
The actual critical H and Q have the adopted meanings of C827, without a finite-mean hypothesis.

Conditionally on R_f>R, let R<t<R_f and use the actual finite positive first-hit function H_t of C511, normalized by H_t(0)=1 and satisfying H_t=t P_D H_t off zero.
For EVERY finite-index additive subgroup I, prescribed coset C, L>0, epsilon>0, M>=0 and finite F subset D containing zero, there exist integers n,k>=1 and two distinct actual endpoints h_k,beta^n h_k in C intersect(D minus F) such that both endpoints have real-coordinate absolute values at most epsilon, their neutral radii are equal and greater than M, and H_t(h_k)/H_t(beta^n h_k)>L.
The proof gives a fixed arithmetic progression dN of permissible n and the stronger quantitative comparison FE9 for every n in that progression and all sufficiently large k.
The construction and its scale depend on the fixed subgroup/coset and on the displayed bounds; no uniform-modulus assertion is made.

These statements do not classify the critical mean, decide R_f=R versus R_f>R, provide a fixed-start tail estimate, or exclude additive/nonuniform drift, arithmetic resolution increasing with radius, or arbitrary finite-state partitions not defined by congruences.

## Complete argument

### A sequence in an arbitrary prescribed congruence class

Put v=beta+beta^(-1)-2 and tau=(3+sqrt13)/2 as in C790, so

    v^2+3v-1=0,       v^(-1)=v+3 in O,
    v_+=v_-=tau^(-1), v(zeta)=-tau,       tau>1.          (FE3)

Since O/I is a finite additive group, there is an integer m>=2 with mO contained in I.
For example, take twice a common multiple of the finite additive orders of all elements of O/I.
This argument does not suppose that multiplication by beta acts on O/I.
Instead work in the actual finite ring O/mO, which has m^4 elements in the power basis.
The algebraic identity beta^(-1)=-beta^3+beta^2+beta+1 shows that beta is a unit of this order, and FE3 shows the same for v.
Multiplication by beta and by v^2 therefore gives permutations of O/mO.
Powers of these finite permutations supply positive integers d and ell such that

    beta^d=1 mod mO,          v^(2 ell)=1 mod mO.         (FE4)

Write dN={d,2d,3d,...} for the positive multiples of this fixed d.
Choose a nonzero b in C.
Such a representative exists even for the zero coset, since I contains mZ and every coset is infinite.
The embedding b->b(zeta) is injective, so r_b=|b(zeta)|>0.
Set A_b=max(|b_+|,|b_-|)>0 and, for integers k>=1, define

    h_k=b v^(2 ell k).
    (h_k)_+=b_+ tau^(-2 ell k),
    (h_k)_-=b_- tau^(-2 ell k),
    h_k(zeta)=b(zeta) tau^(2 ell k).                    (FE5)

Every h_k is congruent to b modulo mO and hence belongs to C.
For EVERY positive n divisible by d, beta^n h_k is also congruent to b modulo mO and belongs to the same C.
For such n the endpoint radii satisfy the exact identity

    rho(beta^n h_k)=rho(h_k)=r_b tau^(2 ell k).           (FE6)

For each fixed n both endpoint real-coordinate pairs tend to(0,0) as k grows, while their common neutral radius tends to infinity.
In particular every prescribed finite-index coset has infinitely many actual strict-core states with this central-real and escaping-neutral behavior.
No fractional enlargement of O, equidistribution assertion or independent sampling of congruence and neutral coordinates is used.

### Complete original returned words survive the congruence restriction

Fix n in dN before choosing k.
Let A_n be the finite set of all chronological states on all original zero-to-zero words of length n, including both endpoints.
The all-zero word makes A_n nonempty, and every member lies in the actual strict core.
Thus

    delta_n=min_(x in A_n){B-|x_+|, S-|x_-|}>0,
    M_F=max_(x in F)rho(x)

are well-defined finite numbers, with delta_n strictly positive.
For a returned word with states x_j, its translation from h_k has states y_j=x_j+beta^j h_k and obeys exactly the same original digit recursion.
Choose k large enough that

    beta^n A_b tau^(-2 ell k)<delta_n,
    r_b tau^(2 ell k)>M_F+n.                            (FE7)

For 0<=j<=n the change in the expanding coordinate is at most beta^n A_b tau^(-2 ell k), and the contracting-coordinate change is at most A_b tau^(-2 ell k).
Hence every y_j satisfies the two strict core inequalities.
Since rho(x_j)<=j<=n and |(beta^j h_k)(zeta)|=r_b tau^(2 ell k), also rho(y_j)>M_F, so every intermediate state avoids F, including zero.
The intermediate states need not lie in C, and the argument never requires that condition.
Only the endpoint comparison FE2 is restricted to C; the supersolution inequality FE1 remains imposed at every state outside F.

Let B_F be P_D restricted to D minus F.
All translated words retain their complete original probabilities and end at beta^n h_k.
Distinct original digit words remain distinct paths, so their weights sum to the full p_n, without a congruence-conditioned or truncated replacement law.
Dropping nonnegative F terms in FE1 and iterating the finitely branching kernel gives

    B_F^n(h_k,beta^n h_k)>=p_n,
    t^n p_n W(beta^n h_k)<=W(h_k).                      (FE8)

Every iterated sum has at most3^n terms with finite values of W.
For each fixed n in dN, FE7 and the neighborhood/radius requirements of FE2 hold for all sufficiently large k.
The exact radius equality FE6 cancels a, so FE8 gives

    t^n p_n<=C_0/c,                      for EVERY n in dN.

Taking nth roots along this unbounded arithmetic progression and using the entire root limit gives t/R<=1, proving the claimed exclusion.
The periods d and ell are fixed once m is chosen, the representative b depends on the coset, and the sufficiently large scale k may depend on n and F.
No uniform cost across moduli or return lengths has been discarded.
As in C827, the translated paths are open and this comparison supplies no fixed-start entrance mass or closed-loop probability.

### Continuous factors on each residue class and actual H consequences

Suppose on a chosen coset C and on all sufficiently large-radius states with central real coordinates one proposes

    W(x)=a_C(rho(x))G_C(x_+,x_-,x(zeta)/rho(x)),

where G_C is continuous and strictly positive on U_C times S^1 for an open neighborhood U_C of(0,0).
Choose a closed real square inside U_C.
Its product with S^1 is compact, so G_C has a strictly positive minimum and finite maximum there, giving FE2 for this coset alone.
The exclusion therefore permits different neighborhoods, constants, radial functions and continuous angular factors for every residue class.
A fixed finite collection of congruence observations is covered by taking the finite-index intersection of its additive subgroups and choosing one joint coset.
No analogous claim is made for arbitrary finite-state partitions not determined by such congruences.

For the actual critical H and Q_0, the identity Q_0(W/H)=R B_0 W/H is precisely the C827 identity.
Thus a uniform multiplicative drift Q_0(W/H)<=q W/H outside finite F, with 0<q<1, is impossible whenever FE2 holds on even one finite-index coset, since it would give FE1 with t=R/q>R.

There is also a more localized conditional constraint on the ACTUAL canonical H_t.
Assume R_f>R and fix R<t<R_f.
C511 gives finite positive H_t and H_t=t P_D H_t off zero, so t B_0 H_t<=H_t.
For every finite-index subgroup I and prescribed coset C, the same construction yields

    H_t(h_k)/H_t(beta^n h_k)>=t^n p_n
    for every n in dN and all sufficiently large k.     (FE9)

Because(t^n p_n)^(1/n)->t/R>1 along dN, for every L>0, epsilon>0, M>=0 and finite F containing zero there exist such n,k with both endpoints in C intersect(D minus F), both real-coordinate absolute values at most epsilon, common neutral radius greater than M, and H_t(h_k)/H_t(beta^n h_k)>L.
Thus the mandatory same-radius oscillation of a hypothetical supercritical H_t occurs within EVERY prescribed finite-index coset, not merely between residue classes.
This is conditional on the actual strict-radius branch and does not construct that branch or an alternative stationary law.

The bounded test rules out repairing a radial-angular strict certificate by any fixed congruence resolution of the stated form.
A potentially useful next discriminator is whether arithmetic information increasing with radius can control the actual H ratios, or whether a genuinely additive/nonuniform central drift can avoid this multiplicative-certificate obstruction.
Neither mechanism is supplied here, and finite or infinite critical mean, R_f=R versus R_f>R, fixed-start return tails and positive linear bridge-level growth remain unresolved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision finite-coset-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:15 |
| status | open |
| reason | Fix the complete author FE1--FE9 argument: one prescribed coset of any finite-index additive subgroup suffices to exclude a supercritical radial-envelope tail certificate, including unrelated envelopes and continuous angular factors per residue class; actual canonical H_t has conditional unbounded ratios inside every such coset. Whole independent review and adoption remain outstanding, with no mean or strict-radius classification. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire original quartic law, all finite-index additive subgroups and prescribed cosets, finite exceptions and pointwise finite positive supersolutions, one-coset arbitrary radial comparison, continuous-factor and true-Q consequences, and conditional canonical H_t ratio quantifiers with every limitation. |
| argument | [Complete FE1--FE9 proof](#complete-argument) | Reduction through mO without assuming I is an ideal, actual finite-ring unit periods, nonzero representative and strict-core escaping sequence, every translated intermediate state and complete original word weight, same-radius cancellation along a fixed progression and all actual H consequences. |
| dependency | [Adopted complete original translation interface](Yin_C_G0827_v1.md#decision-whole-reviewed-2026-10-27) | Full returned-word comparison mechanism and all five exact underlying interfaces: actual strict core, explicit balanced unit, complete p_n and entire root limit, canonical finite positive H_t for 0<t<R_f, and actual critical H/Q. The changed congruence restriction is proved here rather than imported. |
| dependency | [Actual strict quartic core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Strict real strip equals the original accessible/coaccessible O-core at the fixed quartic, with C399's retained co-return certificate scope. |
| dependency | [Actual balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | The O-unit v, exact inverse and real/neutral embeddings used in FE3--FE7; no counting lower bound is treated as original probability. |
| dependency | [Entire complete-return root limit](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Original iid complete return p_n and p_n^(1/n)->1/R, hence the same limit along the fixed positive arithmetic progression dN. |
| dependency | [Canonical first-hit family](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Actual finite positive H_t and off-zero t-harmonicity for 0<t<R_f; use beyond R is conditional on that interval being nonempty. |
| dependency | [Actual critical H and Q](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Actual finite positive H_R and stochastic original-weight Doob Q; no summable stationary normalization or uniform operator-power conclusion. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T17:32 |
| status | proved |
| reason | Adopt the unchanged complete finite-coset theorem after whole independent R1050 and responsible inspection of the complete statement, FE1--FE9 argument and actual adopted input interfaces. The arbitrary additive subgroup reduction, same-coset equal-radius endpoints, every original intermediate-state margin and weight, progression root limit and conditional actual H_t ratios are covered. Neither critical mean nor strict first-return-radius separation nor the unrestricted Mahler gap is determined. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire original quartic law, all finite-index additive subgroups and prescribed cosets, finite exceptions and pointwise finite positive supersolutions, one-coset arbitrary radial comparison, continuous-factor and true-Q consequences, and conditional canonical H_t ratio quantifiers with every limitation. |
| argument | [Complete FE1--FE9 proof](#complete-argument) | Reduction through mO without assuming I is an ideal, actual finite-ring unit periods, nonzero representative and strict-core escaping sequence, every translated intermediate state and complete original word weight, same-radius cancellation along a fixed progression and all actual H consequences. |
| dependency | [Adopted complete original translation interface](Yin_C_G0827_v1.md#decision-whole-reviewed-2026-10-27) | Full returned-word comparison mechanism and all five exact underlying interfaces: actual strict core, explicit balanced unit, complete p_n and entire root limit, canonical finite positive H_t for 0<t<R_f, and actual critical H/Q. The changed congruence restriction is proved here rather than imported. |
| dependency | [Actual strict quartic core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Strict real strip equals the original accessible/coaccessible O-core at the fixed quartic, with C399's retained co-return certificate scope. |
| dependency | [Actual balanced unit](Yin_C_G0790_v1.md#decision-whole-reviewed-2026-10-26) | The O-unit v, exact inverse and real/neutral embeddings used in FE3--FE7; no counting lower bound is treated as original probability. |
| dependency | [Entire complete-return root limit](Yin_C_G0555_v1.md#decision-isolated-whole-review-adoption-20261022) | Original iid complete return p_n and p_n^(1/n)->1/R, hence the same limit along the fixed positive arithmetic progression dN. |
| dependency | [Canonical first-hit family](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Actual finite positive H_t and off-zero t-harmonicity for 0<t<R_f; use beyond R is conditional on that interval being nonempty. |
| dependency | [Actual critical H and Q](Yin_C_G0805_v1.md#decision-whole-reviewed-2026-10-26) | Actual finite positive H_R and stochastic original-weight Doob Q; no summable stationary normalization or uniform operator-power conclusion. |
| review | [Whole independent R1050](../audits/reviews/Yin_R_G1050_v1.md#whole-finite-coset-finding) | Entire statement and FE1--FE9 proof, six exact adopted dependency interfaces, all finite-coset quantifiers and original-law limitations; no new native calculation. |
