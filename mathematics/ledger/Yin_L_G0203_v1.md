---
author: Yin
---

# Bounded-measure interlaced realizations with unbounded irreducible degree

Date: 2026-10-10.

<a id="bounded-measure-interlaced-fixed-scope"></a>
## Adopted scope

The coordinating AI for Yin retains orbit_research's complete pendant-chain proof and resultant_research's complete separate noncontributor review.
The review discloses its author's earlier L175 contribution.
J42 retains the necessary author program and mathematical output; the reviewer reran all fourteen actual matrices with output intercepted in memory and reproduced every saved mathematical field.

Appending a unit-edge path to a fixed interlaced core yields explicit complete reciprocal determinants with fixed entry height3 and bounded total Mahler measure.
Each contains exactly two nonreal expanding roots and has a unique positive-measure reciprocal irreducible factor.
Those factors are pairwise distinct, hence have unbounded degree, and lie outside the real trace-matrix subclass.
The entire cyclotomic multiplier remains inside the actual determinant.
The complete absolute-cover factor, all exterior roots, uniform cost bounds, positive limits and linear dimension/entry-energy costs are retained.

The Salem-Boyd sequence form and general exterior-root/convergence mechanism are classical and attributed to the inspected published Hir06 source.
The actual plus-sign matrix recurrence and particular seed/root/cost statements have the full local proof below.
No universal target prescription or all-k irreducibility of the complete determinant is claimed.
Positive coefficients exclude every positive-real Salem target from this particular family, and its logarithmic measure stays above log4.
Unrestricted realization and small-total-measure coverage remain open; G0001 is active and unresolved.

The full author proof and complete review follow.
Historical pending-review text preserves chronology; the appended review determines the adopted review scope.
Only heading depth and relative navigation are transformed.

<a id="retained-pendant-chain-proof"></a>
## Coupled interlaced realizations at increasing degree

Date: 2026-10-10.
Starting question: Test coupled interlaced integral upper-unitriangular realizations on independently specified degree-six-or-higher reciprocal inputs, and track full original/absolute-cover measure and every allowed neutral factor.
Develop an actual variable-degree mechanism or its precise obstruction beyond L196 growing-measure quartics.

The full unrestricted Task remains active and unresolved.

### Current construction and reuse boundary

