---
author: Yin
---

# Uniform Mahler gaps for bounded transvection words and bounded vector norms

<a id="statement"></a>
## Statement and exact alternatives

Fix an integer \(k\ge1\) and a real \(B\ge1\).
Let \(H\) be any positive definite symmetric integral Gram matrix of rank \(g\ge1\), and equip
\[
\Lambda=\mathbb Z^g\oplus U,\qquad
G_0=H\oplus\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
with its displayed integral form.
Write \(e,f\) for the hyperbolic basis, with \(e^2=f^2=0\) and \((e,f)=1\).
Every positive integral isometry is extended to fix both \(e\) and \(f\).
For an integral positive vector \(v\) of even squared norm, use
\[
T_{e,v}(x)=x-(v,x)e+(e,x)v-\frac{(v,v)}2(e,x)e,
\]
and define \(T_{f,v}\) by exchanging \(e,f\).

Consider every finite word \(A\) in positive integral isometries and these two fixed-cusp transvection groups, with at most \(k\) transvection factors and squared norm at most \(B\) for every displayed transvection parameter.
The complete characteristic polynomial \(P_A(z)=\det(zI-A)\) has a uniform positive total-logarithmic gap:
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta(k,B)>0.          \tag{1}
\]
The constant depends only on \(k,B\), independently of rank, the positive lattice and its determinant, all integer coordinates, the number and orders of positive-isometry factors, the cusp pattern and the particular parameters.
Zero and linearly dependent parameters are included.
For the empty positive lattice, every transvection is the identity and the conclusion is neutral.

Separately, the established absolute constant \(\eta_*>0\) in [v2](Yin_C_G0885_v2.md#decision-positive-lattice-two-transvection-gap) works for all such words with at most three transvections without any norm bound:
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta_*.              \tag{2}
\]
This second assertion reuses the existing exact short-word conjugacy argument.

Consequently a sequence of these complete polynomials with \(1<M(P_{A_j})\to1\) cannot admit presentations with both uniformly bounded transvection count and uniformly bounded parameter squared norms.
For each fixed pair \(k,B\), every sufficiently late member has no presentation satisfying both bounds.
This does not require both quantities to grow separately in every presentation.
No effective threshold at \(6/5\), general fixed-length theorem with unbounded norms, or unrestricted Lehmer conclusion is asserted.

<a id="argument"></a>
## Complete argument and accepted inputs

