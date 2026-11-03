---
author: Yin
---

<a id="msy23-u006"></a>
# MSY23-U006: Strong Atiyah Property and Bounded Dual Systems

- Source: [MSY23.pdf](../../../literature/pdf/MSY23.pdf), the 50-page published version registered as MSY23.
- Locators: Example 5.24 and Theorem 5.25 with Remarks 5.26-5.27, pp. 42-45; Section 6, pp. 45-48; references, pp. 49-50.
- Record: 2026-09-08, the unit authoring agent, for the [MSY23 source audit](readme.md).
- Kind: reconstructed source proofs and exact external interfaces.
The Haar-dual sign correction below is necessary for literal consistency with Definition 6.1.

## Setting and closure conventions

Let `(M,tau)` be finite tracial with faithful normal normalized trace, and put `A=U(M)`.
The bounded tuple `X=(X_1,...,X_n)` need not be normal or selfadjoint.
In this unit let

\[
R=\operatorname{Rat}_{A}\mathbb C\langle X\rangle,
\qquad
D=\operatorname{Div}_{A}\mathbb C\langle X\rangle.
\]

Both are taken in the affiliated algebra A.
The letter D in this paragraph is a ring, distinct from the dual operators used later.
[U003](Yin_U003.md#msy23-u003) supplies linear representations of elements of R, inverse closure of R, and Proposition 4.11 relating R and D when either is a division ring.
[U004](Yin_U004.md#msy23-u004) supplies rank, stable finiteness of A, and the equivalence between full analytic rank and affiliated invertibility.

The strong Atiyah property means that for every size N and every polynomial matrix P, the **unnormalized** rank `rk(P(X))` is a nonnegative integer.
It need not equal the inner rank over the original free polynomial algebra.
[U005](Yin_U005.md#msy23-u005) already establishes that maximal Delta implies this property.

## Example 5.24: integral rank need not preserve free-field rank

Take two standard free semicirculars S,T and set

\[
A_0=T^2,\qquad B_0=TST,\qquad C_0=TS^2T.
\]

Every polynomial matrix in this three-tuple is a polynomial matrix in S,T.
Hence the strong Atiyah property transfers from the semicircular pair to `(A_0,B_0,C_0)`.

The source also states that the triple is algebraically free; this can be checked directly.
Its monomials correspond to words obtained by concatenating blocks `t s^k t`, `k=0,1,2`, in the free monoid on s,t.
The lengths one or two of the s-runs recover each nonzero k.
The leading, intervening, and trailing t-run lengths then recover the number of zero-k blocks; the all-zero case is the even-length pure t-word.
Thus distinct words in the three generators give distinct words in s,t.
Algebraic freeness of S,T proves linear independence of the evaluated words.

Nevertheless,

\[
B_0 A_0^{-1} B_0=C_0
\]

in the affiliated algebra, since T is invertible there.
This is a genuine rational relation in three formal variables: at the scalar tuple `(a,b,c)=(1,0,1)`, the expression `ba^{-1}b-c` equals minus one.
The matrix

\[
P=\begin{pmatrix}a&b\\b&c\end{pmatrix}
\]

is full over the three-generator free polynomial algebra, because that same scalar tuple evaluates it to `I_2`, ruling out a factorization through dimension one.
At the displayed operator triple, multiplication by `diag(T^{-1},T^{-1})` on both sides gives

\[
\begin{pmatrix}1&S\\S&S^2\end{pmatrix}
 =\binom1S(1\ \ S),
\]

whose analytic rank is exactly one: it factors through one coordinate and has an identity entry.
Thus the triple has the strong Atiyah property but does not realize the free field on three generators.
No bounded inverse of T or A_0 is asserted or required.

## Theorem 5.25: the complete equivalence

With the above R and D, the following are equivalent:

1. Every linear polynomial matrix whose evaluation is full over R is invertible over A.
2. The same assertion holds for all polynomial matrices.
3. For every polynomial matrix P, `rk(P(X))=rho_R(P(X))`.
4. R is a division ring.
5. D is a division ring.
6. X has the strong Atiyah property.

The fullness in the first two items is over the evaluated ring R, not over the formal free polynomial algebra.
This distinction is essential in Example 5.24.

### Reconstruction of the implications

The second item implies the first trivially.
The third implies the second because full R-inner rank is N and analytic rank N is equivalent to an inverse in `M_N(A)`.
The equivalence between the fourth and fifth items is U003's Proposition 4.11, applied with the same ambient A.

Assume R is a division ring.
Gaussian elimination over R gives invertible U,V over R with

\[
UP(X)V=\operatorname{diag}(I_k,0),
\qquad k=\rho_R(P(X)).
\]

Their inverses remain inverses over A.
Analytic rank invariance under these factors gives item 3.

For item 1 implying item 4, take `0 != r in R`.
U003 gives a linear polynomial pencil L and scalar row u and column v such that

\[
r=uL(X)^{-1}v,
\]

where `L(X)` is invertible over A.
Its inverse has entries in R by the definition of rational closure, so it is also invertible over R.
The block pencil

\[
Q(X)=\begin{pmatrix}0&u\\v&L(X)\end{pmatrix}
\]

has Schur complement minus r.
A nonzero scalar entry is full as a one-by-one matrix over any unital nonzero algebra.
Since R is stably finite as a subalgebra of A, the fullness/Schur-complement lemma from U001 makes Q full over R.
Item 1 therefore makes Q invertible over A.
Block elimination then makes r invertible in A, and inverse closure of R puts `r^{-1}` in R.
Thus every nonzero r is a unit in R.

For item 6 implying item 4, use an arbitrary polynomial denominator matrix L from a representation of `0 != r in R`.
The same block Q satisfies the explicit identity

\[
\begin{pmatrix}-r&0\\0&I_N\end{pmatrix}
 =
\begin{pmatrix}1&-uL(X)^{-1}\\0&L(X)^{-1}\end{pmatrix}
\begin{pmatrix}0&u\\v&L(X)\end{pmatrix}
\begin{pmatrix}1&0\\-L(X)^{-1}v&I_N\end{pmatrix}.
\]

Both outer matrices are invertible over A.
Consequently

\[
\operatorname{rk}(Q(X))=N+\operatorname{rk}(r).
\]

The left side is integral because Q is a polynomial matrix.
Since `0<=rk(r)<=1` and `r != 0`, faithfulness implies `rk(r)>0`, so `rk(r)=1`.
Hence r is invertible in A and its inverse lies in R.
Finally item 3 immediately implies item 6 because inner ranks are integers.
This completes the entire equivalence without any bounded-inverse claim.

Remarks 5.26-5.27 compare this result with its group and commutative counterparts.
In the commutative setting the coefficient algebra is replaced by commutative polynomials and its rational closure; the same proof still takes closures and inverses in A.
The result does not imply that all polynomial relations vanish, that D is necessarily the free field, or that `D intersect M` equals scalar division closure in M.

## Section 6.1: how entropy supplies maximal Delta

For a selfadjoint tuple the source recalls two non-microstates dimensions, with distinct superscripts:

\[
\delta^*(X)
 =n-\liminf_{\epsilon\downarrow0}
       \frac{\chi^*(X+\sqrt\epsilon S)}{\log\sqrt\epsilon},
\qquad
\delta^\star(X)
 =n-\liminf_{t\downarrow0}t\Phi^*(X+\sqrt t S),
\]

where S is a free standard semicircular family free from X.
The verified external interface from CS05 is

\[
\delta^*(X)\le\delta^\star(X)\le\Delta(X)\le n.
\tag{1}
\]

The cited [CS05 preprint](https://arxiv.org/pdf/math/0309343v1), Lemma 4.1 on pp. 27-28, Theorem 4.4 on p. 29, and Corollary 4.6 on p. 31, was inspected for these exact statements and selfadjoint hypotheses.
Its full homological and entropy comparison proofs were not independently audited in this task.
Equation (1) is therefore an accepted external theorem, not a consequence of the new local trace calculation below.

The earlier [Voi98 entropy audit](../Voi98/Yin_U001.md#voi98-u001) supplies the finite-information entropy bound with its recorded analytic interfaces.
Together with the standard entropy-dimension implication recalled by the source, one obtains

\[
\Phi^*(X)<\infty\ \Longrightarrow\ \chi^*(X)>-\infty
\ \Longrightarrow\ \delta^*(X)=n
\ \Longrightarrow\ \delta^\star(X)=n
\ \Longrightarrow\ \Delta(X)=n.
\]

For one bounded selfadjoint variable the recalled formula is

\[
\delta^*(X)=1-\sum_{t\in\mathbb R}\mu_X(\{t\})^2.
\]

The scalar entropy comparison underlying it retains the boundary documented in the earlier Voi98 audit; the present source cites Part II Proposition 6.3 and Part V Proposition 7.6.
The source's conclusion for freely independent atomless selfadjoint variables additionally uses free additivity.
These entropy statements are kept as external interfaces.
They are not asserted for a tuple of arbitrary normal or nonnormal generators, and adjoining adjoints as formally independent variables would not preserve their hypotheses.

## Definition 6.1 and Proposition 6.2: the dual-system route

On `H=L2(M,tau)`, with `Omega=1` and vacuum projection P, the published source defines a bounded dual system by

\[
[X_i,D_j]=\delta_{ij}P,\qquad D_j\in B(H).
\tag{2}
\]

No adjoint condition or vacuum normalization is imposed.
For the project's convention `[D_j,X_i]=delta_ij P`, negate every source dual.
This is a harmless convention conversion, not an additional assumption.

Suppose finite-rank operators `T_1,...,T_n` satisfy `sum_i[T_i,X_i]=0`.
For any `Q_1,Q_2 in M'`, multiply this identity by `Q_1 D_j Q_2` and apply the ordinary operator trace.
All products are trace class because a T_i is finite rank and all other factors are bounded.
Cyclicity and commutation of Q_1,Q_2 with X_i give

\[
\begin{aligned}
0&=\sum_i\operatorname{Tr}([T_i,X_i]Q_1D_jQ_2)\\
 &=\sum_i\operatorname{Tr}(T_iQ_1[X_i,D_j]Q_2)\\
 &=\operatorname{Tr}(T_jQ_1P Q_2).
\end{aligned}
\]

For the inner product linear in its second variable this last scalar equals `<Q_2* Omega,T_j Q_1 Omega>`.
Since Omega is cyclic for M', both arguments range independently over dense subspaces.
Boundedness of T_j therefore implies `T_j=0`.
This proves vanishing of the finite-rank cycle space, hence `Delta(X)=n` by the definition in [U002](Yin_U002.md#msy23-u002).

The proof works for any bounded tuple and does not require selfadjointness, normality, freeness, factoriality, or generation of the ambient M by X.
In the standard tracial representation, cyclicity of Omega for the commutant can also be seen directly from bounded right multiplication by elements of M.
Boundedness of the D_j is essential to the trace-class products; no extension to unbounded dual systems is inferred.

## Proposition 6.3: the Haar example and its sign

On `ell2(F_n)` let `U_i` be left translation by the positive free generator `g_i`.
Define V_j to delete a terminal positive `g_j` from a reduced word and to be zero on all other words, including the identity.
This partial deletion is bounded of norm one.

Directly on the group basis,

\[
[U_i,V_j]=-\delta_{ij}P_e.
\tag{3}
\]

At the identity this is `0-V_j g_i=-delta_ij e`.
On a nonempty reduced word, left multiplication and terminal deletion agree after reduction; if left multiplication cancels the whole word, the word is a single `g_i^{-1}` and both outputs are zero.
If a terminal `g_j` is deleted, the remaining prefix does not end in `g_j^{-1}`, which prevents an unaccounted right cancellation.
These cases verify (3) for all reduced words, and boundedness extends it to the whole Hilbert space.

**Source correction, p. 48.**
Proposition 6.3 calls V itself a dual for the plus-sign convention (2), but its own displayed vacuum computation gives the minus sign.
Thus use `D_j=-V_j` under the source convention.
Under the project's convention, V itself has the required `[V_j,U_i]=delta_ij P_e`.
The rendered page was checked; this is a sign inconsistency in the published text, not a PDF-extraction artifact.

After this correction Proposition 6.2 applies.
Corollary 6.4 follows: the division and rational closures of `C<U_1,...,U_n>` in affiliated operators are isomorphic to the free field.
Adjoining `U_j^{-1}` does not enlarge that affiliated division closure.
The corollary reproduces the free-group field conclusion attributed to Linnell; its proof here is the dual calculation plus the paper's own free-field theorem, so Linnell's original proof is not an additional assumption.

## Reuse boundary and bibliography coverage

Theorem 5.25 and Corollary 6.4 refer throughout to A, the affiliated algebra.
An inverse `L(X)^{-1}` in these proofs is not shown to lie in `M_N(M)`.
Neither a scalar output being bounded nor minimality of a representation is used to infer such a bounded matrix inverse.
This unit therefore supports the passage from a bounded dual system to free-field realization, while leaving any bounded scalar-closure descent as a separate obligation.

The references on pp. 49-50 were read and classified for the present proof chain.
The exact original CS05 dimension comparisons are accepted at the inspected scope; source [54] is the separately audited Voi98.
Source [46], [SS15](https://arxiv.org/pdf/1305.1920v1), Theorem 3.4, p. 8, was checked as historical context: its strong-Atiyah theorem applies to the star algebra of normal freely independent variables with the stated atom lattice.
It is not needed to deduce Theorem 5.25 or the semicircular specialization once maximal Delta is available.
Source [33] Linnell and [35] Lueck supply historical group-theoretic comparisons, not extra premises of the reconstructed proofs.
Source [41] is the earlier MSY preprint, distinct from the present published artifact.
Source [38] is Miy22, whose independently audited bounded criterion is confined to the semicircular model.
The remaining bibliography is contextual or belongs to the algebraic/affiliated units U001-U004; no complete audit of all 56 cited works is claimed.

All assigned text on published pp. 42-50 was read.
Published pp. 43, 46, 47 and 48 were visually inspected for the equivalence list, the distinct dimension superscripts, the finite-rank trace calculation, and the Haar sign.
The block products, algebraic-freeness example, trace argument, and reduced-word cases were reconstructed directly.
Independent cross-review is recorded separately when completed.
No numerical test, formal verification, author confirmation of the sign correction, or full recursive audit of the cited literature is asserted.

Independent review, 2026-09-08, a separate reviewing agent: compared this unit with published pp. 42-50 and independently viewed pp. 44 and 48.
For Theorem 5.25, verified that the denominator inverse lies over R before applying the stable-finite fullness argument, checked both outer factors in the integral-rank Schur identity, and checked all implications in the six-way equivalence.
The three words `tt`, `tst`, `tsst` form a prefix code, independently confirming the algebraic-freeness argument; the evaluated rational relation and rank-one matrix computation preserve the affiliated ambient.
For the dual proof, every trace cyclicity uses a trace-class factor and bounded remaining factors, and the commutant vectors are independently dense.
The Haar deletion maps distinct eligible basis words to distinct words; the vacuum and the whole-word cancellation case were checked separately, confirming the corrected minus sign under the source convention.
The stated entropy comparisons remain the explicitly declared external interfaces, whose original proofs were not re-audited by this reviewer.
No additional substantive defect was found in the reconstructed statements.

## Source and inspection

Source edition: MSY23 / MSY23, the user-supplied 50-page published article in Journal of Functional Analysis 285 (2023), article 110016, DOI 10.1016/j.jfa.2023.110016. Printed pages equal PDF pages. The separate 37-page arXiv v2 was not compared in full; other works retain their own versions and inspection limits in the body.

Passages: Example 5.24, Theorem 5.25 and Remarks 5.26-5.27, published pp. 42-45; Section 6, pp. 45-48; bibliography pp. 49-50.

Inspection: 2026-09-08: all assigned pages read; the six-way equivalence, finite-rank trace argument and reduced-word cases reconstructed and independently reviewed; the Haar-dual sign correction was visually checked. CS05 arXiv:math/0309343v1 dimension comparisons were inspected as exact statements, not a full audit of their homological/entropy proofs. Voi98 retains its separate analytic boundaries; SS15 is historical context. No unbounded-dual extension, bounded scalar descent, numerical test, formal verification, author-confirmed erratum or full audit of all cited works is claimed.
