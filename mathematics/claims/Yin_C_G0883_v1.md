---
author: Yin
---

# A homological Mahler gap for bounded normalized pseudo-Anosov entropy

<a id="statement"></a>
## Precise statement

For each real \(C>0\), there is a number \(\eta_C>0\) with the following property.
Let \(S_g\) be a closed connected orientable surface of genus \(g\ge2\), and let \(f:S_g\to S_g\) be an orientation-preserving pseudo-Anosov homeomorphism of stretch factor \(\lambda(f)>1\).
Suppose
\[
                    (2g-2)\log\lambda(f)\le C.
\]
For the full integral homological characteristic polynomial
\[
             P_f(t)=\det(tI-f_*|H_1(S_g;\mathbb Z)),
\]
one has
\[
                      m(P_f)=0\quad\hbox{or}\quad m(P_f)\ge\eta_C.
\]
The logarithmic Mahler measure is the total measure, counting all roots with their multiplicities.

A stronger intermediate assertion applies to any fixed finite collection of mapping tori of orientation-preserving homeomorphisms of compact connected orientable surfaces with nonempty boundary.
Among all such fibrations of these mapping tori, the whole first-homology characteristic polynomials have a uniform positive Mahler gap.
The same gap applies after filling any invariant collection of punctures whenever the monodromy extends to the filled orientable surface.
No assertion about arbitrary individual noncyclotomic factors of these characteristic polynomials is made.

<a id="external-inputs"></a>
## External inputs and their inspected scope

