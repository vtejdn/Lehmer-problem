---
author: Yin
---

# Irreducibility at simultaneous splitting primes for the equal blocks 2 and 3

## Question and scope

For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), determine the irreducible factors at fixed simultaneous splitting delays by testing modular degrees of the reciprocal trace.
Write \(n=q-g\) and
\[
  P_\varepsilon(X)=X^{q-g}(X^g-2)(X^g-3)
                  +\varepsilon(1-2X^g)(1-3X^g),\qquad \varepsilon=\pm1.
\]
Each prime \(q\) below satisfies \(g\mid(q-1)/\operatorname{ord}_q(\ell)\) for both \(\ell=2,3\), the [simultaneous splitting condition](../../../claims/Yin_C_G0345_v211.md#limits).
The [torsion classification](../../../claims/Yin_C_G0345_v212.md#torsion) gives precisely the linear cyclotomic factors at these inputs, since \(q\) is odd, prime to \(g\), and \(q>7g\).
The finite irreducibility test needs no estimate involving the unspecified constant in the ninth-power delay range.

## Files and reproduction

Run the [deterministic verifier](split_traces.py) from the repository root with Python 3.10 or later and its standard library.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0166/split_traces.py
~~~~

The program constructs all ten polynomials directly from \(g,q,\varepsilon\), performs trial division to verify primality of \(q\), and computes the two multiplicative orders.
Its replaceable [certificates.json](../../outputs/Yin_J_G0166/certificates.json) records all modular degree counts with multiplicity, the candidate degrees remaining after each prime, and a rational sign-change interval for each trace.
No earlier generated file is an input.

## Why the degree counts decide irreducibility

After exact monic division by every prescribed linear factor, write the reciprocal quotient as \(H(X)=X^m T(X+X^{-1})\).
The recurrence for \(X^j+X^{-j}\) computes the monic integral \(T\), and an independent binomial expansion checks every coefficient of the lift against \(H\).
At an auxiliary prime \(p\), the program obtains the factor degrees of \(T\bmod p\) by successive greatest common divisors with \(X^{p^j}-X\).
This latter polynomial is squarefree and contains precisely the monic irreducibles over \(\mathbb F_p\) whose degrees divide \(j\), since its roots form \(\mathbb F_{p^j}\).
After all lower degrees have been removed, the gcd at step \(j\) therefore selects exactly the remaining degree-\(j\) factors.
Taking repeated gcds with this squarefree product and dividing restores their multiplicities.
Once the remaining degree is less than \(2j\) at the start of a step, a nonconstant remainder can contain only a single irreducible factor.

A monic integral factor preserving its degree modulo every \(p\) must have a degree expressible as a subset sum of each modular multiset.
For a reducible \(T\) there is such a degree between one and \(\lfloor m/2\rfloor\), by monic factorization over the integers.
The program intersects these sets and verifies the intersection is empty.
Finally it exhibits a strict sign change of \(T\) at two rationals in \((-2,2)\).
For an intervening real root \(t\), the field \(\mathbb Q(t)\) is real but the roots of \(X^2-tX+1\) are nonreal.
Adjoining either root thus doubles the degree, and its minimal polynomial has the full degree \(2m\) of \(H\).

<a id="finite-results"></a>
## Results and limits

For both signs at all five pairs the noncyclotomic quotient is irreducible over \(\mathbb Q\).
The orders and resulting degrees are

| \(g\) | \(q\) | \(\operatorname{ord}_q(2)\) | \(\operatorname{ord}_q(3)\) | \(\deg H_-\) | \(\deg H_+\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 307 | 102 | 34 | 308 | 310 |
| 4 | 577 | 144 | 48 | 580 | 580 |
| 5 | 431 | 43 | 43 | 434 | 436 |
| 8 | 601 | 25 | 75 | 608 | 608 |
| 10 | 431 | 43 | 43 | 440 | 440 |

For example, at \(g=8,q=601\) the degree-304 trace of the positive-sign quotient has modular degree multisets \(1^4,25^{12}\) and \(4,75^4\) at 2 and 3, respectively, with exponents denoting counts.
These leave the smaller candidate degrees \(4,75,79,150\).
The degrees \(1,3,3,5,42,250\) at 7 leave just 4, and \(1,2,7,294\) at 11 exclude 4 as well.
This demonstrates why two multiplicative orders on the splitting family can leave apparent factorizations that a different reduction eliminates.
The ten complete finite checks give no bound on the degrees or measures of individual factors for unbounded \(g,q\).
