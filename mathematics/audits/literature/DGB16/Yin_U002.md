---
author: Yin
---

<a id="dgb16-u002"></a>
# DGB16-U002: Addition Theorem and the torsion and finite-rank reductions

## Source and inspection

Source edition: [DGB16](../../../literature/pdf/DGB16.pdf), Dikran Dikranjan and Anna Giordano Bruno, *Entropy on abelian groups*, Advances in Mathematics 298 (2016), 612-653; the supplied 42-page published article, retained unchanged under the canonical key.

Passages: Theorem 1.1 and notation on pp. 614-615 (PDF pp. 3-4); all of Section 5, pp. 635-643 (PDF pp. 24-32); interfaces from Propositions 2.6 and 2.8, Lemma 3.5, Proposition 3.7, Corollaries 3.9-3.10, Lemma 4.3 and Proposition 4.7.

Inspection: 2026-10-06T05:55. Complete Section 5 statement and source-proof check, including the extended-real arithmetic, pure-subgroup and hyperkernel interfaces. **Audited within scope**, over the explicitly retained external inputs below and with the source slips recorded here. Text read throughout the specified Section 5 scope; delicate formulas and printed citations visually checked on pp. 636 and 638-642. The Algebraic Yuzvinski Formula's exact statement and normalization were checked separately in the primary source GBV15, arXiv v3, pp. 3-4; its original proof was not audited.


