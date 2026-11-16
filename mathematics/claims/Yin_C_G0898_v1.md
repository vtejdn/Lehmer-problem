---
author: Yin
---

# Frobenius congruences force normalized residues above four

<a id="statement"></a>
## A correlated arithmetic test

Take the [strict integral odd-grid chamber](Yin_C_G0893_v1.md#statement), \(p=2n+1\to\infty,\ 1<M(P)\to1\), and pass to a fixed one of the five profiles \(x\).
Use \(b_j=2\cos(2\pi j/p)\), \(U_j=p\rho_j/(b_j-x)^2\), and write \(j'\) for the representative between one and \(n\) of \(\pm2j\bmod p\).
Doubling permutes this half grid even at composite odd conductors.
Omit pairs meeting a pole of \(U\) when forming empirical distributions.
Every subsequential joint weak limit of \((U_j,U_{j'})\), written as the law of \((u,v)\), satisfies, for each fixed integer \(k\ge0\),
\[
 \mathbb E\log\left|T_{2^k}(v-2)-T_{2^{k+1}}(u-2)\right|
                                 \ \ge\ (k+1)\log 2,                     \tag{1}
\]
where \(T_d(z+z^{-1})=z^d+z^{-d}\).
Both marginals equal the same nonatomic probability \(\eta\) on \([0,\infty)\) with mean at most two.
In particular put
\[
                     B=2+2\cosh\!\left(\tfrac18\operatorname{arcosh}3\right)>4.
\]
There is an absolute \(\delta>0\) such that, on each such sequence, the lower limiting fraction of nodes with \(U_j>B\) is at least \(\delta\).
For every \(2<s<B\), this yields at least a positive constant times \(L\) separate excursions from at most \(s\) to above \(B\) on interior angular intervals, for every profile matching length \(L\to\infty\) in its [eligible range](Yin_C_G0897_v1.md#statement).
No nonnegative integral Laurent polynomial evaluated on a fixed finite-dimensional Haar torus can have the limiting marginal law.

The strategy-discovery contributor proposed testing the two ordered residues by a Frobenius congruence and testing finite Laurent models.
The main researcher combined the two signs, iterated the congruence and obtained (1) and the tail bound for all five profiles.
The earlier [correlated prime-grid estimate](../ledger/Yin_L_G0464_v25.md#norm-tests) uses an ordinary difference at two conjugate nodes on the zero profile.

<a id="orbit-test"></a>
## A nonzero multiple of a growing power of two

Write \(Z_j=p\rho_j=(4-b_j^2)h(b_j)\), \(s_j=(b_j-x)^2\), so \(U_j=Z_j/s_j\) where \(s_j\ne0\).
Both \(Z\) and \(s\) are integral polynomials in \(b\).
Since \(b_{j'}=b_j^2-2\), one has \(Z_{j'}\equiv Z_j^2,\ s_{j'}\equiv s_j^2\bmod 2\) in the ring of algebraic integers.
For one pair set
\[
 H=s_{j'}s_j^2,\qquad A=(Z_{j'}-2s_{j'})s_j^2,\qquad
 C=((Z_j-2s_j)^2-2s_j^2)s_{j'} .
\]
These are algebraic integers and \(A-C\) is divisible by two.
The quotients \(A/H,C/H\) give \(U_{j'}-2,\ T_2(U_j-2)\), respectively.
Starting with this triple replace \((A,C,H)\) at every step by
\((A^2-2H^2,C^2-2H^2,H^2)\).
The new difference equals \((A-C)(A+C)\), with the second factor also divisible by two whenever \(A\equiv C\bmod2\).
After \(k\) steps the difference is an algebraic integer divisible by \(2^{k+1}\), and its quotient by \(H^{2^k}\), using the initial \(H\), is the expression inside the absolute value in (1).

Retain the full real cyclotomic orbits of orders \(d>\max(6,p/(2\kappa-1))\), where \(\kappa\) is the size of the negative block.
As in the [orbit count](Yin_C_G0893_v1.md#orbit), these exclude \(o(n)\) nodes, avoid \(b=x\), and each has at least one negative normalized residue.
Every difference just constructed is nonzero there.
If it vanished once then by conjugacy it would vanish on the entire orbit, since multiplication of indices by a unit commutes with doubling.
Along the doubling cycle of a negative \(U_j\), the real values \(y_j=T_{2^k}(U_j-2)\) would satisfy \(y_{j'}=T_2(y_j)=y_j^2-2\).
At the negative node \(|y_j|>2\).
After one more step the value exceeds two and strictly increases at every subsequent step, contradicting periodicity.

The product over the retained nodes of all the nonzero numerators divided individually by \(2^{k+1}\) is a nonzero rational integer by Galois invariance.
Its absolute value is at least one.
To convert this to (1) it suffices to control the denominators and the upper logarithmic tails.

<a id="limit"></a>
## Passage to the ordered pair law

Write \(a=2\cos((2c+1)\pi/p)\) for the midpoint of the strict sign gap, where \(c=n-\kappa\).
For \(b_*=a\) or \(b_*=x\), the positive parts of \(-\log|b_j-b_*|\) are uniformly integrable with normalized counting measure, omitting equalities.
Indeed, in \([0,\pi]\) the angular separations from \(\theta_*=\arccos(b_*/2)\) at nonequal nodes are at least \(\pi/(6p)\).
For \(a\) this follows from the midpoint choice, and for \(x\) from the angles \(0,\pi/3,\pi/2,2\pi/3,\pi\).
The sine difference formula gives \(|2\cos\theta-2\cos\theta_*|\ge4|\theta-\theta_*|^2/\pi^2\).
The grid spacing therefore bounds the fraction in \(0<|b_j-b_*|<\epsilon\) by \(O(\sqrt{\epsilon}+1/p)\), and when this set is nonempty the least separation absorbs the \(1/p\) into \(O(\sqrt\epsilon)\).
This gives uniform exponential upper tails for the logarithms.
The positive parts of \(\log|b_j-x|\) are bounded.
The full grid averages of \(\log|b_j-x|\), ignoring any equalities, consequently tend to the arcsine mean zero by angular equidistribution and the circle mean formula for \(z^2-xz+1\).
Removing \(o(n)\) nodes leaves the same limit.
Since the retained set is stable under doubling, the logarithm of the initial denominator \(H=s_{j'}s_j^2\) has mean tending to zero there.

The positive quantities \(X_j=p(b_j-a)\rho_j\) have [bounded empirical first moments](Yin_C_G0893_v1.md#normalization), so \(\log^+ X_j\) is uniformly integrable.
The identity \(U_j=X_j/((b_j-a)s_j)\) and the angular estimates give uniform integrability of \(\log^+|U_j|\), also at the permuted nodes.
For fixed \(k\) the integrand in (1) has positive part bounded by a constant times \(1+\log^+|U_j|+\log^+|U_{j'}|\).
The pairs are tight because their marginals are tight, and omission of \(o(n)\) pairs does not change any weak limit.
The norm lower bound and the denominator estimate give a lower limiting mean logarithm of at least \((k+1)\log2\) on the retained pairs.
Truncate the logarithm from below before passing to any joint weak limit, using uniform integrability at the upper end, and then remove the lower truncation.
This proves (1).
The equal marginal, its support, first moment and absence of atoms follow from the permutation and the [arithmetic law](Yin_C_G0893_v1.md#statement).

<a id="threshold"></a>
## A tail and angular excursions beyond four

For \(0\le u,v\le B\), the trace Chebyshev polynomial \(T_8(u-2)\) takes values in \([-2,6]\), since \(T_8(B-2)=2\cosh(\operatorname{arcosh}3)=6\).
Similarly \(T_4(v-2)\in[-2,2\cosh(\operatorname{arcosh}(3)/2)]\) and its upper bound is less than six.
The absolute difference is at most eight and is strictly smaller except possibly at \(u=B\).
Consequently the test (1) at \(k=2\) rules out any admissible law supported on \([0,B]^2\), since the first marginal has no atom at \(B\).

To see uniformity, consider all probability laws on \([0,\infty)^2\) with equal marginals of mean at most two, marginal logarithmic energy at least zero and the \(k=2\) inequality in (1).
This class is tight by the first moment.
It is weakly closed: the mean is lower semicontinuous, and the positive logarithmic parts in both tests are uniformly integrable by the first moment and polynomial growth.
Truncation from below thus preserves both lower bounds in the limit, using weak convergence of independent copies for the energy.
Nonnegative energy implies absence of atoms.
If the class is nonempty, the lower semicontinuous marginal mass of the open interval \((B,\infty)\) attains its minimum there.
The preceding strict comparison makes that minimum positive.
The empty class would already exclude the shrinking sequences.
Tightness and the open-set inequality transfer the lower bound to the empirical proportions.
Remove small fixed angular neighborhoods of the profile and endpoints and apply the [positive-kernel run estimate](Yin_C_G0897_v1.md#grid-filter) at level \(s\).
That estimate uses only \(s>2\) and the positive fraction above the chosen higher level.
It gives the claimed number of excursions also at the new threshold \(B\).

<a id="torus"></a>
## Fixed integer Laurent models

Suppose a nonnegative real-valued Laurent polynomial with integer coefficients on \(\mathbb T^r\), evaluated in Haar probability, had marginal law \(\eta\).
Its constant coefficient \(a_0\) equals its mean and is at most two.
Choose an integer vector which separates all exponents in its finite support together with zero under the scalar product.
Such vectors exist outside a finite union of proper hyperplanes, for example on \((1,m,\ldots,m^{r-1})\) for large integers \(m\).
Restrict to the corresponding one-parameter subgroup.
In the nonconstant case the resulting real, nonnegative trigonometric polynomial \(f\) has the same constant term and integer top coefficient \(a_N\ne0\) at some \(N>0\).
Averaging \(f\) over all rotations by \(N\)-th roots of unity leaves \(a_0+2\Re(a_Nz^N)\), so \(2\ge a_0\ge2|a_N|\).
Equality holds throughout.
At a phase attaining zero in this average, all \(N\) summands are zero.
Each zero is at least double because \(f\ge0\), so \(z^N f(z)\) has these \(N\) double roots and no others, by degree.
Its leading coefficient and these roots give \(f(z)=2+a_N(z^N+z^{-N})\) with \(a_N=\pm1\).
The separating choice of the integer vector implies that the original Laurent polynomial likewise has only one pair of opposite nonconstant exponents and range \([0,4]\).
A constant model has range in \([0,2]\).
Both contradict the preceding tail bound.

## Assessment history

### Decision ordered-frobenius-excursions

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:46 |
| status | open |
| reason | Submit the ordered Frobenius inequalities, the tail above four and the obstruction to finite Laurent models for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Ordered doubling pairs](#statement) | Every fixed iterate, all five profiles, interior excursions and the limiting Laurent-model exclusion. |
| argument | [Orbit divisibility](#orbit-test) | Cleared integral Frobenius congruence and escape of a negative node under the real trace map. |
| argument | [Upper logarithmic tails](#limit) | Denominator averages, retained orbits and passage to the correlated law. |
| argument | [A threshold above four](#threshold) | Strict trace-polynomial comparison, compactness and a positive density of large excursions. |
| argument | [Finite Laurent models](#torus) | Highest frequency, nonnegativity and classification at mean at most two. |
| dependency | [Arithmetic marginal law](Yin_C_G0893_v1.md#statement) | Tightness, nonnegative logarithmic energy, first moments and normalization. |
| dependency | [Large orbits](Yin_C_G0893_v1.md#orbit) | Each retained Galois orbit contains a negative node. |
| dependency | [Angular run bound](Yin_C_G0897_v1.md#grid-filter) | Exact filtered moments and the length bound on runs above a fixed level. |


### Decision ordered-frobenius-excursions-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:53 |
| status | proved |
| reason | Adopt the congruences for doubling pairs, the positive tail above four and the obstruction to fixed integral Laurent models. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Ordered doubling pairs](#statement) | Every fixed iterate, all five profiles, interior excursions and the limiting Laurent-model exclusion. |
| argument | [Orbit divisibility](#orbit-test) | Cleared integral Frobenius congruence and escape of a negative node under the real trace map. |
| argument | [Upper logarithmic tails](#limit) | Denominator averages, retained orbits and passage to the correlated law. |
| argument | [A threshold above four](#threshold) | Strict trace-polynomial comparison, compactness and a positive density of large excursions. |
| argument | [Finite Laurent models](#torus) | Highest frequency, nonnegativity and classification at mean at most two. |
| dependency | [Arithmetic marginal law](Yin_C_G0893_v1.md#statement) | Tightness, nonnegative logarithmic energy, first moments and normalization. |
| dependency | [Large orbits](Yin_C_G0893_v1.md#orbit) | Each retained Galois orbit contains a negative node. |
| dependency | [Angular run bound](Yin_C_G0897_v1.md#grid-filter) | Exact filtered moments and the length bound on runs above a fixed level. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v73.md#ordered-frobenius-review) | Independent proof review of integral orbit products, logarithmic limits, the uniform tail, excursions and the finite torus classification. |

## Current assessment
[Selected decision](#decision-ordered-frobenius-excursions-reviewed)
