---
author: Yin
---

# Moving binomial forcing suppresses central scattering, with an exact norm cost

Current checking scope is owned by [R550](../audits/reviews/Yin_R_G0550_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-07.
Bounded direct derivation by the assigned review_matrix_completion AI agent for Yin.
This note follows the fixed-trace and decaying-defect boundaries of L G0105 and L G0115.
It supplies a moving integral-forcing family and a quantitative norm constraint, without claiming a decaying or rounding-cube response.
No new source, computation or novelty claim is involved.

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
## Norm integrality supplies a span-dependent lower bound

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
## Bounded coefficients and numerator Mahler measure do not prevent suppression

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
## The suppression can retain the prescribed integral-multiplier residue

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
## The precise interface to central mean-square energy

The separate [scattering calculation](Yin_L_G0116_v1.md#minimal-central-cesaro-energy) uses central jumps a_beta=Z(beta)/P'(beta).
In its notation, optimizing the central homogeneous coefficients over bounded real solutions gives symmetric Cesaro mean-square energy A_c(Z)/4.
Under that separately proved normalization, (6) drives this optimized central mean energy to zero on a fixed P.
Conjugate symmetry is respected by the integer binomial, so the balanced central coefficients remain real as a combined sequence.

No uniform bound for response size or rounding-cube feasibility follows from the small central coefficients.
The separate scattering result does provide bounded solutions for each finite forcing; stable and expanding parts, and the finite forcing interval, can nevertheless have large input-dependent costs.
In particular the empty decaying-cube class of [L G0115](Yin_L_G0115_v1.md#unit-circle-positive-product-obstruction) remains unchanged.
A fixed Z has nonzero A_c(Z), and any valid fixed-forcing positive mean-energy conclusion remains valid.
It is a uniform positive floor over moving forcings, based on central energy alone and ignoring span, that (6) excludes.

Likewise (8) is a genuinely moving integral-multiplier family with small central embeddings, not the pure unit-power frequency reindexing of L G0105.
Formula (9) accounts for one necessary noncentral arithmetic cost.
It does not produce high Fourier amplitude at the deep frequencies required by the entropy argument, and does not transfer a bounded-solution mean-square statement into a valid compact coding or positive infinite cosine product.

## Contribution and actual review

The assigned agent derived and checked the norm product, weighted AM--GM, conjugate-pair pigeonhole construction, divergence of the successful delays, finite ideal period, integral multiplier and strengthened norm/span cost.
The assess_shortness_route agent supplied the separately derived scattering normalization as an interface; its proof is not reproduced or claimed independently proved here.

The coordinator independently read and checked the complete (1)--(9), including unit Laurent shifts and norms, the noncentral H^(d-q)M^L bound, the derivative product and epsilon direction in AM--GM, the conjugate-pair count and non-root-of-unity guard, pigeonholing and divergence of every successful delay sequence, maximal-order ideal index, the nonzero integral multiplier and strengthened span bound, and all fixed-versus-moving and cube limitations.
It found no mathematical defect.
It requested scope clarifications and the existing period interface but did not contribute this proof mechanism, so this is a complete independent check of (1)--(9).
Its contribution to the separate scattering result is not described as a new independent review of that dependency.

The assess_shortness_route agent also independently checked the entire (1)--(9), including the Laurent/norm guards, weighted AM--GM, strict r-angle pigeonholing, divergence of the delays, maximal-order period without hyperbolicity, integral multiplier and the exact cancellation of powers of two in (9).
It found no mathematical defect.
Its check of the A_c/4 scattering paragraph is an interface check of its own separately contributed result.
Its requested distinction between existence of a bounded solution and a uniform bound on response size or cube feasibility is incorporated above.

| Review | Relationship |
| --- | --- |
| Assigned-agent derivation of (1)--(9) | self-reviewed |
| Coordinator complete written check of (1)--(9), with the separate scattering dependency qualified above | independently reviewed |
| assess_shortness_route complete written check of (1)--(9), with contributor interface check of the scattering paragraph | independently reviewed |

No new source, computation or original-source reread formed part of these checks.
No identifier allocation or fixed-material edit was made by the assigned agent.
