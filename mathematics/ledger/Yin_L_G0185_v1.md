---
author: Yin
---

# Positive absolute-cover cost and exact interacting-triangle reductions

The current complete [C440v2 proof](../claims/Yin_C_G0440_v2.md#argument) is adopted with the [later isolated whole finding](../audits/reviews/Yin_R_G0653_v1.md#positive-cover-isolated-whole).
The original adoption and contribution accounts below retain their own dates and inputs.

Date: 2026-10-10.
Fixed retention by the coordinating AI for Yin.
Full arguments, contribution history, computational inspection boundaries and completed separate reviews are preserved below.

<a id="positive-cover-cost-fixed-scope"></a>
## Adopted scope

The complete independently reviewed positive-cost round is adopted, including the closed local interpretation correction.
For integral upper-unitriangular V, positive logarithmic Mahler measure of det(tV+V^T) forces its all-negative absolute presentation to have strictly positive extra cost, at least 2 arcosh(rho(A)/2), with A the symmetric absolute adjacency.
The explicit shared-triangle family admits exact local reductions that decrease the whole extra measure until it equals the original measure.
This supplies a necessary lower cost and a controlled positive-measure family, not the optimized upper-cost or unrestricted small-measure representation needed for a gap transfer.

Historical pending-review wording in the retained arguments records their status when written.
This adoption and the completed findings determine current status.
Only heading depth and relative navigation are relocated.
Necessary author programs and mathematical results remain at J32; no fresh computation or source-proof inspection is claimed by this retention.
Unrestricted G0001 remains active and unresolved.

<a id="retained-positive-cover-proof"></a>
## Positive absolute-cover cost and exact reductions of interacting frustrated triangles

Date: 2026-10-10, Asia/Hong_Kong.

The coordinator supplied the Gram-instability/Perron-root candidate below.
The structural author checks its details, supplies the explicit positive-vector proof and develops the interacting-triangle family.
These contributions are disclosed; neither author checking nor the coordinator's eventual check of its own candidate is independent review of that candidate.

### Reuse, source comparison and scope

Reuse the original unnormalized signed-cover factorization and exact adjacent mutations from [D G0009](../claims/Yin_C_G0002_v1.md#signed-cover-identity), and the isolated-cycle and attachment distinctions from [D G0021](Yin_L_G0184_v1.md#cycle-order-polynomial).
For an integral upper unitriangular V, write p_V(t)=det(tV+V^T), and let V^- have diagonal one and strict upper entries -|V_ij|.
The doubled all-negative cover has p_W=p_V p_(V^-) and extra logarithmic Mahler cost exactly m(p_(V^-)).
The zero-cost rigid-cycle examples have m(p_V)=0; the first question is whether that phenomenon can persist when m(p_V)>0.

The retained [McM02](../literature/pdf/McM02.pdf) was already acquired and registered; no new source artifact is needed.
A targeted primary-source comparison on 2026-10-10 read Theorem1.3/5.1 and the bicolored-eigenvalue definition in [the publisher PDF](https://www.numdam.org/item/PMIHES_2002__95__151_0.pdf), pp.153 and168--171.
The displayed lower bound is the same spectral bound obtained below, and p.171 explicitly notes extension to symmetric nonnegative adjacency matrices.
Thus the nonnegative spectral comparison is established context, not a novelty claim.
The present proof directly treats the needed integral matrix and signed-to-absolute interface.
The full Coxeter gap/classification proof remains uninspected and is not an adopted premise; the existing D9 statement-depth boundary is not silently expanded to that proof.
This search stops at the exact source comparison rather than reopening a broad Coxeter literature search.

The continuing exact controls are in [J G0032](../computations/programs/Yin_J_G0032/readme.md).
The formulas below are proved for their full stated parameters, independently of those finite controls.
No arbitrary reciprocal-polynomial realization, optimized global cost bound or near-one family is assumed.

<a id="positive-absolute-cover-cost"></a>
### 1. Positive measure forces strictly positive extra cover cost

Let G=V+V^T and let A be the symmetric nonnegative matrix with A_ii=0 and A_ij=|V_ij| for i<j.
Set a=rho(A).
If m(p_V)>0, then G is not positive semidefinite, a>2, and p_(V^-) has a positive real root at least

    T(a)=((a+sqrt(a^2-4))/2)^2.

Consequently

    m(p_(V^-)) >= log T(a) = 2 arcosh(a/2) > 0.

All measures are ordinary logarithmic Mahler measures without division by the matrix rank.
Reducible support and arbitrary integral entry magnitudes are allowed.
This gives a necessary positive cost, not a degree-uniform lower bound or a cost upper bound relative to m(p_V).

#### The semidefinite kernel cannot hide off-circle eigenvalues

Put C=-V^(-1)V^T.
Direct multiplication gives

    C^T G C=G,       C-I=-V^(-1)G.

If G is positive semidefinite, C fixes ker G pointwise.
On the quotient by that kernel, G induces a positive definite inner product and the induced C is an isometry.
Its complex eigenvalues have modulus one.
The characteristic polynomial of C is the product of the quotient characteristic polynomial and (t-1)^(dim ker G), even if the full transformation has nontrivial Jordan blocks.
Since p_V=det(tI-C), all its roots have modulus one.
Its leading coefficient is one, so its logarithmic Mahler measure is zero.
This proves the contrapositive without assuming G is nonsingular.

When G is not positive semidefinite, some real v has v^T Gv<0.
Since G has diagonal2 and absolute off-diagonal matrix A,

    2||v||^2 < -sum_(i!=j) G_ij v_i v_j
               <= |v|^T A |v| <= a||v||^2.

Thus a>2.
More quantitatively, if delta=-lambda_min(G)>0, the same Rayleigh comparison gives a>=2+delta and hence the extra-cost lower bound 2 arcosh(1+delta/2).
Delta depends on the presentation; its size is not an invariant of integral congruence.

#### A positive real root from the absolute adjacency

Let B be the strictly upper triangular part of A and M(t)=tB+B^T for t>0.
Then

    p_(V^-)(t)=det((t+1)I-M(t)).

We claim rho(M(t))>=sqrt(t)*a.
Choose a connected support component attaining a; on it M(t) is irreducible unless it is an isolated vertex, which cannot attain a>2.
Let u,v be strictly positive right eigenvectors of M(t),M(t)^T with the same Perron eigenvalue r_t.
Put w_i=sqrt(u_i v_i).
For every i, Cauchy--Schwarz gives

    sum_j sqrt(M_ij M_ji) w_j
       <= sqrt((sum_j M_ij u_j)(sum_j M_ji v_j))
       = r_t w_i.

The matrix on the left is sqrt(t) times the same A component.
A positive subeigenvector bounds its spectral radius above by r_t: after diagonal scaling by w, every row sum is at most r_t.
Hence r_t>=sqrt(t)*a, and the full M(t) has at least that spectral radius.
This proves the needed geometric-mean inequality directly; no equality case or irreducibility of the full support is assumed.

Define h(t)=t+1-rho(M(t)).
It is continuous.
The equation T+1=a sqrt(T) gives h(T)<=0 for T=T(a)>1.
On the other hand,

    rho(M(t))/t = rho(B+B^T/t) -> rho(B)=0

as t tends to infinity, since B is strictly upper triangular.
Thus h(t)>0 eventually.
The intermediate value theorem supplies t_0>=T with rho(M(t_0))=t_0+1, which makes the displayed determinant zero.
This is an actual positive real root of p_(V^-), whose contribution to logarithmic Mahler measure is at least log T.
The argument does not require h to be monotone or assert t_0 is the only root outside the unit circle.

In particular every positive-measure signed presentation has positive extra cover cost.
This resolves the specific zero-cost question left by the isolated neutral cycles.
It does not compare that cost with the original measure strongly enough to transfer a uniform gap, and reducing a chosen energy does not by itself control either quantity.

<a id="interacting-triangle-cost-family"></a>
### 2. An exact positive-measure family with independently removable frustrations

For every integer r>=1, use vertices 0,a_1,b_1,...,a_r,b_r in this order.
Let V_r be upper unitriangular with exactly the three entries

    V_(0,a_j)=V_(0,b_j)=V_(a_j,b_j)=1

for each j.
Its support consists of r triangles sharing the central vertex0, and each triangle is frustrated.
Its energy is E=3r.
Put F(t)=t^2+t+1 and s=t+1.

The full polynomial is

    p_(V_r)(t)=s F(t)^(r-1) [t^2+(1-r)t+1].                 (1)

To prove it, each leaf pair has block D=[[s,t],[1,s]] in tV+V^T, with determinant F.
Its coupling row from the central vertex is (t,t), and the reverse column is (1,1)^T.
The corresponding scalar Schur-complement contribution is t*s/F.
Summing the r disjoint branches gives

    F^r [s-r*t*s/F] = s F^(r-1)(F-r*t).

This rational-function computation proves a polynomial identity, including at the zeros of F, by multiplication of denominators.
It requires no approximate root computation.

For r=1,2,3 the final quadratic in (1) is cyclotomic (with a repeated root at r=3).
For r>=4 it has one root greater than one, its reciprocal, and no further roots.
Therefore

    m(p_(V_r))=arcosh((r-1)/2)>0  for r>=4.                (2)

The signed Gram threshold agrees exactly here.
Each leaf block [[2,1],[1,2]] is positive definite and its central Schur contribution is2/3.
The remaining scalar is2-2r/3.
Thus G is positive definite for r<3, positive semidefinite with one-dimensional kernel for r=3, and has exactly one negative direction for r>3.
This agreement is specific to this family; the general result above proves only the implication from positive measure to indefiniteness.

#### Partial exact mutations and the full cost at every step

Apply the forward adjacent mutation at the consecutive pair (a_j,b_j).
Its two by two basis block is [[0,1],[1,-1]].
The pair entry becomes -1, while the central coupling row (1,1) becomes (1,0).
All other branches are unchanged.
Hence each move replaces one triangle by a two-edge arm, lowers energy by exactly one, and preserves the complete signed polynomial by integral unimodular congruence.
Distinct branch moves commute because their basis blocks are disjoint and their external couplings do not introduce cross-branch edges.

Let V_(r,k) denote the matrix after any k distinct branch moves, 0<=k<=r.
It has energy3r-k and still has polynomial (1).
Its absolute negative presentation satisfies

    p_(V_(r,k)^-)(t)
      =s F(t)^(r-1) [t^2+(1-3r+2k)t+1].                 (3)

Indeed the leaf-pair absolute block is [[s,-t],[-1,s]], still of determinant F.
An unprocessed triangle has central coupling row(-t,-t), column(-1,-1)^T and Schur contribution3*t*s/F.
A processed arm has row(-t,0), column(-1,0)^T and contribution t*s/F.
Thus the total contribution is (3r-2k)*t*s/F, proving (3) for every subset of k branches and every r.

For r>=4 all these quadratics have a unique positive root greater than one.
The exact extra logarithmic cover cost at the k-th stage is

    m(p_(V_(r,k)^-))=arcosh((3r-2k-1)/2).                (4)

It strictly decreases at each step and at k=r equals the original measure in (2).
The final graph is the tree of r two-edge arms, so it is switchable; its signed and absolute polynomials coincide.
The doubled cover at that explicit endpoint has total logarithmic measure2*m(p_(V_r)).
This is an achieved cost ratio, not a proof of minimality among all congruent or stabilized representations.

This family shows a concrete interaction threshold: up to three individually neutral frustrated triangles together remain neutral, while four or more produce positive Mahler measure.
The independent local cancellations then remove every frustration without a temporary energy increase and track the complete extra cost, not merely a dominant eigenvalue or determinant value at one.
Its smallest positive measure is arcosh(3/2), so it is bounded away from zero and supplies no near-one family.

#### Sharpness of the spectral lower bound at the final tree

The adjacency spectral radius of the final r-arm tree is sqrt(r+1).
One positive Perron vector is obtained by assigning central value r, each middle vertex sqrt(r+1), and each outer vertex1: the adjacency equations all have eigenvalue sqrt(r+1).
Connectivity makes it the Perron value.
Therefore

    2 arcosh(sqrt(r+1)/2)=arcosh((r-1)/2),   r>=4.

The general lower bound from Section1 is attained at this endpoint.
The identity follows by cosh(2u)=2cosh(u)^2-1.
It establishes sharpness of that adjacency-dependent bound within positive-measure integral examples; it does not make energy a general measure-cost potential or prove a global optimized bound.

The comparison is strict before all triangles have been removed.
More explicitly, the adjacency characteristic polynomial after k moves is

    det(xI-A_(r,k))
      =(x^2-1)^(r-1) [x^3-(1+2r-k)x-2(r-k)].            (5)

The same leaf-pair Schur complement proves this: an unprocessed triangle contributes2/(x-1) to the central equation and a processed arm contributes x/(x^2-1).
For r>=4 the Perron value is the largest positive root of the cubic.
Put D=3r-2k+1, the number whose square root would make the Section1 lower bound equal the actual cost in (4).
The cubic evaluated at sqrt(D) is

    (r-k)(sqrt(D)-2).

For k<r this is positive since D>=r+1>=5, and the cubic has exactly one positive root by its signs.
Hence rho(A_(r,k))<sqrt(D), so the spectral lower bound is strictly smaller than the actual added measure at every such stage.
For k=r equality holds.
This supplies an explicit strict excess above the symmetric-adjacency bound; it is still an exact family calculation, not an inequality for every presentation.

<a id="positive-cover-round-checks"></a>
### 3. Checks and continuation boundary

The written Gram, Perron and Schur-complement calculations have been author-checked.
On 2026-10-10 the retained J G0032 verifier ran successfully with Python and SymPy.
It checks60 concrete matrices with r=1,...,8: all branch subsets for r<=4 and all prefix subsets for larger r.
A separately coded integer Bareiss determinant is evaluated at n+1 distinct integer values for each of the signed, absolute and adjacency polynomials, so the2148 exact determinant values certify all three complete polynomials for those finite inputs.
The program checks every executed adjacent step's unitriangular endpoint and one-unit energy drop,38 reverse-order controls for multi-branch operations, and the explicit final sign gauge.
Eight exact signed-Gram characteristic-polynomial checks certify the finite inertia and kernel controls, including the semidefinite r=3 case.
Symbolic rank-three matrices with arbitrary three upper entries also check both general C/G identities.
No floating root estimate, broad random scan or old research implementation is used.

The actual program and successful result are [verify.py](../computations/programs/Yin_J_G0032/verify.py) and verification.json (`mathematics/computations/outputs/Yin_J_G0032/verification.json`).
These are finite controls for the all-parameter written proof, not an independent review or a proof by extrapolation.
No initial failed run occurred.
The coordinator originated Section1's candidate proof and is therefore a contributor to that component.
The triangle family and all-r cost identities were developed by the structural author; no independent review of either new component is yet claimed.

The next discriminating structural question is whether comparable cost identities survive when frustrated cycles share an edge or have attachments at their internal vertices, where the independent branch cancellation fails.
Separately, any gap transfer still requires justified representation/neutral-completion coverage and an upper bound for an optimized extra cost in the actual small-measure class.
The present positive-cost necessity, sharp lower-bound examples and explicit positive-measure reductions do not close either obligation.
Existing fixed L169/L170 and the general G0001 status remain unchanged.


<a id="positive-cover-collaborator-review"></a>
### Complete local contributor-aware check

On 2026-10-10 the coordinating AI for Yin read the whole proof and J32 verifier, then actually reran that verifier with its output path redirected to a disposable directory.
Every retained mathematical field matched exactly.
The rerun reproduced all60 family matrices,2148 determinant values,38 reverse-order controls, eight Gram controls and the symbolic weighted rank-three identities.
This is a rerun of the author's implementation, not a new independently written verifier.

The coordinator originated Section1's general candidate and is a contributor there.
Its complete reread checked the singular positive-semidefinite kernel and quotient argument, the signed-to-absolute Rayleigh comparison, the precise left/right Perron Cauchy--Schwarz inequality on a connected component, diagonal row-sum conclusion, spectral-radius continuity and large-t strictly triangular limit.
The root lower bound uses an intermediate-value argument, not monotonicity.
The delta corollary retains its presentation dependence.
This is a collaborator check of that component; it is not independent review merely because the author filled in the details.

The structural author supplied the shared-triangle family without derivation by the coordinator.
The coordinator separately checked the full all-r Schur-complement computations, preservation of all polynomial factors, signed Gram inertia, exact disjoint adjacent changes of basis and absence of cross-branch couplings.
Each partial absolute factor and its cost are correct, including the r<=3 neutral boundary and r>=4 positive range.
It verified the final tree's displayed positive Perron vector, the hyperbolic-cosine identity, the full cubic adjacency factor and its strict comparison at k<r.
The finite verifier's integer determinant interpolation uses degree-plus-one values and the right degrees, so its checks establish entire finite-input polynomial identities rather than values at a few unconnected test points.
The general proof, not the finite sample, supports all r and k.

No mathematical defect was found at the written scope.
The family reaches a specified cost ratio and makes the spectral lower bound sharp at its final tree; it does not prove that this endpoint is globally optimal among all allowed representations.
The source comparison is retained at the author's exact statement/locator scope, not enlarged into a review of McMullen's full gap proof.
Complete noncontributor review and fixed promotion of this new combined round remain separate from this contributor-aware check.
Unrestricted small-measure representation and optimized upper-cost control remain open.


The original 2026-10-10 day-precision whole review, its unsupported-ordering negative finding and its actual later single-sentence closure remain historical facts at their original UNKNOWN relationships.
[R653's later comparison](../audits/reviews/Yin_R_G0653_v1.md#positive-cover-isolated-whole) retains their exact inputs, correct formulas, source/static-code scope and narrow closure separately from its new whole corrected-chain review.
That later review was not an input to the original adoption above.




<a id="positive-cover-retention-bindings"></a>
## Retention and review bindings

The coordinator contributed the general Gram/Perron candidate; the structural author completed that proof and developed the exact interacting-triangle family.
The [contributor-aware check](#positive-cover-collaborator-review) remains SELF.
The complete original noncontributor review and its explicitly closed interpretation correction are retained as exact historical facts in [R653's later comparison](../audits/reviews/Yin_R_G0653_v1.md#positive-cover-isolated-whole), without upgrading their UNKNOWN arrangements or the single-sentence closure.
The latter covers both the general necessary positive-cost theorem and every all-parameter family identity, with the precise McM02 source-inspection and [J32](../computations/programs/Yin_J_G0032/readme.md) implementation boundaries.
No ordering-dependence, global optimum or unrestricted coverage is adopted.

Only completed D33 is retired after consumer repair.
Necessary J32 programs/results, the source artifact and historical review findings remain retained.
No new execution or source review is claimed by retention.
