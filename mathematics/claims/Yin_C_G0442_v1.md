---
author: Yin
---
# Complete unbounded second-root congruence obstruction and all companion costs

The entire original L258 mathematical argument and its finite certificate are retained here.
L258 preserves the meaningful exploratory declarations, incomplete modulus4 outcome, original failed symbolic check, authorship/freeze and fixed original review inputs.
No Task/E execution resumes.

## Statement

Use the explicit six-dimensional integer Gram H and actual norm-two root c=(-1,0,1,1,0,1) displayed in the complete argument.
For EACH ordered pair of distinct positions i,j in {0,1,2,3,4,5}, put c at position i, ANY integer d at position j and the unchanged coordinate columns at the other four positions in their displayed order.
Require BOTH d^T H d=2 and the exact coordinate minor c_i d_j-c_j d_i=+1 or-1.
Let V be the upper-unitriangular integer matrix reconstructed from this true norm-two Gram.
Its WHOLE reciprocal determinant polynomial is

    p_V=t^6+a t^5+b t^4+(-3-2a-2b)t^3+b t^2+a t+1.

Whenever a is even, a+b=1 modulo4.
Thus neither F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1 nor S6=t^6-t^4-t^3-t^2+1 is obtained, for ANY size of d and in all30 ordered placements.
The two positions(1,4),(4,1) have identically zero minor and admit no basis; no rank or integrality case is dropped.

The exclusion of those two WHOLE polynomials also holds for EVERY actual integer norm-two first root c' congruent to+/-c modulo8, the same arbitrary integer second root and the same four unchanged columns/order, under the same exact basis conditions.
It includes the distinct unbounded actual roots c_t=c+8t(c+e0), t in Z; every c_t occurs in an actual integral norm-two basis with positions(0,1),d=e1.
Independent column signs and cyclic/reversal images preserve BOTH complete original and absolute-companion polynomials.
Other first-root residue classes, arbitrary reorderings, three changing columns, other lattices and an unrestricted realization obstruction are outside the theorem.

The full certificate is the120 exact integer polynomial models, all30*4^6=122880 residues with1664 F and1920 S6 survivors, all229376 original target-labelled modulus8 lifts with none surviving, and all3584 compressed-invariant classes with their complete ordered-position histogram.
The preliminary modulus4 result is incomplete and is not represented as an exclusion.
For odd minor, D=(Pf^2-ell^2)/8 is an integer whose parity depends only on d modulo4; the exact identity A+2D=2 modulo4 under N=1 modulo4 and even A implies the stated all-integer relation.
The complete one-position elimination for(0,2) retains every integer parameter/divisibility condition and all eight target/sign residual quadratics; no parameter search or coverage of the other29 by that example is asserted.

Every achieved matrix has rank6, full monic determinant p_V(1)=-1 and positive original measure.
Its literal rank12 integer cover has ENTIRE polynomial p_V p_(V^-), full additive measure, unchanged height and doubled energy, with every neutral/repeated/absolute factor retained.
For fixed c, M=max(1,||d||_infinity) gives h<=9M,E<=1215M^2.
For general c', U=max(1,||c'||_infinity) gives h<=54UM,E<=15(54UM)^2.
With B=9M or54UM the full bounds are m(p_V)<=log720+6log B, m(p_(V^-))<=log720+6log B and m(p_W)<=2log720+12log B.
Both old actual controls retain all three complete polynomials and energies24/48 and34/68 at height2; the cheaper Phi2^2 P4 control retains rank6/height1/energy5, identical absolute companion and rank12 full cover Phi2^4 P4^2 of measure2log beta4.
No failed target is assigned an actual favorable companion, and no optimized cost, near-one coverage or unrestricted G0001 gap is proved.

<a id="argument"></a>
## Complete argument

### Adequate actual seed, endpoint, ordering and cover interfaces

