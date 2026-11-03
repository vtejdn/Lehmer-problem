---
author: Yin
---
# Exact pair-supported correlated rounding and its full-surplus boundary

Date: 2026-10-12T11:09.
Human author Yin.
Internal fixed extraction under the continuing G0001 instruction.
g0001_routes authored the complete D12 correlated-law proof and now authors this registered statement/wrapper.
Root supplied only the broad question, not this mechanism or its formulas.
The ENTIRE original author account is retained below.
Separate noncontributor R267 covers the original18:42 whole proof only; this newly written statement, preservation and actual interfaces require their own noncontributor extraction review.
No adoption is performed here.

## Statement

Let P(t)=sum_(i=0)^d p_i t^i be an ACTUAL monic irreducible nontorsion algebraic integer-unit minimal polynomial, original degree d>=2, with p_i in{0,+1,-1}, p_d=1 and p_0 in{+1,-1}.
Reciprocity is NOT required.
Use K=Q(alpha), actual O0=Z[alpha], I={i:p_i!=0}, n=|I|>=3, sigma_i=p_i on I, and

    a_h=sum_(i<j in I,j-i=h)sigma_i sigma_j, 1<=h<=d,
    L=sum_(h=1)^d |a_h|>=1,
    m(P)=sum_(P(beta)=0)log max(1,|beta|).

The COMPLETE RESTRICTED family in this theorem consists of finite rational laws on subsets B of I with |B|<=2, every marginal Pr(i in B)=1/q for some INTEGER q>=2, and original coefficient polynomials

    f_B=P/q-sum_(i in B)sigma_i t^i.

The only zero-valued atom is B empty.
Replace that atom by P/q+1 and P/q-1 at half its OWN actual probability each, omitting zero weights.
Every final value is then a NONZERO actual O0 integer.
No zero atom is deleted or conditionally renormalized.
The class is NOT all correlated laws, all modular codewords or full C16 capacity.

**A. Complete finite parameterization and all-lag criterion.**
For nonnegative rational edges g_ij, i<j in I, put

    d_i=sum_(j!=i)g_{min(i,j),max(i,j)},
    G=sum_(i<j)g_ij,
    w_{i,j}=g_ij/q^2,
    w_i=(q-d_i)/q^2,
    w_empty=(q^2-nq+G)/q^2.

Every restricted subset law is uniquely of this form before optional splitting of identical labels.
It is a genuine law exactly when d_i<=q for all i and q^2-nq+G>=0; zero types are omitted and all remaining probabilities are positive rational.
The repaired coefficient mean is zero.
If X is its COMPLETE second-moment matrix, then for distinct support positions

    X_ij=sigma_i sigma_j(g_ij-1)/q^2.

The active diagonal entries before repair are(q-1)/q^2, and repair adds w_empty to X_00 only.
All positive/negative lag sums vanish EXACTLY when

    sum_(i<j in I,j-i=h)sigma_i sigma_j g_ij=a_h
        for EVERY h=1,...,d.

When these conditions hold the exact constant circle covariance is

    E=1-(n-G)/q^2>0.

No finite-moment existence is inferred from PSD alone.

**B. Exact success criterion and entire restricted infimum.**
Allowing ALL integer q>=2 and ALL rational feasible edges above, a packet with E<1 exists if and only if L<n.
Every successful member has q>=n-1.
Its restricted energy infimum is

    E_pair(P)=1-max{1/(n-1)^2,(n-L)/n^2}, if L<n,
    E_pair(P)=1, if L>=n.

For L<n the infimum is ATTAINED by an explicit finite packet.
At L=n the value1 is attained.
At L>n every finite member has E>1 and the infimum1 is NOT attained.
No infinite packet or full-capacity equality is asserted.

For the explicit q=n attainer, choose at each gap with a_h!=0 one actual pair with coefficient-product sign sign(a_h), and give it edge mass |a_h|; choose the lexicographically first such pair for a canonical version.
All other edges are zero.
Then G=L, all loads<=L<n, w_empty=L/n^2 and E=1-(n-L)/n^2.
For the q=n-1 attainer start with those same edges.
If L=n-1 use them unchanged.
If L<n-1, some actual gap has both sign types; add (n-1-L)/2 to one edge of each sign at that gap.
Then G=n-1, all loads<=q, empty mass0 and E=1-1/(n-1)^2.
Both constructions are finite rational and include all actual positive leaves.
For L>n the first integer edge assignment with q>=max{n,L} supplies the finite E>1 sequence tending to1.

**C. Genuine signed cross covariance and the actual flat-form constraint.**
Every feasible law has

    sum_(i!=j in I)sigma_i sigma_j X_ij
       =[2G-n(n-1)]/q^2.

This is STRICTLY negative whenever E<1, proving actual nonzero off-diagonal covariance despite all lag sums being zero.
For the C29 original coefficient form

    H_flat=I_(d+1)+[diag(p_i^2)-pp^T]/(n-1),

one has the exact identity

    Tr(H_flat X)=1+G(n-3)/[(n-1)q^2]>=1.

Thus the complete arithmetic-form bound is respected.
Its old diagonal obstruction is not promoted to a full-domain obstruction.

