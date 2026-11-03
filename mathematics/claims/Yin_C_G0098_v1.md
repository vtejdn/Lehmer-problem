---
author: Yin
---
# Failure of a linear-in-density triple-capture bound in actual reciprocal units

Date: 2026-10-13T04:34.
Human author Yin.
The direct_triple author supplied the complete original D25 frozen at12:29, crediting averaged_lcm for the prior C96 finite-moment idea.
The actual_income reviewer separately WHOLE-reviewed that entire original in R335 and NOW authors this new statement/extraction, becoming a contributor to this actual wrapper.
R335 covers the original only.
This proof draft requires a different noncontributor to review its ACTUAL extraction before adoption.

## Statement

The results below refute the stronger uniform LINEAR-in-density estimate T_X<=K X H_X W.
They do NOT refute the unrestricted fixed-positive-triple-density implication, since no positive uniform lower bound for the constructed normalized density is supplied.

**A. Exact finite third-moment lower bound.**
For positive squarefree Q and real t>=1 set

    D_Q(t)={a:a divides Q, a<=t},
    W_Q(t)=sum_(a in D_Q(t))phi(a),
    T_Q(t)=sum_(a,b,c divide Q,lcm(a,b,c)<=t)phi(a)phi(b)phi(c),
    kappa_Q=max_(N divides Q)T_Q(N)/(N^2 W_Q(N)).

Triples are ORDERED and include every repeated label.
The full capacities are positive integers phi(a), and D_Q(t) is a nonempty divisor downset.
Then

    kappa_Q >= (1/3)product_(p divides Q)
                           (2-p^(-3))/(2-p^(-1)).

The product is unbounded along products of increasing primes after any fixed finite prime exclusion.
In particular let Q_j be the product of the first j odd primes and N_j the LEAST divisor attaining the displayed finite maximum.
With W_j=W_(Q_j)(N_j), T_j=T_(Q_j)(N_j), one has

    kappa_(Q_j)->infinity, N_j->infinity, W_j->infinity,
    h_j(n)=gcd(n,Q_j) for every1<=n<=N_j,
    H_(N_j)=N_j,
    T_j/(N_j H_(N_j) W_j)=kappa_(Q_j)->infinity,
    N_j/W_j<=kappa_(Q_j)^(-1/2)->0.

The maximizer is defined by an exact finite choice, not a claimed numerical optimization.
The proof includes all real thresholds, the infinite tail t>=Q, Q1 and all eight prime-membership patterns.
It uses no prime asymptotic beyond elementary reciprocal divergence.

**B. Actual odd-degree realization.**
For a selected odd Q=Q_j,N=N_j with W=W_Q(N)>1, put F(t)=product_(a in D_Q(N))Phi_a(t).
Its degree W is odd, constant coefficient-1, and reduction modulo2 squarefree.
Define a monic degree-W integer P with constant-1 by

    P congruent F modulo2,
    P congruent (t-1)^W+3t modulo9,

choosing each remaining coefficient as the unique representative in{0,...,17}.
Then P is irreducible by the Eisenstein translate P(t+1), is a nontorsion algebraic-unit polynomial, and2 does not divide its original polynomial discriminant.
Its complete actual root inventory at2 is EXACTLY w_a=phi(a) for a in D_Q(N), with original degree d=W.
Thus A's capture and ratio conclusions occur on actual inputs.
This first lift does not prescribe the higher binary depths and does not claim an upper bound for full A_2.

**C. Bounded deletion inside the reciprocal core.**
Continue with the same Q,N,W,T,kappa and remove orders1 and3.
Put

    O={a:a divides Q, 5<=a<=N},
    b=1+2*1_(3 divides Q and 3<=N)<=3,
    d=sum_(a in O)phi(a)=W-b,
    V=sum_(a,b',c in O,lcm(a,b',c)<=N)phi(a)phi(b')phi(c).

For all sufficiently large j, kappa>9, O is nonempty and d=2s is even.
One has

    V>=T-9W^2,
    V/(N^2 d)>=kappa-9->infinity,
    N/d->0,
    h_O(n)=gcd(n,Q)-1-2*1_(3 divides gcd(n,Q)) for n<=N,
    N-3<=H_N(O)<=N.

In particular V/(N H_N(O)d)->infinity.
The proof establishes positivity before replacing the denominator d by W; it retains the actual remaining degree.
This bounded deletion is not asserted to preserve a positive uniform triple density.

**D. Actual reciprocal construction and ALL binary depths.**
For every selected nonempty O in C, let S_a be the unique monic integer trace polynomial with

    Phi_a(t)=t^(phi(a)/2)S_a(t+t^-1),
    T0=product_(a in O)S_a, deg T0=s=d/2.

Let B be the coefficient0/1 lift of the remainder of x^2 T0'(x) modulo T0 over F2.
Define monic integer T of degree s by

    T congruent T0+2B modulo4,
    T congruent (x-2)^s+3 modulo9,

taking each lower coefficient in[-18,17] in its class modulo36, and put P*(t)=t^s T(t+t^-1).
Then P* is monic irreducible reciprocal nontorsion of ORIGINAL degree d and constant1, with fixed good prime2.
Its complete actual residue-root groups are exactly phi(a), a in O.

At EVERY original2-adic root alpha_i of residue order a, with v_2(2)=1, both v_2(alpha_i^a-1) and v_2(alpha_i^a+1) equal1, and for EVERY integer n>=1,

    v_2(alpha_i^n-1)=1+v_2(n) if a divides n,
                     0 otherwise.

Every inverse/Frobenius orbit, including inversion-stable orbits, is included.
The explicit first residue is the trace theta=zeta+zeta^-1, which is neither0 nor1 because orders1 and3 were removed.
No two-factor assumption, degree drop or first-squaring exception is omitted.

For an original root alpha generating K of degree d, the COMPLETE signed norm and local income are

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P*,t^n-1), C_n=|D_n|>0,
    A_2(n)=(log2)v_2(C_n)
          =(log2)(1+v_2(n))sum_(a in O,a divides n)phi(a).