The changed mechanism attaches an arbitrarily long unit-edge pendant chain to the fixed interlaced rank-four matrix from [L196](Yin_L_G0196_v1.md#interlaced-realization-fixed-scope).
This grows degree at fixed entry height and bounded full Mahler measure, rather than increasing the four core weights.
It does not yet prescribe an arbitrary reciprocal target.
The explicit degree-six member below is irreducible and has nonreal trace roots; the whole family will be kept, including all possible neutral factors.
Continuing exact algebra checks belong to [J42](../computations/programs/Yin_J_G0042/readme.md).

The local reuse screen read L196, D9's full signed-cover identity, L184's ordered cycle/attached-path calculations and L179's elementary averaging scope.
A primary search located Eriko Hironaka, *Salem-Boyd sequences and Hopf plumbing*, Osaka Journal of Mathematics43(3) (2006),497--516, now retained as [Hir06](../audits/literature/Hir06/readme.md).
The published introduction, Theorems1/3 and determinant convention on pp.497--500 were text-read, followed by Section3.1's Lemmas10--11 and Theorem12 on pp.505--506.
These identify the established Salem-Boyd sequence form and exterior-root/convergence argument; the topological convention uses det(tS-S^T), so no topological sign/convention transfer is assumed.
The [source reading](../audits/literature/Hir06/readme.md) keeps the complete inspected scope and excluded proof claims.
The argument below derives the actual plus-sign determinant directly and writes out the elementary root argument at its no-circle-zero scope.
No historical novelty is claimed for path recurrences, the sequence form or its general measure-convergence phenomenon.

<a id="pendant-chain-full-determinant"></a>
### 1. Exact chain transfer and the fixed cubic numerators

For an integral upper-unitriangular core V of rank d and vertex v, let p=det(tV+V^T) and q be the principal-deletion determinant at v.
Append k vertices after the core, with strict-upper entry1 between v and the first new vertex and between successive new vertices, and no other new entries.
Write p_k for the full polynomial, p_0=p.
Expanding at the last leaf gives

    p_1=(t+1)p-tq,
    p_(k+1)=(t+1)p_k-t p_(k-1).

The factor t is the product of the two opposite entries of tV+V^T.
If C_k=1+t+...+t^k and C_(-1)=0, induction gives

    p_k=C_k p-t C_(k-1)q,
    (t-1)p_k=t^(k+1)(p-q)-(p-tq).                 (1)

Since p is reciprocal of degree d and q of degree d-1, reversal at degree d gives (p-q)^*=p-tq.
The constant terms of p and q are both1, so p-q is divisible by t.
This exact cancellation must be retained when naming the smaller seed polynomial; reversal is always taken at its actual stated degree.

Use the fixed core

    V=[[1,2,0,-2],[0,1,3,0],[0,0,1,2],[0,0,0,1]],

and attach at vertex2.
Its polynomial is p=t^4+7t^3+16t^2+7t+1.
Deleting vertex2 leaves a three-vertex path with squared edge sum8, hence

    q=(t+1)^3-8t(t+1)=t^3-5t^2-5t+1.

Consequently p-q=t H and the entire chain determinant is

    H=t^3+6t^2+21t+12,
    p_k=(t^(k+2)H-H^*)/(t-1),     k>=0.           (2)

All matrices have rank k+4, every diagonal one, maximum entry3 and squared strict-upper sum k+21.
Their determinant is precisely p_k: there is no extra unlisted multiplier or extraction of a preferred factor.
The division in(2) removes the explicit factor t-1 in the displayed numerator; it is an identity for the complete determinant, not a modification of the realization.

For the absolute presentation, replace every strict-upper entry by its negative magnitude.
The core polynomial becomes r=t^4-41t^3+16t^2-41t+1.
Its vertex2 deletion remains q, since it is a tree and only squared weights occur.
The same leaf recurrence therefore gives

    J=t^3-42t^2+21t-36,
    r_k=(t^(k+2)J-J^*)/(t-1).                    (3)

D9's full signed double cover has rank2k+8, maximum entry3, squared strict-upper sum2k+42 and complete determinant p_k r_k.
Its total logarithmic Mahler measure is m(p_k)+m(r_k).
Both terms and every factor remain in the analysis; the absolute factor is not called neutral.

<a id="degree-six-interlaced-chain-control"></a>
### 2. An irreducible degree-six control outside the real-trace class

For k=2, direct expansion of(2) gives

    p_2=t^6+7t^5+28t^4+40t^3+28t^2+7t+1,
    t^(-3)p_2=U(t+t^(-1)),
    U(u)=u^3+7u^2+25u+26.                         (4)

The derivative U'=3u^2+14u+25 has negative discriminant and is positive everywhere.
Its unique real root lies in(-2,-1), since U(-2)=-4 and U(-1)=7.
Every rational root of this monic cubic would be an integer, impossible in that interval.
Thus U is irreducible and has two nonreal roots.
In the cubic field generated by any root, one real embedding makes u^2-4 negative, so it is not a square.
The quadratic lift t^2-u t+1 is irreducible and proves p_2 irreducible of degree six.
Its root configuration is one unit-circle pair and two nonreal expanding roots with their two contracting reciprocals.
In particular it cannot divide a real block-Gram determinant, even after cyclotomic multiplication.
This is an exact higher-degree realization, but its coefficients are produced by the stated chain construction rather than an arbitrary prescribed-input algorithm.

<a id="bounded-measure-chain-root-control"></a>
### 3. All exterior roots, without discarding circle factors

We use the elementary root argument recorded in Hir06 Lemmas10--11 at the following sufficient scope.
If a fixed monic real polynomial F has no zero on the unit circle and N>=1, then

    Q_N=t^N F-F^*

has no more roots strictly outside the unit circle, counted with multiplicity, than F.
To see this, for0<=e<1 compare t^N F and e F^* on the circle.
Their moduli differ strictly because |F^*|=|F| there.
Rouche gives the same number of interior roots as t^N F, hence exactly the exterior count of F.
Let e tend to1.
Any roots strictly exterior at e=1 persist in disjoint exterior disks for nearby e, so their number cannot increase at the limit.
Also each exterior root of F attracts its full multiplicity of roots of Q_N as N tends to infinity: on a sufficiently small exterior disk, F^*/t^N tends uniformly to zero and Rouche applies to F-F^*/t^N.
These arguments supply the needed bounds and convergence, without an interchange of singular logarithmic integrals or a claim about topological realizations.

For H, the derivative is3((t+2)^2+3)>0.
Its unique real root is-alpha with

    2/3<alpha<3/4,

as the two rational endpoint evaluations show.
The other roots are a complex-conjugate pair of modulus sqrt(12/alpha)>4.
In particular H has no circle root and exactly two exterior roots.
The preceding bound proves that p_k has at most two exterior roots for every k, since dividing by t-1 only removes a circle root.

In fact both are nonreal and have modulus greater than2 for every k.
Put N=k+2.
On |t|=2,

    |H(t)|>(2-3/4)(4-2)^2=5,
    |H^*(t)|<=1+6*2+21*4+12*8=193.

For N>=6, 2^N*5>193.
Rouche therefore gives exactly two roots of Q_N outside radius2.
No such root is real.
For positive t>1, t^2 H-H^*=(t-1)p_0>0 and H>0, so t^N H-H^*>0.
For t=-r, r>=2, one has

    H(-r)<0,    H^*(-r)<0,
    |H(-r)|=r((r-3)^2+12)-12>=6r,
    |H^*(-r)|=12r^3-21r^2+6r-1<=(27/2)r^3.

When N is odd, Q_N(-r)>0.
When N is even and N>=4,

    |H^*(-r)|/|H(-r)|<=(9/4)r^2<r^N,

so Q_N(-r)<0.
This excludes both real half-lines beyond radius2 in the N>=6 argument.

The four smaller N are exact controls.
For k=0, the two trace roots satisfy u^2+7u+14=0; for k=1,

    p_1=(t+1)(t^4+6t^3+22t^2+6t+1),

and the nontrivial traces satisfy u^2+6u+20=0.
Their moduli are sqrt14 and sqrt20.
For k=2 use(4): its real trace lies in(-2,-1), so the other two traces have modulus greater than sqrt13.
For k=3,

    p_3=(t+1)(t^6+6t^5+22t^4+18t^3+22t^2+6t+1),
    U_3(u)=u^3+6u^2+19u+6.

Here U_3' is positive everywhere and its real root is in(-1/2,0); the two nonreal trace roots have modulus greater than sqrt12.
All four lower bounds exceed5/2.
If a trace u comes from a root with1<=|t|<=2, then |u|<=|t|+|t|^(-1)<=5/2.
Thus the nonreal traces in all four controls produce two conjugate roots outside radius2.
The exterior upper count already proved is two, so every p_k has exactly this pair; its reciprocals are the only strictly contracting roots and all remaining k roots are on the unit circle.
In particular

    m(p_k)=2 log R_k>log4,                         (5)

where R_k>2 is the modulus of either expanding root.
This formula retains all roots; the other roots contribute zero rather than being deleted.

For J, exact discriminant calculation gives-9391248, so it has one real root rho and a nonreal conjugate pair.
The evaluations J(41)<0<J(42) imply41<rho<42.
The pair has squared modulus36/rho<1, by the constant term.
Thus J has no unit-circle root and exactly one exterior root.
The elementary bound gives at most one for r_k.
Differentiating its numerator at1 gives

    r_k(1)=(k+2)J(1)+J'(1)-(J^*)'(1)
          =-56k-64<0.

Since r_k is monic, it has a positive real root rho_k>1.
This is its unique exterior root, counted with multiplicity; reciprocity gives its sole contracting root and puts every other root on the circle.
Consequently the exact entire extra cost is

    m(r_k)=log rho_k.                              (6)

No irreducibility or complete cyclotomic classification of r_k is used to obtain(6).

<a id="bounded-measure-interlaced-factor-coverage"></a>
### 4. Distinct positive irreducible inputs at unbounded degree

Each p_k has a unique positive-measure monic irreducible factor F_k, occurring once.
Indeed any rational irreducible factor containing one nonreal expanding root also contains its conjugate.
Every monic integral factor has constant term plus or minus1 because p_k does.
To have absolute norm1 it must therefore also contain both contracting roots: the two expanding moduli are R_k and the two possible contracting moduli are R_k^(-1), while all other root moduli are1.
A factor with only one contracting root would have product modulus R_k, not1.
Thus the same irreducible factor contains all four off-circle roots.
Its reciprocal shares a root with it, proving reciprocity after monic normalization.
Its constant term is1: all its roots occur in reciprocal pairs, and it has no rational unit-circle root.
Every other irreducible factor is cyclotomic by the usual monic integral all-roots-on-the-circle criterion.
We retain the complete factorization in the form

    p_k=F_k C_k,
    C_k a product of all cyclotomic factors with multiplicities,
    m(F_k)=m(p_k),   deg C_k=k+4-deg F_k,   0<=deg C_k<=k.       (7)

The full explicit polynomial(2) is always the realized determinant.
No general formula for the individual cyclotomic orders or for deg C_k is claimed.
Equation(7) records the actual whole multiplier, its exact degree identity and its proved bound; it is not an assertion that C_k=1 or that all k circle roots are cyclotomic.
For k=2, the proof in Section2 gives F_2=p_2 and C_2=1.
For odd k, t+1 divides p_k and is included in C_k.

The F_k are pairwise distinct.
H is irreducible: its unique real root lies strictly between-1 and0 and hence is not an integer, excluding a rational root of the monic cubic.
Also gcd(H,H^*)=1, since these irreducible cubics cannot be scalar multiples (their leading/constant coefficients are1,12 and12,1).
If a common nonzero root z of p_k and p_l existed outside the circle, equations(2) would give H(z)!=0 and z^(k-l)=1, impossible when k!=l.
More generally all common roots of two different p_k are roots of unity.
Hence their positive irreducible factors are distinct.

Their degrees are unbounded.
Section5 below gives a common Mahler upper bound.
For a monic degree-e polynomial with measure at most M, every coefficient is bounded by binomial(e,j) M, by the elementary symmetric-function formula and product max(1,|root|).
If the degrees of infinitely many F_k were bounded, only finitely many integral coefficient lists would be possible, contradicting distinctness.
This proves unbounded degree, not that deg F_k=k+4 or that the neutral degree in(7) stays bounded.

Thus this is a concrete family of distinct reciprocal irreducible inputs with nonreal trace roots, unbounded degree, bounded positive measure and actual integral upper-unitriangular realizations after their entire retained cyclotomic cofactors.
Such F_k cannot divide a real block-Gram determinant under any further cyclotomic stabilization, by the same nonreal-trace test as L196.
The new coverage is precisely this constructed family, not independently prescribable coefficients or unrestricted small-measure units.

<a id="pendant-chain-complete-cost-and-obstruction"></a>
### 5. Complete costs, limits and a decisive coverage boundary

On the unit circle |t^N H-H^*|<=2|H|.
The complete logarithmic integral and m(t-1)=0 yield

    m(p_k)<=m(H)+log2=log(24/alpha)<log36,
    m(r_k)<=m(J)+log2=log(2rho)<log84.             (8)

The possible numerator zeros are finite and have integrable logarithms; the pointwise upper bound suffices for these inequalities.
No bounded-away-from-zero assertion for the numerators is being used.
Together with(5), all original measures lie in(log4,log36).
The total signed-cover measure is exactly2log R_k+log rho_k and is less than log3024.
Its extra/original ratio is bounded by log84/log4 at every k, at this already uniformly positive-measure scope.

The exterior-root convergence argument in Section3, applied in disjoint small disks around the two exterior roots of H and the one exterior root of J, gives

    R_k -> sqrt(12/alpha),   rho_k -> rho,
    m(p_k) -> log(12/alpha),   m(r_k) -> log rho,
    m(r_k)/m(p_k) -> log rho/log(12/alpha).         (9)

The exterior counts are exact for every k, so no extra uncontrolled root contributions are hidden in these limits.
The argument does not claim an effective convergence rate or monotonicity.
The limits are positive: log16<log(12/alpha)<log18 and log41<log rho<log42.
The presentation degree grows, its entry height stays3, and its squared-entry cost grows linearly.
The unknown individual cyclotomic degree remains explicitly(7); normalizing by dimension would change the measure being studied.

There is a sharp limitation against arbitrary prescribed inputs.
For k>=2, the whole polynomial has the coefficient formula, with d=k+4,

    p_k=1+7t+28t^2+40 sum_(i=3)^(d-3)t^i
             +28t^(d-2)+7t^(d-1)+t^d.            (10)

The k=0,1 formulas also have strictly positive coefficients.
Therefore no p_k has a positive real root.
The independently specified degree-six Salem polynomial t^6-t^5-t^3-t+1, the original Lehmer polynomial, and every Salem polynomial with a positive expanding root cannot divide any p_k, regardless of which cyclotomic multiplier is allowed.
This is an exact obstruction for this fixed chain family, not for all interlaced unitriangular matrices.
The positive coefficients and fixed numerator explain why bounded measure at increasing degree does not supply near-one coverage.

There is also a general coefficient-prescription caution: adding a unit-edge leaf preserves the coefficient immediately below the leading term.
From p_new=(t+1)p-tq, with q monic of degree d-1, the new coefficient is(a+1)-1=a if the old one was a.
Repeated unit-leaf additions cannot independently change this trace coefficient.
The higher-degree control in(4) is a valid realized irreducible polynomial; it is not a solution of an arbitrary target-coefficient problem.
A next changed mechanism would need multiple independent couplings or adjustable core data while retaining bounded measure and all costs.
No such extension is claimed here.

### 6. Executed checks, contribution and review boundary

[J42](../computations/programs/Yin_J_G0042/readme.md) constructs the actual original and absolute integer matrices for k=0,...,6 and independently computes the characteristic polynomial of -V^(-1)V^T, checking it against(2)--(3).
It checks unit diagonals, both entry/energy costs, reciprocity, the explicit degree-six irreducibility and trace data, and the seed discriminants and rational root endpoint signs.
These exact finite checks supplement the written all-k proofs; they are not extrapolated into those proofs.
No mathematical program failure or larger scan occurred.

The selected Hir06 comparison was acquired through the source writer after checking the declared flat PDF destination and existing identity.
Its source-local reading record and sole registry retain the published artifact and actual inspection limits.
The general Salem-Boyd form, exterior-root bound and convergence are established background; the new local contribution is this explicit interlaced plus-sign realization, exact cubic pair, all-k root exclusion and full factor/cost/coverage analysis.
The coordinator assigned only the broad question and supplied no derivation.
Earlier L196/D9/L184 inputs retain their original contributions and reviews.
The author derived and checked every new formula and wrote/executed the exact J42 certificate; complete noncontributor review and fixed adoption remain pending.

The current result moves from L196's fixed-degree growing-measure examples to a family of pairwise distinct positive reciprocal irreducible factors with unbounded degree, bounded measure, fixed presentation entry height and completely retained neutral/absolute factors.
It also proves that this particular positive-coefficient family cannot supply Salem targets or approach measure one.
Unrestricted integral realization, uniform small-measure cover costs and the full G0001 gap remain unresolved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0102_v1.md#complete-separate-noncontributor-review), with its original inspected scope and relationship.
