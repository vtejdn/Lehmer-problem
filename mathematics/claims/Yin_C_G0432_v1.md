---
author: Yin
---
# Complete covariance-minor grid and actual-core return costs

The complete original L255 theorem and every necessary geometric proof, exact control and input-dependent cost are retained here.
L255 preserves original investigation/source/contribution history and fixed old review inputs.
No Task/E execution resumes.

## Statement

Use the original independent digits eta_j with probabilities1/4,1/2,1/4 on-1,0,1.
For every algebraic integer alpha and N>=1, let mu_N(z)=Pr(sum_(j<N)eta_j alpha^j=z), p_N=mu_N(0)>0 and tau_0 be its real neutral Minkowski map, with each real neutral place once and both Cartesian coordinates of one representative of each complex neutral pair.
Set q=r_0+2s_0, v_j=tau_0(alpha^j) and C_N=sum_(j<N)v_jv_j^T.
Then the full joint endpoint law satisfies equations2--3, including support in range C_N and the inverse-on-range Gaussian when C_N is singular.
C_N is twice the unconditioned covariance, not a conditional covariance.

For every integer q>=1, every real positive-semidefinite q-by-q C, all lengths h_i>0 and all translations c, set g_C(w)=exp(-w^T C^+w/2) on range C and zero outside, with g_0(0)=1.
For half-open coordinate cells G_k=product_i[k_i h_i,(k_i+1)h_i),

    sum_(k in Z^q) sup_(x in G_k)g_C(x-c)<=B_h(C),
    B_h(C)=sum_I 2^(q-|I|)(2pi)^(|I|/2)
                         sqrt(det C_I)product_(i in I)h_i^-1,
    B_h(C)<=product_i[2+sqrt(2pi C_ii)/h_i].

The subset sum includes det C_empty=1 and all zero/singular minors.
It follows from the exact coordinate-box expansion5 for every NONEMPTY compact convex set, projected-ellipsoid volume6 and nonnegative Gaussian layer integration; no coordinate independence, covariance invertibility or lattice-covolume substitution is assumed.

For every algebraic UNIT alpha, use its actual zero-to-zero original core D_act in Z[alpha], K_act on complex counting-measure l2(D_act), nonneutral radii/factor C_non in8, neutral lengths1 at real places and1/sqrt2 at complex Cartesian coordinates, and orthogonal multiplication O_N by alpha^N on those neutral coordinates.
For every N>=1, retain BOTH row and rotated-column profiles:

    p_N<=||K_act^N||
       <=C_non sqrt[B_h(C_N)B_h(O_N^T C_N O_N)]p_N
       <=E_N p_N,
    E_N=C_non[2+sqrt(2pi N)]^q, ||K_act||<=1.

For q=0 the neutral factor is one, so E_N=C_non.
Every real/complex place, singular early covariance, translation, fixed input and original clock remains in the bound, with no phase-separation or waiting-time premise.
For all integers n>=0,

    p_n<=min{1,(E_N p_N)^floor(n/N)},
    0<=-log p_N/N-h_2(alpha)<=log E_N/N.

A retained original same-time return entry b with separately proved omitted fraction epsilon in(0,1) gives p_N<=b/(1-epsilon) and the block bound13, paying all state enumeration and relative-error costs.
An arbitrary finite retained entry is not thereby complete.

For the actual quartic P=t^4-t^3-t^2-t+1, the complete existing p64=121338835637214357477/2^121 and C_non<259/8 yield

    p_n<=2^[-40 floor(n/64)] for EVERY integer n>=0,
    h_2(beta)>=5log2/8.

This is a fully charged fixed-input consequence, not a new return enumeration or an optimized rate.
For every d=2^r>=2 and alpha=exp(pi i/d), the actual irreducible torsion input t^d+1 at N=d has C_d=(d/2)I_d, p_d=2^-d and full actual-core norm ||K_act^d||=1.
The ENTIRE principal-minor sum is [2+sqrt(2pi d)]^d, exceeding the true norm/return ratio by the factor[1+sqrt(pi d/2)]^d.
This locates a limitation of this sufficient coordinate-grid certificate, not a failure of the bound or a no-go theorem for sharper actual-order estimates or nontorsion Salem inputs.
All nonneutral/degree/time/relative-error costs and the varying Salem comparison19 remain explicit.
No positive-theta analogue, actual new covariance independence, uniform near-one estimate or unrestricted gap is proved.