The finite-column reduction was proposed in the bounded strategy investigation and is checked here for every fixed \(k\), including the six-column four-factor case.
The new argument extends the integer-correlation and signed-coset mechanism of [v2](Yin_C_G0885_v2.md#argument), not its two-factor large-norm estimate.
It uses the accepted [Sanders integer-valued Fourier-algebra theorem](../audits/literature/San20/Yin_U001.md#san20-u001) and [DS17 univariate fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) at their recorded statement and applicability depths.
No new inspection of those sources' foundational proofs is claimed.
The rest is a project deduction from the full integer word and its complete characteristic polynomial.

<a id="word-normalization"></a>
### Normalize the word without changing parameter norms

The [integral transvection calculation](../ledger/Yin_L_G0462_v13.md#integer-generators) proves integrality, pairing preservation and the negative-vector inverse under the stated even-norm hypothesis.
For every positive integral isometry \(R\), the [covariance identity](../ledger/Yin_L_G0462_v14.md#short-word-reduction) gives
\[
T_{e,v}R=RT_{e,R^{-1}v},\qquad
T_{f,v}R=RT_{f,R^{-1}v}.
\]
Move all positive-isometry factors to the left, retaining their ordered product.
The transformed integer parameters keep their original norms, cusp directions and number.
Padding by zero parameters gives
\[
A=\overline R C,\qquad
C=T_{\epsilon_1,v_1}\cdots T_{\epsilon_k,v_k},
\qquad \epsilon_i\in\{e,f\},\quad (v_i,v_i)\le B,          \tag{3}
\]
where \(\overline R=R\oplus I_U\).
This also covers a word with no nonidentity transvection.

The integral \(H\)-isometry group is finite: its \(j\)-th columns have fixed positive squared norm \(H_{jj}\), so their integer coordinates range over finite sets.
Thus \(R^N=I\) for some \(N\ge1\), with no uniform bound on \(N\) required.
Its monic integer characteristic polynomial
\[
\chi_R(z)=\det(zI-R)
\]
has only roots of unity and has complete measure one.
The isometry \(A\) is integral, so \(P_A\) is a nonzero monic integer polynomial.

<a id="finite-column-determinant"></a>
### The full word determinant without independent columns

Put \(m=k+2\), let \(S\) be the \((g+2)\)-by-\(m\) integer matrix with columns
\[
v_1,\ldots,v_k,e,f,
\qquad F=S^{\mathsf T}G_0.
\]
The columns of \(S\) need not be independent.
No inverse of \(S^{\mathsf T}G_0S\), rational projection onto its span, or integral direct-sum decomposition is introduced.

For an e-factor at position \(i\), define the integer \(m\)-by-\(m\) matrix \(D_i\) by the three possibly nonzero entries
\[
(D_i)_{i,k+1}=1,\qquad
(D_i)_{k+1,i}=-1,\qquad
(D_i)_{k+1,k+1}=-(v_i,v_i)/2 .
\]
For an f-factor, replace \(k+1\) with \(k+2\).
Direct substitution gives
\[
T_{\epsilon_i,v_i}=I+SD_iF.
\]
This remains true when \(v_i=0\): the corresponding column and pairing row both vanish and its half-norm is zero.

The identity
\[
(I+SDF)(I+SEF)=I+S\bigl(D+E+D(FS)E\bigr)F
\]
produces an integer matrix \(D\) for the entire ordered product:
\[
C=I+SDF.                                                \tag{4}
\]
No size bound on entries of \(D\) will be needed.

Over the rational-function field define
\[
Z(z)=F(zI-\overline R)^{-1}\overline R S.
\]
The rectangular determinant identity \(\det(I-XY)=\det(I-YX)\), applied to (3)--(4), gives
\[
P_A(z)=\chi_R(z)(z-1)^2\det\bigl(I_m-DZ(z)\bigr).         \tag{5}
\]
This identity holds without injectivity or surjectivity of \(S\) or \(F\).
In particular it covers every zero or dependent parameter pattern in the six-column case \(k=4\).

Put \(K_R(z)=(zI-R)^{-1}R\).
The positive \(k\)-by-\(k\) block of \(Z\) consists of
\[
Z_{ij}(z)=(v_i,K_R(z)v_j).
\]
The two hyperbolic rows and columns form
\[
\begin{pmatrix}0&(z-1)^{-1}\\(z-1)^{-1}&0\end{pmatrix},
\]
and all mixed blocks are zero.
These are actual entries in the original-dimensional determinant reduction; no characteristic factor has been discarded.

<a id="uniform-correlations"></a>
### Uniform Fourier bounds for all integer cyclic correlations

On \(\mathbb Z/N\mathbb Z\), define all \(k^2\) integer functions
\[
f_{ij}(a)=(v_i,R^a v_j).
\]
Extend the positive form to a Hermitian inner product, conjugate-linear in its first entry.
For the mutually orthogonal spectral projections \(\Pi_\lambda\) of \(R\), \(\lambda^N=1\), one has
\[
f_{ij}(a)=
 \sum_{\lambda^N=1}\lambda^a
 \langle\Pi_\lambda v_i,\Pi_\lambda v_j\rangle_H.
\]
In the [normalized Fourier convention](../audits/literature/San20/Yin_U001.md#finite-abelian-fourier-algebra-norm), these are precisely the Fourier coefficients.
Cauchy--Schwarz in each eigenspace and then across the eigenspaces gives
\[
\|f_{ij}\|_A
\le\sum_\lambda\|\Pi_\lambda v_i\|_H\|\Pi_\lambda v_j\|_H
\le\|v_i\|_H\|v_j\|_H
\le B.                                                   \tag{6}
\]
This includes repeated eigenvalues, zero vectors, \(N=1\), and arbitrary integer bases of \(H\).
No number of occupied coordinates or bound on \(N\) appears.

The accepted Sanders theorem supplies an integer \(L=L(B)\ge1\), depending only on \(B\), so each \(f_{ij}\) is a signed sum of at most \(L\) subgroup-coset indicators.
Split integer coefficients into signed repetitions when necessary.
A coset in the cyclic group is a residue class \(a\equiv u\pmod d\), where \(d\mid N\) and \(0\le u<d\).

For \(|z|>1\), the positive entries of \(Z\) equal
\[
Z_{ij}(z)=\sum_{a\ge1} f_{ij}(a)z^{-a}.
\]
For one residue class, set \(\nu=u\) when \(u>0\) and \(\nu=d\) when \(u=0\).
Then
\[
\sum_{\substack{a\ge1\\a\equiv u\pmod d}}z^{-a}
 =\frac{z^{d-\nu}}{z^d-1},\qquad 0\le d-\nu<d.            \tag{7}
\]
This treats the zero-residue class and the trivial cyclic group without an extraneous constant term.
Each positive entry of \(Z\) is therefore a signed sum of at most \(L\) integer monomials divided by cyclotomic binomials.

<a id="neutral-clearing"></a>
### Neutral clearing with the complete original measure

Let \(\Delta(z)\) be \(z-1\) times the product of every denominator occurrence in all \(k^2\) signed-sum expressions.
Repeated denominators are retained as repeated factors.
There are at most
\[
q=1+k^2L
\]
binomial factors.
Thus \(\Delta\) is monic, nonzero and has complete measure one, with at most \(2^q\) terms.

Every entry of \(\Delta Z\) is an integer polynomial with at most \(L2^q\) terms.
For a positive entry, multiply each signed numerator monomial by the product of the other factors in \(\Delta\); this is a sum of at most \(L\) such products.
For a nonzero hyperbolic entry, \(\Delta/(z-1)\) is the product of the remaining binomials and satisfies the same bound since \(L\ge1\).
Zero mixed entries need no separate bound.

Define the actual integer polynomial
\[
U(z)=\det\bigl(\Delta(z)I_m-D\Delta(z)Z(z)\bigr).          \tag{8}
\]
Equation (5) becomes the complete polynomial identity
\[
\chi_R(z)(z-1)^2U(z)=\Delta(z)^mP_A(z).                  \tag{9}
\]
It first follows as an equality of rational functions; both sides are polynomials, so it retains all multiplicities also at the former poles.
Since \(\Delta\ne0\) and \(P_A\ne0\), identity (9) implies \(U\ne0\).
Multiplicativity of complete Mahler measure, with
\[
M(\chi_R)=M((z-1)^2)=M(\Delta)=1,
\]
now gives exactly
\[
m(U)=m(P_A).                                            \tag{10}
\]
There is no claim that \(U/P_A\) is an integer polynomial, and no leading coefficient or exceptional root is omitted.

Each entry in the determinant (8) has at most
\[
(1+mL)2^q
\]
nonzero terms: the matrix product uses at most \(m\) entries of \(\Delta Z\), multiplied by constant integers, plus the possible diagonal term \(\Delta\).
Hence a uniform upper bound for the support of \(U\) is
\[
K(k,B)=m!(1+mL)^m2^{mq},\qquad m=k+2,\quad q=1+k^2L.     \tag{11}
\]
Cancellations, repeated terms or zero entries can only reduce this bound.
The accepted DS17 univariate consequence gives a positive \(\eta_{K(k,B)}\) for every nonzero integer polynomial of at most this support whenever its logarithmic measure is positive.
Together with (10), this proves (1) with \(\eta(k,B)=\eta_{K(k,B)}>0\).
No coefficient-height bound or effective numerical choice of this constant is used.

<a id="short-word-and-sequence"></a>
### Reused short-word case and the sequence consequence

The [complete short-word reduction](../ledger/Yin_L_G0462_v14.md#short-word-reduction), independently checked in [R1114 v4](../audits/reviews/Yin_R_G1114_v4.md#short-word-conjugacy-control-review), combines equal-cusp factors and integrally conjugates every alternating three-factor word to a two-factor word.
For example,
\[
T_{e,u}\bigl(\overline R T_{e,v}T_{f,w}T_{e,u}\bigr)T_{e,-u}
=\overline R T_{e,R^{-1}u+v}T_{f,w}.
\]
The new parameter has even integral norm, with no bound required.
The other cusp pattern follows by exchanging \(e,f\); zero and one-factor cases are neutral.
The full characteristic polynomial is unchanged by this conjugacy.
Applying the [adopted v2 theorem](Yin_C_G0885_v2.md#decision-positive-lattice-two-transvection-gap) proves (2), retaining its absolute gap and source-review scope.

For any fixed \(k,B\), (1) excludes positive values below \(\eta(k,B)\) from every presentation satisfying both bounds.
If the complete positive logarithmic measures tend to zero, they are eventually below this constant.
This proves the stated presentation-level sequence consequence, without inferring that length and norm must each separately diverge.

<a id="limits"></a>
## Consequence and limits for counterexample construction

The bounded-norm conclusion applies even to rootless positive lattices and isometries of unbounded order; it does not use a Coxeter representation.
It therefore addresses a different parameter restriction from the [E8-block permutation-order theorem](Yin_C_G0886_v1.md#decision-e8-block-canonical-cover).
The theorem does not bound four-factor or longer words with unrestricted norms.

The [constant-Lehmer conjugacy control](../ledger/Yin_L_G0462_v14.md#unbounded-parameters) shows why displayed large norms alone supply no low-measure mechanism or large-measure estimate.
A new positive-to-one construction would need presentations escaping the simultaneous bounds, together with an actual complete-measure estimate.
No such construction, effective \(6/5\) exclusion or [unrestricted G0001 resolution](../tasks/Yin_T_G0001_v1.md#contract) follows from this result.

## Assessment history

### Decision bounded-word-bounded-norm-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T03:55 |
| status | proved |
| reason | The complete independent review found no unresolved gap in the arbitrary-positive-lattice finite-column identity, all uniform Fourier and support bounds, exact complete-measure transfer, degenerate cases, accepted source interfaces or retained short-word and sequence assertions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact bounded-count and bounded-norm statement](#statement) | Every fixed k and B, all positive integral lattices and specified words, the separate unbounded-norm at-most-three assertion and the exact presentation-level sequence consequence. |
| argument | [Complete argument](#argument) | Norm-preserving normalization, dependent finite columns, all cyclic correlations, neutral polynomial clearing, uniform support and the separate reused short-word proof. |
| dependency | [Integral generators](../ledger/Yin_L_G0462_v13.md#integer-generators) | Even-norm integrality, pairing preservation and negative-vector inverses at the actual arbitrary-positive-lattice scope. |
| dependency | [Covariance and short-word reduction](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Norm-preserving normalization and the exact three-to-two conjugacy, with no norm restriction on the latter assertion. |
| dependency | [Adopted unbounded-norm two-factor gap](Yin_C_G0885_v2.md#decision-positive-lattice-two-transvection-gap) | The absolute constant used only for the separate at-most-three-transvection statement. |
| dependency | [Accepted Sanders theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Uniform signed-coset length from the normalized integer Fourier-algebra norm bound B, at the recorded source-review depth. |
| dependency | [Accepted fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | Uniform positive total-logarithmic gap for nonzero integer polynomials with the displayed bounded support, independent of degree and coefficient height. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1114_v9.md#bounded-word-bounded-norm-review) | Every quantifier, full determinant and measure identity, both accepted source interfaces, degenerate cases and the precise limits of the conclusion. |

## Current assessment

[Selected decision](#decision-bounded-word-bounded-norm-gap)
