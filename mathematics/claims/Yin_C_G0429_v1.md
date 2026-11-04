---
author: Yin
---
# Complete simultaneous root-basis and ordering reductions with both scalar targets

The complete original L254 theorem, exact finite evidence and all negative/source/cost boundaries are retained here with the necessary existing elementary interfaces explicit.
L254 retains substantive construction history, failed outcomes, source-search limits and the actual original fixed review inputs.
No Task/E execution resumes.

## Statement

In the standard integer lattice Z^6 use the exact G0 and ordered norm-two path basis Q0 displayed in the proof, with H=Q0^T G0 Q0.
For every pair0<=i<j<=5 and every c,d in Z^6, replacing only columns i,j by Q0 c,Q0 d gives an admissible integral norm-two basis if and only if

    c_i d_j-c_j d_i in{+1,-1}, c^T H c=d^T H d=2.

Reconstruct V with diagonal one and strict upper entries equal to the new Gram entries.
Its full reciprocal polynomial is t^6+a t^5+b t^4+c0 t^3+b t^2+a t+1, with c0=-3-2a-2b and p_V(-1)=5+4b=Pf(V-V^T)^2.
Thus the entire F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1 is equivalent to(a,Pf)=(-2,+/-3), and the entire S6=t^6-t^4-t^3-t^2+1 to(a,Pf)=(0,+/-1).

For every fixed ordered norm-two basis, all independent column signs, cyclic rotations and reversal preserve BOTH complete original and absolute-companion polynomials, hence the full literal-cover polynomial and unnormalized costs.
For six distinct labelled vectors, exactly60 order representatives suffice.
This remains valid for a degenerate absolute Gram; it is no classification of all integral bases.

Let R be every r in{-1,0,1}^6 with r^T G0 r=2.
There are114 such roots.
For every pair of distinct path positions and every ordered r,s in R, admit the basis exactly when its replacement minor is+/-1, and call it genuine when neither r nor s equals its own original column up to sign.
Among all such genuine bases, EVERY subsequent ordering and independent sign choice realizes neither F nor S6.
The complete fixed-order scope has194940 pairs,64736 unimodular,3220 discarded old controls,61516 genuine pairs,11248 Pfaffian+/-3 cases and zero F targets.
Sign normalization and unordered deduplication give7446 bases and446760 order representatives, with79867 Pfaffian+/-3 cases,71095 Pfaffian+/-1 cases and no corresponding target coefficient.
Their missing classes a=2 mod4 and a=0 mod4 are assertions ONLY on this finite class.
Arbitrary reorderings of the discarded3220 old controls remain outside this exclusion; the fixed-order one-column theorem does not discharge them or the secondary target.

For any fixed first norm-two c and positions i<j, the unrestricted second root d realizes a prescribed target exactly when the two linear minor/Pfaffian equations and the two quadratic norm/first-coefficient equations4 hold, with all signs, integrality, divisibility and dependent/inconsistent cases retained.
No elimination, integer solution or unbounded nonexistence is asserted.

The scalar S6 is irreducible of degree six, with one positive expanding/contracting pair and four nonreal circle roots, no neutral factor and0<m(S6)<m(P4).
No matrix realizing S6 was found, and no minimality, source priority or near-one theorem follows.
Every actual finite-class V has rank6, height at most3, energy between17 and69 and0<m(p_V)<=log524880.
Its complete absolute companion has0<=m(p_minus)<=log524880; the literal integral cover has rank12, height at most3, twice the energy and ENTIRE polynomial p_V p_minus, with measure at most2log524880.
All neutral/repeated factors remain charged.
The unchanged achieved quartic and different sextic comparison controls retain their complete original/absolute/cover factors and costs below.
No new target realization, cost optimum, arbitrary-root congruence obstruction or unrestricted gap is proved.

<a id="argument"></a>
## Complete argument

### Explicit consumed seed, reflection, sign and full-cover interfaces

