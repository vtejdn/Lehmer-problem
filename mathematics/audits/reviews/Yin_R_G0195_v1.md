---
author: Yin
---

# Genuine Salem trace interlacing, explicit oscillatory constants and quarter sharpness: independent whole-proof review

Date and human attribution: 2026-10-11T12:20.
Record author Yin; mathematical inspection by the separately assigned salem_review AI reviewer.
No personal human proof inspection or formal verification is asserted.

## Arrangement, inputs and exact scope

This is an initial whole-proof review of [D_G0015](../../ledger/Yin_L_G0369_v1.md), the root-authored account dated2026-10-11 and frozen in its Section5, complete Sections1--5 and equations(1)--(11).
The reviewer made no contribution to its derivation.
The assignment supplied the topic, intended conclusions and an obligation outline: genuine Salem trace interlacing, all canceled phase orders, quarter/half exponents, a smaller critical polynomial with constants and an irreducible sharpness control.
It supplied no proof-generation dialogue or additional author derivation.
The proof itself and its author self-check were read; neither the outline nor the self-check was treated as evidence.

The reviewer first reconstructed the Salem specialization and its necessary general-theorem interfaces directly from D_G0015 and [L368](../../ledger/Yin_L_G0368_v1.md), and formed the initial mathematical conclusions before reading the upstream whole review [R193](Yin_R_G0193_v1.md#whole-oscillatory-certificate-finding).
R193 was then checked for the exact scope and limits of the accepted general theorem and its sources.
No earlier independent finding on D15 was supplied or consulted.
A lightweight older G0001 status-memory lookup supplied no proof reasoning.

The actual other mathematical input read was [L66](../../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain), at its unchanged reciprocal trace representation and field-degree scope, including its exact retained Lehmer trace expression.
The whole general theorem in L368 is accepted at R193's stated scope.
Its phase cancellation, derivative estimate, Haar constants, uniform tail and positive-Fejer mechanism used here were also checked directly.
L358's original regularized-source argument and the original Tao/DLMF/Szego/Smyth sources were not newly re-audited: their applicable established interfaces remain covered by the exact upstream review, rather than a new source-proof claim here.
No new external theorem is used in the Salem specialization; its Rolle and quadratic-field arguments are supplied locally.

The review covers the complete frozen symbolic argument, applicability of the retained inputs, all constants and limiting/estimate directions.
It does not evaluate critical roots, finite moments or a numerical lower certificate.
There is no declared program, computation, J or scan.
This is not a completion audit of [G0001](../../tasks/Yin_T_G0001_v1.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [D15 complete frozen argument](../../ledger/Yin_L_G0369_v1.md) | Entire dated2026-10-11 author freeze, Sections1--5 and equations(1)--(11), including ownership, conclusions and all no-computation/nonuniformity limits. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [D15 Salem domain and orders](../../ledger/Yin_L_G0369_v1.md#salem-interlacing-critical-orders) | Full original degree-d irreducible Salem domain, real simple trace roots, exhausted Rolle count, ordinary/cusp/angular-endpoint cases and exact bounds M<=3 and M<=1 under Q'(2)!=0. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [D15 exponent and lower certificate](../../ledger/Yin_L_G0369_v1.md#salem-uniform-exponent-certificate) | Application of the same paid L368 constants in both critical-set branches; quarter/half decay, integer-N tails, unregularized finite lower direction, exact Lehmer substitution and input-dependent conditioning. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [D15 integer critical polynomial](../../ledger/Yin_L_G0369_v1.md#smaller-salem-critical-polynomial) | Complete Section3 and equations(6)--(10): integrality/degree/leading coefficient, every circle/off-circle root and multiplicity, all factorization costs, arc and monotonicity counts, explicit normalized constant and tail. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [D15 actual quarter-sharp control](../../ledger/Yin_L_G0369_v1.md#salem-quarter-exponent-actual-control) | Complete Section4 and equation(11): trace and quartic irreducibility, genuine Salem configuration, exact coefficient scale and fourth-order phase change, positive-Fejer obstruction for every b>1/4, fixed-measure and near-one limits. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L66 original trace domain](../../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Only the original monic integer reciprocal trace representation and quadratic field-degree normalization; the new total-real/interlacing conclusion is checked in D15, not inferred for the broad L66 domain. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L66 Lehmer trace polynomial](../../ledger/Yin_L_G0066_v1.md#reciprocal-trace-lehmer-control) | Exact displayed original degree-five trace expression used for the arithmetic derivative substitution; no reuse or rerun of its old numerical programs is claimed. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L368 exact phase cancellation](../../ledger/Yin_L_G0368_v1.md#exact-phase-critical-cancellation) | Actual continuous gcd-canceled squared derivative, numerator order2M_i, denominator with no circle roots, all endpoint cancellations and rational monotonicity partition used by D15. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L368 paid oscillatory theorem](../../ledger/Yin_L_G0368_v1.md#paid-oscillatory-moment-decay) | Same original symbol/degree/Haar scale, explicit integration-by-parts constant4, K_P and both nonempty/empty critical-set branches; new Salem hypotheses verified here. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L368 unregularized certificate](../../ledger/Yin_L_G0368_v1.md#unregularized-integer-moment-certificate) | Accepted exact log-moment identity, rational finite moments and uniform regularizer tail at R193's reviewed scope; specialization and finite lower direction rechecked here. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [L368 positive-Fejer mechanism](../../ledger/Yin_L_G0368_v1.md#oscillatory-degeneracy-integer-obstruction) | Symmetrized phase law, exact finite positive kernel, Fourier coefficients, concentration estimate and all exponent ranges; only its mechanism is applied to the newly proved Salem quartic. |
| [Whole Salem-specialization finding](#whole-salem-specialization-finding) | [R193 upstream whole-proof input](Yin_R_G0193_v1.md#whole-oscillatory-certificate-finding) | Accepted fixed general theorem and exact source/verification limits; no implication that R193 itself reviewed the new Salem specialization. |

## 1. Original Salem degree and all critical orders

For a genuine Salem minimal polynomial, characteristic zero makes every original root simple.
The inverse pairs consist of one positive real pair beta,beta^-1 and s-1 nonreal circle pairs.
Distinct inverse pairs have distinct traces: a trace determines the quadratic z^2-xz+1 and hence its inverse pair.
Thus the monic integer trace polynomial has the stated one root above2 and s-1 distinct roots strictly between-2 and2.
Neither endpoint is a trace root.
L66's integral reciprocal representation retains the original degree2s; no proper factor or entropy normalization is substituted.

Ordering the s real trace roots, Rolle supplies s-1 distinct derivative roots in their s-1 gaps.
Since deg Q'=s-1, every derivative root is simple, real and strictly between consecutive trace roots; Q and Q' have no common root.
All derivative roots lie above-2.
Only the last gap can reach2, so at most one derivative root lies at or above2.
This includes the exact equality Q'(2)=0 and gives Q''(2)!=0 there.

Differentiating arccos(2Q(x)^2/H^2-1) on0<Q(x)^2<H^2 cancels the absolute Q factor and gives exactly2|Q'(x)x'|/sqrt(H^2-Q(x)^2).
At an interior trace zero, Q' and x' are nonzero, B has order2, and the phase has a linear cusp with nonzero one-sided slope.
At an interior derivative zero with B<H^2, simple Q' gives a nonzero quadratic phase change and M=1.
If B=H^2, the exact order2 maximum becomes a linear phase cusp and M=0.
These conclusions agree with L368's full gcd cancellation; a cusp is not treated as a smooth stationary point.

At pi, x+2 has exact order2 and Q(-2)Q'(-2)!=0.
Thus the ordinary phase order is2 with M=1; an endpoint-value maximum has phase order1 with M=0.
At0, x-2 has exact order2 and Q(2)!=0.
If Q'(2)!=0 the same two cases apply.
If Q'(2)=0, Q''(2)!=0 makes B-B(0) have exact order4 because Q(2) is nonzero.
An interior phase value then has order4 and M=3; at B(0)=H^2 the square-root endpoint-value behavior has order2 and M=1.
The maximum sign is forced by the global bound B<=H^2 whenever that endpoint-value case occurs.
The angular expansions are one-sided on adjacent smooth arcs, as required; no smooth extension across a cusp is used.
There are no other derivative zeros.
Consequently the complete bounds in(2) hold.

## 2. Same-input constants, tails and exact lower direction

The actual Salem P is a nonmonomial real integer polynomial with nonzero endpoint coefficients, so it satisfies L368's complete input hypotheses without dropping original degree or leading costs.
When its canceled critical set is nonempty, its actual exponent a=1/(M+1) is at least1/4 and at least1/2 under Q'(2)!=0.
When that set is empty, the separately defined exponent is1.
Since k>=1, weakening any of these exponents preserves the same actual paid K_P.
This validates(3)--(4) in every branch, without replacing K_P by an unproved uniform value.

Integral comparison gives sum_(k>N)k^(-5/4)<=4N^(-1/4) and sum_(k>N)k^(-3/2)<=2N^(-1/2), with N>=1 integer.
Applying these absolute tails to the exact same unregularized identity in L368 gives(5) with a negative error term, in the correct lower direction.
The rational finite moments and regularizer removal are the accepted upstream interfaces; no endpoint pointwise log-series limit is newly presumed.
Direct differentiation of the retained Lehmer trace expression gives Q'(2)=80+32-60-20+4=36, so its declared half-exponent substitution is exact and requires no root computation.

The exponent is uniform over the stated Salem class.
The algebraic coefficient/radial/separation quantities within K_P remain those of each original input.
No degree-linear useful window, degree-uniform constant, near-one estimate or Mahler gap follows.

## 3. Smaller polynomial, every cost and explicit normalized constant

The polynomial z^(s-1)Q'(z+z^-1) is integral with degree2s-2, leading coefficient s and nonzero constant s.
Multiplication by z^2-1 gives F of exact degree2s=d and leading coefficient s, with no additional zero root.
On the circle, its modulus is2|sin theta||Q'(2cos theta)|=|x'Q'(x)|.
Since sqrt(H^2-Q^2)<=H, equation(7) follows with exactly the factor2/H.

Each simple trace derivative root y contributes the roots of z^2-yz+1.
For y in(-2,2) these are a distinct simple inverse circle pair.
The root y=2, if present, contributes(z-1)^2; combined with z^2-1 this makes+1 triple.
There is no y=-2, so-1 is simple, and+1 is simple otherwise.
The possible sole y>2 gives a positive real reciprocal off-circle pair, with both members retained.
All s-1 derivative roots were exhausted by Rolle, so no other roots or nonreal off-circle roots are omitted.
Hence L>=2, L<=d and all actual circle multiplicities are1 or3, as asserted.

For z on the circle and a nearest circle root eta_i, triangle inequality gives |z-eta_j|>=|eta_i-eta_j|/2 for j!=i.
Every off-circle root xi contributes at least||xi|-1|, with its multiplicity.
Full factorization, including lead(F)=s, therefore gives exactly gamma_i|z-eta_i|^(m_i).
Every displayed factor is positive for this fixed input, so c_P>0.
Outside the union of radius-r circular arcs,0<r<=1, the chord distance is at least2r/pi.
Since this base is at most1, replacing m_i by m_* weakens the lower estimate safely and proves(9).
Overlapping arcs need not be disjoint.

The same canceled rational g from L368 has at most8d-1 monotonicity zeros if its derivative numerator is nonzero; if that numerator is identically zero, g is a positive constant and no such zeros are inserted.
There are at most2d cusps, at most2L<=2d arc boundaries and one angular cut.
These give fewer than16d+2 open pieces.
Every F root is removed in a bad arc, including the extra endpoint arcs when an endpoint is a cusp rather than a canceled derivative zero.
On each retained piece phi is smooth and phi' has fixed nonzero sign; monotonicity of g=(phi')^2 makes phi' monotone.
This establishes the required partition without assuming the smaller polynomial's derivative itself controls monotonicity.

The omitted arcs have Haar mass at most Lr/pi.
Integration by parts on each complementary piece gives4/(k lambda), with lambda=c_P(2r/pi)^(m_*); exhaustion by closed subintervals is valid because the integrand has modulus1.
Dividing by2pi yields

    |mu_k|<=Lr/pi+2J pi^(m_*-1)/(2^(m_*) c_P k r^(m_*)).

Taking r=k^(-1/(m_*+1)) proves exactly(10), including every factor2 and pi and the stated K_P^tr.
The same integral comparison gives the complete tail(m_*+1)K_P^tr N^(-1/(m_*+1)).
The alternative certificate can be weaker at an individual cusp because its extra F roots are retained; no claim that it always improves K_P is made.
Taking the minimum of certified bounds is valid.
Clustering circle roots or an off-circle pair approaching1 makes the actual products small and remains fully paid.

## 4. Actual irreducible Salem quartic and absolute-decay sharpness

The trace polynomial x^2-4x+1 has discriminant12, so is irreducible over Q with roots2+sqrt3 and2-sqrt3.
Its trace field is real quadratic.
For x=2+sqrt3, the conjugate of x^2-4 at the other real embedding is(2-sqrt3)^2-4<0.
A square in a real number field is nonnegative under every real embedding, so x^2-4 is not a square in this field.
Thus z^2-xz+1 is irreducible over it.
Conversely x=z+z^-1 belongs to the field generated by a root z, proving that this root has degree4 over Q.
Multiplying the trace identity gives exactly z^4-4z^3+3z^2-4z+1; it is therefore the irreducible minimal polynomial.
The large trace produces one positive expanding reciprocal pair and the small trace lies in(0,1), producing a nonreal circle pair.
The example is a genuine Salem input of the original degree.

Its coefficient norm is H=13 and Q(2)=-3.
Since x=2cos theta=2-theta^2+O(theta^4), Q(x)=-3+(x-2)^2 gives B=9-6theta^4+O(theta^6).
The phase center has arccos argument-151/169 strictly inside(-1,1), and the derivative of arccos with respect to B is nonzero there.
Thus the phase has exact order4; for example the resulting leading coefficient is1/(2sqrt10), nonzero.
A radius proportional to L^(-1/4) theta interval maps into the phase interval of radius1/L.
Haar normalization and phase-law symmetrization cost only fixed positive constants, so that phase interval has mass at least c L^(-1/4) for all sufficiently large integer L.

For the symmetrized phase law nu, the kth Fourier coefficient is exactly mu_k.
The finite nonnegative Fejer polynomial has the exact expansion1+2sum_(k=1)^(L-1)(1-k/L)cos(kt), and is at least4L/pi^2 on |t|<=1/L.
Integrating its translate about the phase center bounds the local mass above by pi^2/(4L) times1+2sum(1-k/L)mu_k cos(k phi(0)).
If |mu_k|<=C k^-b with1/4<b<1, integral comparison bounds this by O_C(L^-b), contradicting the actual mass lower bound.
Any b>=1 can first be weakened to one strictly between1/4 and1.
Kernel positivity makes cancellation among different stationary contributions irrelevant.
This proves the stated obstruction for every b>1/4 without a stationary-phase asymptotic or numerical scan.

The example has fixed positive Mahler measure; it is not a family tending to1.
It proves sharpness of the universal quarter exponent for this absolute coefficient estimate on the complete named class, while leaving the half-exponent gate Q'(2)!=0 and additional justified near-one hypotheses open.

## 5. Sources, scope and verification limits

The original reciprocal trace construction is used only within L66's stated field-degree boundary; total reality and simple interlacing are reconstructed from the genuine Salem domain here.
The first-derivative and Fejer mechanisms have the retained exact source accounts in L368/R193, and their complete explicit local formulas were checked rather than extrapolating a generic stationary-phase claim.
This review identifies no new unresolved mathematical dependency or source-use extension within that scope.
It does not certify novelty, a literature-wide search or a fresh audit of the original upstream sources.

No mathematical program, algebraic-root isolation, finite coefficient evaluation, numerical quadrature, old J rerun or proof-assistant verification was performed or needed for this symbolic proof.
Material-format checks, reported separately by the creating command, are not mathematical evidence.
All review conclusions concern the frozen argument above; later substantive changes require review at their actual scope.

<a id="whole-salem-specialization-finding"></a>

## Complete Salem-specialization outcome

**Pass for the complete frozen symbolic argument and its explicit limits.**
No actionable mathematical, input-domain, endpoint/cusp, multiplicity, constant, estimate-direction, irreducibility or retained-source-interface defect was found in complete Sections1--5 and equations(1)--(11).
Genuine Salem trace interlacing gives the uniform absolute moment exponent1/4, and1/2 under the exact condition Q'(2)!=0.
The smaller degree-d integer critical polynomial gives the stated alternative fully paid constant.
The genuine irreducible quartic rules out every stronger absolute decay exponent on the whole class, even with arbitrary input-dependent constants.

The finding supports only this result and its declared conditioning limits.
No uniformly useful K_P, finite numerical lower-certificate value, unrestricted Lehmer gap, canonical Claim adoption or G0001 completion is established.
G0001 remains active and mathematically unresolved.
The root main agent owns any fixed retention, adoption, strategy consequence and shared navigation.

## Actual initial-context relationship clarification

The original initial whole-target inspection expressly included the author mathematical self-check before reporting this whole outcome. Its separately assigned/noncontributing role and pre-upstream-review reconstruction do not remove that actual target-author input. The whole finding is SELF; every original mathematical conclusion, date, binding, source boundary and computation limit remains unchanged.
This declaration clarifies the original arrangement; it does not record a new historical review, withdraw a mathematical result or reopen a Task.
