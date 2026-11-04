---
author: Yin
---

# Complete critical-level positive-log tails, unrun quadrature and exact original-Lehmer certificate

This retains the complete necessary mathematical argument from [the complete original G383 account](../ledger/Yin_L_G0383_v1.md).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be an actual genuine Salem minimal polynomial of original degree d=2s>=4, P(z)=z^s Q(z+z^-1), Q monic integral with s-1 simple roots in(-2,2) and one root x0>2.
Use original H=sum|P_j|, total logarithmic m(P), actual nonnegative moments nu_n=integral(1-|P|²/H²)^n and T_N=logH-(1/2)sum_(n=1)^Nnu_n/n.
Every original root/coefficient and the full exterior pair remain in Q, all values/derivatives and the exact identity T_N-m=(1/2)sum_(n>N)nu_n/n.

Let Y be all real roots of Q' in[-2,2], with endpoint critical points included, and put b_*=min{|Q(-2)|,|Q2|,|Q(y)|:y inY}>0.
For any rational0<b<b_*, the full sublevel set{|Q|<=b} in[-2,2] is exactly s-1 disjoint interior closed intervals J_i, each containing exactly one circle trace root, with opposite endpoint levels+/-b and fixed nonzero derivative sign.
Choose disjoint rational interior intervals I_i covering J_i, with Q' nonzero there, and actually certified rational D_i>0 such that(4-x²)Q'(x)²>=D_i on every I_i.
Every gate, root/level/derivative isolation, subdivision and weighted lower-bound cost must be certified in a numerical application.
Then for every n>=1 and integer N>=1,

    nu_n<=C_I n^-1/2+rho^n,
    C_I=(H/sqrt(pi))sum_i D_i^-1/2,
    rho=1-b²/H² in[0,1),
    0<=T_N-m<=C_I/sqrtN+rho^(N+1)/[2(N+1)(1-rho)]=R_N^I,
    m>=T_N-R_N^I.

The rho0 term is0.
The proof uses the full paired Haar density1/[pi sqrt(4-x²)], monotone y=Q(x), the exact weighted derivative cost and a complete complementary modulus b, not a product of root distances or a missing factor2.
No actual critical/endpoints, cover, derivative, H or off-circle cost is omitted, and no all-input/degree-uniform useful cutoff follows.

There is also a fully proved but UNRUN finite quadrature alternative.
For F_N(theta)=logH-(1/2)sum_(n=1)^N(1-|P(e^itheta)|²/H²)^n/n, the positive derivative in B=|P|² and nonzero degree-d extreme autocorrelation give at most2d monotone circle pieces and Var(F_N)<=d H_N.
For every integer M>=1, its exact M-point mean A_(N,M) obeys |T_N-A_(N,M)|<=d H_N/M.
For real coefficients and even M, endpoint weights1 and interior weights2 on M/2+1 nodes give precisely the same mean.
Thus a certified finite mean lower A_- and rational H_+>=H_N, R_+>=R_N^I yield m>=A_- -d H_+/M-R_+.
This samples a finite continuous polynomial even at zeros, not the singular logarithm or an assumed high-order quadrature.

The rational certification contract includes degree-exhausting distinct sign/point root brackets, full interval Horner/weighted inequalities, outward2^-p multiplication/division/sums, neighboring integer-square bounds, the directly proved Machin pi and atanh log9 series/remainders, and the unused degree80 cosine remainder4^82/82!.
The planned n<=8/M256 Fourier-grid discriminator is proved but was not executed after the method revision.

For the exact original Lehmer input

    P=[1,1,0,-1,-1,-1,-1,-1,0,1,1],
    Q=[3,4,-5,-5,1,1], d10,H9,
    R=81-Q²=[72,-24,14,70,9,-64,-23,20,9,-2,-1],

