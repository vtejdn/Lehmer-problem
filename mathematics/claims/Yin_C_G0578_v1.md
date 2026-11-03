---
author: Yin
---

# Complete integral cycle-to-tree conversion and exact Lehmer target costs

This retains the complete [L303](../ledger/Yin_L_G0303_v1.md) proof, actual congruence and all full factors/costs, with its original written/computational findings together in [R784](../audits/reviews/Yin_R_G0784_v1.md#preserved-complete-original-r202-accounts).

<a id="statement"></a>
## Complete statement

For EVERY integer n>=4, in the standard basis e_0,...,e_n let V_n be integral upper unitriangular with exactly
    V_(i,i+1)=-1 (0<=i<=n-3), V_(n-2,n-1)=+1,
    V_(0,n-1)=V_(n-1,n)=-1
above the diagonal.
Let V_n^- replace each upper entry by its negative magnitude.
Put h=e_1+...+e_(n-2), and let Q_n have ordered columns
    e_0,-e_2,...,-e_(n-2),e_(n-1)-h,h,e_n.
Q_n is integral unimodular and W_n=Q_n^T V_n Q_n is upper unitriangular with exactly the negative unit edges
    (j,j+1) for1<=j<=n-4,
    (0,n-1),(n-3,n-1),(n-2,n-1),(n-2,n).
Empty ranges are allowed at n=4.
This is the actual all-negative three-arm tree with arm EDGE lengths1,2,n-3, with no stabilization or nonintegral lattice change.

Using p_V=det(tV+V^T),C_j=1+t+...+t^j, the COMPLETE polynomials are
    P_n=(t+1)^2(t^(n-1)+1)-t C_(n-1),
    A_n=(t+1)(t-1)(t^(n-1)-1)-t C_(n-1).
For F=t^3-t-1,F*=1-t^2-t^3,G=t^3-2t^2-t+1,G*=1-2t-t^2+t^3,
    P_n=[t^(n-1)F-F*]/(t-1), A_n=[t^(n-1)G-G*]/(t-1).
The reversals have actual degree3; division removes no factor from the actual determinant.
The same-polynomial integral conversion gives
    p_(W_n)=p_(W_n^-)=P_n,
    p_initial_literal_cover=P_n A_n,
    p_final_literal_cover=P_n^2.
Every neutral factor and multiplicity remains.
V_n/V_n^- rank,height,energy are(n+1,1,n+1), W_n costs(n+1,1,n), and their covers have rank2n+2,height1 and energies2n+2/2n.

The FULL original zero-measure boundaries are
    P_4=Phi2 Phi8, P_5=Phi3 Phi12, P_6=Phi2 Phi18,
    P_7=Phi30, P_8=Phi1^2 Phi2 Phi3 Phi5.
For EVERY n>=9, let theta be the unique real plastic root of F in(1,4/3), chi the G root in(2,5/2).
P_n/A_n have exactly one simple positive expanding reciprocal pair beta_n/alpha_n, with
    1<beta_n<theta<4/3<2<chi<alpha_n<3.
All other roots lie on the circle, and full measures are log beta_n and log alpha_n.
beta_n strictly increases to theta and alpha_n strictly decreases to chi.
The full cover saving at the SAME P_n is log(alpha_n/beta_n)>log(chi/theta)>log(3/2).
No energy surrogate or rank normalization is used.

The unique positive irreducible factors R_n/S_n occur once and are reciprocal, with all other factors cyclotomic.
For b=beta_9,
    deg R_n>2+[(n-1)log b-log8]/log3,
    deg S_n>2+[(n-1)log chi-log26]/log5.
Every contracting and circle conjugate is retained in the complete nonzero INTEGER resultant against F/G.
Full irreducibility at arbitrary n is not asserted.
For n>=9 the full original measure is at least log b>0, with equality exactly at n=9, and tends increasingly to log theta.

At n=9, P_9 is the FULL actual Lehmer polynomial
    L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1
without a neutral multiplier.
W_9 has rank10,height1,energy9, identical full companion L and literal cover L^2 at rank20/energy18.
Over EVERY proper integral upper-unitriangular V of ANY rank/height with complete polynomial L times a monic cyclotomic product, full cover measure>=2log b.
The tree attains that exact infimum AND minimum.
In the SAME stabilized target class rank>=10,energy>=9 and literal-cover rank>=20,energy>=18, attained simultaneously.
The irreducibility and complete scalar target are actual accepted inputs; the bound is not a universal lower bound on signed original measure or coverage of arbitrary targets.
No n>9 companion optimum is claimed.

The classical Y_(2,3,n-2) family and Lehmer/plastic comparison retain McM02's actual selected attribution.
Its separate accepted canonical-action Theorem1.1 is used ONLY through C573's complete integral companion lower bound for the exact target minimum.
Hir06 supplies its already scoped classical root mechanism, with the local full-root proof retained.
The original J76 nine indices n=4,...,12 retain all45 complete arrays,612 pencils, every Q/inverse/congruence/edge/expense/boundary and native type, with original author2026-10-10T07:13 runtime0.2845266000076663seconds and120-second caps.
The original complete computational finding is in R202; its exact act minute/runtime are unrecorded and not invented.
No new source/native/program execution, near-zero family, general scalar realization or unrestricted gap is asserted.

## Complete argument

<a id="argument"></a>

<a id="plastic-tree-reuse-and-cost-question"></a>
### 1. Exact reuse and the changed question

The Task, repository entry rules and knowledge-reuse rule were read.
The local screen read the full [L299 unit-cycle leaf argument](Yin_C_G0567_v1.md#statement), [L184 cycle-order formula and integral sweep](Yin_C_G0437_v2.md#cycle-order-polynomial), [L203 pendant determinant and exterior-root argument](Yin_C_G0488_v1.md#pendant-chain-full-determinant), [L238 uniform companion lower bound](Yin_C_G0573_v1.md#uniform-companion-gap-and-bounded-ratio), and the [D9 literal cover](Yin_C_G0002_v1.md#signed-cover-identity).
L38's plastic PLUS sequence is a different sign from the minus sequence below and is not silently substituted.
These interfaces suffice for the new calculation.
The unavailable local path `framework/rules/knowledge.md` in one operational read was corrected to the existing `knowledge-reuse.md`; no missing mathematical source or proof was assumed.

The lower seed discovered by changing the cycle's ordering is t^3-t-1.
Its three-arm tree realization is CLASSICAL.
To check that recognition before sustained work, I directly text-read the already acquired published [McM02](../audits/literature/McM02/readme.md) PDF, printed pp.154--155/PDF pp.4--5.
The source explicitly describes Y_(2,3,n), identifies Y_(2,3,7) with the Lehmer number, and places that family below the plastic number.
These are attribution/comparison passages, not a newly adopted classification theorem or a full proof audit.
The source's usual branch parameter includes the central vertex, so our arm EDGE lengths1,2,n-3 are its parameters2,3,n-2.
The actual plus-sign matrix identities and root bounds are proved below.
The classical Salem-Boyd root mechanism retains the already inspected [Hir06](../audits/literature/Hir06/readme.md) scope and L203's local no-circle-zero proof.
No new source intake or novelty claim is needed.
L238's already accepted McM02 Theorem1.1 interface is used only for the exact companion optimum in Section5, with its existing statement/applicability depth unchanged.

The changed objective is not to rediscover the scalar tree family.
It is to track an explicit integral CONGRUENCE from a signed one-cycle presentation to that tree, its complete nonneutral companion expense, its exact cost saving at all positive indices, and the attained whole-cover optimum at the original Lehmer input.
The initial matrices use one cyclic ascent rather than L299's balanced ascent count; the same graph shape can therefore have a different full polynomial.
All new deductions here are by orbit_research for Yin; root supplied only the broad question and allocation coordination.

<a id="ordered-cycle-leaf-tree-congruence"></a>
### 2. Actual standard matrices and an explicit integral conversion

For every integer n>=4, use standard basis e_0,...,e_n and put V_n upper unitriangular with exactly these nonzero strict-upper entries:

    V_(i,i+1)=-1, 0<=i<=n-3;
    V_(n-2,n-1)=+1;
    V_(0,n-1)=-1;  V_(n-1,n)=-1.                    (1)

The first n vertices form a frustrated n-cycle; vertex n is its leaf.
Its cycle has n-1 ascents, equivalently one after reversing traversal.
Let V_n^- replace all upper entries by their negative magnitudes.
Both have rank n+1, height1 and squared strict-upper energy n+1.
These are actual standard integer matrices, not abstract determinant targets.

Define h=e_1+...+e_(n-2), and let Q_n have the following columns in this order:

    e_0, -e_2,...,-e_(n-2), e_(n-1)-h, h, e_n.       (2)

This is an integral unimodular basis.
Apart from the displayed sign changes, its path block is exactly the final L184 sweep; alternatively h together with e_2,...,e_(n-2) recovers e_1, and h with e_(n-1)-h recovers e_(n-1), directly giving an integral inverse.
Direct bilinear pairing in(1) proves that W_n=Q_n^T V_n Q_n is upper unitriangular with all nonzero upper entries equal to-1.
In the NEW indices, its complete edge list is

    (j,j+1), 1<=j<=n-4;
    (0,n-1), (n-3,n-1), (n-2,n-1), (n-2,n).         (3)

Empty ranges are allowed, notably at n=4.
Thus the central vertex n-1 has three arms with edge lengths1, n-3 and2.
The internal sign changes in(2) convert the one positive last-interior-to-h edge of the raw sweep to-1 without changing its path edges.
Pairings of e_0 with e_(n-1)-h cancel exactly; that vector alone retains the old leaf coupling.
All below-diagonal pairings vanish, and each diagonal pairing is one.
This verifies the complete congruence rather than only its symmetric part or polynomial.

Consequently W_n has rank n+1, height1, energy n and W_n^-=W_n.
The conversion lowers energy by one but, more importantly, changes the whole absolute polynomial while preserving the whole original.
The initial and final literal covers have rank2n+2, heights1 and energies2n+2 and2n respectively.
No stabilization, nonintegral lattice or hidden factor has entered.

<a id="plastic-tree-complete-polynomials"></a>
### 3. Full polynomials and all neutral factors

Write C_j=1+t+...+t^j.
L184's ordered-cycle determinant and the exact leaf expansion give

    P_n=det(tV_n+V_n^T)
       =(t+1)^2(t^(n-1)+1)-t C_(n-1),
    A_n=det(tV_n^-+(V_n^-)^T)
       =(t+1)(t-1)(t^(n-1)-1)-t C_(n-1).            (4)

The deleted neighbor leaves a path with n-1 vertices, so its determinant is exactly C_(n-1).
Put

    F=t^3-t-1,       F^*=1-t^2-t^3,
    G=t^3-2t^2-t+1,  G^*=1-2t-t^2+t^3.

Multiplication of(4) by t-1 gives the complete sparse identities

    P_n=[t^(n-1)F-F^*]/(t-1),
    A_n=[t^(n-1)G-G^*]/(t-1).                       (5)

Every reversal here is at actual degree three.
The numerators have the shown factor t-1; the quotient is the ACTUAL degree n+1 determinant, not a selective factor removal.
Congruence and the literal cover identity now give

    p_(W_n)=p_(W_n^-)=P_n,
    p_initial_cover=P_n A_n,
    p_final_cover=P_n^2.                             (6)

Both covers retain all cyclotomic factors with their full multiplicities.
There is no assertion that P_n is always irreducible.
The complete zero-measure starting polynomials are

    P_4=Phi2 Phi8,
    P_5=Phi3 Phi12,
    P_6=Phi2 Phi18,
    P_7=Phi30,
    P_8=Phi1^2 Phi2 Phi3 Phi5.                       (7)

These follow by direct multiplication in(5).
Here the subscripts are family indices, not the quartic denoted P4 in earlier ledgers.
The boundary has no positive-measure success hidden inside it.
At n=9,

    P_9=L=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,          (8)

the complete original Lehmer polynomial.
Thus W_9 gives it at rank10 with no neutral multiplier, height1 and energy9; its complete companion is L and cover is L^2 at rank20/energy18.
This is the classical Coxeter realization, now matched to the precise local matrix and full signed-to-tree expense.

<a id="plastic-tree-all-root-cost"></a>
### 4. Every exterior root and the genuine change in total expense

Let theta be the unique real root of F.
It lies in(1,4/3), and its other two roots are a conjugate pair of modulus theta^(-1/2)<1.
Indeed the two critical values of F at plus/minus1/sqrt3 are negative, so it has only one real root; its root product is one.
Let chi be the unique root of G in(2,5/2).
The other two real roots lie in(-1,0) and(0,1), by signs at -1,0,1,2,5/2.
Thus F and G have no unit-circle root and each has exactly one exterior root.

The elementary L203/Hir06 argument then bounds the number of exterior roots of each numerator in(5) by one, with multiplicity: for0<=epsilon<1, compare t^(n-1)F with epsilon F^* on the unit circle, then pass epsilon to1 in disjoint exterior disks.
The same applies to G.
Dividing by t-1 changes no exterior root.
The full determinants are reciprocal, so any exhibited positive exterior root has exactly one contracting reciprocal and all remaining roots on the circle.

At t=1, the full values are P_n(1)=8-n and A_n(1)=-n.
At theta, F^*(theta)=-theta(theta+1)<0, so P_n(theta)>0.
At chi, G^*(chi)=chi(chi-1)>0, so A_n(chi)<0.
Finally G(3)=7 and G^*(3)=13 give A_n(3)>0 for n>=4.
Therefore for all n>=9 there are unique simple expanding roots

    1<beta_n<theta<4/3<2<chi<alpha_n<3,
    m(P_n)=log beta_n, m(A_n)=log alpha_n.            (9)

The original boundary n=4,...,8 was completely factored in(7); the companion already has its unique positive exterior root for every n>=4.
These roots are not found numerically.
At beta_n the next original numerator equals(beta_n-1)F^*(beta_n)<0, so beta_(n+1)>beta_n.
At alpha_n, G^*(alpha_n)>0 (its derivative is positive above2 and G^*(2)=1), so the next absolute numerator is positive and alpha_(n+1)<alpha_n.
Dividing the root equations by t^(n-1), using beta_n>=beta_9>1 and alpha_n>chi, proves

    beta_n increases to theta, alpha_n decreases to chi.

Thus the two actual presentations of the SAME full P_n have expenses

    initial companion/cover: log alpha_n,
                              log beta_n+log alpha_n;
    final companion/cover:   log beta_n, 2log beta_n;
    saving =log(alpha_n/beta_n)>log(chi/theta)>log(3/2).
                                                               (10)

The limiting covers are log theta+log chi and2log theta.
The conversion removes an entire nonneutral companion factor expense at fixed rank and original polynomial, not merely a decrease of energy used as a surrogate for measure.
It is an explicit allowed integral basis conversion, rather than an arbitrary comparison of unrelated presentations.

Each P_n for n>=9 has a unique reciprocal positive-measure monic irreducible factor R_n once, with every other irreducible factor cyclotomic; the same holds for A_n with factor S_n.
The unit constant forces the sole contracting reciprocal into the factor containing the sole expanding root; reversal then gives the same irreducible factor.
The circle-only criterion is the one already used in L203/L299.
Hence the actual neutral degrees remain n+1-deg R_n and n+1-deg S_n, and their multiplicities persist in(6).
Strict root motion makes the factors pairwise distinct; bounded root moduli force both degrees to tend to infinity.

For an explicit linear version put b=beta_9.
On the original expanding root, |F(beta_n)|=|F^*(beta_n)|beta_n^(-(n-1))<4b^(-(n-1)); on its contracting reciprocal |F|<2, and on every circle root |F|<=3.
The integer resultant Res(F,R_n) is nonzero: F's complex interior roots are neither the only positive contracting root nor circle roots, and beta_n!=theta.
Therefore

    deg R_n>2+[(n-1)log b-log8]/log3.                (11)

For the companion, |G(alpha_n)|<13chi^(-(n-1)), |G(1/alpha_n)|<2 (evaluate on0<t<1/2), and |G(z)|<=5 on the circle.
The cubic G is irreducible because its only possible rational roots are plus/minus1 and both give -1.
Its seed's two interior roots cannot be a positive reciprocal in S_n: if one coincided, irreducibility of G would force chi among the conjugates of S_n, contrary to alpha_n>chi.
Thus Res(G,S_n) is nonzero and

    deg S_n>2+[(n-1)log chi-log26]/log5.             (12)

The original total measure approaches log theta, strictly below log phi from L299, with genuine linearly growing positive irreducible complexity.
It stays at least the fixed positive log b, with equality exactly at n=9.
Neither this classical family nor its new explicit cost accounting supplies measures tending to zero.

<a id="lehmer-whole-cover-optimum"></a>
### 5. An exact attained cost benchmark at the original Lehmer input

Consider ANY proper integral upper-unitriangular presentation V, of any rank, with complete polynomial L times a monic cyclotomic product.
Its complete original measure is log b>0.
The already accepted L238 theorem, including its precise McM02 canonical-action and large-entry treatment, gives m(p_(V^-))>=log b.
Therefore

    m(p_literal_cover)>=2log b.                      (13)

W_9 attains equality by(8).
Thus2log b is the exact infimum AND minimum of the full proper-cover measure over this specified stabilized scalar target.
The conclusion is not that every positive input has measure at least log b, nor that every scalar target is realizable.
For n>9 the corresponding2log beta_n tree expense is not claimed optimal; another presentation could have a smaller companion while still respecting L238.

There are elementary attained rank and energy bounds at the SAME target.
The degree forces rank>=10.
Decompose the support graph of an arbitrary presentation into its connected components.
Simultaneously permuting the pencil makes a block determinant, even though that permutation need not be an allowed upper-unitriangular congruence.
The irreducible L must divide one component determinant, whose degree is its number of vertices and is at least10.
A connected graph on that many vertices needs at least9 nonzero edges; integral entries make the squared energy at least9.
W_9 attains rank10, height1 and energy9 simultaneously.
Every literal proper cover doubles rank and energy, so rank20/energy18 are also attained minima in this stated class.
Stabilized presentations and multiple-edge integers were included in the lower bound, rather than silently restricting to trees.
The established irreducibility of the original Lehmer polynomial is reused from its [fixed L170 input](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem), not inferred from a short coefficient table.

<a id="plastic-tree-verification-declaration"></a>
### 6. Finite check declared before execution

Request a responsible J for exactly n=4,5,6,7,8,9,10,11,12, nine explicit inputs(1), with aggregate author runtime cap120seconds and NO search.
Retain V_n,V_n^-,Q_n,W_n and both actual literal covers.
Check Q_n unimodular with its displayed full integer inverse, the entire congruence Q_n^T V_n Q_n=W_n and every edge/diagonal in(3); compute complete original, initial absolute, final original, initial cover and final cover polynomials and rank/height/energy.
Certify every polynomial with degree-plus-one integer pencil values.
Check all complete boundary factors(7), exact L at n9, both formal seed numerator identities and endpoint formulas, and the n9 unfilled neutral degree0.
This finite verification does not prove the all-n conversion, exterior-root count, limits, degree or global optimum by extrapolation; those are the written arguments above.
Actual execution and any failure will be recorded after the run, without extending the declared domain.


<a id="plastic-tree-author-verification-and-scope"></a>
### 7. Actual computation, complete self-check and the remaining gap

The declared nine-input calculation is retained in [J76](../computations/programs/Yin_J_G0076/readme.md), with author `verify.py` and complete `result.json`.
Its FIRST and SOLE execution at2026-10-10T07:13 passed in0.2845266000076663seconds on Python3.12.14/SymPy1.14.0.
It checked all45 full coefficient arrays and612 direct integer pencil evaluations, all nine entire congruences and integral inverses, exact tree edge lists, ranks/heights/energies, all five boundary factorizations, the original unfilled Lehmer control, the formal independent-y numerator identities and seed endpoint values.
The new program reuses the author's J75 helpers openly; it is author verification, not an independent computational review.
No failure, restart, parameter search, extra index, numerical root approximation or cap expansion occurred.
The all-n argument and the source-based lower optimum are not established by the finite checks.

The author reread the complete proof and checked the following chain.
The support and one-ascent count in(1) match the precise L184 convention, and the signed block basis in(2) has an integral inverse and the entire upper-unitriangular target(3), not just a matching Gram matrix.
The two pendant deletions retain exactly the cycle and path scalar factors.
Every reversal and t-1 division is made at its displayed actual degree, and the final cover contains the whole square including all neutral multiplicities.
The elementary root bounds account for every exterior root, the explicit zero-measure cases and all contracting/circle roots, without assuming all-n irreducibility.
Both monotonicity signs are checked at the previous root, and the two root equations give the claimed fixed-seed limits.
The integer-resultant degree lower bounds include all conjugates and prove nonvanishing at their actual factor scopes.
The scalar saving concerns complete logarithmic measures, while dimension and energy are separately charged.
L238's uniform companion theorem is used only at the exact positive original target L times a cyclotomic product; connected support components then give the independent rank/energy minima, with no converse realization assertion.

The useful result is an explicit all-size same-polynomial cost conversion and an exact, attained full-cost benchmark.
It strengthens the interpretation of signed presentations: a nonneutral absolute companion expense may be removable by an actual integral congruence, and the classical small scalar target supplies the limiting comparison that the phi family did not.
The original positive factors have unbounded, indeed at least linear, degree, but their complete measures remain at least log(beta_9)>0 and tend to log(theta).
The source recognition is not rebranded as a new Salem construction or a new proof of its historical priority.
Other scalar inputs, changed forms outside the displayed congruence, cheaper companions for n>9, and a coverage mechanism for hypothetical smaller total measures remain open.
Neither the universal companion lower bound nor this optimality at one exact target lower-bounds all signed original measures.
The unrestricted G0001 objective remains unresolved; its current execution is paused.
The original separately organized whole findings are retained in R202 at their actual inputs and checking relationships; current adoption is governed by the explicit current assessment below.




## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:48 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Entire initial/final determinant products and doubled actual rank/energy. |
| dependency | [Ordered cycle and sweep mechanism](Yin_C_G0437_v2.md#cycle-order-polynomial) | Actual ordered-cycle matching/sign convention; the entire new Q/congruence is displayed and checked locally. |
| dependency | [Complete leaf/exterior-root proof](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Full induced path/leaf determinant and no-circle-seed exterior-root mechanism, not a transferred topological convention. |
| dependency | [Complete absolute-companion lower bound](Yin_C_G0573_v1.md#uniform-companion-gap-and-bounded-ratio) | ALL positive-original-measure proper integral ranks/heights, canonical-action/large-entry cases; applied only to full L times cyclotomic target for the attained optimum. |
| dependency | [Actual Lehmer irreducibility](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | The actual degree10 irreducible full polynomial and its Salem root; no full-core certificate is a new premise of the matrix proof. |
| support | [Original complete J76 evidence](../computations/programs/Yin_J_G0076/readme.md) | Entire nine-input finite arrays/pencils/basis/native scope, with actual original computation finding in R202 and no rerun. |
| support | [Original complete proof/input](../ledger/Yin_L_G0303_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--13, all original attribution/author/native/failed-scope limits and old R202 written/computational inputs. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:55 |
| status | proved |
| reason | Adopt after actual whole SELF of the entire published Statement and complete Argument; original unknown review arrangements remain unknown and no isolated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Entire initial/final determinant products and doubled actual rank/energy. |
| dependency | [Ordered cycle and sweep mechanism](Yin_C_G0437_v2.md#cycle-order-polynomial) | Actual ordered-cycle matching/sign convention; the entire new Q/congruence is displayed and checked locally. |
| dependency | [Complete leaf/exterior-root proof](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Full induced path/leaf determinant and no-circle-seed exterior-root mechanism, not a transferred topological convention. |
| dependency | [Complete absolute-companion lower bound](Yin_C_G0573_v1.md#uniform-companion-gap-and-bounded-ratio) | ALL positive-original-measure proper integral ranks/heights, canonical-action/large-entry cases; applied only to full L times cyclotomic target for the attained optimum. |
| dependency | [Actual Lehmer irreducibility](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | The actual degree10 irreducible full polynomial and its Salem root; no full-core certificate is a new premise of the matrix proof. |
| support | [Original complete J76 evidence](../computations/programs/Yin_J_G0076/readme.md) | Entire nine-input finite arrays/pencils/basis/native scope, with actual original computation finding in R202 and no rerun. |
| support | [Original complete proof/input](../ledger/Yin_L_G0303_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--13, all original attribution/author/native/failed-scope limits and old R202 written/computational inputs. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0759_v1.md#cycle-tree-whole-self) | Entire current Statement and complete original proof chain, every actual domain/cost/source/native/negative qualification; SELF with prior context, not a replacement of historical UNKNOWN independent scope. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Full literal proper cover](Yin_C_G0002_v1.md#signed-cover-identity) | Entire initial/final determinant products and doubled actual rank/energy. |
| dependency | [Ordered cycle and sweep mechanism](Yin_C_G0437_v2.md#cycle-order-polynomial) | Actual ordered-cycle matching/sign convention; the entire new Q/congruence is displayed and checked locally. |
| dependency | [Complete leaf/exterior-root proof](Yin_C_G0488_v1.md#pendant-chain-full-determinant) | Full induced path/leaf determinant and no-circle-seed exterior-root mechanism, not a transferred topological convention. |
| dependency | [Complete absolute-companion lower bound](Yin_C_G0573_v1.md#uniform-companion-gap-and-bounded-ratio) | ALL positive-original-measure proper integral ranks/heights, canonical-action/large-entry cases; applied only to full L times cyclotomic target for the attained optimum. |
| dependency | [Actual Lehmer irreducibility](Yin_C_G0399_v1.md#lehmer-infinite-core-theorem) | The actual degree10 irreducible full polynomial and its Salem root; no full-core certificate is a new premise of the matrix proof. |
| support | [Original complete J76 evidence](../computations/programs/Yin_J_G0076/readme.md) | Entire nine-input finite arrays/pencils/basis/native scope, with actual original computation finding in R202 and no rerun. |
| support | [Original complete proof/input](../ledger/Yin_L_G0303_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--13, all original attribution/author/native/failed-scope limits and old R202 written/computational inputs. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0784_v1.md#cycle-tree-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R784. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0076](../computations/programs/Yin_J_G0076/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
