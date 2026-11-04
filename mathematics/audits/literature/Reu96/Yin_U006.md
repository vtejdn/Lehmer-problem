---
author: Yin
---

# Scalar Extension and the Limits of the Language Analogy

## Reu96-U006

- Source: [Reu96](../../../literature/pdf/Reu96.pdf), the 17-page published journal article, Selecta Mathematica 2 (1996), 93-109.
- Locators: Sections 5.1-5.2, printed pp. 107-108 (PDF pp. 15-16); the relevant references are on printed pp. 108-109 (PDF pp. 16-17).
- Review: 2026-09-08, the source reconstruction agent; both concluding sections read, the example and change-of-basis matrices visually checked, and the algebraic proof reconstructed below.
  This is an internal mathematical source review, not formal verification.
- Purpose: supplies the field-sensitive example and the limits of the concluding claims for [Reu96 free-field source audit](readme.md#reu96-free-field-source-audit).

### Exact Claim and Conventions

For two freely noncommuting variables $x,y$, set

\[
f=\frac12(x+iy)^{-1}+\frac12(x-iy)^{-1}
\]

in the free field over $\mathbb C$.
The same element lies in the embedded real free field and satisfies

\[
f=(x+yx^{-1}y)^{-1}.
\]

Its inversion height is exactly one relative to $\mathbb C\langle x,y\rangle$ and exactly two relative to $\mathbb R\langle x,y\rangle$.
Thus height may decrease after extension of the coefficient field.
A source phrase on printed p. 107 gives the height-one base as the complex free field itself; the mathematically intended base is the complex free polynomial algebra, as dictated by the definition of height and the example.

All complex scalar coefficients, including $i$, commute with $x,y$ in the complex free algebra.
The later auxiliary division ring $D$ need not commute with the variables: its correct polynomial setting is a free tensor ring over its center.
Coefficient order is preserved below.

### Dependencies and Inspection Boundary

| Input | Role and inspection depth |
| --- | --- |
| [U001](Yin_U001.md#reu96-u001) | Fullness, universal free fields, scalar extension, and minimal representations. |
| [U004](Yin_U004.md#reu96-u004) | Theorem 2.2 applied over the auxiliary division ring to a hypothetical height-one expression. |
| [U005](Yin_U005.md#reu96-u005) | The constant-entry consequence of a height structure; the coefficient-extension and minimal-equivalence interfaces also used there. |
| Reu96 reference [7], P. M. Cohn, *Free Rings and their Relations*, 1985 edition, Exercise 3 on p. 502 | The source cites this for a division ring $D$ containing $\mathbb R$ centrally, infinite-dimensional over its center, with no square root of $-1$. The exercise and its construction were not directly inspected in this unit. This is an explicitly retained, secondary-reported existence input. |
| [CR94-U001](../CR94/Yin_U001.md#cr94-u001), Theorem 3.2, Corollary 4.2, and Theorem 4.1 | Comparison embedding over the center, minimality from independent families, and equivalence of minimal representations. Exact primary statements and applicability were checked by the CR94 reviewer and accepted, with original proofs unreviewed. The free-field interfaces assume finite $X$, $k=Z(D)$, infinite $k$, and $[D:k]=\infty$. |

If $k=Z(D)$, then $\mathbb R\subseteq k$, so $k$ is automatically infinite.
The additional requirement $[D:k]=\infty$ is necessary for the stated Theorem 2.2.
The assertion that $D$ has no square root of $-1$ is stronger than merely saying $i\notin k$.

If $\mathbb R\subseteq k$ is proper, the initial embedding under this commutative scalar extension still uses the secondary-reported coefficient-extension input recorded in U005.
CR94's checked comparison embedding then applies from the scalar free field over $k$ to the free tensor field over $D$; its scope is not arbitrary change of coefficient rings.

### Direct Check of the Complex-to-Real Representation

Write

\[
B=\begin{pmatrix}x+iy&0\\0&x-iy\end{pmatrix},
\quad
Q=\begin{pmatrix}1&1\\i&-i\end{pmatrix},
\quad
P=Q^{-1}=
\begin{pmatrix}
\frac12&\frac1{2i}\\
\frac12&-\frac1{2i}
\end{pmatrix}.
\]

The rendered display has entries $1/(2i)$; it must not be read as $i/2$.
Direct multiplication gives

\[
QBP=A:=\begin{pmatrix}x&y\\-y&x\end{pmatrix},
\qquad
(1,1)P=(1,0),
\qquad
Q\binom{1/2}{1/2}=\binom10.
\]

Consequently

\[
f=e_1^{\mathsf T}A^{-1}e_1.
\]

The matrix $A$ is full over the real free algebra and over each auxiliary free tensor ring used below: its polynomial evaluation at $x=1,y=0$ is $I_2$, which rules out a factorization through a one-dimensional intermediate space.
The lower-right entry $x$ is nonzero.
Its Schur complement is

\[
s=x-yx^{-1}(-y)=x+yx^{-1}y\neq0,
\]

so the block inverse formula yields $f=s^{-1}$.
This proves the asserted real expression and the real height upper bound two.

The displayed complex expression gives height at most one.
It is not a polynomial.
Indeed, put $p=x+iy$ and $q=x-iy$; this invertible complex linear substitution gives two free variables.
If $f$ were a polynomial in them, the identity

\[
pfq=\frac12(q+p)
\]

would equate a polynomial all of whose words have length at least two with a nonzero polynomial homogeneous of length one.
Thus the complex height is exactly one.
This proof does not evaluate any rational expression at a possible pole.

### Why the Real Representation Stays Minimal over the Auxiliary Ring

It is insufficient to infer minimality over $D$ merely from a representation over $\mathbb C$, since the chosen $D$ has no square root of $-1$.
Instead, check both families directly in the universal field of $D*_{k}k\langle x,y\rangle$.

Let

\[
s=A^{-1}e_1=\binom{s_1}{s_2},
\qquad
t=e_1^{\mathsf T}A^{-1}=(t_1,t_2).
\]

The equations $As=e_1$ and $tA=e_1^{\mathsf T}$ give

\[
s_2=x^{-1}ys_1,\qquad s_1\neq0;
\qquad
t_2=-t_1yx^{-1},\qquad t_1\neq0.
\]

A left $D$-linear dependence $a s_1+b s_2=0$ implies

\[
a+b x^{-1}y=0.
\]

If $b\neq0$, this would make $x^{-1}y=-b^{-1}a\in D$, and hence equate $y$ to $x$ times a constant.
This contradicts the independent degree-one $x$ and $y$ summands of the free tensor ring.
If $b=0$, then $a=0$.

Similarly, a right dependence $t_1a+t_2b=0$ gives $a-yx^{-1}b=0$.
If $b\neq0$, then $yx^{-1}=ab^{-1}\in D$, again contradicting the independent variables after multiplication on the right by $x$; if $b=0$, then $a=0$.
Both families are therefore independent.
The minimality criterion from [10, Corollary 4.2] applies to the size-two representation $(e_1^{\mathsf T},A,e_1)$ over $D$.

### The Lower Bound over the Reals

Assume that $f$ has real height at most one.
By the retained coefficient-extension embedding, its image in the free tensor field over the specified $D$ also has height at most one.
Theorem 2.2 and minimal equivalence then give invertible matrices $P,Q\in\mathrm{GL}_2(D)$ for which $QAP$ has a height structure with values in $\{0,1\}$.

Such a matrix has a constant entry.
If a height value is zero, its diagonal entry is one.
If both height values are one, (2.2) makes the upper-right entry zero.
Independently permuting rows and columns lets us place this constant entry in position $(1,1)$, still using invertible constant matrices on both sides.

Write the relevant row of $Q$ as $(a,b)$ and the relevant column of $P$ as $(\alpha,\gamma)^{\mathsf T}$.
For a constant $u\in D$ the resulting equality is

\[
u=ax\alpha-by\alpha+ay\gamma+bx\gamma.
\]

The grading first gives $u=0$, and the separate variable summands give

\[
ax\alpha+bx\gamma=0,\qquad -by\alpha+ay\gamma=0.
\]

Applying the polynomial substitution $x=1$ to the first equality and $y=1$ to the second gives the necessary equalities

\[
a\alpha+b\gamma=0,\qquad -b\alpha+a\gamma=0.
\]

Only implications from polynomial identities to these scalar identities are used; arbitrary scalar evaluation is not being used to establish a rational identity.

If $a\neq0$, the first equality gives $\alpha=-a^{-1}b\gamma$.
The second becomes

\[
(ba^{-1}b+a)\gamma=0.
\]

The column $(\alpha,\gamma)^{\mathsf T}$ is nonzero, so $\gamma\neq0$.
Right cancellation of $\gamma$ and multiplication on the right by $a^{-1}$ therefore yield

\[
(ba^{-1})^2+1=0,
\]

contrary to the choice of $D$.
If $a=0$, the row being nonzero gives $b\neq0$, and the two scalar equations force $\gamma=\alpha=0$, contradicting the nonzero column.
Thus no constant entry exists, and real height at most one is impossible.
Combined with the displayed height-two expression, this proves the claimed real height.

### What Section 5.2 Does and Does Not Establish

The source compares the generic-matrix theorem with star-height results for regular languages.
It explicitly states that the corresponding Boolean results do not logically imply its field/series results.
In particular, the minimal-representation height characterization and the stable-subspace Lemma 3.4 do not transfer directly to minimal deterministic automata.

The statements about a complete directed graph's path language and differing cycle ranks of left and right minimal automata are reports attributed to the source's references [21], [5, Corollary 6.1], and [6, p. 270].
Those Boolean results and their exact language/automaton conventions were not independently checked here; they are not needed for the algebraic example above.

The following concluding passages are suggestions or conjectural comments within Reu96, not theorems proved in this article:

- Languages for which both minimal automata have cycle rank strictly larger than the language's star height.
- Arbitrarily large inversion height in a free field on two variables.
- Computing inversion height, including the source's proposed setting of an algebraically closed ground field.

This classification concerns the content of Reu96 in 1996.
It makes no claim about whether these problems have subsequently been solved.
The cited decidability result for language star height is not an algorithm for free-field inversion height.

### Corrections, Verification Facts, and Reuse Limits

The matrix conversion, Schur complement, complex nonpolynomial argument, minimality after extension to $D$, height-one constant-entry alternative, and every cancellation in the no-square-root argument were checked algebraically.
In particular, the proof preserves $ba^{-1}$ rather than silently replacing it by $a^{-1}b$.

The source's phrase on printed p. 107 describing height one relative to the complex free field itself must be corrected to the complex free polynomial algebra.
Its statement that height over $D$ is one only needs the weaker conclusion “at most one” in the contradiction argument; equality is not assumed from scalar extension.
The compressed minimality step is supplied above.

No script or proof assistant was run for this unit.
No original proof of the auxiliary-division-ring existence statement or the imported normal-form theorem was reviewed, and no independent search for later developments or errata was performed.
The real lower-bound proof is reconstructed subject to those declared interfaces and U004; the existence input must remain visible when reusing it.

The example proves a strict decrease for this element under $\mathbb R\subset\mathbb C$.
It does not assert that every extension decreases height, that algebraic closure preserves height, or that language algorithms compute inversion height.
No new project claim beyond the source-audit goal is introduced here.

On 2026-09-08, the CR94 comparison and minimal-representation interfaces were updated to the primary statement and applicability checks in CR94-U001.
Their original proofs remain unreviewed, and the auxiliary-division-ring existence input and arbitrary commutative scalar-extension input retain their separate limits.

Independent review, 2026-09-08: the separate reviewing agent compared the example with rendered Reu96 pp. 107-108.
It verified the signs in $QBP$, the polynomial-degree obstruction, minimality over the chosen $D$ without assuming an embedding of $\mathbb C$, and both cancellation cases leading to the no-square-root contradiction.
No additional local gap was found; this does not verify the external existence construction.

## Exact passage and inspection limits


Passages: Sections 5.1-5.2, printed pp. 107-108 / PDF pp. 15-16; relevant references, printed pp. 108-109 / PDF pp. 16-17.

Inspection: 2026-09-08: real/complex conversion, minimality and lower-bound contradiction reconstructed and independently reviewed. Auxiliary-division-ring existence and scalar-extension inputs retain separate unreviewed original-proof limits; CR94 primary checks do not remove them. Boolean language reports and later status of concluding problems were not independently checked. No height algorithm, new project theorem or formal verification.
