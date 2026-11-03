---
author: Yin
---

# Complete positive-half integral realization criteria and stable norm-one boundaries

This retains the entire [L307](../ledger/Yin_L_G0307_v1.md) proof, with exact form/decomposition/scalar distinctions and every original source/cost/terminology limit.
The original full finding remains in [R784](../audits/reviews/Yin_R_G0784_v1.md#preserved-complete-original-r206-accounts), with no new source or research run.

<a id="statement"></a>
## Complete statement

Let A,D be symmetric positive-definite integral matrices of ranks r,s>=1 with det A=det D=1, and C ANY integral r-by-s matrix.
On the displayed standard integer direct sum put
    G=[[A,C],[0,D]], B=G+G^T,
    sigma_1=[[-I,-A^-1 C],[0,I]],
    sigma_2=[[I,0],[-D^-1 C^T,-I]].
Both sigma_i are integral involutions preserving B, even if the TOTAL symmetric B is indefinite or degenerate.
Their minus-one eigenspaces are precisely the two coordinate halves, and
    sigma_1 sigma_2=-G^-1G^T,
    p_G(t)=det(tG+G^T)=det(tI-sigma_1 sigma_2).
p_G is integral monic reciprocal of degree r+s and constant1; integral unimodular congruence preserves the entire polynomial.
This is a BILINEAR realization and does not itself make G proper upper unitriangular.

Call a basis adapted when each basis vector belongs to one of the two selected halves, with arbitrary interleaving/order allowed.
An adapted integral unimodular basis makes G upper unitriangular IF AND ONLY IF both halves are standard integral orthonormal lattices:
    Q_A^T A Q_A=I_r, Q_D^T D Q_D=I_s
for Q_A,Q_D integral unimodular.
In the sufficient direction the actual matrix in half order is V=[[I,C'],[0,I]], C'=Q_A^T C Q_D.
The criterion concerns the specified decomposition and does not exclude a nonadapted basis of an indefinite total form.

For ANY positive-definite integral lattice A of rank r, without a unimodularity requirement, let U(A) be the integer span of its vectors x with x^T A x=1.
It has an integral primitive orthogonal splitting
    A congruent I_u direct-sum A_0,
where u=rank U(A) and A_0 has no norm-one vector.
The deficit epsilon(A)=r-u vanishes exactly for an integral orthonormal basis and satisfies
    epsilon(A direct-sum D)=epsilon(A)+epsilon(D)
for all positive integral lattices.
Thus ANY positive orthogonal stabilization of a nonstandard positive half retains nonzero deficit and cannot repair the ADAPTED extraction.
Indefinite additions and basis mixing of an indefinite total form are outside this conclusion.

There is also a WHOLE-FORM obstruction with arbitrary basis mixing in the positive setting.
For every positive symmetric integral A with epsilon(A)>0 and EVERY integral bilinear H with y^T H y>0 for all nonzero real y, NO integral unimodular congruence of A direct-sum H is upper unitriangular.
H need not be symmetric or unimodular.
After splitting off all norm-one vectors of A, its positive complementary lattice has no such vector, so every norm-one vector of the padded form lies in a proper subspace.
No arbitrary-rank or finite-search exception is inserted.

An explicit classical E8 control A_* has diagonal2, off-diagonal-1 at the tree edges
    (0,1),(0,2),(2,3),(0,4),(4,5),(5,6),(6,7)
and zero elsewhere.
The three arm edge lengths are1,2,4.
Direct arm recurrences and the central Schur complement
    2-1/2-2/3-4/5=1/30
prove A_*>0,det A_*=1.
Its nonzero integer norms are even and at least2, with2 attained; epsilon(A_*)=8.
It obstructs EVERY basis after arbitrary positive integral bilinear orthogonal padding, while its FULL polynomial is(t+1)^8.
For k>=0 the padded polynomial(t+1)^(8+k) is separately realized by the proper identity I_(8+k), whose companion is itself and literal cover is I_(16+2k).
Thus the form obstruction is not a scalar-polynomial obstruction.
These are zero-measure controls.
A_* has rank8,height2,full-entry squared sum46,strict-upper squared sum7; identity padding gives rank8+k,height2,sum46+k,upper sum7.
Its relaxed doubled block has polynomial(t+1)^(16+2k),rank16+2k,height2,full-entry sum92+2k,upper sum14.
The diagonal2 data are RELAXED forms, not a proper D9 cover; the proper scalar identity instead has height1,energy0.

When the adapted criterion succeeds, let d=min(r,s), and let sigma_j/tau_j be ALL singular values, including zeros, of actual C'/|C'|.
The full polynomials are
    p_V=(t+1)^|r-s| product_(j=1)^d[(t+1)^2-t sigma_j^2],
    p_(V^-)=(t+1)^|r-s| product_(j=1)^d[(t+1)^2-t tau_j^2],
    p_literal_cover=p_V p_(V^-).
Every zero singular value contributes two further Phi2 factors.
For g(u)=0 at0<=u<=4 and g(u)=log[(u-2+sqrt(u(u-4)))/2] at u>4,
    m(p_V)=sum_j g(sigma_j^2),
    m(p_(V^-))=sum_j g(tau_j^2),
    m(cover)=m(p_V)+m(p_(V^-)).
These are full ordinary logarithmic measures without rank normalization.
Actual V has rank r+s,height max(1,max|C'_ij|),energy sum(C'_ij)^2, and its proper cover doubles rank/energy with the same height.
Real singular coordinates only evaluate the already specified integer matrix and change no lattice.
Neither existence of A,D,C nor zero deficits bounds C' or its absolute cost for free.

All complete local matrix, lattice, E8 and cost proofs, original contributor/source/no-program limits and the terminology clarification remain.
The phrase rootless was replaced by the precise absence of norm-ONE vectors; no absence of norm-two roots, formula change or scope strengthening was asserted.
Gro02 supplies only its selected attribution/convention comparison, not an accepted arithmetic existence/classification/ideal-class/reflection-subgroup theorem.
McM02's separate canonical Coxeter action is not extended to all lattice isometries.
No new source/native/program execution, indefinite-stabilization obstruction, scalar coverage failure, smaller positive measure or unrestricted gap is proved.

## Complete argument

<a id="argument"></a>

<a id="positive-half-lattice-reuse"></a>
### 1. Reuse, source boundary and exact changed question

The [L303 attained Lehmer tree minimum](Yin_C_G0578_v1.md#statement) is a complete actual scalar realization and cost optimum for that target.
It does not say that an arbitrary reciprocal target is realized.
The [L191 integral Gram construction](Yin_C_G0458_v2.md#integral-gram-realization-fixed-scope), [L283 charged rank-eight bipartite result](../ledger/Yin_L_G0283_v1.md), and [D9 literal signed cover](Yin_C_G0002_v1.md#signed-cover-identity) already give the appropriate determinant and cost interfaces once an actual standard integer unitriangular matrix exists.
The [L274 form-specific obstruction](../ledger/Yin_L_G0274_v1.md#all-bases-mod-four-fixed-scope) and [L279 complete rank-six scalar obstruction](../ledger/Yin_L_G0279_v1.md) have different quantifiers: neither settles arbitrary higher-rank scalar coverage or an unrelated bilinear form.
They are retained as boundaries, not rerun searches.

A bounded primary-source search for integral unitriangular/Coxeter polynomial realization found Gross's *Unramified reciprocal polynomials and Coxeter decompositions*.
The inspected edition and passages are recorded in [Gro02's selected source home](../audits/literature/Gro02/readme.md#coxeter-half-lattice-selected-inspection).
The precise useful source comparison is its Section4 distinction between positive integral half-lattices and real orthogonal root bases.
These need not give orthonormal INTEGER bases.
The later examples explicitly include a nonstandard positive half.
The canonical Coxeter group action in the already accepted [McM02 interface](../audits/literature/McM02/readme.md#canonical-coxeter-gap-input) must likewise not be replaced by a claim about all lattice isometries.
The present proof does not import Gross's arithmetic existence, ideal-class or reflection-subgroup theorems; selected reading supplies attribution and prevents this overreach.

The changed result below is a necessary and sufficient integral criterion for realizing a specified positive-half decomposition by an adapted upper-unitriangular basis.
A stable norm-one deficit proves that positive orthogonal additions cannot repair a nonstandard half.
A displayed classical eight-dimensional control also obstructs every integral basis of its positive form, even after arbitrary positive integral bilinear orthogonal padding, although its complete scalar polynomial has an elementary proper realization.
This separates a form obstruction from a scalar-polynomial obstruction without using an unproved classification or finite search.
It does not repeat the impossible basis search of L274.

All new local deductions below were developed by orbit_research for Yin.
Root supplied only the broad research assignment, source-intake coordination and review arrangement, not these derivations.
There is no new computational experiment or J; the finite displayed control is checked analytically.
No novelty claim is made for the classical norm-one lattice splitting or the E8 example.

<a id="positive-half-bilinear-coxeter-identity"></a>
### 2. An actual integral two-half form and its full polynomial

Let A and D be symmetric positive-definite integral matrices of ranks r,s>=1 and determinant one.
Let C be an arbitrary integral r by s matrix.
In the displayed standard integer direct sum define

    G = [[A,C],[0,D]],       B = G+G^T,
    sigma_1 = [[-I_r,-A^(-1)C],[0,I_s]],
    sigma_2 = [[I_r,0],[-D^(-1)C^T,-I_s]].              (1)

All matrices in(1) are integral, because unimodularity makes A^(-1),D^(-1) integral.
Both sigma_i are involutions and preserve the symmetric form B, even when B is indefinite or degenerate.
For sigma_1, set z=A^(-1)Cy and replace x by -x-z in

    (x,y)^T B(x,y)=2x^T A x+2x^T C y+2y^T D y.

The two z-quadratic terms cancel and the mixed term returns to 2x^T C y.
The sigma_2 calculation is the same with the two halves interchanged.
Their minus-one eigenspaces are exactly the respective coordinate halves.
Direct block multiplication gives

    sigma_1 sigma_2 = -G^(-1)G^T,
    p_G(t):=det(tG+G^T)=det(tI-sigma_1 sigma_2).         (2)

For example, the top row of the product in(2) is [-I_r+A^(-1)CD^(-1)C^T, A^(-1)C], fixing the sign convention.
Since det G=1, p_G is monic of degree r+s, integral, with constant term one.
Transposition gives t^(r+s)p_G(1/t)=p_G(t).
There is no suppressed determinant scalar, reciprocal factor or neutral multiplier.
Under an integral unimodular congruence G->Q^T GQ, this entire polynomial stays equal, and the action in(2) changes by similarity.

The assertion so far is an integral BILINEAR realization.
In general G does not have diagonal one, so it is not a proper matrix in the D9 scalar/cover class.
Likewise real changes of coordinates can make A and D identity matrices but need not preserve the integer lattice.
No such real coordinate change discharges the following integral problem.

<a id="adapted-unitriangular-basis-criterion"></a>
### 3. Exact adapted-basis criterion and stable defect

Call a basis adapted if every basis vector lies in one of the two displayed summands, allowing any interleaving or ordering of the chosen vectors.
Then the following conditions are equivalent:

1. Some adapted integral unimodular basis makes G upper unitriangular.
2. A and D each have an integral orthonormal basis: there exist Q_A in GL_r(Z), Q_D in GL_s(Z) with Q_A^T A Q_A=I_r and Q_D^T D Q_D=I_s.

To prove necessity, an adapted integral basis supplies integer bases of both direct summands.
Indeed linear independence bounds the number of columns in each half by its rank, and full spanning forces both bounds to be equalities; expressing a vector of one summand in the full basis then uses only its own columns.
Restrict the transformed bilinear form to the selected columns from one half.
This restriction is symmetric.
For each distinct pair of those columns, the lower entry is zero by upper triangularity and the upper entry is the same by symmetry.
Both are therefore zero, while all diagonal entries are one.
This proves the required orthonormality independently of the interleaving.

For sufficiency, order the two orthonormal bases by halves.
The actual matrix is

    V = [[I_r,C'],[0,I_s]],       C'=Q_A^T C Q_D.        (3)

This is integral upper unitriangular, obtained by an explicitly specified integral congruence with determinant plus or minus one.
This criterion concerns bases adapted to the selected decomposition.
It makes no assertion that every unitriangular basis of an indefinite G must be adapted.

Here is an intrinsic way to evaluate its two lattice conditions.
For a positive-definite integral lattice with Gram matrix A of rank r, let U(A) be the integer span of its norm-one vectors, where norm means x^T A x.
Two norm-one vectors v,w have integral inner product.
By the Cauchy inequality it is in {-1,0,1}; equality in magnitude forces w=+v or -v.
Thus representatives of distinct sign pairs are orthogonal.
There are finitely many norm-one vectors by positive definiteness, and choosing one from each sign pair gives an orthonormal set v_1,...,v_u, with u<=r.
Every integer lattice vector x has the integral orthogonal decomposition

    x = sum_(i=1)^u <x,v_i> v_i
        + [x-sum_(i=1)^u <x,v_i> v_i].                  (4)

The bracket lies in the lattice and is perpendicular to every v_i.
This proves an integral orthogonal splitting A congruent to I_u direct-sum A_0.
The complement A_0 has no norm-one vector, since any such vector would have belonged to the enumerated set.
In particular U(A) is primitive, and the splitting has no finite-index error.
Define

    epsilon(A) = r-u.                                    (5)

It vanishes exactly when A is integrally congruent to I_r.
For two positive integral lattices, a norm-one vector in their orthogonal direct sum lies wholly in one summand: both nonzero components would have positive integer norm and hence sum at least two.
Consequently

    epsilon(A direct-sum D)=epsilon(A)+epsilon(D),
    epsilon(A direct-sum I_k)=epsilon(A).                 (6)

No unimodularity is required for(4)--(6); it is used in Section2 for the integral involutions.
Thus any positive orthogonal stabilization of a nonstandard positive half retains a nonzero deficit, and cannot yield an adapted upper-unitriangular realization.
This remains true for arbitrarily many positive integral added summands, not merely a bounded rank or a finite root search.
Indefinite additions or a basis mixing the original halves can escape the statement; neither is excluded by(6).

<a id="positive-padding-global-norm-one-obstruction"></a>
### 4. A global positive-padding obstruction with the same realizable scalar

For an exact classical control, take the eight-vertex tree with central vertex0 and arms of edge lengths1,2,4.
Its edges are

    (0,1), (0,2), (2,3), (0,4), (4,5), (5,6), (6,7).

Let A_* have diagonal2, entry-1 on each edge in both directions, and all other entries zero.
This is the usual E8 Cartan-lattice control, whose relevant properties are verified here from the entries; no classification theorem is invoked.
The length-l arm matrix K_l has diagonal2 and adjacent entries-1.
Its quadratic form equals the sum of the squared adjacent differences plus the two squared endpoint coordinates, so it is positive definite.
Its determinants satisfy d_l=2d_(l-1)-d_(l-2), d_0=1,d_1=2, hence d_l=l+1.
Its inverse entry at the attachment endpoint is d_(l-1)/d_l=l/(l+1), by the cofactor formula.
Eliminating the three positive arm blocks leaves the central Schur complement

    2-1/2-2/3-4/5 = 1/30,
    det A_* = (2*3*5)/30 = 1.                            (7)

It follows both that A_* is positive definite and that it is unimodular.
Its integer quadratic values are even, because its diagonal entries are even and each off-diagonal term occurs twice.
Every nonzero integer vector therefore has norm at least two.
The standard coordinate vectors attain two.
Hence epsilon(A_*)=8.

There is a stronger basis obstruction for the symmetric bilinear form G_*=A_*.
Let H be ANY integral bilinear form whose quadratic values q_H(y)=y^T H y are positive for all nonzero real y.
H need not be symmetric or unimodular.
For the integral orthogonal direct sum G_* direct-sum H, every norm-one integer vector has its first eight coordinates zero: a nonzero first component contributes at least two, and the other contributes a nonnegative integer.
All norm-one integer vectors thus lie in a proper real subspace of codimension at least eight.
No collection of them can be a full integer basis.
In particular no integral unimodular congruence of G_* direct-sum H can be upper unitriangular, whose basis columns would all have norm one.
This argument allows complete mixing by the proposed new basis; it is not confined to adapted bases.

The exact same proof works with any nonzero positive integral lattice having no norm-one vector in place of A_*.
It also applies after first splitting off all unit vectors by(4).
For a positive symmetric A with epsilon(A)>0 and any positive integral bilinear H, its summand with no norm-one vector contributes no component to any norm-one vector of A direct-sum H.
Thus this more general whole-form obstruction also survives arbitrary positive integral bilinear orthogonal padding.
It is a positivity/norm-one-span argument, not a universal statement about indefinite stabilization.

For G_* the complete polynomial and its positive identity padding are

    p_(G_*)(t)=(t+1)^8,
    p_(G_* direct-sum I_k)(t)=(t+1)^(8+k).              (8)

The equalities use det A_*=1, not normalization by an unrecorded content.
They demonstrate why the form obstruction is not a scalar obstruction: the proper upper-unitriangular matrix I_(8+k) has precisely the same full polynomial.
Its absolute companion is itself and its literal proper cover is I_(16+2k), with complete polynomial (t+1)^(16+2k).
Every measure is zero; its rank is8+k, height1 and squared strict-upper energy0.
This is a neutral comparison, not a new positive-measure seed or near-one success.

All matrix costs for the obstructed form are also explicit.
A_* has rank8, height2, determinant1, fourteen nonzero off-diagonal entries, squared full-entry sum46, and squared strict-upper sum7.
For A_* direct-sum I_k these become rank8+k, height2, full-entry sum46+k and strict-upper sum7.
Since all its off-diagonal entries are nonpositive, replacing them by their negative magnitudes leaves this form unchanged.
Its relaxed two-copy block sum has polynomial (t+1)^(16+2k), rank16+2k, height2, full-entry sum92+2k and strict-upper sum14.
These are RELAXED bilinear data only.
The diagonal2 entries remain, so neither this block sum nor the number7 is being identified with a proper D9 cover realization of the obstructed form.
Its scalar polynomial separately has the proper identity realization just described.

<a id="positive-half-complete-cost-interface"></a>
### 5. Complete costs when the integral criterion succeeds

When the criterion of Section3 succeeds, (3) is an actual matrix and the existing bipartite formulas apply.
For clarity the entire polynomial is retained here, with no factor discarded.
Put d=min(r,s), and let sigma_1,...,sigma_d be all singular values of C', including zeros.
Orthogonal singular-value coordinates in the determinant, used only to EVALUATE the actual integer matrix, give

    p_V(t)=(t+1)^|r-s|
           product_(j=1)^d [(t+1)^2-t sigma_j^2].       (9)

In particular zero singular values contribute two further Phi2 factors.
The absolute companion V^- has the same diagonal blocks and cross block -|C'|.
If tau_1,...,tau_d are all singular values of |C'|, its full polynomial is the right side of(9) with sigma_j replaced by tau_j.
These assertions follow by pairing the singular directions in the two blocks of tV+V^T; they are the direct specialization of the retained L191/L283 interface, not a new realization theorem.

Define g(u)=0 for 0<=u<=4 and

    g(u)=log[(u-2+sqrt(u(u-4)))/2] for u>4.

Each factor in(9) has reciprocal roots and trace u-2.
It has both roots on the unit circle when0<=u<=4; for u>4 it has one positive root greater than one, given by the argument of the logarithm.
Therefore the complete ordinary logarithmic measures, without a division by rank, are

    m(p_V)=sum_j g(sigma_j^2),
    m(p_(V^-))=sum_j g(tau_j^2),
    m(p_W)=m(p_V)+m(p_(V^-)).                            (10)

Here W is the literal proper signed cover of D9, so its whole polynomial is p_V p_(V^-).
The proper matrix rank is r+s, height max(1,max_ij|C'_ij|), and energy E=sum_ij(C'_ij)^2.
The proper cover has rank2(r+s), the same height, and energy2E.
Empty/zero cross blocks have height1.
These formulas charge every neutral factor, degree, and extra companion contribution.
Orthogonality over R in the determinant calculation never changes the integer matrix used to define these costs.

No uniform bound on C' or on the ratio in(10) follows just from the existence of A,D,C in(1).
Even when epsilon(A)=epsilon(D)=0, such bounds require the actual resulting integer cross block.
Conversely epsilon>0 prevents this adapted extraction but does not prove that the scalar polynomial lacks another proper representation.
Equations(8) give an exact counterexample to that invalid implication.

<a id="half-lattice-coverage-boundary"></a>
### 6. What the new discriminator settles and leaves open

The local criterion makes a potentially useful arithmetic strategy precise.
Given a genuine two-involution realization with positive unimodular halves, first compute their norm-one spans and deficits.
Vanishing deficits produce the actual matrix(3) and the full costs(9)--(10).
Positive deficits show that positive orthogonal additions to those halves cannot repair this particular adapted construction, at any rank.
A real orthogonal basis, a lattice isometry with the desired characteristic polynomial, and an arithmetic Coxeter decomposition alone do not settle this integral unitriangular gate.

The source examples with nonstandard halves are relevant motivation, but their arithmetic or Salem assertions are not newly adopted here.
For such an example our adapted criterion is conditional on the displayed half-lattice data being independently supplied.
The proof's unconditional concrete control is(7)--(8), whose entire algebra is given above.
There is no claim that the source's nonstandard half excludes every possible scalar realization of its polynomial.

The next changed tests remain open: a different decomposition of the SAME integral form, a basis mixing halves when the total quadratic form is indefinite, an explicitly paid indefinite stabilization, or a different form with the same entire scalar polynomial.
Any successful test must still produce the standard integer unit diagonal and evaluate the complete absolute companion.
In the positive control of Section4, changing the form rather than merely its basis is essential and is explicitly possible.
L303 remains the attained positive Lehmer-target benchmark, while none of this argument produces a lower positive total measure or solves unrestricted G0001.

<a id="half-lattice-author-self-check"></a>
### 7. Author self-check and actual evidence boundary

The author checked all blocks and signs in(1)--(2), the determinant-one normalization and reciprocity, necessity for every interleaving in Section3, the integer coefficients in(4), the exact positive-direct-sum quantifier in(6), the arm determinants and Schur complement1/30 in(7), the stronger whole-form padding argument, and every full scalar/relaxed/proper cost distinction in(8)--(10).
The eight-dimensional example uses rank8 and arm lengths1,2,4; it is not the Lehmer tree of arms1,2,6.
No root-count computation, numerical spectrum, finite experiment, unrecorded failure or new program is involved.

The Gro02 inspection was bounded and selective: it did not read Proposition4.5's entire proof and does not accept its classification.
The exact source home retains successful acquisition and failed rendering/extraction facts; root owns canonical intake.
The classical norm-one splitting, E8 terminology and bipartite determinant mechanism are not claimed as new.
The present contribution is their complete local integral criterion, stable-domain obstruction and actual scalar/form/cost separation for this route.
Root supplied no mathematical derivation.
The complete original author self-check and later R206 whole finding remain at their actual inputs; current adoption is governed by the explicit current assessment below.

<a id="norm-one-terminology-review-clarification"></a>
### Review terminology clarification

During the whole written review, root identified that Section4 had used the word "rootless" for absence of norm-one vectors.
That word can instead mean absence of norm-two roots, and A_* explicitly has norm-two vectors.
The author replaced both uses and the nearby "root-span" phrase by precise norm-one terminology.
The hypotheses, formulas, proofs and claimed obstruction are unchanged; no absence of norm-two roots was proved or needed.
This clarification is retained as a resolved review observation, not a change of mathematical scope.




## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:49 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full determinant product, doubled actual rank/energy only after an actual proper upper-unitriangular integer extraction. |
| support | [Existing exact Gram mechanism](Yin_C_G0458_v2.md#integral-gram-realization-fixed-scope) | Established bipartite determinant/cost convention; all rectangular/singular-value factors and costs are displayed and proved locally here. |
| support | [Exact attained Lehmer benchmark](Yin_C_G0578_v1.md#statement) | A scalar realization of that exact target is a comparison, not arbitrary coverage or an arithmetic premise for the positive-lattice criterion. |
| support | [Original entire proof/input](../ledger/Yin_L_G0307_v1.md#complete-retained-proof-and-review) | Complete Sections1--7/equations1--10, all adapted/global/positive/indefinite quantifiers, explicit classical control, source/no-program limits and retained norm-one clarification with original R206 input. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:55 |
| status | proved |
| reason | Adopt after actual whole SELF of the entire published Statement and complete Argument; original unknown review arrangements remain unknown and no isolated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full determinant product, doubled actual rank/energy only after an actual proper upper-unitriangular integer extraction. |
| support | [Existing exact Gram mechanism](Yin_C_G0458_v2.md#integral-gram-realization-fixed-scope) | Established bipartite determinant/cost convention; all rectangular/singular-value factors and costs are displayed and proved locally here. |
| support | [Exact attained Lehmer benchmark](Yin_C_G0578_v1.md#statement) | A scalar realization of that exact target is a comparison, not arbitrary coverage or an arithmetic premise for the positive-lattice criterion. |
| support | [Original entire proof/input](../ledger/Yin_L_G0307_v1.md#complete-retained-proof-and-review) | Complete Sections1--7/equations1--10, all adapted/global/positive/indefinite quantifiers, explicit classical control, source/no-program limits and retained norm-one clarification with original R206 input. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0759_v1.md#positive-half-whole-self) | Entire current Statement and complete original proof chain, every actual domain/cost/source/native/negative qualification; SELF with prior context, not a replacement of historical UNKNOWN independent scope. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:26 |
| status | proved |
| reason | Adopt the ENTIRE unchanged current Statement and all complete mathematical Arguments after the actual isolated whole review, necessary fixed interfaces and bounded original finite-evidence check where applicable; all original mathematical/source/native/correction/negative scopes and historical checking relationships remain distinct. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Literal proper signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Full determinant product, doubled actual rank/energy only after an actual proper upper-unitriangular integer extraction. |
| support | [Existing exact Gram mechanism](Yin_C_G0458_v2.md#integral-gram-realization-fixed-scope) | Established bipartite determinant/cost convention; all rectangular/singular-value factors and costs are displayed and proved locally here. |
| support | [Exact attained Lehmer benchmark](Yin_C_G0578_v1.md#statement) | A scalar realization of that exact target is a comparison, not arbitrary coverage or an arithmetic premise for the positive-lattice criterion. |
| support | [Original entire proof/input](../ledger/Yin_L_G0307_v1.md#complete-retained-proof-and-review) | Complete Sections1--7/equations1--10, all adapted/global/positive/indefinite quantifiers, explicit classical control, source/no-program limits and retained norm-one clarification with original R206 input. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0784_v1.md#positive-half-current-independent) | Entire exact current Statement and complete Argument, every original quantified input, complete proof chain/cost, actual finite versus universal evidence, source-depth/contribution/correction/negative limit; real independently reviewed arrangement and exact current bindings in R784. |

