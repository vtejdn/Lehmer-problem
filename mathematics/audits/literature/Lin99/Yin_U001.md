---
author: Yin
---

<a id="lin99-u001"></a>
# Lin99-U001: small boundaries, point-separating low-entropy factors, and the algebraic-category boundary

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Lin99 published NUMDAM scan](../../../literature/pdf/Lin99.pdf). The detailed comparison uses the separately registered [Lin95 author manuscript](../../../literature/pdf/Lin95--author-ps-converted.pdf), not an inspected copy of its journal edition, and the [SW91 journal scan](../../../literature/pdf/SW91.pdf).

Passages: Lin99 Definition 3.2 and the closed-set observation, printed p.232 (PDF p.7); Definition 6.1 and Theorem 6.2, p.251 (PDF p.26); Lemma 6.3, pp.252-253 (PDF pp.27-28); Theorem 6.7, Lemma 6.8 and the proof sketch, pp.256-257 (PDF pp.31-32); introduction p.228 and statements in pp.258-260 for comparison. Detailed proof interfaces: Lin95 Section 4, author pp.12-20, especially Lemma 4.2, Sections 4.3-4.4, Proposition 4.5, Lemma 4.9 and Theorem 4.10; SW91 Sections 1-2, pp.537-540.

Inspection: 2026-10-18, Yin; prepared by root under the explicit request for source reading and strategy analysis while G0001 remains paused. The statement, the small-neighborhood and coding estimates, the closed quotient, the symbolic extension and the periodic-point completion were checked, with the reconstruction below. Critical Lin99 pp.256-257 and Lin95 author pp.14-20 were read as page images; the image-only SW91 pp.537-545 were read visually. This is a single-agent source check with self-check of the record, not a second independent review or formal verification.


## Assessment and exact scope

**Audited within scope** for the implication in Theorem 6.7, using the standard compact-quotient and topological-entropy interfaces listed below and correcting the quotient-metric sentence as Lin99 itself instructs.
The theorem is accepted as an external topological result for this bounded comparison.
Lin99 labels its own argument a rough sketch and treats only the case of nonperiodic separating points there.
The periodic completion below specializes the repeated-block device in Lin95 Lemma 4.2 under the stronger SBP hypothesis; it does not silently extend the scope of the printed sketch.

The proof of Lin99 Theorem 6.2, the embedding theorem, and the universal zero-mean-dimensional factor results were not audited.
Their relevant statements were read to separate the hypotheses of Theorem 6.7 from the additional minimal-extension hypotheses used to obtain SBP from zero mean dimension.
No theorem about all finite-entropy systems having SBP is accepted.
The source-reading accounts for [Lin95](../Lin95/readme.md) and [SW91](../SW91/readme.md) retain their distinct coverage and version limits.

<a id="topological-factors-and-entropy"></a>
## Definition: topological factors and entropy conventions

Let X be a compact metrizable space and T:X to X a homeomorphism.
A topological factor consists of a compact metrizable space Y, a homeomorphism S:Y to Y, and a continuous surjection pi:X to Y satisfying pi T=S pi.
No group structure or homomorphism property is part of this definition.
When X and Y are compact abelian groups and the maps are group automorphisms, requiring pi also to be a group homomorphism is an additional algebraic-factor condition.

For a compatible metric d, put d_n(x,y)=max_{0<=j<n} d(T^j x,T^j y), and let s_n(delta) be the maximum cardinality of a set whose distinct points have d_n-distance greater than delta.
The topological entropy is

\[
h_{\rm top}(X,T)=\lim_{\delta\downarrow0}\limsup_{n\to\infty}
  \frac{1}{n}\log s_n(\delta).
\]

All logarithms in this record are natural.
Changing the logarithm base only rescales the prescribed epsilon.
The finite-valued entropy assumption is not needed in Theorem 6.7.

<a id="orbit-capacity-and-small-boundary"></a>
## Definition: orbit capacity and the small boundary property

For a subset A of X define

