---
author: Yin
---

# Review of the full reciprocal shell at conductors 13, 17 and 19

<a id="shell-census-review"></a>
## Independent finding on the finite census

At 2026-11-08T03:20 UTC, a reviewing agent for Yin checked the [J147 census](../../computations/programs/Yin_J_G0147/readme.md#whole-shell) independently of its development.
The initial inspection used the fixed mathematical description, its programs and their cited dependencies, without development discussion or previous review conclusions.
The height-free enumeration, strict classifications and chamber counts hold for the three specified degrees.

### Coverage and exact arithmetic

An exterior root and its partner \(1/\bar\alpha\) have the same argument.
Their contribution to the difference between the real Newton sum and the angular sum has absolute value at most \(2\cosh(k\log|\alpha|)-2\).
Superadditivity on the nonnegative half-line bounds the total error by \(E_k=(6/5)^k+(5/6)^k-2\).
Summing the squared geometric sum at the five specified phases gives the stated Fejér inequalities because conjugate angles cancel the sine terms.
The integer part of each error allowance therefore preserves every input with \(M\le6/5\).
I checked the five projection arrays, the prefix endpoints obtained by solving Newton's identity for each next integer coefficient, the reflection at the central coefficient, and the Newton recurrence on both sides of the degree in the tail.
Each monic reciprocal polynomial has exactly one free prefix.

The common denominator \(30^{32}\) gives the stated floors exactly.
Using the coefficient majorant \(\binom{35}{10}=183579396\) and \(20+\lfloor E_{32}\rfloor=359\), the absolute terms of any Newton step sum to at most \(20\cdot183579396\cdot360<2^{41}\).
This bounds the intermediate integer operations as well as the final sum.
The prefix denominators are at most ten and the final Fejér weights have absolute value one or two, so binary division cannot round a noninteger across either endpoint.

For the neutral count I independently multiplied the degree generating series for the two squared linear factors and one factor \((1-x^{\varphi(h)})^{-1}\) for each allowed cyclotomic order \(h\ge3\).
Unique factorization and Kronecker's theorem identify its degree-\(D\) coefficient with the number of neutral polynomials, including multiplicities.
This gives \(2257,10133,20399\) at degrees \(14,18,20\).
For the other inputs I checked the two rational endpoint exclusions and the coefficient lower bound and Parseval–Jensen upper bound after exact root squaring, including the integer cross multiplication in both strict tests.

Rerunning the supplied command for all three degrees classified every survivor and reproduced these counts of distinct whole polynomials.

| \(D\) | Newton survivors | Survivors with \(M>6/5\) | \(1<M<6/5\) | Strict chamber | Strict chamber with unit resultant |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 14 | 2955 | 660 | 38 | 0 | 0 |
| 18 | 21726 | 11261 | 332 | 0 | 0 |
| 20 | 64799 | 43550 | 850 | 1 | 0 |

### Residues, the unique input and the two laws

For each strict candidate I checked the program's rejection of a shared pole or a failed left endpoint and its rational interval test of \(Q(b)\).
In increasing order the derivative of the monic \(B\) alternates in sign and is positive at the last pole.
Sorting the signs and requiring both values tests exactly the specified negative block followed by a positive block.
Euclidean division of each monic \(Q\) by \(B\) has integer quotient \(t-a\) and remainder \(C\) of degree below \(\deg B\).
The determinant of multiplication by \(C\) on \(\mathbb Z[t]/B\) is \(\operatorname{Res}(B,Q)\), so the last column includes every unit and every integer shift at these three conductors.

I reconstructed the recorded degree-20 vector and independently obtained \(B(-2)=-1\), \(Q(-2)=4\), \(P(-1)=4\), and multiplication determinant \(-4313=-19\cdot227\).
On the rational grid of spacing \(1/100\) in \([-2,2]\), nine sign changes of \(B\) isolate its nine roots.
Sturm counts exclude a zero of \(Q\) in each isolating interval.
The signs of \(Q\) and of \(B\) at the right ends give the ordered residue signs \((-,+,+,+,+,+,+,+,+)\).

The stated degree-nine trace core \(H=Q/(t-2)\) has Sturm variation counts \(9,1,0\) at \(-2,2,+\infty\), and \(H(-2)=H(2)=-1\).
For \(\bar H\) modulo two I also checked \(t^{512}\equiv t\pmod{\bar H}\) and \(\gcd(\bar H,t^8-t)=1\), which establish irreducibility in degree nine.
An embedding sending a root \(u\) of \(H\) into \((-2,2)\) sends \(u^2-4\) to a negative number, so its quadratic lift is irreducible over the totally real field \(\mathbb Q(u)\).
Thus \(P=(z-1)^2S\) has one exterior root in the irreducible degree-18 factor \(S\).
I obtained \(S(118836814/10^8)<0<S(118836815/10^8)\), verifying the recorded interval for the whole measure.

All ten free coordinates of the unique prefix lie in \(\{-4,\ldots,4\}\), so the joint chamber-and-shell event under the independent uniform coefficient law has mass \(9^{-10}\).
The second law gives equal mass to all 850 distinct degree-20 strict-shell polynomials and therefore gives the chamber mass \(1/850\).
The reviewed construction gives a single real exterior root at this fixed radius.
Further conductors, arbitrarily small positive shells and a required nonreal exceptional pair remain outside the finite result.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite census](#shell-census-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite census](#shell-census-review) | [Finite census statement](../../computations/programs/Yin_J_G0147/readme.md#whole-shell) | All table counts, height-free coverage and unit scope at the three stated conductors. |
| [Finite census](#shell-census-review) | [Unique input](../../computations/programs/Yin_J_G0147/readme.md#unique-input) | Witness, signed chamber, factorization, whole measure and the two specified probability laws. |
| [Finite census](#shell-census-review) | [Newton cover](../../computations/programs/Yin_J_G0147/readme.md#newton-cover) | Moment and Fejér bounds, exhaustion and arithmetic precision. |
| [Finite census](#shell-census-review) | [Classification](../../computations/programs/Yin_J_G0147/readme.md#measure-and-chamber) | Kronecker neutral enumeration, strict measure bounds and exact chamber tests. |
| [Finite census](#shell-census-review) | [Replay](../../computations/programs/Yin_J_G0147/readme.md#replay) | Complete replay at degrees 14, 18 and 20. |
| [Finite census](#shell-census-review) | [Newton program](../../computations/programs/Yin_J_G0147/newton.cjs) | Exact allowance and prefix arithmetic, reciprocal completion and all 32 moment tests. |
| [Finite census](#shell-census-review) | [Census program](../../computations/programs/Yin_J_G0147/census.py) | Neutral products, strict classifications, residues and checks on the unique witness. |
| [Finite census](#shell-census-review) | [Root-squaring dependency](../../computations/programs/Yin_J_G0144/pilot.py) | The imported integer Graeffe map on monic reciprocal even-degree inputs. |
