---
author: Yin
---

# A uniform bound for the positive Pisot constant on the leading-two Chebyshev path

<a id="statement"></a>
## Exclusion of the entire path

Let \(f\) be a monic Pisot minimal polynomial of positive constant \(q\ge2\), with exterior root \(\theta\).
Suppose its [interlacing numerator](Yin_C_G0345_v7.md#trace) is
\[
            C_h(x)=2U_h(x/2)-U_{h-1}(x/2),\qquad h\ge1,
\]
where \(U_h(\cos t)=\sin((h+1)t)/\sin t\).
There is an absolute constant \(Q\) such that \(q\le Q\) for all these inputs, in both degree parities.
In particular \(\theta-q\) is bounded away from zero on the entire path.
Equivalently only bounded values of \(q\) can give integer points in the [inverse simplices](../ledger/Yin_L_G0462_v43.md#inverse) with these numerators, including their odd-degree equality faces.
The proof gives no numerical value for \(Q\).

If the constants were unbounded we could choose \(q\to\infty\).
The [three-profile reduction](../ledger/Yin_L_G0462_v49.md#exclusions) and the [two endpoint exclusions](../ledger/Yin_L_G0462_v52.md#exclusions) leave only \(K=2-z\) as a subsequential limit of the normalized integer series.
We exclude that limit below.
Once \(q\) is bounded, the [exact derivative identity](../ledger/Yin_L_G0462_v36.md#second) gives \(\theta-q\ge2/(q+3)\) since the index is \(j=2\).
The main researcher and agent-S independently found the second-harmonic endpoint test and the elimination of the two binomial patterns below.
Agent-S supplied the specialization at \(i\) in the final step.

<a id="fibers"></a>
## Moment restrictions at every multiple of the first departure

For \(K=2-z\), write \(x=v+v^{-1}\), \(|v|=1\).
By the [moving harmonic comparison](../ledger/Yin_L_G0462_v52.md#harmonics) there are conditional circle probabilities with moments \(c_r(v)\), \(r\ge1\), given for almost every \(v\) by
\[
     c_r(v)=H_r(v)\frac{2-v^{-1}}{4-x},\qquad H_1\ne0 .
\]
Indeed the continuous density of the first marginal is \(2(4-x)/|2-v|^2\), and \(H_r\) is its product with \(c_r(1-v/2)\).
Each \(H_r\) is zero or an integer Laurent polynomial.
Applying the [integral shape bound](../ledger/Yin_L_G0462_v50.md#shapes) after shifting its least exponent to zero, each nonzero \(H_r\) is \(\pm v^{d_r}P_r(v)\) for an integer \(d_r\) and
\[
                        P_r=1,\quad 1-v,\quad\text{or}\quad 1+v^2 .
\]
Take these continuous representatives at every \(v\), set \(c_0=1\) and \(c_{-r}=\overline{c_r}\).
Every finite Toeplitz matrix \((c_{a-b}(v))\) is positive semidefinite almost everywhere and hence everywhere by continuity and the full support of arc length.
Consequently the sequence is the moment sequence of a circle probability \(\lambda_v\) at each \(v\), by the Herglotz theorem.

<a id="binomials"></a>
## The phase at minus one rules out every binomial

For each \(r\ge1\),
\[
              |c_{2r}-c_r^2|\le1-|c_r|^2,                              \tag{1}
\]
by integrating \((u^r-c_r)^2\) against \(\lambda_v\).
If \(P_r\) is either binomial, \(|c_r(-1)|=1\).
In (1) this requires \(P_{2r}\) to be a binomial as well, since the monomial has modulus \(1/2\) there.
Along \(v=-e^{it}\), the right side of (1) vanishes to order at least two by smoothness, nonnegativity and its zero at \(t=0\).
Thus \(c_{2r}\) and \(c_r^2\) have the same value and phase derivative there.
The factor \(2-v^{-1}=2+e^{-it}\) has phase derivative \(-1/3\), and \(4-x\) is positive.
The factors \(1-v=1+e^{it}\) and \(1+v^2=1+e^{2it}\) contribute \(1/2\) and \(1\), respectively.
The two possible phase derivatives modulo integers are therefore \(1/6\) and \(2/3\).
Doubling either gives \(1/3\) modulo integers, which is unavailable for \(c_{2r}\).
This excludes a binomial at any \(r\).

<a id="specialization"></a>
## Two circle specializations

At \(v=i\), each \(c_r(i)\) with \(r>0\) is zero or \((2+i)/4\) times a fourth root of unity.
None of those four nonzero values is real.
On all of \(\mathbb Z\), both \(4\Re c_r(i)\) and \(4\Im c_r(i)\) are integer-valued Fourier–Stieltjes transforms of finite complex measures.
Indeed the conjugate sequence is the transform of the reflection of \(\lambda_i\), so taking sums and differences gives the required transforms.
The [integer Fourier–Stieltjes theorem](../audits/literature/San20/Yin_U001.md#fourier-stieltjes) expresses each as a finite integer combination of coset indicators on \(\mathbb Z\).
Thus both sequences are periodic away from a finite set, and \(c_r(i)\) has a common period \(D\) on its positive tail.

On the progression \(r=Dl\) the eventual constant is the limit of the averages of \(c_{Dl}(i)\), equal to \(\lambda_i(\{u:u^D=1\})\) by the geometric sum and dominated convergence.
It is real and nonnegative, so the four-value restriction makes it zero.
On any other progression \(Dl+a\), the same argument identifies its eventual value with \(\int_{u^D=1}u^a\,d\lambda_i=0\).
It follows that \(c_r(i)=0\) for all sufficiently large \(r\).
Since a nonzero \(H_r\) is a monomial, it never vanishes at \(i\).
Only finitely many \(H_r\) can therefore be nonzero anywhere.

At \(v=1\), every positive-index coefficient of \(2\lambda_1\) is now \(0,1\) or \(-1\).
This measure has a nonnegative even trigonometric-polynomial density of mean two by Fourier uniqueness and the finite support of its Fourier sequence.
The [integer mean-two classification](Yin_C_G0403_v1.md#integer-mean-two-classification) permits at most one positive nonzero frequency.
Frequency one is present by \(H_1\ne0\), and specialization at one preserves every monomial.
Thus \(c_r(v)=0\) for all \(r\ge2\) and every \(v\).
The density of \(\lambda_v\) is then \(1+2\Re(c_1(v)\bar u)\), whose nonnegativity requires \(|c_1(v)|\le1/2\).
But for \(-2<x<2\),
\[
      4|c_1(v)|^2-1
         =\frac{4(5-2x)-(4-x)^2}{(4-x)^2}
         =\frac{4-x^2}{(4-x)^2}>0.
\]
This last contradiction excludes \(K=2-z\) and proves the bound.

## Assessment history

### Decision path-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T14:31 |
| status | open |
| reason | Submit the uniform constant bound on the full leading-two Chebyshev family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform bound](#statement) | Arbitrary trace degree and both degree parities in the specified family. |
| argument | [Conditional moments](#fibers) | All positive harmonics, continuous representatives and specialization at every circle point. |
| argument | [Binomial exclusion](#binomials) | Variance bound at twice the frequency and incompatible phase derivatives. |
| argument | [Two specializations](#specialization) | Eventual periodicity at a fourth root of unity, positivity of the progression means and the mean-two obstruction. |
| dependency | [Three remaining profiles](../ledger/Yin_L_G0462_v49.md#exclusions) | The initial nine-profile list after six exclusions. |
| dependency | [Harmonic comparison](../ledger/Yin_L_G0462_v52.md#harmonics) | Integral Laurent polynomials at every fixed multiple of the departure index. |
| dependency | [Two exclusions](../ledger/Yin_L_G0462_v52.md#slopes) | The two profiles with an endpoint factor. |
| dependency | [First-departure shapes](../ledger/Yin_L_G0462_v50.md#shapes) | The three admissible polynomial shapes up to sign after shifting the least exponent. |
| dependency | [Integer transforms](../audits/literature/San20/Yin_U001.md#san20-u001) | Sanders's locally compact theorem on the discrete group of integers. |
| dependency | [Mean-two symbols](Yin_C_G0403_v1.md#integer-mean-two-classification) | Classification of finite integral even nonnegative densities. |

### Decision path-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T14:47 |
| status | proved |
| reason | Adopt the uniform bound for the leading-two Chebyshev path after independent review of all three limiting series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform bound](#statement) | Arbitrary trace degree and both degree parities in the specified family. |
| argument | [Conditional moments](#fibers) | All positive harmonics, continuous representatives and specialization at every circle point. |
| argument | [Binomial exclusion](#binomials) | Variance bound at twice the frequency and incompatible phase derivatives. |
| argument | [Two specializations](#specialization) | Eventual periodicity at a fourth root of unity, positivity of the progression means and the mean-two obstruction. |
| dependency | [Three remaining profiles](../ledger/Yin_L_G0462_v49.md#exclusions) | The initial nine-profile list after six exclusions. |
| dependency | [Harmonic comparison](../ledger/Yin_L_G0462_v52.md#harmonics) | Integral Laurent polynomials at every fixed multiple of the departure index. |
| dependency | [Two exclusions](../ledger/Yin_L_G0462_v52.md#slopes) | The two profiles with an endpoint factor. |
| dependency | [First-departure shapes](../ledger/Yin_L_G0462_v50.md#shapes) | The three admissible polynomial shapes up to sign after shifting the least exponent. |
| dependency | [Integer transforms](../audits/literature/San20/Yin_U001.md#san20-u001) | [Locally compact Corollary 12.4](../audits/literature/San20/Yin_U001.md#fourier-stieltjes) on the discrete group of integers. |
| dependency | [Mean-two symbols](Yin_C_G0403_v1.md#integer-mean-two-classification) | Classification of finite integral even nonnegative densities. |
| review | [Independent path review](../audits/reviews/Yin_R_G0562_v8.md#chebyshev-path-review) | Whole path theorem, all conditional harmonics, endpoint phase identities, fourth-root specialization and resulting Pisot excess. |

## Current assessment

[Selected decision](#decision-path-reviewed)
