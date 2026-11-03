---
author: Yin
---

# Complete single-pair companion equality and Perron-weighted frustration prices

This retains the complete necessary mathematical argument from [complete original L405](../ledger/Yin_L_G0405_v1.md#single-expanding-companion-question).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

For every real r-by-g matrix B, V_B=[[I_r,-B],[0,I_g]], p_B=det(tV_B+V_B^t), p_abs=p_(|B|) and the literal full cover p_cover=p_B p_abs have the COMPLETE determinant p_B=(t+1)^|r-g| product_(i=1)^min(r,g)(t^2+(2-sigma_i^2)t+1), keeping zero singular values and all multiplicities.
With f(s)=0 for 0<=s<=2 and f(s)=2arcosh(s/2) for s>2, ordinary unnormalized total measures are m(p_B)=sum_i f(sigma_i) and m(p_cover)=m(p_B)+m(p_abs).
Assume exactly ONE singular value sigma_*>2 counted with multiplicity, equivalently exactly one simple positive expanding/contracting reciprocal pair of the full determinant; no irreducibility or integrality is assumed.
A nonzero connected bipartite edge block C has ||C||_2<=||H||_2 for H=|C|, with equality exactly when every entry sign can be written u_i v_j for row/column signs, equivalently every support cycle has positive sign product.
The direct nonnegative Gram maximizer proof gives strict positivity even for rectangular/single-column blocks; equality in every row triangle then gives the full switching, and switching preserves EVERY singular value and polynomial.
Decompose the support into edge components C_j and isolated vertices.
Exactly one C_* carries sigma_*>2; m(p_abs)>=m(p_B) and m(p_cover)>=2m(p_B), with equality exactly when C_* is switchable and EVERY other absolute block has norm<=2.
Other neutral polynomials may differ while costs agree; with one nontrivial connected component switching also gives equality of complete original/absolute polynomials including isolated Phi2 factors.
For any connected non-switchable real block C with sigma=||C||_2>2, let H=|C|,tau=||H||_2 and choose any strictly positive vector w with H^tH w=tau^2w.
For EVERY row k and two distinct supported columns i<j retain the separate signed multigraph edge e=(k,i,j), a_e=|C_ki C_kj|w_iw_j>0 and epsilon_e=sign(C_ki C_kj); opposite parallel edges are never merged.
Writing x_i=w_i y_i gives the exact identity tau^2||x||_2^2-||Cx||_2^2=E_w(y)=sum_e a_e(y_i-epsilon_e y_j)^2 and tau^2-sigma^2=min_(y!=0)E_w(y)/sum_i w_i^2 y_i^2.
The column multigraph is connected and sign balanced exactly when C is switchable, so the non-switchable case has a negative cycle Gamma, allowing an opposite parallel-edge two-cycle.
Choose any base v on Gamma and simple paths P_j from v to all column vertices, including the empty path at v; R_Gamma=sum_(e in Gamma)1/a_e, R_j=sum_(e in P_j)1/a_e and K=sum_j w_j^2(sqrt(R_Gamma)/2+sqrt(R_j))^2 are finite with K>0.
Signed telescoping and full-energy Cauchy--Schwarz give tau^2-sigma^2>=1/K>0, even when paths meet or overlap the cycle or one another; K is invariant under every positive rescaling of w.
In the single-expanding-pair full determinant when its expanding component is such a C, the COMPLETE cost difference is m(p_abs)-m(p_B)>=1/[tau sqrt(tau^2-4)K]>0, with all other absolute components charged nonnegatively and the decreasing derivative direction retained.
The actual integral L299 frustrated-cycle/leaf family at every a>=5 has one expanding pair on each side and both roots tending to phi, so its positive cost difference tends to zero and K must diverge for EVERY chosen negative cycle/path system.
The existing L234 many-pair ratio family lies outside the single-pair hypothesis and keeps its growing measure/repeated quadratic costs; the original J104 rank-nine finite test and rank-ten minimum conclusion are motivation only, with no native computation used as a proof premise here.
The complete original ten-formula classification/resistance argument, all neutral/zero/rectangular cases, full fixed-input roles and both original listed author checks are retained below.
This is a paid LOWER comparison: no uniform additive margin, upper-cost realization, bounded neutral padding, all nonbipartite theorem, near-one family, numerical Perron/cycle run or new Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:54 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Full rectangular pencil comparison](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Existing complete Gram/polynomial/neutral-factor cost identity; arbitrary-real rectangular and transpose cases are also proved directly here. |
| dependency | [Literal full signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Exact original-times-absolute sheet determinant and row/column switching sufficiency; local real block extension has its full direct proof. |
| dependency | [Actual connected frustrated family](../ledger/Yin_L_G0299_v1.md#unit-cycle-leaf-full-polynomials) | Actual integral cycle-leaf matrices with all full polynomials, all a>=5 one-pair threshold, exact original and companion measures. |
| dependency | [Actual nonuniform-margin control](../ledger/Yin_L_G0299_v1.md#unit-cycle-leaf-root-motion) | Every expanding root and full costs tend to positive log phi; necessary divergence of EVERY charged cycle/path K is conditional on these actual matrices. |
| support | [Multiple-pair comparison](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) | Accepted many-pair vanishing companion/original ratios with growing measure and repeated quadratic factors, outside the single-pair hypothesis. |
| support | [Motivation only](../computations/programs/Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) | Original rank-nine finite test and rank-ten all-bipartite minimum consequence only; no native computation is a proof premise or rerun here. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:00 |
| status | proved |
| reason | Adopt after actual entire SELF of the complete real rectangular full-spectrum one-pair equality and disconnected-neutral classification, exact all-edge weighted energy, negative-cycle/path resistance and complete logarithmic lower-cost proof, with all fixed-input and nonuniformity limits. No upper realization or independent replacement is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Existing complete Gram/polynomial/neutral-factor cost identity; arbitrary-real rectangular and transpose cases are also proved directly here. |
| dependency | [Exact dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Exact original-times-absolute sheet determinant and row/column switching sufficiency; local real block extension has its full direct proof. |
| dependency | [Exact dependency](Yin_C_G0567_v1.md#unit-cycle-leaf-full-polynomials) | Actual integral cycle-leaf matrices with all full polynomials, all a>=5 one-pair threshold, exact original and companion measures. |
| dependency | [Exact dependency](Yin_C_G0567_v1.md#unit-cycle-leaf-root-motion) | Every expanding root and full costs tend to positive log phi; necessary divergence of EVERY charged cycle/path K is conditional on these actual matrices. |
| support | [Exact support](Yin_C_G0573_v1.md#walsh-companion-ratio-fixed-scope) | Accepted many-pair vanishing companion/original ratios with growing measure and repeated quadratic factors, outside the single-pair hypothesis. |
| support | [Exact support](../computations/programs/Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) | Original rank-nine finite test and rank-ten all-bipartite minimum consequence only; no native computation is a proof premise or rerun here. |
| review | [Exact review](../audits/reviews/Yin_R_G0711_v1.md#complete-single-pair-frustration-whole-self-finding) | ENTIRE Statement and complete original ten-formula proof, every singular/neutral/rectangular case, all signed parallel edges/weights/paths/normalization and full-cost constants, source/contribution/motivation/negative limits, explicitly SELF. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-18T14:43.
Human author Yin.
Root develops this S3/S6 structural continuation of the rank-nine test.
This is author work, without independent review, adoption or a numerical experiment.

<a id="single-expanding-companion-question"></a>
## Exact question and prior scope

[L191](Yin_C_G0458_v2.md#retained-integral-gram-realization-proof) supplies the full rectangular Gram determinant and spectral costs.
[L234](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) supplies companion/original ratios tending to zero with many expanding pairs, growing original measure and a repeated quadratic factor.
The sign-switching sufficient mechanism belongs to [C2](Yin_C_G0002_v1.md#signed-cover-identity) and is also proved directly below.
The present question restricts the ACTUAL complete original determinant to one expanding reciprocal pair and seeks a necessary and sufficient equality criterion, including disconnected neutral components.
[J104](../computations/programs/Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) motivates the question but is not a premise of this proof.

For arbitrary real r-by-g B, put V_B=[[I_r,-B],[0,I_g]], p_B(t)=det(tV_B+V_B^t), p_abs=p_|B|, and p_cover=p_B p_abs for the literal full signed cover.
For ALL min(r,g) singular values sigma_i, including zeros and multiplicities, a Schur complement for t!=-1 followed by polynomial identity gives

    p_B(t)=(t+1)^|r-g| product_i[t^2+(2-sigma_i^2)t+1].       (1)

Each zero singular value contributes(t+1)^2; no neutral factor is suppressed.
With f(s)=0 for0<=s<=2 and f(s)=2 arcosh(s/2) for s>2,

    m(p_B)=sum_i f(sigma_i),
    m(p_cover)=m(p_B)+m(p_abs).                              (2)

All measures are complete ordinary logarithmic Mahler measures, without normalization by rank.
Assume exactly ONE singular value sigma_*>2, counted with multiplicity.
Equivalently p_B has one simple positive expanding/contracting reciprocal pair and all other roots lie on the circle.
No irreducibility is assumed, and m(p_B)=f(sigma_*)>0.

<a id="connected-sign-equality"></a>
## Complete equality case for connected support

The support graph has row and column vertices and an edge wherever B_ij!=0, carrying its sign.
A component is switchable if signs u_i,v_j in{1,-1} satisfy B_ij=u_i |B_ij|v_j on every edge.
Equivalently every cycle has positive sign product: one direction cancels vertex signs twice, and the reverse follows by propagating signs on a spanning tree then using each chord cycle.
Trees and isolated vertices cause no exception.

For any nonzero block C with connected edge support, H=|C|, sigma=||C||_2 and tau=||H||_2 satisfy

    sigma<=tau, with equality iff C is switchable.          (3)

Indeed ||Cx||_2<=||H|x|||_2<=tau||x||_2 for every real x.
The column graph of the symmetric nonnegative H^tH is connected: a bipartite path gives a chain of positive off-diagonal Gram entries.
For a single column the same conclusion is immediate.
A nonnegative maximizing unit Rayleigh vector w exists by compactness and replacement by absolute values, and satisfies H^tH w=tau^2 w.
A zero coordinate would force all its neighbors to vanish by the nonnegative eigenvalue equation, and hence force w=0 by connectedness.
Thus EVERY nonnegative maximizing vector is strictly positive; this is a direct proof of the needed positivity.

When sigma=tau, a real unit right singular vector x for sigma has equality in both norm inequalities.
Consequently |x| is maximizing and every x_j is nonzero.
Every row triangle has zero squared defect, since these nonnegative defects sum to zero.
All nonzero summands C_ij x_j in each row therefore have one common sign u_i.
Set v_j=sign(x_j); then sign(C_ij)=u_i v_j on every edge, proving switchability.
Conversely row/column sign matrices are orthogonal, so a switched H has all the same singular values and complete polynomial as C.
This proves(3) for rectangular blocks and all lower multiplicities.

<a id="single-expanding-complete-classification"></a>
## Full cost classification with neutral components

Row/column permutations decompose B into nontrivial edge blocks C_j and isolated vertices.
Exactly one component C_* contains sigma_*>2; all singular values in other components are at most2.
Put tau_j=|| |C_j| ||_2.
By(2)--(3),

    m(p_abs)>=f(tau_*)>=f(sigma_*)=m(p_B),
    m(p_cover)>=2m(p_B).                                    (4)

Equality in(4) holds precisely when

    (i) C_* is switchable;
    (ii) tau_j<=2 for EVERY other edge component.            (5)

For necessity, strict monotonicity of f above2 forces tau_*=sigma_* and hence(i); all other nonnegative singular costs must vanish, giving(ii).
For sufficiency, (i) preserves every singular value of C_*, so its unique expanding pair is unchanged; (ii) makes every other absolute component neutral.
Their neutral polynomials need not agree with their original ones: equal costs do not imply complete equality there.
If the entire nonzero support is connected, equality reduces to switchability and DOES imply identical complete original/absolute polynomials, including all isolated Phi2 factors.

Thus dense sign cancellation cannot give companion/original ratio less than1 in this actual single-pair bipartite class, unlike L234's multiple-pair family.
The result applies to a Salem factor occurring once with only neutral factors whenever such a bipartite realization is given.
It does not construct a realization, bound neutral padding, or bound companion cost ABOVE by a fixed multiple of original cost.
This lower comparison therefore supplies no new Mahler gap and no statement about arbitrary non-bipartite upper-unitriangular matrices.

<a id="single-pair-next-boundary"></a>
## Remaining quantitative issue

A connected non-switchable expanding realization has a strictly more expensive companion, but no uniform margin follows from the proof.
[L299's frustrated-cycle family](../ledger/Yin_L_G0299_v1.md) already has strict original/absolute costs with both expanding roots tending to phi.
Its fixed positive-measure and growing irreducible-degree scope is not a near-one family, but excludes a universal positive ADDITIVE separation based only on connected frustration.
The next section charges the position and weight of frustrated cycles relative to actual positive singular vectors through an explicit finite resistance estimate.
Uniform control of that charge or further arithmetic restrictions on small-measure inputs remain unresolved.

The author check covers singular multiplicities, rectangular and zero padding, strict positivity and rowwise equality, every disconnected neutral component, and the difference between a lower comparison and an upper transfer.

<a id="perron-weighted-frustration-price"></a>
## Exact frustration energy and a finite paid separation

Continue with one connected non-switchable real block C whose signed norm sigma exceeds2, and H=|C|, tau=||H||_2.
Choose a strictly positive right vector w with H^tH w=tau^2w; any positive normalization is allowed.
Build a COLUMN multigraph: for every row k and distinct columns i<j with C_ki C_kj!=0, retain a separate edge e=(k,i,j) with

    a_e=|C_ki C_kj| w_i w_j>0,
    epsilon_e=sign(C_ki C_kj).

Parallel edges, including opposite signs from different rows, MUST remain separate.
The column graph is connected as above.
For x_i=w_i y_i the exact identity is

    tau^2 ||x||_2^2-||Cx||_2^2
       =sum_e a_e (y_i-epsilon_e y_j)^2 = E_w(y).           (6)

For the diagonal coefficient of x_i^2, the right side is
sum_(j!=i)(H^tH)_ij w_j/w_i=tau^2-(H^tH)_ii.
The cross coefficient is -2(C^tC)_ij, while (H^tH)_ii=(C^tC)_ii.
This proves(6) for every real x, with every parallel edge and all signs retained.
Taking the minimum Rayleigh quotient gives the exact paid norm defect

    tau^2-sigma^2=min_(y!=0) E_w(y)/sum_i w_i^2 y_i^2.      (7)

The column multigraph is sign balanced iff C is row/column switchable.
Indeed row/column switchability supplies epsilon_e=v_i v_j.
Conversely such column signs make C_ki v_i have the same sign within each row, giving the required row sign.
The spanning-tree chord argument then implies that a non-switchable C has a negative-sign cycle in this multigraph.
A length-two cycle formed by two opposite parallel edges is explicitly allowed.
Choose one such cycle Gamma, a base vertex v on it, and for every column j a simple path P_j from v to j (empty for j=v).
Define the actual weighted resistances

    R_Gamma=sum_(e in Gamma) 1/a_e,
    R_j=sum_(e in P_j) 1/a_e,
    K=sum_j w_j^2 (sqrt(R_Gamma)/2+sqrt(R_j))^2.            (8)

They are finite and K>0; no lower bound on a_e is assumed.
Signed telescoping around Gamma, whose sign product is -1, and weighted Cauchy--Schwarz give

    2|y_v|<=sum_(e in Gamma)|y_i-epsilon_e y_j|
           <=sqrt(R_Gamma E_w(y)).

Telescoping along P_j similarly yields

    |y_j|<=|y_v|+sqrt(R_j E_w(y)).

These estimates remain true when a selected path meets the cycle, because each separate energy is bounded by the complete nonnegative E_w.
After squaring the last bound and summing with weights w_j^2,

    sum_j w_j^2 y_j^2<=K E_w(y),
    tau^2-sigma^2>=1/K>0.                                 (9)

Thus(8) supplies a fully explicit finite separation certificate, with all actual Perron weights, cycle lengths and attachment paths charged.
Scaling w by a positive constant scales every a_e by its square and every resistance by its inverse square, so K is normalization invariant.
No rationality, bounded degree or uniform estimate for K is asserted.

For the single-expanding-pair full determinant of the preceding section, the complete cost difference is at least f(tau)-f(sigma).
Since f'(s)=2/sqrt(s^2-4) decreases for s>2,

    m(p_abs)-m(p_B)
       >=2(tau-sigma)/sqrt(tau^2-4)
       =2(tau^2-sigma^2)/[(tau+sigma)sqrt(tau^2-4)]
       >=1/[tau sqrt(tau^2-4) K]>0.                       (10)

Other absolute components can only add nonnegative cost, so none is discarded in this lower bound.
This remains a paid LOWER comparison; it is not an upper-cost realization theorem or a degree-independent Mahler gap.
The actual L299 family has signed and absolute norms converging to the same number greater than2, so(9) forces K to become unbounded for every choice of its negative cycle and connecting paths.
That necessary deterioration is consistent with its vanishing additive cost difference and identifies the missing quantitative control rather than suppressing it.

The additional author check covers every parallel signed edge, diagonal and cross coefficient, normalization invariance, negative two-cycles, signed telescoping, overlapping chosen paths, strict sigma>2 and the derivative direction in the complete logarithmic cost estimate.

<a id="single-pair-companion-fixed-inputs"></a>
## Exact fixed inputs and proof boundaries

| Role | Target | Scope |
| --- | --- | --- |
| Complete rectangular determinant and cost | [L191 block and spectral identity](Yin_C_G0458_v2.md#higher-degree-phi2-realization) | Full real rectangular Gram determinant, every singular value and zero/Phi2 factor, complete logarithmic spectral cost; the proof here includes the transpose case and its exact singular-value form. |
| Full signed cover and switching sufficiency | [C2 literal cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full original-times-absolute polynomial with no rank normalization; diagonal sign switching is sufficient for equality. Necessity for connected support and all quantitative estimates are proved here. |
| Multiple-pair comparison | [L234 full ratio family](../ledger/Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) | Accepted many-expanding-pair ratios tending to zero, growing original measure and repeated quadratic factors; not a counterexample under the present single-pair assumption. |
| Nonuniform-margin comparison | [L299 cycle-leaf family](../ledger/Yin_L_G0299_v1.md#unit-cycle-leaf-fixed-scope) | Connected frustrated integral family with exactly one expanding pair on each side for a>=5, both complete measures tending to positive log phi and growing positive irreducible degree; excludes an uncharged universal additive margin. |
| Motivation only | [J104 rank-ten minimum](../computations/programs/Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) | The separate finite rank-nine test motivated this question; none of its computation, coefficients or new minimum conclusion is a proof premise here. |

The complete equality classification and Perron-weighted multigraph/resistance proof are local author arguments, with all source and project comparisons restricted to the roles above.
No source-original proof audit, numerical computation, uniform arithmetic control, upper-cost realization theorem or Task completion is asserted.
