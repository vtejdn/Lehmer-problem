---
author: Yin
---

# Actual first-deviation costs beyond shortest distance nine

Human author Yin.
Contributor original_signed_asymptotic developed the shortest-path normalization, accumulated excess-cost operator, complete-level certificate and distinct exact author verification.
Root supplied the raw geodesic/nongeodesic resolvent formulation and clarified the distinction between excepting starting states and changing the operator by finite-core killing or resummation.
The current adopted assessment is [the whole-reviewed decision](#decision-whole-reviewed-2026-10-28), selecting [independent mathematical/native R1053](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding).

## Statement

Fix P(t)=t^4-t^3-t^2-t+1, its exterior root beta, upper neutral root zeta and actual order O=Z[beta].
Write x_+,x_- for the beta and beta^(-1) embeddings, rho(x)=|x(zeta)|, b=1/(beta-1), and s=beta b.
Use the complete original accessible/coaccessible core

    D={x in O: |x_+|<b, |x_-|<s}.

The original digit weights are pi_(-1)=pi_1=1/4 and pi_0=1/2.
Let P_D(x,y)=pi_e when y=beta x+e belongs to D, and zero otherwise.
Let B_0 be P_D restricted to D_0=D minus{0}, killed on entry into zero without row renormalization.
Let R be the true radius of the complete original return series and R_f the radius of its complete first-return series.
Set

    t0=68883/40000,
    m0=36193899689180879400344643/
       26214400000000000000000000 > 69/50 > 1.           (GD1)

The adopted C796 input gives R>t0.

<a id="shortest-first-deviation-definition"></a>
**Definition (shortest-word normalization and first-deviation operator).**
Let d(x) be the minimum original word length from x to zero, with d(0)=0.
It is finite on D by the adopted whole-core co-return theorem.
Let M(x) be the sum of the ORIGINAL product probabilities of all words of length d(x) from x to zero, with M(0)=1.
For nonzero x these are exactly the shortest first-hit words, and M(x) is positive rational.
Every legal edge from nonzero x has d(y)>=d(x)-1.
Call it geodesic when equality holds and nongeodesic otherwise.
On D_0 define

    A(x,y)=P_D(x,y) if d(y)=d(x)-1, and0 otherwise,
    B_ng(x,y)=P_D(x,y) if d(y)>=d(x), and0 otherwise,
    B_0=A+B_ng.                                         (GD2)

For t>0 put g_t(x)=t^(d(x))M(x), including g_t(0)=1.
Let Hcal_t(x) be the complete original first-hit series at t, allowing infinity, with Hcal_t(0)=1.
For 0<t<R_f this is the actual finite canonical H_t of C511.
No finiteness outside that interval is assumed.
The locally finite geodesic unrolling is

    E_t f(x)=sum_(j=0)^(d(x)-1)t^j(A^j f)(x), x in D_0.

It is the pointwise finite sum denoted(I-tA)^(-1), not a bounded-operator inverse assertion.
Writing a_0(x)=P_D(x,0), one has

    g_t=t E_t a_0,
    Hcal_t=g_t+E_t t B_ng Hcal_t.                        (GD3)

Every expression involving Hcal_t is interpreted through extended nonnegative word sums.
The actual normalized first-deviation operator is

    G_0(x,y)=pi_e M(y)/M(x) on geodesic edges in D_0,
    D_t(x,y)=pi_e M(y)/M(x)t^(1+d(y)-d(x))
             on nongeodesic edges in D_0,
    T_t=diag(g_t)^(-1)E_t t B_ng diag(g_t)
       =sum_(j>=0)G_0^j D_t.                            (GD4)

Each row of that sum stops at j=d(x)-1 and is finite.
Adding the terminal transition to zero makes the geodesic chain stochastic; it hits zero after exactly d(x) steps from x.
Every exponent in D_t is a positive integer.
Consequently the full accumulated row cost c_t(x)=(T_t 1)(x), with c_t(0)=0, is a polynomial in t with nonnegative rational coefficients.
Put delta_t(x)=(D_t 1)(x).
Then

    c_t(x)=delta_t(x)+sum_(geodesic x->y)
                              pi_e M(y)c_t(y)/M(x).     (GD5)

The sum may include zero with c_t(0)=0.
It charges the entire geodesic continuation, not merely the current-row delta_t.
There is also an exact complete-word identity

    Hcal_t(x)/g_t(x)=sum_(k>=0)(T_t^k 1)(x),             (GD6)

allowing infinity.
The kth term collects exactly first-hit words with k nongeodesic edges.
All original probabilities and chronological lengths are retained.

For EVERY t>=t0 and EVERY actual x with d(x)>=9,

    c_t(x)>=m0>69/50.                                   (GD7)

The exact minimum of c_(t0) on the complete distance-nine level is m0.
For any t>=R, any finite exceptional set F of STARTING states and any q<1, the inequality c_t(x)<=q therefore cannot hold for every x in D_0 outside F.
This excludes an unweighted subunit-row budget for the SAME full T_t at infinity.
It does not assert unbounded c_t, a spectral-radius conclusion, failure of a weighted operator estimate, or either critical-mean or first-return-radius branch.
Killing intermediate or terminal contributions at a finite core, stopping geodesic unrolling there, or resumming its detours changes the operator; GD7 supplies no conclusion for those changed costs.

## Exact inputs and reuse

[C400](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) supplies the actual strict-core equality, with the fixed quartic's C399 co-return certificate scope retained.
[C590](Yin_C_G0590_v1.md#decision-complete-isolated-whole-adoption) supplies actual whole-core termination, rho<=d<=A_D rho+B_D with fixed paid constants, and unbounded actual radii.
Only these deterministic facts are used; no random mean upper bound is imported.
[C511](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) supplies the complete first-hit interpretation and its finite interior domain0<t<R_f.
[C796](Yin_C_G0796_v1.md#decision-whole-reviewed-2026-10-26) supplies R>t0, used only to specialize GD7 to true critical and supercritical parameters.
The [J52 exact certificate](../computations/programs/Yin_J_G0052/readme.md#geodesic-first-deviation-cost) supplies the complete level-nine list and five polynomials below, with retained native input/output and a distinct author verification.

The bounded reuse check found the general first-hit decomposition in C511, the finite spatial-resolvent method in C590, and the forced-central-clock comparison in [C593 v2](Yin_C_G0593_v2.md#central-count-complete-clock-comparison).
They do not supply this shortest-distance normalized cost or its complete-level lower bound.
The elementary finite unrolling and nonnegative word partition are written out below, without invoking a general countable-operator theorem or claiming priority for a resolvent identity.

## Complete argument

### Shortest words and locally finite normalization

A shortest word from nonzero x first hits zero at its last step, since an earlier hit would give a shorter continuation.
There are finitely many such words and all original weights are positive, so M(x)>0 is finite rational.
Prepending a legal edge to a shortest continuation from y gives d(x)<=1+d(y).
The first edge of a shortest continuation attains equality.
Conversely, any geodesic edge followed by a shortest continuation gives a shortest continuation from x.
Hence for x!=0,

    M(x)=sum_(geodesic x->y)pi_e M(y).                   (GD8)

All shortest-word multiplicities are retained.
A geodesic word from x to zero has exactly d(x) steps, and A^j has zero row at x for j>=d(x), since A kills arrival at zero.
Its complete original mass is M(x), proving t E_t a_0=g_t.
Unrolling the first-step equation along geodesic edges until zero or the first nongeodesic edge proves GD3.
Each such expansion is finite, even if the remaining first-hit series is infinite.

Normalizing a geodesic edge by t g_t(y)/g_t(x) cancels t because d(y)=d(x)-1.
This gives G_0.
On a nongeodesic edge it gives the positive integer exponent e(x,y)=1+d(y)-d(x)>=1 and the entry D_t.
Products along geodesic prefixes telescope, proving the normalized operator formula GD4.
By GD8, pi_e M(y)/M(x), including the terminal edge to zero when d(x)=1, sums to one.
It defines a finite-length auxiliary geodesic sampling law used to evaluate the retained original weights; it is not substituted for the actual critical Q.
Under that auxiliary law,

    c_t(x)=E_geo,x[sum_(j=0)^(d(x)-1)delta_t(X_j)].      (GD9)

This proves GD5 and explicitly retains every geodesic-prefix cost.
A bound on delta_t at the initial row alone would not control c_t.
All sums here are finite at each starting state, with no global uniformity or integrability assumption.

### Unique complete-word decomposition and paid clock

Every finite original first-hit word splits uniquely into blocks consisting of a geodesic prefix and one nongeodesic edge, followed by a final geodesic continuation to zero.
A normalized block from x to z contributes its full original word probability times t to its full length and the factor g_t(z)/g_t(x).
These endpoint factors telescope across successive blocks.
The terminal geodesic word mass is g_t at its starting state.
Grouping the nonnegative original word sum by the number of nongeodesic edges proves GD6, including possible infinity.
No signed interchange, analytic continuation, bounded inverse or uniform convergence premise is used.

For a first-hit word of chronological length L, telescoping the distance gives

    L-d(x)=sum_(all edges)(1+d(next)-d(current))
          =sum_(nongeodesic edges)e(current,next).       (GD10)

Geodesic terms vanish.
The powers in the normalized operator therefore charge exactly the excess length over d(x); the baseline t^(d(x)) in g_t restores the full t^L.
The number of blocks is never substituted for the original time.

### The complete distance-nine certificate

The entire distance-nine level consists of the following five sign pairs.
Each displayed polynomial is the EXACT full c_t, not a truncated contribution.
Sign reversal preserves original probabilities, d, M and edge classification; the verifier also checked both signs explicitly.
Tuples use ascending powers(1,beta,beta^2,beta^3).

| Representative, with both signs included | Exact c_t |
| --- | --- |
| (-2,-1,3,-1) | t^3/2+3t^4/128+t^5/256+t^7/2048 |
| (-1,-3,2,0) | t/4+3t^3/32+3t^4/64+t^5/256 |
| (-1,0,-3,2) | 7t^3/32+t^4/32+t^5/256+t^7/4096 |
| (0,-2,3,-1) | t/4+3t^3/32+9t^4/128+t^5/256 |
| (0,-1,2,-1) | 13t^3/64+t^4/32+t^5/256+t^7/4096 |

For every n<=9, a word from x to zero determines x=-sum_(j=1)^n e_j beta^(-j).
The distinct author verifier enumerates EVERY such word directly, using generic polynomial reduction and beta^(-1)=1+beta+beta^2-beta^3.
It tests actual strict-core membership by certified rational intervals, keeps the least n for each endpoint, and sums every shortest word's original weight.
This gives exactly57 states with d<=9 and precisely the ten listed states at d=9, without a neutral-radius cutoff.
A word ending at zero from an actual accessible state has all intermediate states in the actual core; the verifier additionally checks the used shortest paths.
The proof uses C400's equality with the strict strip, not an enlarged real projection.

Those57 states together with all their legal successors form a required target set of73 states.
Their largest shortest distance is15.
The verifier constructs unrestricted forward endpoint sums for split halves of length at most8; the largest half-word endpoint set has2901 states.
For every target x and n<=15, writing n=a+b, it tests the complete weighted equation

    beta^n x+beta^b S_a+S_b=0.

Products of integer word-weight numerators give the exact original mass with denominator4^n.
The first nonzero length certifies d(x), and its numerator certifies M(x).
Any earlier hit of zero would already have appeared at a smaller length.
This independently checks all73 required distances and masses, including every nongeodesic target used in the five polynomials.
No unknown-target term occurs in these costs.

For each level-nine state, the verifier then averages the sum of local delta_t polynomials over EVERY shortest word with exact conditional weight p(word)/M(x).
This evaluates GD9 by explicit paths, independently of the author's distance-DAG fold.
It reproduces the five displayed polynomials exactly and verifies

    min_(d(x)=9)c_(t0)(x)=m0>69/50.                     (GD11)

The minimum at t0 occurs at the sign pair represented by(-1,-3,2,0).
No claim that this pair minimizes for every larger t is needed.

### Propagation to the whole infinite tail

Fix t>=t0 and x with d(x)=n>=9.
Each c_t is nondecreasing in t because its polynomial coefficients are nonnegative.
The auxiliary geodesic chain reaches distance9 after exactly n-9 steps.
Splitting the finite expectation GD9 there leaves nonnegative earlier costs and the conditional remaining expectation c_t at the distance-nine state.
Therefore

    c_t(x)>=E_geo,x[c_t(X_(n-9))]
           >=min_(d(y)=9)c_t(y)
           >=min_(d(y)=9)c_(t0)(y)=m0.                 (GD12)

This proves GD7 on the entire actual core, without extrapolating finite observations at distances10 through24.
The set d<=8 is finite because each state is determined by a word of length at most8.
The actual core has unbounded rho and d>=rho, so states with d>=9 escape every finite set.
Because R>t0, an unweighted bound c_t<=q<1 outside finitely many STARTING states is impossible for every t>=R.

The lower bound can come from costs incurred near the terminal low-distance part of the geodesic path.
Excepting finitely many initial rows does not remove these contributions from other rows of the unchanged T_t.
Killing a block on entrance to a finite core, dropping possible intermediate or terminal contributions, or resumming that core changes the operator and its cost recursion.
GD12 cannot be transferred to those changed costs without a new proof.
It implies neither unboundedness nor a spectral-radius lower bound, and does not preclude a suitable weighted operator estimate.
No critical-mean or first-return-radius classification follows.
A useful continuation must explicitly pay finite-core coupling or detour resummation instead of discarding these terminal costs.

## Native reproduction and checking scope

The coherent native group is [J52](../computations/programs/Yin_J_G0052/readme.md#geodesic-first-deviation-cost).
The author [reverse BFS](../computations/programs/Yin_J_G0052/shortest_first_hit.py) completed depth24 under100000-state/120-second bounds, with417 states, exact rational core tests, complete shortest masses and explicitly unknown successors where appropriate.
The [DAG fold](../computations/programs/Yin_J_G0052/geodesic_detour_cost.py) used only those existing states and distinguished exact costs from lower bounds obtained by omitting unknown positive terms.
Only the exact complete-level-nine certificate is a numerical input to GD7.
The [distinct verifier](../computations/programs/Yin_J_G0052/verify_geodesic_level9.py) imports no BFS or DAG-fold routine.
It uses the direct/split-word and explicit-shortest-path methods above, with the separate generic polynomial/rational-interval routines in [verify_shortest_witness.py](../computations/programs/Yin_J_G0052/verify_shortest_witness.py).
Its rational root interval is explicitly refined from43/25<beta<173/100, with endpoint signs and a positive derivative bound checked.
An unresolved strict-core comparison would fail rather than use a floating decision.

The initial data (`mathematics/computations/outputs/Yin_J_G0052/shortest_first_hit_24.json`), fold data (`mathematics/computations/outputs/Yin_J_G0052/geodesic_detour_cost_24.json`) and complete level-nine verification (`mathematics/computations/outputs/Yin_J_G0052/geodesic_level9_check.json`) retain the actual reproduction inputs and certificate.
All three calculations completed at their declared scopes.
The distinct word verification required73 targets of distance at most15 and halves of length at most8, with no larger actual-core graph.
The distinct-method checks described above were authored during proof development.
The later whole independent mathematical/native inspection and decisive reproduction are recorded in [R1053](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding); neither scope is a theorem for changing algebraic inputs.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-28)

## Assessment history

### Decision first-deviation-open

| Field | Value |
| --- | --- |
| date | 2026-10-28T18:22 |
| status | open |
| reason | Fix the complete author GD1--GD12 proof and exact complete-level-nine certificate: unchanged full first-deviation cost is at least m0>69/50 for every d>=9 and t>=t0. Whole independent review and adoption remain outstanding. Finite-core killing/resummation changes the operator; no unboundedness, spectral, weighted-operator, mean or first-return-radius conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire actual quartic/original law, complete shortest d/M, locally finite unrolling and normalized operator, extended word identity, exact level-nine minimum, every d>=9 and t>=t0, and unchanged-operator limitations. |
| argument | [Complete GD1--GD12 proof](#complete-argument) | Full geodesic masses, normalized first-deviation blocks and chronological excess, complete finite certificate coverage, distinct direct/split-word check, nonnegative-cost propagation and finite-starting-state versus changed-operator scope. |
| dependency | [Actual complete strict core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed quartic actual order/embeddings and equality of the strict strip with the accessible/coaccessible core; C399 certificate scope retained. |
| dependency | [Whole-core deterministic termination](Yin_C_G0590_v1.md#decision-complete-isolated-whole-adoption) | Finite actual continuations, rho<=d<=A_D rho+B_D with paid constants, and unbounded actual radii; no random mean bound. |
| dependency | [Canonical first-hit interpretation](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Complete original first-hit series and finite positivity for0<t<R_f; outside that domain only extended nonnegative word identities are used. |
| dependency | [True critical lower bound](Yin_C_G0796_v1.md#decision-whole-reviewed-2026-10-26) | Only R>68883/40000=t0 for the true critical/supercritical specialization. |
| support | [Exact complete-level certificate](../computations/programs/Yin_J_G0052/readme.md#geodesic-first-deviation-cost) | Complete10-state level9 list,73 required d/M values through15, five exact cost polynomials and rational minimum; retained native evidence and distinct author verification, without independent-agent review. |

### Decision whole-reviewed-2026-10-28

| Field | Value |
| --- | --- |
| date | 2026-10-28T18:33 |
| status | proved |
| reason | Adopt the unchanged complete first-deviation theorem after whole independent mathematical/native R1053 and responsible inspection of the entire fixed statement and GD1--GD12 proof. The reviewer reproduced the complete decisive level-nine certificate, all73 required shortest distances/masses and five exact cost polynomials, and checked every chronological factor and all-distance propagation step. The lower bound concerns the SAME full operator outside finitely many starting states; finite-core stopping, killing, resummation and weighted estimates remain open. No mean, first-return-radius or unrestricted G0001 conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Entire actual quartic/original law, complete shortest d/M, locally finite unrolling and normalized operator, extended word identity, exact level-nine minimum, every d>=9 and t>=t0, and unchanged-operator limitations. |
| argument | [Complete GD1--GD12 proof](#complete-argument) | Full geodesic masses, normalized first-deviation blocks and chronological excess, complete finite certificate coverage, distinct direct/split-word check, nonnegative-cost propagation and finite-starting-state versus changed-operator scope. |
| dependency | [Actual complete strict core](Yin_C_G0400_v1.md#decision-complete-isolated-whole-adoption) | Fixed quartic actual order/embeddings and equality of the strict strip with the accessible/coaccessible core; C399 certificate scope retained. |
| dependency | [Whole-core deterministic termination](Yin_C_G0590_v1.md#decision-complete-isolated-whole-adoption) | Finite actual continuations, rho<=d<=A_D rho+B_D with paid constants, and unbounded actual radii; no random mean bound. |
| dependency | [Canonical first-hit interpretation](Yin_C_G0511_v1.md#decision-complete-current-self-adoption) | Complete original first-hit series and finite positivity for0<t<R_f; outside that domain only extended nonnegative word identities are used. |
| dependency | [True critical lower bound](Yin_C_G0796_v1.md#decision-whole-reviewed-2026-10-26) | Only R>68883/40000=t0 for the true critical/supercritical specialization. |
| support | [Exact complete-level certificate](../computations/programs/Yin_J_G0052/readme.md#geodesic-first-deviation-cost) | Complete10-state level9 list,73 required d/M values through15, five exact cost polynomials and rational minimum; retained native evidence and distinct author verification, without independent-agent review. |
| review | [Whole independent mathematical/native R1053](../audits/reviews/Yin_R_G1053_v1.md#whole-first-deviation-finding) | Entire statement and GD1--GD12 proof, four adopted interfaces, full decisive certificate reproduction and direct polynomial/minimum reconciliation, exact unchanged-operator and global limits. |

