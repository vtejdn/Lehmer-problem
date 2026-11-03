---
author: Yin
---

# Fast exact integer log moments through a finite arcsine state

Date:2026-10-11T14:56.
Root coordinating AI for Yin fixes the complete restricted author account below under the continuing G0001 weekly authorization, after separately organized complete review in [the responsible R](../audits/reviews/Yin_R_G0205_v1.md#finite-arcsine-state-whole-finding).
Adopt exactly its stated hypotheses, original costs, failures and source/review limits.
No unrestricted Mahler gap, canonical Claim or Task completion is asserted.

<a id="coupled-method-fixed-scope"></a>
## Fixed scope and preservation

The entire author account follows, with only title depth, navigation and final blank-line normalization.
Allocation-era pending-review statements remain history; the linked fixed R supplies the actual completed review scope.
Proposed or unrun computations remain unrun.
No new allowance, input-uniform conditioning or actual unit/covariance realization is inferred.
Further mathematics uses a distinct draft.

The current complete finite-state theorem and all arithmetic/bit/output costs are retained in [C439](../claims/Yin_C_G0439_v1.md#complete-finite-arcsine-integer-state), adopted after [R642 whole self-review](../audits/reviews/Yin_R_G0642_v1.md#current-finite-arcsine-whole-finding).
The original full account below preserves the actual22:44 author freeze,22:53 review,22:56 retention, both bounded native stages, contributions and then-active status; it creates no current Task/E resumption.
R205 retains its complete separate-implementation evidence at its actual SELF arrangement.

## Complete retained account


## Fast exact positive log moments by a finite integration-by-parts state

Date: 2026-10-11.
Authored by integer_symbol_review AI for Yin under continuing G0001 weekly-only authority.
Root supplied the core derivation below.
This new responsible draft precedes implementation; no program or numerical certificate is asserted by allocation.

## Assigned scope and contribution disclosure

Root supplies the change of variable x=z+z^-1, the integer polynomial R(x)=H^2-P(z)P(z^-1), and the integration-by-parts identity for I[n,k]=integral x^k R(x)^n dmu_arcsine.
The leading coefficient -(j+1+(n+1)d)r_d permits triangular reduction to the d+1 moments k=0,...,d and a finite-state update.
Initial even arcsine moments are central binomial coefficients and odd moments zero.
This core finite-state candidate is root's substantive contribution, not a separately discovered argument here.

Develop and verify the exact reduction/update formulas, all domain/boundary cases and full bit/output costs before code.
Search local and primary attribution for integration-by-parts/creative-telescoping context without invoking an unseen theorem.
Then predeclare a new bounded J comparing independent direct Laurent convolution with the finite-state recurrence on exactly the four J84 inputs through n64.
One additional larger-N Lehmer run is authorized only with a precise predeclared scope, retention and cap.
No huge scan or numerical lower Mahler certificate is authorized or inferred: D24's actual tail constants would require their own fully certified computation.


No new allowance or Task completion is created.

<a id="fast-positive-moment-reuse-and-attribution"></a>
## 1. Responsible inputs and attribution boundary

The complete [D24 positive-moment proof, fixed in L378](Yin_L_G0378_v1.md#positive-log-moment-identity), independently reviewed in [R202](../audits/reviews/Yin_R_G0202_v1.md#positive-log-whole-finding), fixes the intended nu_n, original H, exact constant term and lower-tail boundary.
[L358](Yin_L_G0358_v1.md#single-haar-moment-lower-certificate) and [J84](../computations/programs/Yin_J_G0084/readme.md) retain the four ORIGINAL polynomial controls and their earlier Chebyshev computation; their old Chebyshev moments are not the new positive moments.
The actual J84 main.py CASES table and computation rules were directly read.
The new comparison uses those exact polynomials, not their old numerical output as an oracle.

A bounded local search found related integration-by-parts and arcsine contexts but no matching finite positive-moment state.
A primary context screen directly read Gert Almkvist and Doron Zeilberger, *The method of differentiating under the integral sign*, [author-hosted23-page PDF](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/duis.pdf), introduction and total-derivative elimination on pp.1--4.
The source's own header identifies J.Symbolic Computation10(1990),571--591; no independently reconciled final-page metadata or full-source proof audit is claimed.
It explains constructing integral relations by integration by parts and eliminating total derivatives.
This is classical method context only, now recorded at [AZ90-U001](../audits/literature/AZ90/Yin_U001.md#az90-u001).
No holonomic existence theorem, automatic telescoping algorithm, unseen recurrence-order result or source complexity bound is invoked.
The complete actual boundary/triangular proof follows below.
No historical novelty is claimed.

Root supplied the core integral identity and the d+1-state candidate.
The exact signed coefficient formula, integer divisibility, arithmetic/bit/output accounting and bounded implementation/check design below are developed here.
This author-side work and later author-side program checks need a separate whole noncontributor review.

<a id="arcsine-integer-state-domain"></a>
## 2. Exact integer polynomial and arcsine state

Let P(z)=sum_(j=0)^d a_j z^j be a nonmonomial integer polynomial after stripping a monomial, with actual span d>=1 and a_0 a_d!=0.
Keep H=sum|a_j| and B(z)=P(z)P(z^-1).
Symmetry gives the UNIQUE integer polynomial

    R(x)=H^2-b_0-sum_(l=1)^d b_l C_l(x),
    b_l=sum_(j=0)^(d-l) a_j a_(j+l),
    C_l(z+z^-1)=z^l+z^-l,
    R(z+z^-1)=H^2-B(z),
    deg R=d, r_d=-a_0 a_d!=0.                     (1)

The integer polynomials in(1) satisfy C_0=2,C_1=x and C_(l+1)=x C_l-C_(l-1), which proves their monic integral triangular form and the coefficient-norm bound used below.

Write R=sum_(l=0)^d r_l x^l and W=sum|r_l|.
Its leading coefficient may have either sign.
On x in[-2,2],0<=R(x)<=H^2.
The pushforward of Haar probability under x=2cos theta is

    dmu_A(x)=dx/[pi sqrt(4-x^2)] on(-2,2).

For all integers n,k>=0 define

    I[n,k]=integral_(-2)^2 x^k R(x)^n dmu_A(x),
    I[0,2h]=binom(2h,h), I[0,2h+1]=0,
    nu_n=I[n,0]/H^(2n).                            (2)

The initial formula follows from the constant term of(z+z^-1)^k; this also proves that EVERY I[n,k] is an integer, since x^k R(x)^n has integer coefficients.
Odd states need not be positive.
The useful exact bounds are

    |I[n,k]|<=2^k H^(2n),
    0<=I[n+1,0]<=H^2 I[n,0]<=H^(2n+2).             (3)

These bounds use the actual nonnegative circle function, not coefficientwise positivity.
A monomial P=a z^j instead has R=0 and nu_n=0 for n>=1 and is handled directly, without assigning the zero polynomial a false degree.

<a id="triangular-integration-by-parts-reduction"></a>
## 3. Full triangular reduction and state update

For integers n,j>=0 differentiate x^j sqrt(4-x^2)R(x)^(n+1) on(-2,2).
Its endpoint values tend to zero, and its derivative is a polynomial divided by sqrt(4-x^2), hence integrable.
Integrating first on compact interior intervals and taking endpoint limits gives

    0=integral R(x)^n A_(n,j)(x)dmu_A(x),
    A_(n,j)=sum_(l=0)^d r_l [
       4(j+(n+1)l)x^(j+l-1)
       -(j+1+(n+1)l)x^(j+l+1)].                    (4)

The term at j=l=0 in the first sum is zero and is OMITTED; no moment of exponent-1 is introduced.
No division by R is used, so interior or endpoint zeros and repeated roots of R cause no singularity or missing hypothesis.

For k>d set j=k-d-1>=0 and

    D_(n,j)=[j+1+(n+1)d]r_d!=0.

The coefficient of x^k in(4) is-D_(n,j), and all other exponents are below k.
Therefore

    I[n,k]=D_(n,j)^-1 [
       sum_(l=0)^d 4(j+(n+1)l)r_l I[n,j+l-1]
       -sum_(l=0)^(d-1)(j+1+(n+1)l)r_l I[n,j+l+1]
                              ],                 (5)

again omitting the zero negative-exponent term.
The denominator is signed and nonzero for every n>=0.
The identity determines every higher I[n,k] successively from I[n,0],...,I[n,d].
In particular compute k=d+1,...,2d, corresponding to j=0,...,d-1.
Then

    I[n+1,j]=sum_(l=0)^d r_l I[n,j+l], 0<=j<=d.    (6)

Equations(5)--(6) are the complete rational linear d+1-state recurrence.
Their starting vector is(2).
Correctness by induction follows from the exact integral identity: triangular reduction recovers actual moments at n, then(6) gives actual moments at n+1.
Since all those moments are integers, EACH signed division in(5) is exact.
An integer implementation can and must assert zero remainder; no rational-state denominator need be retained.
This integrality is a consequence of the actual arcsine functional, not of an assumed monic R or positive numerator.

<a id="fast-positive-moment-arithmetic-cost"></a>
## 4. Full arithmetic, bit and retention costs before implementation

Autocorrelation and the integer Chebyshev basis construct(1) in O(d^2) integer arithmetic operations.
At each n, d triangular reductions use O(d) terms each, and d+1 state updates use d+1 terms each.
Thus all moments through N cost O(Nd^2) integer arithmetic operations with O(d) live state integers.
Constructing a dense symbolic transition matrix is unnecessary.
This improves the direct growing-Laurent convolution's O(N^2d^2) arithmetic count, without making bit cost independent of N.

The recurrence temporarily needs k<=2d.
Equation(3) bounds those states by2^(2d)H^(2n).
The elementary ||C_l||_1<=2^(l+1) bound and sum_(l=-d)^d|b_l|<=H^2 give

    W<=2^(d+2)H^2.

For0<=j<d, the absolute numerator of(5) is bounded by

    5(n+2)d W 2^(2d)H^(2n).                        (7)

Its denominator has modulus at most(n+2)d W.
Intermediate state-update sums have the same scale without the n d factor.
Thus all signed states, products, numerator partial sums and divisors through N have bit size

    B_N=O((N+1)log(2H)+d+log(N+2)+log(d+1)).        (8)

Integer exact division is still a paid operation.
With elementary quadratic multiplication/division, a conservative bit-operation upper bound is O(Nd^2 B_N^2); the arithmetic-operation statement does not claim constant-time big integers.
Live mathematical state storage is O(d B_N) bits.
Source polynomial coefficients and output metadata have their own smaller fixed input costs.

Retaining ALL nu_n as unreduced numerator I[n,0] plus the known H requires up to O(N^2 log(2H)) output bits; writing every denominator separately does not avoid that growth.
Retaining every full d+1 state through N has an additional d factor and degree overhead.
A larger run can instead retain named checkpoints and its final complete state, making its narrower retention explicit, while the reproducible program checks all intermediate exact divisions and scalar bounds.
No permanent mathematical hash substitutes for necessary data.

## 5. Bounded execution plan and limits

Before any code run, allocate one responsible new J with exactly the four original J84 coefficient lists and the main proof above.
The first declared stage is n=0,...,64, comparing the new integer recurrence against an INDEPENDENT direct Laurent convolution of Z=H^2-P(z)P(z^-1).
Compare not only CT Z^n but all stored I[n,k],0<=k<=d, by direct constant terms of(z+z^-1)^k Z^n.
Retain exact input coefficients, H, R, all finite states and positive-moment numerators; preserve actual check counts and any failed assertion.
Use standard-library integers only and a30second process cap for this complete four-input comparison.

The responsible [J86](../computations/programs/Yin_J_G0086/readme.md) was allocated with this complete scope before implementation or execution.
At initial implementation its recurrence and independent Laurent reference were author-inspected and unrun; the subsequent exact execution facts are recorded below.
The runtime was read as CPython3.12.14.

Only after that stage passes, execute ONE further recurrence-only Lehmer run through n=1024 with its own30second process cap.
Retain exact scalar checkpoints at n=0,64,128,256,512,1024, the final full d+1-state vector, arithmetic/check counts and runtime facts.
Check all signed exact divisions and the scalar positivity/monotonicity/size assertions at every n, but do not claim independent direct-convolution verification beyond64.
No different input, second larger N, parameter search or retry with a weakened check is included.

No tail modulus b, local radius, derivative S or certified logarithmic enclosure is computed by these stages.
Therefore an exact fast positive moment is NOT a positive finite lower Mahler certificate.
D24's full analytic tail and all original coefficient/degree costs remain required.
The recurrence works for arbitrary nonzero integer inputs at its stated domain, but the executed evidence will cover only the four declared cases and single additional Lehmer depth.
Separate whole mathematical/program review is pending.

<a id="fast-positive-moment-execution-outcome"></a>
## 6. Exact bounded author execution and remaining review

The two predeclared [J86](../computations/programs/Yin_J_G0086/readme.md) stages were actually executed once each, in order, on2026-10-11 before the 2026-10-11T14:42 closeout check, with the current saved programs and exact standard-library integers.
The complete comparison payload (`mathematics/computations/outputs/Yin_J_G0086/comparison.json`) retains all state vectors n0--64 and all four original input/H/R lists.
The independent direct original-Laurent algorithm shares no trace-polynomial or integration-by-parts reduction code.
All1,235 full-state equalities passed, along with960 exact signed divisions and the scalar/Fourier/state bounds.
In particular both signs of r_d occur among the controls.

The first three exact R polynomials in ascending coefficients are[2,1],[8,-2,-1],[16,6,-1].
For the original Lehmer input H=9 and

    R=[72,-24,14,70,9,-64,-23,20,9,-2,-1].

The single additional Lehmer1024 payload (`mathematics/computations/outputs/Yin_J_G0086/lehmer1024.json`) passed all10,240 signed divisions,10,240 extended-state size bounds,11,275 stored-state size bounds,1,025 scalar range bounds and1,024 normalized monotonicity bounds.
Its n64 overlap matches the independently checked data.
It retains scalar checkpoints0,64,128,256,512,1024 and the final full11-state vector, with original positive moment denominator9^(2n).
No independent direct-convolution agreement beyond64 is asserted.
The recorded maximum numerator/divisor lengths were6,513/14bits.
Both worker/supervisor elapsed times were below one second on these runs, with actual values and separate30second hard caps in J86.
No further input/depth or failed/retried mathematical run occurred.

The mathematical benefit is the proved reduction of the arithmetic recurrence from quadratic to linear dependence on N at fixed d, with full bit/output costs in(7)--(8), and a bounded actual implementation discriminator.
The exact moments do not establish tail constants or a positive Mahler lower certificate.
No old J84 output, root approximation, floating arithmetic or huge scan supplies hidden acceptance.
Root's core derivation is disclosed; these checks are author-side and whole separate mathematical/program scrutiny remains pending.

## 7. Author self-check and readiness

Self-check reconstructed the actual symmetric Laurent-to-integer trace conversion and nonzero signed r_d; Haar-to-arcsine normalization and central binomial initial values; all-moment integrality and odd-state signs; endpoint integration-by-parts limits and absence of division by R; every coefficient/index in(4)--(6), omitted zero negative-power term, nonzero signed denominator and exact division; triangular degree bounds and the d+1 state; all arithmetic, numerator/divisor bit and live/output storage costs; original four J84 arrays and distinct old Chebyshev observable; predeclared J scope before code; independent Laurent full-state comparison, both denominator signs, all native check counts and the single guarded larger run; and the absence of a tail/log/Mahler certificate.
The complete primary source-context boundary remains exactly Section1; no unseen telescoping theorem or source algorithm is used.

Root supplied the integral identity and finite-state core; the completed exact formulas, integrality/cost derivation and bounded implementation/checks are by integer_symbol_review AI for Yin.
The full proof is ready for the separately assigned whole noncontributor mathematical/program review.
G0001 remains active and unrestrictedly unresolved.

<a id="fast-positive-moment-entire-author-freeze"></a>
## Entire author freeze

2026-10-11T14:44.
The complete responsible author body, contribution/reuse/source context and Sections1--7, equations(1)--(8), exact signed integer state recurrence, boundary/degree/integrality proof, full arithmetic/bit/output costs and bounded J86 execution account are frozen.
The complete current J86 programs, declared four-input comparison through64 and single additional Lehmer1024 output are ready for separate whole mathematical/program review.
Author self-check and scoped D/J material check passed.
Source-context canonical locator maintenance remains coordinator work and changes no mathematics.
No tail/logarithmic/Mahler lower certificate, native scan or parameter domain beyond the declared two stages was used.

G0001 remains active and unresolved.
