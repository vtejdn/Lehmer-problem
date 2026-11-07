---
author: Yin
---

<a id="dr97-u002"></a>
# DR97-U002: Cayley-Tree Defects and Finite Residual Spaces

- Source: [DR97](../../../literature/pdf/DR97.pdf), published version, Section 2.2, pp. 616-618; Remark 2 and Proposition 5.
- Record: 2026-09-08, the coordinating agent, local proof reconstruction and self-review for [DR97 rational-series source audit](readme.md#dr97-rational-series-source-audit).
- Kind and coverage: algebraic construction and finite-rank criterion, audited within the finite-generator scope below, with the restricted injectivity argument made explicit.

## Spaces, domains, and statement

Let $k$ be a commutative field, $X$ a finite set, $\Gamma=F_X$, and $A=X\sqcup\bar X$.
Use the word and group conventions in [DR97-U001](Yin_U001.md#dr97-u001).
Let $E$ be the unoriented edges of the Cayley tree.
For $g\ne1$, let $\phi(g)$ delete the last letter of $m(g)$.
Define

$$
H_+=k^{(\Gamma)},\quad H_-=k^{(E)}\oplus kq,
\qquad \widehat H_+=k^\Gamma,\quad
\widehat H_-=k^E\oplus kq.
$$

The map $P:H_+\to H_-$ sends $e_1$ to $q$ and $e_g$ to the edge $\{\phi(g),g\}$; it extends coefficientwise to the hatted spaces.
Put

$$
F=\begin{pmatrix}0&P^{-1}\\P&0\end{pmatrix}.
$$

Every $a=\sum_h\alpha_hh\in k^\Gamma$ acts on a vertex or edge by left translation of its coefficients and acts as zero on $q$.
These are maps $H_\pm\to\widehat H_\pm$.
They are well-defined for arbitrary coefficients because a fixed output coordinate receives only finitely many terms from a finite-support input.
**No product of two arbitrary group series is being defined.**

Write $C_a=P^{-1}a_--a_+P^{-1}:H_-\to\widehat H_+$.
Proposition 5 asserts

$$
\operatorname{rank}_k[F,a]<\infty
\quad\Longrightarrow\quad m(a)\text{ is rational in }k\langle\!\langle A\rangle\!\rangle.
$$

The block relation $P a_+-a_-P=-P C_a P$ proves that either off-diagonal block is finite rank exactly when the other is.
In fact $\operatorname{rank}[F,a]=2\operatorname{rank}C_a$.
The extra column is $C_a(q)=-a$.

## The decisive coefficient identity

Orient an edge away from the root as $e=\{g,gx\}$ with $x\in A$ and $m(g)x$ reduced.
Then $P^{-1}e=gx$.
Translation by $h$ preserves which vertex is farther from the root except when the whole suffix $gx$ cancels.
In that exceptional case

$$
m(h)=m(h_1)\bar x\,m(g^{-1})
$$

is a **reduced concatenation**, and the translated farther endpoint is $h_1\bar x$, whereas $hgx=h_1$.
Thus, with $S=m(a)$ and $v=\bar x\,m(g^{-1})$,

$$
C_a(e)=s(v\circ S)(\bar x-1).
\tag{*}
$$

The product on the right is a group series multiplied by a polynomial, hence defined coefficientwise even without a general convolution algebra.
The sign and multiplication order follow from the convention $[P^{-1},a]=P^{-1}a_--a_+P^{-1}$; swapping a commutator convention reverses both terms.

Every nonempty reduced word $v$ occurs uniquely in this form for an outward edge.
Nonreduced $v$ have zero residual, because $S$ has reduced support.

## Restricted injectivity and the finite-dimensional conclusion

For a fixed $x$, every residual $T=v\circ S$ in (*) has no support word ending in $x$, since $v$ begins with $\bar x$.
On this subspace, right multiplication by $\bar x$ is **concatenation without cancellation**, so $s(T)(\bar x-1)$ corresponds to the formal series $T\bar x-T$.

If $T\ne0$, choose its least nonzero homogeneous degree.
The coefficients of that degree cannot be canceled by $T\bar x$, whose least degree is one larger.
Therefore $T\bar x-T\ne0$.
The same argument applies to a linear combination of these residuals, proving injectivity on their whole span.

Let $r=\operatorname{rank}C_a<\infty$.
For each of the $2|X|$ letters, (*) and this restricted injectivity bound its residual span by $r$.
Adding the empty residual $S$ gives

$$
\dim_k\operatorname{span}\{v\circ S:v\in A^*\}
\leq1+2|X|r<\infty.
$$

Theorem 2, at the field scope reconstructed in U001, now proves Proposition 5.

**Why the restriction matters.**
Multiplication by $\bar x-1$ is not injective on all $k^\Gamma$.
For nonempty $X$, the nonzero series $\sum_{n\in\mathbb Z}x^n$ is fixed by right multiplication by $\bar x$.
DR97's sentence on p. 618 is valid for the displayed residual family, with the no-cancellation support condition supplied, and must not be cited as a universal group-series cancellation law.

## Finite-support inputs and boundary cases

For a single group element $h$, a nonzero defect column can occur only when $gx$ is completely canceled by $h$.
Such edges are on the finite root path determined by $h^{-1}$.
Together with the scalar column $q$, this proves finite rank for $h$, and hence for every $a\in k\Gamma$, as asserted in Remark 2(i).

If $a$ is a scalar multiple of the group identity, the edge columns vanish but $C_a(q)=-a$; the full $[F,a]$ need not be zero.
This is consistent with the source's **zero** action on the auxiliary $kq$ summand.
In the later inverse-closure argument it is necessary to account for this nonunital block action, or work modulo finite-rank maps; one must not silently replace it by a unital representation.
U003 handles the analytic closure chain; the separately reported Malcev-Neumann support construction is located at the [fixed original source home](readme.md#original-section-4-evidence), while current U005 supplies its external foundation.

For $X=\varnothing$, $\Gamma=\{1\}$ and $E=\varnothing$; all series are scalars and all spaces and defects have finite dimension.
The result is immediate without the letter-by-letter argument.
For $a=0$, every defect and residual vanishes.
The algebraic argument allows arbitrary characteristic and requires no group order or square summability.

## Dependencies and intended use

The dependencies are elementary reduced-word geometry and the finite-residual equivalence in U001.
The unit supplies Proposition 5 to both analytic and Malcev-Neumann branches.
It gives no boundedness assertion for a general $k^\Gamma$ sequence, no convolution algebra structure on that space, and no identification of the two later rational closures with each other.

The finite-generator assumption is used at the displayed dimension bound.
DR97 mentions it explicitly only in the proof on p. 618.
This review records that scope rather than claiming an unaudited infinite-generator extension.

## Verification facts and revisions

The coordinating agent read the complete Section 2.2 and inspected rendered pp. 616-618 on 2026-09-08, including both cancellation sums, barred letters, product order, and the definition of the auxiliary scalar action.
The proof above is a local mathematical reconstruction.
The historical exact finite computation reports 78,185 passing equalities for ranks 0-2, coefficient words of lengths 0-5, and edge endpoints of lengths 1-4.
The native program is [original J_F0001/main.py](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/computations/programs/Yin_J_F0001/main.py), with its exact finite inputs and checking relationships in the [original execution account](https://github.com/vtejdn/experimental-math-ai/blob/f1ab0a38da990d7e62f5f79acff1dd2312149ca9/mathematics/computations/programs/Yin_J_F0001/versions/v1/record.md).
The [fixed-source and access boundary](readme.md#original-section-4-evidence) applies; these are source-only locators rather than a local J group or a newly executed verification.
The standard-library program encodes all inputs and needs no separate dataset.
It supplements the universal argument and does not establish a general rationality theorem.
On the same date the Malcev-Neumann reconstruction agent independently checked the identity, edge/suffix correspondence, restricted injectivity, rank factor, scalar column, and finite-generator bound; no unresolved objection remained in that scope.
No formal verification or external human review is claimed.
The restricted-injectivity explanation is an audit clarification, not an author-confirmed erratum.

## Source and inspection

Source edition: DR97, the retained ten-page published Inventiones mathematicae 128 (1997), pp. 613-622, DOI 10.1007/s002220050154. Printed page equals PDF page plus 612. The separately retained 14-page author typeset version has an unstated preparation/revision date and was compared only at the selected passages recorded in U005; it does not replace the primary version.

Passages: Section 2.2, printed pp. 616-618; Remark 2 and Proposition 5.

Inspection: 2026-09-08: reduced-word identity, restricted injectivity and finite-generator bound reconstructed and independently reviewed. The recorded computation checks 78,185 finite equalities and supplements the universal proof only. No unrestricted convolution algebra, general boundedness, infinite-generator extension, external human review or formal verification.
