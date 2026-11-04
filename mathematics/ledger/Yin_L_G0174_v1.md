---
author: Yin
---

# Salem dyadic energy, the plastic-family resultant and doubling-auxiliary universality

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's explicit instruction, following the complete reviews preserved below.
This combines completed D G0029, D G0038 and D G0039 without changing their mathematical statements or source boundaries.
G0001 remains active and unresolved; this is fixed support, not a Claim acceptance or Task-completion decision.

<a id="salem-arithmetic-fixed-scope"></a>
## Current adopted results and distinct limitations

- For every positive Salem minimal polynomial, the [exact damping identity](#salem-exact-damped-mixed-identity) expresses the original mixed coefficients as C_n=b_n b_(2n)+2r^n(1-r^(2n)), where r is the reciprocal exterior root.
  It transfers the full mixed resultant to the complete Abel dyadic energy with the explicit bounded correction.
  The [primitive plastic-family calculation](#plastic-fourth-mode-certificate) gives a positive original frequency-4N contribution gamma*d+O(1), with 0.021931<gamma<0.021932, supported by exact and validated J30 calculations and their recorded separate review/reruns.
- On P_N=t^N(t^3-t-1)+(1-t^2-t^3), N=9 modulo120 and N>=129, the [complete resultant reduction](#plastic-lehmer-resultant-reduction) proves R_(1,2)=2^(N+3) Res(L,t^(N-8)+1)>0 for the original degree-ten Lehmer polynomial L.
  The [complete energy limit](#complete-plastic-mixed-energy-limit) is E_Q=kappa*d+O(log N), with kappa=log(2lambda/(theta+1)) in (0.0119,0.012).
  The net contribution of the other original modes after removing the fourth-delay term tends to kappa-gamma<-0.01 per degree.
  The fixed residual polynomial's all-index estimate uses exactly the accepted Dim16-U001 interface; J35's finite controls do not prove that limit by extrapolation.
- For every monic reciprocal irreducible nontorsion unit polynomial P with constant coefficient one, the [doubling-auxiliary construction](#doubling-auxiliary-factor-universality) gives an integer seed f of degree at most2d+1 such that nonzero G_f=((f*)^2 f(t^2)+f^2 f*(t^2))/2 is integral and divisible by P.
  After removing its initial monomial the auxiliary is reciprocal of degree at most8d+4; the seed may also be primitive.
  The unnormalized representative has the stated coefficient-height lower bound, but the [content-normalization boundary](#retained-doubling-universality-argument) supplies no controlled primitive height, Mahler measure or complementary-factor cost.

The plastic family has measure tending to the fixed positive log(theta).
Its linear resultant surplus and signed energy do not establish a uniform near-one estimate.
Factor occurrence alone is also nonselective by the universality statement.
Ongoing D G0041's sparse-seed pilot is outside this retention and has not been adopted here.

The complete original bodies follow.
Their dated pending, self-check and future-work language preserves the state when written and is superseded only by this present adoption statement and the complete reviews.
Every formula, proof, contribution disclosure, corrected reuse finding and full review remains present; only heading depth and relative navigation are relocated.

<a id="retained-salem-energy-argument"></a>
## Degree-scale mixed Fourier contributions on primitive Salem families

Assigned AI resultant_research for Yin, 2026-10-10, under the shared resumed G0001 authorization.
This arithmetic round follows [D G0015's high-band localization](../claims/Yin_C_G0004_v1.md#growing-band-resultant-localization) and the [AM01 coefficient-bound screen](../audits/literature/AM01/readme.md#coefficient-growth-screen).
The direct derivations and same-author computations below are exploratory and self-checked; independent review and fixed adoption remain outstanding.

### Results and actual domain

Two results distinguish a genuine arithmetic input from the earlier relaxed angular controls.
First, for every positive Salem minimal polynomial, the original pair-specific mixed Fourier coefficients admit an exact expression in the damped power sums of D G0015.
Their full logarithmic sums differ by a bounded explicit correction.
Second, an accepted primitive irreducible Salem family of coefficient height one has a positive single-mode contribution proportional to its degree, at frequency four times its delay.
An exact algebraic certificate fixes the sign, and one actual degree-132 input is certified separately.

The family has total logarithmic Mahler measure tending to log(theta), where theta is the plastic number, rather than to zero.
A positive Fourier term does not lower-bound a signed full sum.
Neither result establishes new arithmetic surplus, excludes a genuinely near-one family, or resolves G0001.

<a id="salem-exact-damped-mixed-identity"></a>
### 1. An exact Salem reduction to the damped polynomial

Let P be a positive Salem minimal polynomial of degree d, with exterior root tau>1, reciprocal root tau^(-1), and remaining d-2 roots on the unit circle.
Write q=tau^(-1), m=log(tau), and

    U_n=sum_(|zeta|=1, P(zeta)=0) zeta^n,
    b_n=U_n+2q^n.

The conjugate-pair symmetry makes both sums real.
Here b_n is exactly the power sum of the damped roots z_i=exp(-|l_i|+i theta_i), so it is the coefficient used in the zero-free disk logarithm

    Q(w)=product_i(1-z_i w),
    log Q(w)=-sum_(n>=1)b_n w^n/n.

In particular this Q is the exterior-root-corrected object of [D G0015](../claims/Yin_C_G0004_v1.md#exact-damped-polynomial), not P evaluated at a smaller radius.
Retain the original mixed coefficient

    C_n=sum_(i,j) exp(-n|l_i-2l_j|)
                       cos(n(theta_i-2theta_j)).       (1)

Both real exceptional roots are positive and hence have phase zero.
Counting ordered pairs by type gives

    C_n=U_n U_(2n)+2q^n U_(2n)+2q^(2n) U_n
                         +2q^n+2q^(3n)
       =b_n b_(2n)+2q^n(1-q^(2n)).                   (2)

Indeed, unit-unit pairs give U_n U_(2n).
The two choices for the first exceptional root give 2q^n U_(2n), while the two choices for the second give 2q^(2n) U_n.
Among the four exceptional-exceptional pairs, two have |l_i-2l_j|=m and two have 3m.
This proves (2), with no replacement of a damping factor.

For each fixed P first take the Abel limit in the exact angular logarithmic part K of [D G0007](../claims/Yin_C_G0001_v1.md#doubling-exact-radial-angular-split).
Nonvanishing of its full mixed resultant ensures that this limit exists.
The correction in (2) is absolutely summable after division by n.
Therefore

    E_Q=-lim_(r up to 1) sum_(n>=1) r^n b_n b_(2n)/n,
    K=E_Q-2log(1+q+q^2),
    log|R_(1,2)|=(3d-2)m+E_Q-2log(1+q+q^2).         (3)

For the second equality use sum_(n>=1)(q^n-q^(3n))/n=log(1+q+q^2).
Thus 0<E_Q-K<2log3, independently of d, and the correction tends to 2log3 as m tends to zero.
The limit defining E_Q is justified by (2), not by unproved absolute convergence of its series.

Equation (3) is restricted to the positive Salem root configuration.
It does not extend unchanged to an arbitrary irreducible reciprocal unit with several exterior root pairs.
In its stated domain it gives a precise interface for further work on Q: the genuine floor |R_(1,2)|>=2^d forces

    E_Q >= d log2-(3d-2)m+2log(1+q+q^2).             (4)

This is a restatement of the existing arithmetic income in a simpler exact object, not additional income.
In particular a hypothetical near-one Salem sequence would require E_Q/d>=log2-o(1).

<a id="primitive-plastic-phase-moments"></a>
### 2. An actual primitive family and its degree-scale moments

Put

    f(z)=z^3-z-1,       f*(z)=1-z^2-z^3,
    P_N(z)=z^N f(z)+f*(z),
    N=9 mod120,        N>=129,        d_N=N+3.       (5)

The [complete cyclotomic classification in L G0038](Yin_L_G0038_v1.md#family-cyclotomic-factors), applied as in [L G0131](Yin_L_G0131_v1.md), proves that P_N itself is monic irreducible and Salem.
These fixed results also give theta<tau_N<4/3 and tau_N tending to theta, where theta is the real root of f.
Their upper root bound requires N>=16, which (5) satisfies.
There is no cyclotomic padding.
The six coefficients are 1 or -1, with no overlap because N>3.
The exponents 2 and 3 occur, so the support has greatest common divisor one and P_N is not a nontrivial substitution H(z^a).
Thus this control is distinct from the radical lifts considered earlier.
Its total measure tends to the fixed positive log(theta).

Define the rational circle map

    g(z)=-f*(z)/f(z),
    c_k=(1/(2pi)) integral_0^(2pi) g(exp(it))^k dt.   (6)

The cubic f has discriminant -23, one real root theta in (13/10,4/3), and two conjugate roots of modulus theta^(-1/2)<1.
Its reciprocal has one root inside the circle and two outside.
Neither has a circle zero.
On the circle, f*(z)=z^3 conjugate(f(z)); consequently |g(z)|=1.
The winding number of g is 1-2=-1.
It follows that one can write

    g(exp(it))=exp(i psi(t)),
    psi(t+2pi)=psi(t)-2pi,
    phi(t)=psi(t)+t,

with a smooth bounded 2pi-periodic real phi.
Every unit root zeta=exp(it) of P_N satisfies the exact equation

    zeta^N=g(zeta),
    (N+1)t-phi(t) in 2pi Z.                          (7)

For all sufficiently large N, the real function H_N(t)=(N+1)t-phi(t) is strictly increasing, and its increment over a period is 2pi(N+1).
It therefore yields exactly N+1 distinct unit roots in a half-open period.
Label their arguments by consecutive integers j so that H_N(t_j)=2pi j.
Equation (7) gives

    |t_j-2pi j/(N+1)|<=||phi||_infinity/(N+1).

Modulo a full period the comparison grid is the uniform (N+1)-point grid.
Hence these unit-root empirical measures converge to Haar measure.
More precisely, for each fixed smooth F, its sum over this set equals (N+1) integral F dmu+O_F(1), by the displayed displacement estimate and the ordinary uniform-grid Riemann-sum estimate.
This proof supplies the needed convergence directly; it does not invoke a height equidistribution theorem.

Use F=g^k, with fixed positive integer k.
The exact phase equation (7) now gives

    U_(kN)(P_N)=sum_unit g(zeta)^k=N c_k+O_k(1).     (8)

The c_k are real by conjugation symmetry.
Formula (8) concerns a moving frequency of order d_N, rather than a fixed Fourier mode; weak equidistribution alone would not justify substituting that moving character into the limit.

By (2), or by bounding the at most 4d_N-4 exceptional ordered pairs in (1), it follows that

    C_(kN)(P_N)/N^2 -> c_k c_(2k),
    [-C_(kN)(P_N)/(kN)]/d_N -> -c_k c_(2k)/k.       (9)

For the latter exceptional-pair bound, every summand has absolute value at most one, independently of n and tau_N.
Thus no uniform small-radial-error assumption is needed for (9).
The O_k(1) control in (8) also gives an O_k(1/N) error in the second normalized limit.

<a id="plastic-fourth-mode-certificate"></a>
### 3. Exact residue calculation and a positive mode

The constants in (6) can be calculated by one exterior residue.
Since g(infinity)=1, the residue of g(z)^k/z at infinity is -1.
Its only finite pole outside the circle is theta.
The residue theorem therefore gives

    c_k=1-Res_(z=theta) [g(z)^k/z].                  (10)

All finite poles inside the circle, including zero, are already included in this contour integral; none is dropped.
To evaluate the residue, write z=theta+t and

    g(theta+t)=H(t)/t,
    H(t)=[theta(theta+1)+(3theta^2+2theta)t
                         +(3theta+1)t^2+t^3]
                      /[(3theta^2-1)+3theta t+t^2]. (11)

The identity uses theta^3=theta+1, and the denominator at t=0 is nonzero.
The residue in (10) is exactly the coefficient of t^(k-1) in H(t)^k/(theta+t).
Finite formal series arithmetic in Q(theta) consequently proves

    c_4=(216755-364434 theta+94629 theta^2)/279841,
    c_8=(-33746367025-182673511531 theta
                         +168086028459 theta^2)/78310985281.   (12)

The exact root bracket

    13247179572447/10^13 < theta < 13247179572448/10^13

has negative and positive f values at its endpoints, respectively, with f strictly increasing there.
Rational interval substitution in (12) gives

    -0.358<c_4<-0.357,       0.245<c_8<0.246,
    0.021931 < -c_4 c_8/4 < 0.021932.                (13)

Here terminating decimals denote exact rational numbers.
For direct verification of the final interval, the reduced field element is

    -c_4 c_8/4 = (3732920400112960
                    +3910162439241763 theta
                    -5031232757467695 theta^2)
                   /3811239031655708.               (14)

[J G0030](../computations/programs/Yin_J_G0030/readme.md) retains the exact formal-series calculation, coefficient reduction and rational interval checks.
A separate 400-bit Arb series implementation encloses c_1 through c_32; its decisive value is approximately 0.02193113542797359 for (14).
The sign in (13) rests on exact rational arithmetic, so it does not rely on a floating approximation or an unbounded numerical tail.

Combining (9) and (13) proves the actual-family conclusion

    -C_(4N)(P_N)/(4N) = gamma d_N+O(1),
    gamma=-c_4 c_8/4 in (0.021931,0.021932).          (15)

This is one positive term of the exact mixed Fourier expansion.
For completeness J G0030 also certifies an actual finite instance without approximating all unit roots.
At N=129, exact Newton recurrences provide integer s_516 and s_1032.
Exact rational endpoint signs isolate the unique exterior root tau_129 to width below 2^(-800); 1000-bit Arb arithmetic then forms U_n=s_n-tau_129^n-tau_129^(-n) and uses (2).
The result is

    -C_516(P_129)/(516*132)
       =0.02142602846843519960... > 1/50.            (16)

The retained interval handles the large cancellation in the Newton-sum subtraction.
The established family theorem supplies irreducibility and Salem geometry; the finite program does not independently classify factors.
Equations (15) and (16) are compatible but neither numerical checking nor a single finite instance is used to prove the asymptotic phase argument.

### Scope, search and next discriminating question

This result obstructs a proposed universal estimate making each degree-scale actual-root mixed Fourier term o(d), even if the proposed domain is restricted to primitive irreducible Salem polynomials of coefficient height one and uniformly bounded total measure.
Such a proposal would fail on (5).
This is a precise counterpressure statement, not a refutation of an existing adopted Claim.
The total measure in (5) does not tend to zero, so the result does not obstruct an estimate that uses m->0 essentially.
Nor does it address whether arbitrarily small-measure inputs must have tall coefficients.

Positive and negative terms occur: the certified phase moments give -c_1 c_2<0, while (13) is positive.
Thus selecting the latter alone supplies no lower bound for E_Q, K, log|R_(1,2)| or a normalized arithmetic quotient.
No interchange of the infinite Fourier sum with N tending to infinity is made.
In particular (15) cannot be summed over k without separate uniform and nonresonant-frequency control.

The useful new bridge for a genuinely near-one Salem sequence is (3): the complete pair-specific energy is the dyadic correlation of the exact Q power sums, up to a universal bounded correction.
A next discriminating target is an upper estimate for that complete signed correlation using both the integer boundary relation |Q|=exp(-m)|P| and the reciprocal Salem exterior-root correction.
It must distinguish m->0 from the fixed-m construction (5); controlling each Fourier coefficient separately or assuming all high terms have one sign would miss the phenomenon certified here.
This is a research target, not an asserted upper estimate.
The non-Salem reciprocal domain requires a separate analogue of (2) before such an argument could address unrestricted G0001.

The bounded reuse screen inspected D G0007/G0011/G0015, the plastic-family interfaces L G0038/G0131/G0137, the full-resultant convention L G0059, and the AM01 relevance screen.
No matching exact phase-moment/correction argument was found in that inspected set; no exhaustive search or novelty claim is made.
All new analytic ingredients are proved here and no new external theorem or literature artifact is adopted.
The authoring AI supplied these derivations and the three J programs.
The coordinator supplied the broad arithmetic question and received progress explanations; this document does not treat those exchanges as independent review.




The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0073_v1.md#separate-complete-local-review), with its original inspected scope and relationship.



<a id="retained-plastic-resultant-argument"></a>
## Complete mixed-resultant energy for the primitive plastic Salem family

Date: 2026-10-10.
New bounded arithmetic exploration by assigned resultant_research AI for Yin under the shared G0001 continuation.
This follows D G0029's individual degree-scale Fourier contribution, now targeting the entire normalized mixed energy for the actual primitive family P_N(z)=z^N f(z)+f*(z), f=z^3-z-1 and N=9 modulo120.
Fixed positive limiting measure is distinguished from a hypothetical near-one family.

### Input and result

Write

    f(z)=z^3-z-1,             h(z)=f*(z)=1-z^2-z^3,
    L(z)=z^10+z^9-z^7-z^6-z^5-z^4-z^3+z+1,
    P_N(z)=z^N f(z)+h(z),     d_N=N+3,
    N=9 mod120,              N>=129,
    q=N-8.

The actual primitive irreducible Salem-family input is the already fixed [L G0038](Yin_L_G0038_v1.md#family-cyclotomic-factors), used in [L G0131](Yin_L_G0131_v1.md).
Its exterior root tau_N satisfies theta<tau_N<4/3 and tends to the plastic root theta of f.
There is no removed cyclotomic factor.
The polynomial L is exactly the original degree-ten Lehmer minimal polynomial, with exterior root lambda in (117/100,118/100) and eight unit-circle roots, as retained in [L170](Yin_L_G0170_v1.md#lehmer-infinite-core-theorem).
Put mu=log(lambda).

Use all d_N conjugates in the powered resultant R_(1,2), as in [L59](Yin_L_G0059_v1.md#mixed-power-resultant-identities).
The complete exact reduction proved below is

    |R_(1,2)(P_N)|=2^(d_N) |Res(L,z^q+1)|.             (1)

In fact both sides before taking absolute values are positive in this domain.
Consequently the normalized Frobenius quotient is precisely a plus-cyclic norm of the fixed Lehmer unit; it is not an isolated Fourier mode or an estimate with omitted conjugates.

The already accepted [Dim16 all-index cyclic-norm bound](../claims/Yin_C_G0854_v1.md#dim16-cyclic-all-index) then gives

    log|R_(1,2)(P_N)|=d_N log2+q mu+O(log q).          (2)

For the exact original damped-polynomial energy E_Q of [D29](#salem-exact-damped-mixed-identity), the resulting complete limit is

    E_Q(P_N)/d_N -> kappa,
    kappa=log2+mu-3log(theta)
         =log(2lambda/(theta+1))>0.                  (3)

This is a fixed-positive-measure family: log M(P_N) tends to log(theta)>0.
The result gives a genuine linear normalized resultant quotient on this actual family, but supplies neither a near-one example nor a uniform estimate over variable Salem inputs.
New deductions here are self-checked and awaiting independent review.

<a id="plastic-lehmer-resultant-reduction"></a>
### 1. Exact elimination with every resultant factor retained

The first identity below is already retained in [L38's odd-order elimination row](Yin_L_G0038_v1.md#family-cyclotomic-factors).
It was independently rediscovered in this round.
Direct polynomial expansion checks it and the separately derived second identity in Z[z]:

    h(z)^2 f(z^2)+f(z)^2 h(z^2)=2z L(z),
    h(z)-z^8 f(z)=(1-z)L(z).                          (4)

There are no common zeros of f and h.
More precisely,

    Res(f,h)=-1,       Res(f,1-z)=f(1)=-1,
    Res(L,f)=Res(f,L)=1.                              (5)

Here is a direct check of the unit constants.
At a root u of f, h(u)=-u(u+1).
The products of the three roots u and of u+1 are respectively 1 and -f(-1)=1, so their h product is -1.
The second identity in (4), evaluated on those same roots, gives Res(f,h)=Res(f,1-z)Res(f,L), hence Res(f,L)=1.
Interchanging the degrees 3 and 10 introduces no sign.
Thus (5) does not rely on a numerical resultant computation.

Since d_N is even, resultant interchange between f and P_N has sign (-1)^(3d_N)=1.
Evaluation at the f roots therefore gives

    Res(P_N,f)=Res(f,P_N)=Res(f,h)=-1.                (6)

For each root alpha of P_N, f(alpha) is nonzero and alpha^N=-h(alpha)/f(alpha).
Thus

    P_N(alpha^2)
       =[h(alpha)^2 f(alpha^2)+f(alpha)^2 h(alpha^2)]/f(alpha)^2.

Taking products over all d_N roots, with multiplicities, and using (4)--(6) proves

    Res(P_N,P_N(z^2))=Res(P_N,2zL)/Res(P_N,f)^2
                    =2^(d_N) Res(P_N,L).             (7)

The factor Res(P_N,z) is one, because P_N has even degree, is monic and has constant coefficient one.
The denominator in (7) is also one; neither can carry an unrecorded exponential cost.
On the other hand

    Res(P_N,P_N(z^2))
      =product_(i,j)(alpha_i^2-alpha_j)
      =(-1)^(d_N^2) R_(1,2)(P_N)
      =R_(1,2)(P_N).                                 (8)

This explicitly distinguishes polynomial substitution from powering its complete root multiset and accounts for their sign here.

Interchange with L again has positive sign.
At a root z of L, the second identity in (4) gives h(z)=z^8 f(z), so

    P_N(z)=z^8 f(z)(z^q+1).

The factor Res(L,z^8) is one, since L is a monic even-degree unit polynomial, and Res(L,f)=1 by (5).
Consequently

    Res(P_N,L)=Res(L,P_N)=Res(L,z^q+1).               (9)

Equations (7)--(9) establish (1).
No degree loss or factor deletion is hidden in this calculation.
L has no root of unity, so its last resultant is nonzero.
Its two real-root factors lambda^q+1 and lambda^(-q)+1 are positive, and each complex pair contributes an absolute square.
Thus the resultant in (9) and R_(1,2) in (8) are actually positive.
The algebraic reduction also holds at N=9, q=1; the stricter N>=129 bound is used for the uniform root bounds and asymptotic family scope.

<a id="complete-plastic-mixed-energy-limit"></a>
### 2. Complete growth from an already accepted fixed-polynomial estimate

For this one fixed L put C_n=|Res(L,z^n-1)|.
Its irreducible degree is ten, it is a nontorsion unit, and 0<mu<1.
It therefore satisfies the full hypotheses of the retained Dim16-U001 specialization.
There is a fixed K_0 such that for every n>=1,

    n mu-K_0 log(2n) <= log C_n <= n mu+10log2.        (10)

The accepted source bound is the reported Baker--Wustholz interface at its existing statement/applicability scope.
Its transcendence proof and absolute numerical constant were not audited there and are not newly audited or calibrated here.
The guarded n=1 case in that unit remains valid; no uninspected multivariable convergence theorem is used.

Multiplicativity of resultants gives the exact plus-cyclic identity

    A_q:=|Res(L,z^q+1)|=C_(2q)/C_q.

Both C values are positive.
Equation (10) yields

    q mu-K_0 log(4q)-10log2 <= log A_q
                         <= q mu+K_0 log(2q)+10log2. (11)

The elementary bound |1+z^q|<=2 max(1,|z|)^q improves the right side to q mu+10log2 if desired.
Thus log A_q=q mu+O(log q), proving (2).
This is an all-q limit for a fixed degree-ten residual polynomial.
The exponent q tends to infinity; no claim q<=C deg(L), and no invocation of L168 under such a false condition, is made.
The growing original degree d_N and the fixed residual degree ten have different roles.

It remains to convert this resultant growth to the complete energy.
Define m_N=log(tau_N) and r_N=tau_N^(-1).
D29's exact per-input identity is

    E_Q(P_N)=log|R_(1,2)(P_N)|-(3d_N-2)m_N
                                +2log(1+r_N+r_N^2). (12)

The energy here is the Abel limit of the complete signed dyadic correlation of the original Q power sums.
D29 proved its existence from nonvanishing of the mixed resultant and the exact Salem correction.
We first use (12) for each fixed N, and only then let N tend to infinity.
No Fourier series is truncated, no sum of limiting mode coefficients is substituted, and no Abel/N limit exchange occurs.

Dividing (12) by d_N, using q/d_N=(N-8)/(N+3) tending to one, m_N tending to log(theta), and the bounded correction, proves (3).
There is also the fixed-input error statement

    E_Q(P_N)=kappa d_N+O(log N).                      (13)

For completeness the required rate of m_N follows directly from the family equation.
On theta<=tau_N<4/3, f'(t)>=3theta^2-1 and -h(t)<=85/27.
Since tau_N^N f(tau_N)=-h(tau_N),

    0<tau_N-theta
       <=[85/(27(3theta^2-1))] theta^(-N).

Thus m_N-log(theta)=O(theta^(-N)), and multiplying this error by d_N does not spoil (13).
All O constants in (10)--(13) concern the fixed f and L and may include the uncalibrated accepted logarithmic-form constant.

### 3. The sign, cancellation, and actual arithmetic content

The identity theta^3=theta+1 gives kappa=log(2lambda/(theta+1)).
The retained rational bounds lambda>117/100 and theta<4/3 already imply

    2lambda/(theta+1)>351/350>1.

So the complete normalized energy is strictly positive without a numerical approximation.
[J G0035](../computations/programs/Yin_J_G0035/readme.md) additionally certifies

    0.0119 < kappa < 0.012,
    kappa=0.0119060695987979093132786328095...,
    kappa/log(theta)=0.04234028315108191908....        (14)

The two strict decimal endpoints are exact rationals.
Exact polynomial identities and direct full powered-resultant controls at N=9 and N=129 both pass; their quotient values A_q are respectively 1 and 62723699809.
The former is an initial exact-floor instance, not a contradiction to eventual linear growth.
The intervals and finite controls do not prove the source-dependent all-index limit by extrapolation.

The quotient |R_(1,2)|/2^(d_N)=A_(N-8) has logarithm mu*d_N+O(log N), giving an actual linear arithmetic surplus for this family.
The original radial term is simultaneously about 3d_N log(theta).
The residual kappa is the full signed-energy balance after that radial contribution is subtracted, not the entire logarithmic resultant quotient.

In contrast, [D29's fourth-delay term](#plastic-fourth-mode-certificate) has coefficient gamma=-c_4 c_8/4 approximately 0.0219311354.
Its positive contribution is larger than the complete constant kappa.
Let K_N denote the complete original pair-specific angular energy, so K_N=E_Q(P_N)-2log(1+r_N+r_N^2).
Removing just that fourth-delay term gives

    [K_N+C_(4N)(P_N)/(4N)]/d_N -> kappa-gamma
       =-0.01002506582917568187... < -0.01.           (15)

The expression on the left is exactly the per-input Abel sum of all the other original Fourier terms.
Thus they have a negative normalized net contribution even though the total limit is positive.
This statement uses the difference of two proved finite-input quantities and their separate limits, rather than summing termwise limits.
The bounded correction between E_Q and K_N does not affect their normalized limits.
J35's validated interval check certifies the strict rational upper bound in (15).

This calculation supplies a concrete benchmark for a proposed upper bound such as E_Q<=C*d*m+o(d): any such bound covering this family would need C>=kappa/log(theta).
It supplies no bound in the other direction, no evidence that a candidate inequality extends to m tending to zero, and no same-exponent coverage for arbitrary inputs.
In particular the original Lehmer polynomial's appearance as a residual algebraic factor is an exact identity for the plastic family, not a reduction of unrestricted Lehmer's problem to that fixed example.

### Reuse, evidence and contribution boundary

The local screen inspected the actual family interfaces L38/L131, L59's full-root resultant convention, D29's exact damping identity, and retained cyclic-norm sources.
Dim16-U001 already supplies the needed all-index estimate with its guards; no new literature acquisition or source adoption is necessary.
The initial bounded search incorrectly reported no retained occurrence of both identities in(4).
On 2026-10-10 the independent reviewer located the first identity exactly in L38's odd-order elimination table.
That identity is reused/rediscovered here; the mistaken absence statement is withdrawn.
The z^8 reduction and complete resultant/energy deductions have their stated derivation below, without an exhaustive literature or novelty claim.

The assigned arithmetic AI rediscovered the fixed numerator and its original-Lehmer factor already retained in L38, and derived the z^8 reduction and complete resultant factors used here.
After the exact reduction was communicated, the coordinator independently identified the expected energy expression and emphasized its distinction from the earlier one-mode coefficient and the fixed residual degree.
The complete derivation, accepted-source specialization and computation here were supplied by the assigned AI.
These exchanges are not independent review.
The material remains a proof draft until separately reviewed; no Claim or fixed-ledger promotion is asserted.

The authoring AI ran J35 successfully on 2026-10-10.
Its finite-resultant verification uses exact integer polynomial arithmetic and a direct squared-root polynomial from the even/odd parts of P_N.
For N=9 it additionally verifies the substitution resultant in (8).
Exact rational root brackets of width below 2^(-280) and 320-bit Arb arithmetic certify (14)--(15); the fixed family/root-configuration interfaces supply root uniqueness.
No infinite Fourier tail is numerically truncated or evaluated, and no new original-source proof is claimed.

<a id="plastic-resultant-collaborator-review"></a>
### Complete coordinator check with contribution disclosed

On 2026-10-10 the coordinating AI for Yin read and checked the complete proof, all equations(1)--(15), the exact accepted Dim16-U001 source interface, the fixed L38/L131/L137 family conditions, D29's energy and fourth-mode conclusions, and the full J35 program.
No mathematical defect was found.
The coordinator had identified the expected limiting expression after receiving the author's exact reduction, so this is a complete collaborator check rather than noncontributor review of the whole result.

The check verified both integer identities in(4), all unit resultants and their signs in(5)--(9), the distinct meanings of substituting z^2 and powering all roots, and the degree-dependent signs using d_N even.
The factor z and the f denominator each have norm one and do not hide costs.
The final plus-cyclic resultant is positive by the actual two-real/eight-circle conjugate configuration of L.
The existing Dim16 unit supplies the all-index bound at fixed degree ten, positive mu<1, and its stated external Baker--Wustholz boundary.
Its quotient C_(2q)/C_q gives both logarithmic error bounds in(11); the variable exponent q is not subject to L168's degree-linear restriction here.

The conversion uses the exact finite-input Abel identity before taking N to infinity.
The elementary derivative and -h bounds on [theta,4/3] give exponentially small tau_N-theta, sufficient for the O(log N) total-energy remainder.
The positivity ratio 351/350, the distinction between full quotient income and radial subtraction, and the sign of the remaining-mode limit kappa-gamma were checked directly.
The subtraction in(15) removes the positive contribution -C_(4N)/(4N) with the displayed plus sign and does not interchange infinite sums with the degree limit.

The coordinator separately reran J35 with its output redirected to a disposable task-local directory.
Both direct complete powered-resultant checks and every exact/validated constant passed.
Every mathematical result field matched the retained author JSON; the original output was unchanged.
The review checked the even/odd construction of the full squared-root polynomial, exact remainder/resultant arithmetic, rational sign brackets, propagated Arb intervals and the use of fixed root uniqueness.
This is a rerun of the fully inspected author implementation, not a new independent verifier or a proof of the asymptotic by finite testing.
Noncontributor whole-proof review remains separately assigned; G0001 remains unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0073_v1.md#plastic-resultant-independent-review), with its original inspected scope and relationship.



<a id="retained-doubling-universality-argument"></a>
## Every reciprocal unit factor occurs in an integral doubling auxiliary

Date: 2026-10-10.
Direct bounded exploration by the coordinating AI for Yin.
The trigger is the arithmetic agent's exact observation in [D38](#retained-plastic-resultant-argument) that the plastic seed's unnormalized doubling numerator equals twice a monomial times the original Lehmer polynomial.
This material asks whether occurrence as such an auxiliary factor imposes a restrictive new class.
It proves that factor occurrence is universal for the present reciprocal unit domain, while explicitly leaving height and cofactor cost uncontrolled.
No source novelty claim is made.

<a id="doubling-auxiliary-factor-universality"></a>
### Statement and scope

Let P in Z[t] be monic, reciprocal, irreducible and nontorsion, of degree d with constant coefficient1.
Here reciprocal means t^d P(1/t)=P(t), and nontorsion means its roots are not roots of unity.
For any nonzero f in Z[t] of actual degree k, write f*(t)=t^k f(1/t), and define

    G_f(t)=[f*(t)^2 f(t^2)+f(t)^2 f*(t^2)]/2.             (1)

Then there is an explicitly constructed f of degree k<=2d+1 such that G_f is a nonzero integer polynomial, P divides G_f in Z[t], and deg G_f<=8d+4.
After removing its maximal monomial factor, G_f is reciprocal.
Neither f nor G_f is asserted to be monic or primitive.
No estimate making the complementary factor's Mahler measure small is supplied.

The division by2 in(1) is integral for every integer f, independently of the construction: modulo2 the identities f(t^2)=f(t)^2 and f*(t^2)=f*(t)^2 make the two numerator summands equal.
This is exactly the elementary Frobenius divisibility behind the normalization, not an extra norm-income theorem.

### 1. A full powered polynomial and an integral construction

Let alpha_1,...,alpha_d be all conjugates of a root alpha of P, and retain every multiplicity in

    Q(t)=product_(i=1)^d(t-alpha_i^2).

This is a monic reciprocal polynomial in Z[t] of degree d and constant coefficient1.
It need not be the minimal polynomial of alpha^2; no power-degree-preservation assumption is made.
The fixed nonzero full mixed resultant interface [L59](Yin_L_G0059_v1.md) gives

    R=Res(P,Q) != 0,              |R|>=2^d.               (2)

In particular P and Q are relatively prime over Q.
The integral Sylvester matrix has determinant R up to the harmless basis-order sign.
Applying its adjugate to the coefficient vector of the constant polynomial gives integer polynomials A,B of degrees less than d such that, after fixing that sign,

    A(t)P(t)+B(t)Q(t)=R.                                 (3)

This elementary adjugate statement can also be read as clearing denominators in the degree-bounded polynomial Bezout identity; the actual signed resultant, rather than an unspecified denominator, suffices.
Define

    f(t)=t B(t)Q(t)+(t^2-1) A(t)P(t).                    (4)

All coefficients are integral and deg f<=2d+1.
Reducing modulo the two polynomials gives

    f(t)=R t                  modulo P(t),
    f(t)=R(t^2-1)             modulo Q(t).               (5)

In particular f is nonzero, since f(alpha)=R alpha!=0.

### 2. Exact vanishing at the target factor

Reciprocity puts alpha^(-1) among the roots of P, while alpha^2 and alpha^(-2) are roots of Q.
Formula(5) therefore yields

    f(alpha)=R alpha,          f(alpha^(-1))=R alpha^(-1),
    f(alpha^2)=R(alpha^4-1),   f(alpha^(-2))=R(alpha^(-4)-1).

The actual degree k of f fixes its reversal, so

    f*(alpha)=R alpha^(k-1),
    f*(alpha^2)=-R alpha^(2k-4)(alpha^4-1).

Substituting these exact values in the numerator of(1) gives

    R^3 alpha^(2k-2)(alpha^4-1)
       -R^3 alpha^(2k-2)(alpha^4-1)=0.

Thus P divides G_f over Q.
Since P is monic and G_f has integer coefficients, monic polynomial division gives the divisibility in Z[t].
The values f(alpha^2) and f*(alpha^2) are also nonzero because alpha is nontorsion, although their nonvanishing is not needed for this cancellation itself.

### 3. The constructed auxiliary cannot vanish identically

For completeness, a vanishing polynomial in(1) would not constitute factor occurrence.
Suppose its numerator were identically zero and put

    r(t)=f*(t)/f(t),          s(t)=-r(t) in Q(t).

Then r(t^2)=-r(t)^2, or s(t^2)=s(t)^2.
Every nonzero rational function satisfying this equation is a monomial t^j with integer j.
Indeed, expand at zero as s(t)=c t^j(1+a t^l+...), where l>=1 is the first nonzero higher term if there is one.
Comparing leading coefficients gives c=c^2 and hence c=1.
If a first higher term existed, the right-hand side would have coefficient2a at degree l relative to its leading term, while the left-hand side has no such term because its first higher degree is2l.
This contradiction shows that the normalized Laurent expansion is exactly1, and rational identity then gives s=t^j.

Consequently r(t)=-t^j.
But the computed values at alpha give r(alpha)=alpha^(k-2).
Therefore alpha^(k-2-j)=-1.
If the exponent is zero this says1=-1; otherwise it makes alpha a root of unity.
Both are impossible.
Thus G_f is nonzero.

### 4. Reciprocal shape, cost boundary and consequence

Formal reversal at length4k gives

    t^(4k) G_f(1/t)=G_f(t).

If ell is the order of vanishing at zero, its actual degree is4k-ell.
Removing t^ell leaves a reciprocal polynomial of degree4k-2ell.
Since P(0)=1, P remains a factor after this removal.
The degree bound in the statement follows from k<=2d+1.

This is a factor-universality statement with a linear degree bound.
It does not realize P as the whole auxiliary, make its complementary factor cyclotomic, bound coefficient height favorably, or preserve small Mahler measure.
The construction uses a Bezout identity cleared by the full resultant R, whose absolute value already has the floor2^d.
The unnormalized representative does have the elementary height bound recorded next, but normalization can remove part of that scalar.
Neither fact precludes a more efficient representation.
The construction has no controlled Mahler-cost theorem.

In particular, the appearance of the original Lehmer polynomial in D38's fixed plastic calculation is mathematically concrete but occurrence somewhere in this auxiliary class alone cannot restrict the unrestricted reciprocal-unit problem: every target in that domain occurs.
A useful strengthened route would need an exact auxiliary identity with controlled cofactor measure or a restriction on the permitted seeds that is both restrictive and covers the target inputs.
D38's special fixed seed retains its much sharper exact factorization and full-energy interpretation; this general construction does not replace or weaken that calculation.

### 5. Coefficient height and its content-normalization boundary

Write m=log M(P), H(f)=max_j|f_j|, and ||f||_circle=max_(|z|=1)|f(z)|.
Choose a conjugate alpha with |alpha|>=1, which exists because the unit constant coefficient makes the product of all conjugate moduli one.
Since f(alpha)=R alpha and k>=1, the exterior polynomial bound gives

    ||f||_circle >= |R| |alpha|^(1-k)
                  >= |R| exp(-(k-1)m)
                  >= 2^d exp(-2d m).

The exterior bound follows by applying the maximum-modulus principle to z^k f(1/z) on the unit disk.
Also ||f||_circle<=(k+1)H(f), so for the specific unnormalized representative(4),

    H(f)>=2^d exp(-2d m)/(2d+2).                         (6)

If P has a unit-circle conjugate, direct evaluation there improves this to H(f)>=2^d/(2d+2).
This describes the constructed representative itself, after any cancellations of its coefficients, but it is not a scale-invariant height obstruction.

Indeed let c>0 be its integer coefficient content and let f_0=f/c be primitive.
Since alpha is an algebraic unit,

    R/c = f_0(alpha)/alpha

is both rational and an algebraic integer, so c divides R.
Put D=R/c, a nonzero integer.
Then f_0(alpha)=D alpha, f_0(alpha^2)=D(alpha^4-1), and G_(f_0)=G_f/c^3 remains a nonzero integer polynomial divisible by P.
Its degree is unchanged.
Thus the factor-universality statement can also use a primitive seed.
The elementary lower bound for that primitive seed replaces |R| by |D|; there is no conclusion here forcing |D| to retain the exponential floor2^d.
Such a conclusion cannot be obtained merely by dividing the resultant floor by an uncontrolled content.

Finally even a coefficient-height lower bound would not itself lower-bound Mahler measure or the complementary factor's measure.
Equation(6) is therefore a precise normalization/cost boundary, not a hidden proof of a gap or a prohibition on controlled alternative seeds.

### Contribution and checking

The arithmetic agent supplied the special plastic auxiliary identity that motivated the question.
The coordinator alone supplied the general Sylvester/Bezout construction, its evaluations, nonvanishing proof, reciprocal-degree argument and the explicitly normalized height boundary above.
The only reused non-elementary mathematical interface is L59's already accepted full mixed-resultant nonvanishing/floor at its recorded scope; no new literature acquisition or computation is needed.
The complete direct proof has been self-checked and is ready for separately assigned noncontributor review.
G0001 remains active and unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0073_v1.md#doubling-auxiliary-universality-independent-review), with its original inspected scope and relationship.



<a id="auxiliary-reuse-scope-clarification"></a>
### Subsequent reuse-scope clarification

On 2026-10-10 the D38 independent reviewer located the plastic numerator identity in L38's already retained [odd-order elimination table](Yin_L_G0038_v1.md#family-cyclotomic-factors).
The arithmetic agent's rediscovery was the actual trigger for this draft; the identity itself is older retained mathematics.
No novelty was claimed here, and it is not a premise of the general construction beyond motivating its question.

The coordinator also directly reread [L139's half-degree delay encoding](Yin_L_G0139_v1.md#universal-half-degree-delay-encoding).
That earlier theorem realizes every reciprocal core of even degree at least four as the unique noncyclotomic factor of a delay polynomial with a monic coprime nonreciprocal seed of half the core degree plus one, together with explicit coefficient costs.
Its auxiliary is t^N f+f*, distinct from this draft's nonlinear doubling auxiliary G_f.
The older encoding already establishes that an unrestricted seed presentation alone is not selective.
The current proof checks the corresponding coverage and normalization boundary for G_f specifically; it neither replaces L139 nor claims to be the first such presentation-universality observation.
This comparison is a later reuse clarification, outside the preceding review's proof scope and without a mathematical change to Sections1-5.

<a id="salem-arithmetic-retention-map"></a>
## Fixed-retention map and actual review scope

The coordinator supplied D29's separate complete noncontributor proof/program review and actually reran its three programs, as recorded in that body.
D38's author and coordinator contributions remain disclosed separately; its whole noncontributor review is the assigned orbit_research AI's written proof/code review, without an additional rerun or independent-verifier claim.
D39's construction and height argument are the coordinator's work, followed by the same assigned AI's complete noncontributor written review.
This retention implements the coordinator's adoption after those reviews; it does not relabel collaborator checks.

D38's provenance correction is preserved in full: its first polynomial identity was already retained in L38's odd-order elimination table and was rediscovered in this round.
D39's later L38/L139 reuse clarification remains separately labelled outside its preceding review's proof scope; it does not change the reviewed Sections1--5.
No new literature novelty, external-source proof audit or computational rerun is claimed by this retention.

| Retired working identity | Complete fixed home and reviews |
| --- | --- |
| D G0029 | [Entire argument](#retained-salem-energy-argument), [exact damping identity](#salem-exact-damped-mixed-identity), [phase moments](#primitive-plastic-phase-moments), [fourth-mode certificate](#plastic-fourth-mode-certificate), [complete separate review](../audits/reviews/Yin_R_G0073_v1.md#salem-phase-mixed-local-review) |
| D G0038 | [Entire argument](#retained-plastic-resultant-argument), [resultant reduction](#plastic-lehmer-resultant-reduction), [complete energy limit](#complete-plastic-mixed-energy-limit), [collaborator check](#plastic-resultant-collaborator-review), [complete noncontributor review](../audits/reviews/Yin_R_G0073_v1.md#plastic-resultant-independent-review) |
| D G0039 | [Entire argument](#retained-doubling-universality-argument), [universality statement](#doubling-auxiliary-factor-universality), [complete noncontributor review](../audits/reviews/Yin_R_G0073_v1.md#doubling-auxiliary-universality-independent-review), [subsequent reuse clarification](#auxiliary-reuse-scope-clarification) |

The three completed drafts were retired after their complete mathematical bodies and review accounts were retained here and their incoming consumers were updated.
Continuing D41 is neither retired nor promoted.
