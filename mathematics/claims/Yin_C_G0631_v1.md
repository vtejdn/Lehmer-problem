---
author: Yin
---

# Exact original sign-flow lifting on alternating label paths

Root proposed the last-two-update exact lift and the finite short-path exception; original_law checked the full path-conditioned tail distributions and completed the current-length converse, mixed-path accounting and original-mass consequences below.
Both are contributors to this author argument, not independent reviewers.
C627's original conditional factors and C625's current-length positive-mass construction are fixed inputs.
The new result concerns exact paid path lifting and a finite exceptional set; no uniform inter-label congestion or mean branch is supplied.

## Statement

Fix the actual quartic P(t)=t^4-t^3-t^2-t+1, its exterior root beta, neutral conjugate zeta, O=Z[beta] and actual core D.
Put B=1/(beta-1), S_real=beta B.
For every integer n>=5 let k=n-2 and use ALL returned length-2n ternary words eta=(A,theta,C), with both outside tails of length k and four middle digits.
The original digit probabilities are1/4,1/2,1/4, the integer word weight is w(V)=2^(number of zero digits), c_j(x) is the complete integer endpoint count and Z=c_(2n)(0).
Use pi(eta)=w(A)w(theta)w(C)/Z, K=(H_A+H_C)/2 and full sign reversal S eta=-eta.
For actual positive current labels e=(y,c), let

    y=-beta^-k A(beta), c=C(beta), theta_e(beta)=y-beta^4c,
    L_y=c_k(-beta^k y), R_c=c_k(c),
    p_e=L_y R_c w(theta_e)/Z,
    r_y=sum_(e:y(e)=y)p_e, s_c=sum_(e:c(e)=c)p_e,
    alpha_y(A)=w(A)/L_y, gamma_c(C)=w(C)/R_c,
    mu_e(A,C)=alpha_y(A)gamma_c(C).

