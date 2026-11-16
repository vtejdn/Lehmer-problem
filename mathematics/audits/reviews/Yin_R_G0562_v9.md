---
author: Yin
---

# Review of the uniform Pisot bound for a fixed Chebyshev offset

An agent outside the development of C345v9 reviewed its complete fixed argument for Yin on 2026-11-16T14:48 UTC.
The assignment supplied the target and scope without proof-development discussion or a prior finding on this claim.
The reviewer had previously checked the offset-one perturbation and harmonic arguments and rechecked their interfaces at offset \(d\).

<a id="fixed-offset-review"></a>
## The fixed-offset theorem

For fixed \(d,s,\epsilon\), the proof bounds \(q\) uniformly on the stated sparse class and therefore bounds \(\theta-q\) away from zero.
The minus sign allows all \(d\ge1\), and substitution \(z\mapsto-z\) gives the plus sign when \(d\) is odd.

### Reduction to integer Laurent rows

The bound \(q-1\mid C(2)\le2\cdot4^h\) forces \(h\to\infty\) along any hypothetical sequence with \(q\to\infty\).
All roots of \(\Pi\) are on the circle and \(M(\Pi)=2\), so the sparse height estimate bounds its circle supremum in terms of \(s\).
Since the prescribed prefix grows proportionally to \(h\), \(\Pi\) tends coefficientwise to \(A=2-z^d\) after the indicated rotation.
From \(B^\sharp=\Pi/K_q\), the integer coefficients of \(B^\sharp\) converge to the coefficients of \(A/K\), which are therefore integers.
As in L462v55 the poles of this rational integer series are torsion, while the reduced numerator of \(K\) must contain the whole irreducible \(z^d-2\) exactly once.
Otherwise either a nontorsion pole remains in \(A/K\) or \(K\) is twice an integral series, impossible because the coefficient of \(z^d\) in \(A\) is odd.
The remaining factors are squarefree cyclotomic factors by positivity, rationality and the simple-pole and simple-zero bounds.
The nonzero continuous density persists under the rotation.

For \(K=AU/V\), the exact identity \(AUB^\sharp-V\Pi=(AU/2)\Pi(J_q-J)\) follows from \(J=2V/(AU)\).
If \(B^\sharp=V/U\) through a fixed fraction of the degree, then \(J_q-J\) vanishes through a common linear-length prefix.
Choose \(L=2h+O_{d,U,V}(1)\) strictly greater than the two product degrees.
The two cutoffs of L462v51 apply with the same bounded \(L^1\) norms and \(|A|\ge1\) on the circle.
They force the positive-measure polynomial \(UB^\sharp\) to have bounded support while its Mahler measure tends to one, a contradiction.
This also excludes an infinite subsequence of exact equalities and gives \(n\to\infty,\ n/h\to0\).
For fixed \(k\ge1\) and \(l\in\mathbb Z\), both \(kn+l\) and \(kn+l-d\) then fall inside the exact prefix.
The coefficients of \(J_q-J\) vanish at negative offsets from the first discrepancy, by formal division by \(1-z^d/2\).
The first weighted marginal therefore cancels the atomic phases, and the extremal value on each such fiber fixes every higher atomic phase as in L462v52.
The vanishing negative atom costs the same uniform error after rotation.
Multiplication by \(1-v^d/2\) gives integer coefficients in the moving windows, including a nonzero first discrepancy.
Bounded marginal density and Parseval make every \(H_k\) a Laurent polynomial, and continuous Toeplitz positivity gives probability moments at all regular points with positive density.
The identities \(\sigma=2\rho/|K|^2\), \(M(K)=2\), and \(M(1-z^d/2)=1\) give exactly \(M(D)=M(\rho)/2\).

### Finite shapes and the prime specialization

A bound \(|P|\le D\) bounds the number and sizes of integer coefficients by Parseval.
After fixing the ordered coefficients and shifting the least exponent to zero, infinitely many polynomials would force at least one unbounded consecutive gap.
Extraction makes each gap fixed or divergent, leaving fixed nonzero blocks and divergent distances between different blocks.
Against every continuous test the cross terms of their squared moduli vanish by Fourier decay.
Hence the sum of the block squares is bounded by \(D^2\) almost everywhere, using arbitrary nonnegative continuous tests.
The geometric-mean inequality for any two blocks gives \(M(D)^2\ge2M(P_1)M(P_2)\ge2\).
The logarithms used for the nonzero integer blocks are integrable, so isolated zeros have no effect on the argument.

