---
author: Yin
---

# Analytic Realization and Inverse Closures

Source: [DR97](../../../literature/pdf/DR97.pdf), the registered ten-page published journal version.
The source-unit order below follows the logical dependency: the analytic realization supplies the difficult inclusion in the closure theorem.

Review record: 2026-09-08, the analytic reconstruction agent.
Extracted text and original rendered pages were inspected for printed pp. 618-621 (PDF pp. 6-9); the definitions and representation conventions on pp. 613-617 were also read.
The arguments below reconstruct all local steps of Section 3 under the explicit finite-generator hypothesis.
They are an internal mathematical review, not formal verification or external peer review.
Independent cross-review and any subsequent changes are recorded under revisions.


This source analysis comprises [U004](#dr97-u004), [U003](Yin_U003.md#dr97-u003).
Its [shared source, inspection and setting](#analytic-realization-and-inverse-closures) and [joint review dated 2026-09-08](Yin_U003.md#verification-facts-and-revisions-for-u003-u004) retain their original scopes.

<a id="dr97-u004"></a>
## DR97-U004: Rational Square-Summable Series and Scalar Inverse Realization

- **Kind and locators:** Lemmas 10-11 and Proposition 9, Section 3.2, printed pp. 619-621 / PDF pp. 7-9.
- **Intended use:** [DR97 rational-series source audit](readme.md#dr97-rational-series-source-audit); the reverse inclusion in [DR97-U003](Yin_U003.md#dr97-u003).
- **Assessment:** Audited within scope: statements checked and local proof reconstructed and independently cross-reviewed with the corrections below.
  The homogeneous Haagerup estimate is a primary-statement-checked external input from [DR97-U005](Yin_U005.md#dr97-u005), whose original proof is not re-audited here.

### Statements and Conventions

Let $X$ be a **finite** set, $\Gamma=F(X)$, and $A=X\sqcup\bar X$ the alphabet with inverse letters.
Write $s:A^*\to\Gamma$ for group evaluation and $m:\Gamma\to\operatorname{red}(X)\subset A^*$ for the reduced-word section.
Formal word-series multiplication is concatenation; group multiplication reduces words.
A series supported on reduced words can be transported coefficientwise by $s$, but $s$ is not defined on an arbitrary infinite word series by an unrestricted infinite sum over all preimages.

For $a=(a_g)_{g\in\Gamma}\in\ell^2(\Gamma)$ put

\[
S=m(a)=\sum_{g\in\Gamma}a_gm(g),\qquad
a_m=\sum_{|g|=m}a_g\lambda(g).
\]

Each $a_m$ is a finite group polynomial because $X$ is finite.
Here $\lambda$ denotes the left regular representation, $\|a\|_2^2=\sum_g|a_g|^2$, and unadorned operator norms are norms in $C_r^*(\Gamma)$.
The source's initial definition on p. 613 omits the square root in the displayed Hilbert norm; the conventional norm above is used throughout this audit.

**Lemma 10, precise form.**
If $S$ is a rational/recognizable word series, then $\sum_{m\geq0}\|a_m\|<\infty$.
Its sum $b\in C_r^*(\Gamma)$ satisfies $b\delta_e=a$, and agrees with convolution by $a$ on finitely supported vectors.
For every polynomial shift

\[
T=P\circ S\circ Q,\qquad (T,w)=(S,QwP),
\]

the reduced-support series $T$ has $s(T)\in\ell^2(\Gamma)$ and defines an element of $C_r^*(\Gamma)$ by the same procedure.

**Lemma 11, precise form.**
Let $\mathcal B$ be a unital real or complex Banach algebra and let $x\in M_n(\mathcal B)$, $n\geq1$.
If $x^m\to0$ in the product topology, then $\sum_m x^m$ converges absolutely in any compatible Banach matrix norm to $(I-x)^{-1}$.
Every entry of this inverse belongs to the smallest unital subalgebra of $\mathcal B$ containing the entries of $x$ and closed under inversion of its elements that are invertible in $\mathcal B$.
This is **scalar inverse closure**, not merely matrix inverse closure.

**Proposition 9.**
Under the hypotheses of Lemma 10, the bounded convolution operator associated to $a$ lies in the scalar inverse closure $R_1$ of $\mathbb C\Gamma$ inside $C_r^*(\Gamma)$.

The word-rationality notion and minimal-representation interface are those of [DR97-U001](Yin_U001.md#dr97-u001).
The case $S=0$ is immediate and can be removed before choosing a nonzero-dimensional minimal representation.
If $X=\varnothing$, then $\Gamma=\{e\}$ and all conclusions reduce to scalar identities.

### Lemma 10(i): Decay and the Bounded Operator

Set $b_m=\sum_{|g|=m}|a_g|^2$.
Coefficient conjugation and the Hadamard product preserve recognizability, so $S\odot\bar S$ is rational.
Because the alphabet is finite, substituting every letter by a commuting variable $t$ gives the rational scalar series

\[
E(t)=\sum_{m\geq0}b_mt^m.
\]

This can also be seen directly from a representation $(\lambda_0,\mu,\gamma)$ of $S$:

\[
E(t)=(\lambda_0\otimes\bar\lambda_0)
\left(I-t\sum_{x\in A}\mu(x)\otimes\bar\mu(x)\right)^{-1}
(\gamma\otimes\bar\gamma).
\]

The notation $\lambda_0$ distinguishes the scalar representation row from the regular group representation.
Since $\sum_m b_m=\|a\|_2^2<\infty$, the power series converges absolutely and uniformly on $|t|\leq1$.
The reduced rational function representing $E$ therefore has no pole in the closed unit disk: there are no interior poles by analyticity, and a boundary pole would make the function unbounded along an interior radial approach, contradicting the uniform bound.
Choose $R>1$ with no pole on or inside $|t|=R$.
Cauchy's coefficient estimate gives constants $M>0$ and $0<c=R^{-1}<1$ such that

\[
b_m\leq Mc^m.
\]

If $E$ is a polynomial, any sufficiently chosen $R>1$ works.
This reconstruction supplies the precise rational-series decay step attributed on p. 620 to Kronecker through Connes; it does not require accepting that secondary citation as an unresolved extra theorem.

The homogeneous Haagerup inequality gives

\[
\|a_m\|\leq(m+1)\sqrt{b_m}
\leq\sqrt M\,(m+1)c^{m/2}.
\]

The numerical series on the right is summable.
Consequently $B=\sum_m a_m$ exists in $C_r^*(\Gamma)$.
Evaluation at $\delta_e$ is continuous, so $B\delta_e=a$.
The operators $a_m$ commute with right translations; therefore their limit does too, and $B\delta_g$ is exactly the right translate of the coefficient vector $a$ required by convolution on a basis vector.
Linearity identifies $B$ with convolution by $a$ on $\mathbb C\Gamma$.

This is the point where boundedness is established.
The assertions on pp. 613 and 619 that **every** $\ell^2$ coefficient function already belongs to $\operatorname{End}(\ell^2)$ by convolution are not valid.
Before this argument, only the map $\mathbb C\Gamma\to\ell^2(\Gamma)$ is justified.
For instance, in $\Gamma=\mathbb Z$, the coefficients $a_n=(n+1)^{-3/4}$ for $n\geq0$, and $a_n=0$ otherwise, are square summable.
If convolution had a bounded extension of norm $K$, its matrix quadratic form on $N^{-1/2}\sum_{j=0}^{N-1}\delta_j$ would be bounded by $K$, whereas it equals

\[
\sum_{k=0}^{N-1}(1-k/N)(k+1)^{-3/4},
\]

which tends to infinity.
It also fails to define an everywhere $\ell^2$-valued convolution map: for the input vector $a$ itself,

\[
(a*a)_n=\sum_{j=0}^n(j+1)^{-3/4}(n-j+1)^{-3/4}
\geq(n+1)^{-1/2}\qquad(n\geq0),
\]

so $a*a\notin\ell^2(\mathbb Z)$.
This elementary counterexample checks both failed implications independently of Fourier-transform conventions.
It is not rational and does not contradict Lemma 10.

**Rate correction.**
The source keeps the same symbols in $b_m\leq Mc^m$ and an operator bound of the form $M(1+m)^kc^m$.
The justified direct bound has $\sqrt M$ and $c^{m/2}$; one may rename $\sqrt c$ as a new decay constant.
No change to the convergence conclusion is needed, but carrying the original $c$ into the operator estimate without justification is invalid.

### Lemma 10(ii): Polynomial Shifts

For words $u,v$, the map $w\mapsto vwu$ is injective in the free monoid, so

\[
\|u\circ S\circ v\|_{\ell^2(A^*)}^2
=\sum_w|(S,vwu)|^2\leq\|S\|_{\ell^2(A^*)}^2.
\]

If $w$ is not reduced, neither is $vwu$; thus every shift of a reduced-support series remains supported on reduced words.
Transport by $s$ is then an isometry for coefficient $\ell^2$ norms.
Writing $P=\sum_u p_u u$ and $Q=\sum_v q_v v$ and using the triangle inequality yields

\[
\|s(P\circ S\circ Q)\|_2
\leq\left(\sum_u|p_u|\right)
\left(\sum_v|q_v|\right)\|a\|_2.
\]

The printed contraction bound for **every** shift is false because the definition includes polynomials: $P=2$, $Q=1$, and any nonzero $S$ already contradict it.
The word-shift contraction and the displayed finite constant repair the argument.
Shifts preserve recognizability directly by changing the initial row and terminal column of a representation.
Apply part (i) to the rational **word series $T$**, supported on reduced words.
The phrase on p. 620 that "$s(T)$ is rational" should not be used to assume the desired rational closure conclusion before proving Proposition 9.

### Lemma 11: Decaying Powers and Scalar Inverses

Choose a submultiplicative matrix norm defining the product topology.
There is $q\geq1$ with $\|x^q\|<1$.
For $m=kq+r$, $0\leq r<q$,

\[
\|x^m\|\leq\|x^q\|^k\|x^r\|.
\]

Summing over $k,r$ proves absolute convergence.
Multiplying finite geometric sums by $I-x$ on either side and taking limits proves that their sum is $(I-x)^{-1}$.
The limit assumption thus supplies the geometric bound; completeness alone, as the compressed printed argument might suggest, would not suffice.

For the scalar rationality assertion, choose an equivalent submultiplicative norm on $\mathcal B$ with $\|1\|=1$; the left-multiplication operator norm provides such a normalization.
The zero algebra is immediate.
Put $y=x^q$ with $q$ large enough that every entry of $y$ has norm below $1/(2n)$.
A direct elimination argument proves that $(I-y)^{-1}$ is obtainable using only scalar inverses in $\mathcal B$ and ring operations.
At any stage, suppose the remaining matrix is $I-z$ with entries bounded by $r<1$.
Its first pivot $p=1-z_{11}$ is invertible by the scalar Neumann series, with $\|p^{-1}\|\leq(1-r)^{-1}$.
The Schur complement is $I-z'$ where

\[
z'_{ij}=z_{ij}+z_{i1}p^{-1}z_{1j},\qquad i,j>1,
\]

and each entry has norm at most $r+r^2/(1-r)=r/(1-r)$.
Starting with $r_0=1/(2n)$, the successive bounds are $r_k=1/(2n-k)<1$ for all required $0\leq k\leq n-1$.
Hence every scalar pivot is invertible.
Inductive block inversion expresses all inverse entries through these pivots; every expression belongs to the scalar inverse closure of the entries of $y$, and hence of the entries of $x$.
Finally,

\[
(I-x)^{-1}=(I-x^q)^{-1}(I+x+\cdots+x^{q-1}).
\]

The identity is valid in the noncommutative matrix algebra: the polynomial factors commute with $x$, and direct multiplication by $I-x$ gives the identity.
This finishes the scalar, not only matrix, closure assertion.

For comparison with the p. 620 display, for compatible blocks $a_{ij}$ the corrected formulas are

\[
\begin{aligned}
A_{11}&=(1-a_{11}-a_{12}(I-a_{22})^{-1}a_{21})^{-1},\\
A_{22}&=(I-a_{22}-a_{21}(1-a_{11})^{-1}a_{12})^{-1},\\
A_{12}&=(1-a_{11})^{-1}a_{12}A_{22},\\
A_{21}&=(I-a_{22})^{-1}a_{21}A_{11}.
\end{aligned}
\]

All displayed inverses must exist; choosing a sufficiently small power supplies this condition.
The diagonal formulas in the original rendered page have misplaced parentheses around the inverse exponent and are not the correct Schur formulas read literally.
Setting all $a_{ij}=0$ already exposes the problem with an inverse applied to the inner sum.
The formulas above put the inverse around the whole Schur complement, preserve factor order, and follow by multiplying the block matrices.
The elimination proof avoids treating the $(n-1)\times(n-1)$ inverse as if its entries automatically belonged to scalar inverse closure.

### Proposition 9: Why Minimality Prevents Group Cancellations

Take a minimal representation $(\lambda_0,\mu,\gamma)$ of nonzero $S$, of dimension $n$.
Minimality gives both reachable-row and observable-column spanning.
Consequently, for each pair $i,j$, there are finitely supported scalars $c_{iv},d_{uj}$ such that

\[
e_i^{\mathsf T}=\sum_v c_{iv}\lambda_0\mu(v),\qquad
e_j=\sum_u d_{uj}\mu(u)\gamma,
\]

and therefore

\[
(\mu(w))_{ij}=\sum_{v,u}c_{iv}d_{uj}(S,vwu).
\tag{*}
\]

This is the coefficient-shift identity actually needed from Theorem 4, without imposing an unjustified special choice of representation basis.
Define

\[
S_{ij}=\sum_{w\in A^*}(\mu(w))_{ij}w.
\]

Equation (*) makes each $S_{ij}$ a finite linear combination of polynomial shifts of $S$.
It is rational, belongs coefficientwise to $\ell^2$, and is supported on reduced words.
In particular,

\[
\mu(w)=0\quad\text{for every nonreduced word }w.
\]

This strong statement uses minimality; hidden states of a nonminimal representation need not have it.
It is the precise reason no shorter-length terms survive cancellation after evaluating words in the group.

Put

\[
U=\sum_{x\in A}\mu(x)x,\qquad
V=\sum_{x\in A}\mu(x)\lambda(s(x))\in M_n(\mathbb C\Gamma).
\]

For each integer $m\geq0$, multiplication involves only finite polynomials, so

\[
V^m=s(U^m)
=s\left(\sum_{\substack{|w|=m\\w\text{ reduced}}}\mu(w)w\right).
\]

Thus $(V^m)_{ij}$ is exactly the degree-$m$ group homogeneous part of $s(S_{ij})$.
Lemma 10(i), applied entrywise, gives

\[
\sum_{m\geq0}\|(V^m)_{ij}\|<\infty;
\qquad V^m\longrightarrow0.
\]

The final sentence on p. 620 should cite **Lemma 10(i)** for this inference; Lemma 11(i) is about the matrix geometric series after decay has been obtained.
No circular use of Lemma 11 is needed.

Lemma 11 now shows that $(I-V)^{-1}$ exists and its entries belong to $R_1$.
Coefficientwise on reduced words, the norm-convergent geometric series agrees with $s(\sum_m U^m)$: each coefficient is eventually constant in the partial sums, and Fourier coefficient evaluation is continuous in operator norm.
Hence

\[
a=\lambda_0(I-V)^{-1}\gamma\in R_1.
\]

This notation identifies the original coefficient vector with its established bounded convolution operator.
It is not an application of an unrestricted homomorphism from all formal word series to operators.

### Dependencies, Limits, and Verification Facts

- [DR97-U001](Yin_U001.md#dr97-u001) supplies recognizability, shifts, and the correct minimal-representation interface.
  The shift identity was also reconstructed explicitly in (*).
  The displayed proof of scalar decay above replaces dependence on a secondary Kronecker attribution.
- [DR97-U005](Yin_U005.md#dr97-u005) supplies the accepted homogeneous Haagerup estimate with its original-source locator and proof-review boundary.
  Finite dimensional matrix algebra, elementary Banach-algebra arguments, and Cauchy's estimate are retained standard infrastructure.
- Finite $X$ ensures finite homogeneous group polynomials and a finite letter sum in the rational scalar specialization.
  No unrestricted infinite-alphabet extension is claimed here.
- Absolute convergence means $\sum_m\|a_m\|<\infty$, grouped by word length.
  It does not assert $\sum_g|a_g|<\infty$, nor absolute operator-norm summability of every individual group term.
- On 2026-09-08 the original formulas on pp. 619-621 were checked visually; proof steps and boundary examples were derived as written above.
  No mathematical software computation, proof-assistant check, exhaustive errata search, or human review was performed by this subagent.
  Source-search evidence and primary dependencies are kept in U005 rather than duplicated here.


## Source and inspection

Source edition: DR97, the retained ten-page published Inventiones mathematicae 128 (1997), pp. 613-622, DOI 10.1007/s002220050154. Printed page equals PDF page plus 612. The separately retained 14-page author typeset version has an unstated preparation/revision date and was compared only at the selected passages recorded in U005; it does not replace the primary version.

Passages: Lemmas 10-11 and Proposition 9, Section 3.2, printed pp. 619-621 / PDF pp. 7-9.

Inspection: 2026-09-08: decay, shifts, minimality, Banach inversion and scalar realization reconstructed and independently reviewed under finite generators; shared U003-U004 revisions are linked. Boundedness precedes inversion. U005 supplies only the accepted primary-statement Haagerup estimate, not a fresh proof audit. No arbitrary alphabet/formal substitution, exhaustive errata search, computation or formal verification.
