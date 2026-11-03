---
author: Yin
---

# MS24: Integer Capacity and the Haar Model

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: Retained arXiv:2406.15922v1, 19 pages; margin date 2024-06-22 and distinct title-page date 2024-06-25.

Source passages: [MS24 PDF](../../../literature/pdf/MS24.pdf), Theorems 1.3/4.1 and Corollary 1.4, printed/PDF pp. 4, 15-16.

Inspection: Date/reviewer: 2026-09-12, assigned MS24 reviewer.

The registered artifact and acquisition record retain both dates.

## MS24-U004

Source: [MS24 PDF](../../../literature/pdf/MS24.pdf), Theorems 1.3/4.1 and Corollary 1.4, printed/PDF pp. 4, 15-16.
Date/reviewer: 2026-09-12, assigned MS24 reviewer.
The complete local inequality chain was reconstructed.
The subsequent user-requested integer dependency review checks the Haar injectivity interface and reconstructs the exact injective free-group determinant input from finite quotients.
The general Sch01 theorem retains its separately recorded original-proof limits.

### Statements

Let a_1,...,a_n be matrices in M_m(Z), and eta(b)=sum_i a_i b a_i*.
If eta is rank non-decreasing, then

\[
\operatorname{cap}(\eta)\ge1.
\]

If eta is rank-decreasing, its capacity is zero by Gur04's rank/capacity theorem.
Thus capacity for these integral Kraus families lies in {0} union [1,infinity).
Integrality means integral **Kraus coefficient matrices** as specified here; it is not merely integrality of an arbitrary coordinate matrix representing eta.

For the associated S=sum_i a_i tensor s_i, affiliated invertibility implies

\[
\Delta_{\operatorname{tr}_m\otimes\tau}(S)\ge e^{-1/2}.
\]

