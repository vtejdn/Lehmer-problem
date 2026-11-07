---
author: Yin
---

# Yin20: Evaluation Consistency, Schur Complements, and the Two Closures

<a id="yin20-u004"></a>
## Yin20-U004: Sections IV.4-IV.5

- Source: [Yin20](../../../literature/pdf/Yin20.pdf), supplied 109-page dissertation.
- Date and reviewer: 2026-09-10; the evaluation-and-closure agent, complete local reconstruction and author self-check of this unit, submitted for separate cross-review.
- Primary coverage: printed pp. 56-61 / PDF pp. 66-71, from the start of IV.4 through the end of IV.5.
  PDF p. 72, the unnumbered blank verso corresponding to printed p. 62, was also inspected.
- Boundary coverage: Algorithm IV.3.4 on printed p. 56 is read because IV.4-IV.5 explicitly reuse its arithmetic formulas.
  Definition IV.3.1, Theorem IV.3.2, Definition IV.3.3, and the preceding rank-preserving embedding statement on printed pp. 54-55 were read for their exact input conventions.
  Proposition III.1.6 on printed p. 39 was checked for its invertible-pivot hypothesis.
- Existing record: [Yin20-U001](Yin_U001.md#yin20-u001), the earlier targeted division-closure reading, is preserved unchanged.
- Verification depth: all local proofs and omitted algebra needed for the statements below are reconstructed; the retained general free-field foundations are explicitly identified.
  No complete original-source proof audit of Cohn, HMS18, or the dissertation's other cited works is claimed.

## 1. Statement and Page Map

Use $R=\mathbb C\langle x_1,\ldots,x_d\rangle$ for the free polynomial algebra, $\mathbb F$ for its free field, $\mathcal B$ for a nonzero unital complex ambient algebra, and $X\in\mathcal B^d$.
Subalgebras in this unit share the ambient identity.
Write $\rho_{\mathcal B}$ for inner rank over $\mathcal B$.
A representation $r=uA^{-1}v$ has a full square matrix $A$ over $R$ and constant scalar row and column vectors $u,v$.
The matrix need not be affine linear in Theorem IV.4.1.

| Source item | Printed / PDF pages | Exact content and disposition |
| --- | --- | --- |
| Algorithm IV.3.4, boundary interface | 56 / 66 | Scalar, variable, sum and product representations are valid; the inverse formula needs the sign correction in Section 2 below |
| Opening counterexample | 56-57 / 66-67 | Infinite unilateral shifts show that rational-function evaluation cannot be representation independent in every unital algebra |
| Theorem IV.4.1 and Definition IV.4.2 | 57-58 / 67-68 | Evaluation is well-defined on the union of representation domains in a stably finite ambient algebra; the polynomial-rank step needs the intermediate free-field computation in Section 3 |
| Polynomial and arithmetic compatibility | 58 / 68 | Holds on the respective domains, using the corrected representation arithmetic |
| Definition IV.5.1 and Lemma IV.5.2 | 58-59 / 68-69 | Matrix rational closure is a unital subalgebra containing the polynomial image; the source cites its proof, reconstructed here by triangular matrices |
| Remark IV.5.3 | 59 / 69 | In a stably finite ambient algebra, matrix rational closure equals the set of evaluations whose representation matrices are invertible in that ambient algebra |
| Reciprocal formula and Lemma IV.5.4 | 59-60 / 69-70 | Rational closure is inverse closed; the reciprocal formula has the same missing minus sign, while the Schur invertibility lemma is correct |
| Definition IV.5.5 and Remark IV.5.6 | 60 / 70 | Division closure, its containment in rational closure, its equality with the free field in the free-field ambient, and its recursive construction |
| Proposition IV.5.7 and Lemma IV.5.8 | 61 / 71 | If either closure is a division ring, the closures agree; matrices over a unital division subring are inverse closed in the same matrix ambient |
| Final contextual remark | 61 / 71 | The von Neumann regular generalization is verified against a selected primary Reich passage, with its version-dependent locator corrected in Section 6.4 |

## 2. Representation Arithmetic and the Inverse Sign

The source's convention is $r=uA^{-1}v$, with a plus sign, in both Definitions IV.3.1 and IV.3.3.
This matters because its description preceding Definition IV.3.3 explicitly changes a sign relative to the cited representation convention.

For a scalar or a variable $a$, the matrix

\[
Q_a=\begin{pmatrix}-a&1\\1&0\end{pmatrix},\qquad
Q_a^{-1}=\begin{pmatrix}0&1\\1&a\end{pmatrix}
\tag{1}
\]

is invertible over every unital ambient algebra.
Its lower-right inverse entry is $a$, verifying the two base rules of Algorithm IV.3.4.
The block-diagonal rule evaluates to the sum of the represented elements.

The printed product matrix, with block columns of sizes $n_2,n_1$, is

\[
Q=\begin{pmatrix}-v_1u_2&A_1\\A_2&0\end{pmatrix},
\qquad u=(0,u_1),\qquad v=\binom0{v_2}.
\tag{2}
\]

When $A_1,A_2$ are invertible in their matrix ambient, solving $Q\binom{x}{y}=\binom0{v_2}$ gives $x=A_2^{-1}v_2$ and $y=A_1^{-1}v_1u_2A_2^{-1}v_2$.
Column permutation makes $Q$ block triangular with invertible diagonal, so $Q$ is invertible there.
Consequently $uQ^{-1}v=r_1r_2$, with all noncommutative orders as printed.

For inversion, put

\[
L=\begin{pmatrix}0&u\\v&A\end{pmatrix}.
\]

If $A$ and $r=uA^{-1}v$ are invertible in the relevant ambient, the Schur complement of $A$ is $-r$.
Therefore

\[
e_1^{\mathsf T}L^{-1}e_1=-r^{-1},
\qquad
r^{-1}=-e_1^{\mathsf T}L^{-1}e_1.
\tag{3}
\]

**Source correction:** Algorithm IV.3.4(iii), printed p. 56, omits the minus sign in (3).
The repeated reciprocal formula immediately before Lemma IV.5.4, printed p. 59, has the identical omission.
Both formulas were checked in rendered pages; this is not a text-extraction ambiguity.
One can repair the representing row by changing $e_1^{\mathsf T}$ to $-e_1^{\mathsf T}$, or equivalently change one off-diagonal sign in the bordered matrix.
The scalar test $u=v=A=1$ already distinguishes the signs: the inverse of $\begin{pmatrix}0&1\\1&1\end{pmatrix}$ has upper-left entry $-1$.

The sign does not affect the invertibility test or inverse closedness of a complex algebra, but it does affect the claimed value of the represented inverse.
All uses of inversion below employ (3).
This unit does not re-audit the general external existence theorem for full linear representations; it only checks the arithmetic rules consumed by these sections.

## 3. Theorem IV.4.1: Evaluation in a Stably Finite Algebra

### 3.1. Why the ambient assumption appears

Let $l$ be the unilateral left shift on $\ell^2(\mathbb N_0)$, so $ll^*=I$ and $l^*l=I-P_{e_0}$.
In the free field on $x,y$, the expression $y(xy)^{-1}x$ equals one.
At $(l,l^*)$ it is defined in $B(\ell^2)$ but evaluates to $l^*l\ne I$.
Thus it disagrees with the constant representation of the same free-field element.
This checks the source's counterexample directly.
The source's cited converse characterization of stable finiteness is background, not required for the sufficient theorem proved here.

### 3.2. Definition of the representation domain

For a representation $\varrho=(u,A,v)$, define

\[
\operatorname{dom}_{\mathcal B}(\varrho)
=\{X\in\mathcal B^d:A(X)\in GL_n(\mathcal B)\},
\qquad
\operatorname{dom}_{\mathcal B}(r)
=\bigcup_{\varrho\text{ representing }r}
\operatorname{dom}_{\mathcal B}(\varrho).
\tag{4}
\]

The tentative value is $uA(X)^{-1}v$ using any eligible representation.
The union in (4) may include a point at which a particular alternative expression or representation for $r$ is not defined.
The theorem proves agreement of values when both chosen representation matrices are invertible; it does not require every representation to be invertible at each point of the union.

### 3.3. Zero representations and the required rank repair

Two representations $u_1A_1^{-1}v_1$ and $u_2A_2^{-1}v_2$ for the same field element give a representation of zero with matrix $\operatorname{diag}(A_1,-A_2)$, row $(u_1,u_2)$ and stacked column $(v_1,v_2)^{\mathsf T}$.
That matrix stays invertible after evaluation wherever both original matrices are invertible.
It therefore suffices to prove that a representation $uA^{-1}v=0$ evaluates to zero on its domain.

Let $A$ have size $n$ and set

\[
L=\begin{pmatrix}0&u\\v&A\end{pmatrix}.
\tag{5}
\]

In the free field, $A$ is invertible and the Schur complement in (5) is zero.
After simultaneous row and column permutations, Proposition III.1.6, or direct elimination over the division ring, therefore gives

\[
\rho_{\mathbb F}(L)=n.
\tag{6}
\]

The rank-preserving embedding of the free polynomial algebra into its free field, recorded in Theorem IV.2.5(iv) and the paragraph following that theorem, is the next necessary input:

\[
\rho_R(L)=\rho_{\mathbb F}(L)=n.
\tag{7}
\]

Now let $X\in\operatorname{dom}_{\mathcal B}(\varrho)$, with $\mathcal B$ stably finite.
Evaluation is a homomorphism on polynomial entries, so inner rank cannot increase:

\[
\rho_{\mathcal B}(L(X))\leq\rho_R(L)=n.
\tag{8}
\]

If $uA(X)^{-1}v\ne0$, Proposition III.1.6 applied in $\mathcal B$, where its pivot $A(X)$ really is invertible, says that the inner rank is strictly larger than $n$.
Its size is $n+1$, so its inner rank would be $n+1$, contradicting (8).
Thus every zero representation evaluates to zero, proving consistency.

**Source correction:** on printed p. 58 the proof applies Proposition III.1.6 directly over $R$ to infer the rank of $L$ from $uA^{-1}v=0$ and stable finiteness of $R$.
The proposition requires its pivot to be invertible in the algebra where rank is computed.
The pivot $A$ is full over $R$ and invertible over $\mathbb F$, but need not be invertible over $R$.
Equations (6)-(7) supply the missing change of rank ring and its justification.
The target-side use of the proposition is valid as printed because $A(X)$ is assumed invertible in $M_n(\mathcal B)$.

This repair uses a retained free-field foundation, not a claim that all full polynomial matrices are polynomial-invertible.
The local statements of Proposition III.1.6 and Theorem IV.2.5(iv) were read with these exact hypotheses.
Their original Cohn/Sylvester-domain foundations belong to the preceding chapter units and the already registered free-field interfaces, not to a new original-proof audit in this section.

### 3.4. Arithmetic compatibility and domains

Equation (1) and repeated sum and product constructions supply everywhere-defined representations for polynomials, with their usual evaluated values.
The block constructions in Section 2 show that two functions defined at $X$ have their sum and product defined there, with the corresponding arithmetic values.
If $r$ is defined at $X$ and its value is a unit of $\mathcal B$, the bordered construction (3) gives an eligible representation of $r^{-1}$ and the inverse value in $\mathcal B$.
Here $r$ is necessarily nonzero in the free field because the zero field element evaluates to zero.
The bordered polynomial matrix is full: its Schur complement in $\mathbb F$ is $-r$, a unit, and rank preservation then gives fullness over $R$.

These assertions are local to the available representation domains.
The theorem does not say that every rational function is defined at every $X$ or that evaluation at an arbitrary $X$ embeds the whole free field.

## 4. Rational Closure Is an Algebra in Every Unital Ambient

Let $B=\mathbb C\langle X\rangle\subseteq\mathcal B$.
Definition IV.5.1 sets $\operatorname{Rat}_{\mathcal B}(B)$ equal to the entries of all inverses $A(X)^{-1}$, where $A$ is a square polynomial matrix and $A(X)$ is invertible over $\mathcal B$.
No stable-finiteness assumption is needed for this definition or for Lemma IV.5.2.

The source cites the general proof of that lemma.
Here is a reconstruction in its tuple-evaluation setting.
Every polynomial value $p(X)$ is the upper-right entry of

\[
\begin{pmatrix}1&-p(X)\\0&1\end{pmatrix}^{-1},
\tag{9}
\]

so the rational closure contains $B$, including zero and one.
An entry of $A(X)^{-1}$ has the form $uA(X)^{-1}v$ for scalar coordinate selectors $u,v$.
More generally, any scalar row and column can be encoded as a single inverse entry by the polynomial matrix

\[
Q=\begin{pmatrix}1&-u&0\\0&A&-v\\0&0&1\end{pmatrix}.
\tag{10}
\]

If $A(X)$ is invertible, then $Q(X)$ is invertible, and its upper-right inverse entry is $uA(X)^{-1}v$.
Thus arbitrary scalar combinations selected from one such inverse stay in the defining entry set, rather than merely in an algebra artificially generated from that set.

For a sum, use the diagonal matrix with blocks $A_1,A_2$, concatenate rows and stack columns, and then apply (10).
For a product, the polynomial block matrix

\[
\begin{pmatrix}A_1&-v_1u_2\\0&A_2\end{pmatrix}
\tag{11}
\]

has inverse upper-right block $A_1(X)^{-1}v_1u_2A_2(X)^{-1}$.
Select it with $(u_1,0)$ and $(0,v_2)^{\mathsf T}$, then apply (10).
Scalar multiplication and additive inverses are obtained by changing the row selector and using (10).
All matrices used are invertible by explicit triangular elimination in the same ambient matrix algebra.
This proves the entire subalgebra assertion of Lemma IV.5.2 without invoking its external cited proof.

If $\mathcal B$ is stably finite, an invertible $A(X)$ is full there.
The homomorphism rank inequality implies that the polynomial matrix $A$ was already full over $R$.
Its selected inverse entry therefore represents a free-field element defined at $X$ in (4).
Conversely, every such defined representation value is a scalar combination of entries of its matrix inverse and hence belongs to the rational closure just proved to be an algebra.
This establishes Remark IV.5.3:

\[
\operatorname{Rat}_{\mathcal B}(B)
=\{r(X):r\in\mathbb F,\ X\in\operatorname{dom}_{\mathcal B}(r)\}.
\tag{12}
\]

The ambient subscript in both sides of (12) is essential.

## 5. The Schur Lemma and Inverse Closedness

For arbitrary blocks over a unital algebra with the lower-right block $D$ already invertible, put $S=A-BD^{-1}C$.
Direct multiplication gives the factorization

\[
\begin{pmatrix}A&B\\C&D\end{pmatrix}
=
\begin{pmatrix}I&BD^{-1}\\0&I\end{pmatrix}
\begin{pmatrix}S&0\\0&D\end{pmatrix}
\begin{pmatrix}I&0\\D^{-1}C&I\end{pmatrix}.
\tag{13}
\]

The first and last factors have inverse obtained by negating their off-diagonal block.
The middle factor is invertible if and only if both diagonal blocks are invertible; the necessity follows also by multiplying a proposed inverse on both sides and reading its diagonal blocks.
Since $D$ is already a unit, this proves Lemma IV.5.4 in both directions.
No stable finiteness or commutativity is needed.
Every product in (13), including $D^{-1}$, is computed in that one stipulated ambient algebra.

If $r=uA(X)^{-1}v$ belongs to rational closure and is a unit of $\mathcal B$, apply (13) to the bordered matrix in (3).
It is a polynomial matrix evaluated at $X$, its inverse exists over $\mathcal B$, and its upper-left inverse entry is $-r^{-1}$.
The subalgebra property therefore puts $r^{-1}$ in rational closure.
This proves that rational closure is division closed for every unital ambient algebra, with the corrected sign.

The Schur formula has no assertion that boundedness of a selected inverse entry forces boundedness of the whole inverse matrix.
In an application with $\mathcal B=M$, its pivot inverse must be in the corresponding matrix algebra over $M$ before (13) is used there.
If only affiliated invertibility is known, the same formula is valid with $\mathcal B=U(M)$ and supplies conclusions in $U(M)$.
Changing that ambient algebra is an additional step, absent from the lemma.

## 6. Division Closure and the Division-Ring Case

### 6.1. Definition IV.5.5 and all parts of Remark IV.5.6

The division closure $\operatorname{Div}_{\mathcal B}(B)$ is the smallest unital subalgebra of $\mathcal B$ containing $B$ and closed under inverses which exist in $\mathcal B$.
Intersection of all such subalgebras supplies its existence.

For item (i), if each nonzero element of a division-closed algebra is a unit of the ambient, its inverse belongs to the algebra, which is therefore a division ring.
For item (ii), rational closure contains $B$ and is division closed by Section 5, so minimality gives

\[
\operatorname{Div}_{\mathcal B}(B)\subseteq\operatorname{Rat}_{\mathcal B}(B).
\tag{14}
\]

For item (iii), take $B=R$ and ambient $\mathbb F$.
Every nonzero element of the division closure is invertible in the ambient field, so this closure is itself a division subring containing $R$.
The defining epic, or division-generation, property of the free field makes it the whole $\mathbb F$.
This uses the free-field foundation recorded in IV.2; it is not a claim that the same equality follows in a different ambient algebra without a field-generation hypothesis.

For item (iv), put

\[
B_0=B,\qquad
B_{k+1}=\operatorname{alg}\bigl(B_k\cup\{b^{-1}:b\in B_k\cap\mathcal B^\times\}\bigr).
\tag{15}
\]

Every division-closed algebra containing $B$ contains each finite stage by induction, hence their increasing union.
That union is a unital algebra, and if an element at stage $k$ is invertible in $\mathcal B$, its inverse lies at stage $k+1$.
The union is therefore itself division closed and minimal, proving

\[
\operatorname{Div}_{\mathcal B}(B)=\bigcup_{k\geq0}B_k.
\tag{16}
\]

Each individual element uses finitely many arithmetic operations and allowed scalar inverses.
The old [Yin20-U001](Yin_U001.md#yin20-u001) already records this exact recursive proof; the present whole-section review confirms its scope and does not alter that earlier artifact.
The source's phrase that the union "belongs to" the division closure is read as containment; the final equality and its proof are unambiguous.

### 6.2. Lemma IV.5.8, with every pivot justified

Let $D\subseteq\mathcal B$ be a unital division subring.
For $n=1$, if $a\in D$ is a unit in $\mathcal B$, it is nonzero and has its division-ring inverse in $D$.
That inverse equals the ambient inverse by uniqueness.
This supplies the explanation of the source's base-case phrase "since D is division closed": no extra inverse-closedness hypothesis is required.

Suppose the matrix assertion holds at size $n-1$ and let $Q\in M_n(D)$ be invertible in $M_n(\mathcal B)$.
It is nonzero, so row and column permutations put a nonzero entry in the last diagonal position.
Those permutations and their inverses lie in $M_n(D)$ and preserve the desired conclusion.
Write the permuted matrix as

\[
Q=\begin{pmatrix}B&c\\d&e\end{pmatrix},\qquad e\ne0.
\]

Since $D$ is a division ring, $e^{-1}\in D$ and is also its inverse in $\mathcal B$.
The Schur complement $S=B-ce^{-1}d$ is a matrix over $D$ and is invertible over $\mathcal B$ by Lemma IV.5.4.
Induction therefore gives $S^{-1}\in M_{n-1}(D)$.
Inverting (13) gives exactly the displayed source formula

\[
Q^{-1}
=\begin{pmatrix}I&0\\-e^{-1}d&1\end{pmatrix}
\begin{pmatrix}S^{-1}&0\\0&e^{-1}\end{pmatrix}
\begin{pmatrix}I&-ce^{-1}\\0&1\end{pmatrix}.
\tag{17}
\]

Every factor lies in $M_n(D)$; undoing the permutations does too.
Thus $M_n(D)$ is inverse closed in $M_n(\mathcal B)$ at every size.
The argument uses scalar pivots that are invertible because the coefficient subring is a division ring, not because an arbitrary nonzero element of a general ambient algebra is invertible.

### 6.3. Proposition IV.5.7

If rational closure is a division ring, every nonzero element of division closure is a unit of that ring, hence of $\mathcal B$.
Its ambient inverse returns to division closure, so division closure is itself a division ring.
It remains to treat that latter case.

Set $D=\operatorname{Div}_{\mathcal B}(B)$ and assume $D$ is a division ring.
Any polynomial matrix $A(X)$ defining rational closure is a matrix over $D$, invertible over $\mathcal B$.
Lemma IV.5.8 puts its inverse in the matrix algebra over $D$.
Every inverse entry is therefore in $D$, giving rational closure contained in division closure.
Together with (14), this proves the claimed equality if either closure is a division ring.

### 6.4. The Reich strengthening and its corrected primary locator

The final contextual sentence refers to `[Rei06, Note 13.16]`, but the bibliography's 2006 source is Reich's chapter *L2-Betti numbers and Noncommutative Localization*.
In the [primary published collection](https://webhomes.maths.ed.ac.uk/~v1ranick/books/nlat.pdf#page=132), the exact locator is Proposition 4.9 and its immediately following **unnumbered remark**, printed p. 122 / collection PDF p. 132.
They state that an algebraically von Neumann regular ring is division closed and rationally closed in every overring, and consequently a von Neumann regular division closure equals rational closure.
The cited number instead occurs in Reich's [dissertation *Group von Neumann Algebras and Related Algebras*](https://www.mi.fu-berlin.de/math/groups/top/members/publ/diss.pdf#page=107), whose title page says Göttingen 1998: Proposition 13.15 and Note 13.16, printed p. 103 / PDF p. 107.
This is a source-version locator mismatch, not a failure of the mathematical assertion.

The following direct argument reconstructs the essential overring step without needing the published proof's kernel/cokernel terminology.
An algebraically von Neumann regular unital ring $S$ satisfies: for every $a\in S$, there is $b\in S$ with $a=aba$.
If $S\subseteq\mathcal B$ and $a$ is invertible in $\mathcal B$, multiply this identity on both sides by the ambient inverse to obtain

\[
a^{-1}=a^{-1}(aba)a^{-1}=b\in S.
\]

Thus $S$ is division closed in every unital overring.
For matrices, use the standard matrix-regularity fact stated explicitly in the primary proof: every $M_n(S)$ is von Neumann regular when $S$ is.
If $A\in M_n(S)$ is invertible over $\mathcal B$, choose $B\in M_n(S)$ with $A=ABA$; the same calculation yields $A^{-1}=B\in M_n(S)$.
This proves rational inverse-closedness, with matrix regularity retained as the precise standard structural input rather than claimed as proved here.

Apply this with $S=\operatorname{Div}_{\mathcal B}(B)$ when that particular division closure is von Neumann regular.
Every inverse entry defining $\operatorname{Rat}_{\mathcal B}(B)$ lies in $S$, and (14) supplies the reverse inclusion, proving equality.
The two closures are still formed in the same ambient algebra.
In particular, a bounded von Neumann algebra is not automatically a von Neumann regular ring in this algebraic sense: an element can have an affiliated inner inverse without a bounded one.
The strengthening therefore supplies no passage from a calculation in $U(M)$ to a calculation in $M$.

This supplement uses a fresh primary text check of the published proposition, its full proof and the following remark, together with the dissertation's corresponding page and title page for the numbering repair.
The parent reviewer obtained the primary texts; the present unit's author read the extracted passages and independently reconstructed the argument above.
No fresh visual inspection or full audit of either Reich work is claimed.

## 7. The Same-Ambient Boundary for the Research Retry

The useful implication supplied by Definition IV.4.2 and Remark IV.5.3 is

\[
X\in\operatorname{dom}_{M}(r)
\quad\Longrightarrow\quad
r(X)\in\operatorname{Rat}_{M}(\mathbb C\langle X\rangle)\subseteq M.
\tag{18}
\]

Conversely, an element in that matrix rational closure has such a representation by definition and Section 4.
This is a statement about representations with whole inverse matrices over $M$.
It does not identify the set in (18) with all values $r(X)\in M$ obtained using a representation invertible only over $U(M)$.
The latter condition first asserts $X\in\operatorname{dom}_{U(M)}(r)$ and then boundedness of one evaluated output.

The earlier project account reports an illustration under its bounded-dual hypotheses in former Yin_C_F0012.
Its exact fixed proof/review homes are located in the [original C12 source account](../MSY23/Yin_U003.md#original-project-obstruction), with source-only access and no newly adopted local obstruction theorem.
Its polynomial matrix $\begin{pmatrix}h&-Y\\0&h\end{pmatrix}$ has affiliated inverse $\begin{pmatrix}h^{-1}&b\\0&h^{-1}\end{pmatrix}$, with bounded selected output $b$ and unbounded diagonal entries.
The source theorem audited here does not change the ambient of that inverse.
The further exclusion of alternative bounded matrix representations in that model is a project argument involving its C*-algebra, not a conclusion imported from Yin20 without proof.

Likewise, Proposition IV.5.7 equates the two closures computed in one fixed ambient when one of them is a division ring.
Applying it with ambient $U(M)$ does not equate their intersection with $M$ to closures recomputed inside $M$.
The recursive construction (15) also makes this dependence explicit at each inverse node.

These sections contain no operator-domain estimates for dual systems, adjoint cores, or arbitrary bounded fraction coefficients.
Their algebraic evaluation and Schur mechanisms can be consumed after those analytic objects are defined, but do not themselves extend a dual from a polynomial core to all bounded vectors.
The separate small-core rationality retry must preserve that distinction.

## 8. Evidence, Corrections, and Retained Inputs

All PDF pages 66-72 were rendered and visually inspected, including the two reciprocal signs, the ambient in the rank argument, every Schur factor in (17), the complete recursive definition, and the blank final verso.
Their corresponding extracted text was read in full.
The source artifact was not edited or replaced.
No new PDF was added to the literature directory.
The selected Reich primary-text comparison and its limited version-locator purpose are recorded in Section 6.4; no whole-work comparison is claimed.

The two actual formula corrections are the repeated inverse sign, and the missing free-field rank computation plus rank preservation in the polynomial step of Theorem IV.4.1.
The base case of Lemma IV.5.8 and the division-closure union need explanatory precision, without changing either conclusion.
The Schur complement factorization and the closure comparison themselves pass the reconstruction.

The local proofs supplied here replace the source's omitted proof of Lemma IV.5.2 and the unexpanded Schur algebra.
Retained substantive inputs are the existence of full linear representations, the rank-preserving free-field embedding of the free polynomial algebra, stable-finite inner-rank pivot comparison from III.1.6, and the free field's division-generation property.
Their precise statements are recorded in the preceding source sections and the project free-field audits.
The original general Cohn/HMS18 proofs are outside this unit's original-proof coverage.
The Reich supplement additionally retains matrix regularity of a von Neumann regular ring as a standard structural input and proves the remaining closure argument explicitly.

The scalar inverse-sign test is an exact algebra calculation, not a numerical certificate for the full theorem.
No numerical experiment, proof-assistant verification, external human review, publication or historical-priority claim has been made.
Separate cross-review of this written source unit is pending at creation; its final evidence belongs in the Yin20 audit index or an explicit review record.

## 9. Independent Complete-Artifact Review

On 2026-09-10, the rational-expression agent independently read this complete unit and compared it with the supplied Yin20 source.
The review covered every proof, domain qualification and retained input in Sections 1–8, including the complete Reich supplement.
Source PDF pp. 66–72 / printed pp. 56–62 were read and visually inspected; p. 66 was covered during the same reviewer's immediately preceding U003 reconstruction, and pp. 67–72 were inspected for this cross-review.
The blank final verso, both printed reciprocal signs and the precise polynomial-rank gap in IV.4.1 were verified in the rendered source.

The independent calculations confirm the following points.

- The product block in (2) has the stated asymmetric block-column sizes, its inverse exists on the common input domain, and the multiplication order produces `r₁r₂`.
- The inverse compression in (3) is `−r⁻¹` before correcting the outer sign, and the same correction is required at both source occurrences.
- The zero-representation argument correctly computes rank in the free field first, transfers it to the polynomial algebra using rank preservation, and then uses the genuinely invertible evaluated pivot in the stably finite target.
- The triangular matrices (9)–(11), together with the subsequent sum construction, keep inverse entries and scalar row-column compressions within the defining rational-closure set.
- Both sides of the Schur factorization (13) and all three factors of (17) have the correct signs and noncommutative orders.
- The finite-stage division construction is increasing, is inverse closed in the fixed ambient, and has the asserted minimality.
- The induction in Lemma IV.5.8 uses a nonzero scalar entry in the division coefficient ring as its pivot, and Proposition IV.5.7 follows without an extra inverse-closedness assumption on that division ring.

For Section 6.4, the reviewer independently read the supplied primary-text extractions of Reich's published Proposition 4.9 and following unnumbered remark on printed p. 122 / PDF p. 132, and dissertation Proposition 13.15 and Note 13.16 on printed p. 103 / PDF p. 107.
The dissertation title-page extraction gives Göttingen 1998, while Yin20's bibliography identifies the 2006 chapter, confirming the version-dependent locator mismatch.
The `a=aba` overring proof is valid on both the scalar and matrix levels, with matrix regularity retained explicitly as the structural input.
This review does not claim fresh rendered inspection of either Reich source or a proof of that general matrix-regularity theorem.

Contribution disclosure: this reviewer authored U003 and independently checked its overlapping representation rules, and had previously worked on the project's small-core domain issue and bounded-compression example.
Those preliminary contributions are disclosed rather than counted as independent discovery of the overlapping sign correction.
The present review independently checks the complete U004 artifact and its additional evaluation, closure and Reich arguments.
The general free-field foundations were additionally primary-checked at their selected Cohn locators during U003; their entire original proofs are not recursively certified here.

Outcome: accepted at the stated scope, with the source repairs already present in the reviewed artifact and no additional correction required.
The mathematical body was preserved; this review record is the only change made by the independent reviewer.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Yin20, the supplied 109-page doctoral dissertation with title-page year 2019; its defense date 2020-01-27 and public repository metadata are separate facts. Printed Arabic page = PDF page minus 10. Other source editions retain their separate exact locators.

Passages: Sections IV.4-IV.5, printed pp. 56-61 / PDF pp. 66-71, plus blank PDF p. 72; Algorithm IV.3.4 on p. 56, input conventions on pp. 54-55 and Proposition III.1.6 on p. 39.

Inspection: 2026-09-10: complete local reconstruction and self-check of evaluation consistency, Schur complements and the two closures, followed by the appended independent artifact review. Exact Reich published/dissertation locators and selected Cohn interfaces are distinguished; general matrix regularity and free-field foundations remain structural inputs. Prior overlapping reviewer contributions are disclosed. No fresh rendered Reich check, whole external-source proof audit, formal verification or external human review is claimed.
