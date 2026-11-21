---
author: Yin
---

# Critical residues of sections of the quadratic curve

<a id="sieve"></a>
## Residues at the first eight primes

For the [quadratic sections](../Yin_J_G0183/readme.md#census) write \(F(U,V)=A(U)V^2+U^2V+A^*(U)\), \(P(X)=F(X^k,X^\ell)\), with positive coprime \(k,\ell\).
If two integral factors of \(P\) share a nonzero root \(x\) modulo \(p\), the torus point \((u,v)=(x^k,x^\ell)\) satisfies
\[
 F=0,\qquad kU F_U+\ell V F_V=0,\qquad
 J_p=\frac{F(U^p,V^p)-F(U,V)^p}{p}=0 \pmod p.
\]
Indeed the product rule gives the middle equation.
At the Teichmuller lift of \(x\) in the unramified extension with residue field containing \(x\), both factors vanish modulo \(p\), so their product vanishes modulo \(p^2\).
Frobenius preserves that divisibility and sends the Teichmuller coordinates to their \(p\)-th powers, giving the last equation.

The table gives the complete common zero sets over the algebraic closure of each prime field, indexed by the projective slope \([k:\ell]\) modulo \(p\).
An omitted slope has empty zero set.
The final column imposes \(u^\ell=v^k\) on these points.

| Prime | Slope | Torus points | Condition from the section |
| --- | --- | --- | --- |
| 2, 7, 11, 17 | None | Empty | No common residue |
| 3 | \([1:0]\) | \(u^2=-1,\ v=-u\) | \(\ell\equiv3k\pmod4\) |
| 5 | All | \((1,1),(-1,1)\) | The second point requires even \(\ell\) |
| 13 | \([1:0]\) | \((5,4),(8,10)\) | \(9\ell\equiv2k\pmod{12}\) |
| 19 | \([1:1]\) | \(u^2-5u+1=0,\ v=7u+7\) | \(2\ell\equiv k\pmod{20}\) |
| 19 | \([1:-1]\) | \(u^2+5u+1=0,\ v=7u+4\) | \(8\ell\equiv k\pmod{20}\) |

For 3 the element \(u\) has order four and \(v=u^3\).
For 13 the two listed pairs are inverses and the first pair is \((2^9,2^2)\), with 2 of order twelve.
For 19 the two rows give \(u=v^2\) and \(u=v^8\), respectively, with \(v\) of order twenty in both cases.
At 5 both possible coordinates give \(x=\pm1\) by Bezout's identity for \(k,\ell\).
A surviving point satisfies necessary tests for a common residue of two factors; factorization over the rationals remains open beyond the finite census.

<a id="reproduction"></a>
## Reproducing the eight-prime calculation

Run `python mathematics/computations/programs/Yin_J_G0184/critical_digits.py` from the repository root with SymPy 1.14.0.
The program computes \(J_p\) by exact division over the integers and prints the reduced lexicographic Groebner basis for each slope.
The auxiliary equation \(WUV=1\) restricts the calculation to the torus.
For empty cases the program checks that the basis is \(\{1\}\).
For each surviving case it checks that powers of the two displayed point equations belong to the computed ideal and that each original equation vanishes after substitution into the squarefree univariate quotient defining the listed points.
These checks verify both inclusions of geometric supports, including the nonreduced ideals at 5.
