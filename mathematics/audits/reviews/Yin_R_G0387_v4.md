---
author: Yin
---

# Mixed resultants and the degree-sized return of a Salem–Boyd family

A reviewer outside the proof development independently examined the whole statement and proof of G0162v3 for Yin on 2026-11-16 at 11:29 UTC.
The inputs were the fixed claim, its direct mathematical interfaces and the applicable review rules.
The reviewer also consulted the earlier finding on the different finite-prime constructions in G0162v2.
No development discussion, author explanation or previous verdict on G0162v3 was supplied or used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Salem family and its local products](#salem-local-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Salem family and its local products](#salem-local-review) | [Statement](../../claims/Yin_C_G0162_v3.md#statement) | The full family, degree and measure, local window, mixed and cyclic resultants, orbit fractions and the degree-sized half-turn. |
| [Salem family and its local products](#salem-local-review) | [Delay and reduction](../../claims/Yin_C_G0162_v3.md#choice) | Both choices of degree, the lcm estimate, coefficients, avoidance of small residue degrees and squarefree reduction. |
| [Salem family and its local products](#salem-local-review) | [Irreducibility](../../claims/Yin_C_G0162_v3.md#salem) | The exterior root, torsion exclusion, irreducibility of the entire quotient and preservation of degree under powers. |
| [Salem family and its local products](#salem-local-review) | [Mixed collisions](../../claims/Yin_C_G0162_v3.md#different-ratios) | Elimination at non-Frobenius ratios, injectivity on reduced roots and exclusion of cyclic collisions. |
| [Salem family and its local products](#salem-local-review) | [Local depths](../../claims/Yin_C_G0162_v3.md#unit-depth) | The two signs, first nonzero coefficient modulo the prime square, valuation amplification and the contributing pairs. |
| [Salem family and its local products](#salem-local-review) | [Orbit fractions](../../claims/Yin_C_G0162_v3.md#orbit-fraction) | All ordered-pair orbits, rank-two applicability, the uniform upper bound and weighted lower bound. |
| [Salem family and its local products](#salem-local-review) | [Degree-sized return](../../claims/Yin_C_G0162_v3.md#adaptive-return) | The exact products, degree choice, prime support and positive certificate. |
| [Salem family and its local products](#salem-local-review) | [Rank-two estimate and dependence](../../claims/Yin_C_G0483_v1.md#independent-and-dependent-pairs) | The field of an ordered pair, conjugate heights and torsion-dependent pairs. |
| [Salem family and its local products](#salem-local-review) | [Fixed rank-two source](../literature/AM16/Yin_U003.md#am16-u003) | The accepted uniform height bound at fixed rank two over the rational field. |
| [Salem family and its local products](#salem-local-review) | [Compatible fraction](../../claims/Yin_C_G0162_v2.md#statement) | The definition using a fixed prime and one ordered-pair orbit. |
| [Salem family and its local products](#salem-local-review) | [Inertia criterion](../../claims/Yin_C_G0162_v2.md#finite-pool) | Inertia fixes every root whose reduction is distinct from all the others. |
| [Salem family and its local products](#salem-local-review) | [Salem–Boyd comparison](../literature/Hir06/Yin_U001.md#hir06-u001) | The family form and exterior-root mechanism at the source unit's recorded scope. |

<a id="salem-local-review"></a>
## Finding

For both admissible degrees, \(p^j-1\mid d\) for every prescribed residue degree \(j\) and \(p^3\mid d\).
Thus \(z^d-1\) vanishes to order greater than \(\deg H=4\) at every nonzero element of those degrees.
The identity \(S=1+zf(z)(z^d-1)/H\) shows that \(S\) takes value one there, even when \(H\) vanishes.
A repeated root would also annihilate \((zf)'g-(zf)g'\), of degree at most six with constant \(-1\).
This proves squarefreeness and the stated inertia conclusion.
The sum of the logarithms of the \(p^j-1\) contributing to the lcm is bounded by \(K(K+1)\sum_{p\le T}\log p/2\), giving the claimed window for either degree.

In the integral quotient the coefficients at exponents \(0,6,12,\ldots,d\) are one, and the negative coefficients occupy exactly the two disjoint classes \(1,5\bmod 6\) between zero and \(d\).
Both the numerator and \(H\) are anti-reciprocal, hence the quotient is reciprocal.
The strict Rouché perturbation leaves one exterior root at most in the limit, counted with multiplicity.
The signs at each fixed \(s\in(1,\theta)\) and at \(\theta\) give the exterior real root, its strict upper bound and convergence.
For a torsion root of order \(m\), the exponents \(2,m/2+2,m/2+1\) in their three respective parity cases are each prime to \(m\).
The resulting cleared identities for \(G\) are nonzero by their constants in the first and third cases and their linear coefficients in the second case.
Their degrees are at most twelve, so reduction of the putative monic cyclotomic factor at two contradicts the residue-degree bound.
Integrality of the unit factors and reciprocity put the two off-circle roots in the same irreducible factor, and Kronecker's theorem excludes any remaining factor.
Transport to the exterior root excludes equality of like positive powers of distinct conjugates.
Unequal positive powers of conjugates have unequal absolute logarithmic heights.
These facts justify the use of all original labels and the nonvanishing of the rational integral resultants.

On every geometric branch of \(X^a=Y^b\), the first nonconstant exponents of the two rational power series in the parameter agree only if \(b p^{v_p(a)}=a p^{v_p(b)}\).
This criterion also holds in inseparable cases and is equivalent to equality of the prime-to-\(p\) parts.
If it fails, the nonzero elimination polynomial over \(\mathbb F_p\) has degree at most \(6ab\) and cannot vanish at a reduced root.
For a collision of equal \(n\)-th powers the multiplier \(\xi\ne1\) instead gives an equation of degree at most six over \(\mathbb F_p(\xi)\), nonzero at zero.
The extension degree is at most \(n\), giving the needed contradiction.
A root of \(z^n-1\) likewise has degree at most \(n\).

For \(q=p^h\), raising the formal Frobenius congruence with exponent \(q/p\) to the \(p\)-th power lifts it modulo \(p^2\).
In \(\xi G(z^{q/p})^p-G(\xi z^q)\) the coefficient at \(q/p\) is \(\xi p(-1)^{p-1}\), for both signs allowed in the proof.
The unit denominator therefore yields a nonzero \(D/p\bmod p\) of degree at most \(6q\), so \(v(D(\alpha))=1\) at each root \(\alpha\) of \(S\).
The complementary factor \(H\), \(f\), and every nonmatching linear factor are units there.
Consequently the unique matched quotient \(w\) has \(v(w-1)=1\), and \(v(w+1)=1\) at two.
At two the first squaring has depth two and each further squaring gains one.
At odd \(p\) the term \(p(w-1)\) uniquely minimizes the valuation in the binomial expansion at each step.
Prime-to-\(p\) powers preserve depth.
The injectivity already checked gives exactly \(d\) matched pairs, each of depth \(1+v_p(n)\) for the common smaller exponent \(n\).

At a fixed prime the \(d\) Frobenius edges avoid equality and inversion, since either would put a reduced root in \(\mathbb F_{p^2}\).
Multiplicative dependence of a pair of equal positive heights forces \(y=\zeta x^{\pm1}\), and all-power degree preservation reduces these possibilities to precisely the two excluded cases.
On the other orbits the joint degree is the orbit size \(sd\).
The accepted rank-two bound and \(m<\log\theta\) give \(s\gg_\delta d^{(1-2\delta)/(1+2\delta)}\), uniformly in the prime.
Since such an orbit has at most \(d\) edges, this gives the claimed upper bound, while averaging over all \(d(d-2)\) off-pair positions gives the lower bound.
The external height theorem was used at its recorded fixed-rank scope, without a new review of its original proof.

Every \(d\)-th root outside the sixth roots contributes one to the full-turn product.
The six remaining factors are \(1-k,1+3k,1+2k,1+2k,1,1\).
For the half-turn, multiplication of the numerator and denominator evaluations gives the \(W\)-product divided by \(2^4\).
The two traces of \(W\) give one real reciprocal pair with largest root \(\lambda>2\) and a conjugate pair on the circle.
If the latter pair would give \(|1+\gamma^{d_0}|<1\), then \(\Re(\gamma^{d_0})<-1/2\) implies \(\Re(\gamma^{2d_0})>-1/2\).
The chosen degree thus gives \(\log B_d=d\log\lambda+O(1)\) without disturbing any earlier divisibility condition.
At a prime in the prescribed range a common root with \(z^d+1\) would annul the monic quartic \(W\).
This excludes those primes, including two, and \(B_d\le 2^d M(S)^d\) gives the positive certificate.
The stated assertions follow for this family, whose measures approach \(\theta\) from below.
