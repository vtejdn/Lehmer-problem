---
author: Yin
---

# Canonical Coxeter covers through neutral integral embeddings

<a id="statement"></a>
## Statements and precise embedding condition

Let \(H\) be a positive definite symmetric integral Gram matrix of rank \(g\ge1\), and put
\[
L=H\oplus U,\qquad e^2=f^2=0,\quad (e,f)=1.
\]
Consider a specified finite word \(A\) in positive integral \(H\)-isometries extended to fix \(e,f\), and the transvections
\[
T_{e,v}(x)=x-(v,x)e+(e,x)v-\tfrac12(v,v)(e,x)e,
\]
with \(T_{f,v}\) obtained by exchanging \(e,f\), for integral parameters of even squared norm.
Suppose there is one integer matrix \(V\) of size \(N\)-by-\(g\) such that
\[
V^{\mathsf T}V=H,                                      \tag{1}
\]
and that for each positive-isometry factor \(R_j\) of this word there is a signed permutation matrix \(S_j\) on \(\mathbb Z^N\) satisfying
\[
S_jV=VR_j.                                             \tag{2}
\]
No primitivity, square matrix or uniform bound on \(N\) is required.
The choices \(S_j\) need not define a homomorphism on the whole positive isometry group.

Let \(P_A(z)=\det(zI-A)\), and let \(\lambda_{\rm L}\) be the Lehmer Salem root specified in [v2](Yin_C_G0886_v2.md#statement).
Then
\[
M(P_A)=\rho(A),\qquad
M(P_A)=1\quad\hbox{or}\quad M(P_A)\ge\lambda_{\rm L},      \tag{3}
\]
and
\[
1<M(P_A)<6/5\quad\Longrightarrow\quad M(P_A)=\lambda_{\rm L}. \tag{4}
\]
Both conclusions are uniform over all the stated ranks, embeddings, positive factors, word lengths and parameter norms.

In particular, (3)--(4) hold for every word over every positive integral lattice admitting an integral orthogonal basis.
In such a basis its Gram matrix is
\[
D=\operatorname{diag}(d_1,\ldots,d_g),\qquad d_i\in\mathbb Z_{>0},           \tag{5}
\]
and all its positive integral isometries and all its even-norm parameters are allowed.
Thus the diagonal entries may be arbitrary and unequal; the scalar-standard result of v2 is included.

The independent [E8-block conclusion of v1](Yin_C_G0886_v1.md#statement) is also retained.
For a specified word over \(E_8^{\oplus r}\oplus U\), let \(d\) be the order of the ordered product of its positive block permutations.
Then
\[
M(P_A)=\rho(A),\qquad
M(P_A)=1\quad\hbox{or}\quad M(P_A)\ge\lambda_{\rm L}^{1/d}. \tag{6}
\]
For \(d\le D_0\) this gives the uniform logarithmic gap \(\log\lambda_{\rm L}/D_0\), with no bound on \(r\), word length or vector norms.
For \(r=3\) the complete-measure bound is \(\lambda_{\rm L}^{1/3}\).
In a positive-to-one sequence, every choice of these presentations has permutation order tending to infinity.
For the E8 presentations with \(d=1\), conclusion (4) holds as well.
No embedding condition (1)--(2) is asserted for general E8-block words, and no presentation-independent block-permutation homomorphism is assumed.

<a id="argument"></a>
## Complete argument and fixed mathematical inputs

The proof combines the explicit full-dimensional canonical representations and exact source comparison written in v2 with the neutral embedding proved here.
The precise fixed argument inputs are [the rank-at-least-two standard basis](Yin_C_G0886_v2.md#standard-rank-two-up), [the rank-one basis](Yin_C_G0886_v2.md#standard-rank-one), [the complete-measure identity](Yin_C_G0886_v2.md#standard-gap), and [the six exact rational evaluations](Yin_C_G0886_v2.md#six-fifths-classification).
These proof sections are actual parts of the present selected argument; no separate prior adoption of the unassessed v2 statement is assumed.
The v2 scalar-only embedding is not needed for this stronger result.
The E8 part uses the separately adopted and independently reviewed v1 argument at its unchanged scope.

The accepted external interfaces are [McM02 Theorem 1.1 in its exact canonical convention](../audits/literature/McM02/Yin_U002.md#canonical-coxeter-gap-input) and [Theorem 7.9 with exact Table 6](../audits/literature/McM02/Yin_U002.md#small-canonical-spectrum).
Accept them at the source unit's actual statement, convention and applicability depth, with no new audit of the foundational classification or catalog.
Their application concerns the canonical representation, not an arbitrary orthogonal representation of an abstract Coxeter group.

<a id="standard-cover-input"></a>
### Full standard representation and exact small interval

The fixed v2 construction supplies a real norm-two basis of \(I_N\oplus U\) with precisely the canonical Coxeter pairings.
For \(N\ge2\), those basis vectors are
\[
u_i-u_{i+1}\ (1\le i<N),\quad \sqrt2\,u_N,\quad
e-u_1-u_2,\quad -e-f;
\]
for \(N=1\), they are
\[
\sqrt2\,u,\quad \sqrt2(e-u),\quad -e-f.
\]
The cited arguments check every pairing, linear independence, the rank-two endpoint, and the exponent-infinity value in rank one.
They show that the resulting canonical group contains all positive signed permutations and all even-norm transvections at both fixed cusps.
In particular, this is coverage in the full real dimension and requires no power of the input word.

The form has negative index one, so the [complete expanding-count argument](../ledger/Yin_L_G0462_v13.md#negative-index-bound) identifies complete monic Mahler measure with spectral radius.
The accepted canonical theorem gives (3) for every word on \(I_N\oplus U\).
The v2 rational comparison proves that among the six exact canonical spectral radii in \((1,1.3)\), only the Lehmer value is below \(6/5\).
Its exact signed integer values are
\[
6762031,\quad -3478199,\quad -5935199,\quad -10121099,\quad
-386759,\quad -13388099,
\]
with denominator \(5^{10}\) except for the fifth value, whose denominator is \(5^8\).
The complete arithmetic, source polynomials and Salem sign argument remain in that fixed proof section.
They give (4) for the full standard action without a numerical root approximation.

<a id="neutral-equivariant-embedding"></a>
### Embedding a whole word with a finite-order positive complement

Assume (1)--(2).
Replace each positive factor \(R_j\) by \(S_j\), extended to fix \(e,f\).
Replace each transvection parameter \(v\) by the integer vector \(Vv\).
Equation (1) preserves the squared norm exactly, so every new transvection satisfies the same even-norm integrality condition.
The resulting word \(A'\) belongs to the standard group on \(I_N\oplus U\).

Let
\[
F=V(\mathbb Q^g),\qquad K=F^\perp=\ker(V^{\mathsf T})
   \subseteq\mathbb Q^N.
\]
Positive definiteness of \(H=V^{\mathsf T}V\) gives \(\operatorname{rank}V=g\), and the standard positive pairing gives the rational orthogonal direct sum
\[
\mathbb Q^N=F\oplus K.
\]
Each \(S_j\) preserves \(F\) by (2), acts there as \(R_j\), and preserves \(K\) by orthogonality.
The transvection formula shows directly that a transvection with parameter \(Vv\) preserves \(F\oplus U_{\mathbb Q}\), restricts there to the original transvection, and fixes \(K\) pointwise.
Hence \(A'\) preserves
\[
(F\oplus U_{\mathbb Q})\oplus K,
\]
with restrictions \(A\) and
\[
B=(S_1\cdots S_t)|_K,
\]
where the product follows the order of the positive factors in the original word.
Intervening transvections are the identity on \(K\), so no commutation assumption is used.

The product \(S_1\cdots S_t\) is itself a signed permutation of a finite basis and thus has finite order.
So does its restriction \(B\) to the rational invariant subspace \(K\).
Its characteristic polynomial \(\chi_B\) is rational and monic, and all its roots are roots of unity.
Every coefficient is therefore both a rational number and an algebraic integer, so
\(\chi_B\in\mathbb Z[z]\) and \(M(\chi_B)=1\).
When \(K=0\), take \(\chi_B=1\).

The actual complete characteristic identity is
\[
P_{A'}(z)=P_A(z)\chi_B(z).                               \tag{7}
\]
It requires only the rational invariant decomposition, not an integral direct-sum basis or a primitive embedding.
Both original and enlarged actions are integral isometries of negative-index-one forms.
Their reciprocal spectra have radius at least one, and (7) therefore gives
\[
M(P_{A'})=M(P_A)=\rho(A)=\rho(A').                       \tag{8}
\]
The standard conclusions applied to \(A'\) prove (3)--(4).
No expanding eigenvalue, leading coefficient or nonneutral factor has been discarded.

<a id="all-positive-diagonal"></a>
### Every positive integral orthogonal basis supplies the embedding

For (5), first determine the full positive integral isometry group.
Let \(a=\min_i d_i\).
For a nonzero integer vector \(v\),
\[
v^{\mathsf T}Dv=\sum_i d_i v_i^2\ge a.
\]
Equality holds precisely for the signed coordinate vectors \(\pm e_i\) with \(d_i=a\).
Every integral \(D\)-isometry therefore permutes those vectors and preserves their integral coordinate span.
It preserves the orthogonal complement as well, namely the coordinate sublattice on the remaining indices.
Apply the same argument to that smaller positive diagonal lattice and continue.
Thus every positive integral isometry is a signed permutation preserving the diagonal weights, and all such signed permutations are isometries.

For each distinct weight \(a\), let \(n_a\) be its multiplicity and group those coordinates together.
Embed its block \(aI_{n_a}\) in \(I_{a n_a}\) by repeating its coordinate vector \(a\) times.
Take the direct sum of these embeddings:
\[
V:\bigoplus_a\mathbb Z^{n_a}\longrightarrow
       \bigoplus_a(\mathbb Z^{n_a})^a.
\]
This is an integer isometric embedding, with \(V^{\mathsf T}V=D\) and \(N=\sum_a a n_a=\sum_i d_i\).
Every positive isometry has block form \(\bigoplus_a R_a\), with \(R_a\) a signed permutation.
The standard signed permutation
\[
S=\bigoplus_a\operatorname{diag}(R_a,\ldots,R_a)
\]
using \(a\) copies in its block satisfies \(SV=VR\).
Thus one common embedding satisfies (1)--(2) for every positive factor of every word.
All transvection parameters of even norm are covered by the preceding argument, independently of the sizes or parity of the \(d_i\)'s.

If the original lattice has another integer basis, an integral change of basis to the given orthogonal basis conjugates every generator and leaves the complete characteristic polynomial unchanged.
This proves the assertion for every positive integral lattice admitting such a basis, without claiming that every positive integral lattice is integrally diagonalizable.

<a id="e8-reuse"></a>
### The retained E8 result and its zero-permutation interval

The [complete v1 canonical-star argument](Yin_C_G0886_v1.md#argument) and its [independent review](../audits/reviews/Yin_R_G1114_v7.md#e8-block-canonical-cover-review) prove (6) and all its stated uniformity and sequence consequences.
Their root-system inputs and the word-dependent permutation convention are unchanged.

For \(d=1\), the actual canonical lift is already a Coxeter-group element rather than merely an element of its diagram extension.
Its full characteristic polynomial is
\[
\chi_{\widetilde A}(z)=(z-1)^{r-1}P_A(z).
\]
The added radical factor is neutral and the quotient has negative index one.
The same exact Table 6 comparison from v2 therefore proves (4) for this case as well.
For \(d>1\), the original proof takes the \(d\)-th power and pays its full logarithmic cost; no unpowered version of (4) is inferred.

<a id="limits"></a>
## Consequences for construction and remaining obligations

The entire two-fixed-cusp search over positive lattices with an integral orthogonal basis is excluded as a source of positive complete measures tending to one.
In the strict interval \(1<M<6/5\), it can only reproduce the Lehmer value, even with arbitrary unequal positive diagonal entries, rank, word length and vector norms.
The neutral-embedding condition also permits other explicitly verified input words, but supplies no embedding or extension for an arbitrary positive lattice.

Leaving these domains is not a construction of small measure.
For general positive lattices, [C885 v3](Yin_C_G0885_v3.md#decision-bounded-word-bounded-norm-gap) separately excludes simultaneously bounded transvection count and parameter squared norms from a positive-to-one sequence.
The E8-block family retains its unbounded-permutation-order obligation.
Neither condition is sufficient for nonneutrality, a new finite value or a complete-measure estimate tending to one.

This theorem neither identifies the generated subgroup with the full indefinite isometry group nor allows a real diagonalization to replace the actual integer embedding and signed-permutation extension.
It leaves arbitrary positive lattices without the stated embedding, other cusps and more general integer polynomial constructions unresolved.
The [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) is not completed.

## Assessment history

### Decision neutral-integral-embedding-cover

| Field | Value |
| --- | --- |
| date | 2026-11-10T04:08 |
| status | proved |
| reason | The complete independent review found no unresolved gap in the full standard canonical action, the per-word integer embedding and neutral complement, all positive diagonal lattices, six exact rational comparisons, retained E8 assertions or actual accepted source interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact embedding and diagonal-lattice theorem](#statement) | All embeddings and factor extensions, arbitrary ranks, diagonal weights, words and even-norm parameters, the absolute complete-measure gap, strict interval and retained E8 conclusions. |
| argument | [Complete assembled argument](#argument) | The actual standard-action inputs, whole-word neutral embedding, full positive diagonal isometry group, exact interval transfer and unchanged E8 reuse. |
| argument | [Standard rank at least two](Yin_C_G0886_v2.md#standard-rank-two-up) | Full real canonical basis, all pairings, every signed permutation and the complete two-cusp even-norm parameter groups; this is a selected fixed proof input, not an assumed v2 adoption. |
| argument | [Standard rank one](Yin_C_G0886_v2.md#standard-rank-one) | Exact infinite-edge canonical basis and reflection products covering the entire endpoint parameter group. |
| argument | [Standard complete-measure identity](Yin_C_G0886_v2.md#standard-gap) | Negative-index-one identification and the actual canonical action without a power or discarded nonneutral factor. |
| argument | [Exact six-fifths comparison](Yin_C_G0886_v2.md#six-fifths-classification) | All six integer evaluations and the Salem factorization sign test used with the published exact classification. |
| dependency | [Accepted McM02 interfaces](../audits/literature/McM02/Yin_U002.md#mcm02-u002) | Theorem 1.1, the exact canonical convention, and Theorem 7.9 with Table 6, at the recorded statement, primary-source inspection and applicability depth; foundational classification and catalog proofs are not newly audited. |
| dependency | [Adopted E8-block cover](Yin_C_G0886_v1.md#decision-e8-block-canonical-cover) | The unchanged full block-isometry group, primitive canonical quotient, specified-word permutation order, full power cost and sequence conclusions. |
| dependency | [Complete negative-index bound](../ledger/Yin_L_G0462_v13.md#negative-index-bound) | All generalized expanding eigenvalues and reciprocal spectrum, yielding complete Mahler measure equal to spectral radius. |
| dependency | [Integral transvection formulas](../ledger/Yin_L_G0462_v13.md#integer-generators) | Integrality, pairing preservation and inverse with even parameter norm on the actual positive integral lattice. |
| dependency | [Addition and covariance](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Full parameter addition and positive-isometry conjugation identities, without a word-length restriction. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1114_v10.md#neutral-embedding-canonical-gap-review) | The entire v3 theorem and all selected v2 proof inputs, exact source applicability, all degenerate cases and retained E8 scope, with no substantive repair or numerical search. |

## Current assessment

[Selected decision](#decision-neutral-integral-embedding-cover)
