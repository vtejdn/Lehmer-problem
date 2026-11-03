---
author: Yin
---

# Suppressed central tails retain a linear binomial transient cost

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI assess_shortness_route for Yin.
The coordinator proposed the balanced-tail interior calculation.
This note checks its exact normalization, gives its finite constant, and optimizes the whole three-interval window over every bounded center correction.
No source, computation or novelty claim is involved.

Fix a monic irreducible algebraic-unit polynomial P with m=log M(P)>0 and at least one unit-circle root.
Denote its central, stable and expanding root sets by C, S and U.
All roots are distinct and every complex pair is counted twice.
Let q=|C|>0 and put

    b_beta=1/P'(beta),
    W=sum_C |b_beta|^2>0,
    H=sum_C |b_beta|,
    rho=max({1/2} union {|beta|: beta in S}
                       union {|beta|^(-1): beta in U})<1,
    T=[rho sum_U |b_beta|+sum_S |b_beta|]/(1-rho).

For distinct central roots define

    delta=min_(beta!=gamma in C)|1-beta conjugate(gamma)|,
    K_0=2(q-1)/delta.

In a case with q=1, the convention is K_0=0 and no delta is needed.
The positive-measure irreducible-unit assumptions here in fact exclude the roots +/-1, so q is even and at least two.
Constants below depend on this fixed P.

<a id="binomial-three-interval-coefficients"></a>
## The binomial and its exact three center coefficients

