---
author: Yin
---

# Unit-circle roots exclude every nonzero decaying integer defect in the rounding cube

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI assess_shortness_route for Yin.
The coordinator proposed the l2 Fourier obstruction.
This note proves the stronger c0 statement directly, records its product consequence, and keeps fixed infinite sequences separate from moving finite windows.
There is no new source, computation or novelty claim.

Let P(t)=sum_(i=0)^d p_i t^i be monic and irreducible over Z, of positive degree, with a root beta on the unit circle.
In particular p_0 is nonzero and all its complex roots are distinct.
Write (Se)_j=e_(j+1), with j in Z.
The main theorem requires no unit, positive-Mahler-measure or all-power degree assumption.

<a id="unit-circle-c0-integer-forcing"></a>
## The exact c0 obstruction

For any real sequence e tending to zero at both ends,

    P(S)e in Z^Z  implies  e in Z^(Z),                 (1)

where Z^(Z) denotes the finitely supported integer sequences.
Conversely every sequence in Z^(Z) has the stated properties.
Thus this is an exact description, not only nonexistence in a particular norm ball.

Put z=P(S)e.
Finite sums of shifts preserve c0, so z tends to zero.
Since its entries are integers, z has finite support.
Use the Laurent convention of [L G0107](Yin_L_G0107_v1.md#rounded-defect-residue-class):

    Z(t)=sum_j z_j t^(-j-1).

We show Z(beta)=0 without assuming that e is summable.
For N large enough to contain the support of z, expand

    Z(beta)=sum_(i=0)^d p_i beta^i
                 sum_(l=-N+i)^(N+i) e_l beta^(-l-1).

Subtract the common sum over -N<=l<=N inside every term.
Its coefficient is P(beta)=0.
For each i, at most 2i boundary terms remain.
Since |beta|=1, for N>d this gives

    |Z(beta)| <= 2 sum_i i|p_i|
                         sup_(|l|>=N-d)|e_l| ->0.      (2)

The irreducibility and monicity of P now imply Z(t)=P(t)Q(t) with Q an integer Laurent polynomial.
Indeed clear a monomial from Z, divide the resulting integer polynomial by monic P, and use that the rational remainder vanishes at beta and has degree less than d.
Let q be the finite integer sequence corresponding to Q.
The Laurent convention gives P(S)q=z, so v=e-q is in c0 and P(S)v=0.

For completeness that homogeneous equation has no nonzero bilateral c0 solution.
Distinct nonzero roots beta_1,...,beta_d and a Vandermonde matrix give a unique representation v_j=sum_l c_l beta_l^j: match any d consecutive values, then use p_d=1 and p_0!=0 to continue the recurrence both ways.
Applying the inverse Vandermonde matrix to (v_j,...,v_(j+d-1)) shows that every c_l beta_l^j tends to zero as j tends to either infinity.
No nonzero exponential mode can do that.
Thus v=0 and e=q, proving (1).

In particular,

    e in c0, P(S)e integer, |e_j|<=1/2 for every j
                       imply e=0.                     (3)

The closed cube suffices; a strict uniform margin is unnecessary.
Every l^p sequence, for any finite real p>0, belongs to c0, so (1)--(3) also apply to all those spaces.
This includes the coordinator's original l2 proposal.
There is no assertion for arbitrary bounded sequences.

<a id="unit-circle-positive-product-obstruction"></a>
## Positive bilateral cosine products and the free forcing class

For a real sequence satisfying |e_j|<=1/2, define its bilateral product by the decreasing limit of symmetric finite products.
All factors are nonnegative.
The elementary bound

    -log cos(pi x)>=pi^2 x^2/2,  |x|<1/2,

and the quadratic Taylor bound near zero show the exact criterion

    product_(j in Z) cos(pi e_j)>0
       iff sum_j e_j^2<infinity and |e_j|<1/2 for every j. (4)

A boundary coordinate makes the product zero.
For the converse, l2 gives tails tending to zero, where the logarithms are bounded in absolute value by a constant times e_j^2; the remaining finitely many logarithms are finite.
Hence no order-dependent conditional convergence is being invoked.

Combining (3)--(4) yields

    P(S)e integer and |e_j|<=1/2 for every j:
    product_j cos(pi e_j)>0 iff e=0.                    (5)

Consequently the following set of pairs is empty:

    { (z,e): z nonzero finite integer,
             e in c0, P(S)e=z, ||e||_infinity<1/2 }.   (6)

Replacing c0 in (6) by any finite l^p does not change emptiness.
Requiring a positive product instead of c0 likewise leaves no nonzero pair.
On this branch P(S) has no bounded inverse on l2, so (6) is deliberately phrased as an equation for a pair, not an undefined application of P(S)^(-1).

This is the precise obstruction to extending the nonempty hyperbolic free-forcing class of [L G0110](Yin_L_G0110_v1.md#relaxed-residue-amplitude-equivalence) to an irreducible polynomial with a unit-circle root.
Dropping the prescribed residue does not help: there is already no nonzero decaying integer forcing response in the cube.
We do not assign a positive optimized amplitude to an empty class or assert that a supremum over it is attained.

<a id="unit-circle-fixed-trace-product"></a>
## Application to actual fixed weighted traces

Now assume additionally that alpha is an algebraic unit with minimal polynomial P, m=log M(P)>0, and at least one unit-circle conjugate.
For a fixed theta in Q(alpha) minus {0}, put

    u_j=sum_(|sigma(alpha)|<1) sigma(theta) sigma(alpha)^j.

This is real, satisfies P(S)u=0, and tends to zero as j->+infinity.
There is at least one stable conjugate: positive m supplies an expanding conjugate, and the unit norm forces a stable one.
All coefficients sigma(theta) are nonzero.
Thus u is not the zero sequence, by the Vandermonde argument on its stable roots.

Choose a nearest integer n_j to 2u_j, arbitrarily if tied, and let e_j=2u_j-n_j.
Then |e_j|<=1/2 and P(S)e=-P(S)n is an integer sequence.
If its cosine product were positive, (5) would force e=0.
Then 2u_j is integral for every j and tends to zero at positive infinity, hence is eventually zero.
The stable-root Vandermonde argument again contradicts theta!=0.
We have proved

    product_(j in Z) |cos(2pi u_j)|=0                 (7)

for every such fixed theta.
This qualitative conclusion does not require theta to be integral; an individual half-integer rounding tie already gives a zero factor.
In particular (7) applies to every nonzero integral multiplier in the earlier trace construction.

This does not replace the stronger quantitative fixed-multiplier decay in [L G0105](Yin_L_G0105_v1.md).
It proves no uniform decay rate over P or theta, and no bound on when a finite product becomes small.
It does not exclude the moving-multiplier finite windows retained in that record.
The statements (1)--(7) concern each complete bilateral sequence; they cannot be applied to finite windows without their exterior recurrence and boundary data.

<a id="unit-circle-defect-hypothesis-boundaries"></a>
## Why the hypotheses matter

The c0 or positive-product condition cannot be replaced by boundedness alone.
If beta is a unit-circle root, then e_j=epsilon Re(beta^j), with 0<epsilon<1/2, is a nonzero bounded real homogeneous solution in the strict cube.
Its integer forcing is zero.
It does not tend to zero, as follows from the same finite-mode argument, and (5) gives product zero.

Irreducibility is also essential.
Let

    Q=t^2-3t+1, lambda=(3+sqrt5)/2,
    w_j=-lambda^(-|j|)/sqrt5,
    R=(t-1)Q.

Direct substitution gives Q(S)w=delta_(-1), and hence

    R(S)w=delta_(-2)-delta_(-1).                        (8)

Here R has a unit-circle root, w is nonzero and exponentially decaying, ||w||_infinity=1/sqrt5<1/2, and its product is positive by (4).
The cancellation only removes the factor t-1 from the forcing; it does not remove Q.
This reducible control is not an irreducible small-Mahler counterexample.

The theorem excludes a particular decaying-defect mechanism on the unit-circle branch.
It is not a Lehmer counterexample, does not prove an entropy gap, and does not exclude other central-dynamics methods or finite-window tests with explicit boundary costs.

## Contribution and review scope

The coordinator proposed the l2 Fourier cancellation and its arithmetic irreducibility consequence, and requested the c0 extension.
The assigned agent supplied the finite boundary-sum proof of that extension, the two-sided recurrence argument, the exact product criterion and trace application, and the scope controls.
The assigned agent checked all shift and Laurent orientations, the finite l^p and pair quantifiers, and the two explicit hypothesis boundaries.

The separate ms25_source agent independently read and checked the complete assembled (1)--(8), finding no mathematical defect.
Its review covered the finite boundary-sum orientation and c0 bound, monic Laurent division, the two-sided Vandermonde argument, closed cube and every finite l^p, the exact product criterion, the empty-pair formulation without an undefined inverse, arbitrary nonzero fixed theta in the trace application, and both bounded and reducible controls.
This complete review also covers the coordinator's initial l2 mechanism through the stronger c0 proof.
No source acquisition, computation, identifier allocation or fixed material edit is part of this derivation or review.

The coordinator subsequently checked the complete assembled (1)--(8), including the boundary cancellation, integer Laurent division, two-sided recurrence, all stated sequence classes, product equivalence, arbitrary fixed field multiplier and both hypothesis controls.
This is a contributor check of the strengthened result; ms25_source supplies the separate complete independent coverage.
