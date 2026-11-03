---
author: Yin
---

# Exact Salem dyadic energy and a positive primitive plastic-family mode

The complete original D29 statement, all equations(1)--(16), proofs and actual finite-evidence boundaries are retained from [L174](../ledger/Yin_L_G0174_v1.md#retained-salem-energy-argument).
The original author supplied the analytic derivations and three J30 programs.
The original coordinator assigned the broad arithmetic question, received progress explanations, read the whole proof/programs and reran them as actually recorded in [R73](../audits/reviews/Yin_R_G0073_v1.md#salem-phase-mixed-local-review).
That historical whole finding's actual initial target context is not established, so its independent-review relationship remains unknown.
The current registration does not turn the original author-program reruns into independent implementations.
Necessary fixed family/full-resultant interfaces retain their exact scopes.
No new source or native execution is used.

## Statement

Let P be a positive Salem minimal polynomial of degree d, exterior root tau>1, reciprocal root q=tau^(-1), and d-2 unit-circle roots zeta.
Put m=log(tau), U_n=sum_unit zeta^n, b_n=U_n+2q^n, and Q(w)=product_i(1-exp(-|l_i|+i theta_i)w), with alpha_i=exp(l_i+i theta_i) the full conjugate list.
For every integer n>=1 the exact original mixed coefficient is

    C_n=sum_(i,j)exp(-n|l_i-2l_j|)cos(n(theta_i-2theta_j))
       =b_n b_(2n)+2q^n(1-q^(2n)).

Its complete dyadic energy exists as a finite-input Abel limit, and

    E_Q=-lim_(r up to1)sum_(n>=1)r^n b_n b_(2n)/n,
    K=E_Q-2log(1+q+q^2),
    log|R_(1,2)(P)|=(3d-2)m+E_Q-2log(1+q+q^2).

Here R_(1,2) is the nonzero full-conjugate powered resultant.
The existing2^d floor transfers to

    E_Q>=dlog2-(3d-2)m+2log(1+q+q^2),

and 0<E_Q-K<2log3.
No absolute convergence at the boundary is assumed.

Let f=z^3-z-1, h=f*=1-z^2-z^3, theta the real root of f, and

    P_N=z^N f+h, N=9 mod120, N>=129, d_N=N+3.

These are the actual monic irreducible primitive Salem polynomials, without a removed cyclotomic factor, with coefficient height one, theta<tau_N<4/3 and tau_N tending to theta>1.
For g=-h/f on the unit circle and fixed integer k>=1, put c_k=integral g^k dmu.
Then

    U_(kN)(P_N)=N c_k+O_k(1),
    -C_(kN)(P_N)/(kN)=(-c_k c_(2k)/k)d_N+O_k(1).

The proof uses the exact phase equation zeta^N=g(zeta), a bounded smooth lifted phase with winding-1, and quantization of all N+1 unit roots.
The constants have the exact exterior-residue formula and finite Q(theta) calculation retained below.
In particular,

    -C_(4N)(P_N)/(4N)=gamma d_N+O(1),
    gamma=-c_4 c_8/4,
    0.021931<gamma<0.021932.

The exact rational algebraic certificate and the separate retained N=129 validated control

    -C_516(P_129)/(516*132)>1/50

have their actual scopes below and in J30.
This is one positive contribution to a signed full sum; it supplies no lower bound for that complete sum.
The total measure tends to the fixed positive log(theta), and no estimate for a near-one family or interchange of an infinite sum with N tending to infinity is asserted.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:14 |
| status | open |
| reason | Retain the complete exact positive-Salem Abel/damping transfer and full primitive-family phase/residue/fourth-mode proof with original finite-control, source and signed-energy limits. Actual complete current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete exact energy and primitive-family theorem](#statement) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| argument | [Complete original mathematical argument](#argument) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| dependency | [Full-conjugate powered-resultant theorem](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates with full multiplicities, nonvanishing for distinct positive exponents on an irreducible nontorsion unit and the doubling2^d Frobenius floor; no minimal-polynomial degree-preservation assumption or new income. |
| dependency | [Complete plastic-family classification](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact P_N=z^N(z^3-z-1)+(1-z^2-z^3) cyclotomic classification, root configuration and theta<tau_N<4/3 for N>=16; the stated progression has no cyclotomic padding. |
| dependency | [Actual no-padding progression](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem/actual degree N+3 and fixed-positive-measure family interface; unrelated triple-return or mass conclusions are not used. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:21 |
| status | proved |
| reason | Adopt after the actual entire current statement/proof and necessary fixed-input/native-certificate self-check of all positive-Salem exact damping/Abel equations and primitive-family phase/residue/fourth-mode conclusions. Preserve the complete signed-sum, fixed-positive-measure, finite-control and no-limit-exchange boundaries. The current whole finding is SELF and does not close the original whole UNKNOWN arrangement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| argument | [Exact retained argument](#argument) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates with full multiplicities, nonvanishing for distinct positive exponents on an irreducible nontorsion unit and the doubling2^d Frobenius floor; no minimal-polynomial degree-preservation assumption or new income. |
| dependency | [Exact retained dependency](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact P_N=z^N(z^3-z-1)+(1-z^2-z^3) cyclotomic classification, root configuration and theta<tau_N<4/3 for N>=16; the stated progression has no cyclotomic padding. |
| dependency | [Exact retained dependency](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem/actual degree N+3 and fixed-positive-measure family interface; unrelated triple-return or mass conclusions are not used. |
| review | [Complete actual current whole self finding](../audits/reviews/Yin_R_G0613_v1.md#current-salem-phase-energy-finding) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. Actual whole relationship is self-reviewed; all original complete noncontributor UNKNOWN and known collaborator/author SELF scopes remain separately retained. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:02 |
| status | proved |
| reason | Adopt the new isolated complete finding for the entire exact positive-Salem damping/Abel and primitive-family phase/residue/fourth-mode argument, including finite-pair Abel/radial justification and exact original-parameter read-only J30 reproduction. Preserve signed-full-sum, fixed-positive-measure, source and limit-order boundaries; old UNKNOWN/SELF findings remain historical and are not reclassified. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| argument | [Complete selected argument](#argument) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. |
| dependency | [Exact accepted input](Yin_C_G0231_v1.md#mixed-power-resultant-identities) | Only all actual conjugates with full multiplicities, nonvanishing for distinct positive exponents on an irreducible nontorsion unit and the doubling2^d Frobenius floor; no minimal-polynomial degree-preservation assumption or new income. |
| dependency | [Exact accepted input](Yin_C_G0248_v1.md#family-cyclotomic-factors) | Only the exact P_N=z^N(z^3-z-1)+(1-z^2-z^3) cyclotomic classification, root configuration and theta<tau_N<4/3 for N>=16; the stated progression has no cyclotomic padding. |
| dependency | [Exact accepted input](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding) | Only N=9mod120/N>=9 itself irreducible Salem/actual degree N+3 and fixed-positive-measure family interface; unrelated triple-return or mass conclusions are not used. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0618_v1.md#isolated-salem-energy-finding) | Entire positive-Salem exact damping/Abel theorem and primitive plastic-family phase-moment/fourth-mode theorem, original equations(1)--(16): full ordered-pair/root multiplicities, finite-input Abel existence and explicit correction/radial resultant transfer, existing2^d floor without new income, N=9mod120/N>=129/actual degree N+3/no cyclotomic padding/primitive support/fixed positive limiting measure, exact phase quantization and fixed-k moving-frequency error, all residues/exact c4,c8/gamma rational certificates, actual N129 Newton/validated-interval evidence at its retained depth, and signed-full-sum/near-one/no-limit-exchange boundaries. Entire current statement and argument are independently reviewed in the new finding; this includes the full current comparison at its explicitly stated domain where present. Original reviewer reruns remain distinct from the new bounded read-only reproductions, and old historical relationships are unchanged. |

## Complete retained argument

<a id="argument"></a>

<a id="retained-salem-energy-argument"></a>

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

In particular this Q is the exterior-root-corrected object of [D G0015](Yin_C_G0004_v1.md#exact-damped-polynomial), not P evaluated at a smaller radius.
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

For each fixed P first take the Abel limit in the exact angular logarithmic part K of [D G0007](Yin_C_G0001_v1.md#doubling-exact-radial-angular-split).
Nonvanishing of its full mixed resultant ensures that this limit exists.
More explicitly, put w_ij=exp(-|l_i-2l_j|+i(theta_i-2theta_j)).
Each |w_ij|<=1, and w_ij!=1 because the full resultant is nonzero.
For 0<r<1, log|1-r w_ij|=-sum_(n>=1)r^n Re(w_ij^n)/n.
There are finitely many pairs, so summing this identity and taking r upwards to one gives the exact K by continuity at every nonzero 1-w_ij.
For the radial data m,-m and d-2 zeros, the same ordered-pair count gives (1/2)sum_(i,j)|l_i-2l_j|=(3d-2)m.
This supplies the finite-input Abel justification and radial value used below without an infinite-series/degree-limit exchange.
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

The [complete cyclotomic classification](Yin_C_G0248_v1.md#family-cyclotomic-factors), applied as in [the complete no-padding family interface](Yin_C_G0336_v1.md#a-progression-with-no-cyclotomic-padding), proves that P_N itself is monic irreducible and Salem.
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

## Signed-sum scope and actual retained evidence

A universal assertion that every degree-scale actual-root mixed Fourier term is o(d) would fail on this primitive height-one bounded-measure family.
This is counterpressure to that proposed assertion, without a refutation of an existing adopted Claim.
The measure tends to log(theta)>0, so the example supplies no obstruction to an estimate that uses m tending to zero essentially.
There are both positive and negative original terms; selecting the fourth-delay term does not lower-bound E_Q, K, the full logarithmic resultant or its normalized arithmetic quotient.
No infinite sum is interchanged with the degree limit or summed over k from these separate fixed-k estimates.

J30 retains the exact formal-series reduction/rational signs, the 400-bit Arb 32-moment/16-product consistency evidence, and the single N=129 control using exact Newton sums through 1032, a tau bracket narrower than 2^(-800) and 1000-bit propagated cancellation intervals.
Those retained finite checks remain distinct from the written all-N proof.
The actual old reruns, unchanged author outputs, author contributions and original scope/search/future-question record remain in L174/R73/J30.
This construction performs no new run, independently written verifier, literature acquisition, formal proof or Task execution.