\[
\operatorname{ocap}(A)=\lim_{n\to\infty}\frac1n
 \sup_{x\in X}\sum_{j=0}^{n-1}1_A(T^jx)
=\inf_{n\ge1}\frac1n\sup_{x\in X}\sum_{j=0}^{n-1}1_A(T^jx).
\]

The equality and existence follow from subadditivity of the unnormalized suprema.
A set is uniformly small when its orbit capacity is zero.
Orbit capacity is subadditive for finite unions and invariant under T and its inverse.
For a closed set A, the source identifies orbit capacity with sup_mu mu(A), where mu ranges over all T-invariant Borel probability measures.
In particular, closed A is uniformly small exactly when every such measure gives A mass zero.
SW91 p.538 proves the zero-capacity equivalence by empirical measures and compactness; the closedness hypothesis is essential.
This is uniform control over orbit segments and all invariant measures, not smallness for one distinguished measure.

The small boundary property, abbreviated SBP, means that for every x in X and every open neighborhood U of x there is an open neighborhood V of x, contained in U, with ocap(boundary V)=0.
If the source's word neighborhood is not assumed open, taking its interior gives the same usable convention.
No finite dimension, minimality, aperiodicity or finite entropy is included in this definition.

<a id="point-separating-small-factor"></a>
## Exact result: Lin99 Theorem 6.7

If (X,T) has SBP, then

\[
\forall a,b\in X\ (a\ne b)\quad\forall\varepsilon>0\quad
\exists(Y,S),\pi:X\twoheadrightarrow Y:
\quad \pi T=S\pi,\quad \pi(a)\ne\pi(b),\quad
h_{\rm top}(Y,S)<\varepsilon.
\]

The factor is nontrivial because it separates the selected pair.
The displayed conclusion does not require that this particular factor have positive entropy.
Neither its dimension nor the number or regularity of its defining observations is uniformly bounded by the theorem.
The minimal-extension condition occurs in Theorem 6.2 and Corollary 6.9, not in Theorem 6.7 once SBP is assumed.
Finite entropy implies zero mean dimension in the background theory, but the paper's reverse implication from zero mean dimension to SBP has additional hypotheses.

<a id="coding-entropy"></a>
## Definition and estimate: binary coding entropy

For a set U in X let

\[
M_U(x)=(1_U(T^j x))_{j\in\mathbb Z},\qquad
\mathcal S_U=\overline{M_U(X)}\subset\{0,1\}^{\mathbb Z},\qquad
h(U)=h_{\rm top}(\mathcal S_U,\sigma).
\]

The closure is taken in the product topology.
The coding map M_U need not be continuous; the shift space is a counting device and is not automatically a topological factor of X.
Its entropy is lim_n n^{-1} log |W_n(S_U)|, where W_n denotes the set of length-n binary words occurring in the shift space.
For 0<=delta<1/2, ocap(U)<=delta implies

\[
h(U)\le H_2(\delta),\qquad
H_2(u)=-u\log u-(1-u)\log(1-u),
\]

