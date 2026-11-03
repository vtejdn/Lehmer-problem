---
author: Yin
---
# Euler-capacity prime layers under their original conditioned product law

Date: 2026-10-15.
Human author Yin.
New G0001 author inquiry by g_bridge_audit under root assignment.
Root supplied the full-phi layer inquiry, without a proof step.
The preceding C126 and its D37 original remain frozen.

## Responsible question

For primes in a common interval (P,2P], put the FULL Euler weight w_A=phi(product_(p in A)p)=product_(p in A)(p-1) on EVERY k-subset.
Test whether fixed positive ordered triple density at the ORIGINAL X<=CW forces fixed-proportion capture at a fixed enlarged window, with all original mass and degree costs retained.
Global weight distortion can grow with k.
The precise normalized law is a fixed-cardinality conditioned product law, not arbitrary weights and not an unconditioned independent law.

## Reuse screen and source obligation

Read [C104's exact product and finite-envelope statements](Yin_C_G0104_v1.md#product-fractional-moment-statement).
A single k-layer is not a product profile unless it degenerates to one order.
Its natural full-divisor Euler envelope has mass N=product p; no uniformly bounded envelope-to-layer mass ratio is supplied by C104.
Thus no direct general-layer application is asserted.
[C126v2's equal-weight and bounded-distortion theorem](Yin_C_G0126_v2.md#statement) is relevant but does not uniformly cover the full Euler weights.
Its original probability/time structure is reused below only after replacing the law honestly.
The v2 correction of an unrelated C105 comparison is respected; no such compression monotonicity is used here.

A local exact-term search over Claims, ledgers, reviews/source audits, references and registry initially found no applicable negative-association, conditional-Bernoulli or Newton-inequality input.
The needed source check was for pairwise nonpositive covariance of product-weighted fixed-size subset indicators (and their complements), not arbitrary fixed-size laws.
The exact external statement was then checked before the substantial argument below and registered as BBL09-U001.
No computation is proposed, and the unrestricted capacity target remains open.

<a id="euler-layer-source-interface"></a>
## Source check and exact known input

The author directly inspected Borcea--Branden--Liggett, *Negative dependence and the geometry of polynomials*, [arXiv0707.2340v2](https://arxiv.org/pdf/0707.2340v2), dated27July2008,47-page version.
The needed result is Corollary4.17, printedp28/PDFindex27, with Lemma4.16's definitions on the same page.
At f(z)=product_i(1+z_i), which is stable because none of its factors vanish when all Im(z_i)>0, the homogeneous component E_r is the elementary symmetric polynomial e_r.
The corollary therefore gives the classical normalized Newton inequality for positive variables.
In particular

    e_r(x)^2>=e_(r-1)(x)e_(r+1)(x).                      (N)

Only this positive-variable specialization is used below, at the accepted statement/applicability scope of [BBL09-U001](../audits/literature/BBL09/Yin_U001.md#bbl09-u001).
The author also inspected Definition2.3 on printedp7 and the statements of Theorem4.9 onp24 and Corollary4.18 onp29; those stronger negative-association and truncation results are background, not additional proof inputs.
The primary Adamczak--Polaczyk arXiv2108.12636 introduction was screened for conditional-Bernoulli terminology only; none of its concentration theorems is used.
Root separately checked and registered the actual BBL v2 source.
Neither the stable-polynomial proof chain nor the entire BBL paper was newly audited.
The normalized Newton inequality implies(N) because the ratio binom(N,r)^2/[binom(N,r-1)binom(N,r+1)] is at least1 in its interior range; boundary indices are handled below directly.

The remaining calculations below are ordinary finite expansions and probability bounds.
In particular the passage from (N) to pair covariance, the marginal bounds, and the numerical original-time constraints are written out rather than hidden inside a stronger external concentration theorem.

<a id="statement"></a>
## 1. Full Euler layers and positive-retention arbitrary thinning

Let P>=2 be real and Q any pool of m distinct primes in (P,2P].
Fix an integer0<=k<=m.
On its complete k-layer put

    o_A=product_(p in A)p,  v_A=phi(o_A)=product_(p in A)(p-1),
    V=sum_(|A|=k)v_A.

For ANY array 0<=w_A<=v_A on this layer, omit zero weights and suppose W=sum_A w_A>0.
Define ORIGINAL ordered triple mass and capture by

    T_w(X)=sum_(A,B,D: lcm(o_A,o_B,o_D)<=X)w_A w_B w_D,
    H_w(X)=max_(integer1<=n<=X)sum_(o_A divides n)w_A.

Repeated labels are included.
T_v uses the full Euler weights and total V.

**A. Full-layer vanishing.**
For every fixed C>0, uniformly along all sequences with m->infinity,1<=k<=m-1 and integer1<=X<=CV,

    T_v(X)/V^3 ->0.                                      (1)

No assumption of globally comparable label weights is made; their ratio may grow with k.

**B. Original-time capture after positive retained mass.**
For every fixed C>0,0<delta<=1 and0<a<=1 there is c(C,delta,a)>0 such that

    W>=aV,  1<=X<=CW,  T_w(X)>=delta W^3
       ==> H_w(X)>=c(C,delta,a)W.                        (2)

The enlargement is B=1.
The weights may be arbitrary real capacities, with arbitrary zeros, and need not themselves have a product law.
The price is the GLOBAL retained fraction a, not a pointwise lower weight bound.
Taking w=v and a=1 gives the full Euler-layer result.
Constants below are existential, not numerical.

The result does not cover a->0, an unrestricted mixture of different k-layers, primes of uncontrolled relative sizes, or arbitrary capacity arrays.
It asserts no realization of these inventories by an actual irreducible near-one polynomial.

<a id="argument"></a>
## 2. The original conditional product law and its pair covariance

For the nonendpoint proof assume m>=2 and1<=k<=m-1, and write j=m-k.
Index the primes by i and put x_i=p_i-1>0.
The EXACT original full-layer law is

    mu(A)=product_(i in A)x_i / e_k(x_1,...,x_m), |A|=k.   (3)

For three independent samples from this SAME law, the probability that their lcm is at most X is exactly T_v(X)/V^3, including repeated labels.

Equivalently, take independent Bernoulli variables with success probabilities x_i/(1+x_i) and condition their sum to equal k.
This equality follows simply by canceling the common product of (1+x_i)^(-1); it does not assume the conditioned coordinates remain independent.
The complement B=Q\A has the analogous j-set product law with variables y_i=1/x_i, since product_(i in A)x_i=(product_i x_i) product_(i in B)y_i.

For distinct i,l, let a0=e_k, b0=e_(k-1), c0=e_(k-2) in the OTHER m-2 variables, with e_0=1 and e_r=0 outside its permitted range.
Its normalizer is

    Z=a0+(x_i+x_l)b0+x_i*x_l*c0>0.

Writing pi_i=Pr(i in A), direct expansion gives

    Pr(i,l in A)=x_i*x_l*c0/Z,
    pi_i=x_i*(b0+x_l*c0)/Z,
    pi_l=x_l*(b0+x_i*c0)/Z,
    pi_i*pi_l-Pr(i,l in A)=x_i*x_l*(b0^2-a0*c0)/Z^2>=0. (4)

The last inequality is (N) in the interior indices.
If k=1 then c0=0; if k=m-1 then a0=0.
These handle all endpoint indices, including m=2, without an out-of-range Newton assertion.
Complement indicators have the same covariance because Cov(1-X_i,1-X_l)=Cov(X_i,X_l).
We require only this pairwise conclusion, not the stronger negative-association hierarchy.

<a id="euler-layer-marginals"></a>
## 3. Uniform coordinate bounds and three-sample variance

Set u=min_i x_i and v=max_i x_i.
Since P>=2,

    v/u<=(2P-1)/(P-1)<=3.                               (5)

For the m-1 variables excluding i, the elementary double-counting identity is

    k e_k(x_-i)=sum_(|B|=k-1) product_(l in B)x_l
                            *sum_(l notin B,l!=i)x_l.

Each inner sum has exactly j terms.
Therefore j*u*e_(k-1)<=k*e_k<=j*v*e_(k-1).
All these symmetric polynomials are positive at1<=k<=m-1.
The exact odds formula is pi_i/(1-pi_i)=x_i*e_(k-1)(x_-i)/e_k(x_-i), so

    k/(3j)<=pi_i/(1-pi_i)<=3k/j,
    k/(k+3j)<=pi_i<=3k/(3k+j)<=3k/m,
    j/(j+3k)<=rho_i:=1-pi_i<=3j/(3j+k)<=3j/m.            (6)

Also sum_i pi_i=k and sum_i rho_i=j, exactly, because every sample has cardinality k.
Upper bounds such as3k/m may exceed1 and are used only as bounds.

Take THREE independent samples from (3).
Let U be their union size and I the common missing-set size, so U=m-I.
By (4), for two distinct coordinates the probability that both lie in all three complements is at most (rho_i*rho_l)^3.
Thus the indicators contributing to I, and also their complements contributing to U, have nonpositive pair covariances.
It follows that

    E I=sum_i rho_i^3<=9j*(j/m)^2,
    E U=sum_i[1-(1-pi_i)^3],
    3k-3(max_i pi_i)k<=E U<=3k,
    E U-k=sum_i pi_i*rho_i*(1+rho_i)>=min_i(rho_i)*k,
    Var I=Var U<=min(E I,E U)<=3k.                       (7)

These estimates retain the full original law.
For two independent samples,

    E|A_1 intersect A_2|=sum_i pi_i^2<=3k^2/m.            (8)

Equations(6)--(8) replace the uniform marginals in C126; the integer capacities and time bounds below do not depend on a change of law.

<a id="euler-layer-original-time"></a>
## 4. Full Euler capacity pays the two time bounds

The finite prime estimate already proved in [C100](Yin_C_G0100_v1.md#prime-power-small-order-capacity) gives, for P>=8,

    m<=pi(2P)<=14P/log P.                                (9)

In particular m->infinity implies P->infinity.
For any layer,

    V=e_k(p_i-1)<=binom(m,k)(2P)^k.

Since the lcm of a sampled triple is the product of its union primes, compatibility at X<=CV implies

    U<=L:=k+[k log2+log binom(m,k)+log C]/log P.           (10)

Near the full layer use instead N=product_i p_i and the EXACT identity

    V=phi(N)e_j((p_i-1)^(-1))
       <=N binom(m,j)/(P-1)^j.

The triple lcm is exactly N divided by the product of its common missing primes.
Consequently compatibility implies

    I>=b:=[j log(P-1)-log binom(m,j)-log C]/log(2P).       (11)

If b>0, Markov and(7) give

    Pr(compatible)<=9j*(j/m)^2/b.                        (12)

No factor N, prime product, or original mass has been dropped.
The rough (2P)^k estimate is not substituted for the exact complement estimate in the near-full regime.

<a id="euler-layer-vanishing-proof"></a>
## 5. All three regimes and uniform vanishing

Suppose (1) fails.
Then one can choose a sequence with m->infinity and compatibility probability bounded below by some fixed positive number.
Pass to a subsequence k/m->alpha in [0,1].
The following cases contradict that lower bound.
They also show why the needed concentration does not require a global ratio of label weights.

**If0<alpha<1**, (10) and binom(m,k)<=2^m give L=k+o(m).
By(6)--(7),

    E U-k>=k*j/(j+3k),

which is a positive multiple of m eventually.
Meanwhile Var U<=3m.
Chebyshev therefore gives Pr(U<=L)->0.

**If alpha=0**, use binom(m,k)<=(e m/k)^k and eventually m<=P from(9).
Then (10) yields L/k<=2+o(1), uniformly in k>=1; the term log C/(k log P) is bounded above by max(log C,0)/log P.
By(6)--(7), E U/k->3.
If k->infinity, eventually E U-L>=k/2 and Chebyshev gives Pr(U<=L)<=12/k->0.
If k has a bounded subsequence, pass to a fixed positive k.
Eventually L<3k; the event U<3k requires an intersection in one of the three pairs of samples.
Equation(8) and a union bound give

    Pr(U<3k)<=9k^2/m ->0.                               (13)

Every sequence of positive integer k has one of these two subsequences, so this also covers all sparse-layer sequences.

**If alpha=1**, set theta=j/m->0, still j>=1, and C_+=max(C,1).
From(11) and the binomial bound,

    b/j>=[log(P-1)-1+log theta-(log C_+)/j]/log(2P).       (14)

When theta>=P^(-1/2), the right side is at least1/4 for large P.
Hence (12) gives Pr(compatible)<=36theta^2->0.
When theta<P^(-1/2), use j>=1,theta>=1/m,(9), and P-1>=P/2.
With D_C=log28+1+log C_+,

    b/j>=[log log P-D_C]/log(2P)>0

eventually, and

    Pr(compatible)<=9log(2P)/[P(log log P-D_C)] ->0.       (15)

The Markov threshold is positive in both cases once the parameters are sufficiently large.
The bounds remain valid if the sequence switches between the two cases.
This covers fixed j as well as growing j, and completes the proof of uniform(1).

<a id="euler-layer-thinning-capture"></a>
## 6. Arbitrary thinning with a paid retained fraction

Let the weights in StatementB satisfy W>=aV.
Positivity and the pointwise bound w_A<=v_A give

    T_v(X)>=T_w(X)>=delta W^3>=delta*a^3*V^3,
    X<=CW<=CV.                                         (16)

Thus (1) bounds the pool size in every nonendpoint layer: there is an integer M(C,delta*a^3)>=2 such that any example satisfying (16) has m<M.
This is an all-finite assertion by contradiction: otherwise choose models with unbounded m, violating uniform(1).
No pointwise lower bound on a retained w_A is used.

Let S_X=sum_(o_A<=X)w_A be the mass of eligible labels.
Every compatible triple has all three labels eligible, so

    delta W^3<=T_w(X)<=S_X^3,
    S_X>=delta^(1/3)W.                                  (17)

There are at most binom(m,k)<=2^M eligible labels.
One therefore has weight at least delta^(1/3)2^(-M)W; its OWN integer order is at most X and captures that weight.
Thus(2) holds with

    c(C,delta,a)=delta^(1/3)2^(-M(C,delta*a^3)).            (18)

If k=0 or k=m, including m=0 or1, the full layer has one order and W>0 means its weight is positive.
Positive triple mass forces it to be at most X, whence H_w(X)=W.
Thus all small and endpoint cases are covered separately from the nonendpoint divisions and limits.
The original X is integer; no enlargement, real-time replacement, or weighted average of different times appears.
For delta>1 the premise is impossible.

The use of the full law in(16) is solely an entrywise domination inequality with the explicit a^3 density payment.
It does not assert that arbitrary retained weights have negative correlation.
A failure of negative correlation in a thinned law therefore would not invalidate this step, whereas a->0 would remove its uniform force.

<a id="euler-layer-costs-and-limits"></a>
## 7. Existing-envelope comparison and actual-polynomial costs

For clarity, the natural C104 full-divisor product majorant really can have an unbounded mass ratio here.
Its mass is N.
At the layer k=m-1,

    V/N=(phi(N)/N)sum_i1/(p_i-1)
        <=m/(P-1)<=28/log P

for sufficiently large P by(9).
Thus N/V->infinity on any sequence with m->infinity.
This does not prove that ALL possible finite product envelopes fail; it shows why that natural direct C104 substitution supplies no uniform cost.
The present proof uses the fixed-cardinality law instead of asserting a new envelope.

For an actual monic irreducible nontorsion integer-unit polynomial F, original degree d, root alpha and K=Q(alpha), a good prime p must provide COMPLETE occurring order groups with the actual weights w_A, each bounded by phi(o_A).
To use StatementB require that these selected orders lie in one indicated comparable-prime k-layer, that their mass W is at least a times the total Euler capacity V of that COMPLETE ambient layer, W>=gamma*d, and that their original triple density is at least delta at an integer X<=C*d.
The absent ambient orders may have weight0; no artificial root is inserted there.

Use(2) with capacity-scale C/gamma.
At one actual original integer n<=X,

    sum_(o_A divides n)w_A>=c(C/gamma,delta,a)*gamma*d.

The existing [C256 original-root interface](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) then gives

    D_n=Norm_(K/Q)(alpha^n-1)=Res(F,t^n-1),
    C_n=|D_n| in Z_(>0),
    log C_n>=(log p)v_p(C_n)
       >=gamma*c(C/gamma,delta,a)*log2*d.                 (19)

All original roots, every nonnegative local depth, and the original field remain in this norm.
The auxiliary t^n-1 has degree n<=Cd, content1 and squared coefficient norm2.
[L168's finite-income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion), with its accepted Pri11 statement/applicability scope, supplies its strict positive Mahler lower bound for this covered class.
No automatic existence of such a good prime, positive retained fraction a, linear actual mass or triple density is proved here.

This round isolates and closes the full Euler-layer mechanism and its fixed-retention thinning extension.
It does not solve arbitrary capacities, uncontrolled inter-prime scales, multiple layers, or vanishing retained mass.
A general fixed-size distribution need not satisfy(4); arbitrary thinning is handled only through(16), with its explicit price.
No native program, numerical evidence or near-one realization is used.

For comparison, no containment of C126's entire equal-weight class is asserted: its equal weights need not retain a uniform fraction of the full Euler-layer mass.
Conversely this statement permits zeros and uncontrolled ratios between positive retained weights.
The two positive interfaces have different assumptions; no claim of a universal hierarchy is needed.

<a id="euler-layer-author-freeze"></a>
## Author check and freeze

2026-10-15T08:28.
The g_bridge_audit author freezes this ENTIRE draft for fixed retention and separate whole review.
StatementA is the full Euler-layer uniform density vanishing; StatementB is original-time capture for arbitrary thinning with a fixed fraction of the complete layer's Euler capacity retained.
Sections2--6 supply the original-law covariance and marginal calculations, all three asymptotic regimes, exact complement product/time constraint, and the all-finite capture.
Section7 preserves the C104 comparison, conditional actual-polynomial norm and all remaining coverage limitations.
Root supplied the inquiry and source registration, not a proof step.
No independent review is asserted by the author.

The author checked the Newton index range, m=2 endpoints, the exact same-law pair covariance identity, reciprocal complement law, all marginal denominators, the independent-three-sample step, near-full threshold positivity and constants9/36, real P, real weights and zero omissions, k=0/m and m=0/1, fixed-k collision bound, nonconstructive uniform-to-finite quantifier, a^3 payment, eligible-mass pigeonhole, and the original-field norm/degree/coefficient costs.
Direct proof inputs are [BBL09-U001](../audits/literature/BBL09/Yin_U001.md#bbl09-u001), C100's elementary prime estimate, and L74/L168 solely for the conditional actual-polynomial application.
C104 and C126 are comparison and derivation-history inputs, not invoked theorem premises.
The structural material check returned checked1 on the developed draft; no mathematical program or J was needed.
The unrestricted G0001 goal remains open.

## Fixed organization

The entire author account is retained: exact full Euler law, positive-variable Newton source, original pair covariance/marginal calculations, all three uniform regimes, arbitrary thinning with the explicit retained-mass price, finite capture, natural-envelope comparison and full conditional original norm costs, plus complete author check and limits.
Root supplied direction and source registration, not a proof step.
Actual separate whole review remains pending.

## Current assessment
[Selected decision](#decision-isolated-current-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T08:32 |
| status | open |
| reason | Retain complete full-Euler comparable-prime layer density vanishing and original-window capture after arbitrary capacity thinning retaining a fixed fraction of full-layer mass. The law, covariance, numerical time and original norm costs are explicit; general sparse-retention, mixed-layer and uncontrolled-scale coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full Euler and retained thinning](#statement) | Entire A--B, exact original weights and time, uniform varying k/pool, arbitrary zero weights with fixed global retention, and conditional actual-polynomial scope. |
| argument | [Complete original-law proof](#argument) | All Sections1--7, Newton specialization and equations1--19, finite boundaries, covariance/marginals, three regimes, retention price, comparisons, source limits and freeze. |
| dependency | [Newton positive-variable input](../audits/literature/BBL09/Yin_U001.md#bbl09-u001) | Only accepted classical Corollary4.17 specialization and explicitly handled boundary indices; no wholesale strong-Rayleigh theorem assumed. |
| dependency | [Elementary prime count](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16 and P>=8 pool consequence. |
| dependency | [Full original local norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups and all original roots/depths at the single captured original time. |
| dependency | [Original finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional original degree, full field norm and actual auxiliary degree/coefficient costs; no automatic actual coverage. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T08:40 |
| status | proved |
| reason | Adopt R482 complete actual noncontributor review. Full Euler comparable-prime layers lose positive triple density as the nonendpoint pool grows; arbitrary capacity thinning with a fixed positive retained fraction has original-window capture. All original-law, Newton, time, norm and boundary costs are proved. Vanishing retained mass, general mixed/scaled inventories and actual coverage remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full Euler and retained thinning](#statement) | Entire A--B, exact original weights and time, uniform varying k/pool, arbitrary zero weights with fixed global retention, and conditional actual-polynomial scope. |
| argument | [Complete original-law proof](#argument) | All Sections1--7, Newton specialization and equations1--19, finite boundaries, covariance/marginals, three regimes, retention price, comparisons, source limits and freeze. |
| dependency | [Newton positive-variable input](../audits/literature/BBL09/Yin_U001.md#bbl09-u001) | Only accepted classical Corollary4.17 specialization and explicitly handled boundary indices; no wholesale strong-Rayleigh theorem assumed. |
| dependency | [Elementary prime count](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16 and P>=8 pool consequence. |
| dependency | [Full original local norm](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups and all original roots/depths at the single captured original time. |
| dependency | [Original finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional original degree, full field norm and actual auxiliary degree/coefficient costs; no automatic actual coverage. |
| review | [Whole actual Euler-layer finding](../audits/reviews/Yin_R_G0798_v1.md#euler-layer-whole-independent-finding) | Entire statement and all Sections1--7, equations1--19 and sourceN, exact original-law covariance/marginals, thinning price, all direct inputs and scope limits. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--B, exact original weights and time, uniform varying k/pool, arbitrary zero weights with fixed global retention, and conditional actual-polynomial scope. |
| argument | [Argument](#argument) | All Sections1--7, Newton specialization and equations1--19, finite boundaries, covariance/marginals, three regimes, retention price, comparisons, source limits and freeze. |
| dependency | [Dependency](../audits/literature/BBL09/Yin_U001.md#bbl09-u001) | Only accepted classical Corollary4.17 specialization and explicitly handled boundary indices; no wholesale strong-Rayleigh theorem assumed. |
| dependency | [Dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16 and P>=8 pool consequence. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups and all original roots/depths at the single captured original time. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Conditional original degree, full field norm and actual auxiliary degree/coefficient costs; no automatic actual coverage. |
| review | [Review](../audits/reviews/Yin_R_G0798_v1.md#euler-layer-whole-independent-finding) | Entire statement and all Sections1--7, equations1--19 and sourceN, exact original-law covariance/marginals, thinning price, all direct inputs and scope limits. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--B, exact original weights and time, uniform varying k/pool, arbitrary zero weights with fixed global retention, and conditional actual-polynomial scope. |
| argument | [Exact retained argument](#argument) | All Sections1--7, Newton specialization and equations1--19, finite boundaries, covariance/marginals, three regimes, retention price, comparisons, source limits and freeze. |
| dependency | [Exact retained dependency](../audits/literature/BBL09/Yin_U001.md#bbl09-u001) | Only accepted classical Corollary4.17 specialization and explicitly handled boundary indices; no wholesale strong-Rayleigh theorem assumed. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16 and P>=8 pool consequence. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups and all original roots/depths at the single captured original time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Conditional original degree, full field norm and actual auxiliary degree/coefficient costs; no automatic actual coverage. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0798_v1.md#euler-layer-whole-independent-finding) | Entire statement and all Sections1--7, equations1--19 and sourceN, exact original-law covariance/marginals, thinning price, all direct inputs and scope limits. |

### Decision isolated-current-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:50 |
| status | proved |
| reason | Adopt the new isolated R798 whole finding for this exact highest physical statement and complete argument, after necessary fixed-mathematics/source inspection and subsequent comparison with all original review accounts. Preserve the complete current mathematical status, input relations and scopes, all original costs and open coverage limits. R798 separately retains the original unknown findings, dates, exact historical bindings, missing-table observations and negative predecessor findings; this new independent review does not retrospectively upgrade them or claim source-proof audits or Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--B, exact original weights and time, uniform varying k/pool, arbitrary zero weights with fixed global retention, and conditional actual-polynomial scope. |
| argument | [Exact retained argument](#argument) | All Sections1--7, Newton specialization and equations1--19, finite boundaries, covariance/marginals, three regimes, retention price, comparisons, source limits and freeze. |
| dependency | [Exact retained dependency](../audits/literature/BBL09/Yin_U001.md#bbl09-u001) | Only accepted classical Corollary4.17 specialization and explicitly handled boundary indices; no wholesale strong-Rayleigh theorem assumed. |
| dependency | [Exact retained dependency](Yin_C_G0100_v1.md#prime-power-small-order-capacity) | Only pi(y)<=7y/log y for real y>=16 and P>=8 pool consequence. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Conditional actual complete good-prime groups and all original roots/depths at the single captured original time. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Conditional original degree, full field norm and actual auxiliary degree/coefficient costs; no automatic actual coverage. |
| review | [Isolated current whole finding](../audits/reviews/Yin_R_G0798_v1.md#g127-current-whole-independent) | Entire exact current statement and complete argument, every necessary original/current mathematical interface, original norms/weights/times/costs, source depth, finite controls and explicit limits; old physical-version and relationship findings remain separate in R798. |
