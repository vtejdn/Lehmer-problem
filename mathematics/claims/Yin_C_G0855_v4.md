---
author: Yin
---
# Disconnected branch cuts and the original Salem capacity cost

This fixed result serves the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
It asks whether changing the admissible compact cuts for the original square-root function can remove the radial-hull capacity cost in [C855 v3](../claims/Yin_C_G0855_v3.md#decision-whole-independent-review-2026-11-04).
The scope below is a finite embedded graph of compact arcs containing every original branch point, with each branch point's connected component containing another branch point.
The coordinating research agent developed the argument for Yin, and the selected assessment adopts its independent whole review at the exact scope below.


## Retained versions and current revision

[C855 v3](Yin_C_G0855_v3.md#decision-whole-independent-review-2026-11-04) retains its adopted radial-hull estimates and independent review.
[C855 v2](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04) retains its separately adopted universal raw p=2 bound and original upper contour comparison.
[C855 v1](Yin_C_G0855_v1.md#statement) retains its unassessed restricted statement and earlier limits.
The present version extends the geometric lower-bound question to disconnected finite-graph cuts and all stated prime rotation collections.
It neither replaces those earlier arguments nor adopts a new total-Mahler conclusion.
<a id="disconnected-cut-capacity"></a>
## Statement

Let P be the minimal polynomial of an actual Salem number lambda=exp(m), with degree d>=4 and 0<m<=1.
Write P_k(X)=product_i(X-alpha_i^k) for k=2,4, using all original conjugates.
Use either S={0}, with its single rotation equal to one, or an odd prime q and S=F_q^* or F_q, with zeta a primitive q-th root of unity.
Put s=|S| and

    A(X)=product_(j in S) product_i (X-zeta^j alpha_i^2)(X-zeta^j alpha_i^4),
    n=2ds, N=2s(d-2), L0=log(2 exp(4)).                         (DC1)

Let K be a compact finite graph made of finitely many compact piecewise smooth arcs, containing all n roots of A.
Require that the connected component of every root contains at least one other root of A.
The same argument covers a larger compact set containing such a graph by monotonicity.
There is an absolute D0 such that, for every such actual input with d>=D0, every permitted S and every such K,

    log cap(K) >= m^2/log d.                                   (DC2)

For S={0}, the stronger bound

    log cap(K) >= 3m^2/[log(4/m)+5]                            (DC3)

holds once d is sufficiently large, uniformly in the stated actual Salem class.
Neither threshold is numerically evaluated.
The estimates concern the compact geometric envelope, not a lower bound on Hankel determinants.
They do not establish a positive total Mahler gap.

## Capacity and arithmetic interfaces

For a probability measure nu of finite logarithmic energy, write

    I(nu)=integral integral log(1/|z-w|) dnu(z)dnu(w).

Only the trial-measure direction log cap(K)>=-I(nu) is needed, in the same capacity normalization as [C855 v2](../claims/Yin_C_G0855_v2.md#argument).
It follows directly from the accepted capacity/transfinite-diameter identity: for k independent samples from nu, the expected logarithm of their Vandermonde product is -k(k-1)I(nu)/2, so the maximum product on K is at least the exponential of that expectation.
Taking its power 2/[k(k-1)] and then the transfinite-diameter limit proves the inequality.
All measures below have finite energy, making the expectation well defined; the logarithm is bounded above on a compact set and its negative part is integrable.
For an interval of length l, its arcsine measure has energy log(4/l).
Indeed write its points as l(1+cos theta)/2, use cos theta-cos phi=-2 sin((theta+phi)/2)sin((theta-phi)/2), and use the circle logarithmic mean integral log|1-exp(it)| dt/(2pi)=0 to compute its constant potential on the interval.
Thus no additional equilibrium-measure theorem is a premise of the argument.
The finite discrepancy input is only the accepted statement of [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), with its existing source-proof limits.
The arithmetic input is the numerical Dobrowolski consequence at [C147 v5](../claims/Yin_C_G0147_v5.md#reuse-and-source-scope), as explicitly used in [C855 v3 SH6](../claims/Yin_C_G0855_v3.md#the-accepted-arithmetic-lower-bound-fixes-the-order-of-the-error):

    m >= (1/2400)(log log d/log d)^3, d>=55.                    (DC4)

No separate external aggregate-separation theorem is used in the proof below.
A bounded source search located the Davenport-Mahler literature, but the matching argument below supplies the needed weaker estimate directly and makes no novelty claim.

## A discriminant bound for all nearest separations

Let B be any monic squarefree integer polynomial of degree n>=2, with roots b_1,...,b_n and total logarithmic Mahler measure h=log M(B).
Set delta_i=min_(j!=i)|b_i-b_j|.
Then

    sum_i log^+(1/delta_i) <= 26n log n +52n h.                (DC5)

To prove this, choose one nearest neighbor of each point.
At most six different points can choose the same neighbor: for two incoming segments of lengths r>=t, nearest-neighbor minimality gives |u-v|>=r, hence their angle has cosine at most t/(2r)<=1/2.
Seven pairwise angular separations of at least pi/3 cannot fit around the center.
The underlying simple undirected graph consequently has maximum degree at most seven.
A greedy edge coloring uses at most thirteen colors, each color being a matching.
Every undirected edge is counted at most twice in the directed nearest-neighbor sum.

Fix a matching E consisting only of edges of length less than one.
In the Vandermonde matrix (b_i^k), 0<=k<n, replace one row of each pair (u,v) by its difference with the other, divided by v-u.
This divides the determinant by product_E(v-u).
An unchanged row has Euclidean norm at most sqrt(n) max(1,|u|)^(n-1).
A divided-difference row has norm at most n^(3/2) max(1,|u|,|v|)^(n-1), since (v^k-u^k)/(v-u)=sum_(l=0)^(k-1)v^(k-1-l)u^l.
For a matched pair, the product of these bounds is at most n^2[max(1,|u|)max(1,|v|)]^(2(n-1)).
Hadamard's inequality and the nonzero integer discriminant give

    1 <= |Vandermonde(B)|
      <= product_E|u-v| n^(n/2+|E|) M(B)^(2(n-1)).

As |E|<=n/2, each matching contributes at most n log n+2n h to the sum of inverse-distance logarithms.
Thirteen matchings and the multiplicity at most two prove (DC5).

## Local measures on an actual cut

If a root b_i lies in a component with another root, choose a path in the finite graph to such a root and stop it at its first exit from the disk of radius r_i around b_i, where

    r_i=min(m,delta_i)/(8n), 0<m<=1.                           (DC6)

The stopped path stays in that closed disk and joins two points at distance r_i.
Orthogonal projection onto their joining line covers an interval of length r_i.
Choose a Borel section of this projection on the path and push the interval's arcsine measure forward.
Such a section can be obtained by taking the first path-parameter at each projected level; its level sets show measurability.
Distances do not decrease under this lift from the projected interval, so the resulting probability measure nu_i satisfies

    supp nu_i subset K intersect closed_disk(b_i,r_i),
    I(nu_i) <= log(4/r_i).                                   (DC7)

For distinct roots, r_i+r_j<=|b_i-b_j|/(4n).
Consequently the mutual energy of nu_i and nu_j is at most log(1/|b_i-b_j|)+1/(2n), using -log(1-x)<=2x for x<=1/2.
The min(m,delta_i) in (DC6) also gives

    log(4/r_i) <= log(32n/m)+log^+(1/delta_i).                 (DC8)

## Neutral-root energy for the original rotated polynomial

Every positive power of a Salem root has degree d, and no two distinct conjugates have a root-of-unity quotient, by the unique expanding-conjugate argument retained in C855 v3.
The squared and fourth-power orbits are disjoint because their positive absolute Weil heights differ.
The polynomial A in (DC1) therefore has n distinct roots.
Its root set is Galois stable, including the rotations, so A is monic with integer coefficients.
Its total measure is h=6sm, and all its roots have modulus at most exp(4).
Exactly N roots lie on the unit circle; the other 4s are the four real-radius orbits.

Let nu_0 be the average of the local nu_i over the N neutral roots.
The complete ordered off-diagonal sum is -log|disc A|<=0.
Removing the ordered pairs involving an off-circle root increases this sum by at most

    [8sN+4s(4s-1)] L0,

because every root distance is at most 2 exp(4).
Combining this fact with (DC5), (DC7) and (DC8) gives

    I(nu_0)<=epsilon,
    epsilon=[N log(32n/m)+26n log n+312ns m
             +(8sN+4s(4s-1))L0]/N^2+1/(2n).                 (DC9)

Since N=n(1-2/d)>=n/2 and s>=1, this implies uniformly over all permitted s

    epsilon=O((log d+log(1/m)+m+1)/d).                       (DC10)

Here log n/n<=log(2d)/(2d), because n>=2d>=8 and log x/x decreases on that range.
The term 312ns m/N^2 is O(m/d), so a growing conductor has not been hidden in the constant.

## A uniformly negative mutual potential outside the circle

Fix an outer root a=exp(4m) zeta^j.
Any other root of A has distance at least 2m from a if its radius is different, and at least 4/q if it has the same radius and a different q-th-root rotation.
In the single-rotation case use r=m; otherwise use r=min(m,1/q).
There is a stopped path in K from a to distance r, contained in its closed r-disk, and a measure nu_1 there with

    I(nu_1)<=L=log(4/r).                                    (DC11)

Every z in this disk satisfies |z|>=exp(4m)-m>=exp(3m), because exp(3m)(exp(m)-1)>=m.
It also satisfies |z|<=exp(4)+1.
Thus its distance from the unit circle is at least 3m.

The following compact Lipschitz test makes the discrepancy use explicit.
Let chi(w)=min(1,max(0,exp(4)+1-|w|)), let R=exp(4)+1, let C0=log(2 exp(4)+3), and put

    phi_z(w)=chi(w) log max(m,|z-w|),
    B_m=log(1/m)+C0, C1=2+C0.

The test has support in |w|<=R, absolute value at most B_m, and global Lipschitz constant at most C1/m.
Indeed the truncated logarithm is 1/m-Lipschitz, while the cutoff term is bounded by B_m and m log(1/m)<=1/e.
At every root of A and on the unit circle the cutoff is one.
At neutral roots and on the circle the logarithm is untruncated.
Its circle mean is log|z| by the elementary harmonic mean-value identity.
For n>=55, Pri11, applied to the actual degree n and total measure 6sm, gives discrepancy at most

    Delta=(C1/m)(2R+1) sqrt(max(log n,6sm)/n).                (DC12)

Remove the 4s off-circle roots from this empirical average and renormalize.
The resulting neutral-root mean differs from log|z| by at most 2Delta+(4s/N)(B_m+5), because n/N<=2 and |log|z||<=5.
Moving a neutral root into its local support changes log|z-w| by at most 1/n: its displacement is at most m/(8n), while the original distance is at least 3m.
Therefore

    I(nu_0,nu_1)<=-3m+eta,
    eta=2Delta+(4s/N)(B_m+5)+1/n.                           (DC13)

This bound is uniform over the entire support of nu_1, not only the central root.
Also max(log n/n,6sm/n)<=max(log(2d)/(2d),3m/d), so no conductor factor remains in eta.

## The energy mixture and the single-rotation conclusion

Suppose eta<=m, so (DC13) is at most -2m.
For t=2m/(L+4m+epsilon), which lies in (0,1), the probability measure nu=(1-t)nu_0+t nu_1 has

    I(nu)<=epsilon-4m^2/(L+4m+epsilon),
    log cap(K)>=4m^2/(L+4m+epsilon)-epsilon.                 (DC14)

This follows by expanding the three energy terms; the exact expansion at this t has the additional nonpositive term -4m epsilon/(L+4m+epsilon).
For s=1, L=log(4/m).
If epsilon<=m^2/(L+5), then epsilon<=1, L+4m+epsilon<=L+5, and (DC14) proves (DC3).
The arithmetic lower bound (DC4) makes eta/m tend to zero and epsilon(L+5)/m^2 tend to zero uniformly over actual inputs with d tending to infinity and 0<m<=1.
Indeed (DC10)--(DC13) involve only inverse powers of d multiplied by fixed powers of log d, 1/m and log(1/m), while (DC4) bounds 1/m by a fixed power of log d.
This proves the stated uniform eventual conditions, without assuming a particular near-one sequence exists.

## All prime rotation collections

If q<=d, the same one-root measure has

    L=log 4+max(log(1/m),log q)<=2 log d

for all sufficiently large actual d, by (DC4).
Uniformly in this range, eta<=m, epsilon<=1, L+4m+epsilon<=3 log d and epsilon<=m^2/(3 log d) eventually.
Equation (DC14) then gives (DC2).

If q>=d, use every outer root a_j=exp(4m)zeta^j for j in S.
Around each take a stopped path of radius r_*=min(m,1/q)/(8q) and a local probability measure of energy at most log(4/r_*).
Let nu_out be the average of these s measures.
The centers have mutual distance at least 4/q, and the total displacement of a pair is at most 1/(4q^2).
Their mutual energy exceeds the central logarithmic energy by at most 1/(8q).
For S=F_q, the ordered logarithmic distance sum of the unscaled roots is q log q, from the derivative of X^q-1 at its roots.
For S=F_q^*, it is (q-2)log q: remove the pairs with 1 and use product_(j=1)^(q-1)|1-zeta^j|=q.
Both sums are nonnegative and can be dropped for an upper energy estimate.
Scaling the centers by exp(4m) consequently gives

    I(nu_out)<=-4m+4m/s
        +[log(32q)+max(log(1/m),log q)]/s+1/(8q).            (DC15)

For q>=d and sufficiently large actual d, (DC4) gives q>=1/m.
The positive error in (DC15) is O(log q/q)=O(log d/d)=o(m), uniformly over q>=d, using s>=q-1.
Thus I(nu_out)<=-2m, and log cap(K)>=2m>=m^2/log d.
Together with the small-q case, this completes the author argument for (DC2).

## Relation to the original trace and what remains open

For an original nonempty-mask orbit trace, the union of used positions is {0}, F_q^* or F_q.
Every root in (DC1) is a genuine branch point of that trace: local continuation changes the sign of precisely the radical basis terms whose mask contains its position, and their nonempty sum cannot vanish by the original quadratic-class independence.
This is the private-branch argument already retained in [C860 v7](../claims/Yin_C_G0860_v7.md#componentwise-pole-rank).
If a finite graph K is an admissible compact cut for the trace and a component contains exactly one branch point, a small boundary around that component yields its nontrivial local monodromy, contradicting single-valued continuation off K.
Thus the component hypothesis used above is necessary for such admissible finite-graph cuts.
This argument does not classify arbitrary pathological compact sets, meromorphic charts on covers, or non-capacity determinant estimates.

On a hypothetical actual Salem near-one sequence, (DC2) gives uniformly over these cuts and rotations

    log cap(K)/(log d/d) >= d m^2/(log d)^2 -> infinity.       (DC16)

The last limit follows from (DC4).
Consequently optimizing finite-graph branch cuts cannot reduce this geometric envelope to O(log d/d), the scale available from the stated controlled-depth arithmetic certificates.
This does not upper-bound actual determinant valuations, rule out better joint arithmetic, or resolve the unrestricted Task.
The statement and argument retain their exact finite-graph, actual-input and source-interface scope.

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T23:49 |
| status | proved |
| reason | Adopt complete DC1--DC16 after independent R1086 v3: every stated original Salem finite-graph cut satisfying the root-component condition retains the displayed positive capacity cost, uniformly over all stated prime rotation collections; the single-rotation strengthening and exact entire-complement trace application are included. External source statements retain their actual inspection limits. This is an envelope bound, not a determinant lower bound or an unrestricted Mahler-gap result; earlier versions retain their separate adopted scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact finite-graph statement](#disconnected-cut-capacity) | Entire DC1--DC3, all actual Salem inputs beyond an absolute degree threshold, single and prime rotation collections, graph root-component hypothesis and monotonicity extension. |
| argument | [Complete capacity argument](#capacity-and-arithmetic-interfaces) | Complete trial-measure proof, DC4--DC16, nearest-separation matching, local graph measures, neutral discrepancy, both conductor regimes and exact trace/contour limits. |
| dependency | [Capacity normalization](Yin_C_G0855_v2.md#sources-and-proof-interfaces) | Accepted classical capacity/transfinite-diameter identity and Dim19 scope; the new energy direction is proved directly in this version. |
| dependency | [Original degree and powers](Yin_C_G0855_v3.md#the-mesh-estimate-uses-the-actual-integral-squared-polynomial) | Unique expanding Salem conjugate, power preservation and no torsion quotient, applied at the original input. |
| dependency | [Numerical arithmetic interface](Yin_C_G0147_v5.md#reuse-and-source-scope) | Only accepted Smy08 equation (11) and its 1/2400 total-measure consequence; no cyclic-norm theorem or new original-proof audit. |
| dependency | [Original trace branches](Yin_C_G0860_v7.md#componentwise-pole-rank) | Private original branch points and independence over C(x), with C858's adopted input and no new Padé review. |
| support | [Pri11 quantitative discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Exact Theorem 3.1/(3.2), simple original rotated integer polynomial, actual degree and total measure, compact global Lipschitz test and retained source-proof limits. |
| support | [Smy08 numerical statement](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact numerical statement, total-height normalization and exclusion of the defective resultant explanation and uninspected original proof. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1086_v3.md#disconnected-salem-cut-whole) | Entire DC1--DC16, uniform conductor bounds, actual inputs and exact finite-graph/entire-complement trace application, with no numerical threshold evaluation, determinant lower bound or G0001 completion. |

## Current assessment

[Selected decision](#decision-whole-independent-review-2026-11-04)
