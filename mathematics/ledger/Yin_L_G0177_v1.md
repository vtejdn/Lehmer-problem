---
author: Yin
---

# Original integer finite cores: state-size spectral barriers and exact torsion boundary

Date: 2026-10-10.
Fixed retention under the coordinating AI for Yin's adoption instruction, after its complete noncontributor review of D46.
The authoring arithmetic agent performs this mechanical retention; it is not an independent review of its own proof.
No C acceptance or Task-completion decision is created.
G0001 remains active and unresolved.

<a id="integer-finite-core-fixed-scope"></a>
## Adopted scope

For every algebraic unit and every finite original-law compression on N actual order states, the spectral radius is at most1-1/(8N^2).
The complete [Dirichlet proof](#integer-finite-core-dirichlet-bound) retains both row and column substochasticity and integer4K, with no boundary renormalization.
Every nontrivial finite-prime restricted core at a nontorsion degree-d input has at least d+1 states; a near-one radius approximation has the stated [necessary size cost](#finite-prime-near-one-size-cost), not an entropy lower certificate from one truncation.
The exact [torsion control](#torsion-quantized-near-one-control) shows N-to-minus-two order is unavoidable over the full original algebraic-unit domain, even with trace(4K)=2 and the genuine reciprocal involution.
It is explicitly not a nontorsion Salem family or an ESS finite-prime example.

The complete author argument and separate review follow without mathematical alteration.
Their earlier pending status records the drafting stage and is superseded by this adoption statement.
No new source theorem, numerical calculation, program or fixed-input actual-core claim is introduced in retention.

<a id="retained-integer-finite-core-argument"></a>
## Preserved complete D46 argument and independent finding

## Integer finite cores: a size-dependent spectral barrier and its exact boundary

Date: 2026-10-10.
Arithmetic/operator author inquiry by resultant_research for Yin.
The question is whether integrality of the original weighted finite-core matrices can exclude full spectral radius approaching one.
All mathematical development belongs here.
The original weights are (1/4,1/2,1/4); no numerical enumeration is planned.

### Scope and reuse screen

Read the exact collision-radius and finite-prime exhaustion results of [L173](Yin_L_G0173_v1.md#collision-operator-fixed-scope), the complete finite-prime domain and rational renewal law of [L157](Yin_L_G0157_v1.md#finite-prime-return-core), and [L154](Yin_L_G0154_v1.md#uniform-small-unweighted-return-tail).
L154 already proves that small complete unweighted first-return mass need not control the weighted tail, so repeating that argument is not this round's target.
The new target is an exact dimension-dependent bound from doubly substochastic quantization, together with an actual original-law algebraic control showing the unavoidable size dependence.
No uniform entropy or near-one Salem construction is claimed.

<a id="integer-finite-core-dirichlet-bound"></a>
### 1. Every finite original compression has a polynomial size gap

Let alpha be an algebraic unit, including possibly torsion, O=Z[alpha], and F a nonempty finite subset of O of size N.
On counting-measure l2(F), take the genuine killed original matrix

    K_F(x,y)=sum_(eta in {-1,0,1}) p_eta 1_(y=alpha*x+eta),
    p_0=1/2, p_(-1)=p_1=1/4.                            (1)

There is no renormalization at the boundary.
Then

    r(K_F)<=1-1/(8N^2).                                (2)

This applies, in particular, to every finite-prime core D_S supplied by L157 for a nontorsion input.
It does not imply a uniform gap on their increasing union.

For each fixed eta the map x->alpha*x+eta is injective, so all row sums and all column sums of K_F are at most one, and 4K_F has nonnegative integer entries.
Put

    H=(K_F+K_F^T)/2,
    delta_x=1-sum_y H(x,y)>=0.

Every positive off-diagonal H entry and every positive delta_x is at least1/8.
Every connected component of the undirected H graph has a vertex with delta_x>0.
Otherwise all its H row sums equal one.
Since both original row and column sums are at most one, each original row sum at those vertices must then equal one.
No positive original edge leaves the component, by its definition, so a finite nonempty component C would be invariant under both x->alpha*x and x->alpha*x+1.
Injectivity makes alpha*C=C and alpha*C+1=C, hence C+1=C, impossible for a nonempty finite subset of a characteristic-zero field.
This proves the existence of leakage without a nontorsion hypothesis.

The exact quadratic-form identity for any complex vector f is

    <f,(I-H)f>
      =sum_({x,y}, x!=y) H(x,y)|f(x)-f(y)|^2
                         +sum_x delta_x |f(x)|^2.      (3)

The first sum is over unordered pairs once.
Choose in each connected component C a leaking root o and a spanning tree.
Write n=|C|.
For every x in C, express f(x) as f(o) plus the edge differences along its tree path.
Cauchy--Schwarz, using at most n summands, gives

    sum_(x in C)|f(x)|^2
       <=n^2 [ |f(o)|^2+sum_(tree edges)|f(x)-f(y)|^2 ].

Equation(3) dominates one eighth of the bracket.
Summing over components and using n<=N proves

    <f,(I-H)f> >= ||f||_2^2/(8N^2).                   (4)

The finite nonnegative matrix K_F has a nonnegative Perron eigenvector v for its spectral radius r.
Normalize its l2 norm to one.
Then <v,Hv>=<v,K_Fv>=r, so (4) proves(2).
This uses the ordinary finite-dimensional Perron theorem; neither selfadjointness nor normality of K_F is assumed.
For a strongly connected finite core this vector is strictly positive.

The exact integrality being used is the quantization of both conductances and boundary deficits.
Integrality of a characteristic polynomial alone is weaker: det(4I-4K_F) is a nonzero integer, while all eigenvalues of 4K_F have modulus at most four.
Factoring off its real Perron eigenvalue gives only

    1<=det(4I-4K_F)<=(4-4r)8^(N-1),
    1-r>=1/[4*8^(N-1)].                              (5)

The determinant is positive: the positive real factors 4-lambda for real eigenvalues and the positive conjugate-pair products give this sign.
The two-sided substochastic graph structure improves this elementary exponential-in-N bound to the polynomial bound(2).
No determinant divisibility beyond its integer value is claimed.

<a id="finite-core-degree-size-barrier"></a>
### 2. Actual finite-prime cores also retain a degree barrier

Suppose now that alpha is nontorsion with minimal-polynomial degree d, and let F=D_S be a finite-prime restricted core as defined in L157.
Its graph is the strongly connected component of zero in the fully restricted original graph.
If F has a nonzero state, a restricted closed word must leave zero via eta=+1 or-1 after any initial zero self-loops.
Take such an edge and then a shortest path back to zero inside F.
The resulting nontrivial zero-to-zero cycle has length l<=N: the shortest return path has no repeated vertex and first reaches zero at its endpoint.
Its first digit is nonzero, so its endpoint polynomial has degree l-1 and is divisible by the minimal polynomial.
Hence

    D_S={0}, or |D_S|>=d+1.                           (6)

This is the state-count version of the already retained first-return length obstruction f_n=0 for2<=n<=d in L154.
It is not a new bound on the degree of an unrestricted input.
Every D_S has its original weight-one-half self-loop at zero, so r(K_S)>=1/2 and (2) gives

    1/2<=r(K_S)<=1-1/(8|D_S|^2).

The core {0} has radius exactly1/2.
If a nontrivial cycle of length l and probability a>0 is present, concatenating it with the zero self-loop gives a return series dominating1/(1-z/2-a z^l).
Its positive singularity is below2, so r(K_S)>1/2.
Thus improvement over the singleton radius really requires the nontrivial alternative in(6).
This uses complete actual restricted words and their original product probabilities.

<a id="finite-prime-near-one-size-cost"></a>
### 3. What a near-one full radius would force on finite approximants

For a fixed nontorsion input, L173 proves

    r(K_S) increases along the stated exhaustion to r(K_act)=exp(-h_2).

Its entropy approximants -log r(K_S) decrease from above.
Preserve that direction.
If one finite core approximates the full radius within an additive epsilon>0,

    r(K_S)>=exp(-h_2)-epsilon,

then(2) forces the actual state cost

    |D_S| >= [8(1-exp(-h_2)+epsilon)]^(-1/2).         (7)

For a Salem beta in(1,2), put m=log(beta).
The retained h_2<=m gives, whenever0<epsilon<=m,

    |D_S|>=1/(4 sqrt(m)).                            (8)

This is a conditional implication along any hypothetical near-one Salem family, not a construction of that family.
The exact exhaustion supplies an approximating finite core for each fixed input and epsilon, but gives no bound on its prime set or its cardinality.
The independent condition(6) also applies to every nontrivial chosen core.
None of these lower state costs can be reversed into an upper entropy estimate with a new sign, or into an upper full radius from one finite truncation.

More precisely, the positive Perron profile v_S, normalized in l2, satisfies the exact identity

    1-r(K_S)
      =sum_({x,y}, x!=y) H_S(x,y)|v_S(x)-v_S(y)|^2
                            +sum_x delta_x v_S(x)^2. (9)

Thus radius close to one requires an actual positive eigenprofile with both small aggregate edge variation and small mass at leaking boundary vertices.
The individual summands are nonnegative and their nonzero coefficients are quantized in units of1/8.
Their smallness is not contradicted by integrality: the eigenvector coordinates are unrestricted real algebraic numbers and can spread over arbitrarily many vertices.
Formula(9) describes the exact finite mechanism that a further arithmetic argument would have to obstruct.

<a id="torsion-quantized-near-one-control"></a>
### 4. An exact actual-law control makes the N^(-2) order unavoidable

Take the torsion algebraic unit alpha=-1, with O=Z and the same original digits and probabilities.
Its unrestricted actual returning core is all of Z.
Indeed two original steps with digits(0,+1) send x to x+1, and(0,-1) send x to x-1, so every integer is both reachable from zero and returnable.
For L>=1 restrict states to

    F_L={-L,...,L},  N=2L+1.

The same two-step moves stay inside F_L whenever their endpoints do, because the intermediate state is -x.
Thus F_L is exactly the strongly connected restricted returning core for this finite allowed-state domain; it is not an arbitrary collection of unconnected vertices or a reassigned word law.
It is not asserted to be a finite-prime core D_S, and L157's nontorsion/ESS theorem does not apply to alpha=-1.

Let Rf(x)=f(-x), and let C_N be the killed lazy nearest-neighbor matrix on F_L,

    (C_N f)(x)=f(x)/2+[f(x-1)+f(x+1)]/4,

with values outside F_L set to zero.
The actual alpha=-1 compression is exactly

    K_L=R C_N=C_N R.                                 (10)

With vertices indexed j=1,...,N, the sine vectors sin(pi k j/(N+1)) have C_N eigenvalues1/2+(1/2)cos(pi k/(N+1)).
The top vector is positive and invariant under R.
Consequently it is also a K_L eigenvector with the same top eigenvalue; the reverse upper bound follows from ||K_L||=||C_N||.
Hence

    r(K_L)=cos^2(pi/[2(N+1)]),
    1-r(K_L)=sin^2(pi/[2(N+1)])
               ~pi^2/[4(N+1)^2].                    (11)

All matrices4K_L are nonnegative integer matrices with the original weights2,1,1 before killing, at most three incoming and outgoing edges per vertex, and row and column sums at most four.
They are irreducible and have a weight-two self-loop at zero.
There are no other diagonal entries: -x+eta=x with x integral and eta in{-1,0,1} forces x=0 and eta=0.
In particular

    Tr(4K_L)=2

for every L.
They also retain the genuine reciprocal involution T(x)=alpha^(-1)x=-x, with K_L^*=U K_L U; in fact K_L is selfadjoint here because R and C_N commute.
These stronger exact constraints still allow the radii in(11) to approach one.
Thus no dimension-free forbidden neighborhood follows from quantization, two-sided substochasticity, the zero-only self-loop, reciprocal symmetry and this actual restricted-word structure alone.
The N^(-2) order in(2) cannot be improved to a larger order uniformly over this original-law algebraic-unit domain.

For completeness the unrestricted original endpoint law here is the same as the usual sum of n symmetric eta digits, since multiplying any eta by(-1)^j preserves its distribution and independence.
Therefore

    p_n=binomial(2n,n)/4^n >=1/(2n+1),

where the last inequality follows because the central binomial coefficient is maximal among the2n+1 coefficients summing to4^n.
Since p_n<=1, its nth-root rate is one.
This agrees exactly with L173's torsion-inclusive radius identity and with the finite radii(11).
It is an actual zero-entropy torsion control, not an unproved near-one nontorsion or Salem sequence.

### 5. Discriminating conclusion and next boundary

The useful positive result is a quantitative finite-core barrier from the actual integer-weight graph, polynomial in its state size, plus the exact eigenprofile identity(9).
Its sharp-order control shows why matrix integrality itself cannot yield a degree-free spectral exclusion.
The counterpressure remains explicitly torsion; it does not refute an additional Salem-specific theorem based on the complete embeddings, absence of torsion, or relations among all loop polynomials.

Bounding all finite-core sizes is not a plausible replacement premise: the two already fixed infinite Salem cores have unbounded sizes along exhaustion even though their entropy is positive.
A meaningful stronger test would constrain the low-variation positive Perron profiles in(9) through actual non-torsion arithmetic or retain all excursions in a full-kernel estimate.
A new condition must be checked on those profiles and on an increasing family of genuine cores; an integer characteristic polynomial or one favorable finite-prime compression is insufficient.
The complete renewal-tail warning is already in L154 and has not been relabeled as a new result here.

### 6. Checking, sources and status

The assigned arithmetic agent authored and self-checked the full proof, including the factor-of-two convention in(3), each connected component's leakage, finite Perron usage, positive determinant sign, first-return/state degree count, the direction of finite-prime approximation, exact original two-step paths for alpha=-1, sine eigenvector normalization and the torsion boundary.
The coordinating agent assigned the broad arithmetic/operator question but supplied none of these derivations before this draft.
A bounded local screen found the previously retained norm, finite-prime and renewal interfaces stated above; no novelty or exhaustive literature-search claim is made.
These elementary finite-matrix deductions use no newly adopted external source, numerical enumeration or computational result.
No J is necessary.
Independent mathematical review and fixed adoption are pending; unrestricted G0001 remains unresolved.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0076_v1.md#separate-complete-independent-mathematical-review), with its original inspected scope and relationship.




<a id="integer-finite-core-retention-record"></a>
## Retention and review bindings

The resultant_research AI authored D46 and self-checked it.
The coordinating AI assigned only the broad question, supplied no derivation, and recorded the complete nonblind noncontributor finding retained above.
It then explicitly authorized fixed retention.
The same authoring arithmetic agent retained the complete argument and review here and retired D46 under that authorization.

| Review | Target | Scope |
| --- | --- | --- |
| [Complete noncontributor finding](../audits/reviews/Yin_R_G0076_v1.md#finite-core-size-independent-review) | [Integer finite compression bound](#integer-finite-core-dirichlet-bound) | Full leakage, Dirichlet-form, spanning-tree, Perron and determinant comparison proof, with the original weights and both row/column bounds. |
| [Complete noncontributor finding](../audits/reviews/Yin_R_G0076_v1.md#finite-core-size-independent-review) | [Degree/state barrier](#finite-core-degree-size-barrier) and [near-one size cost](#finite-prime-near-one-size-cost) | Actual restricted-word domain, first-return/state count, correct finite-prime radius approximation direction and exact positive-eigenprofile identity. |
| [Complete noncontributor finding](../audits/reviews/Yin_R_G0076_v1.md#finite-core-size-independent-review) | [Torsion control](#torsion-quantized-near-one-control) | Actual alpha=-1 finite allowed-state cores, unchanged law, exact sine radius, trace/involution conditions and unrestricted collision rate; no transfer to finite-prime nontorsion or Salem inputs. |
