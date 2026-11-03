---
author: Yin
---

# Partial original sign flows: exact capture and the mass versus congestion bound

This physical v2 retains the complete argument of [v1](Yin_C_G0602_v1.md) developed by contributor original_law, and explicitly restricts the component upper bound A_n to be nonnegative.
The isolated reviewer identified that the empty-union premise of the old statement otherwise permitted a negative bound.
Root supplied this exact parameter-domain correction in the Statement and corresponding argument; every other mathematical statement and proof is unchanged.
The old physical version and its actual review outcome remain separate; this version's actual re-review and adoption are selected below.
Its elementary weighted path-Cauchy mechanism is reused from [C514v2](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) and [C519](Yin_C_G0519_v1.md#seed-path-load-and-mass); no new general canonical-path theorem or priority claim is made.
The present argument supplies the original sign-pair specialization, its complete finite feasibility and capture conclusions, and the explicit neutral-packing mass versus load lower bound.
The selected assessment below owns the actual re-review and adoption; ordinary author checking in the retained argument is distinct.

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta, O=Z[beta], B=1/(beta-1), S_real=beta B and the ACTUAL core D={q in O:|q_+|<B,|q_-|<S_real}.
For every integer n>=5 use ALL length-2n returned ternary words with their independent probabilities p_-=p_+=1/4,p_0=1/2 divided by the COMPLETE return probability p_(2n).
Write this law as pi_n, use K_n=(H_A+H_C)/2 with conditioning on the first and last n-2 full digits, and let S eta=-eta.
The true midpoint is Z_n=-zeta^-n sum_(j<n)eta_j zeta^j, with algebraic midpoint Y_n in D and D_n=p_(2n)/p_n^2.
For every original positive unordered nonloop edge put Q_n({u,v})=pi_n(u)K_n(u,v) and E_n(f)=sum_e Q_n(e)|f(u_e)-f(v_e)|^2.

Take ANY subprobability 0<=a_n<=pi_n satisfying a_n(S eta)=a_n(eta), with mass delta_n.
For EVERY selected word choose a positive-K_n path gamma_eta from eta to S eta at the SAME n, with length ell_eta and edge traversal count N_e.
The zero word permits an empty path; all used edge conductances are the complete original ones.
Define

    Lambda_n=max_e Q_n(e)^-1 sum_eta a_n(eta) ell_eta N_e(gamma_eta),

with zero load on unused edges and zero maximum when all paths are empty.
The sum includes each directed starting word, including its negative when selected.
For every real or complex odd f,

    sum_eta a_n(eta)|f(eta)|^2 <=(Lambda_n/4)E_n(f).

Finite path feasibility at fixed n and selected mass delta is equivalent to 0<=delta<=s_n, where s_n is the COMPLETE original mass of all self-sign communicating components.
This equivalence gives no uniform load bound.
With the actual midpoint one has

    M_n=sum_eta a_n(eta)|Z_n(eta)|^2<=Lambda_n,
    pi_n{|Z_n|<=R}>=delta_n-Lambda_n/R^2               for every R>0.

Consequently, if for EVERY n>=n0 some such family has delta_n>=delta>0 and Lambda_n<=L<infinity, then with R^2=max{1,2L/delta} and N(R)=card{q in D:|q(zeta)|<=R},

    pi_n{|Z_n|<=R}>=delta/2,
    mu<=2N(R)/delta<infinity,

where mu is the original chronological first-return mean at the ACTUAL critical radius.
No full-component odd coefficient, other-component mixing or selected-event closure is required for this implication.
The two sufficient quantitative hypotheses, partial sign-flow load and complete-component odd energy, are not asserted to imply one another.

The actual integer norm gives neutral separation greater than 1/(2sqrt(B S_real)) and

    N(R)<=(1+4sqrt(B S_real)R)^2                      for every R>=0.

Put H(x)=0 for 0<=x<=1 and H(x)=(sqrt(x)-1)^3(3sqrt(x)+1) for x>1.
Every selected path family, without any uniform path-length cap, necessarily satisfies

    Lambda_n>=H(delta_n D_n)/(96 B S_real D_n).

Along ANY sequence with D_n tending to infinity and delta_n>=delta>0, therefore

    liminf Lambda_n/D_n>=delta^2/(32 B S_real).

On the hypothetical infinite-mean branch this applies along C204's SAME common divergent subsequence.
For C554's full zero-middle event, whose actual mass is at least 1/16, any current-length flow covering that entire event obeys liminf Lambda_n/D_n>=1/(8192 B S_real) on that subsequence, or fails current-length path feasibility.
If it instead has uniformly bounded load L at EVERY sufficiently large n, it gives mu<=32N(R) for R^2=max{1,32L}.
Neither alternative is supplied as actual input here.

For ANY nonnegative real bound A_n and ANY union of self-sign complete components of mass delta_n, each having C552 odd coefficient at most A_n, the same argument also forces

    A_n>=H(delta_n D_n)/(384 B S_real D_n).

At the digit-work clock Lambda_n is multiplied by n+2 and E_n is divided by n+2, leaving all capture and mean comparisons unchanged.
Randomized paths satisfy the same statements with expected length-times-traversal loads when those expectations are finite.
No current-length positive-mass uniformly bounded flow, actual mean branch, new computation, finite-topology gap or unrestricted Lehmer conclusion is proved.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision nonnegative-component-bound

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:02 |
| status | open |
| reason | Register the corrected nonnegative component bound after the isolated review identified the empty-union quantifier defect in v1. The complete original proof is retained, with A_n>=0 explicit in both affected passages; actual re-review and adoption remain pending, and no flow construction or mean branch is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every actual quartic n>=5/full original law/positive conductance, fractional sign-symmetric selection/current-length path/empty-path convention, odd complex inequality, exact finite feasibility, all-late capture/critical mean, integer norm/packing/layer-cake constants, full zero-middle and component comparisons, work-clock and random-path scope, with all unsupplied construction and Task limits. |
| argument | [Complete author argument](#argument) | All Sections 1--4, equations (1)--(12), original-law definitions, complete finite feasibility, norm/packing/integration derivations, actual input matching and every limitation. |
| dependency | [Actual original operator and energy](Yin_C_G0170_v1.md#short-overlap-operator-and-energy) | Full-word conditional expectations at b=2, exact midpoint, complex energy at most 4 and n+2 digit-work price. |
| dependency | [Complete original capture](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Actual quartic core and pointwise midpoint bound, fixed finite-set all-late capture implies mu<=card(F)/mass at the actual critical radius. |
| dependency | [Same common null subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Only under infinite critical mean, one common subsequence with D_n tending to infinity and original midpoint atoms at most 1/D_n. |
| dependency | [Odd component definitions and coefficients](Yin_C_G0552_v2.md#odd-component-exact-theorem) | Finite sign involution, self-sign complete components and their actual odd coefficients; no all-late mass or energy premise imported. |
| dependency | [Original full zero-middle mass](Yin_C_G0554_v1.md#zero-middle-complete-probability) | Complete event mass at least 1/16 at each n>=5, including all outside representations and its full original normalizer; no sign-path membership imported. |
| support | [Existing path-Cauchy mechanism](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Standard elementary weighted path-Cauchy regrouping and true original conductance accounting, specialized here to sign pairs; no existing load bound transferred. |
| support | [Paid original fixed-hub comparison](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Reuse of the original mass versus path-load distinction; no fixed-hub mass bound is substituted for the selected word mass. |

<a id="argument"></a>

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T15:09 |
| status | proved |
| authority | Yin activated all strategies and continued the unchanged G0001 Task. |
| reason | Adopt the complete corrected partial sign-flow, finite feasibility, capture and quantitative mass-versus-load theorem through the isolated whole v2 re-review. The explicit nonnegative component bound closes the exact v1 empty-union finding, which remains preserved. No uniformly bounded actual flow, mean-branch conclusion or unrestricted Lehmer result is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Every actual quartic n>=5/full original law/positive conductance, fractional sign-symmetric selection/current-length path/empty-path convention, odd complex inequality, exact finite feasibility, all-late capture/critical mean, integer norm/packing/layer-cake constants, full zero-middle and component comparisons, work-clock and random-path scope, with all unsupplied construction and Task limits. |
| argument | [Complete author argument](#argument) | All Sections 1--4, equations (1)--(12), original-law definitions, complete finite feasibility, norm/packing/integration derivations, actual input matching and every limitation. |
| dependency | [Actual original operator and energy](Yin_C_G0170_v1.md#short-overlap-operator-and-energy) | Full-word conditional expectations at b=2, exact midpoint, complex energy at most 4 and n+2 digit-work price. |
| dependency | [Complete original capture](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Actual quartic core and pointwise midpoint bound, fixed finite-set all-late capture implies mu<=card(F)/mass at the actual critical radius. |
| dependency | [Same common null subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Only under infinite critical mean, one common subsequence with D_n tending to infinity and original midpoint atoms at most 1/D_n. |
| dependency | [Odd component definitions and coefficients](Yin_C_G0552_v2.md#odd-component-exact-theorem) | Finite sign involution, self-sign complete components and their actual odd coefficients; no all-late mass or energy premise imported. |
| dependency | [Original full zero-middle mass](Yin_C_G0554_v1.md#zero-middle-complete-probability) | Complete event mass at least 1/16 at each n>=5, including all outside representations and its full original normalizer; no sign-path membership imported. |
| support | [Existing path-Cauchy mechanism](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Standard elementary weighted path-Cauchy regrouping and true original conductance accounting, specialized here to sign pairs; no existing load bound transferred. |
| support | [Paid original fixed-hub comparison](Yin_C_G0519_v1.md#seed-path-load-and-mass) | Reuse of the original mass versus path-load distinction; no fixed-hub mass bound is substituted for the selected word mass. |
| review | [Whole isolated independent finding](../audits/reviews/Yin_R_G0805_v2.md#whole-sign-flow-v2-finding) | Entire exact current statement, complete argument and every selected input at the explicit binding scopes; actual isolated independent review and inherited source/input limits remain distinct. |

## Complete author argument

<a id="partial-sign-flow-original-law"></a>
## 1. Exact law, selected mass and path normalization

Fix P(t)=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta and O=Z[beta].
Write B=1/(beta-1), S_real=beta B and

    D={q in O: |q_+|<B, |q_-|<S_real},
    rho(q)=|q(zeta)|.

For n>=5 let Omega_n be ALL length-2n ternary words returning to zero, with complete original law pi_n from independent digit probabilities p_-=p_+=1/4, p_0=1/2 conditioned on that return.
Its normalizer is the FULL p_(2n).
Let K_n=(H_A+H_C)/2 be C170's b=2 full-word heat bath, where H_A and H_C condition on every digit in the first and last n-2 positions respectively.
Let S eta=-eta denote full word negation; this S is separate from S_real.
Write

    Z_n(eta)=-zeta^-n sum_(j<n) eta_j zeta^j,
    D_n=p_(2n)/p_n^2,
    Q_n({u,v})=pi_n(u)K_n(u,v)=pi_n(v)K_n(v,u)>0

for every unordered nonloop edge with positive original transition probability.
Every tail representation and every complete-fiber probability is retained in Q_n.
For a complex function f define

    E_n(f)=sum_e Q_n(e)|f(u_e)-f(v_e)|^2.

This equals the sum of the ordinary real Dirichlet forms of its real and imaginary parts.
C170 proves E_n(Z_n)<=4.
The algebraic midpoint Y_n=-beta^-n sum_(j<n)eta_j beta^j belongs to D and satisfies Z_n=Y_n(zeta).
C204 proves the pointwise bound pi_n{Y_n=q}<=1/D_n for every q.

Choose a sign-symmetric subprobability a_n on words satisfying

    0<=a_n(eta)<=pi_n(eta),
    a_n(S eta)=a_n(eta),
    delta_n=sum_eta a_n(eta).

Fractional selection is permitted, so a_n need not be the restriction to an event.
For every eta with a_n(eta)>0 choose a finite positive-K_n path gamma_eta from eta to S eta at this SAME current n.
An empty path is allowed when eta=S eta, which for full word negation means eta is the zero word.
Paths in an infinite incidence union that are absent at the current length do not meet this condition.
Write ell_eta for the number of nonloop edge traversals, N_e(gamma_eta) for their multiplicity and

    Lambda_n=max_e (1/Q_n(e))
        sum_eta a_n(eta) ell_eta N_e(gamma_eta).       (1)

An unused edge has load zero, and the maximum is zero if every selected path is empty.
Loops may be deleted before evaluating (1).
Every directed starting word is included in the sum, even when its negative is also selected.
This convention accounts for that double listing and fixes the factor 1/4 below.
Random path choices can also be admitted by replacing each summand by its expectation, provided that the expected length times traversal count is finite.
The deterministic version suffices for the stated conclusions.

<a id="partial-sign-flow-capture"></a>
## 2. Partial sign flow gives the needed original capture

For every odd real or complex f, f(S eta)=-f(eta), path Cauchy--Schwarz gives

    4|f(eta)|^2
       <=ell_eta sum_e N_e(gamma_eta)|f(u_e)-f(v_e)|^2.

Multiply by a_n(eta), sum over all selected words and regroup by the SAME original edge conductance.
The exact result is

    sum_eta a_n(eta)|f(eta)|^2 <=(Lambda_n/4)E_n(f).   (2)

No hypothesis says that the selected words form complete components or that every odd mode of their components has bounded energy coefficient.
The required paths do imply that the selected words lie in self-sign complete components, so their total original mass s_n satisfies s_n>=delta_n.
Conversely, at a single finite n, a path family of some finite load and selected mass delta exists exactly when 0<=delta<=s_n.
Indeed each word in a self-sign communicating component has a finite positive path to its negative, while any such path forces its component to be self-sign.
One may select pi_n restricted to those components and scale it by delta/s_n; finiteness of the state space and positivity of the used conductances give finite load.
For s_n=0 only delta=0 is possible.
This finite feasibility statement supplies no uniform upper bound on Lambda_n.

Apply (2) to the actual complex midpoint to obtain

    M_n:=sum_eta a_n(eta)|Z_n(eta)|^2<=Lambda_n.      (3)

For every R>0 this yields

    pi_n{|Z_n|<=R}>=delta_n-Lambda_n/R^2.            (4)

To justify (4), the a_n-mass with |Z_n|>R is at most M_n/R^2, and pi_n dominates a_n pointwise.
Thus a sufficient all-late hypothesis is the existence of delta>0, L<infinity and n0>=5 such that EVERY n>=n0 admits (1) with delta_n>=delta and Lambda_n<=L.
Set

    R^2=max{1,2L/delta}, N(R)=card{q in D:rho(q)<=R}.

Equation (4) gives complete original midpoint mass at least delta/2 in the SAME fixed finite set D(R), and C204 therefore gives

    mu<=2N(R)/delta<infinity.                        (5)

Here mu is the original chronological first-return mean at its actual critical radius; no replacement of that radius by beta is made.
This provides a direct partial-path target at the word level, with no endpoint-fiber transfer constant and no angular clipping loss.
It asks for paths only on a positive selected original mass.
It is an alternative sufficient construction to C552's uniform complete-component odd coefficient; no general implication in either direction between those two quantitative hypotheses is claimed.

For the particular zero-middle event E_n of C554, pi_n(E_n)>=1/16 at every n>=5.
If all its words had current-length sign paths with uniformly bounded load L when a_n=pi_n 1_(E_n), then delta=1/16, R^2=max{1,32L} and mu<=32N(R).
If only a subset of it is selected, its actually retained original mass must be supplied instead.
Setwise sign invariance and the 1/16 event bound do not supply any of these paths or their load.

At the digit-work clock, every nonloop conductance is Q_n(e)/(n+2), so Lambda_n^cost=(n+2)Lambda_n and E_n^cost(Z_n)=E_n(Z_n)/(n+2).
Their product in (2) is unchanged.
Thus (3)--(5) have the same mathematical content with the work price retained.

<a id="neutral-packing-and-load-lower-bound"></a>
## 3. An explicit original mass versus congestion lower bound

The actual quartic order gives a direct separation bound in the neutral plane.
For distinct q,r in D the algebraic integer v=q-r is nonzero, so its integer norm satisfies

    1<=|Norm(v)|=|v_+v_-| |v(zeta)|^2
       <4B S_real |v(zeta)|^2.

Consequently the neutral images of distinct core points have distance greater than

    d_0=1/(2 sqrt(B S_real)).

Their disks of radius d_0/2 are disjoint.
For points of neutral radius at most R these disks lie in the disk of radius R+d_0/2.
Comparing their ordinary Euclidean areas gives the explicit all-R bound

    N(R)<=(1+gamma R)^2, gamma=4 sqrt(B S_real).      (6)

This uses the integer norm at BOTH actual real embeddings and the conjugate neutral pair.
It does not replace O by a continuum law or a uniform distribution.
This elementary packing calculation is an explicit consequence of the existing actual-order framework; no external lattice-counting asymptotic is used.

Since a_n<=pi_n, its midpoint mass at every q is at most 1/D_n.
Therefore

    sum_(|Z_n|<=r) a_n <=N(r)/D_n
                         <=(1+gamma r)^2/D_n.       (7)

Put x=delta_n D_n.
For x>1 set t=sqrt(x)-1 and r_*=t/gamma.
The finite-sum layer-cake identity and (7) give

    M_n=integral_0^infinity 2r sum_(|Z_n|>r)a_n dr
       >=integral_0^(r_*) 2r[delta_n-(1+gamma r)^2/D_n]dr
       =[t^3(3t+4)]/[6 gamma^2 D_n].                (8)

The bracket is nonnegative on this integration interval.
At x<=1 retain the lower bound M_n>=0.
Define the continuous nonnegative function

    H(x)=0                                     if 0<=x<=1,
    H(x)=(sqrt(x)-1)^3(3sqrt(x)+1)               if x>1.

Combining (3), (6) and (8) yields the explicit unconditional finite-n restriction

    Lambda_n >= H(delta_n D_n)/(96 B S_real D_n). (9)

Thus, if selected masses stay at least a fixed delta>0 along ANY sequence with D_n tending to infinity,

    liminf Lambda_n/D_n >= delta^2/(32 B S_real). (10)

Equation (9) applies to every possible length of the selected paths.
It is a weighted-load obstruction and does not rely on bounding individual path length.
On the hypothetical infinite-mean branch, C204 supplies ONE common subsequence with D_n tending to infinity, so (10) holds for every proposed positive-mass construction along that subsequence.
In particular a family covering the entire zero-middle event, if it exists at each such current length, must obey

    liminf Lambda_n/D_n >=1/(8192 B S_real)       (11)

along that same subsequence.
If current sign connections fail, path feasibility itself fails instead.
Neither alternative establishes the actual infinite-mean branch.
This strengthens C554's bounded-length failure to a quantitative conditional obstruction for arbitrary-length paths with bounded original load.

For comparison, let A_n>=0 be real and suppose U_n is any union of self-sign COMPLETE components, of original mass delta_n, each with C552 odd coefficient at most A_n.
Apply those coefficients to both real coordinates of Z_n and sum the actual component energies to obtain

    sum_(eta in U_n) pi_n(eta)|Z_n(eta)|^2<=4A_n.

The same packing and atom argument gives

    A_n >= H(delta_n D_n)/(384 B S_real D_n).     (12)

This quantitative consequence retains every original component weight.
It does not prove that a particular selected component has such mass or determine its coefficient.

<a id="partial-sign-flow-failure-and-next-step"></a>
## 4. What is decided and what is still missing

The partial sign-flow criterion (1)--(5), finite feasibility characterization and quantitative lower bounds (9)--(12) are complete author derivations from the stated fixed inputs.
They introduce no new numerical run or native program.
The author checked the unordered-conductance convention, the directed starting-word sum, the factor 1/4, complex-coordinate energy, the empty zero path, fractional selection, current-length membership, exact two-real-place norm, disk packing and layer-cake constants.
This is ordinary contributor checking, not independent review or fixed Claim acceptance.

The change in the mathematical target is precise: it is enough to construct a weighted sign flow on a positive original mass of words, rather than prove a uniform odd Poincare coefficient for every odd function on complete selected components.
The two quantitative hypotheses are not asserted to be logically ordered.
The necessary tradeoff (9) prevents a proposed flow from hiding its cost in rare tail representations or in unspecified long paths.

No positive-mass current-length sign family with uniformly bounded Lambda_n has been constructed.
No current component-membership classification is inferred from C551/C553's mass or degree bounds, and the previously excluded asymptotically tight state-independent overlap schedules stay excluded at their original global-gap scope.
The next useful step is an explicit current-length flow, or an exact failure of such a proposed flow, with full Q_n and retained mass computed together.
An enlarged unweighted connectivity scan would not supply that result.
The actual quartic critical mean and unrestricted Lehmer contract remain unresolved.
