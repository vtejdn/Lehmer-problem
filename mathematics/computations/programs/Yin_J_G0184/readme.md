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

<a id="trace-survey"></a>
## Good-prime trace contacts through 50,000

For \(1\le k\le16\) and \(k<\ell\le100\) with \(\gcd(k,\ell)=1\), the [octic square bound](../../../claims/Yin_C_G0345_v823.md#statement) restricted to the good primes \(p\le50{,}000\) equals one in 902 of the 905 directions with nonzero exceptional form.
In the other three directions it equals \(19^2\), and the [trace-field square test](../../../claims/Yin_C_G0345_v823.md#descent) leaves only \((4,53)\).
There are 906 primitive directions before the exclusion of \((6,7)\), where the exceptional form vanishes.
The following table lists every positive even contact in the range, with its section trace residue \(q=x+x^{-1}\), its valuation \(b\), and a representative of the radicand's unit squareclass in the residue field.

| \((k,\ell)\) | \(p\) | \(q\bmod p\) | \(b\) | Unit in \(\mathbb F_p\) | Two trace branches over \(\mathbb Q_p\) |
| --- | --- | --- | --- | --- | --- |
| \((2,21)\) | 19 | 11 | 2 | 2 | No |
| \((4,53)\) | 19 | 6 | 2 | 9 | Yes |
| \((8,11)\) | 19 | 8 | 2 | 12 | No |

In the first and last rows, the quadratic equation for an orientation has discriminant \(q^2-4\) congruent to 3, a nonsquare modulo 19.
The two trace nonsquares become squares in that quadratic residue extension.
The [rational factor census](../Yin_J_G0183/readme.md#census) proves irreducibility in all three cases, including the one whose trace branches split locally.
The finite survey leaves contributions above 50,000 and at primes of bad reduction undetermined.

Run `python mathematics/computations/programs/Yin_J_G0184/trace_survey.py` with SymPy 1.14.0 from the repository root.
The [survey program](trace_survey.py) tests all 5,133 primes through 50,000 using the exact integer discriminant of the monic trace polynomial \(Q\), where \(P(X)=X^{2k+\ell}Q(X+X^{-1})\).
It constructs \(Q=10C_\ell+C_{2k+\ell}+C_{|2k-\ell|}-7C_{k+\ell}+7C_{|k-\ell|}+1\), using \(C_n(X+X^{-1})=X^n+X^{-n}\).
This follows by expanding \(X^{-2k-\ell}P(X)\) in inverse pairs.
At each good prime a repeated trace residue is a double root: a section endpoint cannot be multiple there since that would give a critical point with \(U=\pm1\), excluded by the [good octic reconstruction](../../../claims/Yin_C_G0345_v812.md#elimination).
Indeed a simple or repeated trace root at an endpoint would make that endpoint multiple in the section.
Away from endpoints the trace parameter has unit derivative in the section coordinate, so each repeated trace orbit of degree \(f\) contributes exactly \(fb\) to \(v_p(\operatorname{disc}Q)\) by the local quadratic equation, and distinct residue disks give unit cross differences.
Thus every positive even contact requires \(p^2\mid\operatorname{disc}Q\).
The program removes primes dividing the exact exceptional form and factors \(\gcd(Q,Q')\bmod p\) at the remaining candidate primes.
For each linear repeated residue it lifts the unique zero \(z\) of \(Q'\) in its disk using the unit \(Q''(z)\), computes \(b=v_p(Q(z))\), and tests the squareclass of \(-2p^{-b}Q(z)/Q''(z)\) when \(b\) is even.
Taylor expansion at \(z\) and a unit square-root change of parameter give this radicand, and twice the valuation of the difference between the two roots recovers the contact \(b\).
A higher-degree repeated factor contributes at least its degree to the discriminant valuation.
In every candidate case the known linear contributions plus these degree lower bounds sum to the exact discriminant valuation, certifying \(b=1\) for every higher-degree repeated factor encountered.
