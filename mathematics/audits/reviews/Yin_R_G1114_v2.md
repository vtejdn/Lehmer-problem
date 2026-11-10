---
author: Yin
---

# Independent review of the uniform gap for two cyclic Eichler transvections

## Review arrangement and exact inputs

The review act is dated 2026-11-10T00:40, with Yin as the human record author.
A separately organized mathematical reviewer inspected the fixed [C885 v1 statement](../../claims/Yin_C_G0885_v1.md#statement), its [complete argument](../../claims/Yin_C_G0885_v1.md#argument) and its [research scope](../../claims/Yin_C_G0885_v1.md#research-scope), without participating in development of that proof.
The supplied mathematical inputs were the fixed proof, the necessary definitions and exterior reduction in [L462 v13](../../ledger/Yin_L_G0462_v13.md#integer-generators), and the accepted [DS17 univariate fixed-support theorem](../literature/DS17/Yin_U001.md#ds17-u001).
No development draft, proof-generation dialogue or substantive development summary was supplied.
The coordinator's notification of the final wording before equation (8) identified the fixed input and supplied no review conclusion.
The reviewer first reconstructed the obligations and checked the new complete-polynomial and uniform-estimate chain, then consulted [R1114 v1](Yin_R_G1114_v1.md#orthogonal-whole-review) for its actual earlier scope and the unchanged GHS13 attribution evidence.
That earlier finding supplies no review coverage for C885's new uniform estimate or whole-polynomial completion.
No substantive repair was contributed.

The review covers all mathematical assertions in C885 v1, including the unbounded parameter quantifiers, integrality, characteristic-polynomial normalization, uniform exterior estimate, zero-vector cases, support count, cyclotomic multiplier, source applicability and final limitation to the displayed family.
The DS17 theorem is retained at its existing accepted external-statement and applicability depth.
Its foundational proofs were not independently audited here, and the GHS13 original was not newly inspected.
No numerical search, solver, native mathematical program or formal verification was used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [C885 statement](../../claims/Yin_C_G0885_v1.md#statement) | Every stated parameter, zero case, whole-measure conclusion, numerical norm threshold and support bound. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [C885 complete argument](../../claims/Yin_C_G0885_v1.md#argument) | Integral isometries, determinant-preserving row operations, exact polynomial identity, uniform negative determinant, correlation sparsity and DS17 application. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [C885 research scope](../../claims/Yin_C_G0885_v1.md#research-scope) | Uniformity over the displayed family and the explicit absence of an unrestricted Lehmer or effective numerical-gap conclusion. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [L462 integral generators](../../ledger/Yin_L_G0462_v13.md#integer-generators) | Actual lattice, transvection, inverse and GHS13 attribution used by C885; the local identities were rechecked. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [L462 exterior reduction](../../ledger/Yin_L_G0462_v13.md#first-family) | Definitions and two-dimensional exterior equation used as the starting interface; C885's stronger complete-polynomial identity was independently checked. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [DS17 accepted input](../literature/DS17/Yin_U001.md#ds17-u001) | Exact nonzero univariate integer-polynomial consequence, total logarithmic normalization, fixed support and unrestricted degree and height. |
| [Whole argument finding](#cyclic-two-transvection-gap-review) | [Earlier source-attribution finding](Yin_R_G1114_v1.md#orthogonal-whole-review) | Reuse only of the unchanged GHS13 edition, formula locator and attribution boundary; no transfer of coverage to the new C885 proof. |

<a id="cyclic-two-transvection-gap-review"></a>
## Finding

No mathematical defect or unresolved applicability gap was found in the inspected C885 v1 argument.
The proof establishes an absolute positive gap for the complete logarithmic Mahler measures of all characteristic polynomials in its exact two-transvection family.
The same proof establishes the stated implication \(\|v\|\|w\|\ge650\Rightarrow M(P_A)>2\), the zero-vector formula, and the fixed support bound for the measure-preserving multiplier in the complementary branch.
The decisive checks follow.

### Lattice hypotheses, integrality and degenerate inputs

The positive-coordinate vectors are orthogonal to both hyperbolic basis vectors, so the transvection formula has exactly its required isotropic and orthogonality hypotheses.
Every lattice pairing is integral, and the even squared norms make \(a=\|v\|^2/2\) and \(b=\|w\|^2/2\) integers.
Expanding the transformed pairing gives the displayed cancellation term by term.
The value of \((e,x)\) is unchanged by \(T_{e,v}\), while \((v,x)\) changes by \(2a(e,x)\); substitution of \(-v\) therefore gives the inverse on both sides.
The same reasoning applies to \(T_{f,w}\).
The cyclic permutation preserves the positive dot product and fixes the hyperbolic plane, so the product is an integral invertible matrix.
Consequently \(P_A\) is a nonzero monic integer polynomial of degree \(g+2\).
No primitiveness of either vector, evenness of the entire lattice or restriction on the integer coordinate signs is needed.

Zero vectors are included in the transvection definition and cause no division by a vector norm in the proof.
If \(v=0\), then \(a=c=V=X=Y=0\), and the determinant in equation (5) is \((z-1)^2\), regardless of \(b+W\).
The case \(w=0\) is symmetric at the determinant level.
Thus the asserted complete characteristic polynomial \((z^g-1)(z-1)^2\) and measure one hold in both zero cases, including when both vectors vanish.
The case \(g=1\) is allowed throughout: \(R_g=I\), \(q=z-1\), and the resolvent and subsequent polynomial identities remain valid for \(z>1\).

### Determinant normalization and the full characteristic polynomial

The composition order was checked directly on \(x+\alpha e+\beta f\).
After \(T_{f,w}\), the positive component is \(x+\alpha w\), the \(e\)-coefficient is \(\alpha\), and the \(f\)-coefficient is \(\beta'=\beta-w^{\mathsf T}x-b\alpha\).
After \(T_{e,v}\), the positive component is \(x+\alpha w+\beta'v\) and the \(e\)-coefficient is \(\alpha-v^{\mathsf T}x-c\alpha-a\beta'\).
Thus the last row of \(zI-A\), applied to these coordinates, is \(z\beta-\beta'\).

Subtracting \(R_gv\) times that last row from the positive-coordinate rows replaces their term \(-\beta'R_gv\) by \(-z\beta R_gv\).
Adding \(a\) times the last row to the \(e\)-coordinate row replaces \(a\beta'\) by \(az\beta\).
These are row additions with the last row unchanged, so their determinant multiplier is exactly one.
They produce precisely the block matrix displayed in C885, without an omitted sign or power of \(z\).

For \(z>1\), the positive block \(zI-R_g\) is invertible and has determinant \(q(z)=z^g-1\).
Its Schur complement has entries
\[
\begin{pmatrix}
z-1+c+v^{\mathsf T}K_Rw & z(a+v^{\mathsf T}K_Rv)\\
b+w^{\mathsf T}K_Rw & z-1+z w^{\mathsf T}K_Rv
\end{pmatrix},
\]
so \(P_A=qD\) is an actual determinant identity.
Equality on the interval \(z>1\) also identifies the corresponding rational functions.
Clearing the stated denominators is therefore valid as a polynomial identity, including at roots of unity after cancellation.
This checks the normalization and multiplicities of the entire characteristic polynomial; exterior-root equivalence alone would not have supplied that conclusion.
The earlier exterior reduction is consistent with the identity, and no root-count assertion from L462 is needed for the new whole-measure lower bound.

### Uniform estimate and the threshold at two

Write \(v=(zI-R_g)u\) and \(w=(zI-R_g)t\) for real \(z>1\).
Because \(R_g\) is orthogonal and commutes with its resolvent, \(K_Rv=R_gu\) and \(K_Rw=R_gt\).
Expansion then gives
\[
a+V=\frac{z^2-1}{2}\|u\|^2,\qquad
b+W=\frac{z^2-1}{2}\|t\|^2.
\]
In checking the cross terms, the two bilinear forms \(u^{\mathsf T}R_gt\) and \(t^{\mathsf T}R_gu\) must not be identified.
Expanding \(c\) and \(X\) separately cancels the former and leaves exactly \(c+X=z(zh-k)\), while \(Y=zk-h\), with the proof's \(h=u^{\mathsf T}t\) and \(k=t^{\mathsf T}R_gu\).

Cauchy--Schwarz gives \(|h|,|k|\le E=\|u\|\|t\|\), hence \(|r|\le E\) for \(r=(h+k)/2\).
For \(d=(h-k)/2\), the exact cross-product identity is
\[
(c+X)Y=z\bigl((z-1)^2r^2-(z+1)^2d^2\bigr).
\]
Subtracting the product of the two positive diagonal quadratic terms uses the coefficient identity
\[
z(z-1)^2-\frac{(z^2-1)^2}{4}
=-\frac{(z-1)^4}{4}.
\]
Also \(E\ge\|v\|\|w\|/(z+1)^2\), by the ordinary operator bound for \(zI-R_g\).
The coefficient is negative, so substituting this lower bound on \(E\) gives the second inequality of (6) in the stated direction.
This estimate uses no cyclic support, orthogonality between \(v\) and \(w\), sign pattern or growing-parameter limit.

At two, the geometric series gives \(\|K_R(2)\|\le1\), and \(\|I+K_R(2)\|\le2\).
Thus \(|Y|\le s\) and \(|c+X|\le2s\), where \(s=\|v\|\|w\|\).
Expansion of the two-by-two determinant gives the linear terms \((c+X)+2Y\) and twice the quadratic difference in (6), yielding exactly
\[
D(2)\le1+4s-\frac{s^2}{162}.
\]
The derivative of the right side is \(4-s/81\), which is negative for \(s\ge650\), and its value at 650 is \(-569/81\).
The strict negative sign therefore holds throughout the claimed range.

For each fixed \(g,v,w\), the resolvent is continuous on \(z>1\), and \(K_R(z)=O(z^{-1})\) gives \(D(z)=z^2+O(z)\).
The argument needs eventual positivity separately for each fixed input, not a uniform large-\(z\) threshold across all inputs.
Continuity supplies a real zero \(\lambda>2\); because \(q(\lambda)\ne0\), the exact determinant identity makes it a root of \(P_A\).
Monicity gives \(M(P_A)\ge\lambda>2\), since every other factor in the complete Mahler product is at least one.
No cancellation, selection of a proper polynomial factor or assumption that there is only one expanding root is involved.

### From small complete measure to bounded correlation support

In the branch \(M(P_A)\le2\) with both vectors nonzero, the strict contrapositive of the previous estimate gives \(s<650\).
The squared norms are positive even integers, each at least two.
Their product is less than \(650^2=422500\), so each squared norm is less than 211250.
Every occupied integer coordinate contributes at least one to that norm, which proves the conservative support bound \(B=211250\).
The bound is independent of \(g\), coordinate locations, coefficient heights and the relative supports.

The finite resolvent identity follows by multiplying its numerator by \(zI-R_g\): consecutive terms cancel and the two endpoints give \((z^g-1)R_g\).
Because \(R_g\) is one cycle on all \(g\) coordinates, every ordered pair of occupied coordinates in \(r,t\) aligns at exactly one lag in \(1,\ldots,g\).
Hence the set of possibly nonzero cyclic correlations has size at most \(b_rb_t\), including the lag \(j=g\).
Repeated lags and coefficient cancellations cannot increase that size.
This verifies the claimed support bound on every \(U_{r,t}\), without a restriction on the integer magnitudes or any equidistribution assumption.

Using \(P_A=qD\), multiplication by \(q\) gives \(qP_A=q^2D\), which clears both resolvent denominators and produces exactly (8).
Each factor involving \((z-1+c)q\) or \((z-1)q\) has at most \(4+B^2\) terms.
Each factor involving \(aq\) or \(bq\) has at most \(2+B^2\) terms.
The number of terms in a product is at most the product of the two term counts, and addition or subtraction has at most the sum of the two counts.
The outer factor \(z\) does not change support size.
Thus the displayed absolute integer
\[
K=(B^2+4)^2+(B^2+2)^2
\]
bounds the support of \(qP_A\), including small-degree overlaps and cancellations.

The polynomial \(qP_A\) is nonzero and integral because both factors are nonzero integer polynomials.
All roots of \(q=z^g-1\) are roots of unity and its leading coefficient is one, so \(M(q)=1\).
Multiplicativity of the complete Mahler product, including leading coefficients and repeated roots, gives \(m(qP_A)=m(P_A)\).
No division by degree or removal of a noncyclotomic factor occurs.

### Accepted source input and final quantifiers

The retained DS17 unit identifies Theorem 2 in arXiv:1606.04376v2 and its exact consequence for nonzero integer univariate polynomials with at most a fixed number of nonzero terms.
That consequence uses total logarithmic Mahler measure and permits unbounded degree and coefficient height, with no irreducibility or reciprocity hypothesis.
The polynomial \(qP_A\) satisfies every required hypothesis with the single absolute \(K\) above.
The theorem's recorded monomial qualification is immaterial to this large fixed \(K\), and the zero polynomial is explicitly excluded by the established nonzero product.
The accepted external premise is resolved at its retained statement and applicability depth; no original DS17 or Smyth foundational proof is newly certified here.

The unchanged GHS13 attribution is supported by the precise arXiv v2, Section 8.3, equation (49), printed/PDF page 54 inspection retained in L462 v13 and R1114 v1.
It identifies the transvection formula, whose needed pairing and inverse identities are proved locally.
No modular-group theorem, signature \((2,n)\) hypothesis or priority claim is imported into C885.
No source-applicability objection affecting these two actual uses was found.

If \(0<m(P_A)\le\log2\), the complete polynomial \(qP_A\) has positive logarithmic measure at least \(\eta_K\).
If \(m(P_A)>\log2\), its measure already exceeds the other branch constant.
Taking \(\eta=\min(\eta_K,\log2)>0\) therefore supplies one constant for every \(g\ge1\) and every permitted pair \(v,w\), including the separately settled zero cases.
Neither the estimates nor the fixed-support interface leave a hidden bounded-degree, disjoint-support, parity-of-\(g\) or coefficient-height condition.

This excludes a sequence of positive complete logarithmic measures tending to zero within the stated two-transvection family.
It does not address a growing number of transvections, general lattice isometries or all nonzero integer polynomials.
The accepted source input supplies no explicit \(\eta_K\) here, so this argument does not prove \(M(P_A)\ge6/5\) whenever \(M(P_A)>1\).
The unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.
This finding records the independent proof review and its exact limits; Claim adoption and Task disposition remain with their responsible materials.
