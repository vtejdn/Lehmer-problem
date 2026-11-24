---
author: Yin
---

# Short two-row witnesses at almost every prime between twice and four times the seed degree

2026-11-24T17:41 UTC.
A research agent working for Yin developed a finite-prime version of the [fixed-width cost estimate](Yin_C_G0901_v1.md#width) for the [Lehmer task](../tasks/Yin_T_G0001_v1.md#contract).
The argument tolerates primes at which the seed has a small number of repeated factors, counted by degree with multiplicity.

<a id="window"></a>
## A linear prime interval for the original seed

Let \(P\) be a monic reciprocal irreducible integer polynomial of a nontorsion unit \(\alpha\), of degree \(e\) and positive logarithmic measure \(h=m(P)\le1\).
Put \(k=\lceil e\sqrt h\rceil,\ B=e+k,\ r=k+1\).
For all but \(O(e/r)\) of the primes \(2e\le p\le4e\), there are nonzero integral rows \(U,V\) of degree at most \(B\), coprime over \(\mathbb Q[Y]\), with
\[
 P^2\mid U(X^p)+XV(X^p),\qquad UU^\iota-VV^\iota\ne0,\qquad \iota(Y)=1/Y .
\]
Writing \(H=\max(\|U\|_1,\|V\|_1)\) in coefficient one-norm, the bound is
\[
 h\ \le\ \frac{\log H}{p}\ \ll\
     \sqrt h\log(2/\sqrt h)+\frac{\log(2e)}{\sqrt e}.                 \tag{1}
\]
The implied constants are absolute.
The exceptional primes can depend on \(P\).
Along every sequence of original seeds with \(h\to0\), the admissible primes have relative proportion tending to one in their respective intervals, and the normalized log heights tend uniformly to zero on the admissible primes.
The [finite construction for two signed targets](../claims/Yin_C_G0345_v463.md#statement) selects a good prime in a longer interval and imposes genuine double contact on a unit and its square.
Here each pair must pass the [ordinary two-row test](../claims/Yin_C_G0345_v408.md#statement) at the original seed and exponent, even when the reduction at that prime has repeated roots.

<a id="finite"></a>
## A jet count with a quantified loss of rank modulo the prime

More generally fix \(B=e+k,\ k\ge0\), and a prime \(p>e+1\).
Write \(\bar P\) for the reduction, \(a_p=e-\deg\operatorname{rad}(\bar P)\), \(r=k+1\), and \(s=\min(e,r-a_p)\).
Assume \(s>0\).
Let \(N=2B+2,\ D=pB+1\) and set
\[
 W=\frac{2Dh+2e\log(6N)+e\log(1+D)+(2r-s)\log3}{s}.
\]
There is a qualifying pair with
\[
                   \log H\le W+\log(10(B+1))
                               +k\log(2\mathrm e B/k),                \tag{2}
\]
where the last term is zero at \(k=0\) and \(\mathrm e=\exp(1)\).

The powered element \(z=\alpha^p\) still has degree \(e\) even when \(p\) divides the discriminant.
Indeed let \(L=\mathbb Q(\alpha)\), \(K=\mathbb Q(z)\), \(d=[L:K]<p\), and \(\nu=N_{L/K}(\alpha)\).
Then \(\nu^p=z^d\).
Choose integers \(a,b\) with \(ad+bp=1\), so \(\beta=\nu^a z^b\in K\) has \(\beta^p=z\).
If \(\alpha\ne\beta\) then \(\alpha/\beta\in L\) has order \(p\), forcing \(p-1\le e\).
Thus \(\alpha=\beta\) and \(K=L\).
The minimum \(Q\) of \(z\) has degree \(e\) and \(m(Q)=ph\).

Use the rational vector space of degree-at-most-\(B\) row pairs whose graph \(G=U(X^p)+XV(X^p)\) is divisible by \(P^2\).
As in the [fixed-width subspace argument](Yin_C_G0901_v1.md#bad), the subspace of pairs with both values zero at \(z\) has dimension at most \(2r-\min(r,e)\).
In fact dividing both rows by \(Q\) leaves \(2r\) rational coordinates subject to a value equation of rank at least \(\min(r,e)\), since \(Q(X^p)\) has a simple zero at \(\alpha\).
Any rational linear subspace on which \(\Delta(U,V)=UU^\iota-VV^\iota\) vanishes identically has dimension at most \(r+a_p\).
For this assertion intersect the subspace with the full coefficient lattice and reduce modulo \(p\).
Saturation preserves its dimension.
The graph value and its derivative give \(\bar P\mid \bar V(X)^p,\bar U(X)^p\), hence \(\operatorname{rad}(\bar P)\) divides each row.
The first reduced row lies in a space of dimension \(B+1-\deg\operatorname{rad}(\bar P)=r+a_p\).
It determines the reduced pair injectively because a zero first row forces \(\bar V\bar V^\iota=0\).
Both unwanted dimensions are therefore at most \(2r-s\).

Choose \(T=1+\lfloor\exp W\rfloor\) and submit the integer coefficient box \([0,T]^N\) to the [two-jet value count](../claims/Yin_C_G0345_v362.md#jets).
Subtracting one member from the members of a largest fiber gives at least
\[
 \frac{(T+1)^N}{(6NT)^{2e}(1+D)^e\exp(2Dh)}>(3T)^{2r-s}
\]
integral pairs in the graph space of supremum norm at most \(T\).
A linear subspace of dimension \(d_0\le2r-s\) contains at most \((2T+1)^{d_0}\le(3T)^{2r-s}\) integral points in that box, by projecting injectively onto \(d_0\) coordinate axes.
Thus the span of the differences has neither unwanted property.
One difference \(J\) has nonzero value at \(z\) in at least one row.
By polarization some difference or sum \(F\) of two differences has \(\Delta(F)\ne0\).
At most one of \(F+cJ\), \(c=0,1,2,3\), has both values zero, and at most two have zero reflected determinant, by any coefficient of \(\Delta(F+cJ)\) nonzero at \(c=0\).
A remaining pair has supremum norm at most \(5T\).
Its graph equation makes both row values nonzero at \(z\).

<a id="division"></a>
## The cost of removing a common divisor of small degree

Let \(E\) be the primitive common polynomial divisor of maximal degree of the last two integral rows, taken over \(\mathbb Q[Y]\).
Its degree \(g\) is at most \(k\).
Indeed \(E(z)\ne0\), so dividing it out over \(\mathbb Z\) preserves \(P^2\) in the graph and preserves the nonzero reflected determinant.
The determinant of the resulting rows is divisible in the Laurent ring by \(Q^2\) by [reflected elimination](../claims/Yin_C_G0345_v405.md#identity).
Clearing negative powers gives degree at most \(2(B-g)\), whence \(e\le B-g\).

For any row \(A\ne0\) of degree at most \(B\) divisible by \(E\),
\[
             \|A/E\|_1\le
          \frac{2^g\binom Bg}{\exp(m(E))}\|A\|_1 .                   \tag{3}
\]
To prove this, use outward roots \(|\rho|\ge1\) first, with multiplicities and number \(l\).
Division by their monic product has coefficient cost at most
\(\binom Bl/\prod_{|\rho|\ge1}|\rho|\).
Indeed the inverse factors are \(-\rho^{-1}\sum_{j\ge0}(Y/\rho)^j\).
Only coefficients through degree \(B-l\) of their product are needed, since the quotient is a polynomial of that degree or less.
The sum of the absolute coefficients through that degree is at most \(\binom Bl/\prod|\rho|\) by counting the \(l\) nonnegative indices of sum at most \(B-l\).
The estimate also holds for \(l=0\).
Reverse the remaining dividend and quotient at their actual formal degrees to divide by the remaining monic factors \(Y-\rho\) with \(|\rho|<1\).
Their reversals are \(1-\rho Y\), with constant term one, so the same coefficient count costs at most \(\binom{B-l}{g-l}\), including zero roots.
Finally divide by the absolute leading coefficient of \(E\).
The denominator is \(\exp(m(E))\), and the product of binomials is \(\binom Bg\binom gl\le 2^g\binom Bg\).
This proves (3).
Since \(E\) is integral, \(m(E)\ge0\).
For \(g\le k\le B\) the log of the numerator in (3) is at most \(k\log(2\mathrm e B/k)\), by the binomial bound and monotonicity of \(x\log(2\mathrm e B/x)\) on this interval.
Combining (3) with \(5(B+1)T\) and \(T\le2\exp W\) gives (2).

<a id="primes"></a>
## Counting the exceptional primes

For \(p>e+1\), the derivative has its original degree on reduction, and \(a_p=\deg\gcd(\bar P,\bar P')\).
Each root multiplicity is less than \(p\), which gives this equality over a splitting field.
In the integer Sylvester matrix of \(P,P'\), the corank modulo \(p\) is \(a_p\).
This follows by dividing each reduced polynomial by their gcd in the linear relation \(A\bar P+B\bar P'=0\) with \(\deg A<e-1,\deg B<e\).
The Smith invariant factors show \(a_p\le v_p(\operatorname{disc}P)\).
The Vandermonde determinant on the \(e\) conjugates has one row per conjugate \(\alpha_i\) of Euclidean norm at most \(\sqrt e\,\max(1,|\alpha_i|)^{e-1}\).
Hadamard's inequality and squaring therefore give \(\log|\operatorname{disc}P|\le e\log e+2(e-1)h\).
There are at most \(2(e\log e+2(e-1)h)/(r\log(2e))\) primes in the indicated interval with \(a_p>r/2\).

Return to \(k=\lceil e\sqrt h\rceil\le e\).
Every other prime has \(s\ge r/2\) since \(r\le e+1\).
Now \(N=O(e)\), \(D=O(e^2)\), and \(p\ge2e\), so (2) gives
\[
 \frac{\log H}{p}\ll
    \frac{eh}{r}+\frac{\log(2e)}r+\frac{\log(2e)}e
       +\frac{k}{e}\log(2\mathrm e B/k).
\]
Here \(eh/r\le\sqrt h\), and the [house bound for nontorsion units](../claims/Yin_C_G0345_v869.md#degree) gives \(h\ge(\log2)/(4e)\) and hence \(r\gg\sqrt e\).
Also \(\sqrt h\le k/e\le\sqrt h+1/e\ll\sqrt h\), so the last term is \(O(\sqrt h\log(2/\sqrt h))\).
This proves the upper bound in (1).
The [individual lower bound](../claims/Yin_C_G0345_v408.md#lower) supplies the other inequality.
The number of exceptions is \(O(\sqrt e)\) and the prime number theorem gives \(\asymp e/\log e\) primes in \([2e,4e]\).

<a id="gap"></a>
## Finite degree tests for a vanishing gap

For each even \(e\ge2\) and prime \(2e\le p\le4e\), take the least of \(\log2\) and the scores
\[
                     \frac{B-e}{e}+\frac{\log H}{p}
\]
of all ordinary qualifying pairs for some degree-\(e\) reciprocal nontorsion unit seed, using integer \(e\le B\le2e\) and \(H\le2^p\).
Denote this number by \(S_{e,p}\).
For each \(e,p\) only finitely many coefficient vectors enter, and factoring the graph and its derivative tests repeated irreducible factors of the specified degree exactly.
The infimum \(\lambda\) of all positive integer-polynomial log measures satisfies \(S_{e,p}\ge\lambda\) by the individual bound and the constant-polynomial fallback.

It follows that \(\lambda=0\) if and only if the minimum of \(S_{e,p}\) over these primes has limit inferior zero as the even degrees tend to infinity.
Equivalently, along some \(e_j\to\infty\) and some positive \(\eta_j\to0\), the fraction of primes in \([2e_j,4e_j]\) with \(S_{e_j,p}\le\eta_j\) tends to one.
For the forward implications the [reciprocal reduction](../claims/Yin_C_G0345_v408.md#lower) gives actual seeds with \(h_j\to0\) and degrees tending to infinity, since bounded degree and bounded measure bound the integral coefficients.
The same seed at each chosen degree passes at every prime except its \(O(\sqrt{e_j})\) exceptions by (1), and the normalized width excess tends to zero.
For the converse a single sequence of scores tending to zero suffices.
The statement does not choose a single prime in advance which works for every seed of a given degree.
A uniform lower bound for these finite tests remains to be established.

## Assessment history

### Decision linear-prime-window

| Field | Value |
| --- | --- |
| date | 2026-11-24T17:46 |
| status | proved |
| reason | The finite estimate and the exceptional-prime bound establish the result for each original seed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#window) | Near-degree ordinary double-contact rows at almost every prime between twice and four times the original degree. |
| argument | [Finite](#finite) | Degree preservation and finite bounds for both exceptional spaces. |
| argument | [Division](#division) | Coefficient cost of removing the common factor. |
| argument | [Primes](#primes) | Discriminant estimate and count of exceptional primes. |
| argument | [Gap](#gap) | Equivalence of the finite score conditions to zero gap. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1043.md#finding) | The fixed statement, argument and qualifications at the specified inputs. |

## Current assessment

[Selected decision](#decision-linear-prime-window)
