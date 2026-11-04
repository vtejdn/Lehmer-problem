---
author: Yin
---

# Complete summed local-curvature oscillatory moment and tail certificate

This retains the complete necessary mathematical argument from [the complete original L375 Sections1–7/equations1–14](../ledger/Yin_L_G0375_v1.md#local-salem-critical-data).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P in Z[t] be a genuine Salem minimal polynomial, monic reciprocal irreducible of degree d=2s>=4, with roots beta>1, beta^(-1), and d-2 unit-circle conjugates; let H=sum_j|p_j| and write P(t)=t^s Q(t+t^(-1)) with Q monic integral.
Set B(theta)=Q(2cos(theta))^2, phi(theta)=arccos(2B(theta)/H^2-1), and mu_k=(2pi)^(-1)integral_circle cos(k phi(theta))dtheta for every integer k>=1.
Use the exact canceled g=A/D=(phi')^2 from C398 on smooth pieces, extended at removable cusps, with D having no circle zero; Z={B=0 or H^2} is the finite cusp set.
The actual coefficient signs give0<|P(1)|=|Q(2)|<H.

Let theta_i be all distinct zeros of g on the circle, at most d, and q_i in{2,4} their first nonzero phase-derivative orders (g has order2(q_i-1)).
All are smooth interior-phase stationary points; cusps have positive canceled g and are excluded from this list.
The only possible q_i=4 point is0, occurring exactly when Q'(2)=0; all other points have q_i=2.
Put c_i=|phi^(q_i)(theta_i)|>0 and kappa_i=c_i/2, with the exact interior, endpoint and quartic formulas(2) below; all Q' leading/content factors and all real derivative roots, including any exterior root, remain in those data.

For n>=1 put T_n=d^n H^2, v_i=min(B(theta_i),H^2-B(theta_i))>0, and let Delta_i be the minimum circular distance to every other stationary/cusp point, capped at pi (pi if there is none).
Define r_i^0=min(1,Delta_i/3,v_i/(2T_1)), and for n>=1 use the finite coefficient sum

    E_n(v)=sum_(m_1+2m_2+...+n m_n=n)
      n! r!/[product_j m_j!(j!)^(m_j)]
      * (2/v)^r product_j T_j^(m_j),   r=sum_j m_j.

Then delta_i=min(r_i^0,c_i/[2E_(q_i+1)(v_i)])>0 defines pairwise disjoint circle arcs U_i avoiding every cusp, and |phi^(q_i)|>=kappa_i on U_i.
An arc crossing0 is integrated exactly once in its real lift.
The proof establishes integral_U exp(ik phi) bounded by8(k kappa)^(-1/2) for a smooth phase with |phi''|>=kappa, and by32(k kappa)^(-1/4) if |phi''''|>=kappa; all empty/full/truncated bad-set limits are included.

Partition the complement of all U_i at the remaining cusps, zeros of K=A'D-AD', and an angular cut, skipping a zero polynomial K.
There are at most J=16d+2 smooth monotonicity intervals I_j; on each use its actual canceled positive endpoint limits and set lambda_j=sqrt(min(g(left_j),g(right_j)))>0.
Retain the complete leading-factor and full-multiplicity factorization of A/D, with all off-circle numerator/denominator roots and any radial bounds paid separately as in(8).
No global product minimum or uncharged omitted neighborhood is substituted.
Set empty sums to zero and define

    A_2=(4/pi)sum_(i:q_i=2)kappa_i^(-1/2),
    A_4=(16/pi)sum_(i:q_i=4)kappa_i^(-1/4),
    A_1=(2/pi)sum_j lambda_j^(-1).

For every integer k>=1,

    |mu_k|<=min(1,A_2 k^(-1/2)+A_4 k^(-1/4)+A_1/k).

There is at most one A_4 summand, and A_4=0 when Q'(2)!=0.
For every integer N>=1 the full absolute logarithmic tail is at most

    R_N^local(P)=2A_2 N^(-1/2)+4A_4 N^(-1/4)+A_1/N.

This remains uniform after multiplication by rho^k for0<rho<=1.
The same exact unregularized original moments satisfy

    m(P)>=log(H/2)+sum_(k=1)^N(-1)^(k+1)mu_k/k-R_N^local(P).

No modified moments, new regularizer, inverse spectral gap, moment evaluation or root scan is introduced.

For the actual irreducible Salem quartic with Q=x^2-4x+1 and H=13, u=1-cos(theta) gives g=32u^3/[(u+2)(2u^2+5)], with its removable pi limit.
Its sole stationary point0 is quartic, c_0=12/sqrt(10), kappa_0=6/sqrt(10), A_2=0 and A_4=(16/pi)(sqrt(10)/6)^(1/4).
The fully paid delta_0 still comes from(3)--(4); four actual complementary pieces permit A_1<=8/[pi sqrt(g(delta_0))].
This is an exact symbolic control without numerical evaluation.

The explicit constants 8 and 32 are proved locally; Tao26 Lemma2.5 supplies checked higher-derivative method attribution only, without an external implicit constant or proof premise.
These are input-dependent fully paid estimates, not an evaluated lower bound or a uniform improvement on every input.
No near-one control of A_2,A_4,A_1 is proved: at N asymptotic to d the displayed sufficient conditions A_2=o(sqrt(d)), A_4=o(d^(1/4)), A_1=o(d) remain unestablished.
The earlier exponential obstruction for a different global product cost does not lower-bound these local costs, and no useful uniform near-one window or unrestricted Mahler gap follows.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:07 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact canceled-phase and moment interface](Yin_C_G0398_v1.md#unregularized-integer-moment-certificate) | Only the original B/phi/mu_k, exact g=A/D cancellation and positive cusp extensions, rational derivative partition and unregularized logarithmic identity; the new local curvature/radius estimates are proved here. |
| dependency | [Exact genuine Salem critical orders](Yin_C_G0402_v1.md#salem-interlacing-critical-orders) | Only genuine Salem trace roots, every real simple Qprime interlacing root and exact smooth/cusp critical orders, actual quartic and original-degree boundary; the three local costs are not inherited estimates. |
| dependency | [Earlier specific global-product comparison](Yin_C_G0406_v1.md#salem-nearest-product-exponential-cost) | Only the exact previous global nearest-product expense obstruction as comparison, which does not transfer automatically to the new local costs. |
| support | [Exact original higher-derivative attribution](../audits/literature/Tao26/Yin_U002.md#tao26-u002) | Only the original directly text/visually checked Lemma2.5 statement and interval/coefficient normalization; explicit constants8 and32 and all applicability costs are fully local, with no uninspected implicit constant or source-proof premise. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:09 |
| status | proved |
| reason | Adopt after actual complete current SELF inspection of every original critical/cusp/radius/derivative/partition/root-factor and normalized whole-circle/tail step, exact symbolic quartic and source/near-one limits. Original R200 initial whole reading included the explicit full author check, so its SELF relationship/date/scopes remain separately historical; no independent coverage or new source/native run is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0398_v1.md#unregularized-integer-moment-certificate) | Only the original B/phi/mu_k, exact g=A/D cancellation and positive cusp extensions, rational derivative partition and unregularized logarithmic identity; the new local curvature/radius estimates are proved here. |
| dependency | [Exact accepted input](Yin_C_G0402_v1.md#salem-interlacing-critical-orders) | Only genuine Salem trace roots, every real simple Qprime interlacing root and exact smooth/cusp critical orders, actual quartic and original-degree boundary; the three local costs are not inherited estimates. |
| dependency | [Exact accepted input](Yin_C_G0406_v1.md#salem-nearest-product-exponential-cost) | Only the exact previous global nearest-product expense obstruction as comparison, which does not transfer automatically to the new local costs. |
| support | [Exact support](../audits/literature/Tao26/Yin_U002.md#tao26-u002) | Only the original directly text/visually checked Lemma2.5 statement and interval/coefficient normalization; explicit constants8 and32 and all applicability costs are fully local, with no uninspected implicit constant or source-proof premise. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0624_v1.md#current-local-curvature-whole-finding) | Entire precise current statement and necessary original Sections1–7/equations(1)–(14), all actual Salem/canceled-phase domains, complete coefficient-certified radii, explicit constants8and32, complementary endpoint/full-factor costs, all integers k>=1/N>=1 and rho limits, exact quartic and unproved near-one cost conditions. Actual whole relationship is self-reviewed. |

## Complete retained argument

<a id="argument"></a>
<a id="summed-local-curvature-certificate"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="local-salem-critical-data"></a>
## 1. Complete actual critical data and smooth local phases

Retain the original genuine Salem P, degree d=2s>=4, beta>1, coefficient sum H, monic integer trace polynomial Q, and phase/moments

    B(theta)=Q(2cos theta)^2=|P(e^(i theta))|^2,
    phi(theta)=arccos(2B(theta)/H^2-1),
    mu_k=(1/(2pi))integral_circle cos(k phi(theta))dtheta.

L368 supplies the exact canceled rational function g=A/D=(phi')^2, with D having no unit-circle root, and the finite cusp set Z={B=0 or H^2}.
L369 supplies every phase-critical multiplicity and the simple real interlacing roots of Q'.
We use these inputs at their reviewed scope rather than repeating their exponent theorem.

One useful actual-domain refinement removes a merely possible upstream endpoint-value branch.
P has a positive real root beta, but its leading and constant coefficients are1.
Some coefficient must therefore be negative; otherwise P(beta)>0.
At1 the coefficient sum consequently has both signs, so

    0<|Q(2)|=|P(1)|<H.                                 (1)

The first inequality follows from the irreducible nontorsion original input.
Thus the phase value at0 is always interior.
In this genuine Salem domain every zero of canceled g is a SMOOTH stationary point at an interior phase value.
Interior Q zeros are linear cusps with positive limiting g, as are interior Q' extrema with B=H^2 and endpoint pi with B=H^2; none is inserted as a stationary point.

Let theta_i be ALL distinct zeros of g on the angle circle.
There are at most d.
They have q_i=M_i+1 in{2,4}.
The fourth-order case occurs precisely at theta_i=0 when Q'(2)=0, so there is at most one such point.
Every other theta_i is quadratic.
Write

    c_i=|phi^(q_i)(theta_i)|>0,   kappa_i=c_i/2.

These are explicit original-input local data.
For an interior Q' root y in(-2,2) with Q(y)^2<H^2, each of its two angular points has

    c_i=2(4-y^2)|Q''(y)|/sqrt(H^2-Q(y)^2).

For theta_i=0 or pi with Q'(2cos theta_i)!=0 and B(theta_i)<H^2,

    c_i=4|Q'(2cos theta_i)|/sqrt(H^2-Q(2cos theta_i)^2).

For the fourth-order point0,

    c_i=24|Q''(2)|/sqrt(H^2-Q(2)^2).                    (2)

These follow by differentiating the L369 phase formula or taking its exact leading terms.
The original leading/content and EVERY real derivative root are present: if Q'=s product_j(x-y_j), then Q''(y_i)=s product_(j!=i)(y_i-y_j), including the possible exterior y_j>2.
Endpoint Q' values contain that full product as well.
The possible off-circle critical pair has not been discarded by retaining only angular stationary points.

<a id="local-coefficient-certified-neighborhoods"></a>
## 2. Neighborhood radii certified by explicit coefficient costs

The local estimates require a neighborhood on which the indicated higher derivative stays nonzero.
We now pay for it, rather than assume generic curvature.
For n>=1 set T_n=d^n H^2.
The Laurent symbol B has frequencies between-d and d and coefficient sum at most H^2, hence

    ||B^(n)||_infinity<=T_n.

At theta_i put v_i=min{B(theta_i),H^2-B(theta_i)}>0.
Let Delta_i be the minimum circular angular distance to every OTHER point in the finite set {theta_j} union Z, capped at pi; if no other point exists use pi.
Define

    r_i^0=min{1,Delta_i/3,v_i/(2T_1)}.

Then these preliminary neighborhoods avoid all cusps, are pairwise disjoint, and have v_i/2<=B<=H^2-v_i/2.
For f(u)=arccos(2u/H^2-1), f'(u)=-[u(H^2-u)]^(-1/2).
Differentiating its two factors gives, on that range,

    |f^(r)(u)|<=r! (2/v_i)^r, r>=1.

For clarity, each order-j derivative of the product f' is bounded by the sum of binomial(j,l)l!(j-l)!(2/v_i)^(j+1), namely(j+1)!(2/v_i)^(j+1); setting r=j+1 gives the stated conservative bound.
No uniform regularity at B=0,H^2 is presumed.

Iterating the ordinary chain rule gives the following finite explicit bound:

    E_n(v)=sum_(m_1+2m_2+...+n m_n=n)
       [n! r!/(product_j m_j! (j!)^(m_j))]
       (2/v)^r product_j T_j^(m_j),
       r=sum_j m_j.                                  (3)

Thus ||phi^(n)|| on the i-th preliminary neighborhood is at most E_n(v_i).
Only n=3 or5 is needed.
Put

    delta_i=min{r_i^0,c_i/[2E_(q_i+1)(v_i)]}>0.          (4)

The mean value theorem now gives |phi^(q_i)|>=kappa_i throughout the radius-delta_i neighborhood U_i.
All U_i are disjoint circle arcs and contain no cusp.
A neighborhood crossing the angular origin is treated in its ordinary real lift about0, with no doubled point or halved Haar normalization.
Phase-value distance, coefficient scale, original degree, local leading derivative and angular separation are all paid in(2)--(4).
No claim is made that these conservative radii are large, optimal or computed.

<a id="explicit-local-vdc-two-four"></a>
## 3. Full explicit second- and fourth-derivative estimates

The retained [Tao26 primary PDF](../literature/pdf/Tao26.pdf), complete printed/PDFp.5, was directly text-read and rendered/visually inspected.
Its Lemma2.5 has exactly the smooth-phase, uniform |phi^(r)|>=c, r>=2 and interval-length-independent conclusion used for method attribution.
It imposes no separate monotonicity assumption when r>=2.
Its implicit constant is not used.
The following elementary specializations prove the constants needed here, so no uninspected higher-derivative proof is a premise.

First recall L368's explicit bound4/(k lambda) when phi' is monotone and |phi'|>=lambda.
Integration by parts gives at most2/(k lambda) from endpoints and at most2/(k lambda) from the total variation of1/phi'; exhausting an open interval by closed subintervals preserves the bound.

**Second derivative.** If |phi''|>=kappa on a smooth interval, it has fixed sign and phi' is monotone.
The portion |phi'|<=alpha has length at most2alpha/kappa.
Its complement consists of at most two intervals, each bounded by4/(k alpha).
Taking alpha=2sqrt(kappa/k) gives

    |integral_I exp(i k phi)|<=8(k kappa)^(-1/2).        (5)

The same conclusion holds if the small-derivative set is empty, all of I, or truncated by an endpoint.
No interval-length or assumed C3 bound enters this estimate.

**Fourth derivative.** If |phi''''|>=kappa on a smooth interval, h=phi'' or h=-phi'' has h''>=kappa.
The set |h|<=alpha has at most two interval components, because h is strictly convex.
Any such component of length ell obeys

    h(midpoint)<= [h(left)+h(right)]/2-kappa ell^2/8.

Since all its values lie between-alpha and alpha, ell<=4sqrt(alpha/kappa).
Its total length is therefore at most8sqrt(alpha/kappa), including limiting/open components.
The complement has at most three intervals with |phi''|>=alpha.
Applying(5) on each and taking alpha=sqrt(kappa/k) gives

    |integral_I exp(i k phi)|
       <=8sqrt(alpha/kappa)+24(k alpha)^(-1/2)
       =32(k kappa)^(-1/4).                           (6)

The convexity inequality follows by subtracting kappa x^2/2 and using midpoint convexity; the component count follows from the two convex sublevel intervals {h<=alpha} and {h<-alpha}.
This proof pays the complete possible two-component bad set, not just one.
Closed exhaustion and bounded convergence justify every open endpoint.

<a id="complementary-interval-derivative-costs"></a>
## 4. Complementary intervals with their own complete derivative minima

Remove the U_i from the circle.
Partition the remainder at every cusp in Z, every circle zero of K=A'D-AD', and a chosen angular cut, as in L368.
If K is identically zero no K partition is inserted.
There are at most8d-1 rational-derivative zeros,2d cusps,2d local-arc boundaries and one angular cut.
Hence at most J=16d+2 open intervals I_j suffice.
On each, phi is smooth, phi' has fixed nonzero sign and g is monotone or constant; consequently phi' is monotone.

Canceled g is continuous on every closed interval closure and has no zero there: all its zeros are strictly inside the removed U_i.
Its cusp limits are positive when a cusp lies at an interval endpoint.
Define the PAID local minimum

    lambda_j=sqrt(min{g(left endpoint),g(right endpoint)})>0. (7)

Because g is monotone or constant this is the exact derivative lower bound on the interval.
An empty remainder contributes no intervals.
At cusp endpoints evaluate the continuous canceled A/D, not the uncanceled formula.
All quantities are explicit finite real input data determined by(2)--(4), actual roots of K and the original A/D; no root isolation or numerical certification is asserted.

Every coefficient, leading factor, content and off-circle root remains in(7).
On the unit circle the complete factorization used to evaluate g is

    g(z)=|lead A|/|lead D|
          product_(gamma:A(gamma)=0)|z-gamma|^mult(gamma)
          /product_(xi:D(xi)=0)|z-xi|^mult(xi).          (8)

D has no circle root by L368.
Off-circle distances are retained at the ACTUAL interval endpoints; they can be certified directly or conservatively bounded using ||gamma|-1| for a numerator factor and1+|xi| for a denominator factor.
Such optional radial bounds pay every member and multiplicity and may weaken the result.
The common rational clearing factor cancels from the ratio.
There is no replacement by a selected factor, no coefficient-free spectral gap, and no factor1/2 per other circle root.
Taking one global minimum over j is unnecessary.

<a id="summed-local-paid-tail-certificate"></a>
## 5. A three-term summed local moment and logarithmic-tail certificate

Define the three COMPLETE positive costs, allowing empty sums to be zero:

    A_2=(4/pi) sum_(i:q_i=2) kappa_i^(-1/2),
    A_4=(16/pi)sum_(i:q_i=4) kappa_i^(-1/4),
    A_1=(2/pi) sum_j lambda_j^(-1).                    (9)

They refer to the SAME original symbol, not separately scaled phases.
Splitting the full oscillatory integral into the disjoint U_i and I_j, using(5),(6) and the first-derivative estimate, dividing by2pi and taking real parts gives for every integer k>=1

    |mu_k|<=min{1,A_2 k^(-1/2)+A_4 k^(-1/4)+A_1/k}.     (10)

There is at most one A_4 summand.
If Q'(2)!=0, A_4=0.
Every critical point contributes separately to the corresponding SUM.
Unlike deleting k-dependent arcs and then dividing by one global product minimum, no critical neighborhood is omitted from the integral: its oscillatory integral is estimated directly by its own certified higher derivative.

Integral comparison therefore gives for integer N>=1

    sum_(k>N)|mu_k|/k
       <=2A_2 N^(-1/2)+4A_4 N^(-1/4)+A_1/N
       =:R_N^local(P).                                (11)

The same bound is uniform after inserting any regularizer rho^k with0<rho<=1.
L368's exact unregularized logarithmic identity consequently gives the new direct finite certificate

    m(P)>=log(H/2)+sum_(k=1)^N (-1)^(k+1)mu_k/k
                           -R_N^local(P).              (12)

No further regularizer, inverse spectral gap or modified moment sequence is introduced.
The finite rational integer-coefficient moments are exactly the retained L368 ones, and none has been evaluated here.

This is a changed fully paid bound, not radius retuning of L371's refuted global estimate.
Small certified radii can make A_1 large, but that complementary cost now has tail order1/N; it is not automatically absorbed into a quarter-power constant.
The local leading costs A_2,A_4 retain every actual curvature.
The bound is not asserted to outperform L368/L369 on every input, and the minimum of certified tails may be used.

<a id="actual-quartic-local-tail-control"></a>
## 6. Exact quartic control and remaining uniformity obligations

Use L369's actual irreducible Salem quartic Q=x^2-4x+1 and H=13, not a relaxed phase.
With u=1-cos theta, direct cancellation of its original phase gives

    g(theta)=32u^3/[(u+2)(2u^2+5)].                     (13)

Indeed Q=-3+4u^2, H^2-Q^2=8(4-u^2)(2u^2+5), and the squared numerator in the phase derivative is256u^3(2-u).
The ratio extends at pi by cancellation.
The only zero of g is0, of order6, so there is one quartic critical point and no quadratic stationary point.
Its c_0=12/sqrt10, kappa_0=6/sqrt10 and

    A_2=0, A_4=(16/pi)(sqrt10/6)^(1/4).                 (14)

The radius delta_0 is still paid by(3)--(4).
On0<=u<=2, differentiating u^3/[(u+2)(2u^2+5)] has strictly positive numerator u^2(4u^2+10u+30).
Thus g increases from0 to pi and then decreases.
Outside the critical arc there are four smooth monotonicity pieces, separated by the two actual Q zeros and the cusp at pi.
All have derivative at least sqrt(g(delta_0)).
In particular one may use the explicit conservative complementary cost

    A_1<=8/[pi sqrt(g(delta_0))].

This is an exact symbolic paid control, with no root or moment scan.
The sharpness obstruction already established in L369 still precludes removing the quarter exponent from ALL absolute-moment bounds on this class.
The new separation of local curvature and faster complementary expense is compatible with that obstruction.

There is no established bound on the three costs over a near-one sequence.
The coefficient construction(3) can be extremely conservative; shrinking neighborhoods or close off-circle/critical roots can still make A_1 huge.
Local inverse curvatures may also diverge, and all stationary points have been summed.
At a degree-linear window N asymptotic to d, sufficient conditions for the local remainder to tend to zero would be

    A_2=o(sqrt d), A_4=o(d^(1/4)), A_1=o(d).

None is proved here.
Other N scales require the corresponding actual inequalities in(11).
The prior exponential lower bound for L369's SPECIFIC global product constant does not automatically lower-bound these different costs.
Conversely the present derivation does not establish a useful near-one uniform window or an unrestricted Mahler gap.

<a id="local-curvature-entire-author-freeze"></a>
## 7. Sources, verification and entire author freeze

Tao26 p.5 Lemma2.5 is recognized classical attribution for higher-derivative van der Corput estimates; its exact statement and interval/coefficient normalization were directly text/visual checked.
The explicit constants8 and32 are proved completely here.
No stationary-phase asymptotic, smooth-amplitude theorem, new source theorem, or uninspected implicit constant is a premise.
The source remains undated; no date is inferred from its server URL.

The original input, gcd cancellation, cusp limits and rational partition are the exact retained L368 interfaces.
Real-trace critical orders, the actual quartic and original-degree boundaries are L369.
The scope of the preceding failure is fixed in L371.
All actual polynomial, endpoint, off-circle, separation, coefficient and normalized Haar costs remain in the new data above.
No mathematical program, J, root-data certification, finite moment evaluation, quadrature or scan was run.
Material-format checks and the source-PDF rendering are operational inspections only.
