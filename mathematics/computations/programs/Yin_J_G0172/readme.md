---
author: Yin
---

# Residue orbits of the cubic Frobenius correction at the remaining primes

<a id="orbits"></a>
## Exact finite result

Let \(g=T^3-T-1,\ B=1-T^2-T^3,\ f=-g/B\).
At a prime \(11\le p\le131\), factor over \(\mathbb F_p\) the reduction of the [integral first Frobenius correction](../../../claims/Yin_C_G0345_v387.md#frobenius)
\[
 H_p(T)=\bigl(g(T^p) B(T)^p+(-g(T))^p B(T^p)\bigr)/p .
\]
Retain the distinct irreducible factors other than the divisors of \(TgB\) and of \(\Phi_j\) for \(j=1,2,3,5,8,12,18,30\).
For each coprime positive \(a,b\) satisfying \(\min(a,b)\le\lfloor270/p\rfloor\) and \(\lvert b-3a\rvert\le2858\), sum the degrees of the retained factors for which \(T^b=f(T)^a\) in their residue fields.
Write \(D_p\) for the maximum of this sum over those directions.

| \(D_p\) | Primes |
| ---: | --- |
| 0 | 11, 13, 19, 23, 31, 37, 47, 59, 67, 73, 79, 83, 101, 103 |
| 2 | 71, 97, 107, 109, 127, 131 |
| 4 | 17, 29, 41, 43, 53, 61, 89, 113 |

The eight removed cyclotomic orders refer to the coordinate \(T\).
Their [values on the graph](../../../ledger/Yin_L_G0462_v172.md#cyclotomic) are roots of unity in characteristic zero.
For this range of primes all these orders and their companion coordinates have order prime to \(p\).

<a id="certificate"></a>
## Certificate and reproduction

Run the [program](odd_orbits.py) with Python and python-flint.
The completed computation used Python 3.14.3 and python-flint 0.9.0.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0172/odd_orbits.py
~~~~

The program forms the numerator over the integers, divides by \(p\), and verifies the exact product and its linear coefficient.
It verifies the finite-field factorization by multiplying back with multiplicities.
For each reported factor \(\psi\) of degree \(k\) it verifies \(T^{p^k}=T\bmod\psi\) and \(\gcd(T^{p^{k/r}}-T,\psi)=1\) for every prime \(r\mid k\), which certify irreducibility.
In the residue field it constructs \(f(T)\) by the extended Euclidean algorithm.

Put \(c=\lfloor270/p\rfloor\).
For \(a\le c\), the program stores the first \(c\) powers of \(f(T)\) and compares all powers of \(T\) through \(3c+2858\).
For \(a>c\) it stores the first \(c\) powers of \(T\) and compares all powers of \(f(T)\) through \(\lfloor(2858+c)/3\rfloor\).
Each match uses equality of the full residues, including when some of the short powers coincide.
The final check of the difference, coprimality and case partition ensures each eligible factor contributes its degree once per direction.
The output also gives the number of directions of positive residual degree sum at each prime.

The [independent verifier](verify_gcd.py) computes the Frobenius numerator modulo the square of the prime and uses a polynomial gcd for each direction.
Run it with the same Python environment.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0172/verify_gcd.py
~~~~

Across the 28 primes both methods found the same 454 triples of positive residual degree sum and agreed on the degree sum for every triple.
