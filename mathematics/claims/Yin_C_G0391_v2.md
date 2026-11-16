---
author: Yin
---

# Invariant factors of periodic points for an irreducible toral automorphism

<a id="statement"></a>
## Which cyclic factors carry the Mahler measure

Let \(A\in\operatorname{GL}_D(\mathbb Z)\) have irreducible characteristic polynomial \(Q\) and a nontorsion eigenvalue \(\alpha\), with logarithmic Mahler measure \(m=m(Q)\).
For every \(N\ge1\) write \(s_1(N),\ldots,s_D(N)\) for the positive Smith invariant factors of \(A^N-I\), in decreasing divisibility order, including ones.
These are the cyclic orders of the group fixed by \(A^N\) on \(\mathbb R^D/\mathbb Z^D\), since that group is \((A^N-I)^{-1}\mathbb Z^D/\mathbb Z^D\).
Let
\[
   b_N=[\mathbb Q(\alpha):\mathbb Q(\alpha^N)]\,
   \begin{cases}
   2,&\alpha^{-N}\text{ is conjugate to }\alpha^N,\\
   1,&\text{otherwise}.
   \end{cases}
\]
The sequence \(b_N\) is periodic and divides \(D\).
There is a positive integer \(C_A\), independent of \(N\), such that
\[
  s_1(N)/s_{b_N}(N)\mid C_A,\qquad
  \sum_{i>b_N}\log s_i(N)=o_A(N).
\]
Consequently each of the first \(b_N\) cyclic factors has logarithm \(Nm/b_N+o_A(N)\).
In particular \(\limsup_{N\to\infty}N^{-1}\log s_1(N)\) equals \(m\) for nonreciprocal \(Q\) and \(m/2\) for reciprocal \(Q\).
Both rates in the limsup are attained as limits along the prime indices.
The positive Lehmer gap is equivalent to a uniform positive lower bound on these limsups over all such toral automorphisms.

