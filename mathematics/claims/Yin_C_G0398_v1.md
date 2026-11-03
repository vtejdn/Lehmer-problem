---
author: Yin
---

# Paid canceled phase data give a direct unregularized Haar certificate and a sharp exponent obstruction

This retains the complete necessary mathematical argument from [complete original L368 oscillatory proof](../ledger/Yin_L_G0368_v1.md#oscillatory-moment-reuse-and-domain).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be a nonmonomial real integer polynomial after stripping monomial factors, with actual degree/span d>=1, nonzero endpoint coefficients and H=sum abs(a_j)>=2.
On the circle define B(z)=P(z)P(z^(-1)), phi(theta)=arccos(2B(exp(i theta))/H^2-1) in[0,pi] and mu_k=integral_T cos(k phi) with Haar probability.
Put V=z^dB, W=H^2z^d-V and C=zV'-dV, all nonzero integer polynomials; with the full monic rational gcd G=gcd(C^2,VW) and least common quotient-denominator normalizer q_0, define A=-q_0C^2/G,D=q_0VW/G,g=A/D.
Then (phi')^2=g off its endpoint/cusp set and D has no circle roots after complete cancellation; simple circle zeros are cusps with the stated nonzero one-sided slope, while all repeated and interior critical orders remain paid.
Let chi_i be all L distinct circle roots of A, each of multiplicity2M_i, and let J=16d+2 bound the complete monotonicity-piece partition.
For L>0 define M=max M_i and the exact positive algebraic g_0 from formula(4), including the full leading coefficient, every other-circle separation, all off-circle roots/multiplicities and ||D||_1; then set a=1/(M+1), K_P=L/pi+2J pi^(M-1)/(2^M g_0).
For L=0 use the separately specified full radial-product g_0, no artificial M, and a=1,K_P=2J/(pi g_0).
For every integer k>=1, abs(mu_k)<=min(1,K_P k^(-a)); the complete local proof retains the explicit4 integration constant, all removed arcs, ties, cusps and constant-rational-function branch.
For every integer N>=1 and 0<rho<=1 the absolute tail sum_(k>N)rho^k abs(mu_k)/k is at most R_N=(K_P/a)N^(-a), uniformly in the regularizer.
Consequently m(P)=log(H/2)+sum_(k>=1)(-1)^(k+1)mu_k/k and its complete finite truncation has absolute error at most R_N, giving the stated global finite lower certificate at exactly those rational original moments.
This allows repeated roots with their actual canceled multiplicities and does not assume squarefreeness for the general certificate.
For every integer n>=1, the actual monic squarefree reciprocal unit P_n=(1+z)^(2n)+z^n has no circle zero but has genuine canceled critical order M_i=2n-1 at theta=pi.
For that fixed input there is no finite C giving abs(mu_k)<=Ck^(-b) for all integers k>=1 when b>1/(2n); the full symmetrized-law/positive-Fejer proof includes all b ranges and possible oscillatory cancellations.
Thus no fixed positive absolute exponent follows for the whole squarefree reciprocal-unit class even with constants depending on the input; no irreducibility, genuine Salem or small-total-measure property of these controls is asserted.
All Sections1--6/(1)--(16), exact algebraic products and costs, classical attribution and actual source-depth/date conventions, fixed-input/finite-rational recurrence and entirely unrun root-data/moment/program boundary are retained.
No useful all-input conditioning, efficient root certification, near-one coverage, evaluated lower value or unrestricted gap follows.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:58 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact fixed single-Haar log expansion](Yin_C_G0379_v1.md#chebyshev-integer-moments) | Only the complete epsilon-independent rational moments, scalar/rho limits and integrable polynomial logarithm, with no old native control rerun. |
| dependency | [Canonical first-derivative attribution](../audits/literature/Tao26/Yin_U001.md#tao26-u001) | Only the retained monotone nonzero derivative and integration-by-parts mechanism, with undated-source/access-year basis; the complete explicit4 proof is local. |
| dependency | [Classical finite Fejer interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the actual finite squared-sum kernel identity and elementary normalization, not unrelated surveyed results or a new source proof audit. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:09 |
| status | proved |
| reason | Adopt the whole exact retained theorem after actual complete SELF checking, precise original-domain/normalization/source-interface verification and full original-review/author-check comparison. Every signed covariance, canceled critical datum, algebraic/cost and unrun/realization boundary remains explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0379_v1.md#chebyshev-integer-moments) | Only the complete epsilon-independent rational moments, scalar/rho limits and integrable polynomial logarithm, with no old native control rerun. |
| dependency | [Exact accepted input](../audits/literature/Tao26/Yin_U001.md#tao26-u001) | Only the retained monotone nonzero derivative and integration-by-parts mechanism, with undated-source/access-year basis; the complete explicit4 proof is local. |
| dependency | [Exact accepted input](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the actual finite squared-sum kernel identity and elementary normalization, not unrelated surveyed results or a new source proof audit. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0602_v1.md#oscillatory-current-whole-finding) | Complete exact current statement and entire retained mathematical argument, all original author/source/finite scopes and meaningful failures, without claimed independent review or new computation. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="oscillatory-moment-reuse-and-domain"></a>
## 1. Exact input, local reuse and classical attribution

The required conclusion is a finite algebraically paid bound for the ACTUAL Chebyshev moments, strong enough to remove the1/epsilon truncation cost from [L358](../ledger/Yin_L_G0358_v1.md#single-haar-moment-lower-certificate).
The local corrected `rg` screen for stationary phase, oscillatory integrals, monotone derivatives and Chebyshev tails found L358's worst-case geometric tail and unrelated oscillatory/Gauss-sum contexts, but no matching moment certificate.
The [L361 derivative account](../ledger/Yin_L_G0361_v1.md#circle-derivative-author-freeze) supplies circle-error information and exact simple-zero scope; it does not supply the oscillatory theorem below.
The Fejer identity later used for the obstruction is already checked in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md) and [L240](../ledger/Yin_L_G0240_v1.md), not a new kernel theorem.

The recognized classical input is the first-derivative van der Corput mechanism.
The reviewer-author directly read [Terence Tao, Lecture notes8 for247B](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf), printed/PDFpp4--5, especially Lemma2.4 and its integration-by-parts proof.
It states that a smooth phase with monotone derivative of modulus at least c has oscillatory integral O(1/(c lambda)), independent of interval length.
The inspected title names Tao but supplies no explicit publication date or version;2007 is NOT inferred from the server path.
This is classical attribution for the complete explicit4-constant proof in Section3, not an invocation of its higher-derivative or stationary-phase expansions.
Root subsequently registered/acquired the undated source as Tao26 and checked its selected source scope in [Tao26-U001](../audits/literature/Tao26/Yin_U001.md#tao26-u001), with provisional alpha-year2026 explicitly based on access rather than inferred publication.
This adds the responsible source locator without changing any mathematical dependency or formula.
No novelty claim or unseen external theorem is used.

Let P be an ACTUAL nonmonomial real integer polynomial after stripping monomial factors, with actual degree/span d>=1 and nonzero endpoint coefficients.
The intended application is squarefree reciprocal unit P, but the elementary finite certificate below also admits other integer P and repeated roots with their actual phase multiplicities.
Put

    B(z)=P(z)P(z^-1)=sum_(h=-d)^d b_h z^h,
    H=sum_j |a_j|, H>=2,
    phi(theta)=arccos(2B(exp(i theta))/H^2-1) in[0,pi],
    mu_k=integral_T cos(k phi(theta)).              (1)

The Haar integral is normalized by1/(2pi).
No degree/rank normalization, freedom between powers or spectral-gap assumption is introduced.
B is nonconstant: otherwise the unique extreme nonzero Fourier lag of |P|^2 would contradict its two nonzero endpoint coefficients.
Thus the finitely many endpoint/cusp points B=0 or H^2 do not occupy an interval.

<a id="exact-phase-critical-cancellation"></a>
## 2. Exact integer cancellation and all actual critical data

Define integral polynomials

    V(z)=z^d B(z)=P(z)z^d P(z^-1),
    W(z)=H^2 z^d-V(z),
    C(z)=z V'(z)-d V(z)=sum_h h b_h z^(h+d).

They have degree at most2d, and V,W,C are all nonzero.
Let G be the monic gcd of C^2 and VW over Q[z].
Divide exactly over Q[z], and let q_0 be the least positive integer clearing EVERY coefficient denominator in both quotients.
This explicit common representation normalizer gives integral polynomials

    A(z)=-q_0 C(z)^2/G(z), D(z)=q_0 V(z)W(z)/G(z),
    g(z)=A(z)/D(z).                               (2)

The common q_0 cancels from their ratio and from the lower phase constant below; it creates no integer norm income or uniform height bound.
If contents are canceled differently by a common nonzero constant, the ratio and all constants below are unchanged.
Away from B=0,H^2,

    (phi'(theta))^2=(B_theta')^2/[B(H^2-B)]
                   =-C(z)^2/[V(z)W(z)]=g(z).       (3)

Every root of D is OFF the unit circle.
To verify this and retain degeneracies, use the real-analytic nonnegative functions B and H^2-B.
At an endpoint value their finite vanishing order is even, say2h.
B_theta' and C then have order2h-1.
Accordingly C^2 has order4h-2 and VW has order2h; their gcd cancels the entire denominator order, leaving numerator order2h-2.
If P has a simple circle zero, B has order2 and the cancellation is COMPLETE: there is no residual phase-critical zero there.
In that case (3) has limiting positive value4|P'(zeta)|^2/H^2, while phi has the two one-sided slopes of modulus2|P'(zeta)|/H.
This treats a cusp as a cusp, not a fictitious smooth stationary point.
At an H^2 maximum of order2h, the remaining phase-critical order is h-1.
At an ordinary interior critical point where B_theta' has order m, the numerator order is2m.
All original endpoint, repeated-root and critical degeneracies are thus explicit.

Let chi_1,...,chi_L be ALL distinct unit-circle roots of A, with multiplicities2M_i.
These multiplicities are even because g is the continuous nonnegative squared phase derivative and D has no circle zeros.
Every such root comes from C, so L<=2d and M_i<=2d.
When L>0 put M=max_i M_i>=1 and

    eta_i=|lead(A)|
       product_(j!=i)(|chi_i-chi_j|/2)^(2M_j)
       product_(gamma:A(gamma)=0,|gamma|!=1)
                                      ||gamma|-1|^(mult_gamma),
    g_0=sqrt(min_i eta_i / ||D||_1)>0.             (4)

All off-circle roots and multiplicities occur in the product.
These are actual algebraic coefficient/root costs, not arbitrary independent constants or a claimed uniform separation.
They can be used with certified lower bounds on the displayed positive quantities; no root-data computation is asserted here.
At a point whose nearest chi-root is chi_i, the same full-factor nearest-root argument as L361 gives

    |phi'|^2=|A(z)|/|D(z)|
        >=(eta_i/||D||_1)|z-chi_i|^(2M_i).

Thus outside circular angular arcs of radius0<r<=1 around all chi_i,

    |phi'|>=g_0(2r/pi)^M.                         (5)

Indeed chord distance is at least2r/pi, and this lower base is at most1, so replacing each M_i by M weakens the bound safely.
Overlapping arcs are permitted; no disjointness claim is required.

When L=0 define instead

    g_0=sqrt[|lead(A)| product_gamma ||gamma|-1|^(mult_gamma)
                                                   /||D||_1]>0,

using every root of A, all off circle, and the empty product if A is constant.
Then |phi'|>=g_0 off the finitely many cusp points.
No M is assigned in this case.

The derivative of g along the circle is i z times

    K(z)/D(z)^2, K=A'D-AD'.

If K is nonzero it has degree at most8d-1 and hence at most8d-1 unit-circle zeros.
If K is identically zero, g is a positive constant and no partition at its zeros is made.
Cusps B=0,H^2 have at most2d distinct circle points altogether, because each has even polynomial multiplicity in V or W, each of degree at most2d.
Bad-arc boundaries number at most2L<=4d.
Partitioning the remaining circle also at these cusp points, at the zeros of K and at a chosen angular origin yields at most

    J=16d+2                                         (6)

open pieces, a deliberately conservative count.
On each piece phi is smooth, nonzero phi' has fixed sign and g' has fixed sign or is identically zero.
Hence phi' is monotone there.
This is a finite algebraically controlled partition, not an assumed generic critical-point hypothesis.

<a id="paid-oscillatory-moment-decay"></a>
## 3. Explicit oscillatory decay and its complete proof

On an interval where phi' is monotone and |phi'|>=lambda>0,

    |integral exp(i k phi(theta))dtheta|<=4/(k lambda). (7)

For completeness integrate by parts on a closed subinterval:

    integral exp(i k phi)
      =[exp(i k phi)/(i k phi')]_ends
        -(1/(i k))integral exp(i k phi)(1/phi')'.

The endpoints contribute at most2/(k lambda).
Since phi' is monotone and nonzero,1/phi' is monotone, and the integral of its absolute derivative is its endpoint variation, at most2/lambda.
This proves(7).
Exhaust an open piece by closed subintervals; the same bound survives by bounded convergence.
No uniform C2 bound near a cusp, no smooth extension through a cusp and no stationary-phase theorem is required.
This is the explicit form of the classical mechanism attributed in Section1.

For L>0 define

    a=1/(M+1),
    K_P=L/pi+2J pi^(M-1)/(2^M g_0).               (8)

Then for EVERY integer k>=1,

    |mu_k|<=min{1,K_P k^(-a)}.                   (9)

Proof.
Remove the union of chi-arcs of radius r.
Its normalized measure is at most Lr/pi and controls the omitted integral of exp(i k phi).
On at most J remaining pieces, use(5),(7), then divide the full integral by2pi.
This gives

    |mu_k|<=Lr/pi+2J pi^(M-1)/(2^M k g_0 r^M).

Take r=k^(-1/(M+1))<=1.
Both terms become the right side in(9).
The real-part integral defining mu_k is bounded by the modulus of that complex integral.
The trivial |mu_k|<=1 supplies the minimum.
All constants depend on the SAME original symbol and its exact canceled critical data.

When L=0, set a=1 and K_P=2J/(pi g_0).
The same piecewise argument without removed arcs gives |mu_k|<=min{1,K_P/k}, so(9) remains valid in this separately defined case.
Simple circle zeros never inflate M via an uncanceled B factor.

The method pays square-root decay a=1/2 whenever every genuine phase-critical zero has M_i=1.
Higher multiplicities are allowed and paid by their actual exponent; this condition has NOT been assumed universally for squarefree or reciprocal input.
The costs g_0,J,M and the algebraic input certification cannot be dropped when an input varies.

<a id="unregularized-integer-moment-certificate"></a>
## 4. A direct unregularized finite lower certificate

The decay(9) implies absolute convergence of sum |mu_k|/k and, for every N>=1 and every0<rho<=1,

    sum_(k>N) rho^k |mu_k|/k
       <=(K_P/a)N^(-a)=:R_N(P).                 (10)

This is the elementary integral comparison sum_(k>N)k^(-1-a)<=N^(-a)/a; it is UNIFORM in rho and hence in the regularizer.

Apply L358's exact log-Chebyshev expansion at epsilon>0, with its rho_epsilon and constant log[(sqrt(H^2+epsilon^2)+epsilon)/2].
Pass epsilon down to0.
The original nonzero polynomial has integrable circle logarithm, so m_epsilon->m by L358's checked argument.
Every finite term converges, while(10) supplies a uniform absolute tail.
Therefore

    m(P)=log(H/2)+sum_(k>=1)(-1)^(k+1)mu_k/k,
    |m(P)-[log(H/2)+sum_(k=1)^N(-1)^(k+1)mu_k/k]|
                                          <=R_N(P). (11)

Consequently

    m(P)>=log(H/2)+sum_(k=1)^N(-1)^(k+1)mu_k/k
                                      -(K_P/a)N^(-a). (12)

This is a correctly directed GLOBAL finite certificate for the ACTUAL single-Haar determinant, including its circle zeros.
It does not require choosing epsilon, an inverse spectral gap or an additional regularization-error bound.
All finite mu_k are the exact rational integer-coefficient moments retained in L358's recurrence.
The elementary log-series identity is reused and attributed there; the new point is the fully paid oscillatory remainder and its uniform regularizer removal.

A target tail r>0 is guaranteed at N>=(K_P/(a r))^(1/a).
This may be extremely large as degree, multiplicity or algebraic separations vary.
In particular no useful all-Salem bound for K_P or M, no practical root-data algorithm, no executed finite moment evaluation and no unrestricted Lehmer gap follows from(11)--(12).
Existing explicit regularized bounds can still outperform this certificate on an individual input.
The formula changes the coupled error mechanism; it is not a claim that every finite candidate is computationally cheap.

<a id="oscillatory-degeneracy-integer-obstruction"></a>
## 5. Squarefree reciprocal integer units do not guarantee a uniform moment exponent

For each integer n>=1 consider the ACTUAL monic reciprocal unit polynomial

    P_n(z)=(1+z)^(2n)+z^n, d=2n,
    H_n=2^(2n)+1.                                (13)

It is squarefree.
A common root of P_n,P_n' can be neither0 nor-1; substituting its root equation into the derivative gives

    P_n'(z)=n z^(n-1)(1-z)/(1+z)

AT such a root.
A zero derivative would force z=1, where P_n(1)=2^(2n)+1 is nonzero.
Reciprocal symmetry and constant1 are exact, and

    exp(-i n theta)P_n(exp(i theta))
         =1+[2cos(theta/2)]^(2n)>0.

Thus there are no unit-circle zeros; this is not a near-one Salem construction or a claim of irreducibility.
Its original phase is nevertheless highly degenerate.
Near theta=pi, writing t=theta-pi,

    B_n(theta)=1+2t^(2n)+O(t^(2n+2)),
    phi_n(theta)-phi_n(pi)=c_n t^(2n)+O(t^(2n+2)), c_n!=0. (14)

The phase value is strictly between0 andpi, so the arccos derivative there is nonzero.
This gives a genuine canceled critical order M_i=2n-1, rather than an endpoint artifact.
Hence squarefreeness, reciprocity and integer-unit normalization alone cannot justify setting a=1/2 in Section3.

In fact no fixed positive algebraic exponent can hold for all these inputs, even with an arbitrary constant depending on the input.
More precisely, for P_n there is NO bound |mu_k|<=C k^(-b) for all k>=1 with b>1/(2n).
The following positive-kernel argument proves the assertion without an uninspected stationary-phase asymptotic.

Let nu be the symmetrized probability law of +/-phi(theta) on the angle circle, so its kth Fourier coefficient is exactly mu_k.
From(14), for some actual c>0 and all sufficiently large L,

    nu([phi_n(pi)-1/L,phi_n(pi)+1/L])
                                      >=c L^(-1/(2n)). (15)

Indeed a theta interval of length proportional to L^(-1/(2n)) maps into that interval; symmetrization merely pays a factor1/2.
This is a fixed-input local conclusion and claims no uniform constant in n.

Use the classical finite Fejer polynomial

    F_L(t)=L^-1 |sum_(j=0)^(L-1)exp(i j t)|^2
          =1+2sum_(k=1)^(L-1)(1-k/L)cos(k t)>=0.

Its exact expansion is the same established elementary kernel identity in Smy08-U001/L240.
For |t|<=1/L, sin(L|t|/2)>=L|t|/pi and sin(|t|/2)<=|t|/2 give F_L(t)>=4L/pi^2.
Therefore, at x=phi_n(pi),

    nu([x-1/L,x+1/L])
       <=pi^2/(4L)[1+2sum_(k=1)^(L-1)(1-k/L)mu_k cos(kx)]. (16)

If |mu_k|<=C k^(-b) with0<b<1, the right side is O_C(L^(-b)) by integral comparison.
This contradicts(15) whenever b>1/(2n).
For b>=1, weaken it to any exponent in(1/(2n),1) and get the same contradiction.
Thus the claimed obstruction is proved, including possible oscillatory cancellations among other critical points.
It does not rely on a numerical leading coefficient of stationary phase or assert an exact asymptotic for mu_k.

These controls have growing degree and no stated small-total-measure or genuine Salem-minimal scope.
They rule out a universal k^-1/2 or ANY fixed positive exponent justified only by the broad squarefree reciprocal-unit class.
They do not rule out a fixed exponent on a separately proved near-one irreducible Salem subclass, an input-dependent exponent as in(9), or a more efficient signed-tail argument that avoids absolute moment decay.

## 6. Verification boundary and next gate

The full derivation is author-side and no mathematical program, J, parameter scan, algebraic root-data certification or exact finite lower-certificate evaluation has been run.
The classical first-derivative estimate and Fejer polynomial are explicitly attributed/reconstructed at their actual scope.
Root coordinates any final citation registration and independent review.

The changed next gate is concrete: for actual near-one irreducible Salem P, prove a useful uniform bound on canceled critical multiplicities/separations and the ratio |lead(A)|/||D||_1, or replace the absolute-moment tail by a still more structured signed estimate.
The actual simple circle derivatives have been canceled correctly, so a remaining failure is an actual phase geometry/coefficient-conditioning cost.
Integrality permits exact gcd and moment arithmetic; it does not by itself establish such uniform conditioning.
Retuning epsilon or launching a huge generic moment scan is unnecessary for the theoretical certificate and is not the selected next test.
