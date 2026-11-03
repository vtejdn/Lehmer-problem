---
author: Yin
---

# True-critical excursion delay, full mean expense and paid finite overlap peaks

The complete original [L297](../ledger/Yin_L_G0297_v1.md) proof is retained here, with its separate degree-conditioned, tiny-total-measure and finite-peak quantifiers.
The original author check/freeze and [R776](../audits/reviews/Yin_R_G0776_v1.md#critical-delay-complete-independent-review) keep their actual dates, inputs and source/proof boundaries.

<a id="statement"></a>
## Complete statement

Let alpha be an ACTUAL nontorsion algebraic unit with minimal degree d>1 and actual order O=Z[alpha].
Use the complete original difference-digit law1/4,1/2,1/4, all p_n=Pr(sum_(j<n)eta_j alpha^j=0), p_0=1 and full first-return f_n.
Put m=log M(alpha)>0, h=lim_n -log p_n/n,R=exp h,F(z)=sum f_n z^n,a_n=R^n p_n,D_n=p_(2n)/p_n^2 for n>=1.
The actual full entropy comparison gives0<g(m)<=h<=m and F(R)<=1.
The extended sum mu_R=sum nR^n f_n is a probability-law mean only when F(R)=1.

**Entire true-critical prefix.**
If0<h<=1/64 and d>=64log(1/h), put L=log(1/h),K=floor(L/(8h)),N=d(K+1)-1.
Then, with ALL original first-return words and the TRUE radius,

    sum_(n=2)^N R^n f_n<=exp(-d/4),
    sum_(n>N)R^n f_n>=F(R)-R/2-exp(-d/4).

This is a finite-prefix estimate, not an all-length weighted-tail upper bound.
The full degree-block Holder/binomial theorem, all d(K+1) chronological terms, floors and endpoint costs are paid in the proof.

Under the ADDITIONAL recurrence premise F(R)=1, the critical law satisfies

    Pr{tau>N}>1/3,
    mu_R>d log(1/h)/(24h),
    sum_(n>=1)n^a R^n f_n
       >(1/3)[d log(1/h)/(8h)]^a for EVERY real a>0,
    limsup_n D_n>=mu_R.

Infinity is allowed; no moment divergence at a fixed input is asserted.
Only IF mu_R is finite do the fixed exact attainment/all-stationary-class criteria give the attaining original critical probability, whose zero and largest atom are
pi_*(0)=max_x pi_*(x)<24h/[d log(1/h)].
The complete critical dual convolution norm is then mu_R.
No recurrence, upper mean bound or finite-mean conclusion is proved by this theorem.

**Accepted house statement removes the degree gate on its stated domain.**
Use only the already accepted Dim19 2019v1 Theorem1 statement at its existing source scope: house(alpha)>=2^(1/(4d)), hence m>=log2/(4d).
C436's exact g(m)=log[2/(1+2^(1-exp(2m)))] obeys g(m)>=m/4 for0<=m<=1/4.
For EVERY actual input with0<m<=2^-16 this gives h>1/(24d) and d>64log(1/h), so the entire preceding theorem applies.
Set K_m=floor(log(1/m)/(8m)) and N_m=d(K_m+1)-1.
Then

    sum_(n=2)^(N_m) R^n f_n<=exp(-d/4),
    F(R)=1 => Pr{tau>N_m}>1/3,
    F(R)=1 => mu_R>d log(1/m)/(24m).

The corresponding finite-mean largest atom is less than24m/[d log(1/m)], and the convolution/limsup expense retains d log(1/m)/(24m).
These conclusions apply only to actual inputs in the given tiny-TOTAL-m domain; no such sequence is constructed.
Torsion h=0 and the retained fixed quartic outside this domain receive no new mean classification.
The source's proof, later editions and a stronger Mahler assertion are not newly audited or adopted.
Without the house statement, the full h/d-conditioned theorem and the following separate peak theorem remain.

**A separately paid finite overlap peak, without recurrence.**
For any actual nontorsion unit with0<m<=1/64, let k=floor(1/(4m)),n=dk and B=(d/2)log(1/(6m))>0.
Then a_n<exp(-B).
Let q be the full neutral REAL dimension and C_non>=1 the full nonneutral-place constant of C432, and E_t=C_non[2+sqrt(2pi t)]^q.
Choose any integer J>=1 satisfying2^-J log E_(2^J n)<=B/2, which exists for each fixed input.
The complete C555 dyadic identity then gives

    max_(0<=j<J) D_(2^j n)>(6m)^(-d/4).

The largest original return observation is p_(2^J n), with all actual order/q/C_non/degree/unknown-radius expenses retained.
No such enumeration or program ran.
This is one finite peak, not an eventual bound, a replacement for the recurrence-conditioned limsup, an infinite-mean criterion or an exponential mean lower bound.
No new source-proof audit, actual near-one family, quartic mean classification or unrestricted Mahler gap is asserted.

## Complete argument

<a id="argument"></a>

<a id="critical-delay-reuse"></a>
### 1. Reuse and the changed quantitative target

The full [C555 overlap identities](Yin_C_G0555_v1.md#dyadic-critical-normalization) were read with their corrected implication boundary: an eventual finite overlap bound is sufficient for finite critical mean, but the retained argument does not classify a single input from unbounded overlaps alone.
The reciprocal involution considered initially is already retained in [L240](../ledger/Yin_L_G0240_v1.md#critical-dual-measure-reuse) and [L198](../ledger/Yin_L_G0198_v1.md#general-unit-excursion-stationary-law); merely applying it again supplies no new estimate.
That possible direction is not developed as a new theorem here.

A more useful input is the COMPLETE degree-block estimate in [L154](Yin_C_G0365_v1.md#uniform-small-unweighted-return-tail), also retained in [L215](Yin_C_G0522_v1.md#original-binary-degree-block-holder).
Its whole original first-return mass and polynomial moments are already bounded in [L198](Yin_C_G0474_v1.md#full-unweighted-return-moment-bound).
These are reused, not rediscovered as new Fourier, Holder or binomial results.
L154's warning about exponentially weighted tails remains: small unweighted mass does not give small mass at the critical radius over ALL lengths.
The new argument instead locates a necessarily late scale for that critical mass, with a rigorous finite truncation that grows as the true entropy decreases.

The other fixed inputs are [L256's general comparison](Yin_C_G0436_v1.md#triangular-gram-collision-bound) through its equations(16)--(18), [L255's full-state expense](Yin_C_G0432_v1.md#statement), [L201's critical attainment criterion](Yin_C_G0479_v1.md#critical-excursion-attainment-condition), [L232's whole stationary-class extension](../ledger/Yin_L_G0232_v1.md#maximum-atom-fixed-scope), and [L240's full critical convolution](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test).
The only external statement used is the ALREADY accepted Dim19 v1 Theorem1 house bound, at exactly the statement/edition scope recorded in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-house) and [L80](Yin_C_G0267_v1.md#degree-only-primitive-escape).
Its original proof and any later edition are not newly audited.
That statement will only remove an explicit degree/entropy condition; the main conditional delay theorem does not depend on it.
No new source acquisition, named asymptotic theorem, numerical experiment or continuing program is used.
The local reuse screen found sufficient inputs above and makes no novelty claim.

Let alpha be an ACTUAL nontorsion algebraic unit of degree d>1, O=Z[alpha], with the original independent digits eta in{-1,0,1} of probabilities1/4,1/2,1/4.
Put

    p_n=Pr(sum_(j<n) eta_j alpha^j=0), p_0=1,
    h=lim_n -log(p_n)/n, R=exp(h),
    F(z)=sum_(n>=1) f_n z^n, a_n=R^n p_n,
    D_n=p_(2n)/p_n^2, n>=1.                              (1)

Here f_n is the COMPLETE original probability of first positive return at time n.
At the true radius, F(R)<=1.
By the fixed entropy comparison0<g(m)<=h<=m, where m=log M(alpha), h is positive; no numerical value of h or R is assumed known.
All sums at R mean increasing limits.
The mean symbol mu_R=sum nR^n f_n is allowed to be infinite; it is the mean of a probability law only when F(R)=1.
Actual stationary and convolution conclusions below explicitly require that recurrence condition.

The new conclusions are a fully quantified critical excursion delay, its near-one uniform mean consequence, and a separately paid finite certificate of large midpoint overlap.
They do not prove critical recurrence, infinite mean at a fixed nontorsion input, or a positive Mahler gap.

<a id="critical-delay-finite-mass"></a>
### 2. An entire critical prefix loses almost all nontrivial excursion mass

Write L=log(1/h).
Assume

    0<h<=1/64, d>=64L,
    K=floor(L/(8h)), N=d(K+1)-1.                       (2)

Then, including EVERY original first-return word through this chronological N,

    sum_(n=2)^N R^n f_n <=exp(-d/4).                   (3)

This is not an all-length tail estimate and it does not replace R by M in the weights.
Both N and its dependence on the unknown true h are displayed exactly.
A version using an upper parameter m will follow.

The fixed L154 proof gives f_1=1/2, f_n=0 for2<=n<=d, and, for n>=d and k=floor(n/d)>=1,

    f_n<=p_n<=b_k^d<=(3k+1)^(-d/2),
    b_k=binom(2k,k)/4^k.                               (4)

Retaining the original tilt, for kd<=n<(k+1)d this implies

    R^n f_n <=exp[d phi(k)],
    phi(x)=h(x+1)-(1/2)log(3x+1).                     (5)

The function phi is convex on[1,K], since phi''(x)=9/[2(3x+1)^2]>0.
Its maximum there is at an endpoint.
At the first endpoint,

    phi(1)=2h-log2 <=1/32-log2<-1/2.

The inequality log2>2/3 follows, for example, by the strict midpoint integral bound for1/x on[1,2].
Also L>=log64>4.
Since L/(8h)>2, floor(L/(8h))>=L/(16h).
Therefore

    h(K+1)<=L/8+h,
    log(3K+1)>=L+log(3L/16)>L-log(4/3).

Using log(4/3)<1/3 and h<=1/64 gives

    phi(K)<-3L/8+1/64+1/6<-1/2.                      (6)

Every block1<=k<=K is thus bounded by exp(-d/2).
There are at most d(K+1) chronological terms to sum.
For completeness the entire counting expense can be absorbed explicitly under(2), not omitted as a polynomial factor.
We have K+1<=L/(4h), so log(K+1)<=L+log L-log4<=2L<=d/32.
Moreover d>=64L>256, and log d<=d/32 for d>=256: equality of the bound need not hold at256, since log256=8log2<8, and log x/x decreases for x>e.
Hence

    log[d(K+1)]<=d/16,
    d(K+1)exp(-d/2)<=exp(-7d/16)<=exp(-d/4).          (7)

Summing(5) and using the exact empty first-return segment proves(3).
Rounding N downward is already in its definition; the last included block ends at d(K+1)-1.
No original word, residue class or late term within that range has been discarded without an upper bound.

More generally, without recurrence, (3) yields the exact useful separation

    sum_(n>N)R^n f_n
       >=F(R)-R/2-exp(-d/4).                          (8)

A negative right side is simply uninformative.
Transient critical inputs are not assigned F(R)=1.

<a id="critical-delay-mean-bound"></a>
### 3. Consequences for the full mean, stationary zero mass and overlap

Suppose additionally F(R)=1.
Then b_n^*=R^n f_n is a probability distribution, with mass R/2 at length one.
Since exp(1/64)<=64/63, we have R/2<=32/63.
Also d>256 implies exp(-d/4)<1/8.
Thus (8) gives the strict, fixed-fraction estimate

    Pr_(b^*){tau>N}
      >=1-R/2-exp(-d/4)>1/3.                         (9)

Indeed1-32/63-1/8=185/504>1/3.
All these estimates refer to the ORIGINAL exponentially tilted first-return weights, not to an arbitrary stationary law or an unweighted conditional return distribution.

Consequently, with infinity allowed,

    mu_R >=(N+1)Pr_(b^*){tau>N}
          >d(K+1)/3
          >d log(1/h)/(24h).                         (10)

The same argument gives every positive real moment order a:

    sum_(n>=1)n^a R^n f_n
        >(1/3)[d log(1/h)/(8h)]^a, a>0.             (11)

This does not assert moment divergence at any one input.
Unlike an upper moment estimate, it requires no upper restriction on a; the constants in the power remain exactly as written.

When mu_R<infinity, the fixed L201/L232 theorem supplies the attaining original critical kernel on the actual core, whose zero mass is1/mu_R.
Therefore

    pi_*(0)<24h/[d log(1/h)].                        (12)

The same expression bounds its largest atom because L232 proves that zero is its unique largest atom at positive measure.
L240 identifies the complete bounded critical dual convolution norm as mu_R; hence that norm exceeds the right side of(10).
If mu_R is infinite, neither an attaining probability nor a bounded convolution is asserted.
Their absence then follows at the fixed criterion's hypotheses, not from the finite calculation(3) alone.

Finally L293's correctly directed full-overlap consequence gives

    limsup_(n->infinity) D_n >=mu_R
                              >d log(1/h)/(24h).    (13)

Thus an eventual all-time arithmetic overlap upper certificate must pay at least this constant.
Equations(10)--(13) do not give an upper bound for mu_R and do not decide its finiteness.
They are stronger necessary expenses than the first-return gap's elementary linear-in-d mean bound as h decreases to zero.

<a id="critical-delay-small-total-measure"></a>
### 4. A uniform statement in the full Mahler measure

The side condition d>=64log(1/h) in(2) is automatic throughout the following actual near-one domain:

    alpha nontorsion algebraic unit,
    0<m=log M(alpha)<=2^(-16).                       (14)

Here is the full dependency and constant check.
The already accepted Dim19 v1 statement implies

    m>=log2/(4d).

L256 gives h>=g(m), with

    g(m)=log[2/(1+2^(1-exp(2m)))].

For0<=m<=1/4, direct differentiation gives

    g'(m)=2log2 exp(2m)/(1+2^(exp(2m)-1))>1/4,
    hence g(m)>=m/4.                               (15)

Indeed exp(1/2)<2, so the denominator is below3 on that range and the numerator is at least2log2>4/3.
The elementary exp(1/2)<2 follows from log2>2/3.
These are merely scalar estimates on an already fixed full-original-law theorem.
Thus under(14),

    h>=m/4>=log2/(16d)>1/(24d),
    d>1/(24h), 0<h<=m<=2^(-16).                     (16)

For0<h<=2^(-16), the function h log(1/h) is increasing, so

    h log(1/h)<=16log2/65536<1/1536.

Combining with(16) proves d>64log(1/h), and h<=1/64 is immediate.
This use of a house-scale accepted theorem does not assume a uniform Mahler gap or silently replace m by an individual root logarithm.
It only controls the relation of degree to the logarithm of the reciprocal entropy scale.

We may also state the whole finite delay without knowledge of h.
Put

    L_m=log(1/m), K_m=floor(L_m/(8m)),
    N_m=d(K_m+1)-1.                                 (17)

The function log(1/t)/t is decreasing on(0,1), so K_m<=K and N_m<=N.
Hence (3) applies to this computable-in-principle smaller prefix with the SAME true critical weights R^n.
Equivalently one may repeat the proof using R^n<=exp(mn); the degree condition d>=64L_m follows from(16) and h<=m.
We obtain, still without knowing R exactly,

    sum_(n=2)^(N_m) R^n f_n<=exp(-d/4),
    F(R)=1 => Pr_(b^*){tau>N_m}>1/3,
    F(R)=1 => mu_R>d log(1/m)/(24m).                (18)

The finite-mean consequence is pi_*(0)<24m/[d log(1/m)], and the corresponding complete convolution and limsup overlap lower expenses are d log(1/m)/(24m).
These are necessary conditions for EVERY actual input in(14) with critical recurrence, not an assertion that a sequence of such inputs exists.
They apply equally to multiple expanding conjugates.
The quartic presently retained in L169 lies outside this numerical small-m domain, so it receives no new finite/infinite mean classification here.
At h=0 the present logarithmic scales are not defined; torsion is outside the theorem rather than inserted by a limit.

The new necessary asymptotic is quantitative: along ANY hypothetical actual sequence m->0 on which critical recurrence holds,

    (mu_R/d) / [log(1/m)/m] >=1/24

in the extended sense.
If these means are finite, the critical probability's largest atom is correspondingly smaller than order m/d.
There is no contradiction: the actual core may support arbitrarily diffuse critical laws and arbitrarily large finite means.
All degree, input and unknown-radius expenses remain visible.

<a id="paid-large-dyadic-overlap"></a>
### 5. A finite, fully paid large-overlap certificate

There is a different unconditional constraint on the midpoint statistic, which does NOT require recurrence.
Let0<m<=1/64 and let alpha be an actual nontorsion unit of degree d.
Define

    k=floor(1/(4m)), n=dk,
    B=(d/2)log(1/(6m))>0.                            (19)

Then n>=d/(8m), since1/(4m)>=2.
From the complete bound(4), h<=m and k<=1/(4m),

    a_n=exp(hn)p_n
       <=[exp(mk)/(3k+1)^(1/2)]^d
       <=[exp(1/4)(8m/3)^(1/2)]^d
       <(6m)^(d/2)=exp(-B).                          (20)

The last exact comparison uses exp(1/2)<2, so exp(1/2)*8/3<16/3<6.
No bare finite p_n is used to lower-bound the limiting entropy.
This is an UPPER bound for the already normalized return a_n, with the known upper entropy h<=m.

L293's exact dyadic identity and full L255 remainder give

    H_n=sum_(j>=0)2^(-j-1)log D_(2^j n)=-log a_n>B,
    H_n-H_(n,J)<=epsilon_(n,J),
    epsilon_(n,J)=2^(-J)log E_(2^J n),
    E_t=C_non[2+sqrt(2pi t)]^q.                      (21)

Here q is the ENTIRE real neutral dimension, and C_non is the product of L255's explicit nonneutral factors.
They refer to the actual order/kernel and may be very large as the input varies.
Choose any integer J>=1 satisfying the explicit test epsilon_(n,J)<=B/2.
Such J exists for each fixed input, with no uncharged varying-input onset, because the logarithm of E_t grows at most logarithmically in t.
Then

    max_(0<=j<J) D_(2^j n) >exp(B/2)=(6m)^(-d/4).    (22)

Indeed H_(n,J)>B/2 while its positive weights sum to1-2^(-J)<1; their weighted average cannot exceed that weight sum times the maximum logarithm.
Every time in(22) is an actual original-word time.
The largest return probability used to evaluate those D values is p_(2^J n).
No computational bound is asserted beyond the fully specified finite observation horizon and the existing in-principle exact word counts.
No such enumeration ran in this round.

Unlike the earlier degree-scale initial plateau control, (22) holds throughout a conditional near-one input class and begins at chronological n of order d/m.
It shows quantitatively that any proposal bounding ALL original overlaps by a small input-independent number is already impossible on a hypothetical near-one sequence.
However it is a finite peak, not an eventual lower bound.
It cannot be substituted for(13), cannot prove infinite critical mean, and does not give an exponential lower bound for that mean.
The two statements(18) and(22) have genuinely different quantifiers and are kept separate.

<a id="critical-delay-scope-and-self-check"></a>
### 6. Scope, remaining mechanism and author self-check

The changed contribution is the full finite-window suppression of the TRUE critically tilted nontrivial first-return distribution at a scale d log(1/h)/h, its explicit conditional mean and atom consequences, and the separate paid finite dyadic peak.
The Fourier basis-block inequality, original polynomial moments, source house bound, all-time entropy comparison, dyadic telescope, full original kernel expense and critical attainment/convolution criteria remain their cited fixed premises.
Root supplied the broad question only.
No current sibling argument, including D161, entered these deductions.

This sharpens the expense of a prospective positive-recurrent critical law; it does not manufacture one or rule one out.
A new arithmetic upper estimate of order O(d/m) for its complete critical mean, uniform over the actual near-one class, would contradict(18) as m tends to zero.
Such an upper estimate is a precise new discriminating target, not a theorem, and its proof must address all sufficiently late original excursions beyond N_m.
Similarly, an eventual overlap bound of that order would be sufficient by L293 and would encounter the same contradiction.
The present argument supplies neither bound.
It also does not infer those bounds from an early plateau, a finite quotient, unweighted moment concentration or a finite peak.

The source boundary matters: without invoking the accepted Dim19 statement one still has the complete theorem(2)--(13), the explicit degree-conditioned version of(18), and the unconditional-in-recurrence finite theorem(19)--(22).
The extra small-m simplification is separately supported by the already adopted statement scope; it does not need a fresh source edition, new external proof audit or an unproved stronger Mahler bound.


## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:00 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 exact all-late overlap/dyadic theorem](Yin_C_G0555_v1.md#statement) | Complete true-radius dyadic identity/remainder and the correctly directed eventual-bound/limsup consequence only. |
| dependency | [C365 complete return bound](Yin_C_G0365_v1.md#uniform-small-unweighted-return-tail) | Actual original first-return gap and whole degree-block Holder/binomial mass bound. |
| dependency | [C522 original degree-block Holder](Yin_C_G0522_v1.md#original-binary-degree-block-holder) | Full original iid unit basis-block inequality, not a finite empirical rate. |
| dependency | [C436 exact entropy comparison](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | All-time original collision lower entropy g(m) with its exact definition and actual input scope. |
| dependency | [C432 whole-core expense](Yin_C_G0432_v1.md#statement) | All-time actual unit counting-kernel bound with full q/C_non at the actual observed times. |
| dependency | [C479 attainment criterion](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Critical recurrence/finite mean and exact rooted stationary kernel only. |
| dependency | [Original all-state maximum-atom theorem](../ledger/Yin_L_G0232_v1.md#maximum-atom-fixed-scope) | Fixed accepted extension to all stationary classes and unique maximum at zero on the finite-mean positive-measure branch. |
| dependency | [Original full convolution criterion](../ledger/Yin_L_G0240_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized to mu_R only under recurrence. |
| dependency | [Accepted Dim19 house statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing2019v1 Theorem1 house>=2^(1/(4d)) statement only; no new external proof or later edition. |
| support | [Original complete author/review input](../ledger/Yin_L_G0297_v1.md#critical-delay-reuse) | All original Sections1--6/equations1--22, actual freeze 2026-10-10T05:53 and R196 whole no-repair/source/no-program scope. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:14 |
| status | proved |
| reason | Adopt the complete retained theorem at its exact hypotheses, full costs and negative limits after actual whole current SELF of the published Statement and entire Argument; no independent arrangement or research resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 exact all-late overlap/dyadic theorem](Yin_C_G0555_v1.md#statement) | Complete true-radius dyadic identity/remainder and the correctly directed eventual-bound/limsup consequence only. |
| dependency | [C365 complete return bound](Yin_C_G0365_v1.md#uniform-small-unweighted-return-tail) | Actual original first-return gap and whole degree-block Holder/binomial mass bound. |
| dependency | [C522 original degree-block Holder](Yin_C_G0522_v1.md#original-binary-degree-block-holder) | Full original iid unit basis-block inequality, not a finite empirical rate. |
| dependency | [C436 exact entropy comparison](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | All-time original collision lower entropy g(m) with its exact definition and actual input scope. |
| dependency | [C432 whole-core expense](Yin_C_G0432_v1.md#statement) | All-time actual unit counting-kernel bound with full q/C_non at the actual observed times. |
| dependency | [C479 attainment criterion](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Critical recurrence/finite mean and exact rooted stationary kernel only. |
| dependency | [Original all-state maximum-atom theorem](Yin_C_G0560_v1.md#maximum-atom-fixed-scope) | Fixed accepted extension to all stationary classes and unique maximum at zero on the finite-mean positive-measure branch. |
| dependency | [Original full convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized to mu_R only under recurrence. |
| dependency | [Accepted Dim19 house statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing2019v1 Theorem1 house>=2^(1/(4d)) statement only; no new external proof or later edition. |
| support | [Original complete author/review input](../ledger/Yin_L_G0297_v1.md#critical-delay-reuse) | All original Sections1--6/equations1--22, actual freeze 2026-10-10T05:53 and R196 whole no-repair/source/no-program scope. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0745_v1.md#critical-delay-whole-self) | The complete current Statement and entire Argument, every selected dependency interface and all original failed-scope/source/native limits. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [C555 exact all-late overlap/dyadic theorem](Yin_C_G0555_v1.md#statement) | Complete true-radius dyadic identity/remainder and the correctly directed eventual-bound/limsup consequence only. |
| dependency | [C365 complete return bound](Yin_C_G0365_v1.md#uniform-small-unweighted-return-tail) | Actual original first-return gap and whole degree-block Holder/binomial mass bound. |
| dependency | [C522 original degree-block Holder](Yin_C_G0522_v1.md#original-binary-degree-block-holder) | Full original iid unit basis-block inequality, not a finite empirical rate. |
| dependency | [C436 exact entropy comparison](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | All-time original collision lower entropy g(m) with its exact definition and actual input scope. |
| dependency | [C432 whole-core expense](Yin_C_G0432_v1.md#statement) | All-time actual unit counting-kernel bound with full q/C_non at the actual observed times. |
| dependency | [C479 attainment criterion](Yin_C_G0479_v1.md#critical-excursion-attainment-condition) | Critical recurrence/finite mean and exact rooted stationary kernel only. |
| dependency | [Original all-state maximum-atom theorem](Yin_C_G0560_v1.md#maximum-atom-fixed-scope) | Fixed accepted extension to all stationary classes and unique maximum at zero on the finite-mean positive-measure branch. |
| dependency | [Original full convolution criterion](Yin_C_G0563_v1.md#critical-convolution-bounded-density-test) | Exact norm RFprime+1-F, specialized to mu_R only under recurrence. |
| dependency | [Accepted Dim19 house statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Existing2019v1 Theorem1 house>=2^(1/(4d)) statement only; no new external proof or later edition. |
| support | [Original complete author/review input](../ledger/Yin_L_G0297_v1.md#critical-delay-reuse) | All original Sections1--6/equations1--22, actual freeze 2026-10-10T05:53 and R196 whole no-repair/source/no-program scope. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-critical-delay) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

