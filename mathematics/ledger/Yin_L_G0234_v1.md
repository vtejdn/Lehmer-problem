---
author: Yin
---

# Height-one signed Gram matrices and vanishing companion ratios

The complete current mathematical home is [C573](../claims/Yin_C_G0573_v1.md#walsh-companion-ratio-fixed-scope), adopted at 2026-10-22T19:35 after the [actual current whole SELF](../audits/reviews/Yin_R_G0755_v1.md#current-complete-whole-self-finding).
The original dated argument and frozen input below remain the actual input of R133; current links do not backfill that review or supply its missing relationship declaration.

Date: 2026-10-10.
The original2026-10-10 coordinating account adopted this restricted result after its separately organized noncontributor review at the original scope.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="walsh-companion-ratio-fixed-scope"></a>
## Original adopted scope and fixed review input

An explicit integer character-matrix construction of every dyadic size gives integral upper-unitriangular presentations of height one with full original polynomial Q_r^r and absolute companion Phi2^(2r-2) Q_(r^2).
All lattice determinants, dimensions, multiplicities and complete cover costs are retained.
Its companion-to-original measure ratio tends to zero, proving that the unrestricted-rank companion ratio infimum is zero and the complete-cover ratio infimum is one, both unattained.
The original total measure grows without bound and its irreducible factor stays quadratic.
No bounded-measure, increasing irreducible-degree, near-one or unrestricted scalar-realization conclusion is asserted.


<a id="complete-retained-proof-and-review"></a>
## Complete original author proof and dated review input

## Varying-rank realization and complete absolute-companion cost

Date: 2026-10-10.
Starting question: After L230 proves the rank7 versus rank8 tradeoff, investigate a genuinely changed varying-rank or varying-input construction, or a new universal comparison between original and absolute-companion measure.
Explore a bold structural hypothesis and test it exactly before sustained enumeration.
Preserve all polynomial factors, integral unitriangular data and complete cost; do not repeat the settled rank7 comparison.


### Reuse resolves the first conjecture and changes the target

The proposed comparison m(p_(V^-))>=m(p_V) is already false in the fixed record.
The complete [L191 signed Gram control](Yin_L_G0191_v1.md#signed-gram-cover-cost-control) has original measure2 arcosh(3/2) and absolute-companion measure arcosh2, strictly smaller.
Its full factors and complete separate review were reread.
That counterexample is reused, not rediscovered or promoted as this round's contribution.
The [L230 all-rank7 bound](Yin_L_G0230_v1.md#companion-tradeoff-fixed-scope) has its exact prescribed-input scope; it is not a general ordering of original and companion measures.

The next question is stronger and different: is there some universal c>0 with m(p_(V^-))>=c m(p_V) for every integral upper-unitriangular V of positive measure, perhaps even with all strict-upper entries in{0,1,-1}?
The construction below disproves this stronger comparison by increasing rank, with every full determinant and multiplicity retained.
It also computes the exact infimum of the full signed-cover/original cost ratio in this class.
It does not make the original measure bounded or near zero.

The actual block determinant and spectral formula for arbitrary real rectangular B are already in [L175](Yin_L_G0175_v1.md#sparse-trinomial-auxiliary) and reused explicitly in [L191, Section2](Yin_L_G0191_v1.md#higher-degree-phi2-realization).
We invoke that formula directly.
L191's special identity |B|^T|B|=A# applies only to its sparse row construction and is NOT imported for the new B below.
The new example is precisely a different integral Gram factorization where cancellation between dense signed rows matters.
The full two-sheet cover is the [D9 literal construction](../claims/Yin_C_G0002_v1.md#signed-cover-identity); the strict positive-companion input is the [fixed L185 theorem](Yin_L_G0185_v1.md#positive-absolute-cover-cost).

The matrix used below is the standard Boolean character, or Walsh, matrix.
Its characters and their finite orthogonality are already used in [L223](Yin_L_G0223_v1.md#partial-mask-collision-information-retention).
The existing [ODo07 source record](../audits/literature/ODo07/readme.md#boolean-hypercontractivity-attribution) owns the checked author lecture and Boolean Fourier convention.
Its retained PDF p.4 was text-read again for that convention.
We use only the character definition and the direct finite product sum below, not the lecture's hypercontractivity theorem or an uninspected Hadamard existence/classification theorem.
This standard character matrix and its orthogonality are not claimed new.
Local reuse supplies all needed inputs; no new source registration, external theorem acceptance, computation or program is required.

<a id="walsh-companion-ratio-construction"></a>
### 1. A dense signed integral root basis in every dyadic size

Let k>=3, r=2^k, and index rows and columns by binary vectors a,b in{0,1}^k.
Define the integer r-by-r matrix

    H_(a,b)=(-1)^(a dot b).                               (1)

The exponent is read modulo2.
For any b,c,

    (H^T H)_(b,c)
      =sum_a (-1)^(a dot(b+c))
      =product_(j=1)^k [1+(-1)^(b_j+c_j)]
      =r if b=c, and0 otherwise.                         (2)

Thus H^T H=r I, whereas entrywise |H|=J, the all-ones matrix, and J^T J=r J.
Put

    V_r=[[I_r,-H],[0,I_r]].                              (3)

This is an actual integral upper-unitriangular matrix in the displayed block order.
All diagonal entries are1 and each strict-upper nonzero entry is plus or minus1.
Its rank is2r, its height is1, and its squared-entry energy is E=r^2.
The underlying integer lattice is Z^(2r) in its displayed standard basis, with symmetric pairing

    G_r=V_r+V_r^T=[[2I_r,-H],[-H^T,2I_r]].               (4)

Every standard basis vector is an integral norm-two root and these roots form a unimodular basis of this lattice; there is no denominator, rescaling or claimed identification with the different fixed rank7 lattice of L226.
The symmetric eigenvalues are2+sqrt r and2-sqrt r, each with multiplicity r, since the singular values of H are all sqrt r.
For r>=8, G_r is nondegenerate, has inertia(r,r), and det G_r=(4-r)^r.
The different lattice determinant is retained as part of the varying-rank construction.

For any integer s>4 set

    Q_s(t)=t^2-(s-2)t+1,
    lambda_s=[s-2+sqrt(s(s-4))]/2>1,
    a(s)=log lambda_s=arcosh((s-2)/2).                   (5)

The block determinant identity with equal block sizes, together with(2), gives the entire original polynomial

    p_(V_r)(t)
      =det((t+1)^2 I_r-t H^T H)
      =Q_r(t)^r.                                       (6)

This has degree2r, is monic integral reciprocal with constant1, and has no omitted cyclotomic multiplier.
Each Q_s in(5) is irreducible over Q: with A=s-2>=3, its discriminant A^2-4 lies strictly between(A-1)^2 and A^2.
Its two roots are positive reciprocal roots lambda_s and lambda_s^-1.
Therefore(6) has exactly r expanding roots counted with multiplicity and

    m(p_(V_r))=r a(r)>0.                                (7)

The original polynomial is reducible, being a repeated quadratic factor; no unbounded irreducible-degree coverage is inferred from increasing matrix rank.

<a id="walsh-full-absolute-cover-cost"></a>
### 2. Absolute values collapse the expanding Gram spectrum

The complete absolute presentation is

    V_r^-=[[I_r,-J],[0,I_r]].                            (8)

The eigenvalues of J^T J=r J are r^2 once and0 with multiplicity r-1.
Hence its entire determinant and measure are

    p_(V_r^-)(t)=(t+1)^(2r-2) Q_(r^2)(t),
    m(p_(V_r^-))=a(r^2)>0.                              (9)

All2r-2 neutral factors are retained.
Taking absolute entries has changed r independent expanding trace directions into one larger expanding direction and r-1 zero Gram directions.
It is therefore the sum of expanding logarithms, rather than just the largest root, that distinguishes(7) from(9).
The largest companion root grows faster than each individual original root, while its full measure is much smaller than their sum with multiplicities.

The absolute symmetric adjacency here is [[0,J],[J,0]], with spectral radius r.
L185's already proved lower bound is therefore2 arcosh(r/2)=arcosh((r^2-2)/2)=a(r^2), exactly the value in(9).
Thus this family attains that adjacency-dependent lower bound; the comparison does not weaken L185 or prove an optimum over all representations of its original polynomial.

Let W_r be the actual two-sheet upper-unitriangular cover: each original upper entry a<=0 becomes a I2 and each a>0 becomes [[0,-a],[-a,0]], in vertex-then-sheet order, with every diagonal block I2.
The equal/opposite sheet decomposition of the full pencil gives

    p_(W_r)=p_(V_r) p_(V_r^-)
           =(t+1)^(2r-2) Q_r^r Q_(r^2),
    rank W_r=4r, height W_r=1, E(W_r)=2r^2,
    m(p_(W_r))=r a(r)+a(r^2).                            (10)

The degrees add to(2r-2)+2r+2=4r.
No half-rank normalization, deleted power, or change to the required integral diagonal-one determinant convention occurs.
Formula(10) specifies the whole cover polynomial, including every repeated noncyclotomic factor.

The growth and ratio can be bounded without numerical root calculations.
For any s>4,

    s-3<lambda_s<s-2,
    log(s-3)<a(s)<log(s-2).                             (11)

Indeed s-4<sqrt(s(s-4))<s-2, as follows by squaring the positive quantities.
For r>=8 one has r-3>sqrt r; the difference is already positive at8 and increases thereafter, or its squared form r^2-7r+9>0 increases for integers r>=8.
Consequently

    0 < m(p_(V_r^-))/m(p_(V_r))
      =a(r^2)/(r a(r))
      <2log r/[r log(r-3)]<4/r.                       (12)

In particular every member r>=8 strictly violates m(p_(V^-))>=m(p_V), and the ratio tends to zero at bounded entry height1.
More precisely(11) gives a(r)/log r ->1 and a(r^2)/log r ->2, so the ratio is asymptotic to2/r.
Meanwhile the original measure exceeds r log(r-3) and tends to infinity; the companion measure also tends to infinity.
The ratio limit is not a bounded-original-measure statement.

<a id="height-one-cover-ratio-infimum"></a>
### 3. An exact unrestricted-rank cost infimum, with a different quantifier from Lehmer

Consider the class of all finite integral upper-unitriangular matrices V with m(p_V)>0, using this fixed literal absolute companion and signed cover W(V).
The fixed L185 theorem gives m(p_(V^-))>0 for every member.
Additivity of the full cover measure therefore gives

    m(p_(W(V)))/m(p_V)
      =1+m(p_(V^-))/m(p_V)>1.                          (13)

The matrices(3) are members, and(12) approaches this lower boundary.
Thus

    inf_V m(p_(W(V)))/m(p_V)=1,
    inf_V m(p_(V^-))/m(p_V)=0,                         (14)

and neither infimum is attained by a positive-measure member.
The same two infima hold if the class is restricted to strict-upper entries in{0,1,-1}, since(3) already has that property and L185 still applies.
These are infima over all such original inputs and ranks, not optimization in a fixed mutation orbit or over presentations of one fixed polynomial.
There is no constant c>0, even in the height-one class, such that the complete companion measure is at least c times the original measure.

The familiar achieved cover cost2m has a different sufficient condition.
If V can be made equal to V^- by a diagonal sign congruence, then p_V=p_(V^-) and p_W=p_V^2, so its complete measure is exactly2m(p_V).
For a block form [[I,-B],[0,I]], a sufficient condition is |B|=D_1 B D_2 for diagonal sign matrices D_1,D_2: their block diagonal congruence produces the absolute presentation.
Nonnegative B is the immediate case, including L191's quartic family and the rank8 P6 control.
Our H cannot satisfy that condition for r>1, because diagonal signs preserve its rank r whereas J has rank1.
This is only a sufficient sign condition, not a classification of all polynomial coincidences or of when equality of the two measures occurs.
The new(14) proves that2m is not a universal lower cost, even though it is an attained exact cost in those earlier constructions.

### 4. Exact first member, structural scope and next test

At r=8 the construction is already explicit through the64 signs H_(a,b)=(-1)^(a dot b), a,b in{0,1}^3.
It has rank16, height1, E=64, and

    p_V=(t^2-6t+1)^8,
    p_(V^-)=(t+1)^14(t^2-62t+1),
    p_W=(t+1)^14(t^2-6t+1)^8(t^2-62t+1),
    rank W=32, E(W)=128,
    m(p_V)=8 arcosh3,
    m(p_(V^-))=arcosh31.                              (15)

This is a direct all-parameter specialization, not a finite search or numerical optimum.
Its factors are complete and its quadratic discriminants32 and3840 are nonsquares.
The strictly smaller companion measure follows already from(12).
A separate short direct check is cosh(4 arcosh3)=577>31, which gives arcosh31<4 arcosh3<8 arcosh3.
No floating root approximation is required.

The mechanism is dense sign cancellation in an integer Gram matrix.
It lies within the old real block determinant interface but outside the special L191 sparse-row identity A to A#.
Indeed H^T H=rI while |H|^T|H|=rJ, not rI.
This is the actual construction change, not a renaming of the earlier trace matrix.
It gives no new arbitrary reciprocal polynomial prescription, and its positive irreducible factor always has degree2.
The large multiplicity and growing measure are fully charged; neither can be discarded to simulate a near-one or unbounded irreducible-degree result.

The universal proportional-cost conjecture is therefore closed negatively at this scope, and(14) identifies the exact unrestricted-rank ratio boundary.
A genuinely discriminating continuation must restrict or control the original measure, noncyclotomic multiplicities or irreducible target complexity while preserving integral realization.
For example, determine whether an analogous collapse can coexist with bounded positive total original measure and an irreducible target of increasing degree, or whether those additional conditions force a quantitative companion cost.
The present proof supplies neither outcome and does not justify extrapolating(14) into the near-one regime.

### Contribution and author self-check

The coordinator assigned the broad varying-rank/cost question and suggested testing the unsupported comparison m_abs>=m_original.
The reuse screen found its already adopted L191 counterexample before any such comparison was claimed new.
The authoring orbit agent supplied the stronger dyadic character-matrix construction, all full-factor and lattice calculations, the asymptotic and exact ratio bounds, and the nonattained infima(14).
The standard block determinant, character orthogonality, signed cover and strictly positive-companion theorem are explicitly reused at their stated scopes.
No external novelty claim is made.

The complete original author SELF account is retained in [R755](../audits/reviews/Yin_R_G0755_v1.md#original-g234-author-self-finding), at its original input and date precision.
The first member in(15) was checked by the same exact formulas, not by a program.
No J, numerical scan, new source acceptance or source-proof audit was used.
The original author argument was frozen before the subsequent complete noncontributor review and adoption.

Author freeze: 2026-10-09T22:35.
The complete author argument, Sections1--4 and equations(1)--(15), including the reuse finding, all factors/costs and contribution boundaries, was the original frozen input of the subsequently recorded complete noncontributor review.
There are no author program/output artifacts for this round.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0782_v1.md#walsh-companion-complete-independent-review), with its original inspected scope and relationship.
