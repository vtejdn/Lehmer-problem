---
author: Yin
---

# GGOW20: Polynomial Linearization and Rank Computation

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Source: the full published [GGOW20 PDF](../../../literature/pdf/GGOW20.pdf), *Operator scaling: theory and applications*, Foundations of Computational Mathematics 20 (2020), 223-290; version identity.

Passages: This unit concerns Appendix A, printed pp. 281-287 / one-based PDF pp. 59-65, and the affine convention in Remark 1.19, printed p. 233 / PDF p. 11.

Inspection: Date/reviewer: 2026-09-12, assigned MS24 reviewer, as an independent Appendix A assignment.


## GGOW20-U005

Source: the full published [GGOW20 PDF](../../../literature/pdf/GGOW20.pdf), *Operator scaling: theory and applications*, Foundations of Computational Mathematics 20 (2020), 223-290; version identity.
This unit concerns Appendix A, printed pp. 281-287 / one-based PDF pp. 59-65, and the affine convention in Remark 1.19, printed p. 233 / PDF p. 11.
It is not an audit of these statements in the former nine-page FOCS file.

Date/reviewer: 2026-09-12, assigned MS24 reviewer, as an independent Appendix A assignment.
All seven appendix pages were read and visually inspected.
The local linearization, generic compression, rank-oracle and CP-map arguments were reconstructed.
The proof uses the main paper's exact fullness/rank equivalences and its certified polynomial-time fullness algorithm as declared inputs; those main proofs are reviewed in the other units.
No implementation of the rank algorithm or formal proof assistant check was performed.

## Definitions and Exact Scope

For a polynomial matrix A over the free associative algebra F<x>, nc-rank is its rank over the universal free field F(<x>), equivalently its polynomial inner rank in this setting.
A square matrix is **full** when this rank equals its size.
Division-ring matrix rank and polynomial inner rank must not be interchanged for an arbitrary ring lacking this free-field property.

In Definition A.1, a division-free noncommutative formula has rational constants or variables at its leaves and addition/multiplication gates.
Its bit complexity b is the maximum bit complexity of a **rational leaf**, not of every coefficient after expanding the computed polynomial.
Formula size counts the description including repeated subexpressions; a compact circuit is not substituted without controlling its expansion.

Theorem A.4 states that an m by n polynomial matrix over Q, each entry given by a division-free formula of size at most s and rational leaf bit complexity at most b, has its exact nc-rank computable deterministically in time polynomial in m,n,s,b.
This is a rank-value algorithm.
It does not by itself output a rational inverse, a full-rank minor, a shrunk-subspace witness, or a bounded operator inverse.

## Effective Higman Linearization

Proposition A.2, pp. 282-284 / PDF pp. 60-62, counts k multiplication gates across the entry formulas.
It constructs invertible polynomial matrices P and Q such that

\[
N=P(A\oplus I_k)Q
\]

has affine linear entries and size (m+k) by (n+k).
The exact rank relation is

\[
\operatorname{nc\text{-}rank}N=k+\operatorname{nc\text{-}rank}A.
\]

Thus both row and column rank deficits are preserved, rather than the numeric rank itself.
The analogous ordinary commutative rank statement follows by commuting specialization of the same polynomial elementary matrices.

The elementary step isolates an uppermost multiplication gate in a selected entry a+bc.
After adjoining a unit row and column, left multiplication by an elementary matrix with b in the new column and right multiplication by one with -c in the new row replaces the affected two by two corner:

\[
\begin{pmatrix}1&b\\0&1\end{pmatrix}
\begin{pmatrix}a+bc&0\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-c&1\end{pmatrix}
=
\begin{pmatrix}a&b\\-c&1\end{pmatrix}.
\]

