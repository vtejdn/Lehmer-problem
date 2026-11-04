---
author: Yin
---
# Complete pairwise residue-order synchronization without linear binary cyclic income

Date: 2026-10-12T16:44.
Human author Yin.
Internal fixed extraction under continuing G0001 authorization.
The matrix-recovery AI authored ALL new mathematics in the complete original00:30:51 D38.
The rounding-recovery AI independently WHOLE-reviewed that actual original in R309 and NOW authors this new statement and extraction wrapper; it is therefore a contributor to this artifact and cannot independently review its extraction.
Root supplied the broad question only and will separately inspect the actual new wrapper.
Initial status is proof draft / under review.
The ENTIRE original candidate, history, proof, costs, source/contribution limits and freeze are retained below.

## Statement

For EVERY integer Q>=64 define the complete selected order set and cyclotomic product

    O_Q={o in Z:5<=o<=Q and o odd},
    R_Q(t)=product_(o in O_Q) Phi_o(t),
    d=d_Q=sum_(o in O_Q) phi(o), s=d/2,

where phi is Euler's totient and Phi_o the complete cyclotomic polynomial.
Then

    Q^2/8<=d<=(Q+1)^2/4.

The degree is even and tends to infinity with Q.
The following construction and conclusions retain ALL original roots and the ORIGINAL degree d.

**A. Explicit reciprocal irreducible unit construction.**
For each selected o let S_o in Z[x] be the unique monic trace polynomial of degree phi(o)/2 satisfying

    Phi_o(t)=t^(phi(o)/2) S_o(t+t^-1),
    T_0(x)=product_(o in O_Q) S_o(x).

The actual degree of T_0 is s.
In F_2[x], take the unique remainder of x^2 T_0'(x) modulo T_0(x), and lift it to H in Z[x] with degree<s and coefficients0 or1.
Define the monic integer polynomial T of degree s by coefficientwise CRT:

    T congruent to T_0+2H modulo4,
    T congruent to(x-2)^s+3 modulo9,

choosing each of its s lower coefficients as the unique representative in[-18,17] of its class modulo36.
Finally set

    P_Q(t)=t^s T(t+t^-1).

This is a monic irreducible reciprocal nontorsion integer-unit polynomial of EXACT degree d and constant coefficient1.
No root is a root of unity.
Its reduction is EXACTLY R_Q modulo2, which is squarefree, so2 does not divide the original polynomial discriminant.
Irreducibility follows from

    P_Q(t+1) congruent to t^(2s)+3(t+1)^s modulo9,

which is Eisenstein at3.
T is consequently irreducible and has simple characteristic-zero roots.
Nontorsion is proved by the exact finite local valuations in B, not assumed from Eisenstein.

**B. ALL original local roots and every binary depth.**
In the full2-adic root list of P_Q, for each o in O_Q EXACTLY phi(o) original roots have residue order o; these groups contain all d original roots.
Every root is in an unramified extension, with normalized valuation v_2(2)=1.
For EVERY such root alpha with residue order o,

    v_2(alpha^o-1)=v_2(alpha^o+1)=1,
    v_2(alpha^n-1)=1+v_2(n) when o divides n,
                   0 otherwise, for EVERY integer n>=1.

No first-squaring exception or later depth is omitted.
The construction covers all inverse/Frobenius orbits, including even-degree orbits fixed by inversion; it makes no two-factor or inverse-exchanged-orbit assumption.

