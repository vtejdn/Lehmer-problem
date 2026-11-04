---
author: Yin
---

# A constructive lower trace amplitude from rounded Green defects

The current complete mathematical proof is retained in [C307](../claims/Yin_C_G0307_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
The coordinator proposed separating two rounded Green kernels and testing their integral residue.
This note resolves the rounding boundary by an explicit dyadic multiplier, proves admissibility and the limiting product, and records the remaining quantitative cost.
No source acquisition, computation or novelty claim is involved.

Let alpha be a hyperbolic algebraic unit, with monic irreducible polynomial P of degree d and m=log M(P)>0.
Put O=Z[alpha], let O_K be the full integer ring, and write (Sx)_j=x_(j+1).
All root sums count both members of every complex pair.
We use the exact residue and open-cube converse of [L G0107](Yin_L_G0107_v1.md#rounded-defect-residue-class).

<a id="dyadic-green-rounding"></a>
## Removing every half-integer rounding boundary

The bilateral Green sequence is

    w_j=sum_(|beta|<1) beta^j/P'(beta),          j>=0,
    w_j=-sum_(|beta|>1) beta^j/P'(beta),         j<0.

It is real and exponentially decaying, and the coefficient identity in L G0107 gives

    P(S)w=delta_(-1).                                   (1)

Let

    D=|disc P|,    b=2^(v_2(D)),    D_odd=D/b.

The element D/P'(alpha) is integral: up to sign it is the product of the other conjugates of the integral element P'(alpha), and it belongs to K.
Therefore every D w_j is an algebraic integer, also at negative indices because alpha is a unit.
If b w_j were an integer plus 1/2, then D_odd b w_j would be a rational noninteger half-integer, contradicting its algebraic integrality.
Thus

    b w_j notin Z+1/2 for every j in Z.                 (2)

This argument does not assert that the unscaled w has no ties.
It supplies a fixed explicit numerator that avoids all of them; if D is odd, b=1 suffices.

Choose the unique nearest integer q_j to b w_j, and set

    e_j=b w_j-q_j,    s=||e||_infinity,
    a=1/2-s,          E=sum_j e_j^2.

The integer sequence q has finite support, since w tends to zero at both ends.
Every coordinate of e has absolute value less than 1/2 by (2), and its tails tend to zero, so the supremum is strictly less than 1/2.
Also e is not identically zero: otherwise b w=q would give b delta_(-1)=P(S)q, whose residue in O is b=0, an impossibility.
Consequently

    0<s<1/2,    0<a<1/2,    0<E<infinity.              (3)

For explicit tail constants put

    rho=max(max_(|beta|<1)|beta|,
            max_(|beta|>1)|beta|^(-1))<1,
    C=b sum_beta |P'(beta)|^(-1).

Nearest-integer error is at most the distance to zero, so

    |e_j|<=|b w_j|<=C rho^|j|,
    E<=C^2(1+rho^2)/(1-rho^2).                          (4)

In particular E is the rounded energy.
The pointwise inequality gives E<=b^2||w||_2^2, not the reverse.
A lower bound on the unrounded Green energy alone does not give a lower bound on E, or the upper control of E needed to improve (11).

All margin data are finite algebraic data.
For example choose an integer J_0>=1 with C rho^J_0<1/4.
Outside |j|<J_0 the error is less than 1/4, while the finite set inside has no ties by (2).
Thus a can be bounded below by the minimum of 1/4 and those finitely many positive distances to the rounding boundary.
This is an exact finite prescription, not a uniform lower bound for that margin across polynomials.

<a id="admissible-separated-green-defects"></a>
## The finite quotient supplies admissible separated pairs

By L G0107, P'(alpha)O_K is contained in O.
Hence I=2P'(alpha)O_K is an ideal of O of finite index.
The class of alpha is a unit in the finite ring O/I; let h>=1 be its multiplicative order.
In particular,

    alpha^h=1 mod I,
    h<=|O/I|=2^d D/[O_K:O]<=2^d D.                    (5)

The equality follows by taking the norm of 2P'(alpha) on O_K and then the lattice index.
It is not an unramifiedness assumption.

For a positive multiple n of h set

    e^(n)=e-S^n e,
    z_0=b delta_(-1)-P(S)q,
    z_n=z_0-S^n z_0,
    theta_n=b(1-alpha^n)/(2P'(alpha)).

The multiplier theta_n is in O_K, and is nonzero because alpha is not a root of unity.
The residue map Phi(z)=sum_j z_j alpha^(-j-1) satisfies Phi(S^n z)=alpha^n Phi(z), so

    P(S)e^(n)=z_n,
    Phi(z_n)=b(1-alpha^n)=2P'(alpha)theta_n.             (6)

To verify the other admissibility condition explicitly, choose J>=1 with C rho^J<=a/2 and take n>=2J.
For each j, at least one of |j| and |j+n| is at least n/2.
Its corresponding error has size at most a/2; the other has size at most s.
Therefore

    ||e^(n)||_infinity<=s+a/2=1/2-a/2<1/2.             (7)

Equations (6)--(7) and the L G0107 converse prove that e^(n) is exactly the rounded stable-trace error of the integral multiplier theta_n.
This is not merely a small real solution of an integer recurrence.
One may take n=h ceil(2J/h); then 2J<=n<2J+h<=2J+2^d D.
All larger multiples of h also become admissible.

<a id="green-product-lower-amplitude"></a>
## An actual positive lower amplitude

Define

    c_0=product_(j in Z) cos(pi e_j)>0.

The product is positive because s<1/2, e is in l2, and log cos(pi x)=O(x^2) near zero.
The amplitudes of the admissible multipliers above obey

    c_P(theta_n)=product_j cos(pi(e_j-e_(j+n)))
                      ->c_0^2                         (8)

as n tends to infinity through multiples of h.

Here is a proof that does not interchange an uncontrolled infinite product and a limit.
Write L(x)=log cos(pi x).
For every fixed t<1/2, the function L on [-t,t] has |L''|<=pi^2 sec^2(pi t) and L'(0)=0.
The mean-value integral and Cauchy--Schwarz therefore give

    |sum L(x_j)-sum L(y_j)|
      <=[pi^2 sec^2(pi t)/2]
                   (||x||_2+||y||_2)||x-y||_2          (9)

whenever both sequences lie in that interval and in l2.
Truncate e to |j|<=R.
For n>2R the two truncated translates have disjoint support, so the sum of L on their difference is exactly twice the truncated sum of L(e_j), using evenness.
The l2 truncation error of their difference is at most twice the tail norm.
For large n, (7) gives the common bound t=1/2-a/2 for the untruncated difference; the truncated, disjoint difference is bounded by s<t.
Applying (9) makes the error tend to zero uniformly in those n as R tends to infinity.
This proves (8).

In particular, with the same supremum as L G0109,

    boxed: c_opt(P)>=c_0^2>0.                          (10)

No maximizing multiplier is asserted to exist.
This inequality follows from an explicit admissible sequence, not from compactness of a multiplier lattice.
In entropy applications every theta_n is fixed while the word length tends to infinity.
Only afterwards is the multiplier supremum used.
No uniform bound on the multiplier-dependent finite-time offsets, and no moving-multiplier finite-time estimate, is needed or asserted.

The lower bound can be given a simple tail/margin form.
The same second derivative estimate at t=s yields L(x)>=-pi^2 x^2/[2 cos^2(pi s)] for |x|<=s.
Since cos(pi s)=sin(pi a), (4) gives

    c_opt(P)>=c_0^2
      >=exp[-pi^2 E/sin^2(pi a)]
      >=exp[-pi^2 C^2(1+rho^2)/
                    ((1-rho^2)sin^2(pi a))].          (11)

For an individual admissible n in (7), rather than the limiting supremum, the bound ||e-S^n e||_2^2<=4E and the margin a/2 give

    c_P(theta_n)>=exp[-2pi^2 E/sin^2(pi a/2)]>0.       (12)

<a id="relaxed-residue-amplitude-equivalence"></a>
## Removing the prescribed residue up to squaring

The coordinator contributed the following extension.
Define A_free(P) to be the supremum of product_j cos(pi e_j) over all nonzero finite integer forcings z for which

    e=P(S)^(-1)z,    ||e||_infinity<1/2,

without imposing the residue condition on Phi(z).
This set is nonempty: z_0 and e above already belong to it.
Every such e is real and has exponential tails, since it is a finite sum of translates of w.
Its product is therefore strictly positive.

The residue Phi(z) cannot be zero.
Otherwise the L G0107 kernel identity would give z=P(S)q for a finite integer q.
Invertibility gives e=q, and the open cube forces q=0, contrary to z nonzero.

For each such z choose the same period h from (5) and let n tend to infinity through multiples of h.
Set z_n=z-S^n z and e_n=e-S^n e.
Then

    Phi(z_n)=(1-alpha^n)Phi(z)
                    in 2P'(alpha)O_K minus {0}.

The inclusion uses the ideal property of I in O; nonvanishing uses Phi(z)!=0 and alpha^n!=1.
Exponential tails and the strict margin for e give eventual open-cube membership exactly as in (7).
The converse thus makes e_n an actual integral multiplier error.
The proof of (8)--(9), with the constants of this fixed forcing, gives the limit product(e_n)->product(e)^2.
Taking suprema yields

    boxed: A_free(P)^2<=c_opt(P)<=A_free(P).            (12a)

The second inequality holds because every actual rounded trace defect belongs to this larger set.
No supremum needs to be attained.
In particular the known c_opt<1 also implies A_free<1.

There is no increase of numerator Mahler measure in this conversion.
In the Laurent convention Z(t)=sum_j z_j t^(-j-1),

    Z_n(t)=(1-t^n)Z(t),
    M(Z_n)=M(Z),                                      (12b)

where Laurent Mahler measure is unchanged by clearing a monomial.
The equality follows from multiplicativity and M(1-t^n)=1.
The number of nonzero coefficients is at most twice that of Z; its exponent span can grow.
Neither the period nor the separation length is claimed to be bounded uniformly over inputs.

<a id="green-amplitude-budget-obligation"></a>
## What the construction supplies and what still needs control

The construction applies to every hyperbolic irreducible algebraic unit with positive Mahler measure.
It resolves both arithmetic admissibility and possible half-integer ties for a constructive Green-kernel lower bound.
It does not use all-power degree preservation, reciprocity, a bounded number of expanding conjugates, or a small-measure premise.

Let A(P) denote the last exponential in (11).
The already proved [convolution amplitude budget](Yin_L_G0109_v1.md#optimizing-convolution-fourier-tests) therefore gives the explicit necessary inequalities

    sup_(k>=1) k^2 g(A(P)^k)<=L_eff C_entropy(m),        (13)

where C_entropy(m)=(5/12)(exp(2m)-1)^2(1-exp(-4m)).
The Green constant C in (4) is different from this entropy constant.

No degree-independent estimate is proved for D, b, the root-derivative sum, rho, or the rounding margin a.
In particular (11) can be too small to contradict (13); positivity alone does not do so.
The precise next arithmetic obligation is to control these costs, or to find a better arbitrary nonzero integral forcing with small response energy and a useful open-cube margin.
By (12a), its prescribed integral-multiplier residue need not be solved separately: the conversion loses at most a square in product amplitude at the level of the supremum, and preserves numerator Mahler measure.
The integer-forcing and open-cube constraints remain essential.
There is no claim of a Lehmer gap, and the argument does not include unit-circle conjugates.

## Original contribution and actual checks

The complete original base, addition, contributor and necessary-input checking account is retained in [R546](../audits/reviews/Yin_R_G0546_v1.md#complete-original-l110-checking-account).
Its original inputs, date, mathematical scopes and verdicts remain unchanged, with the exact base-versus-addition and finding-specific relationships.
