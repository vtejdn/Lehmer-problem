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

<a id="full-squares"></a>
## Complete square divisors in seventeen primitive directions

Take \(\ell=hk+1\) in the following finite ranges with \(h\ge2\).
The table gives all directions for which the [largest square divisor](../../../claims/Yin_C_G0345_v827.md#statement) \(b(\Delta)\) exceeds one, with \(\Delta=|\operatorname{disc}Q|\).
It also gives the full integer \(U\) of that criterion and its refinement \(U_{\rm tr}\) obtained by the [trace-field square test](../../../claims/Yin_C_G0345_v823.md#descent) at good primes.
Among the seventeen directions, the other ten have \(b(\Delta)=U=U_{\rm tr}=1\).
These values include every rational prime, including the exceptional primes and those above 50,000.

| \(k\) | Range of \(h\) checked | \(\ell\) with \(b(\Delta)>1\) | \(b(\Delta)\) | \(U\) | \(U_{\rm tr}\) |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 through 10 | 9, 19 | 25 at both | 25 at both | 25 at both |
| 2 | 2 through 10 | 21 | \(19^2 47^2\) | \(19^2\) | 1 |
| 3 | 2 through 6 | 7 | 9 | 9 | 9 |
| 3 | 2 through 6 | 16 | 25 | 25 | 25 |
| 3 | 2 through 6 | 19 | \(11^2 13^2\) | \(11^2 13^2\) | \(11^2 13^2\) |
| 4 | 2 through 3 | 13 | \(5^2 17^2\) | \(5^2 17^2\) | \(5^2 17^2\) |
| 5 | 2 | None | 1 | 1 | 1 |

For \((2,21)\) the complete square divisor has two prime divisors with different causes.
At 47 the two repeated trace residues have valuation one each, so their contributions to the discriminant combine into a square while neither orbit enters the octic bound.
At 19 there is one trace orbit with valuation two and nonsquare unit, as computed in the [good-prime survey](#trace-survey).
Consequently every reciprocal complementary resultant in this direction has absolute value one even before rational factorization.
The four finite ranges do not give asymptotic control as both \(k\) and \(\ell/k\) grow.

Run `python -B mathematics/computations/programs/Yin_J_G0184/full_squares.py` from the repository root with SymPy 1.14.0.
The [verification program](full_squares.py) reconstructs the exact trace discriminant from the recurrence in the preceding survey and compares it with the product of the supplied factors with multiplicities.
It proves primality of each factor, including a 233-bit factor in direction \((2,19)\).
Below one million it uses trial division through the integer square root.
For a larger candidate \(n\) it recursively certifies distinct primes \(q\) dividing \(n-1\), verifies their powers divide \(n-1\) and uses an integer witness \(a\) for each \(q\) with \(a^{n-1}=1\pmod n\) and \(\gcd(a^{(n-1)/q}-1,n)=1\).
For any prime \(r\mid n\) these conditions force the multiplicative order of the corresponding witness modulo \(r\) to contain the full \(q\)-part of \(n-1\).
Thus the product of the certified powers divides \(r-1\), and as soon as that product exceeds \(\sqrt n\) the integer \(n\) must be prime.
The program uses SymPy factorization of \(n-1\) to obtain candidates for the recursive certificates.
For prime divisors of \(b(\Delta)\) it checks divisibility of the exact exceptional form, and at the remaining primes it verifies every repeated trace orbit and valuation by the same discriminant accounting and lifting as the preceding survey.