The record is authored under the bound human key Yin.
An AI reviewer assigned to Section 5 performed the source-proof check and a self-check of this record.
The source article, extracted text, repository rules and the parent audit assignment were supplied; preliminary findings from the reviewer of Sections 2-4 were consulted before finalizing the dependency account.
This was a review of an external proof, not participation in its construction, but no second independent review of this audit record or formal verification is claimed.
The related [DGB16-U001](Yin_U001.md#dgb16-u001) owns the detailed foundational source checks.

## Exact statement and conventions

Let $G$ be any abelian group, let $\phi:G\to G$ be a group endomorphism, and let $H\le G$ satisfy $\phi(H)\subseteq H$.
The induced endomorphism is

\[
\bar\phi_H:G/H\longrightarrow G/H,\qquad
g+H\longmapsto\phi(g)+H.
\]

For each nonempty finite subset $F\subseteq G$, put

\[
T_n(\phi,F)=F+\phi(F)+\cdots+\phi^{n-1}(F),\quad
H(\phi,F)=\lim_{n\to\infty}\frac{\log|T_n(\phi,F)|}{n},\quad
h(\phi)=\sup_F H(\phi,F).
\]

The logarithm is natural; the limit exists by the subadditivity argument of Lemma 2.2.
All entropies belong to $[0,\infty]$.
Theorem 1.1 asserts

\[
h(\phi)=h(\phi|_H)+h(\bar\phi_H).
\tag{AT}
\]

The notation $\operatorname{AT}_h(G,\phi,H)$ means precisely (AT), including invariant-subgroup applicability.
No countability, finite generation, finite rank, purity, injectivity or surjectivity assumption belongs to the final theorem.
Addition uses the usual extended nonnegative reals; no subtraction of infinite quantities is allowed.
The source's $\mathrm{ent}$, defined using finite subgroups, agrees with $h$ on torsion groups, but does not replace $h$ on general groups.

## Proof mechanism and checks

### 1. The legitimate reduction to finite rank

Proposition 4.7(d) reduces an instance with invariant $H$ to finitely $\phi$-generated invariant subgroups $N$, with subgroup $N\cap H$, of finite free rank.
This is not an assumption that an arbitrary abelian group has finite rank.

If some cyclic flow $V(\phi,g)=\langle\phi^j(g):j\ge0\rangle$ has infinite rank, Lemma 3.5 gives $h(\phi)=\infty$.
If its intersection with $H$ is nonzero, that intersection has infinite entropy; if the intersection is zero, the cyclic flow embeds into $G/H$, whose entropy is infinite.
Thus the right side of (AT) is infinite in either case.
The lemma's printed omission of invariance is corrected at its point of use: $H$ here is invariant, as Proposition 4.7 requires.

Otherwise every finitely $\phi$-generated subgroup has finite rank.
Proposition 4.7(b)-(c) constructs one increasing chain that simultaneously approximates the entropy on $G$, on $H$, and on $G/H$.
The limits of the two nonnegative increasing summands sum to the limit of their sums, also if a limit is infinite.
This avoids an unjustified exchange of unrelated suprema.

For the torsion-subgroup reduction in Proposition 5.4, $N\cap t(G)=t(N)$, so the restricted instances are exactly the required torsion-subgroup instances.
For Proposition 5.10, each $N$ is still torsion-free.
These class-preservation checks justify both uses of Proposition 4.7(d).

### 2. Finite skew products and the full torsion subgroup

In Propositions 5.3-5.4, write $G=K\oplus T$, with $T$ invariant and torsion, and

\[
\phi(x,y)=(\phi_1x,\phi_2y+s(x)).
\]

If $s(K)$ is finite, choose a finite subgroup $F_2\le T$ containing it.
For any finite $F_1\subseteq K$, induction gives

\[
\phi^j(x,0)-(\phi_1^j x,0)
\in 0\oplus T_j(\phi_2,F_2).
\]

The second-coordinate trajectory is a subgroup.
Therefore it absorbs all accumulated error terms in both directions, and

\[
T_n(\phi,F_1\times F_2)
=T_n(\phi_1,F_1)\times T_n(\phi_2,F_2).
\]

These rectangles form a cofinal collection of finite subsets: every finite subset of a torsion abelian group is contained in a finite subgroup.
Proposition 2.8(d) consequently yields $h(\phi)=h(\phi_1)+h(\phi_2)$.
The finite-image hypothesis is essential to this specific cofinal-rectangle argument.

After the preceding finite-flow reduction, Lemma 4.3(b) says that $t(G)$ is bounded and splits: $G=K\oplus t(G)$, with $K$ torsion-free of finite rank.
If $m\,t(G)=0$, then $s(mK)=0$.
The source cites the finiteness of $K/mK$, whence $s(K)$ is finite and Proposition 5.3 applies.
This proves addition over $t(G)$.

The finiteness interface can also be checked directly.
For a prime $p$, any $r+1$ elements of a torsion-free rank-$r$ group have an integer relation with coprime coefficients: divide a relation by its coefficients' gcd, using torsion-freeness.
Its reduction modulo $p$ is nontrivial.
Thus $\dim_{\mathbf F_p}K/pK\le r$.
Factoring $m$ into primes and using multiplication's injectivity gives $|K/mK|\le m^r$.
This checks the exact finite-rank input without asserting inspection of the source's reference [4].
The bounded splitting theorem itself remains a cited external input, as recorded below.

### 3. Pasting addition without cancellation

Proposition 5.5 applies to invariant $H,K\le G$.
Write $I=H\cap K$, and abbreviate the entropies induced on $I,H/I,K/I,G/(H+K)$ as $a,b,c,d$.
The five assumed addition statements and the quotient isomorphisms give

\[
h(\phi)=(a+c)+(b+d)=(a+b)+(c+d)
=h(\phi|_H)+h(\bar\phi_H).
\]

All four quantities are nonnegative extended reals, so reassociation and commutation are valid even with infinity.
No cancellation occurs.
Corollary 5.6 is the corresponding chain rule for $H\subseteq K\subseteq G$, in either direction specified there.

Lemma 5.7(a), when $G/H$ is torsion, applies this pasting result with $K=t(G)$.
Two premises come from Proposition 5.4, two from torsion addition, and the fifth from the essential-subgroup case, Corollary 3.9(b), in $G/t(G)$.
The quotient of that torsion-free group by $(H+t(G))/t(G)$ is torsion, so essentiality is satisfied.
Lemma 5.7(b), when $H$ is torsion, uses $t(G/H)=t(G)/H$ and the chain $H\subseteq t(G)\subseteq G$.
The equality of torsion subgroups follows because $n(g+H)=0$ forces $ng\in H$ torsion and hence $g$ torsion.

### 4. Killing the hyperkernel in finite rank

Let $G$ be torsion-free of finite rank and $N=\ker_\infty\phi=\bigcup_{j\ge1}\ker\phi^j$.
It is pure, and Proposition 2.6 gives $h(\phi|_N)=0$.
Zero entropy on a kernel is not, by itself, used to assume addition.
Proposition 5.8 establishes the necessary equality $h(\phi)=h(\bar\phi_N)$ separately.

For $G=\mathbf Q^r$, choose a **positive** $q$ after stabilization of the kernels and images.
Then

\[
G=\ker\phi^q\oplus\operatorname{im}\phi^q,
\]

Both summands are invariant, $\phi$ is nilpotent on the first and invertible on the second.
To check the decomposition, the intersection is zero because $\ker\phi^{2q}=\ker\phi^q$, and dimensions add to $r$.
Weak addition for this direct product and conjugacy of the second summand to the quotient prove the entropy equality.
Equivalently, the source applies this decomposition to $\gamma=\phi^q$ and then the logarithmic law, dividing by the positive integer $q$; this is valid also for infinite entropy.

For general torsion-free $G$, pass to its divisible hull $D(G)=\mathbf Q\otimes G$.
The extended hyperkernel equals $D(N)$: every nonzero vector in the extended hyperkernel has a nonzero integer multiple in $G$, still killed by the same iterate.
Purity and Corollary 3.10 identify the quotient entropy; Proposition 3.7 identifies the ambient and restricted entropies.
Thus the result descends to $G$.
The source's essentiality argument must be read with a nonzero vector, as in the definition of an essential subgroup.

### 5. Rational finite dimension and Mahler normalization

Theorem 5.9 concerns an endomorphism of $D=\mathbf Q^r$ and a pure invariant $H\le D$.
Such $H$ is a rational vector subspace.
In an adapted basis,

\[
A=\begin{pmatrix}A_1&B\\0&A_2\end{pmatrix},\qquad
\chi_A=\chi_{A_1}\chi_{A_2}.
\]

If $s_i>0$ is the least common denominator of the coefficients of the monic rational polynomial $\chi_{A_i}$, then $p_i=s_i\chi_{A_i}$ is primitive integral.
Gauss's lemma makes $p_1p_2$ primitive, so the required leading coefficient for the product is $s_1s_2$.
Its root multiset is the union of the two block root multisets.
Therefore the **logarithmic** Mahler measures add:

\[
m(p_1p_2)=m(p_1)+m(p_2),\qquad
m(p)=\log|\operatorname{lc}(p)|+
\sum_{|\alpha|>1}\log|\alpha|.
\]

The Algebraic Yuzvinski Formula gives the desired entropy equality and finiteness.
One must retain the leading-coefficient term; using only the monic rational characteristic polynomial's expanding complex roots would give the wrong answer, for example for multiplication by $1/2$ on $\mathbf Q$.
The cases $H=0,D$ are tautological and do not require applying a positive-dimension theorem to dimension zero.

The source first treats automorphisms, then uses Proposition 5.5 and the hyperkernel to reduce an arbitrary endomorphism to that case.
The required identification

\[
(H+N)/H=\ker_\infty\bar\phi_H
\tag{HK}
\]

is valid here, but is not a formal identity for arbitrary invariant subgroups in arbitrary dimension.
A check of the compressed step is as follows.
In the stabilized decomposition $D=N\oplus J$, the restriction of $\phi$ to $J$ is invertible.
The subspace $H\cap J$ is invariant and finite-dimensional, so $\phi|_{H\cap J}$ is invertible too.
If some iterate of $x=n+j$ belongs to $H$, take a later iterate killing $n$; its value belongs to $H\cap J$, hence $j\in H\cap J$ by invertibility there.
Thus $x\in N+H$; the reverse inclusion is immediate.
This proves (HK) and validates the quotient application of Proposition 5.8.
All other pasting premises come from zero entropy on $N$ and the automorphism case on $D/N$.

### 6. Removing purity and torsion-freeness

In Proposition 5.10, reduce to finite rank and set $H^*=\{g\in G:mg\in H\text{ for some }m\ge1\}$.
This is invariant and pure; $H$ is essential in $H^*$.
Theorem 5.9 and Corollary 3.10 give addition over $H^*$.
Corollary 3.9(b) gives addition for $H\subseteq H^*$.
Finally, $H^*/H=t(G/H)$, so Proposition 5.4 supplies addition in $G/H$ over $H^*/H$.
Corollary 5.6(b) proves (AT) for $H$.
The printed reference to Corollary 3.9(a) at this point is corrected below.

For arbitrary $G$, first use the chain $t(G)\subseteq H+t(G)\subseteq G$.
Proposition 5.4 and the torsion-free result on $G/t(G)$ give addition over $H+t(G)$.
In the second chain $H\subseteq H+t(G)\subseteq G$, the intermediate quotient $(H+t(G))/H$ is torsion.
Lemma 5.7(a) handles its appearance as a quotient; Lemma 5.7(b) handles its appearance as a subgroup of $G/H$.
Corollary 5.6(b) completes Theorem 1.1.
Every subgroup used in these steps is invariant.

## Dependencies and acceptance boundaries

| Input | Exact role and inspection |
| --- | --- |
| DGB16, Lemma 2.2, Remark 2.3, Propositions 2.6 and 2.8, and (2.3) | Existence of entropy; cofinal finite sets; zero hyperkernel entropy; conjugacy, logarithmic law, directed continuity and direct-product addition. Statements and relevant proofs/interfaces read here; fuller foundational check in DGB16-U001. |
| DGB16, Lemma 3.5, Proposition 3.7, Corollaries 3.9-3.10, Lemma 4.3 and Proposition 4.7 | Infinite cyclic-flow case; divisible-hull invariance; essential and pure subgroups; bounded torsion in a finite flow; simultaneous finite-flow reduction. The actual hypotheses needed above were checked. Corollary 3.6's torsion zero-entropy criterion remains an upstream cited input as recorded in DGB16-U001. |
| [GBV15](../../../literature/pdf/GBV15.pdf), arXiv:1111.1287v3, 2013-02-19, pp. 3-4 | The primary-source statement says $h_A(\psi)=m(s\chi_\psi)$ for every endomorphism of $\mathbf Q^n$, $n\ge1$, where $s>0$ is the minimal integral denominator. Natural logarithms, multiplicities and the leading coefficient agree with DGB16. The discrete counting-measure definition agrees with $h$; finite sets containing zero are cofinal. **Accepted established external input after statement and applicability checks; original proof not reviewed.** See the retained. |
| Torsion Addition Theorem, source reference [16] in DGB16 | Used in Lemma 5.7 for torsion ambient groups, with invariant subgroups and $h=\mathrm{ent}$. Its role and applicability are explicit in DGB16, pp. 614 and 639-640. Retained cited input reported through DGB16; the original [16] was not directly read or independently proof-audited for this unit. This is a boundary of the whole dependency audit. |
| Bounded pure-subgroup splitting, source reference [22, Section 27.5] in DGB16 | Used through Lemma 4.3(b). The torsion subgroup is pure and bounded in the reduced finite flow, so the stated splitting input applies. Retained standard input reported through DGB16; the cited book passage and original proof were not directly inspected. |
| Source references [4, Theorem 0.1] and [26, Section 58, Theorem 1] in DGB16 | Their exact finite-quotient and stabilized linear-decomposition interfaces were directly checked by the elementary arguments above. No assertion is made about independently verifying those bibliographic attributions or the original proofs. |

The source's established torsion theorem and bounded splitting theorem are retained explicitly as external foundations.
The scope assessment certifies the checked Section 5 reasoning over these inputs; it does not label all upstream literature independently audited.
No project Claim, Task completion or manuscript adoption is selected by this unit.

## Located source corrections and their effect

All items below are existing features of the supplied published article, newly recorded in this source audit.
The supplied PDF is preserved.

| Severity and locator | Trigger, effect, correction and verification |
| --- | --- |
| P3, p. 636 (PDF p. 25), paragraph immediately before Proposition 5.3 | The source writes the extended skew map as $s_\phi\in\operatorname{End}(G\times H)$, although its construction is the endomorphism of $G=K\times H$ given by $(x,y)\mapsto(0,s_\phi(x))$. The displayed difference $\phi-\pi_\phi$ is in $\operatorname{End}(G)$. Read the former ring as $\operatorname{End}(G)$; otherwise the types do not match. Confirmed in the rendered page. Proposition 5.3 itself uses the correct map, so its proof is unaffected. |
| P3, p. 642 (PDF p. 31), proof of Proposition 5.10 | The text cites Corollary 3.9(a) for addition on the essential subgroup $H\subseteq H^*$. Part (a) only states entropy equality with the purification; the explicit essential-subgroup addition conclusion is part **(b)**. Use Corollary 3.9(b), whose hypotheses hold. Confirmed by comparing the displayed Corollary 3.9 on p. 629 with the rendered p. 642 citation. The required result is already proved earlier in the source, so this repairs a locator rather than introducing a new theorem. |

The positive stabilization exponent and nonzero vector qualifications in the hyperkernel proof were also made explicit above.
No failed mathematical implication remains in the inspected Section 5 reduction chain after these readings; in particular, no infinity subtraction, unjustified finite-rank assumption, or unjustified general quotient-hyperkernel identity is needed.

## Access, search and reuse limits

The complete Section 5 proof was read from the local published artifact's extracted text, and rendered pages resolved overbars, nested quotient maps, block matrices and the two cited source slips.
GBV15's current arXiv landing page identified v3; its exact-version HTML and the subsequently retained v3 PDF were read for the introductory theorem and normalization, with PDF pp. 3-4 visually inspected.
Direct web requests for the versioned PDF initially failed in the web tool; the linked current PDF and exact-version HTML succeeded, and the parent audit retained the versioned PDF separately.
This access check did not inspect GBV15's full proof or establish page-for-page identity with its 2015 journal version.
No computational experiment or proof-assistant check was used.

The user requested literature entry and audit; there is no newly assigned mathematical research objective and no local specialization beyond explaining the source proof.
Source-level metadata and any bounded errata search are owned by the [source reading map](readme.md).
Future reuse must preserve the abelian setting, forward trajectories, invariant-subgroup condition and entropy normalization.
Nonabelian analogues, arbitrary topological groups and stronger hyperkernel statements are outside this unit.