with H_2(0)=0.
Indeed, for each delta'>delta and all sufficiently large n, every coded n-block has at most delta' n ones.
Taking closure adds no new finite words beyond those occurring in M_U(X).
The number of such blocks is bounded by the sum of binomial coefficients up to floor(delta' n); taking logarithmic rates and then delta' down to delta gives the estimate.
This is the sparse-word estimate used in SW91 p.537 and Lin95 author p.15, with the capacity convention of Lin99.

<a id="proof-reconstruction"></a>
## Checked proof reconstruction

### 1. Small closed sets have small open neighborhoods

Lin99 Lemma 6.3 says that for closed E and gamma>0 there is open W containing E with ocap(W)<=ocap(E)+gamma.
Choose a block length N for which the occupation bound for E is already within a strict gamma margin.
Every forbidden intersection of the corresponding finitely many translates of E is empty.
Compactness preserves all these finitely many empty intersections after replacing E by a sufficiently small open neighborhood, and hence preserves the finite-block occupation bound.
Subadditivity then gives the capacity estimate.

Lin99 Lemma 6.8 has the essential hypothesis closure U contained in U', for open U and U'.
It produces open U contained in V contained in U' with uniformly small boundary.
Cover the compact boundary of U by finitely many SBP neighborhoods inside U' and adjoin those neighborhoods to U.
The new boundary is contained in their finite union of boundaries.
Combining the two lemmas allows boundary neighborhoods to have arbitrarily small coding entropy, arbitrarily small geometric width, and uniformly small boundary again.

### 2. The first separating set, including a periodic point

For a nonperiodic a, the singleton {a} has zero orbit capacity because an orbit visits a at most once.
The preceding lemmas supply a small-entropy open U_1 with a in U_1, b outside closure U_1, and uniformly small boundary.

For a periodic a of period p this rare-visit argument is invalid: ocap({a})=1/p.
Use instead the repeated-block part of Lin95 Lemma 4.2.
First take an SBP neighborhood W of a whose closure excludes b, and set

\[
U_1=\bigcap_{i=0}^{N}T^{-pi}W.
\]

Then a is in U_1, b is outside its closure, and its boundary is uniformly small because it is contained in finitely many translates of boundary W.
Along each residue class of times modulo p, a membership bit for U_1 is the conjunction of N+1 consecutive membership bits for W.
Two runs of ones in this conjunction sequence are separated by at least N+1 zeros.
Consequently, in a block of length N each residue-class sequence has at most one run of ones and at most (N+2)^2 possible words.
Thus h(U_1)<=2 log(N+2)/N, which tends to zero.
The harmless larger count avoids relying on the endpoint convention of the printed N^2 estimate.
This completes the initial step for every a, whether b is periodic or not.

### 3. Boundary refinements with a summable entropy budget

Build a countable family A={U_1,U_2,...} of open sets, each with uniformly small boundary, such that sum_i h(U_i)<epsilon.
For every U in A and every neighborhood O of its boundary, include some V in A with boundary U contained in V contained in O.
This is obtained by adding finitely many refinements at each stage and assigning a summable budget to the stages and their finitely many sets, as in Lin95 Section 4.3.
The first set retains a in U_1 and b outside closure U_1.
Saturate the family by all integer translates when defining the equivalence relation; those translates require no new coding-entropy payments.

### 4. A genuine continuous quotient

Define x~y when 1_U(T^j x)=1_U(T^j y) for every U in A and every integer j.
This is a T-invariant equivalence relation.
To check closedness, suppose x and y are distinguished by U, with x in U and y outside U.
If y is outside closure U, their distinction persists on a product of open neighborhoods.
If y lies on boundary U, a sufficiently narrow boundary refinement V contains y and has closure avoiding x; the same robust distinction is now supplied by V.
The complement of the relation is therefore open in X times X.

A closed equivalence relation on a compact metrizable space gives a compact metrizable Hausdorff quotient Y=X/~ with its quotient topology.
The quotient map pi is continuous and onto, and T descends to a homeomorphism S because the relation is invariant under T and T^{-1}.
The selected a,b remain distinct in Y.

Lin95 author pp.16-17 writes a distance between quotient points as the Hausdorff distance between their fibers.
That distance need not induce the quotient topology and must not be used to justify continuity.
Lin99 p.257 explicitly identifies the corresponding error in the published Lin95 p.248 and says it is unused elsewhere.
Use any compatible metric for the actual compact quotient instead.
The remaining argument requires only that topology and continuity of pi, not the displayed Hausdorff formula.

### 5. The entropy comparison has the correct direction

Let Z be the closure of the simultaneous binary coding image inside the product of the S_{U_i}.
Although the coding X to Z may be discontinuous, there is a continuous onto equivariant map Z to Y.
For a limiting code, intersect the closed coding constraints: a zero coordinate gives X minus U, and a one coordinate gives closure U.
Finite intersections are nonempty by the definition of Z, and compactness gives a nonempty full intersection.
Any two points in this intersection have the same image in Y: otherwise the robust separating set from the previous step contradicts their common limiting code.
Compactness also shows that images of the finite coding intersections have diameter tending uniformly to zero.
This is Lin95 Proposition 4.5 and supplies continuity of Z to Y.

It follows that

\[
h_{\rm top}(Y)\le h_{\rm top}(Z)
\le h_{\rm top}\left(\prod_i\mathcal S_{U_i}\right)
=\sum_i h(U_i)<\varepsilon.
\]

The entropy of the countable compact product is the supremum of the finite-product entropies.
The proof uses monotonicity and product/join upper bounds, not an entropy addition formula for independent indispensable layers of X.

## Consequences and quantifier limits

If h_top(X)>0, SBP does give some factors of arbitrarily small strictly positive entropy, although positivity is not part of the selected-pair conclusion.
For fixed epsilon, choose a countable point-separating family of factors of entropy below epsilon using second countability of X times X minus its diagonal.
If all members had zero entropy, their countable product and its subsystem homeomorphic to X would have zero entropy, a contradiction.

Lin95 Lemma 4.9 and the proof of Theorem 4.10 give the stronger interpolation mechanism, also described in Lin99's introduction on p.228.
Starting with a factor Y_0 and a target r strictly between h_top(Y_0) and h_top(X), adjoin small-entropy point-separating factors until the joined entropy first crosses r, and retain the join immediately before that crossing.
Repeat with decreasing error budgets and use continuity of entropy under the resulting countable joins.
The limiting factor has entropy r and still maps onto Y_0.
The printed Lin95 theorem assumes finite dimension, which its earlier theorem uses to obtain point separation; the interpolation argument itself needs only that separation property and therefore applies under SBP via Theorem 6.7.
The [Lin95 account](../Lin95/readme.md#entropy-interpolation) records the target/error notation correction in the inspected author version.

Pairwise separation with arbitrarily small entropy does not give one injective factor with arbitrarily small entropy.
Nor can one assign a summable budget to a previously selected countable family and assume that the replacement factors still separate all points.
The neighborhoods they distinguish can shrink as the budget shrinks, and the required number and complexity of observations are not controlled.
This is the missing quantitative uniformity, rather than a contradiction with entropy monotonicity.

<a id="algebraic-category-boundary"></a>
## Applicability to G0001 and genuine quotient layers

This is a comparison with the [existing S_G1 question](../../../strategies/Yin_S_G0001.md#real-quotient-entropy-dispersion-2026-10-16), not a new entropy-gap result or a change to that strategy's selected disposition.
The equivalence relation above need not be translation-invariant when X happens to be an abelian group.
There is therefore no reason for Y to be a compact abelian quotient, for pi to be a homomorphism, or for its entropy to come from an integer/rational linear flow.
Theorems about general continuous factors cannot simply be inserted into the algebraic Addition Theorem.

The direction of Pontryagin duality also matters.
For an invariant subgroup V of a discrete abelian G, exactness gives

\[
0\longrightarrow\widehat{G/V}=V^\perp
\longrightarrow\widehat G\longrightarrow\widehat V
\longrightarrow0.
\]

Thus V corresponds to a factor of the compact dual, whereas G/V corresponds to that factor map's kernel subgroup.
Under an applicable Bridge Theorem, the finite-capture target h_alg(G/V(phi,F))=0 asks for zero entropy in this kernel, after a factor generated by finitely many characters has retained the entropy.
The Lin99 construction bounds the image entropy instead.
Even if its factor were algebraic, small image entropy would not establish the required zero residual kernel entropy.
For numerical identification when G is countable and the relevant induced flows are automorphisms, the standard Bridge Theorem is stated in DGB16 Theorem 1.8(b), printed p.617 (PDF p.6); that statement was reread, but its original Peters proof was not audited here.
For a merely forward-invariant V, the induced quotient map need not be an automorphism even when phi is one, so that restricted formulation cannot be applied silently.
DGB16's following paragraph reports the general endomorphism bridge from DGB12; its existing original-source access limitation is unchanged, and no new original-proof audit or project adoption is asserted here.
The exact-sequence direction itself does not require that entropy theorem.
The original G0001 contract also allows arbitrary endomorphisms, whereas Lin99 starts with a homeomorphism; that domain difference must be respected in any proposed transfer.

The standard two-sided binary full shift is a useful calibration.
It has SBP because it is zero-dimensional, and Lin95's finite-dimensional conclusion supplies factors with entropy anywhere in (0,log 2).
On its discrete dual direct-sum binary shift, F={0,e_0} has trajectory cardinality 2^n and attains the total algebraic entropy log 2.
Thus arbitrarily small continuous factors coexist with finite-set entropy attainment in the same standard model.
This is an elementary use of the existing Bernoulli-shift normalization, not a proposed counterexample to G0001.

## Strategy implications for a future authorized round

The useful transferable mechanism is to budget all refinements and to verify a genuine quotient before using entropy inequalities.
The nontransferable freedom is the use of arbitrary open sets and continuous observations without an arithmetic, frequency, degree or regularity budget.
SW91's construction even emphasizes that its Cantor-type continuous observation is generally not Lipschitz.

For [C155's direct logarithmic branch](../../../strategies/Yin_S_G0001.md#c155-next-round-strategy-2026-10-16), the relevant analogy is to isolate expensive regions and control their total contribution uniformly.
Small Haar measure of a bad set is insufficient: the empirical original-conjugate measure and the size of the logarithm on that set also matter.
All radial and regularization costs remain separate obligations.
For example, a future argument might compare a circle test q_P=log Q_P, with an explicit regularization if needed, with the conjugate-angle measure nu_P, prove q_P<=log 2-eta off a declared set E_P, and prove

\[
\int_{E_P}(q_P-(\log2-\eta))_+\,d\nu_P\le\eta/2.
\]

Such a bound would control the nu_P average, but comparison to the actual original-root average would still need its own paid error tending to zero.
The finite conjugate-angle measure has not been shown to be an invariant measure of any system to which these SBP estimates apply.
This is a proposed diagnostic shape, not an estimate established by SBP or computed here.

For the value-preserving branch, B_tilde=B_3+P R must still preserve the prescribed value at every original conjugate.
Lin99 supplies no mechanism producing such a representative in a width bounded by a fixed multiple of d.
Its arbitrarily many boundary refinements have no established counterpart inside the fixed 2d coefficient window.
The energy-four screen remains a necessary test for the strict supremum target, with its original continuation and stopping criteria unchanged.

A useful structural attempt must first exhibit a closed invariant subgroup or a translation-invariant equivalence relation, or prove a quantitative arithmetic return from a nonlinear observable.
It must then supply a new uniform bound beyond merely assuming small positive quotient entropies.
If it only reconstructs small continuous factors, changes category, or uses an unpriced observation/window complexity, it has not advanced the genuine-quotient question.
The current direct-logarithm and value-preserving branches remain appropriate parallel future candidates; this reading supplies no reason to restart broad scans or to execute their pending tests.

## Retained foundations and inspection limits

The standard compact Hausdorff quotient theorem, metrizability of a closed quotient of a compact metric space, topological-entropy monotonicity, finite-product additivity and countable-product/inverse-limit continuity are retained foundations.
The concrete countable-join continuity proof in Lin95 Lemma 4.9 was checked with component metrics bounded by one.
Pontryagin exactness and the already retained algebraic-entropy interfaces are used only at their stated comparison scopes.
No proof of the entire Lin95 finite-dimensional small-boundary theorem, Lin99 mean-dimension/embedding theory, or SW91 transversality and Anosov theory is claimed.
The Lin95 author version has not been compared passage by passage with its published edition.
The explicit correction in Lin99 p.257 was considered; no claim of an exhaustive errata search is made.

No C155 matrix, energy, logarithmic diagnostic or native computation was executed, and no new project Claim was adopted by this source check.
