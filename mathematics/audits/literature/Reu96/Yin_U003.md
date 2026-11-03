---
author: Yin
---

<a id="reu96-u003"></a>
# Reu96-U003: Height Families and the Invariant-Subspace Theorem

This source analysis comprises [U002](Yin_U002.md#reu96-u002), [U003](#reu96-u003).
Its [shared source, inspection and setting](Yin_U002.md#reu96-rational-tensor-series-and-height-preserving-state-spaces) and [joint review dated 2026-09-08](#reu96-u002-u003-cross-review-2026-09-08) retain their original scopes.


- Kind: height-preserving linear-algebra mechanism.
- Locators: height bases and (3.1)-(3.2), p. 100; Lemma 3.3, p. 101; Lemma 3.4, pp. 102-103; Lemma 3.5 statement, p. 103, and proof, pp. 104-105; height families and Lemma 3.6, p. 104.
- Scope: finite-dimensional left vector spaces over a division ring $D$ with central $k$, acted on by a set $E$ of $k$-linear endomorphisms.
  Individual endomorphisms need not be $D$-linear.
  The subspace in Lemma 3.4 must be a left $D$-subspace stable under every member of $E$.

### Exact Height Rules

Let $S$ be a finite ordered $D$-basis of $V$ and $h:S\to\mathbb Z_{\ge0}$.
For each positive-height $v$, put
\[
n(v)=\min\{v'>v:h(v')\ge h(v)\},
\]
with value $\infty$ if absent.
For every $e\in E$, $d\in D$, and $v\in S$, the height-basis requirements are
\[
\begin{cases}
e(dv)\in\operatorname{span}_D\{v'<v\},&h(v)=0,\\
e(dv)\in\operatorname{span}_D\{v'<n(v)\},&h(v)\ge1.
\end{cases}
\]
When $n(v)=\infty$, the second constraint permits the whole space.
The height is $\max_{v\in S}h(v)$.
This formulation retains the crucial universal coefficient $d$; checking only $e(v)$ is insufficient for merely $k$-linear maps.

A height family is a finite indexed spanning family $(v_i)_{i\in I}$ obeying the same rules with indices in place of basis vectors.
It may be redundant.
Its next index must also be strictly later:
\[
n(i)=\min\{j>i:h(j)\ge h(i)\}.
\]
The displayed (3.8) on p. 104 instead prints $j\ge i$.
This is a source error: it would always give $n(i)=i$, eliminating the permitted positive-height feedback and contradicting (3.2) and the star construction below.
The corrected strict inequality and the same infinity convention are used throughout this reconstruction.

### Lemma 3.3: Triangular Reduction with Chosen Support Positions

For nonzero $w=\sum_{v\in S}d_vv$, let $\operatorname{supp}(w)=\{v:d_v\ne0\}$ and $\operatorname{lead}(w)=\max\operatorname{supp}(w)$.
Suppose a position $c(w)\in\operatorname{supp}(w)$ has been chosen for every nonzero $w$.

For any left $D$-subspace $W\subseteq V$, the lemma constructs a basis $T$ such that its leading positions are distinct and
\[
\operatorname{lead}(w)<\operatorname{lead}(w')
\quad\Longrightarrow\quad c(w)\notin\operatorname{supp}(w')
\quad(w,w'\in T).
\]
Hence all chosen positions $c(w)$ in $T$ are distinct.

Start with an echelon basis with distinct leading positions.
Process it in increasing leading order.
For a current basis vector $w_0$ and a later vector $w'$, eliminate the coefficient of $c(w_0)$ from $w'$ by subtracting $d w_0$.
If that coefficient in $w'$ is $a$ and in $w_0$ is $b\ne0$, the correct left coefficient is $d=ab^{-1}$.
This preserves the leading position of $w'$ because $\operatorname{lead}(w_0)<\operatorname{lead}(w')$.
Positions already removed remain absent from both participating vectors.
Earlier processed vectors are unchanged, so their already chosen positions do not change.
This proves the induction over the finite basis.

Distinct leading positions also give the filtration property used in (3.5):
\[
w\in W,\quad\operatorname{lead}(w)<v
\quad\Longrightarrow\quad
w\in\operatorname{span}_D\{t\in T:\operatorname{lead}(t)<v\}.
\]
In a nonzero linear combination of the echelon basis, its largest participating leading position cannot cancel.
The zero vector is included trivially.

### Lemma 3.4: Transferring the Height to an Invariant Subspace

Assume $S$ is a height basis for $E$ of height at most $\ell$ and $W$ is invariant.
A support position $v$ in a nonzero vector $w$ is *semicritical* if it is the leading position, or if
\[
h(v)\ge1\quad\text{and}\quad\operatorname{lead}(w)<n(v).
\]
Let $c(w)$ be the semicritical position of largest height.

This choice is unique.
Two height-zero semicritical positions would both have to be the leading position.
If two positive-height semicritical positions $v_1<v_2$ had equal height, then $n(v_1)\le v_2\le\operatorname{lead}(w)$, contradicting semicriticality of $v_1$.
Thus semicritical positions have distinct heights.

Apply Lemma 3.3 with this $c$.
Order the resulting basis $T$ of $W$ by increasing $c(t)$, rather than by its old leading order, and set
\[
h_T(t)=h(c(t)).
\]
This is a total order because the chosen positions are distinct, and the height has not increased.

**Height-zero case.** If $h_T(w)=0$, then $c(w)=\operatorname{lead}(w)$.
Every positive-height position $v$ in the support is not semicritical, so $n(v)\le\operatorname{lead}(w)$.
The original height rules, applied to every coefficient in $dw$, show
\[
e(dw)\in\operatorname{span}_D\{v<\operatorname{lead}(w)\}.
\]
The vector is in $W$ by invariance.
The filtration property expresses it in basis vectors $t$ with $\operatorname{lead}(t)<\operatorname{lead}(w)$.
Since $c(t)\le\operatorname{lead}(t)<c(w)$, every such $t$ precedes $w$ in the new order.
This is the required height-zero rule on $T$.

**Positive-height support bound.** If $h(c(w))\ge1$, every term in $e(dw)$ is supported strictly before $n(c(w))$.
When that next position is infinite the bound is vacuous.
Otherwise examine a support position $v$ of $w$:

- If $h(v)=0$, its image is supported before $v\le\operatorname{lead}(w)<n(c(w))$.
- If $h(v)>0$ and $v$ is not semicritical, then $n(v)\le\operatorname{lead}(w)<n(c(w))$.
- If $v=c(w)$, its image is supported before $n(c(w))$ directly.
- If $v$ is semicritical and $v>c(w)$, its height is strictly smaller than $h(c(w))$.
  Also $v\le\operatorname{lead}(w)<n(c(w))$, so $n(c(w))$ is a later position of sufficiently large height, giving $n(v)\le n(c(w))$.
- A semicritical $v<c(w)$ is impossible: it would have smaller height, making $c(w)$ a candidate for $n(v)$ and forcing $n(v)\le c(w)\le\operatorname{lead}(w)$.

The bound applies to arbitrary left coefficients because the original rules apply to $e(dv)$ for every $d\in D$ and $e$ is additive.

**Positive-height next position in the new basis.** Let $w_1=n_T(w)$, if this is finite.
Then $c(w)<c(w_1)$ and $h(c(w_1))\ge h(c(w))$, hence
\[
n(c(w))\le c(w_1).
\]
The filtration property expresses $e(dw)\in W$ in $t\in T$ with $\operatorname{lead}(t)<n(c(w))$.
For these,
\[
c(t)\le\operatorname{lead}(t)<n(c(w))\le c(w_1),
\]
so $t$ precedes $w_1$.
If $n_T(w)=\infty$ there is no restriction.
This proves the positive-height rule and Lemma 3.4.

No invariance of an arbitrary coordinate flag was assumed.
The chosen critical positions and the second basis ordering are what make the bound survive passage to $W$.

### Lemma 3.6: Removing Redundancy Without Increasing Height

Suppose a height family has a dependence
\[
v_r=\sum_{j<r}d_jv_j.
\]
Delete index $r$.
Replacing $v_r$ in any earlier initial-segment span uses only indices still earlier than its old position, so every such span is preserved after deletion.
For a remaining positive-height index $i$, the next surviving index satisfies $n'(i)\ge n(i)$: deletion cannot create an earlier candidate.
The old image bound, followed by substitution of the dependence, is therefore within the permitted new initial segment.
The height-zero rule is preserved for the same reason.
Repeat until the family is a basis.

On p. 104, step 1 of the source writes $I'=I\setminus\{k\}$ immediately after selecting dependent $v_r$, with no such $k$ defined there.
The deleted index must be $r$.
With this correction and the strict next-index definition above, the removal proof is valid.
The next-index comparison in step 4 is non-strict, $n'(i)\ge n(i)$; it does not require the next index to change.

### Lemma 3.5: Building a Height Family from a Star Expression

Let $E$ be all the left transductions of U002.
The induction is on the size of a rational star expression, retaining its star-depth bound.
It constructs a finite-dimensional left $D$-space $V$ containing the represented series and a height family for $E$.
Lemma 3.6 then gives a height basis.

**Polynomial case.** Expand the finite tensor polynomial in $k$-basis monomials, include all tails obtained by deleting successive initial coefficient-letter pairs, and order this finite family by increasing $X$-degree.
Applying a transduction to $d$ times a monomial gives a $k$-linear combination of its one-step tail: the initial coefficient $d u_\alpha$ has a finite expansion in the $k$-basis.
Each nonzero image has smaller degree.
Constants have zero image, so all heights can be zero.

**Sum $f=f_1+f_2$.** If $V_j,S_j,I_j$ are the previously constructed spaces and indexed families, take $V=V_1+V_2$ and the concatenated spanning family with the $I_1$ block before $I_2$.
Retain each height.
A next index originally inside a block stays the same.
A formerly infinite next index in the first block may become an index in the second block, but every vector in the first block is still earlier than that new cutoff.
Thus the old image constraints continue to hold.

**Product $f=f_2f_1$.** Take
\[
V=V_2 f_1+V_1
\]
with the $S_1$ block first and the $S_2f_1$ block second, retaining the original heights.
Multiplication on the right by $f_1$ is left $D$-linear, so this family spans $V$.
For $g\in V_2$,
\[
T_{\alpha,x}(d g f_1)
=T_{\alpha,x}(dg)f_1+
T_{\alpha,x}(\operatorname{ct}(dg)f_1).
\]
The second term lies in $V_1$, whose whole family precedes the second block.
The first term obeys the original cutoff within the $S_2f_1$ block.
This checks stability and every height condition without assuming that transductions are $D$-linear.

**Star $f=f_1^*$, with $f_1$ proper and star height at most $\ell-1$.**
Here $\ell\ge1$.
Set
\[
V=Df+V_1f,\qquad
S=\{f\}\ \cup\ \{(g-\operatorname{ct}(g))f:g\in S_1\}.
\]
Place the new vector $f$ first, with height $\ell$, and keep the old order and heights, all at most $\ell-1$, on the remaining indexed family.
It spans $V$ since $gf=(g-\operatorname{ct}(g))f+\operatorname{ct}(g)f$.

The identity $f=1+f_1f$ and properness of $f_1$ give
\[
T_{\alpha,x}(df)=T_{\alpha,x}(df_1)f.
\]
The new first vector has no later vector of height at least $\ell$, so its images may use the whole family.
For an old family member,
\[
T_{\alpha,x}\bigl(d(g-\operatorname{ct}(g))f\bigr)
=T_{\alpha,x}(dg)f.
\]
Express $T_{\alpha,x}(dg)$ in the old permitted initial segment, then replace each $g'f$ by its properized family member plus $\operatorname{ct}(g')f$.
The new $f$ is earlier than every old index, so these extra multiples never violate an old height bound.
This checks the star step, including old height-zero vectors.

The constructed space $V$ contains $L(f)$, by the latter's minimal invariant-space property.
Apply Lemma 3.6 to get a basis of $V$, Lemma 3.4 to get a height basis of $L(f)$, and Lemma 3.2 to get the minimal height-structured representation.
This is the complete local forward chain for Theorem 3.1.

### Findings, Dependencies, and Scope of Verification

Two specific source corrections are required on p. 104:

| Location | Printed issue | Reading used in the checked proof |
| --- | --- | --- |
| Equation (3.8) | The next-index set includes $j=i$, so it collapses to the present index. | Use $j>i$, with $h(j)\ge h(i)$, as in (3.2). |
| Lemma 3.6, step 1 | The deleted index is written $k$ after the dependence selects $v_r$. | Delete $r$. |

The first correction changes a literal defining inequality and is necessary for positive-height feedback; it is not a harmless replacement of strict by non-strict notation.
The corrected invariant-subspace, family-reduction, and expression-induction proofs were reconstructed in full, including arbitrary left coefficients, the infinite-next convention, and all cases in the critical-support bound.
No unresolved local implication was identified after these corrections.

The source writes the maximum of the height function using a vector-space variable at p. 100, although the function is defined only on the basis.
The precise maximum is over the finite basis, or the finite index set for a family, as used here.

This unit uses U001's coefficient and height conventions and U002's transductions.
The purely linear-algebraic Lemmas 3.3, 3.4, and 3.6 need no commutativity of $D$ and no infinite-center hypothesis.
The source's external rational-series characterization is kept at the declared U002 inspection depth.
The unit supports U002 and then U004; it does not claim height preservation for arbitrary noninvariant subspaces, arbitrary state-coordinate changes, Boolean automata, or changed coefficient fields.

Verification date: 2026-09-08.
The exact inequalities, subscripts, and zero/nonzero alternatives were visually checked on pp. 100-105; the proofs above are mathematical reconstructions of the source's claims.
The separate CR94 interface inspection is identified in U002.
No new project claim, computation, proof-assistant artifact, or independent proof audit of cited reference [10] or [12] was produced.
This is the initial audit of these units.

<a id="reu96-u002-u003-cross-review-2026-09-08"></a>
Independent local cross-review, 2026-09-08: the height-machinery reviewing agent read U002-U003 and visually checked the source's height machinery on printed pp. 100-105, together with the series statement and diagrams.
The review checked arbitrary left coefficients, the echelon-support reduction, reordered critical basis, all semicritical cases, redundancy removal, the product-family order, the new star vector's position, and the minimality/finite-support reasoning under the declared representation interface.
It confirmed the two p. 104 corrections and identified no additional local mathematical gap.
This cross-review does not extend the inspection depth of the external CR94 proofs.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Reu96, the retained 17-page published Selecta Mathematica 2 (1996), pp. 93-109, DOI 10.1007/BF01587940. Printed page equals PDF page plus 92. The historically incorrect supplied filename DR97.pdf was corrected with authorization; it is not a citation alias, and the separately registered DR97 article is distinct. No second version was compared.

Passages: Height bases and (3.1)-(3.2), printed p. 100; Lemma 3.3, p. 101; Lemma 3.4, pp. 102-103; Lemma 3.5, pp. 103-105; height families and Lemma 3.6, p. 104.

Inspection: 2026-09-08: invariant-subspace, critical-support, family-reduction and star-expression arguments reconstructed in full with both p. 104 corrections; the retained joint U002-U003 independent review does not deepen the external CR94 proof inspection. No extra infinite-center hypothesis for these local linear-algebra lemmas, independent audit of cited original proofs, computation or formal verification.
