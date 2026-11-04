---
author: Yin
---
# Correlated capacity arrays beyond multiplicative profiles

Date: 2026-10-15.
Human author Yin.
Continuing algebraic exploration under the resumed G0001 goal.

## Responsible question

The author-complete first-round product theorem is now retained in C104 for independent review.
Investigate the genuinely correlated weak L1 fractional-lcm moment or direct positive-density localization.
Seek an exact compression principle, a bounded-cost representation genuinely forced by density, or a sharp counterfamily satisfying the relevant hypotheses.
Deliberate departures from product/dyadic models are permitted.
The earlier product theorem, C99, C96/C98 and L396 supply exact starting boundaries; do not silently use C104 as independently accepted before its actual review.
Preserve full reasoning and useful failures here.
Programs requiring retention need a coordinated J group.

## Current investigation

2026-10-15.
The delegated g_bridge_audit AI is the author of this continuation.
The author derives a general finite extremal reduction by extending C91's endpoint/downset method to the fractional-moment normalization.
Root subsequently supplied the full-divisor-minus-maximum formula and the instruction to compare it against the INFINITE product constant with its tail paid; that is a substantive contribution to the counterexample inquiry below, not independent review.
The author had separately identified the maximal-order first-variation test.
The fixed C104 product theorem remains at its own actual review status.

<a id="correlated-fractional-reuse"></a>
## Reuse and source scope

