---
author: Yin
---

# Near Minimizers and Tensor Products of Capacity

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Source/version: GGOW20, [published full PDF](../../../literature/pdf/GGOW20.pdf).

Passages: Locators: Section 3, pp. 253-261 (PDF 31-39); Lemmas 3.2/3.4, pp. 254-256; Lemma 3.6 and Definition 3.8, p. 257; Lemmas 3.9-3.10, pp. 257-258; Theorem 3.11 and Lemma 3.12, pp. 259-261.

Inspection: State: `Audited within scope`, using the corrected interfaces below and the declared Gur04 approximate-scaling foundation.


<a id="ggow20-u003"></a>
## GGOW20-U003 - Quantitative balancing and multiplicativity

- Source/version: GGOW20, [published full PDF](../../../literature/pdf/GGOW20.pdf).
- Locators: Section 3, pp. 253-261 (PDF 31-39); Lemmas 3.2/3.4, pp. 254-256; Lemma 3.6 and Definition 3.8, p. 257; Lemmas 3.9-3.10, pp. 257-258; Theorem 3.11 and Lemma 3.12, pp. 259-261.
The dual variational formula is also stated on p. 242 (PDF 20).
- Record: 2026-09-12, the operator-scaling source reviewer; complete local proof review of Section 3, with the coordinating agent independent review of the near-minimizer chain, its domain conditions and Lemma 3.6's missing branch.
- State: `Audited within scope`, using the corrected interfaces below and the declared Gur04 approximate-scaling foundation.
This does not claim independent review of every paper cited in Section 3.

### Conventions and duality

