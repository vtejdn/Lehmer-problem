---
author: Yin
---

# Arithmetic constraints on near-extremal fractional lcm slices

Date: 2026-10-14T20:34.
Human author Yin.
The delegated strategy_critique AI authors this G0001 continuation.
Root assigned an independent positive general fractional-lcm or near-global arithmetic inverse inquiry, without supplying a proof step.
The averaged-pair/density and Toeplitz/integer lines belong to other agents.

## Responsible question

Can full-capacity divisor-ideal extremality and the strict potential inequalities in C111 yield a usable uniform fractional-lcm estimate, or a genuine arithmetic slice constraint that pays the first-order loss in C108's prime recursion?
The inquiry may change method if a better mechanism emerges.
Generic PSD inequalities and the N=2310 finite outcome are not universal evidence.
Repetition of C105/C108/C111 is not a new result.
Preserve a complete new theorem if obtained, or the precise unclosed implication and useful failures.

## Initial reuse scope

The responsible inputs are C105's finite extremal reduction, C108 v2's exact slice factor and excluded-prime deficit, and C111's strict all-optimizer characterization, with their independent adoption scopes.
C104's finite Gram and product formulas supply exact kernel interfaces.
C112's uniform-base row obstruction rules out another whole-row enlargement but neither disproves a uniform fractional constant nor supplies a density counterexample.
The current author previously independently reviewed C105/C108/C111/C112 and authored the distinct C106/C109 inputs; those relationships do not predetermine the outcome here.

No native mathematical program is declared.
Continuing mathematics will be written directly in this responsible material.
A necessary computation would require its own coordinated J and pre-execution scope.
No source-global edits, new fixed Claim or research decision are authorized by this draft allocation alone.

## Current investigation

No new result is asserted at allocation.
Begin with a bounded reuse/source screen, then derive the exact arithmetic obligations in this material before drawing a conclusion.

<a id="rounding-reuse-and-failed-first-approaches"></a>
## Reuse screen and preserved preliminary failures

The local screen reread C104's finite Gram/product theorem, C105's endpoint reduction, C108 v2's exact relaxed factor and actual local saturation, C111's complete optimizer proof, and L396's refuted strong-functional estimate.
Exact searches for potential, near-extremal, prime exclusion and divisibility-chain estimates did not find the simultaneous mass/nesting/near-correlation reduction developed below.
A bounded primary-source web screen for totient-weighted lcm inequalities and divisor-closed gcd sums located related GCD-sum and divisibility-poset literature, but no exact imported theorem supplying this reduction.
Search results from secondary aggregators were not used as mathematical inputs.
No novelty or exhaustive search claim is made.
All random variables below have finitely many outcomes; their expectation, second-moment and union-bound calculations are supplied directly.

Two preliminary lines are retained with their limitations.

1. For a positive optimizer with ratio R on a finite ambient, C111 gives 2WV_a>tE at selected a, while V_a<=W/a^s.
   Hence a<(2/(tR))^(1/s) W.
   This controls selected orders in terms of the optimizer value, but does not itself bound that value.
   The exact averaged test below explains why no cancellation was obtained merely from the first-variation averages.
2. On ANY divisibility chain a1|...|an with arbitrary0<=w_i<=phi(a_i), put M_j=sum_(i<=j)w_i.
   Then M_j<=sum_(d|a_j)phi(d)=a_j and

       E_s=sum_j (M_j^2-M_(j-1)^2)/a_j^s
           <=sum_j (M_j^2-M_(j-1)^2)/M_j^s
           <=integral_0^W 2x^(1-s) dx=2W^t/t.

   Zero increments are omitted.
   For an explicit disjoint partition into L chains of masses W_j, C104's finite Gram inequality consequently gives

       E_s<= (2/t)(sum_j W_j^(t/2))^2<=(2/t)L^s W^t.

   This is a valid varying-prime chain estimate, but not a new unrestricted capture mechanism.
   If all labels are at most X, each chain is already captured by its maximal label at a time<=X.
   With positive triple density, restricting to labels<=X leaves mass at least delta^(1/3)W, and the same elementary chain cover captures at least delta^(1/3)W/L.
   Thus bounded L would already be an explicit additional cover hypothesis, not near-one coverage.
   No Dilworth theorem or new source input is needed for this explicitly supplied-chain statement, and no inferred bounded chain count is claimed.

