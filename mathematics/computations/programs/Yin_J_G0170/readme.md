---
author: Yin
---

# Rational factors and exterior roots of the cubic family through degree 104

<a id="census"></a>
## Finite census

For every pair of coprime positive integers \(a,b\) with \(3a+b\le104\), factor over \(\mathbb Q\) the monic polynomial
\[
     H_{a,b}(x)=-[g(x^a)+x^b B(x^a)],\qquad
     g(T)=T^3-T-1,\qquad B(T)=1-T^2-T^3.
\]
This tests the [exterior allocation](../../../ledger/Yin_L_G0462_v169.md#partition) for actual irreducible factors of the [Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract).
The core is what remains after all cyclotomic factors are removed with their multiplicities.
The last two columns give degrees of actual nontorsion irreducible factors.

| Domain | Directions | Empty core | One factor | At least two factors, counting multiplicity | Minimum degree | Maximum degree |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(b>3a\) | 552 | 2 | 550 | 0 | 8 | 104 |
| \(b\le3a\) | 556 | 3 | 553 | 0 | 6 | 104 |
| Both | 1,108 | 5 | 1,103 | 0 | 6 | 104 |

The two empty cores for \(b>3a\) occur at \((1,4)\) with orders \(2,18\), and \((1,9)\) with orders \(8,30\).
The other empty cases are \((1,1),(1,2),(2,1)\), with orders \(\{8\},\{2,12\},\{2,6,10\}\), respectively.
In the strict domain the minimum degree 8 occurs at \((1,5)\) and \((1,6)\).
The full-domain minimum 6 occurs at \((1,3)\).
All 1,103 nonempty cores are reciprocal irreducibles having at least one unit-circle root, and every rational factor throughout the census has multiplicity one.
The only cyclotomic orders found are \(2,6,8,10,12,18,30\), consistent with the [classification for primitive directions](../../../ledger/Yin_L_G0462_v172.md#cyclotomic).

<a id="allocation"></a>
## Certified exterior allocations

Every nonempty core for \(b>3a\) has only nonreal exterior roots.
Of these 550 cores, 266 have exactly \(a\) complex-conjugate exterior pairs.
The greatest \(b/a\) among the remaining positive-degree cores is \(61/5\), attained at \((5,61)\).
The following exact counts use the core alone.

| \((a,b)\) | Cyclotomic orders removed | Core degree | Circle roots | Nonreal exterior pairs |
| --- | --- | ---: | ---: | ---: |
| \((5,61)\) | 8 | 72 | 56 | 4 |
| \((8,77)\) | 2 | 100 | 68 | 8 |
| \((5,89)\) | none | 104 | 84 | 5 |
| \((17,53)\) | none | 104 | 64 | 10 |

At \((8,77)\) the degree-50 trace has Sturm variations \(42,42,8,8\) at \(-\infty,-2,2,+\infty\), giving 34 trace roots in \((-2,2)\) and 16 nonreal trace roots.
All eight exterior pairs belong to the single degree-100 rational factor.
At \((5,61)\) the full polynomial has four exterior pairs, since its removed cyclotomic roots all lie on the unit circle.
Consequently a threshold \(r_0\) guaranteeing exactly \(a\) pairs for *every* primitive direction with \(b/a\ge r_0\) must exceed \(61/5\).
The finite census supplies no upper bound on such a threshold and no irreducibility assertion beyond degree 104.

<a id="method"></a>
## Exact factorization, root counts and reproduction

Run the [census program](census.py) from the repository root.
The completed run used Python 3.14.3 and SymPy 1.14.0 with integer coefficient arithmetic.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0170/census.py --workers 4
~~~~

Omit the worker option for serial execution of the same cases.
The program requires no earlier output.
Its replaceable [census.json](../../outputs/Yin_J_G0170/census.json) contains every direction, the cyclotomic orders and multiplicities, and the full descending coefficient list, multiplicity and root signature of each nontorsion factor.
It records four additional Sturm variation counts for each of the four displayed controls.

For each \(1\le a\le34\) the program enumerates \(1\le b\le104-3a\) and tests \(\gcd(a,b)=1\) directly.
The program builds the six signed terms of \(H_{a,b}\) by integer addition, including when exponents coincide.
It applies SymPy's exact polynomial factorization over \(\mathbb Z\) to the original polynomial and checks that the reported factors with multiplicities multiply back to every coefficient.
Monicity gives the rational factorization by Gauss's lemma.
To classify the factors the program constructs every cyclotomic polynomial of degree at most 104, using a totient sieve up to \(2\cdot104^2\), and compares full coefficient lists.
Indeed \(\varphi(m)^2\ge m/2\), since the contribution \(\varphi(q^e)^2/q^e=q^{e-2}(q-1)^2\) is at least one for every prime power except \(q^e=2\), whose contribution is \(1/2\).
Thus classification is exhaustive without assuming the list of seven observed orders.

For a reciprocal noncyclotomic factor \(P\) of degree \(2n\), write \(P(x)=x^n T(x+x^{-1})\).
As in the [earlier trace computation](../Yin_J_G0166/split_traces.py), the program recovers \(T\) using \(S_0=2,S_1=t,S_{j+1}=tS_j-S_{j-1}\), then independently expands the lift by the binomial formula.
The program isolates the real roots of \(T\) in rational intervals with exact arithmetic, refining their positions relative to \(-2,2\) by signs if an interval straddles a cutoff.
A root in \((-2,2)\) lifts to two circle roots, a root below \(-2\) or above \(2\) gives one negative or positive real exterior root, and a conjugate pair of nonreal trace roots gives one nonreal conjugate pair of exterior roots.
The endpoints cannot occur in a noncyclotomic irreducible factor.
For the four displayed controls a separate integer Sturm chain checks the same three real-interval counts by sign variations at \(-\infty,-2,2,+\infty\).
The chain uses pseudo-remainders with the sign of the leading-coefficient power corrected before removing positive content, so each element is a positive multiple of the ordinary signed Sturm remainder.
All factor degrees come from direct rational factorization of the original \(x\)-polynomial, including in the complementary domain.

After generating the census, run the [independent verifier](verify_traces.py) from the repository root.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0170/verify_traces.py
~~~~

It removes cyclotomic factors using their exponent congruences, factors the remaining trace polynomial over the rationals and checks its real roots by Sturm counts.
The [independent review](../../../audits/reviews/Yin_R_G0562_v419.md#finding) verified all 1,108 records, including the complementary domain and the four displayed controls.
