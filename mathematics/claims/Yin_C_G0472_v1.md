---
author: Yin
---

# Scale-spread integer capacities and failure of the stronger fractional lcm norm

This retains the complete necessary mathematical argument from [the entire original G396 bounded failed-route account](../ledger/Yin_L_G0396_v1.md).
Original contribution and dated review accounts are retained in the [complete later comparison](../audits/reviews/Yin_R_G0695_v1.md#l396-and-r455) and the [exact original author SELF](../audits/reviews/Yin_R_G0343_v1.md#scale-loss-original-author-check-finding).
This maintenance creates no research authority.

## Statement

Fix0<epsilon<1, beta=2/(2+epsilon) and r=1-beta/2.
For each integer m>=2 put B=2^(3m), and in each band2^j<=a<2^(j+1),2m+1<=j<=3m, scan in increasing order assigning full integer phi(a) until reaching mass B, truncate only the last positive weight to the exact remaining integer, and retain no zero weights.
This defines finite distinct positive labels with integer1<=w_a<=phi(a), total W=mB and integer X=2B-1<=W.
For the C101 band definition, L_eff=(sum_j(W_j/W)^r)^(2/beta)=m, while H_X=max_(1<=n<=X)sum_(a|n)w_a<=X and H_X/W<2/m.
Its actual ordered repeated-label triple density delta_m=T_X/W^3 is positive and obeys delta_m<=min(1,(4/[c_(1/2)m])^(4/9)) tending to0, where c_(1/2)>0 is the actual finite C101 constant at its existing GW21 statement/applicability scope.
Thus capacities and the physical condition X<=W alone do not uniformly bound L_eff; this construction supplies no fixed-positive-triple-density counterexample.

Fix0<s<1, t=2-s and q_s=2/t.
There is no finite universal A_s such that every nonnegative finite-support f satisfies sum_(a,b)phi(a)phi(b)f(a)f(b)/lcm(a,b)^s <= A_s[sum_a phi(a)f(a)^(q_s)]^(2/q_s).
Failure holds even for0<=f<=1 and for functions f(a)=w_a/phi(a) coming from finite positive INTEGER capacities1<=w_a<=phi(a).
For any odd squarefree Q whose primes are at least max(3,8/s), let f_Q(a)=a^(-t) on a|Q, zero otherwise.
The exact finite ratio is R_s(Q)=product_(p|Q){[1+2(p-1)/p^2+(p-1)^2/p^(4-s)]/[1+(p-1)/p^2]^t}, and log of each local ratio is at least s/(2p).
Consequently R_s(Q) is unbounded over finite such prime products for every FIXED s.
For v=2^k, c=phi(v)=2^(k-1), the weights w_(va)=floor(c phi(a)f_Q(a)) are positive legal integer capacities for sufficiently large finite k, and their strong-norm ratio tends to2^(-s)R_s(Q) at each fixed finite Q.
Choosing finite Q first and then finite k therefore gives an actual integer-capacity witness against each proposed A_s.
Both ordered cross patterns and diagonal terms, floor positivity and the exact2^(-s) cost are retained.

The false strong norm would imply a weak L1 estimate E_s(w)<=C_s W^(2-s), but its failure does not refute that different weak estimate.
For the original law and integer X>=1 the residual-bucket proof gives T_X/W^3<=(XH_X/W)^s E_s(w)/W^2; hence a valid weak bound implies H_X>=(delta/C_s)^(1/s)W^2/X whenever T_X>=delta W^3.
This is the exact conditional deduction already present in the retained account, not a new proof of a weak estimate from the false strong norm.
The later current C142v2 separately owns the proved general weak estimate and positive-triple-density capture; the original2026-10-13 account did not resolve it.
Neither finite counterexample asserts good-prime Frobenius multiplicities, an actual irreducible polynomial lift, full norm or Mahler costs, a near-one family, automatic original-root positive density or an unrestricted gap.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:40 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact scale-mass and capture theorem](Yin_C_G0101_v1.md#statement) | Actual real weights/physical integer X, all band masses, L_eff and c_(1/2), ordered repeats and finite domains; only the equal-band density decay uses this accepted theorem. |
| dependency | [Complete residual-bucket argument](Yin_C_G0101_v1.md#nonlinear-triple-capture-theorem) | Every residual class divides one integer Lr<=X, each has mass<=H_X, zero links beyond X and exact original-law normalization. |
| dependency | [Elementary totient capacity](Yin_C_G0094_v1.md#oriented-row-bound-failure) | Only its full phi(a)>=sqrt(a/2) prime-power proof, including the unique2-power loss and n1 case; no averaged or oriented-row conjecture imported. |
| dependency | [Retained prime-reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only the complete elementary finite-Euler-product/harmonic-series proof and finite-prime exclusion at existing DLMF attribution scope. |
| dependency | [Accepted fixed-epsilon source interface](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Published Theorem1.1/setup statement/applicability as inherited through C101 only; no complete source proof or source-chain audit and no numerical c_(1/2). |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T22:42 |
| status | proved |
| reason | Adopt the actual complete whole SELF inspection of both exact finite integer-capacity negative theorems, all fixed-s finite-factor/floor-transfer proofs and every source/density/actual-input boundary. Preserve original R343 whole UNKNOWN and listed author SELF, actual historical weak-gate wording and the separate later C142v2 theorem; no global weak counterexample, new source audit or Task/E continuation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0101_v1.md#statement) | Actual real weights/physical integer X, all band masses, L_eff and c_(1/2), ordered repeats and finite domains; only the equal-band density decay uses this accepted theorem. |
| dependency | [Exact dependency](Yin_C_G0101_v1.md#nonlinear-triple-capture-theorem) | Every residual class divides one integer Lr<=X, each has mass<=H_X, zero links beyond X and exact original-law normalization. |
| dependency | [Exact dependency](Yin_C_G0094_v1.md#oriented-row-bound-failure) | Only its full phi(a)>=sqrt(a/2) prime-power proof, including the unique2-power loss and n1 case; no averaged or oriented-row conjecture imported. |
| dependency | [Exact dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Only the complete elementary finite-Euler-product/harmonic-series proof and finite-prime exclusion at existing DLMF attribution scope. |
| dependency | [Exact dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Published Theorem1.1/setup statement/applicability as inherited through C101 only; no complete source proof or source-chain audit and no numerical c_(1/2). |
| review | [Exact review](../audits/reviews/Yin_R_G0680_v1.md#complete-scale-loss-whole-self-finding) | Entire actual C472 Statement and Argument, all original equations1--11, band/capture/density and strong-norm/integer-transfer proofs, conditional consequence and precise old/current source/date limits. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:52 |
| status | proved |
| reason | Adopt the actual new isolated whole finding after reading the complete R695 reconstruction and its real initial/post-comparison/publication sequence. Preserve the entire original UNKNOWN arrangement, original author SELF, prior current whole SELF and all fixed positive/negative mathematics, source occurrences, true dates and unrestricted boundaries. This is a new current review adoption, not a historical isolation certificate or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0101_v1.md#statement) | Actual real weights/physical integer X, all band masses, L_eff and c_(1/2), ordered repeats and finite domains; only the equal-band density decay uses this accepted theorem. |
| dependency | [Exact dependency](Yin_C_G0101_v1.md#nonlinear-triple-capture-theorem) | Every residual class divides one integer Lr<=X, each has mass<=H_X, zero links beyond X and exact original-law normalization. |
| dependency | [Exact dependency](Yin_C_G0094_v1.md#oriented-row-bound-failure) | Only its full phi(a)>=sqrt(a/2) prime-power proof, including the unique2-power loss and n1 case; no averaged or oriented-row conjecture imported. |
| dependency | [Exact dependency](Yin_C_G0220_v1.md#discriminant-divergence) | Only the complete elementary finite-Euler-product/harmonic-series proof and finite-prime exclusion at existing DLMF attribution scope. |
| dependency | [Exact dependency](../audits/literature/GW21/Yin_U001.md#gw21-u001) | Published Theorem1.1/setup statement/applicability as inherited through C101 only; no complete source proof or source-chain audit and no numerical c_(1/2). |
| review | [Exact review](../audits/reviews/Yin_R_G0695_v1.md#isolated-scale-loss-whole-finding) | Entire actual C472 Statement and Argument, all original equations1--11, band/capture/density and strong-norm/integer-transfer proofs, conditional consequence and precise old/current source/date limits. |

## Complete retained argument

Current comparison: [C142v2](Yin_C_G0142_v2.md#statement) is the later adopted general weak-moment and original-window positive-triple-density theorem.
Every then-open weak-moment sentence in the original account below is historical at2026-10-13; the two fully proved negative results do not conflict with that later theorem.

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

Date: 2026-10-13T05:20.
Human author Yin.
Delegated direct_triple author develops this G0001 account.
The preceding whole D24 has an independent original-argument review, R453; its fixed wrapper is being organized separately and no prospective wrapper acceptance is assumed.

<a id="scale-loss-removal-question"></a>
## Exact question

For fixed delta,C>0 and every finite integer capacity array 1<=w_a<=phi(a), W=sum w_a, X<=CW and ordered repeated-label T_X=sum_(lcm(a,b,c)<=X)w_a w_b w_c>=delta W^3, prove H_X=max_(1<=n<=X)sum_(a|n)w_a>=c(delta,C)W, or construct a genuine fixed-positive-density counterfamily.
The prior weighted-band argument gives H_X>=c_epsilon delta^(2+epsilon/2)W^2/(X L_eff) with L_eff<=1+floor(log_2X), and positive linear capture if L_eff is bounded.
This draft seeks to remove that assumption or prove a new informative inverse statement, not repeat it as an open gate.

The universal linear short-pair bound is false by C96, and the direct LINEAR-in-density estimate is false by C98.
C99's full squarefree threshold-downset theorem shows that the prior actual moment-family controls have vanishing triple density; they are not fixed-positive-density counterexamples.
Actual use always retains original degree, complete groups, good prime, every local depth and full original norm.
No new native program has started.

<a id="scale-loss-removal-starting-inputs"></a>
## Starting reuse

The exact prior weighted two-band proof and finite level-set transfer are retained in [C101's complete original author artifact](Yin_C_G0101_v1.md#nonlinear-triple-weighted-two-band), with [GW21-U001](../audits/literature/GW21/Yin_U001.md#gw21-u001) as its accepted published-source input and R453 as independent original-whole evidence.
The C91 residual-bucket mechanism, C96/C98 negative controls, and the newly adopted [C99](Yin_C_G0099_v1.md#statement) are fixed inputs at their actual scopes.
The contemplated subcritical fractional moment bound was only an unproved idea in the prior artifact; this draft may investigate it without assuming it.
The original starting reference was to the then-live D24; after complete preservation in C101, this locator was rebased without changing the cited argument.

## Continuing status

New author exploration.
No no-loss theorem, useful counterexample or independent review is asserted.

<a id="scale-loss-removal-search-and-disposition"></a>
## Bounded round disposition and search

The human subsequently instructed the team to finish only this already-started exploration round, organize the drafts and pause.
The present author has bounded this inquiry accordingly.
No unrestricted fixed-positive-density capture theorem or counterexample was obtained.
Two exact failed-shortcut findings below are useful for continuation: the physical constraint X<=W does not itself bound the order-scale factor, and a tempting stronger weighted kernel estimate is false even after transfer to INTEGER totient capacities.
Neither finding refutes the original density question.

The source/reuse screen checked the preceding C101 argument and its precise unproved fractional-moment suggestion, C99's actual full-squarefree result, existing local fractional-lcm/strong-kernel material and a bounded web search for weighted gcd/lcm norm inequalities.
The exact sought estimate was not located in that bounded screen.
No new external theorem, source acceptance, novelty claim or formal-code inspection results.
The elementary prime-reciprocal divergence is reused from [L17](Yin_C_G0220_v1.md#discriminant-divergence), already read in the preceding round with its checked DLMF attribution.
The two finite constructions below are directly supplied, not inferred from a search failure.

<a id="linear-window-does-not-bound-scale-mass"></a>
## 1. Linear windows and exact integer capacities do not bound L_eff

For each integer m>=2, set B=2^(3m).
Use the m disjoint integer bands

    I_k={a in Z:2^k<=a<2^(k+1)}, 2m+1<=k<=3m.

Each band has sufficient FULL totient capacity to carry exactly B units of integer weight.
Indeed the elementary bound phi(a)>=sqrt(a/2), already proved in [C94](Yin_C_G0094_v1.md#oriented-row-bound-failure), gives phi(a)>=2^m on these bands.
Each contains2^k>=2^(2m+1) integers, so its total capacity is at least2^(3m+1)=2B.

Define the weights without any optimizer: scan each band in increasing integer order, assign the current number its full phi(a) until reaching the first one where that would exceed total B, assign only the remaining positive integer there, and assign zero to later numbers.
If the total reaches B exactly at an endpoint, stop there.
Retain only the positive-weight numbers.
This finite greedy prescription gives exact integer weights1<=w_a<=phi(a) and total B in EACH of the m bands.

For their union set

    W=mB, X=2^(3m+1)-1=2B-1.                         (1)

All selected orders are<=X, and X<=W since m>=2.
For every epsilon in(0,1), the exact C101 band-mass formula, with beta=2/(2+epsilon) and r=1-beta/2, gives

    L_eff=[m*(1/m)^r]^(2/beta)=m ->infinity.          (2)

This is an actual INTEGER arithmetic capacity construction at a window X<=W, not a collection of arbitrary abstract graph weights.
It disproves the proposed inference that the original linear-window condition and capacities alone control L_eff.

Its root-capture peak is small as well: for each n<=X,

    h(n)<=sum_(a|n)phi(a)=n<=X,
    H_X/W<2/m ->0.                                   (3)

But it is NOT a fixed-positive-density counterexample.
Let delta_m=T_X/W^3 be its actual ordered, repeated-label triple density; it is positive because at least one selected order contributes its repeated diagonal triple.
The fixed epsilon=1/2 C101 inequality applies to these exact weights and L_eff=m, and gives

    c_(1/2)*delta_m^(9/4)*W^2/(Xm)<=H_X<=X.

Consequently

    0<delta_m<=min(1,(4/[c_(1/2)*m])^(4/9)) ->0.      (4)

The constant is exactly C101's positive finite source-dependent c_(1/2), not a computed numerical value.
This use keeps GW21's original statement/applicability scope through C101.
The construction supplies no actual polynomial lift and no local valuation-depth or Mahler-measure assertion.
Those are unnecessary for its precise negative statement about a proposed capacity-only scale inference.
The density-to-scale/capture question must genuinely USE the positive density hypothesis; it cannot be removed merely by invoking X<=CW.

<a id="subcritical-capacity-moment-and-failed-strong-form"></a>
## 2. The desired weaker fractional moment and a false stronger form

For0<s<1 define the positive finite lcm kernel energy

    E_s(w)=sum_(a,b) w_a*w_b/lcm(a,b)^s,
    W=sum_a w_a.

One contemplated route is the uniform bound

    E_s(w)<=C_s W^(2-s) for1<=w_a<=phi(a),            (5)

with C_s depending only on s and all finite integer-capacity arrays allowed.
It remains UNPROVED and UNREFUTED in this round.
The following stronger estimate is tempting because it would imply(5), but is FALSE.

Put t=2-s in(1,2), q_s=2/t in(1,2), and use the totient measure mu(a)=phi(a).
For nonnegative finitely supported functions f on the positive integers, the proposed strong form is

    sum_(a,b) phi(a)phi(b) f(a)f(b)/lcm(a,b)^s
        <=A_s [sum_a phi(a) f(a)^(q_s)]^(2/q_s),      (6)

where A_s would depend only on s.
There is NO such finite A_s.
This remains false even when0<=f<=1, and remains false on functions f(a)=w_a/phi(a) arising from positive INTEGER totient-capacity arrays after an explicit dilation below.

Why(6) would have sufficed must be distinguished from its actual truth.
For f=w/phi in[0,1], f^(q_s)<=f, and2/q_s=t=2-s.
If(6) were true, its right side would be at most A_s W^(2-s), giving(5).
The converse is not claimed: (5) has the generally larger L1-based right side.
A counterexample to(6) therefore does not automatically contradict(5).

<a id="strong-kernel-finite-product-counterexample"></a>
## 3. Complete finite counterexample to the strong form

Fix any0<s<1 and t=2-s.
Let Q be squarefree with all prime factors at least max(3,8/s).
On its finite divisor set put

    f_Q(a)=a^(-t) if a divides Q, and0 otherwise.

All values lie in[0,1].
Since t*q_s=2, the q_s-norm power has the exact finite product

    sum_a phi(a) f_Q(a)^(q_s)
       =sum_(a|Q)phi(a)/a^2
       =product_(p|Q)(1+(p-1)/p^2).                  (7)

The ordered energy in(6) also factors.
At one prime the four membership patterns in(a,b) contribute

    1,
    (p-1)/p^(t+s), (p-1)/p^(t+s),
    (p-1)^2/p^(2t+s).

As t+s=2 and2t+s=4-s, their sum is

    1+2(p-1)/p^2+(p-1)^2/p^(4-s).

Thus the ratio of the actual left side of(6) to its proposed norm factor WITHOUT A_s equals

    R_s(Q)=product_(p|Q)
      [1+2(p-1)/p^2+(p-1)^2/p^(4-s)]
            /[1+(p-1)/p^2]^t.                       (8)

All four patterns and both orientations are included; no distinct-pair convention or limiting Euler product is used to obtain this finite identity.

For a local factor, put x=2/p-2/p^2>=0.
The elementary inequalities log(1+x)>=x-x^2/2 and log(1+y)<=y for y>=0 give

    log(numerator)>=log(1+x)>=2/p-4/p^2,
    log(denominator)<=t/p,
    log(local ratio)>=s/p-4/p^2>=s/(2p).              (9)

The last inequality uses p>=8/s.
Let Q range through successive products of primes exceeding that fixed cutoff.
The sum of their reciprocals diverges by L17, even after the finite exclusion.
Equations(8)--(9) imply R_s(Q) tends to infinity.
Hence for every proposed finite A_s a FINITE such Q violates(6).
The same proof works for every fixed s in(0,1); the cutoff and rate are allowed to depend on that fixed s.
It does not make s tend to zero inside a uniform constant.

The real weights phi(a)f_Q(a) in this first construction can be below1; that fact must not be hidden.
The next paragraph removes precisely that objection to the stronger form, without upgrading the weaker conclusion.

<a id="strong-kernel-integer-capacity-transfer"></a>
## 4. Transfer of the strong-form failure to integer capacities

Fix one of the preceding ODD squarefree Q.
For integer k>=1 put v=2^k, c=phi(v)=2^(k-1).
Since v is coprime to Q, phi(va)=c*phi(a) for a|Q.
For all sufficiently large k define

    w_(va)=floor(c*phi(a)*f_Q(a)), a|Q,
    F_k(va)=w_(va)/phi(va),

and set all other weights/functions to zero.
Because Q has finitely many divisors and every f_Q(a)>0 there, all these floors are positive once k is large enough.
They satisfy the exact integer capacity condition

    1<=w_(va)<=phi(va).

For each of those finitely many a, F_k(va) tends to f_Q(a).
Also lcm(va,vb)=v*lcm(a,b).
Therefore the ratio in(6), now evaluated at F_k, is

    [c^2/v^s]/c^t times
      {sum_(a,b|Q)phi(a)phi(b) F_k(va)F_k(vb)/lcm(a,b)^s}
        /{sum_(a|Q)phi(a)F_k(va)^(q_s)}^t
      ->2^(-s) R_s(Q),                               (10)

because2-t=s and c/v=1/2.
The denominator limit is positive; all limiting operations involve only the fixed finite divisor set.
Given any finite A_s, first choose finite Q with R_s(Q)>2^(s+1)A_s, then choose finite k so that the ratio in(10) exceeds A_s.
This proves failure of(6) on actual positive integer-capacity arrays, without rational approximations, a density limit, prime-progression theorem or an unspecified polynomial realization.

The transfer is a statement about integer capacities only.
No good-prime Frobenius-orbit multiplicity constraint, actual irreducible unit, positive normalized triple density, full norm/depth or near-one measure is asserted for these arrays.
The scaled support need not be a divisor downset.
Those restrictions are unnecessary to refute(6), whose proposed domain was all capacity arrays.

<a id="scale-loss-removal-consequence-and-handoff"></a>
## What has and has not changed

This bounded inquiry did NOT remove C101's scale factor and did NOT produce a fixed-positive-density obstruction.
It supplies two fully reasoned failed-shortcut checks to preserve as exploration: even X<=W permits L_eff tending to infinity for legal integer capacities, and the proposed strong-form weighted kernel estimate fails on legal integer capacities.
The first construction itself has delta tending to zero by the already proved C101 bound; the second construction supplies no fixed-positive delta at all.
Neither is a counterexample to G0001 or to the target positive-density implication.

The weaker fractional moment(5) remains a possible route.
For clarity, its exact sufficient consequence follows from the OLD residual inequality, not from any asserted new proof of(5): for a pair with L=lcm(a,b), U_X(a,b)/W<=min(1,XH_X/(WL)).
Since min(1,z)<=z^s for z>=0 and0<s<1,

    delta<=T_X/W^3
       <=(XH_X/W)^s * E_s(w)/W^2.

IF(5) held, this would give

    H_X>=(delta/C_s)^(1/s)*W^2/X.                    (11)

The step from(5) to(11) is elementary and already the reason for considering that moment in C101; it is recorded to identify the unresolved scope, not as a newly solved reduction.
The present negative result says one cannot justify(5) by the FALSE stronger norm inequality(6).
A successful continuation must establish the actual L1/capacity form directly, prove scale/core localization using the fixed positive density, or find a counterfamily that truly retains that density.
Repeating a generic strong norm interpolation argument or ignoring the density of the equal-band construction would be invalid.

The finite constructions use only elementary phi capacities, squarefree factorization, exact floors and L17 prime divergence.
C101 is used solely to verify that the explicit equal-band example's actual density vanishes; its GW21 published-statement dependence and proof-inspection limits remain unchanged.
C99 is a comparison marking why earlier moment-family examples also have zero density, not a premise in either new finite counterexample.
No new external source registration, native computation, source-proof audit, formal assistant, shared record edit or Git operation occurred.

The author checked the exact m-band count and endpoints, the capacity lower bound, greedy final partial weight, X<=W, every normalization in L_eff and(4), all four local patterns in(8), logarithm directions and cutoff, q_s/t relations, the real-to-integer objection and finite dilation repair, positivity of floors and denominator limits, the factor2^(-s), and the logical separation between(5),(6),(11) and the main positive-density gate.
These are AUTHOR checks only.
A noncontributing whole review is pending; no Claim extraction or acceptance is sought automatically for this bounded failed-route account.

<a id="scale-loss-removal-entire-author-freeze"></a>
## Entire bounded-round author freeze

2026-10-13T05:29.
ENTIRE artifact frozen for the assigned noncontributing whole review: original question and starting/search chronology, equations(1)--(11), both finite failed-shortcut constructions, exact integer-capacity transfer, source/contribution scope, the unproved weaker fractional-moment gate and the explicit absence of a fixed-positive-density or unrestricted G0001 resolution.
Scoped material validation passed.
All former D24 consumers here now point to its preserved C101 anchors.
No further exploration round will be started; root will organize the completed evidence and pause under the human's instruction.
This freeze is author completion of a bounded exploratory account, not independent acceptance or Task completion.
