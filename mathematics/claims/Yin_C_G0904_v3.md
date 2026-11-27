---
author: Yin
---

# Short modular returns and the width of reciprocal coefficient blocks

<a id="statement"></a>
## A test using the coefficients at one end

Let \(Q\in\mathbb Z[X]\) be monic of degree \(r\), put \(Q^*(X)=X^rQ(1/X)\), and set \(D=X^nQ+\varepsilon Q^*\) for \(n\ge1\), \(\varepsilon=\pm1\).
Let \(P\) be any monic integral divisor of \(D\) of degree \(d\ge1\).
The case \(P=D\) includes reciprocal polynomials whose coefficients are confined to two intervals of width \(r+1\) at the ends.
For a prime \(p\), write \(\bar Q=X^t T\) in \(\mathbb F_p[X]\), where \(T(0)\ne0\), and use \(T^*=X^{r-t}T(1/X)\).
Write \(b_p(j)=\deg\gcd(\bar P,X^j-1)\), including all multiplicities.

* If \(T^*=\pm T\), then \(b_p(2(n+t))\ge d-(r-t)\).
* Otherwise \(r\ge1\) and \(b_p(j)\le 2r+2\sqrt{rj}\) for every \(j\ge1\).

Consequently, along any sequence with \(d\to\infty\), \(r=o(d)\) and \(n=O(d)\), a fixed finite set of primes gives returns \(b_p(j)\ge\eta d\) at \(j\le Ad\), with fixed \(A,\eta>0\) on all sufficiently late inputs, if and only if each sufficiently late input has \(T^*=\pm T\) at some prime in that set.
The required prime may vary with the input.
For \(P=D\), the latter condition gives \(j\le2d\) and \(b_p(j)/d\to1\).
These returns give the [two finite-time lower bounds](Yin_C_G0904_v2.md#statement) when \(P\) is the minimum of a nontorsion unit.

<a id="finite-field"></a>
## The bound at every prime, including multiplicities

Since \(Q\) is monic, reduction preserves its degree, and \(\bar D=X^{n+t}T+\varepsilon T^*\).
If \(T^*=cT\) for a scalar \(c\), reversal twice gives \(c^2=1\).
Then \(\bar P\) divides \(T(X^{n+t}+\varepsilon c)\), and \(X^{n+t}+\varepsilon c\) divides \(X^{2(n+t)}-1\).
At most \(\deg T\) degrees of \(\bar P\), counted with multiplicity, can be missing from this last binomial.

In the other case put \(C=\gcd(T,T^*)\), \(U=T/C\), \(V=-\varepsilon T^*/C\) and \(N=n+t\).
The numerator and denominator of \(V/U\) are coprime and have nonzero constant terms.
Their ratio is nonconstant because \(T^*\) is not proportional to \(T\).
Set \(G=\gcd(X^N U-V,X^j-1)\).
From the factorization \(\bar D=C(X^N U-V)\) we get \(b_p(j)\le\deg C+\deg G\).
In \(\mathbb F_p[X]/G\) both \(X\) and \(U\) are units and \(X^N=V/U\).
This quotient retains repeated factors of \(G\).

For any integer \(H\ge1\) there exist \(1\le a\le H\) and \(b\in\mathbb Z\) with \(aN\equiv b\bmod j\) and \(|b|\le j/(H+1)\).
Indeed consider the \(H+1\) residues of \(0,N,\ldots,HN\) around the circle of circumference \(j\).
Either two coincide or a pair of consecutive residues has circular separation at most \(j/(H+1)\), and the sign of the separation may be chosen after ordering the two indices.
In the quotient one then has \((V/U)^a=X^b\).
On clearing denominators this gives a polynomial divisible by \(G\) of degree at most \(ar+|b|\).
It is nonzero in \(\mathbb F_p[X]\), since an identity \((V/U)^a=X^b\) in the rational function field would force \(b=0\) by the valuation at zero and then \(V/U\) constant by coprimality.
Taking \(H=\lceil\sqrt{j/r}\rceil\) gives \(\deg G\le r+2\sqrt{rj}\).
Adding \(\deg C\le r\) proves the bound in the statement.

<a id="bounded-height"></a>
## The only possible prime for coefficients of height one

Suppose \(P\) is irreducible and noncyclotomic with \(d>r\), and every coefficient of \(Q\) has absolute value at most \(B\).
Every prime with \(T^*=\pm T\) is at most \(2B\).
Indeed for \(p>2B\) the exponent \(t\) is the true order of vanishing of \(Q\) at zero.
Write \(Q=X^t T_0\) over the integers.
Congruence of the coefficients of \(T_0^*\) and \(\pm T_0\) then implies their equality over the integers.
This would factor \(D=T_0(X^{n+t}\pm1)\), so any irreducible noncyclotomic divisor of \(D\) would divide \(T_0\) and have degree at most \(r\).

For \(B=1\), reduction modulo two therefore decides the entire short-return question in the range \(r=o(d)\), \(n=O(d)\).
An input has \(T^*=T\bmod2\) precisely when the exponents of the nonzero terms of \(Q\) are symmetric about the midpoint of their least and greatest elements.
On such inputs the first bound applies at two.
On every other input the second bound applies at all primes simultaneously.

<a id="record-width"></a>
## A width constraint on the whole polynomial below the plastic number

Let \(\theta>1\) be the real root of \(X^3-X-1\), and fix \(1<\lambda<\theta\).
Suppose the whole \(P=D\) is irreducible and noncyclotomic and \(M(P)\le\lambda\).
Remove any factor \(X^t\) from \(Q\) by increasing \(n\) by \(t\) and decreasing \(r\) by \(t\).
Then \(r\ge1\) and
\[
                        d=n+r\ \ll_\lambda\ r^2\log(2r).
\]
In particular every strict record after a fixed [subplastic example](Yin_C_G0901_v163.md#rows) satisfies this width constraint in any such representation with disjoint coefficient blocks.
The estimate uses the complete measure of \(D\).

When \(n\le r\) the bound follows from \(d\le2r\).
For \(n>r\) all coefficients of \(Q\) occur in \(P\).
This polynomial has at most \(2r+2\) nonzero terms, so its [sparse coefficient bound](../audits/literature/DS17/Yin_U002.md#sparse-height-bound) gives \(H(Q)\le 2^{2r}\lambda\), where \(H\) denotes maximum absolute coefficient.
If \(Q^*=\pm Q\) the integral factorization above excludes the hypothesized \(P\), including \(r=0\).
Thus \(Q\), whose constant term is nonzero, contains a nonreciprocal irreducible factor up to reversal by a sign.
Indeed a product of irreducible factors each equal to its signed reversal is itself equal to its signed reversal.
Every factor of the monic integral \(Q\) has measure at least one, and [Smyth's nonreciprocal bound](../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions) gives \(m(Q)\ge\log\theta\), where \(m=\log M\).

Put \(\Delta=\log(\theta/\lambda)\), choose \(0<u<\min(1/8,\Delta/8)\), and choose \(0<\delta<1\) with \(\log(1-\delta)>-\Delta/4\).
Some \(R\in[1+u/r,1+2u/r]\) has distance at least \(u/(4r^2)\) from the modulus of each zero of \(Q\), since their \(r\) excluded intervals have total length at most \(u/(2r)\).
On \(|z|=R\) this gives
\[
       |Q(z)|\ge (u/(4r^2))^r,\qquad
       |Q^*(z)|\le(r+1)H(Q)e^{2u},\qquad \log R\ge u/(2r).
\]
For \(n>C_\lambda r^2\log(2r)\) with a sufficiently large \(C_\lambda\), these estimates give \(|Q^*/(z^nQ)|\le\delta\) on the whole circle.
For a monic polynomial \(F\) put \(s_R(F)=\sum_{F(\beta)=0}\log^+(|\beta|/R)\), counting multiplicities.
Jensen's formula on this circle gives its mean logarithm as \((\deg F)\log R+s_R(F)\).
Hence
\[
 m(P)\ \ge\ s_R(P)\ \ge\ s_R(Q)+\log(1-\delta)
 \ \ge\ m(Q)-r\log R+\log(1-\delta)\ >\ \log\lambda .
\]
This contradicts the measure ceiling and proves the stated bound.
For a sequence of strict records of growing degree it gives \(r\gg_\lambda\sqrt{d/\log(2d)}\).
The range between this width and \(o(d)\) still permits the modular test.

<a id="salem"></a>
## A decreasing Salem sequence without a positive return fraction

Put \(f=X^3-X-1\), \(f^*=1-X^2-X^3\), and \(D_n=X^n f+f^*\).
The identity \(f+f^*=-X(X+1)\) and \(f(0)=f(-1)=-1\) give \(\gcd(\bar f,\bar f^*)=1\) over every prime field.
The coefficient of \(X\) distinguishes the two polynomials up to every nonzero scalar in every characteristic.
In the proof above \(\deg C=0\), \(r=3\) and \(H=\lceil\sqrt j\rceil\) therefore give, for every prime \(p\), every \(j\ge1\) and every monic factor \(P\mid D_n\),
\[
                       b_p(j)\le4\lceil\sqrt j\rceil .
\]
The same estimate holds for factors of \(X^nf-f^*\), including the [explicit Salem factors below the plastic number](Yin_C_G0901_v195.md#cubic).

The positive-sign exterior roots provide decreasing measures.
The discriminant of \(f\) is \(-23\), and its two nonreal roots have modulus \(\theta^{-1/2}\).
For real \(0<s<1\), Rouché's theorem on the unit circle gives exactly one root outside for \(X^nf+s f^*\), because \(|f^*|=|f|>0\) there.
By continuity of the roots \(D_n\) has at most one exterior root, counted with multiplicity.
It has a real root \(\alpha_n>\theta\), since \(D_n(\theta)=f^*(\theta)<0\) and its leading coefficient is positive.
At this root \(f(\alpha_n)>0\), so \(D_{n+1}(\alpha_n)=\alpha_n^n f(\alpha_n)(\alpha_n-1)>0\) and \(\theta<\alpha_{n+1}<\alpha_n\).
For each \(x>\theta\) one has \(D_n(x)>0\) eventually, giving \(\alpha_n\to\theta\).
Reciprocity gives the unique interior root \(\alpha_n^{-1}\), and all remaining roots lie on the unit circle.
Since \(D_n\) is monic with constant term one, every monic integral factor has unit constant term.
The minimal polynomial \(P_n\) of \(\alpha_n\) must therefore contain \(\alpha_n^{-1}\), and \(M(P_n)=\alpha_n\).
The degrees \(d_n\) tend to infinity, since bounded degree and bounded measure allow only finitely many monic integral polynomials and all these exterior roots are distinct.
Thus \(\alpha_n\) is a Salem number for all sufficiently large \(n\).
For every \(k\ge1\), the conjugates of \(\alpha_n^k\) arise with common multiplicity \([\mathbb Q(\alpha_n):\mathbb Q(\alpha_n^k)]\) when the \(k\)-th powers of the conjugates of \(\alpha_n\) are listed.
The unique exterior root forces that multiplicity to equal one.

For \(n\equiv1\bmod120\) sufficiently large, the [cyclotomic factor calculation](Yin_C_G0345_v129.md#progression) gives \(P_n=D_n\), of degree \(n+3\).
Along this subsequence the degrees increase and the measures strictly decrease, and for each fixed \(A>0\) the supremum of \(b_p(j)/d_n\) over all primes and all \(j\le A d_n\) tends to zero.
At the same time the [integral cyclic resultant at \(4d_n\)](Yin_C_G0336_v2.md#statement) exceeds \((41/20)^{d_n}\).
The measures approach \(\theta\), above the known strict degree records, so the family tests the force of the one-exterior-root condition, degree preservation under powers and decrease within a family.
Whether every strict record satisfies the finite-prime short-return condition remains open.

## Assessment history

### Decision end-block-returns

| Field | Value |
| --- | --- |
| date | 2026-11-27T12:32 |
| status | proved |
| reason | The quotient-ring bound preserves all multiplicities, and the coefficient and circle estimates distinguish the exceptional primes from a genuine decreasing Salem family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [End-block criterion](#statement) | Finite-prime coverage for a polynomial or a divisor of its two-block presentation. |
| argument | [Modular proof](#finite-field) | Signed short relation and the two coefficient cases. |
| argument | [Height-one test](#bounded-height) | Finite exceptional prime set and support reflection. |
| argument | [Record width](#record-width) | Jensen bound below a fixed subplastic measure ceiling. |
| argument | [Salem controls](#salem) | Uniform failure of linear return fractions along a decreasing Salem family. |
| dependency | [Window inequality](Yin_C_G0904_v2.md#statement) | Applicability to both original observables. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1284.md#finding) | All five sections and the named source and integer-resultant interfaces. |

## Current assessment

[Selected decision](#decision-end-block-returns)
