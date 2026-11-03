---
author: Yin
---
# Exact first positive matched parity covariance in the original Salem quartic bridge

Date: 2026-10-12T10:16.
Human author Yin.
Internal fixed extraction under the continuing G0001 instruction.
g0001_routes authored the complete D6 argument and original J91 computation and now authors this registered statement.
The ENTIRE original author proof/history is retained below.
Separate noncontributor R355 covers the original whole D6/J91 proof/program/output and an independently authored exact finite reproduction, not this newly registered statement or its extraction interfaces.
Root will coordinate the actual extraction review and adoption separately.

## Statement

Fix the ACTUAL Salem quartic P(t)=t^4-t^3-t^2-t+1, its real root beta>1 and a neutral root zeta with |zeta|=1.
Put gamma=beta^2, Q(t)=t^4-3t^3+t^2-3t+1, tau=beta+beta^-1 and t_-= (1-sqrt13)/2, the neutral value of tau.
Relative conjugation sends beta to beta^-1.
Neutral squared norms are measured as the sum of squares of TWO unweighted real coordinates; the conjugate complex coordinate is not double-counted.

For each integer n>=1 use ORIGINAL independent digits eta_j in{-1,0,1},0<=j<2n, with probabilities1/4,1/2,1/4, and condition on COMPLETE return

    sum_(j=0)^(2n-1) eta_j beta^j=0.

Define actual parity endpoints U_e=sum_(k=0)^(n-1)eta_(2k)gamma^k and U_o=sum_(k=0)^(n-1)eta_(2k+1)gamma^k.
They satisfy U_e+beta U_o=0.
Define the chronological neutral midpoint

    X_n=-zeta^-n sum_(j=0)^(n-1) eta_j zeta^j.

Under the complete returned law let m_n=E|X_n|^2, let a_n be the expectation of the conditional covariance TRACE of X_n given BOTH complete parity endpoints, and let h_n be the covariance TRACE of those conditional means.
Global sign symmetry centers X_n, so m_n=a_n+h_n with both parts nonnegative.
These use the actual full return weights and finite opposite-block support, not just ambient fibers or order membership.

**A. Exact finite first-positive statement.** The complete parity-innovation trace satisfies

    a_n=0 for EVERY integer1<=n<=7,
    a_8=7(5+2sqrt13)/53390>0.

Thus original length16 is the FIRST positive time of THIS two-parity conditional-covariance certificate.
It is not the first positive total midpoint second moment; in particular m_6,m_7>0 and h_n=m_n at n6,7.
The n1--5 conclusion uses the exact C51 singleton-fiber proof, and n6--10 below uses the exhaustive exact finite computation, separately reproduced at that same native domain.

**B. Complete original-law finite table.** For a gamma endpoint x put W_x=sum_(a:x)2^(number of zero digits in a), summing EVERY original n-digit ternary word.
Match only y=-beta^-1x that belongs to the ACTUAL original finite gamma-word support.
Then

    C_n=sum_(matched x,y)W_x W_y,
    Pr(original return at2n)=C_n/16^n,
    Pr(U_e=x | complete return)=W_x W_y/C_n.

With t=t_- in the following exact expressions, the complete values are:

| n | C_n | matched endpoint pairs | pairs with positive innovation | m_n | a_n |
| --- | --- | --- | --- | --- | --- |
| 6 | 7296 | 75 | 0 | (115-49t)/228 | 0 |
| 7 | 35120 | 201 | 0 | (1324-547t)/2195 | 0 |
| 8 | 170848 | 539 | 8 | (3672-1560t)/5339 | (49-28t)/53390 |
| 9 | 835448 | 1435 | 42 | (399910-172945t)/522155 | (960-536t)/522155 |
| 10 | 4119392 | 3921 | 138 | (111909-48309t)/128731 | 383/111940-(7409/3861930)t |

In each row h_n=m_n-a_n; no conditional-mean term is discarded.
The corresponding numbers of COMPLETE original returned words are75,201,547,1481,4083.
Word counts are distinct from probabilities: their original unequal zero-digit weights remain in every mass and moment.
All6171 endpoint-row payloads and6387 full returned words across this fixed domain have been independently reconstructed in J91; this does not extend the native scope beyond n6--10.

**C. Explicit matched additive witness and its COMPLETE price.** At n8 take powered even words and actual odd complement

    e_a=(-1,1,-1,-1,-1,-1,0,1),
    e_b=(-1,0,1,1,1,1,-1,1),
    o  =( 1,1, 1, 0,-1,-1,-1,0).

Their common even endpoint is the ADDITIVE translation

    x=gamma*(2-4gamma-4gamma^3)+(gamma^7-1)
     =-21+54gamma-3gamma^2+60gamma^3,
    y=13-31gamma+2gamma^2-35gamma^3=-beta^-1x.

The outside digits are-1 at powered index0 and+1 at index7.
They retain legal original support and probabilities, change the index3 order residue and supply a genuinely realized finite opposite endpoint.
No pure monomial shift alone is asserted to match.

