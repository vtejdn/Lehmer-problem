---
author: Yin
---

<a id="bv20-u003"></a>
# BV20-U003: The Lehmer gap and uniform growth of linear groups

## Source and inspection

[Source and edition notes](readme.md).

Source edition: BV20, [retained PDF](../../../literature/pdf/BV20.pdf), arXiv:1510.04043v4, 23 April 2021.

Passages: Conjecture 3 and Theorem 4, pp.2--3; complete Section 4, pp.23--30: Theorem 20, Corollaries 21,24,26,31, Lemmas 25,27,29,33 and Remarks 22--23,28,30,32,34.
Printed and PDF page numbers coincide.
Section 5 is recorded in U002.

Inspection: 2026-10-06, human author Yin.
The assigned AI source-review agent read the full mathematical body and checked this reduction and record.
Root and a second source-review agent separately read Section 4 and cross-checked the main local defects; this is independent checking of source passages, not an independent human review or an independently accepted project proof.
Rendered pp.27--30 were used to resolve algebraic-group fonts, subgroup notation and missing logarithms.
Original proofs of the external algebraic-group and uniform-Tits inputs were not recursively audited.


## Assessment

**Audited within scope** for the qualitative growth/Lehmer reduction, with the explicit subgroup, coset and symbolic-constant repairs below, relative to the listed external structural inputs.
**Questioned** for the literal general field-of-definition assertion in Remark 28, its use in Remark 34/Corollary 24, the proof of Lemma 33 under its one-sided hypothesis, and unqualified reuse of the printed numerical constants.

No counterexample to the qualitative Theorem 4 is asserted.
This record does not certify the field refinement, the explicit rational-matrix bound of Corollary 24, or the original proofs of its cited foundational results.
It supports no newly created project Claim or Task.

<a id="bv20-growth-rate"></a>
## Growth rate and quantifiers

For a **nonempty** finite subset \(S\) of a group, let \(S^n\) be the set of products of exactly \(n\) elements of \(S\), and set
\[
\rho_S=\lim_{n\to\infty}\frac1n\log_2|S^n|.
\]
Submultiplicativity and Fekete's lemma give existence.
In a group, \(|S^i|\le |S^n|\) for \(i\le n\), by padding with a fixed element of \(S\).
Thus
\[
|S^n|\le|(S\cup\{1\})^n|\le(n+1)|S^n|,
\]
and adjoining the identity does not change the rate.
For a symmetric generating set containing the identity, these sets are the word-metric balls.
The paper permits **nonsymmetric** sets, so general \(S^n\) should not silently be replaced by those balls.

A group is *virtually* nilpotent or solvable if it contains a subgroup of finite index with that property.
The uniformity below is over both the group and its finite generating set in a fixed matrix dimension.
It is stronger than a separate positive lower bound depending on each individual group.

<a id="bv20-growth-gap"></a>
## Growth gap equivalent to the classical Lehmer gap

The source's Growth Conjecture is
\[
\forall d\ge1\ \exists\varepsilon_d>0\ \forall\,\varnothing\ne S\subset GL_d(\mathbb C)
\text{ finite},\qquad
\rho_S=0\quad\text{or}\quad\rho_S>\varepsilon_d.
\]
Theorem 4 equates it to the **existence** of \(\delta>0\) such that every algebraic number has \(M_\lambda=1\) or \(\log_2M_\lambda\ge\delta\).
This is the ordinary uniform-gap Lehmer conjecture, not the assertion that the optimal lower bound is Lehmer's degree-ten number, and not the house/Schinzel--Zassenhaus conjecture.

For non-virtually-solvable subgroups the requisite dimension-dependent growth gap is retained as the established uniform-Tits input cited on p.3.
Section 4 handles the virtually solvable case.
Replacing a non-strict lower bound by a strict inequality with half the constant has no mathematical effect on the stated quantifiers.

## Checked proof chain over the complex numbers

Write \(g_{a,b}(x)=ax+b\), so \(\operatorname{Aff}(\mathbb C)=\{\left(\begin{smallmatrix}a&b\\0&1\end{smallmatrix}\right):a\ne0\}\).
This is a solvable group; its commutator subgroup consists of translations.
It is already a subgroup of \(GL_2(\mathbb C)\).

