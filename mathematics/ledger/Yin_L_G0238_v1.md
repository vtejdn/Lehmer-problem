---
author: Yin
---

# Bounded-measure companion obstruction and growing positive factors

The complete current mathematical home is [C573](../claims/Yin_C_G0573_v1.md#bounded-companion-factor-fixed-scope), adopted at 2026-10-22T19:35 after the [actual current whole SELF](../audits/reviews/Yin_R_G0755_v1.md#current-complete-whole-self-finding).
The original dated argument and frozen input below remain the actual input of R137; current links do not backfill that review or supply its missing relationship declaration.

Date: 2026-10-10.
The original2026-10-10 coordinating account adopted this restricted result after its separately organized noncontributor review at the original scope.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="bounded-companion-factor-fixed-scope"></a>
## Original adopted scope and fixed review input

The accepted McM02 canonical Coxeter spectral-radius theorem, an exact reflection-product transfer and a separate large-integer-entry bound give a universal positive lower bound log(lambda_Lehmer) for the complete absolute companion of every positive-measure integral unitriangular presentation.
Hence its ratio to a bounded original total measure cannot tend to zero.
An explicit height-one Walsh-core path family nevertheless has bounded positive full measure, companion ratio below one-half and distinct positive irreducible factors of degrees tending to infinity.
Every fixed positive background factor, neutral multiplicity, lattice, rank and cover cost is retained, as is the strictly positive exact ratio limit.
McM02 is accepted at statement/applicability scope, not a new source-proof audit.
The complete targets stay reducible and away from measure one; no unrestricted signed realization or Lehmer gap is proved.


<a id="complete-retained-proof-and-review"></a>
## Complete original author proof and dated review input

## Signed companion collapse at bounded original measure

Date: 2026-10-10.
Starting question: Investigate whether the actual signed-Gram companion collapse of L234 can coexist with uniformly bounded positive original total measure and increasing irreducible complexity.
Seek changed sparse matrices, controlled couplings, an actual construction or a precise restriction that explains the obstruction.
Keep all original and absolute factors, neutral multiplicities, integral realization and complete cover costs.
Bold bounded experiments are permitted before a uniform construction is known.



<a id="bounded-collapse-reuse-and-result"></a>
### Reuse, changed construction and result

The full [L234 proof](Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) leaves a genuine quantifier change: its zero ratio uses original measure tending to infinity and only a repeated quadratic factor.
The complete [L203 path transfer and factor argument](Yin_L_G0203_v1.md#pendant-chain-full-determinant), [L207 multichain costs](Yin_L_G0207_v1.md#many-chain-complete-cost-bound), [L185 positivity/spectral comparison](Yin_L_G0185_v1.md#positive-absolute-cover-cost), and [D9 literal signed cover](../claims/Yin_C_G0002_v1.md#signed-cover-identity) were read before the new derivation.
The L203 exterior-root argument already carries its exact classical Hir06 attribution; it is reused at its proved no-circle-zero scope, not renamed as new.

The first outcome is a restriction stronger than the new question initially required.
The already retained [McM02 published source](../literature/pdf/McM02.pdf), Theorem1.1 on printed p.151, has a canonical Coxeter spectral-radius gap.
Its actual reflection conventions on pp.161--162 permit entries of absolute value0,1,2; larger integral entries admit a separate elementary bound.
The [new compact source record](../audits/literature/McM02/readme.md#canonical-coxeter-gap-input) records the accepted external statement and precise inspection depth.
D9's earlier motivation-only reading and L185's spectral-comparison reading are not retroactively extended to a full classification review.

The second outcome is an actual positive construction.
Attaching a unit path to ONE fixed height-one Walsh core gives bounded positive original total measure, an increasing set of positive reciprocal irreducible factors of unbounded degree, and companion measure strictly smaller than original measure at EVERY path length.
The entire fixed positive quadratic background is retained.
Thus strict companion collapse is possible under the bounded-total-measure condition, while collapse to ratio zero is impossible.
These are different assertions.
Neither supplies an irreducible complete original polynomial, a near-one family, an optimized ratio at a fixed measure cap or unrestricted scalar realization.

All substantive new arguments are written here.
No program, numerical search, J allocation, floating root calculation or new source acquisition is a premise.

<a id="uniform-companion-gap-and-bounded-ratio"></a>
### 1. A universal companion gap and its bounded-measure consequence

For any integral upper-unitriangular V, use the complete ordinary logarithmic measures

    p_V(t)=det(tV+V^T),   V^-_ij=-|V_ij| for i<j,
    p_W=p_V p_(V^-),     m(p_W)=m(p_V)+m(p_(V^-)).       (1)

The diagonal of V^- is one.
Let A be its symmetric absolute adjacency, with zero diagonal.
Assume m(p_V)>0.
The already proved L185 theorem gives rho(A)>2 and a positive real root of p_(V^-) at least

    T(rho(A)),    T(x)=((x+sqrt(x^2-4))/2)^2.            (2)

Write lambda_L for the Salem root of the original Lehmer polynomial fixed in L170; it is the same exact root specified by McM02 equation(1.1).

**Uniform companion bound.** Every such V, of any rank and integer entry height, satisfies

    m(p_(V^-))>=log lambda_L.                           (3)

First suppose every |V_ij|<=2.
Define a Coxeter system on the vertices by exponent2 for A_ij=0, exponent3 for A_ij=1, and exponent infinity for A_ij=2.
The source's canonical geometric form is exactly G=2I-A.
Its simple reflection is

    R_i x=x-(Gx)_i e_i.

This construction includes disconnected diagrams and degenerate forms.
No sign from the original V enters this canonical absolute action.

For clarity, its Coxeter product has exactly the required determinant, not a surrogate graph polynomial.
Set U=V^-=I-B, where B is the strict upper part of A, and let C=R_1 R_2 ... R_n with the rightmost reflection acting first.
For y=Cx, the updates occur in order n,n-1,...,1.
At the update of coordinate i, coordinates j>i already equal y_j and coordinates j<i still equal x_j.
Thus

    y_i=-x_i+sum_(j>i)A_ij y_j+sum_(j<i)A_ij x_j,
    U y=-U^T x,     C=-U^(-1)U^T,
    det(tI-C)=det(tU+U^T)=p_U(t).                       (4)

Every diagonal remains one and det U=1.
L185 supplies an eigenvalue of C greater than one.
The accepted McM02 Theorem1.1 therefore gives rho(C)>=lambda_L.
For every monic polynomial p with roots alpha_j, its full measure satisfies exp(m(p))=product_j max(1,|alpha_j|)>=max_j |alpha_j|; consequently m(p_U)>=log rho(C), proving(3) in this case.
Reciprocal pairs and neutral multiplicities are retained; no division by rank or passage to only a quotient characteristic polynomial occurs.
The source theorem includes its radical, fixed by the simple reflections, so affine or other degenerate components cause no exception.

If instead some |V_ij|>=3, the corresponding two-vertex principal adjacency block has spectral radius at least3, and a vector supported on those vertices proves rho(A)>=3.
Equations(2) then give

    m(p_(V^-))>=2 arcosh(3/2)
                    =log((7+3sqrt5)/2)>log lambda_L.    (5)

For the final comparison it suffices to use the retained actual bound lambda_L<2 and (7+3sqrt5)/2>2.
No Coxeter identification for entries of magnitude3 or more is made.
This covers all remaining integral matrices, irrespective of their components, ordering, signs or neutral factors.
Equations(4)--(5) together prove(3); the external source is used only where its canonical conventions apply.

In particular, for any fixed finite B_0>0 and any nonempty class with0<m(p_V)<=B_0,

    m(p_(V^-))/m(p_V)>=log(lambda_L)/B_0,
    m(p_W)/m(p_V)>=1+log(lambda_L)/B_0.                 (6)

Thus no sequence with uniformly bounded positive original total measure can have the L234 companion ratio tend to zero, even if rank or irreducible degree tends to infinity.
This is not a lower bound on m(p_V), and does not resolve Lehmer.
It is a lower bound on the complete EXTRA factor.
It leaves room for that extra factor to be strictly smaller than the original one, as the construction below demonstrates.
The constants in(6) are lower bounds, not claimed sharp infima at a prescribed B_0.

<a id="walsh-path-complete-determinants"></a>
### 2. A fixed signed core with a genuinely varying irreducible factor

Fix a dyadic integer r=2^h>=8.
Let H be the r-by-r Walsh matrix H_(a,b)=(-1)^(a dot b), so H^T H=H H^T=rI and |H|=J.
These exact identities and their standard Boolean-character attribution are reused from L234.
Put

    Q_s(t)=t^2-(s-2)t+1,
    a(s)=arcosh((s-2)/2),   s>4,
    V_r=[[I_r,-H],[0,I_r]].                             (7)

Select one vertex in the first block and append k>=0 new vertices after all core vertices, joined in a single path by unit entries, with the first new vertex joined to that selected core vertex and no other new edges.
Denote the actual integral upper-unitriangular matrix by V_(r,k).
All new edge signs can be chosen plus one; their squared values are one in both original and absolute leaf recurrences.

The complete original core determinant is Q_r^r.
Its selected-vertex deletion has determinant

    q_r=(t+1) Q_r^(r-1).                               (8)

To verify(8) directly, deleting the selected row of H gives an (r-1)-by-r matrix H' with H'H'^T=rI_(r-1).
The rectangular block Schur complement has one extra uncoupled dimension and r-1 identical factors ((t+1)^2-r t), proving(8) as a full polynomial identity.
It is not a projection onto a preferred spectral subspace.

Write b=r-1 and set

    F_(r,k)(t)=[t^(k+2)(t-b)-(1-b t)]/(t-1).
                                                                    (9)

L203's exact unit-leaf recurrence p_k=C_k p_0-t C_(k-1)q_r, C_j=1+t+...+t^j, now gives

    p_(V_(r,k))=Q_r^(r-1) F_(r,k).                    (10)

Indeed p_0-q_r=t(t-b)Q_r^(r-1); its actual-degree reversal produces exactly(9).
Alternatively, factoring Q_r^(r-1) out of the recurrence gives F_(r,0)=Q_r, F_(r,1)=(t+1)Q_r-t(t+1) and the same recurrence for every subsequent k.
The numerator in(9) has the explicit factor t-1, and F_(r,k) is the complete remaining monic integral reciprocal polynomial of degree k+2.
Its constant term is one.
This factorization keeps every one of the r-1 fixed positive-measure factors Q_r.

For the absolute core, |H|=J gives full determinant(t+1)^(2r-2)Q_(r^2).
Deleting the same vertex gives an all-ones (r-1)-by-r block, whose sole nonzero squared singular value is r(r-1).
Hence its complete deletion is

    q_r^-=(t+1)^(2r-3) Q_(r(r-1)).                    (11)

Define the monic quadratic seed and full growing absolute factor by

    J_r(t)=t^2-(r^2-2)t+1-r,
    A_(r,k)(t)=[t^(k+2)J_r(t)-J_r^*(t)]/(t-1),       (12)

where reversal in J_r^* is at degree2.
The core-minus-deletion identity is

    (t+1)Q_(r^2)-Q_(r(r-1))=t J_r.

Applying the SAME exact leaf recurrence, this time to the whole absolute pencil, proves

    p_(V_(r,k)^-)=(t+1)^(2r-3) A_(r,k).              (13)

For k=0, A_(r,0)=(t+1)Q_(r^2), so the original full core multiplicity2r-2 is recovered.
For every k, A_(r,k) has degree k+3, is monic integral reciprocal and has constant term one.
The displayed neutral factor has degree2r-3; any additional neutral factor inside A_(r,k) remains inside the full polynomial, rather than being silently discarded.

The literal D9 cover W_(r,k) consequently has COMPLETE determinant and entry costs

    p_(W_(r,k))=(t+1)^(2r-3) Q_r^(r-1) F_(r,k) A_(r,k),
    rank V_(r,k)=2r+k,        rank W_(r,k)=4r+2k,
    height V_(r,k)=height W_(r,k)=1,
    E(V_(r,k))=r^2+k,         E(W_(r,k))=2r^2+2k.       (14)

All matrices use the displayed standard integer basis, every diagonal entry one, and integer couplings.
The total degree in(14) is(2r-3)+(2r-2)+(k+2)+(k+3)=4r+2k.
No cyclotomic quotient or nonintegral basis change has been used to obtain the matrices.

<a id="walsh-path-root-and-factor-control"></a>
### 3. All off-circle roots and unbounded irreducible complexity

We reuse the precise elementary Salem-Boyd argument proved in L203 and attributed there to Hir06.
If a fixed real monic seed D has no root on the unit circle, t^N D-D^* has no more strictly exterior roots than D, counted with multiplicity.
For0<=epsilon<1, Rouche on the unit circle compares t^N D with epsilon D^*; passing to epsilon=1 preserves every root strictly outside in its own small disk.
On exterior disks about roots of D, the perturbation D^*/t^N tends uniformly to zero, so those exterior roots also attract roots with their full multiplicities.
Division by t-1 only removes a unit root.
No claim about singular integral interchanges or a source-wide new theorem is made.

The seed t-b, b=r-1>=7, has exactly one exterior root and no unit root.
Therefore F_(r,k) has at most one exterior root.
Its numerator, at t=b, is b^2-1>0.
At t=b-2>1, with N=k+2>=2, it is

    -2(b-2)^N-1+b(b-2)
        <=-2(b-2)^2-1+b(b-2)=-(b-3)^2<0.

Thus it has a positive root lambda_(r,k) in(b-2,b).
It is the unique exterior root, simple.
Reciprocity supplies its unique strictly contracting root lambda_(r,k)^(-1), and all other k roots lie on the unit circle.
In particular

    r-3<lambda_(r,k)<r-1,
    m(F_(r,k))=log lambda_(r,k),
    lambda_(r,k)->r-1 as k->infinity.                  (15)

The convergence follows from the same exterior-disk argument; the exact one-root count precludes a hidden exterior contribution.

Let R_(r,k) be the monic irreducible factor containing lambda_(r,k).
Since F_(r,k) is monic integral with constant one, every monic irreducible factor has constant plus or minus one.
A factor containing the only exterior root must contain the only contracting root to have absolute root product one.
Its reversal then shares that root and is the same irreducible factor after monic normalization.
This gives a reciprocal unit factor, with positive constant one: its real nonunit roots form the positive reciprocal pair, its other nonreal roots occur in conjugate pairs, and rational unit roots cannot belong to this irreducible factor.
Every other factor is cyclotomic by the same monic-integral circle-root criterion reused in L203.
Hence the complete decomposition is

    F_(r,k)=R_(r,k) C_(r,k),
    C_(r,k) contains ALL cyclotomic factors with multiplicities,
    m(R_(r,k))=log lambda_(r,k),
    deg C_(r,k)=k+2-deg R_(r,k).                       (16)

The positive factor occurs once because the exterior root is simple.
It may be quadratic for some small k; at k=0 it is exactly Q_r.
No all-k irreducibility of F_(r,k) or complete formula for C_(r,k) is claimed.

For distinct k,l these positive factors are distinct.
Indeed t-b and1-bt have no common root since b>1.
If z were a common exterior root of F_(r,k),F_(r,l), equation(9) would imply z^(k-l)=1, impossible for |z|>1.
Thus there is no common exterior root.
A common positive irreducible factor would supply one and is excluded.

Their degrees are unbounded, and in fact tend to infinity along k.
From(15), exp(m(R_(r,k)))<r-1 is a common bound at fixed r.
For any fixed degree D, the elementary coefficient estimate |c_j|<=binomial(D,j) exp(m(R)) allows only finitely many monic integral polynomials of degree at most D and that measure bound.
Since the factors in(16) are pairwise distinct, only finitely many k can have degree at most D.
This proves increasing irreducible complexity without assuming that the actual neutral degree is bounded.
In degrees greater than two these factors are Salem polynomials: they have precisely one positive real exterior root, its reciprocal, and all other conjugates on the unit circle.

For the absolute seed, put c=r^2-2 and let rho_r be its positive root.
Since J_r(c)=1-r<0 and J_r(c+1)=c+2-r=r^2-r>0,

    r^2-2<rho_r<r^2-1.

Its other root is negative, with absolute value(r-1)/rho_r<1.
Thus J_r has exactly one exterior root and no unit root.
The reused root bound shows A_(r,k) has at most one exterior root.
At t=1 its value, computed by differentiating its numerator, is

    A_(r,k)(1)=(k+2)(4-r^2-r)+2r<0.

Since it is monic it has a positive real root rho_(r,k)>1.
That root is the unique exterior root and is simple.
Reciprocity gives the sole contracting root; all others are on the circle.
Consequently

    m(A_(r,k))=log rho_(r,k),
    rho_(r,k)->rho_r.                                 (17)

All these counts apply to the full actual factors in(10),(13).
No cyclotomic multiplicity inside either growing factor is assumed away.

<a id="bounded-measure-strict-collapse-cost"></a>
### 4. Bounded full measure, strict companion collapse, and its exact limit

Equations(10),(15) give the complete original cost

    m(p_(V_(r,k)))=(r-1)a(r)+log lambda_(r,k),
    (r-1)a(r)+log(r-3)
         <m(p_(V_(r,k)))<(r-1)a(r)+log(r-1).            (18)

For every fixed r this is a uniformly bounded interval of positive TOTAL logarithmic measures, with no rank normalization.
The fixed Q_r^(r-1) contribution is part of both bounds.

On the unit circle, |t^(k+2)J_r-J_r^*|<=2|J_r|.
The logarithmic integral, with m(t-1)=0, therefore gives

    m(p_(V_(r,k)^-))=log rho_(r,k)
        <=log2+m(J_r)=log(2rho_r)<log(2(r^2-1)).        (19)

All circle zeros have integrable logarithms, so this upper bound does not need the numerator bounded away from zero.
It is the complete companion measure, not a bound on an isolated chosen root.
Together(14),(17)--(19) give

    m(p_(W_(r,k)))=(r-1)a(r)+log lambda_(r,k)
                                 +log rho_(r,k),
    m(p_(W_(r,k)))<(r-1)a(r)+log(r-1)+log(2(r^2-1)).
                                                                    (20)

A single fixed r=8 already yields the requested changed behavior.
Here Q_8=t^2-6t+1 and a(8)=log(3+2sqrt2).
The original full polynomial is Q_8^7 F_(8,k), and the complete absolute factor is(t+1)^13 A_(8,k), with seed J_8=t^2-62t-7.
Thus, for every k>=0,

    7log(3+2sqrt2)+log5
       <m(p_(V_(8,k)))<7log(3+2sqrt2)+log7,
    log lambda_L<=m(p_(V_(8,k)^-))<log126.             (21)

The lower bound in the second line is the independently sourced/local-transfer result(3); the direct positive-root proof also shows strict positivity without that external gap.
Since3+2sqrt2>5, the first original lower bound exceeds8log5.
Since126<5^4, the companion upper bound is less than4log5.
Hence the exact all-k strict comparison

    0<m(p_(V_(8,k)^-))/m(p_(V_(8,k)))<1/2,
    1<m(p_(W_(8,k)))/m(p_(V_(8,k)))<3/2              (22)

holds.
It uses complete measures and is stronger than merely less than the original cost.
This is a height-one actual family of rank16+k with bounded positive total measure and distinct positive reciprocal irreducible factors of degrees tending to infinity.
The cover has rank32+2k and full polynomial(t+1)^13 Q_8^7 F_(8,k) A_(8,k).
Its energy is128+2k.
All dimensions, neutral multiplicities and fixed positive factors remain charged.

The exact limits are also available.
The positive root of J_8 is31+22sqrt2, so

    lim_k m(p_(V_(8,k)))=7log(3+2sqrt2)+log7,
    lim_k m(p_(V_(8,k)^-))=log(31+22sqrt2),
    lim_k m(p_(V_(8,k)^-))/m(p_(V_(8,k)))
       =log(31+22sqrt2)/[7log(3+2sqrt2)+log7]>0.        (23)

There is no zero-ratio assertion.
More generally the fixed-r limit is log rho_r/[(r-1)a(r)+log(r-1)].
Letting r also tend to infinity would allow that ratio to shrink, but the original upper and lower bounds in(18) then diverge.
It would leave the bounded-total-measure class, just as(6) requires.

<a id="bounded-collapse-scope-and-contribution"></a>
### 5. Scope, discriminating continuation and contribution

The new obstruction(3)--(6) and actual family(9)--(23) answer two distinct versions of the question.
With bounded positive original total measure, vanishing companion ratio is impossible for ALL integral upper-unitriangular presentations, by an established external Coxeter theorem and the displayed elementary extension.
Strict ratio reduction can coexist with bounded total measure and a growing positive irreducible factor: the height-one path family supplies it with full factor bookkeeping.
This is not an optimization of the same rank7 P6 orbit and is not the unmodified L234 repeated-quadratic family.

The new irreducible factor R_(8,k) has measure between log5 and log7.
The full original has the additional fixed positive block Q_8^7; removing it would change the actual determinant and no integral unitriangular realization of R_(8,k) alone is supplied.
The complete original polynomial therefore remains reducible.
These facts preclude any near-one, vanishing-total-measure or irreducible-complete-target claim.
Cyclotomic factors C_(8,k) may have growing degree; their exact degree identity in(16), not an unproved uniform bound, is retained.
An upper bound for a displayed presentation is not an optimum among all presentations.

A useful changed next experiment can try to couple or replace the fixed Q_8^7 background while maintaining bounded measure and controlling the entire companion, aiming at a complete irreducible positive target or a family whose positive measure is substantially smaller.
A different route can determine a sharper optimal ratio at a chosen measure cap B_0; (6) supplies a nonzero necessary lower bound but no attainment or sharpness theorem.
Bold candidate couplings and bounded exact tests are permitted before either target is proved.
No failure above suspends other structural mechanisms, and no such experiment has been executed in this round.

The coordinator supplied only the broad bounded-measure/increasing-complexity question, authorized the identified source inspection, and requested that the canonical action and arbitrary-entry boundary be checked.
The authoring orbit_research AI supplied the reflection-product transfer, the integer-entry split, the bounded-ratio consequence, and the new fixed-Walsh-core path calculation with all root, factor and cost deductions.
The underlying spectral-radius gap is McM02's theorem, not a newly proved project theorem.
Its statement/conventions were directly read and accepted at the source record's limited depth; its full geometric/classification proof was not inspected.
The Walsh identity, block determinant, positive-companion interface, literal cover, path recurrence, exterior-root argument and bounded-degree coefficient finiteness are reused at the exact retained scopes identified above.
No theorem of universal signed realization or uninspected full Coxeter classification is asserted as a local derivation.

The complete original author SELF account is retained in [R755](../audits/reviews/Yin_R_G0755_v1.md#original-g238-author-self-finding), at its original input and date precision.
No program or numerical check was needed.
That original self-check was not an independent review; its adoption was a subsequent separate action.


Author self-check correction before freeze: the first written radical for the positive root of J_8 was31+8sqrt15.
Directly simplifying its discriminant62^2+28=3872 corrects it to31+22sqrt2, as now used in(23).
The root interval(62,63), all earlier determinant formulas and every stated inequality were unchanged.
This corrected arithmetic slip is retained here as author history, not an independent-review finding.

Author freeze: 2026-10-09T22:58.
Complete Sections1--5 and equations(1)--(23), including both the universal extra-cost obstruction and the actual bounded-measure growing-factor family, were the original frozen input of the subsequently recorded complete noncontributor review.
The compact McM02 source statement/convention record is included in the frozen dependency scope.
The author correction above is retained; no program or numerical result is present.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0782_v1.md#bounded-collapse-complete-independent-review), with its original inspected scope and relationship.
