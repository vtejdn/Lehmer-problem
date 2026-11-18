---
author: Yin
---

# Dyadic square classes for all primitive cubic directions

<a id="classification"></a>
## Square classes and dyadic towers

Put \(g(T)=T^3-T-1\), \(B(T)=1-T^2-T^3\), \(f=-g/B\) and \(A(X)=g(X^a)+X^bB(X^a)\) for coprime positive \(a,b\).
For every nontorsion root \(\alpha\) of \(A\), both \(\alpha\) and \(-\alpha\) are nonsquares in \(\mathbb Q(\alpha)\).
Consequently, if \(P\) is the monic minimal polynomial of \(\alpha\), the polynomial \(P(X^{2^k})\) is irreducible of degree \(2^k\deg P\) and logarithmic Mahler measure \(m(P)\) for every \(k\ge0\), by the [norm induction](../../../ledger/Yin_L_G0462_v164.md#all-towers).

We use the [multiple-residue exclusions](../../../ledger/Yin_L_G0462_v172.md#dyadic) and [Frobenius and height bounds](../../../ledger/Yin_L_G0462_v172.md#frobenius).
If \(\epsilon\alpha\) is a square for \(\epsilon=\pm1\), every root \(x\) of \(\overline P\) is a simple root of \(\overline A\) in characteristic two.
The coordinate \(t=x^a\) satisfies \((H_{\epsilon^a,\epsilon^b}/2)(t)=0\bmod2\), in the notation of the [cyclotomic calculation](../../../ledger/Yin_L_G0462_v172.md#cyclotomic).
The two values \(t,f(t)=x^b\) determine \(x\) by Bézout's identity for \(a,b\).

<a id="negative"></a>
## The negative square class

For \(\epsilon=-1\), the following table gives the possible orders of \(t\) from that Frobenius calculation.
Each row lists the corresponding values of \(x^b=f(t)\) in the same order, by reducing the cyclotomic identities in characteristic two.
Because each value is a power of \(t\), one has \(\langle x\rangle=\langle t\rangle\), so \(x\) has the same order \(j\) and \(a\) is invertible modulo \(j\).

| Parity of \((a,b)\) | \(j\) | \(f(t)\) | Cyclotomic factors of \(A\) supplying the respective residues |
| --- | --- | --- | --- |
| even, odd | \(1,3,5\) | \(1,t^2,t^3\) | \(\Phi_2,\Phi_6,\Phi_{10}\) |
| odd, even | \(1,9\) | \(1,t^4\) | \(\Phi_2,\Phi_{18}\) |
| odd, odd | \(3,15\) | \(t^2,t^9\) | no factor asserted for \(3\), and \(\Phi_{30}\) for \(15\) |

For each listed cyclotomic factor, \(x^b=t^s\) gives \(b\equiv sa\bmod j\), and adjoining the displayed parity gives the exact congruence in the cyclotomic table for \(\Phi_{2j}\).
Its reduction contains every root of order \(j\), so simplicity excludes any such root in a nontorsion factor.
The only remaining possibility has both exponents odd, \(b\equiv2a\bmod3\), and \(\overline P=X^2+X+1\).
In this case \(\deg P=2\), and the square of a unit has norm \(+1\), so \(\mathrm N(\alpha)=\mathrm N(-\alpha)=1\).
A nontorsion quadratic unit of norm one has integral trace of absolute value at least three and Mahler measure at least \((3+\sqrt5)/2\).
Here the six signed monomials of \(A\) have distinct exponents, since coincidences require \(b=a\) or \(b=3a\), both excluded by primitivity and \(b\equiv2a\bmod3\).
The coefficient norm bound \(M(P)\le M(A)\le\|A\|_2=\sqrt6\) rules out this last case.

<a id="positive"></a>
## The only possible residue for a positive square

For \(\epsilon=1\), each \(t\) is a zero of the Lehmer polynomial modulo two.
Its two factors are \(T^5+T^3+T^2+T+1\) and its reciprocal.
In the quotient by the first, \(T\) has order \(31\) and \(f(T)=T^{23}\), as direct binary polynomial arithmetic verifies.
The \(31\) distinct nonzero powers together with zero fill this quotient, which proves it is a field.
Since \(f(T^{-1})=f(T)^{-1}\), the same exponent applies to the reciprocal factor.
Thus \(x\) too has order \(31\), and \(b\equiv23a\bmod31\).
The possible \(x\)'s form two distinct reciprocal Frobenius orbits of length five, obtained by raising the ten \(t\)'s to \(a^{-1}\bmod31\).

In either possible degree, a positive square requires an integral monic reciprocal divisor \(D\) of \(A\) of degree ten containing both orbits after reduction.
Indeed, \(-A\) is monic reciprocal of constant one.
If \(\overline P\) contains one orbit, \(P\) and its distinct monic reciprocal have product \(D\).
If it contains both, a distinct monic reciprocal would repeat simple roots in \(\overline A\), so \(P\) equals its monic reciprocal.
Its constant term is \(+1\), since an anti-reciprocal factor would vanish at one.
In both cases \(D(1)\) is odd and divides \(A(1)=-2\), hence equals \(\pm1\).

<a id="enumeration"></a>
## Exact test of the finite range

The height bounds restrict \(1\le a\le437\) and \(-218\le b-3a\le218\).
Within these inclusive ranges, \(b>0\), coprimality and the order-\(31\) congruence leave **3,468** pairs.
For each, the required \(\overline D\) is \(\gcd(X^{31}-1,\overline L(X^a))\) over \(\mathbb F_2\), where \(L\) is the Lehmer polynomial.
Its simple roots in \(\overline A\) determine a unique monic factor lift at each power of two.
For a current monic \(D_m\) modulo \(m=2^n\), let \(E=(A\bmod D_m)/m\bmod2\), computed by monic division modulo \(2m\) and coefficientwise division by \(m\).
Writing \(A=D_m Q+mE\bmod 2m\) shows that the next lift is \(D_m+mU\), where \(U=E\overline D'/\overline A'\bmod\overline D\) has degree below ten.
Indeed \(\overline Q\,\overline D'=\overline A'\bmod\overline D\), and both derivatives are units there.

At each of the moduli \(4,8,\ldots,2048\), retain the lift only if its value at one equals \(1\) or \(-1\) modulo that modulus.
The respective counts were \(3468,3468,1848,967,510,290,145,78,37,15\).
Every coefficient of a possible \(D\) has absolute value at most \(\binom{10}{5}M(D)\le252\sqrt8<1024\), by expanding the elementary symmetric polynomials in its roots.
Here \(M(D)\le M(A)\le\|A\|_2\le\sqrt8\), including the collisions \(b=a,3a\).
Centering the coefficients of the final lifts modulo \(2048\) therefore recovers every possible \(D\) exactly.
Ordinary integer polynomial division found **zero** divisors among all fifteen candidates, completing the positive square exclusion.

The [verifier](squares.py) uses Python 3 and its standard library, with binary polynomial arithmetic, monic reduction modulo powers of two, and integer long division.
It also recovers the signed Lehmer polynomial from its product with \(X+1\) and rejects exact divisibility after adding \(2048\) to that product.
From the repository root, run the following command to reproduce the counts and exact divisor list on standard output.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0169/squares.py
~~~~