**D. ACTUAL coefficient denominator, FINAL weights, contents, width and full signs.**
EVERY final atom has ACTUAL least coefficient denominator q, primitive integer numerator and physical width d; so does the complete union.
The numerators are

    F_B=P-q sum_(i in B)sigma_i t^i, B nonempty,
    F_+=P+q, F_-=P-q when the empty mass is positive.

For the retained positive indexed final weights define their ACTUAL least denominator M=lcm_b denominator(omega_b), and integer copies k_b=M omega_b>0, sum k_b=M.
If r clears all rational g_ij then M divides2r q^2, an upper divisor only.
For the canonical q=n integer-edge construction the ACTUAL M equals n^2 when L is even and2n^2 when L is odd.
For the explicit q=n-1 construction, writing r_extra=n-1-L, its ACTUAL M is q^2 when r_extra is even and2q^2 when odd.
Positive splitting may increase M; the formulas thereafter use that actual new indexed M, not the unsplit denominator.

Put nu=Norm_K(alpha)=(-1)^d p_0 in{+1,-1}.
Singleton values have full signed norms(-sigma_i)^d nu^i.
Pair values and full signed degree-d norms are

    u_ij=-sigma_i alpha^i(1+sigma_i sigma_j alpha^(j-i)),
    D_ij=(-sigma_i)^d nu^i Norm_K(1+sigma_i sigma_j alpha^(j-i))
         in Z minus{0}.

Repair values+/-1 have signed norms1 and(-1)^d.
Let D_b retain all these signed norms.
Then the complete original arithmetic is

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(k_b)=q^(dM)product_b D_b^(k_b),
    Lambda=(1/(d q^2))sum_(i<j)g_ij log|D_ij|>=0,
    S_int=q^2 E,
    I_income=log q+Lambda,
    I_income-(1/2)log S_int=Lambda-(1/2)log E<=m(P).

Every original root, signed factor and positive copy is retained.
Contents are PROVED1 for these numerators, not silently discarded.
The final inequality uses C10 only after full complementarity, with SAME final weights and actual T/d=1.
There is no extra uncancelled log q charge or identification of q with FINAL M.

**E. Full-surplus ceiling for EVERY successful member.**
For every actual pair, the original-root product bound gives

    0<=log|D_ij|<=d log2+(j-i)m(P)<=d[log2+m(P)].

Consequently every successful choice in this ENTIRE restricted family satisfies

    0<=Lambda<=G[log2+m(P)]/q^2
               <n[log2+m(P)]/(n-1)^2,
    0<1-E<=1/(n-1),
    0<Lambda-(1/2)log E
       <=n[log2+m(P)]/(n-1)^2+1/[2(n-2)].

Thus on any inputs with n->infinity and bounded m(P), the FULL surplus of every successful member tends to zero, including all norm income and arbitrary permitted q/edges.
At fixed n and bounded input measure, successful q->infinity gives full surplus O(q^-2).
These are limitations of this two-bit uniform-marginal mechanism, not of larger supports or other representatives.
Conversely for bounded n with L<n, the attained construction gives the explicit subclass lower bound m(P)>=-(1/2)log E_pair(P)>0.
No theorem here supplies those conditions on unrestricted inputs.

**F. Exact original inputs and failure boundary.**
For the ACTUAL original quartic P=t^4-t^3-t^2-t+1, its signs are(1,-1,-1,-1,1), n5, autocorrelations(0,-1,-2,1) and L4.
Take q4 and g_02=1,g_03=2,g_04=1, all other edges zero.
Loads are(4,0,1,2,1), empty mass0.
The COMPLETE seven-label packet is:

| B | Numerator F_B | Actual value F_B(beta)/4 | Signed full norm | Weight |
| --- | --- | --- | --- | --- |
| {1} | P+4t | beta | 1 | 4/16 |
| {2} | P+4t^2 | beta^2 | 1 | 3/16 |
| {3} | P+4t^3 | beta^3 | 1 | 2/16 |
| {4} | P-4t^4 | -beta^4 | 1 | 3/16 |
| {0,2} | P-4+4t^2 | beta^2-1 | -3 | 1/16 |
| {0,3} | P-4+4t^3 | beta^3-1 | -1 | 2/16 |
| {0,4} | P-4-4t^4 | -1-beta^4 | 1 | 1/16 |

All contents are1, actual q4,M16,T4 and

    sum_b(16 omega_b)F_B(t)F_B(t^-1)=240,
    E=15/16, S_int15, M E15,
    product_b Res(P,F_B)^(16 omega_b)=-3*4^64,
    Lambda=log3/64,
    m(P)>=log3/64+(1/2)log(16/15)>0.

This15/16 is the EXACT optimum of the declared restricted family, since max{1/16,1/25}=1/16.
It is not a full C16 optimum, a new input, a near-one family or a strongest-known measure bound.

For the original degree10 Lehmer polynomial t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, n9 and its complete autocorrelations(6,1,-2,-3,-4,-4,-2,1,2,1) give L26.
Therefore EVERY finite member of this restricted recipe has E>1 for EVERY integer q and feasible rational edge assignment.
Its restricted infimum1 is not attained.
This excludes no different C31 successful packet, C17 unrestricted realization, larger-subset law or changed marginal/representative mechanism.

