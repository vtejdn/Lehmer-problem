---
author: Yin
---

# Every-cluster collar exclusion and a balanced finite coercivity radius

Current checking scope is owned by [R568](../audits/reviews/Yin_R_G0568_v1.md), with its exact findings and declared relationships.
Retained review narration and relationship labels below preserve historical declarations; they do not establish an independent current relationship beyond those responsible findings.


Date: 2026-10-08.
Bounded G0001 derivation by the coordinating AI and the assigned execution_and_deliverables AI for Yin.
The coordinator identified that the existing local collar proof applies to every nonzero cluster, proposed the smallest-gap merging argument and its balanced recursion, and supplied its intended final radius.
The assigned agent checked and expanded the complete finite combinatorial proof and derived the exact zero-gap-certificate control below.
Both are contributors.
The complete checking account below retains the responsible findings' actual relationships.
No numerical mathematical run, optimization or new source is involved.

## A combinatorial statement with both boundary anchors

Let R be a nonnegative integer.
Suppose a nonempty finite set of integer defects in [-R,R] has positions

    a_1<...<a_M,       0 in {a_1,...,a_M},       M<=K,
    a_0=-R-1,         a_(M+1)=R+1,             K>=1.       (1)

The two additional points are boundary anchors, not defects.
Let L be a positive, integer-valued, nondecreasing function on the nonnegative integers.
Assume the following prohibition for EVERY consecutive nonempty defect cluster, not only clusters containing the origin: for all 1<=i<=j<=M, the two inequalities

    a_i-a_(i-1)-1 >= L(a_j-a_i),
    a_(j+1)-a_j-1 >= L(a_j-a_i)                         (2)

cannot both hold.
These are counts of zero-defect indices, including the available indices between a boundary anchor and the first or last defect.
Each count is the corresponding point distance minus one.

Define integer F(n) for n>=1 by

    F(1)=0,
    F(n)=(n-1)L(F(floor(n/2))),             n>=2,
    G=L(F(K)),
    R_bal(K,L)=K G.                                      (3)

Then the purely finite conclusion is

    R < R_bal(K,L).                                      (4)

All quantities in (3) depend on the supplied K and L.
In particular, no statement about omitted root or coefficient constants is implicit.

<a id="every-cluster-balanced-radius"></a>
## Proof by merging a smallest remaining point gap

First F is nondecreasing.
F(2)=L(0)>0=F(1).
At any later step, floor((n+1)/2)>=floor(n/2); induction, monotonicity of L, and the increase of the prefactor from n-1 to n give F(n+1)>=F(n).

Start with singleton components consisting of the M defects and the two boundary anchors, in their original order.
At each step merge adjacent components across a smallest remaining point-distance gap g.
Ties can be resolved in any manner.
A component containing an anchor is called a boundary component.
Stop as soon as there are no interior components, so the two boundary components are not merged with one another.

Every component is a consecutive block of the original ordered points.
A gap between two components is an original distance a_(k+1)-a_k, not a distance between component centers.
Merging removes just that gap and leaves every other intercomponent gap unchanged.
Thus the successive selected distances g are nondecreasing.
A boundary-to-boundary merge cannot occur before the stopping condition: since the anchors are the extreme points, two adjacent boundary components already exhaust all components.
Consequently the procedure terminates with exactly those two components and with every defect assigned to one of them.

Consider any selected merge with distance g, and an interior child component of that merge, containing the defect cluster [a_i,a_j].
Both of its exterior point-distance gaps are still unmerged at that time, so both are at least g.
If g>L(a_j-a_i), integrality would make both corresponding zero gaps at least L(a_j-a_i), contradicting (2).
Therefore each interior child obeys

    g<=L(span of that child).                            (5)

This assertion also applies when its other neighbor is a boundary component, and when a smallest gap has ties.
It uses neither an unavailable exterior index nor a claim that a boundary component itself obeys (2).

We next prove that every interior component with n defects that is formed during the procedure has span at most F(n).
This is true for a singleton.
If an interior n-component is formed by merging two interior children, one child has at most floor(n/2) defects.
The induction hypothesis, (5), and monotonicity give

    g<=L(F(floor(n/2))).                                 (6)

All n-1 original point gaps inside the new component were either the current gap g or gaps selected at earlier steps.
They are therefore at most g.
Their sum is its span, which gives

    span <= (n-1)g <= F(n).                              (7)

This proof does not bound an unbalanced merge by the large child; the small child's prohibition bounds the present gap, and the global increasing order bounds every previously merged gap.

Every gap selected in an interior-to-interior merge is at most G, by (6), since n<=M<=K.
In a merge absorbing an interior component into a boundary component, that interior child's span is at most F(n)<=F(K), so (5) again bounds the selected gap by G.
These are all selected gaps before the stopping condition.

The path in the final point chain from a boundary anchor to any defect in its component contains no more than K selected edges.
Each edge has length at most G.
Every defect is consequently at distance at most KG from one of the two anchors.
The origin, however, is at distance exactly R+1 from either anchor.
Thus

    R+1<=KG,

