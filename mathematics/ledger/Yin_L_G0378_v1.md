---
author: Yin
---

# Positive integer log moments and squarefree circle-zero tails

Date:2026-10-11T14:34.
Root coordinating AI for Yin fixes the complete restricted author account below under the continuing G0001 weekly authorization, after separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0202_v1.md#positive-log-whole-finding).
Adopt exactly its stated hypotheses, original costs, failures and source/review limits.
No unrestricted Mahler gap, canonical Claim or Task completion is asserted.

<a id="coupled-method-fixed-scope"></a>
## Fixed scope and preservation

The entire author account follows, with only title depth, navigation and final blank-line normalization.
Allocation-era pending-review statements remain history; the linked fixed R supplies the actual completed review scope.
Proposed or unrun computations remain unrun.
No new allowance, input-uniform conditioning or actual unit/covariance realization is inferred.
Further mathematics uses a distinct draft.

The current complete positive-log identity and paid simple-zero tail theorem is retained in [C434](../claims/Yin_C_G0434_v1.md#complete-positive-integer-logarithmic-tail), adopted after the actual [whole self-review R636](../audits/reviews/Yin_R_G0636_v1.md#current-positive-log-whole-finding).
The original author account, all factors and repeated-zero identity, source limits and original review remain below.
The author date has only day precision; the retention time22:34 and R202 review22:26 do not establish an author freeze or reading minute.

## Complete retained account


## Positive integer log moments and squarefree circle-zero tails

Date:2026-10-11.
Root AI for Yin under the continuing G0001 weekly authorization.
This is a changed single-Haar candidate using a positive logarithmic power series, separate from the oscillatory Chebyshev phase.

## Exact question and scope

For an actual nonzero squarefree integer polynomial P, with B=|P|^2 and H=sum|a_j|, use nu_k=integral(1-B/H^2)^k.
The formal log expansion has nonnegative tail terms.
Test whether local SIMPLE circle zeros, together with a paid positive lower modulus on their complement, give an explicit k^-1/2 plus exponential moment bound and a direct unregularized lower certificate.
Irreducibility in characteristic zero supplies squarefreeness, without requiring real trace roots or any circle conjugate to exist.
Repeated-root and monomial branches must retain their own exact scopes.

The local reuse screen searches the G ledgers for unregularized Taylor/log-power and Laplace-tail accounts.
[L358](Yin_L_G0358_v1.md) already discusses regularized Taylor versus Chebyshev costs; [L361](Yin_L_G0361_v1.md#local-circle-error-and-multiplicity) supplies complete coefficient-paid simple-zero arcs and a complementary lower modulus.
Reuse those exact local estimates rather than attribute a generic zero-separation theorem.
The question is a new coupling of the positive exact integer moments with that retained squarefree geometry, not a claim of historical novelty for a logarithmic series or Gaussian estimate.
No program, J or scan is declared.

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
Reuse [L361's complete local construction](Yin_L_G0361_v1.md#local-circle-error-and-multiplicity): writing f(theta)=P(e^(i theta)), let
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

## 5. Outcome and author freeze

The positive coefficient moments give a second direct unregularized integer lower certificate, with a uniform half exponent across squarefree inputs and a separately paid complementary geometric term.
Its substantive gain is the removal of internal phase-critical multiplicity from the tail mechanism.
Its unresolved costs are actual circle derivatives, local radii, coefficient scale and off-circle distance.
Neither this result nor the earlier oscillatory result is asserted to dominate the other on every input.

The series proof is elementary monotone convergence, and all root geometry reuses the complete L361 simple-zero construction.
The new proof retains original integer moments, full leading/factor costs, the monomial/no-circle/repeated-root branches, normalized Gaussian factors, finite lower direction and all fixed-input versus uniform limits.
Historical novelty is not claimed.
Author self-check is complete for Sections1--5 and equations(1)--(9); the whole account is frozen for separate noncontributor review.
No mathematical program, new J, numerical quadrature, root isolation, moment evaluation or unrestricted gap is asserted.