All finite construction, exact boundary and full-cost claims are locally proved below, with no native mathematical program or external dependent-rounding theorem.
The unrestricted G0001 objective remains unresolved.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:09 |
| status | open |
| reason | Register the complete pair-supported finite-law classification, exact restricted optimum/attainment cases, genuine off-diagonal covariance, full original costs/surplus ceiling and both exact controls. The entire original proof/history is retained. R267 covers only the original18:42 D12 whole proof; this newly authored statement and fixed interfaces await actual noncontributor extraction review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, general flat actual-unit domain, complete DECLARED pair-supported uniform-marginal family, all-q optimization and every arithmetic/asymptotic/control boundary. |
| argument | [Entire retained proof](#argument) | ENTIRE original D12 question/reuse/proposed-model history, Sections1--8/Theorems1--2/equations1--11, all probability/cost/control cases and18:42 freeze. |
| dependency | [Complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same final weights, all original nonzero signed resultants and exact physical T=d, used after full complementarity. |
| dependency | [Actual flat arithmetic form](Yin_C_G0029_v1.md#statement) | Exact H_flat/domain convention and diagonal-versus-full distinction; current correlated form value is calculated locally. |
| dependency | [Original Lehmer autocorrelations](Yin_C_G0031_v1.md#lehmer-residue-dual-reuse-and-hand-kernel) | Actual original degree10 polynomial, support9 and complete ten autocorrelations only; no solver optimum or new norm premise. |
| dependency | [Actual original quartic](Yin_C_G0051_v1.md#statement) | Actual original irreducible Salem P, original degree4, beta and monogenic order only; no parity-growth input. |
| support | [Finite moment domain](Yin_C_G0016_v1.md#statement) | Actual nonzero integral values and all-lag finite positive rational packet conventions; realization is explicitly supplied here. |
| support | [Full first-window existence](Yin_C_G0017_v1.md#statement) | Unrestricted qualitative comparison only, not equality of the present restricted optimum with full capacity. |
| support | [Earlier independent rounding](Yin_C_G0054_v1.md#statement) | Old diagonal finite/recursive repair and full costs, as bounded reuse; not a correlated-law premise. |
| support | [Necessary denominator price](Yin_C_G0050_v1.md#statement) | Actual q versus FINAL M and hypothetical near-one linear-window necessity only; no sufficiency or near-one existence. |
| support | [Earlier signed-period inventory](Yin_C_G0015_v2.md#statement) | Different divided-binomial/trinomial mechanism credited at its actual scope, not imported into the present residue law. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0267_v1.md#pair-correlated-whole-independent-finding) | Entire original18:42 D12 and direct interfaces only, with no prospective current statement/extraction or Task coverage. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-12T11:18 |
| status | proved |
| reason | Adopt the separately performed original whole R267 and actual fixed-extraction R270 findings at their precise scopes. The entire original proof and history remain. Exact optimum, all-q failure and full-surplus boundary belong only to the stated pair-supported common-marginal family; no full capacity, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--F, general flat actual-unit domain, complete DECLARED pair-supported uniform-marginal family, all-q optimization and every arithmetic/asymptotic/control boundary. |
| argument | [Entire retained proof](#argument) | ENTIRE original D12 question/reuse/proposed-model history, Sections1--8/Theorems1--2/equations1--11, all probability/cost/control cases and18:42 freeze. |
| dependency | [Complete original-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Same final weights, all original nonzero signed resultants and exact physical T=d, used after full complementarity. |
| dependency | [Actual flat arithmetic form](Yin_C_G0029_v1.md#statement) | Exact H_flat/domain convention and diagonal-versus-full distinction; current correlated form value is calculated locally. |
| dependency | [Original Lehmer autocorrelations](Yin_C_G0031_v1.md#lehmer-residue-dual-reuse-and-hand-kernel) | Actual original degree10 polynomial, support9 and complete ten autocorrelations only; no solver optimum or new norm premise. |
| dependency | [Actual original quartic](Yin_C_G0051_v1.md#statement) | Actual original irreducible Salem P, original degree4, beta and monogenic order only; no parity-growth input. |
| support | [Finite moment domain](Yin_C_G0016_v1.md#statement) | Actual nonzero integral values and all-lag finite positive rational packet conventions; realization is explicitly supplied here. |
| support | [Full first-window existence](Yin_C_G0017_v1.md#statement) | Unrestricted qualitative comparison only, not equality of the present restricted optimum with full capacity. |
| support | [Earlier independent rounding](Yin_C_G0054_v1.md#statement) | Old diagonal finite/recursive repair and full costs, as bounded reuse; not a correlated-law premise. |
| support | [Necessary denominator price](Yin_C_G0050_v1.md#statement) | Actual q versus FINAL M and hypothetical near-one linear-window necessity only; no sufficiency or near-one existence. |
| support | [Earlier signed-period inventory](Yin_C_G0015_v2.md#statement) | Different divided-binomial/trinomial mechanism credited at its actual scope, not imported into the present residue law. |
| support | [Original whole independent finding](../audits/reviews/Yin_R_G0267_v1.md#pair-correlated-whole-independent-finding) | Entire original18:42 D12 and direct interfaces only, with no prospective current statement/extraction or Task coverage. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0270_v1.md#c58-pair-correlated-actual-extraction-finding) | Entire actual A--F statement, complete preserved argument and direct interfaces, separately performed by a noncontributor to original proof and wrapper. |

## Registration and complete preservation

Date: 2026-10-12T11:09.
The original author now registers this precise statement and retains the ENTIRE D12 body with only its short front matter removed, first title demoted once, exact relative Claim links rebased and terminal whitespace normalized.
Every theorem, proof, proposed-model/reuse account, actual cost, positive/failed input, source/contribution boundary, author self-check and18:42 freeze remains.
Original pending-review language is preserved as history, not treated as the current Claim assessment.
The current registration does not extend R267's original whole-proof scope, conduct its own independent review or adopt a proved decision.
No new experiment, native mathematical program, source intake or original-draft retirement is performed.
Root retains those later organizational responsibilities.

## Argument

## Pair-supported correlated rounding and an exact autocorrelation budget

Date: 2026-10-12T10:33.
Human author Yin.
New AUTHOR inquiry by g0001_routes under root's continuing G0001 assignment.
Root supplied only the broad question of actual correlated packets beyond diagonal rounding, not any formula, distribution or proof here.
This new rolling address inherits no prior scope.

## Question and bounded first choice

Construct an ACTUAL finite correlated bit law whose prescribed one-coordinate marginals preserve original monogenic-order integrality, whose signed pair probabilities cancel EVERY polynomial lag and whose zero-residue repair retains all mass.
Focus first on original monic irreducible nontorsion unit P with flat coefficients0,+/-1 at its first window[0,d], where the already adopted C29 excludes diagonal covariance.
The proposed law is supported on the empty subset, singletons and pairs of the nonzero coefficient positions.
It is a newly explicit finite probability construction, not an invocation of a named dependent-rounding algorithm, a PSD realization assertion or a rerun of C31's fixed Lehmer LP.

The working discriminator is the COMPLETE autocorrelation absolute sum L=sum_(h>=1)|a_h(P)| relative to the number n of nonzero coefficients, with actual edge loads and rational probabilities.
Determine exact feasibility and energy within this two-bit support restriction, then all signed original norms/q/FINAL M/contents/physical width and any quantitative limitation.
The statements below are author development awaiting complete proof/self-check and independent review.
No native mathematical program, J, scan, solver or new external theorem is planned.


<a id="pair-correlated-reuse-and-model"></a>
## 1. Existing boundaries and proposed actual model

Read [C16](Yin_C_G0016_v1.md#statement), [C17](Yin_C_G0017_v1.md#statement), [C29](Yin_C_G0029_v1.md#statement), [C31](Yin_C_G0031_v1.md#statement), [C50](Yin_C_G0050_v1.md#statement) and [C54](Yin_C_G0054_v1.md#statement) at their relevant interfaces.
C54's independently sampled and recursively repaired law stays diagonal.
C29 rules that mechanism out for EVERY first-window flat input; C17 nevertheless gives qualitative full-domain existence.
C31 is one exact positive-measure original-Lehmer packet with selected new residue classes, not a general correlated generator.
C50 forces actual coefficient denominators to grow in a hypothetical small-measure linear-window sequence; its final-weight and full-surplus boundaries remain.
A focused reuse search for the pair-support/autocorrelation-budget mechanism will be recorded before adopting a new theorem claim.

Let P(t)=sum_(i=0)^d p_i t^i be ACTUAL monic irreducible nontorsion integer-unit, d>=2, p_i in{0,+1,-1}, p_0 in{+1,-1}.
No reciprocity is imposed.
Let I={i:p_i!=0}, n=|I|>=3, sigma_i=p_i on I, K=Q(alpha) and O0=Z[alpha].
The n>=3 fact follows because a monic unit binomial has only roots of unity.
For h=1,...,d put

    a_h=sum_(i<j in I,j-i=h)sigma_i sigma_j,
    L=sum_(h=1)^d |a_h|.

For integer q>=2 let p=1/q.
We seek a correlated random subset B of I with EVERY marginal Pr(i in B)=p and support ONLY empty, singleton and two-element sets.
Its coefficient polynomial is

    f_B=P/q-sum_(i in B)sigma_i t^i.

It has mean-zero coefficients and actual value -sum_(i in B)sigma_i alpha^i in O0.
Minimality at degree at most d says a zero bit polynomial must be0 or P, because its leading bit is0or1.
Since n>=3 and |B|<=2, the ONLY zero-valued atom is the empty subset.
Thus every nonempty atom is admissible before repair, independently of norm size.
The empty atom P/q is replaced by P/q+1 and P/q-1 with half its actual mass each, as in the old paired identity; it is never removed or conditionally renormalized.

<a id="pair-correlated-proposed-exact-gate"></a>
## 2. Proposed edge-weight parameterization and immediate identities

Write a nonnegative rational number g_ij for each unordered pair i<j in I and set

    w_{i,j}=g_ij/q^2,
    d_i=sum_(j!=i)g_{min(i,j),max(i,j)},
    G=sum_(i<j)g_ij,
    w_i=(q-d_i)/q^2,
    w_empty=(q^2-nq+G)/q^2.

Then the displayed weights sum1 and every bit marginal is1/q exactly.
They are nonnegative precisely when each d_i<=q and q^2-nq+G>=0, with zero labels omitted.
For i!=j, the coefficient second moment before and after empty repair is

    X_ij=sigma_i sigma_j (g_ij-1)/q^2.

The diagonal bit variance remains(1/q)(1-1/q), with additional w_empty at coefficient0 after repair.
Consequently all lags vanish exactly when

    sum_(i<j in I,j-i=h)sigma_i sigma_j g_ij=a_h
        for EVERY h=1,...,d.

The actual complete repaired energy is

    E=n(q-1)/q^2+w_empty=1-(n-G)/q^2.

These explicit finite identities are to be fully proved and their edge cases checked below.
They are not yet an assertion that every needed edge assignment exists or that a uniformly positive surplus follows.

A candidate minimal assignment has total G=L: for each nonzero a_h, choose an actual pair at gap h whose sign product equals sign(a_h) and put g_ij=|a_h| there, all other edge weights zero.
Such a sign occurs because a_h is the signed sum of the actual gap pairs.
With q=n and L<n, the weighted degrees are at most L<n, the singleton weights are positive and the empty probability is L/n^2.
This points to an exact restricted success test L<n and a finite explicit all-input formula within that condition.
Whether its full surplus remains quantitatively useful, and what it excludes, require the complete cost and limit analysis below.
No fixed-input numerical search is used.

<a id="pair-correlated-complete-realization"></a>
## 3. Complete finite realization and exact restricted capacity

The additional bounded search located [C15v2's one-copy trinomial rigidity](Yin_C_G0015_v2.md#statement), where divided binomial values force signed periods and total integer multiplicity matches a trinomial's autocorrelation.
That is a different inventory and original-order condition: here the numerator is P-q times a signed subset, its value is an UNDIVIDED signed monomial/binomial, and the complete law has correlated prescribed marginals.
C31's selected fixed-Lehmer residue/LP mechanism and C17's qualitative limiting dual argument were also read at their actual roles.
No already registered result of the present restricted-class edge budget was found.
This is a bounded reuse observation, not a novelty assertion.
The following proof specifies every probability directly and invokes no external dependent-rounding theorem; the prior RT87 attribution to independent rounding is not used as a correlated-realization premise.

**Theorem 1 (all feasible laws and strict success).**
Fix the original flat P above.
For an integer q>=2, EVERY subset law supported on empty/singletons/pairs with marginals1/q is uniquely represented by the g_ij and probabilities of Section2.
It gives a complete repaired complementary packet if and only if all the displayed nonnegative-weight conditions and every lag equation hold.
Its energy is E=1-(n-G)/q^2.
There exists a strict-below-one packet in this COMPLETE restricted family, allowing any integer q>=2, if and only if

    L<n.                                             (1)

*Proof.*
The pair masses determine g_ij=q^2 w_{i,j}.
Each prescribed marginal forces w_i=1/q-sum_j w_{i,j}, and normalization forces w_empty=1-n/q+sum_{i<j}w_{i,j}.
Thus the parameterization is both necessary and sufficient, with every zero mass omitted.
Its finite normalized probabilities have no unproved realization condition.
Centered coefficient moments give the formula X_ij in Section2; all off-diagonal entries involving zero coefficients of P are zero.
At lag h the sum is [sum_(j-i=h)sigma_i sigma_j g_ij-a_h]/q^2, so the complete d positive-lag equations are exactly the stated equations; negative lags follow by symmetry and higher ones vanish by the actual window.
Empty repair adds only w_empty e0e0^T, hence preserves all those lags and gives the displayed energy.
Minimality proves nonzero actual values of every final atom as in Section1.

For any feasible edges, the triangle inequality at each gap gives sum_(j-i=h)g_ij>=|a_h|.
Summing gives G>=L, so strict E<1 requires L<n.
Conversely choose at each nonzero gap the lexicographically first actual pair whose sign is sign(a_h), and place integer mass |a_h| there.
This realizes ALL lag equations with G=L and loads d_i<=L.
If L<n, q=n makes every singleton weight positive and w_empty=L/n^2>=0.
Also a_d=p_0 p_d is+/-1, so L>=1 and the empty mass is actually positive in this canonical construction.
This proves(1) with a finite explicit rational law, not a solver or a second-moment hull relaxation.
Its energy is

    E_can=1-(n-L)/n^2<1.                            (2)

**Theorem 2 (exact infimum over this entire restricted family).**
If L<n, the least attainable energy, allowing ALL q>=2 and ALL rational feasible edges, is

    E_pair(P)=1-max{1/(n-1)^2,(n-L)/n^2}.            (3)

It is attained by an explicit finite law.
If L=n, the restricted infimum is1 and is attained.
If L>n, its infimum is1 but no finite member attains1.
These are restricted subset-law conclusions, not the full C16 capacity.

*Proof.*
For any successful law, G<n and nonnegative empty mass require G>=q(n-q).
If2<=q<=n-2, then q(n-q)>=2(n-2)>=n for n>=4, contradiction.
The interval is empty for n3.
Therefore every successful q satisfies q>=n-1.
At q=n-1, G>=n-1 and the deficit is at most1/(n-1)^2.
At q>=n, G>=L bounds the deficit by(n-L)/n^2.
The second bound is attained by the canonical construction already given.

To attain the first bound, start with the same G=L assignment and set q=n-1.
If L=n-1, no change is needed.
If L<n-1, there is some gap containing BOTH signs among its actual pairs: otherwise every gap has only one sign and L would equal the TOTAL number of unordered support pairs, n(n-1)/2>=n, a contradiction.
Choose the first such gap and one pair of each sign.
Add (n-1-L)/2 to BOTH of those edge weights.
Net lag values do not change; total G becomes n-1.
Every load is at most G=q, so all singleton weights are nonnegative; the empty mass is zero.
This yields the first deficit with no forbidden zero atom remaining.
All weights are rational and zero labels are omitted.
The larger of the two attainable deficits gives(3).

If L=n, the original G=L assignment with q=n gives E1 and valid probabilities.
If L>n, every finite G>=L makes E>1.
For that same fixed integer G=L assignment, take integers q>=max{n,L}; all weights are then nonnegative and E=1+(L-n)/q^2 tends to1.
This proves the infimum statement without claiming attainment or using an infinite packet.
In every case the actual finite full complementary identity has already been proved.

<a id="pair-correlated-offdiagonal-and-limits"></a>
## 4. The required signed covariance is actually present

For every feasible law the COMPLETE ordered signed support sum is

    sum_(i!=j in I)sigma_i sigma_j X_ij
       =(2G-n(n-1))/q^2.                            (4)

This uses actual original coefficients, not an unweighted graph overlap.
In the successful case G<n and n>=3, the right side is strictly negative.
Thus the constructed second moment is genuinely not diagonal while EVERY lag sum is zero.
It meets precisely the kind of off-diagonal requirement absent from C54.

For a more exact comparison with [C29](Yin_C_G0029_v1.md#statement), let H_flat=I+(diag(p_i^2)-pp^T)/(n-1), using the full original coefficient column.
The repaired law has

    Tr(H_flat X)=E-[sum_(i!=j)p_i p_j X_ij]/(n-1)
                 =1+G(n-3)/[(n-1)q^2]>=1.           (5)

The actual arithmetic-form floor is respected.
We do not turn the old diagonal obstruction into a full capacity lower bound.
No single off-diagonal entry is required to vanish, and cancellation occurs among the actual different pairs of the same lag.

As a direct useful failure control, the [original Lehmer coefficient autocorrelations](Yin_C_G0031_v1.md#lehmer-residue-dual-reuse-and-hand-kernel) recorded and independently adopted in C31 are(6,1,-2,-3,-4,-4,-2,1,2,1), with n9 and L26.
Hence THIS COMPLETE empty/singleton/pair marginal family cannot have energy below1 for that actual input, for any integer q or any feasible rational pair allocation.
This does not contradict C31's different successful packet or C17's unrestricted existence.
Merely adjusting our edge allocation or enlarging q cannot escape this exact restricted obstruction; larger subset support or another representative/marginal mechanism would be required.

<a id="pair-correlated-entire-original-costs"></a>
## 5. Actual denominators, all signs, contents and every copy

Every positive nonempty leaf has integer numerator

    F_B=P-q sum_(i in B)sigma_i t^i,

and each repaired leaf has F_+=P+q,F_-=P-q.
Since |B|<=2<n, some original support coefficient is unselected and remains+/-1.
Each F_B is therefore primitive and has ACTUAL coefficient denominator q after division.
For the two repairs the leading coefficient is1, also proving primitive content and actual denominator q.
At both physical endpoints0,d every such numerator coefficient is nonzero: an original+/-1 cannot equal q times its selected sign for q>=2, and p_0+/-q is nonzero.
Thus EVERY final atom and the union have actual physical width d.
No final support discount or different field basis is used.

Keep the actual indexed weights and define

    M=lcm_b denominator(omega_b), k_b=M omega_b>0,
    sum_b k_b=M.

These are integers.
For rational edges, if r clears all g_ij, M divides2r q^2; that is only a bound, not an asserted least denominator.
For the canonical integer G=L construction at q=n, the extreme gap d has its UNIQUE pair weight1/n^2.
The repaired weights are L/(2n^2).
All other weights have denominator dividing n^2.
Therefore its ACTUAL least final denominator is

    M_can=n^2 if L is even, and2n^2 if L is odd.      (6)

Positive labels may be split further, changing the indexed least denominator; all later formulas then use that actual M.
The q=n-1 construction may have half-integer edges and no empty mass, so its denominator is computed from its real final list rather than assigned(6).

More precisely, for the explicit q=n-1 construction of Theorem2 let r_extra=n-1-L.
Its least FINAL denominator is q^2 when r_extra is even, and2q^2 when r_extra is odd.
The original extreme-gap pair always has g_0d=1 (there is only one pair at gap d), forcing q^2 to divide M.
The extra opposite-sign pair cannot lie at that extreme gap.
If r_extra is even every edge and singleton numerator is integral over q^2; if odd the added two edges have genuine half-integer numerators, one such weight has an odd numerator over2q^2, and together with1/q^2 this forces M=2q^2.
There is no empty repair in this construction.
Thus both explicit attainers in(3) have exact final denominators, without claiming these minima for all split realizations.

Write nu=Norm_K(alpha)=(-1)^d p_0 in{+1,-1}.
Singleton actual values are -sigma_i alpha^i, with signed norms (-sigma_i)^d nu^i.
Pair actual values and complete norms are

    u_ij=-sigma_i alpha^i(1+sigma_i sigma_j alpha^(j-i)),
    D_ij=(-sigma_i)^d nu^i Norm_K(1+sigma_i sigma_j alpha^(j-i))
         in Z minus{0}.                             (7)

The last nonvanishing is from the actual minimal-polynomial argument, not from a selected embedding.
Repaired values+/-1 have signed norms1 and(-1)^d.
Let D_b denote these ACTUAL full signed original norms for every label.
Then

    Res(P,F_b)=q^d D_b,
    product_b Res(P,F_b)^(k_b)=q^(dM)product_b D_b^(k_b),
    Lambda=(1/(d q^2))sum_(i<j)g_ij log|D_ij|>=0,
    S_int=q^2 E,
    I=log q+Lambda,
    I-(1/2)log S_int=Lambda-(1/2)log E<=m(P).         (8)

The income formula uses the ACTUAL pair probabilities g_ij/q^2; singleton and repair absolute norms are1 but their signed factors still occur in the copied product.
All numerator contents here are exactly1 by the proof above, rather than being discarded by convention.
The last inequality is the [accepted complete C10 estimate](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) after every lag has been proved zero, with original T=d and the SAME final weights.
No extra uncancelled log q penalty or final-denominator substitution appears.

<a id="pair-correlated-uniform-surplus-ceiling"></a>
## 6. Full-surplus ceiling for every successful member of the mechanism

The restricted success test gives quantitative packets, but does not make their FULL surplus uniform in growing coefficient support.
At every original root beta,

    |1+/-beta^h|<=2 max(1,|beta|)^h.

Multiply over ALL original roots; the monomial factor in(7) has absolute norm1.
For every actual pair gap h<=d this gives

    0<=log|D_ij|<=d log2+h m(P)<=d[log2+m(P)].

For every successful law, G<n, q>=n-1 and L>=1.
Thus

    0<=Lambda<=G[log2+m(P)]/q^2
               <n[log2+m(P)]/(n-1)^2,
    0<1-E=(n-G)/q^2<=1/(n-1),
    0<Lambda-(1/2)log E
       <=n[log2+m(P)]/(n-1)^2+1/[2(n-2)].           (9)

The last estimate uses -log(1-z)<=z/(1-z), proved by integrating1/(1-z) over[0,z], with0<z<=1/(n-1)<1.
All constants apply to the ENTIRE successful pair-law family, not just the canonical allocation.
Along any inputs with n->infinity and bounded m(P), every such full surplus tends to zero, including all true pair norms and every permissible q.
In particular the norm income cannot silently repair the vanishing coefficient deficit in a hypothetical near-one growing-support sequence.

For bounded n satisfying L<n, (3) and(8) do give an explicit positive degree-independent subclass lower bound m(P)>=-(1/2)log E_pair(P), already from nonnegative full norm income.
No theorem here makes n bounded or L<n for arbitrary inputs.
At fixed n and bounded input measure, any successful q->infinity also has full surplus O(1/q^2), because G<n and the same two bounds apply before replacing q by n-1.
These are precise limits of this mechanism, not an impossibility theorem for larger correlated supports or the unrestricted problem.

<a id="pair-correlated-original-quartic-hand-control"></a>
## 7. A genuinely correlated original Salem-quartic packet, by exact hand algebra

Use the ACTUAL original P=t^4-t^3-t^2-t+1 and beta from [C51](Yin_C_G0051_v1.md#statement), at original d4 and O0=Z[beta].
Its flat support is I={0,1,2,3,4}, n5, with signs(1,-1,-1,-1,1).
Direct coefficient multiplication gives

    (a_1,a_2,a_3,a_4)=(0,-1,-2,1), L4<n5.

Choose q=n-1=4 and edges g_02=1,g_03=2,g_04=1, all others zero.
They satisfy the exact signed lag equations.
Loads are(4,0,1,2,1), G4=q, and the empty probability is ZERO.
The complete positive packet therefore needs no final empty repair:

| Bit set B | Numerator F_B | Actual value F_B(beta)/4 | Full signed norm | Weight |
| --- | --- | --- | --- | --- |
| {1} | P+4t | beta | +1 | 4/16 |
| {2} | P+4t^2 | beta^2 | +1 | 3/16 |
| {3} | P+4t^3 | beta^3 | +1 | 2/16 |
| {4} | P-4t^4 | -beta^4 | +1 | 3/16 |
| {0,2} | P-4+4t^2 | beta^2-1 | -3 | 1/16 |
| {0,3} | P-4+4t^3 | beta^3-1 | -1 | 2/16 |
| {0,4} | P-4-4t^4 | -1-beta^4 | +1 | 1/16 |

All seven atoms have exact coefficient denominator4, primitive numerators and physical width4.
Their strictly positive weights sum1 and have ACTUAL least denominator M16.
The theorem gives the full exact identity

    sum_b (16 omega_b)F_B(t)F_B(t^-1)=240,
    E=15/16, S_int15, M E15.                       (10)

This can also be checked without multiplying seven square polynomials: signed pair sums at lags1,2,3,4 are0,-1,-2,1 exactly, while their diagonal trace is15/16 by the actual probabilities.
Section3 proves that these quantities determine the complete Laurent identity, including negative lags and no higher lags.

The signed norms are hand exact.
Norm(beta)1 and d4 even give singleton norms1.
Since P(1)=-1 and P(-1)=3, Norm(beta^2-1)=P(1)P(-1)=-3.
For primitive cube roots zeta, reduction of the ORIGINAL P modulo t^2+t+1 is -t^2, whose product over that conjugate pair is1.
The elementary product over all cube roots thus gives Norm(1-beta^3)=P(1)*1=-1; degree4 makes the sign reversal harmless.
Finally1+beta^4=beta(1+beta+beta^2)=beta(beta^3-1)/(beta-1), with both denominator and numerator nonzero, so its full norm is1*(-1)/(-1)=1.
No field is replaced and no original conjugate is discarded.

The resulting FULL copied signed product and income are

    product_b Res(P,F_B)^(16 omega_b)=-3*4^64,
    Lambda=log3/64,
    I=log4+log3/64,
    m(P)>=log3/64+(1/2)log(16/15)>0.              (11)

The negative norms occur with multiplicities1 and2 respectively; their total signed product is-3.
This is a NEW explicit correlated recipe on a previously accepted actual input, not a new polynomial, a new optimum for full C16, a stronger-best-known quartic bound or a near-one family.
It differs from C31's original degree10 solver packet, and from C54's impossible flat-first-window diagonal law.
Formula(3) does show that15/16 is the EXACT optimum within THIS empty/singleton/pair uniform-marginal family for this quartic, since1/16>1/25; that limited optimum is not enlarged.

<a id="pair-correlated-complete-author-selfcheck"></a>
## 8. Complete author self-check, outcome and review boundary

The author reconstructed the complete finite probability law in both directions: all pair masses, forced singleton/empty probabilities, exact normalization and fixed marginals; actual signed coefficient mean zero, each off-diagonal entry and EVERY lag; minimality excluding all nonempty zero residues at subset size at most2; preservation of all original mass and mean by paired empty repair.
General nonreciprocal unit signs, p_0=-1, q2, n3, zero singleton/empty probabilities and omitted zero labels were retained.
No PSD-plus-trace or infinite closure substitutes for an actual finite law.

For Theorems1--2 the author checked each gap triangle bound, actual existence of a correct-sign pair, the extremal gap forcing L>=1, the q=n positive construction, and the necessary q>=n-1 condition for EVERY successful rational law.
The opposite-sign same-gap construction really exists whenever L<n-1, since otherwise L would equal all n(n-1)/2 pairs; both added masses are nonnegative and their load at any vertex cannot exceed the total G=q.
This checks both attained candidates in the exact restricted infimum, all L=n and L>n branches, and the distinction between infimum1 and finite attainment.
The restriction remains the explicit P/q signed-bit law with UNIFORM1/q marginals and at most two selected indices, not all modular codewords, correlated laws, representative packets or C16.

The arithmetic check keeps actual coefficient denominator q for EVERY final atom, primitive content proved from an unselected unit coefficient, both physical endpoints and width d, ACTUAL final M rather than an upper clearing bound, exact canonical and q=n-1 parity-dependent denominators, arbitrary positive splits and all copied signs.
Norm income uses only nonzero complete original values, with singleton/repair absolute norms1 but their signed factors retained in the full product.
The original full-root C10 inequality uses the same final weights and original T/d1 only after exact complementarity is established.
The original-root pair-norm upper bound and the q>=n-1 constraint establish(9) for ALL successful choices, including their full norm income; the conclusion is limited to bounded m and growing support n.

The original quartic check used exact support signs and all four autocorrelations, the specific three edges and all vertex loads, zero empty probability, seven positive original values, actual q4/M16/content1/width4, every signed original norm, the complete constant240 Laurent identity and copied product-3*4^64.
The exact full surplus and restricted optimum15/16 were retained without asserting a full-capacity optimum, a near-one family or best known bound.
The original Lehmer L26/n9 test is an exact failure of this ENTIRE limited recipe, not a contradiction of its separately adopted C31 packet.
Enlarging q, permuting the chosen correct-sign pairs or using the old independent recursion cannot bypass that gate.

The new outcome is an ACTUAL correlated finite construction and complete restricted success/capacity criterion, with a genuine flat original-Salem example and a precise all-q failure on original Lehmer.
It also gives a full-surplus ceiling that prevents this successful two-bit mechanism alone from yielding a uniform gap on bounded-measure inputs with n->infinity.
The next changed question would need larger subset support, different marginals or a different representative mechanism, with genuinely new control of its all-lag probabilities and full norms.
No such next exploration is started in this artifact.

All new formulas and proofs in this draft are by g0001_routes for Yin.
Root supplied only the broad correlated-packet task and received the author's proposed mechanism, not a mathematical step, correction or code.
The author previously extracted C54 and authored original-law C51/D6; those activities neither prove nor independently review the present result.
The old paired repair, C16/C17/C29/C31/C50/C54 interfaces and distinct C15 signed-period mechanism are credited at their stated scopes.
No recognized external dependent-rounding theorem, new source, native mathematical program, solver, enumeration, J or formal proof assistant was used.
Material checking validates structure only.
Whole noncontributor review, fixed extraction/adoption and any strategy update remain separate and root-coordinated.

<a id="pair-correlated-entire-author-freeze"></a>
## Entire author freeze

2026-10-12T10:42.
Freeze the ENTIRE starting question/reuse/proposed-model history and Sections1--8, Theorems1--2, equations(1)--(11), all feasibility/attainment cases, full original norms/copies/denominators/contents, exact positive and failed controls, complete surplus ceiling and source/contribution boundaries.
The proof has completed author checking and is a complete draft awaiting separately organized whole noncontributor review.
No independent verdict or fixed Claim adoption is supplied by this author.

This author stops here for independent review without extending the construction or running an experiment.
