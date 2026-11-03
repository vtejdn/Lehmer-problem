---
author: Yin
---
# Original quartic conditional-resampling energy and exact parity nonclosure

Date: 2026-10-12T11:26.
Human author Yin.
Internal fixed extraction under the continuing G0001 authorization.
The rounding-recovery author of the complete D13 also authors this exact statement and wrapper and cannot independently review either.
Root's actual separate whole R271 covers the original combined19:09 author body only.
This 2026-10-12 author preface records the extraction before its later wrapper/interface finding; the current selected decision and that R account state the actual adopted scope and relationship.
The entire original proof, both freezes, dated source-access resolution and actual role history are retained below.
No adoption, retirement or new mathematics is performed here.

## Statement

Fix the ACTUAL irreducible Salem quartic P(t)=1-t-t^2-t^3+t^4, real root beta>1, gamma=beta^2 and a nonreal unit-circle conjugate zeta.
Put u=zeta+zeta^-1=(1-sqrt13)/2, so u^2=u+3.
Neutral norms use exactly TWO unweighted real coordinates.
For every integer n>=4 set N=2n and L=2n-4.
Let Omega_n consist of EVERY lengthN word eta in{-1,0,1}^N with complete original field return F_eta(beta)=0, where F_eta=sum_(r=0)^(N-1)eta_r t^r.
All independent original digit probabilities remain1/4,1/2,1/4, including every zero digit and every previous return.
Define

    W_n=sum_(eta in Omega_n)2^z(eta)>0,
    p_(2n)=W_n/4^(2n), pi_n(eta)=2^z(eta)/W_n,

where z(eta) counts original zeros.
Each word has a UNIQUE integer quotient F_eta=P A_eta, A_eta=sum_(j=0)^(L-1)a_j t^j.
Conversely, every integer quotient whose product has all N digits legal is included, without a quotient-coefficient cutoff.

**A. Exact coordinate law and original stationary operator.**
For each0<=j<L, let K_j resample a_j from its exact conditional law under pi_n given all other quotient coordinates.
The legal values are a consecutive set of one, two or three integers.
Their conditional weights are proportional to2^(number of zero affected digits), so their variances are respectively0; 2^b/(1+2^b)^2 for an odd b in{-5,-3,-1,1,3,5}; or1/17 with three-point weights(1,32,1)/34.
If

    v_j(n)=E_(pi_n)Var(a_j | a_-j),

then at EVERY site and n>=4,

    1/512<=v_j(n)<=2/9.

These are averaged conditional bounds and do not assert a positive variance on each fiber or connectivity.
The random-site operator

    T_n=(1/L)sum_j K_j

