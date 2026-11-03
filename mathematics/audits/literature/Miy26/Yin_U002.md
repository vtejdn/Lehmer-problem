---
author: Yin
---

<a id="miy26-u002"></a>
# Miy26-U002: Rational L2 Functions Are Bounded

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), arXiv:2603.19528v2, Theorem 1.1 and Section 3, Lemmas 3.1-3.4, pp. 1, 6-10.
- Record: 2026-09-08, the coordinating agent, local reconstruction for [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit).
- Kind and coverage: complete local proof chain of the main boundedness theorem, with its source-rate correction and explicit domain justifications.
  External and independent-review boundaries are stated below.

## Statement and conventions

Use finite $d\geq1$, the standard semicircular tuple, $M$, $D(s)$, $C_{\rm div}(s)$, and the canonical $L^2$ affiliated realization from [Miy26-U001](Yin_U001.md#miy26-u001).
Theorem 1.1 states

$$
D(s)\cap L^2(M,\tau)\subseteq M.
$$

Together with the Miy22 bounded-intersection interface and finiteness of the trace, it gives the exact equality

$$
D(s)\cap L^2(M,\tau)=D(s)\cap M=C_{\rm div}(s).
$$

This is about rational affiliated functions.
It does not assert that every square-integrable affiliated operator is bounded.
The proof actually constructs a norm-convergent homogeneous expansion in $C^*(s)$; this additional membership is part of the inspected source mechanism, not an identification of the full C*-algebra with the rational algebra.

## Lemma 3.1: Finite Defects on the Algebraic Core

Fix $f\in D(s)\cap L^2$ and write

$$
a=(1+ff^*)^{-1},\qquad b=(1+ff^*)^{-1}f.
$$

Positive affiliated functional calculus gives $a\in M$, $\ker a=0$, and $\|a\|\leq1$.
If $f=v|f|$ is its polar decomposition, then the closed product $b$ is $v|f|(1+|f|^2)^{-1}$, with norm at most $1/2$.
Star and inverse closure give $a,b\in D(s)$, because $1+ff^*$ has an affiliated inverse.
Consequently $a,b\in C_{\rm div}(s)$ by U001, and $[r_i^*,a]$, $[r_i^*,b]$ are bounded finite-rank operators.

For $\xi\in\mathcal F_{\rm alg}$, both $f\xi$ and $fr_i^*\xi$ are defined, since $r_i^*$ preserves that algebraic core.
The bounded product $b$ agrees with $af$ on $\operatorname{Dom}(f)$.
Expanding the three terms on this common domain gives

$$
[r_i^*,b]\xi
=a[r_i^*,f]\xi+[r_i^*,a]f\xi.
$$

Thus the image of $a[r_i^*,f]$ on $\mathcal F_{\rm alg}$ lies in the sum of two fixed finite-dimensional ranges.
Since $a$ is injective, the range of $[r_i^*,f]$ on that core is finite dimensional as well.
No bounded inverse of $a$ is needed; injective linear maps preserve the dimension of finite-dimensional preimages.
This proves Lemma 3.1 and avoids assuming that the unregularized commutator extends boundedly to all of Fock space.

## Extending the Coefficient Identity Without Assuming Boundedness

Write $f\Omega=\sum_w\alpha_we_w$ and let $f_N=\sum_{|w|\leq N}\alpha_wU_w$.
For every fixed word $v$,

$$
\|(f_N-f)U_v\|_2\leq\|U_v\|\,\|f_N-f\|_2\longrightarrow0.
$$

The analogous statement holds for the fixed polynomial vector $r_i^*e_v$.
Boundedness of $r_i^*$ then permits passage in each commutator column from the polynomial identity in U001.
The suffix coefficient restriction is an $\ell^2$ contraction, so the right side also converges.
The result is

$$
[r_i^*,f]e_v=\sum_u\alpha_{uiv^{\rm rev}}e_u.
\tag{1}
$$

This fills the domain-sensitive step compressed into the citation of Miy22 Lemma 3.3 on p. 6.
It uses convergence in $L^2$ for fixed right factors, not operator-norm convergence of the still-unproved bounded expansion.

Every nonempty suffix is $iv^{\rm rev}$.
Adding the empty suffix $f\Omega$ to the finite sum of the $d$ ranges in Lemma 3.1 shows that

$$
K'=\operatorname{span}\left\{\sum_u\alpha_{uv}e_u:v\in[d]^*\right\}
$$

is finite dimensional.
The empty suffix must be included separately; finite $d$ is used in summing the ranges.

## Lemma 3.2: Squared Coefficients Remain in a Finite Space

Let $g_i=\sum_u\beta_u^ie_u$, $1\leq i\leq k$, be a basis of $K'$.
For every $i,j$ the coefficient sequence $\beta^i\overline{\beta^j}$ lies in $\ell^1([d]^*)$ by Cauchy-Schwarz, hence also in $\ell^2$.
Set $g_{ij}=\sum_u\beta_u^i\overline{\beta_u^j}e_u$.

For a given suffix $v$, choose coefficients $c_i(v)$ with $\alpha_{uv}=\sum_i c_i(v)\beta_u^i$.
Then

$$
\sum_u|\alpha_{uv}|^2e_u
=\sum_{i,j}c_i(v)\overline{c_j(v)}g_{ij}.
$$

Therefore the squared-residual space $K$ is **contained** in the span of the $k^2$ vectors $g_{ij}$, and $\dim K\leq k^2$.
This containment is all the proof needs; there is no need to assert that every $g_{ij}$ lies in $K$.
The complex conjugates are present in the original rendered formula, although easily lost in text extraction.

The source's literal equality of spans can fail even for a bounded rational example.
For one generator and $0<q<1$, take $\alpha_n=q^n$ for even $n$ and $\alpha_n=iq^n$ for odd $n$.
Its residual space is spanned by $(q^n)$ and $((-q)^n)$, but every squared residual is a scalar multiple of $(q^{2n})$.
Thus $\dim K=1$, whereas the pair-product span has basis $(q^{2n})$, $((-q^2)^n)$ and dimension two.
The coefficient sequence is the linear combination with weights $(1+i)/2$ and $(1-i)/2$ of the Chebyshev generating series $(1-qs+q^2)^{-1}$ and $(1+qs+q^2)^{-1}$.
Both denominators are bounded below by $(1-q)^2$ on the semicircular spectrum.
This independently checked example justifies replacing equality by containment without changing the lemma's conclusion.

## Lemma 3.3: Finite Residual Sequences in c0 Decay Exponentially

The precise statement is: if $a=(a_n)_{n\geq0}\in c_0$ and the span $V$ of all left shifts $(a_{n+m})_{n\geq0}$ is finite dimensional, then there is a finite matrix realization $a_n=\lambda B^n\gamma$ and constants $M>0$, $0<A<1$ with $|a_n|\leq MA^n$.

Here is a shorter reconstruction of the source's spectral argument which also handles all degenerate cases.
Restrict the left shift $L$ to $V$.
Every $v\in V\subset c_0$ satisfies

$$
\|L^nv\|_\infty=\sup_{m\geq n}|v_m|\longrightarrow0.
$$

On the finite-dimensional space $V$, convergence on a basis implies operator-norm convergence $L^n\to0$.
Thus every eigenvalue of $L$ has modulus less than one.
Choosing a basis gives its matrix (or its transpose under the source's row-coordinate convention), an initial coordinate vector and empty-coordinate evaluation, producing $a_n=\lambda B^n\gamma$.
Jordan form, or a sufficiently small fixed power, yields an exponential bound for **any chosen** $A$ satisfying $r(B)<A<1$.
A zero sequence can be treated separately, and a nilpotent $B$ permits any $0<A<1$ after enlarging $M$.

**Source-rate error.**
On p. 9 the proof sets $A=\max_i|\lambda_i|$ itself.
A nontrivial Jordan block contributes powers of $n$, so this particular rate generally fails.
For example,

$$
a_n=(n+1)2^{-n}
$$

is in $c_0$, has two-dimensional shift span and eigenvalue $1/2$ with a Jordan block, but $a_n/(1/2)^n=n+1$ is unbounded.
Taking $1/2<A<1$ repairs the estimate.
The theorem's existential conclusion is correct; its printed final choice of the rate is not.
The source's occasional summation indices starting at zero for a basis numbered $1,\ldots,k$ are normalized here.

The source's longer minimal-row/column proof also correctly forces $r(B)<1$ before this erroneous endpoint choice.
Its reference to density in $c_0$ can be read simply as testing against every coordinate vector; no Hilbert-space inner product on all of $c_0$ is required.

## Lemma 3.4: Length Aggregation

Every squared residual lies in $\ell^1$.
Apply the bounded linear map

$$
T:\ell^1([d]^*)\to\ell^1(\mathbb N_0),
\qquad T(\beta)_n=\sum_{|u|=n}\beta_u
$$

to the finite-dimensional space $K$.
Put $a_n=\sum_{|w|=n}|\alpha_w|^2$.
For each $m$ the identity

$$
a_{n+m}=\sum_{|v|=m}\sum_{|u|=n}|\alpha_{uv}|^2
$$

shows that the $m$-shift of $a$ belongs to $T(K)$: every word of length $n+m$ has a unique last $m$ letters, and the outer sum has $d^m$ terms.
Since $a\in\ell^1\subset c_0$, repaired Lemma 3.3 applies and gives $a_n\leq MA^n$ for some $0<A<1$.
No exchange of conditionally convergent sums is used; all squared terms are nonnegative and the prescribed fixed-length sums are finite.

## Theorem 1.1: Construct the Bounded Operator and Identify It

The homogeneous bound from U001 yields

$$
\left\|\sum_{|w|=n}\alpha_wU_w\right\|
\leq(n+1)\sqrt{a_n}
\leq\sqrt M(n+1)(\sqrt A)^n.
$$

The scalar series on the right is summable, so the homogeneous series converges in operator norm to $g\in A\subseteq M$.
Applying the limit to $\Omega$ gives $g\Omega=f\Omega$, since the orthogonal homogeneous sums also converge in $L^2$.
The injectivity of the $L^2$ affiliated realization in U001 implies $f=g$.
Equivalently $\|f-g\|_2=0$ and faithfulness of the trace give equality of the affiliated operators.
Agreement on a single vector is justified by this canonical tracial model; it is not a general principle for arbitrary unbounded operators.

The proof thus establishes boundedness before invoking the bounded commutator characterization for $f$ itself.
It does not rely on Corollary 1.2, the circular spectral computations, or their conclusions.
The main chain is acyclic.

## Dependencies, Limits, and Verification

- U001 supplies the Fock and canonical affiliated realization, Miy22's bounded-intersection and finite-rank interfaces, and the homogeneous norm inequality with their recorded original-source boundaries.
  The regularization and domain extension here are local reconstructions.
- Lemmas 3.2-3.4 are finite-dimensional algebra and Banach-space arguments; no unaudited rational-series characterization is needed to pass from finite shifts to exponential decay in this proof.
- $L^2$ cannot simply be replaced by $L^1$.
  The source's endpoint examples and their exact integrability scope are in [Miy26-U003](Yin_U003.md#miy26-u003).
- The theorem does not establish equality between the spectrum and Brown-measure support for arbitrary rational functions; its spectral consequence is the $L^2$ criterion of U003.

The coordinating agent read pp. 6-10 and visually inspected the commutator, complex-conjugation, matrix, and final norm formulas on 2026-09-08.
The polynomial-to-$L^2$ extension, regularizer, finite-space arguments, corrected rate, and final operator equality were reconstructed as above.
On 2026-09-08, the separate spectral-interface reviewer checked the complete local chain against the source, including the span counterexample, all degenerate decay cases and the final affiliated identification; no unresolved local issue was found.
The integrated audit records the complete review scope.
No computation, formalization, or external human review is claimed for this unit.

## Source and inspection

Source edition: Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body.

Passages: Theorem 1.1 and Section 3, Lemmas 3.1-3.4, pp. 1, 6-10.

Inspection: 2026-09-08: the local regularization, residual, decay and boundedness chain was reconstructed and independently cross-reviewed, including explicit corrections and degenerate cases. Retained source interfaces keep their stated limits; no computation, formalization or external human review was claimed for this unit.