J87's sole original execution used b1/4,N4096,p160, grid[-2,9/4]step1/64, width<=2^-40/max60bisections,128cells on each of4covers,64-term arctan and128-term atanh enclosures, and the unchanged J86 integer recurrence under the original180second aggregate cap.
The exact-method revision and implementation handoff occurred before any mathematical execution; neither the original4096-node quadrature nor its256-node control was executed.
Original independent direct Laurent CT control reaches1–8 only; n64/n1024 are precise accepted upstream overlaps, not a fresh direct oracle at higher n.
All4096 exact terms I[n,0]/(n9^(2n)) are rounded outward on the common2^-160 grid, so log lower L_-, sum upper S_+ and tail upper R_+ give m>=L_- -S_+/2-R_+ without a variation allowance.
The finite certificate retains19 degree-exhausting roots,6critical/end gates,4complete covers/512cells, every4096rounded pair,9checkpoints and11final states.
It proves exactly

    m(P)>=415041559215166780091538487173593981975777634805
           /2923003274661805836407369665432566039311865085952
         >7/50.

The original counts are40960signed divisions/extended bounds,45067stored-state bounds,4097scalar bounds,4096monotonicity checks and term inequalities,1351680accumulations,25990/16/25975max numerator/divisor/extended-state bits and7816final scalar decimal digits.
The total rounded-sum width is4096/2^160 before the factor1/2.
Native decimals are readable approximations, while all acceptance inequalities use exact rational bounds; no expanding Salem-root approximation enters this lower certificate.
Original producer execution, original R209 verification and the new whole SELF reconstruction remain distinct actual events; native bytes and original pending-review metadata remain unchanged.
This is one original-input finite lower bound, with no new geometry parameter/input scan, external proof audit, near-one family, unrestricted gap or Task/E resumption.