The complete original Sections1--5/equations1--8 follow, including the exact failed preliminary congruence outcome and all cost/negative boundaries.
Their pre-run and Task-active language is2026-10-10 chronology retained at its original scope; it authorizes no new exploration or execution.
The complete actual seed/path-coordinate mechanism, two-column determinant/norm interface, endpoint equivalence, sign/cyclic/reversal proof for BOTH determinant polynomials and local secondary-scalar comparison are already adequately proved in [C429](Yin_C_G0429_v1.md#argument).
That proof explicitly fixes det H=-1 and constructs V from a true norm-two integral Gram; it does not infer unbounded exclusion from its finite cube/order test.
For such a V, det V=1 and transposition give a monic reciprocal sextic; p_V(1)=det(V+V^T)=-1 fixes its central coefficient, and p_V(-1)=Pf(V-V^T)^2=5+4b fixes b.
The t^5 coefficient is tr(V^-1 V^T), so the pair(a,Pf)=(-2,+/-3) fixes the ENTIRE F, and(0,+/-1) fixes the ENTIRE S6.
This reproduces the exact consumed endpoint reasoning, including its indispensable true norm/basis hypotheses.
The sign/cyclic/reversal operations use C429's full reflection-product and reciprocity argument for original and absolute matrices, rather than an assumed arbitrary-congruence invariance.

Only the exact literal two-sheet construction in [C2](Yin_C_G0002_v1.md#signed-cover-identity) is consumed for the cover factorization and full additive measure.
Its diagonal blocks I2, nonpositive entry blocks a I2 and positive-entry blocks -a times the swap diagonalize into V and V^- on the symmetric/antisymmetric sheets.
Each original upper entry creates exactly two entries of its absolute size, proving rank12, equal height and doubled energy with no deleted factor.
The original [L246 control](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) and [L191 cheaper control](../ledger/Yin_L_G0191_v1.md) remain fixed inputs at precisely their achieved matrices, complete factors, exact scalar inequalities and costs.
No later home or new source proof is substituted into an old reading account.

<a id="unrestricted-second-root-setup"></a>
### 1. Reuse screen and exact first-root family

The current Task, execution handoff, S3/S6 and knowledge-reuse rules were read.
The entire [L254 two-column and ordering result](../ledger/Yin_L_G0254_v1.md#simultaneous-root-basis-fixed-scope), including its complete separately organized review, supplies an exact unbounded second-root interface; its finite coefficient residues do not supply an unbounded theorem.
The [L250 single-column result](../ledger/Yin_L_G0250_v1.md#unbounded-path-column-fixed-scope) and [L246 actual changed root](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) distinguish the already excluded constructions from the one below.
The earlier conference-source attribution remains at its retained scope.
All new steps proposed here are direct integer substitution and finite congruence certification, so no fresh classification or source theorem is imported.

Use the actual path-coordinate Gram

    H=[[2,-1,0,0,0,0],
       [-1,2,-1,-2,0,2],
       [0,-1,2,1,-2,-2],
       [0,-2,1,2,1,-2],
       [0,0,-2,1,2,1],
       [0,2,-2,-2,1,2]],

and fix the actual root c=(-1,0,1,1,0,1).
Its original standard coordinates are Q0 c=(-1,-1,0,1,-1,1), and c^T H c=2.
This root already escaped the reflection/sign/order class in L246; its use here is reuse, not a newly discovered root.
Put c at position i, an unrestricted integer vector d at position j, and leave the other four columns of the coordinate identity unchanged, where i and j are distinct.
Both orders of these two roles are included.
Reconstruct the integral upper-unitriangular V from the resulting Gram, with diagonal one.

Expanding the coordinate basis determinant gives

    ell_(i,j)(d)=c_i d_j-c_j d_i,

with the same formula for either ordering of the distinct labels.
The integral columns form an actual basis exactly when ell=+1 or -1.
Their norm-two condition is N(d)=d^T H d/2=1; the displayed H is even, so N is an integral quadratic polynomial.
The varying signed Pfaffian P_(i,j)(d)=Pf(V-V^T) is an integral linear polynomial.
With the diagonal of V fixed at one, A_(i,j)(d)=tr(V^(-1)V^T) is an integral polynomial of degree at most two.
At admissible norm and determinant the symmetric endpoint is -1, hence the entire prescribed polynomial

    F=Phi6 P4=t^6-2t^5+t^4-t^3+t^2-2t+1

is equivalent to

    ell=epsilon, P=delta, N=1, A=-2,
    epsilon in {1,-1}, delta in {3,-3}.                  (1)

The same endpoint argument from L254 makes S6=t^6-t^4-t^3-t^2+1 equivalent to delta in {1,-1}, A=0 instead.
Neither equivalence removes the norm or integral-basis equation.

<a id="unrestricted-second-root-declared-scope"></a>
### 2. Declared calculation before execution

The first finite certification target consists of the30 ordered pairs (i,j), not a new cube of candidate roots.
For each pair the author will retain the complete exact polynomials ell,P,N,A in the six coordinates of d.
These identities, once proved, apply to arbitrary integer d.
A first congruence calculation may check all4^6=4096 residue vectors at modulus4 for each position pair, recording every surviving class.
An empty set would exclude that family over all integers; a nonempty set does not prove realizability.
Exact elimination of the two linear equations is preferred when it reduces the dimension and keeps every divisibility condition.
Any extension to a larger modulus or a changed algebraic family will be declared before it is run.
This experiment does not cover other first roots, arbitrary reorderings beyond the specified placement, simultaneous changes of three columns or other lattices.

No execution outcome is yet claimed.
Full original, absolute-companion and literal-cover costs will be retained for every achieved control; a congruence failure alone assigns no unknown target companion a small measure.

The declared modulus4 run has now completed: all30*4096 classes were checked, with1664 surviving F classes and1920 surviving S6 classes in total.
Positions(1,4) and(4,1) have ell identically zero and rank-one linear systems, so cannot be integral bases.
Every other two-row linear system has rank two.
These surviving residues are not integer solutions.

Before a changed-modulus calculation, the mathematical reason is explicit: modulo4, BOTH target sets {+/-3} and {+/-1} reduce to the same odd residues.
Thus that first check cannot distinguish the two exact Pfaffian targets.
Modulo8 does distinguish them, and also distinguishes an exact unit minor +/-1 from arbitrary odd minors.
Lift every retained modulo4 class by adding4 times each vector in {0,1}^6 and check all four equations modulo8.
This is at most(1664+1920)*64=229376 target-labelled lift tests.
The cap is120 seconds and complete survivors will be retained.
No root-size restriction is imposed by this congruence calculation, and no extension beyond modulus8 is currently declared.

<a id="second-root-congruence-theorem"></a>
### 3. Complete congruence certificate and an unbounded theorem

**Theorem.**
In the construction of Section1, for every ordered pair i!=j and EVERY integer second root d that makes the columns a norm-two integral basis, write the complete polynomial as

    p_V=t^6+a t^5+b t^4+(-3-2a-2b)t^3+b t^2+a t+1.

If a is even, then

    a+b = 1 modulo4.                                    (2)

In particular neither F=Phi6 P4 nor S6 is obtained.
This is an all-integer exclusion for the specified first root and placements, not an all-basis or all-unitriangular exclusion.

Here is a fully reproducible finite proof of the only residue identity required.
For each position, form the six coordinate columns q_k, set g_kl=q_k^T H q_l, and let v_kk=1,v_kl=g_kl for k<l, zero otherwise.
The inverse entries used to calculate A obey the finite integer recurrence

    z_kk=1,
    z_kl=-sum_(h=k+1)^l v_kh z_hl,
    A=6+sum_(k<l) z_kl v_kl.                             (3)

The Pfaffian uses its15 signed perfect matchings, or equivalently expansion in the first remaining row.
These formulas, the displayed H and c, and all30 choices i!=j define the certificate without any floating parameters.
J58/exact.py retains all120 resulting integer polynomials as both readable formulas and coefficient/exponent lists.
Each A is quadratic, each ell and P linear, and N is the same quadratic.
The degree bound follows separately from the determinant: the variable root enters only one off-diagonal row and column of tV+V^T, so each determinant term uses it at most twice.
The diagonal has already been fixed to t+1.
This also shows that the polynomial interpolation check below verifies full identities, not selected numerical values.

In every position P-ell has even coefficients.
If ell is odd, so is P, and

    D(d)=(P(d)^2-ell(d)^2)/8

is an integer.
Its parity depends only on d modulo4.
Indeed for d'=d+4h, write P(d')=P(d)+4P(h) and ell(d')=ell(d)+4ell(h).
Then

    D(d')-D(d)=P(d)P(h)-ell(d)ell(h)
                  +2(P(h)^2-ell(h)^2),

which is even since P and ell are congruent modulo2 as linear forms.
This argument does not assume ell equals one before taking residues.

Enumerate r in {0,1,2,3}^6 and retain precisely ell(r) odd, N(r)=1 modulo4 and A(r) even.
There are3584 such position-labelled classes.
Direct substitution in the defined polynomials gives, for EVERY retained class,

    A(r)+2D(r)=2 modulo4.                                (4)

The complete table below reports the two possible pairs (A mod4,D mod2).
The counts happen to be identical for (i,j) and (j,i); both ordered cases were separately computed, and this equality is not used as an unproved symmetry shortcut.
Each row is therefore the count for EACH of the two orders.

| Unordered positions | (A,D)=(2,0) | (A,D)=(0,1) |
| --- | ---: | ---: |
| 0,1 | 0 | 0 |
| 0,2 | 64 | 0 |
| 0,3 | 64 | 64 |
| 0,4 | 0 | 64 |
| 0,5 | 0 | 0 |
| 1,2 | 64 | 0 |
| 1,3 | 192 | 192 |
| 1,4 | 0 | 0 |
| 1,5 | 0 | 64 |
| 2,3 | 192 | 192 |
| 2,4 | 192 | 192 |
| 2,5 | 64 | 64 |
| 3,4 | 0 | 64 |
| 3,5 | 0 | 64 |
| 4,5 | 0 | 0 |

The sum of the second column, doubled, is1664; that of the third, doubled, is1920.
No other pair occurs.
J58/congruence.py verifies this identity on the already retained complete classes; it does not enlarge their range.
For an actual basis ell^2=1 and P^2=5+4b, hence D=(b+1)/2.
Substituting this in(4) proves(2).
For F, a+b=-1=3 modulo4; for S6, a+b=-1 as well.
Both violate(2).

The separately executed modulus8 lifting gives the same exclusion directly: all229376 lifts failed, and in fact none survived the simultaneous unit-minor and target-Pfaffian tests once its modulo4 norm and coefficient constraints were imposed.
This is recorded in full rather than replacing the first incomplete modulus4 result.
It explains why treating +/-3 and +/-1 as merely odd modulo4 would have missed the proof.
No claim that a general even coefficient obeys(2) outside this first-root construction is made.

Two of the linear systems, (i,j)=(1,4),(4,1), are degenerate: c_i=c_j=0 and ell is identically zero.
They admit no basis for the simpler determinant reason.
The other28 have rational rank two.
No rank hypothesis, denominator cancellation or rational solution is needed in the modular proof.
It therefore retains every singular case automatically.

<a id="first-root-congruence-extension"></a>
### 4. A whole first-root congruence class, with actual unbounded roots

The exclusion extends analytically beyond the one fixed root.
Let c' be ANY actual integer root with c'^T H c'=2 and c'=c modulo8.
Put c' at any position i, arbitrary integer d at j, keep the other four path columns and their displayed order, and require an actual norm-two integral basis.
Reducing the entire reconstructed V modulo8 gives the same matrix as using c, because all its entries are integer bilinear products.
The determinant minor, Pfaffian, and first coefficient are integer polynomials in those entries.
Thus any F or S6 realization with c' would give a solution of exactly the excluded modulus8 system for c.
This proves no such realization exists.
The same holds for c'=-c modulo8 by changing the sign of its column: V becomes D V D for a diagonal sign matrix D, which preserves the whole original polynomial and leaves its absolute companion unchanged.

This class contains actual roots of unbounded size, not merely formal residue vectors.
Set

    w=c+e0=(0,0,1,1,0,1).

Directly Hc=(-2,0,1,1,0,-2), c^T H c=2 and e0^T H c=-2.
Consequently w^T H w=0 and c^T H w=0.
For EVERY t in Z,

    c_t=c+8t w,  c_t^T H c_t=2,  c_t=c modulo8.          (5)

These roots are distinct and unbounded.
At i=0,j=1,d=e1, the determinant minor is c_t,0=-1 and d has norm two, so each c_t participates in an actual integral norm-two basis in the proved class.
This does not give either target; it demonstrates the theorem's nonvacuous unbounded domain.
All untouched columns still have norm two.

The entire exclusion also survives independent column signs and the cyclic rotations/reversals of each resulting ordered basis: L254 proves that these operations preserve BOTH the complete original and absolute-companion polynomials.
This statement covers these images of the stated construction.
It does not cover arbitrary reordering, other first-root residue classes, three genuinely variable columns or another lattice.
In particular it does not extrapolate the old finite coefficient pattern to all integral bases.

For a small illustration of the unrestricted equation interface, the (i,j)=(0,2) case has

    ell=-d0-d2,
    P=d0-2d1+5d2-4d4-4d5.

For ell=epsilon, P=delta, put k=(delta+epsilon)/2.
Every integer solution of these two linear equations, with no lost divisibility condition, has

    d=(-x-epsilon, 2x-2z-2w-k, x, y, z, w),
    x,y,z,w in Z.                                       (6)

Here delta and epsilon are odd, so k is always integral; solving the first equation and then the second proves necessity and sufficiency.
J58/eliminate.py retains the exact remaining quadratic norm and coefficient equations for all eight target/sign cases.
This is an illustrative elimination of one position, not the completeness proof for the other29; the uniform modular argument already covers all of them.
No search over the four unrestricted parameters was run.

<a id="unbounded-second-root-full-costs"></a>
### 5. Full polynomial, neutral and companion costs

No new F or S6 realization is achieved.
Their intended original data remain F=Phi6 P4 of degree6 with neutral degree2 and measure log beta4, and S6 of degree6 with no neutral factor and the smaller positive measure proved locally in L254.
A failed realization assigns no actual companion to either target and supplies no optimality theorem.

For any actual basis in Sections1 or4, the constructed V has rank6, integral entries and every diagonal entry one.
Set V^-_ij=-|V_ij| for i<j, V^-_ii=1.
The actual integer literal cover W has rank12 and diagonal blocks I2; its upper block for a=V_ij is a I2 if a<=0 and -a times the two-sheet swap if a>0.
The reused D9 identity gives the ENTIRE polynomials and costs

    p_W=p_V p_(V^-),
    m(p_W)=m(p_V)+m(p_(V^-)).                             (7)

No neutral, repeated, signed or absolute factor is divided out.
If h=max(1,max_(i<j)|V_ij|) and E=sum_(i<j)V_ij^2, then W has height h and energy2E.
These entry costs are not Mahler measures.
Since p_V(1)=-1 and p_V is monic of degree6, it has a real root greater than1 and m(p_V)>0.

Uniform elementary bounds keep the unbounded coordinates visible.
For the fixed c, put M=max(1,||d||_infinity).
The largest row sum of |H| is9 and ||Hc||_1=6, so h<=9M and E<=1215M^2.
For a general actual c' in Section4, put U=max(1,||c'||_infinity).
The bound |c'^T H d|<=54UM and the same row sums give h<=54UM and E<=15(54UM)^2.
With B respectively9M or54UM, B>=2, every circle entry of either determinant matrix has modulus at most B; its6! terms give

    0<m(p_V)<=log720+6log B,
    0<=m(p_(V^-))<=log720+6log B,
    m(p_W)<=2log720+12log B.                             (8)

The logarithmic integral is legitimate at circle zeros since these nonzero monic polynomials have integrable logarithms.
These coarse bounds are complete, unnormalized costs, not useful near-one or optimized ratios.

Two already achieved controls are recomputed only to verify signs, full polynomials and cover conventions.
At i=2,j=0,d=e0 one obtains the L246 matrix, with

    p_V=t^6-2t^5-t^4+3t^3-t^2-2t+1,
    p_(V^-)=t^6-38t^5-61t^4-69t^3-61t^2-38t+1,

height2, energy24, and cover height2, energy48.
The full cover is their degree12 product.
Its original expanding root lambda exceeds beta4 and its absolute expanding root lies in(38,40), at the retained L246 proof scope; companion/original>5 and cover/original>6, with no quartic improvement.
At i=0,j=1,d=(0,1,2,1,0,1) the previously retained J55 sample has

    p_V=t^6-5t^5+t^4+5t^3+t^2-5t+1,
    p_(V^-)=t^6-147t^5-261t^4-347t^3-261t^2-147t+1,

height2, energy34, cover height2, energy68, and again the entire degree12 product.
These exact factors are retained in J58/verification.json; no new small-measure claim or irreducibility claim about the latter pair is made.
The unchanged cheaper L191 control remains rank6/height1/energy5, Phi2^2 P4, identical absolute companion and rank12 cover Phi2^4 P4^2 with measure2log beta4.
The new exclusion does not improve that cost or settle whether the desired alternative padding is achievable elsewhere.


### Complete original-domain certificate and checking limits

All six complete J58 programs, its readme and every complete native JSON object were read or decoded at their actual scopes.
Every model's readable formula and coefficient/exponent data, all stage/rank/count/histogram/elimination/control payloads and the complete survivor-list structures were inspected.
The full survivor tuple lists were compared exhaustively by the original fixed checker; they are not claimed to have been manually read tuple by tuple.
The author SymPy producers and its separate840-node/5040-scalar-determinant verifier were not rerun.
Their original120-second caps, sole corrected symbolic-interface failure and distinct same-author verification remain in L258/J58.

The original standard-library reviewer derives all120 model dictionaries directly from720 Leibniz terms, signed matching Pfaffians, determinant minors and half-norm arithmetic, without author-code imports.
It re-evaluates all122880 residues, compares EVERY complete survivor tuple list/stage count, checks each of the3584 histogram entries' classes and both ordered position roles, and evaluates all229376 lifts by the exact degree-two Taylor formula modulo8.
All56 elimination polynomial checks and both full original/absolute/rank12 control polynomials use its distinct sparse substitution and Newton-trace methods.
Its exact unbounded-family coefficient identities and full cost-row bounds are also checked.

For the present SELF check only that original fixed reviewer run() was called under a non-main module name.
Its final output-writing entry point was not invoked, both Path text/byte write methods were guarded against unexpected writes, and its WHOLE returned object matched the original review_result.json.
All program/readme/native bytes were unchanged; no producer, new input/domain, random/floating decision, source proof or PDF acquisition was used.
The all-integer/congruence-class conclusions rest on the complete written reduction and exact coefficient identities above, not an extrapolation of finite coordinates.
Original R157 is known SELF because its assignment disclosed counts and the proposed target extension before checking; its independent implementation and original no-author-repair outcome remain true at that relationship.

## Current assessment
[Selected decision](#decision-integral-gram-proof-home-maintenance)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:11 |
| status | open |
| reason | Retain the complete original unbounded second-root proof, exact congruence-class extension, every singular/integer/order case, failed preliminary outcome and all original/absolute/cover costs with adequate actual seed/endpoint/order/cover inputs. Only the old fixed reviewer was replayed stdout-only; no producer/domain/source/Task expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact theorem](#statement) | All30 placements and every integer second root, actual first roots in+/-c mod8, unbounded actual family, all singular/sign/order/elimination cases, complete targets and every finite/full-cost/negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--5/equations1--8 and exact finite certificate, adequate endpoint/ordering/cover interfaces, all residue/integrality/unbounded-root/cost mechanisms. |
| dependency | [Actual seed/endpoint/order theorem](Yin_C_G0429_v1.md#argument) | Concrete Gram/path/basis determinant and norm, whole reciprocal target equivalence, both-polynomial sign/cyclic/reversal invariances and local complete S6 scalar/cost only; no unbounded inference from its finite cube. |
| dependency | [Literal full-cover identity](Yin_C_G0002_v1.md#signed-cover-identity) | Exact two-sheet integer block construction, full original/absolute product, additive unnormalized measure and rank/height/doubled-energy consequences only. |
| dependency | [Original actual L246 control](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Same concrete changed-root matrix, full original/absolute factors,38<rho<40,beta4<lambda<2 and full ratios>5/>6; no new root/measure evaluation. |
| dependency | [Original cheaper L191 control](../ledger/Yin_L_G0191_v1.md) | Actual k4 Phi2^2 P4 matrix, rank6/height1/energy5 and whole rank12 Phi2^4 P4^2 cover measure2log beta4 only. |
| support | [Original complete J58 group](../computations/programs/Yin_J_G0058/readme.md) | All original120 polynomial models,122880 residues,229376 target-labelled lifts,3584 invariant classes, eight illustrative sign cases and two full control polynomials; original failure/cap/check distinctions retained. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0058/readme.md#recorded-runs) | Complete readable and coefficient/exponent models, every count/rank and full target-labelled tuple list, not a sufficient standalone exclusion. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0058/mod4_result.json`; this target locates its run account. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:14 |
| status | proved |
| reason | Adopt after the actual whole C442/R645 SELF check of every ordered position and arbitrary integer second root, true norm/unit-minor/endpoint identities, complete parity certificate and all actual first roots in+/-c mod8 with the nonvacuous unbounded family, singular/elimination/order scope and every full original/absolute/cover cost. The original fixed J58 checker matched all120 models, every complete survivor list and122880 residues,229376 lifts,3584 invariant classes,56 elimination checks and both complete controls without writing or expanding the domain. Original R157 is known SELF from shared target counts/proposed extension; no new isolation, author producer/source proof or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact theorem](#statement) | All30 placements and every integer second root, actual first roots in+/-c mod8, unbounded actual family, all singular/sign/order/elimination cases, complete targets and every finite/full-cost/negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--5/equations1--8 and exact finite certificate, adequate endpoint/ordering/cover interfaces, all residue/integrality/unbounded-root/cost mechanisms. |
| dependency | [Actual seed/endpoint/order theorem](Yin_C_G0429_v1.md#argument) | Concrete Gram/path/basis determinant and norm, whole reciprocal target equivalence, both-polynomial sign/cyclic/reversal invariances and local complete S6 scalar/cost only; no unbounded inference from its finite cube. |
| dependency | [Literal full-cover identity](Yin_C_G0002_v1.md#signed-cover-identity) | Exact two-sheet integer block construction, full original/absolute product, additive unnormalized measure and rank/height/doubled-energy consequences only. |
| dependency | [Original actual L246 control](../ledger/Yin_L_G0246_v1.md#root-basis-neutral-padding-fixed-scope) | Same concrete changed-root matrix, full original/absolute factors,38<rho<40,beta4<lambda<2 and full ratios>5/>6; no new root/measure evaluation. |
| dependency | [Original cheaper L191 control](../ledger/Yin_L_G0191_v1.md) | Actual k4 Phi2^2 P4 matrix, rank6/height1/energy5 and whole rank12 Phi2^4 P4^2 cover measure2log beta4 only. |
| support | [Original complete J58 group](../computations/programs/Yin_J_G0058/readme.md) | All original120 polynomial models,122880 residues,229376 target-labelled lifts,3584 invariant classes, eight illustrative sign cases and two full control polynomials; original failure/cap/check distinctions retained. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0058/readme.md#recorded-runs) | Complete readable and coefficient/exponent models, every count/rank and full target-labelled tuple list, not a sufficient standalone exclusion. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0058/mod4_result.json`; this target locates its run account. |
| review | [Actual entire SELF finding](../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) | Entire statement/argument/direct interfaces, all integer/basis/parity/congruence-class/unbounded/finite/elimination/sign/order/neutral/full-cost/negative scope; original R157 remains known SELF. |


### Decision integral-gram-proof-home-maintenance

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:23 |
| status | proved |
| reason | Maintain only the responsible home of the already consumed k4 integral-Gram comparison after reading its complete actual mechanism in C458v2: rank6/height1/energy5 Phi2^2 P4, identical absolute companion and entire rank12/height1/energy10 Phi2^4 P4^2 cover of measure2log beta4. This is the same exact fixed L191 capability, now fully retained at its complete proof home. Statement, Argument, all other inputs, mathematical status and review scopes remain unchanged. The prior whole finding keeps its actual original L191 reading/binding; it is not represented as having read the new Claim. No new theorem, independent review, native run or Task execution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | All30 placements and every integer second root, actual first roots in+/-c mod8, unbounded actual family, all singular/sign/order/elimination cases, complete targets and every finite/full-cost/negative limit. |
| argument | [Exact retained argument](#argument) | Complete original Sections1--5/equations1--8 and exact finite certificate, adequate endpoint/ordering/cover interfaces, all residue/integrality/unbounded-root/cost mechanisms. |
| dependency | [Exact retained dependency](Yin_C_G0429_v1.md#argument) | Concrete Gram/path/basis determinant and norm, whole reciprocal target equivalence, both-polynomial sign/cyclic/reversal invariances and local complete S6 scalar/cost only; no unbounded inference from its finite cube. |
| dependency | [Exact retained dependency](Yin_C_G0002_v1.md#signed-cover-identity) | Exact two-sheet integer block construction, full original/absolute product, additive unnormalized measure and rank/height/doubled-energy consequences only. |
| dependency | [Exact retained dependency](Yin_C_G0573_v1.md#root-basis-neutral-padding-fixed-scope) | Same concrete changed-root matrix, full original/absolute factors,38<rho<40,beta4<lambda<2 and full ratios>5/>6; no new root/measure evaluation. |
| dependency | [Exact retained dependency](Yin_C_G0458_v2.md#irreducible-quartic-gram-family) | Actual k4 Phi2^2 P4 matrix, rank6/height1/energy5 and whole rank12 Phi2^4 P4^2 cover measure2log beta4 only. |
| support | [Exact retained support](../computations/programs/Yin_J_G0058/readme.md) | All original120 polynomial models,122880 residues,229376 target-labelled lifts,3584 invariant classes, eight illustrative sign cases and two full control polynomials; original failure/cap/check distinctions retained. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0058/readme.md#recorded-runs) | Complete readable and coefficient/exponent models, every count/rank and full target-labelled tuple list, not a sufficient standalone exclusion. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0058/mod4_result.json`; this target locates its run account. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0645_v1.md#second-root-whole-self-finding) | Entire statement/argument/direct interfaces, all integer/basis/parity/congruence-class/unbounded/finite/elimination/sign/order/neutral/full-cost/negative scope; original R157 remains known SELF. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0058](../computations/programs/Yin_J_G0058/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
