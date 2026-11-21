---
author: Yin
---

# Excluding third, fifth and seventh powers throughout the primitive cubic family

<a id="classification"></a>
## The three small odd primes

Put \(g(T)=T^3-T-1,\ B(T)=1-T^2-T^3,\ f=-g/B\).
For coprime positive integers \(a,b\), let \(\alpha\) be a nontorsion root of \(A(X)=g(X^a)+X^bB(X^a)\) and \(K=\mathbb Q(\alpha)\).
Then \(\alpha\notin K^p\) for \(p=3,5,7\), for every primitive direction \((a,b)\).
The calculation uses the [first Frobenius correction](../../../claims/Yin_C_G0345_v387.md#frobenius) at the simple residues and at some nonsimple residues.
The resulting degree bound makes a separate finite calculation for reciprocal polynomials of degree at most six sufficient.

<a id="ramification"></a>
## A local test including nonsimple residues

Suppose \(\alpha=\gamma^p\) in \(K\), and write \(d=[K:\mathbb Q]\).
Then \(\gamma\) is an algebraic integer unit with \(\mathbb Q(\gamma)=K\).
Fix a prime in the splitting field above \(p\) and take any conjugate of \(\alpha\) there, writing \(x=\bar\alpha\), \(t=x^a\).
Write \(m_x\) for the multiplicity of \(x\) in the reduction of the entire monic parent \(-A\).
If \(\mathbb Q_p(\alpha)\) has ramification index \(e\) and residue degree \(h\), the degree \(k\) of \(x\) over \(\mathbb F_p\) divides \(h\).
The local minimal polynomial has degree \(eh\), and all reductions of its roots are conjugate to \(x\), since the local Galois group acts on the residue field by powers of Frobenius.
Its reduction therefore contributes \(eh/k\) copies of each root of that residue orbit.
In particular \(e\le m_x\).

Write \(F(U,V)=g(U)+VB(U)\), \(u=\gamma^a,\ v=\gamma^b\).
The exact equality \(F(u^p,v^p)=0\) gives \(\overline{F(u,v)}=0\).
Since \(u,v\in\mathbb Q_p(\alpha)\), this forces \(v_p(F(u,v))\ge1/e\), with \(v_p(p)=1\).
If \(m_x<p\), then \(p/e>1\), so \((F(u^p,v^p)-F(u,v)^p)/p\) vanishes modulo the prime at this point.
The Bézout identity \(-Tg+(1-T)B=1\) permits substitution of \(f(\bar u)\) for \(\bar v\) on the graph.
As in the first Frobenius correction, \(\bar u\) is a zero of the reduction of
\[
             H_p(T)=\{g(T^p)B(T)^p+(-g(T))^p B(T^p)\}/p\in\mathbb Z[T].
\]
Its coefficients are rational integers, so \(t=\bar u^p\) is also a zero.

Use the orders \(j=1,2,3,5,8,12,18,30\) in the [torsion graph table](../../../ledger/Yin_L_G0462_v172.md#cyclotomic).
Write \(\mathcal T_p\) for the roots of \(\prod_{p\nmid j}\Phi_j(T)\) in characteristic \(p\), with \(j\) restricted to these eight orders.
The program verifies the exact characteristic-zero identities \(g(\tau)+f(\tau)B(\tau)=0\) from the table using the prescribed signed powers of each primitive \(j\)-th root \(\tau\).
At \(t\in\mathcal T_p\) the residue \(x\) has a root-of-unity lift \(\xi\) of order prime to \(p\) with \(A(\xi)=0\).
Indeed take the unique prime-to-\(p\) root of unity lifting \(x\).
Then \(\xi^a\) is the lift of \(t\) of the same order \(j\).
The table makes \(f(\xi^a)\) a root of unity of order prime to \(p\), since \(p\) is odd.
It has the same reduction \(f(t)=x^b\) as \(\xi^b\), so these two roots of unity agree.
Thus one of the \(m_x\) available occurrences above \(x\) belongs to a torsion root of the parent.

<a id="residues"></a>
## Exact residue and multiplicity calculations

For \(p=3,5,7\), factorization over \(\mathbb F_p\) shows that every root of \(H_p\) on the unit graph belongs to \(\mathcal T_p\).
Here the unit graph omits roots of \(TgB\), since both graph coordinates are nonzero.
If \(p\mid a\), coprimality gives \(p\nmid b\) and the derivative \(bX^{b-1}B(X^a)\) is nonzero at every root.
Every residue would then be simple and already occupied by its torsion lift, excluding a nontorsion \(\alpha\).
Otherwise put \(\lambda=b/a\bmod p\) and
\[
             R_\lambda(T)=T(g'B-gB')-\lambda gB .
\]
By the [derivative identity](../../../claims/Yin_C_G0345_v383.md#inertia), \(m_x-1\le\operatorname{ord}_{t}R_\lambda\).
Indeed \(X\mapsto X^a\) is unramified at \(x\), and after multiplying the logarithmic derivative of \(A\) by a local unit and subtracting a multiple of \(A\) one obtains \(aR_\lambda(X^a)\).
Distinct \(x\)'s give distinct \(t\)'s because \(t\) determines \(x^b\) and \((a,b)=1\).

For each slope the table gives the largest root multiplicity of \(R_\lambda\) on the unit graph outside \(\mathcal T_p\), taking zero when there is none, and the sum of multiplicities at the roots in \(\mathcal T_p\) on the unit graph.
Entries in a row are ordered by \(\lambda=0,\ldots,p-1\).

| \(p\) | Maximum outside \(\mathcal T_p\) | Sum on \(\mathcal T_p\) |
| ---: | --- | --- |
| 3 | \(1,0,1\) | \(0,6,4\) |
| 5 | \(1,1,1,0,3\) | \(0,2,2,6,0\) |
| 7 | \(0,1,1,2,1,1,1\) | \(4,2,2,2,0,0,0\) |

An \(x\) with \(t\notin\mathcal T_p\) would have \(m_x<p\) by the middle column, and hence \(H_p(t)=0\bmod p\), contradicting the computed root support.
For each remaining \(x\) at most \(m_x-1\) conjugates of \(\alpha\) fit above the residue, since at least one root is the torsion lift.
Summing the derivative bound over their distinct coordinates \(t\) proves that \(d\) is at most the corresponding entry of the last column.
In particular \(d\le6\) for all three primes.
At \(p=3\) this also excludes the slope \(0\) outright.

<a id="measure"></a>
## A reciprocal lift and its possible measure

The reciprocal parent has coefficient norm at most \(\sqrt8\), so Jensen and Parseval give \(M(A)\le\sqrt8\).
If the minimal polynomial \(P\) of \(\alpha\) were nonreciprocal, its distinct monic reciprocal would also divide the parent and \(M(A)\ge M(P)^2\).
A reciprocal \(\gamma\) would make its power \(\alpha\) reciprocal, so in this case \(\gamma\) would be nonreciprocal.
By [Smyth's theorem](../../../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions), \(M(\gamma)\ge\theta>13/10\), where \(\theta>1\) is the real root of \(X^3-X-1\).
Since \(\gamma,\alpha\) have the same degree, this gives \(M(A)\ge M(\gamma)^{2p}>\sqrt8\).
Thus \(\alpha\) is reciprocal.

Let \(\iota\) send \(\alpha\) to \(\alpha^{-1}\) in \(K\), an involution since \(\alpha\) and its inverse generate the same field.
The element \(\delta=\gamma\iota(\gamma)\) is fixed by \(\iota\) and satisfies \(\delta^p=1\).
Set \(\eta=\delta^{(p-1)/2}\gamma\).
Then \(\eta^p=\alpha\) and \(\eta\iota(\eta)=1\), so \(\eta\) is a reciprocal nontorsion unit generating \(K\).
Its monic minimal polynomial has even degree \(d\in\{2,4,6\}\) and constant term one by inverse pairing.

For these degrees the exact enumeration below proves \(M(\eta)>27/20\).
The six parent monomials have distinct exponents apart from \(b=a\) or \(b=3a\), which force \(a=1\).
In the first case their signed coefficient norm drops to \(\sqrt2\), and in the second case it is \(\sqrt8\).
In all other cases the norm is \(\sqrt6\).
Since \((27/20)^3>\sqrt6\) and \((27/20)^5>\sqrt8\), the bound \(M(A)\ge M(P)=M(\eta)^p\) excludes each prime, except possibly \(p=3\) at \((1,3)\).
That direction has slope zero modulo three, already excluded.

<a id="graeffe"></a>
## Exact enumeration in degrees two, four and six

For a monic polynomial of degree \(d\), each coefficient of index \(i\) has absolute value at most \(\binom di M\), by the elementary symmetric formula.
Enumerate all integral reciprocal polynomials with leading and constant coefficient one satisfying those bounds with \(M=27/20\).
If their actual measure is at most \(27/20\), the polynomial on their \(n\)-th powers has measure at most \((27/20)^n\) and must satisfy the corresponding coefficient inequalities.
For \(n=1,2,4,8,16,32,64\) the program computes the powered polynomials by squaring the roots, using \(E(Y)^2-Y O(Y)^2\) for the polynomial \(E(X^2)+X O(X^2)\) of even degree.
Every bound is rounded down by integer division.

| Degree | \(1\) | \(2\) | \(4\) | \(8\) | \(16\) | \(32\) | \(64\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| 4 | 187 | 41 | 21 | 19 | 19 | 19 | 19 |
| 6 | 38,335 | 863 | 163 | 75 | 63 | 61 | 59 |

Every final survivor divides entirely into cyclotomic factors, as checked by exact monic division.
The program tests orders through \(2d^2\), since \(\varphi(j)^2\ge j/2\).
Thus every nontorsion reciprocal minimal polynomial in these degrees has measure strictly greater than \(27/20\).

<a id="reproduction"></a>
## Files and reproduction

Run the [certificate program](small_odd_powers.py) from the repository root.

~~~~powershell
python mathematics/computations/programs/Yin_J_G0171/small_odd_powers.py
~~~~

The completed calculation used Python 3.14.3 and SymPy 1.14.0 with integer and finite-field polynomial arithmetic.
It uses the fixed cubic pair, eight torsion values, three primes and coefficient bounds above, and requires no earlier output.
It checks the torsion identities over the integers, reconstructs each modular factorization and divides every surviving small-degree polynomial by its cyclotomic factors.
Compare the generated `outputs/Yin_J_G0171/certificate.json` in the computations directory with the fixed certificate.
The fixed [certificate](inputs/certificate.json) records the modular factors and their classifications, the counts after each squaring stage, and the coefficients and complete cyclotomic factorizations of the survivors.
This computation excludes powers in the root field for the three specified primes at every degree and direction.