is reversible for the EXACT pi_n and is a self-adjoint positive contraction.
Its real Dirichlet form is

    E_n(g,g)=<g,(I-T_n)g>_(pi_n)
            =(1/L)sum_j E_(pi_n)Var(g | a_-j)
            =(1/2)E[(g(a')-g(a))^2]

for a stationary one-update pair.
Every update adds an integer multiple of a shifted ORIGINAL P and preserves all original conjugate returns and all digit constraints.

**B. Exact midpoint coefficients and all-n update energy.**
The chronological neutral midpoint and its second moment are

    Z_n=-zeta^-n sum_(r=0)^(n-1)eta_r zeta^r,
    E_(pi_n)Z_n=0, m_n=E_(pi_n)|Z_n|^2.

With p_r the five coefficients of P, put w_k=-zeta^-k sum_(r=0)^(k-1)p_r zeta^r for1<=k<=4.
Exactly four quotient coordinates contribute:

    Z_n=sum_(k=1)^4 w_k a_(n-k),
    |w_1|^2=|w_4|^2=1,
    |w_2|^2=|w_3|^2=2-u,
    C_star=sum_k|w_k|^2=5+sqrt13.

Consequently the full two-coordinate update energy satisfies

    D_n=E_n(Re Z_n,Re Z_n)+E_n(Im Z_n,Im Z_n)
       =(1/L)sum_(k=1)^4 |w_k|^2 v_(n-k)(n),
    C_star/[512(2n-4)]<=D_n<=2C_star/[9(2n-4)].

This uses ONE uniformly selected site per update.
For each site updating at unit rate the energy is L D_n, between C_star/512 and2C_star/9.
The 1/L factor is a specified auxiliary clock; it is not a chronological variance-growth result.

**C. Gap direction and explicitly conditional mean implication.**
Define the global gap

    lambda_n=inf_(Var_pi_n(g)>0) E_n(g,g)/Var_pi_n(g) in[0,1].

Reducibility gives lambda_n=0; no irreducibility is assumed.
The old original-law bound m_n>=1/512 and the new energy identity give

    lambda_n m_n<=D_n,
    lambda_n<=min{1,1024C_star/[9(2n-4)]}.

At any n for which m_n>=epsilon n, epsilon>0,

    lambda_n<=2C_star/[9 epsilon n(2n-4)].

Thus diffusive lower midpoint growth would require a same-subsequence O(n^-2) upper gap bound; a small gap does not imply that growth.
If the ADDITIONAL premise

    some c>0 and n0 satisfy lambda_n>=c/(2n-4)
    for EVERY n>=n0

were to hold, then m_n<=2C_star/(9c) eventually.
The full original midpoint laws would be tight on the actual rank-four Minkowski lattice, using the original fixed expanding/contracting strips, and the original chronological critical first-return mean mu would be FINITE by the accepted complete-state tightness interface.
Equivalently,

    mu=infinity implies liminf_(n->infinity)(2n-4)lambda_n=0.

The positive lower-gap premise is not asserted; none of A or B relies on it.
The chronological critical chain and this auxiliary conditional-resampling chain are different.
No finite/infinite mean branch is decided by this statement.
The original conditional formulation and its proof are preserved regardless of later work on whether its premise can hold.

**D. Complete parity increments, failure of closure and paid stationary discrepancy.**
For every original returned word define

    U_e=sum_(r=0)^(n-1)eta_(2r) gamma^r,
    U_o=sum_(r=0)^(n-1)eta_(2r+1) gamma^r,
    Pi=(U_e,U_o), U_e+beta U_o=0,
    E0=1-gamma+gamma^2=beta(1+gamma)>0,
    O0=-(1+gamma).

These are actual finite-support endpoints in Z[gamma]; O0 denotes the increment here, not a ring.
A quotient update by delta at site j has exact endpoint increments

    Delta U_e=delta(-beta)^j E0,
    Delta U_o=-beta^-1 Delta U_e.

A projected Markov chain valid for every starting word requires and is characterized by equality of all exit sums T_n(a,Pi^-1(B)) within each source Pi-class.
That finite row-sum criterion is proved locally in the retained argument.
It fails for the following exact n8 C55 words:

    f_a=(-1,1,1,1,-1,1,-1,0,-1,-1,-1,-1,0,-1,1,0),
    f_b=(-1,1,0,1,1,1,1,0,1,-1,1,-1,-1,-1,1,0).

Their shared complete Pi-class consists of exactly these two words, of equal within-class probability1/2 and total ORIGINAL return-conditioned mass1/10678.
For B=Pi(f_a)+(E0,O0),

    T_8(f_a,Pi^-1(B))=4/51,
    T_8(f_b,Pi^-1(B))=0.

The first is the exact legal site0 removal of -P with conditional probability16/17 and site choice1/12; the second is blocked by its two end-digit constraints.
No other site or nonzero integer delta reaches B, because delta(-beta)^j=1 is impossible for j>=1.
The target class is actually nonempty.

Let Q_n be the pi_n-orthogonal conditional expectation onto functions of Pi.
The stationary averaged endpoint kernel Q_n T_n Q_n exists and is reversible, but on its range

    Q_n T_n^2 Q_n-(Q_n T_n Q_n)^2
       =Q_n T_n(I-Q_n)T_n Q_n>=0.

For n8 and g=1_(Pi^-1(B)), the paid discrepancy is

    <g,[Q_8 T_8^2 Q_8-(Q_8 T_8 Q_8)^2]g>_(pi_8)
        >=4/(2601*10678)>0.

Therefore the actual parity-projected process is not Markov even when the full chain starts in pi_8; its stationary one-step average cannot give its actual two-step law.
This does not preclude a separately designed endpoint chain with the same marginal.
The finite witness and its full original mass are reused at C55's accepted scope, without any new native computation.

The result concerns this fixed original quartic and exact auxiliary operator.
It supplies neither a growing lower bound on m_n nor an unbounded/diffusive limsup, a critical-mean classification, a uniform-degree transfer or an unrestricted Mahler gap.
Classical naming is credited through the precise LP17/TK06 access accounts retained below; no unread external mixing or positive-gap theorem is a premise.

## Current assessment
[Selected decision](#decision-current-complete-lower-fiber-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:26 |
| status | open |
| reason | Register the complete original-law operator, exact all-n update energy, explicitly conditional gap-to-mean implication and full stationary parity nonclosure, retaining the entire combined19:09 D13. R271 independently reviews that original body only. The original author also wrote this wrapper, so this actual extraction and its precise interfaces require a different independent reviewer. No lower-gap premise, mean branch or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--D above, at the actual quartic and complete original unequal-probability return law; every n>=4 estimate, conditional implication and exact n8 stationary nonclosure. |
| argument | [Entire retained author account](#argument) | Complete D13 question/reuse/roles, Sections1--9/equations1--17, original18:55 freeze and19:09 source supplement/freeze, with every probability, conditional premise and source-access limit. |
| dependency | [C55 complete finite witness](Yin_C_G0055_v1.md#statement) | Only the exact n8 two-word complete parity class, original arrays and divisibility, equal within-class weights and full class mass1/10678. No asymptotic inference or new native run. |
| dependency | [Original returned-block minorization](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Every actual coordinate set with its FULL complement and original return probability, used for the averaged lower coordinate variance. |
| dependency | [Actual five-digit law and midpoint floor](../ledger/Yin_L_G0335_v1.md#quartic-uniform-positive-covariance) | p5=17/512, three-block probabilities and actual two-coordinate m_n>=1/512 for n>=4, with original signs and weights. |
| dependency | [Complete-state tightness and chronological mean](../ledger/Yin_L_G0329_v1.md#complete-midpoint-tightness-test) | ONLY the conditional mean implication: actual recurrent quartic, full real strips/rank-four lattice, eventual full-state tightness implies finite original chronological critical mean. |
| support | [Original combined-body whole independent finding](../audits/reviews/Yin_R_G0271_v1.md#quartic-local-dynamics-whole-independent-finding) | Entire original D13 combined19:09 body and actual accepted direct interfaces. It does not inspect this new statement/wrapper or prospectively adopt this Claim. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:45 |
| status | proved |
| reason | Adopt the separately performed original whole R271 and actual extraction R276 findings at their exact original-law/operator/source scopes. The full original proof, both freezes and partial source limits remain. No unproved gap premise, chronological mean classification or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--D above, at the actual quartic and complete original unequal-probability return law; every n>=4 estimate, conditional implication and exact n8 stationary nonclosure. |
| argument | [Entire retained author account](#argument) | Complete D13 question/reuse/roles, Sections1--9/equations1--17, original18:55 freeze and19:09 source supplement/freeze, with every probability, conditional premise and source-access limit. |
| dependency | [C55 complete finite witness](Yin_C_G0055_v1.md#statement) | Only the exact n8 two-word complete parity class, original arrays and divisibility, equal within-class weights and full class mass1/10678. No asymptotic inference or new native run. |
| dependency | [Original returned-block minorization](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Every actual coordinate set with its FULL complement and original return probability, used for the averaged lower coordinate variance. |
| dependency | [Actual five-digit law and midpoint floor](../ledger/Yin_L_G0335_v1.md#quartic-uniform-positive-covariance) | p5=17/512, three-block probabilities and actual two-coordinate m_n>=1/512 for n>=4, with original signs and weights. |
| dependency | [Complete-state tightness and chronological mean](../ledger/Yin_L_G0329_v1.md#complete-midpoint-tightness-test) | ONLY the conditional mean implication: actual recurrent quartic, full real strips/rank-four lattice, eventual full-state tightness implies finite original chronological critical mean. |
| support | [Original combined-body whole independent finding](../audits/reviews/Yin_R_G0271_v1.md#quartic-local-dynamics-whole-independent-finding) | Entire original D13 combined19:09 body and actual accepted direct interfaces. It does not inspect this new statement/wrapper or prospectively adopt this Claim. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0276_v1.md#quartic-dynamics-actual-extraction-finding) | Entire actual statement, completely retained argument/history and current direct interfaces, independently inspected after allocation by a noncontributor. |


### Decision retained-mean-interface

| Field | Value |
| --- | --- |
| date | 2026-10-20T22:12 |
| status | proved |
| reason | Adopt the separately performed original whole R271 and actual extraction R276 findings at their exact original-law/operator/source scopes. The full original proof, both freezes and partial source limits remain. No unproved gap premise, chronological mean classification or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--D above, at the actual quartic and complete original unequal-probability return law; every n>=4 estimate, conditional implication and exact n8 stationary nonclosure. |
| argument | [Entire retained author account](#argument) | Complete D13 question/reuse/roles, Sections1--9/equations1--17, original18:55 freeze and19:09 source supplement/freeze, with every probability, conditional premise and source-access limit. |
| dependency | [C55 complete finite witness](Yin_C_G0055_v1.md#statement) | Only the exact n8 two-word complete parity class, original arrays and divisibility, equal within-class weights and full class mass1/10678. No asymptotic inference or new native run. |
| dependency | [Original returned-block minorization](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Every actual coordinate set with its FULL complement and original return probability, used for the averaged lower coordinate variance. |
| dependency | [Actual five-digit law and midpoint floor](../ledger/Yin_L_G0335_v1.md#quartic-uniform-positive-covariance) | p5=17/512, three-block probabilities and actual two-coordinate m_n>=1/512 for n>=4, with original signs and weights. |
| dependency | [Complete-state tightness and chronological mean](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | ONLY the conditional mean implication: actual recurrent quartic, full real strips/rank-four lattice, eventual full-state tightness implies finite original chronological critical mean. |
| support | [Original combined-body whole finding](../audits/reviews/Yin_R_G0271_v1.md#quartic-local-dynamics-whole-independent-finding) | Entire original D13 combined19:09 body and actual accepted direct interfaces. It does not inspect this new statement/wrapper or prospectively adopt this Claim. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0276_v1.md#quartic-dynamics-actual-extraction-finding) | Complete actual statement, retained argument/history and inspected direct interfaces; the noncontributor account read the prior whole finding for the same proof and declares self-reviewed shared mathematical context. |


### Decision current-complete-lower-fiber-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:36 |
| status | proved |
| reason | Maintain the same already selected original-law, endpoint-conditioned covariance or signed-square input at its complete current C300 proof home. The selected statement and proof, old decisions and actual old Review inputs remain unchanged; no new diffusive premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | A--D above, at the actual quartic and complete original unequal-probability return law; every n>=4 estimate, conditional implication and exact n8 stationary nonclosure. |
| argument | [Entire retained author account](#argument) | Complete D13 question/reuse/roles, Sections1--9/equations1--17, original18:55 freeze and19:09 source supplement/freeze, with every probability, conditional premise and source-access limit. |
| dependency | [C55 complete finite witness](Yin_C_G0055_v1.md#statement) | Only the exact n8 two-word complete parity class, original arrays and divisibility, equal within-class weights and full class mass1/10678. No asymptotic inference or new native run. |
| dependency | [Original returned-block minorization](Yin_C_G0300_v1.md#returned-block-convolution-minorization) | Every actual coordinate set with its FULL complement and original return probability, used for the averaged lower coordinate variance. |
| dependency | [Actual five-digit law and midpoint floor](Yin_C_G0300_v1.md#quartic-uniform-positive-covariance) | p5=17/512, three-block probabilities and actual two-coordinate m_n>=1/512 for n>=4, with original signs and weights. |
| dependency | [Complete-state tightness and chronological mean](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | ONLY the conditional mean implication: actual recurrent quartic, full real strips/rank-four lattice, eventual full-state tightness implies finite original chronological critical mean. |
| support | [Original combined-body whole finding](../audits/reviews/Yin_R_G0271_v1.md#quartic-local-dynamics-whole-independent-finding) | Entire original D13 combined19:09 body and actual accepted direct interfaces. It does not inspect this new statement/wrapper or prospectively adopt this Claim. |
| review | [Actual extraction finding](../audits/reviews/Yin_R_G0276_v1.md#quartic-dynamics-actual-extraction-finding) | Complete actual statement, retained argument/history and inspected direct interfaces; the noncontributor account read the prior whole finding for the same proof and declares self-reviewed shared mathematical context. |


## Registration and complete preservation

This extraction retains the ENTIRE original combined19:09 D13 body below.
Only its duplicate front matter is represented once, its first title is demoted one level, and line endings/separating blank lines are normalized.
The original wording, equations, anchors, all author/checking roles, initial source failures, exact later source limits, historical statuses and both freezes remain.
Relative paths remain valid from the Claim directory.
A direct complete-body comparison accompanies the extraction; no summary substitutes for the original proof.

The original [D13 source freeze](#quartic-local-dynamics-complete-source-author-freeze) is extraction ancestry, not an extra mathematical premise.
It remains in place pending root's separate preservation/consumer/retirement work.
[LP17](../audits/literature/LP17/readme.md#finite-conditional-resampling-attribution) is only partial primary indexed method attribution with the failed full second-edition artifact acquisition retained; [TK06](../audits/literature/TK06/readme.md#finite-row-sum-criterion-attribution) supplies inspected row-sum statement/naming and its explicit Kemeny--Snell attribution.
Neither ordinary account is made a canonical Review target or an external theorem premise.
No full LP17 book or Kemeny--Snell original-book inspection is claimed.

The extracting AI remains a contributor.
R271 is support for the exact original proof; it is not an extraction review.
No new native mathematics, Claim adoption or D retirement is performed.
Later component/connectivity work is a different mathematical account and is not silently inserted into this unchanged statement or historical proof.

2026-10-12T11:28 extraction check: direct comparison of the ENTIRE retained body with the actual D13 source returned equality after only the declared front-matter/title/newline/separator normalization, with30,577 characters on each side.
The scoped material check of this Claim, D13 and R271 passed with checked3.
These are preservation/structure results, not an independent mathematical or wrapper review.

## Argument

## Original quartic local replacement dynamics and the parity-projection obstruction

Date: 2026-10-12T10:43.
Human author Yin.
New AUTHOR inquiry under root-coordinated G0001, with root supplying only the broad request for a genuinely quantitative original-law mechanism beyond finite matched positivity.
This author selects and develops the local-replacement/Dirichlet-energy/parity-projection question; root supplied no mathematical formula or claimed conclusion.
The author cannot independently review this proof.

## Concrete question and unchanged original law

For the actual primitive Salem quartic P=t^4-t^3-t^2-t+1, consider every original length-2n ternary word with probabilities 1/4,1/2,1/4 conditioned on its COMPLETE field return.
Define a finite conditional-resampling chain by changing one integer coefficient of the quotient word/P while retaining legality of every digit.
Determine the exact all-n energy of the neutral midpoint under this chain and the resulting necessary price of an asserted spectral gap; separately test whether the two-parity-endpoint projection is actually a Markov chain under these updates.
This concerns an auxiliary dynamics preserving the exact original returned law, not a replacement for the original chronological walk.

The proposed outcome is a proved operator/conditional-mean obstruction or a justified n-dependent estimate, not an assumed diffusive lower variance.
Keep every original digit probability, field embedding, word length and normalizer.
A fixed finite C55 pair may test a claimed projection identity but will not be promoted to asymptotic evidence by padding.
No native program or new J is authorized by this allocation.

## Initial reuse and attribution boundary

The author read adopted C45's complete endpoint certificate and mesoscopic barrier, C51's true pure-shift failure, C55's actual positive matched pair/finite table and the original plus separately reproduced J91 scopes, L332's precise diffusive lower-moment gate, and L335's complete block minorization and covariance arguments.
The present question adds a conditional-resampling operator on the complete legal return words; it does not repeat the old covariance floor or infer diffusion from a linear upper proxy.

A bounded local source/Claim/ledger screen found no retained heat-bath, Poincare-gap or lumpability account.
Primary author URLs for Levin--Peres, Markov Chains and Mixing Times, second edition, and Tian--Kannan, Lumpability and Commutativity of Markov Processes, were located, but initial web-open attempts timed out.
Root has been informed for bounded source acquisition.
Classical naming/attribution remains pending; no external mixing theorem is a mathematical premise, and the finite conditional-expectation/row-sum arguments will be proved directly here.

<a id="quartic-local-dynamics-domain-and-reuse"></a>
## 1. Actual returned words and their integer quotient coordinates

The precise old inputs are [C45](Yin_C_G0045_v1.md#statement), [C51](Yin_C_G0051_v1.md#statement), [C55](Yin_C_G0055_v1.md#statement), [L332's complete midpoint moment gate](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization), and [L335's original-law block minorization](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization).
The [original and independently reproduced J91 account](../computations/programs/Yin_J_G0091/readme.md) was read at its exact n=6,...,10 scope; none of its programs is rerun.
C55 supplies the complete two-word fiber used only in Section 6.
The later conditional finite-mean implication uses the [complete tightness/capture equivalence](Yin_C_G0204_v1.md#midpoint-capture-fixed-scope), retained from the L329 interface that was read explicitly.
Its original recurrent quartic domain and full state strips are retained.

Fix the ACTUAL primitive Salem quartic

    P(t)=1-t-t^2-t^3+t^4,
    beta>1, gamma=beta^2,
    zeta a nonreal unit-circle conjugate,
    u=zeta+zeta^-1=(1-sqrt13)/2, u^2=u+3.

Use both unweighted real neutral coordinates, identified with C by evaluation at zeta.
For every integer n>=4 put N=2n and L=N-4.
Let Omega_n be the complete finite set of words eta=(eta_0,...,eta_(N-1)) in {-1,0,1}^N satisfying

    F_eta(beta)=0, F_eta(t)=sum_(r=0)^(N-1) eta_r t^r.

The ORIGINAL independent probabilities are 1/4,1/2,1/4.
If z(eta) is the number of zero digits, define the positive integer normalizer

    W_n=sum_(eta in Omega_n)2^z(eta),
    p_(2n)=W_n/4^(2n), pi_n(eta)=2^z(eta)/W_n.       (1)

Thus pi_n is exactly the complete original returned law, with all previous zero visits and all four conjugate constraints retained.
It is not uniform over return words.
The zero word ensures W_n>0.

Monicity and actual minimality give a UNIQUE integer quotient

    F_eta=P A_eta,
    A_eta(t)=sum_(j=0)^(L-1) a_j t^j in Z[t].       (2)

Integer long division by the monic P has integer quotient/remainder; the remainder vanishes at beta and has degree below four, so it is zero.
Conversely an integer a belongs to the finite legal set if all N coefficients of P A lie in {-1,0,1}.
The map between this set and Omega_n is a bijection.
Quotient coordinates may be large; no coefficient cutoff is imposed on them.
Every update below acts on this exact finite set in the original field, not an approximate recurrence state space.

The original chronological neutral midpoint, with the same convention as C55 and L335, is

    Z_n(a)=-zeta^-n sum_(r=0)^(n-1) eta_r zeta^r,
    m_n=E_(pi_n)|Z_n|^2.
                                                            (3)

Sign reversal a->-a preserves pi_n and reverses Z_n, so its mean is zero.
The symbol m_n is this second moment, not the total Mahler measure.
The new dynamics below has its own UPDATE clock; it is not the original chronological process whose critical first-return mean is denoted mu in L329/L332.

<a id="quartic-exact-single-coordinate-law"></a>
## 2. Every legal one-coordinate law with all original weights

For 0<=j<L, fix all quotient coefficients except a_j and resample a_j from its exact conditional distribution under pi_n.
Denote the conditional-expectation operator by K_j.
Changing a_j by an integer delta changes the ORIGINAL word by delta t^j P, so the full return is preserved at every original conjugate.
Legality still requires each of its five affected original digits to stay in {-1,0,1}.

Since all five coefficients p_r of P are +/-1, each affected digit inequality gives a closed interval of length two for a_j, with integer endpoints.
Their intersection is a nonempty integer interval containing one, two or three consecutive values.
The conditional weights are exactly proportional to 2 raised to the number of ZERO affected digits; all unaffected factors in (1) cancel.
This yields a complete classification:

* With one value, the conditional variance is zero.
* With three values, the middle value makes all five affected digits zero, while the two endpoints make them respectively the signs of P and their negatives.
  The conditional weights are (1,32,1)/34, so the variance of a_j is 1/17.
* With two consecutive values, each affected digit changes between zero and one of +/-1.
  The difference between their zero counts is an odd integer b in {-5,-3,-1,1,3,5}.
  The odds ratio is 2^b and the conditional variance is 2^b/(1+2^b)^2, at most 2/9.

For the third assertion, five factors each contribute +1 or -1 to the zero-count difference.
The function r/(1+r)^2 is symmetric under r->1/r and decreases for r>=1; the closest allowed odds to one are 2 and 1/2.
For the three-value assertion, an intersection of length two can contain three integers only when every original constraint interval has the same endpoints; their common midpoint therefore makes every affected digit zero.
No two-point or three-point law has been silently replaced by a uniform law.

Let

    v_j(n)=E_(pi_n) Var(a_j | all a_i, i!=j).

The preceding classification gives v_j(n)<=2/9.
There is also an ORIGINAL-LAW lower bound at EVERY site:

    1/512<=v_j(n)<=2/9,
                  0<=j<L, n>=4.                   (4)

To prove the lower bound, let I_j={j,...,j+4} and let B_j be the event that this block has zero actual field endpoint.
A length-five legal return is exactly 0,P or -P, with total ORIGINAL probability p_5=17/512, as already proved in L335.
Its probability inside the complete returned law is at least p_5 by the accepted center-maximum/block-minorization argument; every complementary endpoint probability is still included there.
The event B_j is constant along an a_j-resampling fiber, since the block endpoint changes by delta beta^j P(beta)=0.
On B_j the fiber has exactly the three values above, with variance 1/17.
Therefore

    v_j(n)>=(1/17)Pr_(pi_n)(B_j)
            >=(1/17)(17/512)=1/512.

This is an averaged conditional variance at each site.
It does NOT say every conditional fiber has positive variance, does not prove that the local-move graph is connected, and does not omit a return probability.
It reuses the old paid block mass rather than claiming new block positivity.

<a id="quartic-local-operator-and-energy"></a>
## 3. The auxiliary reversible operator and its exact midpoint energy

At one update, choose j uniformly from the L sites and perform K_j.
The resulting Markov operator is

    T_n=(1/L)sum_(j=0)^(L-1)K_j.                    (5)

It is a dynamics on complete returned words preserving EXACTLY pi_n.
If a,b lie in the same j-fiber, pi_n(a)K_j(a,b)=pi_n(a)pi_n(b)/pi_n(fiber), symmetric in a,b.
Otherwise both transition probabilities vanish.
Thus each K_j and T_n are reversible.
Each K_j is the orthogonal projection onto functions of all other coordinates in L^2(pi_n); consequently T_n is a self-adjoint positive contraction.
These finite statements follow directly from conditional expectation and do not assume irreducibility or a mixing theorem.

For real g, define its Dirichlet form and the two-coordinate midpoint trace by

    E_n(g,g)=<g,(I-T_n)g>_(pi_n)
       =(1/L)sum_j E_(pi_n)Var(g | a_-j),
    D_n=E_n(Re Z_n,Re Z_n)+E_n(Im Z_n,Im Z_n).
                                                            (6)

The projection identity proves (6).
Equivalently E_n(g,g) is one half of E[(g(a')-g(a))^2] for a stationary one-step pair under T_n, by detailed balance and expansion of the square.
The factor one half is retained.
D_n is an update energy, not the midpoint variance m_n or the covariance certificate called A_n in C45.

A replacement delta t^jP entirely below the midpoint has zero neutral prefix because P(zeta)=0; one entirely above it has no prefix term.
Exactly FOUR quotient coordinates can affect Z_n, namely j=n-k for k=1,2,3,4.
All four indices are legal when n>=4.
Put

    w_k=-zeta^-k sum_(r=0)^(k-1)p_r zeta^r.

Linearity and the zero word give the exact identity

    Z_n=sum_(k=1)^4 w_k a_(n-k).                    (7)

The neutral squared coefficients are

    |w_1|^2=|w_4|^2=1,
    |w_2|^2=|w_3|^2=2-u,
    C_star=sum_(k=1)^4 |w_k|^2=6-2u=5+sqrt13.
                                                            (8)

Here w_1=-zeta^-1 and w_4=1.
The w_2 norm is |1-zeta|^2=2-u.
The w_3 norm is |1-zeta-zeta^2|^2=3-(zeta^2+zeta^-2)=5-u^2=2-u.
These are exact original neutral evaluations; a conjugate complex coordinate is not counted a second time.

Consequently the whole actual update energy is

    D_n=(1/L)sum_(k=1)^4 |w_k|^2 v_(n-k)(n),
    C_star/[512(2n-4)]<=D_n
             <=2 C_star/[9(2n-4)], n>=4.           (9)

This is a new all-n estimate for the specified conditional-resampling OPERATOR, with every original probability retained.
Its 1/(2n-4) scale includes the EXPLICIT choice of one uniformly sampled site per step.
For the generator with EACH site updating at unit rate, the corresponding energy is L D_n and is bounded between C_star/512 and 2C_star/9.
It would be incorrect to promote the normalization factor in (9) to new chronological midpoint diffusion or an n-dependent return-mass lower bound.

<a id="quartic-local-gap-necessary-price"></a>
## 4. A spectral-gap obstruction and a conditional localization implication

Define the global Poincare gap of this FINITE reversible update operator by

    lambda_n=inf_{Var_(pi_n)g>0} E_n(g,g)/Var_(pi_n)g.

It lies in [0,1].
If the local chain is reducible, a nonconstant component indicator has energy zero, so lambda_n=0.
If it is irreducible, ordinary finite-dimensional self-adjoint diagonalization identifies lambda_n with one minus its largest eigenvalue below one.
No irreducibility or positive lower bound is asserted here.

Since the two coordinate variances sum to m_n and their energies sum to D_n, at least one nonconstant coordinate has energy/variance at most D_n/m_n.
The old L335 floor m_n>=1/512 for n>=4 makes the denominator nonzero.
Thus

    lambda_n m_n<=D_n<=2 C_star/[9(2n-4)],
    lambda_n<=min{1,1024 C_star/[9(2n-4)]}.          (10)

In particular an n-independent positive gap in the ONE-SITE-PER-STEP clock is impossible, without assuming diffusion or deciding the mean branch.
At any time with m_n>=epsilon n, epsilon>0,

    lambda_n<=2 C_star/[9 epsilon n(2n-4)].         (11)

Hence a genuine diffusive lower moment along a subsequence would force gaps of order at most n^-2 along that SAME subsequence.
This is a necessary condition only.
A small gap can be caused by another observable or disconnected components and does not imply that Z_n has a large variance.

There is also a precisely conditional implication in the other direction.
If some c>0 and n0 satisfy

    lambda_n>=c/(2n-4) for EVERY n>=n0,             (12)

then (10) yields m_n<=2 C_star/(9c) at every such n.
Markov's inequality makes the neutral midpoint laws uniformly tight.
Their expanding and contracting coordinates lie in the fixed complete real strips from L329/L335; intersecting these strips with a bounded neutral disk leaves a FINITE set of the actual rank-four Minkowski lattice.
Thus the full actual midpoint laws are eventually tight on actual states.
The accepted L329 theorem then gives FINITE critical first-return mean mu for the ORIGINAL chronological quartic chain.
No value R=beta, free Gaussian process or stationary approximation enters this implication.

Condition (12) is UNPROVED and might fail because of reducibility.
It is not used as a premise for (4)--(11).
Its contrapositive is the precise necessary statement

    mu=infinity implies liminf_(n->infinity)(2n-4)lambda_n=0.
                                                            (13)

Indeed a positive liminf would give (12) eventually.
A putative gap bound of order n^-2 supplies through (10) only an UPPER linear bound on m_n, not the lower diffusive gate in L332.
The auxiliary update clock and the original chronological clock remain different throughout.

<a id="quartic-parity-update-increments"></a>
## 5. The actual parity projection and what a closed endpoint chain would require

For a returned word define its two COMPLETE parity endpoints

    U_e=sum_(k=0)^(n-1)eta_(2k) gamma^k,
    U_o=sum_(k=0)^(n-1)eta_(2k+1) gamma^k,
    Pi(a)=(U_e,U_o), U_e+beta U_o=0.

Each endpoint lies in the actual O2=Z[gamma] and must occur in its true finite n-digit support.
Put

    E0=1-gamma+gamma^2=beta(1+gamma)>0,
    O0=-(1+gamma), E0+beta O0=0.

The symbol O0 in this display denotes a fixed endpoint increment, not a ring.
For a j-site quotient replacement by delta, direct splitting of t^jP into its even and odd powers gives

    Delta U_e=delta(-beta)^j E0,
    Delta U_o=-beta^-1 Delta U_e.                   (14)

For even j=2r the first increment is delta gamma^r E0.
For odd j=2r+1 it is -delta gamma^(r+1)(1+gamma), which equals delta(-beta)^j E0.
Every update therefore preserves COMPLETE return and moves to an actually realized matching pair.
Except for delta=0, it also changes the parity endpoints.
These are not moves within a fixed parity fiber.

A Markov description on these endpoint pairs that works for every starting word would require, for every target endpoint class B, the exit sum T_n(a,Pi^-1(B)) to be identical for all a with the same Pi(a).
Necessity follows already by starting the full chain at one of two such words and comparing the next projected state.
Sufficiency follows by conditioning on any past: if those exit sums depend only on the current endpoint pair, the next-pair conditional law has exactly that dependence.
This is the finite row-sum criterion usually called strong lumpability; its direct proof here needs no mixing theorem.

The endpoint-conditioned means in C55 are therefore not automatically observables of a closed Markov dynamics obtained from (5).
The complete counterexample below tests this exact transition requirement, not a heuristic comparison of endpoint sizes or order membership.

<a id="quartic-parity-nonclosure-witness"></a>
## 6. Exact failure of parity closure, reusing the fixed C55 words

Use ONLY the already adopted n=8 C55 pair, with ascending ORIGINAL digits

    f_a=(-1,1,1,1,-1,1,-1,0,-1,-1,-1,-1,0,-1,1,0),
    f_b=(-1,1,0,1, 1,1, 1,0, 1,-1, 1,-1,-1,-1,1,0).

C55 proves their common ACTUAL parity endpoints, their complete returned fibers, their exact P divisibility and original weights.
In particular the endpoint class contains exactly these two returned words, of equal conditional mass 1/2 within that class, and its complete return-conditioned probability is 1/10678.
This reuses the original and independently verified J91 scope rather than running another finite search.

At j=0 the first five digits of f_a are -P.
Its exact resampling fiber has the three blocks -P,0,P, with probabilities 1/34,16/17,1/34.
The move to the zero block changes its quotient coefficient by delta=1, hence changes its endpoint pair by (E0,O0).
In f_b the first and fifth digits are respectively -1 and +1.
Since both end coefficients of P are +1, their legality constraints force delta>=0 and delta<=0; the j=0 fiber is a singleton and cannot make that endpoint change.

No OTHER update site can land at the same target endpoint class from either word.
By (14) it would require delta(-beta)^j=1 for some nonzero integer delta.
For j>=1 its absolute value is at least beta^j>1.
At j=0 it requires exactly delta=1.
There are L=12 sites at n=8, so for the endpoint class B=Pi(f_a)+(E0,O0),

    T_8(f_a,Pi^-1(B))=(1/12)(16/17)=4/51,
    T_8(f_b,Pi^-1(B))=0.                            (15)

The target class is nonempty because the first displayed update gives a legal returned word.
Thus the complete parity projection of this local-update chain is NOT strongly lumpable, already at this actual finite input.
This disproves the universal proposed closure identity.
It does not establish an asymptotic covariance lower bound; no padding argument or repeat of the pair is presented as one.

There is a useful exact operator version.
Let Q_n be conditional expectation onto functions of Pi under pi_n; it is an orthogonal projection.
The stationary averaged endpoint kernel Q_n T_n Q_n always exists and is reversible.
The failure above does NOT deny that fact.
It shows that T_n does not preserve the range of Q_n, so this one-step average need not reproduce the true projected multi-step process.
Direct multiplication gives, on that range,

    Q_n T_n^2 Q_n-(Q_n T_n Q_n)^2
       =Q_n T_n(I-Q_n)T_n Q_n>=0.                  (16)

Its quadratic form at a projected observable g is exactly ||(I-Q_n)T_n g||_(pi_n)^2.
For n=8 take g=1_(Pi^-1(B)) using the actual target B above.
On the source class containing f_a,f_b, (15) gives conditional variance (4/51)^2/4=4/2601.
Its ORIGINAL complete mass is 1/10678.
Hence

    <g,[Q_8T_8^2Q_8-(Q_8T_8Q_8)^2]g>_(pi_8)
       >=4/(2601*10678)>0.                         (17)

Every remaining class contributes nonnegative variance.
Thus the failure persists even as a stationary two-step correlation identity, with an explicit paid lower discrepancy.
This is a transition/projection obstruction extracted from an already known finite fiber, not a new enumeration or an asserted growth law for n.

In particular the projected process is not a Markov chain even when the full chain starts at pi_8.
Its one-step transition probabilities would then have to be the stationary averaged kernel Q_8T_8Q_8; a stationary Markov process would satisfy the two-step identity contradicted by (17).
This conclusion does not rule out another separately designed endpoint Markov chain with the same stationary marginal.

<a id="quartic-local-dynamics-scope"></a>
## 7. What this changes and what remains unproved

The complete original returned law admits an exactly specified legal P-replacement dynamics.
Its midpoint update energy is quantitatively of order 1/n in its stated random-site clock, with constants and every original digit weight given in (9); the corresponding unit-rate-per-site energy stays bounded.
The necessary gap bounds (10)--(11) and the conditional localization implication (12)--(13) are genuine all-n statements on this auxiliary operator, but they do not prove that its graph is connected or that either gap premise is satisfied.

The finite parity nonclosure (15)--(17) prevents simply treating the exact conditional means from C55 as a Markov endpoint walk under these updates.
Any such projected dynamics needs a separately justified closure, approximation or memory analysis.
It is not enough that every individual replacement preserves return and carries positive original probability.
The stationary averaged kernel exists, but its powers fail the actual projected two-step identity in the displayed control.

No lower bound growing with n for the true m_n, no positive diffusive limsup, and no finite/infinite-mean classification is established.
The earlier C45 small-block barrier and C51 pure-shift obstruction remain intact.
No conditional covariance is bounded above by its lower certificate, and no uniform original-field/Mahler transfer is asserted.
The next discriminating mathematical obligation is quantitative control of this actual operator's components and relevant slow modes, or a justified estimate for the nonclosed conditional-mean dynamics, with an inference to the TRUE midpoint moment in the required direction.
A small spectral gap or a finite matched pair alone cannot supply that inference.

<a id="quartic-local-dynamics-author-selfcheck"></a>
## 8. Complete author self-check and contribution boundary

The author checked the actual monic-divisibility bijection with ALL legal returned words; original unequal digit weights and complete normalizer; every coordinate update at the two polynomial endpoints; classification of one/two/three allowed values, odd zero-count changes and exact variance constants; conditional-fiber invariance of the old block-zero event and its paid full-return probability; detailed balance, conditional-expectation projections, positivity and the one-half jump-energy factor; the four and only four midpoint quotient coefficients, the exact neutral coefficients and squared norms; every n>=4 support endpoint and original versus auxiliary clock normalization; reducible chains, zero gaps and the direction of the Rayleigh bound; the unproved all-late gap premise, actual Minkowski-lattice tightness and exact L329 application; the C55 complete two-word endpoint class, individual j=0 legality, exclusion of every other j and every integer delta, actual 4/51 versus zero exit masses; the compressed-operator identity, exact full fiber mass and paid two-step discrepancy; and the distinction between an existing stationary averaged kernel and the actual projected process.

These mathematical derivations were developed by this author after root supplied only the broad task.
Root supplied no candidate formula, lemma, proof step or mathematical correction for this account.
Earlier author/reviewer roles at other G0001 materials remain their own history and do not independently review this work.
The exact adopted C55 finite words and J91 results are inputs reused at their checked scope, not a new author computation.
No original or verification program was executed or changed.

Classical heat-bath, Dirichlet-form/Rayleigh and strong-lumpability naming was recognized and explicitly reported to root.
The bounded initial primary web fetches failed as recorded above; source attribution is still pending at this save, while all mathematical conditional-expectation and exit-row arguments are local and complete.
A later source-resolution paragraph must record the actual artifact, passage, inspection and attribution-versus-proof scope before source-completeness closure is claimed.
No uninspected external mixing, Poincare or lumpability theorem is being used to fill a mathematical gap.

<a id="quartic-local-dynamics-entire-author-freeze"></a>
## Entire mathematical author freeze and explicit source handoff

2026-10-12T10:55.
Freeze the COMPLETE starting question/reuse/source/contribution record and Sections 1--8/equations (1)--(17), including the stationary projected-process interpretation, exact original-law costs, all-n operator estimates, conditional mean implication and unresolved limits.
Mathematical development and author self-check are complete at this scope.
Separately organized whole noncontributor review is pending; no independent acceptance or fixed C is asserted.
Classical source attribution remains explicitly pending as described in Section 8, and this freeze does NOT claim source-completeness closure.
Root is coordinating the bounded primary-source follow-up; any later resolution must remain separately dated and included in the actual review scope.

No native mathematical program, numerical experiment, solver, enumeration, new J or program rerun was performed.
Scoped material checks passed for the complete mathematical body and are repeated after this paragraph; they verify structure and locators, not mathematics.
The actual quartic critical mean, diffusive lower moment and unrestricted G0001 remain unresolved.

<a id="quartic-local-dynamics-dated-source-supplement"></a>
## 9. Dated source follow-up with actual access limits

2026-10-12T11:09.
Root and a separately assigned source helper completed the bounded classical-attribution follow-up.
This author read their actual [LP17 account](../audits/literature/LP17/readme.md#finite-conditional-resampling-attribution) and [TK06 account](../audits/literature/TK06/readme.md#finite-row-sum-criterion-attribution); this author did not independently acquire or render either source.
The original Sections 1--8 and equations (1)--(17) are mathematically UNCHANGED.
The earlier pending statements remain the true history of the 18:55 freeze.

For LP17, the official author book page and official AMS metadata identify David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, second edition, AMS 2017, DOI 10.1090/mbk/107.
The official page's second-edition link is mcmt2e.pdf; the initially proposed markovmixing.pdf is its first-edition link, notwithstanding ambiguous search-index title text.
The bounded attempt to acquire the actual second-edition PDF timed out, and canonical registration retains that exception and unavailable artifact.
No full book PDF, downloaded-page verification, rendering or source-proof inspection is claimed.
Primary indexed-text observations identify Section 3.3, printed p.41, for Glauber dynamics/Gibbs-sampler terminology and Section 13.2.1, printed p.181, Lemma 13.6/equation (13.2), for the familiar one-half weighted squared-jump expression.
These are PARTIAL method-attribution observations with the documented edition/access limit, not verified full-book coverage.

For TK06, root actually acquired the eighteen-page author-hosted journal PDF: Jianjun Paul Tian and D. Kannan, *Lumpability and Commutativity of Markov Processes*, Stochastic Analysis and Applications 24 (2006), 685--702, DOI 10.1080/07362990600632045.
Root text-read the identity and printed pp.686--688 and visually checked printed p.687/PDF p.3.
Definition 2.2 and Theorem 2.3 match the all-initial-law finite row-sum meaning used in Section 5.
TK06 explicitly attributes and quotes that criterion from Kemeny and Snell; this account preserves that attribution and does not call it an original Tian--Kannan theorem.
The Kemeny--Snell book itself was not inspected.
No continuous-time extension, later commutativity result or complete source proof is adopted.

The bounded follow-up is now recorded at precisely these limits; LP17's full-artifact access remains unavailable.
The entire finite conditional-expectation/detailed-balance/Dirichlet identity, Rayleigh inequality, row-sum necessity/sufficiency and exact two-step discrepancy are proved locally above.
No external positive-gap, mixing, convergence, Poincare-bound or lumpability theorem fills a mathematical gap.
These ordinary source accounts supply naming and attribution only, are not canonical project Review targets, and do not assert source-wide completion.
No automatic acquisition retry or broadened source proof claim is introduced.

<a id="quartic-local-dynamics-complete-source-author-freeze"></a>
## Complete author freeze including the dated source limits

2026-10-12T11:09.
Freeze the ENTIRE D13 body: original question/reuse/contribution record, unchanged 18:55 Sections 1--8/equations (1)--(17), the original mathematical freeze and its then-pending source handoff, and this exact Section 9 source supplement.
A whole noncontributor review must inspect this actual combined scope and retain the partial LP17 access and selected TK06 statement/attribution limits.
This author remains the sole substantive proof contributor; root's broad task, coordination and source acquisition do not supply a proof step.
No new mathematics or native computation accompanies this supplement.
Source-global registration was performed by root, not by this author.
Scoped material checking is repeated on this completed body and does not certify mathematics or unread source pages.