The useful new direction is instead simultaneous near-extremal compression with an error paid uniformly in the ambient size.

For the preliminary two-slice test put q_p=p-1 and Theta=tE/(2W) for the WHOLE array.
C111's selected/absent conditions, summed against base phi weights, imply the necessary inequalities

    E0+q_p p^-s E01>Theta V0,
    p^-s(E01+q_p E1)>Theta V1,
    p^-s[E0-E01+q_p(E01-E1)]<=Theta(V0-V1).

The third applies when all missing p-times-base coordinates are available in the rectangular ambient.
Insert the formal C108 data V0=1,V1=p^-2,E0=C0,E1=C0 p^-2t,E01=C0 p^-t, where C0 is the BASE slice reference constant, not a bound on the whole p-extended array.
Then Theta/C0 tends to t/2.
The first left side divided by C0 tends to1; the second left side divided by C0 V1 also tends to1; the third left side divided by C0(V0-V1) tends to0.
Since t/2<1, all three averaged requirements hold for sufficiently large p.
This supplies only a failed scalar discriminator, not a realization by actual globally extremal slices.
The new proof below does not use this formal model.

<a id="statement"></a>
## Statement: simultaneous full-ideal reduction with uniform errors

Fix0<s<1 and put t=2-s.
Let B be a NONEMPTY finite divisor-closed set of positive integers.
For real arrays on B define

    E_s(u,v)=sum_(a,b in B)u_a v_b/lcm(a,b)^s,
    E_s(u)=E_s(u,u), W(u)=sum_a u_a.

Let C>0 be ANY valid constant on its capacity box:

    E_s(u)<=C W(u)^t for every0<=u_a<=phi(a),             (1)

with the zero array interpreted continuously.
In particular the exact finite maximum from C105 is allowed; no uniform bound over different B is presumed.

The theorem therefore does not depend on existence of the unresolved universal constant.
Each finite ambient has such an intrinsic C_B: E_s(u)<=W(u)^2 makes the quotient at most W(u)^s near zero, so it extends continuously to the compact capacity box; its maximum is positive because B contains1 and u_1=1 is feasible.

Suppose0<epsilon<=s/4096 and two nonzero nested arrays satisfy

    0<=w1<=w0<=phi coordinatewise,
    E_s(wi)>=(1-epsilon)C W_i^t, W_i=W(wi), i=0,1.      (2)

Write rho=E_s(w0,w1)/sqrt(E_s(w0)E_s(w1)), and set

    q=1-3s/4,
    A_e=4epsilon/s+4epsilon^2/s^2,
    B_e=(4/s-3)epsilon+4q epsilon^2/s^2,
    eta=sqrt(8A_e), d=sqrt(8B_e/(1-epsilon)).            (3)

Then eta,d<1/4.
There exist NONEMPTY nested FULL-totient divisor ideals D1 subset D0 subset B, with v_i(a)=phi(a)1_(a in D_i), such that

    (1-eta)W_i<=W(v_i)<=(1+eta)W_i,                    (4)
    E_s(v_i)/W(v_i)^t
       >=(1-epsilon) C (1-d)^2/(1+eta)^t,             (5)
    rho(v0,v1)
       >=max(0,[(1-epsilon)rho-2d-d^2]/(1+d)^2).       (6)

In particular the mass ratio lies between (1-eta)/(1+eta) and its reciprocal times W1/W0.
All errors are O_s(sqrt(epsilon)) and have NO dependence on the number of labels, maximal order, prime support, exponents, ratio W1/W0, or numerical size of C.
The constants and the small-epsilon range are deliberately safe.

The proof supplies a finite simultaneous mass-preserving arithmetic compression, followed by common-threshold Bernoulli rounding and a direct positive-probability selection.
It does not assert an efficient algorithm or exact preservation of masses after endpoint rounding.
It reduces the asymptotic near-global nested inverse question to FULL integer divisor ideals at an explicit cost; it does not prove that inverse, the universal weak bound, or actual near-one coverage.

<a id="argument"></a>
## Complete argument

<a id="simultaneous-mass-preserving-divisor-compression"></a>
### 1. A finite arithmetic compression preserving nesting and both masses

For a proper divisor d of a, replace the two coordinates (u_d,u_a) by

    (min(phi(d),u_d+u_a), max(0,u_d+u_a-phi(d))).        (7)

