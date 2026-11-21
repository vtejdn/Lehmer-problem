---
author: Yin
---

# Rational factors and exterior roots of sections of a quadratic curve

<a id="census"></a>
## Factorization over the rationals

Write \(A(U)=(U^2-3U-1)(U^2-4U-1)\) and \(A^*(U)=U^4A(1/U)\).
For positive coprime \(k<\ell\) take
\[
 P_{k,\ell}(X)=X^{2\ell}A(X^k)+X^{\ell+2k}+A^*(X^k).
\]
This tests the search for a factor with two exterior conjugates on the [quadratic curve](../../../claims/Yin_C_G0345_v789.md#example) of the [Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract).

Every one of the 2,286 directions with \(4k+2\ell\le300\) and each additional direction \((k,k^2+1)\) for \(k=13,17,19,23,29,31\) gives an irreducible polynomial over \(\mathbb Q\).
For \(k>1\) the smallest observed number of roots of modulus greater than one is four.
There is no factor with just two exterior conjugates for \(k>1\) in these 2,292 tests.

| Range | Directions | Exterior roots |
| --- | ---: | --- |
| Complete triangle \(4k+2\ell\le300\) | 2,286 | \(2k\) in 2,260 cases and \(2k-2\) in 26 cases. |
| Six additional directions \(\ell=k^2+1\) | 6 | \(2k\) in each case, including two positive real roots and no negative real roots. |

The first deficit in order of increasing \(k\) is at \((23,24)\), with 44 exterior roots.
Among the 26 deficits the largest \(\ell/k\) is \(44/39\).
At the largest degree in the census, \(P_{31,962}\) has degree 2,048 and has 62 exterior roots.
A separate evaluation of `direction((40,1601))` in the [census program](sections.py) gave an irreducible polynomial of degree 3,362 with 80 exterior roots.
These finite irreducibility computations leave open whether proper factors occur outside the tested directions.

<a id="torsion"></a>
## Exact exclusion of torsion points

With \(U=e^{iu}\), \(V=e^{iv}\) and \(t=2\sin u\), the curve equation on the unit torus gives
\[
  2(12-t^2)\cos v+14t\sin v+1=0.
\]
If \(U,V\) are roots of unity and \(V\) has order \(b\), apply an embedding of the common cyclotomic field taking \(V\) to \(e^{2\pi i/b}\).
For \(b\ge12\) the left side is at least \(16\cos(\pi/6)-28\sin(\pi/6)+1=8\sqrt3-13>0\).
For \(1\le b\le11\) the remaining check uses \(R_b(U)=\operatorname {Res}_V(A(U)V^2+U^2V+A^*(U),\Phi_b(V))\).

A primitive \(m\)-th root among its zeros would give \(\varphi(m)\le d=\deg R_b\), hence \(m\le2d^2\).
Indeed \(\varphi(p^a)^2/p^a=p^{a-2}(p-1)^2\) is at least one except at \(p^a=2\), where it equals \(1/2\).
Put \(M_d=\operatorname{lcm}\{m\le2d^2:\varphi(m)\le d\}\).
At the listed prime \(p\), the nonzero reduction of \(R_b\) is relatively prime to \(U^{M_d}-1\).
A common monic cyclotomic divisor over the integers would retain its positive degree after reduction, so these checks exclude every remaining order and give no torsion point on the curve.

| \(b\) | \(d\) | \(M_d\) | \(p\) |
| ---: | ---: | ---: | ---: |
| 1 | 4 | 120 | 2 |
| 2 | 4 | 120 | 2 |
| 3 | 8 | 5040 | 17 |
| 4 | 6 | 2520 | 2 |
| 5 | 16 | 24504480 | 17 |
| 6 | 8 | 5040 | 5 |
| 7 | 24 | 160626866400 | 3 |
| 8 | 16 | 24504480 | 2 |
| 9 | 24 | 160626866400 | 5 |
| 10 | 16 | 24504480 | 17 |
| 11 | 40 | 438120379479182400 | 3 |

<a id="method"></a>
## Reproduction and checks

The [census program](sections.py) uses python-flint 0.9.0 to factor each integer polynomial and checks reconstruction with multiplicities.
For each reciprocal irreducible factor of degree \(2h\) it computes its trace \(T\), given by \(P(X)=X^hT(X+X^{-1})\), by the centered Chebyshev recurrence.
The integer Sturm chain of \(T\) takes negative rational remainders and removes only positive scalars.
Its sign variations at \(-\infty,-2,2,+\infty\) give the negative real exterior, circle, positive real exterior and nonreal exterior counts separately.
Each trace root in \((-2,2)\) gives two circle roots, each real trace outside the interval gives one exterior root, and each nonreal conjugate pair gives two exterior roots.

The [trace and torsion checks](check.py) independently build the trace from the five terms of \(A\) and the central monomial.
For each prime through 43 the degrees of possible monic rational factors must be subset sums of the modular factor degrees counted with multiplicities.
Intersecting these sets leaves no degree from one to half the trace degree in all 2,292 cases.
An exact sign change supplies a real trace root in \((-2,2)\), at whose real embedding \(t^2-4<0\).
The quadratic \(X^2-tX+1\) is then irreducible over the trace field.
Thus every trace has an irreducible reciprocal lift of twice its degree.
The checker also verifies that each stated direction occurs once, reconstructs each recorded polynomial and counts the trace roots again with SymPy for \((1,2),(7,19),(23,24)\).
The two implementations were run by the same researcher.
The torsion check computes the eleven integer resultants with SymPy 1.14.0 and the modular powers and gcds with python-flint.

The following commands run from the repository root with Python 3.14.3 and the two libraries installed.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0183/sections.py --degree 300 --workers 4 --extra 13,170 17,290 19,362 23,530 29,842 31,962
python mathematics/computations/programs/Yin_J_G0183/check.py
python mathematics/computations/programs/Yin_J_G0183/check.py --torsion
~~~~

The first command regenerates every pair, factor coefficient list in ascending degree, multiplicity and signature in the local output `mathematics/computations/outputs/Yin_J_G0183/census.json`.
The second command checks that output, and the third independently reproduces the torsion certificate from the displayed parent and parameters.

<a id="modular-degrees"></a>
## Modular factor degrees and integer values on the quadratic diagonal

Put \(C_j(X+X^{-1})=X^j+X^{-j}\) and \(n=\ell+2k\).
The identity \(P_{k,\ell}(X)=X^nQ_{k,\ell}(X+X^{-1})\) gives the monic trace polynomial
\[
 Q_{k,\ell}=1+C_{\ell+2k}+C_{|\ell-2k|}+10C_\ell-7C_{\ell+k}+7C_{|\ell-k|}.
\]
If this polynomial is reducible over \(\mathbb Q\), Gauss's lemma gives a monic integer factor \(H\) of degree \(1\le d\le\lfloor n/2\rfloor\).
At every prime \(p\), the reduction of \(H\) retains degree \(d\) and is a product of monic irreducible factors of \(Q_{k,\ell}\bmod p\), with each multiplicity bounded by the one in the reduction.
For each integer \(a\) with \(Q_{k,\ell}(a)\ne0\), the value \(H(a)\) is also a signed divisor of \(Q_{k,\ell}(a)\).
We intersect the allowed degrees across primes, first using subset sums with multiplicities, then retaining only degrees of products whose evaluations pass the signed-divisor tests simultaneously at \(-2,-1,0,1,2\).
The [program](modular_degrees.py) skips the evaluation refinement at a prime when the reduction has more than 16,384 monic divisors, including the two improper divisors.
It builds the traces by \(C_{2j}=C_j^2-2\) and \(C_{2j+1}=C_j C_{j+1}-C_1\), starting from \(C_0=2\) and \(C_1=t\).

For example, at \((k,\ell)=(4,53)\), the six distinct factors modulo 19 have the following values in \(\mathbb F_{19}\).

| Degree | Multiplicity | Value at \(-2\) | Value at \(-1\) | Value at \(0\) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 8 | 9 | 10 |
| 1 | 2 | 11 | 12 | 13 |
| 2 | 1 | 7 | 2 | 18 |
| 8 | 1 | 11 | 2 | 17 |
| 13 | 1 | 6 | 3 | 4 |
| 35 | 1 | 7 | 18 | 7 |

The integer trace values at these three points are \(-23,-29,1\), respectively.
Of the 47 monic modular divisors of degrees 1 through 30, exactly 15 meet the first value restriction, three meet the first two, and none meet all three.
Thus this single reduction proves trace irreducibility even though it has six distinct factors.

For \(\ell\ge2k\), the [circle-root theorem](../../../claims/Yin_C_G0345_v793.md#statement) supplies \(2\ell\) simple circle roots of \(P_{k,\ell}\), all nontorsion.
Choose one, \(z\), and put \(t=z+z^{-1}\).
Since \(z\ne\pm1\), the trace \(t\) belongs to \((-2,2)\) and \(t^2-4<0\) in the real field \(\mathbb Q(t)\).
Consequently \(X^2-tX+1\) is irreducible over this field.
When \(Q_{k,\ell}\) is irreducible, \([\mathbb Q(z):\mathbb Q]=2n=\deg P_{k,\ell}\), proving irreducibility of the whole section.

For every \(1\le k\le128\) with \(\ell=k^2+1\), the modular tests exclude all proper factor degrees up to \(\lfloor (k+1)^2/2\rfloor\).
All 128 whole sections are therefore irreducible over \(\mathbb Q\), and each has exactly \(2k\) exterior roots.
The last section, \(P_{128,16385}\), has degree 33,282 and 256 exterior roots.
No assertion beyond these 128 indices follows from the census.

| Primes used, in the order \(19,3,5,7,11\) | Sections first certified |
| ---: | ---: |
| 1 | 94 |
| 2 | 25 |
| 3 | 7 |
| 4 | 1 |
| 5 | 1 |

Only \(k=57\) first terminates at 7, and only \(k=91\) first terminates at 11.
The following commands reproduce the example and the complete diagonal using python-flint 0.9.0.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0183/modular_degrees.py --example
python -B mathematics/computations/programs/Yin_J_G0183/modular_degrees.py --first 1 --last 128 --workers 4
~~~~

<a id="modular-361"></a>
## A degree-262088 section on the quadratic diagonal

For \(k=19^2=361\) and \(\ell=k^2+1=130322\), the trace \(Q\) has degree \(131044\).
The irreducible factor degrees modulo 19, all with multiplicity one, are
\[
 1,3,5,8,89,625,869,1285,1604,4696,10128,10292,13217,25203,27274,35745.
\]
Modulo three the distinct factor degrees are \(1,24,298,2975,5327,6874,115545\), again with multiplicity one.
The six smaller factors at three give 63 nonempty subset sums in the range \(1\) through \(65522\).
Exactly nine monic divisors modulo 19 have degrees in that set.
The [certificate program](diagonal_361.py) stores the two evaluations of each individual monic factor modulo 19 and gives the following products.

| Degree | Value at \(-2\) modulo 19 | Value at \(-1\) modulo 19 |
| ---: | ---: | ---: |
| 1 | 10 | 11 |
| 5327 | 15 | 9 |
| 7172 | 4 | 10 |
| 7173 | 2 | 15 |
| 8302 | 5 | 2 |
| 8303 | 12 | 3 |
| 12202 | 18 | 7 |
| 12524 | 4 | 5 |
| 15474 | 16 | 2 |

A monic integer factor evaluated at \(-2\) must divide \(Q(-2)=25\).
Only degrees \(8302\) and \(12202\) pass, with respective residues 5 and 18.
At \(-1\) their residues 2 and 7 both fail to represent a signed divisor of \(Q(-1)=-29\).
Thus \(Q\) is irreducible over the rationals.
The [circle-root argument](#modular-degrees) proves that the whole section of degree \(262088\) is irreducible and has exactly \(722\) exterior roots.
This adds one tested index beyond the consecutive range through \(128\).

Run the first command to check all subset sums and evaluations from the recorded factor data.
The second recomputes the two finite-field factorizations and checks their products and recorded rows using python-flint 0.9.0.

~~~~powershell
python -B mathematics/computations/programs/Yin_J_G0183/diagonal_361.py
python -B mathematics/computations/programs/Yin_J_G0183/diagonal_361.py --refactor --threads 4
~~~~
