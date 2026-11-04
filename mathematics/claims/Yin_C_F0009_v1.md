---
author: Yin
---

# Bounded and affiliated inner ranks agree for bounded rectangular matrices

## Statement

Let M be a finite tracial von Neumann algebra and U its algebra of affiliated operators.
For every bounded rectangular C in M_(m,n)(M), the integer inner ranks satisfy rho_M(C)=rho_U(C).
For a bounded pivot A invertible over U and bounded compatible u,v,f=uA^(-1)v, the bounded bordered matrix has inner rank N over M and U and factors through N bounded columns.
No conclusion places these factors in the polynomial algebra or its bounded division closure.

## Source and original checking boundary

The finite-tracial affiliated-star-algebra and rectangular polar-decomposition interfaces are [MSY23 U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004), at their exact accepted foundational depth.
For the bordered consequence use the [reconstructed Proposition2.3 rank identity](../audits/literature/MSY23/Yin_U001.md#proposition-23-and-lemma-24).
Original local refinement date: 2026-09-09; the main unit reviewing agent authored it and the coordinating agent separately reconstructed the polar-decomposition argument.
These are preserved checking facts, without creating a fresh independent finding for this new path.
No Current assessment is selected for this newly organized fixed account.
Placement preserves the existing argument and actual earlier checking scopes; it supplies no new mathematical adoption, review relationship, source reading or Task/E authority.

## Retained argument

### Local Consequence for the Proposition 2.3 Follow-Up: Bounded Rank Factorizations

Date and provenance: 2026-09-09.
This local refinement was authored by the main unit reviewing agent; the coordinating agent independently reconstructed its polar-decomposition argument.
It is a consequence of the affiliated-operator foundations already retained here, rather than an additional assertion quoted from MSY23.

For every bounded rectangular matrix \(C\in M_{m,n}(M)\),

\[
\rho_M(C)=\rho_U(C).
\tag{C}
\]

These are integer-valued **inner ranks**, not the possibly noninteger tracial rank of the range projection.
To prove (C), choose a factorization \(C=AB\) over \(U\) through \(k=\rho_U(C)\) columns.
For \(k>0\), rectangular affiliated polar decomposition gives \(A=V|A|\), with a bounded partial isometry \(V\in M_{m,k}(M)\) and \(VV^*\) the projection onto the closure of the range of \(A\).
Because the affiliated product is the closure of the ordinary operator product, the closure of the range of \(C=AB\) is contained in that range projection.
Hence

\[
C=VV^*C=V(V^*C).
\]

Both factors in the last expression are bounded matrices over \(M\), so \(\rho_M(C)\le k\).
The reverse inequality follows by viewing any bounded factorization as an affiliated one.
If \(k=0\), then \(C=0\), and the equality is immediate.
This proof does not require projection comparison or a choice of central decomposition.

In particular, suppose \(A\in M_N(M)\) is invertible over \(U\), \(u,v\) are bounded compatible matrices, and the scalar compression \(f=uA^{-1}v\) is bounded.
Proposition 2.3 over the stably finite algebra \(U\), followed by (C), gives

\[
\rho_U\!\begin{pmatrix}A&v\\u&f\end{pmatrix}
=\rho_M\!\begin{pmatrix}A&v\\u&f\end{pmatrix}=N.
\]

Thus the bounded bordered matrix has a factorization through \(N\) columns with both factors in \(M\), even if the displayed pivot is not boundedly invertible.
The polar-decomposition construction gives factors in the ambient von Neumann algebra; it does not put their entries in the polynomial algebra or its bounded division closure.
Algebraic control of such factors, or construction of an appropriate boundedly invertible polynomial block, is the additional premise needed to turn this rank consequence into a bounded rational formula.
