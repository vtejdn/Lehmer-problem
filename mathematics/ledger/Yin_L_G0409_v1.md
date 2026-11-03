---
author: Yin
---
# Weighted bulk contraction and the exact limits of padding carry graphs

Current complete mathematical home: [the exact retained Claim](../claims/Yin_C_G0514_v2.md#statement), with its [entire original proof](../claims/Yin_C_G0514_v2.md#argument).
Current whole checking is the actual 2026-10-22T04:08 [SELF finding](../audits/reviews/Yin_R_G0724_v1.md#complete-supported-bulk-carry-whole-self-finding) and was actually adopted at 2026-10-22T04:10; the original 2026-10-18T15:47 [whole finding](../audits/reviews/Yin_R_G0414_v1.md#bulk-carry-whole-independent-finding) retains its genuinely unestablished initial-context relationship as UNKNOWN.
The dated original mathematics and contribution/source account below remain unchanged; this current maintenance supplies no Task/E continuation.

Date: 2026-10-18T15:46.
Human author Yin.
The angular_envelope_review agent develops this new S2/S7 inquiry under root's continuing allocation.
Root supplied the fixed-defect weak-Poincare target, the all-angle clipped-midpoint argument reaching the defect threshold 1/4, and the component-mass formula for the unavoidable defect.
The assigned author supplies the normalized nested-graph/padding analysis and checks the entire combined argument.
Both are contributors; this fixed exploration preserves the conditional all-late target and does not determine the critical mean.
No additional J input, overlap range or numerical run is proposed.

<a id="bulk-carry-question"></a>
## Exact changed question and reuse

The actual [C170 theorem](../claims/Yin_C_G0170_v1.md#statement), with [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding), bounds the TRUE midpoint update energy at overlap b=2 by 4 independently of n.
Its full global spectral-gap hypothesis is stronger than what [L329](Yin_L_G0329_v1.md#complete-midpoint-tightness-test) needs: eventual positive original-law capture by one finite state set already implies finite critical mean.
The [J106 exact six-case account](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results), now covered by [R412](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding), has rare nonzero-midpoint components at n=5,6,7 but connected graphs at n=8,9,10.
Those finite facts do not classify eventual behavior.

The changed operator hypothesis is a uniform finite coefficient B in

    Var_pi_n(f)<=B D_n(f)+r osc(f)^2,

at ONE fixed defect 0<=r<1/4, for every real function f and every sufficiently large original half-length n.
It is not an assumed full weak-Poincare rate for every vanishing defect and is not a global spectral gap.
Root's all-angle clipping argument is checked below against the exact original finite-box criterion.
The other immediate structural test is whether normalized endpoint support embeds under zero padding, and whether that inclusion pays a useful amount of original conditional probability.
Support connectivity alone must not be promoted to a weighted contraction.

Read [C76](../claims/Yin_C_G0076_v1.md#statement), [C80](../claims/Yin_C_G0080_v1.md#statement), C170/R556, J106's full stated six-case scope and L329's exact eventual capture interface.
C80's infinite frozen family belongs to its six-digit operator and does not transfer to C170.
Its tiny original masses and bounded padding limits remain relevant cautions.
A bounded G-line search found earlier component-centered obstructions and paid zero padding, but no retained fixed-defect/all-angle criterion for this new weighted carry operator.
No absence or novelty claim follows from that search.
The classical weak-Poincare terminology is identified at the necessary primary scope below; no external mixing or convergence theorem is presumed.

<a id="bulk-carry-setting"></a>
## Original objects

Fix P=1-t-t^2-t^3+t^4, exterior root beta, neutral conjugate zeta and O=Z[beta].
For n>=5 use the COMPLETE original ternary returned law pi_n at length 2n, with digit probabilities 1/4,1/2,1/4.
Let K_n=K_(n,2) be exactly C170's two overlapping conditional expectations, D_n(f)=<f,(I-K_n)f> and Z_n its true complex neutral midpoint.
Then E Z_n=0 by sign symmetry and D_n(Z_n)<=4.
Every notation for return probability p_l below means the complete ORIGINAL probability at chronological length l; c_l=4^l p_l is used only at endpoint zero.
No complete-word conditional probability or component mass is replaced by an unweighted graph count.

The complete new proof and decisive failure boundaries follow.

<a id="bulk-one-defect-midpoint-capture"></a>
## 1. One fixed defect below 1/4 suffices for original finite capture

Suppose there are FIXED constants B_W>=0, 0<=epsilon<1/4 and n0>=5 such that, for every n>=n0 and every real function f on the full returned-word space,

    Var_pi_n(f)<=B_W D_n(f)+epsilon osc(f)^2.               (1)

The oscillation is max f-min f on that finite support.
No irreducibility is assumed, and (1) is NOT asserted automatically for the actual graphs.
Unlike a global gap, it allows small invariant components.
Unlike the full classical weak-Poincare profile, it requests only this one defect.

For R>0 and angle theta define the real odd bounded function

    f_(theta,R)=clip(Re(exp(-i theta)Z_n)/R,-1,1).

Global digit sign reversal makes its mean zero at every theta.
Clipping is 1-Lipschitz, so the exact reversible edge formula gives

    D_n(f_(theta,R))<=D_n(Z_n)/R^2<=4/R^2,
    osc(f_(theta,R))<=2,
    E_pi_n f_(theta,R)^2<=4B_W/R^2+4epsilon.              (2)

This uses the same complete original conditional weights and the same auxiliary-update clock as C170.
There is no dropped conditional mean or unweighted graph surrogate.

For a>1, the normalized angular measure of the event |cos theta|>=1/a is

    c(a)=2 arccos(1/a)/pi.

At any fixed complex z with |z|>=aR, the angular mean of clip(Re(exp(-i theta)z)/R,-1,1)^2 is at least c(a).
Integrate (2) over the whole circle and interchange only a finite probability sum and a bounded integral.
Then

    pi_n{|Z_n|>=aR}<=[4B_W/R^2+4epsilon]/c(a).             (3)

In particular set

    c_*=(1+4epsilon)/2,
    a_*=sec(pi c_*/2),
    R_*^2=max{1,16B_W/(1-4epsilon)},
    eta_*=(1-4epsilon)/[2(1+4epsilon)]>0.                  (4)

The angle lies strictly below pi/2, so a_* is finite.
Here c(a_*)=c_*, and (3) implies

    pi_n{|Z_n|<a_* R_*}>=eta_*     for EVERY n>=n0.         (5)

All constants are fixed before n varies.
The case B_W=0 is covered by R_*=1.

To identify the exact finite-state consequence, let Y_n in O be the algebraic midpoint

    Y_n=-beta^-n sum_(j<n)eta_j beta^j
        =sum_(j=n)^(2n-1)eta_j beta^(j-n).

The original return gives both expressions at EVERY conjugate.
They imply the fixed nonneutral bounds

    |Y_n(beta)|<B_real=1/(beta-1),
    |Y_n(beta^-1)|<S_real=beta/(beta-1).

The actual rank-four Minkowski lattice O therefore has only finitely many states in

    F_*={x in the actual core:
         |x(beta)|<=B_real, |x(beta^-1)|<=S_real,
         |x(zeta)|<=a_* R_*}.

Its finiteness uses all four real Minkowski coordinates, including BOTH neutral coordinates.
The conditional distribution of Y_n is precisely L329's original midpoint law b_n.
Indeed, if nu_n(x) is the complete original n-digit endpoint probability, then

    Pr(Y_n=x | full return)
       =nu_n(-beta^n x)nu_n(x)/p_(2n)
       =nu_n(beta^n x)nu_n(x)/p_(2n),

where the last equality uses original sign symmetry.
This is L329's formula, with no new time or stationary law.
Thus (5) gives b_n(F_*)>=eta_* eventually, and L329 yields

    mu<infinity,              mu<=|F_*|/eta_*.             (6)

A uniform bound on the UNTRUNCATED second moments is not required or proved by this argument.
The conclusion is at the fixed actual recurrent quartic, not a varying-degree Mahler-gap theorem.

For the digit-work slowdown K_n^cost=(1-1/(n+2))I+K_n/(n+2), the energy in (1) is divided by n+2.
Its corresponding coefficient is (n+2)B_W, and the clipped energy bound is4/[(n+2)R^2].
These factors cancel in (2).
No uniform cost-clock spectral or mixing estimate is asserted.

<a id="bulk-quarter-defect-boundary"></a>
## 2. The quarter threshold and the distinction from a moment bound

The strict defect threshold has a direct elementary boundary.
If f ranges in [a,b], positivity of (f-a)(b-f) gives

    Var(f)<=(Ef-a)(b-Ef)<=(b-a)^2/4.                      (7)

Hence epsilon=1/4 with B_W=0 holds for EVERY finite law and EVERY kernel, regardless of the midpoint or its mean branch.
It cannot by itself discriminate the question.
The all-angle argument in Section1 reaches every fixed epsilon below this trivial ceiling; it does not substitute a single-coordinate variance for the full neutral norm.

There is also an explicit ABSTRACT comparison showing why (1) need not bound the untruncated second moment.
For fixed0<epsilon<1/4 choose0<q<epsilon, put masses1-q,q/2,q/2 on three states with Z values0,+M,-M, and take the identity kernel.
The law is sign symmetric and its energy is zero.
The component calculation in Section3 gives defect q(1-q)<epsilon for every real test function, so (1) holds with B_W=0 for every M.
Yet E|Z|^2=q M^2 can diverge while the state0 keeps mass1-q.
This is a finite probability comparison only, not a quartic carry graph or an arithmetic input.
It makes the distinction between positive finite capture and a uniformly bounded second moment explicit.

<a id="bulk-component-defect"></a>
## 3. The exact finite-component defect and the actual six controls

For ANY finite reversible chain let its communicating components have masses q_1,...,q_s>0, summing to1.
Within each nonsingleton component its conditional Dirichlet form has a positive gap lambda_j.
This follows directly from the positive-edge squared-difference formula and compactness of the unit-variance sphere: zero energy forces constancy on that connected component.
For singleton components the conditional variance is identically zero.
Let lambda_min be the minimum of the finitely many positive lambda_j, omitting singletons.
If every component is a singleton, take the within-component coefficient to be0 instead.

Define

    chi=max_(I subset {1,...,s}) q(I)[1-q(I)],
    q(I)=sum_(j in I)q_j.                                  (8)

Then

    Var_pi(f)<=lambda_min^-1 D(f)+chi osc(f)^2,              (9)

with the stated zero within-component coefficient in the all-singleton case.
To prove it, decompose variance into the weighted conditional variances and the variance of the component means.
The first part is bounded by lambda_min^-1 D(f).
After translating and scaling the means into [0,1], their variance is a convex quadratic in each individual mean.
Its maximum on the finite cube is attained at a vertex, giving exactly (8).
No uniform value for lambda_min is inferred.

Conversely, the indicator of ANY union of components has zero energy, oscillation1 and variance q(I)[1-q(I)].
Thus EVERY inequality with a finite energy coefficient must have defect at least chi.
The number chi is the exact least possible defect for a finite chain when its energy coefficient may be any finite value.
It measures component mass, not merely the number of components.

Apply this only to the six already computed and whole-reviewed J106 inputs.
At n=5,6,7 the component masses are1-2q,q,q with respectively

    q=1/383, 1/456, 4/2195.

They satisfy q<1/4, and their largest union variance is exactly

    chi=2q(1-2q)<1/100.                                  (10)

For n=8,9,10 the graph is connected, so chi=0.
Consequently all six inputs satisfy (1) with epsilon=1/100 and SOME common finite B_W, by taking the maximum of their finite within-component coefficients.
No gap was numerically estimated or lower-bounded here.
This proves compatibility of the new criterion with the actual early disconnections; it does not estimate B_W or extend it to uncomputed lengths.
It is strictly weaker than requiring a positive global gap on those same six inputs.

The old C80 frozen states belong to a different six-digit operator.
Neither their existence nor their exponentially small selected masses prove the exact component defect for C170 at any uncomputed n.
Conversely J106's n8--10 connectivity says nothing by itself about a uniform eventual coefficient in (1).

<a id="nested-normalized-carry-support"></a>
## 4. Normalized carry graphs are nested, but old frozen components can merge

For k=n-2 let E_k be the support of the complete endpoint count c_k(a).
Normalize the left endpoint by x=beta^-k a.
The b=2 graph can be written with left candidates beta^-k E_k and right candidates E_k, and an edge precisely when

    theta=-x-beta^4 c

has all four original-order coordinates in{-1,0,1}.
Its complete integer edge weight is

    W_n(x,c)=c_k(beta^k x)c_k(c)2^z(theta).                 (11)

The TRUE algebraic midpoint on that edge is

    y(x,c)=-beta^-2[x+theta_0+theta_1 beta],

independent of k in these normalized labels.

Appending a zero gives E_k subset E_(k+1).
Prepending a zero gives beta^-k E_k subset beta^(-(k+1))E_(k+1).
The edge predicate is independent of k.
After removing only vertices of zero marginal, the normalized graph at n is therefore an INDUCED subgraph of the graph at n+1.
Its actual edge weights satisfy

    W_(n+1)(x,c)>=4 W_n(x,c),                             (12)

because the specified leading and trailing zeros each multiply an endpoint count by2.
The inequality can be strict, with different extra multiplicities at different endpoints.
It is not a common rescaling of the stationary law.

Any path between old vertices persists, so old components can merge but cannot split under this inclusion.
New vertices can still create new components; connectivity of one graph does not prove connectivity of every later graph.
Zero-padding a full word on both ends preserves its normalized edge and true midpoint.
It does NOT preserve its component as an isolated component.

In particular use ONLY J106's exactly verified connectivity at n=8.
Every zero-padded image of each n5--7 component is connected to zero at n8, and that path persists at EVERY n>=8.
Thus the specific early nonzero-midpoint components with values +/- (2-beta^2) do not extend as frozen components by arbitrary symmetric zero padding.
Their midpoint value persists, while their invariance fails.
This is an all-later statement about those embedded old states, not an all-later classification of new states or graphs.
No new length was computed to prove it.

<a id="padding-original-measure-cost"></a>
## 5. Original probability costs close two padding shortcuts

Fix n>=5 and an integer r>=0.
Under the length2(n+r) complete returned law, take the event consisting of r initial zeros, ANY old length2n returned word, and r final zeros.
Its exact conditional mass is

    z_(n,r)=4^(-r) p_(2n)/p_(2n+2r).                      (13)

Conditioned on this event the middle word has exactly its original pi_n law, and its true midpoint is unchanged.
The ordinary zero digit has probability1/2, not1/4.

The original collision monotonicity from C169 gives p_(2n+2r)<=p_(2n), so z_(n,r)>=4^(-r).
The relevant upper bound is also explicit.
Concatenating independent returned words gives p_(2n+2r)>=p_(2n)p_(2r).
At length5 the three legal words0^5,+P,-P have total original probability

    2^-5+2*4^-5=2^-5(17/16).

Concatenate floor(2r/5) such blocks and pad the remaining digits by zeros.
This is a subset of the complete original return event, so

    p_(2r)>=2^(-2r)(17/16)^floor(2r/5),
    z_(n,r)<=(16/17)^floor(2r/5) ->0.                      (14)

The last upper bound is uniform in the old n.
It concerns precisely the specified zero-padded copy of old words.
Other long words may have the same normalized endpoint edge, so (14) is NOT an upper bound on the full mass of the embedded endpoint subgraph.
The support inclusion (12) alone supplies no useful uniform normalized weight through this witness.

One may instead place arbitrary r-digit returned words at both ends.
The exact conditional mass of THAT event is

    zret_(n,r)=p_r^2 p_(2n)/p_(2n+2r)
              <=p_r^2/p_(2r)=1/D_r,                       (15)

where D_r=p_(2r)/p_r^2 is L329's complete original overlap.
Its middle law and true midpoint are again unchanged, since both padding endpoints vanish at every conjugate.
The full complete-word event has unique fixed block boundaries, so no multiplicity is lost in its product probability.

For each FIXED n>=5, eventual positive lower mass in (15) is equivalent to finite critical mean.
If zret_(n,r)>=eta>0 for all sufficiently large r, then D_r<=1/eta eventually, and L329 gives mu<infinity.
Conversely if mu<infinity, put a_l=Rcrit^l p_l with the actual critical radius Rcrit.
L329 proves a_l->1/mu, and exact cancellation gives

    zret_(n,r)=a_r^2 a_(2n)/a_(2n+2r)
                  ->a_(2n)/mu>0.                         (16)

This comparison preserves the actual critical radius and does not substitute beta for Rcrit.
Thus using eventual positive mass of unrestricted returned padding as the next hypothesis would merely repackage the already unknown mean branch.
It is not an independent contraction mechanism.

<a id="partial-path-weighted-carry-target"></a>
## 6. A concrete weighted partial-path target

A more specific sufficient proof target can be placed on C170's rational TWO-STEP left-endpoint kernel T_n.
Use its full stationary endpoint law pi_A(a)=r(a)/S and conductances

    c_e=pi_A(a)T_n(a,a')=pi_A(a')T_n(a',a)>0

on each unordered nonloop edge e={a,a'}.
Choose an actual subset G of ORDERED endpoint pairs, each supplied with a path gamma_(a,a') of positive-conductance edges.
Include diagonal pairs with their empty path.
Suppose the discarded ORIGINAL product mass and the complete path load satisfy

    (pi_A tensor pi_A)(G^c)<=2epsilon,
    L_e=[1/(2c_e)] sum_((a,a') in G)
             pi_A(a)pi_A(a') length(gamma_(a,a'))
                  number_of_traversals_of_e(gamma_(a,a')) <=A
                  for EVERY edge e.                       (17)

Here 0<=epsilon<1/4 and A>=0 are intended to be fixed independently of n.
No unweighted adjacency, uniform endpoint law or zero-cost path is allowed.
All displayed quantities are finite and exactly specified from the actual weighted graph; no test of them was executed.

The variance identity over ordered independent pairs and path Cauchy--Schwarz prove

    Var_pi_A(g)<=A D_T(g)+epsilon osc(g)^2.                 (18)

Indeed bad pairs cost at most one half of their mass times osc(g)^2.
For each good pair, the squared difference is at most path length times the sum of squared edge increments, with repetitions counted.
Regrouping exactly by e gives (17) times the actual energy sum sum_e c_e[g(a)-g(a')]^2.
This is the standard finite weighted path argument; C76 already uses its paid path-Cauchy mechanism on specified words.
No external comparison constant or mixing theorem is imported.

For completeness the endpoint inequality (18) transfers to the WHOLE returned-word K_n with no discarded fiber modes.
Write H_A,H_C for C170's full-tail conditional expectations and g=H_A f.
Then

    Var(f)=Var(g)+||f-H_A f||_2^2,
    D_(H_A H_C H_A)(g)=||(I-H_C)g||_2^2
                      <=4D_n(f).                          (19)

The bound follows by writing (I-H_C)g as (I-H_C)f+(I-H_C)(g-f), using the projection contraction and the squared triangle inequality.
The two squared residuals sum to2D_n(f).

Split g into its mean gbar(a) within each left endpoint and a residual u with zero mean on every such fiber.
C170's exact conditional law gives H_C u=0.
Thus this two-step kernel kills u, while on gbar it is precisely T_n, and

    Var(g)=||u||_2^2+Var_pi_A(gbar),
    D_(H_A H_C H_A)(g)=||u||_2^2+D_T(gbar).

Also osc(gbar)<=osc(g)<=osc(f).
Using (18)--(19) gives the complete sufficient inequality

    Var_pi_n(f)<=[4max(1,A)+2]D_n(f)
                                      +epsilon osc(f)^2.  (20)

Consequently a uniform all-late construction satisfying (17), with ANY fixed epsilon<1/4, proves finite original critical mean by Section1.
It permits omitted pairs and rare disconnected components, while requiring a quantitatively bounded load on the pairs actually retained.
This is a concrete weighted arithmetic graph target beyond graph nesting or a renamed midpoint mean.
No such all-late path family or uniform load has yet been constructed.
The six finite controls establish neither of these requirements.

<a id="bulk-carry-source-and-boundaries"></a>
## 7. Source scope, selected continuation and contributions

The term weak Poincare inequality is classical.
The necessary primary formulation is now retained in [RW01-U001](../audits/literature/RW01/Yin_U001.md#rw01-u001): equation(1.6) of the September19,2000 Bielefeld preprint, visually inspected on printed/PDF pages1--3.
It has a homogeneous defect functional and quantifies over EVERY positive defect.
The current project asks only for the single-defect inequality (1), with a complete local proof of its midpoint consequence.
No RW01 convergence, isoperimetric, perturbation or numerical-constant theorem is a premise.
Its published-edition equivalence and original proofs were not audited.
Source acquisition/availability belong to the registry, not to the mathematical evidence here.

The selected next mathematical target is (17) for the actual rational T_n, or another directly proved weighted inequality implying (18) with the same fixed defect and a uniform finite coefficient.
It must retain all original endpoint multiplicities and ultimately all word-fiber modes through (19)--(20).
A merely larger connected sample, an unweighted graph estimate, a zero-padding path without its conductance, or the returned-padding positive-mass hypothesis (16) does not settle that target.
No additional n, overlap, eigenvalue scan or J is proposed in this account.

Root supplied the all-angle improvement reaching epsilon<1/4 and the exact component-defect idea, including its application to the three recorded early masses.
The assigned author checked those arguments and supplied the complete normalized-support inclusion, both padding probability boundaries, whole-word endpoint transfer and explicit partial-path target.
Both are mathematical contributors.
The source reading only supplies terminology and quantifier attribution; it is not independent review.

All proof arguments are finite except the explicitly reused L329 limit and the elementary fixed-parameter limit in (14).
The actual eventual inequality and original critical-mean branch remain unresolved.

<a id="bulk-carry-fixed-inputs"></a>
## Exact input roles

| Input | Scope |
| --- | --- |
| [C170 statement](../claims/Yin_C_G0170_v1.md#statement), [R803 analytic review](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Exact original returned law, two conditional expectations, midpoint and energy bound4 at b2; source and clock limits unchanged. |
| [C170 complete weighted reduction](../claims/Yin_C_G0170_v1.md#short-overlap-exact-carry-matrix), [exact marks](../claims/Yin_C_G0170_v1.md#four-digit-overlap-exact-marks) | Full tail-word and endpoint-fiber conditional laws, rational two-step kernel, component correspondence and actual y(x,c), with no uniform contraction supplied. |
| [L329 finite-capture equivalence](Yin_L_G0329_v1.md#complete-midpoint-tightness-test) | Eventual positive mass on any one finite actual state set gives finite critical mean and the cardinality/positive-mass bound; bounded full second moment is not necessary. |
| [L329 original ratio limits](Yin_L_G0329_v1.md#true-harmonic-ratio-limits), [positive-mean convergence](Yin_L_G0329_v1.md#positive-branch-coupling-proof) | Exact midpoint law and finite-mean a_l limit used in the returned-padding equivalence; no uniform convergence rate imported. |
| [J106 actual six-case results](../computations/programs/Yin_J_G0106/readme.md#complete-six-case-results), [R412 whole review](../audits/reviews/Yin_R_G0412_v1.md#carry-j106-whole-independent-finding) | Exact component masses at n5--7 and finite n8 connectivity; no new native reconstruction or uncomputed-length assertion borrowed from the table. |
| [C169 original collision monotonicity](../claims/Yin_C_G0169_v1.md#endpoint-collision-monotonicity) | Original p_l is nonincreasing and the exact probabilities of0^5,+P,-P; the new padding estimate is proved directly from these values. |
| [C76 paid original paths](../claims/Yin_C_G0076_v1.md#statement), [C80 different frozen operator](../claims/Yin_C_G0080_v1.md#statement) | Existing weighted path-Cauchy mechanism and precise different-operator/rare-mass boundaries; neither supplies an eventual contraction for C170. |
| [RW01-U001](../audits/literature/RW01/Yin_U001.md#rw01-u001) | Primary definition/terminology and the every-defect versus single-defect distinction only; every new project estimate is proved here. |

The complete argument, exact finite controls and conditional continuation are retained here.
