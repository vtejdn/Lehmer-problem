---
author: Yin
---

# Moving binomial central suppression with exact integral norm and span costs

This retains the complete original 2026-10-07 [L117 mathematical argument](../ledger/Yin_L_G0117_v1.md).
The original review_matrix_completion agent derived this argument for Yin, using the separately contributed scattering normalization only as an interface.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix an algebraic unit alpha whose monic irreducible P has m=log M(P)>0, degree d, discriminant magnitude D, and q>0 unit-circle roots.
For every nonzero integer Laurent Z not divisible by P, of exponent span L and coefficient l1 norm H, the central size A_c(Z)=sum_C abs(Z(beta)/P'(beta))^2 satisfies

    A_c(Z)>=q[H^(-(d-q))exp(-Lm)/product_C abs(P'(beta))]^(2/q).

All roots and complex multiplicities are counted exactly.
For every integer Q>=2, conjugate-pair simultaneous pigeonholing supplies 1<=n<=Q^(q/2) for which the height-one, Mahler-one numerator 1-t^n has A_c bounded by (4pi^2/Q^2)sum_C abs(P'(beta))^(-2).
Every successful delay sequence tends to infinity as Q tends to infinity; hence the infimum of A_c over these moving numerators is zero on the same fixed P.
The actual maximal-order ideal period h<=2^d D permits n=h ell<=h Q^(q/2), theta_n=(1-alpha^n)/(2P'(alpha)) in O_K minus {0}, with the same suppression and necessary cost nm>=q log(Q/pi)+log D.
This verifies a nonzero prescribed residue, without asserting inverse-cube feasibility, positive infinite products, a uniformly bounded response or a uniform Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:08 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(9): Laurent and norm guards, exact derivative/AM--GM cost, conjugate-pair construction and divergence, maximal-order period and integral residue, strengthened span cost and all bounded-response/cube/fixed-versus-moving limitations. |
| argument | [Complete argument](#argument) | Entire original (1)--(9): Laurent and norm guards, exact derivative/AM--GM cost, conjugate-pair construction and divergence, maximal-order period and integral residue, strengthened span cost and all bounded-response/cube/fixed-versus-moving limitations. |
| dependency | [Exact retained input](Yin_C_G0317_v1.md#minimal-central-cesaro-energy) | Complete scattering normalization A_c/4 and existence of bounded responses, without cube feasibility or input-uniform transient costs. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-positive-product-obstruction) | Exact empty decaying cube class; moving finite forcings do not alter that complete-sequence obstruction. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:12 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, retaining every fixed-input, source-inspection, cube, conditional and uniformity boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(9): Laurent and norm guards, exact derivative/AM--GM cost, conjugate-pair construction and divergence, maximal-order period and integral residue, strengthened span cost and all bounded-response/cube/fixed-versus-moving limitations. |
| argument | [Complete argument](#argument) | Entire original (1)--(9): Laurent and norm guards, exact derivative/AM--GM cost, conjugate-pair construction and divergence, maximal-order period and integral residue, strengthened span cost and all bounded-response/cube/fixed-versus-moving limitations. |
| dependency | [Exact retained input](Yin_C_G0317_v1.md#minimal-central-cesaro-energy) | Complete scattering normalization A_c/4 and existence of bounded responses, without cube feasibility or input-uniform transient costs. |
| dependency | [Exact retained input](Yin_C_G0316_v1.md#unit-circle-positive-product-obstruction) | Exact empty decaying cube class; moving finite forcings do not alter that complete-sequence obstruction. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0550_v1.md#current-moving-forcing-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with actual old findings retained separately at their original inputs and precision. |

## Complete retained argument

<a id="argument"></a>
Let P be the monic irreducible polynomial of an algebraic unit alpha, with m=log M(P)>0 and with q>0 roots on the unit circle.
Let d=deg P and D=|disc P|.
All roots are simple.
No root is a root of unity: otherwise irreducibility would make P cyclotomic, contrary to m>0.
In particular the central roots are nonreal, so q=2r and they occur in r conjugate pairs.
Every product or sum below counts both members of each pair.

For a nonzero integer Laurent polynomial Z not divisible by P, define its central scattering size by

    A_c(Z)=sum_(|beta|=1) |Z(beta)/P'(beta)|^2.          (1)

Every term is nonzero, since vanishing at one conjugate would force P to divide Z after clearing a monomial.
The Laurent orientation in the forcing convention Z(t)=sum_j z_j t^(-j-1) has no effect on the following binomial evaluations.

<a id="central-forcing-norm-cost"></a>
### Norm integrality supplies a span-dependent lower bound

Shift the lowest exponent of Z to zero.
Write L for the resulting degree, equal to its original exponent span, and H for its coefficient l1 norm.
Its constant coefficient is a nonzero integer.
Since alpha is a unit, a Laurent monomial shift does not change the absolute field norm of Z(alpha), its central size, or the coefficient norm H.

The value Z(alpha) is a nonzero algebraic integer, so its absolute norm is at least one.
At every noncentral conjugate gamma,

    |Z(gamma)|<=H max(1,|gamma|)^L.

Multiplying these bounds and retaining the central factors gives

    product_(|beta|=1)|Z(beta)|
                      >=H^(-(d-q)) exp(-Lm).           (2)

Put J_P=product_(|beta|=1)|P'(beta)|>0.
Arithmetic/geometric mean applied to the q positive terms in (1) now proves

    A_c(Z)>=q [H^(-(d-q)) exp(-Lm)/J_P]^(2/q).          (3)

This includes complex pairs with exactly their field-norm multiplicities.
For example, if A_c(Z)<=epsilon^2, then

    Lm+(d-q)log H+log J_P
                             >=q log(sqrt(q)/epsilon). (4)

The derivative product is an explicit fixed-input cost; it is not asserted uniformly bounded.
Formula (3) is positive at fixed span and coefficient norm, but its exponential span dependence is essential for the construction below.

<a id="moving-binomial-central-suppression"></a>
### Bounded coefficients and numerator Mahler measure do not prevent suppression

Select one central root beta_i=exp(2pi i x_i) from each pair, i=1,...,r.
For an integer Q>=2, pigeonhole the Q^r+1 points given by multiples 0,...,Q^r of (x_1,...,x_r) modulo one into Q^r half-open boxes.
The difference of two points provides an integer n with

    1<=n<=Q^r,
    ||n x_i||_(R/Z)<1/Q,
    |1-beta_i^n|<=2pi/Q.                              (5)

The same bound holds for their conjugates.
Thus the nonzero integer binomial Z_n(t)=1-t^n has coefficient height one, coefficient l1 norm two, Mahler measure one, and

    A_c(Z_n)<=(4pi^2/Q^2)
                       sum_(|beta|=1)|P'(beta)|^(-2).  (6)

P does not divide Z_n, since none of its roots is a root of unity.
As Q tends to infinity, any choice of successful n in (5) must tend to infinity: a bounded subsequence would contain one fixed positive n infinitely often, forcing beta_i^n=1.
This contradiction already follows from one central root.
Hence (6) is a genuine moving-forcing family on the SAME fixed P, with unbounded exponent span and unchanged coefficient size and numerator Mahler measure.

In particular, no strictly positive lower bound for A_c(Z), uniform over all such Z on a fixed P, can depend only on P, m, d, coefficient height or M(Z).
A span or other noncentral cost must enter.
This is stronger than merely lacking a bound uniform in degree: the infimum is zero for each fixed admissible P.

<a id="integral-multiplier-binomial-cost"></a>
### The suppression can retain the prescribed integral-multiplier residue

The same idea works with theta_n=(1-alpha^n)/(2P'(alpha)) required to be integral.
Use the finite ring

    O_K/(2P'(alpha)O_K).

Multiplication by the nonzero integral element 2P'(alpha) has lattice index 2^d D, by its field norm.
The image of alpha is a unit.
Let h>=1 be its finite multiplicative order, so

    h<=2^d D,
    alpha^h=1 modulo 2P'(alpha)O_K.                    (7)

This uses only the finite ideal-quotient argument underlying L G0110; it does not require hyperbolicity or invertibility of P(S) on l2.
Working in the maximal order here directly ensures the stated integral-multiplier condition, without any assumption about the power-basis index.

Apply the preceding r-dimensional pigeonhole argument to beta_1^h,...,beta_r^h.
It gives n=h ell with

    1<=ell<=Q^r,
    n<=h Q^r,
    |1-beta^n|<=2pi/Q for every central beta,
    theta_n=(1-alpha^n)/(2P'(alpha)) in O_K minus {0}.  (8)

The binomial forcing still has (6), and its Laurent residue is Phi(z_n)=1-alpha^n=2P'(alpha)theta_n.
Nonvanishing follows because alpha is not a root of unity.
This verifies the arithmetic residue condition; it does not verify any inverse or cube condition on a unit-circle branch.

There is an exact additional cost.
The nonzero integral norm of theta_n implies

    |Norm(1-alpha^n)|>=2^d D.

Every noncentral factor is at most 2 max(1,|gamma|)^n.
Using (8) at the q central factors therefore gives

    2^d D<=2^(d-q) exp(nm)(2pi/Q)^q,
    nm>=q log(Q/pi)+log D.                             (9)

This lower bound is meaningful whenever its right side is positive.
Together, (8)--(9) make the span cost explicit.
There is no conflict as Q grows: the construction allows n of order Q^r, whereas the necessary lower bound in (9) is logarithmic in Q divided by m.
There is no unproved uniformly short recurrence or period premise.

<a id="central-scattering-counterinterface"></a>
### The precise interface to central mean-square energy

The separate [scattering calculation](Yin_C_G0317_v1.md#minimal-central-cesaro-energy) uses central jumps a_beta=Z(beta)/P'(beta).
In its notation, optimizing the central homogeneous coefficients over bounded real solutions gives symmetric Cesaro mean-square energy A_c(Z)/4.
Under that separately proved normalization, (6) drives this optimized central mean energy to zero on a fixed P.
Conjugate symmetry is respected by the integer binomial, so the balanced central coefficients remain real as a combined sequence.

No uniform bound for response size or rounding-cube feasibility follows from the small central coefficients.
The separate scattering result does provide bounded solutions for each finite forcing; stable and expanding parts, and the finite forcing interval, can nevertheless have large input-dependent costs.
In particular the empty decaying-cube class of [L G0115](Yin_C_G0316_v1.md#unit-circle-positive-product-obstruction) remains unchanged.
A fixed Z has nonzero A_c(Z), and any valid fixed-forcing positive mean-energy conclusion remains valid.
It is a uniform positive floor over moving forcings, based on central energy alone and ignoring span, that (6) excludes.

Likewise (8) is a genuinely moving integral-multiplier family with small central embeddings, not the pure unit-power frequency reindexing of L G0105.
Formula (9) accounts for one necessary noncentral arithmetic cost.
It does not produce high Fourier amplitude at the deep frequencies required by the entropy argument, and does not transfer a bounded-solution mean-square statement into a valid compact coding or positive infinite cosine product.