Corvaja, Rudnick and Zannier study the gcd of the entries of \(A^N-I\), and Magagna studies divisibility of its higher minors in terms of multiplicative dependence among eigenvalues.
The calculation below uses the fixed matrix conjugation and the S-unit gcd estimate to determine the individual factors in the irreducible unit case at every exponent, including the effect of torsion ratios. [Corvaja, Rudnick and Zannier](https://arxiv.org/abs/math/0309215) and [Magagna](https://arxiv.org/abs/math/0610277).

<a id="blocks"></a>
## Conjugates with equal or inverse powers

Write \(x_1,\ldots,x_D\) for the roots of \(Q\) in a Galois splitting field \(L\).
Put indices \(i,j\) in the same class if \(x_i^N=x_j^N\) or \(x_i^N=x_j^{-N}\).
Every fiber of \(x_i\mapsto x_i^N\) has the field degree in the formula for \(b_N\), by the extensions of each embedding of \(\mathbb Q(\alpha^N)\).
If the powered orbit contains one inverse it contains the inverses of all its elements, and an element cannot equal its own inverse by nontorsion.
Thus all classes have size \(b_N\).
Membership of a pair depends only on whether the order of one of the roots of unity \(x_i/x_j,\ x_ix_j\), whenever it is torsion, divides \(N\).
The lcm of the finitely many such orders is a period.
Every class for \(N=1\) is contained in the corresponding class for each \(N\).
All primes exceeding the period have \(b_p=b_1\), with \(b_1=2\) for reciprocal \(Q\) and one otherwise.

At a finite prime \(\mathfrak P\) of \(L\) put \(w_i=v_{\mathfrak P}(x_i^N-1)\) in integral valuation.
Within each class these weights are identical because every \(x_i\) is a unit.
For pairs in distinct classes the total normalized pairwise overlap satisfies
\[
 \frac1{[L:\mathbb Q]}
 \sum_{i<j\ {\rm in\ distinct\ classes}}\ \sum_{\mathfrak P}
 \min(w_i,w_j)\log N\mathfrak P=o_A(N).                               \tag{1}
\]
For an independent pair this is the [Corvaja–Zannier estimate](../audits/literature/CZ05/Yin_U001.md#s-unit-gcd) on \(x_i^N,x_j^N\), independent units of equal height \(Nm/D\).
Distinct exponents give distinct pairs, so its finite exceptions do not affect the limit.
For a dependent pair the equal positive heights give \(x_j=\zeta x_i^{\pm1}\), as in the [conjugate-pair calculation](Yin_C_G0899_v5.md#overlap).
When the pair belongs to different classes the ideal of the two differences contains the nonzero \(\zeta^N-1\).
There are only finitely many nonzero values of this element, bounding the pair's contribution uniformly at these \(N\).
Summing over the fixed finite list proves (1) along all exponents.

<a id="smith"></a>
## Comparing the integer lattice with the eigenbasis

For each \(\mathfrak P\), sort the weights in decreasing order as \(w_{(1)},\ldots,w_{(D)}\).
A class of largest weight gives \(w_{(1)}=\cdots=w_{(b_N)}\).
The sum after removing that entire class is bounded by the sum of pairwise minima over different classes, since each remaining index can be paired with one fixed member of the removed class.
This remains true in a tie.

Diagonalize \(A\) over \(L\) by a fixed matrix \(V\), and choose a rational integer \(h\ge1\) clearing all denominators of \(V,V^{-1}\).
For every \(r\), the ideals of \(r\)-row minors of \(A^N-I\) and of the diagonal matrix with entries \(x_i^N-1\) include one another after multiplication by \(h^{2r}\).
This follows in both directions by Cauchy–Binet from the fixed conjugation.
Over the integers the gcd of the \(r\)-row minors is the product of the \(r\) smallest Smith factors.
Over the splitting field the smallest valuation of a diagonal \(r\)-row minor is the sum of the \(r\) smallest weights.
Taking two consecutive sizes shows, for \(1\le i\le D\),
\[
 \big|v_{\mathfrak P}(s_i(N))-w_{(i)}\big|
                                  \le 4D\,v_{\mathfrak P}(h).
\]
The upper factors therefore satisfy \(s_1/s_{b_N}\mid h^{8D}\), using integrality of their quotient and the equality of the largest \(b_N\) local weights.
Summing the lower-factor comparison with weights \(\log N\mathfrak P/[L:\mathbb Q]\) changes the total by \(O_A(1)\).
Equation (1) proves the sublinear bound for the entire tail.

The product of all the factors is \(|\det(A^N-I)|=|\operatorname{Norm}_{\mathbb Q(\alpha)/\mathbb Q}(\alpha^N-1)|\).
Its logarithm is \(Nm+O_A(\log(2N))\) by the [signed resultant estimate](../ledger/Yin_L_G0462_v42.md#substitution).
Subtracting the tail, dividing by \(b_N\), and using the bounded quotient within the leading part proves the individual rates.
The limsup assertion follows from \(b_N\ge b_1\) and \(b_p=b_1\) at sufficiently large primes.
Every nontorsion unit occurs as an eigenvalue of its integral companion automorphism, proving both directions of the gap equivalence by \(1\le b_1\le2\).

<a id="example"></a>
## Changes in the number of growing factors for one matrix

For the companion of \(Q(z)=z^4+z^2-1\), the number \(b_N\) is one for odd \(N\), two for \(N\equiv2\bmod4\), and four for \(4\mid N\).
Indeed the positive root \(\alpha\) has square \(u=(\sqrt5-1)/2\), of quadratic norm \(-1\).
Thus \(u\) cannot be a square in its quadratic field, proving irreducibility.
The roots are \(\alpha,-\alpha,i/\alpha,-i/\alpha\).
At odd \(N\) the four powers are distinct and none is the inverse of another, as their phases and moduli show.
At \(N\equiv2\bmod4\) each pair with the same modulus coalesces, and the two powered values have product \(-1\).
At \(4\mid N\) the two remaining values are inverses.
The same positive measure is accordingly shared by one, two or four leading cyclic factors according to the exponent.

## Assessment history

### Decision periodic-smith-factors-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:29 |
| status | open |
| reason | Register all-exponent growth of the cyclic factors of an irreducible toral periodic point group. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Periodic point group](#statement) | Leading factors, bounded ratios, subexponential tail, limsup and gap equivalence. |
| argument | [Power classes](#blocks) | Periodicity, powered field degree and normalized overlap across distinct classes. |
| argument | [Smith factors](#smith) | Fixed conjugating matrices, all local determinantal divisors, growth and exact divisibility. |
| argument | [Quartic example](#example) | One, two and four leading factors for the same integral automorphism. |
| dependency | [S-unit gcd](../audits/literature/CZ05/Yin_U001.md#cz05-u001) | Sublinear normalized common valuation on independent conjugate powers. |
| dependency | [Dependent conjugates](Yin_C_G0899_v5.md#overlap) | Equal heights force an inverse or direct torsion twist. |
| dependency | [Norm estimate](../ledger/Yin_L_G0462_v42.md#substitution) | Total logarithmic size at every exponent. |

### Decision periodic-smith-factors-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:33 |
| status | proved |
| reason | Adopt the periodic point invariant-factor theorem after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Periodic point group](#statement) | Leading factors, bounded ratios, subexponential tail, limsup and gap equivalence. |
| argument | [Power classes](#blocks) | Periodicity, powered field degree and normalized overlap across distinct classes. |
| argument | [Smith factors](#smith) | Fixed conjugating matrices, all local determinantal divisors, growth and exact divisibility. |
| argument | [Quartic example](#example) | One, two and four leading factors for the same integral automorphism. |
| dependency | [S-unit gcd](../audits/literature/CZ05/Yin_U001.md#cz05-u001) | Sublinear normalized common valuation on independent conjugate powers. |
| dependency | [Dependent conjugates](Yin_C_G0899_v5.md#overlap) | Equal heights force an inverse or direct torsion twist. |
| dependency | [Norm estimate](../ledger/Yin_L_G0462_v42.md#substitution) | Total logarithmic size at every exponent. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v82.md#periodic-smith-review) | All exponent classes, bounded integral ratios, tail and leading rates, prime limit, gap equivalence and the quartic example. |

## Current assessment

[Selected decision](#decision-periodic-smith-factors-reviewed)
