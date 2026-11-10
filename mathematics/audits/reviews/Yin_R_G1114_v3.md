---
author: Yin
---

# Independent review of the two-transvection gap over arbitrary positive integral lattices

## Review arrangement and exact inputs

The review act is dated 2026-11-10T00:58, with Yin as the human record author.
A separately organized mathematical reviewer inspected the fixed [C885 v2 statement](../../claims/Yin_C_G0885_v2.md#statement), [complete argument](../../claims/Yin_C_G0885_v2.md#argument) and [research scope](../../claims/Yin_C_G0885_v2.md#research-scope).
The reviewer did not develop that proof, receive its development dialogue or a substantive author explanation, or contribute a repair.
The prior context consisted of the same reviewer's independent examination of C885 v1 and its fixed inputs, retained in [R1114 v2](Yin_R_G1114_v2.md#cyclic-two-transvection-gap-review).
That earlier result is reused only for the real-orthogonal determinant estimate and unchanged elementary interfaces that remain applicable.
The new lattice, cyclic Fourier, coset and polynomial-measure steps were checked directly from the fixed v2 argument.

The [San20 source unit](../literature/San20/Yin_U001.md#san20-u001), including its [Fourier normalization](../literature/San20/Yin_U001.md#finite-abelian-fourier-algebra-norm), and the [DS17 source unit](../literature/DS17/Yin_U001.md#ds17-u001) supply the two accepted external statements.
The recorded source editions, exact hypotheses, uniformity and inspection limits were read in those units.
The related [C880 v1 clearing mechanism](../../claims/Yin_C_G0880_v1.md#sparse-completion) and its [earlier source-interface finding](Yin_R_G1105_v1.md#whole-lift-review) were consulted at that existing scope.
C880's trace identities and residue hypotheses are provenance for the mechanism, not premises transferred to the new correlation construction.
The [L462 v13 generator definition](../../ledger/Yin_L_G0462_v13.md#integer-generators) and its retained GHS13 attribution remain the unchanged formula input.
The present review does not newly inspect the original source PDFs or audit the original Sanders, DS17 or Smyth foundational proofs.
No numerical search, solver, native mathematical program or formal verification was used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [C885 v2 statement](../../claims/Yin_C_G0885_v2.md#statement) | Every positive integral lattice and integral positive isometry, all permitted vector pairs, complete-measure gap, explicit large-norm implication and zero cases. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [C885 v2 complete argument](../../claims/Yin_C_G0885_v2.md#argument) | Finite order, pairing transfer, exact determinant, four normalized Fourier bounds, signed cosets, common denominator, support count and whole-measure equality. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [C885 v2 research scope](../../claims/Yin_C_G0885_v2.md#research-scope) | Uniformity in all stated lattice and matrix data, with no representation theorem, additional-transvection result or unrestricted Lehmer conclusion. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [C885 v1 real-orthogonal argument](../../claims/Yin_C_G0885_v1.md#argument) | Reuse of the determinant row operations and uniform estimate, whose derivations use real orthogonality and not cyclic-coordinate sparsity. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [Earlier independent estimate finding](Yin_R_G1114_v2.md#cyclic-two-transvection-gap-review) | Actual prior review of that unchanged estimate and its constants; no inherited coverage of the new lattice or Fourier interfaces. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [Integral generator input](../../ledger/Yin_L_G0462_v13.md#integer-generators) | The pairing identity, inverse and integrality under the precise even-norm hypotheses, with unchanged GHS13 attribution. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [Sanders accepted theorem](../literature/San20/Yin_U001.md#san20-u001) | Uniform signed-coset decomposition for integer functions with bounded Fourier algebra norm on any finite abelian group. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [Sanders Fourier convention](../literature/San20/Yin_U001.md#finite-abelian-fourier-algebra-norm) | Probability normalization on the cyclic group and counting normalization on its dual, exactly as used for the four correlations. |
| [Whole argument finding](#positive-lattice-two-transvection-gap-review) | [DS17 accepted theorem](../literature/DS17/Yin_U001.md#ds17-u001) | Positive total logarithmic gap for a nonzero integer polynomial with a fixed support bound, independently of degree, coefficient height and irreducibility. |

<a id="positive-lattice-two-transvection-gap-review"></a>
## Finding

No mathematical defect or unresolved source-applicability gap was found in the inspected C885 v2 argument.
It establishes the asserted absolute positive gap for the complete logarithmic Mahler measure over all of its stated positive integral lattices, finite-order positive isometries and even-norm integer vector pairs.
The large-norm implication and neutral zero-vector cases also hold at their full stated scope.
The following checks supply the decisive evidence, including every new interface beyond v1.

### The lattice domain, finite order and integral generators

The hypotheses require a symmetric positive definite integral matrix, without a determinant, rank or basis bound and without an evenness assumption on every lattice vector.
For a fixed such matrix, an integral isometry's column \(j\) lies in the bounded ellipsoid of \(H\)-squared norm \(H_{jj}\).
Only finitely many integer columns can lie in that ellipsoid, so only finitely many such matrices exist.
All powers of the given invertible \(R\) are among them.
Equality of two distinct powers, followed by multiplication by an inverse power, proves \(R^N=I\) for some positive integer \(N\).
There is no assertion that \(N\) or the size of the isometry group is uniformly bounded.

Every root of \(\chi_R\) is therefore a root of unity, with all its characteristic-polynomial multiplicities retained.
Since \(R\) is an integer matrix, \(\chi_R\) is monic integral and has complete Mahler measure one.
In particular it has no zero on the real interval \(z>1\).
The cases \(N=1\), repeated eigenvalues and \(g=1\) require no change to this reasoning.

The full lattice pairing is integral, while \((e,e)=(e,v)=(f,f)=(f,w)=0\).
The supplied even norms make \(a=(v,v)/2\) and \(b=(w,w)/2\) integers.
The transvection pairing calculation and negative-vector inverse from L462 use exactly these hypotheses, so they continue to prove integral invertibility in the present lattice.
No coordinate-support bound, unimodularity or Euclidean norm assumption is involved.
It follows that \(P_A\) is a nonzero monic integer polynomial of degree \(g+2\).

### Complete determinant and transfer of the real-orthogonal estimate

For \(x+\alpha e+\beta f\), the first applied transvection \(T_{f,w}\) gives positive component \(x+\alpha w\) and last coefficient
\[
\beta'=\beta-w^{\mathsf T}Hx-b\alpha.
\]
The next transvection gives positive component \(x+\alpha w+\beta'v\) and \(e\)-coefficient \(\alpha-v^{\mathsf T}Hx-c\alpha-a\beta'\).
Thus the last row of \(zI-A\) is \(z\beta-\beta'\), exactly as in the prior row-operation argument.
Subtracting \(Rv\) times this row from the positive rows and adding \(a\) times it to the \(e\)-row yields the stated block matrix, with \(v^{\mathsf T}H\) and \(w^{\mathsf T}H\) in its last two rows.
These operations have determinant multiplier one.

For \(z>1\), the positive block is invertible and its determinant is \(\chi_R\).
The Schur complement therefore gives exactly (3), including the factors of \(z\) in its second column.
This is an identity for the full determinant, hence for the corresponding rational functions, not merely a criterion for exterior eigenvalues.
If \(v=0\), its upper-right entry vanishes and its diagonal product is \((z-1)^2\); if \(w=0\), the lower-left entry vanishes with the same diagonal product.
Together with \(M(\chi_R)=1\), this proves the complete neutral polynomial and measure in every zero-vector case.

Let \(S=H^{1/2}\) be the real positive symmetric square root.
Then \(Q=SRS^{-1}\) is Euclidean orthogonal, and \((r,t)_H=(Sr)^{\mathsf T}(St)\).
The resolvent obeys
\[
(zI-Q)^{-1}Q=S(zI-R)^{-1}RS^{-1},
\]
so \(a,b,c,V,W,X,Y\) and the two-by-two determinant are all preserved under this simultaneous change of coordinates.
The transformed vectors need not be integral, because integrality was established before this step and is not a hypothesis of the reused real-orthogonal estimate.

The reviewed estimate in v1 uses only orthogonality, Cauchy--Schwarz and the resolvent bounds.
It therefore applies with \(\|Sv\|\|Sw\|=s\), yielding \(D(2)\le1+4s-s^2/162\).
The already checked value \(-569/81\) at \(s=650\) and the decreasing right side for larger \(s\) give a strict negative determinant.
For each fixed input, \(D(z)=z^2+O(z)\) and continuity on \(z>1\) give a real zero greater than two.
Its transfer to a root of the full \(P_A\) follows from (3) and the nonvanishing of \(\chi_R\) there.
Monicity then gives \(M(P_A)>2\), independently of every remaining root and multiplicity.
Neither the cyclic standard-coordinate support argument nor a small bound on the number of expanding roots is reused.

### Integer cyclic correlations and their exact normalized algebra norms

In the remaining branch \(1<M(P_A)\le2\), both vectors are nonzero and \(s<650\).
Their \(H\)-squared norms are positive even integers and therefore at least two.
Their product is less than \(422500\), so each squared norm is less than \(B=211250\).
This bounds their inner-product norms, without making any claim about the number of nonzero coordinates in the chosen basis.

For each of the four ordered pairs, \(f_{r,t}(j)=r^{\mathsf T}HR^jt\) is integral because all its displayed data are integral.
It is well defined on \(\mathbb Z/N\mathbb Z\) because \(R^N=I\).
It is not necessary that \(N\) be the minimal order or that the action be faithful after restricting to the vectors.

The complex Hermitian extension, conjugate-linear in its first entry, makes \(R\) unitary.
Its orthogonal eigenspace projections give
\[
f_{r,t}(j)=\sum_{\lambda^N=1}\lambda^j
\langle\Pi_\lambda r,\Pi_\lambda t\rangle_H.
\]
The exponent has this sign because \(R^j\) acts on the second, linear entry of the inner product.
For the character \(j\mapsto\mu^j\), the normalized Fourier coefficient is consequently
\[
\frac1N\sum_{j=0}^{N-1}f_{r,t}(j)\overline{\mu^j}
=\langle\Pi_\mu r,\Pi_\mu t\rangle_H,
\]
with zero coefficient when the eigenspace is absent.
Thus no factor of \(N\), multiplicity or inverse character is missing.
Eigenvalue multiplicities are contained in the respective projections rather than counted as distinct characters.

Taking absolute values, using Cauchy--Schwarz in each eigenspace and then in the finite sum, and using orthogonality of the projections proves
\[
\|f_{r,t}\|_A
\le\sum_\lambda\|\Pi_\lambda r\|_H\|\Pi_\lambda t\|_H
\le\|r\|_H\|t\|_H.
\]
This is precisely the probability/counting convention recorded in San20-U001.
For the two diagonal correlations the bound is the corresponding squared norm, and for either cross correlation it is \(s\).
All four norms are therefore bounded by the same absolute \(B\), regardless of \(N\), basis or lattice determinant.

### Signed-coset generating functions and the common integer denominator

Sanders Theorem 1.1 applies to these integer-valued functions on the finite abelian cyclic group with the fixed norm bound \(B\ge1\).
Its bound on the sum of absolute integer coset coefficients gives a single finite integer \(L=L(B)\ge1\) after taking an upper integer bound and splitting coefficients into signed repetitions.
Only this uniform finiteness is used; the asymptotic exponent in the source estimate is not evaluated.
The decomposition of a zero correlation can be empty.

Every subgroup of \(\mathbb Z/N\mathbb Z\) is the set of multiples of a divisor \(d\mid N\), so its cosets are exactly the congruences \(j\equiv u\pmod d\).
This includes \(d=1\), the full group, and \(d=N\), the trivial subgroup and its singleton cosets.
For \(|z|>1\), the geometric resolvent converges in the \(H\)-operator norm and gives
\[
K_R(z)=\sum_{j\ge1}z^{-j}R^j.
\]
Pairing with \(r,t\) therefore supplies the actual correlation resolvent in the proof.

For \(u>0\), the positive indices in a coset begin at \(j=u\), and their generating function is
\[
z^{-u}(1-z^{-d})^{-1}=\frac{z^{d-u}}{z^d-1}.
\]
For \(u=0\), they begin at \(j=d\), so the numerator is one rather than \(z^d\).
This is exactly the stated choice \(\nu=d\), and it removes any possible \(j=0\) contribution.
Every numerator exponent \(d-\nu\) is a nonnegative integer less than \(d\).
All four correlation resolvents are therefore sums of at most \(L\) signed monomial-over-binomial terms, with the required equality as rational functions.

The product \(\Delta\) includes one denominator for each occurrence in all four sums, so its factor count is \(F\le4L\).
It is a nonzero monic integer polynomial of measure one with at most \(2^F\) terms.
For every summand, its denominator is an actual factor occurrence in this product, even if other occurrences have the same modulus.
Multiplication by \(\Delta\) leaves an integer polynomial consisting of its numerator monomial times the remaining factors.
For \(F\ge1\), each such polynomial has at most \(2^{F-1}\) terms, so the proof's weaker bound \(L2^F\) is valid.
When \(F=0\), all four sums are empty and the four cleared correlations are zero, which also satisfies the stated bound.
Neither coefficient cancellation nor repeated denominator factors increases any term count.

### Cross-multiplied whole-polynomial identity and the final gap

Every entry in the displayed definition of \(U\) is an integer polynomial: \(a,b,c\) are integers and the four cleared correlations were just established to be polynomials with nonnegative exponents.
On \(|z|>1\), direct expansion gives \(U=\Delta^2D\).
Combining with the complete determinant identity yields
\[
\chi_R U=\Delta^2P_A.
\]
Both sides are polynomials, so this equality holds identically, including at zeros of the clearing factors.
The right side is nonzero, hence \(U\ne0\).

The first two factors in the definition of \(U\) have at most \((L+2)2^F\) terms each, and the other two have at most \((L+1)2^F\) terms each.
Multiplication by the outer \(z\) does not change the support size.
Consequently its term count is at most
\[
\bigl((L+2)^2+(L+1)^2\bigr)2^{2F}
\le2(L+2)^2 2^{8L}=K.
\]
This accounts for all products, sums, degree collisions and cancellations; the coefficients' sizes do not affect the bound.
The value \(K\) is a fixed positive integer depending only on the fixed \(B\).

The multiplicative Mahler measure of each nonzero polynomial includes its leading coefficient and every root with multiplicity.
Applying multiplicativity directly to the polynomial identity gives
\[
M(\chi_R)M(U)=M(\Delta)^2M(P_A).
\]
Both cyclotomic measures are one, so \(m(U)=m(P_A)\) exactly.
This argument requires neither a polynomial quotient \(U/P_A\) nor an integer divisibility assertion, and it remains valid with shared cyclotomic factors and arbitrary multiplicities.

The DS17 accepted univariate theorem applies to this actual nonzero integer polynomial \(U\) with at most the fixed \(K\) terms.
It imposes no irreducibility, degree, coefficient-height or reciprocal-polynomial condition.
It gives a positive \(\eta_K\) whenever \(m(U)>0\), using total logarithmic measure with no degree normalization.
Thus the low-measure branch has \(m(P_A)\ge\eta_K\), while the other positive branch has \(m(P_A)>\log2\).
The single choice \(\eta=\min(\eta_K,\log2)>0\) proves the assertion for every \(g,H,R,v,w\) in the statement.
Measure-one inputs and the explicitly checked zero-vector cases satisfy the zero alternative.

The source uses retain their exact accepted inspection depth: San20's arXiv v5 Section 1 and Theorem 1.1 supply the normalized uniform coset statement, and DS17's arXiv v2 Theorem 2 supplies the fixed-support gap.
No relevant unresolved applicability objection was found, and no original foundational proof is newly certified by this review.
The unchanged GHS13 attribution identifies a locally verified transvection formula and imports no modular-group result into the positive-lattice argument.

The strengthened theorem excludes positive complete logarithmic measures tending to zero throughout the displayed two-transvection family, even as the positive lattice, basis, rank, determinant, isometry order and integer coordinates vary.
It does not prove that all integral indefinite isometries admit that representation, with or without stabilization, and does not cover a growing number of transvections.
No effective bound \(M(P_A)\ge6/5\) for every nonneutral input is obtained here.
The unrestricted [G0001 contract](../../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.
This record supplies the independent finding for C885 v2 while preserving the fixed v1 statement and its earlier review at their actual scopes.
