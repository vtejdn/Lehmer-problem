---
author: Yin
---
# Exact original-quartic parity matching obstruction and macroscopic dead fibers

Date: 2026-10-12T09:05.
Human author Yin.
Provenance: project deduction.
Internal fixed extraction under the continuing unchanged G0001 contract.
The ENTIRE original D4 proof and author history are retained below.
The separate R252 whole finding covers the original16:53 freeze only; this actual registered statement and its fixed interfaces require their own review.
The extractor previously provided that noncontributor whole review but contributes this NEW wrapper and cannot independently review its own extraction.

## Statement

Fix the ACTUAL monic irreducible Salem quartic P(t)=t^4-t^3-t^2-t+1, real root beta>1 and nonreal unit-circle conjugate zeta.
Set gamma=beta^2, omega=zeta^2, O=Z[beta] and O2=Z[gamma].
Then gamma has ACTUAL degree4 minimal polynomial Q(t)=t^4-3t^3+t^2-3t+1, its other roots are gamma^-1,omega,conjugate(omega), and2<gamma<3 while beta^3>3.
These are the SAME original field but possibly different orders.

At every length N, use independent ORIGINAL digits eta_j in{-1,0,1} with probabilities1/4,1/2,1/4, with no tilting or law replacement.
Define nu_l as the actual finite O2-endpoint law of sum_(k=0)^(l-1)eta_k gamma^k, with nu_0 concentrated at0 and every nu_l zero off its actual finite support.
For an original length2n word, set U_even=sum_(k<n)eta_(2k)gamma^k, U_odd=sum_(k<n)eta_(2k+1)gamma^k, U_total=U_even+beta U_odd and p_(2n)=Pr(U_total=0)>0.
The original neutral midpoint is Z=-zeta^-n sum_(r<n)eta_r zeta^r; its even-coordinate contribution is Z_even=-zeta^-n sum_(2k<n)eta_(2k)omega^k, viewed in TWO unweighted real neutral coordinates.

**A. Actual parity-order gate and original return weights.**
The exact identities are

    beta=(-gamma^3+4gamma^2-2gamma+2)/3,
    beta^-1=(-2gamma^3+5gamma^2+2gamma+4)/3.

For x=r(gamma) in O2 with ordinary integer representative deg r<4,

    beta^-1 x in O2 iff r(-1)=0 mod3,
    O2 intersection beta O2=(3,gamma+1), of index3 in O2.

Membership and nonmembership are invariant under EVERY integer power of gamma.
The COMPLETE original parity conditioning gives

    p_(2n)=sum_x nu_n(x)nu_n(-beta^-1 x),
    Pr(U_even=x given U_total=0)
             =nu_n(x)nu_n(-beta^-1x)/p_(2n).

Order membership alone does not make the second factor positive.

**B. Coarse strides reveal digits rather than average them.**
For a real b>=3, the endpoint map from finite ternary words to sum a_j b^j is injective; the same holds for exponent gaps>=h when beta^h>=3.
Thus every residue-class block of stride h>=3 at the ORIGINAL beta has3^l distinct endpoints at l digits and original entropy(3l/2)log2.
Its endpoint determines every digit.
Conditioning on all such block endpoints makes every within-block covariance zero, and the conditional-mean observable is the original midpoint itself.
This is a precise absence of averaging, not a new covariance bound or independent-increment assertion.

**C. COMPLETE shortest stride-two ambiguity and its probabilities.**
For lengths<=5 every gamma endpoint is unique.
At length6 the ONLY nonzero word differences are plus/minus

    D(t)=(1+t)Q(t)=1-2t-2t^2-2t^3-2t^4+t^5.

There are exactly FOUR ambiguous endpoint fibers, each of exactly TWO words.
With A,B in{0,1} and difference oriented as D, they are

    a_(A,B)=(A,-1,-1,-1,-1,B),
    b_(A,B)=(A-1,1,1,1,1,B-1),
    x_(A,B)=(A+1-3B)+(8B-4)(gamma^3+gamma).

All four endpoints are distinct and NONZERO.
Their original word probabilities are2^(-10-A-B),2^(-12+A+B), respectively.
For A=B the fiber probability is5/4096 and conditional weights are1/5,4/5 in the appropriate order; for A!=B the fiber probability is1/1024 and both conditional weights are1/2.
The uniqueness of the ZERO endpoint word at gamma>2 is not confused with uniqueness of arbitrary endpoints.

**D. No finite original complement for any shortest ambiguous endpoint or monomial shift.**
For EVERY A,B in{0,1}, EVERY integer j and EVERY finite l>=0,

    nu_l(-beta^-1 gamma^j x_(A,B))=0.

For A!=B this follows from the exact order gate.
For A=B the endpoints are plus/minus x, where x=4gamma^3+4gamma-1, and beta^-1x=Y=2gamma^3+gamma^2+2gamma has NO finite Laurent representation with coefficients-1,0,1.
The proof uses the ACTUAL contracting embedding to exclude every negative exponent, then expanding dominance to bound degree by4 and exclude all possible integer quotients.
The conclusion covers all finite lengths and all monomial shifts, but NOT arbitrary additive translations by other same-parity digits.