1. **The model walk.**
   For \(S_\lambda=\{g_{\lambda,1},g_{\lambda,-1}\}\), \(\lambda\ne0\), an \(n\)-fold product has multiplier \(\lambda^n\) and translation a finite sign sum (with reversed independent digits).
   Consequently \(|S_\lambda^n|=|\operatorname{supp}\mu_\lambda^{(n)}|\) and \(\rho_{S_\lambda}=\rho_\lambda\).
   [U001](Yin_U001.md#bv20-u001) gives
   \[
   c_0\min\{1,\log_2M_\lambda\}\le h_\lambda\le\rho_\lambda\le\log_2M_\lambda.
   \]
   For transcendental \(\lambda\) no two sign polynomials coincide, so \(h=\rho=1\); Section 4 uses the explicit convention \(M_\lambda=2\) there.
   This convention is not a definition of an algebraic Mahler measure for transcendental numbers.
2. **Affine reduction, Lemma 25.**
   If a finite \(S\subset\operatorname{Aff}(\mathbb C)\) containing one generates a non-virtually-nilpotent group, some generator has multiplier of infinite order.
   Conjugate its fixed point to zero and choose another generator with a nonzero translation.
   Comparing \(s_0s\) with \(ss_0\), or \(s_0^2s\) with \(ss_0^2\), produces two elements of \(S^3\) with the same non-torsion multiplier and distinct translations.
   Affine conjugacy normalizes those translations to \(1,-1\).
   The slope cannot be zero or one.
   Hence \(\rho_S\ge(c_0/3)\min\{1,\log_2M_\lambda\}\).
3. **Upper triangular groups, Lemmas 27 and 29.**
   The source first constructs a diagonalizable complement to the unipotent radical when the commutator subgroup is unipotent; invariant flags then give simultaneous upper triangularization.
   For a non-virtually-nilpotent triangular group, induction on the dimension of a connected solvable ambient algebraic group isolates a one-dimensional weight space in the center of its unipotent radical.
   A nontrivial torus weight \(\chi\) and a cocycle \(\beta(g)=[h_0,g]\) yield the affine map \(g\mapsto g_{\chi(g),\beta(g)}\).
   Here \(\beta(gh)=\beta(g)+\chi(g)\beta(h)\), and \(\beta(\ker\chi)\ne0\), while \(\chi\) is nontrivial on the identity component.
   These facts ensure the image is not virtually nilpotent.
   Zariski density transfers that property back to the original subgroup.
   This paragraph uses the complex-field structural interfaces below, not the disputed rational-point assertion of Remark 28.
4. **Finite-index triangularization.**
   Let \(\Gamma=\langle S\rangle\) and \(G=\overline\Gamma^{\rm Zar}\).
   A maximal torus \(T\) of \(G^\circ\) has normalizer/centralizer quotient of order at most \(d!\), by the permutation action on its weight spaces.
   Platonov's finite-component subgroup and Jordan's theorem supply an abelian subgroup \(A\) giving a triangularizable subgroup \(AG^\circ\) with index at most \(m=d!J(d)\).
   Here \(J(d)\) bounds the index of an abelian normal subgroup in any finite subgroup of \(GL_d(\mathbb C)\).
5. **Return to the discrete subgroup correctly.**
   Put \(H=\overline{\Gamma\cap AG^\circ}^{\rm Zar}\) and **\(H_0=\Gamma\cap H\)**.
   Use \(H_0\), not the algebraic group \(H\), for subgroup indices and cosets in \(\Gamma\); \([\Gamma:H_0]\le m\).
   Let \(S_0=S^m\).
   The finite left and right coset graphs are reachable by positive words; paths of length at most the number of cosets minus one suffice.
   Since \(1\in S\), \(\Gamma=S_0H_0=H_0S_0\).
   These two coset-covering properties repair the precise Lemma 33 application; see F2.
   The affine map restricted to \(H_0\) still has non-virtually-nilpotent image by density.
   Lemma 33's repaired argument finds that image already on \(\langle S_0^3\cap H_0\rangle\).
6. **Growth bound and equivalence.**
   Applying the affine bound and dividing word lengths gives, for a suitable non-torsion \(\lambda\),
   \[
   \rho_S\ge\frac{c_0}{9d!J(d)}\min\{1,\log_2M_\lambda\}.
   \]
   Thus Lehmer supplies the required gap for virtually solvable subgroups, and the retained non-virtually-solvable input covers the remainder.
   Conversely, the dimension-two growth gap applied to \(S_\lambda\), together with positivity from Theorem 5 and \(\rho_\lambda\le\log_2M_\lambda\), yields the Mahler gap whenever \(M_\lambda>1\).
   Nonunits already have \(M\ge2\).
   This verifies the converse using statements checked inside BV20 rather than treating its citation of the earlier Breuillard paper as an extra unaudited proof step.

Virtually nilpotent finitely generated groups have polynomial growth, hence rate zero.
For virtually solvable linear groups the other branch of the reduction has positive rate.
The qualitative dichotomy therefore has exactly the scope used in Theorem 4.

<a id="bv20-u003-findings"></a>
## Findings and reproducible checks

The following are existing source issues checked on 2026-10-06.
The repairs are local completions of the source argument; they do not establish a new project theorem or close the separate arithmetic refinement.

- **F1 -- medium, Remark 28 p.27: the rational-point assertion is false as universally stated.**
  The remark says that for a \(K\)-defined upper triangular algebraic group one can choose the finite component-covering group \(F\) of Lemma 27 inside \(G(K)\).
  Take \(K=\mathbb Q\) and \(G=\mu_3=\{z\in\mathbb C^*:z^3=1\}\subset GL_1\).
  It is \(\mathbb Q\)-defined and upper triangular, but \(G^\circ=\{1\}\) and \(G(\mathbb Q)=\{1\}\).
  No \(F\subset G(\mathbb Q)\) has \(G=FG^\circ\).
  In Remark 34 p.30 the same remark is also invoked before the relevant upper triangularization over the field is established.
  A dense rational-point hypothesis might help a narrower application, but this audit does not supply the required descent proof.
  The claimed degree-\(d!\) field control and Corollary 24 remain outside the closed proof scope.
- **F2 -- medium, Lemma 33 p.29: wrong-side Schreier-generation step.**
  The hypothesis is \(G=SH\), but the proof asserts that \(H\) is generated by \(s_1s_2s_3^{-1}\in H\), the usual conclusion for the opposite coset cover \(G=HS\).
  To reproduce the failure of this intermediate assertion, use right-to-left composition in \(S_4\), \(H=\operatorname{Stab}(4)\), and the one-line permutations
  \[
  S=\{1234,4123,4312,4231\}.
  \]
  Then \(1\in S\), \(\langle S\rangle=S_4\), and \(SH=S_4\), whereas \((SSS^{-1})\cap H=\{1234,2314,3124\}\) generates \(A_3\), of order three, rather than \(H\), of order six.
  A direct finite enumeration of products and generated subgroups was independently rerun in this audit.
  This is **not** a counterexample to the full lemma, since a finite \(H\) has no non-virtually-nilpotent affine image.
  In the main application, \(S_0=S^m\) covers both coset directions, as proved above.
  With both covers, the source's argument works: the \(HS_0\) cover gives the stated Schreier generators; the \(S_0H\) cover supplies \(s_4\) with \(s_3^{-1}\in s_4H\) to replace inverse letters by positive words.
- **F3 -- medium reuse limitation, Corollary 26/Theorem 20 pp.25,23.**
  The fixed constants \(1/9\) and \(1/(27d!J(d))\) use a lower bound at least \(c_0\ge1/3\), while the source gives an unqualified analytic proof only of \(c_0>0\) and labels its `0.44` calculation non-rigorous.
  This audit certifies the displayed symbolic constants in the proof chain, not those printed numeric constants.
  Theorem 4 and Corollary 21 require only positivity and survive this distinction.
- **F4 -- low, Theorem 20 proof p.30: algebraic/discrete subgroup mismatch.**
  The defined \(H\) is a Zariski closure, not necessarily a subgroup of \(\Gamma\).
  Its alleged index in \(\Gamma\) and the expression \(S_0H=\Gamma\) must use \(H_0=\Gamma\cap H\).
  Restricting the map to \(H_0\), using density, and using \(S_0^3\cap H_0\) gives the valid application above without changing the index bound.
- **F5 -- low, local slips.**
  On pp.24 and26 the text says the affine image is “non-virtually solvable”; no such subgroup exists in the solvable affine group, and Lemma 29 correctly uses **non-virtually nilpotent**.
  On p.30 the application of Corollary 26 prints \(\rho\ge M_\lambda/9\), omitting \(\log_2\).
  Its actual cited bound has \(\log_2M_\lambda\), with the constant qualification in F3.
  These slips do not change the repaired qualitative argument.

## Retained structural inputs and unchecked scope

| Interface used | Source location and inspection boundary |
| --- | --- |
| Dimension-dependent growth gap for non-virtually-solvable complex linear groups | BV20 p.3 cites the uniform Tits alternative, references [11,14]. Its precise role and distinction from the virtually solvable branch were checked here. The original theorem/proof in those works was not separately audited; this remains an explicitly retained established structural input. |
| Finite linear group Jordan bound \(J(d)\) | BV20 p.23 and Remark 22. Only existence for each fixed \(d\) is used for Theorem 4. Neither the sharp factorial bound nor the original Jordan/Collins proof is independently certified here. |
| Finite subgroup meeting every complex algebraic-group component | BV20 Lemma 27, citing Platonov [42], Wehrfritz [50,10.10], Borel--Serre [5,5.11]. Retained **over \(\mathbb C\)**. Moving it to \(G(K)\) is precisely the disputed step, not an automatic field extension of this input. |
| Connected solvable algebraic groups | Lie--Kolchin, connectedness of closed unipotent groups in characteristic zero, maximal-torus conjugacy, the torus/unipotent decomposition and the centralizer-surjectivity interface are used at BV20 pp.26--28 with locators [30,17.6,18.4,19.3,19.4,21]. Their hypothesis matches and uses in the printed induction were inspected. The original textbook proofs were retained, not recursively checked. |
| Polynomial growth for finitely generated virtually nilpotent groups | Retained standard implication used only to identify the zero-rate branch; not an inference that all groups of zero rate are nilpotent. |

The paper's Corollary 24 states an unconditional lower bound \(c/d^{2d}\) for positive growth of virtually solvable subgroups generated in \(GL_d(\mathbb Q)\).
Its printed proof additionally uses Remark 34's field-degree control, Dobrowolski and the quantitative Jordan bound.
Those dependencies are identified, but F1 prevents this record from certifying that whole refinement.
This is a scoped proof issue, not a claim that the corollary is false.

The main theorem asserts an equivalence between two conjectures; it proves neither conjecture.
The discussion of solvable groups with fixed derived length in Section 5 is a separate uniformity question and is recorded in [U002](Yin_U002.md#bv20-u002).