Thus, for every integer1<=n<=N,

    A_2(n)<=N log2,
    A_2(N)=(N-1-2*1_(3|N))log2,
    max_(n<=N)A_2(n)/d->0.

This all-depth bound concerns the selected windows N=o(d) ONLY, not every larger fixed Cd window.
It bounds the2-primary part of the original norm, not the all-prime logarithmic norm.

**E. Full original cost and exact refuted estimate.**
For the reciprocal family,

    ||P*||_1<=19*2^s-18,
    M(T)<=sqrt(1+324s)<=s when s>=400,
    (d/48)log[(1+sqrt17)/4] <= m(P*)
                       <=(d/2)log2+log19

whenever s>=400 and10sqrt(log(s)/s)<=1/24 for the lower bound.
These sufficient thresholds hold eventually.
The accepted Pri11 statement is applied to the ACTUAL integer trace polynomial with simple roots, its full degree s, Lipschitz constant2, support radius2 and the stated compact test.
Its existing source-proof inspection limits are unchanged.
Therefore TOTAL m(P*)=Theta(d), far from a hypothetical m->0 sequence.

Writing X=N and T_X=V for the full surviving actual root inventory W=d gives

    T_X/(X H_X d)->infinity,
    H_X/d->0,
    max_(n<=X)A_2(n)/d->0, with X=o(d) and X<=d eventually.

Hence no absolute K gives T_X<=K X H_X W for every such ACTUAL reciprocal good-2 inventory.
Equivalently there is no uniform c>0 giving H_X>=c*delta*d^2/X for every positive actual density parameter delta=T_X/d^3.
This refutes the LINEAR dependence on delta.
The proof does NOT establish inf delta>0 and does not refute another dependence on FIXED delta, such as c(delta,C)d, the earlier conditional quadratic bound, actual near-one coverage or the unrestricted G0001 gap.