**E. Every-even-n positive ambient covariance with exact zero returned weight.**
For EVERY even n=2l>=6, put j=l-3.
Insert a_(1,1) or b_(1,1) into the even-block positions k=j,...,j+5 and set all other even digits zero.
Their actual even-block probabilities are a_n=2^(-n-6),b_n=2^(-n-4), and their common endpoint is gamma^j x.
Their neutral midpoint difference is

    h_mid=omega^2-2omega-2,
    |h_mid|^2=5+2sqrt13.

With V_n=nu_n(gamma^j x)>0, original-law center maximality and the powered zero-word identity give V_n<=nu_n(0)=2^-n.
Therefore

    tr Cov(Z_even given U_even=gamma^j x)
       >=(a_n b_n/V_n^2)(5+2sqrt13)
       >=(5+2sqrt13)/1024,
    Pr(U_even=gamma^j x given U_total=0)=0.

This ambient nonzero-endpoint covariance requires neither a centered fiber nor completeness of its larger-n word list.
The positive fiber contributes ZERO to C45's actually return-weighted certificate and to the returned endpoint distribution.
No positive all-ambient-supported-fiber complement comparison, even with a positive n-dependent factor, can hold for this mechanism.
Nothing upper-bounds other fibers, the actual total midpoint covariance, or a law first restricted to truly matchable fibers.

**F. Positive-match guard and exact limits.**
The original P-word has legal nonzero even endpoint1-gamma+gamma^2=beta(gamma+1) and odd endpoint-(1+gamma).
Zero padding inside a sufficiently large original word gives a nonzero endpoint with positive matching return weight.
Thus D--E do not exclude all nonzero fibers.
The whole result concerns this FIXED original quartic and exact original probabilities.
It supplies no diffusive lower moment, critical-mean classification, near-one transfer, unrestricted gap or Task completion.