For a finite list of actual shapes \(P\) with \(M(P)<2\), none vanishes at \(t=2^{1/d}\).
Indeed \(z^d-2\) is Eisenstein, has measure two, and divisibility after clearing a Laurent monomial would give \(M(P)\ge2\) by Gauss's lemma.
The numerator of \(R_P\) at \(t\) is \(P(t)(2-t^{-d})\ne0\) and its denominator is zero.
If \(R_P(z^2)=R_P(z)^2\) identically, a pole at \(t\) would force a pole at \(t^2\), and iteration would give infinitely many distinct poles.
The nonidentity and the finite shape list allow one to exclude all exceptional zeros and poles at a single sufficiently large prime, simultaneously for all its primitive roots.
Include all zeros of the fixed nonzero rational density, so every chosen conjugate is a regular point of positive marginal density.
If \(R_P(\xi)\in\mu_p\), the automorphism \(\xi\mapsto\xi^2\) would imply the excluded equality at \(\xi\).
The ratio of a nonzero \(c_k(\xi)\) to its conjugate is \(\xi^{2e}R_P(\xi)\), since the density cancels and the factor \(1-\xi^d/2\) supplies the displayed phase ratio.
It cannot equal one, regardless of the monomial shift \(e\).

At fixed \(\xi\), a single positive integer clears the denominator \((1-\xi^d/2)\sigma(\xi)\) in the sense that its quotient by this element belongs to \(\mathbb Z[\xi]\).
This handles every shift and shape, and conjugation handles all negative moment indices.
At every embedding the evaluation is again the moment sequence of a probability because the formulas are rational over \(\mathbb Q\), complex conjugation commutes with the embeddings, and positivity holds at all these points.
The coordinates of the cleared values in \(1,\xi,\ldots,\xi^{p-2}\) are integers and are fixed linear combinations of the conjugate sequences by invertibility of the conjugate evaluation matrix.
Each coordinate is a Fourier–Stieltjes transform on the full discrete group \(\mathbb Z\), since the same finite linear combination of its representing measures is a finite complex measure.
Sanders's locally compact Corollary 12.4 gives eventual periodicity, with a common positive period \(T\) for the finitely many coordinates.
I used this theorem at its statement and application scope.
The eventual value on \(Tl\) is the mass on \(\mu_T\) by Cesàro averaging, and must be zero since every allowed nonzero moment is nonreal.
Positivity then gives zero eventual value on every \(Tl+a\).
Since none of the chosen shapes vanishes at \(\xi\), only finitely many \(H_k\) are nonzero globally.
At the greatest such index \(r\), the pushforward by \(u\mapsto u^r\) has only constant and first moments and their conjugates.
Positivity gives \(|c_r|\le1/2\) at every regular positive-density point, proving \(1\le M(H_r)\le M(D)/2\).
This contradicts \(M(D)<2\).

### Checking the bracket enumeration and both exceptional envelopes

I regenerated the primitive slope list using the exact adjacent-level test in L462v55.
The forbidden open-arc crossing is of odd multiplicity, while the only allowed torsion phases have \(w^a=1,-1,e^{\pm i\pi/3}\).
The five endpoint levels consequently give the displayed inequalities in \(a,s=a+b\), and the candidate \(a=6\) fails coprimality.
The sole extra triple from enumeration with \(a\le5\), namely \((5,-4,-)\), has a sign change of \(2\sin t+\sin(9t)\) between \(\pi/9\) and \(\pi/6\).
The fifth power takes no allowed value inside that interval.
I also factored each surviving primitive Laurent bracket over the integers after clearing its lowest exponent.
For \(a=1\) the two large cases have bracket \(4-w-w^{-1}\) and \(3(1-w)\).
The first has no circle zero.
In the second all \(d\) lifted zeros are simple and the required denominator-minus-numerator degree is \(d\), forcing every factor into \(V\), including after rational splitting.
The absolute constants of two in the \(b=1\) brackets give measure two and stay below \(2\sqrt2\).

The seven rows for \(a\ge2\) give the quadratic pair stated for \(a=2\), the cubic and its signed reciprocal in the three indicated degree-seven brackets, a cyclotomic residual at \((3,-1,-)\), and the reciprocal quartic at \((3,-2,-)\).
For the cubic the positive real root \(\gamma>2/3\) is unique, its complex roots have modulus \(\gamma^{-1/2}\), and the product with its reciprocal has measure \(\gamma^{-2}<9/4\).
For the quartic, substituting the real and imaginary parts of the nonreal trace in the ellipse equation gives \(t^2-t-5=0\) for \(t=R^2+R^{-2}>2\).
Its larger solution gives \(1<R^2<5/2\), and the two exterior roots give measure \(R^2\).
All these cases have \(M(D)<\sqrt2\).