This is Corollary 1.4, obtained by substituting the capacity bound into [U003](Yin_U003.md#ms24-u003).
The constant is independent of both the matrix size m and the number n of semicircular variables.

### Complete Local Proof

Let u_1,...,u_n be the standard free Haar generators in L(F_n), and put T=sum_i a_i tensor u_i.
Rank non-decreasing means that A=sum_i a_i x_i is full over the free field.
The checked MSY23 Corollary 6.4 free-Haar realization then makes T injective, with an affiliated inverse.
This hypothesis is essential when passing from the kernel-omitting group determinant to the ordinary determinant.

Since T is an integral free-group matrix, the accepted [Sch01-U001](../Sch01/Yin_U001.md#sch01-u001) input gives Delta(T)>=1.
Precisely, that source uses the unnormalized trace Tr_m tensor tau for the positive group-ring matrix T* T and proves

\[
0\le\int_{(0,\infty)}\log t\,
 d[(\operatorname{Tr}_m\otimes\tau)(1_{[0,t]}(T^*T))]
=2m\log\Delta_{\operatorname{tr}_m\otimes\tau}(T).
\]

The integral omits the kernel; the equality uses injectivity of T already established above.
The factor 2m accounts for both the square and matrix trace normalization.

The [finite-quotient reconstruction](../Sch01/Yin_U001.md#finite-quotient-determinant-proof) now verifies this exact needed lower bound directly.
Finite approximating matrices may be singular: their nonzero-eigenvalue products are positive integers, their normalized kernel masses tend to zero because the limiting matrix is injective, and the limit is taken at a fixed logarithmic cutoff before removing that cutoff.
This proves the lower bound without assuming convergence of the determinants.

For the injectivity step, the same supplement checks the source Corollary 6.4 and identifies a smaller sufficient chain: the explicit bounded Haar duals imply absence of finite-rank cycles, and MSY23's full-linear-kernel argument gives injectivity.
This route does not rely on a determinant lower bound, so the reasoning is not circular.

Fix b>0 with det b=1.
Rank non-decreasing implies eta(b)>0.
Set

\[
c_i=\eta(b)^{-1/2}a_i b^{1/2},
\qquad
\widetilde T=\sum_i c_i\otimes u_i
 =(\eta(b)^{-1/2}\otimes1)T(b^{1/2}\otimes1).
\]

By multiplicativity and Delta(b^(1/2))=1,

\[
\Delta(\widetilde T)
=\Delta(\eta(b))^{-1/2}\Delta(T)
\ge\Delta(\eta(b))^{-1/2}.
\]

On the other hand sum_i c_i c_i*=I, and freeness of the Haar generators gives tau(u_i u_j*)=delta_(ij).
The determinant/arithmetic-mean inequality therefore gives

\[
\Delta(\widetilde T)^2
=\Delta(\widetilde T\widetilde T^*)
\le(\operatorname{tr}_m\otimes\tau)(\widetilde T\widetilde T^*)
=\operatorname{tr}_m\left(\sum_i c_i c_i^*\right)=1.
\]

Consequently Delta(eta(b))>=1, or equivalently det eta(b)>=1.
Taking the infimum over b proves the capacity estimate.
This argument never takes the Fuglede-Kadison determinant of an unbounded inverse: all inverse factors appearing in the determinant manipulations are finite-dimensional positive matrices.

The phrase “bigger than 1” on source p. 16 must mean “at least 1”; the factor Delta(b^(1/2)) equals 1.
No strict lower bound is needed or true in general.

### Comparison and Limits

MS24 compares this estimate with the bound m^(-2m) in the expanded GGOW paper, Theorem 2.18.
The original nine-page FOCS conference file does not contain that numbered theorem.
The GGOW20 version record and [its audit](../GGOW20/readme.md) must be consulted for the selected full version and locators; numbering is not transferred between the conference and full texts.

The stronger constant uses the determinant property of the integral **free-group** model.
It does not follow merely from a second-moment normalization or a generic CP-map inequality.
After the Haar proof establishes capacity>=1, the specifically semicircular determinant formula transfers the estimate to S.
The proof neither extends that formula to arbitrary q-Gaussian/transported tuples nor proves a bounded inverse for any such tuple.

## Complete retained algebra and Haar interfaces

The following original 2026-09-12 interface reconstruction was retained from L_F0077 at 2026-10-21T01:19.
The finite-quotient determinant proof now has its sufficient source home in [Sch01-U001 v2](../Sch01/Yin_U001.md#finite-quotient-determinant-proof).
The original R_F0125 check includes the terminal dual sign, finite-rank cycle argument and capacity normalization, while explicitly retaining the prior MSY23 kernel/Cohn foundations rather than claiming their fresh full reconstruction.
This maintenance performs no new source or proof review.

## Rank Non-Decrease to a Full Homogeneous Pencil

For \(V\subseteq\mathbb C^m\), let \(p_V\) be the orthogonal projection and put
\[
W=\sum_i a_iV.
\]
Positivity gives
\[
\operatorname{Ran}\eta(p_V)=W.
\]
More generally, if \(b\geq0\) has range \(V\), its restriction to \(V\) is invertible, so the same range identity holds with \(b\) in place of \(p_V\).
Thus rank non-decrease is exactly
\[
\dim\Big(\sum_i a_iV\Big)\geq\dim V
\quad\hbox{for every }V\subseteq\mathbb C^m.
\tag{1}
\]

A shrunk subspace, with \(\dim V=\ell\) and \(\dim W=r<\ell\), supplies scalar invertible changes of domain and range bases for which every \(a_i\) has a common zero block of size \((m-r)\)-by-\(\ell\).
Its row and column sizes sum to more than \(m\).
Such a hollow pencil factors through fewer than \(m\) coordinates, so it is not full.

Conversely, the linear hollow criterion puts every nonfull square linear pencil into a scalar-equivalent hollow form.
The corresponding column subspace maps under every coefficient matrix into the complementary row subspace, whose dimension is strictly smaller.
It violates (1).
Homogeneity ensures that the coefficients in this comparison are exactly the Kraus matrices \(a_i\); an omitted constant term would invalidate the comparison.

The precise algebraic input is MSY23 Theorem 2.10 and Proposition 2.11, printed pp. 10-11, with the citation repair proved and independently reviewed in [MSY23-U001](../MSY23/Yin_U001.md#msy23-u001).
The retained Cohn input is the matched-degree bound in the proof of Coh06 Lemma 5.8.7, printed pp. 316-317: a rank factorization of a degree-one matrix can be internally reduced so that each matched column/row degree sum is at most one.
Partitioning those factors into constant columns and constant rows yields the hollow form.
The book's cited Theorem 5.8.8 has different hypotheses and is not used.

This audit rechecked the block/range interface and the existing independent review.
It accepts that primary-source-checked degree-reduction theorem and the full-submatrix property of free-algebra matrices; the complete weak-algorithm foundations of the free algebra are not reproved here.
No invariant-theory characterization or operator-scaling algorithm is needed.

## Haar Evaluation: Actual Source Scope and a Smaller Sufficient Proof

MSY23 Corollary 6.4, printed/PDF p. 48 of [MSY23.pdf](../../../literature/pdf/MSY23.pdf), states that the division and rational closures of the canonical free group generators \(u_1,\ldots,u_n\) (without adjoining their inverses as additional formal variables) in the operators affiliated to \(L(F_n)\) are the free field.
Together with Theorem 5.6, pp. 30-34, this makes every full polynomial matrix invertible in the matrix algebra over \(U(L(F_n))\), hence injective in its bounded realization.

The actual ambient algebra in the corollary is \(U(L(F_n))\); it is not \(L(F_n)\).
There is no hypothesis \(n\geq2\), no factoriality hypothesis, and no requirement that the positive-generator polynomial algebra be strongly dense in \(L(F_n)\).
In fact that holomorphic density assertion would already be false for one Haar unitary.
The corollary does not treat the formal symbols \(x_i^*\) as additional independent generators.

For the homogeneous linear pencil required by MS24, the following shorter route proves injectivity without invoking the full rational-closure theorem.

1. Define \(V_j\in B(\ell^2(F_n))\) on reduced group words by deleting a terminal positive \(g_j\), and sending all other words, including the identity, to zero.
   This map sends distinct eligible basis vectors to distinct basis vectors, so its norm is one.
   Direct cancellation gives
   \[
   [u_i,V_j]=-\delta_{ij}P_e.
   \]
   At the identity, the left side is \(-\delta_{ij}e\).
   For any nonidentity reduced word the two operations agree; the whole-word left cancellation case is the one-letter word \(g_i^{-1}\), and both terms are then zero.
   Hence \(D_j=-V_j\) satisfies the source convention \([u_i,D_j]=\delta_{ij}P_e\).
   This corrects the sign in the prose of MSY23 Proposition 6.3; the published vacuum calculation itself has the minus sign.

2. Suppose finite-rank \(R_1,\ldots,R_n\in B(\ell^2(F_n))\) satisfy \(\sum_i[R_i,u_i]=0\).
   For \(Q_1,Q_2\in L(F_n)'\), ordinary trace cyclicity gives
   \[
   0=\operatorname{Tr}\!\left(\sum_i[R_i,u_i]Q_1D_jQ_2\right)
    =\operatorname{Tr}(R_jQ_1P_eQ_2).
   \]
   Every trace has a finite-rank factor and bounded remaining factors.
   The vectors \(Q_1e\) and \(Q_2^*e\) range independently through dense subspaces because right translations belong to the commutant.
   Therefore \(R_j=0\) for every \(j\).

3. The implication in MSY23 Theorem 3.1 from absence of nonzero finite-rank cycles to injectivity of full linear evaluations is reconstructed in [MSY23-U002](../MSY23/Yin_U002.md#msy23-u002), with independent review.
   Its mechanism is finite rank: kernel vectors for a linear matrix and its adjoint produce a cycle; independent component families force the coefficient matrix to vanish.
   An induction using full square submatrices rules out dependent components for a full pencil.
   Finite trace equates the traces of the two kernel projections and supplies the adjoint kernel.
   This argument applies to the unitary, generally nonselfadjoint tuple \(u\).

Thus \(A\) full implies \(\ker A(u)=0\).
This proof uses neither a group determinant theorem, nor free entropy/Fisher information, nor the original Linnell theorem.
The general von Neumann dimension theory used to name maximal \(\Delta\) can also be omitted: the actual premise of the linear-kernel argument is exactly the vanishing of finite-rank cycles proved in step 2.

For completeness, finite trace and polar decomposition imply that an injective \(T\in M_m(L(F_n))\) has dense range, since its initial and final support projections have equal trace.
Its spectral inverse is then a closed densely defined affiliated inverse.
This is the affiliated interpretation of injectivity, not a bounded inverse estimate.

The case \(n=1\) is especially transparent.
Rank non-decrease is equivalent to \(a_1\) being an invertible complex matrix; then \(T=a_1\otimes u_1\) is even boundedly invertible, and \(\Delta_\varphi(T)=|\det a_1|^{1/m}\geq1\).
The common proof above also works with \(F_1=\mathbb Z\).
The scalar matrix size \(m=1\) causes no exceptional case.