<a id="argument"></a>
## Complete argument

### Exact existing original-law and actual-core inputs

The full original Sections1--7/equations1--19 follow, retaining all singular, translation, dimension, time, cutoff, control and source limits.
Their active-task and prospective-investigation language records the original2026-10-10 chronology; no Task/E or research/source execution resumes.
The original proof/contribution/self-check/freeze and old R154 input remain fixed in L255.

The adequate existing [C419 finite endpoint inequality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) applies to every integer column list and every real coefficient observable with the ORIGINAL iid three-point digits.
At exact endpoint z, applying it to r_j=u dot tau_0(alpha^j) gives mu_N(z)exp(u dot tau_0(z))<=p_N exp(u^T C_N u/2).
No conditional independence, martingale or changed probability law is used.

For a unit, let D_act consist exactly of states lying on finite original paths from zero back to zero under x->alpha*x+eta, and let K_act be that kernel restricted to D_act.
A path between core endpoints stays in the core by attaching its two zero endpaths.
Thus K_act^N(0,0)=p_N.
Each digit acts by a restricted partial permutation on Z[alpha], so its counting-l2 norm is at most one; their probability-weighted sum gives ||K_act||<=1.
The complete past/future nonneutral bounds, one-point-per-full-Minkowski-cell injection and the unchanged full-space Schur argument are proved in [C419's actual-core input](Yin_C_G0419_v1.md#gaussian-full-state-norm-sandwich).
Sections3--4 below replace its old isotropic envelope with the full covariance geometry while preserving its precise actual core and Hilbert space.

The complete existing [C419 quartic certificate input](Yin_C_G0419_v1.md#relative-truncation-complete-original-block-certificate) retains p64, the proved C_non<259/8 and the same-time original return/box boundary.
Its [actual dyadic-cyclotomic core and norm proof](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits), including reachability/co-returnability of the entire order and cube-indicator norm one, is used only for the exact torsion control in Section6.
Neither comparison is a new J52 execution, source-proof reading or adopted near-one statement.

<a id="covariance-grid-reuse-boundary"></a>
### 1. Reuse, actual law and the changed geometric question

The current Task/continuing execution gate and [L251](../ledger/Yin_L_G0251_v1.md#original-conditional-gaussian-fixed-scope) were read.
Its exact original Fourier inequality, zero-atom normalization, full-core counting-l2 operator, translated norm-grid injection and nonneutral constants are reused at their complete reviewed scopes.
The complete quartic finite return is the prior [L243](../ledger/Yin_L_G0243_v1.md#finite-box-salem-experiment-fixed-scope) certificate; no J52 execution or modification is made.
A local screen also read [L120's actual central covariance warning](../ledger/Yin_L_G0120_v1.md#central-whitening-fourier-test) and L147 Sections7--8: its phase-separated sampling and Fejer Gramian estimates pay an explicit phase/time cost on their specified family.
They are related geometric precedents, not the argument used below.

The changed question is whether an anisotropic Gaussian can be summed over the actual norm grid without first replacing its covariance by kappa*N times the identity.
A coordinate-by-coordinate bound on each point cannot be multiplied independently, since all conjugates use the same digits.
Instead the proof below counts Gaussian SUPERLEVEL ellipsoids, expands their volumes after addition of a coordinate box, and integrates every projected volume.
This preserves covariance dependencies, including singular covariance.
It removes a degree-dependent kappa factor without a phase-separation hypothesis or a waiting time.
It does not optimize an observable modulo endpoint row-space functionals; root's simultaneous D123 question is separate and is not a premise or a contribution here.

All new derivations here are by structural_research for Yin.
The coordinator supplied only the broad question and material allocation.
The needed convex-coordinate extrusion and ellipsoid-volume identities are proved below at their exact scope, with no new external theorem adoption or literature-priority claim.
There is no new computation group or proposed numerical scan.
G0001 remains active and unresolved; author self-review and later independent review are distinct.

<a id="complete-neutral-covariance-profile"></a>
### 2. The full original covariance profile, including singular cases

Use the original independent digits eta_j with mu(0)=1/2, mu(+/-1)=1/4.
For an actual algebraic integer alpha, let mu_N(z) be the complete displacement law of sum_(j<N) eta_j alpha^j and p_N=mu_N(0).
Let tau_0 be the REAL neutral Minkowski map: each real neutral place once, and the real and imaginary coordinates of one representative of each complex neutral pair.
Its dimension is q=r_0+2s_0.
Put

    v_j=tau_0(alpha^j),
    C_N=sum_(j=0)^(N-1) v_j v_j^T.                        (1)

This is the deterministic matrix governing the proved exponential-moment proxy, twice the actual unconditioned covariance.
It is not the conditional covariance and is not presumed scalar.
For every real u in R^q, L251's endpoint inequality gives

    exp(u dot tau_0(z)) mu_N(z)
                    <=p_N exp(u^T C_N u/2).              (2)

This is the ORIGINAL full law at the endpoint z, not a positive-theta law or a return-conditioned projection argument.
If tau_0(z) is not in the range of C_N, choose a vector in its kernel with nonzero dot product and scale it in(2); then mu_N(z)=0.
On its range, diagonalize the real symmetric positive-semidefinite C_N and optimize each positive eigenvalue coordinate.
With C_N^+ the inverse on that range and zero on its orthogonal complement, this proves

    mu_N(z)<=p_N g_(C_N)(tau_0(z)),
    g_C(w)=exp(-w^T C^+w/2) if w in range C,
           0 otherwise.                                 (3)

The zero-rank case means g_0=1 at0 and zero elsewhere.
No determinant inverse is taken in a singular direction.
For each complex place, the sum of its two diagonal entries of C_N is EXACTLY N.
At a real neutral place its diagonal entry is N.
These elementary identities follow from modulus one, regardless of resonances or correlations between places.

<a id="ellipsoid-coordinate-box-volume"></a>
### 3. A complete weighted grid bound from projected ellipsoid volumes

Fix q>=1, any real positive-semidefinite q-by-q matrix C, coordinate grid lengths h_i>0 and any center c in R^q.
Write G_k=product_i[k_i h_i,(k_i+1)h_i), k in Z^q.
For I a subset of the q coordinates, C_I is the corresponding principal submatrix; det C_empty=1.
The assertion is

    sum_(k in Z^q) sup_(x in G_k) g_C(x-c)
       <=B_h(C),
    B_h(C)=sum_(I subset {1,...,q})
        2^(q-|I|) (2pi)^(|I|/2) sqrt(det C_I)
                         product_(i in I) h_i^(-1).      (4)

Every summand is nonnegative and the finite right side is valid even when C has deficient rank.
The assertion is uniform in the translation c.
The proof uses full geometric dependence; it does not multiply separate marginal probability bounds.

First prove the exact coordinate-box expansion.
If K is a compact convex set in R^q, and a_i>=0, then

    vol_q(K+product_i[-a_i,a_i])
       =sum_I vol_(|I|)(projection_I K)
                           product_(j notin I)2a_j.       (5)

The convention for the nonempty K at I=empty is vol_0=1.
For a single segment in direction e_j, each nonempty fiber over projection onto the other coordinates is a closed interval, possibly a point.
Adding [-a_j,a_j] extends its length by2a_j.
Fubini gives the original q-volume plus2a_j times that (q-1)-dimensional projection volume.
This includes lower-dimensional K: fibers of zero length still gain2a_j, and lower-dimensional projections have zero ambient volume as appropriate.
Repeat this identity for the q coordinate segments.
Projection commutes with the remaining coordinate additions, so expansion produces every subset I exactly once and proves(5).
This proof also covers zero a_i by continuity or direct omission of that segment.

For t>0 the closed superlevel ellipsoid of g_C is

    E_t={C^(1/2)y: ||y||_2<=sqrt(2t)}.

It lies in range C if C is singular.
Its projection onto I is the ellipsoid with matrix C_I.
Thus its |I|-dimensional volume is

    vol_(|I|)(projection_I E_t)
       =omega_(|I|)(2t)^(|I|/2) sqrt(det C_I),
    omega_k=pi^(k/2)/Gamma(1+k/2), omega_0=1.             (6)

For singular C_I this is zero when |I|>0: the projected ellipsoid has lower dimension.
To verify the formula without a regularity assumption, the projected linear map has Gram C_I; an orthogonal singular-value decomposition turns the image into a ball with axes equal to its singular values.
Its volume is the unit-ball volume times their product.
The familiar unit-ball constant in(6) follows by evaluating the product Gaussian integral in Cartesian and polar coordinates.
No lattice covolume is being equated with this continuous volume.

For a fixed level t, count grid cells with sup_(G_k) g_C(x-c)>exp(-t).
Each such cell contains some point of c+E_t.
The union of these disjoint half-open cells is contained in

    c+E_t+product_i[-h_i,h_i].

Indeed, any two points in one cell differ by less than h_i in coordinate i.
Its total volume is the number of cells times product_i h_i.
For compact E_t only finitely many cells occur.
Therefore (5)--(6), divided by the cell volume, bound that number by

    sum_I 2^(q-|I|) omega_(|I|)(2t)^(|I|/2)
                   sqrt(det C_I) product_(i in I)h_i^(-1).

Strict superlevels avoid any issue of a supremum attained only on a grid boundary.
For each cell value b in[0,1], b=integral_0^infinity exp(-t)1_(b>exp(-t))dt.
Sum and integrate by nonnegativity.
The elementary gamma integral

    integral_0^infinity exp(-t)t^(k/2)dt=Gamma(1+k/2)

cancels EXACTLY the denominator of omega_k.
This yields(4), with no lost dimension-dependent ball-volume or radial factor.
A lower-dimensional ellipsoid, including a single point, has already been covered; an invertible-covariance limiting argument is unnecessary.

Hadamard's inequality for a positive-semidefinite Gram matrix gives det C_I<=product_(i in I)C_ii.
For completeness, represent C_I as the Gram of vectors; successive orthogonal projections express its determinant as the product of squared perpendicular lengths, each at most the original squared length.
In a dependent case both the determinant and an appropriate perpendicular length are zero.
Expanding the product consequently gives the simpler bound

    B_h(C)<=product_(i=1)^q
                      [2+sqrt(2pi C_ii)/h_i].             (7)

The full sum(4) can be retained when actual principal minors are available.
It may improve(7), since small or zero minors remain present.
Neither formula presumes a product covariance, a random phase model or coordinate independence.

<a id="degree-cost-reduced-original-core-norm"></a>
### 4. A uniform-in-phase complete-state expense with all input costs

Now alpha is any actual algebraic UNIT.
Let D_act be its original return core and K_act its original kernel on the complex counting-measure space l2(D_act).
Reuse L251/L173's precise nonneutral bounds and constant

    R_v=1/(|v(alpha)|-1) if |v(alpha)|>1,
        1/(1-|v(alpha)|) if |v(alpha)|<1,
    C_non=product_(real nonneutral v)(2R_v+2)
       product_(complex nonneutral v)(2sqrt2 R_v+2)^2.     (8)

No equality of D_act with a full strip is required.
The complete real Minkowski grid has side1 at a real coordinate and1/sqrt2 at each Cartesian complex coordinate.
Its full cells contain at most one actual order element: a nonzero difference inside one cell would have every conjugate of modulus strictly less than one and hence nonzero integral norm of absolute value less than one.
All actual core states occupy at most C_non nonneutral cells.
Their neutral coordinates remain unbounded.

Use h_i=1 for a real neutral coordinate and h_i=1/sqrt2 for a complex Cartesian coordinate in(4).
Let O_N be multiplication by alpha^N on the neutral real coordinate space, an orthogonal direct sum of signs and planar rotations.
For a row based at x, the displacement law and(3) give

    K_act^N(x,y)<=p_N g_(C_N)(tau_0(y)-O_N tau_0(x)).

Grid injection, nonneutral counting and(4) bound every row by C_non B_h(C_N)p_N.
For a fixed y the same function can be written

    g_(C_N)(tau_0(y)-O_N tau_0(x))
      =g_(O_N^T C_N O_N)(O_N^T tau_0(y)-tau_0(x)).

This identity preserves the range support even for singular C_N.
Thus every column is bounded by C_non B_h(O_N^T C_N O_N)p_N.
Both quantities are finite.
Schur's weighted Cauchy--Schwarz argument on the SAME full Hilbert space proves

    p_N<=||K_act^N||_(2->2)
       <=C_non sqrt[B_h(C_N)B_h(O_N^T C_N O_N)]p_N.       (9)

The lower coefficient p_N, actual core, original iid index reversal and one-step contraction are exactly the L251 interfaces.
No killed finite box or auxiliary-law matrix replaces them.

There is a particularly useful bound requiring NO covariance computation.
In either covariance of(9), each real neutral diagonal is N.
For a complex pair its two diagonal entries u,v are nonnegative with u+v=N: the column rotation preserves the trace of each individual2-by-2 block, even though it need not diagonalize the complete covariance.
Formula(7) gives for this pair

    [2+sqrt(4pi u)][2+sqrt(4pi v)]
                       <=[2+sqrt(2pi N)]^2.              (10)

Indeed sqrt u+sqrt v<=sqrt(2N) and sqrt(uv)<=N/2 prove(10) after expansion.
A real coordinate contributes exactly2+sqrt(2pi N).
Hence for ALL N>=1 and all phases,

    p_N<=||K_act^N||_(2->2)<=E_N p_N,
    E_N=C_non[2+sqrt(2pi N)]^q,
    ||K_act||_(2->2)<=1.                                 (11)

When q=0, the neutral sum/product is1 and E_N=C_non.
This includes all real/complex multiplicities and any rank-deficient early covariance.
In particular there is no phase gap delta, hidden N>=N_alpha, favorable separation assumption or kappa=r_0+s_0 factor.
It is a full original-law theorem for every unit, including torsion; it does not apply automatically to the positive-theta normalized kernel.

For the same full operator, write n=kN+r with0<=r<N.
Submultiplicativity and contraction, paying the complete row/column expense once per block, give

    p_n<=min{1,(E_N p_N)^floor(n/N)},
    0<=-log p_N/N-h_2(alpha)<=log E_N/N.                  (12)

The opposite entropy direction uses concatenation of actual zero-return words, as in L251.
If an exactly evaluated retained entry b_(N,H) has a proved ORIGINAL same-time relative error at most epsilon<1, such as L251's complete returned-height cutoff, then

    p_N<=b_(N,H)/(1-epsilon),
    p_n<=min{1,[E_N b_(N,H)/(1-epsilon)]^floor(n/N)}.      (13)

All state enumeration and relative-error obligations remain.
The improved geometric factor does not make an arbitrary retained entry complete or permit a bare finite p_N to lower-bound the entropy.


<a id="covariance-grid-quartic-all-time-certificate"></a>
### 5. An exact stronger quartic certificate from the same retained data

For the actual quartic P=t^4-t^3-t^2-t+1, q=2 and the previously proved bound C_non<259/8 is unchanged.
The new complete-state expense is

    E_64=C_non[2+sqrt(128pi)]^2
                       <(259/8)*23^2=137011/8.           (14)

Only a crude rigorous bound for pi is needed: the finite geometric expansion gives

    1/(1+x^2)<=1-x^2+x^4-x^6+x^8 for0<=x<=1,
    pi=4 integral_0^1 dx/(1+x^2)<1052/315<441/128.

The first inequality has remainder -x^10/(1+x^2) and is strict on a set of positive length.
Thus sqrt(128pi)<21, proving(14) without a decimal assumption or a source-dependent numeric table.

Reuse the COMPLETE original J52/L243 value, with no rerun:

    p_64=121338835637214357477/2^121,
    121338835637214357477<7*2^64.

All remaining comparisons are integers:

    E_64 p_64<959077/2^60<2^(-40),
    137011*7=959077<1048576=2^20.

The complete all-time and entropy conclusions therefore are

    p_n<=2^[-40 floor(n/64)] for every integer n>=0,
    h_2(beta)>=40log2/64=5log2/8.                         (15)

This adds one bit per length64 block to L251's already fully charged39-bit certificate, using the SAME finite return value.
It is not a new finite calculation, a best-known claim, a change of original law, or a lower entropy inference from a bare p_64.
The new premise is the independently reviewable complete-state geometric estimate(11).
No existing J52 author or review file was edited or re-executed.
For n<64 the bound is one, and at n=0 it includes equality.

<a id="full-covariance-grid-cost-control"></a>
### 6. An actual control locating the remaining geometric loss

The degree factor removed by(11) is real, but the new grid estimate is not claimed optimal.
There is an exact actual-input control where even retaining EVERY principal minor in(4) gives no improvement over the simplified product.
Take d=2^r>=2 and alpha=exp(pi i/d), with its actual irreducible polynomial t^d+1.
The complete neutral dimension is q=d and there are d/2 complex pairs.
At the time N=d,

    C_d=(d/2)I_d.                                        (16)

To verify this directly, the conjugates are exp((2a+1)pi i/d), a=0,...,d-1.
For two distinct such phases, their ratio is a nontrivial dth root of unity, whose sum over powers j=0,...,d-1 is zero.
Choose one phase from each conjugate pair and expand cos*cos, sin*sin and cos*sin into sums/differences of these exponentials.
Differences give d only for an identical coordinate pair; sums give d only when the two chosen phases are conjugate, which the representative choice excludes.
The diagonal sine and cosine squared sums are each d/2, and every mixed sum is zero.
This proves the full matrix(16), not just its trace.

All grid lengths are1/sqrt2.
Every principal determinant equals(d/2)^|I|, so(4) is EXACTLY

    B_h(C_d)=[2+sqrt(2pi d)]^d.                          (17)

No covariance-angle refinement within this particular principal-minor bound improves it.
On the other hand no nonzero polynomial of degree below d vanishes at alpha, so the only length-d original return is the all-zero word:

    p_d=2^(-d).

L251's explicit actual torsion-core proof applies: D_act=Z[alpha], multiplication by alpha is a signed coordinate permutation, and cube indicators give ||K_act^d||=1.
Hence the TRUE ratio of the complete norm to the return coefficient is exactly2^d, while this geometric upper ratio is(17).
Their quotient is

    [1+sqrt(pi d/2)]^d.                                 (18)

This is a discrepancy of the specified sufficient grid certificate, not a contradiction to it and not an impossibility theorem for sharper lattice estimates.
The covariance is already perfectly isotropic at this time, so tuning phase separation or off-diagonal covariance cannot remove this discrepancy.
A genuinely sharper method would have to use more information about the ACTUAL order lattice or the discrete atom law than at most one point in each small conjugate grid cell.
No unproved replacement of lattice counting by continuous covolume is made here.
This torsion family does not substitute for a varying nontorsion Salem family or exclude a sharper theorem on that class.

For context, L251 already proves that the exponent q/2 in a fixed-input all-unit norm comparison cannot simply be reduced.
Equation(18) isolates a different limitation: the size of the degree-dependent constant and the coupled degree/time regime N=d.
The present result improves that constant substantially over the old kappa envelope, but does not eliminate every dimension loss.
The two boundaries have distinct quantifiers.

<a id="phase-free-covariance-expense-and-next-gate"></a>
### 7. Varying-input comparison, full scope and author self-check

For an actual degree d=2s+2 Salem input with expanding root beta, all the new expenses are

    E_N=(2/(beta-1)+2)(2beta/(beta-1)+2)
                              [2+sqrt(2pi N)]^(2s).       (19)

The prior L251 expense was the same real prefactor times[2+sqrt(4pi sN)]^(2s).
At large N their ratio tends to(2s)^s.
Thus the removed logarithmic expense is asymptotically s log(2s) at fixed s as N tends to infinity, and the displayed finite-N formulas give the exact comparison in every joint regime.
The improvement uses neither a favorable phase gap nor a degree-dependent waiting time.
All remaining costs are explicit: log C_non, (d-2)log(2+sqrt(2pi N)), a proved relative-error cost -log(1-epsilon) if an incomplete retained entry is used, and the actual finite-state computation needed for that entry.
There is no uniform bound on C_non as beta approaches1 and no assumption that an N-scale return gain exceeds these costs.

The strongest available covariance-sensitive version is(9), using BOTH the row and column principal-minor sums; arbitrary translations are already covered.
It may be useful when some actual covariance minors are small.
The torsion control demonstrates why covariance information alone in this fixed grid need not settle the degree-cost question.
A discriminating next investigation is an actual-order lattice estimate that preserves its point density AND controls all translated row/column ellipsoids, rather than replacing volume by a putative lattice count without a remainder.
Another is a fully evaluated original retained-entry certificate with a justified same-time relative error, tested only after all of(19).
Both are next questions, not adopted new results or a suspension of other routes.

This proof establishes no analogue for the state-dependent positive-theta law, no distributional independence between conjugates, no general critical recurrence, and no uniform near-one entropy or Mahler gap.
It does not use the separately assigned RETURN-conditioned coefficient-projection argument.
The all-time quartic claim is fixed-input progress and retains its complete finite-data dependency.
Every nonneutral embedding, complex multiplicity, time, degree, truncation and operator-space boundary is present.
G0001 and its parallel strategies remain active and unresolved.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:41 |
| status | open |
| reason | Retain the full original covariance/minor/grid theorem with every nonempty/singular/translation and both row-column interface, exact40bit quartic certificate and torsion constant-loss control for actual whole checking. Reuse only adequate existing C419 original-law/core/p64/torsion interfaces; no new research, J/native/source reading or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete theorem](#statement) | Every finite original neutral profile and every translated PSD/singular grid, all algebraic-unit actual cores/N/n, both row-column covariances, complete quartic40bit and dyadic torsion loss/cost boundaries. |
| argument | [Entire proof](#argument) | Full exact original-law/core input and original Sections1--7/equations1--19: coordinate extrusion, singular ellipsoid volumes/gamma integration, Gram minors, both operator orientations, block entropy, rational/integer arithmetic and complete torsion/varying-input controls. |
| dependency | [Original endpoint inequality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Complete actual iid law for every integer column list and real observable, exact zero atom and full joint profile, without conditional independence or positive-theta transfer. |
| dependency | [Actual full-state grid/core](Yin_C_G0419_v1.md#gaussian-full-state-norm-sandwich) | Only actual original unit core, full Minkowski injection/nonneutral costs, same Hilbert-space row-column Schur and contraction; the improved covariance estimate is proved here. |
| dependency | [Complete existing quartic value](Yin_C_G0419_v1.md#relative-truncation-complete-original-block-certificate) | Entire original p64/C_non<259/8 and same-time relative box obligations; original J52 evidence is reused without a new enumeration. |
| dependency | [Actual torsion core/norm](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits) | Irreducible t^d+1,d=2^r, complete order core and signed-permutation/cube-indicator norm one; no nontorsion extrapolation. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:44 |
| status | proved |
| reason | Adopt after the actual whole C432/R634 SELF check of all original-law singular covariance profiles, exact nonempty coordinate extrusion/projected-volume/gamma/grid bounds, both rotated row-column full-space estimates, every original-time/relative-error cost and the complete quartic/torsion/varying-input controls. Exact Fraction/integer comparisons reproduce the charged40bit/64 result from the unchanged complete p64 without executing J52. Original R154 remains whole SELF from its known proposed-conclusion context; no independent isolation, new source proof, new computation or Task/E resumption is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete theorem](#statement) | Every finite original neutral profile and every translated PSD/singular grid, all algebraic-unit actual cores/N/n, both row-column covariances, complete quartic40bit and dyadic torsion loss/cost boundaries. |
| argument | [Entire proof](#argument) | Full exact original-law/core input and original Sections1--7/equations1--19: coordinate extrusion, singular ellipsoid volumes/gamma integration, Gram minors, both operator orientations, block entropy, rational/integer arithmetic and complete torsion/varying-input controls. |
| dependency | [Original endpoint inequality](Yin_C_G0419_v1.md#original-endpoint-conditioned-exponential-moments) | Complete actual iid law for every integer column list and real observable, exact zero atom and full joint profile, without conditional independence or positive-theta transfer. |
| dependency | [Actual full-state grid/core](Yin_C_G0419_v1.md#gaussian-full-state-norm-sandwich) | Only actual original unit core, full Minkowski injection/nonneutral costs, same Hilbert-space row-column Schur and contraction; the improved covariance estimate is proved here. |
| dependency | [Complete existing quartic value](Yin_C_G0419_v1.md#relative-truncation-complete-original-block-certificate) | Entire original p64/C_non<259/8 and same-time relative box obligations; original J52 evidence is reused without a new enumeration. |
| dependency | [Actual torsion core/norm](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits) | Irreducible t^d+1,d=2^r, complete order core and signed-permutation/cube-indicator norm one; no nontorsion extrapolation. |
| review | [Actual complete SELF finding](../audits/reviews/Yin_R_G0634_v1.md#covariance-grid-whole-self-finding) | Whole exact statement/argument/required C419 interfaces, every singular/translation/row-column/clock/degree/input cost, exact quartic arithmetic and full torsion/source/uniformity limits. |