Use the causal-center kernel of [L G0116](Yin_L_G0116_v1.md#unit-circle-scattering-coefficients):

    w_j=sum_(S union C) b_beta beta^j, j>=0,
    w_j=-sum_U b_beta beta^j,          j<0,
    P(S)w=delta_(-1),  (Se)_j=e_(j+1).

For n>=1 the forcing z_n=delta_(-1)-delta_(-n-1) has Laurent polynomial Z_n(t)=1-t^n.
Every bounded real solution is exactly

    e_j=w_j-w_(j+n)+sum_C c_beta beta^j,              (1)

where c_(conjugate beta)=conjugate(c_beta).
Write zeta_beta=beta^n and

    A_n=sum_C |(1-zeta_beta)b_beta|^2,  0<=A_n<=4W.

On the consecutive intervals

    I_-=[-2n,-n-1], I_0=[-n,-1], I_+=[0,n-1],

the center coefficient vectors are, respectively,

    u_-=c,   u_0=c-zeta b,   u_+=c+(1-zeta)b.         (2)

Products of root-indexed vectors in this note are coordinatewise.
In particular the interior formula is

    e_j=sum_C(c_beta-zeta_beta b_beta)beta^j
             -sum_U b_beta beta^j
             -sum_S b_beta beta^(j+n),  -n<=j<=-1.   (3)

Let h be the indicated piecewise center sum and r=e-h.
Geometric series give the uniform estimates

    sum_(I_0)|r_j|<=T,
    sum_(I_- union I_0 union I_+)|r_j|<=2T.            (4)

For the left interval the expanding exponents in the two kernel terms have absolute values 1,...,2n, so its bound is rho sum_U|b_beta|/(1-rho).
The right stable exponents are 0,...,2n-1, giving sum_S|b_beta|/(1-rho).
The middle contributes the sum of those bounds.
This records the seam at exponent zero and explains all factors in (4).

<a id="balanced-central-tail-transient"></a>
## Balanced tails and the tail-versus-interior tradeoff

L G0116 gives the symmetric tail Cesaro energy

    C_tail(c)=||c+(1-zeta)b/2||_2^2+A_n/4.

Its unique minimizer is c=-(1-zeta)b/2.
For that choice the interior coefficient in (3) is -(1+zeta)b/2, with squared norm

    B_n=sum_C |(1+zeta_beta)b_beta|^2/4=W-A_n/4.       (5)

The last equality uses |1+zeta|^2+|1-zeta|^2=4 at each unit-circle root.
Define the finite constant

    D_P=sum_(beta!=gamma in C)
           2|b_beta||b_gamma|/|1-beta conjugate(gamma)|,
    K_bal=D_P+2HT.

For all n>=1 the balanced solution obeys

    sum_(j=-n)^(-1)e_j^2 >= n(W-A_n/4)-K_bal.          (6)

Indeed an off-diagonal geometric sum on an interval has modulus at most 2/|1-beta conjugate(gamma)|.
The balanced center coefficients have modulus at most |b_beta|, so their total error is at most D_P.
The center sum has pointwise modulus at most H, and |h+r|^2>=|h|^2-2|h||r|; now use (4).

Thus along the moving binomials whose A_n tends to zero in L G0117, the balanced interior has mean-square energy tending to W>0, even though its two-tail Cesaro energy tends to zero.
An upper error bound D_P+2HT+T^2 follows by retaining |r|^2, so this assertion is an actual limit, not merely a liminf.

There is also a quantitative tradeoff for arbitrary center corrections.
Suppose C_tail(c)<=epsilon, where necessarily epsilon>=A_n/4.
Writing t=c+(1-zeta)b/2 gives ||t||_2<=sqrt(epsilon-A_n/4), whereas u_0=t-(1+zeta)b/2.
Hence

    ||u_0||_2^2 >=
       [max(0,sqrt(W-A_n/4)-sqrt(epsilon-A_n/4))]^2,
    ||u_0||_2<=sqrt(W)+sqrt(epsilon).                 (7)

For any center coefficient vector u, the off-diagonal energy error is at most K_0||u||_2^2, since sum_(beta!=gamma)|u_beta||u_gamma|<=(q-1)||u||_2^2.
Its pointwise sum is at most sqrt(q)||u||_2.
Consequently (7) gives an interior lower bound equal to n times its displayed square, minus

    K_0(sqrt(W)+sqrt(epsilon))^2
                    +2sqrt(q)(sqrt(W)+sqrt(epsilon))T.

If A_n and epsilon both tend to zero along successful delays, this again gives interior energy at least n(W-o(1))-O_P(1).
No cube hypothesis was used.

<a id="three-interval-optimized-transient"></a>
## No bounded center correction removes the three-interval cost

Let E_n(c) be the actual energy sum over [-2n,n-1], which has exactly 3n indices.
Its diagonal center energy per interval length is

    V_n(c)=||c||_2^2+||c-zeta b||_2^2
                              +||c+(1-zeta)b||_2^2
       =3||c-(2zeta-1)b/3||_2^2+s_n,
    s_n=(2W+A_n)/3,    2W/3<=s_n<=2W.                (8)

This is completion of squares in the coefficient space.
It respects conjugate symmetry, so its minimizer c_*=(2zeta-1)b/3 is a valid real correction.

Apply the preceding off-diagonal bound on each of the three intervals.
Together they lose at most K_0 V_n(c).
Each interval's pointwise center sum is bounded by sqrt(q)||u||_2<=sqrt(q V_n(c)).
Using (4) and again dropping the nonnegative |r|^2 term gives

    E_n(c)>=(n-K_0)V_n(c)-4sqrt(q)T sqrt(V_n(c)).

Put L=4sqrt(q)T and

    K_-=2W(K_0+1)+L^2/4,
    K_+=2K_0W+L sqrt(2W)+4T^2.

Young's inequality L sqrt(V)<=V+L^2/4 proves, for n>=K_0+1, the lower bound below.
For smaller n it follows from E_n(c)>=0 and s_n<=2W.
For the upper bound choose c_*, use V_n(c_*)=s_n<=2W, and bound sum |r_j|^2 by (2T)^2.
Thus for every n>=1,

    n s_n-K_- <= inf_(bounded real solutions) E_n
                  <= E_n(c_*) <= n s_n+K_+.           (9)

In particular every bounded real solution, without any constraint on the size of c, satisfies

    E_n(c)>=(2W/3)n-K_-.

Equation (9) determines the unrestricted finite-window minimum up to a fully specified O_P(1), uniformly in n.
It does not assert that the exact finite-window minimizer equals the diagonal minimizer c_*, or that either lies in the rounding cube.
The uniformity over c is important: making one interval inexpensive by shifting a center mode does not avoid the other two intervals' cost.

<a id="moving-binomial-cosine-window-cost"></a>
## What follows for products, and what does not

Only when the actual solution has |e_j|<=1/2 on the window may we apply cos(pi e_j)<=exp(-pi^2 e_j^2/2) as a nonnegative product estimate.
Under that condition on [-2n,n-1], (9) yields

    product_(j=-2n)^(n-1)cos(pi e_j)
       <=exp(pi^2 K_-/2) exp[-pi^2 n(2W+A_n)/6]
       <=exp(pi^2 K_-/2) exp[-pi^2 W n/3].             (10)

For the balanced solution with the cube condition only on [-n,-1], (6) similarly gives the bound exp(pi^2 K_bal/2) exp[-pi^2 n(W-A_n/4)/2].
Zero cosine factors are included in these inequalities.

The moving-binomial construction of L G0117 can make central jumps arbitrarily small while preserving an allowed integral-multiplier residue.
All its delays are covered here, including those restricted by its finite ideal period.
Its small tail energy therefore does not give a large cosine product on the entire growing transition window.
Residue admissibility still is not cube feasibility or identification with an actual rounded trace error.

These are fixed-P statements.
W, K_0 and T retain root-derivative, root-separation and noncentral-decay costs.
No bound uniform over varying P or in terms of Mahler measure alone has been proved.
No other forcing family, changed window, or coding without this bounded finite-forcing response is excluded.
The conclusion supplies no uniform Lehmer gap.

## Contribution and review scope

The coordinator proposed the balanced interior coefficient and its expected n-linear cost.
The assigned agent checked its indices and constants, derived the arbitrary-correction tail tradeoff, and proved the full three-interval optimization and uniform finite errors.
The kernel and tail-energy classification are separately proved in L G0116; the moving-family scope is separately proved in L G0117.
The assigned agent checked every constant and the product's cube guard.
No source, computation, identifier allocation or fixed-material edit is part of this draft.

The coordinator read and checked the complete assembled (1)--(10), finding no mathematical defect.
Its check covered the forcing and all three interval indices, the expanding and stable exponent ranges, T and 2T, the balanced and general tail tradeoffs, completion of squares, both branches of the Young lower bound, the K_- and K_+ constants, and every cosine-product factor and cube/residue boundary.
This is contributor verification because it proposed the balanced interior mechanism.

The separate ms25_source agent independently read and checked the complete assembled (1)--(10), finding no mathematical defect.
Its review covered the kernel forcing shift, three interval coefficients and seam exponents, T and 2T, the balanced B_n and D_P bounds, the arbitrary tail tradeoff, complex-pair and ordered cross-term counts, completion of squares, both ranges of n in the lower estimate, K_- and K_+, and every product prefactor and cube/residue restriction.
It treated L G0116 and L G0117 as their already fixed interfaces; it did not claim a fresh source audit or perform a mathematical computation in this review.