All other coordinates remain fixed.
This moves h=min(u_a,phi(d)-u_d)>=0 units from a to d.
It preserves the mass and feasibility: the new a-coordinate is at most its former value, and the new d-coordinate stays within its own capacity.
Both new coordinates are nondecreasing functions of the sum u_d+u_a.
Therefore applying the SAME operation to two coordinatewise nested arrays preserves their nesting, although their moved amounts may differ.

For every b, lcm(d,b) divides lcm(a,b), so K(d,b)>=K(a,b) for K(a,b)=lcm(a,b)^(-s).
Thus moving nonnegative mass down from a to d increases its bilinear energy with ANY fixed nonnegative other array.
Applying first to one array and then to the other proves that a simultaneous compression does not decrease either self-energy or the cross energy.
For self-energy one can also verify directly, with V_c=sum_b u_b K(c,b),

    E_s(u+h(e_d-e_a))-E_s(u)
      =2h(V_d-V_a)+h^2(d^-s-a^-s)>=0.                 (8)

The last coefficient is positive for d<a.
This is an arithmetic row-monotonicity argument, not a claim about an arbitrary PSD kernel.

Use the following FINITE schedule on both arrays.
Process each d in B in increasing numerical order.
For this d, process every proper multiple a in B once, in increasing order, using(7).
After its block, either coordinate d is full or all its proper multiples have zero weight.
Later blocks never decrease coordinate d.
If d remains nonfull, a later block cannot recreate a positive proper multiple c of d: a transfer into c would have to come from a proper multiple of c, hence from another proper multiple of d, all of which were already zero.
This invariant applies separately to both arrays.

The final arrays x1<=x0 therefore have the same original masses W_i and satisfy

    x_i(a)>0, d|a, d<a => x_i(d)=phi(d).              (9)

Every positive label has ALL its proper divisors full.
In particular positive support is a divisor ideal, and any partial capacities occur only at its maximal labels.
This property is stronger than support closure but does not claim that every maximal label is full before rounding.

By(1), (2) and energy monotonicity,

    (1-epsilon)C W_i^t<=E_s(x_i)<=C W_i^t.

The cross energy also did not decrease.
Each old-to-new self-energy ratio is at least1-epsilon, so

    rho(x0,x1)>=(1-epsilon)rho(w0,w1).                (10)

This is the point where near-globality pays for the possible denominator increase in correlation.
Compression alone does NOT assert that normalized correlation is monotone.

<a id="uniform-near-extremal-order-tail"></a>
### 2. A uniform order-tail estimate at near extremality

This step applies to ANY nonnegative feasible array x of mass W>0 satisfying E_s(x)>=(1-epsilon)CW^t; downward saturation is not needed.
Define

    Z=W(qC)^(-1/s),
    x_low=x 1_(a<=Z), x_high=x 1_(a>Z),
    tau=W(x_high)/W.                                  (11)

Whenever a>Z, K(a,b)<=a^-s<Z^-s=qC W^-s for every b.
Thus, retaining both cross orientations and the high-high term,

    E_s(x)<=C(1-tau)^t W^t
              +qC W^t(2tau-tau^2).                    (12)

For0<=z<=1, and in fact all z>=0, the weighted arithmetic-geometric mean inequality gives

    z^t<= (2-t)z+(t-1)z^2.

At z=1-tau this yields (1-tau)^t<=1-t tau+(t-1)tau^2.
Since q=1-3s/4, t-2q=s/2 and t-1-q=-s/4.
Consequently(12) and near extremality imply

    1-epsilon<=1-(s/2)tau-(s/4)tau^2,
    tau<=2epsilon/s.                                  (13)

This tail bound is uniform in the finite ambient and works even when Z is not an integer.
Its use of global C is explicit: the low subarray must satisfy(1).
No bound on ordinary numeric density or support width was assumed.

<a id="uniform-near-extremal-fractionality"></a>
### 3. Uniform control of low-order fractionality by partial random rounding

Keep x,W,Z as in Section2.
Independently for each low coordinate a<=Z, replace x_a by a Bernoulli variable taking phi(a) with probability x_a/phi(a) and0 otherwise; keep each high coordinate unchanged.
Call this partially rounded array Y.
Every realization is feasible for(1), and E W(Y)=W.
Put

    V=sum_(a<=Z)x_a(phi(a)-x_a),
    J=sum_(a<=Z)a^-s x_a(phi(a)-x_a).                  (14)