Read [C91's complete short-pair downset argument](Yin_C_G0091_v1.md#short-pair-finite-downset-reduction), [C96's actual finite moment and tail model](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof), [C99's atom comparison](Yin_C_G0099_v1.md#squarefree-density-atom-proof), L396 and the author's complete product proof now preserved in [C104](Yin_C_G0104_v1.md#product-fractional-moment-argument).
C91 ALREADY proves full-capacity divisor-downset extremality for a different short-pair numerator divided by W.
The exact new question has the full fractional kernel and denominator W^(2-s); its coordinate derivative needs the additional bound K(a,b)<=K(a,a).
No new general rounding or compression principle is claimed.

The primary-source GCD/capacity screen and its exact non-adoption limits were completed in the preceding C104 author argument.
They are reused here.
No checked source from that screen supplied this fractional objective or a universal constant.
The finite derivative algebra below and the alternating-series constant enclosures are proved directly.
There is no imported approximation theorem, SDP or statistical premise.
The classical identity between the convergent Euler product and zeta series is rederived below at the exact exponents used; neither an unchecked zeta value nor a numerical library constant is an input.

<a id="correlated-fractional-statement"></a>
## General extremal statement

Fix0<s<1, write t=2-s, and let B be a finite nonempty divisor-closed set of positive integers.
For0<=w_a<=phi(a), a in B, define

    W=sum_a w_a,
    E_s(w)=sum_(a,b in B)w_a w_b/lcm(a,b)^s,
    R_s(w)=E_s(w)/W^t for W>0, and R_s(0)=0.              (1)

Then

    max_(0<=w_a<=phi(a)) R_s(w)
       =max_(nonempty divisor ideals D subset B)
          [sum_(a,b in D)phi(a)phi(b)/lcm(a,b)^s]
                            /[sum_(a in D)phi(a)]^t.     (2)

Every ideal on the right uses FULL integer totient capacities.
Thus a uniform constant for the weak fractional-moment inequality on all finite REAL or INTEGER capacities exists if and only if it bounds all such full-capacity finite divisor ideals.
This is a general correlated extremal reduction, not a proof of a uniform bound.
The ideal need not be a complete numerical-threshold set or the full divisor set of one integer.

**Certified obstruction to the sharp product constant, after the declared run.**
At s=1/2, let Q be the product of ALL primes<=73 and let N=Q^e for ANY integer e>=8.
Set w_a=phi(a) on EVERY proper divisor of N and0 otherwise.
The complete proof and exact native certificate below give

    E_(1/2)(w)/W^(3/2)>7943/5000,
    K_(1/2)<7941/5000,
    E_(1/2)(w)/W^(3/2)-K_(1/2)>1/2500.                  (2a)

Thus the sharp product-profile constant does NOT extend to arbitrary correlated capacities, even full integer divisor ideals.
The family has fixed positive triple density at X=N/2 and captures more than half its mass there; it is NOT a counterexample to fixed-positive-density capture or to existence of a larger universal weak constant.
No actual polynomial lift or near-one family is asserted.

<a id="correlated-fractional-argument"></a>
<a id="correlated-fractional-extremal-proof"></a>
## 1. Exact fractional endpoint and divisor-ideal reduction

Since lcm(a,b)>=1, E_s(w)<=W^2 and R_s(w)<=W^s.
Hence the extension by0 is continuous at the zero vector.
The compact capacity box has a maximum, and that maximum is positive because1 belongs to B and w_1=1 is available.

Hold all but one coordinate w_a=x fixed.
Let

    k=a^-s, D=sum_(b!=a)w_b,
    b=sum_(c!=a) w_c/lcm(a,c)^s,
    c=sum_(i,j!=a)w_iw_j/lcm(i,j)^s.

Letters b,c here are scalar quantities in this one-coordinate calculation.
The objective is

    f(x)=(k x^2+2b x+c)/(x+D)^t.                         (3)

If D=0, it equals k x^s and increases, with its prescribed continuous value0 at x=0.
If D>0, the derivative has the sign of

    Q(x)=s k x^2+2[kD-(1-s)b]x+2bD-tc.                 (4)

The exact inequality lcm(a,c)>=a gives b<=kD.
Consequently

    Q'(x)=2s kx+2[kD-(1-s)b]>=2s k(x+D)>0.             (5)

Thus f is monotone or first decreases and then increases; it has no interior maximum.
Each coordinate can be replaced by0 or its full phi(a) without lowering a global maximum.
After finitely many such replacements a full-capacity maximizing subset D0 remains.

Let W0,E0 be its mass and energy.
If a in D0 has an absent divisor h in B, define its full potential

    V_a=sum_(c in D0)phi(c)/lcm(a,c)^s.

At the full upper endpoint w_a=phi(a), maximality against a small downward change implies

    2V_a W0-tE0>=0.                                    (6)

Since h divides a, lcm(h,c) divides lcm(a,c), so V_h>=V_a.
The derivative when the absent coordinate w_h increases from0 is therefore nonnegative.
Its derivative numerator is strictly increasing by(5), with D=W0>0, so EVERY sufficiently small positive allowed increase makes the objective strictly larger, including when the initial derivative is zero.
This contradicts maximality.
No divisor can be absent, proving(2).

For an arbitrary finite capacity array, take B to be its divisor closure, or the full interval up to its largest order, and apply(2).
Conversely every full ideal is itself an admissible integer array.
This proves the stated real/integer equivalence.
The optimization does NOT preserve total mass, triple density, Frobenius multiplicities or actual polynomial realization of its starting array.
It is only an exact universal-energy reduction; no replacement of actual root counts in a norm certificate is authorized by it.

<a id="maximal-order-deletion-formula"></a>
## 2. A genuinely correlated candidate and its exact ratio

Fix s and t as above, and take the full divisor array w_a=phi(a) for a|N.
Write

    c_N=phi(N)/N,
    R_N=E_s(full divisors of N)/N^t
       =product_(p^e||N) K_(p,e),                        (7)

using C104's EXACT finite prime-chain factors.
Its total mass is N.
At its maximal order N the potential is

    sum_(a|N)phi(a)/lcm(a,N)^s=N^(1-s).

Delete ONLY the maximal order N, retaining full phi capacities at every proper divisor.
The remaining mass is N-phi(N), and its exact normalized energy is

    R_N^-=[R_N-2c_N+c_N^2]/(1-c_N)^t.                    (8)

The two orientations and diagonal correction are all present.
Formula(8) is root's supplied finite-deletion candidate, independently reconstructed by the author here.
It is not inferred solely from a first derivative.
If N has at least two distinct prime factors, the resulting support is a divisor ideal but is NOT a Cartesian product of its prime-exponent supports: every local maximal exponent still occurs in a proper divisor, while their simultaneous maximum N is absent.
Thus this is a correlated test beyond C104's product class.

The first-variation calculation only shows a local improvement over R_N when tR_N>2; it does NOT show R_N^->K_s, where K_s is the larger infinite product.
That inference would omit the finite-prime and finite-exponent costs.
The declared computation below instead compares strict rational enclosures of both complete quantities.
Even if it proves R_N^->K_s, it refutes only the extension of the sharp PRODUCT constant to arbitrary capacity arrays.
It neither refutes a possibly larger universal weak-moment constant nor constructs fixed positive triple density or a near-one polynomial.

<a id="half-moment-exact-constant-certificate"></a>
## 3. Exact analytic reduction for the declared half-moment certificate

For the finite test fix s=1/2, t=3/2, and exponent e=8.
For each prime prefix P consisting of all primes up to one of the primes<=97, define

    Q=product_(p in P)p,  N=Q^8,
    c=product_(p in P)(1-1/p),
    k_p=(1-p^-2)/(1-p^(-3/2)),
    R_N=product_(p in P)[k_p+(1-k_p)p^-12].               (9)

Every listed N is a finite explicit integer; (9) avoids enumerating its potentially enormous divisor set.
Equation(8) gives its proper-divisor ideal ratio.
All prime prefixes in the declared range will be retained, including those whose intervals fail to separate from K_(1/2).

The infinite product satisfies

    K_(1/2)=zeta(3/2)/zeta(2).                           (10)

To justify the only infinite identity needed, for any r>1 the finite geometric expansion of product_(p<=Y)(1-p^-r)^(-1) equals the sum of n^-r over integers whose prime factors are<=Y.
These sums increase to sum_(n>=1)n^-r, because each integer is eventually included and the full series converges by the integral test.
Taking the ratio of the two positive convergent products at r3/2 and r2 yields(10).

For r>1 absolute convergence permits separating the even terms, giving

    eta(r):=sum_(n>=1)(-1)^(n-1)n^-r
           =(1-2^(1-r))zeta(r).                         (11)

At an EVEN positive integer M, monotonic decrease of n^-r and adjacent-term pairing give the exact signed bounds

    S_M(r)<=eta(r)<=S_M(r)+(M+1)^-r,
    S_M(r)=sum_(n=1)^M(-1)^(n-1)n^-r.                    (12)

The inequalities follow directly by grouping the remainder into consecutive positive differences for the lower bound, or subtracting such pairs after its first term for the upper bound.
All remainder terms converge and have the indicated order.
Thus no unproved tail formula or asymptotic error is used.

The native program uses M=512 AND1024, precision B=96 and scale S=2^B.
For a positive rational x=A/D, set

    j=isqrt(floor(A S^2/D)).

Then j^2 D<=A S^2<(j+1)^2 D proves

    j/S<=sqrt(x)<(j+1)/S.                               (13)

For n^-3/2=1/(n sqrt(n)), invert these positive bounds and then round outwards onto denominator S.
For n^-2 use direct rational integer division and outward rounding.
Accumulating the signs with the appropriate interval endpoints gives an enclosure of S_M; add the upper bound for the first omitted term for(12).
Divide the r3/2 interval by the positive interval for1-1/sqrt2 and multiply the r2 interval by2.
Finally divide the positive zeta intervals to enclose(10).
The finite root bounds in(9), the exact rational c and the denominator (1-c)sqrt(1-c) in(8) use the SAME method(13), retaining their full outward interval operations.

A declared row is certified only if its rational LOWER bound for R_N^- exceeds the rational UPPER bound for K_(1/2), by exact integer cross multiplication.
Decimal displays have no role in that test.
Positivity of every divisor and interval denominator is checked before division.
No numerical root approximation, optimized support search or unlisted prime is used.

<a id="half-moment-native-declaration"></a>
## 4. Declared native scope, before execution

The allocated [J94](../computations/programs/Yin_J_G0094/readme.md) owns the author program and native output.
Root explicitly authorized this refined finite scope before implementation: all prime prefixes ending at primes<=97, e8, s1/2, both even eta truncations512/1024,96-bit outward square-root/term bounds, and a180-second aggregate author-run ceiling.
The abandoned broader possibilities of enumerating every ideal in a27-order ambient or using up to one million zeta terms will NOT be executed by this declaration.
The program will preserve every candidate row, all exact constant enclosures, finite factor/root intermediates, full integer N/phi(N)/remaining mass and the entire signed finite-sum term data.
A separate noncontributing verifier may later use its own program; no such verification is claimed in advance.

Before the declared run, the program will be source-inspected and syntax parsed without running mathematical code.
A single supervised author invocation will then either publish its complete successful certificate or retain/report its failure.
No altered parameters, extra candidate, solver retry or extended run is permitted silently.
At this point the analytic implications above are author deductions; no numerical separation or native mathematical result has yet been obtained.

<a id="correlated-half-moment-native-outcome"></a>
## 5. Complete native outcome and a growing-mass capacity family

The declared author calculation completed the fixed finite scope on 2026-10-15, with no failed/incomplete invocation, changed parameter or additional mathematical run.
The certificate (`mathematics/computations/outputs/Yin_J_G0094/certificate.json`) retains every mathematical intermediate and candidate.
The [J account](../computations/programs/Yin_J_G0094/readme.md#results-and-limits) states the actual finite outcome and limitations.
These are author checks; the historical author-stage account does not itself assert independent review.

All25 prime-prefix rows and all1025 signed-series term enclosures were retained.
Every integer-square, exact rational positivity, phi(N) integrality and full N^(3/2) scaling check passed.
The eta truncation1024 certifies a strict separation at prefix endpoints73,79,83,89,97.
The first certified endpoint is73; it also separates using the looser512-term bound.
Earlier rows, including71, remain in the same native output as nonseparating candidates; they are not deleted or described as exact failures of the candidate inequality.

Readable approximations to the exact outward intervals are

    1.58810120881024727455 < K_(1/2) < 1.58816629610300950278,
    R_(Q^8)^- = 1.58867663837140234074...  (Q=product_(p<=73)p),
    certified lower difference >0.00051034226839283796.

The displayed decimal precision of the candidate hides its much smaller NONZERO interval width; the native rational endpoints are the certificate.
By reading those saved rational endpoints and comparing integers, the author checked the simpler exact claims

    R_(Q^8)^->7943/5000,  K_(1/2)<7941/5000.              (14)

This proves the strict gap1/2500 in(2a) without using a rounded decimal as a bound.
No new moment evaluation or parameter run was used for this saved-output comparison.
The certificate is802953bytes and retains every required finite factor, root bound, full integer N/phi(N)/W and unscaled energy enclosure; no separate compressed digest is used as mathematical evidence.

For this FIXED finite prime pool, keep Q and let the common exponent e grow through integers>=8.
The product constant R_(Q^e)=product_(p|Q)K_(p,e) increases with e by C104's exact formula K_(p,e)=K_p+(1-K_p)p^(-3e/2).
The ratio c=phi(Q^e)/Q^e=product_(p|Q)(1-1/p) is unchanged.
Hence(8) increases with e, and the e8 certificate proves(2a) for EVERY e>=8.
This creates an explicit infinite family of INTEGER correlated capacity arrays with W tending to infinity.
Their ratios have a finite limit given by(8) with R_N replaced by the finite-pool product; no divergent ratio or absence of every universal bound follows.

<a id="proper-divisor-positive-density-control"></a>
## 6. The same arrays have positive density and positive capture

The exact family permits a useful check against the actual target.
Since2 divides N, its largest proper divisor is N/2.
Choose the integer window X=N/2.
EVERY selected order lies in that window.
For any n<=X, all divisors of gcd(n,N) are proper divisors of N and are selected, so

    h(n)=sum_(a|n, a proper divisor of N)phi(a)=gcd(n,N).

Consequently H_X=N/2, attained at the ACTUAL integer n=N/2.
With c=phi(N)/N,

    W=N(1-c),  c<=1/2,  X<=W,
    H_X/W=1/[2(1-c)]>1/2.                               (15)

Every triple of divisors of N/2 is compatible and has total ordered weight(N/2)^3.
Thus the same full integer array has

    T_X/W^3 >=1/[8(1-c)^3]>=1/8.                         (16)

Alternatively, the complete ordered triple count gives the exact value

    T_X=N^3[1-product_(p|N)(1-p^-3)].                    (17)

To check(17) locally, the total mass for three divisor labels in0,...,e at p is p^(3e); those with maximum exponent<e have mass p^(3e-3), so maximum exponent e contributes p^(3e)(1-p^-3).
Product expansion counts every triple with lcm EXACTLY N.
Subtract this from the full total N^3.
A triple with lcm proper automatically has each label proper, and every proper divisor of this even N is<=N/2.
Hence this subtraction is precisely T_X for the selected proper-divisor array.
All diagonals and repetitions are retained.

Equations(15)--(17) show why the certified counterexample to the SHARP PRODUCT CONSTANT is no threat to the desired nonlinear positive-density capture: the family already has a single time catching more than half the mass.
It has no local norm depths, designated good prime or proven irreducible-unit realization; integer capacities alone do not supply those additional structures.
In particular W is a combinatorial mass here, not an asserted original polynomial degree.

<a id="correlated-fractional-remaining-scope"></a>
## 7. What the general continuation now requires

The universal weak fractional inequality is now reduced exactly to correlated FULL divisor ideals.
The product constant is ruled out on an explicit such family, with its entire infinite-product normalization paid.
These are distinct findings: the second does not undo the first or decide whether a larger constant C_s exists.
C104's optimality statement remains correct on its stated product class.

An argument that rounds arbitrary capacities to full weights and then treats their support as a rectangular prime-exponent product would be invalid.
The true extremal support is only a divisor ideal, and the proper-divisor witness proves that this distinction affects the best constant.
A successful next bound must control correlated ideals themselves, or prove a useful localization genuinely forced by positive density.
A new negative construction must make E_s/W^(2-s) UNBOUNDED to refute every constant, or retain fixed positive density while H_X/W tends to0 to refute the separate capture target.
No such construction is present here.

The author checked the continuous extension at zero, D=0 coordinate case, the exact b<=kD inequality and derivative sign, all divisor-closure and one-sided endpoint guards, the change of normalization from C91, the finite deletion diagonal/sign, the infinite Euler-product identity, the signed eta remainder, every rational sqrt/reciprocal/denominator direction, the code/output interface and full declared finite scope, the fixed-prime-pool e extension, and the exact compatible-triple count.
These are contributing author checks.
The root's supplied deletion candidate and tail-discrimination direction are credited above.
The native program has not been independently reproduced, and this entire new argument has not yet received a noncontributing whole review.

<a id="correlated-fractional-entire-author-freeze"></a>
## Entire bounded-round author freeze

2026-10-14T19:37.
Freeze this ENTIRE artifact and J94's author source/certificate/execution: exact general fractional extremal reduction, genuine correlated proper-divisor family, all original formulas and candidate boundaries, the before-run declaration and complete single-run outcome, strict rational separation from the infinite product constant, all exponent extensions and density sanity checks, source/contribution accounts and unresolved general/actual-near-one scope.
The statement and complete proof anchors permit direct fixed retention.
A separately assigned reviewer must inspect the entire mathematical chain and independently reproduce the declared native evidence at its actual scope.
No Claim status, Task completion or independent acceptance is claimed by this author freeze.

## Fixed organization

The entire author original above is retained at its actual freeze, including mathematical arguments, native declaration and outcome, contributor accounts and limitations.
The root contributed the deletion candidate and is not an independent reviewer.
This actual fixed artifact and the declared J94 evidence await a separately organized noncontributor whole review and independent native verification.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:39 |
| status | open |
| reason | Retain the complete fractional divisor-ideal reduction and certified obstruction to the sharp product constant for separate whole and native review. Neither a larger uniform bound nor unrestricted positive-density capture or the original Mahler gap is decided. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#correlated-fractional-statement) | General real/integer extremal reduction and complete proper-divisor counterfamily at their stated scopes. |
| argument | [Entire argument](#correlated-fractional-argument) | Sections1--7, exact analytic and integer interval reductions, exponent extension and density control. |
| dependency | [Original downset method](Yin_C_G0091_v1.md#short-pair-finite-downset-reduction) | Earlier endpoint/downset input whose changed fractional normalization is explicitly rederived. |
| dependency | [Exact product constants](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite and infinite product formulas and monotonicity, retained only at their proved product scope. |
| support | [Native finite certificate](../computations/programs/Yin_J_G0094/readme.md) | Exact author source, all declared parameters, rational certificate and complete actual execution; independent native check pending. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:51 |
| status | proved |
| reason | Adopt [R797 original correlated-fractional](../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding)'s complete independent review and independent J94 native reproduction. The full-capacity divisor-ideal extremal reduction and the strict correlated obstruction to the sharp product constant, including every e>=8 extension and exact positive-density control, are established. Existence of a larger universal constant, general density capture and the unrestricted Mahler gap remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#correlated-fractional-statement) | General real/integer extremal reduction and complete proper-divisor counterfamily at their stated scopes. |
| argument | [Entire argument](#correlated-fractional-argument) | Sections1--7, exact analytic and integer interval reductions, exponent extension and density control. |
| dependency | [Original downset method](Yin_C_G0091_v1.md#short-pair-finite-downset-reduction) | Earlier endpoint/downset input whose changed fractional normalization is explicitly rederived. |
| dependency | [Exact product constants](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite and infinite product formulas and monotonicity, retained only at their proved product scope. |
| support | [Native finite certificate](../computations/programs/Yin_J_G0094/readme.md) | Exact author source, all declared parameters, rational certificate and complete actual execution; independent native check pending. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0797_v1.md#correlated-fractional-actual-whole-independent-finding) | Entire actual statement/argument, all direct inputs, exact declared native evidence and independent reproduction, every exponent extension and scope limit. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:39 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. The full-ideal extremal reduction, exact correlated obstruction, every e>=8 extension and all density/capture identities are supported; a fresh inline exact reconstruction checked the available complete J94 certificate at its original 25-prefix, 96-bit, e8 and eta512/1024 scope. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. The support row retains its author-stage pending wording as historical scope; the present independent native reconstruction is supplied by the new selected finding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#correlated-fractional-statement) | General real/integer extremal reduction and complete proper-divisor counterfamily at their stated scopes. |
| argument | [Entire argument](#correlated-fractional-argument) | Sections1--7, exact analytic and integer interval reductions, exponent extension and density control. |
| dependency | [Original downset method](Yin_C_G0091_v1.md#short-pair-finite-downset-reduction) | Earlier endpoint/downset input whose changed fractional normalization is explicitly rederived. |
| dependency | [Exact product constants](Yin_C_G0104_v1.md#product-fractional-moment-argument) | Finite and infinite product formulas and monotonicity, retained only at their proved product scope. |
| support | [Native finite certificate](../computations/programs/Yin_J_G0094/readme.md) | Exact author source, all declared parameters, rational certificate and complete actual execution; independent native check pending. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0105-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. Includes the fresh exact reconstruction of the complete available J94 finite certificate and original parameter/input bindings, not a rerun of the old verifier. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0094](../computations/programs/Yin_J_G0094/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