Interlacing e_a or e_b with o gives ASCENDING coefficient arrays

    f_a=(-1,1,1,1,-1,1,-1,0,-1,-1,-1,-1,0,-1,1,0),
    f_b=(-1,1,0,1, 1,1, 1,0, 1,-1, 1,-1,-1,-1,1,0),

with exact ORIGINAL polynomial identities

    f_a(t)=P(t)*(-1+t^5+t^7+t^8+t^10),
    f_b(t)=P(t)*(-1-t^2-t^3-t^5+t^10).

All original conjugate returns are therefore satisfied.
Each word has exactly three original zero digits, including its trailing zero, and thirteen nonzero digits.
Each probability is2^-29.
Their midpoint squared difference is5+2sqrt13.
The COMPLETE actual fibers have even weights2+2=4 and odd weight4 from the one displayed odd word, and C8=170848.
Hence

    conditional endpoint mass=16/170848=1/10678,
    conditional covariance trace=(5+2sqrt13)/4,
    this endpoint's exact contribution to a_8
        =(5+2sqrt13)/42712>0.

The explicit two positive original words already prove qualitative matched positivity; the exact endpoint mass and equality of this paid contribution use the complete finite fiber totals.
They are not an unweighted-overlap proxy.

**D. Actual mechanism and limitations.** Given both complete endpoints, the two original internal word laws are independent.
Their prefix cuts are ceil(n/2) and floor(n/2), and the odd contribution is multiplied by beta before taking the relative norm.
The retained proof expands both covariance parts with these factors and every original endpoint mass.
Multiplication by-zeta^-n preserves neutral squared norm, and full sign reversal justifies centering; no new law is substituted.
The explicit additive witness passes the original order gate AND actual finite complement support, escaping C51's pure-shift obstruction at this bounded scope.