## Current assessment
[Selected decision](#decision-current-complete-general-block-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:05 |
| status | open |
| reason | Register the exact original-quartic order, complete shortest-fiber, no-Laurent-complement and every-even-n conditional-weight conclusions, retaining the ENTIRE original author proof/history. R252 covers only the original16:53 whole freeze. The actual registered statement, selected fixed argument, interfaces and complete preservation await a separate noncontributor extraction finding. No moment-growth or Task-completion claim is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--F, actual original quartic/degree/order, full finite digits and all parity weights, every Laurent shift, every even n>=6, fixed-input scope and all limitations. |
| argument | [Entire original proof](#argument) | ENTIRE D4 Sections1--8/Lemmas1--3/Theorem4/equations1--16, starting question, reuse/source/contribution history, full16:53 freeze and final execution paragraph. |
| dependency | [Current complete endpoint certificate](Yin_C_G0045_v1.md#statement) | Exact original-law disjoint/interlaced endpoint weights and conditional covariance; only interpretation of zero weighted contribution, not an upper bound on total covariance. |
| dependency | [Actual squared Salem control](../ledger/Yin_L_G0332_v1.md#actual-salem-zero-bridge-control) | ACTUAL Q irreducibility/degree/root configuration and gamma>2, original zero-word law; no transfer of its total measure to original beta. |
| dependency | [Original law and midpoint](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Exact original P/beta/zeta,1/4,1/2,1/4 digits and neutral midpoint -zeta^-n first-half sum, as two unweighted real coordinates. |
| dependency | [Center maximality and covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Finite original binary-autocorrelation/Cauchy--Schwarz bound and correct conditional covariance accounting, retaining all complement probabilities. |
| support | [Fixed-input moment significance](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Only context for why a genuine diffusive lower bound would matter; no such bound or critical-mean premise is imported. |
| support | [General original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Existing full-conjugate/unweighted-real/original-probability conventions only; no new amplification premise. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0252_v1.md#quartic-decimation-whole-independent-finding) | ENTIRE exact original16:53 D4 proof at its recorded noncontributor scope only; not a review of this newly authored registered statement or fixed interfaces. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T09:20 |
| status | proved |
| reason | Adopt the separate noncontributor actual registered-statement, complete-preservation and selected-interface finding, alongside the exact whole-author review. Retain all original proofs, corrections, contribution and source limits, actual costs and historical assessments. The supplied-profile, finite-class or fixed-input scopes do not establish unrestricted Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--F, actual original quartic/degree/order, full finite digits and all parity weights, every Laurent shift, every even n>=6, fixed-input scope and all limitations. |
| argument | [Entire original proof](#argument) | ENTIRE D4 Sections1--8/Lemmas1--3/Theorem4/equations1--16, starting question, reuse/source/contribution history, full16:53 freeze and final execution paragraph. |
| dependency | [Current complete endpoint certificate](Yin_C_G0045_v1.md#statement) | Exact original-law disjoint/interlaced endpoint weights and conditional covariance; only interpretation of zero weighted contribution, not an upper bound on total covariance. |
| dependency | [Actual squared Salem control](../ledger/Yin_L_G0332_v1.md#actual-salem-zero-bridge-control) | ACTUAL Q irreducibility/degree/root configuration and gamma>2, original zero-word law; no transfer of its total measure to original beta. |
| dependency | [Original law and midpoint](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Exact original P/beta/zeta,1/4,1/2,1/4 digits and neutral midpoint -zeta^-n first-half sum, as two unweighted real coordinates. |
| dependency | [Center maximality and covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Finite original binary-autocorrelation/Cauchy--Schwarz bound and correct conditional covariance accounting, retaining all complement probabilities. |
| support | [Fixed-input moment significance](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Only context for why a genuine diffusive lower bound would matter; no such bound or critical-mean premise is imported. |
| support | [General original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Existing full-conjugate/unweighted-real/original-probability conventions only; no new amplification premise. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0252_v1.md#quartic-decimation-whole-independent-finding) | ENTIRE exact original16:53 D4 proof at its recorded noncontributor scope only; not a review of this newly authored registered statement or fixed interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0255_v1.md#c51-quartic-parity-extraction-finding) | Actual registered statement, complete retained argument and present selected interfaces, checked separately from the original whole-author freeze. |


### Decision current-complete-moment-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:48 |
| status | proved |
| reason | Maintain the same already selected midpoint/control interface at its complete current C285 proof home. The original statement, full proof, old decisions and actual R inputs remain unchanged; no new lower-moment premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--F, actual original quartic/degree/order, full finite digits and all parity weights, every Laurent shift, every even n>=6, fixed-input scope and all limitations. |
| argument | [Entire original proof](#argument) | ENTIRE D4 Sections1--8/Lemmas1--3/Theorem4/equations1--16, starting question, reuse/source/contribution history, full16:53 freeze and final execution paragraph. |
| dependency | [Current complete endpoint certificate](Yin_C_G0045_v1.md#statement) | Exact original-law disjoint/interlaced endpoint weights and conditional covariance; only interpretation of zero weighted contribution, not an upper bound on total covariance. |
| dependency | [Actual squared Salem control](Yin_C_G0285_v1.md#actual-salem-zero-bridge-control) | ACTUAL Q irreducibility/degree/root configuration and gamma>2, original zero-word law; no transfer of its total measure to original beta. |
| dependency | [Original law and midpoint](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Exact original P/beta/zeta,1/4,1/2,1/4 digits and neutral midpoint -zeta^-n first-half sum, as two unweighted real coordinates. |
| dependency | [Center maximality and covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Finite original binary-autocorrelation/Cauchy--Schwarz bound and correct conditional covariance accounting, retaining all complement probabilities. |
| support | [Fixed-input moment significance](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Only context for why a genuine diffusive lower bound would matter; no such bound or critical-mean premise is imported. |
| support | [General original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Existing full-conjugate/unweighted-real/original-probability conventions only; no new amplification premise. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0252_v1.md#quartic-decimation-whole-independent-finding) | ENTIRE exact original16:53 D4 proof at its recorded noncontributor scope only; not a review of this newly authored registered statement or fixed interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0255_v1.md#c51-quartic-parity-extraction-finding) | Actual registered statement, complete retained argument and present selected interfaces, checked separately from the original whole-author freeze. |


### Decision current-complete-lower-fiber-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:36 |
| status | proved |
| reason | Maintain the same already selected original-law, endpoint-conditioned covariance or signed-square input at its complete current C300 proof home. The selected statement and proof, old decisions and actual old Review inputs remain unchanged; no new diffusive premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact A--F, actual original quartic/degree/order, full finite digits and all parity weights, every Laurent shift, every even n>=6, fixed-input scope and all limitations. |
| argument | [Entire original proof](#argument) | ENTIRE D4 Sections1--8/Lemmas1--3/Theorem4/equations1--16, starting question, reuse/source/contribution history, full16:53 freeze and final execution paragraph. |
| dependency | [Current complete endpoint certificate](Yin_C_G0045_v1.md#statement) | Exact original-law disjoint/interlaced endpoint weights and conditional covariance; only interpretation of zero weighted contribution, not an upper bound on total covariance. |
| dependency | [Actual squared Salem control](Yin_C_G0285_v1.md#actual-salem-zero-bridge-control) | ACTUAL Q irreducibility/degree/root configuration and gamma>2, original zero-word law; no transfer of its total measure to original beta. |
| dependency | [Original law and midpoint](Yin_C_G0300_v1.md#lower-fiber-reuse-and-law) | Exact original P/beta/zeta,1/4,1/2,1/4 digits and neutral midpoint -zeta^-n first-half sum, as two unweighted real coordinates. |
| dependency | [Center maximality and covariance](Yin_C_G0300_v1.md#returned-block-convolution-minorization) | Finite original binary-autocorrelation/Cauchy--Schwarz bound and correct conditional covariance accounting, retaining all complement probabilities. |
| support | [Fixed-input moment significance](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Only context for why a genuine diffusive lower bound would matter; no such bound or critical-mean premise is imported. |
| support | [General original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Existing full-conjugate/unweighted-real/original-probability conventions only; no new amplification premise. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0252_v1.md#quartic-decimation-whole-independent-finding) | ENTIRE exact original16:53 D4 proof at its recorded noncontributor scope only; not a review of this newly authored registered statement or fixed interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0255_v1.md#c51-quartic-parity-extraction-finding) | Actual registered statement, complete retained argument and present selected interfaces, checked separately from the original whole-author freeze. |



### Decision current-complete-general-block-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T14:40 |
| status | proved |
| reason | Maintain the same complete original-mass/full-conjugate returned-block input at its actual complete C370 proof home. The selected theorem/proof and existing whole finding remain unchanged; the original historical inputs and decisions remain exact. No new lower-moment or amplification premise is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact A--F, actual original quartic/degree/order, full finite digits and all parity weights, every Laurent shift, every even n>=6, fixed-input scope and all limitations. |
| argument | [Complete selected argument](#argument) | ENTIRE D4 Sections1--8/Lemmas1--3/Theorem4/equations1--16, starting question, reuse/source/contribution history, full16:53 freeze and final execution paragraph. |
| dependency | [Exact accepted input](Yin_C_G0045_v1.md#statement) | Exact original-law disjoint/interlaced endpoint weights and conditional covariance; only interpretation of zero weighted contribution, not an upper bound on total covariance. |
| dependency | [Exact accepted input](Yin_C_G0285_v1.md#actual-salem-zero-bridge-control) | ACTUAL Q irreducibility/degree/root configuration and gamma>2, original zero-word law; no transfer of its total measure to original beta. |
| dependency | [Exact accepted input](Yin_C_G0300_v1.md#lower-fiber-reuse-and-law) | Exact original P/beta/zeta,1/4,1/2,1/4 digits and neutral midpoint -zeta^-n first-half sum, as two unweighted real coordinates. |
| dependency | [Exact accepted input](Yin_C_G0300_v1.md#returned-block-convolution-minorization) | Finite original binary-autocorrelation/Cauchy--Schwarz bound and correct conditional covariance accounting, retaining all complement probabilities. |
| support | [Exact support](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Only context for why a genuine diffusive lower bound would matter; no such bound or critical-mean premise is imported. |
| support | [Exact support](Yin_C_G0370_v1.md#general-returned-block-reuse) | Existing full-conjugate/unweighted-real/original-probability conventions only; no new amplification premise. |
| support | [Exact support](../audits/reviews/Yin_R_G0252_v1.md#quartic-decimation-whole-independent-finding) | ENTIRE exact original16:53 D4 proof at its recorded noncontributor scope only; not a review of this newly authored registered statement or fixed interfaces. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0255_v1.md#c51-quartic-parity-extraction-finding) | Actual registered statement, complete retained argument and present selected interfaces, checked separately from the original whole-author freeze. |

## Argument

The ENTIRE original author account follows.
Only its short author front matter is removed and its first title is demoted by one heading level.
Every other word, proof, source/contribution note, original freeze, final execution paragraph and edge newline is preserved.
Existing relative links resolve from this fixed home without any locator rebasing.
Original pending-review and allocation language remain historical, not a substitute for this Claim's Current assessment.
The present extractor's earlier R252 finding remains independent at its original whole-D scope; creating this wrapper makes the extractor a contributor to the new registered statement and bars a self-supplied independent extraction verdict.

## Original quartic endpoint-conditioned means beyond the small-block innovation barrier

Date: 2026-10-12T08:35.
Human author Yin.
Responsible bounded AUTHOR inquiry by g0001_routes under the continuing G0001 instruction and root's parallel original-law assignment.
Root gives the broad target only.
This is a newly allocated working address; no prior use of its serial is inherited.

## Question and actual starting scope

Seek a genuinely quantified contribution from covariance of endpoint-conditioned means, or an actual mesoscopic/macroscopic endpoint law, for the ORIGINAL returned digit process at the Salem quartic P(t)=t^4-t^3-t^2-t+1.
The goal of this bounded inquiry is a new n-dependent diffusive lower estimate, or a precise failed mechanism with the original return weights, full field constraints, actual constants and missing implication retained.

Read and reuse [C45's complete endpoint-fiber barrier](Yin_C_G0045_v1.md#statement), [L332's actual midpoint discriminator](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization), [L335's original conditional covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization), [C370's fixed-unit returned-block scope](Yin_C_G0370_v1.md#statement), and the exact current [S7 continuation](../strategies/Yin_S_G0007.md#current-complete-fiber-continuation).
Additional direct interfaces and previous failed recipes will be checked before sustained proof work.

No theorem is asserted at allocation.
The inquiry must not rename total covariance, recover the unknown law through a singleton/whole-word tautology, add overlapping certificates without weights, substitute an upper Gaussian proxy for actual covariance, or drop original endpoint/return probabilities.
Every substantive attempt, successful or failed, will be retained below.
No native mathematical program, numerical scan or continuing computation is authorized without a separately declared J scope coordinated with root.
No C adoption or fixed-material mutation is part of this author assignment.

Author checking and separate noncontributor review remain distinct.

<a id="decimation-reuse-and-changed-test"></a>
## 1. Reuse, failed earlier mechanisms and the new precise test

The current C45 statement, original proof and adopted decision were read, as were L332's actual original law, complete projection upper proxy, uniform-integrability/diffusive discriminator and actual higher-house Salem control; L335's original endpoint weights, center-maximum proof, fixed positive covariance floor, annular lower-tail price and signed-fiber boundary; and S2/S7's new continuation.
The relevant L353/C45 conditional-mean and arbitrary-endpoint distinctions were also checked.
The local G-material screen included decimation, parity, stride, lacunary support, actual two-block means and powered endpoint injectivity.
It found the existing paired-reflection candidate C6, which is a different decomposition with an unproved coupled arithmetic gate, and L332's exact higher-house quartic below.
No novelty or exhaustive search claim is made.

The tested candidate is REGULAR DECIMATION: reveal endpoints of the two interlaced parity blocks, or of three or more residue-class blocks.
One might hope that their endpoint-conditioned means/fibers are simpler than the complete original bridge and that positive ambient fiber covariance can be transferred with a controlled complement probability.
The new discriminator is whether a fiber is ACTUALLY MATCHABLE by the other original block, including its order membership and full finite digit representation.
This is a necessary arithmetic condition before any covariance or entropy transfer.

The whole original bridge is not replaced by a Gaussian proxy.
The elementary digit-dominance proof used in [L332's actual Salem control](../ledger/Yin_L_G0332_v1.md#actual-salem-zero-bridge-control) is reused, with a crucial distinction: absence of a nonzero zero-word uses coefficients at most1 and a base above2; uniqueness of an arbitrary ternary endpoint uses DIFFERENCE coefficients at most2 and needs the stronger base at least3.
Confusing these thresholds would incorrectly discard all nonzero fibers.
The bounded test below proves that stride2 really has nonzero ambiguous fibers, but its shortest such fibers have ZERO exact whole-return weight at every admissible shifted placement.
No new external theorem, native program or numerical experiment supplies any step.

<a id="actual-quartic-power-and-order"></a>
## 2. Actual squared input and exact parity matching order

Keep the ACTUAL original irreducible Salem quartic

    P(t)=t^4-t^3-t^2-t+1, beta>1,
    tau=beta+beta^-1=(1+sqrt13)/2,
    zeta+zeta^-1=(1-sqrt13)/2.

Set gamma=beta^2 and omega=zeta^2.
Then gamma+gamma^-1=tau^2-2=tau+1=(3+sqrt13)/2, so gamma is the ACTUAL degree4 input of L332's control:

    Q(t)=t^4-3t^3+t^2-3t+1,
    roots gamma,gamma^-1,omega,conjugate(omega).             (1)

Its irreducibility and Salem status are already proved there, not inferred from numerical squaring.
Since 3<(3+sqrt13)/2<10/3, monotonicity of x+x^-1 for x>1 gives 2<gamma<3.
Also tau>13/6, hence beta>3/2 and beta^3>27/8>3.
These are strict exact inequalities.
No degree drop, new trace convention or original-law normalization is introduced.

Let O2=Z[gamma], O=Z[beta].
They are actual monogenic orders in the SAME field.
From P(beta)=0 one obtains

    beta=(gamma^2-gamma+1)/(gamma+1)
         =(-gamma^3+4gamma^2-2gamma+2)/3,
    beta^-1=(-2gamma^3+5gamma^2+2gamma+4)/3.                (2)

The first fractional-polynomial identity follows by reducing with Q; the second follows by division by gamma and Q's unit identity gamma^-1=-gamma^3+3gamma^2-gamma+3.
Thus O2 is not silently identified with O.

**Lemma 1 (exact order gate).**
For ANY x=r(gamma) in O2, with its unique ordinary integer representative deg r<4,

    beta^-1 x in O2  iff  r(-1)=0 mod3.                   (3)

Equivalently O2 intersection beta O2 is the index3 ideal (3,gamma+1) of O2.
Formula(3) is invariant under multiplication by any integral power of gamma.

*Proof.*
O2 is the free integer module on1,gamma,gamma^2,gamma^3.
By(2), beta^-1x is in it exactly when the remainder of B(t)r(t) modulo Q is coefficientwise divisible by3, where B=-2t^3+5t^2+2t+4.
Over F3,

    Q=(t-1)^2(t+1)^2,
    B=(t-1)^2(t+1).

Consequently Q divides Br over F3 exactly when t+1 divides r.
That is r(-1)=0 mod3, proving(3).
Evaluation at-1 modulo3 maps O2 onto F3 because Q(-1)=9; its kernel is (3,gamma+1), proving the ideal/index claim.
Since gamma is a unit of O2 and has value-1 modulo this ideal, multiplying by gamma^j preserves kernel membership for every integer j.
No conductor formula, maximal-order assumption or nonarchimedean norm bound is invoked.

For the ORIGINAL length2n word, write its digits in ascending exponent order and split

    U_even=sum_(k=0)^(n-1)eta_(2k)gamma^k,
    U_odd=sum_(k=0)^(n-1)eta_(2k+1)gamma^k,
    U_total=U_even+beta U_odd.

The two block endpoint laws are the SAME finite law nu_n of sum_(k<n)eta_k gamma^k, with original digit probabilities1/4,1/2,1/4.
The EXACT original return probability and conditional even-endpoint weights are

    p_(2n)=sum_x nu_n(x)nu_n(-beta^-1x),
    w_n(x)=nu_n(x)nu_n(-beta^-1x)/p_(2n).                 (4)

All sums are over actual O2 values; nu_n is zero off its actual finite support.
In particular w_n(x)=0 outside the ideal in(3), even if nu_n(x)>0.
Neither a field vector nor order membership alone suffices for a positive matching probability.

<a id="coarse-decimation-no-compression"></a>
## 3. Why three or more regular residue blocks provide no averaging

**Lemma 2.**
If b>=3 is real, the map from any finite ternary word to sum_j a_j b^j is injective.
More generally powers with successive exponent gaps at least h are injective when beta^h>=3.

*Proof.*
A nonzero difference has coefficients in{-2,-1,0,1,2}.
If its top occupied exponent is k, the leading term has magnitude at least b^k, whereas the absolute sum below it is at most2(b^k-1)/(b-1)<=b^k-1.
Thus it cannot vanish.
For gap h compare the decreasing geometric tail of ratio beta^-h; the same strict finite-tail estimate applies after a monomial factor.
Empty/singleton supports cause no exception.

At the target beta, every residue class modulo h>=3 has step beta^h>3.
Therefore its endpoint determines ALL its digits.
Conditioning on every such block endpoint leaves zero within-block conditional covariance, and the conditional mean of the original midpoint is the midpoint itself.
The residual covariance-of-means equals the unknown actual covariance.
This proves the precise failure of this proposed coarse decimation, rather than using that tautology as a new estimate.
Even before return conditioning, a residue block of l digits has3^l distinct endpoints and retains the full digit entropy (3l/2)log2; revealing it compresses none of those digits.
Under exact return the endpoint vector and word remain in bijection.
No independent-increment or summable-covariance conclusion follows.

Stride2 is genuinely different because2<gamma<3.
The next section establishes its first actual ambiguity rather than extending Lemma2 across the wrong threshold.

<a id="shortest-powered-ambiguities"></a>
## 4. Complete classification of the shortest squared-input fibers

**Lemma 3.**
For ternary words in gamma of length at most5 every endpoint is unique.
At length6 the ONLY nonzero differences between two words with the same endpoint are plus or minus

    D(t)=(1+t)Q(t)=1-2t-2t^2-2t^3-2t^4+t^5.            (5)

There are exactly FOUR ambiguous endpoint fibers at length6; each has exactly TWO words.
Orient the difference as D and choose A,B in{0,1}.
The pair is

    a_(A,B)=(A,-1,-1,-1,-1,B),
    b_(A,B)=(A-1,1,1,1,1,B-1).                         (6)

Their common endpoint is

    x_(A,B)=A-(gamma+gamma^2+gamma^3+gamma^4)+B gamma^5
           =(A+1-3B)+(8B-4)(gamma^3+gamma).             (7)

All four are distinct and nonzero.

*Proof.*
Any difference polynomial of degree<4 vanishing at gamma is zero by actual minimality.
At degree4 it is aQ, whose coefficient-3a cannot lie in[-2,2] for nonzero integer a.
At degree<=5 it is Q(a+bt), with coefficients

    (a,b-3a,a-3b,b-3a,a-3b,b).

The endpoint coefficients give abs a,abs b<=2.
If either had absolute value2, a middle coefficient would have absolute value at least4, contradiction.
Thus a,b belong{-1,0,1}.
Exactly one nonzero entry would give a coefficient of absolute value3, and opposite nonzero signs would give4.
The only remaining nonzero choices are a=b=+/-1, proving(5).
The middle difference-2 forces the four middle digit pairs(-1,1); each end difference+1 has exactly the two choices in(6).
Reversing a pair gives-D and introduces no new fiber.
A third distinct member would force a pair difference2D, which is impossible at a middle coefficient.
The four endpoints are distinct since gamma^5>1; they occur in opposite pairs by(7) and cannot be zero because gamma>2 admits no nonzero ternary zero-word.
Reduction in(7) uses gamma^4=3gamma^3-gamma^2+3gamma-1 and gamma^5=8gamma^3+8gamma-3.

The original word probabilities at length6 are

    Pr(a_(A,B))=2^(-10-A-B),
    Pr(b_(A,B))=2^(-12+A+B).                            (8)

Thus the two A=B fibers have probability5/4096 and conditional weights1/5,4/5 in the appropriate order.
The two A!=B fibers have probability1/1024 and equal conditional weights1/2,1/2.
These are actual NONZERO endpoint fibers even though the only ZERO endpoint word at this powered input is the all-zero word.
The coefficient1 versus2 distinction is essential.

<a id="shortest-fibers-unmatchable"></a>
## 5. Every shortest ambiguous endpoint has zero complete-return weight

**Theorem 4.**
For EVERY A,B in{0,1}, EVERY integer j, and EVERY finite original odd-block length l,

    nu_l(-beta^-1 gamma^j x_(A,B))=0.                    (9)

In particular every feasible monomial shift of each shortest ambient even-block ambiguity has EXACT weight zero in(4), at every complete word length.
This concerns the specified endpoints and all their monomial shifts, not arbitrary additive translations by other same-parity digits.

*Proof for A!=B.*
By(7), the ordinary representative evaluated at-1 is congruent to A-B modulo3, which is nonzero.
Lemma1 excludes membership of beta^-1x in O2.
Its monomial shifts remain excluded.
Every finite odd endpoint lies in O2, so the probability in(9) is zero, independent of length.

*Proof for A=B.*
The two endpoints are plus and minus

    x=4gamma^3+4gamma-1,
    beta^-1x=Y:=2gamma^3+gamma^2+2gamma.                 (10)

The second equality follows from beta=(gamma^2-gamma+1)/(gamma+1): expanding (gamma^2-gamma+1)Y-(gamma+1)x gives a multiple of Q, hence zero.
Equivalently it follows directly from(2) and Q.
We show that Y has NO finite Laurent representation with coefficients-1,0,1; symmetry then handles-Y and multiplication by gamma^j handles every shift.

First such a representation cannot contain a negative exponent.
At the contracting embedding gamma->gamma^-1 its prescribed value is

    Y_minus=2gamma^-3+gamma^-2+2gamma^-1>0.

If the lowest exponent were-k with k>=1, its leading magnitude at that embedding would be gamma^k.
The sum of ALL later possible magnitudes is strictly less than gamma^k/(gamma-1).
Thus the absolute endpoint would exceed gamma^k(gamma-2)/(gamma-1), at least gamma(gamma-2)/(gamma-1).
But

    gamma(gamma-2)/(gamma-1)-Y_minus
      =(3gamma^2+gamma+1)/[gamma^3(gamma-1)]>0.          (11)

To verify(11), multiply by its positive denominator and use Q: the numerator before reduction is gamma^5-2gamma^4-2gamma^3+gamma^2-gamma+2, whose remainder is3gamma^2+gamma+1.
This is a contradiction.
Using the ACTUAL contracting conjugate is indispensable; a real expanding-place estimate alone does not exclude negative exponents.

Now all exponents are nonnegative.
If the largest exponent is k, its absolute value is at least

    L_k=gamma^k-sum_(a<k)gamma^a.

For gamma>2 the positive sequence L_k strictly increases, since L_(k+1)=gamma L_k-1 and L_0=1.
At k=5 the reduction of Q gives

    L_5=4gamma^3+4gamma-3,
    L_5-Y=2gamma^3-gamma^2+2gamma-3>0.                  (12)

The last inequality follows directly from gamma>2.
Consequently a representation of Y would have degree<=4.
Such an integer polynomial differs from the degree3 polynomial Y by aQ; its leading coefficient forces a in{-1,0,1}.
Its coefficients would be

    (a,2-3a,1+a,2-3a,a).

For a=0 or-1 the second coefficient is respectively2 or5; for a=1 the middle coefficient is2.
None is a ternary word.
Thus no finite Laurent representation exists, proving(9).

Order membership alone therefore eliminates two fibers, while the other two pass the order gate but fail ACTUAL digit representability at both real embeddings.
Replacing the odd law by a nonzero density on all of O2 would incorrectly create positive whole-return weights.

<a id="uniform-positive-ambient-dead-fiber"></a>
## 6. Positive midpoint fiber covariance with exact zero original matching weight

The obstruction remains visible at arbitrarily large midpoint times, not merely at a fixed short word.
Let n=2l>=6 and j=l-3>=0.
In the complete ORIGINAL length2n bridge, the even coordinates are2k,0<=k<n.
Insert either of the two words a_(1,1),b_(1,1) of(6) into its even-digit positions k=j,...,j+5, with all other even digits zero.
Both are legal and have common nonzero even endpoint gamma^j x.
Their full even-block ORIGINAL probabilities are

    a_n=2^(-n-6), b_n=2^(-n-4).                        (13)

The complete neutral midpoint observable is Z=-zeta^-n sum_(r<n)eta_r zeta^r.
The two even-block midpoint values differ by

    h=-omega^-3(1-2omega-2omega^2)
      =omega^2-2omega-2,
    abs h^2=5+2sqrt13>0.                              (14)

Indeed the cut lies immediately after the third digit of the inserted powered word.
The equality in(14) is D(omega)=0.
For the squared modulus put v=omega+omega^-1=(3-sqrt13)/2, so v^2=3v+1; direct multiplication gives abs h^2=13+2v-2v^2=5+2sqrt13.
These are two REAL neutral coordinates, not a doubled full-norm convention.

Let V_n=nu_n(gamma^j x)>0.
The original binary-difference/Cauchy--Schwarz identity recalled in L335 gives nu_n(t)<=nu_n(0).
Since gamma>2, only the all-zero original ternary word returns at gamma, so nu_n(0)=2^-n.
The two ordered pair terms in the elementary conditional-variance identity therefore imply the ACTUAL ambient even-fiber bound

    tr Cov(Z_even given U_even=gamma^j x)
        >=(a_n b_n/V_n^2)abs h^2
        >=(5+2sqrt13)/1024.                            (15)

This is a genuine positive covariance of a nonzero endpoint fiber of a MACROSCOPIC parity block.
No completeness claim about that fiber or independent increments was needed: two actual words suffice for the lower bound, and center maximality supplies the paid denominator upper bound.

Nevertheless Theorem4 gives

    Pr(U_even=gamma^j x given original length2n return)=0.  (16)

Consequently this entire positive fiber contributes ZERO to C45's actually weighted within-block certificate and to the covariance-of-means decomposition under return.
Equations(15)--(16) hold for EVERY even n>=6.
They rule out any positive all-supported-fiber complement-matching lower comparison for this parity mechanism, even with an n-dependent positive factor: its proposed right side at this actual fiber is positive while the true left side is zero.
They do not upper-bound the other fibers, the actual midpoint covariance or a law restricted in advance to truly matched fibers.

For an elementary positive-match guard, the original P word has even endpoint1-gamma+gamma^2=beta(gamma+1) and odd endpoint-(1+gamma).
Both are original legal ternary sums; after enough zero padding this gives a positive nonzero matched fiber.
Thus the theorem does not assert that all nonzero endpoints are excluded.
That finite control gives no growing midpoint estimate, and no new early numerical moment is claimed.

<a id="decimation-outcome-and-next-discriminator"></a>
## 7. Outcome and next discriminator

The original attempted shortcut was to move beyond C45's small-block limitation by decimating into large interlaced blocks and transferring available positive ambient fiber covariance/mean information through a generic complement comparison.
The test fails at a precise actual scope.
Three or more regular residue blocks reveal every digit and offer no averaging.
Two parity blocks have genuine nonzero ambiguity, but ALL four shortest ambiguous endpoints and all their monomial shifts have exactly zero matching weight in the complete original law.
Even a uniform positive ambient neutral covariance floor at these fibers does not survive conditioning on return.

The new positive content is the exact index3 parity-order gate, complete shortest-ambiguity classification and original probabilities, an all-shift two-real-embedding nonrepresentability proof, and the explicit every-even-n contrast(15)--(16).
This is not a restatement of total covariance or a claim that a failed sufficient method settles the original process.
It eliminates an actual proposed transfer and identifies a sharper next question: build ADDITIVELY TRANSLATED or otherwise different parity fibers that simultaneously satisfy the index3 order gate AND the actual opposite-block digit support, then prove an n-dependent lower covariance or conditional-mean contribution with their full weights.
A membership test alone or positive ambient covariance alone is insufficient.
C45's larger-block option and the truly matched covariance-of-means direction remain open.

No positive diffusive limsup, unbounded actual second moment, critical-mean classification or unrestricted G0001 gap is proved.
L332's actual quartic moment test remains the target rather than a premise.
All constants and statements above concern this fixed original quartic.
No assertion transfers its squared-control total measure to the original task's unrestricted near-one class.

<a id="decimation-complete-author-selfcheck"></a>
## 8. Complete author self-check and review boundary

The author checked the complete Sections1--7/Lemmas1--3/Theorem4/equations1--16.
The exact checks covered original P versus squared Q and their actual degree/conjugates; both exact real-base thresholds and the distinct coefficient1/2 dominance requirements; beta and beta^-1 polynomial expressions, free O2 basis, modulo3 factorization, the precise ideal/index and invariance under every integer gamma power; complete original parity law and its beta multiplier; all short quotient coefficients, the four and only four fibers, original probabilities and two conditional weight patterns; both nonmembership cases; the exact x/beta identity; contracting-embedding exclusion of ALL negative Laurent exponents, strict finite geometric tail and the numerator in(11); expanding dominance, monotonic L_k, the degree4 remainder and all three possible quotients; every integer shift and the explicit exclusion of arbitrary additive translations.

The midpoint check retained n=2l>=6, valid j=l-3 placement inside the actual even block, exactly three digits below the original midpoint, the unit-modulus rotation, the D(omega) identity, the exact squared length5+2sqrt13, original padded word probabilities, conditional-pair covariance without centering a nonzero fiber, center maximality at the ACTUAL powered zero-word law, the factor1/1024, and the zero complement probability at every stated n.
A legal nonzero matched P-word guards against overextending the support obstruction.
No actual covariance upper bound, hidden mean classification, growing-moment claim, near-one transfer or model-law substitution was made.

All new derivations and proposed decimation tests are by g0001_routes for Yin.
Root supplied only the broad parallel target and received progress reports, with no proof step or correction.
This author's prior C45 extraction and C46 independent extraction review are disclosed upstream activities and are not an independent review of the present new proof.
The arguments here use only the explicitly retained project interfaces and elementary algebra/probability proved locally; no new external theorem or source acceptance is needed.
No native mathematical computation, solver, enumeration, J or proof assistant was run.
Scoped material validation returned checked1 on the complete Sections1--7 before this self-check/freeze addition and is repeated afterward; it is not proof review.

<a id="decimation-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T08:53.
The COMPLETE Sections1--8, Lemmas1--3, Theorem4, equations1--16, all source/reuse/contribution accounts, actual original-law costs, failed transfer and precise continuation boundary are AUTHOR-FROZEN after the complete self-check.
This bounded test did not produce a diffusive lower bound.
It produced the exact actual-law matching obstruction and all-time ambient/conditioned contrast stated above.
The whole proof awaits a separately organized noncontributor review; no fixed adoption or independent pass is asserted.


The author inquiry is frozen at the mathematical scope above.

## Registration and preservation operation

2026-10-12T09:05.
Human author Yin.
Under the explicit continuing G0001 organization instruction, the assigned extractor read the full original D4 and R252, stated the exact reusable result above, and retained the ENTIRE source account.
[D4](#decimation-entire-author-freeze) is extraction ancestry only, not mutable selected proof support.
No mathematics, original author/source/contribution status, probability cost or pending-history assertion was rewritten.
Only front-matter removal and the first-title level change were used; even original edge newlines are retained inside the source span.
Original D4 and R252 remain unchanged.
This operation performs no native mathematical computation or new exploration.