The order bc and the negative sign matter.
Existing unrelated entries are unchanged because the adjoined row and column initially vanish outside their final unit entry.
Exactly one multiplication gate is removed; the remaining a,b,c are retained as separate subformulas.
Iterating gives the stated k identity blocks.
Each elementary matrix has a polynomial inverse obtained by changing the sign of its off-diagonal entry.
Store P,Q as products of these elementary matrices with their subformula descriptions; expansion into all monomials is not needed for the polynomial-time construction.

### Correction to the Printed Bit Bound

Proposition A.2 claims that the **coefficients** of the final linear matrix still have bit complexity at most b.
Its proof on p. 284 only preserves rational **leaf** complexity.
These are different: already the multiplication-free one-entry formula 1+1 has leaf input 1 but coefficient 2.
More generally, addition of distinct rational leaves can increase both numerator and denominator sizes.

The valid bound is polynomial in the total formula size and b.
After all multiplication gates are removed, the surviving affine entries are signed sums of rational leaves, variables and unit constants.
For a sum of at most L rationals with numerator/denominator bit lengths at most b, using the product of their denominators bounds the resulting bit length by O(Lb+log L).
A variable coefficient is an integer sum of at most L signs.
Here L is bounded polynomially by the formula input length and the number of elementary steps.
Collecting affine coefficients therefore takes polynomial time with polynomial output bits.
This suffices for Theorem A.4, but the source's literal unchanged-coefficient-bit claim is not retained.

## Generic Compression to Fullness

Lemma A.3, p. 284 / PDF p. 62, takes 1<=r<=min(m,n), an r by m generic matrix U, and an n by r generic matrix V.
All their entries are fresh noncommuting variables, also free from the original alphabet.
Then

\[
\operatorname{nc\text{-}rank}M\ge r
\quad\Longleftrightarrow\quad UMV\text{ is full}.
\]

If M has rank at least r over the free field, division-ring elimination supplies an invertible r by r submatrix Q of M.
Specialize U,V to row and column selector matrices, giving Q.
Any polynomial inner-rank factorization of UMV specializes to a factorization of Q of the same intermediate size; hence specialization cannot increase its inner rank and UMV must be full.
This explains the source's specialization step without pretending that every rational expression remains defined under that specialization.

Conversely, a polynomial inner-rank factorization M=BC through a space of dimension d<r gives UMV=(UB)(CV), so UMV is not full.
This reverse direction is immediate but not written out in the source proof.
These arguments retain the free-algebra inner-rank/free-field-rank equivalence as the external algebraic interface.

The construction uses fresh generic variables, not a guessed numeric specialization.
The proof's unknown full minor is an existence device; the algorithm need not find its indices.

## Algorithm 5 and Theorem A.4

For each r=1,...,min(m,n), form M_r=U_r M V_r, apply the preceding linearization, and test the resulting square affine matrix N_r for fullness with the paper's certified Algorithm G'.
Return the largest successful r, or **0 if no test succeeds**.
The printed step 5 omits the latter convention, which is necessary for the zero matrix; equivalently include r=0 as a trivially successful threshold.

The selector lemma and the added identity blocks give N_r full iff nc-rank(M)>=r.
Hence the algorithm returns exactly the desired rank.
The formulas for M_r have polynomial size; total multiplication count, linearized size, variable count and the corrected coefficient bit size are all polynomial.
At most min(m,n) oracle calls are made.
Clear rational denominators by a nonzero scalar when applying an integral-coefficient fullness routine; the common denominator has polynomial bit length and does not change rank.

The linearized matrices may have a constant term.
Remark 1.19 of the main paper permits the usual affine-to-homogeneous conversion by adjoining a new variable x_0 to the constant coefficient.
At the free-field level, multiplying

\[
A_0x_0+\sum_i A_i x_i
\]

on the right by x_0^(-1) gives A_0+sum_i A_i x_i x_0^(-1).
The reversible free rational change x_i -> x_i x_0^(-1), with inverse x_i -> x_i x_0 and x_0 fixed, preserves rank in the enlarged free field.
This makes explicit the source's affine convention when connecting Appendix A to the homogeneous coefficient-map algorithm.
No evaluation of x_0^(-1) at zero is used.

