---
author: Yin
---
# Positive-real-root domination by the complete absolute companion

Current complete mathematical home: [exact current C](../claims/Yin_C_G0566_v1.md#statement), [full proof](../claims/Yin_C_G0566_v1.md#argument) and [actual current adoption](../claims/Yin_C_G0566_v1.md#decision-complete-current-self-adoption).
The current complete [R752 finding](../audits/reviews/Yin_R_G0752_v1.md#current-g428-complete-self-finding) is constructor SELF.
All original mathematics, source/native/contribution history and mathematical next questions below retain their original dated scope; the current entry does not rebind an old review or create independent evidence.
The later complete [arbitrary-support equality criterion](../claims/Yin_C_G0568_v1.md#statement) supplies a separate bounded extension.

Date: 2026-10-18T17:52.
Human author Yin.
Root assigned a bounded S6 reuse analysis of varying original inputs, neutral stabilization and full companion costs.
The loglog_cyclic_review agent supplies the conditional deduction below.
Root supplied the broad question, not this proof step.
No native computation, matrix-box scan or new source acquisition is used.

<a id="positive-root-companion-reuse"></a>
## Reuse and the remaining conditional comparison

[L230](Yin_L_G0230_v1.md#trace-energy-companion-cost-bound) gives a complete trace/energy lower bound depending on the actual rank, energy and original trace.
Its rank-seven floor for Phi2 P6 uses the additional L210 signature/energy theorem and cannot be transferred to arbitrary ranks or neutral stabilizers.
[L185](Yin_L_G0185_v1.md#positive-absolute-cover-cost) proves positive companion cost from the symmetric absolute adjacency, using the matrix pencil tB+B^T, Perron vectors and continuity to an actual positive root.
The present proof reuses that SAME pencil and its large-t limit, with a different starting lower bound supplied by an actual positive original root.
This is an elementary local extension of that mechanism, not a novelty or source-priority claim.

The stronger general integral statement is already [L238](Yin_L_G0238_v1.md#uniform-companion-gap-and-bounded-ratio): every positive-measure integral upper-unitriangular V has m(p_abs)>=log(lambda_Lehmer), at the retained McM02 statement/applicability scope and separate large-entry argument.
That result already prevents companion/original ratio tending to zero under a fixed positive TOTAL original measure cap.
Conversely [L234](Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) proves that no positive constant comparison m_abs>=c*m_original holds for all varying original inputs: its height-one Walsh family has ratio tending to zero, many expanding pairs, repeated quadratic factors and unbounded original measure.
Those full factors cannot be deleted or divided by rank.

[L405](Yin_L_G0405_v1.md#single-expanding-complete-classification) proves m_abs>=m_original and exact equality criteria in the BIPARTITE class with one simple expanding reciprocal pair.
Its complete disconnected neutral components and its quantitative Perron-weighted frustration expense are retained.
A targeted search/read of these responsible statements and positive-root/absolute-pencil comparisons found no retained all-upper-unitriangular positive-root version below.
This is a bounded reuse result, not an exhaustive literature survey.
The new scope removes the bipartite assumption from that LOWER comparison when the original off-circle pair is positive real; it supplies no equality classification or upper-cost construction.

<a id="positive-root-companion-statement"></a>
## 1. Exact statement

Let V=I+N be any real upper-unitriangular R-by-R matrix, with N strictly upper triangular, and put

    B=|N| entrywise,
    V_abs=I-B,
    p_V(t)=det(tV+V^T),
    p_abs(t)=det(tV_abs+V_abs^T).

Both polynomials are monic of degree R and constant coefficient one.
If p_V has ANY positive real root lambda>1, then p_abs has a positive real root t0>=lambda.
Consequently its COMPLETE logarithmic Mahler measure satisfies

    m(p_abs)>=log lambda.                                  (1)

No integrality, irreducibility, connectedness, bipartite support or rank bound is required for this conditional statement.
Every complete factor and root multiplicity remains in the Mahler measure.
The theorem does not replace log lambda by the sum of all positive-root contributions.

<a id="positive-root-companion-proof"></a>
## 2. Complete proof on the actual support

Choose a nonzero REAL vector x in the kernel of lambda V+V^T; a real nonzero kernel vector exists because this is a singular real matrix.
Then

    (lambda+1)x=-(lambda N+N^T)x,
    (lambda+1)|x|<=(lambda B+B^T)|x|                 (2)

entrywise.
Let the undirected support graph have an edge i--j whenever B_ij or B_ji is nonzero.
Its connected components are invariant coordinate subspaces for N,N^T,B and B^T, because entries between different components vanish.
Choose one component C on which x is not identically zero.
It cannot be an isolated vertex, since (2)'s original kernel equation would then give (lambda+1)x_i=0.

For t>0 write

    M_C(t)=(tB+B^T)|C.

This is nonnegative and irreducible: each undirected support edge gives positive entries in BOTH directions, with weights tB_ij and B_ij.
The finite Perron interface already used in L185 supplies a strictly positive left eigenvector u of M_C(lambda), with eigenvalue rho(M_C(lambda)).
Taking the scalar product of (2) restricted to C with u gives

    (lambda+1) u^T|x_C|
       <=rho(M_C(lambda)) u^T|x_C|.

The scalar u^T|x_C| is strictly positive even if some coordinates of x_C vanish.
Therefore

    rho(M_C(lambda))>=lambda+1.                          (3)

This argument does not presume a positive signed eigenvector or connectedness of the full matrix.

Define h_C(t)=t+1-rho(M_C(t)).
Finite-matrix spectral radius is continuous, so h_C is continuous on t>0 and h_C(lambda)<=0.
The principal submatrix B_C is still strictly upper triangular in its inherited index order and is nilpotent.
Hence the SAME large-t argument as L185 gives

    rho(M_C(t))/t=rho(B_C+B_C^T/t)->rho(B_C)=0.

Thus h_C(t)>0 for all sufficiently large t.
The intermediate value theorem yields t0>=lambda with h_C(t0)=0.
If h_C(lambda)=0, one may take t0=lambda; if h_C(lambda)<0, a zero occurs strictly after lambda before a sufficiently large positive value of h_C.
At that value, t0+1 is an eigenvalue of M_C(t0), so

    det((t0+1)I_C-M_C(t0))=0.

After grouping the disconnected coordinate blocks, this determinant is a factor of

    p_abs(t)=det((t+1)I-(tB+B^T)).

Consequently p_abs(t0)=0.
Because p_abs is monic and t0>1, its whole Mahler product is at least t0, proving (1).
No monotonicity of h_C, uniqueness of t0, simplicity of the absolute root or exclusion of further off-circle roots is used.

<a id="salem-neutral-companion-consequence"></a>
## 3. Arbitrary neutral stabilization of a single positive expanding pair

Suppose now V is integral and its ENTIRE original polynomial is

    p_V=P Q,

where P is the monic minimal polynomial of a genuine Salem number alpha>1 occurring ONCE, and Q is any monic integer polynomial all of whose roots lie on the unit circle, with every multiplicity retained.
No block decomposition or sign pattern of V is assumed, and Q is not required to have bounded degree.
Its actual rank is R=deg P+deg Q.
Since m(Q)=0 and P has exactly one simple positive expanding root,

    m(p_V)=m(P)=log alpha.

Applying (1) with lambda=alpha proves

    m(p_abs)>=m(P),
    m(p_cover)=m(p_V)+m(p_abs)>=2m(P),                    (4)

where the literal full signed cover has p_cover=p_V p_abs by the accepted C2 identity.
This holds for ANY such actual integral realization and ANY neutral factor Q, including non-bipartite realizations and coupled neutral directions.
It is conditional on existence of the proper upper-unitriangular realization; it does not construct one.
The original degree d=deg P is not replaced by rank R in the measure, and neither neutral multiplicity nor extra companion factors are discarded.

Combining with the already accepted L238 lower bound gives, on this same class,

    m(p_abs)>=max{m(P),log(lambda_Lehmer)}.                (5)

This is a direct combination of lower bounds, not an asserted sharp minimum or an upper bound on achievable cost.
When m(P)<=log(lambda_Lehmer), L238 already supplies the stronger or equal numerical lower bound; the present contribution is the positive-root comparison on a wider matrix class, not a new near-one absolute-companion floor.
It supplies no lower bound for m(P) itself, no unrestricted Mahler gap and no claim that an inexpensive proper realization exists for every Salem input.
If P is repeated or if several expanding pairs occur, m(p_V) need not equal log alpha and (4) is not inferred.
L234's many-pair control is therefore consistent with (1).
Negative or nonreal outside roots do not satisfy the positive-real kernel step with lambda+1; no domination theorem for those moduli is asserted.

<a id="positive-root-companion-boundary"></a>
## 4. What changes and what remains unpaid

L230's trace/energy bound remains useful when its actual rank, trace and energy obstruction are supplied.
Neutral factors change the rank and trace and can change the admissible signatures, so the fixed-rank-seven constants cannot be inserted into the present arbitrary-Q statement.
The new lower comparison uses the positive original root itself and avoids those representation-dependent signature hypotheses.
L405 still owns its stronger equality classification and finite weighted frustration estimate within its bipartite domain; neither is extended here.

For the original S6 transfer objective, an upper-cost realization theorem or another full polynomial relation is still needed.
A lower bound on the extra factor, even (5), does not transfer a lower bound in the desired direction to the original factor.
No optimization over ranks, entries, neutral factors or a mutation orbit has been performed.
The next genuinely different mechanism would need to control an actual integral construction's COMPLETE companion from above, or exploit a stated non-bipartite equality/strictness condition with every original factor and arithmetic cost paid.
The present proof stops at (1)--(5), without developing either further mechanism.

<a id="positive-root-companion-inputs"></a>
## Inputs and author status

| Input | Exact role |
| --- | --- |
| [L185 absolute pencil](Yin_L_G0185_v1.md#positive-absolute-cover-cost) | Actual pencil tB+B^T, finite Perron vectors on connected support, spectral continuity/nilpotent-tail crossing and whole positive-root Mahler contribution; new starting bound (3) is proved here. |
| [C2 literal signed cover](../claims/Yin_C_G0002_v1.md#signed-cover-identity) | Exact full original-times-absolute determinant, not a deleted-factor or rank-normalized measure. |
| [L230 trace/energy cost](Yin_L_G0230_v1.md#trace-energy-companion-cost-bound) | General parameter-dependent lower inequality and its separate fixed-rank-seven signature premise; comparison only. |
| [L238 uniform companion gap](Yin_L_G0238_v1.md#uniform-companion-gap-and-bounded-ratio) | Accepted integral bound log(lambda_Lehmer), including its canonical McM02 source scope and large-entry branch; no new source-proof audit. |
| [L234 multiple-pair control](Yin_L_G0234_v1.md#walsh-companion-ratio-fixed-scope) | Actual height-one zero-ratio limit with unbounded original total measure and repeated positive factors, not a counterexample to the single-pair condition. |
| [L405 bipartite result](Yin_L_G0405_v1.md#single-expanding-complete-classification) | Earlier lower comparison with exact equality and disconnected neutral components; no general non-bipartite equality claim is inherited. |

The complete original author SELF finding is retained at [R752](../audits/reviews/Yin_R_G0752_v1.md#original-g428-author-self-finding).

All new deductions are by loglog_cyclic_review; root supplied only the research question.
