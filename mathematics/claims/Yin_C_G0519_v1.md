---
author: Yin
---

# Complete original-fiber weights and paid paths on the persistent finite carry hub

This retains the complete necessary mathematical argument from [complete original L411](../ledger/Yin_L_G0411_v1.md#fixed-seed-weight-question).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Fix the ACTUAL quartic P(t)=1-t-t^2-t^3+t^4, its exterior positive root beta>1, the original order O=Z[beta] and the original independent digit probabilities 1/4,1/2,1/4 on{-1,0,1}.
For each integer k>=0 let nu_k(z)=Pr(sum_(i=0)^(k-1)eta_i beta^i=z) be the COMPLETE original k-digit endpoint probability, c_k(z)=4^k nu_k(z) its integer weighted count, and p_k=nu_k(0).
The chronological kernel is K(x,beta x+eta)=Pr(eta), so independent digit reversal gives K^k(0,z)=nu_k(z).
All later representations and every original returned word are included.

For EVERY integer k>=6 put n=k+2, so the full return length is 2k+4=2n.
At actual normalized left labels x=beta^(-k)z and right labels c, the unique middle word theta has four original-order coordinates in{-1,0,1} and theta=-x-beta^4 c.
Write

    W_k(x,c)=a_k(x)b_k(c)w(theta),
    a_k(x)=c_k(beta^k x), b_k(c)=c_k(c),
    w(theta)=2^(number of zero coordinates),
    S_k=c_(2k+4)(0), t_k=c_k(0)^2/S_k,
    r_k(x)=sum_c W_k(x,c), h_k(c)=sum_x W_k(x,c),
    pi_k(x)=r_k(x)/S_k.

Only actual positive endpoint fibers are vertices.
Here S_k is the FULL return normalization, with no seed restriction.
Let V and U be the normalized left and right sets of the ACTUAL connected n=8 seed already verified by J106: |V|=|U|=v=25 and 141 edges.
All these labels and edges persist at every k>=6 by the induced nesting theorem; no larger graph is computed.
Put a=4^(-6), C=256.
Then for ALL k>=6 and EVERY seed x in V,c in U,

    a c_k(0)<=a_k(x)<=c_k(0),
    a c_k(0)<=b_k(c)<=c_k(0).

The proof uses actual length-six chronological witnesses and arbitrary length-(k-6) returns, including k=6 through p_0=1, and the original monotonicity p_(k-6)>=p_k.
It is a COMPLETE-fiber comparison, not the probability of one zero-padded word or a conditional fiber law.
The global binary-autocorrelation bound and full middle weight sum(1+2+1)^4=C give at EVERY actual vertex

    r_k(x)<=C a_k(x)c_k(0), h_k(c)<=C b_k(c)c_k(0),
    pi_k(x)<=C t_k.

Consequently with M_k=pi_k(V),

    a^2 t_k<=pi_k(x)<=C t_k  for x in V,
    v a^2 t_k<=M_k<=min(1,v C t_k).

For C170's ORIGINAL two-step left-endpoint kernel T_k the nonloop conductance, denoted c_k(x,x') with TWO endpoint arguments, is

    c_k(x,x')=pi_k(x)T_k(x,x')
       =(1/S_k)sum_c W_k(x,c)W_k(x',c)/h_k(c).

Every seed two-step edge sharing a seed right neighbor satisfies c_k(x,x')>=a^3 t_k/C for all k>=6.
No nonseed neighbor contribution is subtracted.
Fix ANY spanning tree of the connected seed two-step left graph and its simple ordered-pair paths, with maximum length L=v-1=24 and no repeated edge.
Reflection of T_k onto V changes only transitions leaving V into loops, with stationary law pi_k^V=pi_k/M_k and internal conductance c_k/M_k.
For any kernel Q and its stated stationary law rho, D_Q(f)=(1/2)sum_(x,y)rho(x)Q(x,y)|f(y)-f(x)|^2.
Every chosen edge has conditional conductance at least a^3/(v C^2), and for EVERY real f on V,

    Var_(pi_k^V)(f)<= [L v C^2/(2a^3)]
                      D_(T_k reflected to V)(f),  k>=6.

This is a local finite-patch estimate in its true conditional weights; it supplies no positive original mass or full-chain gap by itself.

On the FULL endpoint law choose G_k=(V times V) union{(x,x):x any actual vertex}.
Use the fixed seed paths on V and empty paths on all other diagonal pairs.
For each unordered nonloop edge e use the ordered-pair load convention Load_k(e)=[1/(2c_k(e))]sum_((x,y) in G_k)pi_k(x)pi_k(y)|gamma_xy|N_e(gamma_xy).
Here |gamma_xy| is path length and N_e is its edge traversal count.
The tree paths have no repeated edge; unused edges have load 0.
For all used edges,

    Load_k(e)<=L M_k^2/[2c_k(e)]
       <=[L C/(2a^3)] M_k^2/t_k
       <=[L v^2 C^3/(2a^3)]t_k.

The exact retained ORIGINAL product mass, including all outside diagonal pairs, is

    (pi_k tensor pi_k)(G_k)=M_k^2+sum_(x outside V)pi_k(x)^2
       <=v^2 C^2 t_k^2+C t_k.

For the ORIGINAL overlap D_k=p_(2k)/p_k^2>=1, degree 4 gives p_4=1/16 and returned-block concatenation with collision monotonicity gives p_(2k)/16<=p_(2k+4)<=p_(2k).
Thus EXACTLY t_k=p_k^2/[256p_(2k+4)] and

    1/(256D_k)<=t_k<=1/(16D_k)<=1/16,
    Load_k(e)<=L v^2 C^3/(32a^3)  for EVERY k>=6.

All full-word normalization, middle weights, path lengths, factors 1/2 and original clocks are paid.
In particular the COMPLETE seed mass is between v a^2/(256D_k) and min(1,v C/(16D_k)).
This proves the UNIFORM LOAD half of the concrete partial-path mechanism, not its retained-mass half.

Here mu is the original chronological first-return mean at the TRUE critical radius, as in C204; no R=beta premise is made.
If that ACTUAL unresolved mean is infinite, the existing complete midpoint theorem supplies ONE common subsequence k_j->infinity with D_(k_j)->infinity.
Along that same subsequence (pi_(k_j) tensor pi_(k_j))(G_(k_j))->0; the fixed hub omits asymptotically all original product pairs despite its uniformly bounded loads.
This is conditional on the null branch and does not prove that branch occurs.
If the mean is finite, D_k->mu and the seed has positive eventual original mass, but these constants do not imply retained product mass>1/2 or any fixed omitted mass 2epsilon with epsilon<1/4.
Even that branch alone does not certify this particular seed as a sufficient bulk hub.
The result asserts no growing-patch construction, translated-seed uniformity, moving-endpoint bound, global contraction, actual mean classification or unrestricted gap.
All twelve original formulas and eight input rows, complete original proof, contributor declarations and exact finite-versus-all-late boundaries are retained.
There is no new graph length, native execution, external source theorem or source-proof audit.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:48 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Complete original endpoint reduction](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Exact original W,S,r,h and two-step T with positive actual marginals; no uniform contraction is inherited. |
| dependency | [Actual four-digit marks](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Original rank-four basis, unique middle word and all 81 possible weighted neighbors, not unweighted degree. |
| dependency | [Complete normalized seed nesting](Yin_C_G0514_v2.md#nested-normalized-carry-support) | Only induced persistence of the actual fixed seed labels and edges; positivity belongs to actual endpoints and no absolute mass is inferred. |
| dependency | [Complete original paid-path test](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Full-word transfer, ordered-pair load 1/(2c_e), every clock and discarded original mass threshold 2epsilon with epsilon<1/4. |
| dependency | [Original chronological law](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Binary autocorrelation domination for complete endpoint counts, original K and D_k>=1. |
| dependency | [Actual finite-mean overlap limit](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | D_k->mu only in the finite-mean branch; no moving-state ratio or convergence rate. |
| dependency | [Original complete midpoint equivalence](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Finite mean iff eventual bounded original overlap; a lower hub mass is not substituted for the full criterion. |
| dependency | [One common null-branch subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Infinite mean would supply one subsequence D_(k_j)->infinity; neither all-time divergence nor the actual branch is asserted. |
| dependency | [Original collision monotonicity](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Only p_l nonincreasing and p_0=1 are reused; no unrelated large-block gap. |
| dependency | [Actual fixed n8 seed](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results) | Exactly 25+25 vertices,141 edges and connectivity from the retained finite evidence; no present execution, extra length or spectral estimate. |
| support | [Existing finite seed inspection](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) | Original all-payload verification at its actual exposure, runtime and nonblind limits, not newly executed evidence. |
| support | [Earlier paid paths](Yin_C_G0076_v1.md#statement) | Only the earlier path-Cauchy method and original mass expenses, not connectivity from its different six-digit graph. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:54 |
| status | proved |
| reason | Adopt after actual complete whole SELF formed12:53 of the exact current Statement and entire complete-fiber fixed-hub proof, all conductance/path/reflection/return-normalization factors and original full product mass, using only the retained n8 seed. No substantive defect or proof repair was found. The original complete author check is retained separately, and original R562 inputs/date/exposure remain. Uniform load does not pay the unproved half-product mass premise, and neither actual critical mean, growing-patch control, new computation nor Task/E continuation is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix) | Exact original W,S,r,h and two-step T with positive actual marginals; no uniform contraction is inherited. |
| dependency | [Exact dependency](Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Original rank-four basis, unique middle word and all 81 possible weighted neighbors, not unweighted degree. |
| dependency | [Exact dependency](Yin_C_G0514_v2.md#nested-normalized-carry-support) | Only induced persistence of the actual fixed seed labels and edges; positivity belongs to actual endpoints and no absolute mass is inferred. |
| dependency | [Exact dependency](Yin_C_G0514_v2.md#partial-path-weighted-carry-target) | Full-word transfer, ordered-pair load 1/(2c_e), every clock and discarded original mass threshold 2epsilon with epsilon<1/4. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse) | Binary autocorrelation domination for complete endpoint counts, original K and D_k>=1. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#true-harmonic-ratio-limits) | D_k->mu only in the finite-mean branch; no moving-state ratio or convergence rate. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Finite mean iff eventual bounded original overlap; a lower hub mass is not substituted for the full criterion. |
| dependency | [Exact dependency](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Infinite mean would supply one subsequence D_(k_j)->infinity; neither all-time divergence nor the actual branch is asserted. |
| dependency | [Exact dependency](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Only p_l nonincreasing and p_0=1 are reused; no unrelated large-block gap. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results) | Exactly 25+25 vertices,141 edges and connectivity from the retained finite evidence; no present execution, extra length or spectral estimate. |
| support | [Exact support](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) | Original all-payload verification at its actual exposure, runtime and nonblind limits, not newly executed evidence. |
| support | [Exact support](Yin_C_G0076_v1.md#statement) | Only the earlier path-Cauchy method and original mass expenses, not connectivity from its different six-digit graph. |
| review | [Exact review](../audits/reviews/Yin_R_G0729_v1.md#complete-fixed-hub-whole-self-finding) | Entire exact current Statement and all twelve original formulas/eight input rows, full later-fiber counts, original conductance/reflection/path costs, exact retained product mass and both true-radius mean branches; original finite evidence is reused without execution and actual current whole is SELF. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

## Complete-fiber weights on a fixed carry seed and the cost of hub paths

Date: 2026-10-18T15:57.
Human author Yin.
Root assigned the open S2/S7 question of proving or refuting a concrete weighted-carry path mechanism.
The entropy_attainment_bridge agent authors the deductions below; root supplied the question only.
This fixed ledger retains the complete author argument without mathematical alteration; independent review and adoption remain separate.
No new graph length, numerical scan or mathematical program is used.

<a id="fixed-seed-weight-question"></a>
## Changed concrete mechanism and reused inputs

[L410](Yin_C_G0514_v2.md#nested-normalized-carry-support) proves that the normalized b=2 carry graphs are induced nested graphs and that the n=8 seed is connected.
Its zero-padding estimate concerns a specified copy of full words and explicitly does NOT bound all later representations of those endpoint edges.
Here the candidate is to keep the finite connected n=8 seed as a permanent hub network, use ALL representations of every seed endpoint at later lengths, and route all seed endpoint pairs on fixed paths.
We calculate actual multiplicity ratios, original conductances, full endpoint mass and the resulting weighted path load.
This tests the missing complete-fiber question rather than repeating the probability of specified zero-padded words.

The exact original law, two-step kernel and marks are [C170](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix), with its separate [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding).
The finite seed has25 left and25 right endpoints and141 edges and is connected, exactly the n=8 [J106 result](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results), independently checked in [R412](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding).
The present author contributed to C170/J106 and does not independently re-review them.
[L329](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) supplies original endpoint autocorrelation domination, overlap D_k and its actual critical-mean equivalence.
[C169](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) gives monotonicity of the original return probabilities.
[C76](Yin_C_G0076_v1.md#statement) and L410 already retain the weighted path-Cauchy argument; no general path theorem is claimed anew.
A bounded reuse check of C76, C170, L329, L332, L353 and L410 found no complete-fiber estimate for this fixed persistent hub; this is not a literature novelty claim.

<a id="seed-complete-count-comparison"></a>
## 1. Complete endpoint count comparison at fixed seed vertices

Fix the actual quartic P=1-t-t^2-t^3+t^4, its exterior root beta and original order O=Z[beta].
Write nu_k(a) for the complete original k-digit endpoint probability and c_k(a)=4^k nu_k(a) for its integer weight, with digit weights1,2,1.
Set p_k=nu_k(0), k=n-2 and C=4^4=256.
The original chronological kernel is K(x,beta x+eta)=Pr(eta); reversal of the independent digit order gives K^k(0,z)=nu_k(z).
For a normalized left endpoint x=beta^-k a and right endpoint c, the middle word theta has four original-order coordinates in{-1,0,1} and satisfies

    theta=-x-beta^4 c,
    W_k(x,c)=a_k(x)b_k(c)w(theta),
    a_k(x)=c_k(beta^k x), b_k(c)=c_k(c),
    w(theta)=2^(number of zero coordinates),
    S_k=c_(2k+4)(0), t_k=c_k(0)^2/S_k.                  (1)

The notation S_k is the complete weighted return sum, not a restricted seed normalization.
The endpoint marginals are r_k(x)=sum_c W_k(x,c), h_k(c)=sum_x W_k(x,c), and pi_k(x)=r_k(x)/S_k.
Let V and U be the normalized left and right vertex sets of the actual connected n=8 seed, so k0=6 and |V|=|U|=v=25.
Every seed edge and its two normalized labels persist at all k>=6 by L410.
Put a=4^-6.
Then for every k>=6 and every seed x in V,c in U,

    a c_k(0)<=a_k(x)<=c_k(0),
    a c_k(0)<=b_k(c)<=c_k(0).                          (2)

These bounds use ALL later endpoint representations.
For the upper bounds, binary endpoint autocorrelation gives nu_k(z)<=nu_k(0)=p_k for every z; sign symmetry also identifies nu_k(beta^k x)=K^k(x,0) for the original chronological kernel K.
For each seed x, choose any actual length-six tail word witnessing c_6(beta^6 x)>0 and negate and reverse its digits to get an original chronological length-six path from x to zero.
Its probability is at least4^-6=a.
Concatenating that fixed path with an arbitrary length-(k-6) return gives K^k(x,0)>=a p_(k-6)>=a p_k.
For each seed c, prepend an arbitrary length-(k-6) return to a fixed chronological length-six word reaching c (reverse a word witnessing c_6(c)>0); this gives K^k(0,c)>=a p_(k-6)>=a p_k.
Both comparisons use the actual monotonicity p_(k-6)>=p_k.
Multiplying by4^k proves (2), with no conditional fiber probability or harmonic-ratio limit assumed.

Each normalized left vertex has at most one neighbor for each middle word, and conversely for each right vertex.
The sum of w(theta) over all81 middle words is exactly(1+2+1)^4=C.
The global autocorrelation upper bound therefore gives, at every actual vertex,

    r_k(x)<=C a_k(x)c_k(0),
    h_k(c)<=C b_k(c)c_k(0),
    pi_k(x)<=C t_k.                                    (3)

The last bound is global, not restricted to V.
For each x in V at least one seed edge remains, so (2) and w(theta)>=1 give

    a^2 t_k<=pi_k(x)<=C t_k,
    v a^2 t_k<=M_k:=pi_k(V)<=min(1,v C t_k).            (4)

Thus every persistent seed vertex has uniformly comparable complete-fiber weight, but its absolute original probability carries the common factor t_k.

<a id="seed-original-conductance"></a>
## 2. Actual two-step conductances and a uniform reflected seed estimate

C170's two-step left-endpoint kernel has nonloop conductance

    c_k(x,x')=pi_k(x)T_k(x,x')
             =(1/S_k) sum_c W_k(x,c)W_k(x',c)/h_k(c).   (5)

If x,x' in V share a seed right neighbor c in U, then their corresponding middle words have weights at least1.
Using (2)--(3) on this one term proves

    c_k(x,x')>=a^3 t_k/C.                              (6)

Indeed the numerator after cancellation of one b_k(c) is
 a_k(x)a_k(x')b_k(c)w(theta)w(theta')/[S_k sum_z a_k(z)w(theta_z)],
whose remaining sum is at most C c_k(0).
No multiplicity from other newly available right neighbors is subtracted.

The left two-step graph generated by common right neighbors in the connected seed is connected.
Fix any spanning tree of that finite graph and its simple paths between ordered seed vertices; their length is at most L=v-1=24, and no edge is repeated.
This is a path choice on the already verified finite seed, not a claim about an uncomputed graph.
All chosen edges satisfy (6) at every later k.

Reflect the full T_k onto V by replacing transitions leaving V by self-loops.
The resulting kernel has stationary probability pi_k^V(x)=pi_k(x)/M_k and internal edge conductance c_k(x,x')/M_k.
By (4)--(6) every chosen tree edge has conditional conductance at least a^3/(v C^2).
The ordered-pair path-Cauchy argument therefore gives, for every real f on V,

    Var_(pi_k^V)(f)<=[L v C^2/(2a^3)] D_(T_k reflected to V)(f)
                    for every k>=6.                    (7)

This is a proved uniform finite-patch coefficient in the actual complete-fiber weights.
It neither replaces the original stationary law by a uniform law nor asserts positive original mass for V.
Reflection is used only to state this local estimate; it is not a replacement of the full operator in L410.

<a id="seed-path-load-and-mass"></a>
## 3. Original path load and the precise retained-pair mass

For the full endpoint law choose G_k=(V times V) union {(x,x):x any actual vertex}.
Use the fixed tree paths on V and empty paths on the other diagonal pairs.
With the exact load convention of L410, every used edge has

    Load_k(e)<= L M_k^2/(2 c_k(e))
              <=[L C/(2a^3)] M_k^2/t_k
              <=[L v^2 C^3/(2a^3)] t_k.               (8)

All unused edges have zero load.
The selected original product mass is exactly

    (pi_k tensor pi_k)(G_k)
       =M_k^2+sum_(x outside V)pi_k(x)^2
       <=v^2 C^2 t_k^2+C t_k.                         (9)

The diagonal contribution in(9) uses the global upper bound (3) and total mass1.
It must not be silently discarded when evaluating the bad-pair defect.

The original overlap D_k=p_(2k)/p_k^2 satisfies D_k>=1.
Since a length-four polynomial has degree below deg P, its only returned word is0^4 and p_4=2^-4=1/16.
Original collision monotonicity and concatenation of a2k return with a4 return give

    p_(2k)/16<=p_(2k+4)<=p_(2k),
    1/(256 D_k)<=t_k<=1/(16 D_k)<=1/16.               (10)

Thus (8) supplies the explicit UNIFORM original-load bound

    Load_k(e)<= L v^2 C^3/(32a^3) for all k>=6.        (11)

This proves the load half of L410's partial-path test for the concrete fixed-seed mechanism.
The discarded-mass half remains a separate expense: the finite-patch coefficient does not certify that G_k carries more than one half of the original product law.

<a id="seed-fixed-support-boundary"></a>
## 4. What this finite-block mechanism does and does not settle

Equations (4) and(10) prove that the original probability of the COMPLETE seed endpoint set is comparable, with fixed positive explicit constants, to1/D_k.
Unlike L410's specified zero-word padding, this conclusion includes every later full-word representation of its labels.
If the actual mean is infinite, L329 supplies a common subsequence k_j tending to infinity with D_(k_j) tending to infinity.
Along that subsequence (9) gives

    (pi_(k_j) tensor pi_(k_j))(G_(k_j))->0.             (12)

Hence the fixed hub mechanism would omit asymptotically all original product pairs on the null branch despite its proved uniformly bounded path load.
This is a conditional obstruction to that concrete mechanism, not a proof that the actual mean is infinite.

Conversely, finite mean makes D_k converge to mu, and (4),(10) give an eventual positive original mass for this fixed seed.
No claim that this lower mass exceeds the amount required for defect below1/4 follows from these constants.
Thus even finite mean alone does not validate this PARTICULAR seed as a sufficient bulk hub.
The present result does not propose positive seed mass as a replacement mean criterion; it proves the actual complete-fiber and conductance estimates and identifies their precise remaining mass cost.

The all-late question now requires paths serving a growing collection of endpoints, or a direct control of the omitted product mass together with its paid conductances.
Fixed-endpoint path probabilities in(2) are explicit for the seed but need not remain bounded below for endpoints escaping it.
No translated-seed uniformity, all-state ratio bound, growing-patch construction or new numerical test is asserted here.

<a id="seed-inputs-and-author-limits"></a>
## Exact inputs and completed author boundary

| Input | Actual role |
| --- | --- |
| [C170 weighted endpoint reduction](Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix), [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Exact original endpoint weights, two-step conductances and complete fiber law; no uniform contraction is borrowed. |
| [J106 complete six-case results](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results), [R412](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) | Only actual n8 connected seed,25 vertices per side and141 edges; no larger length computed, no spectral numerical estimate used. |
| [L410 induced nesting](Yin_C_G0514_v2.md#nested-normalized-carry-support) | All later original seed edges and normalized labels persist; this alone supplied no complete-fiber weight comparison. |
| [L410 partial paths](Yin_C_G0514_v2.md#partial-path-weighted-carry-target), [R414](../audits/reviews/Yin_R_G0414_v1.md#bulk-carry-whole-independent-finding) | Actual ordered-pair load convention, bad mass threshold and distinction from the unproved all-late bulk condition. |
| [L329 original law](Yin_C_G0204_v1.md#actual-midpoint-occupation-reuse), [mean equivalence](Yin_C_G0204_v1.md#complete-midpoint-tightness-test) | Complete autocorrelation domination nu_k(z)<=p_k, D_k>=1 and the finite-mean/overlap equivalence. |
| [L329 null-branch subsequence](Yin_C_G0204_v1.md#null-branch-original-bridge-escape) | Infinite mean would supply D_(k_j) tending to infinity, not an assertion of the actual mean branch or an all-time divergence. |
| [C169 collision monotonicity](Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Original p_l is nonincreasing; its large-block gap is not transferred. |
| [C76 original paid paths](Yin_C_G0076_v1.md#statement) | Earlier path-Cauchy mechanism only; its different six-digit graph and explicit word paths are not assumed to connect these endpoint states. |

The author checked the ascending versus chronological digit reversal, original length-six probability floor, arbitrary-return concatenations, both complete-count upper bounds, weighted middle sum256, actual conductance cancellation, reflected stationary normalization, all ordered-pair factors, diagonal-pair mass, p_4=1/16 and both directions of the t_k bounds.
The new proven result is a uniform all-fiber estimate and paid path construction on this one concrete fixed hub.
The remaining mass expense is explicit rather than assumed or replaced by unweighted connectivity.
Root supplied only the open question; entropy_attainment_bridge supplied all new mathematics here.
The earlier C170/J106 authorship and their separate independent reviews remain disclosed above.
No numerical execution, new source theorem, fixed adoption or actual critical-mean decision is asserted.