[FLM11's retained author edition](../audits/literature/FLM11/readme.md) defines \(\Psi_P\) by \(\lambda(f)\le P^{1/|\chi(S)|}\).
Its Theorem 1.1 on printed/PDF page 1 says that the mapping tori of restrictions obtained by puncturing all singularities of the invariant foliations range over a finite set of homeomorphism types for each fixed \(P\).
The definition, puncturing convention and theorem statement were read directly.
The theorem is accepted as an established external input, with its original proof unreviewed here.

[DGT23's retained author edition](../audits/literature/DGT23/readme.md), Section 4 and Corollary 4.10 on printed/PDF pages 19--20, concerns a graph map \(h:G\to G\), its mapping torus \(X\), the group \(\Gamma=\pi_1(X)\), and the dual primitive integral class \(u\).
Write \(H=H_1(\Gamma;\mathbb Z)/\operatorname{torsion}\).
For its integral Alexander polynomial \(\Delta_\Gamma\in\mathbb Z[H]\), the corollary gives, up to a unit of \(\mathbb Z[t^{\pm1}]\),
\[
 \det(t^{-1}I-h_*|H_1(G;\mathbb Z))
       =(1-t)^p\Delta_\Gamma^u(t),\qquad
 p=\begin{cases}1,&\operatorname{rank}H\ge2,\\0,&\operatorname{rank}H=1.\end{cases}
 \tag{1}
\]
Here \(\Delta_\Gamma^u\) substitutes \(t^{u(v)}\) for each group monomial \(v\).
The general graph-map setting, the exact corollary, its short characteristic-polynomial argument and Remark 4.11 were inspected.
The complete Alexander determinant theorem used by the source was not independently proof-audited.

The accepted [DS17 fixed-support theorem](../audits/literature/DS17/Yin_U001.md#ds17-u001) supplies \(\eta_K>0\) for every fixed number \(K\) of nonzero monomials in a nonzero integer polynomial.
Its scope is independent of degree, exponents, coefficient height and irreducibility.
We use its one-variable consequence at that existing source-inspection scope.

<a id="fixed-mapping-torus"></a>
## The whole measure for a fixed mapping torus

Fix a mapping torus \(M\) as in the intermediate assertion, and put \(\Gamma=\pi_1(M)\).
A compact connected surface \(S\) with nonempty boundary deformation retracts onto a finite connected graph \(G\).
Using that retraction and an inverse inclusion, a monodromy on \(S\) gives a graph map representing the same automorphism of \(\pi_1(S)\).
The two mapping tori have the same group with the same dual class, and their induced first-homology maps agree under the retraction.
Thus (1) applies to every chosen fibration of \(M\).

Choose one representative of \(\Delta_\Gamma\) and write it as a finite integral Laurent sum.
Every primitive integral fibration class \(u\) factors through \(H\).
Its specialization is nonzero, because the left side of (1) is nonzero.
Coincident exponents may merge or cancel terms, so the number of nonzero monomials of \(\Delta_\Gamma^u\) is at most the fixed support size \(K_M\) of \(\Delta_\Gamma\).
A change of basis of \(H\), or multiplication of \(\Delta_\Gamma\) by a group-ring unit, preserves this support size.

Substitution \(t\mapsto t^{-1}\), multiplication by a Laurent unit and multiplication by \(1-t\) preserve logarithmic Mahler measure.
Taking measure in (1) therefore gives the exact identity
\[
                   m(P_{S,f})=m(\Delta_\Gamma^u).
 \tag{2}
\]
Multiplying the specialization by a monomial makes it an ordinary nonzero integer polynomial without changing its measure or support size.
DS17 now gives \(m(P_{S,f})=0\) or \(m(P_{S,f})\ge\eta_{K_M}\).
For a finite collection of mapping tori, take the minimum of their finitely many positive constants.

<a id="filling-punctures"></a>
## Filling punctures preserves the whole measure

Suppose an orientation-preserving monodromy permutes a finite nonempty invariant set \(A\) of punctures, and let \(S\) denote the surface after filling them.
The natural map \(H_1(S\setminus A;\mathbb Q)\to H_1(S;\mathbb Q)\) is surjective.
Its kernel is generated by the small positively oriented meridians about the points of \(A\), subject to the homological relations of the filled surface.
The induced action on these meridians is a permutation.
Consequently its action on the invariant kernel has finite order, and its characteristic polynomial is monic integral with all roots roots of unity.
Equivalently the kernel can be calculated over the invariant integral kernel, which is a free abelian subgroup of \(H_1(S\setminus A;\mathbb Z)\).
The characteristic polynomial of the punctured monodromy is the product of that of the filled monodromy and this cyclotomic polynomial.
It follows that their total logarithmic Mahler measures are equal.
For a closed connected filled surface and \(s=|A|\), the meridian kernel is the permutation module on \(s\) points modulo its diagonal invariant line.
Its dimension is \(s-1\).
This also treats a single filled puncture, when the kernel is zero.

<a id="bounded-normalized-entropy"></a>
## Deduction for bounded normalized entropy

Apply FLM11 with \(P=e^C\).
A closed orientable surface of genus at least two has singularities in a pseudo-Anosov invariant foliation, so puncturing the finite singularity set gives a nonempty-boundary surface after replacing punctures by boundary circles.
The singularity set is invariant under the monodromy.
FLM11 gives finitely many mapping-torus homeomorphism types for these punctured maps under the stated normalized-entropy bound.
The fixed-mapping-torus argument supplies a common positive gap for their whole first-homology characteristic polynomials.
The puncture-filling argument transfers exactly the same measure to \(P_f\), proving the statement.

The induced map on the closed surface preserves the integral intersection pairing.
Thus \(P_f\) is a monic reciprocal integer polynomial with constant coefficient one, an actual input to the [unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract).
The argument gives a restricted gap and no numerical value for \(\eta_C\).
It imposes no orientability assumption on the invariant foliations.

## Assessment history

### Decision bounded-normalized-entropy-gap

| Field | Value |
| --- | --- |
| date | 2026-11-09T08:54 |
| status | proved |
| reason | Independent review checked the complete fixed-mapping-torus argument, exact filling identity and normalized-entropy deduction at the disclosed accepted-external-input depth. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Homological gap](#statement) | Complete bounded-normalized-entropy assertion and the fixed finite mapping-torus intermediate assertion. |
| argument | [Fixed mapping tori](#fixed-mapping-torus) | Exact Alexander specialization, fixed support size and complete homological measure. |
| argument | [Filling punctures](#filling-punctures) | Finite-order meridian kernel and equality of full measures. |
| argument | [Normalized entropy](#bounded-normalized-entropy) | Finite-source theorem, all hypotheses and transfer to closed surfaces. |
| dependency | [Inspected external inputs](#external-inputs) | FLM11 Theorem 1.1, DGT23 Corollary 4.10 and the accepted DS17 fixed-support theorem, at their stated inspection scopes. |
| review | [Independent whole review](../audits/reviews/Yin_R_G1109_v1.md#whole-topological-gap) | Complete statement, all argument sections and exact source applicability. |

## Current assessment

[Selected decision](#decision-bounded-normalized-entropy-gap)