Independence gives Var(W(Y))=V and E E_s(Y)=E_s(x)+J, since only diagonal contributions gain variance.
The preceding elementary power inequality, applied to W(Y)/W and then averaged, gives

    E W(Y)^t <= W^t+(t-1)W^(t-2)V.

Together with(1) and near extremality,

    J-C(t-1)W^-s V<=epsilon C W^t.                    (15)

Every low order has a^-s>=Z^-s=qC W^-s.
Since q-(t-1)=s/4, (15) proves

    V<=4epsilon W^2/s,
    J<=(4/s-3)epsilon C W^t.                          (16)

This is a genuine capacity-sensitive quantitative stability estimate.
No strong functional estimate of the refuted L396 type is used.
No number-of-coordinates factor appears.
The partially rounded Y is used to prove expectation inequalities, not selected as the final divisor ideal.

<a id="coupled-full-ideal-rounding"></a>
### 4. Coupled endpoint rounding into nested full divisor ideals

Apply Sections2--3 to each compressed x_i, with Z_i=W_i(qC)^(-1/s).
Since W1<=W0, Z1<=Z0.
For EACH label a in B choose one independent random U_a uniform in(0,1), using the SAME U_a for the two arrays.
Define

    v_i(a)=phi(a)1_(a<=Z_i)1_(U_a<=x_i(a)/phi(a)).     (17)

The arrays are full endpoint arrays, and v1<=v0 because both the cutoff and the threshold are nested.
Property(9) makes each positive support a divisor ideal: if a is selected and d is a proper divisor, then x_i(d)=phi(d) and d<a<=Z_i, so d is selected with probability1.
The description by continuous U_a is merely a convenient coupling of finitely many joint Bernoulli outcomes; no limiting random process is used.

Let n_i=v_i-(x_i)_low be its centered low-coordinate rounding noise.
Its expected mass is0 and expected kernel energy is J_i.
The omitted high part h_i=(x_i)_high has mass at most(2epsilon/s)W_i, and

    E_s(h_i)<=Z_i^-s W(h_i)^2
                <=4q epsilon^2 C W_i^t/s^2.

The errors are v_i-x_i=n_i-h_i.
Their expected squared mass error and expected kernel energy satisfy EXACTLY

    E[W(v_i)-W_i]^2=V_i+W(h_i)^2<=A_e W_i^2,
    E E_s(v_i-x_i)=J_i+E_s(h_i)<=B_e C W_i^t.          (18)

The cross term in the second expectation is zero because each coordinate of n_i has mean zero.
Signed-array energies are nonnegative by C104's finite PSD Gram theorem, so Markov's inequality applies.

There are four nonnegative random quantities in(18), two for each array.
A union bound with threshold eight times the stated expectations shows that with probability at least1/2 all satisfy

    |W(v_i)-W_i|<=eta W_i,
    E_s(v_i-x_i)<=8B_e C W_i^t.                       (19)

For0<epsilon<=s/4096, one has A_e<1/512, B_e<=A_e and1-epsilon>1/2.
Hence eta^2<1/64 and d^2<1/32, in particular eta,d<1/4.
On the positive-probability event, both supports are nonempty because their masses are at least(1-eta)W_i>0.
Thus the required finite nested ideals exist.

<a id="rounding-energy-and-correlation-controls"></a>
### 5. Final normalized-energy, mass-ratio and correlation bounds

By the finite Gram representation write ||u||_K=sqrt(E_s(u)); Cauchy and its triangle inequality are valid also for signed errors.
From(19) and E_s(x_i)>=(1-epsilon)CW_i^t,

    ||v_i-x_i||_K<=d ||x_i||_K.

Therefore ||v_i||_K>=(1-d)||x_i||_K.
With the mass upper bound in(19), this proves(5), while(4) and the stated mass-ratio interval follow directly.

Cauchy applied to the two error cross terms and their product gives

    E_s(v0,v1)>=E_s(x0,x1)
                  -(2d+d^2)||x0||_K||x1||_K,
    ||v0||_K||v1||_K<=(1+d)^2||x0||_K||x1||_K.

When the first resulting numerator is nonnegative, divide by the latter upper bound and use(10).
If it is negative, the actual cross energy of the nonnegative v_i is nonnegative, supplying the zero bound instead.
This proves exactly(6).
There is no dependence on the ratio W1/W0 in any of these estimates.