The four-digit middle word is unique and pi(eta)=p_e mu_e(A,C).
The exact label kernel is

    Kbar(e,e')=1_(y=y')p_(e')/(2r_y)+1_(c=c')p_(e')/(2s_c).

All full-word and label conductances Q(q)=pi(u)K(u,v), Qbar(qbar)=p_e Kbar(e,e') below are for unordered positive NONLOOP edges of these complete original chains.
No conditional source law or graph is renormalized.
For a complete returned word define its algebraic midpoint Y_n=-beta^-n sum_(j<n)eta_j beta^j and its neutral mark Z_n=Y_n(zeta).

Take ANY label selection w_sel in[0,1] with w_sel(Se)=w_sel(e), source masses abar_e=p_e w_sel(e) and a(eta)=pi(eta)w_sel(e(eta)).
For each selected e, suppose Gamma_e is a probability law on finitely many positive nonloop label paths from e to Se, depends only on e, and is supported on ALTERNATING coordinate updates of lengths ell>=4.
Alternating means that successive steps change different coordinates, y then c or c then y.
Define the ordinary original label load

    Lambda_label=max_qbar Qbar(qbar)^-1
                          sum_e abar_e E_(Gamma_e)[ell N_qbar].  (1)

There is an explicit randomized full-word path from EACH eta to its OWN full negative S eta, with exactly the same ell as its chosen label path, no same-label transitions and

    Lambda_full=max_q Q(q)^-1 sum_eta a(eta)E[length N_q]
               =Lambda_label.                                (2)

Each of the first ell-2 updates samples the changed tail from its complete original alpha or gamma law.
The last two updates change different tails and set those tails to the stored negatives of the original A and C.
No additive length cost, label-holding denominator or individual-tail atom denominator occurs in (2).
The identity includes repeated visits and both orientations of every edge.
It does not cover a path of length below4 by this construction.
Section3 gives a complete paid mixture with C627's existing lift for short paths, together with an actual zero-length counterexample to dropping the length restriction.

Any finite positive label path can be shortened to an alternating path with the same endpoints by clique shortcuts and removal of closed two-step backtracks.
Its length does not increase, but no monotonicity of congestion under this shortening is asserted.
Its paid load must be computed from the resulting paths.

Let Theta={sum_(j=0)^3 theta_j beta^j:theta_j in{-1,0,1}} and define the FIXED set

    F_exc=(beta^-2 Theta) intersect D,
    card(F_exc)<=81, |x(zeta)|<=4 for every x in F_exc.       (3)

For any actual positive zero-middle label e=(y,c), y=beta^4c, with c!=0, the CURRENT label distance from e to Se is at most3 if and only if y belongs to Theta.
In that case the distance is exactly3, with the explicit current path

    (y,c) -> (y,0) -> (-y,0) -> (-y,-c).                    (4)

Distances1 and2 are impossible for any such nonzero e.
The zero label has distance0.
The actual algebraic midpoint on this zero-middle label is Y_n=beta^-2y=beta^2c, not merely a value of the same neutral norm.
Thus a zero-middle source outside F_exc cannot have a label sign path shorter than4.

Use C625's fixed N_sqrt and L_n=ceil(4A_len sqrt(n log128)+2B_len), with their exact original realization constants as defined in that fixed statement.
For every integer n>=N_sqrt define M_n by theta_e=0 and |Y_n(e)(zeta)|<=2sqrt(n log128), and M_n_long by the additional condition Y_n(e) not in F_exc.
Set delta_n_long=sum_(e in M_n_long)p_e and D_n=p_(2n)/p_n^2, with the original return probabilities.
Then

    delta_n_long>=1/32-b_n(F_exc)
                >=1/32-card(F_exc)/D_n
                >=1/32-81/D_n.                             (5)

Here b_n is C204's COMPLETE original chronological midpoint law.
Every selected label in M_n_long has an alternating sign path with 4<=ell<=L_n at the SAME n, and the complete source fibers admit (2).
In particular delta_n_long>=1/64 at each n>=N_sqrt with D_n>=5184.
This is a pointwise condition on D_n, not an assertion that it eventually holds.

If the actual critical mean mu is infinite, use C204's ONE common subsequence n_j with D_(n_j)->infinity.
Along precisely that subsequence,

    liminf_j delta_(n_j)_long>=1/32,
    delta_(n_j)_long>=1/64 for all sufficiently large j.     (6)

No all-late escape or convergence D_n->infinity is asserted.
At each n>=N_sqrt either b_n(F_exc)>=1/64 or delta_n_long>1/64; the choice may vary with n.
If the first alternative holds for EVERY sufficiently large n, C204 gives mu<=64 card(F_exc)<=5184.
An occurrence on merely a subsequence does not imply that conclusion.

For ANY such exact lifted path laws along ANY sequence n_j with D_(n_j)->infinity, C602 also gives the conditional necessary endpoint-load bound

    liminf_j Lambda_label(n_j)/D_(n_j)
                      >=1/(32768 B S_real).                 (7)

This uses liminf selected mass at least1/32 from (5), not an unproved mean branch.
No upper estimate of Lambda_label is obtained from path length, topology or (2).
The original mean classification, a uniform paid inter-label load and the unrestricted Lehmer Task remain open.
At the digit-work clock both loads in (2) multiply by n+2, so the equality remains exact.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision exact-alternating-lift-registration

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:43 |
| status | open |
| reason | Register the complete exact same-length original sign-flow lift for alternating label paths of length at least4, the paid mixed-length boundary and actual empty-path counterexample, the exact current zero-middle short-distance classification, and the complete-mass pointwise/common-subsequence consequences. No uniform inter-label load, all-late escape, actual mean branch or final Task conclusion is supplied; fresh isolated whole review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Complete actual n>=5 quartic word law, full conditional fibers and source selection, label-only finite path laws, exact length and load identity, mixed and short-path limits, clique compression without a congestion comparison, current distance3 iff middle label lies in Theta, fixed at-most81-point exception, exact midpoint, original current mass, precise all-late versus common-subsequence scope and conditional necessary load price. |
| argument | [Complete proof](#argument) | All Sections 1--5 and formulas 1--13, including every first/intermediate/final update distribution, source-terminal correlation, exact edge-factor cancellation and unordered repetitions, short empty-path obstruction, current positive tail witnesses, parity in the actual integer basis, original midpoint orientation and unchanged time/mean quantifiers. |
| dependency | [Complete original factors](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) | Exact full product law and original conductances for each current label edge, with all endpoint counts and complete original normalizer; no uniform label estimate imported. |
| dependency | [Existing general paid negative-word lift](Yin_C_G0627_v2.md#full-negative-word-randomized-lift) | Complete four-refresh construction and load formula used only for short paths in the mixed-length bound, including original source/terminal correlation and unordered edge factors. |
| support | [Existing selected odd-energy comparison](Yin_C_G0627_v2.md#selected-odd-energy-lift) | Already proved optimal residual-mode cost at most2, separate from the new exact path-load identity. |
| support | [Existing matching refresh estimate](Yin_C_G0627_v2.md#square-root-matching-application) | Previously paid refresh control on an all-late matching selection remains valid; it is not imported as a uniform inter-label bound or used to replace the new source mass. |
| dependency | [Actual current paths and exact square-root constants](Yin_C_G0625_v1.md#statement) | Complete original zero-middle radius mass at least1/32, exact N_sqrt and A_len,B_len,L_n, and same-current-n full-word sign paths at every n>=N_sqrt. |
| dependency | [Original midpoint law and pointwise atom bound](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Exact chronological midpoint law, full original return counts and pointwise b_n(F)<=card(F)/D_n, including complete sign/orientation matching. |
| dependency | [One common null-branch subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Only on the infinite-mean branch, one common sequence D_nj tending to infinity and escape of all fixed finite sets; neither all-late escape nor full-sequence divergence is imported. |
| dependency | [All-late finite-core capture implication](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | The conditional bound mu<=64 card(F_exc) requires capture at every sufficiently large n, not merely along a subsequence. |
| dependency | [Necessary original flow price](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Actual sign-symmetric full source mass, original conductance and randomized-load obstruction, transferred by the exact load identity along a supplied divergent sequence. |
| support | [Four-digit uniqueness and midpoint mark](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Actual power basis, unique middle word and complete label midpoint mark; no relaxed or uniform graph law. |

<a id="argument"></a>

<a id="alternating-lift-original-factors"></a>

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T19:53 |
| status | proved |
| reason | Adopt the entire exact alternating lift and its full current/mixed-path consequences after main reading of the fixed C and isolated whole R835. Every first/final tail correlation and edge factor is checked, giving exact same length and Lambda_full=Lambda_label for alternating lengths at least4. The actual short-distance iff, finite81-point exception, pointwise5184 threshold, common divergent subsequence and necessary load price retain their precise quantifiers. No upper label load or actual critical-mean branch is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Complete actual n>=5 quartic word law, full conditional fibers and source selection, label-only finite path laws, exact length and load identity, mixed and short-path limits, clique compression without a congestion comparison, current distance3 iff middle label lies in Theta, fixed at-most81-point exception, exact midpoint, original current mass, precise all-late versus common-subsequence scope and conditional necessary load price. |
| argument | [Complete proof](#argument) | All Sections 1--5 and formulas 1--13, including every first/intermediate/final update distribution, source-terminal correlation, exact edge-factor cancellation and unordered repetitions, short empty-path obstruction, current positive tail witnesses, parity in the actual integer basis, original midpoint orientation and unchanged time/mean quantifiers. |
| dependency | [Complete original factors](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) | Exact full product law and original conductances for each current label edge, with all endpoint counts and complete original normalizer; no uniform label estimate imported. |
| dependency | [Existing general paid negative-word lift](Yin_C_G0627_v2.md#full-negative-word-randomized-lift) | Complete four-refresh construction and load formula used only for short paths in the mixed-length bound, including original source/terminal correlation and unordered edge factors. |
| support | [Existing selected odd-energy comparison](Yin_C_G0627_v2.md#selected-odd-energy-lift) | Already proved optimal residual-mode cost at most2, separate from the new exact path-load identity. |
| support | [Existing matching refresh estimate](Yin_C_G0627_v2.md#square-root-matching-application) | Previously paid refresh control on an all-late matching selection remains valid; it is not imported as a uniform inter-label bound or used to replace the new source mass. |
| dependency | [Actual current paths and exact square-root constants](Yin_C_G0625_v1.md#statement) | Complete original zero-middle radius mass at least1/32, exact N_sqrt and A_len,B_len,L_n, and same-current-n full-word sign paths at every n>=N_sqrt. |
| dependency | [Original midpoint law and pointwise atom bound](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Exact chronological midpoint law, full original return counts and pointwise b_n(F)<=card(F)/D_n, including complete sign/orientation matching. |
| dependency | [One common null-branch subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Only on the infinite-mean branch, one common sequence D_nj tending to infinity and escape of all fixed finite sets; neither all-late escape nor full-sequence divergence is imported. |
| dependency | [All-late finite-core capture implication](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | The conditional bound mu<=64 card(F_exc) requires capture at every sufficiently large n, not merely along a subsequence. |
| dependency | [Necessary original flow price](Yin_C_G0602_v2.md#neutral-packing-and-load-lower-bound) | Actual sign-symmetric full source mass, original conductance and randomized-load obstruction, transferred by the exact load identity along a supplied divergent sequence. |
| support | [Four-digit uniqueness and midpoint mark](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Actual power basis, unique middle word and complete label midpoint mark; no relaxed or uniform graph law. |
| review | [Independent whole alternating-flow finding](../audits/reviews/Yin_R_G0835_v1.md#alternating-sign-flow-whole-independent-finding) | Entire statement and five-section proof, all original factors/correlations/orientations, mixed short paths and actual counterexample, exact current distance3 classification, algebraic midpoint and every mass/subsequence/all-late/clock condition; historical source and prior reviews unchanged. |

## 1. Exact reuse and complete edge factors

C627v2's [complete original comparison](Yin_C_G0627_v2.md#conditional-lift-exact-reuse) supplies the product law, strong lumping and full conditional factors at the stated current n.
Its [selected odd-energy theorem](Yin_C_G0627_v2.md#selected-odd-energy-lift) already bounds the optimal tail-noise cost by2; that result is unchanged here.
Its four-refresh random lift remains valid for arbitrary finite sign paths, with all holding probabilities paid, and its matching trim remains a separate proved way to bound the refresh term on a positive-mass selection.
The present new construction removes those four refreshes only under the stated alternating-length premise.
The local reuse search found no earlier exact equality (2) in these actual full-word interfaces.

For distinct labels e,e' sharing y, let the full edge fix the same left word A and change C to C'.
Its exact conductance is

    Q(q)=Qbar({e,e'}) alpha_y(A)gamma_c(C)gamma_(c')(C').    (8)

For labels sharing c it is

    Q(q)=Qbar({e,e'}) gamma_c(C)alpha_y(A)alpha_(y')(A').    (9)

The factors are invariant under reversing the full edge orientation.
Every positive pair of actual endpoint labels admits all combinations of the indicated tail representations, because its middle word is unique and its return equation is satisfied by each combination.
Thus every positive label edge has positive full-word edges of exactly the displayed form.
An original full-word nonloop edge either projects to one of these nonloop label edges or keeps its label and changes one tail within its own complete fiber.
The latter edges will be unused by the construction of Section2.

<a id="alternating-exact-negative-word-lift"></a>
## 2. The same-length lift and exact congestion identity

Fix an entire selected label path e_0,...,e_ell, ell>=4, and condition on this choice.
Because Gamma depends only on e_0, the initial full source mass conditional on the path is exactly alpha_(y0)(A0)gamma_(c0)(C0).
Store A0,C0.
For steps i=1,...,ell-2 sample the changed tail independently from its COMPLETE alpha or gamma marginal at e_i.
At steps ell-1 and ell, set the changed tail to the stored negative of its original source tail.
The last two coordinate changes are different, so the destination coordinate at step ell-1 is already the corresponding coordinate of e_ell=Se_0.
That stored negative therefore belongs to the exact required endpoint fiber.
The unchanged coordinate is likewise correct for the last step, and the final full word is (-A0,-theta_(e0),-C0)=S eta0.

Each label step is nonloop and changes one coordinate.
The corresponding old and new tail endpoints are different, so the full word also changes and each step is an actual positive nonloop K edge by (8) or (9).
There is no identity move to delete: the full path has exactly ell steps.
No update is conditioned on holding its label fixed.

It remains to check the COMPLETE path-conditioned traffic at every position, including the first and final pairs.
At step1 the held and old-changing tails are the two independent original source tails, and the new-changing tail is an independent complete draw.
Thus the joint law for the three words is precisely the factor in (8) or (9).
At step2, alternation means the held tail is the fresh draw from step1; the old-changing tail is the other original source tail, and the new-changing tail is another independent complete draw.
The same factorization holds.
After step2 both current tails have their complete product law and are independent of BOTH stored original tails.
They remain so through step ell-2, because each subsequent sampled update changes one tail independently and retains the other marginal.
This includes the case ell=4, where the first two sampled steps are exactly all the steps before the final pair.

At step ell-1, the old-changing and held tails are fresh product-law tails independent of the stored source.
The target is the corresponding stored negative, which by original sign symmetry has the complete required alpha or gamma marginal and is independent of both current tails.
At step ell, the held tail is the stored negative set at step ell-1.
The old-changing tail is still fresh, and the target is the negative of the OTHER original tail.
The two original source tails are independent conditional on e_0 and the path, so these three words again have precisely the complete factor in (8) or (9).
This last check preserves the required correlation between source and terminal full word; no unrelated terminal word is sampled.

Consequently for EVERY position i and EVERY full edge q projecting to the label edge qbar traversed at that position,

    Pr(full edge q is used at i | entire label path)
                     = Q(q)/Qbar(qbar).                     (10)

The probability refers to the complete product-distributed sources and the specified internal draws, not to the K probability of selecting the prescribed label path.
The latter is paid by Qbar in the load denominator.
The same factor in (10) holds for reverse traversals.
Multiply by ell, sum positions and sum all directed original source masses abar_(e0), with their path-law probabilities.
Repeated visits require no independence between positions, since only their expected traversal counts are added.
The resulting exact identity for each such full edge is

    Q(q)^-1 sum_eta a(eta) E[ell N_q]
       =Qbar(qbar)^-1 sum_e abar_e E[ell N_qbar].            (11)

All within-label loads are zero, and every positive label edge has a full representative edge.
Taking maxima proves (2), including zero/unused loads by the empty-maximum convention.
This is exact original probability cancellation; no full word atom is bounded below.

<a id="alternating-shortening-and-short-path-scope"></a>
## 3. Path shortening, mixed lengths and the short-path boundary

Two consecutive label moves that change the same coordinate lie in the same row or column clique of the actual positive label chain.
If the first and third vertices are distinct, replace the two edges by their positive direct clique edge.
If they coincide, erase the closed two-edge backtrack instead.
The retained vertices are actual current vertices and the replacement or concatenated edges remain positive at the same n.
Repeating this length-decreasing operation terminates with an alternating path and the original endpoints.
No weights are removed from the graph, but a shortcut may use a different small-conductance edge.
Thus this argument bounds only length and feasibility; it does not assert that congestion decreases.

If a finite alternating label path law with the same label-only dependence mixes long and short paths, use Section2 on ell>=4 and C627's four-refresh lift on ell<4.
This gives a full path to the exact negative for every source with the following paid bound.
Put

    chi=1_(ell<4),
    m_e_short=abar_e E[(ell+4)chi],
    Lambda_mix=max_qbar Qbar(qbar)^-1
                      sum_e abar_e E[(ell+4chi)N_qbar],
    q_A(e)=p_e/(2r_y), q_C(e)=p_e/(2s_c).

Then

    Lambda_full<=max{Lambda_mix,
      max_e 2(m_e_short+m_(Se)_short)
                          /[p_e min(q_A(e),q_C(e))]}.       (12)

For inter-label edges, the long-path contribution has the exact factor (10), while the short-path contribution has C627's upper length ell+4 and the same original representation factor.
Within-label edges receive only the two initial and two final refresh contributions from the short paths.
C627's unordered-edge calculation gives exactly the second term of (12).
No symmetry of the short-path probability in Gamma_e versus Gamma_(Se) is required: both appear separately in that numerator, while the original source selection remains sign-symmetric.
If all chosen paths are long, the second term is zero and the stronger identity (2) applies.

There is an actual reason not to state an unrestricted same-length theorem.
For n>=7, k>=5, take the left word A0 with first five coefficients (1,-1,-1,-1,1), followed by zero padding, and let the middle and right words be zero.
Since P(beta)=0, this is an original positive returned word at the zero label e=(0,0), but eta0 is not its negative.
The empty label path has length0, so no full path of that same length can join eta0 to S eta0.
For a three-step path the argument of Section2 would also leave only one sampled step before the final pair, so its independence proof is not applicable in general.
This is a stated limitation of that construction, not an obstruction to every other short-path comparison.

<a id="zero-middle-exact-short-exception"></a>
## 4. The exact short exception at the actual current length

The powers1,beta,beta^2,beta^3 form the integer basis of O used by C170, and beta is a unit: beta^-1=-beta^3+beta^2+beta+1.
Thus Theta has exactly81 members and beta^-2Theta lies in O.
The set F_exc in (3) is finite and sign-symmetric, with card at most81 and neutral radius at most4 because |zeta|=1.
No enumeration of these patterns or assumption that all81 are in D is needed.

Fix an actual positive zero-middle e=(y,c), y=beta^4c and c!=0.
Both its coordinates differ from those of Se, so distance1 is impossible.
An alternating two-step path must pass through (y,-c) or (-y,c), whose middle polynomial is respectively 2y or -2y.
If either is in Theta, each integer coordinate of 2y lies in{-1,0,1} and is even; hence y=0, a contradiction.
Nonalternating two-step paths would fix one coordinate and cannot have these endpoints.
Therefore distance2 is impossible.

Any three-step shortest path is alternating by Section3.
For the coordinate pattern c,y,c, write its two intermediate labels as (y,d),(-y,d), with middle polynomials theta1=y-beta^4d and theta2=-y-beta^4d.
Then theta1-theta2=2y.
For the pattern y,c,y, write the intermediate labels as (z,c),(z,-c), with theta1=z-y and theta2=z+y.
Then theta2-theta1=2y.
In either case the difference has even integer coordinates, each in{-2,-1,0,1,2}; division by2 gives the coordinates of y in{-1,0,1}.
Thus y belongs to Theta, proving necessity without any relaxed-state approximation.

Conversely suppose y belongs to Theta and e is an actual current zero-middle label with c!=0.
Let theta_y be the unique four-digit word representing y.
The two intermediates in (4) have middle words theta_y and -theta_y, whose polynomials are y and -y.
Their left-tail counts L_y and L_(-y) are positive because e and Se are current original labels.
Their right-tail count is R_0>=2^k, from the all-zero word.
Their weights L_y R_0 w(theta_y) and L_(-y) R_0 w(-theta_y) are therefore positive at exactly the same n, proving the actual current path (4).
All three steps are nonloop because c and y are nonzero.
This proves the exact label-distance assertion.
Indeed for any full source one can realize this three-step path by (A0,0,C0)->(A0,theta_y,0)->(-A0,-theta_y,0)->(-A0,0,-C0).
That existence statement does not assert the generic product traffic of Section2, since its middle tail pair is correlated as A0,-A0.

For a zero-middle source the original algebraic midpoint is

    Y_n=-beta^-n A(beta)=beta^-2 y=beta^2c.                 (13)

Its first-half sum contains only A and the first two zero middle digits.
This proves the orientation and value exactly, in addition to the neutral-radius identity.
Membership in F_exc is equivalent to y in Theta for this actual source, so (3) gives precisely the short-label exception within the actual zero-middle support.

<a id="alternating-current-mass-and-null-subsequence"></a>
## 5. Complete original mass and the exact time quantifiers

C625 supplies, for EVERY n>=N_sqrt, the complete original zero-middle radius selection M_n of mass at least1/32 and positive same-current-n full-word sign paths of length at most L_n.
Project these paths onto the actual label graph, remove successive equal labels and perform Section3's clique compression.
For any source in M_n_long, Section4 excludes every length below4, while compression never increases the supplied L_n bound.
The resulting paths thus meet every hypothesis of Section2.
One may choose a path for each label independently of its tail representations; the label graph and finite supplied length bound suffice.
This construction is finite at each specified n and uses no graph search or unproved uniform support assertion.

The law of the exact midpoint in (13) is the b_n of C204, including its original sign and chronological-time convention.
Write S_n=sum_(j=0)^(n-1)eta_j beta^j for an independent original half-word, so p_n=Pr(S_n=0).
For an arbitrary returned word its two half sums then give

    Pr(Y_n=x)=Pr(S_n=-beta^n x) Pr(S_n=x)/p_(2n).

Original sign symmetry changes the first factor to Pr(S_n=beta^n x), giving exactly C204's complete midpoint formula.
Consequently the original mass discarded from M_n is at most b_n(F_exc), and (5) follows from C625 and C204's pointwise inequality b_n(F)<=card(F)/D_n for every fixed finite F subset D.
All source selections are still unions of complete alpha/gamma fibers with unnormalized original mass, and the graph conductances are unchanged.
The threshold5184 is 64 times81; no hidden estimate of D_n is used.

On the infinite-mean branch C204 supplies ONE common subsequence with D_(n_j)->infinity and b_(n_j)(F)->0 simultaneously for every fixed finite F.
Apply it to this one fixed F_exc and discard only finitely many indices below N_sqrt.
This proves (6), with the same subsequence, and does not extend it to all sufficiently large n.
Separately (5) implies the stated pointwise alternative between b_n(F_exc)>=1/64 and delta_n_long>1/64.
Its alternatives can change with n.
Only the additional ALL-LATE premise b_n(F_exc)>=1/64 for every n beyond one finite threshold permits C204's mean bound mu<=64 card(F_exc)<=5184.
A subsequence of finite-core capture alone supplies no such implication.
No actual alternative has been selected as the mean classification.

For (7), choose any fixed 0<delta<1/32.
Along any sequence with D_(n_j)->infinity, (5) ensures delta_(n_j)_long>=delta eventually.
C602's necessary original sign-flow bound therefore gives liminf Lambda_full/D>=delta^2/(32 B S_real).
Use the exact identity (2) and then increase delta to1/32, obtaining1/(32768 B S_real).
This transfers a necessary load price to the actual label chain; it supplies no upper bound and makes no claim that such a divergent sequence exists on the actual branch.
The digit-work equality follows because all original conductances, label and full-word alike, divide by n+2.
No finite computation, external theorem, uniform endpoint mixing claim or final Task conclusion is used.