The complexity assertion depends on the main algorithm's bit-precision and iteration guarantees, not just on exact-arithmetic convergence of operator scaling.
This unit checks the polynomial overhead of the reduction and does not supply a separate precision proof for that oracle.

## Quantum Rank-Deficit Reduction

Lemma A.5, pp. 286-287 / PDF pp. 64-65, starts with a CP map T:M_n(C)->M_n(C) and an integer 1<=c<=n.
The phrase c-rank-decreasing means that there exists X>=0 with rank T(X)<=rank X-c.
On block matrices of total size n+c-1, define

\[
\overline T
\begin{pmatrix}X_{11}&X_{12}\\X_{21}&X_{22}\end{pmatrix}
=
\begin{pmatrix}
T(X_{11})+\operatorname{Tr}(X_{22})I_n&0\\
0&\operatorname{Tr}(X_{11})I_{c-1}
\end{pmatrix}.
\]

The traces are ordinary unnormalized matrix traces on the indicated blocks.
Then overline T is CP, and T is c-rank-decreasing iff overline T is rank-decreasing.

For complete positivity, the source checks the Choi matrix.
An explicit equivalent construction also makes the input arithmetic transparent: if A_i are Kraus matrices for T, use diag(A_i,0), together with all matrix units E_(a,n+b) and E_(n+b,a), 1<=a<=n and 1<=b<=c-1, as Kraus matrices of overline T.
Their sums give precisely the displayed map.
Rational/integral input Kraus matrices therefore produce rational/integral output Kraus matrices of polynomial total size; no eigenvector computation is required.
This clarifies Remark A.7, whose suggested Choi spectral decomposition by itself does not guarantee rational coefficients.

For the rank equivalence, let X>=0 be a witness for rank decrease of overline T.
If both diagonal blocks are nonzero, their positive traces make the output full rank, a contradiction.
If X_11=0, positivity forces the off-diagonal blocks to vanish; for nonzero X_22, the input rank is at most c-1 whereas the output has rank n, also impossible.
Thus X_22=0, X_11 is nonzero, and again the off-diagonal blocks vanish.
The output rank is rank T(X_11)+c-1, so rank decrease is equivalent to rank T(X_11)<=rank X_11-c.
Conversely, any such X_11 gives a witness diag(X_11,0).
This proves both directions including the boundary c=1, when the new map is simply T.

For a square homogeneous pencil L=sum_i A_i x_i, the main paper's rank/shrunk-subspace equivalence identifies

\[
n-\operatorname{nc\text{-}rank}L
=\max_{X\ge0}\bigl(\operatorname{rank}X-\operatorname{rank}T(X)\bigr).
\]

Testing c=1,...,n via overline T therefore recovers that deficit and the rank.
If no positive c passes, the deficit is zero.
The case r=n in the equivalent threshold question nc-rank(L)<=r is automatic and does not call Lemma A.5 with the invalid parameter c=0.
The matching comparison in Remark A.6 is an explanatory analogy; the proof is the CP-map rank argument above.

## Coverage and Reuse Decision

The local arguments of Proposition A.2, Lemmas A.3/A.5, Algorithm 5 and Theorem A.4 are checked with the coefficient-bit correction, explicit zero-output convention, affine conversion and exact rational Kraus construction.
Retained external inputs are the free-field/inner-rank framework, division-ring matrix elimination, the source's rank-deficit equivalence and its certified fullness algorithm.
The original Higman [43] and Choi [12] proofs were not re-audited; GGOW's displayed elementary constructions were checked directly.
No earliest-attribution claim is made.

These reductions are useful when a project has a finite polynomial/formula presentation and needs an algebraic rank test.
They supply no analytic singular-value bound or operator boundedness conclusion.
Their symbolic rank value must be related to an operator evaluation by a separately checked realization theorem, such as the repository's MSY23 interface.
