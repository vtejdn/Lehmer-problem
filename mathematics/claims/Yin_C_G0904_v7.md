---
author: Yin
---

# A two-thirds lower bound for the width of separated coefficient blocks

<a id="width"></a>
## Width and exterior roots at a fixed measure ceiling

Let \(Q\in\mathbb Z[X]\) be monic of degree \(r\), let \(Q^*(X)=X^rQ(1/X)\), and assume that \(P=X^nQ\pm Q^*\) is irreducible and noncyclotomic, with \(n>r\).
Write \(d=n+r\), \(k=\#\{\beta:Q(\beta)=0,\ |\beta|>1\}\) with multiplicities, and \(m=\log M(Q)\).
Fix \(1<\lambda<\theta\), where \(\theta\) is the plastic number, and suppose \(M(P)\le\lambda\).
Then
\[
                n\ll_\lambda r\left(1+\sqrt{k/m}\right),
              \qquad r\gg_\lambda d^{2/3}.
\]
The degree-ten competitor puts every [strict degree record from degree ten onward](Yin_C_G0904_v5.md#record) in this range with \(\lambda=19/16\).
The proof needs only the ceiling on the whole polynomial and the arithmetic of its end block.
If a sequence of these records still has \(r=o(d)\), then \(m/k\ll_\lambda(r/d)^2\).
In particular the geometric mean of the exterior root moduli of the end block must tend to one.

Absorb any factor \(X^t\) of \(Q\) by replacing \(n\) by \(n+t\) and \(r\) by \(r-t\).
Proving the bound after this operation proves it for the original parameters, since \(m,k,d\) do not change.
The remaining \(Q\) has no factor in common with \(Q^*\), since such a factor would divide \(P\) and have smaller degree.
Every irreducible factor of \(Q\) is consequently nonreciprocal up to sign, and no root has modulus one.
In the last assertion, a unit-circle root and its complex conjugate would supply a common root of \(Q,Q^*\).
The case \(r=0\) gives only a product of cyclotomic factors.
Thus \(m\ge m_0=\log\theta>0\) by [Smyth's nonreciprocal bound](../audits/literature/Smy71/Yin_U001.md#smy71-statement-and-conventions).

<a id="energy"></a>
## Angular concentration from the reciprocal resultant

Send every root \(\beta_i\) of \(Q\) to \(w_i=\beta_i\) if \(|\beta_i|<1\), and to \(w_i=1/\overline{\beta_i}\) otherwise.
All \(w_i\) lie in the open unit disk.
Writing \(S_l=\sum_{i=1}^r w_i^l\), we have
\[
              \mathcal E=\sum_{l\ge1}\frac{|S_l|^2}{l}\le 2rm.
\]
Indeed the nonzero integer \(\operatorname{Res}(Q,Q^*)\) has absolute value \(\prod_{i,j}|1-\beta_i\overline{\beta_j}|\), using reality and monicity.
Divide each factor by \(\max(1,|\beta_i|)\max(1,|\beta_j|)\).
For roots on the same side of the circle its new absolute value is \(|1-w_i\bar w_j|\).
For roots on opposite sides it is \(|w_i-w_j|\le |1-w_i\bar w_j|\), since the difference of the squared moduli is \((1-|w_i|^2)(1-|w_j|^2)\).
Expanding \(\log|1-w_i\bar w_j|\) as a convergent power series and summing proves \(\mathcal E\le2rm-\log|\operatorname{Res}(Q,Q^*)|\).
This argument includes repeated factors of \(Q\).

For \(|v|<1\) put \(K(v)=(1-|v|^2)/|1-v|^2=1+2\Re\sum_{l\ge1}v^l\).
For \(0<T\le1/16\), \(T\le y\le2T\) and every angle \(u\), Cauchy–Schwarz gives
\[
 y\sum_i K(e^{-y-iu}w_i)\ll rT+\sqrt{rm},
\]
using \(\sum_{l\ge1}l e^{-2ly}\ll y^{-2}\).
Partition the circle into equal intervals of lengths between \(T/2\) and \(T\), and let \(B_j\) count the \(w_i\) in interval \(j\) for which \(-\log|w_i|\le 8T\).
For two such points in the same interval \(K(e^{-2T}w_i\bar w_h)\gg1/T\) because the exponent of its modulus lies between \(2T\) and \(18T\), and its argument has absolute value at most \(T\).
Positivity and summation now give
\[
   \sum_j B_j^2\ll T\sum_{i,h}K(e^{-2T}w_i\bar w_h)
     =T\left(r^2+2\sum_{l\ge1}e^{-2lT}|S_l|^2\right)
     \ll r^2T+rm .
\]
The last inequality uses \(\sup_{l\ge1} l e^{-2lT}\ll1/T\).

<a id="circle"></a>
## Choosing a radius that works for every angle

At \(z=e^{y+iu}\), the modulus of \(Q^*(z)/Q(z)\) is the product of \(|1-\bar\beta_i z|/|z-\beta_i|\).
Roots inside the unit circle contribute at most one.
For an exterior root set \(x_i=\log|\beta_i|\), \(w=w_i\), \(v=1/\bar z=e^{-y+iu}\) and \(\rho=|v-w|/|1-\bar wv|\).
Its log contribution is \(-\log\rho\), which is nonnegative.
When \(\rho\ge1/2\) one has
\[
 -\log\rho\ll 1-\rho^2
  =\frac{(1-|v|^2)(1-|w|^2)}{|1-\bar wv|^2}
  \le 2yK(\bar v w).
\]
The total of these contributions is \(O(rT+\sqrt{rm})\), uniformly in \(u,y\), by the first kernel estimate.

If \(\rho<1/2\), then \(|v-w|< (1-|v|^2)/(2-|v|)\le 2y\), by \(|1-\bar wv|\le1-|v|^2+|v||w-v|\).
The smallest possible \(\rho\) at given moduli occurs when \(u=\arg w\), by the same identity for \(1-\rho^2\).
Thus \(|\,|v|-|w|\,|/(1-|v||w|)<1/2\), so \(|w|>(|v|-1/2)/(1-|v|/2)\).
For \(0<y\le1/8\) the last bound gives \(x_i\le4y\).
Indeed \((e^{-y}-1/2)/(1-e^{-y}/2)\ge e^{-4y}\) follows after putting \(a=e^{-y}\) and factoring \(2a-1-2a^4+a^5=(a-1)(a^4-a^3-a^2-a+1)\), since \(a\ge e^{-1/8}>7/8\).
The bound on \(|v-w|\), together with \(|v|,|w|\ge e^{-1/2}\), also gives circular angular distance \(O(T)\) from \(u\).
Hence at each angle only a bounded number of consecutive intervals can contain these roots.

For each such root with \(x_i\le8T\), evaluating the potential at its maximal angle \(u=\arg w_i\) gives the bound
\[
 -\log\rho\le \log\frac{1-e^{-(y+x_i)}}{|e^{-y}-e^{-x_i}|}
 \le C+\log^+\frac{T}{|y-x_i|}\qquad(T\le y\le2T).
\]
Here \(C\) is absolute by the mean value theorem and \(x_i+y\le10T\).
Write \(L_j(y)\) for the sum of these last upper bounds over the exterior roots counted in \(B_j\), taking \(C>0\).
With normalized Lebesgue measure on \([T,2T]\) each summand has bounded \(L^2\) norm, since \(\int_0^1\log^2(1/t)\,dt=2\).
The \(L^2\) triangle inequality yields \(\|L_j\|_2\ll B_j\).
The sum from all \(\rho<1/2\) is at most \(C'\max_j L_j(y)\), uniformly in \(u\), because only boundedly many intervals meet the angular condition.
Since \(\int\max_j L_j^2\le\sum_j\|L_j\|_2^2\), one can choose \(y\in[T,2T]\) off the finite set of root log radii with
\[
       \log\max_{|z|=e^y}|Q^*(z)/Q(z)|
             \ll rT+\sqrt{rm}+\sqrt{r^2T+rm}
             \ll r\sqrt{T}+\sqrt{rm}.
\]

<a id="comparison"></a>
## Consequences of the measure comparison

Put \(\Delta=m_0-\log\lambda>0\).
Choose \(0<c\le1/16\) with \(2c m_0\le\Delta/4\), and put \(T=c\min(1,m/k)\).
For \(y\in[T,2T]\) we have \(m-ky\ge(1-2c)m\ge m_0-\Delta/4\).
Choose \(0<\delta<1\) fixed with \(\log(1-\delta)>-\Delta/4\).
If \(m\le k\), the preceding circle choice gives \(|Q^*/(z^nQ)|\le\delta\) as soon as \(nT>C(r\sqrt T+\sqrt{rm})+\log(1/\delta)\).
Jensen's formula on that circle then gives \(\log M(P)\ge m-ky+\log(1-\delta)>\log\lambda\), by the [radial measure comparison](Yin_C_G0904_v5.md#exterior).
Therefore \(n\ll_\lambda r\sqrt{k/m}\) in this case, using \(k\le r\) and \(m\ge m_0\) to absorb the constant term after division by \(T\).
When \(m>k\), take \(T=c\) and use the [angle-independent bound](Yin_C_G0904_v5.md#exterior) on a circle in this same radial range, namely \(\log\max|Q^*/Q|\ll k\).
The same Jensen comparison then forces \(n\ll_\lambda k+1\ll_\lambda r\).
These two cases prove the claimed width bound.

Finally each nonreciprocal irreducible factor of \(Q\) costs at least \(m_0\) in log measure even when repeated.
Consequently \(Q\) has at most \(m/m_0\) irreducible factors with multiplicities.
On a hypothetical sequence with \(r=o(d)\), the fraction of its \(k\) exterior roots belonging to factors with at most \(H\) exterior conjugates is \(O_\lambda(H(r/d)^2)\).
This tends to zero for any \(H=o((d/r)^2)\).
The range \(d^{2/3}\ll_\lambda r=o(d)\) still allows blocks made up of factors with many near-unit exterior conjugates.
Excluding this range requires another consequence of the hypotheses.

<a id="progression"></a>
## When the exponents of the block lie in an arithmetic progression

After removing the monomial at zero, suppose \(Q(X)=R(X^\ell)\), where \(\ell\ge1\), \(q=\deg R\), and \(k_R\) counts the exterior roots of \(R\) with multiplicities.
Then
\[
        \frac{n}{r}\ll_\lambda 1+\sqrt{\frac{k_R}{\log M(R)}} ,
        \qquad r=\ell q.
\]
Indeed \(\log M(R)=m\), and \(R,R^*\) have no common root because \(Q,Q^*\) have none.
Use the circle estimate for \(R\) with parameters \(q,k_R,m\) and \(T=c\min(1,m/k_R)\).
On \(|z|=e^{y/\ell}\) the supremum of \(|Q^*/Q|\) equals its counterpart for \(R\) on \(|z|=e^y\).
The total loss in the exterior log measure of \(Q\) on the smaller circle is at most \(k_R y\), since each exterior root of \(R\) produces \(\ell\) roots of \(Q\) with log radius divided by \(\ell\).
The dominant term now has exponent \(ny/\ell\), so both cases of the preceding comparison apply with \(n/\ell\) in place of \(n\) and \(q\) in place of \(r\).
No integrality of \(n/\ell\) is used.
If \(P\) is a strict record, then \(\gcd(n,\ell)=1\), since a common divisor \(b>1\) would give \(P(X)=A(X^b)\) with \(\deg A=d/b\) and \(M(A)=M(P)>1\).
Thus a narrow record sequence would require \(k_R/m\gg_\lambda(d/r)^2\) even after this compression, and in particular \(q\gg_\lambda(d/r)^2\).

## Assessment history

### Decision two-thirds-width

| Field | Value |
| --- | --- |
| date | 2026-11-28T07:47 |
| status | proved |
| reason | The integral reciprocal resultant limits the angular concentration of near-unit roots. Selecting a circle simultaneously for all angles bounds the separation compatible with small measure. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Width](#width) | Two-thirds degree lower bound and mean exterior log radius. |
| argument | [Angular energy](#energy) | Reciprocal resultant and the Poisson kernel. |
| argument | [Radius selection](#circle) | Exterior root contributions near and away from the angle tested. |
| argument | [Comparison](#comparison) | Jensen bound and factor multiplicities. |
| argument | [Progression support](#progression) | Power substitution and strict-record coprimality. |
| dependency | [Measure comparison](Yin_C_G0904_v5.md#exterior) | Radial Jensen inequality and the angle-independent estimate. |
| dependency | [Record ceiling](Yin_C_G0904_v5.md#record) | The degree-ten competitor. |
| dependency | [Nonreciprocal measure](../audits/literature/Smy71/Yin_U001.md#smy71-u001) | Lower bound for each irreducible factor of the monic block. |
| review | [Independent examination](../audits/reviews/Yin_R_G0562_v1295.md#finding) | Entire argument, both parameter ranges and compressed support. |

## Current assessment

[Selected decision](#decision-two-thirds-width)
