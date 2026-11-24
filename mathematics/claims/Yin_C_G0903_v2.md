---
author: Yin
---

# Reciprocal multiple roots with at most twice the multiplicity plus one terms

2026-11-24T18:22 UTC.

<a id="statement"></a>
## The degree after removing common exponent differences

Let \(G(X)=\sum_{i=1}^k c_iX^{a_i}\) be a rational Laurent polynomial with distinct integer exponents, all \(c_i\ne0\), and \(k\ge2\).
Suppose \(\alpha\in\mathbb C^\times\) and \(\alpha^{-1}\) are roots of multiplicity at least \(r\ge1\).
Write \(g=\gcd_{i,j}|a_i-a_j|\) and \(\beta=\alpha^g\).
One has \(k\ge r+1\).
If \(k\le2r+1\), put \(t=k-r-1\).
Then
\[
                     [\mathbb Q(\beta):\mathbb Q]\le {2t\choose t}.                \tag{1}
\]
If \(\alpha\) is a nontorsion algebraic unit, its total logarithmic Mahler measure satisfies
\[
                         m(\alpha)\ge\frac{\log2}{4{2t\choose t}} .                \tag{2}
\]
The bounds are independent of the coefficients and the exponent span.
In particular an [ordinary two-row graph](Yin_C_G0345_v408.md#lower) with at most five occupied terms, coprime integral rows, nonzero reflected determinant and a repeated monic reciprocal irreducible nontorsion unit factor satisfies
\[
                   [\mathbb Q(\alpha^g):\mathbb Q]\le6,\qquad
                   H\ge2^{p/24},\qquad H=\max(\|A\|_1,\|C\|_1),
\]
where \(p\) is its exponent parameter and \(\alpha\) is a root of that factor.
For four or fewer terms no such factor exists.
At five terms and degree six for \(\alpha^g\), a further condition on the sextic field [excludes the known consecutive-coefficient Salem seed](#sextic).

<a id="interpolation"></a>
## Interpolating the two Euler systems

Translate the least exponent to zero and divide all exponent differences by \(g\).
The resulting polynomial has roots \(\beta,\beta^{-1}\) of the same respective multiplicities because a nonzero monomial does not affect them and the power map is unramified away from zero.
Write \(b_1,\ldots,b_k\) for its resulting exponents, whose differences have gcd one.
Let \(D_i=\prod_{j\ne i}(b_i-b_j)\).
For either sign the Euler equations at \(\beta^{\pm1}\) read
\[
                     \sum_i b_i^j c_i\beta^{\pm b_i}=0\qquad(0\le j<r).
\]
If \(k\le r\), the first \(k\) equations form an invertible Vandermonde system, contradicting the nonzero terms.

For \(k\ge r+1\), the kernel of these first \(r\) moment rows consists exactly of the vectors \((Q(b_i)/D_i)_i\) with \(\deg Q\le t\).
Indeed, for \(0\le j<r\), the coefficient of \(x^{k-1}\) in the Lagrange interpolation of \(x^jQ(x)\) is \(\sum_i b_i^jQ(b_i)/D_i\), and it vanishes since \(j+t\le k-2\).
The evaluation map is injective on these polynomials, so the indicated subspace has dimension \(t+1=k-r\), equal to the kernel dimension.
There are therefore polynomials \(Q_+,Q_-\) of degrees at most \(t\) with \(Q_\pm(b_i)=D_i c_i\beta^{\pm b_i}\).
Their product \(S=Q_+Q_-\) takes the rational values \((D_i c_i)^2\) at all \(k\) distinct rational nodes.
When \(k\le2r+1\), its degree is at most \(2t\le k-1\), so interpolation determines \(S\) over \(\mathbb Q\).

Let \(Q\) be the monic normalization of \(Q_+\).
Its coefficients are algebraic, and their conjugates give monic divisors of \(S\) of the same degree.
The number of such divisors is at most \({2t\choose t}\), even if some roots of \(S\) repeat, by counting subsets of a labelled list of at most \(2t\) roots.
For every pair of indices,
\[
                  \beta^{b_i-b_j}
                    =\frac{D_jc_j Q(b_i)}{D_ic_i Q(b_j)} .
\]
Thus all these powers belong to the coefficient field of \(Q\).
Their exponents generate \(\mathbb Z\), which proves (1).

For (2), take \(E=\mathbb Q(\alpha)\), \(K=\mathbb Q(\alpha^g)\), \(s=[E:K]\), and \(u=N_{E/K}(\alpha)\).
Each conjugate over \(K\) differs from \(\alpha\) by a \(g\)-th root of unity, so \(u^g=\alpha^{gs}\).
In particular \(u\) is a nontorsion unit and its absolute logarithmic height is \(s\) times that of \(\alpha\).
Hence \(m(\alpha)=[K:\mathbb Q(u)]m(u)\).
The [house bound of Dimitrov](../audits/literature/Smy08/Yin_U001.md#smy08-house) yields \(m(u)\ge(\log2)/(4[\mathbb Q(u):\mathbb Q])\), since a rational unit is torsion.
Now apply (1).
For the stated graph application take \(r=2\) and use the [individual determinant bound](Yin_C_G0345_v408.md#lower), which gives \(p\,m(\alpha)\le\log H\).

<a id="real"></a>
## Four-term exclusion and sharpness for double roots

More generally, a real Laurent polynomial with \(k\le r+2\) terms cannot have roots \(z,z^{-1}\) of multiplicity at least \(r\ge2\) if \(|z|\ne1\).
The Vandermonde argument leaves \(k\ge3\).
Choose any pair of indices \(i,j\) and retain a third index \(h\).
With \(\mathcal E=X\,d/dX\), apply \(\prod_{\ell\notin\{i,j,h\}}(\mathcal E-a_\ell)\) to the polynomial.
Each operator lowers the multiplicity at a nonzero root by at most one, and \(k-3\le r-1\), so both points remain roots.
The three surviving coefficients are real and nonzero.
After removing a monomial the two equations are \(u+v z^{\pm(a_j-a_i)}=-w z^{\pm(a_h-a_i)}\).
Multiplication gives
\[
 z^{a_j-a_i}+z^{-(a_j-a_i)}=(w^2-u^2-v^2)/(uv)\in\mathbb R .
\]
This uses the same two-orientation identity as the [individual trinomial factor estimate](Yin_C_G0345_v181.md#powers).
Since \(z^{a_j-a_i}\) has modulus different from one, its imaginary part must vanish.
This holds for every pair, so \(z^g\) is real by Bézout's identity.
After the common exponent divisor is removed, the two distinct real roots \(z^g,z^{-g}\) have the same sign and both retain multiplicity at least \(r\).
Substitute \(-X\) if necessary and apply Descartes' rule of signs to the polynomial after removing its lowest monomial.
Its \(k\) terms allow at most \(k-1<2r\) positive roots counted with multiplicity, a contradiction.
For a reciprocal nontorsion unit at least one conjugate lies off the circle by Kronecker's theorem, and its inverse is also a conjugate.
This proves the four-term exclusion.

Five terms can realize double contact with all the structural conditions on ordinary two-row graphs if their coefficient height is unrestricted.
Let \(B=(3+\sqrt5)/2\), let \(P=X^2-3X+1\) be its minimum, and fix any odd prime \(p\).
Divisibility by \(P^2\) imposes at most four rational homogeneous conditions on the five coefficients at exponents \(0,1,p,p+1,2p\).
Take a nonzero rational solution and clear denominators.
All five coefficients are nonzero by the four-term exclusion.
The resulting \(A(X^p)+XC(X^p)\) has \(\deg A=2\), \(\deg C=1\), nonzero endpoints in both rows and exponent-difference gcd one.
The power \(B^p\) is irrational since its inverse is its distinct conjugate.
A common row factor would thus be linear and nonvanishing at \(B^p\).
Removing it would leave double contact on a graph with at most three terms, again impossible.
The reflected determinant is nonzero since \(A(Y)A(Y^{-1})\) has a nonzero term of exponent two whereas \(C(Y)C(Y^{-1})\) does not.
Here \(m(B)=\log B>\log2\), so the individual determinant bound forces \(H>2^p\).
This example establishes sharpness in the number of terms before imposing the height cutoff of the [prescribed-prime test](Yin_C_G0901_v3.md#statement).

<a id="sextic"></a>
## The square condition at degree six

Suppose \(r=2,\ k=5,\ [\mathbb Q(\beta):\mathbb Q]=6\).
Equality in the divisor count implies that \(S\) has four distinct roots and that \(Q_+\) and \(Q_-\) are both quadratic.
Indeed a polynomial of degree at most three, or a quartic with a repeated root, has fewer than six monic divisors of any fixed degree.
The monic normalization of \(Q_+\) therefore has six conjugates corresponding to all unordered pairs of four roots.
Its coefficient field contains \(\beta\) and has degree six, so equals \(\mathbb Q(\beta)\).
The formula for \(\beta^{b_i-b_j}\) above recovers \(\beta\) from each conjugate by a fixed rational expression, using a single Bézout identity for the differences.
For the complementary pair the same expression recovers \(\beta^{-1}\), by the interpolation values of \(Q_-\).
In particular the six conjugates are paired by inversion.

Every permutation of four letters acts evenly on their six unordered pairs, since a transposition switches precisely two pairs of these subsets.
Thus the Galois action on the six embeddings of \(\mathbb Q(\beta)\) is even.
Let \(F\) be the monic minimum of \(\beta\) and choose one value \(\beta_j\) from each of the three inverse pairs.
The product \(D=\prod_{j=1}^3(\beta_j-\beta_j^{-1})\) is fixed by Galois because a permutation of whole pairs is even and preserves the product, while each flip is odd and changes its sign.
Consequently
\[
                              -F(1)F(-1)=D^2\in\mathbb Q^{\times2}.
\]
If \(\beta\) is integral then \(D\) is a rational algebraic integer, so the product is an integer square.

For example, let \(\lambda\) be the [sextic Salem unit at coefficients two and three](../computations/programs/Yin_J_G0185/witnesses.md#witness), of minimum \(P_\lambda=X^6-X^5-X^3-X+1\).
Here \(-P_\lambda(1)P_\lambda(-1)=5\), so some Galois element acts oddly on the six embeddings of \(\mathbb Q(\lambda)\) by the same flip count.
Every nonzero power of \(\lambda\) generates that field because \(\lambda>1\) is the unique conjugate of its modulus.
More generally, take \(\alpha\) satisfying \(\alpha^v=\omega\lambda^u\) for nonzero integers \(u,v\) and a root of unity \(\omega\).
If \(\alpha,\alpha^{-1}\) were both double roots of a rational polynomial with at most five terms, then a nonzero power of \(\beta=\alpha^g\) would equal a nonzero power of \(\lambda\).
Thus \(\mathbb Q(\beta)\) would contain \(\mathbb Q(\lambda)\).
Bound (1) and the four-term exclusion would give degree six and equality of the fields.
The even action at degree six contradicts the odd permutation just obtained.
This rules out reciprocal double contact throughout these powers, radicals and torsion twists.

## Assessment history

### Decision sparse-reciprocal-interpolation

| Field | Value |
| --- | --- |
| date | 2026-11-24T18:35 |
| status | proved |
| reason | Interpolation bounds the power degree uniformly in the coefficients and yields an exponential row-height lower bound through five terms. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The degree and measure of a reciprocal multiple root at the given support and multiplicity. |
| argument | [interpolation](#interpolation) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [real](#real) | Proof of the conclusions in this section under its stated hypotheses. |
| argument | [sextic](#sextic) | Proof of the conclusions in this section under its stated hypotheses. |
| dependency | [House bound](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | The house bound gives a total measure floor after norm descent. |
| dependency | [Input](Yin_C_G0345_v408.md#lower) | The ordinary row height bounds the seed measure at the exponent prime. |
| dependency | [Input](../computations/programs/Yin_J_G0185/witnesses.md#witness) | The sextic Salem polynomial determines the parity obstruction for its powers and radicals. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1048.md#finding) | The statement, proofs and qualifications at the checked input interfaces. |

## Current assessment

[Selected decision](#decision-sparse-reciprocal-interpolation)