Use \(T:M_n(\mathbb C)\to M_n(\mathbb C)\), the unnormalized trace, capacity and marginal defect from [U002](Yin_U002.md#ggow20-u002).
The Frobenius/Hilbert-Schmidt norm is \(\|A\|_{\mathrm{HS}}^2=\operatorname{Tr}(AA^*)\).

The capacity-duality identity used in Lemmas 3.9-3.10 is \(\operatorname{cap}(T)=\operatorname{cap}(T^*)\).
Its proof is supplied by the variational formulation on p. 242:

\[
 n\operatorname{cap}(T)^{1/n}
 =\inf_{X,Y>0,\ \det X=\det Y=1}\operatorname{Tr}(T(X)Y)
 =\inf_{X,Y>0,\ \det X=\det Y=1}\operatorname{Tr}(XT^*(Y)).
\]

For fixed \(X\), arithmetic-geometric mean gives the first equality by choosing \(Y=(\det T(X))^{1/n}T(X)^{-1}\) when \(T(X)>0\).
If \(T(X)\) is singular, determinant-one positive matrices that tend to zero on its support and grow on its kernel make the infimum zero.
Swapping the two variables proves duality, including capacity zero.
This checks the exact identity rather than assuming that an optimizer exists.

### Almost doubly stochastic maps

The reusable form of Lemma 3.4 is: if \(T\) is positive, \(T^*(I)=I\), and

\[
 \operatorname{Tr}(T(I)-I)^2\leq\epsilon,\qquad 0\leq\epsilon\leq1/n,
\]

then

\[
 (1-\sqrt{n\epsilon})^n\leq\operatorname{cap}(T)\leq1.
\]

The analogous statement holds with the two marginals exchanged.
**Correction F3:** the printed Lemmas 3.2 and 3.4 omit the small-\(\epsilon\) restriction.
Their stated polynomial lower bound must not be used when its base is negative: for even \(n\) this could falsely give a positive lower bound for a zero-capacity map.
The range above covers the paper's small-error applications; outside it only the trivial lower bound zero is retained here.

The complete proof passes through nonnegative matrices.
For a row-stochastic matrix with column-error squared sum at most \(\epsilon\), successively subtract positive multiples of supported permutation matrices.
There are at most \(n^2\) such subtractions before the residual permanent vanishes.
This gives \(A=\lambda B+Z\), with \(B\) doubly stochastic and \(Z\geq0\).
If \(\lambda<1\), the normalized residual is row stochastic and has zero permanent; Hall's matching criterion yields a set of rows whose neighbors are fewer, forcing squared column error at least \(1/n\) by Cauchy-Schwarz.
Hence \(\lambda\geq1-\sqrt{n\epsilon}\).
Jensen's inequality gives capacity at least one for \(B\), so the lower bound follows by entrywise monotonicity and homogeneity.
Transposing the decomposition proves the version with rows and columns exchanged.

For the positive map, diagonalize \(X=\sum_j\lambda_jv_jv_j^*\) and \(T(X)=\sum_i\sigma_iu_iu_i^*\), and set \(a_{ij}=u_i^*T(v_jv_j^*)u_i\geq0\).
Then \(\sigma=A\lambda\), the column sums are one, and the row sums are \(r_i=u_i^*T(I)u_i\).
Their squared error is at most \(\operatorname{Tr}(T(I)-I)^2\), by the scalar Cauchy-Schwarz inequality on each vector \(u_i\).
Apply the matrix bound.
**Correction F4, p. 256:** the source calls these \(r_i\) "column sums", but its displayed formula is the row sum.
The proof uses the row sum as above.

The reverse estimate (Lemma 3.6) is: if \(T^*(I)=I\), \(0\leq\delta\leq1/6\), and \(\operatorname{cap}(T)\geq e^{-\delta}\), then

\[
 \operatorname{ds}(T)=\operatorname{Tr}(T(I)-I)^2\leq6\delta.
\]

To check the proof completely, let \(x_i>0\) be the eigenvalues of \(T(I)\), so \(\sum_ix_i=n\), and put \(\alpha=\sum_i(x_i-1)^2\).
For \(\alpha\leq1\), Lemma 5.1 gives \(\prod_ix_i\leq e^{-\alpha/6}\).
**Correction F5:** the source invokes this conclusion without excluding \(\alpha>1\).
For that case put \(y_i=x_i-1\), and consider \(F(t)=\prod_i(1+ty_i)\).
For \(0<t\leq1\),

\[
 \frac{d}{dt}\log F(t)
 =-t\sum_i\frac{y_i^2}{1+ty_i}<0
\]

unless all \(y_i=0\).
At \(t=\alpha^{-1/2}<1\), the variance equals one, so Lemma 5.1 gives \(F(t)\leq e^{-1/6}\); strict decrease then yields \(\prod_ix_i<e^{-1/6}\leq e^{-\delta}\), a contradiction.
Thus \(\alpha\leq1\), and the desired bound follows.
The coordinating agent independently checked this missing-branch repair.

### Near minimizers as approximate balancing points

For \(C>0\) such that **\(T(C)>0\)**, put

\[
 r_T(C)=\frac{\det T(C)}{\det C},\qquad
 E_T(C)=C^{1/2}T^*(T(C)^{-1})C^{1/2}-I.
\]

Definition 3.8's fixed-point error is \(\operatorname{Tr}(E_T(C)^2)\).
The source writes \(\operatorname{Tr}[(CT^*(T(C)^{-1})-I)^2]\), which agrees by similarity and cyclicity of trace.
The matrix inside that latter square need not be Hermitian; do not replace the expression by its Hilbert-Schmidt norm squared.
The \(E_T(C)\) formulation is Hermitian and nonnegative after taking its squared trace.

The two checked interfaces are:

- **Lemma 3.9:** if \(\operatorname{Tr}(E_T(C)^2)\leq\epsilon\leq1/(n+1)\), then \(T\) is rank non-decreasing and
  \[
  (1-\sqrt{n\epsilon})^n r_T(C)
       \leq\operatorname{cap}(T)\leq r_T(C).
  \]
- **Lemma 3.10:** if \(0\leq\delta\leq1/6\) and
  \[
  \operatorname{cap}(T)\geq e^{-\delta}r_T(C),
  \]
  then \(\operatorname{Tr}(E_T(C)^2)\leq6\delta\).

Both proofs use the normalized map

\[
 Z(X)=T(C)^{-1/2}T(C^{1/2}XC^{1/2})T(C)^{-1/2}.
\]

It satisfies \(Z(I)=I\), \(Z^*(I)-I=E_T(C)\), and \(\operatorname{cap}(Z)=\operatorname{cap}(T)/r_T(C)\).
Theorem 2.12 and Lemma 3.4 applied to \(Z^*\) prove Lemma 3.9.
Lemma 3.6 applied to \(Z^*\) proves Lemma 3.10.

**Correction F6, p. 258:** Lemma 3.10 as printed needs \(T(C)>0\) for these inverse expressions.
The zero map satisfies its displayed numerical premise but does not define \(Z\) or the fixed-point residual.
Positive capacity is a sufficient convenient standing hypothesis and is available in MS24's application.

**Correction F7, p. 258:** retain the exact \(\operatorname{cap}(Z)=\operatorname{cap}(Z^*)\geq e^{-\delta}\).
The source weakens this to \(1-\delta\) and then invokes Lemma 3.6 with the same parameter; that weaker bound alone would not justify the constant \(6\delta\).
The actual hypothesis supplies precisely the stronger inequality needed.

These are quantitative controls of the scaled **finite-dimensional marginal**, not operator-norm bounds for a free-field element evaluated at a tuple.
They are the exact near-minimizer inputs for the [MS24 audit](../MS24/readme.md).

### Tensor multiplicativity

Theorem 3.11 gives, for completely positive \(T_i:M_{d_i}(\mathbb C)\to M_{d_i}(\mathbb C)\),

\[
 \operatorname{cap}(T_1\otimes T_2)
 =\operatorname{cap}(T_1)^{d_2}\operatorname{cap}(T_2)^{d_1}.
\]

The upper bound follows by testing determinant-one \(X\otimes Y\) and passing to minimizing sequences; no minimizer is assumed.
If either factor has zero capacity, this upper bound already gives equality.

For the other direction assume both capacities positive.
The [Gur04 approximate-scaling criterion](../Gur04/Yin_U002.md#gur04-u002) yields right-normalized scalings \(S_i\) with \(\operatorname{ds}(S_i)\leq\epsilon\), for arbitrary \(\epsilon>0\).
Then \(S=S_1\otimes S_2\) is right normalized and

\[
 \operatorname{ds}(S)\leq2(d_1+d_2+\epsilon)\epsilon.
\]

Indeed expand \(S_1(I)\otimes S_2(I)-I\) as the sum \(S_1(I)\otimes(S_2(I)-I)+(S_1(I)-I)\otimes I\), use the Hilbert-Schmidt triangle-square bound, and \(\operatorname{Tr}(S_1(I)^2)\leq d_1+\epsilon\).
The summands are Hermitian, which suffices; the source's phrase "for psd matrices" is unnecessarily restrictive here.
The small-error capacity bound makes \(\operatorname{cap}(S)\to1\).
Scale back using Proposition 2.7 and \(\operatorname{cap}(S_i)\leq1\), and let \(\epsilon\downarrow0\).

**Correction F8:** the source cites Theorem 2.14 for arbitrary-complex-coefficient, arbitrarily accurate scalings although that theorem is stated for integral input and a fixed decision threshold.
The qualitative Gur04 criterion just used, or the same capacity-growth proof for an arbitrary fixed positive initial capacity and prescribed threshold, supplies the needed premise.
No uniform bit-complexity assertion for arbitrary complex coefficients is required.

### Review boundaries and downstream effects

The local Section 3 proofs were reviewed, including the nonnegative-matrix decomposition, spectral reduction, similarity identity, marginal estimate, minimizing-sequence argument and scaling powers.
The Hall matching criterion, finite-dimensional spectral theorem, Gur04 scaling characterization, and Lemma 5.1 as checked in [U004](Yin_U004.md#ggow20-u004) are the retained inputs.
The coordinating agent independently checked Lemma 3.6 and Lemma 3.10, including F5-F7, on 2026-09-12.
Rendered PDF pp. 32-39 were inspected at the key matrix and determinant formulas.
No formal verification was performed.

F3-F8 restrict or repair the source's displayed proof interfaces; they do not invalidate the small-error results used by this audit or MS24.
No broad claim about the current state of operator-scaling algorithms or optimal constants is inferred from the paper's dated introductory discussion.
