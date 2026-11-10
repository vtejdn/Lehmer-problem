---
author: Yin
---

# McM02: canonical Coxeter conventions, the small spectrum and the degree-18 extension

<a id="mcm02-u002"></a>
## Source and inspection scope

Use the [retained published PDF](../../../literature/pdf/McM02.pdf), printed pages 151--183 corresponding to one-based PDF pages 1--33.
The selected passages are the canonical action and radical conventions in Section 3, printed pages 161--162, Theorem 7.6 on page 179, and Corollary 7.8, Theorems 7.9--7.10, Table 6, Figure 7 and Corollary 7.11 on pages 180--182.
Table 6, including all six exact polynomials, was checked visually on page 180, and the statement and printed proof of Theorem 7.9 were read on pages 180--181.
Figure 7 and the complete degree-18 example and corollary were checked visually on pages 181--182.
The [previously retained canonical-gap inspection](#canonical-coxeter-gap-input) supplies the precise Theorem 1.1 scope.
This unit records statement, diagram and applicability reading; it does not independently audit Vinberg's reflection-group description, the small-Salem classification used in Theorem 7.9, or the spectral-gap proof.

<a id="small-canonical-spectrum"></a>
## The uniform classification below 1.3

Theorem 7.9, printed page 180 / one-based PDF page 30, states that for a Coxeter system $(W,S)$ and any $w\in W$ with $1<\lambda(w)<1.3$, the value $\lambda(w)$ is one of the six Salem numbers in Table 6, and that all six occur.
Here the finite generating set and the canonical real geometric action are the global conventions of the introduction and Section 3, printed pages 151 and 161--162 / PDF pages 1 and 11--12.
The statement is uniform over all such finite-generator Coxeter systems and all their elements, not just Coxeter elements, one rank, one Lorentzian lattice, or the group $Y_{2,3,7}$.
It imposes no initial irreducibility, crystallographic, hyperbolic-signature or Salem-number hypothesis.
Corollary 7.8 first establishes that a canonical spectral radius in $(1,\lambda_{\mathrm{Pisot}})$ is Salem; the proof of Theorem 7.9 then restricts which systems can contribute below $1.3$.
This is not a classification of spectral radii in arbitrary integral orthogonal representations of abstract Coxeter groups.

The following $S_i$ and row labels are local notation for the exact Table 6 entries, in the source's displayed increasing order.
For each row, $\lambda_i$ is the unique real root greater than one of its irreducible Salem polynomial $S_i$.
The source explicitly describes its first column as approximate; these decimals are not certified isolating intervals.
The $\beta$ notation denotes the source's Coxeter eigenvalue, while a group name without $\beta$ records an occurrence as the radius of a suitable element.

| Row | Displayed $\lambda_i$ | Exact $S_i(x)$ | Source realization data |
| --- | --- | --- | --- |
| 1 | $1.17628$ | $1+x-x^3-x^4-x^5-x^6-x^7+x^9+x^{10}$ | $\beta(Y_{2,3,7})$ |
| 2 | $1.21639$ | $1-x^4-x^5-x^6+x^{10}$ | $Y_{2,3,7}$ |
| 3 | $1.23039$ | $1-x^3-x^5-x^7+x^{10}$ | $\beta(Y_{2,3,8})$ |
| 4 | $1.26123$ | $1-x^2-x^5-x^8+x^{10}$ | $\beta(Y_{2,3,9})$, $Y_{2,3,7}$ |
| 5 | $1.28064$ | $1-x^3-x^4-x^5+x^8$ | $\beta(Y_{2,3,10})$, $\beta(Y_{2,4,5})$ |
| 6 | $1.29349$ | $1-x^2-x^3+x^5-x^7-x^8+x^{10}$ | $\beta(Y_{2,3,11})$, $Y_{2,3,7}$ |

The first polynomial is the Lehmer polynomial in Theorem 1.1.
The assertion that all six arise does not mean that each occurs in every Coxeter system.

<a id="small-spectrum-proof-scope"></a>
The printed proof on page 181 / PDF page 31 was read for its dependency and scope reduction, not independently audited.
After reducing to an irreducible system and an essential element, the applicable inequality is $1<\beta(W,S)\le\lambda(w)<1.3$, as stated in the preceding Corollary 7.8.
The proof of Theorem 7.9 prints a strict inequality at this intermediate place, but the non-strict form suffices for its restriction and includes the equality cases realized by Coxeter elements.
Theorem 7.6 and the lower bound supplied by $Y_{2,3,12}$ reduce the systems to $Y_{2,4,5}$ or $Y_{2,3,n}$ with $7\le n\le11$.
The algebraic degree is even and at most the number of generators, hence at most 14 in this reduced list.
The proof uses the catalog cited as [B1], D. Boyd, *Small Salem numbers*, Duke Mathematical Journal 44 (1977), 315--328, which it states is complete through degree 20, together with lower bounds for the degree-12 and degree-14 cases.
Those ranges leave the one degree-8 and five degree-10 entries above.
Realization uses the indicated bicolored Coxeter eigenvalues and the unramified degree-10 realization theorem together with $O^+(II_{9,1})=Y_{2,3,7}$ in its geometric representation.
Thus the theorem's exhaustiveness is not a claim that the nearby list of 47 then-known Salem numbers below $1.3$ was complete in unbounded degree.
No independent Boyd-catalog check, enumeration of minimal diagrams, audit of Theorem 7.6, or verification of the realization theorem was performed in this reading.
The published classification is available at its stated external-theorem scope; a consumer must still match the canonical representation and record its own adoption.

<a id="six-fifths-threshold"></a>
## The six-fifths specialization and its finite arithmetic obligation

The inspected passage states its exact classification for $(1,1.3)$, rather than a separate theorem for $(1,6/5)$.
The displayed ordering places only the Lehmer entry below $6/5$.
For a rigorous application at that rational threshold, the exact Table 6 inputs reduce the remaining comparison to
\[
S_1(6/5)>0,\qquad S_i(6/5)<0\quad(2\le i\le6).
\]
These six sign evaluations, or equivalent certified root isolations, should be supplied rather than treating the displayed decimals as interval bounds.
They may be performed by integer arithmetic after multiplication by $5^{\deg S_i}$; this source preparation does not report an executed arithmetic certificate.

The reason these signs suffice is the Salem factorization
\[
S_i(x)=(x-\lambda_i)(x-\lambda_i^{-1})
       \prod_j(x^2-2\cos\theta_j\,x+1).
\]
For real $x>1$, every factor except $x-\lambda_i$ is positive, so the polynomial sign locates $x$ relative to $\lambda_i$.
Together with Theorem 7.9, the stated signs would certify that a canonical Coxeter spectral radius strictly between one and $6/5$ equals the Lehmer value.
This needs no new census of Salem numbers or extension of the source classification.
It does need the indicated exact comparison and a proved canonical-representation interface for the actual project matrices.
No canonical cover for fixed-cusp words with positive Gram $I_g$ is assumed or constructed here.
Nor does a spectral-radius statement by itself control the complete Mahler measure of a general matrix: a consumer identifying the two quantities must supply its complete exterior-root argument.

<a id="lorentzian-root-subgroup"></a>
## The actual group and exceptional coset

McM02 defines $O^+(II_{p,1})$ to be the index-two subgroup of the full integral orthogonal group preserving one sheet of the negative-unit hyperboloid.
This is a cone-preserving convention, not a determinant-one convention or an unspecified spinor kernel.
On printed page 180 it identifies $O^+(II_{9,1})$ with $Y_{2,3,7}$ in its geometric representation, citing Vinberg and Conway--Sloane.
On page 181 it states that the root reflections of $II_{17,1}$ generate the Coxeter subgroup $W$ of index two in $O^+(II_{17,1})$, with diagram Figure 7.

<a id="degree18-polynomial"></a>
The polynomial displayed immediately after Figure 7 is
\[
H(x)=1-x+x^2-x^3-x^6+x^7-x^8+x^9-x^{10}
     +x^{11}-x^{12}-x^{15}+x^{16}-x^{17}+x^{18}.
\]
It agrees coefficient by coefficient with H_ascending in [J144's fixed input](../../../computations/programs/Yin_J_G0144/trace56_cell.json).
Corollary 7.11 states that its Salem root, approximately $1.188368$, occurs as the spectral radius of an element of $O^+(II_{17,1})$ but not of an element of $W$.
The source then specifies $g=g_1g_2$, where $g_1$ is induced by the order-two symmetry of Figure 7 and $g_2$ is a bicolored Coxeter element of a $Y_{2,3,7}$ subdiagram.
This is an existing source example, not a new value or a newly verified matrix.

The source's nonmembership statement is stronger than merely failing the Lehmer lower bound: it uses [Theorem 7.9's uniform list](#small-canonical-spectrum) of the six Salem spectral radii below $1.3$ in canonical Coxeter representations.
The root of $H$ is absent from that list.
Indeed the displayed irreducible degree-18 polynomial differs from every degree-8 or degree-10 polynomial in Table 6, so the classification excludes this number from all canonical Coxeter spectral radii in its range, while Corollary 7.11 identifies the particular lattice extension where it occurs.
The index-two extension must not be replaced by $W$ when applying Theorem 1.1.
Squaring an element of $O^+(II_{17,1})$ places it in $W$, but squares its spectral radius and doubles its complete logarithmic Mahler measure.
Thus a gap transferred through this index-two step has the square-root threshold, not the unaltered Lehmer threshold.
No such power is part of the unchanged-polynomial construction requested here.

<a id="figure-seven-recipe"></a>
## Exact combinatorial transcription of Figure 7

The source diagram is unlabelled; the following labels and column-action matrices are an explicit transcription of its canonical convention.
Label the horizontal chain $h_1,\ldots,h_{17}$ from left to right, and label the two extra leaves $\ell,r$.
The edges are
\[
\{h_i,h_{i+1}\}\ (1\le i\le16),\qquad
\{h_3,\ell\},\qquad \{h_{15},r\}.
\]
There are 19 vertices.
With coordinate order $(h_1,\ldots,h_{17},\ell,r)$, put $B_{ii}=2$, $B_{ij}=-1$ on the displayed edges, and $B_{ij}=0$ otherwise.
These are simple Coxeter edges of exponent three; missing edges have exponent two.
For each vertex $i$, use the column-action reflection
\[
S_i=I-e_i(e_i^{\mathsf T}B),\qquad S_i(v)=v-B(e_i,v)e_i.
\]
Let $\Pi$ be the permutation matrix sending $h_i$ to $h_{18-i}$ and exchanging $\ell$ with $r$.
This transcribes the source's diagram involution.

Choose the left subdiagram on $\{h_1,\ldots,h_9,\ell\}$, centered at $h_3$.
Its arm edge lengths are $1,2,6$, hence it is $Y_{2,3,7}$ in the source's convention.
Its two color classes are
\[
A=\{h_1,h_3,h_5,h_7,h_9\},\qquad
D=\{h_2,h_4,h_6,h_8,\ell\}.
\]
Reflections within either class commute, so a concrete version of the recipe is
\[
C=\left(\prod_{i\in A}S_i\right)
  \left(\prod_{j\in D}S_j\right),\qquad G=\Pi C.
\]
The rightmost factor acts first.
The source specifies the diagram symmetry and a bicolored subdiagram element, but does not print these vertex labels or a 19-by-19 matrix.
The above choice is therefore a source transcription to be checked exactly, not an independently verified characteristic-polynomial certificate.

<a id="integral-model-verification"></a>
## Integral quotient and generator-coverage limits

Figure 7 has 19 vertices while the target lattice has rank 18.
The canonical reflection matrices act on the free space on the vertices; that space cannot simply be identified with an 18-dimensional integral lattice.
Section 3 explains that the Coxeter group fixes the radical of its canonical form and that its quotient carries the nondegenerate action.
A diagram automorphism can act nontrivially on that radical, so an extra factor in the 19-dimensional characteristic polynomial must be identified rather than discarded without a quotient calculation.

The direct finite verification should determine the primitive integer radical $N=\ker(B)\cap\mathbb Z^{19}$, an integral basis of $\mathbb Z^{19}/N$, and the induced form and action.
It must check rank 18, evenness, signature $(17,1)$, determinant $-1$, integrality of the induced matrix and complete characteristic polynomial $H$.
If the root-lattice quotient is not unimodular, the source's group identification alone is not an explicit overlattice certificate; an actual invariant unimodular overlattice would still have to be specified and checked.
No rank, determinant, quotient or characteristic-polynomial computation is performed in this source preparation.

For a chosen splitting $L=H_0\oplus U$, positive-summand isometries extended by the identity fix the negative vector $e-f$, and hence preserve the selected cone component.
The integral Eichler transvections also preserve that component, as follows from their real one-parameter formula, and have determinant one.
Consequently these permitted generators lie in $O^+(L)$; the statements above do not identify each with an element of $W$ or show that together they generate all of $O^+(L)$.
An arbitrary positive-summand isometry can have either determinant sign.
The [GHS09 spinor conventions and two-plane generation hypotheses](../GHS09/Yin_U001.md#integral-transvection-groups) remain separate and cannot be substituted for the cone convention here.
In particular, a norm-two transvection can be expressed using the two integral root reflections in the [existing local identity](../../../ledger/Yin_L_G0462_v13.md#integer-generators); extending that observation to every parameter requires the actual integral root-span or another argument.
The source recipe does not specify a fixed integral hyperbolic splitting in which the diagram involution becomes a positive-summand isometry, or a word in the prescribed two cusp groups.
Those are distinct tests after verifying the complete integral model.

<a id="canonical-coxeter-gap-input"></a>
## Accepted statement and exact convention scope

Source/version: [McM02, published 2002 PDF](../../../literature/pdf/McM02.pdf), as already acquired.
The bibliography and artifact acquisition record remain authoritative there; no new artifact, download, hash or source identity was created in this reading.

Date/reader: 2026-10-10, orbit_research AI for Yin, during the authorized G0001 D105 round.
Coverage state: **Read; established external theorem accepted at statement/applicability depth**.
This is not an independent review of McM02's full proof or finite classification.

Trigger/intended use: L234 makes the complete absolute-companion/original measure ratio tend to zero with growing original total measure.
The new question is whether the same can happen with bounded positive original measure.
L185 supplies positivity and an adjacency-dependent lower bound, but not a uniform constant.
D9 and L185 had inspected McM02 for motivation/comparison and expressly had not adopted its full gap theorem.
A local check found no existing McM02 source unit or source home; this compact record owns the newly selected input rather than changing those historical scopes.

Exact passages text-read from the retained PDF: Introduction Theorem1.1 and equation(1.1), printed p.151/PDF p.1; surrounding action and bicolored/classification summary, printed pp.152--154/PDF pp.2--4; Section3's Coxeter-system, form and geometric-action conventions, printed pp.161--162/PDF pp.11--12.
The extraction was clear for the consumed formulas.
No rendered diagram or table is an evidential premise, and no full proof of Sections2--6 or enumeration of minimal hyperbolic diagrams was inspected in this round.

The accepted theorem is: for every finite-generator Coxeter system (W,S) and every w in W, the spectral radius lambda(w) of its canonical real geometric action is either1 or at least lambda_Lehmer, the Salem number specified by equation(1.1).
That equation is the complete polynomial t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.
It is a spectral-radius statement for that representation, not a theorem about arbitrary signed integral matrices or all lattice isometries.

The source uses basis e_s and B(e_s,e_t)=-2 cos(pi/m(s,t)), including diagonal2 because m(s,s)=1.
The action is s(v)=v-B(e_s,v)e_s.
For an infinite Coxeter exponent it sets the off-diagonal form value to-2.
Consequently symmetric Gram off-diagonal entries0,-1,-2 correspond exactly to exponents2,3,infinity.
The radical is fixed pointwise; the quotient carries the induced nondegenerate form, and the source records reciprocal spectral-radius symmetry in(3.1).
No positive-definiteness, nonsingularity, connectedness, hyperbolic-signature or finite-order hypothesis is imposed in Theorem1.1.

Acceptance decision: after checking these statements and conventions, accept Theorem1.1 as an established external input for this authorized local deduction under the repository's accepted-external-input rule.
No concrete objection or version discrepancy affecting this use was found.
Its original geometric/classification proof remains unreviewed here, and no computational or formal verification is claimed.
The integer unitriangular-to-reflection product identity, treatment of entries of absolute value at least3, Mahler-versus-spectral-radius comparison and bounded-measure ratio consequence are separate local proofs in [L_G238](../../../ledger/Yin_L_G0238_v1.md#uniform-companion-gap-and-bounded-ratio); they are not quoted as source statements.
The path-extension construction in that retained argument instead reuses the already accepted L203/Hir06 scope.

Search/stopping boundary: the existing D9/L185 source-role records and the exact retained primary source were read.
No external search or new acquisition was needed.
Stop at this sufficient theorem/convention interface; no broad novelty assertion, whole-source audit, acceptance of a general signed-matrix gap, or unrestricted Lehmer conclusion follows.
A future use with other Gram entries must prove its own canonical-representation or separate comparison interface.