The table, witness and finite onset supply no unbounded m_n, positive diffusive limsup, uniform integrability, arbitrary-input transfer or uniform Mahler gap.
Repetition of a local pair without controlling its growing actual return weights proves none of these.
The unrestricted G0001 problem remains unresolved.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:27 |
| status | proved |
| reason | Adopt the separately performed actual noncontributor extraction/interface finding together with the exact original whole-author and applicable native-review scopes. Preserve all original source/contribution/correction history and finite costs. No uniform surplus, uncomputed-time growth, expanded native domain or unrestricted Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual quartic/digit/return law, two-real-coordinate moments, exact finite onset/table/witness and every limitation. |
| argument | [Entire retained argument](#argument) | ENTIRE original D6 starting scope, Sections1--7/equations1--10, complete original-law costs, source/reuse/contribution history and17:55 freeze. |
| dependency | [Actual quartic/order and shortest fibers](Yin_C_G0051_v1.md#statement) | Accepted exact original P/Q/order/complete shortest ambiguity and pure-shift limits, with no additive-translation exclusion. |
| dependency | [Singleton fibers through length5](Yin_C_G0051_v1.md#shortest-powered-ambiguities) | Full actual endpoint uniqueness for n1--5, supplying the analytic part of the onset extension outside native n6--10. |
| dependency | [Complete endpoint covariance](Yin_C_G0045_v1.md#statement) | Actual original conditional independence, endpoint weights and retained covariance of means; no larger-time lower theorem assumed. |
| dependency | [Exact original finite J91 result](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) | The original one-run n6--10 scope, both complete groupings and saved all-row output/witness, keeping original probabilities and author-check relationship. |
| support | [Independent finite J91 reproduction](../computations/programs/Yin_J_G0091/readme.md#independent-verification-complete) | Actual independent one-run reconstruction of all6171 rows/6387 returned words at exactly n6--10, with no research range extension or future Claim acceptance. |
| support | [Original law conventions](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Original quartic, digits, chronological midpoint and two unweighted real neutral coordinates only. |
| support | [Unresolved diffusive target](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Meaning of actual complete moments and distinction from the still-open growing/diffusive lower gate, not a premise asserting growth. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) | ENTIRE original17:55 D6 plus original J91 code/output and independently authored exact reproduction; expressly excludes future fixed statement/extraction interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0795_v1.md#c55-matched-parity-actual-extraction-finding) | Actual fixed statement, complete original preservation and present mathematical/computation interfaces, inspected separately from the original whole scope. |


### Decision current-complete-moment-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:48 |
| status | proved |
| reason | Maintain the same already selected midpoint/control interface at its complete current C285 proof home. The original statement, full proof, old decisions and actual R inputs remain unchanged; no new lower-moment premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual quartic/digit/return law, two-real-coordinate moments, exact finite onset/table/witness and every limitation. |
| argument | [Entire retained argument](#argument) | ENTIRE original D6 starting scope, Sections1--7/equations1--10, complete original-law costs, source/reuse/contribution history and17:55 freeze. |
| dependency | [Actual quartic/order and shortest fibers](Yin_C_G0051_v1.md#statement) | Accepted exact original P/Q/order/complete shortest ambiguity and pure-shift limits, with no additive-translation exclusion. |
| dependency | [Singleton fibers through length5](Yin_C_G0051_v1.md#shortest-powered-ambiguities) | Full actual endpoint uniqueness for n1--5, supplying the analytic part of the onset extension outside native n6--10. |
| dependency | [Complete endpoint covariance](Yin_C_G0045_v1.md#statement) | Actual original conditional independence, endpoint weights and retained covariance of means; no larger-time lower theorem assumed. |
| dependency | [Exact original finite J91 result](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) | The original one-run n6--10 scope, both complete groupings and saved all-row output/witness, keeping original probabilities and author-check relationship. |
| support | [Independent finite J91 reproduction](../computations/programs/Yin_J_G0091/readme.md#independent-verification-complete) | Actual independent one-run reconstruction of all6171 rows/6387 returned words at exactly n6--10, with no research range extension or future Claim acceptance. |
| support | [Original law conventions](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Original quartic, digits, chronological midpoint and two unweighted real neutral coordinates only. |
| support | [Unresolved diffusive target](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Meaning of actual complete moments and distinction from the still-open growing/diffusive lower gate, not a premise asserting growth. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) | ENTIRE original17:55 D6 plus original J91 code/output and independently authored exact reproduction; expressly excludes future fixed statement/extraction interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0795_v1.md#c55-matched-parity-actual-extraction-finding) | Actual fixed statement, complete original preservation and present mathematical/computation interfaces, inspected separately from the original whole scope. |


### Decision current-complete-lower-fiber-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:36 |
| status | proved |
| reason | Maintain the same already selected original-law, endpoint-conditioned covariance or signed-square input at its complete current C300 proof home. The selected statement and proof, old decisions and actual old Review inputs remain unchanged; no new diffusive premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual quartic/digit/return law, two-real-coordinate moments, exact finite onset/table/witness and every limitation. |
| argument | [Entire retained argument](#argument) | ENTIRE original D6 starting scope, Sections1--7/equations1--10, complete original-law costs, source/reuse/contribution history and17:55 freeze. |
| dependency | [Actual quartic/order and shortest fibers](Yin_C_G0051_v1.md#statement) | Accepted exact original P/Q/order/complete shortest ambiguity and pure-shift limits, with no additive-translation exclusion. |
| dependency | [Singleton fibers through length5](Yin_C_G0051_v1.md#shortest-powered-ambiguities) | Full actual endpoint uniqueness for n1--5, supplying the analytic part of the onset extension outside native n6--10. |
| dependency | [Complete endpoint covariance](Yin_C_G0045_v1.md#statement) | Actual original conditional independence, endpoint weights and retained covariance of means; no larger-time lower theorem assumed. |
| dependency | [Exact original finite J91 result](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) | The original one-run n6--10 scope, both complete groupings and saved all-row output/witness, keeping original probabilities and author-check relationship. |
| support | [Independent finite J91 reproduction](../computations/programs/Yin_J_G0091/readme.md#independent-verification-complete) | Actual independent one-run reconstruction of all6171 rows/6387 returned words at exactly n6--10, with no research range extension or future Claim acceptance. |
| support | [Original law conventions](Yin_C_G0300_v1.md#lower-fiber-reuse-and-law) | Original quartic, digits, chronological midpoint and two unweighted real neutral coordinates only. |
| support | [Unresolved diffusive target](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Meaning of actual complete moments and distinction from the still-open growing/diffusive lower gate, not a premise asserting growth. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) | ENTIRE original17:55 D6 plus original J91 code/output and independently authored exact reproduction; expressly excludes future fixed statement/extraction interfaces. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0795_v1.md#c55-matched-parity-actual-extraction-finding) | Actual fixed statement, complete original preservation and present mathematical/computation interfaces, inspected separately from the original whole scope. |



### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:18 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Entire A--D, actual quartic/digit/return law, two-real-coordinate moments, exact finite onset/table/witness and every limitation. |
| argument | [Exact material](#argument) | ENTIRE original D6 starting scope, Sections1--7/equations1--10, complete original-law costs, source/reuse/contribution history and17:55 freeze. |
| dependency | [Exact material](Yin_C_G0051_v1.md#statement) | Accepted exact original P/Q/order/complete shortest ambiguity and pure-shift limits, with no additive-translation exclusion. |
| dependency | [Exact material](Yin_C_G0051_v1.md#shortest-powered-ambiguities) | Full actual endpoint uniqueness for n1--5, supplying the analytic part of the onset extension outside native n6--10. |
| dependency | [Exact material](Yin_C_G0045_v1.md#statement) | Actual original conditional independence, endpoint weights and retained covariance of means; no larger-time lower theorem assumed. |
| dependency | [Exact material](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) | The original one-run n6--10 scope, both complete groupings and saved all-row output/witness, keeping original probabilities and author-check relationship. |
| support | [Exact material](../computations/programs/Yin_J_G0091/readme.md#independent-verification-complete) | Actual independent one-run reconstruction of all6171 rows/6387 returned words at exactly n6--10, with no research range extension or future Claim acceptance. |
| support | [Exact material](Yin_C_G0300_v1.md#lower-fiber-reuse-and-law) | Original quartic, digits, chronological midpoint and two unweighted real neutral coordinates only. |
| support | [Exact material](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Meaning of actual complete moments and distinction from the still-open growing/diffusive lower gate, not a premise asserting growth. |
| support | [Exact material](../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) | ENTIRE original17:55 D6 plus original J91 code/output and independently authored exact reproduction; expressly excludes future fixed statement/extraction interfaces. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0795_v1.md#current-g0055-finding) | Entire A-D and all original Sections1-7/equations1-10, original law/costs, all five finite rows, actual additive witness and full native program/data scope. |

This decision adopts the complete isolated review actually formed at 2026-10-22T22:51:33 UTC and recorded at the new finding.
The fixed mathematics, status, all non-review premises and historical decisions retain their existing scope.
The retained historical findings keep their original dates, declared relationships and actual inspection limits.

## Registration and complete preservation

Date: 2026-10-12T10:16.
The original author now registers this statement and retains the ENTIRE original D6 body after only short front-matter removal, first-title demotion, exact sibling-Claim link rebasing and terminal whitespace normalization.
Every derivation, finite result, witness, original probability, failed-transfer/asymptotic boundary, source/reuse/contribution note and17:55 freeze remains.
Historical pending-review and original one-run statements are retained as the author's then-current record; subsequent R355/J91 independent verification is linked above without rewriting that history.

The native programs and complete data remain in [J91](../computations/programs/Yin_J_G0091/readme.md): author main.py/worker.py/result.json and separately authored verify.py/verification.json.
No payload was copied or native computation performed during Claim extraction.
R355 records the actual independent reconstruction of every matched row; the present author does not reclassify that verifier as formally verified or independently reviewed by a third party.
R355's original proof/native scope and the new statement/interface review remain distinct.

## Argument

## Actually matched parity fibers and additive translations in the original Salem quartic bridge

Date: 2026-10-12T09:20.
Human author Yin.
New bounded AUTHOR inquiry by g0001_routes under root's renewed parallel assignment within the unchanged G0001 execution.
Root supplies the broad target only.
This newly allocated working address inherits no former mathematics.

## Question and starting scope

Seek genuinely MATCHED parity endpoint fibers at the actual quartic P(t)=t^4-t^3-t^2-t+1, with positive COMPLETE ORIGINAL return weights, beyond [C51's shortest-fiber matching obstruction](Yin_C_G0051_v1.md#statement).
Test whether additive translations by other same-parity digits can satisfy both the exact order gate and the opposite block's actual finite digit support.
The intended bounded outcome is a checkable quantitative gain or precise failed-mechanism closure; no finite observation is a uniform or infinite-time lower bound.

Retain exact digits-1,0,1 with probabilities1/4,1/2,1/4, every complete field coordinate and return constraint, actual occupancy, original midpoint, and the difference between within-block covariance and covariance of endpoint-conditioned means.
Source and previous finite-computation reuse will be checked before any new native mathematical run.
All derivation and failures belong here.
If useful, one exact finite domain n=6,...,10 will be declared in a newly allocated responsible J with an aggregate resource cap, exact output verification and stop-on-first-failure before running; no scan or adaptive retry is presumed.
Root coordination precedes that execution.
No C adoption or old fixed proof edit is part of this assignment.

Author self-check and whole noncontributor review remain separate.

<a id="matched-parity-reuse-and-law"></a>
## 1. Reuse, complete law and the finite discriminator

The new [C51](Yin_C_G0051_v1.md#statement) preserves the exact order gate, shortest ambiguity and every shifted zero-complement example.
C45 and L335 supply the FULL original conditional-covariance decomposition, including all endpoint weights and covariance of means.
L332's actual quartic diffusive limsup criterion is the eventual target, not a lower bound assumed here.
The bounded local computation search found no retained parity-fiber/midpoint native calculation at the proposed domain; L293/L329/L335 retain proof-only exact formulas and deliberately no such finite run.
Their existing constant covariance and exponentially paid annular lower bounds are not to be rediscovered from a finite table.
This is a bounded reuse screen, not a novelty claim.

Root coordinated ONE exact experiment in [J91](../computations/programs/Yin_J_G0091/readme.md) on n=6,...,10 with180-second aggregate cap and no adaptive rerun/extension.
The domain and original weights were declared before native execution.
The candidate seeks an ADDITIVE outside-digit translation of C51's six-symbol equal-endpoint pair that is actually matchable by the other original block.
Every outside digit remains in its original allowed alphabet and probability.
A monomial shift with no additive change is already excluded and is not new evidence.

Fix P(t)=t^4-t^3-t^2-t+1, beta>1 and its actual neutral zeta; set gamma=beta^2, Q(t)=t^4-3t^3+t^2-3t+1, tau=beta+beta^-1.
Relative conjugation sigma sends beta to beta^-1.
For an actual field vector v put N_rel(v)=v sigma(v) in Q(tau).
Its evaluation at tau_-=(1-sqrt13)/2 is abs(v(zeta))^2.
Integer field vectors are represented in the COMPLETE actual power basis, not by a numerical embedding.
Every relative product is checked to lie in that trace field with the exact pair representation a+b tau.

Let nu_n be the endpoint law for gamma digits.
Integer weights are w(a)=2^(number of zeros in a) and actual word probability w(a)/4^n.
Thus a full original2n-word has denominator16^n.
Let W_x be the sum of those integer weights at endpoint x.
The matching condition is y=-beta^-1x, with BOTH x and y present in the ACTUAL finite gamma-digit support; C51's index3 gate is necessary and is explicitly checked before the support lookup.
Then

    C_n=sum_(matched x,y)W_x W_y,
    p_(2n)=C_n/16^n,
    Pr(U_even=x given full return)=W_x W_y/C_n.           (1)

Zero is included; unmatched endpoints have weight0.
No distinct-endpoint uniformization or discarded multiplicity is allowed.

<a id="matched-parity-exact-moments"></a>
## 2. Exact moment and conditional-mean formulas for the computation

For a gamma-word a define its two lower-prefix values

    L_e(a)=sum_(k<ceil(n/2))a_k gamma^k,
    L_o(a)=sum_(k<floor(n/2))a_k gamma^k.

At each full gamma endpoint x form integer-weighted first sums M_e(x)=sum_(a:x)w(a)L_e(a), M_o(x)=sum_(a:x)w(a)L_o(a), and trace-field second sums B_e(x)=sum w(a)N_rel(L_e(a)), B_o(x)=sum w(a)N_rel(L_o(a)).
These are over EVERY original word in the endpoint fiber.
At a matched pair x,y, the actual lower half of the original full word is L_e+beta L_o.
Multiplication by-beta^-n identifies the chronological midpoint; at the neutral place it is a rotation of modulus1, so it changes no squared radius or covariance trace.

Define the trace-field cross term

    K(x,y)=M_e(x)sigma(beta M_o(y))
                +sigma(M_e(x))beta M_o(y).

Conditional on BOTH endpoints, the two original block word laws are independent.
Averaging their exact squares with complete weights gives the raw total-moment contribution

    T(x,y)=W_y B_e(x)+W_x B_o(y)+K(x,y).                 (2)

Since beta sigma(beta)=1, no missing factor occurs in B_o.
With

    D(x,y)=(W_y/W_x)N_rel(M_e(x))
                 +(W_x/W_y)N_rel(M_o(y)),

its within-block conditional-covariance contribution and conditional-mean-square contribution are

    A(x,y)=W_y B_e(x)+W_x B_o(y)-D(x,y),
    H(x,y)=D(x,y)+K(x,y),
    T(x,y)=A(x,y)+H(x,y).                               (3)

All expressions are exact elements of Q(tau); their neutral embeddings are nonnegative where they represent squares or variance.
The complete returned law is centered by sign reversal, so after summing and dividing by C_n, T gives the actual midpoint second moment, A the two-block innovation trace and H the covariance-of-conditional-means trace.
These equations are the existing total-covariance law applied to exact COMPUTABLE finite weights.
They are a justified reduction for this experiment, not by themselves a new quantitative theorem.
The proposed new information must be in an actually matched positive witness or the exact bounded table.

For a separate complete check, enumerate original beta words of length n, with endpoint weight Z_x.
Match x+beta^n y=0.
Then the SAME probability numerator is sum Z_x Z_y and the same squared midpoint numerator is sum Z_x Z_y N_rel(x): the factor-beta^-n is neutral unit modulus.
These contiguous-half sums must agree EXACTLY with(1)--(2), and use neither the parity matching formula nor a saved prior output as an oracle.

<a id="matched-additive-witness-certificate"></a>
## 3. Exact candidate certification and its quantitative meaning

The candidate replaces the segment a_(A,B)=(A,-1,-1,-1,-1,B) by b_(A,B)=(A-1,1,1,1,1,B-1), A,B in{0,1}, at a strictly midpoint-crossing powered shift j, preserving every outside same-parity digit.
Its even endpoint is gamma^j x_(A,B)+z, with the exact outside translation z.
Both full even words must be legal and have the same endpoint.
An actual odd word must realize-beta^-1 times that endpoint.
The resulting TWO full interlaced ORIGINAL words must each divide exactly by the ORIGINAL P; actual coefficient arrays, quotient and zero remainder are saved.

If the even words have integer weights w_a,w_b, the actual full even/odd endpoint totals are W_x,W_y>0, and h is their neutral midpoint difference, two ordered terms in the pairwise-variance identity give the ACTUAL complete within-block contribution lower bound

    w_a w_b W_y/(W_x C_n) * abs(h)^2 >0.                (4)

This includes the actual endpoint probability W_xW_y/C_n and is not an ambient-only fiber assertion.
The program records the exact trace-field pair for abs(h)^2 and exact positive multiplier; signs are decided in Q(sqrt13) by rational comparisons, never floating approximations.
This lower bound is at that finite n.
Repetition of a fixed local pair or a growing table supplies no linear-in-n asymptotic without an additional theorem.

All five n are mandatory even after the first witness.
Candidate selection uses the complete predeclared deterministic order; a failed execution remains incomplete and no parameter retry is implicit.
No native mathematical execution has occurred at this written reduction.

<a id="matched-parity-finite-result"></a>
## 4. Completed exact finite result and all original costs

The declared [J91 calculation](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) completed on 2026-10-12.
It enumerated 88,209 words in each grouping, 176,418 total visits, at exactly n=6,7,8,9,10.
Every word has its original weight and full field coordinates; the complete output (`mathematics/computations/outputs/Yin_J_G0091/result.json`) retains matched endpoint aggregates rather than an expanded listing of all words.
No parameter extension or floating mathematical decision is involved.

Write t=tau_-=(1-sqrt13)/2.
Let m_n be the ACTUAL original returned midpoint second moment, a_n its complete two-parity conditional-covariance trace and h_n its covariance-of-conditional-means trace, all with the conventions of Section2.
Thus m_n=a_n+h_n, with each quantity evaluated in the two unweighted real neutral coordinates.
The following are exact outputs, not rounded estimates or unweighted endpoint averages.

| n (original length2n) | C_n | matched endpoint pairs | pairs with positive a contribution | m_n | a_n |
| --- | --- | --- | --- | --- | --- |
| 6 (12) | 7296 | 75 | 0 | (115-49t)/228 | 0 |
| 7 (14) | 35120 | 201 | 0 | (1324-547t)/2195 | 0 |
| 8 (16) | 170848 | 539 | 8 | (3672-1560t)/5339 | (49-28t)/53390 |
| 9 (18) | 835448 | 1435 | 42 | (399910-172945t)/522155 | (960-536t)/522155 |
| 10 (20) | 4119392 | 3921 | 138 | (111909-48309t)/128731 | 383/111940-(7409/3861930)t |

The original return probabilities C_n/16^n, in the same order, are57/131072,2195/16777216,5339/134217728,104431/8589934592,128731/34359738368.
The actual numbers of full return words are75,201,547,1481,4083.
Word counts are not probabilities: the unequal zero-digit weights remain in every moment.
For example, at n=8 the nonzero total innovation is exactly

    a_8=7(5+2sqrt13)/53390>0.                           (5)

The complete conditional-mean trace is m_n-a_n, not a discarded residual.
It equals ALL of m_n at n=6,7 even though m_n>0.
No inference from the smallness or growth of these finite values is made at uncomputed n.

For each n, the separately implemented contiguous-half grouping reproduced EXACTLY the complete return mass, the count of full return words, and the total raw neutral second moment.
Its unique beta-endpoint counts were525,1267,2901,6451,13989.
Its raw moment pairs, in the a+b tau basis before neutral evaluation, were(3680,-1568),(21184,-8752),(117504,-49920),(639856,-276712),(3581088,-1545888), each equal to the complete parity total.
Sign reversal gave exactly zero total first moment.
All asserted variance/squared-mean signs and a_n+h_n=m_n were checked by exact arithmetic.
This is one author's two-grouping crosscheck, not an independent review or a second independently authored implementation.

<a id="matched-positive-additive-witness"></a>
## 5. A genuinely matched additive translation with positive full return weight

The first candidate in the declared order occurs at n=8, shift j=1, A=1,B=0.
Its actual even words and actual odd complement are

    e_a=(-1,1,-1,-1,-1,-1,0,1),
    e_b=(-1,0,1,1,1,1,-1,1),
    o  =( 1,1, 1, 0,-1,-1,-1,0).                       (6)

The outside even digits are-1 at index0 and+1 at index7.
Thus the additive translation is z=gamma^7-1, and the common even endpoint is

    x=gamma*x_(1,0)+z,
    x_(1,0)=2-4gamma-4gamma^3,
    z=-25+64gamma-3gamma^2+72gamma^3,
    x=-21+54gamma-3gamma^2+60gamma^3,
    y=13-31gamma+2gamma^2-35gamma^3=-beta^-1x.           (7)

These are all actual complete power-basis identities.
The old shifted endpoint gamma*x_(1,0)=4-10gamma-12gamma^3 fails the index3 order test: evaluating its reduced representative at-1 gives26, congruent to-1 modulo3.
The outside translation's reduced representative evaluates at-1 to-164, congruent to+1 modulo3.
The new reduced total evaluates to-138, divisible by3.
More importantly, (6) explicitly realizes the opposite endpoint y in the same finite original digit support.
Passing the order test alone would not suffice.

Interlacing these actual even and odd words gives original coefficient arrays in ASCENDING powers:

    f_a=(-1,1,1,1,-1,1,-1,0,-1,-1,-1,-1,0,-1,1,0),
    f_b=(-1,1,0,1, 1,1, 1,0, 1,-1, 1,-1,-1,-1,1,0).

They obey the explicit integer polynomial identities

    f_a(t)=P(t)*(-1+t^5+t^7+t^8+t^10),
    f_b(t)=P(t)*(-1-t^2-t^3-t^5+t^10).                (8)

Direct multiplication proves complete original return at beta and every conjugate.
The leading coefficient at index15 is zero; it is an original random zero digit and its probability is retained.
Each full word contains exactly three zero digits and thirteen nonzero digits, hence has probability(1/2)^3(1/4)^13=2^-29.
Equivalently, both even words have integer weight2, the odd word has integer weight4, and each full word has weight8 over16^8=2^32.
The outside digits are legal and have not been replaced by an arbitrary field translation or a free deterministic shift.

At the original midpoint time8, the even prefix ends after powered index3.
The difference of these two even prefixes is gamma*(1-2gamma-2gamma^2).
At the neutral root put omega=zeta^2 and v=omega+omega^-1=(3-sqrt13)/2=t+1.
Since v^2=3v+1 and both the leading omega and the chronological midpoint factor-zeta^-8 have modulus1,

    abs(h_mid)^2=abs(1-2omega-2omega^2)^2
               =13+2v-2v^2=7-4t=5+2sqrt13>0.         (9)

The explicit words, positive original weights, full matching and (9) already prove that the actual conditional parity covariance is positive at n=8.
This qualitative positivity does not require trusting the exhaustive counts: any additional fiber words leave a positive pairwise-variance term.
The following EXACT quantitative coefficient does use the complete enumeration, which reports W_x=4,W_y=4 and C_8=170848.
The two even weights2+2 exhaust W_x, and the one odd weight4 exhausts W_y; since every legal word has positive weight, these are the entire actual fibers.
Consequently

    Pr(U_even=x | original full return)=16/170848=1/10678,
    Var(midpoint | these endpoints)=(5+2sqrt13)/4,
    this endpoint's actual innovation contribution
        =(5+2sqrt13)/42712>0.                          (10)

Here variance denotes the trace in the two real neutral coordinates.
Equation(10) is an equality for this one matched endpoint, as well as a strict lower bound for the complete a_8.
It is not an ambient conditional variance with its matching weight omitted.

<a id="matched-parity-onset-and-boundaries"></a>
## 6. Precise finite onset, failed controls and remaining gate

Combining the [accepted shortest-fiber classification](Yin_C_G0051_v1.md#shortest-powered-ambiguities) with the complete finite calculation gives the following author result, still awaiting independent whole review:

**Finite onset statement.** For the actual original quartic and original1/4,1/2,1/4 digit law, condition the two parity blocks of a length2n word on their complete actual endpoints and then on complete original return.
The resulting sum a_n of conditional covariance traces is zero for every integer1<=n<=7 and positive at n=8, with exact value(5).
In particular original length16 is the first positive time for THIS specified parity-innovation certificate.

For n<=5 every gamma endpoint fiber is a singleton by C51, so its conditional covariance is zero.
For n=6 C51's only ambiguous endpoints have no possible original complement; this agrees with J91's complete zero output.
For n=7 the conclusion is the complete exact finite computation, not an unproved extrapolation of the six-symbol classification.
At n=8 either the explicit matched witness proves positivity or the exact complete sum(5) does so.
The word "first" concerns this parity certificate only: it says nothing about the first positive TOTAL midpoint second moment, which is already positive in the n=6,7 rows and is then carried entirely by endpoint-conditioned means.

The new mechanism succeeds at a boundary left open by C51.
Its additive outside digits change both order membership and actual complement support, whereas all pure monomial shifts of the shortest ambiguous endpoint remain dead by C51.
It supplies positive COMPLETE return-weighted covariance and finite n-dependent exact information.
It does not prove unbounded m_n, a positive limsup of m_n/n, a uniform integrability statement, a uniform Mahler gap, or any transfer to an arbitrary algebraic input.
Repeating this one local witness or counting a larger family without its exact occupancy and return probabilities would not establish those claims.
The asymptotic gate remains to control a genuinely growing collection of matched fibers or the actual endpoint-conditioned means, with all original weights at increasing n.
No extension or further experiment is started here.

<a id="matched-parity-complete-author-selfcheck"></a>
## 7. Complete author self-check, sources and review boundary

The author checked the reduction against [C45's complete original-law formula](Yin_C_G0045_v1.md#statement), [L335's actual covariance conventions](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization), and [L332's true diffusive target](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization).
C51 supplies the actual P/Q/order/shortest-fiber and no-monomial-complement inputs at the linked scopes.
No new recognized external theorem, literature artifact or source-status premise is used.
The original two real neutral coordinates are retained; a complex coordinate and its conjugate are not separately double-counted.

Both executed source files were read in full; the saved output's scope, all five summary records, execution fields and complete candidate were inspected, while the full matched-row data remain available for separate review.
The primary grouping uses all four gamma coordinates, integer original weights, the exact order divisibility condition and actual opposite support.
It retains both unequal prefix cuts at odd n, the beta factor in the cross term, all endpoint-conditioned means, every matched row and exact positivity signs.
The separately implemented contiguous grouping uses original beta Horner steps and inverse-beta steps, and compares total mass, full-word counts and total second moment.
Algebra helpers are shared inside one author program; no claim of independent implementation or independent proof review follows from its passing comparisons.

The witness check retains all original coefficients including trailing zeros, both complete P divisions, exact outside occupancy, strict midpoint crossing, original weights and full finite endpoint totals.
The simple analytic multiplication and squared-norm derivation above supplement the native checks without rerunning the mathematical computation.
No native mathematical run beyond the ONE declared J91 execution occurred.
Reading its saved JSON and file metadata is operational inspection, not a new experiment.

The author contribution is the new additive-matching inquiry, the exact reduction specialized to its finite computation, both program groupings, the native experiment and all arguments written here.
Root supplied only the broad research target and execution-scope coordination, not a proof step, code, mathematical correction or independent verdict.
Earlier C45 extraction and C51 authorship are disclosed dependencies, not independent validation of this extension.
Structural material checks and this self-check do not adopt a Claim or replace whole noncontributor review of the written argument, executable sources and saved output.

<a id="matched-parity-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T09:55.
The COMPLETE starting scope, Sections1--7, equations(1)--(10), finite onset statement, complete original-law costs, source/reuse/contribution history and all positive/failed/unresolved boundaries are AUTHOR-FROZEN together with the J91 declaration, executed main.py/worker.py and complete native mathematical result.
The original operational reports were inspected at that author handoff, without creating a permanent archive requirement.
At the original handoff, the source and native evidence were unchanged during inspection; the subsequent source-layout/storage maintenance is not a new independent review.
The scoped D6/J91 check returned checked2 before this freeze and is repeated afterward.
The actual outcome is a positive matched additive fiber and exact finite covariance/onset data, not a diffusive lower bound.
Whole noncontributor written/program/output review is pending, and no fixed adoption is asserted.

This bounded inquiry is frozen at its review handoff; no extra mathematical experiment or exploration was performed by this author.

## Historical assessments

<a id="decision-initial"></a>

### Historical assessment initial

| Field | Value |
| --- | --- |
| date | 2026-10-12T10:16 |
| status | proof draft |
| review-status | under review |
| reason | Register the exact original-law first positive two-parity certificate, complete n6--10 table and actual matched additive witness with every original probability/cost and the entire original proof retained. R355 independently covers the original whole D6/J91 scope and exact finite reproduction only; this new author-written statement/extraction awaits actual noncontributor review. No asymptotic or unrestricted result is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, actual quartic/digit/return law, two-real-coordinate moments, exact finite onset/table/witness and every limitation. |
| argument | [Entire retained argument](#argument) | ENTIRE original D6 starting scope, Sections1--7/equations1--10, complete original-law costs, source/reuse/contribution history and17:55 freeze. |
| dependency | [Actual quartic/order and shortest fibers](Yin_C_G0051_v1.md#statement) | Accepted exact original P/Q/order/complete shortest ambiguity and pure-shift limits, with no additive-translation exclusion. |
| dependency | [Singleton fibers through length5](Yin_C_G0051_v1.md#shortest-powered-ambiguities) | Full actual endpoint uniqueness for n1--5, supplying the analytic part of the onset extension outside native n6--10. |
| dependency | [Complete endpoint covariance](Yin_C_G0045_v1.md#statement) | Actual original conditional independence, endpoint weights and retained covariance of means; no larger-time lower theorem assumed. |
| dependency | [Exact original finite J91 result](../computations/programs/Yin_J_G0091/readme.md#completed-exact-parity-run) | The original one-run n6--10 scope, both complete groupings and saved all-row output/witness, keeping original probabilities and author-check relationship. |
| support | [Independent finite J91 reproduction](../computations/programs/Yin_J_G0091/readme.md#independent-verification-complete) | Actual independent one-run reconstruction of all6171 rows/6387 returned words at exactly n6--10, with no research range extension or future Claim acceptance. |
| support | [Original law conventions](../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Original quartic, digits, chronological midpoint and two unweighted real neutral coordinates only. |
| support | [Unresolved diffusive target](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Meaning of actual complete moments and distinction from the still-open growing/diffusive lower gate, not a premise asserting growth. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0795_v1.md#matched-parity-whole-independent-finding) | ENTIRE original17:55 D6 plus original J91 code/output and independently authored exact reproduction; expressly excludes future fixed statement/extraction interfaces. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0091](../computations/programs/Yin_J_G0091/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
