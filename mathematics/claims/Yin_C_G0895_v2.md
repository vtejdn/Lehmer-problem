---
author: Yin
---

# Small-degree modular factors on the full odd grid

<a id="statement"></a>
## The sampled factor norm and the complete Mahler measure

Let \(p=2n+1\ge5\) be odd, \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), and \(B_n(t)=\prod_j(t-b_j)\).
For any nonzero \(F\in\mathbb Z[t]\) of degree \(d\ge1\) with \(F(b_j)\ne0\) at every node, put \(F^*=z^dF(z+z^{-1})\), \(m_F=\log M(F^*)\), and \(\Delta_F=|\operatorname{Res}(B_n,F)|\).
There is an absolute \(C>0\) such that
\[
 m_F-C\,\frac{d^3\log(2d)\log(2p)}{p}(1+m_F)
       \ \le\ \frac{\log\Delta_F}{n}\
       \le\ m_F+\frac{2d\log p}{p-1}.                                \tag{1}
\]
The coefficient height, multiplicities, leading coefficient and order of any torsion roots are unrestricted subject to the nonvanishing conditions.
Constant factors give the exact identity \(\log\Delta_F/n=\log|F|\).

Use now the [strict integral chamber](Yin_C_G0893_v1.md#statement) with \(p\rho_j=(4-b_j^2)h(b_j)\) and canonical integral representative \(\deg h<n\).
For every sequence with \(p\to\infty,\ 1<M(P)\to1\) and every integral modular factorization
\[
 h\equiv F G\pmod{B_n},\qquad F,G\in\mathbb Z[t],\qquad
                       d^3\log(2d)\log(2p)=o(p),                       \tag{2}
\]
one has \(\limsup M(F^*)\le149/100\).
Here (2) is a condition on the degree only, and places no height bound on \(F\) or \(G\).
The previously [adopted genuine polynomial divisor result](Yin_C_G0895_v1.md#decision-trace-factor-transfer-reviewed) retains its wider degree range \(d=o(\sqrt{p/\log p})\), aggregate factor bound and lower bound for the algebraic degree of the transition root.
The modular conclusion also holds for an explicitly supplied product \(F=\prod_\ell F_\ell\) with each \(\deg F_\ell\le p^{1/3-\epsilon}\), for fixed \(0<\epsilon<1/3\), when the product itself divides \(h\) in the quotient order and no bound on its total degree is assumed.

<a id="circle"></a>
## A relative estimate for each irreducible factor

For a root \(\xi\) of \(F^*\), set \(w=\xi\) if \(|\xi|\le1\) and \(w=1/\xi\) otherwise.
There are no zero roots.
The complete set of nontrivial \(p\)-th roots is invariant under inversion, so its product of distances to \(\xi\), each divided by \(\max(1,|\xi|)\), equals
\[
       H_p(w)=\left|1+w+\cdots+w^{p-1}\right| .
\]
This follows from \(z^p-1\) with the factor \(z-1\) removed, also at \(w=1\).
It gives \(H_p(w)\le p\).
Writing \(a_F\) for the leading coefficient of \(F\), the two conjugate angles for each \(b_j\) and the factorization of \(F^*\) give precisely
\[
        \frac{\log\Delta_F}{n}
                 =m_F+\frac1{p-1}\sum_{\xi:F^*(\xi)=0}\log H_p(w),    \tag{3}
\]
with multiplicities and \(m_F=\log|a_F|+\sum_\xi\log^+|\xi|\).
This proves the upper estimate in (1).

If \(w\) is a root of unity of order \(q>1\), then \(q\nmid p\) by nonvanishing and \(|1-w^p|\ge 2\sin(\pi/q)\ge4/q\).
Consequently \(H_p(w)\ge 2/q\).
With \(D=[\mathbb Q(w):\mathbb Q]=\varphi(q)\), the inequality \(q\le2D^2\) follows from the prime-power formula for \(\varphi\): each odd prime power contributes at least one to \(\varphi(q)^2/q\), and the factor at 2 contributes at least \(1/2\).
For \(w=1\) one has \(H_p(w)=p\).

For a nontorsion root let \(S_w\) be its primitive irreducible integer polynomial, \(m_w=\log M(S_w)\), and \(D=\deg S_w\).
Reciprocal inversion preserves \(D\) and \(m_w\).
We prove the uniform estimate
\[
          \log H_p(w)\ \ge\
              -C_1 D^2\log(2D)\log(2p)(1+m_w) .                       \tag{4}
\]
If \(|w|^p\le1/2\), then \(H_p(w)=|1-w^p|/|1-w|\ge1/4\).
Otherwise take the principal logarithm of \(w\) and the determination \(\log(-1)=i\pi\).
Choose an integer \(k\) with \(|p\arg(w)-2\pi k|\le\pi\).
Then \(|2k|\le p+1\), and
\(\Lambda=p\log w-2k\log(-1)\ne0\) because \(w\) is nontorsion.
Its real part is in \([-\log2,0]\) and \(|\Im\Lambda|\le\pi\).
On this rectangle \(|1-e^\Lambda|\ge c|\Lambda|\) for an absolute \(c>0\), by the identity
\((1-e^u)^2+4e^u\sin^2(v/2)=|1-e^{u+iv}|^2\), the mean-value theorem, and the sine chord bound.

Apply the [Baker–Wüstholz estimate with unrestricted height](../audits/literature/Wus02/Yin_U001.md#logarithmic-form) in \(\mathbb Q(w,-1)=\mathbb Q(w)\).
For two logarithms its constant is \(O(D^4\log(2D))\).
The field-relative logarithmic height of \(w\) in this field is \(m_w\) by the minimal-polynomial formula.
Since \(|\log w|\le\pi+\log2\), its modified height is \(O((1+m_w)/D)\).
For \(-1\) the modified height is \(\pi/D\), and the modified height of the integer form is \(O(\log(2p))\) even when \(k=0\).
Thus \(\log|\Lambda|\) has the lower bound in (4), up to an absolute constant.
The rectangle comparison and \(|1-w|\le2\) prove (4).
Only the published statement with its given determinations of logarithms and height normalization is used.

Every \(D\) is at most \(2d\) and \(m_w\le m_F\) by integral factorization.
Insert (4) and the preceding torsion bounds in (3), summing over \(2d\) roots.
This gives the lower estimate in (1).
The previously [bounded-height estimate for an algebraic unit](Yin_C_G0854_v1.md#dim16-cyclic-all-index) concerns the complete cyclic product of one irreducible polynomial.
Here the omission of the node \(1\), possible torsion factors, and height dependence in (1) are needed for arbitrary quotient-order inputs.

<a id="modular"></a>
## Divisibility on every grid orbit

For \(Q=(t-A)B_n+C\) in the chamber one has \(C\equiv B_{n-1}h\bmod B_n\) from the [trace coordinates](Yin_C_G0881_v3.md#prefix-coordinates).
The product of \(|B_{n-1}(b_j)|=\sqrt{2+b_j}\) over the full half grid is one, since \(\prod_j(2+b_j)=|B_n(-2)|=1\) by the [odd-grid formula](../ledger/Yin_L_G0464_v5.md#odd-grid-product).
Therefore \(|\operatorname{Res}(B_n,h)|=|\operatorname{Res}(B_n,Q)|=\Delta\).
Integral modular factorization gives the exact product \(\Delta=\Delta_F\Delta_G\) of positive integers by evaluation, hence \(\Delta_F\le\Delta\).
The [whole-chamber resultant bound](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) gives \(\limsup (\log\Delta_F)/n\le\log(149/100)\).
Under (2) the coefficient of \(1+m_F\) in the error of (1) tends to zero.
Moving its \(m_F\) term to the other side proves \(\limsup m_F\le\log(149/100)\), including when no initial estimate for \(m_F\) is known.

For the product assertion, suppose its measure exceeded \(149/100+\delta\) infinitely often, for some fixed \(\delta>0\).
From the given factors with positive logarithmic lift measure take successive factors until the subproduct first exceeds \(149/100+\delta/2\) in measure.
The [polylogarithmic lower bound](Yin_C_G0895_v1.md#transfer) gives \(O_\delta((\log p)^3)\) such factors even if one factor already exceeds the threshold.
Each \(\deg F_\ell\le p^{1/3-\epsilon}\); the resulting degree therefore satisfies (2).
The supplied modular factorization of the whole product yields an integral modular cofactor for the selected subproduct by including all remaining factors.
This contradicts the modular bound just proved.
Constants present in the product cause no difficulty since an integer of absolute value above one costs at least \(\log 2\).

## Assessment history

### Decision modular-trace-factor

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:00 |
| status | open |
| reason | Retain the uniform cyclic product estimate and the modular extension for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Modular divisor bound](#statement) | All odd grids, arbitrary heights, the two-sided product estimate and both modular measure conclusions. |
| argument | [Cyclic product](#circle) | Unit and nonunit roots, torsion, logarithm choice and degree and height dependence. |
| argument | [Modular norm](#modular) | Equality of the sampled norms, effective transfer to the shrinking chamber and subproducts. |
| dependency | [Unrestricted-height logarithmic form](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | External two-logarithm statement, field-relative heights, degree dependence and form coefficients. |
| dependency | [Resultant ceiling](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | All five limiting profiles, including composite grids. |
| dependency | [Earlier genuine divisor theorem](Yin_C_G0895_v1.md#decision-trace-factor-transfer-reviewed) | Wider square-root degree range, aggregate bound and degree at the sign change. |


### Decision modular-trace-factor-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T10:14 |
| status | proved |
| reason | Adopt the variable-height cyclic estimate and quotient-order factor bounds, retaining the wider genuine-divisor conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Modular divisor bound](#statement) | All odd grids, arbitrary heights, the two-sided product estimate and both modular measure conclusions. |
| argument | [Cyclic product](#circle) | Unit and nonunit roots, torsion, logarithm choice and degree and height dependence. |
| argument | [Modular norm](#modular) | Equality of the sampled norms, effective transfer to the shrinking chamber and subproducts. |
| dependency | [Unrestricted-height logarithmic form](../audits/literature/Wus02/Yin_U001.md#wus02-u001) | External two-logarithm statement, field-relative heights, degree dependence and form coefficients. |
| dependency | [Resultant ceiling](Yin_C_G0893_v1.md#decision-normalized-residue-tests-reviewed) | All five limiting profiles, including composite grids. |
| dependency | [Earlier genuine divisor theorem](Yin_C_G0895_v1.md#decision-trace-factor-transfer-reviewed) | Wider square-root degree range, aggregate bound and degree at the sign change. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v67.md#modular-trace-factor-review) | Independent verification of the exact cyclic normalization, variable degree and heights, external logarithmic form, divisibility and products. |

## Current assessment
[Selected decision](#decision-modular-trace-factor-reviewed)
