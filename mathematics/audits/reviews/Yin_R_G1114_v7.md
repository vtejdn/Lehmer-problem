---
author: Yin
---

# Independent review of the canonical Coxeter cover over arbitrarily many E8 blocks

## Review arrangement and exact scope

The review act is dated 2026-11-10T02:41, with Yin as the human record author.
A separately organized reviewer inspected the complete fixed C886 v1 statement and argument without participating in its proof development or receiving the main thread's derivation dialogue.
The final text explicitly requires \(1<M(P_{A_j})\to1\) in the sequence consequence and applies \(s_{\theta_j}\) before \(s_{e-\theta_j}\) in equation (6).
Those actual sentences and the completed source-interface paragraph were read before this finding.
No substantive proof repair or new construction was supplied.

The review covers every finite \(r\ge1\), all integer transvection parameters, every specified finite generator word, the integral canonical quotient, the word's ordered permutation product, complete spectral and Mahler transfer, and all stated consequences and limitations.
Earlier independent findings are reused only for the unchanged finite E8 data, transvection identities and negative-index argument; their applications here were checked directly.
The reviewer read both new E8 source units and source notes.
The reviewer directly text-compared Section 2 and Lemma 1 in the [WvL21 original](../../literature/pdf/WvL21.pdf) on printed page 1970, one-based PDF page 6; the cited Humphreys proofs were not audited.
The reviewer also directly text-compared Remark 2.5, the explicit edge list and the simple-root basis in the [JKZ08 author original](../../literature/pdf/JKZ08--author.pdf) on author/PDF pages 6--7; its cited foundational proofs were not audited.
The accepted McM02 theorem retains its existing statement and applicability depth.
No foundational root-system proof or complete McM02 proof was newly audited, and no numerical test, root calculation, word search or new computation program was run.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [C886 v1 statement](../../claims/Yin_C_G0886_v1.md#statement) | Every stated quantifier, complete-measure equality and bound, fixed-D subfamilies, the r=3 consequence and strict nonneutral sequence condition. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Complete argument and inputs](../../claims/Yin_C_G0886_v1.md#argument) | The complete assembled proof and the actual finite-root and canonical-Coxeter interfaces, at their stated source depths. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Positive components](../../claims/Yin_C_G0886_v1.md#positive-blocks) | Exact E8 Gram and theta, connected root components, integral block spans and the full wreath-product decomposition. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Canonical star](../../claims/Yin_C_G0886_v1.md#canonical-star) | All pairings, canonical exponents, integral surjection, entire primitive radical, quotient, signatures and full characteristic-polynomial identity for every r. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Generator coverage](../../claims/Yin_C_G0886_v1.md#generator-coverage) | Root-reflection product, positive Weyl words, all integer parameter sums and inverses, and the sign in opposite-cusp conjugation. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Permutations and gap](../../claims/Yin_C_G0886_v1.md#permutations-and-gap) | Specified-word permutation, normalization, d-th power, full radical and quotient spectrum, negative index one, complete Mahler cost and every consequence. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Coverage limits](../../claims/Yin_C_G0886_v1.md#limits) | Distinction from the ambient reflection group and other positive lattices/cusps; no unrestricted shrinking construction or Task completion. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Accepted canonical Coxeter theorem](../literature/McM02/Yin_U002.md#canonical-coxeter-gap-input) | Absolute spectral threshold for every word in the actual finite-generator canonical representation, including degenerate forms; original proof not newly audited. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Full E8 group and root orbit](../literature/WvL21/Yin_U001.md#full-isometry-and-transitivity) | Full positive lattice isometry group equals the Weyl group, and transitivity on all norm-two roots, at the established statement scope. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [E8 simple generators and Gram](../literature/JKZ08/Yin_U001.md#simple-generators-and-gram) | Eight simple-root reflections, actual basis permutation, lattice span and norm-two convention. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Finite E8 model finding](Yin_R_G1114_v6.md#coxeter-two-transvection-model-review) | Reuse of the verified positive integral E8 block and norm-two vector; the finite model does not establish the arbitrary-r result. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Two-block calibration](../../computations/programs/Yin_J_G0158/coxeter_model.md#two-transvection-model) | Consistency of the known two-block realization with this cover, without extrapolating its finite computation. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Negative-index bound](../../ledger/Yin_L_G0462_v13.md#negative-index-bound) | Generalized expanding eigenspaces with all algebraic multiplicities, reciprocal spectrum and the exact index-one complete-measure specialization. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Integral transvection formula](../../ledger/Yin_L_G0462_v13.md#integer-generators) | Pairing preservation, integrality and inverse for the actual positive even lattice; source attribution is unchanged. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Addition and covariance](../../ledger/Yin_L_G0462_v14.md#short-word-reduction) | The unrestricted parameter addition, inverse and positive-isometry covariance identities only; no use of its short-word bound. |
| [Whole canonical-cover finding](#e8-block-canonical-cover-review) | [Leech normalization boundary](../literature/Bor96/Yin_U001.md#canonical-normalization-boundary) | The recorded distinction between actual chamber pairings below minus two and the different explicit canonical star used here. |

<a id="e8-block-canonical-cover-review"></a>
## Finding

No unresolved mathematical or source-applicability gap was found in the final inspected C886 v1 statement and complete argument.
For every specified word, the proof establishes
\[
M(P_A)=\rho(A),\qquad
M(P_A)=1\quad\text{or}\quad
M(P_A)\ge\lambda_{\rm L}^{\,1/\operatorname{ord}(\pi)}.
\]
The bound depends only on the order of the ordered component permutation assigned to that word.
It is uniform over the stated subfamilies with that order bounded, with no hidden bound on rank, word length, coordinates or norms.
The decisive checks below reference the fixed proof instead of duplicating it.

### Positive blocks and exact canonical normalization

The source statements concern the full positive lattice isometry group, including determinant-minus-one reflections.
They do not restrict to a special orthogonal or cone subgroup.
The JKZ08 basis, reordered as \((\alpha_1,\alpha_3,\alpha_4,\alpha_5,\alpha_6,\alpha_7,\alpha_8,\alpha_2)\), has precisely the claim's chain and branch Gram matrix.
Its stated integral lattice basis and norm-two convention identify the actual lattice without a rescaling or index change.
The WvL21 full-group and transitivity statements therefore apply to this exact block.

The finite positive minors are already verified in R1114 v6.
Directly checking the eight rows of \(K\theta\) gives the seventh unit vector; since \(\theta_7=2\), this also verifies \(\theta^2=2\).
Thus every pair involving the new \(b_j\) has the sign and normalization asserted in the claim.

For the positive direct sum, an integral nonzero block has even norm at least two, so a norm-two vector occupies exactly one block.
The simple roots form a connected pairing graph, and nondegeneracy makes every other root pair nontrivially with at least one simple basis vector.
Consequently the graph's connected components are exactly the \(r\) full block root sets.
An integral isometry permutes them and their integral spans.
After removing that permutation, the accepted full E8 theorem applies separately to each block.
Conversely the block Weyl actions and block permutations are isometries, proving the equality \(O(H_r)=W(E_8)^r\rtimes S_r\).
No orthogonal-sum decomposition theorem is being assumed beyond this argument.

### Entire integral quotient, including r=1

The formula for \(q\) is integrally onto: its images contain the positive basis and the displayed integer combinations giving both \(e\) and \(f\).
The pulled-back norm-two Gram has exactly the E8 edges, the edges \(a_{j,7}-b_j\), and the edges \(b_j-c\).
All other distinct pairings are zero.
This is exactly the canonical geometric form with Coxeter exponents three and two, on a finite set of \(9r+1\) generators for each finite \(r\).
The accepted McM02 theorem allows its degeneracy and supplies a constant independent of the number of generators.

For completeness, write a possible kernel vector as
\[
x=\sum_j u_j+\sum_j\beta_j b_j+\gamma c,
\]
with \(u_j\) in the \(j\)-th eight-dimensional free positive span.
The \(f\)-coordinate of \(q(x)=0\) gives \(\gamma=0\); the \(e\)-coordinate gives \(\sum_j\beta_j=0\); and the positive coordinates give \(u_j=\beta_j\vartheta_j\).
Thus every integer kernel vector is exactly an integer combination of the displayed \(r-1\) differences.
Their elimination leaves the claimed integral quotient basis and proves primitiveness, without a denominator or overlattice argument.
For \(r=1\) the empty kernel sum is zero and the same explicit quotient isomorphism still holds.

The target has inertia \((8r+1,1,0)\), so the pullback has inertia \((8r+1,1,r-1)\).
Every canonical reflection fixes the radical pointwise, and its descent is the reflection in the actual image root because the form is pulled back by \(q\).
The whole characteristic polynomial consequently factors as
\[
\chi_w=(z-1)^{r-1}\chi_{\bar w}.
\]
This follows from the invariant-subspace determinant identity even when Jordan blocks occur.
There is no discarded exterior root or multiplicity.
The quotient isometry has spectral radius at least one, so adjoining these ones preserves both its radius and complete measure.

### Coverage of every integral parameter at both cusps

The accepted simple-root generating theorem realizes every positive block Weyl element through the canonical \(a_{j,i}\) reflections.
In particular the positive reflection \(s_{\theta_j}\) is available.
The explicitly ordered calculation in equation (6) gives
\[
s_{e-\theta_j}s_{\theta_j}x
=x+(e,x)\theta_j-\bigl((\theta_j,x)+(e,x)\bigr)e
=T_{e,\theta_j}x
\]
on the entire lattice, with half-norm one.
Positive Weyl conjugation fixes \(e,f\) and replaces the vector by its Weyl image, so root transitivity gives the transvections for every simple basis vector.

The addition and inverse identities hold for all permitted positive vectors, including nonorthogonal pairs, because the cross term in the squared norm is \(2(u,v)\).
All vectors of \(E_8^r\) have even integral norm.
Integer coefficients of either sign in the simple basis therefore give every \(T_{e,v}\) as a finite canonical word.
The zero vector is the identity case.
There is no bound on those coefficients or on the resulting word length, and none is needed by the Coxeter theorem.

The reflection in \(-e-f\) fixes the positive space and sends \(e,f\) to \(-f,-e\).
Covariance of the formula sends \(T_{e,v}\) to \(T_{f,-v}\), with the negative sign included.
Since the parameter set is closed under negation, this covers the entire other cusp group.
These statements prove coverage of the specified generators; they do not identify the canonical image with the whole indefinite orthogonal group.

### Specified-word permutation and full power cost

A permutation of the positive blocks acts on the canonical free module by the same permutation of all \(a\)-blocks and \(b_j\)'s, fixing \(c\).
It is a genuine finite-order diagram automorphism, normalizes the canonical reflection group, preserves the kernel and induces the required positive isometry fixing \(e,f\).

Choose a lift for each factor of the specified finite word.
Moving the diagram automorphisms to the left using normalization produces \(\widetilde A=\widetilde\pi w\).
The left product is exactly the ordered product in the statement, and no commutativity of the factors is used.
This construction does not require that the permutation be determined by the quotient matrix \(A\), that the quotient action be faithful, or that different word presentations have the same permutation.

For \(d=\operatorname{ord}(\pi)\), the exact diagram permutation satisfies \(\widetilde\pi^d=I\).
Expanding \((\widetilde\pi w)^d\) as a product of conjugates of \(w\) therefore puts it in the canonical reflection group.
Its quotient is \(A^d\), and its entire characteristic polynomial is
\[
\chi_{\widetilde A^d}=(z-1)^{r-1}\chi_{A^d}.
\]
The case \(d=1\), including the empty word and identity permutation, is included.

For any isometry of \(L_r\), inverse powers on the real generalized expanding space tend to zero.
Pairing invariance makes that space totally isotropic, so negative index one bounds its real dimension by one.
This counts algebraic multiplicities and both members of any nonreal pair.
Together with reciprocal spectrum, it proves \(M(P_A)=\rho(A)\) in both the neutral and nonneutral cases, without diagonalizability.
Applying the accepted canonical theorem to the nonneutral \(\widetilde A^d\) now gives \(\rho(A)^d\ge\lambda_{\rm L}\).
Every eigenvalue of \(A^d\) is the corresponding eigenvalue of \(A\) raised to \(d\), with algebraic multiplicity, so the complete logarithmic cost is exactly \(d\,m(P_A)\).
No power is being substituted as a representation preserving the original polynomial or measure.

### All consequences and source limits

If a subfamily admits a presentation with \(d\le D\) for each member, select any such presentation.
The per-word bound gives \(m(P_A)\ge\log(\lambda_{\rm L})/D\) whenever \(M(P_A)>1\).
It requires neither a common word nor a common number of E8 blocks.
For \(r=3\), the permutation orders are precisely one, two and three, so the asserted \(\lambda_{\rm L}^{1/3}\) bound follows for every member of \(\Gamma_3\).

For a sequence with \(1<M(P_{A_j})\to1\), division by its strictly positive logarithm gives
\[
d_j\ge\frac{\log\lambda_{\rm L}}{\log M(P_{A_j})}\longrightarrow\infty.
\]
This lower bound holds for every chosen presentation of every member; neutral sequences are excluded by the final explicit hypothesis.
Growing permutation order alone supplies no small radius, nonneutrality, new irreducible factor or shrinking family.

The source inputs resolve the finite-root and canonical-theorem interfaces at their recorded statement, convention and applicability depths.
Their cited Humphreys, Bourbaki and Adams foundations and McMullen's full geometric/classification proof remain unreviewed here.
The two-block J158 calculation is a compatible calibration only; the arbitrary-r quotient and generator arguments above supply the unbounded coverage.
The Bor96 chamber warning remains valid for its actual pairings and does not change this separate canonical star.

No extension to positive Leech summands, other positive lattices, arbitrary cusps or all isometries of \(L_r\) is proved.
There is no uniform absolute threshold asserted when the specified permutation orders are unbounded.
This finding supports the complete stated C886 result and leaves the [unrestricted G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) unresolved.
