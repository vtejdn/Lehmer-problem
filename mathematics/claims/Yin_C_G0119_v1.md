---
author: Yin
---
# Canonical prime-power stripping and large balanced remainders

Date: 2026-10-15.
Human author Yin.
Continuing G0001 within the same root-owned execution; g_bridge_audit authors this round.
Root contributes the extension from a dominant prime to the minimal dominant power q^e>sqrt(Y), using distinct-prime coprimality.
That direct extension alone is not treated as grounds for a duplicate new Claim.
Root did not supply the subsequent whole-tree/terminal-remainder argument being investigated here.

<a id="power-stripping-question"></a>
## Question and bounded reuse

Can one use the omitted prime-power-smooth remainders in the complete stripping tree, rather than select a path with an assumed retention budget, to obtain a positive actual structural class or an unconditional necessary remainder escape?
Preserve complete original labels, conditional/real versus original weights, physical time and all auxiliary-degree costs.

The local screen covered dominant prime-power/square-root partitions and exact lcm partition language in G Claims, ledgers and current drafts; no retained exact whole-tree terminal-remainder statement was found within that bounded screen.
Read [C118's complete partition invariant and transport](Yin_C_G0118_v1.md#argument), [L395's common/relative-core transport and failed cover](../ledger/Yin_L_G0395_v1.md#single-core-exact-window), and the already accepted C101/C114/C116 relevant interfaces.
C118 was initially fixed awaiting whole review; its actual selector now points to [the whole-reviewed decision](Yin_C_G0118_v1.md#decision-whole-reviewed-2026-10-15).
Those sufficient inputs cover the direct prime-power substitution and elementary divisibility needed here; the new work is a finite combinatorial tree argument, with no new recognized source theorem invoked.
A broad registry query was truncated and supplies no absence/novelty evidence.
No code or J is used.

<a id="power-stripping-incremental-argument"></a>
## Incremental argument

Develop and retain the exact canonical tree, finite count and original-time bounds here.
The claim that positive original density automatically gives a paid single path remains unproved and is not used.

<a id="canonical-power-stripping-tree"></a>
## 1. The entire canonical prime-power tree

Let S be a finite set of DISTINCT positive integer labels o with arbitrary positive REAL weights w_o, W=sum w_o>0.
Unlike the earlier capacity estimates, the theorem below requires NO upper bound w_o<=phi(o).
Fix an integer X>=1 and let T_X be the sum of w_a w_b w_c over all ordered triples with lcm(a,b,c)<=X, including all repetitions.
Put delta_X=T_X/W^3 and H_Z=max_(integer1<=n<=Z)sum_(o|n)w_o for integer Z>=1.

Only eligible labels o<=X enter the tree; ineligible labels retain their weights in W and contribute no compatible triple.
If no label is eligible, the tree is empty, T_X=rho_N=0 and the later inequalities are immediate.
Otherwise start at core G=1 with window Y=X and quotient labels b=o.
At any occupied node with core G, all its original labels have unique quotient b=o/G, and Y=floor(X/G)>=1.
For each prime q let

    g_q(Y)=q^e,  e=min{integer e>=1: q^e>sqrt(Y)}.

Only q for which this power divides an occurring quotient need be considered.
Put a quotient in the q-child if g_q(Y)|b.
Two distinct such powers are coprime and their product exceeds Y, so no eligible b<=Y belongs to two children.
All remaining labels STOP at the current node.
A stopped quotient b satisfies

    q^(v_q(b))<=sqrt(Y) for every prime q|b;            (1)

b=1 satisfies this vacuously.
At the q-child replace G by G g_q(Y), b by b/g_q(Y), and Y by floor(Y/g_q(Y))=floor(X/(G g_q(Y))).
The updated window is strictly below sqrt(Y), and eligibility is preserved.
Every step divides an actual label by an integer at least2 and leaves a nonempty integer time range.
Thus the finite construction terminates; each eligible original label has exactly one stopping node and one terminal remainder r_X(o).
Its original weight w_o is NEVER changed during this whole-tree proof.

At Y=1 the sole possible quotient is1 and stops.
A prime power exactly equal to sqrt(Y) does not trigger its own cell; the next strictly larger power must actually divide b.
In particular q^2 at Y=q^2 now lies in the q^2-child (the minimal power STRICTLY exceeding q), so the direct extension handles C118's exact q^2 boundary.
It does not remove the residual case(1).

This first section is the direct root-proposed prime-power extension.
If one chose a single child, L395's phi(gb)<=g phi(b) would still give the correctly scaled real capacity w/g.
The remaining proof keeps the ENTIRE tree and actual weights instead; it uses no such capacity estimate or assumed retention product.

<a id="compatible-stopping-chain"></a>
<a id="argument"></a>
## 2. Compatible stopping nodes lie on one chain

Consider two original labels whose paths split at distinct q- and r-children of a node with core G and window Y=floor(X/G).
Their original lcm is divisible by G g_q(Y)g_r(Y).
Since the integer g_q(Y)g_r(Y)>Y, it is at least Y+1, so

    lcm(o,o')>=G g_q(Y)g_r(Y)>=G(Y+1)>X.              (2)

The final strict inequality pays the floor exactly.
Therefore labels compatible at the ORIGINAL window X cannot lie in different child subtrees of any node.
Their stopping nodes must be comparable in the ancestor order.
In a compatible triple the three stopping nodes are consequently on a single chain, possibly with ties.
No claim that pair overlap implies a common prime for three labels is used; this is an exact separation by the prime-power cells.

Fix an integer N>=1 and put L_N=lcm(1,2,...,N), with L_1=1.
Call an eligible label SMALL if its terminal remainder r_X(o)<=N, and LARGE otherwise.
Let a compatible triple consist of small labels, and let v be a deepest stopping node of that triple, with core G_v.
For each of the three labels, its stopping core G_i divides G_v because its node is an ancestor of v.
Its terminal remainder r_i divides L_N.
Thus

    o_i=G_i r_i divides L_N G_v,
    1<=L_N G_v<=L_N X.                               (3)

The bound G_v<=X follows from its nonempty eligible label set.
This is ONE physical return time for the triple.
Large common cores are retained; no quotient time is substituted for an original time.

For a fixed small original label c, let v(c) be its stopping node.
Every small label whose stopping node is an ancestor of v(c), including v(c) itself, divides n_c=L_N G_v(c) by the same argument.
The TOTAL ORIGINAL mass of all these labels is therefore at most H_(L_N X).
Every compatible ordered small triple has at least one coordinate at a deepest node; taking the union of the three possible coordinate positions and summing first over that label proves

    T_small(X) <= 3 H_(L_N X)^2 W_small
                 <=3 H_(L_N X)^2 W.                  (4)

Ties only cause overcounting in this upper bound; repeated coordinates are fully retained.
The factor3 is paid explicitly.
The proof neither selects one triple as representative of the entire mass nor assumes one common time serves all deepest nodes.
The single global finite maximum H_(L_N X) bounds every n_c, and a time attaining that maximum supplies the eventual capture certificate.

<a id="terminal-remainder-capture-statement"></a>
<a id="statement"></a>
## 3. Finite remainder/capture inequality with all original mass

Let rho_N=(1/W)sum_(eligible o with r_X(o)>N)w_o.
Ineligible labels count in W but in neither small nor large eligible set.
Removing the large eligible labels can delete at most[1-(1-rho_N)^3]W^3 ordered triples.
Every remaining compatible triple is small, since ineligible labels never occur in one.
Consequently(4) gives the fully finite inequality

    delta_X <= 1-(1-rho_N)^3
                    +3[H_(L_N X)/W]^2.               (5)

In particular if delta_X>=delta>0 and rho_N<=r<1 satisfy

    lambda:=delta-1+(1-r)^3>0,

then ONE integer n<=L_N X captures at least sqrt(lambda/3)W original weight.
If EVERY eligible terminal remainder is at most N, one may take r=0 and lambda=delta.
More generally a small-remainder fraction at least p supplies lambda=delta-1+p^3 whenever positive; no assertion that an arbitrary positive small fraction suffices is made.

The equivalent necessary lower bound is

    rho_N >= max(0,1-[1-delta_X
                          +3(H_(L_N X)/W)^2]^(1/3)). (6)

The cube root has a nonnegative argument because0<=delta_X<=1.
The theorem holds for every finite weighted array and every N>=1, regardless of phi capacities, factor-support size, tree depth, or the retention on individual paths.
Its new cost is the EXPLICIT physical time multiplier L_N<=N!, fixed only when N is fixed.
No n<=X conclusion is claimed.

<a id="balanced-remainder-actual-norm"></a>
## 4. Actual original polynomial transfer and remainder escape

Let P be ACTUAL monic irreducible nontorsion in Z[t], with constant coefficient+/-1 and original degree d.
Let ell be a good prime not dividing disc(P).
Select COMPLETE occurring residue-order groups with full original-root counts w_o and W>=gamma d,0<gamma<=1.
Assume an integer1<=X<=Cd has delta_X>=delta>0, with fixed C,gamma,delta.
Build the tree on these exact original orders; all intermediate quotients are bookkeeping of divisibility, NOT new polynomial root groups.
The combinatorial theorem even allows larger real weights, so no extra totient-capacity import is needed.

If fixed N and r give the positive lambda of §3, choose a time attaining the relevant finite maximum.
Then the FULL original signed norm and local floor satisfy

    D_n=Res(P,t^n-1)=Norm_(Q(alpha)/Q)(alpha^n-1),
    log|D_n|>=A_ell(n)=v_ell(|D_n|)log ell
                     >=gamma sqrt(lambda/3)d log ell,
    1<=n<=L_N X<=L_N C d.                            (7)

All original roots and unselected or deeper/exceptional contributions stay on the left, using the accepted [C256 good-prime floor](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail).
Income from different n_c in §2 is NOT summed; their use only bounds H, which is attained at one n.
Although every stripped core is prime to ell, L_N may be divisible by ell; the same floor remains valid with all resulting deeper contributions retained.
The auxiliary t^n-1 has full degree at most L_N C d, coefficient content1 and squared norm2.
[L168's accepted finite original-norm criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) therefore yields strict m(P)>m0(L_N C,eta)>0 with

    eta=gamma sqrt(lambda/3)log2>0.

The extra time/degree cost cannot be suppressed or treated as uniform when N grows.

For the near-one implication define the ORIGINAL budget U_D(P)=max_(1<=n<=floor(Dd))log|D_n|/d for any fixed D>0 with a nonempty range.
[L168's full original-norm/degree-escape proof](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) supplies U_D(P)->0 uniformly along hypothetical actual near-one nontorsion units, preserving its degree-drop/finite-degree and accepted source limits.
The same local floor gives

    H_(L_N X)/W <= U_(L_N C)(P)/(gamma log ell).

Thus(5) gives the exact actual finite obstruction

    delta_X<=1-(1-rho_N)^3
             +3[U_(L_N C)(P)/(gamma log ell)]^2.      (8)

For EVERY FIXED N, any hypothetical near-one sequence with the stated original coverage must therefore satisfy

    liminf rho_N >= e_delta:=1-(1-delta)^(1/3)>0.      (9)

This is positive original-root mass, not a model-weight or changed-law conclusion.
Every counted label has a terminal quotient r_X(o)>N whose full prime-power factors obey(1) at its own stopping window Y=floor(X/G).
In particular those quotients cannot remain in a fixed finite set.
Their stopping windows exceed N, and the large terminal quotient forces Y>=r_X(o)>N.
The selected labels can have DIFFERENT cores G and stopping windows; no common core or positive conditional triple density is inferred.
When delta=1, all selected original mass escapes every fixed terminal-remainder threshold.
For0<delta<1 only the stated positive fraction is proved.

The mean terminal remainder, setting it to0 on ineligible labels for definiteness, must tend to infinity: for each fixed N it is at least N rho_N, and(9) holds for all N.
This means terminal remainder SIZE, not the number of its prime factors.
No lower bound on omega of the remainder or uniform m-dependent rate follows from(9).

<a id="power-stripping-limits-and-contribution"></a>
## 5. What remains unresolved

The direct dominant-prime-power extension fixes the q^2 example in C118 but not all smooth remainders.
For a concrete endpoint, take the singleton order72, full weight phi(72)=24 and window X=72.
Its prime-power factors8 and9: 9>sqrt72, so the first child strips9, leaving b8 and Y8; the next minimal2-power>sqrt8 is4, leaving b2,Y2; then strips2 and reaches1.
This illustrates why testing only PRIME size or only the original factorization is insufficient: the stopping rule is recursive with exact floors.
It is an easily captured finite control, not a near-one construction.

By contrast singleton order30 at X=30 has all prime-power factors2,3,5<=sqrt30 and stops immediately with remainder30.
It is also easily captured.
Thus a large balanced terminal remainder is a necessary structural possibility under the hypothetical sequence, not itself an obstruction to capture or evidence that such a sequence exists.
The theorem creates a positive bounded-remainder class and a precise obstruction to that class; it does not supply automatic original good-prime coverage, bounded terminal remainder, or a universal Mahler gap.

Root contributed the minimal dominant-prime-power substitution and is a contributor.
The g_bridge_audit AI supplied the canonical full-tree organization, ancestor-chain implication for compatible tuples, small-terminal-remainder mass bound with factor3 and physical L_N cost, the full original-norm transfer, and positive-tail remainder escape.
Existing C118/L395 mechanisms are credited rather than reproved as new transport.
The proof itself uses only elementary divisibility/finite weighted sums and the accepted L74/L168 actual-norm interfaces; C114/C116 are motivation, not extra proof dependencies.
No native mathematical computation, J or new external theorem was used.

<a id="power-stripping-entire-author-freeze"></a>
## Entire author freeze

2026-10-14T21:14.
Freeze the ENTIRE original: bounded source/reuse account and actual contribution division; the direct prime-power extension and complete canonical tree; all eligibility, floor and strict-threshold details; ancestor-chain separation; the factor3 deepest-coordinate estimate with original weights; exact finite remainder/capture inequalities and threshold lambda; the enlarged L_N physical time/degree and full signed-norm costs; fixed-N original-mass remainder escape and mean-size implication; finite controls, all nonimplications and unresolved automatic coverage.
The author self-check covered empty eligible trees, repeated labels and deepest-node ties, arbitrary real weights without a capacity assumption, unique child assignment, partial prime-power stripping, original versus quotient lcm and floor composition, original mass retained outside eligibility, possible ell-divisibility of L_N, single-time maximum versus summing different times, every fixed-N/unbounded-N distinction, and actual source/contribution scope.
This is author completion, not independent acceptance.
A noncontributor must review the actual fixed form before adoption; no mathematical program or new external source theorem is involved.

## Fixed organization

The entire final author body is retained, including the direct root-contributed prime-power extension, full canonical tree, chain argument, original-mass inequality, enlarged physical time, actual original norm transfer, fixed-threshold escape, finite controls and unresolved coverage.
Root is a substantive contributor and does not independently review this Claim.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:19 |
| status | open |
| reason | Retain the whole arbitrary-real-weight tree estimate and actual bounded-terminal-remainder sufficient class for separate independent review. Fixed N pays the full L_N time multiplier; no automatic remainder bound, coverage or unrestricted Mahler gap is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Terminal-remainder estimate and actual transfer](#statement) | Entire finite inequality, enlarged-time capture and fixed-threshold original-mass escape, including all domain and nonimplication boundaries. |
| argument | [Complete tree and original-norm argument](#argument) | All Sections 1--5 and equations 1--9, unique stopping, exact floors, deepest-coordinate counting, original weights, repeated coordinates, costs and finite controls. |
| dependency | [Original local norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original residue groups and same-time valuation income, preserving every root and extra depth. |
| dependency | [Uniform original budget](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Full U_D(P) decay for fixed actual auxiliary-degree multiplier D along hypothetical near-one inputs. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler bound from original linear income and fully paid L_N C degree multiplier. |

### Decision whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:22 |
| status | proved |
| reason | Adopt the complete noncontributor [R797 original canonical-tree](../audits/reviews/Yin_R_G0797_v1.md#canonical-tree-whole-independent-finding) review of every retained tree/counting/original-norm step and direct input. Arbitrary positive real weights and all tree branches are covered without retention or capacity hypotheses, with fixed N paying the full L_N physical-time multiplier. Automatic coverage or bounded remainders and the unrestricted gap remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Terminal-remainder estimate and actual transfer](#statement) | Entire finite inequality, enlarged-time capture and fixed-threshold original-mass escape, including all domain and nonimplication boundaries. |
| argument | [Complete tree and original-norm argument](#argument) | All Sections 1--5 and equations 1--9, unique stopping, exact floors, deepest-coordinate counting, original weights, repeated coordinates, costs and finite controls. |
| dependency | [Original local norm floor](../ledger/Yin_L_G0074_v1.md#good-prime-aggregation-and-global-tail) | Complete original residue groups and same-time valuation income, preserving every root and extra depth. |
| dependency | [Uniform original budget](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Full U_D(P) decay for fixed actual auxiliary-degree multiplier D along hypothetical near-one inputs. |
| dependency | [Finite income criterion](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler bound from original linear income and fully paid L_N C degree multiplier. |
| review | [Complete actual finding](../audits/reviews/Yin_R_G0797_v1.md#canonical-tree-whole-independent-finding) | Entire actual retained statement, proof and direct inputs, all hypotheses, quantitative costs, controls, contribution and source limits. |


### Decision current-cyclic-norm-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T05:43 |
| status | proved |
| reason | Locate the already used complete original norm/valuation proof at C256 and, where selected, the original ramified powering proof at C255. Full original proofs were read, retained without mathematical change and actually self-reviewed at their new homes; the same original input scope, current mathematical status and every other relation are retained. This routine proof-location adoption asserts no new independent review or broader theorem and leaves every old dated decision and fixed R input unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire finite inequality, enlarged-time capture and fixed-threshold original-mass escape, including all domain and nonimplication boundaries. |
| argument | [Argument](#argument) | All Sections 1--5 and equations 1--9, unique stopping, exact floors, deepest-coordinate counting, original weights, repeated coordinates, costs and finite controls. |
| dependency | [Dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original residue groups and same-time valuation income, preserving every root and extra depth. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Full U_D(P) decay for fixed actual auxiliary-degree multiplier D along hypothetical near-one inputs. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler bound from original linear income and fully paid L_N C degree multiplier. |
| review | [Review](../audits/reviews/Yin_R_G0797_v1.md#canonical-tree-whole-independent-finding) | Entire actual retained statement, proof and direct inputs, all hypotheses, quantitative costs, controls, contribution and source limits. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire finite inequality, enlarged-time capture and fixed-threshold original-mass escape, including all domain and nonimplication boundaries. |
| argument | [Exact retained argument](#argument) | All Sections 1--5 and equations 1--9, unique stopping, exact floors, deepest-coordinate counting, original weights, repeated coordinates, costs and finite controls. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original residue groups and same-time valuation income, preserving every root and extra depth. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Full U_D(P) decay for fixed actual auxiliary-degree multiplier D along hypothetical near-one inputs. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler bound from original linear income and fully paid L_N C degree multiplier. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0797_v1.md#canonical-tree-whole-independent-finding) | Entire actual retained statement, proof and direct inputs, all hypotheses, quantitative costs, controls, contribution and source limits. |

### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:39 |
| status | proved |
| reason | Adopt the newly performed isolated whole finding in R797 after complete independent reconstruction of this exact fixed mathematics and necessary interfaces, with old target findings consulted only after the initial judgment. The complete arbitrary-weight canonical tree, floor-sensitive chain argument, original-mass remainder inequality, fully paid L_N time multiplier and every fixed-N original-mass escape consequence are supported. Preserve all current statement, argument, dependency and support targets and scopes, prior dates and unknown historical arrangements; their complete original accounts and declarations remain in R797. This decision does not resume G0001 or select Task completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire finite inequality, enlarged-time capture and fixed-threshold original-mass escape, including all domain and nonimplication boundaries. |
| argument | [Exact retained argument](#argument) | All Sections 1--5 and equations 1--9, unique stopping, exact floors, deepest-coordinate counting, original weights, repeated coordinates, costs and finite controls. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) | Complete original residue groups and same-time valuation income, preserving every root and extra depth. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Full U_D(P) decay for fixed actual auxiliary-degree multiplier D along hypothetical near-one inputs. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-finite-income-criterion) | Strict positive Mahler bound from original linear income and fully paid L_N C degree multiplier. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0797_v1.md#g0119-isolated-whole-finding) | Entire exact statement, complete retained mathematical body and all current selected input interfaces, source/contribution limits, original costs, controls and unresolved conclusions; the new isolated whole finding does not reclassify any historical review. |