which proves (4), including its integer boundary.
Equivalently, R>=KG is impossible under (1)--(2).

<a id="every-cluster-energy-coercivity"></a>
## Applying the actual cube collar theorem at every cluster

Use precisely the finite energy problem of [L G0130](Yin_L_G0130_v1.md#finite-rational-energy-coercivity).
P is monic irreducible in Z[t], has constant coefficient +/-1, M(P)>1, and q>0 unit-circle roots.
Let B>0 be rational, put W=||P||_1 and K=floor(W^2 B), and suppose a feasible closed-cube vector x on I_R has energy at most B.
Its integer defects obey

    sum_(-R<=j<=R) |z_j| <= sum_j z_j^2 <=K,
    z_0!=0.                                              (8)

For K=0 this is already impossible.
Otherwise its M nonzero defect positions satisfy (1).

Any of the following already proved integer collar functions L can be used without changing its constants:

- The L G0135 collar, including its entirely coefficient-only rational version.
- The all-central L_* of L G0138.
- The improved L_flux of L G0141.

For definiteness the last choice is

    A_*(ell)=min(K,floor(W/2)(ell+1)),
    T_flux(ell)=1+ceil[2B Phi A_*(ell)^(2h/q)
                          exp(2m ell/q)+4B Psi^2],
    L_flux(ell)=d T_flux(ell),             h=d-q, m=log M,
                                                               (9)

with exactly the Phi and Psi constants of [L G0141](Yin_L_G0141_v1.md#joint-collar-flux-radius).
The other choices and their constants are fixed in [L G0135](Yin_L_G0135_v1.md#explicit-finite-energy-coercivity-radius) and [L G0138](Yin_L_G0138_v1.md#all-central-coercivity-radius).

Here is the additional quantifier needed to apply (2).
The local proof in each cited record uses an origin-containing cluster in its displayed global construction.
Within that LOCAL proof, the only role of containing the origin is to ensure that its cluster polynomial is nonzero.
Every nonempty cluster of actual nonzero defects already ensures this.
Its integer coefficient budget is still bounded by the same global K.
If its two immediate zero gaps contain collars of length L(ell), the collars are entirely inside [-R,R].
The same disjoint boundary blocks share at most the global energy B.
The same central norm argument either contradicts its bounds or forces P to divide that nonzero cluster polynomial.
In the latter case monic division gives a nonzero finite integer response supported in [a+d,b].
The unchanged homogeneous endpoint estimate contradicts the cube at one of those response coordinates.
None of these steps uses z_0.

Thus the proved local collar prohibition holds for EVERY nonempty consecutive defect cluster.
Applying (4) yields the new sufficient finite-energy certificate

    R>=R_bal(K,L)  implies E_R>B,                        (10)

with R_bal=0 when K=0.
The feasible set is compact and the minimum is attained when it is finite; therefore exclusion of every energy-at-most-B vector gives the strict conclusion in (10).
No defect outside [-R,R] or infinite homogeneous extension is used.

<a id="balanced-radius-nesting-cost"></a>
## Cost improvement and its precise limit

The earlier origin-centered construction evaluates L successively K times through s_(j+1)=s_j+L(s_j).
In (3), repeated halving of the positive integer argument reaches 1 in floor(log_2 K) steps.
Computing R_bal therefore needs exactly

    1+floor(log_2 K)                                     (11)

nested evaluations of L along that recursion, with the displayed integer multipliers retained.
This count does not mean polynomial bit complexity or a small resulting radius.
For example, if H_0=0 and H_(j+1)=K L(H_j), monotonicity gives

    R_bal <= H_(1+floor(log_2 K)).                        (12)

The root-separation, degree, coefficient, B and Mahler costs inside L remain exactly present.
For arbitrary nondecreasing L the new radius is not asserted to be pointwise smaller than the old one: for K=2 it is 2L(L(0)), whereas the old radius is L(0)+L(L(0)).
Both proved sufficient radii are available, so their minimum is also a valid sufficient radius.
The new gain is the balanced nesting depth rather than a universal pointwise ordering.

This does not contradict the [origin-containing abstract model of L G0138](Yin_L_G0138_v1.md#abstract-collar-model-sharpness).
That model imposes the no-two-empty-collars property only on intervals containing the origin.
Condition (2) applies also to every child cluster that does not contain the origin.
The merger proof uses precisely this additional condition.
It is supplied by the actual recurrence and cube argument, rather than assumed to follow from the weaker origin-only combinatorial model.

There is no claim that (10) lies below a useful L G0132 cutoff at a supplied orbit length, or that its costs are uniform in near-one inputs.
The result supplies a new explicit sufficient radius, not the actual least successful window, an energy optimization or a transition-product lower bound.

<a id="all-gap-central-certificate-zero-control"></a>
## An exact zero control for all central gap certificates

The use of the cube in the local theorem above cannot be replaced by L G0140's gap bound alone.
This has an exact control stronger than merely bounding a cube-free Gram minimum by one.

Fix any P in the domain above and any integer R>=d+1.
On I_R take x=delta_0, with its single nonzero coordinate equal to one.
This vector deliberately violates the cube.
It gives integer defects

    z_j=p_(-j) for -d<=j<=0, and zero otherwise,
    z_0=p_0!=0,        ||x||_2^2=1.                      (13)

Since zero is not a zero-defect index, x vanishes on every raw zero-defect gap.
Applying the hyperbolic filter only inside each raw gap therefore gives zero output.
In the notation of [L G0140](Yin_L_G0140_v1.md#summed-gap-weighted-variance), all actual quadratic terms a_j^* H_j a_j are zero, including short-gap null spaces.
Consequently both the scalar weighted variance and the exact matrix minimum over the common amplitude are exactly zero: each is nonnegative, while this actual recurrence vector supplies a common offset with value zero.

This applies to the complete collection of maximal zero-defect gaps, not only a selected sample.
The exterior gaps can be arbitrarily long and their central amplitudes are zero.
Interior gaps have length at most d-1; when present their scalar smallest Gram eigenvalue is zero.
Their full matrices still give zero on the actual amplitude vectors.
Thus keeping the full matrix refinement does not remove this control.

This integer pattern also survives the cube-derived entry and coefficient budgets at explicit thresholds.
P(beta)=0 for a unit-circle root gives, for every coefficient,

    |p_i|<=sum_(k!=i)|p_k|,  hence |p_i|<=W/2,
    sum_i p_i^2<=W^2/2.                                  (14)

For B>=1/2, the integer squared-defect budget and the entry bound |z_j|<=floor(W/2) therefore admit (13).
For B>=1, the same x also passes the full cube-free energy condition, and hence the unconstrained Gram minimization has value at most B.
This is not a claim that it passes the cube fiber test.

These thresholds occur inside the conditional Salem target.
If 0<m<=1/4096 and B>=B_m from L G0132, then

    B>=B_m>=2log(256)/pi^2>16/15>1,                      (15)

using log2>2/3 and pi^2<10.
No existence of such a Salem input is assumed.
Formula (15) states the conditional comparison for every input in that domain.

For the full defect cluster [-d,0], its reversed cluster polynomial is exactly P.
It is the P-divisible residue-zero branch, distinct from the reciprocal-product divisibility exception P|A in L G0142.
The actual cube would have to exclude every possible response for the specified integer pattern; the particular vector (13) is only a cube-free witness.
Therefore the zero certificate is not a feasible low-energy counterexample to (10) or to finite-energy coercivity.
It proves that global coverage cannot come from central-gap charges alone, even with all gaps, exact matrix coupling, integer budgets and arbitrary long exterior gaps retained.
The local cube/finite-integer-response argument is an essential separate premise of the new radius.

## Contributions and actual review

The coordinating AI contributed the every-cluster quantifier, smallest-gap merging mechanism and balanced radius proposal.
The assigned execution_and_deliverables AI checked its finite indices, ties, all component cases and exact recurrence, expanded the proof, and derived the all-gap zero-certificate control (13)--(15).
Both are authors/contributors, and the coordinator read the complete assembled proof as a contributor check.

On 2026-10-08 the separately assigned entropy_status AI for Yin independently checked the full proof (1)--(15) and all scope statements.
It did not derive the new merging mechanism or zero-certificate control, write or edit this proof, or run a computation.
It had seen the research question and related branch context, so this was not blind review.
Its earlier contributions to L G0135/L G0138/L G0141 are disclosed; here those were reused as fixed local interfaces, not newly audited as independent proofs.

Coverage includes every-cluster quantifiers, boundary anchors and point-distance-minus-one counts, ties and monotonicity of selected gaps, both types of merge, the small-child induction and F monotonicity, the final path of at most K edges and strict R+1 boundary.
The reviewer directly reread the complete used L G0135 local finite indices, norm, monic division, integer response and cube contradiction, and checked the corresponding fixed L G0138/L G0141 interfaces.
It checked K=0, compactness, the exact nesting count and comparison sequence, the K=2 nonordering example and the distinction from the origin-only model.
It directly checked L G0140's full scalar/matrix gap interfaces and the delta_0 control, including short-gap null spaces and all-gap common offset.
It rechecked the coefficient and integer budgets, the different B>=1/2 and B>=1 thresholds, and the conditional Salem B_m>16/15 comparison.
No substantive mathematical defect or missing hypothesis was found.
The cube-free control was not treated as a feasible cube counterexample or as uniform near-one coverage.

This is complete independent AI written-proof review, not formal verification, a numerical experiment, or new external source-proof audit.
The coordinator accepted the result for fixed-ledger preservation on 2026-10-08.
The unrestricted G0001 Task remains unresolved.
