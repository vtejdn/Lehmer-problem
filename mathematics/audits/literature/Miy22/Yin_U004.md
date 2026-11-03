---
author: Yin
---

# Analytic Realization and the Bounded Theorem

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), published journal version.
- Review date and reviewer: 2026-09-08, the analytic reconstruction agent.
  This is an internal mathematical source review, with explicit reconstructions of the steps below; it is not formal verification or external peer review.
- Inspected material: extracted text and rendered formulas on printed/PDF pp. 6-8 and 11-18, together with the setting and commutator context on pp. 4-5 and 9-10.
- Scope: Lemmas 3.4-3.8, Proposition 3.9, and the bounded Theorem 3.1 assembly.
  The imported formal-series equivalence and the bounded extension of the commutator identity are supplied by the linked units.

The analytic steps below remain valid after the local repairs identified in this record and the scalar-rate correction in U002.
This assessment concerns the stated full-Fock semicircular setting and the specified imported inputs.
It does not assert that the printed proof is free of errors.


This source analysis comprises [U004](#miy22-u004), [U005](Yin_U005.md#miy22-u005).
Its [shared source, inspection and setting](#analytic-realization-and-the-bounded-theorem) and [joint review dated 2026-09-08](Yin_U005.md#independent-cross-review-of-u004-u005) retain their original scopes.

<a id="miy22-u004"></a>
## Miy22-U004: Matrix Realization, Haagerup Estimates, and Norm Convergence

**Locators:** Lemma 3.4, pp. 11-12; Lemma 3.5, pp. 12-14; Lemma 3.6, pp. 14-15; Corollary 3.7, pp. 15-16.

### Setting and Dependencies

Use the finite-dimensional full-Fock setting of [Miy22-U001](Yin_U001.md#miy22-u001): $d\geq1$, $s_i=\ell_i+\ell_i^*$, $M=W^*(s)$, and $A=C^*(s)$.
Let $U_w$ be the word polynomials with $U_w\Omega=e_w$, using the monic Chebyshev recurrence

\[
U_{-1}(t)=0,\qquad U_0(t)=1,\qquad
U_{n+1}(t)=tU_n(t)-U_{n-1}(t).
\]

The formal rational/recognizable equivalence, coefficientwise conjugation and Hadamard operations, and the repaired scalar rational-decay estimate are inputs from [Miy22-U002](Yin_U002.md#miy22-u002).
They are not consequences of the norm estimates in this unit.

The notation $U_w$ is not multiplicative in arbitrary concatenations.
All infinite sums below are grouped by word length.
Absolute summability of the homogeneous-block norms is proved; arbitrary reordering of individual word terms is not asserted.

### Matrix Realization: Lemma 3.4

Put

\[
T_i=\begin{pmatrix}s_i&-1\\1&0\end{pmatrix},
\qquad P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
S_i=E_{ii}\otimes T_i+\sum_{j\ne i}E_{ji}\otimes P_0T_i
\in M_{2d}(A).
\]

Here $E_{ji}$ are the matrix units in $M_d(\mathbb C)$.
Let

\[
\mathbf e=\sum_{j=1}^d e_j,\qquad
p=(1\;\;0)(e_1^{\mathsf T}\otimes I_2),\qquad
q=(\mathbf e\otimes I_2)\binom10.
\]

Then $p$ is a scalar row, $q$ a scalar column, and

\[
U_v=pS^vq,\qquad S^{v_1\cdots v_m}=S_{v_1}\cdots S_{v_m}.
\]

The identity includes the empty word: $S^\Omega=I_{2d}$ and $pq=1$.

The local algebra check uses, for $k\geq1$,

\[
T_i^k=
\begin{pmatrix}
U_k(s_i)&-U_{k-1}(s_i)\\
U_{k-1}(s_i)&-U_{k-2}(s_i)
\end{pmatrix}.
\]

For a maximal-run decomposition $v=i_1^{k_1}\cdots i_r^{k_r}$, adjacent run letters differ.
Matrix-unit multiplication inserts $P_0$ between different runs, whereas powers within one run retain $T_i^k$.
Multiplying by $p$ and $q$ selects the product of the top-left Chebyshev entries, giving precisely $U_v$.
The run letters need not be pairwise distinct.
This verifies the matrix realization without replacing the nonmultiplicative map $X^v\mapsto U_v$ by an algebra homomorphism.

### Homogeneous Estimate: Lemma 3.5

For coefficients supported on words of length $m$, set

\[
h_m=\left(\sum_{|v|=m}|\alpha_v|^2\right)^{1/2}.
\]

The asserted inequality is

\[
\left\|\sum_{|v|=m}\alpha_vU_v\right\|\leq(m+1)h_m.
\]

A direct check of the displayed proof is as follows.
Define $L_u=\ell_{u_1}\cdots\ell_{u_k}$ and, for a word $v$, define $B_v=\ell_{v_1}^*\cdots\ell_{v_{|v|}}^*$.
Thus $B_v$ is not generally $L_v^*$: reversal is required.
For coefficients on a fixed word length,

\[
\left\|\sum_v b_vB_v\right\|
=\left(\sum_v|b_v|^2\right)^{1/2}.
\]

This follows by taking the adjoint, conjugating coefficients, reversing words, and using the orthogonal ranges of equal-length creation words.

The Wick normal form is

\[
U_{v_1\cdots v_m}
=\sum_{k=0}^{m}
\ell_{v_1}\cdots\ell_{v_k}
\ell_{v_{k+1}}^*\cdots\ell_{v_m}^*.
\]

Its form was checked by the recurrence $U_{iv}=s_iU_v-\delta_{i,v_1}U_{v_2\cdots v_m}$, together with the empty-word case.
This is also the normal form cited on p. 13 via Miy22's reference [5], Proposition 2.7.

Let

\[
F_k=\sum_{\substack{|u|=k\\|v|=m-k}}\alpha_{uv}L_uB_v.
\]

For any Fock vector $\xi$, orthogonality of the ranges of the $L_u$ gives

\[
\|F_k\xi\|^2
=\sum_{|u|=k}
\left\|\sum_{|v|=m-k}\alpha_{uv}B_v\xi\right\|^2
\leq h_m^2\|\xi\|^2.
\]

Summing the $m+1$ operators $F_k$ proves the inequality.
This argument also covers $k=0,m$ and avoids any dependence of the coefficient lengths on the tensor degree of $\xi$.

**Local source repair (pp. 13-14).**
After defining $F^{(k)}$ with coefficient-word lengths $k$ and $m-k$, the source prints ranges $k=0,\ldots,n$ and later uses $n-k$ in coefficient sums, although $n$ has become the input tensor degree.
These occurrences must be $m$ and $m-k$, respectively.
Taken literally, the displayed sums use coefficients outside the fixed degree under discussion.
The corrected estimate above proves the intended statement.

### Matrix Estimate: Lemma 3.6

For every $m\geq0$,

\[
\left\|\sum_{|v|=m}\alpha_vS^v\right\|
\leq4d^2(m+1)h_m.
\]

The constant and the endpoint-word bookkeeping were checked explicitly.
If $m\geq2$, the $(i,j)$ block of the matrix on the left is

\[
\begin{pmatrix}
\displaystyle\sum_{|w|=m-1}\alpha_{wj}U_{wj}
&
\displaystyle-\sum_{|w|=m-1}\alpha_{wj}U_w
\\[2mm]
\displaystyle\sum_{|w|=m-2}\alpha_{iwj}U_{wj}
&
\displaystyle-\sum_{|w|=m-2}\alpha_{iwj}U_w
\end{pmatrix}.
\]

Within each entry the retained coefficient indices are injectively drawn from the length-$m$ coefficients.
The four polynomial degrees are $m,m-1,m-1,m-2$.
Lemma 3.5 therefore bounds every scalar entry by $(m+1)h_m$.
There are $4d^2$ scalar matrix entries, and the corresponding scalar matrix units have norm one.
The triangle inequality yields exactly the stated bound.
For $m=0,1$, direct inspection of $I_{2d}$ and the displayed $S_i$ gives the same bound, using the degree-one case of Lemma 3.5.

**Local source repair (p. 15).**
The first displayed factorization separates the first and last runs as distinct factors.
It is valid when the number of runs is at least two, but that condition does not follow from $m\geq2$.
For a single run $v=i^m$, use directly

\[
T_i^m=
\begin{pmatrix}
U_{i^m}&-U_{i^{m-1}}\\
U_{i^{m-1}}&-U_{i^{m-2}}
\end{pmatrix},\qquad m\geq2.
\]

This proves the same endpoint-deletion formula and hence the same block entries and norm bound.
The source's first factorization, read literally with one run, duplicates that run and is false; its final block formula and Lemma 3.6 remain valid after this separate-case check.

### Rational Square-Summability Implies Norm Convergence: Corollary 3.7

Suppose

\[
\sum_v|\alpha_v|^2<\infty,\qquad
Z(X)=\sum_v\alpha_vX^v
\]

is a rational noncommutative formal series.
Define $a_m=\sum_{|v|=m}\alpha_vS^v$ and $b_m=h_m^2$.
By coefficientwise conjugation and the Hadamard product, the formal series with coefficients $|\alpha_v|^2$ is rational.
Sending every letter to the same formal variable $z$ gives the rational scalar series

\[
B(z)=\sum_{m\geq0}b_mz^m.
\]

This substitution is degree-preserving formal algebra, not substitution of operators at a point of unproved convergence.
Moreover, $\sum_m b_m<\infty$ implies $\sum_m b_m^2<\infty$.
Corollary 2.9, using the correction documented in [U002](Yin_U002.md#miy22-u002), supplies $M_0>0$ and $0<c<1$ with $b_m\leq M_0c^m$.
Therefore

\[
\|a_m\|\leq4d^2\sqrt{M_0}(m+1)(\sqrt c)^m,
\qquad
\sum_{m\geq0}\|a_m\|
\leq\frac{4d^2\sqrt{M_0}}{(1-\sqrt c)^2}<\infty.
\]

This proves the required operator-norm convergence.
It also proves norm convergence of the corresponding homogeneous sums in the $U_v$ basis, by Lemma 3.5 or by the fixed compression $p(\cdot)q$.

**Citation correction (p. 16).**
The bound with factor $4d^2$ uses Lemma 3.6.
The source calls it an application of Lemma 3.5.
This is a cross-reference error, not a change to the estimate.

### Verification Boundary and Reuse

The matrix identities, coefficient injections, numerical constant $4d^2$, small degrees, normal-form estimate, and exponential summability argument were checked mathematically as above.
No computational experiment or proof assistant was used for these units.

Miy22 credits the general Haagerup-type inequality to its reference [4], the Wick normal form to reference [5], and the convergence method to reference [10].
Those originals were not read in this subtask; the relevant full-Fock estimates were reconstructed here.
The formal-series equivalence remains the imported interface stated in U002.
No independent errata search was performed.

This unit provides norm-convergent evaluation at the special matrices $S_i$.
It does not authorize evaluation of an arbitrary formal rational series at arbitrary bounded operators, and square summability alone without rationality is not the stated convergence criterion.


## Source and inspection

[Source and edition notes](readme.md).

Source edition: Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here.

Passages: Lemma 3.4, pp. 11-12; Lemma 3.5, pp. 12-14; Lemma 3.6, pp. 14-15; Corollary 3.7, pp. 15-16.

Inspection: 2026-09-08: matrix realization, coefficient injections, degree cases, estimates and norm convergence reconstructed, with the shared independent U004-U005 cross-review linked here. Original references for general Haagerup estimates, Wick normal form and the convergence method were not read in this subtask; the relevant full-Fock estimates were reconstructed locally. Formal-series inputs retain U002's limits; no computation, proof assistant or independent errata search.