## Current assessment
[Selected decision](#decision-complete-critical-positive-certificate-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:54 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact complete positive logarithmic series](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only exact original nonnegative moments/full all-multiplicity tail and finite upper/lower distinction; the new critical-level geometry is proved here. |
| dependency | [Exact accepted finite integer recurrence and costs](Yin_C_G0439_v1.md#argument) | Complete actual normalized trace state/signed divisions/integrality and all arithmetic/bit/output costs used through4096; original high-order evidence is separately implemented recurrence, not direct convolution. |
| dependency | [Original reciprocal and Salem trace domain](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the exact monic integral trace representation, original degree/all inverse pairs and separability; the stated genuine-Salem root pattern gives the trace locations directly, and all local sublevel/Gaussian/variation proofs are complete here. |
| dependency | [Exact original Lehmer input](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only the already accepted original degree10 irreducible genuine Salem/unit polynomial/root domain; no old optimized measure/collision/native output is an oracle for this new finite certificate. |
| dependency | [Exact original finite certificate](../computations/programs/Yin_J_G0087/readme.md) | Only the original fixed P/Q/b/N/p/grid/cells/series method, complete4096term/root/cell/checkpoint/final-state rational evidence and its actual execution/review/UNRUN boundaries; no producer or wider parameter scope. |


### Decision complete-critical-positive-certificate-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:56 |
| status | proved |
| reason | Adopt the exact complete original critical-level tail, UNRUN quadrature proof and sole original Lehmer finite certificate after the complete actual SELF reconstruction; retain all original costs/source/negative limits and truthful R209 SELF scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0434_v1.md#positive-log-moment-identity) | Only exact original nonnegative moments/full all-multiplicity tail and finite upper/lower distinction; the new critical-level geometry is proved here. |
| dependency | [Exact accepted input](Yin_C_G0439_v1.md#argument) | Complete actual normalized trace state/signed divisions/integrality and all arithmetic/bit/output costs used through4096; original high-order evidence is separately implemented recurrence, not direct convolution. |
| dependency | [Exact accepted input](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Only the exact monic integral trace representation, original degree/all inverse pairs and separability; the stated genuine-Salem root pattern gives the trace locations directly, and all local sublevel/Gaussian/variation proofs are complete here. |
| dependency | [Exact accepted input](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | Only the already accepted original degree10 irreducible genuine Salem/unit polynomial/root domain; no old optimized measure/collision/native output is an oracle for this new finite certificate. |
| dependency | [Exact accepted input](../computations/programs/Yin_J_G0087/readme.md) | Only the original fixed P/Q/b/N/p/grid/cells/series method, complete4096term/root/cell/checkpoint/final-state rational evidence and its actual execution/review/UNRUN boundaries; no producer or wider parameter scope. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0654_v1.md#current-critical-positive-tail-whole-finding) | Entire exact Statement and Argument, all Sections1–9/equations1–12, original rational/native/UNRUN limits and complete source/arithmetic/bit/output costs. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="complete-critical-level-positive-log-certificate"></a>
For the stated genuine Salem root pattern, every original circle inverse pair maps to2Re(gamma) in(-2,2), and the only expanding/contracting positive pair maps to beta+beta^-1>2.
Two different inverse pairs cannot have the same trace, since the roots of t²-xt+1 are precisely one inverse pair.
The accepted monic integral trace representation therefore has exactly the stated simple roots and no root at either endpoint; every original pair remains represented.


The original critical-level proof and its author implementation/handoff are retained below at their dated scopes, with the exact positive series now in [C434](Yin_C_G0434_v1.md#positive-log-moment-identity) and unchanged signed finite-state theorem/costs in [C439](Yin_C_G0439_v1.md#argument).
The full author checking/freeze and all contribution/history remain at the original responsible L/R; neither the unrun alternatives nor dated Task state is current execution authority.

<a id="critical-level-complement-theorem"></a>
## 1. Critical-value levels give a complete complement without a root product

Let Y be all real roots of Q' in[-2,2], including either endpoint when appropriate.
Since Q is squarefree and Q(+/-2)!=0, define the positive actual critical/end value

    b_* = min{|Q(-2)|,|Q(2)|, |Q(y)|:y in Y}>0.

Choose a rational0<b<b_*.
The set {x in[-2,2]:|Q(x)|<=b} consists of exactly s-1 disjoint closed intervals J_i, one about each actual circle trace root.
Every J_i lies strictly inside(-2,2), its endpoints have Q values-b and+b in one order, and Q' has a fixed nonzero sign there.                         (1)

Proof.
The endpoints are outside the sublevel set and no derivative zero can be inside it, by the strict critical/end gate.
Every connected component is therefore an interval on which Q is strictly monotone.
Its two endpoint values must be opposite levels, so it contains exactly one Q zero.
Conversely every one of the s-1 circle trace zeros lies in a component.
There is no endpoint or root-free sublevel component.
The remaining actual trace root x_0>2 does not introduce a component.
This proves(1), including the case Q'(2)=0: its nonzero endpoint value is still part of b_*.

Choose disjoint rational closed intervals I_i containing J_i, contained in(-2,2), with Q' nonzero on I_i.
Such choices exist by compactness and the strict gate.
Suppose rational numbers D_i>0 are CERTIFIED to satisfy

    (4-x^2)Q'(x)^2>=D_i for every x in I_i.             (2)

These are finite interval polynomial inequalities.
They can be certified by rational subdivisions and outward Horner/Bernstein bounds, or by exact critical-point isolation of the displayed polynomial.
No root-separation constant is assumed.
Every derivative/endpoint isolation and subdivision cost must be stated in an actual computation.

Outside union I_i, the original modulus is at least b, since the full sublevel set is covered.
This is an ACTUAL complementary modulus, with no factor1/2 for each root and no radial root-product replacement.
The full original off-circle pair remains in Q(x)=(x-x_0)product_(j<s)(x-x_j), in its coefficients, and in every value and derivative in(1)--(2).
No factor or original leading/content cost is removed.

<a id="trace-density-positive-tail"></a>
## 2. Local trace densities and the complete positive tail

The original normalized Haar change of variables is

    integral_circle F(Q(2cos theta)^2)dmu
       =(1/pi) integral_(-2)^2 F(Q(x)^2)/sqrt(4-x^2) dx. (3)

This counts both members of each original circle pair.
On each I_i, substitute y=Q(x), using its fixed derivative sign.
By(2) the inverse density1/[sqrt(4-x^2)|Q'(x)|] is at most D_i^-1/2.
The nonnegative local moment is therefore bounded by

    (1/(pi sqrt(D_i))) integral_R exp(-n y^2/H^2)dy
       =H/[sqrt(pi D_i n)].

The inequality uses1-u<=exp(-u), with the original0<=Q(x)^2/H^2<=1.
On the complement, use|Q|>=b and total Haar mass at most1.
Thus for every n>=1,

    nu_n<=C_I n^-1/2+rho^n,
    C_I=(H/sqrt pi)sum_i D_i^-1/2,
    rho=1-b^2/H^2 in[0,1).                            (4)

Every I_i and its full density cost is summed.
In particular no Taylor-radius eta loss is inserted as an uncomputed proxy for(2).
This is a different finite geometry from L378's product complement, not a retuning of that product.

Integral/geometric comparison then gives, for integer N>=1,

    0<=T_N-m<=C_I/sqrt N
             +rho^(N+1)/[2(N+1)(1-rho)]=:R_N^I.       (5)

At rho=0 the second term is0.
The finite lower direction is

    m>=T_N-R_N^I.                                    (6)

All constants are input dependent.
Small actual critical values, close trace roots, small weighted derivatives or large H can still make this expensive.
The level b, the rational covering intervals and every D_i require genuine certification.
No degree-uniform cutoff, all-Salem coefficient bound or Mahler gap is implied.

<a id="finite-positive-log-quadrature"></a>
## 3. A rigorous finite quadrature avoids an enormous Laurent expansion

Exact individual nu_n may be expensive.
The finite partial expression is also the integral of the continuous trigonometric polynomial plus a constant

    F_N(theta)=log H-(1/2)sum_(n=1)^N
                       (1-|P(e^(i theta))|^2/H^2)^n/n. (7)

For B=|P|^2, its derivative as a function of B is

    dF_N/dB=(1/(2H^2))sum_(n=1)^N(1-B/H^2)^(n-1)>0.

B is a nonconstant trigonometric polynomial of degree/span d, because its extreme autocorrelation coefficient is P_0P_d!=0.
Its derivative has at most2d distinct circle zeros: multiply its nonzero Laurent polynomial by z^d to obtain a polynomial of degree at most2d.
Therefore F_N has at most2d monotone circle pieces.
Its total value range is at most H_N/2, where H_N=sum_(n=1)^N1/n, so its total variation obeys

    Var(F_N)<=d H_N.                                 (8)

For integer M>=1 let A_(N,M)=M^-1 sum_(j=0)^(M-1)F_N(2pi j/M).
On each grid cell the point-sample error is at most that cell's oscillation times its normalized width1/M.
Summing the cell variations gives the proved elementary bound

    |T_N-A_(N,M)|<=d H_N/M.                          (9)

No assumed high-order quadrature, sampling of a singular logarithm or Fourier tail is used.
F_N is a finite continuous polynomial even at P's zeros.
For real P, its symmetry allows an even M to be evaluated at M/2+1 nodes with weights1 at0,pi and2 elsewhere; this is the SAME original M-point average.

If an outward rational interval [A_-,A_+] encloses that finite sample average, and rational upper bounds R_+>=R_N^I and H_+>=H_N are certified, then

    m>=A_- -d H_+/M-R_+.                            (10)

This enclosures the exact same rational-moment T_N; it does not claim each nu_n has been individually expanded or evaluated.
The additional arithmetic/variation allowance in(10) is explicit.

<a id="rational-computation-contract"></a>
## 4. Fully rational certification and elementary constants

The needed operations can all be performed with rational or outward fixed-point arithmetic.
Rational sign brackets that give as many DISTINCT real roots as the polynomial degree exhaust every root and prove simplicity; no uninspected root solver is required.
Refining those brackets isolates the roots of Q,Q',Q-b,Q+b.
Interval evaluation at every critical bracket proves b<b_*; the Q+/-b brackets provide the J_i covers.
Finite subdivisions of I_i can verify the same nonzero derivative sign and a positive lower bound(2) using the elementary product(4-x^2)Q'^2.

For sample nodes, enclose pi and cos(2pi j/M) and evaluate the original Q by interval Horner.
Square and intersect with the proved range0<=B<=H^2.
On a common grid of denominator2^p, round every multiplication, division, square and sum outward.
For u=1-B/H^2 in[0,1], repeated multiplication encloses each u^n and then sum u^n/n; no floating estimate is a proof bound.
Integer square roots enclose sqrt(pi) and sqrt(D_i).
The rational geometric tail can be bounded by an outward integer power of the fixed rational rho.

For completeness, the elementary pi identity used for certification is

    pi=16 arctan(1/5)-4 arctan(1/239).

The tangent addition rule gives tan(2a)=5/12 and tan(4a)=120/119 for a=arctan(1/5).
Subtracting arctan(1/239) gives tangent1, and the angle is between0 and pi/2, hence equals pi/4.
Integrating the finite geometric series supplies alternating rational arctan bounds.
The logarithm uses log9=4atanh(1/2), whose positive series has remainder at most4(1/2)^(2K+1)/[(2K+1)(1-1/4)] after K terms.
These are direct elementary identities, not a new numerical source theorem.

For cos on[0,pi], the degree80 Taylor polynomial has absolute remainder at most4^82/82!, using pi<4 and the degree81 Taylor formula whose odd coefficients vanish.
At fixed precision this remainder and every intermediate arithmetic error are explicitly included.
Ordinary square-root rounding is verified by the neighboring integer-square inequalities.
No call to an unvalidated transcendental or floating quadrature routine is needed.

A meaningful independent arithmetic control is available on the SAME polynomial: for n<=8 the Fourier degree of(1-B/H^2)^n is at most80.
An M=256 uniform grid therefore integrates it exactly, by the finite geometric sum for every nonzero frequency |h|<256.
Exact small CT powers can be compared against the interval sample result for sum_(n=1)^8nu_n/n.
This checks the original symbol, both normalizations, interval trigonometry and finite-sum arithmetic without assuming the large-N result.

<a id="lehmer-bounded-candidate"></a>
## 5. Original Lehmer candidate and required finite scope

The intended single actual input is the retained original Lehmer polynomial

    P=[1,1,0,-1,-1,-1,-1,-1,0,1,1] in ascending order,
    Q=x^5+x^4-5x^3-5x^2+4x+3,
    d=10,H=9.

Its irreducible genuine Salem status is the retained L66/L369 input, not a new root scan.
The changed finite candidate fixes b=1/4, N=4096 and M=4096, with common precision p=160bits.
No parameter tuning or other polynomial is selected.
The critical/end gate b<b_* and every weighted derivative bound remain to be proved by the declared native computation, so no useful certificate is asserted in advance.

The planned finite rational geometry searches exactly the grid[-2,9/4] with step1/64 for Q,Q',4Q+1,4Q-1, requires degree-exhausting distinct brackets, and bisects each to width at most2^-40.
Exact rational grid roots are retained as point intervals.
The eight Q+/-b roots inside[-2,2] form four rational I_i covers, which must be disjoint and interior and contain the four actual circle trace roots.
Each I_i is divided into128 equal rational cells for the full nonzero Q' sign and positive D_i bound.
All root counts, critical interval values, endpoints and subdivision minima must be retained.

The large finite partial sum uses the full M=4096 average, evaluated by symmetry at2049 nodes, with4096 positive powers at each.
Constants use64-term arctan series,128-term atanh series and the fixed degree80 cosine polynomial; every remainder is rounded outward.
The independent same-input control uses exact CT moments through8 and the256-node grid, with no new input family.
One aggregate author execution may use at most180seconds and stops at the first mathematical check, scope, positivity, precision or resource failure.
No retry, larger cutoff, altered b or widened grid is authorized by this declaration.
A precise J will be allocated BEFORE any mathematical program executes, and every actual outcome, including a vacuous or failed certificate, will remain explicit.

## 6. Proof boundary before computation

Sections1--4 give the complete symbolic reduction, with equations(1)--(10) and all original degree/root/coefficient costs.
The elementary critical-level argument, monotone change of variables, Gaussian bound and bounded-variation inequality are proved here; the exact infinite positive-log identity is the reviewed L378 input.
This work supplies no unrestricted positive gap or near-one uniformity.
Numerical usefulness on Lehmer is an unrun finite question until its J output and mathematical checks exist.

The original author self-check and contribution/then-pending-review account remain in the complete responsible L383 and corresponding exact original-author R finding.
The necessary mathematical proof, all source/input boundaries and the actual pre-run revision follow at their unchanged scopes.

<a id="pre-run-exact-recurrence-revision"></a>
## 7. Explicit pre-run method revision after the new exact recurrence

2026-10-11T14:55.
A transient stream interruption occurred after the complete proof and [J87 declaration](../computations/programs/Yin_J_G0087/readme.md) were saved.
Recovery inspection found ONLY the J87 README: no program, output, partial output or mathematical execution existed.
The root's new instruction supplied the intervening [L379 finite integer-state theorem](../ledger/Yin_L_G0379_v1.md#triangular-integration-by-parts-reduction), retained from D25 with [R205](../audits/reviews/Yin_R_G0205_v1.md#finite-arcsine-state-whole-finding), and its [J86](../computations/programs/Yin_J_G0086/readme.md) exact implementation and controls.
This author read the complete proof, the actual fast/direct programs and the retained1024scope before changing this unrun method.
The original Sections3--5 remain a proved but UNRUN quadrature alternative.

The revised first execution keeps the identical original Lehmer input, b=1/4,N=4096,160bits, root grid/refinement/128-cell geometry and aggregate180second one-run cap.
It replaces the planned4096-node quadrature/cosine calculation and256-node control with the reused exact integer-state recurrence.
The direct original-Laurent CT control through8 remains; named n64 and1024 scalar overlaps are also checked against J86's retained exact data.
No other input, cutoff, geometry parameter or retry is added.
This revision precedes program implementation and first execution and is also explicit in J87.

The recurrence input is the ORIGINAL R=H^2-|P|^2 expressed at x=z+z^-1, degree d=10 and

    R=[72,-24,14,70,9,-64,-23,20,9,-2,-1] ascending.

Its signed triangular reduction and d+1-state update are the complete D25 identities, with exact integer divisions, full state bounds and original arcsine normalization.
Root supplied that upstream core; its development and verification remain attributed there.
This is mathematical/implementation reuse, not a new recurrence contribution.
All4096 rational terms nu_n/n are now accumulated outward directly from their exact integer numerator I[n,0] and known denominator n H^(2n).
No float, quadrature or individual moment approximation supplies the numerator.

If S_-<=sum_(n=1)^Nnu_n/n<=S_+ are the resulting rational bounds, L_-<=log H<=L_+ and R_+>=R_N^I, the final lower certificate becomes simply

    m(P)>=L_- -S_+/2-R_+.                              (11)

There is no variation allowance in(11), because no sampling is used.
Every fixed-point summand is rounded outward; its total accumulation error is at most N/2^160 on each side before the factor1/2, in addition to the separately enclosed logarithm and tail constants.
Native output will retain all rounded term pairs, declared exact checkpoints and final full state, rather than pretending to retain every enormous integer state.
The full upstream bit/output costs remain paid.

This change makes the full finite positive-log evaluation linear in N at fixed d, using the existing recurrence, while the newly proved critical-level/weighted-density tail remains the contribution of Sections1--2.
Any failed or nonpositive finite result must still be preserved.
No mathematical execution or useful lower bound is claimed by this pre-run revision.

## 8. Pre-execution author handoff and implementation inspection

After a second transient stream disconnection, the root confirmed that the prior author had stopped and that J87 still contained only its README, without a mathematical program, output or native execution.
The replacement critical_tail_author AI for Yin read this entire saved D/J scope, L379's complete proof, J86's actual fast/direct implementation and retained control structure, and R205's complete scope.
The new author's work is the implementation of this already declared exact-method scope and its author-side check; the critical-level proof remains attributed to the original author, while the reused integer recurrence remains attributed to L379/J86.
No scope, input, parameter, allowance or review relationship changes by this handoff.

The implemented [J87 worker](../computations/programs/Yin_J_G0087/worker.py) uses exact rational interval Horner evaluation for the predeclared19 degree-exhausting roots and512 derivative cells.
It verifies P=z^5 Q(z+z^-1) by the binomial expansion and checks the same original R both through J86's construction and the exact identity R=81-Q^2.
Its CT1--8 control is a separate direct multiplication of the original Laurent symbol, without calling the trace/recurrence construction.
The full finite sum uses the unchanged J86 signed step with all original bounds plus outward integer-division inequalities for every summand.
Only declared scalar overlap values64 and1024 are reused as exact controls; no fresh independent direct verification above8 is claimed.

All geometry products are exact Fraction operations.
Constants and finite-sum terms are enclosed outward at160bits, with neighboring integer-square checks for inverse-density denominators.
The local tail divides its rounded C upper bound by the exact sqrt4096=64; the geometric tail uses the exact rational power of1295/1296 before outward rounding.
The original quadrature alternative remains proved and UNRUN.
Source inspection and syntax/scoped checks before the first mathematical invocation do not supply a numerical result or independent review.

<a id="critical-level-lehmer-native-outcome"></a>
## 9. Completed single author execution and useful finite lower certificate

The revised J87 exact-recurrence calculation completed on 2026-10-11.
The full certificate.json (`mathematics/computations/outputs/Yin_J_G0087/certificate.json`) retains every root/cover/term and the final rational lower bound.
No failed or incomplete mathematical invocation, input extension, parameter change or quadrature alternative was executed.
The source inspection before the run was author-side and does not constitute independent review.

All19 roots were degree-exhaustingly isolated: five for Q, four for Q', and five for each of4Q+1 and4Q-1.
The six endpoint/critical gates certify b=1/4<b_*.
All four covers are disjoint and interior, each encloses exactly its original trace root and both level boundaries, and all512 rational derivative cells certify the required fixed derivative sign and positive weighted lower bound.
The following decimals are readable approximations to the exact rational native values, not substitute certificate bounds:

| Cover | Approximate I_i endpoints | Approximate exact D_i lower value | Sign of Q' |
| --- | --- | --- | --- |
| 1 | [-1.923287600584,-1.835199911629] | 9.175660885721 | positive |
| 2 | [-1.556978535432,-1.389455157635] | 9.717232538137 | negative |
| 3 | [-0.643253616240,-0.531428035452] | 57.843105784786 | positive |
| 4 | [0.890967916754,0.935943451684] | 376.223174972102 | negative |

The native outward C upper value is approximately4.23462008713455; the local and geometric tail upper values are approximately0.0661659388614773 and0.00669358773692324, respectively.
Their complete outward sum is approximately0.0728595265984006.
The exact finite partial-sum enclosure for T4096 has both endpoints approximately0.214851005982969; its small nonzero arithmetic width is retained as rational endpoints in the output.
Combining these exact enclosures through(11) gives the author-side certificate

    m(P) >= 415041559215166780091538487173593981975777634805
            /2923003274661805836407369665432566039311865085952
         = 0.141991479384568075688962... > 7/50.          (12)

The strict comparison with7/50 was checked by exact rational comparison while inspecting the saved output.
It does not come from rounding the displayed decimal.
Every original coefficient, H=9, degree10, all four circle trace roots and the off-circle trace root remain in the certificate.
There is no numerical approximation of the exterior Salem root in(12).

All40,960 signed triangular divisions and40,960 extended-state bounds passed, as did45,067 stored-state bounds,4,097 scalar range bounds,4,096 normalized monotonicity bounds and4,096 outward-term inequalities.
The exact CT controls1--8 and the exact scalar overlaps64/1024 passed.
All4,096 rounded term pairs are retained; their summed width is exactly4096/2^160 before the factor1/2.
All nine declared scalar checkpoints and the final full11-state vector are retained.
The largest triangular numerator/divisor sizes were25,990/16bits, and the final scalar numerator has7,816decimal digits.
These are observed finite bit/output costs, alongside L379's proved general costs; no constant-time bigint claim is made.
The complete certificate retains the necessary rational arrays and final state; incidental serialization size is not a mathematical input.

This outcome demonstrates an effective fully paid finite positive-log lower certificate on one original Salem input.
It does not bound critical values, weighted derivatives or cutoffs uniformly over Salem inputs, does not address every original polynomial, and does not resolve the unrestricted G0001 contract.
At the original pre-adoption handoff, a separate complete review of the new tail proof, the unrun proved quadrature alternative, all arithmetic/code interfaces and this native outcome was still required before fixed adoption.
The reviewer may reuse L379/R205 only at their exact upstream scope; those records do not review this new geometry or tail certificate.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0087](../computations/programs/Yin_J_G0087/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