The following complete argument retains original Sections1--5/equations1--6, including the actual original pre-run declarations, negative outcomes and source-search limits.
Those declarations describe2026-10-10 history; no Task/E, discovery scan, source-proof reading or source intake resumes here.
The original proof, author execution/contribution/failure account and fixed R117 inputs remain in L254.

The exact standard-lattice input is

    G0=[[2,1,1,1,1,1],
        [1,2,1,-1,-1,1],
        [1,1,2,1,-1,-1],
        [1,-1,1,2,1,-1],
        [1,-1,-1,1,2,1],
        [1,1,-1,-1,1,2]],
    Q0=(e0,e1-e0,e2-e1,e3-e2,e4-e3,e5-e4).

Put C0=G0-2I.
Direct integer multiplication gives C0^2=5I and tr C0=0, so its eigenvalues+sqrt5 and-sqrt5 each have multiplicity3.
Consequently det G0=(4-5)^3=-1 and its inertia is(3,3).
Q0 is upper triangular with diagonal one; its columns have G0-norm two, and its inverse sends r to the exact suffix sums c_i=sum_(k=i)^5 r_k.
These are the actual seed/reflection/endpoint interfaces already fully retained in [C415v2](Yin_C_G0415_v2.md#argument); no binary-forest exclusion is needed for the present changed-basis theorem.

For ANY symmetric6-by-6 Gram K with diagonal two, let V be its upper-unitriangular reconstruction.
Reflection at coordinate i is S_i x=x-(Kx)_i e_i and satisfies S_i^2=I because K_ii=2, even if K is singular.
Applying indices5 down to0, the updated coordinates obey

    y_i=-x_i-sum_(j<i)K_ij x_j-sum_(j>i)K_ij y_j,
    V y=-V^T x.

Thus S_0 S_1 ... S_5=-V^(-1)V^T and its characteristic polynomial is p_V=det(tV+V^T).
Since det V=1, this polynomial is monic integral of degree six with constant one.
Transposing tV+V^T gives t^6 p_V(1/t)=p_V(t); no Gram nondegeneracy is needed.
Cyclic products are conjugate by invertible individual reflections, and reversing the product gives its inverse.
The characteristic polynomial of that inverse is the same reciprocal polynomial because the dimension is even and its determinant is one.
Apply this entire calculation also to K^- with diagonal two and off-diagonal-|K_ij|, including singular K^-.
A diagonal column sign change D gives V->D V D and leaves its determinant polynomial unchanged; the absolute companion is unchanged entrywise.
This proves all sign/order invariances used in Section2 for both full factors.

For completeness, the literal signed cover has diagonal2-by-2 blocks I2 and block a I2 for a=V_ij<=0, or-a S for a>0, with S=[[0,1],[1,0]].
The equal-sheet and opposite-sheet rational subspaces are invariant for W and W^T; their restrictions are V^- and V respectively.
Therefore det(tW+W^T)=p_minus p_V and ordinary logarithmic Mahler measure is additive, with no rank division or removed factors.
Each original entry produces exactly two entries of the same magnitude, proving height preservation and energy doubling.
This is exactly the adequate existing [C2 signed-cover identity](Yin_C_G0002_v1.md#signed-cover-identity), reused at that interface rather than a new cover theorem.

<a id="two-column-exact-reduction"></a>
### 1. Reused inputs and exact changed construction

The original2026-10-10 work read the then-current Task/strategy and knowledge-reuse/computation rules.
The complete [L250 single-column proof](../ledger/Yin_L_G0250_v1.md#unbounded-path-column-fixed-scope), [L246 seed and binary model](../ledger/Yin_L_G0246_v1.md#rank-six-root-basis-discovery), and the actual [D9 signed-cover identity](Yin_C_G0002_v1.md#signed-cover-identity) supply the needed inputs.
The source screen reused L246's precise HPM22 attribution boundary and searched the responsible fixed inputs and local registry for the two-column/target mechanism.
These inputs suffice for the following elementary determinant expansion and changed finite test.
No fresh source theorem, classification claim, literature-wide absence claim or novelty claim is needed or asserted.

Keep L246's actual G0=2I+C and ordered path basis Q0=(e0,e1-e0,...,e5-e4).
Its Gram H=Q0^T G0 Q0 is

    H=[[2,-1,0,0,0,0],
       [-1,2,-1,-2,0,2],
       [0,-1,2,1,-2,-2],
       [0,-2,1,2,1,-2],
       [0,0,-2,1,2,1],
       [0,2,-2,-2,1,2]].

For two distinct positions i<j, replace their columns by Q0 c and Q0 d.
Leave the other four columns fixed.
Expanding the coordinate-change determinant on those four unchanged columns gives

    det Q = c_i d_j-c_j d_i.                              (1)

Thus the displayed vectors form an actual standard integral basis if and only if this minor is +1 or -1.
Both replacement columns have norm two exactly when

    c^T H c=2,  d^T H d=2.                               (2)

There is no constraint that their mutual product be small.
Reconstruct V with diagonal one and strict upper entries equal to the new Gram entries.
Then V is integral upper-unitriangular, V+V^T=Q^T G0 Q, and det(V+V^T)=-1.
Unlike a bilinear congruence of an existing V, this reconstruction can change its polynomial.

For any admissible such basis write

    p_V(t)=t^6+a t^5+b t^4+c0 t^3+b t^2+a t+1.

Reciprocity, determinant one and the endpoint expansion give

    c0=-3-2a-2b,
    p_V(-1)=5+4b=Pf(V-V^T)^2.                            (3)

Consequently the COMPLETE prescribed target

    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1,
    P4=t^4-t^3-t^2-t+1

is equivalent to a=-2 and Pf(V-V^T)=+3 or -3.
This is L250's full polynomial reduction at its stated endpoint hypotheses; it is reused, not a new endpoint theorem.
The coefficient a is tr(V^(-1)V^T); the sign follows from p_V=det(tI+V^(-1)V^T).

Before any execution, the bounded discovery scope is declared as follows.
Enumerate every r in {-1,0,1}^6 with r^T G0 r=2 (L246 recorded114 such roots, to be recomputed), every pair of distinct positions i<j, and every ORDERED pair of these roots r,s.
Put c=Q0^(-1)r and d=Q0^(-1)s, so c_i=sum_(k=i)^5 r_k and similarly for d.
The complete Cartesian scope has15*114^2=194940 pairs.
Filter the exact minor(1), and separate cases where either inserted column equals its old column up to sign; those are previously excluded one-column controls, not new construction evidence.
Every retained new candidate must satisfy(2), then the exact signed Pfaffian and coefficient equations(3).
A target hit requires an additional full polynomial expansion, actual basis/Gram verification and complete absolute/cover accounting.
This is a finite short-root test only: even a complete unsuccessful enumeration would not exclude unbounded two-column replacements, changed orderings or other lattices.


<a id="ordering-exact-reduction"></a>
### 2. A reusable reduction for a genuinely changed order

For a fixed integral norm-two basis with Gram G, changing its order reconstructs a new V and can change p_V.
However, cyclically rotating the order preserves p_V: the corresponding reflection product is cyclically conjugate, because each reflection is invertible.
Reversing the order replaces the reflection product by its inverse, which has the same characteristic polynomial here by reciprocity and determinant one.
These statements follow from the actual reflection-product identity already checked in L246; they do not assume a Coxeter classification theorem.

The same two invariances hold simultaneously for the COMPLETE absolute companion.
Its symmetric Gram has diagonal two and off-diagonal entries -|G_ij|.
The same coordinate-update reflection identity applies to this signed Gram whether or not it is nonsingular.
Individual norm-two reflections are invertible even if the whole Gram is degenerate.
Its polynomial is again reciprocal, so the same cyclic/reversal argument applies.
Consequently both complete polynomials, and thus the literal cover polynomial and unnormalized Mahler cost, depend only on the order up to cyclic rotation and reversal.
The rank, entry height and energy are also unchanged by ordering, directly from the multiset of Gram entries.

For six labelled distinct basis vectors, every cyclic class has exactly one representative beginning with label0.
Reversal pairs the resulting120 orders without a fixed point, since the remaining five distinct labels cannot form a palindrome.
Thus there are exactly60 representatives, for example all orders(0,p1,...,p5) with p1<p5.
Testing these60 orders is complete for the pair of full determinant polynomials of THIS fixed basis.
It is not an equivalence or finite classification of all integer bases.
This observation provides a changed-order test if the first fixed-order two-column experiment is unsuccessful; any such subsequent finite scope will be declared separately before execution.


The first fixed-order experiment has now actually completed:194940 pairs,64736 unimodular pairs,3220 old single-column controls,61516 genuine two-column candidates,11248 target-Pfaffian candidates, and zero full targets.
All original roots and per-position counts are retained.
This is a finite failure, not an all-integer obstruction.

Before the changed-order extension, declare its scope: normalize each of the six columns by making its first nonzero coordinate positive, sort the resulting six columns and deduplicate this unordered set over all61516 genuine candidates.
The four independent signs on the two replacement roots are already present in the complete Cartesian range and give the same unordered normalized basis.
Thus there are at most61516/4=15379 different bases, possibly fewer because of additional coincidences.
Test all60 representatives from Section2 for every such basis, at most922740 exact order tests.
Every full-target hit will be retained, with no asserted minimum over other roots, bases, lattices or matrices.
This extension changes the order of a simultaneously modified basis; it is not a larger trial inside L250's excluded class.


The changed-order extension completed with7446 distinct normalized unordered bases and446760 order tests;79867 orders had target Pfaffian and none had a=-2.
Before a final diagnostic on this SAME finite set, declare a changed scalar target

    S6=t^6-t^4-t^3-t^2+1.

This is an explicitly displayed secondary algebraic target, with local trace polynomial u^3-4u-1.
A primary-source web search returned snippets identifying the same polynomial in McMullen's author-hosted `pos/pos.pdf` and Lanneau--Thiffeault's small-genus table.
No primary page from those works was inspected or adopted, and no classical-minimality, priority or new-scalar claim is made.
These remain unadopted discovery leads; an attribution or minimality use would require scoped primary inspection.
The facts needed to justify this secondary target are proved directly below.
This final diagnostic examines exactly the same7446 bases and60 orders, with Pfaffian+/-1 and a=0, and retains every hit.
There is no new root cube, basis or order beyond the already enumerated446760.
A successful matrix would be a new local realization/control for this known input; a failure would remain a finite negative result.
No smallest-degree claim or new source theorem is imported.


<a id="two-column-finite-exclusion"></a>
### 3. Complete finite outcomes and a useful unbounded reduction

The three completed tests give the following exact finite conclusion.
Among every genuine simultaneous replacement of two distinct path columns by two actual G0-norm-two roots in {-1,0,1}^6, and EVERY subsequent ordering and independent sign choice, neither F=Phi6 P4 nor S6 is realized.
The qualifier genuine excludes only cases where an inserted column equals its own old column up to sign.
Such discarded cases were counted in the fixed-order test, but their arbitrary reorderings are NOT included in this new finite conclusion or silently discharged by L250.
The7446-base ordered class is exactly the genuine class specified here.

For F the fixed-order counts are194940 total pairs,64736 unimodular pairs,3220 single-column controls,61516 genuine pairs,11248 target-Pfaffian cases and zero targets.
For arbitrary ordering,7446 distinct normalized unordered bases give446760 representatives and79867 cases with Pfaffian +/-3; none has a=-2.
For S6, on exactly that same set,71095 representatives have Pfaffian +/-1; none has a=0.
The complete coefficient histograms, root list and position counts are retained in J55.
The scalar condition for S6 is exact: (3) gives b=-1,c0=-1 when a=0 and Pf^2=1.

The finite histograms exhibit an additional pattern: among these Pfaffian +/-3 cases, a is never2 modulo4; among these Pfaffian +/-1 cases, a is never0 modulo4.
Both missing target coefficients are therefore excluded by the observed residue classes.
This statement quantifies ONLY over the completely enumerated finite class.
It is not a proof that a modular obstruction survives arbitrary integer root sizes, other simultaneous changes or other lattices.
No residue-class extension is inferred by sampling.

The algebra explains an actionable next test without another unchanged scan.
Fix an actual first root c of norm two and the first replaced position i, and leave the second root d at position j unrestricted.
The basis determinant

    ell_c(d)=c_i d_j-c_j d_i

is linear in d.
The signed alternating Pfaffian is also a linear form in d, because each perfect matching uses the varying row/column once, including its product with the fixed c.
The remaining first polynomial coefficient a(d) has degree at most two: each determinant term uses the varying row at most once and varying column at most once.
The Gram diagonal of the reconstructed V stays one during this polynomial calculation; the separate norm equation supplies admissibility.
Hence the ENTIRE target problem for that fixed c is exactly

    ell_c(d)=epsilon,  Pf_c(d)=delta,
    d^T H d=2,        a_c(d)=a_target,                     (4)

with epsilon=+/-1, and (delta,a_target)=(+/-3,-2) for F or(+/-1,0) for S6.
If the two linear equations are independent over Q, they leave four rational free variables, but every integrality/divisibility condition must remain.
If dependent or inconsistent, that case must be treated separately.
No rational solution, canceled denominator or small nonzero minor substitutes for an integer basis.
This is a reusable exact reduction for an unbounded continuation; no elimination, complete congruence obstruction or solution of (4) is claimed in this round.

The next meaningful choices are to test the observed congruence pattern against (4) with an unrestricted second root, to replace three columns, or to change the lattice/seed.
Merely enumerating more orders of the same7446 bases cannot alter the present exact outcome.
The restricted finite failure neither pauses S3/S6 nor excludes a general realization of F.

<a id="secondary-sextic-local-facts"></a>
### 4. Why the secondary polynomial is a smaller complete scalar target

The following direct facts about S6 justify that particular diagnostic, without a source classification or an achieved matrix.
Write

    S6=t^3 q(t+t^(-1)),  q(u)=u^3-4u-1.

The rational-root candidates +/-1 are not roots, so q is irreducible over Q.
Its signs place one root in each of(-2,-1),(-1,0),(2,9/4): q(-2)=-1,q(-1)=2,q(0)=-1,q(2)=-1,q(9/4)=89/64.
These three disjoint sign intervals account for all roots, and all are simple.
The trace field is totally real and u^2-4 is negative at each of the first two real embeddings; it cannot be a square in that field.
Thus t^2-u t+1 is irreducible over it.
Since u=t+t^(-1) belongs to the field generated by t, S6 is irreducible of degree six.
Its roots comprise one positive expanding/contracting pair and four nonreal circle roots.
If lambda is its expanding root, then

    m(S6)=log lambda=arcosh(u_+/2)>0.

The quartic expanding trace u4=(1+sqrt13)/2 exceeds9/4.
Therefore lambda<beta4 and m(S6)<m(P4).
There is no neutral factor in this polynomial.
HOWEVER no matrix in the tested class realizes it.
These are facts about a displayed scalar target, not a new smaller-measure realization, a minimum theorem, a near-one family or a theorem extracted from an uninspected source.
The external identity/minimality leads above are not proof premises and were not selected for source intake.

<a id="two-column-complete-cost-scope"></a>
### 5. Full determinant and cost boundaries

No new target matrix was found, so no target companion is assigned a small or numerical measure.
The requested F has degree6, neutral factor Phi6 of degree2 and original measure log beta4.
The secondary S6 has degree6, no neutral factor and the smaller original measure just proved.
A realization of either would require its own actual complete extra factor p_(V^-); none is supplied by the finite failure.

Every actual candidate in the enumerated class is an integral6-by-6 upper-unitriangular matrix with actual norm-two standard basis and det(V+V^T)=-1.
The exact energy histogram over the7446 unordered normalized bases ranges from17 to69, and the largest strict-upper magnitude is3.
These costs are unchanged by ordering and column signs.
For any such candidate define

    V^-_ii=1,  V^-_ij=-|V_ij| for i<j,
    p_V=det(tV+V^T),  p_minus=det(tV^-+(V^-)^T).

The actual literal signed cover from D9 has2-by-2 diagonal blocks I2 and, for a=V_ij, upper block a I2 when a<=0 and -a[[0,1],[1,0]] when a>0.
Thus its standard integer rank is12, its height is at most3 and its energy is twice that of V.
The complete identity is

    p_W=p_V p_minus,
    m(p_W)=m(p_V)+m(p_minus),                              (5)

with every original, neutral and absolute factor retained.
There is no deletion or division by rank.
Since p_V(1)=-1 and p_V is monic of even degree, it has a real root greater than1, so each such complete original polynomial has positive measure.
This observation does not identify its irreducible factors or optimize them.

For a coarse but fully charged upper bound, on the unit circle each off-diagonal entry of tV+V^T has modulus at most3 and each diagonal entry at most2.
Expanding its determinant over the6! permutations gives |p_V|<=6!*3^6=524880, and the same is true of p_minus.
The usual scalar logarithmic-integral formula therefore gives

    0<m(p_V)<=log524880,
    0<=m(p_minus)<=log524880,
    m(p_W)<=2log524880.                                   (6)

Circle zeros cause no difficulty because a nonzero polynomial's logarithm is integrable.
These are deliberately coarse upper bounds, not exact Mahler values, and energy69 is not substituted for measure.
The exact determinant formula(5), rather than the bound, owns every factor.
The program independently expands three sample complete rank12 covers solely to check implementation and conventions; it does not claim cost optimization over the finite class.

The unchanged cheaper achieved comparison remains [L191](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family): actual rank6, height1, energy5, full polynomial Phi2^2 P4, identical absolute companion, and rank12 height1 energy10 cover Phi2^4 P4^2 with measure2log beta4.
L246's different unpadded sextic remains another actual control, with rank6 height2 energy24 and companion/original>5, cover/original>6 at its retained complete proof scope.
Neither control is improved by this round.
The rank, padding and original-measure comparisons do not imply an optimized absolute cost or the unrestricted Lehmer gap.

### Complete fixed-domain certificate and its limits

The full original J55 group was read: search.py, orders.py, smaller_control.py, verify.py, review_independent.py, readme and all five complete native JSON objects.
The original fixed-domain checker uses no author imports.
It reconstructs all729 cube vectors and114 roots, every194940 actual full basis Bareiss determinants, and checks their equality with the signed replacement minor, every per-position counter and the entire signed-Pfaffian histogram.
Its Pfaffian is the alternating6! permutation definition collected into15 perfect matchings of signed coefficient48, separately from the author's recursive implementation.
The admitted genuine bases and all720 labelled orders are reconstructed independently; every dihedral orbit has12 elements and there are60 representatives.

For e=p(1),u=p(2),w=p(3), reciprocity gives

    u=49+18a+4b+8e,
    w=676+192a+36b+27e,
    a=(w-9u-235+45e)/30,
    b=(u-49-8e-18a)/4, c0=e-2-2a-2b.

Exact scalar Bareiss evaluations and checked integer divisions therefore determine the WHOLE polynomial, not only the target coefficient.
The checker recovers all11248 fixed-order target-Pfaffian polynomials and all150962 changed-order target-Pfaffian polynomials(79867+71095), verifies their complete alternating endpoint and compares all coefficient-frequency, root, position and energy histograms with the native author records.
Both complete target counts are zero; every finite bin, height3 and energy range17--69 matches.
The implementation distinction does not establish agent-context independence: the original R117 is SELF because shared target counts and limits preceded its finding.

The additional deterministic sample uses the first12, last12 and middle unordered-basis key, exactly25 bases and all720 labelled orders, checking36000 original/absolute full polynomials and each again at t=4.
It checks the author verifier's entire three-basis payload, all4320 degree-six/order polynomials, labels, norms, determinant signs, Grams, energies and complete degree-twelve coefficient lists.
The three literal-cover identities also pass39 scalar Bareiss evaluations at-6 through6;13 distinct values plus degree at most12 prove each whole identity.
These samples corroborate the general written symmetry and cover proofs; they do not replace those proofs or enlarge the finite nonexistence class.

For the present whole check, only review_independent.py was replayed on its original fixed domain, with its sole final review_result.json write intercepted in memory and unexpected writes refused.
Its entire returned native object matched the retained review_result.json; its within-run checks matched every original author mathematical payload.
No author producer, larger root box, new basis/order, source/PDF passage, floating-root decision or persisted native output was used or changed.
The original author verifier remains SAME-author checking, and both the original R117 and this maintaining-agent whole finding remain SELF.

## Current assessment
[Selected decision](#decision-integral-gram-proof-home-maintenance)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:25 |
| status | open |
| reason | Retain the complete original two-column/order theorem, full exact genuine finite class for both targets, unresolved unrestricted-second-root system, locally proved secondary scalar and every original/absolute/cover factor and cost, with actual elementary interfaces explicit for whole checking. No new research/source proof, expanded computation or Task/E execution is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | Every integer two-column minor/norm pair, all signs and general fixed-basis cyclic/reversal symmetries, complete genuine cube/order class, exact unrestricted-second-root interface and all scalar/cost/negative limits. |
| argument | [Entire proof](#argument) | Full explicit seed/reflection/sign/endpoint/cover interfaces, original Sections1--5/equations1--6, every integrality/dependent case, secondary trace-field proof and complete fixed-domain certificate/costs. |
| dependency | [Adequate seed/reflection/endpoint interface](Yin_C_G0415_v2.md#argument) | Only the explicit G0/Q0, exact reflection product and full reciprocal endpoint conventions, reproduced here; no arbitrary-order one-column exclusion is imported. |
| dependency | [Adequate full signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Literal equal/opposite sheet decomposition with complete original/absolute factors, ordinary unnormalized measure and energy doubling. |
| support | [Original J55 group](../computations/programs/Yin_J_G0055/readme.md) | Complete original exact194940-pair/7446-base/446760-order class, both targets/histograms and original three-cover/symmetry controls; no unbounded inference. |
| support | [Achieved quartic control](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Fixed rank6/height1/energy5 Phi2^2 P4, identical companion and rank12/height1/energy10 Phi2^4 P4^2 comparison only. |
| support | [Different sextic control](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Existing rank6/height2/energy24 unpadded sextic and full companion/original>5, cover/original>6 at the original completed scope; no new realization. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:27 |
| status | proved |
| reason | Adopt after the actual whole C429/R630 self-check of every integer minor/norm/endpoint, both full sign/order companion symmetries, exact genuine finite class for both targets, all unresolved second-root linear/quadratic cases, secondary trace-field/root proof and complete original/absolute/cover costs. Only the original J55 fixed reviewer was replayed, reproducing all native mathematics without a write or expanded domain. Original R117 is whole SELF from known prior target counts/limits; neither algorithm distinction nor upstream roles are misused as isolation. All discarded-control, unbounded, source and near-one negatives remain, with no Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | Every integer two-column minor/norm pair, all signs and general fixed-basis cyclic/reversal symmetries, complete genuine cube/order class, exact unrestricted-second-root interface and all scalar/cost/negative limits. |
| argument | [Entire proof](#argument) | Full explicit seed/reflection/sign/endpoint/cover interfaces, original Sections1--5/equations1--6, every integrality/dependent case, secondary trace-field proof and complete fixed-domain certificate/costs. |
| dependency | [Adequate seed/reflection/endpoint interface](Yin_C_G0415_v2.md#argument) | Only the explicit G0/Q0, exact reflection product and full reciprocal endpoint conventions, reproduced here; no arbitrary-order one-column exclusion is imported. |
| dependency | [Adequate full signed cover](Yin_C_G0002_v1.md#signed-cover-identity) | Literal equal/opposite sheet decomposition with complete original/absolute factors, ordinary unnormalized measure and energy doubling. |
| support | [Original J55 group](../computations/programs/Yin_J_G0055/readme.md) | Complete original exact194940-pair/7446-base/446760-order class, both targets/histograms and original three-cover/symmetry controls; no unbounded inference. |
| support | [Achieved quartic control](../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Fixed rank6/height1/energy5 Phi2^2 P4, identical companion and rank12/height1/energy10 Phi2^4 P4^2 comparison only. |
| support | [Different sextic control](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Existing rank6/height2/energy24 unpadded sextic and full companion/original>5, cover/original>6 at the original completed scope; no new realization. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0630_v1.md#two-column-ordering-whole-self-finding) | Complete exact statement/argument/dependencies/supports, all parameters/signs/order/finite native scope, local secondary scalar and full cost/negative boundaries; not a fresh isolated finding. |


### Decision integral-gram-proof-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:23 |
| status | proved |
| reason | Maintain only the responsible home of the already consumed k4 integral-Gram comparison after reading its complete actual mechanism in C458v2: rank6/height1/energy5 Phi2^2 P4, identical absolute companion and entire rank12/height1/energy10 Phi2^4 P4^2 cover of measure2log beta4. This is the same exact fixed L191 capability, now fully retained at its complete proof home. Statement, Argument, all other inputs, mathematical status and review scopes remain unchanged. The prior whole finding keeps its actual original L191 reading/binding; it is not represented as having read the new Claim. No new theorem, independent review, native run or Task execution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Every integer two-column minor/norm pair, all signs and general fixed-basis cyclic/reversal symmetries, complete genuine cube/order class, exact unrestricted-second-root interface and all scalar/cost/negative limits. |
| argument | [Exact retained argument](#argument) | Full explicit seed/reflection/sign/endpoint/cover interfaces, original Sections1--5/equations1--6, every integrality/dependent case, secondary trace-field proof and complete fixed-domain certificate/costs. |
| dependency | [Exact retained dependency](Yin_C_G0415_v2.md#argument) | Only the explicit G0/Q0, exact reflection product and full reciprocal endpoint conventions, reproduced here; no arbitrary-order one-column exclusion is imported. |
| dependency | [Exact retained dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Literal equal/opposite sheet decomposition with complete original/absolute factors, ordinary unnormalized measure and energy doubling. |
| support | [Exact retained support](../computations/programs/Yin_J_G0055/readme.md) | Complete original exact194940-pair/7446-base/446760-order class, both targets/histograms and original three-cover/symmetry controls; no unbounded inference. |
| support | [Exact retained support](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Fixed rank6/height1/energy5 Phi2^2 P4, identical companion and rank12/height1/energy10 Phi2^4 P4^2 comparison only. |
| support | [Exact retained support](Yin_C_G0573_v1.md#root-basis-neutral-padding-fixed-scope) | Existing rank6/height2/energy24 unpadded sextic and full companion/original>5, cover/original>6 at the original completed scope; no new realization. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0630_v1.md#two-column-ordering-whole-self-finding) | Complete exact statement/argument/dependencies/supports, all parameters/signs/order/finite native scope, local secondary scalar and full cost/negative boundaries; not a fresh isolated finding. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0055](../computations/programs/Yin_J_G0055/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
