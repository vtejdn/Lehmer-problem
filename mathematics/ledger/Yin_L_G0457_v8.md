---
author: Yin
---

# The longest integral prefix at conductor 21 for the first exceptional parent

<a id="optimal-prefix"></a>
## Minimum degree and exact prefix

Take \(F_2=(1+z^2)^3\), \(p=21\), \(n=10\), \(r=17\), and \(b_j=2\cos(2\pi j/21)\) for \(1\le j\le10\).
Use \(B_0=1,\ B_1=t+1,\ B_{a+1}=t B_a-B_{a-1}\).
For the [exceptional-parent construction](Yin_L_G0457_v7.md#effective-cutoff) the perturbed trace is \(Q=t^3 B_8+H\).
Among integral \(H\) that give a strict terminal cut, the minimum degree is three.
The same minimum holds with the strict endpoint \(Q(-2)/B_{10}(-2)<0\).
Indeed the [integer cubic witness](../computations/programs/Yin_J_G0138/readme.md#p21-cubic-witness) \(H=t-t^3\) gives nine positive residues and one negative residue, with endpoint ratio \(-2\).
The main researcher obtained the lower bound below from interpolation at three nodes of the finite grid.
The [independent optimality review](../audits/reviews/Yin_R_G1107_v49.md#p21-optimal-review) checks the four interpolation values, integrality exclusion and matching prefix against the cubic witness.

Consequently the longest possible initial agreement with \(F_2/(1-z)\) for the integral lifts in the positive-residue-sum domain \(\deg H\le n-2\) ends at coefficient index seven, counting the constant term as index zero.
Indeed their difference from the reference is
\[
   -z^{17}F_2/(1-z)+z^{11}H(z+z^{-1}).
\]
For nonzero \(H\) of degree \(k\le8\), the first differing coefficient has index \(11-k<17\) and is exactly the leading coefficient of \(H\).
The zero perturbation has no negative residue.

<a id="three-node-test"></a>
## Three-node interpolation

Suppose \(\deg H\le2\), and put \(v_j=-b_j^3 B_8(b_j)\).
On the initial positive block \(H(b_j)>v_j\) at odd \(j\), while \(H(b_j)<v_j\) at even \(j\).
On the terminal block these inequalities reverse, since \(B'_{10}(b_j)\) has sign \((-1)^{j+1}\).
The [nonnegative grid phase](Yin_L_G0457_v7.md#effective-cutoff) forces \(H\) to alternate strictly on every pair of consecutive terminal nodes.
A quadratic or lower-degree polynomial can therefore have at most three such terminal nodes, leaving only cuts \(c=7,8,9\).

For a triple \(I\) of distinct node indices write
\[
 \ell_j=\prod_{i\in I\setminus\{j\}}\frac{-b_i}{b_j-b_i},\qquad
 V_I=\sum_{j\in I}\ell_j v_j .
\]
Lagrange interpolation gives \(H(0)=\sum_{j\in I}\ell_j H(b_j)\).
The signs of the three weights follow from \(b_1>\cdots>b_{10}\) and \(b_5>0>b_6\).
For each row they make all three terms of \(\sum\ell_j(H(b_j)-v_j)\) strictly of the same sign, as indicated.

| Cuts \(c\) | Triple \(I\) | Weight signs in order | Interpolation inequality | Rational enclosure for \(V_I\) |
| --- | --- | --- | --- | --- |
| \(7,8\) | \(7,9,10\) | \(+,-,+\) | \(H(0)>V_I\) | \((85,86)\) |
| \(7,8\) | \(2,9,10\) | \(+,+,-\) | \(H(0)<V_I\) | \((-32,-31)\) |
| \(9\) | \(4,5,10\) | \(-,+,+\) | \(H(0)>V_I\) | \((-5/100,-4/100)\) |
| \(9\) | \(4,6,10\) | \(+,+,-\) | \(H(0)<V_I\) | \((-1/100,-9/1000)\) |

The first two rows exclude \(c=7,8\) over the reals.
The last two force \(-1<H(0)<0\) for \(c=9\), excluding integrality without a bound on any coefficient.

<a id="arithmetic"></a>
## Exact evaluation of the four bounds

Set \(x=b_1\) and \(g(X)=X^6-X^5-6X^4+6X^3+8X^2-8X+1\).
The recurrence for \(B_{10}\) gives
\[
 B_{10}(X)=(X+1)(X^3+X^2-2X-1)g(X).
\]
The [ten isolating intervals](../computations/programs/Yin_J_G0138/readme.md#p21-cubic-witness) put its largest root in \((1910/1000,1912/1000)\) and every other root below it.
Direct substitution gives opposite signs of \(g\) at \(19111456/10^7,19111457/10^7\), in increasing order negative and positive.
Hence this smaller rational interval contains \(x\).

For each row the following table gives the coefficients in descending order from \(X^5\) to \(1\) of the polynomial \(R\) with \(V_I=R(x)\).

| \(I\) | Coefficients |
| --- | --- |
| \(7,9,10\) | \(11,8,-48,-13,49,-13\) |
| \(2,9,10\) | \(-2,-2,7,2,-7,3\) |
| \(4,5,10\) | \(-8,4,49,-21,-70,19\) |
| \(4,6,10\) | \(-5,0,25,-5,-25,19\) |

To check these identities, generate \(b_j=T_j(x)\) with \(T_0=2,T_1=X,T_{j+1}=XT_j-T_{j-1}\).
Insert \(T_j\) for \(b_j\) and \(-T_j^3B_8(T_j)\) for \(v_j\) in the interpolation formula.
After clearing its denominators, subtraction of the displayed \(R\) has remainder zero upon division by \(g\) in each of the four rows.
The denominators are nonzero at \(x\) because the ten grid nodes are distinct.
Starting with the rational interval for \(x\) above, Horner evaluation of these four polynomials using interval products and sums gives the stated rational enclosures.
