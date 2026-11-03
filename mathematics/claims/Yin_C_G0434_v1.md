---
author: Yin
---

# Complete positive integer logarithmic moments and paid square-root tails

This retains the complete necessary mathematical argument from [the entire original L378 positive-logarithmic account](../ledger/Yin_L_G0378_v1.md#positive-log-moment-identity).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be any nonzero integer Laurent polynomial.
Strip only a Laurent monomial, preserving circle modulus, coefficient sum H=sum_j|a_j|>=1 and logarithmic Mahler measure, and let d be its actual resulting span.
On Haar probability measure on the circle put B(z)=P(z)P(z^(-1))=|P(z)|², Z=H²-P(z)P(z^(-1)) in Z[z,z^(-1)], and nu_n=integral(1-B/H²)^n for integers n>=1.
For every such input, including repeated roots and all scalar content,

    0<=nu_(n+1)<=nu_n<=1,
    nu_n=CT(Z^n)/H^(2n),
    m(P)=log(H)-(1/2)sum_(n>=1)nu_n/n.

The nonnegative series follows by monotone convergence despite the finite circle-zero set and signed individual Laurent coefficients.
For every integer N>=1, T_N=log(H)-(1/2)sum_(n=1)^N nu_n/n decreases to m(P) from above; the entire positive remainder is (1/2)sum_(n>N)nu_n/n.
A monomial P=a z^j has nu_n=0 and m(P)=log|a| exactly.
The original integer convolution retains support[-nd,nd], coefficient/denominator bit size O(n log(2H)) and O(N²d²) arithmetic operations through N; this is not a bit-operation or executed-computation claim.

For the following tail theorem assume the nonmonomial normalized P is squarefree, permitting arbitrary leading coefficient, degree1, nonreal roots and an empty circle-root set.
Let C contain all actual circle roots, A_zeta=|Pprime(zeta)|>0 and S=sum_(zeta in C)1/A_zeta.
Fix0<eta<1, put K=sum_(j=0)^d j²|a_j|, and choose disjoint proper circle arcs of positive radii r_zeta<=pi satisfying K r_zeta/2<=eta A_zeta.
The complete local Taylor proof gives |P(exp(i(theta_zeta+t)))|>=(1-eta)A_zeta|t| for |t|<r_zeta.
Retaining the leading coefficient and EVERY off-circle root, set

    b=|a_d| product_(zeta in C)2sin(r_zeta/2)
             * product_(|alpha|!=1)||alpha|-1|>0,
    rho=1-b²/H² in[0,1),
    C_P=H S/[2sqrt(pi)(1-eta)].

The arc complement is nonempty, possibly only endpoints, and b<=H; for empty C the first product is1 and S=0.
For every n>=1,

    nu_n<=C_P n^(-1/2)+rho^n.

Consequently for every N>=1,

    0<=T_N-m(P)<=C_P/sqrt(N)
           +rho^(N+1)/[2(N+1)(1-rho)] = R_N^+(P),
    T_N-R_N^+(P)<=m(P)<=T_N.

At rho=0 the geometric term is0; with no circle roots only the geometric term remains.
All finite moments are the same exact original rational coefficient data, and logs/constants require rigorous enclosure before an actual numerical certificate is claimed.
In characteristic zero every nonconstant irreducible input is squarefree, so this includes the unrestricted irreducible hard core without assuming any real trace or circle conjugate.

For each FIXED squarefree P,

    lim_(n->infinity)sqrt(n)nu_n=H S/(2sqrt(pi)).

The proof rescales each fixed simple-zero arc and uses its complete Gaussian dominator and the fixed complementary rho.
It does not interchange changing-polynomial/radius limits.
For any circle root of multiplicity r>=2, an actual local upper bound |P(exp(i(theta0+t)))|<=C|t|^r and Bernoulli give a positive input-dependent lower bound times n^(-1/(2r)); P=(z-1)^r excludes a square-root bound over that repeated-root class.
The exact positive logarithmic series still holds for nonsquarefree P; removing its factor multiplicities is not an allowed normalization.

For the actual irreducible Salem P=z^4-4z³+3z²-4z+1, Q=x²-4x+1,H=13, the two circle roots have trace2-sqrt(3), derivative modulus2sqrt(3)sqrt(4sqrt(3)-3) and S=1/[sqrt(3)sqrt(4sqrt(3)-3)].
Its positive moments have precisely the preceding half-power coefficient even though its different Chebyshev moments cannot have absolute decay exponent above1/4.
That older phase degeneracy is at B(0)=9>0, not a zero controlling these positive Laplace tails.

The exponent is uniform across the squarefree class, while every derivative, local radius, original leading/off-circle factor and complementary geometric scale H²/b² remains input-dependent.
At N comparable to d, HS=o(sqrt(d)) with fixed eta and d b²/H² tending to infinity are only unproved sufficient conditions for this displayed remainder to vanish.
No useful uniform cutoff, dominance over every oscillatory certificate, executed finite moment/radius/root evaluation or unrestricted Mahler gap is established.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:48 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| support | [Exact local Taylor and factorization method](Yin_C_G0384_v1.md#local-circle-error-and-multiplicity) | Only the same fully paid simple-zero geometry and leading/all-off-circle method; the required proof is retained here for arbitrary leading coefficient and degree1 as well, rather than extending the separate monic degree>=2 optional discriminant estimate. |
| dependency | [Exact genuine Salem quartic comparison](Yin_C_G0402_v1.md#salem-quarter-exponent-actual-control) | Only the actual quartic irreducibility/root configuration and distinct Chebyshev quarter-exponent obstruction; the positive Gaussian derivative/asymptotic and changed-observable explanation are proved locally. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:55 |
| status | proved |
| reason | Adopt the actual complete self-review of this exact statement and full selected argument, including all factors and repeated-zero identity, arbitrary-leading simple-zero tails, all cost parameters and the distinct quartic comparison; no source proof, numerical execution or uniform cutoff is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| support | [Exact support](Yin_C_G0384_v1.md#local-circle-error-and-multiplicity) | Only the same fully paid simple-zero geometry and leading/all-off-circle method; the required proof is retained here for arbitrary leading coefficient and degree1 as well, rather than extending the separate monic degree>=2 optional discriminant estimate. |
| dependency | [Exact accepted input](Yin_C_G0402_v1.md#salem-quarter-exponent-actual-control) | Only the actual quartic irreducibility/root configuration and distinct Chebyshev quarter-exponent obstruction; the positive Gaussian derivative/asymptotic and changed-observable explanation are proved locally. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0636_v1.md#current-positive-log-whole-finding) | Complete current Statement and Argument, every retained equation and proof, all degenerate and multiplicity cases, exact quartic comparison, directions and paid limitations. |

## Complete retained argument

<a id="argument"></a>
<a id="complete-positive-integer-logarithmic-tail"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="positive-log-moment-identity"></a>
## 1. Complete positive expansion and exact integer moments

Remove a Laurent monomial from the nonzero integer input, preserving its circle modulus, measure and coefficient sum.
Let P have degree/span d, H=sum|a_j|>=1 and B(z)=P(z)P(z^-1) on the circle.
For n>=1 define
\[
\nu_n=\int_{\mathbb T}(1-B/H^2)^n\,d\mu,\qquad
Z(z)=H^2-P(z)P(z^{-1})\in\mathbb Z[z,z^{-1}].
\]
Because0<=B/H^2<=1,
\[
0\le\nu_{n+1}\le\nu_n\le1,\qquad
\nu_n=\frac{\operatorname{CT}Z^n}{H^{2n}}.                    \tag{1}
\]
The moments are exact rationals obtained from the original integer symbol; no independent phase or new probability law is substituted.
Their Laurent coefficients need not all be positive.

For0<x<=1, integration of the geometric series gives
\[
-\log x=\sum_{n\ge1}(1-x)^n/n.
\]
All summands are nonnegative.
The finitely many zeros of a nonzero polynomial on the circle have measure zero, and its logarithm is integrable.
Monotone convergence therefore proves directly
\[
m(P)=\log H-\frac12\sum_{n\ge1}\frac{\nu_n}{n}.                \tag{2}
\]
No regularizer or absolute oscillatory Fourier convergence is needed.
Define the finite partial expression
\[
T_N(P)=\log H-\frac12\sum_{n=1}^N\nu_n/n,\quad N\ge1.
\]
It is a decreasing UPPER bound for m(P).
A lower certificate will be obtained only by subtracting an independently proved upper bound on its positive remainder.

For a monomial P=a z^j, H=|a|, B=H^2 and every nu_n=0, giving m(P)=log|a| exactly.
The remaining sections concern nonmonomial P.
Integer moments can be computed by the recurrence Z^0=1,Z^(n+1)=Z Z^n, retaining support[-nd,nd].
Each Fourier coefficient has modulus at most integral Z^n<=H^(2n), so numerator/denominator bit sizes are O(n log(2H)).
The same direct convolution bound O(N^2d^2) arithmetic operations as the earlier coefficient-moment account applies.
No program is run here.

<a id="simple-circle-positive-moment-bound"></a>
## 2. Paid simple-zero neighborhoods and a positive complementary modulus

Assume P is squarefree.
Let C be its set of actual circle roots, with
\[
A_\zeta=|P'(\zeta)|>0,\qquad S(P)=\sum_{\zeta\in C}A_\zeta^{-1}.
\]
Fix0<eta<1.
Reuse [L361's complete local construction](../ledger/Yin_L_G0361_v1.md#local-circle-error-and-multiplicity): writing f(theta)=P(e^(i theta)), let
\[
K=\sum_{j=0}^d j^2|a_j|.
\]
Choose disjoint circle arcs of positive radii r_zeta<=pi with K r_zeta/2<=eta A_zeta.
All gaps and coefficient costs are actual input data.
Taylor's integral remainder gives
\[
|P(e^{i(\theta_\zeta+t)})|\ge(1-\eta)A_\zeta |t|
\quad (|t|<r_\zeta).                                        \tag{3}
\]
The complement has the explicit complete lower modulus
\[
b=|a_d|\prod_{\zeta\in C}2\sin(r_\zeta/2)
           \prod_{|\alpha|\ne1}||\alpha|-1|>0,               \tag{4}
\]
where every original off-circle root is included.
The leading factor is retained.
The complement is nonempty (possibly only endpoints), and the construction gives b<=H.
In the case C empty use the same full off-circle product, with the first product empty.

Put
\[
\rho=1-b^2/H^2\in[0,1),\qquad
C_P=\frac{H S(P)}{2\sqrt\pi(1-\eta)}.
\]
Then for every n>=1,
\[
\nu_n\le C_P n^{-1/2}+\rho^n.                                \tag{5}
\]
To prove this, on each root arc use1-x<=e^-x and(3), and enlarge its nonnegative integral to the real line:
\[
\frac1{2\pi}\int_{\text{arc}}(1-|P|^2/H^2)^n\,d\theta
\le \frac1{2\pi}\int_{\mathbb R}
 e^{-n(1-\eta)^2A_\zeta^2t^2/H^2}\,dt
=\frac{H}{2\sqrt\pi(1-\eta)A_\zeta\sqrt n}.
\]
The Gaussian integral is the elementary identity obtained by squaring the integral and using plane polar coordinates.
On the complement, the original integrand is at most rho^n and its Haar measure is at most1.
Summing proves(5).
If C is empty, S=0 and only the exponential term is present.

This argument uses the original simple zeros of P, not the zeros of a phase derivative.
High multiplicity of a nonzero critical value of |P| does not affect its exponent.
There is no assumption of real trace roots, of any circle root existing, or of a globally bounded inverse.

<a id="positive-unregularized-lower-certificate"></a>
## 3. A direct lower certificate with all tail costs

From(5) and elementary integral/geometric comparisons,
\[
0\le T_N(P)-m(P)
=\frac12\sum_{n>N}\nu_n/n
\le \frac{C_P}{\sqrt N}
+\frac{\rho^{N+1}}{2(N+1)(1-\rho)}
=:R_N^+(P).                                                  \tag{6}
\]
Indeed sum_(n>N)n^-3/2<=2/sqrtN and sum_(n>N)rho^n/n<=rho^(N+1)/[(N+1)(1-rho)].
At rho=0 the second term is0.
Thus
\[
T_N(P)-R_N^+(P)\le m(P)\le T_N(P).                           \tag{7}
\]
Every finite moment is exact integer coefficient data; the logarithm of H and the positive geometric/derivative constants may be enclosed rigorously when an actual certificate is computed.

In characteristic zero, an irreducible nonconstant integer polynomial is squarefree.
Therefore(6)--(7) cover every irreducible hard-core input, including those with nonreal trace roots or with no circle conjugates.
The generic positive moment exponent is one-half at simple circle zeros, in contrast to the critical-point-dependent exponent for the DIFFERENT Chebyshev moment sequence.
There is no contradiction with the quarter-exponent Salem example or L368's broad high-degeneracy obstruction.

The constants are fully input dependent.
Close circle roots or off-circle roots near the circle can force small radii or tiny b; H and S(P) may grow.
L361's full polynomial-discriminant bound is available for S but keeps its degree/height cost.
In particular the complementary geometric scale may be as large as H^2/b^2.
No useful uniform cutoff or gap follows just from squarefreeness.
At windows N comparable to d, the sufficient conditions H S(P)=o(sqrt d) (with eta fixed) and d b^2/H^2 tending to infinity would make this displayed remainder vanish; neither is proved here.

The exact logarithmic series(2) also holds for nonsquarefree P, but the half-power bound(5) need not.
One may factor an input into irreducibles and retain every factor multiplicity in total Mahler measure; silently replacing P by its squarefree part is not a valid normalization.

<a id="positive-moment-sharp-local-coefficient"></a>
## 4. Exact fixed-input leading term and the repeated-root boundary

For every fixed squarefree P,
\[
\lim_{n\to\infty}\sqrt n\,\nu_n
=\frac{H S(P)}{2\sqrt\pi}.                                  \tag{8}
\]
On each fixed simple-zero arc substitute t=u/sqrt n.
The Taylor expansion gives n|P(e^(i(theta_zeta+u/sqrt n)))|^2/H^2 tending to A_zeta^2u^2/H^2.
Hence the integrand tends to the corresponding Gaussian.
The lower bound(3) supplies an integrable Gaussian dominator after extension by0 outside the expanding rescaled interval.
Dominated convergence gives each coefficient H/(2sqrtpi A_zeta).
The complementary contribution is at most sqrt n rho^n and vanishes.
With no circle roots both sides are0.
This is a fixed-input limit with fixed radii, not an input-uniform assertion.

For a root of multiplicity r>=2, a local upper estimate |P(e^(i(theta0+t)))|<=C|t|^r holds for small t.
On an interval of radius [H/(sqrt(2n)C)]^(1/r), for sufficiently large n, B/H^2<=1/(2n), and Bernoulli's inequality gives(1-1/(2n))^n>=1/2.
Thus nu_n is bounded below by a positive input-dependent multiple of n^-1/(2r).
In particular P=(z-1)^r rules out a universal square-root bound on the repeated-root class.
This restriction is exactly why irreducibility/squarefreeness matters in the current integer application.

For the already accepted genuine Salem quartic P=z^4-4z^3+3z^2-4z+1, Q=x^2-4x+1 and H=13, the two circle roots lie over x=2-sqrt3.
Their common derivative modulus is 2sqrt3 sqrt(4sqrt3-3), so
\[
S(P)=\frac1{\sqrt3\sqrt{4\sqrt3-3}}.                          \tag{9}
\]
Consequently its positive moments have the exact square-root leading coefficient(8), while its Chebyshev moments cannot satisfy an absolute decay exponent above one-quarter.
The old phase degeneracy occurs at a positive value B(0)=9; that point does not create a slow Laplace tail near B=0.
This exact symbolic comparison changes the observable and accounts for the different exponent; no finite moment or radius computation was executed.

### Complete complementary-factor justification

For any point outside the chosen open arcs, its circular distance from each circle root is at least that root's r_zeta and at most pi after choosing the shorter distance.
Its chord distance is therefore at least2sin(r_zeta/2).
Every off-circle factor has distance at least||alpha|-1| by the reverse triangle inequality.
Multiplying the full original factorization with |a_d| gives the exact displayed b for arbitrary leading coefficient and degree1 as well.
At a complementary point b<=|P|<=H, so the declared rho interval is justified without a monic degree-at-least2 discriminant theorem.