<a id="asymptotic-inverse-equivalence-and-cost"></a>
## Consequence for the arithmetic inverse, and the remaining gap

For any sequence of finite divisor-closed ambients and valid constants C, nested nonzero feasible arrays with both normalized ratios divided by C tending to1 and correlation tending to1 have nested full-totient divisor-ideal replacements with the SAME limiting properties and relative masses tending to the original ones.
The ambients, constants, prime supports, exponents and original mass ratio may vary arbitrarily.
In particular a hypothetical counterexample to an asymptotic near-global nested inverse for REAL arrays transfers to full integer divisor ideals without a dimension or prime-support loss.
Conversely full ideals are already real-capacity arrays.
This is a quantitative asymptotic reduction, not the inverse itself.

The reduction pays O_s(sqrt(epsilon)).
To preserve a hypothetical first-order prime-recursion effect of size1/p using this bound alone, it is sufficient to have epsilon=o(p^-2); epsilon merely tending to0 does not guarantee the needed precision.
The theorem supplies neither a lower bound on the available deficit nor cancellation of C108's1/p term.
It also does not turn C111's finite99% boxes into a universal fractional-capacity assertion: its constants may be too coarse for that finite threshold, and the ambient remains fixed in any individual use.

What remains open is an arithmetic estimate on the resulting nested full ideals that rules out or pays for matched near-global energies, near-Cauchy equality and mass ratio near p^-2 at precisely the needed scale.
Generic PSD alone is excluded by C111's countermodel.
Here the genuinely arithmetic ingredients are the pointwise divisor-row monotonicity, the finite down-compression schedule, lcm(a,b)>=max(a,b), the capacity Bernoulli diagonal identity and the common near-extremal constant.
They provide the exact reduction but no universal bound on that constant.

No actual polynomial order inventory, valuation certificate or near-one Mahler sequence has been constructed.
No preservation of original arithmetic root-group realization is asserted by these abstract replacements.
G0001's original degree, complete groups and full norm costs would still be required in an application.

## Author checking status

The preceding theorem is newly developed author mathematics awaiting a separately organized noncontributing review of its actual fixed retention.
Root has not supplied a proof step in this argument.
No native program, new J or fixed C was made by this author.
The statement and complete proofs are retained here for inspection; no independent acceptance is claimed.

<a id="uniform-nested-rounding-entire-author-freeze"></a>
## Complete author checks and whole-artifact freeze

2026-10-14T20:47.
The author checked the complete finite compression formula and its feasibility without assuming phi(d)<=phi(a); coordinatewise monotonicity of BOTH new entries for simultaneous nesting; the strict arithmetic row comparison and both cross orientations; finite ascending-d termination and preservation of each previously nonfull-divisor invariant; origin/compactness and positive finite C_B; the direction of correlation after individual energy growth; the exact high-high versus high-low tail coefficients; the weighted power inequality for ALL nonnegative arguments; the constants q, t-2q and q-(t-1); every variance and diagonal identity with high coordinates kept deterministic; the use of the SAME uniforms with the ordered cutoffs; full proper divisors after rounding; zero expectation of the signed error cross term; all four Markov events and their joint positive probability; positivity of the rounded masses; both norm-triangle directions; the case of a negative lower numerator in the final rho formula; and every small-epsilon/ambient-independent constant.
No numerical experiment supplies any of these steps.

The preliminary chain lemma and its simpler direct-capture comparison, the failed scalar first-variation discriminator with its explicit formal limits, and the precise O_s(sqrt(epsilon)) cost and sufficient epsilon=o(p^-2) precision are retained.
The latter is sufficient for an o(1/p) error from these estimates, not asserted necessary for every possible improved method.
Root subsequently read this rolling argument and reported a preliminary reconstruction without supplying a proof step; that discussion is not fixed acceptance and does not replace the later complete independent review.

Freeze the ENTIRE actual original: responsible question/reuse and failed approaches; Statement/equations1--6; complete Argument Sections1--5/equations7--19; all finite scheduling, probability, uniformity, error and asymptotic-reduction controls; exact accepted C104/C105/C108/C111 interfaces and non-adoption of search leads; contribution account and unrestricted weak-bound/actual-polynomial limitations.
A structural material check passed but does not establish mathematical truth.
Root may retain the whole original directly in an actual C and organize complete independent review of that artifact.
The author will not edit global research decisions or claim a universal constant from this reduction.

## Fixed organization

