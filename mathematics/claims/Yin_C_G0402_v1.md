---
author: Yin
---

# Genuine Salem phase orders, paid quarter/half decay and sharp quartic control

This retains the complete necessary mathematical argument from [complete original L369 proof](../ledger/Yin_L_G0369_v1.md#salem-interlacing-critical-orders).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For every irreducible minimal polynomial P(z)=z^s Q(z+z^-1) of a genuine Salem number beta>1, retain its full degree d=2s>=4 and all original trace roots: x_0=beta+beta^-1>2 and s-1 distinct roots in(-2,2).
Put H=sum|a_j|, phi(theta)=arccos(2Q(2cos theta)^2/H^2-1) and mu_k=integral_T cos(k phi) with normalized Haar measure.
Every zero of the exactly canceled squared phase derivative has one-sided derivative order M_i<=3; if Q'(2)!=0 every such order is at most1.
Interior root cusps, endpoint-value cusps and both angular endpoints have exactly the cases proved below; no smooth crossing of a cusp is assumed.
For every integer k>=1 the complete paid constant K_P of the general phase theorem gives |mu_k|<=K_P k^(-1/4), with tail sum_(k>N)|mu_k|/k<=4K_P N^(-1/4) for every integer N>=1.
If Q'(2)!=0 the corresponding bounds are K_P k^(-1/2) and 2K_P N^(-1/2).
Consequently the exact unregularized logarithmic moment identity gives the stated finite lower certificate with that negative tail error; the actual rational moments and every coefficient/root cost remain charged.
An alternative complete constant uses the integral degree-d polynomial F(z)=(z^2-1)z^(s-1)Q'(z+z^-1), leading coefficient s.
Its distinct circle roots eta_i include +/-1; their multiplicities m_i are1 or3, +1 being triple exactly when Q'(2)=0.
All remaining roots, if any, are one positive reciprocal pair.
Define gamma_i and c_P=(2/H)min_i gamma_i by the full products in(8), including all leading, separation and off-circle radial factors, L the number of distinct circle roots, m_*=max_i m_i and J=16d+2.
Then for all k>=1, |mu_k|<=K_P^tr k^(-1/(m_*+1)), where K_P^tr=L/pi+2J*pi^(m_*-1)/(2^(m_*) c_P); the full logarithmic tail is at most(m_*+1)K_P^tr N^(-1/(m_*+1)).
These are input-dependent paid constants, and no comparison claiming one is always smaller is made.
The explicit P=z^4-4z^3+3z^2-4z+1 is irreducible and genuinely Salem, with Q=x^2-4x+1, H=13 and a nonzero fourth-order phase change at theta=0.
For this fixed input no bound |mu_k|<=C k^-b for all k>=1 exists for any b>1/4 and any finite input-dependent C.
Thus the class-wide quarter exponent for absolute moments is sharp.
The original Lehmer trace has Q'(2)=36 and satisfies the half-exponent gate.
No root data, finite certificate value or uniform useful conditioning constant has been computed; the sharpness control has fixed positive measure and supplies neither a near-one family nor an unrestricted Mahler gap.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:38 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact original reciprocal trace domain](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the full original monic reciprocal trace representation and degree normalization, with the genuine Salem hypotheses verified locally. |
| dependency | [Complete paid oscillatory theorem](Yin_C_G0398_v1.md#paid-oscillatory-moment-decay) | Complete canceled phase, explicit integration-by-parts and both critical-set branches, full constants and unregularized moment/positive-Fejer interfaces at the same original input. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T17:43 |
| status | proved |
| reason | Adopt the actual complete whole SELF finding after checking every exact current statement domain, complete retained proof, necessary accepted input and all source/realization/conditioning/cost limitations. Original author and whole-review scopes, dates and actual SELF relationships remain separate; no new source/native run or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the full original monic reciprocal trace representation and degree normalization, with the genuine Salem hypotheses verified locally. |
| dependency | [Exact accepted input](Yin_C_G0398_v1.md#paid-oscillatory-moment-decay) | Complete canceled phase, explicit integration-by-parts and both critical-set branches, full constants and unregularized moment/positive-Fejer interfaces at the same original input. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0606_v1.md#current-salem-phase-whole-finding) | Entire exact Statement and complete necessary retained argument with all source, finite-symbol/actual-unit, endpoint, arithmetic, conditioning and original-cost limits. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="salem-interlacing-critical-orders"></a>
## 1. Complete actual Salem domain and phase-critical orders

Let P be the irreducible minimal polynomial of a genuine Salem number beta>1, of degree d=2s>=4.
Write
\[
P(z)=z^s Q(z+z^{-1}).
\]
The monic integer trace polynomial Q has distinct real roots x_0=beta+beta^-1>2 and x_1,...,x_(s-1) in(-2,2).
Neither endpoint is a root.
These are the original complete trace roots; no factor or proper field replaces P.
Let H=sum|a_j|, x(theta)=2cos theta and
\[
\phi(\theta)=\arccos(2Q(x(\theta))^2/H^2-1).
\]
This is precisely D14's original phase, since |P(e^(i theta))|^2=Q(2cos theta)^2.

Rolle's theorem gives one root of Q' in each gap between consecutive Q roots.
Their number s-1 exhausts deg Q', so all are real and simple and none is a root of Q.
In particular every root of Q' lies strictly above -2.
At most one can lie at or above2; it must be in the gap between the largest circle trace root and x_0.

Away from Q(x)=0 and Q(x)^2=H^2, differentiation gives
\[
|\phi'|=\frac{2|Q'(x)x'|}{\sqrt{H^2-Q(x)^2}}.                  \tag{1}
\]
The exact gcd-canceled squared derivative of D14 extends continuously across its endpoint-value points.
Its circle zero multiplicity is twice the vanishing order M_i of the one-sided derivative.
All possibilities are as follows.

- At an interior angle with Q(x)=0, Q' and x' are nonzero.
  B=Q(x)^2 has a simple-square zero of order2; the phase has a linear cusp.
  D14's cancellation leaves a nonzero limiting derivative, so M_i=0.
- At an interior angle with Q'(x)=0, Q is nonzero and Q' is simple.
  If B<H^2, the phase has a nonzero quadratic leading change and M_i=1.
  If B=H^2, H^2-B has order2 and its square-root phase has a linear cusp; cancellation leaves M_i=0.
- At theta=pi, x=-2 and x+2 has order2.
  Both Q(-2) and Q'(-2) are nonzero.
  If B<H^2, the phase has a quadratic leading change, so M_i=1; if B=H^2 it has a linear cusp and M_i=0.
- At theta=0, x=2 and x-2 has order2.
  Q(2)!=0.
  If Q'(2)!=0, the same orders1 or0 occur.
  If Q'(2)=0, simplicity of this root of Q' gives Q''(2)!=0.
  Thus B-B(0) has exact order4.
  For B(0)<H^2 the derivative order is3; for B(0)=H^2 the phase has leading order2 and derivative order1.

All other points have nonzero derivative.
For the interior B=H^2 case, simplicity makes the second-order term nonzero; the global B<=H^2 forces its maximum sign.
At angular endpoints the expansions are one-sided on either adjacent arc, which suffices for the canceled squared derivative.
No smooth passage through a cusp is assumed.

Consequently every actual canceled phase multiplicity satisfies
\[
M_i\le3,\qquad
Q'(2)\ne0\ \Longrightarrow\ M_i\le1.                         \tag{2}
\]
The all-real trace hypothesis is essential to this conclusion.
Squarefreeness of an arbitrary reciprocal polynomial alone does not make Q' simple.

<a id="salem-uniform-exponent-certificate"></a>
## 2. Uniform exponents, with input-dependent constants retained

Apply D14's complete paid oscillatory theorem at this exact original input.
When its critical set is nonempty, it supplies |mu_k|<=K_P k^(-1/(M+1)) with all actual canceled root and coefficient costs.
When the set is empty, it supplies |mu_k|<=K_P/k.
From(2), for every genuine Salem input there is an explicitly paid finite K_P>0 such that
\[
|\mu_k|\le K_P k^{-1/4}\quad(k\ge1),\qquad
\sum_{k>N}\frac{|\mu_k|}{k}\le4K_P N^{-1/4}.                  \tag{3}
\]
If Q'(2)!=0, the stronger bounds are
\[
|\mu_k|\le K_P k^{-1/2},\qquad
\sum_{k>N}\frac{|\mu_k|}{k}\le2K_P N^{-1/2}.                  \tag{4}
\]
These reuse the actual K_P defined in D14; weakening the exponent for k>=1 leaves that same constant valid, including its no-critical-root branch.
Finite N>=1 is an integer.

The direct exact moment formula therefore has the finite lower certificate
\[
m(P)\ge\log(H/2)+
 \sum_{k=1}^{N}(-1)^{k+1}\frac{\mu_k}{k}-4K_P N^{-1/4},       \tag{5}
\]
with2K_P N^-1/2 replacing the last term under Q'(2)!=0.
Every mu_k is the actual integer-coefficient rational moment, and no regularizer is needed.
The exponent is uniform on this named class; K_P is **not** proved uniformly bounded, polynomial in degree, or useful at a degree-linear window.
Thus this conclusion does not contradict D14's broad-class obstruction and does not establish a Lehmer gap.

For the retained original Lehmer trace polynomial
\[
Q=x^5+x^4-5x^3-5x^2+4x+3,
\]
the exact evaluation Q'(2)=80+32-60-20+4=36 is nonzero.
Its actual moment sequence therefore falls under(4), with its own still-paid constants.
This is a direct arithmetic substitution into the theorem, not a critical-root numerical calculation or an executed lower certificate.

<a id="smaller-salem-critical-polynomial"></a>
## 3. A smaller integer critical polynomial pays the derivative bound directly

Define
\[
F(z)=(z^2-1)z^{s-1}Q'(z+z^{-1})\in\mathbb Z[z].             \tag{6}
\]
Its degree is d=2s and its leading coefficient is s.
Its circle modulus is2|sin theta| |Q'(2cos theta)|.
Equation(1), with denominator at most H, yields
\[
|\phi'|\ge\frac2H|F(e^{i\theta})|                            \tag{7}
\]
on every smooth phase piece.
Endpoint-value limits are handled by excluding the finitely many cusps, as in D14.

All roots of F are now described by real interlacing.
The endpoint -1 is simple.
The endpoint+1 is simple unless Q'(2)=0, when it has multiplicity3.
A Q' root in(-2,2) gives a distinct simple inverse pair on the circle.
At most one root of Q' is above2 and it gives the only possible off-circle pair, real positive and reciprocal.
No Q' root lies below-2 or is nonreal.

Let eta_1,...,eta_L be the distinct circle roots of F and m_i their actual multiplicities.
Here L>=2 and m_i in{1,3}.
Put m_*=max m_i and
\[
\gamma_i=s
 \prod_{j\ne i}(|\eta_i-\eta_j|/2)^{m_j}
 \prod_{\xi:F(\xi)=0,\ |\xi|\ne1}||\xi|-1|^{\operatorname{mult}(\xi)},
\qquad
c_P=\frac2H\min_i\gamma_i>0.                                 \tag{8}
\]
Every root, leading factor and multiplicity occurs.
No root data is claimed computed.
At a nearest circle root eta_i, full factorization and the triangle inequality give |F(z)|>=gamma_i |z-eta_i|^(m_i).
Outside angular arcs of radius0<r<=1 around all eta_i, (7) thus gives
\[
|\phi'|\ge c_P(2r/\pi)^{m_*}.                                \tag{9}
\]

Reuse D14's conservative monotonicity partition count J=16d+2; adding the at-most2L arc boundaries is within the same count, since L<=d<=2d and all these roots are among genuine critical points or the two original endpoints.
If an endpoint has no canceled derivative zero, retaining it as an extra bad arc only weakens the estimate; D14 already counts both endpoint/cusp cuts.
The full rational-derivative zero count and cusp count remain unchanged.
Equivalently the direct bound of8d-1 rational zeros, at most2d cusp points, at most2d F-arc boundaries and an angular cut is below J.

The same explicit4 integration-by-parts argument then proves
\[
|\mu_k|\le K_P^{\mathrm{tr}} k^{-1/(m_*+1)},\qquad
K_P^{\mathrm{tr}}=\frac L\pi+
 \frac{2J\pi^{m_*-1}}{2^{m_*}c_P}.                            \tag{10}
\]
The complete omitted log tail is at most(m_*+1)K_P^tr N^-1/(m_*+1).
This is an alternative paid constant using a degree-d integer polynomial instead of a general canceled rational representation.
It does not claim to be smaller on every input; the minimum of two actually certified bounds may be used.
If the off-circle Q' pair approaches1 or circle critical roots cluster, (8) records the full resulting cost.

<a id="salem-quarter-exponent-actual-control"></a>
## 4. The quarter exponent is necessary on an actual Salem control

Take
\[
Q(x)=x^2-4x+1,\qquad
P(z)=z^4-4z^3+3z^2-4z+1.                                    \tag{11}
\]
Q is irreducible over Q, with distinct trace roots2+sqrt3>2 and2-sqrt3 in(0,1).
At the latter real embedding x^2-4<0, so x^2-4 is not a square in the quadratic trace field.
Adjoining a root of z^2-xz+1 has degree2 over that field, and x=z+z^-1 lies in Q(z).
Hence P is its irreducible degree-four minimal polynomial.
It has one positive real expanding reciprocal pair and one nonreal circle pair, so it is an actual genuine Salem minimal polynomial.
No original-degree or leading-factor cost is removed.

Here Q'(2)=0, Q(2)=-3, H=13 and B(0)=9<169=H^2.
Writing x=2cos theta gives
\[
Q(x)=-3+(x-2)^2,\qquad
B(\theta)=9-6\theta^4+O(\theta^6).
\]
Since the arccos argument at0 lies strictly inside(-1,1), the phase has an exact nonzero fourth-order change.
The symmetrized phase law consequently has mass at least a positive input-dependent constant times L^-1/4 in an interval of radius1/L about phi(0).

D14's positive Fejer argument applies unchanged to this actual local expansion: a hypothetical |mu_k|<=C k^-b with b>1/4 would bound that mass by O(L^-b), a contradiction (weaken b>=1 to an exponent in(1/4,1) first).
Thus the absolute-moment exponent1/2 cannot hold for all genuine Salem minimal inputs, even with an arbitrary input-dependent constant.
The universal quarter exponent in(3) is sharp for this type of absolute coefficient estimate.

This control has fixed positive total measure and is not a near-one family.
It does not exclude the half exponent on Q'(2)!=0 inputs, or a theorem ruling out this exact endpoint degeneracy under an additional justified near-one hypothesis.
No phase asymptotic or finite moment scan was used.
