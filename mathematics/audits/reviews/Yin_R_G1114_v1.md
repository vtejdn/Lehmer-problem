---
author: Yin
---

# Independent review of integral orthogonal inputs and the fixed-radius obstruction

## Review arrangement and exact inputs

The review act is dated 2026-11-09T20:20, with Yin as the human record author.
A separately organized mathematical reviewer inspected the fixed [L462 v13](../../ledger/Yin_L_G0462_v13.md#scope), without participating in its proof development.
No D20 development draft, author conversation, proof-generation summary or earlier review finding about this argument was supplied or consulted.
The reviewer first reconstructed the mathematical obligations from the fixed text, then checked its directly used project and source interfaces.
The proof's own attribution of a suggested evaluation point is part of the inspected proof, not additional development context.
No substantive repair was contributed.

The scope is the whole new argument in L462 v13: finite prefix padding, the expanding-root count with algebraic multiplicities, integral transvections, the exterior eigenvalue reduction, the displayed growing-support family, its fixed-radius obstruction and its stated applicability limits.
The contextual project results were checked at their exact statement and interface scopes; their full proofs and earlier R findings were not independently reviewed again.
The record below supplies an actual independent mathematical finding for this fixed input, without selecting a Claim assessment or completing the unrestricted Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole argument finding](#orthogonal-whole-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole argument finding](#orthogonal-whole-review) | [Question and judgment](../../ledger/Yin_L_G0462_v13.md#scope) | New argument and its stated partial-research scope; contextual results retain their own hypotheses and prior evidence. |
| [Whole argument finding](#orthogonal-whole-review) | [Prefix padding](../../ledger/Yin_L_G0462_v13.md#prefix-padding-control) | Every finite integral target prefix can be attained by a reciprocal cyclotomic multiplier without changing the complete measure. |
| [Whole argument finding](#orthogonal-whole-review) | [Expanding eigenvalues](../../ledger/Yin_L_G0462_v13.md#negative-index-bound) | Real generalized expanding space, all algebraic multiplicities, isotropic dimension bound, reciprocal spectrum and complete Mahler upper bound. |
| [Whole argument finding](#orthogonal-whole-review) | [Integral generators](../../ledger/Yin_L_G0462_v13.md#integer-generators) | Lattice hypotheses, pairing preservation, inverse, composition and exact source attribution for the transvection formula. |
| [Whole argument finding](#orthogonal-whole-review) | [First family and exterior equation](../../ledger/Yin_L_G0462_v13.md#first-family) | Admissible signed vectors and norms, exact two-dimensional elimination, and both directions of exterior eigenvalue equivalence. |
| [Whole argument finding](#orthogonal-whole-review) | [Fixed-radius obstruction](../../ledger/Yin_L_G0462_v13.md#first-family-obstruction) | Cayley bound, both cyclic overlap estimates, determinant sign, real exterior root and complete measure greater than two for every stated parameter. |
| [Whole argument finding](#orthogonal-whole-review) | [Applicability and remaining bridge](../../ledger/Yin_L_G0462_v13.md#coverage-and-first-test) | Coxeter and sparse-completion boundaries, norm-two reflection identity, and the unresolved nonneutral small-radius supply problem. |

<a id="orthogonal-whole-review"></a>
## Finding

No mathematical defect was found in the inspected new argument.
For the precise family and scaling stated in L462 v13, the proof establishes
\[
 M\!\left(\det(zI-A_{r,\,2^{3r}+1})\right)
 =\rho(A_{r,\,2^{3r}+1})>2
 \qquad(r\ge4).
\]
This rules out that family as a source of positive complete measures tending to one.
The automatic root-count bound and the integral generators do not establish a replacement family with small spectral radius.
The following checks are the decisive evidence for this finding.

### Prefix padding and its exact limitation

At induction index \(j\), the current polynomial has constant coefficient one.
Multiplication by a factor with constant term one, zero coefficients in degrees \(1,\ldots,j-1\), and coefficient \(d\) in degree \(j\) changes precisely the currently targeted coefficient by \(d\).
For \(d>0\), the proposed power of \(1+z^j+z^{2j}\) has that coefficient.
For \(d<0\), the exponent \(-d\) on \(1-z^j+z^{2j}\) is a nonnegative integer and has coefficient \(d\).
Thus no inverse polynomial or formal negative exponent is required.

The two base factors are respectively \(\Phi_3(z^j)\) and \(\Phi_6(z^j)\).
Every root is a root of unity, each factor is monic reciprocal of even degree with constant one, and arbitrary nonnegative integer powers preserve those properties.
The induction is finite for every prescribed \(L\), and multiplication preserves the complete multiplicative Mahler measure, including multiplicities.

The [C881 v3 statement](../../claims/Yin_C_G0881_v3.md#statement), its [original domain](../../claims/Yin_C_G0881_v3.md#original-domain), and its [complete measure estimate](../../claims/Yin_C_G0881_v3.md#whole-measure-upper) were checked at the invoked interface.
Its upper bound tends to one as \(L\) tends to infinity and requires the strict residue signs, endpoint and permitted degree range.
A fixed positive \(m(F)\) therefore contradicts simultaneous satisfaction of all those hypotheses at arbitrarily large matching lengths.
Padding alone establishes none of those strict conditions.

### Expanding multiplicities and complete measure

The isometry identity with nondegenerate \(H\) makes \(A\) invertible.
On every generalized eigenspace with \(|\lambda|>1\), inverse powers tend to zero despite their possible polynomial Jordan factors.
The real invariant space obtained from all such blocks has dimension equal to the sum of their complex algebraic multiplicities, since each nonreal conjugate pair contributes its full real dimension.

Preservation of \(H\) under inverse powers makes its restriction to that real space zero.
For signature \((a,q)\) with \(a\ge q\), projection of a totally isotropic subspace to the negative coordinate space is injective, so its dimension is at most \(q\).
This justifies the expanding-root count without assuming diagonalizability or discarding conjugate roots.

The identity \(A^{-1}=H^{-1}A^{\mathsf T}H\) gives reciprocal eigenvalue multisets.
In every positive-dimensional application here, \(\rho(A)\ge1\).
The monic integral characteristic polynomial has its complete logarithmic measure equal to the sum of all positive logarithmic radii, hence at most \(q\log\rho(A)\).
The definite case \(q=0\) has no expanding roots and measure one.
For \(q=1\), nonneutrality leaves exactly one expanding eigenvalue, which must be real and algebraically simple because a nonreal pair or a repeated exterior root would exceed the count.
Consequently the complete measure is exactly the spectral radius.

This checks spectral reciprocity as used in the proof.
It does not assert that every characteristic polynomial of an odd-dimensional or determinant-minus-one isometry has the same monic palindromic normalization as the separate prefix-padding input.

The [cyclic-shift control in L462 v5](../../ledger/Yin_L_G0462_v5.md#separable-control) was also rechecked directly from its displayed polynomial \(z^{2g}-(2+de)z^g+1\).
When \(|2+de|>2\), its quadratic root of larger modulus gives \(g\) expanding roots of equal radius, so the complete logarithmic cost stays fixed while the house is diluted.
The comparison correctly identifies the root-count distinction.

### Integral generators and exact exterior elimination

In the given integral lattice, every pairing in the transvection formula is an integer.
The even norm condition makes \((v,v)/2\) integral.
Using \((e,e)=(e,v)=0\), the displayed pairing expansion cancels term by term, and substitution of \(-v\) gives the two-sided inverse.
Thus integrality and lattice invertibility require neither primitivity of \(e\) nor an even ambient lattice.
The cyclic permutation preserves the positive dot product and fixes the hyperbolic summands, so its product with these transvections is an integral isometry.

The order of the two transvections matters and was independently checked.
For \(X=x+\alpha e+\beta f\), applying \(T_{f,w}\) first gives positive component \(x+\alpha w\) and \(f\)-coefficient \(\beta-w^{\mathsf T}x-b\alpha\).
The eigenvalue equation identifies that coefficient with \(z\beta\).
After applying \(T_{e,v}\) and the positive rotation, the remaining equations are exactly the three equations displayed in L462 v13.

For \(|z|>1\), \(zI-R_g\) is invertible and its finite geometric series yields the stated \(K(z)\).
Substituting the positive component gives precisely the two-by-two matrix in equation (5), including both factors of \(z\) in its second column.
A nonzero eigenvector cannot have \(\alpha=\beta=0\).
Conversely, any nonzero kernel vector of that matrix determines a nonzero \(X\) satisfying all original eigen-equations.
Therefore the determinant is equivalent to the existence of an exterior eigenvalue in both directions.
No claim about eigenvalues on the unit circle, pole cancellation or a globally normalized characteristic polynomial is needed.

### Growing support and the fixed-radius estimate

The binary expansion of the exponents in \(V_r\) gives one coefficient of magnitude one at every index from zero through \(N-1\).
Thus the squared norm is \(N=2^r\), which is even for the stated \(r\ge1\).
The shifted vector occupies indices \(N,\ldots,2N-1\) without wrap because \(g>2N\), so \(c=0\).
The vanishing order at one is \(r\).
All these facts hold for the stated scaling \(g=N^3+1\), which is odd and exceeds \(2N\).

For the Cayley estimate, orthogonal spectral decomposition reduces the real quadratic form to
\[
 \operatorname{Re}\frac{2+e^{i\theta}}{2-e^{i\theta}}
 =\frac{3}{5-4\cos\theta}\ge\frac13.
\]
The extra factor \(1/2\) gives the lower bound \(N/6\) for each diagonal quadratic expression in equation (5).
Complex phases do not remove positivity because the original vector is real and the real part is the symmetric quadratic-form contribution.

The cyclic overlap supports were checked in both directions.
The pairing \(w^{\mathsf T}R_g^jv\) can be nonzero only for \(1\le j\le2N-1\), with magnitude at most \(\min(j,2N-j)\).
The reverse pairing is its complementary cyclic shift and is supported only at \(j=g-2N+k\), \(1\le k\le2N-1\), with magnitude at most \(k\).
These support statements include wraparound and need only \(g>2N\).
Using \(\sum_{j\ge1}j2^{-j}=2\) gives exactly both bounds in equation (7).

For the stated scaling, \(|B|<1\) and \(|C|<3\), whence
\[
 (1+B)(1+2C)
 \le |1+B|\,|1+2C|<14.
\]
The positive quadratic terms therefore imply
\[
 D_{v,w}(2)<14-\frac{N^2}{18}<0
 \qquad(N\ge16).
\]
For each fixed \(r,g\), \(K(z)=O(z^{-1})\) and the determinant has leading term \(z^2\).
This asymptotic statement needs no uniform constant in the growing parameters.
Continuity on \(z>1\) supplies a real zero strictly greater than two.
The exact exterior equivalence and the \(q=1\) root count then give the claimed whole-measure result.
No numerical approximation, finite parameter extrapolation or discarded polynomial factor enters this chain.

### Source applicability and the remaining arithmetic problem

The [GHS13 edition record](../literature/GHS13/readme.md#arxiv-v2) was checked against the retained original.
The reviewer text-read the title/contents page and complete printed/PDF pages 53--54, and visually inspected page 54.
Equation (49), the adjacent inverse identity and Section 8.2's cusp notation match the formula and locator in L462 v13.
The source is attribution for a formula proved directly in the present lattice.
Its modular-group conclusions, primitive-cusp setup and signature \((2,n)\) are not assumptions transferred to this argument.
No priority investigation or full GHS13 proof audit is claimed.

The [accepted McM02 input](../literature/McM02/readme.md#canonical-coxeter-gap-input) concerns every word in the specified canonical geometric representation, not all integral isometries.
For a norm-two \(v\), direct composition of the stated reflections gives
\[
 s_{v-e}s_v(x)=x+(e,x)v-\bigl((v,x)+(e,x)\bigr)e=T_{e,v}(x),
\]
so the caution against assuming escape from Coxeter coverage is justified.
This identity alone does not identify the complete proposed family with a canonical Coxeter representation, and the reviewed text makes no such claim.

The [DS17 accepted univariate input](../literature/DS17/Yin_U001.md#ds17-u001) gives a positive logarithmic gap for every fixed bound on the number of nonzero coefficients, without bounds on degree or coefficient height.
The [L464 v19 cyclotomic completion](../../ledger/Yin_L_G0464_v19.md#fixed-number-of-terms) was checked at its explicit support-count interface: its fixed number \(K\) of central terms gives at most \(12+4K\) monomials after a measure-one multiplier.
Neither a fixed number of transvections nor growing vector support decides that property for the complete orthogonal characteristic polynomial.
L462 v13 correctly leaves the actual completion and representation checks open for any successor family.
The accepted external theorems retain their existing source-proof inspection limits; this review does not audit their original proofs.

The contextual restrictions in C881 v4, C884 v3, C880 v4, L462 v11 and L464 v18 were compared with the actual statement domains cited in L462 v13.
They respectively concern the specified integer pole, single signed term, unreduced linear-times-square input, preserved double trace factor and failure of a volume argument to furnish integer existence.
The reviewed text does not combine them into an exclusion of arbitrary integer prefix completion.
In particular, small volume is not treated as absence of integer points.

The sufficient original-Task bridge is still an actual nonneutral integral family with fixed negative index and spectral radius tending to one, or a varying-index family with \(q\log\rho\to0\).
The \(q=1\) discussion is a Salem-type restriction and does not assert that every possible Lehmer counterexample has that root type.
The displayed obstruction resolves neither this existence problem nor the unrestricted [Task contract](../../tasks/Yin_T_G0001_v1.md#contract).
No new computational campaign, formal verification or research-law optimization was performed in this review.