The ENTIRE final author original is retained above: actual question and reuse limits, failed first-variation and chain approaches, exact valid-finite-C interface, complete simultaneous compression/tail/rounding theorem and all constants, actual asymptotic meaning and prime-recursion precision expense.
Root supplied direction and a preliminary noncontributing read, not a proof step.
This fixed whole body needs actual complete independent review before acceptance.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:50 |
| status | open |
| reason | Retain the complete simultaneous near-global real-capacity to full-divisor-ideal reduction, with uniform paid errors and explicit remaining arithmetic inverse. No universal fractional constant, recursion cancellation or actual near-one coverage is assumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full quantitative nested replacement theorem for every finite nonempty divisor-closed ambient and every valid common C, with all real/epsilon/mass/correlation guards. |
| argument | [Entire proof](#argument) | Finite synchronized compression, all tail and variance identities, common-threshold ideal rounding, four-event selection, complete norm/correlation controls and asymptotic limits. |
| dependency | [Finite lcm Gram kernel](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Actual finite positive semidefinite kernel and signed-error Gram/Cauchy interface, not a universal correlated constant. |
| dependency | [Earlier strict optimizer interface](Yin_C_G0111_v1.md#strict-extremal-capacity-characterization) | Selected-potential comparison in the preserved preliminary approach; full simultaneous near-optimal theorem is proved separately here. |
| support | [Exact prime-recursion cost](Yin_C_G0108_v2.md#nested-slice-continuation-statement) | The actual first-order1/p mechanism to which the explicit O_s(sqrt epsilon) precision consequence refers; cancellation is not imported or established. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:53 |
| status | proved |
| reason | Adopt R470 complete independent review of the actual simultaneous compression/tail/rounding proof and all selected interfaces. Nested real near-global extrema admit full divisor-ideal replacements with dimension-independent O_s(sqrt epsilon) losses. The arithmetic inverse, first-order recursion cancellation and universal fractional bound remain unproved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full quantitative nested replacement theorem for every finite nonempty divisor-closed ambient and every valid common C, with all real/epsilon/mass/correlation guards. |
| argument | [Entire proof](#argument) | Finite synchronized compression, all tail and variance identities, common-threshold ideal rounding, four-event selection, complete norm/correlation controls and asymptotic limits. |
| dependency | [Finite lcm Gram kernel](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Actual finite positive semidefinite kernel and signed-error Gram/Cauchy interface, not a universal correlated constant. |
| dependency | [Earlier strict optimizer interface](Yin_C_G0111_v1.md#strict-extremal-capacity-characterization) | Selected-potential comparison in the preserved preliminary approach; full simultaneous near-optimal theorem is proved separately here. |
| support | [Exact prime-recursion cost](Yin_C_G0108_v2.md#nested-slice-continuation-statement) | The actual first-order1/p mechanism to which the explicit O_s(sqrt epsilon) precision consequence refers; cancellation is not imported or established. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0797_v1.md#uniform-nested-rounding-actual-whole-independent-finding) | Entire actual statement, complete retained argument, direct dependency interfaces, source/contribution limits and exact conditional/nonconclusion scope. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:39 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. The simultaneous nested full-ideal replacement, all finite-C, compression, tail, variance, coupling, mass, energy and correlation controls are supported with the stated ambient-independent O_s(sqrt(epsilon)) cost. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full quantitative nested replacement theorem for every finite nonempty divisor-closed ambient and every valid common C, with all real/epsilon/mass/correlation guards. |
| argument | [Entire proof](#argument) | Finite synchronized compression, all tail and variance identities, common-threshold ideal rounding, four-event selection, complete norm/correlation controls and asymptotic limits. |
| dependency | [Finite lcm Gram kernel](Yin_C_G0104_v1.md#finite-product-envelope-extension) | Actual finite positive semidefinite kernel and signed-error Gram/Cauchy interface, not a universal correlated constant. |
| dependency | [Earlier strict optimizer interface](Yin_C_G0111_v1.md#strict-extremal-capacity-characterization) | Selected-potential comparison in the preserved preliminary approach; full simultaneous near-optimal theorem is proved separately here. |
| support | [Exact prime-recursion cost](Yin_C_G0108_v2.md#nested-slice-continuation-statement) | The actual first-order1/p mechanism to which the explicit O_s(sqrt epsilon) precision consequence refers; cancellation is not imported or established. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0115-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. |

