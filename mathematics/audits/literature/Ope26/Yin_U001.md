---
author: Yin
---

<a id="ope26-u001"></a>
# Ope26-U001: the characteristic-two scalar direct-finiteness counterexample

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26, [retained PDF](../../../literature/pdf/Ope26a.pdf), OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, September 23, 2026; [fixed source commit](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026), `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

Passages: Theorem 1.1, printed/PDF p.1; complete main-theorem proof in Sections 2--6, pp.4--24. Additional checked transfer: Sections 7.1--7.2, pp.25--26. Excluded additional conclusion: Section 7.3, p.27. The PDF has 28 pages and its printed and PDF page numbers agree.

Inspection: 2026-10-08, human record author Yin. A separately assigned AI reviewer read and checked the full main-theorem chain in the fixed-commit TeX and checked the PDF locators. The coordinating AI reviewer independently checked the critical algebraic and geometric arguments, reconciled the findings, and inspected rendered PDF pp.1, 20 and 24. This is a separately organized mathematical proof review, with the published least-prime theorem retained at its checked applicability scope. The enormous finite prescription was not executed.


## Statement, conventions, and supported scope

Theorem 1.1 asserts that there exist a finite field \(K\) of characteristic two, a finitely presented group \(G\) containing an element of odd prime order, and scalar finite sums \(a,b\in K[G]\) such that

\[
ab=1,\qquad ba\ne1.
\]

Here \(K[G]\) is the ordinary group algebra of finitely supported functions, with convolution induced by the group law.
The theorem does not assert that \(K=\mathbb F_2\), nor that \(G\) is torsion-free.
Its scalar conclusion is stronger than merely finding square matrices with a one-sided inverse defect.
This exact scalar pair is the input needed by the group-ring determinant manuscript.

The review covers the theorem and its complete internal proof chain through Sections 2--6.
It also checks the elementary configuration-space transfer in Sections 7.1--7.2.
The type-\(F_\infty\) conclusion in Section 7.3 invokes a separate new universal-group embedding manuscript and is excluded.
Nonsoficity additionally uses the established sofic stable-finiteness theorem; that external theorem's proof was not re-audited here.
This unit contains no assessment of the Lean source and makes no formal-verification claim.

No original proof-generation dialogue or unpublished author explanation was supplied.
The reviewers had the preceding discussion of the determinant manuscript.
The separately assigned reviewer formed initial findings from the companion's argument before comparing the coordinating reviewer's independently obtained conclusions on the geometric and algebraic core.
Agreement is corroboration; the checks supporting the assessment are recorded below.

**Reading state: Audited within scope.**
No concrete proof defect or unresolved mathematical interface was found in the inspected chain to Theorem 1.1.
The accepted published least-prime theorem is identified in [Xyl11-U001](../Xyl11/Yin_U001.md#xyl11-u001); its original proof was not re-audited.
This assessment concerns the mathematical argument in the specified artifact.
It does not assert that a concrete numerical witness has been computed.

## Polynomial pairings and the size interface

Locators: Section 2, pp.4--6; Lemmas 2.1 and 2.2; Proposition 2.3.

Put \(q=2^h\), \(d_0=(q-2)/2\), and let \(S\) be the index simplex in \(Q^n\), where \(|Q|=q\).
The Newton polynomials indexed by the same lower set give an invertible triangular evaluation matrix: for two tuples in lexicographic order, the first differing coordinate forces the appropriate evaluation to vanish; each diagonal product is nonzero because the enumerated field elements are distinct.
Since \(d_0<q\), there is no omitted coordinate restriction in the count \(\binom{d_0+n}{n}\).

For every deleted point \(o\), the interpolant \(f_o\) is the coordinate indicator on \(S\).
Each product \(f_of_{o'}\) has total degree at most \(q-2\).
Its restriction to any full affine \(Q\)-line therefore has zero sum, by the finite-field power-sum identity.
Partitioning into parallel lines gives zero total sum on \(Q^n\).
At the deleted points the evaluation columns are distinct coordinate vectors.
Consequently, after deleting the hole set \(O\) and putting \(V=Q^n\setminus O\),

\[
\sum_{v\in V}x_vx_v^{\mathsf T}=-I_m,
\qquad
\sum_{v\in f}x_vx_v^{\mathsf T}=0\quad(f\in\mathcal F),
\qquad m=|O|.
\]

The transpose is ordinary transpose, with no involution.
These are finite algebraic equalities; no analytic convergence or positivity is used.

The hole bounds imply precisely the packing range.
Write \(D=\ell+1\), \(N=q^n\), and \(t=|V|\).
The upper bound \(m\le7N/D^2\) is strictly below \(N/2\), since \(D\ge4\).
The lower bound gives

\[
\frac{t}{m}=\frac Nm-1
\le\frac{D^2}{2}-1
\le(D-1)^2=\ell^2.
\]

Thus \(0<m<t\le m\ell^2\).
The parity compatibility is also correct: \(D\) vanishes in characteristic two, so summing the line identities does not force the nonzero total point pairing to vanish.

## The local groups embed

Locators: Section 3.1, Lemma 3.2, pp.7--9.

Each local additive group \(\mathbb F_\ell^2\) assigns its \(\ell+1\) one-dimensional subgroups to the incident hyperedges.
Every nonzero local vector has a unique one-line representative.
The presentation using all local zero-sum signed words is equivalent to the finite multiplication-table presentation with relators of length at most three.
This establishes finite presentation without assuming any local embedding in advance.

The injection argument was checked at its planar-graph interface.
A hypothetical one-letter null word produces a connected planar bipartite weighted graph with zero balances at all black and ordinary white vertices and a nonzero balance at one exceptional white vertex.
Both relator insertions and deletions preserve the stated signs; the initial token accounts for the sole exception.
The use of insertions and deletions is justified by the presentation congruence, including formal inverse-pair insertions.

In a graph minimal first in vertices and then in edges, parallel edges can be combined using the additive edge group.
Consecutive neighbors of the same label can be merged along an arc in the intervening empty sector.
The merge is legitimate for either color, retains every relevant incidence map, adds compatible balances, and preserves the exceptional nonzero balance.
If cancellation disconnects the graph, retaining the exceptional component causes no new nonzero balances.

The resulting degree bounds are: every black degree is at least three, every ordinary white degree is at least two, and the exceptional white degree is at least one.
The degree-two black obstruction uses the distinct local one-dimensional subspaces, not an unproved intersection assertion about their global images.
Facial boundary walks have no immediate backtracking in the incidence graph except possibly at the exceptional degree-one vertex.
Bridges are allowed and counted by edge sides; they do not invalidate this observation.
Every other facial walk therefore contains a cycle of length at least twelve.

With \(E\) edges, the bounds are

\[
n_{\mathrm b}\le E/3,
\qquad n_{\mathrm w}\le(E+1)/2,
\qquad n_{\mathrm f}\le E/6+1.
\]

They contradict \(n_{\mathrm b}+n_{\mathrm w}+n_{\mathrm f}=E+2\).
The exceptional-face allowance is sufficient even if its length is ignored entirely.
This proves that every local generator is nontrivial and hence that the local \(\mathbb F_\ell^2\) and \(\mathbb F_\ell\) subgroups embed.
No stronger statement about intersections of unrelated local groups is used downstream.

## Rectangular identity, HNN twists, and the reverse defect

Locators: Sections 4.1--4.4, pp.10--13.

The subgroup average

\[
P_v=\ell^{-2}\sum_{u\in K_v}u
\]

is a valid idempotent because \(\ell\) is odd.
The decomposition of the nonidentity elements of \(K_v\) among its local lines is used inside that embedded finite group.
Let \(X\) be the matrix of columns \(x_v\) and \(P=\operatorname{diag}(P_v)\).
Reordering the finite sums against the vanishing line pairings gives

\[
U=-\ell^2XP,\qquad T=PX^{\mathsf T},
\qquad UT=I_m,\quad UP=U,\quad PT=T.
\]

For \(H=N\times C_\ell\), the specified maps between \(K_v\times C_\ell\) and \(K_*\times C_\ell\) are actual group isomorphisms.
The paper supplies a faithful permutation representation of the base group in the multiple HNN extension: its regular action decomposes into the same number of orbits for the two finite associated subgroups, and each stable letter can be realized by an orbit-pairing bijection.
No compatibility relation between distinct stable letters is assumed.
This validates the subgroup-algebra injection required later.
Centrality of the cyclic generator \(z\) is retained because every stable letter conjugates \(z\) to itself.

The central character idempotent \(e\) and orthogonal idempotents \(Q_\alpha\) were checked with the paper's character signs.
Conjugation gives

\[
\tau_veP_v\tau_v^{-1}=eQ_{\alpha_v}.
\]

The inequality \(t\le m\ell^2\) permits distinct slot-character pairs.
Consequently the packing matrices satisfy \(J_0C=eP\), including the off-diagonal entries for equal slots.
Adding \((1-e)I_m\) to the two square factors annihilates all cross terms and gives \(a_{\mathrm{mat}}b_{\mathrm{mat}}=I_m\).

For \(\Delta=b_{\mathrm{mat}}a_{\mathrm{mat}}-I_m\), the crucial identity is

\[
J_0\Delta C=e(TU-P).
\]

The right side belongs to the embedded \(K[H]\), even though the outer factors need not.
The homomorphism \(\varepsilon(nz^r)=\zeta^r\) is applied only to \(K[H]\).
It sends \(e\) and every \(P_v\) to one and gives

\[
\varepsilon\bigl(e(TU-P)\bigr)=X^{\mathsf T}X-I_t.
\]

This matrix is nonzero because \(\operatorname{rank}(X)\le m<t\).
Thus the argument never extends \(\varepsilon\) illegally across the HNN relations.
Preservation of the nonzero right side under the subgroup-algebra embedding proves \(\Delta\ne0\).

## The matrix defect becomes a scalar defect

Locators: Sections 4.5--4.6, pp.13--14.

The auxiliary finite group is \(F=(C_\ell)^m\rtimes S_m\).
Averaging over its odd-order base gives nonzero pairwise orthogonal coordinate-character idempotents.
Permuting coordinates produces elements \(p_{ij}\) satisfying

\[
p_{ij}p_{kr}=\delta_{jk}p_{ir}.
\]

Multiplying a linear relation by the diagonal idempotents isolates each coefficient, proving their linear independence.
No division by \(|S_m|\) occurs; its potentially even order in characteristic two causes no difficulty.

The tensor-product group basis proves injectivity of the map from \(\operatorname{Mat}_m(K[L])\) into \(K[L\times F]\).
The corner identity \(f_{\mathrm{blk}}\) need not be the identity of the whole group ring and need not be central there: it acts as a two-sided identity on this image, which is exactly what is required.
Adding \(1-f_{\mathrm{blk}}\) to both factors produces scalar \(a_{\mathrm{out}}b_{\mathrm{out}}=1\), while \(b_{\mathrm{out}}a_{\mathrm{out}}-1\) is the injective image of \(\Delta\).
This resolves the stable-finiteness versus direct-finiteness interface without relying on an invalid general implication for arbitrary rings.

Finite presentation is tracked through \(N\), the direct product with \(C_\ell\), the finitely many HNN relations, and the finite group factor.
The embedded local groups retain \(\ell\)-torsion.
All group-algebra sums are finite; deciding equality between every displayed pair of group words is unnecessary for defining them or for the algebraic nonvanishing certificate.

## The complete geometric existence input

Locators: Section 5, Theorem 5.1 and Lemmas 5.2--5.9, pp.14--22.

### Parameters and uniformity

The least prime \(\ell\equiv-1\pmod {q^{100}}\) exists and satisfies \(\ell\le Cq^{100L}\) by the uniform least-prime theorem.
The substitution is legitimate because \(\gcd(q^{100}-1,q^{100})=1\).
Thus \(D=\ell+1\) is divisible by \(q^{100}\), \(s=\lfloor\log_qD\rfloor\ge100\), and \(s\) has a bound independent of \(h\).
Therefore \(b=s+20\) and \(n=10b\) are uniformly bounded as \(h\) grows.
In particular, constants depending on \(n\), including the lower bound for \(|S|/q^n\), may be chosen uniformly.
The argument does not incorrectly keep an unbounded dimension fixed during an asymptotic estimate.

The accepted published input is [Xyl11-U001](../Xyl11/Yin_U001.md#xyl11-u001), covering the statement of Xylouris's Theorem 1.1 and the substitution above.
It gives the stronger exponent \(L=5.18\).
Its statement and application were checked against the publisher PDF; its analytic-number-theoretic proof was not re-audited.
Any classical absolute \(L\) suffices for this construction.

### Independent direction spaces

There are \(D+D/q\) spaces to choose and exactly \(q^b\) extension-field parameters available, with \(D+D/q<q^b\).
The Vandermonde construction in ten extension-field coordinates gives direct sums for any at most ten distinct spaces in the list.
Choosing a two-dimensional \(W_r\) or a \((b-1)\)-dimensional \(E_j\) inside its assigned extension-field line preserves this directness.
Within a bundle, \(d_j\) and \(e_r\) are distinct directions in the same plane; across bundles their planes are independent.
These facts prove every stated pairwise intersection without treating all \(q\) selected directions in one plane as independent.

### Hole selection

Let \(M=N/D^2\), and independently select each point of \(S\) with probability \(\theta=5M/|S|\).
The lower-set count gives \(\theta=O(D^{-2})\), and \(M>q^{8s+198}\).
Concentration of the selected set's size around \(5M\) follows from the elementary variance bound.

The occupancy union bound has exponent

\[
2s+2+n+100(b+2-2s)=2402-88s<0.
\]

Using 100-subsets to bound the event of more than 100 selected points is a valid upper bound.
The subsequent marked-point removal has expected fraction \(O(q/D+q^8/D^4)\), which tends to zero.
The rectangle count uses distinct witness tuples; this distinction is necessary for the \(\theta^4\) factor and is explicitly present.
Deleting marked points preserves the occupancy bound and leaves enough holes.
Adjacent replacement-side planes intersect only at the corner, while opposite-side planes are disjoint; hence a rectangle made from replacement lines would indeed yield four distinct hole witnesses.
This validates the interface from the hole condition to excluding all-replacement rectangles.

### Classification of all relevant short polygons

Every step uses at most two of the \(W\) and \(E\) spaces, so at most ten are involved in a polygon of three, four, or five steps.
A generic label must occur at least twice by vanishing of its independent \(E\)-component; cyclic nonadjacency permits at most twice.
Thus there are either one or two generic labels.
With one label, the only possibility is an alternating generic/replacement rectangle.
With two labels and four steps, it is an alternating generic/generic rectangle.
With two labels and five steps, the remaining replacement direction forces both generic labels into that bundle.
The two generic directions in its plane are distinct and together determine the exceptional cancellation.
These are all cases, including sequences with repeated vertices.

For each generic label, the two occurrences have exactly one intervening step in one cyclic direction.
That step lies outside the corresponding \(U_j\).
Hence the occurrences use distinct \(U_j\)-cosets and distinct independent random variables \(P_{j,C}\).
Distinct labels have separately chosen variables as well.
Thus the polygon event probabilities are \(p_*^2\) or \(p_*^4\), not an unjustified product of dependent inclusion events.

### Event counts and the local lemma

For a fixed random variable, the hole-pair, generic rectangle, mixed rectangle, and pentagon contributions are bounded respectively by

\[
10^4p_*,\qquad
O(Dq^{3b}p_*^4),\qquad
O((D+q^3)p_*^2),\qquad
O(q^{3b+2}p_*^4).
\]

The mixed-rectangle bound uses the occupancy condition to replace a count over all points of a coset by at most \(100q\) candidate endpoints in its own bundle and at most 100 in each other bundle.
This is the crucial saving: both endpoints of the initial generic step belong to the corresponding union of replacement planes.
The pentagon bound correctly uses only \(q\) choices for the other generic label because the classification confines it to one bundle.

Substituting \(p_*\le2q^{3-b}\), \(b=s+20\), and \(D<q^{s+1}\) yields the exponents

\[
-s-17,\quad -7,\quad -s-33,\quad -2s-31,\quad -s-6.
\]

Thus the total is uniformly \(O(q^{-7})\).
Each event uses at most four independent variables.
The supplied asymmetric local-lemma proof sets \(x_A=2\Pr(A)\), obtains neighbor-weight sum at most \(1/2\), and verifies the product condition.
Its conditional-probability induction also supplies positivity of every conditioning event.
The existence conclusion follows for sufficiently large \(q\); no resampling execution is needed.

### Partitions, trades, and complete girth verification

The three-dimensional slab partition was checked directly.
With \(P\) a two-dimensional field-extension space and \(J\) multiplication by an element outside \(Q\), the vectors \(x,Jx\) are independent whenever \(x\ne0\).
Therefore each point off the selected axis corresponds to a unique linear functional \(\gamma\) satisfying \(\gamma(x)=1\) and the prescribed value of \(\gamma(Jx)\).
The displayed lifted lines are genuine affine lines and partition exactly the off-axis points.
Their directions have nonzero \(E\)-components.

The trade removes \(q\) axes through a hole and adds \(q-1\) parallel lines in the same plane.
Every non-hole point has zero net degree change.
Hole separation prevents duplicate removals, and the direction-space intersections prevent coincident lines of distinct labels.
Each label remains a disjoint family.
All lines through a hole have been removed, and replacement lines avoid all holes, giving exact degree \(D\) on the punctured space.

A four-cycle in the incidence graph is impossible because distinct affine lines intersect in at most one point.
Any cycle of length six, eight, or ten yields one of the enumerated three-, four-, or five-step polygons, with distinct consecutive labels.
If it contains a generic step, its slab event was excluded.
If not, independent replacement directions force the rectangle already excluded by the hole selection.
This proves girth at least twelve, rather than only excluding selected examples of short cycles.

## Termination and complete assembly

Locators: Section 6, pp.22--24.

For each fixed \(h\), the prime search terminates by the accepted least-prime theorem.
The chosen field of degree \(h(\ell-1)\) over \(\mathbb F_2\) contains both \(Q=\mathbb F_{2^h}\) and a primitive \(\ell\)-th root: \(h\) divides \(h(\ell-1)\), and \(\ell\mid2^{\ell-1}-1\).
The subsequent search ranges over finite sets and tests finite incidence data.
The geometric theorem applies uniformly in the induced field enumeration, so some \(h\) succeeds.
An effective numerical threshold for all successful \(h\) is not required to prove termination of this exhaustive search.

The output satisfies Proposition 2.3 and every hypothesis of Theorem 3.1, including the same prime \(\ell\), characteristic two, the root of unity, both size inequalities, all matrix pairings, and incidence girth.
Every later choice is finite and specified.
This yields the scalar pair required by the determinant paper without invoking the determinant theorem.
The determinant manuscript is mentioned in the introduction as a downstream application, not a logical premise.
The two papers therefore have no circular dependency at this interface.

The optional type-\(F_\infty\) overgroup theorem is not a premise of Theorem 1.1.
It is unnecessary even for finite generation, which already follows from the finite presentation proved here.

## Additional checked transfer

Locators: Sections 7.1--7.2, pp.25--26.

For

\[
(T_cx)(g)=\sum_uc_ux(gu),
\]

composition is \(T_cT_d=T_{cd}\) in the stated right-neighbor convention.
The sums are finite even for arbitrary configurations.
Testing a point indicator reads off a coefficient and proves faithfulness.
From \(ab=1\), one obtains \(T_aT_b=I\), so \(T_b\) is injective.
Its image is exactly the fixed space of \(T_{ba}\).
A nonzero coefficient of \(ba-1\) excludes the corresponding point indicator from that image.
This is a valid finite-alphabet cellular automaton because \(K\) is finite; it does not confuse all configurations with finitely supported functions.

## Dependencies and limits

The only substantial external existence input in the construction of Theorem 1.1 is the uniform least-prime theorem accepted in [Xyl11-U001](../Xyl11/Yin_U001.md#xyl11-u001).
Standard finite-field algebra is used with the precise extension degrees and divisibility conditions checked above.
The interpolation, local-lemma estimate, subgroup embedding, finite matrix block, and all necessary group-ring identities have supplied internal proofs, which were inspected rather than replaced by their historical citations.

The optional type-\(F_\infty\) extension in Section 7.3, p.27, has an additional new companion dependency.
Its embedding assertion is outside this verdict.
The historical survey's bibliographic completeness, the full proofs of established background results, execution of the finite witness search, and normalization of all displayed group words are also outside this inspection.
This unit does not inspect the Lean source.
These limits do not leave an unnamed premise in the checked proof of Theorem 1.1.

The determinant manuscript's characteristic-two scalar-pair input has been traced through its full companion argument, rather than accepted from an abstract or treated as an already established external theorem.
No unresolved mathematical dependency was identified at that interface after retaining the specified least-prime input.
This assessment does not include the optional type-\(F_\infty\) conclusion.