## Current assessment
[Selected decision](#decision-current-cyclic-norm-proof-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:34 |
| status | open |
| reason | Register the finite third-moment obstruction, both actual unit realizations, reciprocal all-depth selected-window bound and complete original cost, preserving the entire12:29 D25 and original whole R335. This newly authored statement/extraction awaits a distinct noncontributor review; fixed-positive-density capture and near-one G0001 coverage remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted results](#statement) | Entire A--E: finite product, all actual constructions and depths, selected-window restriction, full cost and linear-in-density versus fixed-density distinction. |
| argument | [Entire original proof and history](#argument) | Complete12:29 D25, original question/search/contribution history, Sections1--5/equations1--20, both realizations and all limits. |
| dependency | [C91 exact model](Yin_C_G0091_v1.md#statement) | Ordered repeated-label weights and original-root capture interpretation; no open universal K is used. |
| dependency | [L17 prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only elementary reciprocal-prime divergence and existing DLMF attribution, without a rate or discriminant theorem. |
| dependency | [C83 reciprocal construction](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) | Credited trace/CRT/Eisenstein and first-residue mechanism, fully adapted to the actual arbitrary finite O; no interval degree estimate inherited. |
| dependency | [C83 actual all-depth interface](Yin_C_G0083_v1.md#pairwise-exact-income-and-divisor-bound) | Both initial binary depths and stable all-n valuation; no interval-specific divisor bound used. |
| dependency | [C83 full cost](Yin_C_G0083_v1.md#pairwise-complete-mahler-cost) | Credited bounded-coefficient trace argument, explicitly rechecked for actual T and complete P*. |
| dependency | [L64 local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Good-prime unramified complete rings, uniformizer2 and simple-root lifting. |
| dependency | [L74 original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original-field resultant, every original root/residue-degree contribution and distinction from scalar content. |
| dependency | [L74 stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Odd-power preservation and stable binary tail, with first depths separately prescribed. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted statement/applicability only for the exact integer/simple-zero trace polynomial and compact Lipschitz test; no new original-proof audit. |
| support | [C96 credited moment mechanism](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof) | Extraction ancestry of the finite pair-moment idea; the new third-moment derivation is complete locally. |
| support | [Whole original independent finding](../audits/reviews/Yin_R_G0335_v1.md#third-moment-reciprocal-whole-independent-finding) | Entire original12:29 D25 only; no prospective review of this new extraction. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:37 |
| status | proved |
| reason | Adopt original whole R335 and distinct actual extraction R336 for the third-moment obstruction, both actual unit realizations, reciprocal complete-depth selected-window bound and total Mahler cost. The universal LINEAR-in-density estimate is refuted even for actual reciprocal good-2 units; fixed positive density is not established and its capture implication remains unresolved. The chosen window is X=o(d), and the reciprocal family's total m=Theta(d); no near-one or G0001 resolution follows. Shared method ancestry, all original history and source inspection limits are retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted results](#statement) | Entire A--E: finite product, all actual constructions and depths, selected-window restriction, full cost and linear-in-density versus fixed-density distinction. |
| argument | [Entire original proof and history](#argument) | Complete12:29 D25, original question/search/contribution history, Sections1--5/equations1--20, both realizations and all limits. |
| dependency | [C91 exact model](Yin_C_G0091_v1.md#statement) | Ordered repeated-label weights and original-root capture interpretation; no open universal K is used. |
| dependency | [L17 prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only elementary reciprocal-prime divergence and existing DLMF attribution, without a rate or discriminant theorem. |
| dependency | [C83 reciprocal construction](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) | Credited trace/CRT/Eisenstein and first-residue mechanism, fully adapted to the actual arbitrary finite O; no interval degree estimate inherited. |
| dependency | [C83 actual all-depth interface](Yin_C_G0083_v1.md#pairwise-exact-income-and-divisor-bound) | Both initial binary depths and stable all-n valuation; no interval-specific divisor bound used. |
| dependency | [C83 full cost](Yin_C_G0083_v1.md#pairwise-complete-mahler-cost) | Credited bounded-coefficient trace argument, explicitly rechecked for actual T and complete P*. |
| dependency | [L64 local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Good-prime unramified complete rings, uniformizer2 and simple-root lifting. |
| dependency | [L74 original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original-field resultant, every original root/residue-degree contribution and distinction from scalar content. |
| dependency | [L74 stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Odd-power preservation and stable binary tail, with first depths separately prescribed. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted statement/applicability only for the exact integer/simple-zero trace polynomial and compact Lipschitz test; no new original-proof audit. |
| support | [C96 credited moment mechanism](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof) | Extraction ancestry of the finite pair-moment idea; the new third-moment derivation is complete locally. |
| support | [Whole original independent finding](../audits/reviews/Yin_R_G0335_v1.md#third-moment-reciprocal-whole-independent-finding) | Entire original12:29 D25 only; no prospective review of this new extraction. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0336_v1.md#c98-third-moment-actual-extraction-finding) | Complete actual A--E, preserved original, finite moment and bounded deletion, both actual lifts, every root/depth, selected window, complete cost and fixed-density/source boundaries. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact restricted results](#statement) | Entire A--E: finite product, all actual constructions and depths, selected-window restriction, full cost and linear-in-density versus fixed-density distinction. |
| argument | [Entire original proof and history](#argument) | Complete12:29 D25, original question/search/contribution history, Sections1--5/equations1--20, both realizations and all limits. |
| dependency | [C91 exact model](Yin_C_G0091_v1.md#statement) | Ordered repeated-label weights and original-root capture interpretation; no open universal K is used. |
| dependency | [Retained elementary divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only elementary reciprocal-prime divergence and existing DLMF attribution, without a rate or discriminant theorem. |
| dependency | [C83 reciprocal construction](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) | Credited trace/CRT/Eisenstein and first-residue mechanism, fully adapted to the actual arbitrary finite O; no interval degree estimate inherited. |
| dependency | [C83 actual all-depth interface](Yin_C_G0083_v1.md#pairwise-exact-income-and-divisor-bound) | Both initial binary depths and stable all-n valuation; no interval-specific divisor bound used. |
| dependency | [C83 full cost](Yin_C_G0083_v1.md#pairwise-complete-mahler-cost) | Credited bounded-coefficient trace argument, explicitly rechecked for actual T and complete P*. |
| dependency | [L64 local lift](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) | Good-prime unramified complete rings, uniformizer2 and simple-root lifting. |
| dependency | [L74 original norm](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original-field resultant, every original root/residue-degree contribution and distinction from scalar content. |
| dependency | [L74 stable valuations](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Odd-power preservation and stable binary tail, with first depths separately prescribed. |
| dependency | [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted statement/applicability only for the exact integer/simple-zero trace polynomial and compact Lipschitz test; no new original-proof audit. |
| support | [C96 credited moment mechanism](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof) | Extraction ancestry of the finite pair-moment idea; the new third-moment derivation is complete locally. |
| support | [Whole original independent finding](../audits/reviews/Yin_R_G0335_v1.md#third-moment-reciprocal-whole-independent-finding) | Entire original12:29 D25 only; no prospective review of this new extraction. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0336_v1.md#c98-third-moment-actual-extraction-finding) | Complete actual A--E, preserved original, finite moment and bounded deletion, both actual lifts, every root/depth, selected window, complete cost and fixed-density/source boundaries. |


### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--E: finite product, all actual constructions and depths, selected-window restriction, full cost and linear-in-density versus fixed-density distinction. |
| argument | [Argument](#argument) | Complete12:29 D25, original question/search/contribution history, Sections1--5/equations1--20, both realizations and all limits. |
| dependency | [Dependency](Yin_C_G0091_v1.md#statement) | Ordered repeated-label weights and original-root capture interpretation; no open universal K is used. |
| dependency | [Dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Only elementary reciprocal-prime divergence and existing DLMF attribution, without a rate or discriminant theorem. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) | Credited trace/CRT/Eisenstein and first-residue mechanism, fully adapted to the actual arbitrary finite O; no interval degree estimate inherited. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-exact-income-and-divisor-bound) | Both initial binary depths and stable all-n valuation; no interval-specific divisor bound used. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-complete-mahler-cost) | Credited bounded-coefficient trace argument, explicitly rechecked for actual T and complete P*. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Good-prime unramified complete rings, uniformizer2 and simple-root lifting. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#content-versus-ideal-norm) | Full original-field resultant, every original root/residue-degree contribution and distinction from scalar content. |
| dependency | [Dependency](../ledger/Yin_L_G0074_v1.md#fixed-prime-actual-growth) | Odd-power preservation and stable binary tail, with first depths separately prescribed. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted statement/applicability only for the exact integer/simple-zero trace polynomial and compact Lipschitz test; no new original-proof audit. |
| support | [Support](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof) | Extraction ancestry of the finite pair-moment idea; the new third-moment derivation is complete locally. |
| support | [Support](../audits/reviews/Yin_R_G0335_v1.md#third-moment-reciprocal-whole-independent-finding) | Entire original12:29 D25 only; no prospective review of this new extraction. |
| review | [Review](../audits/reviews/Yin_R_G0336_v1.md#c98-third-moment-actual-extraction-finding) | Complete actual A--E, preserved original, finite moment and bounded deletion, both actual lifts, every root/depth, selected window, complete cost and fixed-density/source boundaries. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:42 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--E: finite product, all actual constructions and depths, selected-window restriction, full cost and linear-in-density versus fixed-density distinction. |
| argument | [Argument](#argument) | Complete12:29 D25, original question/search/contribution history, Sections1--5/equations1--20, both realizations and all limits. |
| dependency | [Dependency](Yin_C_G0091_v1.md#statement) | Ordered repeated-label weights and original-root capture interpretation; no open universal K is used. |
| dependency | [Dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Only elementary reciprocal-prime divergence and existing DLMF attribution, without a rate or discriminant theorem. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) | Credited trace/CRT/Eisenstein and first-residue mechanism, fully adapted to the actual arbitrary finite O; no interval degree estimate inherited. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-exact-income-and-divisor-bound) | Both initial binary depths and stable all-n valuation; no interval-specific divisor bound used. |
| dependency | [Dependency](Yin_C_G0083_v1.md#pairwise-complete-mahler-cost) | Credited bounded-coefficient trace argument, explicitly rechecked for actual T and complete P*. |
| dependency | [Dependency](Yin_C_G0241_v1.md#direct-etale-frobenius-lift) | Good-prime unramified complete rings, uniformizer2 and simple-root lifting. |
| dependency | [Dependency](Yin_C_G0256_v1.md#content-versus-ideal-norm) | Full original-field resultant, every original root/residue-degree contribution and distinction from scalar content. |
| dependency | [Dependency](Yin_C_G0256_v1.md#fixed-prime-actual-growth) | Odd-power preservation and stable binary tail, with first depths separately prescribed. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted statement/applicability only for the exact integer/simple-zero trace polynomial and compact Lipschitz test; no new original-proof audit. |
| support | [Support](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof) | Extraction ancestry of the finite pair-moment idea; the new third-moment derivation is complete locally. |
| support | [Support](../audits/reviews/Yin_R_G0335_v1.md#third-moment-reciprocal-whole-independent-finding) | Entire original12:29 D25 only; no prospective review of this new extraction. |
| review | [Review](../audits/reviews/Yin_R_G0336_v1.md#c98-third-moment-actual-extraction-finding) | Complete actual A--E, preserved original, finite moment and bounded deletion, both actual lifts, every root/depth, selected window, complete cost and fixed-density/source boundaries. |

## Registration and complete preservation

The ENTIRE original follows, with only its duplicate short author/framework frontmatter removed and its first title demoted one level.
All nine explicit anchors, equations1--20, starting question/search, both actual constructions, contributor/source boundaries, cost and author freeze remain.
Relative links remain valid.
The original working draft remains until actual extraction review, adoption, full preservation comparison and incoming-locator repair; root coordinates retirement.
No original failed candidate or mathematical paragraph is abridged.
R335 reviewed the original before its reviewer authored this actual wrapper, so a separate reviewer is required for this extraction.

## Organization after adoption

Following whole R335 and distinct actual extraction R336, root compared the complete original body under the declared frontmatter/title/newline normalization, repaired all exact incoming draft locators to the retained anchors and retired the redundant working draft.
All original source, failed-candidate and contribution history remains below.

## Argument

## Failure of linear triple-density capture bounds at selected windows in actual reciprocal units

Date: 2026-10-13T04:17.
Human author Yin.
Delegated author direct_triple works within the root's continuing G0001 authorization.
Root supplied the question only and retains sole Task, execution, strategy and shared-navigation responsibility.

<a id="direct-triple-question"></a>
## Question and exact scope

For a finite integer capacity array 1 <= w_a <= phi(a), set W=sum w_a, h(n)=sum_{a|n}w_a, H_X=max_{1<=n<=X}h(n), and T_X=sum_{lcm(a,b,c)<=X}w_a*w_b*w_c, with ordered triples and repeated labels.
Determine whether T_X>=delta W^3 and X<=C W force H_X>=c(delta,C) W WITHOUT assuming the universal short-pair bound in [C91](Yin_C_G0091_v1.md#statement).
The stronger candidate T_X<=K X H_X W would suffice, but is not presumed.
An abstract capacity theorem would apply to actual C91 root inventories; an abstract counterexample would still require realization before refuting an actual polynomial statement.

The actual-polynomial context retains original degree d, selected complete root groups W>=gamma*d, good prime p, full original norm and all local depths.
A positive same-time capture gives only the accepted good-prime lower floor A_p(n)>=h(n)log p.
The global near-one coverage hypothesis is a separate missing obligation.

<a id="direct-triple-reuse-search"></a>
## Reuse and search

Read the exact [C91 statement and retained proof](Yin_C_G0091_v1.md#statement), [C88 circular-score theorem and unresolved global-average boundary](Yin_C_G0088_v1.md#circular-link-obstructions-and-unresolved-average), [C86 residual bucket](Yin_C_G0086_v1.md#triple-anchored-residual-cover), and [C94 strict lower and oriented-row failures](Yin_C_G0094_v1.md#statement).
Local search by global triple density, short-pair, lcm triples and fractional Helly in the literature/audits and responsible Claims yielded these prior interfaces, not a direct uniform theorem.
A bounded external search on 2026-10-13 for divisor/lcm triple sums, totient-weighted density and fractional Helly least-common-multiple results located an Erdos extremal-paper lead and the already recorded Tao dense-lcm lead, but supplied no exact usable direct theorem.
No source theorem or priority claim is being imported.

C91 proves only sublinear capture unconditionally and linear capture conditional on universal K.
C94 rules out the K=1 guess and universal bounds on oriented individual rows; it does not settle the averaged K or direct triple question.
C88's arithmetic circular score is not freely exchangeable with global iid density.
An arbitrary abstract hypergraph is not an arithmetic counterexample.

## Continuing status

Author exploration; no result or independent review asserted yet.
No new mathematical native program has been run.

<a id="direct-triple-moment-contribution"></a>
## New discriminator and contribution boundary

2026-10-13T04:26.
The stronger proposed bound T_X<=K X H_X W is FALSE even for actual irreducible nontorsion integer units at the fixed good prime2, including reciprocal inputs after a bounded deletion and the explicitly adapted C83 lift below.
The main fixed-positive-density implication is NOT refuted: the constructed normalized triple densities are not shown bounded below.
This distinction is part of the result.

The averaged_lcm author derived the squarefree-divisor tail-moment construction for pairs in its entire original now retained in [C96](Yin_C_G0096_v1.md#averaged-short-lcm-finite-moment-proof); root relayed that author's idea, without originating it.
The present author adapts that exact mechanism to third moments and the direct triple estimate, and supplies the actual odd-degree realization and reciprocal/depth adaptation.
C96 does not prospectively prove this extension.
The shared mechanism is credited, not independently rediscovered.
Root supplied only the question, relayed idea and scope reminders.
C83/L217 supply the classical trace, Chinese-remainder and Eisenstein construction; they are not new methods here.
Any reviewer who contributed one of these actual new derivations must not independently review it.

<a id="direct-triple-finite-moment-obstruction"></a>
## 1. An exact third-moment obstruction

For a positive squarefree integer Q and real t>=1 put

    D_Q(t)={a:a divides Q and a<=t},
    W_Q(t)=sum_(a in D_Q(t)) phi(a),
    T_Q(t)=sum_(a,b,c divide Q, lcm(a,b,c)<=t)
                          phi(a)phi(b)phi(c),
    kappa_Q=max_(N divides Q) T_Q(N)/(N^2 W_Q(N)).       (1)

The triples are ordered and include all repeated labels.
The condition on their lcm already places each label in D_Q(t).
This is a nonempty divisor downset with exact full positive integer capacities.
The definition of kappa_Q is a finite maximum, not a claim to have enumerated it.

**Finite theorem.**
For every squarefree Q>=1,

    kappa_Q >= (1/3) product_(p divides Q)
                       (2-p^(-3))/(2-p^(-1)).          (2)

To prove it, W_Q(t) and T_Q(t) change only when t reaches a divisor of Q.
Between consecutive divisors their ratio T_Q(t)/(t^2 W_Q(t)) decreases.
For t>=Q it equals Q^2/t^2, because W_Q=Q and T_Q=Q^3.
Therefore the maximum over all real t>=1 is exactly (1), and

    T_Q(t)<=kappa_Q t^2 W_Q(t) for every t>=1.

Integrate against t^(-4)dt on[1,infinity).
All sums are finite and the integrals converge, including the tail beyond Q.
The integral of t^(-4) from an integer L>=1 to infinity is1/(3L^3), while the right-hand divisor term integrates t^(-2) from a to infinity to1/a.
Thus

    (1/3) sum_(a,b,c divide Q)
                phi(a)phi(b)phi(c)/lcm(a,b,c)^3
       <=kappa_Q sum_(a divides Q)phi(a)/a.            (3)

Squarefree multiplicativity makes the denominator product_p(2-p^(-1)).
At one prime p the all-absent triple has local weight1; the other seven presence patterns have combined numerator weight

    [1+(p-1)]^3-1=p^3-1.

Their common denominator is p^3, so the local triple factor is2-p^(-3).
This includes all three single-present patterns, all three double-present patterns and the all-present pattern, with no distinct-label restriction.
Substitution in(3) proves(2).
Q=1 gives kappa_1=1 and the lower bound1/3.

For every prime p>=2,

    (2-p^(-3))/(2-p^(-1))
       =1+(p^2-1)/[p^2(2p-1)] >=1+1/(3p),
    log[(2-p^(-3))/(2-p^(-1))]>=1/(6p).                (4)

The first inequality is equivalent to p^2+p-3>=0; the second follows from log(1+u)>=u/2 for0<=u<=1, applied to1/(3p).
The divergence of the sum of prime reciprocals, with its elementary Euler-product proof and checked attribution, is reused from the argument retained at [C220](Yin_C_G0220_v1.md#discriminant-divergence), with the original L17 passage explicitly read in C94.
Deleting any finite set of primes preserves divergence.
No prime-number theorem or rate is used.

In particular let Q_j be the product of the first j odd primes.
Let N_j be the LEAST divisor of Q_j attaining(1), and abbreviate W_j=W_(Q_j)(N_j), T_j=T_(Q_j)(N_j), kappa_j=kappa_(Q_j).
This is a fully specified finite sequence, though not an efficient optimizer.
Then kappa_j tends to infinity.
For the corresponding array and every1<=n<=N_j,

    h_j(n)=sum_(a divides gcd(n,Q_j))phi(a)=gcd(n,Q_j).

All those divisors are automatically at most n<=N_j.
Since N_j divides Q_j, the exact peak is

    H_(N_j)=N_j,
    T_j/(N_j H_(N_j) W_j)=kappa_j -> infinity.         (5)

Also W_j>=N_j by retaining all divisors of N_j.
As T_j<=W_j^3,

    N_j/W_j<=kappa_j^(-1/2) ->0.                      (6)

Thus the failure occurs with the time window N_j<=W_j and peak o(W_j).
The elementary capacity bound W_j<=sum_(a<=N_j)a=N_j(N_j+1)/2 implies N_j tends to infinity (otherwise kappa_j<=(W_j/N_j)^2 would be bounded), and then W_j tends to infinity.
These facts do NOT force T_j/W_j^3 away from zero.

<a id="direct-triple-odd-unit-realization"></a>
## 2. Direct realization by actual odd-degree units

This first realization is retained as the actual initial route before the reciprocal refinement.
For a selected odd Q=Q_j and N=N_j with W=W_Q(N)>1, let

    F(t)=product_(a in D_Q(N)) Phi_a(t), deg F=W.

Every selected a is odd, so Phi_a mod2 has distinct roots of exact multiplicative order a; these root sets are disjoint for distinct a.
Their product is squarefree because it divides t^Q-1 in characteristic2, whose derivative t^(Q-1) does not vanish at its roots.
The constant of F is-1, contributed by Phi_1=t-1.
Every other phi(a) is even by pairing primitive residues u and -u, so W is odd.

Define the monic polynomial P of degree W with constant-1 by the coefficientwise congruences

    P(t) congruent F(t) modulo2,
    P(t) congruent (t-1)^W+3t modulo9.                 (7)

The leading and constant coefficients match in both congruences, and W>1 keeps3t below the leading term.
For each remaining coefficient take the unique residue in{0,...,17} satisfying both congruences; existence follows directly because adding9 switches parity.
Thus(7) is an explicit integer construction, not an unspecified realization principle.
Translation gives

    P(t+1) congruent t^W+3t+3 modulo9.

All nonleading coefficients are divisible by3 and the constant is3 modulo9, so the same elementary Eisenstein mechanism used in [C83](Yin_C_G0083_v1.md#statement) proves irreducibility.
Explicitly, a monic factorization over Q would have monic integer factors by the usual Gauss denominator-clearing lemma; reduction modulo3 would make both nonconstant factors powers of t, forcing both constants divisible by3 and their product divisible by9, a contradiction.
Translation preserves rational irreducibility.

P is an actual algebraic-unit polynomial.
It is nontorsion: a nonreal root of unity and its inverse are distinct conjugates, so its rational minimal degree is even; a real root of unity is1 or-1 and has degree1.
The odd irreducible degree W>1 excludes both cases.
Its mod2 squarefreeness proves2 does not divide disc(P).
At that actual good prime its complete original root inventory is exactly w_a=phi(a), a in D_Q(N), with d=W.
No root or residue-factor degree has been discarded.
Therefore(5)--(6) are actual original-root capture facts for this family with X=N<=d.
The construction prescribes no higher2-adic depths, so its small ROOT peak is not promoted to an upper bound for full A_2.

<a id="direct-triple-reciprocal-deletion"></a>
## 3. A bounded deletion preserves the obstruction inside the reciprocal core

Continue with odd Q,N,W,T,kappa as above and remove orders1 and3:

    O={a:a divides Q, 5<=a<=N},
    b=1+2*1_(3 divides Q and 3<=N)<=3,
    d=sum_(a in O)phi(a)=W-b,
    V=sum_(a,b,c in O, lcm(a,b,c)<=N)phi(a)phi(b)phi(c).

In this display the order labels a,b,c inside the sum are dummy indices, distinct from the scalar removed mass b.
The union bound on which of the three coordinates was removed gives

    V>=T-3b W^2>=T-9W^2.                              (8)

Because W<=N(N+1)/2<=N^2, whenever kappa>9 the right side is positive, and since0<d<=W,

    V/(N^2 d) >= (T-9W^2)/(N^2 W)
                >=kappa-9 -> infinity.               (9)

In particular O is nonempty for all sufficiently large j.
Each surviving order has even phi(a), so d=2s is even and tends to infinity.
Moreover

    N/d <= kappa^(-1/2)/(1-3/W) ->0.                  (10)

Hence N<=d eventually.
For the remaining inventory and n<=N,

    h_O(n)=gcd(n,Q)-1-2*1_(3 divides gcd(n,Q)),
    N-3<=H_N(O)<=N.                                  (11)

The exact formula follows because every divisor of gcd(n,Q) already lies below N.
The lower bound evaluates n=N; the upper bound uses gcd(n,Q)<=n.
Thus(9) also forces V/(N H_N(O) d) to infinity.
This proves preservation of the negative estimate with the true remaining degree d, before any polynomial lift.

<a id="direct-triple-reciprocal-realization-and-depths"></a>
## 4. Actual reciprocal construction and every binary depth

The following is the [C83 construction](Yin_C_G0083_v1.md#pairwise-actual-reciprocal-lift) ADAPTED to this finite set O, not an invocation of its interval-specific theorem outside its hypotheses.
The exact retained original proof in C83 Sections3--4 and the [L64 simple-root/unramified interface](../ledger/Yin_L_G0064_v1.md#direct-etale-frobenius-lift) were read.
No density, interval or order/degree-growth fact from C83 is used.

For each odd a>=5 there is a monic integer trace polynomial S_a of degree phi(a)/2 with Phi_a(t)=t^(phi(a)/2) S_a(t+t^(-1)).
Indeed t^(-phi(a)/2)Phi_a(t) is a symmetric integer Laurent polynomial, and the recurrence V_(k+1)(x)=xV_k(x)-V_(k-1)(x), V_0=2,V_1=x, expresses t^k+t^(-k) as a monic integer polynomial in x.
Its triangular leading terms give S_a without division by2.
Put

    T_0(x)=product_(a in O) S_a(x), deg T_0=s=d/2.

The reduction of T_0 mod2 is squarefree.
All primitive roots of the odd selected orders are distinct; if their traces agree, the two roots solve the same quadratic t^2-theta*t+1 and are equal or inverse.
Only inverse pairs are identified, and none is self-inverse.
Thus the trace roots are distinct, of exactly the required count s.
Every such trace theta avoids0 and1: trace0 would force root order1, and trace1 would force order3.
Neither is selected.

Let B(x) be the coefficient0/1 lift of the unique remainder of x^2 T_0'(x) modulo T_0 in F_2[x], with degree<s.
Define a monic integer T of degree s by

    T congruent T_0+2B modulo4,
    T congruent (x-2)^s+3 modulo9,                    (12)

taking each lower coefficient in[-18,17] in its unique class modulo36.
Existence can be checked directly by adding multiples of9 to reach any required class modulo4.
Define

    P*(t)=t^s T(t+t^(-1)).                            (13)

This is monic, integral and reciprocal of ORIGINAL degree d=2s, with constant1.
Modulo9 its translate satisfies

    P*(t+1) congruent t^(2s)+3(t+1)^s,

because t^s(t+t^(-1)-2)^s=(t-1)^(2s).
The nonleading coefficients are divisible by3 and the constant is3 mod9, so the preceding Eisenstein argument proves irreducibility.
T is irreducible as well: a rational factorization of its monic integer form would induce one of P*.
Both have simple characteristic-zero roots.
Modulo2, P* is exactly product_(a in O)Phi_a, so it is squarefree and2 is good.
Its complete original root inventory is precisely phi(a) at each a in O.

Here is the complete local check ensuring that the adaptation controls ALL binary depths.
In the unramified2-adic ring at any selected residue root, lift that root to the exact odd-order-a root of unity zeta, and put theta=zeta+zeta^(-1).
Simple-root lifting is valid by the directly read L64 interface; its derivative is a unit for both t^a-1 and the simple trace root.
Then T_0(theta)=0.
There is a unique root z of T near theta and a unique root alpha of t^2-z*t+1 near zeta.
In this ring T_0'(theta), theta and theta-1 are units.
Modulo4,

    (z-theta)/2 congruent -B(theta)/T_0'(theta) mod2,
    z-theta=(alpha-zeta)(1-1/(alpha*zeta)).

All denominators in the next calculation are units.
A first-order expansion of alpha^a gives

    overline[(alpha^a-1)/2]
      = -overline(a)*overline(zeta)^(-1)*overline(B(theta))
          /[overline(T_0'(theta))*(1-overline(zeta)^(-2))]
      =overline(B(theta))/[overline(T_0'(theta))*overline(theta)]
      =overline(theta).                               (14)

The middle equality uses characteristic2 and odd a.
The last equality is the actual remainder prescription B=theta^2 T_0'(theta) in the residue field.
Quadratic and higher terms in alpha-zeta vanish modulo4 because alpha-zeta is divisible by2.
Since the residue theta is neither0 nor1, both(alpha^a-1)/2 and(alpha^a+1)/2 are units; their residues differ by1.
Thus both initial valuations equal1.

Odd powering preserves a positive2-adic valuation by its geometric-sum factor.
The first squaring has valuation2, and once v_2(y-1)>=2, the two terms2(y-1) and(y-1)^2 have different valuations, so each subsequent squaring adds exactly1.
Consequently at EVERY original root of order a and EVERY n>=1,

    v_2(alpha^n-1)=1+v_2(n) if a divides n,
                   0 otherwise.                       (15)

Every value is finite, which proves nontorsion, rather than assuming it from Eisenstein.
This check covers all primitive roots, all inverse and Frobenius orbits, including inversion-stable orbits; no two-factor hypothesis enters.

For any root alpha generating its actual degree-d field K, retain the complete original signed norm and full local income

    D_n=Norm_(K/Q)(alpha^n-1)=Res(P*,t^n-1),
    C_n=abs(D_n)>0,
    A_2(n)=(log2)v_2(C_n)
          =(log2)(1+v_2(n))*sum_(a in O,a divides n)phi(a).
                                                               (16)

Each residue factor contributes its full degree once, and every actual depth is counted.
Norms do not switch to the minimal field of alpha^n.

For1<=n<=N write n=2^r v, v odd.
The odd orders divide v; hence their captured mass is at most sum_(a|v)phi(a)=v.
Since(r+1)/2^r<=1 for every integer r>=0,

    A_2(n)<=(log2)(r+1)v <=N log2,
    max_(1<=n<=N) A_2(n)/d <=(N/d)log2 ->0.           (17)

At n=N, which is odd, formula(11) gives A_2(N)=(N-1-2*1_(3|N))log2.
Thus the local upper bound retains even exponent depths rather than discarding them.
The assertion(17) concerns ONLY the chosen window X=N=o(d).
No assertion for EVERY fixed larger window n<=C*d is made.

<a id="direct-triple-full-cost-and-scope"></a>
## 5. Full Mahler cost and the unresolved fixed-density implication

The reciprocal family is far from a vanishing-positive-measure family.
This follows by the SAME accepted C83/L217 bounded-coefficient trace argument, whose hypotheses are explicitly verified here.
The s lower coefficients of T in(12) have absolute value at most18, so

    ||P*||_1<=2^s+18*sum_(k=0)^(s-1)2^k=19*2^s-18,
    M(T)<=||T||_2<=sqrt(1+324s)<=s for s>=400.          (18)

The first Mahler inequality is the usual circle integral and Jensen/Parseval inequality already used in C83's complete cost proof; no coefficient, trace pair or root of P* is omitted.
The actual integer trace polynomial T has simple roots and degree s.
Read and use exactly the accepted [Pri11-U001 Theorem3.1 statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001), with its recorded statement/applicability inspection and incomplete underlying source-proof-audit scope.

For completeness its specialized test is f(z)=min(1,(2-|z|)_+)*min(1,(|Im z|-1/2)_+).
Each factor is globally1-Lipschitz, between0 and1, so f is globally2-Lipschitz and supported in radius2.
On the unit-circle arcs with angles[pi/3,2pi/3] and[4pi/3,5pi/3], f>=1/4, giving circle mean>=1/12.
With s>=400 and10sqrt(log(s)/s)<=1/24, the accepted discrepancy estimate and(18) give the mean of f over all s trace roots at least1/24.
Therefore at least s/24 trace roots have absolute imaginary part>1/2.
For each full inverse pair over such a trace, if R>=1 is the larger root modulus then |Im(trace)|<=R-R^(-1), hence R>(1+sqrt17)/4.
Keeping every pair yields

    (d/48)log[(1+sqrt17)/4] <= m(P*)
       <=(d/2)log2+log19                              (19)

for all sufficiently large j.
Here m is TOTAL logarithmic Mahler measure, not height per degree.
The thresholds apply eventually because d tends to infinity.
This reproduces the needed cost specialization, credits the old mechanism and adds no uninspected external analytic theorem.

Combining(9), (11), (13)--(17), there is thus a rigorously specified sequence of actual irreducible reciprocal nontorsion integer-unit polynomials with fixed good prime2, original degrees d tending to infinity, chosen windows X=N<=d, complete root capacities, and

    T_X/(X H_X d) ->infinity,
    H_X/d ->0,
    max_(n<=X) A_2(n)/d ->0.                          (20)

The last two claims are at these chosen windows ONLY.
The full measures obey(19), so do not tend to zero.
Other-prime income remains in C_n; neither(17) nor(20) bounds the all-prime norm.
A small local root peak alone would not give(17); the explicit depth prescription is essential.

Write delta_j=T_X/d^3 for the ACTUAL ordered iid triple density.
Then the divergence in(20) says only

    delta_j*d^2/(X H_X) ->infinity.

It does NOT prove inf_j delta_j>0.
In the untrimmed model kappa_j=delta_j*(d/X)^2 exactly; kappa_j tending to infinity while d/X tends to infinity places no positive constant lower bound on delta_j.
The same logical issue persists after trimming.
Thus no absolute c>0 can prove H_X>=c*delta*d^2/X uniformly for every positive density parameter delta, even on actual reciprocal good-2 inputs with X<=d.
This refutes a LINEAR-in-delta candidate estimate.
It does not refute a bound with a different dependence on fixed delta, such as c(delta,C)d, the earlier conditionally proposed quadratic dependence, a near-one coverage statement or the unrestricted Mahler-gap contract.

Before this finding the direct estimate was only a candidate.
It is now a failed stronger route with an actual polynomial obstruction; the original positive-fixed-density question remains unresolved.
Future continuation must exploit a nonlinear dependence on density or an additional actual small-measure restriction, and cannot re-use the refuted T_X<=K X H_X W estimate.
No further open-ended exploration is included in this author handoff.

<a id="direct-triple-author-check-and-freeze"></a>
## Author check and entire freeze

The author checked finite maximum endpoints including Q1, the integral tail t>=Q, all eight local triple membership patterns, ordered/repeated labels, the prime-exclusion and divergence use, exact H_N=N, N and W escape, the missing constant-density premise, coefficientwise CRT, odd degree and W>1 in the first lift, good2 squarefreeness and all root masses, the loss bound3bW^2, positivity needed before replacing d by W in(9), every trace/inverse root, exclusions1/3, both initial binary depths, all later depths, complete signed norms, the smaller-window limitation, every original-degree and Mahler-cost input, and the precise failure of the linear-in-density estimate.
These are AUTHOR checks, not independent review.
No native mathematical program, numerical optimizer, formal verification or source acquisition was performed.

The shared moment method is from averaged_lcm; the present author supplied the triple extension and both actual constructions/adaptation.
The existing C83/L217 lift and cost argument, L64 local algebra, L17 divergence and Pri11 accepted statement receive their original credit and retain their inspection limits.
Earlier starting questions and unsuccessful candidates above remain historical, not current theorem assertions.
This entire artifact is ready for a separate noncontributing whole review; no independent verdict or Claim acceptance is asserted by this draft.

2026-10-13T04:29.
ENTIRE author-complete freeze: starting question/search/history, shared-method contribution account, Sections1--5/equations(1)--(20), both actual realizations, selected-window all-depth bound, original full-measure cost, actual inputs and explicit unresolved fixed-positive-density/G0001 boundaries.
No further mathematical edits are planned during whole review.
