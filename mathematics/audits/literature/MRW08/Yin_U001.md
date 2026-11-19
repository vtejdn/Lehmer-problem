---
author: Yin
---

<a id="mrw08-u001"></a>
<a id="degree"></a>
# A polynomial of measure strictly between one and Lehmer's has degree at least 56

Use the [November 2007 author manuscript](readme.md#edition).
Its p. 2 identifies \(\rho=M(X^{10}+X^9-X^7-X^6-X^5-X^4-X^3+X+1)\) as the unique exterior root of that polynomial.
The first assertion of Theorem 1 on p. 3 states that every \(P\in\mathbb Z[X]\) with \(1<M(P)<\rho\) has \(\deg P\ge56\).
The inequalities are strict and \(M\) is the multiplicative Mahler measure.
The degree-ten polynomial attains the endpoint \(\rho\). [Theorem 1](../../../literature/pdf/MRW08--author.pdf#page=3)

Coyston's thesis cites this paper as reference 27 on p. 254 and describes the verification as extending through degree 56 on p. 24.
The primary theorem's lower bound \(\deg P\ge56\) leaves degree 56 open, and Table 1 ends at degree 54.
At the [prime-223 frontier](../../../ledger/Yin_L_G0462_v264.md#frontier), both remaining degree pairs contain 56, so treating the secondary wording as an inclusive degree bound would discard both cases. [Coyston, p. 24](../../../literature/pdf/Coy22--thesis.pdf#page=24) · [Mossinghoff, Rhin and Wu, Theorem 1](../../../literature/pdf/MRW08--author.pdf#page=3)

The theorem's second assertion identifies per-degree lower bounds for irreducible noncyclotomic polynomials at each even degree from 8 through 54, under the authors' additional primitivity condition.
Their definition on pp. 2–3 requires that the polynomial cannot be written as \(S(X^k)\) for any \(k\ge2\).
Table 1 specifies the minimizers by coefficients up to the reciprocal symmetry and gives their multiplicative measures numerically.
For an irreducible polynomial \(P(X)=S(X^k)\), \(S\) is irreducible by substitution into any putative factorization, and the root product gives \(M(S)=M(P)\).
Iterating reduces the degree until the no-substitution condition holds.
The general first assertion of Theorem 1 already includes all such substitutions. [Definition and table](../../../literature/pdf/MRW08--author.pdf#page=2)

Section 3 distinguishes verification of the per-degree minima from enumeration of all such polynomials below \(1.3\).
The latter list is exhaustive through degree 44, using earlier results and the searches at degrees 42 and 44.
The authors also report additional examples beyond degree 44.
I checked both assertions of Theorem 1, the coefficient and measure columns in Table 1, and the scope of the two searches against §3 and its Tables 2–3.
I use the published computational theorem at statement scope and did not rerun its coefficient enumeration or verify its long numerical search independently. [Computations and scope](../../../literature/pdf/MRW08--author.pdf#page=9)
