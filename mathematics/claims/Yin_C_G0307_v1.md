---
author: Yin
---

# Admissible separated Green defects and constructive trace amplitude lower bounds

This retains the complete original2026-10-07 [L110 proof](../ledger/Yin_L_G0110_v1.md),including the later relaxed-residue addition12a–12b.
The assigned ms25_source agent supplied the tie-removal/admissibility/product proof; the coordinator supplied the initial separated-kernel construction and the relaxed-residue extension.
The original base,addition and necessary-input checking scopes remain in the formal review linked by L110.
No source,computation or Task is newly executed.

## Statement

Let alpha be a hyperbolic algebraic unit, P monic irreducible of degree d,m=log M(P)>0,O=Z[alpha].
Let w be the actual bilateral Green kernel with P(S)w=delta_(-1).
Put D=abs(disc P),b=2^(v2(D)).
Then b w_j is never a half-integer.
Its unique nearest-integer error e=bw-q has finite integer q,strict margin
a=1/2-norm(e)_infinity in(0,1/2),and rounded energy E in(0,infinity).
For

    rho=max(max_stable abs(beta),max_expanding abs(beta)^(-1)),
    C=b sum_beta abs(P'(beta))^(-1),

abs(e_j)<=C rho^abs(j) and E<=C²(1+rho²)/(1-rho²).
These data are input dependent; the rounded energy is bounded above by b² times the unrounded energy,not conversely.

The ideal I=2P'(alpha)O_K is contained in O and has finite index
|O/I|=2^d D/[O_K:O]<=2^d D.
Let h be the order of alpha mod I.
For every sufficiently large positive multiple n of h,

    theta_n=b(1-alpha^n)/(2P'(alpha)) is in O_K minus{0},
    e-S^n e is its exact rounded trace error.

If C rho^J<=a/2 and n>=2J,the error norm is at most1/2-a/2.
One may take n=h ceil(2J/h)<2J+2^dD.
The proof uses both exact residue and the open rounding cube.

Put c0=product_j cos(pi e_j)>0.
Along these admissible multiples n,

    c_P(theta_n) tends to c0²,
    c_opt(P)>=c0²>=exp(-pi² E/sin²(pi a))
       >=exp(-pi² C²(1+rho²)/((1-rho²)sin²(pi a))).

The complete proof gives uniform l2 logarithmic-product continuity and the individual finite bound
c_P(theta_n)>=exp(-2pi²E/sin²(pi a/2)).
Each multiplier is fixed before the entropy-time limit; no uniform moving-multiplier boundary or optimizer is asserted.

Let A_free(P) be the supremum of product cos(pi e_j) over all nonzero finite integer forcings z with e=P(S)^(-1)z and norm(e)_infinity<1/2,without the prescribed residue.
Then

    A_free(P)²<=c_opt(P)<=A_free(P)<1.

The residue of such a nonzero open-cube forcing cannot be zero.
Separated translates restore the actual nonzero multiplier residue,lose at most a square of amplitude at the supremum,and preserve numerator Laurent Mahler measure:
Z_n(t)=(1-t^n)Z(t),M(Z_n)=M(Z).
Sparsity at most doubles,but exponent span and period need not be uniformly bounded.
The explicit lower amplitude obeys the prior convolution budget; no degree-free cost control or uniform Mahler gap is proved,and unit-circle inputs are excluded.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:39 |
| status | open |
| reason | Whole original dyadic tie removal, arithmetic separated-pair admissibility, complete product-limit/lower-bound proof and relaxed-residue extension retained; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire hyperbolic integral Green-defect construction, exact finite dyadic/period/margin/tail costs, actual amplitude lower bound and fixed-multiplier limits, plus arbitrary integer-forcing residue relaxation up to squaring with Laurent Mahler/sparsity/span boundaries. |
| argument | [Complete argument](#argument) | Full original1–13 including12a–12b: dyadic algebraic-integrality tie exclusion, exact ideal index/residue/shift, two-tail open cube, controlled l2 logarithmic-product continuity, both amplitude constants and nonattained suprema, arbitrary-forcing conversion and revised arithmetic budget. |
| dependency | [Exact defect residue and converse](Yin_C_G0304_v1.md#rounded-defect-residue-class) | Complete Phi quotient, nonzero2P'(alpha)O_K class and unique open-cube inverse criterion; no arbitrary real forcing is silently an actual integral multiplier. |
| dependency | [Integral trace product and fixed-multiplier scope](Yin_C_G0298_v1.md#algebraic-trace-multiplier) | Exact positive bilateral amplitude and its admissible-multiplier supremum/fixed-time order; the lower construction and residue relaxation are fully proved here. |
| dependency | [Actual convolution amplitude budget](Yin_C_G0306_v1.md#optimizing-convolution-fourier-tests) | Exact sup_k k²g(c_opt^k)<=L_eff C_entropy(m),used only for13 with the displayed constructed lower amplitude and distinct Green constant. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:44 |
| status | proved |
| reason | Adopt the entire original dyadic Green/admissible separated-defect lower construction and relaxed-residue12a–12b extension after actual whole self-review; preserve every discriminant,index,period,tail,margin,product-limit and fixed-multiplier cost without a uniform Mahler claim. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire hyperbolic integral Green-defect construction, exact finite dyadic/period/margin/tail costs, actual amplitude lower bound and fixed-multiplier limits, plus arbitrary integer-forcing residue relaxation up to squaring with Laurent Mahler/sparsity/span boundaries. |
| argument | [Argument](#argument) | Full original1–13 including12a–12b: dyadic algebraic-integrality tie exclusion, exact ideal index/residue/shift, two-tail open cube, controlled l2 logarithmic-product continuity, both amplitude constants and nonattained suprema, arbitrary-forcing conversion and revised arithmetic budget. |
| dependency | [Dependency](Yin_C_G0304_v1.md#rounded-defect-residue-class) | Complete Phi quotient, nonzero2P'(alpha)O_K class and unique open-cube inverse criterion; no arbitrary real forcing is silently an actual integral multiplier. |
| dependency | [Dependency](Yin_C_G0298_v1.md#algebraic-trace-multiplier) | Exact positive bilateral amplitude and its admissible-multiplier supremum/fixed-time order; the lower construction and residue relaxation are fully proved here. |
| dependency | [Dependency](Yin_C_G0306_v1.md#optimizing-convolution-fourier-tests) | Exact sup_k k²g(c_opt^k)<=L_eff C_entropy(m),used only for13 with the displayed constructed lower amplitude and distinct Green constant. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0546_v1.md#current-green-amplitude-finding) | Exact current full statement,complete retained original proof and all selected interfaces,self-reviewed; historical findings retain their actual old inputs and precise partial/contributor/whole relationships. |

## Complete retained argument

<a id="argument"></a>
Let alpha be a hyperbolic algebraic unit, with monic irreducible polynomial P of degree d and m=log M(P)>0.
Put O=Z[alpha], let O_K be the full integer ring, and write (Sx)_j=x_(j+1).
All root sums count both members of every complex pair.
We use the exact residue and open-cube converse of [C304](Yin_C_G0304_v1.md#rounded-defect-residue-class).

<a id="dyadic-green-rounding"></a>
### Removing every half-integer rounding boundary

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
### The finite quotient supplies admissible separated pairs

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
### An actual positive lower amplitude

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
### Removing the prescribed residue up to squaring

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
### What the construction supplies and what still needs control

The construction applies to every hyperbolic irreducible algebraic unit with positive Mahler measure.
It resolves both arithmetic admissibility and possible half-integer ties for a constructive Green-kernel lower bound.
It does not use all-power degree preservation, reciprocity, a bounded number of expanding conjugates, or a small-measure premise.

Let A(P) denote the last exponential in (11).
The already proved [convolution amplitude budget](Yin_C_G0306_v1.md#optimizing-convolution-fourier-tests) therefore gives the explicit necessary inequalities

    sup_(k>=1) k^2 g(A(P)^k)<=L_eff C_entropy(m),        (13)

where C_entropy(m)=(5/12)(exp(2m)-1)^2(1-exp(-4m)).
The Green constant C in (4) is different from this entropy constant.

No degree-independent estimate is proved for D, b, the root-derivative sum, rho, or the rounding margin a.
In particular (11) can be too small to contradict (13); positivity alone does not do so.
The precise next arithmetic obligation is to control these costs, or to find a better arbitrary nonzero integral forcing with small response energy and a useful open-cube margin.
By (12a), its prescribed integral-multiplier residue need not be solved separately: the conversion loses at most a square in product amplitude at the level of the supremum, and preserves numerator Mahler measure.
The integer-forcing and open-cube constraints remain essential.
There is no claim of a Lehmer gap, and the argument does not include unit-circle conjugates.