More precisely, in the unramified ring lift the primitive residue root to the exact order-o root of unity zeta and put theta=zeta+zeta^-1.
Its reduction is neither0 nor1 because orders1 and3 were excluded.
The full squarefree trace reduction has T_0'(theta) a unit.
The chosen H makes the exact normalized first residue

    overline[(alpha^o-1)/2]
       =overline H(theta)/[overline T_0'(theta)*overline theta]
       =overline theta.

Hence both initial quotients divided by2 have nonzero residue, since they differ by1.
This holds simultaneously at every original root.
The stable binary recurrence then proves the displayed all-n formula and nontorsion.

Choose any root alpha generating K=Q(alpha) of degree d.
The COMPLETE ORIGINAL signed norm and its absolute value are

    Norm_(K/Q)(alpha^n-1)=Res(P_Q,t^n-1),
    C_n=abs Norm_(K/Q)(alpha^n-1)>0.

Their exact binary valuation and local logarithmic income are

    v_2(C_n)=(1+v_2(n)) sum_(o in O_Q, o divides n) phi(o),
    A_2(n)=(log2)v_2(C_n).

Each residue factor contributes its full degree times its root valuation.
The original field K is retained even if alpha^n has smaller minimal degree.
This is the2-primary part of the original norm, distinct from scalar coefficient content or the total all-prime logarithmic norm.

**C. Complete pairwise synchronization at one linear time.**
EVERY pair of DISTINCT occurring orders o,o' has a SINGLE simultaneous exponent

    n=lcm(o,o')<=Q^2<=8d.

It is odd, so at that SAME n every original root in both order groups has depth EXACTLY1.
Other activated groups remain included.
Every individual order is at most Q<=sqrt(8d).
Thus all original root mass lies at individually short orders, and every pair can be synchronized at a uniformly degree-linear exponent at the SAME fixed good prime2.
This does not assert that all groups share such an exponent.

**D. Uniform quantitative sublinear local income on EVERY fixed linear window.**
Define the explicit finite constants

    K_div=product_(p in{2,3,5,7,11,13})(1-p^(-1/4))^(-2),
    T_*=(1-2^(-1/4))^(-2),
    K_*=sqrt8*(log2)*K_div*T_*.

For EVERY integer v>=1 the locally proved divisor bound is tau(v)<=K_div v^(1/4).
Writing n=2^r v with v odd, the COMPLETE valuation formula gives

    A_2(n)<=(log2)K_div T_* Q n^(1/4).

Consequently for EVERY real C>0 and every integer1<=n<=Cd,

    A_2(n)/d<=K_* C^(1/4)d^(-1/4).

An empty integer range has maximum0.
Hence for EVERY FIXED C>0,

    max_(1<=n<=C d_Q) A_2(n)/d_Q ->0 as Q->infinity.

The bound includes arbitrarily high binary powers in n; it is not a depth-one or odd-time restriction.
The constant K_* is independent of Q,n,C.
Complete pairwise degree-linear synchronization therefore does NOT imply positive-linear contribution from this prime at ANY degree-linear common exponent, absent further hypotheses.

**E. Full original Mahler cost is Theta(d), with explicit thresholds.**
Write m(P_Q)=log M(P_Q), with ordinary multiplicative Mahler measure, not normalized height.
The COMPLETE original polynomial satisfies

    ||P_Q||_1<=19*2^s-18,
    m(P_Q)<(d/2)log2+log19.

For s>=400 and10sqrt(log(s)/s)<=1/24, one also has

    m(P_Q)>=[d/48]log[(1+sqrt17)/4].

These sufficient conditions hold for all sufficiently large Q.
Thus m(P_Q) is of order d as Q grows.
The lower bound uses the ACTUAL integer degree-s trace polynomial T, its proved simple roots and M(T)<=sqrt(1+324s)<=s.
The accepted Pri11-U001 discrepancy statement applies with N=s,A=2,R=2 to the explicitly retained real compact test.
It yields at least s/24 traces with absolute imaginary part>1/2.
The COMPLETE inverse pair associated to each such trace contributes more than log[(1+sqrt17)/4] to m(P_Q); all original pairs are counted.
No powered-degree substitution, omitted cofactor, Salem hypothesis or singular limiting logarithm is used.

For every n the full original norm still obeys log C_n<=d log2+n m(P_Q).
Parts B--D bound only A_2(n); other rational primes may contribute substantial income.
The theorem does not say log C_n=o(d) on linear windows.

**F. Exact failed transfer and limits.**
This is an ACTUAL reciprocal irreducible nontorsion integer-unit counterfamily to the inference that full original residue-root mass plus pairwise degree-linear synchronization at one fixed good prime forces linear local income at some degree-linear exponent.
All degree/order/depth/construction costs and original root multiplicities are paid.
The control is FAR from m(P)->0 and gives no counterexample under an added genuine near-one hypothesis.

No uniform bound on o/ord_o(2), where ord_o(2) is the residue-degree order of2 modulo o, is asserted for this dense order family.
The older L217 control has a different bounded order/degree hypothesis and its own incompatible-pair structure; neither theorem silently inherits the other's hypotheses.
The conjunction of pairwise synchronization with additional bounded order/degree efficiency remains outside this result.
No all-prime norm upper bound, near-one sequence, new universal positive arithmetic-income mechanism, improved L168 cost theorem or unrestricted Mahler gap is supplied.

## Current assessment
[Selected decision](#decision-independent-current-whole-review-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:44 |
| status | open |
| reason | Register the complete actual fixed-prime2 pairwise-synchronization counterfamily, all original roots and binary depths, exact reciprocal irreducible construction, quantitative all-window sublinear local income and full Theta(d) Mahler costs. The ENTIRE original00:30:51 D38 is retained. R309 whole-reviewed that original mathematics; its reviewer now authors this new wrapper, which requires another actual extraction review before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Entire original author body](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [L64 complete local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [L74 original norm convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [L74 stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [L217 actual lift antecedent](../ledger/Yin_L_G0217_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [L217 full Mahler method](../ledger/Yin_L_G0217_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Pri11-U001 accepted discrepancy statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [L168 original finite income gate](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T16:55 |
| status | proved |
| reason | Adopt original whole R309 and separate ACTUAL extraction R417. Fix the actual dense-order reciprocal-unit family with complete pairwise short synchronization but sublinear full-depth binary income at every fixed linear window. Full Mahler cost is Theta(d); this excludes only the stated pairwise transfer and supplies neither a near-one counterexample nor an all-prime norm-income bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Entire original author body](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [L64 complete local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [L74 original norm convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [L74 stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [L217 actual lift antecedent](../ledger/Yin_L_G0217_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [L217 full Mahler method](../ledger/Yin_L_G0217_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Pri11-U001 accepted discrepancy statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [L168 original finite income gate](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0794_v2.md#c83-pairwise-binary-actual-extraction-finding) | ENTIRE actual A--F, complete preserved original and all exact local/analytic/source/cost interfaces; original R309 whole scope unchanged. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Argument](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [Dependency](../ledger/Yin_L_G0217_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [Dependency](../ledger/Yin_L_G0217_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [Support](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Support](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |
| review | [Review](../audits/reviews/Yin_R_G0794_v2.md#c83-pairwise-binary-actual-extraction-finding) | ENTIRE actual A--F, complete preserved original and all exact local/analytic/source/cost interfaces; original R309 whole scope unchanged. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Argument](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [Dependency](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [Dependency](../ledger/Yin_L_G0217_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [Dependency](../ledger/Yin_L_G0217_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [Support](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Support](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |
| review | [Review](../audits/reviews/Yin_R_G0794_v2.md#c83-pairwise-binary-actual-extraction-finding) | ENTIRE actual A--F, complete preserved original and all exact local/analytic/source/cost interfaces; original R309 whole scope unchanged. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Exact retained argument](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [Exact retained dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [Exact retained dependency](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [Exact retained dependency](Yin_C_G0527_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [Exact retained support](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Exact retained support](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0794_v2.md#c83-pairwise-binary-actual-extraction-finding) | ENTIRE actual A--F, complete preserved original and all exact local/analytic/source/cost interfaces; original R309 whole scope unchanged. |


### Decision independent-current-whole-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:10 |
| status | proved |
| reason | The current finding is SELF because its initial complete argument input included author-validation conclusions beyond the necessary derivation. Adopt the separately organized current fixed-target finding after complete statement and retained-argument inspection, including late extensions, actual costs, controls, necessary mathematical interfaces and source limits, while excluding credited comparison scopes first separately checked after old-review exposure. The initial mathematical conclusion was formed at 2026-10-22T22:47 UTC before old-target review comparison. The finding records the exact interface and later credited-comparison reading sequence. Preserve fixed mathematics, historical decisions, all non-review premises and their scopes; retain earlier findings in their original homes at their actual recorded relationships and checking scopes. This selects current review evidence and supplies no new research, Task completion or execution resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement: statement](#statement) | Entire A--F, every Q>=64 and original degree/root, actual good prime2, complete pairwise times, all binary depths, every fixed linear window, explicit constants/cost thresholds and exact excluded scopes. |
| argument | [Argument: argument](#argument) | COMPLETE actual00:30:51 D38 question/reuse/candidate history, Sections1--7/equations1--19, nine explicit anchors, full construction/cost/source/role limits and freeze. |
| dependency | [Dependency: direct-etale-frobenius-lift](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Unramified finite complete rings, unit derivatives and exact simple-root Hensel lifting at p2. |
| dependency | [Dependency: content-versus-ideal-norm](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Complete original field norm and residue-degree/ramification weighting, distinct from scalar content and powered minimal degree. |
| dependency | [Dependency: fixed-prime-actual-growth](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Exact odd-power preservation and stable binary growth; the new construction independently proves both first binary depths. |
| dependency | [Dependency: binary-depth-and-irreducible-realization](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | Credited trace/Hensel/CRT/Eisenstein mechanism, fully adapted and checked for the new dense order set; no old two-factor orbit or bounded o/f hypothesis imported. |
| dependency | [Dependency: efficient-order-construction-full-measure-cost](Yin_C_G0527_v1.md#efficient-order-construction-full-measure-cost) | Bounded-coefficient trace/full-polynomial cost mechanism, with its full local derivation and actual new-input hypotheses retained. |
| dependency | [Dependency: pri11-u001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Sole external analytic premise: integer/simple-zero degree>=55 compact Lipschitz theorem, used only at actual N=s>=400,A=2,R=2,M(T)<=s and the retained sufficient size condition. Original statement/applicability proof limits unchanged. |
| support | [Support: general-unit-finite-income-criterion](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Interpretation and comparison: actual same-exponent eta*d income at n<=Cd forces a measure bound, but this family supplies no universal positive income and is not near one. |
| support | [Support: pairwise-synchronization-whole-independent-finding](../audits/reviews/Yin_R_G0309_v1.md#pairwise-synchronization-whole-independent-finding) | ENTIRE original00:30:51 D38 and exact actual inputs independently reconstructed before this wrapper. R309 does not inspect or adopt the current statement/extraction prospectively. |
| review | [Current SELF finding](../audits/reviews/Yin_R_G0794_v2.md#g83-current-independent) | Complete current mathematical statement and retained proof, including all late extensions, paid arithmetic, useful controls and accepted necessary interfaces at their exact scopes; exclude post-initial credited comparison scopes identified by the finding; initial conclusion 2026-10-22T22:47 UTC, then old-finding comparison; actual interface and credited-comparison reading limits are disclosed in the finding. |

## Registration and complete preservation

The [original D38 entire-author freeze](#pairwise-synchronization-entire-author-freeze) is extraction ancestry, not a mathematical dependency.
The actual original contains28822 characters,256 lines and9 explicit anchors.
The ENTIRE body is retained below, with only duplicate author/framework front matter removed, the first title demoted one hash, and ordinary line-ending/terminal/separating blank-line normalization.
Every original candidate/history paragraph, all19 numbered equations, construction, failed transfer, quantitative bound, source/contribution limit and actual freeze is preserved.
Existing ../ledger/ and ../audits/ links remain valid and require no rebasing.
No proof is replaced by a summary.

The matrix-recovery AI remains the original proof author.
Rounding-recovery's R309 is a whole independent review of that original only; the same AI NOW contributes the present exact statement/wrapper and cannot independently review it.
Root supplied the broad research question and may separately perform the new actual extraction review.
Historical pending-review language in the retained body remains at its actual date; the selected initial decision identifies the present extraction as pending review.
No original proof or review is adopted, retired or rewritten by this registration.

The Pri11 external input remains exactly its accepted statement/applicability scope; no potential-theory source-proof audit, full-source acceptance or new acquisition is claimed.
L217's earlier trace/construction/cost methods and L64/L74's local algebra are credited at their exact scopes.
The new dense order family, explicit trace prescription, quadratic degree and divisor-depth bounds are project deductions, not new general Hensel or discrepancy theorems.
No native mathematical execution, new J or unrestricted Task conclusion accompanies this extraction.

## Argument

## Pairwise short residue-order synchronization need not supply linear local cyclic income

Date: 2026-10-12T16:20.
Human author Yin.
New AUTHOR inquiry by g0001_matrix_recovery under the continuing G0001 instruction.
Root requested a distinct arithmetic synchronization or valuation direction, without supplying this candidate or proof.
No native mathematical program or new source acquisition is proposed.

## Responsible question and bounded reuse

The actual current S1/S3/S4/S8 frontier was read, including C75's already fixed matrix boundary and the separate ongoing all-energy packet work.
The main gate remains actual same-exponent income A(n)>=eta*d at ONE n<=C*d, with the full original norm and all conjugates retained.
The [L168 actual general-unit cost](../ledger/Yin_L_G0168_v1.md#general-unit-actual-product-cost) and [finite income implication](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) are cost/conditional interfaces, not a new source of income.

The bounded arithmetic reuse pass read [L74's original norm valuation convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm), its full local table and stable tail, [L78's actual cyclotomic layers](../ledger/Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers), [L159's short-order capacity](../ledger/Yin_L_G0159_v1.md#good-prime-short-order-capacity), [L188's complete layer-average normalization](../ledger/Yin_L_G0188_v1.md#complete-cyclic-layer-average), [L213's full selected-depth escape](../ledger/Yin_L_G0213_v1.md#full-depth-fixed-scope), [L217's individually efficient but incompatible-order controls](../ledger/Yin_L_G0217_v1.md#efficient-order-fixed-scope), and [L221's order-adapted squarefree auxiliary](../ledger/Yin_L_G0221_v1.md#order-auxiliary-fixed-scope).
Cross-time averaging, bounded residue-degree control, individually affordable orders and merely replacing a cyclic polynomial by a product of cyclotomic blocks are already accounted for.
Repeating those statements is not the intended contribution.

<a id="pairwise-synchronization-responsible-candidate"></a>
## Candidate and proposed distinguishing test

Test the stronger candidate that COMPLETE original root mass at one fixed good prime, with EVERY PAIR of occurring residue orders jointly realizable at a degree-linear common exponent, must force linear local income at some degree-linear exponent.
This adds pairwise coordination to ordinary degree-linear individual affordability.
It is distinct from L217's bounded ratio o/f: the present family does not assert that ratio is bounded.
It does not presuppose a small-total-measure theorem.

The proposed control uses ALL odd orders5<=o<=Q at the fixed prime2.
Let R_Q(t)=product Phi_o(t) over those orders and d_Q=deg R_Q=sum phi(o).
The coefficient-root capacity makes d_Q quadratic in Q, while every pair lcm is at most Q^2.
A reciprocal actual integer lift with squarefree reduction R_Q mod2 and exactly prescribed first binary depths should therefore have all pairs synchronized by8d_Q, yet only divisor-many order groups at any ONE n<=C d_Q.
The exact full valuation candidate is

    v_2(C_n)=(1+v_2(n)) sum_(5<=o<=Q, o odd, o|n) phi(o).

The full direct construction, not an arbitrary incidence array, must establish this formula.
The first-depth prescription will adapt the already proved trace/Hensel/Eisenstein method of L217.
The proposed explicit lift uses the trace polynomial T_0 and H congruent to x^2 T_0' modulo T_0 over F_2: its local first residue should be the trace theta, which avoids0 and1 for every selected order.
All actual roots, including inversion-stable Frobenius orbits, must be checked.
This is an adaptation of old algebra, not a new Hensel principle.

The required cost boundary is essential: this construction is expected to have m(P_Q) of order d_Q, as in the old bounded-coefficient trace lift.
It would refute only the proposed pairwise-to-one-time transfer without a near-one hypothesis, not produce a near-one sequence or bound all other-prime norm income.
The proof must retain the complete original signed norm, all binary depths, actual polynomial degree and upper/lower Mahler costs.
All substantive proof and failures will remain here before independent review.
No numerical or native enumeration is authorized or used.

<a id="pairwise-complete-family-and-theorem"></a>
## 1. Exact family and the new pairwise obstruction

For EVERY integer Q>=64 let

    O_Q={o:5<=o<=Q, o odd},
    R_Q(t)=product_(o in O_Q) Phi_o(t),
    d=d_Q=sum_(o in O_Q) phi(o), s=d/2.                  (1)

Here phi is Euler's totient, and Phi_o the complete cyclotomic polynomial.
Every selected order is odd and greater than3.
The elementary estimate proved below is

    Q^2/8<=d<=(Q+1)^2/4.                                (2)

There is an EXPLICIT finite coefficient construction of a monic irreducible reciprocal nontorsion unit polynomial P_Q in Z[t] of EXACT original degree d, with constant coefficient1, such that the following statements all hold.

1. The prime2 does not divide disc(P_Q), and the complete reduction is P_Q mod2=R_Q mod2.
   For each o in O_Q, EXACTLY phi(o) of the original d roots reduce to order o; these groups contain ALL original roots.
2. At EVERY one of these original local roots alpha of residue order o, with normalized v_2(2)=1, both v_2(alpha^o-1)=1 and v_2(alpha^o+1)=1.
   Consequently the complete original-field norm satisfies, for EVERY n>=1,

    C_n=abs(Norm_(Q(alpha)/Q)(alpha^n-1)),
    v_2(C_n)=(1+v_2(n)) sum_(o in O_Q, o|n) phi(o),
    A_2(n)=(log2)v_2(C_n).                              (3)

All initial depths and later lifts are included.
The original full signed norm is the integer Res(P_Q,t^n-1); its absolute value is C_n.
No powered-field degree replaces d or any original root in(3).

3. EVERY pair of distinct occurring orders o,o' is simultaneously present at the SINGLE exponent lcm(o,o')<=Q^2<=8d.
   At that exponent every root of BOTH groups has depth exactly1.
   Every single order is at most Q<=sqrt(8d).
   Thus all original mass occurs at individually short orders and every pair is jointly short, at ONE fixed good prime.
4. Nevertheless for EVERY fixed real C>0,

    max_(1<=n<=C d) A_2(n)/d ->0 as Q->infinity.         (4)

An explicit universal constant K_* below gives the bound K_* C^(1/4) d^(-1/4).
Empty integer ranges have maximum0.
Thus even COMPLETE pairwise degree-linear coordination does not force positive-linear income from this prime at one degree-linear exponent.

5. The full original Mahler cost is bounded by

    m(P_Q)<(d/2)log2+log19,
    m(P_Q)>=[d/48]log[(1+sqrt17)/4]                     (5)

whenever s>=400 and10sqrt(log(s)/s)<=1/24 for the lower bound.
This holds for all sufficiently large Q.
Hence this is an actual fixed-prime synchronization counterfamily with m(P_Q) of order d, NOT a near-one counterfamily or a bound on other-prime income.
It does not contradict L168 or settle the unrestricted uniform gate.

The number and mass of groups which one exponent activates remain distinct from pairwise feasibility.
The result excludes this precise stronger proposed transfer without a small-total-measure hypothesis; it does not assert that pairwise synchronization is useless when accompanied by a further genuinely near-one structural theorem.

<a id="pairwise-quadratic-order-capacity"></a>
## 2. Complete order mass really is quadratic

Let M=ceil(Q/2), the number of odd integers in[1,Q], and let G_Q count ORDERED coprime pairs of such odd integers.
Counting by their maximum gives

    G_Q=1+sum_(3<=o<=Q, o odd) phi(o), d=G_Q-3.         (6)

Indeed for each odd maximum o>1, exactly phi(o)/2 smaller positive coprime integers are odd: pairing a with o-a exchanges parity.
Each smaller choice appears in two orders.
The pair(1,1) supplies1; removing o3 removes phi(3)=2.

Every noncoprime odd pair has a common odd prime.
The number of odd multiples of any odd integer h within[1,Q] is at most Q/(2h)+1/2.
A union bound, enlarged from odd primes to ALL odd integers h>=3, therefore gives

    M^2-G_Q
      <=sum_(3<=h<=Q, h odd)(Q/(2h)+1/2)^2
      <=Q^2/16+(Q/4)log Q+Q/8.                         (7)

For the squared reciprocal sum, writing h=2j+1 gives

    sum_(h>=3, h odd)1/h^2
       <sum_(j>=1)1/[4j(j+1)]=1/4.

For the reciprocal sum, integrate1/x on each interval[h-2,h] to obtain sum_(3<=h<=Q, h odd)1/h<=(1/2)log Q.
There are at most Q/2 summands.
These prove every term in(7), without a prime-distribution or asymptotic-totient theorem.

Since M^2>=Q^2/4,

    d>=3Q^2/16-(Q/4)log Q-Q/8-3.

For Q>=64 this is at least Q^2/8: equivalently Q-4log Q-2-48/Q>=0, which follows from log Q<=Q/8 on that range.
The latter follows at64 and then by differentiation.
For the upper bound, phi(o)<=o and the sum of the first M positive odd integers is M^2<=(Q+1)^2/4.
This proves(2).
In particular d is positive and even, and s tends to infinity with Q.

<a id="pairwise-actual-reciprocal-lift"></a>
## 3. Actual reciprocal lift with ALL first binary depths prescribed

This adapts the already retained [C527 trace/Hensel/Eisenstein construction](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization).
The difference is the complete dense order set and an explicit common prescription which covers inverse-stable Frobenius orbits as well.
The elementary complete-ring/Hensel interface was directly reread in [L64](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift); no new local-field theorem is imported.

For each odd o>1, reciprocity and even degree give a unique monic integer S_o(x) of degree phi(o)/2 with

    Phi_o(t)=t^(phi(o)/2) S_o(t+t^-1).

To see integrality directly, t^(-phi(o)/2)Phi_o is a symmetric integer Laurent polynomial.
For every j>=1, t^j+t^-j is a monic integer polynomial in x=t+t^-1 by V_(j+1)=x V_j-V_(j-1), V_0=2,V_1=x.
The triangular leading terms supply S_o without division by2.
Put

    T_0(x)=product_(o in O_Q) S_o(x), deg(T_0)=s,
    R_Q(t)=t^s T_0(t+t^-1).                             (8)

The reduction of R_Q modulo2 is squarefree: every selected order is odd, t^o-1 has distinct roots, and the primitive-order root sets are disjoint.
Its roots are all nonzero and none equals its inverse.
The map zeta->theta=zeta+zeta^-1 identifies EXACTLY an inverse pair, because its fibers solve t^2-theta*t+1.
Thus T_0 mod2 has s DISTINCT roots.
Traces from different orders cannot coincide, and no irreducibility assertion about an individual S_o is needed.

Every such trace theta is neither0 nor1.
A zero trace would force zeta=1 in characteristic2.
A trace1 would force zeta^2+zeta+1=0 and hence order3.
Both cases were excluded from O_Q.
Therefore T_0'(theta), theta and theta-1 are all nonzero in the actual residue field.

Choose H in Z[x], deg H<s, with coefficients0 or1, as the unique remainder satisfying

    H congruent to x^2 T_0'(x) modulo(T_0(x),2).         (9)

The division is in F_2[x] by the monic T_0 mod2.
Now specify a monic integral T of degree s by

    T congruent to T_0+2H modulo4,
    T congruent to (x-2)^s+3 modulo9.                   (10)

Coefficientwise Chinese remaindering gives a unique residue modulo36 for every lower coefficient.
Choose its representative in[-18,17].
Thus every lower coefficient of T has absolute value at most18.
Define the ACTUAL original polynomial

    P_Q(t)=t^s T(t+t^-1).                               (11)

It is monic integral reciprocal of degree d=2s with constant coefficient1.
The second congruence in(10) gives

    P_Q(t+1) congruent to t^(2s)+3(t+1)^s modulo9.

Every nonleading coefficient is divisible by3 and its constant coefficient is3 modulo9.
Eisenstein at3 proves irreducibility of P_Q.
It also proves irreducibility of T indirectly: a nontrivial monic integer factorization of T would produce a nontrivial integer factorization of(11).
In characteristic zero T and P_Q consequently have simple roots.

Modulo2, P_Q is exactly R_Q, so2 does not divide its polynomial discriminant.
Every original2-adic root lies in an unramified extension, as in the directly proved L64 interface.
Fix ANY primitive residue root of order o in O_Q and its primitive o-th root-of-unity lift zeta in that extension.
Simple-root lifting of t^o-1 gives this lift, of exact order o.
Put theta=zeta+zeta^-1, so T_0(theta)=0.
There is a unique root z of T near theta, then a unique root alpha of t^2-z t+1 near zeta.
The latter derivative reduces to zeta-zeta^-1, which is nonzero.

In the unramified integer ring, first-order expansion modulo4 gives

    T(theta)-T(z)=(theta-z)U, U congruent T_0'(theta) mod2,
    z-theta=(alpha-zeta)(1-1/(alpha zeta)),
    a:=overline[(alpha^o-1)/2]
      =-overline(o) overline(zeta)^(-1) overline[H(theta)]
         /[overline(T_0'(theta))(1-overline(zeta)^(-2))]
      =overline[H(theta)]/[overline(T_0'(theta)) overline(theta)]
      =overline(theta).                               (12)

All displayed denominators are units.
The second equality for a uses characteristic2, o odd and zeta-zeta^-1=theta in the residue field; the final equality is the explicit prescription(9).
Terms of order at least two in alpha-zeta are divisible by4, because alpha-zeta is divisible by2.
Thus no deeper term is dropped from the needed first residue.

Since overline(theta) is neither0 nor1, both(alpha^o-1)/2 and(alpha^o+1)/2 have nonzero residue: their residues differ by1.
Consequently BOTH valuations in part1.2 are exactly1.
This argument applies to EVERY primitive residue root, including its inverse and all Frobenius conjugates.
It does not assume that an order has exactly two irreducible factors or that inversion exchanges two distinct Frobenius orbits.
All d original roots are covered.
This completes the promised actual irreducible unit construction and the depth prescription.

<a id="pairwise-exact-income-and-divisor-bound"></a>
## 4. Exact original income and all-time synchronization cost

Use the original degree-d field generated by any root alpha of P_Q.
At an original local root of residue order o, a nonmultiple of o has valuation0.
At exponent o, both factors alpha^o-1 and alpha^o+1 have valuation1, so alpha^(2o)-1 has valuation2.
If v_2(y-1)>=2, the two terms in y^2-1=2(y-1)+(y-1)^2 have distinct valuations, giving v_2(y^2-1)=v_2(y-1)+1.
An odd power preserves any positive valuation, since its geometric-sum quotient reduces to1.
Therefore for EVERY n>=1,

    v_2(alpha^n-1)=1+v_2(n) if o divides n,
                   0 otherwise.                       (13)

These finite values also establish nontorsion; a root of unity would give an infinite valuation at some n.
The full norm is nonzero for every n.
Summing over ALL phi(o) original roots in each order group proves(3), including every residue-degree contribution and every later binary depth.
Equivalently each irreducible factor contributes its full degree times its root valuation.
The original signed resultant is retained before the absolute value; the valuation sum does not replace it by a primitive quotient or a selected smaller-field norm.

For any distinct o,o' in O_Q, n=lcm(o,o') is odd and at most Q^2<=8d.
Formula(13) then gives depth exactly1 at EVERY root of both groups.
This is simultaneous same-exponent arithmetic, not addition of two values from different times.
Any other groups activated at that exponent are retained as well.

Nevertheless define the explicit finite constants

    K=product_(p in{2,3,5,7,11,13})(1-p^(-1/4))^(-2),
    T_*=(1-2^(-1/4))^(-2), K_*=sqrt8*(log2)*K*T_*.

For EVERY integer v>=1 the divisor count satisfies

    tau(v)<=K v^(1/4).                                 (14)

Indeed if p>=17, then a+1<=2^a<=p^(a/4) for every integer a>=0.
For each smaller prime, (a+1)p^(-a/4) is at most the positive series sum_(b>=0)(b+1)p^(-b/4)=(1-p^(-1/4))^(-2).
Multiplication over the prime factorization proves(14), including v1.
This elementary, nonoptimal divisor bound is fully proved here, not a new external number-theoretic estimate.

For n=2^r v with v odd, only orders dividing v contribute.
Each phi(o)<=o<=Q, and there are at most tau(v) such orders.
Formula(3) and(14) give

    A_2(n)
      <=(log2)(r+1)Q tau(v)
      <=(log2)K Q n^(1/4)(r+1)2^(-r/4)
      <=(log2)K T_* Q n^(1/4).                         (15)

The last inequality bounds a single nonnegative term by the complete series sum_(r>=0)(r+1)2^(-r/4)=T_*.
It charges ALL high powers of2 rather than incorrectly imposing a depth-one cutoff.
With Q<=sqrt(8d), for every n<=Cd,

    A_2(n)/d<=K_* C^(1/4) d^(-1/4).                    (16)

This proves(4) for every fixed C, with a constant independent of Q,n and every original root.
The exponent1/4 is a convenient sufficient choice, not an optimality claim.
Increasing the allowed fixed C never supplies a positive-linear lower bound from this prime along the family.

<a id="pairwise-complete-mahler-cost"></a>
## 5. Full original Mahler cost and the near-one boundary

The cost mechanism here is deliberately credited to the [C527 bounded-coefficient trace analysis](Yin_C_G0527_v1.md#efficient-order-construction-full-measure-cost).
Its hypotheses are checked for the ACTUAL new T and P_Q, and the argument is included so no applicability is hidden.
The sole external theorem used is the already accepted [Pri11-U001 statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001), which was actually read for this inquiry.
Its potential-theory proof and source inputs retain their original statement/applicability acceptance depth; no new source acquisition or full source-proof audit is claimed.

The coefficient bounds from(10) give, by the triangle inequality and the full coefficient sum of(t+t^-1)^j,

    ||P_Q||_1<=2^s+18sum_(j=0)^(s-1)2^j=19*2^s-18.

Jensen's formula then gives the strict upper bound in(5).
Every original coefficient/root is included.
Also Jensen, Parseval and concavity of log give

    M(T)<=||T||_2<=sqrt(1+324s)<=s for s>=400.           (17)

Define real functions on C by

    chi(z)=min(1,(2-|z|)_+),
    g(z)=min(1,(|Im z|-1/2)_+), phi(z)=chi(z)g(z).

Both factors lie in[0,1] and are globally1-Lipschitz.
Thus phi is globally2-Lipschitz, at most1, and supported in the disk of radius2.
On the two unit-circle arcs with arguments[pi/3,2pi/3] and[4pi/3,5pi/3], chi=1 and g>=1/4.
Their total normalized arclength is1/3, so integral phi dmu>=1/12.

The ACTUAL degree-s integer polynomial T has simple roots, and s>=400 exceeds Pri11's threshold55.
Apply the accepted statement with N=s, Lipschitz constant2, support radius2 and(17).
For its complete root list z_1,...,z_s this gives

    (1/s)sum_j phi(z_j)>=1/12-10sqrt(log(s)/s).          (18)

Under10sqrt(log(s)/s)<=1/24, at least s/24 of these roots have |Im z_j|>1/2.
Each z_j corresponds to the complete inverse pair of roots of t^2-z_j t+1 in P_Q.
If R_j>=1 is their larger modulus, writing that root as R_j exp(i theta) gives |Im z_j|<=R_j-R_j^-1.
Therefore R_j>(1+sqrt17)/4 whenever |Im z_j|>1/2.
Keeping BOTH members of EVERY original inverse pair,

    m(P_Q)=sum_(j=1)^s log R_j
       >=(s/24)log[(1+sqrt17)/4]
        =(d/48)log[(1+sqrt17)/4].                       (19)

Equations(17)--(19) supply an explicit sufficient size condition, which holds for all sufficiently large Q by(2).
They use no claim about the degree of a power of alpha, no Salem classification, no discarded neutral conjugates and no interchange of singular limiting logarithms.

In particular the new control is FAR from a hypothetical m(P)->0 family.
For every n its complete norm also retains the elementary original-root expense log C_n<=d log2+n m(P_Q); formula(16) only controls the2-primary contribution inside that same full norm.
Other rational primes may provide large income, and no bound on their total is asserted.
The actual high measure cannot be silently removed by dividing degree, passing to the trace polynomial, replacing alpha by a root of unity, or using only the selected prime.

<a id="pairwise-synchronization-limits-and-next-gate"></a>
## 6. Failed transfer, actual progress and remaining question

The proposed transfer from complete pairwise degree-linear synchronization to one degree-linear exponent with A_2(n)>=eta d is FALSE for actual irreducible reciprocal nontorsion units without an extra near-one hypothesis.
Here the prime is fixed and good, every original root belongs to a selected group, each order is only O(sqrt d), EVERY pair has common time<=8d, all initial depths are explicitly one, and the COMPLETE later valuations are paid.
Yet(16) tends to zero on every fixed linear window.
There is no unnormalized time sum or abstract adversarial array substituting for actual arithmetic.

This differs from the already fixed L217 control: that construction has individually efficient high-degree order groups whose widely separated pairs may have large lcm.
The present dense full order set makes EVERY pair affordable, while divisor-count growth still prevents a single time from collecting a positive proportion with linear weighted income.
The Hensel/Eisenstein and Mahler-cost methods are reused/adapted explicitly, not counted as new general tools.
The new mathematical discriminator is the insufficiency of this stronger pairwise coordination condition.

The general L168/L209 cost theorem still says that any actual same-exponent income eta d at n<=Cd forces a positive measure bound.
The present proof supplies no uniform income mechanism for all inputs, no genuine near-one counterexample and no all-prime upper bound.
A successful repair must use additional multi-order concentration at one common time, a specific near-one restriction which rules out this dispersion, or a genuinely different fully charged scalar auxiliary.
Neither the existing order entropy nor this pairwise counterexample proves that such a repair exists.

The candidate's potential failure at inversion-stable residue orbits was resolved by the explicit trace prescription H=x^2 T_0' modulo(T_0,2), which makes the normalized first residue overline[(alpha^o-1)/2] equal overline(theta) at EVERY original root; it does not depend on the two-factor pattern of L217.
The exclusion of orders1 and3 is essential to force both first binary depths exactly one.
The quadratic degree count, same-time pairwise bound, all-depth divisor estimate and full Mahler boundary are proved above.
No coefficient or root table was enumerated by a mathematical program.

The comparison with L217 is not a logical inclusion of its hypotheses: no fixed bound on o/ord_o(2) is asserted for this dense family.
The new condition checked here is complete pairwise synchronization at a fixed degree-linear time cost, together with the stated absolute O(sqrt d) individual-order bound.
Combining pairwise synchronization with additional fixed order/degree efficiency or genuine near-one restrictions remains outside this counterexample.

<a id="pairwise-actual-inputs-and-author-check"></a>
## 7. Actual dependencies, contribution and complete author checking

The original full norm/valuation convention and stable binary lifting are retained from L74 and completely specialized in(12)--(16).
The finite unramified simple-root lifting used in Section3 is the directly read L64 interface.
The trace-polynomial, Chinese remainder, Eisenstein and full Mahler-cost mechanism is expressly credited to L217; its local hypotheses are reproved for the new complete order set, including inverse-stable Frobenius orbits.
Classical cyclotomic/Frobenius root counting, polynomial division, integer Chinese remaindering and Eisenstein are used at their explicit elementary scope.
The divisor estimate and quadratic degree lower bound are proved locally.
No novelty claim is attached to these methods.

The sole external analytic premise is the actually read accepted Pri11-U001 statement.
Its exact hypotheses here are the actual degree-s INTEGER trace polynomial T, its simple roots supplied by irreducibility, s>=400>=55, its independently established M(T)<=s, and the real globally2-Lipschitz test supported in radius2.
The constant is2(2*2+1)=10.
This is reuse at accepted statement/applicability scope, not a fresh source-proof inspection.
L168 is used to state the original unresolved income gate and interpret the result; the counterfamily never supplies small m and makes no inverse inference from its cost bound.

| Actual input | Precise use |
| --- | --- |
| [L74 original norm convention](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) and [stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Complete original-degree norm, root/residue-degree multiplicities and the exact binary tail, specialized explicitly with both first depths1. |
| [L64 complete local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Unramified complete rings and simple-root lifting at good prime2, without a missing first-squaring hypothesis. |
| [L217 actual lift](../ledger/Yin_L_G0217_v1.md#binary-depth-and-irreducible-realization) and [full Mahler cost](../ledger/Yin_L_G0217_v1.md#efficient-order-construction-full-measure-cost) | Credited construction/cost antecedents; the dense complete order set and explicit trace prescription have their full new derivation above. No old o/f bound or two-factor pattern is inherited. |
| [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | The single accepted quantitative discrepancy statement applied only to the actual trace polynomial and displayed compact Lipschitz test, with its prior source-proof limits. |
| [L168 finite income interface](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Original same-exponent linear-income gate and its conditional Mahler consequence, not a claimed lower income for this family or all inputs. |

The author reread the entire saved body and checked: the coprime odd-pair identity G_Q=d+3; the complete union-bound constants and Q>=64 threshold; even original degree and every cyclotomic trace factor; all reduction multiplicities and trace identifications; the exclusions of orders1 and3; the actual remainder H and both mod4/mod9 congruences; reciprocal constant1 and the Eisenstein translation; the two unit factors in the first-order expansion and the normalized first residue theta, distinct from H(theta); every original inverse/Frobenius orbit; BOTH first binary depths and all later n; the complete signed norm and unchanged original degree; every pair's one exponent and the difference from simultaneous activation of many groups; all six small-prime constants in the divisor estimate, the binary-depth series and the final d^(-1/4) bound; the exact trace/whole-polynomial coefficient costs, Pri11's10 constant and its explicit size threshold; and the distinction between this pairwise condition and L217's separate o/f condition.
The full original degree, all roots and log-radius contributions stay present.
These are AUTHOR checks, not independent mathematical review.

The earlier scoped structural check on this D and its five selected actual inputs returned checked6; structural validation is not proof acceptance.
No native mathematical computation, new J, source acquisition, prior proof edit or adoption occurred.

<a id="pairwise-synchronization-entire-author-freeze"></a>
## Entire-author freeze

Date: 2026-10-12T16:30.
Freeze the COMPLETE original question/reuse/candidate history and Sections1--7/equations(1)--(19), including the actual irreducible reciprocal family, full binary depths, pairwise common times, exact all-window local-income obstruction, every construction/source cost, author phrasing clarifications and the explicit limits.
g0001_matrix_recovery supplied all new mathematics and cannot independently review it.
Root supplied the broad arithmetic question only.
The existing L217/L64 algebra and Pri11 analytic statement retain their credited prior roles.

This is a complete AUTHOR proof draft ready for a separate WHOLE noncontributor review.
The result concerns insufficient pairwise synchronization of2-primary income on a deliberately large-measure actual family.
It does not bound the rest of the full cyclic norm, claim bounded o/ord_o(2), supply a near-one sequence or unrestricted uniform income, or resolve G0001.
No new numerical example is asserted and no native mathematical program was run.