For \(K=2-z^d\), substitution preserves the mean \(7/2\) of \(D^2\) and its supremum four.
The fourth-moment exclusion for three nonarithmetic exponents and the phase alignment for three arithmetic exponents rely only on these bounds.
With a binomial \(1\pm z^l\) after normalization, every one of its \(l\) alignment points must satisfy \(z^d=\pm1\), giving \(l\le2d\).
This gives finitely many shapes and \(M(D)=(2+\sqrt3)/2<2\).
For \(K=(2-z^d)/(1-z^d)\), the quadratic vanishing of the envelope at every \(d\)-th root forces integral Laurent divisibility by \((1-z^d)^2\).
The quotient has squared mean at most three by orthogonality of powers of \(z^d\).
In the equality case \((2-z^d)P_0\) would have constant nonzero modulus and hence be a Laurent monomial, impossible at \(2^{1/d}\).
Therefore the quotient is a signed monomial or a shifted signed binomial.
For binomial gap \(l\ne d\) the exponents \(0,l,d,l+d\) are distinct and the squared norm of the product is \(1+1+4+4=10\), above its pointwise bound nine.
This leaves finitely many quotient shapes and \(M(D)=3/2<2\), so the specialization applies in this last case too.

Finally the Chebyshev geometric sums give the stated four-term lift, with first trailing index \(2h+2-d>h\) for \(h\ge d\).
It therefore belongs to the claimed class with \(s=4,\epsilon=1\), independently of degree parity.
The derivative identity on the second branch gives \(\theta-q\ge2/(q+3)\), completing the excess assertion without a numerical bound uniform in \(d\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fixed-offset theorem](#fixed-offset-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fixed-offset theorem](#fixed-offset-review) | [Uniform bound](../../claims/Yin_C_G0345_v9.md#statement) | Fixed \(d,s,\epsilon\), the prescribed signs, both degree parities, the exact lift and the excess consequence. |
| [Fixed-offset theorem](#fixed-offset-review) | [Integer harmonics](../../claims/Yin_C_G0345_v9.md#harmonics) | Rational limit, offset-dependent numerator, cutoffs, atomic cancellation, row integrality and density normalization. |
| [Fixed-offset theorem](#fixed-offset-review) | [Finite shapes](../../claims/Yin_C_G0345_v9.md#finite-shapes) | Fixed coefficients, diverging gaps, weak cross-term limits and the strict \(\sqrt2\) threshold. |
| [Fixed-offset theorem](#fixed-offset-review) | [Prime specialization](../../claims/Yin_C_G0345_v9.md#torsion) | Noncanceled pole, dyadic functional identity, every prime conjugate, cleared integer coordinates, eventual periodicity and the greatest harmonic. |
| [Fixed-offset theorem](#fixed-offset-review) | [Primitive bracket measures](../../claims/Yin_C_G0345_v9.md#brackets) | Exact primitive enumeration, rational factorizations, cubic and quartic measures and the two exceptional profiles. |
| [Fixed-offset theorem](#fixed-offset-review) | [Exceptional envelopes](../../claims/Yin_C_G0345_v9.md#exceptions) | Trinomial exclusion, bounded binomial gap, double vanishing, the constant-modulus equality case and the two geometric means. |
| [Fixed-offset theorem](#fixed-offset-review) | [Primitive slope inputs](../../ledger/Yin_L_G0462_v55.md#fixed) | Permitted primitive triples for the fixed \(d\) reduction. |
| [Fixed-offset theorem](#fixed-offset-review) | [Four arcs](../../ledger/Yin_L_G0462_v55.md#bracket) | Local hypotheses for perturbations, exhaustion of triples and allocation after \(w=z^g\). |
| [Fixed-offset theorem](#fixed-offset-review) | [Sparse cutoffs](../../ledger/Yin_L_G0462_v51.md#window) | Both cutoff norms, degree adjustment, exact polynomial identity and sparse gap. |
| [Fixed-offset theorem](#fixed-offset-review) | [Moving harmonics](../../ledger/Yin_L_G0462_v52.md#harmonics) | Common conditional probabilities and moving coefficient differences at offsets \(l\) and \(l-d\). |
| [Fixed-offset theorem](#fixed-offset-review) | [Integer transforms](../literature/San20/Yin_U001.md#fourier-stieltjes) | Locally compact integer Fourier–Stieltjes theorem on \(\mathbb Z\) applied separately to finitely many integer coordinate sequences. |
| [Fixed-offset theorem](#fixed-offset-review) | [Integral shape bounds](../../ledger/Yin_L_G0462_v50.md#shapes) | Fourth moments, arithmetic-progression alignment, constant-modulus equality and finite integer supports. |
| [Fixed-offset theorem](#fixed-offset-review) | [Derivative](../../ledger/Yin_L_G0462_v36.md#second) | Uniform lower excess on the second branch from bounded positive constant. |
