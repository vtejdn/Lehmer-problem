---
author: Yin
---
# Complete endpoint-fiber locality and the mesoscopic conditional-covariance barrier

Date: 2026-10-12T08:16.
Human author Yin.
Provenance: project deduction using the exact retained project and accepted-source interfaces.
Context: [the unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
This fixed organization records an intermediate result about a lower covariance certificate, not a Mahler-gap conclusion.

## Statement

Fix ANY nontorsion algebraic unit alpha, with ACTUAL monic irreducible minimal polynomial of degree d and complete conjugate list alpha_i.
Put r_i=abs(alpha_i), m=sum_(r_i>1)log r_i>0, q=#{i:r_i=1}=2s.
Each root occurs ONCE in the complete field norm; equivalently each complex place has multiplicity two.
The unweighted real Minkowski vector Phi uses one real coordinate for each real place and real/imaginary coordinates at ONE representative of each complex pair.
Write Z for its neutral coordinates and V for the nonneutral coordinates.
Define the fixed-input constants

    D_i=1/(r_i-1) if r_i>1, D_i=1/(1-r_i) if r_i<1,
    C=product_(all original nonneutral roots i)D_i,
    B=2^(d-q)C,
    C_non=sum_(nonneutral real/complex representatives i)D_i^2.

For EVERY integer n>=1 let Omega={0,...,2n-1}; let the independent ORIGINAL digits eta_j have values -1,0,1 with probabilities1/4,1/2,1/4.
For I subset Omega put

    U_I=sum_(j in I)eta_j alpha^j,
    Y_I=-alpha^(-n)sum_(j in I,j<n)eta_j alpha^j,
    nu_I(x)=Pr(U_I=x), E={U_Omega=0}, p=Pr(E)>0, Y=Y_Omega.

For nonempty I, put l_-=abs(I intersect{0,...,n-1}), l_+=abs(I intersect{n,...,2n-1}), t_I=2min(l_-,l_+) and

    g(I)=min({n-1-j:j in I,j<n} union{j-n:j in I,j>=n}).

Empty supports contribute zero; on one-sided supports U_I determines Y_I exactly.

**A. Every-endpoint locality and diameter.**
If TWO legal words on the SAME I have equal endpoint x and different midpoint contributions, their nonzero difference z in Z[alpha] satisfies

    1<=abs(Norm(z))<=B exp(-2m g(I)) t_I^q.

At every neutral representative its absolute value is at most t_I; at every nonneutral representative i it is at most2D_i exp(-abs(log r_i)g(I)).
For q>0, ALL endpoint fibers are deterministic whenever t_I<B^(-1/q)exp(2m g(I)/q); for q=0 this holds whenever B exp(-2m g(I))<1.
Equality is not excluded, and the one-sided case does not use0^0.
For EACH endpoint with nu_I(x)>0,

    tr Cov(Z(Y_I) given U_I=x)<=(s/2)t_I^2,

and the covariance vanishes under the strict locality condition.
These statements do not assume zero endpoint, centered fiber, symmetry within a fiber or a lower endpoint mass.

**B. Complete original conditional certificate.**
For EVERY disjoint collection of nonempty I_1,...,I_k, allowing arbitrary gaps, interlacing and dependence on n, define

    A_n=sum_(a=1)^k sum_x w_(a,x)Cov(Phi(Y_(I_a)) given U_(I_a)=x),
    w_(a,x)=nu_(I_a)(x)nu_(Omega\I_a)(-x)/p
           =Pr(U_(I_a)=x given E).

Every actual nonzero-mass endpoint is retained, and sum_x w_(a,x)=1 for each a.
With principal blocks A_n^Z,A_n^V, the Loewner inequalities and the nonneutral bound are

    0<=A_n<=Cov(Phi(Y) given E), tr A_n^V<=C_non.

The exact total-covariance decomposition leaves the covariance of endpoint-conditioned means, together with the complement contribution when a complement is omitted.
Neither is controlled by the bounds below.
No conditioning-amplification hypothesis is imposed.

**C. Every-time cardinality bounds.**
Suppose q>0.
For any integer L>=1 and EVERY such disjoint collection with abs(I_a)<=L, put

    H_alpha(L)=max(0,1+floor(log(B L^q)/(2m))).

Then

    tr A_n^Z<=s L^2 min(n,H_alpha(L)),
    tr A_n<=C_non+s L^2 min(n,H_alpha(L)),
    tr A_n^Z<=(s/2)sum_a t_(I_a)^2
        1_{B exp(-2m g(I_a))t_(I_a)^q>=1}.

One-sided supports have zero contribution.
The bounds also hold for convex averages of admissible disjoint collections, with a common L when used; they do not authorize unweighted addition of overlapping collections.
When q=0 there is no neutral part, tr A_n<=C_non for all cardinalities/placements, and every fiber is deterministic if g(I)>log B/(2m), with negative thresholds included.

**D. Fixed-input mesoscopic barrier.**
At ANY FIXED input with q>0, a sequence of collections with maximum cardinality L_n and L_n^2log(L_n+1)=o(n) satisfies tr A_n/n->0.
In particular L_n=o(sqrt(n/log n)) suffices.
Put

    K_alpha=[1+max(0,log B)/(2m)]/log2+q/(2m).

For every nonempty collection of actual maximum cardinality1<=L_n<=2n,

    tr A_n^Z<=s K_alpha L_n^2log(2n).

Consequently tr A_n^Z>=c n, c>0, forces

    L_n>=sqrt(c/(s K_alpha))sqrt(n/log(2n)).

Empty collections give zero.
The asymptotic conclusion also holds for convex averages obeying the same cardinality bound.
All constants retain the actual full degree, m, neutral dimension and nonneutral root distances.
No degree-uniform or near-one-uniform estimate is asserted.

**E. Actual nonzero-fiber control and limits.**
For the fixed Salem quartic P(t)=t^4-t^3-t^2-t+1 and its real beta>1, take n=4,I={0,...,6}, complement{7}.
The legal words a=(0,0,0,1,-1,-1,-1) and b=(1,-1,-1,0,0,-1,-1) have the SAME nonzero endpoint-beta^7 and midpoint difference1.
Their ORIGINAL probabilities are2^-11 and2^-12; the complement cancels that endpoint with probability1/4.
Their positive contribution to A_4^Z is at least2^-25.
This is a finite control, not a diffusive lower rate.

The result bounds a COMPLETE within-block LOWER covariance certificate.
It is NOT an upper bound on actual neutral covariance, a proof of finite or infinite critical mean, a changed return law, a uniform Mahler gap or Task completion.
The conditional-mean covariance and genuinely larger-block endpoint laws remain distinct open directions; using the entire returned word as one block only recovers the unknown covariance.

## Current assessment
[Selected decision](#decision-current-complete-lower-fiber-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T08:16 |
| status | open |
| reason | Register the precise intermediate statement and retain the ENTIRE author proof/history. The existing separate whole-D finding covers its exact frozen original, not this new registered statement or actual extraction. A separate noncontributor must check these exact bytes, dependency interfaces, preservation and scope before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion-unit domain, complete original digits/endpoints, exact covariance certificate, all-time fixed-input costs, mesoscopic barrier and quartic control, with all noncompletion limits. |
| argument | [Complete retained argument](#argument) | Entire D10 author account, Sections1--7/Lemmas1and3/Corollaries2and5/Theorem4/equations1--19, full sources, history and freeze. |
| dependency | [General-unit original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Actual unit/full-conjugate/unweighted real covariance conventions and accepted Kronecker positive-measure statement at its retained source-inspection scope; no new original-source audit. |
| dependency | [Existing full-norm interface](../ledger/Yin_L_G0353_v1.md#full-degree-norm-cut-distance) | Original single-word mechanism reused with the new TWO-word factor2^(d-q) proved in the retained argument; complex nonneutral places and q0 kept. |
| dependency | [Original conditional covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Original disjoint-support endpoint-conditioned covariance mechanism; every endpoint, its exact return probability and omitted conditional means are checked in the retained extension. |
| dependency | [Quartic and diffusive-moment interface](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Fixed actual quartic convention and the stated significance of positive diffusive covariance; no such lower bound or mean conclusion is claimed here. |
| support | [Previous limitation](../ledger/Yin_L_G0342_v1.md#full-conditioning-amplification-expense) | Historical zero-fiber restriction and the missing nonzero-fiber/conditional-mean directions; this comparison does not import an amplification assumption. |
| support | [Whole frozen-D review](../audits/reviews/Yin_R_G0244_v1.md#complete-fiber-whole-independent-finding) | Separate complete review of exact14:40 D10 only; no automatic coverage or adoption of the present registered statement/extraction. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T08:21 |
| status | proved |
| reason | Adopt the complete original arbitrary-endpoint proof and exact fixed statement after the separate noncontributor actual extraction and interface finding. Preserve all original law probabilities, complete norms, fixed-input costs, historical whole-review scope and conditional-mean limitations. This bounds a within-block lower certificate, not actual neutral covariance, critical mean or the unrestricted Mahler gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion-unit domain, complete original digits/endpoints, exact covariance certificate, all-time fixed-input costs, mesoscopic barrier and quartic control, with all noncompletion limits. |
| argument | [Complete retained argument](#argument) | Entire D10 author account, Sections1--7/Lemmas1and3/Corollaries2and5/Theorem4/equations1--19, full sources, history and freeze. |
| dependency | [General-unit original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Actual unit/full-conjugate/unweighted real covariance conventions and accepted Kronecker positive-measure statement at its retained source-inspection scope; no new original-source audit. |
| dependency | [Existing full-norm interface](../ledger/Yin_L_G0353_v1.md#full-degree-norm-cut-distance) | Original single-word mechanism reused with the new TWO-word factor2^(d-q) proved in the retained argument; complex nonneutral places and q0 kept. |
| dependency | [Original conditional covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Original disjoint-support endpoint-conditioned covariance mechanism; every endpoint, its exact return probability and omitted conditional means are checked in the retained extension. |
| dependency | [Quartic and diffusive-moment interface](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization) | Fixed actual quartic convention and the stated significance of positive diffusive covariance; no such lower bound or mean conclusion is claimed here. |
| support | [Previous limitation](../ledger/Yin_L_G0342_v1.md#full-conditioning-amplification-expense) | Historical zero-fiber restriction and the missing nonzero-fiber/conditional-mean directions; this comparison does not import an amplification assumption. |
| support | [Whole frozen-D review](../audits/reviews/Yin_R_G0244_v1.md#complete-fiber-whole-independent-finding) | Separate complete review of exact14:40 D10 only; no automatic coverage or adoption of the present registered statement/extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0246_v1.md#c45-actual-extraction-finding) | Exact registered statement and entire fixed argument, actual dependencies and source applicability, complete preservation and noncompletion boundaries inspected by the separate noncontributor root. |


### Decision current-complete-moment-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T07:48 |
| status | proved |
| reason | Maintain the same already selected midpoint/control interface at its complete current C285 proof home. The original statement, full proof, old decisions and actual R inputs remain unchanged; no new lower-moment premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion-unit domain, complete original digits/endpoints, exact covariance certificate, all-time fixed-input costs, mesoscopic barrier and quartic control, with all noncompletion limits. |
| argument | [Complete retained argument](#argument) | Entire D10 author account, Sections1--7/Lemmas1and3/Corollaries2and5/Theorem4/equations1--19, full sources, history and freeze. |
| dependency | [General-unit original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Actual unit/full-conjugate/unweighted real covariance conventions and accepted Kronecker positive-measure statement at its retained source-inspection scope; no new original-source audit. |
| dependency | [Existing full-norm interface](../ledger/Yin_L_G0353_v1.md#full-degree-norm-cut-distance) | Original single-word mechanism reused with the new TWO-word factor2^(d-q) proved in the retained argument; complex nonneutral places and q0 kept. |
| dependency | [Original conditional covariance](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization) | Original disjoint-support endpoint-conditioned covariance mechanism; every endpoint, its exact return probability and omitted conditional means are checked in the retained extension. |
| dependency | [Quartic and diffusive-moment interface](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Fixed actual quartic convention and the stated significance of positive diffusive covariance; no such lower bound or mean conclusion is claimed here. |
| support | [Previous limitation](../ledger/Yin_L_G0342_v1.md#full-conditioning-amplification-expense) | Historical zero-fiber restriction and the missing nonzero-fiber/conditional-mean directions; this comparison does not import an amplification assumption. |
| support | [Whole frozen-D review](../audits/reviews/Yin_R_G0244_v1.md#complete-fiber-whole-independent-finding) | Separate complete review of exact14:40 D10 only; no automatic coverage or adoption of the present registered statement/extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0246_v1.md#c45-actual-extraction-finding) | Exact registered statement and entire fixed argument, actual dependencies and source applicability, complete preservation and noncompletion boundaries inspected by the separate noncontributor root. |


### Decision current-complete-lower-fiber-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:36 |
| status | proved |
| reason | Maintain the same already selected original-law, endpoint-conditioned covariance or signed-square input at its complete current C300 proof home. The selected statement and proof, old decisions and actual old Review inputs remain unchanged; no new diffusive premise or broader review is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual nontorsion-unit domain, complete original digits/endpoints, exact covariance certificate, all-time fixed-input costs, mesoscopic barrier and quartic control, with all noncompletion limits. |
| argument | [Complete retained argument](#argument) | Entire D10 author account, Sections1--7/Lemmas1and3/Corollaries2and5/Theorem4/equations1--19, full sources, history and freeze. |
| dependency | [General-unit original conventions](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse) | Actual unit/full-conjugate/unweighted real covariance conventions and accepted Kronecker positive-measure statement at its retained source-inspection scope; no new original-source audit. |
| dependency | [Existing full-norm interface](../ledger/Yin_L_G0353_v1.md#full-degree-norm-cut-distance) | Original single-word mechanism reused with the new TWO-word factor2^(d-q) proved in the retained argument; complex nonneutral places and q0 kept. |
| dependency | [Original conditional covariance](Yin_C_G0300_v1.md#returned-block-convolution-minorization) | Original disjoint-support endpoint-conditioned covariance mechanism; every endpoint, its exact return probability and omitted conditional means are checked in the retained extension. |
| dependency | [Quartic and diffusive-moment interface](Yin_C_G0285_v1.md#whole-midpoint-moments-and-localization) | Fixed actual quartic convention and the stated significance of positive diffusive covariance; no such lower bound or mean conclusion is claimed here. |
| support | [Previous limitation](../ledger/Yin_L_G0342_v1.md#full-conditioning-amplification-expense) | Historical zero-fiber restriction and the missing nonzero-fiber/conditional-mean directions; this comparison does not import an amplification assumption. |
| support | [Whole frozen-D review](../audits/reviews/Yin_R_G0244_v1.md#complete-fiber-whole-independent-finding) | Separate complete review of exact14:40 D10 only; no automatic coverage or adoption of the present registered statement/extraction. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0246_v1.md#c45-actual-extraction-finding) | Exact registered statement and entire fixed argument, actual dependencies and source applicability, complete preservation and noncompletion boundaries inspected by the separate noncontributor root. |


## Fixed organization and contribution boundary

2026-10-12T08:16.
Under Yin's explicit continuation and root's bounded D10-extraction assignment, g0001_routes for Yin authored this registered statement and copied the complete [original D10](#complete-fiber-author-freeze) into the fixed argument below.
The original return_route_advance author supplied its mathematical proof; the original root supplied broad allocation without a proof step.
This extractor is a contributor to the present statement/organization and cannot independently review it.

The retained original has only its repeated front matter removed and its first title reduced from level1 to level2; its mathematical text, all anchors, equations, source and contribution history, original pending-review prose and dated14:40 freeze remain.
Existing relative links from drafts to ledger resolve identically from claims, so no mathematical locator change is needed.
The original wording 'Each complex root is counted twice' is preserved as history: as [R244 expressly explains](../audits/reviews/Yin_R_G0244_v1.md#complete-fiber-whole-independent-finding), the formulas count each full-list root once and each complex PLACE twice.
The registered statement above makes that convention precise without changing a formula or the original reviewed text.

R244's whole finding is completed independent evidence at its original frozen scope.
The initial decision deliberately remains proof draft / under review until an actual independent extraction/interface finding covers the registered statement and retained fixed proof.
No mathematical program, new source acceptance, native computation, original-review edit or Task completion is part of this organization.

## Argument

The ENTIRE original author account follows.
Its former pending-status and planned-action statements retain their actual historical meaning and do not override the Current assessment above.

## Complete endpoint-fiber locality and the mesoscopic midpoint innovation barrier

Date: 2026-10-12.
Author inquiry for Yin on the G0001 mathematical question.
Current mathematical status: complete author proof with self-review, awaiting separate review; no adoption or independent review is asserted.

## Question and starting scope

Test whether keeping every nonzero endpoint fiber in the original returned-bridge conditional covariance can evade the fixed returned-block barriers of L335, L342 and L353.
The proposed changed target is a full-field-norm locality theorem for differences of two legal words with the SAME arbitrary endpoint, with digit differences in {-2,-1,0,1,2}.
Its planned consequence is a bound for the COMPLETE within-block conditional innovation certificate under exact whole-word return, with no assumed amplification bound.
All supports, original weights, actual conjugates and covariance-of-conditional-means limitations must remain explicit.

Direct fixed inputs: [L353 full norm and original conditional covariance](../ledger/Yin_L_G0353_v1.md#general-conditioning-amplification), [L342 unresolved nonzero-endpoint direction](../ledger/Yin_L_G0342_v1.md#full-conditioning-amplification-expense), [L335 endpoint-conditioned covariance mechanism](../ledger/Yin_L_G0335_v1.md#returned-block-convolution-minorization), and [L332 diffusive moment criterion](../ledger/Yin_L_G0332_v1.md#whole-midpoint-moments-and-localization).
Existing statements do not bound all nonzero endpoint fibers: they retain only endpoint zero.
No native mathematical program, solver, new literature premise or numerical experiment is planned.

The return_route_advance author is responsible for the new argument.
Root supplied the broad other-directions assignment only.
At allocation the next step was to establish the two-word norm bound and determine whether its paid support-size consequence changes the next discriminator rather than merely renaming an unknown quantity.
Sections 3--6 now carry that completed bounded test.
The unrestricted Mahler gap and actual neutral diffusion remain unresolved.

<a id="complete-fiber-reuse-and-scope"></a>
## 1. Reuse and changed conclusion

The author read the current Task contract and selected decision, applicable execution/personal rules, S2/S7 current interfaces, the complete fixed L353, and the relevant complete conditional-covariance and limitation sections of L335/L342.
L332 supplies the actual diffusive-moment discriminator.
The bounded local screen also checked the titles and route terms of later L360--L394; those concern other arithmetic/profile mechanisms.
No assertion that the local search is an exhaustive novelty search is made.

L353 proves an all-support bound for disjoint zero-endpoint blocks at their original masses.
Its refined zero-endpoint theorem requires an upper bound on exact conditioning amplification.
L342 explicitly leaves nonzero endpoint contributions and covariance of endpoint-conditioned means as changed possible directions.
The present result keeps ALL endpoint fibers at their actual conditional probabilities, proves a deterministic diameter constraint on each fiber, and excludes diffusion certificates assembled from blocks of cardinality o(sqrt(n/log n)).
It removes the amplification premise on this stated range.
It does not extend the earlier arbitrary-cardinality zero-block theorem to arbitrary-cardinality full fibers.

The fixed full-norm and conditional-variance mechanisms supply sufficient local evidence.
The steps below are direct finite algebra, geometric sums and the elementary covariance identity; no new substantive external result or attribution claim is introduced.
Kronecker's positive-measure input for nontorsion units is reused only at the existing statement/inspection scope recorded in [L353 Section 1](../ledger/Yin_L_G0353_v1.md#general-returned-block-reuse), with its linked accepted source.
No new source acquisition, program, solver or finite enumeration was used.

<a id="original-full-fiber-conventions"></a>
## 2. Original law and arbitrary endpoint fibers

Fix a nontorsion algebraic unit alpha, with actual monic irreducible minimal polynomial of degree d and complete conjugates alpha_i.
Put r_i=|alpha_i|, m=sum_(r_i>1)log r_i>0, q=#{i:r_i=1}=2s.
Both expanding and contracting conjugates occur, because the norm is a unit and m>0.
Neutral real conjugates would be +/-1 and force torsion by irreducibility.
Each complex root is counted twice in the field norm, but neutral Euclidean coordinates consist of real and imaginary parts at ONE representative of each pair.
Let Phi be this unweighted real Minkowski map, Z its neutral part in R^q and V its nonneutral part.
Define

    D_i=1/(r_i-1) for r_i>1; D_i=1/(1-r_i) for r_i<1,
    C=product_(r_i!=1)D_i,
    B=2^(d-q) C,
    C_non=sum_(nonneutral real/complex representatives i) D_i^2.     (1)

All these constants belong to the complete fixed input.
In particular m is total logarithmic Mahler measure; it is not divided by degree.

For N=2n, n>=1, let Omega={0,...,2n-1}.
Independent original digits eta_j take values -1,0,1 with probabilities 1/4,1/2,1/4.
For I subset Omega put

    U_I=sum_(j in I)eta_j alpha^j,
    Y_I=-alpha^(-n)sum_(j in I,j<n)eta_j alpha^j,
    nu_I(t)=Pr(U_I=t),
    E={U_Omega=0}, p=Pr(E)>0,
    Y=Y_Omega.                                                   (2)

Under E, Y=sum_(j>=n)eta_j alpha^(j-n).
Reversal of iid digit labels identifies its law with the chronological midpoint of the complete original length-2n returned walk.
This is the exact convention of L353; no reciprocal automorphism or changed walk law is needed.
The unit hypothesis ensures that all Y_I belong to Z[alpha].
The vectors Phi(Y_I) need not be centered on a NONZERO endpoint fiber.
Global sign reversal does center Phi(Y) under E.

For a nonempty support I define

    l_-=|I intersect {0,...,n-1}|, l_+=|I intersect {n,...,2n-1}|,
    t_I=2 min(l_-,l_+) <= |I|,
    g(I)=min({n-1-j:j in I,j<n} union {j-n:j in I,j>=n}).         (3)

The notation t_I is a nonnegative integer support parameter; a fiber endpoint will be denoted x, avoiding conflict.
An empty support contributes zero.
A one-sided support has t_I=0.
In that case U_I determines Y_I exactly: either Y_I=0 or Y_I=-alpha^(-n)U_I.

<a id="two-word-full-norm-locality"></a>
## 3. A full-norm locality theorem for every endpoint

**Lemma 1 (arbitrary-fiber diameter and arithmetic locality).**
Suppose two legal words on the same nonempty I have the same endpoint x but different midpoint contributions.
Their difference z in Z[alpha] is nonzero and satisfies

    1 <= |Norm(z)| <= B exp(-2m g(I)) t_I^q.                     (4)

At every neutral representative, the difference has modulus at most t_I.
At every nonneutral representative i it has modulus at most 2D_i exp(-|log r_i|g(I)).
Consequently, if q>0 and

    t_I < B^(-1/q) exp(2m g(I)/q),                              (5)

EVERY endpoint fiber of this support has a deterministic midpoint.
If q=0 the same conclusion follows whenever B exp(-2m g(I))<1.
Both conclusions apply to every possible endpoint, independently of its mass or whole-word conditioning.

*Proof.*
Let delta_j be the difference of the two digits.
Then |delta_j|<=2, sum_(j in I)delta_j alpha^j=0, and

    z=-alpha^(-n)sum_(j in I,j<n)delta_j alpha^j
      =sum_(j in I,j>=n)delta_j alpha^(j-n).                    (6)

At an expanding embedding use the first expression and sum the whole geometric tail through exponent -1-g.
This gives 2D_i r_i^(-g).
At a contracting embedding use the second expression and its full tail from exponent g, giving 2D_i r_i^g.
The first and second expressions give neutral modulus bounds 2l_- and 2l_+, respectively, hence their minimum t_I.
All differences lie in the actual order because alpha is a unit.
Multiplying over EVERY embedding, including both roots of every complex pair, gives the upper bound in (4): the factor two occurs d-q times, and the expanding and contracting logarithms together give -2mg.
The lower bound follows because a nonzero algebraic integer has nonzero integer norm.
If the right side is strictly below one no nonzero difference exists, proving the assertions.
Equality in (4) is not excluded.
One-sided supports were already handled directly, so no use of 0^0 in the q=0 branch is required.
This argument uses two legal words, whose differences may equal +/-2; applying L353's original single-word constant C without the factor 2^(d-q) would be incorrect.

**Corollary 2 (all-fiber covariance bound).**
For any endpoint x with nu_I(x)>0,

    tr Cov(Z(Y_I) | U_I=x) <= (s/2)t_I^2,                       (7)

and this covariance is zero when the strict locality condition of Lemma 1 holds.
Indeed, two independent conditional samples have neutral squared difference at most s t_I^2, and trace covariance is one half the expectation of that squared difference.
The proof does not center either sample at zero or assume symmetry of the nonzero fiber.

<a id="complete-original-innovation-certificate"></a>
## 4. Exact original conditioning, including every nonzero endpoint

Let I_1,...,I_k be pairwise disjoint nonempty supports, with arbitrary gaps, interlacing and placement; the collection may depend on n.
Let I_0 be their complement.
Define the complete within-block conditional covariance contribution

    A_n=sum_(a=1)^k sum_x w_(a,x) Cov(Phi(Y_(I_a)) | U_(I_a)=x),
    w_(a,x)=nu_(I_a)(x) nu_(Omega\I_a)(-x)/p.                   (8)

The sum runs over the finite actual endpoint support.
Fibers of zero mass are omitted.
The weights are EXACT original conditional probabilities Pr(U_(I_a)=x | E); in particular they sum to one for each a.
They are not replaced by original zero-return masses, temporal-return approximations or a separately chosen neutral law.
Write A_n^Z and A_n^V for its principal neutral and nonneutral covariance blocks.

**Lemma 3 (full conditional decomposition).**
One has

    0 <= A_n <= Cov(Phi(Y) | E),
    tr A_n^V <= C_non.                                        (9)

*Proof.*
Condition on the endpoints of every I_a and I_0.
Before imposing E, the internal words in these disjoint sets are independent conditional on their own endpoints.
Event E depends only on the sum of these endpoints, so this conditional independence remains true under E.
The conditional covariance of their sum is the sum of the conditional covariances.
Averaging gives A_n plus the corresponding nonnegative complement term.
The law of total covariance adds the nonnegative covariance of the conditional means.
Formula (8) is just the resulting marginal weight, also obtained directly by independence of I_a and its complement.
This proves the matrix inequality, including the case I_0 is empty.
It does not assert independence when conditioning on E alone.

For the complete returned word, the two expressions in (2) give |sigma_i(Y)|<=D_i at each nonneutral representative, exactly as in L353.
The whole returned law is centered.
Thus the actual nonneutral covariance trace is at most C_non, and the principal-block version of the first inequality gives (9).
No actual neutral upper bound is asserted.

When the collection is a full partition, (9) has an exact useful interpretation.
A_n is the average conditional covariance after revealing all block endpoints; the difference from actual covariance is EXACTLY the covariance of the conditional means.
When a complement is omitted, its conditional covariance is an additional discarded term.
Neither term is controlled by the next theorem.

<a id="mesoscopic-all-fiber-barrier"></a>
## 5. All-time cardinality bound and the changed scale discriminator

Assume q>0.
For an integer L>=1 define

    H_alpha(L)=max(0, 1+floor(log(B L^q)/(2m))).                (10)

**Theorem 4 (complete endpoint-fiber innovation barrier).**
For every n>=1 and every disjoint collection in (8) satisfying |I_a|<=L,

    tr A_n^Z <= s L^2 min(n,H_alpha(L)),
    tr A_n <= C_non+s L^2 min(n,H_alpha(L)).                   (11)

All original endpoint weights and whole-return conditioning are retained, and no amplification bound is required.
A more precise support-sensitive inequality is

    tr A_n^Z <= (s/2) sum_a t_(I_a)^2
                    1_{B exp(-2m g(I_a)) t_(I_a)^q >= 1},     (12)

where one-sided supports contribute zero.
These estimates remain true for convex averages of admissible disjoint collections.

*Proof.*
Lemma 1 makes every fiber covariance vanish unless the indicated norm inequality holds.
Otherwise Corollary 2 and sum_x w_(a,x)=1 bound its full weighted contribution by (s/2)t_(I_a)^2.
This proves (12).
For a contributing block, t_I<=L and (4) imply

    0<=g(I)<=floor(log(B L^q)/(2m)).                           (13)

Assign the block one of its coordinates realizing g(I), breaking a tie by a fixed rule.
Disjoint blocks receive different assigned coordinates.
There are at most TWO such coordinates for any g, namely n-1-g and n+g.
There are therefore at most 2min(n,H_alpha(L)) contributing blocks.
Each contributes at most sL^2/2, proving the neutral bound; add (9) for the full trace.
Convex averaging preserves the estimates and does not authorize unweighted addition of overlapping collections.

If q=0 there is no neutral part and (9) already gives tr A_n<=C_non for any L or support placement.
Lemma 1 also shows exact determinism in every endpoint fiber with g(I)>log B/(2m), where a negative threshold means all g>=0.
This is a separate branch, not division by q.

**Corollary 5 (necessary mesoscopic support growth).**
At any fixed input with q>0, if a sequence of collections has maximum cardinality L_n and

    L_n^2 log(L_n+1)=o(n),                                    (14)

then tr A_n/n tends to zero.
In particular this holds for L_n=o(sqrt(n/log n)).
Thus keeping all nonzero endpoint fibers, with arbitrarily large exact conditioning amplification, cannot produce a positive diffusive lower covariance from such blocks.

For a quantitative converse, put

    K_alpha=[1+max(0,log B)/(2m)]/log 2+q/(2m).                (15)

Since L_n<=2n whenever a nonempty collection exists,

    tr A_n^Z <= s K_alpha L_n^2 log(2n).                       (16)

Hence tr A_n^Z>=c n at any n and c>0 forces

    L_n >= sqrt(c/(s K_alpha)) sqrt(n/log(2n)).                 (17)

To prove these statements, (10) is at most 1+max(0,log B)/(2m)+(q/(2m))log L.
The latter is at most K_alpha log(2n), giving (16)--(17); the same bound by a constant times log(L+1) gives (14).
The constant nonneutral term divided by n vanishes.
For convex averages in which each collection obeys the same L_n, the identical conclusions hold.
If the collection is empty, A_n=0 directly.

Every expense in (10)--(17) depends on the ACTUAL full degree, m, neutral dimension and nonneutral root distances.
No near-one or degree-uniform constant is claimed.
The result is an all-n restriction on a full original-law LOWER certificate.
It does not turn an upper bound on this certificate into an upper bound on the actual neutral covariance.
At the quartic of L332, it removes the indicated complete-fiber block method as a source of the positive diffusive limsup sufficient for infinite critical mean; it establishes neither finite nor infinite critical mean itself.

<a id="actual-nonzero-fiber-control"></a>
## 6. An actual quartic nonzero fiber contributes positively

The inclusion of nonzero endpoint fibers is not vacuous.
Use the actual quartic

    P(t)=t^4-t^3-t^2-t+1, alpha=beta>1,

with its fixed Salem scope already retained in L332.
Set n=4, I={0,...,6}, J={7}.
Two legal words on I, listed in increasing exponent order, are

    a=(0,0,0,1,-1,-1,-1),
    b=(1,-1,-1,0,0,-1,-1).                                  (18)

Both have endpoint x=-beta^7, since appending digit +1 at exponent 7 gives the zero polynomials t^3P and P+t^3P respectively, evaluated at beta.
Their difference is P in exponents 0 through 4.
Its low part through exponent 3 is -beta^4, so by (2) their midpoint contributions differ by exactly 1.
At the unique neutral representative the squared difference is also 1.
The fiber is nonzero and its whole-return probability is positive, because J can supply beta^7 with probability 1/4.

The original I-word probabilities are a_0=2^(-11) and b_0=2^(-12): the first has three zero and four nonzero digits; the second has two zero and five nonzero digits.
Write v=nu_I(-beta^7)>0 and retain p=Pr(E).
Two ordered cross-pairs in the elementary pairwise variance formula show that the neutral covariance trace on this fiber is at least a_0 b_0/v^2.
Its exact whole-return weight is v/(4p).
Consequently its contribution to A_4^Z is at least

    a_0 b_0/(4vp) >= 2^(-25)>0,                              (19)

using only v<=1 and p<=1.
The displayed bound is deliberately coarse; it does not claim the exact fiber mass or a long-time lower rate.
This term is discarded in the zero-endpoint-only certificate.
Its retention is legitimate here, and Theorem 4 still controls the entire all-fiber collection over all n at the stated support-size cost.
No enumeration or numerical root value is used.

<a id="complete-fiber-outcome-selfcheck"></a>
## 7. Outcome, failed implication and author self-check

The tested shortcut was that the nonzero endpoint terms discarded by L342/L353 might, by themselves, repair diffusion certificates built from uniformly small or mesoscopic disjoint digit supports, possibly through large exact conditioning amplification.
Theorem 4 refutes this shortcut for every fixed nontorsion algebraic unit whenever (14) holds.
Its distinction from the previous theorem is the entire arbitrary-endpoint covariance contribution at its actual conditional weight; its new restriction is block cardinality.
The explicit nonzero fiber (18)--(19) verifies that this is a strictly larger certificate than retaining endpoint zero only.

The missing covariance of conditional means is a substantive separate direction.
Revealing all singleton endpoints determines every digit, so the within-block contribution is zero and ALL actual covariance lies in those conditional means.
This elementary limiting case prevents any inference from (11) to actual localization.
Another remaining direction is a quantitative lower covariance estimate from blocks at or beyond (17), together with their complete actual endpoint distributions; merely choosing such large blocks proves nothing.
Choosing the entire word as one block recovers the unknown actual covariance and is tautological.
The present proof therefore changes the smallest useful scale/discriminator without claiming a global solution or replacing the process by a relaxed model.

Author self-check covered the actual unit/minimality/nontorsion hypotheses; positive total measure and both nonneutral modulus classes; unweighted real covariance versus full norm multiplicities; the factor 2^(d-q) for differences of two legal words; negative powers and integrality; arbitrary nonzero endpoint means; empty/one-sided supports; strict versus equality thresholds and floor/max behavior when B L^q<1; all-n two-coordinates-per-distance counting; exact original conditional weights; conditional independence only AFTER endpoints are given; complement and conditional-mean terms; the deterministic pairwise covariance bound; the zero-neutral branch; every fixed-input constant and the little-o implication; and the exact eight-digit quartic words, original weights and positive contribution.
No solver, continuing program, finite search or new source artifact exists for this round.

All new derivations and the explicit word control are by return_route_advance for Yin.
Root supplied broad allocation/coordination and received progress summaries, without contributing a proof step.
The argument has author self-review only and awaits separately organized noncontributor review.
G0001 remains active and unresolved.
Root is responsible for fixed retention/adoption or correction after review.

<a id="complete-fiber-author-freeze"></a>
## Entire author freeze

2026-10-12T06:40.
Sections 1--7, Lemmas 1 and 3, Corollaries 2 and 5, Theorem 4, equations (1)--(19), the explicit original-law quartic control, all fixed-input costs, failed-implication scope and contribution/source boundaries are frozen for a separately organized whole noncontributor review.
The scoped command `python scripts/material.py check mathematics/claims/Yin_C_G0045_v1.md` passed on this author body (`checked: 1`) before adding this freeze marker; this is structural validation, not proof review.

No new exploration begins at this freeze.
